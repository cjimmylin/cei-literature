---
title: "Azani Unsupervised Thematic Clustering Hadith - PDF Extract"
source_pdf: "2023-Al-Azani-Unsupervised Thematic Clustering Hadith.pdf"
pages: 12
extracted_at: "2026-04-03T11:05:41.866257"
---

# PDF Extract: Azani Unsupervised Thematic Clustering Hadith

**Source PDF:** 2023-Al-Azani-Unsupervised Thematic Clustering Hadith.pdf
**Total Pages:** 12

---

## Content

--- Page 1 ---

Unsupervised Thematic Clustering of hadith Texts
using the Apriori Algorithm
1st Wisnu Uriawan
Informatics Department
UIN Sunan Gunung Djati Bandung
Jawa Barat, Indonesia
wisnu u@uinsgd.ac.id
2nd Achmad Ajie Priyajie
Informatics Department
UIN Sunan Gunung Djati Bandung
Jawa Barat, Indonesia
achmadajie74@gmail.com
3rd Angga Gustian
Informatics Department
UIN Sunan Gunung Djati Bandung
Jawa Barat, Indonesia
diazzangga3@gmail.com
4th Fikri Nur Hidayat
Informatics Department
UIN Sunan Gunung Djati Bandung
Jawa Barat, Indonesia
fkrnhdyt@gmail.com
5th Muhamad Fikri Zaelani
Informatics Department
UIN Sunan Gunung Djati Bandung
Jawa Barat, Indonesia
fikrimuhamadzael@gmail.com
6th Sendi Ahmad Rafiudin
Informatics Department
UIN Sunan Gunung Djati Bandung
Jawa Barat, Indonesia
sendymurphy@gmail.com
Abstract—This research stems from the urgency to automate
the thematic grouping of hadith in line with the growing
digitalization of Islamic texts. Based on a literature review,
the unsupervised learning approach with the Apriori algorithm
has proven effective in identifying association patterns and
semantic relations in unlabeled text data. The dataset used is the
Indonesian Translation of the hadith of Bukhari, which first goes
through preprocessing stages including case folding, punctuation
cleaning, tokenization, stopword removal, and stemming. Next, an
association rule mining analysis was conducted using the Apriori
algorithm with support, confidence, and lift parameters. The
results show the existence of meaningful association patterns such
as the relationship between “rakaat-prayer”, “verse-revelation”,
and “hadith-story”, which describe the themes of worship, reve-
lation, and hadith narration. These findings demonstrate that the
Apriori algorithm has the ability to automatically uncover latent
semantic relationships, while contributing to the development of
digital Islamic studies and technology-based learning systems.
Index Terms—Apriori, unsupervised learning, text mining,
hadis, asosiasi tematik.
I. INTRODUCTION
hadith is one of the main sources of Islamic teachings after
the Qur’an which contains theological, historical and moral
values [1].With the advancement of the digital era, various
efforts have been made to transform hadith books into digital
form to facilitate access, searching, and scientific study. How-
ever, this digitization process presents new challenges in terms
of managing, grouping, interpreting, and classifying hadith
by theme. The ever-increasing number of hadith digitally,
both in text form and in online databases, raises the need
for new approaches capable of automatically identifying the
interconnectedness of meaning and context.
Traditionally, the determination of themes in hadith has
been done manually by hadith scholars using philological
and contextual approaches. While accurate, this approach is
time-consuming and prone to interpreter subjectivity. At the
same time, the rapid development of information technology
has opened up opportunities for the application of machine
learning and text mining in the management of religious texts.
In this context, the use of unsupervised learning approaches is
highly relevant, as they are able to recognize thematic patterns
and structures from text data without the need for initial labels
or annotations [2]. This approach is in line with the spirit of
automation in digital Islamic studies which aims to expand
access to religious knowledge while increasing the objectivity
of analysis of hadith texts.
One of the algorithms widely used in the unsupervised
learning domain is Apriori, which is widely implemented in
association rule mining to find relationships between items or
words in a data set [3] [4]. In the context of hadith texts,
this algorithm can be used to extract semantic relationships
between frequently occurring words or concepts, thus creating
a thematic structure that reflects the latent meaning behind the
hadith narrative. Thus, analysis using Apriori is not simply a
frequency count but also an attempt to build a data-driven
conceptual understanding of religious texts.
The application of text mining and natural language pro-
cessing (NLP) in the analysis of Islamic texts can help
discover previously hidden patterns of knowledge, as well as
support the birth of more systematic and measurable data-
based thematic interpretations [5].The use of this method also
strengthens the Digital Islamic Humanities initiative which
seeks to integrate computational methodologies in the study
of classical texts to maintain their relevance in the digital age
[6].
Furthermore, this research supports the achievement of
Sustainable Development Goal (SDG) 4: Quality Education,
particularly in encouraging access to inclusive and technology-
based education [7] [8] [9] [10]. By providing an automated
method for understanding the content of hadith, this approach
expands access to quality learning for students, researchers,
and the general public, while bridging traditional values with
modern technology within the framework of Islamic education.
This research also contributes to the rapidly developing
arXiv:2512.16694v1  [cs.AI]  18 Dec 2025

--- Page 2 ---

