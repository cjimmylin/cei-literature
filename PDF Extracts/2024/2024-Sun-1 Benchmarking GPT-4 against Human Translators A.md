---
title: "2024-Sun-1 Benchmarking GPT-4 against Human Translators A - PDF Extract"
source_pdf: "2024-Sun-1 Benchmarking GPT-4 against Human Translators A.pdf"
pages: 14
extracted_at: "2026-02-13T13:57:12.230443"
---

# PDF Extract: 2024-Sun-1 Benchmarking GPT-4 against Human Translators A

**Source PDF:** 2024-Sun-1 Benchmarking GPT-4 against Human Translators A.pdf
**Total Pages:** 14

---

## Content

```
--- Page 1 ---

1
Benchmarking GPT-4 against Human Translators: A
Comprehensive Evaluation Across Languages,
Domains, and Expertise Levels
Jianhao Yan, Pingchuan Yan, Yulong Chen, Jing Li, Xianchao Zhu, and Yue Zhang
Abstract—This study presents a comprehensive evaluation of
GPT-4’s translation capabilities compared to human translators
of varying expertise levels. Through systematic human evaluation
using the MQM schema, we assess translations across three
language pairs (Chinese←→English, Russian←→English, and
Chinese←→Hindi) and three domains (News, Technology, and
Biomedical). Our findings reveal that GPT-4 achieves perfor-
mance comparable to junior-level translators in terms of total
errors, while still lagging behind senior translators. Unlike
traditional Neural Machine Translation systems, which show
significant performance degradation in resource-poor language
directions, GPT-4 maintains consistent translation quality across
all evaluated language pairs. Through qualitative analysis, we
identify distinctive patterns in translation approaches: GPT-
4 tends toward overly literal translations and exhibits lexical
inconsistency, while human translators sometimes over-interpret
context and introduce hallucinations. This study represents the
first systematic comparison between LLM and human translators
across different proficiency levels, providing valuable insights into
the current capabilities and limitations of LLM-based translation
systems.
Index Terms—Large language models, Machine translation,
GPT-4, Human evaluation.
I. INTRODUCTION
R
ECENT studies show that LLMs can serve as a strong
translation system and a good substitute for NMT mod-
els [1, 2, 3, 4, 5, 6, 7]. For example, [1] and [2] find that GPT-4
can outperform commercial machine translation systems using
both automatic and human evaluation. Such impressive results
have fostered a wide range of applications, such as the use of
GPT-4 for literary translation [8], poetry translation [9] and
cross-lingual summarization [10].
With the advance of LLM translation, traditional evaluation
metrics such as BLEU are inadequate for evaluating their
quality [11, 12]. While the research community has taken
model-based approaches in recent work [13, 14], these metrics
can suffer from model biases and distribution shifts. We take
Jianhao Yan is with Zhejiang University, Zhejiang, P.R. China, and also
with the School of Engineering, Westlake University, Zhejiang, P.R. China
(e-mail: elliottyan37@gmail.com).
Pingchuan Yan is with the University College London, London, UK (e-mail:
ypc1956280693@gmail.com).
Yulong Chen is with the Department of Computer Science and Technology,
University of Cambridge, Cambridge, UK.
Jing Li and Xianchao Zhu are with the LanBridge Group, Sichuan, P.R.
China
Yue Zhang is with the School of Engineering, Westlake University, Zhejiang,
P.R. China, and also with Institute of Advanced Technology, Westlake Institute
for Advanced Study (e-mail: yue.zhang@wias.org.cn).
Corresponding author: Yue Zhang.
a different perspective by benchmarking them against human
translators using systematic human evaluation. Our goal is to
understand LLM translators by putting them into the translation
industry, hiring professionals to evaluate their translation quality
against the translation quality of different levels of human
translators, and gaining insight into any systematic differences
between LLM translations and human translations [1]. Such
evaluation can complement existing studies and give a more
comprehensive understanding of LLM translation quality.
To determine where LLMs fall within the spectrum of
human translation proficiency, we take the current representative
LLM, i.e., GPT-4, comparing it against human translators with
different expertise, ranging from novice translators to seasoned
professionals. A preliminary study comparing human transla-
tions against GPT-4 translations shows that even experts cannot
reach a high consensus on which translation is better, despite
that they tend to give higher scores to human translations.
The results indicate that LLMs do generate translations that
approach the human level, and there can be potential subtle
differences between LLMs and human translators, which are
worth a more in-depth study.
Given these findings, we take a finer-grained evaluation
across different languages and domains, so that translation
quality can be better calibrated and systematic differences
can be measured. Our evaluation covers three language pairs
from resource-rich to resource-poor, i.e., Chinese↔English,
Russian↔English, and Chinese↔Hindi, and three domains,
i.e., News, Technology, and Biomedicine. Given a source
sentence, we ask junior, medium, senior human translators
and two machine translators, i.e., GPT-4 and Seamless, a
traditional NMT translator, to generate the corresponding
translation in the target language. Then we hire independent
expert annotators to label the errors in the target sentence under
the MQM schema [15]. Results show that while traditional
NMT systems significantly underperform, GPT-4 reaches a
comparable performance to junior/medium-level translators in
the perspective of total errors made, yet lags behind senior
ones with a considerable gap. GPT-4 represents a significant
milestone in neural machine translation, establishing a baseline
for legitimate comparative analysis with human translation
performance.
Further language-specific results demonstrate that GPT-4
mitigates traditional machine translators’ drawback of signif-
icant performance gap from resource-high to resource-low
directions. Our traditional MT translator Seamless can be a
reliable translator for English↔Russian, but shows poor quality
arXiv:2411.13775v1  [cs.CL]  21 Nov 2024

--- Page 2 ---

2
for other language pairs. In contrast, GPT-4 demonstrates
consistent performance across all evaluated language directions,
achieving quality levels on par with junior to mid-level human
translators. Across various domains, similar comparisons of
the GPT-4 translator against human translators are observed.
Interestingly, each translator has its own drawbacks, while the
GPT-4 translator is weak in Grammar and Named Entity, it
does not suffer from human hallucination and fatigue. More
specifically, we observe that GPT-4 exhibits two primary
limitations: adherence to overly literal translations and lexical
inconsistency. Conversely, human translators tend to over-
interpret certain contextual cues and introduce hallucinations.
To our knowledge, we are the first to evaluate LLMs against
various levels of professional human translators and analyze the
systematic differences between LLMs and human translators. 1
II. RELATED WORK
a) Benchmarking LLMs: Previous studies have bench-
marked LLMs on various NLP tasks. [16] benchmark several
LLMs on Chinese text, evaluating their Chinese ability. [17]
assess LLMs through Question Answering (QA), MMLU [18],
and other metrics. From these tests, LLMs with larger scales are
generally proved to be more accurate except for certain tasks.
[19] demonstrates that LLMs perform well in long-context
understanding and are more capable with Out-of-Distribution,
which means LLMs have a certain degree of generalization
ability.
Further to the MT field, [20] find that GPT-4 performed
competitively with other SotA translation products. [2] fur-
ther investigated the capability of GPT-4 in document-level
translation, the results show that GPT-4 performs better than
commercial translation products and document NMT methods.
Compared to them, our work empirically shows that GPT-4 is
comparable to junior human translators.
b) LLMs as Human Experts: Due to the great capacities
of GPT-4 over traditional NLP models, researchers have
investigated and compared the performance of GPT-4 as
human experts in multiple NLP tasks. [21] highlight that
GPT-4 and GPT-4-turbo show top performance on a Chinese
financial language understanding task. [22] find the LLMs
can be beneficial to biomedical NLP tasks. [23] compare
GPT models with several summarization models and humans,
and find that GPT can generate summaries preferred by
humans. In AI for education area, [24] show GPT-4’s can
provide teaching feedback for students. [25] find that GPT-4
shows close performance compared with human participants
in coordination games. [26] show that GPT-4 is comparable
to humans on technical translation tasks. [27] find that GPT-4
can outperform human experts on linguistic pragmatic tasks. In
clinical diagnostics, [28] find that GPT-4 can give comparable
performance to humans, and GPT-4v (vision version) can even
outperform human experts.
c) Human Evaluation for MT: [29] first propose Direct
Assessment (DA), which uses a continuous score from 0 to 100
to represent the quality of a hypothesis. DA has been adopted
1We release our code and data at https://github.com/ElliottYan/GPT_versus_
mt_experts.
in WMT translation tasks for the past few years [30, 31, 32].
MQM [33], the annotation used in this paper, is another widely
used annotation scheme [34, 35]. It requires the annotators to
annotate the error span for each hypothesis and is shown to be
more accurate and reliable than DA [15]. Thus, it is utilized in
the metrics tasks of 2022 and 2023 WMT challenges [36, 37].
d) Human Parity: The human parity for machine trans-
lation systems is first claimed by [38], which describes a
comparable performance on the WMT 2017 news translation
task from Chinese to English when compared to professional
human translations. However, this claim is challenged by
the following research, raising concerns about the limited
scope of human parity. These limitations include the expertise
of human evaluators [39], the origin and quality of source
sentences [40, 41], the limited scenario of comparison [42] and
difficulty of translation [43], indicating significant gaps between
NMT models and the professional translators. In this work, we
evaluate whether the SOTA LLM GPT-4 performs comparable
to professional translators and what differs between human
translators and LLMs. With the above lessons in mind, we
address these limitations by hiring expert annotators, avoiding
target-origin source text, manually evaluating source sentences,
and covering high-resource to low-resource language pairs and
various domains.
III. PRELIMINARY STUDY
We aim to first compare GPT-4 translations with human
translations qualitatively, in a coarse manner. We hire expert
annotators from the Lan-Bridge Group2, who are native Chinese
speakers and dedicated to Chinese-English translation for over
5 years. Our comparison is simple and direct. We sample
human-translated texts and prompt GPT-4 to translate the same
source sentence. Then, we ask expert annotators to determine
which translation is better.
Particularly, to have a quick overview of the qualities
of human translations against GPT-4 translations, we first
utilize COMET-QE3 to score our in-house Chinese to English
human-translated documents, and select two documents with
the highest score and the lowest score. Note that our in-
house translated documents are all translated by professional
translators. In this way, we gather 40 pairs of translations
from professional translators and GPT-4, respectively. Recent
findings [15] have demonstrated that crowd-sourced human
ratings are less reliable for high-quality MT evaluation. Thus,
we hire six expert annotators to compare the two translations
and select the better translations they find. We randomly shuffle
the GPT-4 and human translations to prevent annotators from
identifying GPT-4.
The average win rate of GPT is 15.5/40 (36.25%), which
indicates a clear win for human translators. However, when
delving deeper, we find that the expert annotators have a
low ratio of agreement with each other. In Table I, the inter-
agreement ratio between most annotators is around 60% (the
baseline is 50%). A significance test shows that only annotator
B finds human translation significantly better than GPT’s
2https://www.lan-bridge.co.uk/
3Unbabel/wmt23-cometkiwi-da-xl

--- Page 3 ---

3
Annotators
A
B
C
D
E
F
A
100.0
57.5
65.0
65.0
62.5
67.5
B
-
100.0
52.5
52.5
50.0
50.0
C
-
-
100.0
65.0
82.5
67.5
D
-
-
-
100.0
57.5
62.5
E
-
-
-
-
100.0
70.0
F
-
-
-
-
-
100.0
p-value
1.000
0.038
0.268
0.081
0.154
0.875
TABLE I: Ratio(%) of agreed winner across expert annotators
and significance p-value for binomial test. P-value < 0.05
denotes a significant difference between GPT-4 and Human.
translation, while the other annotators have high p-values.
These results indicate that even expert annotators find it difficult
to agree on which translation is better, and GPT-generated
translations might have different advantages against human-
generated ones. We are therefore motivated to conduct a finer-
grained and comprehensive evaluation to reveal the systematic
difference between GPT-4 and human translations.
IV. MAIN EXPERIMENTAL SETUP
We conduct a comprehensive and fine-grained evaluation
of GPT-4 against professional human translators. Specifically,
we employed the widely recognized Multidimensional Quality
Metrics (MQM) framework [33] and compared human transla-
tors with varying levels of expertise to GPT-4. Our evaluation
spans multiple languages and domains, aiming to furnish broad
insights into these comparisons.
A. Data Collection
We strategically collect multilingual and multi-domain source
sentences to evaluate translation across diverse resource levels.
Based on GPT-3 corpus reports, we select four languages:
English (dominant in most models), Russian (0.1884% words,
8th), Chinese (0.099% words, 16th), and Hindi (0.00483%
words, 41st). This choice allows us to assess translations from
resource-high to resource-low scenarios. English and Russian,
both Indo-European, represent resource-high directions, while
English and Chinese, from different language families, serve as
resource-medium directions. Recognizing the scarcity of expert
translators in low-resource languages, we use Chinese ↔Hindi
as our resource-low directions. In summary, we evaluate six
crucial directions: English ↔Chinese, English ↔Russian,
and English ↔Hindi. This selection enables us to assess
bidirectional translation performance across varied resource
levels, providing valuable insights into current capability of
the GPT4 translator against human translators.
For general domain Chinese⇔English and English⇔Russian
translation, we sample source sentences from the test sets of
WMT2023 and WMT2022, respectively. For Chinese⇔Hindi,
we extract source news text from public websites. For
multi-domain evaluation data, we choose two domains, i.e.,
biomedicine and technology, evaluating Chinese to English
translation. The source sentences are extracted news texts from
public websites. We ensure that all sources are source language
origin to avoid the effect of translationese. We manually
evaluate all source sentences for these tasks to ensure that
the source sentences are not too easy or too short. Finally, each
task contains 200 sentences, making our evaluation a total of
1600 sentences.
B. Human and Machine Translators
We ask different human translators from the same company
as Section III to translate our source sentences into the target
language. Translators are of three different levels of expertise,
categorized into junior-level, medium-level, and senior-level
translators. The level of expertise is ranked by in-house criteria
covering the translators’ educational background, translation
experience, and practical proficiency. For instance, a junior
translator could be a graduate student majoring in target
languages and having one or two years of experience in
the translation industry. A medium translator could be a
translator who has 3-5 years of experience or is a native
speaker of the target language. To be classified as a senior-level
translator, an individual must possess a minimum of ten years
of translation experience, demonstrate exceptional proficiency
by achieving a score of 99% on quarterly assessments, and
hold the distinguished CATTI++ translation certification. This
categorization follows the tradition of the human translation
industry.
For all directions except Zh-Hi and Hi-Zh, we collect three
human translation results from each level of expertise. For
Zh-Hi and Hi-Zh, we only have medium-level and senior-level
translators due to the scarcity of translators.
In practice, we find that current human translators also
heavily rely on GPTs or machine translators as assistance. Thus,
to enable a fair comparison, we prohibit human translators from
using machine translation or GPTs as assistance.
We use gpt-4-1106-preview, the current state-of-the-
art large language model released by OpenAI and Seamless
M4T [44] as the representative of traditional machine trans-
lations to complement our experiments. We directly prompt
GPT-4 to obtain the translation, as it is the most common
practice for normal users, the easiest to reproduce, and to
avoid confusion by various techniques.
For GPT-4, we use greedy search for decoding, to ensure
the reproducibility of the results. For SeamlessM4T, we use
the 2.3B version of seamlessM4T_v2_large and adopt
beam search with beam size 5.
C. Prompt Search
Previous study [45, 46] shows that different prompts with
LLMs can result in distinctive performance. Thus, we collect
three candidate prompts used in previous research [1, 47] and
use COMET-QE [48] to select the best prompt to make the
best use of GPT-4, as shown in Table III. In particular, we
use these three prompts to prompt GPT-4 to translate 100
source sentences in our Chinese-to-English test set and adopt
COMET-QE to evaluate the quality of translations. We find
that the third prompt yields the best performance, and hence
we adopt this prompt for all following experiments.

--- Page 4 ---

4
Type
Error Name
Explanations
Examples
Accuracy
Mistranslation
Translation does not
accurately represent the
source.
[EN] It has to be done by the book.
[FR]
Il
doit
être
fait
[par
le
livre]MISTRANSLATION
Addition
Information not present in
the source.
[EN] That way you can be sure that you
were the one who made the changes.
[ES] Así puedes estar seguro de que
fuiste tú quien hizo [todos]ADDITION
los cambios.
MT Hallucination
Information that has
nothing related to source;
or gibberish; or repeats
[EN] You can send us a follow-up email
at this address [EMAIL].
[ES] Hágame saber si tiene alguna otra
pregunta]MT HALLUCINATION.
Omission
Missing content from the
source.
[EN] We do not have much information
on this.
[FR] Nous ne disposons pas []OMIS-
SION beaucoup d’informations à ce
sujet.
Untranslated
Not translated.
[EN] How To Make Pizza Dough
[FR]
Comment
faire
de
[Pizza
Dough]UNTRANSLATED
Incorrect NE and Term
Incorrect usage of NE and
Terminology.
[EN] Dear Wiley,
[IT] Gentile [Wilar]Incorrect NE,
Fluency
Grammar
Problems with grammar of
target language.
[EN] I understand that you want to
check in online.
[CS]
chàpu,
ze
se
chcete
[odbavení]GRAMMAR online.
Punctuation
Incorrect punctuation (for
locale or style)
[EN] Original copy of the Proof of
Purchase or Invoice (not a screenshot):
[PT] C’opia original do comprovante
de compra ou nota fiscal (não uma
captura de tela)[.]PUNCTUATION
Spelling
Incorrect spelling or
capitalization.
[EN] [...], but we will seek assistance
from higher support and see what we
can do regarding this issue.
[IT]
[...],
ma
chiederò
comunque
aiuto ai responsabili dell’assistenza
per capire che cosa [Zi]SPELLING
può fare per quanto riguarda questo
problema.
Register
Incorrect grammatical
register (e.g.,
inappropriately informal
pronouns).
[EN] Wishing you a great day ahead.
[DE] Ich wünsche [Ihnen]REGISTER
einen schönen Tag.
Inconsistent Style
Internal inconsistency (
not related to terminology
)
[EN] Please click on this link. [...] This
link will expire in 24 hours.
[NN]
Klikk
på
denne
[lenken].[...]Denne
[linken]INCONSISTENCY
utloper
om 24 timer.
Unnatural Flow
Translations that are
too literal or sound
unnatural.
[EN] Zebras are ideal for animal match-
ing.
[DE] [Zebras sind ideal, um bestimmte
Tiere zu finden]UNNATURAL FLOW.
Other
Non-translation
-
-
TABLE II: Error category and explanations. We mainly follow the guidelines from Unbabel, and merge some errors to reduce
the efforts for annotators to understand the annotation system.

--- Page 5 ---

5
Prompt
COMET
Please translate the following sentence from Chinese into English. Your language and
style should align with the language conventions of a native speaker. \n{SOURCE}\n
0.775
You are an expert translator for translating Chinese to English. Your language and
style should align with the language conventions of a native speaker. \n[Chinese]:
{SOURCE}\n[English]:
0.755
Please provide the English translation for these sentences. Your language and style
should align with the language conventions of a native speaker. \n{SOURCE}\n
0.780
TABLE III: Taking Chinese to English as an example, our three prompts and corresponding scores with COMET-QE. {SOURCE}
represents the source sentence to be translated.
Task
Cohen Kappa(Segment)
Krippendorffs(Span)
Reference, Re-Annotated by [15]
WMT 2020 En-De
0.208
0.456
WMT 2021 En-De
0.230
0.501
Ours
General Zh-En
0.257
0.436
General En-Zh
0.544
0.579
General En-Ru
0.461
0.566
General Ru-En
0.341
0.875
General Zh-Hi
0.256
0.443
General Hi-Zh
0.234
0.495
Technology Zh-En
0.306
0.581
Biomedicine Zh-En
0.373
0.616
Average
0.321
0.555
TABLE IV: Cohen Kappa (segment-level) and Krippendorffs’
Alpha (span-level) agreement of our annotations.
D. Annotation Protocol
To evaluate the results of candidates’ systems, we hire experts
to annotate the errors of translations blindly. The annotation
platform is Doccano [49], and the error tags are made according
to MQM standards. MQM requires the annotators to annotate
the span of errors in each hypothesis. All hypotheses of the
same source sentence are shown to the annotator together to
help decide which is better. We have 13 error categories and
two severities, as shown in Table II. Our categorization for
errors mostly follows Unbabel’s practice 4 and we focus on
most common error types. Each tag has subtags with two
severities, i.e., Minor or Major. A screenshot of the annotation
system is given in Figure 4.
For each task, we first ask the two expert annotators to
carefully read our manual and conduct a training round on the
first 10 groups of translations. Then, we manually check these
annotations to provide feedback and ask the two annotators to
check their disagreements and revise their results. After two
rounds of such training processes, we ask the annotators to
finish the remaining sentences without knowing each other’s
results.
After the first round of annotation, we conduct a second
round to further refine the evaluation results. In particular, we
hire another two experts for each task and show them the
previous annotation results. They are asked to approve and
make necessary modifications to previous round annotations.
4https://help.unbabel.com/hc/en-us/articles/
6444304419479-Annotation-Guidelines-Typology-3-0
E. Inter-Annotator Agreement
Error annotation with MQM is challenging, and previous
work demonstrates that the agreement scores between MQM
annotations are relatively low [33]. Reasons for this could
be disagreement on precise spans and ambiguous error cat-
egorization [33]. Despite the low agreement scores, MQM
is more reliable than other evaluation protocols like Direct
Assessment [15].
To compute inter-annotator agreement for MQM, we employ
segment-level Cohen’s Kappa [50] and span-level Krippen-
dorff’s alpha [51]. For reference, we calculate the agreement
on the annotated results of the 2020 and 2021 WMT English-to-
German tasks by [15]. Our IAA results are shown in Table IV.
Thanks to our two-round annotation process, our IAA scores
show a favorable agreement, indicating a good annotation
quality.
V. MAIN RESULTS
A. Overall Results
The overall results are shown in Table V, where each
row represents a translator and each column represents the
error score of each type. We compare the traditional machine
translator, i.e., Seamless, LLM translator, i.e., GPT-4, and
different levels of human translators.
a) Error Severity: The left part of Table V presents the
averaged number of errors of different systems and translators.
We normalize each error by the ratio of its span length against
the length of the candidate translation. Our results demonstrate
that GPT-4 represents a significant milestone in neural machine
translation, establishing a baseline for legitimate comparative
analysis with human translation performance, while previous
models demonstrably lag behind human capabilities. Specif-
ically, compared to our MT baseline (seamless), GPT-4 has
significantly fewer errors, i.e., 29.52 vs 20.43 minor errors and
17.35 vs 3.71 major errors. GPT4 translator is comparable with
junior/medium-level human translators, producing 17.35/3.71
minor/major errors compared to 18.19/3.27 for junior-level
and 20.19/3.30 for medium-level translators. However, GPT4
lags behind senior translators by a significant margin, i.e., 3.71
vs 1.83 major errors, indicating machine translation is yet a
solved problem. To our knowledge, this is the first report on
GPT-4 as a translator against various expertise levels of human
translators.
b) Error Categories: The right part of Table V shows
our overall results for two categories of MQM errors, namely
Accuracy and Fluency [15]. We merge different error severity

--- Page 6 ---

6
Mistranslation
Punctuation
Incorrect NE
Unnatural Flow
Omission
Mistranslation
Unnatural Flow
Incorrect NE
Grammar
Punctuation
Mistranslation
Unnatural Flow
Grammar
Incorrect NE
Punctuation
Mistranslation
Unnatural Flow
Incorrect NE
Omission
Grammar
Mistranslation
Unnatural Flow
Addition
Punctuation
Grammar
0
20
40
60
80
Number of Errors
Top5 Error Categories
seamless
gpt4
junior
medium
senior
Fig. 1: Top 5 categories of errors made by each translator.
Severity
Error Type
Translator
Minor
Major
Accuracy
Fluency
Seamless
29.52
17.35
28.25
17.37
Machine
GPT4
20.43
3.71
11.12
12.95
Junior
18.19
3.27
8.55
12.74
Medium
20.19
3.30
12.58
10.66
Human
Senior
12.04
1.83
7.93
5.93
TABLE V: Overall Results: Average score of errors by different
translators.
by assigning them weights, where a minor error weights
1 and a major error weights 3, as done in [15]. GPT-4’s
translation demonstrates good accuracy but worse language
usage when compared with expert translators. In particular,
GPT-4 makes comparable errors in the accuracy of translations
with junior/medium human translators (11.12 vs 8.55/12.58),
while it makes 12.95 fluency errors, weaker than all human
translators. We also find the seniority of human translators
mainly manifests progressively refined language usage, i.e.,
fluency errors from 12.74 to 5.93, while accuracy errors show
fluctuations across seniority levels.
We further investigate errors made by each translator. Figure
1 shows the top 5 categories of errors made by different
systems. ‘Mistranslation’ is the most frequent error made by all
systems. Improving much over the seamless baseline, GPT-4
makes comparable numbers of ‘Mistranslation’ with junior and
medium human translators. ‘Unnatural Flow’ is among the most
frequent errors for all translators. Seamless, GPT-4, and junior
translators have similar levels of ‘Unnatural Flow’, indicating
possible issues of literal translation and not following language
conventions. In contrast, medium and senior translators are
annotated with significantly fewer ‘Unnatural Flow’ errors.
GPT-4 makes much fewer ‘Incorrect Named Entity(NE)’
errors compared to Seamless, which can be because of the huge
knowledge acquired in the pre-training stage. However, it still
has a gap compared to human translators. Finally, we notice that
GPT-4 does not have Omission or Addition problems in its top-
5 errors, whereas even senior translators have Addition errors.
This can be because of the tendency for machine translators
to use literal translation. We will discuss this further in the
following sections.
B. Language-Specific Results
We delve deeper into the detailed results for different
languages, domains, and cases. The language-specific results
are shown in Table VI, which provides our language-specific
results on Accuracy and Fluency, as in the previous section,
average to and from directions of a language pair. We give
language-specific discussions below, with more detailed metrics
being plotted in Figure 2 .
a) English↔Russian: For English-Russian translation,
we find that the MT baseline is comparable with GPT-4, with
slightly better accuracy (14.79 vs 15.82) and slightly worse
fluency (14.60 vs 14.11). More importantly, when comparing
these two machine translators to human translators, we observe
comparable performance. Seamless has the lowest level of
accuracy errors among all translators, and GPT-4 reaches
the same level of fluency as senior translators, indicating
both machine translators are reliable substitutions of human
translators in resource-high directions like English↔Russian.
In Figure 2(a), we can find that each different human
translator has their strengths and weaknesses, performing well

--- Page 7 ---

7
Translator
En↔Ru
Zh↔En
Zh↔Hi
Accuracy
Fluency
Accuracy
Fluency
Accuracy
Fluency
Machine
Seamless
14.79
14.60
129.19
55.46
202.92
17.60
GPT4
15.82
14.11
29.57
34.98
44.36
22.83
Human
Junior
8.52
17.14
35.99
34.18
-
-
Medium
15.09
14.79
37.59
23.04
59.03
22.83
Senior
15.81
14.16
12.40
7.60
45.39
15.19
TABLE VI: Language specific results.
Mistranslation(13)
Addition(3)
Omission(1)
Incorrect NE(2)
Grammar(5)
Punctuation(2)
Spelling(2)
Register(1)
Inconsistent Style(4)
Unnatural Flow(9)
0.0
0.2
0.4
0.6
0.8
1.0
seamless
gpt4
junior
medium
senior
(a) English↔Russian
Mistranslation(85)
Addition(2)
Omission(3)
Incorrect NE(21)
Grammar(10)
Punctuation(8)
Spelling(1)
Register(4)
Inconsistent Style(1)
Unnatural Flow(35)
0.0
0.2
0.4
0.6
0.8
1.0
seamless
gpt4
junior
medium
senior
(b) Chinese↔English
Mistranslation(175)
Addition(13)
Omission(13)
Incorrect NE(9)
Grammar(6)
Punctuation(4)
Spelling(1)
Register(4)
Inconsistent Style(2)
Unnatural Flow(18)
0.0 0.2 0.4 0.6 0.8 1.0
seamless
gpt4
medium
senior
(c) Chinese↔Hindi
Fig. 2: Detailed errors of categories for each domain. Higher values indicate more errors and the number after each error type
is the maximum number of that error.
or poorly in certain error categories. For instance, Seamless
has more errors in Grammar, Punctuation, and Spelling; but
fewer errors in other aspects. GPT-4 is more balanced and
similar to human translators in terms of errors made.
b) English↔Chinese: Here, we observe a distinct pattern
shift. Seamless degrades significantly, scoring 129.19 in Ac-
curacy and 55.46 in Fluency. This may be due to unbalanced
training data for supervision data. In the meanwhile, GPT-4 is
still comparable to human translators, surpassing junior/medium
translators for Accuracy (29.57 vs 35.99/37.59) for Accuracy,
and performing closely for Fluency (34.98 vs 34.19/34.18).
Senior translators substantially outperform GPT-4, attaining a
score of 12.40/7.60 for Accuracy and Fluency.
From the radar chart (Figure 2(b)), we also notice a
similar trend. Different from the English-Russian translator,
Seamless has more Mistranslation, Incorrect NE, Punctuation,
and Unnatural Flow errors, accounting for its performance drop.
On the other hand, GPT-4 performs well overall, except for
more errors in Incorrect NE, Grammar, and Register compared
with human translators. As in the absence of reference, GPT-4
would translate unfamiliar words directly and literally instead
of seeking online materials or other forms of help like human
translators. For example, when translating the phrase ‘the
Safer Transport Command’, GPT4 translates the phrases to
“更(more)安全(safe)交通(traffic)指挥部(command center)” in
Chinese. It implies ‘a more safe traffic command center’ rather
than capturing the intended meaning of a specialized police
unit focused on transport safety. For other errors, GPT-4 is
among the level of junior/medium translators.
c) Hindi↔Chinese: Compared to the directions discussed
before, the overall number of errors made by all translators is
higher, revealing the difficulty of our resource-low directions.
We also notice the same pattern shift as in Chinese-English
– traditional machine translation is not reliable anymore but
GPT-4 maintains its performance. Specifically, a huge gap
is observed between Seamless and other translators, with an
error score over 200 vs 40-60 for accuracy, indicating an
influence of scarcity of resources. In contrast, GPT-4 attains a
better Accuracy score (44.36 vs 59.03/45.39) compared with
human translators. Its fluency score (22.83) is the same as
medium human translators, and slightly weaker than senior
translators (15.19).
From Figure 2(c), Seamless stands out with significantly
more errors in Mistranslation (175) than all the other translators.
Unlike Seamless, GPT-4 excels in technical aspects like
Spelling and Punctuation as well as maintaining source contents,
demonstrated in Omission and Addition. However, GPT-4
struggles with Incorrect NE and Grammar, as in Chinese-
English.
d) Discussion: Our results here manifest an imbalance
of multilinguality [52]. Our results suggest that GPT-4 is a
reliable translator for all three six evaluated directions, while
traditional machine translators such as Seamless are limited by
the resources of the directions and only reliable in resource-high
directions. For most cases, GPT-4 is comparable/better than
junior/medium-level human translators, especially in Accuracy.
One noticeable drawback of GPT4 across resource-medium
and resource-low directions is the Incorrect NE. In future

--- Page 8 ---

8
Mistranslation(62)
Addition(2)
Omission(2)
Incorrect NE(20)
Grammar(10)
Punctuation(1)
Spelling(1)
Register(3)
Inconsistent Style(1)
Unnatural Flow(15)
0.0
0.2
0.4
0.6
0.8
1.0
seamless
gpt4
junior
medium
senior
(a) News domain.
Mistranslation(48)
Addition(1)
Omission(6)
Incorrect NE(33)
Grammar(20)
Punctuation(2)
Spelling(1)
Register(2)
Inconsistent Style(1)
Unnatural Flow(21)
0.0
0.2
0.4
0.6
0.8
1.0
seamless
gpt4
junior
medium
senior
(b) Technology domain.
Mistranslation(18)
Addition(3)
Omission(1)
Incorrect NE(26)
Grammar(2)
Punctuation(2)
Spelling(1)
Register(5)
Inconsistent Style(1)
Unnatural Flow(18)
0.0
0.2
0.4
0.6
0.8
1.0
seamless
gpt4
junior
medium
senior
(c) Biomedicine domain.
Fig. 3: Detailed errors of categories for each domain. Higher values indicate more errors and the number after each error type
is the maximum number of that error.
Translator
News
Technology
Biomedicine
Accuracy
Fluency
Accuracy
Fluency
Accuracy
Fluency
Machine
Seamless
85.38
26.75
86.58
43.41
51.70
26.36
GPT4
17.62
15.96
36.62
28.97
13.74
11.00
Human
Junior
14.36
9.23
32.42
21.79
10.39
6.47
Medium
13.70
6.00
27.76
24.73
9.35
12.07
Senior
8.61
4.90
10.16
10.25
5.52
3.71
TABLE VII: Domain Specific Results.
directions, we think web-agent could be a promising solution
for resolving this issue. In addition, we would expect GPT4 to
make a substantial number of hallucination errors as reported
in various research of large language models [53]. While,
surprisingly, we notice that in all evaluated directions, GPT4
makes almost zero hallucination errors.
C. Domain-Specific Results
Table VII and Figure 3 present our results for different
domains in Chinese-to-English translation. In addition to the
news domain we evaluated in the previous section, we evaluate
two more domains: technology and biomedicine.
First, in Table VII, there is a huge gap from Seamless to
GPT4 and human translators, consistent with results from the
previous section’s English↔Chinese results. Despite varying
levels of translation difficulty, as indicated by the average
error rates among human translators, GPT-4’s translation
performance is marginally inferior to that of junior and mid-
level translators across all three domains. The gaps are slight
for both metrics, with the notable exception of biomedical
translations where GPT-4 achieves superior fluency scores.
For instance, GPT-4 scores 36.62/28.97 for the Technology
domain, and human translators score [32.42, 10.16]/[24.73,
10.25]. Senior translators outperform GPT-4 by a noticeable
margin in error numbers. These results are consistent with our
previous findings. Interestingly, we find errors made by human
translators are diversified (Figure 3). For instance, we observe
more Unnatural Flow errors in Technology domain. Below we
give more detailed discussion on each domain according to
Figure 3.
a) Technology Domain: For most of the error categories,
GPT-4 reaches the level of junior and medium human transla-
tors. The two exceptions are Incorrect NE and Grammar, similar
to our results above. We find that in Technology domain, there
are lots of sentences with descriptive parallel phrases and in-
domain named entities, which make GPT-4 struggle. Examples
is presented in Section V-D. Furthermore, compared to that
in the News domain, there are more Unnatural Flow errors in
Technology domain for both human and GPT-4 translators. This
is due to that the information-intense and compact language
style of source texts in Technology domain complicate the
translation process.
b) Biomedicine Domain: Unlike in Technology, we notice
no clear disadvantage of Incorrect NE for GPT-4 compared
to human translators. In addition, there are fewer Grammar
errors for Biomedicine domain. Human translators occasionally
demonstrate specific weaknesses. For example, here we find
the senior translator makes more Addition errors. Meanwhile,
our medium translator has more Register and Inconsistent Style
errors. These errors are not systematic; rather, each translator
exhibits its own distinct weaknesses. In GPT-4’s case, the
primary limitations manifest in Named Entity recognition and
grammatical accuracy.
In summary, for our evaluated domains, we show that GPT-4
is a reliable translator as junior/medium human translators,
except for mild Incorrect NE and Grammar issues. The
relative performance comparing with human translators remain

--- Page 9 ---

9
Named-Entity
Source
巨人网络有限公司
GPT-4
Giant Network Group Inc.
Human
Giant Interactive Group Inc.
Unnatural Flow
Source
It’s just a white screen or it times out loading it, or the page becomes unresponsive!
GPT-4
它只是一个白屏，要么是加载时超时，要么页面变得无响应了！
Human
页面要么显示空白，要么加载超时或是无响应。
Consistent Usage
Source
最后再来看下仪表盘和座椅，仪表盘设计可圈可点，设计比较稳重。该车采用了
仿皮座椅，座椅包裹性到位，用料讲究，乘坐舒适。
GPT-4
Finally, let’s take a look at the dashboard and seats. The dashboard design is noteworthy
and quite stable. The car features faux leather seats that are well-contoured, made with
quality materials, and offer a comfortable ride.
Human
Finally, let’s take a look at the dashboard and the seat, the dashboard is designed to be
circular, the design is more stable, the car uses a leather seat, the seat is wrapped in
place, the material is careful, and the ride is comfortable.
Human Hallucination
Source
He has health concerns atm but we also have Daley entering his 2nd year and is a
decent safety net.
GPT-4
他目前有健康问题，但我们还有戴利进入他的第二年，他是一个不错的安全保
障。(literal)
Human
他目前有健康问题。不过，戴利两岁了，是个不错的备选人。
TABLE VIII: Case study. Underline indicates the critical phrases in the source sentence, text in red indicates errors, and text in
blue indicates correct usage.
consistent across domains.
D. Case Study
We also qualitatively understand the difference between the
translations given by GPT-4 and human translators.
a) Literal Translations: Among the error cases, the
typical one is literal translations. Specifically, we find that
GPT-4 sometimes translates with semantically correct, but in-
native and literal translations. This is problematic with named
entities, especially those occurring less frequently. As shown
in Table VIII, when not knowing the correct translation of ‘巨
人(Giant)网络(Network)有限公司(Limited Company)’, GPT-4
translates the term word by word. However, the issue of named
entities occurs less for human translators, partially because they
would google it to find the correct translation. Thus, this issue
might be resolved by incorporating web-search into agent-like
translation [54, 55].
Except for named entities, we notice that the literal transla-
tion causes Unnatural Flows. As shown in Table VIII, when
translating ‘It’s just a white screen’, GPT-4 translates the phrase
to ‘它(it)只是(is just)一个(a)白屏(white screen)’, but human
translator translates this phrase to ‘‘页面显示空白(The page
display is white)’’, which represents a more precise meaning
and follows local conventions.
b) Consistent Word Usage: In the previous section, we
observed that GPT4 sometimes makes more Grammar errors.
By delving into cases, we find that GPT4 occasionally makes
grammar errors when involving consistent usage of words or
phrases. For example in Table VIII, GPT4 makes a faulty
parallelism error, i.e., elements in a series do not match.
In this example, ‘well-contoured’ (adjective), ‘made with
quality materials’ (passive phrase), and ‘offer a comfortable
ride’ (active verb phrase) are not in parallel form. In other
cases, GPT-4 sometimes uses inconsistent pronouns or tenses,
e.g., ‘is’ before and ‘was’ after.
c) Human Hallucination: We find human translators also
have drawbacks compared to the GPT-4 translator. When the
source sentence contains insufficient information to translate,
human translators tend to fill the gap by imagination or
overthinking. An example is given in Table VIII. The translator
incorrectly understands the phrase ‘entering his 2nd year’ as
Daley is a two-year-old baby, but the sentence describes a
2nd-year player for sports. This may be due to daily language
habits, misunderstanding, or not spending sufficient time on
reasoning. The mistakes can be inevitable given the nature of
a professional translator’s work and could be related to the
hallucination [53] of LLMs. GPT-4’s literal translation helps
in this, as it keeps faithful to the source sentence. This also
aligns with our findings in Section V-A0b that GPT-4 has fewer
Additions or Omissions.
VI. CONCLUSION
We comprehensively evaluated the translation quality of GPT-
4 against human translators of varying expertise levels across
multiple language pairs and domains, finding that the LLM per-
forms significantly better than the Seamless, a traditional NMT
system, and comparably to junior/medium translators in terms
of total errors made. However, LLMs still lag behind senior
translators. We also notice that GPT-4’s translation capability
weakens from resource-rich to resource-poor language pairs.
Qualitative analysis revealed that GPT-4 produces more literal
translations and consistent word usage than human translators
but suffers less from imagined information. The results above
demonstrate that in all directions, LLMs have the potential
to replace human translators, especially junior and medium
ones feasibly. To our knowledge, we are the first to report
evaluation of machine translation systems by ranking them
among professional human translators according to industry-
level metrics.

--- Page 10 ---

10
REFERENCES
[1] W. Jiao, W. Wang, J. tse Huang, X. Wang, S. Shi,
and
Z.
Tu,
“Is
chatgpt
a
good
translator?
yes
with gpt-4 as the engine,” 2023. [Online]. Available:
https://arxiv.org/abs/2301.08745
[2] L. Wang, C. Lyu, T. Ji, Z. Zhang, D. Yu, S. Shi, and
Z. Tu, “Document-level machine translation with large
language models,” 2023.
[3] M. Enis and M. Hopkins, “From llm to nmt: Advancing
low-resource machine translation with claude,” arXiv
preprint arXiv:2404.13813, 2024.
[4] H. Huang, S. Wu, X. Liang, B. Wang, Y. Shi, P. Wu,
M. Yang, and T. Zhao, “Towards making the most of llm
for translation quality estimation,” in CCF International
Conference on Natural Language Processing and Chinese
Computing.
Springer, 2023, pp. 375–386.
[5] M. Wu, T.-T. Vu, L. Qu, G. Foster, and G. Haffari,
“Adapting large language models for document-level
machine translation,” arXiv preprint arXiv:2401.06468,
2024.
[6] A. Hendy, M. Abdelrehim, A. Sharaf, V. Raunak, M. Gabr,
H. Matsushita, Y. J. Kim, M. Afify, and H. H. Awadalla,
“How good are gpt models at machine translation? a com-
prehensive evaluation,” arXiv preprint arXiv:2302.09210,
2023.
[7] K. Peng, L. Ding, Q. Zhong, L. Shen, X. Liu, M. Zhang,
Y. Ouyang, and D. Tao, “Towards making the most
of chatgpt for machine translation,” in Findings of the
Association for Computational Linguistics: EMNLP 2023,
2023, pp. 5622–5633.
[8] M. Wu, Y. Yuan, G. Haffari, and L. Wang, “(perhaps)
beyond human translation: Harnessing multi-agent col-
laboration for translating ultra-long literary texts,” arXiv
preprint arXiv:2405.11804, 2024.
[9] S. Wang, D. Wong, J. Yao, and L. Chao, “What
is the best way for ChatGPT to translate poetry?”
in Proceedings of the 62nd Annual Meeting of the
Association for Computational Linguistics (Volume 1:
Long Papers), L.-W. Ku, A. Martins, and V. Srikumar,
Eds.
Bangkok, Thailand: Association for Computational
Linguistics, Aug. 2024, pp. 14 025–14 043. [Online].
Available: https://aclanthology.org/2024.acl-long.756
[10] Y. Chen, H. Zhang, Y. Zhou, X. Bai, Y. Wang, M. Zhong,
J. Yan, Y. Li, J. Li, M. Zhu et al., “Revisiting cross-
lingual summarization: A corpus-based study and a new
benchmark with improved annotation.”
[11] A. Chaganty, S. Mussmann, and P. Liang, “The price
of debiasing automatic metrics in natural language
evalaution,” in Proceedings of the 56th Annual Meeting
of the Association for Computational Linguistics (Volume
1: Long Papers), I. Gurevych and Y. Miyao, Eds.
Melbourne, Australia: Association for Computational
Linguistics, Jul. 2018, pp. 643–653. [Online]. Available:
https://aclanthology.org/P18-1060
[12] Q. Ma, J. Wei, O. Bojar, and Y. Graham, “Results of the
WMT19 metrics shared task: Segment-level and strong
MT systems pose big challenges,” in Proceedings of the
Fourth Conference on Machine Translation (Volume 2:
Shared Task Papers, Day 1), O. Bojar, R. Chatterjee,
C. Federmann, M. Fishel, Y. Graham, B. Haddow,
M. Huck, A. J. Yepes, P. Koehn, A. Martins, C. Monz,
M. Negri, A. Névéol, M. Neves, M. Post, M. Turchi,
and K. Verspoor, Eds.
Florence, Italy: Association
for Computational Linguistics, Aug. 2019, pp. 62–90.
[Online]. Available: https://aclanthology.org/W19-5302
[13] R. Rei, C. Stewart, A. C. Farinha, and A. Lavie,
“COMET: A neural framework for MT evaluation,”
in Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing (EMNLP),
B.
Webber,
T.
Cohn,
Y.
He,
and
Y.
Liu,
Eds.
Online:
Association
for
Computational
Linguistics,
Nov. 2020, pp. 2685–2702. [Online]. Available: https:
//aclanthology.org/2020.emnlp-main.213
[14] T. Sellam, D. Das, and A. Parikh, “BLEURT: Learning
robust metrics for text generation,” in Proceedings of the
58th Annual Meeting of the Association for Computational
Linguistics, D. Jurafsky, J. Chai, N. Schluter, and
J. Tetreault, Eds.
Online: Association for Computational
Linguistics, Jul. 2020, pp. 7881–7892. [Online]. Available:
https://aclanthology.org/2020.acl-main.704
[15] M. Freitag, G. Foster, D. Grangier, V. Ratnakar, Q. Tan,
and W. Macherey, “Experts, errors, and context: A large-
scale study of human evaluation for machine translation,”
Transactions of the Association for Computational Lin-
guistics, vol. 9, pp. 1460–1474, 2021.
[16] L. Xu, H. Hu, X. Zhang, L. Li, C. Cao, Y. Li, Y. Xu,
K. Sun, D. Yu, C. Yu et al., “Clue: A chinese language
understanding evaluation benchmark,” arXiv preprint
arXiv:2004.05986, 2020.
[17] F. Ye, M. Yang, J. Pang, L. Wang, D. F. Wong, E. Yilmaz,
S. Shi, and Z. Tu, “Benchmarking llms via uncertainty
quantification,” 2024.
[18] D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika,
D. Song, and J. Steinhardt, “Measuring massive multitask
language understanding,” 2021.
[19] L. Yuan, Y. Chen, G. Cui, H. Gao, F. Zou, X. Cheng, H. Ji,
Z. Liu, and M. Sun, “Revisiting out-of-distribution robust-
ness in nlp: Benchmark, analysis, and llms evaluations,”
2023.
[20] W. Jiao, W. Wang, J. tse Huang, X. Wang, S. Shi, and
Z. Tu, “Is chatgpt a good translator? yes with gpt-4 as
the engine,” 2023.
[21] J. Zhu, J. Li, Y. Wen, and L. Guo, “Benchmarking
large language models on cflue–a chinese financial
language understanding evaluation dataset,” arXiv preprint
arXiv:2405.10542, 2024.
[22] Z. Liu, T. Zhong, Y. Li, Y. Zhang, Y. Pan, Z. Zhao,
P. Dong, C. Cao, Y. Liu, P. Shu et al., “Evaluating
large language models for radiology natural language
processing,” arXiv preprint arXiv:2307.13693, 2023.
[23] T. Goyal, J. J. Li, and G. Durrett, “News summarization
and evaluation in the era of gpt-3,” arXiv preprint
arXiv:2209.12356, 2022.
[24] H. Nguyen and V. Allan, “Using gpt-4 to provide tiered,
formative code feedback,” in Proceedings of the 55th ACM

--- Page 11 ---

11
Technical Symposium on Computer Science Education V.
1, 2024, pp. 958–964.
[25] L. T. Maloney, M. F. Dal Martello, V. Fei, and V. Ma,
“A comparison of human and gpt-4 use of probabilistic
phrases in a coordination game,” Scientific reports, vol. 14,
no. 1, p. 6835, 2024.
[26] S. C. Siu, “Chatgpt and gpt-4 for professional translators:
Exploring the potential of large language models in
translation,” Available at SSRN 4448091, 2023.
[27] L. Bojic, P. Kovacevic, and M. Cabarkapa, “Gpt-4
surpassing human performance in linguistic pragmatics,”
arXiv preprint arXiv:2312.09545, 2023.
[28] T. Han, L. C. Adams, K. Bressem, F. Busch, L. Huck,
S. Nebelung, and D. Truhn, “Comparative analysis of
gpt-4vision, gpt-4 and open source llms in clinical diag-
nostic accuracy: A benchmark against human expertise,”
medRxiv, pp. 2023–11, 2023.
[29] Y. Graham, T. Baldwin, A. Moffat, and J. Zobel,
“Continuous measurement scales in human evaluation
of machine translation,” in Proceedings of the 7th
Linguistic Annotation Workshop and Interoperability with
Discourse, A. Pareja-Lora, M. Liakata, and S. Dipper,
Eds.
Sofia, Bulgaria: Association for Computational
Linguistics, Aug. 2013, pp. 33–41. [Online]. Available:
https://aclanthology.org/W13-2305
[30] A. Farhad, A. Arkady, B. Magdalena, B. Ondˇrej, C. Rajen,
C. Vishrav, M. R. Costa-jussa, E.-B. Cristina, F. Angela,
F. Christian et al., “Findings of the 2021 conference on
machine translation (wmt21),” in Proceedings of the Sixth
Conference on Machine Translation.
Association for
Computational Linguistics, 2021, pp. 1–88.
[31] T. Kocmi, R. Bawden, O. Bojar, A. Dvorkovich, C. Feder-
mann, M. Fishel, T. Gowda, Y. Graham, R. Grundkiewicz,
B. Haddow et al., “Findings of the 2022 conference
on machine translation (wmt22),” in Proceedings of the
Seventh Conference on Machine Translation (WMT), 2022,
pp. 1–45.
[32] T.
Kocmi,
E.
Avramidis,
R.
Bawden,
O.
Bojar,
A. Dvorkovich, C. Federmann, M. Fishel, M. Freitag,
T. Gowda, R. Grundkiewicz et al., “Findings of the 2023
conference on machine translation (wmt23): Llms are
here but not quite there yet,” in Proceedings of the Eighth
Conference on Machine Translation, 2023, pp. 1–42.
[33] A. Lommel, M. Popovic, and A. Burchardt, “Assessing
inter-annotator agreement for translation error annotation,”
in MTE: Workshop on Automatic and Manual Metrics for
Operational Translation Evaluation. Language Resources
and Evaluation Conference Reykjavik, 2014, pp. 31–37.
[34] F. Klubiˇcka, A. Toral, and V. M. Sánchez-Cartagena,
“Quantitative fine-grained human evaluation of machine
translation systems: a case study on english to croatian,”
Machine Translation, vol. 32, no. 3, pp. 195–215, 2018.
[35] R. Rei, C. Stewart, A. C. Farinha, and A. Lavie,
“COMET: A neural framework for MT evaluation,”
in Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing (EMNLP),
B.
Webber,
T.
Cohn,
Y.
He,
and
Y.
Liu,
Eds.
Online:
Association
for
Computational
Linguistics,
Nov. 2020, pp. 2685–2702. [Online]. Available: https:
//aclanthology.org/2020.emnlp-main.213
[36] M. Freitag, R. Rei, N. Mathur, C.-k. Lo, C. Stewart,
E. Avramidis, T. Kocmi, G. Foster, A. Lavie, and
A. F. T. Martins, “Results of WMT22 metrics shared
task: Stop using BLEU – neural metrics are better
and more robust,” in Proceedings of the Seventh
Conference on Machine Translation (WMT), P. Koehn,
L. Barrault, O. Bojar, F. Bougares, R. Chatterjee,
M. R. Costa-jussà, C. Federmann, M. Fishel, A. Fraser,
M. Freitag, Y. Graham, R. Grundkiewicz, P. Guzman,
B. Haddow, M. Huck, A. Jimeno Yepes, T. Kocmi,
A. Martins, M. Morishita, C. Monz, M. Nagata,
T. Nakazawa, M. Negri, A. Névéol, M. Neves, M. Popel,
M. Turchi, and M. Zampieri, Eds.
Abu Dhabi, United
Arab Emirates (Hybrid): Association for Computational
Linguistics, Dec. 2022, pp. 46–68. [Online]. Available:
https://aclanthology.org/2022.wmt-1.2
[37] M.
Freitag,
N.
Mathur,
C.-k.
Lo,
E.
Avramidis,
R. Rei, B. Thompson, T. Kocmi, F. Blain, D. Deutsch,
C. Stewart, C. Zerva, S. Castilho, A. Lavie, and
G. Foster, “Results of WMT23 metrics shared task:
Metrics might be guilty but references are not innocent,”
in Proceedings of the Eighth Conference on Machine
Translation, P. Koehn, B. Haddow, T. Kocmi, and
C. Monz, Eds. Singapore: Association for Computational
Linguistics, Dec. 2023, pp. 578–628. [Online]. Available:
https://aclanthology.org/2023.wmt-1.51
[38] H. Hassan, A. Aue, C. Chen, V. Chowdhary, J. Clark,
C.
Federmann,
X.
Huang,
M.
Junczys-Dowmunt,
W. Lewis, M. Li et al., “Achieving human parity on
automatic chinese to english news translation,” arXiv
preprint arXiv:1803.05567, 2018.
[39] L. Fischer and S. L¨"aubli, “What’s the difference
between professional human and machine translation?
a blind multi-language study on domain-specific MT,”
in Proceedings of the 22nd Annual Conference of
the European Association for Machine Translation,
A. Martins, H. Moniz, S. Fumega, B. Martins, F. Batista,
L. Coheur, C. Parra, I. Trancoso, M. Turchi, A. Bisazza,
J. Moorkens, A. Guerberof, M. Nurminen, L. Marg,
and M. L. Forcada, Eds.
Lisboa, Portugal: European
Association for Machine Translation, Nov. 2020, pp.
215–224. [Online]. Available: https://aclanthology.org/
2020.eamt-1.23
[40] A. Toral, S. Castilho, K. Hu, and A. Way, “Attaining
the unattainable? reassessing claims of human parity
in neural machine translation,” in Proceedings of the
Third Conference on Machine Translation: Research
Papers, O. Bojar, R. Chatterjee, C. Federmann, M. Fishel,
Y. Graham, B. Haddow, M. Huck, A. J. Yepes,
P. Koehn, C. Monz, M. Negri, A. Névéol, M. Neves,
M. Post, L. Specia, M. Turchi, and K. Verspoor,
Eds.
Brussels, Belgium: Association for Computational
Linguistics, Oct. 2018, pp. 113–123. [Online]. Available:
https://aclanthology.org/W18-6312
[41] A. Kim, Y. Bak, J. Sun, S. Lyu, and C. Lee, “The
suboptimal wmt test sets and its impact on human

--- Page 12 ---

12
parity,” Preprints, February 2023. [Online]. Available:
https://doi.org/10.20944/preprints202110.0199.v2
[42] T. Poibeau, “On" human parity" and" super human perfor-
mance" in machine translation evaluation,” in Language
Resource and Evaluation Conference, 2022.
[43] Y. Graham, C. Federmann, M. Eskevich, and B. Haddow,
“Assessing human-parity in machine translation on
the segment level,” in Findings of the Association for
Computational Linguistics: EMNLP 2020, T. Cohn, Y. He,
and Y. Liu, Eds.
Online: Association for Computational
Linguistics,
Nov.
2020,
pp.
4199–4207.
[Online].
Available: https://aclanthology.org/2020.findings-emnlp.
375
[44] S. Communication, L. Barrault, Y.-A. Chung, M. C.
Meglioli, D. Dale, N. Dong, P.-A. Duquenne, H. Elsahar,
H. Gong, K. Heffernan, J. Hoffman, C. Klaiber,
P. Li, D. Licht, J. Maillard, A. Rakotoarison, K. R.
Sadagopan, G. Wenzek, E. Ye, B. Akula, P.-J. Chen,
N. E. Hachem, B. Ellis, G. M. Gonzalez, J. Haaheim,
P. Hansanti, R. Howes, B. Huang, M.-J. Hwang,
H. Inaguma, S. Jain, E. Kalbassi, A. Kallet, I. Kulikov,
J. Lam, D. Li, X. Ma, R. Mavlyutov, B. Peloquin,
M. Ramadan, A. Ramakrishnan, A. Sun, K. Tran,
T. Tran, I. Tufanov, V. Vogeti, C. Wood, Y. Yang,
B. Yu, P. Andrews, C. Balioglu, M. R. Costa-jussà,
O. Celebi, M. Elbayad, C. Gao, F. Guzmán, J. Kao,
A. Lee, A. Mourachko, J. Pino, S. Popuri, C. Ropers,
S. Saleem, H. Schwenk, P. Tomasello, C. Wang, J. Wang,
and S. Wang, “Seamlessm4t: Massively multilingual
& multimodal machine translation,” 2023. [Online].
Available: https://arxiv.org/abs/2308.11596
[45] Z. Zhao, E. Wallace, S. Feng, D. Klein, and S. Singh,
“Calibrate before use: Improving few-shot performance of
language models,” in International conference on machine
learning.
PMLR, 2021, pp. 12 697–12 706.
[46] P. Liu, W. Yuan, J. Fu, Z. Jiang, H. Hayashi, and G. Neu-
big, “Pre-train, prompt, and predict: A systematic survey
of prompting methods in natural language processing,”
ACM Computing Surveys, vol. 55, no. 9, pp. 1–35, 2023.
[47] H. Xu, Y. J. Kim, A. Sharaf, and H. H. Awadalla, “A
paradigm shift in machine translation: Boosting translation
performance of large language models,” 2023.
[48] R. Rei, C. Stewart, A. C. Farinha, and A. Lavie, “Comet:
A neural framework for mt evaluation,” in Proceedings
of the 2020 Conference on Empirical Methods in Natural
Language Processing (EMNLP), 2020, pp. 2685–2702.
[49] H. Nakayama, T. Kubo, J. Kamura, Y. Taniguchi,
and
X.
Liang,
“doccano:
Text
annotation
tool
for
human,”
2018,
software
available
from
https://github.com/doccano/doccano. [Online]. Available:
https://github.com/doccano/doccano
[50] J. Cohen, “A coefficient of agreement for nominal scales,”
Educational and psychological measurement, vol. 20,
no. 1, pp. 37–46, 1960.
[51] K. Krippendorff, “Validity in content analysis,” Comput-
erstrategien für die Kommunikationsanalyse, vol. 69, p.
45p, 1980.
[52] W. Wang, W. Jiao, J. Huang, R. Dai, J.-t. Huang, Z. Tu,
and M. R. Lyu, “Not all countries celebrate thanksgiving:
On the cultural dominance in large language models,”
CoRR, 2023.
[53] Y. Zhang, Y. Li, L. Cui, D. Cai, L. Liu, T. Fu, X. Huang,
E. Zhao, Y. Zhang, Y. Chen et al., “Siren’s song in the
ai ocean: a survey on hallucination in large language
models,” arXiv preprint arXiv:2309.01219, 2023.
[54] Z. Feng, Y. Zhang, H. Li, B. Wu, J. Liao, W. Liu,
J. Lang, Y. Feng, J. Wu, and Z. Liu, “Tear: Improving
llm-based machine translation with systematic self-
refinement,” 2024. [Online]. Available: https://arxiv.org/
abs/2402.16379
[55] M. Wu, Y. Yuan, G. Haffari, and L. Wang, “(perhaps)
beyond
human
translation:
Harnessing
multi-agent
collaboration for translating ultra-long literary texts,” 2024.
[Online]. Available: https://arxiv.org/abs/2405.11804
APPENDIX
To categorize translators into junior, medium, or senior
levels, we have established a comprehensive set of criteria
that take into account various factors indicative of a trans-
lator’s expertise and experience. These factors include the
translator’s educational background, particularly the prestige
of the institution from which they graduated, as well as their
length of service in the translation industry, the duration of their
translation career, the number of translations completed, and
any professional certifications they have obtained. To ensure the
ongoing competence of our translators, we conduct quarterly
assessments to evaluate their performance. For instance, to be
classified as a senior-level translator, an individual must possess
a minimum of ten years of translation experience, demonstrate
exceptional proficiency by achieving a score of 99% on our
assessments, and hold the distinguished CATTI++ translation
certification. By considering these stringent criteria, we aim
to maintain a highly qualified and skilled pool of translators
across all levels of expertise.
A. Error Types
Our annotation system is built upon the open-sourced
doccano system 5. In Figure 4, we provide a screenshot of
our annotation system. For each source sentence, outputs for
different systems are given and the annotators can select spans
of the text and annotate the error type and severity.
Our evaluation protocol largely follows the MQM criteria
released by Unbabel6. We provide a detailed annotation manual
for annotators, including an explanation for each error type as
well as illustrative examples for error types. It is included in
the following:
B. Annotation Requirements
The minimum unit that can be selected and annotated is a
whole word, a whitespace, a punctuation mark, or an isolated
character. In the following example, the version in French has
5https://github.com/doccano/doccano
6

--- Page 13 ---

13
Fig. 4: A screenshot of the Doccano annotation system we use.
an extra exclamation mark, so it’s necessary to annotate it as
a Punctuation error:
[EN] Thank you very much.
[FR] Merci beaucoup!
Wrong selection →Merci [beaucoup!]PUNCTUATION
Correct selection →Merci beaucoup[!]PUNCTUATION
If the issue occurs in a multiword expression, you will
need to select the whole expression; if, for example, an entire
sentence was translated and it shouldn’t have been, you should
select the entire sentence.
In the following example, we have an Unnatural Flow error:
[EN] Hi, Mary here.
[ES] Hola, Mary aquí.
Wrong selection →Hola, [Mary aquí.]UNNATURAL
FLOW
Correct selection →Hola, [Mary aquí]UNNATURAL
FLOW.
C. Error Types
a) Accuracy:
• Mistranslation
– Description: Translation does not accurately represent
the source.
– Example:
[EN] It has to be done by the book.
[FR]
Il
doit
être
fait
[par
le
livre]MISTRANSLATION
[Reason] The word-for-word translation into
French doesn’t work.
• Addition
– Description: Information not present in the source.
– Example:
[EN] That way you can be sure that you were
the one who made the changes.
[ES] Así puedes estar seguro de que fuiste tú
quien hizo [todos ADDItIoN los cambios.
[Reason] [Todos] (meaning ’all’ in Spanish) is
not present in the source and it is incorrectly
added in the target text.
• MT Hallucination
– Description: information that has nothing related to
source; or gibberish; or repeats
– Example:
[EN] You can send us a follow-up email at this
address [EMAIL].
[ES] [Hágame saber si tiene alguna otra pre-
gunta]MT HALLUCINATION.]
[Reason]: The Spanish translation reads please
let me know if you have any other questions and
it’s grammatically correct and fluent, but it has
no relation at all with the source.]
• Omission
– Description: Missing content from the source.
– Example:

--- Page 14 ---

14
[EN] We do not have much information on this.
[FR] Nous ne disposons pas [] OMISSION
beaucoup d’informations à ce sujet.
[Reason]: The French sentence requires the
preposition [de] (disposer de).
• Untranslated
– Description: Not translated.
– Example:
[EN] How To Make Pizza Dough
[FR]
Comment
faire
de
[Pizza
Dough|UNTRANSLATED
[Reason]: [Pizza Dough] is not a named entity
and is untranslated in the French version.
• Wrong Name Entity & Term
– Description: Wrong usage of NE and Terminology.
– Example:
[EN] Dear Wiley,
[IT] Gentile [Wilar WRONG NAMED ENTITY,
[Reason]: The name in the Italian version
doesn’t match the original.
b) Fluency:
• Grammar
– Description: Problems with grammar of target lan-
guage.
– Example:
[EN] I understand that you want to check in
online.
[CS] chàpu, ze se chcete [odbavení]gRAMMaR
online.
[Reason]: Wrong part of speech makes the
sentence ungrammatical in Czech.
• Punctuation
– Description: incorrect punctuation (for locale or
style).
– Example:
[EN] Original copy of the Proof of Purchase or
Invoice (not a screenshot):
[PT] C’opia original do comprovante de com-
pra ou nota fiscal (não uma captura de
tela)[.]PUNCTUATION
[Reason]: There’s a period instead of a colon in
the Brazilian Portuguese version of this sentence.
• Spelling
– Description: incorrect spelling or capitalization.
– Example:
[EN] This sort of damage is not covered under
the warranty, but we will seek assistance from
a higher support and see what we can do
regarding this issue.
[IT] Questo tipo di danno non è coperto dalla
garanzia, ma chiederò comunque aiuto ai re-
sponsabili dell’assistenza per capire che cosa
[Zi]SPELLING può fare per quanto riguarda
questo problema.
[Reason]: There’s a typo in the sentence in
Italian: the word [zi] should be [si] instead.
• Register
– Description: Wrong grammatical register (e.g., inap-
propriately informal pronouns).
– Example:
[EN] Wishing you a great day ahead.
[DE] Ich wünsche [Ihnen]REGISTER einen
schönen Tag.
[Reason]: The required register for the German
translation is Informal but the pronoun [Inhen]
is Formal.
• Inconsistent Style
– Description: internal inconsistency (not related to
terminology).
– Example:
[EN] Please click on this link. [...] This link
will expire in 24 hours.
[NN]
Klikk
på
denne
[lenken].[...]Denne
[linken]INCONSISTENCY utloper om 24 timer.
[Reason]: Both [lenk] and [link] are correct in
Norwegian, but in the same document, only one
should be used. Note: this is a single error, not
two
• Unnatural Flow
– Description: translations that are too literal or sound
unnatural.
– Example:
[EN] Zebras are ideal for animal matching.
[DE] [Zebras sind ideal, um bestimmte Tiere zu
finden]UNNATURAL FLOW.
[Reason] The German translation sounds too
literal, it reads like a translation, using the verb
[finden] (finding) as a translation for matching.
The verb matching should be translated as [de-
tektieren] (detect) to read as if it was originally
written in the target language: [Zebras sind ein
ideales Beispiel zur Detektion von Wildtieren.]
c) Other:
• Non-translation

```
