---
title: "2024-University-Using LLMs to Discover Emerging Coded - PDF Extract"
source_pdf: "2024-University-Using LLMs to Discover Emerging Coded.pdf"
pages: 9
extracted_at: "2026-02-13T09:15:44.836795"
---

# PDF Extract: 2024-University-Using LLMs to Discover Emerging Coded

**Source PDF:** 2024-University-Using LLMs to Discover Emerging Coded.pdf
**Total Pages:** 9

---

## Content

```
--- Page 1 ---

Using LLMs to discover emerging coded
antisemitic hate-speech in extremist social media
Dhanush Kikkisetti, Raza Ul Mustafa, Wendy Melillo, Roberto Corizzo, Zois Boukouvalas, Jeff Gill, Nathalie Japkowicz
American University, 4400 Massachusetts Ave NW, Washington, DC 20016, USA
{vk4372a,rmustafa,melillo,rcorizzo,boukouva,jgill,japkowic}@american.edu
Abstract—Online hate speech proliferation has created a diffi-
cult problem for social media platforms. A particular challenge
relates to the use of coded language by groups interested in both
creating a sense of belonging for its users and evading detection.
Coded language evolves quickly and its use varies over time.
This paper proposes a methodology for detecting emerging coded
hate-laden terminology. The methodology is tested in the context
of online antisemitic discourse. The approach considers posts
scraped from social media platforms, often used by extremist
users. The posts are scraped using seed expressions related
to previously known discourse of hatred towards Jews. The
method begins by identifying the expressions most representative
of each post and calculating their frequency in the whole
corpus. It filters out grammatically incoherent expressions as
well as previously encountered ones so as to focus on emergent
well-formed terminology. This is followed by an assessment of
semantic similarity to known antisemitic terminology using a
fine-tuned large language model, and subsequent filtering out
of the expressions that are too distant from known expressions
of hatred. Emergent antisemitic expressions containing terms
clearly relating to Jewish topics are then removed to return only
coded expressions of hatred.
Index Terms—hate speech, coded antisemitic terminology
I. INTRODUCTION
Online hate speech detection1 is a complex problem for
social media platforms. A particular challenge, not much
discussed in the literature, relates to the use of coded language.
The following post illustrates the issue in the context of
antisemitic hate speech:
“Nope Globalist want us intertwined and run by the
elites, Globalist don’t lay tariffs on their friends you
stupid fu****”. [posted on Dec. 31, 2022, on the
Disqus platform ]
According to the American Jewish Committee (AJC) Translate
Hate Glossary2, a globalist, in its unbiased definition, is
“a person who advocates the interpretation or planning of
economic and foreign policy in relation to events and devel-
opments throughout the world”. According to this definition,
the term is rather flattering. Indeed, that is the way it is
intended in the Hyatt hotel’s welcoming message to its club
members seen in Figure 13. In that commercial context a
Research supported by American University’s Signature Research Initiative
program. We thank Jacob Levine for his inspiration in the initial steps of this
project.
1Warning: Some of the paper’s content may be disturbing to the reader.
2https://www.ajc.org/translatehate/globalist
3Photo by one of the authors on 11/3/23 at a Hyatt Texas property.
Fig. 1. Non antisemitic use of the term ”globalist”
globalist refers to someone “who gets it!” and should feel
good about it! The term does not, in any way, refer to Jews.
Yet, the AJC Translate Hate Glossary argues that the term
has an antisemitic connotation when it “is used to promote
the antisemitic conspiracy that Jewish people do not have
allegiance to their countries of origin, like the United States,
but to some worldwide order—like a global economy or
international political system—that will enhance their control
over the world’s banks, governments, and media”. In the above
post, it is clear that the antisemitic connotation is implied.
From this post, we surmise that
1) The globalists (a.k.a., the Jews) are distinct from “us”,
presumably, the good American citizens;
2) They control “our” fate to be run by the elites (a subset
of these Jews)4;
3) They help each other by not imposing the same tariffs
on each other as those they impose on “us”.
The above post, thus has a double meaning. To a recipient
who is unaware of its antisemitic connotation, some category
of people, the globalists, do not seem to behave very nicely.
Yet, to an informed audience, it is a very pointed post that
reiterates old Nazi and Soviet anitisemitic propaganda5 and
propagates it further. Furthermore, on social media platforms,
4“Elite” appears in the AJC Glossary in the context of “Cosmpolitan Elite”:
““Cosmopolitan” and “elite” are terms that have separately incited antisemites
across the political spectrum. Based on stereotypes of Jewish wealth and
insularity, Jews have been accused of being part of an elite class for centuries.”
5c.f. “Globalist” and “Cosmopolitan Elite” in the AJC Glossary.
arXiv:2401.10841v2  [cs.CL]  23 Jan 2024

--- Page 2 ---

it does so without setting off any serious alerts since, except
for the “stupid fu****” mention, which could raise a flag, no
offensive terms are used.
Though the usefulness and importance of catching such
subtle posts and their impact on society beyond the small
extremist groups they are primarily intended for are important
subjects that we debate elsewhere, this paper is concerned with
the automatic discovery of “coded” terms similar to globalists
and cosmopolitan elite which carry both a “regular” and an
antisemitic connotation depending on the context in which they
are used. Such an automated process is necessary due to the
fact that coded terminology evolves rapidly online and fixed
glossaries such as the AJC glossary become quickly outdated.
In addition, due to the large volume of posts appearing on
social media, human monitoring cannot be performed without
the assistance of automated tools pointing them in the right
direction. The purpose of our approach is just that: to create an
automated monitoring tool to assist human monitors by sug-
gesting emerging, potentially coded, antisemitic terminology,
along with the posts that use that terminology.
Though the topic of hate speech is, unfortunately, quite vast,
this study focuses on antisemitism. The choice of a particular
category of hate speech comes from our belief that we can
perform a more thorough analysis of the problem by remaining
focused. Antisemitism was selected because of the reported
increase in antisemitic incidents in the months preceding the
beginning of this study, in 2022. The lessons learned from
this particular study will apply to other categories of hatred
including hatred against Black, Muslim, Asian, and LGPTQ+
populations amongst others.
The main contribution of this paper is a methodology
for the novel problem of extracting emerging coded hate-
laden terminology (antisemitism, in this paper) from extremist
social posts, along with a practical pipeline to demonstrate
its effectiveness. The methodology is based on the hypothesis
that coded antisemitic terminology begets coded antisemitic
terminology. In other words, those who use coded termi-
nology to remain under the radar of social media monitors
will, when not able to express new ideas with existing coded
terms, derive or invent new ones. Based on this hypothesis, we
harvest terminology used in similar contexts as known coded
antisemitic terminology and propose it as potential emerging
antisemitic coded terminology to human monitors, along with
the context in which that terminology occurs. We propose
four different versions of our pipeline and validate them using
a quantitative approach. The most advanced version is also
evaluated qualitatively. We conclude with a discussion of our
approach’s practical utility.
The remainder of the paper is structured as follows: Section
II presents background and related work. In Section III, we
discuss data preparation matters. Next, the methodology and
pipeline for extracting coded terminology is introduced in
detail in Section IV. This is followed by a presentation and
discussion of the results in Section V. Finally, Section VI
concludes the paper and discusses future work.
II. BACKGROUND AND RELATED WORK
With the advent of the internet and social media, technology
has increased the speed at which language evolves. Propaganda
in the form of hate speech now travels the world at such a fast
pace that it is beyond human capacity to keep up with. Harmful
words take on new meanings in both direct and coded ways,
inciting hatred in the minds of those only too willing to believe
them as they reinforce and justify preexisting prejudices.
A. Machine Learning Methods for Hate Speech Detection
In recent times, there has been a notable rise in hate
crimes across the United States.6 While establishing a clear
relationship between hate crimes and online content is not
straightforward, a report by the US Department of Justice
points to the simultaneous purchases of Facebook ads contain-
ing dividing content and hate crime. These two reports7 thus
suggest that hate speech should not be considered harmless,
and coming up with methods to curb it is an important goal.
Previous work aims to detect hate speech from social media
using various Machine Learning (ML) methods as documented
by a number of surveys written in the last six years [1]–[4].
One of the most recent surveys shows that while up to 2016,
fewer than 10 papers were published on the topic each year,
since then, there has been a huge increase in interest in the
topic with over 150 papers published in 2020, the last year
for which their survey had complete information [4]. Hate
speech detection has been attempted using a wide variety of
techniques and applied to many different problems. Founta et
al. [5], for example, used Recurrent Neural Networks (RNN) to
classify racism and sexism. Serr`a et al. [6] showed that charac-
ter level based Long Short-Term Memory networks (LSTMs)
for abusive language detection could be useful. Similarly,
Convolutional Neural Networks (CNNs) have also been shown
to be successful in hate speech detection and classification
[7]. More recently, large language models have been used for
these tasks like in the work of [8] who propose different fine-
tuned and non-fined-tuned variations of pre-trained models
such as BERT, RoBERTa, ALBERT, etc. on offensive language
detection. Most of these studies, however, consider hate speech
as a whole and, typically, do not distinguish the community
towards which it is directed. We feel that this generalized
approach is too broad and decided, instead, to use a divide-
and-conquer approach by focusing on particular communities
separately. Our first attempt focused on the Jewish community
and the problem of antisemitic speech in social media.
B. Antisemitism in Social Media and its Detection
Antisemitism specifically targets Jewish individuals or the
Jewish community [9]. In [10], authors use the outcomes of
two surveys from EU and ADL to assess how the level of
antisemitism relates to the perception of antisemitism by the
Jewish community in eight different EU countries. A recent
6https://bjs.ojp.gov/library/publications/hate-crime-recorded-law-enforcement-2010-2019
7(1)
https://bit.ly/2xeeF5h;
(2)
https://www.ojp.gov/pdffiles1/nij/grants/
304532.pdf

