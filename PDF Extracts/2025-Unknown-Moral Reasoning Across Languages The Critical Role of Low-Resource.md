---
title: "2025-Unknown-Moral Reasoning Across Languages The Critical Role of Low-Resource - PDF Extract"
source_pdf: "2025-Unknown-Moral Reasoning Across Languages The Critical Role of Low-Resource.pdf"
pages: 5
extracted_at: "2026-02-07T17:00:46.075912"
---

# PDF Extract: 2025-Unknown-Moral Reasoning Across Languages The Critical Role of Low-Resource

**Source PDF:** 2025-Unknown-Moral Reasoning Across Languages The Critical Role of Low-Resource.pdf
**Total Pages:** 5

---

## Content

```
--- Page 1 ---

Moral Reasoning Across Languages: The Critical Role of Low-Resource
Languages in LLMs
Huichi Zhou1, Zehao Xu2, Munan Zhao2, Kaihong Li3, Yiqiang Li, Hongtao Wang2,
1Imperial College London
2North China Electric Power University
3Sun Yat-sen University
Abstract
In this paper, we introduce the Multilingual
Moral Reasoning Benchmark (MMRB) 1 to
evaluate the moral reasoning abilities of large
language models (LLMs) across five typologi-
cally diverse languages and three levels of con-
textual complexity: sentence, paragraph, and
document. Our results show moral reasoning
performance degrades with increasing context
complexity, particularly for low-resource lan-
guages such as Vietnamese. We further fine-
tune the open-source LLaMA-3-8B model us-
ing curated monolingual data for alignment
and poisoning. Surprisingly, low-resource lan-
guages have a stronger impact on multilingual
reasoning than high-resource ones, highlight-
ing their critical role in multilingual NLP.
1
Introduction
The advancement of Large Language Models
(LLMs), such as ChatGPT (OpenAI, 2023), has gar-
nered significant attention in various downstream
applications. Recently, many researchers have fo-
cused on the moral reasoning capabilities of LLMs
and on preventing them from generating toxic or
harmful content (Zhou et al., 2023; Rao et al.,
2023a). Unlike traditional language models (e.g.,
BERT (Devlin et al., 2019)), which tend to make
binary moral judgments and are often criticized
for their lack of interpretability (Rao et al., 2023a;
Talat et al., 2022), LLMs are capable of perform-
ing inference from a reasoning perspective (e.g.,
chain-of-thought (Wei et al., 2023)).
However, prior research on moral reasoning has
mostly focused on monolingual datasets (primarily
English), overlooking the importance of evaluating
LLMs’ multilingual moral reasoning capabilities.
The lack of robustness in multilingual moral reason-
ing may undermine the fairness of LLM-based sys-
tems, potentially affecting user experiences across
1https://anonymous.4open.science/r/ethics_
scenarios-913B
different language backgrounds. Therefore, it is
crucial to assess both the consistency and the key
influencing factors of LLM performance in multi-
lingual moral reasoning.
Do LLMs behave consistently on moral reason-
ing across different languages?
To answer this question, we propose MMRB,
the Multilingual Moral Reasoning Bench-
mark, spanning five languages.
Specifically,
we collect well-established moral reasoning
datasets, including ETHICSBASE (Hendrycks et al.,
2020),
ETHICSPRO (Ma et al., 2023),
and
curate ETHICSMAX using the Moral Stories
dataset (Scherrer et al., 2024) and the moral
dilemma framework (Rao et al., 2023b) to create
more complex moral reasoning scenarios. These
datasets are then translated into five typologically
diverse languages (English, Chinese, Russian, Viet-
namese, and Indonesian).
Based on MMRB, we evaluate the multilin-
gual moral reasoning performance of five promi-
nent LLMs, including both closed-source (e.g.,
GPT-4 (OpenAI, 2023)) and open-source (e.g.,
LLaMA (AI@Meta, 2024)) models. Our exper-
iments reveal significant inconsistencies in moral
reasoning across different languages. To further
explore the impact of language on model perfor-
mance, we fine-tune LLaMA-3-8B on MMRB to
analyze cross-linguistic effects in alignment and
poisoning settings.
Our contributions are: (1) We introduce MMRB,
a multilingual moral reasoning dataset comprising
2,170 moral scenarios across five languages. (2)
We benchmark five popular LLMs using MMRB,
revealing that their moral reasoning performance is
inconsistent across languages. (3) We demonstrate
that fine-tuning on low-resource languages has a
disproportionately strong impact (both positive and
negative) on multilingual reasoning performance.
1
arXiv:2504.19759v1  [cs.CL]  28 Apr 2025

--- Page 2 ---

2
Related Work
Monolingual Moral Reasoning.
Most prior re-
search on moral reasoning focuses on English.
Hendrycks et al. (2020) proposed the ETHICS
dataset, which covers concepts such as justice, well-
being, duties, virtues, and commonsense morality,
and evaluated models like BERT (Devlin et al.,
2019). Ziems et al. (2022) introduced the MIC
dataset to study whether chatbots can generate ut-
terances aligned with Rules of Thumb (RoT) in
moral contexts. The Moral Stories dataset (Emelin
et al., 2021) examines whether language models
can produce moral responses in social scenarios.
To analyze LLMs’ moral reasoning in ambiguous
cases, Scherrer et al. (2024) created datasets with
680 high-ambiguity and 687 low-ambiguity sce-
narios. However, these methods largely do not
leverage LLMs’ advanced reasoning capabilities,
such as chain-of-thought (CoT) prompting (Wei
et al., 2022), which can improve the stability and
accuracy of moral inference. Moreover, they of-
ten overlook the generative nature of LLMs, which
allows for explicit reasoning steps and nuanced
decision-making beyond binary classification.
Multilingual Moral Reasoning.
According to
the LLaMA-3 technical report,2 LLMs are trained
on different quantities of data per language, with
over 5% of the training data comprising high-
quality non-English content covering more than
30 languages. As a result, performance is typically
better in English. Haemmerl et al. (2023) trained
monolingual Sentence-BERT models for five lan-
guages to assess multilingual moral reasoning, but
their approach focused on short, unambiguous sen-
tences and high-resource languages. Khandelwal
et al. (2024) used GPT-4, ChatGPT, and LLaMA2-
70B-Chat to evaluate moral dilemmas across six
languages, finding weaker performance in Hindi
and Swahili compared to Spanish, Russian, Chi-
nese, and English.
3
Experiment
3.1
Setup
Dataset.
We conduct multilingual alignment ex-
periments using three datasets: (1) ETHICSBASE:
A sentence-level binary classification dataset cov-
ering five moral dimensions (e.g., commonsense,
justice).
(2) ETHICSPRO: A paragraph-level
2https://ai.meta.com/blog/meta-llama-3/
dataset enhanced from ETHICSBASE using LLM-
generated moral reasoning (e.g., ChatGPT), incor-
porating richer context and implicit ethical cues. (3)
ETHICSMAX: A document-level dataset created
by expanding paragraph-level entries into struc-
tured moral dilemmas.
Each scenario involves
three ethical branches (Virtue, Deontological, Con-
sequentialist), each tied to six normative principles
and three answer choices.
To support multilingual evaluation, we trans-
late all datasets into five typologically diverse lan-
guages: English, Chinese, Russian, Vietnamese,
and Indonesian. We use the DeepSeek API for
initial translation, followed by manual verification
by bilingual annotators. For quality assurance, we
apply cross-validation using Google Translate to
identify and correct translation inconsistencies or
cultural mismatches. We also filter out scenarios
with conflicting or ambiguous moral content, ensur-
ing linguistic and conceptual fidelity. The resulting
corpus, MMRB, contains 2,170 high-quality scenar-
ios across three complexity levels.
Model Selection.
We evaluate five strong mul-
tilingual LLMs: GPT-43, GPT-3.54, LLaMA3-
70B-Instruct5, LLaMA3-8B-Instruct6, and Mixtral-
8x7B-Instruct-v0.17. Inference is conducted using
greedy decoding (temperature = 0) for consistency.
Fine-tuning Strategy.
To investigate how mono-
lingual data quality affects multilingual perfor-
mance, we fine-tune the open-source LLaMA3-
8B model (AI@Meta, 2024) using LLaMA-
Factory (Zheng et al., 2024). We design two fine-
tuning settings: Monolingual Alignment: Fine-
tuning on verified, high-quality data in a single lan-
guage (e.g., Indonesian) to test cross-lingual gener-
alization. Monolingual Poisoning: Fine-tuning on
label-corrupted data in one language to examine its
negative impact on other languages.
3.2
Results
3.2.1
Evaluation
Our goal is to evaluate the consistency of moral rea-
soning in multilingual settings across five LLMs
on three levels of context: sentence, paragraph,
and document. Table 1 summarizes the results.
3platform.openai.com/docs/models/gpt-4-turbo-and-gpt-4
4platform.openai.com/docs/models/gpt-3-5-turbo
5replicate.com/meta/meta-llama-3-70b-instruct/api
6replicate.com/meta/meta-llama-3-8b-instruct/api
7replicate.com/mistralai/mixtral-8x7b-instruct-v0.1/api
2

--- Page 3 ---

Dataset
Model
GPT-4 GPT-3.5 Llama3-70b Llama3-8b Mixtral
ETHICSBASE-EN
96.5
86.5
92.9
88.3
90.8
ETHICSBASE-ZH
88.1
78.4
84.3
79.7
81.2
ETHICSBASE-RU
91.7
75.3
84.9
76.2
84.2
ETHICSBASE-VI
86.7
67.3
77.1
65.2
73.4
ETHICSBASE-ID
90.3
75.6
79.2
63.0
72.5
ETHICSBASE-AVG
90.6
76.6
83.7
74.5
80.4
ETHICSPRO-EN
84.8
72.0
75.7
72.1
79.6
ETHICSPRO-ZH
81.8
65.9
72.5
69.0
71.9
ETHICSPRO-RU
82.9
64.5
74.7
64.6
74.5
ETHICSPRO-VI
80.6
66.3
71.5
58.2
68.7
ETHICSPRO-ID
82.9
68.9
67.1
57.1
71.1
ETHICSPRO-AVG
82.6
67.5
72.3
64.2
73.2
ETHICSMAX-EN
91.1
78.5
87.4
84.0
63.7
ETHICSMAX-ZH
90.6
53.4
77.7
63.4
66.4
ETHICSMAX-RU
91.3
55.4
86.4
78.0
47.3
ETHICSMAX-VI
85.6
49.0
80.7
72.6
27.6
ETHICSMAX-ID
82.0
50.1
75.5
70.2
44.0
ETHICSMAX-AVG
88.1
57.3
81.5
73.7
49.8
Table 1: Evaluating the ability of moral reasoning across
five LLMs on three datasets in multilingual setting.
GPT-4
GPT-3.5
Llama3-70b
Llama3-8b
Mixtral
V.
D.
C.
V.
D.
C.
V.
D.
C.
V.
D.
C.
V.
D.
C.
EN 94.5 91.0 89.2 79.0 82.9 76.1 89.1 89.5 85.7 85.5 85.9 82.1 63.4 66.1 61.5
ZH 94.5 91.8 89.3 51.3 53.8 52.9 77.4 81.1 76.2 62.5 65.7 62.0 68.6 67.4 63.8
RU 94.5 91.2 89.5 55.1 56.1 54.0 89.8 87.9 84.6 80.5 79.4 74.9 47.7 49.6 45.8
VI 89.9 86.7 83.1 47.8 48.5 47.9 82.1 83.5 77.9 73.5 75.0 69.9 30.0 27.5 28.2
ID 84.7 84.3 80.7 48.3 50.2 48.9 74.1 79.6 73.6 69.6 73.7 68.1 43.8 47.0 42.2
Table 2: The moral reasoning accuracy rate of the LLMs
across the three moral branches (Virtue, Deontological,
Consequentialist).
We draw four main observations. (1) Even state-
of-the-art models such as the GPT series do
not produce consistent moral judgments across
languages. We conduct Mann-Whitney U tests
to measure statistical significance; most com-
parisons across languages fail to reach signifi-
cance, indicating inconsistency in multilingual
moral reasoning.
(2) LLMs generally perform
better in high-resource languages.
For exam-
ple, in ETHICSBASE, English accuracy ranges
from 86.48% to 96.49%, while Vietnamese (a
low-resource language) lags behind, with scores
ranging from 54.25% to 86.71%.
(3) Reason-
ing performance declines as context becomes
more complex—from ETHICSBASE (sentence-
level) to ETHICSPRO (paragraph-level). Interest-
ingly, performance improves again on ETHICSMAX
(document-level), likely because longer contexts
include explicit moral principles that help guide
the model’s decisions. This suggests that ambigu-
ity in short prompts may confuse models, whereas
explicit moral structure restores performance. (4)
In Table 2, performance across the three ethical
branches (Virtue, Deontological, Consequentialist)
in ETHICSMAX varies, but follows similar trends
across models and languages.
Dataset
Model Llama3EN Llama3ZH Llama3RU Llama3VI Llama3ID
ETHICSBASE-EN
94.2↑5.9
91.9↑3.6
91.2↑2.9
90.1↑1.8
91.5↑3.2
ETHICSBASE-ZH
81.5↑1.8
88.5↑8.8
81.8↑2.1
82.9↑3.2
83.7↑4.0
ETHICSBASE-RU
80.4↑4.2
83.0↑6.8
85.6↑9.4
81.2↑5.0
79.9↑3.7
ETHICSBASE-VI
65.5↑0.3
68.5↑3.3
80.3↑15.1
85.1↑19.9
81.4↑27.1
ETHICSBASE-ID
70.6↑7.6
60.0↑1.5
78.5↑15.5
78.1↑16.2
84.2↑21.2
ETHICSPRO-EN
84.6↑12.5
82.9↑10.8
84.6↑12.5
82.7↑10.6
84.5↑12.4
ETHICSPRO-ZH
72.2↑3.2
80.6↑11.6
72.3↑3.3
75.9↑6.9
79.0↑10.0
ETHICSPRO-RU
76.4↑11.8
79.9↑15.3
76.4↑11.8
75.7↑11.1
79.4↑14.8
ETHICSPRO-VI
64.4↑6.2
63.8↑5.6
64.4↑6.2
81.9↑23.7
80.7↑22.5
ETHICSPRO-ID
61.5↑4.4
71.4↑14.3
61.5↑4.4
77.8↑20.7
81.5↑24.4
Table 3: Monolingual alignment result.
Dataset
Model Llama3EN
Llama3ZH Llama3RU
Llama3VI
Llama3ID
ETHICSBASE-EN
80.2↓8.1
85.2↓3.1
83.4↓4.9
86.7↓1.6
86.1↓2.2
ETHICSBASE-ZH
72.4↓7.3
68.0↓11.7
72.0↓7.7
78.4↓1.3
73.2↓6.5
ETHICSBASE-RU
72.6↓3.6
70.9↓5.3
67.6↓8.6
76.1↓0.1
74.8↓1.4
ETHICSBASE-VI
61.3↓3.9
65.0↓0.2
61.7↓7.4
50.5↓14.7
61.4↓3.8
ETHICSBASE-ID
62.2↓0.8
55.4↓7.6
55.3↓7.7
58.1↓4.9
57.0↓6.0
ETHICSPRO-EN
62.90↓9.22
68.30↓3.82
68.04↓4.08
66.63↓5.49
71.18↓0.94
ETHICSPRO-ZH
62.80↓6.20
59.02↓9.98 59.40↓9.60
63.70↓5.30
62.80↓6.20
ETHICSPRO-RU
58.92↓5.68
58.80↓5.80
58.66↓5.94 57.90↓6.10
62.50↓2.10
ETHICSPRO-VI
56.96↓1.24
53.29↓4.91
49.50↓8.70
39.50↓18.70 35.90↓22.30
ETHICSPRO-ID
52.90↓4.20
50.85↓6.25
46.80↓10.30 45.10↓12.00 28.40↓28.70
Table 4: Monolingual poisoning result.
3.2.2
Monolingual Influence
As LLMs are increasingly used across diverse re-
gions and languages, ensuring consistent moral rea-
soning across linguistic boundaries becomes crit-
ical. However, low-resource languages often lack
high quality and a large amount of data, which may
impact the cross-lingual generalization of moral
reasoning. To understand this phenomenon, we
examine how fine-tuning a model on monolingual
data (either clean or corrupted) affects its perfor-
mance in other languages.
Monolingual Alignment.
We fine-tune the
model on high-quality, correctly labeled data from
a single language, then evaluate performance on the
remaining languages. As shown in Table 3, Indone-
sian fine-tuning yields the strongest improvements
across other languages, followed by Vietnamese.
These findings challenge the assumption that high-
resource languages are always the most effective
sources for cross-lingual transfer. On the contrary,
low-resource languages may induce stronger align-
ment effects due to their underrepresentation in
pretraining corpora, which allows fine-tuning to fill
in critical knowledge gaps.
Monolingual Poisoning.
We further test the sen-
sitivity of LLMs to data quality by fine-tuning the
model on corrupted labels in one language, then ob-
serving performance in others. Table 4 shows that
poisoning with Vietnamese data causes the most
3

--- Page 4 ---

0.2
0.4
0.6
0.8
EN
ZH
RU
VI
ID
EN
ZH
RU
VI
ID
EN
ZH
RU
VI
ID
EN
ZH
RU
VI
ID
EN
ZH
RU
VI
ID
ETHICS BASE
0.2
0.4
0.6
0.8
EN
ZH
RU
VI
ID
EN
ZH
RU
VI
ID
EN
ZH
RU
VI
ID
EN
ZH
RU
VI
ID
EN
ZH
RU
VI
ID
ETHICS PRO
0.2
0.4
0.6
0.8
EN
ZH
RU
VI
ID
EN
ZH
RU
VI
ID
EN
ZH
RU
VI
ID
EN
ZH
RU
VI
ID
EN
ZH
RU
VI
ID
ETHICS MAX
GPT-4
GPT-3.5
Llama3-70B
Llama3-8B
Mixtral-8x7B
Figure 1: The performance of three levels datasets across five LLMs in a multilingual setting.
0
20
40
60
80
100
VI
RU
RU
ZH
ZH
ZH
EN
EN
EN
EN
ID
ID
VI
ID
VI
RU
ID
VI
RU
ZH
Figure 2: The win-rate between five languages in
ETHICSPRO dataset based on Llama-3-8B.
degradation in multilingual performance, while En-
glish poisoning has minimal effect. This result
suggests that low-resource languages are not only
impactful in positive transfer (alignment) but also
particularly vulnerable to negative influence, likely
because harmful data in these languages is less
diluted during pretraining. These observations un-
derscore the importance of quality control in low-
resource language data used for training.
4
Discussion
Win-Rate Analysis.
Beyond overall accuracy,
we also examine pairwise win-rates between lan-
guages, as shown in Figure 2. This metric cap-
tures subtle differences in model behavior across
languages. Notably, while English benefits from
extensive pretraining data, it still fails to generalize
consistently in some moral reasoning cases, sug-
gesting that training data volume alone does not
guarantee robust moral understanding.
Model-wise Performance.
Figure 1 illustrates
the performance of all five LLMs across three
datasets and five languages. GPT-4 consistently
achieves the highest scores across all settings. In
contrast, LLaMA-3-8B struggles particularly with
sentence- and paragraph-level scenarios lacking
explicit ethical principles.
Its performance im-
proves markedly on ETHICSMAX, where structured
moral guidance is provided. Mistral-8x7B and
GPT-3.5 show comparable performance on com-
plex document-level tasks, indicating structured
ethical inputs can mitigate some model limitations.
The Role of Low-Resource Languages.
In Ta-
ble 3 and Table 4, low-resource languages play a
pivotal role in shaping multilingual model behav-
ior. On the one hand, high-quality data in these
languages can significantly enhance generalization
(alignment); on the other, corrupted or noisy data
can severely impair moral reasoning across lan-
guages (poisoning). These findings emphasize the
need for greater attention to data curation in under-
resourced languages.
5
Conclusion
We introduce a multilingual benchmark for eval-
uating moral reasoning in LLMs. Our results re-
veal cross-lingual inconsistencies and show that
low-resource languages have a strong impact (both
positive and negative) on multilingual performance.
These insights highlight the importance of data
quality in underrepresented languages.
4

--- Page 5 ---

Limitations
Despite the advances in assessing moral reasoning
capabilities of LLMs across multiple languages,
our study has limitations, including potential trans-
lation inaccuracies and model-specific performance
variability. Furthermore, the scope of moral sce-
narios tested may not fully encompass real-world
complexities, and additional research is needed to
generalize our findings across diverse contexts.
Ethics Statement
The ethical implications of fine-tuning LLMs, par-
ticularly regarding potential biases and fairness is-
sues, require careful consideration. We are com-
mitted to transparency, accountability, respect for
cultural diversity, and continuous improvement to
ensure the development and deployment of respon-
sible and ethical AI systems.
References
AI@Meta. 2024. Llama 3 model card.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. BERT: Pre-training of
deep bidirectional transformers for language under-
standing. In Proceedings of the 2019 Conference of
the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies, Volume 1 (Long and Short Papers), pages
4171–4186, Minneapolis, Minnesota. Association for
Computational Linguistics.
Denis Emelin, Ronan Le Bras, Jena D. Hwang, Maxwell
Forbes, and Yejin Choi. 2021. Moral stories: Situ-
ated reasoning about norms, intents, actions, and
their consequences. In Proceedings of the 2021 Con-
ference on Empirical Methods in Natural Language
Processing, pages 698–718, Online and Punta Cana,
Dominican Republic. Association for Computational
Linguistics.
Katharina Haemmerl,
Bjoern Deiseroth,
Patrick
Schramowski,
Jindˇrich
Libovický,
Constantin
Rothkopf, Alexander Fraser, and Kristian Kersting.
2023. Speaking multiple languages affects the moral
bias of language models. In Findings of the Asso-
ciation for Computational Linguistics: ACL 2023,
pages 2137–2156, Toronto, Canada. Association for
Computational Linguistics.
Dan Hendrycks, Collin Burns, Steven Basart, Andrew
Critch, Jerry Li, Dawn Song, and Jacob Steinhardt.
2020. Aligning ai with shared human values. arXiv
preprint arXiv:2008.02275.
Aditi Khandelwal, Utkarsh Agarwal, Kumar Tanmay,
and Monojit Choudhury. 2024. Do moral judgment
and reasoning capability of llms change with lan-
guage? a study using the multilingual defining issues
test. arXiv preprint arXiv:2402.02135.
Pingchuan Ma, Zongjie Li, Ao Sun, and Shuai Wang.
2023. "oops, did i just say that?" testing and re-
pairing unethical suggestions of large language mod-
els with suggest-critique-reflect process. Preprint,
arXiv:2305.02626.
OpenAI. 2023. Gpt-4. https://openai.com/gpt-4.
Abhinav Rao, Aditi Khandelwal, Kumar Tanmay,
Utkarsh Agarwal, and Monojit Choudhury. 2023a.
Ethical reasoning over moral alignment: A case and
framework for in-context ethical policies in llms.
arXiv preprint arXiv:2310.07251.
Abhinav Rao, Aditi Khandelwal, Kumar Tanmay,
Utkarsh Agarwal, and Monojit Choudhury. 2023b.
Ethical reasoning over moral alignment: A case and
framework for in-context ethical policies in LLMs.
In Findings of the Association for Computational
Linguistics: EMNLP 2023, pages 13370–13388, Sin-
gapore. Association for Computational Linguistics.
Nino Scherrer, Claudia Shi, Amir Feder, and David Blei.
2024. Evaluating the moral beliefs encoded in llms.
Advances in Neural Information Processing Systems,
36.
Zeerak Talat, Hagen Blix, Josef Valvoda, Maya Indira
Ganesh, Ryan Cotterell, and Adina Williams. 2022.
On the machine learning of ethical judgments from
natural language. In Proceedings of the 2022 Con-
ference of the North American Chapter of the Asso-
ciation for Computational Linguistics: Human Lan-
guage Technologies, pages 769–779. Association for
Computational Linguistics.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, and
Denny Zhou. 2023. Chain-of-thought prompting elic-
its reasoning in large language models. Preprint,
arXiv:2201.11903.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou,
et al. 2022. Chain-of-thought prompting elicits rea-
soning in large language models. Advances in neural
information processing systems, 35:24824–24837.
Yaowei Zheng, Richong Zhang, Junhao Zhang, Yanhan
Ye, and Zheyan Luo. 2024. Llamafactory: Unified
efficient fine-tuning of 100+ language models. arXiv
preprint arXiv:2403.13372.
Jingyan Zhou, Minda Hu, Junan Li, Xiaoying Zhang,
Xixin Wu, Irwin King, and Helen Meng. 2023. Re-
thinking machine ethics–can llms perform moral rea-
soning through the lens of moral theories?
arXiv
preprint arXiv:2308.15399.
Caleb Ziems, Jane A Yu, Yi-Chia Wang, Alon Halevy,
and Diyi Yang. 2022. The moral integrity corpus:
A benchmark for ethical dialogue systems. arXiv
preprint arXiv:2204.03021.
5

```
