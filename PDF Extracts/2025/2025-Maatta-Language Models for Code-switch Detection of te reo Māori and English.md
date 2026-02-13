---
title: "2025-Maatta-Language Models for Code-switch Detection of te reo Māori and English - PDF Extract"
source_pdf: "2025-Maatta-Language Models for Code-switch Detection of te reo Māori and English.pdf"
pages: 11
extracted_at: "2026-02-13T14:50:54.726588"
---

# PDF Extract: 2025-Maatta-Language Models for Code-switch Detection of te reo Māori and English

**Source PDF:** 2025-Maatta-Language Models for Code-switch Detection of te reo Māori and English.pdf
**Total Pages:** 11

---

## Content

```
--- Page 1 ---

Findings of the Association for Computational Linguistics: NAACL 2022, pages 650 - 660
July 10-15, 2022 ©2022 Association for Computational Linguistics
Language Models for Code-switch Detection of te reo M¯aori and English in
a Low-resource Setting
Jesin James1, Vithya Yogarajan2, Isabella Shields1, Catherine Watson1, Peter J Keegan3,
Peter-Lucas Jones4 and Keoni Mahelona4
1Dept. of Electrical, Computer, and Software Engineering, The University of Auckland
2Strong AI Lab, School of Computer Science, The University of Auckland
3Te Puna W¯ananga, The University of Auckland
4Te Hiku Media, New Zealand
Abstract
Te reo M¯aori, New Zealand’s only indige-
nous language, is code-switched with English.
M¯aori speakers are atleast bilingual, and the
use of M¯aori is increasing in New Zealand
English. Unfortunately, due to the minimal
availability of resources, including digital data,
M¯aori is under-represented in technological ad-
vances. Cloud-based multilingual systems such
as Google and Microsoft Azure support M¯aori
language detection. However, we provide ex-
perimental evidence to show that the accuracy
of such systems is low when detecting M¯aori.
Hence, with the support of M¯aori community,
we collect M¯aori and bilingual data to use nat-
ural language processing (NLP) to improve
M¯aori language detection. We train bilingual
sub-word embeddings and provide evidence to
show that our bilingual embeddings improve
overall accuracy compared to the publicly-
available monolingual embeddings. This im-
provement has been verified for various NLP
tasks using three bilingual databases containing
formal transcripts and informal social media
data. We also show that BiLSTM with pre-
trained M¯aori-English sub-word embeddings
outperforms large-scale contextual language
models such as BERT on down streaming tasks
of detecting M¯aori language. However, this
research uses large models ‘as is’ for transfer
learning, where no further training was done
on M¯aori-English data. The best accuracy of
87% was obtained using BiLSTM with bilin-
gual embeddings to detect M¯aori-English code-
switching points.
1
Introduction
Te reo M¯aori (referred to as M¯aori) is New
Zealand’s only indigenous language, spoken by
4.5% of the total population of 5 million. M¯aori
speakers are bilingual, and code-switching between
M¯aori and English is expected. M¯aori revitalisa-
tion efforts have increased M¯aori use in the other-
wise English-speaking country. Detecting M¯aori
language and code-switch instances is a prereq-
uisite to analysing language data. M¯aori and En-
glish both use the Roman script (specifically, M¯aori
uses a modified Roman script). Currently, annota-
tions are done manually, making the process time-
consuming and slowing down research and tech-
nology development. Consider the following sen-
tences:
(a) P¯er¯a an¯o i ng¯a mate kua hinga atu i te motu.
(b) I want to give no offence to my mate Willie
Jackson, but once a week hardly qualifies as
the significant M¯aori voice.
where green indicates M¯aori, red is used to indi-
cate that the word has same spelling in M¯aori and
English, and the remaining are English. Based on
expert knowledge, we know the word mate is M¯aori
in sentence (a) and English in sentence (b).
In this research, we focus on two primary tasks:
Task 1: Language Detection (LD) - detecting
M¯aori language words from input text.
Task 2: Code-switch Detection (CS) - detecting
M¯aori to English or English to M¯aori code-
switch points from input text.
There is limited M¯aori-only and M¯aori-English
bilingual data available. We collected data in col-
laboration with the M¯aori researchers, M¯aori tech-
nology developers and M¯aori community, where
data-sharing is based on trust.
As researchers,
we remain guardians of the data, ensuring data
sovereignty (Stats, 2020). Hence, all the resources
shared from this study are bound by the Kaitiaki-
tanga license (Te-Hiku-Media). This paper presents
some of the first research to use advances in NLP to
detect M¯aori language and code-switching. No ex-
isting models are using NLP techniques for M¯aori-
English code-switch detection. Google and Mi-
crosoft Azure’s cloud-based services are the only
options available for language detection, which is
the primary reason for using such large-scale multi-
lingual cloud-based services for comparison in this
paper.
650

--- Page 2 ---

This paper’s contributions are:
1. Evaluation of detecting M¯aori using multilin-
gual models, including the cloud-based ser-
vices such as Google and Azure, and large
scale language models such as Bidirectional
Encoder Representations from Transformers
(BERT).
2. Pre-training M¯aori-English bilingual, and
M¯aori-only monolingual sub-word embed-
dings using collected data. Experiments using
three different bilingual data for various NLP
tasks show that bilingual embeddings outper-
form monolingual embeddings.
3. Large scale language models such as BERT
–without further training on M¯aori-English
data– fine-tuned on down streaming tasks of
detecting M¯aori are outperformed by BiLSTM
with fastText pre-trained sub-word bilingual
embeddings for low-resourced language such
as M¯aori.
4. Providing baseline results for detecting low-
resourced M¯aori and code-switch between
M¯aori-English language pair.
2
Te reo M¯aori (The M¯aori Language)
M¯aori is a Polynesian language belonging to the
Austronesian family. Phonologically, M¯aori has
ten consonants /p t k m n N f r w h/. The M¯aori
vowel system is described by five short vowels /i
e a o u/ (Bauer et al., 1993). Orthographically,
there is mostly a one-to-one mapping of a M¯aori
phoneme to a grapheme, except for two digraphs,
‘wh’, which is /f/, and ‘ng’ which is /N/. In mod-
ern orthography, long vowels are denoted with a
macron (e.g. ¯a). In older texts, they are sometimes
expressed as double vowels (e.g. aa), with an um-
laut (e.g. ä), or ignored completely (that is, ¯a is writ-
ten a). In addition, there is some regional variation
in the way words are spelt (e.g. Aorangi vs Aoraki).
English, in contrast, has a highly non-phonemic or-
thography. The M¯aori syllable structure consists of
a nucleus, which may be occupied by a vowel (or
a diphthong), and an optional onset (syllable start)
occupied by a single consonant (consonant clusters
are not present in M¯aori) (Harlow, 2007).
3
Related Work
Research using NLP for tasks relating to M¯aori
is relatively young. Examples include statistical
machine translation for M¯aori-English pair (Mo-
haghegh et al., 2014) and the inclusion of M¯aori
language detection and translation using cloud ser-
vices Google and Azure (Keegan, 2017). (Keegan,
2017) indicates that although the growth of cloud
services for M¯aori translations is welcoming, due
to the minimal availability of digitised M¯aori data,
the resulting output is inaccurate. Google also ac-
knowledges that for low-resource languages, the
quality of language detection and automatic ma-
chine translation is far from perfect (Google-AI-
Blog).
We present the first research that uses deep learn-
ing techniques to detect a code-switch between
M¯aori and English. Hence, except for the Google
and Azure cloud services (more details in Sec-
tion 5.1), we are limited by the availability of
systems for M¯aori language detection and M¯aori-
English code-switch detection for comparison. We
use approaches that were inspired by the litera-
ture on other language pairs. Examples include
XNLI (Cross-lingual Natural Language Inference)
cross-lingual classification benchmark (Conneau
et al., 2018) where the bidirectional long short-term
memory (BiLSTM) model was used across sev-
eral low resource languages, including Swahili and
Urdu; and code-switch detection using BiLSTM
and Character-LSTM for language pair English-
Hindi (Lal et al., 2019; Mukherjee et al., 2019).
XNLI benchmark uses fastText common-crawl em-
beddings (denoted as E300 in this paper) and aligns
it with the MUSE library. Comparison among deep
learning models shows that adding background in-
formation through sub-word pre-trained embed-
dings trained using fastText and in the form of
lexicons improves the overall performance of deep
neural networks on databases of low-resource lan-
guages (Adouane et al., 2018).
Transformers such as BERT is the state-of-the-
art in many NLP tasks, including language detec-
tion, named entity recognition, and machine trans-
lation (Devlin et al., 2019; Conneau et al., 2020).
There are many large scale multilingual models,
such as XLM-R (Conneau et al., 2020) and multilin-
gual BERT (mBERT) (Devlin et al., 2019) trained
in more than 100 languages. Research shows that
for languages that are under-sampled during train-
ing, the effectiveness of large scale multilingual
models such as mBERT are sub-optimal (Wu and
Dredze, 2020; Wang et al., 2020). In comparison to
the contextual representations such as BERT, em-
beddings with sub-word representation are more
data-efficient when data availability is limited (Wu
651

--- Page 3 ---

Data
# Sentences
# Words
Text
Labels
Task
Hansard data0
2,021,261
36,757,230
formal
word-level & sentence level language labels
LD, CS
MLT corpus
2,500
50,000
informal
tweet level labels: relevance/irrelevance
LD
(Trye et al., 2019)
RMT corpus
79,018
1,000,000
informal
M¯aori words are identified and labelled
LD
(Trye et al., 2022)
Table 1: Databases used for experimental evaluations. LD: Language Detection, CS: Code-Switch Detection.
and Dredze, 2020). Furthermore, (Muller et al.,
2021) provide evidence to show that many under-
sampled or unseen languages during training –such
as Maltese or Narabizi– code-mixed with French
perform worse when using mBERT compared to
an RNN with non-contextual dependency parsing
baseline. It has been shown that for such unseen or
under-sampled languages, there is a need to further
train or fine-tune directly with available raw data in
the unseen target languages (Muller et al., 2021).
4
Databases
Due to the low-resource nature of the M¯aori lan-
guage, extensive databases are currently are un-
available.
We collected text data from differ-
ent sources to form the M¯aori-English Words
(MEW) database, as summarised in Table 2. MEW
database contains legal context, stories, social me-
dia posts and newspaper articles. The unlabelled
MEW database is used to pre-train bilingual and
M¯aori-only monolingual embeddings.
We use
three labelled databases for experiments: Hansard
database, MLT corpus, and RMT corpus. Details
of these databases are provided in Table 1.
Hansard database contains the New Zealand Par-
liament debates from 2003 onwards.
Together
with experts in M¯aori (Te-Hiku-Media), we have
labelled the Hansard database, where English or
M¯aori labels are assigned using linguistic rules and
manual checking. Each sentence in the databases
is marked as M¯aori, English or bilingual. Each
word of each sentence is labelled as M¯aori or En-
glish. The resulting data includes 102,559 bilin-
gual, 1,909,876 English-only and 8,826 M¯aori-only
sentences.
The M¯aori Loanword Twitter (MLT) corpus is
a small database, where each tweet is labelled as
‘relevant’ and ‘irrelevant’, based on the presence of
a pre-determined set of M¯aori loanwords in a given
tweet. Given detecting M¯aori language in tweets
is a prerequisite to this task, we consider this task
also as a M¯aori language detection task.
Name and Database
# Words
M¯aori only
D1: Te Taka Database*1
9,862,131
D2: Nga Mahi corpus (James et al., 2020)
81,036
D3: M¯aori Wikipedia
431,280
D4a: LMC Corpus2
5,486,328
Total size of M¯aori-only database = 92 MB
M¯aori and English
D4b: LMC Corpus
7,197,059
D5: Niupepa (M¯aori Newspapers)3
5,050,988
D6: Twitter Corpus*(Trye et al., 2019)
48,289,375
Total size of bilingual data = 0.4 GB
Table 2: M¯aori-English Words (MEW) database.‘*’ in-
dicates private collections of data.
Reo M¯aori Twitter (RMT) corpus contains
tweets, where at least 80% of text is in M¯aori. RMT
corpus provides a list of 879,000 M¯aori words
across the tweets. We use this corpus also for the
language detection task where the aim is to detect
the M¯aori words identified in the RMT corpus.
5
Language Models and Classifiers
This section provides details of the language mod-
els and classifiers we used. We evaluate the perfor-
mance of cloud-based language detection systems
from Google and Azure for M¯aori. We represent
text as bag-of-words and sub-word embeddings us-
ing fastText. We use logistic regression and multi-
nomial naive Bayes as baseline classifiers for lan-
guage detection. We also use neural networks such
as RNNs and CNNs to train and evaluate language
detection and code-switch detection tasks. Further-
more, we fine-tune transformer models, BERT and
mBERT, for the down streaming task of language
detection.
0https://www.parliament.nz/en/pb/
hansard-debates/rhr/
1Private collection of te reo M¯aori text data, Te Taka Kee-
gan, The University of Waikato, New Zealand, 2021
2http://nzetc.victoria.ac.nz/tm/
scholarly/tei-legalMaoriCorpus.html.
3http://www.nzdl.org/cgi-bin/library.
cgi?a=p&p=about&c=niupepa.
652

--- Page 4 ---

5.1
Cloud-based Online Tools
Google Translate4 and Microsoft Azure Cognitive
Services language detection5 are two popular cloud-
based online tools that can detect multiple lan-
guages. Google supports 108 languages, including
New Zealand English and M¯aori. Google’s RNN-
based GNMT (Google Neural Machine Trans-
lation) model (Wu et al., 2016) showed signif-
icant improvements in enabling translations to
cover many languages, including low-resourced
languages. Google recently replaced the GNMT
model with a hybrid model (transformer encoder
and RNN decoder). This model has shown signifi-
cant improvements compared to the other machine
translation systems. Azure’s cognitive services can
translate 100+ languages, including M¯aori. Azure’s
early-stage neural network model (Xiong et al.,
2017) included a CNN-BiLSTM architecture. Re-
cently, Azure has combined several machine learn-
ing algorithms and neural networks to provide vari-
ous cognitive services.
5.2
Bag of words
Bag of words (BOW) is an effective method (Gold-
berg, 2017; Joulin et al., 2017) to represent text as
a sparse vector, where the order of words in a docu-
ment is not considered. The number of occurrences
of a word or a binary value indicating that the word
is present in the document is stored.
5.3
Word Embeddings
For language processing tasks, continuous word
representations such as word embeddings trained
on large unlabelled databases facilitate effective
representation learning (Bojanowski et al., 2017;
Joulin et al., 2016). Here, we use fastText (Bo-
janowski et al., 2017) to learn word embeddings,
as novel words not present during training can
also be represented using fastText-based embed-
dings. This can be beneficial for a low-resource
setting. FastText supports two word embeddings
models: continuous bag-of-words (CBOW) and
Skip-grams (Mikolov et al., 2013). The CBOW
predicts the specific word from the source context.
Skip-gram predicts the source context from the spe-
cific word. The embeddings in this research are
trained to the specifications of Wikipedia and com-
mon crawl fastText models (Grave et al., 2018) (re-
4https://translate.google.com/
5https://azure.microsoft.com/en-us/
services/cognitive-services/translator/
Embeddings Model
Data
Size
# Unique
Words
Monolingual Embeddings
E300 (Grave et al., 2018)
downloaded
7GB
2,000,000
M¯aori-300/300SG
D1 - D4a
3GB
49,315
Bilingual Embeddings
Model-M¯aori-Eng-300
D1 - D6
3GB
303,505
(and 300SG)
Table 3: Outline of fastText pre-trained 300 dimensional
embeddings. The MEW database (Table 2) was used for
training. ‘SG’: Skipgram model, otherwise it is CBOW.
ferred to as E300) for both CBOW and Skip-gram6.
E300 uses the CBOW method, character n-grams
of length 5, window of size 5, and 10 negative sam-
ples per positive sample with 300 dimensions. The
learning rate is 0.05. Table 3 provides details of
our bilingual embeddings, which are available to
on request, including E300 details for comparison.
5.4
Baseline Classifiers
We used multinomial naive Bayes (John and Lang-
ley, 1995) and logistic regression (LR) (Cox, 1958)
to classify text features represented by BOW and
static word embeddings. LR is a statistical model
used to analyse databases where independent vari-
ables determine an outcome. Naive Bayes (John
and Langley, 1995) is an easy to build supervised
learning algorithm, which applies Bayes’ theorem
with the “naive” assumption of independence.
5.5
Convolutional Neural Network (CNN)
CNN for text (Kim, 2014) combines one-
dimensional convolutions with a max-over-time
pooling layer and a fully connected layer. If xi:i+j
is a concatenation of words from a sentence, each
word, xi, xi+1, ... is mapped to its k-dimensional
embeddings using word embeddings. A new fea-
ture is produced using convolution. Max-over-time
pooling is applied over the feature map to capture
the most important feature value. The final predic-
tion is made by computing a weighted combination
of the pooled values and applying Softmax activa-
tion function.
5.6
Recurrent Neural Networks (RNN)
RNNs (Rumelhart et al., 1986) are designed to
handle sequential data, such as text, where the
6Embeddings trained on a 4 core Intel i7-6700K CPU @
4.00GHz with 64GB of RAM. Average time: <30 minutes.
653

--- Page 5 ---

data contains complex temporal dependencies and
hidden information. Long Short Term Memory
networks (LSTM) (Hochreiter and Schmidhuber,
1997) are modified RNNs designed to overcome the
issue of vanishing gradient with RNNs. LSTM has
a gating mechanism consisting of input gate, for-
get gate, and output gate, ensuring a constant error
flow and avoiding long-term dependency problems.
The memory in LSTM is stored in an internal state,
and the three gates play a vital role in deciding
which information is to be included, added or re-
moved from the memory. Over time, the memory
cells learn which information is essential based on
the weights. Bidirectional RNNs are widely used
extensions where the input sequence is fed from
beginning to end and from end to beginning. For
BiLSTM (Grave et al., 2018), given there are two
LSTM layers, the hidden layer output is split into
two - for forward and backwards passes over the
input.
5.7
Transformers
BERT (Devlin et al., 2019) is one of the early
transformer models that apply bidirectional train-
ing of encoders (Vaswani et al., 2017) to lan-
guage modelling. The 12-layer BERT-base model
with a hidden size of 768, 12 self-attention heads,
110M parameter neural network architecture was
pre-trained from scratch on BookCorpus and En-
glish Wikipedia. The mBERT-base (Devlin et al.,
2019) model uses the same pre-training objective
as BERT-base and is pre-trained with Wikipedia
text of 104 languages with most articles. In this
research, we use BERT and mBERT to refer to
BERT-base and mBERT-base. It is vital to point out
that this research does not pre-train BERT models
(both BERT-base and mBERT-base) from scratch
or continuously on the very limited available M¯aori
language data.
Instead, this research only per-
forms fine tuning on down streaming task. There
are evidence on mBERT performance of zero-shot
tasks (Keung et al., 2020), and hence the decision
to limit this study to only fine-tuning. Pre-training
BERT models is out of scope of this current re-
search.
6
Experimental Setup
We experiment with various language models and
classifiers for two main tasks: language detection
(LD) and code-switch detection (CS). Our ultimate
goal is to find a combination of language modelling
and NLP techniques to improve the overall accu-
racy of LD and CS tasks. We use three databases
to evaluate these tasks with details provided in Ta-
ble 1. We use the Hansard database sentences as
the primary data for training and testing. All three
datasets were pre-processed by lower-casing and
using regular expressions to remove punctuation us-
ing Python 3.9 library with Pandas data frame. All
experimental results are obtained from a random
seeds training-testing scheme; 70% of the shuffled
data is used for training, with 10% for validation
and 20% for testing, and averaged over three runs.
The variation of these three independent runs is
within a range of ±0.015.
To represent text we use both fastText pre-trained
embeddings (see Table 3) and sparse vectors ob-
tained from BOW representations. An overview of
code-switch detection using trained models such as
BiLSTM and CNN is presented in Figure 1. This
diagram is an example to demonstrate the system
we used for end-to-end code-switch detection using
neural networks. Step 1 includes training and eval-
uating a neural network. We use the training set
of the Hansard database to train the model and use
validation loss as the stopping condition to avoid
over-fitting. In step 2, we load the trained model
and detect languages at the word level on testing
data. Once the language detection is done, the
points in the sentence where the language labels
switch from M¯aori to English or from English to
M¯aori are marked as code-switch points.
Neural network models presented in this re-
search are implemented using Keras/Tensorflow.
Adam (Kingma and Ba, 2015), an adaptive learning
rate optimisation algorithm, is used as the optimiser
for neural networks. Softmax activation function
is used in the output layer of the network. We use
a combination of dropout (Srivastava et al., 2014),
with a rate of 0.5, and early stopping (Zhang et al.,
2017) to avoid over-fitting. We use a maximum
length of 250 tokens (or words) for BiLSTM and
CNN, and padding for sentences with less than the
maximum length. The term tokens and words is
used interchangeably in this paper. The embed-
dings layer is with a dimension of 300. The hidden
units of BiLSTM are 128, and the hidden units of
one-dimensional convolutions are 128. For both
CNN and BiLSTM, categorical cross-entropy is
used as the loss function.
We also fine tune pre-trained transformers,
BERT and mBERT on the down streaming task
654

--- Page 6 ---

Figure 1: Code-switch detection using neural networks. Example shows ‘English’ words {Everyone, who, spoke, at,
those, meetings, did, so, with} are detected as ‘English’ and ‘aroha’ detected as ‘M¯aori’.
of language detection. We use batch size of 16,
maximum sequence length of 256 and learning rate
of 1e-5. For both BERT and mBERT, the loss and
accuracy were reported at each epoch. For both
BERT and mBERT, the model converges fast, need-
ing an average of 5 epochs per run.
All evaluations were done using Sklearn met-
rics7. Evaluations using baseline classifiers such as
multilingual naive Bayes and LR with BOW and
static features from embeddings require CPU only8
machines and are very quick to train and evaluate.
Neural networks require GPU devices9 for efficient
training and testing. The average training time for
CNN was 150-180 minutes, and BiLSTM was 300-
360 minutes, while BERT and mBERT required
240 minutes per epoch being trained for an aver-
age of 5 epochs. The testing time for trained deep
learning models is rapid, requiring a few minutes.
The code used in this research is made available10.
We present overall macro-F1 score and weighted-
7https://scikit-learn.org/stable/
modules/generated/
84 core Intel i7-6700K CPU @ 4.00GHz with 64GB of
RAM.
912 core Intel(R) Xeon(R) W-2133 CPU @ 3.60GHz,
GV100GL
10Pre-trained
bilingual
and
monolingual
embed-
dings are available for researchers on request.
Ex-
perimental
details,
model
implementations,
and
trained language models are available for researchers,
all
bound
by
the
Kaitiakitanga
license:
https:
//github.com/MaoriEnglish-Codeswitch/
MaoriEnglish-CodeSwitch-Detection
F1 score to provide different insights (Toftrup et al.,
2021; Khanuja et al., 2020). We also provide F1-
scores of each label where appropriate. Macro-
F1 provides average per-language results and is
equally important to all languages. The weighted-
F1 score considers the popularity of the languages
in the data set.
The Nemenyi posthoc test (95% confidence
level) identifies statistical differences between
learning methods. Critical Difference (CD) plots
show the average ranking of individual F1 scores
obtained using various language models. The lower
the rank, the better the model is. The difference in
average ranking is statistically significant if there
is no bold line connecting the two settings.
7
Experimental Results
The results are presented for the language detec-
tion (LD) tasks and code-switch detection (CS)
tasks. The language detection task is a crucial first
step for detecting code-switching (Rijhwani et al.,
2017; Barman et al., 2014). First, we present the
results of the language detection tasks using the
three databases (Table 1), followed by the results
of the code switch task using the Hansard database.
As indicated in the experimental setup, all exper-
imental results are obtained from a random seeds
training-testing scheme and averaged over three
runs. The variation of these three independent runs
is within a range of ±0.015.
655

--- Page 7 ---

Figure 2: Pie Chart of the languages detected by Google (left) and Azure (right) at word level for the test set of the
Hansard Database. The gold-standard label for all the words used here is ‘M¯aori’.
7.1
Task 1: Language Detection
7.1.1
Cloud-based Online Tools
To analyse the effectiveness of using Google Trans-
late and Azure services to detect M¯aori (and En-
glish), we experimented with the test set of the
Hansard database where the sentences are either
monolingual (M¯aori or English) or code-switched.
Google Translate detected 99.7% of the English
words, and Azure detected 97.8% of the English
words correctly. Figure 2 presents pie charts of the
resulting language detection for ‘M¯aori’ word (i.e.
the gold-standard labels for the words is ‘M¯aori’).
For M¯aori words, Google Translate detected with
an accuracy of 65.2%, and Azure detected with
an accuracy of 52%. Although the accuracy of
Google Translate was better than Azure, the error
rate of both services are too high for M¯aori lan-
guage detection. In addition, apart from wrongly
detecting M¯aori words as English, around 14-21%
of the words were classified as various other lan-
guages by both cloud services. We acknowledge
that cloud-based services such as Google and Azure
are multilingual and hence low-resource languages
such as M¯aori are dominated by the resource-rich
languages during training. This will inevitably in-
fluence the accuracy of LD of M¯aori using Google
and Azure’s cloud services. However, given there
is no other system available to detect M¯aori, it was
still vital to evaluate the outcome of the above men-
tioned cloud-based services.
7.1.2
Baseline Classifiers
LD task using the Hansard database is a multi-class
classification problem at the sentence level (classes:
M¯aori, English or Code-Switched sentence). The
LD task using MLT corpus is a binary classification
problem of relevant/irrelevant tweets based on the
usage of the M¯aori loanwords. Table 4 presents
Model
Data
Results
Multi-class
Macro-F1
Multinomial NB (BOW)
Hansard
0.887
LR (BOW)
Hansard
0.913
LR (Eng300)
Hansard
0.831
LR (M¯aori-Eng-300)
Hansard
0.853
LR (M¯aori-Eng-300SG)
Hansard
0.859
Binary
F1-score
LR (Eng300)
MLT corpus
0.833
LR (M¯aori-300SG)
MLT corpus
0.812
LR (M¯aori-Eng-300)
MLT corpus
0.849
LR (M¯aori-Eng-300SG)
MLT corpus
0.846
Table 4: Macro-F1 scores and F1-scores for the test set
of Hansard database and labelled MLT corpus respec-
tively, where BOW or sentence level features are used
to represent text. Bold: best results for each task.
overall macro-F1 and F1 scores for the LD task
using Hansard database and MLT corpus, respec-
tively, where BOW and static word embeddings
at the sentence level (or tweet level) are used to
represent the text. We obtain embeddings for each
sentence by computing the vector sum of the em-
beddings for each word in the sentence. This vec-
tor sum is then normalised to have length one, to
ensure that sentences of different lengths have rep-
resentations of similar magnitudes. The bilingual
embeddings perform better than monolingual em-
beddings for both Hansard and MLT corpus. How-
ever, BOW outperforms static embeddings feature
representation for LR.
7.1.3
Neural Networks
After evaluating the performance of baseline classi-
fiers, we further proceed with LD task using neural
networks. As the size of the labelled MLT corpus
is small, it is insufficient for training and evaluating
neural networks. Table 5 presents macro-F1 and
weighted-F1 scores obtained using the test set of
the Hansard database for performance comparison
656

--- Page 8 ---

Model
Macro-F1
Weighted-F1
Monolingual Embeddings
CNN (E300)
0.946
0.985
CNN (M¯aori-300)
0.905
0.986
CNN (M¯aori-300SG)
0.914
0.990
BiLSTM (E300)
0.943
0.996
BiLSTM (M¯aori-300)
0.926
0.995
BiLSTM (M¯aori-300SG)
0.940
0.995
Bilingual Embeddings
CNN (M¯aori-Eng-300)
0.963
0.995
CNN (M¯aori-Eng-300SG)
0.969
0.996
BiLSTM (M¯aori-Eng-300)
0.984
0.997
BiLSTM (M¯aori-Eng-300SG)
0.989
0.997
Contextual Embeddings
BERT-base
0.931
0.988
mBERT-base
0.946
0.991
Table 5: Comparison of results for the Hansard database
(test set) with various models. Bold: best results.
Figure 3: Critical difference plots identifying statistical
differences between models presented in Tables 4 & 5.
Model
Training
Testing
Accuracy
data
data
(M¯aori)
Google
Wikipedia
RMT
68.2%
BiLSTM (E300)
Hansard
RMT
56.6%
BiLSTM (M¯aori-Eng-300)
Hansard
RMT
85.4%
BiLSTM (M¯aori-Eng-300SG)
Hansard
RMT
85.6%
Table 6: Accuracy of M¯aori words detection in RMT
corpus using Hansard-based trained models (Table 5).
across language models. The macro-F1 score is
an unweighted average score of all the classes. In
comparison, weighted-F1 scores are higher than
macro-F1 scores across the models. The imbal-
anced distribution in the data, where labels are
predominantly English, is reflected in the scores
where the minority classes penalise the macro-F1
scores. Bilingual embeddings (M¯aori-Eng-300)
consistently perform better than monolingual em-
beddings. BiLSTM with M¯aori-Eng-300SG em-
beddings are the best across all models, including
BERT-base and mBERT-base. Skip-gram models
are better than CBOW. In comparison, English-only
embeddings E300 outperform M¯aori-only mono-
lingual embeddings. One possible explanation for
this is the lack of training data for M¯aori-only em-
beddings compared to E300.
Figure 3 presents critical difference plots across
the models presented in Table 5 and BOW repre-
sentation presented in Table 4. BiLSTM (M¯aori-
Eng-300SG) has the lowest rank, and multinomial
naive Bayes (BOW) has the highest rank with no
bold line connecting the two, indicating the dif-
ference in average ranking is statistically signifi-
cant. Bold lines are connecting BiLSTM (M¯aori-
Eng-300SG) with mBERT and BERT-base in the
CD-plot, indicating that the difference in average
ranking is not statistically significant. A 4-6 % im-
provement was observed between BERT/mBERT
and BiLSTM (M¯aori-Eng-300SG).
To further evaluate the language models, we used
the models trained with the Hansard data to detect
M¯aori words in the RMT corpus. Table 6 presents
the accuracy of the detection. We also present the
accuracy of M¯aori language detection using Google
Translate for comparison. Evidently, BiLSTM with
M¯aori-Eng-300SG embeddings model trained on
the training set of the Hansard database has the
best accuracy. As observed with other databases,
the accuracy of the bilingual embeddings is higher
than the monolingual embeddings. However, the
accuracy of BiLSTM with E300 embeddings is
considerably lower than other models, including
Google. One possible reason is the lack of vocab-
ulary in E300 for the informal language used in
RMT data (Tweets).
7.1.4
In Summary
The results suggest that the bilingual embeddings
perform better than monolingual embeddings (both
the downloaded Eng300 and M¯aori only models)
for the LD task. This finding was verified across the
Hansard database (Tables 4, 5) and the MLT corpus
(Table 4). Further evidence is provided in M¯aori
words detection using RMT corpus (Table 6). We
also observed that the bilingual embeddings outper-
formed the contextual embeddings. One possible
reason for this finding is the lack of vocabulary
in BERT models, as no further training was per-
formed using M¯aori data. This research only fine
tunes the BERT models for down streaming tasks.
As emphasised before, the M¯aori data availability
is the biggest limitation to this research. Among
the experimented models for LD task, BiLSTM
with M¯aori-Eng-300SG performed the best.
7.2
Task 2: Code-Switch Detection
For evaluation of the code-switch detection be-
tween M¯aori-English pair, we require word-level la-
bels and hence, only the Hansard database was used
for this task. We use selected trained models pre-
657

--- Page 9 ---

Figure 4: F1-scores for M¯aori and English calculated at
the word level for the Hansard database.
Model
CS: Accuracy
CNN (E300)
35%
BiLSTM (E300)
83%
BiLSTM (M¯aori-Eng-300)
67%
BiLSTM (M¯aori-Eng-300SG)
87%
Table 7: Accuracy of code-switch detection in the
Hansard data (bilingual sentences of the test set) us-
ing the trained models, as shown in Figure 1.
sented in Section 7.1, and identify the code-switch
points (see Figure 1). Figure 4 presents word-level
F1 scores of M¯aori and English for CS task. For
English words, all systems perform equally well.
However, for M¯aori, cloud-based multilingual sys-
tems perform poorly, and BiLSTM with bilingual
embeddings shows a substantial improvement in
F1 score, as observed before. It is vital to point out,
cloud-based services such as Google and Azure are
multilingual models and these systems have to clas-
sify between large number of languages. Hence,
the poor performance with detecting M¯aori is not
surprising, especially when compared to models
which only have to classify between English and
M¯aori. However, we include the results of large
scale models here to emphasise the fact that the
only existing tool that can detect M¯aori have lim-
itations. Furthermore, Table 7 presents the accu-
racy of detecting the code-switch points of the test
set of the Hansard database. Among the reported
results, CNN with E300 performed poorly, and
BiLSTM with M¯aori-Eng-300SG outperformed the
other models.
8
Discussion and Conclusions
This research is the first attempt to use advances
in NLP in two tasks - M¯aori (a low-resourced
language) language detection, and M¯aori-English
code-switch detection. Our experiments show that
the accuracy of existing cloud-based systems to de-
tect M¯aori is very low. Hence, there is the need to
have more specialised systems for detecting M¯aori.
We collected data in collaboration with M¯aori
researchers for training and evaluations. Experi-
ments obtained across tasks using three databases
show that our bilingual embeddings outperformed
downloaded, pre-trained English-only embeddings
trained on large databases. Among the models
tested, BiLSTM with bilingual embeddings trained
using the Skip-gram model is the best for both
tasks. We provide evidence to show BERT-base
used on the down-streaming task of language detec-
tion –where M¯aori is under-represented or unseen
by the model vocabulary– is not always the best
solution (as also observed by (Wu and Dredze,
2020; Wang et al., 2020)). For most low-resourced
languages, including M¯aori, the Wikipedia data is
significantly smaller than English, resulting in a
reduced vocabulary. Due to limited resources, con-
tinuous training or training from scratch of models
such as BERT-base is not possible.
For future work, it is a possibility to use ideas
such as Extend M-BERT (Wang et al., 2020) and
explore more efficient pre-training techniques to
improve the accuracy of BERT like models for lan-
guage detection of low-resource languages such
as M¯aori. In addition, hybrid models using hand-
crafted rules based on the phonotactic differences
between the languages and deep learning-based
methods are a promising pathway for future work.
The availability of digitised M¯aori and bilingual
data is limited, which restricts the ability to train
large language models. In addition, considering
this is the first deep learning-based research in this
area, comparison with published work is not pos-
sible. We overcome these limitations by respect-
ing the available data and data sovereignty for this
research. We provide experimental results using
cloud services such as Google and Azure, as these
are the only available systems that can detect M¯aori.
The study reported here is a much-needed contri-
bution to M¯aori language technology development.
Word embeddings developed in this research are
available to other researchers on request, bound by
the Kaitiakitanga license.
Acknowledgements
Thanks to all researchers who shared their data col-
lections with us, and to the University of Auckland
Faculty Research Development Fund (FRDF) 2020
for support. We also thank Human Aspects of Soft-
ware Engineering Lab (HASEL) at the University
of Auckland for the computing facilities.
658

--- Page 10 ---

References
Wafia Adouane, Jean-Philippe Bernardy, and Simon
Dobnik. 2018.
Improving neural network perfor-
mance by injecting background knowledge: Detect-
ing code-switching and borrowing in algerian texts.
In Proc. of the Third Workshop on Computational Ap-
proaches to Linguistic Code-Switching, pages 20–28.
Utsab Barman, Amitava Das, Joachim Wagner, and Jen-
nifer Foster. 2014. Code mixing: A challenge for
language identification in the language of social me-
dia. In Proc. of the first workshop on computational
approaches to code switching, pages 13–23.
Winifred Bauer, William Parker, and Te Kareongawai
Evans. 1993. In M¯aori. London: Routledge.
Piotr Bojanowski, Edouard Grave, Armand Joulin, and
Tomas Mikolov. 2017. Enriching word vectors with
subword information. Transactions of the Associa-
tion for Computational Linguistics, 5:135–146.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
Vishrav Chaudhary, Guillaume Wenzek, Francisco
Guzmán, Edouard Grave, Myle Ott, Luke Zettle-
moyer, and Veselin Stoyanov. 2020. Unsupervised
cross-lingual representation learning at scale. In Proc.
ACL Conference.
Alexis Conneau, Guillaume Lample, Ruty Rinott, Adina
Williams, Samuel R Bowman, Holger Schwenk, and
Veselin Stoyanov. 2018. XNLI: Evaluating Cross-
lingual Sentence Representations. In Proc. EMNLP,
pages 2475–2485.
David R Cox. 1958. The regression analysis of binary
sequences. Journal of the Royal Statistical Society:
Series B (Methodological), 20(2):215–232.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. BERT: Pre-training of
deep bidirectional transformers for language under-
standing. In Proc. of the 2019 Conference of the
North American Chapter of the Association for Com-
putational Linguistics: Human Language Technolo-
gies, Volume 1 (Long and Short Papers), pages 4171–
4186.
Yoav Goldberg. 2017. Neural network methods for
natural language processing. Synthesis Lectures on
Human Language Technologies, 10(1):1–309.
Google-AI-Blog.
Google
AI
Blog:
Recent
advances
in
Google
Translate.
https:
//ai.googleblog.com/2020/06/
recent-advances-in-google-translate.
html, accessed Dec 15 2021.
Edouard Grave, Piotr Bojanowski, Prakhar Gupta, Ar-
mand Joulin, and Tomas Mikolov. 2018. Learning
word vectors for 157 languages. In Proc. of the In-
ternational Conference on Language Resources and
Evaluation, pages 3483–3487.
Ray Harlow. 2007. M¯aori: A linguistic introduction.
Cambridge University Press.
Sepp Hochreiter and Jürgen Schmidhuber. 1997. Long
short-term memory. Neural computation, 9(8):1735–
1780.
Jesin James, Isabella Shields, Rebekah Berriman, Pe-
ter J. Keegan, and Catherine I. Watson. 2020. Devel-
oping Resources for Te Reo M¯aori Text To Speech
Synthesis System. In Proc. Sojka P., Kopeˇcek I., Pala
K., Horák A. (eds) Text, Speech, and Dialogue, Lec-
ture Notes in Computer Science, pages 294–302.
George H John and Pat Langley. 1995. Estimating con-
tinuous distributions in bayesian classifiers. In Proc.
Conference on Uncertainty in Artificial Intelligence,
pages 338–345.
Armand Joulin, Edouard Grave, Piotr Bojanowski,
Matthijs Douze, Hérve Jégou, and Tomas Mikolov.
2016. Fasttext. zip: Compressing text classification
models. arXiv preprint arXiv:1612.03651.
Armand Joulin, Edouard Grave, Piotr Bojanowski, and
Tomas Mikolov. 2017. Bag of tricks for efficient text
classification. In Proc. of the 15th Conference of the
European Chapter of the Association for Computa-
tional Linguistics: Volume 2, Short Papers, pages
427–431.
Te Taka Adrian Gregory Keegan. 2017.
Machine
translation for te reo M¯aori. He Whare Hangarau
M¯aori - Language, culture & technology, Editors:
Whaanga, H., Keegan, T. T., Apperley, M.. 23-28. Te
Pua W¯ananga ki te Ao / Faculty of M¯aori and In-
digenous Studies, Te Whare W¯ananga o Waikato /
University of Waikato, pages 23–28.
Phillip Keung, Yichao Lu, Julian Salazar, and Vikas
Bhardwaj. 2020.
Don’t use english dev: On the
zero-shot cross-lingual evaluation of contextual em-
beddings. In Proceedings of the 2020 Conference on
Empirical Methods in Natural Language Processing
(EMNLP), pages 549–554.
Simran Khanuja, Sandipan Dandapat, Anirudh Srini-
vasan, Sunayana Sitaram, and Monojit Choudhury.
2020.
GLUECoS: An evaluation benchmark for
code-switched NLP. In Proc. of the 58th Annual
Meeting of the Association for Computational Lin-
guistics, pages 3575–3585.
Yoon Kim. 2014. Convolutional neural networks for
sentence classification. In Proc. of the 2014 Con-
ference on Empirical Methods in Natural Language
Processing (EMNLP), pages 1746–1751.
Diederik P Kingma and Jimmy Ba. 2015. Adam: A
method for stochastic optimization. In Proc. Inter-
national Conference on Learning Representations
(ICLR), pages 1–13.
Yash Kumar Lal, Vaibhav Kumar, Mrinal Dhar, Manish
Shrivastava, and Philipp Koehn. 2019. De-mixing
sentiment from code-mixed text. In Proc. of the 57th
Annual Meeting of the Association for Computational
Linguistics: Student Research Workshop, pages 371–
377.
659

--- Page 11 ---

Tomas Mikolov, Kai Chen, Greg Corrado, and Jef-
frey Dean. 2013.
Efficient estimation of word
representations in vector space.
arXiv preprint
arXiv:1301.3781.
Mahsa Mohaghegh, Michael McCauley, and Mehdi Mo-
hammadi. 2014. M¯aori-English machine translation.
in Proc. NZCSRSC New Zealand Computer Science
Research Student Conference, Canterbury University.
Unitec Research Bank.
Siddhartha Mukherjee, Vinuthkumar Prasan, Anish
Nediyanchath, Manan Shah, and Nikhil Kumar. 2019.
Robust deep learning based sentiment classification
of code-mixed text. In Proc. of the 16th International
Conference on Natural Language Processing, pages
124–129.
Benjamin Muller, Antonios Anastasopoulos, Benoît
Sagot, and Djamé Seddah. 2021. When being un-
seen from mBERT is just the beginning: Handling
new languages with multilingual language models.
In Proc. of the 2021 Conference of the North Amer-
ican Chapter of the Association for Computational
Linguistics: Human Language Technologies, pages
448–462.
Shruti Rijhwani, Royal Sequiera, Monojit Choudhury,
Kalika Bali, and Chandra Shekhar Maddila. 2017.
Estimating code-switching on twitter with a novel
generalized word-level language detection technique.
In Proc. of the 55th annual meeting of the associa-
tion for computational linguistics (volume 1: long
papers), pages 1971–1982.
David E Rumelhart, Geoffrey E Hinton, and Ronald J
Williams. 1986. Learning representations by back-
propagating errors. Nature, 323(6088):533–536.
Nitish Srivastava, Geoffrey Hinton, Alex Krizhevsky,
Ilya Sutskever, and Ruslan Salakhutdinov. 2014.
Dropout: A simple way to prevent neural networks
from overfitting. Journal of Machine Learning Re-
search, 15(56):1929–1958.
N. Z. Stats. 2020.
Ng¯a tikanga paihere:
a
framework
guiding
ethical
and
culturally
appropriate
data
use.
Guidelines,
page
8.
https://data.govt.nz/toolkit/
data-ethics/nga-tikanga-paihere/.
Te-Hiku-Media.
Kaitiakitanga
license.
https://github.com/TeHikuMedia/
Kaitiakitanga-License, accessed 10 Dec
2021.
Te-Hiku-Media. Te Hiku Media. https://tehiku.
nz/te-hiku-tech/papa-reo/.
Mads Toftrup, Søren Asger Sørensen, Manuel R.
Ciosici, and Ira Assent. 2021. A reproduction of
apple’s bi-directional LSTM models for language
identification in short strings. In Proc. of the 16th
Conference of the European Chapter of the Associa-
tion for Computational Linguistics: Student Research
Workshop, pages 36–42.
David Trye, Andreea S Calude, Felipe Bravo-Marquez,
and Te Taka Adrian Gregory Keegan. 2019. M¯aori
loanwords: a corpus of New Zealand English tweets.
In Proc. of the 57th Annual Meeting of the Associa-
tion for Computational Linguistics: Student Research
Workshop, pages 136–142.
David Trye, Te Taka Keegan, Paora Mato, and Mark
Apperley. 2022. Harnessing indigenous tweets: The
Reo M¯aori Twitter corpus. Language resources and
evaluation, pages 1–40.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz
Kaiser, and Illia Polosukhin. 2017. Attention is all
you need. Advances in neural information processing
systems, 30:5998–6008.
Zihan Wang, K Karthikeyan, Stephen Mayhew, and
Dan Roth. 2020. Extending multilingual bert to low-
resource languages. In Proc. of the 2020 Conference
on Empirical Methods in Natural Language Process-
ing: Findings, pages 2649–2656.
Shijie Wu and Mark Dredze. 2020. Are all languages
created equal in multilingual BERT? In Proc. of the
5th Workshop on Representation Learning for NLP,
pages 120–130.
Yonghui Wu, Mike Schuster, Zhifeng Chen, Quoc V Le,
Mohammad Norouzi, Wolfgang Macherey, Maxim
Krikun, Yuan Cao, Qin Gao, Klaus Macherey, et al.
2016. Google’s neural machine translation system:
Bridging the gap between human and machine trans-
lation. arXiv preprint arXiv:1609.08144.
Wayne Xiong, Jasha Droppo, Xuedong Huang, Frank
Seide, Mike Seltzer, Andreas Stolcke, Dong Yu, and
Geoffrey Zweig. 2017. The microsoft 2016 conversa-
tional speech recognition system. In Proc. Acoustics,
Speech and Signal Processing (ICASSP), 2017 IEEE
International Conference on, pages 5255–5259.
Chiyuan Zhang, Samy Bengio, Moritz Hardt, Benjamin
Recht, and Oriol Vinyals. 2017. Understanding deep
learning requires re-thinking generalization. In Proc.
International Conference on Learning Representa-
tions 2017, pages 1–15.
660

```