--- Page 3 ---

survey finds that 20% of American Jewish adults have expe-
rienced an act of antisemitism, such as an attack either online
or on social media.8 In another study, the authors address the
challenges of quantifying and measuring online antisemitism.
It raises the question of whether the number of antisemitic
messages is increasing proportionally to other content or if the
share of antisemitic content is rising. Additionally, the paper
aims to determine the extent of online Jew-hatred beyond well-
known websites, forums, and closed social media groups [11].9
A few studies have attempted to combat online antisemitism
in a way similar to the way in which generalized hate speech
has been countered in the works discussed in the previous
section. In [12], for example, the authors prepared a data
set that includes both social posts and associated images,
when available. They labeled the entries as antisemitic or
not, and if antisemitic, indicated the kind of antisemitism:
political, economic, religious or racial. They used a bimodal
deep learning approach for classifying the data into these
categories. [13] considers a subset of the text-only part of
this datasetin an attempt to classify antisemitic posts using a
less computationally-intensive approach. Focusing on the class
imbalance problem in the data while taking advantage of Ope-
nAI’s GPT technology, they compared GPT-based resampling
techniques against other traditional kinds. Very recently, [14]
proposed a new data set for antisemitism detection in social
media posts that uses a strict annotating process. The data
set is so recent, however, that it has not yet been used for
classification or the results obtained on such efforts have not
yet been published. There are other projects that consider the
detection of online antisemitism using AI approaches as well.
In particular, the project entitled “Decoding Antisemitism”10
calls itself an “AI-driven Study on Hate Speech and Imagery
Online”, and already produced five published reports on the
subject. The project specifically aims at linking national or
international events reported in the traditional media to anti-
semitic online social media discussions.
C. Alternatives to automated hate speech detection
In [15], the authors question whether the way in which hate
speech detection has been handled by the machine learning
community is the way forward, or whether hate speech detec-
tion is a lot more complex than previously assumed by the
researchers who labeled data sets and applied classifiers to
them. Furthermore, the authors note that some hateful content
may occur without the use of well-known slurs and that on
top of it all, the nature of hate speech is constantly evolving.
In contrast to previous studies, our work takes these observa-
tions into consideration and focuses on identifying emerging,
potentially coded terms related to antisemitism using NLP
methods. There has been a lack of rigorous research in finding
emerging antisemitic coded terms that can lead to the detection
of hate speech and, perhaps, subsequently, to the prevention of
hate crimes. This paper aims to bridge this gap and provide an
8https://bit.ly/41FV6ei
9These studies preceded 10/7/23 when the situation worsened drastically.
10https://decoding-antisemitism.eu/
Known Antisemitic
Terms
Extract raw data
Data scrapping
Extremist Social Media Platforms
Important Terms
Extraction
Generate Fine-Tuned
LLM Embeddigs for the
context in which the
term is used
Weighted
Context
Similarity
Score
Extract Trending
Antisemitic Terminology
Fig. 2. Emergent Coded Antisemitic Terminology Extraction Pipeline
approach for the detection of emerging antisemitic, sometimes
coded, terminology used on extremist social media platforms.
III. DATA PREPARATION
This study is part of a large multi-disciplinary project
sponsored by our institution which, simultaneously, collects
and analyzes the use of coded language to express antisemitic
sentiment in lightly moderated social media platforms typi-
cally preferred by individuals with extremist tendencies and
studies the migration of this language from these extremist
platforms to the general population. The overall project in-
cludes a data team, a population team, and a software team
which collaborate closely and work in parallel. The pipeline
illustrating our proposed methodology is shown in Figure 2.
A. Dataset
The project is constantly evolving, though for this study,
we considered the first delivery of the data curated by the
data team in June 2023. The data team’s objectives concerning
this study was to analyze the usage of antisemitic terms.
We describe the data gathering and cleanup methodologies
summarized by the 3 leftmost components in Figure 2.
1) Data Scraping and Labeling: To build the corpus, the
data team analyzed antisemitic social media posts from various
extremist social media platforms including Discuss, Telegram,
Minds, and GETTR. It used antisemitic expressions obtained
from the previously mentioned American Jewish Commit-
tee (AJC) Translate Hate Glossary as well as the Southern
Poverty Law Center (SPLC) to collect social media posts.
This collection effort was facilitated by Pyrra11, a private
software company that allows its users to scrape posts from
alt-social media platforms according to a list of seed terms.
The data team considered the 46 seed expressions available
from the AJC Glossary at the time as well as the term “Cultural
Marxism”, discussed in a SPLC article12 and chose 16 of them
to make the process tractable. It analyzed the 659 retrieved
posts related to these seed expressions to determine whether
11https://www.pyrratech.com/
12https://www.splcenter.org/fighting-hate/intelligence-report/2003/
cultural-marxism-catching

