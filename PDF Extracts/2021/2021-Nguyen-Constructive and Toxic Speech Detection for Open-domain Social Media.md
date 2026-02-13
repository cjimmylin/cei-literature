---
title: "2021-Nguyen-Constructive and Toxic Speech Detection for Open-domain Social Media - PDF Extract"
source_pdf: "2021-Nguyen-Constructive and Toxic Speech Detection for Open-domain Social Media.pdf"
pages: 12
extracted_at: "2026-02-13T09:50:28.374356"
---

# PDF Extract: 2021-Nguyen-Constructive and Toxic Speech Detection for Open-domain Social Media

**Source PDF:** 2021-Nguyen-Constructive and Toxic Speech Detection for Open-domain Social Media.pdf
**Total Pages:** 12

---

## Content

```
--- Page 1 ---

Constructive and Toxic Speech Detection for
Open-domain Social Media Comments in
Vietnamese
Luan Thanh Nguyen1,2, Kiet Van Nguyen1,2,⋆, and Ngan Luu-Thuy Nguyen1,2
17520721@gm.uit.edu.vn, kietnv@uit.edu.vn, ngannlt@uit.edu.vn
1 University of Information Technology, Ho Chi Minh City, Vietnam
2 Vietnam National University Ho Chi Minh City, Vietnam
Abstract. The rise of social media has led to the increasing of com-
ments on online forums. However, there still exists invalid comments which
are not informative for users. Moreover, those comments are also quite
toxic and harmful to people. In this paper, we create a dataset for con-
structive and toxic speech detection, named UIT-ViCTSD (Vietnamese
Constructive and Toxic Speech Detection dataset) with 10,000 human-
annotated comments. For these tasks, we propose a system for construc-
tive and toxic speech detection with the state-of-the-art transfer learning
model in Vietnamese NLP as PhoBERT. With this system, we obtain
F1-scores of 78.59% and 59.40% for classifying constructive and toxic
comments, respectively. Besides, we implement various baseline mod-
els as traditional Machine Learning and Deep Neural Network-Based
models to evaluate the dataset. With the results, we can solve several
tasks on the online discussions and develop the framework for identify-
ing constructiveness and toxicity of Vietnamese social media comments
automatically.
Keywords: Constructive Speech Detection · Toxic Speech Detection ·
Machine Learning · Deep Learning · Transfer Learning
1
Introduction
In the era of technology and the Internet, one of the most important factors
that need to be concerned about is the quality of online discussions. Focusing
on constructive comments and automatically classifying them promotes and
contributes to improving online discussion quality and bringing knowledge for
users. Besides, toxic comments, which cause the shutting down of user comments
completely, are rising dramatically. Hence, filtering toxic comments relied on its
level helps improve online conversations.
In this paper, we introduce the UIT-ViCTSD dataset for identifying construc-
tiveness and toxicity of Vietnamese comments on social media. To ensure the
quality of the dataset, we build a detailed and clear annotation scheme. Thereby,
⋆Corresponding author
arXiv:2103.10069v5  [cs.CL]  6 Sep 2021

--- Page 2 ---

2
Luan Thanh Nguyen et al.
annotators can annotate comments correctly. Moreover, our system for detecting
constructiveness and toxicity is proposed.
We organize the paper as follows. Section 2 reviews related works that are
relevant to our works. Section 3 describes the dataset and defines the meanings
of constructiveness and toxicity of comments. Section 4 introduces our proposed
system for constructive and toxic speech detection. Section 5 describes experi-
ments, results, and error analysis. Finally, Section 6 draws conclusions and future
works.
2
Related Work
Constructiveness of comment is an essential element that positively gives users
useful information and knowledge and promote online conversations. From these
comments, conversations can be extended and more active, provide more informa-
tion for users. Many Natural Language Processing (NLP) researchers all around
the world has concentrated on characteristic. Since 2017, The New York Times
has had full-time moderators to evaluate comments of users on their website.
They then highlight comments that have constructiveness and label them as
NYT Picks [3] manually. In Japan, we can react like or unlike with comments of
other users on Yahoo News. So that Yahoo filter their comments of users and
rank that one by useful or not. A dataset named The Yahoo News annotated
comments dataset was built to find good conversations online [4]. The keyword
constructive was focused recently in 2017 by Napoles et al. [11]. They defined a
new task for identifying good online conversations, called ERICs, which is used
for classifying comments of users and identify good ones.
In 2020, Varada et al. [9] had an in-depth study about the constructiveness
of comments, the main element promoting the quality of online conversations.
They also built a dataset which is mainly about constructive comments named
C3. Furthermore, they discussed the toxicity of comments and demonstrated the
relationship between constructiveness and toxicity. They obtained the results of
constructive comment detection with 72.59% F1-score by the BiLSTM.
In recent years, NLP is increasing with the rise of high-quality datasets.
For Vietnamese, there are several datasets about social media comments such
as Vietnamese Social Media Emotion dataset (UIT-VSMEC) [7] with 6,927
labeled comments and achieved a F1-score of 59.74% by CNN model; Vietnamese
Students’ Feedback dataset (UIT-VSFC) [14] with 16,000 labeled comments and
the F1-score they gained by using Maximum Entropy was 84.03%. Moreover,
there are still datasets about preventing negative comments or hate speech,
like the one presented by Vu et al. [18]. However, Vietnamese is a low-resource
language, and there is no dataset about the constructiveness of comments so
far. Hence, we aim to build a dataset to develop a framework for automatically
identifying the constructiveness and toxicity of Vietnamese comments. With the
results, we hope that we can use it to enhance the nature of online conversations,
create meaningful and informative content, and make social media more useful.

--- Page 3 ---

Constructive and Toxic Speech Detection for Vietnamese Comments
3
3
Dataset
3.1
Task Definition
The main task in this paper is constructive speech detection of Vietnamese
comments. To understand the study, we explain constructive (as label 1) or
non-constructive (as label 0) labels and their examples. Following the guidelines,
annotators annotate comments with one of the two labels.
– Constructive: Comments of users reinforce their point of view for the article.
Frequently, those comments provide lots of information and particularized
opinions and contribute to promoting the topic.
– Non-Constructive: Comments of users which have little information. Their
contents are only about expressing simple emotions and do not have much
meaning.
Furthermore, we also concentrate on another task of toxic speech detection.
With this characteristic, we annotate comments with one of four different labels
consisting of very toxic, toxic, quite toxic, or non-toxic as follows:
– Very toxic: Comments which have offensive contents; directly attacking
individuals and organizations, showing disrespect to others. Especially using
offensive words often causes shutting down conversation rapidly.
– Toxic: Comments whose contents are sarcasm and criticism; having a mockery
attitude; disagreeing with the opinion but with a lack of delicacy and impolite.
– Quite toxic: Comments whose contents might be harmful to people (but
not everyone) in specific contexts express disappointment.
– Non-toxic: Comments which have non-constructive content only express
pure emotions and not make much sense.
Several examples of two tasks in our dataset are shown in Table 1 and Table
2 below.
Table 1: Several examples about constructiveness of comments in our dataset. 1
= Constructive and 0 = Non-constructive.
No. Comment
Label
1
Nội dung của bài viết là câu trảlời cuối đơn giản cho câu hỏi "Khủng
hoảng tài chính là cái gì". Năm 2010,... Cuối cùng một câu trảlời đơn giản
được đưa ra: "Bán mà không ai mua !"... cảthếgiới đều thếthì khó mà
mong đến việc giữvững tốc độtăng trưởng kinh tế!
(The content of this article is the right answer for "What is a financial
crisis?". Finally, the most suitable answer is: "...")
1
2
Cầu mong ông sớm khỏe mạnh
I hope you will get well soon
0
3
Tôi băn khoăn là ... mà không cần chữkí của người mởthẻhay sao ạ? Rồi
còn phải .... Rồi còn phải làm sao nữa ạ?
I fret about ... without the owner’s own signature? Then, ...? What should i
do next?
1

--- Page 4 ---

4
Luan Thanh Nguyen et al.
Table 2: Several examples about toxic levels of comments in our dataset.
No. Comment
Label
1
Đúng là cặn bã ấu dâm!
What a pedophile scum!
Very toxic
2
Ích kỷvà vô ý thức.
Selfish and unconscious!
Toxic
3
Xe Việt Nam vẫn quá đắt và đường xá thì quá kém
Vietnamese cars are still too expensive and the quality of roads are too
poor
Quite toxic
4
70% cơ thểngười là nước mà!
70 percent of the human body is made up of water
Non-toxic
3.2
Dataset Creation
One of the most challenging issues we have to deal with is differences of Vietnamese
language from other high-resource languages as English. A word may have different
meanings in different sentences depending on the context. Also, its implications
cause difficulties in building the Vietnamese dataset. Therefore, we have to refer
to various other researches about the constructiveness of English comments
and that definition in Vietnamese to build a high-quality dataset exactly and
qualitatively.
Figure 1 shows us the progress of building this dataset with detailed steps.
After crawling data, we start to label comments. The comment labeled with the
low inter-annotator agreement (IAA) by members is labeled again as the given
progression. Besides that, we analyze those cases and then update the annotation
scheme again to improve the quality of the dataset.
Fig. 1: The process overview of building our annotated dataset.
Before collecting data, we do several surveys about our social media topic,
which have many comments relevant to our interests. With the obtained results,
we decide to crawl data from comments of users in VnExpress.net3 because there
3 https://vnexpress.net/

--- Page 5 ---

Constructive and Toxic Speech Detection for Vietnamese Comments
5
are huge comments that are useful for our research. Then, we build a tool for
crawling data using Python and BeautifulSoup44 library useful functions for
crawling data. The dataset consists of 10,000 comments and is divided equally
into ten domains, including entertainment, education, science, business, cars, law,
health, world, sports, and news (1,000 comments each domain)5.
Three annotators label each comment in our dataset. Before labeling data, we
built an annotation scheme with detailed and necessary information, which helps
annotators label data quickly and precisely. We describe each task with a detailed
definition. Several examples, as well as easily confused comments, are also listed
in the annotation scheme. Therefore, annotators can label the data easier and
more precisely. We also build a tool for labeling data easily and quickly.
After completing building the dataset, we split it into training, validation,
and test sets with a 70:20:10 ratio by train_test_split function of scikit-learn6.
3.3
Dataset Evaluation
To evaluate the inter-annotator agreement of annotators, we use Fleiss’ Kappa
[1]. With that result, progress becomes more trustworthy.
Am = Pe −P0
1 −P0
(1)
Where:
– Am : The inter-annotator agreement
– Pe
: Expected probability of agreement
among the annotators
– P0: Actual probability of agreement among
the annotators
To understand the definition of each label, annotators have to be trained
strictly and carefully. Hence, we train them with five challenges (200 comments
per round). After the challenges, members of the annotation team understand
how to annotate comments with their labels. With the first challenge, the inter-
annotator agreement is only 21.7% in identifying constructiveness of comments
and 30.4% for toxic speech detection. The inter-annotation agreement in both
tasks is not as high as expected in the first challenge because of differences in
knowledge of each annotator in a separate domain. Thus, after each challenge,
we consider conflicting cases, then we edit and update the annotation scheme.
After five challenges, the inter-annotator agreement we gained for constructive
and toxic speech detection is 59.48% and 58.74% IAA, respectively.
With the task of classifying constructive comments, the final label of a
comment is chosen by the above 2/3 annotators. And the final label of comments
in toxic speech detection is the average of the results of three annotators.
4 https://pypi.org/project/beautifulsoup4/
5 http://nlp.uit.edu.vn/datasets/
6 https://scikit-learn.org/

--- Page 6 ---

6
Luan Thanh Nguyen et al.
3.4
Dataset Analysis
Distribution of Constructiveness To gain an overview of the dataset, we
conduct analyses on it. Figure 2 illustrates the distribution of constructive
comments. We found that constructive comments are usually long comments and
have a huge difference from non-constructive comments.
Fig. 2: Distribution of constructive com-
ments in the dataset.
Fig. 3: The number of constructive and
non-constructive comments on each do-
main.
In addition, we analyze the number of constructive and non-constructive
labels of comments on each domain to make an overview of the distribution of the
dataset. The result is shown in Figure 3. Nevertheless, there are disadvantages we
have to face. That is the imbalance of the dataset. The constructive comments
are still less than non-constructive ones. Hence, we plan to balance the dataset
in future.
The relative between Constructiveness and Toxicity We analyze the
number of constructive comments by their toxic levels to obtain an overview of
the relative between them, as shown in Figure 4. We found that constructive
comments also have toxicity. It proves that toxic contents still provide useful
information for users.
Fig. 4: The number of constructive comments by their toxic levels.

--- Page 7 ---

Constructive and Toxic Speech Detection for Vietnamese Comments
7
Because the number of non-toxic comments is too large compared to the rest
of the comments, we decide to combine the quite toxic, toxic, and very toxic
labels into only one label as toxic. Hence, the task about toxic levels of comments
becomes a problem with classifying a comment into toxic or non-toxic, a binary
text classification task.
4
Proposed System
4.1
System Overview
In this research, we propose a system for identifying the constructiveness and
toxicity of Vietnamese comments. Figure 5 shows an overview of our proposed
system described as follows.
Fig. 5: The proposed system for identifying constructiveness and toxicity of
Vietnamse comments.
4.2
Data Preprocessing
The dataset we built is a collection of texts, and it is an unstructured dataset,
which is why it is difficult to be approached with models without applying
preprocessing methods. Thus, we use popular techniques in NLP for preprocessing
data of dataset. Firstly, we remove HTML tags. Unlike English or other popular
languages, the space in Vietnamese is only the sign for separating syllables, not
words. Tokenizing texts is important, and it directly affects the result of models.
Hence, we tokenize those comments by using ViTokenizer of the library Pivi7.
7 https://pypi.org/project/pyvi/

--- Page 8 ---

8
Luan Thanh Nguyen et al.
Table 3: Several examples about normalizing Vietnamese abbreviations.
Abbreviations Normalization
k, kh, hok, hk
không
oke, okay, oki
ok
vn, Vietnam, VN Việt Nam
In the next step, we normalize texts by building a dictionary for abbreviations.
Several examples are mentioned in Table 3.
Within the main model of our system, PhoBERT, which is mentioned in the
next subsection, we use VNcoreNLP [17] and FAIRSeq [15] for preprocessing
data and tokenizing words before applying to the dataset.
Finally, we eliminate spaces, especially special characters such as capital
letters and symbols, before feeding them into training models. But, we still keep
numbers because it also has essential information, which promotes constructive
features.
4.3
Transfer Learning - PhoBERT
The transfer learning model has attracted increasing attention from NLP re-
searchers around the world for its outstanding performances. One of the SOTA
language models as BERT, which stands for Bidirectional Encoder representations
from transformers, is published Devlin et al. [2]. It is a bi-directional transformer
model for pre-training over lots of text data with no label to understand a
language representation. Then, we fine-tune for specific problems.
For Vietnamese, the SOTA method was first released and called PhoBERT
by Nguyen et al. [13] for solving Vietnamese NLP problems. PhoBERT is a
pre-trained model, which has the same idea as RoBERTa, a replication study of
BERT is released by Liu et al. [10], and there are modifications to suit Vietnamese.
In our proposed system, we use PhoBERT as the primary method for constructive
and toxic speech detection for Vietnamese comments. We set the learning rate of
3e-5 and 24 for batch size.
5
Experiments and Results
5.1
Baseline Systems
Besides our system, we implement various models, including traditional methods
as machine learning and neural network-based models.
Machine learning models
– Logistic Regression: A basic machine learning algorithm for classification,
especially binary task.

--- Page 9 ---

Constructive and Toxic Speech Detection for Vietnamese Comments
9
– Support Vector Machine (SVM): This model is widely used for classifi-
cation, regression and other problems in machine learning.
– Random Forest: An ensemble learning method for classification, regression,
and other problems. It operates by constructing a multitude of decision trees
at the training phase.
Neural networks models
– Long Short-Term Memory (LSTM): This is a Deep Learning method
based on RNN architecture. It is capable of learning long-term dependencies
because of its feedback connections [5].
– Bi-GRU-LSTM-CNN: A customized ensemble model by Huynh et al. [16].
It is a combination of CNN-1D, Bidirectional LSTM and Bidirectional GRU
layers and achieves optimistic results in binary classification task [8].
Unlike machine learning methods, neural network models have different
approaches to the dataset. Before the training model, we use the word-embedding
for models as below.
– fastText: A multilingual pre-trained word vector, including Vietnamese,
released by Grave et al [6].
– PhoW2V: PhoW2V is a pre-trained Word2Vec word embedding for Viet-
namese, which is published by Nguyen et al. [12]. In this research, we use a
PhoW2V word level embedding for preprocessing (300 dims).
5.2
Experimental Settings
For finding suitable parameters of each model, we use the GridSearchCV technique
from sklearn. The final parameters we implemented are presented in Table 4.
Table 4: Suitable parameters of each model for constructive and toxic speech
detection of Vietnamese comments.
Parameters
System
Constructiveness
Toxicity
Logistic Regression
C=100
C=100
SVM
C=1000, gamma=0.001,
kernel="rbf"
C=1000, gamma=0.001,
kernel="rbf"
Random Forest
n_estimators=108,
max_depth=400
n_estimators=108,
max_depth=400
LSTM
units=128,
activation="sigmoid"
units=128,
activation="sigmoid"
Bi-GRU-LSTM-CNN CNN-1D: drop_out=0.2,
Bi-LSTM: units=128,
activation="sigmoid"
CNN-1D: drop_out=0.2,
Bi-LSTM: units=128,
activation="sigmoid"

--- Page 10 ---

10
Luan Thanh Nguyen et al.
5.3
Experimental Results
Before training models, we vectorize texts from the training set, from which
models understand and learn from data. Then, we conduct experiments on our
dataset, and the results of each model are shown in the Table 5 below. We
use metrics as Accuracy and macro-averaged F1-score (%) for evaluating the
performances of models.
Table 5: The experimental results of each model for constructive and toxic speech
detection.
System
Constructiveness
Toxicity
Accuracy F1-score Accuracy F1-score
Logistic Regression
79.91
70.78
90.27
55.35
Random Forest
79.10
73.75
90.03
55.30
SVM
78.00
76.10
90.17
59.06
LSTM + fastText
80.00
76.26
88.90
49.63
LSTM + PhoW2V
78.20
77.42
89.00
49.70
Bi-GRU-LSTM-CNN + fastText
79.90
77.53
89.10
48.88
Bi-GRU-LSTM-CNN + PhoW2V
79.50
77.94
88.90
49.62
Our system
79.40
78.59
88.42
59.40
With the results above, our system achieves the best performance for iden-
tifying constructiveness of comments with the F1-score of 78.59% and 59.40%
F1-score for toxic speech detection. However, the current results are not the
highest ones. In particular, the F1-score result of the toxicity classification task
is relatively low on the test set because of the significant imbalance between the
toxic label and the non-toxic label, according to Figure 4. Moreover, it proves that
the dataset still has noisy data affecting classifier model performance directly.
5.4
Error Analysis
For analyzing errors of predictions by our system, we calculate a confusion
matrix. Figure 6 presents the confusion matrix of our system for constructive and
toxic speech detection. We see that in identifying constructiveness, the highest
confusing cases are wrong to predict constructive (1) instead of non-constructive
(0) with 14% of the incorrect prediction. The confusion matrix of toxic speech
detection shows us that the performance of the model for this task is still not
high. The reason for that confusion is the imbalance of the dataset. Comments
in our dataset are crawled mainly from official online sources, which blocks and
prevents toxic contents on their forum. Hence, the number of toxic comments in
the dataset are much less than the non-toxic ones, and models cannot be trained
well and obtain the highest performances. We plan to improve its quality by
adding more toxic comments from other social media platforms in the future.

--- Page 11 ---

Constructive and Toxic Speech Detection for Vietnamese Comments
11
Fig. 6: Confusion matrix of our system for constructive and toxic speech detection.
6
Conclusion and Future work
This paper presented a new dataset named UIT-ViCTSD, including Vietnamese
comments annotated manually with constructiveness and toxic labels. Firstly, we
built an annotation scheme for labeling comments. In particular, we achieve the
dataset consisting of 10,000 human-annotated comments on ten different domains.
Secondly, we proposed a system for constructive and toxic speech detection with
the state-of-the-art transfer learning model in Vietnamese NLP as PhoBERT.
We achieved 78.59% and 59.40% F1-score for identifying constructive and toxic
comments, respectively. Then, we implemented traditional machine learning and
neural network models. Finally, we analyzed errors of our system on the dataset.
In future, we plan to evaluate the balanced dataset by removing inappropri-
ately annotated comments and inserting new comments with the appropriate
label. Besides, we intend to improve the quality of our dataset and our system in
order to obtain the best results on constructive and toxic speech detection for
Vietnamese social media comments.
References
1. Plaban Kumar Bhowmick, Anupam Basu, and Pabitra Mitra. An agreement measure
for determining inter-annotator reliability of human judgements on affective text. In
Coling 2008: Proceedings of the workshop on Human Judgements in Computational
Linguistics, Manchester, UK, August 2008. Coling 2008 Organizing Committee.
2. Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT:
Pre-training of deep bidirectional transformers for language understanding. In Pro-
ceedings of the 2019 Conference of the North American Chapter of the Association
for Computational Linguistics: Human Language Technologies, Volume 1.
3. Nicholas Diakopoulos. Picking the nyt picks: Editorial criteria and automation in
the curation of online news comments. ISOJ Journal, 6(1):147–166, 2015.

--- Page 12 ---

12
Luan Thanh Nguyen et al.
4. Soichiro Fujita, Hayato Kobayashi, and Manabu Okumura. Dataset creation for
ranking constructive news comments. In Proceedings of the 57th Annual Meeting
of the Association for Computational Linguistics, pages 2619–2626, 2019.
5. Felix A Gers, J¨urgen Schmidhuber, and Fred Cummins. Learning to forget: Contin-
ual prediction with lstm. 1999.
6. Edouard Grave, Piotr Bojanowski, Prakhar Gupta, Armand Joulin, and Tomas
Mikolov. Learning word vectors for 157 languages. In Proceedings of the Eleventh
International Conference on Language Resources and Evaluation (LREC 2018),
Miyazaki, Japan, May 2018. European Language Resources Association (ELRA).
7. Vong Anh Ho, Duong Huynh-Cong Nguyen, Danh Hoang Nguyen, Linh Thi-Van
Pham, Duc-Vu Nguyen, Kiet Van Nguyen, and Ngan Luu-Thuy Nguyen. Emotion
recognition for vietnamese social media text. In Communications in Computer and
Information Science, pages 319–333. Springer Singapore, 2020.
8. Tin Huynh, Luan Thanh Luan, and Son T. Luu.
BANANA at WNUT-2020
task 2: Identifying COVID-19 information on Twitter by combining deep learning
and transfer learning models. In Proceedings of the Sixth Workshop on Noisy
User-generated Text (W-NUT 2020), pages 366–370.
9. Varada Kolhatkar, Nithum Thain, Jeffrey Sorensen, Lucas Dixon, and Maite
Taboada. Classifying constructive comments. arXiv preprint arXiv:2004.05476,
2020.
10. Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer
Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. Roberta: A robustly
optimized bert pretraining approach. arXiv preprint arXiv:1907.11692, 2019.
11. Courtney Napoles, Aasish Pappu, and Joel Tetreault. Automatically identifying
good conversations online (yes, they do exist!). In Eleventh International AAAI
Conference on Web and Social Media, 2017.
12. Anh Tuan Nguyen, Mai Hoang Dao, and Dat Quoc Nguyen. A Pilot Study of
Text-to-SQL Semantic Parsing for Vietnamese. In Findings of the Association for
Computational Linguistics: EMNLP 2020, pages 4079–4085, 2020.
13. Dat Quoc Nguyen and Anh Tuan Nguyen. PhoBERT: Pre-trained language models
for Vietnamese. In Findings of the Association for Computational Linguistics:
EMNLP 2020, pages 1037–1042, Online, November 2020. Association for Computa-
tional Linguistics.
14. K. V. Nguyen, V. D. Nguyen, P. X. V. Nguyen, T. T. H. Truong, and N. L. Nguyen.
Uit-vsfc: Vietnamese students’ feedback corpus for sentiment analysis. In 2018 10th
International Conference on Knowledge and Systems Engineering (KSE), 2018.
15. Myle Ott, Sergey Edunov, Alexei Baevski, Angela Fan, Sam Gross, Nathan Ng,
David Grangier, and Michael Auli. fairseq: A fast, extensible toolkit for sequence
modeling. In Proceedings of the 2019 Conference of the North American Chapter
of the Association for Computational Linguistics (Demonstrations).
16. Tin Van Huynh, Vu Duc Nguyen, Kiet Van Nguyen, Ngan Luu-Thuy Nguyen, and
Anh Gia-Tuan Nguyen. Hate speech detection on vietnamese social media text
using the bi-gru-lstm-cnn model. arXiv preprint arXiv:1911.03644, 2019.
17. Thanh Vu, Dat Quoc Nguyen, Dai Quoc Nguyen, Mark Dras, and Mark Johnson.
VnCoreNLP: A Vietnamese natural language processing toolkit. In Proceedings
of the 2018 Conference of the North American Chapter of the Association for
Computational Linguistics: Demonstrations, New Orleans, Louisiana, June 2018.
18. Xuan-Son Vu, Thanh Vu, Mai-Vu Tran, Thanh Le-Cong, and Huyen Nguyen. Hsd
shared task in vlsp campaign 2019: Hate speech detection for social good. arXiv
preprint arXiv:2007.06493, 2020.

```
