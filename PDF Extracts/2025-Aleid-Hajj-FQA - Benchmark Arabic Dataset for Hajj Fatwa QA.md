---
title: "2025-Aleid-Hajj-FQA - Benchmark Arabic Dataset for Hajj Fatwa QA - PDF Extract"
source_pdf: "2025-Aleid-Hajj-FQA - Benchmark Arabic Dataset for Hajj Fatwa QA.pdf"
pages: 28
extracted_at: "2026-02-08T06:02:19.941654"
---

# PDF Extract: 2025-Aleid-Hajj-FQA - Benchmark Arabic Dataset for Hajj Fatwa QA

**Source PDF:** 2025-Aleid-Hajj-FQA - Benchmark Arabic Dataset for Hajj Fatwa QA.pdf
**Total Pages:** 28

---

## Content

```
--- Page 1 ---

/ Published online: 25 July 2025
Journal of King Saud University Computer and Information Sciences (2025) 37:135 
https://doi.org/10.1007/s44443-025-00128-w
ORIGINAL PAPER
Hajj-FQA: A benchmark Arabic dataset for developing
question-answering systems on Hajj fatwas
Hayfa A. Aleid1 · Aqil M. Azmi1
Received: 21 February 2025 / Accepted: 20 June 2025
© The Author(s) 2025
Abstract
Deep learning has signiﬁcantly advanced the question-answering (QA) systems across various sectors. However, Arabic-
language systems for Hajj-related fatwas (non-binding Islamic legal opinions issued by muftis) remain underdeveloped. This
paper introduces Hajj-FQA, a benchmark Arabic dataset speciﬁcally designed to develop HajjBot - a specialized chatbot for
fatwas QA during the annual Hajj pilgrimage. The dataset captures the unique linguistic and jurisprudential characteristics
of pilgrims’ inquiries, enabling accurate, domain-speciﬁc responses. We present a comprehensive quantitative analysis of the
dataset’s construction methodology and its distinctive question-answer patterns. Evaluation using multilingual and Arabic-
speciﬁc language models across three tasks - machine reading comprehension (MRC), duplicate question detection (DQD),
and duplicate answer detection (DAD) - with 10-fold cross-validation demonstrates the practical utility of Hajj-FQA. Results
show exceptional performance in classiﬁcation tasks (AraBERTv0.2 achieved a precision score of 99.19% for DQD and
99.26% for DAD) and strong extractive answering capability with an F-score of 72.78%. While generative performance
reached BERT-F score of 71.4% (AraBART), MRC variability highlights challenges in religious reasoning. These ﬁndings
establish Hajj-FQA as both: (1) a critical resource for developing specialized fatwa chatbots like HajjBot, and (2) a benchmark
for Arabic religious QA systems. The dataset directly addresses the urgent need for accurate, automated fatwa assistance
during Hajj, while providing insights for future improvements in Islamic NLP applications.
Keywords Chatbots · Arabic question-answering · Arabic NLP · Dataset · Fatwa · Hajj
1 Introduction
A Question Answering (QA) chatbot is a specialized dia-
logue system designed to automatically return precise and
contextually relevant answers to user queries, often within
a predeﬁned domain. Unlike general conversational agents,
QA chatbots aim to emulate aspects of human informa-
tion retrieval and reasoning by providing accurate, concise
responses. Recent analyses highlight their potential as cost-
effective solutions for automating high-volume, repetitive
information services across sectors. For instance, in aca-
demic institutions, QA chatbots serve as virtual advisors,
offering timely information about registration, academic cal-
endars, and course requirements. In the healthcare domain,
B Aqil M. Azmi
aqil@ksu.edu.sa
Hayfa A. Aleid
haaleid@ksu.edu.sa
1
Department of Computer Science, College of Computer &
Information Sciences, King Saud University, Riyadh 11543,
Saudi Arabia
they function as virtual receptionists, assisting with appoint-
ment scheduling and preliminary patient intake.
Inrecentyears,NaturalLanguageProcessing(NLP)research
has increasingly prioritized the development of robust and
trustworthydialoguesystemscapableofgeneratingcoherent,
factual, and contextually appropriate answers. These systems
integrate a wide array of machine learning approaches—
including deep neural networks and transformer-based archi-
tectures—to process and generate language, typically mod-
eling higher linguistic levels such as syntax, semantics, and
discourse structures relevant to task performance.
Despite signiﬁcant advancements, current QA chatbots
remain susceptible to errors, including the generation of
hallucinated responses, incoherent or contradictory outputs,
and failures in intent recognition. In sensitive domains—
especially those involving religion, law, or healthcare—such
errors may lead to severe consequences. Accordingly, sys-
tems should be explicitly designed to handle epistemic
uncertainty. For example, in the Islamic tradition, honesty
and the avoidance of conjecture without knowledge are
highly emphasized; therefore, it is ethically preferable for
0123456789().: V,-vol 
123

--- Page 2 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
a system to admit uncertainty (e.g., stating “I don’t know” )
rather than provide a potentially misleading answer. How-
ever, many chatbots default to evasive or uninformative
responses, underscoring the persistent challenges in build-
ing reliable NLP systems for critical-use cases.
These challenges are particularly acute in the context of
Arabic, a linguistically complex and resource-scarce lan-
guage. Despite recent advances in generative AI, Arabic QA
systems lag behind their English and Chinese counterparts.
Most existing Arabic chatbots rely on retrieval-based meth-
ods, as many large-scale generative language models (LLMs)
demonstrate lower performance on Arabic input due to lim-
ited high-quality training data (Alsheddi and Alhenaki 2022).
Consequently, there is an urgent need for enriched Arabic
NLP resources, particularly annotated datasets that reﬂect
domain-speciﬁc linguistic nuances and support long-context
comprehension.
To address these limitations—particularly artiﬁcial gen-
eration, restricted size, and topical gaps—we propose a
manually annotated Arabic dataset tailored for Hajj fat-
was. By prioritizing linguistic integrity and domain-speciﬁc
complexity, our framework mitigates pitfalls of prior work.
Moreover, the scarcity of closed-domain Arabic datasets fur-
ther restricts the development of specialized QA systems,
such as those for medical, legal, or religious guidance. Most
available datasets are open-domain and not well-suited to
applications that require rigorous domain knowledge and ter-
minology.
One such application is the Hajj pilgrimage, a mandatory
religious obligation for physically and ﬁnancially capable
Muslims. Every year, millions of pilgrims travel to Makkah,
Saudi Arabia, during the Islamic month of Dhul Hijjah, the
twelfth month of the Islamic lunar calendar, to perform a
series of ritual acts in a speciﬁc sequence. These acts are
governed by detailed legal rulings, and adherence to correct
procedures is critical for the validity of the pilgrimage.1
Given that most pilgrims perform Hajj only once in their
lifetime, they typically lack familiarity with its intricate legal
aspects.Duringthepilgrimage,timeconstraintsandthephys-
ical demands of rituals make it difﬁcult to seek scholarly
guidance. Hence, fatwa services—a non-binding legal opin-
ions issued by qualiﬁed Islamic jurists (muftis)—become
indispensable.2 However, responding to millions of queries
in real time using only human scholars is logistically unfea-
sible.
1 Over the past decade, the number of Hajj pilgrims usually ranged from
2 to 3 million each year. However, due to the COVID-19 pandemic, there
was a signiﬁcant drop. Government records indicate that in 2024, the
total attendance at Hajj was approximately 1.83 million.
2 The Arabic term “fatwa” denotes a formal legal opinion provided by
a recognized scholar in response to a question concerning Islamic law.
We hypothesize that deep learning (DL)-based NLP mod-
els can automate fatwa responses accurately and at scale,
leveraging well-deﬁned, authoritative sources such as the
Standing Committee for Issuing Fatwas’ Hajj Guidebooks
and decrees. This domain’s stable legal content and struc-
tured rulings make it ideal for AI-driven solutions.
To this end, we propose a comprehensive framework for
constructing a high-quality Arabic QA dataset tailored to
the Hajj domain. Our methodology addresses key limitations
in existing resources by emphasizing manual annotation,
topic coverage, and linguistic integrity. The resulting dataset
supports both extractive and generative machine reading
comprehension (MRC) tasks, as well as semantic similarity
detection (e.g., duplicate question identiﬁcation).
We present Hajj-FQA (for Hajj-related Fatwa Question
Answering) as a case study - a novel closed-domain dataset
of expert-annotated Hajj-related fatwas speciﬁcally designed
for developing Hajj chatbot applications. The dataset cap-
tures domain-speciﬁc jurisprudential terminology and com-
plex question formulations to enable accurate QA model
development.Webenchmarkedmultiplestate-of-the-artAra-
bic language models ﬁne-tuned for MRC tasks, employing
standard evaluation metrics including Exact Match (EM) and
F-score to assess performance and identify improvement
opportunities.
We may summarize our contribution as follows,
• Development of a specialized dataset. We constructed
a high-quality, human-annotated dataset speciﬁcally tai-
lored for Hajj-Fatwa question answering, addressing the
gap in resources for Arabic natural language processing.
• Model benchmarking. We provided an extensive bench-
marking of different LLMs on the dataset, showcasing
their capabilities and limitations in understanding and
processing Arabic religious texts.
• Cross-disciplinary methodological framework. The com-
bination of deep learning techniques and traditional
Islamic scholarship in our approach represents a pioneer-
ing effort in the ﬁeld of computational Islamic studies,
paving the way for further interdisciplinary research.
The remainder of this paper is structured as follows. Sec-
tion 2 outlines the classiﬁcation of QA chatbots and the core
technical methodologies that support their development. Sec-
tion 3 surveys recent advancements in Arabic QA systems.
Section 4 details the construction methodology of the pro-
posed Hajj-FQA dataset. Section 5 provides a qualitative
analysis of the dataset’s content and characteristics. In Sec-
tion 6, we present a comprehensive evaluation of the dataset
usingdifferent languagemodels. Finally, Section7concludes
the paper and highlights avenues for future research.
123
 135 
Page 2 of 28

--- Page 3 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
2 Background
2.1 Overview of chatbots, QA, and MRC
Chatbots are intelligent conversational agents designed
to simulate human-like dialogue across various domains.
These systems are typically categorized along three key
dimensions: (1) knowledge domain (open-domain, closed-
domain, or task-speciﬁc), (2) functional purpose (task-
oriented vs. non-task-oriented), and (3) technical implemen-
tation approach. Task-oriented chatbots include question-
answering (QA) systems and personal assistants, while
non-task-oriented variants encompass social bots and infor-
mation gathering systems (Adamopoulou and Moussiades
2020a; Hussain et al. 2019). Within task-oriented systems,
QA chatbots represent a specialized class that typically
employs machine reading comprehension (MRC) techniques
to extract or generate responses from knowledge sources.
Modern chatbot architectures employ diverse response gen-
eration mechanisms spanning rule-based systems, retrieval-
based methods, and generative approaches using machine
learning. Their operational autonomy ranges from human-
supervised to fully autonomous implementations, with mul-
timodal interaction support including text, voice, and visual
interfaces.
2.1.1 QA and MRC
QA and MRC are interconnected NLP subﬁelds with dis-
tinct focuses. MRC speciﬁcally evaluates a model’s capacity
to comprehend passages and answer questions grounded in
that text. QA systems employ broader methodologies, uti-
lizing either structured knowledge bases (like databases and
knowledge graphs) or unstructured documents to retrieve and
generate answers (Zeng et al. 2020).
Modern QA systems often enhance traditional search
engines through different operational approaches. Struc-
tured systems deliver factual responses from curated sources,
while unstructured systems process natural language doc-
uments. Implementation methods vary between retrieval-
based approaches (extracting text spans) and generative
techniques (synthesizing answers) (Almansor and Hussain
2020).
A standard QA pipeline includes several stages (Azmi
and AlShenaiﬁ2014; Azmi and Alshenaiﬁ2016). First,
in the question analysis phase, the input query is parsed
and classiﬁed to identify its intent, expected answer type,
and key entities. This is followed by document or passage
retrieval, where relevant contexts are fetched using sparse
or dense retrieval algorithms. Finally, the answer genera-
tion or extraction phase involves extracting a text span from
the passage (in extractive QA) or producing a free-form
response (in generative QA). Additional techniques, such
as passage ranking, named entity recognition, and answer
veriﬁcation, are often incorporated to improve accuracy and
coherence. Furthermore, both QA and MRC models are fre-
quently integrated into broader conversational AI systems,
such as task-oriented chatbots (Biltawi et al. 2021).
2.1.2 Question semantic similarity
Question Semantic Similarity (QSS) is an NLP task that mea-
sures the similarity between two questions, playing a crucial
role in QA systems by identifying duplicate questions. This
helpsstreamlinetheansweringprocess,conservingresources
and improving system efﬁciency by enabling the retrieval of
existing answers (Fuad and Al-Yahya 2022).
2.2 Underlying and NLP techniques
Early chatbot development relied on handcrafted rules and
string-matching techniques, often implemented using AIML
and Chatscript. These rule-based systems were limited in
scalability and adaptability. Early statistical methods such
as Term Frequency-Inverse Document Frequency (TF-IDF)
provided simple, frequency-based representations, while
Latent Semantic Analysis (LSA) employed matrix factor-
ization to uncover latent relationships between terms and
documents (Adamopoulou and Moussiades 2020b; Trivedi
etal.2019;Landaueretal.1998;Rameshetal.2017).Markov
chains were also used to generate probabilistic responses,
though these approaches often suffered from sparsity and
lack of contextual understanding (Williams and Young 2007;
Li et al. 2024). Ontologies, by contrast, offered structured
semantic frameworks for interpreting user input and dynam-
ically generating responses (Maynard et al. 2008).
A key challenge in NLP has been the effective encoding
of language for neural models. Traditional approaches like
one-hot encoding and bag-of-words generated sparse, high-
dimensional vectors with limited semantic content (Alman-
sor and Hussain 2020; Zhou et al. 2020). The introduction of
word embedding algorithms addressed this issue by produc-
ing dense vector representations. These embeddings fall into
two main categories: context-independent methods, such as
Word2Vec (Mikolov et al. 2013), GloVe (Pennington et al.
2014), and FastText (Bojanowski et al. 2017), which assign
static vectors to words irrespective of context; and context-
aware models, such as ELMo and BERT, which generate
dynamic embeddings based on the surrounding textual con-
text. Contextualized embeddings, often obtained through
large-scale pretraining followed by task-speciﬁc ﬁne-tuning,
have signiﬁcantly improved performance across a wide range
of downstream NLP tasks (Li et al. 2024; Radford et al. 2018;
Peters et al. 2018).
123
Page 3 of 28 
135

--- Page 4 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
2.3 Language models
The ﬁeld of AI, particularly within machine learning (ML),
has witnessed transformative growth with the advent of
LLMs. A milestone in this evolution was the introduction
of the attention mechanism in the Transformer architecture,
which signiﬁcantly improved the scalability and contextual
understanding of language models by allowing them to pro-
cess entire sequences more efﬁciently (Vaswani et al. 2017).
One of the most inﬂuential developments in LLMs has
been the Generative Pre-trained Transformer (GPT) series.
These models are trained in a two-phase process: large-scale
unsupervised pretraining on diverse corpora, followed by
instruction tuning or reinforcement learning from human
feedback to align outputs with human expectations (Radford
et al. 2019). Building on this foundation, OpenAI introduced
specialized variants such as Codex, designed for code gen-
eration, and ChatGPT, optimized for dialogue (Chen et al.
2021; Nakano et al. 2022; OpenAI 2024). The Llama series
extended these capabilities by providing open-access, high-
performance base models trained on expanded datasets with
architectural optimizations, facilitating downstream task-
speciﬁc ﬁne-tuning (Touvron et al. 2023a,b).
Beyond generative models, encoder-only architectures
such as BERT have greatly advanced contextual under-
standing by using bidirectional masked language modeling.
Subsequent models like RoBERTa, ALBERT, and DeBERTa
improved upon BERT’s architecture by reﬁning training
objectives and increasing model efﬁciency (Devlin et al.
2019; Liu et al. 2019; Lan et al. 2020b; He et al. 2021).
Meanwhile, encoder-decoder models like T5 showcase the
ﬂexibility of the Transformer paradigm in handling diverse
text-to-text tasks, using uniﬁed input-output formats (Raffel
et al. 2020).
The most recent trend in the development of LLMs is
the move towards multimodal models capable of processing
diverse data types such as text, images, and audio. Systems
likeGPT-4,Falcon,andGeminiexemplifythistrend,pushing
toward more general and human-like AI by integrating cross-
modal representations (OpenAI et al. 2024; Almazrouei et al.
2023; Team et al. 2024).
The development of Arabic language models has largely
followed these global trends, often adapting existing archi-
tectures through pretraining on Arabic or multilingual cor-
pora. These adaptations aim to capture the rich linguistic
features of Arabic, including its morphological complexity
and dialectal variation. Table 1 presents a detailed compari-
son of key Arabic LLMs across these dimensions.
Arabic LLMs can be broadly categorized by architec-
tural design and training data. Encoder-only models form
the foundation of Arabic NLP, with AraBERT representing a
pioneering effort tailored to Modern Standard Arabic (MSA).
AraELECTRA introduced efﬁciency gains through replaced-
token detection (Antoun et al. 2020), while CAMeLBERT
and MDABERT extended coverage to dialectal and classical
Arabic (Inoue et al. 2021; Talafha et al. 2020). Other notable
models include ArabicBERT and MARBERT, both of which
demonstrate competitive performance across a range of clas-
siﬁcation and sequence-labeling tasks (Abdul-Mageed et al.
2021; Safaya et al. 2020).
For generative tasks, decoder-only models like AraGPT2
initiated progress in Arabic text generation (Antoun et al.
2020). More recent efforts, including Arabian GPT and
AceGPT, address challenges in Arabic dialogue generation
by incorporating morphological and syntactic priors (Koubaa
et al. 2024; Huang et al. 2024). Encoder-decoder models such
as AraT5 provide ﬂexible text-to-text solutions across sum-
marization, translation, and question answering (Nagoudi
et al. 2022). In parallel, multilingual models like mBERT and
XLM-R have been leveraged for Arabic NLP, though their
performance often lags behind monolingual counterparts due
to tokenization and data sparsity issues (Devlin et al. 2019).
Recent contributions such as Jais (Sengupta et al. 2023),
Noor (Noor 2022), Fanar (Kahil 2024), and ALLAM (Bari
et al. 2024) represent the forefront of Arabic LLM devel-
opment. These models are trained on curated, high-quality
Arabic datasets and incorporate optimizations for regional
and domain-speciﬁc applications. Nevertheless, challenges
remain—particularly the lack of standardized evaluation
benchmarks for Arabic dialects and generative tasks, which
impedes direct model comparison and downstream deploy-
ment.
The evolution of Arabic LLMs reﬂects the broader trajec-
tory of global NLP innovation, while also highlighting the
unique demands posed by Arabic’s diglossia, morphological
richness, and underrepresentation in annotated datasets.
2.4 Islamic fatwas
The fatwa is a crucial Islamic resource that provides clar-
ity on religious issues and has been a part of Islam since
its inception. Essentially, it serves to elucidate ambigui-
ties and resolve uncertainties concerning Islamic teachings.
Fatwas are issued by a mufti, a qualiﬁed Islamic scholar,
who interprets and explains Islamic law (Shari’ah) based on
authoritative religious texts. This process ensures that adher-
ents receive grounded and insightful guidance on matters of
faith and practice.
Given the continuous demand for religious guidance, fat-
wasareavailableinarangeofformats—fromtraditionaltexts
and letters to contemporary media such as TV programs and
websites. Typically, a fatwa involves a question posed by an
individual about a religious matter, to which a mufti provides
an answer based on Islamic teachings (Ibrahim et al. 2024).
123
 135 
Page 4 of 28

--- Page 5 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
Table 1 Overview of Arabic Language Models
Name
Architecture
Language
Dataset
Pretraining Corpus
AraBERT v1 and v2 (Antoun et al. 2020)
BERT (base, large)
Arabic
77GB
OSCAR + Arabic Wikipedia + Words Arabic Corpus
+ OSIAN Corpus + Assaﬁr news articles
AraELECTRA (Antoun et al. 2020)
ELECTRA-base
(generator-
discriminator)
Arabic
77GB
OSCAR + Arabic Wikipedia + Words Arabic Corpus
+ OSIAN Corpus + Assaﬁr news articles
AraGPT2 (Antoun et al. 2020)
GPT2 (base,
medium, large)
Arabic
77GB
OSCAR + Arabic Wikipedia + Words Arabic Corpus
+ OSIAN Corpus + Assaﬁr news articles
CAMeLBERT (Inoue et al. 2021)
BERT (MSA,
DA, CA, mix)
Arabic (CA,
MSA, DA)
107GB, 54GB,
6GB, 167GB
Arabic Gigaword + Abu El-Khair Corpus + OSIAN
corpus + Arabic Wikipedia + Arabic OSCAR corpus
+ OpenITI corpus + Many data source for dialectal
Arabic
Multi-dialect-Arabic-BERT (Talafha et al. 2020)
BERT
Arabic (MSA, DA)
Arabic OSCAR corpus + 10M tweets
GigaBERTv4 (Lan et al. 2020b)
BERT
Bilingual
Wikipedia + Gigaword + OSCAR corpus
MARBERT (Abdul-Mageed et al. 2021)
BERT
Arabic (MSA, DA)
128GB
1B Arabic tweets
ARBERT (Abdul-Mageed et al. 2021)
BERT
Arabic
61GB
Books Hindawi + El-Khair + Arabic Gigaword +
OSCAR+ArabicNewsCorpus(OSIAN)+Wikipedia
Arabic
mBERT (Devlin et al. 2019)
BERT
Multilingual Arabic
ArabicBERT (Safaya et al. 2020)
BERT (mini,
medium, base, large)
Arabic
95GB
Arabic OSCAR corpus + Arabic Wikipedia
AraT5 (MSA, Tweet) (Nagoudi et al. 2022)
T5 (base, small)
Arabic
70GB, 178GB
AraNews + El-Khair + Gigaword + OSCAR + OSIAN
+ Wikipedia Arabic + Hindawi Books
Arabian GPT (Koubaa et al. 2024)
GPT
Arabic
10GB
Abu Elkhiar Corpus
AceGPT - AceGPT-chat (Huang et al. 2024)
LlaMA2
Bilingual
19.2B tokens,
10.8B tokens (Ar-En)
Open-source Arabic text + Arabic Wikipedia + CC100
+ OSCAR3
Mulhem (Malin 2024)
Generative LM
Bilingual + Saudi DA
90B tokens,
90B tokens (Ar-En)
Proprietary dataset, comprising 70,000 Saudi QA
entries, 500,000 Arabic single and turn dialogues, and
specialized context retrieval dataset
Jais (Sengupta et al. 2023)
Decoder from
transformer model
Bilingual
116B tokens, 279B
tokens (Ar-En)
Abu El-Khair, Aranews, C4, ArabicNews 2020, Mak-
tabah8, UN, Arabic Wikipedia, En2Ar Wikipedia,
Baai1to 7 Misc
Noor (Noor 2022)
Arabic
Fanar (Kahil 2024)
Arabic
300B words
ALLAM (Bari et al. 2024)
Bilingual
Under the “Languages” heading, “Arabic” refers to Modern Standard Arabic (MSA) by default. Notations such as CA or DA specify Classical or Dialectal Arabic, respectively. While “Bilingual”
includes models that support both Arabic and English
123
Page 5 of 28 
135

--- Page 6 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
Nowadays, the public frequently turns to modern platforms
like television, radio, and online resources for fatwas. This
shiftisoftenduetotherelevanceofmodernfatwastocontem-
porary issues and their use of contemporary Arabic, which
is easier for the general population to understand compared
to the classical Arabic used in older texts.
Modern fatwas typically appear in the form of letters or dia-
logues. Inthe letter format, the inquirer begins withagreeting
and proceeds to describe their situation and the speciﬁc reli-
gious or legal issue they are facing. They then pose a detai-
led question seeking guidance. The mufti’s reply typically
includes background information on the issue and discusses
interpretations and opinions from various Islamic schools,
drawing on the two principal sources, the Qur’an (Bashir
et al. 2023) and Hadith (Azmi et al. 2019). The mufti then
concludes with their well-informed viewpoint on the matter.
Conversely, in live broadcasts, fatwas are conducted as
interactive dialogues between the mufti and the questioner.
The questioner explains their circumstances, poses their
questions, and the mufti responds in a conversational man-
ner, often involving multiple exchanges. Despite this, many
modern fatwas are archived exactly as they are presented,
with no edits or simpliﬁcations. This can make it difﬁcult for
those seeking clear and straightforward answers.
2.5 Challenges and research gap
We explore the unique aspects of the Arabic language and
the challenges it presents to various NLP tasks.
Arabic, a Semitic language with 427 million native speak-
ers and an ofﬁcial language in 26 countries and the UN, holds
immense cultural and religious signiﬁcance as the liturgical
language for 1.8 billion Muslims, central to daily prayers and
key Islamic texts. Despite its widespread use, Arabic digital
content is surprisingly limited, representing only 5% of the
internet. The language is categorized into historical Clas-
sical Arabic and the contemporary literary standard, MSA,
which, while related, have distinct features. The emergence
of diverse colloquial dialects, lacking standardized spelling
and varying signiﬁcantly even within countries like Saudi
Arabia, further complicates the linguistic landscape. Ara-
bic’s right-to-left script comprises 28 consonants and three
long vowels, utilizing diacritics for short vowels, often omit-
ted in MSA, causing ambiguity. Arabic words, primarily
nouns, verbs, and particles, stem from consonant roots mod-
iﬁed morphologically to convey meaning and grammatical
information. While the typical word order is VSO, SVO and
VOS variations exist, and the absence of capitalization poses
challenges in identifying proper nouns (Mannaa et al. 2022;
Alwaneen et al. 2022; Biltawi et al. 2021; Saoudi and Gam-
moudi 2023). Finally, Arabization demonstrates Arabic’s
ability to integrate foreign words, while Arabizi, a Roman-
izedArabicscript,reﬂectsthelanguage’sadaptationtodigital
communication and raises discussions about linguistic iden-
tity.
In the development of QA systems, unique challenges
arise, especiallywithwordambiguityinNLPtasks, asdiscussed
by Saoudi and Gammoudi (2023). These include context sen-
sitivity, where the meaning of words can shift based on their
usage context; gender agreement, affecting word forms based
on the gender of the speaker or subject; and homonymy,
where words may sound identical but carry different mean-
ings, such as “right” and “write” or “
” and “
”.
Most current word and context embedding techniques rely
on computationally intensive methods, posing a signiﬁcant
challenge. Despite the promising advances in generative AI,
Arabic chatbots and QA systems continue to lag behind
those in dominant languages like English and Chinese.
Current trends lean towards generative-based approaches
that craft new responses. However, a survey by Alsheddi
and Alhenaki (2022) indicates that while English chatbots
frequently employ generative methods, Arabic systems pre-
dominantly use retrieval-based approaches with predeﬁned
responses. This disparity may stem from the less effec-
tive performance of advanced LLMs (e.g., ChatGPT) in
low-resource languages compared to English. Consequently,
there is a pressing need to enhance Arabic NLP resources,
including the development of more sophisticated tools and
datasets, to close the performance gap with high-resource
languages (Siu 2023).
Arabic NLP continues to struggle with a scarcity of high-
quality annotated datasets, which are essential for training
precise LLM models. The majority of available QA datasets
are not only limited in size but are also often generated
through AI techniques such as machine translation, lead-
ing to inaccuracies and numerous errors. Furthermore, many
existing QA datasets only offer short contexts and/or sim-
ple question pairs, which are inadequate for training systems
designed to manage long contexts or documents and com-
plex questions. There is a clear need for more open-domain
datasets as well as specialized QA datasets, such as those for
medical or customer service applications, to develop accu-
rate and high-performing closed-domain QA systems (Zeng
et al. 2020; Biltawi et al. 2021).
According to Alsheddi and Alhenaki (2022), evaluating
chatbots, including QA chatbots, presents signiﬁcant chal-
lenges due to the absence of a comprehensive evaluation
framework. Most Arabic studies depend on human eval-
uation, which is not only costly and time-consuming but
also prone to bias and error. Automated metrics may fail to
accurately assess human-like qualities in responses, such as
empathy, user satisfaction, and linguistic ﬂuency. Factors like
sentence length, multi-turn dialogues, conversational history,
and input ambiguity add further complexity to the evaluation
of QA chatbots. Commonly used evaluation metrics include
human assessments, followed by BLEU scores, and then
123
 135 
Page 6 of 28

--- Page 7 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
ROUGE-1 and ROUGE-2 scores. Notably, Arabic chatbot
studies predominantly utilize human evaluation, in contrast
to English studies, which often employ BLEU scores, possi-
bly reﬂecting the limited NLP resources available for Arabic.
2.6 Concluding remarks
This section has established a comprehensive foundation for
understandingthetechnologicalandlinguisticunderpinnings
of Arabic QA systems. It began by delineating the clas-
siﬁcation and operational mechanisms of chatbots, with a
particular focus on Question Answering (QA) and Machine
Reading Comprehension (MRC) systems, along with their
integration of question semantic similarity and document
retrieval techniques. We then examined the evolution of NLP
methodologies—from rule-based and statistical approaches
to modern deep learning architectures—and emphasized
the role of both context-independent and context-aware
word embeddings. A detailed overview of the development
of LLMs was provided, highlighting major architectural
paradigms, such as encoder-only, decoder-only, and encoder-
decoder models, and their adaptation to Arabic, including
recent specialized models like AraBERT, AraT5, and Jais.
The discussion also introduced the concept and structure of
Islamic fatwas as a domain of inquiry relevant to Arabic
QA, outlining their traditional and contemporary forms and
their reliance on authoritative Islamic texts (the Qur’an and
Hadith). Finally, we outlined the linguistic, computational,
and evaluation-related challenges that Arabic poses for NLP,
particularly in low-resource settings. These insights collec-
tively contextualize the research gaps and justify the need
for specialized datasets and robust evaluation frameworks,
thereby motivating the contributions presented in the remain-
der of this work.
3 Related works
We categorize the related literature into three sections: QA
systems, systems for detecting duplicate questions, and QA
datasets, with a focus exclusively on works pertaining to the
Arabic language.
3.1 Arabic QA systems
The investigation of Arabic Question Answering systems
reveals a shift from early information retrieval and rule-based
approaches (like QARAB and LEMAZA) towards more
sophisticated neural network models, particularly trans-
former architectures (exempliﬁed by SOQAL and SDMCN),
accompanied by a signiﬁcant drive to create diverse Arabic
QA datasets of varying sizes, domains, and question types
(including factoid, non-factoid, and multi-hop), often lever-
aging Arabic Wikipedia as a key resource and emphasizing
the importance of both standard and domain-speciﬁc eval-
uation metrics, while also addressing the unique linguistic
challenges of Arabic and exploring domain-speciﬁc applica-
tions like Qur’anic QA.
The early investigations into Arabic Question Answer-
ing, demonstrated by the QARAB system (Hammo et al.
2002), primarily depends on Information Retrieval methods
integrated with basic NLP techniques. QARAB’s reliance
on Salton’s vector model and keyword matching against a
database of Arabic newspaper texts represents a foundational
approach focused on retrieving short, factoid answers from
single documents. Similarly, Azmi and Alshenaiﬁ(2017)
developed LEMAZA, a reﬁned version of their earlier work
(Azmi and Alshenaiﬁ2016; Azmi and AlShenaiﬁ2014), to
answer “why” questions in Arabic texts using a Rhetorical
Structure Theory (RST) approach, which outlines texts in
hierarchical trees and identiﬁes rhetorical relations. While
LEMAZAdemonstratedthepotentialofleveraginglinguistic
structures for non-factoid QA, both systems represent funda-
mentally different approachs compared to the neural network
revolutionthatfollowed.Moreover,thebreadthofknowledge
accessible to these systems was less signiﬁcant than that of
subsequent systems.
A significant turning point in Arabic QA was marked by the
introduction of SOQAL (Mozannar et al. 2019), the ﬁrst sys-
tem to employ neural networks. By integrating a BERT-based
reader module for Machine Reading Comprehension and a
TF-IDF-based retrieval module accessing Arabic Wikipedia,
SOQAL tackled into open-domain QA. This transition to
neural architectures allowed for a deeper understanding of
contextcomparedtothekeyword-basedmethodsofQARAB.
Furthermore, SOQAL necessitated the creation of the ARCD
dataset, highlighting the growing recognition of the impor-
tance of dedicated evaluation resources for Arabic QA. This
emphasis on dataset creation continued with the work of
Abdallah et al. (2024), who introduced the large-scale, open-
domain ArabicaQA dataset, speciﬁcally designed for MRC
tasks on Arabic Wikipedia, directly addressing the data
scarcity issue prevalent in the ﬁeld.
The development of domain-speciﬁc Arabic QA systems
also emerged as a crucial research direction. The work by
Malhas and Elsayed (2022) focused on the Holy Qur’an,
utilizing a ﬁne-tuned AraBERT model (CL-AraBERT) and
introducing the QRCD dataset. This research underscores
the need for specialized models and evaluation metrics
when dealing with the unique linguistic and semantic char-
acteristics of speciﬁc domains. Similarly, the creation of
datasets like Arabic WikiReading and KaifLematha (Albi-
lali et al. 2022) further diversiﬁed the available resources,
with KaifLematha speciﬁcally targeting non-factoid “how”
and “why” questions through crowdsourcing, demonstrating
a move beyond purely fact-based QA.
123
Page 7 of 28 
135

--- Page 8 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
More recent advancements have focused on tackling the
complexities of multi-hop reasoning and non-factoid ques-
tion answering. The introduction of the ACQAD dataset (Sid-
houm et al. 2022) provided a valuable resource for training and
evaluating systems capable of answering complex questions
requiringinferenceacrossmultipledocuments.Furthermore,the
development of models like the Stacked Dynamic Memory-
Coattention Network (SDMCN) (Alwaneen and Azmi 2024),
building upon sophisticated attention and memory mecha-
nisms, represents a signiﬁcant step towards improving the
accuracy of responses to non-factoid questions, particu-
larly “why” questions, outperforming earlier linguistic-based
approaches like LEMAZA on dedicated datasets.
3.2 Arabic duplicated question detection system
Since duplicate questions can be valuable for training
retrieval-based QA (Question Answering) systems, several
studies focus on this area. Hamza et al. (2022) aims to
improveArabicquestionclassiﬁcationandduplicationdetec-
tion. Their approach combines ELMo for contextualizing
questions with a specialized Bidirectional Attention Bidirec-
tional LSTM (BiAttention-BiLSTM) architecture, designed
to identify key features within question pairs from the maw-
doo3 dataset. The study also incorporates ﬁltering and data
augmentation techniques to enhance performance. In addi-
tion, DAQAS (Alami et al. 2023) tackles this by utilizing
denseretrieval for questions previouslyencountered. For new
questions, the system employs a pipeline starting with BM25
retrieval, which is enhanced by neural query expansion. Sub-
sequently, MRC (Machine Reading Comprehension) is used
to extract the answer. DAQAS demonstrates strong per-
formance on both duplicate question detection (using the
mawdoo3 dataset) and answer extraction (using a combined
dataset). Notably, the GiGA BERT model proved particularly
effective in this system.
3.3 Arabic QA dataset
The signiﬁcant advancements in NLP applications, fueled
by AI and the development of LLM models, underscore the
necessity for high-quality datasets. To construct QA datasets,
researchers employ a variety of methods such as crowdsourc-
ing, human annotation, AI-driven techniques, or a blend of
these approaches. Each method offers its own set of strengths
and weaknesses:
• Crowdsourcing. This method leverages the collective
efforts of a large number of contributors to quickly gen-
erate substantial data volumes. However, crowdsourced
data can be prone to quality issues, especially if the tasks
are not clearly deﬁned or require specialized knowledge.
Problems can be further compounded in unsupervised or
semi-supervised settings, where limited oversight may
allow inaccuracies to proliferate. For instance, the expe-
riences reported by Almuzaini and Azmi (2022) using
platforms like Click Worker and Amazon Mechanical
Turk (Mturk) revealed signiﬁcant challenges in qual-
ity management, especially when dealing with tasks in
Arabic. Despite detailed instructions and a meticulous
selection process, many documents were still incorrectly
annotated, highlighting the difﬁculty in ensuring consis-
tent quality in crowdsourced data.
• Human annotation. Datasets annotated by humans, par-
ticularly by domain experts, typically offer the highest
quality, ensuring relevance and accuracy critical for NLP
tasks. The main drawbacks are the costs associated with
recruiting and training annotators and the time-intensive
nature of the annotation process. Additionally, even
expert annotators can introduce bias, potentially com-
promising data integrity. In the context of Almuzaini and
Azmi (2022), the reliance on human experts via crowd-
sourcing platforms provided mixed results in terms of
data coherence and annotation accuracy compared to the
AI model developed.
• AI techniques. Employing AI methods such as data aug-
mentation and machine translation can greatly expand the
volume of a QA dataset. These approaches help automate
the dataset creation process, which can decrease costs
and expedite development compared to manual annota-
tion. However, AI-generated data might include errors or
inconsistencies that are challenging to identify and cor-
rect in subsequent quality control steps.
The experiences detailed in Almuzaini and Azmi (2022)
underline the trade-offs between these methods. While
crowdsourcing offers a practical solution for large-scale data
annotation, particularly when expert resources are limited
or expensive, it requires stringent management to maintain
quality. AI techniques, while efﬁcient, must be continuously
reﬁned to ensure the output’s quality matches human-level
precision. By combining these approaches, the goal is to
harness their strengths while mitigating their weaknesses,
striving for an optimal balance of quality, efﬁciency, and cost
in dataset creation for NLP applications.
Table 2 lists the Arabic QA datasets. As noticed, a key
observation is the signiﬁcant role of Arabic Wikipedia as
the primary source for context passages. This leads to a bias
toward encyclopedic knowledge, which suits open-domain
QA systems. Furthermore, MSA is the predominant lan-
guage type, with Classical Arabic addressed by QRCD, while
dialectal Arabic remains largely underrepresented in these
prominent datasets. This could be related to the primary
dependence on Wikipedia as the main source of knowledge in
most of the datasets. On the level of the NLP task, extractive
MRC is the most dominant, as seen in datasets like SQuAD,
ARCD, AQAD, ArQuAD, and ArabicaQA-MRC
123
 135 
Page 8 of 28

--- Page 9 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
Table 2 Summary of Arabic QA datasets: The datasets are classiﬁed under the task of Machine Reading Comprehension (MRC) and are further categorized by question type, differentiating
between ’Open’ domain and ’Closed’ domain questions. The datasets are arranged in chronological order based on their publication date
Name
Size
Technique
Task
Source
Question type
QArabPro (Akour et al. 2011)
335
Crowdsourced
QA
Wikipedia
Open
LEMAZA (Azmi and Alshenaiﬁ2017)
110
Manually compiled
Why-QA pairs
700 documents from OSAC
(Saad and Ashour 2010)
Open (non-factoid questions)
DAWQAS (Ismail and Homsi 2018)
3,205
Automatically Generated question
QA
Web documents
Open (non-factoid questions)
ARCD (Mozannar et al. 2019)
1395
Crowdsourced
MRC
Arabic Wikipedia
Open
Arabic-SQuAD (Mozannar et al. 2019)
48,344
MT Squad
Extractive MRC
Translated Wikipedia
Open
Xsquad (Artetxe et al. 2020)
1190
Translated squad (development set)
Extractive MRC
Wikipedia
Open
AQAD (Atef et al. 2020)
17,911
MT on squad QA + Semantic Sim-
ilarity module
Extractive MRC
Arabic Wikipedia
Open
TyDiQA (Arabic) (Clark et al. 2020)
15,645
Crowdsourced
Extractive MRC
Arabic Wikipedia
Open
MLQA (Lewis et al. 2020)
5,852
Parallel Sentence Mining + Crowd-
sourced + translation
Extractive MRC
Wikipedia articles
Open
Arabic WikiReading (Albilali et al. 2022)
98,643
Distant supervision + Wikidata as
ground truth
MRC
Wikipedia articles
Open
KaifLematha (Albilali et al. 2022)
6,761
Crowdsourced
MRC
Wikipedia articles
Open (non-factoid questions)
MSA-QA (Alruqi and Alzahrani 2023)
398
Augmentation techniques + Collect
context
MRC
Web documents
Closed (AI and ML)
Arabic AskFM(*)
98,422
Collected from ask-FM
QA pairs
Closed (Islamic fatwa)
ASER (Biltawi et al. 2023)
10,000
Manually collected
Extractive MRC
Open
OpenQAS (Alami et al. 2023)
72,507
Fusing sample from other dataset
Extractive MRC
ARCD, Arabic SQuAD,
MLQA, XQuAD,
and TyDi QA
Open
ArQuAD (Obeidat et al. 2024)
16,020
Language experts
Extractive MRC
Arabic Wikipedia
Open
ArabicaQA (Abdallah et al. 2024)
89,095+3,701
Crowdsourced
Extractive MRC
Wikipedia
Open
ArTrivia (Alrowili and Vijay-Shanker 2023)
10,000
Automated
pipeline
for
Arabic
Wikipedia structured data
Extractive MRC
Wikipedia
Open
QRCD (Malhas and Elsayed 2022)
1,337
Human annotation (Expertise)
Extractive MRC
Qur’an
Closed (Islamic-Qur’an)
FAAQA-QAD (Abdelaziz et al. 2021)
520
Expertise and Crowdsourced
Extractive MRC
Webteb and Islamweb
Closed (Healthcare)
(*) Dataset available at, https://github.com/Omarito2412/ASKFM
123
Page 9 of 28 
135

--- Page 10 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
The methods employed for creating these datasets have
evolved from machine translation, exempliﬁed by Arabic-
SQuAD, toward crowdsourcing or expert linguists, as seen
in datasets like ARCD, ArQuAD, TyDiQA, and ArabicaQA,
to ensure data quality. Many datasets aim to balance scale and
quality through hybrid approaches, with AQAD, DAWQAS,
and Arabic WikiReading representing this direction.
Simultaneously, there’s a growing trend towards special-
ization, with the emergence of resources targeting speciﬁc
domains like the Qur’an (QRCD) and health (FAAQA-QAD).
Another direction focuses on speciﬁc question types such as
Why-questions (LEMAZA, KaifLematha, and DAWQAS).
Another trend focuses on evaluation paradigms such as cross-
lingual transfer (XQuAD, MLQA) and information-seeking
(TyDiQA).
Despite the presented progress, Arabic QA systems still
lag considerably behind those developed for languages with
more resources, highlighting a critical need for extensive
and high-quality datasets. Although ongoing research is
addressing this gap, more dedicated effort is essential, par-
ticularly in tackling non-factoid and complex reasoning
questions. Another important direction is the development
of specialized QA systems that require deep understand-
ing of speciﬁc domains and corresponding datasets. Ulti-
mately, the advancement of sophisticated Arabic chatbots
demands a transition from basic factoid responses based
on limited data to the ability to handle complex reasoning,
non-factual inquiries, and domain-speciﬁc knowledge, all
while accounting for the unique linguistic features of Arabic.
Unfortunately, Arabic QA datasets continues to face a fun-
damental dilemma: the trade-off between generating large
datasets (often using methods that might compromise qual-
ity) and ensuring the availability of high-quality, authentic
data, which requires human annotation. As a result, while
benchmarks for cross-lingual evaluation exist, the need for
robust monolingual Arabic resources remains to drive the
progress in this ﬁeld.
4 Our Hajj QA dataset
The Hajj-FQA dataset was developed to address the crit-
ical need for accurate Arabic question-answering systems
that can assist pilgrims during the Hajj with human-like
conversational responses. Recent advances in LLMs have
demonstrated their potential for such applications, but their
effectiveness remains constrained by the limited availability
of high-quality, domain-speciﬁc Arabic QA datasets - a key
bottleneck in Arabic NLP development.
Our primary aim is to bridge this gap by developing a
dataset that not only supports the training of LLMs but also
boosts the functionality of QA chatbots. This dataset will
cater to various NLP tasks within the QA chatbot pipeline,
including machine reading comprehension for extractive and
generative answering and Semantic Similarity to identify
duplicate questions and answers. By creating this compre-
hensive dataset, we intend to provide a foundational resource
that enhances the capabilities of Arabic QA systems, ensur-
ing they are as responsive and effective as possible.
In this section we will discuss the process of constructing
our Hajj-FQA dataset, followed by testing the dataset using
multiple LLM.
4.1 Compiling preliminary dataset
To construct our datasets, we follow the four-step process
outlined in Algorithm 1, which includes data collection,
question construction, answer generation, and ﬁltering and
cleaning. Each step in this sequence will be discussed in
greater detail to clarify the methodologies employed. This
procedure adheres to a comprehensive guideline speciﬁed in
Section 4.2.
123
 135 
Page 10 of 28

--- Page 11 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
We developed a web scraping tool to gather contextual
data from reliable fatwa websites, speciﬁcally https://binbaz.
org.sa and https://binothaimeen.net, chosen for their exten-
sive and varied content, including fatwas in the forms of
letters or dialogues. To ensure relevance to our study, we uti-
lized these websites’ search engines to collect only fatwas
pertaining to Hajj, using search terms like
(Hajj),
(umrah),
(tawaf),
(sa‘i),
(ihram), and
(miqat). This targeted approach resulted in a collection of
886 Hajj-related fatwas, with the majority—791 fatwas—
sourced from https://www.binbaz.org.sa. Each record in our
dataset includes the source website, fatwa number, title, ques-
tion, and answer.
We recruited Arabic editing experts who are well-versed
in Islamic fatwas to assist in analyzing each fatwa and
developing a set of questions. The experts were tasked with
formulating four types of questions for each fatwa:
Semantically identical question pairs. This process invol-
ves creating two simpliﬁed questions (referred to as “SI Q1”
and “SI Q2”) that rephrase the original fatwa question. For
fatwas containing multiple questions, particularly those in
a dialogue format, experts concentrated on extracting and
rephrasing the primary question to create these pairs.
Cleaning the question. Recognizing that fatwa questions
oftencontainstandaloneinquiriesmixedwithextraneousele-
ments like greetings, prayers, or personal details, the experts
reﬁned these questions by removing unrelated/irrelevant con-
tent to improve clarity. We refer to this reﬁned version as
“Cleaned Q”. For those unfamiliar with Arabic culture, it
is common to encounter expressions such as
(meaning “May Allah protect you”) or
(meaning “May Allah reward you”) within such questions.
These elements, while culturally signiﬁcant, were removed
to focus on the core inquiry.
Title question. Experts also crafted concise and direct ques-
tions derived from the titles of the fatwas, whenever titles
were available, to provide clear and pointed inquiries. It will
be referred to as “Title Q”.
This structured approach ensured that the derived ques-
tions were both relevant and speciﬁc, aiding in the effective
comprehension and use of the fatwa content.
After formulating the questions, we directed the experts to
respond to the four questions by selecting up to ﬁve pertinent
text spans from the fatwa’s answer, “extractive answers”. We
stressed the importance of using the same text span to answer
all four questions. Furthermore, we directed the experts to
create a semantically similar answer to the ﬁrst extracted
span. It will be referred to as “Generative answer”.
4.2 Annotation guidelines
The fatwa dataset’s questions and answers were developed
according to three annotation guideline groups. First, rele-
vance and scope guidelines maintained consistent focus on
Hajj-related topics. Second, answer content and quality along
withquestionformulationguidelinesgovernedboththecraft-
ing of effective questions and the production of high-quality
answers. Finally, quality assurance and consistency guide-
lines were applied to verify the dataset’s overall reliability.
Relevance and scope ensures Hajj-focused content consis-
tency:
• Both question and answer must directly address Hajj rit-
uals, rulings, or speciﬁc circumstances.
• Fatwas exceeding 2000 words in original answer length
are excluded.
• Each question-answer pair must focus on a single Hajj
topic (multiple topics require separate Q-A pairs when
feasible).
• For dialogic or compound-question fatwas, extract only
one Hajj-related question with all relevant answer spans.
Answer content and quality question formulation governs
question creation and answer processing:
• Questions should clearly target the fatwa’s core issue.
• Answers must be concise and pilgrim-focused during
Hajj.
• Answers should directly quote the Mufti’s opinion with-
out supporting Qur’anic verses or Hadith.
• Case-dependent answers require combination with rele-
vant cases to prevent misinterpretation.
• Exclude fatwas with implied rather than explicit answers.
• Prioritize the most probable/general answer when multi-
ple options exist.
• For repetitive answers, select the ﬁve most concise ver-
sions.
Quality assurance and consistency maintains data reliabil-
ity:
• Four expert annotator groups work in pairs on each fatwa
to minimize bias.
• Initial sample review resolved annotation ambiguities.
• Annotation examples (related/unrelated fatwas, com-
pound cases) were provided.
123
Page 11 of 28 
135

--- Page 12 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
Table 3 Randomly selected examples from the Hajj-FQA dataset. SI Q1 and SI Q2 represent semantically identical question pairs
123
 135 
Page 12 of 28

--- Page 13 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
• Answer extraction follows question construction to ensure
context comprehension.
• Reject fatwas presenting uncovered edge cases.
• Finalcomprehensive reviewfilterednon-compliant entries.
After constructing the preliminary dataset and following
the annotation guidelines, we removed leading and trailing
white spaces and excluded fatwas with excessively long con-
texts, questions, or answers. The dataset now comprises 800
samples. Selected random samples from the dataset are dis-
played in Table 3.
4.3 Constructing four datasets
We derived four specialized datasets from the preliminary
collection: (1) HajjFatwa MRC (extractive), (2) HajjFatwa
MRC (generative), (3) HajjFatwa SQS (similar question
semantic), and (4) HajjFatwa SAS (similar answer seman-
tic). Each dataset serves distinct purposes in our analysis, as
we will detail below. All together, these four datasets com-
prise the Hajj-FQA dataset.
HajjFatwa MRC (extractive). This dataset integrates the
original fatwa answer as context along with one of the for-
mulated questions—either the title question, the cleaned
question, or one from the identical question pair—and the
corresponding extractive answers (up to ﬁve answer spans).
It comprises 2826 samples.
HajjFatwa MRC (generative). This dataset incorporates
the original fatwa answer as context along with one of four
crafted questions (title question, cleaned question, or one
from a pair of identical questions) and the generative answer.
It contains the same number of samples as the previous
dataset.
HajjFatwa SQS (duplicate question). This dataset utilizes
the identical question pairs, labeling them with a 1 to indicate
they are duplicates. Additionally, two questions from differ-
ent samples are paired, manually veriﬁed to ensure they are
not duplicates, and labeled with a 0. This yielded a dataset
containing 1600 samples.
HajjFatwa SAS (duplicate answer). This dataset uses the
same process as before on both extractive and generative
answers to construct it, maintaining the same size.
5 Analysis of the dataset
We conducted a quantitative analysis of our Hajj-FQA
dataset, with the results of the question word distribution pre-
sented in Table 4. Furthermore, a visual compression against
Table 4 Statistical distribution of question types in our Hajj-FQA
dataset. ‘Polar’ denotes questions that require Yes/No answers, while
‘Comp Q’ indicates “composed questions,” which are structured with-
out traditional question words
Title Q
Cleaned Q
SI Q1
SI Q2
Total
%
What
533
73
242
225
1073
37.97
When
4
3
5
5
17
0.6
Where
2
1
5
5
13
0.46
How much
1
2
2
1
6
0.21
How
11
7
7
17
42
1.49
Polar
107
109
277
257
750
26.54
Which
9
19
25
17
70
2.48
Why
3
3
4
2
12
0.42
Comp Q
30
309
233
271
843
29.83
Total
700
526
800
800
2826
100
the other datasets (QRCD, ArTrivia, TyDi) is provided in
Fig. 1.
We analyzed question distributions by applying string
matching to categorize each question based on its initial
word (e.g., “What”, “When”, “How”). To accommodate non-
standard question structures, we introduced a “composed
question” category for inquiries beginning with descriptive
context rather than typical question words. These composed
questions typically present a speciﬁc situation or issue before
posing the actual query, as illustrated in this Arabic example
with English translation:
“A person donned the ihram for Umrah for the ﬁrst time
but did not complete it. Several years later, he entered
ihram again and ﬁnished his Umrah. What steps should
he take now?”
Fig. 1 Question words distribution diagram comparing our Hajj-FQA
dataset with QRCD, ArTrivia, and TyDi datasets
123
Page 13 of 28 
135

--- Page 14 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
The “composed questions” are considered the most chal-
lenging category due to their length and the advanced level of
comprehension they require. Responding to these questions
is particularly difﬁcult because the answers found in fatwas
are often complex, with descriptive sentences integral to the
context that must be fully understood.
The skewed distribution in the Hajj-FQA dataset reﬂects
its specialized domain. Composed questions, which preface
inquiries with contextual details, account for nearly 30% of
questions in Hajj-FQA but are rare or absent in other datasets.
This pattern indicates users’ tendency to frame queries with
speciﬁc circumstances. Polar (Yes/No) questions also domi-
nateinHajj-FQA(26.54%)andQRCD(21.73%),contrasting
sharply with their minimal presence in ArTrivia and TyDi
(≈1%), as users often seek clear rulings on permissibility.
“What” questions appear consistently across datasets (30–
44%), with their prevalence in Hajj-FQA reﬂecting the need
for deﬁnitional clariﬁcations and ruling explanations.
Conversely, “Who”, “When”, and “Where” questions are
nearly absent in Hajj-FQA (0–0.6%), despite their promi-
nence in general-knowledge datasets (e.g., 24% “Who” in
ArTrivia, 29% “When” in TyDi). QRCD shows moderate
representation of these types (“Who” at 16.85%, “When” at
2.32%). Their scarcity in Hajj-FQA aligns with the dataset’s
focus on religious guidance, where such questions are less
relevant compared to factual or spatiotemporal inquiries in
broader domains.
From the question distribution, it is clear that the closed-
domain Hajj-FQA dataset and QRCD share a distribution
more similar to each other than to the open-domain ArTrivia
and TyDi QA datasets. Based on this, we provide a compar-
ison of the Hajj-FQA dataset with two other Arabic closed-
domain datasets on key metrics. As shown in Table 5, this
Table 6 Token count for fatwa dataset using the NLTK package
Number of tokens
Min
Max
Avg
Original fatwa answer
15
1914
163.99
Title Q
3
21
8.29
Cleaned Q
3
36
16.63
SI Q1
3
68
13.26
SI Q2
3
64
12.73
Extractive answer
1
291
20.28
Generative answer
2
103
17.9
comparison involves three closed-domain Arabic datasets:
QRCD (focused on the Qur’an), FAAQA-QAD (healthcare),
and our Hajj-FQA.
Hajj-FQA emerges as the most extensive dataset in scale,
containing both the highest number of question-context pairs
and answer triplets. Its distinctive feature lies in answer
multiplicity, with over 2000 cases containing multiple valid
answers - signiﬁcantly surpassing QRCD’s 154 instances and
FAAQA-QAD’s complete absence of such cases. While all
datasets support extractive machine reading comprehension
(MRC-Ex), Hajj-FQA uniquely accommodates generative
approaches (MRC-Gen). Benchmark results reveal dataset-
speciﬁc model performance patterns: CL-AraBERT excels
on QRCD, ARBERT performs best on FAAQA-QAD, while
AraBERTv0.2-base achieves superior results on Hajj-FQA,
attaining the highest reported F-score (≈72.78). Compre-
hensive performance analysis follows in subsequent sections.
Table 5 Comparison of three closed-domain Arabic datasets which includes our Hajj-FQA
Feature
QRCD
FAAQA-QAD
Hajj-FQA
Domain
Islamic
Healthcare
Islamic Hajj Fatwas
Source
The Holy Qur’an
WebTeb
https://binbaz.org.sa, and https://
binothaimeen.net
Model
CL-AraBERT
ARBERT
AraBERTv0.2-base
Performance (F-score, EM)
(40.94, 21.19)
(68.29, 35)
(72.78, 26.13)
Question-Context pairs
1093
520
2826
Multi answers
154
0
2059
Question-Context-Answer triplets
1337
520
6363, and 2826
Tasks
Extractive machine reading com-
prehension (MRC-Ex)
MRC-Ex
MRC-Ex,
Generative
machine
reading
comprehension
(MRC-
Gen), Duplicate question detection
(DQD),
and
Duplicate
answer
detection (DAD)
123
 135 
Page 14 of 28

--- Page 15 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
Fig. 2 Trigram preﬁxes distribution of: (a) SI Q1, (b) SI Q2, (c) Title Q, and (d) Cleaned Q
Additionally, we performed a token count analysis using
the NLTK (Natural Language Toolkit) package in Python.3
The ﬁndings, presented in Table 6, demonstrate variations
in question length, with cleaned questions being the longest
and title questions the shortest. This suggests that the experts
3 See, https://www.nltk.org.
closely followed the guidelines provided for constructing
questions.
To further analyze the dataset questions, we examined the
distribution of trigram preﬁxes for title questions, cleaned
questions, and duplicate question pairs, as illustrated in
Fig. 2. Notably, the duplicate question pairs exhibit similar
distributions of question words. In contrast, title questions
123
Page 15 of 28 
135

--- Page 16 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
are predominantly phrased with
(translation: “What
istheIslamicruling”),likelybecausetheyaredirectlyderived
from the question titles. Cleaned questions, which most accu-
rately reﬂect the actual content of the fatwas, display a
distinct distribution compared to the other categories. These
patterns indicate that the experts adhered closely to the anno-
tation guidelines for constructing questions.
Our analysis demonstrates that Hajj-FQA surpasses exist-
ing Arabic QA datasets for Hajj-speciﬁc applications due
to its domain-focused design. Derived from authentic Hajj
fatwa inquiries, the dataset captures real-world question
patterns, including a signiﬁcant proportion of composite
questions (often absent in general-knowledge datasets like
AR-SQuAD, ARCD, or TyDiQA). These distinctive char-
acteristics enable better model training for Hajj-related
nuances, which are underrepresented even in broader Islamic
QA datasets like QRCD. Hajj-FQA’s rigorous manual con-
struction, guided by strict inter-annotator agreement proto-
cols, ensures high-quality annotations. The dataset’s ver-
satility supports multiple QA tasks: generative answering
(HajjFatwa MRC-Gen), extractive answering (HajjFatwa
MRC-Ex), retrieval systems (HajjFatwa SQS), and answer
evaluation (HajjFatwa SAS). In the following section, we
validate these advantages through comprehensive LLM ﬁne-
tuning experiments across all four dataset variants.
6 Testing and evaluation of the dataset
on diﬀerent language models
We benchmarked our dataset by ﬁne-tuning the following
models and evaluating their performance on each designated
task.
1. XLM-V-base (Liang et al. 2023). XLM-V is a mul-
tilingual language model with a one-million-token
vocabulary, trained on 2.5TB of data from Common
Crawl.
2. XLM-RoBERTa-base (Conneau et al. 2020). XLM-
RoBERTa is a multilingual model pre-trained on 2.5TB
ofﬁlteredCommonCrawldata,encompassingtextfrom
100 languages.
3. BERT-multilingual-base-cased (Devlin et al. 2019). A
BERT model pre-trained on the top 104 languages from
Wikipedia.
4. DistilBERT-base-multilingual-cased (Sanh et al. 2020).
A distilled version of the BERT base multilingual
model.
5. DeBERTaV3-base (He et al. 2023). The multilingual
version of DeBERTa, enhanced using ELECTRA-style
pre-training.
6. Arabic-BERT-base (Safaya et al. 2020). A BERT-base
model pre-trained on 95GB of Arabic data.
7. AraELECTRA-base-discriminator (Antoun et al. 2021).
A BERT base model enhanced with ELECTRA learn-
ing, trained on 77GB of Arabic data.
8. MARBERTv2 and ARBERT (Abdul-Mageed et al.
2021). BERT base models trained on Modern Standard
Arabic and Dialectal Arabic.
9. CAMeLBERT-MSA (Inoue et al. 2021). A BERT base
model pre-trained on MSA Arabic.
10. AraBERTv2-base, AraBERTv2-large, AraBERTv0.2-
base, AraBERTv0.2-large.4 Various BERT models of
different sizes, trained on 77GB of Arabic data.
11. A bert2BERT-based model initialized with AraBERT
and ﬁne-tuned on 84K paragraph-summary pairs (Bani-
Almarjeh and Kurdy 2023).
12. Transformer, an encoder-decoder model trained on a
385K paragraph-summary dataset (Bani-Almarjeh and
Kurdy 2023).
13. mT5-base_ar.5 A streamlined version of Google’s mt5-
base, is pretrained on Arabic and includes some English
embeddings.
14. Arabic-T5-small.6 A T5v1.1 (small) version, pretrained
using 10% of the Arabic Billion Words corpus, along
with Arabic mC4 and Arabic Oscar datasets.
15. AraBART.7 A BART-based model featuring 6 encoders
and 6 decoders, pretrained on a comprehensive Arabic
dataset.
16. mT5-small (Xue et al. 2021). A multilingual version of
the T5-small, pretrained across 101 languages using the
mC4 corpus.
17. AraT5-base (Nagoudi et al. 2022). A T5-base model
pretrained using a mix of Modern Standard Arabic
(MSA) and Twitter data.
18. AraT5-MSA-base (Nagoudi et al. 2022). A T5-base
model speciﬁcally pretrained on MSA datas.
6.1 Evaluation metrics
Our evaluation framework accounts for both answering
paradigms (extractive/generative) and Arabic’s linguistic
properties. For extractive QA, we adopted SQuAD’s stan-
dard metrics (Rajpurkar et al. 2016): Exact Match (EM) and
F-score, which measure lexical overlap between predicted
and reference answer spans. To address Arabic orthographic
variations, we applied text normalization—standardizing let-
4 Pre-trained Transformers for Arabic language understanding and gen-
eration (Arabic BERT, Arabic GPT2, Arabic ELECTRA) are available
for download from, https://github.com/aub-mind/arabert
5 Available: https://huggingface.co/ﬂax-community/arabic-t5-small.
6 Available: https://huggingface.co/ﬂax-community/arabic-t5-small.
7 Available: https://huggingface.co/moussaKam/AraBART.
123
 135 
Page 16 of 28

--- Page 17 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
ter forms, removing diacritics and Tatweel—before metric
computation. This approach ensures direct comparability
with established QA research while accommodating Arabic’s
unique characteristics.
For EM and the F-score. Let PredAns represent the pre-
dicted answer, and RefAns denote the reference or ground
truth answer. Subsequently,
EM =

0, if PredAns ̸= RefAns,
1, otherwise,
,
(1)
P = Count

match PredAns words

Count

PredAns words

,
(2)
R = Count

match PredAns words

Count

RefAns words

,
(3)
F1 = 2P R
P + R ,
(4)
the matched PredAns words refer to the words that appear
both in the reference and the predicted answers.
Many of the automatic metrics rely on the concept of
n-gram. Brieﬂy, an n-gram is a contiguous sequence of n
items from a given sample of text, where the items can be
phonemes, syllables, letters, or words according to the appli-
cation. This concept is widely used in statistical NLP to
model language data and predict the next item in sequences.
For instance, in the sentence “The quick brown fox jumps
over the lazy dog,” a 2-gram (or bigram) sequence would
include “The quick,” “quick brown,” “brown fox,” and so
forth. Similarly, a 3-gram (or trigram) sequence from the
same sentence would generate “The quick brown,” “quick
brown fox,” etc. These n-grams help in tasks like text pre-
diction by providing a probabilistic framework to anticipate
subsequent elements based on observed sequences.
For generative QA evaluation, we combined n-gram overlap
metrics (F-score, BLEU-N, ROUGE-N) with BERTScore
(Zhang et al. 2019). BLEU-N emphasizes precision by
measuring word presence in references, while ROUGE-N
focuses on recall of key information. Although these n-gram
metrics cannot fully capture Arabic morphological varia-
tion or semantic equivalence—penalizing valid paraphrases
and weighting all words equally—they remain valuable for
assessing adherence to original fatwa wording, a critical
requirement in our domain. Their computational efﬁciency
and widespread adoption further justiﬁed their inclusion.
BERTScore complements these limitations by leverag-
ing contextual embeddings to evaluate semantic similarity,
demonstrating stronger correlation with human judgments
despite higher computational costs and lower interpretabil-
ity (Zhang et al. 2019). Its effectiveness has been validated
acrossArabicNLPtasksincludingparaphrasing(Al-Shameri
and Al-Khalifa 2024), text simpliﬁcation (Khallaf et al. 2022;
Al-ThanyyanandAzmi2023,andlegalQA(BayanKmainasi
et al. 2025). While alternatives like METEOR (Banerjee and
Lavie2005)(limitedbystemmingandsynonymresources)or
KPQA (Lee et al. 2020) (challenging to train) offer speciﬁc
advantages, and LLM-based evaluators such as GPT-score
(Fu et al. 2023) and LLM-Mixtral (Abdel Azim et al. 2025)
presentscalabilityconstraints,BERTScoreprovidedtheopti-
mal balance of accuracy and practicality for our Arabic
generative QA task.
BLEU-N = Brevity Penalty × n-gram overlap,
= min

1, exp

1 −
Count

RefAns words

Count

PredAns words


×
N

n=1
N
n-gram precision,
(5)
where N is the maximum n-gram order, typically 4, and the
n-gram precision is calculated using,
n-gram precision = Number of matching n-grams
Count

PredAns n-grams

,
(6)
wherethenumeratorcountsthenumberofn-gramsinthepre-
dicted answers that appear in the reference(s). If an n-gram
appears multiple times, it is counted only as many times as
it appears in the reference(s).
ROUGE (Recall-Oriented Understudy for Gisting Evalu-
ation) primarily uses ROUGE-n for n-gram overlap measure-
ment and ROUGE-L for longest common subsequence. The
ROUGE-n score calculates n-gram matches between pre-
dicted and reference answers as:
ROUGE-n = Number of overlapping n-grams
Count

RefAns n-grams

,
(7)
where the numerator counts the number of n-grams in the
PredAns that also appears in the RefAns. On the other hand,
the ROUGE-L measures the overlap of the longest common
subsequence (LCS) between the predicted and the reference
answers. It focuses on the longest sequence of words that
appear in both answers in the same order (but not necessarily
consecutively). It is calculated using,
ROUGE-L = Length of LCS(PredAns, RefAns)
Count

RefAns words

.
(8)
Generated answers are evaluated using BERTScore
(BERT-P, BERT-R, BERT-F), which measures cosine sim-
ilarity between contextual embeddings from a pretrained
123
Page 17 of 28 
135

--- Page 18 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
BERT-base model. Given predicted answer embeddings
PredTks and reference embeddings RefTks, with representing
vector similarity, the metric computes:
BERT-P =
	
p∈{PredTks}
max
r∈{RefTks}CosSim(p,r)
|PredTks|
,
(9)
BERT-R =
	
r∈{RefTks}
max
p∈{PredTks}CosSim(r, p)
|RefTks|
,
(10)
BERT-F = 2 · BERT-P · BERT-R
BERT-P + BERT-R ,
(11)
where CosSim( ) measures the cosine similarity between
tokens embedding vectors.
Given that the task of semantic similarity (duplicate detec-
tion) is classiﬁed as a classiﬁcation problem, we employ the
following metrics. It’s important to note that TP (TN) and FP
(FN) represent the true positives (negatives) and false posi-
tives (negatives), respectively:
Acc =
TP + TN
TP + TN + FP + FN,
(12)
P =
TP
TP + FP,
(13)
R =
TP
TP + FN.
(14)
We determined the optimal threshold (cut-off) for cal-
culating these metrics by utilizing the receiver-operating
characteristic curve (ROC), which plots the true positive rate
(TPR) against the false positive rate (FPR ). The point on the
curve that maximizes the Youden index (YI) was selected as
the optimal threshold (toptimal).
toptimal = argmax(YIt),
(15)
YIt = TPR(t) −FPR(t),
(16)
Moreover, we use the average precision avgP score to
evaluate the model’s performance,
avgP =
n

i=1
(Ri −Ri−1) · Pi,
(17)
where i denotes the i-th threshold.
6.2 Machine reading comprehension (MRC)
We conducted MRC ﬁne-tuning using an Nvidia GeForce
RTX 4090 GPU (24GB memory) with 10-fold cross-valida-
tion. Encoder-based models (1–10 in Section 6) for extrac-
tive QA were trained for 6 epochs (learning rate at 3e-5,
Table 7 Training hyperparameters. CE denotes cross-entropy, while
CBE refers to binary cross-entropy
Parameter
MRC-Ex
MRC-Gen
DQD/DAD
Epoch
6
5
5
Training Batch
16
4
16
Loss Function
CE
CE
BCE
Warmup_steps
500
500
100
Scheduler
Linear
Linear
Linear
Optimizer
AdamW
AdamW
AdamW
Learning rate
3e-05
3e-04
2e-05
Weight_decay
0.0
0.0
0.01
Seed
135
135
135
AdamW optimizer), while Seq2Seq models (11–18) for gen-
erative QA used 5 epochs with a higher learning rate (3e-4)
to accommodate larger architectures. Complete hyperparam-
eters appear in Table 7, with training dynamics visualized in
Fig. 3.
The training dynamics (Fig. 3) show BERT-multilingual-
base-cased achieving the lowest final training loss in the MRC-
Ex task, closely followed by ARBERTv2, DeBERTaV3-base,
DistilBERT-base-multilingual-cased, and Arabic-BERT-base.
For generative answering, Arabic-T5-small demonstrated
superior performance with the lowest training loss, outper-
forming strong competitors like Transformer and AraBART
while showing rapid initial convergence. In contrast, mT5
variants, AraT5-base, BERT2bert, and AraT5-MSA-base
exhibited signiﬁcantly higher ﬁnal losses.
Evaluationresultsdemonstrate AraBERTv0.2-base achiev-
ing the highest average F-score (Table 8) and DeBERTaV3-
base attaining the top EM score for extractive QA across 10
validation folds. For generative QA (Table 9), AraBART out-
performs other models on both word-based and embedding-
based metrics.
6.3 Duplicate detection/semantic similarity
For semantic similarity tasks (DQD and DAD), we ﬁne-tuned
models 1–10 (Section 6) as cross-encoders with sequence
classiﬁcation heads. Training used an Nvidia RTX 4090
GPU (24GB memory) with a 2e-5 learning rate (AdamW
optimizer) and 10-fold cross-validation. Complete hyperpa-
rameters appear in Table 7, with training dynamics in Fig. 4.
Training loss trends showed successful learning across
5 epochs for most models. Arabic-BERT-base performed
best on DQD, while CAMeLBERT-MSA led on DAD.
AraBERTv2-large, XLM-V-base, and XLM-RoBERTa-base
exhibited higher ﬁnal losses.
Evaluation results (Tables 10–11) show AraBERTv0.2-
base achieving top precision, accuracy, and F1 for DQD, with
AraBERTv0.2-large leading in recall. For DAD, AraBERT-
123
 135 
Page 18 of 28

--- Page 19 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
Fig. 3 Training dynamics for: (a) MRC-Ex, and (b) MRC-Gen
v0.2-base attained highest recall and average precision, while
AraBERTv0.2-large performed best overall in accuracy, pre-
cision, and F1. The narrow standard deviation (SD) indicates
comparable performance across models.
6.4 Error analysis
Given the suboptimal MRC performance in both generative
and extractive approaches, we conducted an error analysis
on 50 samples from the top-performing ﬁne-tuned models
on the MRC-Gen and MRC-Ex tasks. Errors were deﬁned as
predictions scoring 0 in exact match after normalization. We
identiﬁed seven error categories:
Partial Answers. Correct but incomplete responses missing
key details.
Extraneous Answers. Accurate answers containing unnec-
essary content (Qur’anic verses, Hadith, or redundant infor-
mation).
Paraphrased Answers. Semantically correct responses but
rephrase the reference answer. These are classiﬁed as errors
due to the nature of the lexical matching metrics used.
Enhanced Answers. Responses more comprehensive or pre-
cise than references.
Conﬂicting Answers. Direct contradictions of reference
answers, representing the most problematic errors as they
often provide false or misleading information.
Irrelevant Answers. Completely unrelated responses that
undermine user trust.
Disﬂuent Answers. Grammatically or structurally ﬂawed
outputs, primarily occurring in generative tasks (extractive
answers maintain source text ﬂuency).
The error analysis in Fig. 5 shows that 72% of extractive
QA answers marked incorrect (including enhanced, para-
phrased, and extraneous categories) are factually correct,
Table 8 Results for large language models (LLMs) on extractive
question answering using the HajjFatwa MRC (extractive) dataset,
employing a 10-fold cross-validation (CV) approach. The models are
categorized into Arabic and multilingual groups. We report the EM
(Exact Match) and F1 scores, along with their respective standard devi-
ations (SD) which reﬂect variations across the folds. Average scores for
each category are provided
Model name
EM ± SD
F1 ± SD
avg EM
avg F1
Arabic
Arabic-BERT-base
24.11 ± 3.72
69.83 ± 3.58
AraELECTRA-base-discriminator
26.71 ± 3.96
71.81 ± 3.19
AraBERTv0.2-base
26.13 ± 3.84
72.78 ± 1.68
AraBERTv2-base
26.23 ± 3.69
70.15 ± 2.52
AraBERTv0.2-large
22.11 ± 3.6
68.83 ± 1.98
23.69 ± 4.53
69.04 ± 4.57
AraBERTv2-large
14.03 ± 12.37
55.67 ± 19.95
CAMeLBERT-MSA
23.04 ± 3.34
70.07 ± 2.45
ARBERTv2
27.08 ± 3.55
71.85 ± 3.25
MARBERTv2
23.76 ± 2.66
70.36 ± 2.58
Multiling.
BERT-multilingual-base-cased
23.72 ± 3.31
68.47 ± 3.45
DistilBERT-base-multilingual-cased
22.71 ± 4.57
66.27 ± 4.41
XLM-RoBERTa-base
24.94 ± 3.52
69.58 ± 3.36
24.96 ± 3.79
69.25 ± 3.5
XLM-V-base
25.80 ± 4.03
71.06 ± 3.2
DeBERTaV3-base
27.65 ± 3.51
70.86 ± 3.09
⎫
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎬
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎭
⎫
⎪⎪⎪⎬
⎪⎪⎪⎭
123
Page 19 of 28 
135

--- Page 20 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
Table 9 Results for LLMs on generative question answering using the HajjFatwa MRC (generative) dataset, employing a 10-fold CV approach. The SD is reported for the word-base and
embedding-base metrics to indicate variability across the folds. For BERTScore calculations, bert-base-multilingual-cased model was used for token embeddings
Model
F1
BLEU-2
BLEU-3
ROUGE-1
ROUGE-2
ROUGE-L
BERT-P
BERT-R
BERT-F
Arabic
Arabic-T5-small
16.48 ± 1.74
5.25 ± 1.67
2.29 ± 1.29
15.84 ± 1.74
4.7 ± 1.62
14.57 ± 1.75
69.5 ± 1.28
69.03 ± 1.46
69.17 ± 0.92
BERT2bert
4.54 ± 4.51
0.48 ± 1.28
0.11 ± 0.31
4.33 ± 4.27
0.41 ± 0.96
4.19 ± 4.01
38.16 ± 22.1
34.53 ± 20.2
36.2 ± 21.04
Transformer
11.11 ± 1.89
2.21 ± 0.93
0.69 ± 0.52
10.75 ± 1.84
1.78 ± 0.76
9.69 ± 1.73
68.11 ± 0.49
68.27 ± 1.05
68.14 ± 0.66
AraBART
19.94 ± 2.9
7.12 ± 2.26
3.43 ± 2.09
19.31 ± 2.82
6.73 ± 2.68
17.44 ± 2.93
71.86 ± 1.17
71.14 ± 1.22
71.4 ± 0.87
AraT5-base
11.48 ± 3.69
1.86 ± 1.27
0.48 ± 0.52
11.27 ± 3.62
2.15 ± 1.22
10.6 ± 3.38
70.47 ± 1.52
64.57 ± 3.66
67.29 ± 2.72
AraT5-MSA-base
7.88 ± 2.43
0.44 ± 0.49
0.03 ± 0.03
7.79 ± 2.47
0.73 ± 0.67
7.52 ± 2.34
68.89 ± 4.58
61.95 ± 5.69
65.16 ± 5.22
Average
11.9 ± 2.86
2.89 ± 1.31
1.17 ± 0.79
11.55 ± 2.79
2.75 ± 1.32
10.67 ± 2.69
64.5 ± 5.19
61.58 ± 5.55
62.89 ± 5.24
Multi.
mT5-base_ar
17.38 ± 2.56
6.3 ± 1.75
3.17 ± 1.73
16.52 ± 2.31
5.74 ± 2.38
15.31 ± 2.37
68.95 ± 1.63
69.32 ± 1.13
69.04 ± 0.78
mT5-base
15.91 ± 2.82
5.01 ± 1.81
2.37 ± 1.36
15.17 ± 2.63
4.82 ± 2.34
14.2 ± 2.26
69.21 ± 1.41
68.46 ± 1.66
68.73 ± 1.02
mT5-small
15.41 ± 2.06
4.59 ± 1.48
1.99 ± 1.3
14.67 ± 1.85
4.77 ± 2
13.91 ± 1.99
69.23 ± 1.78
67.42 ± 0.96
68.19 ± 0.88
Average
16.23 ± 2.48
5.3 ± 1.68
2.51 ± 1.46
15.46 ± 2.26
5.11 ± 2.24
14.48 ± 2.21
69.13 ± 1.61
68.4 ± 1.25
68.66 ± 0.89
123
 135 
Page 20 of 28

--- Page 21 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
Fig. 4 Training dynamics for: (a) DQD, and (b) DAD
demonstrating the limitations of EM for evaluation. Incom-
plete answers account for 28% of errors, revealing model
comprehension gaps. While no conﬂicting or irrelevant
answers appeared in our sample, their potential occurrence
remains.
For generative QA, 60% of ﬂagged errors contain cor-
rect information, with 12% surpassing human comprehen-
sion quality - suggesting opportunities for model feedback
systems. However, 40% represent irrelevant or conﬂict-
ing responses, indicating fundamental failures in question
and context understanding. This is particularly critical for
Islamic legal applications where accuracy is paramount.
Additionally, 28% of generated answers exhibit ﬂuency
issues, compromising output quality.
6.5 Discussion
After training several models on machine reading com-
prehension (MRC) and duplicate detection and analyzing
the outcomes, we arrived at several key conclusions. We
observed a clear necessity for domain-speciﬁc training
datasets. Open-domain datasets have a fundamentally dif-
ferent nature, and relying on them for training results in less
accurate outcomes.
To explore this further, we analyzed the performance
of AraElectra on the FatawaQA-extractive dataset, utilizing
only the test data. This model, originally trained on the open-
domain tydiQA dataset (Arabic section), achieved an EM
Table 10 Results for testing LLMs on the duplicate question detection (DQD) task using the HajjFatwa SQS dataset utilizing a 10-fold CV method.
The reported SD reﬂect the variability across the folds
Model
toptimal
Acc
F1
P
R
avgP
Arabic
Arabic-BERT-base
53.42
97.44 ± 0.1
98.69 ± 0.05
98.69 ± 0.05
98.69 ± 0.05
98.55 ± 1.1
AraELECTRA-base-discriminator
73.72
97.58 ± 0.4
98.76 ± 0.2
98.83 ± 0.42
98.69 ± 0.06
98.85 ± 0.79
AraBERTv0.2-base
61.55
97.74 ± 0.51
98.84 ± 0.26
98.98 ± 0.54
98.71 ± 0.02
99.19 ± 0.52
AraBERTv2-base
46.48
97.46 ± 0.46
98.7 ± 0.24
98.76 ± 0.45
98.63 ± 0.1
97.7 ± 1.85
AraBERTv0.2-large
68.62
97.5 ± 0.06
98.72 ± 0.03
98.72 ± 0.03
98.72 ± 0.03
99.19 ± 0.57
AraBERTv2-large
30.27
97.3 ± 0.89
98.61 ± 0.47
98.67 ± 0.61
98.55 ± 0.4
95.76 ± 7.29
CAMeLBERT-MSA
70.71
97.71 ± 0.54
98.83 ± 0.28
98.96 ± 0.55
98.7 ± 0.05
98.95 ± 0.76
ARBERTv2
66.66
97.74 ± 0.53
98.84 ± 0.27
98.97 ± 0.54
98.72 ± 0.03
99.17 ± 0.59
MARBERTv2
53.9
97.42 ± 0.06
98.68 ± 0.03
98.68 ± 0.03
98.68 ± 0.03
98.03 ± 0.83
Average
58.37
97.54 ± 0.39
98.74 ± 0.21
98.81 ± 0.36
98.68 ± 0.09
98.38 ± 1.59
Multiling.
BERT-multilingual-base-cased
80.66
97.73 ± 0.65
98.84 ± 0.33
99.04 ± 0.66
98.63 ± 0.06
98.23 ± 1.31
DistilBERT-base-multilingual-cased
79.53
97.49 ± 0.63
98.71 ± 0.33
98.84 ± 0.61
98.57 ± 0.07
97.13 ± 1.34
XLM-RoBERTa-base
57.32
97.41 ± 0.12
98.67 ± 0.06
98.67 ± 0.06
98.67 ± 0.06
98.17 ± 1.22
XLM-V-base
79.7
97.32 ± 0.16
98.63 ± 0.08
98.63 ± 0.08
98.63 ± 0.08
97.32 ± 2.04
DeBERTaV3-base
96.12
97.69 ± 0.54
98.82 ± 0.28
98.95 ± 0.56
98.69 ± 0.04
98.9 ± 0.9
Average
78.67
97.53 ± 0.42
98.73 ± 0.22
98.83 ± 0.39
98.64 ± 0.06
97.95 ± 1.36
123
Page 21 of 28 
135

--- Page 22 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
Table 11 Results for testing LLMs on the duplicate answer detection (DAD) task using the HajjFatwa SAS dataset, with SD reported for each
metric
Model
toptimal
Acc
F1
P
R
avgP
Arabic
Arabic-BERT-base
49.2
97.51 ± 0.08
98.72 ± 0.04
98.72 ± 0.04
98.72 ± 0.04
98.75 ± 1.09
AraELECTRA-base-discriminator
79.3
97.58 ± 0.4
98.76 ± 0.21
98.82 ± 0.41
98.69 ± 0.02
98.58 ± 1.27
AraBERTv0.2-base
47.75
97.63 ± 0.4
98.78 ± 0.21
98.85 ± 0.41
98.72 ± 0.03
99.26 ± 0.72
AraBERTv2-base
71.81
97.55 ± 0.43
98.74 ± 0.22
98.81 ± 0.43
98.68 ± 0.07
98.39 ± 1.15
AraBERTv0.2-large
73.09
97.97 ± 0.66
98.96 ± 0.34
99.22 ± 0.67
98.7 ± 0.04
99.04 ± 0.96
AraBERTv2-large
65.5
97.14 ± 0.9
98.52 ± 0.49
98.52 ± 0.49
98.52 ± 0.49
94.18 ± 12.16
CAMeLBERT-MSA
66.76
97.61 ± 0.4
98.77 ± 0.21
98.84 ± 0.41
98.71 ± 0.02
99.12 ± 0.63
ARBERTv2
79.2
97.47 ± 0.1
98.7 ± 0.05
98.7 ± 0.05
98.7 ± 0.05
99.11 ± 0.85
MARBERTv2
76.65
97.51 ± 0.42
98.72 ± 0.22
98.79 ± 0.43
98.66 ± 0.06
98.05 ± 1.53
Average
67.7
97.55 ± 0.42
98.74 ± 0.22
98.81 ± 0.37
98.68 ± 0.09
98.28 ± 2.26
Multiling.
BERT-multilingual-base-cased
78.61
97.53 ± 0.42
98.73 ± 0.22
98.8 ± 0.43
98.66 ± 0.09
98.19 ± 1.46
DistilBERT-base-multilingual-cased
68.61
97.2 ± 0.17
98.56 ± 0.09
98.56 ± 0.09
98.56 ± 0.09
95.19 ± 2.7
XLM-RoBERTa-base
67.31
97.43 ± 0.12
98.68 ± 0.06
98.68 ± 0.06
98.68 ± 0.06
97.67 ± 1.67
XLM-V-base
52.03
97.42 ± 0.13
98.68 ± 0.07
98.68 ± 0.07
98.68 ± 0.07
97.06 ± 1.86
DeBERTaV3-base
78.97
97.71 ± 0.53
98.83 ± 0.27
98.96 ± 0.55
98.7 ± 0.04
98.5 ± 1.47
Average
69.1
97.46 ± 0.27
98.7 ± 0.14
98.74 ± 0.24
98.66 ± 0.07
97.32 ± 1.83
score of 74.91 and an F-score of 86.68 (Antoun et al. 2021).
The performance of other models in this study is presented
in Table 12. However, when evaluated on the FatawaQA-
extractive dataset, it obtained signiﬁcantly lower scores, with
an EM of 6.69 and an F-score of 31.62. This stark con-
trast highlights the unique characteristics of the Fatawa QA
data, which differ substantially from those encountered in
open-domain QA datasets. Consequently, it underscores the
importanceofutilizingclose-domainQAdatasetsforspeciﬁc
tasks, such as those in Fatwa, Medical, or Legal contexts.
The training dynamics for DQD and DAD revealed
consistently strong performance from Arabic-speciﬁc pre-
trained models (CAMeLBERT-MSA, Arabic-BERT-base,
AraBERTv0.2-base, ARBERTv2), which achieved the low-
est ﬁnal training loss in both tasks. The marginally lower ﬁnal
loss values in DAD suggest it may present a slightly easier
learning problem than DQD.
For MRC, extractive models showed consistent convergence,
though larger variants (AraBERTv0.2-large, AraBERTv2-
large) exhibited higher ﬁnal loss than their base versions,
indicating potential need for extended training or more
data. AraBERTv0.2-large displayed particular instability,
suggesting requirement for reﬁned hyperparameter tuning.
Performance clustering appeared tighter among top MRC-
Ex models compared to the clearer separation in MRC-Gen
Fig. 5 Answer error distribution for: (a) AraBERTV0.2 MRC-Ex, and (b) AraBART MRC-Gen
123
 135 
Page 22 of 28

--- Page 23 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
Table 12 Model performance comparison on TyDiQA dataset (from
Antoun et al. 2021)
Model
EM
F-score
AraBERTv0.1
68.51
82.86
AraBERTv0.2-base
73.07
85.41
AraBERTv0.2-large
73.72
86.03
Arabic-BERT-base
67.42
81.24
Arabic-BERT-large
70.03
84.12
Arabic-ALBERT-base
67.10
80.98
Arabic-ALBERT-large
68.07
81.59
Arabic-ALBERT-xlarge
71.12
84.59
ARBERT
71.55
83.69
AraELECTRA
74.91
86.68
results, with extractive tasks showing generally higher ﬁnal
loss values than generative ones.
From the evaluation results we did not observe a distinct
advantage for models pre-trained exclusively on Arabic data
across most of the evaluated tasks. This tendency could be an
evidence that either the Arabic language has not received suf-
ﬁcient effort in the NLP ﬁeld, or it may indicate the progress
of cross-lingual and transfer learning in multilingual lan-
guage models.
Tables 8–9 present the results for the MRC tasks, showing
variability in model performance across different folds and
highlighting room for improvement. This variability can be
attributed to the inherent complexity of MRC tasks in the
Fatwa domain, which may require larger datasets and more
robust models to achieve effective convergence.
Furthermore, the evaluation metrics currently used—
F-score, ROUGE, and BLEU—are primarily designed to
measure word overlap. While these metrics are suitable for
extractive tasks, they are less effective for generative tasks.
Although BERTScore demonstrates a strong correlation with
human evaluation, it has notable limitations: it focuses heav-
ily on the semantic similarity of answer tokens without
adequately considering the question and context. Addition-
ally, BERTScore can be biased towards models with similar
architectures and does not account for the syntactic structure
of the answer during evaluation.
The overall outcomes of the duplicate detection tasks
(Tables 10–11) are highly satisfactory across most models,
demonstrating that the cross-encoder architecture effectively
captures sentence semantics.Moreover, the narrow variance
in results across different folds, as reﬂected by the small SD,
suggests consistent performance by the models (except for
AraBERTv2-large).
AraBERTv0.2 achieves better results in Arabic Machine
Reading Comprehension than other basic BERT models,
likely because it was trained on a much larger (77GB) Mod-
ern Standard Arabic (MSA) text collection. This extensive
training enabled it to develop more detailed and subtle under-
standings of the language compared to the training data
sizes of CAMeLBERT (54GB), MARBERT (61GB), and
ARBERT (61GB) for MSA. Additionally, a key difference is
that AraBERTv0.2 does not rely on explicit pre-segmentation
using tools like Farasa, unlike other AraBERT versions (1
and 2). This might lead to better handling of unseen or less
standard forms of words that could be segmented incorrectly
by an external tool, especially when applied to downstream
closed-domain tasks with speciﬁc terms. For the generative
MRC,it’s noteworthy that AraBART achieved superior per-
formance compared to other models, despite being smaller
than almost all of them, with the exception of the transformer
model. This observation reinforces our earlier point that
smaller models can sometimes converge more quickly and
be preferable when dealing with smaller datasets. Moreover,
our ﬁndings align with another research (Masri et al. 2024)
indicating that AraBART outperforms models like AraT5,
mT5, and mBART in summarization tasks. This is particu-
larly relevant as summarization shares similarities with the
generative answering task in terms of requiring comprehen-
sion and the ability to capture subtle nuances.
The evaluation results across all models trained for MRC-
extractive (Table 8), duplicate question detection DQD
(Table 10), and duplicate answer detection DAD (Table 11)
reveal inconsistent performance in AraBERTv2-large. This
instability is evidenced by wide metric variations and high
standard deviation values. The training dynamics shown in
Figs. 3 and 4 further demonstrate distinct learning patterns
for AraBERTv2-large and AraBERTv0.2-large in MRC-
extractive and DAD tasks. Both models exhibit higher ﬁnal
training loss compared to others, indicating convergence
difﬁculties, with AraBERTv0.2-large showing particularly
ﬂuctuating learning behavior.
This unstable performance with high standard deviation,
particularly observed in AraBERTv2-large and AraBERT-
v0.2-large, stems from several factors related to training
large language models on closed-domain datasets. Existing
research (Alsubhi et al. 2021) shows AraBERT base models
often outperform larger versions on smaller datasets (e.g.,
ARCED and AQAD), while larger models excel on extensive
datasets (e.g., Arabic-SQuAD and TyDiQA-Arabic). This
suggests larger models require substantially more data to
achieve stable convergence and generalization. When trained
on limited data, they become prone to overﬁtting and learning
spurious patterns rather than robust representations.
Additional contributing factors may include Deep Neural
Networks’ inherent challenges, where larger architectures
face increased risks of vanishing or exploding gradients
during training. Suboptimal hyperparameter conﬁgurations,
while suitable for base models, may further exacerbate insta-
bility in larger models. The complex parameter space of
these models also makes locating global minima more dif-
123
Page 23 of 28 
135

--- Page 24 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
ﬁcult, increasing the likelihood of settling in suboptimal
local minima. These ﬁndings underscore the need for dataset
expansion and precise hyperparameter optimization to fully
realize the potential of larger models in this domain.
It is common for MRC tasks to exhibit lower and more
inconsistent performance compared to semantic similarity
tasks. This performance gap stems from MRC’s inherent
complexity, which requires deep understanding of context
passages, questions, word relationships, and reasoning. The
challenge is compounded by longer input sequences (con-
text) and potential noise in the data, making accurate answer
extraction difﬁcult.
In contrast, semantic similarity tasks measure the relat-
edness between text pairs of comparable length - typically
shorter than MRC contexts. While still requiring seman-
tic understanding, these tasks don’t demand the same level
of comprehension and reasoning as MRC. This difference
is particularly pronounced in Arabic, a linguistically rich
language, and with complex question types like composed
questions in our dataset.
The evaluation processes further highlight these differ-
ences. MRC outputs text spans or generated answers, where
lexical metrics impose strict penalties for minor deviations.
Semantic similarity, however, produces continuous scores
based on sentence embeddings, capturing meaning beyond
lexical matching. This allows recognition of semantic equiv-
alence even with synonym variation.
Duplicate detection represents a special case of semantic
similarity with simpliﬁed requirements. As a binary classi-
ﬁcation task, it only needs to distinguish between duplicate
(a score of 1) and non-duplicate (a score of 0) pairs. This
clear distinction facilitates threshold optimization. The task
primarily requires correct ranking of pairs rather than precise
similarity scoring, contributing to its stronger performance.
7 Conclusion
Recentadvancesindeeplearninghavecreatedtransformative
opportunities for intelligent systems to support religious ser-
vices, particularly in addressing Hajj-related fatwas—non-
binding Islamic legal opinions issued by qualiﬁed scholars
(muftis) during the annual pilgrimage, when millions of pil-
grims seek accurate and timely guidance. While the demand
for such services is substantial, progress has been hindered
by the absence of specialized Arabic-language resources tai-
lored to this unique domain.
This study addresses this critical gap through the cre-
ation of Hajj-FQA, a high-quality, closed-domain Arabic
dataset speciﬁcally designed for fatwa question answering
during Hajj. The dataset captures the distinctive linguistic
patterns, jurisprudential nuances, and contextual elements
characteristic of pilgrims’ inquiries. Through comprehen-
sive quantitative validation—examining question structures,
lexical patterns, and task-speciﬁc benchmarks—we have
demonstrated Hajj-FQA’s utility as a foundation for devel-
oping accurate and reliable QA systems.
The implications of this work extend across multiple
dimensions. For pilgrims, this research enables the devel-
opment of assistive technologies that provide trustworthy
guidance during time-sensitive rituals, helping to ensure
proper observance while enhancing the spiritual experience
of Hajj. For religious institutions, it offers a framework for
scalable solutions capable of handling large volumes of rou-
tine inquiries, allowing scholars to focus on more complex
or nuanced issues. From a technical perspective, this work
advances Arabic natural language processing in high-stakes,
domain-speciﬁc applications and supports the development
of context-aware QA systems and multilingual support tools.
Looking ahead, we propose the following recommenda-
tions and future research directions:
Dataset expansion using LLMs. The demonstrated capabil-
ities of LLMs (GPT, Gemini, Llama, DeepSeek) in Arabic
text generation (Alsulami and Almansour 2025) suggest their
potential for expanding fatwa datasets through zero-shot and
few-shot learning, which could achieve quality comparable
to human paraphrasing.
Addressing data skew via deep learning. To mitigate
the observed imbalance in question types (particularly for
“Why,” “Who,” and “Where” questions), targeted data aug-
mentation using deep learning techniques should be investi-
gated to generate more representative samples.
Improving dataset robustness. Enhancing the dataset’s
practicalutilityrequiresincorporatingchallengingcasessuch
as unanswerable questions and hard duplicates. A hybrid
human-AI approach would ensure quality while maintain-
ing jurisprudential accuracy.
Multilingual and multidomain expansion. The dataset
should be extended to cover broader Islamic topics using
approved scholarly sources. Machine translation could inc-
rease accessibility for non-Arabic speakers while maintain-
ing theological precision through expert validation.
Arabic-speciﬁc generative QA evaluation. Current eval-
uation frameworks inadequately address Arabic generative
QA. New metrics should be developed, informed by success-
ful LLM-based approaches in English QA (Fu et al. 2023;
Abdel Azim et al. 2025; Alhawasi and Youssef 2024), while
accounting for Arabic’s linguistic and religious nuances.
Efﬁcient model benchmarking. Continued evaluation of
distilled/smaller LLMs (Llama, Mistral, DeepSeek) is war-
ranted given their near-human performance and potential for
resource-efﬁcient deployment.
123
 135 
Page 24 of 28

--- Page 25 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
Deployment optimization. Future work should compare
deployment strategies (edge vs. cloud-based) for QA sys-
tems, with particular attention to scalability during peak
demand periods like Hajj. Model distillation techniques
should be explored for portable devices, alongside systems
for real-time query management.
Funding The authors would like to thank Ongoing Research Funding
Program, (ORFFT-2025-006-1), King Saud University, Riyadh, Saudi
Arabia for ﬁnancial support.
Data Availability The dataset is available upon request through direct
email.
Declarations
Conﬂict of Interest The authors declare that they have no conﬂict of
interest.
Ethical approval This article does not contain any studies with human
participants or animals performed by the authors.
Open Access This article is licensed under a Creative Commons
Attribution-NonCommercial-NoDerivatives 4.0 International License,
which permits any non-commercial use, sharing, distribution and repro-
duction in any medium or format, as long as you give appropriate credit
to the original author(s) and the source, provide a link to the Creative
Commons licence, and indicate if you modiﬁed the licensed mate-
rial. You do not have permission under this licence to share adapted
material derived from this article or parts of it. The images or other
third party material in this article are included in the article’s Creative
Commons licence, unless indicated otherwise in a credit line to the
material. If material is not included in the article’s Creative Commons
licence and your intended use is not permitted by statutory regula-
tion or exceeds the permitted use, you will need to obtain permission
directly from the copyright holder. To view a copy of this licence, visit
http://creativecommons.org/licenses/by-nc-nd/4.0/.
References
Abdallah A, Kasem M, Abdalla M, Mahmoud M, Elkasaby M,
Elbendary Y et al (2024) ArabicaQA: A Comprehensive Dataset
for Arabic Question Answering. In: Proceedings of the 47th Inter-
national ACM SIGIR Conference on Research and Development
in Information Retrieval, pp 2049–2059
Abdel Azim H, Waheed MT, Mohammed A (2025) Large language
models-based metric for generative question answering systems.
IAES Intern J Artif Intel (IJ-AI) 14(1):152–161
Abdelaziz N, Elsayed E, El-Sayed M (2021) FAAQA-QAD: A Fre-
quently Asked Arabic Question Answering Dataset for Diseases
DetectionSystem.In:Proceedingsofthe12thLanguageResources
and Evaluation Conference, pp 3109–3116
Abdul-Mageed M, Elmadany A, Nagoudi EMB (2021) ARBERT &
MARBERT: Deep Bidirectional Transformers for Arabic. In: Zong
C, Xia F, Li W, Navigli R (eds) Proceedings of the 59th Annual
Meeting of the Association for Computational Linguistics and
the 11th International Joint Conference on Natural Language
Processing (Volume 1: Long Papers). Online: Association for
Computational Linguistics, pp 7088–7105
Adamopoulou E, Moussiades L (2020a) Chatbots: History, technology,
and applications. Mach Learn Appl 2:100006
Adamopoulou E, Moussiades L (2020b) An Overview of Chatbot Tech-
nology. In: Maglogiannis I, Iliadis L, Pimenidis E (eds) Artiﬁcial
Intelligence Applications and Innovations. Springer International
Publishing, Cham, pp 373–383
Akour M, Abufardeh S, Magel K, Al-Radaideh Q (2011) QArabPro: A
rule based question answering system for reading comprehension
tests in Arabic. Am J Appl Sci 8(6):652–661
Alami H, El Mahdaouy A, Benlahbib N, En-Nahnahi N, Berrada I,
Alaoui Ouatik SE (2023) DAQAS: Deep Arabic Question Answer-
ing System based on duplicate question detection and machine
reading comprehension. J King Saud Univ - Comput Inf Sci
35(8):101709
Albilali E, Al-Twairesh N, Hosny M (2022) Constructing Arabic
Reading Comprehension Datasets: Arabic WikiReading and Kai-
fLematha. Lang Res Eval 56(3):729–764
Alhawasi H, Youssef A (2024) Using LLMs for Evaluating QA Sys-
tems: Exploration and Assessment. In: 2024 2nd International
Conference on Foundation and Large Language Models (FLLM),
pp 462–469
AlmansorEH,HussainFK(2020)SurveyonIntelligentChatbots:State-
of-the-Art and Future Research Directions. In: Barolli L, Hussain
FK, Ikeda M (eds) Complex, Intelligent, and Software Intensive
Systems. Springer International Publishing, Cham, pp 534–543
Almazrouei E et al (2023) The Falcon Series of Open Language Models.
arxiv:2311.16867
Almuzaini HA, Azmi AM (2022) An unsupervised annotation of Ara-
bic texts using multi-label topic modeling and genetic algorithm.
Expert Syst Appl 203:117384
Alrowili S, Vijay-Shanker K (2023) ArTrivia: Harvesting Arabic
Wikipedia to Build A New Arabic Question Answering Dataset.
Proceedings of ArabicNLP 2023:191–207
AlruqiTN,AlzahraniSM(2023)EvaluationofanArabicChatbotBased
on Extractive Question-Answering Transfer Learning and Lan-
guage Transformers. AI 4(3):667–691
Al-Shameri N, Al-Khalifa H (2024) Arabic paraphrased parallel syn-
thetic dataset. Data Brief 57:111004
Alsheddi AS, Alhenaki LS (2022) English and Arabic Chatbots:
A Systematic Literature Review. Int J Adv Comput Sci Appl
13(8):662–675
Alsubhi K, Jamal A, Alhothali A (2021) Pre-trained transformer-based
approach for arabic question answering: A comparative study.
arXiv preprint arxiv:2111.05671
Alsulami HR, Almansour AA (2025) Exploring GPT-4 Capabilities in
Generating Paraphrased Sentences for the Arabic Language. Appl
Sci 15(8):4139
Al-Thanyyan SS, Azmi AM (2023) Simpliﬁcation of Arabic text: A
hybrid approach integrating machine translation and transformer-
based lexical model. J King Saud Univ-Comput Inf Sci
35(8):101662
Alwaneen TH (2024) Azmi AM (2024) Stacked dynamic memory-
coattention network for answering why-questions in Arabic.
Neural Comput Appl 36:8867–8883
Alwaneen TH, Azmi AM, Aboalsamh HA, Cambria E, Hussain A
(2022) Arabic question answering system: A survey. Artif Intell
Rev 55(1):207–253
Antoun W, Baly F, Hajj H (2020) AraBERT: Transformer-based Model
for Arabic Language Understanding. In: Proceedings of the 4th
Workshop on Open-Source Arabic Corpora and Processing Tools
(LREC 2020), pp 9–15
Antoun W, Baly F, Hajj H (2021) AraELECTRA: Pre-Training Text
Discriminators for Arabic Language Understanding. In: Proceed-
ings of the Sixth Arabic Natural Language Processing Workshop.
Kyiv, Ukraine (Virtual): Association for Computational Linguis-
tics, pp 191–195
123
Page 25 of 28 
135

--- Page 26 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
Artetxe M, Ruder S, Yogatama D (2020) On the Cross-lingual Trans-
ferability of Monolingual Representations. In: Jurafsky D, Chai
J, Schluter N, Tetreault J (eds) Proceedings of the 58th Annual
Meeting of the Association for Computational Linguistics. Online:
Association for Computational Linguistics, pp 4623–4637
Atef A, Mattar B, Sherif S, Elrefai E, Torki M (2020) AQAD: 17,000+
Arabic questions for machine comprehension of text. In 2020
IEEE/ACS 17th International Conference on Computer Systems
and Applications (AICCSA), pp 1–6
Azmi AM, AlShenaiﬁN (2014) Handling “why” questions in Arabic.
In: Proceedings of the Fifth International Conference on Arabic
Language Processing (CITALA 2014)
Azmi AM, AlshenaiﬁNA (2016) Answering Arabic why-questions:
Baseline vs. RST-based approach. ACM Trans Inf Syst (TOIS)
35(1):1–19
Azmi AM, AlshenaiﬁNA (2017) LEMAZA: An Arabic why-question
answering system. Nat Lang Eng 23(6):877–903
Azmi AM, Al-Qabbany AO, Hussain A (2019) Computational and natu-
rallanguageprocessingbasedstudiesofhadithliterature:Asurvey.
Artif Intell Rev 52(2):1369–1414
Banerjee S, Lavie A (2005) METEOR: An automatic metric for MT
evaluation with improved correlation with human judgments. In:
Proceedings of the acl workshop on intrinsic and extrinsic evalu-
ation of machine translation and/or summarization, pp 65–72
Bani-Almarjeh M, Kurdy MB (2023) Arabic abstractive text summa-
rization using RNN-based and transformer-based architectures. Inf
Process Manag 60(2):103227
Bari MS, Alnumay Y, Alzahrani NA, Alotaibi NM, Alyahya HA,
AlRashed S et al (2024) ALLaM: Large Language Models for
Arabic and English. arXiv preprint arxiv:2407.15390
Bashir MH, Azmi AM, Nawaz H, Zaghouani W, Diab M, Al-Fuqaha
A et al (2023) Arabic natural language processing for Qur’anic
research: A systematic review. Artif Intell Rev 56(7):6801–6854
Bayan Kmainasi M, Ezzat Shahroor A, Al-Ghraibah A (2025) Can
Large Language Models Predict the Outcome of Judicial Deci-
sions? arXiv e-prints, p. arXiv–2501
Biltawi MM, Awajan A, Tedmori S (2023) Arabic Span Extraction-
based Reading Comprehension Benchmark (ASER) and Neural
Baseline Models. ACM Trans Asian Low-Resour Lang Inf Process
22(5):127:1–127:29
Biltawi MM, Tedmori S, Awajan A (2021) Arabic Question Answering
Systems: Gap Analysis. IEEE Access 9:63876–63904
Bojanowski P, Grave E, Joulin A, Mikolov T (2017) Enriching Word
Vectors with Subword Information. Trans Assoc Comput Linguist
5:135–146
Chen M, Tworek J, Jun H, Yuan Q, Pinto HPDO, Kaplan J et al
(2021) Evaluating Large Language Models Trained on Code.
arxiv:2107.03374
Clark JH et al (2020) TyDi QA: A Benchmark for Information-Seeking
Question Answering in Typologically Diverse Languages. In:
Jurafsky D, Chai J, Schluter N, Tetreault J (eds) Proceedings of
the 58th Annual Meeting of the Association for Computational
Linguistics. arxiv:2003.05002
Conneau A, Khandelwal K, Goyal N, Chaudhary V, Wenzek G, Guzmán
F, et al (2020) Unsupervised Cross-lingual Representation Learn-
ing at Scale. In: Proceedings of the 58th Annual Meeting of the
Association for Computational Linguistics, pp 8440–8451
Devlin J, Chang MW, Lee K, Toutanova K (2019) BERT: Pre-training
of deep bidirectional transformers for language understanding. In:
Proceedings of the 2019 conference of the North American chapter
of the association for computational linguistics: human language
technologies, volume 1 (long and short papers), pp 4171–4186
Fuad A, Al-Yahya M (2022) Recent Developments in Arabic Conver-
sational AI: A Literature Review. IEEE Access 10:23842–23859
Fu L, Yan P, Peng Y, Zeng S, Lin X, Zhou W (2023) Gpt-score: Evaluate
as you desire. arXiv preprint arXiv:2305.04353
Hammo B, Abu-Salem H, Lytinen SL, Evens M (2002) QARAB:
A: Question answering system to support the Arabic language.
In: Proceedings of the ACL-02 workshop on Computational
approaches to semitic languages
Hamza A, Alaoui Ouatik SE, Zidani KA, En-Nahnahi N (2022) Arabic
duplicate questions detection based on contextual representation,
class label matching, and structured self attention. J King Saud
Univ - Comput Inf Sci 34(6, Part B):3758–3765
He P, Gao J, Chen W (2023) DeBERTaV3: Improving DeBERTa
using ELECTRA-Style Pre-Training with Gradient-Disentangled
Embedding Sharing. arxiv:2111.09543
He P, Liu X, Gao J, Chen W (2021) DeBERTa: Decoding-enhanced
BERT with Disentangled Attention. arxiv:2006.03654
Huang H, Yu F, Zhu J, Sun X, Cheng H, Dingjie S et al (2024)
AceGPT, Localizing Large Language Models in Arabic. In: Pro-
ceedings of the 2024 Conference of the North American Chapter of
the Association for Computational Linguistics: Human Language
Technologies (Volume 1: Long Papers), pp 8139–8163
Hussain S, Ameri Sianaki O, Ababneh N (2019) A Survey on Conver-
sational Agents/Chatbots Classiﬁcation and Design Techniques.
In: Barolli L, Takizawa M, Xhafa F, Enokido T (eds) Web, Artiﬁ-
cial Intelligence and Network Applications. Springer International
Publishing, Cham, pp 946–956
Ibrahim B, Ariﬁn M, Abd Rashid SZ.: The Role of Fatwa and Mufti in
Contemporary Muslim Society. https://www.openurl.ebsco.com/
contentitem/
Inoue G, Alhafni B, Baimukan N, Bouamor H, Habash N (2021) The
Interplay of Variant, Size, and Task Type in Arabic Pre-trained
Language Models. arxiv:2103.06678
Ismail WS, Homsi MN. DAWQAS: A Dataset for Arabic Why Question
Answering System. In: Shaalan K, ElBeltagy SR, editors. Arabic
Computational Linguistics. vol. 142 of Procedia Computer Sci-
ence. Amsterdam: Elsevier Science Bv; 2018. p. 123–131
Kahil N (2024) Inside Qatar’s AI project that aims to preserve the Arabic
language. Wired
Khallaf N, Sharoff S, Soliman R (2022) Towards Arabic Sentence
Simpliﬁcation via Classiﬁcation and Generative Approaches. In:
Bouamor H, Al-Khalifa H, Darwish K, Rambow O, Bougares F,
Abdelali A et al. (eds) Proceedings of the Seventh Arabic Natural
Language Processing Workshop (WANLP), pp 43–52
Koubaa A, Ammar A, Ghouti L, Najar O, Sibaee S (2024) Ara-
bianGPT: Native Arabic GPT-based Large Language Model.
arxiv:2402.15313
Lan W, Chen Y, Xu W, Ritter A (2020a) An Empirical Study of
Pre-trained Transformers for Arabic Information Extraction. In:
Webber B, Cohn T, He Y, Liu Y (eds) Proceedings of the 2020
Conference on Empirical Methods in Natural Language Process-
ing (EMNLP). Online: Association for Computational Linguistics,
pp 4727–4734
Lan Z, Chen M, Goodman S, Gimpel K, Sharma P, Soricut R (2020b)
ALBERT: A Lite BERT for Self-supervised Learning of Language
Representations. arxiv:1909.11942
Landauer TK, Foltz PW, Laham D (1998) An introduction to latent
semantic analysis. Discourse Process 25(2–3):259–284
Lee H, Yoon S, Dernoncourt F, Kim DS, Bui T, Shin J et al
(2020) KPQA: A metric for generative question answering using
keyphrase weights. arXiv preprint arxiv:2005.00192
Lewis P, Oguz B, Rinott R, Riedel S, Schwenk H (2020) MLQA: Eval-
uating Cross-lingual Extractive Question Answering. In: Jurafsky
D, Chai J, Schluter N, Tetreault J (eds) Proceedings of the 58th
Annual Meeting of the Association for Computational Linguistics.
Online: Association for Computational Linguistics, pp 7315–7330
123
 135 
Page 26 of 28

--- Page 27 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
Liang D, Gonen H, Mao Y, Hou R, Goyal N, Ghazvininejad M, et al
(2023) XLM-V: Overcoming the Vocabulary Bottleneck in Mul-
tilingual Masked Language Models. In: Proceedings of the 2023
Conference on Empirical Methods in Natural Language Process-
ing, pp 13142–13152
Li S, Che Y, Yang J, Li Q, Tian T (2024) A question answer chatbot
using term frequency-inverse document frequency and Markov
chain. In: International Conference on Computer Graphics, Arti-
ﬁcial Intelligence, and Data Processing (ICCAID 2023). SPIE, pp
966–971
Liu Y et al (2019) RoBERTa: A Robustly Optimized BERT Pretraining
Approach. arxiv:1907.11692
Malhas R, Elsayed T (2022) Arabic machine reading comprehen-
sion on the Holy Qur’an using CL-AraBERT. Inf Process Manag
59(6):103068
MalinC(2024)FirstLLMtrainedexclusivelyonSaudidatasets.Middle
East AI News
Mannaa ZM, Azmi AM, Aboalsamh HA (2022) Computer-assisted
i‘raab of Arabic sentences for teaching grammar to students. J
King Saud Univ-Comput Inf Sci 34(10B):8909–8926
Masri S, Raddad Y, Khandaqji F, Ashqar HI, Elhenawy M (2024) Trans-
former models in education: Summarizing science textbooks with
arabart, MT5, arat5, and mBART. In: International Conference on
Intelligent Systems, Blockchain, and Communication Technolo-
gies. Springer, pp 286–300
Maynard D, Li Y, Peters W (2008) NLP Techniques for Term Extraction
and Ontology Population. In: Cimiano P (ed) Buitelaar P. Bridg-
ing the Gap between Text and Knowledge. IOS Press, Ontology
Learning and Population, pp 107–127
Mikolov T, Chen K, Corrado G, Dean J (2013) Efﬁcient Estimation of
Word Representations in Vector Space. In: Bengio Y, LeCun Y
(eds) 1st International Conference on Learning Representations,
ICLR 2013, Scottsdale, Arizona, USA, May 2–4, 2013. Workshop
Track Proceedings
Mozannar H, Maamary E, El Hajal K, Hajj (2019) Neural Arabic
Question Answering. In Proceedings of the Fourth Arabic Nat-
ural Language Processing Workshop, pp 108–118
Nagoudi EMB, Elmadany A, Abdul-Mageed M.: AraT5: Text-to-Text
Transformers for Arabic Language Generation. arxiv:2109.12068
Nakano R, Hilton J, Balaji S, Wu J, Ouyang L, Kim C et al (2022)
WebGPT: Browser-assisted question-answering with human feed-
back. arxiv:2112.09332
Noor (2022) The World’s Largest Arabic NLP model. Technology Inno-
vation Institute
Obeidat R, Al-Harbi M, Al-Ayyoub M, Alawneh L (2024) ArQuAD:
An Expert-Annotated Arabic Machine Reading Comprehension
Dataset. Cogn Comput
OpenAI (2024) Introducing ChatGPT. OpenAI
OpenAI et al (2024) GPT-4 Technical Report. arxiv:2303.08774
Pennington J, Socher R, Manning CD (2014) Glove: Global Vectors for
Word Representation. In: EMNLP, pp 1532–1543
Peters ME et al (2018) Deep Contextualized Word Representations. In:
Walker M, Ji H, Stent A (eds) Proceedings of the 2018 Conference
of the North American Chapter of the Association for Compu-
tational Linguistics: Human Language Technologies, Volume 1
(Long Papers). New Orleans, Louisiana: Association for Compu-
tational Linguistics, pp 2227–2237
Radford A, Narasimhan K, Salimans T, Sutskever I (2018) Improving
Language Understanding by Generative Pre-Training. https://cdn.
openai.com/research-covers/language-unsupervised/language_
understanding_paper.pdf
Radford A, Wu J, Child R, Luan D, Amodei D, Sutskever I (2019)
Language Models are Unsupervised Multitask Learners. https://
cdn.openai.com/better-language-models/language_models_are_
unsupervised_multitask_learners.pdf
Raffel C, Shazeer N, Roberts A, Lee K, Narang S, Matena M et al (2020)
Exploring the limits of transfer learning with a uniﬁed text-to-text
transformer. J Mach Learn Res 21(140):1–67
Rajpurkar P, Jia R, Liang P (2016) Squad: 100,000+ questions for
machine comprehension of text. In: Proceedings of the 2016 con-
ference on empirical methods in natural language processing, pp
2383–2392
Ramesh K, Ravishankaran S, Joshi A, Chandrasekaran K (2017) A Sur-
vey of Design Techniques for Conversational Agents. In: Kaushik
S, Gupta D, Kharb L, Chahal D (eds) Information, Communication
and Computing Technology. Springer, Singapore, pp 336–350
Saad MK, Ashour W (2010) OSAC: Open source Arabic corpora. In:
6th International Conference on Electrical and Computer Systems
(EECS ’10)
Safaya A, Abdullatif M, Yuret D (2020) KUISAIL at SemEval-2020
Task 12: BERT-CNN for Offensive Speech Identiﬁcation in Social
Media. In: Proceedings of the Fourteenth Workshop on Seman-
tic Evaluation. Barcelona (online): International Committee for
Computational Linguistics, pp 2054–2059
Sanh V, Debut L, Chaumond J, Wolf T (2020) DistilBERT, a dis-
tilled version of BERT: smaller, faster, cheaper and lighter.
arxiv:1910.01108
Saoudi Y, Gammoudi MM (2023) Trends and Challenges of Arabic
Chatbots: Literature Review. Jordanian J Comput Info Technol
9(3):261–286
Sengupta N et al (2023) Jais and Jais-chat: Arabic-Centric Foundation
and Instruction-Tuned Open Generative Large Language Models.
arxiv:2308.16149
Sidhoum AH, Mataoui M, Sebbak F, Smaïli K (2022) ACQAD: A
dataset for arabic complex question answering. In: International
Conference on Cyber Security, Artiﬁcial Inteligence and Theoret-
ical Computer Science, Boumerdès, Algeria
Siu, SC (2023) ChatGPT and GPT-4 for Professional Translators:
Exploring the Potential of Large Language Models in Transla-
tion. Computational Linguistics & Natural Language Processing
eJournal, 5(24)
Talafha B, Ali M, Za’ter ME, Seelawi H, Tuffaha I, Samir M et al (2020)
Multi-dialect Arabic BERT for Country-level Dialect Identiﬁca-
tion. In: Zitouni I, Abdul-Mageed M, Bouamor H, Bougares F,
El-Haj M, Tomeh N et al (eds) Proceedings of the Fifth Arabic Nat-
ural Language Processing Workshop. Barcelona, Spain (Online):
Association for Computational Linguistics, pp 111–118
Team G, Anil R, Borgeaud S, Wu Y, Alayrac JB, Yu J, et al (2024)
Gemini: A family of highly capable multimodal models. arXiv
preprint arxiv:2312.11805, 10
Touvron H, Lavril T, Izacard G, Martinet X, Lachaux MA, Lacroix
T et al (2023a) LLaMA: Open and efﬁcient foundation language
models. arXiv preprint arxiv:2302.13971
Touvron H, Martin L, Stone K, Albert P, Almahairi A, Babaei Y et al
(2023b) Llama 2: Open foundation and ﬁne-tuned chat models.
arXiv preprint arxiv:2307.09288
Trivedi A, Gor V, Thakkar Z (2019) Chatbot generation and integration:
A review. Inter J Adv Res Ideas Innov Technol 5(2):1308–1311
Vaswani A, Shazeer N, Parmar N, Uszkoreit J, Jones L, Gomez AN et al
(2017)AttentionisAllyouNeed.In:GuyonI,LuxburgUV,Bengio
S, Wallach H, Fergus R, Vishwanathan S et al (eds) Advances
in Neural Information Processing Systems, vol 30. Inc, Curran
Associates, pp 1–11
Williams JD, Young S (2007) Partially observable Markov deci-
sion processes for spoken dialog systems. Comput Speech Lang
21(2):393–422
Xue L, Constant N, Roberts A, Kale M, Al-Rfou R, Siddhant A
et al (2021) mT5: A Massively Multilingual Pre-trained Text-to-
Text Transformer. In: Toutanova K, Rumshisky A, Zettlemoyer
L, Hakkani-Tur D, Beltagy I, Bethard S, et al. (eds) Proceed-
ings of the 2021 Conference of the North American Chapter of
123
Page 27 of 28 
135

--- Page 28 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:135 
the Association for Computational Linguistics: Human Language
Technologies. Association for Computational Linguistics, pp 483–
498
Zeng C, Li S, Li Q, Hu J, Hu J (2020) A Survey on Machine Read-
ing Comprehension-Tasks, Evaluation Metrics and Benchmark
Datasets. Applied Sciences 10(21):7640
Zhang T, Kishore V, Wu F, Weinberger KQ, Artetxe M (2019) Bertscore:
Evaluating text generation with bert. In: International conference
on learning representations
Zhou M, Duan N, Liu S, Shum HY (2020) Progress in Neural NLP:
Modeling, Learning, and Reasoning. Engineering 6(3):275–290
Publisher’s Note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional afﬁliations.
123
 135 
Page 28 of 28

```
