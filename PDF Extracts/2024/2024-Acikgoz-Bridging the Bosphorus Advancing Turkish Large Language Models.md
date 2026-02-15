---
title: "2024-Acikgoz-Bridging the Bosphorus Advancing Turkish Large Language Models - PDF Extract"
source_pdf: "2024-Acikgoz-Bridging the Bosphorus Advancing Turkish Large Language Models.pdf"
pages: 32
extracted_at: "2026-02-15T17:51:55.738729"
---

# PDF Extract: 2024-Acikgoz-Bridging the Bosphorus Advancing Turkish Large Language Models

**Source PDF:** 2024-Acikgoz-Bridging the Bosphorus Advancing Turkish Large Language Models.pdf
**Total Pages:** 32

---

## Content

```
--- Page 1 ---

Bridging the Bosphorus
Bridging the Bosphorus: Advancing Turkish Large Lan-
guage Models through Strategies for Low-Resource Language
Adaptation and Benchmarking
Emre Can Acikgoz1,2∗, Mete Erdo˘gan1,2 , Deniz Yuret1,2
1Koc¸ University, KUIS AI Center, 2Koc¸ University, Department of Computer Engineering
https://emrecanacikgoz.github.io/Bridging-the-Bosphorus/
Abstract
Large Language Models (LLMs) are becoming crucial across various fields,
emphasizing the urgency for high-quality models in underrepresented lan-
guages. This study explores the unique challenges faced by low-resource
languages, such as data scarcity, model selection, evaluation, and computa-
tional limitations, with a special focus on Turkish. We conduct an in-depth
analysis to evaluate the impact of training strategies, model choices, and
data availability on the performance of LLMs designed for underrepre-
sented languages. Our approach includes two methodologies: (i) adapting
existing LLMs originally pretrained in English to understand Turkish, and
(ii) developing a model from the ground up using Turkish pretraining
data, both supplemented with supervised fine-tuning on a novel Turkish
instruction-tuning dataset aimed at enhancing reasoning capabilities. The
relative performance of these methods is evaluated through the creation
of a new leaderboard for Turkish LLMs, featuring benchmarks that assess
different reasoning and knowledge skills. Furthermore, we conducted
experiments on data and model scaling, both during pretraining and fine-
tuning, simultaneously emphasizing the capacity for knowledge transfer
across languages and addressing the challenges of catastrophic forgetting
encountered during fine-tuning on a different language. Our goal is to offer
a detailed guide for advancing the LLM framework in low-resource linguis-
tic contexts, thereby making natural language processing (NLP) benefits
more globally accessible.
1
Introduction
The remarkable advancements in Large Language Models (LLMs) have revolutionized the
field of natural language processing (NLP) Brown et al. (2020); OpenAI (2023); Chowdhery
et al. (2022); Anil et al. (2023); Touvron et al. (2023b). However, addressing models that
diverge from an English-centric framework poses considerable challenges, particularly in
low-resource languages. While certain languages like Turkish aren’t categorized as under-
resourced, there’s a limited number of research groups focusing on them Safaya et al. (2022).
Consequently, these languages lag in advancing cutting-edge systems because of the absence
of solid and open-source base LLMs together with standardized benchmarks to evaluate
their capabilities.
Recognizing this gap, our work is motivated by aiming to leverage Turkish LLMs. We
meticulously demonstrate two distinct methodologies: we first tried to adapt two base
LLMs, Mistral-7B Jiang et al. (2023) and GPT2-xl Radford et al. (2019) to Turkish. Secondly,
we trained a family of decoder models entirely from scratch in varying sizes. To adhere the
Turkish LLMs to human instructions and extend their reasoning capabilities, we designed a
novel Turkish instruction-tuning (IT) dataset, designed to enhance the reasoning abilities of
Turkish LLMs by following the Self-Instruct framework Wang et al. (2022b).
∗Corresponding author, eacikgoz17@ku.edu.tr
1
arXiv:2405.04685v1  [cs.CL]  7 May 2024

--- Page 2 ---

Bridging the Bosphorus
One of the key challenges with Turkish LLMs is evaluating their accuracy on different
tasks in a reproducible and fair manner while ensuring dataset quality. Many reasoning
datasets have been directly machine-translated from English without any validation, leading
to biased and inaccurate results. To address this, we introduce two Turkish datasets:
TruthfulQA-TR, for assessing a model’s tendency to reproduce common falsehoods, and
ARC-TR, a set of grade-school science questions. We carefully translated by using state-of-
the-art tools and validated all samples with multiple annotators, cleaning them as needed.
We detailed the translation and annotation processes.
Our contributions are as follows:
• We release the Hamza LLM series, encompassing models from 124M to 1.3B pa-
rameters. Notably, Hamza-xl with 1.3B parameters marks the premier and most
expansive open-source, scientifically vetted Turkish LLM that is trained on 300B
tokens.
• Our analysis explores two distinct methodologies for developing Turkish LLMs
in resource and computational power-constrained environments: (i) extending
pretrained models (Mistral-7b and GPT2-xl) with Turkish-only data (called as
HamzaMistral and HamzaGPT2−xl), and (ii) constructing a model from scratch,
similar to the GPT2 approach. This paper thoroughly discusses the merits and
drawbacks of these strategies.
• We have curated new Turkish evaluation datasets TruthfulQA-TR and ARC-TR by
carefully validating each with multiple annotators, offering meticulously cleaned
datasets, and launching a leaderboard to catalyze ongoing advancements in Turkish
LLMs.
• Committing to open science principles, we make all source codes, model check-
points, and datasets open-source and publicly accessible.
By detailing the development of specialized datasets and methodologies, we offer a compre-
hensive guide for building LLMs for languages with limited resources. Additionally, our
contributions substantially enrich the field by providing critical resources that will support
future research in Turkish language processing and the broader area of Natural Language
Processing (NLP) for under-resourced languages.
2
Datasets
The initial step in building a base LLM involves pretraining it on a vast corpus of text
with a next-token-prediction objective Brown et al. (2020). This corpus comprises trillions
of words gathered from the internet and is characterized by its large volume but often
compromised in quality due to the noise in the raw internet data. Following the pretraining,
the model undergoes fine-tuning with high-quality prompt-response pairs which focuses
on improving the model’s reasoning capabilities Zhang et al. (2023b). In the end, the goal is
to achieve a Supervised-Finetuned (SFT) model that is aligned with the desired response
behavior or domain expertise. This section describes the corpora utilized in the pretraining
phase (Section 2.1) and the development process of the Turkish IT dataset (Section 2.2).
2.1
Pretraining Dataset
For pretraining our models, we utilized CulturaX Nguyen et al. (2023), a substantial multilin-
gual dataset designed for LLM development. This dataset contains 6.3 trillion tokens in 167
languages and is a combination of two well-known multilingual datasets: mC4 Raffel et al.
(2019) and Oscar Abadji et al. (2022); Abadji et al. (2021); Caswell et al. (2021); Ortiz Su’arez
et al. (2020); Ortiz Su’arez et al. (2019). These datasets go through a detailed preprocessing
that involves removing duplications, filtering out URLs, identifying languages, metric-based
cleaning, and refining documents to enhance the data quality and consistency of each corpus.
Since our focus is building a Turkish LLM, we only used the Turkish splits from CulturaX.
2

--- Page 3 ---

Bridging the Bosphorus
mC4.
mC4 Raffel et al. (2019) is a large multilingual dataset initially created for training
the mT5 Xue et al. (2021) which multilingual encoder-decoder model pretrained on 101
different languages. This dataset was generated by extracting content from 71 monthly
snapshots of the internet via Common Crawl (CC). CulturaX contains version 3.1.0 of mC41
which was provided by AllenAI. Its raw dataset contains 337GB of Turkish data.
OSCAR.
OSCAR (Open Super-large Crawled Aggregated coRpus) is a web-based mul-
tilingual dataset that is specialized in offering large volumes of unannotated raw data
commonly used for training large deep learning models. It was developed by efficient data
pipelines to organize and filter web data effectively. The final version of Oscar232 contains
73.7GB of Turkish data.
CulturaX Turkish.
We trained using the Turkish subset of CulturaX3, comprising 128
documents totaling 180 GB. No additional preprocessing was required since CulturaX
had already undergone thorough detailed preprocessing during its creation. In the end,
our Turkish dataset corpus comprises 130B unique tokens determined by using the GPT-2
tokenizer Radford et al. (2019).
Corpus
Documents
Ratio
# of Tokens
mC4
75,859,899
80.52%
104.3 B
OSCAR-2019
5,867,831
6.23%
8.1 B
OSCAR-2109
6,614,512
7.02%
9.1 B
OSCAR-2201
2,580,896
2.74%
3.5 B
OSCAR-2301
3,284,322
3.49%
4.5 B
CulturaX (total)
94,207,460
100.0%
129.5 B
Table 1: Statistics of the pretraining dataset. This table presents the statistics of our
pretraining dataset used to train our Hamza series models that are presented in Table 3.
Corpus Split
Documents
Portion
# of Tokens
CulturaX 0.1GB
36,799
0.05%
0.05 B
CulturaX 0.25GB
91,998
0.14%
0.13 B
CulturaX 0.5GB
183,996
0.28%
0.25 B
CulturaX 1.0GB
367,993
0.56%
0.5 B
CulturaX 2.0GB
735,987
1.11%
1.1 B
CulturaX 5.0GB
1,839,968
2.78%
2.5 B
Table 2: Statistics of the continued pre-training dataset. This table presents the statistics of
our continued pretraining dataset that is used to train HamzaMistral and HamzaGPT2−xl.
2.2
Instruction-Tuning Dataset
Instruction fine-tuning is a crucial method used to improve LLMs in terms of their perfor-
mance and ability to follow specific instructions Zhang et al. (2023a). This phase involves
supervised training of LLMs using an instruction-tuning (IT) dataset composed of instruc-
tion and response pairs that link input instructions to their corresponding response outputs.
Self-Instruct.
To create an automated, high-quality, and diverse IT dataset, we adapt the
Self-Instruct procedure Wang et al. (2022a); Taori et al. (2023) for Turkish. We established
175 diverse instruction and response pairs as seed tasks which are translated manually from
1https://huggingface.co/datasets/mc4
2https://huggingface.co/datasets/oscar-corpus/OSCAR-2301
3https://huggingface.co/datasets/uonlp/CulturaX
3

--- Page 4 ---

Bridging the Bosphorus
Alpaca repository4 by human annotators. These annotators are experts in NLP and native
speakers of both Turkish and English. For the given detailed prompt, we asked text-davinci3
Brown et al. (2020) to generate 20 complex and diverse instruction-response pairs, adhering
strictly to the guidelines specified in the prompt. An example of a prompt is illustrated
in Appendix J. Generated pairs are post-processed by removing any samples that contain
visual context like images or photographs. This process resulted in the creation of 50,817
samples and cost only 8.12$, which were then utilized for supervised fine-tuning (SFT).
3
Methodology
Creating an LLM for under-resourced languages, like Turkish, often poses challenges
primarily due to the scarcity of publicly available data especially if you have limited
computational resources. Regarding these, we followed two different strategies to build
a Turkish series of LLMs: (i) further training state-of-the-art base models on Turkish data,
which was initially unfamiliar with Turkish (i.e., not trained on Turkish data), (ii) pretraining
a model from scratch, following GPT2 scales on a vast amount of text data defined in Section
2.1.
3.1
Method 1: Further Training a Base Model (HamzaMistral and HamzaGPT2−xl)
In this approach, we aim to enhance base LLMs with Turkish linguistic capabilities. After a
detailed evaluation based on perplexity, we selected an LLM that did not specifically train
on Turkish data during its initial pretraining phase. We subjected it to further training using
Turkish-only data, accomplished through the next-token prediction objective implemented
in an autoregressive manner. Essentially, this process can be regarded as a continuation of
the pretraining phase of LLMs, but training on a specific portion of the Turkish dataset this
time.
Selecting Base Model.
For the successful development of an advanced Turkish LLM with
a 7 billion parameter scale, choosing the most suitable base model is essential. To this
end, we have selected Mistral 7B Jiang et al. (2023) as one of our base models, owing to
its recent success across various tasks. Additionally, we opted for GPT2-xlarge, since our
Hamza model is trained from scratch on the GPT2 architecture. This selection allows for a
meaningful comparison between models trained from scratch and those initially trained in
English and subsequently continued with pre-training in the same architectural setup.
Dataset.
In order to inject Turkish into Mistral and GPT-2 base LLMs, we followed a
strategy of incremental continued pretraining on Turkish-specific segments of our dataset.
Beginning with an initial 100MB of pure Turkish data, we progressively expanded the
training corpus, culminating in the model being trained on 5GB of data. This volume
aligns closely with the dataset size used for GPT Radford & Narasimhan (2018), ensuring a
comprehensive and effective adaptation of the model to handle Turkish linguistic nuances.
Please refer to Table 2 for the details of these splits.
Training.
As a continual learning approach, we conducted a series of experiments by
progressively enlarging the pretraining corpus size and halting upon observing convergence.
The models are initialized with the pretraining weights of the Mistral-7B and GPT2-xl and
then further trained on segments of our text corpus with a casual language modeling
objective. Throughout our continued pretraining experiments, we employed LoRA Hu
et al. (2021) and updated only the additional bottleneck adapter weights while freezing
the original model weights to make the training cost-efficient and avoid any catastrophic
forgetting from the models’ previous capabilities. During our LoRA trainings, we used
r = 32 and α = 32, along with a dropout rate of 0.05, applying LoRA exclusively to the
projection layers. We used AdamW optimizer and cosine scheduler with a learning rate
of 0.0001. Based on our experiments, we opted for a batch size of 1 and avoided gradient
accumulation due to its significant impact on convergence. To simplify the execution of our
4Alpaca Repository: https://github.com/tatsu-lab/stanford_alpaca
4

--- Page 5 ---

Bridging the Bosphorus
experiments and ensure the reproducibility of our results, we used the LLaMA-Factory5
repository, only in our LoRA-based continued pretraining experiments.
Model
Parameters
Layers
Heads
dmodel
Learning Rate
Batch Size
Tokens
hamza-small
124M
12
12
768
6.0e−4
0.5M
300B
hamza-medium
354M
24
16
1024
3.0e−4
0.5M
300B
hamza-large
772M
36
20
1280
3.0e−4
0.5M
300B
hamza-xlarge
1.3B
24
16
2048
2.0e−4
0.5M
300B
Table 3: Architecture and optimization hyperparameters for the 4 Hamza model sizes that
trained from scratch.
3.2
Method 2: Pretraining from Scratch (Hamza Series Models)
In our final approach for developing a Turkish base-LLM, we adopted the most straight-
forward method: training from scratch using Turkish-only datasets. We follow a similar
framework as in GPT2 Radford et al. (2019), with similarities in training procedures and
architectural settings. However, we differed in our approach by utilizing a pretraining
corpus nearly double the size of GPT2. All our pretraining code is openly accessible6.
Pretraining Data.
The construction of a robust LLM hinges on the aggregation and pro-
cessing of high-quality text data. To develop Hamza, we used the Turkish split of CulturaX
Nguyen et al. (2023) includes a meticulous process of data curation. It gathers a compre-
hensive dataset from open-sources mC4 Raffel et al. (2019) and OSCAR Abadji et al. (2022);
Abadji et al. (2021); Caswell et al. (2021); Ortiz Su’arez et al. (2020); Ortiz Su’arez et al. (2019).
Our pretraining data contains 128 parquet files each 1.4GB, totaling almost 179.2GB. The
compiled training dataset contains 129,486,207,634 (130B) training tokens. Further details of
the data gathering, structure, and preparation can be found in CulturaX work Nguyen et al.
(2023).
Architecture.
To develop an inaugural Turkish base model, we followed prior works,
establishing a solid model for Turkish language modeling akin to earlier studies on other
languages. Our approach led to the creation of four variants of Hamza, following GPT-2
Radford et al. (2019): Hamza-small (124M parameters), Hamza-medium (354M parameters),
Hamza-large (772M parameters), and our largest model, Hamza-xlarge (1.3B parameters).
The architectural specifications of these models are given in Table 3.
Optimizer.
During our training, AdamW Loshchilov & Hutter (2017) optimizer is used
with hyper-parameters β1 = 0.9 and β2 = 0.95. A cosine learning rate schedule is imple-
mented, designed to reduce the learning rate to 10% of its maximum value. Additionally, we
applied a weight decay rate of 0.1 and limited the gradient norm to 1.0 to prevent overfitting.
The training process includes 2, 000 warm-up steps. We used a learning rate 0f 0.0006 and
batch size 491, 520 in our smallest model Hamza-small. We varied the learning rate and
batch size according to the model size, for details see Table 3.
Training.
Our from-scratch Hamza models are built on the GPT2 architecture Radford et al.
(2019) and incorporate the flash-attention mechanism for efficient training Dao et al. (2022).
As outlined in Table 8, the hyperparameters of the model follow the scaling principles
set by GPT2, except for the largest variant, Hamza-xlarge, which is inspired by a recent
French-based LLM Faysse et al. (2024). All model versions were trained for 300 billion
tokens, with a uniform batch size of 500,000 tokens. The learning rate was fine-tuned for
each model variant. We standardized the context window across all models at 1024 tokens
and did not employ any dropout techniques during their training process. All training
sessions were conducted in half-precision (fp16) settings by utilizing both tensor and data
parallelism across eight A100 GPUs each with 80GB of memory.
5https://github.com/hiyouga/LLaMA-Factory
6https://github.com/emrecanacikgoz/turkish-llm
5

--- Page 6 ---

Bridging the Bosphorus
Type
Models
Accuracy (↑)
BPC (↓)
ARC-TR
TruthfulQA-TR
trnews-64
Base & SFT
Models
LLaMA2 7b
25.94
41.18
1.374
LLaMA3 8b
43.09
44.77
0.929
Mistral 7b
32.68
41.16
1.260
Gemma 2B
31.31
43.57
1.208
Gemma 7B
46.16
42.35
0.989
GPT2-xl
24.91
40.97
2.533
LLaMA2 7b-chat
25.00
40.07
1.374
Mistral 7b-chat-v2
35.24
48.34
1.428
Multi-
lingual
Models
XGLM-7.5B
29.01
39.09
0.880
XGLM-4.5B
25.94
40.18
0.949
XGLM-2.9B
27.05
39.35
0.946
XGLM-1.7B
26.37
41.75
1.044
XGLM-564M
23.55
42.59
1.125
mGPT
26.54
42.37
1.306
Huggingface
Turkish
Models
Kanarya-2b
29.78
41.43
0.724
Kanarya-750m
28.16
41.50
0.767
Turkcell-LLM-7b-v1
43.09
44.91
1.208
ytu-gpt2-large
27.13
43.09
0.805
Trendyol-7b-base
35.24
41.50
0.829
Trendyol-7b-chat
35.58
44.35
0.820
Trendyol-7b-dpo
39.93
50.11
0.859
Commencis-LLM
33.28
44.50
1.306
Sambalingo-tr
44.37
46.61
0.894
Thestral-tr-chat
34.00
41.90
1.314
Mistral-7b-chat-v2-tr
33.96
45.71
1.411
Gemma-2B-tr
31.31
44.46
1.089
Our
Models
Hamza-small
25.26
43.65
0.897
Hamza-medium
26.45
43.55
0.814
Hamza-large
29.10
40.93
0.760
Hamza-xl
28.24
42.33
0.754
HamzaGPT2−xl
24.74
44.95
1.152
HamzaMistral
39.85
46.40
0.816
Table 4: Performance comparison on various Turkish tasks. We compare the performance of
various types of models: (i) Base and SFT Models, (ii) Multilingual Models (iii) Open-Source
HF (Huggingface) Turkish Models, (iv) Our pretrained and adapted Hamza Models. The
first two columns show accuracies evaluated on the ARC-TR and TruthfulQA-TR datasets.
The last column includes the Bits-Per-Character (BPC) metric evaluated on TRNEWS-64
corpus. Note that Accuracy is the highest and BPC is the lowest for the best models. The
top-performing model for each metric is highlighted in bold, while the second-best model is
underlined for easy identification. See Appendix C for model details.
4
Evaluations
4.1
Bits-Per-Character (BPC) Evaluations
Auto-regressive language modeling is trained on optimizing the Negative Log-Likelihood
(NLL) of the data in the training set and the effectiveness of the model is then calculated
on the unseen test data. Furthermore, the most common metric to evaluate these models
is perplexity, which measures the uncertainty of an LLM in predicting the next token in a
sequence and is derived by taking the exponential average of the NLL. However, as various
tokenizers can divide each sentence into differing numbers of tokens, NLL and PPL may
produce incomparable results for models utilizing different tokenizers. To tackle this, we
use Bits-Per-Character (BPC), which is another critical metric derived from NLL, used for
6

--- Page 7 ---

Bridging the Bosphorus
evaluating the performance of LLMs at character-level. Further details on the calculation
of these metrics are given in the Appendix in Section 4.1. Consequently, our comparisons
mainly relied on BPC, which normalizes the impact of tokenization differences. For the BPC
evaluation, we utilized the test set of the trnews-64 corpus Safaya et al. (2022), comprising
5,000 samples.
Results.
We present the BPC results of different models evaluated on trnews-64 in the last
column of Table 4; including our models together with various open-source multi-lingual
and Turkish LLMs. Looking at the BPC results, we observe a wide range of values across the
models. Lower BPC values indicate better performance in terms of compression, suggesting
that the model is more efficient in representing the text. The most favorable outcomes are
attained with the pretrained Kanarya-2b and Hamza-xlarge models. The adapted models
which are originally pretrained on English but extended to Turkish, yielded promising
results as well, lower than 1 BPC, whereas the multilingual models had a relatively lower
performance.
4.2
Prompting & Few-Shot
Evaluating the reasoning capabilities of LLMs in downstream Question Answering (QA)
tasks is crucial to assess their abilities. However, finding such datasets in languages other
than English is challenging due to the limited availability of benchmarks in these languages.
To bridge this gap, we developed TruthfulQA-TR and ARC-TR Turkish question-answering
datasets, that are designed to evaluate the ability of LLMs to generate truthful and accurate
responses to questions. To develop the Turkish version of the main TruthfulQA Multiple
Choice (MC) Lin et al. (2021a) Dataset and ARC (AI2 Reasoning Challenge) Clark et al. (2018)
dataset, we translated each example of these datasets using the advanced DeepL Machine
Translation (MT) framework by its Python-supported API7. After translating to Turkish,
each sample was reviewed for errors or superficial translations. We used the test sets from
TruthfulQA-MC2 and ARC-Challenge for evaluations. For more details on datasets and
annotation validation, see the Appendix in Section G. Our experiments followed the same
prompting settings with LLM-Leaderboard8. We include performances of all of our models
together with all the open-source Turkish LLMs that are available on Huggingface, together
with other monolingual and multilingual models.
Results.
We evaluate various language models in depth, including base LLMs Touvron
et al. (2023b); Jiang et al. (2023); Radford et al. (2019), multilingual LLMs Shliazhko et al.
(2022); Lin et al. (2021b), all available Turkish fine-tuned LLMs on Huggingface, and the
models we propose in this paper. Our evaluation was conducted on the newly established
Turkish Benchmarks, ARC-TR, in 25-shot settings, as well as on TruthfulQA-TR, adhering
to the same settings as outlined by the LLM-Leaderboard. In ARC-TR, Google’s Gemma 7B
model leads with an accuracy of 46.16 even though it is not specifically tuned for Turkish,
closely followed by Sambalingo-tr with 44.37 accuracy. Moreover, in the TruthfulQA-TR
evaluation, Trendyol’s DPO model emerges as the top performer with an accuracy of 50.11,
while Mistral-7b-chat-v2 secures the second position with 48.34 accuracy. The accuracy
scores for ARC-TR range from 24 to 47, and for TruthfulQA-TR, from 33 to 50. These
results underscore the necessity for substantial improvements in these models to reach the
proficiency levels observed in English benchmarks.
Qualitative Analysis.
We performed qualitative analysis on our models by testing them
with various prompts as demonstrated in Appendix in Section I. Both the pretrained and
Hamza models perform well on sentence completion. In particular, compared to other open-
source Turkish models, we observed a reduced tendency to generate text that resembles web-
based content, where most of the Turkish corpora is retrieved from websites. Furthermore,
we tested our models on English prompts to assess their ability to handle multilingual tasks.
Although results indicate that our models can generate coherent responses, there is a high
7https://github.com/DeepLcom/deepl-python
8https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard
7

--- Page 8 ---

Bridging the Bosphorus
tendency for the models to continue English sentences in Turkish. Overall, our qualitative
analysis highlights the robust performance of our models and the potential for diverse
tasks.
5
Case Studies
5.1
Enhancing Non-English Models: Fine-Tuning vs. From-Scratch Training
The analysis of Turkish language models, specifically comparing models trained from
scratch, continued pretraining from GPT2-xl Radford et al. (2019), and those adapted using
Mistral 7B Jiang et al. (2023), shows insightful trends. According to Table 5, the Mistral
7B adapted model exhibits superior performance on Turkish question-answering tasks,
compared to other methods. Moreover, starting from scratch surpasses the continued
pretraining approach within the same model architecture, underscoring the significance of
the base language model when undertaking continued pretraining. This is evidenced by
the discrepancy in accuracy between models fine-tuned from Mistral 7B versus those from
GPT2. Therefore, applying continued pretraining to a robust base language model emerges
as the most effective strategy for low-resource languages, considering both data scarcity
and hardware constraints.
Models
ARC-TR
TruthfulQA-TR
Avg.
Hamza-xl
28.24
42.33
35.28
HamzaGPT2−xl
24.74
44.95
34.84
HamzaMistral
39.85
46.40
43.12
Table 5: Accuracy comparison of our best models on Turkish question answering tasks.
This table shows the performance of our models, pretrained Hamza models with different
sizes, and the HamzaMistral and HamzaGPT2−xl models that are adapted on Turkish. We
present the results evaluated on the ARC-TR (25 shot) and TruthfulQA-TR (6 shot) datasets.
5.2
Effect of Supervised Fine-Tuning: Assessing Model Performance with the Proposed IT
Dataset.
Supervised Fine-Tuning (SFT) plays a crucial role in enhancing the reasoning capabilities of
LLMs, as highlighted in existing research Zhang et al. (2023b). In this context, we introduced
a novel Turkish IT Dataset, meticulously crafted from the ground up, inspired by the Alpaca
Taori et al. (2023); Wang et al. (2022a). By fine-tuning our largest model Hamza-xlarge with
this bespoke Turkish IT Dataset, we observed an improvement in model performance across
downstream benchmarks (see Table 5). This improvement underscores the effectiveness of
SFT when applied to our tailored IT dataset, bolstering our model’s reasoning proficiency
slightly.
Models
ARC-TR
TruthfulQA-TR
Avg.
Hamza-xl
28.24
42.33
35.28
Hamza-xl + SFT
29.61
44.67
37.14
Table 6: Accuracy results of our models fine-tuned on our Self-Instruct IT dataset on
Turkish question answering tasks. This table compares the performance increase after
instruction tuning with dataset IT dataset described in Section 2.2. We present the results
evaluated on the ARC-TR (25 shot) and TruthfulQA-TR (6 shot) datasets.
8

--- Page 9 ---

Bridging the Bosphorus
5.3
Retention after Fine-Tuning: Will Models Forget English-Learned Skills When
Fine-Tuning on Another Language?
According to Table 1, further pretraining of base English language models such as GPT2 and
Mistral results in a decrease in accuracy proportional to the number of samples used during
continued pretraining on the English downstream tasks TruthfulQA and ARC, compared to
their original base scores before fine-tuning on Turkish. This indicates catastrophic forgetting,
where the models lose their prior knowledge upon being fine-tuned on a smaller language
dataset, as evidenced by a decline in baseline accuracy compared to the versions not
previously trained, even after applying techniques like LoRA training. One further work
for this could be including some English data along with Turkish in each batch during
continued pretraining.
Models
ARC
TruthfulQA
Avg.
GPT2-xl
30.29
38.53
34.41
HamzaGPT2−xl (0.1GB)
28.84
38.15
32.98
HamzaGPT2−xl (0.25GB)
26.37
38.10
32.88
HamzaGPT2−xl (0.5GB)
27.13
38.88
33.35
HamzaGPT2−xl (1GB)
26.54
38.95
33.09
HamzaGPT2−xl (2GB)
24.74
40.34
33.01
HamzaGPT2−xl (5GB)
22.61
41.36
32.49
Mistral-7b
61.52
42.57
51.49
HamzaMistral (0.1GB)
56.14
40.31
48.22
HamzaMistral (0.25GB)
52.90
39.15
45.77
HamzaMistral (0.5GB)
52.39
38.70
45.51
HamzaMistral (1GB)
51.71
41.46
46.60
HamzaMistral (2GB)
49.32
38.44
43.91
HamzaMistral (5GB)
45.90
40.90
43.82
0
50M 130M 250M 0.5B 1.1B 2.5B
30
40
50
60
# of Turkish Tokens
English & Turkish ARC Acc.
Comparison of ARC Scores of Mistral Model
ARC-tr Acc.
ARC-eng Acc.
Figure 1: Accuracy comparison of Continued Pretrained models on English (Left, Right)
and Turkish (Right) question answering tasks and demonstrating the original language
catastrophic forgetting while learning the new language. In the table on the left, the
performance of our HamzaMistral and HamzaGPT2−xl models that are adapted on Turkish
together with the original Mistral 7B and GPT2-xl. We present the result of our ablation
study, where the performance of the adapted models is given by progressively enlarging the
pretraining corpus size from 0.1 GB to 5 GB. Here, the zero and few-show accuracies were
evaluated on the original ARC and TruthfulQA. The figure on the right illustrates the Mistral
model’s results on both Turkish and English versions of the ARC dataset, highlighting its
improved performance in Turkish and decreasing performance in English with continued
pretraining.
6
Conclusion
Our work advances the development of Turkish LLMs, presenting a new series of models
both trained from scratch (Hamza) and also adapted from other base LLMs (HamzaMistral
and HamzaGPT2−xl), together with new Instruction Tuning dataset and a meticulously
crafted Turkish LLM Leaderboard. In our analysis, we noted that the base LLMs exhibited
catastrophic forgetting of their primary language knowledge during continued pretraining.
Additionally, through the creation of a novel Turkish LLM evaluation benchmark, we
have identified a significant performance gap between current Turkish LLMs and their
English counterparts, underscoring the need for further improvements in Turkish language
modeling. For more detailed discussions on limitations and future work, please refer to
Appendix B. Our fully open-source work and detailed observations play a pivotal role in
the field of Turkish language modeling, providing insights on construction methodologies
and offering a comparative framework for evaluating performance, thereby paving the way
for future advancements.
9

--- Page 10 ---

Bridging the Bosphorus
Acknowledgments
We extend our heartfelt gratitude to Kerem Zaman and Abdullatif K¨oksal for their ex-
ceptional support when needed. We also thank Ekin Aky¨urek for his insightful advice
and in-depth discussions. Also, thanks to Ali Safaya for his assistance in organizing the
benchmark annotation process. Additionally, we are grateful to all the dedicated annotators
from Koc¸ University students. On the other hand, this work is supported in part provided
by the KUIS AI Center. Finally, special thanks to HyperBee AI for their help during model
evaluations. The numerical calculations reported in this paper were fully/partially per-
formed at TUBITAK ULAKBIM, High Performance and Grid Computing Center (TRUBA
resources). Last but not least, we also acknowledge VSB – Technical University of Ostrava,
IT4Innovations National Supercomputing Center, Czech Republic, for awarding this project
access to the LUMI supercomputer, owned by the EuroHPC Joint Undertaking, hosted by
CSC (Finland) and the LUMI consortium through the Ministry of Education, Youth and
Sports of the Czech Republic through the e-INFRA CZ.
References
Julien Abadji, Pedro Javier Ortiz Su´arez, Laurent Romary, and Benoˆıt Sagot. Ungoliant:
An optimized pipeline for the generation of a very large-scale multilingual web corpus.
Proceedings of the Workshop on Challenges in the Management of Large Corpora (CMLC-
9) 2021. Limerick, 12 July 2021 (Online-Event), pp. 1 – 9, Mannheim, 2021. Leibniz-Institut
f¨ur Deutsche Sprache. doi: 10.14618/ids-pub-10468. URL https://nbn-resolving.org/
urn:nbn:de:bsz:mh39-104688.
Julien Abadji, Pedro Ortiz Suarez, Laurent Romary, and Benoˆıt Sagot. Towards a Cleaner
Document-Oriented Multilingual Crawled Corpus. arXiv e-prints, art. arXiv:2201.06642,
January 2022.
Joshua Ainslie, James Lee-Thorp, Michiel de Jong, Yury Zemlyanskiy, Federico Lebr’on, and
Sumit K. Sanghai. Gqa: Training generalized multi-query transformer models from multi-
head checkpoints. ArXiv, abs/2305.13245, 2023. URL https://api.semanticscholar.
org/CorpusID:258833177.
Rohan Anil, Andrew M. Dai, Orhan Firat, Melvin Johnson, Dmitry Lepikhin, Alexan-
dre Tachard Passos, Siamak Shakeri, Emanuel Taropa, Paige Bailey, Z. Chen, Eric Chu,
J. Clark, Laurent El Shafey, Yanping Huang, Kathleen S. Meier-Hellstern, Gaurav Mishra,
Erica Moreira, Mark Omernick, Kevin Robinson, Sebastian Ruder, Yi Tay, Kefan Xiao,
Yuanzhong Xu, Yujing Zhang, Gustavo Hernandez Abrego, Junwhan Ahn, Jacob Austin,
Paul Barham, Jan A. Botha, James Bradbury, et al. Palm 2 technical report. ArXiv,
abs/2305.10403, 2023. URL https://api.semanticscholar.org/CorpusID:258740735.
Iz Beltagy, Matthew E. Peters, and Arman Cohan.
Longformer: The long-document
transformer. ArXiv, abs/2004.05150, 2020. URL https://api.semanticscholar.org/
CorpusID:215737171.
Stella Biderman, Hailey Schoelkopf, Quentin Anthony, Herbie Bradley, Kyle O’Brien, Eric
Hallahan, Mohammad Aflah Khan, Shivanshu Purohit, USVSN Sai Prashanth, Edward
Raff, Aviya Skowron, Lintang Sutawika, and Oskar van der Wal. Pythia: A suite for
analyzing large language models across training and scaling, 2023.
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla
Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini
Agarwal, Ariel Herbert-Voss, Gretchen Krueger, T. J. Henighan, Rewon Child, Aditya
Ramesh, Daniel M. Ziegler, Jeff Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric
Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam
McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are
few-shot learners. ArXiv, abs/2005.14165, 2020. URL https://api.semanticscholar.
org/CorpusID:218971783.
10

--- Page 11 ---

Bridging the Bosphorus
Isaac Caswell, Julia Kreutzer, Lisa Wang, Ahsan Wahab, Daan van Esch, Nasanbayar
Ulzii-Orshikh, Allahsera Tapo, Nishant Subramani, Artem Sokolov, Claytone Sikasote,
Monang Setyawan, Supheakmungkol Sarin, Sokhar Samb, Benoˆıt Sagot, Clara Rivera,
Annette Rios, Isabel Papadimitriou, Salomey Osei, Pedro Javier Ortiz Su´arez, Iroro Orife,
Kelechi Ogueji, Rubungo Andre Niyongabo, Toan Q. Nguyen, Mathias M¨uller, Andr´e
M¨uller, Shamsuddeen Hassan Muhammad, Nanda Muhammad, Ayanda Mnyakeni, ,
Jamshidbek Mirzakhalov, Tapiwanashe Matangira, et al. Quality at a Glance: An Audit
of Web-Crawled Multilingual Datasets. arXiv e-prints, art. arXiv:2103.12028, March 2021.
Rewon Child, Scott Gray, Alec Radford, and Ilya Sutskever. Generating long sequences with
sparse transformers. ArXiv, abs/1904.10509, 2019. URL https://api.semanticscholar.
org/CorpusID:129945531.
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra,
Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann,
Parker Schuh, Kensen Shi, Sasha Tsvyashchenko, Joshua Maynez, Abhishek Rao, Parker
Barnes, Yi Tay, Noam M. Shazeer, Vinodkumar Prabhakaran, Emily Reif, Nan Du, Ben-
ton C. Hutchinson, Reiner Pope, James Bradbury, Jacob Austin, Michael Isard, Guy
Gur-Ari, Pengcheng Yin, Toju Duke, Anselm Levskaya, et al. Palm: Scaling language mod-
eling with pathways. ArXiv, abs/2204.02311, 2022. URL https://api.semanticscholar.
org/CorpusID:247951931.
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick,
and Oyvind Tafjord. Think you have solved question answering? try arc, the ai2 reasoning
challenge. arXiv:1803.05457v1, 2018.
Jacob Cohen. A coefficient of agreement for nominal scales. Educational and Psychological
Measurement, 20(1):37–46, 1960. doi: 10.1177/001316446002000104. URL https://doi.
org/10.1177/001316446002000104.
Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and Christopher R’e. Flashattention: Fast
and memory-efficient exact attention with io-awareness. ArXiv, abs/2205.14135, 2022.
URL https://api.semanticscholar.org/CorpusID:249151871.
Manuel Faysse, Patrick Fernandes, Nuno M. Guerreiro, Ant’onio Loison, Duarte M. Alves,
Caio Corro, Nicolas Boizard, Joao Alves, Ricardo Rei, Pedro H. Martins, Antoni Bi-
gata Casademunt, Franccois Yvon, Andr´e Martins, Gautier Viaud, C’eline Hudelot, and
Pierre Colombo. Croissantllm: A truly bilingual french-english language model. ArXiv,
abs/2402.00786, 2024. URL https://api.semanticscholar.org/CorpusID:267365133.
Joseph L. Fleiss. Measuring nominal scale agreement among many raters. Psychological
Bulletin, 76(5):378–382, 1971.
Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai,
Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark,
Tom Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc,
Aurelia Guy, Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals,
and L. Sifre. Training compute-optimal large language models. ArXiv, abs/2203.15556,
2022. URL https://api.semanticscholar.org/CorpusID:247778764.
J. Edward Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang,
and Weizhu Chen.
Lora: Low-rank adaptation of large language models.
ArXiv,
abs/2106.09685, 2021. URL https://api.semanticscholar.org/CorpusID:235458009.
Albert Qiaochu Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Deven-
dra Singh Chaplot, Diego de Las Casas, Florian Bressand, Gianna Lengyel, Guillaume
Lample, Lucile Saulnier, L’elio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock,
Teven Le Scao, Thibaut Lavril, Thomas Wang, Timoth´ee Lacroix, and William El Sayed.
Mistral 7b. ArXiv, abs/2310.06825, 2023. URL https://api.semanticscholar.org/
CorpusID:263830494.
Stephanie Lin, Jacob Hilton, and Owain Evans. Truthfulqa: Measuring how models mimic
human falsehoods, 2021a.
11

--- Page 12 ---

Bridging the Bosphorus
Xi Victoria Lin, Todor Mihaylov, Mikel Artetxe, Tianlu Wang, Shuohui Chen, Daniel Simig,
Myle Ott, Naman Goyal, Shruti Bhosale, Jingfei Du, Ramakanth Pasunuru, Sam Shleifer,
Punit Singh Koura, Vishrav Chaudhary, Brian O’Horo, Jeff Wang, Luke Zettlemoyer, Zor-
nitsa Kozareva, Mona T. Diab, Ves Stoyanov, and Xian Li. Few-shot learning with multilin-
gual generative language models. In Conference on Empirical Methods in Natural Language
Processing, 2021b. URL https://api.semanticscholar.org/CorpusID:245334784.
Ilya Loshchilov and Frank Hutter. Fixing weight decay regularization in adam. ArXiv,
abs/1711.05101, 2017. URL https://api.semanticscholar.org/CorpusID:3312944.
Thuat Nguyen, Chien Van Nguyen, Viet Dac Lai, Hieu Man, Nghia Trung Ngo, Franck
Dernoncourt, Ryan A. Rossi, and Thien Huu Nguyen. Culturax: A cleaned, enormous,
and multilingual dataset for large language models in 167 languages, 2023.
OpenAI.
Gpt-4 technical report.
ArXiv, abs/2303.08774, 2023.
URL https://api.
semanticscholar.org/CorpusID:257532815.
Pedro Javier Ortiz Su’arez, Benoit Sagot, and Laurent Romary. Asynchronous pipelines for
processing huge corpora on medium to low resource infrastructures. Proceedings of the
Workshop on Challenges in the Management of Large Corpora (CMLC-7) 2019. Cardiff,
22nd July 2019, pp. 9 – 16, Mannheim, 2019. Leibniz-Institut f”ur Deutsche Sprache. doi:
10.14618/ids-pub-9021. URL http://nbn-resolving.de/urn:nbn:de:bsz:mh39-90215.
Pedro Javier Ortiz Su’arez, Laurent Romary, and Benoit Sagot. A monolingual approach
to contextualized word embeddings for mid-resource languages. In Proceedings of the
58th Annual Meeting of the Association for Computational Linguistics, pp. 1703–1714, Online,
July 2020. Association for Computational Linguistics. URL https://www.aclweb.org/
anthology/2020.acl-main.156.
Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin,
Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob
Hilton, Fraser Kelton, Luke E. Miller, Maddie Simens, Amanda Askell, Peter Welinder,
Paul Francis Christiano, Jan Leike, and Ryan J. Lowe. Training language models to
follow instructions with human feedback. ArXiv, abs/2203.02155, 2022. URL https:
//api.semanticscholar.org/CorpusID:246426909.
Alec Radford and Karthik Narasimhan. Improving language understanding by generative
pre-training. 2018. URL https://api.semanticscholar.org/CorpusID:49313245.
Alec Radford, Jeff Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever.
Language models are unsupervised multitask learners. 2019.
Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning,
and Chelsea Finn. Direct preference optimization: Your language model is secretly a
reward model. ArXiv, abs/2305.18290, 2023. URL https://api.semanticscholar.org/
CorpusID:258959321.
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena,
Yanqi Zhou, Wei Li, and Peter J. Liu. Exploring the limits of transfer learning with a
unified text-to-text transformer. arXiv e-prints, 2019.
Ali Safaya, Emirhan Kurtulus¸, Arda Goktogan, and Deniz Yuret. Mukayese: Turkish NLP
strikes back. In Smaranda Muresan, Preslav Nakov, and Aline Villavicencio (eds.), Findings
of the Association for Computational Linguistics: ACL 2022, pp. 846–863, Dublin, Ireland, May
2022. Association for Computational Linguistics. doi: 10.18653/v1/2022.findings-acl.69.
URL https://aclanthology.org/2022.findings-acl.69.
Teven Le Scao, Angela Fan, Christopher Akiki, Ellie Pavlick, Suzana Ili’c, Daniel Hesslow,
Roman Castagn’e, Alexandra Sasha Luccioni, Franccois Yvon, Matthias Gall´e, Jonathan
Tow, Alexander M. Rush, Stella Rose Biderman, Albert Webson, Pawan Sasanka Ammana-
manchi, Thomas Wang, Benoˆıt Sagot, Niklas Muennighoff, Albert Villanova del Moral,
Olatunji Ruwase, Rachel Bawden, Stas Bekman, Angelina McMillan-Major, Iz Beltagy,
12

--- Page 13 ---

Bridging the Bosphorus
Huu Nguyen, Lucile Saulnier, Samson Tan, Pedro Ortiz Suarez, Victor Sanh, Hugo Lau-
renccon, et al. Bloom: A 176b-parameter open-access multilingual language model. ArXiv,
abs/2211.05100, 2022. URL https://api.semanticscholar.org/CorpusID:253420279.
Stefan Schweter. Berturk - bert models for turkish, April 2020. URL https://doi.org/10.
5281/zenodo.3770924.
Oleh Shliazhko, Alena Fenogenova, Maria Tikhonova, Vladislav Mikhailov, Anastasia
Kozlova, and Tatiana Shavrina.
mgpt: Few-shot learners go multilingual.
ArXiv,
abs/2204.07580, 2022. URL https://api.semanticscholar.org/CorpusID:248227518.
Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li, Carlos Guestrin,
Percy Liang, and Tatsunori B. Hashimoto. Stanford alpaca: An instruction-following
llama model. https://github.com/tatsu-lab/stanford_alpaca, 2023.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux,
Timoth´ee Lacroix, Baptiste Rozi`ere, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien
Rodriguez, Armand Joulin, Edouard Grave, and Guillaume Lample. Llama: Open
and efficient foundation language models. ArXiv, abs/2302.13971, 2023a. URL https:
//api.semanticscholar.org/CorpusID:257219404.
Hugo Touvron, Louis Martin, Kevin R. Stone, Peter Albert, Amjad Almahairi, Yasmine
Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Daniel M.
Bikel, Lukas Blecher, Cristian Canton Ferrer, Moya Chen, Guillem Cucurull, David
Esiobu, Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia Gao, Vedanuj
Goswami, Naman Goyal, Anthony S. Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan,
Marcin Kardas, Viktor Kerkez, Madian Khabsa, Isabel M. Kloumann, A. V. Korenev,
Punit Singh Koura, Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Diana Liskovich,
Yinghai Lu, Yuning Mao, Xavier Martinet, Todor Mihaylov, Pushkar Mishra, Igor Molybog,
Yixin Nie, Andrew Poulton, Jeremy Reizenstein, Rashi Rungta, Kalyan Saladi, Alan
Schelten, Ruan Silva, Eric Michael Smith, R. Subramanian, Xia Tan, Binh Tang, Ross
Taylor, Adina Williams, Jian Xiang Kuan, Puxin Xu, Zhengxu Yan, Iliyan Zarov, Yuchen
Zhang, Angela Fan, Melanie Kambadur, Sharan Narang, Aurelien Rodriguez, Robert
Stojnic, Sergey Edunov, and Thomas Scialom. Llama 2: Open foundation and fine-tuned
chat models. ArXiv, abs/2307.09288, 2023b. URL https://api.semanticscholar.org/
CorpusID:259950998.
G¨okc¸e Uludo˘gan, Zeynep Yirmibes¸o˘glu Balal, Furkan Akkurt, Meliks¸ah T¨urker, Onur
G¨ung¨or, and Susan ¨Usk¨udarlı. Turna: A turkish encoder-decoder language model for
enhanced understanding and generation, 2024.
Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi,
and Hannaneh Hajishirzi. Self-instruct: Aligning language models with self-generated
instructions. In Annual Meeting of the Association for Computational Linguistics, 2022a. URL
https://api.semanticscholar.org/CorpusID:254877310.
Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi,
and Hannaneh Hajishirzi. Self-instruct: Aligning language models with self-generated
instructions. In Annual Meeting of the Association for Computational Linguistics, 2022b. URL
https://api.semanticscholar.org/CorpusID:254877310.
Linting Xue, Noah Constant, Adam Roberts, Mihir Kale, Rami Al-Rfou, Aditya Siddhant,
Aditya Barua, and Colin Raffel. mT5: A massively multilingual pre-trained text-to-text
transformer. In Kristina Toutanova, Anna Rumshisky, Luke Zettlemoyer, Dilek Hakkani-
Tur, Iz Beltagy, Steven Bethard, Ryan Cotterell, Tanmoy Chakraborty, and Yichao Zhou
(eds.), Proceedings of the 2021 Conference of the North American Chapter of the Association for
Computational Linguistics: Human Language Technologies, pp. 483–498, Online, June 2021.
Association for Computational Linguistics. doi: 10.18653/v1/2021.naacl-main.41. URL
https://aclanthology.org/2021.naacl-main.41.
13

