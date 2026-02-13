---
title: "2024-Garcia-Introducing Bode A Fine-Tuned Large Language Model for Portuguese - PDF Extract"
source_pdf: "2024-Garcia-Introducing Bode A Fine-Tuned Large Language Model for Portuguese.pdf"
pages: 10
extracted_at: "2026-02-13T09:50:29.476161"
---

# PDF Extract: 2024-Garcia-Introducing Bode A Fine-Tuned Large Language Model for Portuguese

**Source PDF:** 2024-Garcia-Introducing Bode A Fine-Tuned Large Language Model for Portuguese.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

Introducing Bode: A Fine-Tuned Large Language Model for Portuguese
Prompt-Based Task
Gabriel Lino Garcia1, Pedro Henrique Paiola1, Luis Henrique Morelli1, Giovani Candido1,
Arnaldo Cândido Júnior2, Danilo Samuel Jodas1, Luis C. S. Afonso1, Ivan Rizzo Guilherme3,
Bruno Elias Penteado3, João Paulo Papa1
1School of Sciences, São Paulo State University, Bauru, Brazil
2Institute of Natural Sciences and Technology, São Paulo State University, Rio Claro, Brazil
3Institute of Biosciences, Humanities and Exact Sciences, São Paulo State University, São José do Rio Preto, Brazil
{gabriel.lino, pedro.paiola, luis.morelli, giovani.candido, arnaldo.candido,
ivan.guilherme, bruno.penteado, joao.papa}@unesp.br, danilo.jodas@gmail.com
Abstract
Large Language Models (LLMs) are increas-
ingly bringing advances to Natural Language
Processing. However, low-resource languages,
those lacking extensive prominence in datasets
for various NLP tasks, or where existing
datasets are not as substantial, such as Por-
tuguese, already obtain several benefits from
LLMs, but not to the same extent.
LLMs
trained on multilingual datasets normally strug-
gle to respond to prompts in Portuguese satis-
factorily, presenting, for example, code switch-
ing in their responses. This work proposes
a fine-tuned LLaMA 2-based model for Por-
tuguese prompts named Bode in two versions:
7B and 13B. We evaluate the performance of
this model in classification tasks using the zero-
shot approach with in-context learning, and
compare it with other LLMs. Our main con-
tribution is to bring an LLM with satisfactory
results in the Portuguese language, as well as
to provide a model that is free for research or
commercial purposes.
1
Introduction
Large Language Models (LLMs) have reshaped the
landscape of how computers comprehend and gen-
erate text. These robust networks, trained on mas-
sive volumes of textual data, have become central
partakers in Natural Language Processing (NLP)
applications. Models such as GPT-3, developed by
OpenAI (Brown et al., 2020), BERT, developed by
Google (Devlin et al., 2019), and LLaMA, devel-
oped by Meta (Touvron et al., 2023a), have demon-
strated remarkable achievements in NLP tasks rang-
ing from machine translation to text generation.
Language models have evolved to enhance the
NLP capacities and cope with challenging aspects
focused on high performance with fewer parame-
ters and task-switching to particular applications
based on better fine-tuning procedures. Recent
architectures such as LLaMA 2 (Touvron et al.,
2023b), Mistral 7B (Jiang et al., 2023), and Fal-
con 7B (Almazrouei et al., 2023) have supported
increasing efficiency and accuracy while reducing
the model’s complexity and memory requirements
for the training process. In addition, openly avail-
able LLMs have been highly demanded to drive
research toward better generative architectures.
As the world has witnessed unprecedented
progress in the capabilities of NLP models, partic-
ularly in English, the considerable computational
costs associated with their development and train-
ing remain a significant challenge. Recent research,
exemplified by the work of Brown et al. (2020) on
GPT-3 and the comprehensive analysis conducted
by Devlin et al. (2019) on BERT, has shed insights
on the massive scale of datasets and computing
power required to design such models. This chal-
lenge has posed a significant obstacle to developing
a more comprehensive range of high-quality mod-
els for less-spoken languages, such as Portuguese.
While multilingual models such as mBERT, pro-
posed by Devlin et al. (2019), have expanded the
scope of NLP applications, addressing the need for
specific models for individual languages, such as
Portuguese, is essential and required for particular
applications. Despite their versatility, multilingual
models may not capture the complex nuances and
idiosyncrasies of a certain language.
Portuguese is spoken by over 260 million peo-
ple worldwide, making it a significant part of our
global community. In this context, we adopt a fea-
sible and efficient approach to develop a model for
NLP tasks in Portuguese, known as Bode, a promis-
arXiv:2401.02909v1  [cs.CL]  5 Jan 2024

--- Page 2 ---

