---
title: "Finding Answers From The - PDF Extract"
source_pdf: "2015-Schmidhuber-Finding Answers From The.pdf"
pages: 19
extracted_at: "2026-04-03T11:05:33.533573"
---

# PDF Extract: Finding Answers From The

**Source PDF:** 2015-Schmidhuber-Finding Answers From The.pdf
**Total Pages:** 19

---

## Content

--- Page 1 ---

Finding Answers from the Word of God:
Domain Adaptation for Neural Networks in
Biblical Question Answering
Helen Jiahe Zhao, Jiamou Liu
Department of Computer Science
The University of Auckland
New Zealand
jiamou.liu@auckland.ac.nz
October 30, 2018
Abstract
Question answering (QA) has signiﬁcantly beneﬁtted from deep learning tech-
niques in recent years. However, domain-speciﬁc QA remains a challenge due to
the signiﬁcant amount of data required to train a neural network. This paper stud-
ies the answer sentence selection task in the Bible domain and answer questions by
selecting relevant verses from the Bible. For this purpose, we create a new dataset
BibleQA based on bible trivia questions and propose three neural network mod-
els for our task. We pre-train our models on a large-scale QA dataset, SQuAD,
and investigate the effect of transferring weights on model accuracy. Furthermore,
we also measure the model accuracies with different answer context lengths and
different Bible translations. We afﬁrm that transfer learning has a noticeable im-
provement in the model accuracy. We achieve relatively good results with shorter
context lengths, whereas longer context lengths decreased model accuracy. We
also ﬁnd that using a more modern Bible translation in the dataset has a positive
effect on the task.
1
Introduction
The desire for a computer system that could answer natural language questions has
been an ability that signiﬁes artiﬁcial intelligence. In recent years, neural networks
and machine learning have become popular approaches for question answering (QA)
tasks within the natural language processing (NLP) community. One problem with this
approach is the expense of creating a suitable dataset for speciﬁc domains. Machine
learning works well under the assumption that training and test are from the same
distribution. Therefore, the tasks that machine learning can solve is highly dependent
on the dataset. As a result, most of neural QA research predominantly uses existing
datasets, and not as much work has been done for domain-speciﬁc QA.
1
arXiv:1810.12118v1  [cs.IR]  26 Oct 2018

--- Page 2 ---

In this paper, we focus on the task of answer sentence selection, speciﬁcally to
answer questions by selecting verses from the Bible as answers. This task takes as
input a question and a context paragraph and asks for a sentence from the context that
contains the answer to the given question. In our case, the context would consist of
passages from the Bible.
The Bible is not only an inﬂuential literary work but is also the most important
religious document amongst Christians. So far, not much work has been done using
this corpus within QA or other NLP tasks. Even today, it is still widely read and
studied amongst both the religious and the secular community. The Bible is often seen
as a source of wisdom where people turn to seek answers to the big questions in life. A
QA system that can answer a question using passages from the Bible has the potential
to be very beneﬁcial for the users.
A biblical QA system could be useful for non-Christians, seeking to learn more
about the Bible. They might ask questions such as: “Who is Jesus?”, “What will
happen when I die?”. The system could then output a series of relevant verses as
answers. The same system could also be useful for scholars seeking to use the Bible as
a historical or archaeological document. They could be interested in questions such as,
“When did Babylon destroy the Jerusalem temple?”, “Where was the city of Jericho
located?”. Such questions can be answered from the relevant passages that described
the historical aspect of the Bible. Finally, one of the widest use cases could be from the
Christian community who uphold the Bible as the ultimate authority for their faith and
life. They could be interested in a wide variety of questions, ranging from theological to
practical. For example, “Is salvation by faith or by works?”, “How should I treat people
that have wronged me?”, “How should I pray?”. While many of these questions can
also be answered through a search engine, the quality of results from search engines
can often be questionable and answering using passages directly from the Bible is a
valuable resource from a Christian perspective.
Contribution.
The goal of the research is to investigate neural-based methods for
answering biblical question through verse selection. (1) Since large-scale datasets are
needed for efﬁcient learning using neural network methods, our ﬁrst contribution in-
volves the creation of a new dataset BibleQA. The dataset consists of Biblical questions
and the corresponding verse as derived from an existing set of questions that is avail-
able on the Internet. (2) Then, for biblical sentence selection, we design three answer
selection models based on different neural network architectures. Each of these models
takes as input a question and an answer verse and outputs a predicted probability of the
verse containing the answer to the question. (3) Thirdly, we leverage transfer learning
techniques by pre-training the models on a larger QA dataset and provide insight into
the effect of domain adaptation used in QA tasks. Our experiments also reveal how
changing context lengths affects the performance of answer selection, and reveals new
insights regarding various Bible translation.
2

--- Page 3 ---

