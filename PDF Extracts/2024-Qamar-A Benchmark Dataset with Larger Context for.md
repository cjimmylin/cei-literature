---
title: "A Benchmark Dataset with Larger Context for - PDF Extract"
source_pdf: "2024-Qamar-A Benchmark Dataset with Larger Context for.pdf"
pages: 28
extracted_at: "2026-01-24T17:05:40.399038"
---

# PDF Extract: A Benchmark Dataset with Larger Context for

**Source PDF:** 2024-Qamar-A Benchmark Dataset with Larger Context for.pdf
**Total Pages:** 28

---

## Content

```
--- Page 1 ---

A Benchmark Dataset with Larger Context for
Non-Factoid Question-Answering over Islamic Text
Faiza Qamar
School of Electrical Engineering and Computer Science (SEECS)
National University of Sciences and Technology (NUST),
Islamabad, Pakistan.
Seemab Latif†
School of Electrical Engineering and Computer Science (SEECS)
National University of Sciences and Technology (NUST),
Islamabad, Pakistan.
Rabia Latif
College of Computer and Information Sciences (CCIS)
Prince Sultan University, Riyadh, 12435, Saudi Arabia
Abstract
Accessing and comprehending religious texts, particularly the Quran (the sacred
scripture of Islam) and Ahadith (the corpus of the sayings or traditions of the
Prophet Muhammad), in today’s digital era necessitates efficient and accurate
Question-Answering (QA) systems. Yet, the scarcity of QA systems tailored
specifically to the detailed nature of inquiries about the Quranic Tafsir (expla-
nation, interpretation, context of Quran for clarity) and Ahadith poses signif-
icant challenges. To address this gap, we introduce a comprehensive dataset
meticulously crafted for QA purposes within the domain of Quranic Tafsir and
Ahadith. This dataset comprises a robust collection of over 73,000 question-
answer pairs, standing as the largest reported dataset in this specialized domain.
Importantly, both questions and answers within the dataset are meticulously en-
riched with contextual information, serving as invaluable resources for training
and evaluating tailored QA systems. However, while this paper highlights the
dataset’s contributions and establishes a benchmark for evaluating QA perfor-
mance in the Quran and Ahadith domains, our subsequent human evaluation
uncovered critical insights regarding the limitations of existing automatic evalu-
ation techniques. The discrepancy between automatic evaluation metrics, such
as ROUGE scores, and human assessments became apparent. The human eval-
†Corresponding author: Seemab Latif (Email: seemab.latif@seecs.edu.pk; ORCID: 0000-
0002-5801-1568)
Preprint submitted to Elsevier
September 17, 2024
arXiv:2409.09844v1  [cs.CL]  15 Sep 2024

--- Page 2 ---

uation indicated significant disparities: the model’s verdict consistency with
expert scholars ranged between 11% to 20%, while its contextual understand-
ing spanned a broader spectrum of 50% to 90%. These findings underscore the
necessity for evaluation techniques that capture the nuances and complexities in-
herent in understanding religious texts, surpassing the limitations of traditional
automatic metrics.
Keywords:
Question-Answering System; Non-Factoid Question-Answers;
Question-Answering Dataset; Automatic Evaluation Techniques; Human
Evaluation
1. Introduction
In the age of rapidly advancing technology and the increasing reliance on
digital resources, there arises a pressing need for efficient and accurate methods
to access and comprehend religious texts [29]. Specifically, the Quran and Aha-
dith hold immense significance for millions of individuals seeking guidance and
understanding in their religious practices [21]. The Quran is the central religious
text in Islam, revealed upon the last Prophet Muhammad (P.B.U.H). Tafsir, the
interpretation of the Quran, helps us understand its meaning and context. On
the other hand, Ahadith are the sayings and actions of Prophet Muhammad
(P.B.U.H), providing guidance for Muslims [18]. Being the fundamental sources
of Islamic legislation, having a reliable and comprehensive QA system designed
specifically for the Quran and Ahadith can greatly aid in exploring and under-
standing these important texts. However, exploring these vast repositories of
knowledge can be a time-consuming and challenging task [38].
By leveraging advancements in natural language processing and machine
learning, Question-Answering (QA) systems offer the promise of swiftly retriev-
ing relevant passages and generating answers to questions in natural language
[34].
In Question-Answering Systems (QAS), Long-form question-answering
(LFQA) is an intriguing challenge that involves retrieving documents relevant
to a given question and using them to generate a paragraph-length answer
[13]. While there has been remarkable recent progress in factoid open-domain
question-answering, where a short phrase or entity is enough to answer a ques-
tion [20], LFQA is still understudied and challenging for Large Language Models
(LLMs) [10]. LFQA is an important task, especially because it provides a test-
bed to measure the factuality of generative text models. To make progress in
long-form question-answering, researchers need a large, diverse dataset of com-
plex how- and why-type questions with paragraph-length answers.
While QA systems have been developed for various fields, their application
to the Quran, Tafsir, and Ahadith is very significant, but scarce [8]. Muslims
worldwide rely on Muslim scholars for guidance in their daily life queries. Several
studies have concentrated on a wide range of topics on Islamic text from retrieval
to classification. However, where QA is of concern only factoid type has been
addressed [20]. Some of these studies are in Arabic [29, 28, 1, 39, 17], English
[18], and Indonesian [35]. Whereas question answers available online on https:
2

--- Page 3 ---

//islamqa.org1 strongly points out that the users require not only factoid but
detailed answers to their questions with references from the Quran and Ahadith.
A QA system targeting Quran and Ahadith that could answer users’ ques-
tions with extensive details has its own set of challenges.
These challenges
include but are not limited to; lack of dataset, appropriate question classifica-
tion system, accurate facts extraction from different sources while keeping in
mind the context provided by the user, to infer the answer [42], and the absence
of suitable evaluation techniques that can adequately address the sensitivity of
this domain because precision is of utmost importance here.
This paper has two significant contributions in the following areas:
1. The research presents a comprehensive and extensive dataset specifically
designed to address the question-answering problem in the domain of
Quran, Tafsir, and Ahadith. The dataset consists of over 73,000 question-
answer pairs, making it, to the best of our knowledge, the largest reported
dataset for long-form question-answering in this domain.
Importantly,
both the questions and answers come with rich contextual information,
providing valuable resources for training and evaluating tailored question-
answering systems2.
2. The paper introduces a benchmark for evaluating question-answering sys-
tems targeted towards the intricacies of the Quran, Tafsir, and Ahadith.
This benchmark serves as a standardized evaluation framework, allowing
researchers to assess the performance of their models and compare them
against existing approaches. It enables the advancement of QA systems
specifically tailored for religious literature.
The following sections will provide a comprehensive analysis of existing liter-
ature (Section 2), present the methodology used for data collection (Section
3), discuss the obtained results (Section 4), analyze findings (Section 5), and
conclude with implications and suggestions for future research (Section 6).
2. Related Work
In the dynamic field of natural language processing, the pursuit of effective
long-form question-answering models is underscored by the critical role played
by meticulously curated datasets. This literature review embarks on a dual ex-
ploration, focusing on datasets that cater to the broader landscape of long-form
question-answering, while concurrently digging into specialized datasets tailored
for the unique challenges presented by the interpretation and understanding of
Quranic verses and Ahadith. By examining the characteristics, methodologies,
and outcomes associated with these datasets, in this section, we aim to provide
a nuanced perspective on the advancements made in the development of models
1It has indexed the answers to over 90K questions of the Muslims across the globe
2Dataset will be released along with the submission of accepted paper
3

--- Page 4 ---

capable of comprehending and responding to extended queries, with a specific
emphasis on the sacred texts of Islam.
It is divided into three parts; review of language models, available datasets
and work on religious scriptures.
2.1. Language Models
The introduction of LLMs and transformers has significantly shaped research
in LFQA. These models have enabled the development of automated systems
that can generate detailed, paragraph-length answers to complex questions, ad-
dressing real-world issues such as legal literacy, analyzing public opinion on
politics, and information retrieval etc.
Several recent studies have proposed
novel methodologies and frameworks to improve the performance of LFQA mod-
els, addressing challenges such as generating faithful answers with less halluci-
nated content, evaluating long-form output, and incorporating exemplification
in question-answering.
Long-form question-answering (LFQA) research has made progress using
large pre-trained models, but a primary challenge remains: generating faith-
ful answers with less hallucinated content.
To address this, a recent study
proposed an end-to-end framework that jointly models answer generation and
machine reading, incorporating fine-grained, answer-related salient information
to emphasize faithful facts [40]. This approach achieved state-of-the-art results
on two LFQA datasets (ELI5 and MS MARCO), outperforming strong base-
lines on both automatic and human evaluation metrics.
A detailed analysis
confirmed the effectiveness of this method in generating fluent, relevant, and
faithful answers, contributing to the advancement of LFQA research.
Another research has demonstrated the capabilities of large language mod-
els (LLMs) in question-answering and long-form text generation, particularly in
few-shot closed-book settings. However, evaluating long-form output remains a
challenge. A recent study addressed this issue by combining question-answering
with long-form answer generation, leveraging multifaceted questions that require
information from multiple sources [5]. The authors introduced query refinement
prompts to encourage LLMs to explicitly address question ambiguities and gen-
erate comprehensive answers. Experiments on ASQA and AQuAMuSe datasets
showed that this approach outperformed fully fine-tuned models in closed-book
settings and achieved comparable results to retrieve-then-generate open-book
models, highlighting a promising direction for evaluating and improving LLMs’
long-form answer generation capabilities.
Exemplification, the process of using examples to clarify complex concepts,
is a crucial aspect of long-form question-answering (LFQA). Despite its im-
portance, exemplification in QA has received little computational attention. A
recent study addressed this gap by conducting a fine-grained annotation of differ-
ent example types in three corpora, revealing that state-of-the-art LFQA models
struggle to generate relevant examples [43]. Furthermore, standard evaluation
metrics like ROUGE were found to be insufficient for assessing exemplification
quality. The authors proposed a novel approach, treating exemplification as
a retrieval problem, which allows for reliable automatic metrics that correlate
4

--- Page 5 ---

well with human evaluation. Human evaluation confirmed that the proposed
model’s retrieved examples were more relevant than those generated by state-
of-the-art LFQA models, highlighting the potential of this approach to improve
exemplification in LFQA.
The following section highlights the datasets available to support the LFQA
and their importance in its progress.
2.2. Datasets
The exploration and analysis of suitable datasets play a pivotal role in ad-
vancing the capabilities of models designed to comprehend and respond to com-
plex queries in extended textual contexts. This section of the literature review
looks into the landscape of datasets tailored specifically for Long-Form Question-
Answering (LFQA), scrutinizing their characteristics, strengths, and limitations.
By navigating through the diverse array of datasets available, we aim to gain a
comprehensive understanding of the challenges posed by extended-context ques-
tions and the advancements achieved through the utilization of various datasets
in the development of robust and nuanced question-answering systems.
LFQA term was formally introduced in 2019 by Facebook when they re-
leased the dataset Explain Like I’m Five (ELI5) along with a leader board 3.
ELI5 stands as the most extensive dataset for the Question-Answering task,
comprised of posts and comments from the Reddit forum ”Explain Like I’m
Five” annotated with explanations for diverse concepts [15]. ELI5 encompasses
both abstractive and extractive answers and is the largest reported dataset
with 270K QA pairs for Long-form question-answering. The magnitude of the
ELI5 dataset assumes particular importance, as it lays the foundation for the
development of models adept at handling a broad array of questions and cor-
responding answers. This capacity is integral for the practical application of
LFQA systems, where real-world scenarios demand a nuanced understanding
of diverse topics.
The substantial size of the dataset contributes to the ro-
bustness of LFQA models, enabling them to navigate and respond effectively
to the intricate and varied nature of user queries within the broader context
of natural language understanding. However, a notable critique of ELI5 lies
in potential inaccuracies and incompleteness within explanations. Given that
they are contributed by internet volunteers, leaving room for misinformation.
The dataset is derived from user-generated content on the Reddit community,
which may contain noise, inaccuracies, or subjective interpretations. This can
lead to a lower quality of data, which can negatively impact the performance
of LFQA models trained on this dataset [48]. Furthermore, the dataset’s ori-
gins within the Reddit community may introduce biases, deviating from expert
or generalized explanations. This bias should be cautiously considered when
utilizing the ELI5 dataset for machine learning models. Despite its status as
the largest Long Form Question-Answering dataset, its 81% train/eval overlap
3https://facebookresearch.github.io/ELI5/
5

--- Page 6 ---

impacts model performance, necessitating careful handling during training and
evaluation [22].
Other datasets existed before ELI5 which also addressed the problem of
LFQA, i.e. Microsoft Machine Reading Comprehension (MS MARCO) 4 and
Natural Questions (NQ) [23]. MS MARCO is a collection of large-scale datasets
focused on machine reading comprehension, question-answering, and passage
ranking. It is used for various tasks such as question-answering, natural lan-
guage generation, passage ranking, keyphrase extraction, crawling, and conver-
sational search. The MS MARCO datasets are derived from real anonymized
Bing user queries and real web documents, making them grounded in real-world
problems and providing valuable resources for advancing research in these ar-
eas [7, 6]. It emerges as a substantial contributor to the domain of machine
question-answering and passage ranking, garnering attention within the litera-
ture for its commendable attributes and acknowledged drawbacks. Noteworthy
merits encompass the incorporation of approximately 500,000 5 authentic search
queries sourced from the Bing search engine, providing a reservoir of real-world
queries essential for training models in information retrieval. Furthermore, the
dataset distinguishes itself by presenting human-generated answers, a facet that
bolsters the overall quality of the dataset. Its sheer scale, constituting a large
and diverse collection, proves advantageous for the training and evaluation of
machine learning models [7].
However, the dataset is not without its demerits, as scrutinized in the liter-
ature. Notably, concerns arise regarding the high level of redundancy present
in the dataset, potentially influencing the efficacy of model training and evalu-
ation. Additionally, apprehensions about unfair comparisons surface due to the
existence of two distinct corpora within MS MARCO, leading to challenges in
result reproduction and the monitoring of state-of-the-art outcomes. Further
complicating matters, instances of augmented data introducing leaked relevant
information contravene the original guidelines of the dataset. The dataset does
not include multi-hop reasoning questions, which are important for evaluating
models’ ability to reason over multiple pieces of information [24].
The NQ dataset is a large-scale, real-world dataset for QA research.
It
consists of anonymized, aggregated queries issued to the Google search engine
and is designed to drive research in Natural Language Understanding (NLU)
and provide a benchmark for QA systems.
In contrast with the MS Marco
dataset, it contains 100,000 questions with free-form answers. For each question,
annotators are presented with 10 passages returned by the search engine. They
are asked to generate an answer to the query or state that the answer is not
contained within the passages [23].
[27] addressed the legal literacy gap by proposing an end-to-end methodology
for generating long-form answers to statutory law questions.
The approach
utilized a ”retrieve-then-read” pipeline and was supported by the introduction
4https://microsoft.github.io/MSMARCO-Question-Answering/
5https://www.sbert.net/examples/training/ms_marco/README.html
6

--- Page 7 ---

of the Long-form Legal Question-Answering (LLeQA) dataset, comprising 1,868
expert-annotated legal questions in French. While the results showed promising
performance on automatic evaluation metrics, a qualitative analysis revealed
areas for refinement. The LLeQA dataset has the potential to accelerate research
towards resolving real-world issues and act as a benchmark for evaluating NLP
models in specialized domains.
Moreover, the development of the WebCPM dataset for Chinese LFQA intro-
duced a unique feature where information retrieval is based on interactive web
search, resulting in a pipeline that generates answers comparable to human-
written ones [36].
These studies collectively demonstrate the significant impact of Datasets and
large language models on shaping research in long-form question-answering, ad-
dressing various challenges and advancing the capabilities of automated systems
in generating detailed, coherent answers to complex questions [12].
2.3. Literature on Religious Scriptures
This section highlights the work done on the Quran and Ahadith.
Several studies have addressed the challenge of auto-extracting reliable an-
swers from reference texts, such as constitutions or holy books [19, 2, 42]. Among
these texts, the Quran and Ahadith hold particular significance as the holy scrip-
tures of Islam, serving as primary legislative sources for millions of Muslims
globally.
An Arabic Question-Answering (QA) system specialized in Islamic sciences,
including prophetic tradition (Hadith), Hadith narrator encyclopedia [30], and
Quran interpretation (Tafsir), was developed to address the complexity of un-
structured information in online databases [29]. The system’s knowledge re-
source is a normalized database in the Text Encoding Initiative (TEI) standard,
and it employs a three-phase method: question analysis, information search, and
answer processing. A graphic interface allows user interaction. Experimental
results on 100 questions in Hadith, narrator, and Tafsir themes showed a 92% ac-
curacy rate in generating responses, demonstrating the system’s effectiveness in
providing accurate answers to factoid questions in Islamic research fields. This
study contributes to the development of QA systems for specialized domains
and languages.
In a similar vein, [44] proposed a question-answering system built on a Ha-
dith knowledge graph to address the limitations of existing digital platforms
in answering religious questions. The system utilized the Levenshtein distance
function to interpret user questions and Neo4J as the graph database to store
the Hadith in a graph format. The results showed that (i) a knowledge graph
is suitable for representing the Hadith and performing reasoning tasks, and (ii)
the proposed approach achieved a top-1 accuracy of 95%. This study demon-
strates the potential of knowledge graph-based question-answering systems for
religious texts, enabling users to seek answers to specific questions and pro-
moting a deeper understanding of Islamic knowledge. Notably, their findings
indicated an improvement in the system’s results through the utilization of the
Levenshtein distance approach [46].
7

--- Page 8 ---

The ”Qur’an QA 2022” shared task was organized to promote state-of-the-
art research in Arabic Question-Answering (QA) and Machine Reading Compre-
hension (MRC) on the Holy Qur’an, a rich source of knowledge for Muslim and
non-Muslim inquirers [28]. The task attracted 13 participating teams, with 30
submitted runs, demonstrating the growing interest in QA and MRC research.
This overview paper provides insights into the main approaches adopted by
participating teams, highlighting trends and perceptions that characterize the
submitted systems. The shared task aims to advance research in Arabic QA
and MRC, enabling the development of more accurate and efficient question-
answering systems for the Holy Qur’an.
The automatic extraction of reliable answers from religious texts, such as the
Qur´an, poses a significant challenge for the natural language processing commu-
nity. Despite its importance, previous research on Question-Answering (Q&A)
from the Qur´an is limited and lacks a benchmark for meaningful comparison.
Recently, a shared task [28] was organized, providing a dataset of 1,093 question-
Qur´an passage pairs [3]. A participating system achieved the best scores of 0.63
pRR and 0.59 F1 on the development set and 0.56 pRR and 0.51 F1 on the test
set, with an Exact Match score of 0.34, highlighting the difficulty of the task and
the need for further research. This study contributes to the development of QA
systems for religious texts, enabling users to seek answers to specific questions
and promoting a deeper understanding of Islamic knowledge.
Despite progress in Question-Answering (QA) systems, Arabic QA systems
face challenges, particularly for the Holy Qur’an, due to limited resources and
the difference between Classical and Modern Standard Arabic [32]. To address
this, a Deep Learning-based method was proposed for the Qur’an QA 2022
Shared task, fine-tuning models on large datasets before adapting to the target
dataset.
This approach achieved promising results, with 66.9% pRR on the
development set and 54.59% pRR on the test set. This study contributes to
the development of effective QA systems for the Holy Qur’an, highlighting the
potential of Deep Learning techniques in overcoming the limitations of existing
resources.
A concept-based searching tool (QSST) for the Holy Quran was developed to
facilitate information retrieval for Quran scholars and Arabic researchers [31].
The tool consists of four phases: dataset construction by annotating Quran
verses based on the ontology of Mushaf Al-Tajweed, word embedding using
Continuous Bag of Words (CBOW) architecture, feature vector calculation for
input queries and Quranic topics, and retrieving relevant verses by computing
cosine similarity. Evaluation metrics (precision, recall, F-score) showed promis-
ing results (76.91%, 72.23%, 69.28%), and expert evaluation by Islamic scholars
achieved an average precision of 91.95%. Comparison with existing tools demon-
strated the superior performance of QSST, highlighting its potential for efficient
concept-based searching in the Quran.
Arabic Question-Answering Systems (QAS) face challenges due to the com-
plexity of the Arabic language, despite its widespread use by 450 million native
speakers [4]. Current QASs are limited to specific domains, and a comprehensive
examination is needed to improve development. While previous studies catego-
8

--- Page 9 ---

rized QASs based on various factors, there is a lack of research on development
techniques. This systematic literature review aimed to address this gap by an-
alyzing 40 selected papers from a pool of 617 articles. The findings highlight
the importance of datasets and deep learning techniques in enhancing QAS per-
formance. Moreover, the reliance on supervised learning methods hinders QAS
performance, and the development of unsupervised QAS using advanced ma-
chine learning techniques is encouraged. This review provides valuable insights
for developing effective Arabic QAS, aligning with the Saudi Arabian govern-
ment’s push for automation and improved services.
Despite the numerous studies conducted in the past decade on Quran and
Hadith texts, a significant research gap remains in the availability of a compre-
hensive dataset that can effectively harness the power of available pre-trained
models for non-factoid [11] question-answering. Furthermore, there is a notable
absence of an established evaluation protocol specifically designed for assess-
ing the performance of such sensitive systems. These gaps highlight the need
for further research and development in this area to address the challenges of
dataset scarcity and the lack of standardized evaluation methods for Quran and
Hadith QA systems.
In summary, this literature review navigates the landscape of LFQA in Nat-
ural Language Processing, scrutinizing pivotal datasets like ELI5, MS MARCO,
and NQ. Evaluating their strengths and limitations, the review showcases their
role in advancing machine learning models for intricate QA tasks.
It high-
lights recent strides driven by LLMs and transformers, unveiling methodologies
enhancing LFQA model performance. Additionally, the review sheds light on
challenges faced in extracting reliable answers from religious scriptures like the
Quran and Ahadith, emphasizing the scarcity of comprehensive datasets and
evaluation methods in this domain.
The identified gaps urge further explo-
ration and the need for robust datasets and standardized evaluation methods
in Quran and Hadith QA systems to propel specialized research in this field.
3. Task Description and Dataset
This section provides a comprehensive overview of the data sources and pro-
cessing procedures employed in this study.
The dataset was compiled from
multiple reputable sources to ensure diversity and authenticity. Firstly, we col-
lected question-answer pairs from Islamqa.org6, a prominent online Question-
Answering platform that hosts an extensive collection of over 90,000 question-
answer pairs. This platform allows users to pose questions, which are then an-
swered by Muslim scholars based on Islamic Law, providing a valuable resource
for understanding Islamic perspectives.
In addition to the question-answer pairs, we obtained the English translation
of the Tafsir of the Holy Quran from Al-Tafsir.com7, a trusted online resource
6Available at https://islamqa.org/, Last Visited: 14 June 2023.
7Tanwir al-Miqbas min Tafsir Ibn Abbas, available at: https://www.altafsir.com/Books/
9

--- Page 10 ---

that offers detailed explanations and interpretations of the Quranic text. This
Tafsir provides a deeper understanding of the Quran’s meaning and context,
which is essential for developing a comprehensive Islamic Question-Answering
system.
Furthermore, we acquired English translations of over 33,000 Aha-
dith from the six major Hadith books known as Sahah-e-Sittah8, which are
considered the most authentic and reliable sources of Hadith in the Muslim
Community. Relying on Sahah-e-Sittah in our study upholds dataset quality
and adheres to esteemed sources, ensuring the development of a robust and
accurate Islamic Question-Answering system.
The collected data, comprising question-answer pairs, Tafsir, and Ahadith
translations, underwent rigorous processing to prepare it for utilization in sequence-
to-sequence pre-trained models. These models were then fine-tuned and eval-
uated for their performance, as detailed in the subsequent sections. The pro-
cessing steps involved data cleaning, tokenization, and formatting to ensure
compatibility with the pre-trained models. The resulting dataset is a compre-
hensive and diverse collection of Islamic texts, providing a solid foundation for
developing an effective Islamic Question-Answering system.
3.1. Data Preprocessing
Data preprocessing is a crucial step in preparing the collected data for use
in sequence-to-sequence pre-trained models. After collecting the raw data, we
cleaned it to eliminate any duplicate entries and missing data.
We also re-
moved the Arabic counterparts of answers provided in both English and Arabic
languages.
To reduce the search space from the complete text of Quranic Tafsir and
Ahadith, we employed Latent Dirichlet Allocation (LDA) [45, 49] topic mod-
eling. LDA is a probabilistic model that recognizes topics within a document
collection by assuming that each document comprises a blend of various top-
ics, where each topic represents a distribution of words. By applying LDA, we
aimed to identify the underlying topics in the dataset and group similar docu-
ments together, thereby reducing the search space and making the system more
efficient [41]. This approach enables the model to focus on a subset of relevant
texts, rather than the entire corpus when generating answers.
We divided the corpus into eight topics, namely Prayer, Fasting, Hajj, Ha-
dith, Daily Life, Marriage, Family, and Finance, using LDA. Table 1 presents the
top words from each topic with an assigned label. By categorizing the dataset
into these topics, we significantly reduced the search space, allowing the model
to quickly identify relevant texts and generate accurate answers.
To ensure the accuracy of the assigned topic labels, we had three language
experts evaluate the assigned topic label for each question from the subset of the
IbnAbbas.pdf
8More information available at:
https://en.wikipedia.org/wiki/Kutub_al-Sitta and
https://islamhashtag.com/the-six-sitta-al-sihah-\al-sittah-the-authentic-books-on-hadeeth/
10

--- Page 11 ---

Table 1: Topics with their Top Keywords
Topic Top Keywords
Label
1
Prayer, Pray, Read, Recite, Imam, Salaah, Mosque,
Perform, Answer, Salah
Prayer
2
Fast, Muslim, Allah, People, Person, Month, Good,
Feel, Think, Mean
Fasting
3
Hajj, Day, Perform, Umrah, Travel, Babi, Go,
Name, Makkah, Rule
Hajj
4
Hadith, Prophet, Hair, Bless, Preach, Aalayhi, Nar-
rate, S.A.W, Authentic, Follow
Hadith
5
Wear, Water, Cloth, Wash, Ghusal, Rule, Hand,
Food, Muslim, Allow
Daily
Life
6
Wife, Husband, Marry, Family, Year, Mother, Di-
vorce, Marriage, Parent, Live
Marriage
7
Father, Child, Wealth, Belong, Children, Son, Need,
S.A.W, Alaihi, Salam
Family
8
Money, Work, Company, Bank, Year, sell, Pay,
Give, Month, House
Finance
complete dataset. The evaluators were crowd workers with expertise in Islamic
studies and language. They assessed the relevance of the assigned topic labels
and provided feedback on the accuracy of the labels. The detailed results of
this evaluation are presented in Table 2, which shows the relative percentage of
questions from the total dataset evaluated by the evaluators and the accuracy of
the assigned labels. If a label was deemed incorrect by annotators, they assigned
the appropriate label from the eight defined categories, and the decision was
taken with a majority vote.
Table 2: Results of Evaluation of the Extracted Topics
Topic
Correct/ Evaluated
Accuracy
Total Questions
Percentage of Total
from that Topic
Questions that were
Evaluated
Finance
365/425
85.88%
10,203
4%
Prayer
341/529
64.4%
14,883
3%
Hajj
32/88
36.3%
3,104
2%
Family
73/385
18.9%
9,944
3%
Hadith
124/162
76.5%
7,722
2%
Marriage
360/506
71.1%
14,983
3%
Fasting
1/4
25%
3,291
0.1%
Daily Life
320/364
87.9%
12,983
3%
Total
1616/2463
64.6%
77113
20.1%
By using LDA and evaluating the assigned topic labels, we ensured that the
11

--- Page 12 ---

dataset was well-organized, relevant, and ready for use in training sequence-to-
sequence pre-trained models to generate accurate and informative answers to
user queries. The reduced search space and accurate topic labels enabled the
model to efficiently derive answers by focusing on a subset of pertinent text
rather than the entire corpus of Ahadith and Tafsir.
When presented with a question, a Muslim scholar typically begins by refer-
ring to the Quran and Ahadith to seek the answer. We focused on the Quran
and Ahadith texts and drew context from these to feed our seq-to-seq language
models. Ahadith and Ayahs that were categorized in the same topic as a ques-
tion were stored as context for that question-answer pair. However, the resulting
context was too large to process, so we picked the top three Ayahs and top three
Ahadith based on soft cosine similarity [33].
As a result of this process, the dataset was organized into three distinct
columns: Question (representing user queries), Answer (responses from Muslim
scholars), and Context (comprising excerpts from Quranic Tafsir and Ahadith
that had the same topic as the question). The incorporation of context allowed
the model to efficiently derive answers by focusing on a subset of pertinent
text rather than the entire corpus of Ahadith and Tafsir. An example from
the dataset is provided below, demonstrating how the context column provides
relevant information from the Quran and Ahadith to support the answer. By
preprocessing the data in this manner, we ensured that the dataset was well-
organized, relevant, and ready for use in training sequence-to-sequence pre-
trained models to generate accurate and informative answers to user queries.
More examples of this data are available in the appendix Appendix B for
reference.
4. Models and Experimental Design
To establish baseline results for the language models on this dataset, we per-
formed fine-tuning on several transformer-based pre-trained models, including
T5, BART, LED, and LongT5. The input format for the models is shown in
appendix Appendix
B, and the hyperparameters and specifications for each
model are listed in 3.
4.1. Experimental Setup
The experiments were conducted using an NVIDIA GeForce GTX 1080 Ti
with 12 GB RAM. Due to RAM limitations, the input sequence length and batch
size were adjusted accordingly.
We observed that not all models performed
equally well with the same learning rate. For instance, fine-tuning BART-large
with a learning rate of 0.001 (which performed well for T5) resulted in poor
performance, significantly worse than any other model used in this study. This
contrasts with literature suggesting that BART performs well on language gen-
eration and QA tasks, as it was released alongside ELI5 as a state-of-the-art
model [25]. To address these limitations, we used the base versions of the mod-
els due to limited RAM space. The hyperparameter settings for each experiment
12

--- Page 13 ---

Question: 
I have a question regarding wudu. I work in an office where the only place to perform wudu is the toilet area.
Is it permissible to make wudu in the toilet area in this situation? Also, is it permissible to wipe over my shoes
instead of removing my socks and shoes to wash my feet? It is a toilet and although it is kept very clean and
tidy, Ive been wiping my shoes as a precautionary measure because I dont want to step onto a naapaak area.
Please advise me. Shukran?
Context: 
Narrated Aws ibn AbuAws ath-Thaqafi:The Messenger of Allah () performed ablution and wiped over his
shoes and feet. Abbad (a sub-narrator) said: The Messenger of Allah () came to the well of a people. Musaddad
did not mention the words Midat (a place where ablution is performed), and Kazamah (well). Then both agreed
on the wording:"He performed ablution and wiped over his shoes and feet."<D>Narrated `Isa bin
Tahman:Anas brought out to us two worn out leather shoes without hair and with pieces of leather straps. Later
on Thabit Al-Banani told me that Anas said that they were the shoes of the Prophet.<D>Al-Mughirah bin
Shubah narrated:"The Prophet performed Wudu and wiped over is socks and sandals."<D>(It is not for the
townsfolk of al-Medina) it is not permissible for the folk of Medina (and for those around them of the
wandering Arabs) from Muzaynah, Juhaynah and Aslam (to stay behind the Messenger of Allah) when there is
a military expedition (and prefer their lives to his life) and it is not permissible that theyshould feel more
compassionate towards themselves than they are towards the Prophet; it is also said that this means: they
should not refrain from accompanying the Prophet (pbuh) in jihad. (That) accompaniment (is because neither
thirst) when going or returning (nor toil nor hunger afflicteth them in the way of Allah) in jihad, (nor step they
any step) nor do they go past any territory they conquer (that angereth the disbelievers, nor gain they from the
enemy a gain) by killing or defeating them, (but a good deed is recorded for them therefore) the reward of a
good deed is recorded for them in jihad. (Allah loseth not) thwarts not (the wages of the good) the reward of
the believers in jihad.[...]
Answer: Wa alaika as salam A place is considered clean unless there is visible uncleanliness. Therefore you
may make wudhu at the place mentioned in your question. It is not allowed to wipe over shoes unless they
cover the ankles as in boots. And only Allah Almighty knows best.
Figure 1: Dataset Example
are listed in Table 3. We used a batch size of 4 for T5 and LongT5, and 2 for
BART and LED, with input sequence lengths adjusted accordingly to fit within
the 12 GB RAM constraints.
4.2. Model Architecture
The transformer-based pre-trained models used in this study are: T5: a text-
to-text transformer model that generates output text based on input text [37].
BART: a denoising autoencoder that uses a transformer encoder and decoder
to reconstruct input text [25] LED: a long-range dependence transformer model
designed for long-form text generation [9] LongT5: a variant of T5 designed
for long-form text generation [16] These models were chosen for their ability
to handle long-range dependencies and generate coherent text, making them
suitable for the non-factoid question-answering task.
4.3. Hardware Details
The experiments were conducted on an NVIDIA GeForce GTX 1080 Ti with
12 GB RAM, which provided sufficient computational resources for fine-tuning
the pre-trained models. The GPU architecture allowed for parallel processing
13

