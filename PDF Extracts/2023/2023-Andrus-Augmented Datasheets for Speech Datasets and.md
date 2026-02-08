---
title: "2023-Andrus-Augmented Datasheets for Speech Datasets and - PDF Extract"
source_pdf: "2023-Andrus-Augmented Datasheets for Speech Datasets and.pdf"
pages: 24
extracted_at: "2026-01-29T13:51:08.505545"
---

# PDF Extract: 2023-Andrus-Augmented Datasheets for Speech Datasets and

**Source PDF:** 2023-Andrus-Augmented Datasheets for Speech Datasets and.pdf
**Total Pages:** 24

---

## Content

```
--- Page 1 ---

Augmented Datasheets for Speech Datasets and Ethical
Decision-Making
Orestis Papakyriakopoulos∗
orestis.papakyriakopoulos@sony.com
Sony AI
Zurich, Switzerland
Anna Seo Gyeong Choi∗
sc2359@cornell.edu
Cornell University
Ithaca, New York, USA
Jerone Andrews
jerone.andrews@sony.com
Sony AI
Tokyo, Japan
Rebecca Bourke
rebecca.bourke@sony.com
Sony AI
Tokyo, Japan
William Thong
william.thong@sony.com
Sony AI
Zurich, Switzerland
Dora Zhao
dora.zhao@sony.com
Sony AI
New York, New York, USA
Alice Xiang†
alice.xiang@sony.com
Sony AI
Seattle, Washington, USA
Allison Koenecke†
koenecke@cornell.edu
Cornell University
Ithaca, New York, USA
ABSTRACT
Speech datasets are crucial for training Speech Language Tech-
nologies (SLT); however, the lack of diversity of the underlying
training data can lead to serious limitations in building equitable
and robust SLT products, especially along dimensions of language,
accent, dialect, variety, and speech impairment—and the intersec-
tionality of speech features with socioeconomic and demographic
features. Furthermore, there is often a lack of oversight on the un-
derlying training data—commonly built on massive web-crawling
and/or publicly available speech—with regard to the ethics of such
data collection. To encourage standardized documentation of such
speech data components, we introduce an augmented datasheet for
speech datasets1, which can be used in addition to “Datasheets for
Datasets” [78]. We then exemplify the importance of each question
in our augmented datasheet based on in-depth literature reviews
of speech data used in domains such as machine learning, linguis-
tics, and health. Finally, we encourage practitioners—ranging from
dataset creators to researchers—to use our augmented datasheet to
better define the scope, properties, and limits of speech datasets,
while also encouraging consideration of data-subject protection and
user community empowerment. Ethical dataset creation is not a
one-size-fits-all process, but dataset creators can use our augmented
datasheet to reflexively consider the social context of related SLT
applications and data sources in order to foster more inclusive SLT
products downstream.
∗Both authors contributed equally.
†Co–principal investigator.
1Augmented datasheet templates and examples are available at https://github.com/
SonyResearch/project_ethics_augmented_datasheets_for_speech_datasets
Permission to make digital or hard copies of part or all of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for third-party components of this work must be honored.
For all other uses, contact the owner/author(s).
FAccT ’23, June 12–15, 2023, Chicago, IL, USA
© 2023 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-0192-4/23/06.
https://doi.org/10.1145/3593013.3594049
CCS CONCEPTS
• Human-centered computing →Collaborative and social
computing design and evaluation methods; • Applied com-
puting →Sound and music computing.
KEYWORDS
datasets, speech, datasheets, ethics, transparency
ACM Reference Format:
Orestis Papakyriakopoulos, Anna Seo Gyeong Choi, Jerone Andrews, Re-
becca Bourke, William Thong, Dora Zhao, Alice Xiang, and Allison Koe-
necke. 2023. Augmented Datasheets for Speech Datasets and Ethical Decision-
Making. In 2023 ACM Conference on Fairness, Accountability, and Trans-
parency (FAccT ’23), June 12–15, 2023, Chicago, IL, USA. ACM, New York,
NY, USA, 24 pages. https://doi.org/10.1145/3593013.3594049
1
INTRODUCTION
The ubiquity of Speech Language Technologies (SLT) in every-
day life raises serious questions about the disparate harms these
technologies can have on different populations. Use cases such as
automated speech recognition (ASR), speaker recognition, speech
synthesis, speech quality assessment, speech enhancement and
denoising are now integrated in smartphones, cameras and virtual-
assistants [260], and applied in domains such as customer ser-
vice [16], finance [85, 178, 199], navigation [63, 273, 279], health [171],
education [191, 195, 196, 202, 276], and law [107]. The downstream
impacts of biased SLT can be severe. Individuals who do not speak
“standard ” varieties of a language [185] may be disproportion-
ately unlikely to be hired given speech-based hiring screening soft-
ware [285]. Doctors increasingly use SLT to efficiently take patient
notes, which could result in serious health harms if transcribed
incorrectly [171]. Moreover, SLT technology has been developed
to surveil the phone calls of incarcerated individuals; the result-
ing transcriptions—likely disproportionately inaccurate for Black
individuals [128]—can result in differential treatment [231].
Speech technologies—as with any machine learning applications—
are prone to bias; these biases often stem from nonrepresentative
881

--- Page 2 ---

FAccT ’23, June 12–15, 2023, Chicago, IL, USA
Trovato et al.
or inaccurate training data [35, 124, 128, 129, 186]. There is a mis-
match between the “world as it is,” and the “world according to data”
[186]; there are further mismatches between the data used to train a
machine learning model, and the data testing the model in practice
[129]. Generating robust SLT is an especially complex task given
the diversity of human speech, comprising of different languages,
accents, dialects, varieties, and speech impediments. An additional
layer of complexity arises from the collection of speech data used
to train SLT applications: there is high variability across necessary
tasks, from noise in a recording environment to transcription of
language and acoustic features. Finally, as with any dataset, it is
imperative to center ethical dataset creation and usage—regarding
the privacy, respect, and protection of data subjects, interviewers,
and transcription annotators.
Given the complexity of creating, documenting, and using speech
datasets, we propose “augmented datasheets for speech datasets,”
inspired by the original “datasheets for datasets” [78]. Datasheet
usage can make dataset creation more transparent and accessible,
while also assisting dataset users—such as SLT practitioners and
researchers—to select appropriate datasets for their objectives. Our
specific contributions are as follows: first, we generate a set of
speech data-specific questions for practitioners to answer when
creating or using speech data (Section 3, bolded). Second, we sub-
stantiate why each question is important via examples of related
papers and datasets (Section 3, plain text). Third, we make a call to
action—for all practitioners using speech data, whether dataset cre-
ators or users—to use speech-specific datasheets in a collaborative
effort to ensure transparency regarding speech data ethics and diver-
sity (Section 4). Fourth, we provide speech datasheet templates—in
both .tex and .docx—both empty and with worked examples, for
practitioner use (available on GitHub, Footnote 1).
The questions comprising our “augmented datasheet” for speech
datasets are formulated by the authors’ positionalities as SLT prac-
titioners, linguists, machine learning researchers, algorithmic fair-
ness researchers, and lawyers; we also draw upon an in-depth
literature review revealing data-centric best practices and issues in
SLT (Appendix B). We believe our augmented datasheet template
can guide researches in ethical speech dataset design and usage,
and have released our template for immediate public use. However,
we emphasize that our datasheet template should not replace the
dire need for in-depth conversations on speech dataset ethics and
diversity among datasheet users.
1.1
Related Work & Existing Datasheets
Our study builds on prior work scrutinizing the design [11, 103, 138,
201, 259], documentation [36, 54, 78, 210, 222, 239], and analytical
evaluation [68, 166, 181, 227] of datasets. For example, Hanley et
al. [95] identified four aspects of human-centric dataset develop-
ment that result in ethical concern, namely purpose (e.g., moral
legitimacy), creation (e.g., data sourcing and cleaning), composition
(e.g., data instances, metadata), and distribution (e.g., terms of use).
Similarly, Mahajan et al. [166] conducted a systematic review of
over 300 research papers related to spoken or written multi-party
dialogue, highlighting the need for diverse representation of human
participants, privacy protection of sensitive information, and pre-
registration of proposed data collection processes to avoid purpose
creep. A core cause of ethical concerns has been identified: opaque,
sparse, and non-standardized documentation practices [68].
Following common practices in the electronics industry, Gebru
et al. [78] proposed datasheets to document the key stages of a
dataset’s lifecycle. Such documentation can help to address the
reproducibility crisis by making “research validity and integrity”
[68] more transparent. Various similar and complementary pro-
posals have since followed, including nutrition labels [99], data
statements [17], data cards [210], data briefs [68], model info sheets
[117], and causal datasheets [36]. A common thread is the desire
to standardize practices for qualitatively summarizing datasets, in-
creasing transparency and addressing bias by exposing key details
to stakeholders such as a dataset’s motivation, provenance, com-
position, and maintenance. As Datasheets for Datasets [78] only
represents an all-purpose starting point, more specialized documen-
tation has been proposed, for example focusing on art [239] and
health datasets [222].
As the creation of dataset documentation is primarily a reflective
process (i.e., the data already exists), others have instead focused on
the actual process of collecting data. For example, Hutiri et al. [103]
present guidelines for designing speaker verification evaluation
datasets, addressing limitations in previous datasets, i.e., evalua-
tion bias, unrepresentativeness, and unaccounted-for sources of
error. LeClair and McMillan [138] provide a set of recommenda-
tions alongside a new dataset, motivated by conflicting results in
the task of source code summarization, which was due to a lack
of community consensus on how datasets should be designed and
collected. Similarly, in the library domain, despite the major role
that library-linked data plays in retrieval, there is a lack of agreed
upon methodological guidelines for publishing library linked data,
which has now been addressed by Vilazzon et al. [259].
Focusing on SLT, in addition to the guidelines of speaker veri-
fication evaluation datasets by Hutiri [103] and the survey of Ma-
hajan et al. [166], Feng et al. [71] provide a review of issues re-
lated to speech-centric trustworthy machine learning, including
discussing the importance of fairness and privacy for developing
speech datasets. Nonetheless, no prior work focuses on the deci-
sions speech dataset creators should make when facing speech-
specific issues and appropriate documentation for such decisions, a
gap that our study aims to bridge.
2
SPEECH PRELIMINARIES
2.1
Speech Definitions
A fundamental characteristic of language is that a single meaning
can be expressed in multiple different ways; some go so far as
to argue that language uniformity is a pure myth [67]. As such,
linguistic variation is detectable in all communities, even if only a
single language is spoken. This variation, once noted as “orderly
hierarchy” [256], is what the members of the speech community
use to construct both their personal and social identities, and is
therefore crucial to understanding how to rightfully represent the
community in an SLT system.
While it is common for speech datasets to specify which language
or languages are spoken, there are more granular linguistic catego-
rizations that can, and often should, be used to better foster speech
diversity. Within a language, it is common to define a certain way
882

--- Page 3 ---

Augmented Datasheets for Speech Datasets and Ethical Decision-Making
FAccT ’23, June 12–15, 2023, Chicago, IL, USA
of speaking as “standard,” which problematically erases the many
other valid ways of speaking that language [70, 192]. Specifically,
populations may speak with different accents, dialects, or varieties
of a single language. Furthermore, individuals may speak in atypical
manners, such as with speech impairments, which can manifest in
different speaking styles [47, 70, 80, 92, 111, 253]. We refer to speech
types along these dimensions as “linguistic subpopulations” and
provide formal definitions for each, though we note that ongoing
debate on these topics continues in many subdomains.
An accent is defined by Edwards [64] as a unique mode of sound
production affected by the speaker’s specific linguistic characteristics—
especially phonology and prosody. Accent is commonly thought to
be a phonological variant of a language, and it is likely that certain
speech features, such as the speakers’ first language’s phonology
system, could have carried on to create accented speech [152]. Exam-
ples of accents include non-native speech such as Chinese-accented
Korean or French-accented Spanish, or regional speech such as
Texan-accented English.
A dialect is generally considered to be more broad, and occurs
when a subgroup of a language’s speakers is isolated from the rest
of the population [64]. This would not only include phonology and
prosody (as in the concept of accent), but also syntax, semantics,
morphology, and pragmatics. A looser definition of dialect per Paul
[205] is simply a version of a language that is similar to the form
spoken by the majority group but different in some aspects. Our
earlier example of Texan-accented English would hence classify as
a dialect as well, as part of a larger Southern dialect of American
English. Additional examples of regional dialects include British
English or Australian English; there are also social dialects, such as
African American Vernacular English (AAVE).
Language variety is a more neutral term that is used to refer
to any type of language, encompassing all of dialect, accent, and
the specific language in general [254]. Variety can include registers,
styles, and idiolects, in addition to accents or dialects mentioned
above. For example, Texan-accented English or African American
Vernacular English would also be considered varieties of English.
Additional examples of varieties that are neither dialects nor accents
include honorific speech, child-directed speech, or code-switching.
Code switching refers to a situation in which the speaker alter-
nates between two or more linguistic varieties [74], whether in-
tentionally or unintentionally. Code switching can happen within
a clause (intra-sentential, e.g. “quiero ir al [es] mall next Tuesday
[en]”) or outside a clause, e.g. “es difícil encontrar trabajo estes
dias, [es] you know? [en]”; it can also occur at a clause-level (inter-
sentential, e.g. using an English phrase when speaking Spanish),
or even within a single word, at a morphological level (intra-word
switching, e.g. using a single English word in a sentence when
speaking Spanish).
Speech impairments refer to communication disorders of peo-
ple with difficulties in formulating normal speech sounds neces-
sary for communicating with others. These are often caused by
disorders such as aphasia, stuttering, and lisping [229]. ASR mod-
els have been deployed for the detection of pathological or psy-
chological issues including dysarthria [44, 184, 235], Alzheimer’s
[148], obstructive sleep apnoia [23], and other health concerns
[39, 47, 50, 92, 135, 142, 143, 157, 244, 283].
A speech corpus could contain speech uttered by any number of
linguistic subpopulations. However, this speech can present itself
very differently depending on the kind of speech material used for
corpus collection. The two main types of speech material are read
speech and spontaneous speech. Read speech provides partici-
pants with a certain prompt to read aloud. When reading a text,
people have a tendency to read in a more tense and formal manner,
controlling for their articulation, which makes it differ from their
original way of speaking [175]. In contrast, spontaneous speech
is when participants are allowed to speak freely, such as in a mono-
logue or a dialogue, where the topic of the talk may or may not be
predetermined.
2.2
Diversity of speech data
Diversity in speech itself is multifaceted: within a dataset, it can
refer to (a) the overall distribution of languages, (b) the distribution
of a single language’s varieties, and (c) the distribution of speaker
socioeconomic and demographic factors.
In the first case, diversity may be lacking even if a high count of
languages are present in the data. Indeed, in the broader field of Nat-
ural Language Processing, there exists the concept of “low-resource
languages” that are systematically under-represented [165]. For
example, in one of the most recent and advanced ASR models [213],
some languages take up an exponentially smaller share of the un-
derlying training data.
In the second case, diversity may still be lacking even within
the realm of high-resource languages, if only the majority dialect
or accent is included in the data—e.g., only including speakers of
“Standard English” and excluding speakers of “African American
Vernacular English” [128].
This is directly related to the third case, wherein a single lan-
guage can be divided into numerous diversities (usually represented
as dialects or accents), often interacting with socioeconomic and
demographic factors such as nationality, gender, age, education,
and income level—arising in speech data not just through the hu-
man speech uttered, but also through background noises being
recorded [38, 40]. Multilingual or code-switching speech is also
an important component of multi-ethnic communities, and groups
of people may portray distinct speech styles associated with var-
ious factors like profession. Furthermore, health status can play
a role, such as for people with different impairments that take a
toll on speech abilities (e.g., cerebral palsy [192] or Alzheimer’s
[148]). Finally, demographic diversity in speech datasets is impor-
tant to consider. While many datasets contain gender labels [26, 76],
very few include non-binary individuals (only 3% in the sample of
datasets we reviewed, e.g., [12, 82]). The same applies for speech
data on different speaker age groups [80, 278]: datasets may ag-
gregate age into coarse groups, but the result is that certain age
groups are still systematically under-represented, such as young
children [275].
Great strides have been made in each of the three cases described
above. For example, there are specific datasets on spontaneous and
colloquial speech for low-resource language [188], accented speech
[232], bilingual individuals [113], and speech impaired individuals
[164]. That said, numerous studies have found the data lacking
for all three cases: most text-to-speech services can only support
883

--- Page 4 ---

FAccT ’23, June 12–15, 2023, Chicago, IL, USA
Trovato et al.
a dozen languages out of the over 7,000 languages in the world
[247]; and, data is still sparse for dialects [61, 172] and individuals
with disabilities [39]. Beyond the three facets of speech diversity
described above, there are other dimensions to consider: there are
also often limited data on domain-specific vocabulary [81], speaker
geography [87], and, relatedly, political alignment [60].
Machine learning models trained on non-inclusive datasets fur-
ther perpetuate the lack of representation, especially as in-the-
wild performance is particularly dependent on the level of acoustic
match with the training data [119, 230]. Prior studies have found
biases—based on lower ASR model performance—for speech sub-
groups across speech impairment [89, 156, 170], and intersectional
speech subgroups: of gender and race [128], gender and geography
[248], and gender and accented chatter noise [261].
We suggest that practitioners be aware of the many facets of
speech diversity, and be able to support their decisions to include or
exclude different linguistic subpopulations in the collection process.
In this way, we bring awareness to the lack of content validity [108]
in datasets that can result in representational harm [24].
3
AUGMENTED DATASHEETS FOR SPEECH
DATASETS
In this section, we showcase the questions included in the Aug-
mented Datasheets for Speech Datasets. We follow the same section
ordering as the original Datasheets for Datasets paper [78]. We refer
to “linguistic subpopulations” as subpopulations speaking any of
different: languages, accents, dialects, varieties, and/or impaired or
atypical speech. For each question, we provide in-depth examples
about how these questions can support dataset creators in ethical
decision-making and enhancement of dataset transparency.
These examples are the result of a literature review we performed
on a set of 178 speech studies related to fairness and diversity, as
well as 220 speech datasets.2 For the 178 studies, we tabulated
the authors’ ethical considerations related to diversity, inclusion,
privacy, user empowerment, crowdworker protection, data qual-
ity assessment, explainability, and the context of application of a
speech technology. For the 220 speech datasets, we investigated
their diversity, inclusion, and privacy considerations, and identified
limitations regarding ethical dataset development. Our literature
review allowed us to map extracted information from datasets and
research studies to the corresponding categories of our augmented
speech datasheets, and develop representative datasheet questions
for each category.
While the “Augmented Datasheets for Speech Datasets” ques-
tions in this Section are each followed by additional context based
on our literature review, we additionally created .tex and .docx tem-
plates for use by dataset creators and users. We include both blank
templates to be filled out, as well as worked datasheet examples
on common speech datasets, at https://github.com/SonyResearch/
project_ethics_augmented_datasheets_for_speech_datasets.
2The studies were extracted from ArXiv, The ACM Digital Library, Google Scholar,
the ACL Anthology, IEEE Xplore, or were published in the following venues: IN-
TERSPEECH, ICASSP, NeurIPS, and ICML. The speech datasets were extracted from
on paperswithcode.com [243], huggingface.co [270], and openslr.org [198]. See more
details on the literature review in Appendix B.
3.1
Motivation
The reasons motivating the creation of a dataset and their conse-
quences should be well-documented. Depending on the task, or
the existing gap the dataset seeks to fill, the dataset creators’ mo-
tivations may influence many parameters. These may include the
composition, naming, licensing terms or the data collection process.
Below, we showcase the importance of three augmented speech
datasheet questions regarding motivations for dataset creation.
3.1.1
What is the speech dataset name, and does the name accu-
rately describe the contents of the dataset? It is important to choose
a descriptive and informative dataset name, ensuring it accurately
describes its content. For example, it is ideal to include the speech
technology a dataset is developed for (e.g., IISc-MILE Tamil ASR
Corpus [207]—where ASR refers to Automated Speech Recognition;
LibriTTS corpus [281]—where TTS refers to text-to-speech), men-
tion the exact demographic information it concerns (e.g., Samrómur
Children 21.09 [177], MAGICDATA Mandarin Chinese Conversa-
tional Speech Corpus [274], Korean Read Speech Corpus [104],
Parkinson Speech Dataset with Multiple Types of Sound Record-
ings Data Set [224]), mention specific linguistic features of note (e.g.,
A Mandarin-English Code-Switching Corpus [149], Multi-dialect
Arabic Speech Parallel Corpora [10], Korean English Learners’ Spo-
ken Corpus [115]), or provide information about the related speech
domain of the recordings (e.g., Audio-Visual Speech Corpus in a
Car Environment [139]—recordings from noisy automobile environ-
ment; Deeply BibleTTS [179]—recordings of Bible readings). Given
that it is a standard technique to combine speech resources from
different domains, languages, varieties, and styles (e.g., [213]), an
appropriate name selection and detailed description can assist the
efficient retrieval of datasets that can lead to more inclusive models.
3.1.2
Can the dataset be used to draw conclusions on read speech,
spontaneous speech, or both? A dataset focusing on speech syn-
thesis for audiobooks would ideally contain read speech (e.g., [12,
200, 221]), while a dataset used for in-the-wild speech recognition
would contain spontaneous speech (e.g., [13, 208]). In the case of
the creation of a general purpose speech model, it would be ideal
to use a dataset that contains both read and spontaneous speech
(e.g., [45, 197]). Especially since the robustness of speech technolo-
gies such as ASR are largely dependent on their training data, it is
important to guide researchers in using appropriate speech data
types.
3.1.3
Describe the process used to determine which linguistic sub-
populations are the focus of the dataset. We ask for disclosure on
the process behind linguistic subpopulation choice: e.g., a dataset
aiming to achieve language preservation should contain resources
that focus on under-resourced languages [132], and the selection
of content will ideally correspond to the vocabulary and culture
of the corresponding community. In commercial speech product
audits, it may be important to collect observations spanning spe-
cific parameters (e.g., accent, gender, race, user group) reflecting
the diversity of the user population (e.g., [72, 153, 180]).
3.2
Composition
We propose necessary questions that scrutinize the sufficiency and
coverage of a dataset in terms of quantity (questions 3.2.1—3.2.2),
884

--- Page 5 ---

Augmented Datasheets for Speech Datasets and Ethical Decision-Making
FAccT ’23, June 12–15, 2023, Chicago, IL, USA
quality (questions 3.2.3—3.2.7), and content of speech (questions
3.2.8—3.2.10).
3.2.1
How many hours of speech were collected in total (of each
type, if appropriate), including speech that is not in the dataset? If
there was a difference between collected and included speech, why?
E.g., if the speech data are from an interview and the dataset contains
only the interviewee’s responses, how many hours of speech were
collected in interviews from both interviewer and interviewee? This
quantification can help ensure the robustness of the data collection
process by scrutinizing choices of the dataset creators. It is impor-
tant to understand why specific segments of the data are retracted,
and how they handle data-related obstacles. For example, in MLS
[209], the authors had to restrict the final dataset coverage given
technical inabilities in retrieving book transcriptions. The VOICES
dataset [217] was created by using a gender-balanced subset of
another dataset, LibriSpeech [200]. Similarly, the creators of Parlia-
mentParla [133] chose specific segments to optimize for vocabulary
diversity. Such choices need to be carried out with caution towards
robust & inclusive dataset design and documentation.
For datasets where interviews were conducted, the creators may
need to decide whether or not to include the interviewers’ speech
in the raw dataset, since it will greatly affect the dataset size and
properties (e.g., the interviewer’s questions may be considered
read speech and not spontaneous speech). Some datasets decide
to exclude the interviewer speech through means such as silence
detection, using the fact the interviewers are usually recorded at
a much lower frequency [284]. Other datasets do not transcribe
interviewer speech [208], or do not record the interviewer at all
[160]. On the other hand, some datasets choose to retain their
interviewer speech [164, 266].
3.2.2
How many hours of speech and number of speakers & words
are in the dataset (by each type, if appropriate)? We suggest de-
scribing both the number of hours included in the dataset for each
combination of type (e.g., by speakers’ intersectional identities)
as well as the corresponding counts of speaker and vocabulary
diversity.
Quantifying dataset size in hours can provide guidelines for
model training using the data at different sizes. For example, Mozilla
suggests that 10,000 validated hours of speech per language is the
ideal number to build an ASR system in production [12], while for
pre-trained foundational models, Zelasco et al. [280] and Microsft
Azure [183] suggest that fewer than 20 hours of target language fine-
tuning can significantly reduce ASR error rates. Some datasets are
small enough such that they can only be used for model evaluation
and not training (e.g., VIVOS [158]).
It is similarly important to tabulate the numbers of speakers
since speaker variety can be a decisive factor for the usage of a
dataset. For example, in the field of speech synthesis—more so than
the speech recognition field—an important parameter is whether
the dataset is collected from a single speaker [204] or multiple
speakers. Hence, it is crucial to pinpoint the number of speakers as
well as the variability between the speakers.
Finally, it is useful to quantify the number of total and unique
words being uttered. Each language has a different size of unique
words, which results in different ratios of Out-Of-Vocabulary (OOV)
words for the same dataset size when performing an unstratified
train/test set split [56]. Lexicon vastness and its corresponding pho-
netic inventory plays a pivotal role in the performance of the ASR
model, as OOV words often cause misrecognition of neighboring
words [3, 271]. Furthermore, words that do not appear as frequently
as others are commonly considered outliers by the models, resulting
in disparate treatment of scarce speech that many times is uttered
by minority linguistic subpopulations.
3.2.3
Are there standardized definitions of linguistic subpopula-
tions that are used to categorize the speech data? How are these
linguistic subpopulations identified in the dataset and described in
the metadata? While it is important for datasets to be robust across
different language varieties, oftentimes the documentation is lack-
ing in formal definitions of the linguistic subpopulations speak-
ing in the dataset. The creators should not simply assume that a
certain definition is broadly agreed upon by the linguistic commu-
nity; rather, it is helpful to provide detailed definitions of such sub-
populations. This is especially true for datasets created for dialect
identification or classification, or non-native speech assessment
[7, 20, 28, 60, 250, 282].
The linguistic groups to be identified and described should con-
tain recording-specific sub-groups that emerge as part of the dataset.
Linguistic groups often include categories that are fluid and non-
deterministic (e.g., age, gender, social background, accent, dialect).
For such categories, dataset creators should make aggregation
choices that speak to the diversity of the data, while respecting the
privacy of the speakers’ identities and histories. Dataset creators
should explicitly describe how they identify and define such sub-
populations in the dataset, while considering the implications of
and absence of such categorizations.
3.2.4
For any linguistic subpopulations identified in the dataset,
please provide a description of their respective distributions within the
dataset. It is important to understand the representational makeup
of speakers and utterances in a speech dataset, in particular among
linguistic subpopulations, and among socioeconomic and demo-
graphic groups. Different levels of representation in speech data
used to train models can have different downstream effects on
model performance among diverse test sets. Augmenting data to
make the original training dataset more balanced in terms of gen-
der has been found to yield improvement in model performance
[48], and there have been attempts to create datasets specifically
tackling gender balance in the training data for fields with known
imbalances [264]. In our review, we found that fewer than 10% of
the datasets were balanced on demographic properties of gender
and age. That said, we note that ensuring demographic parity in all
datasets would disproportionately penalize researchers for generat-
ing important training data focused on underrepresented minority
language types that are time- and labor-intensive to collect.
3.2.5
How much of the speech data have corresponding transcrip-
tions in the dataset? It is useful to first understand whether speech
transcriptions are necessary for the SLT tasks at hand, and if so,
to what extent they are provided. For example, a model to sim-
ply detect background noise would not require transcriptions—it
would only need labeling of spoken noise. Meanwhile, training
an ASR model necessitates having the ground-truth transcription
provided with the speech dataset (due to the underlying language
885

--- Page 6 ---

FAccT ’23, June 12–15, 2023, Chicago, IL, USA
Trovato et al.
model using textual data), and will yield better performance with
high quality transcriptions [34]. However, the cost of generating a
high volume of transcriptions for large speech datasets is extremely
demanding, so current ML methods such as semi-supervised learn-
ing or weakly-supervised learning have been developed to allow
for training on only a small initial transcribed dataset, and then
self-learning to make hypotheses on the remaining larger portion
of the unlabeled dataset [145, 151, 213]. Furthermore, dataset cre-
ators may use existing ASR models to generate transcriptions of
speech recordings—significantly less expensive than hiring human
transcribers—which can inject pre-existing biases of the ASR model
into a new speech dataset ([136, 286]). Another technology used is
data augmentation, where an in-domain, fully-transcribed dataset
is adapted—mainly through acoustic modification—to be used as
training data to predict the ground truth transcriptions of a new
dataset [116, 134]. It is important to enumerate transcriptions and
state their limitations in a dataset so practitioners can consider
whether these enhancement methodologies can suffice for their
SLT.
3.2.6
Does the dataset contain non-speech mediums (e.g. images or
video)? Oftentimes, speech data are extracted from videos crawled
from public domains [30, 90, 246]. Furthermore, there are specific
use cases requiring multimedia datasets, such as discourse analysis
of speech with a high level of difficulty in voice intelligibility [164].
Relatedly, combining audio and visual resources has been found to
improve ASR performance in low speech-to-noise settings [139].
Finally, there are use cases where additional data formats can benefit
ML prediction tasks. For example, the Turkish Audio-Visual Bipolar
Disorder Corpus [49] uses audio-visual data because the creators’
goal is to recognize affective states of patients for bipolar disease
classification by combining both audio and appearance features.
As such, it is useful to consider whether additional media formats
should be released with the speech data.
3.2.7
Do speakers code switch or speak multiple languages, and if so,
how is this identified in the data? One of the main sources of errors
in ASR is words being uttered in different languages [269]. Hence,
it is important to document when code switching happens, ranging
from single words, to sentences or full segments of speech record-
ings [190]. Especially since data-subjects may not be aware that
they are code-switching, dataset curators should carefully review
speech and include appropriate label tags to indicate a change of lin-
guistic feature. Code-switching may be more difficult to transcribe,
since languages used to code-switch may use different alphabeti-
cal systems, and each language could require separate annotation
systems (e.g., TALCS—using Mandarin and English [144]). Some
code-switching corpora include a separate layer of transcription to
mark where the code-switching happens, either inter-sentential or
intra-sentential (e.g., TuGeBic [43]).
3.2.8
Does the speech dataset focus on a specific topic or set of top-
ics? It is important to carefully choose and document the content
of speech included in the dataset. For example, speech focusing
on finance [197] or politics [126] may not be suitable for training
general-purpose synthesis or recognition systems. In addition, spe-
cific applications for speech systems such as air traffic control [273]
or the medical domain [125] contain disproportionate amounts of
domain-specific vocabulary and jargon, which may be out of scope
in pre-trained general purpose models [81]. Therefore, it is cru-
cial for dataset creators to report the content scope of the speech
recordings.
3.2.9
Does the dataset include sensitive content that can induce
different emotions (e.g., anger, sadness) that can cause the speakers to
produce unusual pitch or tone deviating from plain speech? Datasets
that contain only emotion-neutral speech [233] might be less useful
for broadly deployed ASR systems, or for speech synthesis models
for music or other creative tasks. In addition, emotional language
diversifies prosodic [73] and phonetic elements of language [6],
resulting in lower performance in models [111]. Thus, it is helpful
to include—and perhaps label—emotional speech in datasets.
3.2.10
Does the dataset contain content that complies to the users’
needs, or does it result in symbolic violence (the imposition of reli-
gious values, political values, cultural values, etc.)? The problematic
composition of a dataset can lead to the creation or perpetuation of
power asymmetries in the society, a term that sociologist Bourdieu
terms as symbolic violence—defined as a type of non-physical vio-
lence manifested in the power differential between social groups
[31]. Unless the dataset is specifically aiming to collect a certain
portrayal of reactions to power dynamics, it is the creator’s re-
sponsibility to attempt to discard content deemed as promoting
symbolic violence [162]. For example, the usage of the Bible or
highly value-laden text (e.g., novels with colonialist themes [21])
for creating speech recordings should be avoided among some com-
munities, due to the differences in cultural & religious values and
histories—being forced to reach such texts could exacerbate the
powerlessness felt by those communities [179, 251]. Furthermore,
the mere presence of certain kinds of speech in a released dataset
could be enough to perpetuate symbolic violence towards dataset
users—regardless of whether or not the dataset creators condone
such speech.
It is therefore important to document whether such limitations
and issues exist in a dataset and also strive to focus on dataset con-
tent that complies with users’ needs and respects data subjects. The
needs of data subjects can be taken into consideration by focusing
on recordings of vocabularies, topics, and speech segments that
best represent subjects’ every day lives, values, social and personal
behaviors.
3.3
Collection Process
Speech data collection encompasses processes that could involve
the scraping of digital or analog content, and/or the cooperation
with data-subjects who will provide their voice/recordings.
3.3.1
What mechanisms or procedures were used to collect the
speech data, e.g.: is the data a new recording of read speech, or an inter-
view? Or is it downloaded speech data from public speeches, lectures,
YouTube videos or movies, etc.? Dataset creators should strategically
and carefully decide on the mechanisms they use to collect speech.
For example, when scraping online content [97, 98, 106, 122, 193],
they should ensure that they have permissions to acquire content,
and disclose the appropriate permissions [71, 155, 238]. Further-
more, they should describe whether the speech is a direct recording,
acquired from a pre-existing speech source, or if they interviewed
886

--- Page 7 ---

Augmented Datasheets for Speech Datasets and Ethical Decision-Making
FAccT ’23, June 12–15, 2023, Chicago, IL, USA
data-subjects specifically to create this dataset. Note that additional
questions on interviewee recruitment and consent are covered in
the original “Datasheets for Datasets” paper [78].
3.3.2
Were all the data collected using the same technical method-
ology or setting, including the recording environment (e.g., lab, mi-
crophone) and recording information (e.g., sampling rate, number of
channels)? The use of different speech collection media can have
a significant impact on the quality of collected speech. Relevant
properties include the distance of individuals from the microphone,
the type of microphone [105], single or multi-channel data collec-
tion [154, 189, 278], and recording frequency. For example, speech
recordings of higher frequency than 20 khz [4, 241] might be pre-
ferred over lower ones [197, 238] in speech synthesis, since they
are of higher quality and improve user experience. Similarly, data
collection using only specific types of microphones [241] could re-
duce hardware-induced noise in recordings that used random or not
model-specific recording media [62, 96, 109, 120, 147, 182, 211, 212].
Additionally, in cases of collection crowdsourcing, dataset creators
should reflect on what technical requirements and processes they
set for collecting speech, since individuals might not have uniform
internet access [2], or be familiar with complicated user interfaces
[132, 137].
3.3.3
Is there presence of background noise? On spontaneous speech
datasets, variable background environments can result in differ-
ential performance of speech models [45, 87]. ASR model perfor-
mance declines with a smaller the signal-to-noise ratio [172, 220].
Generally, depending use case (e.g., speech synthesis), or dataset
motivation (e.g., language preservation), researchers might pre-
fer recordings in quiet environments [94, 234, 241], or enhancing
recordings with artificial noise [53, 258]. However, using datasets
that are highly varied in noise levels—from diverse environmental
conditions—can result in more robust models [12, 15, 22, 81, 87, 111,
121, 216].
Noise-related considerations are not merely for the sake of build-
ing robust ASR models (on its own, a long-standing task in the field
[69, 161, 219]); noise levels also have direct socioeconomic implica-
tions, as they are estimated to be higher for population groups with
higher proportions of lower-socioeconomic status residents, with
factors such as race, poverty, unemployment, and education level
having impact [38, 40]. Casey et al. [40] even considers linguistic
isolation as one of the main factors correlating with higher levels of
noise, where “linguistic isolation” is defined as a household where
no one over the age of 14 speaks English “very well.” In order to fully
consider the diversity of socioeconomic, ethnic, or racial make-up
in speech data, it is critical to ensure that data pre-processing steps
removing background noise do so in a principled way that does not
erase representation across socioeconomic levels.
3.3.4
For interviewer/interviewee speech data: during the interview
process, did interviewers consistently ask questions that are “fair
and neutral”? Qualitative data collection—and in particular, via
interviews—is a common method to collect speech data, especially
for spontaneous speech. In the survey bias literature [268], value
neutrality is defined as being objective to personal values when
conducting sociological studies and staying clear of engaging per-
sonal values and opinions [263]. A critical component of conducting
interviews is maintaining this neutrality [84, 265]. Interviews used
for such data collection are usually open-ended, meaning they can-
not be answered with a simple “yes” or “no” response, and instead
prompt a longer conversation, making the interview become semi-
structured. Even though the semi-structured nature of the interview
makes it difficult to anticipate the response and what question to
move on to, it is important for the interviewers to remain neutral
at all times and withhold judgment [83].
The use of “fair and neutral” questions allows for open, hon-
est, and respectful communication without judgment between the
interviewer and interviewee, who may have different viewpoints
and lived experiences. Fair questions consider the context, circum-
stance, and perspective of the respondent. This necessitates careful
consideration with regard to the impact a question can have on a
respondent. Fair questions should be both respectful and consider-
ate, reflecting that each person has their own set of opinions and
experiences. In addition, the interview should make interviewees
feel comfortable, both in terms of interview content and setting.
For example, Pitt et al. [208] balanced the interviewers and in-
terviewees gender combinations, to control for social dynamics
developed in inter- and intragender discussions. In a similar fash-
ion, Kendall and Farrington [123]—for data collection of African
American English speech among interviewees—also ensured that
the interviewers were speakers of African American English to
minimize code-switching between the two parties.
Neutral questions are neither biased or leading, thus resulting
in more objective and unbiased responses. Such questions are free
from assumptions and suggestive language that might conceivably
prejudice a respondent on the basis of the interviewer’s personal
position. Neutrality can be supported by using open-ended ques-
tions or diverse topics of discussion [58], in order to freely drift
language usage according to their habitual frequency [140] and
capture phenomena such as diction [127].
We include two examples of fair and neutral questions. Firstly,
from Holstein et al. [100] to machine learning practitioners: “Can
you recall times you or your team have discovered fairness issues
in your products?” The question is open-ended, respectful of the
practitioners’ product knowledge, expertise, and experience, and
permits response autonomy (respondents are able to exert control
over what they share and how). Secondly, from Kapoor et al. [118]
to labor organizers in the US technology industry: “How do you
increase membership in your collective? Are you involved in reach-
ing out to other employees who are not yet a part of [collective’s
name]?” The question is open-ended, providing respondents an
opportunity to share their strategies without any assumptions or
biases with respect to how this should be done. Moreover, the ques-
tion is respectful and non-judgmental—it does not assume that the
respondent is, or should be, involved in outreach activities.
3.3.5
Have data subjects consented to the disclosure of the metadata
in the dataset? Also, does the metadata include sensitive personal in-
formation such as disability status? Basic metadata release is critical
for dataset usage, but depending on the dataset’s purpose, addi-
tional metadata may contain information related to sensitive or
biometric properties of the person—it is important to ensure the
data subject agrees to both the validity and release of such metadata.
For example, metrics could include health and speech impairment
887

--- Page 8 ---

FAccT ’23, June 12–15, 2023, Chicago, IL, USA
Trovato et al.
status that could negatively impact the individual if such informa-
tion were made public [6, 224, 277]. A common machine learning
task is one of score prediction—e.g., on the Mini-Mental State Exam-
ination (MMSE)—using impaired speech corpora. Datasets collected
with such a task in mind would include not just speech data, but
also metadata on the participants’ MMSE scores [159]. Additional
metadata can include detailed information about the etiology, the
onset/duration time of the impairment, additional disorders, and
even surgical information [141, 266]—all of which have the poten-
tial to do serious harm to a data subject if stored improperly or
released without consent. Finally, it is important to ensure that
an individual’s metadata is agreed upon—for example, it is helpful
to have data subjects self-report demographic information (e.g.,
[12, 93, 255]), since it may be harmful for individuals to see inaccu-
racies about their identities; such inaccuracies can also affect the
utility of the dataset and ability of developers to conduct fairness
evaluations.
3.4
Preprocessing/Cleaning/Labeling
Speech datasets usually go through significant processing and clean-
ing, since audio segments need to be aligned and standardized, and
transcriptions also often need to be annotated.
3.4.1
When generating the dataset, was any background noise deleted
or adjusted to make all recording qualities similar? Processing dataset
noise is common for speech data. When different recording media
is used, creators often convert speech to uniform formats [187, 238,
258]. Furthermore, there are datasets that explicitly add artificial
noise for speech or perform related augmentations, especially for
tasks such as speech separation or quality assessment [53, 215, 267].
Such transformations should be reported, since they influence the
acoustic and time-series properties of the dataset.
3.4.2
Did the data collectors hire human annotators to transcribe the
data? If so, how trained were the annotators in speech transcription
for this context? How familiar were they with the corpus material,
the vocabulary used, and the linguistic characteristics of different
dialects and accents? The annotation of speech either takes place
by automated means (i.e., an ASR model) to be later reviewed by
human annotators, or is directly annotated by human annotators. In
both cases, it is crucial to consider sociolinguistic factors that influ-
ence the quality of the annotations. Wirth et al. [269] showed that
more than 15% of ASR errors can be traced back to flawed ground
truth transcripts. Many times, these errors are a result of annotators
not being fluent speakers of a specific dialect or accent [18, 55],
with false annotations being systematically found for dialects of
underrepresented groups such as African American English [114].
To mitigate such phenomena, creators should recruit annotators
that have extensive knowledge of dialects or accents appearing in
the speech corpus, and are familiar with the vocabularies included.
Furthermore, many languages and dialects contain features that are
exclusive (e.g. certain vowels [203]), are highly agglutinative [251],
or even do not have a written form. In such cases, it is important
to define guidelines on how to transcribe speech [188], drawing
from existing consortium guidelines [27, 155, 208] or linguistically
motivated rules [190]. Dataset creators should explain how anno-
tators were recruited and trained, including training in and use of
transcription tools like Praat [25].
3.4.3
If multiple transcription methods were used, how consistent
were the annotators? How were transcripts validated? Transcriptions
can be unreliable and subjective, so it is important to document
the methodology for generating them. Prior research has shown
that annotators do not always agree on transcriptions [22], es-
pecially in tasks that are highly subjective [66], such as natural-
ness, coloration, discontinuity, loudness, and emotional expression
[71, 101, 215, 228]. Even in simpler transcription cases annotators
might disagree, since language is never perfectly neutral, nor does
it convey a single meaning [260]. Therefore, it is important to im-
plement appropriate inter-annotator scoring systems [32, 208, 257]
that vote on the final annotations and labels of the dataset. Fur-
thermore, appropriate guidelines should be provided that clarify
how annotators should label in ambiguous cases [187], together
with filtering [57], alignment [2], and qualitative error analysis
processes [170] that validate the final annotations. Depending on
language and use cases, such processes can be expanded by prac-
tices that increase diversity, such as usage of versatile transcriptions
for language without standard orthography [9, 102] and scripting
techniques that adapt to annotators’ accents [251].
3.4.4
If the speech data include transcriptions, what software was
used in the generation of the transcriptions (including, e.g., software
used by human transcribers)? Are timestamps included in transcrip-
tions? Are the alignments provided with the transcripts? When a
speech dataset includes human-generated transcriptions, creators
should carefully choose which software to use and why, as it may
interfere with transcription quality. The most commonly used tools
for linguistic annotations are ELAN [173], CLAN [163] and Praat
[25] (Appendix D), which are software programs created for lin-
guistic annotation purposes. They have distinct methods of saving
transcription files, and provide multiple methods to auto-segment
the audio files according to the creators’ needs. ELAN and CLAN
provides video annotation options, making it possible to annotate
multimodal datasets [65, 206] while Praat is used more often for
phonetic detailing [91, 225]. When the transcription is done manu-
ally through a basic word processing tool and needs to be aligned
with the speech data, there are forced alignment tools available
(e.g., [88, 174]), given the appropriate ground truth transcription.
Creators can also build their own aligner (e.g., [42]); however, since
each aligner can yield different outputs and may cause different
errors, this leads to dissimilarity in performance levels ([86, 168]).
Timestamps are important, since it is the information used to ex-
tract utterances, and on what level the timestamps are labeled also
play a part in the alignment of the transcription to the audio data.
Inaccurate timestamps will truncate the speech or mix fragments
with neighboring ones [262].
When transcriptions are ASR-generated as a first pass, creators
often use commercial or open source speech-to-text services that
are publicly available (e.g., [8]). However, humans still need to
manually check for errors in the final stage.
3.4.5
Were transcription conventions (such as tagging sche-me, treat-
ment of hate speech or swear words, etc.) disclosed along with the
888

--- Page 9 ---

Augmented Datasheets for Speech Datasets and Ethical Decision-Making
FAccT ’23, June 12–15, 2023, Chicago, IL, USA
corpus? Because there are multiple transcription conventions avail-
able to dataset creators, it is thus difficult for users to know how
a transcription is generated without additional information. Even
datasets managed by the same organization can have different con-
ventions.3 Even if the creators decide to use a well-known conven-
tion such as the Text Encoding Initiative (TEI) [249] or the CHAT
standard [164], or decide to follow a transcription methodology
used by a widely used corpus like Librispeech [200] or Common
Voice [12], it is still necessary to provide a detailed transcription
convention along with the actual dataset. Some necessary details
to include are: where to put utterance boundaries; how to treat
incomplete or unintelligible speech; how to standardize foreign
words or loanwords; and whether and to what extent non-lexical
backchannels (e.g., filler words) should be included in the regu-
lar transcript [223]. As any form of hate speech or swearing may
occur in spontaneous speech collection, the onus is also on the cre-
ators to decide whether they will redact those terms or leave them
in the transcription. Commercial speech-to-text products provide
the option of profanity filters as well (e.g., [1]). An additional set
of conventions to consider is tagging, which is done for specific
types of information the dataset intends to deliver. This includes
grammatical tagging of part-of-speech [112, 226], emotion tagging
[14, 59, 237], and audio event or type tagging [79, 150, 252].
3.4.6
Is additional coding performed, separate to transcriptions and
tagging? In case of special coding done in addition to the textual
transcription or tagging, there is no conventional systematization
among dataset creators. Some datasets include information such
as background noise in their transcription—even specifying which
types of noise they are [13, 15, 164]. Others simply include the
basic orthographic and/or phonetic transcription. There may also
be additional linguistic information coded, depending on the spe-
cialty the dataset is focusing on, such as discoursal, stylistic, or
pragmatic information [77]. For example, the Hong Kong Corpus
of Spoken English [46] has prosodic features such as tone bound-
aries, prominence and intonation types, represented in the data.
While such annotation conventions are fairly common in linguistic
research [33, 41], this is not the case in the broader speech dataset
community, so detailed explanations should be provided.
3.5
Uses/Distribution/Maintenance
Since the purpose of speech datasets depends on whether they
are for public, commercial, or private use, we pose questions can
inform the possibilites and limits of their use, distribution, and
maintenance.
3.5.1
How are redactions performed on the dataset? Are personally
identifiable information or sensitive information removed from only
transcripts, audio censored from the speech data, or both? A critical
component of dataset creation is the redaction4 of information that
3For example, even though they were both created by the Korean government, KSpon-
Speech [13] and AI Hub [176] both provide the orthographic and phonetic transcription
of a single word if the speaker enunciates in a non-standardized way, but the ordering
is different, requiring the users to pre-process the transcription in two different ways.
4The United States National Institute of Standards and Technology defines several
terminologies in the field of redaction: personal or identifying information is used
to indicate information that is either from individuals or used to identify a certain
individual. De-identification or anonymization are terms used to refer to the process of
removing the association between the representation in the dataset and the represented
might violate the privacy of data-subjects or can be used for harm,
especially against vulnerable populations in the data [218]. While
the release of a speech dataset allows for the broader public to gain
access to data, this may create tension between the protection of
privacy and the goals of transparent data use. Data redaction or
de-identification can ameliorate this tension [75], and this redaction
of personal information is often exemplified in the medical domain
[52]. Since anonymization and filtering techniques have limited
success [240] and/or significantly lower the quality of speech [157,
272], the most efficient method for both protecting individuals and
maintaining quality of the data is the redaction of speech and the
corresponding captions that could leak personal information to the
public [93]. In the best case, both the transcript and audio would be
redacted [123]; the next best effort is often observed where only the
transcript is redacted but not the audio [13, 164, 176]. Furthermore,
privacy issues should also be addressed via informed consent. If data
subjects know that what they say might become publicly available
information, that can mitigate the risks that they say something
they would not like to be released publicly.
3.5.2
Is there any part of this dataset that is privately held but can
be requested for research purposes? Many times, a specific dataset
is a subset of a larger one, but the extended resource might only be
available as a commercial product [245]. Similarly, parts of a dataset
might not be provided publicly due to privacy constraints, limited
access based on profession or citizenship, or other reasons [130]. If
it is possible to use the extended version of a dataset, it is ideal to
disclose this and elucidate the corresponding access requirements.
3.5.3
Is there a sample dataset distributed? If so, how well does the
sample represent the actual dataset? Do they include all forms of
speech included in the dataset? How big is the sample? Dataset own-
ers often provide a light version of the corpus, which can be used
when there are data size limitations [45]. In this case, the sampled
version should ideally contain the same properties of the original
sample, both qualitatively (using similar metadata and and annota-
tion conventions) and quantitatively (containing observations of
different linguistic groups at similar rates). Differences between the
sampled and full dataset should be disclosed to users.
3.5.4
Aside from this datasheet, is other documentation available
about the data collection process (e.g., agreements signed with data
subjects and research methodology)? More elaborate repositories are
often necessary [188] to contain the exact agreements signed with
data-subjects and annotators, read-me files that describe metadata,
audio, technical infrastructure, and documentation of the overall
collection process. Such documentation can ensure the reproducibil-
ity of datasets, the identification of errors, and the reassurance of
best practices in ethical dataset development.
4
DISCUSSION & LIMITATIONS
Our augmented datasheets provide a blueprint of considerations
that should be carefully reviewed and addressed by practitioners.
The benefits to dataset creators include ensuring standardization of
dataset documentation, enhancing transparency of dataset contents,
individual, and redaction indicates the process of removing any personal or sensitive
information from the dataset [75]. Though terminologically distinct in specific ways,
the three terms are used interchangeably in the field of speech datasets.
889

--- Page 10 ---

FAccT ’23, June 12–15, 2023, Chicago, IL, USA
Trovato et al.
clarifying the underlying motivations and process of data collection,
and encouraging explicit consideration of underrepresented linguis-
tic subpopulations and socioeconomic/demographic groups. The
benefits to dataset users include more comprehensive understand-
ing of dataset utility, and easier decision-making on data selection
for more robust and inclusive SLT—especially for data on under-
represented groups. Regardless of whether the datasheet questions
are being answered by users or creators, engaging with each ques-
tion can provide valuable reflexive knowledge on ethical machine
learning development. We suggest that dataset creators release a
completed augmented datasheet alongside their speech dataset to
inform the broader research community about the dataset’s possi-
bilities and limitations; this release also sets an example for more
ethical, inclusive, and transparent machine learning practices.
We encourage SLT practitioners to view datasheets as a collabo-
rative process, engaging dataset users, data subjects, and affected
communities. A plausible path would be to perform user-centered
research before creating a dataset [167] in order to understand pri-
vacy concerns of data-subjects, implement safe-guards about the
metadata released, and develop corresponding agreement forms
[214]. Simultaneously, dataset creators should develop protocols
and data retention strategies through IRB or institutional ethics
committees [255]. Especially in cases of datasets that focus on low-
resource and vulnerable communities, dataset creators should ide-
ally consult and cooperate with local communities that can inform
the ethical data collection [2, 37, 132, 236], by taking into consider-
ation the geopolitical origin and properties of dialects, accents, and
languages. Furthermore, it is valuable to perform in-the-wild exper-
imentation including focus groups on developed SLT applications,
which can uncover issues and harms affecting user populations [51].
Our augmented datasheets mark an improvement over the cur-
rent state of speech dataset documentation. During our large-scale
literature and dataset review, we found numerous ethical questions
remained unaddressed, and many dataset properties undisclosed,
leading to confusion about dataset utility (Appendix C). That said,
there are still several limitations of our work. These limitations
primarily stem from two factors: the generation of the datasheet
questions, and the lack of ability to dictate how the datasheets will
be used on speech datasets. Regarding the first limitation, our po-
sitionalities (predominantly as researchers) limit our perspectives.
To address this concern, we performed an extensive literature re-
view to uncover pain points emerging during practitioners’ speech
dataset development processes. Regarding the second limitation,
we encourage datasheet use for practitioners—not just individually,
but also in an updating feedback-loop between dataset creators and
users. Furthermore, our datasheets can only be used as a tool, and
cannot make unilateral ethical choices on behalf of practitioners in
lieu of deeper conversations.
For example, in domains such as literacy assessment [22, 194,
277] it is expected that ASR models are only robust to a “standard”
conception of language, rather than encompassing more diverse,
atypical speech. As another example, models of speech recognition
or synthesis in affective computing might support users to under-
stand or express their feelings [14, 93, 157, 169, 260]. But, dataset
creators may be concerned about this work mediating serious bi-
ases when humans assess or interpret the emotional conditions of
others during data labeling, potentially leading to physiognomic
and pseudoscientific inferences [66, 242]. The ethical choices that
practitioners must make in these use cases are ones that augmented
datasheets can help with in information gathering and conversation
starting, but not with final decision-making.
We also believe additional research is needed in the space, espe-
cially as emerging techniques are introduced. For example, synthet-
ically generated data using generative AI [5, 29] could serve as a
solution for expanding low-resource language datasets [19, 146];
however, this raises further ethical questions about diversity, au-
thenticity, and robustness of included speech data. Our proposed
augmented datasheets can serve as a tool to evaluate, document,
and discuss such advancements applied to SLT.
5
RESEARCH ETHICS & SOCIAL IMPACT
When conceptualizing the augmented datasheets template, we fo-
cused on issues of diversity and inclusion of linguistic subpopula-
tions, and ethical treatment of data-subjects and annotators. We did
not obtain or use any private or sensitive information, nor did we
recruit users or perform experiments. Our augmented datasheets
framework has broader impact by increasing transparency of speech
datasets and fostering ethical decision-making by dataset users and
creators, who will be prompted with questions such as: the rep-
resentativeness of linguistic subpopulations and socioeconomic
groups in their data; the ethical treatment of speaker subjects (such
as avoiding “symbolic violence” or release of private data); and
the proper designation of linguistic features (such as referring to a
speaker’s dialect with a term the speaker identifies with). Practi-
tioners can use our augmented datasheets to proactively consider
social features that can mitigate biased SLT outcomes.
REFERENCES
[1] [n. d.]. Enable the profanity filter; cloud speech-to-text documentation google
cloud. https://cloud.google.com/speech-to-text/docs/profanity-filter
[2] Basil Abraham, Danish Goel, Divya Siddarth, Kalika Bali, Manu Chopra, Monojit
Choudhury, Pratik Joshi, Preethi Jyoti, Sunayana Sitaram, and Vivek Seshadri.
2020. Crowdsourcing speech data for low-resource languages from low-income
workers. In Proceedings of the 12th Language Resources and Evaluation Conference.
2819–2826.
[3] Martine Adda-Decker and Lori Lamel. 2000. The use of lexica in automatic
speech recognition. Lexicon Development for Speech and Language Processing
(2000), 235–266.
[4] Devaraja Adiga, Rishabh Kumar, Amrith Krishna, Preethi Jyothi, Ganesh Ra-
makrishnan, and Pawan Goyal. 2021. Automatic speech recognition in Sanskrit:
A new speech corpus and modelling insights. arXiv preprint arXiv:2106.05852
(2021).
[5] Andrea Agostinelli, Timo I Denk, Zalán Borsos, Jesse Engel, Mauro Verzetti,
Antoine Caillon, Qingqing Huang, Aren Jansen, Adam Roberts, Marco Tagliasac-
chi, et al. 2023.
MusicLM: Generating Music From Text.
arXiv preprint
arXiv:2301.11325 (2023).
[6] Ana Aguiar, Mariana Kaiseler, Mariana Cunha, Hugo Meinedo, J Silva, T Abru-
dan, and PR Almeida. 2014. VOCE Corpus: Ecologically Collected Speech Anno-
tated with Physiological and Psychological Stress Assessments.. In Proceedings
of the Ninth International Conference on Language Resources. 1568–1574.
[7] Afroz Ahamad, Ankit Anand, and Pranesh Bhargava. 2020. Accentdb: A database
of non-native english accents to assist neural speech recognition. arXiv preprint
arXiv:2005.07973 (2020).
[8] Shafayat Ahmed, Nafis Sadeq, Sudipta Saha Shubha, Md Nahidul Islam, Muham-
mad Abdullah Adnan, and Mohammad Zuberul Islam. 2020. Preparation of
bangla speech corpus from publicly available audio & text. In Proceedings of The
12th language resources and evaluation conference. 6586–6592.
[9] Ahmed Ali, Stephan Vogel, and Steve Renals. 2017. Speech recognition challenge
in the wild: Arabic MGB-3. In 2017 IEEE Automatic Speech Recognition and
Understanding Workshop (ASRU). IEEE, 316–322.
[10] Khalid Almeman, Mark Lee, and Ali Abdulrahman Almiman. 2013.
Multi
dialect Arabic speech parallel corpora. In 2013 1st International Conference
890

--- Page 11 ---

Augmented Datasheets for Speech Datasets and Ethical Decision-Making
FAccT ’23, June 12–15, 2023, Chicago, IL, USA
on Communications, Signal Processing, and their Applications (ICCSPA). 1–6.
https://doi.org/10.1109/ICCSPA.2013.6487288
[11] Jerone TA Andrews, Dora Zhao, William Thong, Apostolos Modas, Orestis
Papakyriakopoulos, Shruti Nagpal, and Alice Xiang. 2023. Ethical considerations
for collecting human-centric image datasets. arXiv preprint arXiv:2302.03629
(2023).
[12] Rosana Ardila, Megan Branson, Kelly Davis, Michael Henretty, Michael Kohler,
Josh Meyer, Reuben Morais, Lindsay Saunders, Francis M Tyers, and Gregor
Weber. 2019. Common voice: A massively-multilingual speech corpus. arXiv
preprint arXiv:1912.06670 (2019).
[13] J.-U. Bang, S. Yun, M.-Y. Kim, S.-H.and Choi, Lee, M.-K., Y.-J. Kim, D.-H. Kim,
J. Park, Y.-J. Lee, and S.-H. Kim. 2020. KsponSpeech: Korean Spontaeneous
Sopeech Corpus for Automatic Speech Recognition. Applied Sciences 10, 19
(2020), 6369.
[14] Subham Banga, Ujjwal Upadhyay, Piyush Agarwal, Aniket Sharma, and Prerana
Mukherjee. 2019. Indian EmoSpeech Command Dataset: A dataset for emotion
based speech recognition in the wild. arXiv preprint arXiv:1910.13801 (2019).
[15] Jon Barker, Shinji Watanabe, Emmanuel Vincent, and Jan Trmal. 2018. The
fifth’CHiME’speech separation and recognition challenge: dataset, task and
baselines. arXiv preprint arXiv:1803.10609 (2018).
[16] Yasmine Belkacemi, Eric Buesing, Arpit Goenka, Vinay Gupta, Damian
Lewandowski, and Maurice Obeid. 2022. From speech to insights: The value of
the human voice. McKinsey & Company (January 2022).
[17] Emily M Bender and Batya Friedman. 2018. Data statements for natural lan-
guage processing: Toward mitigating system bias and enabling better science.
Transactions of the Association for Computational Linguistics 6 (2018), 587–604.
[18] Kaushal Santosh Bhogale, Abhigyan Raman, Tahir Javed, Sumanth Doddapaneni,
Anoop Kunchukuttan, Pratyush Kumar, and Mitesh M Khapra. 2022. Effective-
ness of Mining Audio and Text Pairs from Public Data for Improving ASR
Systems for Low-Resource Languages. arXiv preprint arXiv:2208.12666 (2022).
[19] Jayadev Billa. 2021. Leveraging Non-Target Language Resources to Improve
ASR Performance in a Target Language.. In Interspeech. 2581–2585.
[20] Jordan J Bird, Elizabeth Wanner, Anikó Ekárt, and Diego R Faria. 2019. Accent
classification in human speech biometrics for native and non-native english
speakers. In Proceedings of the 12th ACM International Conference on PErvasive
Technologies Related to Assistive Environments. 554–560.
[21] Steven Bird. 2020. Decolonising speech and language technology. In Proceedings
of the 28th International Conference on Computational Linguistics. 3504–3519.
[22] Matthew P Black, Abe Kazemzadeh, Joseph Tepperman, and Shrikanth S
Narayanan. 2011. Automatically assessing the ABCs: Verification of children’s
spoken letter-names and letter-sounds. ACM Transactions on Speech and Lan-
guage Processing (TSLP) 7, 4 (2011), 1–17.
[23] José Luis Blanco, Rubén Fernández Pozo, Doroteo T Toledano, F Javier Caminero,
and Eduardo López Gonzalo. 2011. Analyzing training dependencies and poste-
rior fusion in discriminant classification of apnea patients based on sustained
and connected speech. In Interspeech. International Speech Communication
Association.
[24] Su Lin Blodgett, Solon Barocas, Hal Daumé III, and Hanna Wallach. 2020. Lan-
guage (Technology) is Power: A Critical Survey of “Bias” in NLP. In Proceedings
of the 58th Annual Meeting of the Association for Computational Linguistics. As-
sociation for Computational Linguistics. https://doi.org/10.18653/v1/2020.acl-
main.485
[25] David Boersma, Paul & Weenink. 2023. Praat (Version 6.3.06).
http://www.
praat.org/
[26] Marcely Zanon Boito, Laurent Besacier, Natalia Tomashenko, and Yannick Es-
tève. 2022. A Study of Gender Impact in Self-supervised Models for Speech-to-
Text Systems. arXiv preprint arXiv:2204.01397 (2022).
[27] Marcely Zanon Boito, John Ortega, Hugo Riguidel, Antoine Laurent, Loïc Bar-
rault, Fethi Bougares, Firas Chaabani, Ha Nguyen, Florentin Barbier, Souhir
Gahbiche, et al. 2022. ON-TRAC Consortium Systems for the IWSLT 2022 Dialect
and Low-resource Speech Translation Tasks. arXiv preprint arXiv:2205.01987
(2022).
[28] Hynek Boril, Abhijeet Sangwan, and John HL Hansen. 2012. Arabic Dialect
Identification-’Is the Secret in the Silence?’and Other Observations.. In INTER-
SPEECH. 30–33.
[29] Zalán Borsos, Raphaël Marinier, Damien Vincent, Eugene Kharitonov, Olivier
Pietquin, Matt Sharifi, Olivier Teboul, David Grangier, Marco Tagliasacchi,
and Neil Zeghidour. 2022. Audiolm: a language modeling approach to audio
generation. arXiv preprint arXiv:2209.03143 (2022).
[30] Soumia Bougrine, Aicha Chorana, Abdallah Lakhdari, and Hadda Cherroun.
2017. Toward a Web-based speech corpus for Algerian dialectal Arabic varieties.
In Proceedings of the Third Arabic Natural Language Processing Workshop. 138–
146.
[31] Pierre Bourdieu and Jean-Claude Passeron. 1990. Reproduction in education,
society and culture. Vol. 4. Sage.
[32] Thorsten Brants. 2000. Inter-annotator Agreement for a German Newspaper
Corpus.. In LREC. Citeseer.
[33] David Brazil. 1997. The Communicative Value of Intonation in English Book.
Cambridge University Press.
[34] Hui Bu, Jiayu Du, Xingyu Na, Bengu Wu, and Hao Zheng. 2017. Aishell-1: An
open-source mandarin speech corpus and a speech recognition baseline. In 2017
20th conference of the oriental chapter of the international coordinating committee
on speech databases and speech I/O systems and assessment (O-COCOSDA). IEEE,
1–5.
[35] Joy Buolamwini and Timnit Gebru. 2018. Gender Shades: Intersectional Accu-
racy Disparities in Commercial Gender Classification. In Proceedings of the 1st
Conference on Fairness, Accountability and Transparency (Proceedings of Machine
Learning Research, Vol. 81), Sorelle A. Friedler and Christo Wilson (Eds.). PMLR,
77–91. https://proceedings.mlr.press/v81/buolamwini18a.html
[36] Bradley Butcher, Vincent S Huang, Christopher Robinson, Jeremy Reffin, Sema K
Sgaier, Grace Charles, and Novi Quadrianto. 2021. Causal datasheet for datasets:
An evaluation guide for real-world data analysis and data collection design
using Bayesian Networks. Frontiers in Artificial Intelligence 4 (2021), 612551.
[37] Alena Butryna, Shan-Hui Cathy Chu, Isin Demirsahin, Alexander Gutkin, Linne
Ha, Fei He, Martin Jansche, Cibu Johny, Anna Katanova, Oddur Kjartansson,
et al. 2020. Google crowdsourced speech corpora and related open-source
resources for low-resource languages and dialects: an overview. arXiv preprint
arXiv:2010.06778 (2020).
[38] Mathieu Carrier, Philippe Apparicio, and Anne-Marie Séguin. 2016. Road traffic
noise in Montreal and environmental equity: What is the situation for the most
vulnerable population groups? Journal of Transport Geography 51 (2016), 1–8.
[39] Inigo Casanueva, Thomas Hain, and Phil Green. 2016. Improving generali-
sation to new speakers in spoken dialogue state tracking. In Proceedings of
the Annual Conference of the International Speech Communication Association,
INTERSPEECH. Sheffield, 2726–2730.
[40] J. A. Casey, R. Morello-Frosch, K. Mennitt, D. J.and Fristrup, E. L. Ogburn, and
P. James. 2017. Race/Ethnicity, Socioeconomic Status, Residential Segregation,
and Spatial Variation in Noise Exposure in the Contiguous United States. Envi-
ronmental health perspectives 125, 7 (2017), 077017.
[41] R.T. Cauldwell. 2002. Streaming speech: Listening and pronunciation for advanced
learners of English. Speechninaction.
[42] Malgorzata Ćavar, Damir Ćavar, Dov-Ber Kerler, and Anya Quilitzsch. 2016.
Generating a Yiddish speech corpus, forced aligner and basic ASR system for
the AHEYM project. In Proceedings of the Tenth International Conference on
Language Resources and Evaluation (LREC’16). 4688–4693.
[43] Özlem Çetinoğlu. 2017. A Code-Switching Corpus of Turkish-German Conver-
sations. In Proceedings of the 11th Linguistic Annotation Workshop. Association
for Computational Linguistics, Valencia, Spain, 34–40. https://doi.org/10.18653/
v1/W17-0804
[44] Chen-Yu Chen, Wei-Zhong Zheng, Syu-Siang Wang, Yu Tsao, Pei-Chun Li, and
Ying-Hui Lai. 2020. Enhancing Intelligibility of Dysarthric Speech Using Gated
Convolutional-Based Voice Conversion System.. In INTERSPEECH. 4686–4690.
[45] Guoguo Chen, Shuzhou Chai, Guanbo Wang, Jiayu Du, Wei-Qiang Zhang, Chao
Weng, Dan Su, Daniel Povey, Jan Trmal, Junbo Zhang, et al. 2021. Gigaspeech:
An evolving, multi-domain asr corpus with 10,000 hours of transcribed audio.
arXiv preprint arXiv:2106.06909 (2021).
[46] Winnie Cheng, Christopher Greaves, Martin Warren, et al. 2005. The creation
of a prosodically transcribed intercultural corpus: The Hong Kong Corpus of
Spoken English (prosodic). ICAME journal 29 (2005), 47–68.
[47] Piotr Chlebek, Elizabeth Shriberg, Yang Lu, Tomasz Rutowski, Amir Harati, and
Ricardo Oliveira. 2020. Comparing speech recognition services for HCI applica-
tions in behavioral health. In Adjunct Proceedings of the 2020 ACM International
Joint Conference on Pervasive and Ubiquitous Computing and Proceedings of the
2020 ACM International Symposium on Wearable Computers. 483–487.
[48] Prafulla Kumar Choubey, Anna Currey, Prashant Mathur, and Georgiana Dinu.
2021. Improving gender translation accuracy with filtered self-training. arXiv
preprint arXiv:2104.07695 (2021).
[49] Elvan Çiftçi, Heysem Kaya, Hüseyin Güleç, and Albert Ali Salah. 2018. The
turkish audio-visual bipolar disorder corpus. In 2018 First Asian Conference on
Affective Computing and Intelligent Interaction (ACII Asia). IEEE, 1–6.
[50] Renee Peje Clapham, Lisette van der Molen, RJJH van Son, M van den Brekel, and
Frans JM Hilgers. 2012. NKI-CCRT corpus-speech intelligibility before and after
advanced head and neck cancer treated with concomitant chemoradiotherapy.
In Proceedings of the Eighth International Conference on Language Resources and
Evaluation (LREC’12). 3350–3355.
[51] Leigh Clark, Philip Doyle, Diego Garaialde, Emer Gilmartin, Stephan Schlögl,
Jens Edlund, Matthew Aylett, João Cabral, Cosmin Munteanu, Justin Edwards,
et al. 2019. The state of speech in HCI: Trends, themes and challenges. Interacting
with Computers 31, 4 (2019), 349–371.
[52] Ido Cohn, Itay Laish, Genady Beryozkin, Gang Li, Izhak Shafran, Idan Szpek-
tor, Tzvika Hartman, Avinatan Hassidim, and Yossi Matias. 2019. Audio de-
identification: A new entity recognition task. arXiv preprint arXiv:1903.07037
(2019).
891

--- Page 12 ---

FAccT ’23, June 12–15, 2023, Chicago, IL, USA
Trovato et al.
[53] Joris Cosentino, Manuel Pariente, Samuele Cornell, Antoine Deleforge, and
Emmanuel Vincent. 2020. Librimix: An open-source dataset for generalizable
speech separation. arXiv preprint arXiv:2005.11262 (2020).
[54] Marta R Costa-jussà, Roger Creus, Oriol Domingo, Albert Domínguez, Miquel
Escobar, Cayetana López, Marina Garcia, and Margarita Geleta. 2020. Mt-adapted
datasheets for datasets: template and repository. arXiv preprint arXiv:2005.13156
(2020).
[55] Evie Coussé and Steven Gillis. 2006. Regional bias in the broad phonetic tran-
scriptions of the Spoken Dutch Corpus. In Proceedings of the Fifth International
Conference on Language Resources and Evaluation (LREC’06).
[56] Mathias Creutz, Teemu Hirsimäki, Mikko Kurimo, Antti Puurula, Janne Pylkkö-
nen, Vesa Siivola, Matti Varjokallio, Ebru Arisoy, Murat Saraçlar, and An-
dreas Stolcke. 2007. Morph-based speech recognition and modeling of out-of-
vocabulary words across languages. ACM Transactions on Speech and Language
Processing (TSLP) 5, 1 (2007), 1–29.
[57] Amit Das, Preethi Jyothi, and Mark Hasegawa-Johnson. 2016. Automatic Speech
Recognition Using Probabilistic Transcriptions in Swahili, Amharic, and Dinka..
In INTERSPEECH. 3524–3528.
[58] Datatang. [n. d.]. 500 hours - Italian conversational speech data by mobile
phone. https://www.datatang.ai/datasets/1178?utm_source=PaperwithCode&
amp;utm_medium=PaperwithCode&amp;utm_campaign=PaperwithCode&
amp;utm_id=PaperwithCode&amp;utm_term=PaperwithCode&amp;utm_
content=PaperwithCode
[59] Laurence Devillers, Ioana Vasilescu, and Lori Lamel. 2002. Annotation and detec-
tion of emotion in a task-oriented human-human dialog corpus. In proceedings
of ISLE Workshop, Vol. 20. 43.
[60] Alex DiChristofano, Henry Shuster, Shefali Chandra, and Neal Patwari. 2022.
Performance Disparities Between Accents in Automatic Speech Recognition.
arXiv preprint arXiv:2208.01157 (2022).
[61] Rachel Dorn. 2019. Dialect-specific models for automatic speech recognition
of african american vernacular english. In Proceedings of the Student Research
Workshop Associated with RANLP 2019. 16–20.
[62] Jiayu Du, Xingyu Na, Xuechen Liu, and Hui Bu. 2018. Aishell-2: Transforming
mandarin asr research into industrial scale. arXiv preprint arXiv:1808.10583
(2018).
[63] Priyank Dubey and Bilal Shah. 2022. Deep Speech Based End-to-End Auto-
mated Speech Recognition (ASR) for Indian-English Accents. arXiv preprint
arXiv:2204.00977 (2022).
[64] H. T. Edwards. 1997. Applied Phonetics: The sounds of American English. Singular,
San Diego, CA.
[65] Lotte Eijk, Marlou Rasenberg, Flavia Arnese, Mark Blokpoel, Mark Dingemanse,
Christian F Doeller, Mirjam Ernestus, Judith Holler, Branka Milivojevic, Asli
Özyürek, et al. 2022. The CABB dataset: A multimodal corpus of communicative
interactions for behavioural and neural analyses. NeuroImage 264 (2022), 119734.
[66] Severin Engelmann, Chiara Ullstein, Orestis Papakyriakopoulos, and Jens
Grossklags. 2022. What people think AI should infer from faces. In 2022 ACM
Conference on Fairness, Accountability, and Transparency. 128–141.
[67] Nicholas Evans and Stephen C. Levinson. 2009. The myth of language universals:
Language diversity and its importance for cognitive science. Behavioral and
Brain Sciences 32, 5 (2009), 429–448. https://doi.org/10.1017/S0140525X0999094X
[68] Alessandro Fabris, Stefano Messina, Gianmaria Silvello, and Gian Antonio Susto.
2022. Tackling documentation debt: a survey on algorithmic fairness datasets.
In Equity and Access in Algorithms, Mechanisms, and Optimization. 1–13.
[69] Lingyun Feng, Jianwei Yu, Deng Cai, Songxiang Liu, Haitao Zheng, and Yan
Wang. 2021. ASR-GLUE: A new multi-task benchmark for asr-robust natural
language understanding. arXiv preprint arXiv:2108.13048 (2021).
[70] Siyuan Feng, Olya Kudina, Bence Mark Halpern, and Odette Scharenborg.
2021.
Quantifying bias in automatic speech recognition.
arXiv preprint
arXiv:2103.15122 (2021).
[71] Tiantian Feng, Rajat Hebbar, Nicholas Mehlman, Xuan Shi, Aditya Kommineni,
et al. 2022. A Review of Speech-centric Trustworthy Machine Learning: Privacy,
Safety, and Fairness. arXiv preprint arXiv:2212.09006 (2022).
[72] Gianni Fenu, Hicham Lafhouli, and Mirko Marras. 2020. Exploring algorithmic
fairness in deep speaker verification. In International Conference on Computa-
tional Science and Its Applications. Springer, 77–93.
[73] Robert W. Frick. 1985. Communicating emotion: The role of prosodic features.
Psychological Bulletin 97, 3 (May 1985), 412–429. https://doi.org/10.1037/0033-
2909.97.3.412
[74] Penelope Gardner-Chloros. 2009. Code-switching. Cambridge university press.
[75] Simson Garfinkel et al. 2015. De-identification of Personal Information:. US
Department of Commerce, National Institute of Standards and Technology.
[76] Mahault Garnerin, Solange Rossato, and Laurent Besacier. 2019. Gender rep-
resentation in French broadcast corpora and its impact on ASR performance.
In Proceedings of the 1st International Workshop on AI for Smart TV Content
Production, Access and Delivery. 3–9.
[77] R.G. Garside, G. Leech, and A.M. Mcenery. 1997. Corpus Annotation: Linguistic
Information from Computer Text Corpora. Routledge.
[78] Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman
Vaughan, Hanna Wallach, Hal Daumé Iii, and Kate Crawford. 2021. Datasheets
for datasets. Commun. ACM 64, 12 (2021), 86–92.
[79] Jort F Gemmeke, Daniel PW Ellis, Dylan Freedman, Aren Jansen, Wade
Lawrence, R Channing Moore, Manoj Plakal, and Marvin Ritter. 2017. Au-
dio set: An ontology and human-labeled dataset for audio events. In 2017 IEEE
international conference on acoustics, speech and signal processing (ICASSP). IEEE,
776–780.
[80] Mengzhe Geng, Xurong Xie, Zi Ye, Tianzi Wang, Guinan Li, Shujie Hu, Xuny-
ing Liu, and Helen Meng. 2022. Speaker Adaptation Using Spectro-Temporal
Deep Features for Dysarthric and Elderly Speech Recognition. arXiv preprint
arXiv:2202.10290 (2022).
[81] Kallirroi Georgila, Anton Leuski, Volodymyr Yanov, and David Traum. 2020.
Evaluation of off-the-shelf speech recognizers across diverse dialogue domains.
In Proceedings of the 12th language resources and evaluation conference. 6469–
6476.
[82] James Sneed German, Maria Candea, LeAnn Brown, Timothy Mahrt, and Oriana
Reid-Collins. 2022. Gender Spectrum Speech Corpus. https://hdl.handle.net/
11403/gender_spectrum_speech/v2.1 ORTOLANG (Open Resources and TOols
for LANGuage) –www.ortolang.fr.
[83] K. Gerson and S. Damaske. 2020. The Open. Oxford University Press, Oxford,
NY.
[84] K. Gerson and S. Damaske. 2020. The Science and Art of Interviewing. Oxford
University Press, Oxford, NY.
[85] Daniela Gerz, Pei-Hao Su, Razvan Kusztos, Avishek Mondal, Michał Lis, Eshan
Singhal, Nikola Mrkšić, Tsung-Hsien Wen, and Ivan Vulić. 2021. Multilingual and
cross-lingual intent detection from spoken data. arXiv preprint arXiv:2104.08524
(2021).
[86] Simon Gonzalez, James Grama, and Catherine E Travis. 2020. Comparing the
performance of forced aligners used in sociophonetic research. Linguistics
Vanguard 6, 1 (2020).
[87] Jan Gorisch, Michael Gref, and Thomas Schmidt. 2020. Using Automatic Speech
Recognition in Spoken Corpus Curation. In Proceedings of the 12th International
Conference on Language Resources and Evaluation (LREC), May 11-16, 2020, Palais
du Pharo, Marseille, France. European Language Resources Association, 6423–
6428.
[88] Kyle Gorman, Jonathan Howell, and Michael Wagner. 2011. Prosodylab-aligner:
A tool for forced alignment of laboratory speech. Canadian Acoustics 39, 3
(2011), 192–193.
[89] Jordan R. Green, Robert L. MacDonald, Pan-Pan Jiang, Julie Cattiau, Rus
Heywood, Richard Cave, Katie Seaver, Marilyn A. Ladewig, Jimmy Tobin,
Michael P. Brenner, Philip C. Nelson, and Katrin Tomanek. 2021. Automatic
Speech Recognition of Disordered Speech: Personalized Models Outperform-
ing Human Listeners on Short Phrases. In Proc. Interspeech 2021. 4778–4782.
https://doi.org/10.21437/Interspeech.2021-1384
[90] Roberto Gretter. 2014. Euronews: a multilingual speech corpus for ASR.. In
LREC. 2635–2638.
[91] Nina Grønnum. 2009. A Danish phonetically annotated spontaneous speech
corpus (DanPASS). Speech Communication 51, 7 (2009), 594–603.
[92] Anhong Guo, Ece Kamar, Jennifer Wortman Vaughan, Hanna Wallach, and
Meredith Ringel Morris. 2020. Toward fairness in AI for people with disabilities
SBG@ a research roadmap. ACM SIGACCESS Accessibility and Computing 125
(2020), 1–1.
[93] Vikram Gupta, Rini Sharon, Ramit Sawhney, and Debdoot Mukherjee. 2022.
ADIMA: Abuse Detection In Multilingual Audio. In ICASSP 2022-2022 IEEE
International Conference on Acoustics, Speech and Signal Processing (ICASSP).
IEEE, 6172–6176.
[94] Nawar Halabi. 2016. Modern standard Arabic phonetics for speech synthesis. Ph. D.
Dissertation. University of Southampton.
[95] Margot Hanley, Apoorv Khandelwal, Hadar Averbuch-Elor, Noah Snavely, and
Helen Nissenbaum. 2020. An ethical highlighter for people-centric dataset
creation. arXiv preprint arXiv:2011.13583 (2020).
[96] Harveenchadha. [n. d.]. Indic-Voice: Largest Open Source speech corpora for
Indic languages. https://github.com/harveenchadha/indic-voice
[97] François Hernandez, Vincent Nguyen, Sahar Ghannay, Natalia Tomashenko, and
Yannick Esteve. 2018. TED-LIUM 3: twice as much data and corpus repartition
for experiments on speaker adaptation. In International conference on speech
and computer. Springer, 198–208.
[98] Jack Hessel, Zhenhai Zhu, Bo Pang, and Radu Soricut. 2020. Beyond instructional
videos: Probing for more diverse visual-textual grounding on youtube. arXiv
preprint arXiv:2004.14338 (2020).
[99] Sarah Holland, Ahmed Hosny, Sarah Newman, Joshua Joseph, and Kasia
Chmielinski. 2018. The dataset nutrition label: A framework to drive higher
data quality standards. arXiv preprint arXiv:1805.03677 (2018).
[100] Kenneth Holstein, Jennifer Wortman Vaughan, Hal Daumé III, Miro Dudik, and
Hanna Wallach. 2019. Improving fairness in machine learning systems: What
do industry practitioners need?. In Proceedings of the 2019 CHI conference on
human factors in computing systems. 1–16.
892

--- Page 13 ---

Augmented Datasheets for Speech Datasets and Ethical Decision-Making
FAccT ’23, June 12–15, 2023, Chicago, IL, USA
[101] Yi Hu and Philipos C Loizou. 2007. Subjective comparison and evaluation of
speech enhancement algorithms. Speech communication 49, 7-8 (2007), 588–601.
[102] Amir Hussein, Shinji Watanabe, and Ahmed Ali. 2022. Arabic speech recognition
by end-to-end, modular systems and human. Computer Speech & Language 71
(2022), 101272.
[103] Wiebke Toussaint Hutiri, Lauriane Gorce, and Aaron Yi Ding. 2022. Design
Guidelines for Inclusive Speaker Verification Evaluation Datasets. arXiv preprint
arXiv:2204.02281 (2022).
[104] Deeply Inc. 202. Korean Read Speech Corpus. https://github.com/deeplyinc/
Korean-Read-Speech-Corpus
[105] Bahar Irfan, Mehdi Hellou, Alexandre Mazel, and Tony Belpaeme. 2020. Chal-
lenges of a real-world HRI study with non-native english speakers: Can per-
sonalisation save the day?. In Companion of the 2020 ACM/IEEE International
Conference on Human-Robot Interaction. 272–274.
[106] Kazuki Irie, Shankar Kumar, Michael Nirschl, and Hank Liao. 2018. RADMM:
Recurrent adaptive mixture model with applications to domain robust language
modeling. In 2018 IEEE International Conference on Acoustics, Speech and Signal
Processing (ICASSP). IEEE, 6079–6083.
[107] Joseph Darius Jaafari and Nicole Lewis. 2019. In Court, Where Are Siri and
Alexa? The Marshall Project (February 2019).
[108] Abigail Z. Jacobs and Hanna Wallach. 2021. Measurement and Fairness. In
Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Trans-
parency. ACM. https://doi.org/10.1145/3442188.3445901
[109] Adam Janin, Don Baron, Jane Edwards, Dan Ellis, David Gelbart, Nelson Morgan,
Barbara Peskin, Thilo Pfau, Elizabeth Shriberg, Andreas Stolcke, et al. 2003. The
ICSI meeting corpus. In 2003 IEEE International Conference on Acoustics, Speech,
and Signal Processing, 2003. Proceedings.(ICASSP’03)., Vol. 1. IEEE, I–I.
[110] Dinesh Babu Jayagopi, Samira Sheikhi, David Klotz, Johannes Wienke, Jean-
Marc Odobez, Sebastian Wrede, Vasil Khalidov, Laurent Nguyen, Britta Wrede,
and Daniel Gatica-Perez. 2012. The vernissage corpus: A multimodal human-
robot-interaction dataset. Technical Report.
[111] Pin Ji, Yang Feng, Jia Liu, Zhihong Zhao, and Zhenyu Chen. 2022. ASRTest:
automated testing for deep-neural-network-driven speech recognition systems.
In Proceedings of the 31st ACM SIGSOFT International Symposium on Software
Testing and Analysis. 189–201.
[112] Janne Bondi Johannessen, Kristin Hagen, Joel Priestley, and Lars Nygaard. 2007.
An advanced speech corpus for Norwegian. In Proceedings of the 16th Nordic
Conference of Computational Linguistics (NODALIDA 2007). 29–36.
[113] Khia A Johnson, Molly Babel, Ivan Fong, and Nancy Yiu. 2020. SpiCE: A new
open-access corpus of conversational bilingual speech in Cantonese and English.
In Proceedings of the 12th Language Resources and Evaluation Conference. 4089–
4095.
[114] Taylor Jones, Jessica Rose Kalbfeld, Ryan Hancock, and Robin Clark. 2019.
Testifying while black: An experimental study of court reporter accuracy in
transcription of African American English. Language 95, 2 (2019), e216–e252.
https://doi.org/10.1353/lan.2019.0042
[115] Chae Kwan Jung. 2021. Designing and building the Korean English Learners’
Spoken Corpus (KELSC). Studies in Foreign Language Education 35, 3 (2021),
209–223.
[116] Virender Kadyan, Taniya Hasija, and Amitoj Singh. 2022. Prosody features based
low resource Punjabi children ASR and T-NT classifier using data augmentation.
Multimedia Tools and Applications (2022), 1–22.
[117] Sayash Kapoor and Arvind Narayanan. 2022. Leakage and the Reproducibility
Crisis in ML-based Science. https://doi.org/10.48550/ARXIV.2207.07048
[118] Sayash Kapoor, Matthew Sun, Mona Wang, Klaudia Jazwinska, and Eliza-
beth Anne Watkins. 2022. Weaving Privacy and Power: On the Privacy Practices
of Labor Organizers in the US Technology Industry. Proceedings of the ACM on
Human-Computer Interaction 6, CSCW2 (2022), 1–33.
[119] Penny Karanasou, Chunyang Wu, Mark Gales, and Philip C Woodland. 2017. I-
vectors and structured neural networks for rapid adaptation of acoustic models.
IEEE/ACM Transactions on Audio, Speech, and Language Processing 25, 4 (2017),
818–828.
[120] Nikolay Karpov, Alexander Denisenko, and Fedor Minkin. 2021. Golos: Russian
dataset for speech research. arXiv preprint arXiv:2106.10161 (2021).
[121] Kazuya Kawakami, Luyu Wang, Chris Dyer, Phil Blunsom, and Aaron van den
Oord. 2020. Learning robust and multilingual speech representations. arXiv
preprint arXiv:2001.11128 (2020).
[122] Jodi Kearns. 2014. Librivox: Free public domain audiobooks. Reference Reviews
28, 1 (2014), 7–8.
[123] Tyler Kendall and Charlie Farrington. 2018. The corpus of regional african
american language. Version 6 (2018), 1.
[124] Byungju Kim, Hyunwoo Kim, Kyungsu Kim, Sungjin Kim, and Junmo Kim.
2019. Learning Not to Learn: Training Deep Neural Networks With Biased
Data. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition (CVPR).
[125] Sunhee Kim, Jooyoung Lee, S.G. Choi, Seunghun Ji, Jeemin Kang, Jongin Kim,
Dohee Kim, Boryong Kim, Eungi Cho, Hojeong Kim, Jeongmin Jang, Jun Hyung
Kim, Bon Ku, Hyung-Min Park, and Minhwa Chung. 2020. Building a Korean
conversational speech database in the emergency medical domain. Phonetics and
Speech Sciences 12 (12 2020), 81–90. https://doi.org/10.13064/KSSS.2020.12.4.081
[126] Andreas Kirkedal, Marija Stepanović, and Barbara Plank. 2020. FT speech:
Danish parliament speech corpus. arXiv preprint arXiv:2005.12368 (2020).
[127] Keith Kirkpatrick. 2020. Natural language misunderstanding. Commun. ACM
63, 11 (2020), 17–18.
[128] Allison Koenecke, Andrew Nam, Emily Lake, Joe Nudell, Minnie Quartey, Zion
Mengesha, Connor Toups, John R. Rickford, Dan Jurafsky, and Sharad Goel.
2020. Racial disparities in automated speech recognition. Proceedings of the
National Academy of Sciences 117, 14 (March 2020), 7684–7689. https://doi.org/
10.1073/pnas.1915768117
[129] Pang Wei Koh, Shiori Sagawa, Henrik Marklund, Sang Michael Xie, Marvin
Zhang, Akshay Balsubramani, Weihua Hu, Michihiro Yasunaga, Richard Lanas
Phillips, Irena Gao, Tony Lee, Etienne David, Ian Stavness, Wei Guo, Berton
Earnshaw, Imran Haque, Sara M Beery, Jure Leskovec, Anshul Kundaje, Emma
Pierson, Sergey Levine, Chelsea Finn, and Percy Liang. 2021. WILDS: A Bench-
mark of in-the-Wild Distribution Shifts. In Proceedings of the 38th International
Conference on Machine Learning (Proceedings of Machine Learning Research,
Vol. 139), Marina Meila and Tong Zhang (Eds.). PMLR, 5637–5664.
[130] Rostislav Kolobov, Olga Okhapkina, Olga Omelchishina, Andrey Platunov,
Roman Bedyakin, Vyacheslav Moshkin, Dmitry Menshikov, and Nikolay
Mikhaylovskiy. 2021. Mediaspeech: Multilanguage asr benchmark and dataset.
arXiv preprint arXiv:2103.16193 (2021).
[131] Huib Kouwenhoven, Mirjam Ernestus, and Margot Van Mulken. 2018. Register
variation by Spanish users of English: The Nijmegen Corpus of Spanish English.
Corpus Linguistics and Linguistic Theory 14, 1 (2018), 35–63.
[132] Roland Kuhn, Fineen Davis, Alain Désilets, Eric Joanis, Anna Kazantseva, Re-
becca Knowles, Patrick Littell, Delaney Lothian, Aidan Pine, Caroline Run-
ning Wolf, et al. 2020. The Indigenous Languages Technology project at NRC
Canada: An empowerment-oriented approach to developing language software.
In Proceedings of the 28th international conference on computational linguistics.
5866–5878.
[133] Baybars Kulebi, Carme Armentano-Oller, Carlos Rodríguez-Penagos, and Marta
Villegas. 2022. ParlamentParla: A speech corpus of catalan parliamentary ses-
sions. In Proceedings of the Workshop ParlaCLARIN III within the 13th Language
Resources and Evaluation Conference. 125–130.
[134] Vinit Kumar, Avinash Kumar, and S Shahnawazuddin. 2022. Creating robust
children’s ASR system in zero-resource condition through out-of-domain data
augmentation. Circuits, Systems, and Signal Processing 41, 4 (2022), 2205–2220.
[135] Raja S Kushalnagar, Walter S Lasecki, and Jeffrey P Bigham. 2012. A readability
evaluation of real-time crowd captions in the classroom. In Proceedings of the
14th international ACM SIGACCESS conference on Computers and accessibility.
71–78.
[136] Egor Lakomkin, Sven Magg, Cornelius Weber, and Stefan Wermter. 2019. KT-
speech-crawler: Automatic dataset construction for speech recognition from
YouTube videos. arXiv preprint arXiv:1903.00216 (2019).
[137] Swaran Lata and Somnath Chandra Vijay Kumar. 2010. Development of Lin-
guistic Resources and Tools for Providing Multilingual Solutions in Indian
Languages—A Report on National Initiative. In Proceedings of the Seventh Inter-
national Conference on Language Resources and Evaluation (LREC’10).
[138] Alexander LeClair and Collin McMillan. 2019. Recommendations for datasets
for source code summarization. arXiv preprint arXiv:1904.02660 (2019).
[139] Bowon Lee, Mark Hasegawa-Johnson, Camille Goudeseune, Suketu Kamdar,
Sarah Borys, Ming Liu, and Thomas Huang. 2004. AVICAR: Audio-visual speech
corpus in a car environment. In Eighth International Conference on Spoken
Language Processing.
[140] Gilwoo Lee, Zhiwei Deng, Shugao Ma, Takaaki Shiratori, Siddhartha S Srinivasa,
and Yaser Sheikh. 2019. Talking with hands 16.2 m: A large-scale dataset of
synchronized body-finger motion and audio for conversational motion anal-
ysis and synthesis. In Proceedings of the IEEE/CVF International Conference on
Computer Vision. 763–772.
[141] Seonwoo Lee, Sunhee Kim, and Minhwa Chung. 2022. Building A Speech Corpus
Of Children With Cochlear Implants Via An Enhanced Metadata Structure. In
2022 25th Conference of the Oriental COCOSDA International Committee for the
Co-ordination and Standardisation of Speech Databases and Assessment Techniques
(O-COCOSDA). IEEE, 1–6.
[142] Tan Lee, Yuanyuan Liu, Pei-Wen Huang, Jen-Tzung Chien, Wang Kong Lam,
Yu Ting Yeung, Thomas KT Law, Kathy YS Lee, Anthony Pak-Hin Kong, and
Sam-Po Law. 2016. Automatic speech recognition for acoustical analysis and as-
sessment of cantonese pathological voice and speech. In 2016 IEEE international
conference on acoustics, speech and signal processing (ICASSP). IEEE, 6475–6479.
[143] S Lemmety. 2000. Review of speech synthesis technology, Helsinki University of
Technology. Ph. D. Dissertation. Thèse.
[144] Chengfei Li, Shuhao Deng, Yaoping Wang, Guangjing Wang, Yaguang Gong,
Changbin Chen, and Jinfeng Bai. 2022. TALCS: An Open-Source Mandarin-
English Code-Switching Corpus and a Speech Recognition Baseline. ArXiv
abs/2206.13135 (2022).
893

--- Page 14 ---

FAccT ’23, June 12–15, 2023, Chicago, IL, USA
Trovato et al.
[145] Chak-Fai Li, Francis Keith, William Hartmann, and Matthew Snover. 2022.
Combining Unsupervised and Text Augmented Semi-Supervised Learning For
Low Resourced Autoregressive Speech Recognition. In ICASSP 2022-2022 IEEE
International Conference on Acoustics, Speech and Signal Processing (ICASSP).
IEEE, 6892–6896.
[146] Jason Li, Ravi Gadde, Boris Ginsburg, and Vitaly Lavrukhin. 2018. Training
neural speech recognition systems with synthetic speech augmentation. (2018).
[147] Jing Li, Binling Wang, Yiming Zhi, Zheng Li, Lin Li, Qingyang Hong, and Dong
Wang. 2021. Oriental language recognition (OLR) 2020: Summary and analysis.
arXiv preprint arXiv:2107.05365 (2021).
[148] Yuanchao Li, Catherine Lai, Divesh Lala, Koji Inoue, and Tatsuya Kawahara.
2022. Alzheimer’s Dementia Detection through Spontaneous Dialogue with
Proactive Robotic Listeners.. In HRI. 875–879.
[149] Ying Li, Yue Yu, and Pascale Fung. 2012. A Mandarin-English Code-Switching
Corpus. In Proceedings of the Eighth International Conference on Language Re-
sources and Evaluation (LREC’12). European Language Resources Association
(ELRA), Istanbul, Turkey, 2515–2519.
[150] Yuan-Fu Liao, Yung-Hsiang Shawn Chang, Yu-Chen Lin, Wu-Hua Hsu, Matus
Pleva, and Jozef Juhar. 2020. Formosa speech in the wild corpus for improving
taiwanese mandarin speech-enabled human-computer interaction. Journal of
Signal Processing Systems 92 (2020), 853–873.
[151] Shaoshi Ling, Yuzong Liu, Julian Salazar, and Katrin Kirchhoff. 2020. Deep
contextualized acoustic representations for semi-supervised speech recognition.
In ICASSP 2020-2020 IEEE International Conference on Acoustics, Speech and
Signal Processing (ICASSP). IEEE, 6429–6433.
[152] R. Lippi-Green. 1997. English with an accent: Language ideology and discrimina-
tion in the United States. Routledge, London.
[153] Chunxi Liu, Michael Picheny, Leda Sarı, Pooja Chitkara, Alex Xiao, Xiaohui
Zhang, Mark Chou, Andres Alvarado, Caner Hazirbas, and Yatharth Saraf. 2022.
Towards Measuring Fairness in Speech Recognition: Casual Conversations
Dataset Transcriptions. In ICASSP 2022-2022 IEEE International Conference on
Acoustics, Speech and Signal Processing (ICASSP). IEEE, 6162–6166.
[154] Yulan Liu, Charles Fox, Madina Hasan, and Thomas Hain. 2016. The sheffield
wargame corpus-day two and day three. In Proceedings of the Annual Conference
of the International Speech Communication Association, INTERSPEECH. ISCA,
3833–3837.
[155] Yi Liu, Pascale Fung, Yongsheng Yang, Denise DiPersio, Meghan Glenn,
Stephanie Strassel, and Christopher Cieri. 2010. A Very Large Scale Man-
darin Chinese Broadcast Corpus for GALE Project. In Proceedings of the Seventh
International Conference on Language Resources and Evaluation (LREC’10).
[156] Julio C. Hidalgo Lopez, Shelly Sandeep, MaKayla Wright, Grace M. Wandell,
and Anthony B. Law. 2023. Quantifying and Improving the Performance of
Speech Recognition Systems on Dysphonic Speech. Otolaryngology–Head and
Neck Surgery 168, 5 (Jan. 2023), 1130–1138. https://doi.org/10.1002/ohn.170
[157] Paula Lopez-Otero, Laura Docío Fernández, Alberto Abad, and Carmen Garcia-
Mateo. 2017. Depression Detection Using Automatic Transcriptions of De-
Identified Speech.. In INTERSPEECH. 3157–3161.
[158] Hieu-Thi Luong and Hai-Quan Vu. 2016. A non-expert Kaldi recipe for Viet-
namese speech recognition system. In Proceedings of the Third International
Workshop on Worldwide Language Service Infrastructure and Second Workshop on
Open Infrastructures and Analysis Frameworks for Human Language Technologies
(WLSI/OIAF4HLT2016). 51–55.
[159] Saturnino Luz, Fasih Haider, Sofia de la Fuente, Davida Fromm, and Brian
MacWhinney. 2020. Alzheimer’s Dementia Recognition through Spontaneous
Speech: The ADReSS Challenge. In Proceedings of INTERSPEECH 2020. Shanghai,
China. https://arxiv.org/abs/2004.06833
[160] Dau-Cheng Lyu, Tien-Ping Tan, Eng Siong Chng, and Haizhou Li. 2010. Seame:
a mandarin-english code-switching speech corpus in south-east asia. In Eleventh
Annual Conference of the International Speech Communication Association.
[161] Andrew Maas, Quoc V Le, Tyler M O’neil, Oriol Vinyals, Patrick Nguyen, and
Andrew Y Ng. 2012. Recurrent neural networks for noise reduction in robust
ASR. (2012).
[162] Joel Mackenzie, Rodger Benham, Matthias Petri, Johanne R Trippas, J Shane
Culpepper, and Alistair Moffat. 2020. CC-News-En: A large English news
corpus. In Proceedings of the 29th ACM International Conference on Information
& Knowledge Management. 3077–3084.
[163] B. MacWhinney. 2000. The CHILDES Project: Tools for analyzing talk. Lawrence
Erlbaum Associates, Mahwah, NJ.
[164] B. MacWhinney, D. Fromm, M. Forbes, and A. Holland. 2011. AphasiaBank:
Methods for studying discourse. Aphasiology 25 (2011).
[165] Alexandre Magueresse, Vincent Carles , and Evan Heetderks. 2020.
Low-
Resource Languages: A Review of Past Work and Future Challenges. arXiv
preprint arXiv:2006.07264v1 (2020).
[166] Khyati Mahajan and Samira Shaikh. 2021. On the need for thoughtful data
collection for multi-party dialogue: A survey of available corpora and collection
methods. In Proceedings of the 22nd Annual Meeting of the Special Interest Group
on Discourse and Dialogue. 338–352.
[167] Raju Maharjan, Kevin Doherty, Darius Adam Rohani, Per Bækgaard, and Jakob E
Bardram. 2022. Experiences of a Speech-enabled Conversational Agent for the
Self-report of Well-being among People Living with Affective Disorders: An
In-the-Wild Study. ACM Transactions on Interactive Intelligent Systems (TiiS) 12,
2 (2022), 1–29.
[168] Tristan J Mahr, Visar Berisha, Kan Kawabata, Julie Liss, and Katherine C Hustad.
2021. Performance of forced-alignment algorithms on children’s speech. Journal
of Speech, Language, and Hearing Research 64, 6S (2021), 2213–2222.
[169] Adria Mallol-Ragolta, Nicholas Cummins, and Björn W Schuller. 2020. An
Investigation of Cross-Cultural Semi-Supervised Learning for Continuous Affect
Recognition.. In INTERSPEECH. 511–515.
[170] Nina Markl and Catherine Lai. 2021. Context-sensitive evaluation of automatic
speech recognition: considering user experience & language variation. In Pro-
ceedings of the First Workshop on Bridging Human–Computer Interaction and
Natural Language Processing. 34–40.
[171] John Markoff. 2019. From Your Mouth to Your Screen, Transcribing Takes the
Next Step. New York Times (October 2019).
[172] Joshua L Martin. 2021. Spoken Corpora Data, Automatic Speech Recognition,
and Bias Against African American Language: The case of Habitual’Be’. In Pro-
ceedings of the 2021 ACM conference on fairness, accountability, and transparency.
284–284.
[173] The Language Archive Max Planck Institute for Psycholinguistics. 2022. ELAN
(Version 6.4). https://archive.mpi.nl/tla/elan
[174] Michael McAuliffe, Michaela Socolof, Sarah Mihuc, Michael Wagner, and Morgan
Sonderegger. 2017. Montreal forced aligner: Trainable text-speech alignment
using kaldi.. In Interspeech, Vol. 2017. 498–502.
[175] Gita Mehta and Anne Cutler. 1988. Detection of target phonemes in spontaneous
and read speech. Language and Speech 31, 2 (1988), 135–156.
[176] Paul Meier. 2022 [Online]. AI Hub.
https://aihub.or.kr/aihubdata/data/view.
do?currMenu=116&topMenu=100&aihubDataSe=ty&dataSetSn=118
[177] Carlos Mena, Michal Borsky, David Erik Mollberg, Smári Freyr, Guðmundsson
Staffan, Hedström Ragnar, Pálsson Ólafur, Helgi Jónsson, Sunneva Þorsteins-
dóttir, Jóhanna Vigdís Guðmundsdóttir, Eydís Huld Magnúsdóttir, Ragnheiður
Þórhallsdóttir, and Jon Gudnason. 2021. Samrómur Children Icelandic Speech
21.09. Reykjavik University: Language and Voice Lab.
[178] Helen Meng, PC Ching, Shuk Fong Chan, Yee Fong Wong, and Cheong Chat
Chan. 2004. ISIS: An adaptive, trilingual conversational system with interleaving
interaction and delegation dialogs. ACM Transactions on Computer-Human
Interaction (TOCHI) 11, 3 (2004), 268–299.
[179] Josh Meyer, David Adelani, Edresson Casanova, Alp Öktem, Daniel Whitenack,
Julian Weber, Salomon Kabongo Kabenamualu, Elizabeth Salesky, Iroro Orife,
Colin Leong, Perez Ogayo, Chris Chinenye Emezue, Jonathan Mukiibi, Salomey
Osei, Apelete Agbolo, Victor Akinode, Bernard Opoku, Olanrewaju Samuel,
Jesujoba Alabi, and Shamsuddeen Hassan Muhammad. 2022. BibleTTS: a large,
high-fidelity, multilingual, and uniquely African speech corpus. In Interspeech.
ISCA. https://arxiv.org/pdf/2207.03546.pdf
[180] Josh Meyer, Lindy Rauchenstein, Joshua D Eisenberg, and Nicholas Howell.
2020. Artie bias corpus: An open dataset for detecting demographic bias in
speech applications. In Proceedings of the 12th language resources and evaluation
conference. 6462–6468.
[181] Milagros Miceli, Tianling Yang, Laurens Naudts, Martin Schuessler, Diana Ser-
banescu, and Alex Hanna. 2021. Documenting computer vision datasets: an
invitation to reflexive data practices. In Proceedings of the 2021 ACM Conference
on Fairness, Accountability, and Transparency. 161–172.
[182] Boyd Michailovsky, Martine Mazaudon, Alexis Michaud, Séverine Guillaume,
Alexandre François, and Evangelia Adamou. 2014. Documenting and researching
endangered languages: the Pangloss Collection. (2014).
[183] Microsoft. [n. d.]. Training and testing datasets - speech service - azure cognitive
services. https://learn.microsoft.com/en-us/azure/cognitive-services/speech-
service/how-to-custom-speech-test-and-train
[184] Juliette Millet and Neil Zeghidour. 2019. Learning to detect dysarthria from raw
speech. In ICASSP 2019-2019 IEEE International Conference on Acoustics, Speech
and Signal Processing (ICASSP). IEEE, 5831–5835.
[185] James Milroy and Lesley Milroy. 2012. Authority in language: investigating
standard english. Routledge, London, England.
[186] Shira Mitchell, Eric Potash, Solon Barocas, Alexander D'Amour, and Kristian
Lum. 2021. Algorithmic Fairness: Choices, Assumptions, and Definitions. Annual
Review of Statistics and Its Application 8, 1 (March 2021), 141–163. https://doi.
org/10.1146/annurev-statistics-042720-125902
[187] Omid Mohamad Nezami, Paria Jamshid Lou, and Mansoureh Karami. 2019.
ShEMO: a large-scale validated database for Persian speech emotion detection.
Language Resources and Evaluation 53, 1 (2019), 1–16.
[188] Anssi Moisio, Dejan Porjazovski, Aku Rouhe, Yaroslav Getman, Anja Virkkunen,
Tamás Grósz, Krister Lindén, and Mikko Kurimo. 2022. Lahjoita puhetta–a
large-scale corpus of spoken Finnish with some benchmarks. arXiv preprint
arXiv:2203.12906 (2022).
894

--- Page 15 ---

Augmented Datasheets for Speech Datasets and Ethical Decision-Making
FAccT ’23, June 12–15, 2023, Chicago, IL, USA
[189] Nicolás Morales, Javier Tejedor, Javier Garrido, José Colás, and Doroteo T
Toledano. 2008. STC-TIMIT: Generation of a single-channel telephone cor-
pus. In Proceedings of the Sixth International Conference on Language Resources
and Evaluation (LREC’08).
[190] Hamdy Mubarak, Amir Hussein, Shammur Absar Chowdhury, and Ahmed Ali.
2021. QASR: QCRI Aljazeera Speech Resource–A Large Scale Annotated Arabic
Speech Corpus. arXiv preprint arXiv:2106.13000 (2021).
[191] David G. Myers and Morton Ann Gernsbacher. 2021. Captioning for All. Inside
Higher Ed (September 2021).
[192] Karen Nakamura. 2019. My algorithms have determined you’re not human: AI-
ML, reverse turing-tests, and the disability experience. In The 21st International
ACM SIGACCESS Conference on Computers and Accessibility. 1–2.
[193] J Neto, Hugo Meinedo, and Márcio Viveiros. 2011. A media monitoring solution.
In 2011 IEEE International Conference on Acoustics, Speech and Signal Processing
(ICASSP). IEEE, 1813–1816.
[194] Mauro Nicolao, Michiel Sanders, and Thomas Hain. 2018. Improved acous-
tic modelling for automatic literacy assessment of children. In Proceedings of
Interspeech 2018. ISCA, 1666–1670.
[195] Mohammad Niknazar, Aditya Vempaty, and Ravi Kokku. 2021. Voice Privacy
with Smart Digital Assistants in Educational Settings. In International Conference
on Intelligent Tutoring Systems. Springer, 286–290.
[196] Takeshi Nishida. 2014. Promoting intercultural awareness through native-to-
foreign speech accent conversion. In Proceedings of the 5th ACM international
conference on Collaboration across boundaries: culture, distance & technology.
83–86.
[197] Patrick K O’Neill, Vitaly Lavrukhin, Somshubra Majumdar, Vahid Noroozi,
Yuekai Zhang, Oleksii Kuchaiev, Jagadeesh Balam, Yuliya Dovzhenko, Keenan
Freyberg, Michael D Shulman, et al. 2021. Spgispeech: 5,000 hours of transcribed
financial audio for fully formatted end-to-end speech recognition. arXiv preprint
arXiv:2104.02014 (2021).
[198] openslr.org. 2022. Openslr.org. http://openslr.org/
[199] Madhab Pal, Rajib Roy, Soma Khan, Milton Samirakshma Bepari, and Joyanta
Basu. 2018. PannoMulloKathan: Voice Enabled Mobile App for Agricultural
Commodity Price Dissemination in Bengali Language.. In INTERSPEECH. 1491–
1492.
[200] Vassil Panayotov, Guoguo Chen, Daniel Povey, and Sanjeev Khudanpur. 2015.
Librispeech: an asr corpus based on public domain audio books. In 2015 IEEE
international conference on acoustics, speech and signal processing (ICASSP). IEEE,
5206–5210.
[201] Orestis Papakyriakopoulos and Alice Xiang. 2023. Considerations for Ethical
Speech Recognition Datasets (WSDM ’23). Association for Computing Machin-
ery, New York, NY, USA, 1287–1288. https://doi.org/10.1145/3539597.3575793
[202] Sara Papi, Edmondo Trentin, Roberto Gretter, Marco Matassoni, and Daniele
Falavigna. 2021. Mixtures of deep neural experts for automated speech scoring.
arXiv preprint arXiv:2106.12475 (2021).
[203] Kyubyong Park, Yo Joong Choe, and Jiyeon Ham. 2019. Jejueo Datasets for
Machine Translation and Speech Synthesis. arXiv preprint arXiv:1911.12071
(2019).
[204] Kyubyong Park and Thomas Mulc. 2019. Css10: A collection of single speaker
speech datasets for 10 languages. arXiv preprint arXiv:1903.11269 (2019).
[205] R. Paul. 1995. Language disorders from infancy through adolescence: Assessment
and intervention. Mosby, St.Louis, MO.
[206] Dawa Pengcuo and Daojie Ben. 2021. Research on the Construction of Multi-
modal Corpus of Tibetan Teaching. In 1st International Conference on Education:
Current Issues and Digital Technologies (ICECIDT 2021). Atlantis Press, 408–412.
[207] Bharathi Pilar et al. 2022. Subword Dictionary Learning and Segmentation
Techniques for Automatic Speech Recognition in Tamil and Kannada. arXiv
preprint arXiv:2207.13331 (2022).
[208] Mark A Pitt, Keith Johnson, Elizabeth Hume, Scott Kiesling, and William Ray-
mond. 2005. The Buckeye corpus of conversational speech: Labeling conventions
and a test of transcriber reliability. Speech Communication 45, 1 (2005), 89–95.
[209] Vineel Pratap, Qiantong Xu, Anuroop Sriram, Gabriel Synnaeve, and Ronan
Collobert. 2020. Mls: A large-scale multilingual dataset for speech research.
arXiv preprint arXiv:2012.03411 (2020).
[210] Mahima Pushkarna, Andrew Zaldivar, and Oddur Kjartansson. 2022. Data cards:
Purposeful and transparent dataset documentation for responsible ai. In 2022
ACM Conference on Fairness, Accountability, and Transparency. 1776–1826.
[211] Akam Qader and Hossein Hassani. 2019. Kurdish (Sorani) Speech to Text:
Presenting an Experimental Dataset. arXiv preprint arXiv:1911.13087 (2019).
[212] Stephan Radeck-Arneth, Benjamin Milde, Arvid Lange, Evandro Gouvea, Stefan
Radomski, Max Mühlhäuser, and Chris Biemann. 2015. Open Source German
Distant Speech Recognition: Corpus and Acoustic Model. In Proceedings Text,
Speech and Dialogue (TSD). Pilsen, Czech Republic, 480–488.
[213] Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey,
and Ilya Sutskever. 2022. Robust Speech Recognition via Large-Scale Weak
Supervision. arXiv:arXiv:2212.04356
[214] Nan Bernstein Ratner and Brian MacWhinney. 2018. Fluency Bank: A new
resource for fluency research and practice. Journal of fluency disorders 56 (2018),
69–80.
[215] Chandan KA Reddy, Ebrahim Beyrami, Harishchandra Dubey, Vishak Gopal,
Roger Cheng, Ross Cutler, Sergiy Matusevych, Robert Aichner, Ashkan Aazami,
Sebastian Braun, et al. 2020. The interspeech 2020 deep noise suppression
challenge: Datasets, subjective speech quality and testing framework. arXiv
preprint arXiv:2001.08662 (2020).
[216] Microsoft Research. 2022. Neural networks-based speech enhancement: AI to
improve audio quality. https://www.microsoft.com/en-us/research/project/nn-
speech-enhancement/
[217] Colleen Richey, Maria A Barrios, Zeb Armstrong, Chris Bartels, Horacio Franco,
Martin Graciarena, Aaron Lawson, Mahesh Kumar Nandwana, Allen Stauffer,
Julien van Hout, et al. 2018. Voices obscured in complex environmental settings
(voices) corpus. arXiv preprint arXiv:1804.05053 (2018).
[218] Meredith Ringel Morris. 2019. AI and Accessibility: A Discussion of Ethical
Considerations. arXiv e-prints (2019), arXiv–1908.
[219] Christophe Ris and Stephane Dupont. 2001. Assessing local noise level estima-
tion methods: Application to noise robust ASR. Speech communication 34, 1-2
(2001), 141–158.
[220] GS Robinson and JG Casali. 2000. Speech communications and signal detection
in noise. The noise manual 5 (2000), 567–600.
[221] Tony Robinson, Jeroen Fransen, David Pye, Jonathan Foote, and Steve Renals.
1995. WSJCAMO: a British English speech corpus for large vocabulary continu-
ous speech recognition. In 1995 International Conference on Acoustics, Speech,
and Signal Processing, Vol. 1. IEEE, 81–84.
[222] Negar Rostamzadeh, Diana Mincu, Subhrajit Roy, Andrew Smart, Lauren Wilcox,
Mahima Pushkarna, Jessica Schrouff, Razvan Amironesei, Nyalleng Moorosi,
and Katherine Heller. 2022. Healthsheet: development of a transparency artifact
for health datasets. In 2022 ACM Conference on Fairness, Accountability, and
Transparency. 1943–1961.
[223] Scott Sadowsky. 2022. The Sociolinguistic Speech Corpus of Chilean Spanish
(COSCACH). A socially stratified text, audio and video corpus with multiple
speech registers (2022).
[224] Betul Erdogdu Sakar, M Erdem Isenkul, C Okan Sakar, Ahmet Sertbas, Fikret
Gurgen, Sakir Delil, Hulya Apaydin, and Olcay Kursun. 2013. Collection and
analysis of a Parkinson speech dataset with multiple types of sound recordings.
IEEE Journal of Biomedical and Health Informatics 17, 4 (2013), 828–834.
[225] Elizabeth Salesky, Eleanor Chodroff, Tiago Pimentel, Matthew Wiesner, Ryan
Cotterell, Alan W Black, and Jason Eisner. 2020. A corpus for large-scale phonetic
typology. arXiv preprint arXiv:2005.13962 (2020).
[226] Ana Lúcia Santos, Michel Généreux, Aida Cardoso, Celina Agostinho, and
Silvana Abalada. 2014. A corpus of European Portuguese child and child-directed
speech. In Proceedings of the 9th International Conference on Language Resources
and Evaluation (LREC 2014). European Language Resources Association, 1488–
1491.
[227] Patrick Schramowski, Christopher Tauchmann, and Kristian Kersting. 2022. Can
Machines Help Us Answering Question 16 in Datasheets, and In Turn Reflecting
on Inappropriate Content?. In 2022 ACM Conference on Fairness, Accountability,
and Transparency. 1350–1361.
[228] Garima Sharma and Abhinav Dhall. 2021. A survey on automatic multimodal
emotion recognition in the wild. In Advances in Data Science: Methodologies and
Applications. Springer, 35–64.
[229] Shakeel Ahmad Sheikh, Md Sahidullah, Fabrice Hirsch, and Slim Ouni. 2021.
Machine Learning for Stuttering Identification: Review, Challenges and Future
Directions. https://doi.org/10.48550/ARXIV.2107.04057
[230] Hua Shen, Yuguang Yang, Guoli Sun, Ryan Langman, Eunjung Han, Jasha
Droppo, and Andreas Stolcke. 2022. Improving fairness in speaker verification
via Group-adapted Fusion Network. In ICASSP 2022-2022 IEEE International
Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 7077–
7081.
[231] David Sherfinski and Avi Asher-Schapiro. 2021. U.S. prisons mull AI to analyze
inmate phone calls. Thomson Reuters Foundation News (August 2021).
[232] Xian Shi, Fan Yu, Yizhou Lu, Yuhao Liang, Qiangze Feng, Daliang Wang, Yanmin
Qian, and Lei Xie. 2021. The accented english speech recognition challenge 2020:
open datasets, tracks, baselines, results and methods. In ICASSP 2021-2021 IEEE
International Conference on Acoustics, Speech and Signal Processing (ICASSP).
IEEE, 6918–6922.
[233] Yao Shi, Hui Bu, Xin Xu, Shaoji Zhang, and Ming Li. 2020. Aishell-3: A multi-
speaker mandarin tts corpus and the baselines. arXiv preprint arXiv:2010.11567
(2020).
[234] Koichi Shinoda, Sadaoki Furui, et al. [n. d.]. Tokyo Institute of Technology
Multilingual Speech Corpus-Indonesian (TITML-IDN). ([n. d.]).
[235] Joel Shor, Dotan Emanuel, Oran Lang, Omry Tuval, Michael Brenner, Julie Cat-
tiau, Fernando Vieira, Maeve McNally, Taylor Charbonneau, Melissa Nollstadt,
et al. 2019. Personalizing ASR for dysarthric and accented speech with limited
data. arXiv preprint arXiv:1907.13511 (2019).
[236] Kathleen Siminyu, Kibibi Mohamed Amran, Abdulrahman Ndegwa Karatu,
Mnata Resani, Mwimbi Makobo Junior, Rebecca Ryakitimbo, and Britone
Mwasaru. 2022. Corpus Development of Kiswahili Speech Recognition Test
895

--- Page 16 ---

FAccT ’23, June 12–15, 2023, Chicago, IL, USA
Trovato et al.
and Evaluation sets, Preemptively Mitigating Demographic Bias Through Col-
laboration with Linguists. In Proceedings of the Fifth Workshop on the Use of
Computational Methods in the Study of Endangered Languages. 13–19.
[237] Aghilas Sini, Damien Lolive, Gaëlle Vidal, Marie Tahon, and Élisabeth Delais-
Roussarie. 2018. Synpaflex-corpus: An expressive french audiobooks corpus
dedicated to expressive speech synthesis. In Proceedings of the Eleventh Interna-
tional Conference on Language Resources and Evaluation (LREC 2018).
[238] David Snyder, Guoguo Chen, and Daniel Povey. 2015. Musan: A music, speech,
and noise corpus. arXiv preprint arXiv:1510.08484 (2015).
[239] Ramya Srinivasan, Emily Denton, Jordan Famularo, Negar Rostamzadeh, Fer-
nando Diaz, and Beth Coleman. 2021. Artsheets for Art Datasets. In Thirty-fifth
Conference on Neural Information Processing Systems Datasets and Benchmarks
Track (Round 2).
[240] Brij Mohan Lal Srivastava, Nathalie Vauquier, Md Sahidullah, Aurélien Bellet,
Marc Tommasi, and Emmanuel Vincent. 2020. Evaluating voice conversion-
based privacy protection against informed attackers. In ICASSP 2020-2020 IEEE
International Conference on Acoustics, Speech and Signal Processing (ICASSP).
IEEE, 2802–2806.
[241] Adriana Stan, Junichi Yamagishi, Simon King, and Matthew Aylett. 2011. The
Romanian speech synthesis (RSS) corpus: Building a high quality HMM-based
speech synthesis system using a high sampling rate. Speech Communication 53,
3 (2011), 442–450.
[242] Luke Stark and Jevan Hutson. 2022. Physiognomic Artificial Intelligence. Ford-
ham Intellectual Property, Media and Entertainment Law Journal 32, 4 (2022),
922.
[243] Robert Stojnic, Ross Taylor, Marcin Kardas, Viktor Kerkez, and Ludovic
Viaud. 2022.
Papers with Code-The latest in Machine Learning.
URL:
https://paperswithcode. com (2022).
[244] Vishal Sunder, Prashant Serai, and Eric Fosler-Lussier. 2022. Building an ASR
Error Robust Spoken Virtual Patient System in a Highly Class-Imbalanced
Scenario Without Speech Data. arXiv preprint arXiv:2204.05183 (2022).
[245] Surfingtech. [n. d.].
Free ST American English Corpus.
https://openslr.
magicdatatech.com/45/
[246] Shinnosuke Takamichi, Ludwig Kürzinger, Takaaki Saeki, Sayaka Shiota, and
Shinji Watanabe. 2021.
JTubeSpeech: corpus of Japanese speech collected
from YouTube for speech recognition and speaker verification. arXiv preprint
arXiv:2112.09323 (2021).
[247] Xu Tan, Tao Qin, Frank Soong, and Tie-Yan Liu. 2021. A survey on neural speech
synthesis. arXiv preprint arXiv:2106.15561 (2021).
[248] Rachael Tatman. 2017. Gender and Dialect Bias in YouTube's Automatic Captions.
In Proceedings of the First ACL Workshop on Ethics in Natural Language Processing.
Association for Computational Linguistics. https://doi.org/10.18653/v1/w17-
1606
[249] TEI. [n. d.]. TEI P5: Guidelines for Electronic Text Encoding and Interchange.
([n. d.]).
[250] Louis ten Bosch. 2000. ASR, dialects, and acoustic/phonological distances.. In
INTERSPEECH. 1009–1012.
[251] Daniela Teodorescu, Josie Matalski, Delaney Lothian, Denilson Barbosa, and Car-
rie Demmans Epp. 2022. Cree Corpus: A Collection of nêhiyawêwin Resources.
In Proceedings of the 60th Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers). 6354–6364.
[252] Paul Thompson. 2010. Building a specialised audio-visual corpus. The Routledge
handbook of corpus linguistics (2010), 93–103.
[253] Katrin Tomanek, Françoise Beaufays, Julie Cattiau, Angad Chandorkar, and
Khe Chai Sim. 2021. On-device personalization of automatic speech recognition
models for disordered speech. arXiv preprint arXiv:2106.10259 (2021).
[254] Peter. Trudgill. 2003. A glossary of sociolinguistics. Oxford University Press,
Oxford.
[255] Rosanna Turrisi, Arianna Braccia, Marco Emanuele, Simone Giulietti, Maura
Pugliatti, Mariachiara Sensi, Luciano Fadiga, and Leonardo Badino. 2021. Easy-
Call corpus: a dysarthric speech dataset. arXiv preprint arXiv:2104.02542 (2021).
[256] Marvin I. Herzog Uriel Weinreich, William Labov. 1968. Empirical Foundations
for a Theory of Language Change. In Directions for Historical Linguistics, Win-
fred P. Lehmann and Yakov Malkiel (Eds.). Univer’sity of Texas Press, Austin,
95–195.
[257] Tomáš Valenta, Luboš Šmídl, Jan Švec, and Daniel Soutner. 2014. Inter-annotator
agreement on spontaneous Czech language: Limits of automatic speech recog-
nition accuracy. In Text, Speech and Dialogue: 17th International Conference,
TSD 2014, Brno, Czech Republic, September 8-12, 2014. Proceedings 17. Springer,
390–397.
[258] Christophe Veaux, Junichi Yamagishi, Kirsten MacDonald, et al. 2017. CSTR
VCTK corpus: English multi-speaker corpus for CSTR voice cloning toolkit.
University of Edinburgh. The Centre for Speech Technology Research (CSTR) (2017).
[259] Boris Villazón-Terrazas, Luis M Vilches-Blázquez, Oscar Corcho, and Asunción
Gómez-Pérez. 2011. Methodological guidelines for publishing government
linked data. Linking government data (2011), 27–49.
[260] Petra Wagner, Jonas Beskow, Simon Betz, Jens Edlund, Joakim Gustafson, Gustav
Eje Henter, Sébastien Le Maguer, Zofia Malisz, Eva Szekely, Christina Tånnander,
et al. 2019. Speech synthesis evaluation—state-of-the-art assessment and sug-
gestion for a novel research program. In Proceedings of the 10th Speech Synthesis
Workshop (SSW10).
[261] Payton Walker, Nathan McClaran, Zihao Zheng, Nitesh Saxena, and Guofei Gu.
2022. BiasHacker: Voice Command Disruption by Exploiting Speaker Biases in
Automatic Speech Recognition. In Proceedings of the 15th ACM Conference on
Security and Privacy in Wireless and Mobile Networks. 119–124.
[262] Changhan Wang, Morgane Riviere, Ann Lee, Anne Wu, Chaitanya Talnikar,
Daniel Haziza, Mary Williamson, Juan Pino, and Emmanuel Dupoux. 2021.
Voxpopuli: A large-scale multilingual speech corpus for representation learning,
semi-supervised learning and interpretation. arXiv preprint arXiv:2101.00390
(2021).
[263] Max Weber. 1949. " Objectivity" in social science and social policy. The method-
ology of the social sciences (1949), 49–112.
[264] Kellie Webster, Marta Recasens, Vera Axelrod, and Jason Baldridge. 2018. Mind
the GAP: A balanced corpus of gendered ambiguous pronouns. Transactions of
the Association for Computational Linguistics 6 (2018), 605–617.
[265] R. S. Weiss. 1995. Learning from Strangers: The Art and Method of Qualitative
Interview Studies. Simon & Schuster, New York, NY.
[266] Eline Westerhout and Paola Monachesi. 2006. A pilot study for a Corpus of Dutch
Aphasic Speech (CoDAS). In Proceedings of the Fifth International Conference on
Language Resources and Evaluation (LREC’06). European Language Resources
Association (ELRA), Genoa, Italy.
[267] Gordon Wichern, Joe Antognini, Michael Flynn, Licheng Richard Zhu, Em-
mett McQuinn, Dwight Crow, Ethan Manilow, and Jonathan Le Roux. 2019.
Wham!: Extending speech separation to noisy environments. arXiv preprint
arXiv:1907.01160 (2019).
[268] J Allen Williams Jr. 1968. Interviewer role performance: A further note on bias
in the information interview. Public Opinion Quarterly 32, 2 (1968), 287–294.
[269] Johannes Wirth and Rene Peinl. 2022. ASR in German: A Detailed Error Analysis.
arXiv preprint arXiv:2204.05617 (2022).
[270] Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement De-
langue, Anthony Moi, Pierric Cistac, Tim Rault, Rémi Louf, Morgan Funtowicz,
et al. 2019. Huggingface’s transformers: State-of-the-art natural language pro-
cessing. arXiv preprint arXiv:1910.03771 (2019).
[271] Philip C Woodland, Chris J Leggetter, JJ Odell, Valtcho Valtchev, and Steve J
Young. 1995. The 1994 HTK large vocabulary speech recognition system. In
1995 international conference on acoustics, speech, and signal processing, Vol. 1.
IEEE, 73–76.
[272] Peter Wu, Paul Pu Liang, Jiatong Shi, Ruslan Salakhutdinov, Shinji Watanabe,
and Louis-Philippe Morency. 2021. Understanding the Tradeoffs in Client-
side Privacy for Downstream Speech Tasks. In 2021 Asia-Pacific Signal and
Information Processing Association Annual Summit and Conference (APSIPA ASC).
IEEE, 841–848.
[273] Bo Yang, Xianlong Tan, Zhengmao Chen, Bing Wang, Dan Li, Zhongping Yang,
Xiping Wu, and Yi Lin. 2019. ATCSpeech: A multilingual pilot-controller speech
corpus from real air traffic control environment. arXiv preprint arXiv:1911.11365
(2019).
[274] Zehui Yang, Yifan Chen, Lei Luo, Runyan Yang, Lingxuan Ye, Gaofeng Cheng,
Ji Xu, Yaohui Jin, Qingqing Zhang, Pengyuan Zhang, et al. 2022. Open Source
MagicData-RAMC: A Rich Annotated Mandarin Conversational (RAMC) Speech
Dataset. arXiv preprint arXiv:2203.16844 (2022).
[275] Gary Yeung and Abeer Alwan. 2018. On the difficulties of automatic speech
recognition for kindergarten-aged children. Interspeech 2018 (2018).
[276] Gary Yeung and Abeer Alwan. 2019. A Frequency Normalization Technique for
Kindergarten Speech Recognition Inspired by the Role of f0 in Vowel Perception.
Interspeech 2019 (2019).
[277] Su-Youn Yoon, Chong Min Lee, Klaus Zechner, and Keelan Evanini. 2019. De-
velopment of Robust Automated Scoring Models Using Adversarial Input for
Oral Proficiency Assessment.. In INTERSPEECH. 1871–1875.
[278] Fan Yu, Zhuoyuan Yao, Xiong Wang, Keyu An, Lei Xie, Zhijian Ou, Bo Liu,
Xiulin Li, and Guanqiong Miao. 2021. The SLT 2021 children speech recognition
challenge: Open datasets, rules and baselines. In 2021 IEEE Spoken Language
Technology Workshop (SLT). IEEE, 1117–1123.
[279] Kyongsik Yun, Joseph Osborne, Madison Lee, Thomas Lu, and Edward Chow.
2018. Automatic speech recognition for launch control center communica-
tion using recurrent neural networks with data augmentation and custom
language model. In Disruptive Technologies in Information Sciences, Vol. 10652.
SPIE, 1065202.
[280] Piotr Żelasko, Laureano Moro-Velázquez, Mark Hasegawa-Johnson, Odette
Scharenborg, and Najim Dehak. 2020. That sounds familiar: an analysis of pho-
netic representations transfer across languages. arXiv preprint arXiv:2005.08118
(2020).
[281] Heiga Zen, Viet Dang, Rob Clark, Yu Zhang, Ron J Weiss, Ye Jia, Zhifeng Chen,
and Yonghui Wu. 2019. LibriTTS: A corpus derived from LibriSpeech for text-
to-speech. arXiv preprint arXiv:1904.02882 (2019).
896

--- Page 17 ---

Augmented Datasheets for Speech Datasets and Ethical Decision-Making
FAccT ’23, June 12–15, 2023, Chicago, IL, USA
[282] Junbo Zhang, Zhiwen Zhang, Yongqing Wang, Zhiyong Yan, Qiong Song, Yukai
Huang, Ke Li, Daniel Povey, and Yujun Wang. 2021. speechocean762: An Open-
Source Non-native English Speech Corpus For Pronunciation Assessment. In
Proc. Interspeech 2021.
[283] Ziping Zhao, Zhongtian Bao, Zixing Zhang, Nicholas Cummins, Haishuai Wang,
and Björn Schuller. 2020. Hierarchical attention transfer networks for depression
assessment from speech. In ICASSP 2020-2020 IEEE international conference on
acoustics, speech and signal processing (ICASSP). IEEE, 7159–7163.
[284] Marc A Zissman, Terry P Gleason, Deborah M Rekart, and Beth L Losiewicz.
1996. Automatic dialect identification of extemporaneous conversational, Latin
American Spanish speech. In 1996 IEEE International Conference on Acoustics,
Speech, and Signal Processing Conference Proceedings, Vol. 2. IEEE, 777–780.
[285] Lindsey Zuloaga. 2021. The latest leap in HireVue’s assessment technology.
HireVue (September 2021).
[286] Juan Zuluaga-Gomez, Karel Vesel`y, Igor Szöke, Petr Motlicek, Martin Kocour,
Mickael Rigault, Khalid Choukri, Amrutha Prasad, Seyyed Saeed Sarfjoo, Iuliia
Nigmatulina, et al. 2022. ATCO2 corpus: A Large-Scale Dataset for Research
on Automatic Speech Recognition and Natural Language Understanding of Air
Traffic Control Communications. arXiv preprint arXiv:2211.04054 (2022).
897

