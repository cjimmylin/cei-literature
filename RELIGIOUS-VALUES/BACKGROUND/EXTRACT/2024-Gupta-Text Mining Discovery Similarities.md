---
title: "Text Mining Discovery Similarities - PDF Extract"
source_pdf: "2024-Gupta-Text Mining Discovery Similarities.pdf"
pages: 20
extracted_at: "2026-04-03T11:05:43.832866"
---

# PDF Extract: Text Mining Discovery Similarities

**Source PDF:** 2024-Gupta-Text Mining Discovery Similarities.pdf
**Total Pages:** 20

---

## Content

--- Page 1 ---

A Text Mining Discovery of Similarities and Dissimilarities
Among Sacred Scriptures⋆,⋆⋆
Younous Mofenjou Peuriekeua,∗, Victoire Djimna Noyuma,1, Cyrille Feudjioa,2, Alkan Göktug.c
and Ernest Fokouéb
aSchool of Mathematical Sciences, African Institute for Mathematical Sciences, Crystal Garden, Limbe Cameroon
cSchool of Mathematical Sciences, ETH Zurich, Rämistrasse 101, 8092 Zurich, Switzerland
bSchool of Mathematical Sciences, Rochester Institute of Technology, Rochester, NY 14623, USA
A R T I C L E I N F O
Keywords:
Sacred text
Text Mining
DTM
Distance
Classiﬁcation
A B S T R A C T
The careful examination of sacred texts gives valuable insights into human psychology, diﬀerent
ideas regarding the organization of societies as well as into terms like truth and God. To improve
and deepen our understanding of sacred texts, their comparison and their separation is crucial.
For this purpose, we use of our data set has nine sacred scriptures. This work deals with sepa-
ration of the Quran, the Asian scriptures Tao-Te-Ching, the Buddhism, the Yogasutras and the
Upanishads as well as the four books from the Bible, namely the Book of Proverbs, the Book of
Ecclesiastes, the Book of Ecclesiasticus and the Book of Wisdom. These scriptures are analyzed
based on the natural language processing NLP creating the mathematical representation of the
corpus in terms of frequencies called document term matrix (DTM). After this analysis, machine
learning methods like supervised and unsupervised learning are applied to perform classiﬁca-
tion. Here we use the Multinomial Naive Bayes (MNB), the Super Vector Machine (SVM), the
Random Forest (RF) and the K-nearest Neighbors (KNN). We obtain that among these methods
MNB is able to predict the class of a sacred text with an accuracy about 85.84 %.
1. Introduction
The progress in transportation and communication that has brought all the people of the world into one global
village has also brought the religions of the world into close contact. To know what is unique or speciﬁc about a
religion and how religion has gained importance in the life of humans, it is helpful to understand the structural patterns
of these texts. Generally, when we talk about sacred or holy text, we refer to the religious context. Sacred Scripture
are passages from the religious traditions. Often, these scriptural passages support a common theme. This method
of organization allows each topic to be addressed with the resources of many diﬀerent traditions, often providing a
broader and deeper understanding of the topic than considering only the resources of a single tradition. Each religion
has much value to contribute to humankind’s understanding of truth, which transcends any particular expression. The
proper description of religion is an area of study that has been tackled on diﬀerent standpoints. Some of the common
approaches to the study of religion are through history, anthropology, psychology and sociology.
• The historians have been interested in religion as a social movement and has traced the development of various
religions.
⋆This document is the results of the research project funded by the National Science Foundation.
⋆⋆The second title footnote which is a longer text matter to ﬁll through the whole text width and overﬂow into another line in the footnotes area
of the ﬁrst page.
This note has no numbers. In this work we demonstrate 푎푏the formation Y_1 of a new type of polariton on the interface between a cuprous
oxide slab and a polystyrene micro-sphere placed on the slab.
∗Corresponding author
∗∗Principal corresponding author
cvr_1@tug.org.in (Y.M. Peuriekeu); rishi@stmdocs.in (A. Göktug.); cvr3@sayahna.org (E. Fokoué)
www.cvr.cc,cvr@sayahna.org (Y.M. Peuriekeu); www.stmdocs.in (A. Göktug.); www.sayahna.org (E. Fokoué)
ORCID(s): 0000-0001-7511-2910 (Y.M. Peuriekeu)
1This is the ﬁrst author footnote. but is common to third author as well.
2Another author footnote, this is a very long footnote and it should be a really long footnote. But this footnote is not yet suﬃciently long enough
to make two lines of footnote text.
YOUNOUS MOFENJOU PEURIEKEU et al.: Preprint submitted to Elsevier
Page 1 of 20
arXiv:2102.04421v1  [stat.OT]  8 Feb 2021

--- Page 2 ---

Comprehensive Text Mining on Various Sacred Scriptures
• The anthropologists have been interested in the genetic approach in the study of man, both in physiological and
psychological aspects.
• The sociologist is essentially interested in the institutional and the ritualistic aspects of religion.
The transcendentalist approach shows that religion concerns values and ideas. This approach is diﬀerent from other dis-
ciplines of social sciences because, while the latter studies religion only as a structure, the former studies the religious
values constituting the inner core of religion.
There are many diﬀerent ﬁelds studying religions. These studies are always based on investigations on the scrip-
tures. Hence, understanding a religion requires an analysis of its religious scripture.
1.0.1. The sacred texts of our study
• Quran:
It is the single-authored, central religious text of Islam and written in the eastern Arabian dialect of Classical
Arabic. The Quran has 30 divisions or Juz with 114 chapters as Surah, according to the length of surahs, but not
according to when they were revealed and not by subject matter. Each Surah is subdivided into verses or Ayat.
The Quran contains about 6,236 verses with 77,477 words. The Quran is believed to be orally revealed by God
through the archangel Gabriel to Muhammad, considered as the ﬁnal prophet by Muslims. These three corpora
are highly unstructured and do not follow or adhere to structured or regular syntax and patterns. Before applying
any statistical technique or machine learning algorithm, the corpus needs to be converted into a structured text
or a vector format that these techniques and algorithms can work with (Sah and Fokoué, 2019).
• Asian text:
– Yogasutras: From India
This Book contains essence of wisdom. It states that humans think of themselves as living a purely physical
life in their material bodies. The central claim is that, in reality, they have gone far indeed from pure physical
life; for ages, their life has been psychical, and they have been centered and immersed in the psychic nature
(Sah and Fokoué, 2019).
– Buddhism:
This book teaches the so-called four noble truth. Each of these truths entails a duty: stress is to be compre-
hended, the origination of stress is to be abandoned, the cessation of stress is to be realized, and the path
to the cessation of stress is aimed to be developed. When all of these duties have been fully performed, it
is believed that the mind gains total release(Sah and Fokoué, 2019).
– Tao Te Ching: Which is from China
Tao Te Ching is a Chinese classic text traditionally credited to the 6푡ℎcentury BC sage Laozi. The Tao
Te Ching is a short text which has two parts, the Tao Ching (chapters 1-37) and the Te Ching ( chapters
38-81), which may have been edited together into the received text, possibly reversed from an original Te
Tao Ching. The chapters talk about staying detached, letting go and keeping things simple.
– The Upanishads:
This book represents the loftiest heights of ancient Indo-Aryan thought and culture. They form the wisdom
portion or Gnana-Kanda of the Vedas, as contrasted with the Karma-Kanda or sacriﬁcial portion. From
each of the four great Vedas known as Rik, Yajur, Sama and Atharva, there is a large portion which deals
predominantly with rituals and ceremonials aiming to teach humans how they can prepare themselves for
higher attainment (Sah and Fokoué, 2019).
• Christianity books: Their origin is from Central Asia/America
– Book of Proverbs:
The Book of Proverbs is the Book of where we have the wise sentences regulating the morals of men and
directing them to virtue.
– Book of Ecclesiasticus:
From this Book of Ecclesiasticus, it brings out the remarkable lessons of the virtues.
YOUNOUS MOFENJOU PEURIEKEU et al.: Preprint submitted to Elsevier
Page 2 of 20