field of Artificial Intelligence for Islamic Studies (AIIS) in
the last decade. AIIS seeks to combine artificial intelligence
approaches with Islamic texts to extract meaning, analyze
sanad (chain of transmission), and identify conceptual rela-
tionships between hadith. As explained by Al-Hasan et al.
(2021), unsupervised clustering and association rule mining
methods can be used to uncover the semantic dimensions of
hadith texts, which are often missed through manual analysis
[11].Therefore, the integration of the Apriori algorithm in
hadith studies is not only a technical innovation, but also a
methodological transformation in understanding the sources
of Islamic teachings more broadly, deeply, and objectively.
Based on this urgency, this study proposes the application
of the Apriori algorithm within an unsupervised learning
framework to extract word association patterns in digital
Indonesian-language hadith texts. This approach is expected
to automatically form thematic groupings of hadith, facilitate
the process of discovering new meanings, and strengthen
the direction of developing an artificial intelligence-based
religious information system that supports the vision of digital
Islamic education and quality education.
II. RELATED WORK
Previous research has demonstrated the significant potential
of unsupervised learning approaches in detecting patterns from
unlabeled data. One study developed an AI-based framework
capable of recognizing hidden relationships among crime
data, with results demonstrating the model’s effectiveness in
clustering incidents based on pattern similarities. Although the
context of this research is in the realm of crime analysis, the
application of unsupervised methods and association patterns
from text data demonstrates high relevance for thematic clus-
tering of hadith, which are also unlabeled and require mapping
the meaning of latent patterns [12].
A comparative analysis of two popular algorithms, K-Means
for clustering and Apriori for association patterns, shows
that K-Means excels in forming homogeneous clusters, while
Apriori is more effective in finding relationships between items
within a cluster. This approach demonstrates that the combi-
nation of clustering techniques and association algorithms can
enrich the grouping of hadith texts by providing additional
insight into the semantic relationships within them [13].
Another study demonstrated the application of the Apriori
algorithm in analyzing sales transactions to aid inventory
management decisions. The results were concrete association
rules, such as the relationship between purchases of certain
items based on consumer habits. Although this research was
conducted in a retail context, the approach is relevant because
it illustrates Apriori’s ability to extract meaningful rules from
raw data. This ability is also needed to discover thematic
relationships between the contents of hadith texts [14].
Another study examined the process of clustering text-based
documents through feature extraction and classification using
the Na¨ıve Bayes method. Although this approach includes
supervised learning, the study emphasized the importance of
preprocessing stages such as tokenization and feature selection
to improve document clustering accuracy. Its relevance to
clustering hadith texts lies in the importance of preprocessing
the text as a key to success in unsupervised approaches such
as clustering and association algorithms [15].
Another unsupervised learning approach demonstrated the
effectiveness of the K-Means algorithm in forming homo-
geneous clusters from various types of unlabeled data. The
results of this study confirmed that K-Means is capable of
efficiently identifying latent structures in data, provided the
number of clusters is selected appropriately. This aligns with
efforts to cluster hadith texts based on similar themes, where
K-Means can be used to automatically map documents into
thematic clusters [16].
Another study introduced an algorithm for automatically
generating concept maps from text using text analysis and
association rule mining techniques. One of the main techniques
is the Apriori algorithm, which is used to extract relationships
between concepts based on word frequency and association.
The results of this study are concept maps that automatically
represent the knowledge structure within documents, demon-
strating Apriori’s great potential in constructing meaningful
semantic representations from text collections [17].
A similar approach was also applied to identify sales trans-
action patterns for local brands, where the Apriori algorithm
was able to transform sales data into strategic information
for marketing decision-making. The results showed that the
association patterns discovered can support the development
of data-driven strategies, relevant to the goal of clustering
hadith texts, which also focuses on discovering meaningful
relationships between concepts [18].
Another study utilized the Apriori algorithm to provide book
placement recommendations based on borrowing patterns. The
resulting system was able to identify relationships between
frequently searched-for book categories, thereby improving
management and search efficiency. This approach can be used
as an analogy for thematic mapping of hadith texts based on
the co-occurrence of words or concepts within them [19].
Research combining the K-Means and Apriori methods
shows that the combination is capable of forming representa-
tive clusters and identifying strong relationships between items
with significant support and confidence values. This integra-
tion of clustering and association rule techniques is crucial
for exploring the latent structure and semantic relationships of
data, including in the context of hadith texts [20].
The study demonstrates the application of the Apriori algo-
rithm in the retail sector to analyze inter-product relationship
patterns based on large sales data sets. Using an association
rule mining approach, the study was able to identify prod-
uct combinations with high support and confidence values,
resulting in association rules that can be used for promotional
strategies and product arrangement in stores. The relevance of
this study to the study of Unsupervised Thematic Clustering
of hadith Texts using the Apriori Algorithm lies in the ability
of the same algorithm to discover latent relationships between
items or concepts from large data sets [21]. In the context of
hadith texts, this approach can be utilized to uncover associ-

--- Page 3 ---

ations of meaning between terms or themes, thus assisting in
more meaningful and data-based thematic grouping.
Finally, the Apriori algorithm was also applied to identify
spare parts purchasing patterns by generating high-confidence
association rules. The results show that Apriori can aid ef-
ficient product layout and support strategic decisions. This
application conceptually parallels the thematic clustering of
hadith texts, which aims to discover hidden relationships
between concepts or terms within the text [22].
Many issues arise in the study of hadith that are trending in
the discipline, ranging from the digitization of hadith data to
case-based analyses concerning approximate narrator chains.
However, this paper does not focus on estimating, justifying,
or authenticating hadith; instead, it highlights the application
of data mining techniques on hadith datasets. In this study, the
hadith dataset was incorporated into a machine learning tool,
specifically text clustering, to examine the potential clustering
of hadith texts based on frequently appearing words. The
objective was to apply BERT modeling to cluster hadith
from Sahih Bukhari and Muslim, exploring the feasibility
of using NLP techniques for this task. The findings of this
research contribute to the advancement of more sophisticated
and accurate methods for text analysis [23].
Based on various previous studies, it appears that the
Apriori algorithm and clustering methods such as K-Means
have proven effective in uncovering hidden patterns in various
types of data, including transaction data, inventory, and text
documents. The use of an unsupervised learning approach
provides flexibility in analyzing data without the need for
labels, making it highly suitable for thematic clustering of
hadith texts, which naturally lack theme annotations. The
integration of Apriori and clustering opens up significant
opportunities for extracting knowledge structures and semantic
relationships between concepts in religious texts. Therefore,
this study seeks to build on the contributions of previous
studies by applying a similar approach specifically to hadith
texts for the purpose of automatic and systematic interpretation
and knowledge discovery.
III. METHODOLOGY
The increasing use of machine learning in hadith studies not
only enables clustering and thematic grouping using models
such as BERT but also opens opportunities to uncover deeper
semantic relationships within the texts. Beyond clustering
approaches, unsupervised techniques can be employed to
discover patterns that reveal how certain concepts, terms,
or themes frequently appear together in classical narrations.
These methods complement prior analyses by providing an-
other perspective on textual structure and hidden associations
within the hadith corpus.
This research employs an unsupervised learning approach
with the Apriori algorithm to extract word associations from
hadith texts. This method aims to identify thematic connec-
tions between words to establish meaningful theme groups,
serving as a basis for new knowledge. The technical stages of
the process are shown in Figure 1.
Fig. 1. Research Methodology
A. Data Collection
The hadith dataset used in this study was sourced from the
’Indonesian Translation of the hadith of Bukhari’s which is
available on Dataverse. This dataset comprises thousands of
hadith text entries in Indonesian (translated), complete with
their corresponding hadith ID.
1) Amount of Data ± 6000 entry (select a subset if neces-
sary)
2) Data Format Excel (.xlsx)
3) Data Source Indonesian Translation of the hadith of
Bukhari (Single-label) [24]
Data Format
TABLE I
DATASET ATTRIBUTES
dataset
attributes
Information
No
Sequential number for each hadith entry in the dataset,
used as a unique identifier or data index.
BAB
Indicates the chapter number (sub-category/topic) to
which the hadith belongs.
Hadist
The textual content of the hadith. This is the main
component analyzed in the research, particularly in the
pre-processing stage and association analysis.
Len
The length of the hadith text in characters. This can be
used for additional analysis such as text-length filtering
or statistical distribution of hadith lengths.
B. Pre-processing Data
The objective of the preprocessing stage is to clean and
prepare the text so it can serve as transactions for association

--- Page 4 ---

