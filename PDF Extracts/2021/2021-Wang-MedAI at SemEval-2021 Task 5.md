---
title: "MedAI at SemEval-2021 Task 5 - PDF Extract"
source_pdf: "2021-Wang-MedAI at SemEval-2021 Task 5.pdf"
pages: 5
extracted_at: "2026-01-24T17:05:09.320781"
---

# PDF Extract: MedAI at SemEval-2021 Task 5

**Source PDF:** 2021-Wang-MedAI at SemEval-2021 Task 5.pdf
**Total Pages:** 5

---

## Content

```
--- Page 1 ---

Proceedings of the 15th International Workshop on Semantic Evaluation (SemEval-2021), pages 258–262
Bangkok, Thailand (online), August 5–6, 2021. ©2021 Association for Computational Linguistics
258
MedAI at SemEval-2021 Task 5: Start-to-end Tagging Framework for
Toxic Spans Detection
Zhen Wang1, Hongjie Fan2 ∗, Junfei Liu3
School of Software and Microelectronics, Peking University
The Department of Science and Technology, China University of Political Science and Law
National Engineering Research Center for Software Engineering, Peking University
{wang.zh, liujunfei}@pku.edu.cn , hjfan@cupl.edu.cn
Abstract
This paper describes the system submitted to 
SemEval 2021 Task 5: Toxic Spans Detec-
tion. The task concerns evaluating systems 
that detect the spans that make a text toxic 
when detecting such spans are possible. To ad-
dress the possibly multi-span detection prob-
lem, we develop a start-to-end tagging frame-
work on the top of RoBERTa based language 
model. Besides, we design a custom loss func-
tion which take distance into account. In com-
parison to other participating teams, our sys-
tem has achieved 69.03% F1 score, which is 
slight lower (-1.8 and -1.73) than the top 1 
(70.83%) and top 2 (70.77%), respectively.
1
Introduction
In recent years, social networks and microblog-
ging sites’ popularity have increased, attracting
more users. With a huge user base, social media
will continue to publish a large amount of user-
generated content.
As the use of social media
increased, other undesirable phenomena and be-
haviors emerged. Social media users often abuse
this freedom to spread abusive or hateful posts or
comments. In many cases, the user-generated con-
tent is offensive or proactive, and users may have to
deal with threats such as cyberattacks or cyberbully-
ing, and other undesirable (Warner and Hirschberg
2012). Therefore, the issue of detecting and pos-
sibly limiting the spread of toxic post has become
increasingly important.
Although several toxicity or abusive language de-
tection datasets (Wulczyn et al. 2016; Borkan et al.
2019) and models (Borkan et al. 2019; Pavlopou-
los et al. 2017; Zampieri et al. 2019) have been
released, most of them classify whole comments or
documents, and do not identify the spans that make
a text toxic. But highlighting such toxic spans can
* Corresponding author.
assist human moderators (e.g., news portals mod-
erators) who often deal with lengthy comments, 
and who prefer attribution instead of just a system-
generated unexplained toxicity score per post. The 
evaluation of systems that could accurately locate 
toxic spans within a text is thus a crucial step to-
wards successful semi-automated moderation.
For this reason, SemEval 2021 set up the task 
Toxic Spans Detection to detect and extract the 
spans that make a text toxic, when detecting such 
spans is possible (Pavlopoulos et al. 2021). To ad-
dress the possibly multi-span extraction problem, 
we develop a start-to-end tagging framework with 
custom distance loss, which can tag the start and 
end position of a toxic span. Based on this scheme, 
we can effectively deal with the multi-span extrac-
tion problem.
The rest of the paper is organized as follows: 
Section 2 provides system overview. Section 3 
describes our approach in detail. Our experiment 
is discussed in Section 4. We conclude our work in 
Section 5.
2 System Overview
2.1 Preprocessing and Word Embedding
The training dataset contains 3 columns:
ID - Contains a unique number to identify each 
training example.
Spans - Contains a list of indexes that indicates 
the position of toxic spans.
Text - Contains the text that need to detect and 
extract the toxic spans.
Note that the spans are not given in text, We 
transformed the indexes to text ﬁrst. Besides, we 
append the ”negative” word to the end of each post 
serving as the indicator. We use word embeddings 
as input to the model. Word embedding is a dis-
tributed vector representation of words (Mikolov 
et al. 2013), capturing the syntactic and semantic in-

--- Page 2 ---

259
formation of words. Effective word embedding can 
get better performance. After comparison, we use 
the RoBERTa-based pre-training language models 
as sentence encoder for word embedding.
2.2 Sequence Tagging
Sequence tagging as a general methods can be used 
in wide applications, such as named entity recogni-
tion, relation extraction, machine reading compre-
hension and so on.
The tagging scheme can be divided into BIO 
(Zheng et al. 2017), BIOES (Huang et al. 2015) and 
others, in which B denotes the ﬁrst token of an 
output span, I denotes subsequent tokens in a span, 
O denotes tokens that are not part of an output span, 
E denotes the last token of an output span and S 
denotes token that is an output span.
3 Model Description
Our model has two steps as follows: 1. Concatenate 
the ”negative” word at end of each post. 2. Obtain 
the word embedding of each token in the post to 
form the ﬁnal representation and predict the start 
and end probabilities for each token as output.
Figure 1 shows the general structure of the sys-
tem. More details for the systems components are 
shown in the following subsections.
3.1 Embedding Layer
As input sequence X of length T is composed of 
word tokens: X = {x1, . . . , xT }. Each token xt is 
replaced with the corresponding vocabulary index 
V (t). The embedding layer transforms the token 
into vector et ∈ Rd which is selected from the 
embedding matrix E according to the index, where 
d is the dimensionality of the embedding space.
In order to indicate the model extract toxic or 
negative spans, we append the word embedding 
vector of ”negative” to the end of each post. We 
take the mean of last two hidden layer’s weight as 
word embedding. The example of sentence con-
structed is also shown in Figure 1.
3.2 Tagging scheme
Although the classical BIOES tag based model can 
obtain competitive result, we think the training 
dataset is not big enough to learn so many tags. 
So different the above methods, we apply the start-
to-end tagging scheme that predicting start and end 
probabilities for each token. The different target se-
quence used by several loss function are as shown 
in Figure 1.
3.3
Loss Function
3.3.1
Classical Cross-Entropy Loss
At the beginning, we use the classical binary cross-
entropy loss, which creates a criterion that mea-
sures the Binary Cross Entropy between the target
and the output. The loss can be described as:
ℓ(x, y) = L = {l1, . . . , lN}⊤
ln = −[yn · log xn + (1 −yn) · log (1 −xn)]
3.3.2
Label Smoothing Loss
Consider that, we are using roBERTa(Liu et al.
2019) as encoder, which is a large pre-trained lan-
guage model. and may cause the over-ﬁtting prob-
lem. To prevent this, we apply the label smooth-
ing(Szegedy et al. 2015) method and change the
’0’ in the target sequence to small value 0.025. The
computation method is same with cross-entropy
loss.
3.3.3
Kullback-Leibler Divergence Loss
Besides the handcrafted label smoothing loss, we
also tried the KLDivLoss, which is a useful dis-
tance measure for continuous distributions and is
often useful when performing direct regression
over the space of (discretely sampled) continuous
output distributions.
The target sequence is the same with the above
binary cross-entropy loss.
The loss can be de-
scribed as:
l(x, y) = L = {l1, . . . , lN}
ln = yn · (log yn −xn)
where the index N spans all dimensions of input
and L has the same shape as input.
3.3.4
Custom Distance Loss
We notice that the cross-entropy loss pay equal
weight to each position’s loss, no matter how far the
distance between it and the target. To penalize more
on the distant false prediction, we propose a custom
distance loss, which use an auxiliary sequence that
generated by insert equal interval from 0 to 1 center
on the ’1’ target. And use the mean dot product to
compute the distance loss.
4
Evaluation
4.1
Data
The shared task provides trail, training and testing
datasets to be used by all participants. The statistics

--- Page 3 ---

260
Figure 1: Start-to-end Tagging Framework
of trail, training and testing dataset can be shown
in Table 1.
Trail
Train
Test
Without span
43
485
394
With span
647
7454
1606
Total
690
7939
2000
Table 1: Datasets for SemEval-2021 Task 5
In this task, we apply the 5-fold cross-validation
method and only use the ofﬁcial training data set
for training and validating.
4.2
Evaluation Measure
To evaluate the responses of a system, we employ
the F1 score, as in Martino et al. 2019. Let system
Ai return a set St
Ai of character offsets, for parts of
the post found to be toxic. Let Gt be the character
offsets of the ground truth annotations of t. We
compute the F1 score of system Ai with respect to
the ground truth G for post t as follows, where ||
denotes set cardinality.
F t
1 (Ai, G) = 2·P t(Ai,G)·Rt(Ai,G)
P t(Ai,G)+Rt(Ai,G)
P t (Ai, G) =
St
Ai∩St
G

St
Ai

Rt (Ai, G) =
St
Ai∩St
G

|St
G|
If St
G is empty for some post t (no gold spans are
given for t), we set F1t (Ai, G) = 1 if St
Ai is also
empty, and F1t (Ai, G) = 0 otherwise. We ﬁnally
average F1t (Ai, G) over all the posts t of an evalu-
ation dataset T to obtain a single score for Ai.
4.3 Experiments
The model is implemented using Pytorch (Paszke 
et al. 2019). We experiment with RoBERTa (Liu 
et al. 2019) based pre-trained language model as en-
coder, including RoBERTa-base-squad2(Deepset), 
twitter-RoBERTa-base-sentiment (Barbieri et al. 
2020) and DistillRoBERTa-base (Sanh et al. 2019) 
And we take the average of last two hidden layers’s 
weights as embedding. Our model is trained with 
AdamW (Loshchilov and Hutter 2017) optimizer 
with initial learning rate 0.00003 and weight de-
cay coefﬁcient 0.012. The max sequence length is 
512 and dropout (Srivastava et al. 2014) rate is 0.5 
to prevent our model from over ﬁtting. And the 
threshold is set to 0.5. The ﬁnal submission which 
scores 69.03 is equipped with both the bi-nary 
cross-entropy loss, custom distance loss and 
voting ensemble mechanism.
4.4 Results and Analysis
In order to evaluate the effect of the custom loss 
function, we compare our approach with its variant.
Variant 1: The variant only use the cross-entropy 
loss.
Variant 2: The variant only use label smoothing 
loss.
Variant 3: The variant only use Kullback-Leibler 
divergence loss.
We take DistillRoBERTa-base as encoder for 
all of the above experiments. Table 2 show that 
the variant 2 model has the lowest score, which

--- Page 4 ---

261
Model
F1 score
Variant 1
0.6662
Variant 2
0.6347
Variant 3
0.6618
Our Model
0.6754
Table 2: Performance of Our System and Its Variants
may cased by the enormous ’0’ label. Besides,
the model with binary cross-entropy loss and cus-
tom distance loss obtains the best result. Thus we
decide to use the model as our ﬁnal ensembling
element.
4.5
Voting Ensemble
As mentioned above, we tried several RoBERTa
besed pre-trained language model as encoder. In
this section, we will discuss the performance dif-
ference between them.
Encoder
F1 score
DistillRoBERTa-base
0.6754
RoBERTa-base-squad2
0.6793
twitter-RoBERTa-base-sentiment
0.6742
Table 3: Performance of Different Encoder
As shown in Table 3, we can ﬁnd that the over-
all score’s difference is slight. But when we take 
a closer look at the performance, the result on sin-
gle example is different. And the RoBERTa-base-
squad2 encoder achieved best result, which may 
caused by the training method.
Text: ”good side of trump? are you kidding me?
trump has no good side all bad, he is divisive, a 
racist and bigot, pathological liar, scammer, tax 
cheat, sexual pervert,”
Golden Spans: [’pathological liar’, ’scammer’, 
’sexual pervert’]
DistillRoBERTa-base: [’racist and bigot’, ’sex-
ual pervert’]
RoBERTa-base-squad2: [’racist’, ’scammer’, 
’sexual pervert’]
twitter-RoBERTa-base-sentiment: [’racist and 
bigot, pathological liar, scammer’, ’sexual pervert’]
As shown above, Complementing and correcting 
each other may improve the overall performance 
due to the difference. This is exactly what ensemble 
learning is good at. Ensembling of several models 
is widely used method to improve the performance 
of the overall system by combining predictions of
several models, such as as for they provide comple-
mentary information.
Considering this, we decide to apply the model
ensemble methods, particularly the vote mecha-
nism was applied. In which, if the number of oc-
currences of one index is bigger than 3 in the all
above model’s predictions, the index will be add to
the ﬁnal result, otherwise it will be exclude. The
ensemble result obtains 69.03% F1 score on the test
data set without any rule correction or dictionary
based post process. Our model ranks in the top 10
among nearly 100 participating teams with slight
lower (-1.8 and -1.73) than the top 1 (70.83%) and
top 2(70.77%), respectively.
5
Conclusion and future work
In this paper, we propose a start-to-end tagging
framework with custom distance loss function for
SemEval-2021 Task 5. The performance of our
model which is equipped with distance loss and
voting mechanism better than its variants. But the
distance loss target is assigned manually, which
may have low generalization ability to different
data set and task. We will try to improve its perfor-
mance and apply this tagging scheme to other task
in future work.
References
Francesco Barbieri, Jose Camacho-Collados, Luis Es-
pinosa Anke, and Leonardo Neves. 2020. TweetE-
val: Uniﬁed benchmark and comparative evaluation
for tweet classiﬁcation. In Findings of the Associ-
ation for Computational Linguistics: EMNLP 2020,
pages 1644–1650, Online. Association for Computa-
tional Linguistics.
Daniel Borkan, Lucas Dixon, Jeffrey Sorensen, Nithum
Thain, and Lucy Vasserman. 2019. Nuanced metrics
for measuring unintended bias with real data for text
classiﬁcation. CoRR, abs/1903.04561.
Deepset.
Farm.
https://github.com/
deepset-ai/FARM.
Zhiheng Huang, Wei Xu, and Kai Yu. 2015.
Bidi-
rectional LSTM-CRF models for sequence tagging.
CoRR, abs/1508.01991.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-
dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
Luke Zettlemoyer, and Veselin Stoyanov. 2019.
Roberta: A robustly optimized BERT pretraining ap-
proach. CoRR, abs/1907.11692.
Ilya Loshchilov and Frank Hutter. 2017.
Fixing
weight decay regularization in adam.
CoRR,
abs/1711.05101.

--- Page 5 ---

262
Giovanni Da San Martino, Seunghak Yu, Alberto
Barr´on-Cede˜no,
Rostislav
Petrov,
and
Preslav
Nakov. 2019. Fine-grained analysis of propaganda
in news articles. CoRR, abs/1910.02517.
Tomas Mikolov, Kai Chen, Greg Corrado, and Jeffrey
Dean. 2013. Efﬁcient estimation of word represen-
tations in vector space. CoRR, abs/1301.3781.
Adam Paszke, Sam Gross, Francisco Massa, Adam
Lerer, James Bradbury, Gregory Chanan, Trevor
Killeen, Zeming Lin, Natalia Gimelshein, Luca
Antiga, Alban Desmaison, Andreas Kopf, Edward
Yang, Zachary DeVito, Martin Raison, Alykhan Te-
jani, Sasank Chilamkurthy, Benoit Steiner, Lu Fang,
Junjie Bai, and Soumith Chintala. 2019.
Py-
torch: An imperative style, high-performance deep
learning library.
In H. Wallach, H. Larochelle,
A. Beygelzimer, F. d'Alch´e-Buc, E. Fox, and R. Gar-
nett, editors, Advances in Neural Information Pro-
cessing Systems 32, pages 8024–8035. Curran Asso-
ciates, Inc.
John Pavlopoulos, L´eo Laugier, Jeffrey Sorensen, and
Ion Androutsopoulos. 2021. Semeval-2021 task 5:
Toxic spans detection (to appear). In Proceedings of
the 15th International Workshop on Semantic Evalu-
ation.
John Pavlopoulos, Prodromos Malakasiotis, and Ion
Androutsopoulos. 2017. Deeper attention to abusive
user content moderation. In Proceedings of the 2017
Conference on Empirical Methods in Natural Lan-
guage Processing, pages 1125–1135, Copenhagen,
Denmark. Association for Computational Linguis-
tics.
Victor Sanh, Lysandre Debut, Julien Chaumond, and
Thomas Wolf. 2019. Distilbert, a distilled version
of BERT: smaller, faster, cheaper and lighter. CoRR,
abs/1910.01108.
Nitish Srivastava, Geoffrey Hinton, Alex Krizhevsky,
Ilya Sutskever, and Ruslan Salakhutdinov. 2014.
Dropout: A simple way to prevent neural networks
from overﬁtting. Journal of Machine Learning Re-
search, 15(56):1929–1958.
Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe,
Jonathon Shlens, and Zbigniew Wojna. 2015. Re-
thinking the inception architecture for computer vi-
sion. CoRR, abs/1512.00567.
William Warner and Julia Hirschberg. 2012. Detecting
hate speech on the world wide web. In Proceedings
of the Second Workshop on Language in Social Me-
dia, pages 19–26, Montr´eal, Canada. Association for
Computational Linguistics.
Ellery Wulczyn, Nithum Thain, and Lucas Dixon. 2016.
Ex machina: Personal attacks seen at scale. CoRR,
abs/1610.08914.
Marcos Zampieri, Shervin Malmasi, Preslav Nakov,
Sara Rosenthal, Noura Farra, and Ritesh Kumar.
2019. SemEval-2019 task 6: Identifying and catego-
rizing offensive language in social media (OffensE-
val). In Proceedings of the 13th International Work-
shop on Semantic Evaluation, pages 75–86, Min-
neapolis, Minnesota, USA. Association for Compu-
tational Linguistics.
Suncong Zheng, Feng Wang, Hongyun Bao, Yuexing
Hao, Peng Zhou, and Bo Xu. 2017.
Joint extrac-
tion of entities and relations based on a novel tag-
ging scheme.
In Proceedings of the 55th Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 1227–1236,
Vancouver, Canada. Association for Computational
Linguistics.

```