--- Page 14 ---

of the input sequences, enabling efficient training and evaluation of the mod-
els.
By using these transformer-based pre-trained models and adjusting the
hyperparameters and input sequence lengths to accommodate the RAM limi-
tations, we established baseline results for the language models on this dataset
and explored the effectiveness of fine-tuning for non-factoid question-answering
tasks.
Table 3: Experimental Settings for Different Models
Model
Input
Length
Output
Length
learning
rate
Batch
Size
t5-base
512
512
0.001
6
facebook/bart-
base-cnn
1024
512
2e-5
4
allenai/led-base-
16384
4096
512
2e-5
3
google/long-t5-
tglobal-base
4096
512
1e-3
1
4.4. Evaluation Metric
The evaluation of results was carried out using two complementary metrics:
ROUGE [26] and BERTScore [47]. These metrics were chosen for their ability
to assess the quality and similarity of generated text, and their suitability for
evaluating non-factoid question-answering tasks.
4.4.1. ROUGE
ROUGE (Recall-Oriented Understudy for Gisting Evaluation) is a widely
used metric for evaluating text generation tasks, including machine translation,
summarization, and question-answering [26]. It measures text similarity using
N-gram overlap, which calculates the number of overlapping words or phrases
between the generated text and the reference text. ROUGE is adaptable to
various language generation tasks and has been used in numerous studies (Gao
et al., 2019; Lewis et al., 2019). We used ROUGE as our evaluation metric to
maintain consistency with previous work in the field.
4.4.2. BERTScore
BERTScore, on the other hand, is a more recent metric that has been shown
to outperform other commonly used metrics such as BLEU and ROUGE on
several benchmark datasets [47]. It is based on the BERT (Bidirectional En-
coder Representations from Transformers) model, a pre-trained neural network
that can be fine-tuned for various natural language processing tasks (Devlin
et al., 2018). BERTScore computes a similarity score between the generated
text and the reference text by comparing their BERT embeddings, which are
high-dimensional vectors that represent the meaning of the text. The score is
14

