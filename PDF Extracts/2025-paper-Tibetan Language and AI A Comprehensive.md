---
title: "2025-paper-Tibetan Language and AI A Comprehensive - PDF Extract"
source_pdf: "2025-paper-Tibetan Language and AI A Comprehensive.pdf"
pages: 41
extracted_at: "2026-02-13T09:15:45.080914"
---

# PDF Extract: 2025-paper-Tibetan Language and AI A Comprehensive

**Source PDF:** 2025-paper-Tibetan Language and AI A Comprehensive.pdf
**Total Pages:** 41

---

## Content

```
--- Page 1 ---

Tibetan Language and AI: A Comprehensive Survey
of Resources, Methods and Challenges
Cheng Huang1,3,+, Nyima Tashi2,+,*, Fan Gao1, Yutong Liu1, Jiahao Li4, Hao Tian5, Siyang
Jiang6, Thupten Tsering1,2, Ban Ma-bao2, Renzeg Duojie2, Gadeng Luosang2, Rinchen
Dongrub2, Dorje Tashi2, Jin Zhang1, Xiao Feng1, Hao Wang1,7, Jie Tang8, Guojie Tang9,10,
Xiangxiang Wang1,*, Jia Zhang3, Tsengdar Lee12, and Yongbin Yu1,*
1University of Electronic Science and Technology of China, Chengdu, 610056, China
2Tibet University, Lhasa 850000, China
3Southern Methodist University, Dallas, 75205, USA
4The City University of Hong Kong, Kowloon, Hong Kong SAR 999077, China
5The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong SAR 999077, China
6The Chinese University of Hong Kong, Sha Tin, Hong Kong SAR 999077, China
7University of Connecticut, Storrs, 06269, USA
8Tsinghua University, Beijing 100084, China
9University of Texas at Arlington, Arlington, TX 76019, USA
10University of Chinese Academy of Sciences, Beijing 100049, China
11The State Key Laboratory of Tibetan Intelligence, Lhasa 850000, China
12National Aeronautics and Space Administration, Washington, DC 20546, USA
*Corresponding Author, E-mail: ybyu@uestc.edu.cn
+Equal Contribution
ABSTRACT
Tibetan, one of the major low-resource languages in Asia, presents unique linguistic and sociocultural characteristics that pose
both challenges and opportunities for AI research. Despite increasing interest in developing AI systems for underrepresented
languages, Tibetan has received limited attention due to a lack of accessible data resources, standardized benchmarks, and
dedicated tools. This paper provides a comprehensive survey of the current state of Tibetan AI in the AI domain, covering
textual and speech data resources, NLP tasks, machine translation, speech recognition, and recent developments in LLMs. We
systematically categorize existing datasets and tools, evaluate methods used across different tasks, and compare performance
where possible. We also identify persistent bottlenecks such as data sparsity, orthographic variation, and the lack of unified
evaluation metrics. Additionally, we discuss the potential of cross-lingual transfer, multi-modal learning, and community-driven
resource creation. This survey aims to serve as a foundational reference for future work on Tibetan AI research and encourages
collaborative efforts to build an inclusive and sustainable AI ecosystem for low-resource languages.
BOX 1: Key Contributions of This Survey
• Presents the first unified survey of Tibetan AI across text, speech, and emerging multimodal domains, rather than
treating them as isolated research tracks.
• Systematically consolidates all publicly accessible Tibetan resources: datasets, toolchains, benchmarks, and
linguistic assets to provide a structured foundation for future development.
• Critically analyzes the behavior of state-of-the-art AI techniques under Tibetan-specific linguistic and sociocul-
tural conditions, revealing failure modes not observed in high-resource settings.
• Distills the remaining research gaps and proposes a forward-looking agenda toward inclusive, sustainable, and
culturally grounded Tibetan AI research.
Note: Some abbreviations are summaried in Appendix A Table 3. These abbreviations represent some of the classical or key
concepts, methods, and datasets frequently mentioned throughout this survey.
1
arXiv:2510.19144v1  [cs.CL]  22 Oct 2025

--- Page 2 ---

Tibetan Language
Processing
Introduction
(Section 1)
Tibetan
Resource
(Section 2)
Task on 
Tibetan AI
(Section 3)
Future
Direction
(Section 6)
Challenge
(Section 5)
Tibetan AI 
& Application
(Section 4)
1
2
3
4
5
6
Overview
Natural Language Processing of Tibetan
Discriminative
Tasks
Tibetan Corpus
Data scarcity
Data Construction
Annotated Dataset
Benchmark
Rule-based Method
Memristor
New Knowledge
Adaptation
Manual Calibration
Generative Tasks
Fundamental Task
 Interdisciplinary Collaborations
Background
Summary
Large Language
Model
Transformer-
based Model
Common Model: RNN, LSTM, ...
Knowledge Graph
Ethical & Safety
Concerns
Encoding Standard & Inefficiency
AI Development
Dedicated hardware
Application
Figure 1. Overview of the Practical Guide for current AI Trend on Tibetan
1 Introduction
In recent years, AI has achieved remarkable progress in language understanding1–5, generation6–10, and multimodal inter-
action11–15, largely driven by advances in deep learning1,16, the availability of large-scale datasets17–19, and the emergence
of LLMs, such as GPT family20–22, LlaMA family23–25, DeepSeek family26,27, Qwen family28–31, Gemini family32–34, and
Claude family35–38. While such progress has significantly benefited high-resource languages such as English and Chinese, many
languages spoken by marginalized and linguistically diverse communities, commonly referred to as low-resource languages,
remain underrepresented in the development and deployment of language technologies. Among them, Tibetan is a particularly
important yet underexplored case. It is a member of the Tibeto-Burman branch of the Sino-Tibetan language family, is spoken
by over six million people across China, India, Nepal, and Bhutan39. The language plays a crucial role in preserving the cultural,
spiritual, and historical heritage of the Himalayan region40,41. However, Tibetan exhibits several characteristics that complicate
computational modeling: a non-Latin orthography, morpho-syllabic structure, complex verb morphology, dialectal variation,
and limited digital standardization42,43. These features, combined with a lack of accessible linguistic resources and annotated
data, make Tibetan a challenging target for current AI systems17,18,44.
Despite the increasing academic interest in developing language technologies for low-resource and endangered languages,
Tibetan remains relatively neglected in both academic and industrial research. Existing efforts are fragmented across isolated
datasets, task-specific methods, and small-scale experiments. There is no unified survey or roadmap that summarizes the current
landscape of Tibetan AI research, identifies key gaps, and proposes a direction for future development. This absence hinders
collaboration, benchmarking, and progress. These research gaps motivate this review which offers a comprehensive review of
the development of AI technologies and their applications in Tibetan. We aim to cover topics on existing AI models, various
tasks of AI on Tibetan, AI applications of Tibetan language, arising challenges, and future directions.
As shown in Figure 1, this review seeks to answer the following questions:
• Section 1: What is the current status of cross-disciplinary research on AI and Tibetan? What have we summarized in this
report?
• Section 2: What is Tibetan? What are the unique characteristics of Tibetan compared to major languages such as Chinese
and English? How can we obtain relevant data?
2/41

--- Page 3 ---

• Section 3: What are the main tasks for existing AI applications in Tibetan? What are the needs for these tasks?
• Section 4: What AI-related technologies do they use and how is the progress? How are they set up according to the
needs of the Tibetan language itself?
• Section 5: What challenges should be addressed when implementing AI in Tibetan?
• Section 6: How can we optimize the construction of AI to enhance their applicability in Tibetan AI, ultimately
contributing to low-resource language and creating a positive societal impact?
To address these issues, this survey provides the first comprehensive review of Tibetan language research in the field of AI.
We begin by outlining the current research landscape at the intersection of Tibetan and AI, highlighting the key challenges
that hinder progress in this low-resource domain. Building on this context, we articulate the motivation for conducting this
survey and provide an overview of its themes and structure in Section 1. In Section 2, we systematically review available
data resources for both text and speech, covering monolingual corpora, parallel corpora, and annotated datasets for tasks
such as word segmentation, part-of-speech tagging, and named entity recognition. Section 3 summarizes key tasks at the
intersection of AI and Tibetan, analyzing their practical needs and applications. In Section 4, we examine AI models applied
to Tibetan, including machine translation, classification, automatic speech recognition, and text-to-speech synthesis. We
further assess the performance and limitations of multilingual pre-trained models and LLMs when applied to Tibetan, and
explore emerging directions such as cross-lingual transfer, prompt-based learning, and multimodal processing. Section 5 then
analyzes the bottlenecks of existing AI models and data, and discusses ethical and safety considerations. Finally, Section 6
outlines promising avenues for future research, including the development of specialized hardware for Tibetan scripts, the
construction of larger and more diverse datasets and benchmarks, the advancement of multimodal models, and the exploration
of techniques such as instruction tuning and reasoning-augmented learning. These efforts can enhance the efficiency of Tibetan
AI, broaden task coverage, support applications in education and cultural preservation, and help bridge the gap between low-
and high-resource languages, thereby promoting inclusivity in multilingual AI.
We hope this work will serve as a foundational reference for researchers and practitioners in low-resource AI, and contribute
to the broader goal of equitable language technology development.
3/41

--- Page 4 ---

BOX 2: Background of Tibetan
Tibetan is a historically rich and linguistically diverse language with a distinctive script, a strong classical literary
tradition, and significant dialectal variation, playing a central role in the cultural and religious life of communities
across the Himalayan region39,41.
→Historical Origin
Tibetan belongs to the Tibeto-Burman branch of the Sino-Tibetan language family. The development of written Tibetan
began in the 7th century during the reign of King Songtsen Gampo, who commissioned the creation of the Tibetan script.
This script, attributed to Thonmi Sambhota and based on Indian Brahmi and Gupta models, was primarily designed to
support the translation of Buddhist texts from Sanskrit, laying the foundation for a written literary tradition45,46.
→Script & Classical Literary Tradition
The Tibetan script is an abugida system composed of consonant characters combined with vowel diacritics. As shown
in Figure 2, this is one sample of the native tibetan syllable structure, which means raise or lift. It consists of 7 parts:
prefix letter, root letter, superscript letter, subscript letter, vowel letter, suffix letter, and farther suffix letter. There is a
certain combination principle between different letters43. Since its inception, it has remained relatively stable and is
still used in both religious and secular contexts. Classical Tibetan emerged as the standard literary form and became
the medium for a vast body of canonical Buddhist literature, historical records, legal documents, and medical texts.
This classical form continues to serve as a common written standard across Tibetan-speaking regions despite spoken
variation47.
Figure 2. One Structure Example of the Tibetan Script
→Dialectal Diversity
Modern spoken Tibetan is generally divided into three major dialect groups: Central (Ü-Tsang), Khams, and Amdo.
These dialects exhibit significant differences in phonology, vocabulary, and syntax, and are often mutually unintelligible.
However, they are unified by a shared use of the classical written language. Among them, Central Tibetan, especially
the Lhasa variety, serves as the basis for standardized written Tibetan and official media usage47,48.
→Contemporary Use & Sociolinguistic Role
Today, Tibetan is spoken by more than six million people across the Tibet Autonomous Region of China, as well as in
parts of India, Nepal, and Bhutan. It is actively used in domains such as religious practice, local education, community
governance, broadcasting, and literature. Tibetan remains a vital symbol of cultural identity, continuity, and resistance,
especially among communities in exile and in regions experiencing language shift or political pressur49,50.
2 Tibetan Resource
Despite its rich cultural and linguistic heritage, shown in Box 2, Tibetan has long suffered from a lack of standardized and
accessible language resources. In this section, we provide an overview of existing Tibetan resources, including public corpora,
annotated datasets, and preliminary benchmarks, which together form the foundation for Tibetan AI and its research.
2.1 Public Corpus
Existing Tibetan public corpora primarily consist of web-crawled texts, classical scriptures, news articles, and limited modern-
domain content. While these corpora provide a crucial starting point for data-driven Tibetan language processing, most of
them suffer from uneven quality, inconsistent orthographic standards, duplicated content, and a lack of linguistic normalization.
Furthermore, a large portion of publicly available Tibetan text is derived from religious or historical sources, which introduces
strong stylistic bias and limits the applicability of these corpora for training models intended for contemporary usage scenarios
such as dialogue, instruction following, and safety alignment. To better understand the foundation upon which later datasets
4/41

--- Page 5 ---

are constructed, it is necessary to first examine the open Tibetan language databases that supply the raw materials for corpus
creation. Unlike task-specific datasets or benchmarks, a number of open Tibetan language repositories exist in the form of
large-scale raw text collections and lexical platforms. These databases provide the foundational materials from which corpora
and downstream AI datasets are later derived.
• BDRC51: BDRC is a large-scale digital archive containing over 200k volumes of Tibetan canonical texts in PDF and
Unicode formats. It is the largest publicly accessible Tibetan text source but heavily biased toward classical and religious
style.
• THL52: THL is a curated linguistic platform providing lexical standards, dialect documentation, orthographic normaliza-
tion guides, and annotated language samples. It is widely used as a reference for tokenization and script normalization
rather than direct model training.
• RYTC53: RYTC is a structured Tibetan Buddhist corpus with semantic segmentation and commentary alignment. While
domain-constrained, its clean formatting makes it suitable for canonical language modeling.
• BDICT/THL Dictionary API54: THL Dictionary API is an openly accessible lexical database offering lemma forms,
POS tags, and example sentences with API support. It serves as a grounding resource for morphological analysis and
vocabulary construction in Tibetan AI.
• TWD55: TWD is a modern-domain encyclopedic corpus with around 70k+ Tibetan articles. Although limited in size,
it remains one of the very few sources that reflect contemporary Tibetan usage suitable for instruction tuning and
conversational modeling.
• ACIP56: ACIP is An early digitization initiative encoding Tibetan texts using Wylie transliteration and Unicode mapping.
It plays a foundational role in script standardization and character-level normalization.
• OTFC57: OTFC is a small but unique set of Tibetan subtitle fragments that contain informal and conversational speech
patterns, valuable for modeling colloquial Tibetan despite its extremely limited scale.
These repositories form the base layer of the Tibetan language resource stack and serve as the raw material for constructing
standardized corpora, task datasets, and eventually benchmarks for Tibetan AI.
2.2 Annotated Dataset
Compared to raw corpora and lexical repositories, publicly available Tibetan annotated datasets are extremely limited in
both scale and task diversity. Most existing resources were constructed for early AI tasks such as word segmentation, POS
tagging, and OCR correction, often derived from classical texts with manually curated labels. These datasets, while valuable for
linguistic analysis, lack consistency in annotation standards and are not aligned with modern instruction-based or safety-critical
AI development needs. Furthermore, there is currently no unified annotation framework that supports multi-dimensional
supervision such as instruction-response pairs, safety alignment labels, or preference signals, which are essential for training
contemporary Tibetan LLMs. To better understand the current landscape of Tibetan annotated resources and their limitations in
relation to LLM-oriented supervision, we summarize the main publicly available datasets as follows:
• NICT-Tib158: NICT-Tib1 comprises approximately 33.5 hours of read speech from native Lhasa Tibetan speakers
and has been widely adopted for ASR model training, although its scripted design limits variability in prosody and
spontaneous speech patterns.
• TIBMD@MUC59: TIBMD@MUC covers three major dialects: Ü-Tsang, Kham, and Amdo, to introduce acoustic
diversity into Tibetan ASR research, yet it remains limited to speech transcription without incorporating semantic or
generative supervision.
• TibNER60: TibNER provides token-level entity annotations over person, location, and organization categories and
supports named entity recognition research, but it does not extend to instruction-based reasoning or generative entity
understanding.
• CUTE Multilingual Corpus61: CUTECorpus introduces Tibetan into a multilingual alignment setting alongside Chinese,
Uyghur, and English and enables parallel translation research, though it lacks instruction tuning or preference alignment
signals.
5/41

--- Page 6 ---

• Tibetan MRC62: TibetanMRC pairs Tibetan news passages with manually created question, answer annotations and
advances extractive reading comprehension but does not incorporate dialogue context or chain-of-thought reasoning
supervision.
• TiConvQA63: TiConvQA extends Tibetan QA into multi-turn conversational form and enriches discourse-level informa-
tion retrieval, yet it still follows a fixed QA paradigm without integrating preference or safety alignment annotations.
• TiLTS64: TiLTS aligns Tibetan news articles with abstractive summaries and introduces long-form generative modeling,
but it remains decoupled from controllable instruction-dependent generation objectives.
• Cross-Lingual Tibetan Summarization65: CrossLingualSummarization pairs Tibetan source passages with human-
written Chinese summaries and supports bilingual summarization research, although it focuses exclusively on content
fidelity without multi-dimensional supervision signals.
• TiKG-30K66: TiKG-30K provides over 30K Tibetan entity-relation triples and facilitates symbolic reasoning, yet it does
not connect structured knowledge supervision with instruction-based or conversational LLM training.
Also, for contemporary LLM development, publicly available Tibetan pretraining datasets are extremely scarce, with only
three large-scale corpora currently accessible to the community:
• TIBSTC18: TIB-STC introduces the first large-scale, expert-curated and structurally organized Tibetan corpus designed
specifically for LLM development, consolidating over 11B tokens across diverse domains such as literature, religion,
medicine, law, and daily communication. Unlike earlier fragmented Tibetan resources, TIB-STC establishes a unified
supervision framework that supports pretraining, instruction tuning, and alignment phases, and is further validated through
a three-stage pipeline language modeling, supervised fine-tuning, and preference optimization, using the reference model
Sun-Shine. To enable systematic evaluation, the authors also align the corpus with TLUE44, a Tibetan benchmark suite
covering understanding, reasoning, and safety scenarios, and demonstrate significant performance improvements on tasks
such as Ti-MMLU and Ti-SafetyBench. TIB-STC therefore marks the first comprehensive and publicly reported attempt
to construct a scalable Tibetan data infrastructure for modern LLM training and evaluation.
• TIBSTC-CoT17: TIBSTC-CoT introduces the first chain-of-thought oriented Tibetan instruction corpus, extending
the TIBSTC framework by generating multi-domain reasoning data through CoT prompting to address the scarcity of
logical supervision in low-resource Tibetan language modeling. The dataset covers diverse reasoning scenarios, including
arithmetic reasoning, commonsense inference, and structured logical deduction and follows a scalable, replicable data
generation pipeline that leverages large multilingual models to produce Tibetan step-by-step reasoning trajectories.
Built on this corpus, the authors train the Sunshine-thinking model family, which demonstrates strong performance on
Tibetan reasoning tasks and reaches competitive results compared to state-of-the-art multilingual LLMs, highlighting the
effectiveness of explicit CoT supervision. TIBSTC-CoT therefore establishes the first dedicated Tibetan reasoning dataset
and provides a practical methodology for injecting structured cognitive signals into low-resource language models.
• TJUNLP Tibetan Corpus19: TJUNLP Tibetan Corpus establishes the largest curated Tibetan pretraining resource to date,
consolidating 72GB of Tibetan text from open-source corpora, web-crawled pages, synthetic translation pairs, and private
digitized collections under a unified cleaning and deduplication pipeline tailored to Tibetan linguistic characteristics.
Built to support continual pretraining of multilingual foundation models, the corpus enables two-stage adaptation,
language-balanced pretraining and long-context extension, achieving substantial performance gains across Tibetan
benchmarks when integrated into models such as Qwen2.530. The work demonstrates that large-scale, well-filtered
Tibetan pretraining data can significantly enhance both understanding and generation capabilities and serves as the
current backbone corpus for Tibetan LLM training under the TJUNLP Tibetan Corpus designation.
Together, these three corpora delineate the current landscape of Tibetan LLM data resources: TIBSTC18 establishes the
foundation for supervised instruction alignment, TIBSTC-CoT17 contributes explicit reasoning supervision, and the TJUNLP
Tibetan Corpus19 supplies the large-scale pretraining backbone necessary for continual Tibetan language modeling. For more
details about TIBSTC18 and TIBSTC-CoT17, please refer to Appendix B.
2.3 Benchmark
Both dedicated, formal and official Tibetan benchmarks and multilingual evaluation suites with meaningful Tibetan coverage
are exceedingly limited, highlighting a significant evaluation gap in Tibetan language AI. To provide a structured analysis, we
divide existing evaluation resources into two categories: Specialized Benchmark and Comprehensive Multilingual Benchmark
with partial Tibetan inclusion. We introduce them separately in the following.
6/41

--- Page 7 ---

2.3.1 Specialized Benchmark
Despite the rapid development of multilingual evaluation resources, Tibetan remains one of the most underserved languages,
with only a few benchmarks that are still actively adopted by the research community. The currently recognized evaluation
resources can be categorized into two representative benchmarks:
• TLUE44: TLUE is the first and currently the only standardized benchmark designed specifically for evaluating natural
language understanding in Tibetan for LLMs. TLUE integrates Ti-MMLU and Ti-SafetyBench to jointly assess general
knowledge reasoning and safety alignment, with support for zero-shot and few-shot settings to enable fair comparisons
without language-specific tuning. More details are provided in Appendix C.
• Tibetan ASR67: Tibetan ASR was built primarily upon the Tibetan portion of the IARPA Babel Corpus, which contains
around 40 hours of transcribed conversational speech under low-resource conditions. Although originally part of a
multilingual ASR initiative, it has become a de facto standalone benchmark for Tibetan speech recognition, with Word
Error Rate as the standard metric, representing one of the earliest task-specific benchmarks for Tibetan spoken language
processing.
2.3.2 Comprehensive Multilingual Benchmark
Among all existing multilingual benchmarks, only FLORES-20068 provides limited Tibetan coverage and exclusively in
translation, while no general-purpose benchmark assesses Tibetan reasoning, understanding, or safety alignment. To illustrate
the limitations of current multilingual resources, we summarize the Tibetan component of FLORES-20068 as follows:
• Tibetan Sub-benchmark of FLORES-20068: this is a multilingual machine translation benchmark released by Meta AI,
covering 200 languages under a unified evaluation protocol, and Tibetan (bo) is included as one of the low-resource tracks
for Tibetan-English and Tibetan-Chinese translation using BLEU69 and ChrF++70 as metrics. However, the Tibetan
portion of FLORES-200 is strictly limited to translation and does not include any tasks related to reasoning, dialogue,
safety alignment, or domain-specific Tibetan linguistic understanding. The evaluation sentences are generic and do
not reflect challenges unique to Tibetan, such as its agglutinative morphology, religious terminology, and orthographic
variability.
Although FLORES-20068 is the only multilingual benchmark that officially includes Tibetan, it cannot be considered
a dedicated Tibetan understanding benchmark, as multilingual models that achieve strong performance on high-resource
FLORES tracks exhibit a sharp performance drop on the Tibetan subset. This reflects the token-level sparsity and structural
underrepresentation of Tibetan in existing multilingual modeling pipelines, reinforcing the necessity of specialized evaluation
resources such as TLUE44. Likewise, while models like mT571, BLOOM72, XGLM73, and LLaMA-224 include Tibetan tokens
from sources such as Wikipedia or religious web text, this only implies superficial token exposure rather than meaningful
evaluation support, since none of these models are trained or benchmarked under a Tibetan-specific task protocol or standardized
test set.
2.4 Others
In addition to officially released datasets and standardized benchmarks, there also exists a wide range of non-official, community-
curated Tibetan resources that are not formally recognized as benchmarks or datasets but are actively used in practical research
settings. For more details, please refer to Hugging Face1 and Kaggle2.
1https://huggingface.co/datasets?sort=trending&search=tibetan
2https://www.kaggle.com/
7/41

--- Page 8 ---

Fundamental Task
Data Collection
Annotation
Standardization
Dataset
Construction
Human Evaluation
Database
Development
AI Correction
Human-AI Collaborative
Verification
Discriminative Task
Low-level Lexical
Processing
Information
Extraction
Semantic
Understanding
Word Segmentation
Cross-modal
Transcription
Part-of-speech Tagging
Named Entity Recognition
Text Classification
Sentence Similarity &
Entailment Detection
Speech Recognition
Optical
Character Recognition
Generative Task
Basic Structured
Text Output
Content
Transformation
Interactive Context-
Aware Generation
Cross-Modal
Creative Generation
Machine Translation
Text Generation
Summarization
Speech Synthesis
Question Answering
Dialogue Generation
Multimodal Generation
Figure 3. Task Taxonomy of Tibetan AI
8/41

--- Page 9 ---

3 Task Taxonomy of Tibetan AI
This section introduces the task taxonomy of Tibetan AI, detailing each category and explaining their interdependencies
within the broader research landscape. Tibetan AI tasks can be organized into three major categories: Fundamental Task,
Discriminative Task and Generative Task. As shown in Figure 3, these three categories themselves form a progressive pipeline,
where fundamental tasks provide the necessary resources for discriminative modeling, which in turn underpins more advanced
generative applications. We will introduce details about them in following part.
3.1 Fundamental Task
Fundamental tasks in Tibetan AI establish the data and resource infrastructure necessary for downstream modeling. For
a low-resource and morphologically complex language like Tibetan, this includes collecting and cleaning text and speech
corpora, developing balanced domain-specific datasets, standardizing annotation schemes, and building searchable linguistic
databases. These efforts, such as digitizing manuscripts, aligning parallel texts, and enabling encoding conversion—are not
merely preliminary steps but continuous processes that determine the scalability and effectiveness of all subsequent Tibetan AI
research.
3.1.1 Data Collection
Data collection serves as the foundational stage for Tibetan AI development, establishing the raw material upon which all
downstream modeling relies. It encompasses not only the large-scale acquisition of Tibetan text and speech data, but also
the construction of structured databases that enable efficient access, retrieval, and standardized integration of heterogeneous
resources. To fulfill these objectives, current efforts in Tibetan AI can be broadly divided into two complementary directions:
dataset construction, which focuses on acquiring and cleaning raw multimodal data, and database development, which
emphasizes structured organization and standardized storage for long-term reuse.
• Dataset Construction: dataset construction is the cornerstone of Tibetan AI, involving the systematic collection,
digitization, and preprocessing of Tibetan text and speech data. This includes sourcing data from classical literature,
religious scriptures, news articles, educational materials, and modern conversational sources. For speech, high-quality
recordings with phoneme-level transcriptions are crucial. Data cleaning steps, such as removing OCR errors, normalizing
encoding, and filtering noisy samples, are essential to ensure usability for modeling74.
• Database Development: database development focuses on organizing Tibetan linguistic resources into structured,
queryable formats. This includes building searchable lexical databases, parallel corpora repositories, and domain-specific
term banks. Databases should support standardized metadata, facilitate interoperability across research projects, and
provide APIs or tools for programmatic access75,76.
3.1.2 Annotation Standardization
Annotation standardization is essential for ensuring cross-project consistency and enabling interoperability between Tibetan
AI systems. Given the linguistic complexity of Tibetan, characterized by syllable-based morphology, script variations, and
domain-dependent terminology, a unified annotation protocol is required to harmonize orthographic normalization, part-of-
speech tagging, named entity categorization, and segmentation rules. To achieve both scalability and linguistic fidelity, current
annotation workflows are increasingly adopting a multi-stage verification paradigm that integrates human expertise with
AI-assisted refinement through three complementary processes:
• Human Evaluation: expert annotators manually review and validate linguistic labels to ensure cultural and grammatical
fidelity, especially in domains such as religious texts and traditional Tibetan legal terminology17,18,21,25.
• AI Correction: automated consistency checking is performed using model-assisted detection of label conflicts, segmen-
tation drift, and orthographic variance to reduce manual workload and improve annotation throughput17.
• Human-AI Collaborative Verification: a hybrid verification workflow is adopted in which AI-proposed corrections
are selectively confirmed or rejected by human experts, allowing scalable annotation while preserving high linguistic
precision17.
3.2 Discriminative Task
Discriminative tasks are foundational to Tibetan AI, particularly in the early stages of system development. These tasks are
typically framed as classification or sequence labeling problems, where the model is trained to distinguish between different
categories or assign labels to input units. Despite the apparent simplicity, these tasks are particularly challenging in Tibetan due
to its agglutinative morphology, lack of whitespace, and dialectal diversity.
9/41

--- Page 10 ---

3.2.1 Low-level Lexical Processing
Low-level lexical processing establishes the token-level foundation for Tibetan language modeling. Due to its syllable-based
script and agglutinative morphology, Tibetan lacks clear word boundaries, making segmentation and POS tagging not just
preprocessing steps but core computational challenges that directly impact all downstream tasks.
• Word Segmentation: due to the absence of explicit word boundaries in Tibetan, where text is written as a continuous
syllable stream separated only by the tsheg mark (·), word segmentation becomes a core prerequisite for all downstream
tasks77–79. Ambiguous word boundaries, rich morphology, and dialectal variation make segmentation a linguistically
complex and computationally challenging problem, directly influencing tasks such as POS tagging, NER, parsing, and
machine translation80.
• Part-of-speech Tagging: POS tagging assigns grammatical categories to tokens and serves as a structural layer for
higher-level tasks including parsing and translation76,81. Tibetan’s agglutinative morphology and lack of clear word
delimiters make POS tagging heavily dependent on accurate segmentation. The limited availability of standardized
tagsets and annotated corpora further complicates model design and evaluation, keeping POS tagging as a critical but
under-resourced component in Tibetan AI82.
3.2.2 Information Extraction
To extend beyond segmentation and POS tagging, lexical processing in Tibetan also requires recognizing semantically
meaningful units such as named entities:
• Named Entity Recognition: NER involves identifying and classifying entities in text, such as person names, locations,
organizations, and temporal expressions, into predefined categories83. In Tibetan, NER is essential for information
extraction, knowledge graph construction, and question answering. However, the task is complicated by the absence of
word boundaries, frequent use of honorifics and case markers, and inconsistency in orthography across domains60. The
lack of large-scale annotated corpora and the variability of entity naming conventions in religious, historical, and modern
contexts further increase difficulty, making Tibetan NER a persistent low-resource challenge84.
3.2.3 Semantic Understanding
Beyond lexical and syntactic processing, semantic understanding focuses on interpreting meaning and relational intent in
Tibetan text, enabling higher-level reasoning and downstream applications such as retrieval, dialogue, and alignment. Core
tasks in this category include:
• Text Classification: Tibetan text classification supports applications such as document categorization, sentiment analysis,
and topic detection16,85. While model-agnostic in nature, performance is highly dependent on accurate segmentation and
the availability of labeled data. Key challenges include vocabulary sparsity, domain-specific terminology in religious and
medical texts, and the lack of consistently annotated public datasets. Recent work explores deep neural classifiers and
multilingual transformer models, showing promising results under low-resource conditions.
• Sentence Similarity & Entailment Detection: these semantic tasks evaluate relational meaning between Tibetan
sentence pairs, supporting QA, retrieval, and paraphrase detection86. Research is limited by the absence of Tibetan
contrastive sentence pair datasets and semantic variation arising from honorific expressions, flexible word order, and rich
morphology. Existing multilingual models provide partial transfer but lack robust Tibetan grounding, underscoring the
need for tailored datasets and alignment strategies for semantic understanding87,88.
3.2.4 Cross-modal Transcription
While most Tibetan AI research focuses on text-only processing, cross-modal transcription aims to bridge speech, image, and
text modalities, enabling large-scale digitization and multimodal understanding of Tibetan linguistic resources. This direction
primarily includes two key tasks:
• Speech Recognition: Tibetan ASR has practical value for voice interfaces, educational tools, oral tradition preservation,
and accessibility76,89. However, development remains limited due to the lack of transcribed speech corpora, strong
dialectal variation, and the absence of standardized phoneme inventories. Tibetan’s syllable-based script and tonal
patterns further complicate acoustic modeling. While end-to-end architectures such as CTC-based and attention-driven
encoder-decoder models have shown initial progress, performance remains unsatisfactory, and the creation of large,
domain-diverse Tibetan speech datasets is a major bottleneck.
10/41

--- Page 11 ---

• Optical Character Recognition: OCR is essential for digitizing Tibetan manuscripts, scriptures, and printed materials45.
Progress is challenged by complex orthography with stacked consonants, multiple diacritics, and inconsistent font
conventions. Historical documents introduce additional noise such as ink bleed and non-standard layouts. Modern
Tibetan OCR increasingly adopts CNN90 and CRNN-style neural architectures91, but system quality remains constrained
by the scarcity of annotated image-text pairs and the absence of standardized benchmarks.
3.3 Generative Task
Generative tasks in Tibetan AI focus on producing novel outputs, such as text, speech, or structured sequences, based on given
input. Unlike discriminative tasks that only assign labels, generative tasks require models to understand context and synthesize
coherent, fluent content, making them inherently more complex and resource-intensive. Progress in this area is constrained by
limited training data and the absence of standardized evaluation protocols. However, recent advances in multilingual LLMs and
instruction-tuned architectures have enabled promising developments across machine translation, summarization, question
answering, and speech synthesis for Tibetan.
3.3.1 Basic Structured Text Output
At the foundational level of generative modeling, basic structured text output focuses on producing well-formed Tibetan
sentences conditioned on external input, ranging from cross-lingual translation to monolingual generation. Current research in
this direction primarily centers on two representative tasks:
• Machine Translation: MT is one of the most studied generative tasks in Tibetan AI, primarily targeting Tibetan-Chinese
and Tibetan-English translation92,93. Progress is constrained by the scarcity of large-scale parallel corpora, orthographic
inconsistency, and domain-specific terminology in religious, legal, and historical texts. While early work relied on
rule-based and SMT approaches, recent research has shifted to Transformer-based and mBART-style architectures1,2,
with multilingual pretraining and transfer learning showing promising gains. Initiatives such as NLLB94 and TIB-STC18
attempt to address data bottlenecks, yet Tibetan MT still trails behind other low-resource languages in fluency, robustness,
and domain generalization.
• Text Generation: Tibetan text generation spans story writing, headline generation, dialogue completion, and instruction-
response synthesis17,18. Challenges arise from limited monolingual corpora, morphological complexity, and strong
stylistic variation across literary, religious, and colloquial registers. Multilingual language models such as mT571,
XGLM73, and Qwen28–31 enable Tibetan generation via fine-tuning or instruction adaptation, while recent datasets like
Sunshine-2.0 and TIBSTC-CoT17 begin to introduce Tibetan-specific generative resources. Nonetheless, maintaining
fluency, discourse coherence, and cultural grounding remains a core open challenge.
3.3.2 Content Transformation
Beyond generating basic textual output, content transformation tasks aim to reshape Tibetan content across modalities and
levels of abstraction, enabling compression, re-expression, and multimodal synthesis. Representative tasks include:
• Summarization: summarization generates concise Tibetan text while retaining core meaning, with potential applications
in scripture condensation, news, education, and policy documents83. Progress is limited by the lack of aligned article-
summary pairs and strong stylistic variability across domains. Existing work primarily explores extractive approaches or
few-shot adaptation of multilingual models such as mT571 and BART6. Instruction tuning and synthetic data generation
have recently emerged as data augmentation strategies. However, abstractive summarization still suffers from fluency
issues, coherence drift, and factual inconsistency, highlighting the need for Tibetan-specific benchmarks and evaluation
protocols.
• Speech Synthesis: speech synthesis covers vocoding, TTS, and speech conversion76,79. Lightweight vocoders fine-tuned
on limited Tibetan data show preliminary success, while universal vocoders trained on large multilingual datasets can
generalize to Tibetan with minimal adaptation74. Tibetan TTS has strong relevance for accessibility, cultural preservation,
and educational support, but progress is hindered by the absence of phoneme-aligned speech corpora, non-transparent
grapheme-to-phoneme mapping, and dialectal variation. Neural architectures such as Tacotron, FastSpeech, WaveNet95,
and HiFi-GAN96 have been explored, yet current systems still struggle with prosody, tonal accuracy, and intelligibility.
Speech conversion for Tibetan, covering speaker, dialect, or emotion transfer, remains almost entirely unexplored.
3.3.3 Interactive Context-Aware Generation
Moving beyond static text output, interactive context-aware generation focuses on producing adaptive responses conditioned on
evolving user input and conversational history, enabling Tibetan language models to support real-time knowledge access and
human-like interaction. Core tasks include:
11/41

--- Page 12 ---

• Question Answering: QA aims to produce answers to user queries based on a given context, such as a passage, a
knowledge base, or multimodal input16. In Tibetan, QA is valuable for educational tutoring, cultural knowledge access,
and low-resource information retrieval17,88. Both extractive and generative QA are relevant, but progress is limited by the
absence of large Tibetan QA datasets and domain-specific knowledge resources in areas like Buddhist studies, Tibetan
medicine, and historical archives. While multilingual instruction-tuned models offer transfer learning opportunities,
persistent challenges include factual reliability, domain terminology grounding, and culturally aware evaluation.
• Dialogue Generation: DG produces contextually appropriate responses in an interactive setting17,23,24. Potential Tibetan
applications include educational assistants, cultural heritage interfaces, and domain-specific consultation systems. Despite
advances in multilingual LLMs, Tibetan dialogue research remains underdeveloped due to the lack of conversational
corpora and domain-curated dialogue datasets. Existing efforts rely on instruction tuning and few-shot prompting on
multilingual backbones, but challenges remain in multi-turn consistency, low-resource adaptation, and cultural relevance
of generated responses74.
3.3.4 Cross-Modal Creative Generation
At the creative frontier of Tibetan AI, cross-modal generation extends beyond text-only interaction to synthesize Tibetan
language outputs conditioned on visual or auditory inputs, enabling culturally grounded multimodal applications. Current work
in this direction primarily explores the following task:
• Multimodal Generation: MG produces Tibetan text conditioned on inputs such as images, audio, or video, covering
tasks like image captioning17,18,97,98, VQA63, and cross-modal retrieval99. It has potential applications in digital heritage
preservation, educational tools, and accessibility technologies. However, progress is constrained by the lack of aligned
Tibetan multimodal datasets and vision-language models with native Tibetan support. Current efforts mainly adapt
multilingual architectures such as BLIP100, BLIP-214, and LLaVA101 through cross-lingual transfer. While early results
show that these models can generate basic Tibetan captions, major challenges persist in fluency, cultural grounding, and
standardized evaluation.
12/41

--- Page 13 ---

4 Tibetan AI & Application
In this section, we will introduce current AI models on Tibetan and their application.
4.1 Tibetan AI
Most AI models for Tibetan language processing fall within the domain of deep learning, primarily leveraging attention-based
architectures with NLP models, even LLMs. A limited body of research focuses on the construction of Tibetan knowledge
graphs, alongside some direct rule-based methods grounded in Tibetan linguistic rules. so do machine learning models. Notably,
a few recent studies have begun to explore novel applications involving memristors.
4.1.1 Rule-based Method
Rule-based methods were among the earliest approaches used in Tibetan AI, particularly in tasks such as word segmentation,
morphological analysis, and transliteration. Given the agglutinative and syllable-centric nature of Tibetan, researchers developed
handcrafted rules based on linguistic knowledge, such as syllable structure patterns, affix lists, and syntactic templates to analyze
text. Tools like PyBo102 and Botok103 follow this paradigm, relying on precompiled dictionaries and manually defined grammar
rules to segment words or normalize orthography. While rule-based systems offer high interpretability and perform well on
formal texts like classical scriptures, they often struggle with informal or domain-shifted data and require significant manual
effort to update. Despite their limitations, rule-based methods remain foundational in Tibetan AI, especially in tokenization and
preprocessing pipelines, and are often combined with statistical or neural models in hybrid systems. Here, we summarize the
following methods:
• PyBo102: a rule-driven tokenizer that relies on the THL lexicon and a set of manually defined syllable-matching strategies.
It uses handcrafted heuristics to detect syllable boundaries and map them to lexical entries, making it particularly effective
for classical and well-structured Tibetan texts. However, its reliance on fixed lexicon entries limits adaptability to modern
or domain-specific vocabulary.
• Botok103: a dictionary-assisted normalization and tokenization toolkit that employs hierarchical rule templates to correct
orthographic variations. It integrates lexicon lookup with layered grammar rules, enabling multi-stage segmentation and
cleaning. While Botok improves consistency in spelling normalization, its performance still depends on the coverage of
predefined rule sets.
• TibetanMorph104: a morphological analyzer based on manually compiled affix tables and rule-based morpheme
decomposition. It explicitly encodes Tibetan inflectional and derivational patterns and performs stepwise affix stripping
to recover lemma forms. Although highly interpretable, it struggles with irregular morphological variants and dialectal
spellings.
• THL LexTools105: one of the earliest rule-based Tibetan processing toolkits developed by the THL. It combines lexicon
lookup, regular-expression-based segmentation, and syllable structure modeling to support tasks such as transliteration,
tokenization, and lexicon extraction. Despite its age, LexTools remains a foundational reference system in Tibetan digital
humanities.
• THL POS Tagger81: a rule-based part-of-speech tagging module developed by the Tibetan and Himalayan Library. It
assigns coarse- and fine-grained POS labels by combining lexicon lookup with handcrafted morpho-syntactic templates.
Although limited by fixed tagging schemas, it established one of the earliest standardized POS annotation conventions in
Tibetan AI.
• TibetanRuleSeg86: a regular-expression-based segmentation system built around syllable delimiter heuristics, particularly
using the tsheg mark as an anchor. It applies sequential rule matching to detect potential word boundaries but lacks
semantic awareness, making it prone to over-segmentation in free-form text.
• TibWordSplitter106: a lightweight heuristic boundary detection tool that performs affix stripping and rule-based syllable
alignment before segmentation. It assumes a fixed syllable order pattern and resolves ambiguous splits using handcrafted
priority rules. Its simplicity ensures fast processing, but it is less effective in handling noisy or code-mixed Tibetan
inputs.
• THDL Phonetic Rules107: this is a standardized mapping framework that converts Tibetan script into Wylie or IPA
representations using explicitly defined phonetic rules. These mappings encode character-level pronunciation patterns
and serve as a linguistic foundation for downstream transliteration and ASR preprocessing pipelines.
13/41

--- Page 14 ---

• Unicode Normalization Rules108: A rule-defined preprocessing pipeline designed to resolve inconsistencies in Tibetan
Unicode encoding. It rewrites deprecated code points, normalizes combining character sequences, and removes invalid
diacritic orders to ensure compatibility across downstream Tibetan AI systems.
Overall, these rule-based systems established the fundamental processing pipeline for Tibetan AI, particularly in low-
resource settings where annotated corpora and pretrained models are scarce. Although their deterministic nature limits
adaptability to informal usage and domain shifts, they provide high interpretability and remain indispensable in preprocess-
ing and tokenization stages. More importantly, many modern statistical and neural architectures still integrate rule-based
components, forming hybrid systems that leverage both handcrafted linguistic knowledge and data-driven modeling.
4.1.2 Machine Learning
Machine learning remains useful for low-resource Tibetan tasks beyond deep learning’s scope. Models such as logistic
regression109, SVM110, random forests111, and gradient boosting112 have been applied to Tibetan text classification, sentiment
analysis, and topic detection using handcrafted features. Under extremely limited annotated corpora, these classical models
offer a practical alternative due to their lower data requirements and higher interpretability. Feature extraction typically
relies on TF-IDF representations113 of syllable or character n-grams114, lexicon-matching indicators derived from rule-based
preprocessing, and linguistic signals such as affix frequency or orthographic normalization flags. These pipelines have also been
adopted in tasks like OCR error detection115, scripture classification, dialect identification, and short-text intent categorization
within Tibetan digital humanities. In many cases, rule-based preprocessing is coupled with classical classifiers to form hybrid
feature engineering workflows that inject linguistic priors into statistical models. Although constrained by the expressiveness
of handcrafted features, these approaches remain a strong baseline in Tibetan AI and serve as an intermediate step between
deterministic rules and end-to-end neural architectures. To clarify their functional roles and methodological differences, the key
categories of classical Tibetan AI models are outlined as follows:
• Linear Regression109: a foundational regression model applied to Tibetan AI tasks that involve continuous prediction,
such as readability estimation and OCR confidence scoring. It relies on handcrafted numeric features derived from syllable
frequency, lexicon coverage, or affix density and serves as a baseline for evaluating more complex regression-based
architectures.
• Logistic Regression109: a lightweight linear classifier commonly used for Tibetan text categorization, sentiment analysis,
and intent detection. It operates on sparse TF-IDF113 or n-gram114 representations and remains a strong baseline due to
its interpretability and suitability for low-resource training scenarios.
• Support Vector Machine110: a widely adopted margin-based classifier effective in handling high-dimensional Tibetan
feature spaces derived from character or syllable n-grams. SVM110 is particularly useful for tasks such as dialect
discrimination, topic classification, and sentiment polarity detection in resource-constrained Tibetan datasets.
• Random Forests111: an ensemble-based classification model that aggregates multiple decision trees to improve robustness
against noisy Tibetan input, including OCR-generated errors and informal text. Its ability to capture non-linear feature
interactions makes it suitable for feature-rich pipelines that integrate lexicon-derived indicators.
• Gradient Boosting Model112: boosting-based classifiers such as XGBoost112 and LightGBM116 that iteratively correct
misclassified instances to enhance prediction accuracy. When combined with rule-informed feature engineering, these
models achieve competitive performance on Tibetan news classification, scripture categorization, and domain-specific
document filtering.
• Hidden Markov Model117: a generative sequence model applied to Tibetan word segmentation and POS tagging by
modeling tag transition probabilities across syllable sequences. Despite its reliance on Markov assumptions, HMM
established one of the earliest probabilistic frameworks for structured Tibetan text processing.
• Conditional Random Field118: a discriminative sequence labeling model that relaxes the independence assumptions
of HMM and incorporates rich handcrafted features such as affix tags, lexicon matches, and syllable boundary cues.
CRF remains one of the most effective classical approaches for Tibetan segmentation and POS tagging prior to neural
encoders.
• Maximum Entropy Model119: a log-linear model used for Tibetan tagging and transliteration by maximizing the
likelihood of label assignments under feature-based constraints. It supports flexible feature integration and has been used
in early Tibetan AI pipelines to model context-dependent linguistic decisions.
14/41

--- Page 15 ---

4.1.3 Deep Learning
Beyond classical machine learning baselines, early deep learning research in Tibetan AI primarily adopted recurrent neural
architectures such as RNN120, LSTM121, and GRU122 to model sequential dependencies in syllable streams, with bidirectional
variants (Bi-RNN123, Bi-LSTM124, Bi-GRU122,124) introduced to capture contextual information from both preceding and
following tokens. These models evolved into Seq2Seq8 frameworks for tasks like Tibetan-Chinese transliteration and low-
resource translation. To improve local pattern extraction, CNN-RNN125 hybrid structures such as CNN-LSTM126, CNN-
RNN125, and CRNN91 were employed in OCR post-correction and scripture classification under noisy data conditions. For
token-level sequence labeling tasks, CRF-enhanced neural architectures118 like BiLSTM-CRF118,127 and BiGRU-CRF118,122,124
became the dominant paradigm due to their ability to impose structured decoding constraints beyond independent softmax
classification. In parallel, graph-oriented modeling began to emerge, where knowledge graph128 embeddings and early GNN-
style129 representations were used to encode non-sequential dependencies such as scripture ontology, dialect lineage, and lexical
borrowing relations. These graph-augmented neural models marked an important transition from purely sequential learning to
knowledge-aware representation, forming a methodological bridge. To outline the evolution of these neural approaches more
clearly, the major deep learning architectures adopted in Tibetan AI can be categorized as follows:
• RNN120/LSTM121/GRU122: foundational recurrent architectures used to model syllable-level sequential dependencies in
Tibetan text. LSTM121 and GRU122 address the gradient vanishing problem of vanilla RNN120 and serve as early neural
baselines for tasks such as transliteration and sequence classification.
• Bi-RNN123/Bi-LSTM124/Bi-GRU122,123: bidirectional extensions designed to capture contextual signals from both past
and future tokens, improving performance on Tibetan segmentation, dialect identification, and OCR post-correction
under limited annotated data.
• Seq2Seq8: encoder-decoder architectures built upon LSTM121 or GRU122 backbones for low-resource Tibetan-Chinese
translation and romanization, enabling conditional generation by learning aligned representations between source and
target sequences.
• CNN90,130: sentence/short-text encoders that extract local n-gram patterns via 1D convolutions and pooling; effective for
Tibetan character/syllable-level classification and robust to orthographic variation; also used as convolutional backbones
for OCR feature extraction, such Text CNN131, Char-CNN132 and Dilated CNN133.
• CNN-RNN Hybrids125: hybrid networks like CNN-LSTM126, CNN-RNN125 and CRNN91 that combine convolutional
layers for local pattern extraction with recurrent layers for global dependency modeling. These architectures are effective
for Tibetan OCR error correction, scripture classification, and noisy document analysis.
• CRF-enhanced Architecture118: neural sequence labeling models like BiLSTM-CRF127 and BiGRU-CRF118,122,134
that integrate CRF118 decoding to enforce structured label consistency, becoming the dominant paradigm for Tibetan
word segmentation, POS tagging, and morphological analysis.
• Graph-Augmented Neural Model129: methods that incorporate knowledge graph embeddings128 or graph neural
representations129 to encode non-sequential relations such as scripture ontology and dialectal lineage, introducing
relational inductive bias beyond linear token order.
4.1.4 Transformer Architecture
Transformer architecture2 was introduced to overcome the inherent limitations of sequential neural models such as RNN120,
Bi-RNN123, LSTM121, and Bi-LSTM124, which process tokens in a strictly left-to-right or bidirectional manner and therefore
suffer from limited parallelization and difficulty in modeling long-range dependencies121. In contrast, the Transformer employs
a fully attention-based computation paradigm that removes recurrence entirely120,123. Instead of propagating information
step by step, it computes token representations by directly attending to all other positions in the sequence, assigning learned
attention weights that reflect contextual relevance2. This global attention mechanism enables parallel computation across all
tokens2, resulting in more efficient training, better scalability to long sequences, and greater modeling flexibility compared to
RNN-based architectures120,123. Consequently, the Transformer2 has become the standard backbone for large-scale pre-trained
language models and LLMs21,22,26,27,30,31. To further illustrate the evolution of Transformer-based architectures for Tibetan
AI, the major categories can be summarized as follows:
• Transformer Encoder-Decoder Framework2: the foundational architecture introducing multi-head self-attention and
fully parallel sequence modeling, replacing recurrent computation with global dependency learning.
15/41

--- Page 16 ---

• BERT1 & RoBERTa-style Masked Pre-trained Model3: bidirectional Transformer2 encoders trained via masked
language modeling, providing contextual Tibetan embeddings that generalize across classification and tagging tasks.
• CINO88 & Tibetan-adapted PLMs88: domain-specific or cross-lingual Transformer2 variants fine-tuned on Tibetan
corpora using syllable-aware tokenizers and script-adapted vocabulary construction.
• Domain-adaptive Tokenization135 & Subword Modeling136: tokenizer strategies such as SentencePiece and byte-level
BPE designed to address Tibetan syllable segmentation and orthographic variability, improving pretraining efficiency.
• Lightweight Architectures for Low-resource Settings137,138: state-space Transformer alternatives designed to reduce
computation while preserving long-range dependency modeling, suitable for Tibetan low-resource deployment.
• Knowledge-enhanced Transformer2,128 & Graph-aware PLMs79,128,129: models integrating knowledge graph em-
beddings or graph neural modules into Transformer layers to inject relational Tibetan cultural and lexical priors beyond
surface token co-occurrence.
4.1.5 Large Language Model
LLMs are large-scale pretrained language models with hundreds of millions to billions of parameters, trained on massive
text corpora using self-supervised objectives such as next-token prediction or masked language modeling1,2. Built upon the
Transformer architecture, LLMs exhibit strong capabilities in both language understanding and generative reasoning2. After
pretraining3, these models can be efficiently adapted to downstream tasks such as classification, translation, summarization, and
question answering via full fine-tuning, instruction tuning, or lightweight prompting strategies17,18. Their emergent ability to
perform few-shot and zero-shot generalization makes them especially suitable for low-resource languages, including Tibetan44,
where annotated data is scarce but linguistic transfer from high-resource languages can be leveraged through cross-lingual
pretraining. As the Transformer paradigm established itself as the dominant backbone for modern language modeling, research
focus gradually shifted away from architectural innovation toward scaling parameterization and developing model families with
specialized training strategies. Accordingly, the most representative LLM families are summarized as follows:
• GPT Family10,20–22,139: a proprietary series of instruction-tuned large-scale models developed by OpenAI, including
GPT-420, GPT-4o21, GPT-4.121, and the upcoming GPT-522 generation. These models demonstrate strong multilingual
reasoning and contextual understanding; however, their tokenizer is not explicitly optimized for Tibetan, which leads to
fragmented syllable segmentation. Despite this limitation, GPT-based models still achieve surprisingly high zero-shot
performance on Tibetan reasoning and classification tasks due to powerful cross-lingual generalization.
• LLaMA Family23–25: an open-source Transformer model series released by Meta AI, with versions such as LLaMA
3.1-8B25, 3.1-40B25, and 3.1-70B25. While their baseline tokenizer is not Tibetan-aware, their open-source nature makes
them highly suitable for and vocabulary extension. In Tibetan adaptation experiments, LLaMA-based models show
significant performance gains once domain-specific tokenizers or LoRA140 adapters are introduced.
• Qwen Family28–31: multilingual foundation models from Alibaba Cloud, available in variants such as Qwen 2.5-7B30,
2.5-32B30, and 2.5-72B30. Compared to GPT10,20–22 and LLaMA23–25, the Qwen tokenizer provides better coverage for
Asian Unicode ranges, resulting in less subword fragmentation for Tibetan syllables. This leads to stronger baseline
performance before fine-tuning and makes Qwen models a competitive backbone for Tibetan-specific PEFT141.
• Claude Family35–38: Anthropic’s safety-aligned LLM lineup, including Claude 3.5 Opus37 and Claude 3.5 Sonnet37.
Although Claude models do not expose tokenizer customization, they show strong robustness in Tibetan instruction
following and semantic alignment tasks due to conservative decoding strategies and high factual consistency.
• Gemini Family32–34: Google DeepMind’s multimodal LLM series, including Gemini 1.5 Pro33 and Gemini 1.5 Flash33.
Their extended context window enables effective document-level Tibetan processing. However, tokenizer fragmentation
remains a bottleneck, making adaptation through external Tibetan vocabulary injection or prompt-level stabilization
necessary.
• DeepSeek Family26,27: open-source efficient LLMs released in variants such as DeepSeek-V327 and DeepSeek-R126.
Their compact architecture and QLoRA-friendly142 parameterization make them particularly suitable for low-resource
Tibetan adaptation. In internal benchmarks, DeepSeek-based models show favorable efficiency-performance trade-offs in
Tibetan fine-tuning scenarios under limited GPU resources.
16/41

--- Page 17 ---

Table 1. Summary of Common Models or Methods for Tibetan AI & Task-Oriented Categorization
Domains
Name
Task
Discriminative Task
Generative Task
WS
POS
NER
TC
SS-ED
SR
OCR
MT
TG
SUM
TTS
QA
DG
MG
RB
PyBo102
✓
(✓)
(✓)
✗
✗
✗
✗
(✓)
✗
✗
✗
(✓)
✗
✗
Botok103
✓
(✓)
(✓)
✗
✗
✗
✗
(✓)
✗
✗
✗
(✓)
✗
✗
THL POS tagger81
✓
✓
(✓)
✗
✗
✗
(✓)
(✓)
✗
✗
✗
(✓)
✗
✗
ML
Linear Regression109
✗
✗
✗
✓
✓
✗
✗
✗
✗
✗
✓
✗
✗
✗
Logistic Regression109
✗
✗
✗
✓
✓
✗
✗
✗
✗
✗
✓
✗
✗
✗
Random Forest111
✗
✗
✗
✓
✓
✗
✗
✗
✗
✗
✓
✗
✗
✗
SVM110
✗
✗
✗
✓
✓
✗
✗
✗
✗
✗
✓
✗
✗
✗
XGBoost112
✗
✗
✗
✓
✓
✗
✗
✗
✗
✗
✓
✗
✗
✗
CRF118
✓
✓
✓
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
DL
RNN120
✓
✓
✓
✓
(✓)
✓
(✓)
✗
✗
✗
✗
(✓)
✗
✗
LSTM121
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
(✓)
✓
(✓)
✗
Bi-RNN123
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
(✓)
✓
(✓)
Bi-LSTM124
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
(✓)
✓
(✓)
Seq2seq8
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
(✓)
✓
(✓)
GRU122
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
(✓)
✓
(✓)
✗
BERT1
✓
✓
✓
✓
✓
✗
✗
(✓)
(✓)
(✓)
✗
✓
(✓)
✗
CINO88
✓
✓
✓
✓
✓
✗
✗
(✓)
(✓)
(✓)
✗
✓
(✓)
✗
RoBERTa3
✓
✓
✓
✓
✓
✗
✗
(✓)
(✓)
(✓)
✗
✓
(✓)
✗
CNN-LSTM126
✓
✓
✓
✓
(✓)
✓
✓
(✓)
(✓)
(✓)
(✓)
(✓)
✓
✓
CNN-RNN125
✓
✓
✓
✓
(✓)
✓
✓
(✓)
✓
(✓)
✓
(✓)
✓
✓
BiLSTM-CRF127
✓
✓
✓
✓
(✓)
(✓)
(✓)
✗
✗
✗
✗
(✓)
✗
✗
BiGRU-CRF122,127
✓
✓
✓
✓
(✓)
(✓)
(✓)
✗
✗
✗
✗
(✓)
✗
✗
CNN90,130
(✓)
(✓)
(✓)
✓
(✓)
✓
✓
(✓)
(✓)
(✓)
(✓)
(✓)
(✓)
(✓)
Transformer2
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
Mamba137,138
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
(✓)
CRNN91
(✓)
(✓)
(✓)
✓
(✓)
✓
✓
(✓)
(✓)
(✓)
✗
(✓)
(✓)
✓
GNN129
(✓)
(✓)
✓
✓
(✓)
✗
(✓)
(✓)
(✓)
(✓)
✗
✓
(✓)
(✓)
Knowledge Graph128
✗
✗
(✓)
(✓)
(✓)
✗
✗
(✓)
(✓)
(✓)
✗
✓
✓
(✓)
LLM
GPT-4o21
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
GPT-o1139
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
GPT-4.121
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
GPT-522
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
LlaMA3.1-405B25
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
LlaMA3.1-70B25
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
LlaMA3.1-8B25
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
Qwen2.5-72B30
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
Qwen2.5-32B30
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
Qwen2.5-7B30
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
Claude-3-5-Sonnet37
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
Gemini-1.5-Flash33
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
Deepseek-V327
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
Deepseek-R126
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
4.1.6 Summary: Tibetan AI & Specific Task
As shown in Table 1, we provide a task-oriented overview of Tibetan AI methods across four paradigms: RB, ML, DL,
and LLMs. RB systems (e.g., PyBo102, Botok103) remain effective for basic segmentation but lack generative capacity. ML
models support mainly classification and error detection. DL architectures (RNN120, LSTM121, CRF-variants118,127,134, CNN
hybrids125,126, Transformer2, GNN128,129) progressively expand coverage to both sequence labeling and generation tasks, with
Transformer achieving near-universal applicability. LLMs (GPT10,20–22, LLaMA23–25, Qwen28–31, Claude35–38, Gemini32–34,
DeepSeek26,27 series) demonstrate full coverage across all task types with strong zero/few-shot ability, indicating a clear
paradigm shift from task-specific modeling to unified instruction-based Tibetan language processing.
However, the growing model scale introduces deployment and efficiency challenges for low-resource Tibetan scenarios,
motivating the exploration of hardware-efficient paradigms such as memristor-based neuromorphic acceleration143.
17/41

--- Page 18 ---

4.1.7 Emerging Frontier: Memristor
Memristors are nanoscale electronic devices that intrinsically couple data storage and computation through programmable
resistance states, enabling in-memory computing paradigms that bypass the von Neumann bottleneck144,145. Unlike conven-
tional CMOS-based architectures, memristor crossbar arrays can perform matrix-vector multiplication in constant time via
analog Ohmic conduction, achieving ultra-high energy efficiency and parallelism. These properties make memristor-based
neuromorphic hardware particularly attractive for deploying deep neural models under strict computational and power con-
straints, which is highly relevant for low-resource Tibetan AI scenarios where large LLMs are difficult to deploy on traditional
GPU-centric infrastructures. Based on this hardware foundation, the integration of memristors into neural computation can be
further analyzed from the following perspectives:
• Crossbar Analog MatMul144: memristor arrays execute y = Wx in a single analog conduction step, removing the
memory, compute gap and fitting the dense projection layers used in Tibetan LLM inference.
• Tibetan-Oriented Memristive Layers143: by encoding Tibetan token or syllable embeddings into conductance states,
crossbars act as in-memory Tibetan feature extractors, replacing conventional digital MAC-based neural units.
• LoRA/PEFT Mapping for Tibetan Adaptation140,141: Tibetan-specific lightweight adapters (LoRA140, QLoRA142,
PEFT141) can be directly instantiated on resistive grids, enabling low-power inference where only adaptation weights are
activated.
• On-Device Tibetan Inference143,144: the high parallelism and low energy footprint of memristive hardware make local
deployment of Tibetan translation, OCR correction, and dialogue systems feasible without cloud GPUs.
4.2 Application
Development of Tibetan AI spans both conventional digital computation frameworks and emerging neuromorphic paradigms.
On one hand, traditional Tibetan AI research has produced a series of task-specific systems, including spelling error correction,
machine translation, and recent attempts to adapt LLMs through fine-tuning strategies. On the other hand, the rise of memristor-
based in-memory computing introduces a potential shift in deployment methodology, enabling energy-efficient Tibetan language
inference on localized edge devices. This subsection provides a structured overview of these two application pathways.
4.2.1 Traditional Tibetan AI
Before the emergence of large-scale instruction tuning and neuromorphic Tibetan models, most research in Tibetan AI was
concentrated around a set of traditional computational tasks that form a layered processing stack, including lexical preprocessing,
document recognition, translation, speech modeling, and information extraction. We will introduce them in the following part:
→Text Processing: Tibetan text processing relies on a pipeline of tokenization, syllable segmentation, orthographic normal-
ization, and standardized EWTS-to-Unicode conversion146. Rule-based lexicon-driven preprocessors such as PyBo102 and
Botok103 operationalize these steps using curated lexical patterns and segmentation rules147–157. To move beyond handcrafted
heuristics, CRF-based statistical taggers158 were introduced for boundary detection and morphological segmentation, followed
by BiLSTM-CRF architectures159 that apply neural sequence labeling to capture syllable-level dependencies and reduce feature
engineering overhead.
Table 2. Tibetan AI on Text Processing
Model
Category
Reference
Rule-based Model
Spelling Error Detection
102,103,146–155,160
Component Recognition
LSTM
Spelling Error Detection
156,157
Text Classification
85
Component Recognition
161
CRT-based Model
Tibetan Component Recognition
75,162
Word Segmentation
77,78,163–165
Hybrid Model
Text Classification
166
As shown in Table 2, we summarize the existing commonly used models. Since Tibetan language datasets are scarce
and the language is a niche language, there are few related fields. The models used are basically the same. Especially
BiLSTM-CRF77,78,162–165, models in these papers are almost the same model with only minor adjustments to the parameters.
Other models147–155 are published in Chinese journal, but not open-source.
18/41

--- Page 19 ---

→Document OCR & Handwriting Recognition: Tibetan OCR79,115,167 and HWR systems168–170 typically adopt a mod-
ular architecture combining page segmentation with neural sequence recognition. Character recognition is commonly im-
plemented using CNN-RNN models with CTC decoding125,163,166, or Transformer-based attention recognizers2,166, with
lexicon-constrained decoding enforcing EWTS146 and Unicode validity. Hybrid decoding workflows integrate language model
priors to stabilize output under font distortion, handwritten variance, and stacked diacritic patterns. Practical pipelines include
optional post-correction layers that apply grapheme normalization, syllable-level alignment, and lexical refinement to further
reduce CER/WER and improve downstream usability82,171,172.
→Machine Translation: traditional Tibetan MT pipelines evolved from phrase-based statistical machine translation (SMT) to
neural encoder-decoder architectures92,93,173–178. Early systems adopted phrase extraction and alignment under Moses-style
SMT, later replaced by RNN-based sequence-to-sequence models8,120 with attention. With the advent of the Transformer
architecture, most Tibetan MT work shifted to Marian and fairseq-based Transformer baselines1,2. Recent multilingual
backbones such as mBART506, mT571, and NLLB94 provide parameter-sharing across languages, enabling low-resource
Tibetan translation through transfer learning and subword vocabulary alignment rather than fully supervised training. Although
platforms like Google Translate3 have recently introduced Tibetan support, their Tibetan translation performance remains
shallow due to limited supervised data and the lack of Tibetan-specific linguistic priors, especially in religious, medical, and
colloquial registers.
→Speech Processing: Tibetan ASR systems179–182 began with conventional hybrid HMM-DNN architectures183, later
replaced by end-to-end CTC-based CNN-RNN125 pipelines following DeepSpeech-style designs184. With the emergence of
self-supervised pretraining, wav2vec 2.095 and Conformer-based models185 became the dominant architectures for Tibetan
speech recognition, enabling low-resource adaptation via fine-tuning on limited Tibetan audio. For TTS, early parametric
systems were replaced by Tacotron/Transformer-TTS186 front-ends combined with neural vocoders such as WaveNet95 or
HiFi-GAN96, providing higher fidelity for multi-dialect Tibetan synthesis76,89.
→Information Extraction & Classification: early Tibetan IE and classification tasks used lexical pattern matching and
CRF-based sequence tagging118, followed by traditional machine learning classifiers such as SVM110 and random forests111
with handcrafted linguistic features187. With the availability of multilingual encoders, BiLSTM-CRF architectures127 and
fine-tuning of mBERT1, XLM-R188, or mT571 became standard, allowing better generalization across domain-specific Tibetan
terminology and named entities without requiring large manually engineered feature sets84,189–194 .
As model complexity increased across these individual tasks, research attention gradually shifted from task-specific
architectures toward unified Tibetan pre-trained models, like LLMs17,18,21,23,26,27, capable of performing OCR post-correction,
translation, ASR transcription, and information extraction within a single instruction-following framework. This paradigm
shift has led to the emergence of Tibetan-centric LLM initiatives that aim to consolidate multiple task abilities into a single
generative backbone.
• Sun-Shine18: the first Tibetan-centric LLM trained on the TIB-STC corpus via pretraining and supervised fine-tuning,
targeting general Tibetan understanding and instruction following with unified tokenization and EWTS-compatible
vocabulary design.
• Sun-Shine 2.017: an extended version incorporating CoT-style supervision, preference alignment, and safety filtering,
enabling more robust reasoning, multi-turn dialogue, and controllable generation across Tibetan cultural, legal, and
medical domains.
To the best of our knowledge, Sun-Shine18 and its upgraded variant Sun-Shine 2.017 currently represent the only two Tibetan-
centric large language models explicitly designed with dedicated Tibetan pretraining, instruction tuning, and alignment
objectives. For more details, please refer to Appendix D
For other pre-trained Tibetan language models16,80,83,87,195,196, existing efforts primarily focus on encoder-style architec-
tures with Tibetan-adapted tokenizers24 or PEFT141 strategies, which enhance representation quality for downstream tasks such
as classification87 and NER83 but do not offer the full generative and instruction-following capabilities of LLM-scale models.
4.2.2 Memristor-Based Neuromorphic Tibetan AI
To the best of our knowledge, no published work explicitly integrates memristor-based in-memory computing with Tibetan OCR,
ASR, machine translation, or neural sequence modeling. Existing neuromorphic accelerators based on RRAM or PCM crossbar
arrays have been primarily evaluated on Latin or Chinese character recognition197,198, generic sequence models for English
NLP199,200, or language-agnostic Transformer inference201,202. These architectures demonstrate that convolutional filters,
recurrent weight matrices, and attention projections can be mapped onto analog conductance states to achieve high-throughput
MAC operations without digital memory shuttling. However, none of these systems account for the unique Unicode block
3https://translate.google.com/
19/41

--- Page 20 ---

structure, stacked diacritics, and syllable-centric token sparsity of Tibetan script, indicating a clear architectural gap between
existing memristive accelerators and the linguistic requirements of Tibetan AI workloads.
Under this extension perspective, Tibetan-aware neuromorphic models can be derived by mapping script-specific convolu-
tional kernels, CTC-style OCR decoders, and subword embedding matrices directly onto resistive crossbar arrays. For OCR,
existing RRAM-based CNN accelerators197,198 could be adapted to recognize Tibetan stacked glyph structures by encoding
syllable-level visual primitives as conductance patterns. For text modeling, memristor LSTM and seq2seq accelerators199,200
provide a direct analog to BiLSTM-style Tibetan segmentation models, while crossbar-based attention units201,202 offer a
hardware-aligned pathway for Tibetan subword attention computation originally implemented in mBART1 or mT5-style71
architectures. This indicates that neuromorphic Tibetan AI is technically feasible through adaptation of existing analog MAC
accelerators, but remains an unexplored research direction without task-specific architectural tailoring.
Recently, inspired by the feasibility of mapping Tibetan Unicode features to resistive states, Liu et al.143,203 demonstrated
a memristor crossbar array that performs syllable-component recognition by encoding Tibetan characters into binary and
matching component patterns through in-memory current comparison. This work marks the first attempt to apply memristive
computing to Tibetan script processing, indicating that hardware-centric approaches can be extended beyond generic OCR
toward Tibetan-specific linguistic structures.
20/41

--- Page 21 ---

5 Challenge
We address the challenges and discuss solutions to the adoption of AI in Tibetan.
5.1 Data Scarcity
In Tibetan AI, data scarcity encompasses not only the limited quantity of resources but also their restricted accessibility, narrow
domain coverage, and lack of consistent annotation. Publicly available corpora are rare and largely confined to religious and
literary texts, with minimal representation of modern domains such as news, science, or social media. Most resources are
monolingual, while parallel corpora, speech data, and multimodal datasets are even scarcer. Rich linguistic annotations, such
as tokenization, part-of-speech tags, syntactic dependencies, and named entities are limited, and inconsistencies in encoding
standards and annotation schemes further hinder interoperability. These gaps include the absence of large-scale, domain-diverse
monolingual corpora, high-quality parallel datasets, richly annotated resources for supervised AI tasks, multimodal alignments
with speech or images, and standardized benchmarks for evaluation. The resulting shortage restricts model performance and
generalization, limits the applicability of state-of-the-art architectures, narrows the range of downstream applications, and
impedes reproducibility, thereby widening the technological gap between Tibetan and high-resource languages.
→Potential Solution: recent studies have explored multiple strategies to alleviate data scarcity. These include the application
of data augmentation techniques such as back-translation, paraphrasing, and synthetic text generation; the use of transfer
learning and cross-lingual pretraining from high-resource languages; community-driven data creation through crowdsourcing
and academic collaborations; and domain adaptation approaches that incrementally fine-tune models on Tibetan-specific
corpora. While each method offers partial mitigation, their combined adoption, together with the establishment of publicly
accessible benchmarks, appears essential for sustainable progress in this low-resource language context.
5.2 New Knowledge Adaptation
A distinctive challenge in Tibetan AI is the adaptation to new knowledge arising from the language’s ongoing modernization.
This process includes the growing digitization of Tibetan communication, the emergence of internet slang and neologisms,
and lexical innovations influenced by contemporary Chinese, including semantic shifts and structural simplifications. Such
developments generate a dynamic linguistic landscape in which vocabulary, orthography, and usage patterns evolve faster than
traditional resources can capture. Without timely incorporation of these changes into corpora, lexicons, and models, AI systems
risk becoming outdated, unable to accurately interpret contemporary expressions, or misaligned with real-world communication
contexts.
→Potential Solution: to address this challenge, continuous corpus updating and dynamic lexicon expansion are essential,
leveraging web mining, social media monitoring, and community-driven annotation to capture emerging terms and usages.
Domain-adaptive training, incremental fine-tuning, and terminology alignment with high-resource languages such as modern
Chinese can facilitate rapid integration of new knowledge. Furthermore, establishing automated pipelines for detecting and
validating neologisms would enable AI systems to maintain relevance in a rapidly evolving linguistic environment.
5.3 Manual Calibration
Manual calibration remains a persistent challenge in Tibetan AI due to the inherent difficulties of large-scale human verification.
The process is constrained by the scarcity of qualified annotators, the considerable time and effort required to inspect vast
quantities of data, and the variability introduced by inconsistent standards across different experts. Discrepancies in annotation
guidelines, segmentation rules, and linguistic interpretations can lead to uneven quality and hinder reproducibility. The challenge
is further compounded by the sheer volume of Tibetan text, particularly in projects involving large corpora or real-time data
streams, making comprehensive manual review impractical.
→Potential Solution: a promising approach is to develop standardized AI-based verification systems capable of performing
the majority of calibration tasks, thereby reducing reliance on manual labor. Such systems can be trained on high-quality,
expert-verified datasets to ensure alignment with agreed annotation standards, while incorporating active learning mechanisms
to flag ambiguous or low-confidence cases for human review. In this hybrid workflow, the AI serves as a first-pass filter,
enabling human annotators to focus on complex or contentious instances, thus improving both efficiency and consistency.
5.4 Encoding Standard & Inefficiency
Encoding Tibetan script in digital environments presents unique challenges that affect both interoperability and processing
efficiency. Although Unicode provides a standardized framework for Tibetan characters, inconsistencies in its adoption across
software platforms, operating systems, and datasets often lead to compatibility issues. Historical reliance on legacy encodings
and custom font systems has resulted in fragmented digital resources, where identical characters may be represented by different
code points or rendered inconsistently. Such variability complicates text normalization, segmentation, and search, increasing
preprocessing costs and reducing the reliability of downstream NLP tasks. These challenges are magnified at the tokenization
21/41

--- Page 22 ---

and subword levels. Tibetan is written with syllable-based segmentation and complex stacked consonants, meaning that naive
whitespace-based tokenizers often fail to identify meaningful boundaries. Subword-based methods such as Byte Pair Encoding
(BPE) or SentencePiece can mitigate out-of-vocabulary issues but risk breaking apart semantically coherent syllables if not
adapted to Tibetan orthography. Encoding inconsistencies, such as mixed use of legacy fonts and Unicode, can also cause
identical syllables to be split into different tokens or merged incorrectly, thereby inflating vocabulary size, lowering model
efficiency, and degrading performance.
→Potential Solution: a unified encoding pipeline that strictly adheres to Unicode normalization should be paired with Tibetan-
specific tokenization and subword segmentation rules. This includes designing tokenizers that respect syllable boundaries while
allowing controlled subword splits for rare terms. Open-source preprocessing tools should integrate automatic detection and
conversion of non-standard encodings, alongside vocabulary optimization to reduce fragmentation. Collaboration between
linguists, software engineers, and standards organizations is essential to maintain accurate, efficient, and interoperable Tibetan
text processing across platforms.
5.5 Ethical & Safety Concern
Development of AI systems for Tibetan raise complex ethical and safety considerations. From an ethical and moral standpoint,
there is a need to ensure fairness, inclusivity, and respect for cultural and linguistic diversity, avoiding bias in datasets and
preventing the marginalization of underrepresented dialects or communities. Politically and socially, language technologies may
intersect with sensitive issues, including information security, censorship, and the potential misuse of AI for misinformation or
surveillance, which can have implications for political stability and community trust. On the technical side, inadequate control
over model outputs can lead to the generation of harmful, biased, or misleading content, while insufficient oversight of data
sourcing can result in privacy violations or breaches of intellectual property.
→Potential Solution: addressing these concerns requires a multi-layered approach. This includes the establishment of
transparent ethical guidelines for dataset creation and model deployment, adherence to privacy protection regulations, and the
integration of bias detection and mitigation mechanisms into model training pipelines. Political and security risks should be
assessed through impact reviews and controlled by access governance frameworks that regulate who can deploy and modify
models. Continuous monitoring of model outputs, combined with culturally informed community oversight, can help maintain
both technical safety and societal trust.
22/41

--- Page 23 ---

Future Direction
Data Construction
AI Development
Dataset
Benchmark
3. Comprehensive & General Corpus
1. Tibetan Word Components
(Standard & Handwriting)
7. Tibetan Phonetics
(Mandarin & Dialects)
4. Ancient Tibetan & 
Traditional Tibetan Culture
2. Ancient Tibetan & 
Traditional Tibetan Culture
1. Comprehensive & General Corpus
6. Specialized Fields (Science and
Engineering, Humanities, etc.)
2. Fundamental Vocabulary Data
(Standard & Handwriting)
8. Image or Video of Tibetan
Language & Culture
10. Multimodal Tibetan Data
3. Emerging Tibetan & Popular Words
4. Specialized Fields (Science and
Engineering, Humanities, etc.)
6. Multimodal Tibetan Data
9.  Ethics & Moral Constraint
5. Tibetan Phonetics
(Mandarin & Dialects)
5. Emerging Tibetan & Popular Words
10.  Safe-benchmark
9. Reasoning & Thinking
8. Reasoning & Thinking
7. Generation (Vision and Language) 
Hardware
Software (AI)
1. Embedded Development
2. GPU Optimization Acceleration
3. Dedicated Tibetan AI chip
4. Efficient Hardware Encoding
5. Innovative Hardware
(Memristor, etc.)
1. Lightweight, Compact &
Efficient Model 
2. Tibetan-specific LLMs
3. Reasoning-Enhanced Multimodal
Tibetan Large Model
4. Agent
5. AIoT for Tibetan Practical Use
Application
Intelligent Customer Service
Intelligent
Multifunctional Assistant
Digital and AI-assisted
Research Tool
Cultural Knowledge Graph and
Semantic Search
Control and Regulation Center
(Human Assistance)
Figure 4. Future Directions of AI in Tibetan in terms of both Data and Models
6 Future Direction
As shown in Figure 4, Tibetan AI is poised to evolve through coordinated progress in resource development, model and
hardware innovation, and domain-specific applications, underpinned by strong ethical and governance frameworks. Building
large-scale, high-quality, and standardized datasets and benchmarks remains the most pressing need, as they form the backbone
for training and evaluating advanced systems. In parallel, innovations in algorithms and computational infrastructure will
enhance efficiency and broaden the range of feasible applications. Finally, translating these technical achievements into socially
beneficial and culturally sensitive solutions will be essential for sustainable impact.
6.1 Data Construction
6.1.1 Dataset
The construction of high-quality, task-specific datasets is the foundation of Tibetan AI development. At the most fundamental
level, resources for basic tasks such as spelling correction, tokenization, and morphological analysis remain scarce, despite their
essential role in enabling reliable downstream processing. Existing datasets are limited in size, often domain-specific, and rarely
cover both standard printed Tibetan and handwritten script, which significantly constrains the robustness of AI models. Beyond
these basic linguistic tasks, there is also a shortage of resources for higher-level natural language generation, including sentence
and paragraph generation, summarization, and machine translation. Such datasets are critical for building general-purpose
Tibetan language models, yet the available corpora are either too small or lack the diversity required to support robust training.
At the highest level of complexity, the field faces a pronounced lack of multimodal datasets that align Tibetan text with speech,
images, and videos capturing cultural, historical, and social contexts. These resources are indispensable for advanced tasks such
as multimodal cultural heritage preservation, cross-modal retrieval, and reasoning-enhanced AI systems capable of integrating
visual and linguistic information.
23/41

--- Page 24 ---

The scarcity of data is a bottleneck for both small-scale and large-scale models. Small models require carefully curated
datasets to achieve acceptable accuracy under limited capacity, while large models rely on massive, diverse corpora to realize
their full potential. Without systematic efforts to expand and standardize Tibetan datasets from basic spelling correction to
complex multimodal cultural applications, the progress of Tibetan AI will remain fundamentally constrained.
6.1.2 Benchmark
Benchmark development provides the standardized foundation for evaluating Tibetan AI systems across linguistic, semantic,
and multimodal tasks. While datasets enable model training, benchmarks ensure comparability, reproducibility, and progress
tracking. In contrast to high-resource languages that benefit from mature suites such as GLUE204, XTREME205, MMLU206 and
CMMLU207, Tibetan AI still lacks unified evaluation protocols and public benchmark sets.
Existing evaluations are fragmented, often limited to small, private test sets focused on specific domains, making it difficult
to assess model generalization or cultural grounding. To address this, Tibetan benchmarks should evolve across multiple tiers:
• Core Linguistic Benchmarks for Segmentation, Tagging, and Morphological Analysis
• General and Domain Benchmarks for Classification, Translation, and Semantic Understanding
• Cultural and Specialized Benchmarks covering Buddhist, Medical, and Legal Texts
• Multimodal Benchmarks for OCR, ASR, and Vision-language Generation
• Advanced Benchmarks for Reasoning, Ethics, and Safety Alignment
Developing such a hierarchical benchmark ecosystem will enable transparent model comparison, promote reproducible
evaluation standards, and guide future progress toward culturally grounded, safe, and interpretable Tibetan AI systems.
6.2 AI Development
6.2.1 Software
The advancement of AI technologies tailored for Tibetan language processing will require innovations across model architectures,
capabilities, and deployment strategies. At the foundational level, lightweight, compact, and efficient models are essential
for ensuring accessibility in low-resource environments and enabling deployment on devices with limited computational
capacity. Such models can facilitate the early adoption of AI in regions with restricted infrastructure while minimizing energy
consumption. Building upon this foundation, the development of Tibetan-specific LLMs will be critical for capturing the unique
linguistic, morphological, and cultural features of Tibetan. These models, trained on large-scale Tibetan corpora, will provide a
robust basis for diverse downstream applications, from text understanding to dialogue systems. A further step will involve
the creation of reasoning-enhanced multimodal Tibetan large models, integrating textual, visual, and auditory modalities with
advanced inference capabilities. Such systems will enable complex cultural heritage preservation, cross-modal retrieval, and
content generation that aligns with both linguistic structure and cultural context. Intelligent agents represent another promising
direction, capable of autonomously performing tasks, interacting with users in Tibetan, and adapting to dynamic contexts.
These agents could serve roles ranging from personalized learning assistants to domain-specific cultural guides.
Finally, AIoT systems designed for Tibetan practical use can connect AI capabilities with physical devices and real-world
applications, supporting domains such as education, agriculture, tourism, and public administration. This integration will bring
Tibetan AI from research laboratories into everyday life, ensuring that technological progress delivers tangible benefits to local
communities.
6.2.2 Hardware
Advances in dedicated hardware will play a pivotal role in enabling efficient and scalable Tibetan AI systems. At the entry
level, embedded development offers the possibility of deploying lightweight models on resource-constrained devices, making
Tibetan language technologies accessible in low-connectivity or rural environments. Optimizing existing GPU architectures
for Tibetan-specific workloads can significantly reduce training and inference latency, enabling faster experimentation and
deployment without the need for extensive hardware investment. Beyond optimizing general-purpose hardware, future work
may focus on the design of specialized Tibetan AI chips using electronic design automation tools. Such chips could incorporate
dedicated instruction sets and processing units tailored for Tibetan script handling, including efficient support for complex
character rendering and morphological processing. At the encoding level, hardware-oriented modifications, such as custom
mappings that extend or adapt ASCII or Unicode representations for Tibetan, could further streamline data processing pipelines
and reduce computational overhead.
At the frontier of hardware innovation, emerging devices such as memristors present new opportunities for high-density,
low-power, and neuromorphic computing. Their ability to combine storage and computation within the same physical unit
24/41

--- Page 25 ---

could be particularly advantageous for large-scale Tibetan AI applications that require both high-speed processing and energy
efficiency. Progress along this trajectory from embedded systems and GPU optimization to custom AI chips, encoding-level
innovation, and next-generation devices will define the hardware backbone of future Tibetan language processing technologies.
6.3 Application
The ultimate objective of Tibetan AI development lies in its translation into practical applications that deliver tangible benefits
to society, culture, and research. Technological advances in data resources, AI models, and dedicated hardware will only
reach their full potential when integrated into solutions that address real-world needs and contexts. Promising application
areas include intelligent customer service systems capable of understanding and responding in Tibetan, thereby improving
accessibility to information and services for Tibetan-speaking communities. Intelligent multifunctional assistants can serve as
personalized guides, capable of performing a wide range of tasks such as language learning support, document translation,
and daily information retrieval. Cultural knowledge graphs combined with semantic search technologies hold significant
potential for preserving and promoting Tibetan heritage. These tools can enable scholars, educators, and the public to explore
interconnected cultural, linguistic, and historical data through intuitive and intelligent interfaces. Digital and AI-assisted
research tools can further enhance academic productivity by facilitating the analysis, annotation, and organization of Tibetan
language and cultural materials.
In addition, control and regulation centers with human assistance can provide oversight for AI systems, ensuring safety,
reliability, and ethical compliance in deployment. These applications represent concrete pathways for Tibetan AI to make a
meaningful societal impact, highlighting that technological progress is ultimately measured by its ability to serve the needs of
people, preserve cultural identity, and foster sustainable development.
Interdisciplinary Collaboration
The advancement of Tibetan AI will increasingly depend on sustained interdisciplinary collaboration, integrating expertise
from linguistics, computer science, cultural studies, education, and policy-making. Linguists provide critical insights into the
structural and functional properties of Tibetan, including orthography, phonetics, and morphological variation across dialects,
ensuring that AI systems are linguistically sound. Computer scientists contribute advanced algorithms, model architectures, and
data processing pipelines that can address the technical challenges of low-resource language processing. Scholars in cultural
and historical studies offer contextual knowledge that grounds AI applications in the lived realities, traditions, and heritage of
Tibetan-speaking communities. Collaboration with the education sector is essential for developing AI-driven tools that support
Tibetan language teaching, literacy programs, and curriculum design. Partnerships with policy-makers and legal experts can
help establish regulatory and ethical frameworks that govern data collection, privacy protection, and cross-border data flows,
ensuring compliance with both national and international standards. Engagement with local communities plays a central role,
both in contributing authentic data and in shaping the priorities of AI projects to reflect real needs and values.
Interdisciplinary collaborations can be operationalized through joint research initiatives, shared resource platforms, and
co-creation workshops that bring together diverse stakeholders. Such collaborations will not only accelerate technological
innovation but also ensure that Tibetan AI solutions are culturally respectful, ethically grounded, and socially impactful.
25/41

--- Page 26 ---

Conclusion
This survey provides the first systematic and large-scale review of Tibetan AI across linguistic resources, discriminative
modeling, generative architectures, LLM adaptation, and emerging neuromorphic computation paradigms. Unlike high-resource
languages with well-established benchmarks and data ecosystems, Tibetan AI remains fragmented, with isolated datasets,
inconsistent annotation standards, limited cross-domain generalization, and a near-complete absence of hardware-efficient
deployment strategies. Through structured categorization and comparative analysis, we identify the transition of Tibetan AI from
rule-based and classical machine learning models to Transformer-based architectures and LLM-centric instruction-following
systems, highlighting a paradigm shift toward unified generative modeling.
Despite this progress, key gaps remain: large-scale domain-diverse corpora are still scarce, reasoning and safety-aligned
supervision for Tibetan is underdeveloped, and evaluation is constrained by the lack of standardized benchmarks beyond
TLUE. Furthermore, current Tibetan LLMs are purely digital and GPU-dependent, overlooking the potential of neuromorphic
accelerators such as memristor crossbar arrays, which are particularly suitable for low-resource settings and script-specific
symbolic computation.
Looking forward, we argue that the development of Tibetan AI should evolve along three complementary axes: (1)
data-centric scaling through culturally grounded corpus expansion and annotation standardization, (2) alignment-centric
modeling through Tibetan-specific instruction tuning, safety filtering, and reasoning supervision, and (3) hardware-centric
deployment via analog–digital co-designed architectures that leverage the discrete structure of Tibetan script for efficient token
matching and inference. Advancing along these axes will not only improve the accessibility and inclusivity of Tibetan AI but
also provide a transferable blueprint for other low-resource languages facing similar structural and computational constraints.
We hope this survey serves as a foundation for building a sustainable and culturally aligned Tibetan AI ecosystem.
Acknowledgment
This work was supported in part by the National Science and Technology Major Project under Grant 2022ZD0116100, in part
by the Sichuan Provincial Major Science and Technology Project under Grant 2024ZDZX0012, in part by the National Natural
Science Foundation of China under Grants 62276055, 62406062, 62436006 and 62406257,in part by the Sichuan Science and
Technology Program under Grant 2023YFG0288, in part by the Natural Science Foundation of Sichuan Province under Grant
2024NSFSC1476, in part by the Tibetan Natural Science Foundation under GrantXZ202201ZR0054G.
26/41

--- Page 27 ---

References
1. Devlin, J., Chang, M.-W., Lee, K. & Toutanova, K. Bert: Pre-training of deep bidirectional transformers for language
understanding. In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational
Linguistics (NAACL), 4171–4186 (2019).
2. Vaswani, A. et al. Attention is all you need. In Advances in Neural Information Processing Systems (NeurIPS), 5998–6008
(2017).
3. Liu, Y. et al. Roberta: A robustly optimized bert pretraining approach. In arXiv preprint arXiv:1907.11692 (2019).
4. Lan, Z. et al. Albert: A lite bert for self-supervised learning of language representations. In International Conference on
Learning Representations (ICLR) (2020).
5. Yang, Z. et al. Xlnet: Generalized autoregressive pretraining for language understanding. In Advances in Neural
Information Processing Systems (NeurIPS), 5754–5764 (2019).
6. Lewis, M. et al. Bart: Denoising sequence-to-sequence pre-training for natural language generation, translation, and
comprehension. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL),
7871–7880 (2020).
7. Zhang, J., Zhao, Y., Saleh, M. & Liu, P. J. Pegasus: Pre-training with extracted gap-sentences for abstractive summarization.
In Proceedings of the 37th International Conference on Machine Learning (ICML), 11328–11339 (2020).
8. Sutskever, I., Vinyals, O. & Le, Q. V. Sequence to sequence learning with neural networks. Adv. Neural Inf. Process. Syst.
(NeurIPS) 27 (2014).
9. Bahdanau, D., Cho, K. & Bengio, Y. Neural machine translation by jointly learning to align and translate. In International
Conference on Learning Representations (ICLR) (2015).
10. Radford, A. et al. Language models are unsupervised multitask learners. OpenAI Tech. Rep. (2019).
11. Lu, J., Batra, D., Parikh, D. & Lee, S. Vilbert: Pretraining task-agnostic visiolinguistic representations for vision-and-
language tasks. In Advances in Neural Information Processing Systems (NeurIPS), 13–23 (2019).
12. Li, L. H., Yatskar, M., Yin, D., Hsieh, C.-Y. & Chang, K.-W. Visualbert: A simple and performant baseline for vision and
language. In arXiv preprint arXiv:1908.03557 (2019).
13. Radford, A. et al. Learning transferable visual models from natural language supervision. In Proceedings of the 38th
International Conference on Machine Learning (ICML), 8748–8763 (2021).
14. Li, J., Li, D., Savarese, S. & Hoi, S. C. H. Blip-2: Bootstrapping language-image pre-training with frozen image encoders
and large language models. arXiv preprint arXiv:2301.12597 (2023).
15. Alayrac, J.-B. et al. Flamingo: a visual language model for few-shot learning. Adv. Neural Inf. Process. Syst. (NeurIPS)
(2022).
16. Sun, Y., Liu, S., Deng, J. & Zhao, X. Tibert: Tibetan pre-trained language model. arXiv preprint arXiv:2205.07303
(2022).
17. Gao, F. et al. Tibstc-cot: A multi-domain instruction dataset for chain-of-thought reasoning in language models. arXiv
preprint arXiv:2508.01977 (2025).
18. Huang, C. et al. Tib-stc: A large-scale structured tibetan benchmark for low-resource language modeling. arXiv preprint
arXiv:2503.18288 (2025).
19. Pan, L. et al. Advancing large language models for tibetan with curated data and continual pre-training. arXiv preprint
arXiv:2507.09205 (2025).
20. OpenAI. Gpt-4 technical report. arXiv preprint arXiv:2303.08774 (2023).
21. OpenAI. Gpt-4o system card. arXiv preprint arXiv:2410.21276 (2024).
22. OpenAI. Gpt-5 system card. https://cdn.openai.com/gpt-5-system-card.pdf (2025).
23. Touvron, H. et al. Llama: Open and efficient foundation language models. arXiv preprint arXiv:2302.13971 (2023).
24. Touvron, H. et al. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288 (2023).
25. AI, M. The llama 3 herd of models. arXiv preprint arXiv:2407.21783 (2024).
26. Guo, D. et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. arXiv preprint
arXiv:2501.12948 (2025).
27/41

--- Page 28 ---

27. Liu, A. et al. Deepseek-v3 technical report. arXiv preprint arXiv:2412.19437 (2024).
28. Bai, J. et al. Qwen technical report. arXiv preprint arXiv:2309.16609 (2023).
29. Team, Q. & Cloud, A. Qwen2 technical report. arXiv preprint arXiv:2407.10671 (2024).
30. Team, Q. & Cloud, A. Qwen2.5: Open models with 1-million token context window. arXiv preprint arXiv:2412.15115
(2024).
31. Team, Q. & Cloud, A. Qwen3 technical report. arXiv preprint arXiv:2505.09388 (2025).
32. Anil, R. et al.
Gemini 1: 2 trillion token multimodal models with fast training and inference.
arXiv preprint
arXiv:2312.11805 (2023).
33. Anil, R. et al. Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context. arXiv preprint
arXiv:2403.05530 (2024).
34. Anil, R. et al. Gemini 2 technical report. arXiv preprint arXiv:2501.12345 (2025).
35. Anthropic. Claude 1 and 2 technical overview. https://www.anthropic.com/news/claude-2 (2023).
36. Anthropic. Claude 3 family of language models. https://www.anthropic.com/news/claude-3-family (2024).
37. Anthropic. Claude 3.5 sonnet and claude 3.5 haiku. https://www.anthropic.com/news/claude-3-5 (2025).
38. Anthropic. Claude 4 technical overview. https://www.anthropic.com/news/claude-4 (2025).
39. Tournadre, N. Tibetan, vol. 399 of Languages of the World/Materials (LINCOM Europa, Munich, 2003).
40. Tournadre, N. & Dorje, S. Manual of Standard Tibetan: Language and Civilization (Snow Lion, Ithaca, NY, 2014).
41. Zeisler, B. Relative tense and aspectual values in tibetan languages: A comparative study. Mouton de Gruyter (2004).
42. Sun, J. T.-S. Sino-tibetan languages. In Thurgood, G. & LaPolla, R. (eds.) The Sino-Tibetan Languages, 490–502
(Routledge, 2003).
43. van Driem, G. Tibetan language: Linguistic features and sociolinguistic issues. Himal. Linguist. 18, 1–25 (2019).
44. Gao, F. et al. Tlue: A tibetan language understanding evaluation benchmark. arXiv preprint arXiv:2503.12051 (2025).
45. Drup, N. et al. Study on printed tibetan character recognition. In 2010 International Conference on Artificial Intelligence
and Computational Intelligence, vol. 1, 280–285 (2010).
46. DeLancey, S. Ergativity and the syntax of tibetan. Stud. Lang. 8, 1–37 (1984).
47. Tournadre, N. & Suzuki, H. The Tibetic Languages (Routledge, London, 2023).
48. Tournadre, N. Dialect classification in the tibetan linguistic area. Linguist. Tibet. Area 30, 1–50 (2007).
49. Hill, N. W. Classical Tibetan: A Grammar (Oxford University Press, Oxford, 2019).
50. Consortium, U. The unicode standard, version 16.0: Tibetan script specification (2024). Technical Report on Tibetan
Script Encoding Standards.
51. Buddhist digital resource center (bdrc). https://www.bdrc.io/. Accessed: 2025-02.
52. Tibetan and himalayan library (thl). https://thlib.org/. Accessed: 2025-02.
53. Rangjung yeshe tibetan corpus. https://www.rangjung.com/. Accessed: 2025-02.
54. Thl tibetan dictionary api. https://dictionary.thlib.org/. Accessed: 2025-02.
55. Tibetan wikipedia dump. https://bo.wikipedia.org/. Accessed: 2025-02.
56. Asian classics input project (acip). https://asianclassics.org/. Accessed: 2025-02.
57. Opensubtitles tibetan fragment collection. https://www.opensubtitles.org/. Accessed: 2025-02.
58. Shimizu, T. & Yamamoto, K. Nict-tib1: A tibetan speech corpus for low-resource asr. In Proceedings of the Oriental
COCOSDA Conference, 1–6 (IEEE, 2021).
59. Wang, L., Zhou, M. & Tsering, N. Tibmd@muc: A multi-dialect tibetan speech corpus for robust speech recognition. In
Proceedings of the Multilingual Understanding Conference (MUC), 45–52 (ACL, 2023).
60. Tsering, D., Li, H. & Dorje, S. Tibner: A tibetan named entity recognition dataset for low-resource entity extraction. J.
Chin. Inf. Process. 38, 112–123 (2024).
61. Li, J., Zhang, M. & Tsering, D. Cute: A multilingual chinese–uyghur–tibetan–english parallel corpus for low-resource mt.
In Proceedings of COLING 2025 (ACL, 2025).
28/41

--- Page 29 ---

62. Zhang, W., Dorje, T. & Liu, F. Constructing a tibetan machine reading comprehension dataset for low-resource qa. In
Proceedings of the China National Conference on Computational Linguistics (CCL), 210–222 (ACL Anthology, 2021).
63. Du, L., Tsering, N. & Huang, K. Ticonvqa: A conversational tibetan question answering dataset with multi-turn reasoning.
In Proceedings of the China National Conference on Computational Linguistics (CCL) (ACL Anthology, 2024).
64. Dorje, S., Li, Q. & Tenzin, N. Tilts: A long-text tibetan summarization dataset for abstractive generation. In Lecture
Notes in Computer Science, 310–322 (Springer, 2024).
65. Li, H., Zhang, T. & Nyima, P. A tibetan–chinese cross-lingual summarization dataset for bidirectional news understanding.
J. Chin. Inf. Process. 38, 89–101 (2024).
66. Nyima, P., Dorje, S. & Li, H. Tikg-30k: A tibetan knowledge graph dataset for low-resource entity-relation modeling. J.
Chin. Inf. Process. 39, 31–42 (2025).
67. Gales, M., Knill, K., Ragni, A. & Rath, S. Speech recognition for low-resource languages: The babel program. In 2014
IEEE Spoken Language Technology Workshop (SLT), 16–23 (IEEE, 2014).
68. Goyal, N. et al. FLORES-200: Evaluating machine translation for low-resource languages. In Proceedings of the 2022
Conference on Empirical Methods in Natural Language Processing (EMNLP) (2022).
69. Papineni, K., Roukos, S., Ward, T. & Zhu, W.-J. Bleu: a method for automatic evaluation of machine translation. In
Proceedings of the 40th Annual Meeting of the Association for Computational Linguistics, 311–318 (2002).
70. Popovi´c, M. chrf: character n-gram f-score for automatic mt evaluation. In Proceedings of the Tenth Workshop on
Statistical Machine Translation, 392–395 (2015).
71. Xue, L. et al. mt5: A massively multilingual pre-trained text-to-text transformer. In Proceedings of the 2021 Conference of
the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, 483–498
(2021).
72. Workshop, B. et al. Bloom: A 176b-parameter open-access multilingual language model. arXiv preprint arXiv:2211.05100
(2022).
73. Lin, X. et al. Xglm: An extremely large multilingual language model. In Proceedings of the 60th Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers), 473–487 (2022).
74. Liu, Y. et al. Listening, imagining\& refining: A heuristic optimized asr correction framework with llms. arXiv preprint
arXiv:2509.15095 (2025).
75. Liu, Y. et al. Tispell: A semi-masked methodology for tibetan spelling correction covering multi-level error with data
augmentation. arXiv preprint arXiv:2505.08037 (2025).
76. Liu, Y. et al. Fmsd-tts: Few-shot multi-speaker multi-dialect text-to-speech synthesis for\" u-tsang, amdo and kham
speech dataset generation. arXiv preprint arXiv:2505.14351 (2025).
77. Wang, L. & Yang, H. Tibetan word segmentation method based on bilstm_crf model. In 2018 International Conference
on Asian Language Processing (IALP), 297–302 (2018).
78. Chen, M., Zhao, S. & Yang, K. Neural architecture for tibetan word segmentation. In 2017 International Conference on
Asian Language Processing (IALP), 367–370 (2017).
79. Xu, Z. et al. Research on arbitrary shape tibetan text detection with graph network. In 2022 International Conference on
Image Processing, Computer Vision and Machine Learning (ICICML), 452–456 (2022).
80. Zhou, M., Daiqing, Z., Qun, N., Nima, Z. & Nyima, T. Tibetan punctuation is all you need in pretrained language model.
In 2023 International Conference on Intelligent Management and Software Engineering (IMSE), 161–168 (2023).
81. Tibetan & (THL), H. L. Thl pos tagger: Rule-based tibetan part-of-speech annotation toolkit. Tech. Rep., University
of Virginia Digital Humanities Initiative (2017). Accessed: 2025-10-11, available at https://www.thlib.org/toolbox/
pos-tagger/.
82. Gyaltsen, T. & Dorjee, P. Tibetan ocr post-correction via grapheme normalization and lexical filtering. In Proceedings of
the Tibetan Language Technology Workshop, 45–52 (2019).
83. Liang, Y. et al. Tibetan-bert-wwm: A tibetan pretrained model with whole word masking for text classification. IEEE
Transactions on Comput. Soc. Syst. 11, 6268–6277 (2024).
84. Dawa, P. & Wang, Z. Fine-tuning multilingual bert for tibetan named entity recognition. In Workshop on Multilingual
Representation Learning, 91–98 (2021).
29/41

--- Page 30 ---

85. Jia, L., Jiang, T., Meng, J. H. & Zhang, T. Tibetan text classification method based on bilstm model. In 2020 International
Conference on Artificial Intelligence and Electromechanical Automation (AIEA), 27–31 (2020).
86. Developers, C. T. N.
Tibetanruleseg: A regex-based tibetan segmentation script.
https://github.com/tibetan-nlp/
tibetanruleseg (2022). Accessed: 2025-10-11.
87. Sanzhi, C., Danzen, P., Duola & Jiancuo, S. Research on chinese-tibetan sentence alignment based on cino. In 2025 IEEE
6th International Conference on Pattern Recognition and Machine Learning (PRML), 392–396 (2025).
88. Sun, X. et al. Cino: A chinese–tibetan pretrained language model for low-resource multilingual processing. In Findings
of ACL (2021).
89. Liu, Y. et al. Tmd-tts: A unified tibetan multi-dialect text-to-speech synthesis for\" u-tsang, amdo and kham speech
dataset generation. arXiv preprint arXiv:2509.18060 (2025).
90. LeCun, Y., Bottou, L., Bengio, Y. & Haffner, P. Gradient-based learning applied to document recognition. Proc. IEEE
(1998).
91. Shi, B., Bai, X. & Yao, C. An end-to-end trainable neural network for image-based sequence recognition and its
application to scene text recognition. In ICCV (2016).
92. He, C., Gesang, Q., Qun, N., Luosang, G. & Nyima, T. Research on tibetan-chinese machine translation method based
on graphic multimodal fusion alignment. In 2024 6th International Conference on Internet of Things, Automation and
Artificial Intelligence (IoTAAI), 714–717 (2024).
93. Wang, C. et al. A study of tibetan-chinese machine translation based on bidirectional training strategy. In 2022 3rd
International Conference on Pattern Recognition and Machine Learning (PRML), 352–356 (2022).
94. Costa-jussà, M. R. et al. No language left behind: Scaling human-centered machine translation. arXiv preprint
arXiv:2207.04672 (2022).
95. van den Oord, A. et al. Wavenet: A generative model for raw audio. In Proceedings of the 9th ISCA Speech Synthesis
Workshop, 125–125 (2016).
96. Kong, J., Kim, J. & Bae, J. Hifi-gan: Generative adversarial networks for efficient and high fidelity speech synthesis. In
Proceedings of the 34th Conference on Neural Information Processing Systems, 17022–17033 (2020).
97. Huang, C. et al. Semantic and visual attention-driven multi-lstm network for automated clinical report generation. In AI
for Health Equity and Fairness: Leveraging AI to Address Social Determinants of Health, 233–248 (Springer, 2024).
98. Lin, Y. et al. Attention enhanced network with semantic inspector for medical image report generation. In 2023 IEEE
35th International Conference on Tools with Artificial Intelligence (ICTAI), 242–249 (IEEE, 2023).
99. Deng, J. et al. Milmo: minority multilingual pre-trained language model. In 2023 IEEE International Conference on
Systems, Man, and Cybernetics (SMC), 329–334 (IEEE, 2023).
100. Li, J., Li, D., Xie, C. & Hoi, S. C. H. Blip: Bootstrapping language-image pre-training for unified vision-language
understanding and generation. In Proceedings of the 39th International Conference on Machine Learning (ICML),
12888–12900 (2022).
101. Liu, H., Li, C., Wu, Q. & Lee, Y. J. Visual instruction tuning. In Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition (CVPR), 13412–13423 (2024).
102. Esukhia. Pybo: A python toolkit for tibetan tokenization and text processing. https://github.com/Esukhia/pybo (2019).
Version 0.7.7.
103. Esukhia & contributors, O. Botok: Tibetan tokenizer. https://github.com/OpenPecha/Botok (2018). Version 0.9+.
104. Group, T. N. R. Tibetanmorph: A rule-based morphological analyzer for tibetan. Tech. Rep., Tibetan NLP Open Research
Initiative (2019). Technical report, available at https://github.com/tibetan-nlp/.
105. Tibetan & (THL), H. L. Thl lextools: Rule-based lexicon and segmentation toolkit for tibetan. Tech. Rep., University of
Virginia Library Digital Humanities Initiative (2018). Accessed: 2025-10-11, available at https://library.virginia.edu/thl.
106. Contributors, O. T. N. Tibwordsplitter: Heuristic rule-based tibetan word splitter. https://github.com/tibetan-nlp/
tibwordsplitter (2023). Accessed: 2025-10-11.
107. THDL. Thdl standard tibetan phonetic transcription system. Tech. Rep., Tibetan and Himalayan Library (THL) (2016).
Official rule-set, available at https://www.thlib.org/reference/transliteration/.
30/41

--- Page 31 ---

108. Consortium, U. Unicode standard annex: Tibetan script normalization guidelines. Tech. Rep., Unicode Technical
Committee (2020). Technical specification, available at https://unicode.org/reports/.
109. Fan, R.-E., Chang, K.-W., Hsieh, C.-J., Wang, X.-R. & Lin, C.-J. LIBLINEAR: A library for large linear classification. J.
Mach. Learn. Res. 9, 1871–1874 (2008).
110. Chang, C.-C. & Lin, C.-J. LIBSVM: A library for support vector machines. ACM Transactions on Intell. Syst. Technol. 2,
27:1–27:27 (2011).
111. Breiman, L. Random forests. Mach. Learn. 45, 5–32 (2001).
112. Chen, T. & Guestrin, C. XGBoost: A scalable tree boosting system. In Proceedings of the 22nd ACM SIGKDD
International Conference on Knowledge Discovery and Data Mining, 785–794 (2016).
113. Salton, G. & Buckley, C. Term-weighting approaches in automatic text retrieval. Inf. Process. & Manag. 24, 513–523
(1988).
114. Bojanowski, P., Grave, E., Joulin, A. & Mikolov, T. Enriching word vectors with subword information. In Transactions of
the Association for Computational Linguistics, vol. 5, 135–146 (2017).
115. Sun, P. et al. Yi characters recognition based on tesseract-ocr. In 2019 IEEE 3rd Advanced Information Management,
Communicates, Electronic and Automation Control Conference (IMCEC), 102–106 (2019).
116. Ke, G. et al. Lightgbm: A highly efficient gradient boosting decision tree. In Advances in Neural Information Processing
Systems (NeurIPS), 3149–3157 (2017).
117. Rabiner, L. R. A tutorial on hidden markov models and selected applications in speech recognition. Proc. IEEE 77,
257–286 (1989).
118. Lafferty, J., McCallum, A. & Pereira, F. Conditional random fields: Probabilistic models for segmenting and labeling
sequence data. In Proceedings of the 18th International Conference on Machine Learning, 282–289 (2001).
119. Berger, A. L., Pietra, S. A. D. & Pietra, V. J. D. A maximum entropy approach to natural language processing. Comput.
Linguist. 22, 39–71 (1996).
120. Elman, J. L. Finding structure in time. Cogn. Sci. (1990).
121. Hochreiter, S. & Schmidhuber, J. Long short-term memory. Neural Comput. (1997).
122. Cho, K. et al. Learning phrase representations using rnn encoder-decoder for statistical machine translation. In EMNLP
(2014).
123. Schuster, M. & Paliwal, K. K. Bidirectional recurrent neural networks. IEEE Transactions on Signal Process. (1997).
124. Graves, A. & Schmidhuber, J. Framewise phoneme classification with bidirectional lstm and other neural network
architectures. In IEEE International Joint Conference on Neural Networks (IJCNN) (2005).
125. Puigcerver, J. Convolutional recurrent neural networks: Learning spatial dependencies for image-based sequence
modeling. In ICDAR (2017).
126. Shi, B., Bai, X. & Yao, C. An end-to-end trainable neural network for image-based sequence recognition and its
application to scene text recognition. In ICCV (2016).
127. Lample, G., Ballesteros, M., Subramanian, S., Kawakami, K. & Dyer, C. Neural architectures for named entity recognition.
In NAACL (2016).
128. Bordes, A., Usunier, N., García-Durán, A., Weston, J. & Yakhnenko, O. Translating embeddings for modeling multi-
relational data. In NeurIPS (2013).
129. Kipf, T. N. & Welling, M. Semi-supervised classification with graph convolutional networks. In ICLR (2017).
130. He, K., Zhang, X., Ren, S. & Sun, J. Deep residual learning for image recognition. In CVPR (2016).
131. Kim, Y. Convolutional neural networks for sentence classification. In EMNLP (2014).
132. Zhang, X., Zhao, J. & LeCun, Y. Character-level convolutional networks for text classification. In NeurIPS (2015).
133. Yu, F. & Koltun, V. Multi-scale context aggregation by dilated convolutions. In ICLR (2016).
134. Huang, Z., Xu, W. & Yu, K. Bidirectional lstm-crf models for sequence tagging. In EMNLP (2015).
135. Kudo, T. & Richardson, J. Sentencepiece: A simple and language independent subword tokenizer and detokenizer for
neural text processing. In EMNLP (2018).
31/41

--- Page 32 ---

136. Sennrich, R., Haddow, B. & Birch, A. Neural machine translation of rare words with subword units. In ACL (2016).
137. Gu, A. & Dao, T. Mamba: Linear-time sequence modeling with selective state spaces. In ICLR (2024).
138. Dao, T. & Gu, A. Mamba-2: Scaling selective state space models with distributed inference and training. arXiv preprint
arXiv:2405.21060 (2024).
139. OpenAI. Openai o1 system card, DOI: 10.48550/arXiv.2412.16720 (2024). 2412.16720.
140. Hu, E. J. et al. Lora: Low-rank adaptation of large language models. ICLR 1, 3 (2022).
141. Mangrulkar, P. et al. Peft: State-of-the-art parameter-efficient fine-tuning methods. arXiv preprint arXiv:2309.05484
(2023).
142. Dettmers, T., Pagnoni, A., Holtzman, A. & Zettlemoyer, L. Qlora: Efficient finetuning of quantized llms. Adv. neural
information processing systems 36, 10088–10115 (2023).
143. Liu, Y. et al. Tibetan syllable component recognization with memristor. In 2024 International Conference on Neuromor-
phic Computing (ICNC), 1–6 (IEEE, 2024).
144. O, C. L. Memristor-the missing circuit element. IEEE Transactions on Circuit Theory 18, 507–519 (1971).
145. O, C. L. How we predicted the memristor. Nat Electron 1, 322 (2018).
146. Hieber, D. & Garrett, J. The extended wylie transliteration scheme (ewts) for tibetan digital processing. In Proceedings of
the Tibetan and Himalayan Digital Libraries Workshop (2016).
147. Wang, W. & Duola, D. Formation of standard tibetan syllables and comparison as well as analysis of the statistical results.
In Proceedings of the IEEE Conference on Cybernetics and Intelligent Systems, 379–384 (2008).
148. Huang, H. & Da, F. Discussion on collation of tibetan syllable. In Proceedings of the International Conference on Asian
Language Processing, 35–38 (2010).
149. Zhu, J., Li, T., Ge, S., Ren, Q. & Qiao, S. Tibetan syllable rule model and applications. J. Chin. Inf. Process. 49, 68–74
(2013).
150. Wangdui, B., Zhuoga, Z., Chen, Y. & Wu, Q. Study on recognition algorithms for tibetan construction elements. J. Chin.
Inf. Process. 49, 104–111 (2014).
151. Brown, C. J. Improved neural word segmentation for standard tibetan. In Proceedings of the Workshop on Resources and
Technologies for Indigenous, Endangered and Lesser-resourced Languages in Eurasia (EURALI) @ LREC-COLING,
12–17 (Torino, Italy, 2024).
152. San, M., Cai, Z., Cai, R. & Dao, J. Analysis on types of spelling errors in true tibetan characters. MATEC Web Conf. 336,
06019 (2021).
153. Zhu, J., Li, T. & Liu, S. The algorithm of spelling check based on tsrm. J. Chin. Inf. Process. 28, 92–98 (2014).
154. Zhu, J., Li, T. & Liu, S. An approach for tibetan text automatic proofreading and its system design. J. Chin. Inf. Process.
50, 142–148 (2014).
155. Liu, H., Hong, J., Nuo, M. & Wu, J. Statistics and analysis on spell errors of tibetan syllables based on a large-scale web
corpus. J. Chin. Inf. Process. 31, 61–70 (2017).
156. Hua, D., Cai, Z. & Ban, M. A tc_lstm based method for tibetan spelling check. J. Chin. Inf. Process. 34, 50–55 (2020).
157. Hua, G., Jia, S., Ban, M. & Cai, R. Error correction of tibetan verbs based on deep learning. In Proceedings of the
International Conference on Artificial Intelligence and Computer Engineering (ICAICE), 221–226 (2021).
158. Tsering, L. & Li, W. Crf-based tibetan word segmentation with lexicon and character features. In Proceedings of the
International Conference on Asian Language Processing (2014).
159. Dorji, T. & Zhang, M. Neural sequence tagging for tibetan tokenization with bilstm-crf. In Proceedings of the Workshop
on Low-Resource Languages for NLP (2018).
160. Ngodrup & Zhao, D. Research on wooden blocked tibetan character segmentation based on drop penetration algorithm.
In 2010 Chinese Conference on Pattern Recognition (CCPR), 1–5 (2010).
161. Jian, Y., Peng, S. & Zhenpeng, L. An automatic blind syllable segmentation model based on bi-directional lstm. In 2019
IEEE 2nd International Conference on Computer and Communication Engineering Technology (CCET), 109–113 (2019).
162. Hou, Z., Gao, Y. & Fan, M. Research on named entity recognition in tibetan medicine based on bert-bigru-crf model. In
2024 9th International Conference on Intelligent Computing and Signal Processing (ICSP), 899–903 (2024).
32/41

--- Page 33 ---

163. Wang, L., Wang, H. & Yang, H. Classification method for tibetan texts based on in-depth learning. In 2019 IEEE 8th
Joint International Information Technology and Artificial Intelligence Conference (ITAIC), 1231–1235 (2019).
164. An, B. & Long, C. Ancient tibetan word segmentation based on deep learning. In 2021 International Conference on
Asian Language Processing (IALP), 292–297 (2021).
165. Wang, L., Yang, H., Xing, X. & Yan, Y. Tibetan word segmentation method based on cnn-bilstm-crf model. In 2019
International Conference on Asian Language Processing (IALP), 319–324 (2019).
166. Hao, M., Yan, X. & Ouyang, X. A tibetan text classification method based on hybrid model and channel attention
mechanism. In 2024 27th International Conference on Computer Supported Cooperative Work in Design (CSCWD),
1522–1527 (2024).
167. Gongqu, Z. et al. A tibetan ancient uchen text line dataset for ocr. In 2024 International Conference on Image Processing,
Computer Vision and Machine Learning (ICICML), 796–799 (2024).
168. Lobsang, T. & Zhang, W. Handwritten tibetan character recognition using cnn-ctc architectures. In ICDAR Workshop on
Asian Script Analysis, 33–40 (2019).
169. Tashi, N. & Dorjee, T. A dataset and baseline models for handwritten tibetan ocr. In International Conference on
Document Analysis for Oriental Languages, 57–65 (2020).
170. Sonam, D. & Li, J. Lexicon-driven post-processing for tibetan handwriting recognition systems. J. Tibet. Inf. Process. 17,
89–97 (2021).
171. Meelen, M. & van Kooij, T. Orthographic normalization strategies for improving tibetan ocr robustness. In International
Conference on Asian Language Processing, 112–119 (2020).
172. Wang, J., Norbu, S. & Zhang, M. Lexicon-constrained post-ocr correction for tibetan script recognition systems. J. Tibet.
Inf. Process. 18, 73–82 (2022).
173. Cuo, Y., SHI, X., Tashi, N. & CHEN, Y. Phrase-based tibetan-chinese statistical machine translation. In 2019 International
Conference on Asian Language Processing (IALP), 424–427 (2019).
174. He, C., Gesang, Q., Qun, N. & Nyima, T. Research on tibetan-chinese neural machine translation based on gru. In 2023
3rd International Conference on Digital Society and Intelligent Systems (DSInS), 213–216 (2023).
175. Yao, Y. & Zhao, X. A design on tibetan-chinese online translation system. In 2018 International Conference on Intelligent
Transportation, Big Data & Smart City (ICITBS), 448–450 (2018).
176. Zhou, M., Gesang, Q., Qun, N., Nyima, T. & Rinchen, D. Tibetan-chinese machine translation enhanced on cross-lingual
pre-trained model. In 2024 IEEE International Conference on Systems, Man, and Cybernetics (SMC), 1618–1623 (2024).
177. Xu, X., Tan, J. & Zhao, Y. End-to-end tibetan-chinese speech translation based on multi-task and multi-level pre-training.
In 2023 IEEE 6th International Conference on Pattern Recognition and Artificial Intelligence (PRAI), 852–857 (2023).
178. Liu, R., Zhao, Y. & Xu, X. Multi-task self-supervised learning based tibetan-chinese speech-to-speech translation. In
2023 International Conference on Asian Language Processing (IALP), 45–49 (2023).
179. Pema, T. & Luo, M. Language model rescoring for tibetan asr with subword units. In Workshop on Speech and Language
Technologies for Minority Languages, 102–109 (2021).
180. Lhamo, Y. & Zhao, L. Dialect-aware acoustic modeling for tibetan asr across amdo and kham variants. J. Asian Lang.
Speech Technol. 14, 23–31 (2022).
181. Drolkar, K. & Hu, Z. Prosody-aware tibetan tts with phoneme-level pitch conditioning. In Conference on Speech Prosody
for Low-Resource Languages, 71–78 (2023).
182. Jampa, L. & Mei, C. Multi-speaker tibetan tts using speaker embeddings and hifi-gan fine-tuning. In Low-Resource
Speech Synthesis Workshop, 56–63 (2023).
183. Povey, D. et al. The kaldi speech recognition toolkit. In IEEE Workshop on Automatic Speech Recognition and
Understanding (ASRU), 1–4 (2011).
184. Hannun, A. et al. Deep speech: Scaling up end-to-end speech recognition. arXiv preprint arXiv:1412.5567 (2014).
185. Gulati, A. et al. Conformer: Convolution-augmented transformer for speech recognition. In Interspeech, 5036–5040
(2020).
186. Wang, Y. et al. Tacotron: Towards end-to-end speech synthesis. In Interspeech, 4006–4010 (2017).
33/41

--- Page 34 ---

187. Lobsang, T. & Zhao, J. Support vector machine for tibetan text classification with morphological features. J. Tibet. Inf.
Process. 15, 33–41 (2019).
188. Conneau, A. et al. Unsupervised cross-lingual representation learning at scale. In ACL, 8440–8451 (2020).
189. Tsering, N. & Drolkar, L. Rule-based tibetan information extraction using lexical templates and gazetteers. In Workshop
on Asian Language Resources, 58–65 (2017).
190. Jigme, P. & Chen, W. Crf-based tibetan named entity recognition with syllable-level features. In International Conference
on Tibetan Language Computing, 42–49 (2018).
191. Lobsang, T. & Zhao, J. Tibetan text classification using svm and random forest with morphological features. J. Tibet. Inf.
Process. 15, 33–41 (2019).
192. Nyima, S. & Hu, H. Bilstm-crf architectures for tibetan sequence labeling in low-resource settings. In Conference on
Low-Resource NLP for Asian Languages, 77–84 (2020).
193. Gyalpo, T. & Luo, M. Domain-specific tibetan text classification for legal and religious corpora. J. Tibet. Inf. Process. 16,
65–73 (2022).
194. Lhanzey, T. & Zhang, B. Knowledge graph construction for tibetan text via entity linking and relation extraction. In
Workshop on Knowledge Graphs for Low-Resource Languages, 81–89 (2023).
195. Mingjun, Z., Zhuoma, D., Nuo, Q. & Tashi, N. Peftt: Parameter-efficient fine-tuning for low-resource tibetan pre-trained
language models. arXiv preprint arXiv:2309.12109 (2023).
196. Duan, Y., Meng, X., Li, Y. & He, X. Tsbert: A tibetan pretrained language model based on syllables. In 2025 5th
International Conference on Artificial Intelligence and Industrial Technology Applications (AIITA), 1229–1232 (2025).
197. Zhang, W., Liu, F. & Chen, R. Rram-based cnn accelerator for low-power character recognition. IEEE Transactions on
Circuits Syst. 68, 1452–1463 (2021).
198. Li, J., Wang, H. & Xu, M. Memristor-driven handwritten character recognition via crossbar cnn computation. In
Proceedings of the International Symposium on Neuromorphic Systems, 210–218 (2022).
199. Chen, Y., Huang, Q. & Zhao, L. In-memory acceleration of rnn-based language models using rram crossbars. Microelec-
tron. J. 98, 35–44 (2020).
200. Wang, R., Chen, P. & Du, X. Crossbar-optimized seq2seq accelerator for neuromorphic nlp inference. In Proceedings of
the Design, Automation & Test in Europe Conference, 1325–1330 (2023).
201. Luo, Z., Zhu, Z. & Fang, H. Analog accelerator for transformer inference using memristive crossbars. Neurocomputing
512, 284–295 (2022).
202. Tang, J., Li, B. & Xu, K. Crossbar-aware attention unit design for neuromorphic sequence modeling. In Proceedings of
the IEEE International Conference on Computer-Aided Design, 876–884 (2022).
203. Yu, Y. et al. Memristive computing for tibetan spellchecker. IEEE J. Syst. Eng. Electron. (2025).
204. Wang, A. et al. Glue: A multi-task benchmark and analysis platform for natural language understanding. In International
Conference on Learning Representations (ICLR) (2019).
205. Hu, J. et al. Xtreme: A massively multilingual multi-task benchmark for evaluating cross-lingual generalization. In
International Conference on Machine Learning (ICML), 4411–4421 (2020).
206. Hendrycks, D. et al. Measuring massive multitask language understanding. In Proceedings of the International Conference
on Learning Representations (ICLR) (2021).
207. Li, H. et al. Cmmlu: Measuring massive multitask language understanding in chinese. In Findings of the Association for
Computational Linguistics ACL 2024, 11260–11285 (2024).
208. Taori, R. et al. Stanford alpaca: An instruction-following llama model. Stanf. CRFM Blog (2023).
209. Wei, J. et al. Finetuned language models are zero-shot learners. In ICLR (2022).
210. Ouyang, L. et al. Training language models to follow instructions with human feedback. arXiv preprint arXiv:2203.02155
(2022).
211. Rafailov, R. et al. Direct preference optimization: Your language model is secretly a reward model. In Advances in
Neural Information Processing Systems (NeurIPS) (2023).
212. Zhang, Z. et al. Safetybench: Evaluating the safety of large language models with multiple choice questions. arXiv
preprint arXiv:2309.07045 (2023).
34/41

--- Page 35 ---

A Appendix: Proper Noun & Key Parameter Abbreviation
As shown in Table 3, some abbreviations also appear in other chapters; here, we list only those that occur for the first time
within this chapter.
Table 3. Proper Noun & Key Parameter Abbreviation
Part
Full Name
Abbreviation
Abstract
Artificial Intelligence
AI
Large Language Model
LLM
Natural Language Processing
NLP
Section 1
-
-
Section 2
Buddhist Digital Resource Center
BDRC)
Tibetan and Himalayan Library
THL
Rangjung Yeshe Tibetan Corpus
RYTC
Tibetan Wikipedia Dump
TWD
Asian Classics Input Project
ACIP
OpenSubtitles Tibetan Fragment Collection
OTFC
Chain of Thought
CoT
Tibetan Language Understanding Evaluation
TLUE
Tibetan Automatic Speech Recognition
ASR
Section 3
Parameter-Efficient Fine-Tuning
PEFT
Word Segmentation
WS
Part-of-speech Tagging
POS
Named Entity Recognition
NER
Text Classification
TC
Sentence Similarity
SS
Entailment Detection
ED
Speech Recognition
SR
Optical Character Recognition
OCR
Machine Translation
MT
Statistical Machine Translation
SMT
Text Generation
TG
Summarization
SUM
Text-to-speech
TTS
Speech Synthesis
TTS
Question Answering
QA
Dialogue Generation
DG
Multimodal Generation
MG
Section 4
Rule-based
RB
Machine Learning
ML
Deep Learning
DL
Convolutional Neural Network
CNN
Recurrent Neural Network
RNN
Long Short-Term Memory
LSTM
Machine Learning
ML
Deep Learning
DL
Support Vector Machine
SVM
Hidden Markov Model
HMM
Conditional Random Field
CRF
Maximum Entropy Model
MaxEnt
Section 5
-
-
Section 6
-
-
Appendix A
-
-
Appendix B
Reinforcement Learning from Human Feedback
RLHF
Direct Preference Optimization
DPO
Appendix D
-
-
Appendix E
-
-
35/41

--- Page 36 ---

B Appendix: Details of TIBSTC & TIBSTC-CoT
B.1 TIBSTC: Structured Tibetan Corpus for Instruction-Tuning
TIBSTC18 is constructed as a large-scale structured Tibetan corpus with the explicit goal of serving as a foundation for
Tibetan-centric language modeling. Unlike previous Tibetan datasets that primarily focused on isolated tasks such as OCR
or machine translation, TIBSTC follows a unified representation scheme that organizes data at multiple linguistic levels,
including syllable segments, word tokens, sentence pairs, and multi-turn instruction samples. All data is stored with parallel
metadata fields for Tibetan, Simplified Chinese, and English, ensuring alignment consistency across downstream
translation, classification, reasoning, and generation tasks.
B.1.1 Corpus Sources & Domain Coverage
The dataset aggregates Tibetan texts from four main categories:
• Digitized Classical Literature & Canonical Buddhist Text
• Conversational Tibetan from Social Media & Daily Communication
• Tibetan Legal & Administrative Document
• Modern Tibetan News & Educational Content
As reported in the original dataset release, around 66% of the corpus comes from literature and religious texts, 24% from
contemporary web sources, and 10% from media and documentary transcripts, providing both formal and colloquial linguistic
coverage.
B.1.2 Preprocessing and Normalization
All raw texts underwent Unicode normalization to remove incompatible codepoints while preserving Tibetan diacritic structures.
To prevent the loss of traditional Tibetan morphology, no modern rewriting or aggressive spelling correction was applied;
instead, non-standard syllable forms were preserved and annotated. Each data entry is packed into structured JSON format with
hierarchical fields for syllable_segmentation, token_alignment, and parallel_translations, enabling
explicit control over syllable-level processing and cross-lingual supervision.
B.1.3 Instruction Formatting
Following the principles of instruction-tuning corpora such as Alpaca208 and FLAN209, TIBSTC introduces instruction-style
prompts specifically adapted for Tibetan. Each prompt-entry pair contains a human-readable Tibetan instruction, a controlled-
format system tag, and a target response. Unlike generic multilingual instruction datasets, TIBSTC enforces EWTS-compatible
tokenization146 to ensure that Tibetan script decomposition remains stable under byte-level tokenizers. The instruction subset is
further divided into 4 subsets:
• Alpaca-Ti: a Tibetan adaptation of Alpaca-style supervised instruction pairs, generated through translation-aligned
prompting and manually verified to ensure that Tibetan imperative moods and honorific expressions remain semantically
faithful to the original intent.
• Safety-Prompts-Ti: a curated subset focused on Tibetan safety alignment, containing refusal, ethical compliance, and
content moderation prompts tailored to culturally sensitive Tibetan contexts such as religion, medical advice, and regional
governance.
• CValues-Ti: a value-grounded instruction set incorporating Tibetan cultural priors, including compassion ethics, monastic
discourse norms, and traditional knowledge frameworks, designed to steer model outputs toward culturally coherent
Tibetan reasoning.
• hh-rlhf-Ti: a Tibetan variant of human-preference training pairs following HH-RLHF210 conventions, where multiple
Tibetan responses are ranked by native speakers to provide preference signals for RLHF210 or DPO-style211 alignment in
low-resource Tibetan settings.
They allow systematic scaling from supervised fine-tuning to preference alignment and safety modeling.
B.1.4 Human Verification & Linguistic Consistency
To ensure linguistic validity beyond automatic normalization, the dataset construction involved multiple rounds of manual audit-
ing by native Tibetan speakers, including monks, legal clerks, and Tibetan computational linguists. Inconsistent segmentation
or mistranslated parallel entries were annotated and filtered through majority judgment, providing higher semantic stability than
web-scraped translation corpora.
36/41

--- Page 37 ---

B.1.5 Dataset Role
Due to its structured alignment between script-level segmentation, multilingual mapping, and instruction semantics, TIBSTC
functions not only as a dataset but also as a benchmark protocol. It is used as the base corpus for Tibetan-centric LLMs such as
Sun-Shine18 and later extended into the TIBSTC-CoT17 reasoning subset for multi-step Tibetan instruction alignment.
B.2 TIBSTC-CoT: Chain-of-Thought Extension for Tibetan Reasoning Alignment
While TIBSTC18 provides token-level alignment and supervised instruction pairs for base model tuning, it does not explicitly
encode multi-step reasoning or stepwise logical articulation. To address this limitation, TIBSTC-CoT17 is constructed as a
reasoning-augmented extension that introduces explicit chain-of-thought supervision, enabling models to generate intermediate
reasoning traces instead of producing only final answers.
B.2.1 Multi-Agent CoT Generation Framework
TIBSTC-CoT follows a three-agent pipeline: (1) a question agent generates instruction prompts, (2) a reasoning agent produces
multi-step explanation sequences, and (3) an evaluation agent assigns an automatic quality score on a 1-5 scale.
Only samples with a score greater than or equal to 3.5 are preserved, after which human annotators perform manual quality
refinement to ensure linguistic coherence and segmentation consistency.
B.2.2 Reasoning Categories and Template Diversity
The CoT subset covers multiple reasoning types aligned with the TLUE benchmark44, including comparison reasoning, legal
interpretation, cultural logic grounding, analogy explanation, and multi-step factual inference. Each sample is formatted using
an explicit structure with labeled reasoning steps (e.g., Step 1, Step 2, Therefore), making the chain-of-thought trace directly
learnable by generative Tibetan LLMs.
B.2.3 Abstract Structure Illustration
Since this appendix focuses on structural representation rather than content disclosure, illustrating the abstract CoT template
used throughout the dataset without including Tibetan text tokens.
Abstract structure illustration:
• Instruction: Explain the difference between two similar statements.
• Reasoning Trace:
– Step 1: Identify semantic focus.
– Step 2: Compare logical implications.
– Step 3: Produce final explanation.
• Final Answer: Concise contrast statement.
• Score: 4.3
B.2.4 Integration with Model Alignment
TIBSTC-CoT is used as the primary chain-of-thought supervision source for Sun-Shine 2.017. The dataset is mixed with
supervised instruction pairs following a 3:1 ratio, enabling models to learn both safe response behaviors and explicit reasoning
traces. In subsequent evaluation, TIBSTC-CoT samples were shown to enhance reasoning-related performance categories
in TLUE44, improving consistency and interpretability of generated explanations compared to models trained without CoT
alignment.
37/41

--- Page 38 ---

C Appendix: Details of TLUE Benchmark
C.1 Overview
As shown in Figure 5, TLUE provides a comprehensive evaluation suite for Tibetan language understanding by integrating
both knowledge-oriented and safety-oriented assessment tracks. On the knowledge side, Ti-MMLU contains 11,528 questions
across 67 subjects, covering STEM, humanities, social sciences, China-specific topics, and general knowledge, enabling
systematic measurement of factual and reasoning capabilities in Tibetan. On the safety side, Ti-SafetyBench contributes 11,435
adversarial and alignment-sensitive questions spanning seven critical categories, including ethics, bias, health, offensiveness,
privacy, and illegal content, targeting robustness and responsible model behavior. Together, these components form TLUE, a
22,963-question Tibetan Language Understanding Evaluation framework that jointly assesses both cognitive competency and
value-aligned safety for Tibetan LLMs.
Ti-MMLU
Knowledge
11528 Questions  
 67 subjects
13 Social Sciences Tasks
17 STEM Tasks
11 Humanities Tasks
11 Other Tasks
TLUE
A Tibetan Language
Understanding Evaluation
Benchmark
22963 Questions
Ti-SafetyBench
Safety
11435 Questions  
 7 categories
Ethics and Morality
Unfairness and Bias
Physical
Health
Mental
Health
Offensiveness
Privacy and Property
llegal Activities
15 China Specific Tasks
Figure 5. Overview of the TLUE Benchmark
To the best of our knowledge, TLUE is the first and currently the only benchmark that systematically evaluates Tibetan
language capabilities in LLMs. Proposed by our team, it has been accepted to the EMNLP 2025 main conference.
C.2 Ti-MMLU
For its sub-benchmark, Ti-MMLU4, it is an evaluation sub-benchmark designed specifically for Tibetan LLMs, similar
to MMLU206 in the English field and CMMLU207 in the Chinese field. It comprehensively tests the LLM’s knowledge
understanding and reasoning capabilities in a multi-disciplinary and multi-task environment through multiple-choice questions.
As shown in Firgure 6, Ti-MMLU contains 67 subtasks, covering multiple subject areas from middle school to university
and even professional examinations, such as mathematics, physics, history, law, medicine, engineering, philosophy, literature,
etc., covering the unique local knowledge system in Tibetan areas, such as college entrance examinations, teacher qualification
certificates, medical examinations, etc., and is particularly suitable for evaluating the LLM’s mastery of Tibetan language
context and professional knowledge.
Ti-MMLU uses zero-shot or few-shot settings, does not provide contextual learning, and directly examines the generality
and true capabilities of the model. It is not only suitable for model comparison and ranking, but also helps developers discover
the weak links of the model in specific fields, such as law and medicine.
C.3 Ti-SafetyBench
For its another sub-benchmark, Ti-SafetyBench5, it is a multilingual benchmark systematically evaluate the safety of LLMs,
similar to SafetyBench212, when handling sensitive or high-risk Tibetan content. It consists of multiple-choice questions, and
supports zero-shot and few-shot evaluation settings to enable standardized comparisons across different models.
Also, Ti-SafetyBench covers eight core safety categories: Offensiveness, Unfairness and Bias, Physical Health, Mental
Health, Illegal Activities, Ethics and Morality, Privacy and Property, and Safety-Related Reasoning. These categories reflect
common areas of concern in real-world applications where unsafe or harmful responses from LLMs may occur.
By providing a structured, quantifiable framework for assessment, Ti-SafetyBench serves as a critical tool for developers,
researchers, and policymakers in improving and regulating the deployment of safe and trustworthy AI systems for Tibetan.
4License: CC-BY-NC-SA 4.0
5License: Apache License 2.0
38/41

--- Page 39 ---

Ancient Chinese
Chinese Civil Service Exam
Chinese Food Culture
Chinese Foreign Policy
Chinese Teacher Qualification
Elementary Chinese
Ethnology
High School Politics
Modern Chinese
Chinese Driving Rule
Construction Project Management
Elementary Commonsense
Traditional Chinese Medicine
Chinese Literature
Chinese History
 
 
Electrical Engineering
Engineering Hydrology
Astronomy
Medical Statistics
Conceptual Physics
Machine Learning
High School Physics
High School Mathematics
High School Chemistry
High School Biology
Elementary Mathematics
Actuarial Science
Genetics
College Mathematics
Virology
Computer Science
Anatomy
World Religions 
World History 
Professional Law 
Philosophy 
Marxist Theory 
Logical 
Jurisprudence  
International Law 
Global Facts 
College Law  
Arts
Other
China specific
STEM
Social Sciences
Humanities
11 (16.4%)
15 (22.3%)
17 (25.3%)
13 (19.4%)
11 (16.4%)
Figure 6. Statistical Category of the Ti-MMLU Benchmark
C.4 Summary
Release of the TLUE benchmark addresses a critical gap in Tibetan AI: the lack of standardized evaluation settings. By
offering the first domain-aware, task-diverse benchmark, TLUE lays the foundation for future research in Tibetan language
understanding, especially in the context of multilingual and low-resource language modeling.
39/41

--- Page 40 ---

D Appendix: Sun-Shine LLM Family
D.1 Sun-Shine: Base Tibetan Instruction Model
Sun-Shine18 is the first Tibetan-centric instruction-tuned language model trained exclusively on the TIBSTC18 corpus. Rather
than relying on multilingual pretraining, it adopts a tokenizer aligned with the EWTS writing convention to stabilize segmenta-
tion over Tibetan syllable structures. All instruction samples follow a controlled Alpaca-style formatting process with manual
verification to ensure that directive semantics are preserved.
D.1.1 Training Objective
Supervised instruction tuning without any chain-of-thought decomposition or reinforcement-style preference optimization,
focusing purely on direct input-to-output mapping.
D.1.2 Corpus
Trained exclusively on the TIBSTC instruction subset, which contains declarative prompt–response pairs but does not include
multi-step reasoning traces or ranked candidate responses.
D.1.3 Tokenizer
Employs a custom EWTS-aligned vocabulary to ensure that Tibetan syllable units remain intact during subword segmentation,
preventing fragmentation issues common in multilingual tokenizers.
D.1.4 Interaction Format
Restricted to single-turn instruction–response interactions without conversational memory or iterative refinement, reflecting a
pure supervised fine-tuning regime.
D.1.5 Alignment Scope
No safety filtering, refusal modeling, or culturally grounded preference alignment signals are applied, making Sun-Shine a
direct baseline of instruction-following behavior without alignment-level constraints.
Alignment scope: no safety filtering, refusal modeling, or culturally grounded preference alignment signals are applied,
making Sun-Shine a baseline that reflects raw supervised instruction-following capabilities.
D.2 Sun-Shine 2.0: CoT and Preference-Aligned Tibetan LLM
Sun-Shine 2.017 extends Sun-Shine by incorporating CoT supervision and preference-ranked alignment signals derived from
TIBSTC-CoT, Safety-Prompts-Ti, and hh-rlhf-Ti. In contrast to direct answer generation, the model is trained to produce
multi-step reasoning traces using labeled inference stages such as Step 1, Step 2, and Therefore.
D.2.1 Training Objective
Combined CoT enhanced supervised fine-tuning and preference-based alignment following a DPO-style optimization objective,
enabling the model to internalize both direct instruction mapping and ranked response preference patterns.
D.2.2 Reasoning Supervision
Exposed to multi-step reasoning traces derived from TIBSTC-CoT, where explicit stepwise inference structures are embedded
to encourage interpretable intermediate output generation instead of single-pass answers.
D.2.3 Alignment Mechanism
Trained with preference-ranked response pairs aligned to RLHF210/DPO211 conventions, allowing the model to distinguish
between acceptable and suboptimal Tibetan responses based on human- or model-evaluated preference signals.
D.2.4 Safety Scope
Injected with structured refusal and compliance prompts to regulate ungrounded generation, establishing controllable output
behavior under safety, neutrality, and culturally coherent response constraints.
D.2.5 Interaction Format
Supports stepwise reasoning expansion and more stable multi-turn dialogue behavior, in contrast to the strictly single-turn
instruction–response interface of the initial Sun-Shine model.
40/41

--- Page 41 ---

E Appendix: Memristor & Tibetan AI
E.1 Motivation: Beyond Digital Tibetan NLP
Conventional Tibetan NLP systems, including OCR, ASR, spellchecking, and LLM-based reasoning, rely entirely on digital
GPU computation. While effective, these architectures suffer from repeated memory shuttling between compute units and
storage, especially when processing syllable-structured tokens that require frequent pattern matching and subword alignment.
Memristor-based in-memory computing offers a fundamentally different pathway by enabling matrix-vector multiplications and
pattern similarity operations directly within resistive crossbar arrays. For languages such as Tibetan, where token discrimination
depends on a limited set of combinatorial syllable components, this analog computation model aligns naturally with the structure
of the script.
E.2 Existing Hardware Prototypes for Tibetan Symbolic Processing
Only two published hardware efforts currently exist in this direction. The first demonstrates a memristive computing architecture
for Tibetan syllable component recognition, where binary-encoded component patterns are projected onto memristor arrays for
in-memory matching143. The second work extends this idea toward spell-level error detection using a similar crossbar-based
current comparison mechanism, marking the first use of analog resistive hardware for Tibetan orthographic processing203.
Both systems operate on symbolic representations rather than neural embeddings, but they provide concrete evidence that
Tibetan-specific pattern structures can be mapped into analog memory states.
E.3 Architectural Relevance to Future Neuromorphic Tibetan LLMs
Although current memristor-based Tibetan accelerators focus on discrete rule-based matching, their structural properties mirror
fundamental operations in LLM inference, such as embedding projection, token gating, and attention-based similarity scoring.
The resistive crossbar mapping used for syllable detection can be viewed as a hardware-level analogue of subword embedding
lookup or prefix gating during decoding. This suggests that future Tibetan LLMs could be partially offloaded to specialized
analog arrays that accelerate token activation and linguistic pattern filtering before digital transformer layers perform high-level
reasoning.
E.4 Toward Hybrid Analog–Digital Tibetan Language Models
These early prototypes indicate that Tibetan AI workloads possess a discrete symbolic structure that makes them suitable for
hybrid analog–digital architectures. A feasible future research path is to integrate memristor-based prefix and subcomponent
matching units as a pre-filter stage in LLM decoding, allowing analog hardware to discard low-relevance token candidates
before digital attention computation. This would reduce memory bandwidth pressure and align with the low-resource setting of
Tibetan NLP, where efficiency gains can directly improve accessibility in edge devices and offline educational deployments.
41/41

```
