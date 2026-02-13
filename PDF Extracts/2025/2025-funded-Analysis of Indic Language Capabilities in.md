---
title: "2025-funded-Analysis of Indic Language Capabilities in - PDF Extract"
source_pdf: "2025-funded-Analysis of Indic Language Capabilities in.pdf"
pages: 17
extracted_at: "2026-02-13T09:15:44.897194"
---

# PDF Extract: 2025-funded-Analysis of Indic Language Capabilities in

**Source PDF:** 2025-funded-Analysis of Indic Language Capabilities in.pdf
**Total Pages:** 17

---

## Content

```
--- Page 1 ---

Analysis of Indic Language Capabilities in LLMs
AATMAN VAIDYA, Tattle Civic Tech, India
TARUNIMA PRABHAKAR, Tattle Civic Tech, India
DENNY GEORGE, Tattle Civic Tech, India
SWAIR SHAH, , India
1
Introduction
The rapid development in Large Language Models (LLMs) has resulted in state of the art performance on
various natural language processing tasks such as text summarization, machine translation and sentiment analy-
sis [35, 50, 76]. Large language models have become the dominant go-to approach towards building AI systems,
of which many are deployed through conversational interfaces. Model developers claim that these models are
multilingual. For example, OpenAI’s GPT-4, GPT-4o, Anthropic’s Claude and Meta’s Llama family of models
are popular models that were released as multilingual large language models. The technical reports of these
models demonstrate their multilingual capabilities against benchmark datasets [1, 68]. Some studies indicate that
multilingual language models can understand connections between languages, allowing them to apply word
associations and underlying grammatical rules learned from languages with more text data available to those
with the lesser data [54]. Yet, anecdotal experiences and other evaluations point to the limitations of multilingual
performance of these models [17]. As we describe in Section 3.2, LLMs are trained on a large corpus of data
crawled from the internet (e.g. C4 corpus, Books3 corpus etc.) where there is very sparse data for most spoken
languages. This raises questions about their capabilities in low-resource languages [3]. For instance, Microsoft
Bing Chat, which relies on GPT-4, could not surface words for footwear in Spanish that are locally used in Latin
America. Bing Chat also gave different and more vague answers, when the same question was translated from
English to Spanish [11, 22]. In another analysis, a model, when pushed to do more complicated tasks like logical
reasoning in Bengali it did not understand the instructions correctly. It also produced different results for Bengali
and English [23].
This report provides an analysis of the capabilities of text-based LLMs to understand and generate Indic
languages,1 with the goal of providing suggestions on which Indian languages are best positioned for inclusion
in future benchmarks datasets. There are over a hundred languages spoken in the Indian subcontinent. More
than forty of these have a million speakers but, only twenty-two languages are officially recognized in the Indian
Constitution [2, 4]. The number of real-world speakers of a language however, does not directly correlate with
the popularity of languages on the Internet. For example, Hindi- the language with the third highest number of
speakers in the world- ranks at sixty-two in terms of number of Wikipedia articles in the language [25]. This gap
between language popularity online and in the real worlds bears on the performance and safety of LLMs that are
predominantly trained on open access data.
Similar to KJ et al. [45], we divide the analysis into three parts, to understand key elements of Indic AI research
and development:
• Analysis of existing LLMs and their Indic language capabilities.
1Languages spoken in the Indian Subcontinent
*This work was funded by MLCommons to inform their work on AI Safety Benchmark, released as AI Luminate - https://mlcommons.org/
ailuminate/.
Authors’ Contact Information: Aatman Vaidya, aatman@tattle.co.in, Tattle Civic Tech, India; Tarunima Prabhakar, tarunima@tattle.co.in,
Tattle Civic Tech, India; Denny George, denny@tattle.co.in, Tattle Civic Tech, India; Swair Shah, India.
arXiv:2501.13912v1  [cs.CL]  23 Jan 2025

--- Page 2 ---

2
•
Aatman Vaidya, Tarunima Prabhakar, Denny George, and Swair Shah
• Summarization of existing evaluation studies and datasets that assess the capabilities of multilingual large
language models (MLLMs) on specific language tasks.
Figure 1 presents a structured overview of the models, datasets, and evaluation methods considered in our
analysis. We conclude by contrasting LLM capabilities in Indic languages with real-world Indic language usage
to provide suggestions on how to prioritize Indian languages for inclusion in future benchmarks.
Indic LLM Research
LLMs
Pre-Trained LLMs
GPT Family (4, 4-o, 3.5-turbo) [5], Mistral [38], Gemma Family [67]
Llama Family (3.2, 3.1, 3, 2) [28, 69], Claude 3.5 Sonnet, Mistral [38]
Gemini [66], mT5 [74], MuRIL [43], m-BERT [24], BLOOM [48]
Aya 23 [12], OpenHathi, Sarvam-1, IndicBERT [41], IndicBART [20]
Paramanu [55], XLM-R [19], Sarvam-1
Fine-Tuned LLMs
Airavata [31], Navarasa 2.0 (finetuned on Gemma)
Gajendra-v0.1 (instruction finetuned on OpenHathi)
Tamil-Llama [13], MahaMarathi-7B, Llama2-finetuned LLM - Odia language [46]
Gujju-Llama, Malayalam-Llama, Indic-Transformers [37]
AryaBhatta-GemmaOrca-Merged, Dhenu2
Evaluation
Multi-lingual
IndicGenBench [64], GLUECoS [44], MEGA [9], MEGAVERSE [10]
IndicXTREME [26], METAL [32], MAPLE [8], PARIKSHA [72]
IndicGLUE [41], Gender Biases in Multilingual Settings [70], Naamapadam [51]
Culturally Nuanced Scenarios [56], MASSIVE [29], MULTIQ [36]
Multilingual LLMs for content moderation [54], X-FACTR [39], BHASA [49]
INDICXNLI [7], IndicNLG [47], Multilingual BERT [42]
XTREME-R [62], MultiLM [18], Performance of Multilingual NLP Models [65]
Evaluation of mBERT [73]
Language and Task Specific
LLM on Odia Lang. [6] HateCheckHIn [21]
Bangla NLG [14], BenLLM-Eval [40]
Corpora
Multilingual
IndicNLP Suite [41] Samanantar [60] MASSIVE [29]
X-CLAIM [52], PMIndia [33], Vistaar [15]
XL-Sum [34], CulturaX [53], LMSYS-Chat-1M [77]
Language Specific
Indic Instruct Data [31] Universal Dependency treebank for Odia [59]
OdiEnCorp 2.0 [58]
Fig. 1. Landscape of Indic AI Research. (The structure and format has been sourced from KJ et al. [45])
2
Methodology
This report has primarily been compiled through desk research. Since information about models is distributed
across multiple sources, we scanned technical reports, announcement blogs, Hugging Face model cards, model
research papers, survey papers and company press releases. For models that support Indian languages, we conduct
a more detailed analysis using the Ecosystem Graphs framework proposed by Bommasani et al. [16] to understand
the following key attributes about the models:
• Host: Organization that created the model
• Model: Name of the model
• Date Created: When the model was released
• Size: Number of parameters of the model
• Training Dataset: Dataset(s) (source) used to pre-train/fine-tune the model
• Modality: Input and Output modalities represented in the model, i.e. text, image, video, audio etc
• Access: Describes model accessibility. Types are Open (model weights and tokenizer available to users),
Limited (paid API access), and Closed (no access).
• License: License of the model
• LLM Type: Pre-trained or Fine-tuned

--- Page 3 ---

Analysis of Indic Language Capabilities in LLMs
•
3
• Architecture: Encoder only, Encoder-Decoder or Decoder only
While there are over 400 large language models [50], we could identify only twenty-eight models that are
usable in Indian languages. Support for Indian languages was assessed from descriptions of data in technical
report, description of model capabilities on official websites, or evaluation on multilingual benchmarks by the
host organization. Models that claimed to be trained on multilingual corpus that contain Indian language data,2
or were evaluated on multilingual benchmarks were also included in our analysis. Where there are notable
differences in models within a family of models released by an organization, such as LLama or Gemma, we
include these as separate models in our analysis. We provide information on these attributes for 28 models in
Table 5 in the Appendix.
The report also provides an overview of existing evaluation datasets and methodologies for assessing LLMs
capabilities in Indian languages. We identified datasets by searching for papers on Google Scholar and ACL
Anthology with keywords associated with Indian language evaluation, and from scanning references in notable
papers on multilingual evaluation. We categorize these evaluation studies along three broad tasks, and their
sub-tasks (See Figure 2). This categorization was developed based on the tasks listed in existing literature on
evaluation of LLMs for Indian languages [9, 10]. We attempted to be comprehensive in the coverage of evaluations
as they pertain to natural language generation and understanding, but not safety.
3
Indic Language Capabilites in LLMs - An Overview
Large language models are able to support Indic languages either because they are specifically designed to work
on Indian languages through pre-training and fine-tuning, or because they are pre-trained on a multilingual
corpus thereby supporting some Indian languages as a part of broader multilingual capabilities. For clarity, we
call the former Indic language specific large language models (ILLMs), and the second multilingual large language
models (MLLMs). From the over four hundred LLMs that have been released in the last three years, we identified
only twenty-eight models that have some Indic language capabilities. These are listed in Table 5. The twenty-eight
models were developed by fourteen unique organizations. Half the models that we analyzed were developed
by the US based corporations Meta, Google and OpenAI. Five models were developed by other AI corporations
such as Mistral, Anthropic, and Cohere. Five models were developed by three India based corporations. Barring
BLOOM which was developed by the Big Science consortium, the remaining were developed by research labs in
India. Below we provide an overview of the capabilities of models in different Indic languages:
3.1
Indic Language Specific Language Models
Ten models of the twenty-eight we analyzed were specifically pre-trained or fine-tuned to work on an Indian
language. Hindi, the most widely spoken Indic language, was covered by all the ten models. In addition to Hindi,
most models also claim capabilities on nine other Indian languages.
• MuRIL by [43] is pre-trained on 17 Indian languages and their transliterated counterparts. This is developed
by Google Research India. The model is pre-trained from scratch using data from sources like Wikipedia,
Common Crawl, PMINDIA [33] and Dakshina [61].
• The Indian startup Sarvam has developed a number of models focused on Indic languages. Below we list
the language coverage in their text based models:
– OpenHathi model, is pre-trained from scratch in Hindi, English, and Indian English. However, as
with many models we analyzed, information about the training data is not publicly available.
– Sarvam 1 and its precursor Sarvam-2b-v0.5 is pretrained on language tokens for ten languages-
Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Oriya, Punjabi, Tamil, and Telugu [63]. Due
2not necessarily optimized for state of the art of multilingual performance

--- Page 4 ---

4
•
Aatman Vaidya, Tarunima Prabhakar, Denny George, and Swair Shah
to limited availability of good quality of Indic language data [41], the team developed a specialized
training corpus of 2 trillion tokens using synthetic data-generation techniques.
• AryaBhatta-GemmaGenZ-Vikas-Merged, developed by GenVR Research, is finetuned on Gemma and sup-
ports nine Indian languages: Hindi, Tamil, Punjabi, Bengali, Gujarati, Oriya, Telugu, Kannada, Malayalam
• Open Aditi v4 and Gajendra-v0.1 are two other models that support Hindi and Hindi-English. Gajendra
was finetuned on OpenHathi.
• Airavata by Gala et al. [31] is finetuned on Indic Instruct dataset. This dataset is a collection of instruction
datasets (Anudesh, wikiHow, Flan v2, Dolly, Anthropic-HHH, OpenAssistant v1, and LymSys-Chat).
3.2
Multilingual Large Language Models
Several models, while not specific about supporting Indian languages, do claim to be multilingual. These models
have been evaluated for Indic language performance or have been used in building Indian languages specific
applications. While information on training data is not available for many of these models,3 analysing the Indic
language composition of commonly used open access repositories in training provides some indication of the
relative capabilities of MLLMs to support different Indic languages. Below we list the composition of Indian
languages in some widely used training datesets:
• Wikipedia: is an online encyclopedic repository in 332 languages. As an open access repository, data
from Wikipedia is commonly used for training language models. In Table 1, we present the percentage
distribution of articles available in Indian languages on Wikipedia.
• Common Crawl: This is a collection of web archives consisting of terabytes of data. Common Crawl is a
nonprofit organization that crawls the web and freely provides its archives and datasets to the public, it
also includes data from Wikipedia. While Common Crawl provides a multilingual dataset, the majority of
its content is in English. Indian languages such as Hindi, Tamil, Bengali, Telugu, Marathi, and Gujarati
comprise only about 0.5% of the total data [30]. In Table 2 we list the percentage distribution of Indian
languages in the Common Crawl dataset.
• Multilingual Colossal Clean Crawled Corpus (C4): This is a processed version of the Common Crawl
created by Google, specifically for training MLLMs. It includes data for 101 languages of which Indian
languages make up 7.72% of the data [75].
Some organizations supplement these with additional open access repositories, in part, to build language
specific capabilities. Here we note that Indic languages are usually not prioritized in these efforts. If an Indic
language is selected at all, it is Hindi. For example, Llama 3.1 is trained on a custom dataset of 15T multilingual
tokens from publicly available sources to support seven languages in addition to English, with Hindi being the
only Indic language. Similarly, the Command R model by Cohere was updated with additional pre-training data
for Hindi, among thirteen other global languages. Aya 23, which is an instruction fine-tuned on the Command
model with support for 23 languages, also only covers Hindi among Indic languages.
3.3
License and Access
Our ability to analyze Indic language capabilities, as well as the ability of model and application developers to
build in Indic languages is shaped by the license under which the models and dataset are released. All the models
we analyzed were either open-access and limited-access models. 4 See Table 5. For a majority of the models, model
weights and tokenizers can be accessed through model cards on Hugging Face and GitHub. The source code and
weights for Mistral, T5, mT5, Muril, Ganga 1B are available under permissive open-source licenses like Apache
2.0. The Cohere models are released under a Creative Commons license. The weight for Meta’s Llama models are
3Information on training data used was only available for seventeen of the twenty-eight models
4This refers strictly to ability to access, not the ability to inspect, modify or share the model

--- Page 5 ---

Analysis of Indic Language Capabilities in LLMs
•
5
Langauge
Percentage of
Articles (%)
Langauge
Percentage of
Articles (%)
Urdu
0.336
Assamese
0.022
Tamil
0.265
Maithili
0.022
Hindi
0.256
Sanskrit
0.019
Bengali
0.25
Santali
0.018
Telugu
0.159
Bihari (Bhojpuri)
0.014
Marathi
0.154
Central Tibetan (Lhasa Tibetan)
0.011
Malayalam
0.135
Kashmiri
0.009
Western Punjabi
0.115
Konkani (Goan Konkani)
0.006
Punjabi
0.086
Pali
0.004
Kannada
0.052
Awadhi
0.004
Gujarati
0.048
Tulu
0.004
Odia
0.029
Dzongkha
0.00051
Sindhi
0.029
Total
2.047
Table 1. Distribution of number of Articles in Indian Languages on Wikipedia
Langauge
Percentage (%)
Langauge
Distribution (%)
Hindi
0.1967
Marathi
0.0241
Bengali
0.1075
Telugu
0.0181
Tamil
0.0439
Kannada
0.0145
Urdu
0.0298
Gujarati
0.0113
Malayalam
0.0244
Assamese
0.0023
Total
0.4726
Table 2. Distribution of Indian Languages in the Common Crawl Dataset
released under the Llama License and the code is released under GPLv3. Models like OpenHathi, Airavata, and
Gajendra-v0.1 are fine-tuned on Llama, thereby inheriting its license. Similarly Navarasa 2.0 inherits its license
from Gemma, the model it is finetuned on. Sarvam 1 model has been released under a custom Sarvam AI Research
license. In Section 3.2 we describe the datasets used to train the models. We however note that barring a few
exceptions such as MuRIL and Airavata, most models do not release their data under and an open data license.
4
Evaluation Studies
The overall performance of Large language models is evaluated by assessing their reliability, robustness, and
effectiveness on a range of tasks. A comprehensive evaluation not only helps measure a model’s capabilities
but also highlights areas that require further improvement. Popular LLMs like GPT and Llama report scores on
well-rounded large benchmark datasets such as HELM, BIG-Bench, MMLU, MATH, and HellaSwag etc, which
provide insights into their general performance across multiple domains [57]. These benchmarks however don’t
evaluate language specific performance, and also don’t account for context specific usage of LLMs. This has
led some groups to develop Indic language specific evaluation datasets In this section, we summarize existing
evaluation datasets and methods for Indic language performance of LLMs. Please note that the LLMs covered in

--- Page 6 ---

6
•
Aatman Vaidya, Tarunima Prabhakar, Denny George, and Swair Shah
Fig. 2. Evaluation Tasks
the evaluation papers may differ from the 28 models analyzed in the previous section.
To evaluate LLMs effectively, it is essential to assess their core abilities, specifically their capacity to understand
and generate natural language text. This ability is assessed through a number of smaller tasks. In Figure 2
we present a small taxonomy of evaluation tasks and their sub-tasks. As illustrated, the evaluation tasks can
be broadly categorized into three main domains: Natural Language Understanding, Natural Language
Generation, and Safety, each with multiple sub-tasks:
• Natural Language Understanding refers to LLMs’ ability to comprehend and interpret human language.
It involves processing the input text to extract meaning, context, and underlying relationships between
words. There are several tasks that fall under this, such as Natural Language Inference, Text Classification,
Sentiment Analysis, Name-Entity Recognition (NER)5 and POS Tagging 6.
• Natural Language Generation is the ability of LLMs’ to generate text based on a given input. Some key
tasks that fall under it are Translation, which is a models ability to convert text from one language to the
other, Summarization, Question-Answering, Image Captioning etc.
• Safety focuses on the crucial evaluation of the ethical and safety aspects of LLMs.
Since the goal of the report is to provide suggestions on which Indic language should be included in future
safety benchmark datasets, we preclude an analysis of trust and safety datasets relevant to Indic languages. The
following is a summarization of model performance on natural language understanding and generation.
4.1
Summary of Model Evaluations
We found fourteen papers that evaluated an LLM against one or more Indic languages. A detailed description of
the papers can be found in Section B of the Appendix. We note that a majority of these datasets are a direct
translation of existing English datasets which is a serious limitation. For example, while models might score well
on some of these datasets, they may fare poorly on tasks where socio-cultural understanding is required [71].
The following analysis should be read alongside a recognition of this limitation in existing evaluation datasets.
• Language Distribution in Evaluation Datasets: In Table 3 we list the languages covered in existing
evaluation studies across tasks. Except for the work by Singh et al. [64], we observed that all other datasets
primarily support a maximum of the 12 most widely spoken Indian languages.
5NER is a process of identifying and classifying named entities (people, objects, locations) in text
6POS tagging is a way to tag different parts of speech such as noun, verb, adjective, pronoun, prepositions in an given text.

--- Page 7 ---

Analysis of Indic Language Capabilities in LLMs
•
7
Tasks
Sub-Tasks
Languages Covered
Papers Referenced
Natural Language
Understanding
Natural Language
Inference
Hindi, Bengali, Punjabi, Kannada, Gujarati, Malayalam,
Marathi, Telugu, Tamil, Oriya,
Assamese, code-mixed English-Hindi, Nepali
Ahuja et al. [9],
Doddapaneni et al. [26],
Aggarwal et al. [7]
Text Classification
Hindi, Kannada, Malayalam, Marathi, Tamil, Telugu,
Urdu, Bengali, Gujarati,
Assamese, Odia, Punjabi
Doddapaneni et al. [26],
Kakwani et al. [41]
Name-Entity
Recognition
Urdu, Tamil, Telugu, Hindi, Gujarati, Malayalam,
Marathi, Punjabi, Bengali, Kannada
Ahuja et al. [9],
Doddapaneni et al. [26],
Kakwani et al. [41]
Natural Language
Generation
Translation
Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi,
Tamil, Telugu, Urdu, Assamese, Bhojpuri, Nepali,
Odia, Punjabi, Pashto, Sanskrit, Awadhi, Haryanvi, Tibetan,
Bodo, Garhwali, Konkani, Chhattisgarhi, Rajasthani,
Maithili, Manipuri, Malvi, Marwari, Santali
Singh et al. [64]
Summarization
Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi,
Tamil, Telugu, Urdu, Assamese, Bhojpuri, Nepali,
Odia, Punjabi, Pashto, Sanskrit, Awadhi, Haryanvi, Tibetan,
Bodo, Garhwali, Konkani, Chhattisgarhi, Rajasthani,
Maithili, Manipuri, Malvi, Marwari, Santali
Singh et al. [64],
Ahuja et al. [9],
Hada et al. [32],
Kumar et al. [47]
Question-Answering
Bengali, Gujarati, Hindi, Kannada, Malayalam,
Marathi, Tamil, Telugu, Urdu, Assamese, Odia, Punjabi
Singh et al. [64],
Ahuja et al. [9],
Doddapaneni et al. [26],
Kakwani et al. [41]
Image Captioning
Bengali, Hindi, Telugu
Ahuja et al. [10]
Table 3. Tasks and Languages Covered in Existing Evaluation Datasets
– These are Hindi, Bengali, Gujarati, Kannada, Malayalam, Marathi, Tamil, Telugu, Urdu, Assamese,
Odia and Punjabi.
• Performance of LLMs: To understand the relative capabilities of the models in Indic languages, we
categorize the twelve languages in three broad buckets of high, medium and low (See Table 4). This
ranking should not be treated as a universal ranking- there is a significant performance gap in
LLMs between English and Indian languages on natural language understanding and generation
tasks. The rankings in Table 4 are relative to each other.
While it is difficult to summarize the performance of languages across all evaluation datasets, models and
sub-tasks, we provide a high-level approximation of the performance of the models on natural language
understanding and generation tasks. A language was labeled as high performing on a task if it consistently
ranked at the top or had scores similar to the highest ranked language, across a majority of models. A
language was labeled as medium performing, if it had average performance on most sub-tasks, on a
majority models. A language was labeled as low performing, if it has poor scores across most sub-tasks
on a majority of models. We identify that LLMs shows relatively high performance on six Indic languages,
medium on four and low on two of the twelve. We also note that:
– The performance gap between high and low resource languages is because of a lack of good quality
and quantity of pre-training data. This has led some developers to create and use synthetic data.
– Doddapaneni et al. [27] in reviewing performance of LLMs on twenty Indian languages notice a
sharp decline in performance of extremely low resource languages such as Sindhi and Santhali. They
also attribute this performance gap to the lack of a shared script among languages, and absence of
linguistic cousin in the corpus to act as a bridge for effective transfer.

--- Page 8 ---

8
•
Aatman Vaidya, Tarunima Prabhakar, Denny George, and Swair Shah
Langauge
Performance of LLM on Tasks
Number of
Speakers in India
Understanding
Generation
Evaluation Studies
Referenced
Hindi
high
high
Singh et al. [64], Ahuja et al. [9], Aggarwal et al. [7],
Doddapaneni et al. [26], Kakwani et al. [41]
528,347,193
Bengali
high
high
97,237,669
Marathi
high
high
83,026,680
Telugu
high
high
81,127,740
Tamil
high
high
69,026,881
Gujarati
medium
medium
55,492,554
Urdu
high
high
Singh et al. [64], Ahuja et al. [9], Doddapaneni et al. [26]
50,772,631
Kannada
medium
medium
Singh et al. [64], Ahuja et al. [9], Aggarwal et al. [7],
Doddapaneni et al. [26], Kakwani et al. [41]
43,706,512
Oriya
low
low
37,521,324
Malayalam
medium
medium
34,838,819
Punjabi
low
low
33,124,726
Assamese
medium
medium
15,311,351
Table 4. Overall Performance of LLMs on Evaluation Tasks for Indian Languages
5
Prioritizing Languages for Inclusion in Benchmarks
The goal for this report was to provide an overview of Indic language capabilities of prominent LLMs and to
suggest languages that should be included in future safety benchmarks. The prior sections provide an overview
of the technical capabilities of the models. We note, however, that the performance of models in a language is
not directly correlated with the number of people who speak the language. While models show good language
generation and understanding in the five most widely spoken languages in India- Hindi, Bengali, Marathi, Telugu
and Tamil- the performance for other languages is less predictable. As Table 4 shows, Oriya while having more
speakers than Malayalam and Assamese, performs worse.
Based on Table 4 Hindi, Bengali, Marathi, Telugu and Tamil emerge as natural candidates for inclusion in
safety benchmarks.7 For these languages, the model capabilities dovetail the number of language speakers in
the country. Beyond this, however, the selection criteria becomes more complicated. The performance of the
model in a language may be low. Yet, the number of people using the model in the language may be higher and
therefore repercussion from unsafe usage might be greater.8. Model performance on specific languages might
also rapidly change with the availability of newer datasets in the language. At this stage we find it difficult to
unequivocally recommend languages beyond the five most widely spoken in India.
Acknowledgments
This report provides an analysis of the capabilities of text-based LLMs to understand and generate Indic languages
with the goal of providing suggestions on which Indian languages are best positioned for inclusion in future
benchmarks datasets by MLCommons. This work is supported and funded by MLCommons.
References
[1] [n. d.]. Introducing Llama 3.1: Our most capable models to date — ai.meta.com. https://ai.meta.com/blog/meta-llama-3-1/.
[2] 2011. Paper 1 of 2018 on Language, Table C-16, Census of India 2011.
https://censusindia.gov.in/nada/index.php/catalog/42458/
download/46089/C-16_25062018.pdf
[3] 2022. https://community.openai.com/t/chatgpt-spanish-support/24706/3
7Hindi is already included in v1 AI safety benchmark released by MLCommons
8This gap between language speakers and model capabilities can be addressed by model developers but is out of scope for the MLCommons’
AI Safety Working Group

--- Page 9 ---

Analysis of Indic Language Capabilities in LLMs
•
9
[4] 2024. Rajbhasha Vibhag, Ministry of Home Affairs. https://rajbhasha.gov.in/en/languages-included-eighth-schedule-indian-constitution
[5] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt,
Sam Altman, Shyamal Anadkat, et al. 2023. Gpt-4 technical report. arXiv preprint arXiv:2303.08774 (2023).
[6] Parul Agarwal, Aisha Asif, Shantipriya Parida, Sambit Sekhar, Satya Ranjan Dash, and Subhadarshi Panda. 2023. Generative Chatbot
Adaptation for Odia Language: A Critical Evaluation. In 2023 1st International Conference on Circuits, Power and Intelligent Systems
(CCPIS). 1–7. https://doi.org/10.1109/CCPIS59145.2023.10291329
[7] Divyanshu Aggarwal, Vivek Gupta, and Anoop Kunchukuttan. 2022. IndicXNLI: Evaluating Multilingual Inference for Indian Languages.
arXiv:2204.08776 [cs.CL]
[8] Divyanshu Aggarwal, Ashutosh Sathe, and Sunayana Sitaram. 2024. Maple: Multilingual evaluation of parameter efficient finetuning of
large language models. arXiv preprint arXiv:2401.07598 (2024).
[9] Kabir Ahuja, Harshita Diddee, Rishav Hada, Millicent Ochieng, Krithika Ramesh, Prachi Jain, Akshay Nambi, Tanuja Ganu, Sameer
Segal, Maxamed Axmed, et al. 2023. Mega: Multilingual evaluation of generative ai. arXiv preprint arXiv:2303.12528 (2023).
[10] Sanchit Ahuja, Divyanshu Aggarwal, Varun Gumma, Ishaan Watts, Ashutosh Sathe, Millicent Ochieng, Rishav Hada, Prachi Jain,
Maxamed Axmed, Kalika Bali, et al. 2023. Megaverse: Benchmarking large language models across languages, modalities, models and
tasks. arXiv preprint arXiv:2311.07463 (2023).
[11] Murtaza Ali, Sourojit Ghosh, Prerna Rao, Raveena Dhegaskar, Sophia Jawort, Alix Medler, Mengqi Shi, and Sayamindu Dasgupta.
2023. Taking Stock of Concept Inventories in Computing Education: A Systematic Literature Review. In Proceedings of the 2023 ACM
Conference on International Computing Education Research V.1 (ICER 2023). ACM, 397–415. https://doi.org/10.1145/3568813.3600120
[12] Viraat Aryabumi, John Dang, Dwarak Talupuru, Saurabh Dash, David Cairuz, Hangyu Lin, Bharat Venkitesh, Madeline Smith, Jon Ander
Campos, Yi Chern Tan, Kelly Marchisio, Max Bartolo, Sebastian Ruder, Acyr Locatelli, Julia Kreutzer, Nick Frosst, Aidan Gomez, Phil
Blunsom, Marzieh Fadaee, Ahmet Üstün, and Sara Hooker. 2024. Aya 23: Open Weight Releases to Further Multilingual Progress.
arXiv:2405.15032 [cs.CL] https://arxiv.org/abs/2405.15032
[13] Abhinand Balachandran. 2023. Tamil-llama: A new tamil language model based on llama 2. arXiv preprint arXiv:2311.05845 (2023).
[14] Abhik Bhattacharjee, Tahmid Hasan, Wasi Uddin Ahmad, and Rifat Shahriyar. 2023. BanglaNLG and BanglaT5: Benchmarks and
Resources for Evaluating Low-Resource Natural Language Generation in Bangla. In Findings of the Association for Computational
Linguistics: EACL 2023, Andreas Vlachos and Isabelle Augenstein (Eds.). Association for Computational Linguistics, Dubrovnik, Croatia,
726–735. https://doi.org/10.18653/v1/2023.findings-eacl.54
[15] Kaushal Santosh Bhogale, Sai Sundaresan, Abhigyan Raman, Tahir Javed, Mitesh M. Khapra, and Pratyush Kumar. 2023. Vistaar: Diverse
Benchmarks and Training Sets for Indian Language ASR. arXiv:2305.15386 [cs.CL]
[16] Rishi Bommasani, Dilara Soylu, Thomas I Liao, Kathleen A Creel, and Percy Liang. 2023. Ecosystem graphs: The social footprint of
foundation models. arXiv preprint arXiv:2303.15772 (2023).
[17] Govind Choudhary. 2023.
Chatgpt now speaks Hindi, Assamese, Bengali and other Indian languages!
https:
//www.livemint.com/technology/apps/chatgpt-now-speaks-hindi-assamese-bengali-and-other-indian-languages-heres-how-
to-get-replies-in-local-languages-11687948693940.html
[18] Monojit Choudhury and Amit Deshpande. 2021. How Linguistically Fair are Multilingual Pre-Trained Language Models?. In AAAI-21.
AAAI, AAAI. https://www.microsoft.com/en-us/research/publication/how-linguistically-fair-are-multilingual-pre-trained-language-
models/
[19] A Conneau. 2019. Unsupervised cross-lingual representation learning at scale. arXiv preprint arXiv:1911.02116 (2019).
[20] Raj Dabre, Himani Shrotriya, Anoop Kunchukuttan, Ratish Puduppully, Mitesh M Khapra, and Pratyush Kumar. 2021. IndicBART: A
pre-trained model for indic natural language generation. arXiv preprint arXiv:2109.02903 (2021).
[21] Mithun Das, Punyajoy Saha, Binny Mathew, and Animesh Mukherjee. 2022. HateCheckHIn: Evaluating Hindi Hate Speech Detection
Models. arXiv:2205.00328 [cs.CL]
[22] Paresh Dave. 2023. ChatGPT Is Cutting Non-English Languages Out of the AI Revolution. Wired (2023). https://www.wired.com/story/
chatgpt-non-english-languages-ai-revolution/
[23] Andrew Deck. 2023. We tested ChatGPT in Bengali, Kurdish, and Tamil. it failed.
https://restofworld.org/2023/chatgpt-problems-
global-language-testing/
[24] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pre-training of Deep Bidirectional Transformers for
Language Understanding. arXiv:1810.04805 [cs.CL] https://arxiv.org/abs/1810.04805
[25] Martin Dittus and Mark Graham. 2019. The Language Geography of Wikipedia. https://internetlanguages.org/en/numbers/wikipedia-
language-geography/
[26] Sumanth Doddapaneni, Rahul Aralikatte, Gowtham Ramesh, Shreya Goyal, Mitesh M Khapra, Anoop Kunchukuttan, and Pratyush
Kumar. 2022. Towards leaving no indic language behind: Building monolingual corpora, benchmark and models for indic languages.
arXiv preprint arXiv:2212.05409 (2022).
[27] Sumanth Doddapaneni, Rahul Aralikatte, Gowtham Ramesh, Shreya Goyal, Mitesh M. Khapra, Anoop Kunchukuttan, and Pratyush
Kumar. 2023. Towards Leaving No Indic Language Behind: Building Monolingual Corpora, Benchmark and Models for Indic Languages.

--- Page 10 ---

10
•
Aatman Vaidya, Tarunima Prabhakar, Denny George, and Swair Shah
arXiv:2212.05409 [cs.CL]
[28] Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten,
Amy Yang, Angela Fan, et al. 2024. The llama 3 herd of models. arXiv preprint arXiv:2407.21783 (2024).
[29] Jack FitzGerald, Christopher Hench, Charith Peris, Scott Mackie, Kay Rottmann, Ana Sanchez, Aaron Nash, Liam Urbach, Vishesh
Kakarala, Richa Singh, et al. 2022. Massive: A 1m-example multilingual natural language understanding dataset with 51 typologically-
diverse languages. arXiv preprint arXiv:2204.08582 (2022).
[30] Common Crawl Foundation. [n. d.]. Statistics of Common Crawl–Distribution of Languages. https://commoncrawl.github.io/cc-crawl-
statistics/plots/languages.
[31] Jay Gala, Thanmay Jayakumar, Jaavid Aktar Husain, Mohammed Safi Ur Rahman Khan, Diptesh Kanojia, Ratish Puduppully, Mitesh M
Khapra, Raj Dabre, Rudra Murthy, Anoop Kunchukuttan, et al. 2024. Airavata: Introducing hindi instruction-tuned llm. arXiv preprint
arXiv:2401.15006 (2024).
[32] Rishav Hada, Varun Gumma, Mohamed Ahmed, Kalika Bali, and Sunayana Sitaram. 2024. METAL: Towards Multilingual Meta-Evaluation.
arXiv preprint arXiv:2404.01667 (2024).
[33] Barry Haddow and Faheem Kirefu. 2020. PMIndia – A Collection of Parallel Corpora of Languages of India. arXiv:2001.09907 [cs.CL]
[34] Tahmid Hasan, Abhik Bhattacharjee, Md Saiful Islam, Kazi Samin, Yuan-Fang Li, Yong-Bin Kang, M. Sohel Rahman, and Rifat Shahriyar.
2021. XL-Sum: Large-Scale Multilingual Abstractive Summarization for 44 Languages. arXiv:2106.13822 [cs.CL]
[35] Amr Hendy, Mohamed Abdelrehim, Amr Sharaf, Vikas Raunak, Mohamed Gabr, Hitokazu Matsushita, Young Jin Kim, Mohamed Afify,
and Hany Hassan Awadalla. 2023. How good are GPT models at machine translation? A comprehensive evaluation. arXiv. arXiv preprint
arXiv:2302.09210 (2023).
[36] Carolin Holtermann, Paul Röttger, Timm Dill, and Anne Lauscher. 2024. Evaluating the Elementary Multilingual Capabilities of Large
Language Models with MultiQ. arXiv:2403.03814 [cs.CL]
[37] Kushal Jain, Adwait Deshpande, Kumar Shridhar, Felix Laumann, and Ayushman Dash. 2020. Indic-Transformers: An Analysis of
Transformer Language Models for Indian Languages. arXiv:2011.02323 [cs.CL] https://arxiv.org/abs/2011.02323
[38] Albert Q Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand,
Gianna Lengyel, Guillaume Lample, Lucile Saulnier, et al. 2023. Mistral 7B. arXiv preprint arXiv:2310.06825 (2023).
[39] Zhengbao Jiang, Antonios Anastasopoulos, Jun Araki, Haibo Ding, and Graham Neubig. 2020. X-FACTR: Multilingual Factual Knowledge
Retrieval from Pretrained Language Models. arXiv:2010.06189 [cs.CL]
[40] Mohsinul Kabir, Mohammed Saidul Islam, Md Tahmid Rahman Laskar, Mir Tafseer Nayeem, M Saiful Bari, and Enamul Hoque.
2024.
BenLLMEval: A Comprehensive Evaluation into the Potentials and Pitfalls of Large Language Models on Bengali NLP.
arXiv:2309.13173 [cs.CL]
[41] Divyanshu Kakwani, Anoop Kunchukuttan, Satish Golla, NC Gokul, Avik Bhattacharyya, Mitesh M Khapra, and Pratyush Kumar. 2020.
IndicNLPSuite: Monolingual corpora, evaluation benchmarks and pre-trained multilingual language models for Indian languages. In
Findings of the Association for Computational Linguistics: EMNLP 2020. 4948–4961.
[42] Nora Kassner, Philipp Dufter, and Hinrich Schütze. 2021. Multilingual LAMA: Investigating Knowledge in Multilingual Pretrained
Language Models. arXiv:2102.00894 [cs.CL]
[43] Simran Khanuja, Diksha Bansal, Sarvesh Mehtani, Savya Khosla, Atreyee Dey, Balaji Gopalan, Dilip Kumar Margam, Pooja Aggarwal,
Rajiv Teja Nagipogu, Shachi Dave, et al. 2021. Muril: Multilingual representations for indian languages. arXiv preprint arXiv:2103.10730
(2021).
[44] Simran Khanuja, Sandipan Dandapat, Anirudh Srinivasan, Sunayana Sitaram, and Monojit Choudhury. 2020. GLUECoS: An evaluation
benchmark for code-switched NLP. arXiv preprint arXiv:2004.12376 (2020).
[45] Sankalp KJ, Vinija Jain, Sreyoshi Bhaduri, Tamoghna Roy, and Aman Chadha. 2024. Decoding the Diversity: A Review of the Indic AI
Research Landscape. arXiv:2406.09559 [cs.CL] https://arxiv.org/abs/2406.09559
[46] Guneet S Kohli, Shantipriya Parida, Sambit Sekhar, Samirit Saha, Nipun B Nair, Parul Agarwal, Sonal Khosla, Kusumlata Patiyal, and
Debasish Dhal. 2023. Building a llama2-finetuned llm for odia language utilizing domain knowledge instruction set. In Proceedings of
the Third International Conference on AI-ML Systems. 1–7.
[47] Aman Kumar, Himani Shrotriya, Prachi Sahu, Raj Dabre, Ratish Puduppully, Anoop Kunchukuttan, Amogh Mishra, Mitesh M. Khapra, and
Pratyush Kumar. 2022. IndicNLG Benchmark: Multilingual Datasets for Diverse NLG Tasks in Indic Languages. arXiv:2203.05437 [cs.CL]
[48] Teven Le Scao, Angela Fan, Christopher Akiki, Ellie Pavlick, Suzana Ilić, Daniel Hesslow, Roman Castagné, Alexandra Sasha Luccioni,
François Yvon, Matthias Gallé, et al. 2023. Bloom: A 176b-parameter open-access multilingual language model. (2023).
[49] Wei Qi Leong, Jian Gang Ngui, Yosephine Susanto, Hamsawardhini Rengarajan, Kengatharaiyer Sarveswaran, and William Chandra Tjhi.
2023. BHASA: A Holistic Southeast Asian Linguistic and Cultural Evaluation Suite for Large Language Models. arXiv:2309.06085 [cs.CL]
[50] David McCandless. 2024. The rise of Generative AI large language models (llms) like chatgpt.
https://informationisbeautiful.net/
visualizations/the-rise-of-generative-ai-large-language-models-llms-like-chatgpt/
[51] Arnav Mhaske, Harshit Kedia, Sumanth Doddapaneni, Mitesh M Khapra, Pratyush Kumar, Rudra Murthy V, and Anoop Kunchukuttan.
2022. Naamapadam: a large-scale named entity annotated data for Indic languages. arXiv preprint arXiv:2212.10168 (2022).

--- Page 11 ---

Analysis of Indic Language Capabilities in LLMs
•
11
[52] Shubham Mittal, Megha Sundriyal, and Preslav Nakov. 2023. Lost in Translation, Found in Spans: Identifying Claims in Multilingual
Social Media. arXiv:2310.18205 [cs.CL]
[53] Thuat Nguyen, Chien Van Nguyen, Viet Dac Lai, Hieu Man, Nghia Trung Ngo, Franck Dernoncourt, Ryan A. Rossi, and Thien Huu Nguyen.
2023. CulturaX: A Cleaned, Enormous, and Multilingual Dataset for Large Language Models in 167 Languages. arXiv:2309.09400 [cs.CL]
[54] Gabriel Nicholas and Aliya Bhatia. 2023.
Lost in Translation: Large Language Models in Non-English Content Analysis.
arXiv:2306.07377 [cs.CL]
[55] Mitodru Niyogi and Arnab Bhattacharya. 2024. Paramanu: A Family of Novel Efficient Indic Generative Foundation Language Models.
arXiv preprint arXiv:2401.18034 (2024).
[56] Millicent Ochieng, Varun Gumma, Sunayana Sitaram, Jindong Wang, Keshet Ronen, Kalika Bali, and Jacki O’Neill. 2024. Beyond Metrics:
Evaluating LLMs’ Effectiveness in Culturally Nuanced, Low-Resource Real-World Scenarios. arXiv preprint arXiv:2406.00343 (2024).
[57] OpenAI. 2024. Hello GPT-4o. https://openai.com/index/hello-gpt-4o/.
[58] Shantipriya Parida, Satya Ranjan Dash, Ondřej Bojar, Petr Motlicek, Priyanka Pattnaik, and Debasish Kumar Mallick. 2020. OdiEnCorp
2.0: Odia-English Parallel Corpus for Machine Translation. In Proceedings of the WILDRE5– 5th Workshop on Indian Language Data:
Resources and Evaluation, Girish Nath Jha, Kalika Bali, Sobha L., S. S. Agrawal, and Atul Kr. Ojha (Eds.). European Language Resources
Association (ELRA), Marseille, France, 14–19. https://aclanthology.org/2020.wildre-1.3
[59] Shantipriya Parida, Kalyanamalini Sahoo, Atul Kr. Ojha, Saraswati Sahoo, Satya Ranjan Dash, and Bijayalaxmi Dash. 2022. Universal
Dependency Treebank for Odia Language. arXiv:2205.11976 [cs.CL]
[60] Gowtham Ramesh, Sumanth Doddapaneni, Aravinth Bheemaraj, Mayank Jobanputra, Raghavan Ak, Ajitesh Sharma, Sujit Sahoo,
Harshita Diddee, Divyanshu Kakwani, Navneet Kumar, et al. 2022. Samanantar: The largest publicly available parallel corpora collection
for 11 indic languages. Transactions of the Association for Computational Linguistics 10 (2022), 145–162.
[61] Brian Roark, Lawrence Wolf-Sonkin, Christo Kirov, Sabrina J. Mielke, Cibu Johny, Isin Demirsahin, and Keith Hall. 2020. Processing
South Asian Languages Written in the Latin Script: the Dakshina Dataset. In Proceedings of the Twelfth Language Resources and Evaluation
Conference, Nicoletta Calzolari, Frédéric Béchet, Philippe Blache, Khalid Choukri, Christopher Cieri, Thierry Declerck, Sara Goggi,
Hitoshi Isahara, Bente Maegaard, Joseph Mariani, Hélène Mazo, Asuncion Moreno, Jan Odijk, and Stelios Piperidis (Eds.). European
Language Resources Association, Marseille, France, 2413–2423. https://aclanthology.org/2020.lrec-1.294
[62] Sebastian Ruder, Noah Constant, Jan Botha, Aditya Siddhant, Orhan Firat, Jinlan Fu, Pengfei Liu, Junjie Hu, Dan Garrette, Graham
Neubig, and Melvin Johnson. 2021. XTREME-R: Towards More Challenging and Nuanced Multilingual Evaluation. In Proceedings
of the 2021 Conference on Empirical Methods in Natural Language Processing, Marie-Francine Moens, Xuanjing Huang, Lucia Specia,
and Scott Wen-tau Yih (Eds.). Association for Computational Linguistics, Online and Punta Cana, Dominican Republic, 10215–10245.
https://doi.org/10.18653/v1/2021.emnlp-main.802
[63] Sarvam. 2024. Sarvam 1. https://www.sarvam.ai/blogs/sarvam-1
[64] Harman Singh, Nitish Gupta, Shikhar Bharadwaj, Dinesh Tewari, and Partha Talukdar. 2024. IndicGenBench: A Multilingual Benchmark
to Evaluate Generation Capabilities of LLMs on Indic Languages. arXiv preprint arXiv:2404.16816 (2024).
[65] Anirudh Srinivasan, Sunayana Sitaram, Tanuja Ganu, Sandipan Dandapat, Kalika Bali, and Monojit Choudhury. 2021. Predicting the
Performance of Multilingual NLP Models. arXiv:2110.08875 [cs.CL]
[66] Gemini Team, Rohan Anil, Sebastian Borgeaud, Yonghui Wu, Jean-Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Schalkwyk, Andrew M
Dai, Anja Hauth, et al. 2023. Gemini: a family of highly capable multimodal models. arXiv preprint arXiv:2312.11805 (2023).
[67] Gemma Team, Morgane Riviere, Shreya Pathak, Pier Giuseppe Sessa, Cassidy Hardin, Surya Bhupatiraju, Léonard Hussenot, Thomas
Mesnard, Bobak Shahriari, Alexandre Ramé, et al. 2024. Gemma 2: Improving open language models at a practical size. arXiv preprint
arXiv:2408.00118 (2024).
[68] Mistral Team. 2023. Mixtral of experts. https://mistral.ai/news/mixtral-of-experts/
[69] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal
Bhargava, Shruti Bhosale, et al. 2023. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288 (2023).
[70] Aniket Vashishtha, Kabir Ahuja, and Sunayana Sitaram. 2023. On evaluating and mitigating gender biases in multilingual settings.
arXiv preprint arXiv:2307.01503 (2023).
[71] Sshubam Verma, Mohammed Safi Ur Rahman Khan, Vishwajeet Kumar, Rudra Murthy, and Jaydeep Sen. 2024. MILU: A Multi-task
Indic Language Understanding Benchmark. arXiv:2411.02538 [cs.CL] https://arxiv.org/abs/2411.02538
[72] Ishaan Watts, Varun Gumma, Aditya Yadavalli, Vivek Seshadri, Manohar Swaminathan, and Sunayana Sitaram. 2024. PARIKSHA: A
Large-Scale Investigation of Human-LLM Evaluator Agreement on Multilingual and Multi-Cultural Data. arXiv preprint arXiv:2406.15053
(2024).
[73] Shijie Wu and Mark Dredze. 2020. Are All Languages Created Equal in Multilingual BERT?. In Proceedings of the 5th Workshop on
Representation Learning for NLP, Spandana Gella, Johannes Welbl, Marek Rei, Fabio Petroni, Patrick Lewis, Emma Strubell, Minjoon Seo,
and Hannaneh Hajishirzi (Eds.). Association for Computational Linguistics, Online, 120–130. https://doi.org/10.18653/v1/2020.repl4nlp-
1.16
[74] L Xue. 2020. mt5: A massively multilingual pre-trained text-to-text transformer. arXiv preprint arXiv:2010.11934 (2020).

--- Page 12 ---

12
•
Aatman Vaidya, Tarunima Prabhakar, Denny George, and Swair Shah
[75] Linting Xue, Noah Constant, Adam Roberts, Mihir Kale, Rami Al-Rfou, Aditya Siddhant, Aditya Barua, and Colin Raffel. 2021. mT5: A
massively multilingual pre-trained text-to-text transformer. arXiv:2010.11934 [cs.CL] https://arxiv.org/abs/2010.11934
[76] Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang, Junjie Zhang, Zican
Dong, Yifan Du, Chen Yang, Yushuo Chen, Zhipeng Chen, Jinhao Jiang, Ruiyang Ren, Yifan Li, Xinyu Tang, Zikang Liu, Peiyu Liu,
Jian-Yun Nie, and Ji-Rong Wen. 2024. A Survey of Large Language Models. arXiv:2303.18223 [cs.CL] https://arxiv.org/abs/2303.18223
[77] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Tianle Li, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zhuohan Li, Zi Lin, Eric P
Xing, et al. 2023. Lmsys-chat-1m: A large-scale real-world llm conversation dataset. arXiv preprint arXiv:2309.11998 (2023).
A
Indic LLM Table Data
Table 5. An Overview of Indic LLM’s, including their release time, modality, access, license, training data and size
Host
Model
Date
Cre-
ated
Size
Training
Dataset
Modality
(In; Out)
Access
License
LLM
Type
Architecture
OpenAI
GPT 4
14
March
2023
unknown
-
image,
text;
image,
text
limited
unknown
pre-
trained
decoder
only
GPT 3.5-
turbo
1 March
2023
unknown
-
text; text
limited
Custom
pre-
trained
decoder
only
GPT 4-o
13 May
2024
unknown
-
audio,
image,
text,
video;
audio,
image,
text
limited
unknown
pre-
trained
decoder
only
GPT 3
11 June
2020
175B
Common Crawl,
WebText dataset,
Books corpora
and
English-language
Wikipedia data
text; text
limited
unknown
pre-
trained
decoder
only
Anthropic
Claude
3.5
Sonnet
21 June
2021
unknown
-
text;
image,
text
open
unknown
pre-
trained
decoder
only
Mistral
Mistral
27 Sep
2023
7B
-
text; text
open
Apache
2.0
pre-
trained
decoder
only
Google
Gemma
21 Feb
2024
7B
-
text; text
open
Custom
pre-
trained
decoder
only
Gemma
2
21 Feb
2024
27B
-
text; text
open
Custom
pre-
trained
decoder
only
Gemini
1.5 Flash
30 May
2024
unknown
-
audio,
image,
text,
video; text
limited
Googles
Terms
and Con-
ditions
pre-
trained
decoder
only

--- Page 13 ---

Analysis of Indic Language Capabilities in LLMs
•
13
Table 5 – continued from previous page
Host
Model
Date
Cre-
ated
Size
Training
Dataset
Modality
(In; Out)
Access
License
LLM
Type
Architecture
mT5
22 Oct
2020
11B
(large)
Multilingual C4
(mC4), it has 101
languages and is
generated from
86 Common
Crawl dumps
text; text
open
Apache
2.0
pre-
trained
encoder-
decoder
Muril
19 Mar
2021
-
Wikipedia and
Common Crawl
for 17 Indian
languages,
includes
translated and
transliterated
data
text; text
open
Apache
2.0
pre-
trained
encoder
only
mBERT
5 Nov
2018
-
104 languages
with the highest
Wikipedia data
text; text
open
Apache
2.0
pre-
trained
encoder
only
Meta
Llama 3
18 Apr
2024
70B
Trained on over
15 trillion tokens
of data from
publicly available
sources.
text; text
open
Llama 3
Commu-
nity
License
Agree-
ment
pre-
trained
decoder
only
Llama
24 Feb
2023
65B
CommonCrawl,
C4, Github,
Wikipedia,
BooksCorpus,
arXiv,
StackExchange
text; text
open
LLaMa
License
(model
weights),
GPLv3
(code)
pre-
trained
decoder
only
Llama2
18 Jul
2023
7B,
70B
Trained on a new
mix of publicly
available data.
text; text
open
Llama 2
Commu-
nity
License
Agree-
ment
pre-
trained
decoder
only
Llama
3.1
23 Jul
2024
8B,
70B,
405B
Trained on over
15 trillion tokens
of data from
publicly available
sources.
text; text
open
Llama
3.1 Com-
munity
License
Agree-
ment
pre-
trained
decoder
only

--- Page 14 ---

14
•
Aatman Vaidya, Tarunima Prabhakar, Denny George, and Swair Shah
Table 5 – continued from previous page
Host
Model
Date
Cre-
ated
Size
Training
Dataset
Modality
(In; Out)
Access
License
LLM
Type
Architecture
Big
Science
BLOOM
12 Jul
2022
176B
ROOTS corpus
text; text
open
BigScience
RAIL
License
pre-
trained
decoder
only
Cohere
Command
R
11 Mar
2024
35B
-
text; text
open
CC BY
NC 4.0
pre-
trained
decoder
only
Aya-23
31 May
2024
35B
Aya Dataset -
human-curated
prompt-
completion pairs
text; text
open
CC BY
NC 4.0
finetuned
decoder
only
Sarvam AI
OpenHathi
-
7B
-
text; text
open
Llama 2
Commu-
nity
License
Agree-
ment
pre-
trained
decoder
only
Sarvam-
2b-v0.5
13 Aug
2024
2B
Trained on a data
mixture of 4
trillion tokens:
containing equal
parts English (2T)
and Indic (2T)
tokens.
text; text
open
unkown
pre-
trained
decoder
only
Sarvam 1
24 Oct
2024
2B
Sarvam-2T -
includes 2T
tokens for 10
Indic language
text; text
open
Sarvam
AI
Research
License
pre-
trained
decoder
only
AI4Bharat
Airavata
26 Jan
2024
Indic Instruct
Data
text; text
open
Llama 2
Commu-
nity
License
Agree-
ment
finetuned
decoder
only
Telugu
LLM Labs
Navarasa
2.0
-
2B, 7B
LoRA finetuned
on 15 Indian
languages and
English language
instruction
datasets:
text; text
open
Gemma
Terms of
Use
finetuned
decoder
only

--- Page 15 ---

Analysis of Indic Language Capabilities in LLMs
•
15
Table 5 – continued from previous page
Host
Model
Date
Cre-
ated
Size
Training
Dataset
Modality
(In; Out)
Access
License
LLM
Type
Architecture
Lingo
Research
Group at
IIT Gand-
hinagar
Ganga
1B
-
1B
trained on a large
dataset of public
domain
web-crawled
Hindi language
data
text; text
open
Apache
2.0
finetuned
decoder
only
Bhabha AI
Gajendra-
v0.1
-
7B
-
text; text
open
Llama 2
Commu-
nity
License
Agree-
ment
finetuned
decoder
only
-
Open
Aditi v4
-
7B
Samvadd
text; text
open
Apache
2.0
finetuned
decoder
only
GenVR
Research
AryaBhatta-
GemmaGenZ-
Vikas-
Merged
-
7B
GenZ Vikas
dataset
text; text
open
MIT
finetuned
decoder
only
B
Indic LLM Evaluation Papers
In this section, we review relevant papers that evaluate large language models for Indian languages, including
the models assessed, the datasets created/ used, languages and tasks covered and the methodologies employed.
• IndicGenBench by Singh et al. [64] extends existing benchmarks to 29 Indic languages through human
annotation. The dataset comprises of diverse generation tasks like cross-lingual summarization, machine
translation, and cross-lingual question answering. The authors evaluate a wide range of proprietary and
open-source LLMs like GPT-3.5, GPT-4, PaLM-2, mT5, Gemma, BLOOM and LLaMA. The work finds a
significant performance gap in all languages compared to English. They also compares the token fertility
(average number of sub-words that a word is broken down into by the tokenizer) across all Indic languages
in the dataset. They find that Urdu has the lowest token fertility and Tibetan has the highest.
• MEGA by Ahuja et al. [9] presents a comprehensive benchmarking of generative LLMs for 70 typologically
diverse languages across 16 NLP datasets. The authors compare the performance of LLMs like GPT-3.5,
GPT-4, BLOOMZ, m-BERT. They find a significant performance gap between English and non-English
languages, especially low-resource languages with non-Latin scripts. Three of the 16 datasets focus
exclusively on Indian languages, covering over 11 Indic languages, while other datasets include some Indic
languages as well. The authors also explore different prompting strategies, finding that translating test
data to English before inputting it to the model often improves performance for low-resource languages.
They create a framework for for evaluating generative LLMs in the multilingual setting and provide
directions for future research.
• MEGAVERSE by Ahuja et al. [10] extends MEGA coverage to 22 datasets and 83 languages (including
many low-resource African languages). The dataset suite includes tasks such as text classification, POS
tagging, NER, translation, summarization, question answering etc. They benchmark performance of

--- Page 16 ---

16
•
Aatman Vaidya, Tarunima Prabhakar, Denny George, and Swair Shah
GPT-3.5-Turbo, GPT-4, PaLM2, GeminiPro, Mistral, Llama2, Gemma, and multimodal models like LLaVA,
GPT-4-Vision, and GeminiPro-Vision. Results show that larger models, particularly GPT-4, Gemini-Pro,
and PaLM2, outperform smaller models, especially on low-resource languages. The authors also conduct
a data contamination study and point out that several models are likely contaminated with multilingual
evaluation benchmarks, suggesting the need for approaches to detect and handle contamination when
assessing the multilingual performance of LLMs.
• IndicXTREME by Doddapaneni et al. [26] is a human supervised benchmark containing evaluation sets
for nine diverse tasks with each task covering 7-18 Indic languages per task. These are five sentence
classification tasks, two structure prediction, one question answering and one sentence retrieval task. The
authors evaluate IndicBERT, mBERT, XLMR, and MuRIL on the dataset, showing that pre-training on
Indic languages enhances performance, with additional gains from using in-language or related language
data for training and development.
• METAL by Hada et al. [32] contributes a datasets to evaluate LLM-based evaluators, which they refer
to as meta-evaluation. The task covered in the dataset is summarization and contains 10 languages, out
of Hindi and Bengali are the Indic languages. The authors evaluate the performance of GPT-3.5, GPT-4
and PaLM-2 on the dataset and results show that GPT-4 with detailed instructions performs closest to
humans, while GPT-3.5-Turbo is not a suitable multilingual evaluator.
• PARIKSHA by Watts et al. [72] studies human and LLM-based evaluation in a multilingual and multi-
cultural setting. They evaluate 30 models across 10 Indic languages. The task was to evaluate the output
of LLMs based on prompts, covering topics in finance, health, and culture. They find that models such
as GPT-4o and Llama-3 70B consistently perform best for most Indic languages on pairwise settings
and human evaluation. Their findings also indicate that LLM evaluators tend to align less with human
evaluations on assessing culturally nuanced responses.
• IndicNLPSuite by Kakwani et al. [41] is a collection of resources for Indian language NLP. In this this
suite, they introduce IndicGLUE, a benchmark dataset spanning several natural language understanding
tasks supporting 11 Indic languages. The tasks include News Category Classification, Headline Prediction,
Wikipedia Section-title Prediction, Multiple-choice QA, NER and Cross-lingual Sentence Retrieval. They
evaluate XLM-R, mBERT, IndicBERT (large and base) on the dataset and IndicBERT performed the best
on most tasks.
• IndicNLG by Kumar et al. [47] is a collection of natural language generation datasets for 11 Indic languages.
The tasks include biography generation using Wikipedia infoboxes, news headline generation, sentence
summarization, generation and, question generation. They evaluate two models, IndicBART and mT5,
and find that language-specific models like IndicBART demonstrate better performance, highlighting the
advantage of pre-training on language-specific data.
• IndicXNLI by Aggarwal et al. [7] is a natural language inference datasets supporting 11 Indic languages.
The datasets is created by machine translating the original English XNLI dataset. The dataset’s quality is
validated through human evaluation. The authors fine-tune XLM-R, IndicBERT, mBERT, and MuRIL on
the dataset and investigate cross-lingual transfer techniques. Results show that MuRIL generally performs
best, and training on both English and Indic data yields the highest scores.
• MILU (Multi-task Indic Language Understanding) by Verma et al. [71] is benchmark dataset covering 11
Indic languages. The dataset includes tasks for natural language understanding and generation, evaluating
both linguistic competence and cultural understanding. It spans 8 domains and 42 subjects and is designed
with an India-first perspective by collecting questions from various national, state, and regional exams.
These questions include culturally relevant subjects such as local history, arts, festivals, and laws, alongside
traditional academic subjects like science and mathematics. The authors evaluate 45 different LLMs (mix
of closed proprietary, open-source, and language-specific models), and the findings suggest that models

--- Page 17 ---

Analysis of Indic Language Capabilities in LLMs
•
17
struggle with MILU, with GPT-4o achieving the highest average accuracy at 72%. Interestingly, open
multilingual models outperform language specific models. Their domain-wise analysis reveals that models
perform poorly in culturally relevant areas, such as Arts & Humanities and Social Sciences, compared to
more general fields like STEM.
• MAPLE by Aggarwal et al. [8] focuses on multilingual evaluation of parameter efficient fine-tuning of
LLMs. They analyze the effects of percentage of trainable parameters and quantization on 40 languages
across various tasks like classification, question answering, summarization and institution following.
The paper compares performance of Llama-2-7B and Mistral-7B on the datasets. They find that having
more languages in the fine-tuning datasets does not necessarily mean significantly better multilingual
performance.
• Indic LLM Leaderboard translates existing SOTA benchmarks like benchmarks like ARC, Hellaswag,
MMLU, etc to 7 Indic languages. Maintains a leader board evaluating pre-trained and fine-tuned Indic
LLMs.

```