--- Page 4 ---

the post was antisemitic or not.13 The 16 terms used in the
subset were selected based on their potential to reveal posts
that had emerging new antisemitic terms in them. The list
of seed words used is: Cabal, Cosmopolitan Elite, Cultural
Marxism, Deicide, The Goyim Know, Holocough, Jewish Cap-
italist, Jewish Communist, Jew Down, Jewish Lobby, New
World Order, Not the Real Jews, Rothschild, Soros, Zionist,
and Zionist Occupied Government. Since the distribution of
posts with respect to each seed expression is not ideal, though
the software team used all the posts retrieved from the 16
seed expressions, it used only the seed expressions with at
least 5 posts related to them to conduct its analysis. The terms
dropped from the list according to this criterion are Jew Down
and Cosmopolitan elite, leaving us with 14 seed words for the
remainder of the study.
2) Preprocessing: Text preprocessing is a critical step in
Natural Language Processing (NLP). It involves transforming
raw text data into a format that can be easily analyzed by
machine learning algorithms. The preprocessing steps usually
used involve several techniques, such as tokenization, stop
word removal, stemming, and lemmatization [16]. During the
first phase of cleaning the corpus, we removed the urls
and lower-cased all the posts to normalize them. This initial
procedure was followed by stop words removal. Then we
lemmatized the text to get a single root form for each word
prior to passing it on to the coded antisemitic terms extraction
process, which will be discussed in the next section. Bigrams
and trigrams were formed by running two- and three- word
windows through all the posts.14 It was important to filter
out badly-formed expressions obtained through that approach.
In particular, we decided to include bigrams and trigrams
that only contain nouns, proper nouns, adjectives, and verbs,
since others were judged less relevant to our quest.Since the
emphasis of this study is on the novel proposed extraction
process discussed next, we did not experiment with the various
pre-processing techniques suggested in the literature on hate
speech for social media posts [17]. It was left for future work.
IV. CODED ANTISEMITIC TERMS EXTRACTION APPROACH
As previously mentioned, the purpose of this study is the
extraction of emerging coded antisemitic terms. In order to
carry out this goal, we designed a method for operationalizing
each term of that expression. That operationalization and the
linking of its resulting components into a functional system
constitute the main contribution of this work. The purpose
of this section is to discuss the process. To begin with, we
consider each word in the emerging coded antisemitic terms
expression and give it the specific meaning shown below.
• Terms: the extracted expressions are limited to grammat-
ically consistent bigrams and trigrams; they have to be
relevant enough to the documents in which they appear
and appear frequently enough in the corpus.
13A copy of the coding statement is available upon request.
14We also considered unigrams but were not able to filter them effectively
using our current methodology. Their treatment was left for future work.
• Antisemitic:
the candidate expressions have to be se-
mantically related to antisemitic discourse.
• Coded: antisemitic expressions that contain terms relat-
ing to obvious Jewish concepts are removed.
• Emerging: already known coded antisemitic expressions
are removed in order to concentrate on new terminology.
These operations are divided into two phases. In Phase 1, we
address the extraction of emerging coded terminology without
worrying about its semantic relation to antisemitism. In Phase
2, we address semantics using large language models. Phase 1
is represented by the “Important Terms Extraction” component
in Figure 2. Phase 2 is represented by the combination of the
LLM Generation, Similarity Scoring, Antisemitic Terminology
Extraction, and Monitoring components in Figure 2. Both
phases of the pipeline are implemented using two approaches:
a standard solution and an advanced solution. We subse-
quently test all four combinations, yielding a baseline approach
composed of two standard solutions, two hybrid approaches
composed of one standard and one advanced solution, and
one advanced approach composed of two advanced solutions.
A. Phase 1: Emerging Coded Trending Terms Extraction
For the first part of Phase 1, the extraction of trending terms,
we explore the use of off-the-shelf NLP tools for our standard
solution and then propose our advanced solution that combines
tf-idf and frequency. Once the trending terms are extracted, we
propose a strategy to remove non-emerging and non-coded
terms from the list of extracted terms. This strategy is applied
to both the standard and advanced solutions.
1) Standard Solution: Trending Terms Extraction using
Concordance and Collocation tools: In this first attempt at
trending terms extraction, we use traditional NLP techniques to
extract bi-grams and tri-grams using concordance and colloca-
tion algorithms from the NLTK Toolkit [18]. Concordance is a
technique that provides a comprehensive view of how a given
term appears in a corpus. Using this approach, we use the
14 seed terms from Section III-A1 for analyzing patterns and
gaining insights into language usage. For each occurrence of a
seed term, this approach provides the surrounding words con-
text. We use default settings for the extraction of context. Next,
using collocation, we find the most frequent bi-grams and tri-
grams in the collected contexts. Collocation is a technique that
finds a meaningful combination of words from a corpus that
are semantically coherent. Different statistical measures can
be used to detect collocations including frequency, pointwise
mutual information (PMI), and log-likelihood ratio (LLR)
among others. We use frequency, here since that is the measure
also used in the advanced approach In the future, we plan to
experiment with other statistical measures for both approaches.
The standard approach yielded 126 trending terms.
2) Advanced Solution: Trending Terms Extraction using
TF-IDF and Frequency: Our proposed advanced approach
is presented in Algorithm 1 which uses TF-IDF feature-
weighting [19] and frequency to extract trending terms. In a
nutshell, this was done by selecting all the terms that obtained
a TF-IDF value greater than a self-set threshold, listing these