--- Page 15 ---

computed at the word, sentence, and document levels, and takes into account
both precision and recall [41, 14].
The use of BERTScore is motivated by its ability to capture the seman-
tic meaning of text, rather than just relying on surface-level similarity. This
is particularly important for non-factoid question-answering tasks, where the
generated text needs to convey the correct meaning and context.
By using
both ROUGE and BERTScore, we can evaluate the quality of the generated
text from different perspectives and gain a more comprehensive understanding
of its strengths and weaknesses. The next section presents and discusses the
results in detail, highlighting important future work and potential avenues for
improvement.
5. Results and Discussion
The fine-tuning of language models on the dataset resulted in improved
performance, as evident by the evaluation using ROUGE in Table 4. It lists
the ROUGE difference before and after finetuning the models.
Before fine-
tuning, the baseline ROUGE scores for all models were relatively low, ranging
from 13.5 to 19.25. However, after the fine-tuning, significant enhancements
were observed across all models, with ROUGE scores ranging from 24.70 to
27.23. This indicates that the models generated more accurate and relevant
text, capturing the underlying concepts present in the dataset.
Table 4: Results of Different Models before and after Finetuning
Before Finetuning
After Finetuning
Model
Rouge1
Rouge2
RougeL
Rouge1
Rouge2
RougeL
BERTScore
T5
13.87
1.81
9.76
26.85
7.33
17.84
78.05
BART
19.25
2.36
11.92
24.42
5.82
14.52
79.19
LED
13.5
2.14
7.96
27.23
7.55
18.13
78.95
LongT5
18.35
1.59
10.19
24.89
6.64
17.19
80.65
The findings demonstrate the effectiveness of fine-tuning transformer-based
language models for the question-answering task using the Quran, Ahadith,
and Tafsir datasets. These results provide valuable insights into the potential
of using these language models for enhancing QA systems related to Islamic
literature. However, we made some interesting observations by conducting a
manual analysis of some generated answers which are as follows:
In some answers, the high ROUGE score was not a good indicator of the
correct answer, e.g. a question where the user is trying to know if something
is permissible or not according to the Islamic Shariah, the ROUGE score could
be higher regardless of the generated answer to be correct or not. The answer
could be the opposite of the ground truth, factually, but still would have a
higher score.
The generated answer was not always a reflection of the context from which
the model generated the answer. This suggests that the model also relied on
15

