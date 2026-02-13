---
title: "2025-Roussis-Krikri Advancing Open Large Language Models for Greek - PDF Extract"
source_pdf: "2025-Roussis-Krikri Advancing Open Large Language Models for Greek.pdf"
pages: 26
extracted_at: "2026-02-13T13:14:01.379712"
---

# PDF Extract: 2025-Roussis-Krikri Advancing Open Large Language Models for Greek

**Source PDF:** 2025-Roussis-Krikri Advancing Open Large Language Models for Greek.pdf
**Total Pages:** 26

---

## Content

```
--- Page 1 ---

arXiv:2505.13772v2  [cs.CL]  30 May 2025
Krikri: Advancing Open Large Language Models for Greek
Dimitris Roussis*, Leon Voukoutis*, Georgios Paraskevopoulos*,
Sokratis Sofianopoulos*, Prokopis Prokopidis*, Vassilis Papavasileiou,
Athanasios Katsamanis, Stelios Piperidis, Vassilis Katsouros*
Institute for Speech and Language Processing, Athena Research Center
Artemidos 6 & Epidavrou, Athens, Greece
vsk@athenarc.gr
Abstract
We introduce Llama-Krikri-8B, a cutting-edge
Large Language Model tailored for the Greek
language, built on Meta’s Llama 3.1-8B. Llama-
Krikri-8B has been extensively trained on high-
quality Greek data to ensure superior adapta-
tion to linguistic nuances. With 8 billion param-
eters, it offers advanced capabilities while main-
taining efficient computational performance.
Llama-Krikri-8B supports both Modern Greek
and English, and is also equipped to handle
polytonic text and Ancient Greek. The chat ver-
sion of Llama-Krikri-8B features a multi-stage
post-training pipeline, utilizing both human and
synthetic instruction and preference data cre-
ated via various synthesis techniques, such as
MAGPIE, in order to address the issue of data
scarcity for Greek. In addition, for evaluation,
we propose three novel public benchmarks for
Greek which are suitable for instruction-tuned
models. Our evaluation on existing as well as
the proposed benchmarks shows notable im-
provements over comparable Greek and multi-
lingual LLMs in both natural language under-
standing and generation as well as tasks related
to math, code, instruction-following, etc.
1
Introduction
Recent advancements in AI have been largely
driven by the development of large-scale founda-
tion models. Meta’s Llama 3 (Grattafiori et al.,
2024) fostered a new generation of open models,
designed for strong multilingual capabilities, code
generation, reasoning, and tool use. With extended
context windows, and refined training strategies,
models based on Llama 3 have achieved perfor-
mance comparable to proprietary systems like GPT-
4. A critical aspect in this evolution is the develop-
ment of multilingual and language-specific models,
democratizing access to AI technologies and pre-
serving linguistic diversity.
*Equal contribution
While substantial progress has been made for
widely spoken languages, low and medium re-
source languages remain underrepresented. Greek,
in particular, has received limited attention de-
spite its linguistic complexity, rich cultural her-
itage, and historical significance. Addressing this
gap, we present Llama-Krikri-8B, a cutting-edge
open Large Language Model tailored for the Greek
language. Built on Meta’s Llama 3.1-8B architec-
ture, Llama-Krikri has been continually pretrained
on a diverse, high-quality Greek corpus. This al-
lows the model to effectively capture the syntactic
and semantic nuances of Greek, while retaining the
multilingual strengths of the base model. Notably,
Llama-Krikri also supports English and is capable
of handling polytonic and Ancient Greek texts, ad-
dressing not only contemporary but also historical
forms of the language.
Compared to Meltemi-7B (Voukoutis et al.,
2024), the previous state-of-the-art open Greek
LLM built on Mistral 7B (Jiang et al., 2023),
Llama-Krikri-8B significantly increases the num-
ber of parameters, context length, and training data
scale. Additionally, it features an enhanced post-
training pipeline using both human and synthetic
data. By utilizing various data synthesis method-
ologies, such as MAGPIE (Xu et al., 2024), we
generate high-quality synthetic data for Supervised
Fine-Tuning (SFT) and alignment via Direct Pref-
erence Optimization (DPO) (Rafailov et al., 2024).
This pipeline addresses the scarcity of relevant data
for Greek and ensures that the model produces help-
ful, honest, and harmless outputs.
To evaluate Llama-Krikri-8B, we also intro-
duce three novel public benchmarks specifically de-
signed for Greek instruction-tuned models. These,
alongside existing evaluation suites, show that
Llama-Krikri outperforms comparable Greek and
multilingual LLMs in both natural language un-
derstanding and generation, as well as other chal-
lenging tasks related to math, code, instruction-

--- Page 2 ---

following, etc. Moreover, it supports function call-
ing and agentic behavior, opening new applica-
tion domains for Greek users. Llama-Krikri-8B
is available under the Llama 3.1 Community Li-
cense Agreement1.
Our key contributions are:
• We present Llama-Krikri-8B, a state-of-the-
art open Greek foundation model based on
Llama 3.1, demonstrating strong capabilities
in Modern and Ancient Greek, math, code,
instruction-following, etc., while also support-
ing function calling and agentic behavior.
• We incorporate additional steps aiming to in-
crease efficiency, reduce training costs, and
improve performance, such as expanding the
original Llama 3.1 tokenizer and embeddings,
and conducting an annealing phase with high-
quality and synthetic data.
• We collect and curate a large pretraining cor-
pus and utilize synthetic data creation strate-
gies for post-training, in order to address the
scarcity of Greek data.
• We implement a multi-step post-training
pipeline
incorporating
Supervised
Fine-
Tuning (SFT) and alignment through Di-
rect Preference Optimization (DPO), which
leads to Llama-Krikri-8B-Instruct surpass-
ing Llama-3.1-8B-Instruct in several English
tasks.
• We introduce three new benchmarks for eval-
uating instruction-tuned Greek LLMs, cov-
ering instruction-following, multi-turn chats,
code/math tasks, etc.
• We show that Llama-Krikri-8B and Llama-
Krikri-8B-Instruct significantly outperform
existing open multilingual models in Greek
tasks across several domains, while also being
competitive with 3-4 times larger models.
2
Background and Related Work
Large Language Models (LLMs) have achieved
state-of-the-art performance across a wide vari-
ety of natural language processing (NLP) tasks.
These models are typically trained on massive cor-
pora dominated by English, leading to strong per-
formance in English-language tasks but compara-
1https://www.llama.com/llama3_1/license/
tively weaker capabilities in other languages (De-
vlin et al., 2019; Brown et al., 2020). As a result,
the development of language-specific LLMs has
become an active area of research, particularly for
under-represented languages.
One prominent strategy for developing such
models is continual pretraining, where a pretrained
base model is further trained on data in the tar-
get language. This approach allows researchers
to leverage the general capabilities of large base
models while improving performance in specific
linguistic domains, without the prohibitive cost of
training from scratch (Gururangan et al., 2020).
Several recent projects have successfully applied
continual pretraining to adapt existing models to
new languages. BgGPT-GEMMA-2-27B-Instruct
(Alexandrov et al., 2024) fine-tunes Google’s
Gemma-2 model (Riviere et al., 2024) for Bul-
garian, combining over 100B tokens of Bulgarian
and English data and applying techniques such as
Branch-and-Merge to mitigate catastrophic forget-
ting. Similarly, LeoLM (LAION, 2023) adapts
a Llama-based architecture for German, while the
Sabiá (Pires et al., 2023) and Bielik models (Ociepa
et al., 2024) adapt Mistral-based architectures for
Portuguese and Polish respectively, through tar-
geted continual pretraining and post-training.
For Greek, Meltemi-7B represents the first open
generative LLM tailored to the language (Vouk-
outis et al., 2024). It was developed by continually
pretraining Mistral-7B on a substantial Greek cor-
pus, followed by instruction fine-tuning. While
effective, Meltemi’s performance is bounded by
the size and capabilities of the base model, data
scarcity for instruction tuning in Greek, as well
as the limited post-training alignment techniques
employed at the time.
Beyond language adaptation, alignment of
LLMs to generate helpful, harmless, and honest
outputs has become increasingly central. Early ap-
proaches such as InstructGPT (Ouyang et al., 2022)
and Constitutional AI (Bai et al., 2022) rely on
multi-stage fine-tuning pipelines involving human
feedback or rule-based constraints. More recently,
DPO and data synthesis methods like MAGPIE
have enabled scalable and effective post-training.
MAGPIE, in particular, leverages already-aligned
models to generate large volumes of instruction-
response pairs, demonstrating that synthetic data
can rival or surpass human-curated datasets.
These advancements highlight a trend toward
bootstrapping high-quality training data using

--- Page 3 ---

strong base models, especially in low-resource lan-
guages. Our work builds on this foundation by em-
ploying Llama 3.1 as a base architecture, employ-
ing various data synthesis techniques (e.g., MAG-
PIE), and applying a more rigorous post-training
pipeline, including DPO for alignment.
3
Methodology
Llama-Krikri-8B is based on the Transformer archi-
tecture (Vaswani et al., 2023), which has become
the de facto standard for large language models.
The model inherits its architecture from Meta’s
Llama 3.1-8B, leveraging the strong foundation in
multilingual understanding, code generation, and
reasoning provided by Llama 3.1.
Adapting an LLM for the Greek language re-
quires addressing the lack of high-quality Greek
data in the massive datasets typically used to train
foundation models. Even though Llama 3.1’s pre-
training corpus comprises trillions of tokens, it
struggles to generate coherent Greek text, thus in-
dicating that Greek data is only a tiny fraction of
its training data; we should note however that there
is limited information on the composition of its
pretraining data (Grattafiori et al., 2024). Our ap-
proach is to perform continual pretraining with
Greek and parallel data to infuse the model with
Greek knowledge. This training must be done care-
fully to avoid catastrophic forgetting (Luo et al.,
2025) of the base model’s prior knowledge in other
languages and domains, and it must also be fol-
lowed by post-training in order to ensure that the
model follows instructions adequately and safely.
In the subsections below, we detail our compre-
hensive methodology for developing Llama-Krikri-
8B. We begin by describing our process for col-
lecting, filtering, and cleaning a diverse corpus
of Greek text supplemented with English, paral-
lel, and domain-specific content (§3.1). Next, we
explain how we expanded the tokenizer to better
handle Greek text (§3.2) and initialized the corre-
sponding embeddings (§3.3). We then detail our
continual pretraining procedure that extends the
base model while preserving its original capabili-
ties (§3.4), followed by an annealing phase using
high-quality curated data to further refine perfor-
mance (§3.5). Finally, we describe our instruc-
tion tuning pipeline, which includes supervised
fine-tuning and preference optimization to align
the model with human values (§3.6). This com-
prehensive approach addresses both the technical
challenges of adapting a multilingual foundation
model for Greek while ensuring the resulting model
maintains its general capabilities and even outper-
forms the instruction-tuned variant of Llama-3.1-
8B across several tasks.
3.1
Pretraining Data Collection & Cleaning
As a foundation for continual pretraining, we cu-
rated a large corpus of texts totalling approximately
91 billion tokens (after filtering and deduplication),
which was upsampled to 110 billion tokens for
the final pretraining mix. This corpus was con-
structed with a primary focus on Greek by uti-
lizing sources such as Wikipedia2, Wikisource3,
Project Gutenberg4, governmental documents, aca-
demic repositories, literature, and other openly
available datasets. We also included Ancient Greek
texts (as well as other variants of Greek), high-
quality English texts, parallel datasets in language
pairs encompassing Greek, English, French, Ger-
man, Portuguese, Italian, and Spanish, as well as
datasets containing math and code, so as to retain
or even improve the model’s existing capabilities.
The distribution included 56.7 billion monolingual
Greek tokens (62.3%), 21 billion monolingual En-
glish tokens (23.1%), 5.5 billion parallel data to-
kens (6.0%), and 7.8 billion math and code tokens
(8.6%). Table 1 presents the distribution of the pre-
training data mix, with more details provided in
Appendix A.1 Pretraining Data Mix.
After corpus collection, we implemented a multi-
stage preprocessing and filtering pipeline to ensure
a high quality for the pretraining data. Various parts
of our filtering methodology have been informed
by approaches used in previous work Voukoutis
et al. (2024) and large-scale corpus creation efforts
such as Zyda (Tokpanov et al., 2024). However, we
have adapted these approaches to cater for the pecu-
liarities of the Greek language, as well as different
data types, including PDF extraction for academic
and legal texts, rule-based filtering for web content,
and model-based quality assessment for parallel
data using LASER (Artetxe and Schwenk, 2018,
2019) and CometKiwi (Rei et al., 2022). Other
cleaning approaches aim for privacy protection via
the anonymization of personally identifiable infor-
mation, for increased training efficiency via dedu-
plication, and for assigning higher importance to
important or more educational content (e.g., le-
2https://huggingface.co/datasets/wikimedia/wikipedia
3https://huggingface.co/datasets/wikimedia/wikisource
4https://www.gutenberg.org/

--- Page 4 ---

Original
Upsampled
Subcorpus
Tokens (B)
Percentage
Tokens (B)
Percentage
Greek
56.7
62.3%
66.1
60.0%
English
21.0
23.1%
25.2
22.9%
Parallel
5.5
6.0%
8.8
8.0%
Math/Code
7.8
8.6%
10.1
9.1%
Total
91.0
100%
110.2
100%
Table 1: Composition of the pretraining corpus - original and upsampled
gal, scientific, medical, translation) via upsampling
(Carlini et al., 2023; Tang et al., 2024). We detail
the preprocessing pipelines we used in Appendix
A.2 Pretraining Data Cleaning Pipelines.
3.2
Tokenizer Expansion
The original Llama 3 tokenizer comprises 128, 000
tokens and is inefficient for Greek texts, as it gen-
erally performs character-level tokenization for
Greek. This was determined, through the approxi-
mation of the Llama-3.1 tokenizer’s fertility (Csaki
et al., 2023), a metric of the average tokens per
word produced. To determine the efficiency of
the original Llama 3 tokenizer and compare with
our approach, we conducted tests on diverse Greek
and English corpora (each one containing 100, 000
rows and totalling approximately 2M words) and
calculated the difference in fertility, as can be seen
in Table 2. We observe that the Llama-3.1-8B to-
kenizer exhibits a fertility of 2.73 for Greek and
1.33 for English. Our Llama-Krikri-8B tokenizer
demonstrates a significantly lower fertility of 1.65
for Greek, while maintaining the same low fertil-
ity of 1.33 for English as the base Llama-3.1-8B
tokenizer.
In order to develop an optimal tokenizer for
Greek which is also efficient in historical dialects
of the language, as well as in critical domains, we
extended the Llama 3 tokenizer with 20,992 new
tokens through a multi-stage process which encom-
passes curating high-quality texts and allocating
new tokens across five domains: (1) General, (2)
Legal, (3) Scientific, (4) Literature, and (5) An-
cient Greek. This process is especially important
during model inference, as it significantly reduces
the input and output token cost during model use.
Furthermore, more compact representations of in-
put text help to improve model performance. We
provide details on the steps for the tokenizer in
Appendix A.3, Tokenizer Expansion, which also
details the data construction process for creating the
tokenizer with different corpora than the ones we
used to evaluate the tokenizer fertilities presented
above.
Vocabulary
Fertility
Fertility
Tokenizer
Size
Greek
English
Mistral-7B
32,000
6.80
1.49
Meltemi-7B
61,362
1.52
1.44
Llama-3.1-8B
128,000
2.73
1.33
Llama-Krikri-8B
149,248
1.65
1.33
Table 2: Tokenizer statistics for Greek and English
3.3
Greek Embeddings Expansion & Training
To effectively integrate newly introduced Greek
tokens into the model, we implemented an initial,
targeted training phase for their corresponding em-
beddings. By preparing the new token represen-
tations prior to full-scale pretraining, we mitigate
potential disruptions to the existing model parame-
ters.
We initialized the model with Llama 3.1-8B-
Base weights, freezing all but the embeddings and
output-projection weights for the 20,992 new to-
kens, allowing their initial training without large
gradient updates to the rest of the model. Rather
than random initialization, we calculated each new
token’s initial embedding by averaging the embed-
dings associated with the tokens that would have
been produced by the original Llama-3.1 tokenizer
when processing that token. The dataset for this
step was comprised of 5B tokens and was sam-
pled to be representative of the overall pre-training
corpus. This short, several-thousand-step training
regimen ensured a smoother integration of the new
vocabulary into the model’s existing knowledge
representation. More details are described in Ap-
pendix A.4, Greek Embeddings Expansion & Train-
ing.
3.4
Continual Pretraining Process
After embedding training, all parameters were un-
frozen, and training continued on the 110B token

--- Page 5 ---

corpus using a mixed-curriculum strategy, employ-
ing a dataset sampling schedule that prefers data
closer to the initial Llama-3.1 distribution in the
beginning, while shifting closer to our true dataset
distribution as training continues, and re-warming
and re-decaying the learning rate (Ibrahim et al.,
2024).
We utilized a curriculum learning strategy which
evolved throughout the training process, beginning
with a higher proportion of simpler, high-quality
Greek texts and English content to establish foun-
dational Greek language skills while maintaining
the model’s original capabilities. As training pro-
gressed, we gradually introduced more diverse
and complex Greek sources while decreasing the
relative proportion of English content. Addition-
ally, we periodically introduced small "replay" seg-
ments of high-quality English or code to refresh the
model’s memory of content it might not frequently
encounter in the Greek-focused corpus. This ap-
proach is similar to techniques observed by Alexan-
drov et al. (2024), who emphasized careful data or-
dering to preserve base model skills when adapting
to another language.
Training was conducted over ∼50 days on the
110B token dataset at 128K context length, on 2
nodes of 8 NVIDIA H200 GPUs, using Zero 3 for
parallelization and bf16 mixed precision for com-
putational efficiency. The detailed configuration of
the pretraining procedure can be found in Appendix
A.5, Continual Pretraining Process.
3.5
Annealing Phase
Following pretraining, a short annealing pass used
a curated 3.5B token dataset of very high-quality
texts across all subcorpora.
We used within-
dataset normalized perplexity, calculated using 5-
gram KenLM (Heafield, 2011), to implement a
dataset-aware fluency scoring method for docu-
ment selection. This approach aimed at preserv-
ing dataset diversity while removing intra-dataset
outliers with lower linguistic coherence. To boost
comprehension and reasoning, a synthetic question-
answer dataset (189M tokens) was created by curat-
ing a high-quality corpus and prompting stronger
models to generate Q&A triplets with reasoning
from curated documents. Ablations revealed that
adding this synthetic QA component significantly
enhanced performance, not only improving Greek
metrics (+2.1 points over continual pretraining
alone) but notably restoring and even improving
English capabilities beyond the original Llama-3.1-
8B (+0.8 points). These ablations as well as the
training configuration for the annealing phase can
be found in Appendix A.6, Annealing Phase.
3.6
Instruction Tuning and Alignment
Llama-Krikri-8B-Instruct was created by fine-
tuning the base model for instruction following and
dialogue. In order to address Greek data scarcity,
the pipeline combined data synthesis, filtering, two-
stage Supervised Fine-Tuning (SFT), and Direct
Preference Optimization (DPO).
Data collection, synthesis, & curation involved
collecting datasets with high-quality:
• Instruction pairs, sourced from Tulu 35 (Lam-
bert et al., 2025), SmolTalk6 (Allal et al.,
2025), AgentInstruct7 (Mitra et al., 2024),
MAGPIE Ultra v1.08 (Xu et al., 2024), etc.
• Preference triplets, sourced from UltraFeed-
back9 (Cui et al., 2023), UltraMedical10
(Zhang et al., 2024a), UltraInteract11 (Yuan
et al., 2024), HelpSteer212 (Wang et al.,
2024b,a), WildGuard13 (Han et al., 2024), etc.
Additionally, Greek data was synthesized via
translation (with post-editing) of several of the
aforementioned datasets, regenerating responses us-
ing LLMs such as Gemma-2-27B-IT (Riviere et al.,
2024), and generating synthetic instructions di-
rectly in Greek using the MAGPIE technique (steer-
ing the model with system templates towards gen-
eral, reasoning, and natural language processing
tasks). Curated corpora from the annealing phase
were reused for synthetic Q&As and multi-turn di-
alogues created through few-shot prompting tech-
niques. Throughout this process, we utilized the
Skyword-Reward-Gemma-2-27B-v0.2 (Liu et al.,
2024) reward model in order to score and filter the
data, as it demonstrates high accuracy in bench-
marks such as RewardBench (Lambert et al., 2024).
Several processing steps and rule-based filters were
5https://huggingface.co/collections/allenai/
tulu-3-datasets-673b8df14442393f7213f372
6https://huggingface.co/datasets/HuggingFaceTB/smoltalk
7https://huggingface.co/datasets/microsoft/
orca-agentinstruct-1M-v1
8https://huggingface.co/datasets/argilla/magpie-ultra-v1.0
9https://huggingface.co/datasets/openbmb/UltraFeedback
10https://huggingface.co/datasets/TsinghuaC3I/
UltraMedical-Preference
11https://huggingface.co/datasets/openbmb/UltraInteract_
pair
12https://huggingface.co/datasets/nvidia/HelpSteer2
13https://huggingface.co/allenai/wildguard

--- Page 6 ---

also applied across all datasets so as to validate
dialogue structure, ensure consistent formatting,
verify language, and remove empty system mes-
sages, special tokens, and other artifacts.
SFT was done in two stages (∼856k pairs in
Stage 1, ∼638k in Stage 2), with progressively
higher data quality.
Datasets included filtered
original English data, reward-model-filtered syn-
thetic MAGPIE data (higher scores in Stage 2),
translated/post-edited data (Stage 1), regenerated
responses (including a "thinking" section in Stage
2), multi-language translation data, synthetic QA,
synthetic multi-turn dialogues, and upsampled man-
ual safety data. SFT produced a strong model
that followed instructions but needed alignment
for helpfulness, precision, and safety.
DPO provided final alignment using ∼92k pref-
erence triplets. Data included a selection of high-
scored original and translated preferences, prefer-
ences from MAGPIE-synthesized data and regen-
erated translated data using reward model scores
of multiple candidate responses, preferences de-
rived via contrasting regenerated vs. translated ref-
erences which aim to mitigate issues introduced
by unwanted translation artifacts (Dang et al.,
2024a,b), and safety preferences including man-
ually created data targeting Greek-specific safety
concerns and sensitivities.
DPO maximized the likelihood of preferred re-
sponses while minimizing that of dispreferred ones,
while an added length normalization term mitigated
the empirical phenomenon of DPO disproportion-
ally preferring longer sequences. DPO significantly
improved response quality, safety, and helpfulness
compared to the SFT-only model, and resulted to
our final model, i.e., Llama-Krikri-8B-Instruct. Im-
plementation details for both SFT and DPO can
be found in Appendix A.7, Instruction Tuning and
Alignment.
4
Evaluation
In this section, we present evaluation details
for Llama-Krikri-8B-Base and Llama-Krikri-8B-
Instruct, across six Greek and six English bench-
marks.
We compare our base model directly
with the base model Llama-3.1-8B (Grattafiori
et al., 2024) and the previous Greek state-of-the-art
model Meltemi-7B-v1.5 (Voukoutis et al., 2024).
Additionally, we evaluate our chat model, Llama-
Krikri-8B-Instruct on three challenging English
benchmarks, as well as three novelly constructed
Greek benchmarks which correspond to the English
ones.
4.1
Base Model Evaluation: Krikri-8B-Base
We
evaluated
Llama-Krikri-8B-Base
against
Llama-3.1-8B and Meltemi-7B-v1.5 in a few-shot
setting, consistent with the Open LLM Leader-
board14.
Greek Benchmarks:
The evaluation was carried
out on a suite of six Greek-specific benchmarks15
used in Voukoutis et al. (2024), including machine-
translated versions of established English datasets
(ARC-Challenge Greek, Truthful QA Greek, Hel-
laSwag Greek, MMLU Greek ), the existing Bele-
bele Greek benchmark (Bandarkar et al., 2024), and
a novel medical QA benchmark (Medical MCQA).
Results in Table 3 demonstrate substantial im-
provements for Greek (+10.8%) compared to
Llama-3.1-8B. Moreover, we observe that Llama-
Krikri-8B-Base surpasses Meltemi-7B-v1.5 with a
notable +11.6% average improvement across all
benchmarks. On MMLU Greek, Llama-Krikri-
8B-Base surpasses Llama-3.1-8B and Meltemi-7B-
v1.5 by +9.4% and +10.8% respectively, while on
ARC-Challenge Greek, it achieves an accuracy of
49.4%, compared to Llama-3.1-8B’s and Meltemi-
7B-v1.5’s 39.9% and 40.0%, respectively. Simi-
lar substantial gains are observed on the Belebele
Greek dataset, where Llama-Krikri-8B-Base scores
82.7%, surpassing Meltemi-7B-v1.5 and Llama-
3.1-8B by +21.7% and +9.9%, respectively. In
the Greek Medical MCQA, Llama-Krikri-8B-Base
reaches 53.8%, demonstrating clear advancements
over Llama-3.1-8B (+20.4%) in a domain-specific
Greek benchmark that was not translated from En-
glish.
English Benchmarks
For the evaluation of base
models on English, we utilized six benchmarks,
with five of them being the original versions of
those also used for Greek: ARC-Challenge (Clark
et al., 2018), Truthful QA (Lin et al., 2022), Hel-
laSwag (Zellers et al., 2019), MMLU (Hendrycks
et al., 2021), and Belebele (Bandarkar et al., 2024).
Additionally, the Winogrande (Sakaguchi et al.,
2021) test set was used as the sixth benchmark for
English. In the results presented in Table 4 we
14https://huggingface.co/spaces/open-llm-leaderboard/open_
llm_leaderboard
15https://huggingface.co/collections/ilsp/
ilsp-greek-evaluation-suite-6827304d5bf8b70d0346b02c

--- Page 7 ---

Benchmark
Meltemi-7B-v1.5
Llama-3.1-8B
Krikri-8B-Base
Medical MCQA EL (15-shot)
42.2
33.4
53.8
Belebele EL (5-shot)
61.0
72.8
82.7
HellaSwag EL (10-shot)
53.8
52.1
64.6
ARC-Challenge EL (25-shot)
40.0
39.9
49.4
TruthfulQA MC2 EL (0-shot)
49.0
51.1
54.2
MMLU EL (5-shot)
41.2
42.6
52.0
Average
47.9
48.7
59.5
Table 3: Greek benchmark results (accuracy %) for base models.
Benchmark
Meltemi-7B-v1.5
Llama-3.1-8B
Krikri-8B-Base
Winogrande (5-shot)
73.4
74.6
72.6
Belebele EN (5-shot)
77.7
71.5
79.8
HellaSwag EN (10-shot)
79.6
82.0
80.7
ARC-Challenge EN (25-shot)
54.1
58.5
57.8
TruthfulQA MC2 EN (0-shot)
40.5
44.2
44.8
MMLU EN (5-shot)
56.9
66.2
65.1
Average
63.7
66.2
67.0
Table 4: English benchmark results (accuracy %) for base models.
see that our training methodology not only miti-
gates catastrophic forgetting effectively, but also
improves average performance across all English
test sets by +0.8%.
4.2
Chat Model Evaluation:
Krikri-8B-Instruct
For evaluating the capabilities of Llama-Krikri-8B-
Instruct as a conversational assistant, suitable for
multi-turn dialogue, instruction-following and com-
plex coding and math queries, we used a suite of
benchmarks in both English and Greek. For En-
glish, we conducted evaluations across two paths:
• We submitted our model to the Open LLM
Leaderboard (Fourrier et al., 2024) which au-
tomatically evaluates models on IFEval, BBH,
MATH, GPQA, MUSR, and MMLU-Pro us-
ing the Eleuther AI Language Model Eval-
uation Harness (Gao et al., 2021), a unified
framework to test generative language mod-
els on a large number of different evaluation
tasks.
• We used the Arena Hard Auto v0.1 (Li et al.,
2024; Chiang et al., 2024), IFEval (Zhou et al.,
2023) (strict avg) and MT-Bench (Zheng et al.,
2023) benchmarks. Although IFEval was al-
ready included in the Open LLM Leaderboard,
we re-implemented it to enable accurate com-
parison with multiple models. In the evalua-
tion of MT-Bench we used GPT-4o (2024-08-
06) as the judge model, while in the evaluation
of Arena Hard Auto v0.1 we used the standard
approach with GPT-4-0314 as the baseline
model (by default scoring 50%) and GPT-4-
1106-Preview as the judge model, while also
reusing the generations and judgments already
computed by the authors.
For Greek, we created three novel evaluation
benchmarks by translating three challenging, di-
verse, and widely used English benchmarks, ensur-
ing high-quality translations through careful post-
editing and validation:
• IFEval Greek16 (strict avg.):
a manual
translation of 541 prompts from the origi-
nal Instruction-Following Evaluation bench-
mark (Zhou et al., 2023), featuring verifi-
able instructions such as "απάντησε με περισ-
σότερες από 400 λέξεις" (answer with more
than 400 words) and "ανάφερε τη λέξη ΤΝ
τουλάχιστον 3 φορές" (mention the word
AI at least 3 times), designed to assess the
model’s ability to follow specific instructions.
• MT-Bench Greek17, a translated version of
the Multi-turn Benchmark (Zheng et al., 2023)
16https://huggingface.co/datasets/ilsp/ifeval_greek
17https://huggingface.co/datasets/ilsp/mt-bench-greek

--- Page 8 ---

Model
IFEval EL
IFEval EN
MT-Bench EL
MT-Bench EN
Qwen 2.5 7B
46.2
74.8
5.83
7.87
EuroLLM 9B
51.3
64.5
5.98
6.27
Aya Expanse 8B
50.4
62.2
7.68
6.92
Meltemi-7B-v1.5
32.7
41.2
6.25
5.46
Llama-3.1-8B
45.8
75.1
6.46
7.25
Llama-Krikri-8B
67.5
82.4
7.96
7.21
Gemma 2 27B IT
63.2
75.6
8.23
8.00
Aya Expanse 32B
60.3
70.2
8.27
7.40
Table 5: Greek and English evaluation results using IFEval and MT-Bench.
containing 80 high-quality, multi-turn conver-
sations across eight diverse categories (e.g.,
STEM, humanities, roleplay, coding, etc.),
carefully post-edited to ensure natural Greek
phrasing and cultural appropriateness. MT-
Bench is also used to evaluate the function-
calling capabilities of LLMs (Chen et al.,
2025). The performance of each model is
calculated using LLM-as-Judge (Zheng et al.,
2023) with GPT-4o (2024-08-06) serving as
the scoring model.
• Arena-Hard-Auto Greek18, a translated ver-
sion of Arena-Hard-Auto v0.1, which orig-
inates from Chatbot Arena (Chiang et al.,
2024) was included in m-ArenaHard (Dang
et al., 2024b) after translation with Google
Translate API v3. We later post-edited us-
ing Claude Sonnet 3.5 (Anthropic, 2024) with
10-shot examples to address translation is-
sues, particularly in coding-related prompts
where some parts would best be left untrans-
lated, as well as to retain the original style
of the prompts, since some of them would
be best left vaguely posed as in the original
prompt. We used the version of the benchmark
with style control methods for Markdown ele-
ments19. We set GPT-4o-Mini (2024-07-18)
as the baseline model (by default 50% score)
and GPT-4o (2024-08-06) as the judge model.
As shown in Table 5, Llama-Krikri-8B-Instruct
demonstrates exceptional performance across both
Greek and English benchmarks, substantially out-
performing not only its parent model Llama-3.1-
8B-Instruct but also other competitive multilingual
models in the 7-9B parameter range. It should be
noted that the IFEval scores reported in this table
18https://huggingface.co/datasets/ilsp/m-ArenaHard_greek
19https://lmsys.org/blog/2024-08-28-style-control/
reflect our own implementation of the benchmark,
which may differ from the Open LLM Leaderboard
implementation due to variations in prompt format-
ting and evaluation criteria. Despite these method-
ological differences, the relative performance com-
parisons remain valid within each implementation
context.
On IFEval Greek, Llama-Krikri-8B-Instruct
achieves a remarkable 67.5% accuracy, surpassing
Llama-3.1-8B-Instruct by +21.7% and Meltemi-
7B-v1.5 by +34.8%. Notably, our 8B model even
outperforms much larger models like Gemma 2
27B IT (+4.3%) and Aya Expanse 32B (+7.2%) on
this Greek instruction-following benchmark. As
regards the original English IFEval, Llama-Krikri-
8B-Instruct scores 82.4%, significantly higher than
all other models, including those with 3-4 times
more parameters. This dramatic improvement sug-
gests that our data synthesis and instruction tuning
approach successfully addresses the unique chal-
lenges of following instructions in Greek, where
naive translations of instruction data often fail to
capture language-specific nuances.
For
MT-Bench
Greek,
which
evaluates
multi-turn conversation quality, Llama-Krikri-
8B-Instruct achieves a score of 7.96, making it
the top performer amongst other models in its
size class.
While larger models like Gemma
2 27B IT (8.23) and Aya Expanse 32B (8.27)
achieve slightly higher scores on MT-Bench
Greek, the margin is surprisingly small given
the substantial difference in model size.
On
MT-Bench English, Llama-Krikri-8B maintains
competitive performance at 7.21,
essentially
identical
with
Llama-3.1-8B-Instruct
(-0.04),
though understandably lower than the larger
Gemma 2 27B IT (-0.79) and Aya Expanse (-0.19).
As detailed in Table 6,
Llama-Krikri-8B-
Instruct’s official Open LLM Leaderboard submis-

--- Page 9 ---

Llama-3.1-8B
Krikri-8B
Benchmark
Instruct
Instruct
IFEval
49.22
60.79
BBH
29.38
29.31
MATH
15.56
11.78
GPQA
8.72
7.05
MUSR
8.61
10.46
MMLU-PRO
31.09
25.70
Avg.
23.76
24.18
Table 6: Comparative evaluation on English benchmarks
from the Open LLM Leaderboard.
ArenaHard
ArenaHard
Model
Greek
English
Aya Expanse 8B
23.8
–
Llama 3.1 8B Instr.
4.0
19.7
Krikri 8B Instr.
31.8
35.1
Aya Expanse 32B
40.1
45.1
Gemma 2 27B IT
32.2
49.6
Llama 3.1 70B Instr.
27.4
53.9
GPT 4o Mini
50.0
65.0
Table 7: Arena Hard evaluation results (% win rate) for
Greek and English.
sion shows an average score of 24.18% across all
tests, slightly surpassing the 23.76% of Llama-3.1-
8B-Instruct. The model shows particularly impres-
sive gains on IFEval implementation (60.79% vs.
49.22%) and MUSR (10.46% vs. 8.61%), while
closely matching performance on the Big Bench
Hard (BBH) benchmark (29.31% vs. 29.38%).
Although Llama-Krikri performs slightly below
Meta-Llama-3.1-8B-Instruct in the MMLU-PRO
category (25.70% vs. 31.09%), the overall per-
formance indicates successful retention of English
capabilities during the Greek-focused continual pre-
training.
The results from our Arena Hard evaluations,
presented in Table 7, reveal that, in the 8B param-
eter range, Llama-Krikri-8B-Instruct significantly
outperforms its competitors, achieving a 31.8% win
rate on Arena Hard Greek compared to Aya Ex-
panse 8B’s 23.8% and Llama 3.1 8B Instruct’s 4.0%
(+27.8% improvement). This demonstrates the ef-
fectiveness of our Greek-focused training approach.
Even more impressively, Llama-Krikri-8B-Instruct
achieves a 35.1% win rate on Arena Hard English,
substantially outperforming the original Llama-3.1-
8B-Instruct (19.7%) by +16.2%, despite our focus
on Greek capabilities. While Aya Expanse 32B
leads on Arena Hard Greek with 40.1%, our 8B
model is on par with Gemma 2 27B IT (31.8%
vs. 32.2%) and outperforms the 8.75 times larger
Llama-3.1-70B-Instruct (27.4%) by +4.4% on the
Greek evaluation data.
Please note that while all models trail behind
GPT-4o-Mini (used as baseline on the Greek Arena
Hard), recent research (Li et al., 2025) has shown
that judge models are biased towards student mod-
els, i.e., models finetuned on distilled data from the
stronger & larger teacher model which also acts
as a judge. While details on the post-training data
of GPT-4o-Mini are undisclosed, it would be very
reasonable to assume that it has been trained -at
least partly- with GPT-4 and GPT-4o serving as
teacher models and, therefore, that the judges that
we utilized are biased towards it compared to all
other evaluated models.
This performance comparison with much larger
models highlights the efficiency of our approach
since Llama-Krikri-8B-Instruct achieves compara-
ble or even superior performance on Greek bench-
marks compared to models with 3-4x more parame-
ters, while maintaining strong English capabilities.
This efficiency is particularly important for deploy-
ment scenarios where computational resources may
be limited, demonstrating that a carefully trained
smaller model can rival much larger ones for spe-
cific languages, such as Greek, and that data syn-
thesis and curation techniques can lead to a compet-
itive model for English benchmarks with a much
more compact approach than the one used in Llama-
3.1-8B-Instruct (Grattafiori et al., 2024).
Apart from the comparative evaluations men-
tioned above, we have performed zero-shot ma-
chine translation experiments on an Ancient-
Modern Greek (grc↔ell) translation dataset20 that
includes 100 sentences of Ancient Greek texts man-
ually translated into Modern Greek. Using Llama-
Krikri-8B-Instruct we have observed a 54.66 BLEU
score for the Ancient to Modern Greek (grc→ell)
translation direction, with the reverse direction
(ell→grc) being more challenging (20.41 BLEU).
5
Discussion and Conclusions
In this paper, we presented Llama-Krikri-8B, a
new LLM that exhibits significant skills in under-
standing and generating Greek, while also showing
highly accurate handling of text in English and his-
torical Greek dialects. We achieved this by devel-
oping an efficient tokenizer that exhibits a low to-
ken/words fertility for Greek and by further training
Llama 3.1-8B using a carefully constructed dataset
that covered a wide variety of domains. In evalu-
ation experiments on a benchmark suite compris-
20https://huggingface.co/datasets/ilsp/ancient-modern_
greek_translations

--- Page 10 ---

ing Greek and English datasets, we have observed
that Llama-Krikri-8B performs significantly better
in Greek (+10.8%) compared to its base model,
while also showing gains in English (+0.8%). We
then created Llama-Krikri-8B-Instruct, a version
designed for following instructions and engaging
in helpful conversations. This involved a multi-step
process that comprised synthetic data generation
in a multitude of domains, fine-tuning the model
and then aligning it with human preferences. Eval-
uations revealed that Llama-Krikri-8B-Instruct sig-
nificantly outperformed Llama-3.1-8B-Instruct in
both Greek (+21.7%) and English (+7.3%) IFE-
val. Our model also demonstrated highly competi-
tive chat abilities in both languages across several
benchmarks.
6
Limitations
The quality and accessibility of Greek datasets are
critical to the development of Krikri. Greek open-
source corpora are becoming more numerous, but
they might not be as large or varied as datasets
for more extensively spoken languages, like En-
glish. This may result in biases in the model’s
understanding of Greek, especially with regard to
regional variances, dialects, and specialized fields
like technical fields, law, or medicine.
As an 8B parameter model, our model shows
a fairly high level of Greek fluency, but it is less
effective than larger-class and commercial models
at reasoning and instruction following, and is more
likely to experience hallucinations.
In the future, our evaluation benchmarks should
include more original Greek LLM datasets that
are not the result of machine translation and post-
editing. These datasets will help minimize the ef-
fect of machine translation on evaluation results
and also better reflect the target language and cul-
ture.
7
Risks and ethical considerations
To mitigate potential risks, we took several steps
to ensure the data used for training did not contain
personally identifiable information, offensive, or
otherwise inappropriate content. We sourced data
from publicly available, licensed, or open-access
datasets, ensuring compliance with their respective
policies and any flagged data points were excluded.
We did not collect data from private communica-
tions or data sources that could contain personally
identifiable information. We have also given spe-
cial care to align our model’s responses with safety
guidelines followed by manual reviews.
We recognize that these measures are not a sub-
stitute for more thorough evaluation protocols, as
we have not performed a systematic evaluation
against LLM risks including risks related to dis-
crimination, hate speech and exclusion, informa-
tion hazards, and misinformation harms (Weidinger
et al., 2022). Moving forward, we aim to contribute
towards addressing these limitations by promoting
the development of Greek-language evaluation re-
sources for LLM risks. This will enable more ro-
bust and contextually appropriate assessments of
ethical risks in future models.
Acknowledgements
The authors wish to thank AWS and GRNET, espe-
cially Nikiforos Botis and Panos Louridas, for their
ongoing support and helping us attain the required
training infrastructure. We express our sincere grat-
itude to all members of the Institute for Language
and Speech Processing, Athena RC, for their un-
wavering support of this project. Special thanks to
Maria Giagkou, Olga Yannoutsou and Penny Kyri-
azi for their help in translating various evaluation
datasets and their efforts in the internal evaluations
of the models.
References
Alon Albalak, Yanai Elazar, Sang Michael Xie, Shayne
Longpre, Nathan Lambert, Xinyi Wang, Niklas
Muennighoff, Bairu Hou, Liangming Pan, Haewon
Jeong, et al. 2024. A survey on data selection for
language models. arXiv preprint arXiv:2402.16827.
Anton Alexandrov, Veselin Raychev, Dimitar I. Dim-
itrov, Ce Zhang, Martin Vechev, and Kristina
Toutanova. 2024.
Bggpt 1.0: Extending english-
centric
llms
to
other
languages.
Preprint,
arXiv:2412.10893.
Loubna Ben Allal,
Anton Lozhkov,
Elie Bak-
ouch, Gabriel Martín Blázquez, Guilherme Penedo,
Lewis Tunstall, Andrés Marafioti, Hynek Kydlíˇcek,
Agustín Piqueres Lajarín, Vaibhav Srivastav, Joshua
Lochner, Caleb Fahlgren, Xuan-Son Nguyen, Clé-
mentine Fourrier, Ben Burtenshaw, Hugo Larcher,
Haojun Zhao, Cyril Zakka, Mathieu Morlon, Colin
Raffel, Leandro von Werra, and Thomas Wolf.
2025.
Smollm2:
When smol goes big – data-
centric training of a small language model. Preprint,
arXiv:2502.02737.
Duarte M Alves, José Pombal, Nuno M Guerreiro, Pe-
dro H Martins, João Alves, Amin Farajian, Ben Pe-
ters, Ricardo Rei, Patrick Fernandes, Sweta Agrawal,

--- Page 11 ---

et al. 2024.
Tower: An open multilingual large
language model for translation-related tasks. arXiv
preprint arXiv:2402.17733.
AI Anthropic. 2024. The claude 3 model family: Opus,
sonnet, haiku. Claude-3 Model Card.
Mikel Artetxe and Holger Schwenk. 2018. Margin-
based parallel corpus mining with multilingual sen-
tence embeddings. arXiv preprint arXiv:1811.01136.
Mikel Artetxe and Holger Schwenk. 2019.
Mas-
sively multilingual sentence embeddings for zero-
shot cross-lingual transfer and beyond.
Transac-
tions of the association for computational linguistics,
7:597–610.
Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang,
Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei
Huang, et al. 2023. Qwen technical report. arXiv
preprint arXiv:2309.16609.
Yuntao Bai,
Saurav Kadavath,
Sandipan Kundu,
Amanda Askell, Jackson Kernion, Andy Jones, Anna
Chen, Anna Goldie, Azalia Mirhoseini, Cameron
McKinnon, Carol Chen, Catherine Olsson, Christo-
pher Olah, Danny Hernandez, Dawn Drain, Deep
Ganguli, Dustin Li, Eli Tran-Johnson, Ethan Perez,
Jamie Kerr, Jared Mueller, Jeffrey Ladish, Joshua
Landau, Kamal Ndousse, Kamile Lukosuite, Liane
Lovitt, Michael Sellitto, Nelson Elhage, Nicholas
Schiefer, Noemi Mercado, Nova DasSarma, Robert
Lasenby, Robin Larson, Sam Ringer, Scott John-
ston, Shauna Kravec, Sheer El Showk, Stanislav Fort,
Tamera Lanham, Timothy Telleen-Lawton, Tom Con-
erly, Tom Henighan, Tristan Hume, Samuel R. Bow-
man, Zac Hatfield-Dodds, Ben Mann, Dario Amodei,
Nicholas Joseph, Sam McCandlish, Tom Brown, and
Jared Kaplan. 2022. Constitutional ai: Harmlessness
from ai feedback. Preprint, arXiv:2212.08073.
Lucas Bandarkar, Davis Liang, Benjamin Muller, Mikel
Artetxe, Satya Narayan Shukla, Donald Husa, Naman
Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and
Madian Khabsa. 2024. The belebele benchmark: a
parallel reading comprehension dataset in 122 lan-
guage variants. In Proceedings of the 62nd Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 749–775.
Marta Bañón, Miquel Esplà-Gomis, Mikel L. For-
cada, Cristian García-Romero, Taja Kuzman, Nikola
Ljubeši´c, Rik van Noord, Leopoldo Pla Sempere,
Gema Ramírez-Sánchez, Peter Rupnik, Vít Su-
chomel, Antonio Toral, Tobias van der Werff, and
Jaume Zaragoza. 2022. MaCoCu: Massive collec-
tion and curation of monolingual and bilingual data:
focus on under-resourced languages. In Proceedings
of the 23rd Annual Conference of the European As-
sociation for Machine Translation, pages 303–304,
Ghent, Belgium. European Association for Machine
Translation.
A Broder. 1997. On the resemblance and containment
of documents. In Proceedings of the Compression
and Complexity of Sequences 1997, page 21.
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, Sandhini Agarwal, Ariel Herbert-Voss,
Gretchen Krueger, Tom Henighan, Rewon Child,
Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu,
Clemens Winter, Christopher Hesse, Mark Chen,
Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin
Chess, Jack Clark, Christopher Berner, Sam Mc-
Candlish, Alec Radford, Ilya Sutskever, and Dario
Amodei. 2020. Language models are few-shot learn-
ers. Preprint, arXiv:2005.14165.
Nicholas Carlini, Daphne Ippolito, Matthew Jagielski,
Katherine Lee, Florian Tramèr, and Chiyuan Zhang.
2023. Quantifying memorization across neural lan-
guage models. In The Eleventh International Confer-
ence on Learning Representations. OpenReview.
Ilias Chalkidis, Manos Fergadiotis, and Ion Androut-
sopoulos. 2021. Multieurlex – a multi-lingual and
multi-label legal document classification dataset for
zero-shot cross-lingual transfer. In Proceedings of
the 2021 Conference on Empirical Methods in Natu-
ral Language Processing. Association for Computa-
tional Linguistics.
Ilias Chalkidis, Manos Fergadiotis, Prodromos Malaka-
siotis, and Ion Androutsopoulos. 2019. Large-scale
multi-label text classification on EU legislation. In
Proceedings of the 57th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 6314–
6322, Florence, Italy. Association for Computational
Linguistics.
Yi-Chang Chen, Po-Chun Hsu, Chan-Jan Hsu, and Da-
shan Shiu. 2025. Enhancing function-calling capa-
bilities in LLMs: Strategies for prompt formats, data
integration, and multilingual translation. In Proceed-
ings of the 2025 Conference of the Nations of the
Americas Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies
(Volume 3: Industry Track), pages 99–111, Albu-
querque, New Mexico. Association for Computa-
tional Linguistics.
Wei-Lin Chiang, Lianmin Zheng, Ying Sheng, Anasta-
sios Nikolas Angelopoulos, Tianle Li, Dacheng Li,
Banghua Zhu, Hao Zhang, Michael Jordan, Joseph E
Gonzalez, et al. 2024. Chatbot arena: An open plat-
form for evaluating llms by human preference. In In-
ternational Conference on Machine Learning, pages
8359–8388. PMLR.
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot,
Ashish Sabharwal, Carissa Schoenick, and Oyvind
Tafjord. 2018. Think you have Solved Question An-
swering? Try ARC, the AI2 Reasoning Challenge.
arXiv:1803.05457v1.
Zoltan Csaki, Pian Pawakapan, Urmish Thakker, and
Qiantong Xu. 2023. Efficiently adapting pretrained
language models to new languages. arXiv preprint
arXiv:2311.05741.

--- Page 12 ---

Ganqu Cui, Lifan Yuan, Ning Ding, Guanming Yao,
Wei Zhu, Yuan Ni, Guotong Xie, Zhiyuan Liu, and
Maosong Sun. 2023. Ultrafeedback: Boosting lan-
guage models with high-quality feedback. Preprint,
arXiv:2310.01377.
John Dang, Arash Ahmadian, Kelly Marchisio, Julia
Kreutzer, Ahmet Üstün, and Sara Hooker. 2024a.
Rlhf can speak many languages: Unlocking multilin-
gual preference optimization for llms. In Proceed-
ings of the 2024 Conference on Empirical Methods in
Natural Language Processing, pages 13134–13156.
John Dang, Shivalika Singh, Daniel D’souza, Arash
Ahmadian, Alejandro Salamanca, Madeline Smith,
Aidan Peppin, Sungjin Hong, Manoj Govindassamy,
Terrence Zhao, Sandra Kublik, Meor Amer, Viraat
Aryabumi, Jon Ander Campos, Yi-Chern Tan, Tom
Kocmi, Florian Strub, Nathan Grinsztajn, Yannis
Flet-Berliac, Acyr Locatelli, Hangyu Lin, Dwarak
Talupuru, Bharat Venkitesh, David Cairuz, Bowen
Yang, Tim Chung, Wei-Yin Ko, Sylvie Shang Shi,
Amir Shukayev, Sammie Bae, Aleksandra Piktus, Ro-
man Castagné, Felipe Cruz-Salinas, Eddie Kim, Lu-
cas Crawhall-Stein, Adrien Morisot, Sudip Roy, Phil
Blunsom, Ivan Zhang, Aidan Gomez, Nick Frosst,
Marzieh Fadaee, Beyza Ermis, Ahmet Üstün, and
Sara Hooker. 2024b. Aya expanse: Combining re-
search breakthroughs for a new multilingual frontier.
Preprint, arXiv:2412.04261.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. Bert: Pre-training of deep
bidirectional transformers for language understand-
ing. Preprint, arXiv:1810.04805.
Tomaž Erjavec, Maciej Ogrodniczuk, Petya Osenova,
Nikola Ljubeši´c, Kiril Simov, Andrej Panˇcur, Michał
Rudolf, Matyáš Kopp, Starkaður Barkarson, Steinþór
Steingrímsson, Ça˘grı Çöltekin, Jesse de Does, Ka-
trien Depuydt, Tommaso Agnoloni, Giulia Ven-
turi, María Calzada Pérez, Luciana D. de Macedo,
Costanza Navarretta, Giancarlo Luxardo, Matthew
Coole, Paul Rayson, Vaidas Morkeviˇcius, Tomas
Krilaviˇcius, Roberts Darundefinedis, Orsolya Ring,
Ruben van Heusden, Maarten Marx, and Darja Fišer.
2022. The ParlaMint corpora of parliamentary pro-
ceedings. Lang. Resour. Eval., 57(1):415–448.
Clémentine Fourrier, Nathan Habib, Alina Lozovskaya,
Konrad Szafer, and Thomas Wolf. 2024.
Open
llm leaderboard v2.
https://huggingface.
co/spaces/open-llm-leaderboard/open_llm_
leaderboard.
Leo Gao, Jonathan Tow, Stella Biderman, Sid Black,
Anthony DiPofi, Charles Foster, Laurence Golding,
Jeffrey Hsu, Kyle McDonell, Niklas Muennighoff,
Jason Phang, Laria Reynolds, Eric Tang, Anish Thite,
Ben Wang, Kevin Wang, and Andy Zou. 2021. A
framework for few-shot language model evaluation.
Maria Gavriilidou, Stelios Piperidis, Dimitrios Galanis,
Kanella Pouli, Penny Labropoulou, Juli Bakagianni,
Iro Tsiouli, Miltos Deligiannis, Athanasia Kolovou,
Dimitris Gkoumas, Leon Voukoutis, and Katerina
Gkirtzou. 2023.
The CLARIN:EL infrastructure:
Platform, Portal, K-Centre. In Selected papers from
the CLARIN Annual Conference 2023.
Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri,
Abhinav Pandey, Abhishek Kadian, Ahmad Al-
Dahle, Aiesha Letman, Akhil Mathur, Alan Schel-
ten, Alex Vaughan, Amy Yang, Angela Fan, Anirudh
Goyal, Anthony Hartshorn, Aobo Yang, Archi Mi-
tra, Archie Sravankumar, Artem Korenev, Arthur
Hinsvark, Arun Rao, Aston Zhang, Aurelien Ro-
driguez, Austen Gregerson, Ava Spataru, Baptiste
Roziere, Bethany Biron, Binh Tang, Bobbie Chern,
Charlotte Caucheteux, Chaya Nayak, Chloe Bi,
Chris Marra, Chris McConnell, Christian Keller,
Christophe Touret, Chunyang Wu, Corinne Wong,
Cristian Canton Ferrer, Cyrus Nikolaidis, Damien Al-
lonsius, Daniel Song, Danielle Pintz, Danny Livshits,
Danny Wyatt, David Esiobu, Dhruv Choudhary,
Dhruv Mahajan, Diego Garcia-Olano, Diego Perino,
Dieuwke Hupkes, Egor Lakomkin, Ehab AlBadawy,
Elina Lobanova, Emily Dinan, Eric Michael Smith,
Filip Radenovic, Francisco Guzmán, Frank Zhang,
Gabriel Synnaeve, Gabrielle Lee, Georgia Lewis An-
derson, Govind Thattai, Graeme Nail, Gregoire Mi-
alon, Guan Pang, Guillem Cucurell, Hailey Nguyen,
Hannah Korevaar, Hu Xu, Hugo Touvron, Iliyan
Zarov, Imanol Arrieta Ibarra, Isabel Kloumann, Is-
han Misra, Ivan Evtimov, Jack Zhang, Jade Copet,
Jaewon Lee, Jan Geffert, Jana Vranes, Jason Park,
Jay Mahadeokar, Jeet Shah, Jelmer van der Linde,
Jennifer Billock, Jenny Hong, Jenya Lee, Jeremy Fu,
Jianfeng Chi, Jianyu Huang, Jiawen Liu, Jie Wang,
Jiecao Yu, Joanna Bitton, Joe Spisak, Jongsoo Park,
Joseph Rocca, Joshua Johnstun, Joshua Saxe, Jun-
teng Jia, Kalyan Vasuden Alwala, Karthik Prasad,
Kartikeya Upasani, Kate Plawiak, Ke Li, Kenneth
Heafield, Kevin Stone, Khalid El-Arini, Krithika Iyer,
Kshitiz Malik, Kuenley Chiu, Kunal Bhalla, Kushal
Lakhotia, Lauren Rantala-Yeary, Laurens van der
Maaten, Lawrence Chen, Liang Tan, Liz Jenkins,
Louis Martin, Lovish Madaan, Lubo Malo, Lukas
Blecher, Lukas Landzaat, Luke de Oliveira, Madeline
Muzzi, Mahesh Pasupuleti, Mannat Singh, Manohar
Paluri, Marcin Kardas, Maria Tsimpoukelli, Mathew
Oldham, Mathieu Rita, Maya Pavlova, Melanie Kam-
badur, Mike Lewis, Min Si, Mitesh Kumar Singh,
Mona Hassan, Naman Goyal, Narjes Torabi, Niko-
lay Bashlykov, Nikolay Bogoychev, Niladri Chatterji,
Ning Zhang, Olivier Duchenne, Onur Çelebi, Patrick
Alrassy, Pengchuan Zhang, Pengwei Li, Petar Va-
sic, Peter Weng, Prajjwal Bhargava, Pratik Dubal,
Praveen Krishnan, Punit Singh Koura, Puxin Xu,
Qing He, Qingxiao Dong, Ragavan Srinivasan, Raj
Ganapathy, Ramon Calderer, Ricardo Silveira Cabral,
Robert Stojnic, Roberta Raileanu, Rohan Maheswari,
Rohit Girdhar, Rohit Patel, Romain Sauvestre, Ron-
nie Polidoro, Roshan Sumbaly, Ross Taylor, Ruan
Silva, Rui Hou, Rui Wang, Saghar Hosseini, Sa-
hana Chennabasappa, Sanjay Singh, Sean Bell, Seo-
hyun Sonia Kim, Sergey Edunov, Shaoliang Nie, Sha-
ran Narang, Sharath Raparthy, Sheng Shen, Shengye
Wan, Shruti Bhosale, Shun Zhang, Simon Van-

--- Page 13 ---

denhende, Soumya Batra, Spencer Whitman, Sten
Sootla, Stephane Collot, Suchin Gururangan, Syd-
ney Borodinsky, Tamar Herman, Tara Fowler, Tarek
Sheasha, Thomas Georgiou, Thomas Scialom, Tobias
Speckbacher, Todor Mihaylov, Tong Xiao, Ujjwal
Karn, Vedanuj Goswami, Vibhor Gupta, Vignesh
Ramanathan, Viktor Kerkez, Vincent Gonguet, Vir-
ginie Do, Vish Vogeti, Vítor Albiero, Vladan Petro-
vic, Weiwei Chu, Wenhan Xiong, Wenyin Fu, Whit-
ney Meers, Xavier Martinet, Xiaodong Wang, Xi-
aofang Wang, Xiaoqing Ellen Tan, Xide Xia, Xin-
feng Xie, Xuchao Jia, Xuewei Wang, Yaelle Gold-
schlag, Yashesh Gaur, Yasmine Babaei, Yi Wen,
Yiwen Song, Yuchen Zhang, Yue Li, Yuning Mao,
Zacharie Delpierre Coudert, Zheng Yan, Zhengxing
Chen, Zoe Papakipos, Aaditya Singh, Aayushi Sri-
vastava, Abha Jain, Adam Kelsey, Adam Shajnfeld,
Adithya Gangidi, Adolfo Victoria, Ahuva Goldstand,
Ajay Menon, Ajay Sharma, Alex Boesenberg, Alexei
Baevski, Allie Feinstein, Amanda Kallet, Amit San-
gani, Amos Teo, Anam Yunus, Andrei Lupu, An-
dres Alvarado, Andrew Caples, Andrew Gu, Andrew
Ho, Andrew Poulton, Andrew Ryan, Ankit Ramchan-
dani, Annie Dong, Annie Franco, Anuj Goyal, Apara-
jita Saraf, Arkabandhu Chowdhury, Ashley Gabriel,
Ashwin Bharambe, Assaf Eisenman, Azadeh Yaz-
dan, Beau James, Ben Maurer, Benjamin Leonhardi,
Bernie Huang, Beth Loyd, Beto De Paola, Bhargavi
Paranjape, Bing Liu, Bo Wu, Boyu Ni, Braden Han-
cock, Bram Wasti, Brandon Spence, Brani Stojkovic,
Brian Gamido, Britt Montalvo, Carl Parker, Carly
Burton, Catalina Mejia, Ce Liu, Changhan Wang,
Changkyu Kim, Chao Zhou, Chester Hu, Ching-
Hsiang Chu, Chris Cai, Chris Tindal, Christoph Fe-
ichtenhofer, Cynthia Gao, Damon Civin, Dana Beaty,
Daniel Kreymer, Daniel Li, David Adkins, David
Xu, Davide Testuggine, Delia David, Devi Parikh,
Diana Liskovich, Didem Foss, Dingkang Wang, Duc
Le, Dustin Holland, Edward Dowling, Eissa Jamil,
Elaine Montgomery, Eleonora Presani, Emily Hahn,
Emily Wood, Eric-Tuan Le, Erik Brinkman, Este-
ban Arcaute, Evan Dunbar, Evan Smothers, Fei Sun,
Felix Kreuk, Feng Tian, Filippos Kokkinos, Firat
Ozgenel, Francesco Caggioni, Frank Kanayet, Frank
Seide, Gabriela Medina Florez, Gabriella Schwarz,
Gada Badeer, Georgia Swee, Gil Halpern, Grant
Herman, Grigory Sizov, Guangyi, Zhang, Guna
Lakshminarayanan, Hakan Inan, Hamid Shojanaz-
eri, Han Zou, Hannah Wang, Hanwen Zha, Haroun
Habeeb, Harrison Rudolph, Helen Suk, Henry As-
pegren, Hunter Goldman, Hongyuan Zhan, Ibrahim
Damlaj, Igor Molybog, Igor Tufanov, Ilias Leontiadis,
Irina-Elena Veliche, Itai Gat, Jake Weissman, James
Geboski, James Kohli, Janice Lam, Japhet Asher,
Jean-Baptiste Gaya, Jeff Marcus, Jeff Tang, Jen-
nifer Chan, Jenny Zhen, Jeremy Reizenstein, Jeremy
Teboul, Jessica Zhong, Jian Jin, Jingyi Yang, Joe
Cummings, Jon Carvill, Jon Shepard, Jonathan Mc-
Phie, Jonathan Torres, Josh Ginsburg, Junjie Wang,
Kai Wu, Kam Hou U, Karan Saxena, Kartikay Khan-
delwal, Katayoun Zand, Kathy Matosich, Kaushik
Veeraraghavan, Kelly Michelena, Keqian Li, Ki-
ran Jagadeesh, Kun Huang, Kunal Chawla, Kyle
Huang, Lailin Chen, Lakshya Garg, Lavender A,
Leandro Silva, Lee Bell, Lei Zhang, Liangpeng
Guo, Licheng Yu, Liron Moshkovich, Luca Wehrst-
edt, Madian Khabsa, Manav Avalani, Manish Bhatt,
Martynas Mankus, Matan Hasson, Matthew Lennie,
Matthias Reso, Maxim Groshev, Maxim Naumov,
Maya Lathi, Meghan Keneally, Miao Liu, Michael L.
Seltzer, Michal Valko, Michelle Restrepo, Mihir Pa-
tel, Mik Vyatskov, Mikayel Samvelyan, Mike Clark,
Mike Macey, Mike Wang, Miquel Jubert Hermoso,
Mo Metanat, Mohammad Rastegari, Munish Bansal,
Nandhini Santhanam, Natascha Parks, Natasha
White, Navyata Bawa, Nayan Singhal, Nick Egebo,
Nicolas Usunier, Nikhil Mehta, Nikolay Pavlovich
Laptev, Ning Dong, Norman Cheng, Oleg Chernoguz,
Olivia Hart, Omkar Salpekar, Ozlem Kalinli, Parkin
Kent, Parth Parekh, Paul Saab, Pavan Balaji, Pe-
dro Rittner, Philip Bontrager, Pierre Roux, Piotr
Dollar, Polina Zvyagina, Prashant Ratanchandani,
Pritish Yuvraj, Qian Liang, Rachad Alao, Rachel
Rodriguez, Rafi Ayub, Raghotham Murthy, Raghu
Nayani, Rahul Mitra, Rangaprabhu Parthasarathy,
Raymond Li, Rebekkah Hogan, Robin Battey, Rocky
Wang, Russ Howes, Ruty Rinott, Sachin Mehta,
Sachin Siby, Sai Jayesh Bondu, Samyak Datta, Sara
Chugh, Sara Hunt, Sargun Dhillon, Sasha Sidorov,
Satadru Pan, Saurabh Mahajan, Saurabh Verma,
Seiji Yamamoto, Sharadh Ramaswamy, Shaun Lind-
say, Shaun Lindsay, Sheng Feng, Shenghao Lin,
Shengxin Cindy Zha, Shishir Patil, Shiva Shankar,
Shuqiang Zhang, Shuqiang Zhang, Sinong Wang,
Sneha Agarwal, Soji Sajuyigbe, Soumith Chintala,
Stephanie Max, Stephen Chen, Steve Kehoe, Steve
Satterfield, Sudarshan Govindaprasad, Sumit Gupta,
Summer Deng, Sungmin Cho, Sunny Virk, Suraj
Subramanian, Sy Choudhury, Sydney Goldman, Tal
Remez, Tamar Glaser, Tamara Best, Thilo Koehler,
Thomas Robinson, Tianhe Li, Tianjun Zhang, Tim
Matthews, Timothy Chou, Tzook Shaked, Varun
Vontimitta, Victoria Ajayi, Victoria Montanez, Vijai
Mohan, Vinay Satish Kumar, Vishal Mangla, Vlad
Ionescu, Vlad Poenaru, Vlad Tiberiu Mihailescu,
Vladimir Ivanov, Wei Li, Wenchen Wang, Wen-
wen Jiang, Wes Bouaziz, Will Constable, Xiaocheng
Tang, Xiaojian Wu, Xiaolan Wang, Xilun Wu, Xinbo
Gao, Yaniv Kleinman, Yanjun Chen, Ye Hu, Ye Jia,
Ye Qi, Yenda Li, Yilin Zhang, Ying Zhang, Yossi Adi,
Youngjin Nam, Yu, Wang, Yu Zhao, Yuchen Hao,
Yundi Qian, Yunlu Li, Yuzi He, Zach Rait, Zachary
DeVito, Zef Rosnbrick, Zhaoduo Wen, Zhenyu Yang,
Zhiwei Zhao, and Zhiyu Ma. 2024. The llama 3 herd
of models. Preprint, arXiv:2407.21783.
Suchin
Gururangan,
Ana
Marasovi´c,
Swabha
Swayamdipta, Kyle Lo, Iz Beltagy, Doug Downey,
and Noah A. Smith. 2020. Don’t stop pretraining:
Adapt language models to domains and tasks.
Preprint, arXiv:2004.10964.
Seungju Han, Kavel Rao, Allyson Ettinger, Liwei Jiang,
Bill Yuchen Lin, Nathan Lambert, Yejin Choi, and
Nouha Dziri. 2024. Wildguard: Open one-stop mod-
eration tools for safety risks, jailbreaks, and refusals
of llms. Preprint, arXiv:2406.18495.
Kenneth Heafield. 2011. KenLM: Faster and smaller

--- Page 14 ---

language model queries. In Proceedings of the Sixth
Workshop on Statistical Machine Translation, pages
187–197, Edinburgh, Scotland. Association for Com-
putational Linguistics.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2021. Measuring massive multitask language under-
standing. In International Conference on Learning
Representations.
Pin-Lun Hsu, Yun Dai, Vignesh Kothapalli, Qingquan
Song, Shao Tang, Siyu Zhu, Steven Shimizu, Shivam
Sahni, Haowen Ning, and Yanning Chen. 2024. Liger
kernel: Efficient triton kernels for llm training. arXiv
preprint arXiv:2410.10989.
Adam Ibrahim, Benjamin Thérien, Kshitij Gupta,
Mats L Richter, Quentin Anthony, Timothée Lesort,
Eugene Belilovsky, and Irina Rish. 2024. Simple
and scalable strategies to continually pre-train large
language models. arXiv preprint arXiv:2403.08763.
Albert Q Jiang, Alexandre Sablayrolles, Arthur Men-
sch, Chris Bamford, Devendra Singh Chaplot, Diego
de las Casas, Florian Bressand, Gianna Lengyel, Guil-
laume Lample, Lucile Saulnier, et al. 2023. Mistral
7b. arXiv preprint arXiv:2310.06825.
Armand Joulin, Édouard Grave, Piotr Bojanowski, and
Tomáš Mikolov. 2017. Bag of tricks for efficient text
classification. In Proceedings of the 15th Confer-
ence of the European Chapter of the Association for
Computational Linguistics: Volume 2, Short Papers,
pages 427–431.
LAION. 2023. LeoLM: Igniting German-Language
LLM
Research.
https://laion.ai/blog/
leo-lm/. Accessed: (12 July 2024).
Nathan Lambert, Jacob Morrison, Valentina Pyatkin,
Shengyi Huang, Hamish Ivison, Faeze Brahman,
Lester James V. Miranda, Alisa Liu, Nouha Dziri,
Shane Lyu, Yuling Gu, Saumya Malik, Victoria
Graf, Jena D. Hwang, Jiangjiang Yang, Ronan Le
Bras, Oyvind Tafjord, Chris Wilhelm, Luca Soldaini,
Noah A. Smith, Yizhong Wang, Pradeep Dasigi, and
Hannaneh Hajishirzi. 2025. Tulu 3: Pushing fron-
tiers in open language model post-training. Preprint,
arXiv:2411.15124.
Nathan Lambert, Valentina Pyatkin, Jacob Morrison,
LJ Miranda, Bill Yuchen Lin, Khyathi Chandu,
Nouha Dziri, Sachin Kumar, Tom Zick, Yejin Choi,
Noah A. Smith, and Hannaneh Hajishirzi. 2024. Re-
wardbench: Evaluating reward models for language
modeling. Preprint, arXiv:2403.13787.
Katherine Lee, Daphne Ippolito, Andrew Nystrom,
Chiyuan Zhang, Douglas Eck, Chris Callison-Burch,
and Nicholas Carlini. 2022. Deduplicating training
data makes language models better. In Proceedings
of the 60th Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 8424–8445.
Jure Leskovec, Anand Rajaraman, and Jeffrey David
Ullman. 2020. Mining of massive data sets. Cam-
bridge university press.
Dawei Li, Renliang Sun, Yue Huang, Ming Zhong,
Bohan Jiang, Jiawei Han, Xiangliang Zhang, Wei
Wang, and Huan Liu. 2025. Preference leakage: A
contamination problem in llm-as-a-judge. Preprint,
arXiv:2502.01534.
Tianle Li, Wei-Lin Chiang, Evan Frick, Lisa Dunlap,
Tianhao Wu, Banghua Zhu, Joseph E Gonzalez, and
Ion Stoica. 2024. From crowdsourced data to high-
quality benchmarks: Arena-hard and benchbuilder
pipeline. arXiv preprint arXiv:2406.11939.
Stephanie Lin, Jacob Hilton, and Owain Evans. 2022.
TruthfulQA: Measuring how models mimic human
falsehoods. In Proceedings of the 60th Annual Meet-
ing of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 3214–3252, Dublin,
Ireland. Association for Computational Linguistics.
Chris Yuhao Liu, Liang Zeng, Jiacai Liu, Rui Yan, Ju-
jie He, Chaojie Wang, Shuicheng Yan, Yang Liu,
and Yahui Zhou. 2024. Skywork-reward: Bag of
tricks for reward modeling in llms. arXiv preprint
arXiv:2410.18451.
Kyle Lo, Lucy Lu Wang, Mark Neumann, Rodney Kin-
ney, and Daniel S Weld. 2020. S2orc: The semantic
scholar open research corpus. In Proceedings of the
58th Annual Meeting of the Association for Compu-
tational Linguistics, pages 4969–4983.
Andrea Lösch, Valérie Mapelli, Khalid Choukri, Maria
Giagkou, Stelios Piperidis, Prokopis Prokopidis,
Vassilis Papavassiliou, Miltos Deligiannis, Aivars
Berzins, Andrejs Vasiljevs, et al. 2021. Collection
and Curation of Language Data within the European
Language Resource Coordination (ELRC). In Qura-
tor.
Ilya Loshchilov and Frank Hutter. 2017.
Fixing
Weight Decay Regularization in Adam.
CoRR,
abs/1711.05101.
Anton Lozhkov, Raymond Li, Loubna Ben Allal, Fed-
erico Cassano, Joel Lamy-Poirier, Nouamane Tazi,
Ao Tang, Dmytro Pykhtar, Jiawei Liu, Yuxiang Wei,
et al. 2024. Starcoder 2 and the stack v2: The next
generation. arXiv preprint arXiv:2402.19173.
Yun Luo, Zhen Yang, Fandong Meng, Yafu Li, Jie Zhou,
and Yue Zhang. 2025. An empirical study of catas-
trophic forgetting in large language models during
continual fine-tuning. Preprint, arXiv:2308.08747.
Pedro Henrique Martins, Patrick Fernandes, João Alves,
Nuno M Guerreiro, Ricardo Rei, Duarte M Alves,
José Pombal, Amin Farajian, Manuel Faysse, Ma-
teusz Klimaszewski, et al. 2024. Eurollm: Multilin-
gual language models for europe. In Proceedings of
the Ninth Conference on Machine Translation, pages
1393–1409. Association for Computational Linguis-
tics.

--- Page 15 ---

Arindam Mitra, Luciano Del Corro, Guoqing Zheng,
Shweti Mahajan, Dany Rouhana, Andres Codas,
Yadong Lu, Wei ge Chen, Olga Vrousgos, Corby
Rosset, Fillipe Silva, Hamed Khanpour, Yash Lara,
and Ahmed Awadallah. 2024. Agentinstruct: Toward
generative teaching with agentic flows.
Preprint,
arXiv:2407.03502.
Thuat Nguyen, Chien Van Nguyen, Viet Dac Lai, Hieu
Man, Nghia Trung Ngo, Franck Dernoncourt, Ryan A
Rossi, and Thien Huu Nguyen. 2023. CulturaX: A
cleaned, enormous, and multilingual dataset for large
language models in 167 languages. arXiv preprint
arXiv:2309.09400.
Krzysztof Ociepa, Łukasz Flis, Krzysztof Wróbel,
Adrian Gwo´zdziej, and Remigiusz Kinas. 2024.
Bielik 7b v0.1: A polish language model – de-
velopment, insights, and evaluation.
Preprint,
arXiv:2410.18565.
Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Car-
roll L. Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, John
Schulman, Jacob Hilton, Fraser Kelton, Luke Miller,
Maddie Simens, Amanda Askell, Peter Welinder,
Paul Christiano, Jan Leike, and Ryan Lowe. 2022.
Training language models to follow instructions with
human feedback. Preprint, arXiv:2203.02155.
Christos Papaloukas, Ilias Chalkidis, Konstantinos
Athinaios, Despina-Athanasia Pantazi, and Manolis
Koubarakis. 2021. Multi-granular legal topic clas-
sification on greek legislation. In Proceedings of
the Natural Legal Language Processing Workshop
2021, pages 63–75, Punta Cana, Dominican Republic.
Association for Computational Linguistics.
Vassilis Papavassiliou, Sokratis Sofianopoulos, Prokopis
Prokopidis, and Stelios Piperidis. 2018.
The
ILSP/ARC submission to the WMT 2018 parallel
corpus filtering shared task. In Proceedings of the
Third Conference on Machine Translation: Shared
Task Papers, pages 928–933, Belgium, Brussels. As-
sociation for Computational Linguistics.
Guilherme Penedo, Hynek Kydlíˇcek, Anton Lozhkov,
Margaret Mitchell, Colin Raffel, Leandro Von Werra,
Thomas Wolf, et al. 2024. The FineWeb Datasets:
Decanting the Web for the Finest Text Data at Scale.
arXiv preprint arXiv:2406.17557.
Ramon Pires, Hugo Abonizio, Thales Sales Almeida,
and Rodrigo Nogueira. 2023.
Sabiá: Portuguese
large language models. In Intelligent Systems, pages
226–240, Cham. Springer Nature Switzerland.
Ye Qi, Devendra Sachan, Matthieu Felix, Sarguna Pad-
manabhan, and Graham Neubig. 2018. When and
why are pre-trained word embeddings useful for neu-
ral machine translation? In Proceedings of the 2018
Conference of the North American Chapter of the
Association for Computational Linguistics: Human
Language Technologies, Volume 2 (Short Papers),
pages 529–535, New Orleans, Louisiana. Associa-
tion for Computational Linguistics.
Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano
Ermon, Christopher D. Manning, and Chelsea Finn.
2024.
Direct preference optimization: Your lan-
guage model is secretly a reward model. Preprint,
arXiv:2305.18290.
Ricardo Rei, Marcos Treviso, Nuno M. Guerreiro,
Chrysoula Zerva, Ana C Farinha, Christine Maroti,
José G. C. de Souza, Taisiya Glushkova, Duarte
Alves, Luisa Coheur, Alon Lavie, and André F. T.
Martins. 2022. CometKiwi: IST-unbabel 2022 sub-
mission for the quality estimation shared task. In
Proceedings of the Seventh Conference on Machine
Translation (WMT), pages 634–645, Abu Dhabi,
United Arab Emirates (Hybrid). Association for Com-
putational Linguistics.
Morgane Riviere, Shreya Pathak, Pier Giuseppe
Sessa, Cassidy Hardin, Surya Bhupatiraju, Léonard
Hussenot,
Thomas Mesnard,
Bobak Shahriari,
Alexandre Ramé, Johan Ferret, Peter Liu, Pouya
Tafti, Abe Friesen, Michelle Casbon, Sabela Ramos,
Ravin Kumar, Charline Le Lan, Sammy Jerome, An-
ton Tsitsulin, Nino Vieillard, Piotr Stanczyk, Sertan
Girgin, Nikola Momchev, Matt Hoffman, Shantanu
Thakoor, Jean-Bastien Grill, Behnam Neyshabur,
Olivier Bachem, Alanna Walton, Aliaksei Severyn,
Alicia Parrish, Aliya Ahmad, Allen Hutchison, Alvin
Abdagic, Amanda Carl, Amy Shen, Andy Brock,
Andy Coenen, Anthony Laforge, Antonia Pater-
son, Ben Bastian, Bilal Piot, Bo Wu, Brandon
Royal, Charlie Chen, Chintu Kumar, Chris Perry,
Chris Welty, Christopher A. Choquette-Choo, Danila
Sinopalnikov, David Weinberger, Dimple Vijayku-
mar, Dominika Rogozi´nska, Dustin Herbison, Elisa
Bandy, Emma Wang, Eric Noland, Erica Moreira,
Evan Senter, Evgenii Eltyshev, Francesco Visin,
Gabriel Rasskin, Gary Wei, Glenn Cameron, Gus
Martins, Hadi Hashemi, Hanna Klimczak-Pluci´nska,
Harleen Batra, Harsh Dhand, Ivan Nardini, Jacinda
Mein, Jack Zhou, James Svensson, Jeff Stanway,
Jetha Chan, Jin Peng Zhou, Joana Carrasqueira,
Joana Iljazi, Jocelyn Becker, Joe Fernandez, Joost
van Amersfoort, Josh Gordon, Josh Lipschultz, Josh
Newlan, Ju yeong Ji, Kareem Mohamed, Kartikeya
Badola, Kat Black, Katie Millican, Keelin McDonell,
Kelvin Nguyen, Kiranbir Sodhia, Kish Greene,
Lars Lowe Sjoesund, Lauren Usui, Laurent Sifre,
Lena Heuermann, Leticia Lago, Lilly McNealus,
Livio Baldini Soares, Logan Kilpatrick, Lucas Dixon,
Luciano Martins, Machel Reid, Manvinder Singh,
Mark Iverson, Martin Görner, Mat Velloso, Mateo
Wirth, Matt Davidow, Matt Miller, Matthew Rahtz,
Matthew Watson, Meg Risdal, Mehran Kazemi,
Michael Moynihan, Ming Zhang, Minsuk Kahng,
Minwoo Park, Mofi Rahman, Mohit Khatwani, Na-
talie Dao, Nenshad Bardoliwalla, Nesh Devanathan,
Neta Dumai, Nilay Chauhan, Oscar Wahltinez,
Pankil Botarda, Parker Barnes, Paul Barham, Paul
Michel, Pengchong Jin, Petko Georgiev, Phil Culli-
ton, Pradeep Kuppala, Ramona Comanescu, Ramona
Merhej, Reena Jana, Reza Ardeshir Rokni, Rishabh
Agarwal, Ryan Mullins, Samaneh Saadat, Sara Mc
Carthy, Sarah Cogan, Sarah Perrin, Sébastien M. R.

--- Page 16 ---

Arnold, Sebastian Krause, Shengyang Dai, Shruti
Garg, Shruti Sheth, Sue Ronstrom, Susan Chan, Tim-
othy Jordan, Ting Yu, Tom Eccles, Tom Hennigan,
Tomas Kocisky, Tulsee Doshi, Vihan Jain, Vikas Ya-
dav, Vilobh Meshram, Vishal Dharmadhikari, War-
ren Barkley, Wei Wei, Wenming Ye, Woohyun Han,
Woosuk Kwon, Xiang Xu, Zhe Shen, Zhitao Gong,
Zichuan Wei, Victor Cotruta, Phoebe Kirk, Anand
Rao, Minh Giang, Ludovic Peran, Tris Warkentin,
Eli Collins, Joelle Barral, Zoubin Ghahramani, Raia
Hadsell, D. Sculley, Jeanine Banks, Anca Dragan,
Slav Petrov, Oriol Vinyals, Jeff Dean, Demis Hass-
abis, Koray Kavukcuoglu, Clement Farabet, Elena
Buchatskaya, Sebastian Borgeaud, Noah Fiedel, Ar-
mand Joulin, Kathleen Kenealy, Robert Dadashi,
and Alek Andreev. 2024.
Gemma 2: Improving
open language models at a practical size. Preprint,
arXiv:2408.00118.
Richard J Roberts. 2001. Pubmed central: The genbank
of the published literature.
Dimitrios Roussis and Vassilis Papavassiliou. 2022. The
ARC-NKUA submission for the English-Ukrainian
general machine translation shared task at WMT22.
In Proceedings of the Seventh Conference on Ma-
chine Translation (WMT), pages 358–365, Abu
Dhabi, United Arab Emirates (Hybrid). Association
for Computational Linguistics.
Dimitrios Roussis, Vassilis Papavassiliou, Prokopis
Prokopidis, Stelios Piperidis, and Vassilis Katsouros.
2022a.
SciPar: A collection of parallel corpora
from scientific abstracts. In Proceedings of the Thir-
teenth Language Resources and Evaluation Confer-
ence, pages 2652–2657, Marseille, France. European
Language Resources Association.
Dimitrios Roussis, Vassilis Papavassiliou, Sokratis
Sofianopoulos, Prokopis Prokopidis, and Stelios
Piperidis. 2022b. Constructing parallel corpora from
COVID-19 news using MediSys metadata. In Pro-
ceedings of the Thirteenth Language Resources and
Evaluation Conference, pages 1068–1072, Marseille,
France. European Language Resources Association.
Dimitris Roussis, Sokratis Sofianopoulos, and Stelios
Piperidis. 2024. Enhancing scientific discourse: Ma-
chine translation for the scientific domain. In Pro-
ceedings of the 25th Annual Conference of the Euro-
pean Association for Machine Translation (Volume
1), pages 275–285.
Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavat-
ula, and Yejin Choi. 2021. Winogrande: An adver-
sarial winograd schema challenge at scale. Commu-
nications of the ACM, 64(9):99–106.
Víctor M. Sánchez-Cartagena, Marta Bañón, Sergio
Ortiz-Rojas, and Gema Ramírez-Sánchez. 2018.
Prompsit’s submission to WMT 2018 Parallel Cor-
pus Filtering shared task.
In Proceedings of the
Third Conference on Machine Translation, Volume 2:
Shared Task Papers, Brussels, Belgium. Association
for Computational Linguistics.
Liping Tang, Nikhil Ranjan, Omkar Pangarkar, Xuezhi
Liang, Zhen Wang, Li An, Bhaskar Rao, Linghao Jin,
Huijuan Wang, Zhoujun Cheng, Suqi Sun, Cun Mu,
Victor Miller, Xuezhe Ma, Yue Peng, Zhengzhong
Liu, and Eric P. Xing. 2024. Txt360: A top-quality
llm pre-training dataset requires the perfect blend.
Jörg Tiedemann. 2012. Parallel data, tools and inter-
faces in OPUS. In Proceedings of the Eighth In-
ternational Conference on Language Resources and
Evaluation (LREC’12), pages 2214–2218, Istanbul,
Turkey. European Language Resources Association
(ELRA).
Yury Tokpanov, Beren Millidge, Paolo Glorioso,
Jonathan Pilault, Adam Ibrahim, James Whitting-
ton, and Quentin Anthony. 2024. Zyda: A 1.3 T
Dataset for Open Language Modeling. arXiv preprint
arXiv:2406.01981.
Santosh Tyss, Rashid Haddad, and Matthias Grabmair.
2024. Ecthr-pcr: A dataset for precedent understand-
ing and prior case retrieval in the european court
of human rights. In Proceedings of the 2024 Joint
International Conference on Computational Linguis-
tics, Language Resources and Evaluation (LREC-
COLING 2024), pages 5473–5483.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz
Kaiser, and Illia Polosukhin. 2023. Attention is all
you need. Preprint, arXiv:1706.03762.
Leon
Voukoutis,
Dimitris
Roussis,
Georgios
Paraskevopoulos, Sokratis Sofianopoulos, Prokopis
Prokopidis,
Vassilis Papavasileiou,
Athanasios
Katsamanis, Stelios Piperidis, and Vassilis Katsouros.
2024. Meltemi: The first open large language model
for greek. Preprint, arXiv:2407.20743.
Zhilin Wang, Alexander Bukharin, Olivier Delal-
leau, Daniel Egert, Gerald Shen, Jiaqi Zeng, Olek-
sii Kuchaiev, and Yi Dong. 2024a.
Helpsteer2-
preference: Complementing ratings with preferences.
Preprint, arXiv:2410.01257.
Zhilin Wang, Yi Dong, Olivier Delalleau, Jiaqi
Zeng, Gerald Shen, Daniel Egert, Jimmy J. Zhang,
Makesh Narsimhan Sreedhar, and Oleksii Kuchaiev.
2024b.
Helpsteer2:
Open-source dataset for
training top-performing reward models. Preprint,
arXiv:2406.08673.
Laura Weidinger, Jonathan Uesato, Maribeth Rauh,
Conor Griffin, Po-Sen Huang, John Mellor, Amelia
Glaese, Myra Cheng, Borja Balle, Atoosa Kasirzadeh,
Courtney Biles, Sasha Brown, Zac Kenton, Will
Hawkins, Tom Stepleton, Abeba Birhane, Lisa Anne
Hendricks, Laura Rimell, William Isaac, Julia Haas,
Sean Legassick, Geoffrey Irving, and Iason Gabriel.
2022. Taxonomy of risks posed by language models.
In Proceedings of the 2022 ACM Conference on Fair-
ness, Accountability, and Transparency, FAccT ’22,
page 214–229, New York, NY, USA. Association for
Computing Machinery.

--- Page 17 ---

Zhangchen Xu, Fengqing Jiang, Luyao Niu, Yun-
tian Deng, Radha Poovendran, Yejin Choi, and
Bill Yuchen Lin. 2024. Magpie: Alignment data
synthesis from scratch by prompting aligned llms
with nothing. Preprint, arXiv:2406.08464.
Lifan Yuan, Ganqu Cui, Hanbin Wang, Ning Ding,
Xingyao Wang, Jia Deng, Boji Shan, Huimin Chen,
Ruobing Xie, Yankai Lin, et al. 2024. Advancing llm
reasoning generalists with preference trees. arXiv
preprint arXiv:2404.02078.
Jaume Zaragoza-Bernabeu, Gema Ramírez-Sánchez,
Marta Bañón, and Sergio Ortiz Rojas. 2022.
Bi-
cleaner AI: Bicleaner goes neural. In Proceedings
of the Thirteenth Language Resources and Evalua-
tion Conference, pages 824–831, Marseille, France.
European Language Resources Association.
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali
Farhadi, and Yejin Choi. 2019. HellaSwag: Can a ma-
chine really finish your sentence? In Proceedings of
the 57th Annual Meeting of the Association for Com-
putational Linguistics, pages 4791–4800, Florence,
Italy. Association for Computational Linguistics.
Kaiyan Zhang, Sihang Zeng, Ermo Hua, Ning Ding,
Zhang-Ren Chen, Zhiyuan Ma, Haoxin Li, Ganqu
Cui, Biqing Qi, Xuekai Zhu, et al. 2024a. Ultramedi-
cal: Building specialized generalists in biomedicine.
Advances in Neural Information Processing Systems,
37:26045–26081.
Yifan Zhang, Yifan Luo, Yang Yuan, and Andrew Chi-
Chih Yao. 2024b. Automathtext: Autonomous data
selection with language models for mathematical
texts. arXiv preprint arXiv:2402.07625.
Yiran Zhao, Wenxuan Zhang, Guizhen Chen, Kenji
Kawaguchi, and Lidong Bing. 2024. How do large
language models handle multilingualism?
arXiv
preprint arXiv:2402.18815.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan
Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin,
Zhuohan Li, Dacheng Li, Eric Xing, et al. 2023.
Judging llm-as-a-judge with mt-bench and chatbot
arena. Advances in Neural Information Processing
Systems, 36:46595–46623.
Jeffrey Zhou, Tianjian Lu, Swaroop Mishra, Sid-
dhartha Brahma, Sujoy Basu, Yi Luan, Denny Zhou,
and Le Hou. 2023.
Instruction-following evalu-
ation for large language models.
arXiv preprint
arXiv:2311.07911.

--- Page 18 ---

A
Technical Details
A.1
Pretraining Data Mix
The pretraining data mix (Table 1) contains the following four components:
1. Greek Texts (56.7B tokens): The Greek part of the dataset was sourced from publicly available
resources spanning a wide range of domains and sources: Wikipedia, ELRC-SHARE (Lösch et al.,
2021), EUR-LEX & MultiEUR-LEX (Chalkidis et al., 2019, 2021), MaCoCu (Bañón et al., 2022),
CLARIN-EL (Gavriilidou et al., 2023), EMEA21, parliamentary proceedings (Erjavec et al., 2022),
22, governmental and legal documents from the Greek Government Gazette via the National Printing
House23, the Permanent Greek Legislation Code – Raptarchis dataset24 (Papaloukas et al., 2021),
Greek School Books25, the Kallipos initiative of Greek open academic textbooks26, full texts from
publicly available articles, theses, and dissertations from academic repositories and the National
Documentation Center27, as well as pre-filtered resources originally compiled from the web, such as
CulturaX (Nguyen et al., 2023) and CulturaY28. In addition to Modern Greek, we incorporated a
significant amount of Ancient Greek texts into our training corpus from Wikisource, school books,
web pages, and Project Gutenberg29, which provides freely available Ancient Greek texts, including
classical literature and historical documents. By including Ancient Greek data, we ensured that
Llama-Krikri-8B is able process polytonic Greek and engage with historical texts effectively. This
enhances the model’s utility for classical studies, historical research, and philological applications.
2. English Texts (21B tokens): A subset of high-quality English data was mixed into the training corpus.
This subset ensures that the model is continually trained on English data, and is drawn from sources
that were also used for the Greek data, such as Wikipedia, Wikisource, Project Gutenberg (post-
1900), EUR-LEX, EMEA, Greek academic repositories, etc. We also utilized additional English texts
originating from abstracts and full texts of academic records found on multiple scientific repositories
(Roussis et al., 2022a, 2024), ECtHR-PCR (Tyss et al., 2024), and pre-filtered datasets from TxT360
(Tang et al., 2024), like ArXiv, S2ORC (Lo et al., 2020), and PubMed Central (Roberts, 2001). By
incorporating diverse and high-quality English texts, we mitigate the risk of catastrophic forgetting.
3. Parallel Data (5.5B tokens): We compiled a diverse parallel corpus with language pairs covering
multiple languages: Greek, English, French, Portuguese, German, Spanish, and Italian. The decision
to add parallel data which covers other European languages (i.e., German, French, Italian, Portuguese,
and Spanish) is informed from the languages that have been included in the multilingual instruction
tuning of the original Llama-3.1 (Grattafiori et al., 2024). We utilized resources such as SciPar
(Roussis et al., 2022a), MediSys (Roussis et al., 2022b), MultiEUR-LEX (Chalkidis et al., 2021),
Europarl, TED Talk transcripts (Qi et al., 2018), and other sources with sentence pairs such as ELRC-
SHARE (Lösch et al., 2021) & OPUS (Tiedemann, 2012). Our data include parallel documents
and sentence pairs randomly sampled for each translation direction, e.g., EN-EL/EL-EN and EN-
DE/DE-EN, as well as augmented training examples with concatenated parallel content across
multiple languages (e.g., a Greek text followed by its English, German, and Spanish translations with
appropriate prompt templates). The addition of these documents has a twofold effect. It has been
shown that parallel data boosts translation performance (Alves et al., 2024; Martins et al., 2024),
while limited empirical evidence indicates that pretrained LLMs process multilingual queries by first
translating the content into English, utilizing their English knowledge to answer the query and then
translate the answer back to the original language(Zhao et al., 2024).
21https://www.ema.europa.eu/
22https://www.gutenberg.org/
23https://et.gr/
24https://huggingface.co/datasets/AI-team-UoA/greek_legal_code
25https://ebooks.edu.gr/ebooks/
26https://kallipos.gr/en/homepage/
27https://www.ekt.gr/en
28https://huggingface.co/datasets/ontocord/CulturaY
29https://www.gutenberg.org/

--- Page 19 ---

4. Code and Math (7.8B tokens): We also integrated datasets containing text with code and mathemat-
ics, leveraging Stack Overflow30, Python-Edu which is a subset of the SmolLM corpus (Allal et al.,
2025) originating from The Stack V2 dataset (Lozhkov et al., 2024) and having been scored with an
educational code classifier, and the AutoMathText dataset (Zhang et al., 2024b), which is a collection
of math-related documents originating from web data, papers on arXiv, and code/notebooks on
GitHub. AutoMathText has undergone an automatic selection process using Qwen-72B (Bai et al.,
2023) for relevancy to the mathematical domain and the educational value of each document. Code
and Mathematics data, although not specific to Greek, were included to preserve and enhance the
model’s ability to handle coding tasks, math problems and formal language. Maintaining these
capabilities broadens the utility of Llama-Krikri beyond pure language tasks.
A.2
Pretraining Data Cleaning Pipelines
Our filtering processes began with format standardization in order to facilitate uniform processing across
multiple heterogeneous datasets. We converted all textual content from various formats (e.g., PDF, HTML,
plain text, etc.) into JSONL containing both the document text and relevant metadata such as identified
language, word count, and source information (including source URLs).
For PDF documents such as academic records and laws, we implemented a specialized pipeline which
integrated Marker31 for extraction and conversion into Markdown files, as it exhibits strong performance
for Greek texts. Subsequently, the pipeline included language identification using FastText (Joulin et al.,
2017), removal of markdown artifacts, and removal of lines with characters outside Unicode ranges for
Greek, Latin, and other common and scientific symbols. Furthermore, we utilized document structure
metrics (Marker also extracts various structural metadata) as quality indicators, such as the ratio of tables
to pages and the fraction of removed lines in disallowed scripts.
Our main filtering pipeline used sequential rule-based and statistical filters to remove outlier documents
across all data sources. First, we implemented URL-based filtering by removing content from several
blacklisted domains known to contain low-quality or problematic content. This was particularly effective
for web-crawled datasets like CulturaX (Nguyen et al., 2023) where relevant metadata was available. We
then applied a set of minimal content-quality filters:
• Removal of documents containing multiple instances of profane or inappropriate terms from a curated
list of Greek bad words
• Removal of short documents based on character and word counts
• Removal of documents containing multiple substrings like "lorem ipsum" which are indicative of
content with low educational value
• Removal of documents containing extremely long words (>60 characters)
• Removal of documents with mean word length outside specified values.
• Removal of documents with a high fraction of non-alphanumeric characters.
Parallel datasets were filtered using a different pipeline featuring various steps from previous work
(Papavassiliou et al., 2018; Roussis and Papavassiliou, 2022; Roussis et al., 2024) which include: (a)
rule-based filters, such as length ratio, language identification verification, and (b) model-based alignment
quality scores using tools like LASER (Artetxe and Schwenk, 2018, 2019), BiCleaner AI (Zaragoza-
Bernabeu et al., 2022), and CometKiwi (Rei et al., 2022).
Additionally, in order to mitigate privacy concerns and protect sensitive information, we system-
atically identified and anonymized personally identifiable information (PII) with the use of regular
expressions. In particular, we aimed to detect and replace e-mail addresses with a generic placeholder
(“email@example.gr”) and mask IP addresses (replacing them with 0.0.0.0).
30https://huggingface.co/datasets/code-rag-bench/stackoverflow-posts
31https://github.com/VikParuchuri/marker

--- Page 20 ---

Finally, for Greek, English, and Mathematics/Code datasets we implemented intra-dataset deduplication,
as well as cross-dataset (global) deduplication. We utilized MinHashLSH near-deduplication (Broder,
1997; Leskovec et al., 2020) with 5-gram subsets, a MinHash signature of 128, and a Jaccard similarity
threshold of 0.8, following parameter choices similar to those used in other works (Nguyen et al., 2023;
Voukoutis et al., 2024).
It should be noted that deduplication has consistently been shown to lead to higher performance, reduced
training costs, as well as reduced model memorization; thus indirectly protecting sensitive information
(Lee et al., 2022; Carlini et al., 2023; Grattafiori et al., 2024; Albalak et al., 2024). However, global
deduplication may also remove documents of high quality and actually hurt performance (Tang et al.,
2024; Penedo et al., 2024). For this reason, we decided to upsample datasets of specific sources with
important content, which leads to higher relative importance and also higher memorization (Carlini et al.,
2023; Tang et al., 2024).
Regarding the deduplication of parallel datasets, we followed a different approach. All sentence pairs
were normalized and cleaned, by converting them to lowercase and removing digits, punctuation. Pairs
were then deduplicated based on the existance of either the source or target within the same dataset, thus
ensuring that no sentence can be found multiple times in each parallel dataset (Roussis and Papavassiliou,
2022; Roussis et al., 2024).
Table 1 summarizes the composition of the filtered and deduplicated pretraining corpus. In total, our
collected dataset comprises roughly 91B tokens, of which 62.3% is Greek text. For the final training
curriculum, we upsampled parts of the corpus to effectively train on an equivalent of 110B tokens.
Upsampling was used to give higher relative importance to certain underrepresented but valuable segments
and it also leads to higher memorization of important content (Carlini et al., 2023; Tang et al., 2024). For
example, we assigned a slightly higher weight to datasets with long-context documents, Wikipedia-like
sources, dialogue data, multi-parallel documents, and to certain important domains, such as legal, scientific,
and medical. The decision to include a significant amount of English and parallel data (23.1% and 6%
of tokens, respectively) was guided by prior work (Voukoutis et al., 2024) showing that mixed-language
training can help retain the base model’s general knowledge and prevent catastrophic forgetting.
A.3
Tokenizer Expansion
The tokenizer and embeddings expansion process involved the following steps:
• Data Acquisition: We acquired data by collecting sentences from high-quality sources of our
pretraining mix in five domains:
1. General domain which reuses a sampled portion of the data used to train the tokenizer of
Meltemi (Voukoutis et al., 2024) and covers diverse domains,
2. Legal domain which includes legal texts.
3. Scientific domain which uses publicly available articles, theses, and dissertations.
4. Literature domain from public-domain literature, poetry, and other original writings across
various variants of Greek (e.g., Koine Greek, Medieval Greek, Modern Greek, etc.),
5. Ancient Greek which contains texts only in Ancient Greek.
• Filtering and Preprocessing: Each dataset underwent sequential processing and filtering including
language identification verification with FastText (Joulin et al., 2017), application of regular expres-
sions to remove URLs and other anomalies, symbol-to-word ratio filtering to remove outliers, and
NFC normalization. We then performed sentence-level exact deduplication within each individual
dataset. To ensure text quality, we applied fluency scoring using Monocleaner (Sánchez-Cartagena
et al., 2018) which leverages a 7-gram KenLM model for Greek, and setting a score threshold of 0.3
for non-polytonic text and 0.7 for other texts in Modern Greek.
• Creation of Train and Test Sets: For the tokenizer training and test sets creation, we sampled 50%
of the sentences from each source and divided it into train and test splits (80%–20%).

--- Page 21 ---

• Domain-specific Token Allocation: New tokens were added sequentially for each domain until
tokenizer fertility for this domain remained relatively stable, with most of the tokens being allocated
to the General domain. This approach ensured that common Modern Greek patters receive the largest
coverage, while specialized terminology and older Greek variants are adequately represented.
In Table 8, we list the token allocation per domain, as well as the tokenizer fertilities of Llama-3.1-8B
and Llama-Krikri-8B for each of the five domains for which we created test sets during the tokenizer
extention process. We can observe that tokenizer fertility has dropped significantly across all domains,
with Ancient Greek benefiting from the highest reduction (-1.62) with just 492 added tokens, whereas
fertility for Legal texts has almost halved (1.54 from 2.82) after the integration of a significant number of
tokens (4,000).
Domain
Added Tokens
Llama-3.1-8B
Llama-Krikri-8B
Δ Fertility
General
15,000
2.65
1.59
-1.06
Legal
4,000
2.82
1.54
-1.28
Scientific
1,000
2.91
1.73
-1.18
Literature
500
2.90
1.89
-1.01
Ancient Greek
492
3.77
2.15
-1.62
Total
20,992
–
–
–
Table 8: Domain-specific token allocation and fertility comparison
A.4
Greek Embeddings Expansion & Training
Following the development of the Llama-Krikri-8B tokenizer with 149,248 tokens, containing the initial
Llama 3 reserved tokens to reach a vocabulary size divisible by 256 for computational efficiency, we
expanded the embeddings and lm head layer of our Llama 3 based model to match this vocabulary size.
The newly initialized embeddings and lm head weights for each new token were initialized by averaging
the embeddings (or lm head weights respectively) associated with the tokens retrieved by the initial
Llama-3.1 tokenizer when fed with that token. This provided us with a smoother initial Greek embeddings
and lm head training phase of the frozen model.
Prior to full-scale pretraining, we performed an initial adjustment of the newly introduced token
embeddings with the configuration described in Table 9
Parameter
Value
Base model
Llama-3.1-8B-Base
Training data
5B tokens
Training steps
5,000 steps
Learning rate
1e −3 with cosine decay
Batch size
2M tokens
Optimizer
AdamW
β1 = 0.9, β2 = 0.95, ϵ = 10−5
Weight decay
0.1
Table 9: Greek embeddings training hyperparameters
A.5
Continual Pretraining Process
The continual pretraining phase was conducted over 50 days on two AWS p5e.48xlarge instances (8×
NVIDIA H200 GPUs). Throughout all training phases, we employed bf16 mixed precision to optimize
memory usage and computational efficiency.
We employed a mixed-curriculum strategy during continual pretraining, alternating between chunks of
predominantly Greek text and chunks of other supporting data in a round-robin fashion. Early in training,
we emphasized simpler and higher-quality texts in Greek along with a higher proportion of English
data. As training progressed, we introduced more diverse and complex Greek sources and increased the
proportion of Greek relative to English per batch. This approach is akin to mini-batches containing a blend
of languages, ensuring that every training epoch preserved a presence of English and technical content.
The hyperparameters for both the continual pretraining and annealing phases are presented in Table 10.

--- Page 22 ---

Parameter
Continual Pretraining
Annealing Phase
Training corpus
110B tokens (upsampled)
3.5B + 189M synthetic QA tokens
Context length
128K tokens
128K tokens
Learning rate
Cosine annealing with linear warm-up
Linear decay from 3.0 × 10−5 to 0
over 1% of steps from 0 to 3.0 × 10−4,
decay to 3.0 × 10−5 over 90% of steps
Batch size
∼16M tokens
∼16M tokens
Optimizer
AdamW (β1 = 0.9, β2 = 0.95, ϵ = 10−5)
AdamW (β1 = 0.9, β2 = 0.95, ϵ = 10−5)
Gradient clipping
1.0
1.0
Weight decay
lr × 0.1
lr × 0.1
Parallelization
DeepSpeed Zero 3
DeepSpeed Zero 3
Table 10: Hyperparameters for continual pretraining and annealing phases
A.6
Annealing Phase
For the annealing phase, we conducted experiments with two dataset configurations:
• A curated dataset of 3.5B tokens from high-quality sources across all subcorpora
• The same dataset supplemented with 189M tokens of synthetic question-thinking-answer data
Table 11 shows the results of these experiments on the Greek and English benchmarks that were used
in subsection 4.1 for base models. We can observe that continual pretraining improved Greek (+8.7) but
reduced English (-4) vs Llama-3.1. Annealing with curated data gave modest gains. Most notably, adding
synthetic QA significantly improved Greek (+2.1 vs continual pretraining) and enhanced English beyond
original Llama-3.1 (+0.8).
In the annealing phase, we utilized Liger(Hsu et al., 2024) RMSNorm, RoPE, SwiGLU MLP and fused
cross-entropy kernels to achieve lower memory consumption and higher training speeds, along with the
hyperparameters presented in Table 10.
Training Stage
Avg. Greek
Avg. English
Llama-3.1-8B
48.7
66.2
+ Continual Pretraining
57.4
62.2
+ Curated Corpora
58.0
63.4
+ Synthetic QA Dataset
59.5
67.0
Table 11: Average performance across training stages on Greek and English benchmarks
Parameter
SFT (Stages 1 & 2)
DPO
Training data
856K pairs (Stage 1), 638K pairs (Stage 2)
92K preference triplets
Learning rate
Linear decay from 5.0 × 10−6 to 0 with 3% warmup
Linear decay from 2.5 × 10−7 to 0 over 2 epochs
Batch size
128
32
Optimizer
AdamW (β1 = 0.9, β2 = 0.999, ϵ = 10−5)
AdamW (β1 = 0.9, β2 = 0.999, ϵ = 10−5)
Gradient clipping
1.0
1.0
Weight decay
lr × 0.1
lr × 0.1
Special features
Loss masking on prompt tokens
Length normalization
Table 12: Hyperparameters for supervised fine-tuning and direct preference optimization
A.7
Instruction Tuning and Alignment
The SFT phase was implemented in two distinct stages with progressively increasing data quality and
complexity, so as to incrementally improve the model’s instruction-following capabilities. In Stage 1,
we utilized extended datasets including translated ones, while Stage 2 emphasized higher-quality data
with more complex reasoning patterns. For both stages, training used AdamW (Loshchilov and Hutter,
2017) and we masked the cross-entropy loss of prompt tokens so the model would only learn based on the
completions.
For the DPO phase, we applied length normalization as described by Rafailov et al. (2024). At its core
the DPO objective maximizes the likelihood of preferred responses while minimizing the likelihood of

--- Page 23 ---

dispreferred ones, under a regularization term, while the length normalization term ensures the model is
not biased toward longer responses. This approach helped balance verbosity and brevity, optimizing for
overall usefulness. The final model checkpoint was selected based on the largest margin between preferred
and dispreferred completions during validation. Training used the AdamW (Loshchilov and Hutter, 2017)
optimizer, while Liger(Hsu et al., 2024) RMSNorm, RoPE, SwiGLU MLP, fused cross-entropy kernels,
and fused DPO loss kernels were utilized to achieve lower memory consumption and higher training
speeds during SFT and DPO. The hyperparameters for both are listed in Table 12.

--- Page 24 ---

B
Examples of queries and responses
Ex. 1: Programming: Python Fibonacci function
User: Γράψε μια συνάρτηση Python που υπολογίζει την ακολουθία fibonacci.
Krikri: Ακολουθεί η υλοποίηση της αναδρομικής συνάρτησης Python για τον υπολογισμό των αριθμών Fi-
bonacci:
def fibonacci(n):
"""
Υπολογίζει τον n-οστό αριθμό Fibonacci.
Args:
n (int): θετικός ακέραιος. n >= 0 (0-indexed προσέγγιση)
Returns:
int: ο n-οστός αριθμός Fibonacci
Raises:
ValueError: αν n είναι αρνητικός αριθμός
"""
# ΄Ελεγχος εγκυρότητας εισόδου
if not isinstance(n, int) or n < 0:
raise ValueError("Η είσοδος πρέπει να είναι μη αρνητικός ακέραιος")
# Βάση αναδρομής:
# F(0) = 0, F(1) = 1 (κλασικοί ορισμοί)
if n in (0, 1):
return n
# Αναδρομικός τύπος: F(n) = F(n-1) + F(n-2)
return fibonacci(n-1) + fibonacci(n-2)
Παράδειγμα χρήσης:
# Υπολογισμός μερικών όρων της
# ακολουθίας Fibonacci
for i in range(10):
print(f"F({i}) = {fibonacci(i)}")
# Εκτύπωση αποτελεσμάτων
# F(0) = 0
# F(1) = 1
# F(2) = 1
# F(3) = 2
# F(4) = 3
# F(5) = 5
# F(6) = 8
# F(7) = 13
# F(8) = 21
# F(9) = 34
Ex. 2: Translation: Ancient to Modern Greek
User: Μετάφρασέ μου στα Νέα ελληνικά το κείμενο:
‘Οἱμὲν δὴΜήλιοι τοσαῦτα ἀπεκρίναντο· οἱδὲ᾿Αθηναῖοι διαλυόμενοι ἤδη ἐκ τῶν λόγων ἔφασαν «ἀλλ’ οὖν
μόνοι γε ἀπὸτούτων τῶν βουλευμάτων, ὡς ἡμῖν δοκεῖτε, τὰμὲν μέλλοντα τῶν ὁρωμένων σαφέστερα κρίνετε,
τὰδὲἀφανῆτῷβούλεσθαι ὡς γιγνόμενα ἤδη θεᾶσθε, καὶΛακεδαιμονίοις καὶτύχῃκαὶἐλπίσι πλεῖστον δὴ
παραβεβλημένοι καὶπιστεύσαντες πλεῖστον καὶσφαλήσεσθε.»’
Krikri: Ακολουθεί η μετάφραση του κειμένου στα Νέα Ελληνικά:
Οι Μήλιοι απάντησαν με αυτά τα λόγια. Οι Αθηναίοι, καθώς αποχωρούσαν από τη συζήτηση, είπαν: ‘΄Ομως
εσείς είστε οι μόνοι που από αυτές τις συζητήσεις συμπεραίνετε σωστά τόσο τα ορατά όσο και τα αόρατα, σαν
να έχουν ήδη συμβεί. Είστε υπερβολικά αισιόδοξοι και έχετε εναποθέσει τις ελπίδες σας στους Λακεδαιμο-
νίους, στην τύχη και στις προσδοκίες σας. Και όσο περισσότερο έχετε πιστέψει σε αυτά, τόσο περισσότερο
θα απογοητευτείτε.’

--- Page 25 ---

Ex. 3: Translation to JSON Output: Greek to Multiple Languages
User: Μετάφρασέ μου το παρακάτω κείμενο από τα νέα ελληνικά στα αγγλικά, στα ισπανικά και στα γαλλικά.
Δώσε μου τις μεταφράσεις σε JSON.
Σύμφωνα με την οδηγία 2009/28/ΕΚ του Ευρωπαϊκού Κοινοβουλίου, ως ενέργεια από ανανεώσιμες μη
ορυκτές πηγές θεωρείται η αιολική, ηλιακή, αεροθερμική, γεωθερμική, υδροθερμική και ενέργεια των ωκεανών,
υδροηλεκτρική, από βιομάζα, από τα εκλυόμενα στους χώρους υγειονομικής ταφής αέρια, από αέρια μονάδων
επεξεργασίας λυμάτων και από βιοαέρια.
Krikri:
{
"en":
"According to Directive 2009/28/EC of the European Parliament, energy from renewable
non-fossil sources includes wind, solar, aerothermal, geothermal, hydrothermal and ocean energy,
hydropower, biomass, landfill gas, sewage treatment plant gas and biogases.",
"es": "De conformidad con la Directiva 2009/28/CE del Parlamento Europeo, la energía procedente
de fuentes renovables no fósiles incluye la eólica, solar, aerotérmica, geotérmica, hidrotérmica
y la energía del océano, hidroeléctrica, procedente de la biomasa, de los gases de vertedero,
de los gases de estación depuradora de aguas residuales y de los biogás.",
"fr": "Conformément à la directive 2009/28/CE du Parlement européen, les énergies renouvelables
non fossiles comprennent l’éolien, le solaire, l’aérothermique, la géothermie, l’hydrothermie
et l’énergie océanique, l’hydroélectricité, la biomasse, les gaz de décharge, les gaz de station
d’épuration et les biogaz."
}
Ex. 4: Summarization: Basketball game
User: Μπορείς να δημιουργήσεις μια περίληψη 5 προτάσεων για τον παρακάτω αγώνα μπάσκετ: (User provides
the text of an article describing a 2025 basketball game)
Krikri: Ο Ολυμπιακός νίκησε την Μπαρτσελόνα με 90-88 σε ένα συναρπαστικό παιχνίδι, χάρη σε ένα
νικητήριο καλάθι του Φουρνιέ στην εκπνοή. Ο Βεζένκοφ και ο Γκος σημείωσαν από 24 και 20 πόντους
αντίστοιχα για τους νικητές, ενώ ο Μετού ήταν ο κορυφαίος των Καταλανών με 16 πόντους. Η ομάδα του
Μπαρτζώκα παρέμεινε στην κορυφή της Ευρωλίγκας μετά από αυτή τη σημαντική νίκη.
Ex. 5: History: Population exchange between Greece and Turkey
User: Συνόψισε σε μία παράγραφο την Ελληνοτουρκική ανταλλαγή πληθυσμών του 1923
Krikri: Η Ελληνοτουρκική ανταλλαγή πληθυσμών του 1923, που προβλέφθηκε από τη Συνθήκη της Λωζάνης,
αποτέλεσε μια μαζική μετακίνηση πληθυσμών μεταξύ Ελλάδας και Τουρκίας με στόχο την ομογενοποίηση
των εθνών-κρατών. Περίπου 1,5 εκατομμύριο ΄Ελληνες χριστιανοί, κυρίως από την Ανατολική Θράκη, την
Ιωνία, τον Πόντο και την Καππαδοκία, μετακινήθηκαν στην Ελλάδα, ενώ αντίστοιχα 500.000 Μουσουλμάνοι
(κυρίως Τούρκοι αλλά και Πομάκοι και Αθίγγανοι) μετακινήθηκαν από την Ελλάδα στην Τουρκία. Αυτή η
ανταλλαγή, παρά τις τραγικές της συνέπειες για τους ανθρώπους που εκτοπίστηκαν, αποτέλεσε ένα από τα
σημαντικότερα γεγονότα που διαμόρφωσαν τη σύγχρονη δημογραφική και εθνοτική σύνθεση των δύο χωρών,
οδηγώντας σε μια πιο ομοιογενή εθνική ταυτότητα για κάθε κράτος. Η διαδικασία αυτή ολοκληρώθηκε το
1924 και θεωρείται ορόσημο στις ελληνοτουρκικές σχέσεις.
Ex. 6: High school biology: The process of photosynthesis
User: Δώσε μια σύνοψη της διαδικασίας της φωτοσύνθεσης σε μία παράγραφο.
Krikri: Η φωτοσύνθεση είναι η διαδικασία με την οποία τα φυτά, χρησιμοποιώντας την ηλιακή ενέργεια,
μετατρέπουν το διοξείδιο του άνθρακα (῝Ο2) και το νερό (Η2Ο) σε γλυκόζη (῝6Η12Ο6) και οξυγόνο (Ο2).
Συγκεκριμένα, η χλωροφύλλη στα φύλλα απορροφά φως, διασπά το νερό απελευθερώνοντας οξυγόνο, και
χρησιμοποιώντας το υδρογόνο συνθέτει γλυκόζη από το διοξείδιο του άνθρακα. Η παραγόμενη γλυκόζη
αποτελεί πηγή ενέργειας για το φυτό, ενώ το οξυγόνο απελευθερώνεται στην ατμόσφαιρα ως σημαντικό
παραπροϊόν, υποστηρίζοντας την επιβίωση των αερόβιων οργανισμών.

--- Page 26 ---

Ex. 7: Chain-of-Thought Reasoning: Math problem
System: (Appropriate system prompt used to enable thinking mode)
User: Η Αλίκη έχει ένα καλάθι με μήλα. Δίνει τα 2/5 των μήλων στην αδερφή της και το 1/5 στον αδερφό της.
Τελικά της μένουν 6 μήλα. Πόσα μήλα είχε αρχικά στο καλάθι;
Krikri:
<thinking>
Ας λύσουμε αυτό το πρόβλημα βήμα προς βήμα:
1. ΄Εστω x ο αρχικός αριθμός μήλων που είχε η Αλίκη
2. Γνωρίζουμε ότι:
* Δίνει 2/5 του x στην αδερφή της
* Δίνει 1/5 του x στον αδερφό της
* Μετά από όλα αυτά της μένουν 6 μήλα
3. Ας κάνουμε την εξίσωση:
* Αρχικά είχε: x μήλα
* Της μένουν: 6 μήλα
* ΄Αρα: x - (2/5)x - (1/5)x = 6
* Απλοποιώντας: x - (3/5)x = 6
* Συνδυάζοντας όρους: (2/5)x = 6
* Πολλαπλασιάζοντας και τα δύο μέλη με 5/2:
* x = 15
Ας επαληθεύσουμε:
* Αρχικά είχε 15 μήλα
* Δίνει: 2/5 * 15 = 6 μήλα στην αδερφή της
* Δίνει: 1/5 * 15 = 3 μήλα στον αδερφό της
* Μένουν: 15 - 6 - 3 = 6 μήλα
Η λύση είναι σωστή!
</thinking>
<output>
Η Αλίκη είχε αρχικά 15 μήλα στο καλάθι της.
Μπορούμε να το επαληθεύσουμε:
* ΄Εδωσε 6 μήλα στην αδερφή της (2/5 του συνόλου)
* ΄Εδωσε 3 μήλα στον αδερφό της (1/5 του συνόλου)
* ΄Ετσι της έμειναν 6 μήλα (15 - 6 - 3 = 6)
</output>

```