--- Page 5 ---

terms in decreasing order of frequency, and selecting the top
200 terms from the list.15 When the same term appeared in
several documents, the highest TF-IDF value it received was
retained Algorithms 1 shows the approach that was followed
in detail. The algorithm is explained line by line next.
Algorithm 1 Trending terms extraction
1: Initialize Trending terms ▷Stores top 200 trending terms
2: Initialize Ds
▷Stores terms’ highest TF-IDF scores (s)
3: Initialize Df
▷Stores terms’ values and frequencies
4: Set T
▷Stores all the vocabulary terms (value).
5: Set F ▷Stores the frequency of each term in the corpus.
6: Calculate the TF-IDF scores for each term in each doc-
ument and store them in matrix W ∈Rd×v, where
d denotes the number of documents and v denotes the
vocabulary size.
7: for each term t in T do
8:
for each row in W do
▷Each row is a document
9:
Ds[t] ←max(Ds[t], W[row, t])
▷Finds t’s
highest TF-IDF score, s, across all documents
10:
end for
11: end for
12: δ ←Average(Ds)
▷δ is the average of all s’s
13: i = 1
14: for each t in Ds do
15:
if Ds[t] ≥δ then
16:
Df[i] ←(T[t], F[t])
▷If t’s
highest TF-IDF score is larger than threshold δ, store t’s
value and frequency in Df
17:
i = i + 1
18:
end if
19: end for
20: Sort Df in descending order of frequency
21: for i = 1, 2, . . . , 200 do
22:
Trending terms ←Df[i][T]
▷Store the most
frequent terms in Trending terms (drop the frequencies)
23: end for
The
algorithm
begins
by
initializing
the
Trending_terms list which is the list that will return the
200 bigrams and trigrams (terms) that received the highest
combination of TF-IDF and Frequency scores. Next, Ds
and Df are also initialized. Ds will be used to store all the
terms’ highest TF-IDF scores, whereas Df will store all
the terms and their associated frequencies. Since terms are
subsequently referred to according to their indices, T, which
is set next, serves as the reference vector that associates
an index with the actual value of the term (i.e., the actual
bigram or trigram). Next, the frequency of each term in
the corpus is calculated and saved in vector F. The TF-IDF
values obtained for each unique term and each document are
then calculated and placed in the matrix W of size d x v
where d represents the number of documents whereas, v is
the number of terms.
15We assume that at least 200 terms had a TF-IDF value larger than the
self-set threshold.
On lines 7-11, we take each term in matrix W and find the
highest score across all the rows (documents) of the matrix
and store it in Ds. To remove the less relevant terms, we
compute the average of all the values in Ds and use this value,
δ, as a threshold. This allows us to consider only the terms
with TF-IDF values greater than the average value of all the
scores in Ds. δ is calculated on line 12. On lines 13-19, we
check if the terms’ TF-IDF value is greater than δ. If so, we
save the terms’ values and their frequencies in Df. Finally, on
line 20, we sort the terms in Df in descending order of their
frequency values and select the top 200 terms, storing them
in Trending_terms.
3) Removal Strategy: Redundant, Non-Emergent and Non-
Coded terms Removal: Once the list of most trending terms
have been extracted using either the standard or advanced
solution, three categories of terms are removed from it. First,
as we consider expressions that are both bigrams and tri-
grams, there is a possibility of encountering bigrams within
trigrams. Such redundant bigrams are removed from the list
of expressions. Next, we remove the terms that have occurred
earlier. For now, this corresponds to the original list of 16
seed words used to retrieve the posts. In the future, this list
will grow as we intend to use the system continuously, using
newly discovered terms of interest as new seed terms. Lastly,
the terms that are considered non-coded are removed. These
correspond to terms that contain words that obviously pertain
to Jewish themes. The list of words currently used includes
jew, jewish, kike, and zionist. Expressions that include these
words either as stand-alone words or embedded within other
words are removed. After the removal phase is applied, we
are left with 52 and 94 trending terms for the standard and
advanced trending term extraction solutions, respectively.
B. Phase 2: Embeddings and Comparisons
Though the bigrams and trigrams extracted in the previous
section are known to be trending, their semantics are unknown
and, in particular, there is no information as to whether or
not these terms are antisemitic. To find out which of these
trending expressions are antisemitic, we compare the context
in which they are used to the context in which the known
antisemitic expressions are used. If a trending term appears
in contexts similar to those in which seed expressions occur,
it will be deemed antisemitic. Otherwise, it will be discarded
as non-antisemitic. To compute embeddings for the trending
and seed terms, we begin by fine-tuning BERT. Since BERT
was not specifically trained on instances of hate speech or
antisemitism, we fined-tuned it with additional data collected
using the same seed expressions as before (since time elapsed
between the original collection and the new collection, more
posts were available for this exercise). This fine-tuned version
of BERT is then used to generate contextual embeddings for
both the trending terms discovered in the last section and the
seed terms used to extract posts. We present the details of
BERT’s fine-tuning followed by the standard and advanced
embedding solutions we implemented.