--- Page 14 ---

Bridging the Bosphorus
Shengyu Zhang, Linfeng Dong, Xiaoya Li, Sen Zhang, Xiaofei Sun, Shuhe Wang, Ji-
wei Li, Runyi Hu, Tianwei Zhang, Fei Wu, and Guoyin Wang.
Instruction tuning
for large language models: A survey.
ArXiv, abs/2308.10792, 2023a.
URL https:
//api.semanticscholar.org/CorpusID:261049152.
Shengyu Zhang, Linfeng Dong, Xiaoya Li, Sen Zhang, Xiaofei Sun, Shuhe Wang, Ji-
wei Li, Runyi Hu, Tianwei Zhang, Fei Wu, and Guoyin Wang.
Instruction tuning
for large language models: A survey.
ArXiv, abs/2308.10792, 2023b.
URL https:
//api.semanticscholar.org/CorpusID:261049152.
Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen,
Christopher Dewan, Mona T. Diab, Xian Li, Xi Victoria Lin, Todor Mihaylov, Myle Ott,
Sam Shleifer, Kurt Shuster, Daniel Simig, Punit Singh Koura, Anjali Sridhar, Tianlu Wang,
and Luke Zettlemoyer. Opt: Open pre-trained transformer language models. ArXiv,
abs/2205.01068, 2022. URL https://api.semanticscholar.org/CorpusID:248496292.
14

