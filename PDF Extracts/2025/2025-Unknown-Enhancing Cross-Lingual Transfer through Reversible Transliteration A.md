---
title: "2025-Unknown-Enhancing Cross-Lingual Transfer through Reversible Transliteration A - PDF Extract"
source_pdf: "2025-Unknown-Enhancing Cross-Lingual Transfer through Reversible Transliteration A.pdf"
pages: 17
extracted_at: "2026-02-13T13:57:14.703458"
---

# PDF Extract: 2025-Unknown-Enhancing Cross-Lingual Transfer through Reversible Transliteration A

**Source PDF:** 2025-Unknown-Enhancing Cross-Lingual Transfer through Reversible Transliteration A.pdf
**Total Pages:** 17

---

## Content

```
--- Page 1 ---

Enhancing Cross-Lingual Transfer through Reversible
Transliteration: A Huﬀman-Based Approach for Low-Resource
Languages
Wenhao Zhuang1,2, Yuan Sun1,2,3,*, Xiaobing Zhao1,2,3
1Minzu University of China, Beijing, China
2National Language Resource Monitoring & Research Center Minority Languages Branch
3Institute of National Security, Minzu University of China, Beijing, China
Emails: sdrz_zwh@163.com, sunyuan@muc.edu.cn, nmzxb_cn@163.com
* Corresponding author: Yuan Sun
Abstract
As large language models (LLMs) are
trained on increasingly diverse and ex-
tensive multilingual corpora, they demon-
strate cross-lingual transfer capabilities.
However, these capabilities often fail to
eﬀectively
extend
to
low-resource
lan-
guages, particularly those utilizing non-
Latin
scripts.
While
transliterating
low-resource languages into Latin script
presents a natural solution, there currently
lacks a comprehensive framework for in-
tegrating transliteration into LLMs train-
ing and deployment. Taking a pragmatic
approach,
this paper innovatively com-
bines character transliteration with Huﬀ-
man coding to design a complete transliter-
ation framework. Our proposed framework
oﬀers the following advantages: 1) Com-
pression: Reduces storage requirements for
low-resource language content, achieving
up to 50% reduction in ﬁle size and 50-
80% reduction in token count.
2) Ac-
curacy: Guarantees 100% lossless conver-
sion from transliterated text back to the
source language.
3) Eﬃciency:
Elimi-
nates the need for vocabulary expansion for
low-resource languages, improving train-
ing and inference eﬃciency.
4) Scalabil-
ity:
The framework can be extended to
other low-resource languages. We validate
the eﬀectiveness of our framework across
multiple downstream tasks, including text
classiﬁcation, machine reading comprehen-
sion, and machine translation. Experimen-
tal results demonstrate that our method
signiﬁcantly enhances the model’s capa-
bility to process low-resource languages
while maintaining performance on high-
resource languages. Our data and code are
publicly available at https://github.com/
CMLI-NLP/HuffmanTranslit.
1
Introduction
Large language models have demonstrated re-
markable multilingual transfer capabilities, en-
abling knowledge transfer from one language
to another without additional training (Qi
et al., 2023; Gao et al., 2024; Ye et al.,
2023). However, this transfer ability often per-
forms poorly in low-resource languages, pri-
marily constrained by three factors: scarcity
of training data (Costa-jussà et al., 2022), in-
suﬃcient cross-lingual word embedding align-
ment (Deshpande et al., 2021), and writing sys-
tem diﬀerences (Anastasopoulos and Neubig,
2019; Muller et al., 2021).
Common approaches to improving LLMs’
adaptability to low-resource languages include
continued pre-training and supervised ﬁne-
tuning (Tao et al., 2024). Due to the low rep-
resentation of low-resource languages in tok-
enizers and frequent occurrence of UNKnown
tokens (Moosa et al., 2023), vocabulary ex-
pansion becomes a primary task (Zhuang and
Sun, 2025).
However, ensuring high perfor-
mance for multiple low-resource languages is
extremely challenging, facing two key issues.
The ﬁrst issue is the increased training and in-
ference costs due to vocabulary size, as vocab-
ulary must inevitably expand with the addi-
tion of languages to ensure tokenization perfor-
mance for each language (Purkayastha et al.,
2023). The second issue is the curse of mul-
tilinguality, which means that using a ﬁxed-
capacity model to pre-train multiple languages
can improve cross-lingual performance to some
extent, but performance begins to decline be-
yond a certain point (Conneau, 2019).
To
improve
cross-lingual
transfer
while
avoiding issues associated with extensive vo-
cabulary expansion,
transliteration of low-
resource languages has emerged as a viable ap-
arXiv:2509.17493v1  [cs.CL]  22 Sep 2025

--- Page 2 ---

proach. Transliteration refers to the process
of converting text from one writing system to
another according to speciﬁc rules, typically
converting non-Latin scripts to Latin alpha-
bet representation
(Wellisch, 1978).
Previ-
ous studies have demonstrated that translit-
erating text into a common character set can
enhance cross-lingual transfer performance for
low-resource languages with non-Latin scripts
(Liu et al., 2024a, 2025). This improvement
is attributed to the common character set fa-
cilitating knowledge transfer through lexical
overlap
(Dhamecha et al., 2021; Pires, 2019;
Amrhein and Sennrich, 2020) and enabling the
reuse of existing information in embedding ma-
trices
(Purkayastha et al., 2023).
Append-
ing transliterated content to prompt templates
for low-resource languages has been shown to
improve downstream task performance
(Ma
et al., 2024).
Most research on transliteration relies on ex-
isting tools like UROMAN (Hermjakob et al.,
2018), which maps any UTF-8 character to
Latin letters, to investigate the impact of
transliteration on cross-lingual transfer or
alignment. However, this transliteration pro-
cess is irreversible; due to the potential loss
of characteristic information from the original
script during transliteration, it is impossible to
accurately restore the transliterated Latin let-
ters back to the source language script, which
limits its practical applications (Amrhein and
Sennrich, 2020).
Furthermore, low-resource
languages typically utilize extended Unicode
character sets for encoding, resulting in their
textual data occupying more storage space
compared to languages like English. This stor-
age overhead issue becomes more prominent
when processing large-scale multilingual cor-
pora. Therefore, this paper focuses on two key
issues: how to implement a reversible translit-
eration mechanism to facilitate practical appli-
cations while maintaining cross-lingual trans-
fer eﬀectiveness, and how to achieve text com-
pression during the transliteration process to
facilitate storage and training.
We observe
that these two points correspond precisely to
the reversibility and compression properties of
Huﬀman coding, which provides the theoreti-
cal foundation for our Huﬀman coding-based
transliteration scheme.
We selected three low-resource languages:
Tibetan, Mongolian, and Uyghur, which are
minority languages in China with a total
user base exceeding 30 million speakers, along
with English and Chinese as high-resource
languages for our experiments.
We con-
ducted continued pre-training of open-source
LLMs using corpora obtained through vari-
ous transliteration methods, analyzed cross-
lingual transfer performance across text clas-
siﬁcation, named entity recognition, machine
reading comprehension, knowledge extraction,
and machine translation tasks,
while also
comparing compression rates among diﬀer-
ent transliteration methods.
To enable the
model to directly serve low-resource language
users, we developed a FastText-based auto-
matic transliteration framework that performs
language detection before and after model
processing, implementing transliteration and
restoration of input and output, thereby main-
taining native language interaction at the user
end. In summary, our contributions are as fol-
lows:
• We
propose
a
Huﬀman
coding-based
transliteration scheme for low-resource
languages, achieving reversibility in the
transliteration process and addressing the
limitations of traditional transliteration
methods in practical applications.
• Leveraging the compression properties of
Huﬀman coding, we eﬀectively reduce the
storage overhead of low-resource language
texts, making the training of large-scale
multilingual corpora more eﬃcient.
• We develop an end-to-end framework in-
tegrating FastText language identiﬁca-
tion, enabling automatic transliteration
and restoration of low-resource languages
while maintaining native language inter-
action and improving performance across
multiple downstream tasks.
2
Related Works
Cross-lingual Transfer for Low-resource
Languages
To enhance low-resource lan-
guage performance in LLMs, one primary ap-
proach uses continued pre-training and su-
pervised ﬁne-tuning with low-resource cor-
pora (Wenhao et al., 2024).
However, this
method faces signiﬁcant challenges: it requires
complex vocabulary expansion and model ar-

--- Page 3 ---

chitecture modiﬁcations, resulting in poor scal-
ability, and most critically, suﬀers from limited
training data availability (Joshi et al., 2020).
Alternative approaches focus on improving
cross-lingual transfer capabilities through var-
ious mechanisms: concatenating multilingual
input sequences to leverage shared representa-
tion spaces (Kim et al.; Tanwar et al., 2023;
Cueva et al., 2024), projecting target lan-
guage representations onto high-resource lan-
guages for enhanced feature extraction (Xu
et al., 2023), and increasing the parallel con-
tent in multilingual training corpora (Zhuang
and Sun, 2025).
While these methods aim to transfer ca-
pabilities from resource-rich to low-resource
languages, a fundamental challenge remains:
the substantial diﬀerences in writing sys-
tems among low-resource languages.
Uni-
fying multiple languages into a single writ-
ing system could potentially address vocabu-
lary challenges and promote vocabulary shar-
ing, thereby facilitating cross-lingual knowl-
edge transfer (Purkayastha et al., 2023).
Tokenization
and
Vocabulary
Expan-
sion
Existing
subword
tokenizers
(such
as
BPE
(Sennrich,
2015)
and
Sentence-
Piece (Kudo, 2018)) have been widely adopted
for low-resource languages.
However, due
to the limited representation of these lan-
guages in pre-training corpora, they suﬀer
from insuﬃcient vocabulary coverage, over-
segmentation, and high ratios of unknown to-
kens. While vocabulary expansion (Cui et al.,
2023) oﬀers a potential solution, it introduces
new challenges: the need for substantial train-
ing data to adequately train new tokens, and
increased model capacity requirements to mit-
igate the multilingual curse (Conneau, 2019).
Recent approaches have focused on more ef-
ﬁcient solutions, such as leveraging shared lin-
guistic information and cross-lingual word em-
bedding alignment (Ogueji et al., 2021; Liu
et al., 2021), which improve tokenization with-
out signiﬁcant vocabulary expansion. Notably,
transliterating low-resource languages into a
uniﬁed writing system has shown promising re-
sults (Dhamecha et al., 2021; Liu et al., 2024b),
simultaneously enhancing vocabulary sharing
and model transfer capabilities while avoiding
the computational overhead of vocabulary ex-
pansion.
Romanization and Transliteration
Ro-
manization is the process of mapping various
characters to Latin characters, though this
process is typically irreversible. Its objective is
to approximate the pronunciation of the origi-
nal character text as closely as possible. Spe-
cialized tools like UROMAN (Hermjakob et al.,
2018) can romanize almost all characters by
directly mapping UTF-8 characters to Latin
letters, though this process involves informa-
tion loss, such as the omission of tonal infor-
mation. There are also general character con-
version tools like uconv that can preserve more
original character information, such as adding
diacritical marks, but this limits subword shar-
ing across languages.
The Tibetan, Mongolian, Uyghur, and Chi-
nese languages used in our experiments can
all be romanized through UROMAN; however,
due to the uniqueness of the Tibetan writ-
ing system, uconv currently cannot translit-
erate Tibetan.
Romanization encoding has
been studied in both natural language pro-
cessing and speech processing domains, such
as its application in multilingual pre-trained
language models to enhance low-resource lan-
guages (Purkayastha et al., 2023), and in
speech processing systems’ pre-training as
additional forced alignment for text label-
ing (Pratap et al., 2024).
Moreover, phono-
logical distinctions may be lost during roman-
ization - for instance, Chinese characters be-
come toneless pinyin when romanized, with
a single pinyin potentially corresponding to
many diﬀerent characters. UROMAN also con-
verts numbers from diﬀerent writing systems
into Western Arabic numerals (Ding et al.,
2024), which further complicates the process of
converting romanized text back to source lan-
guages, particularly when users expect LLMs
to output in their native writing systems. In
contrast, our proposed Huﬀman coding-based
transliteration method is an innovative ap-
proach that balances transliteration (improv-
ing cross-lingual transfer), compression (reduc-
ing storage and training costs), and reversibil-
ity (facilitating practical restoration and inter-
action).

--- Page 4 ---

3
Methodology
3.1
Overview
We propose a three-stage processing approach
for low-resource language transliteration and
applications:
(1) character encoding design:
analyzing character frequencies and designing
custom encodings.
(2) transliteration and
model training: training on transliterated raw
corpora.
(3) end-to-end language processing
pipeline: comprising input language classiﬁca-
tion and processing, model inference, and out-
put language classiﬁcation and processing, as
shown in Figure 1.
In this study, we focus on three low-resource
languages of China:
Tibetan, Uyghur, and
Mongolian (see Table 1). These languages rep-
resent diﬀerent writing systems, with a com-
bined user base exceeding 30 million speak-
ers. We select these languages because they
present signiﬁcant challenges for cross-lingual
transfer: they use non-Latin scripts, have lim-
ited digital resources, and exhibit distinct writ-
ing systems that diﬀer substantially from high-
resource languages like Chinese and English.
Name
ISO 639-1
Writing System
Tibetan
bo
Tibetan script
Uyghur
ug
Uyghur Arabic script
Mongolian
mn
Traditional Mongolian script
Table 1: Overview of the low-resource languages
studied in this work.
3.2
Character Frequency Analysis
Since English already uses Latin script and
Chinese
has
well-established
romanization
tools for converting characters to pinyin, we
focused our transliteration eﬀorts on three
low-resource languages: Uyghur, Tibetan, and
Mongolian.
Our character frequency analy-
sis began with the CUTE open-source paral-
lel dataset
(Zhuang and Sun, 2025), which
provided aligned text across Chinese, Uyghur,
Tibetan, and English.
To incorporate Mon-
golian, which wasn’t originally included in
CUTE, we followed the dataset’s methodol-
ogy to collect and evaluate Mongolian transla-
tions, using human evaluators to assess trans-
lation quality from Chinese to Mongolian. For
comprehensive character analysis, we sampled
3,000 instances from each of the three low-
resource languages and conducted a thorough
examination of their Unicode characters and
frequencies. Through a systematic approach
combining Unicode code point ranges, char-
acter naming conventions, and expert linguis-
tic validation, we identiﬁed the core charac-
ter sets for each language: 45 characters for
Mongolian, 38 for Uyghur, and 81 for Tibetan.
These character sets were then consolidated
and arranged in descending order of frequency,
providing a foundation for our transliteration
scheme.
3.3
Huﬀman-based Encoding Design
Properties of Huﬀman Coding
Huﬀman
coding, as a variable-length encoding method,
possesses both variable-length allocation and
preﬁx properties. The variable-length alloca-
tion ensures that high-frequency characters re-
ceive shorter codes while low-frequency charac-
ters receive longer codes, providing a theoreti-
cal foundation for our text compression. The
preﬁx property guarantees that no code is a
preﬁx of any other character’s code, facilitat-
ing unambiguous decoding.
Customized Encoding Scheme
Based on
the principles of Huﬀman coding, we designed
an improved encoding scheme. To accommo-
date more languages, our scheme, while not
strictly adhering to the preﬁx property, en-
sures unambiguous decoding through struc-
tured design.
Speciﬁcally, we constrain all
codes to follow the pattern "First letter cap-
italized, subsequent letters lowercase" and em-
ploy a maximum matching strategy for decod-
ing. Table 2 demonstrates the possibilities of
this design pattern at diﬀerent lengths.
Length
Pattern
Capacity
One
A, B, ..., Z
26
Two
Aa, Ab, ..., Zz
676
Three
Aaa, Aab, ..., Zzz
17,576
Four
Aaaa, Aaab, ..., Zzzz
456,976
Total (up to four characters)
475,254
Table 2: Encoding patterns and theoretical capac-
ity for diﬀerent lengths. The pattern consists of
one uppercase letter followed by zero or more low-
ercase letters.
This design oﬀers three key advantages: (1)

--- Page 5 ---

Step 1: Character Encoding Design
 bo: འཇིག་རྟེན་གྱི་སངས་རྒྱས་ཆོས་ལུགས་ཀྱི་སེམས་...
 mn: ᠳᠡᠯᠡᠬᠡᠶ ᠶᠢᠨ ᠪᠤᠳ᠋ᠳ᠋ᠾᠠ ᠶᠢᠨ ᠱᠠ...
 ug: دۇنيا بۇددا دىنى ھەققانىيەت...
"་" : 3158047
"ᠠ" : 1363662
......
"༧" : 137
Unicode
Character
Statistics
"་" : C  or  e
"ᠠ" : E  or  a
......
"༧" : Ev  or  М
Custom
Encoding
Assignment
Step 2: Transliteration and Model Training
 bo: ཀ་བཞི་ག་སིན་གཉིས་ཨན་གསུམ་ནི་རྫས་འགྱུར...
 mn: ᠳᠥᠷᠪᠡᠨ ᠮᠧᠲ᠋ᠢᠯᠲᠦ ᠬᠣᠶᠠᠷᠴᠢ ...
 ug: تېترامېتىل دىپروپىلېن ترى ئامىن ...
 en: March is a good time for ...
 zh: 物业是指已经建成并投入...
 bo: @BzCAfCfQCPCIQAjCP...
 mn: @AlBrAcAoGKBBfCzAu...
 ug: @AbBiAbXHAtBiAbDNB...
 en: March is a good time for ...
 zh: wu ye shi zhi yi jing jian...
Step 3: Language Processing Pipeline
Transliteration
Process
Model
Training Input
Input
Language
Classifier
User Input
Output
Language
Classifier
Model
Output
Need
Transliteration?
Figure 1: Overview of our three-stage approach.
Step 1: Character encoding design with Unicode
character statistics and custom encoding assignment. Step 2: Transliteration process for model training
input. Step 3: Language processing pipeline with language classiﬁcation for user interaction.
By constraining the ﬁrst character to be up-
percase and subsequent characters to be low-
ercase, combined with the maximum match-
ing strategy, it ensures unambiguous decoding.
(2) It maintains the core principle of Huﬀman
coding, allowing for variable-length code al-
location based on character frequencies.
(3)
It provides signiﬁcant scalability, theoretically
supporting encoding for up to 475,254 charac-
ters. In this study, we implemented a subset of
the two-character scheme, utilizing 21 single-
character codes (B-X) and 141 two-character
codes (Aa-Fk), totaling 162 encoding options.
This scale is suﬃcient to cover the character
sets of Uyghur, Tibetan, and Mongolian lan-
guages.
3.4
Transliteration Strategies
To explore optimal transliteration strategies,
we designed three progressive transliteration
schemes, with each scheme building upon and
improving its predecessor.
Basic Transliteration Strategy
We de-
signed a transliteration scheme using "First-
letter-capitalized + lowercase" encoding rules.
This scheme transliterates Uyghur, Tibetan,
and Mongolian into Latin alphabet represen-
tations according to encoding rules, while con-
verting Chinese characters into Pinyin and
preserving English text unchanged.
While
this strategy achieved basic transliteration
functionality and reversibility, it did not ac-
count for the tokenizer’s characteristics, leav-
ing room for further token compression.
Tokenizer-based Optimization Strategy
To address the token optimization potential in
the basic strategy, we analyzed the characteris-
tics of the Llama2 tokenizer. Research showed
that 66% of original characters required four
tokens for representation.
In response, we
innovatively utilized single tokens from the
Llama2 tokenizer (Touvron et al., 2023) as en-
coding mappings for original characters, en-
abling all 162 original characters to be rep-
resented by single tokens.
The comparative
token distribution is shown in Table 3.

--- Page 6 ---

Method
1-token 2-token 3-token 4-token
Original
1
45
9
107
Basic
90
72
0
0
Optimized
162
0
0
0
Table 3: Character distribution by token length
after Llama2 tokenization. The Optimized method
achieves single-token encoding for all characters.
Hybrid
Vocabulary
Strategy
Building
upon the second strategy, we leveraged the
linguistic patterns inherent in the transliter-
ated text to train a specialized vocabulary of
4,000 tokens.
This vocabulary was merged
with Llama2’s original 32,000-token vocabu-
lary to create a hybrid vocabulary of 33,738
tokens, maintaining eﬃcient single-character
encoding while capturing common character
combinations.
The comparison of the three
strategies is presented in Table 4. For a com-
prehensive analysis of ﬁle size and token com-
pression ratios across diﬀerent languages and
strategies, see Appendix B.
Strategy
Vocab Size
Compr.
Cost
Basic
32,000
1.63Œ
Low
Tokenizer
32,000
2.35Œ
Medium
Hybrid
33,738
3.04Œ
High
Table
4:
Comparison
of
diﬀerent
strategies.
Compr.
shows average token compression ratio
across Tibetan, Mongolian and Uyghur languages.
3.5
Reversibility Mechanism
Our transliteration system achieves perfect re-
versibility through a carefully designed map-
ping mechanism,
maintaining bidirectional
mappings between original characters and
Latin codes. For characters not in the map-
ping tables (e.g., emojis, rare characters, or
special symbols), the system preserves them
using ’@’ markers with proper escape se-
quences (e.g., ’@@’ for the ’@’ character itself),
ensuring no information loss during transliter-
ation. The detailed process is shown in Algo-
rithm 1.
The system employs a greedy matching
strategy during restoration, where it attempts
to match the longest possible Latin code
sequence for mapped characters while cor-
rectly handling preserved sequences between
Algorithm 1 Reversible Transliteration Sys-
tem
Input: Mc2l, Ml2c: Bidirectional mappings,
text: Input text
Output: Transliterated or restored text
Function ToLatin(text):
result ←[]
for each c in text do
Append Mc2l[c] if exists, else preserve
as @...@
end for
return joined result
Function FromLatin(latin_text):
result ←[], i ←0
while i < length(latin_text) do
Process @ markers or ﬁnd longest
matching code
Advance i accordingly
end while
return joined result
’@’ markers.
This dual mechanism ensures
100% restoration accuracy by either mapping
characters through the bidirectional tables or
preserving them in their original form.
3.6
Auxiliary Models for Practical
Deployment
To achieve end-to-end system deployment, we
developed three auxiliary models. At the in-
put stage, we trained a FastText-based classi-
ﬁer speciﬁcally for identifying Mongolian, Ti-
betan, Uyghur, Chinese, and other languages.
At the output stage, we trained a FastText
language classiﬁer tailored to the characteris-
tics of transliterated text to guide language
restoration. Additionally, to accurately handle
the conversion from Chinese pinyin to charac-
ters, we ﬁne-tuned a specialized model based
on Qwen2.5-0.5B (Yang et al., 2024). The de-
tailed training processes and evaluation results
of these models are presented in Appendix A.
4
Experiments and Analysis
To
evaluate
the
eﬀectiveness
of
diﬀerent
transliteration schemes, we conducted a se-
ries
of
experiments
examining
the
cross-
lingual transfer performance of models trained
with various transliteration strategies.
We

--- Page 7 ---

Model
Low-resource Languages (Acc / F1)
Chinese
Average
bo
mn
ug
Acc
F1
Minorities
All
Base Llama2
28.65 / 21.23
1.78 / 1.65
73.33 / 74.69
86.12
85.91
13.48 / 9.01
48.15 / 48.78
Expanded Vocab
53.96 / 51.69
64.45 / 67.95
76.00 / 82.91
89.95
89.91
62.58 / 64.56
75.64 / 76.34
UROMAN
49.37 / 48.88
64.92 / 67.78
81.33 / 86.18
89.82
89.75
62.10 / 63.47
75.33 / 75.84
Basic Trans.
52.16 / 52.18
66.46 / 69.55
74.67 / 81.51
89.92
89.81
63.40 / 65.17
76.06 / 76.60
Token-Opt Trans.
54.14 / 54.94
61.25 / 64.61
81.00 / 85.31
90.15
90.07
60.80 / 63.54
74.81 / 75.86
Hybrid Trans.
50.45 / 52.58
61.25 / 65.15
65.33 / 75.59
90.00
89.95
58.80 / 62.15
73.68 / 75.02
Table 5: Performance comparison on the WCM-v2 dataset. The best scores are in bold, with the second
best underlined. Base Llama2: directly ﬁne-tuned on original texts; Expanded Vocab: vocabulary expan-
sion for each low-resource language; Basic/Token-Opt/Hybrid Trans.: three progressive transliteration
strategies. Minorities average is calculated as the mean of scores for low-resource languages.
Model
CMRC-Trained
SQuAD-Trained
Chinese
Tibetan
English
Tibetan
EM
F1
EM
F1
EM
F1
EM
F1
Base Llama2
77.2
89.5
7.9
45.8
89.5
95.3
6.5
50.8
Expanded Vocab
81.3
91.1
11.5
50.6
89.9
95.7
10.3
58.9
UROMAN
79.6
88.3
12.0
53.4
84.2
88.7
11.0
61.1
Basic Trans.
87.7
92.7
15.5
59.5
87.7
89.1
12.7
65.1
Token-Opt Trans.
88.4
93.6
16.0
60.2
88.0
89.3
13.5
66.5
Hybrid Trans.
83.1
90.2
14.8
58.8
87.2
89.0
12.3
64.9
Table 6: Machine Reading Comprehension performance comparison. The best scores are in bold, with
the second best underlined. Results show both source language (Chinese/English) and target language
(Tibetan) performance under diﬀerent training settings. EM: Exact Match score; F1: F1 score.
speciﬁcally focused on whether the models
could eﬀectively transfer knowledge to low-
resource languages (Tibetan, Mongolian, and
Uyghur) while maintaining performance in
high-resource languages (Chinese and En-
glish).
4.1
Experimental Setup
We adopt the following experimental proce-
dure: First, we process the pre-training cor-
pus using diﬀerent transliteration methods, fol-
lowed by continued pre-training of the model.
The choice of continued pre-training over train-
ing from scratch is motivated by the common
challenge of insuﬃcient training data faced by
low-resource languages, which makes it diﬃ-
cult to support a complete pre-training pro-
cess.
After pre-training, we perform super-
vised ﬁne-tuning using downstream task data
from high-resource languages, and then di-
rectly conduct zero-shot evaluation on low-
resource languages to verify the model’s cross-
lingual transfer capability.
For Tibetan, Uyghur, and Mongolian lan-
guages, we identiﬁed a limited number of avail-
able datasets. Our experiments encompassed
three primary tasks: text classiﬁcation, ma-
chine reading comprehension, and translation.
These tasks evaluated the model’s capabili-
ties across diﬀerent levels of language process-
ing, thereby enabling a comprehensive assess-
ment of the transliteration scheme’s eﬀective-
ness. Details regarding the pre-training data
and parameter settings can be found in Ap-
pendix C.
We designed the following comparative ex-
periments:
• Direct Continued Pre-training: Continu-
ing pre-training on the original model us-
ing raw corpora.
• Vocabulary Expansion: Augmenting the
original model’s vocabulary with dedi-
cated lexicons for each low-resource lan-
guage.
• UROMAN Transliteration: Applying uni-
versal romanization tools for translitera-
tion.
• Three Progressive Transliteration Strate-
gies: As detailed in Section 3.4.

--- Page 8 ---

4.2
Text Classiﬁcation
We ﬁrst evaluated the eﬀectiveness of various
transliteration schemes on the text classiﬁca-
tion task. The experiments utilized the WCM-
v2 dataset (see Appendix D.1), a classiﬁca-
tion dataset encompassing multiple ethnic mi-
nority languages of China (Yang et al., 2022).
This dataset maintains balanced distributions
across both categories and languages, contain-
ing texts from 10 domains including arts, geog-
raphy, and history. The experimental results
are shown in Table 5. To comprehensively eval-
uate the eﬀectiveness of each approach, we fo-
cus not only on the overall performance but
also speciﬁcally on the average performance
across low-resource languages.
4.3
Machine Reading Comprehension
For the machine reading comprehension task,
we
evaluate
the
models’
performance
by
ﬁne-tuning
them
on
the
Chinese
CMRC
dataset (Cui et al., 2019) and English SQuAD
dataset (Rajpurkar, 2016), followed by zero-
shot testing on the TibetanQA dataset (Sun
et al., 2021) to assess their cross-lingual trans-
fer capabilities.
We also report the perfor-
mance on the source languages to verify that
our approaches maintain strong performance
on high-resource languages while enabling ef-
fective cross-lingual transfer. The results are
shown in Table 6.
For detailed informa-
tion about the datasets, please refer to Ap-
pendix D.2.
4.4
Machine Translation
To evaluate the models’ machine translation
capabilities for low-resource languages, we con-
duct experiments on Chinese-to-Tibetan (zh-
bo) and Chinese-to-Uyghur (zh-ug) transla-
tion tasks using the Flores-200 dataset (Costa-
jussà et al., 2022).
We employ few-shot
prompting with three carefully selected exam-
ples for each language pair, ensuring the ex-
amples cover diverse linguistic patterns. The
evaluation uses three standard metrics: BLEU
score for overall translation quality, chrF for
character-level accuracy, and Translation Edit
Rate (TER) for measuring the amount of edit-
ing required to match the reference translation.
Table 7 presents the results of our comparative
evaluation. For detailed information about the
dataset and prompts used, please refer to Ap-
pendix E.
4.5
Overall Analysis
Cross-task
Performance
Analysis
Through a comparative analysis of exper-
imental
results
across
text
classiﬁcation,
machine reading comprehension, and machine
translation tasks, our proposed transliteration
approach demonstrated excellent cross-lingual
transfer capabilities.
In text classiﬁcation
tasks,
the
basic
transliteration
strategy
achieved an average accuracy of 63.40% on
low-resource languages, showing an improve-
ment of 0.82% compared to the vocabulary
expansion approach.
For machine reading
comprehension tasks, the tokenizer-optimized
transliteration strategy achieved an exact
match score of 16.0% on Chinese-to-Tibetan
transfer, outperforming the vocabulary ex-
pansion approach by 4.5%. This strategy also
exhibited superior performance in translation
tasks,
achieving a BLEU score of 6.3 in
Chinese-to-Tibetan
translation.
Notably,
these improvements were achieved while main-
taining high performance on resource-rich
languages, as exempliﬁed by our approach
achieving 90.15% accuracy on Chinese text
classiﬁcation tasks.
Key
Findings
Our experimental results
yield three signiﬁcant ﬁndings:
• Performance
and
Eﬃciency:
Our
transliteration
approaches
consistently
outperformed traditional vocabulary ex-
pansion methods across tasks, with both
basic and tokenizer-optimized strategies
showing exceptional results.
By lever-
aging existing tokenizer characteristics,
these approaches signiﬁcantly improved
low-resource language processing without
vocabulary expansion.
• Untapped Potential:
Despite using
simple frequency-based encoding schemes
(B-X, Aa-Fk) and random token assign-
ments,
our methods demonstrated re-
markable eﬀectiveness. This suggests sub-
stantial room for improvement through
the incorporation of linguistic features
and more sophisticated encoding strate-
gies.

--- Page 9 ---

Model
Chinese-to-Tibetan (zh-bo)
Chinese-to-Uyghur (zh-ug)
BLEU↑
chrF↑
TER↓
BLEU↑
chrF↑
TER↓
Base Llama2
3.5
0.28
0.92
4.2
0.31
0.89
Expanded Vocab
5.0
0.35
0.86
5.7
0.38
0.83
UROMAN
4.5
0.33
0.88
5.2
0.36
0.85
Basic Trans.
5.7
0.37
0.84
6.4
0.40
0.81
Token-Opt Trans.
6.3
0.39
0.82
7.0
0.42
0.79
Hybrid Trans.
3.8
0.30
0.90
4.5
0.33
0.87
Table 7: Machine Translation performance comparison on Flores-200 dataset using few-shot prompting
(3 examples). ↑: higher is better, ↓: lower is better. The best scores are in bold, with the second best
underlined. TER: Translation Edit Rate.
• Scalable Framework: Our ﬁndings es-
tablish a new paradigm for low-resource
language
processing,
oﬀering
a
more
promising direction than vocabulary ex-
pansion.
The
success
of
this
rela-
tively simple implementation particularly
demonstrates its potential for scaling to
multiple low-resource languages.
These results not only validate our approach
but also indicate that more sophisticated ver-
sions of these strategies could yield even more
signiﬁcant improvements in low-resource lan-
guage processing.
5
Conclusion
In this paper, we introduce a novel Huﬀman-
based
transliteration
framework
that
ad-
dresses three critical challenges in low-resource
language processing:
cross-lingual transfer,
storage eﬃciency, and practical deployment.
Our framework demonstrates superior perfor-
mance across diverse tasks while maintain-
ing a lightweight implementation.
The ba-
sic and tokenizer-optimized strategies con-
sistently outperform traditional approaches,
achieving up to 4.5% improvement in cross-
lingual machine reading comprehension and
signiﬁcant gains in translation tasks, all while
preserving performance on high-resource lan-
guages.
Beyond performance gains, our ap-
proach oﬀers unique advantages in compres-
sion eﬃciency, reducing both ﬁle size and to-
ken count by 2-3 times without sacriﬁcing re-
versibility. Most importantly, our framework’s
success with simple frequency-based encoding
suggests substantial potential for improvement
through the incorporation of linguistic features
and more sophisticated encoding strategies.
These ﬁndings establish a promising direction
for scaling language technologies to the world’s
many low-resource languages, oﬀering a more
practical alternative to the traditional vocab-
ulary expansion paradigm.
Limitations
While our approach demonstrates promising
results, there are several important limitations
to consider. Our current evaluation scope is re-
stricted to three low-resource languages with
non-Latin scripts. Although the framework is
theoretically extensible to other writing sys-
tems, speciﬁc adaptations may be necessary
to accommodate their unique characteristics.
The limited availability of evaluation datasets
for low-resource languages also poses a chal-
lenge, particularly in tasks like machine read-
ing comprehension, where we could only assess
performance on a subset of languages.
From a practical perspective, our approach
faces a trade-oﬀbetween storage eﬃciency and
computational overhead.
While we achieve
signiﬁcant reductions in storage requirements,
the transliteration and restoration processes
introduce additional computational steps that
could impact real-time performance,
espe-
cially in scenarios requiring frequent language
switching.
Furthermore, our current encod-
ing scheme relies primarily on character fre-
quency, leaving room for potential improve-
ments through the incorporation of linguistic
features such as phonemes and morphological
information.

--- Page 10 ---

Acknowledgments
This work is supported by the National Social
Science
Foundation
(22&ZD035),
the
Na-
tional Nature Science Foundation (61972436),
and the Minzu University of China Foun-
dation
(GRSCP202316,
2023QNYL22,
2024GJYY43).
References
Chantal Amrhein and Rico Sennrich. 2020.
On
romanization for model transfer between scripts
in neural machine translation. In Findings of
the Association for Computational Linguistics:
EMNLP 2020, pages 2461–2469.
Antonios Anastasopoulos and Graham Neubig.
2019.
Pushing the limits of low-resource mor-
phological inﬂection. In Proceedings of the 2019
Conference on Empirical Methods in Natural
Language Processing and the 9th International
Joint Conference on Natural Language Process-
ing (EMNLP-IJCNLP), pages 984–996.
A Conneau. 2019. Unsupervised cross-lingual rep-
resentation learning at scale.
arXiv preprint
arXiv:1911.02116.
Marta R Costa-jussà, James Cross, Onur Çelebi,
Maha Elbayad, Kenneth Heaﬁeld, Kevin Heﬀer-
nan, Elahe Kalbassi, Janice Lam, Daniel Licht,
Jean Maillard, et al. 2022. No language left be-
hind: Scaling human-centered machine transla-
tion. arXiv preprint arXiv:2207.04672.
Emilio
Cueva,
Adrian
López-Monroy,
Fer-
nando Sánchez Vega,
and Thamar Solorio.
2024. Adaptive cross-lingual text classiﬁcation
through
in-context
one-shot
demonstrations.
In Proceedings of the 2024 Conference of the
North American Chapter of the Association for
Computational Linguistics:
Human Language
Technologies (Volume 1: Long Papers), pages
8317–8335.
Yiming Cui, Ting Liu, Wanxiang Che, Li Xiao,
Zhipeng Chen, Wentao Ma, Shijin Wang, and
Guoping Hu. 2019. A span-extraction dataset
for chinese machine reading comprehension. In
Proceedings of the 2019 Conference on Empirical
Methods in Natural Language Processing and the
9th International Joint Conference on Natural
Language Processing (EMNLP-IJCNLP), pages
5883–5889.
Yiming Cui, Ziqing Yang, and Xin Yao. 2023.
Eﬃcient and eﬀective text encoding for chi-
nese
llama
and
alpaca.
arXiv
preprint
arXiv:2304.08177.
Ameet Deshpande, Partha Talukdar, and Karthik
Narasimhan. 2021. When is bert multilingual?
isolating crucial ingredients for cross-lingual
transfer. arXiv preprint arXiv:2110.14782.
Tejas Dhamecha, Rudra Murthy, Samarth Bharad-
waj, Karthik Sankaranarayanan, and Pushpak
Bhattacharyya. 2021. Role of language related-
ness in multilingual ﬁne-tuning of language mod-
els: A case study in indo-aryan languages. In
Proceedings of the 2021 Conference on Empirical
Methods in Natural Language Processing, pages
8584–8595.
Wen Ding, Fei Jia, Hainan Xu, Yu Xi, Junjie
Lai, and Boris Ginsburg. 2024. Romanization
encoding for multilingual asr.
arXiv preprint
arXiv:2407.04368.
Changjiang Gao, Hongda Hu, Peng Hu, Jiajun
Chen, Jixing Li, and Shujian Huang. 2024. Mul-
tilingual pretraining and instruction tuning im-
prove cross-lingual knowledge alignment, but
only shallowly. In Proceedings of the 2024 Con-
ference of the North American Chapter of the
Association for Computational Linguistics: Hu-
man Language Technologies (Volume 1: Long
Papers), pages 6101–6117.
Ulf Hermjakob, Jonathan May, and Kevin Knight.
2018.
Out-of-the-box universal romanization
tool uroman. In Proceedings of ACL 2018, sys-
tem demonstrations, pages 13–18.
Pratik Joshi, Sebastin Santy, Amar Budhiraja, Ka-
lika Bali, and Monojit Choudhury. 2020. The
state and fate of linguistic diversity and inclu-
sion in the nlp world. In Proceedings of the 58th
Annual Meeting of the Association for Computa-
tional Linguistics, pages 6282–6293.
Sunkyoung Kim, Dayeon Ki, Yireun Kim, and Jin-
sik Lee. Translating qa is enough: A key to un-
locking in-context cross-lingual performance. In
ICML 2024 Workshop on In-Context Learning.
T Kudo. 2018. Sentencepiece: A simple and lan-
guage independent subword tokenizer and detok-
enizer for neural text processing. arXiv preprint
arXiv:1808.06226.
Linlin Liu, Bosheng Ding, Lidong Bing, Shaﬁq
Joty, Luo Si, and Chunyan Miao. 2021. Mulda:
A multilingual data augmentation framework
for low-resource cross-lingual ner.
In Proceed-
ings of the 59th Annual Meeting of the Asso-
ciation for Computational Linguistics and the
11th International Joint Conference on Natural
Language Processing (Volume 1: Long Papers),
pages 5834–5846.
Yihong Liu, Chunlan Ma, Haotian Ye, and Hinrich
Schütze. 2024a. Translico: A contrastive learn-
ing framework to address the script barrier in
multilingual pretrained language models. arXiv
preprint arXiv:2401.06620.

--- Page 11 ---

Yihong Liu, Chunlan Ma, Haotian Ye, and Hinrich
Schütze. 2024b. Transmi: A framework to cre-
ate strong baselines from multilingual pretrained
language models for transliterated data. arXiv
preprint arXiv:2405.09913.
Yihong Liu, Mingyang Wang, Amir Hossein Kar-
garan, Ayyoob ImaniGooghari, Orgest Xhelili,
Haotian Ye, Chunlan Ma, François Yvon, and
Hinrich Schütze. 2025. How transliterations im-
prove crosslingual alignment. In Proceedings of
the 31st International Conference on Computa-
tional Linguistics, pages 2417–2433.
Chunlan Ma, Yihong Liu, Haotian Ye, and Hinrich
Schütze. 2024.
Exploring the role of translit-
eration in in-context learning for low-resource
languages written in non-latin scripts.
arXiv
preprint arXiv:2407.02320.
Ibraheem Muhammad Moosa,
Mahmud Elahi
Akhter, and Ashﬁa Binte Habib. 2023.
Does
transliteration help multilingual language mod-
eling? In Findings of the Association for Com-
putational Linguistics: EACL 2023, pages 670–
685.
Benjamin
Muller,
Antonios
Anastasopoulos,
Benoît Sagot, and Djamé Seddah. 2021. When
being unseen from mbert is just the beginning:
Handling
new
languages
with
multilingual
language models.
In Proceedings of the 2021
Conference of the North American Chapter of
the Association for Computational Linguistics:
Human Language Technologies, pages 448–462.
Kelechi Ogueji, Yuxin Zhu, and Jimmy Lin. 2021.
Small data? no problem! exploring the viabil-
ity of pretrained multilingual language models
for low-resourced languages. In Proceedings of
the 1st Workshop on Multilingual Representation
Learning, pages 116–126.
T Pires. 2019.
How multilingual is multilingual
bert. arXiv preprint arXiv:1906.01502.
Vineel Pratap, Andros Tjandra, Bowen Shi, Paden
Tomasello,
Arun Babu,
Sayani Kundu,
Ali
Elkahky, Zhaoheng Ni, Apoorv Vyas, Maryam
Fazel-Zarandi, et al. 2024. Scaling speech tech-
nology to 1,000+ languages. Journal of Machine
Learning Research, 25(97):1–52.
Sukannya Purkayastha, Sebastian Ruder, Jonas
Pfeiﬀer, Iryna Gurevych, and Ivan Vulić. 2023.
Romanization-based large-scale adaptation of
multilingual language models.
In Findings of
the Association for Computational Linguistics:
EMNLP 2023, pages 7996–8005.
Jirui Qi, Raquel Fernández, and Arianna Bisazza.
2023. Cross-lingual consistency of factual knowl-
edge in multilingual language models. In Pro-
ceedings of the 2023 Conference on Empirical
Methods in Natural Language Processing, pages
10650–10666.
P Rajpurkar. 2016. Squad: 100,000+ questions for
machine comprehension of text. arXiv preprint
arXiv:1606.05250.
Rico Sennrich. 2015. Neural machine translation of
rare words with subword units. arXiv preprint
arXiv:1508.07909.
Y Sun, S Liu, C Chen, Z Dan, and X Zhao. 2021.
Construction of high-quality tibetan dataset for
machine reading comprehension.
In Proceed-
ings of the 20th Chinese National Conference on
Computational Linguistics, pages 208–218.
Eshaan
Tanwar,
Subhabrata
Dutta,
Manish
Borthakur,
and Tanmoy Chakraborty. 2023.
Multilingual llms are better cross-lingual in-
context learners with alignment. In Proceedings
of the 61st Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long
Papers), pages 6292–6307.
Mingxu Tao, Chen Zhang, Quzhe Huang, Tianyao
Ma, Songfang Huang, Dongyan Zhao, and Yan-
song Feng. 2024.
Unlocking the potential of
model merging for low-resource languages.
In
Findings of the Association for Computational
Linguistics: EMNLP 2024, pages 8705–8720.
Hugo Touvron, Louis Martin, Kevin Stone, Pe-
ter Albert, Amjad Almahairi, Yasmine Babaei,
Nikolay Bashlykov, Soumya Batra, Prajjwal
Bhargava, Shruti Bhosale, et al. 2023.
Llama
2: Open foundation and ﬁne-tuned chat models.
arXiv preprint arXiv:2307.09288.
Hans H Wellisch. 1978. The conversion of scripts-
its nature, history, and utilization.
Zhuang Wenhao, Sun Yuan, and Zhao Xiaobing.
2024.
Tilamb:
(tilamb: A tibetan large lan-
guage model based on incremental pre-training).
In Proceedings of the 23rd Chinese National
Conference on Computational Linguistics (Vol-
ume 1: Main Conference), pages 254–267.
Shaoyang Xu, Junzhuo Li, and Deyi Xiong. 2023.
Language representation projection:
Can we
transfer factual knowledge across languages in
multilingual language models?
In Proceedings
of the 2023 Conference on Empirical Methods in
Natural Language Processing, pages 3692–3702.
An Yang, Baosong Yang, Beichen Zhang, Binyuan
Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayi-
heng Liu, Fei Huang, Haoran Wei, et al. 2024.
Qwen2. 5 technical report.
arXiv preprint
arXiv:2412.15115.
Ziqing Yang, Zihang Xu, Yiming Cui, Baoxin
Wang, Min Lin, Dayong Wu, and Zhigang Chen.
2022. Cino: A chinese minority pre-trained lan-
guage model. In Proceedings of the 29th Interna-
tional Conference on Computational Linguistics,
pages 3937–3949.

--- Page 12 ---

Jiacheng Ye, Xijia Tao, and Lingpeng Kong. 2023.
Language versatilists vs. specialists: An empir-
ical revisiting on multilingual transfer ability.
arXiv preprint arXiv:2306.06688.
Wenhao Zhuang and Yuan Sun. 2025.
Cute: A
multilingual dataset for enhancing cross-lingual
knowledge transfer in low-resource languages.
In Proceedings of the 31st International Confer-
ence on Computational Linguistics, pages 10037–
10046.

--- Page 13 ---

A
Auxiliary Models
To achieve a comprehensive end-to-end system,
we developed three auxiliary models for in-
put language identiﬁcation, output language
identiﬁcation, and Chinese pinyin conversion.
These models collectively form a complete lan-
guage processing pipeline, ensuring that the
system can accurately process multilingual in-
puts and generate appropriate outputs.
A.1
Input Language Classiﬁer
We trained specialized language identiﬁca-
tion models based on the FastText frame-
work to accurately identify the language type
of input text.
The classiﬁer supports ﬁve
language categories:
Tibetan (bo), Mongo-
lian (mn), Uyghur (ug), Chinese (zh), and
other languages (other).
The training data
was sourced from multiple datasets, includ-
ing CUTE (Zhuang and Sun, 2025), WCM-
v2 (Yang et al., 2022), and other open-source
datasets, to ensure the model can process text
from various domains. The training parame-
ters for the input language classiﬁer are shown
in Table 8.
The evaluation results on the test set of
5,000 entries show that the classiﬁer achieved a
high level of classiﬁcation across all languages
and can be used for actual classiﬁcation needs.
The evaluation results are shown in Table 9.
Language
Precision
Recall
F1
Tibetan
0.992
0.989
0.991
Mongolian
0.987
0.985
0.986
Uyghur
0.995
0.993
0.994
Chinese
0.998
0.997
0.998
Other
0.981
0.978
0.980
Table 9: Performance of the input language classi-
ﬁer on various languages.
A.2
Transliterated Text Classiﬁer
To accurately identify transliterated text in
model outputs and guide proper language
restoration, we trained a specialized FastText
classiﬁer.
The distinguishing feature of this
classiﬁer lies in its need to process transliter-
ated text; therefore, we utilized parallel cor-
pora of transliterated text for training, ensur-
ing the model could recognize textual features
under diﬀerent transliteration strategies. The
training parameters for the output language
classiﬁer are shown in Table 8.
The
classiﬁcation
performance
on
the
transliterated text test set is shown in Ta-
ble 10.
Language
Precision
Recall
F1
Tibetan
0.988
0.985
0.987
Mongolian
0.983
0.981
0.982
Uyghur
0.991
0.989
0.990
Chinese
0.995
0.994
0.995
Other
0.992
0.990
0.991
Table 10: Performance of the transliteration text
classiﬁer in various languages.
A.3
Pinyin-to-Chinese Converter
For Chinese pinyin conversion, we performed
task-speciﬁc ﬁne-tuning based on the Qwen2.5-
0.5B model (Yang et al., 2024). This model
handles the conversion from pinyin sequences
to Chinese characters,
which is a typical
sequence-to-sequence conversion task.
We
used approximately 1 million pinyin-character
pairs for training, with data sourced from news
texts, Wikipedia, and general domain texts.
The parameters used for ﬁne-tuning are shown
in Table 11.
Parameter
Value
Batch Size
128
Learning Rate
2e-5
Max Length
2048
Epochs
3
Warmup Steps
1000
Weight Decay
0.01
Table 11: Qwen2.5-0.5B ﬁne-tuning parameter set-
tings.
The performance evaluation of the model on
the test set is shown in Table 12.
These three auxiliary models collectively
form a complete language processing pipeline,
capable of accurately identifying input lan-
guages, processing transliterated text, and
converting pinyin to Chinese characters when
needed. In practical applications, these mod-
els have demonstrated stable performance and
high accuracy.

--- Page 14 ---

Parameter
Input Classiﬁer
Output Classiﬁer
Note
Learning Rate
0.1
0.05
Initial learning rate
Epochs
25
30
Training epochs
Word n-grams
2
3
Maximum length of word n-gram
Vector Dimension
100
150
Embedding dimension
Context Window
5
7
Size of context window
Min Word Count
5
3
Minimum word frequency
Table 8: Training parameters for FastText language classiﬁers. The input classiﬁer is optimized for raw
text classiﬁcation, while the output classiﬁer is speciﬁcally tuned for transliterated text patterns with
slightly diﬀerent hyperparameters.
Metric
Value
Note
Character Accuracy
0.975
Single character accuracy
Sentence Accuracy
0.892
Complete sentence accuracy
BLEU Score
96.8
Overall translation quality
Inference Speed
125ms/sent
Average processing time
Table 12: Evaluation of Pinyin Conversion Model Performance. The model shows strong performance in
character-level accuracy and complete sentence conversion, with reasonable inference speed suitable for
real-time applications.
B
Compression Analysis
To comprehensively evaluate diﬀerent translit-
eration approaches, we compare our three
strategies with two baselines: vocabulary ex-
pansion (adding 6,000 tokens for each low-
resource language) and UROMAN (a widely-
used romanization tool).
Table 13 presents
the compression performance across diﬀerent
approaches and languages.
Method
Lang
File
Token
Compr.
Compr.
Vocab Expansion
bo
1.00Œ
6.92Œ
mn
1.00Œ
9.66Œ
ug
1.00Œ
4.49Œ
zh
1.00Œ
1.75Œ
UROMAN
bo
2.07Œ
1.88Œ
mn
2.41Œ
5.16Œ
ug
1.78Œ
2.46Œ
zh
1.00Œ
1.12Œ
Basic
bo
1.98Œ
1.33Œ
mn
1.95Œ
2.57Œ
ug
1.25Œ
1.00Œ
zh
0.73Œ
0.90Œ
Tokenizer
bo
2.61Œ
1.80Œ
mn
2.07Œ
3.85Œ
ug
1.27Œ
1.39Œ
zh
0.73Œ
0.90Œ
Hybrid
bo
2.61Œ
2.23Œ
mn
2.07Œ
4.98Œ
ug
1.27Œ
1.92Œ
zh
0.73Œ
1.41Œ
Table 13: Compression performance across diﬀer-
ent approaches and languages. File Compr. shows
the ratio of original ﬁle size to transliterated ﬁle
size.
Token Compr.
indicates the ratio of origi-
nal token count to transliterated token count using
Llama2 tokenizer. Language codes: bo (Tibetan),
mn (Mongolian), ug (Uyghur), zh (Chinese).
The
vocabulary
expansion
approach
achieves the highest token compression ratios

--- Page 15 ---

but maintains original ﬁle sizes.
UROMAN
demonstrates good compression performance
in both ﬁle size and token count.
Our
proposed methods show progressive improve-
ments from Basic to Hybrid strategies, with
the Hybrid approach achieving competitive
token compression while maintaining strong
ﬁle size reduction.
Note that Chinese (zh)
shows diﬀerent patterns due to its unique
characteristics in tokenization and encoding.
C
Training Details
C.1
Pre-training Data
The statistics of the raw corpora used for pre-
training are shown in Table 14.
The data
is primarily sourced from the CUTE parallel
corpus (Zhuang and Sun, 2025), which pro-
vides high-quality aligned multilingual content
across Chinese, Uyghur, Tibetan, and English
languages.
For Mongolian, we followed the
data collection and quality assessment method-
ology described in the CUTE paper to ensure
comparable data quality and distribution.
Language
Lines
Size (GB)
Tibetan (bo)
934,140
11.22
Mongolian (mn)
933,941
11.48
Uyghur (ug)
934,002
7.37
Chinese (zh)
933,946
2.54
English (en)
933,989
3.60
Table 14:
Pre-training Corpora Statistics.
The
data is primarily sourced from the CUTE parallel
corpus, with additional Mongolian data collected
following similar quality standards.
C.2
Training Parameter Settings
Table 15 lists the main parameter settings
for the pre-training and supervised ﬁne-tuning
phases.
D
Dataset Details
D.1
WCM-v2 Dataset
WCM-v2 is a multilingual text classiﬁcation
dataset covering 10 domains including arts, ge-
ography, and history (Yang et al., 2022). The
dataset is characterized by its balanced distri-
bution across both categories and languages,
containing Chinese training sets and test sets
in multiple languages. Table 16 shows the sam-
ple distribution of each language across diﬀer-
ent categories.
D.2
Machine Reading Comprehension
Datasets
We utilize three machine reading comprehen-
sion (MRC) datasets for evaluation. Table 17
shows the key statistics of these datasets.
Dataset
Train
Dev
Test
SQuAD v1.1
87,599
10,570
-
CMRC 2018
10,142
3,219
1,002
TibetanQA
-
-
2,007
Table 17: Statistics of machine reading comprehen-
sion datasets used in our experiments. TibetanQA
is used only for testing cross-lingual transfer capa-
bility.
SQuAD
The Stanford Question Answering
Dataset (SQuAD) v1.1 (Rajpurkar, 2016) is
a widely used English reading comprehen-
sion dataset containing over 100,000 question-
answer pairs. The questions and answers were
created by crowdworkers based on Wikipedia
articles, with answers being continuous spans
from the corresponding reading passages.
CMRC
The
Chinese
Machine
Reading
Comprehension (CMRC) 2018 dataset (Cui
et al., 2019) follows a similar format to
SQuAD, featuring span-extraction questions
in Chinese.
The dataset covers various do-
mains, making it suitable for evaluating Chi-
nese reading comprehension capabilities.
TibetanQA
TibetanQA (Sun et al., 2021)
is a Tibetan machine reading comprehension
dataset, with 2,007 publicly released question-
answer pairs for evaluation.
While the full
dataset contains 20,000 question-answer pairs
annotated from articles on Tibetan web re-
sources, only a portion is publicly available
and used in our experiments for zero-shot
cross-lingual evaluation.
Note on Language Coverage
While our
study aims to evaluate cross-lingual trans-
fer across multiple low-resource languages, we
were unable to identify suitable machine read-
ing comprehension datasets for Mongolian and
Uyghur languages at the time of our research.

--- Page 16 ---

Hyperparameter
Pre-training
Fine-tuning
Learning Rate
1.0e-4
2.0e-5
Training Epochs
1.0
3.0
Global Batch Size
1024
256
Max Sequence Length
4096
4096
Warmup Ratio
0.05
0.05
Data Type
BF16
BF16
LR Scheduler
Cosine
Cosine
Table 15: Hyperparameter settings for pre-training and supervised ﬁne-tuning phases. During the pre-
training phase, except for vocabulary expansion, we observed frequent loss spike phenomena when the
learning rate was set to 2.0e-4. After reducing it to 1.0e-4, the training process became more stable.
Category
mn
bo
ug
zh-train
zh-test
Arts
135
141
3
2,657
335
Geography
76
339
256
12,854
1,644
History
66
111
0
1,771
248
Nature
7
0
7
1,105
110
Natural Science
779
133
20
2,314
287
People
1,402
111
0
7,706
924
Technology
191
163
8
1,184
152
Education
6
1
0
936
118
Economy
205
0
0
922
109
Health
106
111
6
551
73
Total
2,973
1,110
300
32,000
3,995
Table 16: Sample distribution across categories and languages in the WCM-v2 dataset. The dataset con-
tains training and test sets for Chinese (zh), and test sets for ethnic minority languages (mn: Mongolian,
bo: Tibetan, ug: Uyghur). Additional test sets for Korean, Kazakh, and Kyrgyz are also available in the
dataset but not used in our experiments.
This limitation highlights the scarcity of eval-
uation resources for these languages in certain
NLP tasks.
E
Translation Details
Flores-200
Dataset
The
Flores-200
dataset
is
a
multilingual
benchmark
for
evaluating
machine
translation
systems,
encompassing
200
languages
(Costa-jussà
et al., 2022). The sentences in the dataset are
derived from English Wikipedia articles and
professionally translated into other languages.
We utilize both the development and test
sets, which contain 997 and 1,012 samples
per language pair, respectively.
To ensure
fair evaluation, we conduct our experiments
exclusively on the test set.
Translation Prompts
We employ English
as the uniﬁed instruction language for transla-
tion tasks. Each prompt contains three care-
fully selected translation examples (3-shot),
with low-resource language text appearing
only in the source-target translation pairs.
Speciﬁcally, the prompt template follows this
structure:
(1) An instruction header:
Translate the following Chinese text
to {target_language}
(2) Three example translation pairs, each for-
matted as:
Chinese: [source text]
{target_language}: [translation]

--- Page 17 ---

(3) The translation request:
Now translate this:
Chinese: [input text]
This design is motivated by two key consid-
erations: First, utilizing English as the instruc-
tion language leverages the model’s strong ca-
pabilities in English; Second, by minimizing
the presence of low-resource languages in the
prompt, we can better evaluate the model’s
genuine translation capabilities rather than
simple pattern matching.
The three exam-
ples are selected to cover diverse sentence
structures and vocabulary complexity, helping
the model understand the requirements of the
translation task.

```