--- Page 6 ---

Term
Word
Context words in window of size 5
Surronding context
Surronding context
Word
Word
Word
Word
Word
Word
Word
Word
Word
W
W-1
W-2
W-3
W-4
W-5
W+1
W+2
W+3 W+4
W+5
Fig. 3. Pre-truncate embedding approach for a window of size 5.
1) Fine-tuning the BERT model: The generalized BERT
model does not possess domain-specific vocabulary, thus it
is not capable of handling coded hate speech such as anti-
semitism. Indeed, when such out-of-vocabulary terms occur,
they get broken down into smaller tokens for which embed-
dings are generated. These are treated as rare tokens, yielding
unsatisfactory results. To avoid this issue, we fine-tune the
BERT model using an additional 56K posts extracted using
the same seed words as before on Pyrra. We, thus, extend
BERT’s vocabulary from 30k to 55k tokens, and fine-tune
it using the Masked Language Modeling (MLM) approach.
MLM is a pre-training approach that masks a few tokens. The
model is subsequently trained to predict the masked tokens
from the words that surround them.16
2) Comparing Trending Terms to Seed Terms: To differ-
entiate between antisemitic and non-antisemitic terms during
Phase 2, we compare the trending terms’ embeddings to the
seed terms’ embeddings using Cosine Similarity. We generate
two types of embeddings following i) the standard pre-truncate
embedding method and ii) the advanced post-truncate embed-
ding method. In pre-truncate embedding, we truncate the post
containing the term to be embedded prior to embedding it. In
post-truncate embedding, we embed the entire post containing
the term of interest, and truncate the resulting embedding
afterwards.17
a) Standard Solution: Pre-truncate embeddings: In this
approach, we consider context windows of 5 to 14 words,
where the size of the windows refers to the twin windows
located before and after the term being embedded, respectively.
We show an example of windows of size 5 in Figure 3.
Since the same term may be found in more than one post,
we concatenate all the embeddings extracted from fine-tuned
BERT using the same window size and take their average.
Embedding, here, refers to the pooled layer obtained
from the 12 layers of the BERT architecture. We follow the
same procedure for all the trending terms we extracted and
the 14 seed words retained in Section III-A1.
Next, we determine the trending terms antisemitic nature
using Algorithm 2. After some initialisations on lines 1-4,
S[tt], the “similarity to antisemitism” value for trending term
tt, is computed as follows: tt’s embedding is compared to
each of the 14 seed terms (the st’s)’s embeddings using Cosine
16https://huggingface.co/learn/nlp-course/chapter7/3
17Since we cannot embed posts exceeding 512 tokens, we turned large posts
into multiple ones.
Similarity as described on lines 6-8. On line 9, the 14 resulting
measurements are averaged and assigned to S[tt] The process
is repeated for each trending term (lines 5-10) and the median
of all the S[tt]’s, γ, is calculated on line 11. γ is then used
as our threshold for potential antisemitism on lines 12-18: if
S[tt] for trending term tt is greater than γ, tt will be given
the partial label “potentially antisemitic” (TT PL w[tt] =
1). Otherwise, it will be given the partial label “probably
not antisemitic” (TT PL w[tt] = 0). (We used the median
as it offered more flexibility than the mean.) Algorithm 2 is
repeated 10 times, once for each window size w considered.
This yields 10 partial labels TT PL w[tt], w = 1 . . . 10 for
each term tt, and the final labeling for tt is “antisemitic” if
m out of the 10 partial labels are “potentially antisemitic”. It
is “not antisemitic”, otherwise. The optimal value of m was
7 for the pre-truncate case.
Algorithm 2 Comparing semantic similarity–window size w
1: Embeddings tt ←{et 1, et 2 . . . , et n}
▷n pre- or
post- truncate trending terms embeddings at window size
w
2: Embeddings st ←{es 1, es 2 . . . , es 14} ▷14 pre- or
post- truncate seed words embeddings at window size w
3: Initialize TT PL w. TT PL w will store the n trending
terms & predicted antisemitic label for window size w.
4: Initialize S. S will store the average semantic score for
each trending term at window size w.
5: for each tt in Embeddings tt do
6:
for each st in Embeddings st do
7:
tt scores[tt] ←Sim(et tt, es st) ▷Cosine Sim
8:
end for
9:
S[tt] ←Average(tt scores[tt]) ▷Average all the 14
semantic scores between tt and all the st’s
10: end for
11: γ ←Median(S)
▷γ is the median of all the scores
12: for each tt in S do
13:
if S[tt] > γ then
▷check if score greater than γ
14:
TT PL w[tt] ←1
▷if score greater than γ
15:
else
16:
TT PL w[tt] ←0
▷if score less than γ
17:
end if
18: end for
b) Advanced Solution:
Post-truncate
embeddings:
In
this approach, we begin by embedding each complete post
using fine-tuned BERT. The approach is illustrated in Figure
4 for the 18-word post AND THE EVIL LYING DEEP
STATE CABAL SATANIC SCUM BAGS ALL NEED TO
BE ROUNDED UP AND EXECUTED. This yields an 18
x 12 x 768 tensor representing the total number of words
in the post, the total number of encoding layers, and their
dimension. This embedding can be thought of as a word
embeddings lookup table that provides complete context for
each post.18 Once this embedding is constructed, we follow
18We assume that each word in the post has a token id in Bert’s vocabulary.