2
Related Work
From a text retrieval perspective, question answering embodies the task of ﬁnding the
relevant piece of text containing the answer and subsequently extracting the answer
[26]. This view led to open-domain QA, which encompasses the majority of today’s
QA systems. In recent years, QA began incorporating machine learning, with the IBM
Watson being one of the most famous systems [10]. The primary approach behind
Watson is extensive data, statistical and machine learning analysis. Several other neu-
ral network approaches have also been explored. Iyyer et al. used neural networks to
answer quiz bowl type questions, where given a description the task is to identify the
subject being discussed [14]. Kumar et al. extended simple RNN models with an atten-
tion mechanism to enable transitive reasoning and made steps towards reasoning-based
QA [15]. Malinowski proposed a model using both CNN and LSTM to incorporate im-
age recognition and QA [16].
Answer sentence selection is a QA task which involves selecting the sentence that
is the most likely to contain the answer. Early approaches were predominantly syntac-
tical, using the idea that the question and answer sentence should relate to each other
loosely through syntactical transformations. Wang et al. proposed a generative model
that transforms the answers to the questions [29]. Wang and Manning introduced a
probabilistic model that models tree-edit operations on dependency parse trees, mak-
ing use of sophisticated linguistics features [28]. Other similar models include using
dynamic programming to ﬁnd the optimal tree edit sequences [32]. The main draw-
back of these approaches is that they require too much feature engineering and were
difﬁcult to adapt to new domains. Only recently, researchers started applying neural
network models. Yu et al. used CNN models for answer sentence selection on the
TREC benchmark [33]. Feng et al. also proposed several CNN models for answer
sentence selection task. Wang and Nyberg constructed a joint-vector based on both the
question and the answer using an LSTM model [27].
NLP in religious text.
Recently, works start to emerge that use NLP for religious text
mining. The Bible is a good resource for various linguistics tasks, and has been used as
a resource to improve and investigate computational linguistics tasks. Hu applied un-
supervised learning to analyse Proverbs and Psalms. They clustered Psalms by content
and saw how the outcome matches the literary form of the Psalms [13]. Their ﬁndings
mostly matched the works by biblical scholars, but have also made unique contribu-
tions that were only made possible through machine learning methods. Tschuggnall
and Specht explored grammar-based text analysis for authorship attribution in the Bible
[25]. Faigenbaum et al. used novel image processing and machine learning algorithms
for authorship detection [9]. While NLP has undoubtedly given the Biblical scholars a
new method for biblical analysis, the Bible in and of itself is also an invaluable corpus
for computational linguistics research. Buchler et al. used seven English translations
of the Bible to investigate the techniques behind historical text re-use detection process
and examine algorithms for paraphrase detection [5]. The Bible provides a good test
bed for paraphrase detection as there exist several different translations all stemming
from the same origin. Agi´c et al. [1] used the Bible to learn part-of-speech (POS)
3

--- Page 4 ---

taggers for low-resource languages such as Akawaio, Aukan, or Cakchiquel for which
the Bible is only partially translated. They learned POS taggers for 100 languages,
and performs much better (20 −30%) than state-of-the-art unsupervised POS taggers
induced from Bible translations.
Transfer learning in NLP.
Transfer learning and domain adaptation have been very
successful with cross-domain machine learning, especially when we have a lot of data
in one domain but a similar domain of interest does not have enough data for learning
purposes. Computer vision has primarily beneﬁtted from transfer learning [19, 34].
Large-scale image data such as ImageNet [7] is particularly challenging to obtain and
process and researchers want to make use of the existing image data as much as possi-
ble, and many have employed transfer learning in various image processing tasks. Due
to the success of transfer learning in computer vision, transfer learning has been used
in NLP task such as sentiment analysis [3], POS tagger [4], and machine translation
[2]. In particular, transfer learning has recently begun to be applied in QA. Glorot et
al. used transfer learning to examine how a system trained to answer questions from
one knowledge base could answer questions from another knowledge base [11]. Yang
et al. used transfer learning for question generation [31]. For applications of domain
adaptation in neural models, the most common and the most straightforward approach
is to pre-train the model on the source data and then ﬁne-tune the parameters on the
data from the target domain [18, 30]. Overall, transfer learning is essential for machine
learning researchers to make use of smaller datasets, and we can expect that it will be
used increasingly more in the future.
3
BibleQA: Bible Question-Answering Dataset
Answer sentence selection.
QA tasks are classiﬁed by the level of structure in the
context and the type of the task. The answer can be sentence-level by selecting the
relevant sentence from the context; span-level by choosing a span of the text from
the context as the answer; or the answer can be generated using predicate values
and sentence generation models. This paper performs sentence selection from lim-
ited unstructured data based on the BibleQA dataset. Speciﬁcally, the input (Q, A)
contains a list of M questions Q = (q1, q2, . . . qM), and a list of candidate answers
A = (a1,1, a1,2, . . . , a1,N1; . . . ; aM,1, aM,2, . . . , aM,NM ), where aj,k is the kth candi-
date of the jth question. The output will be evaluated likelihood pj,k ∈[0, 1] for each
aj,k to be the correct answer sentence for question qj. Finally, the output answer aj,k∗
corresponding to qt is the one with the highest likelihood, i.e., k∗= arg maxk{pj,k |
1 ≤k ≤Nj}.
SQuAD.
The Stanford Question Answering Dataset (SQuAD) is currently the largest
span-based dataset, containing more than 100, 000 QA pairs from more than 500 Wikipedia
articles [22]. The dataset is span-based, meaning that given a context paragraph and a
question, the dataset outputs the span of text that is the most likely to be the answer to
the question. Since we are interested in a sentence-level task, we converted SQuAD
to a new sentence-level dataset. For each original context paragraph, we divide the
4

--- Page 5 ---