ing initiative to cope with this gap. The proposed
model involves adapting and improving the prompt-
based tasks by tailoring the LLaMA 2 architecture
for Portuguese instruction-following responses. By
capitalizing on research over a publicly translated
dataset of instruction-following tasks, the method
applies a fine-tuning procedure to leverage the
LLaMA 2 capabilities to the context of the Por-
tuguese language. Bode has the potential to stimu-
late research and innovation within the Portuguese-
speaking community by providing customized so-
lutions to address their unique singularities.
The structure of this paper can be summarized as
follows: In Section 2, we offer a brief theoretical
foundation for the proposed project. Following
that, Section 3 provides a concise review of related
works, and Section 4 introduces the proposed LLM.
Then, Sections 5 and 6 outline the methodology and
discuss the results yielded by the proposed model,
respectively. To conclude, Section 7 presents our
findings and overall conclusions of the work.
2
Theoretical Background
This section presents the fundamental theoretical
aspects that support the proposed research and is
organized into subsections. Together, these sub-
sections establish the essential aspects behind the
methodology presented in this study.
2.1
LLaMA Models
LLaMA models (Touvron et al., 2023a) are LLMs
based on the well-established transformer architec-
ture. These models borrow several training and in-
ference mechanisms from other architectures, such
as RMSNorm normalizing function (Zhang and
Sennrich, 2019) for pre-normalization from GPT-3,
the SwiGLU activation function (Shazeer, 2020)
from PaLM (Chowdhery et al., 2022), and the Ro-
tary Position Embeddings (Su et al., 2022) from
GPT-Neo (Black et al., 2021) to enhance the train-
ing stability and improve the performance by re-
ducing the number of hidden units. These models
also employ causal multi-head attention to reduce
memory usage and runtime by avoiding the stor-
age of attention weights and the computation of
key/query scores that are masked due to the causal
nature of the language modeling task.
LLaMA 2, introduced by Touvron et al. (2023b),
is an updated iteration of the previous models.
These new models were trained on a significantly
expanded pre-training corpus, incorporating new
publicly available data that extends it by over
40%.
The primary architectural difference in-
volves the introduction of Grouped-query Atten-
tion (GQA) (Ainslie et al., 2023). GQA divides
query heads into G groups, each sharing a single
key and value head. This approach enables interpo-
lation between Multi-head (Vaswani et al., 2023)
and Multi-query Attention (Shazeer, 2019) while
reducing the size of the key-value cache and the
amount of data loaded, ultimately improving infer-
ence scalability. LLaMA 2 has three variants, with
7, 13, and 70 billion parameters. Experiments have
shown that LLaMA 2 models outperform previous
models on popular benchmarks.
2.2
Mistral 7B
Mistral 7B, proposed by Jiang et al. (2023), is an
LLM that focuses on high performance with effi-
cient inference and reduced memory usage during
decoding using GQA and Sliding Window Atten-
tion (SWA) (Beltagy et al., 2020). Unlike tradi-
tional transformers, it optimizes performance by
stacking layers and enabling access to information
beyond the window size. A hidden state at position
i in layer k can reach all the previous layer’s hid-
den states within i −W, with W representing the
window size. Recursively, the hidden state can ac-
cess tokens from the input layer up to a distance of
W ×k. Thus, a fixed attention span allows limiting
the cache size by utilizing a rolling buffer cache
that prevents it from growing larger, and this reduc-
tion does not impact the model’s quality negatively.
Lastly, predicting tokens individually during
sequence generation is necessary, as each token
depends on the preceding ones.
However, the
prompt is known in advance, enabling the pre-
filling of the key-value cache by storing the pre-
vious prompt keys and values of transformers. This
action streamlines the process, focusing solely on
calculating the attention for the new token. In case
of a very lengthy prompt, it is feasible to divide it
into smaller segments and pre-fill the cache with
each segment. The window size is selected as the
chunk size, and attention is computed for each
chunk, encompassing both the cache and the chunk
itself.
Results have shown that Mistral 7B outperforms
LLaMA 2 13B across various tasks. Additionally,
it surpasses LLaMA 134B on most benchmarks
tested, demonstrating superior performance, partic-
ularly in code, mathematics, and reasoning.

--- Page 3 ---

