---
title: "2023-Shalumov-HeRo RoBERTa and Longformer Hebrew Language Models - PDF Extract"
source_pdf: "2023-Shalumov-HeRo RoBERTa and Longformer Hebrew Language Models.pdf"
pages: 8
extracted_at: "2026-02-13T09:50:27.882664"
---

# PDF Extract: 2023-Shalumov-HeRo RoBERTa and Longformer Hebrew Language Models

**Source PDF:** 2023-Shalumov-HeRo RoBERTa and Longformer Hebrew Language Models.pdf
**Total Pages:** 8

---

## Content

```
--- Page 1 ---

HeRo: RoBERTa and Longformer Hebrew Language Models
Vitaly Shalumov∗
vitaly.shalumov@gmail.com
Harel Haskey∗
harelnh@gmail.com
April 18, 2023
Abstract
In this paper, we fill in an existing gap in re-
sources available to the Hebrew NLP com-
munity by providing it with the largest so
far pre-train dataset HeDC4, a state-of-
the-art pre-trained language model HeRo
for standard length inputs and an eﬀicient
transformer LongHeRo for long input se-
quences. The HeRo model was evaluated
on the sentiment analysis, the named en-
tity recognition, and the question answer-
ing tasks while the LongHeRo model was
evaluated on the document classification
task with a dataset composed of long doc-
uments.
Both HeRo and LongHeRo pre-
sented state-of-the-art performance.
The
dataset and model checkpoints used in this
work are publicly available1 .
1
Introduction
Hebrew NLP research has gained a huge
boost with the introduction of a multi-lingual
encoder-only
transformer
model
mBERT,
based on the BERT architecture (Devlin et al.,
2018). Following mBERT, several other mod-
els were released, among them are the mono-
lingual models HeBERT (Chriqui and Yahav,
2021) and AlephBERT (Seker et al., 2021).
The AlephBERT model is considered state-of-
the-art (SOTA) for Hebrew pre-trained lan-
guage models (PLMs). Shortly before the re-
lease of our paper, a new model named Ale-
phBERTGimmel (Guetta et al., 2022) was re-
leased with a two and a half times larger
vocabulary size than the AlephBERT model.
This model has passed AlephBERT on sev-
eral downstream tasks and we will address this
model (the ”base” version which exhibited the
best results) if applicable.
∗Equal contribution.
1The
resources
are
available
at
the
hugging-
face
hub
under
the
names
HeNLP/HeRo,
HeNLP/LongHeRo, and HeNLP/HeDC4.
While those models provided a means for
performing NLP tasks for standard length in-
puts (up to 512 tokens), the problem of deal-
ing with long input sequences (larger than
512 tokens) was left untouched. Theoretically,
there is no limitation of using the aforemen-
tioned models for long documents. However,
the dense attention approach adopted in those
models suffers from the fact that the computa-
tional complexity of a vanilla transformer ar-
chitecture grows quadratically with the length
of the input.
In recent years, eﬀicient transformers which
leverage the sparse attention approach were
suggested, aiming at dealing with large input
sequences. Among them are the Longformer
(Beltagy et al., 2020) and the BigBird (Zaheer
et al., 2020) models.
Both models initiated
their weights using the pre-trained RoBERTa
model (Liu et al., 2019).
The Longformer
model for the English language was trained on
the Books dataset (Zhu et al., 2015) with a
combination of Wikipedia, Realnews (Zellers
et al., 2019) with larger than 1200 tokens in-
puts and a third of the Stories dataset (Trinh
and Le, 2018). Similarly, BigBird model for
the English language used CC-News (Guu
et al., 2020) combined with Books and Stories.
In this paper, the Longformer architecture was
chosen.
In the scope of pre-training data, the previ-
ous SOTA model (AlephBERT) used mainly
the OSCAR 2019 (Suárez et al., 2020) line-
based multi-lingual pre-train dataset. In 2021,
following the paper on the sequence to se-
quence multi-lingual model mT5 (Xue et al.,
2020), the mC4 corpora which includes the He-
brew language was released. In 2022, the OS-
CAR 22.01 (Abadji et al., 2022) multi-lingual
document-based dataset was released which is
more suitable for pre-training large language

--- Page 2 ---

models then the 2019 version. One of the main
changes from the 2019 version is the utilization
of line filtering intended to limit the integrity
destruction of the documents, keeping contigu-
ous lines and making documents more human
readable and exploitable as documents.
In terms of quality of the pre-train dataset,
the authors of (Lee et al., 2021) highlighted
the importance of deduplication and suggested
two approaches for deduplication - exact and
approximate. In this paper, we adopt the Ap-
proximate Matching deduplication method us-
ing MinHash which is more suitable for docu-
ments. (Broder, 1997).
We followed the methodology introduced in
(Beltagy et al., 2020) and trained a Long-
former model for the Hebrew language from
a RoBERTa checkpoint. No RoBERTa model
for the Hebrew language existed at the time
of writing this paper. In addition, we wanted
to test the effect of the HeDC4 dataset on
the performance of a standard input language
model, thus we trained a SOTA Hebrew lan-
guage model for standard length inputs using
the RoBERTa architecture.
The models for
standard and long inputs are named HeRo and
LongHeRo respectively.
This work introduces the following contribu-
tions:
• Synthesizing a thoroughly cleaned and
approximately
deduplicated
dataset
HeDC4
for
unsupervised
learning,
two and a half times larger than was
previously used in the literature.
• Achieving SOTA results on several He-
brew NLP tasks for a standard input
length of 512 tokens using the HeRo
model.
• Introducing
and
evaluating
the
LongHeRo language model for long
documents in Hebrew.
• Publicly releasing the curated dataset
HeDC4,
the
HeRo
Hebrew
language
model for standard length inputs and the
LongHeRo Hebrew language model for
long documents.
2
Pre-train
2.1
Pre-train Dataset
Both HeBERT and AlephBERT utilized the
deduplicated split of the OSCAR 2019 dataset
as the main source of pre-train data. Both also
included the Hebrew Wikipedia. In addition,
the authors of AlephBERT included a twitter-
based dataset.
Due to the fact that the main objective of
this research was to train a model for long in-
put sequences, we aimed at curating a dataset
that has a large amount of long documents
(larger than 512 tokens). Thus, we combined
the mC4 and the OSCAR 22.01 datasets for
pre-training.
The mC4 and OSCAR 22.01
datasets are not deduplicated, thus we used
the Approximate Matching deduplication to
filter duplicate documents within each dataset
and between the two datasets.
Following the guidelines from (Sarti and Nis-
sim, 2022), we also added a cleaning stage to
our dataset pre-processing procedure with the
exception of retaining long documents. After
deduplication and cleaning, we achieved a two
and a half times larger dataset than the one
used in AlephBERT training, making it the
most extensive publicly available Hebrew cor-
pus to this date. The dataset is composed of
about 30% long documents. Tab. 1 presents
the details of the curated dataset, which we
name Hebrew Deduplicated and Cleaned Com-
mon Crawl Corpus (HeDC4).
2.2
Pre-training HeRo
We began by constructing a BPE tokenizer
(Sennrich et al., 2015) with a vocabulary size of
50,265 tokens using the HeDC4 dataset. The
model was trained in two stages: in the first
stage the model was trained on four NVIDIA
GeForce GTX 1080 Ti 12GB GPUs for 35 days.
The checkpoint was then saved for LongHeRo
initialization. The second stage of training was
identical to the first. Each stage started with
the learning rate of 1e-4 with linear decay and
the AdamW optimizer (Loshchilov and Hutter,
2017).
2.3
Pre-training LongHeRo
We initiated the LongHeRo model using the
weights taken from the HeRo model at the
end of the first training stage. The LongHeRo

--- Page 3 ---

Table 1: The size of the pre-train dataset after each pre-processing stage. Previous largest corpora has
been reported in (Seker et al., 2021) as 17.9GB file size and 1.9B words.
Corpus
File Size
Documents
Words
Hebrew mC4
74 GB
12.3M
7.2B
Hebrew OSCAR 22.01
30.3GB
3.1M
2.2B
Hebrew deduplicated mC4 and OSCAR 22.01
57.1GB
9.5M
5.6B
HeDC4 (deduplicated and cleaned)
47.5GB
8.5M
4.7B
model was then trained for 2 epochs using the
learning rate of 3e-5 with linear decay and the
AdamW optimizer. The model was trained on
a NVIDIA Quadro RTX 6000 48GB GPU for
33 days.
3
Downstream Tasks
To
facilitate
comparability
with
previous
works, we retain the terminology morph-based
evaluation which refers to pre-processing the
input by using morphological segmentation.
The token-based phrase references evaluation
without morphological segmentation. The per-
formance of the models in this paper is re-
ported for the token-based segmentation.
3.1
HeRo Downstream Tasks
We focus on comparing our model to the cur-
rent SOTA as presented in (Seker et al., 2021).
For this purpose, we evaluate our model on
three NLP tasks:
sentiment analysis (SA),
named entity recognition (NER), and question
answering (QA).
3.1.1
Sentiment Analysis
The HeRo model was evaluated on the sen-
timent analysis dataset presented in (Amram
et al., 2018) which is based on 12K social me-
dia comments.
The comments were written
in response to oﬀicial Facebook posts posted
by the former Israeli president, Mr. Reuven
Rivlin, between June and August, 2014. The
comments were annotated with the following
labels - supportive (positive), criticizing (neg-
ative), or off-topic (neutral).
As stated in
(Seker et al., 2021), the original variant of the
dataset had a significant data leakage between
the splits, with duplicates in the data samples.
Thus, the task was evaluated on the dedupli-
cated dataset2 which contains 8,465 samples.
2The dataset was taken from https://github.com
/omilab/Neural-Sentiment-Analyzer-for-Modern-
Hebrew
The dataset will be henceforth referenced as
SMCD (social media comments deduplicated).
3.1.2
Named Entity Recognition
Two NER datasets were established as the
benchmark for the Hebrew NER task.
The
first is the BMC corpus (Mordecai and El-
hadad, 2005) which contains 3,294 sentences
(4,600 entities) and has seven different entity
categories.
The second is the Named Entities and
MOrphology (NEMO) corpus presented in
(Bareket and Tsarfaty, 2021). The NEMO cor-
pus has nine categories and contains 6,220 sen-
tences (7,713 entities).
3.1.3
Question Answering
We evaluate our model on the ParaShoot
dataset (Keren and Levy, 2021) composed of
3,038 annotated examples with SQuAD for-
mat.
3.2
LongHeRo Classification Task
While there are numeral benchmarks for the
evaluation of Hebrew language models with
standard length inputs, no labeled data ex-
isted for an evaluation of a long input Hebrew
language model. Thus, we turned to creating
a labeled dataset for specifically that purpose.
We chose to translate the Hyperpartisan
news detection dataset (Kiesel et al., 2019) on
which the English version of both RoBERTa
and Longformer models were evaluated. This
choice enabled us to compare not only the per-
formance of HeRo to that of LongHeRo, but
also served as a sanity check in comparing the
Hebrew based models to their English coun-
terparts. We chose machine translation under
the assumption that the generated translation
is of suﬀicient quality for the preservation of
the document class.
As stated in (Beltagy et al., 2020), docu-
ments in the Hyperpartisan dataset are rel-

--- Page 4 ---

atively long and the dataset is small with
only 645 documents making it a good test for
LongHeRo’s ability to adapt to limited data.
Translating with Helsinki and NLLB mod-
els introduced in (Tiedemann and Thottin-
gal, 2020) and (Costa-jussà et al., 2022) re-
spectively, proved to be diﬀicult with an off-
the-shelf inference approach.
While most of
the translated text appeared coherent, some
phrases caused the model to repeat a certain
translated sequence several times. Thus, the
Google Translate tool3 was eventually chosen
to translate the Hyperpartisan dataset from
English to Hebrew. We validated manually a
subset of the dataset for quality control.
4
Core Results
4.1
HeRo Results
We fine-tuned the model for 25 epochs with the
default Huggingface (Wolf et al., 2020) param-
eters. The results for the sentiment analysis
task are given in Tab. 2.
Table 2: Token-based SA accuracy results on the
SMCD corpus. Previous SOTA has been reported
by the AlephBERTGimmel model (Guetta et al.,
2022).
Model
SMCD
AlephBERT
89.02
Previous SOTA (AlephBERTGimmel)
89.51
HeRo
89.56
To the best of our knowledge, the NER
dataset on which the AlephBERTGimmel
model was evaluated was not released at the
time of writing this paper, thus we chose to
evaluate this model on the datasets NEMO
and BMC using the released checkpoint. The
results for the NER task are given in Tab. 3.
Table 3: Token-based NER F1 results on NEMO
and BMC datasets. Previous SOTA on both cor-
pora has been reported by the AlephBERT model
(Seker et al., 2021).
Model
NEMO
BMC
Previous SOTA on BMC (AlephBERT)
84.91
91.12
Previous SOTA on NEMO (AlephBERTGimmel)
86.76
91.11
HeRo
86.79
93.56
The HeRo model presents similar perfor-
mance to the AlephBERTGimmel model on
3https://translate.google.com/
SA and NER (NEMO) and outperforms it on
NER (BMC). It is interesting to note that
this level of performance is accomplished with
a much smaller model (AlephBERTGimmel
has 50% more parameters then than HeRo
due to the increased vocabulary: AlephBERT-
Gimmel - 184M parameters; HeRo and Aleph-
BERT: roughly the same size of 125M param-
eters). This fact is attributed to the two and a
half times larger corpus (HeDC4) introduced
in this paper.
The results for the QA task are given in
Tab.
4.
On the QA task the HeRo model
outperforms both the AlephBERT model and
the multi-lingual mBERT model.
Table 4: QA F1 results on the ParaShoot corpus.
The results are compared to other models based
on (Keren and Levy, 2021). Previous SOTA has
been reported by the mBERT model (Devlin et al.,
2018).
Model
F1
Exact Match
Previous SOTA (mBERT)
56.1
32.0
AlephBERT
49.6
26.0
HeRo
58.2
34.8
With respect to dataset diversity, we’ve
experimented with adding several gigabytes
of tweeter-based documents to the HeDC4
dataset. This addition had little effect on per-
formance and was thus discarded.
4.2
LongHeRo Classification
We fine-tuned the HeRo and LongHeRo mod-
els for 15 epochs with the default Huggingface
(Wolf et al., 2020) parameters. The results rep-
resent a mean of F1 scores on three random
80/20 splits. The results for the classification
task are given in Tab. 5.
Table 5: Token-based classification F1 results on
the Hyperpartisan dataset.
The RoBERTa and
Longformer for the English language were taken
from ”roberta-base” and ”allenai/longformer-base-
4096” checkpoints hosted on the Huggingface hub
(Wolf et al., 2020), respectively.
Model
Hyperpartisan (En)
Hyperpartisan (He)
RoBERTa (English)
87.3
—
HeRo
—
86.9
Longformer (English)
90.1
—
LongHeRo
—
89.1
Tab.
5 demonstrates the compatibility of
the Hebrew models to their English counter-

--- Page 5 ---

parts and the improvement of the LongHeRo
model over the standard length input model
HeRo.
The training process exhibited continuing
improvement in both the pre-training loss and
the performance on the downstream tasks.
This suggests that further pre-training of the
released models in conjunction with the re-
leased dataset will yield even higher perfor-
mance. Thus, we encourage the users to con-
tinue pre-training the released models on the
released dataset prior to fine-tuning on down-
stream tasks.
5
Conclusions
In this paper, we presented several additional
resources for the Hebrew NLP community. We
introduced a new pre-train dataset HeDC4
for the Hebrew language, which is two and a
half times larger than the one previously used
in the literature.
This dataset was used to
train a new language model HeRo, based on
the RoBERTa architecture.
A mid-training
checkpoint of the HeRo model was then used
to train the first Hebrew language model for
long documents LongHeRo, based on the Long-
former architecture.
The models were evaluated on several down-
stream tasks and compared to the results pre-
sented in the literature.
The HeRo model
presented state-of-the-art results on the sen-
timent analysis, the named entity recognition
tasks, and the question answering task. The
LongHeRo model was evaluated on the doc-
ument classification task using a translated
dataset.
The HeRo model was evaluated as
a baseline. The performance of both models
were found compatible with their English coun-
terparts. For future work we aim to further
investigate the performance of the LongHeRo
model by evaluating it on other tasks involving
long documents such as document similarity.
6
Acknowledgements
We are grateful to Tal Geva and Amir David
Nissan Cohen for technical discussions during
the project.
References
Julien Abadji, Pedro Ortiz Suarez, Laurent
Romary,
and Benoît Sagot. 2022.
To-
wards a cleaner document-oriented multi-
lingual crawled corpus.
arXiv preprint
arXiv:2201.06642.
Adam Amram, Anat Ben David, and Reut
Tsarfaty. 2018. Representations and archi-
tectures in neural sentiment analysis for
morphologically rich languages:
A case
study from modern hebrew.
In Proceed-
ings of the 27th International Conference
on Computational Linguistics, pages 2242–
2252.
Dan Bareket and Reut Tsarfaty. 2021. Neural
modeling for named entities and morphol-
ogy (nemoˆ2). Transactions of the Associ-
ation for Computational Linguistics, 9:909–
928.
Iz Beltagy, Matthew E Peters, and Arman
Cohan. 2020.
Longformer:
The long-
document transformer.
arXiv
preprint
arXiv:2004.05150.
Andrei Z Broder. 1997. On the resemblance
and containment of documents. In Proceed-
ings. Compression and Complexity of SE-
QUENCES 1997 (Cat. No. 97TB100171),
pages 21–29. IEEE.
Avihay Chriqui and Inbal Yahav. 2021. Hebert
& hebemo: a hebrew bert model and a tool
for polarity analysis and emotion recogni-
tion. arXiv preprint arXiv:2102.01909.
Marta R Costa-jussà, James Cross, Onur
Çelebi, Maha Elbayad, Kenneth Heafield,
Kevin Heffernan, Elahe Kalbassi, Janice
Lam, Daniel Licht, Jean Maillard, et al.
2022.
No language left behind:
Scaling
human-centered machine translation. arXiv
preprint arXiv:2207.04672.
Jacob Devlin, Ming-Wei Chang, Kenton Lee,
and Kristina Toutanova. 2018. Bert: Pre-
training of deep bidirectional transformers
for language understanding. arXiv preprint
arXiv:1810.04805.
Eylon Guetta, Avi Shmidman, Shaltiel Shmid-
man, Cheyn Shmuel Shmidman, Joshua
Guedalia,
Moshe Koppel,
Dan Bareket,
Amit Seker, and Reut Tsarfaty. 2022. Large
pre-trained models with extra-large vocabu-
laries: A contrastive analysis of hebrew bert

--- Page 6 ---

models and a new one to outperform them
all. arXiv preprint arXiv:2211.15199.
Kelvin
Guu,
Kenton
Lee,
Zora
Tung,
Panupong Pasupat, and Mingwei Chang.
2020. Retrieval augmented language model
pre-training.
In International Conference
on Machine Learning,
pages 3929–3938.
PMLR.
Omri Keren and Omer Levy. 2021. Parashoot:
A hebrew question answering dataset. arXiv
preprint arXiv:2109.11314.
Johannes
Kiesel,
Maria
Mestre,
Rishabh
Shukla, Emmanuel Vincent, Payam Adineh,
David Corney, Benno Stein, and Martin
Potthast. 2019. Semeval-2019 task 4: Hy-
perpartisan news detection. In Proceedings
of the 13th International Workshop on Se-
mantic Evaluation, pages 829–839.
Katherine Lee,
Daphne Ippolito,
Andrew
Nystrom, Chiyuan Zhang, Douglas Eck,
Chris Callison-Burch, and Nicholas Carlini.
2021.
Deduplicating training data makes
language models better.
arXiv preprint
arXiv:2107.06499.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei
Du, Mandar Joshi, Danqi Chen, Omer Levy,
Mike Lewis, Luke Zettlemoyer, and Veselin
Stoyanov. 2019.
Roberta: A robustly op-
timized bert pretraining approach.
arXiv
preprint arXiv:1907.11692.
Ilya Loshchilov and Frank Hutter. 2017. De-
coupled weight decay regularization. arXiv
preprint arXiv:1711.05101.
Naama Ben Mordecai and Michael Elhadad.
2005. Hebrew named entity recognition.
Gabriele Sarti and Malvina Nissim. 2022. It5:
Large-scale text-to-text pretraining for ital-
ian language understanding and generation.
arXiv preprint arXiv:2203.03759.
Amit Seker, Elron Bandel, Dan Bareket, Idan
Brusilovsky, Refael Shaked Greenfeld, and
Reut Tsarfaty. 2021. Alephbert: A hebrew
large pre-trained language model to start-
off your hebrew nlp application with. arXiv
preprint arXiv:2104.04052.
Rico Sennrich, Barry Haddow, and Alexan-
dra Birch. 2015.
Neural machine transla-
tion of rare words with subword units. arXiv
preprint arXiv:1508.07909.
Pedro Javier Ortiz Suárez, Laurent Romary,
and Benoît Sagot. 2020. A monolingual ap-
proach to contextualized word embeddings
for mid-resource languages. arXiv preprint
arXiv:2006.06202.
Jörg Tiedemann and Santhosh Thottingal.
2020.
Opus-mt–building open translation
services for the world.
In Proceedings of
the 22nd Annual Conference of the European
Association for Machine Translation. Euro-
pean Association for Machine Translation.
Trieu H Trinh and Quoc V Le. 2018. A simple
method for commonsense reasoning. arXiv
preprint arXiv:1806.02847.
Thomas Wolf, Lysandre Debut, Victor Sanh,
Julien Chaumond, Clement Delangue, An-
thony Moi, Pierric Cistac, Tim Rault, Rémi
Louf, Morgan Funtowicz, et al. 2020. Trans-
formers: State-of-the-art natural language
processing. In Proceedings of the 2020 con-
ference on empirical methods in natural lan-
guage processing:
system demonstrations,
pages 38–45.
Linting Xue, Noah Constant, Adam Roberts,
Mihir Kale,
Rami Al-Rfou,
Aditya Sid-
dhant, Aditya Barua, and Colin Raffel. 2020.
mt5: A massively multilingual pre-trained
text-to-text transformer.
arXiv preprint
arXiv:2010.11934.
Manzil
Zaheer,
Guru
Guruganesh,
Ku-
mar Avinava Dubey, Joshua Ainslie, Chris
Alberti, Santiago Ontanon, Philip Pham,
Anirudh Ravula, Qifan Wang, Li Yang, et al.
2020. Big bird: Transformers for longer se-
quences.
Advances in Neural Information
Processing Systems, 33:17283–17297.
Rowan
Zellers,
Ari
Holtzman,
Hannah
Rashkin,
Yonatan
Bisk,
Ali
Farhadi,
Franziska Roesner, and Yejin Choi. 2019.
Defending against neural fake news.
Ad-
vances in neural information processing sys-
tems, 32.

--- Page 7 ---

Yukun Zhu, Ryan Kiros, Rich Zemel, Rus-
lan Salakhutdinov, Raquel Urtasun, Anto-
nio Torralba, and Sanja Fidler. 2015. Align-
ing books and movies: Towards story-like
visual explanations by watching movies and
reading books. In Proceedings of the IEEE
international conference on computer vision,
pages 19–27.
A
Near-Duplicate Example
The example in Tab. 6 demonstrates the near-
duplicate document which was present in the
dataset prior to deduplication. The similarity
between documents is colored in blue.
It
is clear that the only difference between the
documents is in the short starting sentence.

--- Page 8 ---

Table 6: An example of an identified near-duplicate document.
Example - Doc.Id 135
Near-duplicate example - Doc.Id 89087
'קריינות: בגן הזה הילדים מדברים בעברית
ובערבית וחוגגים בו חגים של שלושת הדתות. הוא
הוקם ביוזמת הורים יהודים וערבים ביפו, שביקשו
כי ילדיהם ילמדו במסגרות משותפות, ללא מחיצות
והפרדה.לאחר שנתיים של פעילות, עלה הצורך
הקמת בית ספר-הטבעי במסגרת המשכית
ערבי. כמו עם הקמת הגנים, גם כאן, נתקלו-יהודי
ההורים בהתנגדות העירייה.אופיר קהת: בעצם מה
שאנחנו מבקשים זה דבר מאד פשוט. אנחנו רוצים
להמשיך עם ההצלחה שלנו של גני הילדים הדו
לשוניים ולפתוח בית ספר צומח שיממש את
השאיפות שלנו לדו קיום.מרב קליין אשר: אני
חושבת שבית ספר דו לשוני הוא הרבה הרבה יותר
מאשר רק ללמוד את השפה. יש משהו ביכולת של
ילדים לא להיות גזעניים, שזה דבר נערץ ומקסים
ושובה לב ואני חושבת שבאמת היכולת ללמוד את
השפות אחד של השני מתוך מקום של כבוד
והערכה ושוויון אמיתי.קריינות: העירייה מצידה
הציעה להורים להשתלב בבית ספר ממלכתי קיים
במקום להקים בית ספר דו לשוני, בשלב זה פתרון
זה לא נתקבל על ידי ההורים בחיוב.אופיר קהת:
הסיבה שאנחנו לא מעוניינים להירשם לבית הספר
החלופי, שאותו העירייה מציעה, מדובר בבית ספר
במסלול עברי שבו המנהל לא מאפשר לערבים
לדבר בערבית.סופי קאסם: אנחנו רוצים לחנך את
הילדים שלנו ללמוד גם את הערכים של היהודים
וגם את הערכים שאנחנו לא רוצים לאבד את
השפה שלנו, את הדת שלנו.מרב קליין אשר:
המערכת עצמה היא מערכת שמעדיפה את
העברית, שמעדיפה את היהודי, שמעדיפה את
הסמלים היהודיים שנותנת כבוד לחגים היהודיים.
ואני חושבת שבאמת כילד ערבי ביפו לגדול בלי
שהגן שלך והבית ספר שלך והמורה שלך מכבדת
את הזהות שלך את החגים שלך את השפה שלך, זה
חינוך לאפליה זה חינוך לגזענות.סופי קאסם: כולנו
עובדים בשביל הילדים שלנו כולנו רוצים לחנך את
הילדים שלנו. לכולנו יש אותן מטרות לחנך את
הילדים שלנו לעולם יותר טוב והבית ספר הזה עונה
על הדרישות שלנו.קריינות: כעבור כמה ימים הגיעו
הצדדים לפשרה. העירייה התחייבה כי בכיתות הדו
לשוניות בבית הספר הממלכתי יהודי ילמדו שתי
מורות ערבייה ויהודיה מו כן לוח החגים יכלול את
כל החגים של היהודים והערבים.'
.ידי: הטלוויזיה החברתית-'הכתבה הופקה על
קריינות: בגן הזה הילדים מדברים בעברית
ובערבית וחוגגים בו חגים של שלושת הדתות. הוא
הוקם ביוזמת הורים יהודים וערבים ביפו, שביקשו
כי ילדיהם ילמדו במסגרות משותפות, ללא מחיצות
והפרדה.לאחר שנתיים של פעילות, עלה הצורך
הקמת בית ספר-הטבעי במסגרת המשכית
ערבי. כמו עם הקמת הגנים, גם כאן, נתקלו-יהודי
ההורים בהתנגדות העירייה.אופיר קהת: בעצם מה
שאנחנו מבקשים זה דבר מאד פשוט. אנחנו רוצים
להמשיך עם ההצלחה שלנו של גני הילדים הדו
לשוניים ולפתוח בית ספר צומח שיממש את
השאיפות שלנו לדו קיום.מרב קליין אשר: אני
חושבת שבית ספר דו לשוני הוא הרבה הרבה יותר
מאשר רק ללמוד את השפה. יש משהו ביכולת של
ילדים לא להיות גזעניים, שזה דבר נערץ ומקסים
ושובה לב ואני חושבת שבאמת היכולת ללמוד את
השפות אחד של השני מתוך מקום של כבוד
והערכה ושוויון אמיתי.קריינות: העירייה מצידה
הציעה להורים להשתלב בבית ספר ממלכתי קיים
במקום להקים בית ספר דו לשוני, בשלב זה פתרון
זה לא נתקבל על ידי ההורים בחיוב.אופיר קהת:
הסיבה שאנחנו לא מעוניינים להירשם לבית הספר
החלופי, שאותו העירייה מציעה, מדובר בבית ספר
במסלול עברי שבו המנהל לא מאפשר לערבים
לדבר בערבית.סופי קאסם: אנחנו רוצים לחנך את
הילדים שלנו ללמוד גם את הערכים של היהודים
וגם את הערכים שאנחנו לא רוצים לאבד את
השפה שלנו, את הדת שלנו.מרב קליין אשר:
המערכת עצמה היא מערכת שמעדיפה את
העברית, שמעדיפה את היהודי, שמעדיפה את
הסמלים היהודיים שנותנת כבוד לחגים היהודיים.
ואני חושבת שבאמת כילד ערבי ביפו לגדול בלי
שהגן שלך והבית ספר שלך והמורה שלך מכבדת
את הזהות שלך את החגים שלך את השפה שלך, זה
חינוך לאפליה זה חינוך לגזענות.סופי קאסם: כולנו
עובדים בשביל הילדים שלנו כולנו רוצים לחנך את
הילדים שלנו. לכולנו יש אותן מטרות לחנך את
הילדים שלנו לעולם יותר טוב והבית ספר הזה עונה
על הדרישות שלנו.קריינות: כעבור כמה ימים הגיעו
הצדדים לפשרה. העירייה התחייבה כי בכיתות הדו
לשוניות בבית הספר הממלכתי יהודי ילמדו שתי
מורות ערבייה ויהודיה כמו כן לוח החגים יכלול את
כל החגים של היהודים והערבים.'

```
