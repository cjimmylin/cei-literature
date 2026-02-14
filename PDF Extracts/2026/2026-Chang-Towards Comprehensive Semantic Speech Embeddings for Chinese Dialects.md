---
title: "2026-Chang-Towards Comprehensive Semantic Speech Embeddings for Chinese Dialects - PDF Extract"
source_pdf: "2026-Chang-Towards Comprehensive Semantic Speech Embeddings for Chinese Dialects.pdf"
pages: 9
extracted_at: "2026-02-13T17:43:27.774078"
---

# PDF Extract: 2026-Chang-Towards Comprehensive Semantic Speech Embeddings for Chinese Dialects

**Source PDF:** 2026-Chang-Towards Comprehensive Semantic Speech Embeddings for Chinese Dialects.pdf
**Total Pages:** 9

---

## Content

```
--- Page 1 ---

Towards Comprehensive Semantic Speech
Embeddings for Chinese Dialects
1st Kalvin Chang*
EECS Dept.
UC Berkeley
Berkeley, U.S.A.
kalvinchang@berkeley.edu
2nd Yiwen Shao
Tencent AI Labs
Tencent
Bellevue, U.S.A.
yiwenyshao@global.tencent.com
3rd Jiahong Li
Tencent AI Labs
Tencent
Shanghai, China
4th Dong Yu
Tencent AI Labs
Tencent
Bellevue, U.S.A.
Abstract—Despite having hundreds of millions of speakers,
Chinese dialects lag behind Mandarin in speech and language
technologies. Most varieties are primarily spoken, making dialect-
to-Mandarin speech-LLMs (large language models) more prac-
tical than dialect LLMs. Building dialect-to-Mandarin speech-
LLMs requires speech representations with cross-dialect semantic
alignment between Chinese dialects and Mandarin. In this paper,
we achieve such a cross-dialect semantic alignment by training
a speech encoder with ASR (automatic speech recognition)-
only data, as demonstrated by speech-to-speech retrieval on a
new benchmark of spoken Chinese varieties that we contribute.
Our speech encoder further demonstrates state-of-the-art ASR
performance on Chinese dialects. Together, our Chinese dialect
benchmark, semantically aligned speech representations, and
speech-to-speech retrieval evaluation lay the groundwork for
future Chinese dialect speech-LLMs. We release the benchmark
at https://github.com/kalvinchang/yubao.
Index Terms—Chinese dialects, ASR, cross-lingual alignment
I. INTRODUCTION
The performance of speech and language technologies for
Chinese dialects still lags behind that of Mandarin, despite the
former having 400 million speakers [1].
A. Background
Chinese dialects are mutually unintelligible. Thus linguists
classify them as distinct languages within the Sinitic family
[2], varieties within a macrolanguage [3], [4], or topolects
(regional varieties) [5]. We adopt the term dialect hereinafter
to be consistent with the ASR (automatic speech recognition)
literature. The mutually unintelligibility among Chinese di-
alects comes from the vast differences in their pronunciation
and lexicon [6]. Despite these differences, Chinese varieties
can be classified into a few subgroups: Mandarin, Xiang,
Gan, Wu, Min, Hakka, and Yue [2], and sometimes Jin, Hui,
Pinghua, and Tuhua [7]). Building speech and language tech-
nologies that support multiple dialect subgroups is inherently
a multilingual translation problem.
B. Motivation
Our ultimate goal is to build a speech translation model
that translates Chinese dialect speech to Mandarin text as
input to a large language model (LLM), to broaden access to
*Work completed during an internship at Tencent.
LLMs to speakers of Chinese dialects, thus encouraging use of
Chinese dialects. A speech translation model would be more
useful than a Chinese dialect ASR-LLM pipeline, since most
speakers do not write Chinese dialects. Even when Chinese
dialects are written, the orthography is not standardized for
all dialects [8], [9]. Within the same dialect, different scholars
or speakers may arrive at different Chinese characters to
represent dialect characters [10]. In informal settings, speakers
can use phonetically similar but semantically different Chinese
characters to transcribe Chinese dialect speech [11], [12]. This
phonetic approximation may even occur in data annotation. For
instance, in one of our training corpora, a Shanghainese Wu
utterance is transcribed as:
欧一生下来就啥个才会。(1)
where 欧is used to approximate the Shanghainese Wu
pronunciation of 我, the first-person singular pronoun, despite
欧not having such a meaning. In short, Chinese dialect
ASR is not our ultimate goal because differences in dialect
transcription prevent meaningful comparison across datasets
or even annotators; instead, we focus on text-free speech-to-
speech retrieval.
The first step in building a Chinese dialect-to-Mandarin
speech-LLM is to build a speech encoder that maps utterances
from different Chinese dialect subgroups, including Mandarin,
into a shared semantic space. The obvious solution would be to
train a dialect-to-Mandarin speech translation model. However,
paired dialect speech-Mandarin text (speech translation data)
is not as abundant as ASR data. For many dialect subgroups,
the problem necessarily becomes zero-shot speech translation
(to Mandarin). Even without paired ST data, we show that it
is still possible to induce a cross-dialect semantic space.
We learn speech representations where semantically similar
words and sentences have similar embeddings, demonstrating
cross-lingual (semantic) alignment [13]. The degree of such
alignment can be measured with retrieval, a task that tests
whether representations from a source language utterance can
be matched to representations of a semantically equivalent
utterance in a target language [13]. [14] in particular used
speech-to-speech retrieval on FLEURS [15] to show that
Whisper’s speech encoder has a cross-lingual semantic space,
which holds even after removing confounders like cognates
arXiv:2601.07274v1  [cs.CL]  12 Jan 2026

--- Page 2 ---

(shared words across related languages) and named entities
that might have inflated the retrieval scores [16]. Thus in this
paper, we leverage speech-to-speech retrieval to measure the
degree of cross-dialect alignment in our speech representation
space.1
Towards this end, we introduce YuBao, a new dataset of
parallel speech across Chinese dialects with comprehensive
coverage of Chinese dialect subgroups. Evaluated on speech-
to-speech retrieval using our new dataset YuBao, our speech
encoder demonstrates strong cross-dialect semantic alignment.
Our speech-to-speech retrieval benchmark provides an addi-
tional evaluation for future work on Chinese dialect speech-
LLMs.2
C. Related Work
Prior work on Chinese dialect ASR built speech-LLMs
[17]–[20],
self-supervised
speech
models
[21],
attention
encoder-decoder models [18], [22], [23], mixture-of-expert
models [24]. With the exception of Seed-ASR [17] and
TeleSpeech’s SSL model [21], prior work does not compre-
hensively cover major Chinese subgroups, often focusing on
Mandarin dialects only [18], [20], [25], [26], two or more
dialects [19], [22]–[24], [27]–[30], or a single dialect [22],
[31]–[36]. [37]’s survey of Chinese dialect ASR highlights
the need for an ASR model with comprehensive coverage of
Chinese dialects. Unlike related work, we achieve state-of-the-
art Chinese dialect ASR with a Zipformer encoder [38] and a
non-LLM attention decoder. Our model also comprehensively
covers most major Chinese dialect subgroups (minus Jin and
Gan).
Within prior work on Chinese dialect speech translation,
there is translation from Hokkien to Mandarin [39]–[41], from
Cantonese to English [42], and Taiwanese Hokkien to English
[43], but not multi-dialect translation to Mandarin. Our speech
representation space with cross-dialect semantic alignment
makes significant strides towards multi-dialect translation to
Mandarin.
D. Contribution
In short, we contribute the following:
• YuBao, a new Chinese dialect speech dataset with
comprehensive coverage of Chinese dialect subgroups
(Sec II-A)
• A state-of-the-art dialect ASR model with comprehensive
coverage of Chinese dialect subgroups (Sec II-B)
• Speech representations with cross-dialect semantic align-
ment induced with ASR-only data, measured by cross-
dialect speech-to-speech retrieval (Sec II-C)
II. METHODOLOGY
A. YuBao: a New Chinese Dialect Speech Benchmark
Our Chinese dialect speech retrieval benchmark comes from
the Centre for the Protection of Language Resources of China
1We chose speech-to-speech retrieval over speech-to-text retrieval because
strong comprehensive dialect text embeddings currently do not exist.
2We release the benchmark at https://github.com/kalvinchang/yubao
[44], which we abbreviate as YuBao (語保). The original
YuBao website has dialect speech, dialect transcripts, IPA
transcripts, and Mandarin translations for 1,000 characters,
1,200 words, and 50 sentences, all of which are parallel
(semantically aligned), across 1,300+ sites in China. For
our retrieval benchmark, we leveraged the up to 50 parallel
sentences available (some sites had slightly less than 50),
which consists of read speech from older males [44], who
are more likely to preserve more linguistic features of their
dialects than younger speakers. We chose 11 sites for each
subgroup of Chinese/Sinitic and additionally scraped 1 site,
Luanping, to represent Standard Mandarin, for a total of 78
sites, spanning the seven major subgroups: Mandarin (dialectal
Mandarin), Yue, Min (Southern Min/Minnan), Hakka, Xiang,
Wu, and Gan. We focused on sites where the subgrouping
info was provided by YuBao or sites where the subgrouping
is unambiguous (e.g. Changsha belonging to Xiang). The
Mandarin spoken in Luanping, Hebei—not Beijing—is the
closest to Standard Mandarin, phonetically speaking [45].
Overall, our retrieval benchmark consists of 3,499 utterances
on average 6.9 ± 3.0 seconds long, for a total of 6 hours, 45
minutes.
B. Dialect ASR with Comprehensive Coverage of Sinitic
Our Chinese dialect ASR model was trained on 34,000
hours of data with coverage of most major Chinese subgroups:
Mandarin, Yue, Wu, Min, Hakka, and Xiang (Tab. I). All
data is clean and has a 16k Hz sampling rate. The Chinese
dialect speech mostly contains spontaneous and read speech,
except for conversational Hakka. The proprietary dialectal
Mandarin and accented Mandarin data contains speech from
non-standard varieties of Mandarin and Mandarin spoken by
speakers whose native dialect is not Mandarin. This data
includes conversational speech from Dongbei (Northeastern)
Mandarin and spontaneous speech from the following cities or
regions across China: Zhengzhou, Lanzhou, Ningxia, Shanxi,
Liaoning, Yunnan, Hefei, Sichuan, Tianjin, Guilin, Wuhan,
Jiangxi, Hebei, Jinan, Zhejiang, Jiangsu, Anhui, Hunan, Fu-
jian, Xi’an, and Changsha. We did not modify noisy text
transcriptions (as highlighted in Ex. 1) as this is the result
of a lack of a standard orthography, and we did not have the
resources to re-annotate the entire corpus. Moving forward,
we concur with [9]’s call for more enforcing orthographic
standards in the transcription process.
We used a Zipformer encoder [38], which achieved state-
of-art ASR performance while being faster and less memory-
intensive than the Conformer [46] due to its U-Net-like
downsampling towards the middle. The Zipformer encoder
was trained with a joint pruned [47] RNN-T loss [48] and
attention loss [49], where label smoothing [50] was used for
the attention loss. We use the RNN-T head (joiner, decoder)
for ASR decoding and the attention head (commonly referred
to as the decoder) for translation (Sec. III-B). See Fig. 1 for
a diagram of the model. The model contains 186,806,275
parameters, with 19 Zipformer encoder layers and 6 Trans-
former decoder layers. The decoder is intentionally weak to

--- Page 3 ---

Fig. 1. Architecture of our models trained with ASR-only or ASR + speech
translation (ST) data (Sec. II-B). During training, ASR data goes through both
the RNN-T head and the attention head (“decoder”), while ST goes through
the attention head (“decoder”) only. During inference, the RNN-T head is
used for ASR, while the attention head (“decoder”) can be used for ST. The
gray boxes illustrate the speech encoder embeddings used in our retrieval
experiments.
TABLE I
DIALECT ASR AND SPEECH TRANSLATION TRAINING DATA
Subgroup
Corpus
Hours
Labels
Mandarin
WeNetSpeech [52]
10,005
ASR
KeSpeech [25]
1,396
ASR
AISHELL-1 [53], AISHELL-2 [54]
1,150
ASR
Mandarin dialects+accents across China
11,151
ASR
Yue
Cantonese
4,528
ASR
Wu
Shanghai
525
ASR
Shanghai2
493
ASR
Hangzhou
234
ASR
Suzhou
162
ASR
Min
Chaoshan
352
ASR
Hokkien
968
ASR
Hokkien2
141
ASR
Hakka
Meizhou
494
ASR, ST
Xiang
Changsha
984
ASR, ST
English
LibriSpeech [55]
960
ASR
En-Zh
Codeswitch-
ing
TALCS [56]
555
ASR
Total
All
34,098
-
concentrate semantic abilities in the encoder. To perform ASR
inference, greedy decoding was applied to the encoder only for
the data in Tab. II. We used [38]’s ScaledAdam optimizer and
Eden learning rate scheduler to train our model, which they
showed to converge more quickly than and perform better than
Adam [51].
TABLE II
DIALECT ASR TEST SET
Subgroup
Corpus
Hours
Mandarin
AISHELL-1 [53], AISHELL-2 [53]
10
KeSpeech [25]
31
Yue
CV-yue [57]
15 min
MDCC [34]
11
Wu
Shanghai
9.5
Shanghai2
9.5
Hangzhou
15
Suzhou
14
Min
Chaoshan
9
Hokkien
10
Hokkien2
10.5
Xiang
Changsha
10
C. Zero-shot Speech-to-speech Retrieval
We evaluated the cross-dialect semantic alignment of our
speech encoder with recall on the task of zero-shot speech-to-
speech retrieval [14], [58], [59], using our YuBao benchmark,
which consists of 50 parallel sentences from YuBao across
78 sites (Sec II-A). Given the speech representations of an
utterance in a source language, we retrieve the utterance in a
target language with the highest embedding similarity to the
source utterance’s representations. If the retrieved utterance
in the target language has the same meaning as the source
utterance, then the retrieved utterance is correct (see Fig. 2).
In other words, for each sentence in the source site, does the
sentence in the target site with the highest speech embedding
similarity have the same meaning as the source dialect? This
is measured by the recall rate between a pair of cities. We
compute the recall between all pairs of cities within a source
and target subgroup and report the mean.
The embedding similarity between the representations of a
source and a target utterance is measured with SeqSim, pro-
posed by [14]. SeqSim is essentially a frame-level BERTScore
[60], where for all source-target pairs of time steps (tokens in
NLP, frames in speech), we take the cosine similarity between
representations at the pair of time steps:
Reseq =
1
|X|
X
x∈X
max
y∈Y xTy
(1)
Prseq =
1
|Y |
X
y∈Y
max
x∈X xTy
(2)
SeqSim = 2 · Prseq · Reseq
Prseq + Reseq
(3)
where x, y ∈RD (single encoder frames), X ∈RT1×D, Y ∈
RT2×D (encoder embeddings). See Fig. 3 for an illustration.
If our encoder maps Chinese dialects to a shared semantic
space, then the speech-to-speech retrieval recall rate should be
above random.
III. EXPERIMENTS
A. Dialect ASR
Models were trained with icefall [61]. Data processing and
speech feature extraction were performed with lhotse [62].

--- Page 4 ---

Fig. 2. Illustration of speech-to-speech retrieval between a pair of dialect sites. Suppose there is a spoken corpus composed of 8 sentences with the same
meaning across different dialects. Then the goal is to measure how well the speech embeddings can match the utterance in a source dialect to the utterance
in the target dialect with the same meaning. The matching (retrieval) is done by identifying the target dialect utterance with the highest embedding similarity
(Fig. 3) to the source dialect utterance. Embedding similarity (Fig. 3) is computed for each each cell in this figure, which represents one pair of sentences
between a source and target dialect. A retrieved pair is identified as correct if both utterances have the same meaning, i.e. they lie along the diagonal in this
figure.
Fig. 3.
Illustration of how SeqSim [14] between a pair of Chinese dialect sites in YuBao is computed. The cosine similarity between all pairs of speech
encoder frames between a source utterance’s embeddings and a target utterance’s embeddings is calculated. Then the maximum similarity is taken across each
row and column to obtain the final SeqSim score according to (3).
We used FBANK features with 80 mel bins and applied
SpecAugment [63]. We applied text normalization to both
the reference and ASR hypotheses during evaluation on the
test set, converting traditional to simplified Chinese, removing
erhua, and introducing spaces between Chinese characters.
Each model was trained for 2 weeks using 32 GPUs. See
Tab. III for model and optimization hyperparameters.
As shown in Tab. IV, our Zipformer-based ASR model out-
performs the Paraformer [64] and FireRed-AED [18] models
for almost all Chinese varieties, except for Mandarin. The
Paraformer is considered a strong (Standard) Mandarin model
but was never trained on dialects. Similarly, FireRed-AED was
trained on Standard Mandarin and Mandarin dialects but not
others. Despite this, we compared our models with Paraformer
and FireRed AED because they are also attention encoder-
decoder models, as opposed to Speech-LLMs. Another reason
for choosing these two models was that ASR models trained
with comprehensive coverage of Chinese dialects, such as [17],
are not public. As for [21], only the SSL data had comprehen-
sive coverage of Chinese dialect subgroups; they did release
an ASR checkpoint, but it was only finetuned on Mandarin
dialects [25]. Additionally, [19], which has significantly larger
decoders than our models, is not public.
Surprisingly, Paraformer and FireRed-AED perform better
on the Changsha corpus than on other non-Mandarin test sets.
We hypothesize this is because Changsha Xiang belongs to the
New Xiang subcluster, which is similar to and even somewhat
intelligible with Southwestern Mandarin due to long-term

--- Page 5 ---

dialect contact [65].
TABLE III
ASR MODEL HYPERPARAMETERS
Hyperparameter
Value
Model:
feature dim
80
output downsampling factor
2
num encoder layers
[2, 2, 4, 5, 4, 2]
downsampling factor
[1, 2, 4, 8, 4, 2]
encoder dim
[192, 256, 512, 768, 512, 256]
feedforward dim
[576, 768, 1536, 2304, 1536, 768]
dropout
null
num heads
[4, 4, 4, 8, 4, 4]
query head dim
[32]
value head dim
[12]
pos head dim
[4]
pos dim
48
encoder unmasked dim
[192, 192, 256, 256, 256, 192]
cnn module kernel
[31, 31, 15, 15, 15, 31]
decoder dim
512
joiner dim
512
causal
false
chunk size
[16, 32, 64, -1]
left context frames
[64, 128, 256, -1]
special tokens
null
vocab size
2000
blank id
0
context size
2
max duration
400 seconds
Optimizer:
base lr
0.045
lr epochs
3.5
lr batches
7500
lr steps per epoch
100000
warmup batches
4000
lm scale
0.25
am scale
0
simple loss scale
0.5
rnnt warm step
2000
use fp16
True
attention loss scale
0.8
balance loss scale
0
specialization loss scale
0
B. ST
[14] improved the performance of X-to-Mandarin speech
translation by finetuning Whisper on English-to-Mandarin
speech translation. This suggests that finetuning on speech
translation strengthens the cross-lingual alignment already
present in Whisper (shown by speech-to-speech retrieval prior
to finetuning), even for languages not represented in the speech
translation data. We thus sought whether limited speech trans-
lation data can enhance the cross-dialect semantic retrieval.
We trained an additional Zipformer model using the 1478
hours of Hakka and Xiang ST data we had (Tab. I). The
hyperparameters of the ASR+ST model are the same as the
model trained with ASR-only data (Tab. III). Since [14], [66]
showed that speech translation with the ASR task token (with
the target language token) performs better than translation with
the ST task token, we do not use any task token and simply
use the Mandarin language token to perform speech translation
to Mandarin using the decoder. ASR data goes through both
the RNN-T and the attention head, while ST data only goes
through the attention head with the target language token as a
prefix. See Fig. 1 for a diagram of the model. (The ASR-only
model has the same architecture but was not trained on ST
data.) The model trained on ASR+ST data achieved similar
ASR performance to the model trained only on ASR data
(Tab. IV).
C. Retrieval
Our retrieval results, shown in Tab. V and Tab. VI, suggest a
cross-dialect shared space emerges, even with ASR-only data.
Unsurprisingly, the similarity between Standard Mandarin and
dialectal Mandarin—members of the same dialect subgroup—
is high in both directions. Furthermore, the Mandarin-dialect
and dialect-Mandarin retrieval recall rates are almost all above
80%, with the exception of Gan, which did not appear in
our training data. This demonstrates that the dialects share a
common semantic space with Mandarin, which suggests that
our speech encoder can be used with a Mandarin LLM. Specif-
ically, retrieving the correct Mandarin sentence for a dialect
sentence suggests that a Speech-LLM is likely to understand
the same sentence. Additionally, the retrieval recall is greatly
above random chance between all pairs of dialect subgroups
for both of our models, including between Standard Mandarin
and other subgroups (in both directions). This indicates that
both our models learn a cross-dialect semantic space between
all pairs of dialect subgroups, not just between Mandarin and
the dialects.
Additionally, that the model trained with ASR-only data
(Tab. VI) demonstrates similar retrieval recall to the model
trained with both ASR and ST data (Tab. V) suggests that
ASR-only data—not ST data—is sufficient to learn a cross-
dialect semantic space. This is surprising because [16] argue
that speech translation is the contributor behind cross-lingual
semantic alignment in speech-to-text foundation models.
We hypothesize that cross-dialect semantic alignment arises
from ASR-only data because of semantic supervision from
text transcripts. Language modeling in text learns a form
of distributional semantics [67], and multilingual language
models in particular can learn cross-lingual semantics even
without parallel data [68], [69]. Furthermore, using ASR
data is known to strengthen semantics when learning speech-
text alignment [70], [71]. This corroborates [16]’s finding
that OWSM v3.1 Small Low-Restriction [72], trained with
ASR-only data, demonstrates cross-lingual semantic retrieval
capabilities between related languages. In short, supervision
from text transcripts in our 34,000 hours of paired cross-
dialect speech and text imbues the encoder with a cross-dialect
semantic space.
IV. CONCLUSION AND FUTURE WORK
Our work has achieved state-of-the-art Chinese dialect ASR
performance across a comprehensive set of major Chinese
dialect subgroups using a Zipformer encoder. When evalu-
ated on zero-shot speech-to-speech retrieval using our new
YuBao benchmark—which has comprehensive coverage of

--- Page 6 ---

TABLE IV
CHARACTER ERROR RATE FOR OUR ZIPFORMER MODELS TRAINED ON
ASR+ST (320K STEPS) AND ASR ONLY DATA (312K STEPS), DECODED
WITH GREEDY SEARCH APPLIED TO THE ENCODER ONLY
ours
theirs
Subgroup
Corpus
ASR+ST
ASR-only
Paraformer
FireRed-AED
Mandarin
AISHELL
1.69
1.85
1.87
0.54
KeSpeech
5.45
5.75
11.26
4.85
Yue
CV-yue
7.44
7.48
73.23
45.79
MDCC
6.37
6.28
47.72
36.18
Wu
Shanghai
10.02
10.25
66.42
58.34
Shanghai2
7.36
7.54
66.70
56.14
Hangzhou
4.95
5.25
46.10
37.73
Suzhou
10.17
10.46
80.62
77.56
Min
Chaoshan
10.60
10.79
83.59
78.64
Hokkien
21.34
21.66
90.63
88.65
Hokkien2
21.00
22.01
92.19
89.20
Xiang
Changsha
6.21
7.83
33.94
28.71
TABLE V
SPEECH-TO-SPEECH RETRIEVAL RECALL RATES FOR ZIPFORMER MODEL
TRAINED WITH ASR AND ST DATA
(320K STEPS)
Source \Target
Mandarin (Std)
Mandarin (Dialect)
Min
Wu
Yue
Xiang
Gan
Mandarin (Std)
–
98.2
93.8
89.3
83.6
91.8
72.7
Mandarin (Dialect)
99.6
–
88.6
85.8
79.8
90.0
70.8
Min
95.3
90.0
–
85.3
80.8
87.5
69.2
Wu
95.3
89.6
86.1
–
75.7
87.8
69.5
Yue
87.5
80.0
79.6
72.7
–
78.3
62.1
Xiang
94.4
89.2
85.8
81.3
74.1
–
71.5
Gan
78.0
72.4
67.1
64.8
59.0
73.1
–
TABLE VI
SPEECH-TO-SPEECH RETRIEVAL RECALL RATES FOR ZIPFORMER MODEL
TRAINED WITH ASR DATA ONLY
(312K STEPS)
Source \Target
Mandarin (Std)
Mandarin (Dialect)
Min
Wu
Yue
Xiang
Gan
Mandarin (Std)
–
98.9
93.1
91.3
84.9
91.5
73.1
Mandarin (Dialect)
99.3
–
89.1
86.4
80.0
89.2
70.8
Min
94.5
90.0
–
86.4
80.5
87.1
68.4
Wu
93.5
88.7
87.4
–
74.9
87.1
68.9
Yue
85.6
78.7
79.9
72.2
–
76.7
61.2
Xiang
91.5
88.7
85.6
81.1
75.3
–
71.2
Gan
77.1
71.8
67.2
64.4
58.8
72.6
–
major Chinese dialect subgroups—our encoder representations
demonstrate strong cross-dialect semantic alignment. Our re-
trieval is particularly beneficial in settings like Chinese dialects
without standardized orthographies. We further showed that
such semantically aligned embeddings can be learned without
dialect-to-Mandarin ST data or data in scarce dialect-dialect
pairs, using ASR-only data. While we focused on Chinese
dialects, our approach can be applied to other closely related
language continua with mid- or high-resource varieties, such
as Bantu or Indic. It remains to be seen if this holds true for
phylogenetically unrelated languages.
In the future, we hope to expand the YuBao benchmark to all
1300 cities so that we can measure the zero-shot generalization
of the cross-dialect alignment to subclusters such as Eastern
Min (Mindong) not represented during training. We will
also strengthen the encoder’s cross-dialect semantic alignment
while still only using ASR-only data via teacher-student dis-
tillation [59], [73] via contrastive learning [74], [75] where a
noisy cross-dialect text model (e.g. SentenceBERT or a Man-
darin LLM finetuned on Chinese dialect ASR transcripts)—
assumed to have cross-dialect semantic alignment—will teach
the student speech model to push utterances with a similar
meaning together in the speech representation space. We also
seek to make the Zipformer encoder even more efficient using
Mixture-of-Experts [24]. Finally, we seek to create a language
family tree or clustering of Chinese dialects [76], [77] using
SeqSim [14], to be compared with linguists’ hypotheses about
how the Chinese dialects evolved from Old and Middle
Chinese [78].
V. ACKNOWLEDGMENTS
We acknowledge the efforts of [44] in collecting YuBao,
without which this work could not exist. In the spirit of this
paper’s focus on preserving linguistic diversity, we close by
expressing our gratitude in several Chinese varieties:
多謝to-si¯a (Minnan) / do1 ’xia5 (Gan) / do1 sie4 (Xiang)
恁仔細an2 zii2 se3 (Hakka)
唔該m4 goi1 (Yue)
謝謝xi`e xie (Mandarin) / 2zia6-zia6 (Wu)

