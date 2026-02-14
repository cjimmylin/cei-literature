---
title: "2025-Metinov-KyrgyzBERT A Compact Efficient Language Model for Kyrgyz NLP - PDF Extract"
source_pdf: "2025-Metinov-KyrgyzBERT A Compact Efficient Language Model for Kyrgyz NLP.pdf"
pages: 3
extracted_at: "2026-02-13T14:50:57.389168"
---

# PDF Extract: 2025-Metinov-KyrgyzBERT A Compact Efficient Language Model for Kyrgyz NLP

**Source PDF:** 2025-Metinov-KyrgyzBERT A Compact Efficient Language Model for Kyrgyz NLP.pdf
**Total Pages:** 3

---

## Content

```
--- Page 1 ---

KyrgyzBERT: A Compact, Efficient Language
Model for Kyrgyz NLP
Adilet Metinov∗, Gulida M. Kudakeeva†, Gulnara D. Kabaeva‡
∗†‡Institute of Information Technology,
Kyrgyz State Technical University named after I. Razzakov, Bishkek, Kyrgyzstan
∗metinovab@kstu.kg, †kgm@kstu.kg, ‡kabaevagd9@kstu.kg
Abstract—The advancement of Natural Language Processing
(NLP) has been largely driven by large-scale transformer models,
yet these breakthroughs have predominantly benefited high-
resource languages. Low-resource languages like Kyrgyz lack
the foundational models necessary for robust NLP application
development. To address this gap, we introduce KyrgyzBert,
the first publicly available, monolingual BERT-based language
model pre-trained for the Kyrgyz language. KyrgyzBERT is a
compact and efficient 35.9M parameter model developed with
a custom tokenizer to optimally handle the language’s unique
morphological characteristics. To demonstrate its effectiveness,
we construct a new, high-quality sentiment analysis benchmark,
kyrgyz-sst2, by translating the Stanford Sentiment Treebank
and manually annotating the entire test set. Our experiments
show that our finetuned model, kyrgyzbert_sst2, achieves an
F1-score of 0.8280, a result highly competitive with a finetuned
mBERT model five times its size. We publicly release all artifacts
from this study, providing a comprehensive suite of tools to
accelerate NLP research for the Kyrgyz language.
Index Terms—Natural Language Processing, Kyrgyz Lan-
guage, Language Model, BERT, Low-resource Languages, Senti-
ment Analysis, Computational Efficiency
I. INTRODUCTION
Recent years have witnessed a paradigm shift in Natural
Language Processing (NLP), spurred by the advent of large-
scale, transformer-based language models such as BERT [1].
These models, pre-trained on vast amounts of text data, have
established new state-of-the-art results across a wide array of
tasks. However, this progress has created a significant resource
disparity; languages like English have a rich ecosystem of
models and datasets, while low-resource languages like Kyr-
gyz remain critically underserved.
The Kyrgyz language, a member of the Turkic language
family, lacks the foundational computational resources neces-
sary to leverage modern NLP techniques. This technological
gap hinders both academic research and the development
of practical applications for the Kyrgyz-speaking commu-
nity. While multilingual models like mBERT [1] and XLM-
RoBERTa [2] offer a potential starting point, they are often
sub-optimal. Recent studies have shown that general-purpose
multilingual models can underperform compared to classical
machine learning methods on Kyrgyz tasks, highlighting the
need for specialized resources [3]. These models must balance
representational capacity across over 100 languages and may
not fully capture the rich, agglutinative morphology of Kyrgyz.
To address this critical gap, we present two primary contri-
butions. First, we introduce KyrgyzBERT, the first publicly
available monolingual BERT model specifically pre-trained
for the Kyrgyz language. To create this model, we developed
a custom WordPiece tokenizer from scratch and pre-trained
a compact, 35.9M parameter model on a large corpus of
Kyrgyz text. Our goal is to provide a computationally efficient
and linguistically tailored foundation for future Kyrgyz NLP
research.
Our second contribution is a rigorous validation of Kyr-
gyzBERT’s capabilities. To this end, we constructed a new,
high-quality sentiment analysis benchmark dataset based on
the Stanford Sentiment Treebank (SST-2) [4]. Crucially, to
ensure the reliability of our evaluation, the entire test set
was manually created and annotated by a native speaker after
translation. We use this benchmark to finetune and evaluate
KyrgyzBERT against strong multilingual baselines. Our exper-
iments demonstrate that KyrgyzBERT achieves performance
highly competitive with mBERT, despite being five times
smaller.
All
artifacts
from
this
study—the
pre-trained
KyrgyzBert, the custom bert-kyrgyz-tokenizer,
the finetuned sentiment models, and the kyrgyz-sst2
benchmark dataset—are made publicly available1 to foster
and accelerate the development of NLP technologies for the
Kyrgyz language.
II. RELATED WORK
Research in NLP for Turkic languages has grown, but
resources for Kyrgyz remain scarce. While models for Turkish,
such as BERTurk [5], and for Arabic, like AraBERT [6], have
demonstrated the value of monolingual transformers, Kyrgyz
has largely relied on multilingual models or classical machine
learning approaches.
A recent and highly relevant study by Benli and Sharshem-
baev [3] conducted a comparative analysis of sentiment anal-
ysis for Kyrgyz. They used a dataset of 500 IMDB reviews
translated into Kyrgyz and tested a range of models, including
Logistic Regression (LR), Random Forest (RF), and deep
learning models like LSTM and RNN. Their key finding was
that a traditional LR model achieved the highest accuracy
1All artifacts from this study are publicly available at: https://huggingface.
co/metinovadilet
arXiv:2511.20182v1  [cs.CL]  25 Nov 2025

--- Page 2 ---

(83%), outperforming a multilingual BERT model which
only scored 60%. This result highlighted the sub-optimal
performance of general multilingual models on Kyrgyz when
not specifically adapted for the task. Crucially, the authors
concluded that future progress in Kyrgyz NLP requires the
development of a Kyrgyz-specific BERT model and larger,
higher-quality datasets. Our work directly addresses this call
by introducing KyrgyzBERT and a new, manually-verified
benchmark dataset.
III. METHODOLOGY
Our methodology is centered around two core efforts: the
creation of the foundational KyrgyzBERT model and the
construction of a high-quality benchmark for its evaluation.
A. KyrgyzBERT Pre-training
The
cornerstone
of
our
work
is
metinovadilet/KyrgyzBert, a monolingual language
model designed specifically for Kyrgyz.
1) Tokenizer: A standard multilingual vocabulary is ill-
suited
for
the
agglutinative
nature
of
Kyrgyz.
There-
fore, we first trained a new WordPiece tokenizer from
scratch,
metinovadilet/bert-kyrgyz-tokenizer,
on a large Kyrgyz text corpus, ensuring optimal segmentation
of Kyrgyz words into meaningful sub-word units.
2) Model Architecture and Training: ‘KyrgyzBert‘ is a
BERT-based model with a compact architecture, making it
efficient for training and inference. The key specifications are
detailed in Table I. The model was pre-trained from scratch on
a private corpus of over 1.5 million Kyrgyz sentences. Training
was performed on a single NVIDIA RTX 3090 GPU using the
Masked Language Modeling (MLM) objective.
TABLE I
KYRGYZBERT MODEL ARCHITECTURE
Parameter
Value
Vocabulary Size
30,522
Hidden Size
512
Attention Heads
8
Number of Layers
6
Total Parameters
35.9M
B. Sentiment Analysis Benchmark
To validate KyrgyzBERT, we constructed a new senti-
ment analysis benchmark, which we name and release as
metinovadilet/kyrgyz-sst2.
1) Dataset Creation: We used the Stanford Sentiment Tree-
bank (SST-2) as our source. The English sentences from the
original train and validation splits were translated into Kyrgyz
using a state-of-the-art Neural Machine Translation (NMT)
system, with their original labels carried over.
2) Gold-Standard Test Set Curation: To create a reliable
evaluation set, the 1,821 **unlabeled** sentences from the
original SST-2 test split were first translated into Kyrgyz using
an NMT system. Subsequently, each of these translated Kyrgyz
sentences was **manually annotated for sentiment by a native
Kyrgyz speaker.** This crucial step ensures that our test set’s
labels are not merely carried over from an English source but
are ground-truth assessments of the sentiment expressed in the
final Kyrgyz text, creating a ’gold-standard’ for evaluation.
C. Experimental Setup
We conducted a comparative sentiment analysis experiment.
The finetuned models are the focus of our analysis, with the
base models serving as a zero-shot baseline. All models were
finetuned for 3 epochs with a learning rate of 2e-5 where
applicable. We evaluated performance using the weighted F1-
score and Accuracy.
IV. RESULTS AND DISCUSSION
The comprehensive results of our evaluation are presented
in Table II, with the performance-to-size trade-off for the
finetuned models visualized in Fig. 1.
TABLE II
SENTIMENT ANALYSIS BENCHMARK RESULTS
Model
F1-score (Weighted)
Size (M Params)
Finetuned Models
KyrgyzBERT
0.8280
35.9
mBERT
0.8401
177.0
Base Models (Zero-Shot)
XLM-RoBERTa
0.3221
270.0
mBERT
0.3509
177.0
0
25
50
75
100
125
150
175
Model Size (Millions of Parameters)
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
F1-Score (Weighted)
mBERT
KyrgyzBERT
Model Performance vs. Size on Kyrgyz-SST2
Fig. 1.
Model performance (F1-Score) vs. size (millions of parameters).
KyrgyzBERT achieves performance competitive with mBERT while being
5x smaller, demonstrating superior computational efficiency.
The results clearly indicate that task-specific finetuning is
essential, as the base models perform poorly, with F1-scores

--- Page 3 ---

near the level of a random classifier (Table II). Our primary
finding is that finetuned ‘KyrgyzBert‘ achieves a strong F1-
score of 0.8280, confirming that a compact, monolingual
model is highly effective for downstream tasks in Kyrgyz.
As visualized in Fig. 1, the most compelling result is the
trade-off between performance and computational efficiency.
‘KyrgyzBert‘ is approximately five times smaller than mBERT,
yet the performance gap is only 1.2%. This exceptional
efficiency is a critical advantage for a low-resource language
community, as it makes advanced NLP models more accessible
by lowering the barrier for training, finetuning, and deploy-
ment on consumer-grade hardware. Interestingly, our finetuned
mBERT achieves a high F1-score of 0.84, in contrast to the
60% accuracy reported by Benli and Sharshembaev [3] for a
non-finetuned mBERT, underscoring the critical importance of
task-specific finetuning and high-quality benchmark data.
The immediate adoption of ‘KyrgyzBert‘ by the community
further underscores its value. Since its release on the Hugging
Face Hub, the model has been downloaded over 300 times,
indicating a clear and active demand for such foundational
resources.
V. CONCLUSION
In this paper, we introduced ‘KyrgyzBert‘, a compact and
efficient 35.9M parameter language model, and its accompa-
nying tokenizer, as new foundational resources for the Kyrgyz
language. By evaluating it on a newly created and manually
annotated sentiment analysis benchmark, we have demon-
strated its strong performance, achieving results competitive
with models five times its size.
Our work makes a significant contribution by providing the
first suite of open-source, monolingual tools specifically for
Kyrgyz NLP. All developed resources—including the base
metinovadilet/KyrgyzBert, the finetuned sentiment
models
metinovadilet/kyrgyzbert_sst2
and
metinovadilet/mbert-kyrgyz-sst2-finetuned,
and
the
metinovadilet/kyrgyz-sst2
dataset—are
publicly available to foster a new wave of research and
application
development.
Future
work
should
focus
on
evaluating
‘KyrgyzBert‘
across
more
diverse
tasks
and
domains, and pre-training larger versions as more data
becomes available.
ACKNOWLEDGMENT
The authors would like to thank the colleagues and admin-
istration of the Institute of Information Technology, Kyrgyz
State Technical University, for their support in providing
computational resources and an environment that enabled this
research.
REFERENCES
[1] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “Bert: Pre-training
of deep bidirectional transformers for language understanding,” arXiv
preprint arXiv:1810.04805, 2018.
[2] A. Conneau, K. Khandelwal, N. Goyal, V. Chaudhary, G. Wenzek,
F. Guzm´an, E. Grave, M. Ott, L. Zettlemoyer, and V. Stoyanov, “Un-
supervised cross-lingual representation learning at scale,” arXiv preprint
arXiv:1911.02116, 2019.
[3] ˙I. Benli and B. Sharshembaev, “Using Machine Learning Algorithms for
Kyrgyz Sentiment Analysis,” World Journal of Advanced Research and
Reviews, vol. 23, no. 03, pp. 554–561, 2024.
[4] R. Socher, A. Perelygin, J. Wu, J. Chuang, C. D. Manning, A. Y. Ng, and
C. Potts, “Recursive deep models for semantic compositionality over a
sentiment treebank,” in Proceedings of the 2013 conference on empirical
methods in natural language processing, 2013, pp. 1631–1642.
[5] S. Schweter, “BERTurk: A turkish BERT model,” arXiv preprint
arXiv:2005.00570, 2020.
[6] W. Antoun, F. Baly, and H. Hajj, “AraBERT: Transformer-based model
for arabic language understanding,” in Proceedings of the 4th Workshop
on Open-Source Arabic Corpora and Processing Tools, with a Shared
Task on Offensive Language Detection, 2020, pp. 9–15.

```