--- Page 16 ---

the pre-consumed knowledge on which it was initially trained. However, it can
be further verified by conducting a specific study. Furthermore, ROUGE is a
recall-oriented matrix. Whereas in this particular domain, achieving the best
results requires a balance between both recall and precision. So that it does
not miss some important facts (focusing on Recall) and also doesn’t infer wrong
conclusions (focusing on precision) from those facts.
5.1. Human Evaluation
The human evaluation of the QA system for the Quran and Ahadith was con-
ducted based on two crucial parameters: Verdict Consistency and Contextual
Understanding. A team of expert evaluators, comprising Islamic scholars and
language experts, assessed the system’s performance in providing accurate and
consistent verdicts and its ability to comprehend the context of the questions.
5.1.1. Verdict Consistency
The assessment focused on determining whether the verdict provided by the
scholar and the model coincided. Results showcased a significant discrepancy,
with the range of consistency falling notably lower, ranging between 11% to
20% (Table 5). This suggests that the agreement between the model’s verdict
and the scholar’s verdict was substantially inconsistent across evaluations. The
highest consistency was achieved by the LED model (22%), while the LongT5
model showed the lowest consistency (11%).
5.1.2. Contextual Understanding
Another key parameter was the system’s ability to comprehend the context
of the question and deliver the relevant answer.
In this aspect, the results
demonstrated a comparatively broader range, spanning between 50% to 90% for
four models (Table 5). This indicates that the models’ capability to grasp the
context varied significantly, with some models showing promising understanding
while others fell short. The LED model achieved the highest score (90%), while
the LongT5 model showed the lowest score (53%).
Table 5: Results of Human Evaluations
Model
Verdict Consistency
Contextual Understanding
T5
0.22
0.78
BART
0.20
0.86
LongT5
0.11
0.53
LED
0.22
0.90
5.1.3. Discussion
The evaluation reveals a substantial disparity between the two parameters.
While the system exhibited a wider range of context understanding, its con-
sistency in providing verdicts aligned with the scholars remained notably low.
This underscores the need for further improvements, particularly in refining the
16