paragraph into sentences. Then, we label each sentence based on whether or not the
originally given span answer is within the sentence. If yes, then the sentence is labelled
as 1, and all the other sentences within the same paragraph are labelled as 0.
BibleQA1.
Although the Bible was written over a period of 1000 years by 40 differ-
ent people, it tells a uniﬁed story regarding the overarching theme of God’s redemptive
work in the past, present, and future. The Bible contains 39 books in the Old Tes-
tament and 27 books in the New Testament. The Old Testament contains a variety
of literary genre, including historical narrative, wisdom books, poetry, and prophecy.
The historical books describe the establishment of Israel as the chosen people of God
and their separation from God due to sin, and the prophetic books prophesied about a
coming Messianic King who will rescue humanity from the bondage of sin. The ﬁrst
part of the New Testament contains stories about Jesus’ life and teachings, who was
widely considered as the Messiah prophesied by the Old Testament prophets. The rest
of New Testament consists of letters of instructions that are extensively read today and
are foundational in the Christian teaching. The Bible is a collection of ancient religious
literature that has undeniable inﬂuence over culture and society, affecting areas ranging
from languages, literature, to law and sciences [6]. It was found through a study that
two-thirds of the American people believe that the Bible holds the answers to all or
most of life’s basic questions [21]. From these, we can see the multi-faceted potential
of the Bible being used in QA systems.
There is no existing dataset directly suitable for sentence-level QA task for the
Bible, and we set out to create our dataset using some existing available questions. We
used a freely available set of 1001 trivia questions from the Bible2 as the basis for the
dataset. The trivia question set consists of question, answer, and the corresponding
verse from the Bible which is relevant to the answer.
Using this resource, we derived a sentence-level dataset which we will name BibleQA.
We extracted verses surrounding the target verse as candidate answers. The actual verse
is labelled with 1, and all the other verses are labelled with 0. There were also some
questions from the original list that wasn’t very suitable to answer using the Bible, es-
pecially questions that we cannot directly ﬁnd answers from the Bible such as “Which
book of the Bible has the most chapters in it?”. Therefore, we ﬁltered out those ques-
tion and added more questions manually. We ended up with 886 questions in total in
the BibleQA dataset. An example is given below:
Question: What is the name of Jesus’ mother?
Verse 1: [Matthew 1:17] So all the generations from Abraham to David are fourteen
generations; from David to the exile to Babylon fourteen generations; and from
the carrying away to Babylon to the Christ, fourteen generations.
Verse 2: [Matthew 1:18] Now the birth of Jesus Christ was like this; for after his
mother, Mary, was engaged to Joseph, before they came together, she was found
pregnant by the Holy Spirit.
1https://github.com/helen-jiahe-zhao/BibleQA
2https://biblequizzes.org.uk/
5

--- Page 6 ---

Verse 3: [Matthew 1:19] Joseph, her husband, being a righteous man, and not willing
to make her a public example, intended to put her away secretly.
Answer: [0, 1, 0]
It is also noteworthy that there are many different English translations of the Bible,
each using a different translation philosophy and results in slightly different verses that
consist of the same idea. We decide to make use of digitalized versions of the Bible
found on GitHub3. We retrieve the verses from four public domain translations: King
James Version (KJV), Young’s Literal Translation (YLT), American Standard Version
(ASV) and World English Bible (WEB). King James Version was published in 1611,
and is still one of the most widely used Bible translations and considered by many as the
most authentic. Young’s Literal Version, from 1862, follows a strictly literal translation
philosophy and translated into English from Greek and Hebrew almost word by word.
American Standard Version from 1901 was very popular in the 20th century in its
usage by biblical scholars. The World English Bible is an updated version of the ASV
and is the most modern translation out of all four being published in 2000. We chose
these four translations for their variety in the use of English and translation method. A
comparison of the translations is shown below. From the comparison we can see that
each translation has its subtle differences, yet substantially different. For BibleQA we
used four translations for each question and answer pair, which meant that the total size
of the dataset ends up with 3544 question-answer pairs.
KJV: Now the birth of Jesus Christ was on this wise: When as his mother Mary was
espoused to Joseph, before they came together, she was found with child of the Holy
Ghost. (Matthew 1:18)
YLT: And of Jesus Christ, the birth was thus: For his mother Mary having been be-
trothed to Joseph, before their coming together she was found to have conceived from
the Holy Spirit. (Matthew 1:18)
ASV: Now the birth of Jesus Christ was on this wise: When his mother Mary had been
betrothed to Joseph, before they came together she was found with child of the Holy
Spirit. (Matthew 1:18)
WEB: Now the birth of Jesus Christ was like this; for after his mother, Mary, was
engaged to Joseph, before they came together, she was found pregnant by the Holy
Spirit. (Matthew 1:18)
4
Methodologies
For our task, we employ three main neural network models for comparison purposes:
one using recurrent neural network (RNN), one using convolutional neural networks
(CNN), another using an adapted Bi-direction Attention Flow model (BiDAF) ﬁrst
suggested by Seo et al. [23]. The three models all follow the same general architecture,
and the subsequent sections will describe the architecture in more detail:
1. Embedding: The input question and answers are ﬁrst pre-processed and con-
verted to word vectors.
3https://github.com/scrollmapper/bible databases
6

--- Page 7 ---

2. Encoding: The embedded sentences are then processed and encoded, to obtain
one single vector representation that captures the sentence.
3. Answer Selection: Based on the encoded question and answer, select an answer
as the predicted output.
4.1
Word Embedding
Word embedding captures word context using distributed word vectors. The underlying
intuition is that words in similar environments tend to have similar meanings [17]. Here
we make use of both GloVe vectors as well as word2vec. word2vec is modelled as a
shallow, two-layered neural network which uses stochastic gradient descent and back-
propagation to iteratively make a word embedding more similar to that of its neighbor
words. The model successfully reduces the complexity of the non-linear hidden layer
and made it possible to learn high dimension word vectors on a signiﬁcant amount of
data. GloVe is an alternative unsupervised learning algorithm to word2vec vectors,
which is also used to obtain vector representation for words [20]. GloVe has pre-
trained vectors available online, that were trained on 6 billion tokens from Wikipedia
and various news outlets, making it very suitable for training on SQuAD.
As the Bible consists of many words and names that are unique to its context,
we also trained our own word vectors for the Bible. We used a combination of all
four aforementioned English translations for the word vector training, which includes
around 3 million words altogether. In the vector training, we used a context window
size of 5 and the Continuous Bag-of-Words algorithm to train vectors of dimension 200.
The resulting word vectors were able to capture the general semantics of the Bible-
speciﬁc vocabularies. Below are some of the most similar words for a few selected
words in descending order of similarity, using the derived word vectors. From these
lists, we see that the most similar words for ‘God’ captures many qualities and roles
God is seen to have throughout the Bible. The most similar words for ‘David’ are other
names who were closely related to him: Saul, his primary adversary; Absalom and
Solomon, his sons; Joab his army commander and Jonathan his best friend.
God: lord, saviour, holiness, mercy, lovingkindness, sworn, redeemer, salvation, jeho-
vah, endureth
sin: trespass, sins, guilt, guilty, transgression, forgiven, sinned, iniquity, forgive, igno-
rance
david: saul, absalom, joab, abimelech, solomon, abner, jonathan, abraham, achish,
samuel
The trained word vectors were concatenated with the GloVe vectors in the transfer
learning process so that the training on BibleQA would be more meaningful.
4.2
Models for the QA System
The baseline model.
This model acts as the basis of comparison for all other results.
The model uses a random function to uniformly randomly generate an output in the
7

