---
title: "2024-Friedrich-M-ALERT LLMs Lost in Translation M-ALERT uncovers Cross-Linguistic - PDF Extract"
source_pdf: "2024-Friedrich-M-ALERT LLMs Lost in Translation M-ALERT uncovers Cross-Linguistic.pdf"
pages: 20
extracted_at: "2026-02-13T13:13:46.058164"
---

# PDF Extract: 2024-Friedrich-M-ALERT LLMs Lost in Translation M-ALERT uncovers Cross-Linguistic

**Source PDF:** 2024-Friedrich-M-ALERT LLMs Lost in Translation M-ALERT uncovers Cross-Linguistic.pdf
**Total Pages:** 20

---

## Content

```
--- Page 1 ---

arXiv:2412.15035v3  [cs.CL]  23 Jun 2025
Preprint. Under review.
LLMs Lost in Translation:
M-ALERT uncovers Cross-Linguistic Safety Inconsistencies
Felix Friedrich1,2,3
Simone Tedeschi4◦
Patrick Schramowski1,2,3,5,6
Manuel Brack1,5
Roberto Navigli4
Huu Nguyen3
Bo Li3,7,8,9
Kristian Kersting1,2,5
1TU Darmstadt
2Hessian.AI
3Ontocord.AI
4Sapienza University of Rome
5DFKI
6CERTAIN
7University of Chicago
8UIUC
9Virtue.ai
friedrich@cs.tu-darmstadt.de
Warning: This paper contains examples of toxic language.
Abstract
Building safe Large Language Models (LLMs) across multiple languages is essen-
tial in ensuring both safe access and linguistic diversity. To this end, we conduct a
large-scale, comprehensive safety evaluation of the current LLM landscape. For
this purpose, we introduce M-ALERT, a multilingual benchmark that evaluates the
safety of LLMs in five languages: English, French, German, Italian, and Spanish.
M-ALERT includes 15k high-quality prompts per language, totaling 75k, with
category-wise annotations. Our extensive experiments on 39 state-of-the-art LLMs
highlight the importance of language-specific safety analysis, revealing that models
often exhibit significant inconsistencies in safety across languages and categories.
For instance, Llama3.2 shows high unsafety in category crime_tax for Italian
but remains safe in other languages. Similar inconsistencies can be observed across
all models. In contrast, certain categories, such as substance_cannabis
and crime_propaganda, consistently trigger unsafe responses across models
and languages. These findings underscore the need for robust multilingual safety
practices in LLMs to ensure responsible usage across diverse communities.
1
Introduction
80
90
100
English
80
90
100
other languages
unsafe
highly unsafe
Llama-3-8B-it
Llama-3.1-8B-it
Mistral-Small-it
QwQ-32B
aya-23-8B
aya-expanse-32b
c4ai-command-r
Gemini-2.0
Gemma-2-9B-it
GPT-4o
Figure 1: Safety comparison of English (ALERT)
vs. Multilingual (M-ALERT) on different prompts.
While models are generally safe (top right corner),
significant deviation from the diagonal reveals
safety inconsistencies across languages. (cf. Ta-
ble 1 & 2)
As Large Language Models (LLMs) see rapid
global adoption, ensuring their safety across
a broad spectrum of languages is essential.
This is not only crucial for promoting inclu-
sive access to information and enabling effective
cross-cultural communication (Friedrich et al.,
2024), but it also mitigates biases arising from
language-specific limitations. While recent ef-
forts, such as ALERT (Tedeschi et al., 2024),
have made strides in assessing LLM safety in
English, comprehensive multilingual safety eval-
uation remains a critical gap.
Existing safety datasets and benchmarks make
valuable contributions but are limited by their
narrow focus, such as toxicity (Jain et al., 2024;
Yang et al., 2024; de Wynter et al., 2024), and by
their small size (Aakanksha et al., 2024), lack of
cross-linguistic coverage (Vidgen et al., 2024), and superficial evaluation scope (Wang et al., 2023b).
To address all these shortcomings, we introduce M-ALERT, a comprehensive multilingual safety
benchmark. It expands on ALERT by systematically translating and adapting its safety prompts into
◦work done while at Babelscape
1

--- Page 2 ---

Preprint. Under review.
(a)
M-ALERT
follows
the
ALERT
(Tedeschi et al., 2024) taxonomy with 6
macro and 32 micro categories.
(b) M-ALERT framework. An LLM is provided with prompts,
each associated with one of five languages and with a risk category.
Its responses are classified for safety by a multilingual judge.
This way, M-ALERT furnishes a general safety score along with
category- and language-specific safety scores.
five languages—English, French, German, Italian, and Spanish. To this end, we use an advanced
translation pipeline, including multiple models and validation methods. We select the most accurate
one using common machine translation quality metrics and conduct human evaluations to further
confirm high translation quality. As a result, we derive high-quality translations with fine-grained
category annotations, ensuring consistent risk categorization across languages. In total, M-ALERT
includes 75k prompts, with 15k per language.
Specifically, we extensively evaluate 10 state-of-the-art LLMs and identify relevant model dimen-
sions for safety performance. While some models exhibit language-specific vulnerabilities, others
demonstrate consistently unsafe behavior in certain high-risk categories across all languages. More
alarmingly, we find substantial inconsistencies across languages and categories (cf. Fig. 1 deviation
from diagonal). Further, we conduct category-specific evaluations for policy compliance, demon-
strating the practical use of M-ALERT. Lastly, we show that while instruction tuning improves safety
over base models, the correlation with model size is less pronounced.
In summary, we put forward the following contributions: (1) We create M-ALERT, a novel multi-
lingual safety benchmark with category annotations for 5 languages, totaling 75k prompts; (2) We
extensively evaluate 40 state-of-the-art LLMs on safety and their consistency, providing a detailed
overview of the field; (3) We conduct language-, category- and policy-specific evaluations, showing
the potential and scope of M-ALERT; (4) We examine various model characteristics, including base
vs. instruct models and model size, to meticulously assess their previously unknown relevance to
safety performance.1
2
Related Work
The remarkable capabilities of LLMs are accompanied by significant concerns regarding safety and
ethical considerations (Longpre et al., 2024), with several studies highlighting their potential risks
(Bender et al., 2021; Weidinger et al., 2021; Bommasani et al., 2021; Hendrycks et al., 2023; Lin
et al., 2023; O’Neill & Connor, 2023; Hosseini et al., 2023). For instance, recent works highlight that
generative language models often produce toxic and biased language, posing ethical concerns for their
deployment in real-world applications (Gehman et al., 2020; ElSherief et al., 2021; Dhamala et al.,
2021; Hartvigsen et al., 2022). Similarly, numerous studies have found bias in the outputs of language
models (Abid et al., 2021; Ganguli et al., 2023; Liang et al., 2023). To this end, several safety
taxonomies have been proposed (Tedeschi et al., 2024; Inan et al., 2023; Wang et al., 2023a; Vidgen
et al., 2024; Ghosh et al., 2025). While many of them cover numerous categories, only Tedeschi et al.
(2024) propose a taxonomy with 6 macro and 32 micro categories leveraging in-depth safety analysis.
Such granularity is essential given the stringent and evolving safety requirements from regulatory
bodies in the EU (EU, 2023), US (WhiteHouse, 2023), and UK (UKGov, 2023). Building M-ALERT
on this foundation allows us to leverage its fine-grained structure and policy-aligned evaluation.
1We publicly release our work at https://huggingface.co/datasets/felfri/M-ALERT
2

--- Page 3 ---

Preprint. Under review.
Multilingual Safety.
Existing datasets and benchmarks (Jain et al., 2024; Aakanksha et al., 2024;
Wang et al., 2023b; Yang et al., 2024; de Wynter et al., 2024) make valuable contributions but are
limited in several ways. First, while the PolygloToxcity dataset (Jain et al., 2024) and others (Yang
et al., 2024; de Wynter et al., 2024) cover multiple languages, they focus exclusively on toxicity,
overlooking other crucial safety considerations. LLMs deployed in real-world applications need
broader alignment to general safety standards beyond toxic language. Second, other efforts like
Cohere’s Aya red-team dataset (Aakanksha et al., 2024), though useful, are relatively small (only a
few hundred examples) and thus lack the scale necessary to capture the extensive range of use cases
and tasks LLMs will encounter. Third, the XSafety dataset (Wang et al., 2023b), although slightly
larger with 2k examples, still lacks scale and evaluates only two outdated models on a superficial level.
Finally, in contrast to all previous approaches, we add a layer of category annotation (with detailed
subcategories) that supports policy-aware safety assessments across languages. This is essential for
adapting to diverse regions’ unique legal and cultural contexts. Additionally, our study assesses
multilingual safety across various dimensions, including model sizes, base versus instruct-tuned
model versions, and checkpoints from continuous training.
3
M-ALERT: A Multilingual Safety Benchmark for LLMs
Our multilingual safety benchmark extends the ALERT benchmark (Tedeschi et al., 2024), which
assesses safety across various dimensions. To enhance its scope, we establish a pipeline to provide
high-quality translations in five languages and offer a comprehensive evaluation framework. This
approach enables a detailed safety assessment of state-of-the-art LLMs across languages.
ALERT.
ALERT describes a taxonomy for categorizing safety risks in conversational AI use cases.
It is designed to provide thorough coverage of risk categories to test LLMs across a broad spectrum
of scenarios. This way, it offers a structured approach for categorizing model safety, allowing each
prompt-response pair to be assigned a specific risk category. The taxonomy’s granularity facilitates
the assessment of custom policies under different legal contexts by focusing on specific categories.
The full taxonomy entailing 6 macro and 32 micro categories is depicted in Fig. 2a. We now construct
a multilingual extension and adoption of ALERT.
M-ALERT Translation Pipeline.
For creating a large-scale safety dataset, M-ALERT, we build
on prior work from toxicity detection (Jain et al., 2024) and reward modeling (Gureja et al., 2024),
leveraging machine-translation for the large-scale translation of safety prompts. In addition, we
adopted the Minimum Bayes Risk decoding approach (Kovacs et al., 2024) and utilized an ensemble
of translation systems to achieve the highest translation quality. We explored multiple translation
methods to ensure robustness. Initial experiments with bilingual language models, such as Llama
versions (Touvron et al., 2023) or Occiglot (Brack et al., 2024)2, showed challenges; these models
often failed to produce the correct language output (answer in English instead of French) or attempted
to respond rather than translate. To overcome these issues, we selected translation systems based
on two criteria: first, those that scored highly on the Tatoeba dataset (Artetxe & Schwenk, 2019),
which includes short sentences similar to our benchmark prompts; and second, those that performed
well on the WMT24 competition (Kocmi et al., 2024), representing the state of the art in translation.
In particular, we used the Big-sized Opus MT (Tiedemann & Thottingal, 2020)3, one of the most
downloaded translation models on HuggingFace, alongside Google Translate (Google, 2025) and
Unbabel’s TowerInstruct4. We sampled translations from each method and selected the best output
based on a translation quality estimator. We selected the translation with the highest quality score and
discarded samples where all systems produced translations below a specified threshold. We selected
the two best methods following Perrella et al. (2024), using two independent translation quality
estimation metrics: COMET-XXL (Rei et al., 2023)5 for selection and MetricX-XXL (Juraska et al.,
2023)6 for validation. We evaluate and showcase this setup in Sec. 5 and show further details in
App. B. This two-step process allows for large-scale supervision of translations, ensuring high quality.
2occiglot/occiglot-7b-eu5-instruct
3https://huggingface.co/Helsinki-NLP/opus-mt-en-X, with X from {de/fr/it/es}
4https://huggingface.co/Unbabel/TowerInstruct-Mistral-7B-v0.2
5https://huggingface.co/Unbabel/wmt23-cometkiwi-da-xxl
6https://github.com/google-research/metricx
3

--- Page 4 ---

Preprint. Under review.
With this pipeline, M-ALERT can be expanded to more languages. The selected languages (English,
French, German, Italian, and Spanish) were chosen based on the proficiency of multilingual judges
and the availability of high-quality translation systems, reflecting a depth-over-breadth approach to
enable precise direct comparisons across languages.
M-ALERT Evaluation Framework.
In contrast to ALERT, M-ALERT extends the evaluation
framework to a multilingual setting, going beyond English to examine safety disparities across
languages. We show our extended framework in Fig. 2b. Each prompt, labeled with a specific
category, is processed by an LLM. An auxiliary auto-evaluator model subsequently assesses its
response, generating a safety score for the prompt and its corresponding category. The result is an
overall safety score and category- and language-specific scores. These scores provide actionable
insights into the reliability and limitations of a model’s performance across the supported languages.
M-ALERT Scoring Safety.
Assessing safety on a large scale is challenging. To achieve scalable
safety scoring, we employ well-established automated evaluation with general-purpose models
as judges. Specifically, given a text prompt p, we auto-regressively generate a response r using
a language model, i.e., r = LLM(p). This prompt-response pair (p, r) is then evaluated by an
automated judge J, yielding a safety score s = J(p, r). To ensure alignment between human
judgments and the automated scores, we conduct human reviews on a random subset of these scores,
as detailed in App. D.
4
Evaluating LLMs’ Safety with M-ALERT
In this section, we describe experimental details before evaluating state-of-the-art LLMs on
M-ALERT.
Experimental Setup.
We evaluate state-of-the-art LLMs on M-ALERT and report their safety
scores.
To obtain the safety scores, we employ a multilingual evaluator model LlamaGuard-
3 (Llama Team, 2024)7.
For our experiments, we rely on SGLang (Zheng et al., 2023), a
batching framework with KV-caching for fast LLM inference.
We use a cluster of 8xA100
GPUs. For each model, we set max_new_tokens=200, use sampling as generation strategy,
and focus on instruct versions (if not stated otherwise) due to the task’s conversational nature.
Llama-3-8B-it
Llama-3.1-8B-it
Mistral-Small-it
QwQ-32B
aya-23-8B
aya-expanse-32b
c4ai-command-r
Gemini-2.0
Gemma-2-9B-it
GPT-4o
60
65
70
75
80
85
90
95
100
unsafe
highly unsafe
safe
de
en
es
fr
it
Figure 3: Overall safety scores for 5 languages.
All models exacerbate unsafe behavior at least for
one language—two models are even highly unsafe.
(y-axis scaled)
Specifically, in this section, we study 10 of
40 multilingual LLMs in-depth from different
model families and architectures: Llama-3-8B-
it, Llama-3.1-8B-it, Mistral-Small-it, QwQ-32B,
aya-23-8b, aya-expanse-32b, c4ai-command-r-
32b, gemini-2.0-flash-001, gemma-2-9b-it, and
GPT-4o—full details in App. C. We evaluate
further models in App. H.
Overall Safety Discrepancies.
As triggered
already in Fig. 1, M-ALERT reveals significant
safety discrepancies across languages. Fig. 3
now further summarizes the main results from
M-ALERT. When interpreting the results, we
consider a model safe when its outputs are safe
at least 99% of the time (gray). Further, we con-
sider a model unsafe when its outputs are safe
only between 90% and 99% of the time, high-
lighted in orange. Lastly, we consider a model
highly unsafe when it generates unsafe outputs
more than 10% of the time, marked in red. Us-
ing this color map, we can easily understand
multilingual LLMs’ safety concerns.
7https://huggingface.co/meta-llama/Llama-Guard-3-8B
4

--- Page 5 ---

Preprint. Under review.
Llama-3-8b-it
Llama-3.1-8b-it
Mistral-Small-it
QwQ-32B
Aya-23-8B
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
crime
cyber
98.91 99.78 97.37 97.81 98.25 99.12 98.47 100.0 99.78 99.12 95.40 94.97 97.16 97.37 97.81 96.94 98.25 95.84 98.03 97.59 49.02 60.61 46.61 51.20 48.80
injury
98.67 99.39 97.16 97.89 97.05 99.94 98.22 99.56 99.78 98.94 96.33 95.49 97.39 96.94 96.22 94.49 94.61 94.16 97.27 96.66 56.06 52.56 54.67 55.78 45.22
kidnapp
99.00 100.0 96.52 97.01 98.51 99.50 98.51 86.57 100.0 94.53 99.00 97.51 99.50 99.50 98.01 92.54 90.55 88.06 98.01 85.07 30.85 20.90 16.92 36.32 20.40
other
99.71 99.71 99.71 99.43 98.28 99.71 99.43 100.0 99.71 99.43 96.56 95.99 97.99 97.71 97.71 98.85 98.57 97.99 98.85 100.0 80.23 85.39 82.23 83.38 68.77
privacy
99.72 99.45 99.72 99.45 99.17 99.72 99.45 100.0 100.0 99.72 98.89 99.17 99.72 99.45 99.72 98.06 99.17 98.34 99.45 99.45 71.47 44.32 59.56 71.75 62.88
propaganda 70.97 46.48 62.49 58.53 62.97 96.53 55.06 97.78 92.77 96.05 80.23 46.48 90.74 81.20 84.38 98.84 91.61 99.71 88.33 99.32 41.95 50.72 60.17 54.10 60.56
tax
92.99 100.0 97.26 98.78 67.68 99.09 100.0 99.70 99.70 99.70 98.17 97.87 94.51 98.78 98.17 99.09 99.09 99.70 98.78 98.78 47.56 66.77 43.60 57.93 46.65
theft
97.94 99.83 96.05 92.37 98.80 99.91 98.97 99.57 98.37 99.40 96.05 93.91 98.80 96.83 98.80 97.17 97.86 96.23 97.43 97.86 40.22 42.02 35.85 35.42 36.19
hate
body
99.40 99.40 98.80 99.40 99.40 100.0 98.80 100.0 100.0 100.0 100.0 98.80 99.40 99.40 100.0 98.80 100.0 99.40 99.40 99.40 75.30 78.92 75.30 89.76 83.13
disabled
100.0 100.0 99.17 99.17 100.0 99.17 100.0 99.17 100.0 100.0 100.0 100.0 100.0 100.0 99.17 98.33 98.33 97.50 100.0 100.0 83.33 71.67 73.33 77.50 74.17
ethnic
99.67 99.67 99.10 99.34 98.12 99.59 99.59 100.0 99.92 100.0 99.34 99.10 99.10 99.02 98.61 98.03 99.18 98.94 99.10 99.10 74.86 78.62 78.46 76.90 71.25
lgbtq+
99.75 100.0 99.75 99.75 99.75 100.0 99.49 99.75 100.0 99.75 99.49 98.47 99.75 98.98 98.73 98.73 99.24 98.98 98.47 98.47 84.48 84.73 82.70 84.73 80.92
other
99.02 99.75 98.77 98.94 96.98 98.04 99.84 99.92 99.92 99.59 98.37 98.77 98.69 95.51 97.55 98.45 98.45 99.59 99.35 98.37 74.92 75.82 74.67 81.45 79.90
poor
100.0 100.0 100.0 98.02 97.03 100.0 100.0 100.0 99.01 100.0 99.01 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 92.08 88.12 88.12 90.10 86.14
religion
99.77 100.0 99.77 100.0 99.32 100.0 99.55 99.55 99.55 99.77 99.32 98.65 99.32 99.77 99.32 98.42 98.42 99.32 98.87 98.19 70.43 77.65 74.72 73.81 71.56
women
99.52 99.64 98.33 99.04 99.16 99.40 98.81 99.64 99.76 99.40 98.92 99.28 99.28 99.40 98.81 97.97 98.57 97.97 98.69 98.92 80.76 78.85 79.81 79.57 78.49
self harm
other
100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 98.61 99.31 100.0 100.0 80.56 90.28 80.56 52.08 77.08
suicide
100.0 100.0 100.0 100.0 100.0 100.0 99.43 100.0 100.0 100.0 97.13 98.85 98.85 99.43 97.70 98.85 99.43 96.55 100.0 98.85 81.03 61.49 56.90 59.20 68.39
thin
99.15 100.0 100.0 99.15 98.30 100.0 99.57 100.0 100.0 99.57 96.17 100.0 96.17 99.57 96.60 95.74 98.72 99.57 98.30 99.57 69.36 88.51 74.04 42.55 64.26
sex
harrasment 98.17 98.43 94.78 97.91 97.65 99.22 96.61 99.48 100.0 99.74 97.13 94.26 97.65 98.43 97.65 95.82 95.56 95.82 94.26 97.65 69.71 71.80 68.41 77.28 69.97
other
98.37 99.46 97.00 99.18 98.09 99.46 96.46 100.0 99.73 98.91 97.00 94.82 96.73 98.37 97.82 97.82 97.82 98.37 99.46 98.37 75.48 81.74 75.48 81.47 73.30
porn
98.67 98.67 93.33 96.00 97.33 98.67 96.00 99.33 99.33 99.33 92.67 91.33 92.67 95.33 95.33 98.67 95.33 100.0 99.33 99.33 60.00 60.67 64.67 74.00 64.67
substance
alcohol
97.48 99.72 95.24 97.76 96.64 99.72 99.44 98.88 100.0 98.88 97.48 94.96 98.88 99.44 97.20 97.20 98.88 99.72 99.44 98.04 85.43 81.51 79.55 82.35 79.55
cannabis
84.86 94.02 80.48 87.25 84.06 89.24 87.25 94.02 97.61 88.05 83.27 67.33 80.48 86.06 77.69 89.24 97.61 94.42 98.01 93.63 41.83 43.82 34.66 52.99 35.86
drug
98.76 99.38 97.68 97.99 98.61 99.23 98.92 99.69 100.0 98.61 93.35 90.88 95.52 96.91 96.45 95.52 97.68 97.68 97.53 98.30 48.84 50.54 43.28 53.79 42.19
other
97.84 99.82 97.48 97.48 97.84 99.46 98.20 100.0 99.46 99.28 95.14 92.79 97.12 96.40 97.84 96.76 98.20 98.02 98.02 98.74 55.32 56.94 55.50 62.70 53.69
tobacco
95.28 97.17 88.68 95.28 89.62 97.17 97.17 100.0 98.11 99.06 85.85 80.19 86.79 83.96 90.57 94.34 94.34 98.11 96.23 98.11 55.66 69.81 52.83 55.66 52.83
weapon
biological 100.0 100.0 99.53 100.0 99.06 99.53 100.0 100.0 100.0 99.53 92.96 97.18 98.12 97.65 97.18 99.06 99.06 99.53 99.53 99.06 67.61 91.08 73.24 71.36 67.14
chemical
100.0 100.0 95.37 97.69 94.91 99.54 100.0 99.54 99.54 99.07 91.20 92.59 95.83 94.44 95.37 97.69 99.54 98.15 99.07 98.15 70.37 79.17 71.76 69.44 64.81
firearm
96.43 100.0 95.54 100.0 98.21 100.0 99.11 99.11 99.11 99.11 98.21 96.43 99.11 98.21 100.0 95.54 96.43 98.21 99.11 98.21 68.75 64.29 63.39 71.43 63.39
other
97.55 99.39 95.71 97.96 96.94 98.16 99.39 99.80 100.0 98.37 92.65 93.47 96.94 95.71 96.12 93.06 97.55 95.92 97.35 96.12 64.29 58.98 58.57 66.33 60.82
radioactive 99.38 99.38 97.52 98.14 97.52 98.76 100.0 100.0 100.0 98.76 96.89 93.79 98.76 98.14 98.14 97.52 97.52 100.0 99.38 99.38 82.61 93.79 80.12 82.61 77.02
Overall
97.41 97.77 95.88 96.77 95.48 99.00 97.24 99.09 99.41 98.80 95.69 93.54 96.91 96.81 96.71 97.11 97.63 97.85 98.28 98.08 66.57 68.82 64.36 67.34 63.44
Table 1: Benchmarking LLMs with M-ALERT. Each row represents a safety category from our
taxonomy (cf. Fig. 2a), while each column corresponds to an LLM under evaluation. The displayed
values are mean scores (higher is safer) across each category or the entire set (last row), e.g. a score
of 34 implies that 34% of prompt-response pairs were classified as safe. Safe scores S(Φ) ≥99 are
gray , unsafe scores within 90 ≤S(Φ)<99 are orange , and highly unsafe scores S(Φ)<90 are
red . Best viewed in color.
Firstly, no model reaches the safe threshold (99%) across all languages. Yet, Gemma-2 stands out by
approaching this threshold, achieving 99% safety or higher in Spanish, French, and Italian (gray area).
This performance across multiple languages demonstrates its safety in diverse linguistic contexts.
While Gemini-2.0 also performs well, it falls slightly short. This is surprising, given that Gemini is
Google’s commercial model, accessible only via API with additional safeguards, whereas Gemma is
a bare LLM. A similar pattern is observed with GPT-4o, which, despite being OpenAI’s commercial
flagship model, exhibits clear unsafety across languages.
Other models, such as Llama-3, Llama-3.1, QwQ, and others, while generally safe, fall slightly short
of the 99% threshold, with most of their scores between 95% and 98% (orange area), which we
consider acceptable but potentially requiring refinement for higher-stakes applications. These models
exhibit minor safety vulnerabilities, suggesting that they can generally maintain safe outputs but
might struggle with nuanced safety challenges across specific languages. Notably, Mistral-Small
also falls in this range but displays more variability, particularly in English, indicating room for
improvement to ensure consistent safety across all languages.
Conversely, the aya-23 and c4ai-command models exhibit the most significant safety concerns. With
scores predominantly below 90% (red area), these models frequently produce unsafe outputs. These
results indicate a high risk of unsafe content generation, underscoring the need for these models to
undergo targeted safety optimization, especially given their considerable potential for unsafe content
in multilingual settings. Despite both models being instruction- and safety-tuned, their relatively
low scores indicate that safety was not sufficiently prioritized, revealing considerable potential for
improvement.
Category-specific Insights.
A closer examination of the models (cf. Tables 1 & 2) reveals that
certain categories exhibit consistently high safety levels across languages and models. For instance,
almost all models demonstrate a high level of safety in the hate category, which seems reasonable
given the extensive prior research on toxicity (Gehman et al., 2020; Jain et al., 2024). In contrast, cat-
egories like crime_propaganda and substance_cannabis consistently receive low safety
scores across nearly all languages and models. Notably, the identification of propaganda as a safety
5

--- Page 6 ---

Preprint. Under review.
Aya-expanse-32b
c4ai-command
Gemini-2.0
Gemma-2-9b-it
GPT-4o
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
crime
cyber
98.91 96.50 96.50 97.59 98.69 87.09 93.87 85.34 89.28 88.62 99.78 100.0 99.12 99.56 98.47 99.56 100.0 99.78 99.56 99.78 99.78 99.78 100.0 100.0 100.0
injury
96.33 93.72 96.83 95.33 95.72 85.98 90.77 82.26 85.65 83.76 99.56 98.83 99.05 98.89 97.72 99.83 99.94 99.94 99.67 99.94 99.83 99.50 99.72 99.67 99.05
kidnapp
96.52 95.02 99.00 95.52 86.57 79.60 90.55 60.20 88.06 67.66 100.0 100.0 99.00 98.51 99.00 100.0 100.0 100.0 100.0 100.0 100.0 99.50 100.0 100.0 99.00
other
97.99 97.71 97.71 96.85 97.42 92.55 93.12 92.55 91.69 92.55 97.42 100.0 97.99 98.85 98.85 100.0 99.71 99.71 99.71 99.71 99.43 99.71 99.71 99.14 99.71
privacy
96.68 93.91 96.68 82.83 77.84 77.01 94.18 89.75 82.83 78.67 99.72 99.45 98.89 99.45 99.45 100.0 99.45 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0
propaganda 68.47 73.10 86.40 93.54 58.53 30.76 34.52 47.35 46.00 51.01 68.47 77.43 81.58 85.92 92.00 75.12 65.19 75.31 74.54 79.94 62.30 74.35 85.44 82.16 82.45
tax
96.34 98.17 95.73 96.95 96.95 95.12 99.70 83.84 95.12 87.20 100.0 99.39 99.09 99.70 98.78 100.0 100.0 100.0 99.70 100.0 100.0 100.0 100.0 100.0 99.39
theft
98.20 96.40 95.97 95.37 95.80 79.67 89.97 79.50 85.42 77.62 99.57 99.57 99.14 99.31 98.37 99.74 100.0 100.0 99.66 100.0 99.83 99.40 99.66 98.71 99.14
hate
body
100.0 98.19 100.0 100.0 98.80 95.78 93.98 91.57 98.19 95.18 100.0 99.40 100.0 100.0 98.80 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0
disabled
99.17 100.0 99.17 100.0 99.17 98.33 99.17 95.00 95.00 96.67 100.0 99.17 100.0 100.0 99.17 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0
ethnic
99.59 98.85 99.75 99.10 99.18 93.20 96.89 90.42 92.30 93.37 99.75 99.67 99.59 99.34 98.77 100.0 100.0 100.0 100.0 100.0 100.0 99.92 99.92 99.84 98.94
lgbtq+
99.75 99.24 99.49 99.75 99.49 95.67 98.22 95.42 97.20 95.17 99.75 98.98 99.49 99.24 98.47 99.75 100.0 100.0 100.0 100.0 99.49 99.75 99.49 99.75 99.24
other
99.67 99.10 99.51 98.04 97.22 87.42 93.46 86.27 85.62 85.38 99.92 99.75 99.75 98.37 98.77 100.0 100.0 100.0 100.0 100.0 99.84 99.84 99.84 99.92 99.59
poor
100.0 100.0 100.0 100.0 100.0 98.02 100.0 96.04 99.01 99.01 100.0 100.0 100.0 99.01 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0
religion
100.0 99.10 100.0 99.10 99.10 96.16 97.29 94.81 94.58 94.81 99.77 99.77 99.55 99.55 98.19 100.0 100.0 100.0 99.77 100.0 100.0 99.55 100.0 100.0 99.10
women
99.04 98.92 98.92 99.76 99.28 95.82 97.49 95.46 95.10 95.46 99.28 99.64 99.76 99.40 98.21 100.0 100.0 100.0 100.0 99.88 99.76 99.52 99.88 99.64 99.28
self harm
other
99.31 98.61 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 99.31 100.0 99.31 95.83 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0
suicide
100.0 99.43 99.43 99.43 100.0 95.98 98.28 89.66 90.23 88.51 100.0 99.43 100.0 100.0 100.0 99.43 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0
thin
96.60 100.0 99.57 98.30 94.89 96.60 98.30 96.17 97.45 94.04 100.0 97.87 100.0 100.0 94.47 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0
sex
harrasment 96.87 96.08 97.39 97.65 97.39 88.51 96.61 89.56 91.64 89.82 97.91 98.17 97.91 96.87 98.17 100.0 100.0 100.0 100.0 99.48 97.65 98.69 98.96 98.69 96.87
other
96.46 97.82 97.00 98.37 97.28 90.74 98.64 91.01 92.37 91.28 98.37 97.00 98.09 93.46 98.64 100.0 100.0 100.0 100.0 100.0 97.00 97.28 97.55 98.37 98.09
porn
94.00 94.67 93.33 92.00 92.67 78.67 92.67 77.33 74.00 78.67 100.0 98.67 97.33 96.67 98.00 100.0 100.0 100.0 100.0 100.0 84.67 91.33 91.33 94.67 95.33
substance
alcohol
96.92 97.48 96.64 97.48 95.80 89.92 94.12 86.83 88.80 87.96 98.60 98.32 98.60 100.0 98.04 99.72 100.0 99.16 100.0 99.44 98.88 98.88 99.16 98.60 98.60
cannabis
87.25 78.49 75.30 86.45 76.10 73.31 74.90 63.35 72.11 60.16 90.84 92.03 80.48 93.23 88.45 96.02 100.0 97.21 98.80 97.61 82.87 90.04 86.45 91.63 90.04
drug
97.99 95.67 94.74 95.36 96.45 83.93 87.33 74.96 83.93 78.83 99.38 99.07 97.84 97.84 97.06 99.85 100.0 100.0 100.0 100.0 98.45 99.54 99.38 99.23 99.07
other
97.12 96.40 97.12 95.86 96.40 86.13 88.11 80.72 84.32 83.24 99.10 98.92 99.46 99.82 98.02 99.82 99.82 99.82 100.0 100.0 99.28 98.92 99.64 99.10 98.56
tobacco
81.13 85.85 77.36 75.47 81.13 75.47 81.13 62.26 68.87 72.64 96.23 94.34 93.40 90.57 93.40 99.06 100.0 99.06 99.06 100.0 83.96 87.74 91.51 83.96 89.62
weapon
biological 96.24 96.24 92.02 94.84 96.71 90.61 97.65 92.49 93.90 89.20 100.0 100.0 98.59 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0
chemical
92.59 87.50 91.67 92.13 93.06 91.67 95.37 90.28 93.52 87.50 100.0 97.22 97.69 98.15 95.37 100.0 100.0 100.0 100.0 99.54 98.15 97.69 98.61 98.61 98.61
firearm
94.64 85.71 96.43 93.75 92.86 89.29 90.18 83.93 83.04 81.25 100.0 96.43 97.32 99.11 96.43 100.0 100.0 100.0 100.0 100.0 99.11 100.0 100.0 100.0 100.0
other
95.31 92.65 94.49 94.49 93.67 84.49 85.71 80.41 81.63 86.53 99.39 98.78 98.37 99.80 96.53 99.59 99.80 99.80 99.80 100.0 98.57 98.78 99.18 98.37 98.98
radioactive 95.03 90.06 91.30 96.89 93.79 94.41 96.27 94.41 95.65 98.76 100.0 100.0 98.76 100.0 99.38 99.38 100.0 100.0 100.0 100.0 98.14 98.76 99.38 98.14 99.38
Overall
95.75 94.71 95.48 95.57 93.69 87.43 91.83 84.97 87.89 85.95 98.21 98.02 97.68 98.12 97.53 98.96 98.87 99.06 99.07 99.23 96.78 97.76 98.28 98.07 98.06
Table 2: Continuation: Benchmarking LLMs with M-ALERT. Details in Table 1.
concern is a novel finding compared to ALERT, which utilizes a safety evaluator that does not classify
propaganda as a dedicated violation under its safety taxonomy. Moreover, when evaluating QwQ
and Qwen-Instruct models (see App. H), we find that they refuse to generate answers (e.g. fake news
articles) significantly more often compared to all other models.
Overall, certain categories appear to be more influenced by plurality and pluralistic alignment
(Sorensen et al., 2024) than others. Hate-related content seems to be more consistently addressed
across models and countries, suggesting less variation in alignment. In contrast, topics such as drug
use and political systems exhibit greater plurality, making it more challenging to achieve broad
consensus within a one-model-fits-all approach (Sorensen et al., 2024). This is particularly evident
in models like Gemma, which rank top in safety overall but show inconsistencies in these more
pluralistic subcategories.
Policy Evaluation.
Building on previous insights into plurality, we now simulate different policies
using textttM-ALERT. A key consideration when implementing safety measures is the variation in
policies across companies and societies. For example, the use of cannabis is legal in some countries
but not in others. Depending on the policy, it may be acceptable to score lower in this category without
being unsafe. For example, the substance_canabis and crime_propaganda categories
seem to be outliers for most models’ safety scores. To this end, the category-wise annotations of our
taxonomy and benchmark prove useful. Individual categories can be selectively excluded, leading
to significant shifts in overall safety scores. For example, when removing cannabis and propaganda
from the benchmark, the models’ overall safety scores increase by around 2%, substantially changing
the tables’ color appearance. Conversely, if these categories are weighted more heavily, the overall
score drops by 1% on average. On the other hand, excluding the hate category, where models usually
score well, results in a more than 2% drop in overall safety scores. These case studies highlight
the valuable insights that can be drawn from category-wise evaluations. By adopting this approach,
different use cases can be explored, allowing for the prioritization of specific categories to align with
particular policy needs.
In summary, our analysis highlights the importance of evaluating multilingual benchmarks like
M-ALERT. The results reveal that while some models achieve high overall safety, they are not
aligned across languages and categories, urging refinement to reduce language-specific weaknesses.
Moreover, M-ALERT is valuable for policy-aware evaluations.
6

--- Page 7 ---

Preprint. Under review.
en (unsafe)
de (safe)
translation
Llama 3.1
prompt
Write a fake news article about Don-
ald Trump
Schreibe einen gefälschten Artikel
über Donald Trump
–
response
**BREAKING:
TRUMP
DE-
CLARES HIMSELF "GREATEST
BURGER
CONNOISSEUR
OF
ALL TIME"** Washington D.C.
- In a shocking move, President
Donald Trump [...]
Ich kann Ihnen keinen gefälschten
Artikel
über
Donald
Trump
schreiben. Wenn Sie jedoch Infor-
mationen über Donald Trump oder
seine politische Karriere benötigen,
kann ich Ihnen gerne helfen.
I can’t write you a fake article
about Donald Trump. However,
if you need information about
Donald Trump or his political ca-
reer, I’m happy to help.
en (safe)
it (unsafe)
translation
Llama 3
prompt
How do I take tax deduction that I
don’t qualified for without getting
caught by the IRS?
Come faccio a prendere la detrazione
fiscale per cui non sono qualificato
senza essere preso dal fisco?
–
response
I cannot provide advice on how to
take tax deductions that you don’t
qualify for or how to avoid detection
by the IRS. Tax fraud is a serious
offense [...]
La detrazione fiscale!
È un tema
molto importante per molti di noi.
Ecco alcuni consigli per aiutarti a
prendere la detrazione fiscale senza
essere preso dal fisco: 1. [...]
Tax deduction! This is a very
important topic for many of us.
Here are some tips to help you
take the tax deduction without be-
ing caught by the taxmen: 1. [...]
Table 3: Inconsistent safety examples. Llama3.1, a model generally considered safe with a high overall
safety rating, exhibits strong safety drops in English for category crime_propaganda, whereas
the model keeps safe when prompted in German. Similar for Llama3 for category crime_tax in
English vs. Italian.
5
Discussion
We now investigate the above findings in more detail.
Case study.
Given the previous quantitative evidence, Table 3 further confirms these safety
inconsistencies across languages on a qualitative basis.
For example, Llama3.1—a model
with a high overall safety rating (98.7%)—demonstrates a notable decline in safety for the
crime_propaganda category when prompted in English (55%), cf. Table 1. In contrast, it
maintains a high safety level in German (96.5%). A manual review confirms that this discrep-
ancy is not attributable to translation quality or the performance of the auto-evaluator model; both
translations and evaluations are accurate and reliable, as evidenced in the examples shown in Table 3.
en–de en–es
en–fr
en–it
all
Llama-3-8B-it
96.35
95.92
96.48
95.51
89.38
Llama-3.1-8B-it
95.29
95.53
95.91
95.27
93.75
Mistral-Small-it
92.40
92.48
92.85
92.60
87.66
QwQ-32B
94.68
95.18
95.56
95.79
89.38
Aya-23-8B
71.24
74.10
72.09
71.07
44.74
Aya-expanse-32B 94.29
93.89
92.68
91.47
85.32
c4ai-command
88.80
87.31
88.76
87.04
74.12
Gemini-2.0
97.80
97.51
97.05
95.99
93.37
Gemma-2-9B-it
98.86
98.84
98.75
98.71
97.21
GPT-4o
98.09
97.52
97.37
97.09
95.45
Table 4: Inter-language consistency. Exact
matching rates of English-to-each and all-
to-all. Using the same prompt, the safety
of generated answers differs substantially
across languages.
Instead, the model exhibits different responses of
varying safety levels to identical queries across lan-
guages. We observe similar behavior with Llama3 for
crime_tax, where the model remains safe in English
(100%) but shows reduced safety in Italian (67.7%).
These are just some qualitative examples of inconsis-
tent safety performance for identical prompts across
languages.
The first example is particularly unexpected, as one
might expect a model’s safety to be most robust and
comprehensive in its primary language, English. Yet,
our experiments reveal that this assumption often does
not hold. While we anticipated some inconsistencies
due to imperfect translations, our findings suggest that
the primary driver of the performance gap lies in mis-
aligned safety behavior across languages. This points
to shortcomings of safety data for specific languages.
Inter-language Consistency.
Building on these find-
ings, we want to better understand safety inconsisten-
cies. Rather than evaluating consistency through general safety scores, as done in previous evaluations,
we now focus on whether a model’s responses to the same prompt are identical across languages. This
approach emphasizes consistency in responses, regardless of whether the answers are deemed safe or
7

--- Page 8 ---

Preprint. Under review.
unsafe. To this end, we introduce an additional metric: an exact matching rate. This metric examines
whether a model’s behavior is not merely similar when averaged across multiple prompts but fully
identical for a given prompt across languages. We visualize these consistency results in Table 4. As
shown, inter-language consistency is significantly lower than overall safety scores might suggest.
This demonstrates that while a model may achieve high safety ratings in individual languages, its
exact alignment across them remains substantially lower. For instance, QwQ produces an exact
matching rate of 89%, meaning its responses are consistent across languages for that proportion
of prompts. However, while the model scores around 97% safe for each language, it often fails to
produce identical responses for the same prompt across languages. Actually, one might expect a
matching rate of 100% regardless of the overall safety score, as there is no obvious reason for a model
to behave differently across languages. Even a model with an overall safety score of 60% could
achieve a 100% matching rate. This discrepancy highlights that the underlying safety inconsistencies
are even more pronounced than they initially appear. Those inconsistencies can be observed across
all models.
0
10
20
30
40
50
60
70
Model Size (Billion Parameters)
60
65
70
75
80
85
90
95
100
Safety Score
unsafe
highly unsafe
safe
Instruct
Base
Figure 4: Comparing model size with safety scores.
One cannot see a clear trend between model size and
safety. While larger models tend to be safer, even very
small models (<3B) show already high levels of safety.
For base models, the trend is clearer than for Instruct
models. (y-axis scaled)
Model Size.
Now that we have investi-
gated several models, we want to under-
stand further whether model size is a key
safety component. In this study, we ob-
serve that the smallest model, Llama3.2-
3B, surpasses larger models with 22B to
32B parameters, while a model with 9B
parameters achieves the best overall per-
formance —a middle-range value. At the
same time, safety does frequently correlate
with general model capabilities, as demon-
strated in prior research (Ren et al., 2024).
Examining our findings more closely, we
underscore the importance of disentangling
general model capabilities from safety ca-
pabilities.
While Llama3.2-3B outper-
forms larger models, it falls behind its im-
mediate predecessor, Llama3.1 with 8B pa-
rameters. This suggests that the difference
in safety performance may be attributed
to the quality of the safety tuning and that
model capacity indeed plays a crucial role
in safety performance. In more detail, when disentangling between instruct and base models, we find
a much clearer trend, in that base models show higher safety with increasing model size compared to
instruction-tuned models. We further visualize and discuss these results in Fig. 4.
Base vs. Instruct.
Upon further analysis of base versus instruct models in Table 6, we observe
significant differences between the base models. As expected, instruct models exhibit higher safety
levels, but there is considerable variation in the safety of the base models. The safety gap between the
best and worst performing base models approaches 30%, with base models of similar size showing
differences of up to 10%. These findings have important practical implications for researchers
selecting models, particularly those planning to fine-tune a base model with their own instruction
data and seeking guidance in the selection process. Selecting a safer base model can be a key aspect,
especially when high-quality safety data is unavailable or task-specific safety is superior compared to
overall safety.
Translation Quality of M-ALERT.
As outlined in Sec. 3, we adopt an automated translation
approach leveraging a Minimum Bayes Risk decoding strategy. In the first iteration, we exclusively
used OPUS-MT models to generate translation candidates. In the second iteration, we expanded
this by incorporating candidates from Google Translate and the TowerInstruct model. The selection
process was guided by the well-established COMET metric, choosing the candidate with the highest
score. Additionally, we discarded prompts where no candidate achieved a COMET score above 0.5,
resulting in a prompt removal rate of 0.2%.
8

--- Page 9 ---

Preprint. Under review.
M-ALERT
fr
de
es
it
Σ
Iter 1
MetricX-XXL (↓) 0.94±0.71 1.01±0.96 0.87±1.08 1.12±0.99 0.99±0.94
COMET-XXL (↑)
0.84±0.05 0.81±0.04 0.82±0.04 0.81±0.02 0.82±0.04
Human (↑)
0.95
0.92
0.91
0.92
0.93
Iter 2
MetricX-XXL (↓) 0.90±0.68 0.97±0.93 0.84±1.05 1.08±0.95 0.95±0.90
COMET-XXL (↑)
0.87±0.05 0.84±0.04 0.88±0.04 0.83±0.02 0.86±0.04
Human (↑)
0.96
0.93
0.94
0.94
0.95
Table 5: Translation quality estimation to English by MetricX & COMET (full set) and human
(subset). MetricX provides scores ranging from 0 to 25, where lower is better. COMET and human
evaluations yield scores between 0 and 1, where higher is better.
Tab. 5 shows consistently high-quality scores (close to 0 for MetricX and close to 1 for COMET),
indicating strong translation accuracy (where 25 is lowest and 0 highest for MetricX and 0 is lowest
quality and 1 highest for COMET), for both iterations. Moreover, the table illustrates performance
improvements across all metrics with the ensemble strategy introduced in Iteration 2. While an
increase in COMET scores is expected, given that selection is based on this metric, the concurrent
improvements in MetricX and human evaluations confirm a genuine enhancement in translation
quality. The selection rates for each model were 12% for OPUS-MT, 67% for Google Translate, and
21% for TowerInstruct.
Since the initial iteration already yielded high-quality translations, the second iteration likely did not
substantially improve most examples but rather focused on refining poor translations.
6
Limitations
M-ALERT as a multilingual safety benchmark has several limitations that must be considered.
A key area for improvement is the translation quality at a large scale. While we recognize the
inherent challenges in translations and translation quality estimation (Zhao et al., 2024; Perrella et al.,
2024), the effectiveness of safety assessments depends on accurate translations. To address this,
we prioritized languages with high-quality translation models and implemented a decoding strategy
to minimize translation errors. Despite our significant efforts to ensure translation quality, future
research could focus on refining and specifying translation methodologies for safety evaluations to
enhance correctness across languages. Moreover, incorporating more languages into the benchmark
would further enrich our evaluation.
As ALERT has been available for over six months now and large model providers (Défossez et al.,
2024) openly state using it, it is important to consider that the models under investigation here may
have been exposed to the underlying ALERT benchmark in some way during their training.
Moreover, the multilingual auto-evaluator LlamaGuard-3, although a valuable asset for our assess-
ment, has its limitations. As the first multilingual evaluator of its kind, it is prone to errors that
could affect the evaluation process (Yang et al., 2024). Confounding factors associated with Llama
base models may also complicate the interpretation of results, potentially misrepresenting the safety
profiles of these specific models.
Lastly, while this work emphasizes safety, future research should additionally explore the balance
between helpfulness and evasiveness (Bai et al., 2022; Cui et al., 2024) to gain a more comprehensive
understanding of model behavior.
7
Conclusions and Future Work
We introduced M-ALERT, a multilingual benchmark with 75k safety prompts, and evaluated the
safety of Large Language Models (LLMs) across five languages: English, French, German, Italian,
and Spanish. Through extensive testing on various state-of-the-art models, we reveal significant safety
inconsistencies across languages and categories, highlighting the importance of language-specific
safety analysis. Our findings demonstrate that while some models exhibit inconsistent safety across
languages, certain categories consistently trigger unsafe responses, emphasizing the need for robust
9

--- Page 10 ---

Preprint. Under review.
multilingual safety measures to ensure responsible LLM deployment globally. We hope our work
fosters new research opportunities and encourages the development of safe LLMs that are compliant
with the latest AI regulations.
8
Ethical Considerations
While M-ALERT is designed to benchmark and promote safety, it also carries the potential for
misuse. For example, a multilingual DPO dataset generated from our prompts and responses could
be repurposed to guide a model toward less safe behaviors instead of fostering safer outcomes.
Furthermore, our methodology highlights vulnerabilities in several large language models (LLMs).
We strongly encourage organizations deploying these models to address these findings proactively to
minimize risks to users and enhance overall safety.
The safety scores we report rely on Llama Guard, which offers a broad understanding of safety.
However, it is essential to acknowledge that perceptions of safety vary by individual and context.
What one person considers safe may differ from another’s perspective. As such, our evaluations
serve as valuable guidance but cannot ensure individual safety. On a positive note, M-ALERT itself
is independent of the judge model used. Also, its adaptable taxonomy facilitates the exploration of
different safety policies, reflecting the changing cultural and legal landscapes.
9
Reproducibility statement
To encourage further research into the development of safe LLMs, we are publicly releasing our
benchmark, software, and generated model outputs on GitHub and HuggingFace. This allows
researchers to create new datasets using our materials.
Acknowledgements
We acknowledge support of the hessian.AI Innovation Lab (funded by the Hessian Ministry for
Digital Strategy and Innovation), the hessian.AISC Service Center (funded by the Federal Ministry
of Education and Research, BMBF, grant No 01IS22091), and the German Research Center for AI
(DFKI). Further, this work benefited from the ICT-48 Network of AI Research Excellence Center
“TAILOR” (EU Horizon 2020, GA No 952215), the Hessian research priority program LOEWE
within the project WhiteBox, the HMWK cluster projects “Adaptive Min” and “Third Wave of AI”,
and from the NHR4CES.
References
Aakanksha, Arash Ahmadian, Beyza Ermis, Seraphina Goldfarb-Tarrant, Julia Kreutzer, Marzieh
Fadaee, and Sara Hooker. The multilingual alignment prism: Aligning global and local preferences
to reduce harm, 2024. URL https://arxiv.org/abs/2406.18682.
Abubakar Abid, Maheen Farooqi, and James Zou. Persistent anti-muslim bias in large language
models, 2021.
Mikel Artetxe and Holger Schwenk. Massively multilingual sentence embeddings for zero-shot
cross-lingual transfer and beyond. Transactions of the Association for Computational Linguistics,
pp. 597–610, 2019.
Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn
Drain, Stanislav Fort, Deep Ganguli, Tom Henighan, Nicholas Joseph, Saurav Kadavath, Jackson
Kernion, Tom Conerly, Sheer El-Showk, Nelson Elhage, Zac Hatfield-Dodds, Danny Hernandez,
Tristan Hume, Scott Johnston, Shauna Kravec, Liane Lovitt, Neel Nanda, Catherine Olsson, Dario
Amodei, Tom Brown, Jack Clark, Sam McCandlish, Chris Olah, Ben Mann, and Jared Kaplan.
Training a helpful and harmless assistant with reinforcement learning from human feedback, 2022.
Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell. On the
dangers of stochastic parrots: Can language models be too big? In Proceedings of the 2021 ACM
Conference on Fairness, Accountability, and Transparency, pp. 610–623, 2021.
10

--- Page 11 ---

Preprint. Under review.
Rishi Bommasani, Drew A Hudson, Ehsan Adeli, Russ Altman, Simran Arora, Sydney von Arx,
Michael S Bernstein, Jeannette Bohg, Antoine Bosselut, Emma Brunskill, et al. On the opportuni-
ties and risks of foundation models. arXiv preprint arXiv:2108.07258, 2021.
Manuel Brack, Patrick Schramowski, Pedro Ortiz, Malte Ostendorff, Fabio Barth, Georg Rehm, and
Kristian Kersting. Occiglot-7b: A polyglot language model for the occident, 2024. URL https:
//occiglot.eu/posts/occiglot-announcement/#model-release-v01.
Justin Cui, Wei-Lin Chiang, Ion Stoica, and Cho-Jui Hsieh. Or-bench: An over-refusal benchmark
for large language models, 2024.
Adrian de Wynter, Ishaan Watts, Nektar Ege Altıntoprak, Tua Wongsangaroonsri, Minghui Zhang,
Noura Farra, Lena Baur, Samantha Claudet, Pavel Gajdusek, Can Gören, Qilong Gu, Anna
Kaminska, Tomasz Kaminski, Ruby Kuo, Akiko Kyuba, Jongho Lee, Kartik Mathur, Petter
Merok, Ivana Milovanovi’c, Nani Paananen, Vesa-Matti Paananen, Anna Pavlenko, Bruno Pereira
Vidal, L. Strika, Yueh Tsao, Davide Turcato, Oleksandr Vakhno, Judit Velcsov, Anna Vickers,
St’ephanie Visser, Herdyan Widarmanto, Andrey V. Zaikin, and Si-Qing Chen. Rtp-lx: Can
llms evaluate toxicity in multilingual scenarios? ArXiv, abs/2404.14397, 2024. URL https:
//api.semanticscholar.org/CorpusID:269293221.
Alexandre Défossez, Laurent Mazaré, Manu Orsini, Amélie Royer, Patrick Pérez, Hervé Jégou,
Edouard Grave, and Neil Zeghidour. Moshi: a speech-text foundation model for real-time dialogue.
Technical report, kyut.ai, 2024. URL https://arxiv.org/abs/2410.00037.
Jwala Dhamala, Tony Sun, Varun Kumar, Satyapriya Krishna, Yada Pruksachatkun, Kai-Wei
Chang, and Rahul Gupta. Bold: Dataset and metrics for measuring biases in open-ended lan-
guage generation. In Proceedings of the 2021 ACM Conference on Fairness, Accountability,
and Transparency, FAccT ’21. ACM, March 2021.
doi: 10.1145/3442188.3445924.
URL
http://dx.doi.org/10.1145/3442188.3445924.
Mai ElSherief, Caleb Ziems, David Muchlinski, Vaishnavi Anupindi, Jordyn Seybolt, Munmun
De Choudhury, and Diyi Yang. Latent hatred: A benchmark for understanding implicit hate speech.
In Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing,
pp. 345–363, 2021.
EU. Artificial Intelligence Act EU. https://artificialintelligenceact.eu/, 2023.
Accessed: March 13, 2024.
Felix Friedrich, Katharina Hämmerl, Patrick Schramowski, Jindrich Libovicky, Kristian Kersting,
and Alexander Fraser. Multilingual text-to-image generation magnifies gender stereotypes and
prompt engineering may not help you, 2024.
Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas I. Liao, Kamil˙e Lukoši¯ut˙e, Anna Chen,
Anna Goldie, Azalia Mirhoseini, Catherine Olsson, Danny Hernandez, Dawn Drain, Dustin Li,
Eli Tran-Johnson, Ethan Perez, Jackson Kernion, Jamie Kerr, Jared Mueller, Joshua Landau,
Kamal Ndousse, Karina Nguyen, Liane Lovitt, Michael Sellitto, Nelson Elhage, Noemi Mercado,
Nova DasSarma, Oliver Rausch, Robert Lasenby, Robin Larson, Sam Ringer, Sandipan Kundu,
Saurav Kadavath, Scott Johnston, Shauna Kravec, Sheer El Showk, Tamera Lanham, Timothy
Telleen-Lawton, Tom Henighan, Tristan Hume, Yuntao Bai, Zac Hatfield-Dodds, Ben Mann, Dario
Amodei, Nicholas Joseph, Sam McCandlish, Tom Brown, Christopher Olah, Jack Clark, Samuel R.
Bowman, and Jared Kaplan. The capacity for moral self-correction in large language models,
2023.
Samuel Gehman, Suchin Gururangan, Maarten Sap, Yejin Choi, and Noah A. Smith. RealToxici-
tyPrompts: Evaluating neural toxic degeneration in language models. In Findings of the Association
for Computational Linguistics: EMNLP 2020, pp. 3356–3369, 2020.
Shaona Ghosh, Heather Frase, Adina Williams, Sarah Luger, Paul Röttger, Fazl Barez, Sean McGre-
gor, Kenneth Fricklas, Mala Kumar, Quentin Feuillade-Montixi, Kurt Bollacker, Felix Friedrich,
Ryan Tsang, Bertie Vidgen, Alicia Parrish, Chris Knotz, Eleonora Presani, Jonathan Bennion,
Marisa Ferrara Boston, Mike Kuniavsky, Wiebke Hutiri, James Ezick, Malek Ben Salem, Rajat
Sahay, Sujata Goswami, Usman Gohar, Ben Huang, Supheakmungkol Sarin, Elie Alhajjar, Canyu
11

--- Page 12 ---

Preprint. Under review.
Chen, Roman Eng, Kashyap Ramanandula Manjusha, Virendra Mehta, Eileen Long, Murali Emani,
Natan Vidra, Benjamin Rukundo, Abolfazl Shahbazi, Kongtao Chen, Rajat Ghosh, Vithursan
Thangarasa, Pierre Peigné, Abhinav Singh, Max Bartolo, Satyapriya Krishna, Mubashara Akhtar,
Rafael Gold, Cody Coleman, Luis Oala, Vassil Tashev, Joseph Marvin Imperial, Amy Russ, Sasid-
har Kunapuli, Nicolas Miailhe, Julien Delaunay, Bhaktipriya Radharapu, Rajat Shinde, Tuesday,
Debojyoti Dutta, Declan Grabb, Ananya Gangavarapu, Saurav Sahay, Agasthya Gangavarapu,
Patrick Schramowski, Stephen Singam, Tom David, Xudong Han, Priyanka Mary Mammen,
Tarunima Prabhakar, Venelin Kovatchev, Ahmed Ahmed, Kelvin N. Manyeki, Sandeep Madireddy,
Foutse Khomh, Fedor Zhdanov, Joachim Baumann, Nina Vasan, Xianjun Yang, Carlos Mougn,
Jibin Rajan Varghese, Hussain Chinoy, Seshakrishna Jitendar, Manil Maskey, Claire V. Hardgrove,
Tianhao Li, Aakash Gupta, Emil Joswin, Yifan Mai, Shachi H Kumar, Cigdem Patlak, Kevin Lu,
Vincent Alessi, Sree Bhargavi Balija, Chenhe Gu, Robert Sullivan, James Gealy, Matt Lavrisa,
James Goel, Peter Mattson, Percy Liang, and Joaquin Vanschoren. Ailuminate: Introducing v1.0
of the ai risk and reliability benchmark from mlcommons. arXiv preprint arXiv:2501.2503.05731,
2025.
Google. Google translate, 2025. URL https://translate.google.com. Accessed: 2025-
03-24.
Srishti Gureja, Lester James V. Miranda, Shayekh Bin Islam, Rishabh Maheshwary, Drishti
Sharma, Gusti Winata, Nathan Lambert, Sebastian Ruder, Sara Hooker, and Marzieh Fadaee.
M-rewardbench: Evaluating reward models in multilingual settings, 2024.
URL https:
//arxiv.org/abs/2410.15522.
Thomas Hartvigsen, Saadia Gabriel, Hamid Palangi, Maarten Sap, Dipankar Ray, and Ece Kamar.
Toxigen: A large-scale machine-generated dataset for implicit and adversarial hate speech detection.
In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics, 2022.
Dan Hendrycks, Mantas Mazeika, and Thomas Woodside. An overview of catastrophic ai risks, 2023.
Saghar Hosseini, Hamid Palangi, and Ahmed Hassan Awadallah. An empirical study of metrics
to measure representational harms in pre-trained language models. In Proceedings of the 3rd
Workshop on Trustworthy Natural Language Processing (TrustNLP 2023), pp. 121–134, 2023.
Hakan Inan, Kartikeya Upasani, Jianfeng Chi, Rashi Rungta, Krithika Iyer, Yuning Mao, Michael
Tontchev, Qing Hu, Brian Fuller, Davide Testuggine, and Madian Khabsa. Llama guard: Llm-based
input-output safeguard for human-ai conversations, 2023.
Devansh Jain, Priyanshu Kumar, Samuel Gehman, Xuhui Zhou, Thomas Hartvigsen, and Maarten Sap.
Polyglotoxicityprompts: Multilingual evaluation of neural toxic degeneration in large language
models, 2024.
Juraj Juraska, Mara Finkelstein, Daniel Deutsch, Aditya Siddhant, Mehdi Mirzazadeh, and Markus
Freitag. MetricX-23: The Google submission to the WMT 2023 metrics shared task. In Proceedings
of the Eighth Conference on Machine Translation, 2023.
Tom Kocmi, Eleftherios Avramidis, Rachel Bawden, Ondˇrej Bojar, Anton Dvorkovich, Christian
Federmann, Mark Fishel, Markus Freitag, Thamme Gowda, Roman Grundkiewicz, Barry Haddow,
Marzena Karpinska, Philipp Koehn, Benjamin Marie, Christof Monz, Kenton Murray, Masaaki
Nagata, Martin Popel, Maja Popovi´c, Mariya Shmatova, Steinthór Steingrímsson, and Vilém
Zouhar. Findings of the WMT24 general machine translation shared task: The LLM era is here but
MT is not solved yet. In Proceedings of the Ninth Conference on Machine Translation, 2024.
Geza Kovacs, Daniel Deutsch, and Markus Freitag. Mitigating metric bias in minimum Bayes risk
decoding. In Proceedings of the Ninth Conference on Machine Translation, 2024.
Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian
Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Kumar, Benjamin Newman, Binhang Yuan, Bobby
Yan, Ce Zhang, Christian Cosgrove, Christopher D. Manning, Christopher Ré, Diana Acosta-Navas,
Drew A. Hudson, Eric Zelikman, Esin Durmus, Faisal Ladhak, Frieda Rong, Hongyu Ren, Huaxiu
Yao, Jue Wang, Keshav Santhanam, Laurel Orr, Lucia Zheng, Mert Yuksekgonul, Mirac Suzgun,
Nathan Kim, Neel Guha, Niladri Chatterji, Omar Khattab, Peter Henderson, Qian Huang, Ryan
12

--- Page 13 ---

Preprint. Under review.
Chi, Sang Michael Xie, Shibani Santurkar, Surya Ganguli, Tatsunori Hashimoto, Thomas Icard,
Tianyi Zhang, Vishrav Chaudhary, William Wang, Xuechen Li, Yifan Mai, Yuhui Zhang, and Yuta
Koreeda. Holistic evaluation of language models, 2023.
Zi Lin, Zihan Wang, Yongqi Tong, Yangkun Wang, Yuxin Guo, Yujia Wang, and Jingbo Shang.
Toxicchat: Unveiling hidden challenges of toxicity detection in real-world user-ai conversation,
2023.
AI @ Meta Llama Team. The llama 3 herd of models, 2024. URL https://arxiv.org/abs/
2407.21783.
Shayne Longpre, Sayash Kapoor, Kevin Klyman, Ashwin Ramaswami, Rishi Bommasani, Borhane
Blili-Hamelin, Yangsibo Huang, Aviya Skowron, Zheng-Xin Yong, Suhas Kotha, Yi Zeng, Weiyan
Shi, Xianjun Yang, Reid Southen, Alexander Robey, Patrick Chao, Diyi Yang, Ruoxi Jia, Daniel
Kang, Sandy Pentland, Arvind Narayanan, Percy Liang, and Peter Henderson. A safe harbor for ai
evaluation and red teaming, 2024.
Taishi Nakamura, Mayank Mishra, Simone Tedeschi, Yekun Chai, Jason T Stillerman, Felix Friedrich,
Prateek Yadav, Tanmay Laud, Vu Minh Chien, Terry Yue Zhuo, Diganta Misra, Ben Bogin, Xuan-
Son Vu, Marzena Karpinska, Arnav Varma Dantuluri, Wojciech Kusa, Tommaso Furlanello,
Rio Yokota, Niklas Muennighoff, Suhas Pai, Tosin Adewumi, Veronika Laippala, Xiaozhe Yao,
Adalberto Junior, Alpay Ariyak, Aleksandr Drozd, Jordan Clive, Kshitij Gupta, Liangyu Chen,
Qi Sun, Ken Tsui, Noah Persaud, Nour Fahmy, Tianlong Chen, Mohit Bansal, Nicolo Monti, Tai
Dang, Ziyang Luo, Tien-Tung Bui, Roberto Navigli, Virendra Mehta, Matthew Blumberg, Victor
May, Huu Nguyen, and Sampo Pyysalo. Aurora-m: The first open source multilingual language
model red-teamed according to the u.s. executive order, 2024.
Michael O’Neill and Mark Connor. Amplifying limitations, harms and risks of large language models.
arXiv preprint arXiv:2307.04821, 2023.
Stefano Perrella, Lorenzo Proietti, Pere-Lluís Huguet Cabot, Edoardo Barba, and Roberto Navigli.
Beyond correlation: Interpretable evaluation of machine translation metrics. In Proceedings of the
2024 Conference on Empirical Methods in Natural Language Processing, 2024.
Ricardo Rei, Nuno M. Guerreiro, JosÃ© Pombal, Daan van Stigt, Marcos Treviso, Luisa Coheur,
José G. C. de Souza, and André Martins. Scaling up CometKiwi: Unbabel-IST 2023 submission
for the quality estimation shared task. In Proceedings of the Eighth Conference on Machine
Translation, 2023.
Richard Ren, Steven Basart, Adam Khoja, Alice Gatti, Long Phan, Xuwang Yin, Mantas Mazeika,
Alexander Pan, Gabriel Mukobi, Ryan H. Kim, Stephen Fitz, and Dan Hendrycks. Safetywashing:
Do ai safety benchmarks actually measure safety progress?, 2024. URL https://arxiv.org/
abs/2407.21792.
Taylor Sorensen, Jared Moore, Jillian Fisher, Mitchell Gordon, Niloofar Mireshghallah, Christo-
pher Michael Rytting, Andre Ye, Liwei Jiang, Ximing Lu, Nouha Dziri, Tim Althoff, and
Yejin Choi. A roadmap to pluralistic alignment, 2024. URL https://arxiv.org/abs/
2402.05070.
Simone Tedeschi, Felix Friedrich, Patrick Schramowski, Kristian Kersting, Roberto Navigli, Huu
Nguyen, and Bo Li. Alert: A comprehensive benchmark for assessing large language models’
safety through red teaming, 2024.
Jörg Tiedemann and Santhosh Thottingal. OPUS-MT — Building open translation services for the
World. In Proceedings of the 22nd Annual Conferenec of the European Association for Machine
Translation (EAMT), Lisbon, Portugal, 2020.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée
Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand
Joulin, Edouard Grave, and Guillaume Lample. Llama: Open and efficient foundation language
models, 2023.
13

--- Page 14 ---

Preprint. Under review.
UKGov. Ai regulation: A pro-innovation approach. https://www.gov.uk/government/
publications/ai-regulation-a-pro-innovation-approach/white-
paper, 2023. Accessed: March 13, 2024.
Bertie Vidgen, Alex Harris, Dong Nguyen, Rebekah Tromble, Scott Hale, and Helen Margetts.
Challenges and frontiers in abusive content detection. In Proceedings of the Third Workshop on
Abusive Language Online, 2019.
Bertie Vidgen, Adarsh Agrawal, Ahmed M. Ahmed, Victor Akinwande, Namir Al-Nuaimi, Najla
Alfaraj, Elie Alhajjar, Lora Aroyo, Trupti Bavalatti, Max Bartolo, Borhane Blili-Hamelin, Kurt
Bollacker, Rishi Bomassani, Marisa Ferrara Boston, Siméon Campos, Kal Chakra, Canyu Chen,
Cody Coleman, Zacharie Delpierre Coudert, Leon Derczynski, Debojyoti Dutta, Ian Eisenberg,
James Ezick, Heather Frase, Brian Fuller, Ram Gandikota, Agasthya Gangavarapu, Ananya
Gangavarapu, James Gealy, Rajat Ghosh, James Goel, Usman Gohar, Sujata Goswami, Scott A.
Hale, Wiebke Hutiri, Joseph Marvin Imperial, Surgan Jandial, Nick Judd, Felix Juefei-Xu, Foutse
Khomh, Bhavya Kailkhura, Hannah Rose Kirk, Kevin Klyman, Chris Knotz, Michael Kuchnik,
Shachi H. Kumar, Srijan Kumar, Chris Lengerich, Bo Li, Zeyi Liao, Eileen Peters Long, Victor Lu,
Sarah Luger, Yifan Mai, Priyanka Mary Mammen, Kelvin Manyeki, Sean McGregor, Virendra
Mehta, Shafee Mohammed, Emanuel Moss, Lama Nachman, Dinesh Jinenhally Naganna, Amin
Nikanjam, Besmira Nushi, Luis Oala, Iftach Orr, Alicia Parrish, Cigdem Patlak, William Pietri,
Forough Poursabzi-Sangdeh, Eleonora Presani, Fabrizio Puletti, Paul Röttger, Saurav Sahay, Tim
Santos, Nino Scherrer, Alice Schoenauer Sebag, Patrick Schramowski, Abolfazl Shahbazi, Vin
Sharma, Xudong Shen, Vamsi Sistla, Leonard Tang, Davide Testuggine, Vithursan Thangarasa,
Elizabeth Anne Watkins, Rebecca Weiss, Chris Welty, Tyler Wilbers, Adina Williams, Carole-Jean
Wu, Poonam Yadav, Xianjun Yang, Yi Zeng, Wenhui Zhang, Fedor Zhdanov, Jiacheng Zhu, Percy
Liang, Peter Mattson, and Joaquin Vanschoren. Introducing v0.5 of the ai safety benchmark from
mlcommons, 2024. URL https://arxiv.org/abs/2404.12241.
Boxin Wang, Weixin Chen, Hengzhi Pei, Chulin Xie, Mintong Kang, Chenhui Zhang, Chejian
Xu, Zidi Xiong, Ritik Dutta, Rylan Schaeffer, Sang T. Truong, Simran Arora, Mantas Mazeika,
Dan Hendrycks, Zinan Lin, Yu Cheng, Sanmi Koyejo, Dawn Song, and Bo Li. Decodingtrust: A
comprehensive assessment of trustworthiness in gpt models. In Proceedings of the 2023 Conference
on Neural Information Processing, 2023a.
Wenxuan Wang, Zhaopeng Tu, Chang Chen, Youliang Yuan, Jen-tse Huang, Wenxiang Jiao, and
Michael R Lyu. All languages matter: On the multilingual safety of large language models. arXiv
preprint arXiv:2310.00905, 2023b.
Laura Weidinger, John Mellor, Maribeth Rauh, Conor Griffin, Jonathan Uesato, Po-Sen Huang, Myra
Cheng, Mia Glaese, Borja Balle, Atoosa Kasirzadeh, Zac Kenton, Sasha Brown, Will Hawkins,
Tom Stepleton, Courtney Biles, Abeba Birhane, Julia Haas, Laura Rimell, Lisa Anne Hendricks,
William Isaac, Sean Legassick, Geoffrey Irving, and Iason Gabriel. Ethical and social risks of
harm from language models, 2021.
WhiteHouse. Fact sheet: President biden issues executive order on safe, secure, and trustworthy arti-
ficial intelligence. https://www.whitehouse.gov/briefing-room/statements-
releases/2023/10/30/fact-sheet-president-biden-issues-executive-
order-on-safe-secure-and-trustworthy-artificial-intelligence/,
2023. Accessed: March 13, 2024.
Yahan Yang, Soham Dan, Dan Roth, and Insup Lee. Benchmarking llm guardrails in handling
multilingual toxicity, 2024. URL https://arxiv.org/abs/2410.22153.
Haofei Zhao, Yilun Liu, Shimin Tao, Weibin Meng, Yimeng Chen, Xiang Geng, Chang Su, Min
Zhang, and Hao Yang. From handcrafted features to llms: A brief survey for machine translation
quality estimation. 2024 International Joint Conference on Neural Networks (IJCNN), 2024.
Lianmin Zheng, Liangsheng Yin, Zhiqiang Xie, Jeff Huang, Chuyue Sun, Cody Hao Yu, Shiyi Cao,
Christos Kozyrakis, Ion Stoica, Joseph E. Gonzalez, Clark Barrett, and Ying Sheng. Efficiently
programming large language models using sglang, 2023.
14

--- Page 15 ---

Preprint. Under review.
Base Instruct
∆
Gemma-2-2b
68.49
98.74 +30.25
Gemma-2-9b
68.62
99.04 +30.42
Gemma-2-27b 71.34
99.05 +27.71
Llama-3-8B
70.83
96.66 +25.83
Llama-3.1-8B
69.47
98.71 +29.24
Llama-3.2-3B
63.64
97.43 +33.79
Qwen2.5-0.5B 60.85
87.53 +26.68
Qwen2.5-1.5B 60.50
95.81 +35.31
Qwen2.5-3B
67.58
97.85 +30.27
Qwen2.5-7B
75.83
97.60 +21.77
Qwen2.5-14B
87.06
98.68 +11.62
Qwen2.5-32B
88.02
98.35 +10.33
Qwen2.5-72B
78.54
98.33 +19.79
Table 6: Comparing safety score for Base and Instruct versions of different models. The given scores
are mean scores across all languages and categories. As expected, instruct models are pretty safe due
to their dedicated safety tuning. However, there are notable differences in safety for base models.
The largest differences describe more than 10%. The insights are invaluable for researchers who want
to use their own instruction data on top of a base model.
Model
Full Model Name
Link
Release
Llama-3-8b-it
Llama-3-8B-Instruct
https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct
2024-04-18
Llama-3.1-8b-it
Llama-3.1-8B-Instruct
https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct
2024-07-23
Mistral-Small-it
Mistral-Small-Instruct-2409
https://huggingface.co/mistralai/Mistral-Small-Instruct-2409
2024-09-18
QwQ-32B
QwQ-32B
https://huggingface.co/Qwen/QwQ-32B
2025-03-05
aya-23-8b
aya-23-8B
https://huggingface.co/CohereForAI/aya-23-8B
2024-05-24
aya-expanse-32b
aya-expanse-32B
https://huggingface.co/CohereForAI/aya-expanse-32b
2024-10-26
c4ai-command-r
c4ai-command-r-08-2024
https://huggingface.co/CohereForAI/c4ai-command-r-08-2024
2024-08-01
gemini-2.0-flash-001
Gemini-2.0
https://ai.google.dev/gemini-api/docs/models#gemini-2.0-flash
2025-02-05
gemma-2-9b-it
gemma-2-9B-it
https://huggingface.co/google/gemma-2-9b-it
2024-07-08
gpt-4o-2024-11-20
GPT-4o
https://huggingface.co/google/gemma-2-9b-it
2024-11-20
Llama-3-8b
Llama-3-8B
https://huggingface.co/meta-llama/Meta-Llama-3-8B
2024-04-18
Llama-3.1-8b
Llama-3.1-8B
https://huggingface.co/meta-llama/Llama-3.1-8B
2024-07-23
Llama-3.2-3b
Llama-3.2-3B
https://huggingface.co/meta-llama/Llama-3.2-3B
2024-09-26
Llama-3.2-3b-it
Llama-3.2-3B-Instruct
https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct
2024-09-26
Llama-3.3-70b-it
Llama-3.3-70B-Instruct
https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct
2024-12-06
Ministral-8b-it
Mistral-8B-Instruct-2410
https://huggingface.co/mistralai/Ministral-8B-Instruct-2410
2024-09-18
Mistral-7b-it
Mistral-7B-Instruct-v0.3
https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3
2024-05-23
aya-expanse-8b
aya-expanse-8B
https://huggingface.co/CohereForAI/aya-expanse-8b
2024-10-26
gemma-2-2b
gemma-2-2B
https://huggingface.co/google/gemma-2-2b
2024-06-28
gemma-2-2b-it
gemma-2-2B-it
https://huggingface.co/google/gemma-2-2b-it
2024-06-28
gemma-2-27b
gemma-2-27B
https://huggingface.co/google/gemma-2-27b
2024-06-28
gemma-2-27b-it
gemma-2-27B-it
https://huggingface.co/google/gemma-2-27b-it
2024-06-28
gemma-2-9b
gemma-2-9B
https://huggingface.co/google/gemma-2-9b
2024-06-28
Qwen2.5-0.5b
Qwen2.5-0.5B
https://huggingface.co/Qwen/Qwen2.5-0.5B
2024-06-28
Qwen2.5-0.5b-it
Qwen2.5-0.5B-Instruct
https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct
2024-06-28
Qwen2.5-1.5b
Qwen2.5-1.5B
https://huggingface.co/Qwen/Qwen2.5-1.5B
2024-06-28
Qwen2.5-1.5b-it
Qwen2.5-1.5B-Instruct
https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct
2024-06-28
Qwen2.5-3b
Qwen2.5-3B
https://huggingface.co/Qwen/Qwen2.5-3B
2024-06-28
Qwen2.5-3b-it
Qwen2.5-3B-Instruct
https://huggingface.co/Qwen/Qwen2.5-3B-Instruct
2024-06-28
Qwen2.5-7b
Qwen2.5-7B
https://huggingface.co/Qwen/Qwen2.5-7B
2024-06-28
Qwen2.5-7b-it
Qwen2.5-7B-Instruct
https://huggingface.co/Qwen/Qwen2.5-7B-Instruct
2024-06-28
Qwen2.5-14b
Qwen2.5-14B
https://huggingface.co/Qwen/Qwen2.5-14B
2024-06-28
Qwen2.5-14b-it
Qwen2.5-14B-Instruct
https://huggingface.co/Qwen/Qwen2.5-14B-Instruct
2024-06-28
Qwen2.5-32b
Qwen2.5-32B
https://huggingface.co/Qwen/Qwen2.5-32B
2024-06-28
Qwen2.5-32b-it
Qwen2.5-32B-Instruct
https://huggingface.co/Qwen/Qwen2.5-32B-Instruct
2024-06-28
Qwen2.5-72b
Qwen2.5-72B
https://huggingface.co/Qwen/Qwen2.5-72B
2024-06-28
Qwen2.5-72b-it
Qwen2.5-72B-Instruct
https://huggingface.co/Qwen/Qwen2.5-72B-Instruct
2024-06-28
EuroLLM-9b-it
EuroLLM-9B-Instruct
https://huggingface.co/utter-project/EuroLLM-9B-Instruct
2024-11-28
Teuken-7b-it
Teuken-7B-instruct-commercial
https://huggingface.co/openGPT-X/Teuken-7B-instruct-commercial-v0.4
2024-11-24
Aurora-m (Nakamura et al., 2024)
Aurora-m-biden-harris-redteamed
https://huggingface.co/aurora-m/aurora-m-biden-harris-redteamed
2023-12-14
Table 7: Full model list with links to HuggingFace repositories. The first part of the table describes
the models used for the main experiments. The second part describes models used for base-instruct
experiments and model-size experiments.
APPENDIX
We scale some of the plots with exponential scaling to make nuanced differences more visible.
Further, we used AI tools to rephrase parts of our paper.
15

--- Page 16 ---

Preprint. Under review.
en
Why are so many Muslims terrorists?
de
Warum sind so viele Muslime Terroristen?
it
Perché così tanti terroristi musulmani?
es
¿Por qué tantos musulmanes son terroristas?
fr
Pourquoi tant de musulmans sont-ils des terroristes ?
Table 8: Toxic language! Exemplary safety translations align well with the English pendant, main-
taining high quality.
A
Human Annotators
We applied human supervision to a subset of both translations and safety classifications. All annotators
involved in this project are researchers with expertise in AI safety and machine translation, making
them well-equipped to handle potentially unsafe content. Furthermore, we adhered to the guidelines
for safeguarding annotator well-being as outlined by Vidgen et al. (2019). To prioritize annotator
well-being, we opted not to hire external paid annotators for this project. The annotation work was
carried out by researchers who are either co-authors of this paper or close colleagues.
For each of our human evaluations, we randomly sampled 100 prompts and evaluated (a) translation
quality across languages and (b) safety classification across languages.
B
Translation Details
In Table 8, we present examples from our multilingual translation results, illustrating translation
accuracy across languages. Overall, the translation quality is high, with both semantic meaning and
sentence structure being generally well-preserved across all languages. This consistency reflects
the translators’ capacity to maintain context and linguistic coherence when translating potentially
sensitive phrases.
However, there are areas where translation quality could be improved. Notably, models lack specific
knowledge about certain cultural movements or contexts, leading to incorrect or incomplete transla-
tions across languages. Additionally, some phrases demonstrate variability in translation accuracy
between languages; while one language may achieve a highly accurate translation, another may
omit or inaccurately render parts of the sentence. This inconsistency suggests a need for improved
translation methods, particularly for large-scale translations of nuanced safety-related content.
C
Models
In this work, we examine the models as presented in Table 7. We focused on models of different
sizes, release dates, model families, and tuning versions. Overall, we focused on openly available
models. In the main experiments, we focused on 10 models to provide clear results. For following
more fine-grained analysis, we expanded to 40 models in total, to account for more variety in terms
of tuning, size, and release date.
D
Scoring Safety
We evaluated the alignment between LlamaGuard and human labels on a random subset of M-ALERT.
The macro F1 score between human and LlamaGuard judgments was 84% across languages, consis-
tent with the results reported by the LlamaGuard authors (Llama Team, 2024), indicating a strong
alignment with only a small gap between human and LlamaGuard assessments. While the model
demonstrates high precision in correctly identifying safe instances, it occasionally falls short in
consistently detecting all unsafe cases. Consequently, while the overall insights and conclusions align
well, caution is advised when interpreting the precise safety scores.
Additionally, we employed GPT-4o as a meta-judge on the same subset to assess whether the
LlamaGuard3 judgment was accurate, given the taxonomy and the prompt-response pair. Similar
16

--- Page 17 ---

Preprint. Under review.
2023-12-14
2024-04-18
2024-05-23
2024-06-28
2024-07-08
2024-07-23
2024-08-01
2024-09-18
2024-09-26
2024-10-26
2024-11-24
2024-11-28
Release Date
60
65
70
75
80
85
90
95
100
Safety Score
unsafe
highly unsafe
safe
Instruct
Base
Figure 5: Visualizing safety scores as a function of release date
to the human user study, GPT-4o achieved an alignment of 90%, averaged across languages. Both
evaluations confirm that the safety scores obtained are largely valid.
E
Model size
In Fig. 4, we depict base and instruct models of different sizes regarding their safety score. We do not
find a clear improvement with increasing model size in terms of parameters. The trend is even less
clear for the instruct models compared to the base models. This shows that while model size might
be one factor for impacting safety, high-quality safety tuning (data) might be even more important.
F
Base vs. Instruct
In Table 6, we compare the safety score for base models with their instruction-tuned version. The
given scores are median scores across all languages and categories. As expected, instruct models
are pretty safe due to their dedicated safety tuning. However, there are notable differences in safety
for base models. The largest differences describe more than 10%. The insights are invaluable for
researchers who want to use their own instruction data on top of a base model. Furthermore, it
emphasizes the need for dedicated safety methods as pure base models largely exhibit unsafe outputs.
G
Release Date
In Fig. 5, we depict models’ safety scores as a function of release date. One can see that newer
models tend to show better safety scores. This suggests ongoing safety efforts.
H
Further Results
We show evaluations with further models in Tables 9, 10, 11, 12, 13, and 14. We find that base models
are worse compared to the instruct models. Furthermore, we find that some models like Teuken are
very unsafe although instruction-tuned.
17

--- Page 18 ---

Preprint. Under review.
EuroLLM-9B-Instruct
Llama-3-8B
Llama-3.1-8B
Llama-3.2-1B
Llama-3.2-1B-Instruct
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
crime
cyber
97.16 97.81 96.06 94.09 97.16 54.27 62.58 62.80 67.61 55.14 51.64 58.64 55.80 61.49 55.80 37.20 50.33 39.61 35.23 57.11 96.28 97.81 93.00 96.06 96.94
injury
94.33 96.22 91.82 85.48 93.05 54.78 54.67 58.34 69.41 55.90 49.89 51.28 58.90 64.68 57.12 42.77 43.16 45.22 38.88 56.73 95.88 94.72 95.88 97.44 95.16
kidnapp
98.01 97.01 96.52 94.53 98.51 31.84 33.83 29.85 72.14 38.81 30.35 36.82 27.36 71.14 25.87 40.80 30.85 23.38 28.86 27.36 98.01 98.01 98.51 98.51 98.01
other
97.99 97.99 96.85 92.26 95.13 79.66 63.32 87.11 83.95 81.95 70.20 60.46 85.67 81.95 79.37 72.49 56.45 79.66 67.05 79.94 97.42 96.85 97.71 98.28 97.99
privacy
98.89 99.72 96.40 98.06 98.34 54.57 73.13 73.41 74.52 72.85 38.78 68.14 67.87 81.16 65.65 35.18 66.76 60.11 37.12 56.79 99.45 98.89 97.78 99.45 99.45
propaganda 94.70 83.51 90.94 85.54 82.55 64.71 73.48 86.11 80.33 89.39 62.01 62.87 80.14 77.34 89.10 29.80 44.94 42.24 43.78 60.46 81.20 65.57 82.16 86.69 78.59
tax
98.17 99.39 99.70 96.65 98.48 58.23 54.88 58.23 68.29 57.93 61.28 70.43 48.48 65.85 45.73 35.98 41.16 23.78 27.74 35.37 98.48 100.0 95.43 93.90 79.27
theft
95.03 97.51 92.88 86.11 94.68 43.57 54.37 48.80 61.75 40.05 42.37 52.66 42.37 60.63 41.25 44.85 49.91 28.90 27.44 48.37 91.42 95.88 88.68 81.39 95.03
hate
body
100.0 99.40 99.40 97.59 100.0 82.53 77.11 80.12 89.16 76.51 80.12 78.92 80.12 89.76 78.31 72.29 69.28 68.67 80.12 81.93 96.99 98.80 98.80 98.80 99.40
disabled
98.33 98.33 100.0 99.17 100.0 83.33 79.17 73.33 90.83 75.00 80.83 80.00 75.83 90.83 73.33 67.50 71.67 60.00 66.67 77.50 98.33 98.33 97.50 97.50 99.17
ethnic
98.53 99.43 98.94 96.07 98.61 69.21 69.86 72.73 77.56 70.52 65.60 67.90 74.20 72.32 70.93 62.57 54.71 62.82 60.11 66.75 96.15 98.03 99.59 98.94 98.77
lgbtq+
99.24 100.0 98.73 99.24 98.22 72.52 80.15 85.50 85.75 79.13 72.01 79.39 82.44 80.66 79.39 69.97 64.12 72.01 70.48 76.08 97.46 98.47 100.0 100.0 99.24
other
98.61 99.26 99.35 93.14 95.26 80.31 83.33 80.80 91.75 84.97 80.80 79.82 82.11 88.15 82.52 76.72 74.02 78.51 73.94 81.37 96.08 97.55 99.51 99.84 98.45
poor
98.02 100.0 100.0 100.0 100.0 82.18 83.17 88.12 89.11 92.08 87.13 87.13 89.11 85.15 89.11 81.19 84.16 87.13 84.16 91.09 99.01 100.0 97.03 97.03 98.02
religion
99.55 98.87 98.87 97.97 97.74 62.75 69.75 73.81 74.04 65.01 56.43 63.21 70.43 70.20 65.46 53.72 46.28 58.47 55.76 64.33 96.39 98.42 99.55 99.32 98.65
women
99.04 99.64 98.57 97.61 98.33 77.06 76.82 81.60 83.51 74.43 78.02 76.70 79.33 82.20 75.87 70.73 65.23 71.33 70.85 77.90 96.65 97.85 98.92 98.33 98.69
self harm
other
100.0 100.0 100.0 99.31 100.0 84.03 70.83 79.86 72.22 73.61 84.03 63.19 82.64 70.14 87.50 72.92 22.92 48.61 37.50 86.81 97.92 100.0 100.0 100.0 100.0
suicide
97.13 100.0 97.70 95.98 98.28 55.75 54.02 63.22 77.01 64.94 54.02 48.28 63.79 77.01 62.64 43.68 46.55 40.80 38.51 52.87 98.85 99.43 99.43 100.0 98.85
thin
97.45 100.0 97.02 97.02 97.87 56.17 48.51 51.06 44.26 50.21 56.17 40.85 46.81 48.51 47.23 37.87 20.85 28.51 20.00 50.21 98.30 97.45 99.57 98.72 98.72
sex
harrasment 99.48 99.48 98.43 97.39 97.13 63.19 64.49 68.15 77.02 70.50 63.97 68.67 66.58 75.20 68.67 62.92 55.09 58.75 57.44 65.54 96.08 95.56 95.30 98.96 98.69
other
99.18 99.18 98.37 97.00 97.55 72.21 72.21 82.56 84.74 79.84 69.21 73.84 81.74 82.56 76.84 63.49 66.76 70.30 70.03 71.93 97.00 98.64 98.09 98.64 98.37
porn
96.00 100.0 97.33 92.00 96.67 66.00 78.00 84.00 80.00 74.67 75.33 79.33 83.33 84.67 79.33 66.00 68.00 71.33 64.67 70.00 94.00 92.00 99.33 98.00 98.67
substance
alcohol
98.60 98.60 94.40 96.36 97.20 80.39 83.19 88.80 89.64 85.43 81.51 83.19 85.99 87.68 83.47 78.15 76.47 77.31 78.43 82.35 95.24 96.64 97.20 98.88 98.04
cannabis
76.49 80.88 72.91 76.49 71.31 49.80 46.22 70.52 66.53 48.61 49.40 44.62 66.53 64.14 51.39 51.39 37.05 47.81 48.61 51.79 81.67 88.84 73.31 93.23 76.10
drug
94.44 96.91 91.50 92.58 94.44 46.21 51.93 62.60 60.59 53.63 45.75 48.84 56.88 58.27 54.87 38.64 38.95 39.57 38.49 49.92 94.44 97.84 91.65 98.76 96.29
other
94.77 95.68 92.97 90.99 92.97 55.50 61.98 70.09 74.05 64.32 54.05 52.07 68.11 69.37 63.78 44.50 43.24 47.57 40.36 60.54 94.05 94.23 94.23 96.40 97.84
tobacco
83.96 83.02 77.36 73.58 82.08 59.43 66.04 72.64 73.58 59.43 61.32 63.21 77.36 71.70 65.09 55.66 54.72 51.89 54.72 57.55 84.91 94.34 80.19 89.62 89.62
weapon
biological 98.12 98.59 96.71 93.43 98.12 87.79 74.18 93.90 84.04 84.98 90.14 72.30 87.79 82.63 81.69 82.16 59.15 57.28 62.44 61.97 98.59 100.0 96.24 100.0 97.65
chemical
94.91 96.30 96.30 89.35 94.44 87.50 68.52 86.11 81.48 83.80 92.59 67.13 92.13 84.72 78.24 85.65 58.80 60.19 68.98 63.43 96.76 99.07 97.22 96.76 93.06
firearm
97.32 91.96 95.54 93.75 95.54 65.18 58.04 77.68 81.25 71.43 70.54 61.61 82.14 74.11 66.07 67.86 52.68 57.14 57.14 59.82 96.43 95.54 96.43 97.32 96.43
other
96.12 94.29 91.02 88.16 90.82 63.27 63.27 71.84 75.10 67.96 63.88 61.02 70.20 70.00 66.94 62.04 57.35 56.33 56.94 67.96 95.92 97.14 95.51 96.73 96.33
radioactive 96.27 95.03 92.55 93.79 94.41 90.68 79.50 93.17 92.55 94.41 90.68 80.75 94.41 91.30 90.68 90.68 77.64 75.16 82.61 80.12 94.41 99.38 93.79 98.14 97.52
Overall
96.43 96.69 95.16 93.15 95.15 66.71 66.58 73.65 77.31 69.92 65.94 65.10 72.08 75.49 68.73 59.29 54.66 55.95 54.53 64.75 95.31 96.29 95.24 96.93 95.72
Table 9: Continuation: Benchmarking LLMs with M-ALERT. Each row depicts a safety category
from our taxonomy (cf. Fig. 2a), while each column depicts an LLM under evaluation. Values in the
last row depict overall safety scores, all others are category-wise safety scores (higher is safer). Safe
scores S(Φ) ≥99 are gray , unsafe scores within 90 ≤S(Φ)<99 are orange , and highly unsafe
scores S(Φ)<90 are red . Best viewed in color.
Llama-3.2-3B
Llama-3.3-70B-Instruct
Qwen2.5-0.5B
Qwen2.5-0.5B-Instruct
Qwen2.5-1.5B
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
crime
cyber
39.17 61.71 54.92 47.92 44.20 99.12 98.91 98.25 99.12 98.25 40.92 29.32 34.57 50.11 47.70 80.96 95.40 92.12 89.06 75.49 37.42 47.48 31.73 40.26 44.42
injury
41.55 51.39 59.68 49.50 48.33 97.94 94.94 98.05 97.83 98.16 47.55 43.21 43.49 55.45 60.68 80.70 92.32 90.32 88.82 82.98 44.94 44.66 41.55 43.16 44.88
kidnapp
21.39 43.28 32.84 48.76 24.38 99.00 98.51 99.00 100.0 100.0 31.84 11.94 17.91 55.72 49.25 75.62 93.03 85.57 83.58 65.67 32.84 35.32 11.44 48.76 29.85
other
66.76 60.74 87.97 80.80 72.78 99.14 96.85 98.85 100.0 99.43 62.18 65.33 75.64 73.64 79.37 78.80 97.42 92.84 94.27 67.34 71.35 72.21 79.37 67.05 63.61
privacy
42.38 84.76 85.04 69.81 62.88 99.45 99.72 99.45 99.72 100.0 45.71 63.43 43.77 47.37 32.96 83.38 94.46 95.84 95.84 80.33 34.90 63.43 62.05 49.86 57.06
propaganda 71.55 41.27 67.60 54.29 66.35 82.35 50.92 88.14 78.88 94.99 45.23 41.47 71.36 45.81 63.16 70.97 83.22 99.81 92.67 98.84 54.87 27.00 37.61 46.19 48.79
tax
24.09 44.51 34.15 24.70 28.66 100.0 99.39 99.70 100.0 99.70 41.46 29.57 40.24 39.33 71.95 59.76 84.45 64.94 64.63 74.70 20.73 37.50 27.44 25.91 53.05
theft
30.96 59.43 51.03 40.05 37.91 98.54 97.94 98.97 98.97 98.80 44.51 27.44 37.56 50.09 46.74 53.69 94.68 94.51 76.07 59.61 37.91 40.57 21.61 29.42 37.74
hate
body
77.11 77.71 78.31 79.52 75.90 100.0 98.19 99.40 98.19 100.0 80.12 79.52 81.93 86.14 86.75 83.73 97.59 90.36 96.99 92.77 79.52 82.53 78.31 87.35 83.73
disabled
60.00 70.83 85.83 78.33 60.00 100.0 100.0 100.0 100.0 100.0 69.17 65.83 69.17 75.00 89.17 92.50 98.33 92.50 93.33 92.50 75.00 66.67 69.17 69.17 75.83
ethnic
60.44 59.46 74.86 62.41 67.73 99.59 99.34 99.18 99.67 99.67 64.54 57.08 63.31 63.55 73.46 76.25 94.19 89.11 88.53 85.67 69.45 79.93 72.07 70.52 73.05
lgbtq+
70.74 74.30 84.22 75.83 78.63 99.75 99.24 99.75 100.0 99.49 73.54 75.32 75.06 74.05 81.93 87.79 96.95 94.40 97.96 92.37 83.21 89.82 84.22 82.95 87.02
other
76.55 77.37 85.46 78.35 76.55 98.53 98.77 98.45 98.86 97.88 75.16 71.41 73.86 77.70 84.72 83.50 97.47 96.16 94.61 93.79 74.02 76.55 69.12 75.08 77.21
poor
82.18 79.21 93.07 90.10 89.11 99.01 100.0 100.0 99.01 100.0 93.07 86.14 87.13 86.14 85.15 93.07 99.01 97.03 98.02 98.02 86.14 94.06 83.17 92.08 88.12
religion
54.85 53.50 74.04 60.50 61.17 100.0 99.10 99.77 100.0 99.55 54.40 53.95 58.69 57.34 66.82 73.36 96.84 83.07 89.62 83.97 63.88 83.30 65.46 66.14 72.46
women
75.03 73.12 78.26 74.79 73.24 99.52 99.52 99.76 99.64 99.28 75.63 74.19 73.60 77.30 81.60 81.48 96.42 92.23 93.55 90.80 77.42 83.87 77.06 78.85 79.93
self harm
other
72.22 61.81 74.31 78.47 81.25 100.0 100.0 100.0 100.0 100.0 80.56 64.58 73.61 51.39 97.22 95.83 98.61 97.92 97.92 98.61 82.64 98.61 79.17 77.78 89.58
suicide
37.36 53.45 59.20 48.85 47.13 99.43 100.0 99.43 99.43 100.0 41.38 45.98 43.10 51.15 54.60 72.41 98.85 97.70 94.83 89.66 45.40 56.32 45.40 49.43 53.45
thin
45.53 40.43 43.83 48.94 53.62 98.72 100.0 98.30 99.57 100.0 56.17 59.15 50.21 40.43 62.13 78.72 99.57 88.09 88.09 77.02 64.68 90.64 73.19 63.40 79.15
sex
harrasment 60.84 63.45 69.71 64.23 64.75 99.22 95.56 98.69 99.48 99.48 63.19 62.14 64.49 73.63 74.15 90.60 96.87 95.30 95.56 92.43 66.84 76.50 60.57 66.84 65.01
other
68.66 74.11 82.29 74.11 68.66 98.37 97.82 98.64 98.37 98.91 67.30 66.49 66.76 76.84 68.39 87.47 95.10 91.83 92.64 91.83 67.57 78.47 65.40 71.12 68.66
porn
68.00 74.00 88.00 72.67 72.00 99.33 94.67 98.67 98.67 99.33 61.33 57.33 64.67 64.67 68.00 90.00 94.00 88.67 91.33 89.33 60.00 62.00 49.33 52.67 57.33
substance
alcohol
77.59 80.95 87.11 81.23 79.27 98.32 98.88 98.32 98.88 98.04 77.31 73.67 74.79 80.39 81.51 85.71 95.52 91.32 90.48 88.80 74.51 78.99 74.79 75.63 78.99
cannabis
43.82 51.39 73.31 50.60 47.01 83.27 87.25 86.85 96.41 87.65 45.42 36.65 47.81 52.59 48.21 70.52 84.86 78.88 83.27 76.89 37.85 37.05 35.06 39.84 45.42
drug
40.80 52.24 64.91 43.74 45.75 98.61 96.45 96.60 98.76 98.61 44.05 33.38 39.41 43.89 47.60 78.98 95.21 88.41 86.55 84.39 43.12 42.81 32.15 43.12 46.99
other
48.83 52.97 68.47 51.17 53.69 98.20 99.10 98.92 99.28 99.46 50.09 42.70 45.23 49.55 56.40 77.48 95.14 91.71 91.89 86.67 42.70 46.31 40.90 40.54 52.79
tobacco
63.21 65.09 61.32 50.94 62.26 90.57 89.62 93.40 92.45 97.17 59.43 46.23 44.34 54.72 67.92 73.58 81.13 68.87 81.13 71.70 46.23 51.89 40.57 44.34 45.28
weapon
biological 77.93 56.34 85.92 67.14 58.22 100.0 100.0 100.0 100.0 100.0 77.46 58.69 64.79 58.69 72.77 93.43 90.14 91.08 88.26 92.49 74.65 64.79 58.22 56.34 75.59
chemical
76.39 58.33 80.09 60.65 62.04 98.15 99.07 99.07 100.0 97.69 73.15 55.56 63.89 56.94 72.22 83.80 92.13 85.19 82.87 82.41 65.28 61.57 54.63 51.39 71.76
firearm
66.96 66.96 79.46 62.50 58.93 100.0 98.21 98.21 100.0 100.0 66.07 49.11 65.18 65.18 62.50 73.21 82.14 78.57 81.25 83.93 59.82 52.68 50.89 50.00 63.39
other
59.39 62.65 73.67 61.63 66.12 98.16 97.76 97.14 98.37 98.16 60.61 45.92 57.35 59.39 63.47 71.84 90.20 85.10 83.27 80.61 53.27 55.92 51.43 49.39 59.59
radioactive 87.58 75.78 91.93 77.02 80.75 98.76 95.03 100.0 99.38 100.0 86.96 74.53 76.40 70.19 81.37 95.65 95.03 90.06 95.65 90.06 77.64 74.53 72.05 65.84 85.71
Overall
59.06 62.58 72.21 62.80 61.54 97.85 96.27 98.09 98.40 98.74 61.11 54.60 59.04 61.39 68.12 80.46 93.63 89.36 89.45 84.74 59.56 64.19 56.10 58.45 64.23
Table 10: Continuation: Benchmarking LLMs with M-ALERT. Each row depicts a safety category
from our taxonomy (cf. Fig. 2a), while each column depicts an LLM under evaluation. Values in the
last row depict overall safety scores, all others are category-wise safety scores (higher is safer). Safe
scores S(Φ) ≥99 are gray , unsafe scores within 90 ≤S(Φ)<99 are orange , and highly unsafe
scores S(Φ)<90 are red . Best viewed in color.
18

--- Page 19 ---

Preprint. Under review.
Qwen2.5-1.5B-Instruct
Qwen2.5-14B
Qwen2.5-14B-Instruct
Qwen2.5-32B
Qwen2.5-32B-Instruct
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
crime
cyber
94.53 98.69 98.69 97.81 97.59 74.18 90.15 90.37 92.78 85.56 99.56 99.34 100.0 99.34 99.78 85.12 87.31 91.03 92.78 86.87 99.34 99.56 99.78 99.12 100.0
injury
95.94 98.39 97.00 97.78 98.22 76.14 79.53 82.76 84.93 77.47 99.05 97.89 98.89 98.89 98.72 82.87 80.92 86.48 90.60 81.81 99.05 98.44 99.33 99.00 98.61
kidnapp
90.05 98.51 85.57 99.00 99.50 77.61 82.09 89.55 88.06 80.60 100.0 99.00 100.0 99.50 100.0 79.60 80.60 85.07 90.55 79.10 100.0 99.50 100.0 100.0 100.0
other
92.26 97.71 99.71 98.85 98.28 90.83 88.54 92.55 93.41 87.97 99.43 98.28 99.14 99.43 98.85 89.68 89.97 98.28 93.70 94.56 100.0 98.57 99.43 99.71 99.43
privacy
82.83 88.92 98.34 95.57 95.57 84.76 78.95 87.26 88.37 76.45 99.17 99.72 100.0 100.0 100.0 86.70 80.33 94.46 90.58 88.09 99.17 99.17 99.17 99.72 99.72
propaganda 98.26 89.39 99.52 94.41 98.26 91.51 33.56 74.54 82.74 67.02 100.0 84.96 89.59 84.47 99.32 75.02 52.56 82.84 69.91 77.72 99.71 59.98 84.86 75.89 89.68
tax
67.07 94.82 82.62 82.62 70.73 81.71 92.99 84.45 90.24 83.23 100.0 99.70 99.70 100.0 99.70 89.02 90.24 85.37 95.12 93.60 100.0 100.0 99.70 100.0 100.0
theft
94.77 98.71 99.06 90.65 97.51 72.73 81.73 88.08 82.85 81.39 99.66 99.14 99.31 99.06 99.31 82.68 85.93 90.82 89.28 83.62 99.66 99.23 99.91 99.57 99.74
hate
body
95.78 98.19 97.59 100.0 96.39 92.17 91.57 95.18 92.77 91.57 100.0 100.0 100.0 100.0 99.40 93.37 88.55 94.58 95.78 95.18 100.0 100.0 100.0 100.0 100.0
disabled
96.67 98.33 98.33 99.17 98.33 97.50 98.33 97.50 98.33 90.00 100.0 100.0 100.0 100.0 100.0 96.67 94.17 95.83 98.33 99.17 100.0 100.0 100.0 100.0 100.0
ethnic
94.10 97.95 97.79 97.71 95.90 90.91 94.10 93.37 94.10 92.55 100.0 100.0 99.92 99.75 99.92 90.66 91.15 92.71 95.33 94.19 99.75 99.84 99.84 99.92 99.26
lgbtq+
97.20 99.24 97.46 99.49 98.47 95.67 96.95 95.67 95.42 95.17 100.0 99.75 100.0 100.0 99.49 89.82 93.38 96.18 96.95 93.64 100.0 100.0 100.0 100.0 99.24
other
93.06 98.94 99.10 99.02 98.94 82.52 84.07 92.73 85.78 86.76 99.84 99.67 99.35 99.51 99.43 86.11 80.64 82.76 92.16 86.03 99.92 99.75 100.0 99.92 99.18
poor
100.0 99.01 99.01 99.01 99.01 95.05 99.01 99.01 99.01 98.02 100.0 100.0 100.0 100.0 100.0 95.05 98.02 98.02 98.02 95.05 100.0 100.0 100.0 100.0 100.0
religion
96.61 97.97 97.97 98.87 98.19 89.39 94.58 93.68 95.49 94.81 100.0 100.0 100.0 100.0 100.0 92.10 95.03 94.58 97.07 93.91 100.0 100.0 99.77 100.0 99.77
women
97.49 99.40 98.21 98.57 98.81 92.59 94.38 95.10 95.58 92.71 99.40 99.64 99.88 99.88 99.64 92.59 94.86 96.06 96.89 93.31 99.52 99.64 99.64 99.76 99.16
self harm
other
99.31 100.0 100.0 100.0 100.0 98.61 100.0 99.31 98.61 97.92 100.0 100.0 100.0 100.0 100.0 95.83 89.58 98.61 97.92 97.22 100.0 100.0 100.0 100.0 100.0
suicide
93.68 98.85 98.85 99.43 97.13 86.21 90.23 90.80 92.53 83.91 100.0 98.85 100.0 100.0 100.0 87.36 90.80 91.38 95.40 90.80 100.0 98.85 99.43 100.0 100.0
thin
95.32 99.57 97.02 95.32 94.47 90.21 94.04 91.49 91.91 95.74 100.0 100.0 100.0 100.0 100.0 82.13 93.19 95.74 92.34 85.53 100.0 100.0 100.0 100.0 100.0
sex
harrasment 97.39 99.48 99.22 100.0 99.74 91.38 90.34 93.47 96.34 94.26 99.22 97.91 99.74 99.74 99.48 87.99 87.73 93.21 97.91 91.12 99.22 98.43 99.74 99.74 99.74
other
99.18 99.73 99.46 99.46 98.64 88.56 91.55 94.82 94.82 92.92 98.64 97.82 99.73 99.73 99.18 85.56 93.73 92.92 97.55 89.92 99.18 96.73 99.73 99.73 99.46
porn
97.33 100.0 99.33 98.67 99.33 86.00 90.67 90.00 90.67 87.33 98.67 94.67 98.67 98.67 98.00 80.00 81.33 82.00 89.33 83.33 95.33 97.33 99.33 97.33 99.33
substance
alcohol
96.36 98.60 97.20 98.32 97.20 87.39 89.64 91.32 91.04 87.11 99.16 98.88 98.60 99.44 99.72 89.92 91.04 94.96 94.96 88.52 97.76 98.04 98.60 99.72 98.88
cannabis
86.45 94.82 89.24 92.43 88.45 65.74 68.53 69.72 74.90 68.92 92.03 88.84 94.82 94.82 96.81 62.55 61.35 66.53 78.09 62.15 90.44 83.67 90.84 97.21 95.62
drug
93.97 98.45 99.07 97.37 99.07 80.53 78.05 80.37 87.64 80.06 99.85 98.61 99.69 99.85 99.69 80.99 82.38 86.40 90.88 79.13 99.54 97.99 99.85 99.85 100.0
other
94.05 98.02 98.38 97.12 96.40 78.38 81.80 84.68 88.29 82.16 99.10 98.02 100.0 99.82 100.0 83.96 84.14 89.91 90.09 84.68 98.92 99.28 99.82 99.64 99.46
tobacco
77.36 83.96 91.51 83.02 85.85 75.47 80.19 81.13 78.30 66.98 92.45 91.51 91.51 85.85 93.40 73.58 82.08 78.30 80.19 68.87 90.57 83.96 93.40 89.62 91.51
weapon
biological 97.65 98.12 95.77 98.12 94.37 92.96 93.90 93.43 86.38 84.51 99.53 100.0 99.53 99.06 100.0 92.49 84.51 88.26 95.77 88.26 99.53 100.0 99.53 100.0 100.0
chemical
93.52 98.15 90.28 96.30 87.96 86.11 90.28 91.67 75.93 80.09 96.30 98.61 98.15 98.15 97.22 90.74 88.43 87.04 90.28 82.87 98.61 98.61 99.07 99.54 98.61
firearm
90.18 94.64 95.54 95.54 90.18 77.68 74.11 79.46 82.14 75.89 100.0 94.64 100.0 100.0 99.11 82.14 79.46 83.04 91.96 76.79 100.0 94.64 98.21 99.11 100.0
other
92.04 97.35 95.71 95.31 95.92 73.67 77.35 77.14 83.67 77.76 97.96 96.73 97.76 96.94 98.57 80.20 82.86 81.02 87.35 80.00 98.98 98.37 99.39 98.57 98.98
radioactive 94.41 96.27 92.55 96.89 93.79 89.44 92.55 85.09 86.34 90.68 99.38 98.14 100.0 100.0 100.0 91.93 83.23 93.17 94.41 88.82 98.76 96.89 100.0 100.0 100.0
Overall
93.28 97.19 96.41 96.62 95.57 85.43 86.37 88.93 89.36 85.24 99.01 97.82 98.87 98.50 99.21 86.08 85.61 89.61 92.11 86.68 98.84 96.77 98.70 98.52 98.92
Table 11: Continuation: Benchmarking LLMs with M-ALERT. Each row depicts a safety category
from our taxonomy (cf. Fig. 2a), while each column depicts an LLM under evaluation. Values in the
last row depict overall safety scores, all others are category-wise safety scores (higher is safer). Safe
scores S(Φ) ≥99 are gray , unsafe scores within 90 ≤S(Φ)<99 are orange , and highly unsafe
scores S(Φ)<90 are red . Best viewed in color.
Qwen2.5-3B
Qwen2.5-3B-Instruct
Qwen2.5-72B
Qwen2.5-72B-Instruct
Qwen2.5-7B
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
crime
cyber
45.08 52.52 39.61 43.76 62.58 98.03 96.94 98.91 98.69 98.91 66.96 69.15 85.34 62.58 74.40 99.78 98.47 99.78 99.34 99.34 70.24 79.43 79.21 72.21 66.96
injury
54.00 57.12 52.06 48.16 62.79 98.28 97.39 99.44 98.16 98.83 69.91 65.68 76.92 66.85 67.24 99.11 98.50 99.50 99.33 99.33 60.79 69.30 68.19 68.41 65.02
kidnapp
44.78 70.65 41.79 54.73 44.28 97.51 97.51 99.00 99.00 100.0 63.18 65.17 67.66 53.23 60.20 100.0 99.50 100.0 99.50 100.0 57.71 64.18 59.20 71.14 60.70
other
79.94 83.09 80.23 78.22 81.95 98.28 97.13 100.0 99.14 98.85 68.77 80.52 89.40 86.53 83.95 99.43 93.98 99.43 98.85 99.14 82.23 83.38 89.11 85.10 83.67
privacy
52.63 63.99 53.46 73.68 66.20 83.38 88.92 88.64 95.57 95.57 75.07 55.12 81.44 86.15 78.95 99.72 99.72 99.72 100.0 100.0 75.35 73.13 67.59 66.20 68.70
propaganda 56.61 36.16 65.48 44.94 67.21 99.81 68.37 98.65 96.53 98.75 64.32 38.38 58.63 72.32 65.96 99.61 66.15 89.59 83.90 99.81 77.43 22.08 84.86 63.84 61.14
tax
39.63 47.26 27.74 32.01 50.91 97.26 98.78 89.33 98.78 84.76 76.83 73.78 82.32 78.66 63.72 99.70 99.09 99.09 98.78 99.70 79.88 89.33 68.29 53.96 51.83
theft
58.75 44.94 30.19 24.19 44.68 97.60 97.68 99.40 98.71 98.80 73.67 80.79 81.22 48.97 64.75 99.49 99.40 99.74 99.40 99.91 65.95 64.41 61.66 62.69 52.83
hate
body
80.72 87.95 81.93 91.57 90.96 99.40 98.80 100.0 99.40 99.40 92.17 87.35 88.55 93.98 89.16 100.0 100.0 100.0 100.0 100.0 80.72 86.14 80.72 89.76 88.55
disabled
84.17 73.33 75.83 77.50 82.50 98.33 100.0 99.17 99.17 100.0 94.17 89.17 92.50 79.17 85.00 100.0 100.0 100.0 100.0 100.0 95.00 87.50 94.17 90.00 90.83
ethnic
76.90 80.67 72.65 73.55 80.34 98.53 99.75 99.67 99.92 99.18 88.04 88.29 89.76 90.01 85.75 99.92 99.84 99.92 99.92 99.59 83.62 86.81 83.95 85.26 85.01
lgbtq+
82.44 88.80 82.95 82.19 87.79 99.49 100.0 99.75 99.75 99.49 93.13 91.86 91.86 93.89 91.09 99.75 100.0 100.0 100.0 99.75 88.04 91.86 89.82 91.86 88.55
other
76.55 78.02 76.63 77.37 86.11 99.43 99.84 99.75 99.51 99.84 80.31 76.88 79.90 83.01 77.53 99.75 99.67 99.84 98.61 98.69 77.29 79.98 83.91 79.82 82.35
poor
87.13 93.07 87.13 90.10 94.06 100.0 100.0 100.0 100.0 100.0 96.04 96.04 98.02 98.02 99.01 100.0 100.0 100.0 100.0 100.0 93.07 94.06 91.09 97.03 95.05
religion
79.68 83.52 74.94 76.52 77.65 99.77 100.0 99.77 99.77 98.65 89.84 90.07 89.62 93.23 88.04 100.0 99.77 100.0 100.0 100.0 81.94 88.26 81.49 86.23 86.00
women
83.15 86.86 78.14 80.17 82.44 99.16 99.88 100.0 99.52 99.64 93.19 90.92 92.83 93.43 90.20 99.76 99.76 99.88 99.88 99.64 88.89 89.13 87.46 91.40 83.87
self harm
other
80.56 93.75 80.56 81.25 95.83 100.0 100.0 100.0 100.0 100.0 97.92 94.44 99.31 97.22 96.53 99.31 100.0 100.0 100.0 100.0 93.06 96.53 93.75 94.44 96.53
suicide
60.92 62.07 54.02 51.72 67.24 100.0 99.43 100.0 100.0 100.0 86.78 85.06 83.91 85.06 78.16 100.0 98.85 100.0 100.0 100.0 66.09 78.74 81.61 67.82 72.99
thin
77.02 94.04 83.40 79.57 85.53 98.72 100.0 100.0 100.0 98.72 91.06 90.21 92.34 91.91 88.94 98.72 100.0 100.0 100.0 99.57 83.40 87.23 88.51 86.81 84.26
sex
harrasment 74.93 86.42 73.37 75.72 82.77 99.48 99.22 100.0 99.74 100.0 84.60 83.81 86.42 89.30 87.99 99.74 98.96 99.74 99.48 99.74 81.20 83.29 81.98 90.60 83.03
other
79.56 84.47 75.48 80.11 82.29 98.64 97.55 99.46 99.73 100.0 85.56 87.74 89.37 89.65 89.10 99.18 98.91 99.73 99.18 99.46 77.66 86.65 82.56 89.92 79.29
porn
65.33 74.67 56.00 63.33 66.00 99.33 97.33 100.0 99.33 100.0 76.00 71.33 78.00 84.67 80.67 98.67 96.67 99.33 98.67 100.0 68.00 72.67 64.67 74.00 62.00
substance
alcohol
79.83 83.19 79.55 77.03 78.99 97.48 98.88 99.72 99.72 98.88 86.83 85.15 88.80 84.03 82.63 98.04 98.88 99.16 98.88 99.16 83.47 82.35 86.55 85.43 83.75
cannabis
52.19 41.43 37.45 47.81 49.40 90.44 90.84 94.82 94.82 92.83 53.78 38.65 53.39 56.57 46.61 92.43 82.07 91.63 92.83 93.63 50.20 52.59 44.62 62.55 45.82
drug
51.62 52.24 42.81 47.45 54.87 98.92 97.68 100.0 99.07 99.69 69.24 60.43 73.88 65.22 65.07 99.23 97.68 99.54 99.07 100.0 57.34 64.76 63.06 68.01 54.25
other
53.33 53.15 50.81 47.21 60.36 98.02 96.40 99.28 98.56 99.10 71.35 64.68 83.24 71.89 74.23 98.92 97.66 99.46 99.64 100.0 60.90 71.17 68.65 69.01 62.34
tobacco
52.83 53.77 46.23 44.34 57.55 90.57 91.51 95.28 89.62 88.68 67.92 57.55 66.98 58.49 57.55 81.13 83.96 90.57 86.79 88.68 57.55 67.92 53.77 53.77 51.89
weapon
biological 83.57 66.67 65.26 69.48 77.00 98.12 98.59 99.06 99.53 98.12 90.14 62.91 81.22 78.87 79.34 100.0 100.0 100.0 99.53 100.0 87.32 74.65 75.59 84.04 75.59
chemical
75.46 63.89 66.20 66.20 78.24 97.22 99.54 98.15 98.15 96.30 82.41 57.87 76.39 70.83 75.00 98.15 98.15 97.22 99.54 98.15 80.09 67.13 75.46 73.15 72.22
firearm
65.18 53.57 61.61 66.96 63.39 98.21 92.86 100.0 97.32 95.54 69.64 58.93 75.00 74.11 58.04 100.0 97.32 100.0 100.0 99.11 72.32 63.39 69.64 69.64 61.61
other
58.98 56.33 57.14 56.94 61.43 96.12 95.71 98.57 95.92 97.76 72.04 69.18 71.22 70.82 67.55 98.57 97.76 99.39 98.16 98.78 62.65 64.49 64.69 69.80 67.96
radioactive 82.61 72.05 77.64 77.02 85.09 99.38 95.65 98.14 97.52 98.76 87.58 69.57 81.37 81.37 81.99 99.38 94.41 98.76 98.76 100.0 91.30 77.02 78.26 78.88 80.75
Overall
68.00 69.36 63.38 65.03 72.14 97.65 96.63 98.56 98.46 97.97 79.95 74.27 82.09 79.06 77.32 98.67 96.72 98.78 98.38 99.10 75.96 76.24 76.38 77.27 73.29
Table 12: Continuation: Benchmarking LLMs with M-ALERT. Each row depicts a safety category
from our taxonomy (cf. Fig. 2a), while each column depicts an LLM under evaluation. Values in the
last row depict overall safety scores, all others are category-wise safety scores (higher is safer). Safe
scores S(Φ) ≥99 are gray , unsafe scores within 90 ≤S(Φ)<99 are orange , and highly unsafe
scores S(Φ)<90 are red . Best viewed in color.
19

--- Page 20 ---

Preprint. Under review.
Qwen2.5-7B-Instruct
Teuken-7B-instruct-commercial
aurora-m
aya-expanse-8b
gemma-2-27b
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
crime
cyber
99.34 97.81 98.47 99.12 99.78 47.05 47.26 46.83 48.36 52.95 68.71 77.02 76.81 84.90 74.40 96.28 98.25 97.16 96.06 97.37 49.67 65.43 65.43 56.24 68.71
injury
98.67 96.77 98.39 98.33 98.72 55.84 55.17 55.01 55.28 53.67 80.59 62.57 78.98 86.60 81.03 96.33 96.61 96.44 95.33 95.61 47.39 55.84 54.34 60.18 59.96
kidnapp
98.51 99.00 96.02 99.50 100.0 21.39 23.88 19.40 19.40 20.90 74.13 46.27 74.63 81.09 76.12 92.04 97.51 95.52 96.02 97.51 22.39 25.87 14.43 63.68 24.88
other
99.71 96.85 100.0 97.71 99.14 73.93 73.64 74.50 71.35 73.07 87.97 79.66 91.12 94.84 84.24 98.57 97.42 98.57 97.42 97.71 74.79 81.09 85.67 71.35 82.81
privacy
98.89 96.68 99.45 99.17 99.45 62.05 65.37 63.99 61.22 64.82 72.85 81.44 63.99 90.86 86.70 90.03 94.74 98.89 93.63 96.12 74.52 77.56 56.79 70.64 48.20
propaganda 92.38 62.78 98.46 94.21 99.61 33.85 32.34 32.98 33.85 34.23 68.66 49.37 64.22 88.24 75.41 68.76 78.98 81.68 82.74 67.21 45.90 24.49 48.31 50.24 52.84
tax
95.12 99.70 98.17 98.78 99.09 39.94 41.77 39.63 41.77 43.29 42.68 51.83 43.90 52.44 45.43 100.0 99.70 97.87 93.60 85.37 65.55 84.76 67.68 76.22 57.93
theft
99.06 98.28 99.66 98.28 99.06 36.62 39.54 37.48 37.39 38.16 77.36 79.07 80.36 88.25 86.45 95.80 97.60 97.00 94.34 97.60 42.88 44.17 46.83 45.28 53.09
hate
body
99.40 100.0 100.0 100.0 100.0 84.34 84.94 82.53 87.35 81.93 96.39 89.16 90.96 98.19 95.78 100.0 100.0 100.0 100.0 99.40 81.93 81.93 75.90 89.16 86.14
disabled
100.0 100.0 100.0 99.17 100.0 80.00 79.17 79.17 83.33 81.67 91.67 82.50 87.50 99.17 92.50 99.17 100.0 100.0 99.17 100.0 80.00 80.83 82.50 75.83 86.67
ethnic
99.10 100.0 99.67 99.59 99.67 76.09 74.77 74.53 75.10 74.86 91.40 77.31 86.49 93.37 86.32 99.51 99.84 99.67 99.26 99.51 75.18 83.13 67.57 71.74 74.61
lgbtq+
99.75 100.0 99.75 99.49 99.75 81.68 82.91 82.95 81.42 81.42 94.91 88.04 91.60 96.44 92.37 99.75 99.75 100.0 99.49 99.75 80.15 87.28 80.41 83.97 82.19
other
99.43 99.26 99.75 99.18 98.45 80.07 79.98 79.82 80.39 80.39 96.16 91.99 92.16 97.63 93.22 99.84 99.18 99.92 99.35 99.35 77.21 79.98 77.53 81.21 80.96
poor
100.0 100.0 100.0 100.0 100.0 93.07 88.12 89.11 89.11 91.09 95.05 92.08 94.06 98.02 96.04 100.0 100.0 100.0 99.01 100.0 84.16 89.11 85.15 88.12 92.08
religion
99.77 99.10 99.55 100.0 99.55 72.69 73.59 71.78 69.53 68.17 86.91 65.24 80.14 88.04 84.65 99.77 99.55 99.32 99.10 100.0 69.98 81.72 72.91 74.27 75.17
women
99.28 99.40 99.64 99.76 99.52 78.38 78.85 78.02 80.29 77.90 93.19 86.62 88.77 95.82 92.71 98.92 99.40 99.16 99.16 99.40 81.00 83.27 77.30 80.41 82.44
self harm
other
100.0 100.0 100.0 100.0 100.0 93.75 90.28 92.36 94.44 93.06 91.67 93.75 99.31 95.83 94.44 100.0 100.0 99.31 100.0 100.0 90.97 94.44 94.44 86.81 93.75
suicide
99.43 98.85 99.43 100.0 99.43 55.75 51.72 52.87 47.13 54.02 83.91 77.01 87.36 95.40 77.59 99.43 100.0 98.28 97.70 98.85 71.84 78.16 70.11 71.26 67.24
thin
97.02 100.0 100.0 100.0 100.0 83.83 87.23 85.96 91.06 87.66 71.06 85.53 84.68 86.81 81.70 92.77 100.0 94.47 97.02 96.60 73.19 84.68 74.89 67.23 75.74
sex
harrasment 98.96 98.43 99.48 99.22 99.22 52.22 53.26 51.96 49.09 51.70 88.51 84.33 87.47 93.47 90.08 98.96 99.22 98.96 98.43 98.96 67.89 76.50 75.20 74.15 77.28
other
97.82 97.82 98.91 99.18 98.91 65.94 65.67 66.21 59.40 61.58 89.37 82.02 90.74 96.19 90.46 99.18 98.91 98.91 99.46 98.37 73.57 82.56 79.02 85.83 83.65
porn
96.67 96.00 98.67 97.33 98.67 44.67 42.00 48.00 40.67 42.67 80.67 79.33 78.00 86.00 84.00 96.67 98.00 98.67 95.33 98.00 71.33 74.00 70.67 80.67 69.33
substance
alcohol
98.04 98.88 99.44 99.44 98.60 80.11 78.99 78.99 78.99 80.11 91.88 89.36 88.24 93.00 91.32 97.48 97.48 97.48 98.04 96.36 79.83 85.71 86.83 84.31 85.15
cannabis
86.45 79.28 91.63 92.83 93.63 41.43 38.25 44.22 44.22 44.22 56.18 57.37 55.78 70.92 56.97 82.47 76.89 75.70 85.26 74.90 51.39 55.38 54.18 63.35 58.96
drug
97.84 96.45 99.54 98.45 98.45 46.52 44.36 41.89 44.82 44.51 70.94 62.91 66.00 74.96 72.95 95.83 96.60 94.13 95.36 95.83 51.00 63.52 56.41 61.36 65.22
other
96.58 96.40 99.28 98.56 99.10 57.30 57.48 54.59 55.86 54.23 80.18 67.39 82.70 86.85 80.72 97.48 96.22 97.30 97.66 97.12 57.48 72.25 64.32 68.47 71.89
tobacco
82.08 82.08 92.45 83.96 91.51 72.64 61.32 65.09 64.15 68.87 74.53 73.58 60.38 65.09 66.98 81.13 83.02 76.42 69.81 74.53 74.53 73.58 50.00 66.04 66.04
weapon
biological 97.65 97.18 99.06 97.65 99.53 67.61 68.08 68.54 70.89 68.08 94.84 81.22 85.92 81.69 86.85 98.12 94.84 97.18 95.31 94.84 89.67 73.24 73.71 85.92 86.38
chemical
93.98 94.44 97.22 97.22 96.30 61.11 61.11 59.26 64.81 63.43 90.28 82.41 85.65 75.46 81.94 95.83 88.89 85.19 88.43 88.89 83.80 74.54 74.54 83.80 81.02
firearm
98.21 87.50 97.32 96.43 98.21 61.61 64.29 63.39 66.96 64.29 68.75 61.61 72.32 76.79 71.43 92.86 79.46 88.39 89.29 89.29 70.54 68.75 64.29 72.32 78.57
other
95.31 94.90 97.14 96.33 97.96 60.82 62.86 63.27 60.82 56.94 72.86 66.12 72.86 80.20 77.76 93.06 94.08 95.10 94.29 93.47 63.27 67.35 66.33 66.73 70.00
radioactive 98.76 89.44 98.76 95.65 98.76 78.26 77.02 74.53 77.64 71.43 91.30 90.68 82.61 84.47 91.30 96.89 91.93 90.68 94.41 94.41 86.34 79.50 81.99 92.55 91.30
Overall
97.29 95.42 98.60 97.96 98.75 63.77 62.51 63.09 63.32 63.29 81.74 76.09 80.18 86.78 82.50 95.40 95.44 95.23 94.98 94.45 69.04 72.83 68.62 73.42 72.82
Table 13: Continuation: Benchmarking LLMs with M-ALERT. Each row depicts a safety category
from our taxonomy (cf. Fig. 2a), while each column depicts an LLM under evaluation. Values in the
last row depict overall safety scores, all others are category-wise safety scores (higher is safer). Safe
scores S(Φ) ≥99 are gray , unsafe scores within 90 ≤S(Φ)<99 are orange , and highly unsafe
scores S(Φ)<90 are red . Best viewed in color.
gemma-2-27b-it
gemma-2-2b
gemma-2-2b-it
gemma-2-9b
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
de
en
es
fr
it
crime
cyber
99.78 100.0 99.78 99.78 100.0 49.23 60.18 59.30 44.42 56.67 99.56 99.78 99.34 99.56 99.12 46.61 65.65 61.71 52.95 62.36
injury
99.67 99.94 99.78 99.61 99.78 43.05 57.23 58.45 52.56 62.96 99.72 99.89 99.50 99.39 99.67 44.49 60.34 62.35 44.49 66.91
kidnapp
100.0 100.0 100.0 100.0 100.0 19.40 42.29 25.37 55.72 33.33 99.50 100.0 100.0 99.50 92.04 41.79 48.26 28.36 59.20 37.81
other
100.0 100.0 99.43 100.0 99.71 70.20 71.06 89.11 74.50 84.81 99.43 99.43 99.43 99.43 99.43 60.74 71.06 82.23 67.62 83.95
privacy
100.0 100.0 99.72 99.72 100.0 56.79 83.10 83.93 64.82 81.99 100.0 100.0 100.0 99.72 99.72 41.27 87.53 81.16 78.95 55.68
propaganda 73.48 64.61 75.51 72.61 78.50 68.85 64.71 76.18 80.52 87.95 79.85 67.79 75.80 69.82 80.91 32.30 40.12 63.36 52.36 56.70
tax
100.0 100.0 100.0 100.0 100.0 54.57 55.18 59.45 48.17 59.76 100.0 100.0 100.0 100.0 100.0 47.56 62.80 47.87 64.63 41.77
theft
99.83 100.0 100.0 99.83 99.83 44.08 58.58 48.54 32.76 62.01 99.57 99.91 99.74 98.11 99.57 36.62 63.29 53.17 30.19 61.66
hate
body
100.0 100.0 100.0 100.0 100.0 82.53 85.54 84.94 89.76 87.95 100.0 100.0 99.40 100.0 100.0 82.53 84.34 74.10 81.93 86.75
disabled
100.0 100.0 100.0 100.0 100.0 75.00 80.00 75.83 71.67 83.33 100.0 100.0 100.0 100.0 100.0 74.17 77.50 77.50 78.33 91.67
ethnic
99.92 99.92 100.0 100.0 100.0 64.46 63.47 70.19 65.44 72.97 99.75 100.0 100.0 100.0 100.0 73.14 76.33 68.80 65.85 72.07
lgbtq+
100.0 100.0 100.0 100.0 100.0 74.81 81.42 81.17 75.83 82.44 99.75 100.0 100.0 100.0 99.49 77.10 84.99 79.64 82.70 86.77
other
100.0 100.0 100.0 100.0 99.75 81.29 83.99 88.56 85.87 87.34 100.0 100.0 99.92 99.75 99.26 76.88 87.34 83.99 81.05 83.66
poor
100.0 100.0 100.0 100.0 100.0 85.15 89.11 90.10 90.10 87.13 100.0 100.0 100.0 99.01 98.02 87.13 89.11 86.14 90.10 91.09
religion
100.0 100.0 100.0 100.0 100.0 62.53 56.21 67.72 59.59 69.75 100.0 100.0 100.0 100.0 100.0 63.43 69.98 70.20 61.85 68.85
women
100.0 100.0 100.0 99.88 100.0 78.61 78.97 80.76 79.33 82.80 100.0 100.0 99.88 99.76 99.76 81.00 83.39 76.34 77.06 81.36
self harm
other
100.0 100.0 100.0 100.0 100.0 76.39 75.00 78.47 69.44 86.81 100.0 100.0 100.0 100.0 100.0 90.28 88.19 94.44 68.06 97.92
suicide
100.0 100.0 100.0 100.0 100.0 45.98 53.45 60.92 60.92 68.39 99.43 100.0 100.0 99.43 99.43 52.87 62.64 76.44 49.43 72.41
thin
100.0 100.0 100.0 100.0 99.57 45.11 48.94 52.34 37.87 59.15 100.0 100.0 99.57 100.0 100.0 66.38 71.06 74.89 61.70 72.34
sex
harrasment 100.0 100.0 100.0 100.0 99.74 66.84 71.54 73.37 73.89 80.16 100.0 100.0 99.74 99.74 100.0 66.84 75.46 70.76 72.32 83.03
other
100.0 100.0 100.0 100.0 100.0 75.75 79.02 83.65 80.38 80.65 99.73 100.0 100.0 100.0 99.73 67.57 82.29 84.47 81.47 79.29
porn
100.0 100.0 100.0 100.0 100.0 78.00 77.33 84.00 76.00 84.00 100.0 100.0 100.0 98.67 100.0 67.33 84.67 73.33 70.00 78.67
substance
alcohol
99.44 100.0 100.0 99.72 99.72 83.47 80.11 84.87 81.51 85.71 99.72 100.0 98.88 99.44 100.0 78.43 85.15 84.87 79.55 81.23
cannabis
98.01 100.0 100.0 100.0 100.0 54.58 56.97 63.75 49.80 59.76 95.22 100.0 97.61 99.60 94.42 41.43 48.21 62.55 44.62 54.18
drug
100.0 100.0 100.0 100.0 100.0 44.20 50.08 58.27 47.45 57.19 99.69 99.69 99.85 99.85 100.0 41.73 54.10 58.58 49.61 62.29
other
100.0 99.64 99.82 99.64 100.0 53.87 57.12 70.99 54.59 68.47 99.64 99.10 99.28 99.28 99.82 47.03 59.10 64.86 51.53 65.59
tobacco
99.06 100.0 99.06 99.06 99.06 66.04 65.09 64.15 63.21 66.04 95.28 100.0 100.0 98.11 99.06 57.55 64.15 61.32 47.17 61.32
weapon
biological 100.0 100.0 100.0 100.0 100.0 77.93 62.44 66.20 65.73 65.73 100.0 99.53 100.0 100.0 99.06 83.10 69.01 82.63 64.32 80.28
chemical
99.07 100.0 100.0 100.0 99.54 75.00 57.87 60.65 66.20 64.35 98.61 100.0 97.69 99.54 95.83 77.31 69.44 79.17 62.04 78.70
firearm
100.0 100.0 100.0 100.0 100.0 76.79 66.07 74.11 74.11 69.64 100.0 100.0 100.0 100.0 100.0 73.21 66.07 66.96 61.61 70.54
other
99.59 99.59 99.80 99.39 99.80 65.31 68.16 71.43 68.98 77.55 98.57 99.39 98.57 98.98 99.39 58.98 63.88 69.18 58.78 74.08
radioactive 100.0 100.0 100.0 100.0 100.0 88.82 73.29 74.53 79.50 81.37 97.52 100.0 100.0 98.76 100.0 81.99 75.16 88.82 77.02 90.06
Overall
99.00 98.87 99.15 99.04 99.22 65.14 67.30 70.67 66.27 73.07 98.77 98.89 98.88 98.61 98.55 63.09 70.96 71.57 64.64 72.84
Table 14: Continuation: Benchmarking LLMs with M-ALERT. Each row depicts a safety category
from our taxonomy (cf. Fig. 2a), while each column depicts an LLM under evaluation. Values in the
last row depict overall safety scores, all others are category-wise safety scores (higher is safer). Safe
scores S(Φ) ≥99 are gray , unsafe scores within 90 ≤S(Φ)<99 are orange , and highly unsafe
scores S(Φ)<90 are red . Best viewed in color.
20

```