rule mining. The procedures performed are as follows:
Fig. 2. Pre-Prossesing
1) Case Folding
Case folding is the process of converting all charac-
ters in the text into (lowercase) [25]. The objective
is to standardize the word format. This is necessary
because in text processing, terms like ”Islam“ ”islam“
and ”ISLAM“ would be treated as three distinct entities
if normalization is not applied. Therefore, every line of
the hadith text is converted to lowercase, ensuring that
words appearing in capitalized forms are still processed
as the same word.
2) Punctuation Removal
Punctuation and non-alphabetic characters (such as pe-
riods, commas, exclamation marks, numbers, and other
symbols) lack semantic contribution in the word associ-
ation formation process. Consequently, these characters
are removed from the text.
3) Tokenization (Lexical Analysis)
Tokenization is the process of splitting the text into word
units called tokens [26].This step is crucial for individ-
ually analyzing words and forming word transactions.
To achieve this, each line of text is broken down based
on spaces, yielding a list of words (tokens) that can be
analyzed separately.
4) Stopword Removal
Stopwords are common words that appear frequently
but lack significant semantic importance in thematic
analysis, such as ”dan“ (and), ”yang“ (which), ”dari“
(from), and so on [26]. n the hadith context, there
are also religious terms that occur too frequently yet
lack relevance in forming thematic clusters, such as
”rasulullah“ (Messenger of God), ”nabi“ (Prophet),
”shallallahu“ (may God bless him and grant him peace),
and ”ibnu“ (son of). The objective of this stage is to filter
out words that do not directly contribute to the formation
of thematic associations within the hadith texts. By
eliminating these terms, the subsequent analysis can
focus more effectively on the core meaning of each
hadith narration, using the following procedure:
a) Retrieve the Indonesian stopword list from the
NLTK library.
b) Add custom stopwords that frequently appear in
hadith texts but are not relevant for association
analysis.
c) Remove all tokens included in the stopword list.
5) Stemming
Stemming is the process of returning a word to its base
form (root form) [27]. For example, the words ”beri-
man“ ”berimanlah“ and ”keimanan“ will be reduced to
the root form ”iman“ The goal is to unify various derived
forms of a word so they are counted as the same entity
in the association process.
6) Data Preprocessing Integration
All of the steps above are then integrated into a single
sequential process and applied to each text entry in the
dataset. The final result of this stage is a representation
of each hadith in the form of a clean and consistent
list of root words, ready to be used for word-association
analysis. This representation is referred to as a transac-
tion, which serves as the input for data transformation
and the application of the Apriori algorithm.
7) Data Transformation
After the preprocessing stage is completed, the text
data in the form of lists of root-word tokens from
each hadith is then converted into a transaction format
for association processing. The data transformation is
carried out so that the data can be interpreted as a binary
representation, indicating whether a word appears (1) or
does not appear (0) in each hadith.
This binary representation is known as one-hot encod-
ing, which is commonly used in data mining techniques.
Each hadith is represented as a row in a table, while
the columns correspond to the unique words that appear
in the entire dataset. If a word appears in the hadith,
its column is assigned a value of 1, and if it does not
appear, it is assigned a value of 0.
This transformation is important because the Apriori al-
gorithm requires input in the form of binary transactions
to calculate the frequency of item (word) combinations
across the entire dataset. With this format, each hadith is
treated as a transaction basket containing a set of items
in the form of words.
This process enables association analysis to be carried

--- Page 5 ---

out efficiently, as the uniform data structure allows the
system to easily calculate the support, confidence, and
lift values for each word combination. In the context of
hadith research, this approach helps reveal relationships
between religious concepts that are hidden within the
narrative text. Each pair or group of words that fre-
quently co-occurs in certain hadiths may indicate se-
mantic relationships that reflect specific themes, topics,
or contexts of religious events.
The binary transaction representation also provides flex-
ibility for integrating other algorithms in later analysis
stages, such as clustering or thematic classification.
Once the association patterns are obtained, the results
can be used to group hadiths based on similarities in
their word structures. In this way, the Apriori method not
only functions to discover relationships between words
but also serves as a foundation for grouping hadiths
according to similar content. This approach expands
the scope of hadith text analysis from simple word
exploration to a more systematic mapping of knowledge.
In its application, constructing the binary representation
requires an accurate word-normalization stage to ensure
that word meanings are not distorted. Each token must
undergo lemmatization or stemming to guarantee that
the word forms used are consistent. For example, the
words ”shalat“ ”menunaikan shalat” and ”shalatlah“
must be reduced to the same root form, namely ”shalat“
This uniformity is essential so that word frequency
truly reflects conceptual connections rather than mere
morphological variations.
The results of this transformation also play a role in
ensuring that recurring patterns can be identified objec-
tively. With a standardized data structure, the system can
calculate word combinations with measurable complex-
ity, free from human interpretive bias. In the context of
religious text studies, this helps produce more neutral,
data-driven analyses while strengthening transparency in
the process of knowledge discovery.
The application of binary transaction formatting in ha-
dith studies reflects the integration of modern scientific
approaches with classical Islamic literacy traditions.
Textual and narrative data can now be processed in
a quantitative form, allowing researchers to uncover
regularities and thematic patterns computationally. Thus,
this approach not only transforms how hadith texts
are analyzed but also broadens the horizon of Islamic
scholarship toward a more empirical, adaptive, and tech-
nologically relevant direction.
C. application of the Apriori algorithm
Apriori is an algorithm used to discover association patterns
from transactional data. In the context of this study, the
algorithm is used to identify frequent itemsets, which are
groups of words that often appear together within the same
hadith.
The first step in this process is determining the minimum
support value, which serves as the threshold for how frequently
a word combination must occur to be considered significant.
For example, if the minimum support is set to 0.02, then only
word combinations that appear in at least 2 percent of all
hadiths will be taken into account.
After that, the algorithm generates word combinations of
increasing sizes—single words (1-itemsets), pairs of words (2-
itemsets), triplets (3-itemsets), and so on. Each combination
is evaluated against the support threshold. If a combination
does not meet the requirement, all combinations that include
it are also discarded. This makes the Apriori algorithm efficient
because it uses the principle of antimonotonicity: if an itemset
is not frequent, then any of its supersets will definitely not be
frequent.
In its application to hadith texts, each word that has gone
through preprocessing is treated as an item, and each hadith
is treated as a transaction. The process of finding frequent
itemsets is carried out iteratively to identify word combina-
tions that commonly appear together in a single hadith. For
example, if the words ”shalat“ and ”rakaat“ frequently appear
close to each other in several hadiths, then their combination
will be detected as a frequent 2-itemset. The higher the support
value of the combination, the stronger the indication that the
two words share a significant thematic relationship within the
context of worship.
The frequent itemsets identified at this stage become the
foundation for forming association rules. Each combination of
words that meets the minimum support value will be paired
in the form of antecedent →consequent to be further
analyzed using the confidence and lift metrics. Thus, this
stage is not only intended to calculate frequency but also to
select word combinations that are suitable to serve as the basis
for thematic inference. This approach allows the identification
of semantic relationships to be carried out objectively based
on the distribution of words across the entire hadith corpus,
without subjective intervention from the researcher.
The application of the Apriori algorithm in religious text
research, such as the study of hadith, demonstrates that com-
putational methods can be used to uncover conceptual patterns
within classical texts. The results obtained are not merely num-
bers or statistics, but also new insights into the connections
between concepts that hold theological relevance. By combin-
ing quantitative approaches with contextual interpretation, this
algorithm serves as a scientific tool that strengthens traditional
qualitative analysis methods. Such an approach affirms that
integrating data science with Islamic studies can produce new
forms of understanding that are systematic, transparent, and
profound in exploring the intellectual heritage of Islam.
D. formation of association rules
The final step in this research method is to construct
association rules based on the frequent itemsets that have
been identified. Association rules express an implicative
relationship between two groups of words, for example, ”if
word A appears, then word B is also likely to appear.“ In the