--- Page 7 ---

REFERENCES
[1] Z. Du, The Chinese language demystified.
Cambridge Scholars
Publishing, 2015.
[2] Z.
Handel,
“The
classification
of
chinese:
Sinitic
(the
chinese
language family),” in The Oxford Handbook of Chinese Linguistics.
Oxford
University
Press,
04
2015.
[Online].
Available:
https:
//doi.org/10.1093/oxfordhb/9780199856336.013.0001
[3] International
Organization
for
Standardization,
“Online
browsing
platform (obp),” 2023. [Online]. Available: https://www.iso.org/obp/ui/
en/#iso:std:iso:639:ed-2:v1:en
[4] D. M. Eberhard, G. F. Simons, and C. D. Fennig, “Ethnologue: Lan-
guages of the world. twenty-fifth edition.” https://www.ethnologue.com/
language/zho, 2025.
[5] V. H. Mair, “What is a “Chinese dialect/topolect”?: Reflections on some
key Sino-English linguistic terms,” Sino-Platonic Papers, no. 29, 1991.
[6] D.-a. Ho, “Chinese dialects,” in The Oxford Handbook of Chinese
Linguistics.
Oxford University Press, 04 2015. [Online]. Available:
https://doi.org/10.1093/oxfordhb/9780199856336.013.0002
[7] R. Li, Language Atlas of China, second edition. The Commercial Press,
2012.
[8] P. Ueda, K. F. Law, and M. K. Chan, “Creating a Corpus: Issues in the
Digital Text Processing of Cantonese, Hakkanese, and Taigi,” Buckeye
East Asian Linguistics, no. 8, 2024.
[9] M.
Lau,
Q.
Chen,
Y.
Fang,
T.
Xu,
T.
Chen,
and
P.
Golik,
“Data
quality
issues
in
multilingual
speech
datasets:
The
need
for
sociolinguistic
awareness
and
proactive
language
planning,”
in Proceedings of the 63rd Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Papers), W. Che,
J. Nabende, E. Shutova, and M. T. Pilehvar, Eds.
Vienna, Austria:
Association for Computational Linguistics, Jul. 2025, pp. 7466–7492.
[Online]. Available: https://aclanthology.org/2025.acl-long.370/
[10] P. Cockrum, “Reanalyzing variation in written Taiwanese Southern Min:
Proposing a three camp framework,” Buckeye East Asian Linguistics,
no. 6, 2023.
[11] J. Liu, “Deviant writing and youth identity: Representation of dialects
with chinese characters on the internet,” Chinese Language and
Discourse, vol. 2, no. 1, pp. 58–79, 2011. [Online]. Available:
https://www.jbe-platform.com/content/journals/10.1075/cld.2.1.03liu
[12] H.-l. Khoo, “The dynamics of Southern Min in Taiwan: From Southern
Min dialects to “Taigi”,” in The Routledge Handbook of Chinese
Discourse Analysis.
Routledge, 2019, pp. 596–610.
[13] K. H¨ammerl, J. Libovick´y, and A. Fraser, “Understanding cross-
lingual Alignment—A survey,” in Findings of the Association for
Computational Linguistics: ACL 2024, L.-W. Ku, A. Martins, and
V. Srikumar, Eds.
Bangkok, Thailand: Association for Computational
Linguistics,
Aug.
2024,
pp.
10 922–10 943.
[Online].
Available:
https://aclanthology.org/2024.findings-acl.649/
[14] R. Ma, M. Qian, Y. Fathullah, S. Tang, M. Gales, and K. Knill,
“Cross-lingual transfer learning for speech translation,” in Proceedings
of the 2025 Conference of the Nations of the Americas Chapter
of the Association for Computational Linguistics: Human Language
Technologies (Volume 2: Short Papers), L. Chiruzzo, A. Ritter,
and L. Wang, Eds.
Albuquerque, New Mexico: Association for
Computational Linguistics, Apr. 2025, pp. 33–43. [Online]. Available:
https://aclanthology.org/2025.naacl-short.4/
[15] A. Conneau, M. Ma, S. Khanuja, Y. Zhang, V. Axelrod, S. Dalmia,
J. Riesa, C. Rivera, and A. Bapna, “FLEURS: Few-shot learning
evaluation of universal representations of speech,” in 2022 IEEE Spoken
Language Technology Workshop (SLT).
IEEE, 2023, pp. 798–805.
[16] R.
S.-E.
Shim,
D.
D.
Cristofaro,
C.
M.
Hu,
A.
Vietti,
and
B. Plank, “Languages in multilingual speech foundation models
align both phonetically and semantically,” 2025. [Online]. Available:
https://arxiv.org/abs/2505.19606
[17] Y. Bai, J. Chen, J. Chen, W. Chen, Z. Chen, C. Ding, L. Dong,
Q. Dong, Y. Du, K. Gao et al., “Seed-asr: Understanding diverse
speech and contexts with llm-based speech recognition,” arXiv preprint
arXiv:2407.04675, 2024.
[18] K.-T. Xu, F.-L. Xie, X. Tang, and Y. Hu, “Fireredasr: Open-source
industrial-grade mandarin speech recognition models from encoder-
decoder to llm integration,” arXiv preprint arXiv:2501.14350, 2025.
[19] T. Xu, H. Chen, Q. Wang, L. Hang, J. Kang, J. Li, Z. Lin, Y. Li,
and L. Xie, “Leveraging LLM and Self-Supervised Training Models for
Speech Recognition in Chinese Dialects: A Comparative Analysis,” pp.
584–588, 2025.
[20] T. Li, J. Liu, T. Zhang, Y. Fang, D. Pan, M. Wang, Z. Liang, Z. Li,
M. Lin, G. Dong et al., “Baichuan-audio: A unified framework for end-
to-end speech interaction,” arXiv preprint arXiv:2502.17239, 2025.
[21] H. Chen, Z. Li, G. Xia, B. Liu, Y. Yang, J. Kang, and J. Li, “Tele-
speechpt: Large-scale chinese multi-dialect and multi-accent speech pre-
training,” in Man-Machine Speech Communication, Z. Ling, X. Chen,
A. Hamdulla, L. He, and Y. Li, Eds.
Springer Nature Singapore, 2025,
pp. 183–190.
[22] A. Radford, J. W. Kim, T. Xu, G. Brockman, C. McLeavey,
and I. Sutskever, “Robust speech recognition via large-scale weak
supervision,” 2022. [Online]. Available: https://arxiv.org/abs/2212.04356
[23] T. Ding, K. Sun, X. Zhang, J. Yu, and D. Huang, “Chinese multi-dialect
speech recognition based on instruction tuning,” in Fourth Symposium on
Pattern Recognition and Applications (SPRA 2023), vol. 13162.
SPIE,
2024, pp. 71–80.
[24] Z. Jie, G. Shengxiang, Y. Zhengtao, D. Ling, and W. Wenjun,
“DialectMoE: An end-to-end multi-dialect speech recognition model
with mixture-of-experts,” in Proceedings of the 23rd Chinese National
Conference on Computational Linguistics (Volume 1: Main Conference),
M. Sun, J. Liang, X. Han, Z. Liu, and Y. He, Eds.
Taiyuan, China:
Chinese Information Processing Society of China, Jul. 2024, pp.
1148–1159. [Online]. Available: https://aclanthology.org/2024.ccl-1.89/
[25] Z. Tang, D. Wang, Y. Xu, J. Sun, X. Lei, S. Zhao, C. Wen, X. Tan,
C. Xie, S. Zhou et al., “Kespeech: An open source speech dataset of
Mandarin and its eight subdialects,” in Thirty-fifth Conference on Neural
Information Processing Systems Datasets and Benchmarks Track (Round
2), 2021.
[26] R. Shen, Y. Zhang, Y. Li, L. Jin, and J. Huang, “A multi-task approach
with multi-grained information extraction for dialect speech recogni-
tion,” in Proceedings of the 2024 4th International Conference on
Artificial Intelligence, Automation and Algorithms, 2024, pp. 51–56.
[27] Z. Dan, Y. Zhao, X. Bi, L. Wu, and Q. Ji, “Multi-task transformer
with adaptive cross-entropy loss for multi-dialect speech recognition,”
Entropy, vol. 24, no. 10, p. 1429, 2022.
[28] M. Chen, P. Liu, H. Yang, and H. Wang, “Towards end-to-end unified
recognition for mandarin and cantonese,” in Proc. Interspeech 2024,
2024, pp. 2365–2369.
[29] F. Zhang, X. Xie, and X. Quan, “Chinese dialect speech recognition
based on end-to-end machine learning,” in 2022 International Confer-
ence on Machine Learning, Control, and Robotics (MLCR).
IEEE,
2022, pp. 14–18.
[30] T. Feng, K. Huang, A. Xu, X. Shi, T. Lertpetchpun, J. Lee, Y. Lee,
D. Byrd, and S. Narayanan, “Voxlect: A speech foundation model
benchmark for modeling dialects and regional languages around the
globe,” arXiv preprint arXiv:2508.01691, 2025.
[31] Y.-H. Chou, K. Chang, M.-J. Wu, W. Ou, A. W.-H. Bi, C. Yang,
B. Y. Chen, R.-W. Pai, P.-Y. Yeh, J.-P. Chiang et al., “Evaluating
self-supervised speech models on a Taiwanese Hokkien corpus,” in
2023 IEEE Automatic Speech Recognition and Understanding Workshop
(ASRU).
IEEE, 2023, pp. 1–7.
[32] Y.-F. Liao, S.-H. Hwang, Y.-S. Chen, H.-C. Lai, Y.-H. Chung, L.-T. Shen,
Y.-C. Huang, C.-J. Huang, H. W. Han, L.-W. Chen et al., “Taiwanese
Hakka across Taiwan corpus and formosa speech recognition challenge
2023-hakka asr,” in 2023 26th Conference of the Oriental COCOSDA
International Committee for the Co-ordination and Standardisation of
Speech Databases and Assessment Techniques (O-COCOSDA).
IEEE,
2023, pp. 1–6.
[33] Y.-F. Liao, J. S. Tsay, P. Kang, H.-L. Khoo, L.-K. Tan, L.-C. Chang, U.-
G. Iunn, H.-L. Su, T.-G. Thiann, H.-K. Tiun et al., “Taiwanese Across
Taiwan corpus and its Applications,” in 2022 25th Conference of the
Oriental COCOSDA International Committee for the Co-ordination and
Standardisation of Speech Databases and Assessment Techniques (O-
COCOSDA).
IEEE, 2022, pp. 1–5.
[34] T. Yu, R. Frieske, P. Xu, S. Cahyawijaya, C. T. Yiu, H. Lovenia,
W. Dai, E. J. Barezi, Q. Chen, X. Ma, B. Shi, and P. Fung, “Automatic
speech recognition datasets in Cantonese: A survey and new dataset,”
in Proceedings of the Thirteenth Language Resources and Evaluation
Conference, N. Calzolari, F. B´echet, P. Blache, K. Choukri, C. Cieri,
T. Declerck, S. Goggi, H. Isahara, B. Maegaard, J. Mariani, H. Mazo,
J. Odijk, and S. Piperidis, Eds.
Marseille, France: European Language
Resources Association, Jun. 2022, pp. 6487–6494. [Online]. Available:
https://aclanthology.org/2022.lrec-1.696/

