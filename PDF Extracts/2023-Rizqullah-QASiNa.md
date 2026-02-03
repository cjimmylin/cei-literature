---
title: "QASiNa - PDF Extract"
source_pdf: "2023-Rizqullah-QASiNa.pdf"
pages: 6
extracted_at: "2026-01-24T17:05:17.177446"
---

# PDF Extract: QASiNa

**Source PDF:** 2023-Rizqullah-QASiNa.pdf
**Total Pages:** 6

---

## Content

```
--- Page 1 ---

QASiNa: Religious Domain Question Answering
using Sirah Nabawiyah
Muhammad Razif Rizqullah1, Ayu Purwarianti1, Alham Fikri Aji2
1School of Electrical Engineering and Informatics
Bandung Institute of Technology. Bandung, Indonesia
razifrizqullah@gmail.com, ayu@stei.itb.ac.id
2Mohamed bin Zayed University of Artificial Intelligence
Abu Dhabi, UAE
alham.fikri@mbzuai.ac.ae
Abstract—Nowadays, Question Answering (QA) tasks receive
significant research focus, particularly with the development of
Large Language Model (LLM) such as Chat GPT [1]. LLM can
be applied to various domains, but it contradicts the principles
of information transmission when applied to the Islamic domain.
In Islam we strictly regulates the sources of information and
who can give interpretations or tafseer for that sources [2].
The approach used by LLM to generate answers based on its
own interpretation is similar to the concept of tafseer, LLM is
neither an Islamic expert nor a human which is not permitted
in Islam. Indonesia is the country with the largest Islamic
believer population in the world [3]. With the high influence of
LLM, we need to make evaluation of LLM in religious domain.
Currently, there is only few religious QA dataset available and
none of them using Sirah Nabawiyah especially in Indonesian
Language. In this paper, we propose the Question Answering
Sirah Nabawiyah (QASiNa) dataset, a novel dataset compiled
from Sirah Nabawiyah literatures in Indonesian language. We
demonstrate our dataset by using mBERT [4], XLM-R [5], and
IndoBERT [6] which fine-tuned with Indonesian translation of
SQuAD v2.0 [7]. XLM-R model returned the best performance
on QASiNa with EM of 61.20, F1-Score of 75.94, and Substring
Match of 70.00. We compare XLM-R performance with Chat
GPT-3.5 and GPT-4 [1]. Both Chat GPT version returned lower
EM and F1-Score with higher Substring Match, the gap of
EM and Substring Match get wider in GPT-4. The experiment
indicate that Chat GPT tends to give excessive interpretations
as evidenced by its higher Substring Match scores compared to
EM and F1-Score, even after providing instruction and context.
This concludes Chat GPT is unsuitable for question answering
task in religious domain especially for Islamic religion.
Index Terms—question answering, low resources, religious
domain, mBERT, XLM-R, IndoBERT, Chat GPT, QASiNa
I. INTRODUCTION
Question answering is a task that closely aligns with every-
day human behavior based on the theory of mind [8]. In daily
human interactions, discussions are conducted to exchange
information, starting with one person providing a statement or
question, followed by response or answer. Currently, question
answering methods have significantly advanced, including
rule-based approaches, extractive language models utilizing
reading comprehension, and Large Language Model (LLM)
with generative approach. These methods are commonly em-
ployed for general question answering problem, but there
Fig. 1. Example of context, question, and answer in QASiNa dataset
is limitations when applied to specific domains such as the
religious domain, especially Islamic religion.
Indonesia is the country with the largest Islamic believer
(moslem) population in the world. According to Annur [3]
on the ”katadata” website, the moslem population is 237.558
million people, 86.7% from total population, based on a
survey conducted by The Royal Islamic Strategic Studies
Centre (RISSC) in 2023. The primary direct references for
moslem are the Holy Qur’an and Sunnah from Book of
Hadith [9]. In addition to these two primary sources, Sirah
Nabawiyah (Prophetic Biography) serves as another important
reference because it contains message, vision, mission, and
historically activities to support both primary references [10].
Sirah Nabawiyah contains comprehensive explanation about
history of Islam from before the birth of Prophet Muhammad
until his passing and the continuation of Islamic preaching.
According to Solahudin [2], interpretation or reasoning
methods in Islamic information sources can be divided
into two types, contextual and textual reasoning. Contextual
reasoning requires extensive and comprehensive knowledge
which requires learning process under supervision of experts,
examination, and scholarly validation. On the other hand, tex-
tual reasoning is a method that involves extracting information
directly from the context without providing interpretation.
With current huge influence of LLM in daily basis, a country
with the largest moslem population will face a problem be-
cause LLM works by giving its own interpretation using next
token prediction. Islamic resource interpretation for public
arXiv:2310.08102v1  [cs.CL]  12 Oct 2023

--- Page 2 ---

audience is called tafseer. Based on tafseer rule in Islam,
tafseer can only be given by a person who specialized at
it [11]. Islamic society need a way to evaluate how far the
interpretation given by LLM. In this paper, we conduct a
research to measure textual reasoning performance of LLM
Chat GPT [1] compared to extractive languages models to
answer religious QA with given context.
Previous research of question answering task in Islamic
domain has utilized information from the Holy Qur’an [12]
[13] [14] [15] [16] [17] [18], Book of Hadith [19] [20], Islamic
fatwa websites [21] [22], with only a few addressing Islamic
history [23]. Most of them are in Arabic language and none
have used literature of the Indonesian Sirah Nabawiyah.
In this research, we propose a new dataset to undertake
the limitation of resources, especially in Indonesian language
and the usage of Sirah Nabawiyah as source of information.
There are three main outcomes of this research: 1) New dataset
consisting of 500 question-answer pairs from 66 different
contexts about Sirah Nabawiyah; 2) Evaluation of the extrac-
tive question answering using language models with transfer
learning; and 3) Evaluate the performance of Chat GPT when
answering extractive question in religious domain.
II. RELATED WORKS
This section presents overview of question answering meth-
ods, datasets, related question answering in religious domain,
and transfer learning technique.
A. Question Answering
The processing of information in computers until the stage
where computers can perform tasks like humans is one of
the goals for successful artificial intelligence [8]. One of
the common information exchange processes performed by
humans is discussion, which is similar to question answering
task. There are several methods that can be used for the
question answering task, namely rule-based, extractive, and
generative.
Based on studies of rule-based question answering [12]
[15] [19] [20], the working principle of rule-based approach
revolves around obtaining answers using predefined patterns.
Extractive method has been conducted in several studies [21]
[13]. The extractive method utilizes context or passage, ques-
tions, and answers, where the answers are obtained from the
context in the form of answer spans. The generative method
which used by LLM [1], differs from extractive methods
because LLM can answer questions with or without context.
The generative model provides answers based on the informa-
tion it has been trained on. In this research we evaluate the
performance of extractive question answering using IndoBERT
[6], XLM-R [5], mBERT [4] and generative model Chat GPT
[1].
B. Religious Domain Question Answering
Research on the religious domain is a sensitive matter
because all of the informations must align with approved
sources by all followers [24]. Therefore, conducting research
on the use of AI in the field of religion, especially Islam, is
both intriguing and challenging. Several previous studies have
been conducted on question answering in the religious domain.
Holy Qur’an used by Abdelnasser et al. [12] to develop
a QA dataset called Al-Bayan in Arabic language. Malhas
et al. [13] examined the Qur’anic Reading Comprehension
Dataset (QRCD) from the Qur’an in Arabic. This study [13]
was an extension of a previous work by Malhas and Elsayed
[14] on Ayatec, a reusable verse-based test QA collection
of Qur’an in Arabic. Alqahtani and Atwell [15] researched
an ontology dataset called the Arabic Quranic Question and
Answer Corpus (AQQAC). Sunnah from Book of Hadith
used by Abdi et al. [19] to explore the use of Sahih al-
Bukhari in Arabic for QA using semantic, word-order, and
sentence similarity. Neamah and Saad [20] investigated the
usage of Sahih al-Bukhari in English for QA, employing
cosine similarity, longest common subsequence, and support
vector machine (SVM). Web resources used by Munshi et al.
[21] for QA of fatwa system, using question-answer data from
Arabic fatwa websites. Mohammed et al. [22] investigated the
English Islamic Article Dataset (EIAD) for Islamic chatbot.
Indonesian translation of Holy Qur’an used by Gusmita et
al. [16] for rule-based question answering for the translation of
the Holy Qur’an, which was later expanded by Sukmana et al.
[17] for the semantic annotated corpus method. The resulting
corpus was then utilized by Putra et al. [18] for semantic
question answering using the inverted index method to search
for answer candidates. Named entity recognition and feature
extraction were employed to obtain the best verse and answer.
Historical literature used by Naf’an et al. [23] to examine
unanswerable question answering using Khulafaa Al-Rashidin
History in the Indonesian language, employing search methods
and answer candidate ranking.
Other than Islamic domain, Zhao and Liu [25] conducted
research about Bible and created a BibleQA based on Bible
trivia questions. Only a small number of QA research on reli-
gious domain exists other than Islamic, because Islam has strict
rules regarding information transmission and interpretation, an
interesting topic to research.
Previous studies in Islamic religion have focused primarily
on the Holy Qur’an, Hadith literature, and website information,
with a small number of research conducted on utilizing histor-
ical material or Sirah Nabawiyah. To tackle the data limitation,
in this research we utilize literature from the Indonesian
language of Sirah Nabawiyah to make a new dataset.
C. Transfer Learning for Low Resources
Developing a model from scratch using data in a specific
domain requires significant time and resources. Therefore,
transfer learning is employed [26]. Transfer learning is a
machine learning technique where a model is trained on a
larger dataset from a more general domain, and then the model
is evaluated on a more specific domain. Previous research on
question answering has utilized transfer learning methods, with
the use of language models such as BERT [27], RoBERTa

--- Page 3 ---

[28], and IndoBERT [29]. The results have shown that transfer
learning can effectively answer questions in specific domains.
In this study, we propose a new dataset focused on infor-
mation from the Sirah Nabawiyah which has low resources of
data. Hence, we employ transfer learning methods for model
training. We utilize mBERT [4], XLM-R [5], and IndoBERT
[6] with transfer learning from Indonesian translation of
SQuAD v2.0 (SQuAD-ID) [7].
III. QUESTION ANSWERING SIRAH NABAWIYAH DATASET
This section presents methods to build the Question An-
swering Sirah Nabawiyah (QASiNa) dataset which is available
to be accessed from public repository1. The process starts
from data acquisition, context retrieval, question and answer
generation, and dataset validation.
A. Data Acquisition
We select the data sources by searching for research litera-
ture on the Sirah Nabawiyah from various campus repositories,
primarily from Islamic universities in Indonesia. The chosen
literature meets specific criteria: 1) It is a valid and reliable
source, proven by its publication through academic mecha-
nisms, and 2) It is publicly accessible, allowing us to share its
content in the form of the QASiNa dataset. In this phase, we
obtained 9 literature sources, as detailed in Table I.
B. Context Retrieval
We select contexts from each literature source and each
context constitutes a complete story containing various facts
within it and manually choose these contexts. Each context
consists of multiple sentences and paragraphs, with the length
ranging from 500 to 2000 characters. At this stage, we
have obtained 66 contexts that will proceed to the question
and answer generation phase. We carefully maintain a wide
diversity of topics covered. We start by providing historical
context, beginning with the history of the Arab region, the
surrounding kingdoms, and their culture before the birth of
Prophet Muhammad SAW. We also include historical context
covering Muhammad SAW’s early years, becoming a Prophet
and building a country, and the period after the Prophet’s
passing.
C. Question and Answer Generation
To make the process of initial question and answer pair
generation faster, we use machine assistance rather than creat-
ing question and answer pairs manually. Similar approach has
been conducted in the past for the creation of dataset Indo-
SQuAD v2.0 [7] using machine translation and IDK-MRC [39]
with the aid of a question generation model. In this study, we
utilized a generative model Chat GPT-3.5 to generate initial
question and answer pairs. We limited the generated results
to 500 question and answer pairs. These question and answer
pairs are not considered valid data as they were generated by
a machine. Therefore, we proceeded to manually validate the
data with the assistance of domain experts.
1https://github.com/rizquuula/QASiNa
TABLE I
SIRAH NABAWIYAH LITERATURE SOURCES
No
Author
Title
1
Bastari [30]
Kontemplasi Politik (Belajar Dari Kisah Perang
Badar Menurut Sirah Ibnu Hisyam Dan Al-
thabari)
(Political Contemplation (Learning from the Story of
the Battle of Badr According to the Sirah of Ibn Hisham
and Al-Thabari))
2
Zakaria [31]
Isra Mi’raj Sebagai Perjalanan Religi: Studi
Analisis Peristiwa Isra Mi’raj Nabi Muhammad
Menurut Al Qur’an Dan Hadits
(Isra Mi’raj as a Religious Journey: An Analytical
Study of the Isra Mi’raj Event of Prophet Muhammad
According to the Qur’an and Hadiths)
3
Salahuddin
[32]
Isra’Mi’raj studi analisis sejarah dalam pen-
didikan islam
(Isra’ Mi’raj is a study of historical analysis in Islamic
education)
4
Mubarok
[33]
Sejarah Sosial-Politik Arab: Dari Hegemoni
Romawi-Persia Hingga Kebangkitan Arab Islam
(Arab Social-Political History: From Roman-Persian
Hegemony to the Rise of Arab Islam)
5
Izzani
and
Rubini [34]
Pendidikan
Karakter
dalam
Buku
Sirah
Nabawiyah
Karya
Syaikh
Shafiyyurrahman
al-Mubarakfuri
(Character Education in the Book of the Prophet’s
Biography by Sheikh Shafiyyurrahman al-Mubarakfuri)
6
Hasbillah
[35]
Sirah Nabawiyah dan Demitologisasi Kehidupan
Nabi
(Prophetic Biography and Demythologization of the
Prophet’s Life)
7
Fuad [36]
Sejarah peradaban Islam
(History of Islamic Civilization)
8
Thabrani
[37]
Tata kelola pemerintahan negara madinah pada
masa nabi Muhammad saw
(The governance system of the Madinah state during
the time of Prophet Muhammad (peace be upon him).)
9
Sairazi [38]
Kondisi Geografis, Sosial Politik, dan Hukum Di
Makkah dan Madinah Pada Masa Awal Islam
(Geographical, Social, Political, and Legal Conditions
in Mecca and Medina during the Early Period of Islam)
D. Dataset Validation
We employ domain experts to validate the context, question,
and answer pairs generated by the machine. To ensure the
quality of the validation process, each expert must meet the
following criteria: 1) Expert is islamic believer; 2) Possess
proficiency in the Indonesian language with good grammar
and vocabulary; 3) Have done intensive study of Islamic
knowledge, either formally and informally for a minimum of
two years; and 4) Demonstrate a comprehensive understanding
of context in Sirah Nabawiyah.
We use some steps in dataset validation including consis-
tency testing of validator performance by doing cross vali-
dation as shown in Fig. 2. The validation process begins by
dividing 500 context-question-answer pairs into five different
dataset parts (A, B, C, D, and E), each part containing the
same number of data. These dataset parts are then duplicated
(F, G, H, I, and J). Each original has the same content with
corresponding duplicate: A with F, B with G, C with H, D with
I, and E with J. Each expert validates one original data and one
duplicated data with different content. This approach facilitates
cross-validation to maintain consistency in the dataset.
Validation process assisted by five experts, each validator
does their task in one week. Once all of the data has been

--- Page 4 ---

Fig. 2. Dataset validation diagram
validated by the experts, we proceed to evaluate the data
checking the answer similarity. We compare the validation
result, fixed small typo by ourselves, 4.2% of the data have non
similar answer, we use discussion mechanisms with related
experts to determine the correct answer. The final outcome of
this process is a set of 500 context-question-answer pairs that
have been validated by the experts.
E. Dataset Content
The final result of QASiNa dataset is a JSON array file,
containing 66 data based on context, example of data is
shown on Fig. 1. Each context has attributes context_id,
context, question_answers, and context_length.
The context length is the number of characters in context,
ranges from minimum of 713 to maximum of 1999, with mean
of 1629.5 and median of 1689.5. Within each context data,
there are several question-answer pairs, which each question-
answer pair has attributes type, question, answer, and
answer_start. There are five types of questions: what,
when, where, who, and how many, with the distribution of
question types shown in Table II.
IV. EVALUATION
We evaluate the dataset using the transfer learning approach
with mBERT, XLM-R, and IndoBERT with also test the
Chat GPT-3.5 and GPT-4. The evaluation metrics used in this
evaluation are Exact Match (EM), F1-Score, and Substring
Match evaluation. We choose the Substring Match evaluation
to assess the interpretations made by Chat GPT. Substring
TABLE II
NUMBER OF DATA BASED ON QUESTION TYPE
Question Type
Number of Data
who
226
what
178
how many
38
where
38
when
20
total
500
TABLE III
EVALUATION RESULTS USING LANGUAGE MODEL
Model
Dataset
Evaluation Metrics
EM
F1-
Score
Substring
Match
IndoBERT [6]
indobert-base-p1
(124.5M)
SQuAD-ID
39.53
59.20
54.48
500 SQuAD-ID
37.00
57.65
53.40
QASiNa
42.40
57.77
49.00
XLM-R [5]
xlm-roberta-base
(279M)
SQuAD-ID
45.29
64.53
59.51
500 SQuAD-ID
42.80
63.87
58.20
QASiNa
61.20
75.94
70.00
mBERT [4]
bert-base-
multilingual-cased
(179M)
SQuAD-ID
43.62
62.33
56.97
500 SQuAD-ID
41.00
60.94
54.80
QASiNa
58.40
71.76
64.60
Match metric assigns a True value if the label is a substring
of the generated answer and otherwise is False.
A. Transfer Learning
We chose mBERT [4], XLM-R [5], and IndoBERT [6] for
extractive question answering tasks in Indonesian Language.
The tools used are 16 GB Kaggle GPU P100, Huggingface
Trainer
with
AutoModelForQuestionAnswering
and WandB for monitoring. To fine-tune the selected language
models, we use tokenized context and question using each lan-
guage model tokenizer as input, then the label is answer token
position in the context. We use training data from Indonesian
translation of SQuAD v2.0 (SQuAD-ID) [7] and conducted
grid search hyperparameters tuning, the used parameters are
learning rate of 2e-5 and 2e-6, batch sizes of 8 and 16, weight
decay of 0.01, and 5 epochs. The best fine-tuned model from
each language model is selected by the highest EM score.
We evaluate fine-tuned mBERT, XLM-R, and IndoBERT
with SQuAD-ID test set and QASiNa dataset. In addition, we
also conducted comparative testing by randomly sampling an
equal number of 500 data from the SQuAD-ID test set with
random_state=0, namely 500 SQuAD-ID. The evaluation
results of the fine-tuned model are presented in Table III.
The best model selected based on the highest EM score,
as in the religious domain, precise answers without any
interpretation or excessive information are prioritized. We use
scaling from 0 to 100 for the evaluation metrics.
The XLM-R model outperforms other models for the
QASiNa dataset, achieving an EM score of 61.20, which is

--- Page 5 ---

TABLE IV
EVALUATION METRICS FOR EACH QUESTION TYPE USING XLM-R
Question Type
Evaluation Metrics
EM
F1-Score
Substring
Match
who
65.49
78.37
73.45
what
58.43
72.52
69.10
where
55.26
75.16
65.79
how many
57.89
76.38
60.53
when
55.00
79.60
65.00
2.80 points higher than mBERT and 18.80 points higher than
IndoBERT. The F1-score and Substring Match also indicate
that the XLM-R model yields the highest score on both.
From each language model, we can see that the F1-Score
values are lower than the Substring Match values, indicating
that interpretation performed by the language model is low.
This F1-score and Substring Match comparison will be further
analyzed using Chat GPT-3.5 and GPT-4 in Subsection IV-B.
We use XLM-R to evaluate QASiNa dataset based on
available question types. From the experiments in Table IV,
we can see that the EM scores range from the lowest for the
”when” question type at 55.00 to the highest for the ”who”
question type at 65.49. The difference between the highest and
lowest values for each evaluation metric is 10.49 for EM, 7.08
for F1-Score, and 12.93 for Substring Match. The difference
range of the scores are not excessively high, indicating data
for each question type is good.
B. Generative Model with Chat GPT
The utilization of ChatGPT continues to grow across a wide
range of domains, including the religious domain. One of
the objectives of QASiNa is to assess ChatGPT’s reasoning
capabilities for questions within the context of the Sirah
Nabawiyah, in the task of extractive question answering. The
outcomes of this evaluation will be compared with the abilities
of language models that were evaluated in the Subsection
IV-A. We conduct testing on the ability of Chat GPT using
API gpt-3.5-turbo and gpt-4 to answer questions with
given context in extractive way. Our ChatGPT prompt consists
of instruction, context, and question, so the Chat GPT will
return the answer as given instruction. We use Python 3 to
call Chat GPT API with prompt as the following code.
def build prompt( context , question ):
return f”””{context}
Berdasarkan konteks pada konteks yang diberikan sebelumnya, berikan jawaban
dengan tipe
ekstraktif
tentang pertanyaan berikut . Kata−kata pada
jawaban hanya boleh diambil dari konteks yang diberikan . Jawaban dibuat
singkat dan tidak boleh ada penjelasan .
{question}
”””
Table V is complete results of the evaluation using Chat
GPT and the comparison with XLM-R. Due to the lim-
ited resources we didn’t evaluate using all of the SQuAD-
TABLE V
CHAT GPT EVALUATION RESULTS
Model
Dataset
Evaluation Metrics
EM
F1-Score
Substring
Match
XLM-R
(279M)
500 SQuAD-ID
42.80
63.87
58.20
QASiNa
61.20
75.94
70.00
ChatGPT-3.5
(gpt-3.5-turbo)
500 SQuAD-ID
11.60
37.86
51.00
QASiNa
30.20
58.92
83.20
ChatGPT-4
(gpt-4)
500 SQuAD-ID
4.20
30.61
61.80
QASiNa
4.60
37.36
93.60
ID dataset, we use sampled 500 SQuAD-ID and QASiNa
dataset in this experiment. We can observe that for both
Chat GPT-3.5 and GPT-4, the EM and F1-score are lower
than Substring Match, which means there are many other
words present besides the actual answer. This concludes that
providing extractive instructions is not sufficient to make the
generative LLM produce extractive answers. Chat GPT intends
to do excessive interpretations, while interpretation within the
context of religious domains by the AI is prohibited. This
experiment lead us to the conclusion that current Chat GPT
(gpt-3.5-turbo and gpt-4) is not suitable for finding extractive
answers for questions related to religious domain.
V. CONCLUSION AND FUTURE WORKS
We create a new dataset named Question Answering Sirah
Nabawiyah (QASiNa) dataset, which employs a previously
unexplored domain, Sirah Nabawiyah in the Indonesian lan-
guage. To evaluate the language models, we conducted testing
using the transfer learning approach for language models with
mBERT [4], XLM-R [5], and IndoBERT [6]. We also evaluate
the performance of LLM Chat GPT (gpt-3.5-turbo and gpt-4)
[1] to solve QASiNa dataset.
By using three language models with data from SQuAD-ID
[7], randomly sampled 500 SQuAD-ID and QASiNa dataset
concludes XLM-R as the best model. We also evaluated
Chat GPT-3.5 and GPT-4 by providing instruction prompt for
extractive answers based on the given context. The conclusion
drawn from this evaluation was that the EM and F1-scores of
Chat GPT are lower compared to XLM-R, on the other side
Chat GPT has high Substring Match score. This experiment
concludes that Chat GPT tends to provide excessive interpre-
tations even after providing the context of question.
Research on question answering in the religious domain
remains relatively rare, making it an intriguing field, especially
in the current LLM’s competitions. Conducting QA research
in the religious domain highlights the presence of a domain-
specific set of issues that needs further attention, especially
when the religious domain has strict rule about giving in-
terpretation. This emphasizes the need for technological ad-
vancements to ensure the preservation of the values held by
religious community. Further studies to advance this research
could involve increasing the dataset size and variations of

--- Page 6 ---

LLM to be analyzed. Furthermore, we can do research about
way to make LLM better at answering religious QA, methods
like In Context Learning and context-based token filtering are
interesting topics. Finally, we intend to make the proposed
QASiNa dataset publicly available to the research community.
ACKNOWLEDGMENT
The authors thank the Indonesia Endowment Fund for
Education (LPDP) for funding this research. We also thank
to the domain experts who have assisted in validating the
datasets.
REFERENCES
[1] OpenAI, “Chatgpt,” 2023. [Online]. Available: https://chat.openai.com
[2] M. Solahudin, “Pendekatan tekstual dan kontekstual dalam penafsiran
alquran,” Al-Bayan: Jurnal Studi Ilmu Al-Qur’an dan Tafsir, vol. 1, no. 2,
pp. 115–130, 2016.
[3] C. M. Annur, “Ini jumlah populasi muslim di kawasan asean, indonesia
terbanyak,” https://databoks.katadata.co.id/datapublish/2023/03/28/ini-
jumlah-populasi-muslim-di-kawasan-asean-indonesia-terbanyak, 2023.
[4] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “Bert: Pre-training
of deep bidirectional transformers for language understanding,” arXiv
preprint arXiv:1810.04805, 2018.
[5] A. Conneau, K. Khandelwal, N. Goyal, V. Chaudhary, G. Wenzek,
F. Guzm´an, E. Grave, M. Ott, L. Zettlemoyer, and V. Stoyanov, “Unsu-
pervised cross-lingual representation learning at scale,” arXiv preprint
arXiv:1911.02116, 2019.
[6] F. Koto, A. Rahimi, J. H. Lau, and T. Baldwin, “Indolem and indobert: A
benchmark dataset and pre-trained language model for indonesian nlp,”
arXiv preprint arXiv:2011.00677, 2020.
[7] F. J. Muis and A. Purwarianti, “Sequence-to-sequence learning for
indonesian automatic question generator,” in 2020 7th International
Conference on Advance Informatics: Concepts, Theory and Applications
(ICAICTA).
IEEE, 2020, pp. 1–6.
[8] A. Nematzadeh, K. Burns, E. Grant, A. Gopnik, and T. L. Griffiths,
“Evaluating theory of mind in question answering,” arXiv preprint
arXiv:1808.09352, 2018.
[9] S. A. F. Jaya, “Al-qur’an dan hadis sebagai sumber hukum islam,” Jurnal
Indo-Islamika, vol. 9, no. 2, pp. 204–216, 2019.
[10] S. S. Al-Mubarakfuri, Sirah nabawiyah.
Pustaka Al Kautsar, 2012.
[11] L. A. Mutalib, W. A. F. W. Ismail, A. S. Baharuddin, M. F. Mohamed,
K. Wafa et al., “Scientific exegesis of al-quran and its relevance in
dealing with contemporary issues: An appraisal on the book of ‘al-
jawahir fi tafsir al-quran al-karim,” International Journal of Recent
Technology and Engineering, 2019.
[12] H. Abdelnasser, M. Ragab, R. Mohamed, A. Mohamed, B. Farouk,
N. M. El-Makky, and M. Torki, “Al-bayan: an arabic question answering
system for the holy quran,” in Proceedings of the EMNLP 2014
Workshop on Arabic Natural Language Processing (ANLP), 2014, pp.
57–64.
[13] R. Malhas, W. Mansour, and T. Elsayed, “Qur’an qa 2022: Overview
of the first shared task on question answering over the holy qur’an,” in
Proceedinsg of the 5th Workshop on Open-Source Arabic Corpora and
Processing Tools with Shared Tasks on Qur’an QA and Fine-Grained
Hate Speech Detection, 2022, pp. 79–87.
[14] R. Malhas and T. Elsayed, “Ayatec: building a reusable verse-based
test collection for arabic question answering on the holy qur’an,”
ACM Transactions on Asian and Low-Resource Language Information
Processing (TALLIP), vol. 19, no. 6, pp. 1–21, 2020.
[15] M. Alqahtani and E. Atwell, “Annotated corpus of arabic al-quran
question and answer,” Archive of University of Leeds, 2018.
[16] R. H. Gusmita, Y. Durachman, S. Harun, A. F. Firmansyah, H. T.
Sukmana, and A. Suhaimi, “A rule-based question answering system
on relevant documents of indonesian quran translation,” in 2014 Inter-
national Conference on Cyber and IT Service Management (CITSM).
IEEE, 2014, pp. 104–107.
[17] H. T. Sukmana, R. H. Gusminta, Y. Durachman, and A. F. Firmansyah,
“Semantically annotated corpus model of indonesian translation of
quran: An effort in increasing question answering system performance,”
in 2016 4th International Conference on Cyber and IT Service Manage-
ment.
IEEE, 2016, pp. 1–5.
[18] S. J. Putra, R. H. Gusmita, K. Hulliyah, and H. T. Sukmana, “A semantic-
based question answering system for indonesian translation of quran,”
in Proceedings of the 18th International Conference on Information
Integration and Web-based Applications and Services, 2016, pp. 504–
507.
[19] A. Abdi, S. Hasan, M. Arshi, S. M. Shamsuddin, and N. Idris, “A ques-
tion answering system in hadith using linguistic knowledge,” Computer
Speech & Language, vol. 60, p. 101023, 2020.
[20] N. NEAMAH and S. SAAD, “Question answering system supporting
vector machine method for hadith domain.” Journal of Theoretical &
Applied Information Technology, vol. 95, no. 7, 2017.
[21] A. A. Munshi, W. H. AlSabban, A. T. Farag, O. E. Rakha, A. A.
AlSallab, and M. Alotaibi, “Towards an automated islamic fatwa system:
Survey, dataset and benchmarks,” International Journal of Computer
Science and Mobile Computing, vol. 10, no. 4, pp. 118–131, 2021.
[22] M. Mohammed, S. Amin, and M. M. Aref, “An english islamic articles
dataset (eiad) for developing an islambot question answering chatbot,”
in 2022 5th International Conference on Computing and Informatics
(ICCI).
IEEE, 2022, pp. 303–309.
[23] M. Z. Naf’An, D. E. Mahmudah, S. J. Putra, and A. F. Firmansyah,
“Eliminating unanswered questions from question answering system
for khulafaa al-rashidin history,” in 2016 6th International Conference
on Information and Communication Technology for The Muslim World
(ICT4M).
IEEE, 2016, pp. 140–143.
[24] C. Vieten, S. Scammell, A. Pierce, R. Pilato, I. Ammondson, K. I.
Pargament, and D. Lukoff, “Competencies for psychologists in the
domains of religion and spirituality.” Spirituality in Clinical Practice,
vol. 3, no. 2, p. 92, 2016.
[25] H. J. Zhao and J. Liu, “Finding answers from the word of god: Domain
adaptation for neural networks in biblical question answering,” in 2018
International Joint Conference on Neural Networks (IJCNN).
IEEE,
2018, pp. 1–8.
[26] L. Torrey and J. Shavlik, “Transfer learning,” in Handbook of research
on machine learning applications and trends: algorithms, methods, and
techniques.
IGI global, 2010, pp. 242–264.
[27] K. Duan, S. Du, Y. Zhang, Y. Lin, H. Wu, and Q. Zhang, “Enhancement
of question answering system accuracy via transfer learning and bert,”
Applied Sciences, vol. 12, no. 22, p. 11522, 2022.
[28] S. Bachina, S. Balumuri, and S. Kamath, “Ensemble albert and roberta
for span prediction in question answering,” in Proceedings of the
1st Workshop on Document-grounded Dialogue and Conversational
Question Answering (DialDoc 2021), 2021, pp. 63–68.
[29] M. I. Rahajeng and A. Purwarianti, “Indonesian question answering
system for factoid questions using face beauty products knowledge
graph,” Jurnal Linguistik Komputasional, vol. 4, no. 2, pp. 59–63, 2021.
[30] A. Bastari, “Kontemplasi politik (belajar dari kisah perang badar menu-
rut sirah ibnu hisyam dan al-thabari),” Jurnal Tapis: Jurnal Teropong
Aspirasi Politik Islam, vol. 9, no. 1, pp. 16–30, 2013.
[31] A. Zakaria, “Isra mi’raj sebagai perjalanan religi: Studi analisis peristiwa
isra mi’raj nabi muhammad menurut al qur’an dan hadits,” Al-Tadabbur:
Jurnal Ilmu Al-Qur’an dan Tafsir, vol. 4, no. 01, pp. 99–112, 2019.
[32] S. Salahuddin, “Isra’mi’raj studi analisis sejarah dalam pendidikan
islam,” Jurnal Ilmiah Pendidikan Anak (JIPA), vol. 2, no. 3, 2017.
[33] A. A. Mubarok, “Sejarah sosial-politik arab: Dari hegemoni romawi-
persia hingga kebangkitan arab islam,” NALAR: Jurnal Peradaban dan
Pemikiran Islam, vol. 4, no. 1, pp. 64–76, 2020.
[34] R. Izzani and R. Rubini, “Pendidikan karakter dalam buku sirah
nabawiyah karya syaikh shafiyyurrahman al-mubarakfuri,” AL-MANAR:
Jurnal Komunikasi dan Pendidikan Islam, vol. 10, no. 1, pp. 103–114,
2021.
[35] A. Hasbillah, “Sirah nabawiyah dan demitologisasi kehidupan nabi,”
Quran and Hadith Studies, vol. 1, no. 2, p. 251, 2012.
[36] A. Z. Fuad, “sejarah peradaban islam,” 2014.
[37] A. M. Thabrani, “Tata kelola pemerintahan negara madinah pada masa
nabi muhammad saw,” IN RIGHT: Jurnal Agama dan Hak Azazi
Manusia, vol. 4, no. 1, 2014.
[38] A. H. Sairazi, “Kondisi geografis, sosial politik, dan hukum di makkah
dan madinah pada masa awal islam,” Journal of Islamic and Law Studies,
vol. 3, no. 1, pp. 119–146, 2019.
[39] R. A. Putri and A. Oh, “Idk-mrc: Unanswerable questions for indonesian
machine reading comprehension,” arXiv preprint arXiv:2210.13778,
2022.

```
