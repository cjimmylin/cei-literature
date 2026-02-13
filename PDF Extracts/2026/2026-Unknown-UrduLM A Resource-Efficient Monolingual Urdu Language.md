---
title: "2026-Unknown-UrduLM A Resource-Efficient Monolingual Urdu Language - PDF Extract"
source_pdf: "2026-Unknown-UrduLM A Resource-Efficient Monolingual Urdu Language.pdf"
pages: 12
extracted_at: "2026-02-13T09:15:46.133182"
---

# PDF Extract: 2026-Unknown-UrduLM A Resource-Efficient Monolingual Urdu Language

**Source PDF:** 2026-Unknown-UrduLM A Resource-Efficient Monolingual Urdu Language.pdf
**Total Pages:** 12

---

## Content

```
--- Page 1 ---

UrduLM: A Resource-Efficient Monolingual Urdu Language Model
Syed Muhammad Ali Naqvi∗
Hammad Sajid∗
Zainab Haider∗
Ali Muhammad Asad∗
Department of Computer Science
Habib University
{sn07590,hs07606,zh07104,aa07190}@st.habib.edu
Haya Fatima∗
Department of Computer Science
Habib University
sf07503@st.habib.edu
Abdul Samad
Department of Computer Science
Habib University
abdul.samad@habib.edu.pk
Abstract
Urdu, spoken by 230 million people world-
wide, lacks dedicated transformer-based lan-
guage models and curated corpora.
While
multilingual models provide limited Urdu sup-
port, they suffer from poor performance, high
computational costs, and cultural inaccura-
cies due to insufficient training data. To ad-
dress these challenges, we present UrduLM, a
pretrained Urdu monolingual language model
trained in low-resource settings. We curate a
33GB Urdu corpus from diverse sources, de-
velop a custom BPE tokenizer that reduces to-
kenization overhead by atleast 20–30% com-
pared to multilingual alternatives, and pretrain
a 100M-parameter decoder-only model.
In
few-shot evaluations, UrduLM achieves com-
petitive performance with multilingual mod-
els up to 30× its size, reaching 66.6% accu-
racy on sentiment classification and BLEU
scores exceeding 30 on grammar correction
tasks. The complete methodology—including
corpus, tokenizer, model weights, and evalu-
ation benchmarks—is released openly to es-
tablish a baseline for Urdu NLP research and
provide a scalable framework for other under-
represented languages.
1
Introduction
Contemporary language models remain English-
centric (LLaMA-2: 89.70% English (Wendler et al.,
2024)), causing hallucinations and code-switching
for low-resource languages (Chang et al., 2024).
The “curse of multilinguality” degrades perfor-
mance as models support hundreds of languages,
resulting in suboptimal tokenization and diluted
linguistic knowledge (Zhao et al., 2024).
Urdu – being the 10th most spoken (Ghafoor
et al., 2021) with 230M speakers worlwide – ex-
emplifies these challenges. Despite widespread
use, Urdu lacks dedicated transformer-based gen-
erative models, curated corpora, and standard-
ized benchmarks.
The hundreds-of-billions pa-
rameter scale of multilingual models renders them
prohibitively expensive for low-resource regions
like Pakistan (Bender et al., 2021), while their
proprietary nature imposes data sovereignty risks.
Unlike other languages with successful monolin-
gual models (CroissantLLM (Faysse et al., 2024),
VBART (Turker et al., 2024), PersianMind (Ros-
tami et al., 2024)), no comparable monolingual
pretrained model exists for Urdu.
We introduce a systematic methodology for
developing efficient monolingual LLMs in low-
resource settings. Using Urdu as a case study, we
demonstrate that a well-designed 100M-parameter
model achieves competitive performance with mul-
tilingual models 30× larger (66.6% sentiment accu-
racy, 30.59 BLEU on grammar correction), while
requiring lower training cost and ∼32kg CO2. Our
complete pipeline—corpus curation, tokenizer de-
velopment, training, and evaluation—provides a
reproducible framework for other underrepresented
languages.
Contributions:
(1) 33GB curated Urdu cor-
pus (∼5–6B tokens) with systematic multi-source
pipeline; (2) Custom BPE tokenizer achieving 20–
30% lower fertility vs GPT-4’s o200k_base; (3)
100M-parameter baseline trained for <$100, com-
petitive with 3B multilingual models; (4) New
benchmark datasets and dual evaluation framework
(LLM-as-a-Judge + few-shot).
2
Related Work
NLP has evolved from statistical models (HMMs,
CRFs,
SVMs (Khan et al., 2016)) through
neural embeddings (Word2Vec (Mikolov et al.,
2013), GloVe (Pennington et al., 2014)) and
RNNs/LSTMs (Hochreiter and Schmidhuber,
1997) to transformer architectures (Vaswani et al.,
2017). Models like BERT (Devlin et al., 2019),
GPT-3 (Brown et al., 2020), and T5 (Raffel et al.,
2020) established foundation models—large-scale,
arXiv:2601.17664v1  [cs.CL]  25 Jan 2026

--- Page 2 ---

self-supervised models adaptable to diverse tasks.
However, most are developed primarily for English.
Urdu (230M speakers (Ghafoor et al., 2021))
remains severely underrepresented. Multilingual
LLMs like LLaMA-2 (89.70% English (Wendler
et al., 2024)) exhibit diminished Urdu performance.
Multilingual workflows often pivot to English
for reasoning (Zhao et al., 2024), losing linguis-
tic nuance.
The “curse of multilinguality” de-
grades both high- and low-resource language per-
formance, whereas monolingual models achieve
better results (Chang et al., 2024). While parameter-
efficient methods (LoRA (Khade et al., 2024)) offer
partial mitigation, they don’t address inherent mul-
tilingual architectural biases.
Recent monolingual LLMs demonstrate strong
performance: CroissantLLM (Faysse et al., 2024)
(French-English, 1.3B) achieved 87% factual accu-
racy with custom bilingual tokenizer and 3T bal-
anced tokens. VBART (Turker et al., 2024) (Turk-
ish, 387M-740M) reduced tokenization overhead
96% with custom SentencePiece tokenizer, setting
SOTA on Turkish benchmarks. PersianMind (Ros-
tami et al., 2024) shows similar benefits for Persian.
These results suggest dedicated Urdu LLMs could
yield comparable improvements.
Tokenization is critical for morphologically rich
languages (Jurafsky and Martin, 2008). Standard
methods (BPE, SentencePiece (Sennrich et al.,
2016; Kudo and Richardson, 2018)) optimized for
English exhibit high fertility and poor semantic
splits for Urdu (Rust et al., 2021). Custom tokeniz-
ers trained on monolingual corpora significantly im-
prove efficiency (Faysse et al., 2024; Turker et al.,
2024; Rostami et al., 2024), yet Urdu-specific tok-
enization research remains lacking.
Low-resource LLM methodologies require ad-
dressing data scarcity, tokenization inefficiency,
and evaluation challenges. Key findings: (1) Mono-
lingual models with <1B tokens can outperform
larger multilingual models when avoiding cross-
linguistic interference (Chang et al., 2024); (2)
Data augmentation via parallel corpora and back-
translation aids low-resource scenarios (Ghafoor
et al., 2021), though at high computational cost;
(3) Vocabulary extension with continued pretrain-
ing improves multilingual models (Rust et al.,
2021), but dedicated tokenizers avoid dilution en-
tirely; (4) Combining automated metrics with LLM-
based judgments provides robust evaluation for
low-resource languages (Chang et al., 2024). Our
work synthesizes these insights into a complete
Urdu pipeline, transferable to other underrepre-
sented languages.
3
Model Architecture
We adopt a decoder-only transformer (GPT-3
style (Brown et al., 2020)) with stacked decoder
blocks, multi-head self-attention, layer normaliza-
tion, and feed-forward networks, enabling capture
of long-range dependencies and contextual relation-
ships.
Training leverages PyTorch’s Distributed Data
Parallel (DDP) and Fully-Sharded Data Parallel
(FSDP) for hybrid parallelism on 4× NVIDIA
V100 GPUs (32GB each). For the 100M model,
DDP distributes model replicas across GPUs with
gradient accumulation to simulate 0.5M token
batches. Decoder-only architecture was chosen
because it naturally supports generative tasks (chat-
bots, creative writing), requires less memory per
parameter than encoder-decoder variants, and ben-
efits from extensive GPT-series prior work provid-
ing validated hyperparameters for low-resource set-
tings.
4
Urdu Tokenizer Development and
Evaluation
Multilingual tokenizers exhibit poor Urdu effi-
ciency, requiring 2–3× more tokens per word due
to: (1) vocabulary dominated by high-resource lan-
guages, leaving few Urdu subword units; (2) Latin-
optimized regex patterns failing on Perso-Arabic
script; and (3) morphological richness causing ex-
cessive fragmentation.
We developed a custom BPE tokenizer with
Urdu-specific regex patterns and three design prin-
ciples: (1) Script-Aware Segmentation: handling
Urdu characters, Urdu numerals, and punctua-
tion; (2) Optimal Vocabulary Size: exploring 10k,
20k, 32k to balance efficiency and coverage; (3)
Morphological Alignment: training exclusively on
Urdu text to capture language-specific patterns.
Training Process: We adapted OpenAI’s GPT-
4 regex rules for Urdu Unicode ranges (U+0600–
U+06FF), applied BPE merge operations for each
vocabulary size, and evaluated using fertility (to-
kens/word), tokenization speed, and vocabulary
coverage metrics.
Figure 1 shows our tokenizers consistently pro-
duce 20–30% fewer tokens than o200k_base. The
32k variant achieved best results: low fertility (com-
parable to 30k), broader vocabulary coverage re-

--- Page 3 ---

ducing out-of-vocabulary issues, and reasonable
embedding size (32k × 768 = 24.6M parameters).
Accordingly, we adopted the 32k tokenizer for our
final model.
Figure 1: Tokenizer efficiency comparison: Our custom
tokenizers produce 20–30% fewer tokens than GPT-4
o200k_base across all vocabulary sizes.
Tokenizer
Fertility
Avg Token Count
o200k_base
1.566
783
UrduLM-10k
1.206
603
UrduLM-32k
1.11
555
Table 1: Fertility, Average Token Count, and Speed for
o200k_base, and our UrduLM tokenizers (500 word
paragraph)
5
Methodology: Data Curation and
Pre-Training
5.1
Pre-Training Dataset
We construct a large-scale Urdu pre-training dataset
entirely from scratch, addressing the scarcity of
publicly available resources for this low-resource
language. Our pipeline (illustrated in Figure 2) ag-
gregates text from diverse domains including news,
literature, education, and informal conversations,
resulting in 33 GB of cleaned, high-quality Urdu
text. This dataset, to our knowledge one of the
largest curated for Urdu, provides a robust foun-
dation for pre-training UrduLM and advancing re-
search in Urdu language modeling.
5.1.1
Data Collection
To capture the richness and real-world usage
of Urdu, we aggregate text from diverse, high-
coverage sources spanning multiple domains. Our
objective is to balance formal and informal reg-
isters while maximizing linguistic diversity. The
dataset draws from four primary categories:
• Existing Resources: Publicly available Urdu
datasets, including UrduHack (Ali and Con-
tributors, 2020) and open-source corpora such
Figure 2: Overview of the data collection and prepro-
cessing pipeline for the UrduLM pre-training dataset.
as FineWeb2 (Penedo et al., 2024b), are incor-
porated as an initial seed for the collection.
• Web Scraping: Large-scale web crawling ex-
tracts Urdu content from blogs, forums, news
sites, poetry platforms, and Urdu Wikipedia.
Domain balancing is applied to prevent over-
representation of any single source.
• OCR of Books:
To enrich literary con-
tent, scanned Urdu books are digitized using
the Google Cloud Vision Optical Character
Recognition (OCR) API, followed by man-
ual verification and post-processing to correct
extraction errors. The API is a proprietary ser-
vice used under the Google Cloud Terms of
Service. No copyrighted or personal content
is redistributed.
• Translated Content: Selected portions of
the English FineWeb (Penedo et al., 2024a)
dataset are translated into Urdu using the
Google Cloud Translation API, injecting struc-
tured educational content often missing from
naturally occurring Urdu data. The Transla-
tion API is a proprietary service used under
the Google Cloud Terms of Service, and out-
puts are used solely for research purposes.

--- Page 4 ---

This multi-source strategy yields a broadly rep-
resentative corpus, blending formal news text, liter-
ary books, informal online conversations, and edu-
cational material. The collected raw data forms the
basis for subsequent cleaning, normalization, and
deduplication. All collected and processed data are
intended solely for research and educational use,
consistent with the licenses and access conditions
of their original sources.
5.1.2
Cleaning
To prepare the collected corpus for downstream
tasks, we developed a robust preprocessing pipeline
tailored to the linguistic complexities of Urdu. In-
spired by established frameworks such as Pars-
BERT (Farahani et al., 2021), the cleaning pro-
cess combined regex-based noise removal with
language-specific normalization techniques to pro-
duce a standardized and high-quality dataset.
Key components of the pipeline include:
• Regex-Based Noise Removal: Custom regu-
lar expressions removed non-linguistic con-
tent such as URLs, emails, phone num-
bers, stray digits, Latin script characters,
and extraneous symbols. An optional flag
(remove_english) allowed conditional re-
moval of embedded English text.
• Digit Conversion: All English numerals (0–
9) were mapped to their Urdu counterparts
to maintain script consistency throughout the
dataset.
• Character Normalization: We used an aug-
mented character mapping (based on Ur-
duHack’s (Ali and Contributors, 2020) cor-
rection dictionary) to normalize commonly
confused or erroneous Urdu characters, align-
ing with ParsBERT-style normalization prac-
tices (Farahani et al., 2021).
• Word Spacing Correction: Incorrectly con-
catenated or misjoined words were segmented
using UrduHack’s (Ali and Contributors,
2020) word-space mapping, ensuring ortho-
graphic accuracy and proper word boundaries.
• Unicode and Symbol Cleanup: Additional
post-processing included collapsing multiple
whitespaces, removing invisible Unicode char-
acters (\u00A0, \u200B), eliminating redun-
dant punctuation (e.g., repeated Urdu question
marks), and discarding empty parentheses.
This systematic pipeline produced clean and lin-
guistically sound Urdu text, optimized for subse-
quent deduplication and tokenization steps.
5.1.3
Deduplication
To ensure dataset quality and integrity, we apply
a rigorous deduplication process aimed at remov-
ing redundant content both within and across data
sources. Redundancy not only inflates dataset size
but can bias language models during pretraining,
reducing generalization and efficiency.
Our deduplication pipeline involves three key
stages:
• Near-Duplicate Detection via LSH: We
adopt a scalable MinHash-based Locality Sen-
sitive Hashing (LSH) approach to identify
near-duplicate text segments. Each document
is encoded into a hash signature, and LSH
bucketing is applied to group similar docu-
ments for comparison.
• Duplicate Removal:
Within each LSH
bucket, exact duplicate entries are removed. In
cases of high similarity (>90% Jaccard simi-
larity), only the most representative document
is retained to preserve diversity while elimi-
nating redundancy.
• Manual Validation: Following automated
deduplication, a manual pass is conducted to
ensure the dataset is free from residual du-
plicates or inconsistencies. This final step
guarantees the retention of only unique and
high-quality text instances.
This deduplication framework significantly re-
duces noise, improves storage efficiency, and en-
hances the reliability of the dataset for downstream
tasks such as model pretraining and evaluation.
5.1.4
Dataset Formatting and Final Statistics
The processed corpus is stored in a structured CSV
format with three columns: data (extracted text),
source (origin, e.g., specific news or book site),
and category (semantic domain such as news,
blogs, books). During pretraining, samples are
separated by explicit End-of-Text (EOT) tokens, al-
lowing the model to learn document boundaries and
handle heterogeneous text segments effectively.
Following the pipeline, the final dataset com-
prises 33 GB of high-quality Urdu text, total-
ing approximately 13 million rows and an es-
timated 5–6 billion tokens.
As this corpus is

--- Page 5 ---

34.2%
24.5%
16.7%
10%
8.8%
3.9%
1.8%
CC Dump 1 (11.3 GB)
CC Dump 2 (8.1 GB)
Translation Data (5.5 GB)
News Websites (3.3 GB)
Existing Datasets (2.9 GB)
Books (1.3 GB)
Blog Sites (0.6 GB)
Figure 3: Distribution of data sources in the UrduLM
pretraining dataset.
used exclusively for unsupervised pretraining, no
train/validation/test splits are defined. This broad
coverage across domains and writing styles ensures
a rich training signal for UrduLM. The distribution
of sources is illustrated in Figure 3. A preview of
the dataset has been made available to the public,
and can be viewed here.
Licensing
and
Usage
The
FineWeb2
dataset
(Penedo
et
al.,
2024b)
is
released
under the Open Data Commons Attribution
License (ODC-By v1.0) and its associated pro-
cessing code under the Apache 2.0 license. The
UrduHack (Ali and Contributors, 2020) toolkit,
used for text normalization, includes components
licensed under MIT (e.g., the urdu-characters
submodule). All data usage aligns with the original
terms of use and is limited strictly to research
purposes.
5.2
Model Pre-training Configuration
UrduLM-100M is a compact 100 million parame-
ter base model designed for low-resource environ-
ments. To explore the impact of vocabulary size
on model performance, we trained three variants
of the 100M model using tokenizers with vocabu-
lary sizes of 10k, 20k, and 32k tokens, respectively.
This allowed us to analyze how different tokenizer
configurations affect model loss and performance.
Among these, the model utilizing the 32k vocabu-
lary tokenizer demonstrated the best overall results,
which are discussed in Section 6.
Detailed configurations and training setups for
each variant are summarized in Table 2.
Here
nparams is the total number of trainable parameters,
nlayers is the total number of layers, dmodel is the
number of units in each bottleneck layer, dhead is
the dimension of each attention head, nctx is the
context length of the model, and Vocab Size is the
number of rows of the embedding table.
5.3
Training Details
Due to our compute limitations, we directly adopt
hyperparameters from GPT-3 (Brown et al., 2020)
considering its relevance to our case. We use Adam
optimizer with β1 = 0.9, β2 = 0.95, and ϵ = 10−8.
We clip the global norm of the gradient at 1.0, and
we use cosine decay for learning rate down to 10%
of its value over the training duration. There is a
linear LR warmup over the first 171 million tokens
(approximately 2% of total training tokens).
We trained all models with full floating point
precision (fp32) rather than bfloat16 or mixed pre-
cision due to hardware architecture limitations of
our GPU resources (NVIDIA V100 lacks efficient
bfloat16 support). While this increases memory
footprint and training time, it ensures numerical
stability for our initial baseline.
Parallelism Strategy: For training the 100M-
parameter model, we employ Distributed Data Par-
allel (DDP) to replicate the model across multiple
GPUs and train on different mini-batches simulta-
neously. For larger models (e.g., 1B parameters
explored in preliminary experiments), we utilize
Fully Sharded Data Parallel (FSDP) to distribute
model parameters across GPUs via sharding. For
all models, gradient accumulation is used to vir-
tually simulate large batch sizes (0.5M tokens per
batch) beyond what fits in GPU memory for a sin-
gle step.
Table 3 summarizes the compute resources spent
in training our models. This excludes the costs of
tokenizer experiments and initial hyperparameter
exploration.
5.4
Training Dynamics
Figures 5, 6, and 7 (in Appendix A) show the train-
ing and validation loss curves for the three model
variants during training. We observe several impor-
tant patterns:
• Vocabulary Size Impact: Models with larger
vocabulary sizes (20k, 32k) exhibit slightly
more unstable loss curves during early train-
ing, likely due to sparser gradient signals
across the larger embedding table. However,
all variants converge to similar final loss val-
ues.
• No Overfitting: For all models, validation
loss closely tracks training loss throughout
training, indicating that the model does not
overfit on the training data despite seeing the

--- Page 6 ---

Model
nparams (M)
nlayers
dmodel
nheads
dhead
nctx
Batch (M)
Vocab (K)
LR
UrduLM-100M-10k
100
12
768
12
64
1024
0.5
10
6.0e-4
UrduLM-100M-20k
116
12
768
16
64
1024
0.5
20
6.0e-4
UrduLM-100M-32k
134
12
768
16
64
1024
0.5
32
6.0e-4
Table 2: Architectural configurations and hyperparameters of UrduLM model variants. Batch size is in millions of
tokens; vocab size is in thousands. All models were trained for a total of 5–6 billion tokens over 3 epochs.
Configuration
UrduLM-100M
Model size
134 M parameters
Token sequence length
1024
Batch size (effective)
512 samples ≈0.5M tokens
FLOPs per step
315 TFLOPs
Total compute per epoch
3.15 PFLOPs
Total compute (3 epochs)
9.45 PFLOPs
GPU type
4 × NVIDIA V100 (32 GB)
Power consumption per GPU
300 W
Training time per epoch
22 hours
Total training time
66 hours (3 epochs)
Total energy
79.2 kWh (3 epochs)
Estimated carbon footprint
∼31.68 kg CO2 (at 0.4 kg/kWh)
Estimated cost (cloud pricing)
<$100
Table 3: Training resource summary for UrduLM-100M. Carbon footprint assumes regional electricity grid intensity
of 0.4 kg CO2/kWh (approximate for South Asia). Cost estimate based on AWS/GCP spot pricing for V100
instances.
same data for 3 epochs. This suggests the
100M model has sufficient capacity for the
task but is not over-parameterized.
• Learning Saturation: Training for additional
epochs beyond the third did not result in mean-
ingful loss reduction, indicating that the 100M
model reaches its effective learning capac-
ity limit on this corpus. This motivated our
preliminary exploration of 1B-parameter vari-
ants.
The final trained UrduLM-100M-32k model has
been made publicly available at Hugging Face
Model Hub.
6
Evaluation
We evaluate UrduLM using: (1) LLM-as-a-Judge
(Gemini 2.0 Flash) assessing coherence, fluency,
and relevance on 50 diverse prompts; and (2)
Few-shot Evaluation (5-shot) across four tasks:
sentiment classification (SC), grammar error cor-
rection (GEC), question answering with/without
context (QA-C, QA-NC). We curated evaluation
datasets by adapting Urdu classification bench-
marks and translating English datasets, available at
UrduLM-Eval-Dataset.
Figure 4: LLM-as-a-Judge evaluation: UrduLM-100M
competitive despite 10–30× size disadvantage. Scores
averaged over 50 diverse Urdu prompts across coher-
ence, relevance, and fluency.
6.1
LLM-as-a-Judge Results
Figure 4 shows UrduLM-100M achieves compet-
itive quality (7.2/10 average) with multilingual
models 10–30× larger (7.5–8.0/10), demonstrat-
ing monolingual pretraining efficiency. Manual in-
spection reveals UrduLM produces more culturally
appropriate idioms and references, though occa-
sionally struggles with very long-form generation
(>512 tokens).

--- Page 7 ---

6.2
Few-shot Results
Table 4 reports 5-shot performance across four
tasks (5 runs, greedy decoding). UrduLM-100M
excels at sentiment classification (66.6% accu-
racy, surpassing Qwen 1.5B and Gemma 2B),
matches multilingual models on open-domain QA
(0.16 ROUGE-L), but lags on grammar correction
(30.59 vs 35–40 BLEU) and extractive QA (0.17
vs 0.35–0.47 ROUGE-L). Performance patterns
reveal: (1) Language-specific pretraining benefits
sentiment tasks capturing cultural/idiomatic pat-
terns; (2) Complex tasks (GEC, QA-C) benefit
from scale; (3) Open-domain QA benefits from
Urdu-specific world knowledge in monolingual cor-
pus.
Key Findings: (1) Efficiency: UrduLM-100M
achieves 70–85% performance of 10–30× larger
models at <1% training cost; (2) Task-dependent
scaling: Sentiment benefits from language special-
ization, complex tasks favor scale; (3) Multilin-
gual weakness: Baselines underperform on Urdu
vs English benchmarks due to poor tokenization
and diluted capacity. Task analysis and efficiency
comparison table in Appendix A.2.
7
Discussion
7.1
Why Does 100M Compete with 3B
Multilingual Models?
UrduLM-100M’s competitive performance with
models 10–30× larger stems from three factors: (1)
Tokenization Efficiency: Our custom tokenizer
reduces sequence length 20–30%, increasing se-
mantic content per training step and reducing atten-
tion overhead. The 32k embedding table is Urdu-
specialized rather than diluted across 200k+ multi-
lingual vocabularies. (2) Capacity Allocation: A
3B multilingual model supporting 100 languages
effectively allocates ∼30M parameters to Urdu (as-
suming uniform distribution; in practice, even less
due to high-resource language bias). UrduLM’s
100M parameters are fully Urdu-dedicated. (3)
Linguistic Specialization: Monolingual pretrain-
ing avoids cross-linguistic interference, optimizing
exclusively for Urdu-specific phenomena (Perso-
Arabic morphology, syntax, cultural context). Anal-
ogy: a 100M specialist outperforms a 3B generalist
for domain-specific tasks.
7.2
Key Design Choices and Generalization
Vocabulary size: 32k achieved best balance; 10k
exhibited higher perplexity on rare words, while
30k–32k converged. Data diversity: Multi-source
corpus (news, books, web, translations) improves
coverage; literary content contributes dispropor-
tionately to fluency, while news aids factual ac-
curacy. Training duration: 3 epochs (15–18B
tokens) showed continued improvement through
epoch 2, with diminishing returns in epoch 3, sug-
gesting the 100M model nears capacity limits.
Our methodology generalizes through three prin-
ciples: (1) Corpus sizing: ∼0.14 GB per million
speakers (33GB for 230M); for 50M-speaker lan-
guages (Pashto, Sindhi), target 7–10GB. (2) Tok-
enizer design: Custom tokenizers for non-Latin,
morphologically rich languages with script-adapted
regex patterns and vocabulary proportional to com-
plexity. (3) Model scale: 100M parameters suffice
for strong baselines; 1B+ needed for production
quality.
When is monolingual pretraining worth it?
Preferable when: ≥5–10GB data available, ty-
pologically distant from high-resource languages,
non-Latin scripts, domain specialization needed,
or sovereignty required. Fine-tuning multilingual
models preferable when: <1–2GB data, linguisti-
cally similar to high-resource languages, compute-
constrained, or rapid prototyping needed. For 2–
5GB scenarios, hybrid approach (vocabulary exten-
sion + continued pretraining) offers middle ground.
8
Future Work
(1) Scaling validation: Collect more data and train
1B–3B variants to quantify the quality–efficiency
frontier; (2) Instruction tuning: Develop Urdu
prompt–response datasets via translation and na-
tive collection. Preliminary work on both scaling
and instruction tuning is already underway and has
progressed significantly. (3) Cross-lingual test-
ing: Apply methodology to Bengali, Pashto, Sindhi
to validate transferability. (4) Comparative stud-
ies: Rigorously compare monolingual vs fine-tuned
multilingual models across quality, efficiency, cul-
tural appropriateness. (5) Architectural innova-
tions: RoPE, grouped-query attention, and quan-
tization (4-bit, 8-bit). (6) Benchmark develop-
ment: Collaborate with native speakers for expert-
annotated benchmarks. (7) Bias analysis: Conduct
rigorous fairness assessment across gender, reli-
gious, socioeconomic, regional dimensions. (8)
Community engagement: Partner with Pakistani
institutions to expand data collection, develop ap-
plications (chatbots, educational tools), and build

--- Page 8 ---

Model
SC Acc. (%)
GEC BLEU
QA-C ROUGE-L
QA-NC ROUGE-L
UrduLM-100M
66.6
30.59
0.17
0.16
LLaMA 3.2 1B
77.6
39.58
0.35
0.16
Qwen 2.5 1.5B
50.2
40.37
0.47
0.12
Gemma 2 2B
62.6
40.19
0.36
0.13
LLaMA 3.2 3B
50.2
39.9
0.42
0.17
Qwen 2.5 3B
50.02
35.01
0.46
0.16
Table 4: Few-shot (k=5) results averaged on 5 runs
sustainable research infrastructure.
9
Conclusion
We introduce UrduLM, a pretrained monolingual
Urdu language model in low-resource settings. Us-
ing Urdu as a case study, we demonstrate that
a carefully designed 100M-parameter model can
achieve competitive performance with multilingual
models up to 30× its size, while requiring dramat-
ically less computational resources (training cost
<$100, carbon footprint ∼32kg CO2).
Our contributions span the complete pipeline:
a 33GB curated Urdu corpus (the largest to our
knowledge), a custom BPE tokenizer reducing tok-
enization overhead by 20–30%, a 100M-parameter
baseline model achieving 66.6% sentiment accu-
racy and 30.59 BLEU on grammar correction, new
evaluation benchmarks for Urdu generative tasks,
and a complete open-source release of methodol-
ogy, code, data, and models.
Beyond Urdu, this work establishes a repro-
ducible framework applicable to other under-
represented languages (Bengali, Pashto, Sindhi,
Swahili, etc.), promoting AI accessibility and data
sovereignty for low-resource linguistic communi-
ties. We hope this baseline enables future research
toward more inclusive, culturally appropriate, and
efficient language technologies worldwide.
10
Limitations
While our work establishes a systematic methodol-
ogy for Urdu language modeling and demonstrates
strong efficiency-performance trade-offs, several
limitations constrain the scope and generalizability
of our findings:
1. Computational Constraints: Due to limited
compute resources (4× V100 GPUs), we were un-
able to train larger models (3B, 8B parameters) that
would enable more direct comparison with state-
of-the-art multilingual counterparts. Our 100M
baseline, while efficient, may not fully capture the
linguistic nuances and world knowledge required
for production-quality applications. Preliminary
experiments with 1B parameters (Appendix) sug-
gest substantial quality gains, but comprehensive
evaluation of scaling behavior remains future work.
2. Architectural Exploration: Compute con-
straints similarly limited our ability to explore alter-
native architectures (e.g., encoder-decoder models,
mixture-of-experts, sparse attention mechanisms).
These may exhibit different efficiency-performance
trade-offs and could potentially improve results.
We adopted GPT-3 hyperparameters due to their
proven effectiveness, but systematic hyperparame-
ter search could yield further improvements.
3. Dataset Limitations: Despite our extensive
curation efforts, the 33GB corpus remains con-
strained by:
• Digitization Gaps: Limited availability of
digitized Urdu literature, particularly classical
texts and regional dialects. Most literary con-
tent is still in physical form, inaccessible for
NLP.
• Domain Imbalance: News and web content
dominate; specialized domains (medical, le-
gal, scientific) are underrepresented.
• Dialectal Coverage: The corpus primarily
reflects standard Urdu used in Pakistan and
India; regional variants and code-mixing with
local languages (Punjabi, Sindhi, Pashto) are
less represented.
• Quality Variance: OCR-extracted book con-
tent contains residual errors despite manual
verification; web-scraped text includes some
noise from advertisements, navigation ele-
ments, etc.
4. Evaluation Constraints:
• Benchmark Availability: Urdu lacks stan-
dardized, expert-annotated benchmarks for
generative tasks. Our evaluation datasets were

--- Page 9 ---

created through adaptation and translation,
which may not fully capture authentic Urdu
language use.
• LLM-as-a-Judge Bias: Using Gemini 2.0
Flash as an evaluator introduces potential
biases (e.g., preference for certain writing
styles, cultural perspectives). Human evalua-
tion would provide more reliable qualitative
assessment but was infeasible at scale.
• Limited Task Coverage: We evaluate on four
tasks (sentiment classification, grammar cor-
rection, QA with/without context). Broader
evaluation covering summarization, transla-
tion, creative writing, and cultural knowledge
would provide more comprehensive perfor-
mance characterization.
5. Bias and Safety: Although we excluded
sources known to contain harmful or biased content
during data curation, we did not perform system-
atic bias analysis of the trained models. Potential
concerns include:
• Gender Bias: Urdu has grammatical gender;
models may perpetuate stereotypical gender
associations.
• Religious Bias: Urdu is closely associated
with Islamic culture; models may under-
represent or misrepresent other religious per-
spectives.
• Regional Bias: Corpus sources are skewed
toward urban, educated register; rural and in-
formal language use is underrepresented.
• Socioeconomic Bias:
Web content tends
to reflect perspectives of digital-access pop-
ulations, potentially marginalizing lower-
socioeconomic viewpoints.
Future work should include comprehensive fairness
audits and mitigation strategies (e.g., data balanc-
ing, adversarial debiasing).
6. Single-Language Validation: Our method-
ology is demonstrated on Urdu alone. While we
provide theoretical arguments and design principles
for transferability to other low-resource languages,
empirical validation on Bengali, Pashto, Sindhi, or
other languages is required to confirm generaliz-
ability.
7. Inference Efficiency: While we report train-
ing costs and carbon footprint, we do not sys-
tematically evaluate inference efficiency (latency,
throughput, memory requirements) across deploy-
ment scenarios (server, edge devices, mobile).
Quantization and distillation techniques could fur-
ther improve deployment feasibility but remain un-
explored.
8. Temporal Drift: Our corpus was collected in
2023–2024; language evolves rapidly, particularly
in domains like technology and politics. The model
may exhibit temporal bias or lack knowledge of
very recent events. Strategies for continual learning
and corpus updating are necessary for long-term
maintenance.
Despite these limitations, we believe this work
provides a solid foundation and reproducible
methodology that future research can build upon,
addressing these gaps through larger-scale data col-
lection, community-led digitization efforts, multi-
language validation studies, and comprehensive
bias audits.
Ethics Statement
Data Provenance and Licensing: All data sources
used in this work are either: (1) publicly available
under open licenses (FineWeb2: ODC-By v1.0;
UrduHack: MIT); (2) collected from publicly ac-
cessible websites with robots.txt compliance; or
(3) generated via commercial APIs (Google Cloud
OCR, Translation) under proper licensing agree-
ments. We do not redistribute copyrighted book
content or personal data. A preview of the corpus is
publicly available, and full access can be provided
to researchers upon request for reproducibility.
Potential Harms and Mitigation: Language
models can perpetuate biases, generate harmful
content, or be misused for malicious purposes (e.g.,
disinformation, impersonation). We acknowledge
these risks and note that our 100M model, while
less capable than larger models, is not immune.
We have taken initial mitigation steps (excluding
known harmful sources, manual data inspection)
but recognize the need for more rigorous safety
evaluation. We strongly encourage future work
to conduct comprehensive bias audits and develop
content filtering mechanisms before deploying Ur-
duLM in user-facing applications.
Accessibility and Inclusivity: A primary moti-
vation for this work is to promote AI accessibility
for Urdu-speaking communities, who are currently

--- Page 10 ---

underserved by existing language technologies. By
releasing all artifacts openly (code, data, models),
we aim to empower local researchers, institutions,
and developers in Pakistan, India, and diaspora
communities to build culturally appropriate appli-
cations. However, we recognize that digital access
barriers (internet connectivity, computational re-
sources) may limit who can benefit from this work.
We encourage partnerships with local organizations
to ensure broader impact.
Environmental Considerations:
Training
UrduLM-100M consumed 79.2 kWh of energy, re-
sulting in an estimated 31.68 kg CO2 emissions (as-
suming 0.4 kg/kWh grid intensity for South Asia).
While this is orders of magnitude lower than large-
scale model training (e.g., GPT-3: ∼500 metric
tons CO2), we acknowledge that even small-scale
research has environmental impact. We commit to
reporting training costs transparently and explor-
ing more sustainable training practices (renewable
energy, efficient hardware) in future work.
Use of AI Assitants for Writing: We used an
AI-based writing assistant to help with language
polishing and clarity.
References
Ikram Ali and Contributors. 2020.
UrduHack: An
NLP library for the Urdu language.
https://
github.com/urduhack/urduhack. Python NLP li-
brary; MIT License.
Emily M. Bender, Timnit Gebru, Angelina McMillan-
Major, and Shmargaret Shmitchell. 2021. On the
dangers of stochastic parrots: Can language models
be too big? In Proceedings of the 2021 ACM Confer-
ence on Fairness, Accountability, and Transparency,
Virtual Event, Canada. Association for Computing
Machinery.
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, Sandhini Agarwal, Ariel Herbert-Voss,
Gretchen Krueger, Tom Henighan, Rewon Child,
Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu,
Clemens Winter, and 12 others. 2020. Language
models are few-shot learners. In Advances in Neural
Information Processing Systems, volume 33, pages
1877–1901.
Tyler A. Chang, Catherine Arnett, Zhuowen Tu, and
Benjamin K. Bergen. 2024. When is multilingual-
ity a curse? Language modeling for 250 high- and
low-resource languages. In Proceedings of the 2024
Conference of the North American Chapter of the
Association for Computational Linguistics: Human
Language Technologies (Volume 1: Long Papers),
pages 5629–5652, Mexico City, Mexico. Association
for Computational Linguistics.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. BERT: Pre-training of
deep bidirectional transformers for language under-
standing. In Proceedings of the 2019 Conference of
the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies, Volume 1 (Long and Short Papers), pages
4171–4186, Minneapolis, Minnesota. Association for
Computational Linguistics.
Mehrdad Farahani, Mohammad Gharachorloo, Marzieh
Farahani, and Mohammad Manthouri. 2021. Pars-
BERT: Transformer-based model for Persian lan-
guage understanding.
Neural Processing Letters,
53(6):3831–3847.
Manuel Faysse, Patrick Fernandes, Nuno M. Guerreiro,
António Loison, Duarte M. Alves, Caio Corro, Nico-
las Boizard, João Alves, Ricardo Rei, Pedro Hen-
rique Martins, Antoni Bigata Casademunt, François
Yvon, André Martins, Gautier Viaud, Céline Hudelot,
and Pierre Colombo. 2024. CroissantLLM: A truly
bilingual French-English language model. Preprint,
arXiv:2402.00786.
Abdul Ghafoor, Ali Shariq Imran, Sher Muhammad
Daudpota, Zenun Kastrati, Abdullah, Rakhi Batra,
and Mudasir Ahmad Wani. 2021. The impact of
translating resource-rich datasets to low-resource lan-
guages through multi-lingual text processing. IEEE
Access, 9:124478–124490.
Sepp Hochreiter and Jürgen Schmidhuber. 1997. Long
short-term memory. Neural Computation, 9(8):1735–
1780.
Daniel Jurafsky and James H. Martin. 2008. Speech
and Language Processing: An Introduction to Natu-
ral Language Processing, Computational Linguistics,
and Speech Recognition, 2nd edition. Prentice Hall,
Upper Saddle River, NJ.
Omkar Khade, Shruti Jagdale, Abhishek Phaltankar,
Gauri Takalikar, and Raviraj Joshi. 2024. Challenges
in adapting multilingual LLMs to low-resource
languages using LoRA PEFT tuning.
Preprint,
arXiv:2411.18571.
Wahab Khan, Ali Daud, Jamal A. Nasir, and Tehmina
Amjad. 2016. A survey on the state-of-the-art ma-
chine learning models in the context of nlp. Kuwait
Journal of Science, 43(4).
Taku Kudo and John Richardson. 2018. SentencePiece:
A simple and language independent subword tok-
enizer and detokenizer for neural text processing. In
Proceedings of the 2018 Conference on Empirical
Methods in Natural Language Processing: System
Demonstrations, pages 66–71, Brussels, Belgium.
Association for Computational Linguistics.

--- Page 11 ---

Tomas Mikolov, Kai Chen, Greg Corrado, and Jeffrey
Dean. 2013. Efficient estimation of word representa-
tions in vector space. In Proceedings of Workshop at
ICLR.
Guilherme Penedo, Hynek Kydlíˇcek, Loubna Ben al-
lal, Anton Lozhkov, Margaret Mitchell, Colin Raffel,
Leandro Von Werra, and Thomas Wolf. 2024a. The
FineWeb datasets: Decanting the web for the finest
text data at scale. In The Thirty-eight Conference on
Neural Information Processing Systems Datasets and
Benchmarks Track.
Guilherme Penedo, Hynek Kydlíˇcek, Vinko Sabolˇcec,
Bettina Messmer, Negar Foroutan, Amir Hossein
Kargaran, Colin Raffel, Martin Jaggi, Leandro
Von Werra, and Thomas Wolf. 2024b. FineWeb2:
One pipeline to scale them all – adapting pre-
training data processing to every language. Preprint,
arXiv:2506.20920.
Jeffrey Pennington, Richard Socher, and Christopher
Manning. 2014. GloVe: Global vectors for word
representation. In Proceedings of the 2014 Confer-
ence on Empirical Methods in Natural Language Pro-
cessing (EMNLP), pages 1532–1543, Doha, Qatar.
Association for Computational Linguistics.
Colin Raffel, Noam Shazeer, Adam Roberts, Kather-
ine Lee, Sharan Narang, Michael Matena, Yanqi
Zhou, Wei Li, and Peter J. Liu. 2020. Exploring the
limits of transfer learning with a unified text-to-text
transformer. Journal of Machine Learning Research,
21(140):1–67.
Pedram Rostami, Ali Salemi, and Mohammad Javad
Dousti. 2024.
PersianMind:
A cross-lingual
Persian-English large language model.
Preprint,
arXiv:2401.06466.
Phillip Rust, Jonas Pfeiffer, Ivan Vuli´c, Sebastian Ruder,
and Iryna Gurevych. 2021. How good is your tok-
enizer? On the monolingual performance of multi-
lingual language models. In Proceedings of the 59th
Annual Meeting of the Association for Computational
Linguistics and the 11th International Joint Confer-
ence on Natural Language Processing (Volume 1:
Long Papers), pages 3118–3135, Online. Association
for Computational Linguistics.
Rico Sennrich, Barry Haddow, and Alexandra Birch.
2016. Neural machine translation of rare words with
subword units. In Proceedings of the 54th Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 1715–1725,
Berlin, Germany. Association for Computational Lin-
guistics.
Meliksah Turker, Mehmet Erdi Ari, and Aydin Han.
2024.
VBART: The turkish LLM.
Preprint,
arXiv:2403.01308.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz
Kaiser, and Illia Polosukhin. 2017. Attention is all
you need. In Advances in Neural Information Pro-
cessing Systems, volume 30, pages 5998–6008.
Chris Wendler, Veniamin Veselovsky, Giovanni Monea,
and Robert West. 2024. Do llamas work in English?
On the latent language of multilingual transformers.
Preprint, arXiv:2402.10588.
Yiran Zhao, Wenxuan Zhang, Guizhen Chen, Kenji
Kawaguchi, and Lidong Bing. 2024. How do large
language models handle multilingualism? In Find-
ings of the Association for Computational Linguistics:
ACL 2024, pages 9986–10005, Bangkok, Thailand.
Association for Computational Linguistics.
A
Appendix: Training Loss Curves
This appendix provides detailed training and valida-
tion loss curves for all model variants, supporting
the analysis in Section 6.
A.1
UrduLM-100M Variants
Figures 5, 6, and 7 show training dynamics for the
three vocabulary size variants of UrduLM-100M.
All models were trained for 3 epochs on the 33GB
corpus, with identical hyperparameters except for
vocabulary size and corresponding embedding di-
mensions.
Key Observations:
• Validation loss tracks training loss closely
across all variants, indicating no overfitting.
• Larger vocabulary models (20k, 32k) exhibit
slightly more loss oscillation during early
training (first 5–10% of steps) but converge to
similar final loss.
• Training beyond epoch 3 showed negligible
loss reduction (not shown), suggesting the
100M model reaches its effective capacity
limit.
Figure 5: Training and validation loss for UrduLM-
100M with 10k vocabulary. Validation loss (orange)
closely tracks training loss (blue), indicating healthy
generalization.

--- Page 12 ---

Figure 6: Training and validation loss for UrduLM-
100M with 20k vocabulary.
Figure 7: Training and validation loss for UrduLM-
100M with 32k vocabulary (final model). Slightly higher
early-training variance compared to 10k variant, but
converges to similar final loss.
A.2
Detailed Evaluation Analysis
A.2.1
Task-Specific Analysis
Sentiment
Classification
UrduLM-100M
(66.6%) surpasses Qwen 1.5B (50.2%) and
Gemma 2B (62.6%), though LLaMA 1B leads
(77.6% with 10× parameters).
Strong perfor-
mance suggests language-specific pretraining
captures sentiment patterns (idioms, cultural refer-
ences) better than multilingual translation-based
reasoning.
Grammar Error Correction
UrduLM-100M
(BLEU 30.59) lags multilingual baselines (35–40),
indicating GEC benefits from scale. Task requires
precise syntax and multiple correction generation,
exceeding 100M capacity.
QA
with
Context
UrduLM-100M
(0.17
ROUGE-L) trails baselines (0.35–0.47) due to:
(1) limited 1024-token context vs Qwen’s 128k;
(2) extractive QA requires precise span selection,
benefiting from scale. Instruction-tuning could
close gap.
QA without Context
UrduLM-100M (0.16)
matches LLaMA 1B and Qwen 3B, indicating
monolingual pretraining advantage when leverag-
ing Urdu-specific world knowledge (culture, his-
tory, geography) naturally present in corpus.
A.2.2
Computational Efficiency and
Environmental Impact
We analyze the efficiency of UrduLM (100M)
vs. Llama 3.2 (3B) for resource-constrained de-
ployment. Calculations assume a single NVIDIA
V100 (32GB) and regional carbon intensity of
0.485 kgCO2e/kWh. To standardize comparisons,
we report theoretical lower bounds based on peak
hardware throughput and memory bandwidth (900
GB/s). Notably, Llama 3.2’s tokenizer is inefficient
for Urdu, producing ≈2.8× more tokens (504M
vs 180M) for the same 1GB corpus.
Fine-Tuning Efficiency
Table 5 shows theoreti-
cal costs for fine-tuning on 1GB of text. UrduLM is
highly efficient, whereas Llama 3.2 incurs a ≈67×
higher compute requirement driven by parameter
count and the "tokenizer tax" (processing 504M vs
180M tokens).
Model
Tokens
Compute
Time*
Energy
CO2
Cost
(1GB Data)
(PFLOPS)
(h)
(kWh)
(kg)
(PKR)
UrduLM
∼180 M
144.7
0.36
0.22
0.11
7.53
Llama 3.2
∼504 M
9,707
23.17
13.90
6.74
486.5
Table 5: 1GB Fine-Tuning Efficiency. *Time repre-
sents theoretical minimum at peak throughput; real-
world wall times are typically 2–3× higher.
Inference Efficiency
Table 6 compares metrics
for a single inference prompt pass (prefill). Based
on V100 memory bandwidth limits, UrduLM of-
fers sub-millisecond theoretical latency, making it
suitable for real-time edge applications.
Model
In Tokens
Compute
Latency*
Energy
Cost
(Prompt)
(TFLOPS)
(ms)
(J)
(PKR/1k)
UrduLM
12
0.003
0.60
0.18
0.004
Llama 3.2
33
0.211
7.20
2.16
0.040
Table 6: Inference Efficiency. *Latency is the theoreti-
cal memory-bound minimum (Model Size / 900 GB/s).
UrduLM benefits from smaller size and 2.75× fewer
tokens.

```