--- Page 6 ---

context of this study, association rules are used to identify
thematic relationships between words in hadith texts. Each
rule is evaluated based on three main metrics:
1) Support:Measuring how frequently the word combina-
tion appears in the dataset.
2) Confidence: Measuring the probability that the conse-
quent word appears when the antecedent word appears.
3) Lift: Measuring the strength of the relationship between
the two groups of words compared to their random oc-
currence. A lift value greater than 1 indicates a positive
association.
Association rules that meet the confidence and lift thresh-
olds are then analyzed to identify thematically meaningful
patterns. The results of this process can be used as a founda-
tion for forming thematic groups within hadiths, discovering
semantic relationships between words, and building hadith
content recommendation systems based on relevant topics.
The process of forming association rules is not only me-
chanical but also requires conceptual interpretation so that the
results can be understood within the context of Islamic schol-
arship. Each word pair with a high lift value must be analyzed
further to ensure its semantic and contextual relevance within
the hadith text. For example, the relationship between the
words ”ayat“ and ”turun“ may statistically indicate a strong
connection, but theologically, it also reinforces the theme of
revelation, which is central to prophetic experience. Thus, the
interpretation stage becomes an important part of ensuring
that the analytical results remain aligned with the religious
meanings embedded in the text.
The use of association rules in hadith research also opens
possibilities for exploring cross-thematic patterns. Combina-
tions of words involving elements of worship, ethics, or
prophetic history can be analyzed together to identify con-
ceptual relationships across different domains. This approach
helps build a more comprehensive understanding of the the-
matic structure of hadith, where a concept does not stand alone
but is interconnected within a broader network of meanings.
Supported by metrics such as support and confidence, these
analytical results can be mapped into a comprehensive, data-
driven model of thematic relationships.
The validated association rules can serve as the founda-
tion for developing digital Islamic knowledge systems. Such
systems can support automatic classification, semantic search,
and theme-based hadith learning. By leveraging accurate word
association data, users can explore hadiths not only through
specific keywords but also through conceptual relationships
mapped by the system. This approach marks an important step
toward the digitalization of hadith studies, focusing not only
on preserving the text but also on uncovering deeper meanings
and semantic relationships among religious concepts.
IV. RESULT AND DISCUSSION
A. Result
1) Thematic Clustering Results: The application of the
Apriori algorithm to the collection of hadith texts aims to
extract word association patterns that indicate dominant narra-
tive themes. With a minimum support parameter of 0.02 and a
minimum lift of 0.6, the system successfully identified several
strong and semantically meaningful association rules. Apriori
produced relations in the form of antecedent →consequent
pairs, which were then interpreted as thematic groupings based
on the co-occurrence of words within hadith documents.
Tabel II The following presents ten association rules with
the highest confidence values, indicating the probability that
the consequent appears when the antecedent has appeared
within a single transaction (hadith document).
Rule number (1) shows the strongest association between
the words ”rakaat“ and ”shalat“, with a confidence value of
0.900000 and a lift of 6.428440. Conceptually, this pattern
represents the most fundamental worship relationship in hadith
texts, where ”rakaat“ is a core component of the practice
of ”shalat.“ Meanwhile, rules (2) to (5) broaden the scope
of associations still related to worship contexts, such as
”laksana,“ ”diri,“ and ”malam,“ each representing expressions
of command, spiritual awareness, and the time of performing
prayer.
The theme of revelation is strongly reflected in rules (3)
and (4), which capture the reciprocal relationship between
”ayat“ and ”turun.“ The highest lift values in these two rules
(6.954309) indicate the consistency of the revelation concept
within hadith narratives, where the process of divine descent is
explicitly recorded through the co-occurrence of these words.
This association affirms that the algorithm can detect semantic
patterns aligned with the theological meaning structure in
Islamic tradition.
Other rule groups, such as (6) and (7), reveal patterns
associated with the theme of hadith transmission. The relation-
ships between ”hadits,“ ”cerita,“ and ”kepada“ reflect the oral
narrative form in the transmission process, consistent with the
sanad and matan structures commonly found in phrases such
as ”telah menceritakan kepada kami...“ Although their confi-
dence values are not as high as those in the worship group,
the high lift values indicate that these associations remain
semantically significant and reflect distinctive characteristics
of hadith literature.
On the other hand, rules (9) and (10) highlight the con-
nection between ”baca“ and ”ayat,“ representing the themes
of recitation worship and Qur’anic revelation. Both have
consistently high lift values (4.912033), indicating a strong
bidirectional relationship in the context of the command to
read revelation. These findings reinforce the view that word
associations can serve as important indicators for automati-
cally identifying religious themes.
The association patterns presented in the table do not merely
show repeated words but also reflect how hadith texts construct
meaning through conceptual co-occurrence. The relationships
between words illustrate an interconnected meaning structure,
where themes of worship, revelation, and transmission form
mutually reinforcing thematic networks. These results show
that the language of hadith is not random but is semantically
organized according to the structure of religious knowledge.

--- Page 7 ---