--- Page 3 ---

Comprehensive Text Mining on Various Sacred Scriptures
– Book of Ecclesiastes :
Also called the preacher, the Book of Ecclesiastes is one of the Christian Books, where Solomon plays a
very important role as a preacher.
– Book of Wisdom:
The Book of Wisdom abounds with instructions and exhortations to kings and all magistrates to minister
justice in the commonwealth, teaching all kinds of virtues under the general names of justice and wisdom
(Sah and Fokoué, 2019).
1.1. Text analysis and learning
To deﬁne text analysis, we can say that, it is the technique used to model and structure the information content
of textual sources for investigation, exploratory data analysis, and research. This technique is described by the set of
statistical and machine learning approach. This technique is very useful in text mining to simplify the data analysis,
research, and investigation(Hobbs, Walker and Amsler, 1982). It is an instance of text analysis applications.
On the other hand, text analysis also refers to the set of processes analyzing a very large amount of unstructured text
data to come up with many attributes as topics respectively keywords. Hence, Natural Language Processing (NLP),
Natural Language Understanding (NLU) and Data Mining (DM) are overlapping areas which include techniques to
process large corpora and extract useful information(Elton, Turakhia, Reddy, Boukouvalas, Fuge, Doherty and Chung,
2019). As technique of extraction, we have text pre-processing, text normalization, text categorization, text clustering,
text similarity etc. However, the corpus are the collection of sentences with phrases and words. For a given unstructured
text data, the foundation of an analysis is the text pre-processing and text normalization converting the raw corpus to
structured data whereas, text clustering and text similarity are processes to check the degree of closeness of two corpora
and the process of grouping similar documents respectively.
1.2. Objectives
Text mining is an approach that combines several ﬁelds of research and also several software tools. According to
(Ignatow and Mihalcea, 2017), this is a technique that has begun to develop in social sciences such as anthropology,
communication (Ezzeldin and El-Dakhakhni, 2020), economics (Levenberg, Pulman, Moilanen, Simpson and Roberts,
2014), education (Evison, 2013), and psychology (Sklad, Diekstra, Ritter, Ben and Gravesteijn, 2012). Social scientists
have spent many decades studying transcribed interviews, newspaper articles, speeches, and other forms of textual data.
After discovering the new, more sophisticated and rapid method of text mining, they have begun to adapt this approach
to diﬀerent forms of textual data analysis. Text mining also takes into account computer science. So, in our study,
we will not limit ourselves to the use of this new analysis technique, but also study the extension of natural language
mining.
The reason why we have come to a multiplicity of religious teachings is due to the fact that their sacred texts are
diﬀerent from one religion to another. The fact that they are diﬀerent can be explained by the lessons they teach their
followers, their period of appearance, and also their geographical location. In this study, we will deepen the excavation
of sacred texts by using text mining techniques.
Besides analyzing the diﬀerences between the books, it is also crucial to extract their similarities. This work
attempts to ﬁnd the similarity using text mining techniques.
Automated lexical analysis techniques are used nowadays for retrieval of useful information from large amounts
of unstructured texts. Several studies have been done in order to study diﬀerent religions. Frank Lloyd Sindler et al.
(Sindler, 2011) have written a thesis on a comparative study of Christian, Jewish, and Islamic theodicy. No automated
technique has been used to analyze the lexical content of religious texts and only three religions have been considered
in this study. Altogether, very little eﬀorts have been made in the past to automatize analysis of important religious
texts.
Daniel McDonald et al (McDonald, 2014) presented a method for automated extraction of topics from nine religious
texts to form a self-organizing map to ﬁnd relationships between these religious texts. The backdraw of this study is
that only nine were taken into consideration leaving out important world religions.
Buddhism, Jainism , Sikhism .Qahl, Salha Hassan Muhammed et al. (Qahl, 2014) developed an automatic similar-
ity detection engine using the Bible and the Quran as corpus to explore the performance of various feature extraction
and machine learning techniques. Only two religious texts were taken into consideration and it did not give deeper
insight into diﬀerences regardings the ideas and beliefs proposed by these two religions.
YOUNOUS MOFENJOU PEURIEKEU et al.: Preprint submitted to Elsevier
Page 3 of 20

--- Page 4 ---