--- Page 17 ---

model’s ability to produce more consistent and accurate verdicts in alignment
with expert scholars while maintaining a consistently high level of contextual
understanding. The human evaluation results highlight the challenges of de-
veloping a QA system for non-factoid questions in the domain of Quran and
Ahadith. The system’s ability to comprehend the context of the question and
provide accurate verdicts is crucial for its reliability and trustworthiness. Future
work should focus on addressing the inconsistencies in verdict consistency and
further enhancing the system’s context understanding capabilities.
While ROUGE and BERTScore are widely used metrics for evaluating text
generation tasks, they may not directly measure verdict consistency between the
model and scholars. This is because they primarily assess the similarity of gen-
erated text to reference text, rather than evaluating the accuracy or consistency
of the verdicts themselves. However, lower scores on these metrics might indi-
cate divergence in the veracity of answers provided by the model compared to
the scholars’ answers. The low ROUGE score, in particular, weakly implies that
the model’s generated answers significantly differed from the reference scholar’s
answers, aligning with the observed low consistency between model and scholar
verdicts. This suggests that the model’s generated answers may not have accu-
rately captured the nuances and complexities of the scholars’ answers, leading
to inconsistencies in verdict consistency.
On the other hand, ROUGE and BERTScore can indirectly reflect the
model’s ability to understand the context by measuring the semantic similar-
ity between the generated answers and reference texts. The higher BERTScore
metric suggests that the models captured and expressed the context well, con-
sistent with the broader range (50% to 90%) of context understanding observed
in the human evaluation. This indicates that the models were able to grasp the
context of the questions to some extent, but may have struggled to generate
answers that accurately reflected the scholars’ verdicts.
Overall, while ROUGE and BERTScore provide valuable insights into the
model’s performance, they should be used in conjunction with human evalua-
tion to get a more comprehensive understanding of the model’s strengths and
weaknesses. By combining these metrics with human evaluation, we can gain a
better understanding of the model’s ability to generate accurate and consistent
verdicts, as well as its ability to understand the context of the questions.
6. Conclusion and Future Work
In conclusion, this paper has introduced a comprehensive dataset tailored
for non-factoid question-answering specifically focused on Quranic Tafsir and
Ahadith.
The dataset, comprising over 73,000 question-answer pairs, is en-
riched with substantial contextual information, providing a robust foundation
for research and development in this domain. The exploration conducted herein
demonstrates the potential of harnessing advanced natural language processing
and machine learning techniques to construct QA systems within the realm of
Islamic literature. However, the limitations of solely relying on automatic eval-
17