TABLE II
ASSOCIATION RULE MINING RESULTS
No
Antecedents
Consequent
Antecedent Support
Consequent Support
Support
Confidence
Lift
1
rakaat
shalat
0.028543
0.140003
0.025689
0.900000
6.428440
2
laksana
shalat
0.056229
0.140003
0.033395
0.593909
4.242118
3
ayat
turun
0.072642
0.082774
0.041815
0.575639
6.954309
4
turun
ayat
0.082774
0.072642
0.041815
0.505172
6.954309
5
diri
shalat
0.069930
0.140003
0.030541
0.436735
3.119470
6
hadits
cerita
0.059797
0.081775
0.024404
0.408115
4.990678
7
cerita
kepada
0.081775
0.100756
0.030113
0.368237
3.654730
8
malam
shalat
0.056943
0.140003
0.020551
0.360902
2.577821
9
baca
ayat
0.062794
0.072642
0.022406
0.356818
4.912033
10
ayat
baca
0.072642
0.022406
0.022406
0.308448
4.912033
Interpretation of the association rules also demonstrates the
capability of this approach to uncover thematic patterns rele-
vant to classical Islamic scholarly traditions. The associations
produced in an unsupervised manner remain consistent with
meanings recognized in hadith studies, such as the concepts of
sanad, matan, and worship. This approach indicates that data-
driven modeling can support the reconstruction of meaning in
religious texts without losing their normative and theological
context.
The association results presented in the table IIindicates
that the Apriori method is capable of capturing the main
themes within hadith texts, including aspects of worship,
revelation, and transmission. These patterns can serve as the
foundation for developing thematic annotations, data-driven
hadith ontologies, and semantic search systems that enable
contextual meaning retrieval. Thus, this approach not only sup-
ports academic analysis but also becomes an important basis
for developing intelligent and structured Islamic knowledge
technologies.
2) Thematic Interpretation and Knowledge Findings: The
association rules generated from the application of the Apriori
algorithm reveal semantic patterns that reflect the main themes
in hadith texts. Although obtained in an unsupervised manner
and without manual annotation, these rules exhibit conceptual
alignment with the meaning structures commonly recognized
in hadith studies, particularly in the domains of worship,
revelation, and oral transmission. Grouping the rules into these
themes forms the basis for potential knowledge representations
that can be developed into thematic annotations, ontologies,
and knowledge-navigation systems for religious texts.
The association rules can be viewed as a form of auto-
matic thematic pattern discovery with the potential to serve
as the foundation for developing representations of religious
knowledge. Grouping the rules into themes such as worship,
revelation, ethics, and oral transmission can assist in con-
structing thematic annotation systems, scientific ontologies of
hadith studies, and semantic navigation tools for religious
texts. Within the fields of computer science and digital Is-
lamic studies, these findings open significant opportunities for
building data-mining-based models of hadith comprehension,
capable of presenting inter-concept relationships in a concep-
tual, systematic, and structured manner without neglecting the
values of traditional scholarship.
These findings demonstrate that association methods func-
tion not only as exploratory tools for discovering relationships
between words but also as bridges toward the development
of computational Islamic knowledge systems. By utilizing the
association rules produced, a system can identify relational
patterns that reflect broader religious understanding. For in-
stance, the associations among the words ”shalat,“ ”rakaat,“
and ”malam“ do not merely illustrate linguistic relationships
but also imply specific worship practices with deep spiritual
significance. This approach enables machines to understand
contextual meaning in religious texts in a more semantic,
rather than merely syntactic, manner.
The application of association analysis in the context of
hadith also contributes to the advancement of digital thematic
exegesis. By tracing relationships between words and themes
within hadith, researchers can identify how particular concepts
are consistently connected to other teachings across various
textual sources. This helps construct an interpretive framework
grounded in data-driven evidence, strengthening the validity of
religious interpretation based on the frequency and consistency
of concept occurrence. Thus, this method can serve as a scien-
tific tool that enriches traditional approaches to understanding
religious messages.
The potential applications of these findings extend beyond
academic research and can be developed into educational and
da’wah technologies powered by artificial intelligence. Digital
systems supported by hadith association data can be used to
explore themes, answer religious questions, or provide text
recommendations based on specific contexts. For example,
users searching for the topic of ”revelation“ can automatically
be directed to hadith closely associated with the words ”ayat“
”turun“ and ”wahyu“ In this way, the results of this research
not only enrich academic discourse but also expand public
access to deep, structured, and data-driven understanding of
hadith.
1) Worship Theme
he following four rules demonstrate strong relationships
related to religious practices, particularly prayer shalat:
a) (rakaat) →(shalat) dengan confidence 0.900000
dan lift 6.428440,
b) (laksana) →(shalat) dengan confidence 0.593909
dan lift 4.242118
c) (diri) →(shalat) confidence 0.436735, dan lift
3.119470

--- Page 8 ---

d) (malam) →(shalat) (confidence 0.360902, dan lift
2.577821)
The four rules reflect ritual practices in Islam. All of
them emphasize aspects of performing prayer (shalat) in
various forms and conditions. The presence of the word
”malam“ (night) in association with ”shalat“ indicates
the recurring theme of night prayers in the hadith,
while ”diri“ (self) relates to the personal and spiritual
dimension of worship.
The knowledge discovered here shows that the concept
of worship in the hadith is not conveyed solely through
the explicit word ”shalat“, but also through patterns of
co-occurring meanings such as ”rakaat“, ”malam“, and
”diri“. These patterns demonstrate that the interpretation
of worship is constructed through temporal, spiritual,
and structural contexts.
2) Prophetic Theme
The following two rules illustrate a narrative about the
delivery of revelation that does not always explicitly
mention ”revelation“ or ”angel“ but is reflected through
the co-occurrence of the words ”descend“ ”verse“ and
”read“.
a) (ayat)
→
(turun)
(confidence
0.575639,
lift
6.954309),
b) (baca)
→
(ayat)
dan
(ayat)
→
(baca)
(lift
4.912033)
The pairing of ”ayat“ and ”turun“ indicates a close
reciprocal relationship in the context of revelation. This
suggests that hadith mentioning ”ayat“ are very likely
to also mention the process of their ”turun“ referring to
the divine context of revelation being sent down to the
Prophet Muhammad (peace be upon him).
The associations (verse–descend) and (read–verse) re-
flect the narrative of revelation and the Prophet’s in-
teraction with it. These bidirectional relations highlight
the strong connection between the words ”read“ and
”verse,“ which appear in early prophetic hadiths, par-
ticularly those related to the command to read (iqra’)
and its relationship to the Qur’anic verses. This finding
reflects the cognitive and spiritual processes of prophet-
hood—how revelation is conveyed and received through
the act of reading and internalizing the divine message.
Overall, these associations reveal a fundamental theme
in hadith literature: the prophetic function as the re-
ceiver, transmitter, and teacher of revelation, consistently
manifested in the linguistic structure and content of the
hadith texts.
As a knowledge finding within the hadith texts, the
narrative of divine transmission can be reconstructed
through semantic traces such as ”verse“ and ”descend“
or ”read,“ without the explicit mention of prophetic or
angelic entities. This shows that the system is capable
of detecting the prophetic process implicitly.
3) Theme of hadith Transmission
The associations in this theme highlight how hadiths are
narrated from one individual to another:
a) (hadits) →(cerita) (confidence 0.408115, lift
4.990678),
b) (cerita) →(kepada) (confidence 0.368237, lift
3.654730)
Although the confidence values are lower compared to
the other rules, the lift values remain high. This indicates
that the narrative structures such as ”was narrated to...“
or ”comes from the story of...“ frequently appear in
hadiths and represent elements of the sanad (chain
of narrators) and matan (content of the hadith). In
other words, the word-association approach is capable
of revealing the pattern of hadith transmission without
requiring explicit structural annotation.
The knowledge discovery that emerges here is that the
structure of the sanad in hadiths can be indirectly iden-
tified through word-association patterns such as ”story“
and ”to“, which function as connectors between narra-
tors. This opens opportunities for developing systems
that can automatically identify patterns of transmission,
even when they are not explicitly labeled as sanad.
3) Validasi dan Implikasi: Validation of the thematic clus-
tering results in this study was carried out by examining
the association metrics quantitatively and through domain-
knowledge evaluation of the semantic meaning and scholarly
context of hadith studies. The quantitative approach was used
to ensure that the co-occurring word patterns exhibit significant
association strength, while semantic validation was performed
to assess the relevance of these patterns to the conceptual
structures known in Islamic studies. The combination of both
provides an objective as well as contextual foundation for
evaluating the validity of the thematic clusters.
Analysis of the association results reveals thematic rela-
tionships that are consistent with the semantic structure of
hadith. Several rules reflect strong connections within the
theme of worship, such as the relationship between ritual
components and religious practices, while other rule groups
display close relations with the contexts of revelation and
hadith transmission. These connections indicate that word co-
occurrence patterns in hadith texts are not merely linguistic
phenomena, but representations of a network of meanings that
reflect the structure of religious knowledge.
Semantic validation was performed by re-examining the
clustered results against traditional hadith structures, including
the sanad, matan, and the context of message transmission.
The findings show a high degree of alignment between the
formed thematic groups and the common narrative structure
of hadith, such as transmission patterns, worship themes,
and revelation accounts. Thus, the resulting clusters can be
considered structurally and conceptually valid, and relevant
within the context of Islamic studies, particularly in the fields
of hadith and fiqh.
Implicitly, these results indicate that an unsupervised ap-
proach such as Apriori can be used to:
1) Building automatic thematic annotations for religious