--- Page 18 ---

FAccT ’23, June 12–15, 2023, Chicago, IL, USA
Trovato et al.
A
AUGMENTED DATASHEETS FOR SPEECH DATASETS
A.1
Motivation
• What is the speech dataset name, and does the name accurately describe the contents of the dataset?
• Can the dataset be used to draw conclusions on read speech, spontaneous speech, or both?
• Describe the process used to determine which linguistic subpopulations are the focus of the dataset.
A.2
Composition
• How many hours of speech were collected in total (of each type, if appropriate), including speech that is not in the dataset? If there
was a difference between collected and included, why? E.g., if the speech data are from an interview and the dataset contains only the
interviewee’s responses, how many hours of speech were collected in interviews from both interviewer and interviewee?
• How many hours of speech, number of speakers & words are in the dataset (by each type, if appropriate)?
• Are there standardized definitions of linguistic subpopulations that are used to categorize the speech data? How are these linguistic
subpopulations identified in the dataset and described in the metadata?
• For any linguistic subpopulations identified in the dataset, please provide a description of their respective distributions within the
dataset.
• How much of the speech data have corresponding transcriptions in the dataset?
• Does the dataset contain non-speech mediums (e.g. images or video)?
• Do speakers code switch or speak multiple languages, and if so, how is this identified in the data?
• Does the speech dataset focus on a specific topic or set of topics?
• Does the dataset include sensitive content that can induce different emotions (e.g., anger, sadness) that can cause the speakers to
produce unusual pitch or tone deviating from plain speech?
• Does the dataset contain content that complies to the users’ needs, or does it result in symbolic violence (the imposition of religious
values, political values, cultural values, etc.)?
A.3
Collection Process
• What mechanisms or procedures were used to collect the speech data, e.g.: is the data a new recording of read speech or an interview?
Or is it downloaded speech data from public speeches, lectures, YouTube videos or movies, etc.?
• Were all the data collected using the same technical methodology or setting, including the recording environment (e.g., lab, microphone)
and recording information (e.g., sampling rate, number of channels)?
• Is there presence of background noise?
• For interviewer/interviewee speech data: during the interview process, did interviewers consistently ask questions that are “fair and
neutral”?
• Have data subjects consented to the disclosure of the metadata in the dataset? Also, does the metadata include sensitive personal
information such as disability status?
A.4
Preprocessing/cleaning/labeling
• When generating the dataset, was any background noise deleted or adjusted to make all recording qualities similar?
• Did the data collectors hire human annotators to transcribe the data? If so, how trained were the annotators in speech transcription
for this context? How familiar were they with the corpus material, the vocabulary used, and the linguistic characteristics of different
dialects and accents?
• If multiple transcription methods were used, how consistent were the annotators? How were transcripts validated?
• If the speech data include transcriptions, what software was used to generate the transcriptions (including, e.g., software used by
human transcribers)? Are timestamps included in transcriptions? Are the alignments provided with the transcripts?
• Were transcription conventions (such as tagging scheme, treatment of hate speech or swear words, etc.) disclosed along with the
corpus?
• Is additional coding performed, separate to transcriptions and tagging?
A.5
Uses / Distribution / Maintenance
• How are redactions performed on the dataset? Are personally identifiable information or sensitive information removed from only
transcripts, audio censored from the speech data, or both?
• Is there any part of this dataset that is privately held but can be requested for research purposes?
• Is there a sample dataset distributed? If so, how well does the sample represent the actual dataset? Do they include all forms of speech
included in the dataset? How big is the sample?
• Aside from this datasheet, is other documentation available about the data collection process (e.g., agreements signed with data
subjects and research methodology)?
898