--- Page 18 ---

uation metrics became apparent, highlighting the need for a nuanced evaluation
approach that incorporates human assessment and expert feedback.
The dataset’s breadth and depth facilitate the application of various tech-
niques, enabling models to navigate the intricate layers of religious texts. Nev-
ertheless, the identified discrepancies between model-generated responses and
expert opinions necessitate a deeper understanding and refinement of these sys-
tems to ensure their alignment with scholarly interpretations and contextual
fidelity.
Therefore, our focus lies in refining and augmenting the evaluation
strategies, integrating expert assessments, user feedback, and meticulous anal-
yses of contextual accuracy.
However, while initial automatic evaluations using ROUGE scores provided
an initial assessment, our subsequent human evaluation yielded critical insights.
The discrepancy between automatic evaluation metrics and human assessment
became apparent. The human evaluation uncovered significant disparities: the
model’s verdict consistency with expert scholars ranged between 11% to 20%,
while its contextual understanding spanned a broader spectrum of 50% to 90%.
This disparity elucidates the limitations of solely relying on ROUGE scores,
underscoring the necessity for a nuanced evaluation approach.
It became evident that automatic evaluation metrics, while useful, fail to
encapsulate the complexities and accuracy required in understanding religious
texts. Manual analysis highlighted the imperative need for further investiga-
tions into the correctness and contextual alignment of the answers generated by
these systems. The identified discrepancies between model-generated responses
and expert opinions necessitate a deeper understanding and refinement of these
systems to ensure their alignment with scholarly interpretations and contextual
fidelity.
Future work should address the limitations of this study, including the incor-
poration of multiple books for Quranic Tafsir to provide a more comprehensive
understanding of the context. Additionally, human expert evaluation should
be included to compare and determine which automatic evaluation measure is
more correlated and aligned with human assessment. This will enable the devel-
opment of more sophisticated models and techniques tailored to the intricacies
of the Quran, Tafsir, and Ahadith.
Furthermore, future research should explore the following avenues:
• Investigating the application of advanced NLP techniques, such as trans-
fer learning and multi-task learning, to enhance the performance of QA
systems in this domain.
• Developing more nuanced evaluation metrics that can accurately capture
the complexities and accuracy required in understanding religious texts.
• Exploring the use of additional resources, such as Islamic scholarly articles
and books, to further enrich the dataset and improve the performance of
QA systems.
• Investigating the potential applications of QA systems in Islamic litera-
ture, such as assisting scholars and researchers in their work, providing
18

--- Page 19 ---