--- Page 9 ---

texts based on word co-occurrence.
2) Revealing the structure of meaning within hadith texts
without the need for manual supervision or domain-
based annotation.
3) Serving as a foundation for developing a hadith knowl-
edge graph, in which relationships between entities (such
as ”shalat,“ ”rakaat,“ ”malam,“ ”turun“) are automati-
cally constructed from data co-occurrence.
4) Supporting the development of digital Islamic stud-
ies systems such as thematic hadith search engines,
meaning-based content recommendation systems, or dig-
ital sanad-tracking models.
These findings reinforce the argument that validation based
on a combination of quantitative metrics and Islamic domain
knowledge can produce an analysis that balances data objec-
tivity with depth of meaning. Such an approach allows the
interpretation of results to move beyond the statistical level
and toward a conceptual understanding that is relevant to
the theological values and epistemological structure of Islam.
Thus, data mining–based research not only contributes to the
technical aspects of text analysis but also enriches scientific
methodologies in contemporary Islamic studies.
This dual-validation approach also opens space for cross-
disciplinary collaboration between data scientists and Islamic
scholars or hadith researchers. Such collaboration is essential
to ensure that the interpretation of analytical results remains
aligned with the context of Islamic scholarship without losing
technological accuracy. hadith experts can evaluate the mean-
ing and theological relevance of the associations found, while
data science experts ensure statistical validity and algorithmic
efficiency. This synergy has the potential to create a new re-
search model that is data-driven yet firmly rooted in traditional
scholarly authority.
The validation results indicate a significant potential for
the development of a more adaptive and intelligent digital
ecosystem for Islamic knowledge. With the ability to identify
thematic patterns automatically and verify their validity, data
mining–based systems can serve as a foundation for more
structured and traceable digitalization of religious sources.
Such models may be applied in Islamic learning platforms,
digital fatwa systems, or thematic analysis of the Qur’an and
hadith, thereby expanding public access to religious knowl-
edge that is authentic, contextual, and supported by scientific
evidence.
The integration of computational methods with classical
Islamic studies encourages the emergence of new analyti-
cal frameworks that can respond to contemporary research
challenges. As religious texts continue to be explored within
increasingly digitized environments, the availability of algo-
rithmic tools enables researchers to revisit long-standing dis-
cussions with fresh empirical evidence. This does not replace
traditional interpretative methodologies; rather, it complements
them by offering alternative perspectives that can confirm,
challenge, or refine existing scholarly conclusions. In this
sense, data-driven validation becomes a catalyst for method-
ological renewal while maintaining reverence for authoritative
textual traditions.
The growing relevance of digital methodologies in Is-
lamic scholarship highlights the importance of developing
standardized evaluation protocols to ensure the reliability of
computational findings. Establishing guidelines for integrating
statistical metrics with domain-specific knowledge will help
maintain consistency across studies and reduce interpretative
bias. Such protocols may include criteria for selecting thresh-
old values in association mining, frameworks for semantic
validation by experts, and mechanisms for documenting inter-
pretative justifications. By institutionalizing these standards,
researchers can create a more transparent and reproducible
research environment that strengthens the academic credibility
and long-term sustainability of data-driven Islamic studies.
B. Discussion
The application of the Apriori algorithm to the corpus
of hadith texts in this study opens a new perspective on
non-manual approaches to thematic interpretation of Islamic
sources. The results show that word associations within the
text can serve as strong representations of dominant themes
that are not always explicitly stated but recur consistently
within the semantic structure of hadith narratives.
Supported by high confidence levels and substantial lift
values, indicate a strong semantic connection between the con-
cept of rakaat and the practice of shalat, thereby reinforcing
the construction of meaning within ritual contexts. A similar
pattern appears in the association between references to ayat
and the process of turun, as well as the link between the
act of baca and the text of the ayat. Interestingly, these rela-
tionships form an implicit depiction of the revelation process
without explicitly mentioning terms such as wahyu or Jibril.
This demonstrates that word associations can uncover latent
meaning structures embedded within religious narratives.
These findings illustrate that unsupervised thematic group-
ing using Apriori is not merely a data exploration method
but also a relevant instrument for detecting latent meaning
structures in religious texts. Compared to traditional meth-
ods that require manual annotation or expert labeling, this
approach offers scalability and efficiency while maintaining
interpretive consistency through quantitative metrics such as
support, confidence, and lift.
1) Contribution to Digital Islamic Studies: From the per-
spective of Islamic scholarship, this research contributes to
a methodological shift from manual philological approaches
toward data-driven methods. Findings such as (hadits) →
(cerita) and (cerita) →(kepada) provide a pathway for sys-
tems to understand patterns of hadith transmission (sanad)
without requiring structural formats or predefined tags. This
represents a form of discovery-based knowledge representa-
tion, where meaning is derived from data structures rather than
solely from editorial structures.
Furthermore, the successful identification of themes such as
worship, revelation, and hadith transmission through word as-
sociations brings hadith studies closer to systematic text-based

--- Page 10 ---

