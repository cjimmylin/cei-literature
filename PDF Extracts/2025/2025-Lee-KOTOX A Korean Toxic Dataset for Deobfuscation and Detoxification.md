---
title: "2025-Lee-KOTOX A Korean Toxic Dataset for Deobfuscation and Detoxification - PDF Extract"
source_pdf: "2025-Lee-KOTOX A Korean Toxic Dataset for Deobfuscation and Detoxification.pdf"
pages: 26
extracted_at: "2026-02-13T09:50:29.123479"
---

# PDF Extract: 2025-Lee-KOTOX A Korean Toxic Dataset for Deobfuscation and Detoxification

**Source PDF:** 2025-Lee-KOTOX A Korean Toxic Dataset for Deobfuscation and Detoxification.pdf
**Total Pages:** 26

---

## Content

```
--- Page 1 ---

KOTOX: A Korean Toxic Dataset for Deobfuscation and Detoxification
Yejin Lee, Su-Hyeon Kim, Hyundong Jin, Dayoung Kim, Yeonsoo Kim and Yo-Sub Han*
Yonsei University, Seoul, Republic of Korea,
{ssgyejin,suhyeon.kim,tuzi04,dy3835,yujacha0806,emmous}@yonsei.ac.kr
Abstract
Online communication increasingly amplifies
toxic language, and recent research actively
explores methods for detecting and rewriting
such content. Existing studies primarily focus
on non-obfuscated text, which limits robust-
ness in the situation where users intention-
ally disguise toxic expressions. In particular,
Korean allows toxic expressions to be easily
disguised through its agglutinative characteris-
tic. However, obfuscation in Korean remains
largely unexplored, which motivates us to in-
troduce a KOTOX: Korean toxic dataset for
deobfuscation and detoxification. We catego-
rize Korean obfuscation patterns into linguisti-
cally grounded classes and define transforma-
tion rules derived from real-world examples.
Using these rules, we provide paired neutral
and toxic sentences alongside their obfuscated
counterparts. Models trained on our dataset bet-
ter handle obfuscated text without sacrificing
performance on non-obfuscated text. This is
the first dataset that simultaneously supports
deobfuscation and detoxification for the Ko-
rean language. We expect it to facilitate bet-
ter understanding and mitigation of obfuscated
toxic content in LLM for Korean. Our code and
data are available at https://github.com/
leeyejin1231/KOTOX.
1
Introduction
Throughout human history, toxic expressions have
consistently appeared in communication, and de-
tecting such expressions has long been recog-
nized as an ethically significant challenge. With
the advent of Language Models (LM), research
has shifted from traditional rule-based methods to
LM-driven approaches that leverage their language
comprehension abilities to detect toxic text (Kim
et al., 2024; Ahn et al., 2024; Kim et al., 2023; Lee
et al., 2025; Hartvigsen et al., 2022a). Recently,
*Corresponding author.
Figure 1: Comparison of obfuscated toxic text detection
results before and after fine-tuning on KOTOX.
researchers have increasingly focused on detoxi-
fication, which rewrites toxic text into non-toxic
alternatives (Huimin et al., 2025; Ko et al., 2025;
Tang et al., 2023).
Meanwhile, users intentionally obfuscate toxic
expressions to evade automatic moderation sys-
tems. Such obfuscation modifies surface forms
while preserving the original intent, which compli-
cates reliable detection. Several studies investigate
this challenge by evaluating model robustness to
textual perturbation in toxicity detection. Works
such as Xiao et al. (2024a) and Röttger et al. (2021)
show that minor typographical or orthographic al-
terations can severely degrade toxicity detection
performance of models, revealing vulnerabilities of
language models to obfuscated inputs. These find-
ings indicate that obfuscation poses a substantial
challenge for current toxicity detection models.
Most existing toxicity datasets and benchmarks
focus on non-obfuscated text (ElSherief et al.,
2021; Hartvigsen et al., 2022b). Moreover, existing
obfuscation approaches rely on simple techniques
such as homophone replacement or emoji inser-
tion (Wei et al., 2024; Zhang, 2025; Xiao et al.,
1
arXiv:2510.10961v2  [cs.CL]  9 Jan 2026

--- Page 2 ---

Dataset
Lang.
Toxic
Obfus.
Pair Type
Size
Obfus. Types
SBIC (Sap et al., 2020)
EN
O
X
–
44.0K
–
CADD (Song et al., 2021)
EN
O
X
–
24.5K
–
ToxiGen (Hartvigsen et al., 2022c)
EN
O
X
–
274.2K
–
KOLD (Jeong et al., 2022)
KO
O
X
–
40.4K
–
ParaDetox (Logacheva et al., 2022)
EN
O
X
n ↔t
12.6K
–
K/DA (Jeon et al., 2025)
KO
O
X
n ↔t
7.5K
–
HateCheck (Röttger et al., 2021)
EN
O
O
–
3.7K
PHON
ToxiCloakCN (Xiao et al., 2024a)
ZH
O
O
t ↔t(o)
1.5K
PHON / ICON
KOTOX (Ours)
KO
O
O
n ↔t,
n ↔n(o), t ↔t(o)
6.9K
PHON / ICON / TRANS
/ SYN / PRAG
Table 1: Representative toxic datasets. Obfus. denotes datasets containing obfuscated toxic content. Pair Type
indicates the pairing scheme, where n = neutral, t = toxic, and the (o) marks obfuscated forms. Obfus Types represent
the applied obfuscation approaches: phonological, iconological, transliteration-based, syntactic, and pragmatic.
2024b). In addition, existing resources do not pro-
vide jointly aligned toxic content with its obfus-
cated variants, which makes unified experimenta-
tion difficult.
In particular, Korean is an agglutinative language
with flexible spacing and rich morphological varia-
tion (Sohn, 1999; Taylor and Taylor, 2014) which
allows surface forms to change without disrupting
meaning. Its writing system further enables obfus-
cation through phonological variation and visual
similarity that remain easily interpretable to na-
tive speakers. These linguistic characteristics lead
to diverse and systematic, obfuscation patterns in
real-world usage. Despite this, obfuscation in Ko-
rean toxic text remains relatively underexplored in
existing research.
In response to these limitations, we introduce
KOTOX, a Korean Toxic dataset designed for deob-
fuscation and detoxification. We organize Korean
obfuscation into linguistically grounded classes,
and define transformation rules derived from real-
world instances. By using these rules, we provide
paired neutral and toxic sentences along with their
obfuscated counterparts, which allows models to
learn both text recovery and toxic rewriting.
We support three evaluation tasks: (i) Obfuscated
Toxic Text Classification, (ii) Neutral Text Deob-
fuscation, and (iii) Obfuscated Toxic Text Sani-
tization. We evaluate these tasks using multiple
toxicity classifiers and large language models un-
der zero-shot, few-shot, and fine-tuning settings.
The results show that training with KOTOX im-
proves robustness to obfuscated toxic text while
preserving performance on non-obfuscated inputs.
To the best of our knowledge, KOTOX is the first
high-quality paired dataset of obfuscated Korean
toxic text. We expect KOTOX to facilitate a deeper
analysis of obfuscated toxic content in Korean.
2
Related Works
2.1
Toxicity Classification
Early studies on toxic text classification pri-
marily employed lexical or keyword-based ap-
proaches (Waseem et al., 2017; Ocampo et al.,
2023). The development of deep learning acceler-
ated the creation of various toxic datasets for model
training. Representative datasets such as SBIC (Sap
et al., 2020) and ToxiGen (Hartvigsen et al., 2022c)
cover a wide spectrum of abusive, hateful, and bi-
ased texts collected from social media. For toxicity
classification, previous research explored encoder-
based fine-tuning approaches (Caselli et al., 2021;
Liu et al., 2019; Wan et al., 2022), as well as con-
trastive learning methods (Kim et al., 2022; Ahn
et al., 2024).
2.2
Detoxification
Unlike classification, detoxification requires rewrit-
ing toxic text into a neutral counterpart while pre-
serving its semantic content. Motivated by the need,
paired corpora such as ParaDetox (Logacheva et al.,
2022) and K/DA (Jeon et al., 2025) provide paral-
lel toxic-neutral sentences for model supervision.
Meanwhile, these paired corpora are utilized to
train models that rewrite toxic language into neu-
tral forms, or to suppress toxic content generation
during decoding (Ko et al., 2025).
2.3
Obfuscated Toxicity
In recent years, researchers recognized the need
to evaluate model robustness against intrinsically
complex or intentionally obfuscated toxic language.
2

--- Page 3 ---

Online
data
Define Obfuscation 
Taxonomy
Korean experts
Sec. 3.2
Human Experts Filtering
· Interpretability
· Semanticity
· Mislabeling
· Personal information
Sec. 4.1
Filtered Dataset
2.3k
Phonological
Iconological
Transliteration
Syntactic
Pragmatic
Transformation Rules
Taxonomy
Dataset Construction
Rule Construction
KOTOX
K/DA Dataset 
7.5k
...
...
...
...
...
...
6.8k
Make Rules
Rule Application
Initial consonant replacement
Medial vowel replacement
Final consonant replacement
Orthographic resyllabification
Sec. 4.2
...
{
, 
} pairs
Neutral Toxic
idx 0
idx 1
idx 2
idx 0
idx 1
idx 2
idx 0
{
, 
} pairs
Neutral Toxic
{
,
, 
,
} pairs
Neutral  Obfuscated Neutral
Toxic  Obfuscated Toxic
idx 0
idx 0
idx 2
idx 19
idx 0
idx 0
idx 2
idx 2
idx 2
idx 19
idx 0
idx 0
idx 2
idx 2
Figure 2: Overview of KOTOX construction pipeline. It encompasses the design of transformation rules, source
corpus filtering of neutral-toxic pairs, and the generation of quadrupled obfuscated variants for each sample.
Within this line of work, several studies focused on
obfuscation-based robustness. HateCheck (Röttger
et al., 2021) employed leetspeak or orthographic
perturbations to challenge toxic detection models,
while ToxiCloakCN (Xiao et al., 2024a) showed
that homophone and emoji substitutions in Chinese
substantially degrade model performance. Together,
these findings indicate that even surface-level ob-
fuscation can effectively undermine both toxicity
detection and detoxification systems.
2.4
Limitations of Previous Works
Existing toxic datasets exhibit two key limitations.
First, they address either non-obfuscated toxic texts
for detoxification or obfuscated toxic texts for de-
tection in isolation, leaving no dataset that jointly
captures both toxicity and obfuscation. Second,
they mainly target narrow surface changes (e.g.,
homophones, or emojis substitutions), yielding lim-
ited variety. These limitations highlight the need for
a paired, obfuscation-aware dataset that includes
both neutral and toxic texts along with their ob-
fuscated counterparts. Such a resource enables in-
tegrated evaluation and training on toxicity and
obfuscation within a unified framework.
3
Overview of KOTOX & Tasks
We introduce a KOTOX, a Korean neutral-toxic
pair dataset that includes corresponding obfuscated
counterparts. We extend obfuscation beyond sim-
ple spelling or visual modifications in prior work
by leveraging linguistic properties of Korean and
its writing system, Hangeul. Korean is an aggluti-
native language, and Hangeul is a compositional
script in which a syllable block decomposes into
three parts (e.g., ㅊ+ㅐ+ㄱ→책). This structure
enables fine-grained phonological and iconological
transformations. The resulting pairs constitute a
challenging benchmark for robustness analysis.
3.1
Task Definitions
We define three tasks that jointly address toxicity
and obfuscation, enabled by the KOTOX dataset.
These tasks are more challenging than conventional
settings and can be utilized for evaluating the ro-
bustness of LLMs.
Obfuscated Toxic Text Classification
Given an
obfuscated text, the goal of the task is to classify
whether the given text is toxic or not. This mir-
rors standard toxicity classification but explicitly
evaluates robustness under obfuscation.
Neutral Text Deobfuscation
Given an obfus-
cated neutral text, the goal of the task is to generate
its deobfuscated neutral text. This task is newly
defined in our work and can be regarded as a form
of constrained translation.
Obfuscated Toxic Text Sanitization
Given an
obfuscated toxic text, the goal of the task is to gen-
erate the deobfuscated neutral text that preserves
semantics while removing toxicity. This task com-
bines detoxification and deobfuscation in one step—
the most challenging setting supported in KOTOX.
3

--- Page 4 ---

Category
Rule
Phono-
logical
1. Initial consonant replacement
2. Medial vowel replacement
3. Final consonant replacement
4. Orthographic resyllabification
5. Initial consonant insertion
6. Medial vowel insertion
7. Final consonant insertion
8. Liaison (forward, reverse)
Icono-
logical
9. Hangeul look-alike
10. Cross-script substitution
11. Rotation-based variation
Trans-
literation
12. Phonetic substitution (Latin)
13. Phonetic substitution (CYK)
14. Semantic substitution
Syntactic
15. Spacing perturbation
16. Syllable anagram
Pragmatic
17. Symbol/emoji insertion
Table 2: Transformation rules grouped by category with
rule indices. Details of rules and examples are presented
in Appendix B.
3.2
Class of Korean Obfuscation
Figure 2 illustrates our approach to construct a
Korean obfuscation dataset. We classify obfusca-
tion methods into five categories based on the lin-
guistic taxonomy of Korean. Two Korean experts
analyze 144 real-world obfuscated instances col-
lected from user reviews on platforms (e.g., Agoda,
Google Maps, and Booking.com), and they identify
recurring obfuscation characteristics used by native
speakers. We organize these characteristics into a
structured taxonomy and define 17 transformation
rules accordingly, as summarized in Table 2.
Phonological approach.
We adopt a phonologi-
cal approach that treats phonemes as the smallest
units of sound. Korean exhibits unique phonolog-
ical properties, where small textual changes yield
diverse but phonetically similar sounds. This char-
acteristic enables obfuscation by replacing words
with phonetically close alternatives or by modi-
fying text to match actual pronunciation. We de-
fine 8 rules for this phonological process, and Ap-
pendix B.1 describes these rules in detail.
Iconological approach.
The iconological ap-
proach converts text by leveraging visual similar-
ity. It substitutes characters with visually analo-
gous symbols, numbers, or foreign scripts, such
as Chinese characters. Hangeul, the Korean writ-
ing system, consists of syllabic blocks that can be
decomposed into up to three components. These
transformations preserve readability while intro-
ducing iconological variation. We establish three
rules for this process, detailed in Appendix B.2.
Transliteration-based approach.
This approach
converts text into another language that shares
the same pronunciation. Obfuscation occurs when
Korean pronunciation is transcribed into English
letters or replaced with Chinese characters that
sound identical. Alternatively, obfuscation can be
achieved by translating a Korean word into a
foreign-language synonym and then phonetically
transcribing it into Hangeul. We specify three rules
for this approach, presented in Appendix B.3.
Syntactic approach.
The syntactic approach op-
erates at the word and sentence levels rather than
at the character level. Korean differs from English
due to its agglutinative morphology and grammar-
dependent spacing, which allows deviations to ob-
scure meaning. Korean word recognition relies
on holistic syllabic blocks rather than sequential
phonemes, which enables readers to infer meaning
even when internal character order changes. We
exploit these linguistic characteristics to establish
two transformation rules. The details of the rules
appear in Appendix B.4.
Pragmatic approach.
This process perturbs text
by inserting irrelevant elements, such as symbols or
onomatopoeia. Prior work reports that adding such
elements can evoke positive sentiment, thereby re-
ducing the effectiveness of toxicity detection in
large language models (Röttger et al., 2021). Ap-
pendix B.5 provides details of the rule-based prag-
matic approach.
4
KOTOX Construction
Figure 2 illustrates the overall process of our data
construction. Based on the previously defined rules,
we construct neutral-toxic paired data containing
corresponding obfuscations, enabling three tasks:
obfuscated toxic text classification, neutral text de-
obfuscation, and obfuscated toxic text sanitization.
4.1
Source Dataset Preprocessing
We use the K/DA dataset (Jeon et al., 2025), consist-
ing of Korean neutral-toxic sentence pairs, as the
source corpus for constructing KOTOX dataset. We
4

--- Page 5 ---

Algorithm 1 Neutral-toxic pair obfuscation
Input: Neutral-toxic pair (xn, xt), rule set R,
rewrite rate M = {r : τr}r∈R, apply num-
ber k
Output: Obfuscated pair (xn, xt), applied rules Π
1: Π ←∅
2: for i = 1 to k do
3:
while R ̸= ∅do
4:
r ←SAMPLE(R); τ ←M[r]
5:
yn ←APPLYRULE(xn, r, τ)
6:
yt ←APPLYRULE(xt, r, τ)
7:
if SANITYCHECK(yn, yt, Π, r) then
8:
xn ←yn, xt ←yt
9:
Π ←Π ∪{r}
10:
break;
11:
end if
12:
R −{r}
13:
end while
14: end for
15: return (xn, xt), Π
identify several quality issues within the original
data, including imbalance, misaligned neutrality,
semantic ill-formedness, and ethical concerns such
as the exposure of personal information. For a reli-
able alignment, three Korean natives conducted a
manual filtering process based on a 10-item rubric
covering label fidelity, linguistic validity, and data
distribution integrity. The experts independently re-
viewed 7,555 pairs, achieving a Gwet’s AC1 score
of 0.7408 (p < 0.001), indicating inter-annotator
agreement. This rigorous refinement yielded 2,294
high-quality pairs, ensuring a reliable and balanced
foundation for the KOTOX. The details appear in
Appendix C.1.
4.2
Construct Obfuscation of Text
Using the filtered neutral-toxic pairs, we construct
KOTOX by applying the implemented transforma-
tion rules to each pair. For every source pair, three
augmented pairs are generated by repeating the
rule-application process k ∈{2, 3, 4} times.
As shown in Alg. 1, given a single pair, the
algorithm samples a rule r from the rule set
R and applies it to both the neutral and toxic
sides. If the applied result violates any sanity
check (SANITYCHECK), a new rule is resam-
pled and reapplied until successful modification
is achieved. This mechanism ensures that each pass
introduces a meaningful transformation and avoids
trivial or destructive overlaps among rules.
4.3
Dataset statistics
The dataset follows an 8:1:1 split for training, val-
idation, and testing, resulting in 5,505 training in-
stances, 687 validation instances, and 690 test in-
stances. The details of dataset statistics are pre-
sented in Appendix C.4.
5
Experimental Settings
5.1
Classification
To investigate the detection capability of differ-
ent models, we conduct a toxic text classifica-
tion task. We compare model performance on non-
obfuscated dataset (Toxic) and obfuscated dataset
(Ours) using F1-score to examine their understand-
ing of obfuscated toxic content. For LMs, we per-
form supervised-fine-tuning (SFT) independently
on each dataset and conduct cross-validation across
them. For LLMs, we apply few-shot prompting us-
ing examples from the corresponding datasets.
Classification models.
We use three LMs fine-
tuned on toxic datasets for the classification task,
along with one open-source and one closed-source
LLM. HateBERT1 was fine-tuned on Reddit posts,
offensiveRoBERTa2 (RoBERTa) was fine-tuned
on Kaggle toxic comment challenge dataset, and
toxicity-xlmr-v23 (XLM-R) was fine-tuned on mul-
tilingual corpora covering 15 languages from vari-
ous language families. Qwen2.54 is a strong mul-
tilingual instruction-tuned LLM and GPT-4.1 is a
closed-source LLM representing the proprietary
models.
5.2
Deobfuscation and Sanitization
For the Deobfuscation and Sanitization tasks, we
perform experiments in two settings: LLM prompt-
ing and fine-tuning. The experiments consist of
zero-shot prompting, five-shot prompting, and SFT.
We train the SFT models using LoRA and repeat
each experiment three times for consistency. De-
tailed configurations are provided in Appendix D.
LLMs.
We employ four LLMs selected to ensure
linguistic diversity. The open-source set comprises
Qwen2.5, along with two Korean-focused LLMs,
EXAONE 3.55 and Bllossom6. These three mod-
1GroNLP/hateBERT
2unitary/multilingual-toxic-xlm-roberta
3textdetox/xlmr-large-toxicity-classifier-v2
4Qwen/Qwen2.5-7B-Instruct
5LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct
6MLP-KTLim/llama-3-Korean-Bllossom-8B
5

--- Page 6 ---

Model
Eval
Base
Toxic
Ours Comb.
HateBERT
(LM)
Toxic 36.56 76.69 77.19
78.44
Ours
36.28 65.88 71.65
71.32
∆
0.28
10.81
5.54
7.12
RoBERTa
(LM)
Toxic 33.29 91.86 92.02
92.68
Ours
33.61 69.98 84.97
86.94
∆
-0.32
21.88
7.04
5.74
XLM-R
(LM)
Toxic 79.28 95.06 96.30
96.16
Ours
56.80 53.66 89.57
88.13
∆
22.48 41.40
6.73
8.03
Qwen2.5
(LLM)
Toxic 83.66 79.00 82.32
83.13
Ours
69.01 69.85 70.03
70.32
∆
14.65
9.15
12.29
12.13
GPT-4.1
(LLM)
Toxic 89.47 92.05 90.21
91.80
Ours
78.34 80.93 80.56
80.65
∆
11.13 11.12
9.65
11.15
Table 3: Binary toxicity classification under obfusca-
tion (F1-score (%)). For LMs, the Base setting indicates
no fine-tuning, while for LLMs, it indicates zero-shot
inference. Comb. denotes the combination of Toxic and
Ours, along with the robustness gap ∆=Toxic−Ours.
The best performance and the smallest gap are high-
lighted in bold.
els have comparable parameter sizes and are all
instruction-tuned. We also use GPT-4.1.
Toxicity & similarity metrics.
We report evalu-
ation results using two common metrics for both
deobfuscation and sanitization, and one additional
metric for sanitization. To measure similarity with
the reference text, we use BertScore (Zhang et al.,
2020) and chrF (Popovi´c, 2015). To evaluate the
toxicity of sanitized outputs, we employ Google
Jigsaw’s Perspective API7, which is widely adopted
in detoxification tasks.
6
Experimental Results
6.1
Obfuscated Toxic Text Classification
Table 3 presents the result of the toxic classifica-
tion task. Since none of the three LMs were pre-
trained on Korean data, the performance without
tuning (Base) is considerably low. However, XLM-
R achieves relatively higher performance due to
multilingual pretraining. Models fine-tuned only
on the non-obfuscated toxic dataset (Toxic) shows
substantially lower performance on the obfuscated
7https://perspectiveapi.com/
evaluation set (Ours) than on the Toxic set. This re-
sult indicates that understanding toxic expressions
alone is insufficient for detecting obfuscated toxic
text.
Models trained exclusively on Ours set achieve
higher performance on the Toxic evaluation set than
models trained only on the Toxic set. Moreover, the
performance gap between the Ours and Toxic eval-
uations decrease by up to 34.67%p. Finally, when
the models were trained on both the Toxic and Ours
set (Comb.), the results were comparable to those
obtained when using only our dataset. This con-
firms that our dataset enhances the detection of ob-
fuscated toxic text without degrading performance
on the original toxic data.
For LLMs, both Qwen2.5 and GPT-4.1 show
stronger performance on the Toxic dataset in the
zero-shot (Base) setting than the LM baselines,
while their performance noticeably degrades on
the obfuscated dataset. The five-shot results fur-
ther indicate that few-shot prompting does not con-
sistently improve performance, and the degree of
improvement differs across models and datasets.
GPT-4.1 benefits from few-shot prompting more
reliably than Qwen2.5, which suggests that Korean
obfuscation affects LLMs in different ways. These
findings show that the proposed benchmark cap-
tures differences in obfuscation robustness across
models and reveals variation in their ability to in-
terpret obfuscated Korean text.
6.2
Neutral Text Deobfuscation
Table 4 shows the experimental results for deob-
fuscating obfuscated neutral texts. We conduct ex-
periments under three configurations: zero-shot,
five-shot, and supervised fine-tuning (SFT). In the
zero-shot setting, all models exhibit lower deob-
fuscation performance, even though they are pre-
trained on Korean dataset. In the five-shot setting
yields small improvements in BERTScore across
models. All open-source models achieve their best
performance under the SFT setting.
The chrF score, an n-gram-based metric, in-
creases substantially compared to the zero-shot re-
sults under SFT. The BERTScore, which measures
semantic similarity based on embedding, shows im-
provements of up to 11%p SFT. The closed-source
model GPT achieves the highest overall perfor-
mance. These results suggest that existing LLMs,
which are typically trained on clean and noise-free
text, have limited understanding of obfuscated Ko-
rean text. By contrast, models fine-tuned on our
6

--- Page 7 ---

Setting
Qwen2.5
EXAONE3.5
Bllossom
GPT-4.1
BertScore
chrF
BertScore
chrF
BertScore
chrF
BertScore
chrF
Zero-Shot
65.96
15.31
60.60
7.64
65.09
14.08
83.17
41.77
Five-Shot
68.93
19.40
67.00
14.39
70.02
21.14
87.22
52.62
SFT
77.90
36.32
78.12
34.39
78.05
39.97
-
-
Table 4: Neutral text deobfuscation experiment result. We use three open-source LLMs and one closed LLM. The
table shows the performance on the settings of zero-shot, five-shot, and fine-tuning.
Shots
Qwen2.5
EXAONE3.5
Bllossom
GPT-4.1
Bert.
chrF
Pers.
Bert.
chrF
Pers.
Bert.
chrF
Pers.
Bert.
chrF
Pers.
Zero
62.48
7.30
9.89
58.34
3.47
7.87
58.69
3.91
12.58
73.39
16.48
6.91
Five
65.70
10.11
11.51
63.67
6.87
8.49
66.11
11.03
13.29
76.78
23.07
7.35
SFT
71.03
15.06
4.35
71.17
13.53
6.38
70.92
16.31
4.31
-
-
-
Table 5: Toxic text sanitization experiment result. We use three open source LLMs and one closed LLM. The table
shows the performance on the settings of zero-shot, five-shot, and finetuning. We additionally report the perspective
API toxicity score. Lower values indicate lower toxicity in the Perspective API.
dataset acquire a better understanding of obfusca-
tion patterns, demonstrating improved robustness
and comprehension of obfuscated Korean toxic
texts.
6.3
Obfuscated Toxic Text Sanitization
Figure 5 presents the results of transforming ob-
fuscated toxic texts into deobfuscated neutral texts.
The Sanitization task shows very low performance
in the zero-shot setting, similar to the deobfusca-
tion experiments.
In the five-shot setting shows slight improve-
ments in BERTScore and chrF. However, the Per-
spective API scores increase in the five-shot setting,
where higher values indicate higher toxicity. These
results indicate that models often succeed in deob-
fuscation but fail to mitigate toxic content in the
five-shot setting. Manual inspection of the gener-
ated outputs confirms that models recover surface
forms while retaining toxic meaning in many cases.
These observations suggest that five-shot prompt-
ing does not provide sufficient understanding of
obfuscation for successful sanitization.
The SFT setting achieves the best performance,
consistent with the deobfuscation results. Models
fine-tuned on KOTOX show improved ability to
interpret obfuscated sentences and generate non-
toxic outputs. These results indicate that current
LLMs still have limited understanding of obfus-
cated Korean text, making them highly vulnerable
to obfuscated toxic content. Therefore, our dataset
is essential for building models that are robust to
toxicity and resilient against obfuscated language.
7
Dataset Analysis
7.1
Rule analysis
Figure 3 presents the classification error ratio of
HateBERT fine-tuned on the KOTOX for each ap-
plied rule. The error ratio represents the proportion
of incorrect predictions for each rule. Figure 11
illustrates the correlation among the rules. The
rules exhibit very little correlation with one an-
other, which allows each rule to be interpreted in-
dependently. Rule 15 corresponds to the spacing
perturbation rule and shows the highest error ra-
tio. Although spacing changes do not significantly
affect human understanding of the original mean-
ing, they severely impact LMs because the mod-
els process text at the token level. When token
boundaries are disrupted, model performance be-
comes highly vulnerable. Rule 17, which is sym-
bol/emoji insertion, also causes a high error ratio.
These symbols are unrelated to the textual context
and hinder the model’s ability to detect toxicity.
They can also induce misleadingly positive senti-
ment, thereby threatening the model’s robustness.
In contrast, within the phonological approach, rules
such as 8, which are based on clearly defined pro-
7

--- Page 8 ---

1
2
3
4
5
6
7
8
9 10 11 12 13 14 15 16 17
Rule
0.0
0.1
0.2
0.3
0.4
Error Ratio
Error Ratio per Rule
Figure 3: Error ratio for each rule. HateBERT is trained
and evaluated on the KOTOX datasets. The error ratio
indicates the proportion of misclassified samples among
the data associated with each rule.
S1
S2
S3
Avg.
Qwen
Bert.
95.73
96.04
95.16
95.64
77.90
chrF
82.91
82.89
80.61
82.13
36.32
Table 6: Human deobfuscation evaluation results. S1,
S2, and S3 denote the three Korean native speaker, and
Qwen denotes Qwen2.5 fine-tuned on KOTOX.
nunciation patterns, tend to yield lower error ratios.
This suggests that LMs can more easily capture sys-
tematic phonological transformations than irregular
or noise-like modifications.
7.2
Semantic Preservation
We conduct a human deobfuscation evaluation on
500 sampled KOTOX test set to verify whether sen-
tence meaning remains preserved after applying
transformation rules. Table 6 presents the results
of the human evaluation and Qwen2.5 result fine-
tuned on our dataset. Three native Korean speak-
ers perform the deobfuscation task. Human evalua-
tion achieves BERTScore values that are 17.75%p
higher and chrF scores that are 45.81%p higher
than those of the fine-tuned Qwen2.5 model, and it
shows consistently strong performance in the 90%
range. These results indicate that sentence mean-
ing remains intact even under the application of
many transformation rules. The high level of hu-
man performance indicates that the proposed rules
are practically applicable. The comparison with cur-
rent LLM performance show that existing LLMs
still exhibit limited understanding of obfuscated
Korean text.
Setting
KOTOX
Wild
Bert.
chrF
Bert.
chrF
Zero-Shot
65.96
15.31
63.03
11.36
Five-Shot
68.93
19.40
65.48
14.13
SFT
77.90
36.32
72.30
21.99
Table 7: Wild dataset evaluation with Qwen2.5. In the
five-shot setting, we use examples from KOTOX, and
in the supervised fine-tuning setting, we use Qwen2.5
fine-tuned on KOTOX.
7.3
Evaluation on Wild Data
We examine how models trained on KOTOX per-
form on wild data to evaluate their real-world
generalization. We collect 144 obfuscated review
instances from online platforms such as Agoda,
Google Maps to construct the wild dataset. We
conduct evaluation under zero-shot, five-shot, and
supervised fine-tuning settings, where the five-shot
settings use examples from KOTOX, and the super-
vised fine-tuning setting also fine-tunes Qwen2.5
on KOTOX. Table 7 presents the evaluation results.
The results show slightly lower performance on
the wild dataset than on KOTOX, while overall per-
formance patterns remain similar. This observation
suggests that the wild dataset presents marginally
higher difficulty than our dataset. At the same time,
the consistent performance trends indicate that ap-
plying multiple transformation rules does not in-
troduce excessive or unrealistic difficulty to the
sentences. In the supervised fine-tuning setting,
Qwen2.5 fine-tuned on our dataset outperforms
the non-fine-tuned settings on the wild dataset,
which indicates that training on our dataset helps
the model better understand real-world obfuscated
examples. These findings demonstrate that KOTOX
captures real-world characteristics of Korean on-
line communities.
8
Conclusion
In this paper, we propose KOTOX, a neutral-toxic
paired dataset that includes obfuscated counter-
parts. We categorize obfuscation approaches into
five classes based on Korean linguistic properties
and define the corresponding transformation rules.
By applying these rules, we construct a neutral-
toxic paired dataset in which each instance includes
its corresponding obfuscated counterpart. Using
our dataset, we conduct classification, deobfusca-
tion, and sanitization tasks, demonstrating that the
8

--- Page 9 ---

dataset effectively facilitates these tasks. As far
as we are aware, this is the first obfuscation and
detoxification dataset in Korean, and we expect it
will contribute to further research on improving the
understanding of Korean obfuscation.
Limitations
Our study focuses exclusively on the Korean lan-
guage and Hangeul. This design choice can be con-
sidered as both a limitation and a strength. KO-
TOX and its transformation rules may not directly
generalize to other linguistic or cultural contexts.
However, Korean presents unique phonological and
orthographic characteristics that make obfuscation
phenomena particularly rich and distinctive. Our
dataset and analysis are therefore deliberately tai-
lored to explore these language-specific traits in
depth, providing insights that would be lost in a
broad multilingual setting. In future work, we plan
to extend the obfuscation taxonomy and data con-
struction framework to other languages.
Ethical Considerations
Our work involves the collection and analysis of
toxic and offensive language, which inherently
raises ethical concerns. All toxic samples used in
KOTOX originate from publicly available sources,
and sensitive or personally identifiable information
was carefully removed during data filtering by fol-
lowing the rubrics in Table 17 in Appendix. 4.1.
While our dataset includes harmful expressions
for research purposes, it is intended solely for aca-
demic use in developing safer and more robust
language technologies. We strongly discourage any
misuse of KOTOX or its contents for generating,
amplifying, or spreading offensive material.
References
Hyeseon Ahn, Youngwook Kim, Jungin Kim, and Yo-
Sub Han. 2024. Sharedcon: Implicit hate speech
detection using shared semantics. In Findings of
the Association for Computational Linguistics, ACL,
pages 10444–10455.
Tommaso Caselli, Valerio Basile, Jelena Mitrovi´c, and
Michael Granitzer. 2021. Hatebert: Retraining bert
for abusive language detection in english. In Proceed-
ings of the 12th Language Resources and Evaluation
Conference, pages 2786–2794, Marseille, France. Eu-
ropean Language Resources Association.
Mai ElSherief, Caleb Ziems, David Muchlinski, Vaish-
navi Anupindi, Jordyn Seybolt, Munmun De Choud-
hury, and Diyi Yang. 2021. Latent hatred: A bench-
mark for understanding implicit hate speech. arXiv
preprint arXiv:2109.05322.
Thomas Hartvigsen, Saadia Gabriel, Hamid Palangi,
Maarten Sap, Dipankar Ray, and Ece Kamar. 2022a.
Toxigen: A large-scale machine-generated dataset
for adversarial and implicit hate speech detection.
In Proceedings of the 60th Annual Meeting of the
Association for Computational Linguistics (Volume
1: Long Papers), ACL, pages 3309–3326.
Thomas Hartvigsen, Saadia Gabriel, Hamid Palangi,
Maarten Sap, Dipankar Ray, and Ece Kamar. 2022b.
Toxigen: A large-scale machine-generated dataset for
adversarial and implicit hate speech detection. arXiv
preprint arXiv:2203.09509.
Thomas Hartvigsen, Saadia Gabriel, Hamid Palangi,
Maarten Sap, Dipankar Ray, and Ece Kamar. 2022c.
Toxigen: A large-scale machine-generated dataset
for implicit and adversarial hate speech detection.
In Proceedings of the 60th Annual Meeting of the
Association for Computational Linguistics (Volume
1: Long Papers), pages 2367–2388, Dublin, Ireland.
Association for Computational Linguistics.
LU Huimin, Masaru Isonuma, Junichiro Mori, and
Ichiro Sakata. 2025. Unidetox: Universal detoxifica-
tion of large language models via dataset distillation.
In The Thirteenth International Conference on Learn-
ing Representations.
Minkyeong Jeon, Hyemin Jeong, Yerang Kim, Jiyoung
Kim, Jae Hyeon Cho, and Byung-Jun Lee. 2025.
K/DA: Automated data generation pipeline for detox-
ifying implicitly offensive language in Korean. In
Proceedings of the 63rd Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 21404–21432. Association for
Computational Linguistics.
Younghoon Jeong, Juhyun Oh, Jongwon Lee, Jaimeen
Ahn, Jihyung Moon, Sungjoon Park, and Alice Oh.
2022. KOLD: Korean offensive language dataset.
In Proceedings of the 2022 Conference on Empiri-
cal Methods in Natural Language Processing, pages
10818–10833.
Jaehoon Kim, Seungwan Jin, Sohyun Park, Someen
Park, and Kyungsik Han. 2024. Label-aware hard
negative sampling strategies with momentum con-
trastive learning for implicit hate speech detection.
In Findings of the Association for Computational
Linguistics, ACL, pages 16177–16188.
Youngwook Kim, Shinwoo Park, and Yo-Sub Han. 2022.
Generalizable implicit hate speech detection using
contrastive learning. In Proceedings of the 29th Inter-
national Conference on Computational Linguistics,
COLING, pages 6667–6679.
Youngwook Kim, Shinwoo Park, Youngsoo Namgoong,
and Yo-Sub Han. 2023. Conprompt: Pre-training
a language model with machine-generated data for
implicit hate speech detection. In Findings of the
9

--- Page 10 ---

Association for Computational Linguistics: EMNLP,
pages 10964–10980.
Ching-Yun Ko, Pin-Yu Chen, Payel Das, Youssef
Mroueh, Soham Dan, Georgios Kollias, Subhajit
Chaudhury, Tejaswini Pedapati, and Luca Daniel.
2025. Large language models can become strong
self-detoxifiers. In Proceedings of the 2025 Interna-
tional Conference on Learning Representations.
Yejin Lee, Joonghyuk Hahn, Hyeseon Ahn, and Yo-Sub
Han. 2025. AmpleHate: Amplifying the attention
for versatile implicit hate detection. In Proceedings
of the 2025 Conference on Empirical Methods in
Natural Language Processing, pages 28862–28874.
Ping Liu, Varada Kolhatkar, and Joel Tetreault. 2019.
Offenseval: Identifying and categorizing offensive
language in social media.
In Proceedings of the
13th International Workshop on Semantic Evalua-
tion, pages 86–94, Minneapolis, Minnesota, USA.
Association for Computational Linguistics.
Varvara Logacheva, Daryna Dementieva, Sergey
Ustyantsev, Daniil Moskovskiy, David Dale, Irina
Krotova, Nikita Semenov, and Alexander Panchenko.
2022. Paradetox: Detoxification with parallel data.
In Proceedings of the 60th Annual Meeting of the
Association for Computational Linguistics (Volume
1: Long Papers), pages 6804–6818, Dublin, Ireland.
Association for Computational Linguistics.
Nicolás Benjamín Ocampo, Ekaterina Sviridova, Elena
Cabrio, and Serena Villata. 2023. An in-depth analy-
sis of implicit and subtle hate speech messages. In
Proceedings of the 17th Conference of the European
Chapter of the Association for Computational Lin-
guistics, EACL, pages 1989–2005.
Maja Popovi´c. 2015. chrf: character n-gram f-score
for automatic mt evaluation. In Proceedings of the
Tenth Workshop on Statistical Machine Translation,
pages 392–395, Lisbon, Portugal. Association for
Computational Linguistics.
Paul Röttger, Bertie Vidgen, Dong Nguyen, Zeerak
Waseem, Helen Margetts, and Janet Pierrehumbert.
2021. Hatecheck: Functional tests for hate speech
detection models. In Proceedings of the 59th Annual
Meeting of the Association for Computational Lin-
guistics and the 11th International Joint Conference
on Natural Language Processing (Volume 1: Long
Papers), pages 41–58. Association for Computational
Linguistics.
Maarten Sap, Saadia Gabriel, Lianhui Qin, Dan Juraf-
sky, Noah A. Smith, and Yejin Choi. 2020. Social
bias frames: Reasoning about social and power im-
plications of language. In Proceedings of the 58th
Annual Meeting of the Association for Computational
Linguistics, pages 5477–5490, Online.
Ho Sohn. 1999. Min. 1999. the korean language. Cam-
bridge: Cambridge UP.
Hoyun Song, Soo Hyun Ryu, Huije Lee, and Jong Park.
2021. A large-scale comprehensive abusiveness de-
tection dataset with multifaceted labels from reddit.
In Proceedings of the 25th Conference on Computa-
tional Natural Language Learning, pages 552–561,
Online. Association for Computational Linguistics.
Zecheng Tang, Keyan Zhou, Juntao Li, Yuyang Ding,
Pinzheng Wang, Bowen Yan, Rejie Hua, and Min
Zhang. 2023.
Cmd: a framework for context-
aware model self-detoxification.
arXiv preprint
arXiv:2308.08295.
Insup Taylor and M Martin Taylor. 2014. Writing and
literacy in chinese, korean and japanese.
Zhen Wan, Yuan Ding, Shuai Jiang, Xiaoyu Huang, and
Qianqian Xie. 2022. Toxicity detection across lan-
guages with xlm-r and fine-tuning strategies. In Pro-
ceedings of the 8th Workshop on Online Abuse and
Harms (WOAH), pages 1–10, Seattle, Washington.
Association for Computational Linguistics.
Zeerak Waseem, Thomas Davidson, Dana Warmsley,
and Ingmar Weber. 2017. Understanding abuse: A
typology of abusive language detection subtasks. In
ALW@ACL, pages 78–84. Association for Computa-
tional Linguistics.
Zhipeng Wei, Yuqi Liu, and N Benjamin Erich-
son. 2024.
Emoji attack: Enhancing jailbreak at-
tacks against judge llm detection. arXiv preprint
arXiv:2411.01077.
Yunze Xiao, Yujia Hu, Kenny Tsu Wei Choo, and Roy
Ka-wei Lee. 2024a. Evaluating robustness of offen-
sive language detection in chinese: The toxicloakcn
dataset. In Proceedings of the 2024 Conference on
Empirical Methods in Natural Language Processing.
Association for Computational Linguistics.
Yunze Xiao, Yujia Hu, Kenny Tsu Wei Choo, and
Roy Ka-wei Lee. 2024b. Toxicloakcn: Evaluating
robustness of offensive language detection in chi-
nese with cloaking perturbations.
arXiv preprint
arXiv:2406.12223.
Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q.
Weinberger, and Yoav Artzi. 2020. Bertscore: Eval-
uating text generation with bert. In International
Conference on Learning Representations (ICLR).
Yangshijie
Zhang.
2025.
Emoti-attack:
Zero-
perturbation adversarial attacks on nlp systems via
emoji sequences. arXiv preprint arXiv:2502.17392.
10

--- Page 11 ---

Class
Mapped Feature (Appx)
Type
Phonological
Combinatorial Syllabary (§A.2.1)
Korean
Iconological
Visual Decomposability (§A.3.1)
Hangeul
Transliteration-based
Multiscript Familiarity (§A.2.2)
Korean
Syntactic
Syllable-Oriented Segmentation (§A.3.2)
Hangeul
Pragmatic
—
Language-agnostic
Table 8: Obfuscation classes and their enabling properties. Features are detailed in Appendix (§A.2, §A.3).
A
Preliminary
A.1
Korean Language & Hangeul
Korean is an agglutinative and morphologically
rich language in which grammatical relations are
expressed through affixes and particles. Its writing
system, Hangeul, is a compositional and featural
phonemic script: each syllable block is formed by
combining an initial consonant, a medial vowel,
and an optional final consonant (e.g., ㅊ+ㅐ+ㄱ→
책). This block-based structure allows fine-grained
phonological and visual variations, making Korean
particularly suitable for studying diverse obfusca-
tion phenomena.
As shown in Table 8, the proposed obfuscation
classes exploit inherent linguistic and orthographic
properties of Korean and Hangeul. The composi-
tional structure of syllables, visual regularity of
graphemes, and multilingual familiarity shared by
Korean users collectively enable diverse and con-
trollable transformation strategies. These character-
istics make Korean particularly suitable for study-
ing systematic and fine-grained text obfuscation.
A.2
Korean Language-Specific Properties
A.2.1
Combinatorial syllabic phonology.
Korean phonology is organized around syllabic
units by the combination of initial consonant, me-
dial vowel, and final consonant. This block-based
composition induces dense neighborhoods of near-
homophones at the syllable level, further enriched
by the lenis–aspirated–tense triplets (e.g., ㄱ/ㅋ/ㄲ,
ㄷ/ㅌ/ㄸ) and pervasive liaison/coarticulation phe-
nomena. As a result, preserving the global “sound
impression” while altering one or more sub-
syllabic elements is structurally easy and perceptu-
ally tolerable for human readers. These properties
systematically increase the search space for sound-
preserving edits (replacement, addition) without
severely degrading legibility, which directly en-
ables phonological obfuscation.
A.2.2
Latent multiscript competence.
Due to historical and educational exposure, Korean
users routinely navigate multiple scripts (Hangeul,
basic chinese character, and Latin alphabet), and
are familiar with bidirectional phonetic transcrip-
tion conventions. This latent multiscript compe-
tence supports intuitive cross-script rendering of
Korean words and names, and facilitates obfusca-
tion by swapping to visually or phonetically similar
forms in other scripts (or by re-Hangeulization af-
ter translation). The community-level familiarity
with such code-mixed writing (e.g., signage, names,
media) lowers the cognitive cost of interpret-
ing transliterations, thereby making transliteration-
based obfuscation particularly viable.
A.3
Hangeul Orthographic Properties
A.3.1
Decomposability and visual iconicity.
Hangeul graphemes are explicitly decomposable
into consonants and vowels within a square syllabic
layout. The clear sub-graphemic structure, together
with geometric regularities of the block, affords vi-
sually motivated substitutions at both the character
and consonant levels and rotation-based variants.
Human readers retain robust recognition under such
geometric perturbations due to the script’s iconic
regularity and redundancy, which, in turn, makes
iconological obfuscation effective.
A.3.2
Syllable-oriented segmentation
Hangeul is written in syllabic blocks, and Ko-
rean readers parse strings with strong syllable-
level awareness. Combined with historically vari-
able spacing practices and the grammatical role
of postpositional particles, this yields high toler-
ance to segmentation perturbations and syllable-
level rearrangements: many strings remain human-
recoverable despite spacing noise or local ana-
grams. This property directly supports syntactic
obfuscation that disrupts surface structure while
preserving overall interpretability.
11

--- Page 12 ---

Category
Granularity
Examples
Replacement
Initial consonant
한국인들만알아볼수→한꾹인뜰만알아뽈쑤
Medial vowel
태국→타이국, 강해짐↔강하이짐
Final consonant
낡았습니다→낡앆슾니다, 돈↔돉
Resyllabification
할짓이가↔할찌시가
Insertion
Initial consonant
많이→많휘, 안에→안네
Medial vowel
거품점수줘서→궈퓸졈슈줘숴
Final consonant
호스트→홋스트, 바깥→박깥
Liaison
Forward liaison
들어봐→드러봐, 할아버지→하라버지
Reverse liaison
바보→밥오, 버블→법을
Table 9: Examples of the Phonological Approach. Each rule edits sub-syllabic components of Hangeul while
maintaining intelligibility through phonological alternations.
B
Classes of Obfuscation
B.1
Phonological Approach
The phonological approach exploits the similar-
ity in pronunciation between sounds, modifying
the phonemic components of a syllable while pre-
serving overall phonetic perception. Three types
of edits are applied—replacement, addition, and
liaison—each operating on the sub-syllabic struc-
ture of Hangeul. Deletions are not employed, as
they tend to remove excessive information and
distort readability. Because Korean exhibits sys-
tematic phonological alternations (liaison), these
operations are especially effective for generating
natural yet obfuscated variants. As noted in Ap-
pendix A.2.1, each syllable in Hangeul can be de-
composed into multiple components, which facili-
tates diverse and fine-grained variations.
Replacement.
We replace sub-syllabic units that
share close phonetic features: (i) Initial consonant,
(ii) Medial vowel, and (iii) Final consonant. Each
is substituted with a phonetically similar unit so
that the pronunciation remains recognizable. Ad-
ditionally, (iv) orthographic resyllabification is ap-
plied, where syllables are recomposed according
to common phonological rules to reflect natural
sound shifts. Korean provides rich substitution op-
tions owing to its lenis–aspirated–tense triplets
(e.g., ㄱ/ㅋ/ㄲ) and various semi-vowels and diph-
thongs, which enable fine-grained and diverse re-
placements. As shown in Table 10, representative
phonological substitution dictionaries such as le-
nis–tense and lenis–aspirated mappings form the
basis of these replacement rules.
Lenis→Tense
Lenis→Aspirated
Vowel→Diph.
ㄱ→ㄲ
ㄱ→ㅋ
ㅏ→ㅑ
ㄷ→ㄸ
ㄷ→ㅌ
ㅓ→ㅕ
ㅂ→ㅃ
ㅂ→ㅍ
ㅗ→ㅛ
ㅅ→ㅆ
ㅈ→ㅊ
ㅜ→ㅠ
ㅈ→ㅉ
ㅊ→ㅋ
ㅡ→ㅢ
Table 10: Representative phonological substitution dic-
tionaries used in the Phonological Approach. Each col-
umn denotes a systematic replacement pattern among
consonants or vowels. Diph. refers to the ‘Diphthong’.
Insertion.
Additions insert new phonemes while
retaining the original pronunciation pattern. (i)
Initial consonant insertion: the silent consonant
‘ㅇ’ allows prefixing repeated or weak consonant
sounds without changing syllable integrity. (ii) Me-
dial vowel insertion: Korean vowels include semi-
vowels (e.g., ㅏ→ㅑ, ㅜ→ㅟ) that can be naturally
inserted to create similar but extended sounds. (iii)
Final consonant insertion: since the final consonant
position in Hangeul is optional, a new consonant
can be appended—often drawn from the onset of
the following syllable—to mimic natural articula-
tion.
Liaison.
Liaison refers to the phonological pro-
cess where the final consonant of a syllable is car-
ried over to the initial position of the next. We sim-
ulate this by two variations: (i) forward liaison and
(ii) reverse liaison, which performs the inverse map-
ping to obscure standard pronunciation patterns.
These operations reflect natural pronunciation flow
while introducing subtle orthographic perturbations
that remain intelligible to human readers.
12

--- Page 13 ---

Category
Granularity
Examples
Look-alike
Hangeul
귀엽다→커엽다, 멍멍이→댕댕이
CJK
쭈꾸미↔卒꾸미, 국밥↔弓밥
Latin Scripts
야구↔OF구, 태평↔EH평
Multiscripts or emoji
참치→え占치, 바꾸자→㉳꾸자
Rotation
90° rotation
비버→뜨또, 똥→버0
180° rotation
눈물→룸곡, 아이폰→궆I어ㅇ
Table 11: Examples of the Iconological Approach. Look-alike transformations operate at both the character and
jamo levels, substituting visually similar glyphs across scripts (Hangeul, CJK, Latin, symbols, or emoji). Rotation-
based rules alter glyph orientation (90° or 180°) to generate visually perturbed yet readable text.
B.2
Iconological Approach
The iconological approach leverages the visual de-
composability of Hangeul consonants and the in-
dependence of their graphical forms. As discussed
in Sec. A.3.1, the clear sub-graphemic structure
of Hangeul, together with the geometric regular-
ity of its syllabic blocks, enables visually moti-
vated substitutions at both the character and conso-
nant levels, as well as rotation-based variants. As
illustrated in Table 11, Hangeul allows a variety
of iconographic transformations owing to its syl-
labic block structure and clear geometric regularity.
These transformations are designed to modify the
visual appearance of text while maintaining overall
recognizability to human readers.
Look-alike substitution.
This method substi-
tutes Hangeul characters with visually similar
glyphs. These substitutes can be other Hangeul
characters or visually analogous symbols drawn
from CJK (Chinese, Japanese, Korean) characters,
Latin scripts, or even emojis.
Specifically, these substitutions occur at two dif-
ferent levels of granularity: (i) at the character
level, entire syllable blocks are replaced with visu-
ally similar symbols. This is particularly frequent
among Hangeul variants, emojis, and CJK charac-
ters. Due to their visual complexity, CJK characters
are often effective at mimicking the overall struc-
ture of a complete Hangeul syllable. (ii) at the sub-
syllabic level, individual graphemes (consonants
and vowels) are replaced with shape-correlated
symbols. For instance, the Hangeul letter ‘ㅇ’ can
be replaced by the Latin ‘O’, or ‘ㅑ’ by ‘F’. Be-
cause Hangeul is a featural script where conso-
nants and vowels are combined into blocks, this
sub-syllabic structure allows for highly flexible and
diverse look-alike substitutions.
Han.→Han.
Han.→CJK
Sub-syllabic
귀→커
틎→長
ㄱ↔プ
멍→댕
국→弓
ㄴ↔レ
비→네
흡→音
ㄷ↔て
면→띤
쭈→卒
ㄹ↔己
명→띵
쇼→企
ㅁ↔口
유→윾
슥→今
ㅂ↔せ
우→윽
리→引
ㅅ↔人
점→겸
튼→長
ㅇ↔○
과→파
숲→金
ㅈ↔久
괄→팔
흠→高
ㅊ↔大
관→판
매→叫
ㅋ↔ヲ
대→머
조→丕
ㅌ↔巨
왕→앟
쇼→企
ㅍ↔立
공→끙
몸→呂
ㅎ↔云
Table 12: Representative iconological substitution dic-
tionaries used in the Iconological Approach. Each
column shows systematic visual mappings between (i)
Hangeul–Hangeul replacements, (ii) Hangeul–CJK sub-
stitutions, and (iii) sub-syllabic correspondences. Han.
denotes Hangeul.
Rotation.
Rotation-based obfuscation manipu-
lates the glyph orientation of Hangeul characters.
By rotating syllable blocks or subcomponents by
90◦or 180◦, we produce text that visually resem-
bles the original while disrupting standard ortho-
graphic patterns. Such geometric perturbations pre-
serve readability to humans but often confuse au-
tomatic recognition models. For example, a 90◦
rotation of the Hangeul ‘비’ results in ‘뜨’, cre-
ating a visually similar but semantically different
character.
13

--- Page 14 ---

Category
Granularity
Examples
Phonetic Transliteration
CJK substitution
수상해→水상해, 남한테→男한테
Latin substitution
망했다고→mang했다고, 게시판→gㅔ시판
Semantic Transliteration
English meaning
가지말고같이먹자→돈트고같이먹자
Japanese meaning
자리좀부탁해→자리좀구다사이
Table 13: Examples of the Transliteration-based Approach. Phonetic transliteration replaces parts of Hangeul
words with phonetically similar units in CJK or Latin scripts, while semantic transliteration substitutes words with
phonetic renderings of their foreign-language meanings (e.g., English or Japanese).
B.3
Transliteration-based Approach
As discussed in Sec. A.2.2, Korean users are inher-
ently familiar with multiple writing systems, includ-
ing Hangeul, basic Chinese characters (Hanja), and
the Latin alphabet, due to historical and educational
exposure. This multilingual competence enables
intuitive transliteration-based obfuscation, where
parts of text are replaced with characters or sounds
drawn from other scripts that share phonetic or
semantic associations. Broadly, two strategies are
employed: one exploits phonetic similarity (sound-
based substitution), and the other leverages seman-
tic equivalence (meaning-based substitution).
Phonetic transliteration.
Phonetic translitera-
tion replaces parts of a Korean word with CJK
or Latin characters that share similar pronunciation.
For instance, the Chinese character 水(pronounced
“su”) can substitute the syllable 수in 수상해, re-
sulting in 水상해. Partial substitutions that target
only specific consonants or vowels are also possi-
ble (e.g., 게시판→gㅔ시판). Such CJK or Latin
replacements preserve phonetic resemblance while
introducing script-level variation that hinders auto-
matic recognition.
Semantic transliteration.
Semantic translitera-
tion exploits the meaning of the original phrase
by translating it into a foreign language and then
re-Hangeulizing the phonetic rendering of the trans-
lated words. For example, the Korean verb 부탁해
can be semantically translated into Japanese as く
ださい, and then phoneticized back into Hangeul
as 구다사이. This substitution thus conveys the
same meaning through a cross-lingual phonetic
rendering that remains easily interpretable to Ko-
rean readers. This approach leverages bilingual
familiarity—especially with English and Japanese—
to generate natural yet obfuscated variants easily
interpretable by Korean readers.
LLM-based obfuscation.
Unlike other obfusca-
tion classes, the transliteration-based approach is
difficult to implement in a purely rule-based man-
ner, as it often requires contextual awareness and
semantic substitution rather than simple character
mapping. Among its variants, phonetic translitera-
tion with CJK characters can be handled determin-
istically through predefined rules, whereas Latin-
based and semantic transliteration demand higher-
level reasoning and cross-lingual understanding.
To address this, we employ a lightweight and ef-
ficient language model, GPT-5 nano, to perform
LLM-assisted obfuscation for these cases.
While Hanja (CJK) characters align one-to-one
with Hangeul syllables, Latin script does not ex-
hibit such a direct correspondence, which fre-
quently led to undesirable substitutions that altered
contextually important words. In contrast, semantic
transliteration inherently involves translation into a
foreign language, making LLM utilization not only
beneficial but necessary.
As shown in Figure 4 and Figure 5, we design
carefully crafted prompts to guide the model in
generating contextually appropriate obfuscations.
Unlike the few-shot or zero-shot prompts used for
English tasks, these prompts were written in Ko-
rean to better align with the linguistic characteris-
tics of Hangeul and to encourage the model to re-
flect native Korean phonological and orthographic
nuances.
The robustness of these obfuscation methods,
including both LLM-based and rule-based ap-
proaches, is indirectly validated in Subsection 7.2.
Specifically, the results from the human de-
obfuscation task demonstrate that our obfusca-
tion techniques successfully preserve the original
semantics. This high level of semantic preserva-
tion ensures that the obfuscated text remains inter-
pretable to humans and retains its toxic intent.
14

--- Page 15 ---

Phonetic Transliteration with Latin Scripts
너는음차표기를해주는GPT이다.
문장이주어졌을때, 다음주어진조건을참고해서, 문장의문자들을음차표기로바꿔줘야한다.
### 변형방식카테고리예시
음차방법: 한글-> 영어문자:
특정자음을같은발음을나타내는알파벳으로차용하거나,
특정글자자체를같은발음을내도록영어로표기해야한다.
### 지시사항- 출력형식을지켜야한다.
- 모음이[ㅏ, ㅑ, ㅓ, ㅕ, ㅣ, ㅔ, ㅐ]인경우에만’게시판-> gㅔ시판’같은초성차용이가능하다. 중성종성은차용안됨.
- 핵심적인부분을위주로수정.
- 문장의절반정도의어절을바꿔줘.
- 오직아래의포맷으로만출력한다. 추가설명, 코드블록, 접두· 접미텍스트금지.
### 출력형식
{ "input": "게시판을확인하세요", "output": "gㅔ시판을확in하세yo" }
{ "input": "한놈잡아먹자", "output": "han norm 잡아먹jㅏ" }
{ "input": "부디믿고맡겨주세요", "output": "boo D I MIT. 고맡겨주세yo" }
{ "input": "시험망했다", "output": "Sㅣ험mang했다" }
{ "input": "방이너무더럽다", "output": "bang이너무the love다" }
Phonetic Transliteration with Latin Scripts (English Translation version)
You are a GPT that performs phonetic transliteration.
When a sentence is given, you must convert the characters of the sentence into phonetic transliteration based on the
conditions provided below.
### Transformation Method Category Examples
Phonetic method: Hangeul -> Alphabet:
Borrow specific consonants as alphabet letters that represent similar sounds,
or write certain characters in English so that they produce the same pronunciation.
### Instructions - Follow the required output format.
- Consonant substitution like "게시판-> gㅔ시판" is allowed only when the vowel is one of [ㅏ, ㅑ, ㅓ, ㅕ, ㅣ, ㅔ, ㅐ].
Medial vowels and final consonants cannot be substituted.
- Modify mainly the core parts.
- Change about half of the words in the sentence.
- Output only in the format below. No extra explanations, code blocks, or prefix/suffix text.
### Outpur Format
{ "input": "게시판을확인하세요", "output": "gㅔ시판을확in하세yo" }
{ "input": "한놈잡아먹자", "output": "han norm 잡아먹jㅏ" }
{ "input": "부디믿고맡겨주세요", "output": "boo D I MIT. 고맡겨주세yo" }
{ "input": "시험망했다", "output": "Sㅣ험mang했다" }
{ "input": "방이너무더럽다", "output": "bang이너무the love다" }
Figure 4: The prompt used for phonetic transliteration obfuscation with Latin scripts. It provides the task descriptions
and instructions.
15

--- Page 16 ---

Semantic Transliteration
너는음차표기를해주는GPT이다.
문장이주어졌을때, 다음주어진조건을참고해서, 문장의문자들을음차표기로바꿔줘야한다.
### 변형방식카테고리예시
한국어-> 외국어-> 한글음차:
한국어내용을외국어로번역한뒤, 외국어를한글로발음나는대로적는방법이다.
### 가이드
- 다음과같은흐름으로변형한다.
- 쉬운일본어와영어를활용한다.
- 가지말아주세요-> don’t go ください-> 돈트고쿠다사이
- 아주좋아요-> 아주nice 해요-> 아주나이스해요
### 지시사항
- 핵심적인부분을위주로수정.
- 문장의절반보다더바꾸지말것.
- 불분명한어절은경솔하게수정하지말고내버려둘것.
- 교체된어절은다시출력하지말것.
- 오직아래의포맷으로만출력한다. 추가설명, 코드블록, 접두· 접미텍스트금지.
### 출력형식
{ "input": "오늘은가지말아주세요", "output": "오늘은돈트고쿠다사이" }
{ "input": "싸가지없는모습아주좋아요", "output": "싸가지없는애티튯아주나이스해요" }
{ "input": "침대냄새엄청난대. 히터키면주유소냄새미친건가.", "output": "침대와스메리혼또니데스. 히터키면
주유소스메리와따팤." }
{ "input": "방이너무좁아요.", "output": "룸이즈너무조바요데스네." }
Semantic Transliteration (English Translation version)
You are a GPT that performs semantic transliteration.
When a sentence is given, you must convert parts of the sentence into semantic transliterated forms according to the
conditions below.
### Transformation Method Category Examples
Korean -> Foreign Language -> Hangeul Transliteration:
This method translates Korean into a foreign language and then writes that foreign language into Hangeul based on its
pronunciation.
### Guide
- Transform the text following this sequence.
- Use simple Japanese and English.
- 가지말아주세요-> don’t go ください-> 돈트고쿠다사이
- 아주좋아요-> 아주nice 해요-> 아주나이스해요
### Instructions
- Modify mainly the core parts.
- Do not change more than half of the words in the sentence.
- Do not modify unclear words carelessly. Leave them as is.
- Do not output the replaced original words again.
- Output only in the format below. No extra explanations, code blocks, or prefix/suffix text.
### Output Format
{ "input": "오늘은가지말아주세요", "output": "오늘은돈트고쿠다사이" }
{ "input": "싸가지없는모습아주좋아요", "output": "싸가지없는애티튯아주나이스해요" }
{ "input": "침대냄새엄청난대. 히터키면주유소냄새미친건가.", "output": "침대와스메리혼또니데스. 히터키면
주유소스메리와따팤." }
{ "input": "방이너무좁아요.", "output": "룸이즈너무조바요데스네." }
Figure 5: The prompt used for semantic transliteration obfuscation with various languages. It provides the task
descriptions and instructions.
16

--- Page 17 ---

Category
Language
Examples
Spacing perturbation
Korean
화장실더럽고별로→화장실더럽고별로
English
this place is dirty →thi splace is dir ty
Syllable/word anagram
Korean
오랜만에외국여행을→오만랜에외여국행을
English
happy trip ↔hpapy tirp
Mixed obfuscation
Korean
이번주말에놀러가자→번이말주에놀러자가
English
I wanna go home →Iwnan ago hoem
Table 14: Cross-lingual examples of Syntactic Obfuscation. Spacing and syllable-level rearrangements in Korean
correspond to word or character boundary shifts in English, but Hangeul’s block-based structure allows greater
flexibility while maintaining readability.
Category
Language
Examples
Emoji insertion
Korean
돈을쓰는호갱→돈을°♡쓰는《호..갱》≥ㅅ≤
English
what a fool →what °♡a 《fo..ol》≥ㅅ≤
Table 15: Cross-lingual examples of Pragmatic Obfuscation. Each language employs visually or emotionally
expressive cues—emojis, symbols, or tone markers—to modulate perceived sentiment, often reducing apparent
toxicity while retaining original meaning.
B.4
Syntactic Obfuscation
As noted in Sec. A.3.2, Hangeul is written in syl-
labic blocks and Korean readers parse text with
strong syllable-level awareness. Combined with
historically flexible spacing and the grammatical
role of postpositions, this yields high tolerance to
segmentation noise and local rearrangements. Thus,
surface perturbations that disrupt spacing or sylla-
ble order often remain human-recoverable while
confusing automatic detectors.
Spacing perturbation.
We randomly insert or re-
move spaces at plausible boundaries (e.g., between
syllable blocks or morphemes), preserving word
order while altering the visual segmentation. When
composed with other rules, spacing noise increases
ambiguity without severely degrading readability.
As shown in Table 14, while text remains easily
understandable when only spacing perturbations
are applied, the introduction of syllable-level ana-
grams significantly amplifies the difficulty of de-
obfuscation.
Syllable-level anagram.
We locally reorder syl-
lables within a word/phrase under constraints
that keep the syllable inventory intact and limit
edit distance. Unlike alphabetic scripts (character-
by-character decoding) or logographic scripts
(character-as-morpheme), the block-based unit in
Hangeul often allows such micro-rearrangements
to stay interpretable to human readers.
B.5
Pragmatic Obfuscation
Pragmatic obfuscation is language-agnostic and
alters discourse cues rather than lexical content.
We insert visually salient symbols or emojis near
sentiment-bearing tokens, which can soften per-
ceived polarity or distract pattern-based heuris-
tics, thereby reducing toxicity detection rates while
keeping the underlying proposition intact. Such
modifications exploit the tendency of large lan-
guage models and toxicity classifiers to rely on
surface-level emotional markers rather than deep
semantic understanding.
Irrelevant symbol insertion.
We constrain the
symbol injection rate and avoid splitting inside
syllable blocks or linguistic morphemes. Hearts,
brackets, or emoticons are placed around target
spans to modulate tone (e.g., °♡, 《》, ≥ㅅ≤),
creating a visually disfluent but emotionally soft-
ened expression. These pragmatic cues preserve
human readability and contextual meaning while
significantly degrading the reliability of automatic
toxicity detection, highlighting a unique challenge
in modeling human-like interpretation of style and
intent.
17

--- Page 18 ---

Education Level
Nationality
Comm. Frequency
Comm. Years
Major / Department
Korean Expert
B.S. Candidate
South Korea
Daily
8 Years
Korean Language and
Literature
B.S.
South Korea
Weekly
6 Years
Korean Language and
Literature
Non-Korean Expert Expert (Native Speaker)
Ph.D. Candidate
South Korea
Daily
10 Years
Computer Science
Ph.D. Candidate
South Korea
Daily
12 Years
Computer Science
Ph.D. Candidate
South Korea
Daily
13 Years
Artificial Intelligence
Table 16: Demographic characteristics and community engagement levels of the non-expert and expert validators
involved in the human evaluation process.
Rule
Filtering Reason
Misaligned Neutrality
Neutral text already conveys toxic or sarcastic intent, compro-
mising its role as a non-harmful counterpart.
Slang or Informal Vulgarity
Neutral sample contains slang or mild expletives (e.g., “개–”,
“씨발–”) inappropriate for detoxified text.
Non-standard or Unintelligible
Expression
Text includes invented words, broken grammar, or unintelligi-
ble noise generated by LLMs.
False Neutrality or Label Ambiguity
Toxic text lacks explicit offensiveness or appears indistinguish-
able from neutral tone, making label assignment unreliable.
Masked or Corrupted Text
Presence of masking artifacts (e.g., “**씨”, “욕***”) or pre-
processing errors that corrupt readability.
Personally Identifiable Information
Sentences expose real names, usernames, or identifiable enti-
ties, raising privacy and ethical concerns.
Semantic Ill-formedness
Either side of the pair is semantically incoherent or ungram-
matical, hindering model training.
Duplication / Near-Duplication
Multiple toxic variants are paired with the same neutral sen-
tence, leading to redundancy and imbalance.
Length Insufficiency
Sentences are too short (≤2 tokens) to allow meaningful trans-
formation or obfuscation.
Label Noise (Inverse Pairing)
Neutral and toxic roles are swapped or mislabeled, resulting in
reversed polarity between pairs.
Table 17: Rubrics for filtering K/DA. Each rule specifies a criterion for discarding or retaining pairs to ensure dataset
quality and label consistency.
18

--- Page 19 ---

C
Dataset Construction Details
C.1
Details of Filtering K/DA
To construct our obfuscated Korean toxic text
dataset, we use K/DA (Jeon et al., 2025) as the
primary source. K/DA is a Korean paired dataset
originally developed for the detoxification task,
where neutral sentences were transformed into
toxic counterparts through LLM-based rewriting.
To capture rapidly evolving slang and online ex-
pressions, K/DA first collected toxic text from var-
ious online communities and built a large corpus.
For each neutral sentence, similar toxic samples
were retrieved using a semantic similarity metric
and then provided as examples to an LLM, which
generated corresponding toxic paraphrases.
Despite its scale and utility, K/DA presents sev-
eral quality limitations. A non-negligible number
of cases contain mislabeling, where already-toxic
sentences are annotated as neutral. Some sentences
are syntactically or semantically ill-formed to the
point of being uninterpretable. The dataset also in-
cludes real personal names, posing potential ethical
concerns. Furthermore, a single neutral sentence in
K/DA is often paired with multiple, near-duplicate
toxic variants, resulting in redundancy, lexical im-
balance between neutral and toxic subsets, and sub-
optimal suitability for classification tasks.
To address these issues, we conduct a manual
filtering process. Following the rubric in Table 17,
three native Korean annotators independently re-
viewed all 7,555 neutral–toxic pairs without discus-
sion. If a neutral sentence was deemed problematic,
the entire set of pairs linked to that neutral sample
was removed, whereas if the toxic side alone was
flawed, only the corresponding pair was discarded.
Inter-annotator consistency was evaluated using
Gwet’s AC1 coefficient, which yielded a score of
0.7408 (p < 0.001, z = 125.75, SE = 0.0059).
This value indicates a high level of agreement
among annotators, supporting the reliability of the
filtering decisions.
After filtering, only the 5,160 pairs marked as
valid by all annotators were retained. We further ex-
clude extremely short sentences consisting of two
tokens or fewer, as they offered limited opportunity
for meaningful obfuscation. In cases where multi-
ple toxic variants were associated with the same
neutral sentence, a single toxic example was ran-
domly selected. The resulting corpus comprises
2,294 high-quality neutral–toxic pairs, which
serve as the foundation for our obfuscated dataset.
Rule
Rewrite Rate
Initial consonant replacement
0.5
Medial vowel replacement
0.3
Final consonant replacement
0.5
Orthographic resyllabification
0.5
Initial consonant insertion
0.3
Medial vowel insertion
0.5
Final consonant insertion
0.5
Liaison (Forward & Reverse)
0.3
Hangeul look-alike
0.3
Cross-script substitution
0.5
Rotation-based variation
0.3
Phonetic substitution (CYK)
0.3
Phonetic substitution (Latin)
0.5
Semantic substitution
0.5
Spacing perturbation
0.5
Syllable anagram
0.3
Symbol/emoji insertion
0.5
Table 18: Per-rule rewrite rates used in dataset construc-
tion. Rates represent the fraction of tokens targeted for
modification within each sentence.
C.2
Dataset Construction Environment
We utilize several libraries for data generation, in-
cluding hgtk 0.2.1, six 1.17.0, openai 1.109.1, jamo
0.4.1, KoNLPy 0.6.0, and KoG2Padvanced8.
C.3
Hyperparameters for Dataset
Construction
During dataset construction, each neutral-toxic pair
from K/DA was processed through the obfuscation
procedure described in Alg. 1. For each pair, a set
of transformation rules was applied up to k times.
Since the scope of application differs across rules—
some can be applied to nearly every token, while
others only affect limited contexts—we control the
overall rewrite intensity using a global rewrite rate.
Specifically, the rate was set to 0.5 or 0.3 of the
total number of tokens in a sentence, depending on
rule coverage. The detailed per-rule rewrite rates
used for all 17 rules are summarized in Table 18.
8https://github.com/seongmin-mun/
KoG2Padvanced.git
19

--- Page 20 ---

Difficulty
# Samples
# Applied Rules
# Rule Combinations
# Total Rules
Avg. # Span
Easy
2,294
2
197
17
7.94
Normal
2,294
3
1,254
17
8.14
Hard
2,294
4
2,079
17
8.20
Total
6,882
2-4
3,530
17
8.09
Table 19: Statistics of the KOTOX dataset by difficulty level. Each level is defined by the number of applied
transformation rules per pair. A total of 6,882 samples were generated and evenly distributed across three difficulty
levels.
C.4
Dataset Statistics
Statistic highlights the key strengths of KOTOX
compared to existing toxic datasets. Previous
datasets lack a sufficient volume of obfuscated
samples or fail to provide direct pairs of origi-
nal and obfuscated text. In contrast, our dataset
goes beyond simple neutral-toxic pairs by provid-
ing aligned obfuscated versions for each sentence.
Furthermore, we distinguish our work by applying
diverse obfuscation methods across five major cat-
egories, ensuring both the breadth and depth of the
benchmarks required to evaluate model robustness
against evolving toxic expressions.
Table 19 summarizes the statistics of the final
KOTOX dataset generated through the aforemen-
tioned obfuscation process. The dataset contains a
total of 6,882 neutral–toxic pairs, evenly divided
into three difficulty levels according to the num-
ber of applied rules per sentence. Easy, Normal,
and Hard subsets of KOTOX are constructed by ap-
plying two, three, and four random transformation
rules to each sample, respectively. Table 20, 21,
22 further provide qualitative examples illustrat-
ing how different rule combinations are reflected
across difficulty levels.
As illustrated in Figure 6, the applied rules ex-
hibit a non-uniform distribution across the datasets,
which results from differences in the text spans
each rule covers. A large proportion of the applied
rules belong to the Phonological approach (rule
1-8). This is because, unlike other rules that require
specific character-level conditions, phonological
transformations can be applied more freely at the
phoneme level.
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
Rule
0
250
500
750
1000
1250
1500
1750
2000
Count
Obfuscated Rule Frequency
Figure 6: Distribution of obfuscated Rule frequencies
in total dataset.
D
Experimental Details
D.1
Details of LMs used for Classification
We use three transformer-based language models
fine-tuned on toxic or offensive text corpora for
toxicity classification.
HateBERT
HateBERT (Caselli et al., 2021) is
a BERT model further pre-trained on Reddit posts
containing abusive and offensive language. It is
optimized for English toxic comment detection and
serves as a strong domain-adapted baseline.
Multilingual-Toxic-XLM-RoBERTa
This
model is based on XLM-RoBERTa and fine-tuned
on multilingual toxic datasets covering 15 lan-
guages. It enables cross-lingual toxicity detection
and serves as our multilingual baseline.
Toxicity-XLMR-v2
Toxicity-XLMR-v2 is a
large XLM-RoBERTa model fine-tuned on diverse
multilingual corpora for toxicity classification. It
provides strong generalization across languages
and complements the English-centric HateBERT.
20

--- Page 21 ---

Type
Example
Label
Neutral (Original)
출산율증가를위해새로운정책이나왔으면좋겠어
[5, 10]
Neutral (Obfuscated)
출산율증가를위ㅇЙ 새로운정ㅊЙㄱ나왔으면좋겠어
Toxic (Original)
출산율증가를위해애낳는머신들한테새로운당근을줬으면좋겠네ㅋㅋ
Toxic (Obfuscated)
출산율증가를위해애ㄴとㄴ는ㅁ†신ㄸ一ㄹŁㄴㅌㅓㅣ새로운당ㄱ一늘줬으면좋겠네ㅋㅋ
Neutral (Original)
아니야ㅋㅋ원동기면허있어야타ㅠㅠ
[16, 6]
Neutral (Obfuscated)
와뉘야ㅋㅋ원기동면허있어야톼ㅠㅠ
Toxic (Original)
아니야ㅋㅋ머가리없는놈들은원동기면허도없이타고다니더라ㅉㅉ
Toxic (Obfuscated)
아야니ㅋㅋ며갸뤼웞늰놈들은원동기면혀됴없이탸교다더니라ㅉㅉ
Neutral (Original)
그러니까등산은직접가는거지
[4, 13]
Neutral (Obfuscated)
그러니까등사는직쩝家는거지
Toxic (Original)
등산은직접가보면알겠지만, 체력딸리는찐따들은산에서죽을수도있어
Toxic (Obfuscated)
등사는직쩝가보면알겠지만, 체력딸리는찐따들恩山에서주글수도이써
Table 20: Easy examples of KOTOX.
Type
Example
Label
Neutral (Original)
오늘처음학교가는날인데
[11, 14, 12]
Neutral (Obfuscated)
오늘first 타임스쿨ㅓㄴ는day인데
Toxic (Original)
오늘처음학교가는날인데찐따들이랑어울려야한다니암걸려
Toxic (Obfuscated)
투데이cheum haekgyo onneun 날인데OTAKU들이랑aO울려야한다니cancer걸려
Neutral (Original)
잠안오는그런거있니?
[5, 1, 17]
Neutral (Obfuscated)
짬♡안♡【요늰】그런「♥」커윘뉘?
Toxic (Original)
잠안와서뒤척이는거진짜빡치는데ㅋㅋ
Toxic (Obfuscated)
참〃얀〃∥와써∥뒤척이는♡【거】♥쮠쨔빡치는데ㅋ‥ㅋ
Neutral (Original)
언니언제엄마밥먹었었어?
[7, 3, 15]
Neutral (Obfuscated)
언니얺제엄마밥먹겆엊어?
Toxic (Original)
언니언제아줌마밥쳐먹었었냐?
Toxic (Obfuscated)
언니언제아줌마밮쳐멐것엍냐?
Table 21: Normal examples of KOTOX.
Type
Example
Label
Neutral (Original)
아근데일쌓이면스트레스받아ㅋㅋ
[1, 13, 9, 8]
Neutral (Obfuscated)
㈕근데一싸히면스트레스팓아
Toxic (Original)
일쌓이면존나열받아서뒤질것같음ㅋㅋ
Toxic (Obfuscated)
일쌓二면존나열㉳㉰서뛰칠것깥음
Neutral (Original)
거기강아지카페도붙어있더라
[1, 5, 14, 4]
Neutral (Obfuscated)
데스네쾅와취카페도퓬녀이썩꾸나데스네
Toxic (Original)
거기개돼지들모여서시끄럽게짖어대는곳도붙어있더라
Toxic (Obfuscated)
데스코도그피그들묘여쒀씨끄럽케쥐줘대닌콛또스테이클로즈윋뗘랴
Neutral (Original)
어떤기술인지정말궁금하다
[11, 6, 4, 12]
Neutral (Obfuscated)
얻떤gㅣ수린지rㅓally guㅁ금하ㅓコ
Toxic (Original)
어떤기술인지정말궁금한데, 깜냥이딸리는한남충들은이해못할듯
Toxic (Obfuscated)
엇떤gㅣt쑤린지really 궁금한데, 깜냥임tails는쿠우남충들은잉애mortal 듯
Table 22: Hard examples of KOTOX.
21

--- Page 22 ---

D.2
Details of LLMs Used for Deobfuscation
and Sanitization
All models used in our experiments are instruction-
tuned large language models (LLMs).
Qwen2.5
Qwen2.5 is a multilingual causal LLM
by Alibaba with significantly improved Korean ca-
pability over its predecessors. Although version
3 is available, we use 2.5 since the newer “think-
ing” mode often produces overly verbose outputs
unsuitable for our tasks.
Exaone 3.5
Exaone 3.5, developed by LG AI
Research, is a Korean-specialized LLM. We adopt
version 3.5 instead of 4.0 to avoid verbosity issues
from the new “thinking” control while maintaining
strong linguistic quality and response stability.
LLaMA-3-Korean-Bllossom
LLaMA-3-
Korean-Bllossom
extends
Meta’s
LLaMA-3
through continued Korean pretraining and instruc-
tion tuning. It serves as an open-source alternative
emphasizing fluency and consistency in Korean
generation.
GPT-4.1
GPT-4.1 is OpenAI’s closed-source
frontier LLM, representing one of the most capa-
ble general-purpose models currently available. It
serves as a strong closed-source baseline for deob-
fuscation and sanitization tasks.
D.3
Details of Metrics
Accuracy
Accuracy measures the proportion of
correctly predicted samples. However, in balanced
binary classification tasks, a trivial model that al-
ways predicts a single class can easily achieve 50%
accuracy. Therefore, it is often reported together
with F1-score for a more reliable assessment.
F1-score
F1-score is the harmonic mean of Pre-
cision and Recall. In binary or imbalanced clas-
sification tasks, F1-score is widely preferred over
accuracy since it better captures the balance be-
tween false positives and false negatives. We treat
the harmful class as the positive label when com-
puting F1-score, which is a common convention in
hate speech detection studies.
BERTScore
Since our dataset is in Korean, we
employ the multilingual BERT-based implementa-
tion of BERTScore following the default configu-
ration of the official library. This allows semantic
similarity to be computed across diverse linguistic
variations.
chrF
Korean exhibits agglutinative morphology,
where particles and affixes are attached to word
stems. As a result, token-level n-gram metrics such
as BLEU or ROUGE may underestimate similarity.
We therefore report character-level matching scores
using chrF, which better captures morphological
overlap.
Perspective API
We additionally use Google’s
Perspective API to estimate toxicity scores of gen-
erated sentences. This tool is widely adopted in
toxicity and hate-speech detection research for pro-
viding a standardized toxicity estimation.
D.4
Experimental Environments
We conduct training and inference on Ryzen 9950x
and Threadripper 9960X CPUs, and NVIDIA
RTX Pro 6000 GPUs. The experiments were per-
formed on Rochy Linux 9.6 using PyTorch 2.8.0,
Transformers 4.56.2, BitsAndBytes 0.48.0, Ker-
nels 0.10.2, PEFT 0.17.1, Scikit-learn 1.7.2, Easy-
Dict 1.13, Pandas 2.3.3, Accelerate 1.10.1. For
evaluation metrics, we additionally use Evaluate
0.4.6, SacreBLEU 2.5.1, BERTScore 0.3.13, Ope-
nAI 1.109.1.
D.5
Hyperparameters for Fine-tuning
Classification.
We fine-tune the LM using su-
pervised learning for the classification task. The
fine-tuning process employed a dropout rate of 0.1,
with hyperparameters set as follows: 15 epochs, a
batch size of 16, a learning rate of 2e-5, a max-
imum sequence length of 245, and the AdamW
optimizer. The model with the best evaluation loss
was selected as the final checkpoint. Each experi-
ment was repeated with seeds 42, 43, and 44.
Deobfuscation and Sanitization.
For each task,
we fine-tune the LLM using LoRA (α=16,
dropout=0.1, r=64) under 16-bit precision. The fine-
tuning configuration included 5 epochs, a batch
size of 16, a learning rate of 2e-5, a weight decay
of 1e-2, a maximum sequence length of 1024, the
AdamW optimizer, a warmup ratio of 0.03, and a
cosine learning rate scheduler. The best-performing
model based on evaluation loss was selected, and
each experiment was repeated with seeds 42, 43, 44.
For both Deobfuscation and Sanitization tasks, we
apply zero-shot and five-shot prompting schemes.
Prompt templates for the Deobfuscation task are
shown in Figures 7 and 8, and for the Sanitization
task in Figures 9 and 10.
22

--- Page 23 ---

Deobfuscation Zero-shot
You are an expert in Korean language correction.
The sentence I provide may be non-standard, use internet slang, phonetic spelling, intentional misspellings, or be obfuscated
in other ways.
Your task is to translate and normalize the sentence into natural, standard Korean.
Rules:
1. Preserve the original meaning.
2. If the tone is conversational, keep it conversational but in standard Korean.
3. Remove unnecessary emoticons or special characters.
4. Make the sentence grammatically smooth and natural.
Translate:
Input sentence: $input
Output sentence:
Figure 7: The zero-shot prompt used for deobfuscation. It provides the task descriptions and instructions.
Deobfuscation Five-shot
You are an expert in Korean language correction.
The sentence I provide may be non-standard, use internet slang, phonetic spelling, intentional misspellings, or be obfuscated
in other ways.
Your task is to translate and normalize the sentence into natural, standard Korean.
Rules:
1. Preserve the original meaning.
2. If the tone is conversational, keep it conversational but in standard Korean.
3. Remove unnecessary emoticons or special characters.
4. Make the sentence grammatically smooth and natural.
Examples:
Input sentence 1: $example1_input
Output sentence 1: $example1_output
Input sentence 2: $example2_input
Output sentence 2: $example2_output
Input sentence 3: $example3_input
Output sentence 3: $example3_output
Input sentence 4: $example4_input
Output sentence 4: $example4_output
Input sentence 5: $example5_input
Output sentence 5: $example5_output
Translate:
Input sentence: $input
Output sentence:
Figure 8: The five-shot prompt used for deobfuscation. It provides the task descriptions, instructions, and five
few-shot examples.
23

--- Page 24 ---

Sanitization Zero-shot
You are an expert in Korean language correction and detoxification.
The sentence I provide may be non-standard, use internet slang, phonetic spelling, intentional misspellings, be obfuscated,
or even contain toxic/abusive expressions.
Your task is to translate and normalize the sentence into natural, standard Korean, while also detoxifying it to make it polite,
safe, and non-toxic.
Rules:
1. Preserve the intended meaning as much as possible, but remove or soften toxic, offensive, or abusive language.
2. If the tone is conversational, keep it conversational but in standard Korean.
3. Remove unnecessary emoticons or special characters.
4. Make the sentence grammatically smooth and natural.
5. Ensure the output is non-toxic, respectful, and safe.
Translate:
Input sentence: $input
Output sentence:
Figure 9: The zero-shot prompt used for sanitization. It provides the task descriptions and instructions.
Sanitization Five-shot
You are an expert in Korean language correction and detoxification.
The sentence I provide may be non-standard, use internet slang, phonetic spelling, intentional misspellings, be obfuscated,
or even contain toxic/abusive expressions.
Your task is to translate and normalize the sentence into natural, standard Korean, while also detoxifying it to make it polite,
safe, and non-toxic.
Rules:
1. Preserve the intended meaning as much as possible, but remove or soften toxic, offensive, or abusive language.
2. If the tone is conversational, keep it conversational but in standard Korean.
3. Remove unnecessary emoticons or special characters.
4. Make the sentence grammatically smooth and natural.
5. Ensure the output is non-toxic, respectful, and safe.
Examples:
Input sentence 1: $example1_input
Output sentence 1: $example1_output
Input sentence 2: $example2_input
Output sentence 2: $example2_output
Input sentence 3: $example3_input
Output sentence 3: $example3_output
Input sentence 4: $example4_input
Output sentence 4: $example4_output
Input sentence 5: $example5_input
Output sentence 5: $example5_output
Translate:
Input sentence: $input
Output sentence:
Figure 10: The five-shot prompt used for sanitization. It provides the task descriptions, instructions, and five few-shot
examples.
24

--- Page 25 ---

1 2 3 4 5 6 7 8 9 1011121314151617
Rule
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
Rule
Label Co-occurrence Correlation Matrix
0.00
0.20
0.40
0.60
0.80
1.00
Co-occurrence Ratio
Figure 11: Correlation heatmap of label
E
Additional Experimental Results
E.1
Full Results on Classification
Table 23 shows the classification F1-score and stan-
dard deviations. Similar to the F1-scores, mod-
els fine-tuned on the combined dataset of non-
obfuscated toxic text and obfuscated text generally
achieved higher performance than those trained on
a single type of data. Furthermore, models trained
solely on the obfuscated dataset also performed
well in detecting non-obfuscated toxic texts, indi-
cating their generalization capability.
Figure 11 shows the rule-wise correlation matrix
of HateBERT fine-tuned on the easy dataset. The
easy dataset contains samples with two applied
rules per instance. As observed, there are no strong
correlations between the rules, suggesting that each
rule operates independently.
E.2
Among Difficulty Levels
Table. 24 illustrates the classification performance
of HateBERT across different dataset difficulty lev-
els. No-Obf refers to the original toxic dataset with-
out obfuscation. Each row represents the dataset
used for fine-tuning, and each column denotes the
evaluation dataset. The model trained on the total
dataset achieved the highest overall performance.
Excluding total, the easy dataset yielded the best
results. This suggests that the model learns to cap-
ture the characteristics of transformation rules from
data with fewer applied rules, enabling it to better
generalize to more challenging datasets with multi-
ple obfuscations.
25

--- Page 26 ---

Setting
HateBert
offensiveRoBERTa
toxicity-xlmr-v2
w/o Obf
Obf
∆
w/o Obf
Obf
∆
w/o Obf
Obf
∆
w/o Tuning
36.56
36.28
0.28
33.29
33.61
-0.32
79.28
56.80
22.48
(±5.59)
(±3.06)
(±0.28)
(±0.08)
(±0.48)
(±0.56)
(±10.44)
(±13.42)
(±22.21)
w/o Obf (FT)
76.69
65.88
10.81
91.86
69.98
21.88
95.06
53.66
41.40
(±0.95)
(±1.16)
(±2.27)
(±2.12)
(±8.22)
(±7.74)
(±47.56)
(±27.19)
(±4.47)
Ours (FT)
77.19
71.65
5.54
92.02
84.97
7.04
96.30
89.57
6.73
(±1.67)
(±0.78)
(±1.98)
(±1.08)
(±3.33)
(±2.89)
(±0.22)
(±0.11)
(±0.16)
w/o Obf + Ours (FT)
78.44
71.32
7.12
92.68
86.94
5.74
96.16
88.13
8.03
(±1.63)
(±0.99)
(±1.02)
(±0.33)
(±0.96)
(±0.95)
(±0.88)
(±2.48)
(±1.66)
Table 23: Binary Toxicity Classification under Obfuscation. Each model reports f1-score on non-obfuscated (No-
Obf) and obfuscated (Obf) sets, and the robustness gap ∆=No-Obf−Obf.
Setting
No-Obf
Easy
Normal
Hard
Total
No-Obf
0.7669 (±0.00)
0.6994 (±0.01)
0.6450 (±0.02)
0.6301 (±0.02)
0.6588 (±0.01)
Easy
0.7706 (±0.00)
0.7229 (±0.01)
0.6862 (±0.02)
0.6633 (±0.00)
0.6912 (±0.01)
Normal
0.7376 (±0.01)
0.7130 (±0.00)
0.6748 (±0.01)
0.6675 (±0.03)
0.6856 (±0.01)
Hard
0.7334 (±0.00)
0.7093 (±0.01)
0.6829 (±0.01)
0.6821 (±0.03)
0.6916 (±0.01)
Total
0.7719 (±0.01)
0.7233 (±0.01)
0.7062 (±0.01)
0.7195 (±0.01)
0.7165 (±0.00)
Table 24: Classification results according to difficulty levels. The F1-scores (%) are reported, with values in
parentheses indicating the standard deviations. Each experiment is repeated three times using HateBERT. Rows
represent the datasets used for SFT, and column denote the evaluation datasets. Bold indicates the best performances
and the second-best is underlined.
26

```