Comprehensive Text Mining on Various Sacred Scriptures
The most recent work was done by Preeti and al. (Sah and Fokoué, 2019) where height sacred text were used, four
from the Bible and four from Asian religions to present the statistical machine learning approach and to analyze many
aspects of sacred texts from both the Asian and Biblical scriptures. Thus, in our study, we will extend the amount
of religious books by adding the Islamic sacred scripture and then use a more sophisticated and rapid method of text
mining, namely the natural language processing (NLP) to extract the high quality information from those books. Based
on this, we will explore the performance of various feature extraction methods and machine learning techniques.
2. Text analysis and learning
After getting the diﬀerent sacred texts that we will use for this study, we proceed with analyzing them in a structured
manner. We begin with the Part-Of-Speech (POS) which is the process of marking up the word in a corpus (text) as
corresponding to the special part of the speech based on both its deﬁnition and its context. For our analysis we will use
the package nltk in Python. After presenting the Information Retrieval, we give an overview about Natural Language
Processing. Then we explain the diﬀerent steps of the pre-processing.
2.1. Information Retrieval
Before stating the pre-processing, we need to understand some concepts related to knowledge discovery. Infor-
mation Retrieval (IR) means ﬁnding documents that contain information about a certain term respectively keyword
(Manning, Manning and Schütze, 1999). For instance, Google does such kind of retrieval in their search engine.
This search engine uses query based algorithm to track the trends and attain more signiﬁcant results. However, this
application has many more everyday uses such as email search or searching a ﬁle on a personal computer.
2.2. Natural Language Processing
Natural language processing (NLP) refers to the automatic processing and analysis of unstructured text data. It
is important to underline that NLP performs diﬀerent types of analysis such as Named Entity Recognition (NER) for
abbreviation and their synonyms extraction to ﬁnd the relationships among them (Laxman and Sujatha, 2013). From
this approach, we can identify all the instances of speciﬁed objects from a group of documents. Moreover, it allows
the identiﬁcation of relationship and other information to attain their key concept. In real world, a single entity has
numerous terms like TV and Television.
2.3. Pre-processing
To give an overview of what we call pre-processing, we can say that it is the conversion of raw text data to a
structured sequence of linguistic components in the form of a standard vector. Examples of pre-processing techniques
are:
• Tokenization ;
Tokenization here means the process of splitting words, sentences or texts into a list of tokens. The components
with special syntax and semantics are called "tokens". We distinguish two tokenization techniques, namely word
tokenization and sentence tokenization. Word tokenization is the technique of splitting sentences into constituent
words and sentences tokenization is the process of splitting the text corpus to meaningful sentences.
• Stemming ;
Stemming means the reduction of words to their roots so that, for instance, the diﬀerent grammatical forms or
declinations of verbs are identiﬁed and counted as the same word (Nisbet, Elder and Miner, 2009). So basi-
cally this step is an important approach for information retrieval and text analysis applications. An example is
clustering and automatic text processing.
• Lemmatization.
Lemmatization is a process to resolve words to their dictionary form. In fact, a lemma of a word is its dictionary
form. To resolve a word to its lemma, its part-of-speech is needed. Another aspect to note about lemmatization
is that it is often times harder to create a lemmatizer in a new language than stemming.
It is also relevant to mention that by using text pre-processing, we can manage to extract the knowledge from the
text data (corpus) which is needed for a good analysis and for an high accuracy of classiﬁers. We can see those steps
in ﬁgure 1
YOUNOUS MOFENJOU PEURIEKEU et al.: Preprint submitted to Elsevier
Page 4 of 20

--- Page 5 ---

Comprehensive Text Mining on Various Sacred Scriptures
Figure 1: The diﬀerent step of Pre-processing.
2.4. Document term matrix
To make the unstructured texts data useful, we need to transform the textual data into vector spaces, which can be
done by using what we call Bag-Of-Words (BOW) representation. The BOW converts the text data in a matrix format
which simplify the statistical analysis of the data. The obtained matrix is called Document Term Matrix (DTM). The
rows in this matrix represent the documents and the columns represent the terms. The DTM gives the occurrence of
each term varying among the documents.
In this study, we will use nine diﬀerent books (T = 9), with 704 chapters/documents (n = 704) and 5131 (p=5131)
tokens/words. Hence, we have a 704 x 5131 DTM. When we consider the 푡푡ℎsacred scripture separately by means of
its own DTM 푋푡, its representation looks like follows:
푋(푡) =
⎡
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢⎣
푋(푡)
1,1
푋(푡)
1,2
…
…
…
푋(푡)
1,푗푡
…
푋(푡)
1,푝푡
푋(푡)
푖푡,1
푋(푡)
푖푡,2
…
…
…
푋(푡)
푖푡,푗푡
…
푋(푡)
푖푡,푝푡
∶
∶
⋱
⋱
…
∶
…
∶
푋(푡)
푛푡,1
푋(푡)
푛푡,2
…
…
…
푋(푡)
푛푡,푗푡
…
푋(푡)
푛푡,푝푡
⎤
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥⎦
(1)
YOUNOUS MOFENJOU PEURIEKEU et al.: Preprint submitted to Elsevier
Page 5 of 20

--- Page 6 ---

Comprehensive Text Mining on Various Sacred Scriptures
From this matrix, each column 푋(푡)
.,푗푡represents a term and each row 푋(푡)
푖푡,. represents a document/chapter.
If we consider the whole corpus of sacred books, the Document Term Matrix is deﬁned by the following relation:
푋=
⎡
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢⎣
푋(1)
1,1
푋(1)
1,2
…
…
…
푋(1)
1,푗1
…
푋(1)
1,푝
∶
∶
⋱
⋱
…
∶
…
∶
푋(1)
푖1,1
푋(1)
푖1,2
…
…
…
푋(1)
푖1,푗1
…
푋(1)
푖1,푝
∶
∶
⋱
⋱
…
∶
…
∶
푋(1)
푛1,1
푋(1)
푛1,2
…
…
…
푋(1)
푛1,퐽1
…
푋(1)
푛1,푝
∶
∶
⋱
⋱
…
∶
…
∶
∶
∶
⋱
⋱
…
∶
…
∶
푋(푡)
1,1
푋(푡)
1,2
…
…
…
푋(푡)
1,푗푡
…
푋(푡)
1,푝
∶
∶
⋱
⋱
…
∶
…
∶
푋(푡)
푖푡,1
푋(푡)
푖푡,2
…
…
…
푋(푡)
푖푡,푗푡
…
푋(푡)
푖푡,푝
∶
∶
⋱
⋱
…
∶
…
∶
푋(푡)
푛푡,1
푋(푡)
푛푡,2
…
…
…
푋(푡)
푛푡,푗푡
…
푋(푡)
푛푡,푝
∶
∶
⋱
⋱
…
∶
…
∶
∶
∶
⋱
⋱
…
∶
…
∶
푋(푇)
1,1
푋(푇)
1,2
…
…
…
푋(푇)
1,푗푇
…
푋(푇)
1,푝
∶
∶
⋱
⋱
…
∶
…
∶
푋(푇)
푖푇,1
푋(푇)
푖푇,2
…
…
…
푋(푇)
푖푇,푗푇
…
푋(푇)
푖푇,푝
∶
∶
⋱
⋱
…
∶
…
∶
푋(푇)
푛푇,1
푋(푇)
푛푇,2
…
…
…
푋(푇)
푛푇,푗푇
…
푋(푇)
푛푇,푝
⎤
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥⎦
(2)
2.5. Similarities between sacred texts
After converting the documents into term vectors, the similarity between them can be estimated by comparing the
corresponding vectors. To distinguish the documents precisely, there are various algorithms which can be used. In
this part, we will describe some of the standard distances used in text analysis like the cosine similarity, Euclidean
distance, Manhattan distance (Qahl, 2014).
2.5.1. Term frequency inverse document frequency
The most common document similarity algorithm is term frequency-inverse document frequency (Tf-IDF). he
Term Frequency (TF) means that the more frequently one term appears in a document the more its weight increases.
In inverse document frequency (IDF), the term occuring in a greater number of documents are relatively less relevant
and should be weighted less. It is presented mathematically by the equation 3 where 푓푟푒푞푖,푗represents the number of
occurrences of the word j in ﬁle i and 푊푖푗is the weight of word j in ﬁle i.
푡푓푖,푗=
푓푟푒푞푖,푗
max(푓푟푒푞푖,푗)
(3)
From equation 4, 푚represents the number of ﬁles, 푚푗represents the number of ﬁles containing the word j.
푖푑푓푖,푗= log 푚
푚푗
(4)
YOUNOUS MOFENJOU PEURIEKEU et al.: Preprint submitted to Elsevier
Page 6 of 20

