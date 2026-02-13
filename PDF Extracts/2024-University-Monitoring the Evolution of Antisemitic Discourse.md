---
title: "2024-University-Monitoring the Evolution of Antisemitic Discourse - PDF Extract"
source_pdf: "2024-University-Monitoring the Evolution of Antisemitic Discourse.pdf"
pages: 11
extracted_at: "2026-02-13T09:15:44.772080"
---

# PDF Extract: 2024-University-Monitoring the Evolution of Antisemitic Discourse

**Source PDF:** 2024-University-Monitoring the Evolution of Antisemitic Discourse.pdf
**Total Pages:** 11

---

## Content

```
--- Page 1 ---

Monitoring the evolution of antisemitic discourse on
extremist social media using BERT
Raza Ul Mustafa, Nathalie Japkowicz
American University, 4400 Massachusetts Ave NW, Washington, DC 20016, USA
{rmustafa,japkowic}@american.edu
Abstract—Racism and intolerance on social media contribute
to a toxic online environment which may spill offline to foster
hatred, and eventually lead to physical violence. That is the
case with online antisemitism, the specific category of hatred
considered in this study. Tracking antisemitic themes and their
associated terminology over time in online discussions could help
monitor the sentiments of their participants and their evolution,
and possibly offer avenues for intervention that may prevent
the escalation of hatred. Due to the large volume and constant
evolution of online traffic, monitoring conversations manually
is impractical. Instead, we propose an automated method that
extracts antisemitic themes and terminology from extremist social
media over time and captures their evolution. Since supervised
learning would be too limited for such a task, we created an
unsupervised online machine learning approach that uses large
language models to assess the contextual similarity of posts. The
method clusters similar posts together, dividing, and creating
additional clusters over time when sub-themes emerge from
existing ones or new themes appear. The antisemitic terminology
used within each theme is extracted from the posts in each
cluster. Our experiments show that our methodology outperforms
existing baselines and demonstrates the kind of themes and sub-
themes it discovers within antisemitic discourse along with their
associated terminology. We believe that our approach will be
useful for monitoring the evolution of all kinds of hatred beyond
antisemitism on social platforms.
Index Terms—hate speech, concept formation, monitoring,
antisemitic speech, large language model, NLP, social media,
BERT, transfer learning
I. INTRODUCTION
Social1 media has played a crucial role in simplifying
the human process of joining communities of like-minded
individuals. People use these platforms to engage with others
by way of expressing their opinions and commenting on
those of others. While technology has had a positive impact
on many people’s lives, it has also brought serious negative
consequences onto society, including an acceleration of the
spread of hatred.
In the past few years, a large number of studies have
been devoted to automatic hate speech detection [1]–[4]. The
more difficult task of understanding the nature of online
discussions automatically has been considered, though only
rarely. On those few occasions, the task was considered in a
static fashion, ignoring the fact that online discussions evolve
Acknowledgements: Research supported by American University’s Signa-
ture Research Initiative program. We also thank Matan Schwartz for his initial
help with this project.
1Warning: This paper contains examples of racist and antisemitic statements
that may be disturbing to the reader.
quickly. Though these attempts constitute a good start, they
are not sufficient since organizations that seek to promote
social peace need to be informed of changes in discussion
themes as they occur rather than on, say, a monthly basis,
when the software is run on a new batch of posts. The purpose
of our work is to explore the ability of machine learning
(ML) and natural language processing (NLP) tools to extract a
continuously evolving map of the semantic themes represented
in social media posts, automatically. To provide continuity
and avoid catastrophic forgetting, it is of utmost importance
that past knowledge be preserved and only updated when
necessary.
We develop a method to continuously monitor antisemitic
themes from discussions taking place on extremist social
media. Many antisemitic themes have emerged throughout the
years, making antisemitism an unfortunately good testbed for
our approach. Indeed, Jews have been victims of discrimi-
nation for centuries, sometimes accused of having too much
power, controlling the world economy, or being disloyal. Dis-
cussions and conspiracy theories about the Holocaust abound.
Other historical tropes include: “Jews killed Jesus” and “Jews
are greedy”. These conspiracy theories evolve continuously
developing new themes, such as linking Jews to the COVID-
19 pandemic [5]. The purpose of our endeavor is to stay ahead
of the ”mood” in extremist social media communities where
antisemitic posts are frequent, so as to be aware of emerging
new themes or recurring old ones in the same or altered form.
To be practical, given the exploratory and continuous nature of
the task, the method we devised is unsupervised and works in
a continual and, thus, stable fashion using state-of-the-art ML
and NLP techniques such as Large Language Models (LLMs).
Though antisemitism was used in this work as a case study, the
methods we propose will apply to any other kinds of hatred,
such as Islamophobia, anti-Black or anti-Asian racism, anti-
LGBTQ+ discourse, etc.
Our proposed approach begins by considering posts col-
lected in a first time-window and groups together semantically
related themes (i.e., concepts, topics). It then proceeds with
the next time-window, adding new posts to the previously
discovered themes and discovering new themes in the data
if the discourse they represent stands semantically apart from
the themes already present in memory and sub-themes, if they
share enough commonality with existing ones. The system
then considers the posts collected in the next time-window
and repeats the same steps over and over.
arXiv:2403.05548v1  [cs.CY]  6 Feb 2024

--- Page 2 ---

The remainder of the paper is organized as follows. In
Section II, we discuss the philosophical basis for our work
along with related studies from the fields of Computer Science,
Psychology and Business. We then review ML and NLP
techniques previously used for combating online hate speech
and antisemitism in Section III. Section IV describes our
methodology. We present and discuss our results in Section
V and conclude our paper in Section VI.
II. GENERAL BACKGROUND
In this section, we consider related work from four different
disciplines: Philosophy, Computer Science, Psychology, Busi-
ness.
Philosophical Concept Theory:
Our work is based on
Philosophical Concept Theory [6] used extensively in the fields
of Psychology and Cognitive Science. In a nutshell, we take
the view that concepts are representations of the mind and that
complex concepts are composed of sub-concepts. Furthermore,
we subscribe to the Prototype Theory rooted in Wittgenstein
[7] and Rosch [8]’s thought where a concept is defined by
its most central, or prototypical, instance and the association
of a separate instance to that concept depends on its distance
to the prototype. We illustrate these ideas with the following
example. A common concept is that flowers are beautiful and
fragrant. However, the reality is more complex: while most
flowers fit the common concept, some flowers are odorless,
and some are even pungent and cause allergies. Therefore,
beauty and fragrance, while brought together in the common
concept of a flower, can also be taken apart. That is the
case for the concept of flowers that are beautiful but pungent
(or odorless). Such flowers remain semantically close to the
prototypical instance (a rose, for example) of beautiful and
fragrant flowers because of their many shared features, but they
must be represented by a different sub-concept since, while
still beautiful, they are not fragrant. Similarly, flowers that
cause allergies must be represented by yet a new sub-concept
that intersects with the concepts of beautiful and fragrant
flowers and beautiful but pungent (or odorless) ones. Our
work equates clusters of posts to concepts and subconcepts
and assesses the relations between them by means of their
distance in LLM embedded space.
Lifelong Unsupervised Learning: The method designed
in this paper is inspired by a recent approach for lifelong
anomaly detection presented in [9], [10]. The main purpose
of that approach was to build an evolving representation and
organization of memory to ensure that new concepts could
be coherently added to the organized structure while older
pieces of knowledge could be retrieved efficiently in a lifelong
learning regimen. The stability of the method ensured that
catastrophic forgetting was avoided. Anomaly detection was
performed on a continual basis by checking whether the new
data fell into one of the categories present in memory. If
not, a decision was made as to whether the new data was
anomalous or not. If it was deemed anomalous, an alert was
issued and the data not saved. Otherwise, the new data was
introduced into the memory structure as either a sub-concept
or a new concept altogether. Decisions were made based
on distance in an autoencoder-based embedding space. The
approach was tested and validated on tabular data representing
fairly straightforward hierarchically organized categories of
data. One of the challenges of the present study is to see
to what extent the principles used in the earlier work can
apply to text data and imprecise concepts that are not always
hierarchically organized.
Psychological Studies on Hate Speech: To underline the
importance of the task we address with our method, we review
two related psychological studies on hate speech that seek to
extract similar types of information as ours from their analysis,
albeit manually. In the first study, closest to our proposed one,
[11] extracted four semantic themes from a series of comments
responding to a Youtube video that displayed a white British
woman abusing black passengers on the Tube (subway). The
four themes they organized the posts around are: 1) posts
that explain the abuser’s behavior; 2) posts that counter the
abuser’s behavior with aggressive and hateful language; 3)
posts that categorize other posters into racist or non racist
people; 4) posts that discuss what it means to be British. The
authors’ analysis led them to conclude that online hate speech
does not necessarily generate more hate speech, a potentially
useful conclusion for this specific content and platform. In
a second study, [12] analyzed the behavioral roles taken by
online users responding to hate speech posts in Ethiopia.
They identified five major roles—trolling, pace-making, peace-
making, informing, and guarding—and used their conclusions
to make recommendations on how to counter online hatred.
Though like in our work, both studies support the need for
a deeper semantic analysis of posts rather than their mere
classification as hateful or not, it is important to note that
both were conducted through human analysis of a relatively
small and static number of posts. Our work, in contrast,
seeks to perform the same type of analysis automatically and
dynamically.
Information Extraction from Customer Surveys: Although
the aim of our study is new in the context of automated
hate speech analysis, the business community has understood
the value of extracting information from product reviews for
some time. As a matter of fact, it has already seized upon the
power of AI to learn how to extract automatically the areas
of satisfaction and concern about its products expressed by
customers. This is shown in both academic research papers
[13], [14] and commercial products available to businesses.
It is important to note, however, that the domain explored
by such business tools is much simpler than the hate speech
domain. Indeed, human beings typically have many conflicting
and hard-to-express resentments about other human beings,
and these feelings may fluctuate as a result of national or
international news items or personal experiences. On the other
hand, feelings about purchased goods are rather straightfor-
ward and limited since they are non-conflictual and pertain
to simple and finite properties such as the product’s price,
functionality, or looks. In addition, the approaches considered
in these works take a static rather than a dynamic view of

--- Page 3 ---

the problem. For these reasons, the techniques used by the
business community, though relevant, are not sufficient, and
new methods must be developed to handle the monitoring of
complex themes that also evolve over time.
III. BACKGROUND ON COMPUTER-BASED HATE SPEECH
ANALYSIS
As previously mentioned, hate-speech detection has become
an important area of study in NLP as reported by a number of
surveys on the topic [1]–[4]. Recently, many of these studies
have employed deep learning techniques [15]. In [16], the
authors proposed a Recurrent Neural Networks (RNNs) based
framework for the classification of racism & sexism, offensive
speech, and cyberbullying using text and metadata. In [17], the
LSTM (Long Short-Term Memory) architecture is used for the
classification of abusive content on social media while [18]
uses more advanced recurrent neural network techniques to
classify sexism and misogyny. In another study, [19] compared
multiple deep learning techniques to classify tweets into three
categories: racism, sexism, or neither.
There have been a few studies devoted to the particular
issue of online antisemitism. [20] used a transformer archi-
tecture (RoBERTA) to classify antisemitic content into four
categories: political, economic, religious, or racial. In [5] the
authors used Latent Dirichlet Allocation (LDA) to find topics
particularly related to the coronavirus and antisemitism in the
Hungarian language. [21] describes a large study with several
outcomes. In that work, the authors collected 7 million images
and comments from 4chan and Gab to study the spread
of antisemitic memes. They provide a framework to better
understand antisemitic memes and content and their relation to
political events. In one part of the study, they used Word2Vec
to discover words closely associated with the term ”Jew” and
used network analysis tools such as community discovery in
an attempt to uncover the themes represented by these terms.
The themes they uncovered are: Jewish moral corruptness,
Jews as geopolitical conspirators, ethnic Jewish identities,
Kabbalistic and cryptic themes, and religious or theological
topics. Following this study, [22] considers both antisemitism
and Islamophobia. In that work, the authors constructed two
lexicons: a lexicon of 48 Antisemitic terms and another of 135
Islamophobic terms. The lexicons were built using pre-existing
knowledge graphs, pre-trained word embedding models, and
manual annotations. Using their lexicons, they extracted posts
from 4Chan and analyzed them using sentence embeddings
by BERT and clustering using HDBSCAN. They subsequently
analyzed the groupings qualitatively.
We summarize the previous work in Table I. Our proposed
approach is summarized at the bottom of the table. As can
be seen, our work is most similar to [5], [21] and [22].
The main difference between these three works and ours is
that they consider a static situation whereas our approach
is an online machine learning approach that provides self-
adaptation mechanisms in a dynamic setting, making sure
that the knowledge base induced in previous steps is not
compromised by a new influx of information. Self-adaptation,
The kike alliance bringing
cultural marxism to your front
door.
[CLS]
The
kike
door
[SEP]
LLM
E
[CLS]
E
[The]
E
[kike]
E
[door]
E
[SEP]
LLM based text embedding
Extract concepts from contextual embeddings
Concepts
Concept
Sub-concept
Sub-concept
d
d= Distance metrics
Contextual embeddings 
Concept
Fig. 1. Overview of the methodology.
dynamism, and stability aside, of the three methods closest to
ours, [22] is the one that uses the closest methodology since
[5] performs topic extraction using LDA, and [21] does so
using Word2Vec. These two methodologies are less recent and
typically obtain lower performance than the one used by both
[22] and our work: transformers. In particular, both works use
BERT, though while [22] rely on pre-trained language models,
we fine-tuned our model to the particular type of data we
analyze. Like in our study, [22] uses clustering on the lan-
guage representations learned and, in particular, HDBSCAN.
Rather than using an off-the-shelf static clustering approach,
however, we design our own approach that works in a dynamic
environment without causing catastrophic forgetting.
IV. METHODOLOGY
Our antisemitic discourse monitoring approach takes as
input continuously arriving batches of posts and organizes
them into a knowledge base containing the antisemitic themes
they convey in an unsupervised way. In more detail, we
designed a repeating two step-method that takes the following
actions for each batch of incoming posts: 1) it generates con-
textual embeddings from the posts using a fine-tuned BERT
model; 2) it inputs these embeddings into our newly proposed
divisive clustering approach which adaptively updates the last
clustering to integrate the new batch of embeddings into
the existing knowledge base using local or global updates.
Decisions are made based on the distance in embedding space
between the new posts and the existing cluster centers. The
two main mechanisms used in the process are illustrated in
Figure 1. Each step of the process will be described in more
detail below.
A. Dataset and Pre-Processing
1) Data Collection and Labeling: This work is part of
a larger project entitled unmasking antisemitism that
our organization has undertaken to control anti-Jewish hatred.
Under this project, a data team collected and labeled the
data set using third-party software Pyrra2. A baseline was set
for data selection under which currently known antisemitic
seed words from the American Jewish Committee (AJC) and
other sources were used (e.g., cabal, new world order). During
labeling, the data team carefully examined word selection in
posts as well as other pieces of information such as i) does
2https://www.pyrratech.com/

--- Page 4 ---

TABLE I
COMPARISON TO TRADITIONAL WORK AND TECHNIQUES USED IN HATE SPEECH DETECTION.
Ref
Unsupervised
Online
Term Extraction
Topic Extraction
ML Tools
Hate Type
[16]
×
×
×
×
RNNs
racism & sexism, offensive speech, and cy-
berbullying
[17]
×
×
×
×
LSTMs
abusive content
[18]
×
×
×
×
LSTMs, CNNs
sexism and misogyny
[19]
×
×
×
×
LSTMs, CNNs, GloVe
racism, sexism, or neither
[20]
×
×
×
×
RoBERTa
antisemitism
[5]
✓
×
×
✓
LDA
coronavirus related antisemitism
[21]
✓
×
✓
✓
Word2Vec, network analysis
antisemitism
[22]
✓
×
✓
✓
BERT, HDBSCAN
antisemitism and islamophobia
This work
✓
✓
✓
✓
BERT, novel algorithm
antisemitism
LLM
Sum last four hidden layer
Concat last four hidden layer
Last hidden layer
Pooled layer
9
10
11
12
9
10
11
12
12
12
+
+
+
+
The kike alliance bringing cultural marxism to your front door.
Contextual embedding 
Fig. 2. BERT layers to extract contextual embedding.
the post demonstrate an applied understanding of particular
antisemitic tropes? ii) does the post express themes of control
over media, politics, academia, economy, or culture at large?
and so on. It then classified the data into different pre-defined
historic tropes or generated variations on them when the post
was found to be antisemitic. The labels generated by the data
team are used in this work to evaluate our approach and the
baselines we will be comparing it to.3
2) Data Pre-Processing: The initial step of our approach,
not shown in Figure 1, involves preparing the dataset using
different techniques. We first normalize the text documents by
converting uppercase to lowercase and replacing references.
Next, we remove links from the text. However, we replace
the links with the titles of the posts they lead to. Finally, we
remove all special characters, white spaces, and line breaks
using regular expressions. The cleaned-up texts are then fed
into BERT for tokenization into small units (words or word
parts) and contextual embeddings are generated to facilitate
the discovery of underlying concepts in the text. The details
of the contextual embedding method used here are described
in the next section.
B. Contextual Embedding
To convert our extremist cleaned-up dataset into embed-
dings, we use embedding techniques derived from large lan-
guage models to extract a structural representation that cap-
tures semantic relationships and contextual meanings. This ap-
3The coding statement used by the data team is available upon request.
proach facilitates the categorization of information to uncover
hidden patterns [20]. Since BERT doesn’t possess vocabulary
specific to our domain, we first added Out of Vocabulary
(OOV) tokens and fine-tuned the BERT uncased model as in
[23]. During concept extraction, we consider different types of
combinations to extract contextual embedding from the BERT
(see Figure 2). To this end, we first explored the summation
of the last four layers, followed by the concatenation of
the last four layers. We also considered the pooled layer,
which provides 768-dimensional sentence-level embeddings.
In our case, the last hidden layer, after taking the mean
of tokens level embedding, produces the best results and
was therefore the embedding technique we retained. These
variations allowed us to evaluate the impact of different feature
representations, contributing to a deeper understanding of the
model’s capabilities and suitability for our specific NLP task.
C. Antisemitic Themes discovery
We now describe the approach we designed to extract con-
cepts from extremist posts. To simulate a streaming situation,
we divide the dataset into batches of vectors ⃗v (each containing
instances of posts embeddings) and feed each batch into algo-
rithm 1. Algorithm 1 uses distances in the embedding space
along with several thresholds to capture the antisemitic themes
expressed in our extremist dataset. Several parameters need to
be set prior to running the algorithm: k, lo, hi, and thresholds λ
and δ. k represents the number of initial concepts considered
in the first batch of data ⃗v1. In our work, we set k = 2,
assuming that the posts in ⃗v1 align along two main themes. lo
and hi represent the lower and higher percentile marks used
in our computations to consider whether a post is within the
vicinity of a concept or not. We set them to lo = 40 and
hi = 60, here. λ is the multiplier used (combined with lo and
hi) to calculate the percentile distribution ranges that will help
determine whether instances from a given batch are outliers
with respect to the concept considered. Finally, δ, determines
the minimum number of outlying instances required to justify
the need for an additional concept in memory (i.e., an increase
in k). In our work, we choose a λ value of 0.25, and δ is set
to 15% of the batch size.
A crucial aspect of the algorithm is its stability. Indeed,
given its continual learning nature, it is imperative that when
new information comes in, previous knowledge is preserved to

--- Page 5 ---

the greatest extent possible. To implement this requirement, we
only allow for two kinds of updates: a local update and a global
one, each with the following allowances and limitations. The
local adjustment phase may be drastic, but it can involve only
one concept. The global adjustment phase is much lighter but
it may affect all the concepts in memory. The two adjustments
are shown in Figure 3 where the top figure illustrates a local
adjustment while the bottom one illustrates a global one. The
leftmost pictures show the “before” situation with black dots
on the top figure and green ones on the bottom representing
data that has arrived in a new batch, but has not yet been
processed. The rightmost pictures show the “after” situation,
i.e., the result of the processing in each case. What is important
to note in the top figure is that while the original C0 concept
gets split into two new concepts C0 and C2, concept C1 is
not affected by this change. That is an instance of a local
adjustment. In the bottom figure, an example of a global
adjustment, no new concept is created, but both C1 and C2
are slightly modified (their center and/or spread change from
the picture on the left to that on the right) to accommodate
the new data. C0 could have accommodated new data as well,
but in our particular illustration, no new data affected it.
We now describe Algorithm 1 line by line. It begins on
line 1 where the batch number b is set to 1. On line 2, a
model is built by clustering the data in ⃗v1 using the k-means
algorithm (we chose an initial value of k = 2). Next, on lines
3-4, we store the initial centroid values in cc and initialize
the semantic similarity structure, ss, that associates the two
concepts most closely related to one another. Specifically, ss
is a list of [r, l]’s, where r refers to the root concept that
already existed in memory, and l, the concept derived from r
during local updating. l has some degree of similarity with r
though the majority of the data in l represents a new concept.
On line 4, we have r1 = r2 = 0 since these are the initial
concepts with no root from which tehy derived. During our
continual learning process, new concepts are created or old
ones modified based on percentile distributions and numbers
of outlying instances, as illustrated in Figure 3. On line 5, we
increment the batch number and on line 6, we assign the next
batch of posts to
⃗
curr. Line 7 is the while loop that drives
the continual consideration of new batches of posts. Inside the
loop, line 8 calculates the size of the batch and assigns it to
s. Line 9 is another loop that considers each of the concepts
currently present in memory, in turn. The purpose of that loop
is to implement the local updates of the type shown on the top
of Figure 3. In more detail, lines 10-22 are repeated for each
concept in memory with respect to the current batch,
⃗
curr. The
purpose of the loop is to estimate whether the data in the batch
fits the current concept well or whether it would be beneficial
to split it. This question is repeated for each of the current
concepts in memory and in every case, if the answer is yes, k
gets incremented. The decision of whether to increment k or
not for a given concept is done by first, determining the lower
and upper percentiles of the distance distribution to find out
whether a particular post belongs to concept c and falls within
the outlier category, and second, seeing whether the number
of instances from the batch to be considered outliers by these
percentiles exceeds a specific threshold. In more detail, on
line 10, a vector is calculated that stores the distance of each
instance in the batch to the concept’s centroid. Lines 11-12
calculate the lower and upper distance values representing the
loth (40) and hith (60)’s percentiles. These correspond to the
limits within which a post is considered the purview of concept
c. These values are used on lines 13-14, along with threshold λ
(.25) to determine the lower and upper percentile distribution
ranges used to establish whether an instance in the batch is
an outlier or not. On line 15, ⃗
out is assigned all the instances
from the current batch that are the purview of concept c and
yet deviate too much from its centroid (either from the lower or
from the upper end). On line 16, the number of instances in ⃗
out
is pitted against threshold δ. If that number exceeds δ (15%), k-
means is run with k=2 on all instances of concept c (⃗c) and all
instances contained in ⃗
out on line 17 to split the concept and
its outliers appropriately (see top of Figure 3). On lines 18-20,
the centroids cc are updated, the number of concepts present in
memory, k, is incremented, and the cluster pair is added to the
semantic similarity list, ss. For example, in the top situation
of Figure 3, C2 is created and was derived from C0 (which
itself was shifted), so we add [C0, C2] to ss. Line 21 ends
the “if statement” that causes a local update to occur, while
line 22 terminates the inner loop that considers each concept
in memory one after the other. Lines 23-24 implement the
second type of adjustment, the global adjustment, that takes
place in our algorithm. This consists of simply running k-
means on the union of all batches of data seen so far with the
updated value of k. Since k fits the data perfectly thanks to
our carefully crafted local adjustment approach and since k-
means has theoretical guarantees of stability [24], line 23 will
have the minimum effect of adjusting the centroids as shown
at the bottom of Figure 3, thus adjusting the knowledge in a
stable manner, as required. Lines 25-26 increment the batch
number and assign the next batch to
⃗
curr prior to looping
back to line 7. The algorithm terminates if no new batch is
present. It is important to note that this process is a continual
learning process. However, though our approach has focused
on the stability of the memory-building process, it has left out
a number of features necessary in lifelong learning. To ensure
our system’s long-term viability, we will outfit it, in the future,
with lifelong learning features such as those proposed in [10]
including knowledge distillation and experience replay.
V. RESULTS AND DISCUSSION
We now discuss both the quantitative and qualitative ways
in which we tested our trope discovery approach. We recall
that our approach is dynamic and creates clusterings over
time. Unfortunately, there are no clear baselines for comparing
the performance of our approach over others in that fashion.
Therefore, we consider the final clustering output by our
approach and compare it quantitatively to those of state-
of-the-art static clustering methods, along with qualitative
considerations. The section starts with a quantitative analysis,
followed by a qualitative one. Using specific information from

--- Page 6 ---

Fig. 3. Local and Global Updates.
the qualitative analysis, we then return to the quantitative
analysis focusing on particular regions of the clustering.
A. Quantitative Analysis
We compared the final clustering obtained by our method
to the following five state-of-the-art clustering approaches.
Affinity Propagation: Affinity Propagation groups data points
together relying on a message-passing process between points
that assesses their similarity to the different groupings. The
algorithm doesn’t require pre-defining the number of clus-
ters [25].
Birch: Birch begins by producing a brief summary tree
structure that preserves the maximum amount of information
in the dataset. In the next step, this summary is classified
into different numbers of clusters. Birch can be used with or
without specifying the desired number of clusters, k. We ran
it without specifying, k and obtained over 300 clusters. We
then searched for the k that optimized the results and settled
on k = 9
Spectral Clustering: Spectral Clustering is derived from
spectral graph theory. It involves analyzing the eigenvalues
and eigenvectors of a similarity matrix derived from the data.
The number of desired clusters, k, must be fixed prior to run-
ning the algorithm. We considered different combinations of
parameters, but none of the combinations clearly differentiated
between the antisemitic themes. For comparison purposes, we
settled on k = 9.
Gaussian Mixture: In Gaussian Mixture (GM), each cluster
is represented as a Gaussian distribution, and data points are
assigned to clusters based on their likelihood of belonging
to each component. GM requires a pre-defined number of
clusters, k. Here again, after evaluating different combinations
to look at the distributions of clusters, we use k = 9 to
compare the results to our method.
Mean Shift: Mean Shift is a centroid-based algorithm that
updates the centroid with each new point. Mean Shift works
in high-dimensional spaces and uses the mean as the centroid
[26]. It does not require a predefined number of clusters.
Algorithm 1: Antisemitic concepts extraction
Input: ⃗v =
⃗v1, ⃗v2, ..., ⃗vn

; Parameters: k, δ , λ, lo, hi
1 b ←1 ;
/* initial batch number*/
2 m ←kmeans(⃗vb, k) ;
/* build initial
model*/
3 cc ←m(k) ;
/* cc contains centroids
c1, ..., ck*/
4 ss ←[(r1, l1), ..., (rk, lk)] ;
/* initialize
semantic similarity structure*/
5 b ←b + 1;
/* increment batch number*/
6
⃗
curr ←⃗vb ;
/* Consider next batch*/
7 while
⃗
curr != Empty do
8
s ←len( ⃗
curr) ; /* numb. of instances in
⃗
curr*/
9
foreach concept c = 1 to k in memory, m do
10
ˆdc ←
 ˆdc
1, ˆdc
2, ..., ˆdcs

;
/* pred. dist. to
c*/
11
l ←percentile( ˆdc, lo) ;
/* loth perc. in
ˆdc*/
12
u ←percentile( ˆdc, hi) ;
/* hith perc. in
ˆdc*/
13
lower ←l −λ ∗(u −l) ;
/* lower
percentile*/
14
upper ←u + λ ∗(u −l) ;
/* upper
percentile*/
15
⃗
out ←(l <
⃗
curr < lower) + (u >
⃗
curr >
upper) ;
/* set of outliers*/
16
if len( ⃗
out) > δ then
17
kmeans([⃗c, ⃗
out], 2) ;
/* local
adjustment*/
18
update cc ; /* add new centroid to
cc*/
19
k+ = 1 ;
/* increment numb. of
k*/
20
ss ←(rc, lc) ;
/* root and child
concept*/
21
end
22
end
23
m ←kmeans([⃗v1, ..., ⃗vb], k) ;
/* global
adjustment*/
24
cc ←m(k) ;
/* update all centroids*/
25
b ←b + 1;
/* increment batch number*/
26
⃗
curr ←⃗vb ;
/* Consider next batch*/
27 end
The results of our comparison are shown in Table II. In
this discussion, we focus on columns 1-4 of the table. The
last two columns will be discussed in Section V-C. We use
three well-known metrics devised for unsupervised learning:
the Davies-Bouldin Index (DBI), the Silhouette Coefficient
(SC), and the Calinski-Harabasz Index (CHI). The first
metric, DBI, computes the average similarity between each
cluster and its most similar one. In contrast to the next metrics,

--- Page 7 ---

a clear separation is indicated by a lower score. The second
metric, SC, measures the similarity of each point within a
cluster to its similarity to the nearest cluster. It then averages
all the results. It returns a value between -1 and 1, where
1 represents an ideal clustering. The third metric, CHI, also
determines the quality of clustering by measuring the ratio
of between- to within-cluster dispersion, however, it does so
at a more abstract level than SC. Here again, the higher the
value of CHI, the clearer the separation of the data points;
however, there is no upper bound. Table II also shows the
number of clusters discovered by each clustering method on
its own when possible (underlined), or assigned to it. Figure 4
in the appendix gives a visual illustration of each approach’s
results by displaying their T-SNE projections.
Putting aside the dynamic element of our approach not
present in any of the methods we compared it to, these results
suggest that our approach is the only one able to estimate
a reasonable number of clusters while also performing near
the top. Indeed, none of the methods that discover k on their
own did a reasonable job: Affinity discovered 31 clusters,
Birch, over 300, and MeanShift, only two. In all these cases,
the results are not very practical and disqualify Affinity and
MeanShift. Birch, on the other hand, remains in the game
since it allows the user to provide a predefined number of
clusters. Our approach settled on 9 clusters which we use
going forward. Once provided with the number of clusters
(k = 9), Birch, Gaussian, and our method perform reasonably
well according to two of the metrics considered (SC and CHI)
with Birch leading the pack, whereas Spectral does well on
DBI and poorly on the other two metrics. A look at the T-
SNE plot for Spectral reveals that the algorithm learns one
very large cluster and eight very small ones, therefore, not
capturing the essence of the dataset. This observation along
with Spectral’s very low scores on SC and CHI disqualify
it from further consideration. We, thus, conclude that Birch,
Gaussian, and our method are competitive for this domain with
Birch possibly learning slightly better clusters as seen by its
slightly better results on SC and CHI (Gaussian does poorly on
CHI, a little worse than Birch and our method on SC though a
little better than both methods on DBI). Nonetheless, we recall
that our method has two advantages over Birch (and Gaussian):
1) it is a continual and stable self-adjusting algorithm; 2) it
does not require a pre-defined number of clusters.
B. Qualitative Analysis
We now present a qualitative analysis of the results
obtained by our method and reported in Tables III and IV.
The tables show samples of prototypical terminology and
posts per extracted concept. The results of Table III were
obtained using aspects4 of the term extraction methodology
described in [23] on each of the concepts extracted by our
method. Due to space limitations, Table IV can be found
in the Appendix. We conducted a qualitative analysis of
4 [23] focuses on coded terminology. This work doesn’t so we disabled the
filtering of non-coded terminology. We also return unigrams in addition to bi-
and tri- grams.
these tables as follows. The majority of posts in C1 is about
Jews controlling the world. Indeed, we frequently observe
the term New world order which, according to the AJC
Translate Hate Glossary (AJC) conveys, in its antisemitic
use, the belief that Jews have created a power structure
that they fully control at the economic, media and political
levels. Some frequent unigrams appearing in C1 are evil,
need, state, zionist, globalists, economic
while bigrams and trigrams include new world order,
world economic forum, deep state, banking
cabal, state cabal. As discussed in AJC, the term
“cabal” refers to a powerful group of (Jewish) individuals
whose goal is to establish control while “globalists”, which
also introduces the idea of dual loyalty, can refer to a Jewish
elite bent on destroying the western world order. Based on
the terms extracted for C1 (Table III) and on the typical posts
belonging to this category (Table IV), we concluded that while
the concept presents a mixture of control types, the dominant
one was economic, and we thus label it C1: accusation
of economic control. In C2, our approach grouped posts
referring
to
the
meme
Shut it down; The goyim
know into a single concept, which we labeled C2: The
goyim know. This meme portrays, in a satirical way, Jews
panicking because their “secret plot to control the world” has
been discovered (AJC). Our algorithm’s ss-structure shows
that C2 was derived from C1 along with C3 and C4 described
next. In C3, we observe the terms cultural, marxism,
frankfurt, school as well as frankfurt school,
white reproduction, political correctness,
etc. According to a report by the Southern Poverty Law
Center (SPLC), these expressions refer to an antisemitic
conspiracy theory that suggests that Cultural Marxism rooted
in the Frankfurt School, a group of self-interested Jews, is
responsible for progressive causes such as LGPTQ+, identity
politics, and political correctness which are meant to destroy
American values.5 We labeled that concept C3: accusation
of cultural control. C4 is mostly centered around wars and
historical events. The themes revolve around history including
USSR, Russia, Ukraine, Britain, WWII and the current war
between Russia and Ukraine. Holocaust denial is also present.
We labeled this concept C4: accusation of political control.
Two seemingly unrelated expressions appear in C4 including
Mel Gibson and Moon Landing. Our Web investigation
revealed that Mel Gibson, upon receiving probation for DUI
in 2006, remarked to the policeman arresting him that “the
Jews are responsible for all the wars in the world.”6. This
comment (about wars) is what must have landed him into
C4. Moon landing refers to the conspiracy theory that claims
that the 1969 moon landing never happened (the footage was,
supposedly, fake).7 Moon landing landed in C4 most probably
because of its role in the Cold War. Though the conspiracy
theories revolving around it are not antisemitic in nature, it
5https://www.splcenter.org/fighting-hate/intelligence-report/2003/cultural-
marxism-catching
6https://shorturl.at/dqyDH
7https://en.wikipedia.org/wiki/Moon landing conspiracy theories

--- Page 8 ---

TABLE II
COMPARISON OF OUR APPROACH WITH FIVE BASELINES.
Approach
Davies-Bouldin
Silhouette Coefficient
Calinski-Harabasz
Clusters
C2 Coverage
C7 Coverage
Affinity
0.85
0.34
407.22
31
30.50 & 23.72%
100%
Birch
0.86
0.35
384.60
9 and 300+
67.79% and ¡5%
100% and ¡5%
Spectral
0.64
-0.01
67.76
9
Not Applicable
Not Applicable
Gaussian
0.81
0.30
283.65
9
33.89%
100%
MeanShift
0.76
0.45
394.10
2
Not Applicable
Not Applicable
Our approach
0.86
0.33
340.38
9
75.50%
100%
TABLE III
TRENDING TERMS PRESENT IN THE EXTRACTED CONCEPTS
Concepts
Unigrams
Bigrams/Trigrams
C1: Control (Economic)
world, new, order, evil, need, state, zionist, globalists, economic,
forum
new world order, world economic forum, deep state, banking
cabal, state cabal
C2: Control (Economic
& Political)
goyim, know, shut, jew, oy, well, kike, cope, oey, kek
goyim know, know shut, many kike, low birthrates, cunning
plan, know fire
C3: Control (Cultural)
jewish, cultural, war, marxism, frankfurt, school, political,
group, white, lobby
frankfurt school, political correctness, central bank, white repro-
duction, holy war, correct coalition
C4: Control (Political)
jewish, war, military, nation, money, control, Ukraine, russia,
communist
mel gibson, zionist partners, zionist agent, ethnic foods , interest
group, jewish community, moon landing, deception mentality,
communist coup, color revolution
C5: Religion
zionist, type, Jesus, reptilian, blood, time, know, f**k, people
blood type, zionist reptilians, jews bible, real jew, fearsome
warrior, rabbinical jew
C6:
Control
(Western
World)
government, shabbos, biden, occupational, enslavement, ameri-
can, goy, fake
zog/zionist, shabbos goy, ashkenazi jewish, enslavement agenda,
mind control, terrorist cabinet, kosher sandwich
C7: Dystopia
slaughtering, zionist, partner, rock, agent, stone, time, informa-
tion, domain
online domain, zionist reptilian, zionist partners, black stone,
latin brown, black rocks
C8: ZOG
Jewish, communist, zionist, zog, capitalist, like
ZOG, scott greer, elephant room, capitalist subhuman, machine
Georgia, bloodline conglomeration, diana spencer, gay jewish
C9: Jewish Mafia
Jewish, rothschild, world, f**k, people, need, soros
jacob rothschild, khazarian mafia, klaus schwab, mafia minion,
george soros, trillionaire jacob
is worth noting that many proponents of these theories also
support antisemitic ones and that some cross-overs sometimes
take place.8 In C5, we observe religious themes represented by
terms such as Jesus, Jews bible, Jews commit,
deicide, rabbinical tradition. These terms and
the text they center around them fit in with the historical
antisemitic trope Jews Killed Jesus Christ. They
are mixed with other terms such as reptilian, Zionist
reptilians which refer to the reptilian conspiracy theory
that suggests that reptilian aliens take the form of politicians
in order to control the world.9 This, of course, gets back
to the trope claiming that Jews control the world and is
clearly antisemitic.10 We labeled this concept C5: rejection
of Christianity as we felt that despite the spread of this
concept, that was the most representative theme. Next, in C6,
the theme seems to revolve around the Zionist Occupation
Government conspiracy theory that claims, once again,
that Jews control the government of Western States.11 This
concept, which we labeled C6: accusation of control of the
Western States is shown to be derived from C4 from the
algorithm’s ss-structure. Finally, C7 directly advocates for the
slaughter of “Zionists” using language rife in conspiratorial
8E.g.,
https://www.memri.org/tv/french-author-guyenot-moon-landing-
hoax-proves-america-is-empire-of-lies
9https://en.wikipedia.org/wiki/Reptilian conspiracy theory
10https://shorturl.at/cfvEQ
11https://en.wikipedia.org/wiki/Zionist Occupation Government
conspiracy theory
metaphors about, once again, reptilians, but other dystopian
types
of
themes
such
as
online domains, time,
information. We labeled this concept C7: Dystopian
Antisemitism. C8, which we labeled C8:Zionist Occupation
Government (ZOG) is derived from C6 (itself derived from
C4). Finally, C9, labeled C9: Jewish Mafia lists names of
Jewish millionaires or purported Jewish millionaires (e.g.,
Klaus Schwab) and is directly related to C8.
C. Quantitative Analysis (cont’d)
Having described the concepts derived by our approach,
we can now get back to the last two columns of Table II
that present the coverage by each approach of concepts C2
and C7 representing 15.90% and 5% of the entire data set,
respectively. C2 and C7 were chosen for a detailed analysis
because they are the most compact and unambiguous concepts
in the entire set of posts. We discuss their treatment by each
of the clustering methods discussed in Section V-A. Using our
own approach described in Algorithm 1, coverage of concepts
C2 and C7 are 75.5% and 100%, respectively. We note that for
C7, three other methods obtain 100% coverage: Affinity, Birch,
and Gaussian. Of these, Affinity is the only one that determines
k, the number of clusters, on its own. The other two methods:
Spectral and MeanShift receive the results “Not Applicable”
because, as seen in Figure 4, MeanShift learns only two
concepts and, therefore, does not discriminate enough to learn
small concepts and, in the case of Spectral, even though small
concepts are learned, our analysis revealed that C7 was merged

--- Page 9 ---

with C4, with no clear separation between them. C2 is more
difficult to cover as seen in Table II. Affinity splits C2 into
two clusters covering 30.50% and 23.72%, respectively, of C2
or 54.22% when considered together. When Birch is run with
k = 9, it does pretty well, covering 67.69% of C2. That is
less than the 75.5% obtained by our method, but it is close.
Gaussian, on the other hand, only covers 33.89% of C2. Once
again, Spectral received the ”Not Applicable” mention because
C2 was distributed into more than one concept. Conversely,
C2 was one of many amalgamated concepts in MeanShift.
This analysis confirms that Birch works quite well on this
domain, but that, based on this detailed analysis as well as the
previously mentioned strength of our approach, it is preferable
given our practical goals.
VI. CONCLUSION
This work proposes a completely unsupervised machine
learning method for monitoring the evolution of antisemitic
discourse in a continual manner. As new posts arrive, they
are presented to the system in a mini-batch fashion. Concepts
representing new themes discussed in the posts are formed and
added to the existing knowledge base while existing concepts
are updated in accordance with the new information contained
in the posts. Our quantitative and qualitative analyses reveal
that our approach accurately describes the themes discussed
in the posts, thus providing a useful monitoring tool for social
media content. Our future work will add lifelong learning
features to ensure that our method is robust enough to sustain
long periods of online use. Our future work will also involve
working in tandem with social scientists to assess how useful
our tool is in answering their research questions. This will
allow us to refine our method to make it more focused on its
users’ needs. In addition, we will add information visualization
features to make the approach more user-friendly. Finally, we
will apply our work to other kinds of hatred in social media.
REFERENCES
[1] A. Schmidt and M. Wiegand, “A survey on hate speech detection
using natural language processing,” in SocialNLP@EACL, 2017.
[2] P. Fortuna and S. Nunes, “A survey on automatic detection of hate
speech in text,” ACM Computing Surveys (CSUR), vol. 51, pp. 1 –
30, 2018.
[3] F. Poletto, V. Basile, M. Sanguinetti, C. Bosco, and V. Patti,
“Resources and benchmark corpora for hate speech detection: a
systematic review,” Language Resources and Evaluation, vol. 55,
pp. 477 – 523, 2020.
[4] M. S. Jahan and M. Oussalah, “A systematic review of hate
speech automatic detection using natural language processing,”
Neurocomputing, vol. 546, p. 126232, 2021.
[5] I. Barna and ´A. Knap, “An exploration of coronavirus-related
online antisemitism in hungary using quantitative topic model and
qualitative discourse analysis,” Intersections. East European Journal
of Society and Politics, vol. 7, no. 3, pp. 80–100, 2021.
[6] C. Allen, U. Nodelman, and E. N. Zalta, “Stanford encyclopedia of
philosophy: a dynamic reference work,” 2003 Joint Conference on
Digital Libraries, 2003. Proceedings., pp. 383–, 2003.
[7] L. Wittgenstein, “Philosophical investigations = philosophische un-
tersuchungen,” in PHILOSOPHICAL INVESTIGATIONS, 1958.
[8] E. Rosch, “Principles of categorization,” in Cognitive Science, 1978.
[9] R. Corizzo, M. I. Baron, and N. Japkowicz, “Cpdga: Change point
driven growing auto-encoder for lifelong anomaly detection,” Knowl.
Based Syst., vol. 247, p. 108756, 2022.
[10] K. Faber, R. Corizzo, B. Sniezynski, and N. Japkowicz, “Vlad: Task-
agnostic vae-based lifelong anomaly detection,” Neural networks : the
official journal of the International Neural Network Society, vol. 165,
pp. 248–273, 2023.
[11] S. Rohlfing and S. J. Sonnenberg, ““who is really british anyway?”:
A thematic analysis of responses to online hate materials,” Journal
of psychosocial research, vol. 10, p. 2, 2016.
[12] T. Megersa and A. M. Gezie, “Social media users’ online behavior
with regard to the circulation of hate speech,” Frontiers in Commu-
nication, 2023.
[13] S. Ramaswamy and N. DeClerck, “Customer perception analysis
using deep learning and nlp,” Procedia Computer Science, vol. 140,
pp. 170–178, 2018.
[14]
´A. Aldunate, S. Maldonado, C. Vairetti, and G. Armelini, “Un-
derstanding customer satisfaction via deep learning and natural
language processing,” Expert Syst. Appl., vol. 209, p. 118309, 2022.
[15] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N.
Gomez, Ł. Kaiser, and I. Polosukhin, “Attention is all you need,”
Advances in neural information processing systems, vol. 30, 2017.
[16] A. M. Founta, D. Chatzakou, N. Kourtellis, J. Blackburn, A. Vakali,
and I. Leontiadis, “A unified deep learning architecture for abuse
detection,” in Proceedings of the 10th ACM conference on web
science, pp. 105–114, 2019.
[17] J. Serra, I. Leontiadis, D. Spathis, G. Stringhini, J. Blackburn, and
A. Vakali, “Class-based prediction errors to detect hate speech with
out-of-vocabulary words,” in Proceedings of the first workshop on
abusive language online, pp. 36–40, 2017.
[18] P. Parikh, H. Abburi, N. Chhaya, M. Gupta, and V. Varma,
“Categorizing sexism and misogyny through neural approaches,”
ACM Transactions on the Web (TWEB), vol. 15, no. 4, pp. 1–31,
2021.
[19] P. Badjatiya, S. Gupta, M. Gupta, and V. Varma, “Deep learning
for hate speech detection in tweets,” in Proceedings of the 26th
international conference on World Wide Web companion, pp. 759–
760, 2017.
[20] M. Chandra, D. Pailla, H. Bhatia, A. Sanchawala, M. Gupta,
M. Shrivastava, and P. Kumaraguru, ““subverting the jewtocracy”:
Online antisemitism detection using multimodal deep learning,” in
Proceedings of the 13th ACM Web Science Conference 2021, pp. 148–
157, 2021.
[21] S. Zannettou, J. Finkelstein, B. Bradlyn, and J. Blackburn, “A
quantitative approach to understanding online antisemitism,” in
Proceedings of the International AAAI conference on Web and Social
Media, vol. 14, pp. 786–797, 2020.
[22] M. Ali and S. Zannettou, “Analyzing antisemitism and islamophobia
using a lexicon-based approach,” in Workshop Proceedings of the
16th International AAAI Conference on Web and Social Media.
Retrieved from https://doi. org/10.36190, 2022.
[23] D. Kikkisetti, R. Ul-Mustafa, W. Melillo, R. Corizzo, Z. Boukou-
valas, J. Gill, and N. Japkowicz, “Using llms to discover emerging
coded antisemitic hate-speech in extremist social media,” ArXiv,
vol. abs/2401.10841, 2024.
[24] S. Ben-David, D. P´al, and H. U. Simon, “Stability of k -means
clustering,” in Annual Conference Computational Learning Theory,
2007.
[25] D. Dueck and B. J. Frey, “Non-metric affinity propagation for
unsupervised image categorization,” in 2007 IEEE 11th international
conference on computer vision, pp. 1–8, IEEE, 2007.
[26] K. G. Derpanis, “Mean shift clustering,” Lecture Notes, vol. 32,
pp. 1–4, 2005.
VII. APPENDIX

--- Page 10 ---

30
20
10
0
10
20
30
15
10
5
0
5
10
15
0
2
4
6
8
10
12
14
Target
(a) Affinity Propagation
30
20
10
0
10
20
30
15
10
5
0
5
10
15
0
50
100
150
200
250
300
Target
(b) Birch
30
20
10
0
10
20
30
15
10
5
0
5
10
15
0
1
2
3
4
5
6
7
8
Target
(c) Birch (with K)
30
20
10
0
10
20
30
15
10
5
0
5
10
15
0
1
2
3
4
5
6
7
Target
(d) Spectral
30
20
10
0
10
20
30
15
10
5
0
5
10
15
0
1
2
3
4
5
6
7
8
Target
(e) Gaussian
30
20
10
0
10
20
30
15
10
5
0
5
10
15
0.0
0.2
0.4
0.6
0.8
1.0
Target
(f) MeanShift
30
20
10
0
10
20
30
15
10
5
0
5
10
15
0
1
2
3
4
5
6
7
8
Target
(g) Our Approach
Fig. 4. T-SNE projections of the clustering obtained by our approach and baseline clustering methods

--- Page 11 ---

TABLE IV
EXAMPLES FROM OUR DATA SET OF POSTS FOUND ON EXTREME SOCIAL PLATFORMS ALONG WITH THE CONCEPT THEY BELONG TO AND THE
TERMINOLOGY THEY USE AS EXTRACTED BY THE APPROACH IN [23]
Posts
Concepts
these poor souls were murdered by the cabal world economic forum evil mad scientists elites. they should all be in front of a patriot firing
squad
C1
the illegal us corp of american government must be eradicated closed permanently all the cabal ,illuminate, world economic forum, world
health organization, united nation, north atlantic treaty organization, new world order and its sub cults all must be arrested and fully
prosecuted world wide door to door
C1
the goyim know about isis.
C2
shut it down, the goyim know
C2
advertising should be banned. it has been used as a social manipulation tool for decades. just watch mad men. it started with the frankfurt
school. the birth of cultural marxism. how the frankfurt school changed america
C3
we are in a war with frankfurt school cultural marxism . harris is an apostle of that woke cult. please stop conflating liberalism with left
wing marxism when we need to divide them starting with the difficult task of convincing boomer liberals they have been fooled since
teenage hood.
C3
you also need to provide all zionist agents embedded in the media organizations, zionist codenames, zionist handlers, zionist caves they
report to, zionist time travellers giving them information, space time information about zionists, zionist ”partner/s”, zionist alliances, zionist
sponsored businesses, zionist media organizations, zionist agents embedded in the national security apparatuses,zionist agents’ names
censoring news and content, etc., etc. ...
C4
the united states government is controlled by interest groups that are only seeking to enlarge their own power. the us government does not
represent the will of the citizenry, and condemning it is not a condemnation on the principles of freedom, democracy, etc.the usa is being
set up to fail.the rootless cosmopolitan elite have been constructing elaborate safehouses for decades in preparation for this...
C4
did jesus came to his own? yes but his own did not receive him? that is correct. so jews killed jesus? yes. so jesus was jewish? no, jews
are not the jews of the bible so how did jews commit deicide if they are not the jews from the bible? hurr durr
C5
he was but the definition of jew changed entirely after the fulfilment of the prophecy those who calls themselves jews now are not the real
jews they are the rabbinical tradition that rejected christ
C5
meet the new shabbos, same as the old shabbos stop eating the kosher sandwich goy zionist occupied government.
C6
zog, zionist occupied government. secretary of state=zog. attorney general=zog. senate majority leader=zog. head of dhs=zog 98 percent of
americans are non jews.
C6
are the jews of belgium, providing the zionist codenames, zionist agent names, names of the zionist reptilians, names of the zionist
”partner/s”, zionist caves, space time information about zionist, etc need full disclosure from the zionists, zionist reptilians, zionist agents,
zionist ”partner/s”, and reptilian ”partner/s”, etc. afterwards, i will slaughter them all, including their women, and their children. i will spare
no one.but then again, i prefer genocides, mass erasures, etc., rather than patches.
C7
i also need the names of all zionist partner/s, all zionist agents, zionist caves, zionist time travel agents, zionist time portal technology,
zionist advanced technology, and zionist reptilian ”partner/s”.and all zionist reptilians embedded in albania, and zionist reptilian ”partner/s”
embedded in albania.all can be published in the online domain, on the internet, available for all to dissect such information.afterwards, i
will slaughter them all. including zionist women, and zionist children, zionist ”partner/s”, and those that interfere on behalf of zionists.
C7
you can post about the gae all you want and not get banned on any platform, like scott greer for example. start tweeting about the zionist
occupied government and expect to be censored and banned. lesson there.
C8
you got a gay jewish communist takeover that is as communist as the chinese, without putting communist in the name.enjoy being spied,
subverted, and psyoped.
C8
klaus schwab is a rothschild on his mother side. he answers to the trillionaire, jacob rothschild and his khazarian mafia minions
C9
radical soros backed group boosts warnock campaign funding ahead of run off billionaire radical george soros has worked his entire life to
control the democrat party and destroy the united states. he has a deep seated hatred of the west and promotes its collapse, pouring millions
of dollars into campaigns and causes that further his radical agenda.
C9

```