methodologies, without diminishing the conceptual depth em-
bedded within the content. This demonstrates that the approach
aligns with the needs of modern society in accessing religious
sources that are accurate, fast, and logically traceable.
A data-driven approach in hadith studies also opens oppor-
tunities for integrating Islamic sciences with computer science,
especially in the fields of text mining and natural language
processing (NLP). With algorithmic analysis of hadith corpora,
researchers can trace semantic relationships between words
or phrases that were previously difficult to identify using
manual methods. This integration enriches Islamic scholarship
by adding quantitative and analytical dimensions capable of
uncovering hidden patterns within religious texts.
The application of this method further strengthens the
validity of hadith research by providing an empirical basis
for hypothesis testing. For example, the consistent appearance
of certain word patterns within specific chains of transmitters
(sanad) can serve as indicators of authenticity or highlight the
linguistic tendencies of particular narrators. Thus, the research
is not only descriptive but also contributes verifiable insights
to the Islamic scholarly tradition, consistent with the classical
methods developed by hadith scholars in sanad and matan
criticism.
This methodological transformation affirms that Islamic
scholarship has significant potential to adapt to modern sci-
entific paradigms. Using data as the foundation for analysis
is not a form of secularization of knowledge, but rather an
innovative step to strengthen the epistemology of Islam so
that it remains relevant in the digital era. When utilized
appropriately, technology can deepen, structure, and broaden
the study of hadith across disciplines without compromising
its spiritual value or the authenticity of its sources.
2) Relevance to the Initial Problem: This research orig-
inated from the urgent need to address the highly manual
and inefficient methods of thematic analysis in hadith studies.
By applying the Apriori algorithm, the process of extracting
themes from hundreds or even thousands of hadiths can be
performed automatically, paving the way for an automated
thematic annotation system. Furthermore, the findings of this
study demonstrate that the associations discovered can be
validated against the knowledge structures inherent in hadith
studies, indicating that this approach is not only technical but
also epistemological.
Thus, the initial goal of the research—to provide an ef-
ficient, objective, and scalable thematic system—has been
achieved, while also yielding additional findings in the form
of latent meaning relationship patterns that were previously
undetectable through explicit approaches.
3) Relevance to SDG 4 – Quality Education: From a socio-
educational perspective, this approach has direct implications
for the Sustainable Development Goals (SDG) 4: Quality Edu-
cation. The findings enable the development of more inclusive,
technology-based Islamic learning systems, such as automated
thematic hadith search platforms, applications for teaching
hadith meanings in contextualized ways, or digital tools for
teachers and students in Islamic boarding schools (pesantren).
By utilizing data mining techniques to provide accurate and
easily accessible religious knowledge, this research bridges
the classical Islamic scholarly tradition with contemporary
technology.
Despite its significant potential, this approach has several
limitations:
1) Syntactic Context Reduction
Apriori does not take word order or grammar into
account. As a result, the associations formed are at a low
semantic level and do not reflect syntactic or pragmatic
relationships within the hadith texts.
2) Possibility of Spurious Associations
Some rules, even though they meet the metric thresholds,
still carry the risk of containing random associations
that are conceptually irrelevant. This necessitates expert
validation to ensure the quality of the meaning.
3) Scalability Constraints
In very large hadith datasets, the computational com-
plexity of Apriori can become a practical bottleneck,
particularly when generating a large number of rules that
are difficult to analyze manually.
With semantic validation and thematic clustering applied
in this study, the majority of the rules have been shown to
be conceptually sound and relevant to the meaning structures
within hadith studies.
In the future, this approach can be further developed by:
1) Integration with word embeddings (e.g., Word2Vec,
BERT) to capture associations based on semantic vector
representations.
2) Utilization of a knowledge graph to connect hadith
entities conceptually and hierarchically..
3) Development of an automatic labeling (auto-annotation)
system that can assist students and researchers in in-
stantly accessing hadith themes based on inter-concept
relationships.
This data-driven approach demonstrates that Islamic studies
have considerable potential to transform toward more empir-
ical and measurable methodologies. The use of algorithms
such as Apriori provides a foundation for establishing an
objective analytical framework for hadith texts, allowing the
knowledge obtained to be not only interpretative but also
verifiable through data. This transformation strengthens the
position of Islamic studies in the digital era by balancing
scientific accuracy with the depth of theological meaning.
The application of this method also contributes to the mod-
ernization of Islamic education curricula. hadith content can
be presented interactively and contextually through visualiza-
tions of thematic relationships, concept networks, or semantic
maps between hadiths. Such innovations have the potential to
enhance digital literacy among students in pesantren as well as
Islamic academics, while also broadening access to authentic
sources of knowledge that have traditionally been dispersed
across thousands of classical texts. Integrating text analysis
technology with classical scholarship can reinforce scientific

--- Page 11 ---