--- Page 7 ---

Deep
State
Word
Context words in a window of size 5
Surronding context
Surronding context
Word
Word
Word
Word
Word
W
W-1
W-2
W-3
W+1
W+2
W+3
AND THE EVIL LYING DEEP STATE CABAL SATANIC SCUM BAGS ALL NEED TO BE
ROUNDED UP AND EXECUTED.
Post
Tensors: 18X12X768
Embeddings
W-5 (Deep State - W) W+5
Word embedding lookup table
Encoder
Encoder
Word
Word
W-4
W-5
Word Word
W+4 W+5
Fig. 4. Post-truncate embedding approach for a window of size 5.
the same procedure described in Section IV-B2a except for the
fact that we now extract word-level contextual embeddings
from the lookup table (see Figure 4). The advantage of
this approach over the previous one is that it builds more
informed embeddings given its use of a complete rather than
partial context. Please note that there are three additional
differences between the standard and the advanced approach:
in the standard approach, we used context window sizes
between 5 and 14 while in the advanced approach, we used
context window sizes between 1 and 10. That is because a
window of 1 word does not convey much information in the
standard approach whereas it does in the advanced approach.
As a result, we started at size 5 in the standard approach and
1 in the advanced approach and used 10 different window
sizes in each case. Furthermore, in the advanced approach,
the embeddings are generated by averaging the final encoder
layer of BERT rather than using the pooled layer since that
yielded better results. Finally, the optimal value for m in the
advanced approach was 9 rather than 7.
V. RESULTS AND DISCUSSION
The purpose of our study was to design a methodology
for extracting emerging coded antisemitic terminology from
online posts appearing on social media platforms often used
by extremist groups. We proposed a pipeline to implement this
methodology and instantiated this pipeline with standard and
advanced components. The difficult part of our evaluation is
the assessment of whether the approach yields a significant
number of terms and whether these terms can, indeed in some
contexts, have an antisemitic connotation. In order to answer
these questions, we created a gold standard and tested our
results according to it.
A. Construction of a gold standard:
The gold standard we created uses two complementary
methodologies. One for the terms already familiar to the
community that fights antisemitism, and the other, for the
terms unknown or not yet catalogued by that community.19
Known Terms For the first category, we simply compiled
a general glossary from three existing sources: the Institute
for Curriculum Services’ Glossary spanning the history of
European Antisemitism, which we took in its entirety; the
American Jewish Committee “Translate Hate” glossary which
we also used in its entirety (prior to its recent expansion from
46 to 70 terms) and portions of the Glossary of Terms and
Acronyms constructed by the R2Pris project on Radicalization
and violent extremism. Since this last source encompassed ha-
tred of different types, for this specific study, we restricted our-
selves to the terms whose composition or definition included
a known antisemitic term (e.g., nazi, Aryan, anti-semitic, Ku
Klux Klan, SS, Swastika, Fascism, White Supremacist, etc.).20
New Terms The new terms are the terms that do not appear in
the glossaries just mentioned and that need to be manually
verified through an internet search. We used the following
systematic procedure to assign ground labels to new terms:
• Each extracted term not found in the glossary compilation
was searched for on Google in two ways: the term alone
or together with “+ antisemitism” added to the search.
• The documents retrieved on the first page of the Google
browser for both searches were examined for references
to antisemitism.
• If, based on this analysis, the term was found to be
associated with antisemitism (e.g., “deep state” was found
to be associated with a conspiracy theory against the
Jews), it was coded as antisemitic in our gold standard
database. If, on the other hand, the term did not carry any
clear meaning (e.g., “late 20th”) or was not associated
with antisemitism (e.g., “new york city”), it was coded
as not antisemitic in our gold standard database.
Qualitative evaluation We conducted two types of qualitative
evaluation. The first one simply consisted of observing the
terms extracted by the approach to assess whether they made
sense when taken out of context. The second one can be
thought of as a sanity check. For terms extracted and labeled
as either antisemitic or not, we went back to the the posts
from which the term was extracted to assess whether, within
the context of the post, it was used in an antisemitic way or
not. Though we do not use these qualitative assessments in
our quantitative evaluation, we show examples of the different
situations that arose in terms of agreement or disagreement
between our system and our gold standard.
B. Results
Quantitative Results: We tested four different versions of
our proposed pipeline, by combining the standard and ad-
19In this paper, we created a prototype system based on the seed words
provided to us by the data team. These seed words are only a small subset of
the already known coded antisemitic terms. As a result, some of the emergent
terms discovered by our system are emergent vis-a-vis the system’s knowledge
but not vis-a-vis the broader current knowledge. Discovering terms known
to the community but not known by the system constitutes a useful proof
of concept. The discovery of terms not currently known by the community
constitutes an added demonstration of the worth of the approach.
20The sources we used can be found at the following websites: https://bit.
ly/45kEtYB; https://bit.ly/3MIjKpt; and http://www.r2pris.org/glossary.html

