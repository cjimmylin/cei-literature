---
title: "Nemotron H Accurate Efficient Models"
source_pdf: "AI Labs/NVIDIA/Nemotron-4/Nemotron-H-Accurate-Efficient-Models.pdf"
company: "NVIDIA"
pages: 35
extracted_at: "2026-01-31T20:18:20.078874"
type: "ai_lab_paper"
---

# Nemotron H Accurate Efficient Models

**Company/Lab:** NVIDIA
**Model:** Nemotron-4
**Source PDF:** AI Labs/NVIDIA/Nemotron-4/Nemotron-H-Accurate-Efficient-Models.pdf
**Total Pages:** 35

---

## Content

```
--- Page 1 ---

2025-9-9
Nemotron-H: A Family of Accurate and Efficient
Hybrid Mamba-Transformer Models
NVIDIA
Abstract. As inference-time scaling becomes critical for enhanced reasoning capabilities, it is
increasingly becoming important to build models that are efficient to infer. We introduce Nemotron-
H, a family of 8B and 56B/47B hybrid Mamba-Transformer models designed to reduce inference cost
for a given accuracy level. To achieve this goal, we replace the majority of self-attention layers in the
common Transformer model architecture with Mamba layers that perform constant computation and
require constant memory per generated token. We show that Nemotron-H models offer either better
or on-par accuracy compared to other similarly-sized state-of-the-art open-sourced Transformer
models (e.g., Qwen-2.5-7B/72B and Llama-3.1-8B/70B), while being up to 3× faster at inference.
To further increase inference speed and reduce the memory required at inference time, we created
Nemotron-H-47B-Base from the 56B model using a new compression via pruning and distillation
technique called MiniPuzzle. Nemotron-H-47B-Base achieves similar accuracy to the 56B model,
but is 20% faster to infer. In addition, we introduce an FP8-based training recipe and show that it
can achieve on par results with BF16-based training. This recipe is used to train the 56B model.
We are releasing Nemotron-H base model checkpoints with support in Hugging Face and NeMo.
1. Introduction
Attention (Vaswani et al., 2023) traditionally has been the powerhouse of large language models
(LLMs). Yet, to generate one token during auto-regressive inference, the self-attention layer must
perform computation that scales linearly with the number of tokens seen so far since it models
interactions between all pairs of tokens in a sequence (potentially in a causal way); as a result, self-
attention layers also have to store state in a KV cache during inference that is linearly proportional to
the number of tokens in the sequence (Kwon et al., 2023). Recent reasoning LLMs, however, exhibit
inference-time scaling, where generating more tokens at inference time can improve the quality of
model responses (OpenAI, 2025; DeepSeek-AI, 2025b). Thus, attention layers can fundamentally
limit overall model intelligence.
To address this issue, much recent work has proposed alternative architectures (Katharopoulos et al.,
2020; Beltagy et al., 2020; Gu & Dao, 2024; Dao & Gu, 2024). One such example is a series of
hybrid models that replace the majority of the self-attention layers in the standard Transformer
architecture with more efficient layers (e.g., Mamba, Mamba-2, or sliding-window attention layers)
that have sub-linear or even constant compute and memory requirements. Recent work has shown
hybrid models to be competitive with more traditional Transformer architectures (Waleffe et al.,
2024; Lieber et al., 2024; DeepMind, 2025).
Motivated by improving inference efficiency, we introduce the Nemotron-H family of hybrid Mamba-
Transformer models. The Nemotron-H models consist of a mixture of Mamba-2, self-attention and
MLP layers, and achieve state-of-the-art accuracy and improved inference speed when compared
to open-sourced Transformer models of similar size (Figure 1). The Nemotron-H family has a
series of 8-billion-parameter models (Nemotron-H-8B-Base, Nemotron-H-8B-Instruct, Nemotron-
H-8B-VLM), and a series of 47/56-billion-parameter models (Nemotron-H-47B-Base, Nemotron-
H-56B-Base, Nemotron-H-56B-VLM) that offer either better or on-par accuracy compared to
© 2025 NVIDIA. All rights reserved.
arXiv:2504.03624v4  [cs.CL]  5 Sep 2025

--- Page 2 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
0
5
10
15
20
25
30
35
40
Throughput (Output tokens/s/GPU)
50.0
52.5
55.0
57.5
60.0
62.5
MMLU-Pro accuracy (%)
2.4x
1.2x
Nemotron-H-56B
Nemotron-H-47B
Llama-3.1-70B
Llama-3.1-405B
Qwen-2.5-72B
Input sequence length = 65536  / Output sequence length = 1024
Figure 1 | MMLU-Pro accuracy (Wang et al., 2024a) versus per-GPU inference throughput for
Nemotron-H-56B/47B-Base compared to existing similarly-sized Transformer models. Nemotron-H
models provide state-of-the-art accuracy and inference time speedups.
Qwen-2.5-7B/Llama-3.1-8B and Qwen-2.5-72B/Llama-3.1-70B, respectively. For example, Nemotron-
H-56B-Base outperforms Llama-3.1-70B on 16 out of 17 tasks that we evaluated (§2.5). With larger
sequences (65536 input sequence length, 1024 output tokens), we measure up to 3× higher inference
throughput on NVIDIA H100 GPUs.
To achieve the above results, we pre-train Nemotron-H models on up to 20 trillion tokens of
high-quality curated and synthetically-generated data (Su et al., 2024; Akter et al., 2024). Nemotron-
H-56B-Base is the first Nemotron model to be fully pre-trained using a FP8-based recipe. Our recipe,
called per-tensor current scaling, is coarse grained and involves quantizing entire tensors using a
single scaling factor. This factor is chosen to preserve the largest value in the given tensor; any value
too small to fit in the desired FP8 format is flushed to zero. In addition, we find it important for
training stability and convergence to leave the first and last 4 GEMMs of the model in BF16. In
smaller ablations with 8B-parameter models on token horizons up to 15 trillion tokens, we show that
FP8 per-tensor scaling can reach equal or better downstream task accuracy compared to BF16.
To efficiently tailor Nemotron-H models for different deployment scenarios, we introduce a new
compression via pruning and distillation paradigm, called MiniPuzzle, that combines the simplicity
of Minitron (Sreenivas et al., 2024) and the versatility of Puzzle (Bercovich et al., 2024). MiniPuzzle
can be used to turn a larger model into a smaller model satisfying specific memory, parameter count,
or latency constraints. We use MiniPuzzle to distill Nemotron-H-56B-Base to Nemotron-H-47B-Base,
using only 63 billion training tokens and FP8 training. Nemotron-H-47B-Base can be deployed in
FP4 precision on a single NVIDIA RTX 5090 GPU with 32GiB of memory (Nemotron-H-56B-Base’s
model weights would require roughly 29.5GiB alone, limiting maximum context size).
The Nemotron-H base models can also be effectively post-trained to produce models with high
accuracies on vision-language, instruction following, and long-context (e.g., RULER) benchmarks.
Vision-Language Models (VLMs) based on both Nemotron-H-8B and Nemotron-H-56B have already
been used to develop very strong reasoning models for physical AI as part of the Cosmos-Reason1
project (NVIDIA et al., 2025).
Overall, the Nemotron-H family of models demonstrates that hybrid models can be state-of-the-art in
terms of capabilities while offering improved inference speed. Moreover, we believe FP8 pre-training
and compression techniques like MiniPuzzle make it cheaper and more efficient to create such models.
2

--- Page 3 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
Mamba-2
FFN
Attention
Mamba-2
FFN
Mamba-2
FFN
Mamba-2
FFN
Mamba-2
FFN
Mamba-2
FFN
Mamba-2
FFN
Mamba-2
FFN
Attention
Mamba-2
FFN
Mamba-2
FFN
Mamba-2
FFN
Mamba-2
FFN
Mamba-2
FFN
Mamba-2
FFN
Nemotron-H-56B
Nemotron-H-8B
x3
x3
x4
x1
x10
x1
Figure 2 | Nemotron-H-8B/56B model architectures. Roughly 8% of the total layers in the model
are self-attention layers; these layers are evenly dispersed throughout the model. The rest of the
model is made up of alternating Mamba-2 and FFN layers.
To enable further research, we have released the following base model checkpoints in Hugging Face
and NeMo formats on the Hugging Face and NGC model repositories:
• Nemotron-H-56B-Base. Hugging Face and NGC.
• Nemotron-H-47B-Base. Hugging Face and NGC.
• Nemotron-H-8B-Base. Hugging Face and NGC.
The rest of this technical report is organized as follows:
• In §2, we discuss the Nemotron-H model architecture and the pre-training process (including
details on the pre-training dataset and FP8 recipe used).
• In §3, we describe the pruning and distillation methods used for model compression.
• In §4, we introduce the vision-language models based on the Nemotron-H models.
• In §5, we show that Nemotron-H models can be extended to create competitive instruct and
long-context versions.
2. Base Models and Pre-Training
In this section, we discuss the Nemotron-H-8B-Base and Nemotron-H-56B-Base model architectures,
as well as key details in the pre-training process used to produce these models. We also compare
Nemotron-H-8B/56B-Base with existing open-source state-of-the-art Transformer models on both
accuracy (on common benchmark tasks used for base models) and inference speed.
2.1. Model Architecture
Nemotron-H models consist of a mixture of Mamba-2 (Dao & Gu, 2024), self-attention, and FFN
layers as summarized in Figure 2 and Table 1. As suggested by prior work (Waleffe et al., 2024),
3

--- Page 4 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
Model
Number of
layers
Model
dimension
FFN
dimension
Q
heads
KV
heads
State
dimension
Mamba
groups
Nemotron-H-8B
52
4096
21504
32
8
128
8
Nemotron-H-56B
118
8192
32768
64
8
256
8
Table 1 | Summary of the Nemotron-H hybrid Mamba-Transformer architectures.
we set the number of attention layers to be roughly 8% of the total number of layers and evenly
disperse them throughout the model. This amounts to 4 self-attention layers (out of 52 layers) for
Nemotron-H-8B and 10 for Nemotron-H-56B (out of 118 layers). The rest of the layers consist of an
even split between FFN and Mamba-2 layers. We also ensure that a) the first layer in the model is a
Mamba-2 layer, b) the last layer in the model is a FFN layer, and c) self-attention layers always
precede FFN layers (as they do in a standard Transformer block like in Vaswani et al. (2023)).
We use a hidden dimension of 4096 for Nemotron-H-8B and 8192 for Nemotron-H-56B. For our
smaller model, we use FFN hidden dimension of 21504, 32 attention query heads, and Mamba-2 state
dimension of 128; for the larger model, we use FFN hidden dimension of 32768, 64 attention query
heads, and Mamba-2 state dimension of 256. Both models use Grouped-Query Attention (Ainslie
et al., 2023) with 8 key-value heads, 8 Mamba-2 groups, and squared ReLU (So et al., 2022) activation
for FFN layers. We do not use any position embeddings. For Mamba-2 layers, we retain the default
values for head dimension (64), expansion factor (2), and window size for convolution (4). We also
use RMSNorm (Zhang & Sennrich, 2019) for normalization, separate embedding and output layer
weights, and no dropout. We do not use bias weights for linear layers. We include a residual skip
connection around each Mamba-2, self-attention, and FFN layer in the architecture.
Nemotron-T-8B Transformer baseline.
To compare Nemotron-H-8B-Base to a Transformer
model in an apples-to-apples fashion, we also trained Nemotron-T-8B-Base on exactly the same
data. The Nemotron-T-8B architecture follows the style of GPT-3 (Brown et al., 2020). We use 32
Transformer layers (each has a self-attention layer followed by a FFN layer). As for Nemotron-H-8B,
we use a hidden dimension of 4096, 32 query heads, GQA with 8 kev-value heads, a FFN hidden
dimension of 21504, squared ReLU activation, RMSNorm, no bias weights for linear layers, no
dropout, and separate parameters for model embeddings and output layer weights. We use RoPE
for position embeddings (Su et al., 2023).
2.2. Pre-Training Data
Nemotron-H-8B-Base and Nemotron-H-56B-Base are pre-trained on a large corpus of high-quality
curated and synthetically-generated data.
2.2.1. Curated Data
We have separate data curation pipelines for four broad data categories: general web crawl data,
math data, code data, and “academic” data. We discuss each in turn next.
Web crawl data.
For Nemotron-H, we made several key innovations in our processing of English
Common Crawl data compared to Nemotron-4 (Parmar et al., 2024; NVIDIA, 2024); these innovations
substantially improved data quality. For full details on how this dataset was prepared and various
ablations, please refer to the dedicated paper (Su et al., 2024). We provide a brief summary here.
We focus primarily on extracting as many high quality tokens as possible, so that we can train
4

--- Page 5 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
Quality label
Tokens (billions)
Tokens (%)
High
554
8.8
Medium-High
505
8.1
Medium
2026
32.4
Medium-Low
896
14.3
Low
403
6.4
Synthetic-High
1536
24.6
Synthetic-Low
336
5.4
Table 2 | Quality distribution of the 6.3 trillion English Common Crawl tokens.
59.0
53.4
53.0
42.9
42.4
MMLU Accuracy
0
20
40
60
Nemotron-CC-HQ
DCLM
Nemotron-CC
FineWeb-Edu
FineWeb-Edu-2
+5.6 MMLU
4x more data
Figure 3 | MMLU scores for 8B-parameter models trained for 1 trillion tokens. Compared to DCLM,
our methods enable us to either create a 4× larger dataset of similar quality or increase the MMLU
using a high quality subset of the tokens. Having a larger dataset (in terms of unique tokens), is
crucial when training over long horizons (e.g., 15 or 20 trillion tokens).
Nemotron-H for long token horizons (e.g., 15 trillion or more tokens). As is common, we begin
with HTML-to-text extraction, language filtering, global fuzzy de-duplication, and exact substring
de-duplication. At this stage, however, we deviate from the norm and employ an ensemble of three
model-based classifiers to bucket each document into five quality categories. By using an ensemble,
we obtain a larger and more diverse set of high-quality tokens compared to approaches that use a
single model-based classifier. To retain as many high-quality tokens as possible, we apply heuristic
and perplexity filters to the low, medium-low, and medium quality buckets. We also rephrase the
low-quality tokens to boost their quality; §2.2.2 describes the synthetic data generation pipeline.
The resulting dataset consists of 6.3 trillion tokens, including 4.4 trillion globally de-duplicated
“real” tokens and 1.9 trillion tokens of rephrased synthetic data. The quality distribution is shown
in Table 2. As shown in Figure 3, our dataset results in higher-quality models compared to other
leading English Common Crawl preparations like DCLM (Li et al., 2024) and FineWeb-Edu (Penedo
et al., 2024): using a high-quality subset increases MMLU by 5.6 points over DCLM, whereas using
the full dataset without any weighting of quality buckets achieves comparable accuracy to DCLM
while having 4× more unique tokens. Having more unique tokens enables pre-training over longer
token horizons without having to do more than 4 to 8 epochs over the full dataset. Higher epoch
5

--- Page 6 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
counts lead to diminishing returns (Muennighoff et al., 2024; Feng et al., 2024).
For the benefit of the community, we have publicly released the dataset (as Nemotron-CC1) under
the Common Crawl terms of use.
Math data.
To ensure that technical pages in Common Crawl retain their mathematical content,
we leverage the recipe and code base from Paster et al. (2023). We also find it essential to apply this
recipe to other high-quality data sources such as Wikipedia. We found that a smaller, higher-quality
dataset led to a larger improvement on relevant benchmarks, similar to FineMath (Allal et al., 2025).
Code data.
We pre-train Nemotron-H models with a considerable number of code tokens. We
started from our previous work on Nemotron-4 (Parmar et al., 2024; NVIDIA, 2024), and chose to
reduce the number of tokens in markup and configuration languages such as HTML, Markdown,
YAML, CSS, JSON, and Makefile. Tokens that would have previously come from these languages
are instead taken from popular languages like Python, C++, C, and Java.
Academic data.
The Nemotron-H pre-training dataset contains additional tokens gathered from
“high information” English texts, including permissively-licensed books and articles. We utilize
examples across a wide variety of domains (e.g., science, math, humanities, law, and engineering) and
a large range of document types including peer-reviewed journal publications, textbooks, published
novels, and patent documents.
As the original data formats of these documents range widely—including EPuB, HTML, XML, plain
text, PDF, LaTeX, and markdown—we write custom functions to parse text from the input format
into a standardized output format. We maintain appropriate formatting in markdown or LaTeX for
complex segments like tables, lists, and equations. We utilize Éclair (Karmanov et al., 2025) for
PDF-to-text extraction. We also develop specialized heuristic filters to remove extraneous information
contained within headers or footers of pages. We then apply the Nemotron-4 heuristic and perplexity
filters to remove low-quality documents from the set of documents used for pre-training.
In order to better weight examples from these sources in our final data blend, we developed classifiers
to rate documents on their educational content and difficulty. We also try to determine each
document’s domain (one of biology, business, chemistry, computer science, economics, engineering,
history, law, mathematics, medicine, philosophy, physics, psychology, or other). For educational
content, we rated all documents on a numerical scale from 0 (no educational information) to 3
(highly relevant educational information). For educational difficulty, we categorized documents with
high educational content into the following levels: elementary school, middle school, high school,
undergraduate, and graduate. We were able to use these buckets (e.g., “biology at the undergraduate
level with high educational content”) to determine document weights (§2.2.3). As expected, we
found increasing the weight of highly educational content in important domains at the high school /
undergraduate levels to be most helpful.
2.2.2. Synthetically-Generated Data
We also synthetically generate data to de-noise low-quality data and to increase the diversity of
tokens given to the model. We use different processing pipelines to synthetically re-write web crawl,
math, and code data.
Web crawl data.
We found rephrasing text by LLMs to be an effective way to reduce noise and
errors in low-quality crawl data, and produce additional variants of high-quality data with new
unique tokens. This leads to better results on downstream tasks.
1https://data.commoncrawl.org/contrib/Nemotron/Nemotron-CC/index.html.
6

--- Page 7 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
Source
Raw tokens
Prompt
Synthetic tokens
Low
403.0
Wikipedia
336.3
High
451.3
Wikipedia
372.9
Diverse QA Pairs
499.5
Distill
157.6
Extract Knowledge
303.6
Knowledge List
203.2
Table 3 | Synthetic data token counts (billions) for web crawl, generated with the instruct version of
Mistral NeMo 12B.
We rephrased our low-quality data using the “medium Wikipedia” prompt from Maini et al. (2024).
For high-quality documents, we generated synthetic data using four additional prompts:
1. Diverse question-answer (QA) pairs. Ask questions in various forms (e.g., yes/no question,
open-ended question, multi-choice question) about factual information in the text.
2. Distill. Rewrite the text into a concise and clear passage.
3. Extract knowledge. Rewrite knowledge from the text and disregard uninformative content.
4. Knowledge list. Extract key information from the text as an organized list.
These prompts required the model to provide clear and concise responses while preserving factual
information and concrete details such as numbers. In total, we generated over 1.8 trillion synthetic
tokens using the instruct version of Mistral NeMo 12B. The breakdown of source and generated
tokens by quality and prompt is shown in Table 3. The full details of this synthetic data generation,
including the prompts used, have been published separately in Su et al. (2024).
Math data.
We use synthetic data to enhance mathematical reasoning benchmarks like GSM8K
and MATH (Cobbe et al., 2021; Hendrycks et al., 2021b), as detailed in Akter et al. (2024).
We expand OpenWebMath (Paster et al., 2023) from 14 billion to over 100 billion tokens using
Nemotron-4-340B (NVIDIA, 2024), yielding an 18-point improvement on GSM8K in controlled
experiments.
To achieve this, we start with technical pre-training documents from Common Crawl and leverage
Nemotron-4-340B to generate dialogues, where a knowledgeable persona guides a less-experienced
one (e.g., an interaction between student and teacher). This approach aligns with insights from
the Physics of Language Models series (Allen-Zhu & Li, 2024), and incorporates strategies such as
presenting incorrect answers alongside corrections. By structuring content as learning interactions,
our method distills broad knowledge from public language models without overfitting to benchmarks.
Code data.
With the goal of adding diverse code data centered around problem solving, we
chose to synthetically generate mixed natural language and code datasets across 11 programming
languages, e.g., Python, C++, C, C#, and Java. To do this, we prompted Mixtral 8x22B to generate
a programming problem inspired by sampled pieces of source code from our curated code dataset.
The samples range from 1 to 15 lines of code (LOC), and typically are just a small function. We
also prompted Mixtral 8x22B to solve the generated problems and removed clearly invalid solutions
on a minimal-effort basis. For example, we extracted the Python code generated by the model
and attempted to parse it into an abstract syntax tree (AST), discarding samples which fail to
parse. Finally, to form a sample for training, we combined the generated problem and answer into a
single sample which is a mix of natural language instruction, generated code (typically enclosed in a
markdown code block), and usually an explanation of the approach.
7

--- Page 8 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
multilingual
5.0%
crawl++
4.0%
academic
8.8%
code
20.0%
wiki
0.3%
math
2.9%
web crawl
59.0%
(a) Data mixture of Phase 1.
multilingual
3.7%
crawl++
7.0%
academic
12.0%
code
20.0%
wiki
1.7%
web crawl
40.7%
math
14.0%
(b) Data mixture of Phase 2.
SFT-style
12.6%
multilingual
3.7%
crawl++
7.0%
academic
12.0%
code
20.0%
web crawl
32.7%
math
10.8%
wiki
1.1%
(c) Data mixture of Phase 3.
SFT-style
31.8%
multilingual
3.7%
crawl++
7.0%
academic
12.0%
web crawl
13.5%
math
10.8%
wiki
1.1%
code
20.0%
(d) Data mixture of Phase 4.
Figure 4 | Data mixtures for each phase of Nemotron-H pre-training.
SFT-style data.
We further add synthetic SFT-style data to the pre-training corpus; this
improves the ability of base models to follow instructions. We use the Qwen2.5 series, Mixtral
8x22B, Nemotron-4-340B, and DeepSeek-R1 (only for 56B) models to produce these datasets. We
improve math abilities following the pipeline presented in OpenMathInstruct-2 (Toshniwal et al.,
2024) using carefully curated seed data such as AoPS2. We also synthesize code data using the
approach proposed in Genetic Instruct (Majumdar et al., 2024), with tigerbot-leetcode3 and
the-stack-v24 as seed data. In order to equip the base model with high-quality general knowledge,
we generate question-solution pairs with selected topics and domain-specific documents. In total, we
add 230 billion synthetic SFT-style tokens (174 billion math tokens, 35 billion code tokens, and 21
billion tokens with general knowledge) to the training corpus.
2.2.3. Data Mixture and Ordering
Our data mixture consists of seven high-level data categories: web crawl, math, wikipedia, code,
academic, crawl++, multilingual, and synthetic SFT-style data. Crawl++ consists of web-crawl
derivatives like OpenWebText, BigScience and Reddit. Our multilingual data has nine languages:
German, Spanish, French, Italian, Portuguese, Chinese, Japanese, Korean, and Russian. We design
the data mixtures in such a way that all data sources of a given quality are weighed similarly, and
data sources of higher quality are weighed higher than data sources of lower quality. We provide
more details on estimating the quality of datasets in Feng et al. (2024).
2https://artofproblemsolving.com.
3https://huggingface.co/datasets/TigerResearch/tigerbot-kaggle-leetcodesolutions-en-2k.
4https://huggingface.co/datasets/bigcode/the-stack-v2.
8

--- Page 9 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Tokens
1e12
0.3
0.2
0.1
0.0
0.1
0.2
0.3
Relative difference (%)
Training LM loss
(BF16 - FP8) / BF16
Figure 5 | The relative training loss gap between a pair of 8B-parameter Transformer models trained
for 3 trillion tokens in BF16 and FP8. The gap is initially large, then shrinks, and then grows again
in the last stage of training.
We use a phased data-blending approach (Feng et al., 2024) to pre-train both Nemotron-H base
models. In the first phase, we use a data mixture that promotes diversity in data; in the second
and third phases, we primarily use high-quality datasets (e.g., Wikipedia). We switch to the second
phase at the 60% point of training, and to the third phase at the 80% point of training. The fourth
phase is performed for the last 380 billion training tokens. The data mixtures used in each phase
are shown in Figure 4. Our initial experiments on a 8-billion-parameter model trained on 1 trillion
tokens show that a phased approach for pre-training outperforms random data ordering by 3.4%.
2.3. FP8 Recipe
Nemotron-H-56B-Base was pre-trained using layer-wise mixed precision: all linear layers in the
model (including both linear layers in FFN blocks and the QKV / output projection in the attention
block) were computed in FP8 precision, except the first 4 and last 4 layers, which were kept in BF16.
We quantized both the forward and backward passes of the linear layers. As in Micikevicius et al.
(2022), we use a hybrid FP8 approach which uses E4M3 for weight and activation tensors, and E5M2
for the gradient tensors.
We used FP8 per-tensor dynamic quantization, which has several steps: we first compute a quantiza-
tion scale (with a check for division by zero); then, we multiply the input tensor with the quantization
scale and cast it to the desired FP8 format. The quantization scale is computed as a ratio of the
maximum representable value for that FP8 data format divided by the maximum absolute value of
the input tensor.
We observed that the log-likelihood loss curves for FP8 pre-training experiments were almost always
higher than for their BF16 counterparts, but by a surprisingly small amount, with typical relative
gaps less than 0.1% on both training and validation. This loss gap tended to decrease as training
progressed but then widened in the last quarter of training. We conjecture that this is because
extremely small gradient updates, which dominate the latter parts of training, get flushed to zero
despite operating in E5M2. Figure 5 shows a typical relative loss gap between a BF16 and FP8
experiment during pre-training.
Despite the marginally worse loss curves, we observed that downstream evaluations for models trained
with FP8 were as good or better than BF16 experiments. Log likelihood, which has traditionally
served as a proxy for downstream task, was not a reliable predictor in our experiments; in fact, we
often observed models with better loss curves to perform worse on downstream evaluation tasks.
9

--- Page 10 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
0.00
0.25
0.50
0.75
1.00
1.25
1.50
Tokens
1e13
45
50
55
60
65
70
Accuracy (%)
MMLU
0.00
0.25
0.50
0.75
1.00
1.25
1.50
Tokens
1e13
54
56
58
60
62
64
Accuracy (%)
Average commonsense understanding
0.00
0.25
0.50
0.75
1.00
1.25
1.50
Tokens
1e13
25
30
35
40
45
50
55
Accuracy (%)
Average code
0.00
0.25
0.50
0.75
1.00
1.25
1.50
Tokens
1e13
20
40
60
Accuracy (%)
GSM8K
BF16
FP8
Figure 6 | Downstream task accuracies for a pair of 8B-parameter Transformer models trained on
15 trillion tokens with BF16 and mixed precision FP8. FP8 accuracies are consistently equal to or
better than BF16 ones. The jump in accuracies at 9 trillion tokens is a result of switching data
mixtures from Phase 1 to Phase 2.
For coding and math tasks, experiments using per-tensor current scaling often had results that
were substantially better than BF16 experiments. Figure 6 shows the accuracy gap between two
8B-parameter Transformers trained for 15 trillion tokens, with one trained in FP8 and the other in
BF16. Because of the equal or better downstream results on the same token horizon, we never had
to overtrain FP8 models relative to BF16 ones. We ran evaluations in both BF16 and FP8 precision
for models trained in FP8; they were typically the same, with BF16 evaluations usually slightly
better. However, for the 56B model, the FP8 evaluations eventually outperformed the BF16 ones.
We found it very important to do verification on a minimum of 8B parameters when constructing our
FP8 recipe, as results with smaller models did not generalize. All experiments used token horizons
of at least 1 trillion tokens.
2.4. Pre-Training
We trained Nemotron-H-8B-Base on a token horizon of 15 trillion tokens and Nemotron-H-56B-Base
on a token horizon of 20 trillion tokens. We used a sequence length of 8192 and global batch size of
768 (6291456 tokens per batch). We do not use any batch size ramp-up. For Nemotron-H-8B-Base,
we used a peak learning rate of 8·10−4 and warmup over 8.3 billion tokens; for Nemotron-H-56B-Base,
we used a peak learning rate of 4 · 10−4 and warmup over 25 billion tokens. In both cases, we used
cosine learning rate decay with a minimum value equal to 1% of the peak value, weight decay of 0.1,
10

--- Page 11 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
and 0.9 and 0.95 for Adam 𝛽1 and 𝛽2, respectively
We pre-train Nemotron-H using Megatron-LM5; we rely on Transformer Engine6 for FP8 support.
We use 8-way tensor model parallelism (Shoeybi et al., 2020) with sequence parallelism (Korthikanti
et al., 2022) for additional memory savings, and 768-way data parallelism with optimizer state
distributed over the data-parallel replicas (Rajbhandari et al., 2020).
2.4.1. Resiliency
We also focus heavily on minimizing downtime when training models at scale: over long training
jobs on a large number of GPUs, job failures and slowdowns are inevitable, leading to lost training
productivity. Failures can occur due to GPU-related errors (e.g., uncorrectable ECC errors or
GPUs falling off the bus), errors in shared infrastructure like the network fabric or Lustre, or
application-induced failures (e.g., numerical instability in certain operations or “bad” data). We
can also experience job slowdowns due to a variety of reasons (e.g., single-GPU throttling or slower
communication collectives).
To minimize the impact of the above issues, we focus on a) accurately attributing failures to the
correct infrastructure and application components to prevent repeated disruptions, and b) reducing
the recovery overhead of each failure. To do so, we leverage the DGX Cloud Resilience service7 to
ensure failures are correctly attributed and the appropriate hardware component (e.g., particular
HGX node with failing GPU) is not included in the next instance of the training job, preventing
repeated failures. With DGX Cloud Resilience enabled, we obtained a 3.3× improvement in mean
time between failures (MTBF) in our cluster.
We also proactively save checkpoints frequently in order to minimize the amount of work lost when a
failure occurs (weight updates from the last checkpoint save to the failure are lost). We use NVRx8
to facilitate checkpointing with low overhead by asynchronously saving checkpoints without blocking
training. We also optimized job restart times (i.e., the set of operations needed by Megatron-LM
before training iterations can start like distributed runtime initialization and checkpoint loading).
Altogether, the above components enable us to train Nemotron-H-56B-Base with high efficiency on
6144 NVIDIA H100 GPUs.
2.5. Base Model Evaluations
We run evaluations of all models ourselves unless otherwise stated. Our evaluation setup is built on
top of lm-evaluation-harness9 for fair comparisons, with the following changes:
1. For mathematical reasoning, we evaluate on the GSM8K and MATH (Cobbe et al., 2021;
Hendrycks et al., 2021b) benchmarks. We also highlight the competition-level slice of the
MATH benchmark as “MATH Level 5”. After carefully looking through disagreeing cases,
we use a combination of Math-Verify10 and the math grading utilities of NeMo-Skills11 to
grade solutions.
2. We also include a MATH-R1 version of the MATH task, where we provide few-shot examples
5https://github.com/nvidia/megatron-lm.
6https://github.com/nvidia/transformerEngine.
7https://developer.nvidia.com/blog/ensuring-reliable-model-training-on-nvidia-dgx-cloud/.
8https://github.com/NVIDIA/nvidia-resiliency-ext.
9https://github.com/EleutherAI/lm-evaluation-harness.
10https://github.com/huggingface/math-verify.
11https://github.com/NVIDIA/NeMo-Skills/blob/main/nemo_skills/code_execution/math_grader.py.
11

--- Page 12 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
Task
N-H
56B-Base
N-H
47B-Base
Qwen-2.5
72B-Base
Llama-3.1
70B-Base
DS-V3
671B-Base
Llama-3.1
405B-Base
General
MMLU-Pro (5-shot COT)
60.5
61.8
58.8
51.3
64.4
52.8
MMLU (5-shot)
84.2
83.6
86.1
78.8
87.1
84.4
Math
GSM8k (8-shot COT)
93.7
93.3
90.9
83.9
89.3
83.5
MATH (4-shot COT)
59.4
57.4
64.6
42.9
61.6
49.0
MATH Level 5 (4-shot COT)
35.2
34.1
41.2
21.1
MMLU STEM (5-shot)
80.6
79.8
84.9
70.5
Code
HumanEval (0-shot greedy pass@1)
60.4
61.0
56.7
57.3
65.2
54.9
HumanEval+ (0-shot greedy pass@1)
54.3
56.1
50.0
52.4
MBPP sanitized (3-shot greedy pass@1)
77.8
75.9
78.2
70.0
75.4
68.4
MBPP+ (0-shot greedy pass@1)
67.2
65.6
71.7
66.9
Commonsense understanding
Arc-Challenge (25-shot)
95.0
94.6
95.8
93.0
95.3
95.3
Hellaswag (10-shot)
89.0
87.9
87.6
88.1
88.9
89.2
Winogrande (5-shot)
84.5
83.9
84.4
85.6
84.9
85.2
PIQA (0-shot)
85.0
83.9
83.6
84.1
84.7
85.9
OpenbookQA (0-shot)
48.6
48.8
46.2
47.6
Long-thought reasoning
MATH (R1-style 4-shot COT)
87.8
73.9
38.7
MATH Level 5 (R1-style 4-shot COT)
74.8
53.2
16.7
Table 4 | Accuracy of Nemotron-H-56B-Base (and its distilled version Nemotron-H-47B-Base,
discussed in §3) versus existing SoTA models.
N-H is short for Nemotron-H, DS is short for
DeepSeek. Numbers in italics are from the DeepSeek-V3 report (DeepSeek-AI, 2025c), all other
numbers are run by us. We bold the highest accuracy in each row, excluding italicized numbers.
generated by DeepSeek-R1 (DeepSeek-AI, 2025b). Both Nemotron-H and the Qwen 2.5 models
show significant improvement on the benchmark by simply changing the prompt.
3. For code tasks (HumanEval (Chen et al., 2021), MBPP (Austin et al., 2021) and their EvalPlus
variants), we always sanitize the generations using EvalPlus (Liu et al., 2023b).
4. General reasoning benchmarks (OpenBookQA (Mihaylov et al., 2018), PIQA (Bisk et al.,
2019), Hellaswag (Zellers et al., 2019), Winogrande Sakaguchi et al. (2019)) are unchanged
except for ARC-Challenge (Clark et al., 2018), where we present all options at the same time,
similar to MMLU (Hendrycks et al., 2021a).
Accuracy results for Nemotron-H-56B-Base and Nemotron-H-8B-Base on common benchmark tasks
are shown in Table 4 and Table 5. Nemotron-H-56B-Base and Nemotron-H-47B-Base are both
evaluated in FP8, and all other models are evaluated in BF16. Across both model sizes, Nemotron-
H base models reach comparable or better accuracy relative to similarly-sized state-of-the-art
Transformer models.
We compare Nemotron-H-56B-Base directly with Qwen-2.5-72B-Base (Qwen, 2025) and Llama-3.1-
70B-Base (Meta, 2024). Out of the 17 task we evaluate, Nemotron-H-56B-Base achieves the highest
accuracy of the three models on 9 tasks, Qwen-2.5-72B-Base achieves the highest accuracy on 7 tasks,
and Llama-3.1-70B-Base achieves the highest accuracy on 1 task; Nemotron-H-56B-Base outperforms
Llama-3.1-70B-Base on all but that single task (Winogrande). We further compare Nemotron-H-56B-
Base with two much larger state-of-the-art models, DeepSeek-V3-671B-Base (DeepSeek-AI, 2025c)
12

--- Page 13 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
Task
Nemotron-H
8B-Base
Nemotron-T
8B-Base
Qwen-2.5
7B-Base
Llama-3.1
8B-Base
Gemma-3
12B-Base
General
MMLU-Pro (5-shot COT)
44.0
41.4
48.3
35.9
45.3
MMLU (5-shot)
72.8
73.2
74.2
65.3
74.5
Math
GSM8k (8-shot COT)
87.1
89.0
83.3
55.5
74.1
MATH (4-shot COT)
46.5
46.7
49.8
19.5
42.1
MATH Level 5 (4-shot COT)
22.9
25.8
24.6
5.6
17.5
MMLU STEM (5-shot)
65.4
65.6
71.2
56.3
Code
HumanEval (0-shot greedy pass@1)
58.5
59.8
56.7
37.8
46.3
HumanEval+ (0-shot greedy pass@1)
55.5
53.0
48.8
31.7
34.1
MBPP sanitized (3-shot greedy pass@1)
65.4
63.4
69.3
57.2
64.6
MBPP+ (0-shot greedy pass@1)
59.5
61.4
65.3
51.6
59.0
Commonsense understanding
Arc-Challenge (25-shot)
88.7
88.3
89.2
80.4
Hellaswag (10-shot)
83.2
82.5
80.3
82.3
84.2
Winogrande (5-shot)
80.5
78.8
76.1
78.1
74.3
PIQA (0-shot)
82.2
82.0
80.1
81.0
81.8
OpenbookQA (0-shot)
47.2
44.8
47.0
45.4
Table 5 | Accuracy of Nemotron-H-8B-Base versus existing SoTA models and a Transformer
(Nemotron-T-8B-Base) trained on exactly the same data.
Likelihood-based evaluations of the
Gemma 3 model are based on the Gemma 3 report (DeepMind, 2025), all other numbers are run by
us. We bold the highest accuracy in each row, excluding italicized numbers.
and Llama-3.1-405B-Base (Meta, 2024); we use publicly-reported numbers for these two models on the
subset of common tasks where numbers are reported. Surprisingly, Nemotron-H-56B-Base remains
competitive with these models, outperforming DeepSeek-V3-671B-Base and Llama-3.1-405B-Base on
4 and 5 out of the 10 overlapping tasks respectively.
We observe similar accuracy results for Nemotron-H-8B-Base compared to Qwen-2.5-7B-Base and
Llama-3.1-8B-Base (Table 5). Out of the 15 tasks used for evaluation, Nemotron-H-8B-Base, Qwen-
2.5-7B-Base, and Llama-3.1-8B-Base achieve the highest accuracy of the three models on 7, 8, and
0 tasks respectively. Nemotron-H-8B-Base is particularly strong on commonsense understanding
tasks, achieving the highest accuracy on 4 out of 5 tasks in this category. As above, we also include
comparisons to a larger model, Gemma-3-12B-Base (DeepMind, 2025); Nemotron-H-8B-Base is
competitive with the larger model.
Table 5 additionally includes the largest apples-to-apples comparison of a hybrid Mamba-Transformer
and pure Transformer model to date (Nemotron-H-8B-Base versus Nemotron-T-8B-Base). Nemotron-
H-8B-Base reaches higher accuracy than the Transformer trained on exactly the same data on 7 out
of 15 tasks, and is within one point on an additional 4 tasks. Overall, this experiment shows that
hybrid models can reach equal or better accuracy compared to Transformer models when trained at
state-of-the-art scales.
2.6. Inference Speed
Due to the reduction in self-attention layers, Nemotron-H-8B/56B-Base provide inference-time
speedups compared to the alternative Transformer models in Tables 4 and 5 above. To quantify these
speedups, we plot the MMLU-Pro accuracy versus inference throughput for Nemotron-H-56B-Base
13

--- Page 14 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
25
50
75
100
125
150
175
200
225
250
Throughput (Output tokens/s/GPU)
20
25
30
35
40
45
50
55
MMLU-Pro accuracy (%)
1.8x
Nemotron-H-8B
Nemotron-T-8B
Llama-3.1-8B
Llama-3.2-3B
Qwen-2.5-7B
Gemma-3-12B
Gemma-3-27B
Input sequence length = 65536  / Output sequence length = 1024
Figure 7 | MMLU-Pro accuracy versus inference throughput (normalized by number of GPUs used)
for Nemotron-H-8B-Base compared to existing similarly-sized Transformer models.
and similarly-sized Transformer models in Figure 1 and for Nemotron-H-8B-Base and relevant
baselines in Figure 7. We use an input sequence length of 65536 and ask the models to generate 1024
output tokens. We use an initial Megatron-LM implementation for Nemotron-H inference and vLLM
v0.7.312 for baselines. In these experiments, we try to maximize per-GPU inference throughput by
using as large a batch size as possible, and we run all experiments on NVIDIA H100 GPUs. We
report results normalized by the number of GPUs used (i.e., output tokens per second per GPU).
In the setting described above, Nemotron-H-56B-Base can generate 2.4× more output tokens per
second per GPU compared to Qwen-2.5-72B and Llama-3.1-70B (and 2.9× more after distillation
to Nemotron-H-47B-Base, see §3). Compared to Llama-3.1-405B, Nemotron-H-56B-Base achieves
19.6× higher throughput. Similar to the larger models, Nemotron-H-8B-Base is also faster to infer
than corresponding Transformer models. As shown in Figure 7, on longer contexts, we measure
a 1.8× and 3× speedup compared to Qwen-2.5-7B and Llama-3.1-8B. Inference speedups are a
byproduct of two factors: a) constant computation in the Mamba-2 layers as opposed to linear
computation in self-attention layers, b) lower memory footprint from Mamba-2 layers facilitates
using higher batch sizes, increasing efficiency. We expect further optimizing Nemotron-H inference
to lead to additional speedups compared to Transformers, which have been heavily optimzed over
the last couple of years.
3. Compression and Distillation
Efficient deployment of LLMs often requires tailoring the model architecture to specific constraints
imposed by hardware. In this section, we describe the pruning and distillation process used to
compress the 56B model to 47B parameters with the goal of running longer context inference on the
NVIDIA GeForce RTX 5090 GPU (storing the weights of a 56B parameter model in FP4 precision
on a RTX 5090 GPU with 32GiB of memory will require 29.5GiB, leaving only 2.5GiB for KV
cache and activation buffers). We introduce a novel model compression framework called MiniPuzzle
that combines the simplicity of Minitron (Sreenivas et al., 2024; Muralidharan et al., 2024) with
the versatility of Puzzle (Bercovich et al., 2024). Our approach uses roughly 300× fewer tokens to
obtain a 47B model compared to training from scratch. Our compressed 47B model achieves a 1.2×
inference speedup (Figure 1) while achieving accuracy on par with the original 56B model.
12https://github.com/vllm-project/vllm/tree/v0.7.3.
14

--- Page 15 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
3.1. MiniPuzzle Overview
Figure 8 | MiniPuzzle’s optimization process: a) estimate layer and FFN importance scores, b) search
for the best model candidates using the conditional Neural Architecture Search (NAS) framework,
considering the 32GiB GPU memory constraint, c) select the best candidate with lightweight
distillation and recover the accuracy lost due to pruning with longer distillation.
MiniPuzzle combines lightweight pruning with neural architecture search (NAS) to produce efficient
compressed models that meet specific target deployment constraints. Figure 8 provides a high-level
overview of the framework. MiniPuzzle’s optimization process consists of three stages: a) importance
estimation (§3.2), b) conditional NAS (§3.3), and c) knowledge distillation (§3.4).
3.2. Importance Estimation
MiniPuzzle first collects importance or sensitivity scores for each model component (e.g., layers,
FFN neurons) to help decide which components to remove; this is the importance estimation phase.
The scores computed in this phase are used to decide which model components can be pruned.
We note that sensitivity analysis based on gradient information is typically impractical at modern
LLM scale (Muralidharan et al., 2024); instead, we rely on a lightweight strategy that uses only on
forward passes. In this work, we use a simplified approach that works well in our ablation studies:
a) prune layers, and b) prune FFN hidden dimensions (effectively neurons). We also experimented
with pruning Mamba heads and Mamba head dimension; unfortunately, both axes caused severe
accuracy degradation (particularly head dimension pruning).
We now describe how we compute the importance of each layer and FFN neuron.
Layer importance.
We use the scoring method from Puzzle to estimate the importance of each
layer in the model. Given an input tensor, layer importance is computed as the Mean Squared
Error (MSE) between the intermediate activation tensor just before the LM head of the full model
and the same activation tensor for a model with the particular layer removed. We average these
rankings over a small random subset of the training data (128 samples in our case) to obtain a
reliable estimate of importance that takes into account sample variability.
Figure 9 plots average importance scores of each layer in Nemotron-H-56B-Base. The green, blue
and red dotted lines correspond to self-attention, FFN and Mamba layers. We notice from the figure
that the 56B model follows a typical pattern observed in Minitron: the most important layers are
concentrated at the beginning and end of the model. Additionally, MSE importance reveals that
even though the 56B model only has 10 self-attention layers, some self-attention layers are ranked
among the least important, particularly the 84th (7th self-attention layer). However, layers 40, 51,
62 and 73 seem to be more important compared to the other layers in their immediate vicinity.
15

--- Page 16 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
0
20
40
60
80
100
118
Layer index
0.000
0.025
0.050
0.075
0.100
0.125
0.150
MSE
Per-layer importance
Average
Mamba layer
MLP layer
Self-attention layer
Figure 9 | Layer importance measured as the MSE between the full model and a model with that
layer removed, averaged over a small training subset. Vertical dotted lines indicate layer types:
self-attention (green), FFN (blue), and Mamba-2 (red).
FFN importance.
FFN layers internally are composed of two linear operators with a non-linear
activation in between:
FFN(X) = 𝛿
(︂
X · 𝑊𝑇
1
)︂
· 𝑊2.
Here, X denotes the input, and 𝑊1 and 𝑊2 are the two associated weight matrices in the FFN
layer. 𝑊1, 𝑊2 ∈R𝑑𝑓𝑓𝑛×𝑑𝑚𝑜𝑑𝑒𝑙, where 𝑑𝑚𝑜𝑑𝑒𝑙and 𝑑𝑓𝑓𝑛are the model hidden dimension and FFN
hidden dimension respectively (Table 1). 𝛿(·) refers to the non-linear activation function (squared
ReLU in this work).
Following the same procedure as Minitron, we compute the importance of each neuron in the first
linear operator of each FFN layer by examining the set of outputs it produces. We use a small
calibration dataset of 1024 samples for this purpose. Formally, we compute each neuron’s importance
score by aggregating its outputs given an input batch 𝑋:
𝐹(𝑖)
neuron =
∑︁
B,S
𝛿
(︂
X
(︀𝑊𝑖
1
)︀𝑇
)︂
.
Here, 𝑊𝑖
1 refers to the 𝑖th row of the weight matrix 𝑊1. ∑︀
B,S refers to aggregation along the batch
and sequence dimensions. We use the mean and l2-norm aggregation functions along the batch and
sequence dimensions, following the observations in the Minitron paper (Muralidharan et al., 2024).
For a sequence of scores S, mean aggregation is defined as 1
𝑛
∑︀𝑛
𝑖=1 |S𝑖|, and l2-norm is
√︁∑︀𝑛
𝑖=1 S2
𝑖.
3.3. Conditional NAS
MiniPuzzle’s conditional NAS utilizes the importance scores of every layer and FFN neuron (computed
as described in §3.2) to identify architectures that meet memory constraints while preserving the
most critical components. This process allows us to efficiently explore the vast search space of
possible layer configurations, and consists of three steps:
1. Pruned candidate enumeration. We iterate over a grid of possible layer counts for each layer
type (i.e., number of self-attention, FFN, and Mamba-2 layers), and FFN hidden dimension
(24576, 25600, . . . , 32768). For each target layer count and FFN hidden dimension size, we
select the top layers and neurons based on their respective importance scores (see §3.2 for
details on importance estimation) and realize the corresponding architecture; i.e., we drop
16

--- Page 17 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
30.3
30.8
31.2
31.7
32.2
32.7
33.2
33.7
34.2
Estimated memory load (GiB)
0.45
0.50
0.55
0.60
0.65
Average benchmark score
Figure 10 | Average benchmark score for pruned candidates with different memory budgets. Each
dot represents a different candidate, i.e., model with different set of layers pruned with respect to
how much memory it consumes. The green dotted line marks the upper memory limit we consider
and the dots marked with red circles are the candidates selected for further distillation.
0
20
40
60
80
100
118
Layer index
Candidate 1
Candidate 2
Candidate 3
Figure 11 | Pruned layers for the top three candidates. Each row represents a candidate, with dots
indicating dropped layers. Vertical dotted lines denote layer types: green for self-attention, blue for
FFN, and red for Mamba.
the irrelevant layers and prune all FFN layers to the same target width. Only architectures
that meet the target memory constraint of less than 31.7 GiB (computed as the total memory
required for FP4 inference on a context of size 1 million tokens) are retained, resulting in
around 400 candidate architectures.
2. Architecture ranking. We score the candidate architectures using a lightweight metric that
compares them to the parent model (Nemotron-H-56B-Base) on a small validation corpus
with 1 million tokens. Specifically, we use two different scores to estimate the quality of each
candidate model: a) next-token accuracy which computes how often the child model correctly
predicts the next ground-truth token, and b) next-token parent agreement which computes
how often the child model agrees with the parent model about the greedy prediction of the
next token. We rank all candidate architectures using both scoring metrics, and retain the top
130 performers.
3. Candidate selection. We now refine the set of ranked architectures from 130 to a manageable
3 by benchmarking them on a subset of evaluation tasks. The first column of Table 6 lists
the tasks we use to evaluate the final 3 candidates. We use the average scores across all these
tasks for evaluation. Figure 10 plots the average benchmark scores for all 130 candidates, and
Figure 11 illustrates the specific layers dropped by all three candidates. Candidates 1 and 2
achieve the highest benchmark scores and drop similar layers. Candidate 3, which drops a
slightly different set of layers, performs significantly worse after pruning. However, we include
it here to study the extent to which distillation can compensate for the loss.
17

--- Page 18 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
Benchmark
Nemotron-H
56B-Base
Candidate 1
47B-pruned
Candidate 2
47B-pruned
Candidate 3
47B-pruned
MMLU
84.2
81.5 →83.7
80.8 →83.2
81.3 →83.6
Commonsense understanding (average)
67.6
64.2 →66.6
63.8 →67.2
64.5 →66.8
GSM8k
91.4
67.9 →89.2
60.7 →91.1
19.5 →90.5
Code (average)
67.0
52.0 →64.9
52.7 →64.6
23.0 →64.9
AVERAGE
70.6
63.3 →69.3
62.1 →69.6
53.7 →69.5
Table 6 | Comparison of benchmark scores for pruned candidates before and after lightweight
distillation. Scores might be slightly different to those presented in Table 4 due to minor differences
in evaluation settings and averages over different sets of tasks.
3.4. Retraining with Distillation
To recover the accuracy lost due to pruning, the model undergoes continued training. Recent work
has demonstrated that distilling knowledge from the original model to the pruned model outperforms
conventional fine-tuning (as shown in Minitron and Puzzle); we thus adopt logit-based distillation for
continued training, employing forward KL divergence loss exclusively during the accuracy recovery
phase (see §3 of the Minitron paper for more details on the distillation loss formulation).
Following the initial candidate selection process described in §3.3, we perform short distillation of
the top 3 candidates using ∼7B tokens, with the 56B model as the teacher. We observe from our
experiments that this step is crucial for picking the best possible final candidate. Table 6 details
the benchmark scores for the 3 candidates before and after short distillation. The most accurate
candidate (averaged across all benchmarks) of the three is chosen for an extended distillation run
using 63 billion tokens to produce the final 47B model; in our case, Candidate 2 performs best, as
shown in Table 6. We observe that the choice of the final candidate varies based on the ultimate
objective; for instance, prioritizing accuracy in coding tasks versus commonsense reasoning tasks.
All distillation runs use FP8 precision, a softmax temperature of 1.0, which controls the softness of
the probability distribution during knowledge distillation (Hinton et al., 2015), sequence length of
8192, and a batch size of 768 samples.
3.5. Results
Using the MiniPuzzle approach, we efficiently compress the 56B model to 47B parameters by
pruning full layers (depth) and FFN hidden dimension size, improving inference speed and enabling
longer-context inference on a 32GiB NVIDIA GeForce RTX 5090 GPU. The 47B model retains
half the self-attention layers of 56B (5 instead of 10), along with 44 Mamba-2 layers (down from
54) and 49 FFN layers (down from 54). Additionally, the FFN intermediate size was pruned from
32768 to 30720. As shown in Figure 1 and Table 4, the resulting 47B model achieves a 1.2× faster
inference on long contexts and near-lossless accuracy on benchmarks while requiring roughly 300×
fewer tokens compared to training from scratch.
4. Vision-Language Models
In this section, we introduce Nemotron-H-8B-VLM and Nemotron-H-56B-VLM, which are built on
Nemotron-H-8B-Instruct and Nemotron-H-56B-Base. Vision-Language Models (VLMs) are generally
recommended to be built on aligned models to enhance instruction-following capabilities (Dai et al.,
2024). In this work, we chose to build Nemotron-H-8B-VLM and Nemotron-H-56B-VLM on Nemotron-
18

--- Page 19 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
H-8B-Instruct and Nemotron-H-56B-Base (since Nemotron-H-56B-Instruct was unavailable). Both
Nemotron-H-8B-VLM and Nemotron-H-56B-VLM have been used as the base models for building
Cosmos-Reason1 (NVIDIA et al., 2025), a family of frontier reasoning models for physical AI.
4.1. Model Architecture
In previous studies, VLMs were constructed by integrating a text-only LLM with a vision encoder.
Two prevalent architectures for this integration are the decoder-only architecture (Liu et al., 2023a)
and the cross-attention-based architecture (Alayrac et al., 2022). We use the decoder-only NVLM-D
architecture (Dai et al., 2024) due to its simplicity, parameter efficiency, ability to process high-
resolution image inputs, and unified handling of multiple modalities by mapping non-text tokens
(e.g., images, audio, videos) into the same embedding space as text tokens. Nemotron-H-VLM
comprises a vision encoder, a projector (a two-layer FFN), and the Nemotron-H LLM backbone.
Vision encoder.
For both the 8B and 56B VLMs, we use InternViT-300M-V2.5 (Chen et al.,
2024) as the vision encoder. It processes static 448×448 pixel images as input with patch size 14×14,
and generates 1024 visual tokens in total. Each visual token is represented by a 1024-dimensional
vector. Following the NVLM design (Dai et al., 2024), we dynamically resize the input image to the
closest predefined aspect ratio {𝑎: 𝑏} (𝑎and 𝑏are integers) based on its resolution and segment it
into 𝑎× 𝑏≤12 tiles13, each corresponding to a 448×448-pixel image tile. To preserve global context,
we also generate a thumbnail 448×448 tile, which is a scaled-down version of the whole image. For
example, given a 1920×1080 image, the closest predefined aspect ratio is 3 : 2. The image is resized
to 1344×896 and divided into 3 × 2 + 1 = 7 tiles, including one thumbnail tile.
To reduce processing overhead for the LLM, we downsample 1024 tokens to 256 by grouping four
neighboring image tokens and concatenating them along the channel dimension. The image tokens
from multiple tiles are concatenated with an interleaved tile ID tag in raw text format, which gives
the downstream LLM information about the dynamic tiling structure; we find this is crucial to
improving accuracies on various vision-language benchmarks. For more details, see the NVLM
technical report (Dai et al., 2024). The concatenated visual tokens are processed by a two-layer FFN
block, which maps each visual token into the text token embedding space. These embeddings are
then fed into the LLM backbone.
4.2. Training Method and Data
Following NVLM (Dai et al., 2024), Nemotron-H-VLM is trained in two stages:
1. VL pre-training. We train only the two-layer FFN for modality alignment while keeping
both the Nemotron-H backbone and vision encoder frozen.
2. VL SFT. We fine-tune the vision encoder, FFN projector, and Nemotron-H backbone end-to-
end on various task-oriented SFT data.
For VL pre-training, we utilize a large and diverse image-text pre-training dataset from NVLM (Dai
et al., 2024), including captioning (Lin et al., 2015; Sharma et al., 2018; Ordonez et al., 2011; Li
et al., 2022), visual question answering (VQA) on natural image (Goyal et al., 2017; Krishna et al.,
2017), visual chart (Kafle et al., 2018) and document understanding (Marafioti & Laurencon, 2024),
13The predefined ratios are {𝑎: 𝑏} = {1 : 1, 1 : 2, 1 : 3, 1 : 4, 1 : 5, 1 : 6, 1 : 7, 1 : 8, 1 : 9, 1 : 10, 1 : 11, 1 : 2, 2 :
1, 2 : 2, 2 : 3, 2 : 4, 2 : 5, 2 : 6, 3 : 1, 3 : 2, 3 : 3, 3 : 4, 4 : 1, 4 : 2, 4 : 3, 5 : 1, 5 : 2, 6 : 1, 6 : 2, 7 : 1, 8 : 1, 9 :
1, 10 : 1, 11 : 1, 12 : 1}.
19

--- Page 20 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
Task
Nemotron-H
8B-VLM
VLM w/ Llama3.1
8B-Instruct
VLM w/ Qwen2.5
7B-Instruct
MMMU (val)
51.3
44.8
51.1
MathVista
62.5
61.7
63.8
ChartQA
84.8
85.4
84.9
AI2D
89.6
90.9
91.0
OCRBench
840
847
836
TextVQA
76.2
76.4
76.1
RealWorldQA
62.2
60.9
60.6
DocVQA
90.6
91.3
91.2
Table 7 | Evaluation of Nemotron-H-8B-VLM on vision-language benchmarks. We compare to the
VLMs built with Llama-3.1-8B-Instruct and Qwen2.5-7B-Instruct using the same training recipe.
Task
Nemotron-H
56B-VLM
VLM w/ Qwen2.5
72B-Instruct
NVLM-D-1.0
72B (2024-09-17)
MMMU (val)
63.6
65.1
62.6†
MathVista
70.7
70.5
66.7†
ChartQA
89.4
88.9
86.0
AI2D
94.7
94.9
94.2
OCRBench
862
869
853
TextVQA
81.1
83.5
82.1
RealWorldQA
68.4
71.4
69.7
DocVQA
93.2
92.0
92.6
Table 8 | We evaluate Nemotron-H-56B-VLM on a range of vision-language benchmarks, and compare
it to a VLM built using Qwen2.5-72B-Instruct with the same training recipe. We also compare
with NVLM-1.0-D 72B, a previous state-of-the-art VLM developed by NVIDIA. †We evaluate
NVLM-1.0-D 72B on MMMU and MathVista using VLMEvalKit (Duan et al., 2024); this is the
same evaluation setup used for other models and yields better results than the official numbers.
optical character recognition (OCR) (Mishra et al., 2019) and scene-text recognition (Veit et al.,
2016), and visual math reasoning (Lindström & Abraham, 2022) data. Overall, our VL pre-training
dataset consists of 130 million samples. We apply careful sanitization to remove any potentially
harmful content.
For VL SFT, we leverage diverse and high-quality datasets from NVLM (Dai et al., 2024) and
Eagle2 (Li et al., 2025). In addition to the previously mentioned categories, the dataset also includes
knowledge-based VQA (Marino et al., 2019), visual reasoning (Hudson & Manning, 2019), science-
related VQA (Lu et al., 2022), and visual instruction-following data. Overall, our VL SFT dataset
consists of 6 million image-text samples. Dai et al. (2024) and Li et al. (2025) have more details.
4.3. Vision-Language Benchmark Results
We evaluate Nemotron-H-8B-VLM and Nemotron-H-56B-VLM on a comprehensive set of vision-
language benchmarks, including MMMU (Yue et al., 2024), MathVista (Lu et al., 2024), ChartQA
(Masry et al., 2022), AI2D (Kembhavi et al., 2016), OCRBench (Liu et al., 2024), TextVQA (Singh
et al., 2019), RealWorldQA (xAI, 2024), and DocVQA (Mathew et al., 2021). These benchmarks
assess a broad range of capabilities such as multimodal reasoning, mathematical reasoning in visual
contexts, natural image understanding, scene-text recognition, chart & document understanding,
real-world perception, and OCR.
20

--- Page 21 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
We compare Nemotron-H-8B-VLM with VLMs built on LLaMA-3.1-8B-Instruct and Qwen2.5-7B-
Instruct, using the same training methodology and dataset. As shown in Table 7, Nemotron-H-8B
proves to be a strong LLM backbone for developing best-in-class VLMs. We further compare
Nemotron-H-56B-VLM with NVLM-1.0-D (Dai et al., 2024) and the VLM built with Qwen2.5-72B-
Instruct using the same training recipe in Table 8. Nemotron-H-56B-VLM achieves state-of-the-art
results, demonstrating superior quality compared to previous models.
5. Nemotron-H Reasoning Models
5.1. Nemotron-H Vs. Transformer Model Alignment
We first study the extent to which our hybrid Mamba-Transformer models can be effectively post-
trained into instruction-tuned and long-context variants. We conducted experiments on Transformer
(Nemotron-T-8B-Exp-Base) and hybrid (Nemotron-H-8B-Exp-Base) models pretrained on identical
data resulting in two models with very similar pretraining performance as seen in Table 9.
Task
Nemotron-T
8B-Exp-Base
Nemotron-H
8B-Exp-Base
MMLU (5-shot)
70.3
69.9
GSM8k
64.8
64.1
MBPP+ (0-shot greedy pass@1)
53.7
54.5
PIQA (0-shot)
81.1
82.8
OpenBookQA (0-shot)
45.4
46.2
Table 9 | Comparison of Transformer and hybrid base models on selected tasks.
We then post-trained both base models into instruction-tuned variants, Nemotron-T-8B-Exp-Instruct
and Nemotron-H-8B-Exp-Instruct using a multistage training procedure. In stage1, we perform
supervised fine-tuning (SFT) on a blend of 6 million samples including code, math, and general
instruction-following tasks. To improve long-context performance, we include training on extended
conversations up to 512k tokens by concatenating shorter samples. We further enhance context
by inserting references to earlier turns and introducing semantically related segments across the
conversation. This improves RULER (Hsieh et al., 2024) scores even at shorter context lengths (e.g.,
128k).
In stage2, we switch to preference tuning using offline RPO (Sun et al., 2025) on general-domain
prompts. We then perform an additional RPO round focused on narrow instruction following,
following IFEval (Zhou et al., 2023) style prompts. Samples are randomly extended to 32k tokens
using conversations from stage1, preserving long-context capabilities.
In stage3, we apply on-policy RPO, generating both preferred and dispreferred completions using
the stage2 checkpoint. We incorporate safety data from AEGIS2.0 (Ghosh et al., 2025) and increase
reward scaling, which improves performance on downstream benchmarks.
We experimented with multiple rounds of iterative offline RPO and DPO. Both yielded similar
outcomes; we report results for the best model from either method. The best Transformer model
used three RPO rounds; the best hybrid model used two DPO rounds.
Table 10 shows the results. These findings support that hybrid Mamba-Transformer models can be
post-trained to match or exceed Transformer performance.
21

--- Page 22 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
Benchmark
Nemotron-T
8B-Exp-Instruct
Nemotron-H
8B-Exp-Instruct
MT-Bench
7.9
8.0
MMLU (0-shot generative)
68.0
67.4
MBPP+
65.6
66.9
MATH
68.8
68.5
IFEval Prompt
74.3
74.7
IFEval Instruct
81.8
82.1
BFCL (V2)
64.3
65.4
Table 10 | Comparison of instruction-tuned Transformer and hybrid models on alignment benchmarks.
5.2. Training Nemotron-H Reasoning Models
Following the pilot study in which we found that mamba2-hybrid models and pure transformer
models have similar post-training properties we proceed to train our Nemotron-H 8B Reasoning and
Nemotron-H 47B Reasoning models.
5.2.1. Supervised Finetuning Stages
The training pipeline began with supervised fine-tuning (SFT), using curated examples that include
explicit reasoning traces—enclosed in <think>...</think> tags—to guide the model through step-
by-step problem-solving before reaching a final answer. These traces often represent multiple possible
solution paths and encourage the model to explore alternatives and iterate, improving accuracy.
However, the added verbosity also increases inference cost, especially for longer traces. To balance
this, we introduced paired examples with the reasoning stripped out, allowing the model to learn
when and how to respond directly. This dual-format training helps the model adapt fluidly to
different reasoning requirements.
Stage 1: Mastering Math, Code and Science Reasoning
The first phase of fine-tuning
focused on math, science, and coding—domains where explicit reasoning is especially valuable. The
training data here used a 5:1 ratio of reasoning to non-reasoning samples, and some of these examples
are available publicly in the Llama-Nemotron-Post-Training-Dataset.
Stage 2: Expanding Instructional Coverage, Dialogue and Safety
The second phase shifted
toward instruction following, safety alignment, and multi-turn dialogue—while continuing to sample
from Stage 1 to retain strong STEM performance. This dataset was more compact—about 10×
smaller—and offered a balanced mix of reasoning and non-reasoning samples. This helped the model
generalize across a broader range of tasks while improving control over reasoning mode switching.
5.2.2. Long-Context Training
In order to improve long-context capabilities, we do additional training on an augmented version
of our Stage 2 blend, consisting of samples up to 512k tokens each. The samples in this extended
blend are created by concatenating the original Stage 2 SFT conversations, as well as adding several
additional types of turns, with the goal of improving the long-range memory of the model. The
added turns are constructed as follows:
1. Long-range references to existing conversations. A random short conversation that appears
22

--- Page 23 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
Figure 12 | After selecting a short conversation
from the original blend, we generate multiple
turns referencing turns from that conversation.
These turns are inserted at some point later in
the extended sample.
Figure 13 | Multiple segments are generated with
a unified theme and scattered throughout the
context. Afterwards, we generate turns that that
refer to one or more of these segments which are
placed later in the sample.
earlier in the concatenated sample is selected; we then generate follow-up user queries that
explicitly references this turn sequence by topic (e.g., “In the part of our conversation where we
discussed modern authors...”). Both the referencing questions and answers are generated with
DeepSeek-R1 (DeepSeek-AI, 2025a) These reference pairs are inserted throughout conversations
in both the reasoning and non-reasoning subsets of the data blend (see Figure 12). This method
does not require relying on the generator model’s long context understanding, as we only need
the referenced conversation as context.
2. Multi-turn references In addition to turns referencing conversations from the short blend, we
also generate multiple turns with a unified topic that may reference each other. Topics for these
sequences are chosen as a combination of 3 random keywords. We then generate multiple follow-up
turns that each reference one or more of these segments, requiring the model to determine which
of these related segments is being referred to. All of these turns are then inserted randomly
thoughout the extended conversations (see Figure 13). Similarly to the previous type, this does
not require a long-context generator.
3. Document aggregation QA. A user turn embeds a long document (up to 32k tokens) drawn
from the pre-training data. The turn is followed by several questions whose answers require
integrating information scattered across the long document.
4. Common-word retrieval with distractors. To target the RULER “common-words” subtask,
we insert user turns that list 30-80k tokens comprising a list of keywords interleaved with random
distractors. The assistant is asked to return the 𝑛most frequent words. This specialised task is
used only in the non-CoT subset. It is created without the use of a language model.
We find that hybrid models can learn to operate on higher context length within just a few hundred
steps of training on these 512k-token extended blends. We evaluated this capability using the
RULER (Hsieh et al., 2024) benchmark in non-reasoning mode, with the model achieving an 83%
RULER score on 128k sequence length after this stage.
5.2.3. Reinforcement Learning with GRPO
After SFT, we applied Group Relative Policy Optimization (GRPO) in multiple phases (Shao
et al., 2024). Each phase targeted specific skills—like instruction following or tool use—by creating
task-specific datasets with automatic verifiers, followed by broader fine-tuning with a general reward
model.
23

--- Page 24 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
Instruction-Following Tuning
To strengthen instruction adherence, we sampled 16,000 prompts
from the LMSYS Chat dataset and paired them with IFEval-style instructions.
A rule-based
verifier scored outputs based on how well they satisfied each instruction, creating a reward signal
that prioritized following directions with precision. We have used TRT-LLM backend for policy
rollouts. IFEval RL experiments provided significant boost to IFEval capabilities while the rest of
the benchmarks fluctuated slightly requiring careful checkpoint selection. We have used a learning
rate of 1e−6 which showed consistent improvement in instruction following capabilities without
regressions in other model capabilities.
General Helpfulness via Reward Model
In the final RL phase, we introduced a Qwen-32B-
based reward model (scoring 92.8 on RewardBench) to improve overall response helpfulness. We
trained using GRPO and prompts from HelpSteer2 Wang et al. (2024b). This final stage led to
noticeable gains in output quality.
5.2.4. Controlled Reasoning Inference
Inference-time behavior can be customized using simple control tags in the system prompt:
• {‘reasoning’: True} triggers reasoning mode
• {‘reasoning’: False} triggers direct-answer mode
• Omitting the tag lets the model choose
Our Jinja chat template detects these control strings and modifies the assistant’s response accord-
ingly. When {‘reasoning’: True} is present, the response is prefixed with Assistant:<think>\n,
indicating the start of a reasoning trace. When {‘reasoning’: False} is found, the response is
prefixed with Assistant:<think></think>, signaling a non-reasoning response. This mechanism
resulted in near 100% control of reasoning or non-reasoning modes.
5.3. Results
5.3.1. Nemotron-H-47B-Reasoning-128K
Across benchmarks in math, coding, science, tool use, and dialogue, Nemotron-H-47B-Reasoning-
128K achieves accuracy on par with or better than Llama-Nemotron Super 49B V1.0, and outperforms
Qwen3 32B on all non-coding benchmarks. The model supports post-training quantization of all
linear layers, enabling efficient deployment with minimal accuracy loss. We also provide the quantized
checkpoint and its corresponding results to demonstrate effectiveness in practical settings.
5.3.2. Nemotron-H-8B-Reasoning-128K
Checkpoint merging
We observed that the smaller 8B model struggled on internal safety
benchmarks. To address this, we opted for checkpoint interpolation Wortsman et al. (2022), blending
in an earlier RL checkpoint aligned from a safer long-context extended checkpoint. Checkpoint
interpolation is performed by linearly interpolating model weights: (1−𝛼)*𝑤𝑚𝑜𝑑𝑒𝑙1 +𝛼*𝑤𝑚𝑜𝑑𝑒𝑙2. We
experimented with a parameter sweep over 𝛼values from 0.1 to 0.9 in increments of 0.1, and found
that values around 0.5 offered a good trade-off between reasoning capabilities and safe behavior.
Across benchmarks in AIME25, science, tool use, and instruction-following, Nemotron-H-8B-
Reasoning-128K achieves accuracy on par with or better than Llama-Nemotron Nano 8B V1.0.
The model supports post-training quantization of all linear layers, enabling efficient deployment with
24

--- Page 25 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
Benchmark
Llama-Nemotron
Super V1
Nemotron-H 47B
Reasoning
Nemotron-H 47B
Reasoning (FP8)
Qwen3
32B
AIME25
53.0
54.2
54.2
55.8
MATH500
96.6
96.2
96.8
91.4
GPQA-D
65.1
65.7
64.6
65.2
MBPP
90.2
91.8
91.9
95.5
MBPP_PLUS
75.1
79.9
79.9
81.5
LCB
41.2
50.2
53.4
64.2
BFCL
72.7
72.9
73.2
71.3
IFEVAL-Prompt
81.8
84.5
84.5
83.9
IFEVAL-Instruction
87.4
89.7
89.6
88.6
Arena Hard
85.0
85.0
80.5
93.8
Table 11 | Comparison of benchmark performance across multiple model variants. Best scores per
row are shown in bold.
Benchmark
Llama-Nemotron
Nano 8B v1.0
Nemotron-H 8B
Reasoning
Nemotron-H 8B
Reasoning (FP8)
AIME25
51.4
51.7
46.7
MATH500
94.8
94.0
94.0
GPQA-D
53.5
55.1
54.5
MBPP
84.1
86.0
86.2
MBPP_PLUS
71.4
74.1
73.3
LCB
52.6
49.5
44.8
BFCL
63.6
68.8
70.6
IFEVAL-Prompt
71.8
71.4
71.5
IFEVAL-Instruction
79.3
79.6
79.9
Table 12 | Comparison of benchmark performance across multiple 8B model variants. Best scores
per row are bolded.
minimal accuracy loss. We also provide the FP8 quantized checkpoint and its corresponding results
to demonstrate effectiveness in practical settings.
6. Conclusions
The Nemotron-H family of models demonstrates that hybrid model architectures can offer the best
of both worlds: comparable to state-of-the-art Transformer models in terms of capabilities while
offering improved inference speed. We find the Nemotron-H base models offer either better or on-par
accuracy compared to other similarly-sized state-of-the-art open-sourced Transformer models (e.g.,
Qwen-2.5-7B/72B and Llama-3.1-8B/70B), while being up to 3× faster at inference. We also find
these base models can be adapted to yield effective VLMs as well as instruction-tuned models.
Additionally, both our FP8-based training recipe and MiniPuzzle can be used to reduce the cost of
creating these models.
We have released the Nemotron-H base checkpoints described in this paper with support in Hugging
Face and NeMo to facilitate further research:
• Nemotron-H-56B-Base. Hugging Face and NGC.
• Nemotron-H-47B-Base. Hugging Face and NGC.
• Nemotron-H-8B-Base. Hugging Face and NGC.
25

--- Page 26 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
Nemotron-H Reasoning checkpoints described are also available in Hugging Face:
• Nemotron-H-47B-Reasoning. Hugging Face.
• Nemotron-H-8B-Reasoning. Hugging Face.
Contributors
We thank the following people for their invaluable contributions to Nemotron-H.
Data.
Abhinav Khattar, Aleksander Ficek, Amala Sanjay Deshmukh, Andrew Tao, Ayush
Dattagupta, Brandon Norick*, Chengyu Dong*, Dan Su*, Daria Gitman, Evelina Bakhturina,
Igor Gitman, Ilia Karmanov, Ivan Moshkov, Jane Polak Scowcroft, Jarno Seppanen, Jiaxuan You,
Jocelyn Huang, John Kamalu*, Joseph Jennings*, Jupinder Parmar*, Karan Sapra, Kateryna
Chumachenko, Kezhi Kong*, Lukas Voegtle, Lindsey Pavao, Markus Kliegl*, Matvei Novikov,
Mehrzad Samadi, Miguel Martinez, Mostofa Patwary*, Osvald Nitski, Philipp Fischer, Pritam
Gundecha, Rabeeh Karimi Mahabadi, Sean Narenthiran, Sanjeev Satheesh*, Seungju Han, Shrimai
Prabhumoye*, Shubham Pachori, Shubham Toshniwal, Siddhartha Jain, Somshubra Majumdar,
Syeda Nahida Akter*, Timo Roman, Ushnish De, Vahid Noroozi, Vitaly Kurin, Wasi Uddin Ahmad,
Wei Du, Yao Xu, Yejin Choi, Ying Lin*.
FP8 recipe. Carlo del Mundo, Dusan Stosic, Eric Chung, Jinze Xue, John Kamalu, Kirthi Sivamani,
Mike Chrzanowski*, Mohammad Shoeybi, Mostofa Patwary, Oleg Rybakov*, Paulius Micikevicius,
Peter Dykas*, Przemek Tredak, Zhongbo Zhu.
Model architecture. Brandon Norick*, Duncan Riach*, Roger Waleffe*, Wonmin Byeon*.
Pre-training. Deepak Narayanan*, Hongbin Liu, Kunlun Li, Maciej Bala, Michael Andersch,
Mikolaj Blaz, Oleg Rybakov, Peter Dykas, Roger Waleffe*, Sangkug Lym, Selvaraj Anandaraj,
Seonmyeong Bak, Slawek Kierat, Szymon Migacz, Xiaowei Ren.
Infrastructure. Aaron Blakeman, Aarti Basant, Ashwin Poojary, Brian Butterfield, Christine
Harvey, Ding Ma, Dong Ahn, Gargi Prasad, Hui Li, Jason Sewall, Jing Zhang, Jining Huang, Kumar
Anik, Maer Rodrigues de Melo, Mohamed Fawzy, Ning Xu, Pasha Shamis, Pierre-Yves Aquilanti,
Rahul Kandu, Ruoxi Zhang, Sabrina Kavanaugh, Sergey Kashirsky, Shelby Thomas, Sirshak Das,
Sriharsha Niverty, Stefania Alborghetti, Tal Shiri.
Distillation. Akhiad Bercovich*, Ali Taghibakhshi*, Daniel Korzekwa, Elad Segal*, Izik Golan*,
Marcin Chochowski*, Mostofa Patwary, Pavlo Molchanov*, Ran El-Yaniv, Raviraj Joshi, Roger
Waleffe, Saurav Muralidharan*, Sharath Turuvekere Sreenivas*, Tomer Ronen*.
VLM. Andrew Tao, Boxin Wang*, Danny Yin, Fuxiao Liu, Guilin Liu, Guo Chen, Jason Lu, Jon
Barker, Lukas Voegtle, Matthieu Le, Mike Ranzinger, Nayeon Lee*, Philipp Fischer, Song Han,
Tuomas Rintamaki, Tyler Poon, Wei Ping*, Wenliang Dai*, Zhiding Yu, Zhiqi Li, Zhuolin Yang*.
Alignment and long context. Adithya Renduchintala*, Ali Taghibakhshi, Ameya Sunil Maha-
baleshwarkar*, Bilal Kartal*, David Mosallanezhad, Dima Rekesh*, Ellie Evans, Fei Jia*, Felipe
Sores*, Gerald Shen*, Haifeng Qian*, Hoo Chang Shin, Jiaqi Zeng, Julien Veron Vialard*, Luis
Vega*, Makesh Narsimhan Sreedhar, Michael Evans, Olivier Delalleau, Prasoon Varshney, Samuel
Kriman*, Shantanu Acharya*, Soumye Singhal, Tugrul Konuk, Yian Zhang*, Yoshi Suhara, Zijia
Chen.
Inference. Helen Ngo*, Keshav Santhanam*, Vijay Korthikanti*.
Software support.
Adithya Renduchintala, Ali Taghibakhshi, Anna Shors, Ashwath Aithal,
26

--- Page 27 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
Balaram Buddharaju, Bobby Chen, Cyril Meurillon, David Mosallanezhad, Deepak Narayanan,
Dmytro Pykhtar, Duncan Riach, Ellie Evans, Fei Jia, Felipe Sores, Gerald Shen, Helen Ngo, Jared
Casper, Jimmy Zhang, Keshav Santhanam, Lawrence McAfee, Luis Vega, Michael Evans, Nima
Tajbakhsh, Olivier Delalleau, Parth Chadha, Piotr Bialecki, Roger Waleffe, Sahil Jain, Terry Kong,
Tyler Poon, Vijay Korthikanti, Yian Zhang, Yoshi Suhara, Zhiyu Li.
Evaluations and safety. Ameya Sunil Mahabaleshwarkar*, Christopher Parisien, David Mosal-
lanezhad*, Denys Fridman, Eileen Long, Erick Galinkin, Ewa Dobrowolska, Katherine Luna, Leon
Derczynski, Marta Stepniewska-Dziubinska, Michael Evans, Roger Waleffe*, Sanjeev Satheesh*,
Shaona Ghosh, Shrimai Prabhumoye, Suseella Panguluri, Syeda Nahida Akter, Varun Singh.
Program management. Joey Conway, Krzysztof Pawelec, Shyamala Prayaga, Swetha Bhendigeri,
Trisha Saar.
Leadership. Alexis Bjorlin, Andrew Tao*, Boris Ginsburg*, Bryan Catanzaro*, Eric Chung, Jan
Kautz, Jonathan Cohen*, Kari Briski, Misha Smelyanskiy, Mohammad Shoeybi*, Mostofa Patwary*,
Oleksii Kuchaiev*, Sharon Clay, Song Han, Timo Roman, Wei Ping*.
* Core contributor.
27

--- Page 28 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
References
Joshua Ainslie, James Lee-Thorp, Michiel de Jong, Yury Zemlyanskiy, Federico Lebrón, and Sumit
Sanghai. GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Check-
points, 2023. URL https://arxiv.org/abs/2305.13245.
Syeda Nahida Akter, Shrimai Prabhumoye, John Kamalu, Sanjeev Satheesh, Eric Nyberg, Mostofa
Patwary, Mohammad Shoeybi, and Bryan Catanzaro. MIND: Math Informed syNthetic Dialogues
for Pretraining LLMs, 2024. URL https://arxiv.org/abs/2410.12881.
Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana Hasson, Karel
Lenc, Arthur Mensch, Katherine Millican, Malcolm Reynolds, et al. Flamingo: A Visual Language
Model for Few-shot Learning. Advances in Neural Information Processing Systems, 35:23716–23736,
2022.
Loubna Ben Allal, Anton Lozhkov, Elie Bakouch, Gabriel Martín Blázquez, Guilherme Penedo, Lewis
Tunstall, Andrés Marafioti, Hynek Kydlíček, Agustín Piqueres Lajarín, Vaibhav Srivastav, Joshua
Lochner, Caleb Fahlgren, Xuan-Son Nguyen, Clémentine Fourrier, Ben Burtenshaw, Hugo Larcher,
Haojun Zhao, Cyril Zakka, Mathieu Morlon, Colin Raffel, Leandro von Werra, and Thomas Wolf.
SmolLM2: When Smol Goes Big – Data-Centric Training of a Small Language Model, 2025. URL
https://arxiv.org/abs/2502.02737.
Zeyuan Allen-Zhu and Yuanzhi Li. Physics of Language Models: Part 3.2, Knowledge Manipulation,
2024. URL https://arxiv.org/abs/2309.14402.
Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David Dohan,
Ellen Jiang, Carrie Cai, Michael Terry, Quoc Le, and Charles Sutton. Program Synthesis with
Large Language Models, 2021. URL https://arxiv.org/abs/2108.07732.
Iz Beltagy, Matthew E. Peters, and Arman Cohan. Longformer: The Long-Document Transformer,
2020. URL https://arxiv.org/abs/2004.05150.
Akhiad Bercovich, Tomer Ronen, Talor Abramovich, Nir Ailon, Nave Assaf, Mohammad Dabbah,
Ido Galil, Amnon Geifman, Yonatan Geifman, Izhak Golan, Netanel Haber, Ehud Karpas, Roi
Koren, Itay Levy, Pavlo Molchanov, Shahar Mor, Zach Moshe, Najeeb Nabwani, Omri Puny,
Ran Rubin, Itamar Schen, Ido Shahaf, Oren Tropp, Omer Ullman Argov, Ran Zilberstein, and
Ran El-Yaniv.
Puzzle: Distillation-Based NAS for Inference-Optimized LLMs, 2024.
URL
https://arxiv.org/abs/2411.19146.
Yonatan Bisk, Rowan Zellers, Ronan Le Bras, Jianfeng Gao, and Yejin Choi. PIQA: Reasoning about
Physical Commonsense in Natural Language, 2019. URL https://arxiv.org/abs/1911.11641.
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel
Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler,
Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott
Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya
Sutskever, and Dario Amodei. Language Models are Few-Shot Learners, 2020. URL https:
//arxiv.org/abs/2005.14165.
Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared
Kaplan, et al. Evaluating Large Language Models Trained on Code, 2021. URL https://arxiv.
org/abs/2107.03374.
28

--- Page 29 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
Zhe Chen, Weiyun Wang, Yue Cao, Yangzhou Liu, Zhangwei Gao, Erfei Cui, Jinguo Zhu, Shenglong
Ye, Hao Tian, Zhaoyang Liu, et al. Expanding Performance Boundaries of Open-Source Multimodal
Models with Model, Data, and Test-Time Scaling. arXiv preprint arXiv:2412.05271, 2024.
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and
Oyvind Tafjord. Think you have Solved Question Answering? Try ARC, the AI2 Reasoning
Challenge. ArXiv, abs/1803.05457, 2018.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser,
Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, and John
Schulman. Training Verifiers to Solve Math Word Problems, 2021. URL https://arxiv.org/
abs/2110.14168.
Wenliang Dai, Nayeon Lee, Boxin Wang, Zhuolin Yang, Zihan Liu, Jon Barker, Tuomas Rintamaki,
Mohammad Shoeybi, Bryan Catanzaro, and Wei Ping. NVLM: Open Frontier-class Multimodal
LLMs. arXiv preprint arXiv:2409.11402, 2024.
Tri Dao and Albert Gu. Transformers are SSMs: Generalized Models and Efficient Algorithms
Through Structured State Space Duality, 2024. URL https://arxiv.org/abs/2405.21060.
Gemma Team @ Google DeepMind. Gemma 3 Technical Report, 2025. URL https://arxiv.org/
abs/2503.19786.
DeepSeek-AI. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning.
arXiv preprint arXiv:2501.12948, 2025a.
DeepSeek-AI. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning,
2025b. URL https://arxiv.org/abs/2501.12948.
DeepSeek-AI. DeepSeek-V3 Technical Report, 2025c. URL https://arxiv.org/abs/2412.19437.
Haodong Duan, Junming Yang, Yuxuan Qiao, Xinyu Fang, Lin Chen, Yuan Liu, Xiaoyi Dong,
Yuhang Zang, Pan Zhang, Jiaqi Wang, et al. VLMEvalKit: An Open-Source Toolkit for Evaluating
Large Multi-Modality Models. In Proceedings of the 32nd ACM International Conference on
Multimedia, pp. 11198–11201, 2024.
Steven Feng, Shrimai Prabhumoye, Kezhi Kong, Dan Su, Mostofa Patwary, Mohammad Shoeybi, and
Bryan Catanzaro. Maximize Your Data’s Potential: Enhancing LLM Accuracy with Two-Phase
Pretraining, 2024. URL https://arxiv.org/abs/2412.15285.
Shaona Ghosh, Prasoon Varshney, Makesh Narsimhan Sreedhar, Aishwarya Padmakumar, Traian
Rebedea, Jibin Rajan Varghese, and Christopher Parisien. AEGIS2. 0: A Diverse AI Safety
Dataset and Risks Taxonomy for Alignment of LLM Guardrails. arXiv preprint arXiv:2501.09004,
2025.
Yash Goyal, Tejas Khot, Douglas Summers-Stay, Dhruv Batra, and Devi Parikh. Making the V
in VQA Matter: Elevating the Role of Image Understanding in Visual Question Answering. In
Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pp. 6904–6913,
2017.
Albert Gu and Tri Dao. Mamba: Linear-Time Sequence Modeling with Selective State Spaces, 2024.
URL https://arxiv.org/abs/2312.00752.
29

--- Page 30 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and
Jacob Steinhardt. Measuring Massive Multitask Language Understanding, 2021a. URL https:
//arxiv.org/abs/2009.03300.
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song,
and Jacob Steinhardt. Measuring Mathematical Problem Solving With the MATH Dataset, 2021b.
URL https://arxiv.org/abs/2103.03874.
Geoffrey Hinton, Oriol Vinyals, and Jeff Dean. Distilling the Knowledge in a Neural Network, 2015.
Cheng-Ping Hsieh, Simeng Sun, Samuel Kriman, Shantanu Acharya, Dima Rekesh, Fei Jia, Yang
Zhang, and Boris Ginsburg. RULER: What’s the Real Context Size of Your Long-Context
Language Models?, 2024. URL https://arxiv.org/abs/2404.06654.
Drew A Hudson and Christopher D Manning. GQA: A New Dataset for Real-World Visual Reasoning
and Compositional Question Answering. In Proceedings of the IEEE/CVF conference on computer
vision and pattern recognition, pp. 6700–6709, 2019.
Kushal Kafle, Brian Price, Scott Cohen, and Christopher Kanan. DVQA: Understanding Data
Visualizations via Question Answering. In Proceedings of the IEEE Conference on Computer
Vision and Pattern Recognition, pp. 5648–5656, 2018.
Ilia Karmanov, Amala Sanjay Deshmukh, Lukas Voegtle, Philipp Fischer, Kateryna Chumachenko,
Timo Roman, Jarno Seppänen, Jupinder Parmar, Joseph Jennings, Andrew Tao, and Karan Sapra.
Éclair – Extracting Content and Layout with Integrated Reading Order for Documents, 2025.
URL https://arxiv.org/abs/2502.04223.
Angelos Katharopoulos, Apoorv Vyas, Nikolaos Pappas, and François Fleuret. Transformers are
RNNs: Fast Autoregressive Transformers with Linear Attention, 2020. URL https://arxiv.org/
abs/2006.16236.
Aniruddha Kembhavi, Mike Salvato, Eric Kolve, Minjoon Seo, Hannaneh Hajishirzi, and Ali Farhadi.
A Diagram Is Worth A Dozen Images. In ECCV, 2016.
Vijay Korthikanti, Jared Casper, Sangkug Lym, Lawrence McAfee, Michael Andersch, Mohammad
Shoeybi, and Bryan Catanzaro. Reducing Activation Recomputation in Large Transformer Models,
2022. URL https://arxiv.org/abs/2205.05198.
Ranjay Krishna, Yuke Zhu, Oliver Groth, Justin Johnson, Kenji Hata, Joshua Kravitz, Stephanie
Chen, Yannis Kalantidis, Li-Jia Li, David A Shamma, et al. Visual Genome: Connecting Language
and Vision Using Crowdsourced Dense Image Annotations. International Journal of Computer
Vision, 123:32–73, 2017.
Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E.
Gonzalez, Hao Zhang, and Ion Stoica. Efficient Memory Management for Large Language Model
Serving with PagedAttention, 2023. URL https://arxiv.org/abs/2309.06180.
Jeffrey Li, Alex Fang, Georgios Smyrnis, Maor Ivgi, Matt Jordan, Samir Yitzhak Gadre, Hritik
Bansal, Etash Guha, Sedrick Scott Keh, Kushal Arora, et al. DataComp-LM: In Search of the Next
Generation of Training Sets for Language Models. Advances in Neural Information Processing
Systems, 37:14200–14282, 2024.
Junnan Li, Dongxu Li, Caiming Xiong, and Steven Hoi. BLIP: Bootstrapping Language-Image Pre-
training for Unified Vision-Language Understanding and Generation. In International Conference
on Machine Learning, pp. 12888–12900. PMLR, 2022.
30

--- Page 31 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
Zhiqi Li, Guo Chen, Shilong Liu, Shihao Wang, Vibashan VS, Yishen Ji, Shiyi Lan, Hao Zhang,
Yilin Zhao, Subhashree Radhakrishnan, et al. Eagle 2: Building Post-Training Data Strategies
from Scratch for Frontier Vision-Language Models. arXiv preprint arXiv:2501.14818, 2025.
Opher Lieber, Barak Lenz, Hofit Bata, Gal Cohen, Jhonathan Osin, Itay Dalmedigos, Erez Safahi,
Shaked Meirom, Yonatan Belinkov, Shai Shalev-Shwartz, Omri Abend, Raz Alon, Tomer Asida,
Amir Bergman, Roman Glozman, Michael Gokhman, Avashalom Manevich, Nir Ratner, Noam
Rozen, Erez Shwartz, Mor Zusman, and Yoav Shoham. Jamba: A Hybrid Transformer-Mamba
Language Model, 2024. URL https://arxiv.org/abs/2403.19887.
Tsung-Yi Lin, Michael Maire, Serge Belongie, Lubomir Bourdev, Ross Girshick, James Hays, Pietro
Perona, Deva Ramanan, C. Lawrence Zitnick, and Piotr Dollár. Microsoft COCO: Common
Objects in Context, 2015. URL https://arxiv.org/abs/1405.0312.
Adam Dahlgren Lindström and Savitha Sam Abraham. CLEVR-Math: A Dataset for Compositional
Language, Visual and Mathematical Reasoning. arXiv preprint arXiv:2208.05358, 2022.
Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual Instruction Tuning. Advances
in Neural Information Processing Systems, 36:34892–34916, 2023a.
Jiawei Liu, Chunqiu Steven Xia, Yuyao Wang, and Lingming Zhang. Is Your Code Generated by
ChatGPT Really Correct? Rigorous Evaluation of Large Language Models for Code Generation.
arXiv preprint arXiv:2305.01210, 2023b. doi: https://doi.org/10.48550/arXiv.2305.01210. URL
https://arxiv.org/abs/2305.01210.
Yuliang Liu, Zhang Li, Mingxin Huang, Biao Yang, Wenwen Yu, Chunyuan Li, Xucheng Yin, Cheng
lin Liu, Lianwen Jin, and Xiang Bai. OCRBench: On the Hidden Mystery of OCR in Large
Multimodal Models, 2024. URL https://arxiv.org/abs/2305.07895.
Pan Lu, Swaroop Mishra, Tanglin Xia, Liang Qiu, Kai-Wei Chang, Song-Chun Zhu, Oyvind Tafjord,
Peter Clark, and Ashwin Kalyan. Learn to Explain: Multimodal Reasoning via Thought Chains for
Science Question Answering. Advances in Neural Information Processing Systems, 35:2507–2521,
2022.
Pan Lu, Hritik Bansal, Tony Xia, Jiacheng Liu, Chunyuan Li, Hannaneh Hajishirzi, Hao Cheng,
Kai-Wei Chang, Michel Galley, and Jianfeng Gao. MathVista: Evaluating Mathematical Reasoning
of Foundation Models in Visual Contexts. In International Conference on Learning Representations
(ICLR), 2024.
Pratyush Maini, Skyler Seto, He Bai, David Grangier, Yizhe Zhang, and Navdeep Jaitly. Rephrasing
the Web: A Recipe for Compute and Data-Efficient Language Modeling. In ICLR 2024 Workshop
on Navigating and Addressing Data Problems for Foundation Models, 2024.
Somshubra Majumdar, Vahid Noroozi, Sean Narenthiran, Aleksander Ficek, Jagadeesh Balam, and
Boris Ginsburg. Genetic Instruct: Scaling up Synthetic Generation of Coding Instructions for
Large Language Models. 2024. URL https://arxiv.org/abs/2407.21077.
Andres Marafioti and Hugo Laurencon. Docmatix - A Huge Dataset for Document Visual Question
Answering, 2024.
Kenneth Marino, Mohammad Rastegari, Ali Farhadi, and Roozbeh Mottaghi. OK-VQA: A Visual
Question Answering Benchmark Requiring External Knowledge. In Proceedings of the IEEE/cvf
conference on computer vision and pattern recognition, pp. 3195–3204, 2019.
31

--- Page 32 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
Ahmed Masry, Do Xuan Long, Jia Qing Tan, Shafiq Joty, and Enamul Hoque.
ChartQA: A
Benchmark for Question Answering about Charts with Visual and Logical Reasoning. arXiv
preprint arXiv:2203.10244, 2022.
Minesh Mathew, Dimosthenis Karatzas, and CV Jawahar.
DocVQA: A Dataset for VQA on
Document Images. In Proceedings of the IEEE/CVF Winter Conference on Applications of
Computer Vision, pp. 2200–2209, 2021.
Llama Team @ Meta. The Llama 3 Herd of Models, 2024. URL https://arxiv.org/abs/2407.
21783.
Paulius Micikevicius, Dusan Stosic, Neil Burgess, Marius Cornea, Pradeep Dubey, Richard Grisenth-
waite, Sangwon Ha, Alexander Heinecke, Patrick Judd, John Kamalu, Naveen Mellempudi, Stuart
Oberman, Mohammad Shoeybi, Michael Siu, and Hao Wu. FP8 Formats for Deep Learning, 2022.
URL https://arxiv.org/abs/2209.05433.
Todor Mihaylov, Peter Clark, Tushar Khot, and Ashish Sabharwal. Can a Suit of Armor Conduct
Electricity? A New Dataset for Open Book Question Answering, 2018. URL https://arxiv.
org/abs/1809.02789.
Anand Mishra, Shashank Shekhar, Ajeet Kumar Singh, and Anirban Chakraborty. OCR-VQA:
Visual Question Answering by Reading Text in Images. In 2019 International Conference on
Document Analysis and Recognition (ICDAR), pp. 947–952. IEEE, 2019.
Niklas Muennighoff, Alexander Rush, Boaz Barak, Teven Le Scao, Nouamane Tazi, Aleksandra
Piktus, Sampo Pyysalo, Thomas Wolf, and Colin A Raffel. Scaling Data-Constrained Language
Models. Advances in Neural Information Processing Systems, 36, 2024.
Saurav Muralidharan, Sharath Turuvekere Sreenivas, Raviraj Joshi, Marcin Chochowski, Mostofa
Patwary, Mohammad Shoeybi, Bryan Catanzaro, Jan Kautz, and Pavlo Molchanov. Compact
Language Models via Pruning and Knowledge Distillation, 2024. URL https://arxiv.org/abs/
2407.14679.
NVIDIA. Nemotron-4 340B Technical Report, 2024. URL https://arxiv.org/abs/2406.11704.
NVIDIA, Alisson Azzolini, Hannah Brandon, Prithvijit Chattopadhyay, Huayu Chen, Jinju Chu, Yin
Cui, Jenna Diamond, Yifan Ding, Francesco Ferroni, Rama Govindaraju, Jinwei Gu, Siddharth
Gururani, Imad El Hanafi, Zekun Hao, Jacob Huffman, Jingyi Jin, Brendan Johnson, Rizwan
Khan, George Kurian, Elena Lantz, Nayeon Lee, Zhaoshuo Li, Xuan Li, Tsung-Yi Lin, Yen-
Chen Lin, Ming-Yu Liu, Andrew Mathau, Yun Ni, Lindsey Pavao, Wei Ping, David W. Romero,
Misha Smelyanskiy, Shuran Song, Lyne Tchapmi, Andrew Z. Wang, Boxin Wang, Haoxiang
Wang, Fangyin Wei, Jiashu Xu, Yao Xu, Xiaodong Yang, Zhuolin Yang, Xiaohui Zeng, and Zhe
Zhang. Cosmos-Reason1: From Physical Common Sense To Embodied Reasoning, 2025. URL
https://arxiv.org/abs/2503.15558.
OpenAI.
Learning
to
Reason
with
LLMs,
2025.
URL
https://openai.com/index/
learning-to-reason-with-llms/.
Vicente Ordonez, Girish Kulkarni, and Tamara Berg. Im2text: Describing Images using 1 Million
Captioned Photographs. Advances in Neural Information Processing Systems, 24, 2011.
Jupinder Parmar, Shrimai Prabhumoye, Joseph Jennings, Mostofa Patwary, Sandeep Subramanian,
Dan Su, Chen Zhu, Deepak Narayanan, Aastha Jhunjhunwala, Ayush Dattagupta, Vibhu Jawa,
Jiwei Liu, Ameya Mahabaleshwarkar, Osvald Nitski, Annika Brundyn, James Maki, Miguel
32

--- Page 33 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
Martinez, Jiaxuan You, John Kamalu, Patrick LeGresley, Denys Fridman, Jared Casper, Ashwath
Aithal, Oleksii Kuchaiev, Mohammad Shoeybi, Jonathan Cohen, and Bryan Catanzaro. Nemotron-
4 15B Technical Report. arXiv preprint arXiv:2402.16819, 2024. URL https://arxiv.org/abs/
2402.16819.
Keiran Paster, Marco Dos Santos, Zhangir Azerbayev, and Jimmy Ba. OpenWebMath: An Open
Dataset of High-Quality Mathematical Web Text, 2023.
Guilherme Penedo, Hynek Kydlíček, Anton Lozhkov, Margaret Mitchell, Colin A Raffel, Leandro
Von Werra, Thomas Wolf, et al. The FineWeb datasets: Decanting the Web for the Finest Text
Data at Scale. Advances in Neural Information Processing Systems, 37:30811–30849, 2024.
Qwen. Qwen2.5 Technical Report, 2025. URL https://arxiv.org/abs/2412.15115.
Samyam Rajbhandari, Jeff Rasley, Olatunji Ruwase, and Yuxiong He. ZeRO: Memory Optimizations
Toward Training Trillion Parameter Models, 2020. URL https://arxiv.org/abs/1910.02054.
Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavatula, and Yejin Choi. WinoGrande: An
Adversarial Winograd Schema Challenge at Scale, 2019. URL https://arxiv.org/abs/1907.
10641.
Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan
Zhang, YK Li, Y Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open
language models. arXiv preprint arXiv:2402.03300, 2024.
Piyush Sharma, Nan Ding, Sebastian Goodman, and Radu Soricut. Conceptual Captions: A Cleaned,
Hypernymed, Image Alt-text Dataset for Automatic Image Captioning. In Proceedings of the 56th
Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp.
2556–2565, 2018.
Mohammad Shoeybi, Mostofa Patwary, Raul Puri, Patrick LeGresley, Jared Casper, and Bryan
Catanzaro. Megatron-LM: Training Multi-Billion Parameter Language Models Using Model
Parallelism, 2020. URL https://arxiv.org/abs/1909.08053.
Amanpreet Singh, Vivek Natarajan, Meet Shah, Yu Jiang, Xinlei Chen, Dhruv Batra, Devi Parikh,
and Marcus Rohrbach. Towards VQA Models That Can Read. In Proceedings of the IEEE/CVF
conference on computer vision and pattern recognition, pp. 8317–8326, 2019.
David R. So, Wojciech Mańke, Hanxiao Liu, Zihang Dai, Noam Shazeer, and Quoc V. Le. Primer:
Searching for Efficient Transformers for Language Modeling, 2022. URL https://arxiv.org/
abs/2109.08668.
Sharath Turuvekere Sreenivas, Saurav Muralidharan, Raviraj Joshi, Marcin Chochowski, Ameya Sunil
Mahabaleshwarkar, Gerald Shen, Jiaqi Zeng, Zijia Chen, Yoshi Suhara, Shizhe Diao, Chenhan
Yu, Wei-Chun Chen, Hayley Ross, Oluwatobi Olabiyi, Ashwath Aithal, Oleksii Kuchaiev, Daniel
Korzekwa, Pavlo Molchanov, Mostofa Patwary, Mohammad Shoeybi, Jan Kautz, and Bryan
Catanzaro. LLM Pruning and Distillation in Practice: The Minitron Approach, 2024. URL
https://arxiv.org/abs/2408.11796.
Dan Su, Kezhi Kong, Ying Lin, Joseph Jennings, Brandon Norick, Markus Kliegl, Mostofa Patwary,
Mohammad Shoeybi, and Bryan Catanzaro. Nemotron-CC: Transforming Common Crawl into a
Refined Long-Horizon Pretraining Dataset, 2024. URL https://arxiv.org/abs/2412.02595.
Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, and Yunfeng Liu. RoFormer: Enhanced
Transformer with Rotary Position Embedding, 2023. URL https://arxiv.org/abs/2104.09864.
33

--- Page 34 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
Shengyang Sun, Yian Zhang, Alexander Bukharin, David Mosallanezhad, Jiaqi Zeng, Soumye
Singhal, Gerald Shen, Adithya Renduchintala, Tugrul Konuk, Yi Dong, Zhilin Wang, Dmitry
Chichkov, Olivier Delalleau, and Oleksii Kuchaiev. Reward-aware Preference Optimization: A
Unified Mathematical Framework for Model Alignment, 2025. URL https://arxiv.org/abs/
2502.00203.
Shubham Toshniwal, Wei Du, Ivan Moshkov, Branislav Kisacanin, Alexan Ayrapetyan, and Igor
Gitman. OpenMathInstruct-2: Accelerating AI for Math with Massive Open-Source Instruction
Data. arXiv preprint arXiv:2410.01560, 2024.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz
Kaiser, and Illia Polosukhin. Attention Is All You Need, 2023. URL https://arxiv.org/abs/
1706.03762.
Andreas Veit, Tomas Matera, Lukas Neumann, Jiri Matas, and Serge Belongie.
COCO-Text:
Dataset and Benchmark for Text Detection and Recognition in Natural Images. 2016. URL
https://arxiv.org/abs/1601.07140.
Roger Waleffe, Wonmin Byeon, Duncan Riach, Brandon Norick, Vijay Korthikanti, Tri Dao, Albert
Gu, Ali Hatamizadeh, Sudhakar Singh, Deepak Narayanan, Garvit Kulshreshtha, Vartika Singh,
Jared Casper, Jan Kautz, Mohammad Shoeybi, and Bryan Catanzaro. An Empirical Study of
Mamba-based Language Models, 2024. URL https://arxiv.org/abs/2406.07887.
Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni, Abhranil Chandra, Shiguang Guo, Weiming
Ren, Aaran Arulraj, Xuan He, Ziyan Jiang, Tianle Li, Max Ku, Kai Wang, Alex Zhuang, Rongqi
Fan, Xiang Yue, and Wenhu Chen. MMLU-Pro: A More Robust and Challenging Multi-Task
Language Understanding Benchmark, 2024a. URL https://arxiv.org/abs/2406.01574.
Zhilin Wang, Yi Dong, Olivier Delalleau, Jiaqi Zeng, Gerald Shen, Daniel Egert, Jimmy J. Zhang,
Makesh Narsimhan Sreedhar, and Oleksii Kuchaiev. Helpsteer2: Open-source dataset for training
top-performing reward models. arXiv preprint arXiv:2406.08673, 2024b. doi: 10.48550/arXiv.
2406.08673.
Mitchell Wortsman, Gabriel Ilharco, Samir Yitzhak Gadre, Rebecca Roelofs, Raphael Gontijo-Lopes,
Ari S. Morcos, Hongseok Namkoong, Ali Farhadi, Yair Carmon, Simon Kornblith, and Ludwig
Schmidt. Model soups: averaging weights of multiple fine-tuned models improves accuracy without
increasing inference time, 2022. URL https://arxiv.org/abs/2203.05482.
xAI. Grok-1.5 Vision Preview: Connecting the Digital and Physical Worlds with our First Multimodal
Model, 2024.
Xiang Yue, Yuansheng Ni, Kai Zhang, Tianyu Zheng, Ruoqi Liu, Ge Zhang, Samuel Stevens, Dongfu
Jiang, Weiming Ren, Yuxuan Sun, Cong Wei, Botao Yu, Ruibin Yuan, Renliang Sun, Ming Yin,
Boyuan Zheng, Zhenzhu Yang, Yibo Liu, Wenhao Huang, Huan Sun, Yu Su, and Wenhu Chen.
MMMU: A Massive Multi-discipline Multimodal Understanding and Reasoning Benchmark for
Expert AGI. In Proceedings of CVPR, 2024.
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi. HellaSwag: Can a Machine
Really Finish Your Sentence?, 2019. URL https://arxiv.org/abs/1905.07830.
Biao Zhang and Rico Sennrich.
Root Mean Square Layer Normalization, 2019.
URL https:
//arxiv.org/abs/1910.07467.
34

--- Page 35 ---

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models
Jeffrey Zhou, Tianjian Lu, Swaroop Mishra, Siddhartha Brahma, Sujoy Basu, Yi Luan, Denny
Zhou, and Le Hou. Instruction-following Evaluation for Large Language Models. arXiv preprint
arXiv:2311.07911, 2023.
35

```
