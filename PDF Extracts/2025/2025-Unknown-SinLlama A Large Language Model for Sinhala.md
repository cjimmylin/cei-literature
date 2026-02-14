---
title: "2025-Aravinda-SinLlama A Large Language Model for Sinhala - PDF Extract"
source_pdf: "2025-Aravinda-SinLlama A Large Language Model for Sinhala.pdf"
pages: 6
extracted_at: "2026-02-13T09:50:28.828722"
---

# PDF Extract: 2025-Aravinda-SinLlama A Large Language Model for Sinhala

**Source PDF:** 2025-Aravinda-SinLlama A Large Language Model for Sinhala.pdf
**Total Pages:** 6

---

## Content

```
--- Page 1 ---

SinLlama - A Large Language Model for Sinhala
H.W.K.Aravinda∗, Rashad Sirajudeen∗, Samith Karunathilake∗,
Nisansa de Silva∗, Rishemjit Kaur†‡, Arshdeep Singh Bhankhar‡, Surangika Ranathunga§
∗Dept. of Computer Science & Engineering, University of Moratuwa, Sri Lanka.
{aravinda.20, rashad.20, samith.20, NisansaDds}@cse.mrt.ac.lk
†Central Scientific Instruments Organisation, Academy of Scientific and Innovative Research, Chandigarh, India.
rishemjit.kaur@csio.res.in
‡IIT Ropar Technology & Innovation Foundation (iHub - AWaDH), India & CSIR-CSIO Chandigarh, India
abhankhar_be20@thapar.edu
§School of Mathematical and Computational Sciences, Massey University, Auckland, New Zealand.
s.ranathunga@massey.ac.nz
Abstract—Low-resource languages such as Sinhala are often
overlooked by open-source Large Language Models (LLMs).
Therefore, it is imperative that the existing LLMs are further
trained to cover such languages. In this research, we extend an
existing multilingual LLM (Llama-3-8B) to get a better coverage
for Sinhala. We enhanced the LLM tokenizer with Sinhala
specific vocabulary and performed continual pre-training on a
10 million sentence Sinhala corpus, resulting in the SinLlama
model. This is the very first decoder-based open-source LLM
with explicit Sinhala support. When SinLlama was instruction
fine-tuned for three text classification tasks, it outperformed base
and instruct variants of Llama-3-8B by a significant margin.
Index Terms—Sinhala, low-resource languages, large language
models, continual pretraining, LLM, Llama, text classification
I. INTRODUCTION
Large Language Models (LLMs) such as ChatGPT have sig-
nificantly advanced the field of Natural Language Processing
(NLP) for languages with abundant training data and linguistic
resources. However, their support for low-resource languages
(LRLs) is significantly low. While some recent successful
open-source LLMs such as Llama [1] and Gemma [2] claim
to have multilingual support, such multilingual LLMs (mul-
tiLLMs) continue to under-perform on LRLs [3]. Given that
these LLMs are being created by large tech corporations, it is
fair to assume that the decision on which languages to include
in an LLM is driven by the perceived economic benefits in a
global scale. As such, there is a risk of LRLs continue to be
neglected, thus further increasing the digital divide between
communities.
Sinhala is an Indo-Aryan language, which is only being
used by a population of about 20 million in the island nation
of Sri Lanka [4]. According to Ranathunga and De Silva
[5]’s language categorization that uses the category definition
of Joshi et al. [6], Sinhala is a low-resource language. There
has been previous research that resulted in word embeddings
and encoder-based language models for Sinhala [7]. However,
techniques based on such models have become out-dated due
to the demonstrated potential of LLMs. However, Sinhala,
similar to many other LRLs, has not been considered during
pre-training of any of the popular open-source LLMs such as
Llama and Gemma released by the tech giants. While Sinhala
is included in MaLA-500 [8] and Aya-101 [9] released by
research teams, these models have not been able to outperform
models such as Llama. On the other hand, MaLA-500 and
Aya-101 models are large in size, incurring in large computer
memory requirements when used for downstream tasks.
To address these limitations, we present a focused adapta-
tion of a state-of-the-art multiLLM to better support Sinhala.
Our approach involves two key stages: (1) enhancing the
model’s tokenizer by merging Sinhala-specific tokens into
its vocabulary to improve subword segmentation; and (2)
conducting continual pretraining using a 10 million sentence
corpus that includes cleaned and diverse Sinhala text, ensuring
deeper linguistic representation.
We first carried out an investigation on the available open-
source LLMs to select the best performing LLM for Sinhala.
Llama-3 emerged as the most promising LLM. Then we
further pre-trained the Llama-3-8B model as mentioned above.
We term the resulting model, SinLlama1, which is publicly
released. In order to evaluate the performance of SinLlama
against the original Llama-3, we fine-tuned both with data
from three Sinhala benchmark datasetss [10]: writing-style
classification, news categorization and sentiment analysis. The
results show that when fine-tuned on Sinhala task-specific data,
SinLlama significantly outperforms both fine-tuned Llama-
base and Llama-instruct versions.
II. RELATED WORK
A. Large Language Models (LLMs)
Pre-trained Language Models (PLMs), created using the
Transformer architecture [11], have significantly advanced
the NLP landscape. Among them, decoder-only models such
as ChatGPT have become especially popular due to their
strong performance across a multitude of tasks. Open-source
large-scale decoder models, known as LLMs (e.g., LLaMA,
Mistral [12], Gemma), are also trained on larger datasets
and offer performance comparable to commercial systems.
Training an LLM has two primary stages: training a tokenizer
1https://huggingface.co/polyglots/SinLlama v01
arXiv:2508.09115v4  [cs.CL]  8 Nov 2025

--- Page 2 ---

and self-supervised training with an unlabeled raw text cor-
pus. The latter step is termed pre-training, and the resulting
model is termed a base model. However, such base models
lack task-specific capabilities. Therefore, these base models
should be fine-tuned with task-specific instruction data, which
is termed fine-tuning or instruct-tuning. The aforementioned
open-source LLMs are available in both base and instruct
versions.
B. Empirical Studies on LLM Performance for LRLs
The evaluation of LLMs across multiple languages reveals
significant performance disparities between high-resource and
LRLs. Ahuja et al. [13]’s MEGA framework conducted the
first comprehensive benchmarking of LLMs on 16 NLP tasks
across 70 diverse languages (including Sinhala) for comparing
the performance of different models on XLSUM dataset. They
showed that while models such as GPT-4 performed well in
high-resource languages, they struggle with LRLs, especially
those with unique morphological structures and/or scripts.
Recent surveys of LLMs underscore the influence of pre-
training data, language typology, and evaluation benchmarks
on model performance across languages. Chang et al. [14]
conducted a comprehensive review of over 200 LLMs, high-
lighting that multilingual performance is significantly affected
by the diversity and representativeness of the pretraining
corpus, with underrepresented languages, especially those with
complex morphology or distinct scripts, often exhibiting de-
graded results. The survey also emphasizes the limitations of
current multilingual benchmarks, which are either narrow in
task scope or limited in linguistic coverage, leading to an
incomplete understanding of LLM capabilities in low-resource
languages.
C. Extending LLMs for New Languages
There are several strategies to extend an LLM to an unseen
language.
• Continual Pre-training: This involves further training
an existing LLM on text data from the target language
to improve its language understanding and generation ca-
pabilities. Continued pre-training can improve alignment
with the new language, but may risk degrading perfor-
mance in previously learned languages if not carefully
managed [15].
• Vocabulary Extension: Adding new tokens specific to
the target language to the tokenizer’s vocabulary improves
encoding efficiency and model performance. Simple vo-
cabulary extension combined with continued pre-training
has been shown to be effective in various languages [16].
• Fine-tuning: Instruction tuning or task-specific fine-
tuning on data in the new language helps the model
adapt to language-specific nuances and tasks. Techniques
such as translation-assisted chain-of-thought fine-tuning
(TaCo) [17] have been proposed to improve cross-lingual
transfer for LRLs.
• Preference Optimization: This method optimizes the
model based on human preference data, which can be
scarce for LRLs. Preference optimization helps align
model output more closely with human expectations in
the new language context.
• In-context Learning: Providing relevant examples to
LLMs during inference is known as in-context learning
or few-shot learning. In-context learning has shown to
work in the context of LRLs as well [18].
• Leveraging Lexicons: Structured language-specific lin-
guistic resources such as lexicons can be integrated with
LLMs to boost their performance for LRLs [19]. Unlike
zero-shot methods, which often fail in domain-specific
settings, few-shot prompts enhance both accuracy and ef-
ficiency, marking a shift toward more adaptive strategies.
D. Sinhala Language Computing
While there has been research on implementing Sinhala
language computing tools, most of it has been done using
rule-based, statistical or early-generation deep learning tech-
niques [4]. In the NLP field, these techniques have long
become obsolete. Nevertheless, there have been some attempts
to keep Sinhala NLP up-to-date. Lakmal et al. [20] presented
Word2Vec and FastText embeddings for Sinhala and carried
out a detailed investigation. Dhananjaya et al. [7] built the
encoder-based language model SinBERT, by fine-tuning an
encoder-based Transformer [21] with 15.7 million Sinhala
sentences.
III. MODEL SELECTION
In the initial phase of our research, we aimed to identify the
most suitable open-source multiLLM, focusing on LRLs. The
first round of was carried out referring to empirical research
that compared open-source LLMs. This resulted in the fol-
lowing models: Llama-3-8B [1], MaLA-500 [8], Aya-101 [9],
PolyLM [22], XGLM, [23] Falcon [24], BLOOMZ [25],
Phi3 [26], Mistral [12], OPT [27], Aya-23 [9], and Big-
Trans [28]. These models are listed in Table I. Based on criteria
including multilingual capability, parameter size (fewer than
8 billion parameters)2, Sinhala language representation, and
performance metrics, we selected Llama-3-8B [1] for further
experimentation.
TABLE I: Model Details and Sinhala Language Support
Model
Parameters
Official
Sinhala Support
Number of
languages
Llama-3-8B
8B
No
8
MaLA-500
10.7B
Yes
534
Aya-101
13B
Yes
101
PolyLM-13B
13B
No
18
XGLM-7.5B
7.5B
Yes
30
Falcon-7B
7B
No
15
BLOOMZ-7.1B
7.1B
No
46
Phi-3-mini
3.8B
No
14
Mistral-7B
7B
No
10
OPT-66B
66B
No
5
Aya-23-8B
8B
No
23
BigTrans-13B
13B
Yes
102
2Model size has a direct relationship with the memory requirement in using
an LLM.

--- Page 3 ---

Llama-3-8B [1] officially supports 8 languages and is pre-
trained on a large dataset over 15 trillion data tokens, sourced
from publicly available Internet materials. It has 128K context
length. Lalama-3-8B outperformed its counterparts such as
Mistral 7B and Gemma 7B on common benchmarks such as
MMLU [29], ARC [30], DROP [31] and GPQA [32].
IV. DATASET
A. Pre-training Data
Pre-training of an LLM has to be done with a substantially
large dataset, in order to guarantee it learns the language-
specific information. Therefore, we created a dataset by
combining MADLAD-400 [33] and CulturaX [34] for the
Sinhala language3. MADLAD-400 is a manually audited,
general-domain 3 Trillion token monolingual dataset based
on CommonCrawl [36], spanning 419 languages. CulturaX
is a multilingual dataset with 6.3 Trillion tokens in 167
languages. Although both have been cleaned, there were
some entries that contained non-Sinhala words. Because of
that, heuristics-based filtering [37] was applied to remove
such noisy sentences. These include rules such as minimum
sentence length, non-Sinhala sentence removal, exclusion
of sentences with irregular punctuation, and elimination of
URLs and numeric prefixes.For the pre-training, we com-
bined both datasets and removed duplicates. Our final dataset
contains 10,730,154 (10.7M) Sinhala sentences, comprising
303,958,959 (303.96M) tokens. This dataset is publicly re-
leased4.
B. Fine-tuning Data
For the supervised fine-tuning experiments, we focused on
Sinhala text classification tasks. We selected three publicly
available datasets: News Category Classification [38], Senti-
ment Analysis [39], and Writing Style Classification [7].These
datasets collectively represent a diverse range of linguistic
features and styles, making them suitable for evaluating the
effectiveness of LLMs for Sinhala.
Since the original datasets were not in a directly usable
format for fine-tuning, several preprocessing steps were per-
formed. The Sentiment classification dataset, originally in
XML format, required extraction of relevant fields: content
within the <phrase> tag was used as the input text, and
the <sentiment> tag provided the corresponding label. For
other datasets, we only applied standard text cleaning proce-
dures such as deduplication, removal of malformed entries,
and whitespace normalization.
To enable robust evaluation, we manually split each dataset
into training, validation, and test sets using an 80:10:10 ratio.
We employed stratified sampling to ensure that each split
preserved the original label distribution, thereby preventing
skewed performance metrics. The final dataset sizes used for
fine-tuning are shown in Table II.
3The dataset created by Dhananjaya et al. [7] is no longer accessible.
According to Ranathunga et al. [35], this is a common problem in LRL
domain.
4https://huggingface.co/datasets/polyglots/MADLAD CulturaX cleaned
TABLE II: Dataset sizes for Text Classificiation Task
Dataset
Train
Test
Validation
Sentiment analysis [39]
10010
1252
1252
Writting style classification [7]
7238
905
905
Sinhala news category classification [38]
2661
333
333
V. CONTINUAL PRETRAINING TO BUILD SINLLAMA
We used vocabulary extension and continuous pre-training
(see Section II-C) on Llama-3-8B to create SinLlama. We
trained a tokenizer using the pre-training corpus using tik-
token5, and merged this tokenizer with the Llama 3 tokenizer.
We used this extended tokenizer and performed continual
pretraining using the codebase from Chinese-Llama [40].
The only modification made to the original Chinese-Llama
hyperparameters was the reduction of the block_size from
1024 to 5126.
VI. TASK-SPECIFIC FINETUNING
A. Prompt Selection
For both inference and supervised fine-tuning, it was es-
sential to select the most effective prompt templates from the
available datasets. We adopted the prompt format introduced
by the Alpaca Instruct Template [41] as in Fig. 1. To identify
the most suitable prompts for each classification task, we
referred to the work by Ahuja et al. [13], which provided
well-designed prompts for several tasks.
Fig. 1: Prompt template for supervised fine-tuning
B. Fine-tuning
We fine-tuned SinLlama and the Llama-3-8B base model
separately with the training split of each dataset mentioned in
Section IV-B, creating a set of task-specific fine-tuned models.
We used LoRA fine-tuning [42], which enables faster training
and lower memory usage.
Figure 2 shows an example experimental setup for one
dataset; we followed a similar process for other datasets.
5https://github.com/openai/tiktoken
6Larger block sizes cause memory allocation issues on the GPUs we used,
preventing successful model loading.

--- Page 4 ---

TABLE III: Performance Comparison Across Tasks
Model
Writing Style
News Category
Sentiment Tagger
Precision
Recall
F1
Precision
Recall
F1
Precision
Recall
F1
Llama-3-8B base
33.091
20.927
24.504
23.904
18.919
19.031
41.942
38.011
36.285
Llama-3-8B base - Finetuned
71.060
38.179
49.451
64.770
63.664
61.136
61.110
61.215
59.353
Llama-3-8B instruct
50.782
50.719
48.755
31.866
30.330
29.219
48.451
36.796
31.257
Llama-3-8B instruct - Finetuned
70.996
35.942
42.256
50.883
50.450
47.812
68.856
68.729
68.784
SinLlama
33.315
4.393
7.531
44.166
19.520
15.614
47.153
25.856
22.689
SinLlama - Finetuned
85.906
52.157
58.893
89.033
86.787
86.402
75.246
70.055
72.471
Fig. 2: An example experimental setup for the Writing Style
Classification dataset.
VII. EVALUATION
We used Llama-3-8B base original model, Llama-3-8B-
instruct original model, and their fine-tuned (with our data)
versions, as the baselines. From the results of table III, we can
identify that the fine-tuned SinLlama model performs best at
each of the task with a significantly high margin. When the
Llama-3-8B base model is fine-tuned with our dataset, there is
a significant gain over the base model. However, this result is
far below the fine-tuned SinLlama model. Fine-tuned Llama-3-
8B instruct model also outperforms its un-fine-tuned version.
However, it falls below the fine-tuned Llama-3-8B base model,
which is surprising. Overall, the writing style classification
task seems to be the most difficult for the LLMs. Because the
input field of that dataset is much larger than those of the other
two datasets.
VIII. CONCLUSION
Although Sinhala has been included in several multilingual
pre-trained large language models, it was not intentionally
targeted during the pre-training phase. In this study, we
introduce SinLlama, the first-ever large language model pre-
trained specifically for Sinhala. Our results demonstrate that
fine-tuning SinLlama with Sinhala task-specific data results in
significant gains compared to fine-tuning Llama-3-8B base and
instruct models. In the future, we plan to conduct experiments
on several fine-tuning strategies and preference optimization
methods.
ACKNOWLEDGMENT
We thank CSIR - Central Scientific Instruments Organiza-
tion, India, and Emojot (Pvt) Ltd for providing the computing
resources.
REFERENCES
[1] A. Grattafiori, A. Dubey, A. Jauhri, A. Pandey, A. Ka-
dian, A. Al-Dahle, A. Letman, A. Mathur, A. Schelten,
A. Vaughan et al., “The llama 3 herd of models,” arXiv
preprint arXiv:2407.21783, 2024.
[2] G. Team, T. Mesnard, C. Hardin, R. Dadashi, S. Bhupati-
raju, S. Pathak, L. Sifre, M. Rivi`ere, M. S. Kale, J. Love
et al., “Gemma: Open models based on gemini research
and technology,” arXiv preprint arXiv:2403.08295, 2024.
[3] X. Zhang, S. Li, B. Hauer, N. Shi, and G. Kondrak,
“Don‘t trust ChatGPT when your question is not in
English: A study of multilingual abilities and types
of LLMs,” in Proceedings of the 2023 Conference on
Empirical Methods in Natural Language Processing,
H. Bouamor, J. Pino, and K. Bali, Eds.
Singapore:
Association for Computational Linguistics, Dec. 2023,
pp. 7915–7927. [Online]. Available: https://aclanthology.
org/2023.emnlp-main.491/
[4] N. De Silva, “Survey on publicly available sinhala natural
language processing tools and research,” arXiv preprint
arXiv:1906.02358v25, 2025.
[5] S. Ranathunga and N. De Silva, “Some languages are
more equal than others: Probing deeper into the linguistic
disparity in the nlp world,” in Proceedings of the 2nd
Conference of the Asia-Pacific Chapter of the Association
for Computational Linguistics and the 12th International
Joint Conference on Natural Language Processing (Vol-
ume 1: Long Papers), 2022, pp. 823–848.
[6] P.
Joshi,
S.
Santy,
A.
Budhiraja,
K.
Bali,
and
M. Choudhury, “The state and fate of linguistic diversity
and inclusion in the NLP world,” in Proceedings
of
the
58th
Annual
Meeting
of
the
Association
for Computational Linguistics, D. Jurafsky, J. Chai,
N. Schluter, and J. Tetreault, Eds.
Online: Association
for Computational Linguistics, Jul. 2020, pp. 6282–
6293. [Online]. Available: https://aclanthology.org/2020.
acl-main.560/
[7] V.
Dhananjaya,
P.
Demotte,
S.
Ranathunga,
and
S. Jayasena, “Bertifying sinhala–a comprehensive anal-
ysis of pre-trained language models for sinhala text
classification,” arXiv preprint arXiv:2208.07864, 2022.
[8] P. Lin, S. Ji, J. Tiedemann, A. F. Martins, and H. Sch¨utze,
“Mala-500: Massive language adaptation of large lan-
guage models,” arXiv preprint arXiv:2401.13303, 2024.
[9] A.
¨Ust¨un,
V.
Aryabumi,
Z.-X.
Yong,
W.-Y.
Ko,
D. D’souza, G. Onilude, N. Bhandari, S. Singh, H.-L.