--- Page 8 ---

TABLE I
ACCURACY, PRECISION, RECALL AND F-SCORE USING THE FOUR VERSIONS OF OUR PIPELINE.
Model+Embedding
Approach Type
Accuracy
Precision
Recall
F-score
colloc-pretrunc
standard
0.74
0.34
1
0.51
colloc-posttrunc
hybrid
0.76
0.36
1
0.53
tfidf-pretrunc
hybrid
0.67
0.47
0.55
0.51
tfidf-posttrunc
advanced
0.80
0.63
0.83
0.72
vanced solutions proposed for trending term extraction with
the standard and advanced solutions proposed for term em-
bedding. These combinations resulted in one standard, two
hybrid, and one advanced implementation. Table I lists the
results obtained by concordance + collocation followed by
pre-truncation embedding (colloc-pretrunc) or post-truncation
embedding (colloc-posttrunc); and those obtained by tfidf
+ frequency followed by pre-truncation embedding (tfidf-
pretrunc) or post-truncation embedding (tfidf-posttrunc). The
results were obtained using our gold standard labels. The
approach using the two advanced components stands out as
the absolute winner: tfidf-posttrunc, although the results for
all four methods, including tfidf-posttrunc, show a higher level
of recall than precision. Future work will attempt to improve
all these metrics scores, with a focus on precision so as
not to unduly label terms as antisemitic when they are, in
fact, benign. When comparing the numbers in Table I, it is
important to note that the number and type of terms retrieved
differ between the two term extraction processes, colloc and
tfidf. While colloc extracted 52 terms of which only 7 were
truly antisemitic, tfidf extracted 94 of which 29 were truly
antisemitic. The recall of 1 obtained by the two colloc-based
methods, thus means that both pretrunc and posttrunc were
able to identify these 7 antisemitic terms. Their low level of
precision, however, suggests that they are too liberal in their
labeling of terms as antisemitic.
Qualitative Results: Our qualitative evaluation was applied
to the version of our pipeline that obtained the best results:
tfidf-posttrunc, i.e., the advanced version. Table II shows some
of the terms extracted by that version. The terms in red
correspond to terms incorrectly classified as antisemitic with
no good explanation; those in black are correctly classified as
antisemitic as they correspond to our Known Terms; those in
blue were verified to be antisemitic as they correspond to our
New Terms; and those in purple were incorrectly classified as
antisemitic, although the context in which they arise is clearly
antisemitic. As discussed below, we call these terms Neutral
(in an antisemitic context).
Sanity Check: In Table III, we show a few sample posts con-
taining the following trending antisemitic terms discovered by
tfifd-posttrunc: Interest groups, White Genocide,
Deep state. Each of these terms had an entry in the
antisemitic glossary compilation described earlier. For in-
stance, White Genocide, refers to a conspiracy theory
rooted in white supremacist ideology, claiming that there is
an intentional effort by Jews to destroy the white race through
immigration, mixed-racial marriage, LGBTQ+ identification,
etc. Table III also shows an instance of a new term —
FEMA camps. This corresponds to a conspiracy theory where
FEMA is believed to plan the incarceration and possible
execution of US citizens in favor of the establishment of a
New World Order, one of our seed words which often refers
to the establishment of a new form of government controlled
by a Jewish elite.On the other hand, during the process of
extracting coded antisemitic terms, some terms were labeled
as antisemitic despite the fact that they do not appear in our
gold standard. In certain cases, that represents an outright
mistake like in the case of Big Part in Table III where
the context is certainly racist, but not specifically antisemitic,
though antisemitism is part of the post, but in other situations,
a case could be made for the antisemitic label. For example,
our approach predicts End game as a coded antisemitic term,
even though we did not find any reason for it in our glossary or
internet search. A look at the post in which the term appeared
(Table III) helps us understand how the antisemitic context of
the post that includes the terms “concentration camps” and
”new world order” led the system to mislabel it. We conclude
that, in such cases, our approach is extracting the right term
according to the context, but the term should be considered
Neutral (in an antisemitic context) rather than antisemitic.
C. Discussion
Though we assume that our approach could still be refined,
we note that the results obtained by the most successful version
of our system are encouraging, suggesting the viability of our
hypothesis that emergent coded terms could be discovered
automatically using distance measures in embedding spaces.
The sanity checks suggest that the terms identified by our
approach are, usually, warranted as the context shown in the
posts attests to the antisemitic nature of the way in which
the identified terms are used. These checks also point to
the errors made by the system and will help us improve
our results. We also believe that our approach could have
important practical uses. After being vetted by a human team,
the emergent coded terminology it discovers could be input
to the moderating algorithms used by social media platforms
to discover problematic discourse or users currently avoiding
discovery.
VI. CONCLUSION
This paper proposes an approach for detecting the emer-
gence of new antisemitic coded terminology which offers
a valuable resource in combating online antisemitism and
contributes to the ongoing efforts to create safer and more
inclusive online spaces. We achieve an accuracy of 80% and

--- Page 9 ---

