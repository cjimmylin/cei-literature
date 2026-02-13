---
title: "2020-Amirkhani-FarsTail A Persian Natural Language Inference Dataset - PDF Extract"
source_pdf: "2020-Amirkhani-FarsTail A Persian Natural Language Inference Dataset.pdf"
pages: 24
extracted_at: "2026-02-13T09:50:27.956327"
---

# PDF Extract: 2020-Amirkhani-FarsTail A Persian Natural Language Inference Dataset

**Source PDF:** 2020-Amirkhani-FarsTail A Persian Natural Language Inference Dataset.pdf
**Total Pages:** 24

---

## Content

```
--- Page 1 ---

FarsTail: A Persian Natural Language Inference Dataset
Hossein Amirkhani, Mohammad AzariJafari, Zohreh Pourjafari,
Soroush Faridan-Jahromi, Zeinab Kouhkan, Azadeh Amirak
Computer Engineering and IT Department, University of Qom, Iran
Abstract
Natural language inference (NLI) is known as one of the central tasks in
natural language processing (NLP) which encapsulates many fundamental
aspects of language understanding. With the considerable achievements of
data-hungry deep learning methods in NLP tasks, a great amount of eﬀort
has been devoted to develop more diverse datasets for diﬀerent languages.
In this paper, we present a new dataset for the NLI task in the Persian lan-
guage, also known as Farsi, which is one of the dominant languages in the
Middle East. This dataset, named FarsTail, includes 10,367 samples which
are provided in both the Persian language as well as the indexed format to
be useful for non-Persian researchers. The samples are generated from 3,539
multiple-choice questions with the least amount of annotator interventions in
a way similar to the SciTail dataset. A carefully designed multi-step process
is adopted to ensure the quality of the dataset. We also present the results of
traditional and state-of-the-art methods on FarsTail including diﬀerent em-
bedding methods such as word2vec, fastText, ELMo, BERT, and LASER,
as well as diﬀerent modeling approaches such as DecompAtt, ESIM, HBMP,
and ULMFiT to provide a solid baseline for the future research. The best
obtained test accuracy is 83.38% which shows that there is a big room for
improving the current methods to be useful for real-world NLP applications
in diﬀerent languages. We also investigate the extent to which the models ex-
ploit superﬁcial clues, also known as dataset biases, in FarsTail, and partition
the test set into easy and hard subsets according to the success of biased mod-
els. The dataset is available at https://github.com/dml-qom/FarsTail.
Keywords:
Natural language processing, Natural language inference,
Email address: amirkhani@qom.ac.ir (Hossein Amirkhani)
Preprint submitted to Elsevier
July 12, 2021
arXiv:2009.08820v2  [cs.CL]  8 Jul 2021

--- Page 2 ---

Persian language, Farsi dataset, Deep learning, Benchmark
1. Introduction
Natural Language Processing (NLP) deals with the development of auto-
matic methods for processing, analyzing, and generating human languages.
It consists of a vast number of problems, ranging from low-level to high-level
tasks such as named entity recognition [1], sentiment analysis [2], machine
translation [3], and machine reading comprehension [4]. One important task
in NLP is Natural Language Inference (NLI) which is believed to be a strin-
gent test for language understanding, since a system with the ability to iden-
tify the implications of natural language sentences should have a good level
of language understanding [5].
The goal of NLI is to determine the inference relationship between a
premise p and a hypothesis h. It is a three-class problem, where each pair
(p, h) is assigned to one of these classes: entailment if the hypothesis can be
inferred from the premise, contradiction if the hypothesis contradicts with the
premise, and neutral if none of the other conditions hold. To determine the
hypothesis status, some prior knowledge is considered besides the premise.
This includes the knowledge that typical speakers of that language know, such
as the commonsense facts and general semantic knowledge. For example, the
typical English speakers know that “USA” refers to “the United States of
America”.
After substantial success of deep learning (DL) based methods in diﬀer-
ent artiﬁcial intelligence tasks, the NLP researchers also started to develop
DL-based models to learn the patterns in available natural language data gen-
erated by humans [6]. The percentage of deep learning papers nearly doubled
in a six-year period from 2012 in the major NLP conferences [7]. Since these
methods need a large amount of training data to let the model learn the
general pattern for the particular task without overﬁtting to the available
data, diﬀerent research groups started to gather and publish large datasets.
For the NLI task, the development of Stanford NLI dataset (SNLI) caused a
considerable progress in developing DL-based models for NLI task [8].
In DL-based NLI literature, there has been a considerable amount of re-
searches on languages with a large amount of training data, such as English,
but relatively little attention has been paid to data-poor languages. Despite
some eﬀorts in developing NLI datasets for other languages by translation or
2

--- Page 3 ---

transferring knowledge obtained from learning on one language to other lan-
guages [9], presenting native datasets for other languages help develop models
with more comprehensive language understanding capabilities. In addition,
these datasets can be used to evaluate the proposed learning architectures
and methods for a broader range of languages.
The focus of this paper is on Persian (Farsi) language which is a pluricen-
tric language spoken and used by around 110 million people in countries such
as Iran, Afghanistan, and Tajikistan. It has had a considerable inﬂuence on
its neighboring languages such as Turkic, Armenian, Georgian, and Indo-
Aryan languages. Its alphabet includes 32 characters written right to left.
Table 1 shows some features of Persian language which make its processing
diﬀerent from other languages.
In this paper, we present, to the best of our knowledge, the ﬁrst relatively
large-scale Persian corpus for NLI task, called FarsTail. We tried to reduce
the amount of annotation interventions to provide realistic samples which are
naturally occurring in real-world applications instead of task-speciﬁc synthe-
sized examples. A protocol similar to the SciTail dataset [10] is followed
where the sentences are either generated, with the least amount of inter-
ventions, from multiple-choice questions or selected from natural sentences
that already exist independently “in the wild”. However, in contrast to Sci-
Tail which only includes the neutral and entailment classes, we also include
contradiction examples in the dataset.
Each person generates three data examples from a multiple-choice ques-
tion, one for each class, with the same premises but diﬀerent hypotheses.
The entailment hypothesis is formed by substituting the correct answer in
the question. Then, a text snippet is extracted from web that the generated
hypothesis can be inferred from. The contradiction hypothesis is formed by
substituting one wrong answer in the question. Finally, the neutral hypoth-
esis is extracted from web such that it is similar to the question but with
an unknown status based on the premise. In the next phase, each sample
is relabeled by four other persons and the samples with at least 4 out of 5
agreements are preserved. The rejected samples undergo a new modiﬁcation
and relabeling phase.
A total of 10,367 samples are generated from a collection of 3,539 multiple-
choice questions. The train, validation, and test portions include 7,266, 1,537,
and 1,564 instances, respectively.
We ensure that the instances with the
same premises are in the same set. The developed dataset can also be used
in other tasks such as question answering, summarization, semantic search,
3

--- Page 4 ---

Table 1: Some features of Persian language which make its processing diﬀerent from other
languages.
Feature 
Example 
Different forms for some words 
“Caesar” is written as either “اﻣﭙﺮاﺗﻮر” or 
“اﻣﭙﺮاﻃﻮر” 
Different words used for some foreign 
concepts 
“computer” is written as either “ﮐﺎﻣﭙﯿﻮﺗﺮ” or 
“راﯾﺎﻧﻪ” 
Adding a space may change the meaning 
“ﻣﺎدر” means “mother”, while “ﻣﺎ در” means 
“we are in” 
Words with the same spelling but different 
pronunciation and meaning 
“ﻣﻠﮏ” can be pronounced as “molk” or 
“malek” which mean “territory” and “king”, 
respectively 
Words arbitrarily disjointed to two words 
separated with a space 
“nobody” is written as either “ﻫﯿﭽﮑﺲ” or  
“ﻫﯿﭻ ﮐﺲ” 
Words with different plural forms 
“teachers” can be written as “ﻣﻌﻠﻤﺎن”, “ﻣﻌﻠﻢ
ﻫﺎ”, 
or “ﻣﻌﻠﻤﯿﻦ” 
Words with different formal and 
conversational forms 
“listening” is formally written as “ﺷﻨﯿﺪن”, 
while it is sometimes written in 
conversational form as “ﺷﻨﻔﺘﻦ” 
The critical role of punctuation in the 
meaning of some sentences 
“ﻻزم ﻧﯿﺴﺖ اﻋﺪاﻣﺶ ﮐﻨﯿﺪ ،ﺑﺨﺸﺶ”: Forgive him, it is 
not necessary to execute him. 
“اﻋﺪاﻣﺶ ﮐﻨﯿﺪ ،ﺑﺨﺸﺶ ﻻزم ﻧﯿﺴﺖ”: It is not 
necessary to forgive him, execute him.  
Prior knowledge that typical Persian language 
speakers know 
“Before revolution” means “Before 1979 
revolution” to Iranians 
and machine translation. The developed dataset (as raw texts for Persian
researchers and indexed data for non-Persian researchers) has been released
for non-commercial usages.
We evaluate diﬀerent traditional and state-of-the-art methods on FarsTail,
including diﬀerent embedding methods such as word2vec [11], fastText [12],
ELMo [13], BERT [14], and LASER [15], as well as diﬀerent modeling meth-
ods such as DecompAtt [16], ESIM [17], HBMP [18], and ULMFiT [19]. The
best obtained accuracy on test set is 83.38% which shows that there are many
rooms to improve the models trained on this dataset. We also investigate
the superﬁcial clues, also known as dataset biases, available in FarsTail to
obtain a more realistic view of the performance of the models.
4

--- Page 5 ---

Concurrent to this work, ParsiNLU [20] is developed which is a suite of
Persian datasets for diﬀerent tasks, including an NLI set with 2,700 instances.
Around half of the instances are written by native speakers and the remaining
instances are translated from the MNLI dataset [21]. FarsTail is superior to
this dataset in three aspects: It has around 4 times more instances; it just in-
cludes ﬁrst-hand native sentences without translation clues; and task-speciﬁc
human-generated texts are kept as low as possible to provide instances which
are naturally occurring in real-world applications.
The rest of this paper is organized as follows. In Section 2, the avail-
able English and non-English NLI datasets are reviewed. Section 3 presents
the FarsTail development process as well as its statistics. The experimental
results are presented in Section 4, and the paper concludes in the last section.
2. Related work
In this section, we review some available English and non-English NLI
datasets.
2.1. English NLI datasets
• SICK [22]: As one of the ﬁrst attempts to introduce relatively large-
scale datasets for NLI task, this dataset was introduced as a task in
SemEval-2014. It consists of about 10k English sentence pairs anno-
tated for two diﬀerent tasks, relatedness in meaning and entailment.
The original sentence pairs are randomly selected from 8k ImageFlickr
dataset and the SemEval 2012 STS MSR-Video Description dataset.
Some rule-based syntactic and lexical transformations are applied to
each sentence to obtain sentences with similar, contradictory, and dif-
ferent meanings. Its partly automated construction introduced some
spurious patterns into the data [8].
• SNLI [8]: The Stanford NLI dataset has been developed to alleviate the
lack of large-scale annotated data for the NLI problem. It includes 570k
labeled instances (550k training, 10k validation, and 10k test examples)
gathered using the Amazon Mechanical Turk. An image caption was
presented to each turker as the premise and they were asked to generate
three sentences as hypothesis, one for each class (entailment, contra-
diction, and neutral). In the relabeling phase, if at least three out of
four new labelers agreed with the main label, this instance was kept in
5

--- Page 6 ---

the dataset. This dataset played a considerable role in developing and
enhancing deep learning-based NLI systems.
• MultiNLI [21]: Compared to SNLI, MultiNLI covers 10 diﬀerent genres
of spoken and written text. With 433k instances, its scale is comparable
to SNLI. The test set consists of two parts: matched set which includes
the same genres in the training set and mismatched set which includes
genres not available in the training set.
This allows for cross-genre
generalization evaluation.
• MedNLI [23]: This dataset was generated by the same approach as
SNLI, adjusted for the clinical domain. The MIMIC-III v1.3 [24], with
de-identiﬁed records of 38,597 patients, was used as the premise source.
The hypothesis sentences were generated by clinicians. Four clinicians
worked on a total of 4,683 premises over a period of six weeks, which
resulted in 14,049 unique sentence pairs.
• SciTail [10]: This is the ﬁrst NLI dataset which is collected using the
available texts without authoring the sentences. This makes the dataset
more realistic, since it consists of natural texts instead of task-speciﬁc
synthesized sentences. SciTail is the most similar dataset to the dataset
presented in this paper.
The hypotheses were created from science
questions and their corresponding answers, and premises were gathered
from the relevant web sentences. It contains 1,834 questions with 10,101
entailment instances and 16,925 neutral ones. This dataset does not
contain the contradiction label.
• QA-NLI [25]: This dataset is similar to SciTail, except that it was
fully automatically constructed. The authors proposed a method to
derive NLI datasets from the question answering datasets. This was
done by introducing the QA2D task to derive a declarative sentence
from a question-answer pair. The generated sentence (D) along with
the corresponding passage (P) forms an NLI example as (P, D). For
the correct, incorrect, and unknown answers, the pairs were labeled as
entailment, contradiction, and neutral, respectively. Note that incor-
rect answers are available in QA datasets with multiple answers, and
unknowns are also available in some datasets such as SQuAD 2.0 [26].
6

--- Page 7 ---

2.2. Non-English NLI datasets
• Evalita [27]: Constructed on the basis of Wikipedia revision histories,
this dataset includes 800 short Italian sentence pairs.
• ArbTEDS [28]: This is a small Arabic dataset with 600 pairs annotated
as either inferable or non-inferable. A semi-automatic tool was used to
extract the candidate pairs from web, using the Arabic news headlines
as the hypothesis and one paragraph returned by the Google-API for
this headline as the premise.
The pairs were then labeled by eight
annotators.
• German emails [29]: Constructed from the customer emails to the sup-
port center of a multimedia software company as premises and the
category descriptions as the hypotheses, this dataset includes 638 en-
tailment and 24,143 non-entailment pairs.
The matching and non-
matching categories were considered as entailment and non-entailment
hypotheses, respectively.
• ASSIN [30]: This is a two-class dataset with the entailment and not-
entailment classes including a collection of 10,000 pairs, half in Brazil-
ian Portuguese and half in European Portuguese.
• XNLI [9]: This dataset was developed for evaluating the cross-lingual
understanding capabilities of models. The same crowdsourcing-based
procedure used for MultiNLI dataset [21] was followed to collect and
validate 750 examples from each of ten text sources resulted in a total
of 7,500 examples. These examples were then translated into 14 diﬀer-
ent languages by professional translators. The total 112,500 annotated
pairs are in English, French, Spanish, German, Greek, Bulgarian, Rus-
sian, Turkish, Arabic, Vietnamese, Thai, Chinese, Hindi, Swahili, and
Urdu languages. Unfortunately, it does not include the Persian lan-
guage.
• OCNLI [31]: This is the ﬁrst large-scale Chinese NLI dataset which
includes around 56k annotated sentence pairs. The annotations are
elicited from native speakers specializing in linguistics.
• ParsiNLU [20]: This concurrent work is a suite of Persian datasets for
diﬀerent tasks, including an NLI set with 2,700 instances. Around half
7

--- Page 8 ---

Retain samples with at 
least 80% agreement
Build entailment hypothesis
(question + correct answer) 
Find premise from web for 
entailment hypothesis
Find neutral hypothesis from 
web
Build contradict hypothesis
(question + incorrect answer) 
Relabel each sample by 
4 other annotators
Data cleaning
Multiple-choice 
questions
FarsTail dataset
Revise and relabel again 
the removed samples
Figure 1: The FarsTail dataset development steps.
of the instances are written by native speakers and the remaining in-
stances are translated from the MultiNLI dataset [21]. The superiority
of the FarsTail dataset over the ParsiNLU NLI set is that it includes
around 4 times more instances which are ﬁrst-hand native sentences
without translation clues. Also, to provide texts that are naturally oc-
curring in real-world applications, FarsTail includes the least amount
of task-speciﬁc human-generated texts.
3. FarsTail dataset
In this section, we present the process of developing FarsTail dataset as
well as its statistics. FarsTail has been developed with a process similar to
the SciTail dataset [10] with some modiﬁcations. A group of ﬁve persons
(called annotators herein) with a background in NLI worked under the su-
pervision of an NLP expert to develop FarsTail. The taken steps are depicted
in Fig. 1 which include generating NLI instances from multiple-choice ques-
tions, relabeling, and data cleaning. The details of these steps are given in
Sections 3.1 and 3.2, and the dataset statistics are presented in Section 3.3.
3.1. Generating NLI instances from questions
A collection of 3,539 multiple-choice questions was gathered from Iranian
university exams in diﬀerent topics including religion, history, constitution of
Iran, history of literature, and Islamic revolution. For each multiple-choice
question, an annotator followed the following steps to generate three diﬀerent
pairs, one for each class (entailment, contradiction, and neutral):
8

--- Page 9 ---

Multiple-choice question: 
دﺑﯿﺮ ﮐﻞ ﺳﺎزﻣﺎن ﻣﻠﻞ ﻣﺘﺤﺪ ﻗﺒﻞ از آﻧﺘﻮﻧﯿﻮ ﮔﻮﺗﺮش ﭼﻪ ﮐﺴﯽ ﺑﻮد؟ 
o
 ﺧﺎوﯾﺮ ﺳﻮﻻﻧﺎ 
o
 
(ﺑﺎن ﮐﯽ ﻣﻮن )ﺟﻮاب ﺻﺤﯿﺢ 
o
 ﮐﻮﻓﯽ ﻋﻨﺎن 
o
 ﯾﻮﺷﯿﺮو ﻣﻮري 
Who was the Secretary-General of the United Nations before António Guterres? 
o Javier Solana 
o Ban Ki-moon (correct answer) 
o Kofi Annan 
o Yoshirō Mori 
 
 
:
Entailment hypothesis (question + correct answer)
 
.دﺑﯿﺮ ﮐﻞ ﺳﺎزﻣﺎن ﻣﻠﻞ ﻣﺘﺤﺪ ﻗﺒﻞ از آﻧﺘﻮﻧﯿﻮ ﮔﻮﺗﺮش، ﺑﺎن ﮐﯽ ﻣﻮن ﺑﻮد 
Ban Ki-moon was the Secretary-General of the United Nations before António Guterres.
 
:
Premise (from web)
 
.ﻣﺠﻤﻊ ﻋﻤﻮﻣﯽ ﺳﺎزﻣﺎن ﻣﻠﻞ ﻣﺘﺤﺪ رﺳﻤﺎً آﻧﺘﻮﻧﯿﻮ ﮔﻮﺗﺮش را ﺑﻌﻨﻮان دﺑﯿﺮﮐﻞ ﺑﻌﺪي ﺳﺎزﻣﺎن ﻣﻠﻞ ﻣﺘﺤﺪ و ﺟﺎﻧﺸﯿﻦ ﺑﺎن ﮐﯽ ﻣﻮن اﻧﺘﺨﺎب ﮐﺮد 
The United Nations General Assembly formally elected António Guterres as the next UN Secretary-General and Ban Ki-
moon's successor.
 
 
Contradiction hypothesis (question + incorrect answer): 
.ﮐﻮﻓﯽ ﻋﻨﺎن ﭘﯿﺶ از آﻧﺘﻮﻧﯿﻮ ﮔﻮﺗﺮش ﺑﻌﻨﻮان دﺑﯿﺮ ﮐﻞ ﺳﺎزﻣﺎن ﻣﻠﻞ ﻣﺘﺤﺪ اﻧﺘﺨﺎب ﺷﺪه ﺑﻮد 
Before António Guterres, Kofi Annan had been selected as the United Nations Secretary-General. 
 
Neutral hypothesis (from web): 
.اﻋﻀﺎي ﺳﺎزﻣﺎن ﻣﻠﻞ ﻣﺘﺤﺪ ﺑﻪ اﺗﻔﺎق آرا آﻧﺘﻮﻧﯿﻮ ﮔﻮﺗﺮش را ﺑﻌﻨﻮان ﻧﺎﻣﺰد دﺑﯿﺮ ﮐﻠﯽ ﺳﺎزﻣﺎن ﻣﻠﻞ ﻣﺘﺤﺪ ﻣﻌﺮﻓﯽ ﮐﺮدﻧﺪ 
The United Nations members unanimously nominated António Guterres as UN Secretary-General. 
 
 
Figure 2: An example of generating NLI instances from questions in FarsTail.
1. The correct answer is inserted into the question to generate a sentence
called h1.
2. The web is searched to ﬁnd a text portion p where (p, h1) has entailment
relation. We use the available texts on the web instead of generating
the premises to provide real-world, naturally occurring texts instead of
task-speciﬁc synthesized examples.
3. An incorrect answer is inserted into the question to generate a sentence
called h2 such that (p, h2) has contradiction relation. The annotator is
asked to generate h2 similar to h1 in length, but diﬀerent in structure
and words.
4. From the web, a related sentence h3 is found with a similar length to
h1 and h2 such that its entailment or contradiction relation cannot be
inferred from p. The pair (p, h3) is considered as a neutral instance.
Fig. 2 shows an example of the sample generation process in FarsTail.
9

--- Page 10 ---

3.2. Relabeling and data cleaning
After the sample generation phase, each sample was relabeled by the
other four annotators retaining the samples with an agreement of at least
80% among ﬁve labelers. The samples were presented to the annotators in
a random order to reduce annotation bias caused by presenting the samples
with the same premise in succession. To give the rejected samples one more
chance, they were revised by their original annotator and relabeled again.
The samples which could not obtain a 80% label agreement in any of these
two relabeling phases were removed. Among all 10,617 samples (3, 5393),
190 samples were removed in this phase resulting in 10,427 instances.
The retained samples were investigated one more time for spelling and
writing mistakes emphasizing on avoiding probable label change caused by
cleaning. Finally, to reduce the unwanted repetition in the data, 60 more
samples were removed including the instances generated from diﬀerent ques-
tions which both their premises and hypotheses had a cosine similarity higher
than 0.8. The total number of samples in the dataset is therefore 10,367.
The instances were randomly divided into training, validation, and test
sets such that the samples generated from the same question were in the same
subset. In addition, to avoid information leak, the samples generated from
diﬀerent questions which either their premises or hypotheses had a cosine
similarity higher than 0.9 were included in the same subset. The training,
validation, and test sets percentages are nearly 70/15/15 with 7,266, 1,537,
and 1,564 samples, respectively.
The dataset is presented in two formats, raw and indexed.
The raw
data includes the Persian sentences, while the indexed data is a tokenized
version of sentences where each sentence is encoded as a list of word indexes
(integers)1.
3.3. FarsTail statistics
The statistics of FarsTail dataset is presented in Table 2. To provide the
possibility for comparing diﬀerent subsets, there is one section for each of
train, validation, and test sets. For each of these sets, beside the total statis-
tics, the statistics for diﬀerent classes are also shown separately where E, C,
and N stand for entailment, contradiction, and neutral classes, respectively.
1Hazm python library was used for tokenization (https://github.com/sobhe/hazm)
10

--- Page 11 ---

Table 2: Statistics of the FarsTail dataset.
subset
class
samples prem.
tokens
hyp.
tokens
prem.
proc.
tokens
hyp.
proc.
tokens
overlap
proc.
overlap
Train
E
2,429
40.50
15.53
19.35
8.42
0.67
0.68
N
2,448
40.52
15.62
19.31
8.26
0.40
0.30
C
2,389
40.23
15.61
19.20
8.30
0.57
0.54
Total
7,266
40.42
15.59
19.29
8.33
0.55
0.51
Val
E
515
39.70
14.85
19.13
8.27
0.67
0.66
N
523
39.71
14.95
19.16
8.06
0.39
0.29
C
499
39.58
15.09
19.17
8.11
0.58
0.54
Total
1,537
39.67
14.96
19.15
8.14
0.54
0.50
Test
E
519
39.57
15.48
18.84
8.39
0.68
0.68
N
535
39.23
16.02
18.73
8.36
0.38
0.27
C
510
39.44
15.81
18.86
8.38
0.57
0.52
Total
1,564
39.41
15.78
18.81
8.38
0.54
0.49
The column “samples” of Table 2 shows the number of samples in each
subset. As mentioned in Section 3.2, 70/15/15% of data go to the train,
validation, and test sets, respectively. It can be seen that this is a balanced
dataset without any meaningful diﬀerences between the number of samples
in diﬀerent classes.
The next column (premise tokens) presents the average number of to-
kens in the premises obtained by the Hazm python library’s tokenizer. The
next column (hypothesis tokens) shows the same values for hypothesis sen-
tences. To provide a more meaningful length statistic, the next two columns
(premise processed tokens and hypothesis processed tokens) report the num-
ber of unique tokens ignoring stopwords2 as well as one-character tokens in-
cluding punctuations. It is worth mentioning that there are a total of 20,973
tokens in FarsTail dataset where 467 tokens are stopwords or one-character
tokens.
According to these four “tokens” columns, there is not any signiﬁcant
diﬀerence between the average number of tokens in train, validation, and test
sets. More importantly, the average number of tokens in diﬀerent classes are
2A stoplist with 389 words was used from Hazm library.
11

--- Page 12 ---

almost the same which shows that the length of premises and hypotheses
cannot be exploited as a feature to ﬁnd clues about the class of the given
inputs.
One more point to consider about the “tokens” columns is that the
premises in FarsTail are longer than the premises in SciTail dataset [10].
The reported average premise length for entail and neutral samples in Sci-
Tail training set are 10.79 and 10.28, respectively, while these numbers are
19.35 and 19.31 in FarsTail. Regarding hypotheses, the average length for
entail and neutral samples are respectively 6.69 and 7.01 which are almost
the same as FarsTail (8.42 and 8.26). These longer premises are due to the
FarsTail’s sample generation process where we insisted on ﬁnding exact web
text portions which the hypothesis could be inferred from.
Anyway, this
makes FarsTail a more challenging dataset since it seeks more reasoning to
connect the facts presented in longer premises.
Finally, the last two columns show the average proportion of the hypoth-
esis tokens that overlap with the premise. Both columns treat the sentences
as a set of tokens ignoring the word repetition, but the second column also
ignore the stopwords and one-character tokens. As expected, the most and
the least overlap between premise and hypothesis are in the entailment and
neutral samples, respectively.
This shows that there are some superﬁcial
clues in the samples which can be exploited to estimate the relationship be-
tween two sentences without truly understanding them. In Section 4.3, we
show that the mere similarity between premise and hypothesis can be used
in a simple baseline model which obtains an accuracy higher than random;
however, this accuracy is far from what that is obtained by more advanced
deep models.
4. Experiments
In this section, we present the results of diﬀerent methods on the FarsTail
dataset to provide a baseline for future researches. The evaluated models
are introduced in Sections 4.1 and the results are presented in Section 4.2.
Finally, in Section 4.3, we investigate the biases available in FarsTail to
provide a more realistic view of the performance of the models.
4.1. Models
We used diﬀerent methods for representing the input sentences rang-
ing from traditional TF-IDF to more recent word embedding methods such
12

--- Page 13 ---

as word2vec3 [11], fastText4 [12], ELMo5 [13], and BERT [14].
For the
BERT method, we ﬁne-tuned two pre-trained models from the Hugging Face
Transformers library [32], ParsBERT [33] and BERT-base-multilingual-cased
(mBERT).
As the classiﬁer, we exploited diﬀerent methods including Support Vector
Machine (SVM), Long Short-Term Memory (LSTM), and Gated Recurrent
Unit (GRU) along with three models developed specially for the NLI task
including DecompAtt [16], ESIM [17], and HBMP [18].
One popular approach in learning with small labeled training datasets is
to train a language model (LM) on a large unlabeled corpus and ﬁne-tune
it on the downstream task. Besides the BERT-based models which lie in
this category, we tested ULMFiT [19] with three steps: LM pre-training, LM
ﬁne-tuning, and classiﬁer ﬁne-tuning. In the ﬁrst step, a language model
was trained on a general-domain corpus. We used the Persian Wikipedia for
this purpose. Then, the trained LM was ﬁne-tuned on the target task texts
without considering their labels. Finally, the pre-trained language model was
augmented with additional layers which were trained on the labeled dataset
of the target task.
We also tested LASER6 [15] as an embedding space which is shared
between multiple languages.
Since LASER provides sentence embeddings
rather than word embeddings, a simple deep model was trained on the com-
puted representations.
The hyper-parameters were chosen based on the models’ accuracy on the
validation set. Most importantly, we selected the following values for the
BERT models: 3 epochs of training with a learning rate of 2e-5, a batch size
of 32, and a weight decay of 0.5.
4.2. Results
Table 3 shows the results obtained from training diﬀerent models on the
FarsTail training set. Note that the LASER and tf-idf representations were
just used with the SVM classiﬁer because they deliver sentence-level repre-
sentations which cannot be used with the word-level methods like LSTM and
BiGRU. On the other hand, to feed the SVM classiﬁer with the word-level
3http://vectors.nlpl.eu/repository
4https://fasttext.cc/docs/en/crawl-vectors.html
5https://github.com/HIT-SCIR/ELMoForManyLangs
6https://github.com/facebookresearch/LASER
13

--- Page 14 ---

Table 3: Validation and test set accuracy of diﬀerent models trained on the FarsTail
training set.
Model
Representation
Val Accuracy
Test Accuracy
SVM
tf-idf
0.5303
0.5301
LASER
0.5459
0.5198
word2vec
0.5120
0.5448
fastText
0.5296
0.5371
ELMo
0.5621
0.5710
LSTM
word2vec
0.5172
0.5243
fastText
0.5205
0.5192
ELMo
0.5478
0.5505
BiGRU
word2vec
0.5192
0.5224
fastText
0.5211
0.5243
ELMo
0.5582
0.5428
DecompAtt
word2vec
0.6597
0.6662
ESIM
fastText
0.7033
0.7116
HBMP
word2vec
0.6617
0.6604
ULMFiT
Learned
0.7281
0.7244
BERT
ParsBERT
0.8081
0.8299
mBERT
0.8263
0.8338
representations including word2vec, fastText, and ELMo, we computed a tf-
idf-weighted average of these word representations for each sentence. Note
that the reported test accuracies are for models trained on both training and
validation sets using the hyper-parameters tuned based on the validation set.
For brevity, we just report the result of one representation for DecompAtt,
ESIM, and HBMP. In the ESIM and HBMP methods, all representations ob-
tained almost similar accuracies; while in the DecompAtt method, word2vec
considerably outperformed other embeddings.
According to Table 3, the
BERT models obtained the best accuracies with a large margin compared to
other models. Between ParsBERT and mBERT, the latter shows a slightly
better performance. Anyway, this 83.38% test accuracy shows that there is a
big room for improving the current methods to be useful for real-world NLP
applications in diﬀerent languages.
To provide a more detailed view of the performance of diﬀerent models,
Fig. 3 shows the confusion matrices of six best performing ones. According
to this ﬁgure, the most diﬃcult class for all methods is contradiction that is
14

--- Page 15 ---

confused more with entailment than neutral. This is because distinguishing a
contradiction situation, especially from an entailment one, needs higher levels
of natural language understanding than superﬁcial pattern recognition.
On the other hand, the neutral class is the simplest one because many
neutral samples can be easily identiﬁed by simple patterns like the overlap
between their premise and hypothesis. This is compatible with the statistics
presented in Table 2 where the overlap between premises and hypotheses
in the neutral class is clearly diﬀerent from that in the other two classes.
Obviously, the performance of the models that rely on such superﬁcial clues
can degrade in out-of-distribution situations.
The next section is a step
towards investigating these biases in the FarsTail dataset.
4.3. Dataset bias
Dataset bias includes correlations between input data and target values
which are not generalizable to real-world instances. For example, negation
words like nobody, no, never, and nothing in some NLI datasets like SNLI
and MultiNLI are strongly correlated with the contradiction class [34]. Deep
models tend to exploit these clues to solve the dataset instead of the intended
task.
Therefore, even though they obtain high in-distribution accuracies,
their performance drops signiﬁcantly for out-of-distribution data [35].
In
this section, we investigate the available biases in the FarsTail dataset.
To identify the words associated with diﬀerent inference classes, the point-
wise mutual information (PMI) is computed between each word and class in
the training set hypotheses:
PMI(word, class) = log
p(word, class)
p(word, .)p(., class).
As in [34, 36], we apply add-100 smoothing to the raw statistics. Table 4
shows the top ten words by PMI(word, class) in FarsTail as well as MultiNLI
and SciTail for comparison. The table also reports the ratio of instances of
each word belonging to the speciﬁed class. FarsTail shows lower PMI values
and lower occurrence number of these superﬁcial clues compared to the other
two datasets. In addition, the top words by PMI in FarsTail belong to a wider
range of classes.
Even though we tried to keep the annotation clues low by reducing the
amount of task-speciﬁc human-generated texts, some of these biases emerged
in FarsTail hypotheses. For example, the words “”تنهاand “( ”فقطonly) have
15

--- Page 16 ---

Entailment
Neutral
Contradiction
True labels
401
39
79
45
408
82
203
74
233
DecompAtt + word2vec
362
48
109
15
460
60
149
70
291
ESIM + fastText
50
100
150
200
250
300
350
400
450
Entailment
Neutral
Contradiction
True labels
306
75
138
22
454
59
112
125
273
HBMP + word2vec
370
30
119
32
445
58
122
70
318
ULMFiT
50
100
150
200
250
300
350
400
Entailment
Neutral
Contradiction
Predicted labels
Entailment
Neutral
Contradiction
True labels
449
11
59
10
468
57
88
41
381
ParsBERT
Entailment
Neutral
Contradiction
Predicted labels
428
14
77
9
484
42
73
45
392
mBERT
100
200
300
400
Figure 3: Confusion matrices of diﬀerent models on the FarsTail test set.
16

--- Page 17 ---

Table 4: The top ten words by PMI(word,class) in three datasets. The Counts column
shows how many of the instances of each word occur in hypotheses belong to the speciﬁed
class.
Word
Class
PMI
Counts
MultiNLI
never
Contradiction
0.852
6599/8363
no
Contradiction
0.820
12499/16515
nothing
Contradiction
0.775
2090/2758
any
Contradiction
0.735
5430/7739
none
Contradiction
0.681
553/702
anything
Contradiction
0.668
2239/3336
completely
Contradiction
0.664
855/1190
also
Neutral
0.644
1845/2726
refused
Contradiction
0.644
401/498
nobody
Contradiction
0.603
612/881
SciTail
to
Neutral
0.488
3541/5266
have
Neutral
0.481
845/1155
the
Neutral
0.479
14194/21758
deﬁnite
Entailment
0.478
144/146
because
Neutral
0.466
571/749
system
Neutral
0.461
654/885
.
Neutral
0.454
14790/23261
a
Neutral
0.451
6086/9514
oﬀ
Neutral
0.437
7644/12162
and
Neutral
0.430
2771/4352
FarsTail
:
Neutral
0.244
95/158
"
Entailment
0.227
466/1053
"
Contradiction
0.222
463/1053
( تنهاonly)
Contradiction
0.221
61/87
( باشدbe)
Contradiction
0.202
202/440
( نیزalso)
Neutral
0.179
50/76
( فقطonly)
Contradiction
0.168
38/50
( خودself)
Neutral
0.163
143/319
( بعدafter)
Contradiction
0.162
74/144
( اثرwork,eﬀect)
Entailment
0.159
70/135
17

--- Page 18 ---

been used to conﬁne the general point presented in the premise to make a
contradicting hypothesis as in the following instance:
ﻣﻘﺪم
: ﯾﮑﯽ از ﻣﻄﺎﻟﺒﯽ ﮐﻪ در ﭘﯿﺎم ﻫﻤﻪ ﭘﯿﺎﻣﺒﺮان ﺗﮑﺮار ﺷﺪه اﺳﺖ اﯾﻦ اﺳﺖ ﮐﻪ: ﻣﻦ اﺟﺮ و ﻣﺰدي از ﺷﻤﺎ ﻧﻤﯽ
ﺧ.ﻮاﻫﻢ 
Premise: One of the things that is repeated in the message of all the prophets is: I do not 
ask you for a reward. 
ﺗﺎﻟﯽ :ﺗﻨﻬﺎ 
 ﺣﻀﺮت
ﻋﯿﺴﯽ 
 ﺑﻪ اﻣﺖ ﺧﻮد
ﻓﺮﻣﻮده
اﻧﺪ ﻣﻦ از ﺷﻤﺎ اﺟﺮ و ﻣﺰدي ﻧﻤﯽ .ﺧﻮاﻫﻢ 
reward.
 
do not ask you for a
 
Jesus said to his people that I
 
Only
: 
Hypothesis
As another approach for investigating dataset biases, we evaluated two
biased models which classiﬁed instances based on incomplete input data.
The classiﬁcation accuracy of these models gives an estimate of the degree
to which the superﬁcial clues can be exploited by the learning algorithms.
Inspired from [34, 37], we ﬁrst investigated a hypothesis-only model by ﬁne-
tuning the mBERT model on the hypotheses to predict the entailment labels
without seeing the premises. The model obtained an accuracy of 55.31% on
the test set. The corresponding confusion matrix presented in Fig. 4 shows
that the main success of the hypothesis-only model has been in the neutral
class, with the entailment and contradiction classes in the next places.
In the second biased model, we used the cosine similarity between the bag-
of-word count vectors of the premise and hypothesis as the input feature to
investigate the ability of a model in deciding about the inference relationship
just exploiting the similarity between the premise and hypothesis. An SVM
classiﬁer trained on this input feature obtained an accuracy of 56.46% on the
test set. Fig. 4 shows that this model has obtained a good performance in
distinguishing the neutral class from the other two classes. This is compatible
with the overlap statistics presented in Table 2 where the overlap between
premises and hypotheses in the neutral class is clearly diﬀerent from that in
the other two classes. On the other hand, the worst performance of this biased
model has been in the contradiction class where the model has performed near
random. This is because contradiction needs a higher level of inference to be
determined.
According to whether or not the test samples were correctly classiﬁed
by each of the biased models, we partitioned the FarsTail test set into two
subsets (for each biased model): easy and hard. Two binary columns added to
the test set, denoted as hard(hypothesis) and hard(overlap), indicate whether
or not each sample belongs to the hard subset based on the hypothesis-only
and overlap-based biased models, respectively.
Comparing these subsets,
18

--- Page 19 ---

Entailment
Neutral
Contradiction
Predicted labels
Entailment
Neutral
Contradiction
True labels
290
109
120
100
343
92
158
120
232
Hypothesis-only
Entailment
Neutral
Contradiction
Predicted labels
293
92
134
30
421
84
185
156
169
Overlap-based
50
100
150
200
250
300
350
400
Figure 4: Confusion matrices of the biased models on the FarsTail test set.
497 (32%) test samples are easy for both biased models, while 313 (20%)
samples are hard for both. On the other hand, 386 (25%) and 368 (23%)
test samples are hard just for the hypothesis-only and overlap-based biased
models, respectively. Obviously, these two models capture diﬀerent biased
patterns in the dataset since nearly half of the samples are easy for one model
and hard for the other.
The introduction of these subsets of the test set allows for a more pre-
cise evaluation of the developed models. As an example, Table 5 shows the
detailed performance of some models on diﬀerent FarsTail test subsets. As
expected, all models were more successful in classifying easy samples. This
shows the previously known fact that a part of the models’ success in recog-
nizing textual entailment is due to their exploitation of available biases in the
dataset [34]. Also, comparing the results obtained for the subsets respective
to the two biased models shows that the models’ accuracy on the hard subset
obtained by the overlap-based biased model is usually lower than that of the
hypothesis-only biased model. This reveals that the models exploit more of
the overlap information between premises and hypotheses than the biased
patterns in the hypotheses. Obviously, these models will have diﬃculty in
classifying samples that come from a diﬀerent distribution. We consider the
construction of out-of-distribution challenge sets for the FarsTail dataset as
a future work.
19

--- Page 20 ---

Table 5: Accuracy of diﬀerent models on diﬀerent subsets of the FarsTail test set.
Hypothesis-only
Overlap-based
Model
Full
Easy
Hard
Easy
Hard
DecompAtt (word2vec)
0.6662
0.7341
0.5823
0.7633
0.5404
HBMP (word2vec)
0.6604
0.7618
0.5350
0.7565
0.5360
ESIM (fastText)
0.7116
0.7931
0.6109
0.8120
0.5815
mBERT
0.8338
0.8763
0.7811
0.8981
0.7504
5. Conclusion
In this paper, we introduced, to the best of our knowledge, the ﬁrst
relatively large-scale NLI dataset for Persian language. We presented the
details of the FarsTail development process, which is carefully designed to
ensure the data quality. We also presented the dataset statistics as well as
the results of some traditional and state-of-the-art methods on it. We also
investigated the dataset biases in FarsTail.
Due to the usage of multiple-choice questions in developing the FarsTail
dataset, these questions along with their corresponding premises can also be
exploited in the machine reading comprehension (MRC) task. In the future,
we plan to present this MRC dataset as a byproduct of FarsTail. We also
consider developing Persian NLI challenge sets as a future work to establish
a benchmark for evaluating the models’ out-of-distribution performance.
Since the best obtained result on the FarsTail test set, using the powerful
BERT method, is 83.38%, we hope it invokes more research on developing
methods which are applicable to real-world NLP tasks in diﬀerent languages,
specially data-poor ones.
References
[1] V. Yadav, S. Bethard, A survey on recent advances in named entity
recognition from deep learning models, in: Proceedings of the 27th In-
ternational Conference on Computational Linguistics, 2018, pp. 2145–
2158.
[2] A. Keramatfar, H. Amirkhani, Bibliometrics of sentiment analysis liter-
ature, Journal of Information Science 45 (1) (2019) 3–15.
20

--- Page 21 ---

[3] S. Yang, Y. Wang, X. Chu, A survey of deep learning techniques for
neural machine translation (2020). arXiv:2002.07526.
[4] R. Baradaran, R. Ghiasi, H. Amirkhani, A survey on machine reading
comprehension systems (2020). arXiv:2001.01582.
[5] B. MacCartney, Natural language inference, Ph.D. thesis, Stanford Uni-
versity (2009).
[6] D. W. Otter, J. R. Medina, J. K. Kalita, A survey of the usages of deep
learning for natural language processing, IEEE Transactions on Neural
Networks and Learning Systems (2020) 1–21.
[7] T. Young, D. Hazarika, S. Poria, E. Cambria, Recent trends in deep
learning based natural language processing, IEEE Computational Intel-
ligence Magazine 13 (3) (2018) 55–75.
[8] S. R. Bowman, G. Angeli, C. Potts, C. D. Manning, A large annotated
corpus for learning natural language inference, in: Proceedings of the
2015 Conference on Empirical Methods in Natural Language Processing,
2015, pp. 632–642.
[9] A. Conneau, G. Lample, R. Rinott, A. Williams, S. R. Bowman,
H. Schwenk, V. Stoyanov, XNLI: Evaluating cross-lingual sentence rep-
resentations, in: Proceedings of the 2018 Conference on Empirical Meth-
ods in Natural Language Processing, 2018, pp. 2475–2485.
[10] T. Khot, A. Sabharwal, P. Clark, SciTail: A textual entailment dataset
from science question answering, in: Thirty-Second AAAI Conference
on Artiﬁcial Intelligence, 2018, pp. 5189–5197.
[11] T. Mikolov, I. Sutskever, K. Chen, G. S. Corrado, J. Dean, Distributed
representations of words and phrases and their compositionality, in: Ad-
vances in neural information processing systems, 2013, pp. 3111–3119.
[12] P. Bojanowski, E. Grave, A. Joulin, T. Mikolov, Enriching word vectors
with subword information, Transactions of the Association for Compu-
tational Linguistics 5 (2017) 135–146.
21

--- Page 22 ---

[13] M. E. Peters, M. Neumann, M. Iyyer, M. Gardner, C. Clark, K. Lee,
L. Zettlemoyer, Deep contextualized word representations, in: Proceed-
ings of the 2018 Conference of the North American Chapter of the Asso-
ciation for Computational Linguistics: Human Language Technologies,
Volume 1 (Long Papers), 2018, pp. 2227–2237.
[14] J. Devlin, M.-W. Chang, K. Lee, K. Toutanova, BERT: Pre-training
of deep bidirectional transformers for language understanding, in: Pro-
ceedings of the 2019 Conference of the North American Chapter of the
Association for Computational Linguistics: Human Language Technolo-
gies, Volume 1 (Long and Short Papers), 2019, pp. 4171–4186.
[15] M. Artetxe, H. Schwenk, Massively multilingual sentence embeddings
for zero-shot cross-lingual transfer and beyond, Transactions of the As-
sociation for Computational Linguistics 7 (2019) 597–610.
[16] A. P. Parikh, O. T¨ackstr¨om, D. Das, J. Uszkoreit, A decomposable
attention model for natural language inference, in: Proceedings of the
2016 Conference on Empirical Methods in Natural Language Processing,
2016, pp. 2249–2255.
[17] Q. Chen, X. Zhu, Z. Ling, S. Wei, H. Jiang, D. Inkpen, Enhanced LSTM
for natural language inference, in: Proceedings of the 55th Annual Meet-
ing of the Association for Computational Linguistics (Volume 1: Long
Papers), 2017, pp. 1657–1668.
[18] A. Talman, A. Yli-Jyr¨a, J. Tiedemann, Sentence embeddings in NLI
with iterative reﬁnement encoders, Natural Language Engineering 25 (4)
(2019) 467–482.
[19] J. Howard, S. Ruder, Universal language model ﬁne-tuning for text clas-
siﬁcation, in: Proceedings of the 56th Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Papers), 2018, pp. 328–
339.
[20] D. Khashabi, A. Cohan, S. Shakeri, P. Hosseini, P. Pezeshkpour,
M. Alikhani, M. Aminnaseri, M. Bitaab, F. Brahman, S. Ghazarian,
et al., ParsiNLU: A suite of language understanding challenges for per-
sian, arXiv preprint arXiv:2012.06154 (2020).
22

--- Page 23 ---

[21] A. Williams, N. Nangia, S. R. Bowman, A broad-coverage challenge
corpus for sentence understanding through inference, in: Proceedings of
the 2018 Conference of the North American Chapter of the Association
for Computational Linguistics: Human Language Technologies, Volume
1 (Long Papers), 2018, pp. 1112–1122.
[22] M. Marelli, L. Bentivogli, M. Baroni, R. Bernardi, S. Menini, R. Zam-
parelli, SemEval-2014 Task 1: Evaluation of compositional distributional
semantic models on full sentences through semantic relatedness and tex-
tual entailment, in: Proceedings of the 8th International Workshop on
Semantic Evaluation (SemEval 2014), Dublin, Ireland, 2014, pp. 1–8.
[23] A. Romanov, C. Shivade, Lessons from natural language inference in the
clinical domain, in: Proceedings of the 2018 Conference on Empirical
Methods in Natural Language Processing, 2018, pp. 1586–1596.
[24] A. E. Johnson, T. J. Pollard, L. Shen, L.-w. H. Lehman, M. Feng,
M. Ghassemi, B. Moody, P. Szolovits, L. Anthony Celi, R. G. Mark,
MIMIC-III, a freely accessible critical care database, Scientiﬁc data 3 (1)
(2016) 1–9.
[25] D. Demszky, K. Guu, P. Liang, Transforming question answering
datasets into natural language inference datasets (2018). arXiv:1809.
02922.
[26] P. Rajpurkar, R. Jia, P. Liang, Know what you don’t know: Unanswer-
able questions for SQuAD, in: Proceedings of the 56th Annual Meeting
of the Association for Computational Linguistics (Volume 2: Short Pa-
pers), 2018, pp. 784–789.
[27] J. Bos, F. M. Zanzotto, M. Pennacchiotti, Textual entailment at evalita
2009, Proceedings of EVALITA 2009 2 (6.4) (2009) 1–7.
[28] M. Alabbas, A dataset for Arabic textual entailment, in: Proceedings
of the Student Research Workshop associated with RANLP 2013, 2013,
pp. 7–13.
[29] K. Eichler, A. Gabryszak, G. Neumann, An analysis of textual inference
in German customer emails, in: Proceedings of the Third Joint Confer-
ence on Lexical and Computational Semantics (*SEM 2014), 2014, pp.
69–74.
23

--- Page 24 ---

[30] E. R. Fonseca, L. Borges dos Santos, M. Criscuolo, S. M. Alu´ısio,
Overview of the evaluation of semantic similarity and textual inference,
Linguam´atica 8 (2) (2016) 3–13.
[31] H. Hu, K. Richardson, L. Xu, L. Li, S. K¨ubler, L. S. Moss, OCNLI: Orig-
inal chinese natural language inference, in: Proceedings of the 2020 Con-
ference on Empirical Methods in Natural Language Processing: Find-
ings, 2020, pp. 3512–3526.
[32] T. Wolf, L. Debut, V. Sanh, J. Chaumond, C. Delangue, A. Moi, P. Cis-
tac, T. Rault, R. Louf, M. Funtowicz, et al., HuggingFace’s Trans-
formers: State-of-the-art natural language processing, arXiv preprint
arXiv:1910.03771 (2019).
[33] M. Farahani, M. Gharachorloo, M. Farahani, M. Manthouri, ParsBERT:
Transformer-based model for persian language understanding, arXiv
preprint arXiv:2005.12515 (2020).
[34] S. Gururangan, S. Swayamdipta, O. Levy, R. Schwartz, S. R. Bowman,
N. A. Smith, Annotation artifacts in natural language inference data,
in: Proceedings of the 2018 Conference of the North American Chap-
ter of the Association for Computational Linguistics: Human Language
Technologies, Volume 2 (Short Papers), 2018, pp. 107–112.
[35] R. T. McCoy, E. Pavlick, T. Linzen, Right for the wrong reasons: Di-
agnosing syntactic heuristics in natural language inference, in: 57th
Annual Meeting of the Association for Computational Linguistics, ACL
2019, Association for Computational Linguistics (ACL), 2020, pp. 3428–
3448.
[36] S. R. Bowman, J. Palomaki, L. B. Soares, E. Pitler, New protocols and
negative results for textual entailment data collection., in: EMNLP (1),
2020, pp. 8203–8214.
[37] A. Poliak, J. Naradowsky, A. Haldar, R. Rudinger, B. Van Durme, Hy-
pothesis only baselines in natural language inference, in: Proceedings of
the Seventh Joint Conference on Lexical and Computational Semantics,
2018, pp. 180–191.
24

```