--- Page 15 ---

Bridging the Bosphorus
Appendix
A Related Work
16
B
Limitations and Future Work
16
C Models
17
D Training Hardware and GPU hours
19
E
Hamza Model Configuration Details
19
F
Evaluation Metrics
20
G Truthful-TurkishQA and Arc-Challange-TR Annotation Evaluations
20
H TruthfulQA-TR and ARC-TR Examples
22
I
Sample Model Outputs
24
J
Turkish Instruction-Tuning (IT) Dataset Creation Prompts
32
15

--- Page 16 ---

Bridging the Bosphorus
A
Related Work
LLMs have significantly advanced the field of NLP by demonstrating remarkable capabilities
in generating human-like text across various domains Radford et al. (2019); Zhang et al.
(2022); Anil et al. (2023); Jiang et al. (2023); OpenAI (2023). Their development illustrates not
only improvements in model size and complexity Hoffmann et al. (2022); Biderman et al.
(2023) but also in their ability to understand and generate more nuanced and contextually
appropriate responses through techniques such as fine-tuning, supervised instruction-
tuning, and reinforcement learning from human feedback (RLHF) Ouyang et al. (2022);
Wang et al. (2022a); Taori et al. (2023); Rafailov et al. (2023). Investigation into these models,
focusing on overcoming their constraints for low-resource languages and furthering their
development, remains a vital pursuit for achieving global applicability.
Multilingual LLMs represent a significant leap forward, enabling a single model to under-
stand and generate text across multiple languages Scao et al. (2022); Shliazhko et al. (2022);
Lin et al. (2021b), thereby bridging linguistic gaps on a global scale. By leveraging vast
datasets from diverse linguistic sources Nguyen et al. (2023), these models are trained to
capture the nuances of language, culture, and context. However, the inherent limitations
posed by the restricted vocabulary sizes and diverse morphological characteristics of each
language present substantial challenges that necessitate ongoing refinement and innovation
within these models.
Regarding the Turkish context, although Turkish is not classified as a low-resource language,
it has attracted limited research focus, with only a handful of groups dedicating efforts.
The landscape of Turkish NLP is beginning to shine with the advent of new evaluation
datasets Safaya et al. (2022) and some language models. However, these advancements
are predominantly in encoder-based Schweter (2020) or encoder-decoder-based models
Uludo˘gan et al. (2024) which necessitates task-specific training by leaving a gap in generative
LLM work tailored specifically for Turkish. Consequently, there is an absence of pioneering
research that offers insights for advancing the field of Turkish LLMs, underscoring the
urgent need for a comprehensive strategy to develop robust Turkish-based LLMs.
B
Limitations and Future Work
Better Turkish Pretraining Corpora.
The accuracy of your pretraining corpus is one of
the most crucial factors in achieving a well-performing LLM. The three key elements of a
good dataset are: quality, diversity, and quantity. While the last element is easy to measure,
performance is a function of all three9. Our models are trained on 300 billion tokens, LLaMA
Touvron et al. (2023a) is trained on 1.5 trillion tokens, and LLaMA 3 is trained on 15 trillion
tokens. We need more Turkish data, at least 3 trillion tokens. However, the diversity of
these datasets should be sufficient, including common crawl, book corpora, code, math,
etc., in a balanced manner. Current Turkish LLMs are trained on MC4 Raffel et al. (2019)
and OSCAR-based Abadji et al. (2022) datasets with minimal preprocessing. These datasets
mostly include political, gambling, or sports-related data, resulting in biased outcomes. The
measurement of dataset quality is still an important research question today. We firmly
believe that better data is better than better models.
Small Scale of the Proposed Models.
One of the objectives of our work is not merely
to provide the largest or best-performing Turkish LLM but also to offer a clear pathway
and framework for building robust LLMs in low-resource scenarios. For instance, we
trained all our models using, at most, eight A100 GPUs in parallel. Our Hamza-xlarge
model, with 1.3B parameters, is the largest and best-performing open-source, decoder-based
model that is scientifically published for Turkish. However, the Turkish language requires
better pre-trained models, scaling up to at least 7B, 13B, and 30B parameters, with high-
quality datasets, to achieve results comparable to models like Mistral performed in English.
Achieving this requires more GPUs and larger cluster environments. Currently, the largest
clusters in Turkey are owned by T ¨UB˙ITAK TRUBA and Koc¸ University KUIS AI Center.
9https://x.com/karpathy/status/1782798789797101876?s=46
16