--- Page 19 ---

Augmented Datasheets for Speech Datasets and Ethical Decision-Making
FAccT ’23, June 12–15, 2023, Chicago, IL, USA
B
LITERATURE REVIEW
Dataset properties
Inclusion
Medium, source,
recording environment,
license, compensation,
consent
Privacy
Privacy considerations,
method of protection
Diversity
Languages, quantity of
speech/speakers,
demographics,
accents, dialects
Research study considerations
Contect of application, diversity,
inclusion, privacy, user
empowerment, crowdworker
protection, data assesment,
explainability
Augmented datasheets
Motivation
Q: 
....
Composition
Q: 
....
Collection Process
Q: 
....
Processing/ cleaning/ labeling
Q: 
....
Uses / Distribution / Maintenance
Q: 
....
Literature
review
Extraction of ethical considerations,
properties and limitations of datasets
Assignment to related section and
formulation of questions
Datasets review
220 speech datasets 
Research studies
review
335 speech studies
related to algorithmic
fairness and diversity
Figure 1: Overview of literature review and the creation of questions in the augmented datasheets. We reviewed 220 speech
datasets and identified properties that ethically collected datasets should possess. We also identified limitations in terms of
diversity, inclusion, and privacy. Furthermore, we reviewed 335 studies related to algorithmic fairness and diversity, focusing on
178 manuscripts in detail, and extracted data-centric ethical considerations. We mapped this information to the corresponding
sections of the Augmented Datasheets, and formulated speech-specific questions.
B.1
Datasets
We collected 432 datasets from paperswithcode.com [243], huggingface.co [270], and openslr.org [198], all of which contain repositories of
speech corpora. For each platform we extracted any dataset containing the query speech in them. Then, we manually examined the corpus,
removed duplicates, and dropped datasets that were falsely categorized. This resulted in 220 datasets, which we reviewed for best practices
and issues in speech dataset development and can be found here. To get a more systematized overview of the datasets in terms of ethical
considerations, we randomly sampled 100 of the datasets, and created a set of descriptive features we searched for, which can be aggregated
in following categories:
• Diversity - what different properties does a dataset posses?
• Inclusion - how is the dataset created and under which conditions?
• Privacy - how does the dataset protect the privacy of data subjects?
• Other.
The underlying features include information about the amount of hours in the speech corpus, the language, accent, and dialect diversity in
them, technical and procedural aspects in data collection, and distributional and privacy considerations. These categories can be found in
Table 1.
B.2
Research studies
To understand issues associated with algorithmic fairness and diversity in speech, as well as to locate practices that protect and empower
data-subjects and users we further collected and reviewed relevant research studies. We crawled the following research databases: ArXiv, The
ACM Digital Library, Google Scholar, the ACL Anthology, and IEEE Xplore; we also collected preprints and papers published in following
venues: INTERSPEECH, ICASSP, ACL conferences, ACM conferences, NeurIPS, and ICML. In total we collected 1415 papers by using the
query (Bias OR Accent OR Divers* OR Dialect OR Fairness) AND “Speech”. Then we manually reviewed the abstracts of the papers to ensure
that they fall within the scope of our study, yielding 335 papers for in-detail exploration. We created a categorization scheme for ethical
considerations related to machine learning, which can be found in Table 2. The categorization included the context of application of speech
technologies, diversity & inclusion practices, privacy & worker protection concerns, data quality assessment, and models’ robustness &
explainability techniques. Then, we excluded studies that focused on the robustness of machine learning models, since they did not have as
primary focus aspects related to datasets, but rather technical and computational modeling techniques. The final list of papers we studied in
detail consisted of 178 manuscripts, and can be found in the Github repository. An overview of the considerations in these studies can be
found in Figure 3.
899