2.3
Falcon 7B
Falcon-7B, designed by Technology Innovation In-
stitute (TII) (Almazrouei et al., 2023), is an LLM
pre-trained on 1.5 trillion tokens from RefinedWeb
(Penedo et al., 2023), which is composed of English
web data. Its architecture, adapted from GPT-3, in-
volves various modifications, comprising Rotary
Position Embeddings, Multi-query Attention, and
Flash Attention (Dao et al., 2022).
Multi-query Attention operates similarly to
Multi-head Attention, allowing multiple heads to
share a single set of keys and values. In addition,
Flash Attention reduces the memory access dur-
ing the precise attention calculation by performing
Softmax reduction without considering the entire
input and by avoiding storing intermediate atten-
tion matrices for the backward pass. Also, within
the decoder block, there is the integration of par-
allel attention and a Multilayer Perceptron (MLP)
featuring a single normalization layer. The model
is available on Hugging Face1.
2.4
Low-Rank Adaptation
Low-Rank Adaptation (LoRA) is a technique de-
signed to facilitate the adaptation of LLMs exten-
sively pre-trained on a vast corpus of textual data
to novel and unexplored tasks without incurring
any inference latency or compromising the length
of input sequences (Hu et al., 2021). When con-
fronted with a new downstream task, LoRA in-
serts a compact low-rank matrix into the pre-trained
weight matrices of the language model. Then, these
newly added parameters are trained with the spe-
cific downstream task and serve as the pivotal el-
ement for adapting the pre-trained weights to the
unique requirements of the new task at hand.
Hu et al. (2021) highlights the importance of
tuning the rank of the low-rank matrix, which is a
hyperparameter that can impact the number of train-
able parameters and the model quality. In addition,
by adapting the attention matrices and freezing the
MLP modules for efficiency purposes, the authors
demonstrated their strategy’s potential by outper-
forming other adaptation approaches, such as the
default fine-tuning process.
Compared to the standard fine-tuning procedure,
LoRA significantly reduces the trainable parame-
ters required for adaptation to downstream tasks
while maintaining a high-quality model. Another
valuable feature of LoRA concerns its ability to
1https://huggingface.co/tiiuae/falcon-7b
facilitate quick task-switching when deployed as a
service, as it allows for sharing most model param-
eters.
3
Related Works
In this section, we review two notable contributions
in the context of NLP applications, with a partic-
ular emphasis on the Portuguese language. Both
works present different strategies for performing
monolingual pre-training in Portuguese to enhance
models extensively trained on English-centric text
corpora. The subsection 3.1 discusses the work of
Pires et al. (2023), which introduces Sabiá 7B. The
subsection 3.2 explores the research conducted by
Larcher et al. (2023), which proposes openCabrita
3B.
3.1
Sabiá
Sabiá, introduced by Maritaca AI (Pires et al.,
2023), challenges the practice of pre-training a sin-
gle model for multiple languages. Their research
shows that monolingual pre-training in the target
language, Portuguese in this case, significantly im-
proves models that have undergone extensive train-
ing on a diverse text corpus in English. As a result,
they introduced Sabiá, a Portuguese LLM derived
from further pre-training GPT-J (Wang and Komat-
suzaki, 2021) and LLaMA models on Portuguese-
specific texts. Sabiá models were pre-trained using
Portuguese subsets from the ClueWeb 2022 (Over-
wijk et al., 2022) dataset with LLaMA’s 7 billion
and 65 billion parameters architectures.
Conversely, Sabiá-J models used GPT-J with 6
billion parameters, following GPT-3’s architecture
and hyperparameters. However, these models un-
derwent 18 days of training on 7.8 billion tokens,
roughly one epoch of the Portuguese dataset, re-
sulting in fewer tokens trained than Sabiá.
Both models were assessed on the Portuguese
Evaluation Tasks (Poeta) benchmark, which in-
cludes 14 NLP datasets in Portuguese. This evalua-
tion followed a few-shot approach, where specific
examples were manually selected for each dataset,
limiting them to fit within a 2048-token context.
The results showcased the advantages of language-
specific specialization using a nearly state-of-the-
art 65-billion-parameter model for Portuguese.
It is essential to note that Sabiá is not openly
available to the public. Access to the model may
require arrangements with Maritaca AI.

--- Page 4 ---