--- Page 8 ---

[35] X. Li, Y. Wang, X. Liu, K. Su, Z. Li, Y. Wang, B. Jiang, K. Xie,
and J. Liu, “Jlms25 and jiao-liao mandarin speech recognition based
on multi-dialect knowledge transfer.” Applied Sciences (2076-3417),
vol. 15, no. 3, 2025.
[36] F. Xu, M. Wang, and M. Li, “Building parallel monolingual Gan
Chinese dialects corpus,” in Proceedings of the Eleventh International
Conference on Language Resources and Evaluation (LREC 2018),
N. Calzolari, K. Choukri, C. Cieri, T. Declerck, S. Goggi, K. Hasida,
H. Isahara, B. Maegaard, J. Mariani, H. Mazo, A. Moreno, J. Odijk,
S. Piperidis, and T. Tokunaga, Eds.
Miyazaki, Japan: European
Language
Resources
Association
(ELRA),
May
2018.
[Online].
Available: https://aclanthology.org/L18-1036/
[37] Q. Li, Q. Mai, M. Wang, and M. Ma, “Chinese dialect speech recog-
nition: a comprehensive survey,” Artificial Intelligence Review, vol. 57,
no. 2, p. 25, 2024.
[38] Z. Yao, L. Guo, X. Yang, W. Kang, F. Kuang, Y. Yang, Z. Jin, L. Lin, and
D. Povey, “Zipformer: A faster and better encoder for automatic speech
recognition,” International Conference on Learning Representations,
2024.
[39] Y.-F. Liao, C.-Y. Chang, H.-K. Tiun, H.-L. Su, H.-L. Khoo, J. S. Tsay, L.-
K. Tan, P. Kang, T.-g. Thiann, U.-G. Iunn, J.-H. Yang, and C.-N. Liang,
“Formosa Speech Recognition Challenge 2020 and Taiwanese Across
Taiwan Corpus,” in 2020 23rd Conference of the Oriental COCOSDA
International Committee for the Co-ordination and Standardisation of
Speech Databases and Assessment Techniques (O-COCOSDA), 2020,
pp. 65–70.
[40] H.-B. Liang, C.-Y. Li, and H.-Y. Lee, “The NTU ASR System for
Formosa Speech Recognition Challenge 2020,” in Speech Signal Pro-
cessing Workshop, 2021. [Online]. Available: https://sites.google.com/
speech.ntut.edu.tw/fsw/home/challenge-2020/sspw-2021?authuser=0
[41] J. Lin, S. Lu, H. Huang, W. Guan, B. Xu, H. Bu, Q. Hong, and L. Li,
“MinSpeech: A Corpus of Southern Min Dialect for Automatic Speech
Recognition,” in Proc. Interspeech 2024, 2024, pp. 2330–2334.
[42] C. Xiao, H. L. Xinyuan, J. Yang, D. Gao, M. Wiesner, K. Duh, and
S. Khudanpur, “HK-LegiCoST: Leveraging Non-Verbatim Transcripts
for Speech Translation,” in Interspeech 2023, 2023, pp. 4074–4078.
[43] P.-J. Chen, K. Tran, Y. Yang, J. Du, J. Kao, Y.-A. Chung, P. Tomasello,
P.-A. Duquenne, H. Schwenk, H. Gong, H. Inaguma, S. Popuri, C. Wang,
J. Pino, W.-N. Hsu, and A. Lee, “Speech-to-speech translation for a
real-world unwritten language,” pp. 4969–4983, Jul. 2023. [Online].
Available: https://aclanthology.org/2023.findings-acl.307/
[44] Centre for the Protection of Language Resources of China, “The
chinese language resources protection project collection and display
platform,” 2023. [Online]. Available: https://zhongguoyuyan.cn
[45] L. Wu and W. Xiaohuan, “Luanping fangyan yuyin xitong diaocha
baogao [investigation report on the phonetic system of the luanping
dialect],” in Hebei Minzu Shifan Xueyuan Xuebao, 2015.
[46] A. Gulati, J. Qin, C.-C. Chiu, N. Parmar, Y. Zhang, J. Yu, W. Han,
S. Wang, Z. Zhang, Y. Wu, and R. Pang, “Conformer: Convolution-
augmented transformer for speech recognition,” in Interspeech 2020,
2020, pp. 5036–5040.
[47] F. Kuang, L. Guo, W. Kang, L. Lin, M. Luo, Z. Yao, and D. Povey,
“Pruned rnn-t for fast, memory-efficient asr training,” arXiv preprint
arXiv:2206.13236, 2022.
[48] A. Graves, “Sequence transduction with recurrent neural networks,”
International Conference of Machine Learning (ICML) 2012 Workshop
on Representation Learning, 2012.
[49] S. Watanabe, T. Hori, S. Kim, J. R. Hershey, and T. Hayashi, “Hy-
brid ctc/attention architecture for end-to-end speech recognition,” IEEE
Journal of Selected Topics in Signal Processing, vol. 11, no. 8, pp.
1240–1253, 2017.
[50] C. Szegedy, V. Vanhoucke, S. Ioffe, J. Shlens, and Z. Wojna, “Rethinking
the inception architecture for computer vision,” in Proceedings of the
IEEE conference on computer vision and pattern recognition, 2016, pp.
2818–2826.
[51] D. P. Kingma, “Adam: A method for stochastic optimization,” arXiv
preprint arXiv:1412.6980, 2014.
[52] B. Zhang, H. Lv, P. Guo, Q. Shao, C. Yang, L. Xie, X. Xu, H. Bu,
X. Chen, C. Zeng et al., “Wenetspeech: A 10000+ hours multi-domain
mandarin corpus for speech recognition,” in ICASSP 2022-2022 IEEE
International Conference on Acoustics, Speech and Signal Processing
(ICASSP).
IEEE, 2022, pp. 6182–6186.
[53] H. Bu, J. Du, X. Na, B. Wu, and H. Zheng, “AISHELL-1: An open-
source Mandarin speech corpus and a speech recognition baseline,”
in 2017 20th conference of the oriental chapter of the international
coordinating committee on speech databases and speech I/O systems
and assessment (O-COCOSDA).
IEEE, 2017, pp. 1–5.
[54] J. Du, X. Na, X. Liu, and H. Bu, “AISHELL-2: Transforming Mandarin
ASR research into industrial scale,” arXiv preprint arXiv:1808.10583,
2018.
[55] V. Panayotov, G. Chen, D. Povey, and S. Khudanpur, “Librispeech: an asr
corpus based on public domain audio books,” in 2015 IEEE international
conference on acoustics, speech and signal processing (ICASSP). IEEE,
2015, pp. 5206–5210.
[56] C. Li, S. Deng, Y. Wang, G. Wang, Y. Gong, C. Chen, and J. Bai, “Talcs:
An open-source mandarin-english code-switching corpus and a speech
recognition baseline,” in Interspeech 2022, 2022, pp. 1741–1745.
[57] R. Ardila, M. Branson, K. Davis, M. Kohler, J. Meyer, M. Henretty,
R. Morais, L. Saunders, F. Tyers, and G. Weber, “Common voice:
A massively-multilingual speech corpus,” in Proceedings of the
Twelfth Language Resources and Evaluation Conference, N. Calzolari,
F. B´echet, P. Blache, K. Choukri, C. Cieri, T. Declerck, S. Goggi,
H. Isahara, B. Maegaard, J. Mariani, H. Mazo, A. Moreno, J. Odijk,
and
S.
Piperidis,
Eds.
Marseille,
France:
European
Language
Resources Association, May 2020, pp. 4218–4222. [Online]. Available:
https://aclanthology.org/2020.lrec-1.520/
[58] M. Zanon Boito, W. Havard, M. Garnerin,
´E. Le Ferrand, and
L. Besacier, “MaSS: A large and clean multilingual corpus of sentence-
aligned spoken utterances extracted from the Bible,” in Proceedings
of the Twelfth Language Resources and Evaluation Conference,
N. Calzolari, F. B´echet, P. Blache, K. Choukri, C. Cieri, T. Declerck,
S. Goggi, H. Isahara, B. Maegaard, J. Mariani, H. Mazo, A. Moreno,
J. Odijk, and S. Piperidis, Eds.
Marseille, France: European Language
Resources Association, May 2020, pp. 6486–6493. [Online]. Available:
https://aclanthology.org/2020.lrec-1.799/
[59] P.-A. Duquenne, H. Schwenk, and B. Sagot, “Sonar: sentence-level
multimodal and language-agnostic representations,” arXiv preprint
arXiv:2308.11466, 2023.
[60] T. Zhang, V. Kishore, F. Wu, K. Q. Weinberger, and Y. Artzi, “Bertscore:
Evaluating text generation with bert,” in International Conference on
Learning Representations, 2020.
[61] “Icefall,” 2021. [Online]. Available: ttps://github.com/k2-fsa/icefall
[62] P. ˙Zelasko, D. Povey, J. Trmal, S. Khudanpur et al., “Lhotse: a speech
data representation library for the modern deep learning ecosystem,”
NeurIPS 2021 Data-Centric AI (DCAI) Workshop, 2021.
[63] D. S. Park, W. Chan, Y. Zhang, C.-C. Chiu, B. Zoph, E. D. Cubuk,
and Q. V. Le, “Specaugment: A simple data augmentation method for
automatic speech recognition,” in Interspeech 2019, 2019, pp. 2613–
2617.
[64] Z. Gao, S. Zhang, I. McLoughlin, and Z. Yan, “Paraformer: Fast and
accurate parallel transformer for non-autoregressive end-to-end speech
recognition,” in Interspeech 2022, 2022, pp. 2063–2067.
[65] R. You, Chinese Dialectology: A Historical and Social Overview.
Springer Nature, 2025.
[66] P. Peng, B. Yan, S. Watanabe, and D. Harwath, “Prompting the hidden
talent of web-scale speech models for zero-shot task generalization,” in
Interspeech 2023, 2023, pp. 396–400.
[67] T. Mikolov, W.-t. Yih, and G. Zweig, “Linguistic regularities in
continuous space word representations,” in Proceedings of the 2013
Conference
of
the
North
American
Chapter
of
the
Association
for
Computational
Linguistics:
Human
Language
Technologies,
L. Vanderwende, H. Daum´e III, and K. Kirchhoff, Eds.
Atlanta,
Georgia: Association for Computational Linguistics, Jun. 2013, pp.
746–751. [Online]. Available: https://aclanthology.org/N13-1090/
[68] T.
Pires,
E.
Schlinger,
and
D.
Garrette,
“How
multilingual
is
multilingual BERT?” in Proceedings of the 57th Annual Meeting
of the Association for Computational Linguistics, A. Korhonen,
D. Traum, and L. M`arquez, Eds.
Florence, Italy: Association
for Computational Linguistics, Jul. 2019, pp. 4996–5001. [Online].
Available: https://aclanthology.org/P19-1493/
[69] A. Conneau and G. Lample, “Cross-lingual language model pretraining,”
Advances in neural information processing systems, vol. 32, 2019.
[70] M. Huzaifah and I. Kukanov, “An analysis of semantically-aligned
speech-text embeddings,” in 2022 IEEE Spoken Language Technology
Workshop (SLT).
IEEE, 2023, pp. 747–754.
[71] S. Arora, K.-W. Chang, C.-M. Chien, Y. Peng, H. Wu, Y. Adi,
E. Dupoux, H.-Y. Lee, K. Livescu, and S. Watanabe, “On the landscape

--- Page 9 ---

of spoken language models: A comprehensive survey,” arXiv preprint
arXiv:2504.08528, 2025.
[72] Y. Peng, J. Tian, W. Chen, S. Arora, B. Yan, Y. Sudo, M. Shakeel,
K. Choi, J. Shi, X. Chang, J. weon Jung, and S. Watanabe, “OWSM
v3.1: Better and Faster Open Whisper-Style Speech Models based on
E-Branchformer,” in Interspeech 2024, 2024, pp. 352–356.
[73] S. Khurana, A. Laurent, and J. Glass, “Samu-xlsr: Semantically-aligned
multimodal utterance-level cross-lingual speech representation,” IEEE
Journal of Selected Topics in Signal Processing, vol. 16, no. 6, pp.
1493–1504, 2022.
[74] R. Rao, A. Ganesan, O. Kjell, J. Luby, A. Raghavan, S. Feltman,
W. Ringwald, R. L. Boyd, B. Luft, C. Ruggero et al., “Whispa: Seman-
tically and psychologically aligned whisper with self-supervised con-
trastive and student-teacher learning,” arXiv preprint arXiv:2501.16344,
2025.
[75] R. S. Srinivasa, J. Cho, C. Yang, Y. M. Saidutta, C.-H. Lee, Y. Shen,
and H. Jin, “Cwcl: Cross-modal transfer with continuously weighted
contrastive loss,” Advances in Neural Information Processing Systems,
vol. 36, 2023.
[76] M.
Bartelds
and
M.
Wieling,
“Quantifying
language
variation
acoustically
with
few
resources,”
in
Proceedings
of
the
2022
Conference of the North American Chapter of the Association for
Computational Linguistics: Human Language Technologies, M. Carpuat,
M.-C. de Marneffe, and I. V. Meza Ruiz, Eds.
Seattle, United States:
Association for Computational Linguistics, Jul. 2022, pp. 3735–3741.
[Online]. Available: https://aclanthology.org/2022.naacl-main.273/
[77] R. S.-E. Shim and J. Nerbonne, “dialectR: Doing dialectometry in R,”
in Proceedings of the Ninth Workshop on NLP for Similar Languages,
Varieties and Dialects, Y. Scherrer, T. Jauhiainen, N. Ljubeˇsi´c,
P. Nakov, J. Tiedemann, and M. Zampieri, Eds.
Gyeongju, Republic
of Korea: Association for Computational Linguistics, Oct. 2022, pp.
20–27. [Online]. Available: https://aclanthology.org/2022.vardial-1.3/
[78] H. Huang, J. Grieve, L. Jiao, and Z. Cai, “Geographic structure of
chinese dialects: a computational dialectometric approach,” Linguistics,
vol. 62, no. 4, pp. 937–976, 2024.

```