--- Page 20 ---

FAccT ’23, June 12–15, 2023, Chicago, IL, USA
Trovato et al.
Language
Dialect
Accent
Style
Type
0
10
20
30
40
50
60
Frequency
Focus of dataset
(a) Linguistic diversity
Continuous
Stratified
No
Age
0
10
20
30
40
50
60
70
Frequency
Age diversity in the sample
(b) Age diversity
cc
Yes
Binary
No
Gender
0
10
20
30
40
50
60
Frequency
Gender diversity in the sample
(c) Gender diversity
Natural
Quiet
Multiple
Conversation
Other
Unknown
Condition
0
10
20
30
40
Frequency
Recording Environment
(d) Recording environment
Microphone
Smartphone
PC
Undisclosed
Device
0
5
10
15
20
25
30
35
40
Frequency
Allowed Recording device
(e) Recording device
Public
cc-by
MIT
Apache
GPL
Custom
Unknown
Type
0
10
20
30
40
50
Frequency
Dataset License
(f) License
Figure 2: Descriptive statistics in the reviewed sample of speech datasets
900

--- Page 21 ---

Augmented Datasheets for Speech Datasets and Ethical Decision-Making
FAccT ’23, June 12–15, 2023, Chicago, IL, USA
Table 1: Overview of the dataset properties that we examined in a subset of 100 speech datasets.
Category
Field
Explanation
Diversity
N. languages
How many different languages does the dataset include?
N. hours
How many hours of speech does the dataset include?
N. tokens
How many total and unique tokens (words) does the dataset include?
N. speakers
How many individuals were recorded in the dataset?
Resource
Are these languages low or high resource?
Languages
What languages are included?
Gender
Are different genders included? If yes, which?
Age
Are different ages included? If yes, how?
Accent diversity
Are different accents included?
Accent diversity - classes
How many different accents are included?
Accent classification
What is the criterion to classify accents?
Dialect diversity
Are different dialects included?
Dialect diversity - classes
How many different dialects are included?
Dialect classification
What is the criterion to classify dialects?
Inclusion
Data source
How were the data obtained?
Medium
What recording medium was used?
Dataset structure
Is the dataset balanced in terms of diversity?
Recording Environment
What were the conditions in the recording environment?
Datasheet
Does the dataset have a dedicated datasheet?
Licence
Is the dataset licensed?
Licence type
What is the type of license?
Compensation
Were data-subjects compensated?
Consent
Do dataset creators acknowledge that
they took the informed consent of data subjects?
Privacy
Privacy
Do dataset creators took explicitly
into consideration the privacy of data subjects?
Privacy type
How do dataset creators protect the privacy of data subjects?
Other
Derivative
Is this dataset a derivative of another dataset?
C
AUGMENTED DATASHEETS OF POPULAR DATASETS
We provide sample answers to the speech-specific questions posed by our augmented datasheets on five popular speech datasets: WHAM
[267], LibriSpeech [200], Common Voice [12], VoxPopuli [262], and CORAAL [123]. These example datasheets are available on GitHub at
https://github.com/SonyResearch/project_ethics_augmented_datasheets_for_speech_datasets. Filling out the datasheets provided useful
information about each of them, but also uncovered systematic gaps in their self-disclosed documentation. Focusing on questions from
the motivation section of the augmented datasheets, we found that the full naming conventions of Common Voice, CORAAL, and WHAM
accurately reflected the content of the datasets, but the choice of LibriSpeech and VoxPopuli were more convoluted. In terms of linguistic
population identification, only some creators precisely explained why they chose specific groups to be included in the recordings (e.g.,
CORAAL for African American Language); others simply stated that they wanted to create a multilingual (VoxPopuli, Common Voice) or
English corpus (LibriSpeech). In the disclosed information about the composition of the datasets, we were able to identify the recording hours
in all of them, though the VoxPopuli creators did not explain how they chose which of the Parliament recordings to be included in the final
dataset (there is a large pool of data available online that can be used), while the information about recorded hours in the Common Voice
paper does not reflect the hours in the database, since the latter is constantly growing. Furthermore, we found that VoxPopuli, Common
Voice and LibriSpeech had different definitions of accented speech: Common Voice had a freeform field for data subjects to self-identify;
VoxPopuli classified accents based on country of origin of the speakers; and LibriSpeech used the accuracy of a standard-English ASR model
to predict a segment’s accent status. Regarding the content of the recordings, in no dataset did creators document whether there was speech
that is highly emotional or sensitive, although this could be the case in recordings such as audio-books and parliamentary hearings. Similarly,
although Common Voice is created out of Wikipedia segments, there are no details about whether the content of these sentences might have
901