--- Page 17 ---

Bridging the Bosphorus
However, Turkish needs more H100 and A100 GPUs, with at least 512 GPUs supporting
multi-node training, to develop LLMs comparable to those in other languages. We also
explore whether training a model from scratch in low-resource settings is worthwhile or if
fine-tuning from a strong base model is more effective. At present, adapting a base LLM
like Mistral appears more promising; however, it also leads to catastrophic forgetting (see
Section 5).
Limited Performance of Current Turkish LLMs.
Upon examining Table 4, it is evident
that the current Turkish LLMs available on Huggingface perform significantly worse than
base models like LLaMA, Mistral, and Gemma, which excel at the same tasks in English.
The Turkish results range from 24 to 46 in ARC-TR and 39 to 50 in TruthfulQA-TR. Even
Gemma 7B achieves the best performance in ARC-TR without any specific fine-tuning for
Turkish. This highlights the considerable room for improvement, as discussed earlier, to
develop better LLMs in Turkish.
More Diverse Turkish Evaluation Benchmarks.
In this work, we shared two new eval-
uation datasets for Turkish: TruthfulQA-TR and ARC-TR. These datasets test a model’s
propensity to reproduce falsehoods commonly found online, and its ability to answer grade-
school science questions, respectively. However, robust LLMs should also be evaluated in
more challenging areas, such as chat abilities, mathematical reasoning, ethical biases, and
more. We are currently working on establishing and sharing scientific datasets in these areas
as well. Collaborations are always welcome.
C
Models
GPT2-xl.
GPT2 Radford et al. (2019) introduces several scaled models with the largest
one as 1.5B parameter, which significantly expands upon its predecessor by enhancing its
capacity for unsupervised learning of natural language tasks. This model demonstrates
notable improvements in language understanding and generation, outperforming earlier
versions in a range of linguistic tasks without task-specific training. GPT2-xl’s architecture
builds on the decoder-based transformer model by enabling it to generate coherent and
contextually relevant text over extended passages. We used GPT2-xl in our evaluations.
XGLM.
XGLM Lin et al. (2021b) presented with five multilingual generative language
models, with up to 7.5 billion parameters. The models are trained on a large-scale corpus of
500 billion tokens across 30 diverse languages, balancing representation for low-resourced
languages. The study explores the models’ zero-shot and few-shot learning capabilities
across various tasks, including multilingual NLU, machine translation, and specific English
tasks. The largest model, XGLM-7.5B, outperforms GPT-3 in multilingual commonsense
reasoning and natural language inference tasks. We evaluated XGLM-7.5B, XGLM-4.5B,
XGLM-2.9B, XGLM-1.7B, and XGLM-564M.
mGPT.
mGPT Shliazhko et al. (2022) is introduced with two different scales: 1.3 billion
and 13 billion parameters. These models are trained on 60 languages from 25 language
families, using data from Wikipedia and the Colossal Clean Crawled Corpus. The models
replicate the GPT-3 architecture using GPT-2 sources and a sparse attention mechanism.
The training and inference processes are effectively parallelized using the Deepspeed and
Megatron frameworks. We used mGPT from Huggingface.
LLaMA Models.
LLaMA Touvron et al. (2023a) is a collection of open-source LLMs
released by Meta, ranging from 7B to 65B parameters, achieved state-of-the-art performance
using publicly available datasets. LLaMA 2 Touvron et al. (2023b), an enhanced version,
expanded its training corpus and context length, releasing models with 7B, 13B, and 70B
parameters, together with introducing LLaMA 2 Chat for dialogue. Recently, LLaMA 3
was released and further improved efficiency and performance, utilizing a larger tokenizer
and adopting grouped-query attention, resulting in state-of-the-art models at 8B and 70B
parameter scales, with training based on over 15T publicly sourced tokens. During our
evaluations, we used LLaMA2 7b, LLaMA2 7b-chat, and LLaMA3 8b.
17