--- Page 5 ---

Ooi, A. Kayid et al., “Aya model: An instruction fine-
tuned open-access multilingual language model,” arXiv
preprint arXiv:2402.07827, 2024.
[10] A. Wang, A. Singh, J. Michael, F. Hill, O. Levy, and
S. R. Bowman, “Glue: A multi-task benchmark and
analysis platform for natural language understanding,”
arXiv preprint arXiv:1804.07461, 2018.
[11] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit,
L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin,
“Attention is all you need,” Advances in neural informa-
tion processing systems, vol. 30, 2017.
[12] A. Q. Jiang, A. Sablayrolles, A. Mensch, C. Bamford,
D. S. Chaplot, D. de las Casas, F. Bressand, G. Lengyel,
G. Lample, L. Saulnier, L. R. Lavaud, M.-A. Lachaux,
P. Stock, T. L. Scao, T. Lavril, T. Wang, T. Lacroix, and
W. E. Sayed, “Mistral 7b,” 2023. [Online]. Available:
https://arxiv.org/abs/2310.06825
[13] K. Ahuja, H. Diddee, R. Hada, M. Ochieng, K. Ramesh,
P. Jain, A. Nambi, T. Ganu, S. Segal, M. Axmed et al.,
“Mega: Multilingual evaluation of generative ai,” arXiv
preprint arXiv:2303.12528, 2023.
[14] Y. Chang, X. Wang, J. Wang, Y. Wu, L. Yang, K. Zhu,
H. Chen, X. Yi, C. Wang, Y. Wang et al., “A survey on
evaluation of large language models,” ACM transactions
on intelligent systems and technology, vol. 15, no. 3, pp.
1–45, 2024.
[15] A. Cossu, A. Carta, L. Passaro, V. Lomonaco, T. Tuyte-
laars, and D. Bacciu, “Continual pre-training mitigates
forgetting in language and vision,” Neural Networks, vol.
179, p. 106492, 2024.
[16] C. Toraman, “Llamaturk: Adapting open-source genera-
tive large language models for low-resource language,”
arXiv preprint arXiv:2405.07745, 2024.
[17] B. Upadhayay and V. Behzadan, “Taco: Enhancing
cross-lingual transfer for low-resource languages in llms
through translation-assisted chain-of-thought processes,”
arXiv preprint arXiv:2311.10797, 2023.
[18] Y. Moslem, R. Haque, J. D. Kelleher, and A. Way, “Adap-
tive machine translation with large language models,”
arXiv preprint arXiv:2301.13294, 2023.
[19] F. Koto, T. Beck, Z. Talat, I. Gurevych, and T. Baldwin,
“Zero-shot sentiment analysis in low-resource languages
using a multilingual sentiment lexicon,” arXiv preprint
arXiv:2402.02113, 2024.
[20] D. Lakmal, S. Ranathunga, S. Peramuna, and I. Herath,
“Word embedding evaluation for sinhala,” in Proceed-
ings of the Twelfth Language Resources and Evaluation
Conference, 2020, pp. 1874–1881.
[21] Y. Liu, M. Ott, N. Goyal, J. Du, M. Joshi, D. Chen,
O. Levy, M. Lewis, L. Zettlemoyer, and V. Stoyanov,
“Roberta: A robustly optimized bert pretraining ap-
proach,” arXiv preprint arXiv:1907.11692, 2019.
[22] X. Wei, H. Wei, H. Lin, T. Li, P. Zhang, X. Ren,
M. Li, Y. Wan, Z. Cao, B. Xie et al., “Polylm: An open
source polyglot large language model,” arXiv preprint
arXiv:2307.06018, 2023.
[23] J. Li, H. Zhou, S. Huang, S. Cheng, and J. Chen,
“Eliciting the translation ability of large language models
via multilingual finetuning with translation instructions,”
Transactions of the Association for Computational Lin-
guistics, vol. 12, pp. 576–592, 2024.
[24] E. Almazrouei, H. Alobeidli, A. Alshamsi, A. Cappelli,
R. Cojocaru, M. Debbah, ´E. Goffinet, D. Hesslow, J. Lau-
nay, Q. Malartic et al., “The falcon series of open lan-
guage models,” arXiv preprint arXiv:2311.16867, 2023.
[25] N. Muennighoff, T. Wang, L. Sutawika, A. Roberts,
S. Biderman, T. L. Scao, M. S. Bari, S. Shen, Z.-
X. Yong, H. Schoelkopf et al., “Crosslingual gener-
alization through multitask finetuning,” arXiv preprint
arXiv:2211.01786, 2022.
[26] M. Abdin, J. Aneja, H. Awadalla, A. Awadallah, A. A.
Awan, N. Bach, A. Bahree, A. Bakhtiari, J. Bao, H. Behl
et al., “Phi-3 technical report: A highly capable lan-
guage model locally on your phone,” arXiv preprint
arXiv:2404.14219, 2024.
[27] S. Zhang, S. Roller, N. Goyal, M. Artetxe, M. Chen,
S. Chen, C. Dewan, M. Diab, X. Li, X. V. Lin et al.,
“Opt: Open pre-trained transformer language models,”
arXiv preprint arXiv:2205.01068, 2022.
[28] W. Yang, C. Li, J. Zhang, and C. Zong, “Bigtranslate:
Augmenting large language models with multilingual
translation capability over 100 languages. arxiv 2023,”
arXiv preprint arXiv:2305.18098.
[29] D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika,
D.
Song,
and
J.
Steinhardt,
“Measuring
massive
multitask
language
understanding,”
arXiv
preprint
arXiv:2009.03300, 2020.
[30] P. Clark, I. Cowhey, O. Etzioni, T. Khot, A. Sabharwal,
C. Schoenick, and O. Tafjord, “Think you have solved
question answering? try arc, the ai2 reasoning challenge,”
arXiv preprint arXiv:1803.05457, 2018.
[31] D. Dua, Y. Wang, P. Dasigi, G. Stanovsky, S. Singh,
and M. Gardner, “Drop: A reading comprehension
benchmark requiring discrete reasoning over paragraphs,”
arXiv preprint arXiv:1903.00161, 2019.
[32] D. Rein, B. L. Hou, A. C. Stickland, J. Petty, R. Y.
Pang, J. Dirani, J. Michael, and S. R. Bowman, “Gpqa:
A graduate-level google-proof q&a benchmark,” in First
Conference on Language Modeling, 2024.
[33] S. Kudugunta, I. Caswell, B. Zhang, X. Garcia, D. Xin,
A. Kusupati, R. Stella, A. Bapna, and O. Firat, “Madlad-
400: A multilingual and document-level large audited
dataset,” Advances in Neural Information Processing
Systems, vol. 36, pp. 67 284–67 296, 2023.
[34] T. Nguyen, C. Van Nguyen, V. D. Lai, H. Man, N. T.
Ngo, F. Dernoncourt, R. A. Rossi, and T. H. Nguyen,
“Culturax: A cleaned, enormous, and multilingual dataset
for large language models in 167 languages,” arXiv
preprint arXiv:2309.09400, 2023.
[35] S. Ranathunga, N. de Silva, D. Jayakody, and A. Fer-
nando, “Shoulders of Giants: A Look at the Degree and
Utility of Openness in NLP Research,” in Proceedings

