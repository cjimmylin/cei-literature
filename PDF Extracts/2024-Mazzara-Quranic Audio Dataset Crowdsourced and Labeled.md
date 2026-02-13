---
title: "2024-Mazzara-Quranic Audio Dataset Crowdsourced and Labeled - PDF Extract"
source_pdf: "2024-Mazzara-Quranic Audio Dataset Crowdsourced and Labeled.pdf"
pages: 8
extracted_at: "2026-02-13T09:15:43.523487"
---

# PDF Extract: 2024-Mazzara-Quranic Audio Dataset Crowdsourced and Labeled

**Source PDF:** 2024-Mazzara-Quranic Audio Dataset Crowdsourced and Labeled.pdf
**Total Pages:** 8

---

## Content

```
--- Page 1 ---

Quranic Audio Dataset: Crowdsourced and Labeled
Recitation from Non-Arabic Speakers
1st Raghad Salameh
Innopolis University
Republic of Tatarstan, Russia
r.salameh@innopolis.university
2nd Mohamad Al Mdfaa
Skoltech University
Moscow, Russia
mohamad.almdfaa@skoltech.ru
4th Manuel Mazzara
Innopolis University
Republic of Tatarstan, Russia
m.mazzara@innopolis.ru
3rd Nursultan Askarbekuly
Innopolis University
Republic of Tatarstan, Russia
n.askarbekuly@innopolis.university
Abstract—This paper addresses the challenge of learning to
recite the Quran for non-Arabic speakers. We explore the pos-
sibility of crowdsourcing a carefully annotated Quranic dataset,
on top of which AI models can be built to simplify the learning
process. In particular, we use the volunteer-based crowdsourcing
genre and implement a crowdsourcing API to gather audio
assets. We integrated the API into an existing mobile application
called NamazApp to collect audio recitations. We developed a
crowdsourcing platform called Quran Voice for annotating the
gathered audio assets. As a result, we have collected around
7000 Quranic recitations from a pool of 1287 participants across
more than 11 non-Arabic countries, and we have annotated 1166
recitations from the dataset in six categories. We have achieved a
crowd accuracy of 0.77, an inter-rater agreement of 0.63 between
the annotators, and 0.89 between the labels assigned by the
algorithm and the expert judgments.1
Index
Terms—Crowdsourcing,
Quranic
recitation,
Audio
Dataset, Dataset annotation, AI technology
I. INTRODUCTION
The Quran is the Holy Scripture of Islam, and millions
of Muslims are learning to read and recite it all over the
world. Learning how to recite the Quran correctly in the
original Arabic form is obligatory, however, many Muslims
are of non-Arabic descent and do not speak the language.
Normally, this problem is solved through learning with a
qualified teacher, however, not everyone has access to a human
instructor. AI technology can be used to partially cover this
need, and simplify the process of learning the recitation of the
Quran. In particular, speech recognition models can be used
to detect mistakes in recitation and provide feedback on the
proficiency of the learner [1], [2], [3]. Training such models
requires a large amount of labeled data, more specifically
the recordings of recitations from many different people with
common mistakes and the corresponding labeling.
In this research, we worked on validating the following
hypothesis:
1) A dataset of Quranic recitation audios can be crowd-
sourced from beginner learners via a recitation app.
1For access to related resources including the Quranic Audio Dataset, please
visit the paper webpage.
2) The collected dataset can be labeled through a dedicated
crowdsourcing tool.
Our study aimed to explore two key questions: Are beginner
learners willing to share their voices when reciting the Quran,
and are proficient reciters willing to participate in labeling
audio recordings of recitations? To investigate these hypothe-
ses, we followed a multi-step approach. First, we constructed
a dataset through crowdsourcing, which involved integrating
our project with the mobile application ”NamazApp” to collect
Quranic data. Next, we developed a crowdsourcing tool,
dubbed ”Quran Voice”, to preprocess and label the collected
data. Finally, we conducted manual quality control to validate
the data, ensuring its readiness for use in training machine
learning models.
The rest of the paper is structured as follows. We provide
a brief overview of the existing work for Arabic linguistic
resources and the Quran in Section II. We then discuss the
process of collecting the data and the annotation collection
procedures in Section III. We present detailed information
about the collected dataset in Section IV. Finally, we conclude
our work in Section V.
II. RELATED WORK
Crowdsourcing is the practice of assigning a computation-
ally challenging task to a large, typically online group of
people. It is a good way to break down a manual, large, time-
consuming task into smaller, more manageable tasks to be
completed by distributed workers [4].
Whenever AI research is conducted, datasets are considered
a crucial component. The creation of a high-quality dataset
requires a lot of effort and time.
There are three types of crowdsourcing paradigms for
dataset creation: mechanized labor (paid-for) [5] [6], where
employees receive cash compensation; games with a purpose
(GWAP) [7] [8], where the task is disguised as a game;
and altruistic work (volunteer-based) [9] [10], which relies
on goodwill. Any of the three prominent crowdsourcing
paradigms can be employed.
arXiv:2405.02675v1  [cs.SD]  4 May 2024

--- Page 2 ---

A. Crowdsourcing for Arabic linguistic resources
Many Arabic speech researchers used Crowdsourcing for
both corpus annotation text-based [5] [6] [11], speech-based
[9] [10] [12] [13] [7] [14], and Arabic digitization with
diacritics [8].
In [5], the authors aim to construct Comment Dataset for
Offensive Language Detection. As a result, they annotated
4000 comments with an accuracy of 94% using Amazon
Mechanical Turk.
In [6], the authors outline a two-step methodology for anno-
tating Arabic targets of opinions using Amazon Mechanical
Turk. First, they asked annotators to identify candidate targets
“entities” in a given text. Then, they asked annotators to
identify the opinion polarity (positive, negative, or neutral)
expressed about a specific entity.
In [11], the authors were running experiments to see if
Crowdsourcing can be used for Effective Annotation of
Arabic. They contrasted two methods for linguistically an-
notating an Arabic corpus: part-of-speech (POS) tagging and
grammatical case-ending. The overall results were 50.07%
accuracy for grammatical case endings and 63.91% for POS
tagging. The study demonstrates that crowdsourcing for Arabic
linguistic annotation is ineffective for both objectives since it
calls for experienced annotators.
In [9], the authors aim to create Speech Corpus for
Algerian Arabic Dialectal called Kalam’DZ which includes
the 8 major Algerian Arabic sub-dialects with 4881 speakers
and more than 104.4 hours. Most annotations are made man-
ually by assigning for each utterance the spoken dialect and
validating the speaker’s gender.
In [10], the authors aim to prove that using the altruistic
(volunteer-based) approach is an effective approach by vali-
dating 10% of dialect annotation conducted for Kalam’DZ [9]
which equals 10 hours and 1012 tasks. The contributors are
asked to answer a question about a given audio with one of
the three possible responses (Yes, No, Unknown). The crowd
annotation accuracy was about 81.1%.
In [12], the authors aim to build Massively-Multilingual
Speech Corpus. For Data Collection They collected 2,500
hours of audio from over 50,000 participants. The recordings
are verified by contributors as correct or incorrect.
In [13], the authors aim to gather large speech corpora
for Egyptian dialectal Arabic. Using a designed Game
With a Purpose, they collect transcriptions for 120 audio
files with 1121 Arabic orthographic transcriptions and 1121
transcriptions in the Arabic Chat Alphabet.
In [14], A multi-dialectal speech corpus of DA, produced
by the authors from high-quality broadcast, debate, and discus-
sion programs from Al Jazeera, incorporates both scripted and
spontaneous speech. They obtained dialect labels for 57 hours
of Egyptian, Levantine, Gulf, and North African DA. They
automatically labeled an additional 94 hours by using speaker
linking to recognize utterances made by the same speaker.
In [7], the authors present a GWAP for crowdsourcing
classifications of several dialects of Arabic in multi-
dialectal audio. Players in Lahajet choose a character that
represents the accent after listening to brief audio snippets.
In [8], the authors present tashkeelWAP: A GWAP For
Digitizing Arabic Diacritics. The participants need to validate
images along with their corresponding diacritic-less digitiza-
tion.
B. Crowdsourcing for Quran
Regarding Quran, there are extremely few public speech
datasets for the Quran available. we can mention the following:
In [15], the authors aim to build dataset of crowdsourced
Quranic recitation. They collected 50,000 verses. About 150
verses were manually annotated. The entire dataset has also
been automatically evaluated by using Google Speech-to-text
to first transcript the recording, then using Iqra (a Quran search
engine) to search for the verse using the transcription. If the
result returned by Iqra matches the recorded ayah, they mark
it as correct.
In [16], the authors build a dataset QDAT from the recita-
tion of one verse from the Quran. They gathered 1500 audio
files having both correct and incorrect recitations. Experts
manually annotate the audio files to demonstrate the accuracy
of reciting the Quran with Tajweed while following three rules
of recitation: Al Mad, Ghunnah, and Ikhfaa.
In [17], the authors present a database of Quranic recita-
tions for automatic speech processing based on tajweed cor-
rection. This database contains audio recordings from Surah
AlFatihah where each audio recitation has some purposefully
inserted tajweed (rules of recitations) errors. Experts identify
54 errors that reciters of Surah Al-Fatihah may make and
collect samples for each such error case. 17 volunteers par-
ticipated, Arabic and non-Arabic speakers. Each audio file is
labeled for the case it covers, along with information on the
reciters.
As can be seen, there are not enough public Quranic datasets
available. This leads to each research project independently
developing its own database to facilitate experimentation,
resulting in challenges when comparing findings. Moreover,
crowdsourcing has not been used in Quran annotation. Our
research aims to fill these gaps and examine the willingness
of beginner learners to share their recitations and proficient
reciters to label the gathered data.
III. INITIAL METHODOLOGY PLAN
To construct a high-quality Quranic recitation dataset, we
have followed the crowdsourcing engineering process defined
by [18]. It suggested breaking down the process into four main
stages: Project Definition, Data Preparation, Project Execution,
and Data Evaluation and Aggregation.
A. Project Definition
The first step is to choose the appropriate crowdsourcing
genre. In this project, we choose the altruistic work crowd-
sourcing genre. Secondly, the chosen NLP problem needs to
be decomposed into a set of simple crowdsourcing tasks. We
can define the tasks for our project as the following:

--- Page 3 ---

1) Beginner learners are asked to record their voices while
reciting a specific verse of the Quran.
2) Proficient reciters are asked to listen to audio and
provide the correct classification.
B. Data Preparation
Besides collecting and preparing the data, we must design
the crowdsourcing user interfaces.
1) The first crowdsourcing task: For the first crowdsourc-
ing task, we built a Quran player responsible for collecting
Quranic recitation coupled with, the chapter and verse being
recited, and demographic background information about the
user (id, age, gender, country, platform, Qiraah). The player
contains short chapters of the Quran and gives the users the
ability to:
• See and listen to the desired verse (Aya) being recited by
a Qari (professional reciter).
• Record their voice.
• Compare their recording with the one from the Qari.
• Upload their recorded voice if they want to share it and
receive feedback.
Importantly, the app provides value for beginner learners
since it will help them to learn how to recite Quran correctly
when receiving feedback. Additionally, they can choose to
share the recordings of their recitations as shown in Figure
1a. The Architecture for the Quran player is shown in Figure
1b.
Before storing the audio of the recitation on the server, we
make it pass through our audio standardization pipeline to
ensure consistency and compatibility across audio files. the
pipeline stages are shown in Figure 2. We employed the Pydub
Python library to standardize all audio files by converting them
to the WAV format with a mono channel, 16kHz frequency,
and 2 bytes bit-depth in addition to removing silence seg-
ments. Moreover, we utilized the Noisereduce library [19] to
effectively eliminate background noise from audio recordings.
Fig. 2: Audio standardization pipeline
The Quran player was implemented as an importable pack-
age that can be integrated easily by other apps. Currently,
this player is already imported into Namaz App which was
published on App Store.
2) The second crowdsourcing task: For the second crowd-
sourcing task, we sought to cover words and diacritics mis-
takes on the audio data we collected in the first crowdsourcing
task. For this purpose, we implemented Quran voice web
platform as shown in Figure 3. The website is available in
three languages: Arabic, English, and Russian.
In this task, referred to as Validate Verse Correctness,
proficient reciters can help us validate if the verse has been
read correctly by validating the correctness of letters and
diacritics. The participant were given an audio of a specific
verse to listen to it and label it with one of the following
choices:
• Correct: when the pronunciation is correct with the dia-
critics, regardless of the rules of Tajweed.
• Has mistakes: The answer is incorrect when the pronun-
ciation is wrong with the diacritics, regardless of the rules
of Tajweed.
• Invalid Audio: When there is a problem with the audio.
– Empty / Not related: When the content of the audio
clip is incomprehensible or contains words that have
nothing to do with the Quran or empty, this choice
should be selected.
– Different Verse: when the audio clip contains words
related to the Quran, but not the given verse, this
choice should be selected.
– Multiple Verses: When a reciter reads several verses,
this choice should be selected regardless of whether
the reading is correct or not.
– Incomplete Verse: When the reciter reads the verse
without completing it, or the verse is not completed
for some reason, this choice should be selected.
An annotation guideline was prepared for this task with
real samples from the dataset. In addition to written instruc-
tions, video instructions were also provided for those who
prefer visual aids.
Before the participants access the real tasks, they have to
pass the training session as shown in Figure 4. A set of 62 gold
standards tasks were collected and annotated by experts for
this purpose. The training session has 8 questions: 2 labeled
as Correct, 2 have mistakes, and 1 for each remaining labels.
The participant passes the training session if they score at least
0.6 Matthews Correlation Coefficient. The participant has 5
attempts to pass the training session, otherwise, they will be
excluded.
C. Project Execution
There are decisions to be taken, such as whether the com-
plete dataset should be annotated more than once to enable a
reconciliation and verification stage (better quality, but greater
costs), or whether it is sufficient to have only two or three
annotators per task as long as they can agree. Some of the
studies mentioned in Section II used 3 judgments and others
used 5 judgments. For our study, we started by taking 3
judgments. The details are described in Section III-D.
To ensure quality annotations, we implement a rigorous
quality control process. In addition to the training session that
participants should pass to access real tasks, we use control
tasks to monitor their performance during the annotation
process. The initial set of control tasks is manually annotated
by experts, and we convert real tasks with full inter-annotator
agreement to control tasks. This helps us adjust participants’
scores and maintain high-quality annotations.
To encourage participation in the voluntary-based crowd-
sourcing approach, advertising efforts were made through

--- Page 4 ---

(a) Quran player - Namaz App
Firbase Realtime DB
Firbase Authentication
Azure Blob Storage
Azure Virtual Machine
Docker Image
Quran Player
Application
(b) Quran player backend Architecture
Fig. 1: Quran player Architecture for the first crowdsourcing task
Azure Virtual Machine
Docker Image
Quran Voice Annotation Platfrom
Azure Blob Storage
Azure Database for
PostgreSQL flexible
servers
Fig. 3: Quran Voice Architecture for the second crowdsourcing task

--- Page 5 ---

social media. A dedicated Facebook page, called ”Quran
Voice”, was created to publish promotional posts for the
website continuously.
Fig. 4: Training session for validate Verse Correctness task
on Quran Voice
D. Data Evaluation and Aggregation
The difficulty in this stage is in analyzing and combining the
contributions from various contributors into a comprehensive
linguistic resource, and in evaluating the resulting overall
quality.
To aggregate the final annotations for the Validate Recitation
task, we employ the Weighted Majority Voting algorithm,
which is suitable for multi-class classification tasks. This ap-
proach is particularly useful in our study because it considers
the performance score of participants as a weight for their
answers. The aggregation process and the number of judges
involved are illustrated in figure 5.
Fig. 5: Annotation Aggregation for Validate Verse Correctness
task
For data evaluation, We took 10% of the data annotated by
the crowd and let it be manually annotated by an expert.

--- Page 6 ---

IV. RESULTS AND DISCUSSION
A.
Overview of the Collected Datasets
In the first task, a pool of 1287 participants recorded
their voices while reciting specific verses. As a result, we’ve
recorded around 7000 verses, totaling 11.5 hours. Figure 6
illustrates demographic information about the participants.
Among the participants, 47.1% identified as female, and
52.9% identified as male, as illustrated in Figure 6a. Out of
the 1287 participants, only 93 provided their ages, with the
distribution depicted in Figure 6b. As shown in Figures 6c-
6d, The majority of reciters are from 11 countries around the
world, namely Germany, United States, Russia, Kazakhstan,
United Kingdom, Netherlands, Spain, Austria, Switzerland,
Senegal and Uzbekistan.
We collected short verses and Duas that Muslims use in
prayer and daily life. The summary found in Table I.
TABLE I: Current audio dataset statistics
Surah
Audios
Females
Males
Unknown
Duration
(min)
Al-Faatihah
2934
1375
1119
440
294
Al-NABAA
30
0
30
0
3
Al-Qadr
132
40
92
0
16
Al-Asr
182
89
52
41
20
Al-Humazah
108
54
40
9
11
Al-Fil
63
34
29
0
6
Quraish
38
19
19
0
4
Al-Maaoon
57
31
26
0
4
Al-Kauthar
183
67
81
35
19
Al-Kafiroon
309
154
79
76
29
An-Nasr
97
50
35
12
11
Al-Masad
112
40
45
27
12
Al-Ikhlas
561
240
218
103
42
Al-Falaq
278
110
110
58
28
An-Nas
557
223
255
79
52
Ayat Ramadan
27
5
20
2
3
Ayat al-Kursi
350
124
169
57
40
At-Tahiyyat
182
102
74
6
20
Subhanaka
91
58
30
3
8
Salawat
84
34
40
10
9
Dua Qunoot
31
3
28
0
2
Adhkar after prayer
70
8
62
0
6
Dua for Protection
30
17
10
3
3
Adhan
322
54
268
0
34
Iqamah Prayer
66
18
48
0
5
Dua from the Quran
6
0
6
0
0
B. Overview of the Annotated Datasets
In the second task, We had 322 participants registered
on Quran Voice platform, 148 attempted to do the training
session, and 71 of them passed the training session and were
ready to participate in the annotating process.
Currently, we have collected 4117 annotations of 1427
recitations made by 62 unique participants, and out of 7000
recitations, we got labels for 1166 recitations, while the rest
261 recitations were waiting for additional judges to get their
labels. The number of occurrences for each label is shown in
Table II.
TABLE II: The number of occurrences for each category
Label
Frequency
Percentage
Correct
396
33.96%
Has mistake
476
40.82%
Incomplete Verse
22
1.89%
Different Verse
53
4.55%
Multiple Verses
78
6.69%
Empty / Not related
141
12.09%
C. Crowd Accuracy
To calculate how well the participants performs while
solving the task we used the Matthews correlation coefficient
(MCC) metric since it is a more reliable statistical rate that
produces a high score only if the prediction obtained good
results in all of the four confusion matrix categories (true
positives, false negatives, true negatives, and false positives).
We have mentioned earlier in III-C that a user is allowed to
participate in solving the task if they pass the entrance exam,
which consists of 8 questions. To pass the entrance exam,
they should score MCC ≥0.6. This number was picked as a
threshold after experiments for the number of mistakes that
annotators can make in the different classes. A participant
will not pass if they make more than one mistake in labeling
Correct or Has Mistakes tasks or make more than two mistakes
in labeling the rest of the labels. Based on the data presented
in the given table III, we can conclude that allowing users to
make three attempts was a suitable number.
TABLE III: The number of attempts for passing the test
Number of attempts
Number of all users
Number of passed
users
1
111
48
2
24
18
3
13
5
By computing the average Matthews Correlation Coefficient
(MCC), Accuracy, and F1 score of individual annotators, the
overall quality of the participants was evaluated. The analysis
yielded an estimated overall quality with an AVG MCC of
0.68, AVG Accuracy of 0.77, and AVG F1score of 0.74.
D. Inter-Rater Agreement
To assess Inter-Rater agreement, we used Krippendorff’s
alpha [20] to analyze 958 labeled tasks with three judges each.
The resulting value of 0.63 indicates Substantial agreement
among the judges. Out of the 958 tasks, 533 were in total
agreement, 42 were in total disagreement, and 383 were
in partial agreement. After examining the tasks with total
disagreement, we observed that some users did not understand
the instructions clearly, leading to confusion between ”Mul-
tiple Verses” and ”Different Verse”, ”Correct” and ”Multiple
Verses”, ”Has mistake” and ” Incomplete Verse”, and ”Has
mistake” and ”Empty / Not related”. We have observed also
that certain audios are not clear or combined between multiple
labels, which highlights the need for a ”Not Clear” label to
address these issues.

--- Page 7 ---

0
200
400
600
800
male
female
(a) Gender Distribution
(b) Reported Age Distribution
(c) Global Distribution
(d) Global Distribution Map
Fig. 6: Demographic Profile of Participants in the Quranic Audio Dataset
To assess the algorithm’s performance in label selection,
a random sample of 50 tasks from the annotated dataset
was selected and labeled by experts. The evaluation yielded
impressive results, with an accuracy of 0.94, an MCC of
0.91, and an F1 score of 0.94. These findings demonstrate the
algorithm’s ability to choose appropriate labels.
To assess the agreement between the labels chosen by the
algorithm and the expert labels, we calculated the inter-rater
agreement. The analysis revealed a substantial agreement with
an inter-rater agreement score of 0.89. This indicates a strong
alignment between the labels assigned by the algorithm and
the expert judgments.
E. Discussion
We have observed that many Muslims are eager to share
their recitations. However, it is not the same as annotating
the recitations. There may be various reasons make Muslims
hesitant to participate in annotating recitation, including:
• Fear of making mistakes in labeling the noble verses.
• Lack of trust in the platform, as it is not supported by an
official religious organization.
• Technological barriers that prevent some users from par-
ticipating.
• Lack of perceived direct value or benefit for them.
Based on our observations in IV-B, we found an inter-rater
agreement of Krippendorff’s alpha = 0.63. This suggests that
not all users may have fully grasped the instructions. The
complexity of the task, with multiple labels to consider, could
have contributed to this outcome. A solution for that could
be to divide this annotation process task into two stages,
one for checking audio validity and the other for checking
audio correctness. Another potential solution is to crowdsource

--- Page 8 ---

the data through learning Quran applications that provide
value to users beyond just crowdsourcing. By incorporating
the crowdsourcing component into a larger and more useful
application, users may be more inclined to participate and
provide accurate data. This approach could also help alleviate
concerns around trust in the platform, as users may be more
likely to trust a platform they are already familiar with and
find useful.
V. CONCLUSION
Learning to recite the Quran can be challenging for many
non-Arabic Muslims around the world, especially those who
do not have access to a tutor. Fortunately, AI technology
can help simplify this process, but it requires a significant
amount of carefully annotated Quranic data. In our work, we
collected around 7,000 Quranic recitations from a pool of 1287
participants from more than 11 different non-Arabic countries.
Additionally, We collected labels for 1166 recitations, with an
inter-rater agreement of 0.63 and crowd accuracy of 0.77. The
evaluation of the used algorithm yielded impressive results,
with an accuracy of 0.91, and an inter-rater agreement of of
0.89.
In future work, we aim to improve both inter-rater agree-
ment and crowd accuracy. We will also incorporate different
levels to identify and classify the exact mistakes made by the
reciters including Tajweed mistakes.
REFERENCES
[1] Al-Ayyoub, Mahmoud, Nour Alhuda Damer, and Ismail Hmeidi. ”Using
deep learning for automatically determining correct application of basic
quranic recitation rules.” Int. Arab J. Inf. Technol. 15, no. 3A (2018):
620-625.
[2] Al-Bakeri, Ahmed AbdulQader, and Abdullah Ahmad Basuhail. ”Asr for
tajweed rules: Integrated with self-learning environments.” International
Journal of Information Engineering and Electronic Business 9, no. 6
(2017): 1.
[3] Bettayeb, Nadjla, and Mhania Guerti. ”Speech synthesis system for the
holy quran recitation.” Int. Arab J. Inf. Technol. 18, no. 1 (2021): 8-15.
[4] Estell´es-Arolas, Enrique, Ra´ul Navarro-Giner, and Fernando Gonz´alez-
Ladr´on-de-Guevara. ”Crowdsourcing fundamentals: definition and typol-
ogy.” Advances in crowdsourcing (2015): 33-48.
[5] Chowdhury, Shammur Absar, Hamdy Mubarak, Ahmed Abdelali, Soon-
gyo Jung, Bernard J. Jansen, and Joni Salminen. ”A multi-platform
Arabic news comment dataset for offensive language detection.” In Pro-
ceedings of the Twelfth Language Resources and Evaluation Conference,
pp. 6203-6212. 2020.
[6] Farra, Noura, Kathleen McKeown, and Nizar Habash. ”Annotating
targets of opinions in Arabic using crowdsourcing.” In Proceedings of
the second workshop on Arabic natural language processing, pp. 89-98.
2015.
[7] Hakouz, Waed, Abdurrahman Ghanem, Samantha Wray, and Ahmed Ali.
”LAHAJET: a Game for Classifiying Dialectal Arabic Speech.” ASRU,
2015.
[8] Kassem, Lin, Caroline Sabty, Nada Sharaf, Menna Bakry, and Slim
Abdennadher. ”tashkeelwap: A game with a purpose for digitizing arabic
diacritics.” (2016).
[9] Bougrine, Soumia, Aicha Chorana, Abdallah Lakhdari, and Hadda
Cherroun. ”Toward a Web-based speech corpus for Algerian dialectal
Arabic varieties.” In Proceedings of the Third Arabic Natural Language
Processing Workshop, pp. 138-146. 2017.
[10] Bougrine, Soumia, Hadda Cherroun, and Ahmed Abdelali. ”Altruistic
crowdsourcing for arabic speech corpus annotation.” Procedia Computer
Science 117 (2017): 137-144.
[11] Zaghouani, Wajdi, and Kais Dukes. ”Can crowdsourcing be used for
effective annotation of Arabic?.” In LREC, pp. 224-228. 2014.
[12] Ardila, Rosana, Megan Branson, Kelly Davis, Michael Henretty, Michael
Kohler, Josh Meyer, Reuben Morais, Lindsay Saunders, Francis M.
Tyers, and Gregor Weber. ”Common voice: A massively-multilingual
speech corpus.” arXiv preprint arXiv:1912.06670 (2019).
[13] El-Sakhawy, Dayna, Slim Abdennadher, and Injy Hamed. ”Collecting
data for automatic speech recognition systems in dialectal arabic using
games with a purpose.” In Multimodal Analyses enabling Artificial
Agents in Human-Machine Interaction: Second International Workshop,
MA3HMI 2014, Held in Conjunction with INTERSPEECH 2014, Sin-
gapore, Singapore, September 14, 2014, Revised Selected Papers 2, pp.
99-108. Springer International Publishing, 2015.
[14] Wray, Samantha, and Ahmed Ali. ”Crowdsource a little to label a lot:
Labeling a speech corpus of dialectal Arabic.” In Sixteenth Annual
Conference of the International Speech Communication Association.
2015.
[15] Abubakar
Abid,
Ali
Abid,
Ali
Abdalla
and
oth-
ers.
”Tarteel
Initiative
White
Paper”.
SCRIBD,
https://www.scribd.com/document/413485204/Tarteel-White-Paper.
2019.
[16] Osman, Hanaa Mohammed, Ban Sharief Mustafa, and Yusra Faisal.
”QDAT: a data set for reciting the Quran.” International Journal on
Islamic Applications in Computer Science And Technology 9, no. 1
(2021): 1-9.
[17] Alobaylani, Ahmed Abdullah, Mohammad Tanvir Parvez, and Suliman
A. Alsuhibany. ”A Database for Speech Processing Based Qur’anic
Recitation Correction.” In 2020 International Conference on Computing
and Information Technology (ICCIT-1441), pp. 1-5. IEEE, 2020.
[18] Sabou, Marta, Kalina Bontcheva, Leon Derczynski, and Arno Scharl.
”Corpus annotation through crowdsourcing: Towards best practice guide-
lines.” In LREC, pp. 859-866. 2014.
[19] Sainburg, Tim, Marvin Thielk, and Timothy Q. Gentner. ”Finding,
visualizing, and quantifying latent structure across diverse animal vocal
repertoires.” PLoS computational biology 16.10 (2020): e1008228.
[20] Krippendorff,
Klaus.
”Computing
Krippendorff’s
alpha-reliability.”
(2011).

```
