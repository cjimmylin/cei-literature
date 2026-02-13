---
title: "2023-Nguyen-Abusive Span Detection for Vietnamese Narrative Texts - PDF Extract"
source_pdf: "2023-Nguyen-Abusive Span Detection for Vietnamese Narrative Texts.pdf"
pages: 8
extracted_at: "2026-02-13T09:50:30.537278"
---

# PDF Extract: 2023-Nguyen-Abusive Span Detection for Vietnamese Narrative Texts

**Source PDF:** 2023-Nguyen-Abusive Span Detection for Vietnamese Narrative Texts.pdf
**Total Pages:** 8

---

## Content

```
--- Page 1 ---

Abusive Span Detection for Vietnamese Narrative Texts
Nhu-Thanh Nguyen
University of Information Technology
Ho Chi Minh City, Vietnam
Vietnam National University
Ho Chi Minh City, Vietnam
thanhnn.15@grad.uit.edu.vn
Khoa Thi-Kim Phan
University of Information Technology
Ho Chi Minh City, Vietnam
Vietnam National University
Ho Chi Minh City, Vietnam
khoaptk@uit.edu.vn
Duc-Vu Nguyen
University of Information Technology
Ho Chi Minh City, Vietnam
Vietnam National University
Ho Chi Minh City, Vietnam
vund@uit.edu.vn
Ngan Luu-Thuy Nguyen
University of Information Technology
Ho Chi Minh City, Vietnam
Vietnam National University
Ho Chi Minh City, Vietnam
ngannlt@uit.edu.vn
ABSTRACT
Abuse in its various forms, including physical, psychological, ver-
bal, sexual, financial, and cultural, has a negative impact on mental
health. However, there are limited studies on applying natural lan-
guage processing (NLP) in this field in Vietnam. Therefore, we aim
to contribute by building a human-annotated Vietnamese dataset
for detecting abusive content in Vietnamese narrative texts. We
sourced these texts from VnExpress, Vietnam’s popular online news-
paper, where readers often share stories containing abusive content.
Identifying and categorizing abusive spans in these texts posed
significant challenges during dataset creation, but it also motivated
our research. We experimented with lightweight baseline models by
freezing PhoBERT and XLM-RoBERTa and using their hidden states
in a BiLSTM to assess the complexity of the dataset. According to
our experimental results, PhoBERT outperforms other models in
both labeled and unlabeled abusive span detection tasks. These
results indicate that it has the potential for future improvements.
CCS CONCEPTS
• Computing methodologies →Natural language processing.
KEYWORDS
Abusive Span Detection, Vietnamese Narrative Texts Dataset, Pre-
trained Language Models, Long Short-Term Memory, Sequence
Labeling
ACM Reference Format:
Nhu-Thanh Nguyen, Khoa Thi-Kim Phan, Duc-Vu Nguyen, and Ngan Luu-
Thuy Nguyen. 2023. Abusive Span Detection for Vietnamese Narrative Texts.
In The 12th International Symposium on Information and Communication
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
SOICT 2023, December 7–8, 2023, Ho Chi Minh, Vietnam
© 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 979-8-4007-0891-6/23/12...$15.00
https://doi.org/10.1145/3628797.3628921
Technology (SOICT 2023), December 7–8, 2023, Ho Chi Minh, Vietnam. ACM,
New York, NY, USA, 8 pages. https://doi.org/10.1145/3628797.3628921
1
INTRODUCTION
Abuse is common worldwide and has substantial adverse conse-
quences [28]. With the main purpose of maintaining power and
control over another, abuse can be categorized into some preva-
lent forms, such as Physical, Sexual, Financial/Economic, Cul-
tural/Identity, Verbal/Emotional, and Mental/Psychological [32].
Understanding its influences, and severity, many works have been
promoted, involving academic fundamental research, and practical
applications [10, 28, 30, 38]. One of these practical applications is
leveraging the proliferation of social media to create a trustworthy
environment, consisting of confession forums, and sharing sections
for abused people to freely express their problems. Therefore, the
amount of narrative text data containing abusive phenomena is
abundant.
[Anh bảo vợ người ta giàu có, vợ mình vô tích sự, ăn hại (mental/psychological)]. [Anh
không mua nổi cái xe, bảo tôi phải mua xe để đi lại, ngoài ra các khoản nợ cũng bắt
tôi gánh vác (financial/economic)]. Tôi chưa kiếm được việc làm, anh bảo tôi lười
nhác. Đến khi tôi đi làm, lại nói vợ ăn diện, đi theo các anh trên công ty. Chưa đóng
tiền nhà trọ, anh cho rằng tôi đi theo người ta để trừ tiền trọ. [Tôi không như thế mà
bị chồng vu oan nhiều lần, cứ bảo tôi đi với người nọ người kia
(mental/psychological)]. 
[Tôi 
cảm 
thấy 
mình 
không 
được 
tôn 
trọng
(mental/psychological)]. Anh sống giả dối, không có tình cảm với tôi, lại hám giàu.
Nếu ở hoàn cảnh của tôi, mọi người nên làm thế nào? 
([He said that other people's wives were rich, but his wife was useless and a loser
(mental/psychological)]. [He couldn't buy a car, so he told me to buy one for him, then
forced me to bear his debts (financial/economic)]. When I don’t have a job, he
concludes I'm lazy. When I went to work, he told me dressing up, having an affair
with other guys at my company. When I haven't paid the rent, he assumes I'm going
with someone to deduct the rent. [I'm not that person, but my husband has accused
me many times, concluding that I have an affair with this person or that person
(mental/psychological)]. [I feel disrespected (mental/psychological)]. He lives a lie, has no
feelings for me, and is greedy for wealth. What should people do if they were in my
situation?)
Output
Anh bảo vợ người ta giàu có, vợ mình vô tích sự, ăn hại. Anh không
mua nổi cái xe, bảo tôi phải mua xe để đi lại, ngoài ra các khoản nợ
cũng bắt tôi gánh vác. Tôi chưa kiếm được việc làm, anh bảo tôi
lười nhác. Đến khi tôi đi làm, lại nói vợ ăn diện, đi theo các anh
trên công ty. Chưa đóng tiền nhà trọ, anh cho rằng tôi đi theo người
ta để trừ tiền trọ. Tôi không như thế mà bị chồng vu oan nhiều lần,
cứ bảo tôi đi với người nọ người kia. Tôi cảm thấy mình không
được tôn trọng. Anh sống giả dối, không có tình cảm với tôi, lại
hám giàu. Nếu ở hoàn cảnh của tôi, mọi người nên làm thế nào? 
(He said that other people's wives were rich, but his wife was
useless and a loser. He couldn't buy a car, so he told me to buy one
for him, then forced me to bear his debts. When I don’t have a job,
he concludes I'm lazy. When I went to work, he told me dressing
up, having an affair with other guys at my company. When I haven't
paid the rent, he assumes I'm going with someone to deduct the
rent. I'm not that person, but my husband has accused me many
times, concluding that I have an affair with this person or that
person. I feel disrespected. He lives a lie, has no feelings for me,
and is greedy for wealth. What should people do if they were in my
situation?)
Input
Figure 1: An example for Abusive span detection for Viet-
namese narrative texts.
In recent years, many works have used Natural Language Pro-
cessing techniques to automatically extract important information
from social media resources. This facilitates meaningful applica-
tions such as chatbots, question-answering, and recommendation
systems. However, before mining the data, the exact classification
arXiv:2312.07831v1  [cs.CL]  13 Dec 2023

--- Page 2 ---

SOICT 2023, December 7–8, 2023, Ho Chi Minh, Vietnam
Nhu-Thanh Nguyen, Khoa Thi-Kim Phan, Duc-Vu Nguyen, and Ngan Luu-Thuy Nguyen
of narrative text data is not easy in this age. Most previous stud-
ies focus on research done using social media data. In particular,
tweets, and comments that are short and lack a sequence of events
are preferred to exploit, especially in the field of detecting abuse
[2, 8, 11, 17].
Similarly, in the Vietnamese domain, there are also some related
works about hate and offensive language mainly mining social
media data such as comments, including ViHOS [14], ViHSD [21],
HSD-VLSP [36], and UIT-ViCTSD [24]. Although the definitions of
abusive and offensive language are closely related, there are still
important distinctions to define. According to [5], while both are as-
sociated with “strongly impolite, rude“, the use of abusive language
often involves an intention. To our knowledge, the monolingual
dataset for recognizing abusive spans in Vietnamese narrative text
is rare and may not exist. This questions us where we find a reliable
source, and how we can address the task of recognizing abusive
spans in Vietnamese narrative texts, which can promote many use-
ful applications in the health science field. Therefore, we would like
to (i) create a new dataset for the task of abusive spans detection in
Vietnamese truly narrative texts as depicted in Figure 1 to not only
the Natural Language Processing research community but also the
health science field in the future, (ii) develop a new task, namely
abusive spans detection described as follows:
• Input: a Vietnamese narrative text P that consists of N
characters.
• Output: One or more spans describing abuse are detected
directly from the narrative text P for each category. Each
span is extracted from the position i to position j such that
0 ≤i, j ≤N, and i ≤j.
In this work, we have two main contributions summarized as
follows:
• We created the first human-annotated dataset for Abusive
spans detection for Vietnamese narrative texts, compris-
ing 519 spans in 198 abusive texts in 1041 narrative texts
annotated with 6 aspect categories: Physical, Sexual, Fi-
nancial/Economic, Cultural/Identity, Verbal/Emotional, and
Mental/Psychological. To build a benchmark narrative text
dataset, we require a reliable source. Fortunately, VnExpress
which is a well-known Vietnamese online newspaper has
a narrative section. The VnExpress’s narrative section [35]
contains personal narrative stories submitted by readers and
standardized by editors. We crawled all stories which were
posted in this section as a source to build our dataset. Besides,
our dataset is annotated with a clear definition of abuse cate-
gories and detailed guidelines based on the study of REACH
community [32].
• To evaluate the challenge of the dataset to models, we con-
ducted experiments with lightweight baseline models by
freezing PhoBERT [23], XLM-RoBERTa [7], and using their
hidden states in a BiLSTM [15], combining with two kinds of
decoders for the classifier layer: Softmax and CRF [31]. We
also investigated the dataset in two tasks: unlabeled abusive
span detection, and labeled abusive span detection. We at-
tained (i) the relaxed evaluation inspired by the approach in
[14] brings better results than the strict one which requires
precise prediction of the start and end points of a span; (ii) us-
ing CRF as the final decoder layer provides better predictions
than the Softmax layer; (iii) using PhoBERTlarge combined
with BiLSTM-CRF gives the highest overall results, at 86.00%
and 58.10% respectively for the relaxed evaluation for both
two tasks.
In Section 2, we review prior research on abusive language detec-
tion, including approaches and datasets from Vietnamese and other
domains. Sections 3 and 4 cover our dataset creation and analysis.
In Section 5, we detail our approach to the new task, and Section 6
concludes and outlines future work.
2
RELATED WORK
In recent years, abusive language detection and other related prob-
lems such as offensive language have attracted much attention
from the Natural Language Processing (NLP) community. Research
in the field has largely considered some particular topics such as
HateSpeech [8, 26], Cyberbullying [1–3, 11], and Sexism/Racism
[6, 16, 37]. By and large, these works have been conducted in Eng-
lish or other resource-rich languages, including Chinese, Spain,
and French. Besides, the majority of datasets for these tasks have
been collected from two main popular social media platforms these
days, consisting of Twitter [2, 8], and Facebook [11, 17]. Similarly,
in the Vietnamese domain, most of the works related to the field
have also mainly focused on Hate Speech such as ViHSD [21], HSD-
VLSP [36], UIT-ViCTSD [24], and Vi-HOS [14] based on comments
crawling from social media platforms. All these datasets represent
multi-class classification problems, except the SemEval-2021 Task5:
Toxic Spans Detection dataset [26] for English and the Vi-HOS:
Hate Speech Spans Detection [14] for Vietnamese, which entail
multi-label classification.
Most of the works related to the field of detecting abusive, offen-
sive, and hate speech have employed traditional machine learning
models such as character n-gram Logistic Regression [13], and
Support Vector Machines [25] and models involving deep neural
networks combined with word embeddings [4, 29, 41]. Since the
emergence of BERT [9], more works have been established based
on itself and its variants, achieving competitive results in shared
tasks such as SemEval-2019 task 6 [39], SemEval-2020 task 12 [40],
and SemEval-2021 task 5 [27]. For the task of span detection, there
are a few works in English such as the teams submitting to the
shared task named SemEval-2021 Task 5: Toxic Spans Detection
[26] and the HateXplain dataset [22], and in Vietnam consisting
of ViHOS: Hate Speech Spans Detection for Vietnamese [14]. In
general, the above works used a mixture of transformer-based mod-
els and neural network methods. In particular, the best-performing
team (HITSZ-HLT) in SemEval-2021 Task 5 [42] employed two
systems based on BERT [9], in which for one system, a Conditional
Random Field (CRF) layer [31] was added on top, and for another,
an LSTM layer [12] was added between BERT and CRF layer. For
the HateXplain dataset [4], they investigated several models such as
CNN-GRU, BiRNN, BiRNN-Attention, and BERT on their dataset. In
the ViHOS [14], they used strong baseline models such as BiLSTM-
CRF [19], XLM-RoBERTa [7], and PhoBERT [23] to evaluate the
efficacy of their dataset.

--- Page 3 ---

Abusive Span Detection for Vietnamese Narrative Texts
SOICT 2023, December 7–8, 2023, Ho Chi Minh, Vietnam
Besides these above works, we argue that abusive language detec-
tion in NLP needs to be expanded to details by recognizing general
types of abuse, particularly 6 types of abuse according to the study of
REACH community [32]: Physical, Sexual, Financial/Economic, Cul-
tural/Identity, Verbal/Emotional, and Mental/Psychological, namely
Abusive spans detection. These categories of abuse have been noted
in the health science field [28, 30, 32], but have not yet received
the same level of attention in NLP. To our knowledge, there is still
little research on Abusive span detection in narrative texts world-
wide, as well as in Vietnamese. Therefore, in this study, we would
like to develop the first Vietnamese benchmark dataset for
the new task namely Abusive spans detection in Vietnamese
narrative texts.
3
DATASET CREATION
Inspired by [34], we defined the process with four phases: data
collection, guideline creation, training, and annotation.
Data Collection
(Phase 1)
Guidelines Creation
(Phase 2)
Training
(Phase 3)
Annotation
(Phase 4)
Figure 2: Overview dataset creation process
3.1
Phase 1 - Data Collection
We crawled 4,800 stories from VnExpress’s narrative section [35].
Each story has been stored as a .txt file in our raw dataset. After
that, we randomly selected 1,041 texts from the 4,800 crawled texts
to annotate and experiment. The remaining texts in our raw dataset
will be annotated in the future.
3.2
Phase 2 - Guidelines Creation
Guidelines
Sample data
(2) Annotate data based on guidelines
(3) Adjust or provide more examples about
the abuse to guidelines.
(1) Initialize guideline
Guidelines
author
Figure 3: Guidelines Creation phase
The objective of this stage is to provide clear instructions for annota-
tors to ensure they can annotate data properly. The guidelines focus
on identifying and categorizing abusive segments within texts. We
have established a two-step process, which includes the following:
Step 1: For each sentence, determine if it contains abusive con-
tent. To do that, annotators will be based on the definition of abuse,
along with a list of common words or phrases that are frequently
used. Although we have a list of common words or phrases, anno-
tators also need to read the contents of the sentence to determine.
Step 2: Categorize the type of abuse if the sentence contains
abuse. Annotators will based on the definition of different types of
abuse. Each type of abuse relates to specific aspects, for example:
• Physical abuse can involve punching, hitting, slapping, kick-
ing, ... a partner against their will.
• Verbal/Emotional abuse is when someone uses words to crit-
icize, insult, or harm the emotional well-being of others.
• Cultural/Identity abuse is when abusers use aspects of a vic-
tim’s cultural identity to inflict suffering or control them. For
example, threatening to expose someone’s LGBQ/T identity
if their loved ones do not know.
• Sexual abuse can include both physical and non-physical
components. It can involve rape or other forced sexual acts,
or withholding or using sex as a weapon. An abusive partner
might also use sex as a means to judge their partner and
assign a value.
• Financial/Economic abuse is when abusers use finances to
maintain the power and control. Whether it is controlling
all of the budgeting in the household and not letting the
survivor have access to their own bank accounts or spending
money, or opening credit cards and running up debts in the
survivor’s name.
• Mental/Psychological abuse happens when one partner,
through a series of actions or words, wears away at the
other’s sense of mental well-being and health.
Besides that, we also provided situational examples for each abuse
type to aid annotators’ understanding.
3.3
Phase 3 - Training Annotators
In this phase, we train annotators to ensure they understand the
guidelines well. We also let them practice labeling on a sample set,
including abusive and non-abusive content. After the annotators
finished their tasks, the guidelines were reviewed and revised. Any
inconsistencies or divergences were resolved based on guidelines.
Then, the difference between the first results and the final results
were clarified with the annotators. In this phase, the guidelines may
be adjusted and enhanced if required.
Annotate on a
small dataset D
Guidelines
Provide feedback to annotators about the conflicts
and differences in the last results.
Finalize results based on guidelines
Result 1
Result 2
Guidelines author
Training phase
Annotator 1
Annotator 2
Annotators
Annotator 3
Result 3
Annotate on a
small dataset D
Annotate on a
small dataset D
Result 1
Result 2
VS
Result 3
VS
Figure 4: Training phase

--- Page 4 ---

SOICT 2023, December 7–8, 2023, Ho Chi Minh, Vietnam
Nhu-Thanh Nguyen, Khoa Thi-Kim Phan, Duc-Vu Nguyen, and Ngan Luu-Thuy Nguyen
After the training, we measured the agreement of our three
annotators to ensure they were on the same page. We randomly
selected a set of 50 abusive texts. And each annotator will annotate
independently. Then, we collected the results and evaluated them
based on F-score. For the first round, the F-score was 76.09%, and
after re-training, the F-score increased to 80.12%
3.4
Phase 4 - Annotation
Each annotator was assigned a specific set of texts to label using the
sequence labeling method. If there was any uncertainty regarding
to the label, annotators would have a discussion to decide on the
final label. Following this stage, we divided our dataset into train,
dev, and test sets for experimentation.
4
DATASET ANALYSIS
Train
Dev
Test
All
Number of texts
700
100
241
1041
Number of abusive texts
133
21
44
198
Number of non-abusive texts
567
79
197
843
Total unlabeled-abusive span count
350
45
118
513
Total labeled-abusive span count
355
45
119
519
Table 1: Overall statistics of the entire dataset
Our dataset consists of 1041 narrative texts, which we divided into
three sets: 700 for the train set, 100 for the dev set, and 241 for the
test set. Our study explored two tasks: (1) unlabeled abusive span
detection, and (2) labeled abusive span detection.
• For task (1), abusive spans in our dataset have only one label:
abusive.
• For task (2), abusive spans in our dataset have one in six
labels representing six abuse types.
Verbal Emotional
39.5%
Financial Economic
8.9%
Cultural Identity
3.1%
Physical
13.5%
Sexual
2.1%
Mental Psychological
32.9%
Figure 5: Distribution of abusive types across the entire
dataset
Before conducting the experiments, we analyzed the dataset to
understand it better and facilitate evaluating the results. Table 1
provides the overall statistics of the entire dataset. As shown in this
table, abusive texts make up 19.02% of the entire dataset. It indicates
that narrative texts containing abuse are lower than non-abusive
narrative texts. Consequently, the accuracy of predicting abuse
may be impacted. This is one of the challenges, which we will see
through the experiment results.
As we explored the classification of abusive behavior in our
dataset, we observed an imbalance among different abusive types.
The distribution of abusive types throughout the entire dataset can
be observed in Figure 5, while Figure 6 illustrates the distribution
of abusive types in the Train, Dev, and Test sets individually.
Figure 6: Distribution of abusive types across Train, Dev, and
Test sets
The charts show that Verbal/Emotional and Mental/Psychological
makeup comprises over 60% of the data, while the distribution of
Sexual (2.1% in total) and Cultural/Identity (3.1% in total) types are
significantly lower. The lack of data on Sexual and Cultural/Identity
abuse types may potentially affect the predicted results for these
types.
Furthermore, when examining the average length of an abusive
span, we observe that the average length of a span in our dataset is
quite high. In Table 2, the longest average length in our dataset is
30.44 words (Financial/Economic type). And our unlabeled dataset
version has an average of 26.59 words per span. The length of
abusive spans is a factor that makes our dataset more challenging.
Besides that, to evaluate the results, we employed strict and relaxed
methods. Because the abusive span is relatively long, which leads
to the strict evaluation provided low results.
Avg span’s length
Physical
22.43
Verbal/Emotional
28.67
Mental/Psychological
24.99
Financial/Economic
30.44
Sexual
26.38
Table 2: Average span’s length of each abusive type

--- Page 5 ---

Abusive Span Detection for Vietnamese Narrative Texts
SOICT 2023, December 7–8, 2023, Ho Chi Minh, Vietnam
5
EMPIRICAL EVALUATION
5.1
Baseline Models
To evaluate the complexity of our dataset, we experimented with
some effective baseline models for the Vietnamese language. Our
approaches are freezing PhoBERT and XLM-RoBERTa and using
their hidden states in a BiLSTM. For the classifier layer, we utilized
two kinds of decoders: Softmax and CRF.
Pre-trained Language Model
RNN-Decoder layer
PhoBERTbase
BiLSTM-Softmax
BiLSTM-CRF
PhoBERTlarge
BiLSTM-Softmax
BiLSTM-CRF
XLM-Rbase
BiLSTM-Softmax
BiLSTM-CRF
XLM-Rlarge
BiLSTM-Softmax
BiLSTM-CRF
Table 3: All baseline models were used in our experiments
Table 3 shows all baseline models we used in our experiments:
• BiLSTM [15]: a recurrent neural network that can process
the input in both directions and utilize information from
both sides.
• BiLSTM-CRF [19]: a BiLSTM combines with Conditional
Random Field (CRF) [18] layer. The BiLSTM is used to process
each sentence token-by-token, and then its results are used
as input for CRF to produce the prediction results. This model
achieved the highest performance in span detection tasks
[26].
• XLM-RoBERTa [7]: a multilingual language model that
supports 100 languages. It was trained on 2.5 TB of newly
created clean CommonCrawl data, including 137 GB of Viet-
namese text.
• PhoBERT [23]: a monolingual language model pre-trained
on a 20 GB Vietnamese dataset that performs the most effi-
ciently for the Vietnamese language. Its approach is based
on RoBERTa [20], which optimizes the BERT [9] for more
robust performance.
5.2
Experimental Settings
Regarding all pre-trained language models, the frozen hidden states
were projected to a dimension of 128, which was then used as
the input for the BiLSTM. To facilitate a lightweight experiment,
the BiLSTM’s hidden size was configured at 64, while both the
word embedding dropout and recurrent dropout were set to 0.1.
Instead of using the entire word as input, the first sub-word from
pre-trained language models was selected as the input word for
the BiLSTM, as detailed in [23]. In terms of optimization details,
all experiments were conducted over 100 epochs to ensure that all
models could converge equally. The batch size was set to 32, and
the initial learning rate was 1e-3, which was then decayed using a
linear scheduler.
5.3
Evaluation Metrics
Drawing upon insights derived from two prior studies focused on
Vietnamese span detection, this paper utilizes both a strict evalu-
ation method, as outlined in the work of Thanh et al. (2021) [33],
and a more permissive evaluation approach, as detailed in the study
by Hoang et al. (2023) [14], to evaluate the performance of pre-
dictive models. In the context of the relaxed evaluation, which is
inspired by the approach in [14], we proposed to exclusively assess
the positive class. This choice deliberately yields lower metrics and
offers ample room for future enhancements and refinements. So,
the F-score for the strict evaluation is computed using the following
formulations.
Precision =
Total exact matching spans
Total spans predicted by the system
(1)
Recall = Total exact matching spans
Total gold spans
(2)
F-score = 2 · Precision · Recall
Precision + Recall
(3)
Similarly, the F-score for the relaxed evaluation is calculated using
the following formulas.
Precision =
Total exact matching characters
Total characters predicted by the system
(4)
Recall = Total exact matching characters
Total gold characters
(5)
F-score = 2 · Precision · Recall
Precision + Recall
(6)
5.4
Experiments Results
Our study explored two tasks, including unlabeled abusive span
detection, and labeled abusive span detection. In the first task, we
identified the abusive spans without categorizing them into specific
types. In the second task, we not only identified abusive spans but
also classified them into six different types of abuse. The results of
those tasks were shown in Table 4: Experimental results of the first
task, and Table 5: Experimental results of the second one.
From both tables, we saw that the results of strict evaluation
are quite lower than the relaxed method. The reason is that strict
evaluation requires precise prediction of the start and end points
of a span, while relaxed evaluation allows for more flexibility.
Most experiment results show that using CRF as the final decoder
layer provided better predictions than the softmax layer. However,
the XLM-Rbase coupled with BiLSTM-Softmax is an exception. It
achieved the best result for Financial/Economic types with a 66.58%
F-score.
For the unlabeled abusive span detection experimental results
in Table 4, on the Test set, PhoBERTbase combined with BiLSTM-
CRF provided the highest F-score (32.70%) in the strict evaluation,
while PhoBERTlarge coupled with BiLSTM-CRF outperformed with
remains with F-score is 86.00% in the relaxed evaluation.
For the labeled abusive span detection experimental results in Ta-
ble 5, we observed that the Verbal/Emotional type had the highest
F-score. Specifically, it achieved a 27.06% F-score in strict evalua-
tion, and a 70.82% F-score in relaxed evaluation when using the
XLM-Rbase with BiLSTM-CRF. The distribution of Verbal/Emotional

--- Page 6 ---

SOICT 2023, December 7–8, 2023, Ho Chi Minh, Vietnam
Nhu-Thanh Nguyen, Khoa Thi-Kim Phan, Duc-Vu Nguyen, and Ngan Luu-Thuy Nguyen
Table 4: Unlabeled abusive span detection performances on dev and test sets
Decoder
Training
Strategy
Pre-trained
Language
Model
Strict
Relaxed
Dev
Test
Dev
Test
P
R
F
P
R
F
P
R
F
P
R
F
Softmax
Unlabeled
Span
Detection
XLM-Rbase
22.22
24.49
23.30
26.89
27.31
27.10
88.00
80.30
83.97
89.00
82.96
85.88
XLM-Rlarge
20.49
25.51
22.73
24.54
30.77
27.30
85.98
73.93
79.50
80.54
80.79
80.67
PhoBERTbase
34.69
34.69
34.69
26.39
29.23
27.74
95.27
73.83
83.19
88.27
80.91
84.43
PhoBERTlarge
27.78
25.51
26.60
25.90
27.69
26.77
94.59
64.78
76.90
91.35
80.27
85.45
Join Span
Detection
& Labeling
XLM-Rbase
10.90
17.35
13.39
7.81
14.12
10.05
91.86
76.15
83.27
91.75
76.72
83.57
XLM-Rlarge
4.46
10.20
6.21
4.62
11.45
6.58
87.94
74.89
80.89
77.19
82.81
79.90
PhoBERTbase
12.82
20.41
15.75
8.12
16.79
10.95
97.33
70.91
82.04
89.75
78.27
83.62
PhoBERTlarge
12.88
17.35
14.78
7.71
14.89
10.16
89.66
64.22
74.83
91.49
77.06
83.66
CRF
Unlabeled
Span
Detection
XLM-Rbase
30.61
30.61
30.61
32.54
31.54
32.03
88.57
82.10
85.21
87.42
82.51
84.90
XLM-Rlarge
29.41
30.61
30.00
26.21
29.23
27.64
84.23
72.19
77.74
76.81
83.12
79.84
PhoBERTbase
36.36
32.65
34.41
32.33
33.08
32.70
97.38
73.65
83.87
87.62
82.29
84.87
PhoBERTlarge
36.25
29.59
32.58
31.78
28.85
30.24
91.93
68.20
78.31
92.72
80.20
86.00
Join Span
Detection
& Labeling
XLM-Rbase
29.00
29.59
29.29
26.64
27.86
27.24
93.02
78.73
85.28
88.75
80.10
84.20
XLM-Rlarge
27.08
26.53
26.80
23.59
25.57
24.54
93.33
67.48
78.33
87.23
77.12
81.86
PhoBERTbase
28.12
27.55
27.84
24.50
27.86
26.07
94.89
69.50
80.24
89.44
80.61
84.80
PhoBERTlarge
37.80
31.63
34.44
28.40
27.10
27.73
92.63
68.72
78.91
92.40
79.19
85.28
Table 5: Labeled abusive span detection F-scores on test set of models using join span detection and labeling training strategy
Decoder
Pre-trained
Language
Model
Strict
Relaxed
Cultural Identity
Financial Economic
Mental Psychological
Physical
Sexual
Verbal Emotional
Overall
Cultural Identity
Financial Economic
Mental Psychological
Physical
Sexual
Verbal Emotional
Overall
Softmax
XLM-Rbase
0.00
9.09
5.88
8.62
0.00
12.40
8.15
28.43
66.58
46.88
59.05
0.00
64.55
55.41
XLM-Rlarge
0.00
1.96
4.40
0.00
0.00
5.71
4.17
0.00
48.43
42.68
26.71
0.00
51.92
44.43
PhoBERTbase
0.00
9.26
7.48
5.66
0.00
11.28
8.46
11.89
60.84
55.01
44.66
0.00
63.10
55.70
PhoBERTlarge
0.00
1.79
8.89
2.13
0.00
10.37
7.29
0.00
64.21
54.51
38.10
0.00
61.50
54.55
CRF
XLM-Rbase
0.00
12.90
18.27
8.82
0.00
27.06
18.28
38.86
65.10
51.34
27.12
0.00
70.82
55.41
XLM-Rlarge
0.00
17.86
15.38
25.00
0.00
15.05
16.48
0.00
58.52
49.36
61.03
0.00
53.96
51.84
PhoBERTbase
0.00
15.62
17.53
19.44
0.00
20.59
17.86
26.11
66.50
54.20
58.27
0.00
61.18
57.46
PhoBERTlarge
0.00
17.24
18.95
20.00
0.00
21.95
18.75
29.24
61.65
58.36
54.11
0.00
64.44
58.10
abuse texts within our dataset, which comprised 39.5%, signifi-
cantly influenced this outcome. Besides that, the Sexual and Cul-
tural/Identity types had the lowest scores, with a F-score of 0%. This
is because these types comprise only a tiny portion of our dataset,
accounting for 2.1% and 3.1% respectively. The dataset’s imbalance
needs to be addressed in the future to enhance predictions for these
types of abuse.
We also discovered that using PhoBERTlarge combined with
BiLSTM-CRF produced the highest overall results. This approach
achieved the highest F-scores in both evaluation methods, with
an F-score of 18.75% for strict evaluation and 58.10% for relaxed
evaluation.
Although the F-scores in strict evaluation were relatively low,
it indicates that there is still room for improvement in the future.
On the other hand, the promising results in the relaxed evaluation
suggest a potential for further development in detecting abusive
spans in Vietnamese narrative texts.
5.5
Error Analysis
We visualized a prediction of the labeled abusive span detection task
in the Test set of PhoBERTlarge coupled with BiLSTM-CRF. The re-
sults are shown in Figure 7. We observed that the Verbal/Emotional,

--- Page 7 ---

Abusive Span Detection for Vietnamese Narrative Texts
SOICT 2023, December 7–8, 2023, Ho Chi Minh, Vietnam
Gold
Quả_thật em đã trải qua một tuổi_thơ theo tôi là vô_cùng khủng khiếp. Cha_mẹ ly_hôn từ năm
em 12 tuổi, độ tuổi đã ý_thức rõ_ràng nhưng tâm_lý vẫn còn rất mong_manh và dễ tổn thương.
Suốt khoảng thời_gian trước đó, không_khí gia_đình em lúc_nào cũng ngột_ngạt với vô_số lần
gây_gổ của cha_mẹ và cả cảnh cha bạo_hành mẹ (mental/psychological). Sau khi ly hôn, cha
em không chu_cấp nuôi con (bạn gái tôi là chị cả và có hai đứa em) (financial/economic). Cha
còn trực_tiếp nói với em những lời_lẽ cực_kỳ nặng nề, tổn_thương sâu_sắc đến tâm_lý của một
đứa con gái mới 12 tuổi (verbal/emotional). Mẹ em không khá hơn, bà cũng bỏ_bê con cái, sống
nhờ tiền chu_cấp của người anh bên Mỹ mà không có công_việc ổn định, thậm_chí qua_lại với
vô_số người_tình trước mặt em (mental/psychological). Tệ hơn nữa, em còn bị không_chỉ một
mà đến hai người_thân tấn_công tình_dục (sexual). Em lớn lên trong sự căm_hận chính cha_mẹ
và những người khác trong gia_đình mình, khi đó chỉ có bà ngoại yêu_thương và quan_tâm em.
English:
My girlfriend went through an extremely terrible childhood. Her parents divorced when she was
12 years old, her psychology was still very fragile and vulnerable. During that period, her
family's atmosphere was always stuffy, with countless fights between her parents, and her father
usually abusing her mother (mental/psychological). After the divorce, her father did not provide
child support (my girlfriend is the oldest sister and has two younger siblings)
(financial/economic). Her father also directly told her extremely harsh words that deeply hurt
the psychology of a 12-year-old girl (verbal/emotional). Her mother is not better. She also
neglects her children, lives on support from her brother in America without a stable job, and
even has sex with countless lovers in front of me (mental/psychological). Even worse, she was
sexually assaulted by not one but two relatives(sexual). She grew up hating my parents and
other people in my family. At that time, only her grandmother loved and cared for her. 
Prediction
Quả_thật em đã trải qua một tuổi_thơ theo tôi là vô_cùng khủng khiếp. Cha_mẹ ly_hôn từ năm
em 12 tuổi, độ tuổi đã ý_thức rõ_ràng nhưng tâm_lý vẫn còn rất mong_manh và dễ tổn thương.
Suốt khoảng thời_gian trước đó, không_khí gia_đình em lúc_nào cũng ngột_ngạt
(mental/psychological) với vô_số lần gây_gổ của cha_mẹ và cả cảnh cha bạo_hành mẹ (sexual).
Sau khi ly hôn, cha em không chu_cấp nuôi con (bạn gái tôi là chị cả và có hai đứa em)
(financial/economic). Cha còn trực_tiếp nói với em những lời_lẽ cực_kỳ nặng nề, tổn_thương
sâu_sắc đến tâm_lý của một đứa con gái mới 12 tuổi (verbal/emotional). Mẹ em không khá hơn,
bà cũng bỏ_bê con cái, sống nhờ tiền chu_cấp của người anh bên Mỹ mà không có công_việc
ổn định, thậm_chí qua_lại với vô_số người_tình trước mặt em (mental/psychological). Tệ hơn
nữa, em còn bị không_chỉ một mà đến hai người_thân tấn_công tình_dục (physical). Em lớn lên
trong sự căm_hận chính cha_mẹ và những người khác trong gia_đình mình, khi đó chỉ có bà
ngoại yêu_thương và quan_tâm em. 
English:
My girlfriend went through an extremely terrible childhood. Her parents divorced when she was
12 years old, her psychology was still very fragile and vulnerable. During that period, her
family's atmosphere was always stuffy with countless fights between her parents, and her father
usually abusing her mother (mental/psychological). After the divorce, her father did not provide
child support (my girlfriend is the oldest sister and has two younger siblings)
(financial/economic). Her father also directly told her extremely harsh words that deeply hurt
the psychology of a 12-year-old girl (verbal/emotional). Her mother is not better. She also
neglects her children, lives on support from her brother in America without a stable job, and
even has sex with countless lovers in front of me (mental/psychological). Even worse, she was
sexually assaulted by not one but two relatives(physical). She grew up hating my parents and
other people in my family. At that time, only her grandmother loved and cared for her.
Figure 7: A prediction from PhoBERTlarge for labeled abusive
span detection
Financial/Economic, and Mental/Psychological abuses were accu-
rately detected with precise start and end points. However, the Sex-
ual abuse (span in blue color) was incorrectly predicted as Physical
(span in orange color) abuse, and the span of Mental/Psychological
abuse (span in purple color) was mistakenly predicted as Sexual
abuse. The reason is that the limited training data for the Sexual
abuse, and future improvements are necessary to achieve more
accurate identification.
6
CONCLUSION AND FUTURE WORKS
We presented the first Vietnamese benchmark dataset for the new
task namely Abusive spans detection in Vietnamese narrative texts.
The dataset can be served with two tasks, including the unlabeled
abusive span detection, and the labeled abusive span detection. For
the labeled abusive span detection, the dataset consists of 519 spans
in 198 abusive texts in 1041 narrative texts annotated with six aspect
categories: Physical, Sexual, Financial/Economic, Cultural/Identity,
Verbal/Emotional, and Mental/Psychological. We also conducted
experiments with models XLM-RoBERTa, PhoBERT coupled with
BiLSTM, and utilized two kinds of decoders: Softmax and CRF for
the classifier layer. As a result, we observed that using CRF as
the final decoder layer provides better predictions than the Soft-
max layer. Most importantly, using PhoBERTlarge combined with
BiLSTM-CRF outperformed other models with the highest overall
results, at 86.00% and 58.10% respectively for the relaxed evaluation
for both two tasks.
To enhance our results, we must address several limitations in
the future. Firstly, our dataset is imbalanced among abusive types,
notably in the Sexual and Cultural/Identity categories. To improve
predictive accuracy, we will gather more data for these categories.
Secondly, our current system can only predict a single abusive type
for each span, whereas real-world abusive spans may encompass
multiple abusive types simultaneously. Additionally, we have not
yet accounted for detecting nested spans in this study, an area for
improvement that should be considered in the future.
ACKNOWLEDGMENTS
This research was supported by The VNUHCM-University of In-
formation Technology’s Scientific Research Support Fund. We are
grateful to the reviewers for their valuable comments, which have
greatly enhanced the quality of our work.
REFERENCES
[1] Stephen Afrifa. 2022. Cyberbullying detection on twitter using natural language
processing and machine learning techniques. International Journal of Innovative
Technology and Interdisciplinary Sciences 5, 4 (2022), 1069–1080.
[2] Mohammed Ali Al-Garadi, Sangmi Kim, Yuting Guo, Elise Warren, Yuan-Chi
Yang, Sahithi Lakamana, and Abeed Sarker. 2022. Natural language model for
automatic identification of intimate partner violence reports from twitter. Array
15 (2022), 100217.
[3] Wan Noor Hamiza Wan Ali, Masnizah Mohd, and Fariza Fauzi. 2018. Cyberbul-
lying detection: an overview. In 2018 Cyber Resilience Conference (CRC). IEEE,
1–3.
[4] Aymé Arango, Jorge Pérez, and Barbara Poblete. 2022. Hate speech detection
is not as easy as you may think: A closer look at model validation (extended
version). Information Systems 105 (2022), 101584.
[5] Tommaso Caselli, Valerio Basile, Jelena Mitrović, Inga Kartoziya, and Michael
Granitzer. 2020. I Feel Offended, Don’t Be Abusive! Implicit/Explicit Messages in
Offensive and Abusive Language. In Proceedings of the Twelfth Language Resources
and Evaluation Conference. European Language Resources Association, Marseille,
France, 6193–6202. https://aclanthology.org/2020.lrec-1.760
[6] Patricia Chiril, Farah Benamara, Véronique Moriceau, Marlene Coulomb-Gully,
and Abhishek Kumar. 2019. Multilingual and multitarget hate speech detection
in tweets. In Conférence sur le Traitement Automatique des Langues Naturelles
(TALN-PFIA 2019). ATALA, 351–360.
[7] Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guil-
laume Wenzek, Francisco Guzmán, Edouard Grave, Myle Ott, Luke Zettlemoyer,
and Veselin Stoyanov. 2020. Unsupervised Cross-lingual Representation Learning
at Scale. In Proceedings of the 58th Annual Meeting of the Association for Computa-
tional Linguistics. Association for Computational Linguistics, Online, 8440–8451.
https://doi.org/10.18653/v1/2020.acl-main.747
[8] Thomas Davidson, Dana Warmsley, Michael Macy, and Ingmar Weber. 2017.
Automated hate speech detection and the problem of offensive language. In
Proceedings of the international AAAI conference on web and social media, Vol. 11.
512–515.
[9] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT:
Pre-training of Deep Bidirectional Transformers for Language Understanding.
arXiv:1810.04805 [cs.CL]
[10] Chuka Emezue et al. 2020. Digital or digitally delivered responses to domestic and
intimate partner violence during COVID-19. JMIR public health and surveillance
6, 3 (2020), e19831.
[11] Md Imdadul Haque Emon, Khondoker Nazia Iqbal, Md Humaion Kabir Mehedi,
Mohammed Julfikar Ali Mahbub, and Annajiat Alim Rasel. 2022. Detection of
bangla hate comments and cyberbullying in social media using nlp and trans-
former models. In International Conference on Advances in Computing and Data
Sciences. Springer, 86–96.
[12] Alex Graves and Alex Graves. 2012. Long short-term memory. Supervised sequence
labelling with recurrent neural networks (2012), 37–45.
[13] Tommi Gröndahl, Luca Pajola, Mika Juuti, Mauro Conti, and N Asokan. 2018. All
you need is" love" evading hate speech detection. In Proceedings of the 11th ACM
workshop on artificial intelligence and security. 2–12.
[14] Phu Gia Hoang, Canh Duc Luu, Khanh Quoc Tran, Kiet Van Nguyen, and Ngan
Luu-Thuy Nguyen. 2023. ViHOS: Hate Speech Spans Detection for Vietnamese.

--- Page 8 ---

SOICT 2023, December 7–8, 2023, Ho Chi Minh, Vietnam
Nhu-Thanh Nguyen, Khoa Thi-Kim Phan, Duc-Vu Nguyen, and Ngan Luu-Thuy Nguyen
In Proceedings of the 17th Conference of the European Chapter of the Association for
Computational Linguistics. Association for Computational Linguistics, Dubrovnik,
Croatia, 652–669. https://aclanthology.org/2023.eacl-main.47
[15] Sepp Hochreiter and Jürgen Schmidhuber. 1997. Long short-term memory. Neural
computation 9, 8 (1997), 1735–1780.
[16] Aiqi Jiang, Xiaohan Yang, Yang Liu, and Arkaitz Zubiaga. 2022. SWSR: A Chinese
dataset and lexicon for online sexism detection. Online Social Networks and Media
27 (2022), 100182.
[17] Ritesh Kumar, Atul Kr. Ojha, Shervin Malmasi, and Marcos Zampieri. 2018.
Benchmarking Aggression Identification in Social Media. In Proceedings of
the First Workshop on Trolling, Aggression and Cyberbullying (TRAC-2018). As-
sociation for Computational Linguistics, Santa Fe, New Mexico, USA, 1–11.
https://aclanthology.org/W18-4401
[18] John D. Lafferty, Andrew McCallum, and Fernando C. N. Pereira. 2001. Con-
ditional Random Fields: Probabilistic Models for Segmenting and Labeling Se-
quence Data. In Proceedings of the Eighteenth International Conference on Machine
Learning (ICML ’01). Morgan Kaufmann Publishers Inc., San Francisco, CA, USA,
282–289. http://dl.acm.org/citation.cfm?id=645530.655813
[19] Guillaume Lample, Miguel Ballesteros, Sandeep Subramanian, Kazuya Kawakami,
and Chris Dyer. 2016. Neural Architectures for Named Entity Recognition. In
Proceedings of the 2016 Conference of the North American Chapter of the Association
for Computational Linguistics: Human Language Technologies. Association for
Computational Linguistics, San Diego, California, 260–270. https://doi.org/10.
18653/v1/N16-1030
[20] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer
Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. 2019. RoBERTa: A
Robustly Optimized BERT Pretraining Approach. arXiv:1907.11692 [cs.CL]
[21] Son T Luu, Kiet Van Nguyen, and Ngan Luu-Thuy Nguyen. 2021. A large-
scale dataset for hate speech detection on Vietnamese social media texts. In
Advances and Trends in Artificial Intelligence. Artificial Intelligence Practices: 34th
International Conference on Industrial, Engineering and Other Applications of
Applied Intelligent Systems, IEA/AIE 2021, Kuala Lumpur, Malaysia, July 26–29,
2021, Proceedings, Part I 34. Springer, 415–426.
[22] Binny Mathew, Punyajoy Saha, Seid Muhie Yimam, Chris Biemann, Pawan Goyal,
and Animesh Mukherjee. 2021. Hatexplain: A benchmark dataset for explain-
able hate speech detection. In Proceedings of the AAAI conference on artificial
intelligence, Vol. 35. 14867–14875.
[23] Dat Quoc Nguyen and Anh Tuan Nguyen. 2020. PhoBERT: Pre-trained language
models for Vietnamese. In Findings of the Association for Computational Linguis-
tics: EMNLP 2020. Association for Computational Linguistics, Online, 1037–1042.
https://doi.org/10.18653/v1/2020.findings-emnlp.92
[24] Luan Thanh Nguyen, Kiet Van Nguyen, and Ngan Luu-Thuy Nguyen. 2021. Con-
structive and toxic speech detection for open-domain social media comments in
vietnamese. In Advances and Trends in Artificial Intelligence. Artificial Intelligence
Practices: 34th International Conference on Industrial, Engineering and Other Ap-
plications of Applied Intelligent Systems, IEA/AIE 2021, Kuala Lumpur, Malaysia,
July 26–29, 2021, Proceedings, Part I 34. Springer, 572–583.
[25] Endang Wahyu Pamungkas, Valerio Basile, and Viviana Patti. 2020. Misogyny
detection in twitter: a multilingual and cross-domain study. Information processing
& management 57, 6 (2020), 102360.
[26] John Pavlopoulos, Jeffrey Sorensen, Léo Laugier, and Ion Androutsopoulos. 2021.
SemEval-2021 Task 5: Toxic Spans Detection. In Proceedings of the 15th Interna-
tional Workshop on Semantic Evaluation (SemEval-2021). Association for Compu-
tational Linguistics, Online, 59–69. https://doi.org/10.18653/v1/2021.semeval-1.6
[27] John Pavlopoulos, Jeffrey Sorensen, Léo Laugier, and Ion Androutsopoulos. 2021.
SemEval-2021 task 5: Toxic spans detection. In Proceedings of the 15th international
workshop on semantic evaluation (SemEval-2021). 59–69.
[28] Milen L Radell, Eid G Abo Hamza, Wid H Daghustani, Asma Perveen, Ahmed A
Moustafa, et al. 2021. The impact of different types of abuse on depression.
Depression research and treatment 2021 (2021).
[29] Tharindu Ranasinghe and Hansi Hettiarachchi. 2019. Emoji powered capsule
network to detect type and target of offensive posts in social media. (2019).
[30] Melanie F Shepard and James A Campbell. 1992. The Abusive Behavior Inventory:
A measure of psychological and physical abuse. Journal of interpersonal violence
7, 3 (1992), 291–305.
[31] Charles Sutton, Andrew McCallum, et al. 2012. An introduction to conditional
random fields. Foundations and Trends® in Machine Learning 4, 4 (2012), 267–373.
[32] Reach Team. 2017. 6 Different Types of Abuse.
https://reachma.org/blog/6-
different-types-of-abuse/
[33] Kim Nguyen Thi Thanh, Sieu Huynh Khai, Phuc Pham Huynh, Luong Phan Luc,
Duc-Vu Nguyen, and Kiet Nguyen Van. 2021. Span Detection for Aspect-Based
Sentiment Analysis in Vietnamese. In Proceedings of the 35th Pacific Asia Confer-
ence on Language, Information and Computation. Association for Computational
Lingustics, Shanghai, China, 318–328. https://aclanthology.org/2021.paclic-1.34
[34] Amanda Stent Tina Tseng and Domenic Maida. 2020. Best Practices for Managing
Data Annotation Projects. Bloomberg Finance L.P.
[35] VnExpress. 2023. Narrative section. https://vnexpress.net/tam-su
[36] Xuan-Son Vu, Thanh Vu, Mai-Vu Tran, Thanh Le-Cong, and Huyen Nguyen.
2020. HSD shared task in VLSP campaign 2019: Hate speech detection for social
good. arXiv preprint arXiv:2007.06493 (2020).
[37] Zeerak Waseem and Dirk Hovy. 2016. Hateful symbols or hateful people? predic-
tive features for hate speech detection on twitter. In Proceedings of the NAACL
student research workshop. 88–93.
[38] Yongjie Yon, Maria Ramiro-Gonzalez, Christopher R Mikton, Manfred Huber,
and Dinesh Sethi. 2019. The prevalence of elder abuse in institutional settings:
a systematic review and meta-analysis. European journal of public health 29, 1
(2019), 58–67.
[39] Marcos Zampieri, Shervin Malmasi, Preslav Nakov, Sara Rosenthal, Noura Farra,
and Ritesh Kumar. 2019. Semeval-2019 task 6: Identifying and categorizing
offensive language in social media (offenseval). arXiv preprint arXiv:1903.08983
(2019).
[40] Marcos Zampieri, Preslav Nakov, Sara Rosenthal, Pepa Atanasova, Georgi
Karadzhov, Hamdy Mubarak, Leon Derczynski, Zeses Pitenis, and Çağrı Çöltekin.
2020. SemEval-2020 task 12: Multilingual offensive language identification in
social media (OffensEval 2020). arXiv preprint arXiv:2006.07235 (2020).
[41] Ziqi Zhang, David Robinson, and Jonathan Tepper. 2018. Detecting hate speech
on twitter using a convolution-gru based deep neural network. In The Semantic
Web: 15th International Conference, ESWC 2018, Heraklion, Crete, Greece, June 3–7,
2018, Proceedings 15. Springer, 745–760.
[42] Qinglin Zhu, Zijie Lin, Yice Zhang, Jingyi Sun, Xiang Li, Qihui Lin, Yixue Dang,
and Ruifeng Xu. 2021. HITSZ-HLT at SemEval-2021 task 5: Ensemble sequence
labeling and span boundary detection for toxic span detection. In Proceedings of
the 15th international workshop on semantic evaluation (SemEval-2021). 521–526.

```
