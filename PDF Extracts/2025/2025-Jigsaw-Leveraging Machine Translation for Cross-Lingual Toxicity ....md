---
title: "2025-Jigsaw-Leveraging Machine Translation for Cross-Lingual Toxicity ... - PDF Extract"
source_pdf: "2025-Jigsaw-Leveraging Machine Translation for Cross-Lingual Toxicity ....pdf"
pages: 16
extracted_at: "2026-02-13T14:50:54.686518"
---

# PDF Extract: 2025-Jigsaw-Leveraging Machine Translation for Cross-Lingual Toxicity ...

**Source PDF:** 2025-Jigsaw-Leveraging Machine Translation for Cross-Lingual Toxicity ....pdf
**Total Pages:** 16

---

## Content

```
--- Page 1 ---

Translate, then Detect: Leveraging Machine
Translation for Cross-Lingual Toxicity Classification
Samuel J. Bell1,∗, Eduardo Sánchez1,2,∗, David Dale1, Pontus Stenetorp2, Mikel Artetxe3, Marta R.
Costa-jussà1
1FAIR at Meta, 2University College London, 3University of the Basque Country (UPV/EHU)
∗Joint first author
Multilingual toxicity detection remains a significant challenge due to the scarcity of training data
and resources for many languages.
While prior work has leveraged the translate-test paradigm
to support cross-lingual transfer across a range of classification tasks, the utility of translation in
supporting toxicity detection at scale remains unclear. In this work, we conduct a comprehensive
comparison of translation-based and language-specific/multilingual classification pipelines. We find
that translation-based pipelines consistently outperform out-of-distribution classifiers in 81.3% of
cases (13 of 16 languages), with translation benefits strongly correlated with both the resource level of
the target language and the quality of the machine translation (MT) system. Our analysis reveals
that traditional classifiers outperform large language model (LLM) judges, with this advantage being
particularly pronounced for low-resource languages, where translate-classify methods dominate
translate-judge approaches in 6 out of 7 cases. We additionally show that MT-specific fine-tuning on
LLMs yields lower refusal rates compared to standard instruction-tuned models, but it can negatively
impact toxicity detection accuracy for low-resource languages. These findings offer actionable guidance
for practitioners developing scalable multilingual content moderation systems.
Date: September 19, 2025
Correspondence: sjbell@meta.com, eduardosanchez@meta.com
1
Introduction
Detecting instances of toxic, abusive, or hateful con-
tent at scale is a challenging problem with important,
real-world implications for content moderation. In
a multilingual setting, however, toxicity detection is
often rendered particularly difficult due to a paucity
of labeled data for lower-resourced languages.
In
parallel, recent years have seen the scaling up of ma-
chine translation (MT) systems to cover a vast array
of world languages (e.g., NLLB-Team et al., 2022),
offering a potential pathway toward leveraging cross-
lingual transfer for improved multilingual toxicity
detection.
In monolingual non-English settings, cross-lingual
transfer has already proven useful for toxicity de-
tection (Eskelinen et al., 2023; Kobellarz and Silva,
2022), aligning with broader analyses of translation’s
utility for cross-lingual transfer across a range of clas-
sification tasks (Artetxe et al., 2023; Etxaniz et al.,
2023b; Ponti et al., 2021). Specifically, Artetxe et al.
(2023) compare translate-test (translating a sample
before zero-shot classification) against translate-train
Input text
es
translate
classify
translate
judge
classify
MT system
es → en
Classifier
en
LLM judge
en
Classifier
es
LLM judge
es
Toxicity
label
judge
Figure
1
Across
17
languages,
we
evaluate
tox-
icity
detection
using
translation-based
pipelines
(translate-classify, translate-judge) against classify-
ing in the original language (classify, judge). In this
example, text in Spanish (es) is optionally translated to
English (en) before classification.
(translating a sample before classification with a clas-
sifier finetuned on translation data) and find that
translate-test is competitive as long as translation
quality is sufficient.
While cross-lingual classification has been widely
studied in other NLP tasks, toxicity detection
1
arXiv:2509.14493v1  [cs.CL]  17 Sep 2025

--- Page 2 ---

presents distinctive challenges that warrant separate
investigation. Toxic language is culturally and contex-
tually grounded, with expressions, slurs, and taboos
that often lack direct equivalents across languages,
making transfer more brittle than for semantically
simpler labels.
Online toxicity also frequently in-
volves code-switching, orthographic variation, and
deliberate obfuscation, which may be less common in
other tasks. Moreover, toxicity labels are inherently
subjective and shaped by cultural norms, leading
to potential label drift when transferring across lan-
guages.
These factors, combined with the high stakes of mod-
eration errors, make cross-lingual transfer in toxicity
detection both consequential and scientifically chal-
lenging.
In this work, we present an empirical exploration
of translation for multilingual toxicity detection,
through the lens of the practitioner for whom labeled
data may be unavailable—a particularly common sce-
nario when working with lower-resourced languages—
by comparing translation-based pipelines against a va-
riety of off-the-shelf multi- and monolingual classifiers.
Across 27 pipelines spanning five MT systems and
nine toxicity classifiers—including both traditional
classifiers and large language model (LLM) judges—
we evaluate the benefit of cross-lingual classification
in 17 languages with varying levels of resources.
Our results suggest that leveraging translation is an
effective method for multilingual toxicity detection
(§4.1), with benefits scaling in line with increasing
language resources and MT system quality (§4.2).
Motivated by these results, we study the issue of re-
fusal rates and its mitigation via MT supervised fine-
tuning (MT-SFT), as well as the downstream effect
of MT-SFT on toxicity detection performance (§4.3).
Finally, we explore classifying using LLM judges and
compare them to traditional toxicity classifiers (§4.4).
We conclude with practical recommendations for de-
ploying multilingual toxicity detection systems at
scale.
2
Related work
2.1
Multilingual toxicity detection
Multilingual toxicity detection is widely used in
cases like content moderation or faithful transla-
tion (e.g. Costa-jussà et al., 2023).
Prior work
has either trained models using multilingual cor-
pora of labeled training data (e.g. Hanu, 2020), or
sought to exploit cross-lingual transfer via monolin-
gual finetuning of multilingual foundation models
(e.g. XLM-ROBERTa; Conneau et al., 2020a). Multi-
lingual evaluation datasets exist for toxicity detection
(e.g. Kivlichan et al., 2020; Gupta, 2021) alongside
those used for text detoxification (Dementieva et al.,
2024b, 2025). In this work, we evaluate a represen-
tative sample of off-the-shelf traditional classifiers,
including cross-lingual, and both mono- and multi-
lingual classifiers, across a wide variety of languages.
2.2
Cross-lingual classification
Early approaches to cross-lingual classification re-
lied on bilingual lexicons and statistical methods to
project documents into a shared feature space (Rapp,
1995; Dumais et al., 1997; Gliozzo and Strapparava,
2006). The introduction of cross-lingual word em-
beddings (Mikolov et al., 2013; Faruqui and Dyer,
2014; Ammar et al., 2016) enabled models trained
in one language to be applied to others through a
shared vector space. Prior to multilingual encoders,
transfer was typically achieved via MT, either by
translating the training data into the target language
(translate-train) or by translating inputs into the
source language at inference (translate-test) (Wan,
2009; Prettenhofer and Stein, 2010).
Multilingual sentence encoders such as LASER
(Artetxe and Schwenk, 2019) and mBERT (Devlin
et al., 2019) demonstrated the feasibility of direct
zero-shot transfer without translation. XLM (Lample
and Conneau, 2019) introduced translation language
modeling to improve alignment, and XLM-R (Con-
neau et al., 2020b) showed consistent gains from
scaling model and data size. Artetxe et al. (2020)
provided a systematic comparison of translate-train
and translate-test, while Etxaniz et al. (2023a) revis-
ited translate-test with modern neural MT, finding it
competitive for low-resource and distant languages.
Recent work explores large multilingual LLMs (Muen-
nighoff et al., 2022) and parameter-efficient adapta-
tion methods (Pfeiffer et al., 2020), aiming to combine
the flexibility of fine-tuning with the scalability of
zero-shot prompting.
3
Methods
We evaluate the performance of toxicity detec-
tion pipelines, where a pipeline comprises a bi-
nary toxicity classifier and an optional MT sys-
tem. In many languages—and particularly for lower-
resourced languages—labeled data for toxicity detec-
tion is unavailable, precluding the training and de-
ployment of specialized classifiers and motivating the
consideration of translation-based pipelines. As such,
2

--- Page 3 ---

we are principally interested in comparing pipelines
in the following three regimes:
classify (ID)
An untranslated, in-distribution
(ID) sample is classified in the source language using
a classifier trained on data from the same distribution
(e.g., evaluating a classifier on French social media
posts that has been trained on French social media
posts).
classify
(OOD)
An
untranslated,
out-of-
distribution (OOD) sample is classified in the source
language using a classifier trained on data from a
different distribution (e.g., evaluating a classifier on
French video comments that has been trained on
French social media posts).
translate-classify
The sample is translated into
English using an MT model before being classified
in English, using a toxicity classifier that supports
English. No evaluated classifiers have been trained
on translated data.
While we expect finetuned classifiers to exhibit the
strongest performance while operating ID, it is rela-
tive to the far more common OOD scenario (i.e.,
where no suitably finetuned classifier is available
to process the source language) that we expect
translate pipelines to offer significant utility.
3.1
Evaluation
We evaluate various pipeline implementations across
several languages and datasets, each of which com-
prises text samples xi and gold toxicity labels yi.
Each pipeline, given a sample, produces a continuous
score corresponding to toxicity.
Pipeline performance
To avoid the need for thresh-
olding, we evaluate pipeline performance via the Area
Under the Receiver Operating Characteristic curve
(AUC), which provides a continuous measure of how
well the pipeline can separate toxic from non-toxic
samples. The AUC is defined as:
AUC =
Z 1
0
TPR(t) dFPR(t)
where TPR(t) and FPR(t) are the true positive and
false positive rates at threshold t.
When comparing pipelines, we typically evaluate the
benefit of using one pipeline over another by way of
change in AUC. For two pipelines, PA and PB,
∆AUC(PA, PB) = AUC(PA) −AUC(PB)
We evaluate all possible combinations of pipeline
and dataset where the supported pipeline language
matches the dataset’s language.
Language resources
We evaluate the role of lan-
guage resourcefulness on pipeline performance, where
we roughly approximate the number of available re-
sources using the amount of documents available in
FineWeb2 (Penedo et al., 2025), a large-scale dataset
of web text sourced from various CommonCrawl snap-
shots.
Translation system quality
Following standard prac-
tice (e.g., Kocmi et al. 2024), we additionally eval-
uate the quality of translations into English using
the COMETKiwi-DA-XL (Rei et al. 2023) quality
estimation model, evaluated on the BOUQuET (Om-
nilingual MT Team et al., 2025) dataset.
3.2
Datasets
We curate a set of ten toxicity benchmarks for evalu-
ating pipeline performance, spanning 17 languages,
where each dataset comprises samples of text with
gold labels indicating toxicity. Benchmarks were iden-
tified via searching related work on toxicity detection
and by searching the Hugging Face datasets catalog.
We limited our search to only datasets comprising
natural human data, and to those where the gold
labels are produced by human annotators, such that
datasets comprising model-generated or otherwise
synthetic text or labels were discarded. Datasets were
restricted to those with a permissive license, where
data provenance was clearly indicated, and where the
data is readily-accessible online. This resulted in the
following benchmarks: Amharic Hate Speech (Ayele
et al., 2023); GermEval 2018 (German; Wiegand et al.
2018); Jigsaw Multilingual (Spanish, French, Italian,
and Turkish partitions only; Kivlichan et al. 2020); L-
HSAB (Levantine Arabic; Mulki et al. 2019); MACD
(Hindi, Kannada, Malayalam, Tamil, and Telugu;
Gupta et al. 2022); OffensiveHebrew Hamad et al.
(2023); ToLD-Br (Brazilian Portuguese; Leite et al.
2020); Russian Language Toxic Comments Belchikov
(2019); Thai Toxicity Tweet Corpus Sirihattasak et al.
(2018); and TextDetox 2024 (Ukrainian partition only;
Dementieva et al. 2024a). See Table 1 for full details.
Across all datasets, only the test partition is used for
evaluation. Where a toxicity classifier is trained on
data that includes one of our benchmark’s training
partitions, we consider that classifier to be operating
ID. Otherwise, as the classifier has been trained on
data unlike the benchmark, we consider it to be
operating OOD. See Table 2 for the training data
used to produce each classifier.
3

--- Page 4 ---

Language Code
Language
FineWeb-2 Docs
Dataset
No. Samples
am
Amharic
280,355
Amharic Hate Speech (Ayele et al., 2023)
1,501
ar
Arabic
57,752,149
L-HSAB Mulki et al. (2019)
5,846
de
German
427,700,394
GermEval 2018 Wiegand et al. (2018)
3,398
es
Spanish
405,634,303
Jigsaw Multilingual Kivlichan et al. (2020)
8,438
fr
French
332,646,715
Jigsaw Multilingual Kivlichan et al. (2020)
10,920
he
Hebrew
13,639,095
OffensiveHebrew Hamad et al. (2023)
500
hi
Hindi
20,587,135
MACD Gupta et al. (2022)
6,728
it
Italian
219,117,921
Jigsaw Multilingual Kivlichan et al. (2020)
8,494
kn
Kannada
2,309,261
MACD Gupta et al. (2022)
6,587
ml
Malayalam
3,406,035
MACD Gupta et al. (2022)
5,170
pt
Portuguese
189,851,449
ToLD-Br Leite et al. (2020)
21,000
ru
Russian
605,468,615
Russian Language Toxic Comments Belchikov (2019)
14,412
ta
Tamil
5,450,192
MACD Gupta et al. (2022)
6,000
te
Telugu
2,811,760
MACD Gupta et al. (2022)
6,000
th
Thai
35,949,449
Thai Toxicity Tweet Corpus Sirihattasak et al. (2018)
2,794
tr
Turkish
88,769,907
Jigsaw Multilingual Kivlichan et al. (2020)
14,000
uk
Ukrainian
47,552,562
TextDetox 2024 Dementieva et al. (2024a)
5,000
Table 1 Toxicity datasets used per language, including number of samples, and number of documents in FineWeb-2 as
a measure of language resourcedness.
Classifier
Supported Languages
Base Model
Training Dataset
xlm-r-finetuned-toxic-
political-tweets-es
es
XLM-RoBERTa
Tweets by Spanish politicians
distilbert-base-multilingual-
cased-toxicity
102 languages
DistilBERT multilingual
Jigsaw
distilbert-base-german-cased-
toxic-comments
de
German DistilBERT
Various incl. GermEval 2018
russian_toxicity_classifier
(Dementieva et al., 2022)
ru
RuBERT
Russian Language Toxic
Comments
xlmr-large-toxicity-classifier
am, ar, de, en, es, hi, ru,
uk, zh
XLM-RoBERTa
TextDetox 2024 (Dementieva
et al., 2024b)
amharic-hate-speech
am
Amharic RoBERTa
Amharic Hate Speech
multilingual-toxic-xlm-
roberta (Hanu, 2020)
en, es, fr, it, pt, ru, tr
XLM-RoBERTa
Jigsaw Multilingual
toxic-bert (Hanu, 2020)
en
BERT
Jigsaw
Table 2 Open-source toxicity classifiers evaluated in this work.
uk
tr
de
pt
it
th
fr
ru
ml
te
kn
es
ta
he
hi
ar
0.3
1.0
AUC
translate-classify
classify (OOD)
Figure 2 AUC of best possible translate-classify pipeline (over all combinations of translation systems and English
toxicity classifiers) and best possible classify (OOD) pipeline (over all OOD toxicity classifiers). Thetranslate-classify
approach wins across 13 out of 16 evaluated languages.
For the purposes of our evaluation, we intentionally
avoid distinguishing between toxicity detection and
and hate speech detection. While hate speech and
toxic or offensive are distinct concepts (Davidson
et al., 2017; Waseem et al., 2017)—with hate speech
typically being interpreted as directed toward a spe-
cific group (Davidson et al., 2017; Röttger et al.,
2021)—in practice, most evaluation datasets use the
terms toxicity, abusive or offensive language, and
hate speech almost interchangeably (Fortuna et al.,
4

--- Page 5 ---

Model
Type
Llama 3.1 8B Instruct Grattafiori et al. (2024)
LLM
Gemma 3 4B Instruct Gemma Team et al. (2025)
LLM
GPT-4o OpenAI (2024)
LLM
NLLB 200 3.3B NLLB-Team et al. (2022)
NMT
Table 3 Translation systems evaluated in this work.
2020; Banko et al., 2020). As a result we consider
datasets spanning toxicity and hate speech detection,
and expect minimal difference in findings between
tasks.
3.3
Toxicity classifiers
We consider eight open-source toxicity classifiers, in-
cluding English-language, non-English monolingual,
and multilingual, all of which are available on Hug-
ging Face. See §A.1 for selection criteria and Table 2
for full details of all classifiers considered.
All classifiers evaluated make use of pretrained
Transformer-based encoder models as a backbone,
such as BERT (Devlin et al., 2019), DistilBERT
(Sanh et al., 2020), ROBERTa (Liu et al., 2019),
or the multilingual XLM-ROBERTa (Conneau et al.,
2020a), some of which have undergone additional
fine-tuning on language specific corpora, such as Rus-
sian RuBERT (Kuratov and Arkhipov, 2019). All
classifiers are then finetuned on a portion of labeled
toxicity data, such as detailed in §3.2.
3.4
Translation systems
For translate-classify pipelines, we translate
samples into English with a translation system
before classifying the translations with an English-
supporting classifier.
We evaluate four different
translation systems (see Table 3), including both
encoder-decoder MT systems (NMT) and decoder-
only (i.e., LLM) translation systems. In the NMT
category, we use NLLB 200 3.3B (NLLB-Team
et al., 2022). We evaluate three LLM systems (two
open-weights and one behind-API): Llama 3.1 8B
Instruct (Grattafiori et al., 2024), Gemma 3 4B
Instruct (Gemma Team et al., 2025) and GPT-4o
(OpenAI, 2024). The following prompt is used to
produce the translations:
Translate the following sentence from
{{
,→lang}} into English. Respond only
,→with the translation into English ,
,→without any additional comments.
{{ sentence }}
am
tr
de
fr
it
es
ru
0.7
1.0
AUC
translate-classify
classify (ID)
Figure 3
AUC of best possible translate-classify
pipeline (over all combinations of translation systems and
English toxicity classifiers) and best possible classify
(ID) pipeline (over all ID toxicity classifiers).
The
translate-classifyapproachstillwinsacrossthreeofseven
languages where in-distribution finetuned classifiers are avail-
able.
4
Experiments
4.1
Translated pipelines often win
We
compare
the
AUC
of
the
best
translate-classify
pipeline
(the
best
possi-
ble combination of translation system and toxicity
classifier) against the best possible classify pipeline
(the best toxicity classifier that supports each
language).
Results
In
Figure
2,
we
evaluate
translate-classify
in
the
common
scenario
where a language-specific finetuned toxicity classifier
is unavailable, i.e., where classifiers are operating
OOD with respect to either their source language or
training domain, classify (OOD). We observe that
in such a scenario, the best translate-classify
pipeline outperforms the best classify
(OOD)
pipeline across 13 of 16 languages considered (81.3%).
Reducing a degree of freedom by using a fixed
classifier,
distilbert-base-multilingual-cased
-toxicity, translate-classify still outperforms
classify in 12 of 16 languages (75%; see Figure S1).
In Figure 3 we evaluate translated pipelines in sce-
narios where a language-specific finetuned classifier is
available (classify (ID)), though we note that this is
far from the case for the majority of languages. Here,
translate-classify still offers a robust baseline, out-
5

--- Page 6 ---

100k
200k 1M2M
10M
20M 100M
200M1G
Resources (fineweb2 documents)
−0.3
0.0
0.3
Translation benefit (Δ AUC)
(a) GPT-4o
100k
200k 1M2M
10M
20M 100M
200M1G
Resources (fineweb2 documents)
−0.3
0.0
0.3
Translation benefit (Δ AUC)
(b) Llama 3.1 8B Instruct
100k
200k 1M2M
10M
20M 100M
200M1G
Resources (fineweb2 documents)
−0.3
0.0
0.3
Translation benefit (Δ AUC)
(c) Gemma 3 4B Instruct
100k
200k 1M2M
10M
20M 100M
200M1G
Resources (fineweb2 documents)
−0.3
0.0
0.3
Translation benefit (Δ AUC)
ar
de
he
hi
kn
ml
pt
ru
ta
te
th
uk
(d) NLLB
Figure 4 Change in AUC (i.e., translation benefit) between translate-classify pipelines with a fixed English classifier,
toxic-bert, and classify pipelines with a fixed multilingual classifier, distilbert-base-multilingual-cased-toxicity,
as a function of language resources, over four translation systems (a) GPT-4o, (b) Llama 3.1 8B Instruct, (c) Gemma 3
4B Instruct, and (d) NLLB. Translation benefit is increased for higher resourced languages.
0.65
0.75
0.85
Translation quality
(cometkiwi-da-xl)
−0.3
0.0
0.3
Translation benefit (Δ AUC)
(a) Llama 3.1 8B Instruct
0.65
0.75
0.85
Translation quality
(cometkiwi-da-xl)
−0.3
0.0
0.3
Translation benefit (Δ AUC)
ar
de
hi
pt
ru
th
uk
(b) NLLB
Figure 5 Change in AUC (i.e., translation benefit) between translate-classify pipelines and classify pipelines, as a
function of English translation quality measured by cometkiwi-da-xl, over two translation systems (a) Llama 3.1 8B
Instruct, and (b) NLLB. Translation benefit increases with translation quality for both LLM-based and NMT systems.
performing finetuned classify (ID) pipelines across
three out of seven languages. See Table S1 for full
results over all languages.
4.2
Translation benefit scales with resources
Next,
we explore which factors determine the
success
of
translate-classify
pipelines.
To
allow
for
consistent
comparison
across
lan-
guages and control for variability in classifier
performance,
we
now
limit
ourselves
to
two
fixed
classifiers:
for
translate-classify
we
use the English classifier, toxic-bert, while for
classify we use our most multilingual classifier,
distilbert-base-multilingual-cased
-toxicity.
We evaluate the role of language resourcefulness
and translation quality on change in AUC between
pipelines, as specified in §3.1.
Results
In Figure 4, we observe that the relative
benefit of translate-classify over classify, as
measured by the change in AUC, is higher for better-
resourced languages. This is consistent across four
different translation systems, including both LLM
and NMT systems. After fixing the best perform-
ing classifiers, we notice that the relative benefit of
translation for some languages is affected, suggesting
the framework is susceptible to model selection to
maximize gains.
Similarly, in Figure 5 we see that the relative benefit
of translate-classify increases with the quality
of translations in each language, across both LLM
and NMT systems. We note a higher sensitivity to
both language resourcefulness and translation quality
for the NMT system, NLLB, compared with LLM
systems.
4.3
MT-SFT reduces refusal and improves
performance
When using safety-tuned LLMs for translation, a
we noticed that key risk is refusal:
the model
declines to translate inputs containing harmful
or toxic content, which can severely limit cover-
age in toxicity detection.
We examine whether
finetuning for MT can mitigate this problem by
comparing two translate-classify pipelines: (1)
6

--- Page 7 ---

am
kn
te
ml
ta
he
hi
th
uk
ar
tr
pt
it
fr
es
de
ru
Increasing resources →
0.2
0.6
1.0
AUC
classify
translate-classify (Llama 3)
translate-classify (+TowerBlocks/MT)
Figure
6
AUC
of
translate-classify
(Llama
3)
and
translate-classify
(+TowerBlocks/MT)
using
a
fixed
English
classifier,
toxic-bert,
and
a
classify
pipeline
using
a
fixed
multilingual
classifier,
distilbert-base-multilingual-cased-toxicity. Using a finetuned LLM for translation improves pipeline performance for
higher-resourced languages.
Name
TPR (Llama 3.1)
TNR (+TowerBlocks/MT)
TH
100%
100%
DE
100%
100%
UK
70%
100%
ML
75%
100%
AR
40%
100%
Table4 Analysis of human annotations of refusal predictions, showing True Positive Rate (TPR) of Llama 3.1 8B Instruct
(Llama 3.1) and the True Negative Rate (TNR) of the same model finetuned on TowerBlocks/MT (+TowerBlocks/MT).
Refusal detection is highly accurate for Thai, German, and Ukrainian. Even for Malayalam and Levantine Arabic where the refusal
detector produces some false positives, the finetuned model never refuses.
100k
200k 1M2M
10M
20M 100M
200M1G
Resources (fineweb2 documents)
−0.3
0.0
0.3
Translation benefit (Δ AUC)
translate-classify (Llama 3)
translate-classify (+TowerBlocks/MT)
Figure 7 Change in AUC (i.e., translation benefit) of
translate-classify (Llama 3) and translate-classify
(+TowerBlocks/MT) pipelines with a fixed English classi-
fier against a fixed classify pipeline with a fixed mul-
tilingual classifier, as a function of language resources.
The translate-classify (+TowerBlocks/MT) pipeline per-
formance is more sensitive to available language resources.
translate-classify (Llama 3), which uses trans-
lations from a standard instruction-tuned LLM
(Llama 3.1 8B Instruct), and (2) translate-classify
(+TowerBlocks/MT), which uses translations from the
same base model after supervised finetuning (MT-
SFT) on the TowerBlocks/MT dataset (Alves et al.,
2024) (see §A.2 for details). Both pipelines feed trans-
lations to a fixed English-only classifier, toxic-bert,
to isolate translation effects, and are compared
against a direct multilingual classify pipeline using
distilbert-base-multilingual-cased -toxicity.
Refusal detection
We use Minos (Suphavadeeprasit
et al., 2025) to assign each translation output yi =
T(xi) a refusal probability Pr(yi). The refusal rate
is defined as:
R(T) = 1
N
N
X
i=1
[Pr(T(xi)) > 0.95],
where a 0.95 threshold minimizes false positives. For
two systems TA and TB, the difference in refusal rates
is:
∆R(PTA, PTB) = R(PTA) −R(PTB).
Refusal
results
As
shown
in
Figure
8,
translate-classify
(+TowerBlocks/MT) reduces
refusal rates in every language compared with
translate-classify
(Llama
3).
The reduction
scales approximately log-linearly with language
resources (Figure 9a), indicating that MT-SFT
particularly benefits high-resource languages where
refusals are rarer but still impactful. Lower refusal
means more toxic content is actually processed by
the classifier, directly improving pipeline coverage.
7

--- Page 8 ---

th
0%
20%
Refusal rate
hi
es
fr
pt
de
it
tr
ru
0%
5%
he
uk
ar
kn
te
ml
ta
am
0.0%
0.3%
translate-classify (Llama 3)
translate-classify (+TowerBlocks/MT)
Figure 8 Translation refusal rate of translate-classify (Llama 3) and translate-classify (+TowerBlocks/MT)
pipelines. Note three separate scales for legibility. Using a finetuned LLM for translation reduces refusal rates.
Human verification of refusal mitigation
To validate
both the accuracy of our automated refusal detec-
tion and the effectiveness of MT-SFT in addressing
refusals, we conducted a targeted human annotation
study. For each dataset, we randomly sampled up
to 5% of the content flagged as refusals by the base
Llama 3.1 8B Instruct model, with a minimum of 10
examples per dataset. Annotators manually verified
whether each flagged case was indeed a refusal, then
examined translations of the same inputs generated
by the MT-finetuned model. As shown in Table 4,
the refusal detector achieved perfect true positive
rates for Thai, German, and Ukrainian, and high
—though not perfect— accuracy for Malayalam and
Levantine Arabic, where some false positives were
observed. Importantly, the MT-finetuned model pro-
duced valid translations for all annotated examples,
yielding a true negative rate of 100% across every
language in the sample. This confirms that, at least
for the languages tested, MT-SFT can completely
eliminate refusals observed in the base instruction-
tuned model, turning previously blocked content into
usable inputs for the downstream classifier.
MT-SFT improves performance for high resource lan-
guages
In addition to lowering refusals, MT-SFT
also improves classification accuracy. In Figure 6,
translate-classify
(+TowerBlocks/MT) achieves
higher AUC than translate-classify (Llama 3)
for 11 of 17 languages, with gains concentrated in
high-resource settings. When measured against the
multilingual classify baseline, translate-classify
(+TowerBlocks/MT) shows even stronger sensitivity
to language resource availability (Figure 7).
4.4
LLM judges underperform on lower-
resourced languages
Given the strong performance of LLMs across a range
of tasks, we additionally compare pipelines based on
traditional classifiers vs. zero-shot LLM judges.
Specifically, we analyze the performance of two
judge-based pipelines: (1) judge, where an LLM
is prompted to classify untranslated samples, and
(2) translate-judge, where the LLM is prompted
to classify samples that have been translated into
English. The judge in both cases is Llama 3.1 8B
Instruct with the following custom prompt, where
{{sample}} is either the translated or original sample
according to pipeline:
You are a toxicity classifier. Classify
,→the following text as toxic or not
,→toxic. Respond with ’toxic ’ or ’not
,→
toxic ’ with no other comments or
,→explanation.
Text: {{ sample }}
Classification:
Translations are also produced using Llama 3.1 8B
Instruct. We compare both judge pipelines against a
classify pipeline based on the overall best English
classifier, toxic-bert, coupled again with Llama 3.1
8B Instruct for fair comparison.
We evaluate all
pipelines using accuracy as opposed to AUC, as the
LLM judge emits only a label, rather than a continu-
ous score.
Results
Figure 10 illustrates notable patterns in the
comparative performance of translate-judge and
judge pipelines. Across all languages, translation-
based approaches narrowly outperform their un-
translated counterparts; however, this advantage be-
comes pronounced in low-resource settings, where
translate-judge completely dominates, outperform-
ing judge in 6 out of 7 low-resource languages.
Similarly,
translate-classify pipelines provide
a slight overall edge compared to both judge
and translate-judge,
but the margin is espe-
cially significant for low-resource languages, where
translate-classify overwhelmingly wins (again in
6 out of 7 cases). These results further indicate that
multilingual capabilities in LLMs are not homoge-
neously distributed: while MT models demonstrate
broader multilingual reach, toxicity classification per-
formance by LLMs is markedly less consistent across
lower-resource languages.
8

--- Page 9 ---

100k
200k 1M2M
10M
20M 100M
200M1G
Resources (fineweb2 documents)
−1.0
0.0
1.0
2.0
Finetuning benefit (Δ refusal rate)
am
kn
ar
ml
de
pt
es
ru
fr
ta
he
te
hi
tr
it
uk
(a) ∆refusal
100k
200k 1M2M
10M
20M 100M
200M1G
Resources (fineweb2 documents)
−0.4
0.0
0.2
Finetuning benefit (Δ AUC)
am
ml
ar
pt
de
ru
es
ta
fr
te
he
th
hi
tr
it
uk
kn
(b) ∆AUC
Figure 9 Change in (a) translation refusal rate and (b) AUC of a translate-classify (+TowerBlocks/MT) pipeline
against a translate-classify (Llama 3) pipeline, both with a fixed English classifier, toxic-bert, as a function
of language resources. The benefit of using a finetuned LLM for translation, in terms of both refusal rates and improved
performance, increases for with language resources.
am
kn
te
ml
ta
he
hi
th
uk
ar
tr
pt
it
fr
es
de
ru
Increasing resources →
0.2
0.6
1.0
Accuracy
translate-classify
translate-judge
judge
Figure 10 Accuracy of translate-judge, judge, and translate-classify with a fixed English classifier, toxic-bert,
all using a Llama 3 for translation. Translation with traditional classifiers outperforms LLM judges for most lower resourced
languages.
5
Discussion
Across ten benchmarks spanning 17 languages, our
analysis suggests that translation-based approaches
can be successfully leveraged to support multilin-
gual toxicity detection at scale. Specifically, we ob-
serve that translate-classify pipelines outperform
classify (OOD), a non-finetuned classifier operating
OOD (i.e., an off-the-shelf model) in the majority of
cases, and can even occasionally outperform classify
(ID), dedicated finetuned classifiers evaluated ID.
The relative benefit of using translate-classify
over classify pipelines increases with both a lan-
guage’s available resources and the quality of the
translation system.
This may suggest that while
translation may be an effective strategy in general,
it does have the potential to increase performance
disparities between better- and worse-resourced lan-
guages.
We additionally note that using an MT-
finetuned LLM for translations can further drive up
pipeline performance, in part, by reducing refusal
rates, but that this benefit appears to be reserved
for higher-resourced languages. Finally, we evaluate
the utility of an LLM judge approach over tradi-
tional (e.g., BERT-based) classification, finding that
in lower-resourced languages, translate-classify
consistently outperforms.
Practical recommendations
We make four practical
recommendations for practitioners looking to deploy
multilingual toxicity detection at scale.
1. At the very least, translate-classify pipelines
using traditional classifiers and LLM-based trans-
lation should be considered a robust baseline.
2. If fine-tuning on dedicated data is unavailable, a
translate-classify pipeline is likely to provide
a strong first choice of model, particularly in
languages where translation quality is high.
3. If operating on a higher-resourced language, mak-
ing use of an MT-finetuned LLM may offer
some performance improvements over a stan-
dard instruction-tuned LLM, particularly in the
scenario where refusal rates can be reduced.
9

--- Page 10 ---

4. Unlike many other NLP tasks, an LLM judge
demonstrates only a limited performance advan-
tage on select higher-resourced languages when
compared to traditional (e.g., BERT-based) clas-
sifiers.
Limitations
While we approach multilingual toxicity detection
through the lens of a practitioner making a choice
between available, off-the-shelf pipeline components,
this does limit our ability to analyze the role of spe-
cific finetuning details. For example, in contrast with
previous work (Artetxe et al., 2023) that has con-
trasted cross-lingual transfer pipelines where the clas-
sifier was finetuned on either the original domain or
the outputs of the translation system, we only make
use of publicly-available classifiers which may be fine-
tuned on different numbers of samples or different
domains, and none of which are finetuned on trans-
lations. However, given the performance improve-
ments offered by the translate-classify pipeline
without finetuning on translations, we might expect a
translation-finetuned classifier to further benefit the
translate-classify approach.
As we note in §3.2, our work is also potentially lim-
ited by shifts in data distribution between languages.
In order to identify broad trends across many lan-
guages with different levels of resources, we draw
samples from different constituent datasets. These
datasets, however, are drawn from different domains
(e.g., social media vs. WikiMedia talk pages) with
labels produced using different annotation schemas
(e.g., identifying hate speech vs.
toxicity).
As a
result, our conclusions should be interpreted as in-
dicative of general trends about the relative utility
of translation, rather than individual claims about
how well translation may function on any given lan-
guage. This limitation could be overcome with access
to additional highly-multilingual datasets of labeled
toxicity data.
References
Duarte M. Alves, José Pombal, Nuno M. Guerreiro, Pe-
dro H. Martins, João Alves, Amin Farajian, Ben Peters,
Ricardo Rei, Patrick Fernandes, Sweta Agrawal, Pierre
Colombo, José G. C. de Souza, and André F. T. Mar-
tins. Tower: An open multilingual large language model
for translation-related tasks, 2024.
Waleed Ammar, Phoebe Mulcaire, Yulia Tsvetkov, Guil-
laume Lample, Chris Dyer, and Noah A. Smith. Mas-
sively multilingual word embeddings. In Proceedings of
the 54th Annual Meeting of the Association for Compu-
tational Linguistics (Volume 2: Short Papers), pages
152–157, Berlin, Germany, 2016. Association for Com-
putational Linguistics. doi: 10.18653/v1/P16-2025.
Mikel Artetxe and Holger Schwenk. Massively multilin-
gual sentence embeddings for zero-shot cross-lingual
transfer and beyond. In Transactions of the Associ-
ation for Computational Linguistics, volume 7, pages
597–610, 2019. doi: 10.1162/tacl_a_00288.
Mikel Artetxe, Sebastian Ruder, and Dani Yogatama.
Translation artifacts in cross-lingual transfer learning.
In Proceedings of EMNLP, pages 7674–7684, 2020. doi:
10.18653/v1/2020.emnlp-main.619.
Mikel Artetxe, Vedanuj Goswami, Shruti Bhosale, An-
gela Fan, and Luke Zettlemoyer. Revisiting machine
translation for cross-lingual classification. In Houda
Bouamor, Juan Pino, and Kalika Bali, editors, Proceed-
ings of the 2023 Conference on Empirical Methods in
Natural Language Processing, pages 6489–6499, Singa-
pore, December 2023. Association for Computational
Linguistics. doi: 10.18653/v1/2023.emnlp-main.399.
https://aclanthology.org/2023.emnlp-main.399/.
Abinew Ali Ayele, Seid Muhie Yimam, Tadesse Destaw
Belay, Tesfa Asfaw, and Chris Biemann. Exploring
Amharic Hate Speech Data Collection and Classifica-
tion Approaches.
In Ruslan Mitkov and Galia An-
gelova, editors, Proceedings of the 14th International
Conference on Recent Advances in Natural Language
Processing, pages 49–59, Varna, Bulgaria, Septem-
ber 2023. INCOMA Ltd., Shoumen, Bulgaria. https:
//aclanthology.org/2023.ranlp-1.6/.
Michele Banko, Brendon MacKeen, and Laurie Ray. A
Unified Taxonomy of Harmful Content. In Seyi Aki-
wowo, Bertie Vidgen, Vinodkumar Prabhakaran, and
Zeerak Waseem, editors, Proceedings of the Fourth
Workshop on Online Abuse and Harms, pages 125–137,
Online, November 2020. Association for Computational
Linguistics. doi: 10.18653/v1/2020.alw-1.16.
Anatoly Belchikov. Russian Language Toxic Comments,
2019.
https://www.kaggle.com/datasets/blackmoon/
russian-language-toxic-comments.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
Vishrav Chaudhary, Guillaume Wenzek, Francisco
Guzmán, Edouard Grave, Myle Ott, Luke Zettlemoyer,
and Veselin Stoyanov. Unsupervised Cross-lingual Rep-
resentation Learning at Scale. In Dan Jurafsky, Joyce
Chai, Natalie Schluter, and Joel Tetreault, editors,
Proceedings of the 58th Annual Meeting of the Associa-
tion for Computational Linguistics, pages 8440–8451,
Online, July 2020a. Association for Computational
Linguistics. doi: 10.18653/v1/2020.acl-main.747.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
Vishrav Chaudhary, Guillaume Wenzek, Francisco
Guzmán, Edouard Grave, Myle Ott, Luke Zettlemoyer,
and Veselin Stoyanov.
Unsupervised cross-lingual
10

--- Page 11 ---

representation learning at scale.
In Proceedings of
ACL, pages 8440–8451, 2020b. doi: 10.18653/v1/2020.
acl-main.747.
Marta Costa-jussà, Eric Smith, Christophe Ropers, Daniel
Licht, Jean Maillard, Javier Ferrando, and Carlos
Escolano.
Toxicity in multilingual machine trans-
lation at scale.
In Houda Bouamor, Juan Pino,
and Kalika Bali, editors, Findings of the Association
for Computational Linguistics: EMNLP 2023, pages
9570–9586, Singapore, December 2023. Association for
Computational Linguistics.
doi: 10.18653/v1/2023.
findings-emnlp.642. https://aclanthology.org/2023.
findings-emnlp.642/.
Thomas Davidson, Dana Warmsley, Michael Macy, and
Ingmar Weber. Automated Hate Speech Detection and
the Problem of Offensive Language. Proceedings of
the International AAAI Conference on Web and Social
Media, 11(1):512–515, May 2017. ISSN 2334-0770. doi:
10.1609/icwsm.v11i1.14955.
Daryna Dementieva, Varvara Logacheva, Irina Nikishina,
Alena Fenogenova, David Dale, Irina Krotova, Nikita
Semenov, Tatiana Shavrina, and Alexander Panchenko.
RUSSE-2022: Findings of the First Russian Detoxi-
fication Shared Task Based on Parallel Corpora. In
Computational Linguistics and Intellectual Technolo-
gies: Proceedings of the International Conference "Di-
alogue 2022", pages 114–131. RSUH, June 2022. doi:
10.28995/2075-7182-2022-21-114-131.
Daryna Dementieva, Valeriia Khylenko, Nikolay Babakov,
and Georg Groh. Toxicity Classification in Ukrainian.
In Yi-Ling Chung, Zeerak Talat, Debora Nozza,
Flor Miriam Plaza-del-Arco, Paul Röttger, Aida
Mostafazadeh Davani, and Agostina Calabrese, edi-
tors, Proceedings of the 8th Workshop on Online Abuse
and Harms (WOAH 2024), pages 244–255, Mexico City,
Mexico, June 2024a. Association for Computational
Linguistics. doi: 10.18653/v1/2024.woah-1.19.
Daryna Dementieva, Daniil Moskovskiy, Nikolay Babakov,
Abinew Ali Ayele, Naquee Rizwan, Florian Schneider,
Xintong Wang, Seid Muhie Yimam, Dmitry Ustalov,
Elisei Stakovskii, Alisa Smirnova, Ashraf Elnagar, Ani-
mesh Mukherjee, and Alexander Panchenko. Overview
of the Multilingual Text Detoxification Task at PAN
2024. CLEF 2024: Conference and Labs of the Evalua-
tion Forum, 2024b.
Daryna Dementieva, Nikolay Babakov, Amit Ronen,
Abinew Ali Ayele, Naquee Rizwan, Florian Schneider,
Xintong Wang, Seid Muhie Yimam, Daniil Moskovskiy,
Elisei Stakovskii, Eran Kaufman, Ashraf Elnagar, Ani-
mesh Mukherjee, and Alexander Panchenko. Multi-
lingual and explainable text detoxification with par-
allel corpora. In Owen Rambow, Leo Wanner, Mar-
ianna Apidianaki, Hend Al-Khalifa, Barbara Di Eu-
genio, and Steven Schockaert, editors, Proceedings of
the 31st International Conference on Computational
Linguistics, pages 7998–8025, Abu Dhabi, UAE, Jan-
uary 2025. Association for Computational Linguistics.
https://aclanthology.org/2025.coling-main.535/.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina
Toutanova. BERT: Pre-training of Deep Bidirectional
Transformers for Language Understanding.
In Jill
Burstein, Christy Doran, and Thamar Solorio, editors,
Proceedings of the 2019 Conference of the North Amer-
ican Chapter of the Association for Computational
Linguistics: Human Language Technologies, Volume 1
(Long and Short Papers), pages 4171–4186, Minneapo-
lis, Minnesota, June 2019. Association for Computa-
tional Linguistics. doi: 10.18653/v1/N19-1423.
Susan T. Dumais, Todd A. Letsche, Michael L. Littman,
and Thomas K. Landauer. Automatic cross-language
retrieval using latent semantic indexing.
In AAAI
Spring Symposium on Cross-Language Text and Speech
Retrieval, pages 18–24, 1997.
Anni Eskelinen, Laura Silvala, Filip Ginter, Sampo
Pyysalo, and Veronika Laippala. Toxicity detection in
Finnish using machine translation. In Tanel Alumäe
and Mark Fishel, editors, Proceedings of the 24th Nordic
Conference on Computational Linguistics (NoDaLiDa),
pages 685–697, Tórshavn, Faroe Islands, May 2023.
University of Tartu Library. https://aclanthology.
org/2023.nodalida-1.68/.
Julen Etxaniz, Mikel Artetxe, and Rodrigo Agerri. On
the effectiveness of translate-test for cross-lingual clas-
sification. In Proceedings of the 2023 Conference on
Empirical Methods in Natural Language Processing,
pages 9933–9947, Singapore, 2023a. Association for
Computational Linguistics.
doi: 10.18653/v1/2023.
emnlp-main.613.
Julen Etxaniz, Gorka Azkune, Aitor Soroa, Oier Lopez
de Lacalle, and Mikel Artetxe. Do multilingual lan-
guage models think better in english?, 2023b. https:
//arxiv.org/abs/2308.01223.
Manaal Faruqui and Chris Dyer. Improving vector space
word representations using multilingual correlation. In
Proceedings of the 14th Conference of the European
Chapter of the Association for Computational Linguis-
tics, pages 462–471, Gothenburg, Sweden, 2014. Asso-
ciation for Computational Linguistics.
Paula Fortuna, Juan Soler, and Leo Wanner. Toxic, Hate-
ful, Offensive or Abusive? What Are We Really Classi-
fying? An Empirical Analysis of Hate Speech Datasets.
In Nicoletta Calzolari, Frédéric Béchet, Philippe Blache,
Khalid Choukri, Christopher Cieri, Thierry Declerck,
Sara Goggi, Hitoshi Isahara, Bente Maegaard, Joseph
Mariani, Hélène Mazo, Asuncion Moreno, Jan Odijk,
and Stelios Piperidis, editors, Proceedings of the Twelfth
Language Resources and Evaluation Conference, pages
6786–6794, Marseille, France, May 2020. European Lan-
guage Resources Association. ISBN 979-10-95546-34-4.
https://aclanthology.org/2020.lrec-1.838/.
Gemma
Team,
Aishwarya
Kamath,
Johan
Ferret,
11

--- Page 12 ---

. . . , Cassidy Hardin, Robert Dadashi, and Léonard
Hussenot. Gemma 3 Technical Report, March 2025.
Alfio Gliozzo and Carlo Strapparava. Exploiting lexical
alignment for cross-language textual entailment. In
Proceedings of the 11th Conference of the European
Chapter of the Association for Computational Linguis-
tics, pages 33–40, Trento, Italy, 2006. Association for
Computational Linguistics.
Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri,
. . . , Zhenyu Yang, Zhiwei Zhao, and Zhiyu Ma. The
Llama 3 Herd of Models, November 2024.
Vikram Gupta.
Multilingual and multilabel emotion
recognition using virtual adversarial training. In Pro-
ceedings of the 1st Workshop on Multilingual Repre-
sentation Learning, pages 74–85, Punta Cana, Domini-
can Republic, November 2021. Association for Com-
putational Linguistics. doi: 10.18653/v1/2021.mrl-1.7.
https://aclanthology.org/2021.mrl-1.7.
Vikram Gupta, Sumegh Roychowdhury, Mithun Das,
Somnath Banerjee, Punyajoy Saha, Binny Mathew,
Hastagiri
Prakash
Vanchinathan,
and
Animesh
Mukherjee.
Multilingual Abusive Comment De-
tection at Scale for Indic Languages.
Advances in
Neural Information Processing Systems, 35:26176–
26191,
December
2022.
https://proceedings.
neurips.cc/paper_files/paper/2022/hash/
a7c4163b33286261b24c72fd3d1707c9-Abstract-Datasets_
and_Benchmarks.html.
Nagham Hamad, Mustafa Jarrar, Mohammad Khalilia,
and Nadim Nashif. Offensive Hebrew Corpus and De-
tection using BERT. In 2023 20th ACS/IEEE Inter-
national Conference on Computer Systems and Appli-
cations (AICCSA), pages 1–8, December 2023. doi:
10.1109/AICCSA59173.2023.10479258.
Laura Hanu. Detoxify, 2020. https://huggingface.co/
unitary/multilingual-toxic-xlm-roberta.
Ian
Kivlichan,
Jeffrey
Sorensen,
Julia
Elliott,
Lucy
Vasserman,
Martin
Görner,
and
Phil
Culliton.
Jigsaw
Multilingual
Toxic
Com-
ment
Classification,
2020.
https://kaggle.com/
jigsaw-multilingual-toxic-comment-classification.
Jordan K. Kobellarz and Thiago H. Silva. Should we
translate? evaluating toxicity in online comments when
translating from portuguese to english. In Proceedings
of the Brazilian Symposium on Multimedia and the
Web, WebMedia ’22, page 89–98, New York, NY, USA,
2022. Association for Computing Machinery. ISBN
9781450394093. doi: 10.1145/3539637.3556892. https:
//doi.org/10.1145/3539637.3556892.
Tom Kocmi, Eleftherios Avramidis, Rachel Bawden,
Ondřej Bojar, Anton Dvorkovich, Christian Federmann,
Mark Fishel, Markus Freitag, Thamme Gowda, Ro-
man Grundkiewicz, Barry Haddow, Marzena Karpin-
ska, Philipp Koehn, Benjamin Marie, Christof Monz,
Kenton Murray, Masaaki Nagata, Martin Popel, Maja
Popović, Mariya Shmatova, Steinthór Steingrímsson,
and Vilém Zouhar. Findings of the WMT24 General
Machine Translation Shared Task: The LLM Era Is
Here but MT Is Not Solved Yet. In Barry Haddow,
Tom Kocmi, Philipp Koehn, and Christof Monz, edi-
tors, Proceedings of the Ninth Conference on Machine
Translation, pages 1–46, Miami, Florida, USA, Novem-
ber 2024. Association for Computational Linguistics.
doi: 10.18653/v1/2024.wmt-1.1.
Yuri Kuratov and Mikhail Arkhipov. Adaptation of Deep
Bidirectional Multilingual Transformers for Russian
Language, May 2019.
Guillaume Lample and Alexis Conneau. Cross-lingual
language model pretraining. In Advances in Neural
Information Processing Systems, 2019.
João Augusto Leite, Diego Silva, Kalina Bontcheva, and
Carolina Scarton. Toxic Language Detection in So-
cial Media for Brazilian Portuguese:
New Dataset
and Multilingual Analysis. In Kam-Fai Wong, Kevin
Knight, and Hua Wu, editors, Proceedings of the 1st
Conference of the Asia-Pacific Chapter of the Asso-
ciation for Computational Linguistics and the 10th
International Joint Conference on Natural Language
Processing, pages 914–924, Suzhou, China, December
2020. Association for Computational Linguistics. doi:
10.18653/v1/2020.aacl-main.91.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar
Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke
Zettlemoyer, and Veselin Stoyanov.
RoBERTa: A
Robustly Optimized BERT Pretraining Approach, July
2019.
Tomas Mikolov, Quoc V. Le, and Ilya Sutskever. Exploit-
ing similarities among languages for machine transla-
tion. In arXiv preprint arXiv:1309.4168, 2013.
Niklas Muennighoff, Nouamane Tazi, and Sebastian
Ruder. Crosslingual generalization through multitask
finetuning. In Proceedings of the 60th Annual Meet-
ing of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 1596–1610, 2022. doi:
10.18653/v1/2022.acl-long.112.
Hala Mulki, Hatem Haddad, Chedi Bechikh Ali, and Hal-
ima Alshabani. L-HSAB: A Levantine Twitter Dataset
for Hate Speech and Abusive Language. In Sarah T.
Roberts, Joel Tetreault, Vinodkumar Prabhakaran,
and Zeerak Waseem, editors, Proceedings of the Third
Workshop on Abusive Language Online, pages 111–118,
Florence, Italy, August 2019. Association for Compu-
tational Linguistics. doi: 10.18653/v1/W19-3512.
NLLB-Team, Marta R. Costa-jussà, James Cross, Onur
Çelebi, Maha Elbayad, Kenneth Heafield, Kevin Hef-
fernan, Elahe Kalbassi, Janice Lam, Daniel Licht,
Jean Maillard, Anna Sun, Skyler Wang, Guillaume
Wenzek, Al Youngblood, Bapi Akula, Loic Bar-
rault, Gabriel Mejia Gonzalez, Prangthip Hansanti,
John Hoffman,
Semarley Jarrett,
Kaushik Ram
12

--- Page 13 ---

Sadagopan, Dirk Rowe, Shannon Spruit, Chau Tran,
Pierre Andrews, Necip Fazil Ayan, Shruti Bhosale,
Sergey Edunov, Angela Fan, Cynthia Gao, Vedanuj
Goswami, Francisco Guzmán, Philipp Koehn, Alexan-
dre Mourachko, Christophe Ropers, Safiyyah Saleem,
Holger Schwenk, and Jeff Wang.
No language left
behind: Scaling human-centered machine translation,
2022.
Omnilingual MT Team, Pierre Andrews, Mikel Artetxe,
Mariano Coria Meglioli, Marta R. Costa-jussà, Joe
Chuang, David Dale, Cynthia Gao, Jean Maillard,
Alex Mourachko, Christophe Ropers, Safiyyah Saleem,
Eduardo Sánchez, Ioannis Tsiamas, Arina Turkatenko,
Albert Ventayol-Boada, and Shireen Yates. BOUQuET:
Dataset, Benchmark and Open initiative for Universal
Quality Evaluation in Translation, June 2025.
OpenAI. GPT-4o System Card, October 2024.
Guilherme Penedo, Hynek Kydlíček, Vinko Sabolčec, Bet-
tina Messmer, Negar Foroutan, Amir Hossein Kargaran,
Colin Raffel, Martin Jaggi, Leandro Von Werra, and
Thomas Wolf. FineWeb2: One Pipeline to Scale Them
All – Adapting Pre-Training Data Processing to Every
Language, June 2025.
Jonas Pfeiffer, Ivan Vulić, Iryna Gurevych, and Se-
bastian Ruder.
Mad-x:
An adapter-based frame-
work for multi-task cross-lingual transfer.
In Pro-
ceedings of EMNLP, pages 7654–7673, 2020.
doi:
10.18653/v1/2020.emnlp-main.617.
Edoardo Maria Ponti, Julia Kreutzer, Ivan Vulić, and Siva
Reddy. Modelling latent translations for cross-lingual
transfer, 2021. https://arxiv.org/abs/2107.11353.
Peter Prettenhofer and Benno Stein. Cross-language text
classification using structural correspondence learning.
In Proceedings of the 48th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 1118–1127,
Uppsala, Sweden, 2010. Association for Computational
Linguistics.
Reinhard Rapp. Identifying word translations in non-
parallel texts.
In Proceedings of the 33rd Annual
Meeting of the Association for Computational Linguis-
tics, pages 320–322, Cambridge, Massachusetts, USA,
1995. Association for Computational Linguistics. doi:
10.3115/981658.981704.
Ricardo Rei, Nuno M. Guerreiro, José Pombal, Daan
van Stigt, Marcos Treviso, Luisa Coheur, José G. C.
de Souza, and André F. T. Martins.
Scaling up
COMETKIWI: Unbabel-IST 2023 Submission for the
Quality Estimation Shared Task, September 2023.
Paul Röttger, Bertie Vidgen, Dong Nguyen, Zeerak
Waseem, Helen Margetts, and Janet Pierrehumbert.
HateCheck: Functional Tests for Hate Speech Detec-
tion Models. In Chengqing Zong, Fei Xia, Wenjie Li,
and Roberto Navigli, editors, Proceedings of the 59th
Annual Meeting of the Association for Computational
Linguistics and the 11th International Joint Conference
on Natural Language Processing (Volume 1: Long Pa-
pers), pages 41–58, Online, August 2021. Association
for Computational Linguistics. doi: 10.18653/v1/2021.
acl-long.4.
Victor Sanh, Lysandre Debut, Julien Chaumond, and
Thomas Wolf. DistilBERT, a distilled version of BERT:
Smaller, faster, cheaper and lighter, March 2020.
Sugan Sirihattasak, Mamoru Komachi, and H. Ishikawa.
Annotation and Classification of Toxicity for Thai Twit-
ter. In Proceedings of TA-COS 2018 – 2nd Workshop
on Text Analytics for Cybersecurity and Online Safety,
2018.
Jai Suphavadeeprasit, Teknium, Chen Guang, Shannon
Sands, and rparikh007. Minos classifier, 2025.
Xiaojun Wan. Co-training for cross-lingual sentiment
classification. In Proceedings of the Joint Conference
of the 47th Annual Meeting of the ACL and the 4th
International Joint Conference on Natural Language
Processing, pages 235–243, Suntec, Singapore, 2009.
Association for Computational Linguistics.
Zeerak Waseem, Thomas Davidson, Dana Warmsley, and
Ingmar Weber. Understanding Abuse: A Typology
of Abusive Language Detection Subtasks. In Zeerak
Waseem, Wendy Hui Kyong Chung, Dirk Hovy, and
Joel Tetreault, editors, Proceedings of the First Work-
shop on Abusive Language Online, pages 78–84, Vancou-
ver, BC, Canada, August 2017. Association for Com-
putational Linguistics. doi: 10.18653/v1/W17-3012.
Michael Wiegand, Melanie Siegel, and Josef Ruppen-
hofer. Overview of the GermEval 2018 Shared Task
on the Identification of Offensive Language. Techni-
cal report, Verlag der Österreichischen Akademie der
Wissenschaften, 2018. https://epub.oeaw.ac.at?arp=
0x003a10d2.
13

--- Page 14 ---

A
Additional methods
A.1
Toxicity classifier selection
We evaluate on a sample of toxicity classifiers that are
publicly-available on Hugging Face. We reviewed clas-
sifiers that matched the search terms “toxic” and “tox-
icity”, selecting those that supported either English
or one or more of the 17 languages analyzed. Clas-
sifiers were limited to those that were permissively-
licensed, with clear data provenance (to allow for
distinguishing between ID and OOD performance),
and substantial community engagement (as measured
by downloads and likes). See Table 2 for all classifiers
evaluated.
A.2
MT finetuning an LLM
We used Llama 3.1 8b Instruct as our baseline model
and finetuned it for 5 epochs with the MT split
from Towerblocks 0.2, a multi-task, multilingual SFT
dataset. We employed the AdamW optimizer with a
learning rate initialized to 1 × 10−6, β1 and β2 coeffi-
cients set to 0.9 and 0.95 respectively, and a weight
decay of 0.1. We used a cosine annealing learning
rate scheduler configured with a final learning rate
scaled to 0.2 times the initial rate and a total of 1,000
warmup steps.
B
Additional results
In Table S1 we present the detailed results behind
Figures 2 and 3, showing the performance of the
best-possible translate-classify, classify (OOD),
and classify (ID) pipelines over all languages. In
Tables S2 to S4 we present the corresponding best-
performing translation system and classifier combina-
tions for translate-classify, classify (OOD), and
classify (ID) respectively.
In Figure S1, we present a version of Figure 2 but
reducing one degree of freedom: rather than choosing
the best-possible combination of translation system
and classifier, here we choose the best possible
translation system though use a fixed classifier,
distilbert-base-multilingual-cased-toxicity.
In this setting, translate-classify still outperforms
across 12 of 16 languages.
14

--- Page 15 ---

AUC
Language
ID
OOD
Translated
ar
-
0.92
0.89
he
-
0.44
0.44
hi
-
0.46
0.44
kn
-
0.42
0.45
ml
-
0.38
0.45
pt
-
0.69
0.79
ta
-
0.42
0.44
te
-
0.43
0.49
th
-
0.57
0.67
uk
-
0.64
0.85
am
0.88
-
0.99
de
0.81
0.67
0.82
es
0.92
0.88
0.91
fr
0.88
0.79
0.88
it
0.88
0.78
0.88
ru
0.97
0.81
0.90
tr
0.94
0.75
0.96
Table S1 Best possible performance over all languages. Where a finetuned classifier isn’t available, translation-based
pipelines often outperform.
uk
tr
ml
de
pt
te
it
ru
fr
kn
th
ta
he
es
hi
ar
0.3
1.0
AUC
translate-classify
classify (OOD)
Fig.
S1
Translation-based
toxicity
detection
pipelines
with
a
fixed
English-supporting
classifier,
distilbert-base-multilingual-cased-toxicity, outperform off-the-shelf pipelines across 12 out of 16 evalu-
ated languages.
Language
Classifier
AUC
am
textdetox/xlmr-large-toxicity-classifier
0.88
de
ml6team/distilbert-base-german-cased-toxic-comments
0.81
es
unitary/multilingual-toxic-xlm-roberta
0.92
fr
unitary/multilingual-toxic-xlm-roberta
0.88
it
unitary/multilingual-toxic-xlm-roberta
0.88
ru
s-nlp/russian_toxicity_classifier
0.97
tr
unitary/multilingual-toxic-xlm-roberta
0.94
Table S2 Best-performing ID pipeline per language.
15

--- Page 16 ---

Language
Classifier
AUC
ar
textdetox/xlmr-large-toxicity-classifier
0.92
de
citizenlab/distilbert-base-multilingual-cased-toxicity
0.67
es
textdetox/xlmr-large-toxicity-classifier
0.88
fr
citizenlab/distilbert-base-multilingual-cased-toxicity
0.79
he
citizenlab/distilbert-base-multilingual-cased-toxicity
0.44
hi
citizenlab/distilbert-base-multilingual-cased-toxicity
0.46
it
citizenlab/distilbert-base-multilingual-cased-toxicity
0.78
kn
citizenlab/distilbert-base-multilingual-cased-toxicity
0.42
ml
citizenlab/distilbert-base-multilingual-cased-toxicity
0.38
pt
unitary/multilingual-toxic-xlm-roberta
0.69
ru
citizenlab/distilbert-base-multilingual-cased-toxicity
0.81
ta
citizenlab/distilbert-base-multilingual-cased-toxicity
0.42
te
citizenlab/distilbert-base-multilingual-cased-toxicity
0.43
th
citizenlab/distilbert-base-multilingual-cased-toxicity
0.57
tr
citizenlab/distilbert-base-multilingual-cased-toxicity
0.75
uk
citizenlab/distilbert-base-multilingual-cased-toxicity
0.64
Table S3 Best-performing OOD pipeline per language.
Language
Translation system
Classifier
AUC
am
Llama 3.1 8B Instruct
unitary/toxic-bert
0.99
ar
GPT-4o
unitary/toxic-bert
0.89
de
GPT-4o
unitary/multilingual-toxic-xlm-roberta
0.82
es
GPT-4o
unitary/toxic-bert
0.91
fr
GPT-4o
unitary/toxic-bert
0.88
he
Llama 3.1 8B TowerBlocks
citizenlab/distilbert-base-multilingual-cased-toxicity
0.44
hi
Llama 3.1 8B Instruct
citizenlab/distilbert-base-multilingual-cased-toxicity
0.44
it
GPT-4o
unitary/toxic-bert
0.88
kn
Llama 3.1 8B Instruct
citizenlab/distilbert-base-multilingual-cased-toxicity
0.45
ml
Llama 3.1 8B Instruct
citizenlab/distilbert-base-multilingual-cased-toxicity
0.45
pt
GPT-4o
unitary/toxic-bert
0.79
ru
GPT-4o
unitary/multilingual-toxic-xlm-roberta
0.90
ta
Llama 3.1 8B Instruct
citizenlab/distilbert-base-multilingual-cased-toxicity
0.44
te
Llama 3.1 8B Instruct
citizenlab/distilbert-base-multilingual-cased-toxicity
0.49
th
GPT-4o
textdetox/xlmr-large-toxicity-classifier
0.67
tr
Llama 3.1 8B TowerBlocks
unitary/toxic-bert
0.96
uk
GPT-4o
unitary/multilingual-toxic-xlm-roberta
0.85
Table S4 Best-performing translated pipeline per language.
16

```
