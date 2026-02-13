---
title: "2024-Chabot-Couture-Bridging the Gap Enhancing LLM Performance - PDF Extract"
source_pdf: "2024-Chabot-Couture-Bridging the Gap Enhancing LLM Performance.pdf"
pages: 69
extracted_at: "2026-02-13T09:15:42.242058"
---

# PDF Extract: 2024-Chabot-Couture-Bridging the Gap Enhancing LLM Performance

**Source PDF:** 2024-Chabot-Couture-Bridging the Gap Enhancing LLM Performance.pdf
**Total Pages:** 69

---

## Content

```
--- Page 1 ---

Bridging the Gap: Enhancing LLM Performance for Low-Resource African
Languages with New Benchmarks, Fine-Tuning, and Cultural Adjustments
Tuka Alhanai†*, Adam Kasumovic†*, Mohammad Ghassemi†*,
Aven Zitzelberger†, Jessica Lundin‡, Guillaume Chabot-Couture‡
†Ghamut Corporation, MI, USA
‡Bill and Melinda Gates Foundation, WA, USA
Abstract
Large Language Models (LLMs) have shown remarkable
performance across various tasks, yet significant dispari-
ties remain for non-English languages, and especially na-
tive African languages. This paper addresses these dispar-
ities by creating approximately 1 million human-translated
words of new benchmark data in 8 low-resource African lan-
guages, covering a population of over 160 million speak-
ers of: Amharic, Bambara, Igbo, Sepedi (Northern Sotho),
Shona, Sesotho (Southern Sotho), Setswana, and Tsonga. Our
benchmarks are translations of Winogrande and three sec-
tions of MMLU: college medicine, clinical knowledge, and
virology. Using the translated benchmarks, we report pre-
viously unknown performance gaps between state-of-the-art
(SOTA) LLMs in English and African languages. Finally, us-
ing results from over 400 fine-tuned models, we explore sev-
eral methods to reduce the LLM performance gap, includ-
ing high-quality dataset fine-tuning (using an LLM-as-an-
Annotator), cross-lingual transfer, and cultural appropriate-
ness adjustments. Key findings include average mono-lingual
improvements of 5.6% with fine-tuning (with 5.4% average
mono-lingual improvements when using high-quality data
over low-quality data), 2.9% average gains from cross-lingual
transfer, and a 3.0% out-of-the-box performance boost on cul-
turally appropriate questions. The publicly available bench-
marks, translations, and code from this study support further
research and development aimed at creating more inclusive
and effective language technologies.
Code — https://github.com/InstituteforDiseaseModeling/
Bridging-the-Gap-Low-Resource-African-Languages
Datasets — https://huggingface.co/datasets/Institute-
Disease-Modeling/mmlu-winogrande-afr
Introduction
For many tasks, Large Language Models (LLMs) perform
on-par with or approaching human performance. Further-
more, LLM capabilities are improving: the performance gap
between state-of-the-art LLMs (e.g. GPT-4) and humans for
many benchmarks is much smaller than the gap between pre-
vious LLM generations (e.g. GPT 3.5) and humans (Achiam
et al. 2023; Bandarkar et al. 2024; Sakaguchi et al. 2021;
*These authors contributed equally.
Copyright © 2025, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
Lin et al. 2021; Hendrycks et al. 2021b). Despite impressive
advancements, LLMs are significantly less capable when
assessed in non-English languages. When assessing LLMs
in native African languages, which are predominantly low-
resource (Joshi et al. 2020), the gap between human and
LLM performance is notable (when known), but generally
remains unknown because many standard benchmarks do
not exist in native African languages.
The performance discrepancy between LLMs in English
and African languages is not just a technical challenge; it is
a significant issue of equity. All 2,123 native African lan-
guages are low-resource, including the 31 languages with
more than 10 million speakers (Hammerstrom 2015; Joshi
et al. 2020)1. Naturally, lower language resource levels re-
sult in poorer-performing LLMs. This is particularly tragic
because LLMs are least reliable for language speakers who
have the most to gain. Of the world’s poor, 66% live in
Africa (Galal 2024), 66% of those don’t have access to the
Internet (ITU 2023), and 80% do not speak English (CIA
2024). Thus, even in the unlikely event that the world’s
poorest could access the Internet and afford the costs of
a state-of-the-art LLM, their ability to read and write En-
glish would prevent them from making use of the tools. Ul-
timately, the differences in LLM performance between lan-
guages result in a “rich-get-richer” effect: LLMs are more
helpful to (English-speaking) people who are better off, and
who may then provide better content to train better LLMs.
One approach to bridging the LLM performance gap is
to translate all non-English language queries into English,
query an English LLM, and backtranslate the response. This
approach is only viable if the cumulative errors from trans-
lation and backtranslation are smaller than the errors from
using non-English language LLMs alone. Previous studies
report that errors from leading machine translation tools (i.e.
Google Translate) can be substantial in African languages
(Bapna et al. 2022; Benjamin 2019); however, the extent to
which translation errors impact the substantive reasoning ca-
pabilities of multilingual LLMs versus their style (“transla-
tionese”), remains unclear. Insofar as the substantive errors
are minimal, machine translation may serve as a workaround
when: (i) the goal is to leverage an LLM to answer questions
1It was assumed that if a resource level rating in (Joshi et al.
2020) for a language was not given, then it was low-resource.
arXiv:2412.12417v1  [cs.CL]  16 Dec 2024

--- Page 2 ---

based on facts, and (ii) when the LLM being used has limited
non-English experience (e.g. Phi 3 (Abdin et al. 2024)).
In summary, existing LLMs under-perform in native
African languages, and it is unknown if translation tech-
nologies introduce too much error to serve as a viable
workaround. Thus, more tools, resources, and studies are
needed to help the research community understand (1) how
large is the LLM performance gap in African languages and
(2) what can be done to close the performance gap, once
known?
Aims
Our work has three specific aims, listed below:
• Aim 1 - Benchmark Translation: We translate the
popular multiple choice reasoning benchmark Wino-
grande, as well as three clinical sections of MMLU (col-
lege medicine, clinical knowledge, and virology) into
8 low-resourced and under-studied African languages
(Amharic, Bambara, Igbo, Sepedi, Shona, Sesotho,
Setswana, and Tsonga), allowing assessment of the (un-
known) capabilities of LLMs in African languages.
• Aim 2 - Performance Assessment: We apply several
state-of-the-art (SOTA) LLMs to the newly translated
benchmarks from Aim 1 and measure the extent of
the performance gap between English and each of the
African languages on the benchmarks. To assess the vi-
ability of machine translation, we compare the perfor-
mance of SOTA LLMs on machine-translated bench-
marks versus human-translated benchmarks. We also as-
sessed the performance gap between culturally appropri-
ate and inappropriate benchmark questions. This quan-
titative assessment highlights the areas and languages
where LLM improvements are most needed.
• Aim 3 - Performance Enhancement: We explore var-
ious fine-tuning strategies to determine their impact on
closing the LLM performance gap in African languages.
This includes adjusting the fine-tuning data used based
on the data domain, language, data quality, and the vol-
ume of training samples. Understanding how fine-tuning
characteristics impact LLM performance will inform
prospective data collection efforts for the community at
large.
The benchmarks, translations, and all the code needed to
recreate the results herein may be found online and are made
publicly available under the MIT license.
Related Work
Benchmarks in African Languages
Recent advances in natural language processing have seen
a growing interest in assessing language modeling perfor-
mance in African languages. This interest has resulted in
benchmarks in several tasks, including language identifica-
tion with AfroLID (Adebara et al. 2022), machine transla-
tion with FLORES-200 (NLLB Team et al. 2024), and nat-
ural language inference with XTREME (Hu et al. 2020).
More recently, benchmarks have emerged for African lan-
guages to assess LLM reasoning using multiple choice
questions. In particular, the manually curated reading com-
prehension benchmark Belebele provides the most exten-
sive coverage of African languages (25 languages; 115 lan-
guages in total) (Bandarkar et al. 2024). In addition to Bele-
bele, Irokobench provides manual translations of reason-
ing tasks into 15 African languages (Adelani et al. 2024),
while Winogrande-MMLU-Clinical-ZA also provides man-
ual translations of reasoning tasks into 3 African languages
(BMGF 2024). Given the lack of reasoning benchmarks
available for African languages, particularly benchmarks
that have been manually translated or otherwise sourced
from human-written text (i.e. not machine-translated or AI-
generated), we aim to translate two established reason-
ing and domain-knowledge benchmarks, Winogrande (Sak-
aguchi et al. 2021) and MMLU (Hendrycks et al. 2021b,a),
into 8 African languages. The translations of these two
benchmarks provide valuable additions to existing African
language datasets, enabling the proper evaluation of LLMs
in African languages in popular LLM evaluation tasks. This
effort helps pave the way for developing LLMs that perform
as well in African languages as they do in English, as the
availability of African language benchmarks allows devel-
opers to continually refine and enhance their LLMs for use
in African languages.
Impact of Culture on LLM Performance
When utilizing data from different languages, cultural fac-
tors have been shown to affect the accuracy, relevance, and
sensitivity of LLM output. Researchers have focused on the
“toxicity” of model outputs (i.e. the output of racist, vio-
lent, or harmful content) and have released several bench-
marks to measure toxicity in LLMs (Wen et al. 2023). How-
ever, the impact of cultural nuances has been relatively less
explored, in which content that in one context (language)
is mundane or inoffensive (e.g. “a child dislikes broccoli”)
may be considered culturally strange, incoherent, or disre-
spectful in another context (language) (Liu et al. 2021). Cul-
tural nuances have been shown to impact both the quality
of translations (Yao et al. 2023) as well as the model’s un-
derstanding and generation of responses (Putri et al. 2024).
Strategies to identify culture-specific references generally
require ground-truth labels generated by human annotators,
such as a list of offensive language-specific words (NLLB
Team et al. 2024), a list of universally acceptable words
(Borin, Comrie, and Saxena 2013), or predefined dimen-
sions of culture (Arora, Kaffee, and Augenstein 2023). Word
lists identify explicit expressions in the data and thus have
the advantage of scaling to large amounts of data; however,
word lists do not capture data that are implicitly inappro-
priate. Therefore, several efforts have been made to anno-
tate implicit expressions of cultural (in)appropriateness (Xu
et al. 2021; Hartvigsen et al. 2022). In this study, we evaluate
the impact of implicit cultural appropriateness on LLM per-
formance (via human annotators), when translating seem-
ingly inoffensive data (i.e. Winogrande) from English. We
also share the cultural annotation data to enrich the trans-
lated benchmark.

--- Page 3 ---

Impact of Fine-tuning on Cross-lingual Transfer
Previous studies report that cross-lingual instruction tun-
ing improves performance by nearly as much as mono-
lingual instruction tuning (Shaham et al. 2024). Given that
even the most widely spoken African languages are low-
resource, cross-lingual tuning may provide a way to “boost”
the amount of data (and thus the performance) of LLMs in
low-resource languages (Beukman and Fokam 2023; White-
house, Choudhury, and Aji 2023). However, the impact of
cross-lingual tuning is unknown for most African languages
(Hu et al. 2020; Liang et al. 2020; Conneau et al. 2018).
Hence, we also compare the effects of mono- and cross-
lingual tuning using the translated benchmarks.
Impact of Data Quality on LLM Performance
The scarcity of data is a significant barrier to improving
LLM performance (Villalobos et al. 2024). In an effort to re-
duce data barriers, automated methods have been presented
to identify high quality data samples within an existing cor-
pus (Longpre et al. 2024). Recent methods have focused on
using LLMs to assess the quality of data (Tan et al. 2024),
which includes annotating data based on the robustness of
question-answer pairs (QA pairs) to variations in the ques-
tion (Chen and Mueller 2024), rating data quality on a Likert
scale (Zhou et al. 2024), evaluating the correctness of an an-
swer (Cole et al. 2023), or generating a binary “preference”
score when selecting between two texts, such as the LLM-
as-a-Judge framework (Zheng et al. 2023). In this study, we
apply an LLM-as-an-Annotator of data quality across two
translated benchmarks in eight African languages.
Methods
Benchmark Translation (Aim 1)
We translated the popular multiple choice reasoning bench-
mark Winogrande, as well as three clinical sections of
MMLU (college medicine, clinical knowledge, and virol-
ogy) into 8 low-resourced and under-studied African lan-
guages (Amharic, Bambara, Igbo, Sepedi, Shona, Sesotho,
Setswana, and Tsonga). These benchmarks were selected
because they are multiple choice (and thus easy to compare
across languages) and widely used (300+ citations/year). A
summary of the translation process is described below, and
we provide additional information on the procedures, trans-
lator profiles, remuneration approach, and other details in
Appendix Section A.
Winogrande Translation Process
The translation of
Winogrande (3,674 QA pairs, 73,742 words) occurred in
three steps: (i) a translator translated QA-pairs from English
to the target language, (ii) an independent validator checked
each of the translations and corrected any identified trans-
lation errors, and (iii) two independent evaluators assessed
the final quality of the validated/corrected translation.
All individuals were recruited from Upwork.com; we re-
cruited the most qualified available individuals (translators,
validators, and evaluators) for each language and always
paid above the average wage ($7.30 USD) in South Africa
(Statistics South Africa 2020). All translators and validators
were allowed to use a machine translation tool, but had to
manually validate the output and correct errors. The evalua-
tors were presented with the validators’ translations (which
were corrections of the translators’ translations) and asked
to rate the quality of the translation according to three op-
tions: (i) “Good translation” (“good”), (ii) “Incorrect, but
someone could understand the idea” (“understandable”), and
(iii) “Completely wrong” (“wrong”) (Benjamin 2019; Bapna
et al. 2022). To aid the research community, we have made
the initial translations, corrections, and evaluations publicly
available along with the translated benchmarks. Examples
of the translation and validation survey forms are available
in Figures A.1 and A.2.
MMLU-Clinical
Translation
Process
Unlike
Wino-
grande, specialized domain-knowledge was required to
translate our selected MMLU sections: virology2 (189 QA
pairs / 5,452 words), clinical knowledge (299 QA pairs /
8,744 words), and college medicine (200 QA pairs / 12,911
words); thus, we hired a professional translation firm (Trans-
lated.com) to perform the translations of the three MMLU
sections. The professional translation firm guaranteed that
only translators with prior translation experience as well as
subject domain translation experience were used. The trans-
lation firm was paid $11,232.29 USD to translate the three
MMLU sections over a 15-day period.
Evaluation of LLM Performance (Aim 2)
We applied several state-of-the-art LLMs to the newly trans-
lated benchmarks from Aim 1 and measured the perfor-
mance gap between English and each of the African lan-
guages on the benchmarks. We also assessed the perfor-
mance gap between culturally appropriate and inappropriate
benchmark questions in Winogrande. Additional details on
the models assessed and the means by which cultural appro-
priateness labels were generated are provided below.
The LLM Performance Gap
We performed evaluations
of SOTA LLMs on the translated benchmarks. We also
compared LLM performance to English as a reference, as
well as pre-existing benchmark translations for Afrikaans,
Zulu, and Xhosa. The LLMs evaluated represented mod-
els that were either private: gpt-3.5-turbo-1106 (GPT-3.5)
(OpenAI 2023), gpt-4-turbo-2024-04-09 (GPT-4) (Achiam
et al. 2023), gpt-4o-2024-05-13 (GPT-4o) (OpenAI 2024);
public: Llama 3 70B / 8B instruction-tuned (Dubey et al.
2024); small for edge-devices: Phi 3 Mini 4K instruction-
tuned (Abdin et al. 2024); or specialized multilingual: Aya
23 (Aryabumi et al. 2024), Aya 101 ( ¨Ust¨un et al. 2024),
BLOOMZ 7b1 (Muennighoff et al. 2023). See Appendix B
for model hyperparameters. For both translated benchmarks,
Winogrande (binary choice co-reference resolution task)
and the three clinical sections of MMLU (multiple choice
medical domain knowledge task), 5-shot accuracy was re-
ported, mimicking (Achiam et al. 2023). Belebele (mul-
tiple choice reading comprehension task) results were also
reported to serve as an additional benchmark (which also
2The virology section for Afrikaans, Zulu, Xhosa were also
translated, extending the work of (BMGF 2024).

--- Page 4 ---

covers the languages in this study), and for which 0-shot ac-
curacy was used (Bandarkar et al. 2024). See Figures A.4-
A.6 for the evaluation prompts used for each benchmark.
Measuring Impact of Cultural Appropriateness
Al-
though our selected MMLU sections have a cross-cultural
focus (i.e. health-related), Winogrande may contain a set of
questions that could be considered strange, incoherent, or
disrespectful in some cultural contexts (e.g. “Jessica thought
Sandstorm was the greatest song ever written but Patricia
hated it. [Patricia / Jessica] bought a ticket to the jazz con-
cert.”).
We assessed how LLM performance in African languages
changed when assessed on culturally appropriate vs. cul-
turally inappropriate questions. More specifically, we gen-
erated annotations of translation appropriateness using the
same evaluators of Winogrande translation quality (de-
scribed earlier). The evaluators were provided with the
translated QA pair and asked “For a typical native speaker
in a typical conversational context (casual or professional),
could the translated sentence be considered strange, inco-
herent, or disrespectful?”, with the following options: (i)
“No, the sentence is typical”, (ii) “Maybe, I’m not sure”,
(iii) “Yes, the sentence is strange, incoherent, or disrespect-
ful”, or (iv) “I don’t understand the sentence” (Sap et al.
2020). Of the QA pairs labeled as a “good” or “understand-
able” translation (i.e. QA pairs with at least decent transla-
tion quality), a QA pair was considered “culturally appro-
priate” if both evaluators labeled it as “No, the sentence is
typical”; otherwise, it was considered “culturally inappropri-
ate”. To clarify, a “culturally appropriate” QA pair requires
labels for both decent translation quality and translation ap-
propriateness. Following our definition, 74.2% of translated
QA pairs were labeled culturally appropriate, while 20.6%
of translated QA pairs were labeled culturally inappropriate.
An example of the task can be seen in Figure A.3 and the
cultural annotation results are shown in Table A.1. In addi-
tion, QA pair examples of translation quality and appropri-
ateness annotation combinations are shown in Tables A.2-
A.93. We provide a detailed discussion of the inter-annotator
agreements, as well as the Cohen’s Kappa and Fleiss’ Kappa
scores in Section C of the Appendix.
To determine the effect of cultural appropriateness on
LLM performance, the GPT-family models were evaluated
out-of-the-box on the Winogrande test set, split by the col-
lected human annotations of appropriateness in each lan-
guage. Additionally, to account for the possibility of the hu-
man annotations capturing appropriateness in English and
not just the target language, the same splits of data for each
language were evaluated in English to be used as a baseline.
Then, if we observe a greater lift achieved in the target lan-
guage than in English for a given split of the data, we can
conclude that the human annotations do indeed reflect a dif-
ference in culture-specific appropriateness and also impact
the LLM’s performance.
3Languages that use non-Latin characters (Amharic, Bambara,
Igbo) cannot be rendered; however, all annotations are available in
the GitHub repository associated with this work.
Enhancement of LLM Performance (Aim 3)
After measuring the LLM performance gap in African lan-
guages (Aim 2), we explored various fine-tuning strate-
gies to reduce it. This included adjusting the fine-tuning
data based on domain (Winogrande vs. MMLU college
medicine), language (mono-lingual vs. cross-lingual con-
texts), data quality (low vs. high), and the volume of train-
ing samples (25%, 50%, 75%, 100%). Additional details
on the specific experiments follow. All experiments in this
section were performed with Llama 3 70B, which was: (i)
the best performing open-source model, (ii) was possible to
fine-tune, and (iii) was fiscally feasible. Moreover, all ex-
periments in this section used the same fine-tuning prompts,
which can be found in Figures A.7-A.8.
Fine-tuning with Varying Languages and Domains
We
determined the effects of mono- vs. cross-lingual fine-tuning
on LLM performance by comparing performance gains of
Lllama 3 70B on our benchmarks after tuning. More specif-
ically, we report the mono- and cross-lingual performance
of Llama 3 70B after fine-tuning using two of the trans-
lated benchmarks (Winogrande small train split, or MMLU
“college medicine” section) and evaluating on four test sets
(Winogrande test split, MMLU “clinical knowledge” sec-
tion, MMLU “virology” section, and Belebele).
Fine-tuning with Varying Data Quality and Quantity
To determine the effects of data quality and quantity on LLM
performance in low-resource settings, we utilized GPT-4o
to generate quality scores for each QA pair in our fine-
tuning datasets (i.e. LLM-as-an-Annotator). More specifi-
cally, for each QA pair in the fine-tuning dataset, GPT-4o
was prompted to provide a score of 1 to 10 based on the use-
fulness of a QA pair for fine-tuning an LLM to improve its
performance on a target evaluation benchmark (1 is the least
useful, while 10 is the most useful. See Figure A.9). The
LLM-as-an-Annotator was run three times to capture poten-
tial variability in outputs. The fine-tuning dataset was then
divided into tertiles according to the average of three quality
scoring runs. The tertile with the highest scores was desig-
nated as the “high quality” set, while the tertile with the low-
est scores was labeled as the “low quality” set. To evaluate
the impact of data volume on fine-tuning LLM performance,
the quality sets were randomly sampled at increments of 0%
(i.e. no tuning), 25%, 50%, 75%, and 100%.
Results
In this section, we provide results of five experiments that
support our three aims: (Aim 1) benchmark translation,
(Aim 2) evaluation of LLM performance, and (Aim 3) en-
hancement of LLM performance. More specifically, the sub-
sections below provide assessments of: (1) benchmark trans-
lation fidelity, (2) “out-of-the-box” LLM performance on
the translated benchmarks, (3) “out-of-the-box” LLM per-
formance on the culturally “appropriate” vs. “inappropriate”
subsets, (4) fine-tuned LLM performance using mono- and
cross-lingual data, and (5) fine-tuned LLM performance us-
ing varying data quality and quantity.

--- Page 5 ---

Benchmark Translation Fidelity
MMLU translations (by Translated.com) took 15 days to
complete and cost $11,232.29 USD. Winogrande transla-
tion (by Upwork.com translators) took between 3 days
(Setswana) and 9 days (Sesotho) and had a cumulative cost
of $15,126.40 USD. Winogrande translation verification (by
Upwork.com validators) took between 4 days (Setswana)
and 9 days (Shona) and had a cumulative cost of $9,179.37
USD. Winogrande translation assessment surveys for qual-
ity and appropriateness (by Upwork.com evaluators) took
between 3 days (Shona) and 8 days (Bambara) and had a
cumulative cost of $4,680.72 USD.
As seen in Figure A.10, corrections to the original transla-
tions varied by language: from 4.9% (for Sesotho) to 65.3%
(for Shona) of the QA pairs. As seen in Table A.10, 94.7% of
the validated / corrected translations were considered a good
/ understandable translation (“Good translation” or “Incor-
rect, but someone could understand the idea”) by at least one
evaluator, only 5.3% were considered wrong (“Completely
wrong”) by either evaluator, and a mere 0.2% were consid-
ered wrong (“Completely wrong”) by both evaluators. Thus,
we have reason to believe that (while not perfect) the trans-
lations are sufficient to measure the LLM performance gap
between English and the African languages.
Measuring the LLM Performance Gap
Here, we provide baseline performance results for SOTA
LLM models on three benchmarks: Winogrande, the three
clinical sections of MMLU, and Belebele. The average 5-
shot (0-shot for Belebele) accuracy scores across all lan-
Model
Bele
Wino
MMLU
CM
CK
Vir.
Baseline Performance (English language)
GPT-4o
95.9
83.9
84.4
89.8
60.2
Average Performance (all 11 African languages)
GPT-4o
76.0
64.8
66.6
70.6
48.2
GPT-4
69.6
60.9
56.2
60.7
46.0
Aya 101
58.4
50.5
35.7
36.1
32.0
Llama 3 70B
41.2
50.6
35.9
40.6
32.3
Aya 23
38.8
51.2
34.3
34.9
28.4
GPT-3.5
36.2
51.2
34.6
37.0
32.8
Llama 3 8B
36.3
50.4
31.9
35.3
27.3
Bloomz 7B
34.2
49.1
28.9
31.0
25.8
Phi 3 3B
32.2
50.7
30.3
32.4
27.8
Random
25.0
50.0
25.0
25.0
25.0
Performance Gap (English - African languages)
GPT-4o
19.9
19.1
17.8
19.2
12.0
Table 1: LLM Performance Gap Between English and
African Languages. The table displays SOTA out-of-the-
box model performance averaged across 11 African lan-
guages. The best performing model (GPT-4o) yields between
12.0% and 19.9% absolute difference in performance be-
tween English and the average of 11 African languages.
Bele: Belebele, Wino: Winogrande, CM: College Medicine,
CK: Clinical Knowledge, Vir.: Virology
guages and benchmarks are reported in Table 1, with En-
glish for reference. The best performing LLM (GPT-4o)
had a performance gap ranging from 12.0% to 19.9% ab-
solute between English and the average of the 11 African
languages. For individual languages, a breakdown of the
baseline performance of SOTA LLM models on the same
three benchmarks can be seen in Table 2. We observed that
among African languages, GPT-4o consistently performed
the best in Afrikaans and the worst in Bambara, with perfor-
mance gaps between the two ranging from 22.9% (MMLU
Virology) to 56.1% (Belebele) absolute across benchmarks,
suggesting that there is considerable variance in the per-
formance of SOTA models across individual African lan-
guages.
Additionally, we provide baseline performance results for
SOTA models when using machine-translated versions of
the benchmarks (see Tables A.11-A.15 for a breakdown of
performance by language and benchmark). The performance
difference between machine-translated queries and directly
using an LLM in non-English languages was not always sig-
nificant. Hence, our findings suggest that native language
LLMs may not be needed in some contexts (see Appendix
Section D for a more detailed discussion).
In Figure A.11, we present correlations between LLM
performance across language pairs. English was the least
correlated with the other languages. The seven Bantu lan-
guages and Igbo (Volta-Niger) had the highest correla-
tion values (see Figure A.12 for language families). Bam-
bara and Amharic were least correlated with the other lan-
guages, reflecting some combination of the different gram-
mar paradigms of the Mande and Semitic language families,
the difference in data quality, and (Amharic) script charac-
ters.
Impact of “Appropriateness” on Performance Gap
Here, we assess the impact of cultural appropriateness on
LLM performance; we evaluated the best-performing model
(GPT-4o) out-of-the box on the Winogrande test set, split-
ting the dataset by the human annotations in each language,
and observing the lift obtained for the “appropriate” QA
pairs compared to the “inappropriate” QA pairs (see Fig-
ure 1). When comparing the performance lift of GPT-4o in
English on the same annotations, we see that 7/11 African
languages have a higher lift in the target language, indicat-
ing that GPT-4o performs better on culturally appropriate
QA pairs for those languages (that is, the lift is not due to
the question itself being odd, independent of language; see
Figure A.14). The performance of GPT-4o on appropriate
over inappropriate Winogrande subsets ranged from -0.6%
(Xhosa) to +12.6% (Shona), with an average difference of
+3.3% across all languages. The performance lift of GPT-4o
when using English evaluations as a baseline ranged from -
2.3% (Igbo) to +15.6% (Sepedi), with an average difference
of +3.0% across all languages. A breakdown of the perfor-
mance by language can be found in Appendix Tables A.16
to A.19.

--- Page 6 ---

Winogrande
en
af
zu
xh
am
bm
ig
nso
sn
st
tn
ts
GPT-4o
83.9
79.7
68.3
65.9
59.4
50.2
60.7
64.1
69.5
67.4
64.7
62.6
GPT-4
83.5
77.0
64.2
62.3
51.0
50.7
58.7
58.8
65.6
63.8
59.9
57.7
GPT-3.5
59.6
55.0
50.8
52.2
51.3
50.4
51.9
50.2
51.6
49.2
51.5
49.6
Llama 3 70B IT
61.2
51.0
50.4
50.8
50.8
50.5
50.5
50.5
50.4
50.4
50.5
50.4
Llama 3 8B IT
52.0
50.7
50.4
50.4
50.3
50.4
50.4
50.4
50.4
50.4
50.4
50.4
Phi 3 Mini 4K IT
64.7
51.6
50.2
51.3
50.2
50.0
51.0
49.7
51.9
49.5
50.9
50.9
Aya 23 35B
68.7
56.5
49.6
51.8
51.3
50.8
50.6
51.4
50.6
50.0
49.8
50.5
Aya 101
49.5
51.1
49.1
51.2
51.2
52.0
50.5
49.0
51.0
50.5
50.8
49.6
BLOOMZ 7b1
48.6
50.3
48.7
48.8
49.3
50.0
48.8
47.9
48.6
49.6
49.2
49.1
MMLU College Medicine
GPT-4o
84.4
84.4
72.8
78.0
67.1
38.2
58.4
66.5
76.9
67.1
63.6
60.1
GPT-4
78.0
79.8
61.3
61.3
46.8
30.1
50.9
53.8
68.8
54.9
57.8
53.2
GPT-3.5
63.6
56.1
32.9
37.6
24.3
30.6
28.9
34.1
35.8
32.4
32.9
34.7
Llama 3 70B IT
76.9
68.2
35.8
40.5
36.9
24.3
33.5
27.2
38.2
28.3
34.1
29.5
Llama 3 8B IT
60.1
44.5
31.8
37.0
16.7
30.1
24.9
32.4
38.7
34.7
27.2
32.9
Phi 3 Mini 4K IT
66.5
39.9
30.6
28.9
28.0
31.2
28.9
28.3
28.3
27.7
34.1
30.1
Aya 23 35B
62.4
49.1
35.8
32.9
34.7
28.3
31.8
35.8
32.4
36.4
34.7
24.9
Aya 101
42.8
40.5
35.3
32.9
35.8
31.2
31.2
34.7
42.2
38.2
34.7
35.8
BLOOMZ 7b1
36.4
34.1
30.1
28.3
26.0
28.9
26.6
27.2
30.1
29.5
27.7
29.5
MMLU Clinical Knowledge
GPT-4o
89.8
87.2
79.6
78.5
70.6
40.0
63.0
72.5
80.4
69.4
71.3
64.5
GPT-4
84.2
81.9
70.2
68.3
54.0
34.7
54.7
58.1
67.2
64.2
58.9
55.8
GPT-3.5
72.5
62.6
39.2
37.4
30.2
31.3
34.3
33.2
41.1
34.3
30.6
32.8
Llama 3 70B IT
82.3
71.3
39.2
38.5
33.6
32.5
33.6
37.0
43.4
43.8
39.2
34.0
Llama 3 8B IT
69.1
45.3
36.6
34.7
24.9
32.1
36.2
35.5
39.2
39.2
33.2
31.7
Phi 3 Mini 4K IT
70.6
40.8
29.1
30.6
32.1
27.2
33.6
32.8
33.2
30.9
35.8
29.8
Aya 23 35B
69.4
55.1
32.5
33.6
29.1
33.2
32.5
37.4
32.5
34.3
30.9
32.5
Aya 101
45.3
42.6
38.1
35.5
38.9
28.3
34.7
36.6
44.2
37.0
30.6
30.9
BLOOMZ 7b1
44.9
33.2
30.6
33.2
28.3
32.5
26.8
34.7
30.6
32.1
27.2
31.3
MMLU Virology
GPT-4o
60.2
55.4
51.2
50.6
51.2
32.5
44.0
50.0
53.0
47.6
48.8
45.8
GPT-4
59.6
59.0
49.4
50.6
45.8
31.9
44.6
46.4
49.4
45.2
44.0
39.8
GPT-3.5
51.8
42.8
30.7
37.3
29.5
36.1
28.3
33.7
31.3
30.1
30.1
30.7
Llama 3 70B IT
53.6
46.4
28.9
27.1
36.1
35.5
34.9
26.5
31.3
29.5
28.3
31.3
Llama 3 8B IT
51.8
38.6
28.9
27.1
28.3
20.5
24.1
27.7
22.3
25.3
27.7
29.5
Phi 3 Mini 4K IT
48.8
30.1
27.1
25.3
27.1
25.3
32.5
27.7
28.3
24.1
25.3
32.5
Aya 23 35B
49.4
42.2
24.7
26.5
39.2
27.7
19.9
28.3
28.3
26.5
25.9
23.5
Aya 101
33.1
34.9
33.7
31.3
36.1
21.7
30.1
35.5
31.3
34.9
33.1
29.5
BLOOMZ 7b1
38.0
26.5
26.5
24.7
21.1
21.1
26.5
24.1
31.3
27.7
27.7
26.5
Belebele
GPT-4o
95.9
94.4
79.7
82.8
78.0
38.3
71.3
77.2
81.0
80.0
77.0
76.8
GPT-4
96.1
93.6
75.9
76.3
61.3
37.9
64.4
64.6
77.6
76.3
67.6
70.0
GPT-3.5
86.2
75.7
33.8
31.8
30.0
30.6
29.2
32.3
34.6
32.1
31.7
36.3
Llama 3 70B IT
94.6
84.8
36.7
36.8
35.1
35.6
35.9
37.1
38.1
35.9
36.4
40.7
Llama 3 8B IT
80.0
69.4
32.6
33.0
30.2
32.0
35.7
32.9
33.9
32.2
34.0
33.4
Phi 3 Mini 4K IT
89.2
52.6
28.3
29.1
28.7
31.7
28.8
31.6
29.1
30.6
29.2
34.3
Aya 23 35B
93.6
83.6
33.2
35.6
29.0
34.6
28.7
34.6
37.8
35.6
36.8
37.4
Aya 101
79.4
77.4
59.3
60.7
67.7
40.7
50.7
59.3
57.8
59.9
57.8
51.0
BLOOMZ 7b1
79.0
36.7
35.8
35.0
24.3
31.6
31.2
34.1
36.7
34.7
35.9
39.7
Table 2: Results of State-of-the-Art Models on Human-Translated Benchmarks. Top state-of-the-art models were evaluated
out-of-the-box (no fine-tuning) on the translated Winogrande (binary choice co-reference resolution task), the translated
three clinical sections of MMLU (multiple choice medical domain knowledge task), as well a pre-existing benchmark Belebele
(reading comprehension task). Results are provided for 11 low-resource African languages of focus: Afrikaans (af), Zulu (zu),
Xhosa (xh) (datasets for these three languages were sourced from (BMGF 2024)), Amharic (am), Bambara (bm), Igbo (ig),
Sepedi (nso), Shona (sn), Sesotho (st), Setswana (tn), and Tsonga (ts). Results on English (en) are also provided as a reference.
All numbers are performance accuracy, where MMLU and Winogrande numbers are 5-shot while Belebele numbers are
0-shot. Best performance is indicated with an underline. Overall, GPT-4o is best performing model across benchmarks.

--- Page 7 ---

Mono- and Cross-lingual Evaluations
Here, we assess how mono- and cross-lingual fine-tuning
impacts LLM performance on our selected benchmarks. The
results are shown in Figure 2 (see more detailed breakdowns
in Appendix Tables A.20 to A.27). Across the 11 languages,
the average mono-lingual gain was 5.6%4. Mono-lingual
performance gains when fine-tuning with MMLU college
medicine were greatest when evaluating on MMLU clinical
knowledge (17.4% on average), followed by Belebele (9.4%
on average), MMLU virology (3.5% on average), and Wino-
grande (1.2% on average). When fine-tuning with Wino-
grande, the greatest gains were observed when evaluating
LLMs on Belebele (6.4% on average), followed by Wino-
grande (2.7% on average), MMLU virology (2.6% on aver-
age), and MMLU clinical knowledge (1.2% on average).
4Average individual gains of all fine-tuned models above the
baselines in the same language as the fine-tuning language.
50%
55%
60%
65%
70%
75%
80%
Performance
Appropriate
Inappropriate
xh
ig
ts
bm
am
tn
st
zu
af nso sn
Language
-10%
-5%
0%
5%
10%
Lift
Target Language
English
Figure 1: GPT-4o Winogrande Performance on “appro-
priate” vs. “inappropriate” Data. GPT-4o was evaluated
on Winogrande (test set) out-of-the-box in each target lan-
guage and in English. Top plot: the absolute performance on
QA pairs considered culturally “appropriate” and “inap-
propriate” according to native speakers. Bottom plot: per-
formance lifts for each language (green) and in English
(grey), using the same annotations. QA Pair was defined as
“appropriate” when either annotator marked the cultural
appropriateness of the question as “typical”. Only QA pairs
where both annotators reported that the translation qual-
ity was “good” or “understandable” were considered. Lan-
guage codes are: Xhosa (xh), Igbo (ig), Tsonga (ts), Bam-
bara (bm), Amharic (am), Setswana (tn), Sesotho (st), Zulu
(zu), Afrikaans (af), Sepedi (nso), Shona (sn). See Table A.19
for a breakdown of performance by language. See Figure
A.13 distributions when repeated random samples of the
same size as the appropriate and inappropriate counts for
each target language are drawn.
Wino
Wino
MMLU
(ck)
MMLU
(vir)
Bele
Wino
MMLU
(ck)
MMLU
(vir)
Bele
Evaluation Data
20
10
0
10
20
30
40
Performance Gain (%)
Fine-tuning Data:
Winogrande
Fine-tuning Data: 
MMLU (college med.)
Mono-ling.
Cross-ling.
En (mono-ling)
En (cross-ling, median)
Figure 2: Mono- and Cross-lingual LLM Performance
Gains. The figure displays boxplots of performance gains
when fine-tuning with either the translated Winogrande train
set (left) or MMLU college medicine section (right). The
fine-tuned models were evaluated across 4 datasests (x-axis)
for mono-lingual gains (blue) across 11 African languages,
and cross-lingual gains (green) across 110 African lan-
guage pairs. The most significant gains were with models
fine-tuned with MMLU college medicine and evaluated on
MMLU clinical knowledge. Wino: Winogrande, ck: clinical
knowledge, vir: virology, Bele: Belebele. En: English.
Cross-lingual evaluations yielded a similar trend as mono-
lingual results; that is, mono-lingual gains (5.6% on aver-
age) also yielded corresponding cross-lingual gains (2.9%
on average)5, although to a lesser degree (see Figure 2). At
the language-level, when mono-lingual gains for a given lan-
guage was observed, then most models trained in other lan-
guages provided gains (i.e. cross-lingual transfer).
Data Quality and Quantity Evaluations
Here, we evaluate the impact of both the quality and quantity
of fine-tuning data on African language LLM performance.
Results across the 11 African languages for the highest per-
forming mono-lingual fine-tuning experiments (fine-tuning
on MMLU college medicine and evaluating on MMLU clin-
ical knowledge) are shown in Figure 3. There were increas-
ing performance gains with increasing data sizes of 2.3% on
average when data sizes were doubled (from 33 to 66 sam-
ples), in either quality sets. When data were split between
high-quality and low-quality data, the average gain from the
data quality split was 5.4% on average. The complete break-
down of results by language for fine-tuning on Winogrande
and MMLU, and evaluating on the four benchmarks is listed
in Appendix Tables A.28 to A.31.
5Average individual gains of all fine-tuned models above the
baselines in languages other than the fine-tuning language.

--- Page 8 ---

0%
(N/A)
0%
(N/A)
25%
(17)
50%
(33)
75%
(50)
100%
(66)
Percent of Data Quality Tertile Used
(samples)
30
40
50
60
70
80
90
100
Performance (%)
Low Quality
High Quality
En (low quality)
En (high quality)
Figure 3: LLM Performance Across Quality and Quan-
tity Combinations. The figure displays LLM performance
when fine-tuning by data quality and quantity, using MMLU
college medicine and evaluating on MMLU clinical knowl-
edge (which had the greatest mono-lingual gains from Fig-
ure 2). The quality of samples was rated using GPT-4o LLM-
as-an-Annotator scores. The lowest tertile and highest ter-
tile were defined as low (yellow) and high (green) qual-
ity samples, respectively, and were used to fine-tune Llama
3 70B IT. Boxplots display performance across 11 African
languages. English (En) is provided as a reference (red).
Overall, the use of high-quality fine-tuning data over low-
quality fine-tuning data improved performance for African
languages. See Table A.29 for a breakdown by language.
Discussion
This study aimed to measure (and explore means to address)
the performance gap of Large Language Models (LLMs)
in English and African languages by translating popular
benchmarks, assessing performance on those benchmarks,
and exploring fine-tuning strategies that close the gap. The
performance gap is not only a technical challenge but also
a matter of equity, as many native African languages are
low-resource, affecting the accessibility and effectiveness of
LLMs for over 160 million speakers6.
The creation of benchmarks in low-resourced African lan-
guages is a critical step toward achieving equitable advance-
ments in natural language processing. By translating pop-
ular benchmarks such as Winogrande and sections of the
MMLU into eight under-studied African languages, we pro-
vide essential tools for evaluating and improving LLM per-
formance in these languages. Our work not only highlights
existing performance gaps, but also lays the groundwork for
future research and development aimed at improving lan-
guage technologies for native African language speakers.
The benchmarks we translated may enable a more accurate
assessment of LLM capabilities and drive progress toward
6Ethical Statement of this work is viewable in the Appendix.
more inclusive and effective language models.
Our study revealed a significant LLM performance gap
between English and African languages: 12.0%-19.9% ab-
solute. This performance gap has profound implications, as
it exacerbates the digital divide and limits the accessibility
and utility of LLMs for millions of speakers of low-resource
languages. Addressing this gap is crucial for ensuring that
advances in AI benefit all language communities equitably,
thereby promoting greater inclusivity.
Moreover, our study also revealed a wide LLM per-
formance gap between individual African languages, with
Afrikaans (the highest-performing language) performing be-
tween 22.9%-56.1% (absolute) better than Bambara (the
lowest-performing language). This disparity is likely due to
Afrikaans and English both belonging to the Germanic lan-
guage family (indicating greater similarity of Afrikaans to
English) and Afrikaans having the highest resource level
(indicating greater data availability for pre-training LLMs)
across all African languages included in our study (Joshi
et al. 2020). In contrast, Bambara is part of the Mande lan-
guage family (see Figure A.12), which does not have a single
language that is considered high-resource (or even at the re-
source level of Afrikaans) (Hammerstrom 2015; Joshi et al.
2020). This implies that Bambara and its relatives have con-
siderably poorer data availability for pre-training LLMs than
Afrikaans. Taken together, these findings underscore the im-
portance of measuring the LLM performance gap of indi-
vidual African languages to guide and prioritize efforts in
creating language resources effectively (i.e. by targeting lan-
guages with lower performance).
Models showed up to 15.6% better performance on cul-
turally appropriate questions, indicating that cultural rele-
vance significantly influences model accuracy. This under-
scores the importance of incorporating cultural context in
model training and evaluation, particularly for diverse and
low-resource languages. Ignoring cultural nuances can lead
to biases and inaccuracies, further marginalizing underrep-
resented language communities.
Fine-tuning was shown to be effective in enhancing
model performance. Across all languages and benchmarks,
an average improvement of 5.6% was observed for mono-
lingual experiments (evaluating in the same language as
fine-tuning). The quality of the dataset significantly influ-
ences performance, with higher quality data leading to im-
provements of up to 14.5%, averaging 5.4% over lower
quality data of the same size. In addition, the alignment
of the training domain with the target domain yielded the
strongest gains. For example, fine-tuning a model with col-
lege medicine data resulted in notable improvements in clin-
ical knowledge tasks: 17.4% on average.
In scenarios where target language data are scarce, uti-
lizing data from related languages may help. Cross-lingual
transfer methods provided gains of up to 21.1%, with an av-
erage improvement of 2.9% across all languages and bench-
marks. Our results highlight the potential benefit of using
linguistically similar resources to enhance model perfor-
mance in low-resource languages.

--- Page 9 ---

Limitations
Our study has several limitations that should be addressed or
extended in future work:
1. Choice of Fine-tuning Model: Although Llama 3 was
the best open-source solution at the time of this study,
it does not outperform GPT-4o out-of-the-box, even af-
ter fine-tuning. Future studies should consider evaluat-
ing other models (e.g. Llama 3.1, released on July 24th,
2024).
2. Fine-Tuning Scope: Our fine-tuning experiments were
conducted on individual languages in isolation. We did
not explore the potential gains from tuning LLMs using
data from multiple languages. Future research should in-
vestigate the effects of grouping African or related high-
resource languages to enhance performance.
3. Benchmark Relevance: The translation of established
LLM benchmarks, while valuable, may not fully capture
the depth and breadth of African-language specific use-
cases. Future benchmark creation efforts should consider
generating content that directly supports and aligns with
use-cases most relevant to African language speakers.
4. Variability in Translation Quality: Recruiting experi-
enced translators for all our chosen languages proved
difficult. The number of speakers available on Upwork
was limited for many languages, most notably Xhosa,
Sesotho, Shona, Setswana, Bambara, Sepedi, and Tsonga
(see Figure A.15 for more details). In some cases, it was
not possible to find workers with prior experience. We
also encountered variability in the dialects spoken by the
workers, a factor which was challenging to control given
the aforementioned lack of available speakers.
5. Language Coverage and Scalability: Although we
were able to cover 11 diverse African languages, there
are naturally many other African languages presumably
with LLM performance gaps which are not covered in
this work. We believe that our presented framework is
scalable, but acknowledge that the most costly part, the
human translation of text, is a significant barrier. To al-
leviate this, we suggest incorporating a step to automat-
ically identify translated text that may require additional
human verification, rather than verifying all translations
multiple times (which we performed to ensure that trans-
lations were high-fidelity). This should make it easier to
extend our work to other languages.
Conclusion
This study takes steps toward addressing the performance
gap in Large Language Models (LLMs) for African lan-
guages. As part of this work, we created approximately 1
million human-translated words of new benchmark data in
8 African languages, covering a population of 160 million
speakers. This effort involved the translation of established
benchmarks and the fine-tuning of more than 400+ mod-
els. The benchmarks, translations, and all the code needed
to recreate the results of this study are publicly available,
supporting ongoing efforts to improve LLM performance in
African languages and beyond. Future work should continue
to explore and address the challenges identified, ensuring
that advancements in AI benefit all language communities
equitably.

--- Page 10 ---

Acknowledgments
All research-related costs (experiments, translation costs,
etc.) were generously provided by the Bill and Melinda
Gates Foundation.
References
Abdin, M.; Jacobs, S. A.; Awan, A. A.; Aneja, J.; Awadal-
lah, A.; Awadalla, H.; Bach, N.; Bahree, A.; Bakhtiari, A.;
Behl, H.; et al. 2024. Phi-3 technical report: A highly capa-
ble language model locally on your phone. arXiv preprint
arXiv:2404.14219.
Achiam, J.; Adler, S.; Agarwal, S.; Ahmad, L.; Akkaya, I.;
Aleman, F. L.; Almeida, D.; Altenschmidt, J.; Altman, S.;
Anadkat, S.; et al. 2023.
Gpt-4 technical report.
arXiv
preprint arXiv:2303.08774.
Adebara, I.; Elmadany, A.; Abdul-Mageed, M.; and Inciarte,
A. 2022. AfroLID: A Neural Language Identification Tool
for African Languages. In Proceedings of the 2022 Confer-
ence on Empirical Methods in Natural Language Process-
ing, 1958–1981.
Adelani, D. I.; Ojo, J.; Azime, I. A.; Zhuang, J. Y.; Alabi,
J. O.; He, X.; Ochieng, M.; Hooker, S.; Bukula, A.; Lee,
E.-S. A.; et al. 2024. IrokoBench: A New Benchmark for
African Languages in the Age of Large Language Models.
arXiv preprint arXiv:2406.03368.
Arora, A.; Kaffee, L.-a.; and Augenstein, I. 2023.
Prob-
ing Pre-Trained Language Models for Cross-Cultural Dif-
ferences in Values.
In Dev, S.; Prabhakaran, V.; Ade-
lani, D.; Hovy, D.; and Benotti, L., eds., Proceedings of
the First Workshop on Cross-Cultural Considerations in
NLP (C3NLP), 114–130. Dubrovnik, Croatia: Association
for Computational Linguistics.
Aryabumi, V.; Dang, J.; Talupuru, D.; Dash, S.; Cairuz, D.;
Lin, H.; Venkitesh, B.; Smith, M.; Marchisio, K.; Ruder, S.;
et al. 2024. Aya 23: Open weight releases to further multi-
lingual progress. arXiv preprint arXiv:2405.15032.
Bandarkar, L.; Liang, D.; Muller, B.; Artetxe, M.; Shukla,
S. N.; Husa, D.; Goyal, N.; Krishnan, A.; Zettlemoyer, L.;
and Khabsa, M. 2024. The Belebele Benchmark: a Parallel
Reading Comprehension Dataset in 122 Language Variants.
In Proceedings of the 62nd Annual Meeting of the Associa-
tion for Computational Linguistics (Volume 1: Long Papers),
749–775. Bangkok, Thailand and virtual meeting: Associa-
tion for Computational Linguistics.
Bapna, A.; Caswell, I.; Kreutzer, J.; Firat, O.; van Esch, D.;
Siddhant, A.; Niu, M.; Baljekar, P.; Garcia, X.; Macherey,
W.; et al. 2022. Building machine translation systems for the
next thousand languages. arXiv preprint arXiv:2205.03983.
Benjamin,
M.
2019.
Empirical
Evaluation
of
Google
Translate
across
107
Languages.
https:
//www.teachyoubackwards.com/empirical-evaluation/.
Accessed: 2024-07-25.
Beukman, M.; and Fokam, M. 2023.
Analysing Cross-
Lingual Transfer in Low-Resourced African Named Entity
Recognition. In Proceedings of the 13th International Joint
Conference on Natural Language Processing and the 3rd
Conference of the Asia-Pacific Chapter of the Association
for Computational Linguistics (Volume 1: Long Papers),
199–224.
BMGF. 2024.
Expanding Reasoning Benchmarks in
Low-Resourced
African
Languages:
Winogrande
and
Clinical MMLU in Afrikaans, Xhosa, and Zulu.
https:
//github.com/InstituteforDiseaseModeling/winogrande-
mmlu-clinical-za.
Borin, L.; Comrie, B.; and Saxena, A. 2013. The Interconti-
nental Dictionary Series: A rich and principled database for
language comparison.
Chen, J.; and Mueller, J. 2024.
Automated data cura-
tion for robust language model fine-tuning. arXiv preprint
arXiv:2403.12776.
CIA.
2024.
The
World
Factbook
—
World.
https://www.cia.gov/the-world-factbook/countries/world/
#people-and-society. Accessed: 2024-07-29.
Cole, J.; Zhang, M.; Gillick, D.; Eisenschlos, J.; Dhingra, B.;
and Eisenstein, J. 2023. Selectively Answering Ambiguous
Questions. In Proceedings of the 2023 Conference on Em-
pirical Methods in Natural Language Processing, 530–543.
Conneau, A.; Rinott, R.; Lample, G.; Williams, A.; Bow-
man, S.; Schwenk, H.; and Stoyanov, V. 2018. XNLI: Eval-
uating Cross-lingual Sentence Representations. In Proceed-
ings of the 2018 Conference on Empirical Methods in Nat-
ural Language Processing, 2475. Association for Computa-
tional Linguistics.
De Melo, G.; Imaizumi, V.; and Cozman, F. 2019. Winograd
schemas in portuguese. In Anais do XVI Encontro Nacional
de Inteligˆencia Artificial e Computacional, 787–798. SBC.
Dubey, A.; Jauhri, A.; Pandey, A.; Kadian, A.; Al-Dahle, A.;
Letman, A.; Mathur, A.; Schelten, A.; Yang, A.; Fan, A.;
et al. 2024. The Llama 3 Herd of Models. arXiv preprint
arXiv:2407.21783.
Galal, S. 2024. Africa: Share of global poverty by country
2024. https://www.statista.com/statistics/1228553/extreme-
poverty-as-share-of-global-population-in-africa-by-
country. Accessed: 2024-07-29.
Hammerstrom, H. 2015. Ethnologue 16/17/18th editions: A
comprehensive review. LANGUAGE, 91(3).
Hartvigsen, T.; Gabriel, S.; Palangi, H.; Sap, M.; Ray, D.;
and Kamar, E. 2022.
ToxiGen: A Large-Scale Machine-
Generated Dataset for Adversarial and Implicit Hate Speech
Detection. In Proceedings of the 60th Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long
Papers), 3309–3326.
Hendrycks, D.; Burns, C.; Basart, S.; Critch, A.; Li, J.; Song,
D.; and Steinhardt, J. 2021a. Aligning AI With Shared Hu-
man Values. Proceedings of the International Conference
on Learning Representations (ICLR).
Hendrycks, D.; Burns, C.; Basart, S.; Zou, A.; Mazeika, M.;
Song, D.; and Steinhardt, J. 2021b. Measuring Massive Mul-
titask Language Understanding. Proceedings of the Interna-
tional Conference on Learning Representations (ICLR).

--- Page 11 ---

Hu, J.; Ruder, S.; Siddhant, A.; Neubig, G.; Firat, O.; and
Johnson, M. 2020. Xtreme: A massively multilingual multi-
task benchmark for evaluating cross-lingual generalisation.
In International Conference on Machine Learning, 4411–
4421. PMLR.
ITU. 2023. Facts and Figures 2023. https://www.itu.int/itu-
d/reports/statistics/facts-figures-2023/. Accessed: 2024-07-
29.
Joshi, P.; Santy, S.; Budhiraja, A.; Bali, K.; and Choudhury,
M. 2020. The State and Fate of Linguistic Diversity and In-
clusion in the NLP World. In Proceedings of the 58th Annual
Meeting of the Association for Computational Linguistics,
6282. Association for Computational Linguistics.
Liang, Y.; Duan, N.; Gong, Y.; Wu, N.; Guo, F.; Qi, W.;
Gong, M.; Shou, L.; Jiang, D.; Cao, G.; et al. 2020. XGLUE:
A New Benchmark Dataset for Cross-lingual Pre-training,
Understanding and Generation. In Proceedings of the 2020
Conference on Empirical Methods in Natural Language
Processing (EMNLP), 6008–6018.
Lin, X. V.; Mihaylov, T.; Artetxe, M.; Wang, T.; Chen, S.;
Simig, D.; Ott, M.; Goyal, N.; Bhosale, S.; Du, J.; et al. 2021.
Few-shot learning with multilingual language models. arXiv
preprint arXiv:2112.10668.
Liu, F.; Bugliarello, E.; Ponti, E. M.; Reddy, S.; Collier, N.;
and Elliott, D. 2021. Visually Grounded Reasoning across
Languages and Cultures. arXiv:2109.13238.
Longpre, S.; Yauney, G.; Reif, E.; Lee, K.; Roberts, A.;
Zoph, B.; Zhou, D.; Wei, J.; Robinson, K.; Mimno, D.; et al.
2024.
A Pretrainer’s Guide to Training Data: Measuring
the Effects of Data Age, Domain Coverage, Quality, and
Toxicity.
In Proceedings of the 2024 Conference of the
North American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies (Volume
1: Long Papers), 3245–3276.
Muennighoff, N.; Wang, T.; Sutawika, L.; Roberts, A.; Bi-
derman, S.; Le Scao, T.; Bari, M. S.; Shen, S.; Yong, Z. X.;
Schoelkopf, H.; et al. 2023.
Crosslingual Generalization
through Multitask Finetuning. In Proceedings of the 61st
Annual Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), 15991–16111.
NLLB Team; et al. 2024. Scaling neural machine translation
to 200 languages. Nature, 630(8018): 841.
OpenAI. 2023.
GPT-3.5 Turbo fine-tuning and API up-
dates. https://openai.com/index/gpt-3-5-turbo-fine-tuning-
and-api-updates/. Accessed: 2024-07-26.
OpenAI. 2024.
Hello GPT-4o.
https://openai.com/index/
hello-gpt-4o/. Accessed: 2024-07-26.
Polignano, M.; Basile, P.; and Semeraro, G. 2024.
Ad-
vanced Natural-based interaction for the ITAlian language:
LLaMAntino-3-ANITA. arXiv:2405.07101.
Putri, R. A.; Haznitrama, F. G.; Adhista, D.; and Oh, A.
2024.
Can LLM Generate Culturally Relevant Common-
sense QA Data? Case Study in Indonesian and Sundanese.
arXiv:2402.17302.
Sakaguchi, K.; Bras, R. L.; Bhagavatula, C.; and Choi, Y.
2021. Winogrande: An adversarial winograd schema chal-
lenge at scale. Communications of the ACM, 64(9): 99–106.
Sap, M.; Gabriel, S.; Qin, L.; Jurafsky, D.; Smith, N. A.; and
Choi, Y. 2020. Social Bias Frames: Reasoning about Social
and Power Implications of Language. In Proceedings of the
58th Annual Meeting of the Association for Computational
Linguistics, 5477–5490.
Shaham, U.; Herzig, J.; Aharoni, R.; Szpektor, I.; Tsar-
faty, R.; and Eyal, M. 2024. Multilingual instruction tun-
ing with just a pinch of multilinguality.
arXiv preprint
arXiv:2401.01854.
Statistics South Africa. 2020. Labour Market Dynamics in
South Africa. Technical report, Statistics South Africa, Pri-
vate Bag X44, Pretoria 0001.
Tan, Z.; Beigi, A.; Wang, S.; Guo, R.; Bhattacharjee, A.;
Jiang, B.; Karami, M.; Li, J.; Cheng, L.; and Liu, H. 2024.
Large language models for data annotation: A survey. arXiv
preprint arXiv:2402.13446.
¨Ust¨un, A.; Aryabumi, V.; Yong, Z.-X.; Ko, W.-Y.; D’souza,
D.; Onilude, G.; Bhandari, N.; Singh, S.; Ooi, H.-L.; Kayid,
A.; et al. 2024.
Aya model: An instruction finetuned
open-access multilingual language model.
arXiv preprint
arXiv:2402.07827.
Villalobos, P.; Ho, A.; Sevilla, J.; Besiroglu, T.; Heim, L.;
and Hobbhahn, M. 2024. Position: Will we run out of data?
Limits of LLM scaling based on human-generated data. In
Forty-first International Conference on Machine Learning.
Wen, J.; Ke, P.; Sun, H.; Zhang, Z.; Li, C.; Bai, J.; and
Huang, M. 2023. Unveiling the Implicit Toxicity in Large
Language Models.
In Proceedings of the 2023 Confer-
ence on Empirical Methods in Natural Language Process-
ing, 1322–1338.
Whitehouse, C.; Choudhury, M.; and Aji, A. 2023. LLM-
powered Data Augmentation for Enhanced Cross-lingual
Performance.
In Proceedings of the 2023 Conference on
Empirical Methods in Natural Language Processing, 671–
686.
Xu, J.; Ju, D.; Li, M.; Boureau, Y.-L.; Weston, J.; and Di-
nan, E. 2021. Bot-adversarial dialogue for safe conversa-
tional agents. In Proceedings of the 2021 Conference of the
North American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies, 2950–
2968.
Yao, B.; Jiang, M.; Yang, D.; and Hu, J. 2023. Benchmark-
ing LLM-based Machine Translation on Cultural Aware-
ness.
Zheng, L.; Chiang, W.-L.; Sheng, Y.; Zhuang, S.; Wu, Z.;
Zhuang, Y.; Lin, Z.; Li, Z.; Li13, D.; Xing35, E. P.; et al.
2023. Judging LLM-as-a-Judge with MT-Bench and Chat-
bot Arena. arXiv preprint arXiv:2306.05685.
Zhou, C.; Liu, P.; Xu, P.; Iyer, S.; Sun, J.; Mao, Y.; Ma, X.;
Efrat, A.; Yu, P.; Yu, L.; et al. 2024. Lima: Less is more
for alignment. Advances in Neural Information Processing
Systems, 36.

--- Page 12 ---

Appendix
Ethical Statement
The lack of publicly available benchmarks for low-resource
languages exacerbates the challenge of developing perfor-
mant LLMs for these languages. By providing the first
known translations of the Winogrande and MMLU bench-
marks into Amharic, Bambara, Igbo, Sepedi (Northern
Sotho), Shona, Sesotho (Southern Sotho), Setswana, and
Tsonga, this work addresses a critical gap in linguistic re-
sources. Our evaluations of SOTA models provide a quanti-
tative measure of existing gaps in model performance; criti-
cally, the ability to measure such gaps provides researchers
and developers with accessible resources to help them re-
duce such gaps. The work highlights the importance of high-
quality data in enhancing model performance, even when
data is limited, motivating further efforts for the curation of
high-quality data. Additionally, annotation of “culturally ap-
propriate” data and the demonstration of LLM sensitivity to
such annotation help promote linguistic equity and inclusiv-
ity in the development of LLMs.
A
Benchmark Translation
Winogrande Translation Process
We recruited a total of 23 initial translators (using Up-
work.com) to translate Winogrande QA pairs into Amharic,
Bambara, Igbo, Sepedi (Northern Sotho), Shona, Sesotho
(Southern Sotho), Setswana, and Tsonga (see translator pro-
files in Table A.32, and translation instructions in Figure
A.1). Specifically, the “small” training (640 QA pairs /
12,650 words), as well as the “dev” (1,267 QA pairs / 25,470
words) and “test” (1,767 QA pairs / 35,622 words) sets
were translated: a total of 3,674 QA pairs consisting of
73,742 words per language. Translators were requested to
(i) maintain original punctuation in translations (commas,
periods), (ii) preserve special characters exactly as they ap-
peared in the original text (e.g., “ ” underscore), and (iii)
retain original names in translations following the approach
of De Melo, Imaizumi, and Cozman (2019).
Translators were prioritized according to the following
metrics: (1) self-reported proficiency in English, (2) self-
reported proficiency in the target language, (3) presence of a
“Top Rated” or “Top Rated Plus” badge on Upwork.com,
(4) prior job success rate on Upwork.com, (5) prior in-
come earned reported on Upwork.com, and (6) any history
of translation jobs in the target language. Translators were
paid $0.0237 USD per word to translate a portion (from
20% to 100% of the dataset, depending on availability) for
up to 5 days, which translates into a (minimum) wage of
$8.75 USD per hour, above the average wage ($7.30 USD) in
South Africa (Statistics South Africa 2020), where four out
of eight of our target languages are spoken (Sepedi, Sesotho,
Setswana, and Tsonga). Translators were allowed to use a
machine translation tool, but with the requirement that they
manually validate the outputs and correct any errors.
To ensure that the translations were correct, a second set
of 28 validators was hired to (i) validate the quality of the
initial translation and (ii) provide corrections to the transla-
tions if any issues were found7 (see validator profiles in Ta-
ble A.32, validation instructions in Figure A.2). Similarly to
the translation task, we paid above the average wage ($7.30
USD) in South Africa (Statistics South Africa 2020). The
amendments to the original translations varied by language:
from 4.9% (for Sesotho) to 65.2% (for Shona) of the QA
pairs (see Figure A.10).
Translation Quality Assessment
We evaluated all translations against (i) the original English
text, and (ii) Google Translate8 results in the target language.
To compare translations with a reference text, we used
standard translation similarity metrics, specifically Recall-
Oriented Understudy for Gisting Evaluation (ROUGE-1).
The aim was to identify if reliance on machine translation
outputs was exceedingly high (represented as high similar-
ity scores against Google Translate in the target language >
0.95; this was the threshold used to warn Winogrande trans-
lators that their translations were similar to machine trans-
lations), or contained a concerningly high number of un-
translated English words (a high similarity score against the
original English text > 0.95), or were generally poor trans-
lations in the target language (represented with low similar-
ity scores against Google Translate into the target language
< 0.5). For MMLU, we observed ROUGE-1 scores com-
pared to Google Translations > 0.95 for at most 79% of the
data (Bambara/bm), and ROUGE-1 scores < 0.5 for at most
60% of the data (Sesotho/st). For Winogrande, we observed
ROUGE-1 scores compared to Google Translations > 0.95
for at most 22% of the data (Afrikaans/af), and ROUGE-1
scores < 0.5 for at most 29% of the data (Xhosa/xh). See
Figures A.16, A.17, and A.18 for more detailed ROUGE-1
scores on our translated datasets.
For the Winogrande data, a set of 48 translation quality
evaluators were recruited from Upwork, using the same re-
cruitment approach described earlier (see evaluator profiles
in Table A.32). The evaluators were asked to assess the pre-
viously obtained and verified human translations of Wino-
grande for translation quality. The evaluators were presented
with the original English and human-translated Winogrande
QA pair with the correct answers filled in and asked to rate
the quality of the translation according to three options: (i)
“Good translation”, (ii) “Incorrect, but someone could un-
derstand the idea”, and (iii) “Completely wrong” (Benjamin
2019; Bapna et al. 2022). An example of the task can be
seen in Figure A.3, while the evaluation results are shown
in Table A.10. 94.6% of the translations were considered
good/understandable (“Good translation” or “Incorrect, but
someone could understand the idea”) by either evaluator,
5.3% were evaluated as wrong (“Completely wrong”) by
either evaluator, and 0.2% were considered wrong (“Com-
pletely wrong”) by both evaluators.
We modeled the probability of a “Good translation” rating
79 translators were hired from the group of initial translators,
although they did not work on their own translations.
8At the time of writing, Google Translate did not support
Setswana on its API, so GPT-4o was prompted to machine-translate
the MMLU and Winogrande datasets into Setswana instead.

--- Page 13 ---

from both evaluators; an accuracy of 67% (Precision=0.67,
Recall=0.66, F1=0.65) was achieved using a random forest
classifier. The feature importances (permutation importance;
n=20), indicating the features that improved accuracy the
most, include the Zulu, Igbo, and Bambara languages as the
target language of translation (see Figure A.19).
B
Model Hyperparameters
The hyperparameters used to fine-tune Llama 3 70B IT in
all experiments were Seed=42, Epochs=3, Batch Size=1,
Learning Rate=2e-4, Optimizer=8-Bit AdamW, Weight De-
cay=0.01, Learning Rate Scheduler=Linear, LoRA Al-
pha=8, LoRA Dropout=0, LoRA Matrix Dimension=8.
These parameters were assigned based on (Polignano,
Basile, and Semeraro 2024). The Unsloth framework was
used for fine-tuning9. We used one A100 80GB GPU for
fine-tuning/evaluation in all experiments.
In all LLM inferences performed for our experiments, as
well as GPT-4o prompting for quality scoring, we used Tem-
perature=0.7 and Top P=0.9 (selected to mimic what was
used in (Shaham et al. 2024), which also conducted cross-
lingual fine-tuning experiments; these settings allowed for
more variance in LLM responses). Given that the outputs for
our experiments were always supposed to be a single letter
or number, we also truncated the outputs to three tokens.
For Setswana translations using GPT-4o, we used a Tem-
perature=0 and Top P=1 to minimize stochasticity similar to
the consistent responses of Google Translate.
C
Cultural Appropriateness Survey Details
We used both Cohen’s Kappa and Fleiss’ Kappa to deter-
mine the inter-rater reliability between the two evaluators
for each language, finding that the highest inter-rater agree-
ment was achieved in Shona with a Cohen’s Kappa score of
0.211 for translation quality (Table A.16). Although Cohen’s
Kappa and Fleiss’ Kappa are sensitive to highly skewed data
(see Table A.1), comparing scores between languages and
annotator questions provides a relative measure of agree-
ment. We observed that the inter-rater agreement for appro-
priateness annotations was very low even when agreement
was present for translation quality annotations, indicating
that different annotators may be sensitive to different aspects
of appropriateness.
In Figure A.14, we provide inter-rater agreement on cul-
tural inappropriateness definitions across the different tar-
get languages. Importantly, the Cohen’s Kappa scores do not
show strong agreement on the definition of “cultural appro-
priateness” across languages. However, it should be noted
that among the languages in our study, Xhosa and Zulu are
the most closely related (linguistically), and are also those
for which the inter-annotator agreement was the greatest
(κ = 0.09).
In order to account for a lack of agreement on appropri-
ateness, we consider a dataset QA pair “inappropriate” if
either evaluator did not mark it as “typical”. Additionally,
to observe any confounding effect that translation quality
9https://github.com/unslothai/unsloth
may have, we performed a comparative analysis on each lan-
guage for 3 conditions: (1) All dataset QA pairs included,
(2) only QA pairs included at least one evaluator considered
understandable, and (3) only QA pairs that both evaluators
considered understandable (“understandable” meaning that
the evaluator labeled it as either “good translation” or “in-
correct, but someone could understand the idea”). GPT-3.5,
GPT-4, and GPT-4o were evaluated on Winogrande in each
target language and in English. Then, for each target lan-
guage, the performance of each LLM in the sets labeled “ap-
propriate” and “inappropriate” was assessed in both the tar-
get language and English. Assessment in English was used
as a reference because it is possible that inappropriate trans-
lations were due to poor dataset QA pairs rather than culture-
specific inappropriateness.
We modeled the probability of inappropriate text using a
random forest classifier, with and without a quality feature,
achieving accuracies of 66% (Precision=0.67, Recall=0.66,
F1=0.65) and 80% (Precision=0.80, Recall=0.80, F1=0.80),
respectively. The quality feature was True if and only if
both evaluators gave a “Good translation” rating. For the
experiment without the quality feature, the feature impor-
tances with the largest contributions toward improving ac-
curacy were: Igbo, Afrikaans, Bambara, and Sepedi as the
target language of translation, as well as the ROUGE-1 score
against machine translation of the corrected translation (see
Figure A.20).
For the experiment with the quality feature, the feature
importances with the largest contributions toward improv-
ing accuracy were: the quality feature and Igbo as the target
language of translation. (see Figure A.21).
D
Out-of-the-Box Evaluations on
Machine-Translated Benchmarks
We performed the same evaluations of SOTA LLMs (Aim 2)
on our benchmarks using (1) machine translations of the hu-
man translations from the target African language back into
English, and (2) machine translations of the text instead of
human translations from English to the target African lan-
guage. Google Translate was used to translate all languages
except Setswana, for which GPT-4o was employed using
a simple “Translate the following from {language X} into
{language Y}” prompt.
Specifically, we took the original English versions of
Winogrande (binary choice co-reference resolution task),
the three clinical sections of MMLU (multiple choice medical
domain knowledge task), as well as Belebele (multiple
choice reading comprehension task) and machine-translated
them into each of Afrikaans, Zulu, Xhosa, Amharic, Bam-
bara, Igbo, Sepedi, Shona, Sesotho, Setswana, and Tsonga.
Moreover, we took the human-translated versions of these
benchmarks and machine-translated them back into English
using the same machine translation tools (i.e. “backtransla-
tions”). We used the same LLM evaluation prompts as were
used for Aim 2 (see Figures A.4-A.6).
The SOTA LLM evaluations on machine-translated
benchmarks are shown in Tables A.11-A.15. We gener-
ally observed that backtranslation to English showed bet-

--- Page 14 ---

ter performance of English-centric LLMs (i.e. LLMs trained
on limited amounts of low-resource language text) such as
Llama 3 (Dubey et al. 2024) or Phi 3 (Abdin et al. 2024),
with gains ranging between 20%-30% and reaching upwards
of 40% for Belebele, MMLU College Medicine, and MMLU
Clinical Knowledge. This finding suggests that when at-
tempting to leverage the knowledge of an English-centric
LLM for multiple choice question answering, it is highly
beneficial to first backtranslate the question into English, al-
lowing the LLM to work in its primary language of train-
ing. In contrast, for the large multilingual models GPT-4
and GPT-4o, the gains from backtranslation into English are
considerably smaller (0%-10% for most languages), with
evaluations on the human-translated benchmarks in the na-
tive language sometimes even yielding greater performance
(between 0%-10%). This is especially evident for Belebele
(Table A.15), suggesting that for certain tasks like read-
ing comprehension or language understanding, there are al-
ready LLMs that perform about as well in native African
languages as they do in English.
For machine translations from English into the target lan-
guage, we observed that our SOTA LLMs across the board
performed better or about the same on machine-translated
versions of the benchmarks for certain languages (e.g. Igbo
for MMLU College Medicine, MMLU Clinical Knowl-
edge, and Belebele), suggesting SOTA LLM reliance on
machine-translated training data or an affinity for “trans-
lationese” versions of certain African languages instead of
genuine, human-made text. However, for Winogrande (Ta-
ble A.11), the differences between machine-translated and
human-translated benchmark performance were generally
within 0-3%, suggesting that machine translation from En-
glish is as good as human translation from English for LLM
benchmark performance.
Finally, when observing the trend between LLM perfor-
mance in English (the original datasets) against African
language backtranslations (datasets machine-translated into
English but originally a human translation from English
into an African language; see Tables A.11-A.15), we ob-
serve degradations in performance (from the original En-
glish to the backtranslation) generally between 5%-25%,
with the lowest degradations occurring consistently when
backtranslating from Afrikaans. This indicates that the ma-
chine translation quality is higher for Afrikaans than for
other African languages, which may be due to Afrikaans and
English sharing Germanic language family membership (see
Figure A.12) and Afrikaans having a higher resource level
(implying greater availability of data for pre-training LLMs)
than all other African languages included in our experiments
(Joshi et al. 2020).
E
Reproducibility Checklist
This paper:
• Includes a conceptual outline and/or pseudocode descrip-
tion of AI methods introduced: Yes
• Clearly delineates statements that are opinions, hypothe-
sis, and speculation from objective facts and results: Yes
• Provides well marked pedagogical references for less-
familiar readers to gain background necessary to repli-
cate the paper: Yes
Does this paper make theoretical contributions? No
If yes, please complete the list below.
• All assumptions and restrictions are stated clearly and
formally. No theoretical contributions made.
• All novel claims are stated formally (e.g., in theorem
statements). No theoretical contributions made.
• Proofs of all novel claims are included. No theoretical
contributions made.
• Proof sketches or intuitions are given for complex and/or
novel results. No theoretical contributions made.
• Appropriate citations to theoretical tools used are given.
No theoretical contributions made.
• All theoretical claims are demonstrated empirically to
hold. No theoretical contributions made.
• All experimental code used to eliminate or disprove
claims is included. No theoretical contributions made.
Does this paper rely on one or more datasets? Yes, public
datasets.
If yes, please complete the list below.
• A motivation is given for why the experiments are con-
ducted on the selected datasets. Yes
• All novel datasets introduced in this paper are included
in a data appendix. Yes, these are included in the Sup-
plementary Materials.
• All novel datasets introduced in this paper will be made
publicly available upon publication of the paper with a
license that allows free usage for research purposes. Yes
• All datasets drawn from the existing literature (poten-
tially including authors’ own previously published work)
are accompanied by appropriate citations. Yes
• All datasets drawn from the existing literature (poten-
tially including authors’ own previously published work)
are publicly available. Yes
• All datasets that are not publicly available are described
in detail, with explanation why publicly available alter-
natives are not scientifically satisficing. N/A
Does this paper include computational experiments? Yes
If yes, please complete the list below.
• Any code required for pre-processing data is included in
the appendix. Yes, uploaded in Supplementary Mate-
rials
• All source code required for conducting and analyzing
the experiments is included in a code appendix. Yes, up-
loaded in Supplementary Materials
• All source code required for conducting and analyzing
the experiments will be made publicly available upon
publication of the paper with a license that allows free
usage for research purposes. Yes

--- Page 15 ---

• All source code implementing new methods have com-
ments detailing the implementation, with references to
the paper where each step comes from. Yes
• If an algorithm depends on randomness, then the method
used for setting seeds is described in a way sufficient to
allow replication of results. Yes, seed values are always
provided.
• This paper specifies the computing infrastructure used
for running experiments (hardware and software), includ-
ing GPU/CPU models; amount of memory; operating
system; names and versions of relevant software libraries
and frameworks. Yes
• This paper formally describes evaluation metrics used
and explains the motivation for choosing these metrics.
Yes
• This paper states the number of algorithm runs used to
compute each reported result. Yes
• Analysis of experiments goes beyond single-dimensional
summaries of performance (e.g., average; median) to in-
clude measures of variation, confidence, or other distri-
butional information. Yes
• The significance of any improvement or decrease in
performance is judged using appropriate statistical tests
(e.g., Wilcoxon signed-rank). No
• This paper lists all final (hyper-)parameters used for each
model/algorithm in the paper’s experiments. Yes
• This paper states the number and range of values tried
per (hyper-) parameter during development of the paper,
along with the criterion used for selecting the final pa-
rameter setting. Yes

--- Page 16 ---

Eval. 1
Eval. 2
xh
zu
af
ig
sn
ts
st
nso
tn
am
bm
Avg. (%)
Typical
Typical
2755
2832
2229
1738
3226
2946
3035
3535
2998
2830
2035
74.6%
Typical
Not sure
26
70
60
3
306
5
1
14
0
0
286
1.9%
Typical
Strange
6
267
335
965
68
160
3
76
1
34
69
4.9%
Typical
D.U.
1
43
3
0
18
2
1
0
0
1
1
0.2%
Not sure
Typical
394
51
246
514
26
337
106
6
467
787
498
8.5%
Not sure
Not sure
7
1
12
1
5
3
0
0
0
0
107
0.3%
Not sure
Strange
0
0
41
300
5
23
0
2
0
8
30
1.0%
Not sure
D.U.
1
0
1
0
1
0
0
0
0
0
1
<0.1%
Strange
Typical
208
356
593
87
14
158
514
36
205
14
431
6.5%
Strange
Not sure
3
0
24
0
3
0
0
0
0
0
97
0.3%
Strange
Strange
4
26
85
61
2
20
3
2
1
0
48
0.6%
Strange
D.U.
0
0
1
0
0
0
0
0
0
0
7
<0.1%
D.U.
Typical
248
28
34
3
0
11
11
1
2
0
47
1.0%
D.U.
Not sure
10
0
3
0
0
0
0
0
0
0
11
0.1%
D.U.
Strange
10
0
7
2
0
9
0
2
0
0
6
0.1%
D.U.
D.U.
1
0
0
0
0
0
0
0
0
0
0
<0.1%
Study Definitions of Cultural Appropriateness Given Translation Appropriateness and Quality
Approp.
Quality
xh
zu
af
ig
sn
ts
st
nso
tn
am
bm
Avg. (%)
Approp.
Good
2732
2811
2229
1737
3224
2863
3019
3506
2995
2829
2028
74.2
Inapprop.
Good
723
659
1240
1520
327
547
548
64
617
831
1238
20.6
Table A.1: Human Evaluation of Winogrande Translation Appropriateness. The table lists the total number of all possible
combinations of evaluator responses for the second survey question, rating whether the translation can be considered “strange,
incoherent, or disrespectful” in a typical conversational context. Possible answers were “No, the sentence is typical” (Typical),
“Maybe, I’m not sure” (Not sure), “Yes, the sentence is strange, incoherent, or disrespectful” (Strange), or “I don’t understand
the sentence” (D.U.). The bottom section, labeled “Study Definitions of Cultural Appropriateness Given Translation Appropri-
ateness and Quality” shows two definitions of cultural appropriateness/inappropriateness used in our study. First are QA pairs
considered “appropriate”, where both evaluators labeled the QA pair as “No, the sentence is typical” (Approp.). Second are
QA pairs considered “inappropriate” where either evaluator labeled the QA pair as anything other than “No, the sentence is
typical” (Inapprop.). In both cases, QA pairs were only considered if both evaluators labeled them as a “good” or “understand-
able” translation (see Table A.10). Language codes are as follows: Xhosa (xh), Zulu (zu), Afrikaans (af), Igbo (ig), Shona (sn),
Tsonga (ts), Sesotho (st), Sepedi (nso), Setswana (tn), Amharic (am), Bambara (bm).

--- Page 17 ---

Original English Version
Translated Afrikaans Version
Approp.
Quality
Sentence
Opt. 1
Opt. 2
Sentence
Opt. 1
Opt. 2
Ans.
Approp.
Good / Unders.
Robert wanted to paint
his bedroom black. Brett
said he would reget it
soon because it’s a poor
choice.
preferred the
lighter colors.
Robert
Brett
Robert wou sy slaap-
kamer swart verf. Brett
het gesˆe hy sal dit bin-
nekort berou, omdat dit
’n swak keuse is.
het
die ligter kleure verkies.
Robert
Brett
2
Inapprop.
Good / Unders.
A transmission is what
I am in need of today
Joseph tells Dennis, has
wrecked many cars.
Joseph
Dennis
n
Ratkas
is
wat
ek
vandag
nodig
het
sˆe
Joseph vir Dennis,
het
al baie motors verwoes.
Joseph
Dennis
1
Inapprop.
Wrong
Jessica often experiences
severe nausea, Victoria
does not therefore often
rides big roller coasters.
Jessica
Victoria
Jessica ervaar dikwels
erge naarheid en Victoria
nie.
ry dus nie dikwels
groot wipwaritte nie.
Jessica
Victoria
2
Table A.2: Examples of Winogrande Translation Appropriateness and Quality Annotation Combinations (Afrikaans).
The table gives example Winogrande QA pairs for each of the possible combinations of translation appropriateness and quality
according to annotations made by evaluators on our Winogrande translations to Afrikaans. QA pairs were considered “appropri-
ate” when both evaluators labeled the QA pair as “No, the sentence is typical” (Approp.). Conversely, QA pairs were considered
“inappropriate” when either evaluator labeled the QA pair as anything other than “No, the sentence is typical” (Inapprop.). QA
pairs were considered “culturally appropriate” if they were “appropriate” and if both evaluators labeled them as a “good” or
“understandable” translation (see Table A.10), hence why we group “good” and “understandable” quality annotations together
(Good / Unders.), separating them from “wrong” quality annotations (Wrong). As such, the top row in the table is an example of
a culturally appropriate Afrikaans Winogrande QA pair while the other rows are examples of culturally inappropriate Afrikaans
Winogrande QA pairs. Note that for Afrikaans, there was no “appropriate” yet “wrong” QA pair.

--- Page 18 ---

Original English Version
Translated Sepedi Version
Approp.
Quality
Sentence
Opt. 1
Opt. 2
Sentence
Opt. 1
Opt. 2
Ans.
Approp.
Good / Unders.
Betty
avoided
get-
ting attacked in the
dark
alley
where
Elena was mugged,
because
ignored
their intuition.
Betty
Elena
Betty o ile a phema
go
hlaselwa
mok-
gotheng wo o bego
o le lefsifsing moo
Elena
a
ilego
a
hlaselwa
gona,
ka
gobane
o
ile
a
hlokomologa
maik-
welo a bona.
Betty
Elena
2
Inapprop.
Good / Unders.
Michael ran track as
a teenager in high
school, but Lawrence
joined the math club,
because
was more
studious.
Michael
Lawrence
Michael
o
be
a
kitima dipapading ge
e be e sa le mofsa yo
a lego mahlalagad-
ing sekolong se se
phagamego,
eupˇsa
Lawrence
o
ile
a
tsenela sehlopha sa
dipalo, ka gobane
o be a le mafolofolo
kudu.
Michael
Lawrence
2
Approp.
Wrong
John had to bow to
walk
through
the
door
but
have
to
crawl to enter the
tent. The
is shorter.
door
tent
Johane
o
ile
a
swanelwa ke go khu-
nama gore a tsene
ka mojako eupˇsa o
ile a swanelwa ke
go khukhuna gore a
tsene ka tenteng.
ke
e kopana.
monyako
tente
2
Inapprop.
Wrong
Victoria
was
dis-
gusted because of the
odor of Sarah, and
did not want to be
around them.
Victoria
Sarah
Ditˇshelete tˇseo di ile
tˇsa lefˇsa ke Jason go
Dennis, ka ge a ile a
adima tˇshelete e ntˇsi
kudu nakong e feti-
lego.
Jason
Dennis
1
Table A.3: Examples of Winogrande Translation Appropriateness and Quality Annotation Combinations (Sepedi). The
table gives example Winogrande QA pairs for each of the possible combinations of translation appropriateness and quality
according to annotations made by evaluators on our Winogrande translations to Sepedi. QA pairs were considered “appropriate”
when both evaluators labeled the QA pair as “No, the sentence is typical” (Approp.). Conversely, QA pairs were considered
“inappropriate” when either evaluator labeled the QA pair as anything other than “No, the sentence is typical” (Inapprop.). QA
pairs were considered “culturally appropriate” if they were “appropriate” and if both evaluators labeled them as a “good” or
“understandable” translation (see Table A.10), hence why we group “good” and “understandable” quality annotations together
(Good / Unders.), separating them from “wrong” quality annotations (Wrong). As such, the top row in the table is an example
of a culturally appropriate Sepedi Winogrande QA pair while the other rows are examples of culturally inappropriate Sepedi
Winogrande QA pairs.

--- Page 19 ---

Original English Version
Translated Sesotho Version
Approp.
Quality
Sentence
Opt. 1
Opt. 2
Sentence
Opt. 1
Opt. 2
Ans.
Approp.
Good / Unders.
The horse prefers the
pasture over the barn
because there is more
room in the
for the
horse to stretch.
pasture
barn
Pere e rata lekhulo ho
feta moliko hobane ho
na le sebaka se sengata
seo pere e ka ikotlol-
lang.
lekhulo
molikong
1
Inapprop.
Good / Unders.
Cynthia had to pee af-
ter one large coffee but
Betty did not as
had a
very big bladder.
Cynthia
Betty
Cynthia o ile a tlameha
ho rota ka mor’a kofi e
le ’ngoe e kholo empa
Betty ha aa ka a etsa
joalo kaha o ne a e na
le senya se seholo ha-
holo.
Cynthia
Betty
2
Approp.
Wrong
Her boyfriend regret-
ted buying her a jacket
and got her a new hat
instead, as he knew
she thought the
was
a bad match for her
wardrobe.
jacket
hat
Mohlankana oa hae o
ile a ikoahlaela ho mo
rekela baki le ho mo
rekela katiba e ncha,
kaha o ne a tseba hore
o ne a nahana hore ha
e tˇsoanele liaparo tsa
hae.
baki
katiba
1
Inapprop.
Wrong
While in Tampa, Laura
lingered at a pirate ship
and
Lindsey
hurried
through a museum, so
was early to their meet-
ing.
Laura
Lindsey
Ha a ntse a le Tampa,
Laura o ile a lieha
ho kena sekepeng sa
masholu ’me Lindsey a
potlakela ho haola mu-
siamo, kahoo o ne a sa
le hoseng ho ea sebo-
keng sa hae.
Laura
Lindsey
2
Table A.4: Examples of Winogrande Translation Appropriateness and Quality Annotation Combinations (Sesotho). The
table gives example Winogrande QA pairs for each of the possible combinations of translation appropriateness and quality ac-
cording to annotations made by evaluators on our Winogrande translations to Sesotho. QA pairs were considered “appropriate”
when both evaluators labeled the QA pair as “No, the sentence is typical” (Approp.). Conversely, QA pairs were considered
“inappropriate” when either evaluator labeled the QA pair as anything other than “No, the sentence is typical” (Inapprop.). QA
pairs were considered “culturally appropriate” if they were “appropriate” and if both evaluators labeled them as a “good” or
“understandable” translation (see Table A.10), hence why we group “good” and “understandable” quality annotations together
(Good / Unders.), separating them from “wrong” quality annotations (Wrong). As such, the top row in the table is an example
of a culturally appropriate Sesotho Winogrande QA pair while the other rows are examples of culturally inappropriate Sesotho
Winogrande QA pairs.

--- Page 20 ---

Original English Version
Translated Setswana Version
Approp.
Quality
Sentence
Opt. 1
Opt. 2
Sentence
Opt. 1
Opt. 2
Ans.
Approp.
Good / Unders.
Brown rice is today’s
special explains Sarah
to Elena,
is buying
lunch for today.
Sarah
Elena
Raese e e borokwa ke
e e kgethegileng ya
gompieno Sarah o tl-
halosetsa Elena,
o
reka dijo tsa motshe-
gare tsa gompieno.
Sarah
Elena
2
Inapprop.
Good / Unders.
I wanted to build a
bathroom on the third
floor of the house but I
couldn’t because the
would be too full.
bathroom
floor
Ke ne ke batla go aga
ntlwana ya botlhapelo
mo boalong jwa bo-
raro jwa ntlo mme ke
ne ke sa kgone ka
gonne
e ne e tla tlala
thata.
phaposi
ya botl-
hapelo
boalo
2
Approp.
Wrong
Adam
was
law-
abiding
and
not
a
crook like Joseph, so
it was surprising that
was the one with
a
restraining
order
against him.
Adam
Joseph
Adam e ne e le leferef-
ere mme e seng moagi
yo o ikobelang molao
jaaka Joseph, ka jalo
go ne go gakgamatsa
gore
e ne e le ene yo
o nang le taelo ya go
mo thibela.
Adam
Joseph
1
Inapprop.
Wrong
Emily looked up and
saw Patricia racing by
overhead, as
was un-
der the ramp .
Emily
Patricia
Emily o ne a leba kwa
godimo mme a bona
Patricia a taboga ka fa
godimo ga tlhogo, ka
a ne a le ka fa tlase ga
tsela .
Emily
Patricia
1
Table A.5: Examples of Winogrande Translation Appropriateness and Quality Annotation Combinations (Setswana).
The table gives example Winogrande QA pairs for each of the possible combinations of translation appropriateness and quality
according to annotations made by evaluators on our Winogrande translations to Setswana. QA pairs were considered “appropri-
ate” when both evaluators labeled the QA pair as “No, the sentence is typical” (Approp.). Conversely, QA pairs were considered
“inappropriate” when either evaluator labeled the QA pair as anything other than “No, the sentence is typical” (Inapprop.). QA
pairs were considered “culturally appropriate” if they were “appropriate” and if both evaluators labeled them as a “good” or
“understandable” translation (see Table A.10), hence why we group “good” and “understandable” quality annotations together
(Good / Unders.), separating them from “wrong” quality annotations (Wrong). As such, the top row in the table is an example of
a culturally appropriate Setswana Winogrande QA pair while the other rows are examples of culturally inappropriate Setswana
Winogrande QA pairs.

--- Page 21 ---

Original English Version
Translated Shona Version
Approp.
Quality
Sentence
Opt. 1
Opt. 2
Sentence
Opt. 1
Opt. 2
Ans.
Approp.
Good / Unders.
Sue wanted to prac-
tice meditation so she
went to the gym with
her class but the
was
too late.
class
gym
Sue aida kudzidzira
kudzikamisa pfungwa
saka akaenda kugym
nevaayidzidza
navo
asi
vaaidzidza navo
vakanonoka.
muclass
mugym
1
Inapprop.
Good / Unders.
Angela
noticed
the
lumps
on
Amy
’s
arms
that
she
had
failed to notice,
is
just
oblivious
that
way.
Angela
Amy
Angela
akaona
ma-
pundu aive mumaoko
aAmy aainge atadza
kuona,
anongoshaya
hanya nenzira iyoyo.
Angela
Amy
2
Approp.
Wrong
After the loss of the
raft, the crew took the
lifeboat as the
was
older anyway.
raft
lifeboat
Munguva
yechamupupuri,
gwenzi
rakadonha
muti usati wadonha,
nokuti
makanga
muine
midzi
dza-
kanyudza.
igwa
chikepe
cheku-
nunura
1
Inapprop.
Wrong
Cosplay really inter-
ested
Matthew,
but
Donald didn’t know
much about it, so
tried to learn about it.
Matthew
Donald
Cosplay
aifarira
chaizvo
Matthew,
asi
Donald
aisaziva
zvakawanda
nez-
vazvo, saka
akaedza
kudzidza nezvazvo.
Matthew
Donald
2
Table A.6: Examples of Winogrande Translation Appropriateness and Quality Annotation Combinations (Shona). The
table gives example Winogrande QA pairs for each of the possible combinations of translation appropriateness and quality
according to annotations made by evaluators on our Winogrande translations to Shona. QA pairs were considered “appropriate”
when both evaluators labeled the QA pair as “No, the sentence is typical” (Approp.). Conversely, QA pairs were considered
“inappropriate” when either evaluator labeled the QA pair as anything other than “No, the sentence is typical” (Inapprop.). QA
pairs were considered “culturally appropriate” if they were “appropriate” and if both evaluators labeled them as a “good” or
“understandable” translation (see Table A.10), hence why we group “good” and “understandable” quality annotations together
(Good / Unders.), separating them from “wrong” quality annotations (Wrong). As such, the top row in the table is an example
of a culturally appropriate Shona Winogrande QA pair while the other rows are examples of culturally inappropriate Shona
Winogrande QA pairs.

--- Page 22 ---

Original English Version
Translated Tsonga Version
Approp.
Quality
Sentence
Opt. 1
Opt. 2
Sentence
Opt. 1
Opt. 2
Ans.
Approp.
Good / Unders.
Victoria
is
makeup
artist and Cynthia is
a
beauty
queen,
knows
a
lot
about
makeup.
Victoria
Cynthia
Victoria
i
makeup
artist kasi Cynthia i
hosikati ya vumbhuri,
u tiva swo tala hi
makeup.
Victoria
Cynthia
1
Inapprop.
Good / Unders.
James got the rod bro-
ken under his grip
when he was trying to
bend it to shape be-
cause the
is strong.
rod
grip
James
u
tshovile
nhonga
hi
nkhomo
wa yena loko a karhi
a ringeta ku yi petsa
hikuva
a yi tiyile.
nhonga
nkhomo
2
Approp.
Wrong
The doctor gave no
fluids
to
Neil
and
gave them to Jason
since
was not dehy-
drated.
Neil
Jason
Dokodela
a
nga
nyikanga Neil mati
kutani a ma nyika
Jason tanihi leswi
a nga heleriwangi hi
mati ya mirhi.
Neil
Jason
1
Inapprop.
Wrong
Lawrence
planned
to
steal
the
valu-
able
painting
from
Michael,
because
wanted
to
own
something beautiful.
Lawrence
Michael
Lawrence
u
kun-
guhate
ku
yiva
swilo
swa
nkoka
swa
swifaniso
swo
vatliwa, hikuva a lava
ku va na wanchumu
wo saseka.
Lawrence
Michael
1
Table A.7: Examples of Winogrande Translation Appropriateness and Quality Annotation Combinations (Tsonga). The
table gives example Winogrande QA pairs for each of the possible combinations of translation appropriateness and quality
according to annotations made by evaluators on our Winogrande translations to Tsonga. QA pairs were considered “appropriate”
when both evaluators labeled the QA pair as “No, the sentence is typical” (Approp.). Conversely, QA pairs were considered
“inappropriate” when either evaluator labeled the QA pair as anything other than “No, the sentence is typical” (Inapprop.). QA
pairs were considered “culturally appropriate” if they were “appropriate” and if both evaluators labeled them as a “good” or
“understandable” translation (see Table A.10), hence why we group “good” and “understandable” quality annotations together
(Good / Unders.), separating them from “wrong” quality annotations (Wrong). As such, the top row in the table is an example
of a culturally appropriate Tsonga Winogrande QA pair while the other rows are examples of culturally inappropriate Tsonga
Winogrande QA pairs.

--- Page 23 ---

Original English Version
Translated Xhosa Version
Approp.
Quality
Sentence
Opt. 1
Opt. 2
Sentence
Opt. 1
Opt. 2
Ans.
Approp.
Good / Unders.
When
it
came
to
taking care of el-
derly people, Adam
was suited for the
job more than Brian
because
lived with
younger
people
longer.
Adam
Brian
Xa
kufikelelwa
kumba
wokun-
yamekela
abantu
abadala,
uAdam
wayewufanelekela lo
msebenzi ngaphezu
kukaBrian
kuba
wayehlala
nabantu
abatsha ixesha elide.
Adam
Brian
2
Inapprop.
Good / Unders.
Randy has a lot of
wrinkles
on
their
face
but
Matthew
does not.
went to
the dermatologist for
treatment.
Randy
Matthew
URandy unemibimbi
emininzi
ebusweni
kodwa
uMatthew
akanayo.
waya
kwi-dermatologist
ukufumana unyango.
uRandy
uMatthew
2
Approp.
Wrong
Cathy felt a stronger
bond with her dog
than her cat because
her
was very aloof.
cat
dog
U
Cathy
waziva
esondelelene
nenja
yakhe
ngaphezu
kwekati yakhe kuba
wayezikhethele.
ikati
inja
1
Inapprop.
Wrong
I made more mis-
takes in the history
test than errors in the
math test, so the
were fewer because I
love math.
errors
mistakes
Ndenze
iimpazamo
ezininzi
kuva-
vanyo
lwembali
kuneziphoso
ku-
vavanyo
lwez-
ibalo, ngoko ke
ibimbalwa
kuba
ndiyazithanda
iz-
ibalo.
iimpazamo
iimpazamo
1
Table A.8: Examples of Winogrande Translation Appropriateness and Quality Annotation Combinations (Xhosa). The
table gives example Winogrande QA pairs for each of the possible combinations of translation appropriateness and quality
according to annotations made by evaluators on our Winogrande translations to Xhosa. QA pairs were considered “appropriate”
when both evaluators labeled the QA pair as “No, the sentence is typical” (Approp.). Conversely, QA pairs were considered
“inappropriate” when either evaluator labeled the QA pair as anything other than “No, the sentence is typical” (Inapprop.). QA
pairs were considered “culturally appropriate” if they were “appropriate” and if both evaluators labeled them as a “good” or
“understandable” translation (see Table A.10), hence why we group “good” and “understandable” quality annotations together
(Good / Unders.), separating them from “wrong” quality annotations (Wrong). As such, the top row in the table is an example
of a culturally appropriate Xhosa Winogrande QA pair while the other rows are examples of culturally inappropriate Xhosa
Winogrande QA pairs.

--- Page 24 ---

Original English Version
Translated Zulu Version
Approp.
Quality
Sentence
Opt. 1
Opt. 2
Sentence
Opt. 1
Opt. 2
Ans.
Approp.
Good / Unders.
Brian was charged
with a felony for
stealing
the
di-
amonds
even
though he hadn’t
touched the gold
bars, because the
original
owner
cared more about
the
.
bars
diamonds
UBrian wabekwa
icala
lokweba
amadayi-
mane
nakuba
ayengazange
azithinte izigxobo
zegolide,
ngoba
umnikazi
wangempela
wayenendaba n .
izingcezu
amaday-
imane
2
Inapprop.
Good / Unders.
Monica
was
taking a knitting
class, Elena gig-
gled at this. This
made
feel bad.
Monica
Elena
UMonica
wayefunda
eki-
lasini
lokuluka,
u-Elena
wagig-
itheka
ngalokhu.
Lokhu kwenza
waphatheka kabi.
uMonica
u-Elena
1
Approp.
Wrong
He try hard jerk
decided to lift ket-
tle bells instead of
free weights, be-
cause he heard the
were more ma-
cho.
kettle bells
free weights
Uzama jerk kanz-
ima
wanquma
ukuphakamisa
izinsimbi
iketela
esikhundleni
izisindo
khulula,
ngoba
wezwa
babe
macho
ngaphezulu.
Amak-
hombothi
ezib-
hengu
Izisindo
zamah-
hala
1
Inapprop.
Wrong
Erin
ordered
a
martini
when
Tanya
only
or-
dered
a
tonic
water with lemon,
because
was
pregnant.
Erin
Tanya
uErin
waOda
iMartini
lapho
uTanya
eyala
kuphela
amanzi
eTonic
anola-
mula,
ngoba
wayekhulelwe.
uErin
uTanya
2
Table A.9: Examples of Winogrande Translation Appropriateness and Quality Annotation Combinations (Zulu). The
table gives example Winogrande QA pairs for each of the possible combinations of translation appropriateness and quality
according to annotations made by evaluators on our Winogrande translations to Zulu. QA pairs were considered “appropriate”
when both evaluators labeled the QA pair as “No, the sentence is typical” (Approp.). Conversely, QA pairs were considered
“inappropriate” when either evaluator labeled the QA pair as anything other than “No, the sentence is typical” (Inapprop.). QA
pairs were considered “culturally appropriate” if they were “appropriate” and if both evaluators labeled them as a “good” or
“understandable” translation (see Table A.10), hence why we group “good” and “understandable” quality annotations together
(Good / Unders.), separating them from “wrong” quality annotations (Wrong). As such, the top row in the table is an example
of a culturally appropriate Zulu Winogrande QA pair while the other rows are examples of culturally inappropriate Zulu Wino-
grande QA pairs.

--- Page 25 ---

Eval. 1
Eval. 2
xh
zu
af
ig
sn
ts
st
nso
tn
am
bm
Avg. (%)
Good
Good
2406
1349
2522
1357
2561
2474
2952
3076
2941
2813
1751
64.8%
Good
Unders.
552
771
353
1637
126
136
4
167
59
51
306
10.3%
Good
Wrong
24
39
36
369
36
11
0
42
3
1
27
1.5%
Unders.
Good
312
898
455
106
689
674
605
290
597
778
967
15.8%
Unders.
Unders.
185
452
139
157
175
126
6
37
15
18
242
3.8%
Unders.
Wrong
3
33
20
32
39
6
0
21
2
2
15
0.4%
Wrong
Good
88
68
80
4
26
186
106
12
52
11
249
2.2%
Wrong
Unders.
100
61
56
8
7
49
1
2
2
0
99
1.0%
Wrong
Wrong
4
3
13
4
15
12
0
27
3
0
18
0.2%
Study Definitions of Translation Quality
Quality
xh
zu
af
ig
sn
ts
st
nso
tn
am
bm
Avg. (%)
Good / Unders.
3455
3470
3469
3257
3551
3410
3567
3570
3612
3660
3266
94.7%
Wrong
219
204
205
417
123
264
107
104
62
14
408
5.3%
Table A.10: Human Evaluation of Winogrande Translation Quality. The table above lists the total number of all possible
combinations of evaluator responses for the first survey question on the full Winogrande dataset, rating the quality of the
translations as “Good translation” (Good), “Incorrect, but someone could understand the idea” (Unders.), and “Completely
wrong” (Wrong). The bottom section, labeled “Study Definitions of Translation Quality”, shows two definitions of translation
quality used in our study. First are QA pairs considered “Good/Understandable”, where both evaluators labeled the QA pair
as “Good translation” or “Incorrect, but someone could understand the idea”. Second are QA pairs considered “Wrong” where
either evaluator labeled the QA pair as “Completely wrong”. Language codes are as follows: Xhosa (xh), Zulu (zu), Afrikaans
(af), Igbo (ig), Shona (sn), Tsonga (ts), Sesotho (st), Sepedi (nso), Setswana (tn), Amharic (am), Bambara (bm).

--- Page 26 ---

Winogrande
en
af
zu
xh
am
bm
ig
nso
sn
st
tn
ts
Machine Translation (en →x)
GPT-4o
83.9
77.9
66.5
65.0
56.9
51.1
62.3
61.5
65.7
65.4
61.7
61.6
GPT-4
83.5
74.8
63.2
62.5
50.9
51.2
60.2
56.0
62.7
60.0
57.7
57.0
GPT-3.5
59.6
55.9
51.3
51.6
50.0
51.5
51.9
49.7
49.9
50.2
52.0
51.0
Llama 3 70B IT
61.2
51.7
50.5
50.5
50.4
50.7
50.4
50.3
50.4
50.5
50.4
50.4
Llama 3 8B IT
52.0
50.9
50.5
50.4
50.4
50.4
50.4
50.4
50.3
50.4
50.5
50.4
Phi 3 Mini 4K IT
64.7
53.0
49.7
49.8
50.7
51.2
51.0
51.3
50.9
50.7
50.3
51.0
Aya 23 35B
68.7
55.2
50.4
51.2
48.3
52.8
52.0
49.6
49.6
50.8
52.0
51.2
Aya 101
49.5
49.1
51.1
49.3
50.0
49.0
50.0
49.2
49.0
50.1
49.9
50.5
BLOOMZ 7b1
48.6
50.3
45.4
48.6
48.7
51.5
48.3
49.8
48.7
49.3
49.6
50.0
Difference Between Human (Table 2) and Machine Translation
GPT-4o
0.0
1.8
1.8
0.9
2.5
-0.9
-1.6
2.6
3.8
2.0
3.0
1.0
GPT-4
0.0
2.2
1.0
-0.2
0.1
-0.5
-1.5
2.8
2.9
3.8
2.2
0.7
GPT-3.5
0.0
-0.9
-0.5
0.6
1.3
-1.1
0.0
0.5
1.7
-1.0
-0.5
-1.4
Llama 3 70B IT
0.0
-0.7
-0.1
0.3
0.4
-0.2
0.1
0.2
0.0
-0.1
0.1
0.0
Llama 3 8B IT
0.0
-0.2
-0.1
0.0
-0.1
0.0
0.0
0.0
0.1
0.0
-0.1
0.0
Phi 3 Mini 4K IT
0.0
-1.4
0.5
1.5
-0.5
-1.2
0.0
-1.6
1.0
-1.2
0.6
-0.1
Aya 23 35B
0.0
1.3
-0.8
0.6
3.0
-2.0
-1.4
1.8
1.0
-0.8
-2.2
-0.7
Aya 101
0.0
2.0
-2.0
1.9
1.2
3.0
0.5
-0.2
2.0
0.4
0.9
-0.9
BLOOMZ 7b1
0.0
0.0
3.3
0.2
0.6
-1.5
0.5
-1.9
-0.1
0.3
-0.4
-0.9
Machine Backtranslation (x →en)
GPT-4o
83.9
79.3
67.9
68.4
66.5
59.8
65.3
66.6
66.5
68.1
67.0
65.9
GPT-4
83.5
78.3
67.3
65.3
62.4
58.7
65.1
67.1
66.8
67.2
64.3
66.2
GPT-3.5
59.6
58.4
53.7
54.1
53.9
52.6
54.6
55.0
54.4
54.6
55.6
53.0
Llama 3 70B IT
61.2
59.7
54.4
54.5
53.1
53.9
53.5
53.2
54.5
53.8
53.9
52.6
Llama 3 8B IT
52.0
51.2
52.1
51.0
52.1
50.9
51.5
51.5
51.3
51.3
51.9
50.7
Phi 3 Mini 4K IT
64.7
63.2
57.0
57.2
55.4
54.6
55.1
54.7
57.0
54.9
58.0
55.6
Aya 23 35B
68.7
66.8
58.9
58.7
55.8
56.0
57.7
59.3
57.3
57.8
58.9
58.2
Aya 101
49.5
51.0
50.9
49.3
48.2
51.2
52.1
49.4
48.2
50.4
49.5
51.0
BLOOMZ 7b1
48.6
50.0
48.8
51.0
49.6
50.0
50.3
49.6
50.4
50.6
49.7
50.7
Difference Between Human (Table 2) and Machine Translation
GPT-4o
0.0
0.4
0.4
-2.5
-7.1
-9.6
-4.6
-2.5
3.0
-0.7
-2.3
-3.3
GPT-4
0.0
-1.3
-3.1
-3.0
-11.4
-8.0
-6.4
-8.3
-1.2
-3.4
-4.4
-8.5
GPT-3.5
0.0
-3.4
-2.9
-1.9
-2.6
-2.2
-2.7
-4.8
-2.8
-5.4
-4.1
-3.4
Llama 3 70B IT
0.0
-8.7
-4.0
-3.7
-2.3
-3.4
-3.0
-2.7
-4.1
-3.4
-3.4
-2.2
Llama 3 8B IT
0.0
-0.5
-1.7
-0.6
-1.8
-0.5
-1.1
-1.1
-0.9
-0.9
-1.5
-0.3
Phi 3 Mini 4K IT
0.0
-11.6
-6.8
-5.9
-5.2
-4.6
-4.1
-5.0
-5.1
-5.4
-7.1
-4.7
Aya 23 35B
0.0
-10.3
-9.3
-6.9
-4.5
-5.2
-7.1
-7.9
-6.7
-7.8
-9.1
-7.7
Aya 101
0.0
0.1
-1.8
1.9
3.0
0.8
-1.6
-0.4
2.8
0.1
1.3
-1.4
BLOOMZ 7b1
0.0
0.3
-0.1
-2.2
-0.3
0.0
-1.5
-1.7
-1.8
-1.0
-0.5
-1.6
Table A.11: Results of State-of-the-Art Models on Machine-Translated Winogrande. Top state-of-the-art models were
evaluated out-of-the-box (no fine-tuning) on Winogrande (binary choice co-reference resolution task) test datasets that were
machine-translated from English into the target language or backtranslated from the human-translated version back into English.
Google Translate was used for machine translations in all languages except Setswana (tn), where GPT-4o was used. Results
are provided for 11 low-resource African languages of focus: Afrikaans (af), Zulu (zu), Xhosa (xh) (datasets for these three
languages were sourced from (BMGF 2024)), Amharic (am), Bambara (bm), Igbo (ig), Sepedi (nso), Shona (sn), Sesotho (st),
Setswana (tn), and Tsonga (ts). Results on English (en) without any translation are also provided as a reference. Differences
with corresponding numbers from Table 2 are given, with negative values indicating that machine translation led to greater
performance than human-translation. All numbers are 5-shot performance accuracy.

--- Page 27 ---

MMLU College Medicine
en
af
zu
xh
am
bm
ig
nso
sn
st
tn
ts
Machine Translation (en →x)
GPT-4o
84.4
84.4
72.8
74.6
56.6
42.8
68.2
64.2
72.8
73.4
61.8
67.6
GPT-4
78.0
76.9
64.7
65.9
39.3
36.4
61.3
53.2
66.5
58.4
54.9
53.8
GPT-3.5
63.6
56.6
36.4
37.0
26.6
30.1
34.1
30.6
41.0
32.9
31.8
30.1
Llama 3 70B IT
76.9
66.5
37.0
38.2
24.4
27.2
38.2
27.2
41.6
34.1
27.7
33.5
Llama 3 8B IT
60.1
41.6
32.9
37.0
23.2
28.3
36.4
35.3
35.3
34.7
29.5
33.5
Phi 3 Mini 4K IT
66.5
38.2
34.1
27.2
22.3
27.2
38.2
34.7
37.6
36.4
26.6
32.9
Aya 23 35B
62.4
51.4
34.1
33.5
37.6
30.6
32.4
28.9
35.3
35.8
30.6
31.8
Aya 101
42.8
42.8
37.0
41.0
39.3
26.0
41.0
36.4
32.9
38.2
32.4
31.2
BLOOMZ 7b1
36.4
27.7
29.5
29.5
25.4
30.1
33.5
31.2
35.3
29.5
28.3
30.1
Difference Between Human (Table 2) and Machine Translation
GPT-4o
0.0
0.0
0.0
3.4
10.5
-4.6
-9.8
2.3
4.1
-6.3
1.8
-7.5
GPT-4
0.0
2.9
-3.4
-4.6
7.5
-6.3
-10.4
0.6
2.3
-3.5
2.9
-0.6
GPT-3.5
0.0
-0.5
-3.5
0.6
-2.3
0.5
-5.2
3.5
-5.2
-0.5
1.1
4.6
Llama 3 70B IT
0.0
1.7
-1.2
2.3
12.5
-2.9
-4.7
0.0
-3.4
-5.8
6.4
-4.0
Llama 3 8B IT
0.0
2.9
-1.1
0.0
-6.5
1.8
-11.5
-2.9
3.4
0.0
-2.3
-0.6
Phi 3 Mini 4K IT
0.0
1.7
-3.5
1.7
5.7
4.0
-9.3
-6.4
-9.3
-8.7
7.5
-2.8
Aya 23 35B
0.0
-2.3
1.7
-0.6
-2.9
-2.3
-0.6
6.9
-2.9
0.6
4.1
-6.9
Aya 101
0.0
-2.3
-1.7
-8.1
-3.5
5.2
-9.8
-1.7
9.3
0.0
2.3
4.6
BLOOMZ 7b1
0.0
6.4
0.6
-1.2
0.6
-1.2
-6.9
-4.0
-5.2
0.0
-0.6
-0.6
Machine Backtranslation (x →en)
GPT-4o
84.4
81.5
69.9
76.9
76.3
63.6
59.5
78.6
76.9
67.1
65.9
62.4
GPT-4
78.0
72.8
65.3
67.6
67.6
60.1
54.9
69.9
68.8
59.0
54.9
55.5
GPT-3.5
63.6
60.1
52.0
53.8
57.2
53.2
46.2
56.6
57.2
52.0
53.2
42.2
Llama 3 70B IT
76.9
75.1
62.4
67.6
68.2
56.6
56.1
68.2
71.7
60.1
57.8
53.2
Llama 3 8B IT
60.1
59.5
50.3
54.9
49.7
49.7
31.2
54.3
54.3
39.3
45.1
37.6
Phi 3 Mini 4K IT
66.5
64.2
49.7
57.8
59.0
51.4
44.5
58.4
60.1
52.6
49.1
46.2
Aya 23 35B
62.4
60.1
55.5
56.1
50.9
47.4
50.3
53.8
52.6
50.3
52.0
49.7
Aya 101
42.8
42.8
41.6
41.0
38.7
34.7
40.5
38.7
45.1
42.8
41.0
37.6
BLOOMZ 7b1
36.4
35.8
30.6
39.9
35.3
33.5
34.7
38.2
39.3
32.4
38.7
29.5
Difference Between Human (Table 2) and Machine Translation
GPT-4o
0.0
2.9
2.9
1.1
-9.2
-25.4
-1.1
-12.1
0.0
0.0
-2.3
-2.3
GPT-4
0.0
7.0
-4.0
-6.3
-20.8
-30.0
-4.0
-16.1
0.0
-4.1
2.9
-2.3
GPT-3.5
0.0
-4.0
-19.1
-16.2
-32.9
-22.6
-17.3
-22.5
-21.4
-19.6
-20.3
-7.5
Llama 3 70B IT
0.0
-6.9
-26.6
-27.1
-31.3
-32.3
-22.6
-41.0
-33.5
-31.8
-23.7
-23.7
Llama 3 8B IT
0.0
-15.0
-18.5
-17.9
-33.0
-19.6
-6.3
-21.9
-15.6
-4.6
-17.9
-4.7
Phi 3 Mini 4K IT
0.0
-24.3
-19.1
-28.9
-31.0
-20.2
-15.6
-30.1
-31.8
-24.9
-15.0
-16.1
Aya 23 35B
0.0
-11.0
-19.7
-23.2
-16.2
-19.1
-18.5
-18.0
-20.2
-13.9
-17.3
-24.8
Aya 101
0.0
-2.3
-6.3
-8.1
-2.9
-3.5
-9.3
-4.0
-2.9
-4.6
-6.3
-1.8
BLOOMZ 7b1
0.0
-1.7
-0.5
-11.6
-9.3
-4.6
-8.1
-11.0
-9.2
-2.9
-11.0
0.0
Table A.12: Results of State-of-the-Art Models on Machine-Translated MMLU College Medicine. Top state-of-the-art
models were evaluated out-of-the-box (no fine-tuning) on MMLU College Medicine (medical domain knowledge task) test
datasets that were machine-translated from English into the target language or backtranslated from the human-translated version
back into English. Google Translate was used for machine translations in all languages except Setswana (tn), where GPT-4o
was used. Results are provided for 11 low-resource African languages of focus: Afrikaans (af), Zulu (zu), Xhosa (xh) (datasets
for these three languages were sourced from (BMGF 2024)), Amharic (am), Bambara (bm), Igbo (ig), Sepedi (nso), Shona (sn),
Sesotho (st), Setswana (tn), and Tsonga (ts). Results on English (en) without any translation are also provided as a reference.
Differences with corresponding numbers from Table 2 are given, with negative values indicating that machine translation led to
greater performance than human-translation. All numbers are 5-shot performance accuracy.

--- Page 28 ---

MMLU Clinical Knowledge
en
af
zu
xh
am
bm
ig
nso
sn
st
tn
ts
Machine Translation (en →x)
GPT-4o
89.8
88.3
80.4
79.2
64.5
41.1
72.8
76.6
81.9
80.4
69.8
72.5
GPT-4
84.2
80.0
71.3
69.1
42.6
36.2
64.9
58.9
74.7
70.9
62.3
61.1
GPT-3.5
72.5
63.8
40.4
40.0
30.9
34.7
35.8
33.6
41.1
33.2
34.0
32.5
Llama 3 70B IT
82.3
69.4
41.5
42.3
27.5
32.1
44.5
34.7
44.2
38.1
36.2
37.0
Llama 3 8B IT
69.1
50.2
37.0
31.3
24.2
34.3
40.0
37.7
38.1
35.8
34.7
32.1
Phi 3 Mini 4K IT
70.6
41.1
30.6
30.9
24.9
32.1
37.7
32.1
33.2
27.9
30.6
27.9
Aya 23 35B
69.4
55.5
37.4
33.2
30.6
29.1
35.8
35.8
38.1
35.1
30.6
37.0
Aya 101
45.3
42.6
40.8
38.9
37.0
29.1
35.5
37.4
39.2
39.6
40.0
35.1
BLOOMZ 7b1
44.9
28.7
32.1
32.8
26.0
30.2
29.4
30.9
37.4
30.6
29.4
33.2
Difference Between Human (Table 2) and Machine Translation
GPT-4o
0.0
-1.1
-0.8
-0.7
6.1
-1.1
-9.8
-4.1
-1.5
-11.0
1.5
-8.0
GPT-4
0.0
1.9
-1.1
-0.8
11.4
-1.5
-10.2
-0.8
-7.5
-6.7
-3.4
-5.3
GPT-3.5
0.0
-1.2
-1.2
-2.6
-0.7
-3.4
-1.5
-0.4
0.0
1.1
-3.4
0.3
Llama 3 70B IT
0.0
1.9
-2.3
-3.8
6.1
0.4
-10.9
2.3
-0.8
5.7
3.0
-3.0
Llama 3 8B IT
0.0
-4.9
-0.4
3.4
0.7
-2.2
-3.8
-2.2
1.1
3.4
-1.5
-0.4
Phi 3 Mini 4K IT
0.0
-0.3
-1.5
-0.3
7.2
-4.9
-4.1
0.7
0.0
3.0
5.2
1.9
Aya 23 35B
0.0
-0.4
-4.9
0.4
-1.5
4.1
-3.3
1.6
-5.6
-0.8
0.3
-4.5
Aya 101
0.0
0.0
-2.7
-3.4
1.9
-0.8
-0.8
-0.8
5.0
-2.6
-9.4
-4.2
BLOOMZ 7b1
0.0
4.5
-1.5
0.4
2.3
2.3
-2.6
3.8
-6.8
1.5
-2.2
-1.9
Machine Backtranslation (x →en)
GPT-4o
89.8
87.5
78.9
77.7
86.4
66.4
58.9
83.4
75.8
65.7
67.2
64.9
GPT-4
84.2
81.5
72.5
68.3
76.6
59.6
50.9
73.6
68.3
63.0
61.9
60.4
GPT-3.5
72.5
69.1
60.4
61.9
63.8
55.1
49.8
67.5
61.5
55.5
55.5
56.6
Llama 3 70B IT
82.3
81.5
66.4
68.7
74.0
56.2
54.0
73.2
67.5
61.9
60.0
57.4
Llama 3 8B IT
69.1
65.7
58.1
60.0
61.1
51.3
43.8
59.6
55.1
55.8
54.0
50.9
Phi 3 Mini 4K IT
70.6
70.9
57.4
56.2
66.0
52.8
49.8
64.5
60.4
56.2
58.5
52.5
Aya 23 35B
69.4
70.6
58.9
59.6
67.2
52.5
47.9
64.5
57.4
54.0
51.7
52.5
Aya 101
45.3
43.8
43.0
38.9
41.9
35.5
39.6
42.6
42.6
38.9
38.1
36.2
BLOOMZ 7b1
44.9
49.1
42.6
42.3
43.4
38.9
40.8
45.7
41.9
40.4
38.1
40.8
Difference Between Human (Table 2) and Machine Translation
GPT-4o
0.0
-0.3
0.7
0.8
-15.8
-26.4
4.1
-10.9
4.6
3.7
4.1
-0.4
GPT-4
0.0
0.4
-2.3
0.0
-22.6
-24.9
3.8
-15.5
-1.1
1.2
-3.0
-4.6
GPT-3.5
0.0
-6.5
-21.2
-24.5
-33.6
-23.8
-15.5
-34.3
-20.4
-21.2
-24.9
-23.8
Llama 3 70B IT
0.0
-10.2
-27.2
-30.2
-40.4
-23.7
-20.4
-36.2
-24.1
-18.1
-20.8
-23.4
Llama 3 8B IT
0.0
-20.4
-21.5
-25.3
-36.2
-19.2
-7.6
-24.1
-15.9
-16.6
-20.8
-19.2
Phi 3 Mini 4K IT
0.0
-30.1
-28.3
-25.6
-33.9
-25.6
-16.2
-31.7
-27.2
-25.3
-22.7
-22.7
Aya 23 35B
0.0
-15.5
-26.4
-26.0
-38.1
-19.3
-15.4
-27.1
-24.9
-19.7
-20.8
-20.0
Aya 101
0.0
-1.2
-4.9
-3.4
-3.0
-7.2
-4.9
-6.0
1.6
-1.9
-7.5
-5.3
BLOOMZ 7b1
0.0
-15.9
-12.0
-9.1
-15.1
-6.4
-14.0
-11.0
-11.3
-8.3
-10.9
-9.5
Table A.13: Results of State-of-the-Art Models on Machine-Translated MMLU Clinical Knowledge. Top state-of-the-art
models were evaluated out-of-the-box (no fine-tuning) on MMLU Clinical Knowledge (medical domain knowledge task) test
datasets that were machine-translated from English into the target language or backtranslated from the human-translated version
back into English. Google Translate was used for machine translations in all languages except Setswana (tn), where GPT-4o
was used. Results are provided for 11 low-resource African languages of focus: Afrikaans (af), Zulu (zu), Xhosa (xh) (datasets
for these three languages were sourced from (BMGF 2024)), Amharic (am), Bambara (bm), Igbo (ig), Sepedi (nso), Shona (sn),
Sesotho (st), Setswana (tn), and Tsonga (ts). Results on English (en) without any translation are also provided as a reference.
Differences with corresponding numbers from Table 2 are given, with negative values indicating that machine translation led to
greater performance than human-translation. All numbers are 5-shot performance accuracy.

--- Page 29 ---

MMLU Virology
en
af
zu
xh
am
bm
ig
nso
sn
st
tn
ts
Machine Translation (en →x)
GPT-4o
60.2
57.8
54.2
51.8
49.4
28.9
48.2
50.0
51.2
54.8
54.2
51.2
GPT-4
59.6
57.2
53.6
53.0
37.3
32.5
50.0
45.8
50.6
48.8
50.0
46.4
GPT-3.5
51.8
44.6
31.3
31.9
31.9
35.5
26.5
34.3
34.3
31.9
31.3
35.5
Llama 3 70B IT
53.6
47.0
35.5
31.9
30.1
31.3
30.7
26.5
28.9
28.3
29.5
33.1
Llama 3 8B IT
51.8
42.8
24.1
26.5
27.7
29.5
28.9
27.7
24.7
25.3
28.9
26.5
Phi 3 Mini 4K IT
48.8
39.8
26.5
25.9
22.9
27.7
25.9
26.5
28.9
26.5
27.9
32.5
Aya 23 35B
49.4
42.2
29.5
26.5
27.7
23.5
29.5
27.1
32.5
26.5
27.1
24.7
Aya 101
33.1
38.6
39.2
30.7
30.1
25.3
31.3
28.3
36.1
31.3
34.3
29.5
BLOOMZ 7b1
38.0
27.7
28.9
24.7
25.9
22.9
27.7
27.1
30.1
27.1
24.1
27.1
Difference Between Human (Table 2) and Machine Translation
GPT-4o
0.0
-2.4
-3.0
-1.2
1.8
3.6
-4.2
0.0
1.8
-7.2
-5.4
-5.4
GPT-4
0.0
1.8
-4.2
-2.4
8.5
-0.6
-5.4
0.6
-1.2
-3.6
-6.0
-6.6
GPT-3.5
0.0
-1.8
-0.6
5.4
-2.4
0.6
1.8
-0.6
-3.0
-1.8
-1.2
-4.8
Llama 3 70B IT
0.0
-0.6
-6.6
-4.8
6.0
4.2
4.2
0.0
2.4
1.2
-1.2
-1.8
Llama 3 8B IT
0.0
-4.2
4.8
0.6
0.6
-9.0
-4.8
0.0
-2.4
0.0
-1.2
3.0
Phi 3 Mini 4K IT
0.0
-9.7
0.6
-0.6
4.2
-2.4
6.6
1.2
-0.6
-2.4
-2.6
0.0
Aya 23 35B
0.0
0.0
-4.8
0.0
11.5
4.2
-9.6
1.2
-4.2
0.0
-1.2
-1.2
Aya 101
0.0
-3.7
-5.5
0.6
6.0
-3.6
-1.2
7.2
-4.8
3.6
-1.2
0.0
BLOOMZ 7b1
0.0
-1.2
-2.4
0.0
-4.8
-1.8
-1.2
-3.0
1.2
0.6
3.6
-0.6
Machine Backtranslation (x →en)
GPT-4o
60.2
55.4
50.6
50.6
57.2
47.6
50.0
53.0
55.4
45.8
46.4
50.0
GPT-4
59.6
56.0
49.4
50.0
54.8
47.0
47.0
53.0
52.4
41.0
39.2
50.6
GPT-3.5
51.8
47.6
44.6
42.8
48.8
48.2
40.4
45.2
44.0
44.6
39.2
45.2
Llama 3 70B IT
53.6
54.2
46.4
43.4
55.4
44.0
41.6
46.4
48.2
41.0
39.2
47.0
Llama 3 8B IT
51.8
48.2
41.0
43.4
47.0
44.0
39.2
44.0
46.4
37.3
41.0
41.0
Phi 3 Mini 4K IT
48.8
47.0
42.2
42.2
50.0
40.4
39.8
39.8
38.6
39.2
41.0
43.4
Aya 23 35B
49.4
49.4
43.4
44.0
50.0
45.2
41.6
45.2
43.4
36.7
42.8
44.6
Aya 101
33.1
36.1
37.3
35.5
30.7
35.5
34.3
29.5
30.7
34.9
35.5
32.5
BLOOMZ 7b1
38.0
41.0
38.0
33.7
33.1
30.1
27.7
34.9
33.1
28.9
31.9
28.3
Difference Between Human (Table 2) and Machine Translation
GPT-4o
0.0
0.0
0.6
0.0
-6.0
-15.1
-6.0
-3.0
-2.4
1.8
2.4
-4.2
GPT-4
0.0
3.0
0.0
0.6
-9.0
-15.1
-2.4
-6.6
-3.0
4.2
4.8
-10.8
GPT-3.5
0.0
-4.8
-13.9
-5.5
-19.3
-12.1
-12.1
-11.5
-12.7
-14.5
-9.1
-14.5
Llama 3 70B IT
0.0
-7.8
-17.5
-16.3
-19.3
-8.5
-6.7
-19.9
-16.9
-11.5
-10.9
-15.7
Llama 3 8B IT
0.0
-9.6
-12.1
-16.3
-18.7
-23.5
-15.1
-16.3
-24.1
-12.0
-13.3
-11.5
Phi 3 Mini 4K IT
0.0
-16.9
-15.1
-16.9
-22.9
-15.1
-7.3
-12.1
-10.3
-15.1
-15.7
-10.9
Aya 23 35B
0.0
-7.2
-18.7
-17.5
-10.8
-17.5
-21.7
-16.9
-15.1
-10.2
-16.9
-21.1
Aya 101
0.0
-1.2
-3.6
-4.2
5.4
-13.8
-4.2
6.0
0.6
0.0
-2.4
-3.0
BLOOMZ 7b1
0.0
-14.5
-11.5
-9.0
-12.0
-9.0
-1.2
-10.8
-1.8
-1.2
-4.2
-1.8
Table A.14: Results of State-of-the-Art Models on Machine-Translated MMLU Virology. Top state-of-the-art models
were evaluated out-of-the-box (no fine-tuning) on MMLU Virology (medical domain knowledge task) test datasets that were
machine-translated from English into the target language or backtranslated from the human-translated version back into English.
Google Translate was used for machine translations in all languages except Setswana (tn), where GPT-4o was used. Results
are provided for 11 low-resource African languages of focus: Afrikaans (af), Zulu (zu), Xhosa (xh) (datasets for these three
languages were sourced from (BMGF 2024)), Amharic (am), Bambara (bm), Igbo (ig), Sepedi (nso), Shona (sn), Sesotho (st),
Setswana (tn), and Tsonga (ts). Results on English (en) without any translation are also provided as a reference. Differences
with corresponding numbers from Table 2 are given, with negative values indicating that machine translation led to greater
performance than human-translation. All numbers are 5-shot performance accuracy.

--- Page 30 ---

Belebele
en
af
zu
xh
am
bm
ig
nso
sn
st
tn
ts
Machine Translation (en →x)
GPT-4o
95.9
94.8
86.0
86.8
76.8
41.4
81.4
86.3
85.7
88.0
80.4
81.4
GPT-4
96.1
93.4
82.2
82.8
62.7
37.0
74.2
72.7
82.0
81.8
75.6
73.6
GPT-3.5
86.2
75.4
35.1
32.9
32.4
30.4
32.0
35.8
32.1
33.3
33.0
34.2
Llama 3 70B IT
94.6
85.4
42.0
38.7
33.9
35.0
45.3
39.1
37.7
37.7
38.8
41.0
Llama 3 8B IT
80.0
69.6
36.3
36.1
33.0
34.1
40.1
33.0
31.4
31.1
33.7
33.3
Phi 3 Mini 4K IT
89.2
52.6
27.6
28.0
27.1
26.9
28.2
30.4
28.3
31.0
28.0
31.0
Aya 23 35B
93.6
84.8
39.3
37.6
28.9
31.4
38.9
35.7
36.3
37.4
36.2
36.4
Aya 101
79.7
76.9
62.2
62.9
66.7
47.1
61.1
66.1
63.3
64.1
63.9
56.1
BLOOMZ 7b1
79.0
35.4
36.6
36.7
24.1
28.7
37.2
38.3
34.3
33.1
37.6
38.8
Difference Between Human (Table 2) and Machine Translation
GPT-4o
0.0
-0.4
-6.3
-4.0
1.2
-3.1
-10.1
-9.1
-4.7
-8.0
-3.4
-4.6
GPT-4
0.0
0.2
-6.3
-6.5
-1.4
0.9
-9.8
-8.1
-4.4
-5.5
-8.0
-3.6
GPT-3.5
0.0
0.3
-1.3
-1.1
-2.4
0.2
-2.8
-3.5
2.5
-1.2
-1.3
2.1
Llama 3 70B IT
0.0
-0.6
-5.3
-1.9
1.2
0.6
-9.4
-2.0
0.4
-1.8
-2.4
-0.3
Llama 3 8B IT
0.0
-0.2
-3.7
-3.1
-2.8
-2.1
-4.4
-0.1
2.5
1.1
0.3
0.1
Phi 3 Mini 4K IT
0.0
0.0
0.7
1.1
1.6
4.8
0.6
1.2
0.8
-0.4
1.2
3.3
Aya 23 35B
0.0
-1.2
-6.1
-2.0
0.1
3.2
-10.2
-1.1
1.5
-1.8
0.6
1.0
Aya 101
0.0
0.5
-2.9
-2.2
1.0
-6.4
-10.4
-6.8
-5.5
-4.2
-6.1
-5.1
BLOOMZ 7b1
0.0
1.3
-0.8
-1.7
0.2
2.9
-6.0
-4.2
2.4
1.6
-1.7
0.9
Machine Backtranslation (x →en)
GPT-4o
95.9
92.0
71.0
77.0
81.2
49.1
62.8
77.9
75.4
76.8
67.7
75.0
GPT-4
96.1
92.0
69.2
76.4
81.1
48.1
62.2
77.0
73.2
75.8
66.3
72.7
GPT-3.5
86.2
80.4
62.1
66.0
69.1
41.8
52.7
66.9
63.2
64.8
60.4
64.1
Llama 3 70B IT
94.6
89.8
65.7
72.7
77.2
40.0
53.4
71.6
68.3
69.8
61.8
68.4
Llama 3 8B IT
80.0
76.0
54.3
58.3
62.9
38.8
48.2
60.0
56.6
58.7
50.7
57.4
Phi 3 Mini 4K IT
89.2
84.0
62.2
64.7
72.2
43.3
50.3
68.8
62.0
65.3
58.2
62.9
Aya 23 35B
93.6
89.8
66.6
72.1
76.6
43.9
52.2
74.2
68.3
71.8
63.4
69.1
Aya 101
79.7
76.7
57.7
61.4
67.9
39.6
48.9
62.1
59.2
59.1
57.7
60.1
BLOOMZ 7b1
79.0
74.6
56.9
58.1
61.9
37.4
45.7
58.3
55.4
57.0
56.3
58.1
Difference Between Human (Table 2) and Machine Translation
GPT-4o
0.0
2.4
8.7
5.8
-3.2
-10.8
8.5
-0.7
5.6
3.2
9.3
1.8
GPT-4
0.0
1.6
6.7
-0.1
-19.8
-10.2
2.2
-12.4
4.4
0.5
1.3
-2.7
GPT-3.5
0.0
-4.7
-28.3
-34.2
-39.1
-11.2
-23.5
-34.6
-28.6
-32.7
-28.7
-27.8
Llama 3 70B IT
0.0
-5.0
-29.0
-35.9
-42.1
-4.4
-17.5
-34.5
-30.2
-33.9
-25.4
-27.7
Llama 3 8B IT
0.0
-6.6
-21.7
-25.3
-32.7
-6.8
-12.5
-27.1
-22.7
-26.5
-16.7
-24.0
Phi 3 Mini 4K IT
0.0
-31.4
-33.9
-35.6
-43.5
-11.6
-21.5
-37.2
-32.9
-34.7
-29.0
-28.6
Aya 23 35B
0.0
-6.2
-33.4
-36.5
-47.6
-9.3
-23.5
-39.6
-30.5
-36.2
-26.6
-31.7
Aya 101
0.0
0.7
1.6
-0.7
-0.2
1.1
1.8
-2.8
-1.4
0.8
0.1
-9.1
BLOOMZ 7b1
0.0
-37.9
-21.1
-23.1
-37.6
-5.8
-14.5
-24.2
-18.7
-22.3
-20.4
-18.4
Table A.15: Results of State-of-the-Art Models on Machine-Translated Belebele. Top state-of-the-art models were evaluated
out-of-the-box (no fine-tuning) on Belebele (reading comprehension task) datasets that were machine-translated from English
into the target language or backtranslated from the human-translated version back into English. Google Translate was used for
machine translations in all languages except Setswana (tn), where GPT-4o was used. Results are provided for 11 low-resource
African languages of focus: Afrikaans (af), Zulu (zu), Xhosa (xh) (datasets for these three languages were sourced from (BMGF
2024)), Amharic (am), Bambara (bm), Igbo (ig), Sepedi (nso), Shona (sn), Sesotho (st), Setswana (tn), and Tsonga (ts). Results
on English (en) without any translation are also provided as a reference. Differences with corresponding numbers from Table
2 are given, with negative values indicating that machine translation led to greater performance than human-translation. All
numbers are 0-shot performance accuracy.

--- Page 31 ---

Question 1
(quality)
Question 2
(appropriateness)
Lang.
Cohen’s κ
Fleiss’ κ
Cohen’s κ
Fleiss’ κ
af
0.136
0.134
0.008
-0.009
zu
-0.023
-0.025
-0.037
-0.038
xh
0.158
0.150
0.027
-0.042
am
0.008
-0.085
-0.002
-0.111
bm
0.060
0.014
0.074
0.051
ig
0.013
-0.214
0.011
-0.073
nso
0.157
0.154
0.041
0.039
sn
0.211
0.179
0.029
-0.001
st
0.012
-0.076
0.006
-0.070
tn
0.016
-0.046
0.002
-0.075
ts
0.133
0.093
0.045
0.023
Table A.16: Inter-rater Reliability between Evaluators. The above table shows Cohen’s Kappa (κ) and Fleiss’ Kappa (κ)
scores for each question asked of the human evaluators (translation quality and appropriateness). The translation quality ques-
tion asked the evaluators to rate the quality of the translation as “Good translation”, “Incorrect, but someone could understand
the idea”, or “Completely wrong”. The translation appropriateness question asked evaluators to determine whether the trans-
lation could be considered “strange, incoherent, or disrespectful” in a typical conversational context, with possible options of
“No, the sentence is typical”, “Maybe, I’m not sure”, “Yes, the sentence is strange, incoherent, or disrespectful”, or “I don’t
understand the sentence”. We observe that there was little agreement on appropriateness even when agreement was present for
translation quality, indicating that different evaluators may be sensitive to different aspects of appropriateness. See Tables A.1
and A.10 for the full agreement matrices for each language. Language codes are as follows: Afrikaans (af), Zulu (zu), Xhosa
(xh), Amharic (am), Bambara (bm), Igbo (ig), Sepedi (nso), Shona (sn), Sesotho (st), Setswana (tn), Tsonga (ts).

--- Page 32 ---

Language
xh
zu
af
ig
sn
ts
st
nso
tn
bm
am
A. Target Language Performance on “appropriate” subset
Sample Size
1379
1355
1086
809
1548
1422
1461
1711
1433
1019
1370
GPT 4o
65.5%
69.1%
81.7%
60.7%
71.7%
63.5%
68.2%
64.7%
64.8%
51.4%
60.0%
GPT 4
61.4%
65.3%
80.0%
60.7%
67.4%
58.7%
65.2%
58.9%
60.1%
52.2%
51.7%
GPT 3.5
51.6%
49.7%
56.7%
51.9%
51.1%
50.4%
49.9%
50.8%
50.7%
49.6%
50.4%
B. Target Language Performance on “inappropriate” subset
Sample Size
388
412
681
958
219
345
306
56
334
748
397
GPT 4o
65.7%
64.3%
74.9%
61.7%
54.5%
60.2%
64.5%
56.0%
62.7%
49.4%
58.0%
GPT 4
60.7%
59.2%
72.3%
57.5%
53.6%
53.3%
58.7%
59.5%
62.1%
49.9%
49.3%
GPT 3.5
53.5%
50.6%
51.9%
50.0%
53.9%
51.3%
52.7%
56.5%
53.9%
51.4%
51.4%
C. English Performance on “appropriate” subset
Sample Size
1379
1355
1086
809
1548
1422
1461
1711
1433
1019
1370
GPT 4o
83.9%
85.1%
85.3%
84.9%
84.3%
84.2%
84.0%
83.6%
84.6%
83.4%
83.2%
GPT 4
83.1%
83.1%
84.8%
83.0%
83.3%
83.8%
83.5%
82.9%
83.2%
82.1%
82.5%
GPT 3.5
58.7%
58.5%
59.9%
61.0%
59.0%
59.0%
59.4%
58.8%
58.6%
57.0%
58.7%
D. English Performance on “inappropriate” subset
Sample Size
388
412
681
958
219
345
306
56
334
748
397
GPT 4o
84.2%
80.0%
81.8%
83.2%
81.3%
82.7%
83.9%
94.0%
81.3%
84.7%
86.6%
GPT 4
82.9%
82.8%
80.2%
83.1%
81.4%
80.1%
80.7%
86.3%
82.4%
84.3%
85.1%
GPT 3.5
59.0%
59.7%
57.0%
56.9%
57.4%
57.9%
55.9%
59.5%
59.7%
61.1%
59.2%
E. Difference in Target Language Performance on “appropriate” subset vs. “inappropriate” subset (A.-B.)
GPT 4o
-0.2%
4.8%
6.8%
-1.0%
17.2%
3.3%
3.7%
8.8%
2.2%
2.0%
2.0%
GPT 4
0.8%
6.1%
7.8%
3.2%
13.8%
5.4%
6.5%
-0.6%
-2.0%
2.4%
2.4%
GPT 3.5
-1.9%
-1.0%
4.7%
1.8%
-2.7%
-0.9%
-2.8%
-5.8%
-3.2%
-1.8%
-1.0%
F. Difference in English Performance on “appropriate” subset vs. “inappropriate” subset (C.-D.)
GPT 4o
-0.3%
5.1%
3.5%
1.7%
3.0%
1.5%
0.1%
-10.4%
3.2%
-1.3%
-3.5%
GPT 4
0.2%
0.3%
4.7%
0.0%
1.8%
3.7%
2.8%
-3.4%
0.7%
-2.2%
-2.6%
GPT 3.5
-0.3%
-1.2%
2.9%
4.1%
1.6%
1.1%
3.5%
-0.8%
-1.1%
-4.1%
-0.5%
G. Comparative Diff. Between Target Lang. and Eng. Performance on “appropriate” vs. “inappropriate” subsets (E.-F.)
GPT 4o
-0.2%
-0.4%
3.3%
-2.7%
14.2%
1.7%
3.6%
19.2%
-1.1%
3.2%
5.4%
GPT 4
0.6%
5.9%
3.1%
3.2%
12.0%
1.8%
3.7%
2.7%
-2.7%
4.6%
5.0%
GPT 3.5
-1.6%
0.3%
1.9%
-2.3%
-4.3%
-2.1%
-6.3%
-5.0%
-2.1%
2.3%
-0.5%
Table A.17: GPT-Family Performance on Winogrande Split by Cultural Appropriateness (All QA Pairs). The table above
shows the performance of GPT-3.5, GPT-4, and GPT-4o on Winogrande when split by human annotations of cultural ap-
propriateness for each language. Bold values indicate the highest-performing values or model (overall across all languages,
determined by the largest sum of performance scores between the models) for the given subtable. Evaluators were asked if
each Winogrande QA pair could be considered “strange, incoherent, or disrespectful in a typical conversational context”, with
the following possible options: (i) “No, the sentence is typical”, (ii) “Not sure”, (iii) “Yes, the sentence is strange, incoherent,
or disrespectful”, or (iv) “I don’t understand the sentence”. A dataset QA pair is considered “inappropriate” if at least one
evaluator marked it as not “typical”. Language codes are as follows: Xhosa (xh), Zulu (zu), Afrikaans (af), Igbo (ig), Shona
(sn), Tsonga (ts), Sesotho (st), Sepedi (nso), Setswana (tn), Bambara (bm), Amharic (am).

--- Page 33 ---

Language
xh
zu
af
ig
sn
ts
st
nso
tn
bm
am
A. Target Language Performance on “appropriate” subset
Sample Size
1379
1355
1086
809
1548
1422
1461
1710
1433
1019
1370
GPT 4o
65.5%
69.1%
81.7%
60.7%
71.7%
63.5%
68.2%
64.8%
64.8%
51.4%
60.0%
GPT 4
61.4%
65.3%
80.0%
60.7%
67.4%
58.7%
65.2%
58.9%
60.1%
52.2%
51.7%
GPT 3.5
51.6%
49.7%
56.7%
51.9%
51.1%
50.4%
49.9%
50.8%
50.7%
49.6%
50.4%
B. Target Language Performance on “inappropriate” subset
Sample Size
385
409
676
956
207
339
306
56
331
737
397
GPT 4o
65.7%
64.1%
75.2%
61.7%
55.4%
60.6%
64.5%
56.0%
62.8%
49.4%
58.0%
GPT 4
60.9%
59.4%
72.5%
57.4%
54.4%
53.6%
58.7%
59.5%
62.1%
50.0%
49.3%
GPT 3.5
53.9%
50.7%
52.0%
50.0%
53.9%
51.0%
52.7%
56.5%
53.7%
51.5%
51.4%
C. English Performance on “appropriate” subset
Sample Size
1379
1355
1086
809
1548
1422
1461
1710
1433
1019
1370
GPT 4o
83.9%
85.1%
85.3%
84.9%
84.3%
84.2%
84.0%
83.7%
84.6%
83.4%
83.2%
GPT 4
83.1%
83.1%
84.8%
83.0%
83.3%
83.8%
83.5%
83.0%
83.2%
82.1%
82.5%
GPT 3.5
58.7%
58.5%
59.9%
61.0%
59.0%
59.0%
59.4%
58.8%
58.6%
57.0%
58.7%
D. English Performance on “inappropriate” subset
Sample Size
385
409
676
956
207
339
306
56
331
737
397
GPT 4o
84.1%
79.9%
81.8%
83.2%
81.2%
82.5%
83.9%
94.0%
81.2%
84.5%
86.6%
GPT 4
83.0%
82.7%
80.0%
83.1%
81.6%
79.7%
80.7%
86.3%
82.3%
84.3%
85.1%
GPT 3.5
59.2%
59.7%
57.1%
56.9%
57.3%
57.7%
55.9%
59.5%
59.4%
61.0%
59.2%
E. Difference in Target Language Performance on “appropriate” subset vs. “inappropriate” subset (A.-B.)
GPT 4o
-0.2%
4.9%
6.5%
-1.0%
16.3%
2.9%
3.7%
8.8%
2.0%
2.0%
2.0%
GPT 4
0.6%
5.9%
7.6%
3.3%
12.9%
5.2%
6.5%
-0.6%
-2.1%
2.2%
2.4%
GPT 3.5
-2.2%
-1.0%
4.6%
1.8%
-2.8%
-0.7%
-2.8%
-5.8%
-3.0%
-1.9%
-1.0%
F. Difference in English Performance on “appropriate” subset vs. “inappropriate” subset (C.-D.)
GPT 4o
-0.2%
5.3%
3.5%
1.6%
3.2%
1.7%
0.1%
-10.4%
3.4%
-1.1%
-3.5%
GPT 4
0.0%
0.4%
4.8%
-0.1%
1.6%
4.0%
2.8%
-3.3%
0.9%
-2.2%
-2.6%
GPT 3.5
-0.5%
-1.2%
2.7%
4.1%
1.7%
1.3%
3.5%
-0.7%
-0.8%
-4.0%
-0.5%
G. Comparative Diff. Between Target Lang. and Eng. Performance on “appropriate” vs. “inappropriate” subsets (E.-F.)
GPT 4o
0.0%
-0.3%
3.0%
-2.6%
13.2%
1.2%
3.6%
19.2%
-1.4%
3.1%
5.4%
GPT 4
0.5%
5.5%
2.8%
3.4%
11.3%
1.1%
3.7%
2.7%
-3.0%
4.4%
5.0%
GPT 3.5
-1.7%
0.2%
1.9%
-2.3%
-4.5%
-1.9%
-6.3%
-5.1%
-2.1%
2.0%
-0.5%
Table A.18: GPT-Family Performance on Winogrande Split by Cultural Appropriateness (QA Pairs with at Least One
“good” Quality Annotation). The table above shows the performance of GPT-3.5, GPT-4, and GPT-4o on Winogrande when
split by human annotations of cultural appropriateness for each language. Bold values indicate the highest-performing values
or model (overall across all languages, determined by the largest sum of performance scores between the models) for the given
subtable. Evaluators were asked if each Winogrande QA pair could be considered “strange, incoherent, or disrespectful in a
typical conversational context”, with the following possible options: (i) “No, the sentence is typical”, (ii) “Not sure”, (iii) “Yes,
the sentence is strange, incoherent, or disrespectful”, or (iv) “I don’t understand the sentence”. A dataset QA pair is considered
“inappropriate” if at least one evaluator marked it as not “typical”. QA pairs are only included in this calculation if at least one
evaluator marked it as a “good” or “understandable” translation. Language codes are as follows: Xhosa (xh), Zulu (zu),
Afrikaans (af), Igbo (ig), Shona (sn), Tsonga (ts), Sesotho (st), Sepedi (nso), Setswana (tn), Bambara (bm), Amharic (am).

--- Page 34 ---

Language
xh
zu
af
ig
sn
ts
st
nso
tn
bm
am
A. Target Language Performance on “appropriate” subset
Sample Size
1371
1339
1086
809
1546
1379
1452
1701
1433
1016
1369
GPT 4o
65.6%
69.3%
81.7%
60.7%
71.8%
64.1%
68.2%
64.8%
64.8%
51.4%
60.0%
GPT 4
61.6%
65.5%
80.0%
60.7%
67.4%
59.3%
65.4%
58.8%
60.1%
52.2%
51.6%
GPT 3.5
51.6%
49.8%
56.7%
51.9%
51.1%
50.3%
49.8%
50.6%
50.7%
49.7%
50.4%
B. Target Language Performance on “inappropriate” subset
Sample Size
292
324
609
758
146
255
259
30
303
569
390
GPT 4o
66.2%
65.0%
76.1%
61.3%
59.1%
63.4%
64.2%
58.9%
62.8%
50.7%
58.4%
GPT 4
61.5%
59.3%
72.7%
57.8%
59.6%
55.0%
58.4%
58.9%
62.2%
50.3%
49.8%
GPT 3.5
54.2%
50.0%
51.6%
49.1%
51.1%
52.0%
53.5%
54.4%
53.8%
54.2%
51.8%
C. English Performance on “appropriate” subset
Sample Size
1371
1339
1086
809
1546
1379
1452
1701
1433
1016
1369
GPT 4o
83.8%
85.3%
85.3%
84.9%
84.3%
84.3%
84.0%
83.6%
84.6%
83.4%
83.2%
GPT 4
83.1%
83.1%
84.8%
83.0%
83.3%
83.9%
83.7%
83.0%
83.2%
82.1%
82.4%
GPT 3.5
58.8%
58.7%
59.9%
61.0%
59.0%
58.9%
59.4%
58.7%
58.6%
57.1%
58.7%
D. English Performance on “inappropriate” subset
Sample Size
292
324
609
758
146
255
259
30
303
569
390
GPT 4o
86.2%
80.8%
81.8%
83.2%
76.9%
85.0%
82.9%
93.3%
81.7%
84.2%
86.9%
GPT 4
83.2%
83.1%
79.6%
82.6%
79.7%
79.7%
80.2%
82.2%
83.3%
83.9%
85.0%
GPT 3.5
58.3%
60.7%
57.3%
56.6%
57.8%
58.7%
56.0%
55.6%
59.3%
62.8%
59.7%
E. Difference in Target Language Performance on “appropriate” subset vs. “inappropriate” subset (A.-B.)
GPT 4o
-0.6%
4.3%
5.6%
-0.6%
12.6%
0.7%
4.0%
5.9%
2.0%
0.7%
1.6%
GPT 4
0.0%
6.3%
7.3%
2.9%
7.8%
4.2%
7.0%
-0.1%
-2.1%
2.0%
1.8%
GPT 3.5
-2.7%
-0.2%
5.1%
2.8%
0.0%
-1.7%
-3.7%
-3.8%
-3.1%
-4.5%
-1.4%
F. Difference in English Performance on “appropriate” subset vs. “inappropriate” subset (C.-D.)
GPT 4o
-2.4%
4.5%
3.5%
1.7%
7.4%
-0.7%
1.1%
-9.8%
2.8%
-0.9%
-3.8%
GPT 4
-0.2%
-0.1%
5.3%
0.4%
3.6%
4.2%
3.5%
0.7%
-0.1%
-1.9%
-2.6%
GPT 3.5
0.4%
-2.0%
2.6%
4.4%
1.3%
0.2%
3.5%
3.1%
-0.7%
-5.7%
-1.0%
G. Comparative Diff. Between Target Lang. and Eng. Performance on “appropriate” vs. “inappropriate” subsets (E.-F.)
GPT 4o
1.8%
-0.2%
2.2%
-2.3%
5.3%
1.3%
2.9%
15.7%
-0.8%
1.6%
5.4%
GPT 4
0.2%
6.3%
2.1%
2.5%
4.2%
0.1%
3.4%
-0.8%
-2.0%
3.9%
4.4%
GPT 3.5
-3.1%
1.8%
2.5%
-1.6%
-1.3%
-1.9%
-7.2%
-6.9%
-2.4%
1.2%
-0.3%
Table A.19: GPT-Family Performance on Winogrande Split by Cultural Appropriateness (QA Pairs with Only “good”
Quality Annotations). The table above shows the performance of GPT-3.5, GPT-4, and GPT-4o on Winogrande when split
by human annotations of cultural appropriateness for each language. Bold values indicate the highest-performing values or
model (overall across all languages, determined by the largest sum of performance scores between the models) for the given
subtable. Evaluators were asked if each Winogrande QA pair could be considered “strange, incoherent, or disrespectful in a
typical conversational context”, with the following possible options: (i) “No, the sentence is typical”, (ii) “Not sure”, (iii) “Yes,
the sentence is strange, incoherent, or disrespectful”, or (iv) “I don’t understand the sentence”. A dataset QA pair is considered
“inappropriate” if at least one evaluator marked it as not “typical”. QA pairs are only included in this calculation if both
evaluators marked it as a “good” or “understandable” translation. Language codes are as follows: Xhosa (xh), Zulu (zu),
Afrikaans (af), Igbo (ig), Shona (sn), Tsonga (ts), Sesotho (st), Sepedi (nso), Setswana (tn), Bambara (bm), Amharic (am).

--- Page 35 ---

Winogrande
en
af
zu
xh
am
bm
ig
nso
sn
st
tn
ts
Base
Llama 3
70B IT
61.2
51.0
50.4
50.8
50.8
50.5
50.5
50.5
50.4
50.4
50.5
50.4
Winogrande
train (small)
en→
88.0
±0.3
73.4
±1.6
50.7
±0.8
52.2
±1.8
50.1
±0.9
51.0
±0.7
52.6
±0.9
50.8
±1.2
52.6
±1.5
51.1
±0.6
51.6
±0.9
49.7
±0.6
af→
87.3
±0.2
75.2
±0.9
52.7
±1.1
52.2
±1.1
49.4
±1.6
48.8
±1.1
53.2
±0.5
52.1
±1.2
52.3
±1.2
51.3
±0.1
51.3
±1.2
50.6
±0.9
zu→
74.4
±0.9
61.0
±0.5
51.2
±0.9
51.2
±0.3
49.1
±0.5
50.0
±0.7
51.9
±0.7
50.2
±0.6
51.1
±1.9
50.1
±1.3
49.4
±0.3
50.6
±0.8
xh→
70.3
±1.1
59.2
±0.5
50.6
±1.4
50.6
±0.3
49.8
±1.0
50.4
±0.4
51.6
±0.2
50.7
±2.0
50.8
±0.4
48.3
±1.8
50.0
±0.8
50.2
±2.2
am→
77.0
±0.7
66.2
±0.6
51.1
±1.5
50.1
±1.4
50.4
±1.5
50.2
±1.4
52.1
±1.2
50.5
±1.0
50.3
±0.3
51.0
±1.5
50.6
±0.8
51.7
±0.5
bm→
60.9
±0.9
52.4
±1.2
51.1
±0.5
50.7
±1.3
50.5
±0.6
49.2
±2.4
49.2
±2.1
50.4
±0.5
50.9
±1.2
49.6
±1.0
49.3
±1.1
51.1
±1.6
ig→
77.9
±0.9
64.7
±0.3
50.5
±1.1
50.0
±2.0
50.2
±0.6
50.4
±0.8
53.8
±1.2
49.9
±1.1
51.3
±1.0
51.3
±2.2
50.2
±0.7
50.5
±1.0
nso→
76.3
±1.3
63.1
±0.4
51.3
±1.9
50.7
±1.2
50.5
±0.7
50.5
±1.4
51.4
±1.2
51.2
±1.1
49.7
±1.2
51.2
±1.5
50.2
±1.0
51.1
±0.3
sn→
76.9
±1.2
65.5
±0.3
50.6
±1.5
51.2
±1.0
50.8
±1.2
51.0
±1.4
52.6
±1.2
52.0
±1.0
50.7
±0.4
50.6
±0.5
49.5
±0.9
51.3
±1.0
st→
74.6
±1.7
62.2
±0.9
49.8
±0.3
50.6
±1.5
49.8
±1.4
50.1
±1.6
52.8
±1.4
51.1
±0.7
51.3
±1.2
52.3
±1.2
50.9
±0.9
52.4
±1.3
tn→
74.2
±1.2
61.9
±0.6
49.6
±0.6
50.1
±0.9
49.9
±0.8
49.5
±2.1
51.2
±0.4
50.9
±1.7
50.9
±1.5
52.0
±0.8
51.8
±2.8
50.5
±0.6
ts→
63.5
±1.4
55.1
±0.7
49.1
±1.7
50.8
±1.1
49.3
±0.5
50.5
±0.6
52.2
±0.8
49.3
±1.6
49.7
±0.5
50.9
±0.1
49.4
±1.4
49.9
±1.1
Table A.20: Results of Cross-lingual Transfer using Llama 3 70B Instruct when Tuning on Winogrande and Testing on
Winogrande. Llama 3 70B Instruct was independently fine-tuned on the 11 African languages of focus: Afrikaans (af), Zulu
(zu), Xhosa (xh) (datasets for these three languages were sourced from (BMGF 2024)), Amharic (am), Bambara (bm), Igbo (ig),
Sepedi (nso), Shona (sn), Sesotho (st), Setswana (tn), and Tsonga (ts). Llama 3 70B Instruct was also fine-tuned on English (en)
for reference. The translated Winogrande training set (small) was used for fine-tuning. The fine-tuned models were evaluated
for their cross-lingual transfer performance on the translated Winogrande (binary choice co-reference resolution task) test set.
Columns indicate the target language of the evaluation, while the rows indicate the source language the models were fine-tuned
with (e.g. “zu→” indicates models fine-tuned with data in Zulu). All numbers are the mean 5-shot performance accuracy of
three evaluations followed by the standard deviation (±). Model fine-tuning that yielded mono-lingual improvements (relative
to the baseline) more than two standard deviations are in blue, while cross-lingual improvements (relative to the baseline) more
than two standard deviations are in green.

--- Page 36 ---

Winogrande
en
af
zu
xh
am
bm
ig
nso
sn
st
tn
ts
Base
Llama 3
70B IT
61.2
51.0
50.4
50.8
50.8
50.5
50.5
50.5
50.4
50.4
50.5
50.4
MMLU College Medicine
dev + test + val
en→
71.4
±0.5
56.9
±0.4
51.0
±0.2
50.9
±0.2
50.0
±0.2
50.4
±0.1
50.4
±0.6
50.6
±0.3
50.3
±0.3
50.5
±0.2
51.3
±0.3
50.7
±0.3
af→
68.3
±0.1
58.0
±0.6
50.8
±0.2
51.0
±0.3
50.2
±0.9
50.9
±0.4
51.3
±0.9
50.4
±0.8
50.4
±0.1
50.4
±0.7
50.2
±0.4
50.0
±0.6
zu→
71.5
±0.2
60.0
±0.2
52.4
±0.3
51.4
±0.4
50.8
±0.4
50.8
±0.4
52.5
±0.3
50.9
±1.3
50.8
±0.5
52.3
±0.3
51.0
±0.3
51.5
±0.8
xh→
69.0
±0.3
59.2
±0.2
51.0
±0.2
51.1
±0.3
50.8
±1.2
50.3
±0.4
51.0
±0.7
50.9
±0.6
50.8
±0.4
51.3
±0.3
51.1
±0.5
51.2
±0.5
am→
70.5
±0.3
60.0
±0.4
50.9
±0.2
50.8
±0.2
49.9
±0.2
50.1
±0.2
51.5
±0.2
50.4
±0.2
50.9
±0.1
50.9
±0.1
50.7
±0.4
50.6
±0.2
bm→
60.2
±0.2
53.4
±0.1
50.5
±0.1
50.6
±0.2
50.4
±0.1
50.4
±0.1
50.3
±0.1
50.4
±0.1
50.5
±0.1
50.5
±0.1
50.5
±0.0
50.4
±0.0
ig→
69.0
±0.3
59.2
±0.3
51.5
±0.9
51.6
±0.1
50.2
±0.1
50.7
±0.1
52.0
±0.3
51.1
±0.1
50.6
±0.6
51.2
±0.4
50.9
±0.2
50.8
±0.6
nso→
68.8
±0.4
59.5
±0.1
50.9
±0.3
50.8
±0.2
50.3
±0.6
50.5
±0.1
52.0
±0.3
50.7
±0.2
50.9
±0.1
51.3
±0.3
51.0
±0.6
50.8
±0.1
sn→
72.0
±0.3
60.8
±0.1
51.3
±0.2
51.4
±0.3
49.7
±1.1
50.8
±0.1
52.0
±0.5
50.8
±0.4
51.3
±0.6
51.1
±1.0
50.8
±0.6
50.9
±0.5
st→
70.2
±0.8
59.8
±0.4
51.4
±0.3
50.9
±0.1
50.8
±0.9
51.2
±0.1
52.0
±0.3
51.7
±0.8
51.1
±0.7
52.6
±0.4
51.7
±0.6
51.1
±0.4
tn→
65.2
±0.4
58.1
±0.3
51.0
±0.3
50.7
±0.2
50.8
±0.4
50.5
±0.1
51.4
±0.4
50.5
±0.1
50.7
±0.1
50.8
±0.4
50.9
±0.4
50.6
±0.3
ts→
70.7
±0.0
59.3
±0.0
50.7
±0.1
50.9
±0.1
50.5
±0.1
50.5
±0.0
51.6
±0.2
50.4
±0.6
51.0
±0.2
51.4
±0.7
50.8
±0.3
50.7
±0.2
Table A.21: Results of Cross-lingual Transfer using Llama 3 70B Instruct when Tuning on MMLU College Medicine and
Testing on Winogrande. Llama 3 70B Instruct was independently fine-tuned on the 11 African languages of focus: Afrikaans
(af), Zulu (zu), Xhosa (xh) (datasets for these three languages were sourced from (BMGF 2024)), Amharic (am), Bambara
(bm), Igbo (ig), Sepedi (nso), Shona (sn), Sesotho (st), Setswana (tn), and Tsonga (ts). Llama 3 70B Instruct was also fine-
tuned on English (en) for reference. The translated MMLU College Medicine section (dev + test + val sets) was used for
fine-tuning. The fine-tuned models were evaluated for their cross-lingual transfer performance on the translated Winogrande
(binary choice co-reference resolution task) test set. Columns indicate the target language of the evaluation, while the rows
indicate the source language the models were fine-tuned with (e.g. “zu→” indicates models fine-tuned with data in Zulu). All
numbers are the mean 5-shot performance accuracy of three evaluations followed by the standard deviation (±). Model fine-
tuning that yielded mono-lingual improvements (relative to the baseline) more than two standard deviations are in blue, while
cross-lingual improvements (relative to the baseline) more than two standard deviations are in green.

--- Page 37 ---

MMLU Clinical Knowledge
en
af
zu
xh
am
bm
ig
nso
sn
st
tn
ts
Base
Llama 3
70B IT
82.3
71.3
39.2
38.5
33.6
32.5
33.6
37.0
43.4
43.8
39.2
34.0
Winogrande
train (small)
en→
82.5
±0.8
71.5
±0.8
36.5
±4.4
37.6
±1.7
34.8
±2.3
31.1
±1.9
35.6
±1.8
37.2
±0.8
41.0
±2.5
40.0
±1.3
37.3
±2.1
35.2
±2.9
af→
83.6
±0.8
74.2
±0.8
40.2
±3.3
39.5
±2.2
38.1
±1.3
30.3
±1.5
38.7
±2.2
40.4
±3.6
43.2
±2.5
44.3
±1.9
39.1
±1.0
38.1
±2.7
zu→
81.3
±2.3
73.1
±0.8
37.1
±3.5
39.3
±2.3
39.1
±3.0
31.6
±2.3
41.3
±0.6
38.6
±0.2
42.1
±0.6
40.9
±2.6
39.1
±1.5
33.7
±2.1
xh→
81.5
±0.7
70.6
±2.3
37.0
±3.3
36.8
±2.9
32.8
±0.4
27.9
±1.9
37.5
±3.1
36.3
±3.0
41.1
±1.7
37.9
±2.5
38.4
±3.6
32.1
±0.4
am→
83.6
±0.8
76.6
±1.7
41.3
±3.0
40.3
±1.2
46.4
±2.0
31.1
±2.9
44.2
±0.8
41.6
±5.5
45.3
±1.3
42.6
±0.4
41.6
±1.7
37.6
±2.5
bm→
79.9
±1.4
67.9
±1.7
31.4
±2.6
31.2
±3.6
29.7
±1.9
25.7
±1.9
34.2
±2.9
31.2
±1.4
35.3
±2.1
33.3
±2.3
31.8
±3.5
30.7
±0.8
ig→
81.8
±1.4
74.0
±1.2
36.6
±2.3
38.1
±2.0
38.5
±5.3
26.8
±1.3
40.5
±1.7
37.1
±3.0
42.9
±1.8
43.3
±1.3
37.2
±1.9
32.2
±2.5
nso→
82.2
±0.6
72.3
±1.2
38.7
±0.9
40.1
±2.0
36.3
±1.2
27.8
±1.4
41.7
±2.9
42.5
±2.3
43.3
±0.6
40.1
±1.9
38.5
±1.0
35.5
±1.6
sn→
83.3
±1.5
72.7
±1.2
36.2
±2.7
39.0
±3.1
34.1
±0.8
30.7
±2.1
38.3
±1.1
39.7
±1.9
39.4
±2.3
38.9
±1.2
40.3
±1.6
33.0
±3.6
st→
82.6
±1.0
73.7
±2.7
39.1
±3.9
40.1
±0.5
36.4
±1.1
31.2
±1.2
39.4
±1.1
42.3
±2.4
42.5
±0.6
40.5
±2.9
41.8
±0.5
36.3
±2.0
tn→
83.9
±1.9
75.2
±0.2
40.3
±2.0
39.5
±2.3
38.5
±2.0
30.2
±0.6
43.4
±2.6
40.1
±3.0
45.9
±1.4
43.0
±3.0
41.9
±1.9
38.6
±4.8
ts→
78.9
±1.3
65.9
±1.9
32.7
±3.3
34.6
±4.1
30.9
±2.3
25.9
±2.9
35.7
±1.1
36.7
±3.2
37.7
±2.1
37.2
±0.9
34.2
±1.4
33.7
±0.5
Table A.22: Results of Cross-lingual Transfer using Llama 3 70B Instruct when Tuning on Winogrande and Testing
on MMLU Clinical Knowledge. Llama 3 70B Instruct was independently fine-tuned on the 11 African languages of focus:
Afrikaans (af), Zulu (zu), Xhosa (xh) (datasets for these three languages were sourced from (BMGF 2024)), Amharic (am),
Bambara (bm), Igbo (ig), Sepedi (nso), Shona (sn), Sesotho (st), Setswana (tn), and Tsonga (ts). Llama 3 70B Instruct was also
fine-tuned on English (en) for reference. The translated Winogrande training set (small) was used for fine-tuning. The fine-
tuned models were evaluated for their cross-lingual transfer performance on the translated MMLU Clinical Knowledge
(clinical domain knowledge task) test set. Columns indicate the target language of the evaluation, while the rows indicate the
source language the models were fine-tuned with (e.g. “zu→” indicates models fine-tuned with data in Zulu). All numbers
are the mean 5-shot performance accuracy of three evaluations followed by the standard deviation (±). Model fine-tuning that
yielded mono-lingual improvements (relative to the baseline) more than two standard deviations are in blue, while cross-lingual
improvements (relative to the baseline) more than two standard deviations are in green.

--- Page 38 ---

MMLU Clinical Knowledge
en
af
zu
xh
am
bm
ig
nso
sn
st
tn
ts
Base
Llama 3
70B IT
82.3
71.3
39.2
38.5
33.6
32.5
33.6
37.0
43.4
43.8
39.2
34.0
MMLU College Medicine
dev + test + val
en→
84.9
±1.0
75.1
±1.6
39.3
±2.8
38.6
±1.7
36.8
±1.1
33.6
±3.0
40.7
±2.5
39.3
±1.7
44.5
±1.3
43.8
±1.0
41.8
±1.9
38.4
±0.5
af→
85.7
±2.0
80.9
±1.7
47.1
±2.6
47.4
±2.2
43.5
±2.0
34.5
±1.9
47.7
±1.4
45.8
±1.7
49.2
±2.1
48.8
±1.7
50.1
±2.9
38.6
±4.4
zu→
83.3
±0.5
78.0
±1.9
53.2
±2.5
51.8
±3.5
45.9
±4.6
36.3
±1.7
49.4
±1.2
49.6
±1.9
49.8
±0.8
52.6
±0.8
49.3
±2.6
44.3
±1.4
xh→
82.3
±1.4
75.7
±2.7
49.6
±2.5
53.7
±0.8
43.7
±1.7
35.4
±1.0
50.7
±3.4
52.2
±1.6
51.6
±1.7
52.3
±1.2
50.7
±3.7
44.0
±1.6
am→
82.7
±0.2
75.8
±1.6
48.1
±2.5
47.2
±3.1
59.2
±2.3
40.1
±0.8
47.3
±0.4
52.5
±2.1
49.6
±1.2
51.6
±2.3
48.2
±1.2
41.5
±0.6
bm→
81.7
±1.1
72.3
±1.0
42.1
±1.9
42.0
±2.6
39.9
±2.0
41.6
±3.2
44.8
±1.0
43.7
±2.1
47.5
±0.6
45.8
±2.1
43.8
±4.0
41.9
±4.0
ig→
84.5
±1.3
75.8
±1.2
44.5
±0.4
45.9
±0.8
42.1
±2.1
35.7
±2.4
56.0
±4.2
49.2
±2.5
49.3
±0.9
50.9
±1.4
50.6
±1.4
40.8
±1.2
nso→
83.1
±2.1
76.1
±0.9
48.5
±1.1
51.7
±2.3
46.9
±2.0
37.4
±3.1
49.4
±3.0
58.6
±1.1
52.2
±1.0
54.7
±1.1
53.2
±1.0
46.2
±2.7
sn→
83.5
±1.0
76.7
±0.8
49.8
±3.3
47.8
±1.2
47.3
±0.9
38.8
±3.5
50.3
±2.3
54.5
±1.0
62.3
±0.4
54.7
±3.9
53.6
±2.3
47.4
±1.6
st→
83.7
±0.6
77.0
±1.0
50.3
±3.1
51.7
±0.4
47.3
±1.9
38.9
±1.7
48.8
±2.1
54.3
±3.1
53.7
±1.8
59.2
±1.0
56.2
±0.7
45.5
±1.5
tn→
84.0
±1.4
76.7
±0.2
49.8
±2.5
50.1
±2.3
47.1
±0.2
39.0
±1.7
50.6
±0.8
58.1
±0.6
52.3
±2.5
55.9
±1.6
59.6
±0.6
46.5
±1.6
ts→
82.5
±0.2
77.8
±1.0
50.3
±2.0
49.2
±0.6
47.8
±3.4
36.2
±1.7
51.3
±1.2
52.2
±2.5
50.9
±0.8
54.6
±1.3
49.0
±2.0
53.5
±1.7
Table A.23: Results of Cross-lingual Transfer using Llama 3 70B Instruct when Tuning on MMLU College Medicine and
Testing on MMLU Clinical Knowledge. Llama 3 70B Instruct was independently fine-tuned on the 11 African languages of
focus: Afrikaans (af), Zulu (zu), Xhosa (xh) (datasets for these three languages were sourced from (BMGF 2024)), Amharic
(am), Bambara (bm), Igbo (ig), Sepedi (nso), Shona (sn), Sesotho (st), Setswana (tn), and Tsonga (ts). Llama 3 70B Instruct was
also fine-tuned on English (en) for reference. The translated MMLU College Medicine section (dev + test + val sets) was
used for fine-tuning. The fine-tuned models were evaluated for their cross-lingual transfer performance on the translated MMLU
Clinical Knowledge (clinical domain knowledge task) test set. Columns indicate the target language of the evaluation,
while the rows indicate the source language the models were fine-tuned with (e.g. “zu→” indicates models fine-tuned with data
in Zulu). All numbers are the mean 5-shot performance accuracy of three evaluations followed by the standard deviation (±).
Model fine-tuning that yielded mono-lingual improvements (relative to the baseline) more than two standard deviations are in
blue, while cross-lingual improvements (relative to the baseline) more than two standard deviations are in green.

--- Page 39 ---

MMLU Virology
en
af
zu
xh
am
bm
ig
nso
sn
st
tn
ts
Base
Llama 3
70B IT
53.6
46.4
28.9
27.1
36.1
35.5
34.9
26.5
31.3
29.5
28.3
31.3
Winogrande
train (small)
en→
56.6
±2.1
46.6
±2.4
34.5
±3.4
31.1
±3.3
30.9
±3.1
32.7
±5.2
31.3
±1.0
30.1
±2.1
31.7
±1.9
31.9
±3.3
30.7
±2.1
32.7
±7.0
af→
55.4
±0.6
49.8
±1.9
32.9
±1.2
32.9
±3.9
37.7
±2.3
35.3
±0.9
36.5
±3.1
30.3
±1.5
37.1
±1.9
34.7
±1.8
33.9
±3.0
30.9
±1.2
zu→
52.8
±3.0
48.0
±1.5
39.0
±3.1
33.3
±1.9
34.7
±5.1
33.5
±3.3
35.1
±0.9
30.7
±6.4
35.3
±5.3
33.7
±2.7
31.7
±2.7
31.1
±2.3
xh→
55.4
±1.6
49.6
±2.7
38.5
±3.2
35.3
±2.3
35.3
±4.3
27.9
±1.2
35.9
±2.8
32.7
±1.5
32.3
±3.0
32.7
±1.9
32.1
±2.5
31.3
±1.6
am→
52.8
±0.7
51.4
±0.9
37.5
±4.1
34.7
±3.1
38.4
±2.6
34.1
±1.5
36.9
±2.2
32.7
±3.3
34.3
±2.2
30.7
±2.2
32.1
±0.9
28.3
±3.7
bm→
52.0
±2.7
49.0
±0.3
30.1
±4.9
29.1
±1.2
30.9
±3.6
27.7
±5.7
29.7
±3.5
29.3
±0.9
31.5
±0.9
29.7
±6.1
29.3
±3.3
30.3
±3.3
ig→
55.2
±1.5
50.6
±2.6
38.0
±1.6
29.5
±2.4
32.7
±2.4
33.9
±5.5
32.3
±1.5
33.1
±3.2
33.3
±3.0
31.9
±4.7
31.3
±1.0
32.1
±1.2
nso→
55.4
±1.6
50.2
±2.3
38.3
±2.9
31.7
±6.4
29.7
±2.1
32.1
±2.7
34.9
±0.6
33.1
±1.8
38.4
±3.1
34.3
±2.4
35.7
±1.2
32.1
±1.8
sn→
53.0
±1.6
48.2
±0.6
36.9
±2.5
33.7
±3.3
32.1
±0.9
31.5
±3.3
32.5
±3.2
32.7
±3.6
32.7
±1.5
31.9
±0.6
31.9
±0.6
30.5
±3.0
st→
55.0
±1.5
48.4
±1.2
34.7
±3.7
35.5
±3.4
33.3
±2.1
30.9
±4.7
35.5
±2.2
31.7
±1.5
37.3
±1.3
34.5
±3.4
31.1
±1.5
32.7
±1.2
tn→
55.6
±0.7
51.2
±1.6
38.6
±0.6
38.2
±1.6
31.3
±7.3
32.5
±2.2
35.9
±0.7
34.3
±1.0
37.3
±1.6
32.1
±0.3
32.3
±1.4
33.1
±3.3
ts→
52.4
±2.2
47.4
±2.4
34.1
±2.3
34.5
±4.0
31.7
±1.8
34.5
±2.8
34.1
±4.0
30.5
±2.4
32.7
±0.9
32.5
±3.9
30.3
±1.2
29.9
±2.8
Table A.24: Results of Cross-lingual Transfer using Llama 3 70B Instruct when Tuning on Winogrande and Testing on
MMLU Virology. Llama 3 70B Instruct was independently fine-tuned on the 11 African languages of focus: Afrikaans (af),
Zulu (zu), Xhosa (xh) (datasets for these three languages were sourced from (BMGF 2024)), Amharic (am), Bambara (bm),
Igbo (ig), Sepedi (nso), Shona (sn), Sesotho (st), Setswana (tn), and Tsonga (ts). Llama 3 70B Instruct was also fine-tuned on
English (en) for reference. The translated Winogrande training set (small) was used for fine-tuning. The fine-tuned models
were evaluated for their cross-lingual transfer performance on the translated MMLU Virology (virology domain knowledge
task) test set. Columns indicate the target language of the evaluation, while the rows indicate the source language the models
were fine-tuned with (e.g. “zu→” indicates models fine-tuned with data in Zulu). All numbers are the mean 5-shot performance
accuracy of three evaluations followed by the standard deviation (±). Model fine-tuning that yielded mono-lingual improvements
(relative to the baseline) more than two standard deviations are in blue, while cross-lingual improvements (relative to the
baseline) more than two standard deviations are in green.

--- Page 40 ---

MMLU Virology
en
af
zu
xh
am
bm
ig
nso
sn
st
tn
ts
Base
Llama 3
70B IT
53.6
46.4
28.9
27.1
36.1
35.5
34.9
26.5
31.3
29.5
28.3
31.3
MMLU College Medicine
dev + test + val
en→
53.8
±1.8
46.2
±0.7
31.1
±0.9
31.9
±3.1
30.5
±3.0
30.1
±2.2
29.9
±3.1
30.5
±2.4
27.5
±1.2
28.1
±0.9
25.7
±0.9
28.9
±0.6
af→
53.8
±1.8
48.4
±0.9
31.1
±3.0
28.9
±4.8
29.7
±1.2
28.3
±2.6
31.1
±0.3
28.9
±1.2
30.3
±2.8
31.9
±5.1
24.3
±0.9
28.1
±1.9
zu→
55.6
±0.9
50.8
±0.7
35.3
±1.4
32.5
±1.6
34.1
±1.2
26.9
±1.5
36.5
±0.3
30.3
±0.7
34.3
±1.8
33.9
±4.1
31.7
±0.3
31.9
±3.3
xh→
55.0
±0.9
50.6
±0.0
34.5
±0.7
32.7
±2.1
32.5
±3.9
28.5
±3.3
35.1
±0.9
28.3
±1.2
34.1
±1.4
31.7
±2.4
28.7
±1.9
33.7
±1.6
am→
55.8
±0.7
52.0
±0.3
38.6
±2.2
33.3
±1.2
37.6
±2.5
28.1
±4.1
33.9
±2.8
30.7
±1.2
34.7
±3.1
33.5
±3.7
30.7
±0.6
32.1
±1.5
bm→
55.2
±0.7
48.8
±0.6
30.9
±2.4
30.9
±2.4
31.7
±2.7
26.1
±2.4
28.7
±3.0
29.9
±0.7
28.9
±2.7
28.9
±1.0
28.5
±2.7
26.5
±4.3
ig→
54.6
±1.8
51.0
±0.9
35.9
±1.8
31.9
±3.2
30.9
±2.5
24.5
±2.8
35.9
±3.0
31.7
±2.1
37.8
±1.4
31.7
±2.1
30.9
±3.0
33.3
±0.3
nso→
54.6
±1.2
50.4
±1.4
35.7
±0.9
33.7
±1.6
38.5
±3.7
26.3
±1.5
34.9
±2.1
33.7
±2.4
32.1
±2.4
33.1
±1.2
30.5
±2.5
32.9
±2.3
sn→
56.4
±0.3
50.6
±0.6
40.0
±1.7
35.1
±3.3
34.5
±1.2
26.5
±2.7
38.6
±3.7
32.9
±1.8
37.5
±0.4
33.7
±2.1
32.3
±0.3
32.5
±3.3
st→
55.2
±0.9
50.0
±1.0
33.5
±2.4
31.7
±4.8
35.3
±1.2
30.7
±3.3
34.7
±2.3
34.3
±2.2
33.1
±3.1
33.7
±3.2
32.7
±1.7
35.7
±2.6
tn→
55.2
±0.3
51.0
±1.8
36.3
±1.9
32.5
±1.6
33.1
±2.4
27.9
±1.5
37.2
±3.6
35.5
±1.2
33.1
±1.2
32.5
±3.3
34.5
±1.8
32.9
±2.5
ts→
56.2
±0.3
49.8
±1.2
37.3
±2.5
33.1
±0.6
38.4
±0.3
24.7
±2.6
38.0
±1.3
34.3
±1.6
35.3
±1.2
33.9
±1.9
32.9
±1.2
38.6
±0.6
Table A.25: Results of Cross-lingual Transfer using Llama 3 70B Instruct when Tuning on MMLU College Medicine
and Testing on MMLU Virology. Llama 3 70B Instruct was independently fine-tuned on the 11 African languages of focus:
Afrikaans (af), Zulu (zu), Xhosa (xh) (datasets for these three languages were sourced from (BMGF 2024)), Amharic (am),
Bambara (bm), Igbo (ig), Sepedi (nso), Shona (sn), Sesotho (st), Setswana (tn), and Tsonga (ts). Llama 3 70B Instruct was
also fine-tuned on English (en) for reference. The translated MMLU College Medicine section (dev + test + val sets) was
used for fine-tuning. The fine-tuned models were evaluated for their cross-lingual transfer performance on the translated MMLU
Virology (virology domain knowledge task) test set. Columns indicate the target language of the evaluation, while the rows
indicate the source language the models were fine-tuned with (e.g. “zu→” indicates models fine-tuned with data in Zulu). All
numbers are the mean 5-shot performance accuracy of three evaluations followed by the standard deviation (±). Model fine-
tuning that yielded mono-lingual improvements (relative to the baseline) more than two standard deviations are in blue, while
cross-lingual improvements (relative to the baseline) more than two standard deviations are in green.

--- Page 41 ---

Belebele
en
af
zu
xh
am
bm
ig
nso
sn
st
tn
ts
Base
Llama 3
70B IT
94.6
84.8
36.7
36.8
35.1
35.6
35.9
37.1
38.1
35.9
36.4
40.7
Winogrande
train (small)
en→
95.4
±0.3
90.1
±0.4
37.2
±1.5
37.4
±0.4
32.4
±1.2
33.4
±1.3
39.2
±1.3
35.4
±0.5
38.8
±2.0
36.2
±0.2
35.3
±1.4
37.7
±1.2
af→
95.2
±0.1
91.0
±0.3
44.7
±2.2
42.4
±0.4
36.4
±1.1
33.6
±0.8
46.7
±0.3
40.1
±1.4
42.2
±1.0
42.6
±0.8
43.3
±0.2
42.3
±1.0
zu→
95.1
±0.3
89.2
±0.7
43.3
±0.9
41.6
±0.3
33.8
±1.5
30.9
±1.2
44.3
±1.5
38.9
±1.2
41.1
±1.3
39.5
±0.3
40.9
±1.2
40.4
±1.1
xh→
94.3
±0.4
89.0
±0.1
43.0
±0.7
42.0
±1.6
31.7
±1.1
29.7
±2.5
41.1
±0.6
37.5
±1.5
39.7
±2.0
38.0
±0.6
39.4
±0.8
39.6
±1.3
am→
95.5
±0.5
91.2
±0.4
45.9
±1.9
43.2
±0.9
53.9
±2.0
34.9
±0.9
47.2
±0.8
42.5
±0.7
42.5
±1.1
44.3
±1.3
44.7
±1.0
44.9
±1.1
bm→
94.4
±0.5
84.9
±0.3
32.7
±0.8
30.3
±1.1
26.8
±1.8
29.0
±0.3
33.0
±2.7
31.3
±1.2
32.1
±0.5
30.1
±1.2
32.2
±0.6
29.7
±1.8
ig→
94.5
±0.2
90.4
±0.1
40.6
±1.4
41.1
±0.3
37.8
±0.3
29.8
±0.8
48.4
±1.8
37.7
±0.4
40.2
±2.8
39.3
±1.3
37.7
±0.4
38.8
±1.7
nso→
94.6
±0.2
89.1
±1.0
44.5
±1.0
44.2
±0.6
33.8
±0.1
30.2
±0.5
44.5
±1.0
44.9
±0.7
42.6
±1.0
45.1
±1.2
45.8
±1.4
43.6
±1.5
sn→
95.2
±0.3
90.5
±0.5
44.2
±1.6
43.3
±1.1
34.7
±1.1
33.3
±1.6
43.0
±0.8
42.6
±1.5
46.3
±0.8
43.1
±0.4
45.7
±1.0
45.3
±1.2
st→
94.6
±0.2
89.7
±0.4
41.7
±2.3
42.4
±1.1
36.1
±0.4
32.2
±1.2
43.7
±0.3
42.3
±0.7
43.0
±3.0
42.3
±0.6
44.4
±0.7
42.0
±2.4
tn→
95.1
±0.2
89.3
±0.2
44.3
±1.6
44.4
±1.5
39.7
±1.0
31.6
±0.9
46.2
±1.1
44.8
±1.2
43.6
±0.5
47.8
±0.9
44.5
±0.4
44.0
±0.2
ts→
93.9
±0.8
85.1
±0.3
38.2
±0.8
37.2
±0.6
29.4
±1.0
29.3
±0.9
37.3
±0.7
34.0
±1.7
37.5
±0.7
36.6
±0.7
36.8
±1.8
37.9
±0.9
Table A.26: Results of Cross-lingual Transfer using Llama 3 70B Instruct when Tuning on Winogrande and Testing on
Belebele. Llama 3 70B Instruct was independently fine-tuned on the 11 African languages of focus: Afrikaans (af), Zulu (zu),
Xhosa (xh) (datasets for these three languages were sourced from (BMGF 2024)), Amharic (am), Bambara (bm), Igbo (ig),
Sepedi (nso), Shona (sn), Sesotho (st), Setswana (tn), and Tsonga (ts). Llama 3 70B Instruct was also fine-tuned on English (en)
for reference. The translated Winogrande training set (small) was used for fine-tuning. The fine-tuned models were evaluated
for their cross-lingual transfer performance on Belebele (reading comprehension task). Columns indicate the target language
of the evaluation, while the rows indicate the source language the models were fine-tuned with (e.g. “zu→” indicates models
fine-tuned with data in Zulu). All numbers are the mean 0-shot performance accuracy of three evaluations followed by the
standard deviation (±). Model fine-tuning that yielded mono-lingual improvements (relative to the baseline) more than two
standard deviations are in blue, while cross-lingual improvements (relative to the baseline) more than two standard deviations
are in green.

--- Page 42 ---

Belebele
en
af
zu
xh
am
bm
ig
nso
sn
st
tn
ts
Base
Llama 3
70B IT
94.6
84.8
36.7
36.8
35.1
35.6
35.9
37.1
38.1
35.9
36.4
40.7
MMLU College Medicine
dev + test + val
en→
94.6
±0.2
90.1
±0.5
36.1
±1.3
36.5
±0.7
31.3
±1.2
33.6
±0.5
38.6
±0.8
36.0
±0.6
38.5
±2.7
34.9
±1.7
37.6
±1.1
38.2
±0.5
af→
94.8
±0.1
90.9
±0.5
42.6
±0.1
38.8
±1.5
35.3
±1.1
30.8
±1.2
44.1
±1.4
40.2
±1.2
40.5
±2.2
40.2
±0.5
42.3
±1.4
41.2
±0.5
zu→
94.7
±0.1
90.3
±0.1
45.1
±0.5
43.9
±1.1
40.6
±0.7
31.5
±1.5
45.0
±0.9
41.9
±0.9
44.3
±0.9
41.2
±0.9
42.5
±0.7
41.3
±1.1
xh→
94.7
±0.4
91.0
±0.3
46.4
±1.1
45.7
±1.4
39.2
±0.5
31.3
±1.6
46.3
±1.1
42.6
±1.6
44.0
±0.2
42.6
±2.4
45.8
±1.4
42.7
±0.5
am→
94.5
±0.3
90.1
±0.5
42.9
±0.6
42.5
±1.0
50.4
±0.3
33.1
±0.8
44.1
±0.9
39.0
±0.2
42.2
±1.2
40.5
±1.0
41.3
±0.4
41.9
±0.7
bm→
94.3
±0.4
89.2
±0.2
37.4
±0.7
37.7
±1.0
35.3
±0.8
32.8
±0.6
40.9
±1.0
33.4
±2.2
37.2
±2.0
35.0
±0.8
37.8
±3.0
38.1
±0.5
ig→
94.6
±0.4
91.5
±0.5
44.3
±0.6
44.0
±0.9
42.7
±0.4
32.5
±1.0
48.3
±1.0
43.0
±1.1
45.5
±1.5
44.1
±0.5
45.9
±1.0
43.1
±0.3
nso→
94.4
±0.6
89.9
±0.7
43.3
±1.5
41.6
±1.2
41.2
±0.9
31.4
±1.5
43.2
±0.6
47.2
±1.4
43.1
±1.4
45.5
±0.4
47.6
±1.8
43.7
±0.8
sn→
94.8
±0.4
90.2
±0.5
45.9
±1.1
43.8
±0.5
41.1
±0.3
34.5
±2.4
46.6
±0.4
45.0
±1.4
50.9
±0.7
44.4
±0.9
46.4
±1.0
45.3
±1.0
st→
94.5
±0.3
91.0
±0.3
45.3
±0.1
44.4
±2.3
42.2
±1.1
32.9
±0.4
45.4
±1.2
46.9
±1.1
45.3
±1.4
49.6
±1.2
49.4
±1.5
44.4
±0.6
tn→
94.3
±0.4
90.5
±0.5
42.3
±0.8
41.4
±1.5
39.4
±2.1
31.0
±1.3
45.6
±1.0
44.1
±0.8
43.0
±0.8
44.4
±1.1
47.3
±0.4
41.7
±0.4
ts→
94.5
±0.3
91.1
±0.3
44.6
±0.8
43.3
±1.0
40.6
±1.0
31.1
±1.1
46.2
±0.9
45.0
±1.2
45.5
±0.3
45.5
±1.3
46.2
±0.6
48.2
±1.3
Table A.27: Results of Cross-lingual Transfer using Llama 3 70B Instruct when Tuning on MMLU College Medicine and
Testing on Belebele. Llama 3 70B Instruct was independently fine-tuned on the 11 African languages of focus: Afrikaans (af),
Zulu (zu), Xhosa (xh) (datasets for these three languages were sourced from (BMGF 2024)), Amharic (am), Bambara (bm), Igbo
(ig), Sepedi (nso), Shona (sn), Sesotho (st), Setswana (tn), and Tsonga (ts). Llama 3 70B Instruct was also fine-tuned on English
(en) for reference. The translated MMLU College Medicine section (dev + test + val sets) was used for fine-tuning. The
fine-tuned models were evaluated for their cross-lingual transfer performance on Belebele (reading comprehension task).
Columns indicate the target language of the evaluation, while the rows indicate the source language the models were fine-tuned
with (e.g. “zu→” indicates models fine-tuned with data in Zulu). All numbers are the mean 0-shot performance accuracy of
three evaluations followed by the standard deviation (±). Model fine-tuning that yielded mono-lingual improvements (relative
to the baseline) more than two standard deviations are in blue, while cross-lingual improvements (relative to the baseline) more
than two standard deviations are in green.

--- Page 43 ---

Fine-Tuning Dataset (language)
Data Quality
Data Quantity
0%
25%
50%
75%
100%
Evaluation set: Winogrande
Samples
N/A
53
107
160
213
Winogrande (en)
Low
61.2 ±0.0
60.3 ±0.9
82.4 ±0.3
83.4 ±0.5
84.9 ±0.8
High
61.2 ±0.0
79.7 ±0.1
82.6 ±0.3
84.2 ±0.4
84.8 ±0.1
Winogrande (af)
Low
51.0 ±0.0
53.7 ±1.1
64.3 ±0.6
66.5 ±0.7
67.5 ±0.4
High
51.0 ±0.0
68.3 ±0.5
72.0 ±0.7
71.8 ±0.4
74.9 ±0.3
Samples
N/A
17
33
50
66
MMLU College Medicine (en)
Low
61.2 ±0.0
62.3 ±0.4
66.9 ±0.5
62.2 ±0.1
67.6 ±0.4
High
61.2 ±0.0
64.8 ±0.2
65.0 ±0.5
66.6 ±1.1
69.4 ±0.4
MMLU College Medicine (af)
Low
51.0 ±0.0
52.9 ±0.2
57.4 ±0.3
56.5 ±0.5
58.0 ±0.5
High
51.0 ±0.0
50.6 ±0.0
54.0 ±0.3
56.4 ±0.1
59.5 ±0.6
Table A.28: Results of Data Quality vs. Quantity using Llama 3 70B Instruct and Evaluating on Winogrande. Llama 3 70B
Instruct was fine-tuned on various GPT-4o LLM-as-an-Annotator quality and random-sampling quantity combination subsets
of Winogrande train (small) and MMLU College Medicine where there was a mono-lingual lift of at least 5% observed when
using the full fine-tuning dataset (see Tables A.20 and A.21). The fine-tuned models were then evaluated on the Winogrande
test split in the same language as the fine-tuning dataset. Note that the exact fine-tuning dataset sample sizes when using
Winogrande as the fine-tuning dataset (Wino) and MMLU College Medicine as the fine-tuning dataset (MMLU) are given
above the performance results. Language codes are as follows: English (en), Afrikaans (af).

--- Page 44 ---

Fine-Tuning Dataset (language)
Data Quality
Data Quantity
0%
25%
50%
75%
100%
Evaluation set: MMLU Clinical Knowledge
Samples
N/A
53
107
160
213
Winogrande (am)
Low
33.6 ±0.0
44.3 ±1.0
45.7 ±2.0
44.8 ±0.5
47.2 ±1.6
High
33.6 ±0.0
44.4 ±0.2
44.9 ±0.4
48.4 ±0.8
47.3 ±0.2
Winogrande (ig)
Low
33.6 ±0.0
36.5 ±4.5
44.8 ±0.9
41.9 ±3.5
40.6 ±3.7
High
33.6 ±0.0
41.3 ±2.4
42.9 ±0.8
44.3 ±1.8
42.8 ±2.2
Winogrande (nso)
Low
37.0 ±0.0
38.9 ±2.7
40.2 ±2.2
42.2 ±0.2
43.0 ±1.7
High
37.0 ±0.0
43.5 ±2.8
44.3 ±1.2
42.0 ±3.5
45.0 ±0.9
Samples
N/A
17
33
50
66
MMLU College Medicine (af)
Low
71.3 ±0.0
64.4 ±3.1
63.8 ±0.4
67.3 ±2.7
71.1 ±1.2
High
71.3 ±0.0
72.5 ±2.5
75.4 ±1.3
76.3 ±1.7
75.6 ±0.4
MMLU College Medicine (zu)
Low
39.2 ±0.0
44.6 ±1.7
39.5 ±1.7
42.5 ±1.5
41.5 ±1.6
High
39.2 ±0.0
40.5 ±0.9
44.0 ±2.4
49.8 ±2.6
50.2 ±2.0
MMLU College Medicine (xh)
Low
38.5 ±0.0
42.2 ±3.1
34.3 ±1.3
40.7 ±2.3
42.3 ±1.7
High
38.5 ±0.0
39.9 ±0.2
48.8 ±1.9
47.6 ±1.4
48.9 ±2.1
MMLU College Medicine (am)
Low
33.6 ±0.0
44.8 ±1.6
42.9 ±2.1
45.9 ±2.9
48.4 ±1.3
High
33.6 ±0.0
48.2 ±0.8
48.2 ±1.7
51.3 ±1.9
51.7 ±2.7
MMLU College Medicine (bm)
Low
32.5 ±0.0
32.8 ±0.8
34.9 ±2.5
32.7 ±0.8
33.9 ±2.1
High
32.5 ±0.0
32.1 ±3.3
33.6 ±3.1
38.7 ±1.2
36.1 ±2.3
MMLU College Medicine (ig)
Low
33.6 ±0.0
41.9 ±3.7
43.4 ±2.1
40.9 ±2.4
47.5 ±2.3
High
33.6 ±0.0
48.7 ±2.1
47.9 ±3.0
50.8 ±2.9
50.3 ±2.8
MMLU College Medicine (nso)
Low
37.0 ±0.0
39.5 ±0.8
46.3 ±1.5
41.9 ±1.3
46.4 ±2.0
High
37.0 ±0.0
46.9 ±2.5
47.4 ±1.7
54.0 ±1.3
53.6 ±0.6
MMLU College Medicine (sn)
Low
43.4 ±0.0
43.7 ±1.3
46.7 ±1.2
43.8 ±1.4
44.5 ±2.0
High
43.4 ±0.0
46.8 ±3.6
48.9 ±1.4
50.1 ±3.0
52.4 ±2.1
MMLU College Medicine (st)
Low
43.8 ±0.0
48.8 ±2.8
44.4 ±2.5
39.5 ±2.3
44.0 ±3.1
High
43.8 ±0.0
47.9 ±0.4
50.7 ±1.0
53.3 ±2.7
54.7 ±1.0
MMLU College Medicine (tn)
Low
39.2 ±0.0
44.0 ±2.4
44.3 ±1.4
46.7 ±1.1
35.9 ±4.1
High
39.2 ±0.0
46.9 ±2.0
46.9 ±4.2
45.7 ±2.3
45.3 ±1.6
MMLU College Medicine (ts)
Low
34.0 ±0.0
36.4 ±1.0
36.8 ±1.0
34.3 ±1.3
40.5 ±2.1
High
34.0 ±0.0
37.9 ±1.0
43.6 ±0.8
43.3 ±3.6
47.4 ±3.4
Table A.29: Results of Data Quality vs. Quantity using Llama 3 70B Instruct and Evaluating on MMLU Clinical Knowl-
edge. Llama 3 70B Instruct was fine-tuned on various GPT-4o LLM-as-an-Annotator quality and random-sampling quantity
combination subsets of Winogrande train (small) and MMLU College Medicine where there was a mono-lingual lift of at least
5% observed when using the full fine-tuning dataset (see Tables A.22 and A.23). The fine-tuned models were then evaluated
on the MMLU Clinical Knowledge test split in the same language as the fine-tuning dataset. Note that the exact fine-tuning
dataset sample sizes when using Winogrande as the fine-tuning dataset (Wino) and MMLU College Medicine as the fine-tuning
dataset (MMLU) are given above the performance results. Language codes are as follows: Amharic (am), Igbo (ig), Sepedi
(nso), Afrikaans (af), Zulu (zu), Xhosa (xh), Bambara (bm), Shona (sn), Sesotho (st), Setswana (tn), Tsonga (ts).

--- Page 45 ---

Fine-Tuning Dataset (language)
Data Quality
Data Quantity
0%
25%
50%
75%
100%
Evaluation set: MMLU Virology
Samples
N/A
53
107
160
213
Winogrande (zu)
Low
28.9 ±0.0
32.1 ±3.5
33.3 ±4.3
36.3 ±2.5
34.1 ±1.2
High
28.9 ±0.0
34.3 ±1.0
36.9 ±0.7
33.7 ±4.4
37.3 ±2.2
Winogrande (xh)
Low
27.1 ±0.0
29.7 ±2.4
36.1 ±1.0
31.3 ±2.2
33.9 ±1.2
High
27.1 ±0.0
32.7 ±2.3
31.3 ±2.6
33.3 ±1.7
33.5 ±3.0
Winogrande (nso)
Low
26.5 ±0.0
33.3 ±2.8
31.5 ±1.2
35.1 ±2.6
38.2 ±1.3
High
26.5 ±0.0
30.3 ±0.3
31.9 ±3.1
34.7 ±1.2
37.5 ±2.6
Winogrande (st)
Low
29.5 ±0.0
28.3 ±1.8
33.7 ±1.0
33.3 ±0.7
32.7 ±2.4
High
29.5 ±0.0
33.1 ±3.2
30.5 ±2.1
32.7 ±1.2
32.9 ±0.9
Samples
N/A
17
33
50
66
MMLU College Medicine (zu)
Low
28.9 ±0.0
35.3 ±2.5
33.7 ±3.1
29.1 ±3.0
32.3 ±2.8
High
28.9 ±0.0
34.3 ±3.8
38.3 ±4.1
36.1 ±1.6
35.9 ±0.7
MMLU College Medicine (xh)
Low
27.1 ±0.0
33.5 ±3.9
32.9 ±2.7
33.7 ±2.2
28.3 ±3.0
High
27.1 ±0.0
34.3 ±2.6
33.5 ±0.9
32.9 ±2.8
34.5 ±1.5
MMLU College Medicine (nso)
Low
26.5 ±0.0
29.3 ±2.4
30.3 ±1.4
27.7 ±1.2
32.3 ±0.3
High
26.5 ±0.0
32.7 ±0.9
34.1 ±1.2
32.3 ±0.3
33.7 ±0.0
MMLU College Medicine (sn)
Low
31.3 ±0.0
28.5 ±1.8
31.7 ±3.4
33.7 ±2.2
35.9 ±2.5
High
31.3 ±0.0
33.1 ±1.2
34.1 ±1.2
38.7 ±3.0
34.9 ±0.6
MMLU College Medicine (tn)
Low
28.3 ±0.0
29.5 ±3.6
32.7 ±4.4
30.9 ±3.5
33.3 ±3.5
High
28.3 ±0.0
34.7 ±1.9
32.1 ±2.5
31.3 ±2.6
34.3 ±2.2
MMLU College Medicine (ts)
Low
31.3 ±0.0
33.7 ±2.2
31.3 ±1.6
31.9 ±1.8
34.1 ±0.3
High
31.3 ±0.0
31.7 ±3.7
33.9 ±1.7
33.3 ±0.9
34.7 ±2.9
Table A.30: Results of Data Quality vs. Quantity using Llama 3 70B Instruct and Evaluating on MMLU Virology. Llama
3 70B Instruct was fine-tuned on various GPT-4o LLM-as-an-Annotator quality and random-sampling quantity combination
subsets of Winogrande train (small) and MMLU College Medicine where there was a mono-lingual lift of at least 5% observed
when using the full fine-tuning dataset (see Tables A.24 and A.25). The fine-tuned models were then evaluated on the MMLU
Virology test split in the same language as the fine-tuning dataset. Note that the exact fine-tuning dataset sample sizes when
using Winogrande as the fine-tuning dataset (Wino) and MMLU College Medicine as the fine-tuning dataset (MMLU) are given
above the performance results. Language codes are as follows: Zulu (zu), Xhosa (xh), Sepedi (nso), Sesotho (st), Shona (sn),
Setswana (tn), Tsonga (ts).

--- Page 46 ---

Fine-Tuning Dataset (language)
Data Quality
Data Quantity
0%
25%
50%
75%
100%
Evaluation set: Belebele
Samples
N/A
53
107
160
213
Winogrande (af)
Low
84.8 ±0.0
90.1 ±0.2
91.3 ±0.4
91.5 ±0.8
90.5 ±0.5
High
84.8 ±0.0
91.4 ±0.2
91.1 ±0.1
91.9 ±0.2
91.6 ±0.2
Winogrande (zu)
Low
36.7 ±0.0
37.6 ±1.2
41.9 ±1.4
43.5 ±0.6
44.2 ±1.8
High
36.7 ±0.0
37.9 ±1.1
43.3 ±1.2
48.1 ±1.4
38.8 ±0.5
Winogrande (xh)
Low
36.8 ±0.0
40.5 ±1.6
44.5 ±1.0
37.1 ±1.2
41.0 ±1.5
High
36.8 ±0.0
43.0 ±0.8
46.5 ±0.5
43.5 ±0.6
45.6 ±0.9
Winogrande (am)
Low
35.1 ±0.0
48.6 ±1.0
48.3 ±0.6
50.7 ±1.0
49.3 ±0.9
High
35.1 ±0.0
50.6 ±1.0
55.9 ±1.1
54.0 ±1.2
53.7 ±0.4
Winogrande (ig)
Low
35.9 ±0.0
44.9 ±1.1
44.0 ±1.5
50.3 ±1.6
51.0 ±0.9
High
35.9 ±0.0
46.5 ±0.4
48.8 ±1.5
47.1 ±0.8
49.7 ±0.8
Winogrande (nso)
Low
37.1 ±0.0
41.5 ±1.0
39.3 ±0.4
42.5 ±1.4
39.5 ±1.0
High
37.1 ±0.0
41.9 ±2.2
48.7 ±1.2
45.1 ±1.7
46.3 ±1.7
Winogrande (sn)
Low
38.1 ±0.0
35.3 ±1.4
42.7 ±0.9
40.1 ±1.0
42.0 ±1.4
High
38.1 ±0.0
41.5 ±1.2
45.4 ±1.1
47.1 ±0.2
45.2 ±0.8
Winogrande (st)
Low
35.9 ±0.0
42.7 ±2.2
44.2 ±1.1
42.1 ±1.9
48.3 ±0.6
High
35.9 ±0.0
40.7 ±0.8
43.5 ±0.7
43.9 ±1.1
45.5 ±2.5
Winogrande (tn)
Low
36.4 ±0.0
43.3 ±0.5
44.4 ±0.5
47.2 ±0.9
48.3 ±0.3
High
36.4 ±0.0
41.8 ±0.6
44.4 ±0.3
45.7 ±0.9
50.4 ±0.6
Samples
N/A
17
33
50
66
MMLU College Medicine (af)
Low
84.8 ±0.0
88.5 ±0.7
87.7 ±0.8
86.1 ±0.6
85.7 ±1.1
High
84.8 ±0.0
88.0 ±0.5
88.8 ±0.4
88.9 ±0.2
90.0 ±0.5
MMLU College Medicine (zu)
Low
36.7 ±0.0
35.5 ±1.1
42.5 ±0.6
38.3 ±2.7
41.1 ±1.3
High
36.7 ±0.0
39.1 ±1.1
43.0 ±0.4
44.4 ±1.1
44.2 ±0.8
MMLU College Medicine (xh)
Low
36.8 ±0.0
40.5 ±1.7
39.3 ±0.9
42.3 ±1.7
46.1 ±0.9
High
36.8 ±0.0
41.1 ±1.0
44.2 ±1.4
45.6 ±0.9
47.3 ±1.7
MMLU College Medicine (am)
Low
35.1 ±0.0
48.3 ±1.3
49.4 ±1.5
48.9 ±1.0
47.0 ±0.3
High
35.1 ±0.0
47.1 ±1.6
45.8 ±0.6
46.2 ±0.1
47.1 ±0.6
MMLU College Medicine (ig)
Low
35.9 ±0.0
42.1 ±0.9
41.2 ±1.0
43.1 ±0.9
46.6 ±2.0
High
35.9 ±0.0
41.6 ±1.3
44.1 ±1.1
48.0 ±1.1
47.1 ±1.4
MMLU College Medicine (nso)
Low
37.1 ±0.0
40.7 ±0.8
38.6 ±0.4
44.5 ±0.5
43.0 ±1.9
High
37.1 ±0.0
34.9 ±0.4
40.0 ±0.4
44.8 ±1.9
46.4 ±1.3
MMLU College Medicine (sn)
Low
38.1 ±0.0
40.1 ±2.0
40.6 ±1.0
42.3 ±1.3
44.2 ±0.5
High
38.1 ±0.0
37.9 ±0.4
36.8 ±0.4
42.8 ±0.6
41.7 ±0.5
MMLU College Medicine (st)
Low
35.9 ±0.0
45.1 ±0.2
41.5 ±1.1
42.6 ±1.6
44.1 ±1.6
High
35.9 ±0.0
42.2 ±0.8
42.0 ±1.1
44.0 ±0.7
46.9 ±0.8
MMLU College Medicine (tn)
Low
36.4 ±0.0
44.3 ±1.0
46.0 ±0.7
45.4 ±0.8
44.0 ±0.8
High
36.4 ±0.0
39.8 ±0.3
41.8 ±1.3
43.7 ±0.6
45.9 ±1.0
MMLU College Medicine (ts)
Low
40.7 ±0.0
40.7 ±0.1
38.7 ±0.9
37.6 ±0.4
41.4 ±0.6
High
40.7 ±0.0
41.5 ±0.7
42.5 ±0.2
42.2 ±1.6
47.2 ±0.9
Table A.31: Results of Data Quality vs. Quantity using Llama 3 70B Instruct and Evaluating on Belebele. Llama 3 70B
Instruct was fine-tuned on various GPT-4o LLM-as-an-Annotator quality and random-sampling quantity combination subsets
of Winogrande train (small) and MMLU College Medicine where there was a mono-lingual lift of at least 5% observed when
using the full fine-tuning dataset (see Tables A.26 and A.27). The fine-tuned models were then evaluated on Belebele in the
same language as the fine-tuning dataset. Note that the exact fine-tuning dataset sample sizes when using Winogrande as the
fine-tuning dataset (Wino) and MMLU College Medicine as the fine-tuning dataset (MMLU) are given above the performance
results. Language codes are as follows: Afrikaans (af), Zulu (zu), Xhosa (xh), Amharic (am), Igbo (ig), Sepedi (nso), Shona
(sn), Sesotho (st), Setswana (tn), Tsonga (ts).

--- Page 47 ---

ID
Badge Loc. Jobs Hours
Earned
JSS
Eng. Prof.
Assigned Tasks
Target Prof.
A.B.
Top
ZA
10
381
$2,000
100%
F
E (af)
af (N)
A.D.
-
ZA
65
1,265
$10,000
100%
N
E/V (af)
af (N)
A.H.
-
ZA
65
283
$10,000
100%
F
V (af)
af (N)
A.M.
-
ZA
4
0
$200
76%
N
E (xh)
xh (N)
A.S.1
-
ZA
16
136
$2,000
90%
N
T (nso); E (zu)
zu (N); nso (F)
A.S.2
-
ZW
6
10
$500
100%
N
V (sn)
sn (N)
A.V.
Top+
ZA
490
1,703
$90,000
99%
N
V/T (af)
af (N)
A.Z.1
-
ZA
6
2
$100
100%
N
E (zu,ts)
zu (N); ts(N)
A.Z.2
-
ZA
23
1,480
$10,000
94%
F
T (zu)
zu (N)
B.A.
Top
ET
259
93
$20,000
100%
N
E (am)
am (N)
B.M.
-
ZA
0
0
$0
-
N
T (zu)
zu (N)
C.B.
Top
NG
137
893
$30,000
97%
N
E (ig)
ig (N)
C.P.
-
ZA
4
21
$300
63%
N
E (xh)
xh (N)
D.C.
-
ML
26
11
$1,000
100%
N
E (bm)
bm (N)
D.D.
Top+
ZA
26
1,004
$20,000
100%
N
V (af)
af (N)
D.E.
Top
NG
15
749
$10,000
100%
N
E/V/T (ig)
ig (N)
D.H.
Top+
ET
255
626
-
100%
F
T (am)
am (N)
D.M.
Top+
ML
131
13,676 $100,000 100%
N
E/T (bm)
bm (N)
F.K.
-
ZW
5
6
$600
100%
N
E/V (sn)
sn (N)
H.B.
-
ZA
5
65
$1,000
100%
N
E (af)
af (N)
H.P.
-
ZA
0
0
$0
-
N
T (af)
af (N)
I.M.
Top
ZA
22
7
$9,000
96%
N
T (st, tn, af, zu)
af (F); zu (C); st (N); tn (N)
L.A.
-
ZA
24
822
$10,000
100%
N
E (af)
af (N)
L.M.
-
ZA
3
0
$0
100%
N
V (zu)
zu (N)
L.R.
-
ZA
2
0
$70
-
N
E (st)
st (F)
L.S.
-
ZA
15
0
$5,000
100%
N
E (af)
af (N)
M.B.
Top
ZA
70
1,258
$10,000
100%
F
E (af)
af (F)
M.H.
-
ZA
3
0
$200
100%
N
E/V/T (zu)
zu (N)
M.L.
Top
ET
67
250
$10,000
100%
F
V (am)
am (N)
M.M.1 -
ZA
76
386
$10,000
100%
N
V (zu)
zu (N)
M.M.2 Top
ZA
14
974
$6,000
100%
N
E/T/V (tn)
tn (N)
M.P.
-
ZA
2
0
$200
-
N
E (nso)
nso (N)
M.S.
-
SN
25
108
$3,000
100%
N
E/V (bm)
bm (F)
M.T.1
Top
ET
38
998
$10,000
100%
N
E (am)
am (N)
M.T.2
Top
ZA
90
3,354
$90,000
90%
F
E/V (xh); V (zu)
xh (N); zu (N)
M.W.
-
ZA
1
1
$15
-
N
E (af)
af (N)
N.B.
-
ZA
6
0
$200
100%
N
V (xh)
xh (N)
N.C.
-
ZA
71
231
$10,000
100%
N
E/V (af)
af (N)
N.H.
-
ZA
8
0
$200
100%
N
E/T/V (ts)
ts(F)
N.K.
-
ZW
4
2
$1,000
-
N
V (sn)
sn (N)
N.M.
-
ZA
13
1,367
$10,000
81%
N
E/T/V (ts)
ts(F)
N.N.
-
ZW
11
120
$10,000
100%
N
T (sn)
sn (N)
N.R.
-
ZA
18
35
$1,000
100%
N
E (st)
st (N)
P.H.
-
ZA
98
167
$5,000
95%
N
E/T/V (af)
af (N)
P.N.
Top+
NG
24
1,583
$20,000
96%
N
V/T (ig)
ig (N)
P.R.
-
ZA
9
42
$500
88%
N
E (zu, xh); E/V (nso)
xh (N); zu (N); nso (N)
P.T.
-
ZA
13
14
$400
100%
N
E (xh)
xh (N)
R.M.
Top
ZA
85
1,166
$40,000
100%
N
T (zu, nso); V (st, nso)
zu (N); nso (N); st (N)

--- Page 48 ---

ID
Badge Loc. Jobs Hours
Earned
JSS
Eng. Prof.
Assigned Tasks
Target Prof.
S.B.
-
ZA
5
7
$300
100%
N
E (af)
af (N)
S.D.
-
ZA
0
0
$50
-
N
E/T (xh)
xh (N)
S.M.1
-
ZA
0
0
$50
-
N
E/T (xh)
xh (N)
S.M.2
Top
ZA
15
257
$5,000
100%
N
E (zu)
zu (N)
S.N.1
-
ZA
0
0
$0
-
F
T (xh)
xh (N)
S.N.2
-
ZA
14
467
$6,000
100%
N
V (zu)
zu (N)
S.N.3
Top
ZA
13
29
$5,000
100%
N
E/V (zu)
zu (N)
S.S.
-
ZA
15
2
$1,000
100%
N
E/V (xh)
xh (N)
S.V.
-
ZA
1
0
$8
-
F
E (zu)
zu (N)
T.B.
-
ZA
7
152
$5,000
100%
N
T (af)
af (C)
T.M.1
-
BW
9
19
$600
100%
N
E/V (tn)
tn (N)
T.M.2
-
ZA
3
0
$50
100%
N
T (xh)
xh (N)
T.M.3
-
ZA
10
80
$2,000
100%
N
E (zu)
zu (N)
V.K.
Top
MW 44
139
$4,000
100%
N
E (zu)
zu (F)
X.P.
-
ZA
1
0
$50
-
N
T (xh)
xh (N)
Y.M.
-
ZW
7
1
$200
100%
N
E/V (sn)
sn (N)
Z.P.
Top
ZA
291
424
$60,000
100%
F
E (af)
af (N)
Table A.32: Profile of Translators / Annotators Sourced from Upwork.com. This table lists the profiles of individuals
recruited to perform the translation, review, and cultural appropriateness tasks. “Badge” is the profile badge present on Upwork
to indicate performance, if applicable (“Top” is for the “Top Rated” badge, and “Top+” is for the “Top Rated Plus” badge).
“Loc.” is the worker’s country of residence (given as an ISO 3166-1 alpha-2 country code). “Jobs” is the number of prior jobs
completed on Upwork. “Hrs.” is the number of prior working hours reported on Upwork (does not count fixed-price jobs).
“Earned” is the total prior earned amount reported on Upwork (in USD). “JSS” is a metric used by Upwork to represent “Job
Success Score”, expressed as a percentage (if not present, the worker likely did not have enough jobs at the time for it to be
calculated). “Eng. Prof.” is the self-reported English language proficiency. “Assigned Task” is a semicolon-separated list of
tasks assigned to the worker, with the task displayed as a single letter followed by the target language for that task. Tasks are
represented as follows: “E”: cultural appropriateness evaluator, “T”: translator, “V”: translation validator. “Target Prof.” is the
self-reported proficiency in the target languages for the assigned tasks. Language proficiency is represented as follows: “N”:
native or bilingual, “F”: fluent, “C”: conversational.

--- Page 49 ---

Figure A.1: Example Translation Task Form Given to Workers Hired on Upwork.com. Workers were tasked to translate
each Winogrande QA pair into eight African languages. The translator was able to see the percentage of the task completed to
aid in time management. The translator was also able to see any warnings regarding translation similarity to Google Translate
output (see Appendix Section A for more information). The figure above shows an example (in Shona) with four rows filled in
by a translator.

--- Page 50 ---

Figure A.2: Example Translation Review Task Form Given to Workers Hired on Upwork.com. Workers were tasked to
review the Winogrande translations provided by a previous worker. The reviewer was able to see the percentage of the task
completed to aid in time management. The reviewer was also able to see any warnings regarding translation similarity to
Google Translate output (see Appendix Section A for more information). The figure above shows an example (in Shona) with
four rows filled in by a reviewer.

--- Page 51 ---

Figure A.3: Example Translation Quality and Cultural Appropriateness Survey Form Given to Workers Hired on Up-
work.com. Workers were tasked to assess the quality and the appropriateness of previously obtained human translations of the
Winogrande dataset in 11 African languages. Each QA pair in Winogrande was provided (in the blue/leftmost column) with
the correct answer filled in, along with the corresponding human translation (in the purple/second-from-the-left column). The
evaluator was able to see the percentage of the task completed to aid in time management. The figure above shows an example
(in Afrikaans), depicting the dropdown options provided for the evaluator to select from.

--- Page 52 ---

Prompt:
The following are sentences that are missing a word or a few words (denoted
with an underscore), each followed by two options to fill in the missing word
or words. The correct option is given for each sentence:
Sentence 1: {Dev Set Sentence #1}
Option1: {Dev Set Option 1 #1}
Option2: {Dev Set Option 2 #1}
Correct Option: {Dev Set Correct Option #1}
...
Sentence 5: {Dev Set Sentence #5}
Option1: {Dev Set Option 1 #5}
Option2: {Dev Set Option 2 #5}
Correct Option: {Dev Set Correct Option #5}
Now, given the following sentence and options, output only the number
corresponding to the correct option. Do not add any explanation.
Sentence: {Test Set Sentence}
Option1: {Test Set Option 1}
Option2: {Test Set Option 2}
Correct Option:
Example Output:
1
Figure A.4: Winogrande Evaluation Prompt. The 5-shot, hard prompt template given to LLMs in order to evaluate them
on Winogrande. The 5-shot examples were all sourced randomly from the translated Winogrande dev set such that the same
examples were used for each language (i.e. the examples were versions of the same English examples but translated to different
African languages). Moreover, within each language, the same 5-shot examples were provided with each question in the trans-
lated Winogrande test set. LLMs were evaluated on all questions in the test set (1,767 questions per language). If the LLM gave
the same number (1 or 2) as the correct answer but not both, the LLM’s response was considered correct. Otherwise, the LLM’s
response was considered incorrect. This prompt was adapted from the one used for MMLU (see Figure A.5 below), since the
GitHub repository for Winogrande lacks LLM evaluation prompts.

--- Page 53 ---

Prompt:
The following are multiple choice questions (with answers) about {MMLU subject
name}.
Question 1: {Dev Set Question #1}
A. {Dev Set Option A #1}
B. {Dev Set Option B #1}
C. {Dev Set Option C #1}
D. {Dev Set Option D #1}
Answer: {Dev Set Answer #1}
...
Question 5: {Dev Set Question #5}
A. {Dev Set Option A #5}
B. {Dev Set Option B #5}
C. {Dev Set Option C #5}
D. {Dev Set Option D #5}
Answer: {Dev Set Answer #5}
Now, given the following question and answer choices, output only the letter
corresponding to the correct answer. Do not add any explanation.
Question: {Test Set Question}
A. {Test Set Option A}
B. {Test Set Option B}
C. {Test Set Option C}
D. {Test Set Option D}
Answer:
Example Output:
A
Figure A.5: MMLU Evaluation Prompt. The 5-shot, hard prompt template given to LLMs in order to evaluate them on the
three clinical sections of MMLU. The 5-shot examples were all sourced from the translated MMLU dev set for the given subject
(each subject had exactly 5 examples in its dev set). LLMs were evaluated on all questions in the test set (265/173/166 questions
per language for clinical knowledge/college medicine/virology). If the LLM gave the correct letter answer after extra characters
like parentheses or periods were removed, the LLM’s response was considered correct; otherwise, the LLM’s response was
considered incorrect. This prompt was inferred from the code provided by the authors of MMLU in their GitHub repository
(Hendrycks et al. 2021a). Find the repository here: https://github.com/hendrycks/test

--- Page 54 ---

Prompt:
Given the following passage, query, and answer choices, output only the letter
corresponding to the correct answer. Do not add any explanation.
###
Passage:
{Test Set Passage}
###
Query:
{Test Set Question}
###
Choices:
(A) {Test Set Option A}
(B) {Test Set Option B}
(C) {Test Set Option C}
(D) {Test Set Option D}
###
Answer:
Example Output:
A
Figure A.6: Belebele Evaluation Prompt. The 0-shot, hard prompt template given to LLMs in order to evaluate them
on Belebele. LLMs were evaluated on all questions in Belebele (900 questions per language; Belebele does not have a
dev set). If the LLM gave the correct letter answer after extra characters like parentheses or periods were removed, the
LLM’s response was considered correct; otherwise, the LLM’s response was considered incorrect. This prompt follows
the one provided by the authors of Belebele in their GitHub repository (Bandarkar et al. 2024). Find the repository here:
https://github.com/facebookresearch/belebele

--- Page 55 ---

Prompt:
Given the following sentence and options, output only the number corresponding
to the correct option. Do not add any explanation.
Sentence: {Train Set Sentence}
Option1: {Train Set Option 1}
Option2: {Train Set Option 2}
Correct Option:
Expected Output:
(1 or 2, depending on which is correct)
Figure A.7: Winogrande Supervised Fine-Tuning Prompt. The prompt template used for all experiments that involved fine-
tuning on all of Winogrande or a subset of Winogrande (e.g. for quality and quantity combinations). As is the case for supervised
fine-tuning, the LLMs were given examples of Winogrande questions with correct answers following the template above (similar
to few-shot learning) and were expected to adjust their parameters to perform better on Winogrande as well as tasks like
Winogrande (e.g. other question-answering tasks like MMLU or Belebele), ideally with lifts in African languages (especially
the language used for fine-tuning). The fine-tuning/training examples were sourced from the Winogrande train (small) set,
which has 640 examples per language. The prompt was designed to be as similar as possible to the Winogrande evaluation
prompt we used, which can be seen in Figure A.4.

--- Page 56 ---

Prompt:
Given the following question and answer choices, output only the letter
corresponding to the correct answer. Do not add any explanation.
Question: {Train Set Question}
A. {Train Set Option A}
B. {Train Set Option B}
C. {Train Set Option C}
D. {Train Set Option D}
Answer:
Expected Output:
(A, B, C, or D, depending on which is correct)
Figure A.8: MMLU College Medicine Supervised Fine-Tuning Prompt. The prompt template used for all experiments that
involved fine-tuning on all of MMLU College Medicine or a subset of MMLU College Medicine (e.g. for quality and quantity
combinations). As is the case for supervised fine-tuning, the LLMs were given examples of MMLU College Medicine questions
with correct answers following the template above (similar to few-shot learning) and were expected to adjust their parameters to
perform better on other clinical MMLU sections as well as other, similar question-answering tasks like Winogrande or Belebele,
ideally with lifts in African languages (especially the language used for fine-tuning). The fine-tuning/training examples were
sourced from the entire MMLU College Medicine section, which has 200 examples per language (MMLU subjects do not have
non-test sets large enough for ample fine-tuning, so all of MMLU College Medicine was used for fine-tuning and excluded
from fine-tuned model evaluations). The prompt was designed to be as similar as possible to the MMLU evaluation prompt we
used, which can be seen in Figure A.5.

--- Page 57 ---

Prompt:
I am trying to curate a supervised fine-tuning dataset that will be used to
improve the performance of my LLM on {benchmark} in {target language} (I have
translated {benchmark} from English into many other languages). Please rate the
following fine-tuning dataset sample on a scale of 1-10. Your rating should
reflect the anticipated usefulness of the sample if included in the fine-tuning
dataset for improving my LLM’s performance on {benchmark} (with 1 implying least
useful and 10 implying most useful). Do not include any additional explanation;
just provide the number rating: {fine-tuning dataset sample}
Example Output:
9
Figure A.9: GPT-4o LLM-as-an-Annotator Prompt. The prompt template given to GPT-4o in order to assign quality scores
to rows in our fine-tuning datasets. {benchmark} was substituted for the name of the benchmark (e.g. MMLU, Belebele) as
well as the MMLU section (if the benchmark was MMLU) and a short description of the benchmark (e.g. “a diversity-focused
reading comprehension evaluation benchmark” for Belebele). {target language} was substituted for the full name of the
language that the model would be both fine-tuned in and evaluated on (e.g. “Xhosa”). Finally, {fine-tuning dataset
sample} was substituted with a JSONL row representing a supervised fine-tuning dataset sample that would be used to fine-
tune a GPT model using OpenAI’s fine-tuning API (see https://platform.openai.com/docs/guides/fine-tuning/example-format
for the format of such JSONL dataset fine-tuning rows).

--- Page 58 ---

Shona
Afrikaans
Tsonga
Zulu
Sepedi
Amharic
Xhosa
Igbo
Bambara
Setswana
Sesotho
Language
0%
20%
40%
60%
80%
100%
Percentage of Winogrande Questions (%)
65.3%
58.5%
57.8%
57.1%
52.4%
36.4%
34.0%
17.0%
11.7%
10.0%
4.9%
34.7%
41.5%
42.2%
42.9%
47.6%
63.6%
66.0%
83.0%
88.3%
90.0%
95.1%
Corrected
Not Corrected
Figure A.10: Results of the Translation Verification Task. Translators were tasked to verify translations of the Winogrande
dataset into 11 African languages, and provide corrections if needed. This table shows the proportion of the Winogrande dataset
that needed corrections for each of the 11 African languages. The proportion that needed corrections (orange/top bars) for a
given language ranged from 65.3% on the higher end (Shona) to 4.9% on the lower end (Sesotho).

--- Page 59 ---

bm
am
ig
sn
nso
ts
tn
st
xh
zu
af
en
bm
am
ig
sn
nso
ts
tn
st
xh
zu
af
en
0.65
0.71
0.85
0.66
0.81
0.89
0.73
0.82
0.86
0.89
0.77
0.73
0.84
0.88
0.86
0.7
0.82
0.89
0.9
0.89
0.87
0.72
0.81
0.87
0.94
0.96
0.88
0.91
0.71
0.78
0.85
0.94
0.9
0.87
0.88
0.9
0.66
0.82
0.9
0.96
0.93
0.86
0.92
0.95
0.94
0.51
0.61
0.67
0.72
0.65
0.73
0.71
0.66
0.75
0.72
0.32
0.3
0.47
0.46
0.42
0.57
0.55
0.43
0.5
0.48
0.84
0.0
0.2
0.4
0.6
0.8
1.0
Spearman Correlation
Figure A.11: Correlation of State-of-the-Art Models on Translated Benchmarks. The correlation heat map shows similari-
ties between out-of-the-box LLM performances from Table 2 by language. The color bar shows the Spearman rank correlation,
where values closer to 1 are more correlated. English is the least correlated with the other languages, while the seven Bantu lan-
guages (Zulu, Xhosa, Sesotho, Setswana, Tsonga, Sepedi, and Shona) and Igbo (Volta-Niger) had the highest correlation values
(see Figure A.12 for language families). Bambara and Amharic are the least correlated with the other languages. Language
codes are as follows: Bambara (bm), Amharic (am), Igbo (ig), Shona (sn), Sepedi (nso), Tsonga (ts), Setswana (tn), Sesotho
(st), Xhosa (xh), Zulu (zu), Afrikaans (af), English (en).

--- Page 60 ---

Figure A.12: Language Groupings. This figure shows the 12 languages of this study grouped by where they are most spoken,
geographically. The legend shows the language families.

--- Page 61 ---

xh
ig
ts
bm
am
tn
st
zu
af
nso
sn
Target Language
0.45
0.50
0.55
0.60
0.65
0.70
0.75
0.80
0.85
Percentage of Correct Responses
Inappropriate
Appropriate
Figure A.13: Comparison of GPT-4o Performance on “appropriate” Versus “inappropriate” Winogrande Questions. The
percentage of correct responses for the GPT-4o model when the translation was appropriate (red/dots to the right of language
code x-axis labels) and when the translation was inappropriate (blue/dots directly above language code x-axis labels) are shown
for each target language. The boxplots show the distribution of the percentage of correct responses when repeated random
samples of the same size as the appropriate and inappropriate counts for each target language were drawn; the figure implies
that the differences in performance on the appropriate vs. inappropriate subsets for many languages (e.g. Shona/sn) are unlikely
to be due to chance. Language codes are as follows: Xhosa (xh), Igbo (ig), Tsonga (ts), Bambara (bm), Amharic (am), Setswana
(tn), Sesotho (st), Zulu (zu), Afrikaans (af), Sepedi (nso), Shona (sn).

--- Page 62 ---

xh
zu
af
ig
sn
ts
st
nso
tn
am
bm
xh
zu
af
ig
sn
ts
st
nso
tn
am
bm
1
0.09
0.04
-0.04
0
0.03
-0.02
0
-0.01
0.01
0.03
0.09
1
0.03
0.06
-0.01
0.09
-0.02
0
-0.01
0.01
0.01
0.04
0.03
1
-0.03
0
-0.01
0.02
0
0
0
0.02
-0.04
0.06
-0.03
1
0
-0.03
0.02
0.01
0
0
0
0
-0.01
0
0
1
-0.01 -0.01
0
0
0
-0.01
0.03
0.09
-0.01 -0.03 -0.01
1
-0.01
0
0
-0.01
0.03
-0.02 -0.02
0.02
0.02
-0.01 -0.01
1
0
-0.01 -0.01 -0.01
0
0
0
0.01
0
0
0
1
0
0
0
-0.01 -0.01
0
0
0
0
-0.01
0
1
0
-0.01
0.01
0.01
0
0
0
-0.01 -0.01
0
0
1
0.03
0.03
0.01
0.02
0
-0.01
0.03
-0.01
0
-0.01
0.03
1
0.0
0.2
0.4
0.6
0.8
1.0
Cohen's Kappa
Figure A.14: Inter-rater Agreement on Cultural Inappropriateness across Different Target Languages. For each pair of
languages, we provide the Cohen’s Kappa (κ) measuring the inter-rater agreement of the cultural inappropriateness labels.
Importantly, the analysis only includes translations marked as “Good translation” by both annotators in both languages. Each
cell in the matrix represents the agreement level (ranging from 0 to 1) between pairs of languages, with 1 indicating the highest
level of agreement. The Cohen’s Kappa scores do not show strong agreement on the definition of “cultural appropriateness”
across languages. However, it should be noted that among the languages listed, Xhosa and Zulu are the most closely related
(linguistically), and are also those for which the inter-annotator agreement was the greatest (κ = 0.09). Language codes are
as follows: Xhosa (xh), Zulu (zu), Afrikaans (af), Igbo (ig), Shona (sn), Tsonga (ts), Sesotho (st), Sepedi (nso), Setswana (tn),
Amharic (am), Bambara (bm).

--- Page 63 ---

Figure A.15: Availability of Translators on Upwork.com. We conducted a simple search on Upwork.com for “{Language}
Translator” (where {Language} was substituted with the actual language name) and counted the number of results, indicating
roughly how many translators for each language were available on Upwork.com. The total number of available translators on
Upwork.com was severely limited (less than 100) for several target languages: Xhosa, Sesotho, Shona, Setswana, Bambara,
Sepedi, and Tsonga.

--- Page 64 ---

af
af
zu
xh
am
bm
ig
nso
sn
st
tn
ts
Target Language
0.0
0.2
0.4
0.6
0.8
1.0
ROUGE-1
Winogrande Sim. to MT
MMLU Sim. to MT
Winogrande Sim. to English
MMLU Sim. to English
Figure A.16: ROUGE-1 Scores of Winogrande and MMLU Translations. The figure displays boxplots of ROUGE-1 distri-
butions for the similarity between the Winogrande and MMLU (college medicine, clinical knowledge, and virology sections
combined) rows and their machine translation equivalents, as well as the original English versions, in 11 African languages.
Google Translate was used to produce machine translations for all languages except Setswana (tn), in which case GPT-4o was
used since Google Translate did not support Setswana on its API. MT: Machine Translation, Sim.: Similarity. Language codes
are as follows: Afrikaans (af), Zulu (zu), Xhosa (xh), Amharic (am), Bambara (bm), Igbo (ig), Sepedi (nso), Shona (sn), Sesotho
(st), Setswana (tn), Tsonga (ts).

--- Page 65 ---

af
af
zu
xh
am
bm
ig
nso
sn
st
tn
ts
Target Language
0.0
0.2
0.4
0.6
0.8
1.0
ROUGE-1
Round 1 Sim. to MT
Round 2 Sim. to MT
Round 1 Sim. to English
Round 2 Sim. to English
Figure A.17: ROUGE-1 Scores of Winogrande Translations by Translation Round. The figure displays boxplots of
ROUGE-1 distributions for the similarity between the Winogrande rows and their machine translation equivalents, as well
as the original English versions, in 11 African languages. The ROUGE-1 scores before corrections (Round 1) and after cor-
rections (Round 2) are given. Google Translate was used to produce machine translations for all languages except Setswana
(tn), in which case GPT-4o was used since Google Translate did not support Setswana on its API. MT: Machine Translation,
Sim.: Similarity. Language codes are as follows: Afrikaans (af), Zulu (zu), Xhosa (xh), Amharic (am), Bambara (bm), Igbo
(ig), Sepedi (nso), Shona (sn), Sesotho (st), Setswana (tn), Tsonga (ts).

--- Page 66 ---

A.S.
A.S.
A.V.
A.Z.
B.M.
D.E.
D.H.
D.M.
H.P.
I.M.
M.H.
M.M.
N.H.
N.M.
N.N.
P.H.
P.N.
R.M.
S.D.
S.M.
S.N.
T.B.
T.M.
X.P.
Upwork.com Winogrande Translator Name
0.0
0.2
0.4
0.6
0.8
1.0
ROUGE-1
Similarity to Machine Translation
Similarity to Original English
Figure A.18: ROUGE-1 Scores of Winogrande Translations by Translator. The figure displays boxplots of ROUGE-1 dis-
tributions for the similarity between the Winogrande rows and their machine translation equivalents, as well as the original
English versions, in 11 African languages grouped by the initial Upwork.com human translator that translated the rows. Google
Translate was used to produce machine translations for all languages except Setswana, in which case GPT-4o was used since
Google Translate did not support Setswana on its API. See Table A.32 for translator profiles.

--- Page 67 ---

0.00
0.01
0.02
0.03
0.04
0.05
Permutation Importance
User Warning: Translation Very Similar to MT (Initial Translation)
Language: Tsonga
User Warning: Translation Very Dissimilar to MT (Initial Translation)
User Warning: Translation Matches MT (Corrected Translation)
User Warning: Translation Very Similar to MT (Corrected Translation)
Translation: Needed Correction
Language: Afrikaans
User Warning: Translation Matches MT (Initial Translation)
Translation: Did Not Need Correction
Language: Sesotho
User Warning: Translation Very Dissimilar to MT (Corrected Translation)
Language: Setswana
ROUGE-1 vs MT: (Corrected Translation)
Language: Shona
Language: Amharic
ROUGE-1 vs MT: (Initial Translation)
Language: Xhosa
Language: Sepedi
Language: Bambara
Language: Igbo
Language: Zulu
Feature
Figure A.19: Quality Feature Importances. The plot shows the distribution of feature importances (using the permutation
feature importance measure with n=20) from a random forest model to predict if two independent evaluators annotated the
translation of Winogrande as a “Good translation”. The three most important features were the target languages Zulu, Igbo,
and Bambara. Note that “MT” stands for “Machine Translation”. “ROUGE-1 vs MT” denotes the ROUGE-1 score (a number
between 0 and 1) of the human translation with the machine translation as the reference. Warnings were displayed to translators
according to three possible options: if a translation was “Very Dissimilar” to the corresponding machine translation (ROUGE-1
< 0.50), “Very Similar” (ROUGE-1 > 0.95), or “Matches” (ROUGE-1 = 1.00). A translation “Needed Correction” if and only
if the second translator made changes to the initial translation.

--- Page 68 ---

0.00
0.01
0.02
0.03
0.04
0.05
0.06
0.07
Permutation Importance
User Warning: Translation Very Dissimilar to MT (Corrected Translation)
Language: Tsonga
Translation: Did Not Need Correction
User Warning: Translation Matches MT (Corrected Translation)
User Warning: Translation Very Dissimilar to MT (Initial Translation)
Translation: Needed Correction
ROUGE-1 vs MT: (Initial Translation)
User Warning: Translation Matches MT (Initial Translation)
Language: Zulu
User Warning: Translation Very Similar to MT (Corrected Translation)
User Warning: Translation Very Similar to MT (Initial Translation)
Language: Sesotho
Language: Setswana
Language: Amharic
Language: Shona
Language: Xhosa
ROUGE-1 vs MT: (Corrected Translation)
Language: Sepedi
Language: Bambara
Language: Afrikaans
Language: Igbo
Feature
Figure A.20: Appropriateness Feature Importances without Quality Feature. The plot shows the distribution of feature
importances (using the permutation feature importance measure with n=20) from a random forest model to predict if either
of two independent evaluators annotated the translation of Winogrande as not “typical” (i.e. “inappropriate”). The three most
important features were the target languages Igbo, Afrikaans, Bambara. Note that “MT” stands for “Machine Translation”.
“ROUGE-1 vs MT” denotes the ROUGE-1 score (a number between 0 and 1) of the human translation with the machine
translation as the reference. Warnings were displayed to translators according to three possible options: if a translation was “Very
Dissimilar” to the corresponding machine translation (ROUGE-1 < 0.50), “Very Similar” (ROUGE-1 > 0.95), or “Matches
MT” (ROUGE-1 = 1.00). A translation “Needed Correction” if and only if the second translator made changes to the initial
translation.

--- Page 69 ---

0.00
0.05
0.10
0.15
0.20
Permutation Importance
User Warning: Translation Very Dissimilar to MT (Initial Translation)
ROUGE-1 vs MT: (Initial Translation)
Translation: Needed Correction
User Warning: Translation Matches MT (Initial Translation)
User Warning: Translation Matches MT (Corrected Translation)
Language: Bambara
User Warning: Translation Very Similar to MT (Initial Translation)
User Warning: Translation Very Similar to MT (Corrected Translation)
Language: Zulu
Language: Xhosa
Translation: Did Not Need Correction
Language: Amharic
ROUGE-1 vs MT: (Corrected Translation)
Language: Sesotho
User Warning: Translation Very Dissimilar to MT (Corrected Translation)
Language: Tsonga
Language: Setswana
Language: Shona
Language: Sepedi
Language: Afrikaans
Language: Igbo
Translation: "Quality"
Feature
Figure A.21: Appropriateness Feature Importances with Quality Feature. The plot shows the distribution of feature im-
portances (using the permutation feature importance measure with n=20) from a random forest model to predict if either of
two independent evaluators annotated the translation of Winogrande as not “typical” (i.e. “inappropriate”). Unlike Figure A.20,
this figure includes a translation quality feature (both evaluators gave a “Good translation” rating for the Winogrande transla-
tion). The three most important features were the quality feature, and the target languages Igbo and Afrikaans. Note that “MT”
stands for “Machine Translation”. “ROUGE-1 vs MT” denotes the ROUGE-1 score (a number between 0 and 1) of the human
translation with the machine translation as the reference. Warnings were displayed to translators according to three possible
options: if a translation was “Very Dissimilar” to the corresponding machine translation (ROUGE-1 < 0.50), “Very Similar”
(ROUGE-1 > 0.95), or “Matches” (ROUGE-1 = 1.00). A translation “Needed Correction” if and only if the second translator
made changes to the initial translation.

```