TABLE II
LIST OF TRENDING TERMS THAT ARE PREDICTED ANTISEMITIC BY THE MOST ADVANCED VERSION OF THE PIPELINE.
False Positives
Known Terms
New Terms
Neutral
plain sight
german people
white genocide
interest groups
FEMA camps
color revolution
end game
world war
new york city
big part
nostra aetate
federal reserve
central bank
critical race theory
western civilization
democrat party
TABLE III
POSTS ON SOCIAL MEDIA WITH AUTOMATICALLY LABELED ANTISEMITIC CODED TERMS AS PER THE MOST ADVANCED VERSION OF THE PIPELINE.
Coded Term
Status
Website
Post
Interest groups
Known Term
Minds
the united states government is controlled by interest groups that are only seeking to enlarge their
own power. the us government does not represent the will of the citizenry, and condemning it is not a
condemnation on the principles of freedom, democracy, etc.the usa is being set up to fail.the rootless
cosmopolitan elite have been constructing elaborate safehouses for decades in preparation for this.
Deep State
Known Term
4chan
US deep state MIGApede detected. The real deep state is the Jewish lobby.
White Genocide
Known Term
Truth Social Rotten Eggs - Dr. Reiner Fuellmich and Whitney Webb! Vatican Pro-Abortion- False Prophet Francis
Owned By New World Order! Jacob’s Trouble =
White Genocide! Pandemic Of The Double
Dosed.Inflation Spiking, More Lockdowns, The Worst Is Yet To Come!
End Game/FEMA camps Neutral/New Term Truth Social FEMA is not a good thing! FEMA camps are concentration camps. FEMA camps are the end game
of the New World Order
Big Part
False Positive
4chan
all turds need to be deported from the West. turds are brown MENA sunni muslim garbage. they are a
big part of the non-white invasion. many of the turkish Iraqi and syrian immigrants who rape women
and girls are actually ethnic turds. turds are also zionists and turdistan is a base for israeli ops. imagine
sympathizing with these zio-muslim invaders.
F-Score of 72% in extracting antisemitic terms using this
approach which relies on NLP techniques including POS
tagging, TF-IDF, and Fined-tuned large language models such
as BERT. In the future, we intend to refine our semantic
similarity technique by exploring other deep learning and
large language model approaches and their various parameter
combinations. Similarly, we will experiment with different
types of text pre-processing approaches to deal specifically
with hate-speech and social media text. This will be done in
the context of a lifelong-learning setting where the trending
terms discovered will be used as input to the data scraping
component in the following iteration. We also intend to create
a more user-friendly version that will be convenient for people
working in this space. Finally, our goal is to extend this study
to hateful terminology against other minority groups.
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
[5] A. M. Founta, D. Chatzakou, N. Kourtellis, J. Blackburn, A. Vakali,
and I. Leontiadis, “A unified deep learning architecture for abuse
detection,” in Proceedings of the 10th ACM conference on web
science, pp. 105–114, 2019.
[6] J. Serra, I. Leontiadis, D. Spathis, G. Stringhini, J. Blackburn, and
A. Vakali, “Class-based prediction errors to detect hate speech with
out-of-vocabulary words,” in Proceedings of the first workshop on
abusive language online, pp. 36–40, 2017.
[7] B. Gamb¨ack and U. K. Sikdar, “Using convolutional neural networks
to classify hate-speech,” in Proceedings of the first workshop on
abusive language online, pp. 85–90, 2017.
[8] G. Wiedemann, S. M. Yimam, and C. Biemann, “Uhh-lt & lt2 at
semeval-2020 task 12: Fine-tuning of pre-trained transformer net-
works for offensive language detection,” ArXiv, vol. abs/2004.11493,
2020.
[9] M. Schwarz-Friesel and J. Reinharz, Inside the antisemitic mind:
the language of Jew-Hatred in contemporary Germany.
Brandeis
University Press, 2017.
[10] S. Zannettou, J. Finkelstein, B. Bradlyn, and J. Blackburn, “A
quantitative approach to understanding online antisemitism,” in
Proceedings of the International AAAI conference on Web and Social
Media, vol. 14, pp. 786–797, 2020.
[11] G. Jikeli, D. Cavar, and D. Miehling, “Annotating antisemitic online
content. towards an applicable definition of antisemitism,” arXiv
preprint arXiv:1910.01214, 2019.
[12] M. Chandra, D. R. Pailla, H. Bhatia, A. J. Sanchawala, M. Gupta,
M. Shrivastava, and P. Kumaraguru, ““subverting the jewtocracy”:
Online antisemitism detection using multimodal deep learning,”
Proceedings of the 13th ACM Web Science Conference 2021, 2021.
[13] N. A. Cloutier and N. Japkowicz, “Fine-tuned generative llm
oversampling can improve performance over traditional techniques
on multiclass imbalanced text classification,” IEEE COnfernece on
Big Data, 2023.
[14] G. Jikeli, S. Karali, D. Miehling, and K. Soemer, “Antisemitic
messages? a guide to high-quality annotation and a labeled dataset
of tweets,” ArXiv, vol. abs/2304.14599, 2023.
[15] S. Parker and D. Ruths, “Is hate speech detection the solution the
world wants?,” Proceedings of the National Academy of Sciences of
the United States of America, vol. 120, 2023.
[16] R. U. Mustafa, M. S. Nawaz, J. Farzund, M. Lali, B. Shahzad, and
P. Viger, “Early detection of controversial urdu speeches from social
media,” Data Sci. Pattern Recognit., vol. 1, no. 2, pp. 26–42, 2017.
[17] A. Glazkova, “A comparison of text preprocessing techniques for
hate and offensive speech detection in twitter,” Social Network
Analysis and Mining, vol. 13, pp. 1–28, 2023.
[18] E. Loper and S. Bird, “Nltk: The natural language toolkit,” arXiv
preprint cs/0205028, 2002.
[19] J. Ramos et al., “Using tf-idf to determine word relevance in doc-
ument queries,” in Proceedings of the first instructional conference
on machine learning, vol. 242:1, pp. 29–48, Citeseer, 2003.

```