--- Page 8 ---

range [0, 1] for each data point. The baseline gives us a model that performs at a level
that does not involve any learning and simply assigning a random prediction for each
question- answer pair. The baseline is then compared with our models to evaluate the
improvement made by more sophisticated models.
The RNN model.
Recurrent networks are designed to model sequences, allowing
the users to work with sequences while preserving structural information. They are
particularly useful in NLP tasks due to the sequential nature of languages. A recur-
rent network consists of loops, where the output of a particular layer is passed back
to the same layer as input. This allows information to persist and capture long-term
dependencies such as those that appear in sequences. One of the most popular imple-
mentations of RNN is the Long Short-Term Memory (LSTM), which was introduced
to mitigate the vanishing gradients problem [12]. As the sequence grows longer, the
distance between the current word and the dependent context grows longer. However,
this means that the error gradients in later steps in the sequence diminish quickly in the
back-propagation and do not reach earlier input signals, hence the gradients “vanish”.
This makes it very difﬁcult to capture relevant information. LSTM introduces a vector
that acts as a memory cell, which preserves gradients over time. The access to the
memory cell is controlled by gating components that can be thought of as logical gates.
Our RNN model makes use of LSTM layers to produce vector representations of
the question and answer phrases. The output is obtained as a probability between [0, 1]
that indicates the similarity between the question vector and the answer vector. This is
based on the intuition that sentences that have closer vectors should be more similar,
and therefore the answer should be more relevant to the question.
The word embedding layer transforms each word into a word vector. A question
is then a sequence of word vectors ⃗x = (x1, x2, . . . , xt) and an answer is another
sequence of word vectors ⃗y = (y1, y2, . . . , yt′). The encoding procedure applies two
LSTMs, one for questions Q and the other for answers A: For each example (⃗x, ⃗y), it
sets for each t
st = (Ct, ht) = RLSTM(st−1, xt−1), and
s′
t = (C′
t, h′
t) = R′
LSTM(s′
t−1, yt−1)
where st (s′
t) is the tth state, Ct (C′
t) is the memory-cell states, and ht (h′
t) is the output
state and RLSTM (R′
LSTM) is the LSTM networks for the question (answer). The output
would be m = (Qe, Ae) where Qe = (h1, h2, . . . , ht), Ae = (h′
1, h′
2, . . . , h′
t). Finally,
we concatenate the question and answer vectors, pass them through a ﬁnal layer which
uses the sigmoid activation function σ =
1
1+e−x , and obtain predicted likelihood for
the answer being the correct one for the question. Fig. 1 shows an overview of the
layers.
The CNN model.
CNNs are special feed-forward neural networks with fully con-
nected layers and consisting of convolutional and pooling layers. These specialized
layers are useful for ﬁnding strong local information present within the input regard-
less of the position of the signals, e.g., in a QA task, a sentence may contain a key
phrase that strongly indicates it as the answer to a question. In NLP, a CNN network
8

--- Page 9 ---

Figure 1: Recurrent Neural Network Model
Figure 2: Convolutional Neural Network Model
ﬁrst takes a sequence of words and applies a ﬁlter over each n-gram of the sequence
obtained by a sliding window of k words. The ﬁlter transforms the n-gram into a d-
dimensional vector that captures important properties of the words. Finally, the pooling
layer combines all the d-dimensional vectors into one single d-dimensional vector by
taking a max or average operation over each dimension of the vector. This ﬁnal vector
is then used for further processing in the neural network since it now contains some of
the most important local information in the entire sequence.
Our CNN model uses the convolutional and pooling layers to represent the question
and answer phrases. We also use a dropout layer to regulate the weights and avoid
overﬁtting. For each question and answer sequence, the convolution layer applies a
kernel across the sequence, transforms it using a ﬁlter, passes through a max-pooling
layer to obtain the element-wise maximum, and ﬁnally passes through an output layer
which returns a prediction.
The convolution and max-pooling layers for each question ⃗x and answer ⃗y is:
Qc
i = f

W T⃗xi:i+k−1 +⃗b

and Ac
i = f

W T⃗yi:i+k−1 +⃗b

Qv
k = max
1<i<m Qc
i[k] and Av
i = max
1<i<m Ac
i[k]
where k is the window size, f is the relu activation function f(x) = max{0, x}, W
is the ﬁlter vector that performs the linear transformation and ⃗b is the bias parameter
of the network. Finally, the output layers are the same as for the RNN model. Fig. 2
shows an overview of the layers.
9

--- Page 10 ---