--- Page 7 ---

Comprehensive Text Mining on Various Sacred Scriptures
And the weight is calculated according to equation 5:
푊푖,푗= 푡푓푖,푗⋅푖푑푓푖,푗
(5)
2.5.2. Distance measures
In this part of our study, we will explore the similarity respectively dissimilarity between chapters and documents by
applying the non-standard distances like cosine similarity and also some standard distances such as Euclidean distance,
Manhattan distance and Jaccard similarity (SAH and FOKOUÉ, 2019). Notice that not every distance measure is a
metric. A metric must satisfy four conditions. Let 퐴and 퐵be any two documents and 푑(퐴, 퐵) be the distance between
both (Maher and Joshi, 2016). The conditions read as follows:
• The distance between any two given points must be nonnegative. Mathematically, it is:
푑(퐴, 퐵) ≥0
• The distance between two points is equal to zero (0) if and only if the two points are the same. It is formulated:
푑(퐴, 퐵) = 0
푖푓푓
퐴= 퐵
• The distance must be symmetric, which means that the distance from A to B is the same as the distance from B
to A.
푑(퐴, 퐵) = 푑(퐵, 퐴)
• The distance measure must satisfy the inequality 6 which is the triangle inequality.
푑(퐴, 퐶) ≤푑(퐴, 퐵) + 푑(퐵, 퐶)
(6)
The diﬀerent distance similarity measures which can facilitate the interpretation or understanding of the similarity
respectively dissimilarity between documents can also be applied for the corpus. In text mining, we deal with high-
dimensional data. The sparsity of the raw data makes the study more complex.
• The Euclidean distance measure :
The euclidean distance can be deﬁned as the shortest straight-line distance between two points. It is part of the
Minkowski family. The Minkowski distance is a metric distance class on the Euclidean space (Deza and Deza,
2006). The mathematical representation of Eucleidean distance is given by equation 7.
푑퐸(푋(푎)
푙, 푋(푏)
푚) =
√
√
√
√
푝
∑
푗=1
(푋(푎)
푙,푗−푋(푏)
푚,푗)2
(7)
• The Jaccard similarity measure:
The Jaccard similarity measure is approached used to measure the similarity between two chapters/documents
by taking the intersection of both and divide it by their union (Zahrotun, 2016). The Jaccard coeﬃcient between
two documents 푋(푎)
푙
and 푋(푏)
푚is mathematically deﬁned by:
푠푖푚(푋(푎)
푙, 푋(푏)
푚) ≡푠푖푚(푋푙, 푋푚) =
푝
∑
푗=1
min{푋푙푗, 푋푚푗}
푝
∑
푘=1
max{푋푙푘, 푋푚푘}
(8)
Thus, by using the equation 8 the Jaccard distance between two document is given by the equation 10:
푑퐽(푋(푎)
푙, 푋(푏)
푚) ≡푑퐽(푋푙, 푋푚) = 1 −푠푖푚(푋푙, 푋푚)
(9)
YOUNOUS MOFENJOU PEURIEKEU et al.: Preprint submitted to Elsevier
Page 7 of 20

--- Page 8 ---

Comprehensive Text Mining on Various Sacred Scriptures
• The Manhattan distance measure :
The Manhattan Distance is the sum of absolute diﬀerences between points across all the dimensions.
푑푀(푋(푎)
푙, 푋(푏)
푚) =
푝
∑
푗=1
|푋(푎)
푙,푗−푋(푏)
푚,푗|
• The Cosine similarity measure
The Cosine similarity measure considers the correlation between the vectors. It is also the most popular similarity
measure applied to text documents (Maher and Joshi, 2016). The formulation of this measure is deﬁned by:
푑퐶표푠(푋(푎)
푙, 푋(푏)
푚) ≡푑퐶표푠(푋푙, 푋푚) =
푋푇
푙푋푚
(푋푇
푙푋푙)
1
2 (푋푇
푚푋푚)
1
2
(10)
2.5.3. Text similarity measures
After having introduced the distance similarity measures, we can use them to explore the similarity between books
respectively documents.
First of all, we are going to compare the similarity between chapters within the same book. For instance in book
푋훼, the distance between the chapters is mathematically represented by:
퐷(훼) =
⎡
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢⎣
푑(훼)
1,1
푑(훼)
1,2
…
푑(훼)
1,푛훼
푑(훼)
2,1
푑(훼)
2,2
…
푑(훼)
2,푛훼
∶
∶
⋱
∶
푑(훼)
푛훼,1
푑(훼)
푛훼,2
…
푑(훼)
푛훼,푛훼
⎤
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥⎦
Notice that the matrix 퐷(훼) is nonnegative 푛훼× 푛훼
(
ℝ푛훼×푛훼
+
)
.
The components are deﬁned as : 푑(훼)
푙,푚≡푑(푋(훼)
푙, 푋(훼)
푚) ≡the distance between the 푙푡ℎchapter and the 푚푡ℎchapter
of the 훼푡ℎbook 푋(훼). This can help us to evaluate the relationship between various chapter within the same book.
If we want to discover the relationship between books 푋훼and 푋훽, we can use the following formula:
퐷=
⎡
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢⎣
푑1,1
푑1,2
…
푑1,푛
푑2,1
푑2,2
…
푑2,푛
∶
∶
⋱
∶
푑푛,1
푑푛,2
…
푑푛,푛
⎤
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥⎦
Also this 푛× 푛matrix is nonnegative (ℝ푛×푛
+ ).
푑푙,푚≡푑(푋(훼)
푙, 푋(훽)
푚) ≡is the distance between the 푙푡ℎchapter of the book 푋(훼) and the 푚푡ℎchapter of book 푋(훽).
This can help us to evaluate the relationship between various chapter within the same book.
There are four diﬀerent approaches existing to study the similarity between the sacred texts reading as following:
1. The ﬁrst approach for obtaining the distance between books is named single or minimum linkage and is given by
the relation 11. This simply means that the distance between two books, for instance 푋(훼) and 푋(훽), corresponds
to the smallest value of the 푛∗푛distance between their chapters. Mathematically, it is deﬁne as:
Δ(푋(훼), 푋(훽)) = min
푙∈[푛훼]
푚∈[푛훽]
{푑(푋(훼)
푙, 푋(훽)
푚)}
(11)
YOUNOUS MOFENJOU PEURIEKEU et al.: Preprint submitted to Elsevier
Page 8 of 20

