---
title: "2024-Khaksar-Shifting from Endangerment to Rebirth in the Artificial Intelligence - PDF Extract"
source_pdf: "2024-Khaksar-Shifting from Endangerment to Rebirth in the Artificial Intelligence.pdf"
pages: 19
extracted_at: "2026-02-13T17:43:17.743427"
---

# PDF Extract: 2024-Khaksar-Shifting from Endangerment to Rebirth in the Artificial Intelligence

**Source PDF:** 2024-Khaksar-Shifting from Endangerment to Rebirth in the Artificial Intelligence.pdf
**Total Pages:** 19

---

## Content

```
--- Page 1 ---

Shifting from endangerment to rebirth in the Artificial
Intelligence Age: An Ensemble Machine Learning Approach
for Hawrami Text Classification
ARAM KHAKSAR and HOSSEIN HASSANI, University of Kurdistan Hewlêr, Iraq
Hawrami, a dialect of Kurdish, is classified as an endangered language as it suffers from the scarcity of
data and the gradual loss of its speakers. Natural Language Processing projects can be used to partially
compensate for data availability for endangered languages/dialects through a variety of approaches, such
as machine translation, language model building, and corpora development. Similarly, NLP projects such as
text classification are in language documentation. Several text classification studies have been conducted for
Kurdish, but they were mainly dedicated to two particular dialects: Sorani (Central Kurdish) and Kurmanji
(Northern Kurdish). In this paper, we introduce various text classification models using a dataset of 6,854
articles in Hawrami labeled into 15 categories by two native speakers. We use K-nearest Neighbor (KNN),
Linear Support Vector Machine (Linear SVM), Logistic Regression (LR), and Decision Tree (DT) to evaluate
how well those methods perform the classification task. The results indicate that the Linear SVM achieves a
96% of accuracy and outperforms the other approaches.
1, 1 (September 2024), 19 pages.
1
Introduction
Language is a medium that connects individuals [34]. The extinction of a language leads to an
impairment in social cohesion while also cleansing the culture and identity of its speakers. Docu-
mentation and digitization through data collection are essential in language preservation [17]. They
also contribute to preserving the culture of the speakers of that language [6]. Natural Language
Processing (NLP) can be employed because it assists in data collection and language modeling that
can help computational work on the language, hence its digital presence [10, 47].
The Kurdish language consists of four dialects [35], each owning unique scripts [9, 21]. This
diversity of dialects in Kurdish introduced many challenges to NLP projects [30, 45]. Additionally,
the speakers of each dialect encounter challenges in understanding one another. Therefore, Kurdish
dialects are considered mutually unintelligible [24, 37]. Attempts to reach a consensus among
all scholars about its dialect classification have failed so far [28]. For example, different claims
identify Hawrami as an independent language. MacKenzie [29] explained that while Hawrami’s
phonetic system is similar to the rest of the Kurdish dialects, Hawrami is an independent language.
In contrast, other scholars identify Hawrami as one of the Kurdish dialects since it shares common
linguistic traits with the other Kurdish dialects [5]. In this research, we adhere to the view of a
group of Kurdish scholars who classify Hawrami as a Kurdish dialect.
Kurdish as a whole is listed as a low-resourced language [3, 15, 20], and Hawrami is classified
as ‘’definitely endangered’‘ by UNESCO [33]. Languages without computational support are also
deemed endangered as they suffer from additional challenges in NLP and Computational Linguistics
projects due to different factors, such as data scarcity, lack of standard orthography, and absence of
NLP expertise familiar with them [10]. Sorani and Kurmanji, the two most widely spoken dialects
in Kurdish, hold a dominant position in NLP projects for Kurdish, while Hawrami has received a
much lesser attention from scholars [12, 32].
arXiv:2409.16884v1  [cs.CL]  25 Sep 2024

--- Page 2 ---

2
Through a text classification project, we aim to collect Hawrami texts from various resources (the
dataset is partially publicly available for non-commercial use under the CC BY-NC-SA 4.0 license 5
at https://github.com/KurdishBLARK/HawramiClassification). Like other projects in Kurdish pro-
cessing, ours also faces some well-known challenges, such as the absence of standard orthography
[4, 23], lack of a universally recognized standard alphabet [18, 46], and lack of standardization of
the language [9, 20].
The rest of this paper is organized as follows. Section two provides an overview of the Hawrami
dialect. Section three reflects on the related work through a literature review. Section four presents
the methodology of the research. Section five illustrates the results and discusses the outcomes.
Finally, section 5 concludes the paper.
2
An overview of Hawrami Dialect
Hawrami is spoken by the people of Hawraman, a place that traverses the border of Iran and Iraq
[41]. There are still no credible statistics to show the accurate number of Hawrami speakers. Table
1 shows various sources that provide different figures of the Hawrami population.
Table 1. Estimated number of Hawrami speakers
Source
Number of Speakers
UNESCO [33]
23,000
Paul [37]
∼44,000
Holmberg and Odden [25]
<100,000
Ethnologue [16]
10,000-1000,000
While some well-known literary works in Kurdish are written in Hawrami, through which the
dialect had a significant contribution to the Kurdish literature [34], UNESCO listed it as ‘’definitely
endangered’‘[33] because it seems it is gradually losing speakers and its online resources are not
growing as expected. For example, currently, Wikipedia has no Hawrami article [22]. Neamat [36]
faced challenges in their research due to the lack of resources to work on Hawrami morphemes.
Arslan [11] shows concerns about Hawrami preservation.
Similarly important, the classification of Hawrami is an ongoing debate among scholars. To
separate dialects from languages, social and political factors must be considered [21]. Mustafa [34]
explained that the phonetics, grammar, and dictionary of all Kurdish dialects are nearly similar,
and the speakers of each dialect identify themselves as Kurds. Although MacKenzie [29] showed
Hawrami’s phonetic system is close to the rest of the Kurdish dialects, introduced it as a separate
language from Kurdish. On the other hand, Haig [19] demonstrated that all Kurdish dialects share
the same vowels and consonants but have different phonetics. Additionally, Ahmadi [5] stated that
Hawrami has common linguistic traits with other Kurdish dialects. Also, Kurdish is a phonemic
language [9], and its orthography highly relies on this factor.
However, Kurdish still lacks a standard orthography [12]. Various attempts towards standardiza-
tion have not yet produced an outcome all parties, or at least a majority, have agreed upon. For
example, while Ahmadi et al. [6] suggested a unified script for all dialects of Kurdish, it cannot
fully cover Hawrami as it lacks some phonetics that appear only in Hawrami. To address that, we
introduce the Hawrami alphabets suggested by [31], as shown in Figure 1. We used this suggestion
in the preparation of our dataset.

--- Page 3 ---

3
Fig. 1. On the left: the proposed unified script Kurdish by Ahmadi et al. [6]. On the right: A unified script for
Hawrami is suggested by Marani [31].

--- Page 4 ---

4
3
Related Work
Text classification automatically categorizes texts into different classes based on the information
they contain. Text classification is a supervised machine-learning task that manually labels the
text entries [26, 27]. To find the best methods for Hawrami text classification, we found articles
that provided different techniques. Accordingly, most reviews relate to research on endangered
languages, as they provide reusable tools applicable to other low-resource languages.
Table 2. A summary of literature review.
Reference
Task
Entries
Best method(s)
Accuracy
Language
[43]
Fake News Detection
100,962
CNN
91.6%
Kurdish (Sorani)
[38]
Text Classification
60,000
BERT
94.48%
Chinese
[3]
Sentiment Analysis
15,000
Naïve Bayes
66%
Kurdish (Sorani)
[23]
Text Classification
7,000
SVM
92%
Kurdish (Sorani & Kurmanji)
[7]
Text Classification
5,003
SMFCNN
95.4%
Urdu
[13]
Fake News Detection
5,000
SVM
88.71%
Kurdish (Sorani)
[42]
Text Classification
4,007
SVM
92.4%
Kurdish (Sorani)
[39]
Text Classification
4,007
SVM
91.03%
Kurdish (Sorani)
[40]
Text Classification
2,000
Naïve Bayes
94.55%
Kurdish (Sorani)
[44]
Sentiment Analysis
511
SVM & Logistic Regression
90%
Kurdish (Sorani)
[8]
Text Classification
500
Linear SVM
97%
Indonesian
[14]
Sentiment Analysis
480
BERT
97%
Greek
NLP tasks can achieve excellent results if sufficient data is collected [21]. In the previous text
classification papers reviewed here, collecting data for low-resourced languages was regarded as a
challenge and time-consuming.
In summary, our review found that the pipeline of a text classification project should follow: data
collection, labeling, preprocessing, splitting, feature extraction, training, and testing. Furthermore,
The TF-IDF method has proven to be compatible with text classification projects. Finally, using
ensemble machine-learning techniques yields better results.
4
Methodology
This chapter provides the processes for text classification for Hawrami, starting from collecting
data, labeling, preprocessing, splitting, balancing, extracting features, classification, and testing
and evaluation. The process diagram is shown in Figure 2.
4.1
Data Collection
We employ two techniques in this project. The first approach is web scraping using the Scrapy
package from Python to undertake the task. Due to Scrapy’s default behavior of sending concurrent
requests to the server, a process yields null data when the server is unable to respond to all
the requests promptly, which results in missing data in the dataset. Scrapy also does not render
dynamically handled pages. Therefore, we use Robotic Process Automation (RPA), one of the
techniques used to automatically repeat human activity on browsers by creating bots to do the task
with the help of the Selenium library in Python.
4.2
Labeling
In this stage, we provide a labeled dataset to two Hawrami speakers to review and make necessary
changes. Concerning the richness of the data, there are no limitations on the number of classes.
We employ various techniques to handle the classes with the fewest text entries. To measure this

--- Page 5 ---

5
Fig. 2. The proposed pipeline for text classification.
agreement rate, we apply Cohen’s kappa, as shown in Formula 1.
𝑘= 𝑝◦−𝑝𝑒
1 −𝑝𝑒
(1)
4.3
Preprocessing
Preprocessing is considered a crucial stage of NLP projects, in which we undertake various tasks to
produce clean data for further processing in the following stage of text classification. In this stage,
we accomplish the normalization task.
Normalization is the process of removing useless information from texts. Generally, the number
of words in each entry differs from others, which later generates biased features. To solve this issue,
we find the interquartile range for the number of words to determine outliers and calculate the 25th
(first quartile) and 75th (third quartile) percentiles to specify the minimum and maximum words
for each entry. For entries with a text length greater than the third quartile, we utilize the capping
technique to reduce words. However, this technique produces entries with a text length below
the first quartile. Therefore, we concatenate the new text entries that fall in the same category.
Concatenating multiple articles with different topics from the same category does not compromise
the quality of the classification model but does increase the accuracy and mitigate bias. Before
capping and concatenation operations, we undertake the following tasks:
• Removing break lines, @bloggers, multiple spaces, hashtags, email addresses, punctuation
marks, symbols, URLs, and numbers.
• Removing duplicated entries.
• Removing null entries.
• Removing Zero-width non-joiners.

--- Page 6 ---

6
• Removing non-Kurdish scripts.
• Removing stop-words.
• Removing words with less than two and more than fourteen characters.
4.4
Splitting
A text classification model should identify variables capable of predicting the target variables or
features and classify any text based on them. To ensure an equal distribution of entries across all
classes, we split our data according to the overall distribution of the target variables. Therefore,
we apply the stratified sampling technique to split the dataset into training and testing sets. This
technique works well where the percentage difference between the number of entries in the major
class and the mean is small. Otherwise, we apply balancing techniques to avoid reducing major
classes while employing. Considering the quality of the model, we take two approaches. First,
allocating only 70% for training and the remaining 30% for testing. In the second approach, 90%
will be taken for training and 10% for testing.
4.5
Balancing
Kurdish is regarded as a low-resource language. Hence, the dataset size for Hawrami is expected to
be small; the data cannot be found equally for each class. Accordingly, we calculate the percentage
difference to identify the degree of imbalance. There are several techniques for balancing, including
under-sampling, over-sampling, and the synthetic minority oversampling technique (SMOTE).
Under-sampling trims the entries of major classes, in which data will be lost. The second technique,
over-sampling, targets minor class entries and duplicates them to match the major classes. The
over-sampling technique introduces a drawback as it duplicates the entire text, including useless
information, and it is prone to over-fitting due to the duplication of entries. In this paper, first, we
use the under-sampling technique to reduce the number of major classes and lower the percentage
difference. Finally, we apply the SMOTE balancing technique to generate synthetic data by targeting
features, selecting them according to the nearest neighbor from the text of minor classes, and
leveraging the TF-IDF to extract those features. The balancing techniques are applied only to the
training set since any resampling from the training set generates the wrong cross-validation.
4.6
Feature Extraction
Before feeding the texts to be trained, a feature extraction process is required to generate new sets
of features from the data. For this purpose, we use Term Frequency Inverse Document Frequency
(TF-IDF) to weigh each term that appears in the dataset. TF-IDF is a statistical measurement to
determine the significance of a term in the entire dataset. According to the Formula 2, TF calculates
the frequency of a word in a single entry, and as shown in the Formula 3, DF calculates the number
of articles that contain that single word. To evaluate how relevant a word is to an article, we apply
the Formula 4, in which N is the total number of articles. Finally, from the Formula 5, we find the
weight of each word. This weight of terms indicates that the frequently appearing words are less
significant. In a small dataset, we expect a small number of features, unless the vocabulary size of
the collected data is large for each text entry. Considering previous facts, we identify single words
as features by setting the N-gram constant to one. Additionally, all the features found in the data
are used. In brief, TF-IDF reduces the high dimensionality of the data and avoids over-fitting.
𝑇𝐹𝑖𝑗= 𝑐𝑜𝑢𝑛𝑡𝑜𝑓𝑖𝑖𝑛𝑗
𝑡𝑒𝑥𝑡𝑙𝑒𝑛𝑔𝑡ℎ𝑜𝑓𝑗
(2)
𝐷𝐹𝑖= 𝑡𝑜𝑡𝑎𝑙𝑛𝑢𝑚𝑏𝑒𝑟𝑜𝑓𝑒𝑛𝑡𝑟𝑖𝑒𝑠𝑐𝑜𝑛𝑡𝑎𝑖𝑛𝑖𝑛𝑔𝑖
(3)

--- Page 7 ---

7
𝐼𝐷𝐹= 𝑙𝑜𝑔1 + 𝑁
1 + 𝐷𝐹𝑖
(4)
𝑇𝐹−𝐼𝐷𝐹𝑖𝑗= 𝑇𝐹𝑖𝑗∗𝐼𝐷𝐹
(5)
4.7
Classification
In this stage, we consider several factors according to our dataset to choose compatible classification
algorithms. In a machine-learning project, the size of the dataset determines the pipeline. To avoid
over-fitting, we employ simpler algorithms for smaller datasets. We train the classification model
using four algorithms. The classifiers are K-Nearest Neighbor (KNN), Linear Support Vector Machine
(Linear SVM), Logistic Regression (LR), and Decision Tree (DT). We build the classification models
based on four scenarios:
(1) On the imbalanced dataset with a stratified split of 90% for training and 10% for testing.
(2) On the imbalanced dataset with a stratified split of 70% for training and 30% for testing.
(3) On the balanced dataset with a stratified split of 90% for training and 10% for testing.
(4) On the balanced dataset with a stratified split of 70% for training and 30% for testing.
4.7.1
K-Nearest Neighbor. KNN is a simple yet effective supervised machine-learning algorithm
for classification problems. This non-parametric algorithm is known as a lazy learner because it
stores the training data for the classification and makes no assumptions about it. Known by its
name, KNN is highly dependent on the value of K, which defines the number of nearest neighbors.
We set different values for K to achieve the highest accuracy.
4.7.2
Linear Support Vector Machine. SVM is an effective supervised machine-learning algorithm
employed in classification projects. This algorithm finds the hyperplanes that divide data points
into different classes according to the number of features. This is achieved by determining the
support vectors, the data points closest to the hyperplane. A larger distance range between the
support vector and the hyperplane may improve classification; this distance is known as the margin
and is measured to determine the maximum distance. In this project, we employ the linear support
vector machine to divide the data points linearly.
4.7.3
Logistic Regression. Logistic regression is a probabilistic supervised machine-learning algo-
rithm mostly used in classification projects. This algorithm applies the sigmoid (logistic) activation
function, shown in Formula 6, to find the probability that a feature belongs to a class. The logistic
function expects the linear combination of a set of linearly separated features to be transformed
into a probability score.
𝜎(𝑥) =
1
1 + 𝑒𝑥
(6)
4.7.4
Decision Tree. A decision tree is a supervised machine-learning algorithm that consists of
three main nodes: the root node, the leaf node, and the decision node. The algorithm follows a
conditional approach with the help of some measures such as entropy and information gain to
perform multiple tests. The process continues until it reaches a leaf node, which indicates the final
classification.
4.8
Testing and Evaluation
We test all models on the testing set to measure the performance of each classifier using various
metrics (Formulas 7, 8, 9, 10, 10, and 12).
(1) Accuracy: To calculate the proportion of correct predictions.
𝑎𝑐𝑐𝑢𝑟𝑎𝑐𝑦= 𝑐𝑜𝑟𝑟𝑒𝑐𝑡𝑝𝑟𝑒𝑑𝑖𝑐𝑡𝑖𝑜𝑛𝑠
𝑎𝑙𝑙𝑝𝑟𝑒𝑑𝑖𝑐𝑡𝑖𝑜𝑛𝑠
=
𝑇𝑃+𝑇𝑁
𝑇𝑃+𝑇𝑁+ 𝐹𝑃+ 𝐹𝑁
(7)

--- Page 8 ---

8
TP: True Positive
TN: True Negative
FP: False Positive
FN: False Negative
(2) Precision: To calculate the proportion of positive predictions that are actually correct.
𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛=
𝑇𝑃
𝑇𝑃+ 𝐹𝑃
(8)
(3) Recall: To calculate the proportion of actual positive instances that are correctly identified.
𝑟𝑒𝑐𝑎𝑙𝑙=
𝑇𝑃
𝑇𝑃+ 𝐹𝑁
(9)
(4) F1-score: Combines precision and recall to provide a better understanding of the model’s
performance for imbalanced datasets.
𝐹1 = 2 · 𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛· 𝑟𝑒𝑐𝑎𝑙𝑙
𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+ 𝑟𝑒𝑐𝑎𝑙𝑙
(10)
(5) F1 macro average: To calculate the model’s performance equally for each class.
𝐹1𝑚𝑎𝑐𝑟𝑜𝑎𝑣𝑒𝑟𝑎𝑔𝑒= 𝑠𝑢𝑚𝑜𝑓𝐹1 𝑠𝑐𝑜𝑟𝑒𝑜𝑓𝑎𝑙𝑙𝑐𝑙𝑎𝑠𝑠𝑒𝑠
𝑡𝑜𝑡𝑎𝑙𝑛𝑢𝑚𝑏𝑒𝑟𝑜𝑓𝑐𝑙𝑎𝑠𝑠𝑒𝑠
= 1
𝐶·
𝐶
∑︁
𝑖=1
𝐹1𝑖
(11)
(6) Hamming loss: To calculate the proportion of mismatched labels between the actual and
predicted labels.
ℎ𝑎𝑚𝑚𝑖𝑛𝑔𝑙𝑜𝑠𝑠= 𝑛𝑢𝑚𝑏𝑒𝑟𝑜𝑓𝑚𝑖𝑠𝑚𝑎𝑡𝑐ℎ𝑒𝑑𝑙𝑎𝑏𝑒𝑙𝑠
𝑡𝑜𝑡𝑎𝑙𝑛𝑢𝑚𝑏𝑒𝑟𝑜𝑓𝑙𝑎𝑏𝑒𝑙𝑠
= 1
𝑀·
𝑀
∑︁
𝑖=1
𝑑𝑖
(12)
5
Results
5.1
Dataset
In the first stage of the experiment, we collected data from two online sources: Firat News (ANF)
[1] and Kurdipedia [2]. As shown in Table 3, we used the Scrapy framework to crawl data from the
ANF website. We discovered that the dataset included empty entries and later identified the missing
data type as Missing Completely at Random (MNAR). This occurred because the framework sent
multiple requests per second to the server, and the website failed to respond instantly, resulting
in missing data. The same scenarios occurred for Kurdipedia after using an alternate approach
because their website is dynamic and Scrapy cannot render their pages. Therefore, we created a
bot with the Selenium library to extract relevant texts.
Table 3. The data amount collected from both sources.
Source
Technique
Collected
Missing
Duplicated
Deleted
After Deletion
ANF
Web Scraping (Scrapy)
5,317
44
3
1,095
4,222
Kurdipedia
RPA (Selenium)
4,128
496
585
1,496
2,632
Total
9,445
61
68
2,591
6,854
As shown in Figure 3, 27.4% of the data was removed, including missing data, duplicated data,
non-textual data, non-Kurdish text, irrelevant content, social media content, and biased data. Finally,

--- Page 9 ---

9
Table 4. Data summary by category.
Politics
Literature
History
Language
Biography
Event
Women’s Right
Natural Disaster
Religion
Health
Economy
Sport
Music
Cinema
Painting
Entries
3,749
2,051
276
218
123
111
98
78
48
43
22
18
13
5
1
Percent
54.69
29.92
4.02
3.18
1.79
1.61
1.42
1.13
0.70
0.62
0.32
0.26
0.18
0.07
0.01
Minimum words
9
9
39
5
24
32
52
23
58
73
58
47
41
84
275
Maximum words
5,112
5,384
1,972
3,992
4,700
1,435
3,178
688
1,088
1,067
393
406
1,218
226
275
Average words
343.29
236.14
248.52
684.14
285.5
253.15
471.59
139.74
204.93
370.3
138.40
106.8
354.53
165.8
275
Total words
1,287,016
484,336
68,593
149,143
35,118
28,100
46,216
10,900
9,837
15,923
3,045
1,923
4,609
829
275
Total unique words
191,543
90,214
23,509
44,984
14,659
13,326
17,693
4,697
4,999
7,526
1,588
1,167
2,271
581
189
First quartile (words)
100
90
134
288.25
145
126
151.25
80
100.25
187
66.5
65.75
168
110
275
Third quartile (words)
341
270
319.5
780.75
303.5
304.5
555.75
172
202.75
440
156.75
123.75
334
226
275
a dataset of 6,854 articles was created, with 65.6% of the collected data coming from ANF and the
remaining 34.4% from Kurdipedia.
Fig. 3. Total data reduction for both sources.
5.2
Labeled Data
We prepared a labeled dataset to simplify the process for the annotators while reviewing and
changing the labels as necessary. Furthermore, no limits on the number of classes were set to
prevent data loss. The agreement rate found among the annotators was 93.9%. After reviewing the
dataset, we decided to use the first labeled dataset. Table 4 provides an overview of all categories in
the dataset.
As shown in Figure 4, the dataset is highly biased towards the politics and literature categories,
and the percentage difference is 156.92% between the total number of political articles and the
mean of the total number of articles, resulting in an imbalanced dataset.

--- Page 10 ---

10
Fig. 4. Distribution of data collected (percentage) across categories.
5.3
Preprocessed Data
In the first step, we cleaned the texts of unnecessary information, including break lines, @bloggers,
multiple spaces, hashtags, email addresses, punctuation marks, symbols, URLs, and numbers. We
found that the dataset included 346 unique characters that needed to be reduced to the number
of Hawrami alphabets, excluding Perian-Arabic characters. To complete this stage, we created a
dataset of all the unique characters found and assigned replacement characters or marked null. We
deliberately excluded the Persian-Arabic characters, as we defined a regex particular to Hawrami
to remove non-Kurdish texts. We finally reduced the number of characters to 50, and all the wrong
characters were corrected according to the suggested alphabet.
A dataset of 521 Hawrami stopwords was created and used to eliminate useless words in the
dataset. Furthermore, we removed double characters words. We discovered that in some of the
text entries, there are meaningless texts formed from the concatenation of two or more words. To
remove these texts, a method was defined to eliminate any word exceeding 14 characters. Finally,
we defined a regular expression of Hawrami alphabets to identify non-Hawrami texts, which were
eliminated, leaving 41 unique characters.
As shown in Figure 5, we observed that the number of words in each article varied and discovered
a positive-skewed distribution. We also calculated the value of skewness, which was 5.34. Moreover,
Figure 6 explicitly depicts the range of text length of entries by category in the entire dataset.
After calculating the interquartile range, which ranged from 54 to 179 words, we detected 3,325
articles with text lengths outside this range. Therefore, we employed the capping technique to
shorten the length of articles that exceeded the range. This approach produced articles with total
words smaller than the first quartile. To solve this problem, we concatenated them based on their
categories. As a result, the skewness ratio has fallen from 5.34 to -0.38. As shown in Figure 7, a
normal distribution for the number of words of all articles was achieved. These operations increased
the number of entries from 6,854 to 8,056 as shown in Figure 8.
In the final step, we removed articles from categories that comprise less than 1% of the entire
dataset, leaving only 7 categories as shown in Table 5 and the percentage difference reduced to
125.66%. As depicted in Figure 9, the preprocessing operations highly affected the dataset size,
particularly for the politics category, by increasing the number of entries. Consequently, removing
irrelevant words decreased the average number of words mostly of language category.

--- Page 11 ---

11
Fig. 5. The overall distribution of the number of words for all entries.
Fig. 6. The range of the number of words by category.
Table 5. The final dataset after the preprocessing stage.
Politics
Literature
Language
History
Women’s Right
Biography
Event
Entries
5,011
1,947
406
290
163
120
119
Percent
61.2
24.16
5.03
3.59
2.02
1.49
1.47
Minimum words
54
54
54
54
54
57
55
Maximum words
179
179
179
179
179
179
179
Average words
138.57
121.06
154.62
117.16
146.79
123.65
128.66
Total words
694,351
235,707
62,776
33,975
23,927
14,838
15,311
Number of unique words
103,168
87,739
21,489
13,845
11,299
7,808
7,879
First quartile (words)
93
77
136
80
112.5
83
93.5
Third quartile (words)
179
179
179
168
179
179
176

--- Page 12 ---

12
Fig. 7. The range of the number of words by category after capping.
Fig. 8. The dataset size after the preprocessing stage.
5.4
Classification Models
For 90% of the training data, the TF-IDF vectorizer extracted 193,381 features and 162,546 from
the 70% training set. We applied two techniques to balance the dataset for the third and fourth
scenarios. Initially, we selected only half of the political articles, comprising 31.1% of the data,

--- Page 13 ---

13
Fig. 9. The difference in total entries and average words for each category after the preprocessing stage.
remaining with 5,551 entries. Subsequently, we applied SMOTE to the training set, resulting in an
equal number of articles for all the categories. Table 6 depicts the testing results for the classifiers
across four scenarios. In Figure 10, the change in the accuracy of models is determined for different
scenarios. Figure 11 depicts the F1 macro average change of the models found in all scenarios.
Table 6. The classifiers’ performance across all scenarios.
Scenario
Algorithm
Accuracy
Precision
Recall
F1-score
F1 macro average
Hamming loss
Training time (s)
K-Nearest Neighbor
0.94
0.93
0.94
0.93
0.71
0.06
2.52
1
Linear SVM
0.96
0.96
0.96
0.95
0.79
0.04
5.51
Logistic Regression
0.93
0.94
0.93
0.93
0.77
0.06
60.56
Decision Tree
0.89
0.90
0.89
0.90
0.66
0.1
14.11
K-Nearest Neighbor
0.94
0.94
0.94
0.94
0.73
0.05
1.51
2
Linear SVM
0.96
0.95
0.96
0.95
0.79
0.04
2.8
Logistic Regression
0.94
0.94
0.94
0.94
0.77
0.06
32.82
Decision Tree
0.87
0.88
0.87
0.87
0.60
0.13
10.9
K-Nearest Neighbor
0.52
0.88
0.52
0.52
0.48
0.48
1.4
3
Linear SVM
0.94
0.93
0.94
0.93
0.80
0.06
17.76
Logistic Regression
0.92
0.92
0.92
0.92
0.78
0.08
60.83
Decision Tree
0.85
0.84
0.85
0.84
0.58
0.15
25.68
K-Nearest Neighbor
0.49
0.90
0.49
0.51
0.47
0.5
0.09
4
Linear SVM
0.94
0.94
0.94
0.94
0.81
0.06
7.4
Logistic Regression
0.93
0.93
0.93
0.93
0.79
0.07
35.6
Decision Tree
0.82
0.83
0.82
0.82
0.59
0.18
16.2
6
Discussion
We employed ensemble machine-learning algorithms to build multiple text classification models
for Hawrami. Accordingly, we used four algorithms, including K-Nearest Neighbor, Linear Support
Vector Machine, Logistic Regression, and Decision Tree. As we obtained a small, imbalanced dataset

--- Page 14 ---

14
Fig. 10. The performance of the models across all scenarios.
Fig. 11. The balanced accuracy of the models across all scenarios.
but rich in vocabulary, we introduced four scenarios to compare the models’ performance before
and after balancing the dataset. Later, we applied various metrics, including accuracy, precision,
recall, F1-score, F1 macro average, and hamming loss, to measure the performance of each model
in different scenarios.
We under-sampled the politics category, which comprised 62.2% of the data, and used SMOTE
to create a balanced dataset. For both groups of scenarios, we created two different training and

--- Page 15 ---

15
testing sets: 70% allocated for training and 30% for testing, and the other two scenarios used 90%
for training and only 10% for testing. The results showed that the models’ accuracy dropped for the
balanced data. Considering the goal of balancing, as shown in Figure 11, the balanced accuracy is
increased, implying a higher accuracy rate obtained for all the classes, particularly minor classes.
There are several reasons behind the performance of KNN on balanced data. The SMOTE
technique generates synthetic data points, which increases the dimension of features in the training
data. Accordingly, the KNN algorithm is prone to high-dimensional features as it fails to select the
best neighbor. Therefore, more complex and robust algorithms must be trained on high-dimensional
features. Due to its nature, the Decision Tree classifier poorly performed on the minor classes; the
algorithm requires large data to build a deeper tree with more nodes. Even after balancing, the
performance hardly improved.
We provided more insights on the models built in the first scenario. Figure 12 shows the prediction
probabilities using the LIME interpreter to visualize the classifiers’ decision-makings. All the models
correctly classified the text and selected similar features to confirm their predictions. It is important
to highlight that the preprocessing stage helped in creating models with great performance. Figure
13 clearly indicates that by removing irrelevant words, the model can prioritize more meaningful
features to make accurate predictions on unseen data.
We investigated further to evaluate the classifier’s performance by generating texts that belong
to multiple categories to challenge the models. We also intended to provide the translated version
of the text into Sorani to observe the prediction probabilities of each classifier and identify the
common traits shared between the dialects. As shown in Figure 14, the Linear SVM classifier
recognized features from several categories, yet it failed to provide enough certainty. Furthermore,
we noted that similar features were selected from both dialects, which supports the conclusion that
Hawrami remains a branch of the Kurdish language.
Despite using a small and imbalanced dataset, the linear SVM and logistic regression scored
the best accuracy in all scenarios, as shown in Table 7. Moreover, the KNN classifier scored 94%
accuracy in the balanced dataset. A Decision Tree model scored 89%, while not poor, as it scored the
least among the best. This achievement in the performance of the models can be attributed to the
richness of the data, since from 90% of the data, the TF-IDF generated 193,381 features. This number
of features in a small dataset can be exhausting for simple algorithms such as KNN, resulting in the
model over-fitting. However, SVM is more robust and designed to reduce over-fitting.
7
Conclusion and Future Works
Hawrami is a dialect of Kurdish that is classified as an endangered language. To preserve a language,
collecting textual data is considered as the first step. Additionally, these texts need to be cleaned
and organized.
This paper offers multiple text classification models for Hawrami using four algorithms, including
K-Nearest Neighbor, Linear Support Vector Machine, Logistic Regression, and Decision Tree. We
presented four scenarios to train the models on different sizes and types of data. The first two
scenarios attempted to conduct experiments on the original, imbalanced dataset as well as allocate
different sizes of data for training. The final scenarios were included to balance the dataset. As
shown in Table 7, the Linear SVM classifier scored the highest accuracy of 96% in the first two
scenarios.
In future works, we ask for attempts to improve techniques such as lemmatization and stemming
that can be employed in the preprocessing stage to reduce the dimensionality of features. We also
intend to use modern algorithms to improve the performance of the classifiers and apply feature
selection methods to prevent over-fitting and select the most relevant features. Finally, we invite

--- Page 16 ---

16
Fig. 12. LIME interpretation for all the models built in the first scenario.
Fig. 13. LIME interpretation for all the models built in the first scenario.
linguists to continue studies on the Kurdish language and share common pieces of knowledge with
NLP researchers to remove the barriers that prevent Kurdish from being computationally enabled.

--- Page 17 ---

17
Fig. 14. LIME interpretation for all the models built in the first scenario.
Table 7. The best model with the highest accuracy across all scenarios.
Scenario
Classifier
Accuracy
Precision
Recall
F1-score
F1 macro average
1
Linear SVM
0.96
0.96
0.96
0.95
0.79
2
Linear SVM
0.96
0.95
0.96
0.95
0.79
3
Linear SVM
0.94
0.93
0.94
0.93
0.80
4
Linear SVM
0.94
0.94
0.94
0.94
0.81
Acknowledgments
• To Ako Marani for his great linguistic interpretations.
• To our annotators, Marwan Mohammed and Fardin Azimi.
• To Hawre Bakhawan, founder of Kurdipedia, for granting permission to use their website as
a data source.
References
[1] 2024. https://anfsorani.com/%D9%87%DB%86%D8%B1%D8%A7%D9%85%DB%8C
[2] 2024. https://www.kurdipedia.org
[3] Salam Abdulla and Mzhda Hiwa Hama. 2015. Sentiment analyses for Kurdish social network texts using Naive Bayes
classifier. Journal of University of Human Development 1, 4 (2015), 393–397.
[4] Sina Ahmadi. 2019. A rule-based Kurdish text transliteration system. ACM Transactions on Asian and Low-Resource
Language Information Processing (TALLIP) 18, 2 (2019), 1–8.
[5] Sina Ahmadi. 2020. Building a corpus for the Zaza–Gorani language family. In Proceedings of the 7th workshop on NLP
for similar languages, varieties and dialects. 70–78.
[6] Sina Ahmadi, Hossein Hassani, and John P McCrae. 2019. Towards electronic lexicography for the Kurdish language.
In Proceedings of the sixth biennial conference on electronic lexicography (eLex). eLex 2019.
[7] Muhammad Pervez Akhter, Zheng Jiangbin, Irfan Raza Naqvi, Mohammed Abdelmajeed, Atif Mehmood, and Muham-
mad Tariq Sadiq. 2020. Document-Level Text Classification Using Single-Layer Multisize Filters Convolutional Neural
Network. IEEE Access 8 (2020), 42689–42707. https://doi.org/10.1109/ACCESS.2020.2976744
[8] Amalia Amalia, Opim Salim Sitompul, Erna Budhiarti Nababan, and Teddy Mantoro. 2020. An Efficient Text Classifica-
tion Using fastText for Bahasa Indonesia Documents Classification. In 2020 International Conference on Data Science,
Artificial Intelligence, and Business Analytics (DATABIA). 69–75. https://doi.org/10.1109/DATABIA50434.2020.9190447

--- Page 18 ---

18
[9] Zhila Amini, Mohammad Mohammadamini, Hawre Hosseini, Mehran Mansouri, and Daban Jaff. 2021. Central Kurdish
machine translation: First large scale parallel corpus and experiments. arXiv preprint arXiv:2106.09325 (2021).
[10] Antonios Anastasopoulos, Christopher Cox, Graham Neubig, and Hilaria Cruz. 2020. Endangered languages meet
Modern NLP. In Proceedings of the 28th International Conference on Computational Linguistics: Tutorial Abstracts. 39–45.
[11] Zeynep Arslan. 2017. Zazaki–yesterday, today and tomorrow. Survival and standardization of a threatened language.
Dieter Halwachs: Grazer Plurlingualismus Studien (GPS 04). Graz: GLM (2017).
[12] Afrasyaw Ashti and Koç Kayhan. 2021. A Brief Overview of Kurdish Natural Language Processing. In Proceedings of
Workshop on Intelligent Information Systems. 185.
[13] Rania Azad, Bilal Mohammed, Rawaz Mahmud, Lanya Zrar, and Shajwan Sdiqa. 2021. Fake News Detection in
low-resourced languages Kurdish language using Machine learning algorithms. Turkish Journal of Computer and
Mathematics Education (TURCOMAT) 12, 6 (2021), 4219–4225.
[14] Dimitris Bilianos. 2022. Experiments in Text Classification: Analyzing the Sentiment of Electronic Product Reviews
in Greek. Journal of Quantitative Linguistics 29, 3 (2022), 374–386. https://doi.org/10.1080/09296174.2021.1885872
arXiv:https://doi.org/10.1080/09296174.2021.1885872
[15] Kyumars Sheykh Esmaili. 2012. Challenges in Kurdish text processing. arXiv preprint arXiv:1212.0074 (2012).
[16] Ethnologue. [n. d.]. https://www.ethnologue.com/language/hac/
[17] Ciprian Gerstenberger, Niko Partanen, Michael Rießler, and Joshua Wilbur. 2017. Instant annotations–Applying
NLP methods to the annotation of spoken language documentation corpora. In Proceedings of the Third Workshop on
Computational Linguistics for Uralic Languages. 25–36.
[18] Jamal Habibullah. 2006. Ferhengî Werqûl. Spîrêz, Duhok.
[19] Geoffrey Haig. 2018. 3.3. The Iranian languages of northern Iraq. The Languages and Linguistics of Western Asia: An
Areal Perspective 6 (2018), 267.
[20] Geoffrey Haig and Yaron Matras. 2002. Kurdish linguistics: a brief overview. STUF-Language Typology and Universals
55, 1 (2002), 3–14.
[21] Hossein Hassani. 2017. BLARK for multi-dialect languages: towards the Kurdish BLARK. Language Resources and
Evaluation 52, 2 (2017), 625–644.
[22] Hossein Hassani. 2023. The impact of the Kurdish language on Technological Singularity. | Hussein Hassani |
TEDxNishtiman. https://www.youtube.com/watch?v=sDvs_8hMDzA&t=78s
[23] Hossein Hassani, Dzejla Medjedovic, et al. 2016. Automatic Kurdish dialects identification. Computer Science &
Information Technology 6, 2 (2016), 61–78.
[24] Amir Hassanpour. 1992. Nationalism and language in Kurdistan, 1918-1985. (1992).
[25] Anders Holmberg and David Odden. 2008. The noun phrase in Hawrami. Aspects of Iranian linguistics (2008).
[26] M Ikonomakis, Sotiris Kotsiantis, Vasilis Tampakas, et al. 2005. Text classification using machine learning techniques.
WSEAS transactions on computers 4, 8 (2005), 966–974.
[27] Ammar Ismael Kadhim. 2019. Survey on supervised machine learning techniques for automatic text classification.
Artificial Intelligence Review 52, 1 (2019), 273–292.
[28] KAL Kurdish Academy of Language. 2016. Kurdish dialectology. https://kurdishacademy.org/?p=373
[29] David Neil MacKenzie. 1966. The dialect of Awroman (Hawr¯am¯an-¯ı Luh¯on): Grammatical sketch, texts, and vocabulary.
Munksgaard, Elisabeth.
[30] Shervin Malmasi. 2016. Subdialectal differences in Sorani Kurdish. In Proceedings of the third workshop on NLP for
similar languages, varieties and dialects (vardial3). 89–96.
[31] Marani. 2020. Elfabêtî Horamî (1st edition ed.). Kurdipedia.
[32] Dastan Maulud, Karwan Jacksi, and Ismael Ali. 2023. Towards a Complete Kurdish NLP Pipeline: Challenges and
Opportunities. J. Inform 17, 1 (2023), 1–17.
[33] Christopher Moseley. 2010. Atlas of the World’s Languages in Danger. Unesco.
[34] Ezadin Mustafa. 1971. Serincê le zimanî edebiî yekgirtûy kurdî. Salman Al-Azmi Printing House, Baghdad, Iraq.
[35] Jamal Nabaz. 1976. Zimanî Yekgirtûy Kurdî. National Union of Kurdish Students.
[36] Saber Neamat. 2015. The Derivational Morphology of Word in Hawrami and Central Kurdish Dialects. Salahaddin
University.
[37] Ludwig Paul. 2008. Kurdish language I. History of the Kurdish language. Encyclopaedia Iranica (2008).
[38] Ni Qing-chao, Yin Cong-jue, and Zhao Dong-hua. 2021. Research on Small Sample Text Classification Based on
Attribute Extraction and Data Augmentation. In 2021 IEEE 6th International Conference on Cloud Computing and Big
Data Analytics (ICCCBDA). 53–57. https://doi.org/10.1109/ICCCBDA51879.2021.9442500
[39] Tarik A Rashid, Arazo M Mustafa, and Ari M Saeed. 2018. Automatic Kurdish text classification using KDC 4007 dataset.
In Advances in Internetworking, Data & Web Technologies: The 5th International Conference on Emerging Internetworking,
Data & Web Technologies (EIDWT-2017). Springer, 187–198.

--- Page 19 ---

19
[40] Tarik A Rashid, Didar D Rashad, Hiwa M Gaznai, and Ahmed S Shamsaldin. 2017. A Systematic Web Mining Based
Approach for Forecasting Terrorism. In Modeling, Design and Simulation of Systems: 17th Asia Simulation Conference,
AsiaSim 2017, Melaka, Malaysia, August 27–29, 2017, Proceedings, Part II 17. Springer, 284–295.
[41] Mohammad Rzgar. 2024. Şêwezarî Hewramî. https://bit.ly/3StnVIl
[42] Ari M Saeed, Tarik A Rashid, Arazo M Mustafa, Rawan A Al-Rashid Agha, Ahmed S Shamsaldin, and Nawzad K
Al-Salihi. 2018. An evaluation of Reber stemmer with longest match stemmer technique in Kurdish Sorani text
classification. Iran Journal of Computer Science 1 (2018), 99–107.
[43] Dana Abubakr Salh and Rebwar Mala Nabi. 2023. Kurdish Fake News Detection Based on Machine Learning Approaches.
Passer Journal of Basic and Applied Sciences 5, 2 (2023), 262–271.
[44] Maryam Sami and Hossein Hassani. 2023. Sentiment Analysis of Opinions about Online Education in the Kurdistan
Region of Iraq during COVID-19. Qeios (2023).
[45] Kazheen Ismael Taher and JIHAN Abdulazeez Ahmed. 2023. Correlation Evaluation Scale Through Text Mining
Algorithms and Implementation on the Kurdish Language: A Review. QALAAI ZANIST JOURNAL 8, 2 (2023), 1312–1337.
[46] Givi Tavadze. 2019. Spreading of the Kurdish language dialects and writing systems used in the Middle East. Bull.
Georg. Natl. Acad. Sci 13, 1 (2019).
[47] Shiyue Zhang, Ben Frey, and Mohit Bansal. 2022. How can NLP help revitalize endangered languages? a case study
and roadmap for the Cherokee language. arXiv preprint arXiv:2204.11909 (2022).

```