educational resources for students, and enhancing the accessibility of Is-
lamic knowledge.
By addressing these limitations and exploring these avenues, we can further
advance research in non-factoid question-answering and promote the develop-
ment of more sophisticated models and techniques tailored to the intricacies of
the Quran, Tafsir, and Ahadith. This will ultimately contribute to the advance-
ment of QA systems in the domain of Islamic literature and provide researchers
and practitioners with a valuable resource to explore and understand the Quran,
Tafsir, and Ahadith more efficiently and accurately.
Author Contributions
Acknowledgements
The authors would like to thank the CPInS Research Lab at SEECS-NUST
and Prince Sultan University for facilitating the research and publication of
this work. The authors also recognize their invaluable support and resources for
these efforts.
References
[1] Heba Abdelnasser, Maha Ragab, Reham Mohamed, Alaa Mohamed, Bas-
sant Farouk, Nagwa M El-Makky, and Marwan Torki. 2014. Al-Bayan: an
Arabic question answering system for the Holy Quran. In Proceedings of the
EMNLP 2014 Workshop on Arabic Natural Language Processing (ANLP).
57–64.
[2] Alyssa Ayelet Aharon. 2022. Deep Torah Learning: A Deep Learning Ap-
proach to Identifying Anomalous Letters in Torah Scrolls. Ph. D. Disserta-
tion. Yeshiva University.
[3] Basem Ahmed, Motaz Saad, and Eshrag A Refaee. 2022. QQATeam at
Qur’an QA 2022: Fine-Tunning Arabic QA Models for Qur’an QA Task.
In Proceedinsg of the 5th Workshop on Open-Source Arabic Corpora and
Processing Tools with Shared Tasks on Qur’an QA and Fine-Grained Hate
Speech Detection. 130–135.
[4] Yazeed Alkhurayyif and Abdul Rahaman Wahab Sait. 2023. A compre-
hensive survey of techniques for developing an Arabic question answering
system. PeerJ Computer Science 9 (2023), e1413.
[5] Reinald Kim Amplayo, Kellie Webster, Michael Collins, Dipanjan Das, and
Shashi Narayan. 2022. Query Refinement Prompts for Closed-Book Long-
Form Question Answering. arXiv preprint arXiv:2210.17525 (2022).
19

--- Page 20 ---

[6] Negar Arabzadeh, Bhaskar Mitra, and Ebrahim Bagheri. 2021. Ms marco
chameleons: challenging the ms marco leaderboard with extremely obsti-
nate queries. In Proceedings of the 30th ACM International Conference on
Information & Knowledge Management. 4426–4435.
[7] Payal Bajaj, Daniel Campos, Nick Craswell, Li Deng, Jianfeng Gao, Xi-
aodong Liu, Rangan Majumder, Andrew McNamara, Bhaskar Mitra, Tri
Nguyen, et al. 2016. Ms marco: A human generated machine reading com-
prehension dataset. arXiv preprint arXiv:1611.09268 (2016).
[8] Muhammad Huzaifa Bashir, Aqil M Azmi, Haq Nawaz, Wajdi Zaghouani,
Mona Diab, Ala Al-Fuqaha, and Junaid Qadir. 2023. Arabic natural lan-
guage processing for Qur’anic research: A systematic review.
Artificial
Intelligence Review 56, 7 (2023), 6801–6854.
[9] Iz Beltagy, Matthew E Peters, and Arman Cohan. 2020. Longformer: The
long-document transformer. arXiv preprint arXiv:2004.05150 (2020).
[10] Meghana Moorthy Bhat, Rui Meng, Ye Liu, Yingbo Zhou, and Semih
Yavuz. 2023. Investigating Answerability of LLMs for Long-Form Ques-
tion Answering. arXiv preprint arXiv:2309.08210 (2023).
[11] Eduardo Gabriel Cortes, Vinicius Woloszyn, Dante Barone, Sebastian
M¨oller, and Renata Vieira. 2022. A systematic review of question answer-
ing systems for non-factoid questions. Journal of Intelligent Information
Systems (2022), 1–28.
[12] Dipanjan Das, Kellie Webster, Michael Collins, Reinald Kim Amplayo, and
Shashi Narayan. 2022. Query Refinement Prompts for Closed-Book Long-
Form Question Answering. (2022).
[13] Aprameya Dash, Mohit Awachar, Anshul Patel, and Bhawana Rudra. 2023.
Open-Domain Long-Form Question–Answering Using Transformer-Based
Pipeline. SN Computer Science 4, 5 (2023), 595.
[14] Markus Eberts and Adrian Ulges. 2019. Span-based joint entity and relation
extraction with transformer pre-training. arXiv preprint arXiv:1909.07755
(2019).
[15] Angela Fan, Yacine Jernite, Ethan Perez, David Grangier, Jason Weston,
and Michael Auli. 2019.
ELI5: Long form question answering.
arXiv
preprint arXiv:1907.09190 (2019).
[16] Mandy Guo, Joshua Ainslie, David Uthus, Santiago Ontanon, Jianmo Ni,
Yun-Hsuan Sung, and Yinfei Yang. 2021. LongT5: Efficient text-to-text
transformer for long sequences. arXiv preprint arXiv:2112.07916 (2021).
[17] Aimad Hakkoum and Said Raghay. 2016. Semantic Q&A System on the
Qur’an. Arabian Journal for Science and Engineering 41, 12 (2016), 5205–
5214.
20

--- Page 21 ---

[18] Suhaib Kh. Hamed and Mohd Juzaiddin Ab Aziz. 2016. A Question An-
swering System on Holy Quran Translation Based on Question Expansion
Technique and Neural Network Classification. J. Comput. Sci. 12 (2016),
169–177.
[19] Andreas Handojo, Erwin Lie, and Rolly Intan. 2011. APLIKASI QUES-
TION ANSWERING SYSTEM DENGAN METODE RULE-BASED
QUESTION ANSWERING SYSTEM PADA ALKITAB.
[20] Zhifeng Hao, Junhao Chen, Wen Wen, Biao Wu, and Ruichu Cai. 2022.
Motif-based memory networks for complex-factoid question answering.
Neurocomputing 485 (2022), 12–21.
[21] Harold G Koenig and Saad Al Shohaib. 2014. Health and well-being in
Islamic societies. Springer.
[22] Kalpesh Krishna, Aurko Roy, and Mohit Iyyer. 2021. Hurdles to progress
in long-form question answering. arXiv preprint arXiv:2103.06332 (2021).
[23] Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, Michael Collins,
Ankur Parikh, Chris Alberti, Danielle Epstein, Illia Polosukhin, Jacob De-
vlin, Kenton Lee, et al. 2019. Natural questions: a benchmark for question
answering research.
Transactions of the Association for Computational
Linguistics 7 (2019), 453–466.
[24] Carlos Lassance and St´ephane Clinchant. 2023.
The tale of two MS
MARCO–and their unfair comparisons. arXiv preprint arXiv:2304.12904
(2023).
[25] Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdel-
rahman Mohamed, Omer Levy, Ves Stoyanov, and Luke Zettlemoyer.
2019.
Bart:
Denoising sequence-to-sequence pre-training for natural
language generation, translation, and comprehension.
arXiv preprint
arXiv:1910.13461 (2019).
[26] Chin-Yew Lin. 2004. Rouge: A package for automatic evaluation of sum-
maries. In Text summarization branches out. 74–81.
[27] Antoine Louis, Gijs van Dijck, and Gerasimos Spanakis. 2023. Interpretable
Long-Form Legal Question Answering with Retrieval-Augmented Large
Language Models. arXiv preprint arXiv:2309.17050 (2023).
[28] Rana Malhas, Watheq Mansour, and Tamer Elsayed. 2022. Qur’an QA
2022: Overview of the first shared task on question answering over the
holy qur’an. In Proceedinsg of the 5th Workshop on Open-Source Arabic
Corpora and Processing Tools with Shared Tasks on Qur’an QA and Fine-
Grained Hate Speech Detection. 79–87.
21

--- Page 22 ---