--- Page 9 ---

Comprehensive Text Mining on Various Sacred Scriptures
2. The second approach for measuring distances between books is the maximum linkage given by the relation 12.
In this method the distance between two books, for instance 푋(훼) and 푋(훽), corresponds to the largest value of
the 푛∗푛distance matrix with respect to their chapters. Mathematically, it is deﬁned as:
Δ(푋(훼), 푋(훽)) = max
푙∈[푛훼]
푚∈[푛훽]
{푑(푋(훼)
푙, 푋(훽)
푚)}
(12)
3. The third approach for the distance between books is the average linkage and is deﬁned by the relation 13. Here,
the distance between two books, for instance 푋(훼) and 푋(훽), corresponds to the mean value of the 푛∗푛distance
matrix with respect to their chapters. It is written as:
Δ(푋(훼), 푋(훽)) = 푚푒푎푛푙∈[푛훼]
푚∈[푛훽]
{푑(푋(훼)
푙, 푋(훽)
푚)}
(13)
4. The last approach for distance between books is the median distance and it is deﬁned by the relation 14 which
reads:
Δ(푋(훼), 푋(훽)) = 푚푒푑푖푎푛푙∈[푛훼]
푚∈[푛훽]
{푑(푋(훼)
푙, 푋(훽)
푚)}
(14)
Having 퐵sacred books, we can give the expression of the distance between the whole set of book as
Δ =
⎡
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢⎣
Δ1,1
Δ1,2
…
Δ1,퐵
Δ2,1
Δ2,2
…
Δ2,퐵
∶
∶
⋱
∶
Δ퐵,1
Δ퐵,2
…
Δ퐵,퐵
⎤
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥⎦
where Δ훼,훽≡Δ(푋(훼), 푋(훽)) corresponds to the distance to the book 훼and the book 훽.
2.6. Learning sacred text recognition
For this research work, we use the Asian scripture, the Bible and Quran as our collection of texts (data), also
named corpus in this context. When we want to obtain the origin of a text or of a text fraction, we can use machine
learning making predictions about the source of these texts. Thus, in what follows, we will describe unsupervised and
supervised machine learning applied to text mining processes.
2.6.1. Introduction to machine learning
In machine learning, we have data with which the machine is trained. Based on this training, it learns patterns in the
data. For text analytics, machine learning involves a set of statistical techniques for identifying various characteristics
and patterns among the considered texts. Machine learning is divided into supervised and unsupervised learning which
will be described in the following. Due to the fact that the text data can have hundreds of thousands of dimensions
(sentences or words), text data requires a particular approach to machine learning.
• Unsupervised learning:
Unsupervised machine learning algorithms infer patterns from a dataset without reference to known or labeled
outcomes. Unlike supervised machine learning, unsupervised machine learning methods cannot be directly
applied to a regression or a classiﬁcation problem because of the missing labels. It is about training a model
without pre-tagging or annotating.
One of the most interesting questions is whether it is possible to classify texts according to the sacred books that
they originate from. In this section, as far as the relationships among entire sacred scriptures are concerned, we
herein brieﬂy describe the way in which we use cluster analysis to tackle and answer that overarching question.
YOUNOUS MOFENJOU PEURIEKEU et al.: Preprint submitted to Elsevier
Page 9 of 20

--- Page 10 ---