thinking in understanding Islamic teachings in a rational and
profound manner.
Further development opportunities for this research lie in
building a collaborative and open digital ecosystem for Islamic
knowledge. By combining data mining, natural language pro-
cessing, and validation within the domain of Islamic schol-
arship, the resulting intelligent system can support interdis-
ciplinary research—ranging from hadith studies and tafsir to
Islamic history. Such development not only promotes research
efficiency but also expands public access to organized, trace-
able Islamic knowledge while maintaining the authenticity of
its scholarly sources.
V. CONCLUSION
This study demonstrates that an unsupervised approach
based on the Apriori algorithm is capable of systematically
and objectively extracting thematic knowledge from a cor-
pus of hadith texts. Through word association analysis, the
system successfully forms rules reflecting significant semantic
relationships, such as the connection between the concepts of
”shalat“ and ”rakaat,“ ”malam,“ and ”diri,“ as well as the
relationship among ”ayat,“ ”turun,“ and ”baca,“ which denote
narratives of revelation. These findings confirm that semantic
relationships can be detected through co-occurrence patterns,
even without manual annotation or expert supervision.
The main contributions of this research lie in two aspects.
First, methodologically, this approach fills a gap among pre-
vious studies that still relied on manual labeling or super-
vised classification methods. Second, in terms of content, the
obtained associations approximate the conceptual structures
known in hadith studies, such as matan, sanad, and the
contexts of worship and prophethood, with strong semantic
validation through lift and confidence metrics.
Nevertheless, there are several limitations to note. The Apri-
ori approach does not consider syntactic structure or sentence
order, and thus cannot fully capture the complexity of meaning
within the construction of hadith sentences. In addition, the
potential formation of spurious or coincidental associations
still requires expert involvement during the interpretive stage.
Practically, this research opens the way for developing ap-
plications based on thematic understanding of hadiths, ranging
from automatic annotation systems, theme-based navigation, to
the construction of Islamic knowledge graphs. In the context of
Islamic education and digital literacy, this approach supports
inclusive, standardized, and efficient learning, in line with
Sustainable Development Goal (SDG) 4.
For future development, this research can be expanded
through integration with semantic representations based on
word embeddings, topic modeling, or graph-based learning,
enabling the exploration of meaning to encompass more
complex syntactic, pragmatic, and historical contexts within
hadith texts.
ACKNOWLEDGMENT
The author’s wishes to acknowledge the Informatics De-
partment UIN Sunan Gunung Djati Bandung, which partially
supports this research work.
REFERENCES
[1] U. Noor, “The revival of hadith study in modern time,” 10 2020, pp.
711–719.
[2] A. Ramponi and B. Plank, “Neural unsupervised domain adaptation in
nlp—a survey,” in Proceedings of the 28th International Conference
on Computational Linguistics.
Stroudsburg, PA, USA: International
Committee on Computational Linguistics, 2020, pp. 6838–6855.
[3] R. Alfianzah, R. I. Handayani, and M. Murniyati, “Implementation of
apriori algorithm data mining for increase sales,” SinkrOn, vol. 5, no. 1,
p. 17, oct 2020.
[4] N. A. Hibnastiar, A. F. Setiawan, and E. H. Susanto, “Penerapan algo-
ritma apriori dalam menentukan rekomendasi paket produk,” MALCOM:
Indonesian Journal of Machine Learning and Computer Science, vol. 5,
no. 1, pp. 321–331, jan 2025.
[5] B.
Doskarayev,
N.
Omarov,
B.
Omarov,
Z.
Ismagulova,
Z. Kozhamkulova, E. Nurlybaeva, and G. Kasimova, “Development
of computer vision-enabled augmented reality games to increase
motivation for sports,” International Journal of Advanced Computer
Science and Applications, vol. 14, no. 4, 2023. [Online]. Available:
http://dx.doi.org/10.14569/IJACSA.2023.0140428
[6] F. F. Wahid, S. K, R. G, D. Swain, B. Acharya, and M. R. Pradhan,
“A novel threshold based method for vessel intensity detection and
extraction from retinal images,” International Journal of Advanced
Computer Science and Applications, vol. 12, no. 6, 2021. [Online].
Available: http://dx.doi.org/10.14569/IJACSA.2021.0120663
[7] D.-N.-M. Do, L.-K. Hoang, C.-M. Le, and T. Tran, “A human rights-
based approach in implementing sustainable development goal 4 (quality
education) for ethnic minorities in vietnam,” Sustainability, vol. 12,
no. 10, p. 4179, may 2020.
[8] T. Ferguson and C. G. Roofe, “Sdg 4 in higher education: challenges
and opportunities,” International Journal of Sustainability in Higher
Education, vol. 21, no. 5, pp. 959–975, jun 2020.
[9] Y. Sayed and K. Moriarty, “Sdg 4 and the ‘education quality turn’,” in
Grading Goal Four.
BRILL, 2020, pp. 194–213.
[10] I. B. Franco and E. Derbyshire, “Sdg 4 quality education,” in Envisioning
Futures for Environmental and Sustainability Education, 2020, pp. 57–
68.
[11] A. J. Alhasan and N. Surantha, “Evaluation of data center network
security based on next-generation firewall,” International Journal of
Advanced Computer Science and Applications, vol. 12, no. 9, 2021.
[Online]. Available: http://dx.doi.org/10.14569/IJACSA.2021.0120958
[12] R. A. Raja, N. Yuvaraj, and N. V. Kousik, “Analyses on artificial
intelligence framework to detect crime pattern,” in Intelligent Data
Analytics for Terror Threat Prediction.
Wiley, 2021, pp. 119–132.
[13] N. P. Dharshinni, F. Azmi, I. Fawwaz, A. M. Husein, and S. D. Siregar,
“Analysis of accuracy k-means and apriori algorithms for patient data
clusters,” in Journal of Physics: Conference Series, vol. 1230, no. 1, jul
2019, p. 012020.
[14] P. M. S. Tarigan, J. T. Hardinata, H. Qurniawan, M. Safii, and R. Winan-
jaya, “Implementasi data mining menggunakan algoritma apriori dalam
menentukan persediaan barang: Studi kasus: Toko sinar harahap,” Jurnal
Janitra Informatika dan Sistem Informasi, vol. 2, no. 1, pp. 9–19, 2022.
[15] D. Nurmalasari and H. R. Yuliantoro, “Implementasi ekstraksi fitur
untuk pengelompokan dokumen proposal menggunakan algoritma na¨ıve
bayes,” Jurnal Komputer Terapan, vol. 8, no. 1, p. 473014, 2022.
[16] K. P. Sinaga and M.-S. Yang, “Unsupervised k-means clustering algo-
rithm,” IEEE access, vol. 8, pp. 80 716–80 727, 2020.
[17] Z. Shao, Y. Li, X. Wang, X. Zhao, and Y. Guo, “Research on a new
automatic generation algorithm of concept map based on text analysis
and association rules mining,” Journal of Ambient Intelligence and
Humanized Computing, vol. 11, no. 2, pp. 539–551, Feb. 2020.
[18] N. S. Az-zahra and Z. Fatah, “Implementasi algoritma apriori pada
analisis pola penjualan sepatu,” Jurnal Riset Teknik Komputer, vol. 1,
no. 4, pp. 73–79, 2024.
[19] M. R. Yudhatama, A. Wijaya, D. Abdullah, and A. Sonita, “Pener-
apan metode association rule menggunakan apriori untuk rekomen-
dasi penyusunan rak buku di perpustakaan universitas muhammadiyah
bengkulu,” Jurnal Multidisiplin Dehasen (MUDE), vol. 3, no. 3, pp.
163–168, 2024.
[20] A. M. Alinafiah, B. C. Octariadi, and S. Sucipto, “Implementasi impe-
mentasi data mining dalam pengelolaan stok obat menggunakan metode
k-means clustering dan asossociation rules apriori: Analisis pola pem-
belian dan hubungan antar obat dalam pengelolaan stok menggunakan

--- Page 12 ---

k-means clustering dan association rules apriori,” Jurnal Informatika
Polinema, vol. 10, no. 4, pp. 551–558, 2024.
[21] W. B. Zulfikar, A. Wahana, W. Uriawan, and N. Lukman, “Implementa-
tion of association rules with apriori algorithm for increasing the quality
of promotion,” in 2016 4th International Conference on Cyber and IT
Service Management, 2016, pp. 1–5.
[22] D. Nurhidayanti and I. Kurniawati, “Implementasi algoritma apriori
dalam menemukan association rules pada persediaan sparepart motor,”
Innovation
in
Research
of
Informatics
(INNOVATICS),
vol.
4,
no. 2, pp. 62–67, 2022, accessed: 2025-11-05. [Online]. Available:
https://jurnal.unsil.ac.id/index.php/innovatics/article/view/5300
[23] A. H. Asy’ari, M. H. Muzakki, and M. Hanafi, “Clusterization model of
hadith topic in bukhari muslim hadith using bert algorithm,” in 2024
6th International Conference on Cybernetics and Intelligent System
(ICORIS), 2024, pp. 1–6.
[24] A. Adiwijaya, S. A. Faraby, M. S. Mubarok, and M. D. Purbolaksono,
“Indonesian Translation of the Hadith of Bukhari (Single-label),” 2022.
[Online]. Available: https://doi.org/10.34820/FK2/GWSEWB
[25] R. Lischner, “Case-folding,” in Exploring C++ 11: Problems and
Solutions Handbook.
Springer, 2014, pp. 111–113.
[26] M. A. Rosid, A. S. Fitrani, I. R. I. Astutik, N. I. Mulloh, and H. A.
Gozali, “Improving text preprocessing for student complaint document
classification using sastrawi,” in IOP Conference Series: Materials
Science and Engineering, vol. 874, no. 1.
IOP Publishing, 2020, p.
012017.
[27] M. Bougar and E. H. Ziyati, “Addressing stemming algorithm for arabic
text using spark over hadoop,” in International Conference on Advanced
Intelligent Systems for Sustainable Development.
Springer, 2019, pp.
74–82.