[29] Hajer Maraoui, Kais Haddar, and Laurent Romary. 2021. Arabic factoid
Question-Answering system for Islamic sciences using normalized corpora.
Procedia Computer Science 192 (2021), 69–79.
https://doi.org/10.
1016/j.procs.2021.08.008 Knowledge-Based and Intelligent Information
& Engineering Systems: Proceedings of the 25th International Conference
KES2021.
[30] Hajer Maraoui, Kais Haddar, and Laurent Romary. 2022. Development
of a normalized hadith narrator encyclopedia with TEI. Computaci˝on y
Sistemas 26, 3 (2022), 1283–1292.
[31] Ensaf Hussein Mohamed and Eyad Mohamed Shokry. 2022.
QSST: A
Quranic Semantic Search Tool based on word embedding. Journal of King
Saud University-Computer and Information Sciences 34, 3 (2022), 934–
945.
[32] Ali Mostafa and Omar Mohamed. 2022. Gof at qur’an qa 2022: Towards
an efficient question answering for the holy qu’ran in the arabic language
using deep learning-based approach. In Proceedinsg of the 5th Workshop
on Open-Source Arabic Corpora and Processing Tools with Shared Tasks
on Qur’an QA and Fine-Grained Hate Speech Detection. 104–111.
[33] V´ıt Novotn`y. 2018. Implementation notes for the soft cosine measure. In
Proceedings of the 27th ACM International Conference on Information and
Knowledge Management. 1639–1642.
[34] Aarthi Paramasivam and S Jaya Nirmala. 2022. A survey on textual entail-
ment based question answering. Journal of King Saud University-Computer
and Information Sciences 34, 10 (2022), 9644–9653.
[35] Syopiansyah Jaya Putra, Ria Hari Gusmita, Khodijah Hulliyah, and
Husni Teja Sukmana. 2016. A semantic-based question answering system
for Indonesian translation of quran. In Proceedings of the 18th Interna-
tional Conference on Information Integration and Web-based Applications
and Services. 504–507.
[36] Yujia Qin, Zihan Cai, Dian Jin, Lan Yan, Shihao Liang, Kunlun Zhu,
Yankai Lin, Xu Han, Ning Ding, Huadong Wang, et al. 2023. WebCPM:
Interactive Web Search for Chinese Long-form Question Answering. arXiv
preprint arXiv:2305.06849 (2023).
[37] Adam Roberts, Colin Raffel, Katherine Lee, Michael Matena, Noam
Shazeer, Peter J Liu, Sharan Narang, Wei Li, and Yanqi Zhou. 2019. Ex-
ploring the limits of transfer learning with a unified text-to-text trans-
former. Google, Tech. Rep. (2019).
[38] Jawad Sadek and Farid Meziane. 2016. A discourse-based approach for
Arabic question answering. ACM Transactions on Asian and Low-Resource
Language Information Processing (TALLIP) 16, 2 (2016), 1–18.
22

--- Page 23 ---

[39] H Shmeisani, S Tartir, A Al-Na’ssaan, and M Naji. 2014. Semantically
answering questions from the Holy Quran. In International Conference on
Islamic Applications in Computer Science And Technology. 1–8.
[40] Dan Su, Xiaoguang Li, Jindi Zhang, Lifeng Shang, Xin Jiang, Qun Liu,
and Pascale Fung. 2022. Read before generate! faithful long form question
answering with machine reading. arXiv preprint arXiv:2203.00343 (2022).
[41] Sophie Trastour, Maxime Genin, and Arthur Morlot. 2016.
Prediction
of the crude oil price thanks to natural language processing applied to
newspapers.
[42] FS Utomo, N Suryana, and MS Azmi. 2020. Question Answering Systems
on Holy Quran: A Review of Existing Frameworks, Approaches, Algorithms
and Research Issues. In Journal of Physics: Conference Series, Vol. 1501.
IOP Publishing, 012022.
[43] Shufan Wang, Fangyuan Xu, Laure Thompson, Eunsol Choi, and Mohit
Iyyer. 2022. Modeling exemplification in long-form question answering via
retrieval. arXiv preprint arXiv:2205.09278 (2022).
[44] Kemas Wiharja, Danang Murdiansyah, Muhammad Romdlony, Tiwa
Ramdhani, and Muhammad Gandidi. 2022. A Questions Answering System
on Hadith Knowledge Graph. Journal of ICT Research and Applications
16, 2 (2022), 184–196.
[45] Hua Yu and Jie Yang. 2001. A direct LDA algorithm for high-dimensional
data—with application to face recognition.
Pattern recognition 34, 10
(2001), 2067–2070.
[46] Li Yujian and Liu Bo. 2007.
A normalized Levenshtein distance met-
ric. IEEE transactions on pattern analysis and machine intelligence 29,
6 (2007), 1091–1095.
[47] Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q Weinberger, and Yoav
Artzi. 2019. Bertscore: Evaluating text generation with bert. arXiv preprint
arXiv:1904.09675 (2019).
[48] Yuchen Zhuang, Yue Yu, Kuan Wang, Haotian Sun, and Chao Zhang. 2024.
Toolqa: A dataset for llm question answering with external tools. Advances
in Neural Information Processing Systems 36 (2024).
[49] Zoya, Seemab Latif, Faisal Shafait, and Rabia Latif. 2021. Analyzing LDA
and NMF Topic Models for Urdu Tweets via Automatic Labeling. , 127531-
127547 pages. https://doi.org/10.1109/ACCESS.2021.3112620
23

--- Page 24 ---

Author Biography
FAIZA QAMAR is a Ph.D scholar at the National University of Sciences
and Technology (NUST), Pakistan.
She completed her Bachelor’s and mas-
ter’s in computer science from the University of Gujrat (UOG) and University
of Engineering and Technology (UET), respectively. Her research interests are
Natural Language Processing (NLP), Machine learning, Deep learning, and In-
terdisciplinary research.
SEEMAB LATIF is an associate professor and a researcher at the National
University of Sciences and Technology (NUST), Pakistan. She received her PhD
from the University of Manchester, UK. Her research interests include artificial
intelligence, machine learning, data mining, and NLP. Her professional services
include Industry Consultations, Conference Chair, Technical Program Commit-
tee Member, and reviewer for several international journals and conferences. In
the last 3 years, she has established research collaborations with national and
international universities and institutes. She has also secured grants from the
Asian Development Bank, HEDP, World Bank, Higher Education Commission
Pakistan, National ICT, HEC Technology Development Fund, and UK ILM
Ideas. She received the School Best Teacher award in 2016 and the University
Best Innovator Award in 2020. She is also the founder of NUST spin-off com-
pany, Aawaz AI Tech.
RABIA LATIF is currently working as an Associate Professor at the Col-
lege of Computer and Information Sciences, Prince Sultan University, Riyadh,
Saudi Arabia. She received her bachelor’s degree in Computer Science from
COMSATS Institute of Information Technology, Islamabad, and her master’s
degree in information security from the National University of Sciences and
Technology (NUST), Pakistan. She has done her PhD in cloud-assisted wire-
less body area networks at the National University of Sciences and Technology,
Pakistan.
Her research interests include wireless body area networks, cloud
computing, information security and Artificial Intelligence.
7. Appendices
Appendix A. Answers generated by Finetuned Language Models
The table presents the answers generated by the language models i.e. T5,
BART, LED and LongT5.
Appendix B. Examples from the Dataset with Context
Following are some examples from the dataset. In each example, there are
three entities. a) Question, b) Context extracted from Quranic Tafsir and Aha-
dith, and c) Answer provided by the Muslim Scholars.
24

--- Page 25 ---

25

--- Page 26 ---

26

--- Page 27 ---

27

--- Page 28 ---

28

```