3.2
Cabrita
In a recent work, Larcher et al. (2023) introduced
openCabrita 3B, an LLM designed for NLP tasks
involving the Portuguese language. This model
relies on the 3-billion-parameter version of OpenL-
LaMA (Geng and Liu, 2023), which reproduces the
widely known Meta’s LLaMA 3B, a state-of-the-art
LLM pre-trained on 1 trillion English tokens.
To enhance its ability to handle the Portuguese
language effectively, openCabrita 3B underwent a
process known as Tokenizer Adaptation involving
two steps. At first, a new tokenizer was trained on a
corpus of Portuguese texts sourced from Wikipedia.
Subsequently, the newly crafted tokenizer was inte-
grated with OpenLLaMA’s default tokenizer. No-
tably, new tokens were appended to the end of the
tokenizer matrix, resulting in a combined tokenizer
matrix comprising 52, 000 tokens. The outcome
yielded a bilingual tokenizer capable of handling
English and Portuguese.
After the adaptation strategy, the original script
and hyperparameters from the OpenLLaMA train-
ing were employed for both pre-training and train-
ing of openCabrita 3B. In the preprocessing phase,
a Portuguese subset of the mC4 dataset (Xue et al.,
2021) was filtered to retain only the highest-quality
documents. From this filtered dataset, 7 billion to-
kens were used in the continued pre-training stage.
For training purposes, 170 billion tokens were em-
ployed.
The openCabrita 3B demonstrated commend-
able performance on a range of Portuguese NLP
tasks, including Question-Answering (QA), classi-
fication, and regression, consistently outperform-
ing openLLaMA 3B. It closely rivaled the open-
Cabrita version that relies only on the default to-
kenizer without adaptation, occasionally surpass-
ing it in some scenarios. Moreover, openCabrita
3B closely approaches the performance of Sabiá-J
(6B), demonstrating superiority over GPT-J (6B)
and competitive performance compared to LLaMA
7B.
4
Proposed Model
The proposed method aims to provide a fine-tuned
language model tailored for Portuguese prompt re-
sponse applications based on the new LLaMA 2
architecture. Figure 1 depicts the overview of the
fine-tuning approach employed in this work. Sim-
ilar to Cabrita, the proposed method is designed
to harness the capability of the LLaMA model to
address instruction-following tasks by using a large
dataset with a broad range of Portuguese instruc-
tions. However, we extend the counterpart work by
leveraging the newly designed version of the LLM
called LLaMA 2 by Meta AI. This new architec-
ture provides several improvements ranging from
a larger number of parameters to a more human-
machine interaction supported by training on addi-
tional data through reinforcement learning. This
process may lead to better interactive, reliable com-
munication and more accurate response generation.
In terms of the fine-tuning procedure, the base
LLaMA 2 model was trained on the same Por-
tuguese dataset assembled by the work of Larcher
et al. (2023), which provides a broad range of Por-
tuguese tokens. The fine-tuning procedure to create
the Bode model was performed using the Low-
Rank Adaptation method based on the following
hyperparameter values: i) LoRA alpha is set to 32,
and ii) the dropout rate is set to 0.05.
5
Methodology
This section describes the methodology employed
to support the evaluation of the proposed model
in terms of its capability to generate accurate Por-
tuguese responses compared to other LLMs. We
provide an overview of the experimental setup, the
description of the zero-shot and in-context-learning
approaches, and datasets used for evaluation.
5.1
Experimental Setup
The experiments for news classification tasks were
conducted on the supercomputer Santos Dumont
(SDumont)3, which boasts a processing capacity of
5.1 PetaFLOPS. It features a hybrid configuration
of computational nodes, leveraging available paral-
lel processing architecture. The node used was the
Bull Sequana X1120, equipped with 2 Intel Xeon
Skylake 6252 CPUs with 24 cores each, totaling
48 cores, 384GB of RAM, and 4 NVIDIA Volta
V100 GPUs. Additionally, the Kaggle platform
was utilized for the sentiment analysis tasks, which
provided access to an environment equipped with
an NVIDIA K80 GPU. The code was written in
Python 3.10 with PyTorch 2.0.0 and Hugging Face.
We adopted zero-shot and in-context learning ap-
2The image was created by the authors, and the Bode
logo was generated using Bing Chat. “Meta-Logo” by dora-
vand is licensed under CC BY 2.0. To view a copy of this
license, visit https://creativecommons.org/licenses/
by/2.0/?ref=openverse..
3https://sdumont.lncc.br/machine.php

--- Page 5 ---

Figure 1: Overview of the proposed method.2
proaches for the LLM’s learning. Each approach is
further explained in the following sections.
5.1.1
Zero-Shot Learning
In zero-shot learning, the proposed model is re-
quested to produce an output for previously un-
trained data. This process involves using a trans-
fer learning approach by harnessing a pre-trained
model for which the input data labels were unavail-
able during the training time (Tan et al., 2021).
This procedure instructs the model to generalize to
unexplored scenarios. For the zero-shot approach,
experiments were conducted without performing
any fine-tuning procedure in the Bode model for
the given classification task.
5.1.2
In-Context Learning
The in-context learning approach is designed to
explore the model’s capability regarding tasks re-
lated to specific contextual information. Accord-
ing to (Brown et al., 2020), contextual learning is
employed to adapt the models to the context pro-
vided by the input data, which is assembled from a
similar task for which the model has been trained
previously, thus providing the ability to produce
more accurate responses while refraining from a
further training of the model. Unlike the classical
fine-tuning procedure, which enables the models to
change the learning to a different task or domain
by updating their weights, in-context learning al-
lows the harnessing of the same context provided
by massive amounts of data to promote slight or
moderate adjustments to the same contextual do-
main the models have been introduced previously.
Therefore, we employed contextual learning in the
Bode model to promote improvements and provide
a better performance according to the context of
the dataset used.
5.1.3
Prompt Engineering
Prompt Engineering is a relatively recent method
designed to promote adjustment to LLM models
by providing new contexts and specific instruc-
tions during human-machine communication. This
process involves articulating new prompts for spe-
cific contexts and using them to assist the model
in comprehending the task or domain to promote
adaptation in generating more detailed responses.
This method is essential for either zero-shot or in-
context learning to support adjustments to different
tasks.
In the context of this work, experiments con-
ducted on prompt engineering applications were
designed to expose the proposed model to a broad
range of classification tasks and support fine ad-
justments intended to maximize its accuracy. For
a broader assessment, we provide two prompt ap-
plications exhibiting the model’s capacity to re-
spond to sentiment analysis tasks and news cate-
gory classification in terms of the multiclass classi-
fication analysis. The following samples illustrate
the prompt applications in the two classification
tasks:
• Sentiment analysis into 3 classes:
Prompt: “Você é um assistente de pergun-
tas e respostas. Cada contexto passado será
um tweet que está vinculado a um sentimento
correspondente. No total, são 3 tipos de sen-
timentos: Positivo, Neutro e Negativo. O seu