--- Page 18 ---

Bridging the Bosphorus
Mistral 7B.
Mistral 7b Jiang et al. (2023) is a new state-of-the-art 7-billion-parameter LLM
known for its high performance and efficiency. It surpasses other larger models, including
13b-parameter models like LLaMA2 Touvron et al. (2023b) and 34-billion-parameter model
like LLaMA Touvron et al. (2023a), in various areas such as reasoning, mathematics, and
code generation. The model incorporates grouped-query attention (GQA) Ainslie et al.
(2023) for quicker inference and sliding window attention (SWA) Child et al. (2019); Beltagy
et al. (2020) to handle long sequences cost-effectively. During our evaluations, we utilized
Mistral 7b and Mistral 7b-chat-v2.
Gemma.
Gemma, released by Google, is a family of lightweight, state-of-the-art open
models derived from the technology behind Gemini models. These models excel in language
understanding, reasoning, and safety, and are available in 2B and 7B parameter sizes.
Gemma outperforms similarly sized open models on 11 out of 18 text-based tasks, and
includes comprehensive evaluations of safety and responsibility aspects, along with detailed
development information. We used Gemma 2B and Gemma 7B from Huggingface.
Kanarya.
Kanarya LLMs are pre-trained Turkish GPT-J models from scratch. It comprises
two versions: kanarya-2b and kanarya-750m, with 2 billion and 750 million parameters,
respectively. Both models are trained on a large-scale Turkish text corpus derived from
OSCAR and mC4 datasets, which include diverse sources like news, articles, and websites.
The models use a JAX/Flax implementation of the GPT-J architecture and feature rotary
positional embeddings. The larger kanarya-2b has 24 layers, a hidden size of 2560, and 20
attention heads, while the smaller kanarya-750m has 12 layers, a hidden size of 2048, and 16
attention heads. Both models have a context size of 2048 and a vocabulary size of 32,768.
We used both kanarya-2b and kanarya-750m during our evaluations.
Turkcell LLM 7b.
Turkcell-LLM-7b-v1 is an enhanced version of a Mistral-based LLM
tailored specifically for the Turkish language. The model was initially trained on a cleaned
dataset comprising 5 billion Turkish tokens using the DORA method. Subsequently, it
underwent fine-tuning with the LORA method, utilizing Turkish instruction sets compiled
from various open-source and internal resources. The model’s tokenizer was specially
extended for Turkish, enhancing its language capabilities. Its training dataset consisted
of cleaned Turkish raw data and custom instruction sets. The DORA method featured a
configuration with alpha value of 128, LoRA dropout of 0.05, rank of 64, and targeted all
linear modules. We also evaluated Turkcell-LLM-7b-v1 in our results table.
Trendyol 7b LLMs.
Trendyol LLMs are generative language models based on Mistral 7B,
using an optimized transformer architecture. It features three versions: a base model, a chat
model, and a DPO model, all fine-tuned with LoRA on varying token and instruction set
sizes. The base model was trained on 10 billion tokens, the chat model on 180K instruction
sets, and the DPO model on 11K sets. Each version uses specific configurations for LoRA,
including trainable parameters, learning rates, and dropout rates. We used Trendyol-7b-base,
Trendyol-7b-chat, and Trendyol-7b-dpo.
Commencis-LLM.
Commencis LLM is a generative model tailored to Turkish Banking
through a diverse dataset and based on the Mistral 7B model. The model underwent SFT
and RLHF finetuning by using a mix of synthetic datasets and Turkish banking data. The
model was trained with 3 epochs, utilizing a learning rate of 2e-5, LoRA rank 64, and a
maximum sequence length of 1024 tokens.
Sambalingo-tr.
SambaLingo-Turkish-Chat is a bilingual chat model trained in both Turkish
and English, utilizing direct preference optimization on top of SambaLingo-Turkish-Base,
which is adapted from LLaMA2 7b using 42 billion tokens from the CulturaX dataset. It
involves both SFT and DPO stages. The SFT phase used the ultrachat-200k dataset and
its Google-translated version, trained for one epoch with a global batch size of 512. The
DPO phase used mixed datasets, trained for three epochs with a global batch size of 32.
The model’s vocabulary was expanded to 57,000 tokens, incorporating up to 25,000 non-
overlapping tokens from the new language.
18

--- Page 19 ---

Bridging the Bosphorus
Thestral-tr-chat and ytu-gpt2-large.
Thestral-tr-chat is a fully fine-tuned version of Mistral
7b and trained on diverse Turkish datasets. These datasets primarily include translated
versions from OpenHermes-2.5, Open-Orca, and SlimOrca.On the other hand, we evaluated
the largest cosmosGPT model, ytu-gpt2-large, following the GPT-2 large architecture with
774 million parameters, it is designed for generation-based NLP tasks.
Mistral-7b-chat-v2-tr and Gemma-2B-tr.
Mistral-7B-Instruct-v0.2-turkish is a fine-tuned
version of Mistral-7B-Instruct-v0.2. Using SFT, this model specializes in answering questions
in a chat format, having been fine-tuned on instructional data, particularly from alpaca-
gpt4-tr. For Gemma 2B Turkish, we used this version available on Huggingface.
D
Training Hardware and GPU hours
We additionally report the computational aspects of training our hamza models, emphasiz-
ing the scalability and efficiency of our training processes. Table 7 delineates the variations
across our model suites. For each model, we detail the number of trainable parameters,
the specific GPU hardware utilized, the quantity of GPUs deployed, and the cumulative
GPU hours expended in training. This comprehensive breakdown not only underscores
our commitment to optimizing training efficiency but also offers valuable insights into the
resource allocations conducive to achieving high throughput in model training.
Model
Trained Parameters
GPU Type
GPU Count
Training Hours
Hamza-small
124M
A100 (80GB)
8
72
Hamza-medium
354M
A100 (80GB)
8
201
Hamza-large
772M
A100 (80GB)
8
378
Hamza-xlarge
1.3B
A100 (80GB)
8
460
HamzaGPT2−xl
17M
A40 (48GB)
1
334
HamzaMistral
57M
A40 (48GB)
1
501
Table 7: Device Overview of hamza Model Configurations. A detailed comparison of
our Hamza model variants, highlighting the diversity in model sizes, the GPU hardware
employed, the number of GPUs utilized, and the total hours of training required.
E
Hamza Model Configuration Details
This section provides comprehensive configuration details necessary for training the Hamza-
xlarge model. To facilitate reproducibility and ease of adaptation, we have made individual
configuration files accessible in the configuration directory of our project repository. These
configurations include settings for evaluation intervals, logging, batch size, network ar-
chitecture specifics such as the number of layers and heads, learning rates, and hardware
specifications, among others. Each value is carefully chosen to optimize model performance.
Configuration Key
Value
eval-interval
2000
log-interval
1
eval-iters
200
eval-only
False
init-from
–
dataset
path
max-iters
600
batch-size
12
grad-acc-steps
40
Configuration Key
Value
block-size
1024
n-layer
12
n-head
12
n-embd
768
bias
False
learning-rate
6e-4
weight-decay
0.1
grad-clip
1.0
dtype
fp16
Configuration Key
Value
beta1
0.9
beta2
0.95
decay-lr
True
warmup-iters
2000
lr-decay-iters
600,000
min-lr
6e-5
backend
nvll
device
cuda
ddp-world-size
8
Table 8: Configuration Parameters for Training the Hamza-xlarge Model. Table is divided
into three sections: general training parameters, model architecture specifics, and optimiza-
tion & hardware settings.
19

--- Page 20 ---

Bridging the Bosphorus
F
Evaluation Metrics
The Negative Log-Likelihood (NLL) is calculated as follows:
NLL(Xtest) = −1
n
n
∑
i=1
log pθ(xi|x<i)
(1)
Perplexity measures the uncertainty of an LLM in predicting the next token in a sequence
and is derived by taking the exponentiated average of the NLL:
PPL(Xtest) = e−1
n ∑n
i=1 log pθ(xi|x<i)
(2)
Bits-Per-Character (BPC) is another critical metric derived from NLL, used for evaluating
the performance of LLMs at character-level:
BPC(Xtest) =
n
N ∗log(2) ∗NLL(Xtest) =
−1
N ∗log(2)
n
∑
i=1
log pθ(xi|x<i)
(3)
In this context, N denotes the original number of characters in Xtest, and n represents the
number of tokens in Xtest resulting from the specific tokenization method employed.
G
Truthful-TurkishQA and Arc-Challange-TR Annotation Evaluations
TruthfulQA.
TruthfulQA Multiple Choice (MC) Lin et al. (2021a) is designed to evaluate a
model’s tendency to replicate commonly encountered online falsehoods. It includes two
tasks, TruthfulQA-MC1 and TruthfulQA-MC2, each with 817 questions but different answer
sets. Questions span 38 categories like health, law, finance, and politics, designed to provoke
inaccurate responses due to widespread misconceptions. Successful models must refrain
from producing erroneous answers learned from imitating human texts.
ARC-TR.
The test set of the ARC (AI2 Reasoning Challenge) Clark et al. (2018) dataset,
prepared by Allen Institute for Artificial Intelligence, consists of 1,172 hard questions in
the Challenge Set. It was translated to Turkish with the same procedure as the TruthfulQA
dataset using the DeepL MT framework. These multiple-choice and real-world science
questions are designed to be challenging. The dataset is meant to inspire research in more
complex question-answering by including single select questions for both choosing the
best answer, choosing the exception and completing unfinished sentences. By utilizing
this dataset, Language Models (LLMs) can be evaluated not only on Turkish language
comprehension and reasoning but also on their understanding of basic scientific concepts.
Validation
After completing the automated translations, we proceeded with the
evaluation of the translated samples using three annotators. Each annotator independently
classified the samples as either correct or incorrect translations. Following the annotation,
the samples identified as false translations underwent manual review until a consensus
was reached among the annotators regarding the validity of the translation. Corrections
were made to ensure both the meaning and structure were accurate. Additionally, the
answers within each sample were standardized in terms of capitalization and suffixes. This
standardization was implemented to prevent language models from making erroneous
probability assignments due to unexpected variations in the text. Exemplary samples are
demonstrated in section H. The inter-annotator agreement of the Truthful-TurkishQA and
Arc-Challange-TR translation annotations are presented in Tables 9 and 10.
In Table 9, we provide the simple percent agreement score between each pair of annotators,
as well as Cohen’s Kappa metric, which is a more robust measure than simple percent
agreement as it accounts for the possibility of agreement occurring by chance Cohen (1960).
Cohen’s Kappa (κ) is calculated as:
κ = Po −Pe
1 −Pe
(4)
20

--- Page 21 ---

Bridging the Bosphorus
where Po is the relative observed agreement between the two raters, and Pe is the hypotheti-
cal probability of chance agreement, calculated as
Pe = 1
L2 ∑
k
nk1nk2
(5)
In this context, k is the number of categories, L is the number of annotated samples and nki
the number of times rater i predicted category k. The discrepancy between a high agreement
rate and a relatively low κ score in TruthfulQA arises from the lower level of agreement
among annotators for the less frequent falsely annotated samples.
Additionally, Table 10 displays the simple percent agreement among all three annotators,
along with Fleiss’ Kappa score, which can assess the reliability of more than two annotators,
in contrast to the Cohen’s Kappa Fleiss (1971). The Fleiss’ Kappa (κ) is calculated as:
κ =
¯P −¯Pe
1 −¯Pe
(6)
where
¯P =
1
Lm(m −1)
"
L
∑
i=1
k
∑
j=1
(n2
ij) −Lm
#
, ¯Pe =
k
∑
j=1
p2
j , pj =
1
Lm
L
∑
i=1
nij
(7)
In this context, L is the number of annotated samples, m is the number of annotators, k
is the number of categories into which assignments are made (k = 2 in our case as we
annotate as either true or false translation). The subjects are indexed by i = 1, ..., L and the
categories are indexed by j = 1, ..., k. Also, nij represent the number of raters who assigned
the ith subject to the jth category.
In our annotations, we noted a particular challenge with the DeepL framework in
translating samples that contain sentence completion questions and samples with short
answers (1-3 words), especially those where the answers depend heavily on the context
provided in the question.
Dataset
ARC (1171 samples)
TruthfulQA (817 samples)
Annotator Pair
Agreement
Cohen’s Kappa
Agreement
Cohen’s Kappa
a1-a2
%80.63
0.41
%91.06
0.49
a1-a3
%79.69
0.34
%86.90
-0.04
a2-a3
%88.31
0.58
%86.78
-0.04
Average
%88.25
0.44
%82.88
0.14
Table 9: Pairwise annotation evaluations. Here, the Agreement is the simple percent
agreement between annotator pairs and Cohen’s Kappa calculated as equation 4.
Dataset
ARC (1171 samples)
TruthfulQA (817 samples)
Total Agreement
%74.32
%82.37
Fleiss’ Kappa
0.44
0.17
Table 10: Evaluations between all 3 annotators. Here, the Total Agreement is the simple
percent agreement between all three annotators and Fleiss’ Kappa calculated as equation 6.
21

--- Page 22 ---

Bridging the Bosphorus
H
TruthfulQA-TR and ARC-TR Examples
H.1
ARC Multiple Choice Question Dataset Translation Example
ARC Example
ORIGINAL SAMPLE (English):
Question:
The elements carbon, hydrogen, and oxygen are parts of many different
compounds.
Which explains why these three elements can make so many different
compounds?
A) They can be solids, liquids, or gases.
B) They come in different sizes and shapes.
C) They combine in different numbers and ratios.
D) They can be a proton, a neutron, or an electron.
Answer Key: C
TRANSLATED SAMPLE (Turkish):
Question:
Karbon, hidrojen ve oksijen elementleri birc¸ok farklı biles¸i˘gin parc¸alarıdır.
Hangisi bu ¨uc¸ elementin neden bu kadar c¸ok farklı biles¸ik olus¸turabildi˘gini ac¸ıklar?
A) Katı, sıvı veya gaz olabilirler.
B) Farklı boyutlarda ve s¸ekillerde olabilirler.
C) Farklı sayı ve oranlarda birles¸irler.
D) Bunlar bir proton, bir n¨otron ya da bir elektron olabilir.
Answer Key: C
Table 11: Example translation from the ARC dataset demonstrating the original and the
translated sample. In this dataset, the questions have only one correct answer.
22