Comprehensive Text Mining on Various Sacred Scriptures
• Supervised learning:
In supervised learning the goal is to predict the label of a data sample. In the context of sacred text classiﬁcation,
we use labelled documents to train a model. In supervised machine algorithm, the goal is to achieve high
prediction accuracy after training with the machine.
So far, there exists a couple of algorithms that we can apply on the labeled corpus. Inter alia, we have the linear
classiﬁcation algorithms like K-nearest neighbors (KNN), Random Forest (RF) and we also have the Support
Vector Machines (SVM) which can be both linear and non-linear.
– The K-Nearest Neighbors (KNN):
In order to proceed with the categorization of texts, there are a number of methods and techniques that we
can apply. Seeing a new document, the KNN method assigns to this document the label that occurs the
most often among its closest neighbors.
– The Support Vector Machine (SVM):
The support vector machine (SVM) is one of the methods of supervised learning that generates input-output
mapping functions from a set of labeled training data (Wang, 2005). To perform classiﬁcation, the input
data is projected to an higher dimensional space feature space through nonlinear kernel functions enforcing
the seperability of the input data. In addition, the SVM creates a margin between the separating hyperplane
and the data.
The equation of the hyperplane is mathematically deﬁned as follow:
푤푇푥−푏= 0
The equation of separating hyperplanes are given by:
{
푤푇푥−푏= 1
푤푇푥−푏= −1
(15)
The ﬁrst instance is about the Hard Margin and the goal here is to maximize
2
∥푊∥which is equivalent
to minimizing ∥푤∥
2
.
We must have two (2) constraints:
{
푤푇푥(푖) −푏≥1
푖푓
푦(푖) = 1
푤푇푥(푖) −푏≤−1
푖푓
푦(푖) = −1
(16)
By combination of constraint, we have the following:
푦(푖)(푤푇푥(푖) −푏) ≥1 for 푖= 1, ..., 푚
For this second instance, the optimization function is deﬁned as:
푤∗= 푎푟푔푚푖푛∥푤∥2
The second instance is the Soft Margin. It allows for points to be inside the margin. The loss function
becomes the hinge loss which is used when one deals with discrete labels. It is mathematically deﬁned by:
(푤) = 1
푚
푚
∑
푖=1
푙(푤; 푥, 푦) + 휆∥푊∥2
2
(17)
with
푙(푤; 푥, 푦) = 푚푎푥[0, 1 −푦(푖)(푤푇푥(푖) −푏)]
Here, the optimization function is deﬁne as: 푤∗= 푎푟푔푚푖푛(푤)
YOUNOUS MOFENJOU PEURIEKEU et al.: Preprint submitted to Elsevier
Page 10 of 20

--- Page 11 ---

Comprehensive Text Mining on Various Sacred Scriptures
The third instance is the non-linear classiﬁcation. In this case, the feature 푥푖moves to the feature space
휙푖and the kernel trick is given by:
퐾(푥, 푥′) = 휙푇(푥) ⋅휙(푥′)
And the weight is equal to:
푤
=
푚
∑
푖=1
훼푖푦(푖)휙(푥(푖))
푤푇
=
푚
∑
푖=1
훼푖푦(푖)휙푇(푥(푖))
푤푇휙(푥(푖))
=
푚
∑
푖=1
훼푖푦(푖)퐾(푥(푖), 푥′)
– The Random Forest (RF):
We can name Random Forest as another tree classiﬁer, which can be used for classiﬁcation of text data.
Because of the fact that it is capable of extracting similarity between features, it is also used in text mining
as an embedded feature selection method.
2.6.2. Classiﬁcation function
Let 푥be the vector of word frequency corresponding to a chapter from one of the nine sacred texts. The probability
that this chapter 푥comes from the 푡푡ℎbook is denoted as ℙ[푦= 푠푡|푥] where 푦is the variable indicating the sacred
book.
The function 푓according to which classiﬁcation is done reads:
푓(푥) = 푎푟푔푚푎푥푡∈[푇]{ℙ[푦= 푠푡|푥]}
(18)
For the pure purpose of scripture authentication, we build the classiﬁer from the data ̂푓(푥). For instance, the classiﬁer
function for K-Nearest-Neighbors is given by:
̂푓(퐾푁푁)(푥) = 푎푟푔푚푎푥푡∈푇
{
1
푘
푛
∑
푗=1
핀(푦푗= 푡)핀(푥푗∈푘(푥))
}
2.6.3. Cross validation and Grid searching
To evaluate the performance of our model, we will Cross validate. Another method that is used for the selection
of the best hyperparameter conﬁguration is the Grid search.
• m-Fold Cross validation
Inspecting the test error, one can separate the data into a training and test set. However, this process may lead
accuracies that are very diﬀerent from one test to another using the same algorithm. To avoid this issue, we will
use the m-Fold Cross-Validation where 푚is a indicating the number of folds. In this process, we divide the
data into 푚folds. A training set is represented by 푚−1 set while the testing set is the remaining. After each
iteration it shuﬄe the data and create a new training and testing sets.
The cross-validation estimate of prediction error is given by
퐶푉( ̂푓) = 1
푁
푁
∑
푖=1
퐿(푦푖, ̂푓−푘(푖)(푥푖))
where 푘(푖) means, the model f is trained without the training patterns in the same partition of the dataset as
pattern 푖.
YOUNOUS MOFENJOU PEURIEKEU et al.: Preprint submitted to Elsevier
Page 11 of 20

--- Page 12 ---

Comprehensive Text Mining on Various Sacred Scriptures
• Grid searching
The hyperparameter optimization is essential in machine learning due to the fact that neural networks are diﬃcult
to conﬁgure and there are a lot of parameters that need to be set. Setting the hyperparameters manually can
consume a lot of time. Hence, we will use the grid search method for this purpose.
Grid-searching is the process of scanning the data to conﬁgure optimal parameters for a given model. Depending
on the type of model that is used, we need to adjust the parameters of the grid search algorithm. Grid-searching
stores a model by doing the iteration through every parameter combination and selects the optimal conﬁguration
for our model. The general formulation to compute the accuracy is given by:
퐴푐푐푢푟푎푐푦=
푇푃+ 푇푁
푇푃+ 푇푁+ 퐹푃+ 퐹푁
(19)
Where TP, TN, FP, FN means True Positive, True Negative, False Positive, False Negative respectively.
3. Results
We are presenting the diﬀerent results we got during our analysis. Starting by describing our data, continuous by
the distribution of the words, then we perform some text analysis and end by presenting the distance measurement.
3.1. Description of the data
Before starting the pre-processing, we needed to download the English version of Quran. Then we will do the
analysis on our data and transform the text into tokens. This transformation yields in total 156110 tokens. This step is
followed by removing useless tokens. Hence, punctuations ( e.g. - , : ""), stop words (e.g. as, it, very, own, any, only,
oﬀ) and integers (e.g. 1, 2, 3 etc) are removed. Finally, we get the cleaner data ready to be used.
3.2. Distribution of words
The frequency distribution contains the ratios between each token and the total number of tokens shown below in
ﬁgure 2.
Figure 2: Frequency distribution of words in text data.
In this graph, we can see that the word god is the most often used word. It is followed by the words lord and belive.
YOUNOUS MOFENJOU PEURIEKEU et al.: Preprint submitted to Elsevier
Page 12 of 20

--- Page 13 ---

Comprehensive Text Mining on Various Sacred Scriptures
Object
Label preﬁx
god
NN
lord
NN
said
VBD
believ
NN
allah
NN
may
MD
Table 1
The Part Of Speech tagging for the data
3.3. Frequency of Part-Of-Speech
In this section, we will present the Part-Of-Speech tagging that, we get from the list of tokens. Then, we will also
present the frequency plot of those POS tagging.
3.3.1. The Part Of Speech tagging
The following table, shows the few example of POS tagging which are from our list of tokens.
Figure 3: Frequency of POS tagging in text data.
From subsection 3.1 to session 3.3, we repeat the same method for the Asian books and the Bible.
3.4. Performance analysis
3.4.1. Document Term Matrix
• Document Terms Matrix of Quran
The following table describes the labeled document term matrix of Quran. From this table, we obtain that the
sacred book has 114 chapters/documents and 4284 terms/tokens. The value in each cell represents the number
of times that the word corresponding to that column occurs in the documents corresponding to that row.
YOUNOUS MOFENJOU PEURIEKEU et al.: Preprint submitted to Elsevier
Page 13 of 20

--- Page 14 ---

Comprehensive Text Mining on Various Sacred Scriptures
• Document Terms Matrix of Asian and Bible
The following table describe the labeled document term matrix of Asian and The holy Bible. The table shows
that these sacred books have together 590 chapters/documents and 1024 terms/tokens.
• Document Terms Matrix of both documents.
Firstly, when we put all the sacred texts together, we get the DTM with 704 chapters/documents and 5131
terms/tokens. We notice that there are some missing values which will not be needed for our analysis. Thus, the
next step consists of removing them. After removing all the missing values, we get the table below. It still has
704 chapters/documents and 5131 terms/tokens. This DTM will be used for several analysis that we make on
the sacred scriptures.
YOUNOUS MOFENJOU PEURIEKEU et al.: Preprint submitted to Elsevier
Page 14 of 20

--- Page 15 ---

Comprehensive Text Mining on Various Sacred Scriptures
Since we already have the matrix representation of the diﬀerent sacred texts, corresponding here to the previous
document term matrix (DTM), we will proceed with the studies of the distances/similarities between the chapters
of the same book, between the chapters of a sacred scripture with those of other sacred books and ﬁnally between
the diﬀerent books without dividing them into chapters.
3.5. Distance Measure
After converting the sacred books into term vectors, the distances/similarities between two documents can be
estimated by comparing the corresponding vectors. In this part, we will apply the Euclidean distance, the Manhattan
distance, the cosine similarity and the Jaccard distance.
3.5.1. Distance between chapters of all sacred books
• Euclidean distance
Using the Euclidean distance, we can visualize the distance matrix by its corresponding heatmap.
Figure 4: Heatmap of the Euclidean distance between the chapters in both sacred books.
YOUNOUS MOFENJOU PEURIEKEU et al.: Preprint submitted to Elsevier
Page 15 of 20

--- Page 16 ---

Comprehensive Text Mining on Various Sacred Scriptures
This heat map shows for instance that there is a very high distance between 10 −푡ℎdocument corresponding to
chapter 9 of Quran and the document with index 600 corresponding to chapter 14 in the Book of Wisdom.
• Cosine distance
Analogously, we obtain a distance matrix after applying the cosine distance and its heatmap representation
depicted below.
Figure 5: Heatmap of the cosine distance between the chapters in both sacred books.
This heat map shows for instance that, there is a considerable distance between the chapters of the books. This
is the reason why we have several block of color in the heat map.
3.5.2. Distances measure between sacred books
Regarding this part, we will show the diﬀerent distance measure between the sacred books.
• Euclidean distances
Figure 6: Heatmap of the Euclidean distance between sacred books
YOUNOUS MOFENJOU PEURIEKEU et al.: Preprint submitted to Elsevier
Page 16 of 20

--- Page 17 ---

Comprehensive Text Mining on Various Sacred Scriptures
Labels
0
1
2
3
4
5
Books
Quran
Buddhism
Tao-Te-Ching
Upanishad
Yogasutra
Book of Proverb
6
7
8
Book of Ecclesiasticus
Book of Ecclesiastes
Book of Wisdom
From this heat map, we can say that there is a distance between the Quran and the other sacred books whereas
there is a similarity between the book 6 corresponding to book of book of ecclesiastes with the book 3 corre-
sponding to Tao Te Ching.
• Cosine distance
Figure 7: Heatmap of the cosine distance between the sacred books.
Here, the heat map shows that, still, there is a distance between the Quran and some of the other sacred books. We
realize that, some of the Asian books (like Buddhism and YogaSutra) are not similar to the Bible.
3.6. Correlation between the distance measures
In this section of our work, we will check if the diﬀerent distance measures are based on the same properties. To
do this, we will compute the correlation between the distance measures applied before.
Figure 8: Correlation matrix between the values obtained from the diﬀerent distance measures
YOUNOUS MOFENJOU PEURIEKEU et al.: Preprint submitted to Elsevier
Page 17 of 20

--- Page 18 ---

Comprehensive Text Mining on Various Sacred Scriptures
3.7. Classiﬁcation of the fragment of sacred text
Here, we used four diﬀerent model to do the prediction. We have, K-Nearest Neighbors (KNN), Super vector
Machine (SVM), Random Forest (RF) and multinomial naive bayes. Grid-search is used to ﬁnd the optimal hyper-
parameters of a model which give the higher accuracy. We used m = 10 folds in this work.
Thus, we ﬁnd the accuracy for the RF equal to 0.7370, for the Super Vector Machine SVM classiﬁer is 0.7781, for
the KNN ﬁnd 0.6128 and 0.8584 for the Multinomial Naive Bayes classiﬁer
Figure 9: The confusion matrix of the Random Forest and Super Vector Machine
Figure 10: The confusion matrix of the K-Nearest Neighbors and Multinomial Naive Bayes
YOUNOUS MOFENJOU PEURIEKEU et al.: Preprint submitted to Elsevier
Page 18 of 20

--- Page 19 ---

Comprehensive Text Mining on Various Sacred Scriptures
4. Discussion
When we carried out the natural language processing using the NLTK Library, we focused on three things that are
essential in text mining: We applied pre-processing steps as well as the Part-Of-Speech tagging to obtain appropriate
text data for the analysis. Finally, we worked out the document term matrix representation of the text data with respect
to several distance measures.
Looking at ﬁgure 6, the Euclidean measure tells us that the distance between the Quran and other sacred books
seems to be high. The Asian books are almost similar to the sacred books from Bible. But looking at ﬁgure 7, we
notice that, the distance between the Quran and some sacred books is not very high. The books from the Bible and
Asian religions are almost similar. This leads us to wonder why the distance measure methods do not give us the same
result. This is the reason why it is interesting to check the correlation between these approaches.
When we look at ﬁgure 8, the Euclidean distance and Manhattan distance are strongly correlated while we do not
observe a high correlation with the Jaccard and Cosine distance. Based on this result, we conclude that, not all of these
methods use the same properties to determine the distance between documents.
To analyze whether the high similarities between documents obtained with respect to the diﬀerent measures are
related to similar meanings among these documents, we consider exemplifying the following fragments:
1- Tao Te Ching :
Not to value and employ men of superior ability is the way to keep the people from rivalry
among themselves; not to prize articles which are diﬃcult to procure is the way to keep them from becoming thieves;
not to show them what is likely to excite their desires is the way to keep their minds from disorder. Therefore the
sage, in the exercise of his government, empties their minds, ﬁlls their bellies, weakens their wills, and strengthens
their bones. He constantly (tries to) keep them without knowledge and without desire, and where there are those who
have knowledge, to keep them from presuming to act (on it). When there is this abstinence from action, good order is
universal.
2- Book of Wisdom :
- the works of the hands of men. 13:1. But all men are vain, in whom there is not the
knowledge of God: and who by these good things that are seen, could not understand him that is, neither by attending
to the works have acknowledged who was the workman: 13:2. But have imagined either the ﬁre, or the wind, or the
swift air, or the circle of the stars, or the great water, or the sun and moon, to be the gods that rule the world. 13:3.
3- Tao Te Ching :
- The skilful traveller leaves no traces of his wheels or footsteps; the skilful speaker says
nothing that can be found fault with or blamed; the skilful reckoner uses no tallies; the skilful closer needs no bolts or
bars, while to open what he has shut will be impossible; the skilful binder uses no strings or knots, while to unloose
what he has bound will be impossible. In the same way the sage is always skilful at saving men, and so he does not cast
away any man; he is always skilful at saving things, and so he does not cast away anything. This is called ’Hiding the
light of his procedure.’Therefore the man of skill is a master (to be looked up to) by him who has not the skill; and he
who has not the skill is the helper of (the reputation of) him who has the skill. If the one did not honour his master, and
the other did not rejoice in his helper, an (observer), though intelligent, might greatly err about them. This is called
’The utmost degree of mystery.’
4-UgaSutra:
- The disciple said: I do not think I know It well, nor do I think that I do not know It. He among
us who knows It truly, knows (what is meant by) "I know" and also what is meant by "I know It not." This appears
to be contradictory, but it is not. In the previous chapter we learned that Brahman is "distinct from the known" and
"beyond the unknown." The disciple, realizing this, says: "So far as mortal conception is concerned, I do not think I
know, because I understand that It is beyond mind and speech; yet from the higher point of view, I cannot say that I do
not know; for the very fact that I exist, that I can seek It, shows that I know; for It is the source of my being.
Philosophically speaking, all the documents show diﬀerences with respect to the content they present. The ﬁrst
document deals with the duties of a government to create a society with peace. The second one is about the existence of
God and about the belief in God. The third document deals with interactions among individuals and describes virtue.
The last fragment is an abstract discussion about what knowledge is and can be classiﬁed as an epistemological text.
Despite the fact that we obtain similarities with respect to the Euclidean and Manhattan measure, we see that
regarding the content of these documents, there is not a large overlapping. This prompts us to claim that these two
methods are not focused on the meaning of the documents. Also, using the Jaccard and Cosine approaches, we obtain
high similarities which leads us to the hypothesis that these measures also do not focus on the semantics. Thus, we
claim that the similarities are mostly based on the syntactical structures of the documents.
Regarding the classiﬁcation, our ﬁndings reveal that the Multinomial Naive Bayes model yields the best prediction
performance depicted in ﬁgures 9 and 10. The Quran and Bible have the largest number of chapters in the corpus,
YOUNOUS MOFENJOU PEURIEKEU et al.: Preprint submitted to Elsevier
Page 19 of 20

--- Page 20 ---

Comprehensive Text Mining on Various Sacred Scriptures
and the Multinomial Naive Bayes is able to predict most of them with a very high accuracy, which is around 0.8584.
Random Forest (RF) follows with 0.737 of accuracy. K-nearest-neighbors (KNN), and Super Vector Machine (SVM)
fails to distinguish the majority of chapters from the Asian sacred books.
Future research: As future work, the plan is to extend the set of our corpus by taking into consideration many
other religions around the world, and therefore, more books. It could be for instance:
• Inclusion of more books from Asian and Christian religions;
• Inclusion of the African tradition Scriptures and also the consideration of religions that are now obsolete. It will
be very interesting to go deep into this study by exploring all the diﬀerent properties that the distance measures
use to analyze the meaning or semantic aspect of the sacred scriptures.
In addition to that, since the focus of this study has been more on the lexical analysis, a further approach could include
semantic. Given, for instance, the intrinsic dependence between words in raw texts, a much more informative feature
engineering could be done before hand. That could include deriving from the bag of words, group of words/tokens
as features instead of single tokens. Subsequently, deep learning approaches including Long Short-Term Memory
(LSTM), and Convolution Recurrent Neural Network (CRNN) could be used to ﬁt the data and extract, for instance,
the contexts inside chapters of the books, categorize them, and run a contextual comparison analysis between (chapter
of) diﬀerent books. These models could also be used after eﬀective training for completion of some of the sentences
in the actual religious books.
References
Deza, M.M., Deza, E., 2006. Dictionary of distances. Elsevier.
Elton, D.C., Turakhia, D., Reddy, N., Boukouvalas, Z., Fuge, M.D., Doherty, R.M., Chung, P.W., 2019. Using natural language processing techniques
to extract information on the properties and functionalities of energetic materials from large text corpora. arXiv preprint arXiv:1903.00415 .
Evison, J., 2013. A corpus linguistic analysis of turn-openings in spoken academic discourse: Understanding discursive specialisation. English
Proﬁle Journal 3.
Ezzeldin, M., El-Dakhakhni, W., 2020. Metaresearching structural engineering using text mining: Trend identiﬁcations and knowledge gap discov-
eries. Journal of Structural Engineering 146, 04020061.
Hobbs, J.R., Walker, D.E., Amsler, R.A., 1982. Natural language access to structured text, in: Proceedings of the 9th conference on Computational
linguistics-Volume 1, Academia Praha. pp. 127–132.
Ignatow, G., Mihalcea, R., 2017. An introduction to text mining: Research design, data collection, and analysis. Sage Publications.
Laxman, B., Sujatha, D., 2013. Improved method for pattern discovery in text mining. International Journal of Research in Engineering and
Technology 2, 2321–2328.
Levenberg, A., Pulman, S., Moilanen, K., Simpson, E., Roberts, S., 2014. Predicting economic indicators from web text using sentiment composition.
International Journal of Computer and Communication Engineering 3, 109–115.
Maher, K., Joshi, M.S., 2016. Eﬀectiveness of diﬀerent similarity measures for text classiﬁcation and clustering. International Journal of Computer
Science and Information Technologies 7, 1715–1720.
Manning, C.D., Manning, C.D., Schütze, H., 1999. Foundations of statistical natural language processing. MIT press.
McDonald, D., 2014. A text mining analysis of religious texts. The Journal of Business Inquiry 13, 27–47.
Nisbet, R., Elder, J., Miner, G., 2009. Handbook of statistical analysis and data mining applications. Academic Press.
Qahl, S.H.M., 2014. An automatic similarity detection engine between sacred texts using text mining and similarity measures .
SAH, P., FOKOUÉ, E., 2019. What do asian and non-asian scriptures have in common? an applied statistical machine learning inquiry. Math. Appl
8, 151–171.
Sah, P., Fokoué, E., 2019. What do asian religions have in common? an unsupervised text analytics exploration. arXiv preprint arXiv:1912.10847 .
Sindler, F.L., 2011. Comparative Study of Christian, Jewish, and Islamic Theodicy. Ph.D. thesis. Reformed Theological Seminary, Virtual Campus.
Sklad, M., Diekstra, R., Ritter, M.d., Ben, J., Gravesteijn, C., 2012. Eﬀectiveness of school-based universal social, emotional, and behavioral
programs: Do they enhance students’ development in the area of skill, behavior, and adjustment? Psychology in the Schools 49, 892–909.
Wang, L., 2005. Support vector machines: theory and applications. volume 177. Springer Science & Business Media.
Zahrotun, L., 2016. Comparison jaccard similarity, cosine similarity and combined both of the data clustering with shared nearest neighbor method.
Computer Engineering and Applications Journal 5, 11–18.
YOUNOUS MOFENJOU PEURIEKEU et al.: Preprint submitted to Elsevier
Page 20 of 20