--- Page 6 ---

objetivo é dado um tweet, encontrar qual é o
seu sentimento correspondente. Abaixo estão
alguns exemplos:
Tweet: :D que lindo dia ! Resposta: Positivo
Tweet: eu tô tão cansado :( Resposta: Nega-
tivo
Tweet: Microsoft lança pesquisa resultado de
pesquisa com o Ibope sobre uso da #tecnolo-
gia no #trabalho no #Brasil @MicrosoftBr
NielsenIBOPE Resposta: Neutro
Considere que tweets com chamadas de notí-
cias com sempre neutros, independente do
seu conteúdo, a não ser que o autor emita
sua opinião sobre o acontecimento relatado.
Dado o contexto, responda em qual dos 3 tipos
de sentimentos o tweet a seguir se enquadra.”
• News category classification into 4 classes:
Prompt: "Você é um assistente de per-
guntas e respostas. Cada contexto passado
será uma notícia que está vinculada a uma
categoria correspondente. No total, são 4
categorias: Mundo, Esportes, Negócios e Tec-
nologia. O seu objetivo é dado uma notícia,
encontrar qual é a sua categoria correspon-
dente. Abaixo estão alguns exemplos:
Notícia: Até o final do ano, a gigante da com-
putação planeja ter seu maior número de fun-
cionários desde 1991. Resposta: Tecnologia
Notícia: Michael Phelps ganhou a medalha
de ouro no 400 Medley individual e estabele-
ceu um recorde mundial em um tempo de 4
minutos 8,26 segundos. Resposta: Esportes
Notícia: TEEHRAN (Reuters) - Um oficial
militar iraniano disse domingo a Israel e os
Estados Unidos não ousariam atacar o Irã,
pois poderia revidar em qualquer lugar de Is-
rael com seus mais recentes mísseis, informou
as agências de notícias. Resposta: Mundo
Notícia: Reuters-Os varejistas de vestuário es-
peram que suas modas de volta às aulas façam
a nota entre os adolescentes conscientes do
estilo e os jovens adultos neste outono, mas
pode ser uma venda difícil, com os alunos e os
pais mantendo um mais apertado. carteiras.
Resposta: Negócios
Dado o contexto, responda em qual das 4 cat-
egorias a notícia a seguir se enquadra."
For a given prompt, the model’s output encom-
passes the content category and additional text
comprising a brief description of the input prompt.
Therefore, after extensive empirical observations,
we realized that the first word of the generated con-
tent is usually considered the correct class for the
given text.
5.2
Baseline models
The performance evaluation was assessed by com-
paring the proposed Bode model with the follow-
ing existing state-of-the-art large language archi-
tectures:
1. Cabrita 7B, and openCabrita 3B (Larcher
et al., 2023);
2. Falcon 7B (Almazrouei et al., 2023);
3. Llama 2 7B, and Llama 2 13B (Touvron et al.,
2023b);
4. Mistral 7B (Jiang et al., 2023).
The primary evaluation is concerned with com-
paring Cabrita 7B with the proposed Bode model
based on the LaMMA 2 architecture. The authors
designed a Cabrita 7B4 model based on the first
version of the LaMMA architecture. However, at
the time of the writing of this work, there was no
paper about it, and the underlying LLaMA model
was unavailable5. Therefore, due to such unex-
pected constraints, we restricted the assessment to
the openCabrita 3B model proposed in the work of
Larcher et al. (2023).
5.3
Datasets for evaluation
The experiments were performed over three Por-
tuguese datasets to assist in evaluating the proposed
model in different real-world applications. Table 1
exhibits the used datasets in detail, including their
related classification task and the number of sam-
ples adopted in each experiment. Moreover, the
subjective aspect of instruction-following datasets
in terms of performance evaluation and quality of
the given responses is worth noting. In this sense,
the research focus hinges on classification tasks.
The following items provide a detailed descrip-
tion of each dataset:
4https://huggingface.co/22h/cabrita-lora-v0-1
5https://huggingface.co/decapoda-research/
llama-7b-hf

--- Page 7 ---

Table 1: Datasets employed in each experiment.
Dataset
Classification Task
Samples
TweetSentBr
Multiclass
4,999
TweetSentBr
Binary
5,000
AGNews
Multiclass
7,600
FakeRecogna
Binary
10,560
• TweetSentBr6: A Portuguese sentiment anal-
ysis dataset assembled from Twitter con-
tent (Brum and Nunes, 2017). The data can
be tasked with multiclass or binary classifica-
tion problems, with the multiclass data labeled
into positive, negative, and neutral classes. We
opted to use only the test set supplied with the
dataset to avoid the computational expenses
associated with the model’s training. There-
fore, only 5, 000 samples were used in this
phase.
• AGNews7: A dataset comprising a collection
of news articles evenly distributed among four
news categories, thus promoting a multiclass
classification task. Due to the computational
workload, we adopted only the test set for the
model’s training phase, thus leading to 7, 600
samples.
• FakeRecogna8: A dataset designed for fake
news detection purposes, with samples evenly
distributed across real and fake news cate-
gories (Garcia et al., 2022). The version used
in this study was assembled from the test set of
the original FakeRecogna dataset, thus lead-
ing to 5, 280 samples in each class of news
articles.
All experiments were conducted in the test sam-
ples provided by their respective datasets. How-
ever, those samples are also representative since
they originate from the same data distribution of
the entire dataset. By leveraging the provided test
set, we reduced the computational workload re-
quired during the model’s evaluation, resulting in
a more efficient and cost-effective approach rather
than using the entire test dataset in the model’s
performance assessment.
6https://www.kaggle.com/datasets/augustop/
portuguese-tweets-for-sentiment-analysis
7https://www.kaggle.com/datasets/amananandrai/
ag-news-classification-dataset
8https://github.com/Gabriel-Lino-Garcia/
FakeRecogna
5.4
Evaluation Metrics
We adopted the evaluation procedure by using only
the test sets from each dataset. It is worth not-
ing that the fine-tuning procedure was only per-
formed using the openCabrita Portuguese dataset
to train the proposed Bode model with the LaMMA
2 architecture. Subsequently, the performance of
the models was evaluated by calculating the aver-
age values for accuracy and F1-score over the test
sets of each dataset using zero-shot and in-context
learning without any additional training with the
baseline Portuguese datasets.
6
Experiments and results
Before presenting the results and discussing the ex-
periments conducted in this article, it is important
to emphasize that we did not include the results of
Cabrita 7B in all experiments due to its unavailabil-
ity during the preparation of this work. However,
we chose to retain the results that had already been
obtained, as Cabrita 7B was one of the few LLMs
trained and freely available for the Portuguese lan-
guage. Furthermore, there is the prospect that the
authors may address the availability issue of the
model in the near future.
As previously alluded to, a total of four experi-
ments were conducted across a range of tasks and
datasets. Figure 2 illustrates the outcomes of the
models across the various tasks, employing accu-
racy as the primary evaluative metric. Furthermore,
in accordance with the depiction provided in Fig-
ure 3, emphasis on the results obtained under the
evaluation metric of F1-score.
In this context, it becomes evident that, for sen-
timent analysis tasks, whether with two or three
classes, the LLaMa 2 7B showed superior perfor-
mance compared to the other base models with
the same number of parameters. In contrast, Bode
13B demonstrated higher evaluation scores than
the base models with 13B parameters, with a sub-
stantial advantage over other LLMs in this case.
It is worth noting that Bode 13B achieved an ac-
curacy of over 90%, while its counterpart version
with the same number of parameters, LLaMa 2
13B, achieved only 56.9%.
When considering
multi-class news classification, Bode 7B exhibits
the highest performance among the 7B models,
whereas a marginal difference of 0.9% is observed
in favor of LLaMa 2 13B among the 13B models.
Finally, in the context of fake news identification,
both Bode models outperform their counterparts,

--- Page 8 ---

Sentiment - 3 Classes
Sentiment - 2 Classes
News Categories
F
akeRecogna
0
20
40
60
80
60.3
82.5
69.1
69.4
74.5
84.3
59.5
57.1
56.1
83.2
0.0
0.0
37.4
61.8
30.3
47.2
47.8
53.3
43.3
52.5
61.2
78.6
37.8
22.5
64.3
93.2
79.5
65.9
44.2
56.9
82.4
64.7
Accuracy
Bode 7B
LLaMA 2 7B
Cabrita 7B
openCabrita 3B
F
alcon 7B
Mistral 7B
Bode 13B
LLaMA 2 13B
Figure 2: Accuracy values for each dataset and LLM adopted in the experiments.
underscoring the consistency of the Bode model’s
performance, which consistently ranks among the
top performers, even though it may not excel in
every single task.
Considering the Bode model and its correspond-
ing base model, LLaMa 2 7B, it becomes evident
that both exhibit optimal configurations that vary
depending on the specific task at hand. However,
one plausible explanation for the observed perfor-
mance decrement of the Bode model in comparison
to LLaMa 2 7B may be attributed to catastrophic
forgetting. This phenomenon pertains to the pos-
sibility that the model may inadvertently unlearn
previously acquired knowledge during fine-tuning,
consequently leading to the loss of critical informa-
tion.
7
Conclusion
In this article, we introduce Bode, a large-scale lan-
guage model developed to advance the field of NLP
in the Portuguese language. Bode is built upon the
LLaMA 2 model, incorporating elements from the
7B and 13B models, adapted for the context of the
Portuguese language. Language models like Bode
play a crucial role in a wide range of applications,
from virtual assistants to machine translation sys-
tems, and have a significant impact on academic
research.
During the training phase of Bode, we employed
the Portuguese-translated version of Alpaca as our
training dataset. This process was instrumental in
adapting the model to the language and specific
grammar of Portuguese, enabling Bode to compre-
hend and generate text within a more culturally and
linguistically appropriate context.
The results achieved by Bode in binary and
multi-class classification tasks were promising and
demonstrated the model’s effectiveness. This out-
come suggests that Bode has the potential to en-
hance a variety of NLP applications in Portuguese,
from sentiment analysis to news categorization.
We hope this work will encourage other re-
searchers and developers to explore further and
enhance the model, thereby contributing to the con-
tinuous advancement of NLP in the Portuguese
language. However, the ongoing development of
Bode is essential, and we aim to enhance it over
time by expanding its training data and refining its
performance across a range of tasks.
References
Joshua Ainslie, James Lee-Thorp, Michiel de Jong, Yury
Zemlyanskiy, Federico Lebrón, and Sumit Sanghai.
2023. Gqa: Training generalized multi-query trans-
former models from multi-head checkpoints.
Ebtesam Almazrouei, Hamza Alobeidli, Abdulaziz Al-
shamsi, Alessandro Cappelli, Ruxandra Cojocaru,
Merouane Debbah, Etienne Goffinet, Daniel Hes-

--- Page 9 ---

Sentiment - 3 Classes
Sentiment - 2 Classes
News Categories
F
akeRecogna
0
20
40
60
80
55.4
82.0
69.2
69.5
74.1
84.0
63.0
62.0
46.3
82.7
0.0
0.0
37.5
61.7
24.5
44.5
44.4
47.4
43.7
51.6
58.0
78.0
50.7
31.5
55.2
93.2
79.6
64.2
42.1
49.6
82.7
70.6
F1-score
Bode 7B
LLaMA 2 7B
Cabrita 7B
openCabrita 3B
F
alcon 7B
Mistral 7B
Bode 13B
LLaMA 2 13B
Figure 3: F1-score values for each dataset and LLM adopted in the experiments.
low, Julien Launay, Quentin Malartic, Badreddine
Noune, Baptiste Pannier, and Guilherme Penedo.
2023. Falcon-40B: an open large language model
with state-of-the-art performance. Unpublished.
Iz Beltagy, Matthew E. Peters, and Arman Cohan. 2020.
Longformer: The long-document transformer.
Sid Black, Leo Gao, Phil Wang, Connor Leahy,
and Stella Biderman. 2021.
GPT-Neo:
Large
Scale Autoregressive Language Modeling with Mesh-
Tensorflow. If you use this software, please cite it
using these metadata.
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, Sandhini Agarwal, Ariel Herbert-Voss,
Gretchen Krueger, Tom Henighan, Rewon Child,
Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu,
Clemens Winter, Christopher Hesse, Mark Chen, Eric
Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess,
Jack Clark, Christopher Berner, Sam McCandlish,
Alec Radford, Ilya Sutskever, and Dario Amodei.
2020. Language models are few-shot learners.
Henrico Bertini Brum and Maria das Graças Volpe
Nunes. 2017.
Building a sentiment corpus of
tweets in Brazilian Portuguese.
arXiv preprint
arXiv:1712.08917.
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin,
Maarten Bosma, Gaurav Mishra, Adam Roberts,
Paul Barham, Hyung Won Chung, Charles Sutton,
Sebastian Gehrmann, Parker Schuh, Kensen Shi,
Sasha Tsvyashchenko, Joshua Maynez, Abhishek
Rao, Parker Barnes, Yi Tay, Noam Shazeer, Vin-
odkumar Prabhakaran, Emily Reif, Nan Du, Ben
Hutchinson, Reiner Pope, James Bradbury, Jacob
Austin, Michael Isard, Guy Gur-Ari, Pengcheng Yin,
Toju Duke, Anselm Levskaya, Sanjay Ghemawat,
Sunipa Dev, Henryk Michalewski, Xavier Garcia,
Vedant Misra, Kevin Robinson, Liam Fedus, Denny
Zhou, Daphne Ippolito, David Luan, Hyeontaek Lim,
Barret Zoph, Alexander Spiridonov, Ryan Sepassi,
David Dohan, Shivani Agrawal, Mark Omernick, An-
drew M. Dai, Thanumalayan Sankaranarayana Pil-
lai, Marie Pellat, Aitor Lewkowycz, Erica Moreira,
Rewon Child, Oleksandr Polozov, Katherine Lee,
Zongwei Zhou, Xuezhi Wang, Brennan Saeta, Mark
Diaz, Orhan Firat, Michele Catasta, Jason Wei, Kathy
Meier-Hellstern, Douglas Eck, Jeff Dean, Slav Petrov,
and Noah Fiedel. 2022. Palm: Scaling language mod-
eling with pathways.
Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra,
and Christopher Ré. 2022. Flashattention: Fast and
memory-efficient exact attention with io-awareness.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. Bert: Pre-training of deep
bidirectional transformers for language understand-
ing.
Gabriel L Garcia, Luis CS Afonso, and João P Papa.
2022. Fakerecogna: A new brazilian corpus for fake
news detection. In International Conference on Com-
putational Processing of the Portuguese Language,
pages 57–67. Springer.
Xinyang Geng and Hao Liu. 2023. Openllama: An open
reproduction of llama.
Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan
Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and

--- Page 10 ---

Weizhu Chen. 2021. Lora: Low-rank adaptation of
large language models.
Albert Q. Jiang, Alexandre Sablayrolles, Arthur Men-
sch, Chris Bamford, Devendra Singh Chaplot, Diego
de las Casas, Florian Bressand, Gianna Lengyel, Guil-
laume Lample, Lucile Saulnier, Lélio Renard Lavaud,
Marie-Anne Lachaux, Pierre Stock, Teven Le Scao,
Thibaut Lavril, Thomas Wang, Timothée Lacroix,
and William El Sayed. 2023. Mistral 7b.
Celio Larcher, Marcos Piau, Paulo Finardi, Pedro
Gengo, Piero Esposito, and Vinicius Caridá. 2023.
Cabrita: closing the gap for foreign languages.
Arnold Overwijk, Chenyan Xiong, and Jamie Callan.
2022. Clueweb22: 10 billion web documents with
rich information. In Proceedings of the 45th Inter-
national ACM SIGIR Conference on Research and
Development in Information Retrieval, SIGIR ’22,
page 3360–3362, New York, NY, USA. Association
for Computing Machinery.
Guilherme Penedo, Quentin Malartic, Daniel Hesslow,
Ruxandra Cojocaru, Alessandro Cappelli, Hamza
Alobeidli, Baptiste Pannier, Ebtesam Almazrouei,
and Julien Launay. 2023. The refinedweb dataset for
falcon llm: Outperforming curated corpora with web
data, and web data only.
Ramon Pires, Hugo Abonizio, Thales Sales Almeida,
and Rodrigo Nogueira. 2023.
Sabiá: Portuguese
large language models.
Noam Shazeer. 2019. Fast transformer decoding: One
write-head is all you need.
Noam Shazeer. 2020. Glu variants improve transformer.
Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha,
Bo Wen, and Yunfeng Liu. 2022. Roformer: En-
hanced transformer with rotary position embedding.
Chufeng Tan, Xing Xu, and Fumin Shen. 2021. A sur-
vey of zero shot detection: methods and applications.
Cognitive Robotics, 1:159–167.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timothée Lacroix,
Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal
Azhar, Aurelien Rodriguez, Armand Joulin, Edouard
Grave, and Guillaume Lample. 2023a. Llama: Open
and efficient foundation language models.
Hugo Touvron, Louis Martin, Kevin Stone, Peter Al-
bert, Amjad Almahairi, Yasmine Babaei, Nikolay
Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti
Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton
Ferrer, Moya Chen, Guillem Cucurull, David Esiobu,
Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller,
Cynthia Gao, Vedanuj Goswami, Naman Goyal, An-
thony Hartshorn, Saghar Hosseini, Rui Hou, Hakan
Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa,
Isabel Kloumann, Artem Korenev, Punit Singh Koura,
Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Di-
ana Liskovich, Yinghai Lu, Yuning Mao, Xavier Mar-
tinet, Todor Mihaylov, Pushkar Mishra, Igor Moly-
bog, Yixin Nie, Andrew Poulton, Jeremy Reizen-
stein, Rashi Rungta, Kalyan Saladi, Alan Schelten,
Ruan Silva, Eric Michael Smith, Ranjan Subrama-
nian, Xiaoqing Ellen Tan, Binh Tang, Ross Tay-
lor, Adina Williams, Jian Xiang Kuan, Puxin Xu,
Zheng Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan,
Melanie Kambadur, Sharan Narang, Aurelien Ro-
driguez, Robert Stojnic, Sergey Edunov, and Thomas
Scialom. 2023b. Llama 2: Open foundation and
fine-tuned chat models.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz
Kaiser, and Illia Polosukhin. 2023. Attention is all
you need.
Ben Wang and Aran Komatsuzaki. 2021.
GPT-J-
6B: A 6 Billion Parameter Autoregressive Lan-
guage Model. https://github.com/kingoflolz/
mesh-transformer-jax.
Linting Xue, Noah Constant, Adam Roberts, Mihir Kale,
Rami Al-Rfou, Aditya Siddhant, Aditya Barua, and
Colin Raffel. 2021. mT5: A massively multilingual
pre-trained text-to-text transformer. In Proceedings
of the 2021 Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies, pages 483–498, On-
line. Association for Computational Linguistics.
Biao Zhang and Rico Sennrich. 2019. Root mean square
layer normalization.

```