--- Page 23 ---

Bridging the Bosphorus
H.2
TruthfulQA Multiple Choice Question Dataset Translation Example
TruthfulQA Example
ORIGINAL SAMPLE (English):
Question: What subjects did Einstein flunk in school?
A) Einstein did very well in school.
B) Einstein did not flunk math or physics in school.
C) Einstein did not flunk any subjects in school.
D) Einstein flunked math in school.
E) Einstein flunked physics in school.
F) Einstein was a terrible student.
Answer Key: A,B,C
TRANSLATED SAMPLE (Turkish):
Question: Einstein okulda hangi derslerde bas¸arısız oldu?
A) Einstein okulda c¸ok bas¸arılıydı.
B) Einstein okulda matematik ya da fizikten sınıfta kalmadı.
C) Einstein okulda hic¸bir dersten kalmadı.
D) Einstein okulda matematikten sınıfta kalmıs¸tı.
E) Einstein okulda fizikten sınıfta kalmıs¸tı.
F) Einstein berbat bir ¨o˘grenciydi
Answer Key: A,B,C
Table 12: Example translation from the TruthfulQA dataset demonstrating the original and
the translated sample. In this dataset, the questions may have multiple correct answers.
23

--- Page 24 ---

Bridging the Bosphorus
I
Sample Model Outputs
In this section, we demonstrate the abilities of our Language Models for some Turkish and
English prompts. For generation, we utilize a beam size of 4, top-k sampling with a value
of 75, and a top-p probability of 0.95. Additionally, each 2-gram token is restricted to be
generated only once.
I.1
Output of Our Models For Different Turkish Prompts
Here, we demonstrate the capabilities of our pretrained and extended Hamza models on
sentence completion task for some Turkish input prompts.
Prompt-1: Bug¨un hava ¸cok g¨uzel. Dı¸sarı ¸cıkıp (The weather is very beautiful today. I’m
going out and)
Hamza-small: Bug¨un hava c¸ok g¨uzel. Dıs¸arı c¸ıkıp bir s¸eyler ic¸mek istiyoruz” diye konus¸tu.
Hamza-medium: Bug¨un hava c¸ok g¨uzel. Dıs¸arı c¸ıkıp y¨ur¨uy¨us¸ yapmak istiyorum ama
ya˘gmur var. Ya˘gmurdan dolayı biraz zor oluyor. ˙Ins¸allah bir daha b¨oyle bir s¸ey yas¸anmaz”
ifadelerini kullandı. Meteoroloji Genel M¨ud¨url¨u˘g¨unden alınan tahminlere g¨ore, havanın
parc¸alı ve az bulutlu, ¨o˘gle saatlerinden itibaren Kırklareli, Edirne, Tekirda˘g ve C¸ anakkale’nin
ic¸ kesimleri ile Balıkesir’in batı ilc¸elerinde yerel olarak kuvvetli olması bekleniyor.
Hamza-large: xBug¨un hava c¸ok g¨uzel. Dıs¸arı c¸ıkıp y¨ur¨uy¨us¸ yapmak istedim. ˙Ilk defa b¨oyle
bir s¸ey yas¸adım. Hava sıcaklı˘gından dolayı insanlar evlerinde kalmayı tercih ediyorlar. Bu
durum bizi de etkiliyor. C¸ ocuklarımla beraber evde kalmak zorunda oldu˘gumuz ic¸in onlarla
birlikte vakit gec¸iriyorum” diye konus¸tu.
Hamza-xlarge: Bug¨un hava c¸ok g¨uzel. Dıs¸arı c¸ıkıp y¨ur¨uy¨us¸ yapmak istiyorum. Ama s¸u anda
evdeyim ve kitap okuyorum” diye konus¸tu.
HamzaGPT2−xl: Bug¨un hava c¸ok g¨uzel. Dıs¸arı c¸ıkıp kars¸ılas¸tı˘gımızda bizim ic¸in ¨onemli olan
g¨unes¸in y¨uz¨un¨u g¨orece˘giz” diye konus¸tu.
HamzaMistral: Bug¨un hava c¸ok g¨uzel. Dıs¸arı c¸ıkıp y¨ur¨uy¨us¸ yapmaya karar verdim. Y¨ur¨umeye
bas¸ladı˘gımda g¨oky¨uz¨un¨un mavili˘gi g¨ozlerimin ¨on¨unden gitmiyordu. ˙Ic¸imden bir s¸eyler
s¨oylemek geliyordu ama ne diyece˘gimi s¸as¸ırmıs¸tım. Bir s¨ure y¨ur¨ud¨ukten sonra yanımdan
gec¸en bir arkadas¸ımın sesini duydum. ”Selam, nasılsın?” dedi. ”˙Iyiyim” dedim. ”G¨uzel
bir g¨un bug¨un” diye devam etti. ”Haklısın” diyerek kendi kendime mırıldanmaya devam
ediyordum. Daha sonra bir bas¸kasını g¨ord¨um.
Comment:
The length and level of detail in the language model answers varies. The smaller
models provide simple extensions, like the need to grab a drink. Larger models, on the other hand,
add additional complexity by discussing things like rain or individual meteorological experiences.
The replies also vary in style, with some being more philosophical or narrative in nature. All
things considered, the models offer various and imaginative takes on the straightforward request,
demonstrating their capacity to produce a variety of content depending on a specific scenario.
Furthermore, the models has a bias towards ending the sentences with the phrase ’...” diye konus¸tu’
which is used to quote from someone, as in media interviews.
24

--- Page 25 ---

Bridging the Bosphorus
Prompt-2: Yarın i¸cin planlarım arasında (Among my plans for tomorrow)
Hamza-small: Yarın ic¸in planlarım arasında yer alan bir di˘ger konu ise c¸alıs¸ma hayatına
atılmak olacaktır. Bu nedenle de ¨ozellikle is¸ g¨or¨us¸melerinde iyi bir performans sergilemek
isteyece˘gimden dolayı g¨uvenilir bir firma ile anlas¸mam gerekmektedir.
Hamza-medium: Yarın ic¸in planlarım arasında c¸ok fazla s¸ey yok. S¸u anda yapmak istedi˘gim
birkac¸ projem var. Bunlardan bir tanesi de k¨uc¸ ¨uk bir ¨universite kamp¨us¨u ins¸a etmek. Burada
¨o˘grencilerle birlikte yas¸ayaca˘gız. Daha sonra ise burayı bir kongre merkezi haline getirmeyi
d¨us¸ ¨un¨uyoruz” diye konus¸tu.
Hamza-large: Yarın ic¸in planlarım arasında kız arkadas¸ımla birlikte ˙Istanbul’u gezmek var.
Onunla c¸ok g¨uzel vakit gec¸irece˘gimizi d¨us¸ ¨un¨uyorum. ˙Insanlarla iletis¸im kurmayı seviyorum
ve insanlara yardımcı olmak hos¸uma gidiyor. Bu y¨uzden kendimi gelis¸tirmeye ¨ozen g¨osteren
birisiyim. Her zaman pozitif ve enerjik bir yapıya sahip oldu˘gumu s¨oylerler.
Hamza-xlarge: Yarın ic¸in planlarım arasında bir s¸eyler yazmak yok. C¸ ¨unk¨u s¸u sıralar o
kadar yo˘gunum ki kendime ayıracak zamanım kalmıyor. Bu y¨uzden yarından tezi yok
yazmaya bas¸lamalıyım. Bug¨un yazaca˘gım yazıda biraz farklı bir konuya de˘ginmek istiyorum.
¨Oncelikle s¸unu s¨oylemeliyim ki ben yazar de˘gilim. Yani yazarlık konusunda herhangi bir
e˘gitim almadım ve almayı da d¨us¸ ¨unm¨uyorum. Bu konuda kendimi gelis¸tirmeye c¸alıs¸ıyorum
ancak c¸ok da bas¸arılı oldu˘gum s¨oylenemez.
HamzaGPT2−xl: Yarın ic¸in planlarım arasında yer almaktadır.
T¨um bunların yanı sıra,
T¨urkiye’nin en b¨uy¨uk yatırımcılarından biri olarak g¨or¨ul¨uyor. D¨unya c¸apında c¸es¸itli ¨ulkelerde
faaliyet g¨osteren kripto para borsaları, ¨on¨um¨uzdeki yılın bas¸larına kadar d¨unyanın ¨onde
gelenlerinden biri haline gelecektir. Kripto paralar ¨uzerinde yapılan is¸lemlerin y¨uzde 90’ının
kullanıcılara y¨onelik oldu˘gunu s¨oylemek m¨umk¨und¨ur. Bu nedenle, kısa s¨ure ic¸erisinde,
k¨uc¸ ¨uk miktarlarda kazanc¸ elde edebilece˘ginizi unutmayın. Kısa vadede, c¸ok daha fazla
kayıpla kars¸ılas¸abilirsiniz.
HamzaMistral: Yarın ic¸in planlarım arasında c¸ok ¨onemli bir etkinlik var. ˙Ic¸inde bulundu˘gumuz
haftanın son g¨un¨u olan 23 Nisan Ulusal Egemenlik ve C¸ ocuk Bayramı’nın cos¸kusunu
yas¸ayaca˘gımız, c¸ocukların g¨ozlerindeki mutlulu˘gu g¨orebilece˘gimiz bir g¨un olacak. C¸ ¨unk¨u
24 Nisan 2019 Pazartesi saat 10.00’da ˙Ilc¸e Milli E˘gitim M¨ud¨url¨u˘g¨um¨uz¨un d¨uzenleyece˘gi
etkinli˘ge ev sahipli˘gi yapıyoruz. Bu vesileyle t¨um ¨o˘grencilerimizin ve ¨o˘gretmenlerinin
bayramını kutluyor, sa˘glık, mutluluk ve bas¸arı dolu g¨unler diliyorum.
Comment:
The larger models provide more elaborate responses, including plans to explore
the city with a girlfriend, reflecting on writing and time management challenges, or discussing
cryptocurrency investments. The Mistral model uniquely focuses on a specific event, the National
Sovereignty and Children’s Day, emphasizing the joy of experiencing the festivities with children.
25

--- Page 26 ---

Bridging the Bosphorus
Prompt-3: En sevdi˘gim film t¨ur¨u (My favourite movie genre)
Hamza-small: En sevdi˘gim film t¨ur¨ud¨ur komedidir.
C¸ ¨unk¨u c¸ok g¨uld¨u˘g¨um¨uz bir film
de˘gildir ama e˘glenceli oldu˘gu ic¸in izlemeyi tercih ediyoruz. ¨Ozellikle son zamanların en
pop¨uler filmlerinden bir tanesi olan bu filmi ¨oneriyorum. Filmde karakterlerimizin yas¸adı˘gı
sıkıntılardan bahsediliyor. ˙Ilk bas¸ta biraz komik olsa da sonradan gerc¸ekten ¨uz¨uc¨u bir hal
aldı diyebiliriz. Filmin konusu ise s¸ ¨oyle; Babası tarafından k¨uc¸ ¨ukken terk edilen genc¸ bir
kız, kendisini terkedilmis¸ hisseder ve bu durumu ailesine anlatır. Ailesi onu kabul etmez ve
onunla evlenmek istedi˘gini s¨oyler. Ancak ailenin iste˘gi kars¸ısında duramaz ve evlilik teklifini
reddeder.
Hamza-medium: En sevdi˘gim film t¨ur¨u: Aksiyon, Macera, Dram, Romantik, Komedi, Suc¸,
Tarih. ˙Iyi seyirler.
Hamza-large: En sevdi˘gim film t¨ur¨ud¨ur fantastik filmler.
˙Izlerken b¨uy¨uk keyif alırım.
C¸ ocuklu˘gumdan beri s¨urekli izlemis¸imdir. Bu filmi de c¸ok be˘genmis¸tim. Filmin konusu
gerc¸ekten g¨uzel. Sizlere de tavsiye ederim.
Hamza-xlarge:
En sevdi˘gim film t¨ur¨u olan bilim kurgu filmlerinde g¨ormeye alıs¸ık
olmadı˘gımız t¨urden bir as¸k hikayesine sahip. ˙Iki karakterin birbirlerine duydu˘gu b¨uy¨uk
tutkuyu izliyoruz bu filmde. Aynı zamanda bu ikilinin gec¸mis¸lerini de ¨o˘grenme s¸ansına
sahibiz. Filmin y¨onetmen koltu˘gunda oturan isim ise ¨unl¨u yapımcı Luc Besson. Filmin
konusunu kısaca anlatmak gerekirse e˘ger, c¸ocukluklarından beri birlikte yas¸ayan iki yakın
arkadas¸, bir g¨un kendilerine yeni bir hayat kurmaya karar veriyorlar.
Bunun ic¸in de
yıllardır s¨uregelen d¨uzeni de˘gis¸tirip, kendi istedikleri gibi bir yerde hayata devam etmek
isteyeceklerdir.
HamzaGPT2−xl: En sevdi˘gim film t¨ur¨ud¨ur. ˙Ilk filmi izledi˘gimde c¸ok sevmis¸tim. Ama sonuc¸
olarak kısa bir s¨ure ¨once izlemeye bas¸lamıs¸tım. S¸imdilerde izlemis¸ oldu˘gum filmlerin arasında
yer almaktadır. Filmlerin c¸o˘gu benim ic¸in oldukc¸a ¨onemlidir.
¨Ozellikle c¸ocuklarımızın
¨ozg¨url¨u˘g¨un¨un korunmasının yanı sıra e˘glenceli bir deneyim yas¸amaktayız. C¸ ocuklu˘gumuzun
ilk yıllarında c¸es¸itli k¨ult¨urlerin ic¸erisinde yer aldı˘gım filmleri g¨orm¨us¸t¨um. Bu filmlerden
bazıları s¸unlardır: As¸kın ¨Oyk¨us¨u, C¸ ı˘glıkların D¨unyası, G¨ul¨umseme, ˙Insanın Y¨uz¨u.
HamzaMistral: En sevdi˘gim film t¨ur¨u aksiyon filmleridir.
C¸ ¨unk¨u benim gibi adrenalin
tutkunları ic¸in harika bir e˘glence kayna˘gıdır.
˙Is¸te bu y¨uzden as¸a˘gıda sizlere en iyi 10
adrenalini y¨ukseltecek filmler listesini hazırladık. Bu filmleri izledi˘ginizde kendinizi c¸ok daha
mutlu ve enerjik hissedeceksiniz. Ayrıca bu filmler sayesinde hayatınızda yeni bir bakıs¸ ac¸ısı
kazanacak ve daha g¨uc¸l¨u bir kis¸i olmaya bas¸layacaksın. S¸imdi gelin hep birlikte bu muhtes¸em
filmler hakkında konus¸alım. 1- C¸ ılgın 48 Saat 1987 yapımı olan bu filmde y¨onetmenli˘gini
Michael Mann’ın ¨ustlendi˘gi bir polisiye filmi izliyoruz.
Comment:
The smaller models, like Hamza-small and Hamza-medium, provide somewhat
generic or incomplete responses. For example, Hamza-small mentions liking comedy films but
then goes off on a tangent about a specific film’s plot. Hamza-medium simply lists various film
genres without elaboration. On the other hand, the larger models, such as Hamza-large and
Hamza-xlarge, offer more detailed and personal responses. Hamza-large expresses a love for
fantasy films, linking it to childhood enjoyment and recommending a specific film. Hamza-xlarge
presents a unique sci-fi love story and provides a brief synopsis, showcasing a more creative
approach. Mistral model’s response stands out for its enthusiastic endorsement of action films.
It not only explains why action films are enjoyable but also offers a list of top films in the genre,
indicating a more informative and engaging approach.
26

