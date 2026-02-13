---
title: "2022-Chriqui-HeBERT & HebEMO a Hebrew BERT Model and a Tool for Polarity Analysis - PDF Extract"
source_pdf: "2022-Chriqui-HeBERT & HebEMO a Hebrew BERT Model and a Tool for Polarity Analysis.pdf"
pages: 26
extracted_at: "2026-02-13T09:50:28.800993"
---

# PDF Extract: 2022-Chriqui-HeBERT & HebEMO a Hebrew BERT Model and a Tool for Polarity Analysis

**Source PDF:** 2022-Chriqui-HeBERT & HebEMO a Hebrew BERT Model and a Tool for Polarity Analysis.pdf
**Total Pages:** 26

---

## Content

```
--- Page 1 ---

HeBERT & HebEMO: a Hebrew BERT Model and a Tool for Polarity
Analysis and Emotion Recognition
Avihay Chriqui, Inbal Yahav
Abstract
Sentiment analysis of user-generated content (UGC) can provide valuable information across nu-
merous domains, including marketing, psychology, and public health. Currently, there are very few
Hebrew models for natural language processing in general, and for sentiment analysis in particu-
lar; indeed, it is not straightforward to develop such models because Hebrew is a Morphologically
Rich Language (MRL) with challenging characteristics. Moreover, the only available Hebrew sen-
timent analysis model, based on a recurrent neural network, was developed for polarity analysis
(classifying text as “positive”, “negative”, or neutral) and was not used for detection of ﬁner-
grained emotions (e.g., anger, fear, joy). To address these gaps, this paper introduces HeBERT
and HebEMO. HeBERT is a Transformer-based model for modern Hebrew text, which relies on
a BERT (Bidirectional Encoder Representations for Transformers) architecture. BERT has been
shown to outperform alternative architectures in sentiment analysis, and is suggested to be partic-
ularly appropriate for MRLs. Analyzing multiple BERT speciﬁcations, we ﬁnd that while model
complexity correlates with high performance on language tasks that aim to understand terms in a
sentence, a more-parsimonious model better captures the sentiment of an entire sentence. Notably,
regardless of the complexity of the BERT speciﬁcation, our BERT-based language model outper-
forms all existing Hebrew alternatives on all common language tasks. HebEMO is a tool that uses
HeBERT to detect polarity and extract emotions from Hebrew UGC. HebEMO is trained on a
unique Covid-19-related UGC dataset that we collected and annotated for this study. Data collec-
tion and annotation followed an active learning procedure that aimed to maximize predictability.
We show that HebEMO yields a high F1-score of 0.96 for polarity classiﬁcation. Emotion detection
reaches F1-scores of 0.78-0.97 for various target emotions, with the exception of surprise, which the
model failed to capture (F1 = 0.41). These results are better than the best-reported performance,
even among English-language models of emotion detection.
Preprint submitted to XX
December 2020
arXiv:2102.01909v3  [cs.CL]  25 Feb 2021

--- Page 2 ---

1. Introduction
Sentiment analysis, also referred to as opinion mining or subjectivity analysis (Liu and Zhang
2012), is probably one of the most common tasks in natural language processing (NLP) (Liu 2012,
Zhang et al. 2018). The goal of sentiment analysis is to systematically extract, from written text,
what people think or feel toward entities such as products, services, individuals, events, news
articles, and topics.
Sentiment analysis includes multiple types of tasks, one of the most common being polarity
classiﬁcation: the binning of overall sentiment into the three categories of positive, neutral, or
negative. Another prominent sentiment analysis task is emotion detection - a process for extracting
ﬁner-grained emotions such as happiness, anger, and fear from human language. These emotions, in
turn, can shed light on individuals’ beliefs, behaviors, or mental states. Both polarity classiﬁcation
and emotion detection have proven to yield valuable information in diverse applications. Research
in marketing, for example, has shown that emotions that users express in online product reviews
aﬀect products’ virality and proﬁtability (Chitturi et al. 2007, Ullah et al. 2016, Adamopoulos
et al. 2018). In ﬁnance, Bellstam et al. (2020) extracted sentiments from ﬁnancial analysts’ textual
descriptions of ﬁrm activities, and used those sentiments to measure corporate innovation.
In
psychology, sentiment analysis has been used to detect distress in psychotherapy patients (Shapira
et al. 2020), and to identify speciﬁc emotions that might be indicative of suicidal intentions (Desmet
and Hoste 2013). Notably, recent studies suggest that the capacity to identify certain emotions
(e.g., fear or distress) can contribute towards the understanding of individuals’ behaviors and mental
health in the Covid-19 pandemic (Ahorsu et al. 2020, Pfeﬀerbaum and North 2020).
The literature oﬀers a considerable number of methods and models for sentiment analysis, with
a strong bias towards polarity detection. Models for emotion detection, though less common, are
also accessible to the research community in multiple languages. As yet, however, emotion de-
tection models do not support the Hebrew language. In fact, to our knowledge, only one study
thus far has developed a Hebrew-language model for sentiment analysis of any kind (speciﬁcally,
polarity classiﬁcation; Amram et al. (2018)). Notably, existing sentiment analysis methods devel-
oped for other languages are not easily adjustable to Hebrew, due to unique linguistic and cultural
2

--- Page 3 ---

features of this language. A key challenge in the development of Hebrew-language sentiment anal-
ysis tools relates to the fact that Hebrew is a Morphologically Rich Language (MRL), deﬁned as
a language “in which signiﬁcant information concerning syntactic units and relations is expressed
at word-level” (Tsarfaty et al. 2010). In Hebrew, as in other MRLs (e.g., Arabic), grammatical
relations between words are expressed via the addition of aﬃxes (suﬃxes, preﬁxes), instead of the
addition of particles. Moreover, the word order in Hebrew sentences is rather ﬂexible. Many words
have multiple meanings, which change depending on context. Further, written Hebrew contains
vocalization diacritics, known as Niqqud (“dots”), which are missing in non-formal scripts; other
Hebrew characters represent some, but not all of the vowels. Thus, it is common for words that
are pronounced diﬀerently to be written in the same way. These unique characteristics of Hebrew
pose a challenge in developing appropriate Hebrew NLP models. Architectural choices should be
made with care, to ensure that the features of the language are well represented. The current best
practice for Hebrew NLP is the use of the multilingual BERT model (mBERT, based on the BERT
[Bidirectional Encoder Representations from Transformers] architecture, discussed further below;
Devlin et al. (2018)), which was trained on a small size Hebrew dictionary. When tested on Arabic
(the closest language to Hebrew), mBERT was shown to have signiﬁcantly lower performance than
a language-speciﬁc BERT model on multiple language tasks (Antoun et al. 2020).
This paper achieves two main goals related to the development of Hebrew-language sentiment
analysis capabilities. First, we pre-train a language model for modern Hebrew, called HeBERT,
which can be implemented in diverse NLP tasks, and is expected to be particularly appropriate
for sentiment analysis (as compared with alternative model architectures). HeBERT is based on
the well-established BERT architecture (Devlin et al. 2018); the latter was originally trained for
the unsupervised ﬁll-in-the-blank task (known as Masked Language Modeling - MLM (Fedus et al.
2018)). We train HeBERT on two large-scale Hebrew corpuses – Hebrew Wikipedia and OSCAR
(Open Super-large Crawled ALMAnaCH corpus, a huge multilingual corpus based on open web
crawl data, (Ortiz Su´arez et al. 2020). We then evaluate HeBERT’s performance on ﬁve key NLP
tasks, namely, ﬁll-in-the-blank, out-of-vocabulary (OOV), Name Entity Recognition (NER), Part
of Speech (POS), and sentiment (polarity) analysis. We examine several architectural choices for
our model and put forward and test hypotheses regarding their relative performance, ultimately
selecting the best-performing option. Speciﬁcally, we show that while model complexity correlates
3

--- Page 4 ---

with high performance on language tasks that aim to understand terms in a sentence, a more-
parsimonious model better captures the sentiment of an entire sentence.
Second, we develop a tool to detect sentiments – speciﬁcally, polarity and emotions – from
user-generated content (UGC). Our sentiment detector, called HebEMO, is based on HeBERT
and operates on a document level. We apply HebEMO to user-generated comments, from three
major news sites in Israel, that were posted in response to Covid-19-related articles during 2020.
We chose this dataset on the basis of ﬁndings that the Covid-19 pandemic intensiﬁed emotions in
multiple communities (Pedrosa et al. 2020), suggesting that online discourse regarding the pandemic
is likely to be highly emotional. Comments were selected for annotation following an innovative
semi-supervised iterative labeling approach that aimed to maximize predictability.
We show that HebEMO achieves a high performance of weighted average F1-score = 0.96
for polarity classiﬁcation. Emotion detection reaches F1-scores of 0.8-0.97 for the various target
emotions, with the exception of surprise, which the model failed to capture (F1 = 0.41). These
results are better than the best reported performance, even when compared to English-language
models for emotion detection (Ghanbari-Adivi and Mosleh 2019, Mohammad et al. 2018).
The remainder of this paper is organized as follows. In the next section, we provide a brief
overview of the state of the art in sentiment analysis in general and emotion recognition in par-
ticular; we also brieﬂy discuss considerations that must be taken into account when developing
pre-trained language models for sentiment analysis.
Next, we present HeBERT, our language
model, elaborating on how we address some of the unique challenges associated with the Hebrew
language. We subsequently describe HebEMO and evaluate its performance on our UGC data.
2. Background
2.1. Language Speciﬁcity in Emotional Expression
Psychologists and psychoanalysts have long known that, despite the importance of non-verbal
behavior, words are the most natural way to externally express an inner emotional world (Ortony
et al. 1987). In line with this premise, theories of emotions stress that emotional experience and
its intensity can be inferred from spoken or written language (Argaman 2010).
Yet, emotions
vary across cultures (Rosaldo et al. 1984), and, consequently, languages diﬀer in the degree of
emotionality they convey and in the ways in which emotions are expressed in words (Wierzbicka
4

--- Page 5 ---

1994, K¨ovecses 2003). In particular, as noted by K¨ovecses (2003), the verbalization of emotions
commonly relies on the use of metaphorical and metonymic expressions, which may diﬀer across
languages. Religion is another source of variation in emotional experience and its associated ex-
pression Kim-Prieto and Diener (2009). One study showed how the moral system of a culture - and
speciﬁcally, a Middle Eastern culture - can be linked to certain types of emotions, and suggested
that diﬀerences in culturally dominant emotions can play a decisive role in cultural clashes (Fattah
and Fierke 2009).
The above discussion implies that emotion detection tools that are implemented in one language
might not be easily transferable to other languages, particularly languages that are culturally
distant. Accordingly, sentiment analysis tools must be tailored to speciﬁc language models in order
to provide informative results. The current paper proposes such a tool for the Hebrew language
– one that takes into account speciﬁc linguistic challenges associated with Hebrew, elaborated in
subsequent sections.
2.2. Overview of Sentiment Analysis Approaches
Many studies oﬀer comprehensive overviews of common sentiment analysis methods (e.g., Liu
et al. 2019, Hemmatian and Sohrabi 2019, Yue et al. 2019, Yadav and Vishwakarma 2020). We
present here the main points, with an emphasis on models that form the basis of this study. Most
of the models described below were developed primarily for polarity analysis; however, as noted in
the following subsection, the architectures are applicable to other sentiment analysis tasks such as
emotion detection.
Current reviews on sentiment analysis tend to categorize the various approaches according to
the granularity level of text that they accommodate (Liu et al. 2019): document level, that is,
evaluating whether an entire document expresses a particular type of sentiment (e.g., positive or
negative); sentence level – assigning a sentiment to each sentence in the document separately; and
aspect level, that is, assigning sentiment to each “aspect” discussed in the text. The latter requires a
pre-processing step to extract aspects from a written text. In this paper we follow a document-level
approach, elaborated further below.
Sentiment classiﬁcation approaches can further be categorized according to their underlying
methodologies. The ﬁrst, and perhaps the most popular, methodology is the lexicon-based ap-
proach. Based on the theory of emotions, this approach uses sentiment terms to score emotions in
5

--- Page 6 ---

an input text. Linguistic inquiry and word count (LIWC), for example, is a popular software pro-
gram that was developed to assess (among other features) emotions in text, using a psychometrically
validated internal dictionary (Pennebaker et al. 2001). The main advantage of the lexicon-based
approach is that it is unsupervised, meaning that it can be applied without any training or labeled
data (Yue et al. 2019). The main limitation of this approach is that is does not account for the
context of terms in the lexicon, and thus overlooks complex linguistic features such as sarcasm, am-
biguity, and idioms (Liu 2012). Accordingly, its accuracy is fairly low compared with the alternative
approaches.
The second sentiment classiﬁcation approach is Deep Learning (DL)-based. DL approaches are
supervised methods that are based on multiple-layer neural networks. DL-based sentiment classiﬁ-
cation models diﬀer by their network architecture. Common architectures include the following: (1)
Convolutional Neural Networks (CNNs), which transform a structured input layer (e.g., sentences
or documents represented as bag-of-words or word-embedding vectors), via convolutional layers,
into a sentiment class (Kim 2014); (2) Recursive or Recurrent Neural Networks (RNNs), which
handle unstructured sequential data, such as textual sentences, and learn the relations between
the sequential elements (Dong et al. 2014); and (3) Long Short-Term Memory (LSTM), a popular
variant of RNN, which can catch long-term dependencies between data segments, in one direction
(e.g., left to right) or in both (denoted bidirectional LSTM, or BiLSTM architecture) (Hochreiter
and Schmidhuber 1997).
In a recent paper, Amram et al. (2018) raised the question of the relationship between the char-
acteristics of a language and the DL architectural choices of a sentiment classiﬁer. They analyzed
this question for the morphologically rich Hebrew language. Speciﬁcally, they compared the per-
formance of CNN and BiLSTM architectures on a polarity classiﬁcation task. They assumed that
the latter method would implicitly capture main morphological signatures, and thus outperform
the former. Interestingly, and in contrast to ﬁndings in English sentiment analysis (Yin et al. 2017,
Acheampong et al. 2020), they found that CNN yielded overall better performance (accuracy =
0.89) than BiLSTM, even when the latter was trained on morphologically segmented inputs. As
far as we know, this is the only paper that developed and evaluated a sentiment analysis model for
the Hebrew language.
The last sentiment classiﬁcation method, which we adopt in this paper, is the transfer learning-
6

--- Page 7 ---

based approach. Transfer learning is the act of carrying knowledge gained from one problem and
applying it to another, similar problem (Pan and Yang 2009). In NLP, transfer learning is imple-
mented via Transformers (Tay et al. 2020). Similarly to RNN, transformers use a DL approach to
process sequential data. The primary advantage of the Transformer is its unique attention mech-
anism, which eliminates the need to process data in order, and allows for parallelization (Vaswani
et al. 2017). With Transformers, a target language is ﬁrst algorithmically learned, irrespective of
the target language task (e.g., sentiment analysis task). To this end, a language model is trained
on a pre-selected unsupervised NLP task (see section 3 for details) . Then the language model is
transferred to the target task. This process is called ﬁne-tuning.
Various pre-trained language models have been used in transfer learning for NLP; these include
fastText (Joulin et al. 2016), ELMo (Embeddings from Language Models, based on forward and
backward LSTMs) (Peters et al. 2018), GPT (Generative Pre-trained Transformer) (Radford et al.
2018), and BERT (Devlin et al. 2018). Of these, BERT is one of the most common Transformer
models for NLP. For sentiment analysis tasks, BERT models - and Transformer models in general
- are widely used and produce the best results compared with alternatives (Zampieri et al. 2019,
Patwa et al. 2020). For the Hebrew language, the only BERT model available is mBERT (Devlin
et al. 2018), which was trained on a small-sized Hebrew dictionary (about 2000 tokens). Notably,
for the Arabic language, which is the closest MRL to Hebrew, Antoun et al. (2020) showed that
a pre-trained Arabic BERT model achieved better performance on polarity analysis than did any
other architecture (improvement of 1% to 6% in accuracy). The Arabic-speciﬁc model also achieved
better performance compared with mBERT.
2.3. Emotion Recognition
Emotion recognition is a sub-task in sentiment analysis that oﬀers a ﬁner granularity sentiment
level compared with polarity analysis.
Two deﬁnitions of human emotions dominate the NLP
literature, with no clear preference between them (Kratzwald et al. 2018). The ﬁrst deﬁnition, based
on a theory developed by Ekman (1999), considers emotions as distinct categories, meaning that
each emotion diﬀers from the others in important ways rather than simply their intensity. Ekman
(1999) identiﬁed six basic emotions, consistent across cultures, that ﬁt facial expressions: anger,
disgust, fear, happiness, sadness and surprise. The second deﬁnition is based on a theory by Plutchik
(1980), who stressed that emotions can be treated as dimensional constructs, and that there are
7

--- Page 8 ---

relations between occurrences and intensities of basic emotions.
In particular, Plutchik (1980)
deﬁned a “wheel” comprising four polar-pairs of basic emotions: joy–sadness, anger–fear, trust–
disgust, and surprise–anticipation. Combinations of dyads or triads of emotions deﬁne another set
of 56 emotions. For example, envy is a combination of sadness and anger. This wheel serves as
the theoretical basis of common automated emotion detection algorithms (Medhat et al. 2014).
Notably, for the purpose of emotion detection, the two conceptualizations of emotion are generally
compatible with each other, as they agree on the set of emotions deﬁned as “basic” emotions.
Though common, emotion recognition is not as widespread as polarity analysis, and it is con-
sidered more challenging (Acheampong et al. 2020). A key challenge is that, whereas any text
can be classiﬁed according to its polarity, not all texts contain emotions, and thus it is harder to
infer emotions via a lexicon-based approach. This challenge is further compounded by the fact
that labeled data are commonly not available. Further, existing datasets are rather imbalanced.
Naturally, the lack of data availability is more severe in non-English languages (Ahmad et al. 2020).
In general, the emotion detection task is treated as a multi-label classiﬁcation task, and models
for emotion recognition are similar in architecture to polarity detection models. Recent research
has shown that, in emotion detection tasks, pre-trained BiLSTM architectures provide advantages
over CNN and unidirectional RNN models (Acheampong et al. 2020), and that Transformers are
preferable to other DL approaches (Chatterjee et al. 2019, Zhong et al. 2019). For example, in
a recent SemEval competition (Chatterjee et al. 2019) that included an emotion detection task
for three emotions (angry, happy, sad), Transformer-based models were shown to give the best
performance (performance ranges: F1-Score = 0.75 - 0.8; precision = 0.78 - 0.85; recall = 0.78 -
0.85).
2.4. Training Language Models for Transfer Learning
As noted above, transfer learning for polarity analysis and/or emotion recognition requires
a pre-trained language model. To develop and train a language model, one needs to make the
following three basic decisions:
1. Input representation (tokenization): What is the granularity of the tokens that are fed to
the model? Common granularity levels include characters, n-gram-based sub-words (using
WordPiece algorithm (Schuster and Nakajima 2012)), morpheme-based sub-words, and full
8

--- Page 9 ---

words (see Figure 1 for the diﬀerences between the approaches).
2. Architectural choices: What is the exact architecture and speciﬁcation of the neural network?
3. Output: What is the (unsupervised) task that the model is trained on?
Figure 1: Input representation alternatives
Regarding input representation, the choice of representation aﬀects the features that the language
model is able to capture, and the training complexity. Character-based representation is better
for learning word-morphology, especially for low-frequency words and MRLs (Belinkov et al. 2017,
Vania et al. 2018), but it comes with longer training time and a deeper architecture, compared
with other representations (Bojanowski et al. 2015). Word-based representation, in turn, treats
each word as a separate token, and thus is considered better for understanding semantics (Pota
et al. 2019).
With this representation, however, words that diﬀer by preﬁx or suﬃx are con-
sidered diﬀerent, necessitating storage of a very large vocabulary.
Moreover, out-of-vocabulary
(OOV) tokens are not represented. The intermediate option is to use a sub-word representation,
which provides some balance between the character- and word-based representations; moreover, it
overcomes the OOV problem associated with the word-based representation, and its vocabulary
requirements are more manageable (Wu et al. 2016). With sub-words, words can be broken into
9

--- Page 10 ---

either n-gram characters, or according to morphemes that have lingual meaning (but also higher
computational costs). Previous literature has produced mixed results regarding to the extent to
which using a morpheme-based approach can improve upon the n-gram-based approach (Bareket
and Tsarfaty 2020). Recently, Klein and Tsarfaty (2020) showed that sub-word splitting in the mul-
tilingual BERT model (mBERT, Devlin et al. (2018)) is sub-optimal for capturing morphological
information.
For the question of architecture selection, Devlin et al. (2018) and Radford et al. (2019) showed
that for similar model size, BERT outperforms other architectures such as GPT and ELMo on
sentiment tasks.
With respect to the model output, there are two tasks on which a model can be trained. The
ﬁrst is predict-the-future, meaning that the model is trained to predict the last token of a sentence.
This task accounts for uni-directional contexts only. The second is the ﬁll-in-the-blank task, where
the model is trained to ﬁll in a missing token within a sentence. This task takes into account
the full (bi-directional) sentence context, and is able to better capture the meanings of tokens,
both syntactically and semantically (Devlin et al. 2018). Recently, Levine et al. (2020) oﬀered a
method to optimize these tasks, called Pointwise Mutual Information (PMI) masking. The authors
suggested that instead of ﬁlling in a single random token, the model should be trained to ﬁll in a
set of tokens that carry mutual information.
3. HeBERT: Language Model
In this section we develop an unsupervised Hebrew BERT model, which we will later ﬁne-tune
for the tasks of polarity analysis and emotion recognition.
3.1. Tokenization, Architecture, and Output
We begin by addressing the three key modeling decisions outlined in the previous section - input
representation (tokenization), architecture, and output - in the context of the Hebrew language.
Recall that, as discussed in the introduction, Hebrew is an MRL with the following important
characteristics: (i) grammatical relations in Hebrew are expressed via the addition of aﬃxes; (ii)
Hebrew sentences are nearly order-free; (iii) many Hebrew words have multiple meanings, which
change depending on context; (iv) Hebrew contains vocalization diacritics that are missing in non-
10

--- Page 11 ---

formal scripts, implying that words that are pronounced diﬀerently can be written in the same
way.
Bearing these features in mind, we ﬁrst address the last two questions, of architectural choice and
model output. As discussed in previous sections, BERT has been shown to outperform alternative
architectures in sentiment analysis tasks (Radford et al. 2019); moreover, the literature oﬀers
evidence that BERT networks eﬀectively capture linguistic information and phrase-level information
(Jawahar et al. 2019), a necessary requirement for MRLs (Tsarfaty et al. 2020). Accordingly, we
decided to use BERT as our base model, with the default architecture. For the output task, we
used BERT’s default ﬁll-in-the-blank task. Fill-in-the-blank has the advantage of understanding
bi-directional context, which corresponds to the order-free property of Hebrew sentences.
With respect to the input - the granularity of the tokens - the literature on MRLs, and Hebrew
speciﬁcally, is inconclusive. Belinkov et al. (2017) and Vania et al. (2018) showed that character-
based representation, which is becoming increasingly popular, is better than word-based represen-
tation for learning Hebrew morphology, especially for low-frequency words. For sentiment tasks,
however, Amram et al. (2018) and Tsarfaty et al. (2020) showed that a word-based representation
yields better predictions than a char-based representation.
With regard to sub-word represen-
tations, Klein and Tsarfaty (2020) suggested (but did not verify) that, for BERT for Hebrew,
morpheme-based sub-words are likely to be preferable to n-gram-based sub-words. A similar argu-
ment was made for Arabic, which is the closest MRL language to Hebrew (Antoun et al. 2020).
To understand what causes diﬀerences in ﬁndings between diﬀerent researchers, consider the
following three examples:
1. First, is the word NA’AL. NA’AL can be translated as either locked (e.g., he locked the
door), a shoe, or the past, singular, tense of the verb wearing (a shoe). It is also often used
as a slang term for stupid. The actual semantic meaning of NA’AL in a sentence is derived
from the context. In that respect, a high-level text granularity (such as a word-based
representation) might be the preferable choice for representing Hebrew, as it is better in
capturing semantic meanings in context (Pota et al. 2019).
2. Next, is the word NA’ALO, which is an inﬂection of the word NA’AL with the suﬃx ”O”.
NA’ALO can refer to either “his shoe” or “locked it”. In that respect, a ﬁner text granu-
11

--- Page 12 ---

larity, such as char-based, which is better at learning morphology, might be preferred.
3. Finally, consider the splitting of the word NA’ALO. Here, a meaningful splitting would be
NA’AL-O. However, such a splitting can be only achieved with morpheme-based sub-words,
using a tool such as YAP (Yet Another Parser, by More et al. (2019)). The alternative, n-
gram-based sub-words, will result in additional splitting, which might have lower semantic
meaning than morpheme-based sub-words, yet higher robustness to OOV.
Given the above discussion, we hypothesize that sub-word representations (n-gram- or morpheme-
based representation), which balance semantic meaning with morphology, will best capture the
features of the Hebrew language, and will yield better performance for various language tasks, as
compared with character-based and word-based representations. Comparing n-gram-based sub-
words with morpheme-based sub-words, we expect the latter to have an advantage on token-level
tasks that require a good “understanding” of the language features; yet, a morpheme-based repre-
sentation might not have such an advantage in document-level downstream tasks.
To examine our hypothesis, we ﬁrst train and evaluate multiple small-size BERT models that
diﬀer by the granularity of the input. We then choose the best-performing architecture, and re-train
the model on a much larger corpus.
3.2. Comparison Analysis of Tokenization Approaches
We examine ﬁve alternative text representations: char-based; two n-gram-based sub-word repre-
sentations, which diﬀer in the total vocabulary size (30K tokens vs. 50K tokens); a morpheme-based
sub-word representation; and a word-based representation, which considers all words in the corpus,
after trimming terms in the lowest 5th quantile according to their term frequency (vocabulary size
of over 53K tokens).
To compare between the input alternatives, we ﬁrst train small-sized base-BERTs on a Hebrew
Wikipedia dump1.
Our working assumption is that the performance of a small-sized BERT is
monotonic with the model’s performance when trained on a larger corpus with the same parameters,
yet requires signiﬁcantly fewer resources. We evaluate the models’ performances on two common
unsupervised language tasks and on three downstream tasks:
1As of September 2013; retrieved from https://u.cs.biu.ac.il/ yogo/hebwiki/. The dataset includes over 63 million
words and 3.8 million sentences.
12

--- Page 13 ---

1. Unsupervised language tasks:
(a) Fill-in-the-blank - the ability to ﬁll in a missing token; tested on a newspaper arti-
cle 2 and a fairy-tale dataset3.
Performance was measured with sequence perplexity
(PP(W)) - a common measure to examine the ability of a language model to evalu-
ate the correctness of sentences in a sample set. Perplexity of a sequence W with N
tokens (W = {w1, w2, ..., wn}) is calculated as the exponential average log-likelihood
of the sequence (PP(W) = exp{−1
N
PN
i logpθ(wi|w<i)}, where logpθ(wi|w<i) is the log-
likelihood of the ith token conditioned on the preceding tokens, according to the language
model).
(b) Generalizability to OOV - the ability of the language model to generalize beyond the
trained corpus (Wikipedia vocabulary), as measured by the percentage of tokens in a
testing set for which the language model could not predict the term embedding. As a
testing set, we used the corpus reported in Amram et al. (2018).
2. Downstream classiﬁcation tasks:
(a) Named-entity recognition (NER) - the ability of the model to classify named entities in
text, such as persons’ names, organizations, and locations; tested on a labeled dataset
from Mordecai and Elhadad (2005), and evaluated with F1-score (2 × precision×recall
precision+recall).
(b) Part of speech (POS) - the ability of the model to classify the grammatical role that
a word or phrase plays in a sentence (e.g., noun, pronoun, verb); tested on a labeled
Israeli newspaper dataset from Sima’an et al. (2001), and evaluated with F1-score (See
appendix A for detailed explanation of how we compared the performance of the models).
(c) Polarity analysis - tested on the polarity data that were collected and labeled by Amram
et al. (2018) and evaluated with F1-score.
The results of this comparison are shown in Table 1.
For the unsupervised tasks (ﬁll-in-the-blank and OOV), the sub-word representations (n-gram-
based and morpheme-based) performed similarly well, and substantially outperformed the word-
based representation. Speciﬁcally, all sub-word methods were able to capture OOV tokens, with the
2Retrieved from: https://www.haaretz.co.il
3Retrieved from https://benyehuda.org/ - a volunteer-based free digital library expanding access to Hebrew liter-
ature.
13

--- Page 14 ---

Fill-the-blank
OOV
NER
POS
Polarity analysis
Metric
(Perplexity)
(%)
(F-1 score)
(F-1 score)
(F-1 score)
chars (1k)
1.17
∼0
0.74
0.92
0.69
n-gram (30k)
4.4
∼0
0.79
0.90
0.79
n-gram (50k)
5.7
∼0
0.79
0.92
0.71
morpheme-based
8.9
0.75
0.92
0.95
0.65
word-based
209830
50
0.86
N/A∗
0.43
Table 1: Comparison of task performance for diﬀerent input alternatives. The best results for each task are in bold.
∗POS cannot be computed due to the high OOV percentage.
exception of special emojis. The performance for the ﬁll-in-the-blank task is monotonic with respect
to the dictionary size. Char-based representation outperformed the sub-word representations on
the ﬁll-in-the-blank task and performed equally well on the OOV task. This is not surprising, as
smaller-sized dictionaries leave less room for mistakes.
For each of the downstream tasks, in line with our hypothesis, the top-performing tokenization
was a sub-word representation. Speciﬁcally, n-gram-based tokenization performed best on the POS
task, whereas morpheme-based tokenization achieved the best performance on NER. For polarity
analysis, the n-gram-based approach with the smaller dictionary (30K) performed signiﬁcantly
better than all other approaches.
These results suggest that (1) there is no single representation that is optimal for the entire set
of tasks, (2) for each task, there is at least one sub-word representation that outperforms both the
char- and word-based representations, and (3) for a sentiment analysis task, which is the focus of
this work, an n-gram-based sub-word representation with a smaller dictionary yielded the highest
performance. On the basis of these results, we selected the latter tokenization for our model.
3.3. Final Model
In line with the speciﬁcations outlined above, we trained a large-size BERT on both the
Wikipedia corpus and an OSCAR corpus (Ortiz Su´arez et al. 2020), with a small-size n-gram-
based sub-word dictionary. For the Hebrew language, OSCAR contains a corpus of size 9.8 GB,
including 1 billion words and over 20.8 million sentences (after de-duplicating the original data).
We used a Pytorch implementation of Transformers in Python (Wolf et al. 2020) to train a base-
BERT network for 4 epochs, with learning rate = 5e-5, using the Adam optimizer in batches of 128
sentences each.
14

--- Page 15 ---

The performance of the ﬁnal model is reported in Table 2, and compared to the performance
of (i) the (non-BERT) model reported in Amram et al. (2018) and More et al. (2019) and Bareket
and Tsarfaty (2020), the only other model developed for NLP tasks in Hebrew (denoted SOTA, or
“state of the art”); and (ii) mBERT. The best results for each task are in bold.
Task
Fill-in-the-blank
OOV
NER
POS
Polarity analysis
Metric
(Perplexity)
(%)
(F-1 score)
(F-1 score)
(F-1 score)
HeBERT
3.24
∼0
0.85
0.92
0.93
Current SOTA
(Not reported)
8%
0.84
0.97
0.89
mBERT
1
0
0.74
0.94
0.88
Table 2: HeBERT performance, compared to alternative models. Best results for each task are in bold.
The results show that while mBERT outperformed HeBERT in an unsupervised task (ﬁll-in-
the-blank), HeBERT performed better on supervised tasks, even when compared to the current
SOTA. Of note, mBERT contains only 2,000 tokens in Hebrew (compared to 30K in HeBERT).
HeBERT’s higher performance in supervised tasks is thus not surprising.
4. HebEMO: A Model for Polarity Analysis and Emotion Recognition
In this section we develop HebEMO - a model for sentiment analysis, including polarity analysis
and emotion recognition. HebEMO, which is based on HeBERT, predicts sentiments at a document
level; as elaborated in what follows, in our case a “document” is a single user-generated comment on
a news website. The development of the model is based on three main elements: (i) data collection;
(ii) data annotation; and (iii) ﬁne-tuning of HeBERT.
4.1. Data Collection and Annotation
The data collected for this study were compiled from user comments that were posted to Israeli
news websites in response to Covid-19-related articles, during the Covid-19 pandemic (Jan-Dec,
2020) - a highly emotional period (Pedrosa et al. 2020).
Our selection of news sites was inspired by a 2016 statement by Israel’s president, Reuven
(Rubi) Rivlin, according to which Israeli society is composed of four equal-sized “tribes” which are
culturally diﬀerent (and hence might express emotions slightly diﬀerently); of these, three comprise
Hebrew-speaking Jews - namely, secular, national-religious, and ultra-Orthodox (“Haredi”) - and
15

--- Page 16 ---

the fourth “tribe” is Israel’s Arab population (Steiner 2016). Each group is represented in both
politics and the media.
Accordingly, we collected data from three popular Israeli news sites that, respectively, represent
the three Hebrew-speaking “tribes”. Speciﬁcally, our dataset contained all Covid-19-related articles
from Ynet4, which is identiﬁed with the secular “tribe” (with a slight left-wing political leaning);
Israel Hayom5 (translation: “Israel Today”), which is identiﬁed with the national-religious “tribe”
(with a slight right-wing political leaning), and Be-Hadre Haredim6 (translation: “In Haredis’
Rooms”), which represents the ultra-Orthodox group.
For each article, we collected the article’s text, its date of publication, the section in the news
site in which it was published (e.g., news, health, sports), the author, and the comments section. We
excluded from the dataset comments that did not contain Hebrew words, and comments with fewer
than 3 words. We further merged repeated consecutive characters (e.g., three or more identical
punctuation symbols) and removed links and double spaces. The compiled corpus, summarized in
Table 3, contained over half a million comments on 10,794 titles in various sections.
source
section
#titles
#comments
Ynet
activism
3
80
article
500
30053
articles
4506
156174
dating
34
793
digital
124
2067
economy
1486
55521
entertainment
153
7000
food
41
4064
health
271
8112
judaism
63
4321
news
138
8214
sport
71
363
vacation
181
10467
wheels
32
964
Israel Hayom
article
2651
71372
opinion
36
392
Be-Hadre Haredim
news
191
805
Table 3: Description of the collected data
4https://www.ynet.co.il/
5https://www.israelhayom.co.il/
6https://www.bhol.co.il/
16

--- Page 17 ---

Figure 2: Iterative annotation process
4.2. Data Annotation
We annotated a total of 4,000 comments. Comments were selected for annotation following
active learning principles (Li et al. 2012) to minimize the well-known imbalance problem in the
emotion recognition literature (Acheampong et al. 2020). The annotation process we used is de-
scribed below and illustrated in Figure 2.
Our iterative process was initialized in step 1 with a naive unsupervised lexicon-based ap-
proach. For this step, we Google-translated EmoLex: a freely-available English-language polarity
and emotion dictionary (Mohammad and Turney 2013). EmoLex contains a list of manually col-
lected (via crowdsourcing) English words classiﬁed according to one or more of the eight basic
emotions and two polarity values (positive and negative). We then used the translated dictionaries
to score the entire set of lemmatized comments in our dataset. Lemmatization was achieved with
UDPipe (Straka et al. 2016).
In step 2, given the initial sentiment scores generated in step 1, we selected a set of 150
comments, of which 75 comments had received the highest positive polarity scores, and 75 had
received the highest negative polarity scores. Similarly, for each of the eight emotions, we selected
a set of 75 comments in which the emotion was highly expressed, and another 75 comments in which
the emotion was not expressed. The resulting set, after removing duplicate comments, comprised
a total of 1,500 initially labeled comments.
17

--- Page 18 ---

We then turned to Proliﬁc7, a trusted online labor and research platform, to manually re-
annotate the 1,500 comments.
Each comment was annotated by at least three distinct native
Hebrew-speaking Proliﬁc workers. Speciﬁcally, annotators were asked to rate individual comments’
polarity on a symmetric 5-point scale of {strongly negative, negative, neutral, positive, strongly
positive}, and to rate the expression of each emotion in the comment on a polar 3-point scale of
{not expressed (in the comment), expressed, strongly expressed}. The participants were given the
context of the comment (i.e., the title of the news article on which the comment was posted). Each
participant annotated 20 randomly selected comments.
The reliability levels of workers’ annotations were then computed with Krippendorﬀ’s alpha
(Krippendorﬀ1970), a measure of inter-rater agreement. We measured reliability independently
for each sentiment in a comment, using coarser sentiment scales of polarity = {positive, neutral,
negative} and emotion = {expressed, not expressed}. For example, if two raters, i and j, rated the
emotion “anger” in a comment c as Li
c,anger = “expressed” and Lj
c,anger = “strongly expressed”,
we computed their mutual response as “agreement” (formally, the observed agreement between
the raters was δ(Li
c,anger, Lj
c,anger) = 0). If the ratings were Li
c,anger = “expressed” (or “strongly
expressed”) and Lj
c,anger = “not expressed”, we computed the raters’ mutual response as “dis-
agreement” (δ(Li
c,anger, Lj
c,anger) = 1). We then excluded comments’ sentiment annotation with
Krippendorﬀ’s alpha lower than 0.75.
In step 3, we trained an initial HeBERT-based sentiment (supervised) classiﬁer (see details
in Section 4.3) on the crowd-annotated data, and predicted polarity and emotion scores for the
remainder of the corpus. We then repeated steps 2 and 3 until the performance of our classiﬁer
converged.
Convergence occurred after three iterations, and a total of 4,000 partially labeled
comments (partially means that the raters agreed on at least one sentiment).
Tables 4 and 5
summarize the number of comments for each sentiment (polarity and emotion, respectively) for
which there was high agreement among raters, and the percentage of the comments that express
this sentiment. For example, the expression/non-expression of the emotion “anger” was labelled
in 1,979 distinct comments; among these, “anger” was expressed in 78% of the comments, and in
22% it was not expressed.
7https://www.proliﬁc.co/
18

--- Page 19 ---

Polarity
# labeled comments
% comments
Positive
253
13.8%
Neutral
55
3%
Negative
1525
83.2%
Table 4: Summary of the polarity data
Emotion
# labeled comments
% comments
Anger
1979
78%
Disgust
2115
83%
Anticipation
681
58%
Fear
1041
45%
Joy
2342
12%
Sadness
998
59%
Surprise
698
17%
Trust
1956
11%
Table 5: Summary of the emotion data
Interestingly, though we attempted to balance the expression and non-expression of each sen-
timent in our labelled data, our raters had signiﬁcantly lower agreement on positive sentiments -
speciﬁcally, positive polarity, expression of happiness, surprise, and trust, and non-expression of
anger and disgust. In line with the theory of Plutchik (1980), we observed high negative corre-
lation between emotions that are located opposite each other in Plutchik’s wheel of emotion, and
positive correlation between closely related emotions (see Table 6). The ﬁnal classiﬁcation model
Anger
Disgust
Anticipation
Fear
Joy
Sadness
Surprise
Trust
Polarity
Anger
1.00
Disgust
0.46
1.00
Anticipation
0.10
0.09
1.00
Fear
0.15
0.11
0.14
1.00
Joy
0.25
0.27
0.12
0.11
1.00
Sadness
0.21
0.16
0.13
0.28
0.12
1.00
Surprise
0.06
0.04
0.10
0.15
0.05
0.12
1.00
Trust
0.27
0.31
0.11
0.07
0.41
0.08
0.07
1.00
Polarity
0.47
0.44
0.11
0.09
0.36
0.14
0.05
0.40
1.00
Table 6: Pearson score for correlation among emotions identiﬁed by human raters
was denoted HebEMO.
19

--- Page 20 ---

4.3. Fine-Tuning of HeBERT: The Classiﬁcation Model
We modeled our classiﬁcation algorithm by ﬁne-tuning HeBERT for a document-level classiﬁca-
tion task. Prediction probabilities were computed with a softmax activation function. We treated
the polarity task as a multinomial problem with three classes (positive, neutral, negative); emotions
were modeled as independent dichotomous classiﬁcation tasks (expressed, not expressed), as mul-
tiple emotions can co-exist in a single comment. Attempts to merge emotion pairs (e.g., joy-sad)
into a single classiﬁcation category yielded lower performance. To train and evaluate our model,
we randomly partitioned the corpus into training (70%), validation (15%), and test (15%) sets. In
order to avoid data leakage, the tokenization process (in HeBERT) was not trained on the UGC
dataset. We repeated the training and evaluation process following a bootstrap approach with 50
samples (each generated a diﬀerent data partition) and examined the stability of our results.
5. Results
We applied HebEMO to our annotated dataset and examined its performance, as measured by
precision, recall, F1-score and overall accuracy of the expressed sentiment. Table 7 presents the
performance of our model on the polarity task, and Table 8 presents the performance for emotion
recognition.
The weighted average performance across all sentiments is F1-score = 0.931, and
overall accuracy = 0.91. With the exception of the emotion “surprise”, the performance of the
model ranges between F1-score and accuracy of 0.78-0.97.
These performance levels, as far as
we know, exceed those of state-of-the-art English-language models for UGC emotion recognition
(Ghanbari-Adivi and Mosleh 2019, Mohammad et al. 2018).
The emotion “surprise” is known to be hard to detect. As mentioned in Zhou et al. (2020),
the best reported F1-score for this emotion in English was found to be as low as 0.19 (Mohammad
et al. 2018). In our dataset, the amount of labeled data for “surprise” - as well as for its opposing
counterpart on the wheel of emotion, “anticipation” (Plutchik 1980) - was also the lowest among
all emotions (see Table 5), implying that this pair is a challenging labeling task even for human
annotators.
Next, we re-trained HebEMO on the polarity data reported by Amram et al. (2018). Amram
et al. (2018) collected comments that were written in response to oﬃcial tweets posted by the
Israeli president, Mr. Reuven Rivlin, between June and August, 2014 (a total of 12,804 Hebrew
20

--- Page 21 ---

Precision
Recall
F1-score
Positive
0.96
0.92
0.94
Neutral
0.83
0.56
0.67
Negative
0.97
0.99
0.98
Accuracy
0.97
Table 7: HebEMO performance on polarity task in the UGC data
F1
Precision
Recall
Accuracy
Anger
0.97
0.97
0.97
0.95
Disgust
0.96
0.97
0.95
0.93
Anticipation
0.85
0.83
0.87
0.84
Fear
0.80
0.84
0.77
0.80
Joy
0.88
0.89
0.87
0.97
Sadness
0.84
0.83
0.84
0.79
Surprise
0.41
0.47
0.37
0.78
Trust
0.78
0.88
0.70
0.95
Table 8: HebEMO performance on emotion detection task in the UGC data
comments). The authors manually annotated the comments with the following labels - supportive
(positive), criticizing (negative), or oﬀ-topic (neutral) comments - and published a partitioned
dataset (training and validation) for the beneﬁt of comparisons between language models.
The performance of our model is presented in Table 9, along with the improvement/ deterio-
ration in performance as compared with the SOTA model reported in Amram et al. (2018). The
results show that, in most aspects, with the exception of oﬀ-topic precision, our model’s perfor-
mance exceeds that of the SOTA model. The improvement is signiﬁcant at the 95% conﬁdence
level.
Precision
Recall
F1-score
Positive
0.95
(+.03)
0.96
(+.01)
0.95
(+.01)
Negative
0.89
(+.05)
0.89
(+.02)
0.89
(+.04)
Oﬀ-topic
0.70
(-.3)
0.56
(+.55)
0.62
(+.03)
Accuracy
0.93
(+.03)
Table 9: The performance of HebEMO when trained on the polarity corpus reported by Amram et al. (2018)
21

--- Page 22 ---

6. Summary and Discussion
This paper presented two new tools that contribute to the development of Hebrew-language
sentiment analysis capabilities: (i) HeBERT - the ﬁrst Hebrew BERT model, and a new state-of-
the-art model for multiple Hebrew NLP tasks; and (ii) HebEMO - a tool for polarity analysis and
emotion recognition from Hebrew UGC.
Although HeBERT was developed for the purpose of optimizing sentiment analysis, we showed
that it outperforms mBERT in a variety of supervised language tasks. This ﬁnding is consistent
with the literature that proposes that language-speciﬁc models are better than multilingual model.
HeBERT also showed better performance than the current (non-BERT) SOTA Hebrew-language
model.
For the task of extracting sentiments from UGC, we showed that a morpheme-based model,
which aims to “understand” features of the language, performed less well than a model that did
not address the language features (ngram-based sub-words). For the latter input representation,
a smaller-size dictionary was better than the larger-size dictionary. A plausible explanation for
these results is that UGC contains unoﬃcial language, which includes non-lexical words such as
slang words and typos. Over-ﬁtting a model to a language in this case may overlook the unique
characteristics of the unoﬃcial language. In future work we plan to examine the performance of
HebEMO when HeBERT is trained on a PMI masking task, rather than ﬁll-in-the-blank.
22

--- Page 23 ---

References
Acheampong FA, Wenyu C, Nunoo-Mensah H (2020) Text-based emotion detection: Advances, challenges,
and opportunities. Engineering Reports e12189.
Adamopoulos P, Ghose A, Todri V (2018) The impact of user personality traits on word of mouth: Text-
mining social media platforms. Information Systems Research 29(3):612–640.
Ahmad Z, Jindal R, Ekbal A, Bhattachharyya P (2020) Borrow from rich cousin: transfer learning for
emotion detection using cross lingual embedding. Expert Systems with Applications 139:112851.
Ahorsu DK, Lin CY, Imani V, Saﬀari M, Griﬃths MD, Pakpour AH (2020) The fear of covid-19 scale:
development and initial validation. International journal of mental health and addiction .
Amram A, David AB, Tsarfaty R (2018) Representations and architectures in neural sentiment analysis for
morphologically rich languages: A case study from modern hebrew. Proceedings of the 27th Interna-
tional Conference on Computational Linguistics, 2242–2252.
Antoun W, Baly F, Hajj H (2020) Arabert: Transformer-based model for arabic language understanding.
arXiv preprint arXiv:2003.00104 .
Argaman O (2010) Linguistic markers and emotional intensity. Journal of psycholinguistic research 39(2):89–
99.
Bareket D, Tsarfaty R (2020) Neural modeling for named entities and morphology (nemoˆ 2). arXiv preprint
arXiv:2007.15620 .
Belinkov Y, Durrani N, Dalvi F, Sajjad H, Glass J (2017) What do neural machine translation models learn
about morphology? arXiv preprint arXiv:1704.03471 .
Bellstam G, Bhagat S, Cookson JA (2020) A text-based analysis of corporate innovation. Management
Science .
Bojanowski P, Joulin A, Mikolov T (2015) Alternative structures for character-level rnns. arXiv preprint
arXiv:1511.06303 .
Chatterjee A, Narahari KN, Joshi M, Agrawal P (2019) Semeval-2019 task 3: Emocontext contextual emotion
detection in text. Proceedings of the 13th International Workshop on Semantic Evaluation, 39–48.
Chitturi R, Raghunathan R, Mahajan V (2007) Form versus function: How the intensities of speciﬁc emo-
tions evoked in functional versus hedonic trade-oﬀs mediate product preferences. Journal of marketing
research 44(4):702–714.
Desmet B, Hoste V (2013) Emotion detection in suicide notes. Expert Systems with Applications 40(16):6351–
6358.
Devlin J, Chang MW, Lee K, Toutanova K (2018) Bert: Pre-training of deep bidirectional transformers for
language understanding. arXiv preprint arXiv:1810.04805 .
Dong L, Wei F, Tan C, Tang D, Zhou M, Xu K (2014) Adaptive recursive neural network for target-
dependent twitter sentiment classiﬁcation. Proceedings of the 52nd annual meeting of the association
for computational linguistics (volume 2: Short papers), 49–54.
Ekman P (1999) Basic emotions. Handbook of cognition and emotion 98(45-60):16.
Fattah K, Fierke KM (2009) A clash of emotions: The politics of humiliation and political violence in the
middle east. European journal of international relations 15(1):67–93.
Fedus W, Goodfellow I, Dai AM (2018) Maskgan: Better text generation via ﬁlling in the . arXiv preprint
arXiv:1801.07736 .
Ghanbari-Adivi F, Mosleh M (2019) Text emotion detection in social networks using a novel ensemble
classiﬁer based on parzen tree estimator (tpe). Neural Computing and Applications 31(12):8971–8983.
Hemmatian F, Sohrabi MK (2019) A survey on classiﬁcation techniques for opinion mining and sentiment
analysis. Artiﬁcial Intelligence Review 1–51.
Hochreiter S, Schmidhuber J (1997) Long short-term memory. Neural computation 9(8):1735–1780.
Jawahar G, Sagot B, Seddah D (2019) What does bert learn about the structure of language?
23

--- Page 24 ---

Joulin A, Grave E, Bojanowski P, Douze M, J´egou H, Mikolov T (2016) Fasttext.zip: Compressing text
classiﬁcation models. arXiv preprint arXiv:1612.03651 .
Kim Y (2014) Convolutional neural networks for sentence classiﬁcation. arXiv preprint arXiv:1408.5882 .
Kim-Prieto C, Diener E (2009) Religion as a source of variation in the experience of positive and negative
emotions. The Journal of Positive Psychology 4(6):447–460.
Klein S, Tsarfaty R (2020) Getting the## life out of living: How adequate are word-pieces for modelling
complex morphology? Proceedings of the 17th SIGMORPHON Workshop on Computational Research
in Phonetics, Phonology, and Morphology, 204–209.
K¨ovecses Z (2003) Metaphor and emotion: Language, culture, and body in human feeling (Cambridge Uni-
versity Press).
Kratzwald B, Ili´c S, Kraus M, Feuerriegel S, Prendinger H (2018) Deep learning for aﬀective computing:
Text-based emotion recognition in decision support. Decision Support Systems 115:24–35.
KrippendorﬀK (1970) Estimating the reliability, systematic error and random error of interval data. Edu-
cational and Psychological Measurement 30(1):61–70.
Levine Y, Lenz B, Lieber O, Abend O, Leyton-Brown K, Tennenholtz M, Shoham Y (2020) Pmi-masking:
Principled masking of correlated spans. arXiv preprint arXiv:2010.01825 .
Li S, Ju S, Zhou G, Lin X (2012) Active learning for imbalanced sentiment classiﬁcation. Proceedings of the
2012 Joint conference on empirical methods in natural language processing and computational natural
language learning, 139–148.
Liu B (2012) Sentiment analysis and opinion mining. Synthesis lectures on human language technologies
5(1):1–167.
Liu B, Zhang L (2012) A survey of opinion mining and sentiment analysis. Mining text data, 415–463
(Springer).
Liu R, Shi Y, Ji C, Jia M (2019) A survey of sentiment analysis based on transfer learning. IEEE Access
7:85401–85412.
Medhat W, Hassan A, Korashy H (2014) Sentiment analysis algorithms and applications: A survey. Ain
Shams engineering journal 5(4):1093–1113.
Mohammad S, Bravo-Marquez F, Salameh M, Kiritchenko S (2018) Semeval-2018 task 1: Aﬀect in tweets.
Proceedings of the 12th international workshop on semantic evaluation, 1–17.
Mohammad SM, Turney PD (2013) Crowdsourcing a word-emotion association lexicon 29(3):436–465.
Mordecai NB, Elhadad M (2005) Hebrew named entity recognition. MONEY 81(83.93):82–49.
More A, Seker A, Basmova V, Tsarfaty R (2019) Joint transition-based models for morpho-syntactic parsing:
Parsing strategies for mrls and a case study from modern hebrew. Transactions of the Association for
Computational Linguistics 7:33–48.
Ortiz Su´arez PJ, Romary L, Sagot B (2020) A monolingual approach to contextualized word embed-
dings for mid-resource languages. Proceedings of the 58th Annual Meeting of the Association for
Computational Linguistics, 1703–1714 (Online:
Association for Computational Linguistics), URL
https://www.aclweb.org/anthology/2020.acl-main.156.
Ortony A, Clore GL, Foss MA (1987) The referential structure of the aﬀective lexicon. Cognitive science
11(3):341–364.
Pan SJ, Yang Q (2009) A survey on transfer learning. IEEE Transactions on knowledge and data engineering
22(10):1345–1359.
Patwa P, Aguilar G, Kar S, Pandey S, PYKL S, Gamb¨ack B, Chakraborty T, Solorio T, Das A (2020)
Semeval-2020 task 9: Overview of sentiment analysis of code-mixed tweets. arXiv e-prints arXiv–2008.
Pedrosa AL, Bitencourt L, Fr´oes ACF, Cazumb´a MLB, Campos RGB, de Brito SBCS, e Silva ACS (2020)
Emotional, behavioral, and psychological impact of the covid-19 pandemic. Frontiers in psychology 11.
Pennebaker JW, Francis ME, Booth RJ (2001) Linguistic inquiry and word count: Liwc 2001. Mahway:
Lawrence Erlbaum Associates 71(2001):2001.
24

--- Page 25 ---

Peters ME, Neumann M, Iyyer M, Gardner M, Clark C, Lee K, Zettlemoyer L (2018) Deep contextualized
word representations. arXiv preprint arXiv:1802.05365 .
Pfeﬀerbaum B, North CS (2020) Mental health and the covid-19 pandemic. New England Journal of Medicine
.
Plutchik R (1980) A general psychoevolutionary theory of emotion. Theories of emotion, 3–33 (Elsevier).
Pota M, Marulli F, Esposito M, De Pietro G, Fujita H (2019) Multilingual pos tagging by a composite deep
architecture based on character-level features and on-the-ﬂy enriched word embeddings. Knowledge-
Based Systems 164:309–323.
Radford A, Narasimhan K, Salimans T, Sutskever I (2018) Improving language understanding by generative
pre-training.
Radford A, Wu J, Child R, Luan D, Amodei D, Sutskever I (2019) Language models are unsupervised
multitask learners. OpenAI blog 1(8):9.
Rosaldo MZ, Shweder RA, LeVine RA (1984) Culture theory: essays on mind, self, and emotion.
Schuster M, Nakajima K (2012) Japanese and korean voice search. 2012 IEEE International Conference on
Acoustics, Speech and Signal Processing (ICASSP), 5149–5152 (IEEE).
Shapira N, Lazarus G, Goldberg Y, Gilboa-Schechtman E, Tuval-Mashiach R, Juravski D, Atzil-Slonim D
(2020) Using computerized text analysis to examine associations between linguistic features and clients’
distress during psychotherapy. Journal of counseling psychology .
Sima’an K, Itai A, Winter Y, Altman A, Nativ N (2001) Building a tree-bank of modern hebrew text.
Traitement Automatique des Langues 42(2):247–380.
Steiner T (2016) President rivlin’s” four tribes” initiative: The foreign policy implications of a democratic
& inclusive process to address israel’s socio-demographic transformation .
Straka M, Hajic J, Strakov´a J (2016) Udpipe: trainable pipeline for processing conll-u ﬁles performing
tokenization, morphological analysis, pos tagging and parsing. Proceedings of the Tenth International
Conference on Language Resources and Evaluation (LREC’16), 4290–4297.
Tay Y, Dehghani M, Bahri D, Metzler D (2020) Eﬃcient transformers:
A survey. arXiv preprint
arXiv:2009.06732 .
Tsarfaty R, Bareket D, Klein S, Seker A (2020) From spmrl to nmrl: What did we learn (and unlearn) in a
decade of parsing morphologically-rich languages (mrls)? arXiv preprint arXiv:2005.01330 .
Tsarfaty R, Seddah D, Goldberg Y, K¨ubler S, Versley Y, Candito M, Foster J, Rehbein I, Tounsi L (2010)
Statistical parsing of morphologically rich languages (spmrl) what, how and whither. Proceedings of the
NAACL HLT 2010 First Workshop on Statistical Parsing of Morphologically-Rich Languages, 1–12.
Ullah R, Amblee N, Kim W, Lee H (2016) From valence to emotions: Exploring the distribution of emotions
in online product reviews. Decision Support Systems 81:41–53.
Vania C, Grivas A, Lopez A (2018) What do character-level models learn about morphology? the case of
dependency parsing. arXiv preprint arXiv:1808.09180 .
Vaswani A, Shazeer N, Parmar N, Uszkoreit J, Jones L, Gomez AN, Kaiser  L, Polosukhin I (2017) Attention
is all you need. Advances in neural information processing systems, 5998–6008.
Wierzbicka A (1994) Emotion, language, and cultural scripts. .
Wolf T, Debut L, Sanh V, Chaumond J, Delangue C, Moi A, Cistac P, Rault T, Louf R, Funtowicz M, Davison
J, Shleifer S, von Platen P, Ma C, Jernite Y, Plu J, Xu C, Scao TL, Gugger S, Drame M, Lhoest
Q, Rush AM (2020) Transformers: State-of-the-art natural language processing. Proceedings of the
2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations, 38–
45 (Online: Association for Computational Linguistics), URL https://www.aclweb.org/anthology/
2020.emnlp-demos.6.
Wu Y, Schuster M, Chen Z, Le QV, Norouzi M, Macherey W, Krikun M, Cao Y, Gao Q, Macherey K, et al.
(2016) Google’s neural machine translation system: Bridging the gap between human and machine
translation. arXiv preprint arXiv:1609.08144 .
Yadav A, Vishwakarma DK (2020) Sentiment analysis using deep learning architectures: a review. Artiﬁcial
Intelligence Review 53(6):4335–4385.
25

--- Page 26 ---

Yin W, Kann K, Yu M, Sch¨utze H (2017) Comparative study of cnn and rnn for natural language processing.
arXiv preprint arXiv:1702.01923 .
Yue L, Chen W, Li X, Zuo W, Yin M (2019) A survey of sentiment analysis in social media. Knowledge and
Information Systems 1–47.
Zampieri M, Malmasi S, Nakov P, Rosenthal S, Farra N, Kumar R (2019) Semeval-2019 task 6: Identifying
and categorizing oﬀensive language in social media (oﬀenseval). arXiv preprint arXiv:1903.08983 .
Zhang L, Wang S, Liu B (2018) Deep learning for sentiment analysis: A survey. Wiley Interdisciplinary
Reviews: Data Mining and Knowledge Discovery 8(4):e1253.
Zhong P, Wang D, Miao C (2019) Knowledge-enriched transformer for emotion detection in textual conver-
sations. arXiv preprint arXiv:1909.10681 .
Zhou D, Wu S, Wang Q, Xie J, Tu Z, Li M (2020) Emotion classiﬁcation by jointly learning to lexiconize and
classify. Proceedings of the 28th International Conference on Computational Linguistics, 3235–3245.
26

```