--- Page 22 ---

FAccT ’23, June 12–15, 2023, Chicago, IL, USA
Trovato et al.
Table 2: Overview of considerations that we matched with the sample of research studies we collected.
Category
Explanation
Context of application
The study discusses issues or solutions for applying ASR systems in a specific social context.
Diversity
The study discusses the limitations of ASR technologies to perform well on different populations.
Inclusion
The study discusses theoretic frameworks on how ASR technologies can be
improved to cover more populations, dialects, accents, social groups, etc.
Privacy
The study discusses privacy issues in ASR or relates to the use of public/gray area data.
Robustness
The study discusses mathematical and technical solutions for improving the performance
of ASR technologies - not data collection methods/quality/properties.
User empowerment
The study discusses ASR technologies & dataset from a civic standpoint.
Crowdworker protection
The study discusses explicitly the issues and rights of crowdworkers who create the data.
Data assessment
The study discusses explicitly how the quality of data
(speech segments, transcriptions) can be assessed in specific socio technical environments.
Explainability
The study discusses how ASR technologies performance can be understood.
Diversity
Inclusion
Context of Application
Robustness
User Empowerment
Data Assessment
Privacy
Explainability
Crowdworker Support
Consideration
0
5
10
15
20
25
percentage (%)
Prevalence of considerations in the reviewed studies
Figure 3: Distribution of ethical considerations in the reviewed sample of SLT studies (N=178). A study could contain more than
one considerations.
negative impact to the data-subjects due to symbolic violence. The questions about the collection process of the datasets yielded that in three
datasets (VoxPopouli, Common Voice, LibriSpeech) there has been no standardization of recording media, nor an exact description about
what recording medium was used for each recording. Furthermore, the VoxPopuli creators do not explain how they trained annotators that
902