Figure 3: Modiﬁed Bidirectional Attention Flow Model
BiDAF Model.
The BiDAF model was proposed for the SQuAD dataset for span-
level QA tasks [23]. The original model was used to ﬁnd the start and end indices of the
answer to a question within a context paragraph: The question and context paragraphs
are ﬁrst converted to vectors using both word and character embeddings then combined
to form a phrase embedding using LSTM. The question and context paragraphs are
then combined to produce a set of query-aware vectors for every word in the context.
Finally, another LSTM is used to scan the context paragraph, and the output layer
produces the start and end indices for the question.
For our sentence-level task, we modify the original BiDAF model slightly. We
use the candidate sentences as the context in the original model, eliminate the use of
character-embeddings, and output only the probability of the answer sentence being
the correct answer to the question. Fig. 3 shows an overview of the layers.
The word and phrasal embedding layers are similar to the RNN model in using
LSTM, whose result contains the matrix representations of a question q and a candidate
answer a. Following that, Q2C and C2Q are two layers that compute the “attention”
for the question and answer which is essentially the interaction between question and
answers. More formally, we use U:i to indicate the ith column vector of any matrix U.
The bidirectional attention is determined by a similarity matrix Sj,k between the jth
answer word and the kth question word, deﬁned as Sj,k = α(a:j, q:k) where α(⃗a, ⃗q) is
a trainable scalar function that represents the similarity between vectors ⃗a, ⃗q. The Q2C,
or query to context layer, signiﬁes which answer words have the closest similarity to
one of the question words. The C2Q, or context to query layer, determines which
question words are the most relevant to each answer word. The exact deﬁnition of Sj,k
and Q2C, C2Q can be found in [23].
The Q2C and C2Q are then concatenated with the answer embedding to output
query-aware vector representations of the context words; it takes the form of a matrix
G, whose jth column is
Gj = β(A:j, ˜
Q:j, ˜
A:j)
where β is a trainable function that combines the three representations. The result is
then passed on to one more LSTM layer to output representation matrix m, and ﬁnally
to the output layer which predicts the probability of a being the answer of q.
10

--- Page 11 ---

5
Experiments
5.1
Experiment Setup
We performed experiments for each of the baseline, RNN, CNN and BiDAF model.
For any dataset, we use 70% of the samples for training and 30% for testing. Out of
the 70% training data points, 10% will be used as the validation set for monitoring
overﬁtting. At each epoch, the model trains on the training sets and calculates the loss
and accuracy concerning both the training and validation set. If the validation loss
is much higher than the training loss and the validation accuracy is much lower than
training accuracy, then we can conclude that the model is overﬁtting to the training set
and will need to modify our model accordingly.
We used the GloVe word vectors (dimension d = 100) for training the SQuAD
models, and both GloVe and word2vec vectors for the BibleQA models where the
word2vec vectors (d = 200) are trained on 4 versions of the Bible. The loss function
that our models will learn to minimize is the binary cross entropy, deﬁned as:
L(Θ) = −1
N
N
X
i=1
(yi · log(pi) + (1 −yi) · log(1 −pi))
where Θ is the set of parameters, N represents the number of training instances, pi is
the probability of class 1, 1 −pi is the probability of class 0, and yi ∈{0, 1} is the
true label of the ith observation. Here, the value of pi is found by the probability of
the activation layer using a sigmoid activation: For weight vector Θ and input vector
⃗x, pi =
1
1+e−Θ·⃗x .
We used the adaptive gradient (AdaGrad) optimizer to train the neural networks,
which is a modiﬁed stochastic gradient with per-parameter learning rate [8]. The learn-
ing rate of a model determines the rate of update between each iteration of backpropa-
gation. AdaGrad allows the learning rate to adapt based on the parameters. It performs
larger updates for infrequent parameters and smaller updates for frequent parameters,
and often improves convergence in tasks where the data is sparse – such as NLP and
image recognition. Let gτ = ∇L(Θ) be the gradient at iteration τ. The per-parameter
update for AdaGrad uses the following formula:
Θτ+1 = Θτ −
η
p
Gτ,τ
gτ
where η is the learning rate, and Gτ,τ = Pτ
j=1 g2
j,τ produces a scaling factor for the
parameter Θτ. This leads to a different learning rate update for each parameter based
on the scaling factor and the learning process is adaptive.
For our experiments, we will use two metrics to evaluate their performance: (1)
F1 score, a widely-used accuracy indicator, is deﬁned as F1 = 2PR/(P + R) where
P and R are precision and recall, resp. (2) Mean reciprocal rank (MRR) which com-
monly measures accuracy of ranked outputs, and is applicable here as we are essentially
ranking the candidate sentences for each question. MRR is deﬁned as 1
n
Pn
i=1 rank−1
i
where n is the number of questions and ranki is the rank of the correct answer of the
ith question.
11

--- Page 12 ---

Model
Transferred Weights
F1
MRR
Baseline
No
0.35
0.59
RNN
No
0.45
0.56
Yes
0.54
0.61
CNN
No
0.39
0.58
Yes
0.48
0.53
BiDAF
No
0.40
0.59
Yes
0.48
0.53
Table 1: Model Comparison Before and After Weight Transfer
5.2
Experiment 1: Transfer Learning Parameter Tuning
Goal and method. The ﬁrst experiment investigates the effect of transfer learning on
the model accuracy. We pre-train the model on the SQuAD dataset and compare that
with training only on BibleQA. For each model, 1) we ﬁrst run the model on BibleQA
to obtain a set results. 2) Then, we train the same model on SQuAD to obtain the
trained weights. 3) Finally, we run the model on BibleQA once again using the trained
weights from SQuAD and perform weight ﬁne-tuning once again. We then compare
the results of each model to see whether there are improvements from before using the
transferred weights. We tune parameters such as learning rate and epoch to ﬁnd the best
performing model. We ﬁnd that a learning rate of η = 0.001 worked the best for the
RNN and BiDAF model, and η = 0.0001 for the CNN model. We use an early stopping
mechanism for determining the optimal number of epochs trained, which monitors the
validation loss at each epoch and stops the training once the model stops improving.
We set the patience to 10, which means that the model will wait for 10 epochs before
terminating the training. Optimal results are achieved with 20 to 30 epochs.
Results and analysis.
Table 1 contains the results we obtained from before and after
the weight transfer. We can see that using the transferred weight improves the F1
results by 0.08 to 0.09 (which is around 20%-30% improvement). This shows that
just as we hypothesized, pre-training had a positive effect on the training accuracy.
However, while the F1 score increases with transferring weights, the MRR of the model
decreased by 0.05 and 0.06 for the CNN and BiDAF model, with only the RNN model
increasing by 0.05. This was surprising as it is often assumed that there is a correlation
between different evaluation measures – that a higher F1 would also result in a higher
MRR. By considering what the MRR is measuring, it seems that these models had
a higher average ranking for the correct output. However since these models also had
lower F1, they are less likely to choose the correct answer as the top ranking answer. So
while the models improved the F1 score, it is choosing the correct output more often,
but it also ranks the correct answer lower in the cases where the model incorrectly
predicts the results. This is an interesting phenomenon and will be worth looking into
in the future. Out of the three models, the RNN model performs the best overall with
the highest F1 score both before and after weight transfer, and the highest MRR after
weight transfer.
12

