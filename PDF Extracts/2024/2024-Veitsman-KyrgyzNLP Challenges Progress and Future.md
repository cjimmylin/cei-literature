---
title: "2024-Veitsman-KyrgyzNLP Challenges Progress and Future - PDF Extract"
source_pdf: "2024-Veitsman-KyrgyzNLP Challenges Progress and Future.pdf"
pages: 37
extracted_at: "2026-02-13T14:50:53.884264"
---

# PDF Extract: 2024-Veitsman-KyrgyzNLP Challenges Progress and Future

**Source PDF:** 2024-Veitsman-KyrgyzNLP Challenges Progress and Future.pdf
**Total Pages:** 37

---

## Content

```
--- Page 1 ---

KyrgyzNLP: Challenges, Progress, and Future
Anton Alekseev1,2,3,4[0000−0001−6456−3329] and
Timur Turatali5[0009−0001−6778−460X]
1 Steklov Mathematical Institute at St. Petersburg, St. Petersburg, Russia
2 St. Petersburg State University, St. Petersburg, Russia
3 Kazan (Volga Region) Federal University, Kazan, Russia
4 Kyrgyz State Technical University n. a. I. Razzakov, Bishkek, Kyrgyzstan
5 The Cramer Project, Bishkek, Kyrgyzstan
6 Kyrgyz AI Research Institute, Bishkek, Kyrgyzstan
{anton.m.alexeyev,timur.turat}@gmail.com
Abstract. Large language models (LLMs) have excelled in numerous
benchmarks, advancing AI applications in both linguistic and non-linguistic
tasks. However, this has primarily benefited well-resourced languages,
leaving less-resourced ones (LRLs) at a disadvantage. In this paper, we
highlight the current state of the NLP field in the specific LRL: кыргыз
тили.
Human evaluation, including annotated datasets created by native speak-
ers, remains an irreplaceable component of reliable NLP performance,
especially for LRLs where automatic evaluations can fall short. In re-
cent assessments of the resources for Turkic languages, Kyrgyz is labeled
with the status “Scraping By”, a severely under-resourced language spo-
ken by millions. This is concerning given the growing importance of the
language, not only in Kyrgyzstan but also among diaspora communities
where it holds no official status.
We review prior efforts in the field, noting that many of the publicly
available resources have only recently been developed, with few excep-
tions beyond dictionaries (the processed data used for the analysis is pre-
sented at https://kyrgyznlp.github.io/). While recent papers have
made some headway, much more remains to be done. Despite interest
and support from both business and government sectors in the Kyrgyz
Republic, the situation for Kyrgyz language resources remains challeng-
ing. We stress the importance of community-driven efforts to build these
resources, ensuring the future advancement sustainability. We then share
our view of the most pressing challenges in Kyrgyz NLP. Finally, we pro-
pose a roadmap for future development in terms of research topics and
language resources.
Keywords: Kyrgyz language · Less-resourced languages · Survey
1
Introduction
In recent years, Natural Language Processing (NLP) and Large Language Mod-
els (LLMs) have revolutionized the field of artificial intelligence, pushing the
arXiv:2411.05503v2  [cs.CL]  16 Nov 2024

--- Page 2 ---

2
A. Alekseev, T. Turatali
boundaries of what machines can accomplish in understanding and generating
human language. These advancements have led to significant improvements in
various applications, from machine translation to sentiment analysis, and from
chatbots to content generation. What might be even more important, LLMs
are already changing the job markets and other spheres of life [14,85]. Since
2022, texts written in natural languages have become a crucial medium between
humans and AI applications, making NLP arguably more prominent than ever.
However, the rapid progress in NLP has not been uniform across all lan-
guages, creating a digital divide that threatens to worsen existing linguistic in-
equalities.
While languages with abundant digital resources, such as English or Span-
ish, have reaped the benefits of these technological breakthroughs, less-resourced
languages (LRLs) have largely been left behind. This disparity is particularly
concerning as it risks further marginalizing communities that already face chal-
lenges in the digital age. One such language that exemplifies this issue is Kyrgyz
(кыргыз тили), a Turkic language spoken by millions of people primarily in
Kyrgyzstan and neighboring regions.
Kyrgyz, despite its rich cultural heritage and significant speaker population,
has been classified as “Scraping By” in terms of NLP resources [57,95]. This
classification underscores the severe lack of digital tools, datasets, and models
available for processing and analyzing the language. The scarcity of resources is
particularly troubling given the growing importance of Kyrgyz, not only within
Kyrgyzstan where it holds official status but also among diaspora communities
worldwide where the language serves as a vital link to cultural identity.
The development of NLP tools for less-resourced languages like Kyrgyz presents
unique challenges. Unlike well-resourced languages that can rely on vast amounts
of digital text for training models, LRLs often require more careful curation of
limited available data. Moreover, the creation of high-quality, annotated datasets
— a cornerstone of modern NLP — demands the involvement of native speakers
and linguistic experts, a resource that can be scarce for many LRLs.
Recent years have seen a growing awareness of the importance of linguistic
diversity in the digital sphere. Both governmental and private sector entities
in Kyrgyzstan, where Kyrgyz is the official language, have shown interest in
developing language technologies.
Government initiatives include, for example, (1) Constitutional Law on the
State Language: on July 17, 2023, President Sadyr Japarov signed the Consti-
tutional Law on the State Language, aiming to implement the Article 13 of the
constitution, which designates Kyrgyz as the state language; this law outlines
procedures for its use, underscoring the government’s commitment to enhancing
the status and usage of the Kyrgyz language [18]; (2) the National Commission
on the State Language and Language Policy operating under the President of the
Kyrgyz Republic and focusing on the development and implementation of lan-
guage policies that promote the Kyrgyz language; it serves as a central body for
coordinating efforts related to language development and policy enforcement7.
7 https://mamtil.gov.kg/en

--- Page 3 ---

KyrgyzNLP: Challenges, Progress, and Future
3
Private sector initiatives in Kyrgyzstan include (1) the AI-related efforts in-
volving Kyrgyz language processing: in early 2024, Kyrgyzstan tested an artificial
intelligence model capable of processing and understanding the Kyrgyz language;
this development highlights the private sector’s role in advancing language tech-
nologies that support linguistic diversity8; (2) collaborations to bridge the AI
language gap: in May 2024, telecom company Veon, along with partners includ-
ing Beeline Kazakhstan and the Barcelona Supercomputing Center, announced
efforts to address the “AI language gap” for under-represented languages; this ini-
tiative focuses on developing tools and documentation for languages like Kyrgyz,
aiming to enhance their representation in AI models9.
These examples demonstrate a concerted effort by both governmental and
private entities in Kyrgyzstan to develop language technologies that promote
linguistic diversity in the digital realm.
This paper aims to address the current state of Kyrgyz language processing
and chart a possible course for its future development. We begin by reviewing
the existing efforts in Kyrgyz NLP, noting the recent emergence of some publicly
available resources10. We then identify the most pressing challenges facing the
field, drawing on insights from both academic research and practical applications.
Finally, we propose a roadmap for future development, outlining key research
areas and necessary language resources.
Our intention is to encourage a community-driven approach to resource de-
velopment and to motivate the interested parties in government and business in
the support of the process, to ensure sustainable progress in making advanced
language technologies accessible to all linguistic communities.
The remainder of this paper is structured as follows. Section 2 discusses the
importance of data in NLP, beginning with motivating examples and exploring
processing methods specifically suited for less-resourced languages. It further ex-
amines the potential of large language models (LLMs) as a universal solution
in this context. Section 3 introduces Kyrgyz as a less-resourced language, offer-
ing an overview of the language and its unique linguistic relations within the
Turkic language family. Section 4 addresses the challenges facing Kyrgyz NLP,
including resource scarcity, script and dialect diversity, the complexities of agglu-
tinative morphology, and the decentralized nature of existing initiatives. Then, in
Section 5, the existing surveys of the field are reviewed. Section 6 presents a sci-
entometric analysis of Kyrgyz NLP, categorizing key topics within the field and
highlighting noteworthy observations. Section 7 provides an overview of recent
Kyrgyz NLP research, with a focus on morphology, syntax, semantics, corpus
studies, and NLP applications. In Section 8, we review existing resources rele-
vant to Kyrgyz NLP. Section 9 identifies untapped subdomains of Kyrgyz NLP,
emphasizing areas for new language resources and innovative, untried method-
ological approaches. Section 10 outlines a roadmap for future development in
8 central-asia.media:Kyrgyzstan has Tested AI Model in Kyrgyz Language.
9 Reuters:Veon teams up with partners to bridge online ’AI language gap’.
10 We have developed an interactive website presenting and organizing the data used
in this study: https://kyrgyznlp.github.io/

--- Page 4 ---

4
A. Alekseev, T. Turatali
Kyrgyz NLP, detailing proposed milestones and a projected timeline. Finally,
Section 11 concludes the paper with a summary of key findings and implications
for the continued advancement of Kyrgyz NLP.
2
On the Importance of Data in NLP
Data is undoubtedly the cornerstone of NLP. Carefully curated datasets have
historically driven significant advancements in the field. In this section, we sup-
port this claim and clarify the reasons behind our advocacy for data annotation
initiatives.
2.1
Motivating Examples
Two notable NLP milestones illustrate the impact of rigorous data preparation
on the progress of language science.
Penn Treebank. Released in the 1990s, the Penn Treebank [54] introduced
syntactic and part-of-speech annotations for millions of English words. This re-
source shifted NLP from rule-based to probabilistic, data-driven approaches, en-
abling breakthroughs in syntactic parsing, machine translation, and statistical
modeling.
BioBERT. Published in the 2020s, BioBERT [45] leveraged annotated biomed-
ical texts to outperform general NLP models in domain-specific tasks like named
entity recognition, relation extraction, and others [56,76]. This demonstrated the
importance of specialized data and triggered a trend in fine-tuning models on
annotated, domain-specific datasets.
A more recent study [77] showed that training BERT [16] on the British
National Corpus [12] (i.e., a carefully curated yet much smaller text collection
than that used to train the original model) achieved even better performance
than the original BERT model.
Thus, even in the age of powerful neural models, the quality and specificity of
data remain critical factors in achieving high-performance NLP systems. More-
over, without datasets for training and validation, the field of Kyrgyz NLP simply
cannot advance.
2.2
Processing Methods for Less-Resourced Languages
Addressing the challenges faced by LRLs requires innovative approaches that
compensate for the lack of resources. Several common methods have been em-
ployed to process LRLs beyond Kyrgyz.
Data Collection and Augmentation. Collecting additional data is a
straightforward but resource-intensive approach. This involves gathering texts
from various domains, including literature, social media, and transcriptions of
spoken language. Data augmentation techniques, such as back-translation [82,23]
and synthetic data generation [44,67], can increase dataset size and diversity.

--- Page 5 ---

KyrgyzNLP: Challenges, Progress, and Future
5
Leveraging Machine Translation and Multilingual Models. Utilizing
machine translation and multilingual models allows for transfer learning from
high-resource languages. Models pre-trained on languages with similar linguistic
features can be fine-tuned for Kyrgyz. For Turkic languages, transfer learning
from Turkish or Kazakh can be beneficial due to linguistic similarities [57,58].
Sampling and Transfer Learning. Sampling strategies help select the
most informative data subsets for training. Transfer learning involves adapting
models trained on large datasets in other languages to Kyrgyz, adjusting the
model’s parameters to better fit the target language.
Manual and Unsupervised Techniques. Rule-based systems, developed
with linguistic expertise, can address specific challenges in morphology and syn-
tax. Unsupervised learning methods, such as clustering and topic modeling, can
extract patterns from unannotated data, which is especially useful when labeled
data is scarce.
Utilizing External Tools. Existing tools and frameworks, such as Aper-
tium [19], a platform for rule-based machine translation, can be adapted for
Kyrgyz [98]. These tools often support multiple languages and can be extended
to include LRLs with additional development.
2.3
LLMs as a “Universal Solution”?
An emerging counter-argument to developing datasets for low-resource languages
(LRLs) and traditional non-LLM NLP methods suggests that next-generation
large language models may surpass prior approaches across various NLP tasks,
even without extensive task-specific data for training or fine-tuning. While an
in-depth discussion of the limitations of this perspective is beyond our scope, it
warrants careful consideration due to its implications for LRL data development.
A recent example involving the Gemini 1.5 Pro model’s in-context learning
is indeed impressive: When given a grammar manual for Kalamang, a language
with fewer than 200 speakers worldwide, the model learns to translate English
to Kalamang at a level comparable to a person learning from the same con-
tent [21,96,88]. Beyond this specific case, more approaches of this sort are likely
to emerge in the future [105].
Essentially, in 2024, given a sufficiently large and comprehensive prompt
derived from a textbook, a proprietary model — available via API as of October
2024 — is capable of providing translations to and from previously “unseen”
languages, achieving a quality level comparable to that of a human learning the
same language. This is not the only example of the success of large language
models (LLMs) in tasks for which, as asserted, they had no direct data in the
training set.
However, we believe this progress should not demotivate those working with
low-resource languages (LRLs), nor those supporting, funding, or volunteering in
data annotation for related research. On the contrary, it should encourage further
exploration, and the example involving the Kalamang language is particularly
inspiring. Evaluation datasets can be viewed as analogous to a textbook — though

--- Page 6 ---

6
A. Alekseev, T. Turatali
they may not contain explicit rules, they are nonetheless rooted in authentic
data.
Beyond the arguments above and the examples in Section 2.1, there are many
practical reasons to continue developing language resources despite the advances
of universal models.
Safety, Decision-Making, and Model Evaluation. All machine learning (ML) and
artificial intelligence (AI) solutions, including those based on LLMs, require rig-
orous quality and safety control by human experts. Incorrect decisions about
which foundational model to select for a given task — whether in industry or
academia — can lead to unnecessary expenses, ecological impacts, security vul-
nerabilities, reputational harm, and other negative outcomes [43]. Evaluating
models on tasks similar to those they are expected to solve in production or at
scale is arguably the most cost-effective approach to understanding their poten-
tial performance.
Further, this perspective underscores the need to create diverse and realistic
datasets for model evaluation, ensuring that models are tested in scenarios that
closely mirror real-world use. This approach will not only enhance model relia-
bility but also provide an essential benchmark for comparing performance across
diverse tasks, ultimately driving the development of safer and more effective AI
systems for both high-resource and low-resource language contexts.
Cultural Preservation. Less-resourced languages preserve unique cultures and
histories. Even independent of the “new AI spring,” it is essential to document
Kyrgyz language patterns across various contexts and media: news reporting,
literary fiction, conversational speech, folklore, children’s language, and social
media commentary. Dialectal forms and linguistic phenomena such as code-
switching, neologisms, irony, and context-specific expressions demand attention,
best captured through contemporary sources and spoken language. To preserve
both “classical” and dynamic, modern expressions of Kyrgyz, it is crucial to
collect, annotate, and organize text corpora. With the anticipated widespread
adoption of AI solutions, there is limited time to accomplish this.
Innovation and Research. Addressing the challenges posed by LRLs, such as
limited data availability, complex morphology, and unique linguistic structures,
fosters the development of novel methodologies that benefit the entire field of
NLP. For instance, strategies developed for low-resource settings often contribute
to advancements in transfer learning, data augmentation, and model robustness
— areas critical to making LLMs more adaptable and efficient across diverse
linguistic contexts. By investing in resources for LRLs like Kyrgyz, the NLP field
not only promotes linguistic inclusivity but also drives research with widespread
implications, strengthening the adaptability and generalizability of AI across
languages and domains.
Human Oversight. Human oversight remains essential across NLP tasks, espe-
cially for handling edge cases and cultural nuances that LLMs may overlook or

--- Page 7 ---

KyrgyzNLP: Challenges, Progress, and Future
7
misinterpret. While LLMs have shown impressive capabilities, their limitations in
understanding context-specific subtleties, idiomatic expressions, and culturally
embedded meanings highlight the need for human review. This is particularly
critical for languages like Kyrgyz, where unique linguistic and cultural elements
may be underrepresented in training data. Human expertise ensures that outputs
are accurate, culturally sensitive, and contextually relevant, safeguarding against
potential misinterpretations and biases. Human involvement is crucial not only
for the safety and reliability of NLP applications but also for maintaining the
integrity and richness of underrepresented languages.
Model Limitations. The success of certain models, such as Gemini 1.5 in translat-
ing the Kalamang language, does not guarantee comparable performance across
all languages. Additionally, while impressive, translation alone does not cover the
full spectrum of linguistic tasks. Generalization remains a challenge, as language-
specific complexities often reveal gaps in performance, underscoring the need for
dedicated resources and models tuned to each language’s unique characteristics.
3
Kyrgyz as a Less-Resourced Language
3.1
The Kyrgyz Language: An Overview
Linguistic and Demographic Profile. Kyrgyz (written “кыргыз тили” or “кыр-
гызча”, and alternatively as “Kirghiz” or “Kirgiz”) is a Turkic language spoken
in Kyrgyzstan, China, Tajikistan, Uzbekistan, and several other countries. Its
classification within Turkic is complex; it appears to belong alternately to the
Kypchak (Northwestern) branch and the South Siberian (Northeastern) branch.
Phonetically and phonologically, the Turkic varieties most similar to Kyrgyz
are the southern dialects of Altay, though Kyrgyz shows strong parallels to
Kazakh, especially in its Talas (Talas Region) dialects, which these Altay vari-
eties lack [98]. In Southern varieties of Kyrgyz, there are also notable similarities
to Uzbek that other dialects lack.
Kyrgyz is spoken primarily in Kyrgyzstan, where it holds official status as
the national language. Many residents of Kyrgyzstan are bilingual in Kyrgyz
and Russian and/or Uzbek, comprising a majority of the country’s population.
In Central Asia, sizable Kyrgyz-speaking communities exist outside Kyrgyzstan,
most notably in China (where the Kyrgyz are an officially recognized minority),
Tajikistan, Afghanistan, Pakistan, and Uzbekistan. The current estimate of the
number of speakers is approximately 5.3 million,11 primarily in Kyrgyzstan.
The Kyrgyz language was initially written in the Göktürk script, which was
later replaced by the Perso-Arabic alphabet. This script was used until 1928
in the Soviet Union and is still in use in China, Afghanistan, and Pakistan.
From 1928 to 1940, the Uniform Turkic Alphabet, based on the Latin script,
was introduced. However, in 1940, Soviet authorities mandated the use of the
Cyrillic alphabet for all Turkic languages within their territory. After Kyrgyzstan
11 Based on figures from [62].

--- Page 8 ---

8
A. Alekseev, T. Turatali
gained independence in 1991, there was renewed interest in transitioning to the
Latin alphabet. Although this shift has not yet been implemented, it remains a
topic of occasional discussion. Examples of Kyrgyz writing in different scripts,
including historical ones, are presented in Table 1.
Cyrillic
alphabet
(1938 – now)
Old Latin
alphabet
(1928 – 1938)
Arabic
alphabet
(pre 1928)
Old Turkic
alphabet
(VIII – X c.)
Translation
into English
language
Бардык адамдар
өз беделинде жана
укуктарында
эркин жана тең
укуктуу болуп
жаралат. Алардын
аң-сезими менен
абийири бар жана
бири-бирине бир
туугандык мамиле
кылууга тийиш.
All human beings
are born free and
equal in dignity
and rights. They
are endowed with
reason and
conscience and
should act
towards one
another in a
spirit of
brotherhood.
Table 1. The examples of Kyrgyz scripts [103].
Certain Linguistic Characteristics. Kyrgyz uses a subject-object-verb word or-
der and lacks grammatical gender, with gender conveyed through context. Unlike
English, Kyrgyz does not have several analytical grammatical features, such as
auxiliary verbs (e.g., “to have”), definite and indefinite articles (e.g., “the” and
“a/an”), modal verbs (e.g., “should”, “will”), dependent clauses, and subordinat-
ing conjunctions (e.g., “that”, “before”, “while”). Instead, it replaces these with
various synthetic grammatical structures.
Kyrgyz is notably agglutinative, meaning it forms words by stringing together
morphemes without altering their spelling or phonetics. This structure results
in a vast number of possible word forms. While a verb in Russian can have a
maximum of 150 written forms, in Kyrgyz, this number can reach thousands.
A famous illustrative example: one of the legitimate interrogative forms of the
verb “камсызда” (“to provide,” “to guarantee,” “to insure”) is “камсыздан-
дырылбагандардансыздарбы” (“Are you from those who have not been
insured?”).
Prominent phonological features, such as vowel harmony and consonant as-
similation, also require special handling in rule-based NLP methods.
3.2
Linguistic Relations
As noted above, classification of the Kyrgyz language within the Turkic family
remains problematic. The Swadesh 100-word list [86] is often used to determine
the degree of lexical similarities and differences between languages as a percent-
age. This list includes words from the basic lexicon, which is generally resistant to

--- Page 9 ---

KyrgyzNLP: Challenges, Progress, and Future
9
historical changes across languages worldwide. A higher percentage of matching
words between languages indicates closer linguistic kinship.
Results of lexical-statistical analysis of the Kyrgyz language’s relationship to
certain Turkic languages, based on the 215-word Swadesh list [87,51]: (1) Kazakh:
91%, (2) Tatar: 79%, (3) Uyghur: 77%, (4) Uzbek: 76%, (5) Altai: 73%.
A lexical similarity of over 85% suggests that two languages in comparison
are likely related as dialects of a single language. These similarities indicate
significant potential for transfer learning and resource sharing among Turkic
languages.
4
Challenges in Kyrgyz NLP
Scarcity of Machine-Readable Resources. A core challenge for any LRL is the
shortage of large, annotated text corpora for training and evaluating models, as
well as other structured resources such as dictionaries, lexicons, and thesauri.
For Kyrgyz, an additional issue arises from the limited diversity in easily ob-
tainable data (e.g., from web scraping), which is predominantly sourced from
news articles. This focus on news media restricts the range of language styles
and registers available for analysis and model training.
Multiple Scripts and Dialects. As discussed in Section 3.1, Kyrgyz speakers use
multiple scripts. Ideally, tools should support both Cyrillic and Perso-Arabic
scripts directly or incorporate reliable open-source transliteration solutions [101]
within user-friendly interfaces.12 Additionally, dialectal variations affect vocab-
ulary, pronunciation, and grammar. For instance, the “Northern vs Southern”
dialectal division in Kyrgyz shows the influence of Mongolian and Uzbek, re-
spectively.
Agglutinative Morphology. As highlighted in Section 3.1, Kyrgyz’s agglutinative
nature generates a vast number of word forms. A single verb in Kyrgyz, for
example, can have thousands of forms, compared to a maximum of around 150
in Russian [94,7]. This complexity requires sophisticated morphological analysis
algorithms to parse and understand word structures.
Decentralized Initiatives. Previous corpus-building efforts have been fragmented
(for details, see Section 7.4), resulting in duplicated work and a lack of standard-
ization across initiatives. Developing a comprehensive national corpus remains
an ongoing effort.
Despite these challenges, there is a growing demand for NLP applications in
Kyrgyz. With over 5 million native speakers and official status in Kyrgyzstan,
there is a need for tools such as machine translation, speech recognition, and text
analysis. The increasing digital presence of Kyrgyz speakers further underscores
12 A suitable tool is already available. A user-friendly interface is implemented for
Kazakh in apertium-kaz; a similar adaptation for apertium-kir is considered feasible
by the authors: https://github.com/apertium/apertium-kir/issues/13

--- Page 10 ---

10
A. Alekseev, T. Turatali
the need for advancements in NLP to support communication, education, and
access to information.
5
Existing Surveys of the Field
Research on computational approaches to processing the Kyrgyz language spans
several decades. To the best of our knowledge, only two surveys focused on
computational linguistics aspects of Kyrgyz text processing have been published
prior to this work.
In the study by Musayev [60] presented at the first TurkLang conference,
the state of computational linguistics in Kyrgyzstan (as of 2013) is reviewed,
covering developments since the 1990s. According to the authors, the key areas
requiring development are (1) unified word formation algorithms, (2) creation
of computational language models and linguistic resources, (3) standardization
of orthography and spelling, (4) transition to the Latin alphabet for Turkic lan-
guages. The survey also identifies key interest groups and institutions involved
in Kyrgyz NLP, such as the Institute of Theoretical and Applied Mathemat-
ics of the National Academy of Sciences of Kyrgyzstan and the computational
linguistics department at the Kyrgyz State University of Construction, Trans-
portation, and Architecture (as of 2024, part of KSTU named after I. Razzakov).
TamgaSoft’s13 solutions are mentioned.
In a recent 2024 survey of Central Asian Turkic languages by Y. Veits-
man [95], progress in data collection and NLP for Kyrgyz is acknowledged,
though significant challenges remain. The author recommends collecting more
high-quality data, focusing on transfer learning from related languages (e.g.,
Kazakh and Turkish), and leveraging LLMs for data augmentation. Veitsman’s
survey categorizes Kyrgyz as “Scraping By”, following the classification in [28],
a label previously assigned in [57] as well. This designation indicates insufficient
resources and initiatives for Kyrgyz NLP, attributed to factors such as a lack
of language-focused initiatives, the dominance of Russian as a lingua franca in
Central Asia, and limited internet access in some regions.
6
Scientometric Analysis of Kyrgyz NLP
To elucidate the landscape of Kyrgyz NLP research, we conducted a sciento-
metric analysis of 67 research works. While some studies date back to the 1980s
and 1990s,14 our primary focus has been on works published from 2011 onward.
This choice is due to the limited availability of programs or datasets from earlier
13 https://tamgasoft.kg/en/
14 The most notable contributions from this period include the seminal works of Dr.
Tashpolot Sadykov, such as [68,69]. A distinguished Turkologist and computa-
tional linguist, Dr. Sadykov passed away in November 2023 and would have turned
75 in October 2024. His pioneering contributions remain foundational to the field,
and his absence is profoundly felt by the research community.

--- Page 11 ---

KyrgyzNLP: Challenges, Progress, and Future
11
publications, which restricts their applicability to contemporary computational
practices.
Our data collection methodology proceeded as follows.
We initially gathered papers containing the keyword “Kyrgyz” in their title
or abstract from all TurkLang conferences15, along with all works cited within
these papers and publications from the authors’ portfolios. After excluding irrel-
evant studies (e. g., non-NLP papers or those lacking computational methods),
additional papers were identified through Google Scholar and other academic
databases.16
A primary limitation of this approach is that it does not ensure comprehen-
sive coverage of all Kyrgyz NLP research. However, we believe this compilation
captures the contributions of researchers actively engaged in the field and in-
vested in the visibility and impact of their work. Our collection encompasses
papers presented at relevant events or in relevant journals and works clearly
indicating connection to the Kyrgyz language, readily accessible through per-
missive indexing engines (contrasting with more restrictive databases such as
Scopus or Web of Science).
Another notable limitation to consider when interpreting the following anal-
ysis is the exclusive focus on Kyrgyz NLP, rather than Turkic NLP (including
multilingual projects leveraging commonalities among Turkic languages, such
as [20]). A broader analysis would have required substantially more time and
likely necessitated a more extensive study beyond the scope of this paper, which
was derived from a keynote presentation constrained to 40 minutes.
6.1
Categorization of Topics.
The collected works were manually categorized by the authors into the following
branches.
MOR Studies focused on morphological analysis and modeling.
SYN Research addressing syntactic structures and parsing.
SEM Works related to semantic analysis and word meaning.
COR Efforts in building and analyzing text corpora.
DIC Construction and usage of lexical resources.
APP Applications, such as machine translation and topic classification.
MSC General surveys and other relevant studies.
During annotation, the APP tag was assigned only when none of the other labels
above (MOR, SYN, SEM, COR, DIC) applied to the paper. If none of the categories ex-
cept MSC were suitable, the MSC label was used. Some manuscripts were assigned
multiple labels to reflect their interdisciplinary nature.
15 TurkLang is an annual conference dedicated to research on Turkic languages, typi-
cally held in regions with a significant population of Turkic language speakers.
16 Also note that, in 2024, the ACL SIGTURK workshop has been established: https:
//sigturk.github.io/workshop/202400/

--- Page 12 ---

12
A. Alekseev, T. Turatali
As expected, works on morphology are the most prevalent, beginning with
the earliest paper in our dataset, while Treebank-related studies have only re-
cently begun to constitute a notable proportion. Although there are relatively
few papers on semantics, they exhibit considerable diversity in both approach
and focus. Several books and surveys, despite their broad titles, do not claim to
be comprehensive (see the statistics in Fig. 1).
Fig. 1. Distribution of the total number of labels (note: some articles may have multiple
labels, so the total does not equal the number of articles).
Collaboration Networks. The manual analysis of co-authorship revealed the fol-
lowing collaboration patterns: (1) Institutional Collaborations: researchers
from the same institution often co-authored papers; (2) International Coop-
eration: some projects involved international teams, particularly in areas like
machine translation and universal dependencies; (3) Interdisciplinary Teams:
successful projects often combined expertise in linguistics, computer science, and
data science.

--- Page 13 ---

KyrgyzNLP: Challenges, Progress, and Future
13
Pankov, P. S.
Washington, J. N.
Ipasov, M.
Tyers, F. M.
Musayev, S. Zh.
Karabaeva, S. Zh.
Imanalieva, A.
Sadykov, T. S.
Sharshembayev, B. Sh.
Salimzianov, I.
Baisa, V.
Suomel, V.
Dolmatova, P.
Zhumalieva, G. E.
Tumenbaeva, M. Zh.
Bakasova, P. S.
Israilova, N. A.
Kokonbaeva, B. O.
Momunaliev, K. Z.
Yiner, Z.
Kurt, A.
Kulamshaev, K.
Zafer, H. R.
Boizou, L.
Mambetkazieva, D.
Ablimit, M.
Parhat, S.
Hamdulla, A.
Zheng, T. F.
Polat, Y.
Zakirov, A.
Bajak, S.
Mamatzhanova, Z.
Sharipbai, A. A.
Ergesh, B. Zh.
Elibaeva, G. K.
Zhetkenbai, L.
Gökırmak, M.
Ivanova, S.
Kuyrukcu, E.
Satybaev, A. D.
Tukeyev, U.
Karibayeva, A.
Zhumanov, Zh.
Kasieva, A. A.
Satybekova, A. T.
Knappen, J.
Fiser, S.
Tei, E.
Egemberdieva, Zh. S.
Li, Z.
Li, X.
Sheng, J.
Slamu, W.
Toleush, A.
Mirzakhalov, J.
Babu, A.
Kunaﬁn, A.
Wahab, A.
Moydinboyev, B.
Uzokova, M.
Pulatova, Sh.
Ataman, D.
Kreutzer, J.
Firat, O.
Licato, J.
Chellappan, S.
Kariev, Sh.
Abduraufov, O.
Hajili, M.
Khaytbaev, A.
Laverghetta, A.
Onal, E.
Kadyrbekova, A. K.
Arikoglu, E.
Benli, I.
Alekseev, A.
Nikolenko, S. I.
Kabaeva, G. Dzh.
Nazirova, E.
Abdurakhmonova, N.
Abidova, Sh.
Uzakova, M.
Turatali, T.
Turdubaeva, A. B.
Dzhumalieva, G. K.
ompson, A.
Jumashev, M.
Chontaeva, B.
Musazhanova, S. Zh.
Senel, L.
Ebing, B.
Baghirova, K.
Sütze, H.
Glavaš, G.
Veitsman, Y.
Aldosova, A.
Abduvaliev, I.
Tohti, T.
Musajan, W.
Bekarystankyzy, A.
Mamyrbayev, O.
Anarbekova, T.
Isaev, R.
Esenalieva, G.
Doszhanov, E.
Ali, S.
Murat, A.
Du, W.
Maimaitiyiming, Y.
Nijat, M.
Li, L.
Wang, D.
Koshueva, M.
Abduvalieva, E.
Yzabekova, D.
Mamasadykov, A.
Abdullaeva, Zh.
Vylomova, E.
White, J.
Salesky, E.
Mielke, S. J.
Wu, S.
Ponti, E. M.
Hall Maudslay, R.
Zmigrod, R.
Valvoda, J.
Toldova, S.
Klyako, E.
Yegorov, I.
Krizhanovsky, N.
Czarnowska, P.
Nikkarinen, I.
Krizhanovsky, A.
Pimentel, T.
Hennigen, L. T.
Kirov, C.
Nicolai, G.
Williams, A.
Anastasopoulos, A.
Cruz, H.
Chodroﬀ, E.
Cotterell, R.
Silfverberg, M.
Hulden, M.
Gatiatullin, A.
Suleymanov, D.
Prokopyev, N.
Khakimov, B.
Meyer, J.
Shliazhko, O.
Fenogenova, A.
Tikhonova, M.
Kozlova, A.
Mikhailov, V.
Shavrina, T.
Fig. 2. Collaboration (co-authorship) network based on the Kyrgyz NLP bibliogra-
phy. Nodes represent individual authors, and an edge between two nodes indicates
co-authorship on at least one work.

--- Page 14 ---

14
A. Alekseev, T. Turatali
6.2
Observations
Most cliques in the co-authorship network represent papers with multiple au-
thors. Isolated vertices indicate single-author papers, i. e., works by researchers
who contributed to Kyrgyz NLP only once (in our dataset), typically with ei-
ther a survey or a focused, standalone contribution. Connected components that
are not cliques (i.e., involving multiple papers) offer insights into collaboration
patterns.
Unsurprisingly, the nodes in this study tend to cluster around specific tasks
or institutions, reflecting researchers’ primary affiliations or project focuses.
In examining the relationship between collaboration structure, topics, and
types of studies presented in the paper, we observed the following patterns.
Resource Scarcity. There is a high demand for tools and datasets, and
contributions in these areas are well-received in the research community.
Online Presence. Research visibility is affected by online presence; projects
without digital traces were less likely to be included or cited.
Complex Studies Require Large and Diverse Research Teams. The
largest communities in the graph, such as those around the SIGMORPHON
paper [97] and Turkic Interlingua studies [58,57], exemplify the need for large,
collaborative efforts. While certain individuals may drive these projects, their
success depends on the collective work of interdisciplinary teams.
Textbooks are Frequently Cited. Although we did not conduct a detailed
citation analysis, textbooks and educational materials are frequently cited, sug-
gesting their value to the field. The development of relevant textbooks, courses,
and workshops is in high demand and could facilitate the adoption of modern
NLP methods, accelerating field progress.
Since we have published the relevant data online17, we encourage those
interested in formal collaboration analysis to apply Social Network Analysis
(SNA) methods [102,80] to the collaboration graph, labeled bimodal author-
paper graph, citation graph (not yet collected), etc. Although the graph sizes
are small in this case, comparing indices such as betweenness centrality with
other indicators of researchers’ output impact could provide a more conclusive
basis to support or challenge our observations.
7
Overview of Kyrgyz NLP Research
7.1
Morphology and Subword-Aware Processing Studies (MOR)
Finite-State Transducers (FSTs) have been employed to model Kyrgyz morphol-
ogy due to their suitability for agglutinative languages. FSTs efficiently handle
the complex affixation and morphological variations. An effective and open mor-
phological analyzer was introduced in 2012 by J. N. Washington, F. M. Tyers,
and M. Ipasov [98] as part of the Apertium project [19]. This tool, along with
17 Bibliography
in
JSON
format:
https://kyrgyznlp.github.io/static/
bibliography_joined.json.

--- Page 15 ---

KyrgyzNLP: Challenges, Progress, and Future
15
other updates and relevant works [100,99,101], has been made publicly available
as code on GitHub.18
Rule-Based Modeling of Different Aspects of Morphology. Researchers have de-
veloped rule-based systems to capture morphological rules since at least the
1980s–1990s [68,65]. These systems define patterns for stem and affix combi-
nations, addressing issues such as vowel harmony and consonant assimilation.
Various aspects of morphological modeling along these lines have been explored
since then [70,39,73,71,27,79,78,41,63], though only a few reference open imple-
mentations or datasets [74], or are integrated into larger frameworks [104]. Also
notable are foundational books on the subject [69,1,75].
Other algorithmic approaches to morphology modeling involve complex data
structures, ontology-like knowledge bases, and various tasks, such as updating
vocabulary in information systems [9,26,25,83].
Another recently studied direction in morphology modeling is the CSE (Com-
plete Set of Endings) approach, discussed in works [93,91,92]. In particular, [93]
explores its applications for neural machine translation.
Perso-Arabic Script as a medium for the Kyrgyz language (primarily used in
China) has also attracted researchers’ attention. Publicly available studies are
few, but they include works on agglutination-aware model fine-tuning [53,52] and
phonological/morphological tools for a uniform multilingual information process-
ing platform primarily targeting UKK (Uyghur, Kazakh, Kyrgyz) languages [2].
Works on character-level approaches to morphology are limited; the only
example we have found is [5].
7.2
Syntax (SYN)
Several recent projects have adapted the Universal Dependencies framework [55]
for Kyrgyz. For links and descriptions, please see Section 8.
Additional efforts are underway to build syntactically annotated corpora and
establish rules and procedures for annotators (e.g., handling copula tokenization,
small words, null-headed clauses, and distinguishing inflection from derivation).
This task is as complex as similar projects for other Turkic languages and has
been addressed in several recent works [17,61,31]. These resources are essential
for training parsers and developing syntactic analysis tools.
7.3
Semantics (SEM)
Studies focused on semantics in Kyrgyz are few and diverse in tasks and ap-
proaches. Works [30,29] describe computational methods for directly modeling
spatial semantics in Kyrgyz, focusing on spatial terms, grammar, and the virtual
geometrical spaces created by verbs. The paper [34] is the only known attempt at
word sense disambiguation (WSD) for Kyrgyz, particularly addressing verb sense
18 E. g., https://github.com/apertium/apertium-kir

--- Page 16 ---

16
A. Alekseev, T. Turatali
disambiguation (VSD). Rule-based methods for VSD automation are presented,
which hold value for NLP and corpus linguistics in agglutinative languages such
as Kyrgyz. A recent effort to create a word embeddings evaluation dataset via
direct translation of the RUSSE benchmark has also been published [3], with
several models evaluated. An even more recent work [84] on multilingual GPT
models was accompanied by the release of the mGPT-1.3B-kirgiz model.19
7.4
Corpus Studies (COR)
Research mentioning corpora is also limited, with some studies noted above
(regarding morphological and syntactic annotation for Kyrgyz corpora).
The study [72] discusses creating a national corpus of the Kyrgyz “Manas”
epic, proposing corpus linguistics techniques to analyze and document its vo-
cabulary and grammar. A framework for building a searchable dictionary of the
epic’s texts, useful for linguistic research and preserving Kyrgyz heritage, is de-
scribed, though no code is provided, and the corpus is still under development.
In the paper [8], Turkic language support in Sketch Engine is described,
focusing on building corpora and providing tools for analysis in Kazakh, Kyr-
gyz, and Turkish. The paper presents methods for web-crawling, concordance
searches, and word sketches.
Papers [37,36,33] focus on part-of-speech (POS) annotation for a newly cre-
ated Kyrgyz language corpus, utilizing the Turkic Lexicon Apertium platform,
with detailed examples of tagging and morphological analysis.
7.5
Applied NLP (APP)
The works focusing on applied tasks (mostly of direct industrial value) are, as
expected, diverse. While some studies concentrate on rule-based approaches to
aid application development, others employ recent neural approaches.
Analysis and Rule-Based. The work [66] compares the accuracy of Google Trans-
late and Yandex Translate for translating Kyrgyz proverbs into English and
Turkish, focusing on lexical, semantic, and syntactic performance. It concludes
that Google Translate performs better overall, particularly in handling Kyrgyz’s
agglutinative structure, though both systems struggle with proverbs. No code or
data are provided, but the presented error analysis highlights key challenges for
improving Kyrgyz machine translation. In the works [38,40], an algorithm for
machine translation from Russian to Kyrgyz, among others, is discussed; how-
ever, these texts primarily focus on morphological and syntactic analysis. They
provide a framework for processing affixes and word formation in Kyrgyz, which
may improve translation accuracy between these languages in automated sys-
tems. These papers mention that a morphological analyzer was developed using
19 The
model
is
freely
available
online:
https://huggingface.co/ai-forever/
mGPT-1.3B-kirgiz

--- Page 17 ---

KyrgyzNLP: Challenges, Progress, and Future
17
Delphi with a database of common Russian words, although no specific code is
provided.
A 2019 overview [99] describes the free and open-source technologies for Tur-
kic languages developed in the Apertium project [19], including morphologi-
cal transducers and machine translation systems for languages such as Kazakh,
Kyrgyz, and Tatar. These tools support language revitalization and linguistic
rights and are useful for developing NLP resources in under-resourced Turkic
languages. All code is available, and the technologies are production-ready for
several languages.
Neural Machine Translation. Two notable works [58,57] evaluate multiway mul-
tilingual neural machine translation (MNMT) for Turkic languages, covering 22
languages, most of them less-resourced. The comparison between bilingual base-
lines and MNMT models shows that MNMT performs better in out-of-domain
tasks, which is useful for enhancing machine translation in under-resourced Tur-
kic languages. Interestingly, the results also indicate that bilingual baselines often
outperform MNMT models for Kyrgyz in domain-specific translations. All code
and models are publicly available.
Other Applications The work [90] proposes solutions for character code con-
version and spelling error correction in Uyghur, Kazakh, and Kyrgyz, aimed at
multilingual information retrieval. Methods for converting non-Unicode charac-
ters to Unicode and root-based query expansion to handle spelling errors are
introduced, enhancing search accuracy and recall in these languages. Although
no specific code is provided, it is claimed that the algorithms for character con-
version and query correction have been tested within the system.
A more recent study [4] presents a manually labeled topic multi-label classifi-
cation dataset of news articles collected from the news site 24.kg. Several baseline
models are evaluated, with results showing that multilingual neural models like
XLM-RoBERTa perform best, which is valuable for advancing Kyrgyz-language
NLP tools. The dataset and models are planned for public release. Additionally,
the construction of a stopwords list (stoplist) — words considered insignificant
for various NLP tasks — is discussed in [24].
A notable contribution, the benchmark described in [81] focuses on cross-
lingual transfer from Turkish to less-resourced Turkic languages like Kyrgyz.
The work presents strategies for improving natural language understanding tasks
through intermediate training and fine-tuning with Turkish, showing significant
accuracy gains for Kyrgyz, which holds potential for future NLP advancements.
All code and models are publicly available for further research and applications.
8
Existing Resources
Dictionaries for Kyrgyz are numerous, listing all of them is beyond the scope
of this paper, however, we would like to emphasize that making them machine-
readable is essential for further progress in corpus creation and overall Kyrgyz
NLP.

--- Page 18 ---

18
A. Alekseev, T. Turatali
Corpora. Manas-UdS corpus [35] contains 1.2 million words from 84 literary
texts across five genres. It includes lemmatization, part-of-speech tags, and rich
metadata. kyWaC, a web corpus of Kyrgyz comprising 19 million words collected
in January 2012 [8]. Leipzig Corpora Collection [47,46,49,48,50] offers community
data, news crawl data, and Wikipedia texts totaling hundreds of thousands of
sentences. TilCorpusu: a 300 million-word corpus including news and fiction data
made public in December 202320.
Syntax Treebanks. UD_Kyrgyz-KTMU : a treebank with 781 sentences anno-
tated with dependency relations [10]; the description has not been yet provided,
though it is clear that the unspecified sources are various: translations of E. Hem-
ingway’s works to Kyrgyz, news articles, etc. the percentages of each genre are
yet to be determined. Kyrgyz-TueCL treebank contains a total of 145 sentences
(including 20 Cairo sentences [64]), and ≈100 sentences suggested by the UD
Turkic Group 21. Translations of all sentences are provided in English, Turkish
and Azerbaijani languages; this dataset is a part of the UD Turkic Treebank.
Other Resources are focused on narrow tasks. WikiANN dataset contains a
Kyrgyz subset for NER tasks, and KyrgyzNER is a dataset currently under de-
velopment, expected to enhance NER capabilities. Used for training respectively
murat/kyrgyz_language_NER22 and TTimur/xlm-roberta-base-kyrgyzNER2324
The previously mentioned word similarity dataset, HJ-Ky-0.1, for evaluating
word embeddings [3], is the first benchmark of its kind for Kyrgyz. It is yet to be
published following the competition event, along with the first topic classification
benchmark [4].
Verbal paradigms for Kyrgyz (100 Kyrgyz verbs fully conjugated in all tenses) [7]
were prepared and published25 for Unimorph by E. Chodroff [97].
For LLM-related evaluation and training, Stanford Alpaca [89] instructions
translated into Kyrgyz using ChatGPT and Google Translate are available on-
line.26
The model mGPT-1.3B-Kirgiz [84], previously mentioned in Section 7.3, has
also been made public.
A joint project by Ulutsoft LLC and the National Commission on the State
Language and Language Policy has resulted in the release of several models on
HuggingFace: a text completion model Mistral-7B-v0.1-kyrgyz-text-completion27,
20 As
of
now,
already
available
at:
https://huggingface.co/datasets/
the-cramer-project/Kyrgyz_News_Corpus.
21 For more information, please see https://github.com/ud-turkic.
22 https://huggingface.co/murat/kyrgyz_language_NER
23 https://huggingface.co/TTimur/xlm-roberta-base-kyrgyzNER
24 KyrgyzNER project heavily depended on the volunteers’ and students’ efforts and
came into being thanks to the collaboration with G. Kabaeva and G. Zhumalieva
(KSTU n. a. I. Razzakov).
25 https://github.com/unimorph/kir
26 https://github.com/Akyl-AI/kyrgyz-alpaca
27 https://huggingface.co/UlutSoftLLC/Mistral-7B-v0.
1-kyrgyz-text-completion

--- Page 19 ---

KyrgyzNLP: Challenges, Progress, and Future
19
a text-to-speech model kyrgyz-tts28, and a speech recognition model whisper-small-kyrgyz29.
While speech processing is not often classified as NLP, related techniques can
play a crucial role in data collection and verification for less-resourced languages.
The Cramer Project’s AkylAI, a smart voice assistant made possible by volun-
teer efforts, is accompanied by an open text-to-speech model30 and several other
models relevant to this study, available at huggingface.co/the-cramer-project
and github.com/Akyl-AI.
For more resources, one may consult an “awesome list” of references: https:
//github.com/alexeyev/awesome-kyrgyz-nlp; this registry is regularly up-
dated, and anyone is welcome to contribute via a pull request.
9
Untapped Subdomains of KyrgyzNLP
Having described the corpus of publicly available research outcomes, it makes
little sense to list the unexplored areas, as “everything else” remains largely
uncharted. However, we aim to highlight the most conspicuous gaps.
9.1
Lacking or Unavailable Language Resources
The variety of language resources required is vast. Here, we aim to emphasize
the necessity of specific datasets and other helpful resources, the lack of which
obstructs multiple paths for Kyrgyz NLP research.
Dictionaries are basic yet essential language resources. Although work on new
dictionaries is ongoing [6] and many human-readable dictionaries exist [42]
(including OCR-ready PDFs), converting them to machine-readable formats
is crucial. A recent dictionary conversion [32] and earlier works [59,13] offer
hope that such efforts will yield resources more easily than before. However,
the core issue is licensing, and obtaining permissions for other dictionaries
and lexicons remains essential for making these tools truly open and usable.
Transliteration tools for languages with multiple scripts, influenced by re-
gion or other factors, are partly available [101], as highlighted in Section 4.
More user-friendly interfaces, benchmarks, and publicly available datasets in
scripts other than Cyrillic are still needed.
Corpora, including a comprehensive National Corpus, are crucial for language
analysis, historical linguistics, and establishing language norms. We discuss
corpus collection and annotation further in Section 10. Additionally, larger
parallel corpora are needed to improve machine translation to and from
Kyrgyz, as indicated by the topics covered in Section 7. From our expe-
rience, many Kyrgyz-language-aware machine translation tools lack estab-
lished glossaries, leading to frequent borrowing of terms from Russian or
English. While there have been efforts in terminology development [106]
28 https://huggingface.co/UlutSoftLLC/kyrgyz-tts
29 https://huggingface.co/UlutSoftLLC/whisper-small-kyrgyz
30 https://huggingface.co/the-cramer-project/TTS_small

--- Page 20 ---

20
A. Alekseev, T. Turatali
and domain-specific dictionaries, e.g., [15], significant work remains in
this area.
Information Extraction datasets, including those for nested NER, OpenIE,
relation extraction, temporal information extraction, entity linking, coref-
erence resolution, etc., are crucial for training and evaluating models that
can support both academic research (e.g., corpus annotation) and industry
applications.
Task-Specific QA & Reading Comprehension datasets, along with other
tasks often considered “AI-hard,” are in high demand. As discussed in Sec-
tion 2, Large Language Models for Kyrgyz are on the horizon, and these
models require evaluation with task-specific data.
Beyond news and encyclopedic content, legal documents data for Kyrgyz
are increasingly available online. Legal NLP is a growing field (see awesome-
legal-nlp, https://nllpw.org/, and many related surveys on Google Scholar).
The need for intelligent processing of official documentation will likely grow in
Kyrgyzstan as well, making this a potentially important area to prioritize in the
near future.
9.2
Untried Methods
From the methodological point of view, as highlighted in Sections 2 and 5, a
large number of techniques traditionally applied for less-resourced languages has
not been implemented or employed. These techniques could significantly speed
up the progress in the field: transfer learning (beyond multiway translation),
cross-lingual models in general, data augmentation and synthesis (beyond the
automatic translation, which is already used), etc.
We list some of the tasks that can aid in corpora annotation and provide the
comments how exactly they can be of some use for the purpose.
Named entity recognition (NER): automatically labeling entities like names,
locations, dates, and organizations in text, NER could provide baseline an-
notations for entities, which annotators can then validate or adjust.
Part-of-speech tagging: assigning PoS tags to words in text is a fundamental
task that serves as a foundation for more complex syntactic and semantic
annotations.
Dependency parsing: this task analyzes the grammatical structure of sen-
tences, assigning tree structures that can be used to automate or guide syn-
tactic annotation processes; the works on treebanks are in progress, please
see the information about the current state in Sections 7.2 and 8.
Coreference resolution: identifying when different expressions refer to the
same entity (e. g., “Meerim’s” and “her” in the same context) aids in cre-
ating coreference annotations by automating entity linking and anaphora
resolution.
Semantic role labeling (SRL): semantic roles are assigned to parts of a sen-
tence, like identifying agents, themes, and goals (e. g., “who did what to
whom”), which assists in annotating event and argument structures.

--- Page 21 ---

KyrgyzNLP: Challenges, Progress, and Future
21
Topic modeling: unsupervised methods like Latent Dirichlet Allocation (LDA) [11],
BERTopic [22], etc. can group texts by topic, helping annotators quickly
identify and label topic-specific text segments within large corpora.
Speech segmentation and speaker diarization: segmenting audio into units
like words, phrases, and sentences, and distinguishing between speakers, fa-
cilitates annotation of multi-speaker conversations or interviews, which is
essential e. g. in building the spoken part of the corpus.
Word sense disambiguation (WSD): identifying the correct sense of a pol-
ysemous word based on context aids in annotating corpora where accurate
word senses are crucial for semantics.
Event detection and temporal tagging: identifying events, their participants,
and temporal information supports the annotation of chronological narra-
tives and event-based corpora, often used in news and historical text.
Text classification for domain labeling: automatically assigning documents
to predefined categories (e.g., news, sports, science) helps streamline the la-
beling process in domain-specific corpora.
Paraphrase detection: identifying similar phrases or sentences can assist an-
notators by flagging repetitive content, reducing manual work when labeling
similar or redundant text.
Automatic summarization: creating summaries for large documents can help
annotators quickly grasp content, especially for annotation tasks that involve
long texts.
Dependency and alignment mapping for parallel texts: for bilingual or
multilingual corpora, aligning segments between two languages can aid an-
notation, especially for translation or language comparison tasks.
Active learning and uncertainty sampling: ML models can suggest sam-
ples that are uncertain or difficult for the model, prioritizing them for human
annotation and reducing redundant labeling of easy cases.
Anomaly detection: identifying outliers or unusual patterns in text can help
annotators focus on rare or unexpected cases, especially useful in large
datasets where anomalies might carry significant insights.
Automatic image and video tagging (for multimodal corpora): if the cor-
pus includes images or videos, tagging objects or actions automatically can
assist annotators working on multimodal data by generating preliminary la-
bels.
This list is far from comprehensive, but it underscores the wide range of op-
portunities in Kyrgyz NLP. In the next section, we propose our vision for the
development of Kyrgyz NLP. However, there are many additional ways for in-
dependent contributions to progress in parallel.
10
Roadmap for Kyrgyz NLP Development
10.1
Proposed Milestones
Developing Kyrgyz NLP requires a multifaceted approach that addresses the
core linguistic challenges of the Kyrgyz language, as well as practical steps to

--- Page 22 ---

22
A. Alekseev, T. Turatali
ensure sustainability and growth. Below is a development roadmap broken down
into specific steps, and then a timeline with three possible scenarios: the best
case (with government support), the suboptimal case (minor or no support from
the officials, and a certain involvement of the private sector), and the worst case
(academic and community-based work without any external support whatso-
ever).
Fig. 3. Milestones.
Data Collection and Annotation
Step 1: Raw Data Collection and Other Preliminaries. The foundation of Kyrgyz
corpus linguistics and overall empirical language science lies in the creation of a
comprehensive and diverse corpus, which should serve as the essential dataset for
training and developing language models. The process must begin by gathering
extensive datasets of Kyrgyz text from a variety of sources. These sources include
literature, social media, news articles, academic publications, government doc-
uments, and other written materials that capture the full range of formal and
informal language usage. This diversity is essential to ensure that the models
represent the language accurately across different contexts, from casual conver-
sation to formal communication.
Beyond raw data collection, it is critical to develop a robust suite of lin-
guistic resources to support and expedite the annotation process. This includes
digitized dictionaries, thesauri, and small pre-trained models that can stream-
line tasks such as syntactic analysis, morphological tagging, and part-of-speech
labeling. These resources are foundational to achieving consistent, high-quality

--- Page 23 ---

KyrgyzNLP: Challenges, Progress, and Future
23
annotation. They also lay the groundwork for more efficient and scalable corpus
processing, as models can rely on existing linguistic information to make quicker
and more accurate decisions. Without these tools, creating a well-annotated cor-
pus for Kyrgyz would be significantly slower and more prone to errors, which
could impact the performance of the final language models.
To further enhance the corpus, spoken language should be incorporated
alongside written text. This can be achieved by collecting and transcribing audio
recordings from interviews, podcasts, radio broadcasts, and everyday conversa-
tional exchanges. Including both written and spoken language is crucial, as it
allows the model to understand and process different styles, dialects, and nuances
that occur in natural speech, which are often absent in written texts.
A robust corpus should also include metadata on regional dialects, language
variations, and other sociolinguistic factors that can affect word choice, syntax,
and tone. Additionally, steps must be taken to clean and preprocess the data, re-
moving noise while preserving essential linguistic structures and variations. This
process may involve filtering out irrelevant or low-quality content and structuring
the data for easier processing by NLP algorithms.
Once a sufficiently large and representative corpus is compiled, not only can
it be used for purely linguistic and documenting purposes (including updating
the dictionaries, revising the grammar, historical linguistics, etc.), it can also
be used to develop models that recognize, interpret, and generate Kyrgyz lan-
guage with a high degree of accuracy, supporting downstream tasks such as
machine translation, code switch detection, sentiment analysis, text generation,
and many, many others.
Step 2: Data Cleaning and Preprocessing. Once the Kyrgyz corpus of unpro-
cessed texts has been assembled, the next crucial step is to clean and preprocess
the data, ensuring it is of high quality. This phase begins with systematically
removing duplicates, irrelevant information, and any noise that may interfere
with the accuracy of language models and linguistic analysis. Redundant text,
unrelated content, and malformed entries need to be carefully filtered out to
retain only the most relevant linguistic data.
After the initial cleanup, the text undergoes normalization, a process that
aligns various forms of the language entities (e. g. words) into a consistent format.
Given that Kyrgyz is spoken in diverse dialects and includes informal language
variations, normalization is vital to ensure that the corpus represents standard
forms that can be uniformly processed. This normalization also involves address-
ing differences in spelling, common informal expressions, and slang. Addition-
ally, since Kyrgyz speakers often use different writing systems (such as Cyrillic,
Perso-Arabic, or Latin), the data must be transliterated to a standardized script
(however, preserving the original one). This step allows the model to manage
variations due to transliteration or non-standard typing practices, commonly
encountered on digital platforms and social media.
By the end of the data cleaning and preprocessing phase, the corpus is trans-
formed into a well-structured, consistent, and high-quality dataset. These refined
data provide a solid foundation for ensuring reliable linguistic analysis and train-

--- Page 24 ---

24
A. Alekseev, T. Turatali
ing language models and other ML-based instruments, helping them understand
the nuances and structures of Kyrgyz language while filtering out errors or in-
consistencies that could negatively impact model performance.
Step 3: Annotation for NLP Tasks and Corpus Querying. With a clean and
structured corpus, the next step is to annotate the dataset for specific NLP
tasks, a critical process that allows language scientists to explore the laws and
regularities of the Kyrgyz language and enables models to learn and perform
essential linguistic functions. Annotation involves labeling text data to highlight
parts of speech (PoS), build the syntax trees, identify named entities, determine
sentiment, and mark other important linguistic features. Each of these tasks
provides unique insights: POS tagging, for example, helps understand the gram-
matical roles of words within sentences, while Named Entity Recognition (NER)
identifies names of people, places, organizations, and other key entities, facilitat-
ing more accurate comprehension of context. Sentiment analysis, in turn, adds
emotional or opinion-based interpretation, which is valuable for tasks like ana-
lyzing public opinion, customer feedback, or the emotional variation patterns in
prose and poetry.
To ensure that the annotation is accurate and reliable, guidelines must be cre-
ated and strictly followed throughout the annotation process. These guidelines
should specify rules for handling ambiguities, dialectal variations, and context-
specific interpretations, offering annotators clear instructions on how to label
each aspect of the text consistently. Additionally, if multiple annotators are work-
ing on the dataset, these guidelines help maintain uniformity, reducing variability
and potential errors that could impact model training.
Once completed, the annotated corpus becomes a rich resource for Kyrgyz
language studies as well as for training the machine learning models, enabling
them to understand complex aspects of the Kyrgyz language such as syntax,
context, and sentiment. This annotated dataset should support a wide range of
NLP applications, from syntax parsing to semantic role labeling, from translation
and summarization to question answering and conversational AI, providing the
necessary foundation for sophisticated language processing capabilities and in-
depth analysis.
Model Development and Training.
Step 1: Baseline Models for Key NLP Tasks. The initial focus should be on
creating basic models to perform essential NLP tasks like part-of-speech (POS)
tagging, Named Entity Recognition (NER), and machine translation, etc. These
fundamental models form the backbone of more advanced applications and en-
able the system to recognize grammatical structures, identify key entities, and
translate between Kyrgyz and other languages. By training on the annotated
corpus, the models learn to accurately tag and classify words within sentences,
paving the way for more complex language processing capabilities. These founda-
tional models are crucial for developing language understanding and generation
systems that can handle Kyrgyz-specific linguistic nuances.

--- Page 25 ---

KyrgyzNLP: Challenges, Progress, and Future
25
Step 2: Kyrgyz Bilingual Models. To support cross-linguistic applications, the
next step is to develop bilingual models that facilitate translation and com-
munication between Kyrgyz and widely used languages like Russian and En-
glish. These models enable users to interact seamlessly in multiple languages
and broaden the accessibility of Kyrgyz NLP applications. Developing Kyrgyz-
Russian-Kyrgyz and Kyrgyz-English-Kyrgyz translation models is particularly
important given the linguistic diversity in the region and the need for efficient
communication across language barriers. By leveraging parallel datasets and
aligning structures across languages, these bilingual models could serve as valu-
able tools for both general and specialized translation tasks.
Step 3: Transfer Learning and Pretrained Models. In this phase, transfer learn-
ing techniques are applied to leverage existing powerful models, such as BERT
and GPT, which have already been trained on massive datasets. These mod-
els could be fine-tuned on Kyrgyz-specific datasets (as well as on raw data in
related languages), allowing them to adapt to the unique characteristics of the
Kyrgyz language without starting from scratch. Fine-tuning pre-trained models
saves both time and resources, while also improving the quality and accuracy of
Kyrgyz NLP tasks. This step enables the model to grasp specific Kyrgyz lan-
guage patterns and vocabulary, enhancing its relevance and performance across
different applications.
Step 4: Open-Source Kyrgyz NLP Library. The final stage in model develop-
ment could be the creation of an open-source NLP library dedicated to Kyrgyz
language processing. This library would compile a suite of ready-to-use models
for tasks such as text classification, language generation, sentiment analysis, and
more. Making this library open-source ensures that researchers, developers, and
educators have easy and straightforward access to Kyrgyz NLP tools, fostering
further innovation and collaboration. By offering a range of functionalities in
one accessible platform, this library could empower users to build and expand
upon Kyrgyz NLP applications, driving growth in both linguistic technology and
cultural preservation.
Community Involvement and Ecosystem Development. Developing a
sustainable and impactful Kyrgyz NLP ecosystem requires active community
engagement and strong partnerships. This phase is dedicated to building a ro-
bust network involving academia, software developers, researchers, government
entities, and the private sector, each contributing to advancing Kyrgyz NLP.
Step 1: Partnerships with Academia. To establish a research-driven foundation
for Kyrgyz NLP, partnerships with local universities and language institutions
are essential. Collaborating with academia allows for the formation of specialized
research teams focused on exploring and solving linguistic challenges unique to
the Kyrgyz language. By engaging linguistics and computer science departments,
these collaborations can provide students and faculty with hands-on experience

--- Page 26 ---

26
A. Alekseev, T. Turatali
in NLP research and development, creating a pipeline of skilled professionals.
Joint projects with universities and language experts can also lead to innovations
in language modeling, semantic analysis, and translation, further advancing the
field of Kyrgyz NLP.
Step 2: Software Developers and Researchers Engagement. Encouraging active
participation from developers and researchers accelerates progress in Kyrgyz
NLP. This step includes organizing open challenges, hackathons, and funding
initiatives that inspire developers and researchers to contribute their skills and
ideas. One of the exemplary efforts is The Cramer Project, which organizes
hackathons and datathons for developers and researchers. For example, they
have hosted three datathons focused on advancing Kyrgyz NLP with support
of High Technology Park of the Kyrgyz Republic, Ulutsoft, KSTU named after
Iskhak Razzakov: MNIST31, morphology32, and NER33. These events provide
participants with hands-on experience in solving real linguistic challenges and
building practical tools for Kyrgyz language processing.
By offering prizes, grants, and networking opportunities, these events make
it possible for anyone interested in Kyrgyz NLP to participate in meaningful
projects. Through hackathons, developers and students can work on specific NLP
tasks, from sentiment analysis to NLU, while researchers may delve into more
complex linguistic issues. This open collaboration not only fosters innovation but
also creates a growing community of Kyrgyz NLP enthusiasts who can continue
contributing to the ecosystem.
Step 3: Government and Private Sector Collaboration. Government and private
sector support is critical to ensuring that Kyrgyz language technology receives
adequate resources and visibility. Advocacy for government involvement can en-
courage the integration of Kyrgyz NLP applications into the public services
and digital platforms (which is already being done, following the corresponding
lawmaking initiatives). A digital-first approach allows government services to
reach more citizens by communicating in Kyrgyz and sets a strong example for
other organizations. In addition, collaboration with private companies is key to
securing investments in Kyrgyz-language tech products, from smart devices to
language-learning applications. By engaging the private sector, Kyrgyz NLP can
become a viable business area, driving innovation in the industry.
This multi-pronged approach to community and ecosystem development helps
ensure that Kyrgyz NLP is not only technically sound but also supported by a
wide range of stakeholders, paving the way for sustainable growth and long-term
impact.
Deployment and Adoption. The final phase focuses on bringing Kyrgyz NLP
models to practical use and establishing a sustainable framework for ongoing
31 https://thecramer.com/blog/datathon-1
32 https://thecramer.com/blog/datathon-2
33 https://thecramer.com/blog/datathon-3

--- Page 27 ---

KyrgyzNLP: Challenges, Progress, and Future
27
development. Deployment and adoption are key to making Kyrgyz language
technology accessible to the public, ensuring its relevance, and fostering long-
term growth.
Step 1: Integrating Kyrgyz NLP in Everyday Use. To maximize impact, Kyrgyz
NLP models should be integrated into public services and digital platforms used
by the Kyrgyz-speaking community. This involves introducing Kyrgyz NLP tools
such as translation services, virtual assistants, and e-governance applications
that make everyday interactions and transactions more accessible in Kyrgyz.
For instance, a Kyrgyz virtual assistant could streamline access to government
services or provide localized information, while a reliable Kyrgyz translation tool
could bridge language barriers in public communication. Beyond public services,
promotion of the Kyrgyz language within popular tech spaces like social media
platforms, messaging apps, and mobile applications can ease their everyday use.
By embedding Kyrgyz language support into widely-used platforms, the lan-
guage may become more accessible, modernized, and widely embraced within
the digital ecosystem.
Step 2: Ongoing Maintenance and Updates For Kyrgyz NLP to remain effective
and relevant, it requires continuous updates and maintenance. Language evolves
over time, and so do the needs of its speakers, making it essential to keep NLP
models aligned with these changes. A sustainable model for ongoing updates can
be established by forming partnerships with research institutions, engaging the
developer community, and securing funding from both public and private sectors.
This model would allow for periodic improvements, expansion of the corpus with
new data, and the retraining of models to account for emerging language trends,
slang, or newly adopted terminology. By prioritizing consistent maintenance,
Kyrgyz NLP tools can adapt to evolving linguistic and technological demands,
ensuring they continue to serve users effectively and foster widespread adoption.
10.2
Timeline
The roadmap summarized in Fig. 4 outlines key priorities and steps for devel-
oping Kyrgyz NLP, emphasizing how the involvement of various stakeholders
(government, private sector, and academic community) can impact the speed
and scope of overall progress in the field, as well as the adoptability of tech-
niques of primary interest.
The Best Scenario: Full Government Support
Year 1
– Government endorses and funds Kyrgyz NLP development.
– Large-scale data collection from public libraries, public records, and media
outlets (with all licensing questions solved).

--- Page 28 ---

28
A. Alekseev, T. Turatali
Fig. 4. Timelines with scenarios.
– Partnerships with local universities for annotation work are established (and
encouraged by the high authorities).
– First baseline models for POS tagging and translation are prepared — to-
gether with reliable (large enough) benchmarks for evaluation.
– Support open-source Kyrgyz NLP initiatives: hackathons, challenges, con-
ferences.
Year 2
– The dataset collection process is expanded, integration of the speech data
from the public and private sources is carried out.
– Development advanced models (NER, sentiment analysis, machine transla-
tion).
– The available models are integrated into the public sector applications (e.
g., chatbots, e-governance).
– The software developers interested in the promotion of the Kyrgyz NLP
engage in open-source products-related collaborations and hackathons.
Year 3-4
– Continued government support ensures long-term sustainability.
– Kyrgyz NLP becomes a core part of the educational system in Kyrgyzstan.
– Kyrgyz tech products reach a certain level of maturity (popularity of the
voice assistants, search engines, etc. with end users).
– Kyrgyz NLP models are widely adopted in the government and business
sectors.

--- Page 29 ---

KyrgyzNLP: Challenges, Progress, and Future
29
Suboptimal Scenario (without full government involvement, but with
private sector support)
Year 1
– Private companies (e. g., tech firms) fund data collection and initial model
development.
– First models for POS tagging, basic translation, and text classification are
released.
Year 2
– Data collection with volunteers’ aid and collaborations with universities is
done continuously.
– Kyrgyz-Russian and Kyrgyz-English translation models are developed and
evaluated.
– Industry adoption starts: Kyrgyz chatbots and customer support tools for
businesses.
Year 3-4
– Continuous improvements are introduced into the popular task models (NER,
sentiment analysis).
– Kyrgyz-language tech products (smart speakers, apps) enter the market.
– Limited adoption in the public sector; mostly driven by private companies.
Worst Scenario (minimal support)
Year 1
– Data collection is slow and mainly community-driven (crowdsourcing, stu-
dent projects).
– The baseline models for POS tagging and translation are developed, but at
a slow pace.
– The overall progress is limited due to the lack of funding and minimal human,
data and computational resources.
Year 2
– The development of other models (NER, sentiment analysis) is slow.
– The results’ industry adoption is minimal; mostly used within academic and
research circles.
Year 3-4
– Limited tech applications; Kyrgyz remains underrepresented in terms of dig-
ital tools.
– Some isolated academic projects do continue, but with slow progress.
– Kyrgyz NLP stagnates without sufficient funding or interest.

--- Page 30 ---

30
A. Alekseev, T. Turatali
11
Conclusion
Advancing Kyrgyz NLP is crucial for ensuring the language’s vitality in the
digital age. Each step forward in developing NLP for less-resourced languages like
Kyrgyz contributes to a more inclusive and linguistically diverse technological
landscape, both now and in the future.
The advancement of Kyrgyz NLP presents both challenges and opportuni-
ties. Although the language faces significant obstacles due to resource limitations
and linguistic complexity, there remains ample room for contributions from re-
searchers, practitioners, and the community.
This overview may serve as a resource for researchers, developers, students,
and policymakers engaged in Kyrgyz NLP and other less-resourced languages. By
highlighting both progress and remaining challenges, we seek to inspire further
research and development in this field.
The proposed roadmap emphasizes collaborative efforts across academia, in-
dustry, and government, focusing on developing larger, more diverse datasets,
adapting state-of-the-art NLP techniques to Kyrgyz, and creating standardized
evaluation benchmarks. Close collaboration among all interested parties is
essential to overcoming current challenges.
We advocate for sustained efforts in data annotation, tool development, and
model training, especially in the age of LLMs. The unique characteristics of each
language require specialized approaches, and success with one language does not
guarantee success with others.
By uniting our efforts, we can ensure that the Kyrgyz language is not left
behind in the global advancement of NLP technologies. The preservation and
development of Kyrgyz not only benefit its native speakers but also enrich the
diversity of global linguistic resources.
Acknowledgments. The work of A. Alekseev was supported by the Russian Science
Foundation grant #23-11-00358. We express our sincere gratitude to the researchers,
practitioners, and community members who have contributed to the development of
Kyrgyz NLP resources and tools, as well as our collaborators and volunteers who
supported data annotation and model development. Your commitment is essential in
advancing the field and preserving the Kyrgyz language. We extend special thanks to
those whose enthusiasm and moral support have inspired our ongoing engagement with
both earlier and recent developments in Kyrgyz NLP, forming the foundation of this
paper. We thank G. Dzhumalieva and A. Kasieva for their invaluable consultations
on examples for this paper, and A. Tillabaeva for insightful discussions on corpus
linguistics. A. A. also acknowledges his advisor, G. Dzh. Kabaeva, for her trust and
invaluable support throughout this endeavor, and S. I. Nikolenko for his assistance with
proofreading the manuscript.
References
1. Abduvaliev, I., Sadykov, T. S.: Азыркы кыргыз тили: морфология: жогорку
окуу жайларынын филология факультеттеринин студенттери үчүн окуу ки-

--- Page 31 ---

KyrgyzNLP: Challenges, Progress, and Future
31
теп. «Kyrgyzstan-Soros» fondu (1997)
2. Ablimit, M., Parhat, S., Hamdulla, A., Zheng, T. F.: A multilingual language
processing tool for Uyghur, Kazak and Kirghiz. In: 2017 Asia-Pacific Signal and
Information Processing Association Annual Summit and Conference (APSIPA
ASC). pp. 737–740. IEEE (2017)
3. Alekseev, A., Kabaeva, G.: HJ-Ky-0.1: набор данных для оценки качества век-
торных представлений слов кыргызского языка. Herald of KSTU 4 (2023)
4. Alekseev, A., Nikolenko, S. I., Kabaeva, G.: Benchmarking Multilabel topic Clas-
sification in the Kyrgyz language (2023)
5. Ali, S., Murat, A.: Improved Character-Based neural network for pos tagging on
Morphologically rich languages. Journal of Information Processing Systems 19(3)
(2023)
6. Arikoglu, E.: Словарный проект современного кыргызского языка. In: Obshch-
estvo, yazyk i kultura XXI veka. pp. 85–91 (2021)
7. Aytnatova, A.: Kyrgyz Language: 100 Kyrgyz Verbs Fully Conjugated in All
Tenses. CreateSpace Independent Publishing Platform, Online (2016), [Accessed
via
Amazon:
https://www.amazon.com/Kyrgyz-Language-Verbs-Conjugated-
Tenses/dp/1523494158]
8. Baisa, V., Suchomel, V.: Turkic language support in sketch Engine. In: Proceed-
ings of the International conference “Turkic Languages Processing” TurkLang-
2015. pp. 214–223 (2015)
9. Bakasova, P. S., Israilova, N. A.: Algoritm obrazovaniya slovoform dlya avtomati-
zatsii protsedury popolneniya bazy dannykh slovarya (in russian). Izvestiya Kyr-
gyzskogo gosudarstvennogo tekhnicheskogo universiteta im. I. Razzakova 38(2),
23–27 (2016)
10. Benli, I.: UD_Kyrgyz-KTMU: UD for Kyrgyz (2023), https://github.com/
UniversalDependencies/UD_Kyrgyz-KTMU/
11. Blei, D. M., Ng, A. Y., Jordan, M. I.: Latent Dirichlet Allocation. Journal of
machine Learning research 3(Jan), 993–1022 (2003)
12. BNC Consortium: The British National Corpus, XML Edition. http://hdl.
handle.net/20.500.14106/2554 (2007), Oxford Text Archive
13. Boizou, L., Mambetkazieva, D.: From Kyrgyz internet texts to an xMl Full-form
Annotated lexicon: a simple semi-automatic pipeline. In: TurkLang 2017: Pyataya
mezhdunarodnaya konferentsiya po kompyuternoy obrabotke tyurkskikh yazykov:
Trudy konferentsii. T 1. Kazan: Izdatelstvo Akademii nauk Respubliki Tatarstan,
2017. Kazan: Izdatelstvo Akademii nauk Respubliki Tatarstan, 2017 (2017)
14. CNN Business: AI is replacing human tasks faster than you think. https:
//edition.cnn.com/2024/06/20/business/ai-jobs-workers-replacing/
index.html (June 2024), accessed: 2024-11-04
15. Committee on Education, Science, Culture & Sports of the Jogorku Kenesh of
the Kyrgyz Republic (editorial board), Tölögönova, S., Davletbayeva, M., Bon-
darenko, O., Teñirbergenova, J.: Русско-кыргызский словарь юридических тер-
минов и иных понятий. Bishkek: “Turar” (2014)
16. Devlin, J., Chang, M.-W., Lee, K., Toutanova, K.: Bert: Pre-training of deep
bidirectional transformers for language understanding. In: Proceedings of the 2019
Conference of the North American Chapter of the Association for Computational
Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers).
pp. 4171–4186 (2019)
17. Dzhumalieva, G. K., Kasieva, A. A., Musazhanova, S. Zh.: Адаптация терми-
нов веб-проекта «Универсальные зависимости» на кыргызский язык. Vestnik
KRSU 23 (6), 71–75 (2023)

--- Page 32 ---

32
A. Alekseev, T. Turatali
18. Dzhumashova, A.: President Congratulates Kyrgyzstanis on State Language Day.
https://24.kg/english/275789_President_congratulates_Kyrgyzstanis_
on_State_Language_Day/ (September 2023), accessed: 2024-11-04
19. Forcada, M. L., Tyers, F. M.: Apertium: a free/open source platform for
machine translation and basic language technology. In: Proceedings of the
19th Annual Conference of the European Association for Machine Translation:
Projects/Products. Baltic Journal of Modern Computing, Riga, Latvia (May 30–
Jun 1 2016), https://aclanthology.org/2016.eamt-2.4
20. Gatiatullin, A., Suleymanov, D., Prokopyev, N., Khakimov, B.: About Turkic
Morpheme Portal. In: CMCL. pp. 226–243 (2020)
21. Google:
Google
Gemini:
Next-Generation
Model
/
Per-
formance
(2024),
https://blog.google/technology/ai/
google-gemini-next-generation-model-february-2024/#performance,
accessed: 2024-10-29
22. Grootendorst, M.: BERTopic: Neural topic modeling with a class-based TF-IDF
procedure. arXiv preprint arXiv:2203.05794 (2022)
23. Hoang, C. D. V., Koehn, P., Haffari, G., Cohn, T.: Iterative back-translation for
neural machine translation. In: 2nd Workshop on Neural Machine Translation
and Generation. pp. 18–24. Association for Computational Linguistics (2018)
24. Isaev, R., Esenalieva, G., Doszhanov, E.: Towards Kyrgyz stop words. Kalbotyra
76, 54–65 (2023)
25. Israilova, N. A.: Алгоритм морфологического анализа и синтеза в транслято-
ре. Современные проблемы механики 2(28), 11–19 (2017)
26. Israilova, N. A., Bakasova, P. S.: Morphological analyzer of the kyrgyz language
(in russian). In: Proceedings of the V International Conference on Computer
Processing of Turkic Languages Turklang. vol. 2, pp. 100–116 (2017)
27. Israilova, N. A., Bakasova, P. S.: Онтологические модели морфологических
правил кыргызского языка. In: Sedmaya Mezhdunarodnaya konferentsiya po
kompyuternoy obrabotke tyurkskikh yazykov «TurkLang 2019»: Trudy konfer-
entsii (Simferopol, Krym, Rossiya, 3–5 oktyabrya 2019 g.) (2019)
28. Joshi, P., Santy, S., Budhiraja, A., Bali, K., Choudhury, M.: The state and fate
of linguistic diversity and inclusion in the nlp world. In: Proceedings of the 58th
Annual Meeting of the Association for Computational Linguistics. pp. 6282–6293
(2020)
29. Karabaeva, S. Zh.: Virtualnye geometricheskie obekty, sozdavaemye glagolami
v kyrgyzskom yazyke (in russian). V mire nauki i iskusstva: voprosy filologii,
iskusstvovedeni i kulturologii 66(11), 74–79 (2016)
30. Karabaeva, S. Zh., Dolmatova, P., Imanalieva, A.: Computer-Mathematical Mod-
eling of National Specificity of Spatial Models in Kyrgyz Language. In: Proceed-
ings of the International conference “Turkic Languages Processing” TurkLang-
2015. pp. 416–422 (2015)
31. Kasieva, A. A., Dzhumalieva, G. K., Thompson, A., Jumashev, M., Chontaeva,
B., Washington, J. N.: Проблемы кыргызской синтаксической аннотации в
фреймворке Universal Dependencies. In: TurkLang, Buxoro (2023)
32. Kasieva, A. A., Dzhumalieva, G. K., Jumashev, M., Tursunova, A., Ryspakova,
M., Washington, J. N.: Structured Data from Dictionary text: Applying large lan-
guage Model in low-resource Kyrgyz lexicography. In: Proceedings of the 12th In-
ternational Conference on Analysis of Images, Social Networks, and Texts (AIST
2024). To appear in Lecture Notes in Computer Science (LNCS), Springer (2024)

--- Page 33 ---

KyrgyzNLP: Challenges, Progress, and Future
33
33. Kasieva, A. A., Kadyrbekova, A. K.: Corpus Annotation Tools: Kyrgyz Language
Corpus (Using Turkic Lexicon Apertium and Penn Treebank Tools). In: Obshch-
estvo, yazyk i kultura XXI veka. pp. 207–214 (2021)
34. Kasieva, A. A., Kadyrbekova, A. K.: КЫРГЫЗ ТИЛИНДЕГИ ЭТИШТЕР-
ДИН КОШ МААНИЛҮҮЛҮГҮН ЖОЮУ (жаны түзүлгөн кыргыз тилинин
корпусунун негизинде). Izvestiya Vuzov Kyrgyzstana 6 (2022)
35. Kasieva, A. A., Knappen, J., Fischer, S., Teich, E.: A new Kyrgyz corpus: sam-
pling, compilation, annotation. In: Jahrestagung der Deutschen Gesellschaft für
Sprachwissenschaft (poster session) (2020), http://hdl.handle.net/21.11119/
0000-0004-{B}62{D}-{D}
36. Kasieva, A. A., Satybekova, A. T.: Частеречные разметки для нового корпу-
са кыргызского языка (Инструментарий Turkic Lexicon Apertium). Вестник
Кыргызско-Российского Славянского университета 20(6), 67–72 (2020)
37. Kasieva, A. A., Satybekova, A. T.: Parts-of-Speech Annotation of the Newly Cre-
ated Kyrgyz Corpus (in Russian). Herald of KRSU 20(6), 67–72 (2020)
38. Kochkonbaeva, B. O.: Tabigyy tildegi tekstterdi orus tilinen kyrgyz tiline
mashinalyk kotoruuda sezderdy analizdoonun algoritmin tyzyy / Development of
Algorithm Analysis of Words in Natural Text Machine Translation from Russian
into Kyrgyz (in Kyrgyz). Izvestiya Kyrgyzskogo gosudarstvennogo tekhnicheskogo
universiteta im. I. Razzakova 2(38), 52–54 (2016)
39. Kochkonbaeva, B. O.: О морфологическом анализе в приложениях автомати-
ческой обработки текста. Byulleten nauki i praktiki 4(12), 608–612 (2018)
40. Kochkonbaeva, B. O., Aldosova, A.: Automatic processing of text in natural lan-
guage. Byulleten nauki i praktiki 4(7), 216–221 (2018)
41. Kochkonbaeva, B. O., Egemberdieva, Zh. S.: Modeling of Morphological Analysis
and synthesis of word Forms of the natural language. Byulleten nauki i praktiki
6(9), 435–439 (2020)
42. Koshueva, M., Abduvalieva, E., Zholdoshova, A., Karaeva, N., Osmonova, A.,
Shaimkulova, R., Abdullaeva, Zh.: Kyrgyz Lexicography in the 20th-21st Cen-
turies. Open Journal of Modern Linguistics 11(5), 719–726 (2021)
43. Kraft,
A.:
Microsoft
shuts
down
AI
chatbot
after
it
turned
into
a
Nazi.
https://www.cbsnews.com/news/
microsoft-shuts-down-ai-chatbot-after-it-turned-into-racist-nazi/
(2016), accessed: 2024-11-01
44. Lample, G., Ott, M., Conneau, A., Denoyer, L., Ranzato, M.: Phrase-based &
neural unsupervised machine translation. In: Proceedings of the 2018 Conference
on Empirical Methods in Natural Language Processing. pp. 5039–5049 (2018)
45. Lee, J., Yoon, W., Kim, S., Kim, D., Kim, S., So, C.H., Kang, J.: Biobert: a pre-
trained biomedical language representation model for biomedical text mining.
Bioinformatics 36(4), 1234–1240 (2020)
46. Leipzig Corpora Collection: Kyrgyz community corpus based on material
from 2017. https://corpora.uni-leipzig.de?corpusId=kir_community_2017,
accessed: 2024-11-01
47. Leipzig Corpora Collection: Kyrgyz news corpus based on material crawled
in 2011. https://corpora.uni-leipzig.de?corpusId=kir_newscrawl_2011, ac-
cessed: 2024-11-01
48. Leipzig Corpora Collection: Kyrgyz news corpus based on material from 2020.
https://corpora.uni-leipzig.de?corpusId=kir_news_2020,
accessed:
2024-
11-01

--- Page 34 ---

34
A. Alekseev, T. Turatali
49. Leipzig Corpora Collection: Kyrgyz web text corpus (kyrgyzstan) based on mate-
rial from 2019. https://corpora.uni-leipzig.de?corpusId=kir-kg_web_2019,
accessed: 2024-11-01
50. Leipzig
Corpora
Collection:
Kyrgyz
wikipedia
corpus
based
on
material
from 2021. https://corpora.uni-leipzig.de?corpusId=kir_wikipedia_2021,
accessed: 2024-11-01
51. Lindsay, R.: Mutual Intelligibility among the Turkic Languages. In: Endangered
Turkic Languages I: Theoretical and General Approaches, pp. 311–384. Interna-
tional Turkic Academy, Astana, Kazakhstan (2016)
52. Li, X., Li, Z., Sheng, J., Slamu, W.: Low-resource text classification via cross-
lingual language model fine-tuning. In: China National Conference on Chinese
Computational Linguistics. pp. 231–246. Springer (2020)
53. Li, Z., Li, X., Sheng, J., Slamu, W.: AgglutiFit: efficient low-resource agglutinative
language model fine-tuning. IEEE Access 8, 148489–148499 (2020)
54. Marcus, M., Santorini, B., Marcinkiewicz, M. A.: Building a large annotated
corpus of english: The penn treebank. Computational linguistics 19(2), 313–330
(1993)
55. de Marneffe, M. C., Manning, C. D., Nivre, J., Zeman, D.: Universal Dependen-
cies. Computational Linguistics 47(2), 255–308 (07 2021). https://doi.org/10.
1162/coli_a_00402, https://doi.org/10.1162/coli_a_00402
56. Miftahutdinov, Z., Alimova, I., Tutubalina, E.: KFU NLP team at SMM4H 2019
tasks: Want to extract adverse drugs reactions from tweets? BERT to the res-
cue. In: Proceedings of the fourth social media mining for health applications (#
SMM4H) workshop & shared task. pp. 52–57 (2019)
57. Mirzakhalov, J., Babu, A., Ataman, D., Kariev, Sh., Tyers, F. M., Abduraufov, O.,
Hajili, M., Ivanova, S., Khaytbaev, A., Laverghetta, A., Moydinboyev, B., Onal,
E., Pulatova, Sh., Wahab, A., Firat, O., Chellappan, S.: A large-scale study of
Machine translation in turkic languages. In: Proceedings of the 2021 Conference
on Empirical Methods in Natural Language Processing. pp. 5876–5890 (2021)
58. Mirzakhalov, J., Babu, A., Kunafin, A., Wahab, A., Moydinboyev, B., Ivanova,
S., Uzokova, M., Pulatova, Sh., Ataman, D., Kreutzer, J., Tyers, F. M., Firat,
O., Li, X., Chellappan, S.: Evaluating Multiway Multilingual nMt in the turkic
languages. In: Proceedings of the Sixth Conference on Machine Translation. pp.
518–530 (2021)
59. Momunaliev, K. Z.: Parsing and annotation of the Turkish-Kyrgyz Dictionary.
Izvestiya Kyrgyzskogo gosudarstvennogo tekhnicheskogo universiteta im. I. Raz-
zakova 38(2), 68–81 (2016)
60. Musayev, S. Zh., Karabaeva, S. Zh., Imanalieva, A.: Проблемы и перспекти-
вы развития компьютерной лингвистики в Кыргызстане. In: Proceedings of
the I International Conference on Computer processing of Turkic Languages
(TurkLang-2013). pp. 34–37 (2013)
61. Musazhanova, S. Zh., Kasieva, A. A., Dzhumalieva, G. K.: Cинтаксическая ан-
нотация кыргызского языка на основе новосозданного корпуса. Vestnik Issyk-
Kulskogo universiteta 54 (2), 140–148 (2023)
62. National
Statistical
Committee
of
the
Kyrgyz
Republic:
El
zhana
turak-zhay
fondun
kattoo/
Uluttuk
statistika
komiteti
(in
Kyr-
gyz)
(2013),
https://www.stat.gov.kg/media/publicationarchive/
0f717d2d-5078-4e18-8b56-fb2a530462a2.pdf
63. Nazirova, E., Abdurakhmonova, N., Abidova, Sh., Uzakova, M.: Морфологиче-
ский анализ словоформ в узбекском, каракалпакском и кыргызском языках,
принадлежащих к тюркской семье языков. In: TurkLang, Buxoro (2023)

--- Page 35 ---

KyrgyzNLP: Challenges, Progress, and Future
35
64. Nivre, J.: Towards a universal grammar for natural language processing. In: Inter-
national conference on intelligent text processing and computational linguistics.
pp. 3–16. Springer (2015)
65. Pankov, P. S.: Обучающая и контролирующая программа по словоизменению
в кыргызском языке на ПЭВМ. Bishkek: Mektep p. 20 (1992)
66. Polat, Y., Zakirov, A., Bajak, S., Mamatzhanova, Z.: Machine translation for Kyr-
gyz proverbs—Google translate vs. yandex translate-From Kyrgyz into English
and turkish. In: Materialy Shestoy Mezhdunarodnoy konferentsii po kompyuter-
noy obrabotke tyurkskikh yazykov «TurkLang-2018»(Tashkent, Uzbekistan, 18–
20 oktyabrya 2018 g.) (2018)
67. Rahimi, A., Li, Y., Cohn, T.: Massively multilingual transfer for ner. In: ACL
2019-57th Annual Meeting of the Association for Computational Linguistics,
Proceedings of the Conference. pp. 151–164. Association for Computational
Linguistics-ACL (2019)
68. Sadykov, T. S.: Проблемы моделирования тюркской морфологии. Frunze: Ilim
p. 3 (1987)
69. Sadykov, T. S.: Основы кыргызской фонологии и морфонологии. Ilim (1995)
70. Sadykov, T. S., Kochkonbaeva, B. O.: Модель морфологического анализа кыр-
гызского языка. In: Proceedings of the V International Conference on Computer
Processing of Turkic Languages Turklang. vol. 2, pp. 135–154 (2017)
71. Sadykov, T. S., Kochkonbaeva, B. O.: Об оптимизации алгоритма морфологи-
ческого анализа. In: Sbornik materialov Shestoy Mezhdunarodnoy konferentsii
po kompyuternoy obrabotke tyurkskikh yazykov «TurkLang-2018»(Tashkent,
Uzbekistan, 18–20 oktyabrya 2018 g.) (2018)
72. Sadykov, T. S., Sharshembayev, B. Sh.: «Манас» эпосунун улттук корпусун
түзүү жөнүндө. In: Kompyuternaya obrabotka tyurkskikh yazykov. Pervaya
mezh dunarodnaya konferentsiya: Trudy. pp. 148–154. Astana: ENU im. L.N. Gu-
mileva. (2013)
73. Sadykov, T. S., Sharshembayev, B. Sh., Kochkonbaeva, B. O.: Морфологические
разметки для национального корпуса. Vestnik Kyrgyzsko-Rossiyskogo Slavyan-
skogo universiteta 18(1), 91–94 (2018)
74. Sadykov, T. S., Turatali, T., Turdubaeva, A. B.: Морфологический анализ для
сбора текстовых данных в Национальном корпусе кыргызского языка. In:
TurkLang, Buxoro (2023)
75. Sadykov, T. S., Zhumalieva, G. E., Tumenbaeva, M. Zh., Sharshembayev, B. Sh.:
Kyrgyz tili: kompyuterdik lingvistikanyn negizderi (in Kyrgyz). Bishkek: Imak
ofset (2015)
76. Sakhovskiy, A., Miftahutdinov, Z., Tutubalina, E.: KFU NLP team at SMM4H
2021 tasks: Cross-lingual and cross-modal BERT-based models for adverse drug
effects. In: Proceedings of the Sixth Social Media Mining for Health (# SMM4H)
Workshop and Shared Task. pp. 39–43 (2021)
77. Samuel, D., Kutuzov, A., Øvrelid, L., Velldal, E.: Trained on 100 million words
and still in shape: Bert meets british national corpus. In: Findings of the Associ-
ation for Computational Linguistics: EACL 2023. pp. 1954–1974 (2023)
78. Satybaev, A. D., Kochkonbaeva, B. O.: Математическое моделирование и алго-
ритм морфологического анализа кыргызского языка. Byulleten nauki i prak-
tiki 5(3), 220–224 (2019)
79. Satybaev, A. D., Kochkonbaeva, B. O.: Тестирование программы морфологи-
ческого анализатора естественного языка. Byulleten nauki i praktiki 5(3), 215–
219 (2019)

--- Page 36 ---

36
A. Alekseev, T. Turatali
80. Scott, J.: Social Network Analysis. SAGE Publications Ltd; 4th edition (2017)
81. Senel, L., Ebing, B., Baghirova, K., Schütze, H., Glavaš, G.: Kardes-nlu: Transfer
to low-resource languages with the help of a high-resource Cousin — A Benchmark
and Evaluation for turkic languages. In: Proceedings of the 18th Conference of
the European Chapter of the Association for Computational Linguistics (Volume
1: Long Papers). pp. 1672–1688 (2024)
82. Sennrich, R., Haddow, B., Birch, A.: Improving neural machine translation mod-
els with monolingual data. In: Proceedings of the 54th Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers). Association
for Computational Linguistics (2016)
83. Sharipbai, A. A., Ergesh, B. Zh., Elibaeva, G. K., Zhetkenbai, L., Israilova,
N. A., Bakasova, P. S.: Сравнение онтологических моделей существитель-
ных казахского и кыргызского языков. In: Materialy Shestoy Mezhdunarodnoy
konferentsii po kompyuternoy obrabotke tyurkskikh yazykov «TurkLang-2018»
(Tashkent, Uzbekistan, 18–20 oktyabrya 2018 g.) (2018)
84. Shliazhko, O., Fenogenova, A., Tikhonova, M., Kozlova, A., Mikhailov, V., Shav-
rina, T.: mGpt: Few-shot learners Go Multilingual. Transactions of the Associa-
tion for Computational Linguistics 12, 58–79 (01 2024)
85. O’Sullivan, I.: The Companies That Have Already Replaced Workers with AI
in 2024. https://tech.co/news/companies-replace-workers-with-ai (August
2024), accessed: 2024-11-04
86. Swadesh, M.: Lexicostatistic dating of prehistoric ethnic contacts. Proceedings of
the American Philosophical Society 96(4), 452–463 (1952)
87. Swadesh, M.: Towards greater accuracy in lexicostatistic dating. International
Journal of American Linguistics 21(2), 121–137 (1955)
88. Tanzer, G., Suzgun, M., Visser, E., Jurafsky, D., Melas-Kyriazi, L.: A benchmark
for learning to translate a new language from one grammar book. In: The Twelfth
International Conference on Learning Representations (2024)
89. Taori, R., Gulrajani, I., Zhang, T., Dubois, Y., Li, X., Guestrin, C., Liang, P.,
Hashimoto, T. B.: Alpaca: A strong, replicable instruction-following model. Stan-
ford Center for Research on Foundation Models. https://crfm.stanford.edu/
2023/03/13/alpaca.html 3(6), 7 (2023)
90. Tohti, T., Musajan, W., Hamdulla, A.: Character code conversion and misspelled
word processing in uyghur, Kazak, Kyrgyz multilingual information retrieval sys-
tem. In: 2008 International Conference on Advanced Language Processing and
Web Information Technology. pp. 139–144. IEEE (2008)
91. Toleush, A., Israilova, N. A., Tukeyev, U.: Development of Morphological segmen-
tation for the Kyrgyz language on Complete set of Endings. In: Intelligent Infor-
mation and Database Systems: 13th Asian Conference, ACIIDS 2021, Phuket,
Thailand, April 7–10, 2021, Proceedings 13. pp. 327–339. Springer (2021)
92. Tukeyev, U.: A New Computational Model for Turkic Languages Morphology and
Processing. Journal of Problems in Computer Science and Information Technolo-
gies 1(1) (2023)
93. Tukeyev, U., Karibayeva, A., Zhumanov, Zh.: Morphological segmentation
method for turkic language neural machine translation. Cogent Engineering 7(1),
1856500 (2020)
94. Tyers, F. M.: Morphological Modelling. https://cl.indiana.edu/~ftyers/
courses/2022/Autumn/L-645/slides/morphology.pdf (2018), [Online; accessed
4-November-2024]
95. Veitsman, Y.: Recent Advancements and Challenges of turkic Central Asian lan-
guage processing (2024), https://arxiv.org/abs/2407.05006

--- Page 37 ---

KyrgyzNLP: Challenges, Progress, and Future
37
96. Visser, E.: A grammar of Kalamang. No. 4 in Comprehensive Grammar Library,
Language Science Press, Berlin (2022)
97. Vylomova, E., White, J., Salesky, E., Mielke, S. J., Wu, S., Ponti, E. M., Hall
Maudslay, R., Zmigrod, R., Valvoda, J., Toldova, S., Tyers, F. M., Klyachko,
E., Yegorov, I., Krizhanovsky, N., Czarnowska, P., Nikkarinen, I., Krizhanovsky,
A., Pimentel, T., Hennigen, L. T., Kirov, C., Nicolai, G., Williams, A., Anasta-
sopoulos, A., Cruz, H., Chodroff, E., Cotterell, R., Silfverberg, M., Hulden, M.:
SIGMORPHON 2020 Shared Task 0: Typologically Diverse Morphological Inflec-
tion. In: Proceedings of the 17th SIGMORPHON Workshop on Computational
Research in Phonetics, Phonology, and Morphology (2020)
98. Washington, J. N., Ipasov, M., Tyers, F. M.: A finite-state morphological trans-
ducer for Kyrgyz. In: LREC. pp. 934–940 (2012)
99. Washington, J. N., Salimzianov, I., Tyers, F. M., Gökırmak, M., Ivanova, S.,
Kuyrukcu, E.: Free/open-source technologies for turkic languages developed in
the Apertium project. In: Proceedings of the International Conference on Turkic
Language Processing (TurkLang 2019) (2019)
100. Washington, J. N., Salimzyanov, I., Tyers, F. M.: Finite-state morphological
transducers for three Kypchak languages. In: LREC. pp. 3378–3385 (2014)
101. Washington, J. N., Tyers, F. M., Kuyrukcu, E.: Multi-script morphological trans-
ducers and transcribers for seven turkic languages. In: Proceedings of the Work-
shop on Turkic and Languages in Contact with Turkic. vol. 5, pp. 173–185 (2020)
102. Wasserman, S, Faust, K: Social network analysis: Methods and applications. The
Press Syndicate of the University of Cambridge (1994)
103. Wikipedia
Contributors:
Kyrgyz_Tili
—
Kyrgyz
language
(in
Kyr-
gyz). https://ky.wikipedia.org/wiki/%D0%9A%D1%8B%D1%80%D0%B3%D1%8B%D0%
B7_%D1%82%D0%B8%D0%BB%D0%B8 (2023), [Online; accessed 4-November-2024]
104. Yiner, Z., Kurt, A., Kulamshaev, K., Zafer, H. R.: Kyrgyz orthography and mor-
photactics with implementation in nuvE. In: Proceedings of International Con-
ference on Engineering and Natural Sciences. pp. 1650–1658 (2016)
105. Zhang, K., Choi, Y., Song, Zh., He, T., Wang, W.Y., Li, L.: Hire a linguist!:
learning endangered languages in llms with in-context linguistic descriptions. In:
Findings of the Association for Computational Linguistics ACL 2024. pp. 15654–
15669 (2024)
106. Zhumalieva, G. E.: Лингвистический аспект формирования компьютерных
терминов в английском и кыргызском языках. Materialovedenie 27(3), 34–38
(2018)

```