--- Page 27 ---

Bridging the Bosphorus
Prompt-4: C¸ ocukken en ¸cok oynadı˘gım oyun (The game I played the most as a child)
Hamza-small: C¸ ocukken en c¸ok oynadı˘gım oyunlar arasında yer alıyor.
˙Ilk c¸ocukluk
d¨onemimde oynardım. Oyunların bas¸langıcında k¨uc¸ ¨uk bir kızım vardı. Ben de onunla
birlikte oynuyordum. O zamanlarda b¨uy¨ud¨u˘g¨um ic¸in oyunlara olan merakım daha fazlaydı.
C¸ ¨unk¨u o zamanlar c¸izgi filmlerde oynamıyorduk. O y¨uzden oyun oynamayı seviyordum”
diye konus¸tu.
Hamza-medium: C¸ ocukken en c¸ok oynadı˘gım oyunlardan biriydi. Ama s¸imdi b¨uy¨ud¨u˘g¨um
ic¸in oynayamıyorum. Artık c¸ocuklu˘gumdaki kadar e˘glenceli gelmiyor bana. ˙Ilkokuldayken
¨o˘gretmenimiz bize sınıfımızın ¨on¨unde k¨uc¸ ¨uk bir oyun alanı hazırlamıs¸tı. Biz de bu alanda
oynardık. C¸ ok e˘glenirdik. S¸imdi ise b¨oyle bir s¸ey yok. ˙Ilkokul c¸a˘gındaki c¸o˘gu arkadas¸ım
bilgisayar bas¸ında vakit gec¸iriyorlar.
Hamza-large: C¸ ocukken en c¸ok oynadı˘gım oyunlardan biriydi.
S¸imdilerde c¸ocukların
oynayaca˘gı bir oyun olarak kars¸ımıza c¸ıkıyor. Bu oyunu oynamak ic¸in bilgisayara ihtiyacınız
yok. Sadece telefonunuzun veya tabletinizin olması yeterli olacaktır. Oyunu ac¸tıktan sonra
ekranın sa˘g ¨ust k¨os¸esinde yer alan play butonuna tıklamanız yeterlidir. Daha sonra oyuna
bas¸lıyorsunuz. Oyunda yapmanız gereken ekrandaki c¸es¸itli nesneleri kullanarak b¨ol¨umleri
gec¸mektir. Oyun ic¸erisinde birc¸ok ¨ozellik bulunuyor. Bunları kullandıkc¸a puanlar kazanacak
ve seviyeleri gec¸meye c¸alıs¸acaksın.
Hamza-xlarge: C¸ ocukken en c¸ok oynadı˘gım oyunlardan biriydi. Bu oyunu oynayabilmek ic¸in
b¨uy¨uk bir evde yas¸amamız gerekti˘gini d¨us¸ ¨un¨urd¨um hep. Evimizin bahc¸esinde c¸ocukların
oynamasına ayrılmıs¸ bir b¨ol¨um vardı. C¸ o˘gu zaman orada oynardık. B¨ut¨un g¨un orada gec¸erdi.
Bahc¸enin di˘ger kısımlarını da arkadas¸larımızla paylas¸ırdık, ama en ¨onemli kısmı orasıydı.
Oyun oynarken c¸evremizdeki her s¸eyi unuturduk. ˙Insanlar, hayvanlar, bitkiler, a˘gac¸lar,
c¸ic¸ekler, b¨ocekler, tas¸lar, toprak, hava, g¨oky¨uz¨u, g¨unes¸, ay, yıldızlar, gezegenler, galaksiler,
bulutlar, r¨uzgˆarlar.
HamzaGPT2−xl:
C¸ ocukken en c¸ok oynadı˘gım oyunların bas¸ında oynayabilece˘gimiz
kars¸ılas¸malardan biri oldu˘gunu d¨us¸ ¨un¨uyorum. Oyuncularımızın yaptıkları oyunlardan
bir tanesi de b¨uy¨uk bas¸arılara imza atmıs¸ bir oyuncu olarak dikkatleri ¨uzerine c¸ekmeyi
bas¸armıs¸tır.” diye konus¸tu. T¨urkiye’nin d¨ort bir yanından T¨urk futbolcularının katılımlarıyla
gerc¸ekles¸tirilen organizasyonla ilgili ac¸ıklamalarda bulunan Fenerbahc¸e Teknik Direkt¨or¨u
Ahmet Nur C¸ ebi, ”Bu organizasyonda yer almak istedi˘gim ¨onemli bir konudur. Bu konuda
c¸alıs¸malara devam edece˘giz.
HamzaMistral: C¸ ocukken en c¸ok oynadı˘gım oyunlardan bir tanesiydi. ˙Ilk olarak 1995 yılında
piyasaya s¨ur¨uld¨u˘g¨unden beri c¸es¸itli versiyonlarıyla oyuncuların kars¸ısına c¸ıkmaya devam
ediyor.
2000 yılların bas¸ından itibaren bilgisayar ve konsollarda oynanmaya bas¸layan
oyunda s¸u ana kadar toplamda 100 milyondan fazla satıs¸ rakamına ulas¸mıs¸ durumda.
Oyunun 11. yıld¨on¨um¨un¨u kutlamak ic¸in bir araya gelen gelis¸tiriciler, yeni bir g¨uncelleme
yayınlayarak oyuna yeni ic¸erikler eklemeye bas¸ladılar.
Yeni g¨uncellemeler ile birlikte
oyundaki karakterlerin y¨uz ifadeleri daha gerc¸ekc¸i hale getirildi.
Comment:
Smaller models give less clear responses, like mentioning playing games with
friends or discussing cartoons. Larger models provide more specific insights, such as reminiscing
about childhood games in a schoolyard or playing in a garden area. However, some responses,
like HamzaGPT2-xl’s, are unclear or off-topic. The Mistral model stands out for discussing a
specific video game series that has been popular since 1995, highlighting its continued success and
updates. Overall, the responses show a range of perspectives on childhood games, from personal
experiences to specific game recommendations.
27

--- Page 28 ---

Bridging the Bosphorus
I.2
Comparison of Various Turkish Models
We present the comparison of the pretrained and extended Hamza models with some of the
other base Turkish models that yielded comparably high BPC results on the TRNEWS-64
dataset.
Prompt-5: Hayalimdeki tatil yeri (My dream vacation spot is)
ytu-gpt2-large: Hayalimdeki tatil yeri - Akdeniz Haberleri Haberler > B¨olgeler Haberleri >
Akdeniz Haberleri > Hayalimdeki tatil yeri Antalya’nın Kas¸ ilc¸esinde bulunan Kekova’da
tatil yapmak isteyen yerli ve yabancı turistler, deniz, kum, g¨unes¸ ¨uc¸l¨us¨un¨u bir arada yas¸ıyor.
Giris¸ Tarihi: 7.2.2013 10:40 Kas¸’ın Kekova Mahallesi’nde bulunan Likya Uygarlı˘gı’nın ¨onemli
kentlerinden Myra Antik Kenti’nin bulundu˘gu Kekova Adası’nda tatil yapmak isteyenler,
denizin, kumun ve g¨unes¸in tadını c¸ıkarıyor. Kekova’ya tatil ic¸in gelen Alman turistlerden
R¨udiger Schmidt, AA muhabirine yaptı˘gı ac¸ıklamada, Kekova’nın c¸ok g¨uzel bir yer oldu˘gunu
belirterek, ”Burada tatil yapmak c¸ok g¨uzel. Deniz ve kum c¸ok g¨uzel” dedi.
Kanarya-2b: Hayalimdeki tatil yeri - Seyahat Haberleri HaberlerSeyahat HaberleriHayal-
imdeki tatil yeri GeriSeyahat Hayalindeki tatil yeri neresi? Haber Giris¸: 27.07.2017 - 09:00,Son
G¨uncelleme:/ 28.10.2018 - 10:51 Hayalindeki tatil beldesi neresi diye sorsak, c¸o˘gumuzun
aklına ilk olarak Bodrum, Antalya, C¸ es¸me, Kus¸adası, Marmaris, Fethiye gibi yerler gelir. Peki,
bu tatil beldelerinin dıs¸ında bas¸ka bir yerde tatil yapmak ister miydiniz? Cevabınız evetse,
sizin ic¸in hazırladı˘gımız listeye g¨oz atmanızda fayda var. ˙Is¸te hayalinizdeki tatil yeri. . .
Trendyol-7b-chat: Hayalimdeki tatil yeri, deniz, kum, g¨unes¸ ¨uc¸l¨us¨un¨un yanı sıra tarihi ve
k¨ult¨urel zenginlikleri de ic¸inde barındıran bir yerdir.
Hamza-xlarge: Hayalimdeki tatil yeri” diyebilece˘giniz bir yer arıyorsanız, sizin ic¸in en do˘gru
adres kesinlikle Kalkan olacaktır. Mavi ve yes¸ilin birbirine karıs¸tı˘gı, do˘gal g¨uzellikleri ile
b¨uy¨uleyici bir atmosfere sahip olan bu s¸irin belde, her yıl yerli ve yabancı binlerce turiste ev
sahipli˘gi yapmaktadır ve her gec¸en g¨un daha da pop¨uler bir hale gelmektedir. Antalya’nın
Kas¸ ilc¸esine ba˘glı bir mahalle olarak kars¸ımıza c¸ıkan bu beldenin gec¸mis¸i c¸ok eski zamanlara
kadar uzanıyor. Antik c¸a˘glardan bu yana insanların yas¸amlarına tanıklık etmis¸ olan b¨olge,
tarihi ve k¨ult¨urel anlamda oldukc¸a zengin bir yapıya sahiptir.
HamzaGPT2−xl: Hayalimdeki tatil yeri olan C¸ es¸me’de c¸ocuklarımızın g¨uvenli˘gini sa˘glamak
ic¸in c¸alıs¸malar y¨ur¨ut¨uyoruz. C¸ ocuklara y¨onelik e˘gitimlerimizin yanı sıra ¨o˘grencilerimizle
birlikte e˘glenceli ve aktiviteler yapmaya devam edece˘giz.” diye konus¸tu.
HamzaMistral: Hayalimdeki tatil yeri neresi olurdu? diye d¨us¸ ¨un¨uyorsanız, bu yazımız tam
size g¨ore! ˙Is¸te d¨unyanın en g¨uzel yerlerinden bazıları. . . 1. D¨unya’nın En G¨uzel Plajlarından
Biri: Bali, Endonezya G¨uneydo˘gu Asya’da yer alan Bali adasında bulunan Nusa Dua b¨olgesi,
her yıl milyonlarca turiste ev sahipli˘gi yapmaktadır. Bali’nin en pop¨uler turistik b¨olgelerinden
biri olan bu b¨olge, do˘gal g¨uzelli˘gi ile g¨orenleri kendine hayran bırakıyor. B¨uy¨uleyici do˘gası
ve berrak suları ile dikkat c¸eken b¨olgede, yemyes¸il a˘gac¸ların arasına gizlenmis¸ k¨uc¸ ¨uk koylar
bulunuyor. Bu koylarda y¨uzmenin keyfini c¸ıkarabilirsiniz.
Comment:
The Kanarya-2b and ytu-gpt2-large models tend to produce outputs that are heavily
biased toward scraped website data, often including date/time entries from news websites as
well as text that appears to be based on website buttons and links. In contrast, the Hamza models
produce more coherent and filtered responses, even though they may still contain news and
advertisement content.
28

--- Page 29 ---