--- Page 13 ---

5.3
Experiment 2: Answer Context Length
Goal and method. The second experiment aims to ﬁnd the variation of prediction
results by changing the length of the answer context, or in other words, the number
of candidate sentences for each question. During the dataset construction phase, af-
ter we identify the verse that corresponds to the correct answer to a question, we in-
clude a different number of context verses surrounding the correct answer. We created
three types of datasets this way: BibleQA-3, BibleQA-10, and BibleQA-chapter. For
BibleQA-3 and BibleQA-10, we included 3 and 10 verses surrounding the true verse
respectively as candidates. For the chapter version, we included all verses from the
same chapter that usually ranges from 10 to 60 verses. Each RNN, CNN, and BiDAF
model was tuned on BibleQA-3 for the maximal accuracy result, and subsequently, the
same model was used for the prediction for BibleQA-10 and BibleQA-chapter. For all
datasets, we included all four Bible translations: KJV, ASV, YLT and WEB.
Results and analysis.
We used the tuned models from the last experiment for training
each dataset, which compares the effect of changing the length of the context has on the
model accuracy. Table 2 describes the results among the three datasets with different
answer context lengths. Across all three datasets, the CNN model performs the best
using the F1 measure, while BiDAF generally has the best MRR score. This echoes
the interesting phenomenon as mentioned above as to why certain models would have a
higher F1 score but lower MRR than others. Once again, more investigation is needed.
For the shortest context with three verses, all the models signiﬁcantly improve on
the baseline by 0.13 to 0.19 F1, with the best results from the RNN model on both F1
and MRR. As the context length increases to 10 verses, the model accuracy signiﬁ-
cantly decreases, improving only 0.03 to 0.05 of the F1 score from the baseline model.
The RNN drops its performance compared to others, and CNN rises as the model with
the highest F1, but BiDAF becomes the model with the highest MRR. Finally, in the
longest context length of using the entire chapter, the models perform at around the
same level as the baseline model, if not worse.
This shows that the models are not yet able to be used for longer contexts. A larger
dataset and longer training time could be used to train a more robust model that can
deal with longer context lengths in the future.
5.4
Experiment 3: Translation Version
Goal and method. The third experiment focuses on the differences among various En-
glish translations of the Bible. As mentioned above, we used 4 English translations in
training the word vectors creating the dataset. Each of these translations varies in their
translation philosophy, as well as the modernity of their language. YLT is the most
literal English translation of the original languages. The other three translations are
roughly the same in their translation philosophy in that they are not as literal as YLT,
but also strive to truthfully capture the original meaning. Ordering them by modernity,
KJV was the oldest translation being published 400 years ago, while WEB is the most
recent at 2000. The literality of the translations could affect the sentence representa-
tions, as they could choose to use certain words for translation that are a more direct
13

--- Page 14 ---

Dataset
Mode
F1
MRR
BibleQA-3
Baseline
0.35
0.58
RNN
0.54
0.61
CNN
0.48
0.53
BiDAF
0.48
0.53
BibleQA-10
Baseline
0.11
0.30
RNN
0.14
0.30
CNN
0.16
0.28
BiDAF
0.14
0.32
Chapter
Baseline
0.05
0.15
RNN
0.02
0.14
CNN
0.05
0.15
BiDAF
0.04
0.14
Table 2: Comparison between BibleQA-3, BibleQA-10 and BibleQA-Chapter for different mod-
els
translation of the intended meaning. The modernity of the language could also affect
the word vector, since older translations are likely to contain obsolete words that are
no longer used, and therefore the word vectors may not necessarily capture an accurate
representation. We want to compare whether the model prediction changes based on
the level of literal translation, or by the language modernity. For this experiment, we
create four further datasets, each only using one particular translation. We use the for-
mat of BibleQA-10, and select 10 candidate verses for each question. We use the same
three models, and compare the result for each translation individually.
Results and analysis. Table 3 compares the results for each translation within each
model. Looking at both F1 and MRR scores, WEB achieves the best performance,
having the top MRR result for RNN and the top F1 score for CNN/BiDAF. This sug-
gests that using a translation with more modern language can be beneﬁcial for the QA
process, and it could be the case that the word vectors used were able to capture more
accurate meanings.
The KJV translation follows the WEB translation and has the highest performance
for the RNN model using the F1 measure, as well as for the CNN model under MRR.
The high performance was surprising, as we expected that for a translation such as
KJV, some of the archaic language used in the translation could have been a deterrent
for learning useful word vectors. It turns out that despite the choice of English words,
the KJV still may perform relatively well in NLP tasks.
The YLT has the highest MRR result for the BiDAF model. However, the vari-
ance is not large enough for the result to be signiﬁcant, and YLT does not perform
particularly well in any other models. From this, we conclude that the translation phi-
losophy and the level of literalness do not necessarily play a dominant role in training
QA system.
14