--- Page 6 ---

of the 62nd Annual Meeting of the Association for
Computational Linguistics, 2024.
[36] J. M. Patel, “Introduction to common crawl datasets,”
in Getting structured data from the internet: running
web crawlers/scrapers on a big data production scale.
Springer, 2020, pp. 277–324.
[37] A. Fernando, S. Ranathunga, and N. de Silva, “Improving
the quality of web-mined parallel corpora of low-resource
languages using debiasing heuristics,” arXiv preprint
arXiv:2502.19074, 2025.
[38] N. de Silva, “Sinhala text classification: observations
from the perspective of a resource poor language,” Re-
searchGate, 2015.
[39] S. Ranathunga and I. U. Liyanage, “Sentiment analy-
sis of sinhala news comments,” Transactions on Asian
and Low-Resource Language Information Processing,
vol. 20, no. 4, pp. 1–23, 2021.
[40] Y. Cui, Z. Yang, and X. Yao, “Efficient and effective text
encoding for chinese llama and alpaca,” arXiv preprint
arXiv:2304.08177, 2023.
[41] P. Chen, S. Ji, N. Bogoychev, A. Kutuzov, B. Haddow,
and K. Heafield, “Monolingual or multilingual instruc-
tion tuning: Which makes a better alpaca,” arXiv preprint
arXiv:2309.08958, 2023.
[42] E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang,
L. Wang, W. Chen et al., “Lora: Low-rank adaptation of
large language models.” ICLR, vol. 1, no. 2, p. 3, 2022.
APPENDIX A
PROMPTS USED
All of the prompts used for the benchmark process referred
to the prompts given from the Ahuja et al. [13]. Selected
prompts are given below.
A. Writing-style-classification
Feature columns in the dataset are “comments”, “labels”.
You are an NLP assistant whose purpose is to classify
Sinhala comments into predefined categories. The
categories are as follows: ACADEMIC, CREATIVE, NEWS,
BLOG. Given a Sinhala comment, your task is to
determine which category it belongs to. Choose one
category: ACADEMIC, CREATIVE, NEWS, or BLOG. Answer
must match exactly in capitalization and formatting.
Comment: {comment}
Answer:
B. Sentiment-tagger
The original dataset consist of XML tags. After the process-
ing we created a dataset with the following features. Feature
columns in the dataset are “context”, “text”, “sentiment”.
You are an NLP assistant whose purpose is to solve
Sentiment Analysis problems. Sentiment Analysis is
the task of determining whether the sentiment,
opinion or emotion expressed in a textual data is.
Does the following Sinhala sentence have a POSITIVE,
NEGATIVE or NEUTRAL sentiment? {text}. Give only
the POSITIVE, NEGATIVE, or NEUTRAL as the answer in
one word.
C. Sinhala-News-Category-classification
Feature columns in the dataset are “comments”, “labels”.
You are an NLP assistant whose purpose is to classify
Sinhala comments into predefined categories. The
categories are as follows: (Political: 0, Business: 1,
Technology: 2, Sports: 3, Entertainment: 4) Given a
Sinhala comment, your task is to determine which
category it belongs to. Please only give the label
as a number (0, 1, 2, 3, or 4) that best represents
the comment’s category. comment: {text} answer:

```