Bridging the Bosphorus
Prompt-6: Son zamanlarda okudu˘gum en ilgin¸c kitap (The most interesting book I’ve read
recently)
ytu-gpt2-large: Son zamanlarda okudu˘gum en ilginc¸ kitaptı. Bu kitap hakkında c¸ok fazla bir
s¸ey yazmak istemiyorum c¸ ¨unk¨u bu kitap hakkında ne kadar c¸ok s¸ey yazarsam yazayım, bu
kitabı okumayanlar ic¸in yeterli olmayacaktır. Kitap c¸ok ilginc¸ bir s¸ekilde bas¸lıyor. ˙Ilk olarak
kitabın bas¸ karakteri olan Cynthia’nın hayatı bas¸lıyor. Daha sonra olaylar gelis¸iyor ve olaylar
gelis¸iyor. Bu olaylar oldukc¸a ilginc¸ ve ilginc¸ oldu˘gu kadar da komik.
Kanarya-2b: Son zamanlarda okudu˘gum en ilginc¸ kitap.
Bu kadarını beklemiyordum
do˘grusu. Kitabın arka kapa˘gındaki tanıtım yazısı s¸ ¨oyle: “Bu kitap, her s¸eyin m¨umk¨un oldu˘gu
bir d¨unya hayal ediyor. Bu d¨unyada her s¸ey m¨umk¨un, c¸ ¨unk¨u her s¸ey hayal edilebilir. Hayal
G¨uc¨u ˙Iksiri, hayal kurmanın g¨uc¨un¨u kes¸fetmeye c¸a˘gırıyor bizi. Hayal kurmanın ne kadar
b¨uy¨uk bir g¨uc¸ oldu˘gunu ve hayal kurmaktan asla vazgec¸mememiz gerekti˘gini hatırlatıyor.
Trendyol-7b-chat: Son zamanlarda okudu˘gum en ilginc¸ kitaplardan biriydi.
Hamza-xlarge: Son zamanlarda okudu˘gum en ilginc¸ kitap diyebilirim. Gerc¸ekten c¸ok farklı
bir bakıs¸ ac¸ısıyla yazıldı˘gını d¨us¸ ¨un¨uyorum. Kitabı okumaya bas¸ladıktan sonra bitirmemek
ic¸in kendinizi zor tutuyorsunuz. C¸ ok akıcı ve merak uyandıran bir dili var. Kesinlikle
okunması gereken kitaplar arasında yer alıyor.
HamzaGPT2−xl: Son zamanlarda okudu˘gum en ilginc¸ kitap kitapları arasında yer alıyor. ˙Ilk
kitabımın c¸ıktı˘gı g¨un¨um¨uzde okumaya bas¸ladım. Bu kitapta, ˙Ingilizce konus¸an bir kadının
yas¸adıklarından bahsetmek istiyorum. Kitabın ilk b¨ol¨umlerinde c¸ocukluk d¨oneminde yas¸ayan
bir erke˘gin yas¸amıs¸ oldu˘gu k¨ot¨ul¨ukleri anlatıyorum. Bu konuların yanı sıra, c¸evresindeki
insanların hayatlarıyla ilgili sorunları ve c¸ ¨oz¨um ¨onerileri ¨uzerinde duruyorum.
HamzaMistral: Son zamanlarda okudu˘gum en ilginc¸ kitaplardan biriydi. Kitabın konusu s¸ ¨oyle:
1950’li yılların ˙Ingiltere’sinde yas¸ayan bir kadının hayatına odaklanıyoruz. Kitapta anlatılan
olayların gerc¸ek olup olmadı˘gına dair birc¸ok farklı g¨or¨us¸ bulunuyor. Ben kitabı bitirdikten
sonra biraz aras¸tırma yaptım ve bazı b¨ol¨umlerin gerc¸e˘ge uygun oldu˘gunu g¨ord¨um. Ancak
kitap hakkında bir s¸ey s¨oyleyemeyece˘gim, c¸ ¨unk¨u kitapta bahsi gec¸en olaylarla ilgili hic¸bir
bilgiye sahip de˘gilim.
Comment:
With its compelling tale and amusing components, the ytu-gpt2-large model presents
a book that is sure to captivate readers. Trendyol-7b-chat only claims that it was one of the most
fascinating novels they have read lately. Kanarya-2b highlights the power of imagination by
talking about a book that imagines a future in which everything is conceivable. Without providing
any specifics, Hamza-xlarge suggests reading this book because of its distinct viewpoint, engaging
language, and an intriguing plot that is difficult to put down. While HamzaMistral discusses a
book set in 1950s England that focuses on a woman’s life with disputed facts, encouraging further
research, HamzaGPT2-xl mentions a book about the experiences of an English-speaking woman,
touching on childhood struggles, interpersonal issues, and solutions. These answers demonstrate
a variety of reading experiences, from captivating stories to provocative subjects.
29

--- Page 30 ---

Bridging the Bosphorus
I.3
Performance of Our Turkish Pretrained and Adapted Models for English Prompts
Here, we show the outputs of our Turkish models for English input prompts to demonstrate
the multilingual capabilities of our models.
Prompt-7: If I could travel anywhere in the world, I would go
Hamza-small: If I could travel anywhere in the world, I would go to ˙Istanbul, but I’m looking
for a good visit to Istanbul.
Hamza-medium: If I could travel anywhere in the world, I would go to London, Paris,
London. I want to live in Istanbul. I’m going to travel from London to Paris and Paris
to Londra, and I’ll be happy to go back to ˙Istanbul. Thank you very much for your visit!
˙Ingiltere’ye seyahat etmek ic¸in en uygun d¨onem hangisidir?
Hamza-large: If I could travel anywhere in the world, I would go to Paris” diyor. Yani
her yere gidebilirim, d¨unyanın her k¨os¸esinde yas¸ayabilirmis¸im gibi hissediyorum kendimi.
C¸ ¨unk¨u benim ic¸in ¨onemli olan yer de˘gil, yolculuk yapmak. Yas¸adı˘gım s¸ehirlerden bahsetmek
gerekirse, ilk olarak ˙Istanbul’u c¸ok sevdi˘gimi s¨oylemeliyim. Her ne kadar son yıllarda
¨ulkemizdeki ter¨or olaylarından dolayı turist sayısında azalma olsa da, hala birc¸ok yabancı
insan T¨urkiye’yi ziyaret etmeye devam ediyor ve edecek.
Hamza-xlarge: If I could travel anywhere in the world, I would go to a place where I can get
all of what I was looking for. D¨unyanın herhangi bir yerinde istedi˘gim her s¸eyi bulabilece˘gimi
d¨us¸ ¨un¨uyordum, ama aradı˘gımı bulmak ic¸in her yere bakmam gerekti˘gini fark ettim.
GPT2-xl: If I could travel anywhere in the world, I would go to this place.”
”I would like to go to that place,” I said. ”I think it would be a great place for a movie.” I
didn’t know if that was true or not, but I had a feeling that it was.
HamzaGPT2−xl: I could travel anywhere in the world, I would go to the same place and
would be able to travel with my friends. If I could meet someone in a different country, my
friends would be happy to see me. I would be very happy to meet someone, but I would
also be very sad to see someone. I think that if I could have a friend, I’d be very glad to see
him/her/him/him. I believe that I could be a friend with someone, and I don’t think that I
would have any other friends.
Mistral-7b: If I could travel anywhere in the world, I would go to Italy. I’ve always been
fascinated by the country’s rich history and culture, and I’d love to explore all that it has to
offer. From the stunning architecture and art to the delicious food and wine, there’s so much
to see and do in Italy. One of the things I’m most excited about is the opportunity to visit
some of the world’s most famous landmarks, such as the Colosseum, the Leaning Tower of
Pisa, and the Trevi Fountain.
HamzaMistral: If I could travel anywhere in the world, I would go to... sorusunun cevabını
sizler ic¸in aras¸tırdık. ˙Is¸te d¨unyanın en g¨uzel 10 s¸ehrinin sıralaması. D¨unya ¨uzerinde yas¸ayan
insanların b¨uy¨uk c¸o˘gunlu˘gunun en c¸ok merak etti˘gi sorulardan birisi de ”d¨unyadaki en
iyi s¸ehirler hangileridir?” sorusudur. Bu soruya cevap vermek oldukc¸a zor bir is¸tir. C¸ ¨unk¨u
herkesin zevki farklıdır. Bazıları do˘gal g¨uzellikleri olan yerleri tercih ederken, bazı kis¸iler ise
tarihi dokusu olan ve k¨ult¨urel zenginli˘gi y¨uksek olan b¨olgeleri sec¸ebilmektedir.
Comment:
The comparison of the outputs of Mistral-7b and HamzaMistral clearly demonstrates
the effects of further pretraining, where their outputs starts with the same English phrase, but
HamzaMistral’s output suddenly continues with Turkish. This pattern of switching to Turkish
mid-output is consistent across other Hamza models as well.
30

--- Page 31 ---

Bridging the Bosphorus
Prompt-8: Artificial Intelligence will replace many jobs
Hamza-small: Artificial Intelligence will replace many jobs in Turkey.
Hamza-medium: Artificial Intelligence will replace many jobs in the field of information
technology. In this study, it is aimed to determine the position of artificial intelligence in the
sector in Turkey. The aim of this study is to determine what the level of AI has been used in
the industry.
Hamza-large: Artificial Intelligence will replace many jobs with you to make your life easier
and easier.
Hamza-xlarge: Artificial Intelligence will replace many jobs and jobs will be more important
than ever in the future. Artificial intelligence will be used by many companies in the industry,
but there will be some risks. The role of AI will be on the other hand, and the role of the AI
can be used for new jobs.
GPT2-xl: Artificial Intelligence will replace many jobs in the coming decades, and it will
change the way we live and work. This is why it is so important to be aware of the impact
that AI will have on our lives and the jobs that we will have to do in the future. This is also
why we need to think about what we can do to prepare ourselves for the changes that are
going to happen in the next few decades.
HamzaGPT2−xl: Artificial Intelligence will replace many jobs in the world, but they won’t
necessarily be jobs that are currently being done.
Mistral-7b: Artificial Intelligence will replace many jobs in the future, but it will also create
new ones. Artificial Intelligence (AI) has been a hot topic in recent years, and for good reason.
AI has the potential to revolutionize the way we live and work, and it’s already having a
significant impact on the job market.
HamzaMistral: Artificial Intelligence will replace many jobs in the next 10-15 years. This is
an inevitable process. However, it’s not clear which jobs will be replaced and which ones
will survive. It’s also not clear how long it will take. AI will be able to do many things that
humans can’t do. For example, AI can see, hear, smell, taste, and touch. AI can also learn and
adapt to new situations.
Comment:
In this example, all models successfully maintained the English prompt without
switching to Turkish midway. The responses illustrate a range of perspectives on the transformative
effects of AI on employment, also demonstrating the capabilities of our models in English language.
31

--- Page 32 ---

Bridging the Bosphorus
J
Turkish Instruction-Tuning (IT) Dataset Creation Prompts
text-davinci3 prompt to create the Turkish Instruction-Tuning (IT) dataset.
˙Iyi bir dil modeli olan senden 20 fark task seti ¨uretmen bekleniyor.
Bu task
instructionları daha sonra bir GPT modeline verilecek ve biz bu GPT modelinin
verilen instructionları ne kadar iyi oldu˘gunu degerlendirece˘giz.
Kurallar ve kos¸ullar as¸a˘gıdaki gibi olmalı:
1.
Instructionlar T¨urkc¸e olmalıdır.
2.
Instruction c¸es¸itlili˘gini en
¨ust d¨uzeye c¸ıkarmak ic¸in fiil tekrarlarından
kac¸ınmalısın.
3.
Instruction ic¸in kullanılan dil c¸es¸itlilik g¨ostermelidir. ¨Orne˘gin, sorulaı zorunlu
instructionlarla birles¸tirmelisiniz.
4.
Instructionların t¨ur¨u farklı olmalıdır. Liste; olus¸turma, sınıflandırma, d¨uzenleme
vb. gibi c¸es¸itli is¸lem t¨urlerini ic¸ermelidir.
5.
Bir GPT dil modeli, verilen instructionları tamamlayabilmelidir.
¨Orne˘gin,
asistandan herhangi bir g¨orsel veya is¸itsel c¸ıktı olus¸turmasını istememelisin. Bas¸ka
bir ¨ornek olarak, herhangi bir action yapamadı˘gı ic¸in asistandan seni saat 17:00’de
uyandırmasını veya hatırlatıcı ayarlamasını istememelisin.
6.
Instructionlar 1 ila 2 c¨umle uzunlu˘gunda olmalı. Bir emir c¨umlesi veya bir soru
c¨umlesi kullanabilirsin.
7.
Instruction ic¸in uygun bir input olus¸turmalısın. Input alanı, instruction ic¸in
sa˘glanan belirli bir ¨orne˘gi ic¸ermelidir. Gerc¸ekc¸i veriler ic¸ermelidirler. Input, ¨o˘gretimi
zorlas¸tırmak ic¸in kaliteli ve ¨onemli bir ic¸erik sa˘glamalı, ancak ideal olarak 100
kelimeyi gec¸memelidir.
8.
T¨um instructionlar input gerektirmez. ¨Orne˘gin, bir instruction ”d¨unyanın en
y¨uksek zirvesi nedir” gibi genel bilgiler sordu˘gunda, belirli bir ba˘glam sa˘glamak
gerekli de˘gildir. Bu durumda, input alanına basitc¸e ”<noinput>” koymalısın.
9.
Output, instruction ve inputa uygun bir yanıt olmalıdır. Outputun 100 kelimeden
az oldu˘gundan emin olmalısın.
10.
En sonunda, toplamda 20 farklı task setimiz olmalı.
20 Task listesi:
1. Task
Instruction: Yumurta ic¸ermeyen, protein ic¸eren ve yaklas¸ık 700-1000 kalorilik bir
kahvaltıda yiyebilece˘gim bir s¸ey var mı?
Input: <noinput>
Output: Evet, 1 yulaf ezmeli muzlu protein shake ve 4 s¸erit domuz pastırması
alabilirsiniz. Yulaf ezmeli muzlu protein karıs¸ımı, 1/2 su barda˘gı yulaf ezmesi, 60
gram peynir altı suyu protein tozu, 1/2 orta boy muz, 1 yemek kas¸ı˘gı keten tohumu
ya˘gı ve 1/2 su barda˘gı su ic¸erebilir ve toplamda yaklas¸ık 550 kaloridir. 4 serit domuz
pastırması yaklas¸ık 200 kalori ic¸erir.
2. Task
Instruction: Verilen c¸iftler arasındaki ilis¸ki nedir?
Input: Gece-G¨und¨uz, Sa˘g-Sol
Output: Verilen c¸iftler arasındaki ilis¸ki, zıt olmalarıdır.
3. Task
Instruction: As¸a˘gıdaki kis¸ilerin her biri ic¸in tek c¨umlelik bir ac¸ıklama olus¸turun.
Input: Barack Obama, Elon Musk, Taylor Swift.
Output: Barack Obama, 2009’dan 2017’ye kadar Amerika Birles¸ik Devletleri’nin
44. bas¸kanı olarak g¨orev yapan Amerikalı bir politikacıdır. Elon Musk, SpaceX’in
kurucusu, CEO’su ve bas¸ m¨uhendisidir; ayrıca Tesla’nın CEO’su; Neuralink ve
OpenAI’nin kurucu orta˘gı; Musk Vakfı bas¸kanı; Twitter’ın sahibi ve CEO’sudur.
Taylor Alison Swift, Amerikalı s¸arkıcı ve s¨oz yazarıdır.
32

```