--- Page 15 ---

Dataset
Mode
F1
MRR
RNN
KJV
0.17
0.30
ASV
0.14
0.29
YLT
0.09
0.31
WEB
0.12
0.32
Combined
0.14
0.32
CNN
KJV
0.13
0.35
ASV
0.14
0.28
YLT
0.14
0.29
WEB
0.16
0.26
Combined
0.16
0.28
BiDAF
KJV
0.11
0.28
ASV
0.10
0.29
YLT
0.11
0.30
WEB
0.16
0.28
Combined
0.14
0.32
Table 3: Translation comparison for each model. The bolded ﬁgures represent the highest score
for each model
6
Conclusions and Future Work
In this paper, we leverage transfer learning techniques to study domain adaptation in
QA tasks using the BibleQA dataset. Transferring the weights from the much larger
SQuAD dataset has a noticeable improvement in the model accuracy. This showed the
potential of using transferred weights for this particular task. We also ﬁnd that RNN
was the best performing model, while BiDAF did not perform as well as expected
despite being the most complicated model. This suggests that simpler architectures
can still sometimes achieve relatively good results.
When increasing the number of candidate sentences to choose from as answers to
questions, unsurprisingly, the model performances deteriorates. Comparing different
Bible translations that vary in degrees of literalness in translation as well as the moder-
nity of language, we ﬁnd that the World English Bible gives the best results, followed
by the King James Version. The modernity of the language may be attributed to the
good performance of WEB. At the same time, although KJV was written centuries
ago and uses different words than we do now, it is still able to produce useful results.
Furthermore, Young’s Literal Translation being the most literal translation does not
perform particularly well. We conclude that the translation philosophy, and how literal
a translation is, does not necessarily improve the results.
Our system has certain limitations, and here we will suggest some potential im-
provements and direction for future research. The implementation of the BiDAF model
was entirely dependent on the DeepQA library, which has very recently been depre-
cated. The researchers behind DeepQA has ported the library to PyTorch4 which they
have found to be better for NLP research. In the future, it could be worthwhile to
4 http://pytorch.org/
15

--- Page 16 ---

consider implementation using PyTorch instead of Keras, and to use reliable and sta-
ble software frameworks. The sentence encoding methods used in our models are still
relatively simple, in particular, the RNN and the CNN models. The main issue with
our current method of encoding is that it mostly only takes into consideration the se-
mantics of the sentences, and not as much the syntax. While it is a simple method that
has shown to have worked relatively well, to achieve better accuracy we could consider
incorporating an encoding scheme which considers both the syntax and the semantics,
such as the treeLSTM [24] or an ensemble of different encoding schemes. The do-
main adaptation methods used in our systems was also a simple approach which only
involves pre-training the weights and transferring the weights. More exploration into
improving the transfer learning method could be beneﬁcial. For example, transferring
only the weights of certain layers or tuning them at different learning rates. As transfer
learning becomes more widely used in NLP research, we expect that more effective
methods would emerge that can improve the system. The accuracy of the model is
highly dependent on the quality of the dataset. The BibleQA dataset we created was
had only 886 distinct question. Extending the size of the dataset is also a worthwhile
task in the future, that can be done by manually adding more questions, combining
with other sources of Bible questions, or potentially leveraging techniques that could
automatically generate questions based on a text.
References
[1] ˇZeljko Agi´c, Dirk Hovy, and Anders Søgaard. If all you have is a bit of the
bible: Learning pos taggers for truly low-resource languages. In The 53rd Annual
Meeting of the Association for Computational Linguistics and the 7th Interna-
tional Joint Conference of the Asian Federation of Natural Language Processing
(ACL-IJCNLP 2015), 2015.
[2] Amittai Axelrod, Xiaodong He, and Jianfeng Gao. Domain adaptation via pseudo
in-domain data selection. In Proceedings of the conference on empirical methods
in natural language processing, pages 355–362. Association for Computational
Linguistics, 2011.
[3] John Blitzer, Mark Dredze, Fernando Pereira, et al.
Biographies, bollywood,
boom-boxes and blenders: Domain adaptation for sentiment classiﬁcation. In
ACL, volume 7, pages 440–447, 2007.
[4] John Blitzer, Ryan McDonald, and Fernando Pereira. Domain adaptation with
structural correspondence learning. In Proceedings of the 2006 conference on
empirical methods in natural language processing, pages 120–128. Association
for Computational Linguistics, 2006.
[5] Marco B¨uchler, Philip R Burns, Martin M¨uller, Emily Franzini, and Greta
Franzini. Towards a historical text re-use detection. In Text Mining, pages 221–
238. Springer, 2014.
16

--- Page 17 ---

