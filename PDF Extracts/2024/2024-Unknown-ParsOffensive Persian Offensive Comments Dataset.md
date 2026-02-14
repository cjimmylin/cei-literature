---
title: "2024-Unknown-ParsOffensive Persian Offensive Comments Dataset - PDF Extract"
source_pdf: "2024-Unknown-ParsOffensive Persian Offensive Comments Dataset.pdf"
pages: 16
extracted_at: "2026-02-14T01:31:36.266863"
---

# PDF Extract: 2024-Unknown-ParsOffensive Persian Offensive Comments Dataset

**Source PDF:** 2024-Unknown-ParsOffensive Persian Offensive Comments Dataset.pdf
**Total Pages:** 16

---

## Content

```
--- Page 1 ---

OPSD: an Offensive Persian Social media Dataset
and its baseline evaluations
Mehran Safayani1*, Amir Sartipi2, Amir Hossein Ahmadi1,
Parniyan Jalali1, Amir Hossein Mansouri1,
Mohammadamir Bisheh-Niasar3, Zahra Pourbahman4
1Department of Electrical and Computer Engineering, Isfahan
University of Technology, Isfahan 84156-83111, Iran.
2Faculty of Computer Engineering, University of Isfahan, Isfahan, Iran.
3Department of Industrial Engineering, Sharif University of Technology,
Tehran, Iran.
4 Computer Engineering Department, Amirkabir University of
Technology (Tehran Polytechnic), No. 350, Hafez Ave, Tehran
1591634311, Iran.
*Corresponding author(s). E-mail(s): safayani@iut.ac.ir;
Contributing authors: amirsartipi.msc@eng.ui.ac.ir;
amir ahmadi@ec.iut.ac.ir; p.jalali@ec.iut.ac.ir; a.mansouri@ec.iut.ac.ir;
ma bishehniasar@ie.sharif.edu; pourbahman@aut.ac.ir;
Abstract
Warning This paper includes a sample of comments extracted from the dataset,
some of which may contain offensive or obscene content.
The proliferation of hate speech and offensive comments on social media has
become increasingly prevalent due to user activities. Such comments can have
detrimental effects on individuals’ psychological well-being and social behav-
ior. While numerous datasets in the English language exist in this domain, few
equivalent resources are available for Persian language. To address this gap, this
paper introduces two offensive datasets. The first dataset comprises annotations
provided by domain experts, while the second consists of a large collection of unla-
beled data obtained through web crawling for unsupervised learning purposes. To
ensure the quality of the former dataset, a meticulous three-stage labeling pro-
cess was conducted, and kappa measures were computed to assess inter-annotator
agreement. Furthermore, experiments were performed on the dataset using state-
of-the-art language models, both with and without employing masked language
1
arXiv:2404.05540v1  [cs.CL]  8 Apr 2024

--- Page 2 ---

modeling techniques, as well as machine learning algorithms, in order to establish
the baselines for the dataset using contemporary cutting-edge approaches. The
obtained F1-scores for the three-class and two-class versions of the dataset were
76.9% and 89.9% for XLM-RoBERTa, respectively.
Keywords: Natural Language Analysis, Text Classification, Low Resource Language,
Pre-trained Language Model, Offensive Language Detection, Social Media
1 Introduction
Social media platforms have experienced a surge in popularity in recent years, pro-
viding users with a platform to express their opinions across various forms of media.
Among these forms, textual data holds significant importance as a means of con-
veying meaning and ideas. Unfortunately, it is not uncommon for certain individuals
to incorporate abusive language within their sentences, resulting in offensive com-
ments. Detecting such instances manually would be a time-consuming and expensive
endeavor. However, thanks to advancements in Natural Language Processing (NLP)
applications, it has become possible to automatically identify and classify these com-
ments as offensive or non-offensive. This task can be approached as a classification
problem, requiring a suitable dataset consisting of sentences of this nature. Regret-
tably, to the best of our knowledge, there are only few datasets available for offensive
comment detection. Leveraging these NLP applications can prove instrumental in
filtering offensive content from social media platforms, particularly for children or
individuals who prefer not to be exposed to such material.
In this study, we collected approximately 5,000 and 17,000 comments from two
widely used social media platforms, namely Instagram and Twitter, respectively. To
ensure accurate labeling of the data, a meticulous three-phase annotation process was
employed. In addition, a collection of 170,000 unlabeled data points in Persian was
gathered using offensive keywords and hashtags. The primary contributions of this
study can be summarized as follows:
1. Introduction of the offensive Persian Social Media Dataset (OPSD).
2. Investigation of the impact of masked language modeling on pre-trained language
models using the unlabeled portion of the dataset.
3. Comprehensive experiments were conducted on the annotated dataset, involving
transformer-based language models and machine learning approaches.
The remaining sections of this article are organized as follows: Section 2 reviews
previous studies relevant to datasets in the field. Section 3 explains the data col-
lection process in detail. Section 4 discusses the annotation methodology employed.
Section 5 presents the extensive experiments conducted and the establishment of base-
lines for the dataset using transformer-based language models and machine learning
approaches. Finally, Section 6 presents the concluding remarks.
2

--- Page 3 ---

2 Related Work
In this section, we first review prior work on offensive language datasets in the English
language and then present the related literature on offensive datasets in the Persian
language.
2.1 English Offensive Datasets
The OLID [1] dataset is designed for the detection (Subtask-A), categorization
(Subtask-B), and identification of offensive language (Subtask-C). Subtask-A focuses
on binary classification with ’NOT’ and ’OFF’ labels. ’NOT’ indicates posts without
any offensive content, while ’OFF’ refers to posts that include insults, threats, profan-
ity, or swear words. The OLID dataset consists of 14,100 samples, with 13,240 samples
for training and 860 samples for testing set.
The Semi-Supervised Offensive Language Identification Dataset (SOLID) [2] was
introduced to address the scarcity of offensive language instances in the OLID
dataset and the time-consuming annotation process. SOLID utilized a semi-supervised
approach, starting with the OLID dataset, to collect new offensive data. This novel
dataset overcomes the limitations of existing datasets and provides a substantial col-
lection of English tweets for offensive language identification. SOLID demonstrates
improved offensive language detection capabilities and includes a comprehensive anal-
ysis of various types of offensive tweets. The hierarchical labeling schema used in
SOLID and related works is based on the OLID dataset.
HSOL [3] is a dataset created for the purpose of hate speech detection. The authors
began by utilizing a hate speech lexicon, which consisted of words and phrases iden-
tified as hate speech by internet users and compiled by Hatebase.org. By using the
Twitter API, they searched for tweets that contained terms from the lexicon. This pro-
cess resulted in a sample of tweets collected from 33,458 Twitter users. The authors
then extracted the timeline of each user, resulting in a corpus of 85.4 million tweets.
From this corpus, a random sample of 25,000 tweets that contained lexicon terms was
selected for manual coding by CrowdFlower (CF) workers. The workers were tasked
with labeling each tweet into one of three categories: hate speech, offensive but not
hate speech, or neither offensive nor hate speech.
2.2 Persian Offensive Datasets
The Persian Offensive Language Identification Dataset (POLID) is one of the pio-
neering datasets in this domain, developed by [4]. The dataset encompasses a diverse
range of text data, including tweets, Instagram comments, and user reviews sourced
from popular Iranian web applications such as Digikala and Snappfood. The anno-
tation process for POLID involved a semi-automatic approach. Initially, a basic list
of common swear words was used to label each text as either ”OFF” (offensive) if it
contained any of these words, or ”NOT” (inoffensive) if it did not. Subsequently, the
authors manually reviewed and corrected the labels assigned to the text data. POLID
consists of 4,988 text entities, with 2,453 labeled as inoffensive and 2,535 as offensive.
Mozafari [5] employed both random and lexicon-based sampling methods to collect
tweets from June to August 2020. In the random sampling approach, tweets were
3

--- Page 4 ---

selected randomly and evaluated by two experts. The analysis revealed that only a
maximum of 2% of the selected tweets contained offensive content, resulting in an
imbalanced sampling. On the other hand, the lexicon-based sampling involved the
utilization of a word list to filter tweets, ensuring a more unbiased representation across
different topics. The random sampling yielded 320,000 tweets, while the lexicon-based
sampling resulted in 200,000 tweets. Approximately 6,000 of the collected tweets were
manually annotated.
The PerBOLD dataset [6] focuses on the acquisition and annotation process for
building a dataset aimed at automatic detection of offensive speech on Instagram.
Two approaches were employed to collect textual data: a user-based approach tar-
geting controversial users’ pages and a news agencies-based approach focusing on
comments published on news agency pages. Due to restrictions imposed by Insta-
gram, data extraction was conducted partially from the platform itself and partially
from the picuki website. The collected data underwent an annotation process, taking
into consideration the subjective nature of offensiveness and the necessity for accu-
rate tagging. A sample of approximately 30,000 comments was randomly selected
and labeled by three annotators, with the involvement of a linguist expert to resolve
any inconsistencies. The annotators classified comments as offensive, non-offensive, or
advertisement, while offensive comments were further categorized into various types
such as curse, insult, sexist, racist, and more. This work underscores the significance of
precise tagging for effective machine learning classifiers. Overall, the paper highlights
the challenges and methodologies involved in creating a dataset for offensive speech
detection on Instagram.
Pars-OFF [7] is a comprehensive annotated corpus comprising 10,563 data samples
for offensive language detection in Persian. To ensure balance in the dataset, a combi-
nation of similarity-based and keyword-based data selection techniques were employed
during the collection of tweets. Additionally, this paper presents an evaluation of tra-
ditional machine learning approaches and Transformer-based models on the Pars-OFF
dataset as a baseline. The BERT+fastText model achieved the highest performance,
attaining an impressive F1-Macro score of 89.57%.
3 Data collection
In this section, we introduce OPSD and delve into how the dataset was collected and
annotated. This section describes the data collection process for OPSD (Twitter),
OPSD (Instagram), and also OPSD (Unlabeled), as demonstrated in Subsections 3.1,
3.2, and 3.3, respectively.
3.1 OPSD (Twitter)
To collect data from Persian Twitter, a list of keywords was compiled by inspecting
trending hashtags and topics known to contain a higher percentage of offensive content.
Over 40,000 records were extracted by searching for these keywords. An initial pre-
processing step was conducted to remove records from company support accounts
and eliminate duplicates. From each keyword, a subset containing more than 16,000
4

--- Page 5 ---

records was sampled. Finally, these samples were aggregated to form a dataset of
17,000 records.
3.2 OPSD (Instagram)
The data collection process for OPSD (Instagram) involved crawling over 13,000
records from the Instagram platform. Specifically, a set of 100 comments from different
posts was extracted from the accounts of an IT service company. Upon examination,
it was discovered that a significant amount of the collected data was unusable. There-
fore, an initial pre-processing step was carried out to remove records that contained
less than one Persian word, after removing emojis, emoticons, hashtags, mentions,
links, and all non-Persian text. Due to the diverse nature of the posts and the evenly
distributed number of collected data from each post, a sample of 5,000 records was
extracted from the crawled data.
3.3 OPSD (Unlabeled)
The OPSD (Unlabeled) dataset was collected following a similar procedure as
described in Subsection 3.1. In this case, a collection of over 140,000 tweets were
crawled from Twitter. An initial pre-processing step similar to previous datasets was
applied. Finally, these records formed the OPSD (Unlabeled) dataset.
4 Annotation
The OPSD dataset is annotated with three labels, which are defined as follows:
• POS (Positive): A comment is labeled as POS if it does not contain any destructive
concepts, such as hate speech, offensive language, or abusive content.
• T-NEG (Targeted Negative): Comments with the T-NEG label specifically target
individuals, companies, or organizations with hateful and offensive content.
• NT-NEG (Non-Targeted Negative): These comments contain hateful and offensive
terms without any identifiable target.
4.1 Annotation Process
The annotation process for this study consists of three phases, involving five differ-
ent annotators. In the first phase, the data were divided into five parts, and each
part was annotated by two annotators. The Cohen’s kappa score was then calculated
between the two annotators. If the Cohen’s kappa score was below 75%, indicating
poor agreement, the process moved to the second phase.
In the second phase, a consensus meeting was conducted to discuss the reasons
behind the poor results. Based on the discussions, the annotation guidelines were
modified as necessary. The annotators then re-labeled the data on which they had
disagreed in the previous phase.
Once the inter-annotator agreement reached a minimum threshold of 75%, the
process moved to the third phase. In this phase, any remaining points of disagreement
were resolved by a third annotator. The final label for each data point was determined
based on the majority vote among the annotators.
5

--- Page 6 ---

Figure 1 provides an overview of the annotation process.
Fig. 1 The annotation process
4.2 Annotation Reliability
The annotation reliability in this study was assessed using Cohen’s kappa coefficient.
Cohen’s kappa measures the agreement between annotators beyond what would be
expected by chance.
Cohen’s kappa is calculated as follows:
κ = po −pe
1 −pe
(1)
where po is the percentage of observed agreement between annotators and pe is the
percentage of agreement expected by chance.
Two cases of labels were considered for calculating Cohen’s kappa. The first case
involved the 3-class labeling, where each class of data was assigned a unique label. For
6

--- Page 7 ---

the NEG+ case, which was used for binary classification, the NT-NEG and T-NEG
labels were combined.
It is important to note that we combined two separate OPSD datasets, namely
OPSD (Twitter) and OPSD (Instagram), and subsequently annotated the combined
OPSD dataset.
Table 1 provides the Kappa scores for the OPSD dataset. The Phase column repre-
sents the first and the second phase of the labeling process. The Part column refers to
five parts of the dataset, where each was annotated by two different annotators. The
Annotator column indicates the five different annotators involved in the labeling pro-
cess. The next three columns denote the number of comments labelled for each class.
The Total and Common columns show the number of comments in each part, and the
number of comments for which the annotators agreed on the label, respectively. Addi-
tionally, the Difference column indicates the number of differences in labeling between
the two annotators. Lastly, the last column shows the Kappa score, considering the
three classes, for each part of the dataset.
Phase
Part
Annotator
POS
NT-NEG
T-NEG
Total
Common
Difference
κ3−class
I
A
Annotator1
3262
126
923
4311
3761
550
0.681
Annotator2
3151
239
921
B
Annotator2
3113
300
904
4317
3672
645
0.626
Annotator3
3318
51
948
C
Annotator3
3138
141
960
4239
3696
543
0.698
Annotator4
2900
40
1299
D
Annotator4
2809
113
1075
3997
3611
386
0.769
Annotator5
2973
158
866
E
Annotator5
3191
61
1049
4301
3924
377
0.781
Annotator1
3122
118
1061
II
A
Annotator1
3230
129
952
4311
4095
216
0.874
Annotator2
3178
189
944
B
Annotator2
3183
194
940
4317
4044
273
0.839
Annotator3
3273
83
961
C
Annotator3
3075
147
1017
4239
4121
118
0.933
Annotator4
3069
150
1020
D
Annotator4
2878
147
972
3997
3828
169
0.899
Annotator5
2889
159
949
E
Annotator5
3201
106
994
4301
4166
135
0.922
Annotator1
3133
124
1044
Table 1 Kappa score of the OPSD dataset for each phase and each part
The average agreement scores per annotation phase are presented in Table 2. This
table provides information on the number of instances for each label in each phase, the
number of agreements and disagreements between annotators, and the average kappa
score for the five parts of the dataset.
7

--- Page 8 ---

Phase
Total
Common
Difference
κ3−class
I
21165
18664
2501
0.711
II
21165
20254
911
0.8934
Table 2 The number of each label and average Kappa scores of OPSD dataset in two phases of
labeling process.
Table 3, presents a selection of example samples from the dataset, showcasing the
Persian text associated with each label.
Label
Comment
POS
For about a year now, the internet quality of Irancell has deteriorated
significantly, to the point that I no longer use it.
POS
What is this previous debt on the Hamrah Aval (MCI) bill? For
each billing cycle that you have an internet plan, the bill shows the
outstanding balance from the previous month, which you pay along
with the current month’s charges.
POS
Hamrah Aval (MCI) has become quite burdensome with its expensive
packages lately ... Come on, have a little mercy on people’s situation.
NT-NEG
I see the gathering of foolish rulers here, don’t they have your national
code to ask you to enter it?
NT-NEG
Is your internet speed also sluggish?
NT-NEG
He’s expelled his essence, yet you’re still recharging; you pour out
more of him, the stench of his putrefaction spreads, and it contami-
nates everything around.
T-NEG
The shameless ones have deleted the unlimited package.
T-NEG
I need to go to the bathroom; the package doesn’t work without
electricity. My phone’s battery is at 4%, the modem is off, and Irancell
hasn’t left any balance. In the parking lot, the gate doesn’t open
without power, and my car is inside the parking lot, and I can’t do
anything. Curse your head and your nonsense.
T-NEG
Your driving is awful, people of Tabriz... I don’t know about other
cities, but I hope it’s not as bad as this. If it is, even the ISIS gov-
ernment would be better for you.
Table 3 Examples of the OPSD dataset for each label.
4.3 Data Analysis
As previously mentioned, a total of 21,165 comments were collected and categorized
into Positive, Targeted Negative, and Non-Targeted Negative. The distribution of these
tags among the comments is illustrated in Figure 2 and the specific counts for each
class are provided in Table 4
After a pre-processing step, which involved normalization and removal of numbers,
URLs, email addresses, and special characters, the distribution of comments length
8

--- Page 9 ---

Fig. 2 The distribution of labels
Class Name
Class Tag
Class Count
POS
1
15436
NT-NEG
0
654
T-NEG
-1
5075
Table 4 Number of Each Class in the OPSD dataset with Class Tags.
(number of tokens) excluding emojis is presented in Figure 3. The distribution of
comment lengths reveals a prominent skew towards shorter texts, which coincides with
the prevailing observation concerning comments in social media platforms.
Moreover, the unprocessed OPSD (unlabeled) data also aligns with the same trend,
as illustrated in Figure 4.
5 Experiments
We trained a classifier and compared multiple models using both supervised and
unsupervised approaches. In supervised methods, we utilize machine learning and
Transformer-based models, while in unsupervised methods, we employ a masked
language model (MLM).
The dataset used in our classification experiments contains 21,165 entries and
is split into a training set (80%), development set (10%), and test set (10%).
Hyperparameters are tuned on the development set.
We employed several machine learning methods, which served as baseline text
categorization models. The feature vectors were constructed using the TF-IDF and
Count Vectorizer methods. The results of applying these methods on the test data are
presented in Table 5.
9

--- Page 10 ---

Fig. 3 Word-level distribution of comments length for the OPSD dataset.
The logistic regression [8] model was utilized with a regularization parameter (C)
set to 1e −9. K-Nearest Neighbors (KNN) algorithm [8] used 3 neighbors for clas-
sification, and the distance metric chosen was the Euclidean distance. We utilized
the SVM algorithm [8] with a Radial Basis Function (RBF) kernel. The regulariza-
tion parameter (C) was set to 0.025, and the gamma value was determined using the
’scale’ method. We employed a single decision tree [8] for classification. The maximum
depth of the tree was set to None, allowing nodes to expand until all leaves were pure
or contained a minimum number of samples required for splitting, and the minimum
samples required to split a node was set to 2. For the Random Forest Classifier [8],
we employed 200 decision trees as estimators. The maximum depth of the trees was
not restricted (None), and the minimum number of samples required to split a node
was set to 2. The Gaussian Naive Bayes algorithm [8] assumes that features follow a
Gaussian distribution. It is particularly useful for continuous features. As it doesn’t
have any hyperparameters to tune, we used it with its default settings.
In our experimental analysis, we employed the following transformer-based mod-
els, including multilingual and monolingual models, to comprehensively explore their
respective performances and capabilities.
ParsBERT
ParsBERT [9] is a monolingual language model based on the BERT [10] architecture.
It is pre-trained on more than 3.9 million Persian documents, allowing it to capture
contextual representations of Persian text.
10

--- Page 11 ---

Fig. 4 Word-level distribution of comments length for the OPSD dataset (unlabeled).
NEG+
3-Class
Feature Extraction Method
Model Name
Acc
F1
Acc
F1
Count Vectorizer
LogisticRegression
0.719
0.420
0.719
0.280
KNeighborsClassifier
0.830
0.741
0.829
0.509
SVC
0.750
0.528
0.751
0.361
DecisionTreeClassifier
0.866
0.831
0.860
0.682
RandomForestClassifier
0.885
0.849
0.879
0.617
GaussianNB
0.513
0.511
0.523
0.399
TF-IDF Vectorizer
LogisticRegression
0.719
0.418
0.719
0.279
KNeighborsClassifier
0.748
0.523
0.748
0.356
SVC
0.726
0.443
0.726
0.297
DecisionTreeClassifier
0.867
0.834
0.847
0.643
RandomForestClassifier
0.879
0.839
0.875
0.614
GaussianNB
0.504
0.499
0.509
0.385
Table 5 Results of applying some machine learning methods on the test set
ALBERT
ALBERT [11] is a ”Lite” version of BERT designed to improve memory efficiency. It
employs parameter-reduction techniques such as dividing the embedding matrix into
smaller matrices and using shared parameters across different BERT hidden layers.
ALBERT-fa [12] is a monolingual language model based on the ALBERT architecture,
specifically trained on Persian data.
11

--- Page 12 ---

RoBERTa
RoBERTa [13] is a variant of the BERT model that employs a larger training
dataset and longer training duration to capture more extensive language representa-
tions. It removes the next sentence prediction objective used in BERT and utilizes
dynamic masking during pretraining. RoBERTa-fa 1 is a variant of RoBERTa trained
specifically on Persian data.
XLM-RoBERTa (XLM-R) [14] is a variant of RoBERTa that incorporates cross-
lingual language modeling capabilities. It is designed for multilingual tasks, enabling
effective understanding and processing of text in multiple languages. XLM-RoBERTa
leverages pre-training on large-scale multilingual corpora to capture cross-lingual
knowledge.
For the fine-tuning of these models, we added a fully-connected layer to the pre-
trained model. We used weighted cross-entropy loss as the objective function, a batch
size of 32, a maximum sequence length of 128, a learning rate of 5e −6, a dropout
rate of 0.5, and the number of epochs 10. The AdamW [15] optimizer with a linear
learning rate scheduler (without warm-up steps) was used.
To further enhance the model’s performance, we conducted an extensive hyperpa-
rameter tuning process. We experimented with various hyperparameter configurations,
exploring batch size ∈{8, 16, 32}, maximum sequence length ∈{64, 128}, learning rate
∈{2e −5, 1e −5, 9e −6, 5e −6, 1e −6}, and dropout rate in the range of [0.3 −0.8].
Through this thorough grid search approach, we aimed to find the most suitable
hyperparameters for our specific task.
After conducting the hyperparameter tuning, we found that the initial hyperpa-
rameter values provided the best performance on our evaluation metrics. Consequently,
we decided to retain these hyperparameters for the final training of models.
To evaluate models on the dataset, we used a multilingual model and three mono-
lingual models that are specifically pre-trained on Persian data. According to table 6,
XLM-RoBERTa has performed best accuracy and F1-score on the test data in both
NEG+ and 3-class.
NEG+
3-Class
Acc
F1
Acc
F1
ALBERT-fa
0.910
0.890
0.891
0.763
ParsBERT
0.904
0.883
0.887
0.726
RoBERTa-fa
0.908
0.885
0.902
0.741
XLM-RoBERTa
0.917
0.899
0.907
0.769
Table 6 Results on the test set in fine-tuning phase for each pre-trained language model
Masked Language Model
In this section, we present an experiment conducted to investigate the effects of addi-
tional training of LLMs using OPSD (unlabeled) data. Specifically, the approach
1https://huggingface.co/HooshvareLab/roberta-fa-zwnj-base
12

--- Page 13 ---

involved training the LLM with OPSD (unlabeled) through Masked Language Mod-
eling (MLM) 2. Subsequently, the LLM was trained on Sentiment Analysis task (SA)
using OPSD (labeled) data to observe potential improvements.
The ALBERT-fa, ParsBERT, RoBERTa-fa, and XLM-RoBERTa models under-
went additional training using the following parameters: epoch=50, learning rate=2e-
6, max sequence length=128, and batch sizes of 8, 16, 32, and 64 on MLM task.
Subsequently, the proposed models were fine-tuned in the same manner as in previous
experiments on the SA task, and the corresponding results are presented in Table 7.
The comparison of results between Table 6 and Table 7 indicates an interesting
fact. Further training the language models on the MLM task improved the performance
of the proposed models, particularly in terms of the F1-score. Notably, the Roberta
model fine-tuned on OPSD (3-class) showed a 4.06% increase, as shown in table 7.
NEG+
3-Class
Acc
F1
Acc
F1
ALBERT-fa
0.9259
0.9087
0.9077
0.7867
ParsBERT
0.9245
0.9065
0.9125
0.7648
RoBERTa-fa
0.9211
0.9024
0.9106
0.7812
XLM-RoBERTa
0.9278
0.9111
0.9130
0.7756
Table 7 Results on the test set in masked language model (MLM) phase for each pre-trained
language model
5.1 Error Analysis of the Best Model (XLM-RoBERTa)
To gain deeper insights into the performance of the best models in our experiment, we
conduct an error analysis using their predictions. This analysis allows us to examine
cases where the model might have made mistakes and provides valuable information
for understanding its strengths and weaknesses. XLM-RoBERTa was chosen for this
analysis due to its outstanding performance on the validation and test sets during
our experimental evaluations. Figure 5 shows the confusion matrices of the XLM-
RoBERTa model on the test set for both NEG+ and 3-class cases.
Error analysis for the 3-class case shows that misclassification on the test data
can be categorized in two groups. The first group is the data samples that have POS
labels, but the model predicts T-NEG or NT-NEG labels (FN) based on existence of
some specific words. The observed issue arises from the discrepancy in the frequency
of certain words within comments labeled as T-NEG and NT-NEG, as opposed to
the significantly lower occurrence of these words in positive comments. This imbal-
ance in word distribution could potentially lead to difficulties in effectively classifying
comments with T-NEG and NT-NEG labels, as the model may not have encoun-
tered sufficient positive instances to learn from. Consequently, this disparity in the
2The task of masking tokens in sequence of tokens using [MASK] token and leading the language model
(LM) in a way that it fills this masked token with appropriate token is so called mask language modeling
(MLM).
13

--- Page 14 ---

Fig. 5 Confusion matrices of the XLM-RoBERTa model. (left) 3-class case and (right) NEG+ case.
occurrence of specific words between different classes might contribute to the model’s
challenges in accurately distinguishing between the negative and positive comments.
The second group is the data samples that are not correctly labeled, even with
high agreement between two annotators. This means that it seemed the model had
predicted the labels correctly, but the data samples had been mislabeled. If we remove
these data points from the test dataset, the results in Table 8 are obtained, showing
an approximately 3% increase in accuracy for the XLM-RoBERTa model.
# Error
Accuracy
F1
Before Removal
195
0.907
0.769
After Removal
139
0.936
0.842
Table 8 The performance of XLM-RoBERTa
before and after removing mislabeled data. Number
of errors is the total number of FP and FN.
6 Conclusion
In this paper, we introduced OPSD, a dataset consisting of Twitter and Instagram
comments written in Persian. The dataset is specifically designed to facilitate the
detection of offensive language in text.
We applied a three-phase process for annotating the comments in the dataset
manually. In the first phase, the dataset is divided into five parts, and each part is
annotated by two annotators. If the agreement falls below 75%, the process moves to
the second phase. In the second phase, a meeting is conducted to discuss the low Kappa
scores, leading to updates in annotation guidelines. The annotators then re-label the
previously disagreed data. Finally, in the third phase, any remaining disagreements
are resolved by a third annotator, determining the final label based on the majority
vote among the annotators.
Our proposed dataset, OPSD, includes an unlabeled subdivision known as OPSD
(Unlabeled). This particular subset was utilized for an additional training stage on the
Masked Language Modeling task. The results demonstrated that incorporating this
training step with OPSD (unlabeled) data prior to conducting the sentiment analysis
task enhanced the performance of baseline text classification models.
14

--- Page 15 ---

We applied baseline text classification models, by using machine learning models
and also state-of-the-work monolingual and multilingual BERT-based models, to show
the effectiveness of the dataset.
In the future, there is a plan to increase the size of the OPSD dataset. This would
require considering semi-supervised or unsupervised techniques to determine offensive
scores and classify textual entities, as labeling all items would be time-consuming.
Additionally, improving preprocessing modules, such as converting emojis to their
Persian textual descriptors, can enhance performance. Considering language struc-
tures and exploring other approaches, such as deep learning methods, for determining
probabilities (offensive scores) can further improve the proposed methodology.
Acknowledgments.
This publication was supported by grant No. RD-53-0105-0012
from the R&D Center of Mobile Telecommunication Company of Iran (MCI) for
advancing information and communications technologies.
References
[1] Zampieri, M., Malmasi, S., Nakov, P., Rosenthal, S., Farra, N., Kumar, R.: Pre-
dicting the Type and Target of Offensive Posts in Social Media. In: Proceedings
of NAACL (2019)
[2] Rosenthal,
S.,
Atanasova,
P.,
Karadzhov,
G.,
Zampieri,
M.,
Nakov,
P.:
SOLID: A large-scale semi-supervised dataset for offensive language identifi-
cation. In: Findings of the Association for Computational Linguistics: ACL-
IJCNLP 2021, pp. 915–928. Association for Computational Linguistics, Online
(2021). https://doi.org/10.18653/v1/2021.findings-acl.80 . https://aclanthology.
org/2021.findings-acl.80
[3] Davidson, T., Warmsley, D., Macy, M., Weber, I.: Automated hate speech detec-
tion and the problem of offensive language. Proceedings of the International AAAI
Conference on Web and Social Media 11(1), 512–515 (2017) https://doi.org/10.
1609/icwsm.v11i1.14955
[4] Alavi, P., Nikvand, P., Shamsfard, M.: Offensive language detection with
bert-based models, by customizing attention probabilities. arXiv preprint
arXiv:2110.05133 (2021)
[5] Mozafari, M.: Hate speech and offensive language detection using transfer learning
approaches. Theses, Institut Polytechnique de Paris (May 2021). https://theses.
hal.science/tel-03276023
[6] Khodabakhsh,
M.,
Jafarinejad,
F.,
Rahimi,
M.,
Ghayoomi,
M.:
Per-
bold:
A
big
dataset
of
persian
offensive
language
on
instagram
comments.
TABRIZ
JOURNAL
OF
ELECTRICAL
ENGINEER-
ING
53(2),
149–158
(2023)
https://doi.org/10.22034/tjee.2023.15794
https://tjee.tabrizu.ac.ir/article 15794 1a75a5b450027a6f41f6dfb9e8cf3e51.pdf
15

--- Page 16 ---

[7] Ataei, T.S., Darvishi, K., Javdan, S., Pourdabiri, A., Minaei-Bidgoli, B., Pilehvar,
M.T.: Pars-off: A benchmark for offensive language detection on farsi social media.
IEEE Transactions on Affective Computing, 1–9 (2022) https://doi.org/10.1109/
TAFFC.2022.3219229
[8] Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O.,
Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A.,
Cournapeau, D., Brucher, M., Perrot, M., Duchesnay, E.: Scikit-learn: Machine
learning in Python. Journal of Machine Learning Research 12, 2825–2830 (2011)
[9] Farahani, M., Gharachorloo, M., Farahani, M., Manthouri, M.: Parsbert:
Transformer-based model for persian language understanding. Neural Processing
Letters 53(6), 3831–3847 (2021) https://doi.org/10.1007/s11063-021-10528-4
[10] Devlin, J., Chang, M.-W., Lee, K., Toutanova, K.: BERT: Pre-training of deep
bidirectional transformers for language understanding. In: Proceedings of the
2019 Conference of the North American Chapter of the Association for Compu-
tational Linguistics: Human Language Technologies, Volume 1 (Long and Short
Papers), pp. 4171–4186. Association for Computational Linguistics, Minneapolis,
Minnesota (2019). https://doi.org/10.18653/v1/N19-1423 . https://aclanthology.
org/N19-1423
[11] Lan, Z., Chen, M., Goodman, S., Gimpel, K., Sharma, P., Soricut, R.: ALBERT:
A Lite BERT for Self-supervised Learning of Language Representations (2020)
[12] Team, H.: ALBERT-Persian: A Lite BERT for Self-supervised Learning of
Language Representations for the Persian Language. GitHub (2021)
[13] Zhuang, L., Wayne, L., Ya, S., Jun, Z.: A robustly optimized BERT pre-training
approach with post-training. In: Proceedings of the 20th Chinese National
Conference on Computational Linguistics, pp. 1218–1227. Chinese Information
Processing Society of China, Huhhot, China (2021). https://aclanthology.org/
2021.ccl-1.108
[14] Conneau, A., Khandelwal, K., Goyal, N., Chaudhary, V., Wenzek, G., Guzm´an,
F., Grave, E., Ott, M., Zettlemoyer, L., Stoyanov, V.: Unsupervised cross-lingual
representation learning at scale. In: Proceedings of the 58th Annual Meeting
of the Association for Computational Linguistics, pp. 8440–8451. Association
for Computational Linguistics, Online (2020). https://doi.org/10.18653/v1/2020.
acl-main.747 . https://aclanthology.org/2020.acl-main.747
[15] Loshchilov, I., Hutter, F.: Fixing weight decay regularization in adam. CoRR
abs/1711.05101 (2017) 1711.05101
16

```
