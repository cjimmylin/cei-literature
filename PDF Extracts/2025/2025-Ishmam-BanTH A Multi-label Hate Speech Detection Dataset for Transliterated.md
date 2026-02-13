---
title: "2025-Ishmam-BanTH A Multi-label Hate Speech Detection Dataset for Transliterated - PDF Extract"
source_pdf: "2025-Ishmam-BanTH A Multi-label Hate Speech Detection Dataset for Transliterated.pdf"
pages: 20
extracted_at: "2026-02-13T09:50:28.390093"
---

# PDF Extract: 2025-Ishmam-BanTH A Multi-label Hate Speech Detection Dataset for Transliterated

**Source PDF:** 2025-Ishmam-BanTH A Multi-label Hate Speech Detection Dataset for Transliterated.pdf
**Total Pages:** 20

---

## Content

```
--- Page 1 ---

arXiv:2410.13281v4  [cs.CL]  31 May 2025
BANTH: A Multi-label Hate Speech Detection
Dataset for Transliterated Bangla
Fabiha Haider1*, Fariha Tanjim Shifat1*, Md Farhan Ishmam1,2*, Deeparghya
Dutta Barua1, Md Sakib Ul Rahman Sourove1, Md Fahim1,3, Md Farhad Alam1
1Research and Development, Penta Global Limited, Bangladesh
2Islamic University of Technology, Bangladesh
3CCDS Lab, Independent University, Bangladesh
pdcsedu@gmail.com, fahimcse381@gmail.com
Abstract
The proliferation of transliterated texts in digi-
tal spaces has emphasized the need for detect-
ing and classifying hate speech in languages
beyond English, particularly in low-resource
languages. As online discourse can perpetu-
ate discrimination based on target groups, e.g.
gender, religion, and origin, multi-label clas-
sification of hateful content can help in under-
standing hate motivation and enhance content
moderation. While previous efforts have fo-
cused on monolingual or binary hate classifica-
tion tasks, no work has yet addressed the chal-
lenge of multi-label hate speech classification
in transliterated Bangla. We introduce BANTH,
the first multi-label transliterated Bangla hate
speech dataset. The samples are sourced from
YouTube comments, where each instance is
labeled with one or more target groups, re-
flecting the regional demographic. We pro-
pose a novel translation-based LLM prompting
strategy that translates or transliterates under-
resourced text to higher-resourced text before
classifying the hate group(s).
Experiments
reveal further pre-trained encoders achieving
state-of-the-art performance on the BANTH
dataset while translation-based prompting out-
performs other strategies in the zero-shot set-
ting. We address a critical gap in Bangla hate
speech and set the stage for further exploration
into code-mixed and multi-label classification
in underrepresented languages.
Content Warning: This article contains examples
of hateful content.
Note: Throughout the work, we use the term
Bangla referring to both Bangla and the endonym
Bengali. The terms denote the same language, pri-
marily spoken by people of the West Bengal region
of India and the vast majority of Bangladesh.
Awami League er shobai ke puriye
mere felo. Ora Indian dalal
non-hate
hate
Binary Classification
Abusive /
Violence
Personal
Offence
Religious
Gender
Body
Shaming
Origin
Political
 Multi-label Classification
Transliterated Bangla Input
Burn everyone from Awami League to
death. They are Indian spy.
English Translation
Figure 1: Binary and Multi-label Classification on an ex-
ample Transliterated Bangla sentence from the BANTH
dataset along with its corresponding English translation.
1
Introduction
The ever-expanding digital landscape that promises
to improve social cohesion has been a breeding
ground for hate speech (Castaño-Pulgarín et al.,
2021). Hate speech is defined as any form of lan-
guage that targets, attacks, or incites implicit or
explicit forms of hatred or violence against groups,
based on specific characteristics, e.g. physical ap-
pearance, religion, ethnic origin, and gender iden-
tity (Papcunová et al., 2023). Hate speech can po-
tentially inflict societal harm by promoting division
among communities, exacerbating mental health
problems, and inciting violence (Sahoo et al., 2024).
The lack of hate speech moderation cultivates an
environment of intolerance and magnifies the nega-
tive impact on the target communities (Hangartner
et al., 2021). Categorizing hate speech requires a
multi-faceted approach to capture overlapping hate
categories and gain a granular understanding of the
underlying motives behind the hateful discourse.
*Equal Contribution
1

--- Page 2 ---

    • Manual Annotation
    • 3 Annotators/Sample
    • Expert Verification
 ✔ English Character
 ✔ Transliterated Bangla
    Min. Sentence Length > 3
      Deduplication
 ✖  Hyperlinks and URLs
 ✖  Redundant Whitespace
 ✖  Personal Information
Data Cleaning
Data Annotation &
Validation
BanTH
Dataset
Data Filtering
 • YouTube API
 • Video Category
 • Published Time
Data Scraping
Data
Source
Figure 2: Overview of the BANTH dataset creation pipeline.
A prevalent informal form of online communi-
cation for non-English languages uses transliter-
ated texts, i.e. writing a language in foreign script.
Transliteration is predominant in Bangla, where
Latin characters are used to produce a colloquial
form of Bangla texts that does not strictly adhere to
the original linguistic rules. Despite boasting over a
quarter of a billion speakers worldwide, Bangla re-
mains a low-resource language in terms of Natural
Language Processing (NLP) tasks (Mahfuz et al.,
2025). The challenges are compounded when work-
ing with the even more under-resourced transliter-
ated Bangla, which dominates online spaces due
to the widespread familiarity of users with English
keyboard layouts (Fahim et al., 2024).
Although transliteration facilitates easier typ-
ing and cross-linguistic communication, it also
complicates the task of automated hate speech de-
tection due to inconsistent spelling and structure,
absence of grammar, mixing with English, and
the loss of script-specific features (Jahan et al.,
2019a). While standard practices have employed
transformer-based encoders (Devlin et al., 2019)
for automated hate speech detection, the recent
surge in popularity of Large Language Models
(LLMs) has positioned them as a viable option
in hate speech NLP, particularly in the zero-shot
setting. While most of the advancements have been
centered on English and other high-resource lan-
guages, transliterated Bangla has limited research
on hate or hate-like speech detection (Jahan et al.,
2019b; Raihan et al., 2023) and LLM-based meth-
ods (Shibli et al., 2023), with no work addressing
the intersection of these areas.
Addressing the aforementioned research gap, our
contribution can be summarized as follows:
• We propose BANTH, the first multi-label
hate speech detection dataset on transliterated
Bangla with 37,350 samples.
• We establish several encoder-based baselines,
with encoders further pre-trained on translit-
erated Bangla achieving state-of-the-art accu-
racy on our dataset.
• We explore zero-shot and few-shot prompt-
ing techniques using state-of-the-art Large
Language Models and introduce a novel
translation-based prompting strategy that out-
performs existing methods on our dataset.
2
BANTH Dataset
The BANTH dataset comprises 37350 samples,
each initially classified into binary labels of Hate or
Non-Hate. To effectively capture the target group,
the hate samples are further multi-labeled as Po-
litical, Religious, Gender, Personal Offense, Abu-
sive/Violence, Origin, and Body Shaming. The de-
scription of target groups is provided in §C.1 and
the dataset creation flowchart is given in Fig. 2.
2.1
Data Sourcing
We construct the dataset by scraping user com-
ments from public YouTube videos using the
YouTube API1. The scraped comments include
three categories of videos: “News & Politics”,
“People & Blogs”, and “Entertainment”, totaling
26 different YouTube channels, outlined in Tab. 4.
The contents often cover a wider range of topics,
including political analysis, interviews, talk shows,
product reviews, and travel videos, regionally rele-
vant to West Bengal of India and Bangladesh.
The scraped comments were collected from Jan-
uary 2020 to July 2024, a time frame that cap-
tures significant recent events, e.g. the COVID-19
pandemic and the Bangladesh quota reform move-
ment2. Such events led to increased social media
activity. The variety of content appeals to a di-
verse audience with a wide range of interests and
perspectives. The label-wise distribution of video
categories is elaborated in Tab. 1 and event-wise
major hate categories are described in Tab. 2.
1https://developers.google.com/youtube/v3/
getting-started
2https://en.wikipedia.org/wiki/2024_
Bangladesh_quota_reform_movement
2

--- Page 3 ---

Hate Category
#News
& Politics
#People
& Blogs
#Enter-
tainment
#Train
#Val
#Test
#Total
Political
1005
174
21
958
120
122
1200
Religious
109
30
0
111
14
14
139
Gender
151
38
4
154
19
20
193
Personal Offense
5883
784
297
5572
696
696
6964
Abusive/Violence
2491
276
121
2312
287
289
2888
Origin
201
11
2
171
21
22
214
Body Shaming
56
29
1
68
8
10
86
Table 1: Distribution of multi-label hate speech among the YouTube video categories and dataset splits of BANTH.
Time Period
Event
#Samples
Major Hate Categories
Dec’19 - Dec’22
COVID-19
878
Abusive/Violence, Personal
Dec’22
Woman dragged by car to death
1245
Personal, Abusive/Violence
Feb’24
BCL leader rapes woman in JU
1542
Personal, Abusive/Violence, Political
July’24 - Aug’24
Quota reform movement
4522
Political, Abusive/Violence, Personal
Aug’24
Anti-Hindu Violence
1081
Religious, Abusive/Violence
Table 2: Events covered in BANTH with the number of hate samples and associated major hate categories.
2.2
Data Filtering
We primarily filtered comments written in Roman
scripts and discarded comments in other translit-
erated languages, e.g. Hindi, during annotation.
The scraped comments were further filtered using
dictionary-based language identification to ensure
only text from the desired language remains. Fi-
nally, texts with a length greater than or equal to
three were kept in the dataset.
2.3
Data Cleaning
During data cleaning, we removed URLs using
regular expressions as they were irrelevant to our
task. We also removed comments that were verba-
tim duplicates of others. Personal information like
addresses and contact numbers was also removed
during annotation.
2.4
Data Annotation
We hired four annotators and two domain experts
for the data annotation process. All the annota-
tors were high school graduates and native Bangla
speakers.
They had extensive exposure to so-
cial media content and actively used transliterated
Bangla text. The annotation process was super-
vised by domain experts with experience in work-
ing with transliterated Bangla text, who provided
guidance and ensured clear and proper annotation
guidelines, outlined in Appendix B. Both the anno-
tators and domain experts received monetary com-
pensation.
Each data sample was annotated by three anno-
tators to ensure consistency and capture a shared
perspective. The annotators were first instructed to
classify a sample as hate or non-hate. The result-
ing hate sample was then multi-labeled according
to the target group descriptions given in §C.1. In
cases where annotators encountered difficulties in
reaching a consensus or understanding the text, the
domain experts resolved the issues.
Fleiss’ Kappa
Expert-
Annotator
Inter-
Annotator
Binary Labeling
0.75
0.71
Political
0.62
0.72
Religious
0.68
0.66
Gender
0.64
0.68
Personal Offense
0.70
0.75
Abusive/Violence
0.72
0.71
Origin
0.68
0.72
Body Shaming
0.64
0.66
Table 3: Expert-annotator and inter-annotator Fleiss’
Kappa Score across hate categories.
2.5
Data Validation
Following the initial phase of data annotation, the
annotators verified whether any samples remained
unlabeled, samples were mislabeled, or if there
were instances where a sample was labeled as hate
without the corresponding multi-label, and vice
3

--- Page 4 ---

Source Category
#Hate
#Non-hate
News & Politics
8745
23695
People & Blogs
1125
2889
Entertainment
412
584
Total
10282
27167
Dataset Statistics
Min Character Count
7
Max Character Count
1951
Average Length
58.09
Standard Deviation
65.13
Total Words
379411
Average Words
10.16
Min Word Count
3
Max Word Count
368
Unique Words
75977
BANTH split
- Train
29879
- Val
3736
- Test
3735
Total
37350
Table 4: Dataset statistics of our BANTH dataset.
versa. Additionally, they ensured that all samples
were in transliterated Bangla only, as samples in
other languages are beyond the scope of our work.
The agreement scores, measured using the Fleiss’
Kappa, are shown the Table 3. We found an inter-
annotator agreement score of 0.53, indicating a
moderate agreement across the hate categories (Is-
lam et al., 2021).
2.6
Dataset Statistics
The train, test, and val dataset splits maintain the
standard 80:10:10 ratio. While splitting, stratifica-
tion was followed to maintain a uniform distribu-
tion of hate and non-hate labels in multi-label cate-
gories. Tab. 1 shows the distribution across video
categories and dataset splits while general statistics
is given Tab. 4. Fig. 3 visualizes the multi-label co-
occurrence within the BANTH dataset, illustrating
the frequency of label pairs appearing together in
the text. Hate categories like Personal and Political
frequently co-occur with other categories while the
opposite is true for categories like Religious and
Body Shaming.
3
Methodology
The experiments are carried out in two stages:
binary classification of hate speech and multi-
label (target group) classification of the predicted
hate speech. Our baselines can be divided into
Political
Religious
Gender
Personal Offense
Abusive/Violence
Origin
Body Shaming
Political
Religious
Gender
Personal Offense
Abusive/Violence
Origin
Body Shaming
1201
31
3
472
133
17
2
31
139
3
50
9
8
0
3
3
193
133
40
7
2
472
50
133
6966
618
61
40
133
9
40
618
2888
10
7
17
8
7
61
10
214
3
2
0
2
40
7
3
86
Heatmap of Co-occurrence of Hate Labels
0
1000
2000
3000
4000
5000
6000
Figure 3: Co-occurrence of multi-label hate BANTH.
two approaches: fine-tuning LMs on our dataset
and prompting GPT-based LLMs using different
prompting and shot settings.
3.1
Further Pretraining
Pretrained LMs such as BERT (Devlin et al., 2019)
and BanglaBERT (Bhattacharjee et al., 2022) are
typically trained on general and formal texts. How-
ever, these models often lack transliterated samples
in their pretraining datasets, essentially becoming a
long-tail distribution problem. To enhance the per-
formance, we employ Further Pretraining (FPT)
(Qiu et al., 2021; Gururangan et al., 2020), utiliz-
ing the Masked Language Modeling (MLM) loss
(Devlin et al., 2019; Zhuang et al., 2021) as our
pretraining objective.
Specifically, for a given sentence S, we represent
the input tokens as X = (x1, x2, . . . , xn). We ran-
domly mask 15% of these tokens with the [MASK]
token, resulting in a masked sequence denoted as
˜X. Let M ⊆{1, 2, . . . , n} represent the set of in-
dices of the masked tokens. We then input ˜X into
the language model fLM. For each masked token
xi (where i ∈M), the model generates predicted
probabilities P(xi| ˜X). The loss for each masked
token is calculated as Li = −log P(xi| ˜X). The
overall loss across all masked tokens is given by:
LMLM = −1
|M|
X
i∈M
log P(xi| ˜X)
We use the encoders further pre-trained on
BanglaTLit-PT corpus(Fahim et al., 2024), which
contains 243k unlabeled Bangla transliterated texts.
The encoders are referred to as TB-Encoders
(Transliterated Bangla Encoders).
4

--- Page 5 ---

Prompt-Strategy
Prompt
Non-Explanatory
Base-prompt
Chain of Though (CoT)
Base-prompt + "Let’s think step by step"
Explanation-based (Exp)
Base-prompt + "Explain why"
HARE
Base-prompt + "Let’s explain step by step"
Why [Positive]
Base-prompt + "Explain why the comment is positive"
Why [Negative]
Base-prompt + "Explain why the comment is negative"
Translation Based [BAN]
"Translate the following transliterated text into standard Bangla" + Prompt-Strategy
Translation Based [ENG]
"Translate the following transliterated text into standard English" + Prompt-Strategy
Table 5: The prompting strategies used in our benchmarks. We consider binary/multi-label classification and
zero-shot/few-shot approaches along with their corresponding prompts.
3.2
LM Finetuning
We input a sentence S into a pre-trained language
model fLM to obtain layer-wise contextual repre-
sentations H = {hl
i}L
l=1, where H = fLM(S) and
L = no. of layers in fLM. We use the representation
from the last layer’s [CLS] token, hL
CLS, as the sen-
tence representation, which is then passed through
a Multi-Layer Perceptron (MLP) for classification.
The transformation is defined as follows:
z = W2 · (ReLU(W1 · hL
CLS + b1)) + b2
The resulting representation z is then employed
for calculating the loss. The TB-Encoders are simi-
larly fine-tuned.
3.3
Prompting Strategy
We adopt one of the following strategies: Why
Positive/Why Negative (Wang et al., 2023),
HARE (Yang et al., 2023), non-explanatory,
explanation-based, CoT (Wei et al., 2022) based
or translation based. An overview of the prompts
has been reported in Tab. 5. We consider GPT
4o (Achiam et al., 2023) and GPT-3.5 (Brown
et al., 2020) in the prompting experiments and
have designed separate base prompts for binary
and multi-label classification. Each of these base
prompts is then extended to one of the prompting
strategies. We consider both zero-shot (Radford
et al., 2019) and few-shot (Brown et al., 2020)
prompting techniques, reported in App. F. The
prompt variations are detailed below:
Vanilla/Base. The base prompting strategy where
we only ask the LLM to do binary or multi-label
classification.
The prompt also includes the
hate speech definition, the target groups, and
their definition in multi-label classification, key
indicators of hate, and labeling instructions.
Explanation Based.
We include the phrase
Explain why with the base prompt and ask the
LLM to show its reasoning.
HARE. We add Let’s explain step by step, as
adapted in Yang et al. (2023), along with the base
prompt and ask the LLM to return its reasoning.
Why Positive Why Negative. Following Wang
et al. (2023), we adopt the approach by adding
the question why the given text is positive or neg-
ative appending to the base prompt in this variation.
CoT-Based. Following Wei et al. (2022), we add
Let’s think step by step along with the base prompt.
Translation Based.
Our proposed prompting
strategy requires LLMs to first convert Bengali
transliterated text into standard Bangla or English
before proceeding with the usual classification. We
hypothesize translating or transliterating an under-
resourced representation to a higher-resourced
representation should help mitigate the problem
of processing under-represented texts, thereby
mitigating the long-tail distribution problem.
Furthermore, LLMs are relatively better at simpler
seq2seq tasks such as transliterating or translat-
ing.
We mix translation-based prompting with
Non-Explanatory, Explanatory, and CoT-based
prompting techniques.
Model
Label
Macro-F1 ↑
Acc. ↑
GPT 3.5
Positive
62.48
69.03
Negative
62.71
66.77
GPT 4o
Positive
63.33
74.91
Negative
69.98
75.29
Table 6: Performance of Why prompting on the BanTH
test split for binary classification.
5

--- Page 6 ---

Models
Binary
Multi-label
Macro-F1 ↑
Acc. ↑
Macro-F1 ↑
Subset Acc. ↑
Hamming Loss ↓
Language Model (LM) Fine-tuning
Bangla LM
BanglaBERT (Bhattacharjee et al., 2022)
76.50
81.04
20.82
54.08
7.26
BanglishBERT (Bhattacharjee et al., 2022)
75.07
80.62
20.61
52.74
7.42
BanglaHateBERT (Jahan et al., 2022a)
70.92
77.54
11.34
49.83
7.97
VAC-BERT (Bhattacharyya et al., 2023)
74.19
79.76
18.45
52.56
7.50
Indian LM
MuRIL (Khanuja et al., 2021)
75.29
80.83
14.58
53.98
7.55
IndicBERT (Kakwani et al., 2020)
74.51
80.48
13.39
51.56
7.88
Multilingual LM
mBERT (Devlin et al., 2019)
74.97
80.37
28.24
52.19
7.78
XLM-R (Conneau et al., 2019)
77.35
81.37
29.29
53.28
7.23
Character-based LM
CharBERT (Ma et al., 2020)
76.61
80.91
19.66
53.21
7.44
Transliterated Bangla (TB) LM (Fahim et al., 2024)
TB-BERT
76.27
79.25
30.17
54.19
7.18
TB-mBERT
77.36
82.57
27.07
54.71
7.28
TB-XLM-R
77.04
81.29
29.04
52.86
7.26
TB-BanglaBERT
77.12
81.61
22.52
53.97
7.37
TB-BanglishBERT
77.12
81.39
21.41
52.79
7.42
Large Language Model (LLM) Prompting
Vanilla/Base Prompting
GPT 3.5 (Brown et al., 2020)
61.44
64.02
24.12
18.27
19.77
GPT 4o (Achiam et al., 2023)
70.05
74.30
36.07
22.60
16.91
GPT 3.5 + Few-shot
61.85
65.65
23.86
16.85
20.36
GPT 4o + Few-shot
68.77
74.18
39.53
26.76
14.16
Chain of Thought (CoT) Prompting
GPT 3.5 + CoT
61.87
65.77
25.61
20.34
19.28
GPT 4o + CoT
69.87
74.14
35.97
22.60
16.64
GPT 3.5 + CoT + Few-shot
63.30
67.80
28.35
20.15
19.15
GPT 4o + CoT + Few-shot
69.50
74.94
36.49
21.10
17.36
Explanation-based (Exp) Prompting
GPT 3.5 + Exp
61.69
65.16
22.61
17.33
19.84
GPT 4o + Exp
69.91
74.16
32.58
19.12
17.94
GPT 3.5 + Exp + Few-shot
62.69
66.60
25.00
18.36
19.57
GPT 4o + Exp + Few-shot
70.70
75.15
35.61
21.33
17.15
HARE Prompting
GPT 3.5 + HARE
62.64
66.77
25.99
20.90
18.94
GPT 4o + HARE
69.71
74.75
36.67
20.80
17.10
GPT 3.5 + HARE + Few-shot
62.20
66.72
24.68
20.06
19.18
GPT 4o + HARE + Few-shot
69.12
74.75
34.06
21.59
17.37
Translation Prompting (Ours)
GPT 4o + Translation [BAN]
69.63
72.70
35.72
23.28
16.73
GPT 4o + Translation [ENG]
69.38
72.96
34.28
20.72
16.91
GPT 4o + Translation [BAN] + CoT
69.01
72.66
36.22
21.35
17.36
GPT 4o + Translation [ENG] + CoT
69.74
74.87
35.94
21.19
16.91
GPT 4o + Translation [BAN] + Exp
70.34
73.65
36.20
21.54
16.46
GPT 4o + Translation [ENG] + Exp
70.19
73.84
36.25
23.92
16.23
Table 7: Model Benchmarking on the test split of BANTH Dataset for Binary and Multi-label Classification. For
LLMS, the results show the zero-shot and few-shot performance for each prompting strategy. Bold represents
overall the best results whereas Underline represents the best performing results in zero-shot settings.
6

--- Page 7 ---

Political
Religious
Gender
Personal Offense
Abusive/Violence
Origin
Body Shaming
Multi-labels
0
20
40
60
80
100
Accuracy (%)
95.6%
99.2%
98.9%
65.9%
84.0%
99.3%
99.4%
4.4%
0.8%
1.1%
34.1%
16.0%
0.7%
0.6%
Correct
Incorrect
Figure 4: Category-wise macro-F1 score of the best-
performing model on BANTH.
4
Experimental Result
The experimental setup is reported in App. D. We
evaluate fine-tuning vanilla pre-trained and further
pre-trained LMs and different prompting strategies
on LLMs. The evaluation metric details have also
been provided in App. E.
4.1
Fine-Tuning LMs Baseline
For the binary classification, TB-mBERT achieves
the best performance across all metrics. In multi-
label classification, TB-BERT outperforms the
other methods based on macro-F1 and hamming
loss but is outperformed by TB-mBERT based on
subset accuracy. Overall, the TB encoders have bet-
ter performance across all metrics in both binary
and multi-label classification tasks.
4.2
Prompt Based LLM Performance
Among prompt-based LLMs, GPT-4o + Few-
shot performed the best for multi-label classifica-
tion, achieving the highest macro-F1 (39.53%),
subset accuracy (26.76%),
and lowest ham-
ming loss (14.16%).
In binary classification,
GPT 4o+Exp+Few-shot has the highest macro-F1
(70.70%). In zero-shot settings, our translation
prompting strategy achieves the best performance
across all metrics by a good margin (~8% improve-
ment over vanilla prompting). Additionally, GPT-4
consistently outperforms GPT-3.5 across all experi-
ments and prompting variations, yielding improve-
ments of 8-10%. We also find that generating ex-
planations can occasionally boost performance, but
may also lead to worse results.
News & Politics
People & Blogs
Entertainment
Video Category
0
20
40
60
80
100
Accuracy (%)
82.8
17.2
82.8
17.2
86.0
14.0
53.7
46.3
53.2
46.8
79.5
20.4
Correct (Binary)
Incorrect (Binary)
Correct (Multi-label)
Incorrect (Multi-label)
Figure 5: Video category-wise class classification ac-
curacy on the BanTH dataset with the best-performing
model. We consider Macro-Accuracy for Binary and
Subset-Accuracy for Multi-label Classification.
5
Error Analysis
5.1
High Error in Personal Offense
Figure 4 illustrates per-label accuracy with the best
performing model, TB-mBERT. Most hate samples
are labeled under Personal Offense (Tab. 1). Inter-
estingly, Personal Offense has the lowest macro-F1
score for mBERT (Fig. 4). This is due to Personal
Offense exhibiting higher variations of transliter-
ated text (Fig. 6,7), making it difficult to attribute
specific words that signify this category. The higher
co-occurrence of this category with other categories
might also contribute to the higher error.
5.2
Representative Words
Analyzing the word cloud in Fig. 6,7, we observe
that certain words representative of their respec-
tive hate categories frequently occurs in the hate
categories with higher performance. For instance,
Muslim frequently appears in "Religious" hate, mo-
hila (woman) and meye (girl) in "Gender" hate, and
so on. In contrast, the frequently occurring words
for "Personal Offense" appear to be generic terms,
e.g. dalal (broker), police, and tui (you). Con-
sequently, it becomes more difficult for language
models to classify a word as "Personal Offense"
due to the lack of representative words.
5.3
Translation by LLMs
As observed in Tab. 8, LLMs can naturally trans-
late Bangla transliterated text into English, even
without explicit instructions. However, when ex-
plicitly instructed to translate, the LLM tends to
give more literal translations. We also observe that
7

--- Page 8 ---

Transliterated Text
English Translation
Pred.
Reason by
GPT-4o+E
Reason by
GPT-4o+E+T
Translation by
GPT-4o+E+T
world er shob deshei torun
shomaj montri mp hoy
khali Bangladesh chara
eitar karon holo onar moto
kichu political peraon jara
sharajibon nijei kheye jete
chay manusher jonno ko-
rte chay na
In all the countries of the
world, youths become so-
cial ministers and MPs,
but except for Bangladesh.
The reason behind this is
a kind of political anarchy
those who live their entire
lives for themselves not
for the welfare of people.
NH
The text criticizes
the entire political
generation
with
derogatory implica-
tions.
The text criticizes politi-
cal leaders in Bangladesh
for not focusing on youth
leadership, but it does not
incite hatred or use dehu-
manizing language.
In all countries of the
world, young people are
made ministers or MPs,
except in Bangladesh. The
reason for this is that some
political persons want to
selfishly continue benefit-
ing themselves instead of
working for the people.
Tomrao to bikri hoe geco
You have been sold too
NH
The
text
implies
corruption and sell-
ing out, suggesting
negative stereotyp-
ing.
The phrase does not ex-
press hatred or discrimina-
tion towards any specific
group or individual.
They have also been sold
out.
Chup catukar khuni
Shut up killer sycophant
H
The text seems to
express frustration
but lacks direct hate
indicators.
The phrase ’chup catukar
khuni’
implies
killing,
which incites violence and
hate.
Shut up, murderous syco-
phant.
Ore dhora hok ainer awtai
ana hok
Let him be caught and
brought under justice
NH
The text calls for
arrest and punish-
ment.
The text talks about bring-
ing someone under the law
without expressing or in-
citing hate or violence.
Let him be caught and
brought under the law.
Agey apnader mordhe in-
dian gulare khuje ber ko-
ren
First,
find the Indians
among yourselves
H
The text calls for
identifying certain
individuals without
expressing hate.
The text stereotypes and
discriminates based on ori-
gin, which is a hate indica-
tor.
First, find the Indian infil-
trators among yourselves.
Myb eta India cal parar
meye
Maybe she is a girl from
some slum in India.
H
The text derogato-
rily implies an In-
dian woman based
on location, with a
stereotype
There is no evident ex-
pression of hate speech in
identifying someone by a
phrase or as a resident of a
place.
Maybe she is a girl from
India Calcutta.
eto jhamelar ki orkar era
beche thakle sob kiso vole
abaro chori bodmashi ko-
rbe
What’s the use of so much
trouble? If they stay alive,
they will forget everything
and steal and do mischief
again.
NH
The text discusses
obstacles
without
expressing hate.
The text suggests that a
group of people, if they
remain alive, will engage
in theft and misconduct
again. It stereotypes and
implies inherent criminal
behavior.
What is the point of all this
trouble, if they stay alive,
they will forget everything
and steal and commit mis-
chief again.
Tora nijerai to political
party er pasa chatis.
You yourselves are the
sycophants of political par-
ties.
H
The text accuses
others
of
oppor-
tunistic
political
affiliations.
The text is a general state-
ment about political affil-
iation without direct hate
speech indicators. It ap-
pears accusatory but not
incite violence or hatred.
You people yourselves are
involved with the political
party.
Bhai
ja
korso
tai
paiso..tmra
joto
marso
oitar hisab k dibe ??
Brother, you got what you
deserved... will you give
an account for how much
you have killed?
NH
The text discusses
the consequences of
actions without hate
indicators.
This text contains implicit
threat and justification for
physical violence, possi-
bly in a retaliatory context.
Brother, you got what you
did.. Who’s going to ac-
count for how much you
hit?
Na
bnp
na
awami
league Islami Andolon
Bangladesh best.
Neither BNP nor Awami
League, Islami Andolon
Bangladesh is the best.
NH
The text expresses
political preference
without any hate in-
dicators.
This text promotes politi-
cal supremacy, suggesting
one political movement is
superior to others.
No
BNP,
no
Awami
League, Islami Andolon
Bangladesh is the best.
Table 8: Comparison of predictions and reasoning generated by GPT-4o using Explanation (E) and Translation (T)
prompting. Green indicates that the prediction (H:Hate and NH:Non-Hate) was correctly labeled by GPT-4o+E+T
but incorrectly labeled by GPT-4o+E, and red indicates incorrect prediction by both the models.
erroneous translations often lead to incorrect classi-
fications, especially with regional dialects or terms
lacking direct English equivalents. English transla-
tions are generally observed to outperform Bangla
ones. When not prompted to translate, the LLM
focuses on identifying hate-related terms, which
works for explicit hate speech but struggles with
subtler forms of offensive content, leading to mis-
classification.
8

--- Page 9 ---

6
Related Work
Hate Speech. Natural Language Processing (NLP)
tasks on hate speech primarily involve hate speech
detection (Schmidt and Wiegand, 2017) which
can be binary (Mutanga et al., 2020; Bose and Su,
2022), multi-class (Yigezu et al., 2023; Hashmi
and Yayilgan, 2024), or multi-label classification
(Mollas et al., 2022). Multi-class and multi-label
tasks generally categorize hate based on race,
religion, gender, origin, and disability. Hate speech
detection has also been explored in multi-modal
(Gomez et al., 2020; Kiela et al., 2020) and
multi-lingual (Aluru et al., 2020; Ousidhoum et al.,
2019) settings.
Bangla Hate Speech.
As a low-resource
language, Bangla has limited work on hate
speech detection (Romim et al., 2022; Das
et al., 2022a) but has made significant progress
on other hate-related tasks involving abusive
content (Hussain et al., 2018; Jahan et al., 2022b),
cyberbullying (Emon et al., 2022), sexism (Jahan
et al., 2023), and violence (Fahim, 2023). The
multi-label variants are generally categorized
based on religion, politics, and gender (Sharif et al.,
2022). Key areas of multi-labeling tasks include
aggression (Hossain et al., 2023), cyberbullying
(Saifuddin et al., 2023), hate speech (Shakil, 2022;
Hasan et al., 2024), and toxic content (Belal et al.,
2023).
Transliterated Bangla.
Research on NLP
tasks using transliterated or romanized Bangla
is notably scarce, with limited works on back-
transliteration (Shibli et al., 2023), abusive content
detection (Jahan et al., 2019b; Sazzed, 2021), hate
speech detection (Das et al., 2022a), offensive
language identification (Raihan et al., 2023),
sentiment analysis (Hassan et al., 2016), and
cyberbullying detection (Ahmed et al., 2021).
While multi-label classification tasks on transliter-
ated Bangla have been explored as sentiment and
emotion analysis tasks (Tripto and Ali, 2018), there
remains a significant research gap on multi-label
hate speech classification for transliterated Bangla.
7
Conclusion
Our novel multi-label hate speech dataset, BANTH,
addresses a crucial research gap in the domain of
transliterated Bangla. Extensive experimentations
on both traditional language models and LLMs
highlight their usefulness in their unique settings.
We envision our novel prompting strategies to be
generalized to the processing of transliterated text
in other languages. We believe our dataset can
serve as a valuable resource in the creation of safer
digital platforms for the future.
Limitations
The BANTH dataset contains 27167 non-hate sam-
ples out of 37350, i.e. a dummy classifier predict-
ing all samples as non-hate achieves an accuracy
of 72.73%. This undermines the performance of
a few methods, notably, GPT-3.5 performs worse
than this baseline.
Our work does not cover all possible hate classes
and may not adequately represent other region-
ally relevant categories, e.g. hate based on socio-
economic conditions.
As the dataset has been
sourced from YouTube comments, there are insuf-
ficient instances of such categories. Adding a low
proportion of these samples will create more imbal-
ance in multi-label classification.
We emphasize that the inter-annotator score is
comparatively lower than in other classification
tasks, primarily due to the inherently subjective
nature of hate speech and the variations in translit-
eration. The expert agreements have also been
found lower than the normal annotators, which can
be attributed to experts having higher levels of dis-
agreement in defining hate categories due to their
deeper understanding of the gray areas in interpre-
tation. In contrast, the simpler and straightforward
thinking can be attributed to the higher agreement
scores between general annotators.
Ethical Considerations
The use of comments scraped from the YouTube
videos complies with the YouTube API’s terms of
services3. All forms of Personal Identification In-
formation (PII) have been removed from the dataset
to prevent privacy violations. We ensured fair dis-
tribution of annotation workload. The hired anno-
tators and domain experts were compensated on an
hourly basis at a rate above the industry standard.
Acknowledgments
We sincerely appreciate the generous support of our
project sponsor, Penta Global Limited, Bangladesh.
3https://developers.google.com/youtube/terms/
api-services-terms-of-service
9

--- Page 10 ---

References
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama
Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
Diogo Almeida, Janko Altenschmidt, Sam Altman,
Shyamal Anadkat, et al. 2023. Gpt-4 technical report.
arXiv preprint arXiv:2303.08774.
Md Tofael Ahmed, Maqsudur Rahman, Shafayet Nur,
Azm Islam, and Dipankar Das. 2021. Deployment
of machine learning and deep learning algorithms
in detecting cyberbullying in bangla and romanized
bangla text: A comparative study. In 2021 Interna-
tional Conference on Advances in Electrical, Comput-
ing, Communication and Sustainable Technologies
(ICAECT), pages 1–10. IEEE.
Tasnim Ahmed, Shahriar Ivan, Mohsinul Kabir, Hasan
Mahmud, and Kamrul Hasan. 2022. Performance
analysis of transformer-based architectures and their
ensembles to detect trait-based cyberbullying. Social
Network Analysis and Mining, 12(1):99.
Sai Saketh Aluru, Binny Mathew, Punyajoy Saha, and
Animesh Mukherjee. 2020. Deep learning models
for multilingual hate speech detection. arXiv preprint
arXiv:2004.06465.
Faisal Yousif Al Anezi. 2022. Arabic hate speech detec-
tion using deep recurrent neural networks. Applied
Sciences, 12(12):6010.
Tanveer Ahmed Belal, GM Shahariar, and Md Hasanul
Kabir. 2023. Interpretable multi labeled bengali toxic
comments classification using deep learning. In 2023
International Conference on Electrical, Computer
and Communication Engineering (ECCE), pages 1–
6. IEEE.
Abhik Bhattacharjee, Tahmid Hasan, Wasi Ahmad,
Kazi Samin Mubasshir, Md Saiful Islam, Anindya
Iqbal, M. Sohel Rahman, and Rifat Shahriyar.
2022. BanglaBERT: Language model pretraining
and benchmarks for low-resource language under-
standing evaluation in Bangla. In Findings of the
Association for Computational Linguistics: NAACL
2022, pages 1318–1327, Seattle, United States. Asso-
ciation for Computational Linguistics.
Pramit Bhattacharyya, Joydeep Mondal, Subhadip Maji,
and Arnab Bhattacharya. 2023.
Vacaspati: A di-
verse corpus of bangla literature.
arXiv preprint
arXiv:2307.05083.
Aditya Bohra, Deepanshu Vijay, Vinay Singh, Syed Sar-
faraz Akhtar, and Manish Shrivastava. 2018.
A
dataset of Hindi-English code-mixed social media
text for hate speech detection. In Proceedings of
the Second Workshop on Computational Modeling
of People’s Opinions, Personality, and Emotions in
Social Media, pages 36–41, New Orleans, Louisiana,
USA. Association for Computational Linguistics.
Saugata Bose and Dr. Guoxin Su. 2022. Deep one-
class hate speech detection model. In Proceedings of
the Thirteenth Language Resources and Evaluation
Conference, pages 7040–7048, Marseille, France. Eu-
ropean Language Resources Association.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, et al. 2020. Language models are few-shot
learners. Advances in neural information processing
systems, 33:1877–1901.
Sergio Andrés Castaño-Pulgarín,
Natalia Suárez-
Betancur, Luz Magnolia Tilano Vega, and Harvey
Mauricio Herrera López. 2021. Internet, social me-
dia and online hate speech. systematic review. Ag-
gression and violent behavior, 58:101608.
Patricia Chiril, Farah Benamara, and Véronique
Moriceau. 2021. “be nice to your wife! the restau-
rants are closed”: Can gender stereotype detection
improve sexism classification? In Findings of the
Association for Computational Linguistics: EMNLP
2021, pages 2833–2844, Punta Cana, Dominican Re-
public. Association for Computational Linguistics.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
Vishrav Chaudhary, Guillaume Wenzek, Francisco
Guzmán, Edouard Grave, Myle Ott, Luke Zettle-
moyer, and Veselin Stoyanov. 2019. Unsupervised
cross-lingual representation learning at scale. CoRR,
abs/1911.02116.
Mithun Das, Somnath Banerjee, Punyajoy Saha, and
Animesh Mukherjee. 2022a. Hate speech and of-
fensive language detection in Bengali. In Proceed-
ings of the 2nd Conference of the Asia-Pacific Chap-
ter of the Association for Computational Linguistics
and the 12th International Joint Conference on Natu-
ral Language Processing (Volume 1: Long Papers),
pages 286–296, Online only. Association for Compu-
tational Linguistics.
Mithun Das, Punyajoy Saha, Binny Mathew, and Ani-
mesh Mukherjee. 2022b. HateCheckHIn: Evaluating
Hindi hate speech detection models. In Proceedings
of the Thirteenth Language Resources and Evalua-
tion Conference, pages 5378–5387, Marseille, France.
European Language Resources Association.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2018. BERT: pre-training of
deep bidirectional transformers for language under-
standing. CoRR, abs/1810.04805.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. BERT: Pre-training of
deep bidirectional transformers for language under-
standing. In Proceedings of the 2019 Conference of
the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies, Volume 1 (Long and Short Papers), pages
4171–4186, Minneapolis, Minnesota. Association for
Computational Linguistics.
Md Imdadul Haque Emon, Khondoker Nazia Iqbal,
Md Humaion Kabir Mehedi, Mohammed Julfikar Ali
Mahbub, and Annajiat Alim Rasel. 2022. Detection
10

--- Page 11 ---

of bangla hate comments and cyberbullying in social
media using nlp and transformer models. In Inter-
national Conference on Advances in Computing and
Data Sciences, pages 86–96. Springer.
Md Fahim. 2023. Aambela at BLP-2023 task 1: Focus
on UNK tokens: Analyzing violence inciting Bangla
text with adding dataset specific new word tokens. In
Proceedings of the First Workshop on Bangla Lan-
guage Processing (BLP-2023), pages 201–207, Sin-
gapore. Association for Computational Linguistics.
Md Fahim, Md Shihab Shahriar, Bangladesh Gazipur,
and Mohammad Ruhul Amin.
Hatexplain space
model: Fusing robustness with explainability in hate
speech analysis.
Md Fahim, Fariha Tanjim Shifat, Fabiha Haider,
Deeparghya Dutta Barua, MD Sakib Ul Rahman
Sourove, Md Farhan Ishmam, and Md Farhad Alam
Bhuiyan. 2024. BanglaTLit: A benchmark dataset
for back-transliteration of Romanized Bangla. In
Findings of the Association for Computational Lin-
guistics: EMNLP 2024, pages 14656–14672, Miami,
Florida, USA. Association for Computational Lin-
guistics.
Raul Gomez, Jaume Gibert, Lluis Gomez, and Dimos-
thenis Karatzas. 2020. Exploring hate speech detec-
tion in multimodal publications. In Proceedings of
the IEEE/CVF winter conference on applications of
computer vision, pages 1470–1478.
Suchin
Gururangan,
Ana
Marasovi´c,
Swabha
Swayamdipta, Kyle Lo, Iz Beltagy, Doug Downey,
and Noah A Smith. 2020. Don’t stop pretraining:
Adapt language models to domains and tasks. arXiv
preprint arXiv:2004.10964.
Dominik Hangartner, Gloria Gennaro, Sary Alasiri,
Nicholas Bahrich, Alexandra Bornhoft, Joseph
Boucher, Buket Buse Demirci, Laurenz Derk-
sen, Aldo Hall, Matthias Jochum, et al. 2021.
Empathy-based counterspeech can reduce racist hate
speech in a social media field experiment.
Pro-
ceedings of the National Academy of Sciences,
118(50):e2116310118.
MD.
Nahid
Hasan,
Kazi
Shadman
Sakib,
Taghrid Tahani Preeti,
Jeza Allohibi,
Abdul-
majeed Atiah Alharbi, and Jia Uddin. 2024. Olf-ml:
An offensive language framework for detection,
categorization, and offense target identification using
text processing and machine learning algorithms.
Mathematics, 12(13).
Ehtesham Hashmi and Sule Yildirim Yayilgan. 2024.
Multi-class hate speech detection in the norwe-
gian language using fast-rnn and multilingual fine-
tuned transformers. Complex & Intelligent Systems,
10(3):4535–4556.
Asif Hassan, Mohammad Rashedul Amin, Abul Kalam
Al Azad, and Nabeel Mohammed. 2016. Sentiment
analysis on bangla and romanized bangla text using
deep recurrent models. In 2016 International Work-
shop on Computational Intelligence (IWCI), pages
51–56. IEEE.
Nimali Hettiarachchi, Ruvan Weerasinghe, and Randil
Pushpanda. 2020. Detecting hate speech in social
media articles in romanized sinhala. In 2020 20th
International Conference on Advances in ICT for
Emerging Regions (ICTer), pages 250–255. IEEE.
Jawad Hossain, Avishek Das, Mohammed Moshiul
Hoque, and Nazmul Siddique. 2023. Multilabel ag-
gressive text classification from social media using
transformer-based approaches. In 2023 26th Inter-
national Conference on Computer and Information
Technology (ICCIT), pages 1–6. IEEE.
Md Gulzar Hussain, Tamim Al Mahmud, and Waheda
Akthar. 2018. An approach to detect abusive bangla
text. In 2018 International Conference on Innovation
in Engineering and Technology (ICIET), pages 1–5.
IEEE.
Muhammad Okky Ibrohim and Indra Budi. 2019. Multi-
label hate speech and abusive language detection
in Indonesian Twitter. In Proceedings of the Third
Workshop on Abusive Language Online, pages 46–
57, Florence, Italy. Association for Computational
Linguistics.
Khondoker Ittehadul Islam, Sudipta Kar, Md Saiful Is-
lam, and Mohammad Ruhul Amin. 2021. SentNoB:
A dataset for analysing sentiment on noisy Bangla
texts. In Findings of the Association for Computa-
tional Linguistics: EMNLP 2021, pages 3265–3271,
Punta Cana, Dominican Republic. Association for
Computational Linguistics.
Maliha Jahan, Istiak Ahamed, Md. Rayanuzzaman Bish-
was, and Swakkhar Shatabda. 2019a. Abusive com-
ments detection in bangla-english code-mixed and
transliterated text. In 2019 2nd International Confer-
ence on Innovation in Engineering and Technology
(ICIET), pages 1–6.
Maliha Jahan, Istiak Ahamed, Md Rayanuzzaman Bish-
was, and Swakkhar Shatabda. 2019b. Abusive com-
ments detection in bangla-english code-mixed and
transliterated text. In 2019 2nd International Confer-
ence on Innovation in Engineering and Technology
(ICIET), pages 1–6. IEEE.
Md Saroar Jahan, Mainul Haque, Nabil Arhab, and
Mourad Oussalah. 2022a. Banglahatebert: Bert for
abusive language detection in bengali. In Proceed-
ings of the Second International Workshop on Re-
sources and Techniques for User Information in Abu-
sive Language Analysis, pages 8–15.
Md Saroar Jahan, Mainul Haque, Nabil Arhab, and
Mourad Oussalah. 2022b.
Banglahatebert: Bert
for abusive language detection in bengali. In Pro-
ceedings of the second international workshop on
resources and techniques for user information in abu-
sive language analysis, pages 8–15.
11

--- Page 12 ---

Sarif Sultan Saruar Jahan, Raqeebir Rab, Peom Dutta,
Hossain Muhammad Mahdi Hassan Khan, Muham-
mad Shahariar Karim Badhon, Sumaiya Binte Has-
san, and Ashikur Rahman. 2023.
Deep learning
based misogynistic bangla text identification from
social media. Computing and Informatics, 42(4):993–
1012.
Divyanshu Kakwani, Anoop Kunchukuttan, Satish
Golla, Gokul N.C., Avik Bhattacharyya, Mitesh M.
Khapra, and Pratyush Kumar. 2020. IndicNLPSuite:
Monolingual Corpora, Evaluation Benchmarks and
Pre-trained Multilingual Language Models for Indian
Languages. In Findings of EMNLP.
TaeYoung Kang,
Eunrang Kwon,
Junbum Lee,
Youngeun Nam, Junmo Song, and JeongKyu Suh.
2022. Korean online hate speech dataset for mul-
tilabel classification: How can social science im-
prove dataset on hate speech?
arXiv preprint
arXiv:2204.03262.
Simran Khanuja, Diksha Bansal, Sarvesh Mehtani,
Savya Khosla,
Atreyee Dey,
Balaji Gopalan,
Dilip Kumar Margam, Pooja Aggarwal, Rajiv Teja
Nagipogu, Shachi Dave, Shruti Gupta, Subhash
Chandra Bose Gali, Vish Subramanian, and Partha
Talukdar. 2021. Muril: Multilingual representations
for indian languages. Preprint, arXiv:2103.10730.
Douwe Kiela, Hamed Firooz, Aravind Mohan, Vedanuj
Goswami, Amanpreet Singh, Pratik Ringshia, and
Davide Testuggine. 2020. The hateful memes chal-
lenge: Detecting hate speech in multimodal memes.
Advances in neural information processing systems,
33:2611–2624.
Jean Lee, Taejun Lim, Heejun Lee, Bogeun Jo, Yangsok
Kim, Heegeun Yoon, and Soyeon Caren Han. 2022.
K-MHaS: A multi-label hate speech detection dataset
in Korean online news comment. In Proceedings of
the 29th International Conference on Computational
Linguistics, pages 3530–3538, Gyeongju, Republic
of Korea. International Committee on Computational
Linguistics.
Wentao Ma, Yiming Cui, Chenglei Si, Ting Liu,
Shijin Wang, and Guoping Hu. 2020.
Char-
bert: Character-aware pre-trained language model.
Preprint, arXiv:2011.01513.
Tamzeed Mahfuz, Satak Kumar Dey, Ruwad Naswan,
Hasnaen Adil, Khondker Salman Sayeed, and
Haz Sameen Shahgir. 2025. Too late to train, too
early to use? a study on necessity and viability of
low-resource Bengali LLMs. In Proceedings of the
31st International Conference on Computational Lin-
guistics, pages 1183–1200, Abu Dhabi, UAE. Asso-
ciation for Computational Linguistics.
Binny Mathew, Punyajoy Saha, Seid Muhie Yimam,
Chris Biemann, Pawan Goyal, and Animesh Mukher-
jee. 2021. Hatexplain: A benchmark dataset for ex-
plainable hate speech detection. In Proceedings of
the AAAI conference on artificial intelligence, vol-
ume 35, pages 14867–14875.
Ioannis Mollas, Zoe Chrysopoulou, Stamatis Karlos,
and Grigorios Tsoumakas. 2022. Ethos: a multi-label
hate speech detection dataset. Complex & Intelligent
Systems, 8(6):4663–4678.
Aida Mostafazadeh Davani, Ali Omrani, Brendan
Kennedy, Mohammad Atari, Xiang Ren, and Morteza
Dehghani. 2021. Improving counterfactual genera-
tion for fair hate speech detection. In Proceedings
of the 5th Workshop on Online Abuse and Harms
(WOAH 2021), pages 92–101, Online. Association
for Computational Linguistics.
Raymond T Mutanga, Nalindren Naicker, and Olu-
dayo O Olugbara. 2020. Hate speech detection in
twitter using transformer methods.
International
Journal of Advanced Computer Science and Applica-
tions, 11(9).
Chikashi Nobata, Joel Tetreault, Achint Thomas, Yashar
Mehdad, and Yi Chang. 2016. Abusive language
detection in online user content. In Proceedings of
the 25th international conference on world wide web,
pages 145–153.
Nedjma Ousidhoum, Zizheng Lin, Hongming Zhang,
Yangqiu Song, and Dit-Yan Yeung. 2019. Multi-
lingual and multi-aspect hate speech analysis. In
Proceedings of the 2019 Conference on Empirical
Methods in Natural Language Processing and the
9th International Joint Conference on Natural Lan-
guage Processing (EMNLP-IJCNLP), pages 4675–
4684, Hong Kong, China. Association for Computa-
tional Linguistics.
Jana Papcunová, Marcel Martonˇcik, Denisa Fedáková,
Michal Kentoš, Miroslava Bozogáˇnová, Ivan Srba,
Robert Moro, Matúš Pikuliak, Marián Šimko, and
Matúš Adamkoviˇc. 2023. Hate speech operational-
ization: a preliminary examination of hate speech
indicators and their structure. Complex & intelligent
systems, 9(3):2827–2842.
Hrushikesh Patil, Abhishek Velankar, and Raviraj Joshi.
2022. L3Cube-MahaHate: A tweet-based Marathi
hate speech detection dataset and BERT models. In
Proceedings of the Third Workshop on Threat, Ag-
gression and Cyberbullying (TRAC 2022), pages 1–9,
Gyeongju, Republic of Korea. Association for Com-
putational Linguistics.
Zhengqi Pei, Zhewei Sun, and Yang Xu. 2019. Slang
detection and identification. In Proceedings of the
23rd Conference on Computational Natural Lan-
guage Learning (CoNLL), pages 881–889, Hong
Kong, China. Association for Computational Lin-
guistics.
Flor Miriam Plaza-del Arco, M Dolores Molina-
González, L Alfonso Urena-López, and M Teresa
Martín-Valdivia. 2021. Comparing pre-trained lan-
guage models for spanish hate speech detection. Ex-
pert Systems with Applications, 166:114120.
Rahul Pradhan, Ankur Chaturvedi, Aprna Tripathi, and
Dilip Kumar Sharma. 2020. A review on offensive
12

--- Page 13 ---

language detection. Advances in Data and Informa-
tion Sciences: Proceedings of ICDIS 2019, pages
433–439.
Yao Qiu, Jinchao Zhang, and Jie Zhou. 2021. Different
strokes for different folks: Investigating appropriate
further pre-training approaches for diverse dialogue
tasks. arXiv preprint arXiv:2109.06524.
Alec Radford, Jeffrey Wu, Rewon Child, David Luan,
Dario Amodei, Ilya Sutskever, et al. 2019. Language
models are unsupervised multitask learners. OpenAI
blog, 1(8):9.
Md Nishat Raihan, Umma Hani Tanmoy, Anika Binte
Islam, Kai North, Tharindu Ranasinghe, Antonios
Anastasopoulos, and Marcos Zampieri. 2023. Offen-
sive language identification in transliterated and code-
mixed bangla. arXiv preprint arXiv:2311.15023.
Tharindu Ranasinghe and Marcos Zampieri. 2020. Mul-
tilingual offensive language identification with cross-
lingual embeddings. In Proceedings of the 2020 Con-
ference on Empirical Methods in Natural Language
Processing (EMNLP), pages 5838–5844, Online. As-
sociation for Computational Linguistics.
Nauros Romim, Mosahed Ahmed, Md Saiful Islam,
Arnab Sen Sharma, Hriteshwar Talukder, and Mo-
hammad Ruhul Amin. 2022. BD-SHS: A bench-
mark dataset for learning to detect online Bangla hate
speech in different social contexts. In Proceedings of
the Thirteenth Language Resources and Evaluation
Conference, pages 5153–5162, Marseille, France. Eu-
ropean Language Resources Association.
Nihar Ranja Sahoo, Gyana Prakash Beria, and Pushpak
Bhattacharyya. 2024. Indicconan: A multilingual
dataset for combating hate speech in indian context.
In Proceedings of the AAAI Conference on Artificial
Intelligence, volume 38, pages 22313–22321.
Md Saifuddin, Mohiuddin Ahmed, Spandan Basu, and
Pritam Acharjee. 2023.
Enhancing online safety:
Natural language processing based multi-label cy-
berbullying classification in bangla. In 2023 26th
International Conference on Computer and Informa-
tion Technology (ICCIT), pages 1–6. IEEE.
Salim Sazzed. 2021.
Abusive content detection in
transliterated bengali-english social media corpus. In
Proceedings of the Fifth Workshop on Computational
Approaches to Linguistic Code-Switching, pages 125–
130.
Anna Schmidt and Michael Wiegand. 2017. A survey
on hate speech detection using natural language pro-
cessing. In Proceedings of the Fifth International
Workshop on Natural Language Processing for So-
cial Media, pages 1–10, Valencia, Spain. Association
for Computational Linguistics.
Mahmudul Hasan Shakil. 2022. A hybrid deep learning
model and explainable AI-based Bengali hate speech
multi-label classification and interpretation. Ph.D.
thesis, Brac University.
Omar
Sharif,
Eftekhar
Hossain,
and
Mo-
hammed Moshiul Hoque. 2022.
M-bad:
A
multilabel dataset for detecting aggressive texts
and their targets. In Proceedings of the Workshop
on Combating Online Hostile Posts in Regional
Languages during Emergency Situations, pages
75–85.
GM Shahariar Shibli, Md Tanvir Rouf Shawon,
Anik Hassan Nibir, Md Zabed Miandad, and
Nibir Chandra Mandal. 2023.
Automatic back
transliteration of romanized bengali (banglish) to ben-
gali. Iran Journal of Computer Science, 6(1):69–80.
Fariha Tanjim Shifat, Fabiha Haider, MSUR Sourove,
Deeparghya Dutta Barua, Md Farhan Ishmam,
Md Fahim, and Farhad Alam Bhuiyan. 2024. Penta-
nlp at exist 2024 task 1–3: Sexism identification,
source intention, sexism categorization in tweets.
Working Notes of CLEF.
Manuel Tonneau, Diyi Liu, Samuel Fraiberger, Ralph
Schroeder, Scott Hale, and Paul Röttger. 2024. From
languages to geographies: Towards evaluating cul-
tural bias in hate speech datasets. In Proceedings
of the 8th Workshop on Online Abuse and Harms
(WOAH 2024), pages 283–311, Mexico City, Mexico.
Association for Computational Linguistics.
Nafis Irtiza Tripto and Mohammed Eunus Ali. 2018.
Detecting multilabel sentiment and emotions from
bangla youtube comments. In 2018 international
conference on Bangla speech and language process-
ing (ICBSLP), pages 1–6. IEEE.
Grigorios Tsoumakas and Ioannis Katakis. 2009. Multi-
label classification: An overview. International Jour-
nal of Data Warehousing and Mining, 3:1–13.
Kanishk Verma, Tijana Milosevic, Keith Cortis, and
Brian Davis. 2022. Benchmarking language mod-
els for cyberbullying identification and classification
from social-media texts. In Proceedings of the First
Workshop on Language Technology and Resources
for a Fair, Inclusive, and Safe Society within the
13th Language Resources and Evaluation Confer-
ence, pages 26–31, Marseille, France. European Lan-
guage Resources Association.
Han Wang, Ming Shan Hee, Md Rabiul Awal, Kenny
Tsu Wei Choo, and Roy Ka-Wei Lee. 2023. Evaluat-
ing gpt-3 generated explanations for hateful content
moderation. Preprint, arXiv:2305.17680.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou,
et al. 2022. Chain-of-thought prompting elicits rea-
soning in large language models. Advances in neural
information processing systems, 35:24824–24837.
Mengzhou Xia, Anjalie Field, and Yulia Tsvetkov. 2020.
Demoting racial bias in hate speech detection. In
Proceedings of the Eighth International Workshop
on Natural Language Processing for Social Media,
pages 7–14, Online. Association for Computational
Linguistics.
13

--- Page 14 ---

Yongjin Yang, Joonkee Kim, Yujin Kim, Namgyu Ho,
James Thorne, and Se young Yun. 2023. Hare: Ex-
plainable hate speech detection with step-by-step rea-
soning. Preprint, arXiv:2311.00321.
Mesay Gemeda Yigezu, Olga Kolesnikova, Grig-
ori Sidorov, and Alexander F Gelbukh. 2023.
Transformer-based hate speech detection for multi-
class and multi-label classification. In IberLEF@
SEPLN.
Liu Zhuang, Lin Wayne, Shi Ya, and Zhao Jun. 2021. A
robustly optimized BERT pre-training approach with
post-training. In Proceedings of the 20th Chinese
National Conference on Computational Linguistics,
pages 1218–1227, Huhhot, China. Chinese Informa-
tion Processing Society of China.
A
Additional Related Work
Hate-like Tasks. Hate speech lacks a consistent
definition across the literature and has significant
overlap with similar detection tasks involving of-
fensive language (Pradhan et al., 2020; Ranasinghe
and Zampieri, 2020), sexism (Chiril et al., 2021;
Shifat et al., 2024), abusive content (Nobata et al.,
2016), slang (Pei et al., 2019), and cyberbullying
(Verma et al., 2022; Ahmed et al., 2022). The
studies on hate speech also focused on areas, such
as explainability (Mathew et al., 2021; Fahim
et al.), fairness (Mostafazadeh Davani et al., 2021),
and bias mitigation (Xia et al., 2020).
Non-English Hate Speech.
While the ma-
jority of the hate speech datasets are in US English
(Tonneau et al., 2024), the task has been explored
in
several
non-English
languages
including
Arabic (Anezi, 2022), Hindi (Das et al., 2022b),
Indonesian (Ibrohim and Budi, 2019), Korean
(Kang et al., 2022; Lee et al., 2022), Marathi
(Patil et al., 2022), and Spanish (Plaza-del Arco
et al., 2021). Due to the prevalence of English
alphabets in digital spaces, some of these works
involve transliterated (Hettiarachchi et al., 2020)
and code-mixed texts (Bohra et al., 2018).
B
BanTH Dataset Annotation Guidelines
This document outlines the procedures required
for accurate annotation of texts within the BanTH
dataset. Annotators are expected to follow each
step meticulously to ensure consistency and preci-
sion. Your role as an annotator is critical to main-
taining the integrity and quality of the dataset.
Binary Classification - Hate/Non-Hate:
Texts
containing offensive, abusive, or harmful language
targeting individuals or groups based on their iden-
tity, characteristics, or affiliations are to be labeled
hate. If the text does not include offensive or harm-
ful content it is to be labeled non-hate.
Steps:
1. Review the text in transliterated Bangla.
2. Classify it as either Hate Speech or Non-Hate
Speech.
3. If the comment is Non-Hate, stop here. No
further labeling is necessary.
Multi-Label Hate Speech Classification:
For
texts classified as Hate Speech, assign one or more
relevant labels from the following categories. Each
text may fit multiple categories, so assign all that
apply.
• Political: Texts that attack, criticize, or pro-
mote hate based on political affiliations, views,
or ideologies. This includes language dehu-
manizing political opponents or encouraging
harm.
Example:
[BN] "Oder rajniti desh ta noshto korche."
[EN] "Their politics are destroying the coun-
try."
• Religious: Texts targeting someone’s reli-
gious beliefs or lack thereof, or that promote
violence or discrimination based on religion.
Example:
[BN] "Ei dhormo manushkei bhag kore."
[EN] "This religion only divides people."
• Gender: Texts that reinforce harmful gender
stereotypes or discriminate based on gender
identity or expression. Includes sexist or trans-
phobic remarks.
Example:
[BN] "Meyera kaj korte pare na, barir kaji
kore."
[EN] "Women can’t work, they only do house-
hold chores."
• Personal Offense: Deeply insulting or offen-
sive remarks directed at an individual, which
do not target a specific group but are highly
personal.
Example:
[BN] "Tui ekta boka chele."
[EN] "You’re a stupid boy."
14

--- Page 15 ---

• Abusive/Violence: Texts that contain explicit
threats of violence or encourage violent acts
against individuals or groups.
Example:
[BN] "Tor matha guriye debo."
[EN] "I’ll smash your head."
• Origin: Texts targeting someone based on
their nationality, ethnicity, or race. This in-
cludes racial slurs or calls for exclusion based
on origin.
Example:
[BN] "Ei desher manush er kono kotha nai."
[EN] "People from this country don’t matter."
• Body Shaming: Texts that criticize or mock
someone’s physical appearance, such as body
size or traits, including physical disabilities or
conditions.
Example:
[BN] "Tor pet eto boro kano?"
[EN] "Why is your stomach so big?"
Each sample will be annotated by three different
annotators. After all of this, domain experts will
verify the labels to ensure quality.
Notes: Firstly, carefully read and understand each
text before assigning labels. Note that, a sample
can receive multiple labels if it fits into more than
one category. Please ensure cross-verification by
collaborating with fellow annotators. If the prob-
lem is not solved even after collaboration then con-
tact domain experts because accuracy is essential
for a high-quality dataset.
C
Additional Details of BANTH
C.1
Formal Description of Target Groups
The description of the target group with suitable
examples is given in the following:
Political: Statements that marginalize, threaten,
or incite violence against individuals or groups
based on their political affiliations or ideologies.
Includes calls for harming political opponents,
dehumanizing metaphors applied to political
groups, or the deliberate spread of disinformation
intended to foment hatred.
Religious: Expressions targeting individuals or
groups due to their religious beliefs, practices, or
lack thereof. Includes language that demonizes re-
ligious communities, advocates for discrimination
against religious groups, or incites violence toward
religious institutions or adherents.
Gender:
Extends beyond sexist remarks and
includes
language
promoting
gender-based
violence, discrimination based on gender identity,
misogynistic or misandrist content, transphobic
speech, and language reinforcing harmful gender
stereotypes.
Personal Offense: Deeply insulting or offensive
language directed at an individual.
Includes
mocking tragedies, using insulting names, or
making derogatory comments.
Abusive/Violence: Explicit threats of violence,
detailed descriptions of harm one wishes to inflict
on others, or speech that glorifies or encourages
violent acts against individuals or groups.
Origin: Expressions that target individuals or
groups based on their national, ethnic, or racial
background.
Includes racial slurs, promotion
of racist/nationalist ideologies, calls for racial
segregation or deportation, or speech that attributes
negative characteristics to groups.
Body Shaming:
Derogatory comments on a
person’s physical appearance, often related to
weight, shape, or size. Can extend to mocking
people with physical disabilities, skin conditions,
or other visible physical traits.
C.2
Wordcloud
From Figure 6 and the corresponding English trans-
lations in Figure 7, we can visualize the mostly
mentioned words for each label in the BanTH
dataset. For Political label, people often referred
to Hasina (ex-prime minister of Bangladesh), bnp
(a major political party in Bangladesh), league/lig
(wing of a political party in Bangladesh), dalal (bro-
ker), police (a law enforcement force), etc. As we
have covered transliterated Bangla YouTube com-
ments of July 2024, the BanTH dataset includes
the public responses related to the political unrest
of Bangladesh during that period.
In Religious labeled sample texts, people often
mention Muslim, Hindu nastik (atheist), Allah (the
one and only God in Islam), etc. Gender related
hate comments are mostly related to females. In
Personal Offense case, commenters address dalal
15

--- Page 16 ---

(broker) and police (a law enforcement force) con-
temptuously using tui/tor. The same case is evident
in Abusive/Violence labeled samples because the
police showed violence during the student protest
of July 2024.
As transliterated Bangla is used by mainly In-
dian and Bangladeshi people, Origin related hate
is often directed towards Bangladeshi and Indian
people. For Body Shaming classified samples, we
see people refer to others as mota (fat) and takla
(bald) to body shame and it is directed mostly to-
wards females as apu (sister) is one of the most
used words. Although the BanTH dataset is con-
centrated on these types of hateful words, it may
not be the case when the source is different.
D
Experimental Setup
For Language Models (LMs) baseline exper-
iments, we fine-tuned a range of pre-trained
LMs to establish baselines for binary and
multi-label classification on the BanTH dataset.
The
models
include
multilingual
architec-
tures
like
XLM-RoBERTa(Conneau
et
al.,
2019) and mBERT(Devlin et al., 2018), as
well
as
language-specific
models
such
as
BanglaBERT(Bhattacharjee et al., 2022) and
BanglishBERT(Bhattacharjee
et
al.,
2022),
which are designed for Bangla and code-mixed
transliterated Bangla text, respectively. We also
employed BanglaHateBERT(Jahan et al., 2022a),
specifically optimized for detecting hate speech
in Bangla, along with IndicBERT(Kakwani et al.,
2020) and MuRIL(Khanuja et al., 2021), tailored
for Indian languages. Additionally, we included
models like CharBERT(Ma et al., 2020), and
VAC-BERT(Bhattacharyya et al., 2023) to capture
diverse model architectures, including lightweight
models and character-level representations.
The models were fine-tuned with a learning rate
of 2e-5, using the Adam optimizer. The maximum
sequence length was set to 512 tokens, and training
was performed for 5 epochs with a batch size of
32. Early stopping was applied based on the valida-
tion loss to prevent overfitting. For prompt-based
experiments, we used OpenAI API to get LLM
responses for GPT-3.5 and GPT-4o models. For
measuring the performance, we consider Macro-F1
& Accuracy metrics for binary classification and
Macro-F1, Subset-Accuracy & Hamming Loss
for multilabel classification. In our further pre-
training experiments, we randomly masked 15%
of the tokens and used Masked Language Model
loss (MLM loss) as the pretraining objectives. We
used a learning rate of 1e-5, with batch_size = 32
and we trained the the TB-Encoder models for 5
epochs on the whole training dataset.
E
Performance Metrics
F1-Score.
Harmonic mean of precision and
recall, providing a balance between the two. It
is particularly useful in cases of imbalanced
datasets, as it accounts for both false positives and
false negatives. For multi-label classification, the
F1-Score is computed per label, and the final score
is obtained by averaging across all labels.
Macro-Accuracy.
For binary classification,
we report macro-accuracy, which averages the
accuracy across both classes (positive and nega-
tive), providing a balanced view of the model’s
performance across the two categories.
This
is especially relevant when dealing with class
imbalance, as it ensures that both classes are
equally represented in the final accuracy measure.
Subset-Accuracy.
Requires an exact match
between the predicted and true label sets for each
instance, meaning that all labels must be predicted
correctly for a prediction to be considered accurate
(Tsoumakas and Katakis, 2009).
Hamming Loss Measures the fraction of labels
that are incorrectly predicted, either by being
wrongly assigned or missed altogether. This metric
is useful for multi-label classification as it accounts
for both false positives and negatives across all
labels. A lower Hamming Loss value indicates
better performance as it signifies fewer labeling
mistakes.
16

--- Page 17 ---

F
Prompts for Classification on BanTH
dataset
Base Prompt for Binary Classification (0
shot)
You are an expert at detecting hate speech in Bangla
text (written in Latin script/English letters). Your
task is to classify texts as either hate speech (true)
or non-hate speech (false).
HATE SPEECH DEFINITION:
Text that expresses or incites hatred, discrimination,
or violence against individuals or groups based on:
- Political affiliation
-
Religion
(e.g.,
Hindu,
Muslim,
Buddhist,
Christian)
- Gender
- Personal offense
- Abusive or violence
- Origin
- Body Shaming
KEY INDICATORS OF HATE SPEECH:
1. Dehumanizing language or comparisons
2. Calls for violence or harm
3. Discriminatory slurs or epithets
4. Stereotyping entire groups negatively
5. Promoting supremacy of one group over others
LABELING INSTRUCTIONS:
1. For each text, determine if it contains hate speech
indicators
2. If any hate indicators are present, classify as hate
speech (true)
3. If no hate indicators are present, classify as
non-hate speech (false)
SPECIAL CONSIDERATIONS:
- Consider local context and cultural references
- Be mindful of dialectal variations in spelling
- Pay attention to code-mixing (Bangla-English
hybrid phrases)
- For ambiguous cases, focus on the presence of
hate indicators
You will receive an array of objects, each containing
an ’id’ and ’text’. Analyze each text and provide
the required classification.
Base Prompt for Multilabel Classification
(0 shot)
You are an expert at detecting and categorizing
hate speech in Bangla text (written in Latin
script/English letters). Your task is to classify texts
into multiple categories of hate speech.
HATE SPEECH CATEGORIES:
1. POLITICAL: Targeting individuals or groups
based on political affiliation or beliefs
2. RELIGIOUS: Targeting individuals or groups
based on religion (e.g., Hindu, Muslim, Buddhist,
Christian)
3. GENDER: Targeting individuals or groups based
on gender identity or expression
4.
PERSONAL OFFENSE: Insults or attacks
directed at specific individuals
5.
ABUSIVE/VIOLENCE: Language that is
abusive or incites violence
6. BODY SHAMING: Targeting individuals based
on physical appearance or body type
7. ORIGIN: Targeting individuals or groups based
on their place of origin, ethnicity, or nationality
8. MISC (Miscellaneous): Other forms of hate
speech not covered by the above categories
KEY INDICATORS OF HATE SPEECH:
1. Dehumanizing language or comparisons
2. Calls for violence or harm
3. Discriminatory slurs or epithets
4. Stereotyping entire groups negatively
5. Promoting supremacy of one group over others
LABELING INSTRUCTIONS:
1. For each text, determine if it contains hate speech
indicators for any of the defined categories
2. Assign (True) all relevant hate speech categories
to the text
3. If no hate indicators are present, classify as
non-hate speech (empty array for categories)
SPECIAL CONSIDERATIONS:
- Consider local context and cultural references
- Be mindful of dialectal variations in spelling
- Pay attention to code-mixing (Bangla-English
hybrid phrases)
- A single text may belong to multiple hate speech
categories
- Use the MISC category for hate speech that
doesn’t fit into other categories
You will receive an array of objects, each containing
an ’id’ and ’text’.
Analyze each text and provide the required classifi-
cation.
17

--- Page 18 ---

In-context Examples in Few-Shot Prompt-
ing for Binary Classification
HATE(true)
1. Ei hindu gula ke desh theke ber kore dite hobe,
era shobi desher shotru
English Translation : These Hindus need to be
thrown out of the country, they are all enemies of
the nation.
Reason: Calls for the expulsion of religious groups
(Hindus) and labels them all as enemies
2. Chakma der manush e bhabo na, oder shob ke
mere fela uchit
English Translation : Don’t even think of the
Chakmas as humans, all of them should be killed.
Reason: Dehumanizes ethnic group (Chakma) and
calls for violence against them
NON-HATE(False)
1. Ami or political opinion er shathe ekmat hoi na,
kintu sheta niye kharap lage na
English Translation:
I don’t agree with his
political opinion, but it doesn’t bother me.
Reason: Expresses disagreement without hatred or
discrimination
2. Amader team abar harlo, ki kharap khelse ora
English Translation: Our team lost again, they
played so badly
Reason: Expresses criticism without targeting any
protected group
CoT-Based Prompt
CHAIN-OF-THOUGHT ANALYSIS STEPS:
1. Initial reading: Read the entire text and identify
any potential hate speech elements.
2. Keyword identification: Highlight specific words
or phrases that could indicate hate speech.
3. Context analysis: Consider the overall context
and tone of the message.
4.
Category mapping:
Connect the identified
elements to specific hate speech categories.
5. Multi-label consideration: Determine if the text
fits into multiple categories.
6. Intensity assessment: Evaluate the severity or
intensity of the hate speech, if present.
7. Final classification: Summarize the findings and
assign relevant categories.
In-context Examples in Few-Shot Prompt-
ing for Multi-label Classification
HATE(true)
1. Ei hindu neta gula ke desh theke ber kore dite
hobe, era shobi desher shotru
English Translation: These Hindu leaders need to
be thrown out of the country, they are all enemies
of the nation.
Categories: RELIGIOUS, POLITICAL
Reason: Calls for expulsion of religious group
(Hindus) and labels them all as enemies
2. Tumi ekta mota beyadob, tomar moto lok der
vote deoya uchit na
English Translation:You are a rude fat person,
people like you don’t deserve to be voted for.
Categories:
BODY SHAMING, POLITICAL,
PERSONAL OFFENCE
Reason: Uses body shaming language, suggests
denying voting rights, and personally insults the
individual
3. Ei mohila neta ra shudhu ghor e thakle e desh er
unnoti hobe, oder politics e ashar ki dorkar
English Translation:
If these women leaders
stayed at home, the country would progress; why
do they need to come into politics?
Categories: GENDER, POLITICAL
Reason: Discriminates against women in poli-
tics, targeting both gender and political participation
NON-HATE(False)
1. Ami or political opinion er shathe ekmat hoi na,
kintu sheta niye kharap lage na
English Translation:
I don’t agree with his
political opinion, but it doesn’t bother me.
Categories: None
Reason: Expresses disagreement without hatred or
discrimination
2. Amader team abar harlo, ki kharap khelse ora
English Translation: Our team lost again, they
played so badly
Categories: None
Reason: Expresses criticism without targeting any
protected group
Translation-Based Prompt
You are an expert at detecting hate speech. You will
be given an array of Bangla texts (written in Latin
script/English letters). First, convert the Bangla
Transliterated text into standard Bangla without los-
ing the semantic meaning, then classify the text as
either hate speech (true) or non-hate speech (false).
Provide a reason for your classification and provide
the translation.
18

--- Page 19 ---

(a) Political
(b) Religious
(c) Gender
(d) Personal Offense
(e) Abusive/Violence
(f) Origin
(g) Body Shaming
Figure 6: Word clouds constructed from transliterated Bangla texts in the BANTH dataset for each label.
19

--- Page 20 ---

(a) English Political
(b) Religious(English Translated)
(c) Gender (English Translated)
(d) Personal Offense (English Translated)
(e) Abusive/Violence (English Translated)
(f) Origin (English Translated)
(g) Body Shaming (English Translated)
Figure 7: Word clouds constructed from English translations of the Bangla texts in the BANTH dataset for each
label.
20

```