[6] David Daniell. The Bible in English: Its history and inﬂuence. Berghahn Books,
2003.
[7] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei. Ima-
genet: A large-scale hierarchical image database. In Computer Vision and Pat-
tern Recognition, 2009. CVPR 2009. IEEE Conference on, pages 248–255. IEEE,
2009.
[8] John Duchi, Elad Hazan, and Yoram Singer. Adaptive subgradient methods for
online learning and stochastic optimization. Journal of Machine Learning Re-
search, 12(Jul):2121–2159, 2011.
[9] Shira Faigenbaum-Golovin, Arie Shaus, Barak Sober, David Levin, Nadav
Na’aman, Benjamin Sass, Eli Turkel, Eli Piasetzky, and Israel Finkelstein. Al-
gorithmic handwriting analysis of judah’s military correspondence sheds light on
composition of biblical texts. Proceedings of the National Academy of Sciences,
113(17):4664–4669, 2016.
[10] David Ferrucci, Eric Brown, Jennifer Chu-Carroll, James Fan, David Gondek,
Aditya A Kalyanpur, Adam Lally, J William Murdock, Eric Nyberg, John Prager,
et al.
Building watson: An overview of the deepqa project.
AI magazine,
31(3):59–79, 2010.
[11] Xavier Glorot, Antoine Bordes, and Yoshua Bengio. Domain adaptation for large-
scale sentiment classiﬁcation: A deep learning approach. In Proceedings of the
28th international conference on machine learning (ICML-11), pages 513–520,
2011.
[12] Sepp Hochreiter and J¨urgen Schmidhuber. Long short-term memory. Neural
computation, 9(8):1735–1780, 1997.
[13] Wei Hu. Unsupervised learning of two bible books: Proverbs and psalms. Soci-
ology Mind, 2(03):325, 2012.
[14] Mohit Iyyer, Jordan L Boyd-Graber, Leonardo Max Batista Claudino, Richard
Socher, and Hal Daum´e III. A neural network for factoid question answering
over paragraphs. In EMNLP, pages 633–644, 2014.
[15] Ankit Kumar, Ozan Irsoy, Peter Ondruska, Mohit Iyyer, James Bradbury, Ishaan
Gulrajani, Victor Zhong, Romain Paulus, and Richard Socher. Ask me anything:
Dynamic memory networks for natural language processing. In International
Conference on Machine Learning, pages 1378–1387, 2016.
[16] Mateusz Malinowski, Marcus Rohrbach, and Mario Fritz. Ask your neurons: A
neural-based approach to answering questions about images. In Proceedings of
the IEEE international conference on computer vision, pages 1–9, 2015.
[17] Tomas Mikolov, Kai Chen, Greg Corrado, and Jeffrey Dean. Efﬁcient estimation
of word representations in vector space. arXiv preprint arXiv:1301.3781, 2013.
17

--- Page 18 ---

[18] Sewon Min, Minjoon Seo, and Hannaneh Hajishirzi.
Question answering
through transfer learning from large ﬁne-grained supervision data. arXiv preprint
arXiv:1702.02171, 2017.
[19] Maxime Oquab, Leon Bottou, Ivan Laptev, and Josef Sivic. Learning and trans-
ferring mid-level image representations using convolutional neural networks. In
Proceedings of the IEEE conference on computer vision and pattern recognition,
pages 1717–1724, 2014.
[20] Jeffrey Pennington, Richard Socher, and Christopher Manning. Glove: Global
vectors for word representation. In Proceedings of the 2014 conference on empir-
ical methods in natural language processing (EMNLP), pages 1532–1543, 2014.
[21] Stephen R Prothero. Religious literacy: What every American needs to know–and
doesn’t. HarperSanFrancisco San Francisco, CA, 2007.
[22] Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and Percy Liang. Squad:
100,000+ questions for machine comprehension of text.
arXiv preprint
arXiv:1606.05250, 2016.
[23] Minjoon Seo, Aniruddha Kembhavi, Ali Farhadi, and Hannaneh Hajishirzi.
Bidirectional attention ﬂow for machine comprehension.
arXiv preprint
arXiv:1611.01603, 2016.
[24] Kai Sheng Tai, Richard Socher, and Christopher D Manning. Improved semantic
representations from tree-structured long short-term memory networks. arXiv
preprint arXiv:1503.00075, 2015.
[25] Michael Tschuggnall and G¨unther Specht. From plagiarism detection to bible
analysis: The potential of machine learning for grammar-based text analysis. In
Joint European Conference on Machine Learning and Knowledge Discovery in
Databases, pages 245–248. Springer, 2016.
[26] Ellen M Voorhees et al. The trec-8 question answering track report. In Trec,
volume 99, pages 77–82, 1999.
[27] Di Wang and Eric Nyberg. A long short-term memory model for answer sentence
selection in question answering. In Proceedings of the 53rd Annual Meeting of the
Association for Computational Linguistics and the 7th International Joint Con-
ference on Natural Language Processing (Volume 2: Short Papers), volume 2,
pages 707–712, 2015.
[28] Mengqiu Wang and Christopher D Manning. Probabilistic tree-edit models with
structured latent variables for textual entailment and question answering.
In
Proceedings of the 23rd International Conference on Computational Linguistics,
pages 1164–1172. Association for Computational Linguistics, 2010.
[29] Mengqiu Wang, Noah A Smith, and Teruko Mitamura. What is the jeopardy
model? a quasi-synchronous grammar for qa. In EMNLP-CoNLL, volume 7,
pages 22–32, 2007.
18

--- Page 19 ---

[30] Georg Wiese, Dirk Weissenborn, and Mariana Neves. Neural domain adaptation
for biomedical question answering. arXiv preprint arXiv:1706.03610, 2017.
[31] Zhilin Yang, Junjie Hu, Ruslan Salakhutdinov, and William W Cohen.
Semi-supervised qa with generative domain-adaptive nets.
arXiv preprint
arXiv:1702.02206, 2017.
[32] Xuchen Yao, Benjamin Van Durme, Chris Callison-Burch, and Peter Clark. An-
swer extraction as sequence tagging with tree edit distance. In HLT-NAACL, pages
858–867, 2013.
[33] Lei Yu, Karl Moritz Hermann, Phil Blunsom, and Stephen Pulman. Deep learning
for answer sentence selection. arXiv preprint arXiv:1412.1632, 2014.
[34] Matthew D Zeiler and Rob Fergus. Visualizing and understanding convolutional
networks. In European conference on computer vision, pages 818–833. Springer,
2014.
19