--- Page 23 ---

Augmented Datasheets for Speech Datasets and Ethical Decision-Making
FAccT ’23, June 12–15, 2023, Chicago, IL, USA
worked on creating transcriptions for a subset of the available data. Only in CORAAL were redactions specified; this was not clearly the case
in the other datasets.
Our inability to answer specific datasheet questions about all datasets exemplifies the exact reason for which augmented datasheets
should be necessary. Many answers require knowledge that only the dataset creators have. As all the questions listed in the datasheets are
specifically built to target information that both the creators and the users should have knowledge of in order to utilize the dataset in a fair
and precise way, it is crucial for creators to take the datasheet as their guide for revision and incorporate the missing information. Taking
the above into consideration, the application of new questions in the augmented datasheets showed that there is a considerable amount of
improvement dataset creators can make in transparently informing users about the properties of their dataset. Most importantly, when using
these questions as a foundation for developing a dataset, they can make more ethically grounded design choices.
903

--- Page 24 ---

FAccT ’23, June 12–15, 2023, Chicago, IL, USA
Trovato et al.
D
EXAMPLES OF TRANSCRIPTION
Figure 4: Transcription made in Praat, example taken from [131]. Because the data was collected through Dutch-speaking
confederates, the tiers are named ‘Spanish speaker’ and ‘Dutch speaker’. The tiers include the orthographic transcription of
each speakers’ speech, broken into segments accordingly, as well as any human-made noise defined prior, such as [breath] or
[laugh]. There is a separate tier for non-human-made noise, named ‘Background’.
Figure 5: Transcription made in ELAN, example taken from [110]. The dataset annotated not only speech but head location and
movement of the speakers, thus needing both audio and visual tiers. Because the data was collected by German researchers, the
audio tier specifically marked where the speech was produced in German. Instead of detailing different types of noise, the
dataset categorized the utterances into three types: speech, silence and laughter.
904

```
