---
title: "2022-Launay-PAGnol An Extra-Large French Generative Model - PDF Extract"
source_pdf: "2022-Launay-PAGnol An Extra-Large French Generative Model.pdf"
pages: 14
extracted_at: "2026-02-13T13:13:45.327376"
---

# PDF Extract: 2022-Launay-PAGnol An Extra-Large French Generative Model

**Source PDF:** 2022-Launay-PAGnol An Extra-Large French Generative Model.pdf
**Total Pages:** 14

---

## Content

```
--- Page 1 ---

PAGnol: An Extra-Large French Generative Model
Julien Launay∗1,2
Elena Tommasone∗1
Baptiste Pannier1
François Boniface†
Amélie Chatelain1
Alessandro Cappelli1
Iacopo Poli1
Djamé Seddah3
1 LightOn 2 LPENS, École Normale Supérieure 3 Inria, Paris
{julien,elena,baptiste,amelie,alessandro,iacopo}@lighton.ai
djame.seddah@inria.fr
lair.lighton.ai/pagnol
Abstract
Access to large pre-trained models of varied
architectures, in many different languages, is
central to the democratization of NLP. We in-
troduce PAGnol, a collection of French GPT
models.
Using scaling laws, we efﬁciently
train PAGnol-XL (1.5B parameters) with the
same computational budget as CamemBERT,
a model 13 times smaller. PAGnol-XL is the
largest model trained to date for the French lan-
guage. We plan to train increasingly large and
performing versions of PAGnol, exploring the
capabilities of French extreme-scale models.
For this ﬁrst release, we focus on the pre-
training and scaling calculations underlining
PAGnol. We ﬁt a scaling law for compute for
the French language, and compare it with its
English counterpart. We ﬁnd the pre-training
dataset signiﬁcantly conditions the quality of
the outputs, with common datasets such as OS-
CAR leading to low-quality offensive text. We
evaluate our models on discriminative and gen-
erative tasks in French, comparing to other
state-of-the-art French and multilingual mod-
els, and reaching the state of the art in the ab-
stract summarization task. Our research was
conducted on the public GENCI Jean Zay su-
percomputer, and our models up to the Large
are made publicly available.
1
Introduction
Large
pre-trained
language
models
are
the
workhorses of modern Natural Language Pro-
cessing (NLP). The use of scalable and efﬁ-
cient attention-based Transformers (Vaswani et al.,
2017), rather than recurrent neural networks, has
enabled increasingly large and capable models.
Through self-supervised learning, these models
learn contextual word embeddings, building a gen-
eral representation of language. After this pre-
*Equal contribution.
†Work performed at LightOn.
training they can be ﬁne-tuned to target speciﬁc
tasks (e.g. classiﬁcation, parsing, summarization).
Three approaches dominate the ﬁeld: (1) causal
autoregressive decoder-only models, such as GPT
(Radford et al., 2018), learning from a gen-
eral language modelling tasks; (2) bidirectional
encoder-only models, such as BERT (Devlin et al.,
2018), learning from masked language modelling;
(3) sequence-to-sequence models, such as BART
(Lewis et al., 2019) or T5 (Raffel et al., 2020), com-
bining both a bidirectional encoder and an autore-
gressive decoder, learning from a language denois-
ing task. Encoder-only and sequence-to-sequence
models excel in language understanding tasks, and
have shadowed autoregressive models as a lesser
option.
Autoregressive models have been shown to pre-
dictably beneﬁt from increased size (Kaplan et al.,
2020; Henighan et al., 2020). Scaling laws estab-
lish a direct relationship between model size and
end-task performance, justifying the training of in-
creasingly large models (Brown et al., 2020; Zeng
et al., 2021; Kim et al., 2021; Wei et al., 2021).
These laws can also inform design decisions, help-
ing practitioners use their available compute budget
optimally. A signiﬁcant ﬁnding has been that larger
models are more sample and compute efﬁcient:
with a given compute budget, it is preferable to
train a larger model signiﬁcantly short of conver-
gence than to train a smaller model to convergence.
Furthermore, at extreme-scale, such as the 175 bil-
lion parameters of GPT-3 (Brown et al., 2020), au-
toregressive models exhibit unique few-shot abili-
ties: they can learn from a few prompted examples,
without weight updates. This capability questions
the current ﬁne-tuning paradigm, and may make
billion parameters models more attractive and us-
able. Recent forays into prompt engineering/tuning
(Li and Liang, 2021; Lester et al., 2021) have even
seemingly bridged the gap between few-shot per-
formance and ﬁne-tuning.
arXiv:2110.08554v1  [cs.CL]  16 Oct 2021

--- Page 2 ---

Encoder-only (CamemBERT (Martin et al.,
2019) and FlauBERT (Le et al., 2019)) and
sequence-to-sequence models (BARThez (Eddine
et al., 2020a)) exist for the French language, and
recently a decoder-only model with 1 billions pa-
rameters has been made available (Simoulin and
Crabbé, 2021). We introduce PAGnol1 in this fam-
ily, a collection of four French GPT-like models,
and make the following contributions:
• Largest French model. We train on CCNet
and publicly release four models, with up to
1.5B parameters for PAGnol-XL. At the time
of this work, this is the largest non-sparse
French language model available, and we plan
to explore increasingly large and powerful
models in the future.
• Optimal scaling. We use scaling laws to in-
form our training setup, resulting in optimal
use of our compute budget. PAGnol-XL is
trained with a budget of only 3 PF-days, just
as much as the 13 times smaller CamemBERT.
From our collection of models, we adjust scal-
ing laws for the French language.
• Dataset suitability.
We highlight the im-
portance of proper dataset pre-processing
when training generative autoregressive mod-
els. While OSCAR has been relied on for
French encoder-only models, we ﬁnd it is not
suited to PAGnol, leading to low-quality of-
fensive outputs.
• End-task performance.
We evaluate on
discriminative (FLUE) and generative tasks
(question answering on FQuAD and summa-
rization with OrangeSum) in the ﬁne-tuning
and prompt tuning regimes.
We establish
a new state of the art for summarization in
French on OrangeSum.
2
Related work
Language models.
The design and training of
neural language models able to create and pro-
cess word embeddings is the cornerstone of mod-
ern NLP. Early on, self-supervised learning was
identiﬁed as an efﬁcient and scalable way to train
such models. The use of deeper and more complex
neural architectures enabled going from static em-
beddings (word2vec (Mikolov et al., 2013), GloVe
(Pennington et al., 2014)) to contextual embed-
dings, allowing models to deal with polysemy. Al-
1PAG: Pré-Apprentissage Génératif. Marcel Pagnol was a
famous French novelist.
though approaches such as ELMo (Peters et al.,
2018) and ULMFiT (Howard and Ruder, 2018)
highlighted that learned representations can be
transferred across downstream tasks, the poor scal-
ability of RNNs prevented this vision from being
fully realized.
By getting rid of the costly and delicate recurrent
processing, attention-based Transformers (Vaswani
et al., 2017) spurred a wide interest in NLP. GPT
(Radford et al., 2018), a decoder-only variant of
Transformers, demonstrated large-scale transfer
learning from general language modelling to 12
NLU tasks. Along with the rise of easy-to-use li-
braries, encoder-only BERT (Devlin et al., 2018),
relying on masked language modeling, made NLP
a commodity – wherein every practitioner could
rely on a pre-trained language model and ﬁne-tune
it cheaply to a task of interest. BERT models are
limited by their ability to only "ﬁll-in-the-gap" for
a span of words: this forbids their use in generative
tasks (e.g. summarization).
With sequence to sequence models and pre-
training through denoising tasks, the original ar-
chitecture of Transformers made a comeback with
BART (Lewis et al., 2019), bridging the gap be-
tween the generative capabilities of decoder-only
models and the downstream task performance of
encoder-only models. Through gradually larger
and more powerful architectures, state-of-the-art
models are approaching human-level performance
on many tasks.
Successive generations of GPT models have
questioned the current ﬁne-tuning paradigm. GPT-
2 (Radford et al., 2019), with 1.5 billion param-
eters, demonstrated that large language models
could tackle entirely new tasks through few-shot
learning2. Without any ﬁne-tuning, from just a few
prompted examples, GPT-2 achieved fair perfor-
mance on a number of complex downstream tasks.
Furthering this endeavour, GPT-3 (Brown et al.,
2020), with 175 billion parameters, achieved state-
of-the-art performance on some tasks, without the
need for ﬁne-tuning. This opens new possibilities
for low-resources tasks, as well as paths to more
natural interactions with these models: recent re-
search suggests the gap between few-shot learning
and ﬁne-tuning may even be bridged through so-
called prompt programming/tuning (Li and Liang,
2021; Lester et al., 2021).
2In other areas of machine learning, this has been referred
to as zero-shot learning, as no weight updates are necessary.

--- Page 3 ---

Scaling laws.
More speciﬁcally to our setting,
neural language models have been shown to pre-
dictably beneﬁt from increased scale (Kaplan et al.,
2020). Their training dynamics are size-invariant,
allowing test loss, parameter count, and dataset
size to be correlated through smooth scaling laws.
This is in fact true of all GPT-like autoregressive
models, even when applied to image, multimodal,
or mathematics modeling (Henighan et al., 2020).
Gains in autoregressive cross-entropy loss also di-
rectly translates to gains in end-task performance
after ﬁne-tuning. As they relate to compute budget,
these predictions can be used to inform the training
of large models.
Non-English
generative
models.
BERT-like
models are now available in a broad number of
languages, either as specialized models are as mul-
tilingual ones. This is less so the case for genera-
tive models, perhaps because of issues in control-
ling the language used at generation time. For the
French language, GPTfr is an autoregressive gener-
ative model, and BARThez (Eddine et al., 2020a)
targets some generative abilities. Smaller-scale ef-
forts exist, such as BelGPT (Louis, 2020), but they
are limited to small models. GPT models have
been trained for German (Schweter, 2020), Chi-
nese (Zeng et al., 2021), and the Arabic language
(Antoun et al., 2021a), among others.
3
Efﬁcient training with scaling laws
Scaling.
We use scaling laws to inform the dura-
tion of the training of our largest models. Rather
than training to convergence, which would be
wasteful, we train to optimality, as predicted by
the equations provided in (Kaplan et al., 2020).
This is akin to what has been done for GPT-3, and
this enables us to keep our computational budget
in line with that of CamemBERT, a model 13x
smaller than PAGnol-XL. We ﬁnd that training all
of our models for a single epoch on the 30GT of
CCNet enables us to reach optimality for the most
expensive XL model. Table 3 presents the ratios
between the compute budget effectively used and
that to optimality (rC
opt) or to convergence (rC
conv).
While our small model is trained to convergence,
others are trained signiﬁcantly short of it. We ﬁnd
that our training performance matches nicely with
the estimated 2.6 PF-days for the training of GPTfr-
LARGE from (Simoulin and Crabbé, 2021).
4
PAGnol
In this section, we describe the data, model, and
training speciﬁcations for PAGnol. In Table 1, we
highlight some of the key differences and similari-
ties with other French models, and in Table 2 we
present two multilingual models that we consider
in the following.
4.1
Pre-training data
Sourcing.
The Common Crawl (CC) project
browses and indexes all content available online. It
generates 200-300 TiB of data per month (around
5% of which is in French), and constitutes the bulk
of most NLP datasets nowadays.
We consider
in our experiments two datasets based on Com-
monCrawl data: CCNet (Wenzek et al., 2020) and
OSCAR (Ortiz Suárez et al., 2020). Once tok-
enized, OSCAR contains 33GT and CCNet 32GT.
We use CCNet for all our main experiments and re-
leased models, and compare with results obtained
on OSCAR in Section 5. We validate on the fr-
wiki dataset (0.5GT) and French TreeBank (650kT)
(Abeillé et al., 2003).
CCNet.
CCNet combines the usual fastText
(Joulin et al., 2017) pre-processing of CC data with
an additional ﬁltering step to select high-quality
documents. This ﬁltering is done through a lan-
guage model trained on Wikipedia, ensuring a text
quality similar to that of its articles. We use a ver-
sion of CCNet identical to the one considered in
the CamemBERT paper.
OSCAR.
OSCAR uses a fastText classiﬁer to se-
lect documents and identify their languages, with-
out any additional ﬁltering. OSCAR is thus more
varied, but more "noisy", than CCNet. OSCAR has
been used to train other French language models
such as CamemBERT.
Tokenization.
We use byte-level Byte-Pair En-
coding (BPE), with a vocabulary of 50,262 tokens:
256 bytes, 6 special tokens, and 50,000 merges.
Paragraphs are separated by an <EOS> token and
documents are separated by a <SEP> token. We
add a preﬁx space before tokenization, so that the
ﬁrst word in a paragraph is tokenized in the same
way as if it was at any other position. This is similar
to the setup of FlauBERT and GPT-2. For the mod-
els trained on OSCAR, we use a slightly smaller
vocabulary size of 50,000 tokens.

--- Page 4 ---

CamemBERT
FlauBERT
BARThez
GPTfr
PAGnol (ours)
Language
French
French
French
French
French
Parameters
110/335M
138/373M
165M
124M/1B
124M/355M/773M/1.5B
Context
512
512
768
1024
1024/2048
Dataset
OSCAR
Customa
Customa
Filtered Common Crawl
CCNet
33GT/138GB
13GT/71GB
66GB
1.6/3.11 GT
32GT
Tokenization
SentencePiece 32k
BPE 50k
SentencePiece 50k
BPE 50k
BPE 50k
Compute [PF-days]
3/10
∼7/26b
∼4b
?/2.6
0.3/0.7/2/3
Table 1: Model, data, and training setup for PAGnol and other French models. Data size is reported in gigatokens
(GT), and compute in PF-days (8.64×1019 FLOP). PAGnol is the largest French model. Despite being signiﬁcantly
larger than existing models, its compute cost remains reasonable: as recommended by scaling laws, we train models
to optimality, and not to convergence.
aFlauBERT and BARThez use a similar pre-training dataset assembling CommonCrawl, NewsCrawl, Wikipedia, and other
smaller corpora.
bInsufﬁcient data was provided by authors to infer compute budgets properly.
mBERT
mBART
Language
104 languages
25 languages
Parameters
110M
610M
Context
512
768
Dataset
Wikipedia
CC25
180GT/1369GB
(10GT/57GB French)
Tokenization
WordPiece 110k
SentencePiece 250k
Compute [PF-days]
2
∼60b
Table 2: Model, data, and training setup for multilin-
gual models including French that we consider. Data
size is reported in gigatokens (GT), and compute in PF-
days (8.64 × 1019 FLOP).
PAGnol
nparams
nlayers
dmodel
nheads
C [PF-days]
rC
conv
rC
opt
S
124M
12
768
12
0.3
1,3
9,0
M
355M
24
1024
16
0.7
0,5
3,0
L
773M
36
1280
20
2
0,4
2,5
XL
1.5B
48
1600
25
3
0,2
1,3
Table 3: Model and training budgets for PAGnol. All
models are trained on a single epoch of our 32GT
CCNet-curated data.
C is the compute budget used
for the training of the model. rC
opt is the ratio between
C and Copt, the optimal compute budget derived from
scaling laws. rC
conv is the ratio between C and Cconv, the
compute budget derived from scaling laws to train the
model to convergence.
4.2
Model speciﬁcation
PAGnol is a decoder-only autoregressive trans-
former, reproducing the architectural choices of
GPT-3, with up to 1.5 billions parameters.. We
evaluate four model sizes: small, medium, large,
and extra-large, with architectures detailed in Table
3. We use a context size of 1,024 tokens for the
S, M and L models. The XL uses a context size
of 2,048, the largest at release for a French model.
Additionally, we use Rotary Embeddings (Su et al.,
2021) in place of Learned Positional Embeddings
for the XL model, since they provide much better
training stability at the billion parameters regime.
4.3
Pre-training
Training objective.
We use an autoregressive
language modelling objective, where the model
learns to predict the next word in a sentence. To im-
prove efﬁciency, we always ﬁll the context with as
much text at possible, and inform the model about
separate documents through the <SEP> token.
Optimization.
We use the Adam optimizer
(Kingma and Ba, 2014) with a warmup followed
by cosine decay learning rate schedule. We ﬁnd
that proper initialization is key to training stability,
and reproduce the setup effectively implemented by
Megatron-LM (Shoeybi et al., 2019). We initialize
all weights with a normal distribution N(0, 0.02)
and scale the weights under the residual layers by
1/p2nlayers. We tune hyperparameters over 10k
step ﬁrst, and pick the set with the best train per-
plexity.
Distributed training.
All training runs were per-
formed on the public GENCI supercomputer Jean
Zay, on nodes with 4x or 8x V100 32GB and a
100Gb/s interconnect. We built our own GPT im-
plementation from scratch in PyTorch (Paszke et al.,
2019), leveraging FairScale for distributed training
(Baines et al., 2021).
Models up to PAGnol-L can be trained using
simple distributed data parallelism (DDP). How-
ever, PAGnol-XL does not ﬁt in 32GB of memory.
We use optimizer and model state sharding, along
with activation checkpointing and CPU ofﬂoading
to ﬁt the model in memory. This results in a setup
similar to ZeRO-3 (Rajbhandari et al., 2021). It
is beneﬁcial to train even small models with this

--- Page 5 ---

setup, as it allows for a larger batch size, and sig-
niﬁcantly higher GPU throughput.
PAGnol
nparams
fr-wiki
FTB: whole
(train/val/test)
S
124M
43.38
23.87
(23.90, 24.38, 23.34)
M
355M
37.46
20.90
(20.92, 21.59, 20.46)
L
773M
34.81
19.97
(19.88, 21.19, 20.02)
XL
1.5B
28.85
16.18
(16.11, 16.67, 16.40)
Table 4: Validation perplexity on fr-wiki and on the
whole French TreeBank (FTB) for PAGnol models af-
ter 1 epoch of training on 30GT of CCNet.
Perplexity.
We report ﬁnal validation perplexity
after 1 epoch over 30GT in Table 4. We use the
the ofﬁcial 2019 French Wikipedia dumps and the
French TreeBank dataset (Abeillé et al., 2003) in
its SPMRL instance (Seddah et al., 2013) as our
validation sets. Because we are running all models
for a single epoch on our data, there are limited
risks of overﬁtting and memorization.
Scaling law for PAGnol models
We ﬁt a scaling
law with the same functional form of (Kaplan et al.,
2020), that is the following power law:
L =
 k
C
α
where L is the validation loss of PAGnol models
trained on CCNet, k is a constant, C is the compute
in PF-days, and α is the scaling exponent. The ﬁt
is performed in log-log, and constrained to remain
under the efﬁcient frontier, using cvxpy (Agrawal
et al., 2018). We exclude the L and XL models
from the ﬁt: due to the HPC environment, the train-
ing was performed in multiple splits. At restart, the
optimizer state is not necessarily available, gener-
ating artefacts in the training and validation curves.
Additionally, the use of Rotary Embeddings for the
XL model would affect the scaling, and make it in-
comparable with the English models. We therefore
trained two smaller models, an XXS and an XS,
following the same architectural decisions of the
larger ones, on the same datasets, and used these
to ﬁt a scaling law. We ﬁnd a scaling exponent
α = −0.036 for the French language, to compare
to the −0.050 for the English language from (Ka-
plan et al., 2020). With the relatively important
caveats that we are using different datasets, code-
base, and hardware, it appears that French is less
compute efﬁcient than English, and that for a same
improvement in validation loss, therefore we need
to spend more compute for French than for English.
10
4
10
3
10
2
10
1
Compute (PF-days)
3.5
4.0
4.5
5.0
5.5
6.0
6.5
Test Loss
XXSmall
XSmall
Small
Medium
3.40 C
0.036
Figure 1: Scaling law relative to the compute for PAG-
nol models from XXS to M. We do not include L and
XL: the interrupted nature of the training due to the
HPC environment and the choice of Rotary Embed-
dings for the XL pollute validation curves with arte-
facts that negatively affect the quality of the ﬁt.
The increase morphological complexity of French
when compared to English (Seddah et al., 2010)
and its, in average, longer sentences could be a
factor explaining this discrepancy.
5
Inﬂuence of the pre-training data
Existing French models (CamemBERT, FlauBERT,
BARThez) have been trained on datasets based on
a simple ﬁltering pipeline. A fastText classiﬁer is
used to isolate content in French, deduplication is
applied, and noisy content (phone numbers, code,
etc.) is removed. While this has been sufﬁcient for
pre-training encoder-only models and sequence-to-
sequence models, the lack of quality control may
be an issue for free-form generation with a decoder-
only model such as PAGnol. Moreover, recent work
on the OSCAR dataset (used by CamemBERT) has
found that it may contain up to 5% of non-linguistic
content, or content in the wrong language, and
0.5% of explicit content for the French language
(Caswell et al., 2021).
We initially pre-trained PAGnol on the OSCAR
dataset, and while experimenting with the model,
we observed the model generated offensive and
explicit content, even when not prompted for it.
For instance, the prompt Bonjour je suis (Hello I
am) often resulted in pornographic content, despite
being rather naive. This motivated our choice to
switch to CCNet instead. For research purposes,
we release the small and medium models trained
on OSCAR. In future iterations of this document,
we will provide a more detailed investigation of
the content generated by PAGnol-CCNet and by
PAGnol-OSCAR.

--- Page 6 ---

6
End-task performance
6.1
Discriminative tasks: FLUE
We evaluate our models on the Sentence Classiﬁca-
tion task of the FLUE evaluation setup (Le et al.,
2019). The task is a binary classiﬁcation problem
on reviews of Books, Music and DVD taken from
the Amazon website. Each review is assigned a
score from 1 to 5, and then labeled as "negative" if
the score is lower than 3 and "positive" otherwise.
We also evaluate our models on the paraphrasing
and natural language inference tasks (PAWS-X and
XNLI). PAWS-X consists in a binary classiﬁcation
task where the model has to identify whether
two sentences are semantically equivalent or not.
XNLI is instead a 3 class problem where we have
to determine if a premise contradicts, entails or
neither a given hypothesis. For the training, we add
a CLS token at the end of the review (but before
the EOS token). We then replace the projector at
the end of the model with a linear layer and use
the embedding of the CLS token to perform the
classiﬁcation.
Table 5 reports the test accuracy of the best
hyperparameter
conﬁguration
along
with
a
comparison with other French language models.
All models are ﬁne-tuned for 6 epochs, except
the medium OSCAR and the extra-large CC-100
which were trained respectively for 4 and 5 epochs.
For each model, we ﬁnetune the learning rate
and weight decay in the interval [10−6, 10−4]
and [0, 10−3] respectively. For the classiﬁcation
task, we use a cosine annealing scheduler that
decays down to 1/10 of the original learning
rate in 5 epochs (3 for the medium OSCAR and
4 for the extra-large CC-100). We additionally
checked if adding dropout with p = 0.1 could
improve the performance. For the PAWS-X and
XNLI tasks, we ﬁnetune the learning rate in the
interval [10−6, 10−4]. We use the cosine annealing
scheduler down to a learning rate equal to 1/10
of the original value (1/5 for the Small models)
over 9/40 Million tokens respectively. PAWS-X
training is over 2 epochs while XNLI training over
1. PAGnol models slightly underperform smaller
BERT models, while being better than multilingual
alternatives, and their GPTfr counterparts.
For
PAGnol, performance improves with size but
seems to saturate with the XL model, possibly
because we had to use a lower batch size to ﬁt
on the hardware for ﬁne-tuning.
Additionally,
while the generation quality of models trained on
OSCAR is noticeably worse, they perform as well
or better than the corresponding models trained on
CCNet on these discriminative tasks.
6.2
Generative task: FQuAD
FQuAD (d’Hoffschmidt et al., 2020) is a native
French question answering dataset, comprising
more than 25.000 questions fabricated by higher
education students from a set of Wikipedia arti-
cles, following the same philosophy as the English
dataset SQuAD (Rajpurkar et al., 2018). Given a
document di, a question qi and the corresponding
answer ai, the Question Answering task is casted
into this format:
"{di} Question: {qi} Réponse: {ai}"
where Réponse corresponds to Answer in French.
Given this input format, in a setup similar
to pretraining, the likelihood of the sequence
corresponding to the answer is maximized using
the cross entropy loss on the tokens corresponding
to the answer. We use the Adam optimizer and
ﬁnetune the learning rate and weight decay in the
interval [10−6, 10−4] and [0, 10−3]. The different
models were trained for 2 epochs.
As noted
by Radford et al. (2019), the performance of
autoregressive models is still worse than question
answering systems based on masked language
models. Indeed, we evaluated the ﬁnetuning of
OpenAI GPT-2 small and medium on SQuAD, and
obtained EM and F1 scores in the same range of
PAGnol on FQuAD (Table 7).
6.3
Generative task: OrangeSum
OrangeSum (Eddine et al., 2020b) is a summariza-
tion dataset, considered to be the French equiva-
lent of the XSum (Narayan et al., 2018). It is an
abstractive dataset containing summary of news
article from the "Orange Actu" website. Each ar-
ticle comes with a professionally-written title and
abstract. Hence, the dataset includes two tasks:
OrangeSum Title and OrangeSum Abstract. We
evaluate PAGnol on the latter.
Similarly to our setup for question answering,
given a news article ni and an abstract ai, we cast
the summarization task in this format:
"{ni} Summary: {ai}"

--- Page 7 ---

Model
Parameters
Books
Music
DVD
PAWS-X
XNLI
MultiFiT
Not Speciﬁed
91.25
89.55
93.40
-
-
mBERT
110/340 M*
86.15
86.90
86.65
89.30
76.9
mBART
610 M
93.40
93.13
93.10
89.70
81.07
BARThez
216 M
94.47
94.97
93.17
88.90
80.73
CamemBERT-BASE
110 M
92.30
94.85
93.00
90.14
81.20
CamemBERT-LARGE
335 M
95.47
96.00
95.37
91.83
85.33
Flaubert-BASE
138 M
93.10
92.45
94.10
89.49
80.60
Flaubert-LARGE
373 M
95.00
94.10
95.85
89.34
83.40
GPTfr-BASE
124 M
88.30
86.90
89.30
83.30
75.60
GPTfr-LARGE
1 B
91.60
91.40
92.60
86.30
77.90
PAGnol-S OSCAR
124 M
92.05
92.60
91.70
84.19
76.10
PAGnol-M OSCAR
355 M
94.40
94.90
94.30
87.44
79.46
PAGnol-S CC-100
124 M
92.00
93.00
91.65
87.19
75.67
PAGnol-M CC-100
355 M
94.40
95.20
93.70
89.14
79.00
PAGnol-L CC-100
773 M
94.65
95.25
94.00
90.70
81.48
PAGnol-XL CC-100
1.5 B
94.65
95.35
94.18
89.47
81.83
Table 5: Results on the FLUE Benchmark including classiﬁcation (Books, Music, DVD), paraphrasing (PAWS-X)
and natural language inference (XNLI) tasks. The best overall results are highlighted in bold, and the best results
for GPT models are underlined.
Model
EM
F1
CamemBERT-LARGE
82.1
92.2
CamemBERT-BASE
78.4
88.4
PAGnol-S OSCAR
31.7
52.8
PAGnol-M OSCAR
37.1
59.4
PAGnol-S CC-100
33.7
56.0
PAGnol-M CC-100
36.8
59.0
PAGnol-L CC-100
42.8
66.3
PAGnol-XL CC-100
44.4
68.5
Table 6: Question answering on FQuAD.
Model
Size
EM
F1
GPT
small
45.5
62.7
GPT
medium
50.8
68.1
Table 7: GPT-2 small and medium model performance
on SQuaD
We ﬁnetune our model on the crossentropy loss
computed only on the tokens of the produced sum-
mary. We optimize the learning rate and weight
decay in the same interval as FLUE, using the same
scheduler, and train for 4 epochs. We add a dropout
with p = 0.1 to improve the performance. We
evaluate the ﬁne-tuned model using greedy token
generation and the ROUGE metric. This task, more
geared towards generation, sees PAGnol-XL estab-
lish a new state of the art for summarization on
OrangeSum.
Model
Parameters
R-1
R-2
R-L
BARThez
216 M
31.44
12.77
22.23
PAGnol-S OSCAR
124 M
22.79
6.16
16.03
PAGnol-M OSCAR
355 M
24.89
7.87
17.78
PAGnol-S CC-100
124 M
26.47
9.49
17.12
PAGnol-M CC-100
355 M
28.20
10.80
20.79
PAGnol-L CC-100
773 M
28.12
11.05
20.81
PAGnol-XL CC-100
1.5 B
31.17
12.86
22.50
Table 8: Text summarization on the OrangeSum Ab-
stract task. Best results are highlighted in bold, and
second best are underlined.
7
Prompt Tuning
Human prompt engineering to extract good zero-
and few-shot performance for large language mod-
els has motivated research in prompt tuning: plac-
ing some random vectors in the input sequence
and optimizing their values, while keeping the pre-
trained model weights ﬁxed. The advantage of
this approach is that the model does not change,
and only the prompt is optimized. We follow the
approach in (Lester et al., 2021), and optimize a
certain number k of tokens in our soft prompt for
the three aforementioned tasks. The best hyper-
parameters per size per task have been selected
through a grid search for the value of k, learning
rate and dropout. In particular we performed a
grid search over k = {1, 5, 20, 35, 50}, learning
rate in {0.3, 0.1, 0.01, 0.001, 0.0005}, and dropout
values in {0, 0.01, 0.1}. We show the results for
FLUE, FQuAD, and OrangeSum in Tables 9, 10

--- Page 8 ---

and 11. We expected a smooth scaling in perfor-
mance with size and to progressively close the gap
with ﬁne-tuning performance, as shown by (Lester
et al., 2021), however this scaling slows signiﬁ-
cantly when we reach the XL model. We suspect a
bug in our implementation of prompt tuning with
Rotary Embeddings, causing the performance hit,
therefore we temporarily show the results for the
XL model in italic in this setting. This is a work in
progress and will be updated in a new release.
PAGnol
Books
Music
DVD
S
88.50
87.95
88.24
M
91.60
92.65
90.69
L
92.60
93.1
91.69
XL
92.50
93.25
92.14
Table 9: Prompt Tuning performance for sentence clas-
siﬁcation (CLS).
PAGnol
EM
F1
S
0.243
0.427
M
0.320
0.561
L
0.365
0.526
XL
0.403
0.450
Table 10: Prompt Tuning performance for question an-
swering on fQuad.
PAGnol
R-1
R-2
R-L
S
24.54
8.98
18.45
M
27.80
10.56
20.29
L
28.25
11.05
21.03
XL
28.72
11.08
20.89
Table 11: Prompt tuning performance for text summa-
rization on OrangeSum.
8
Discussion
Without fear of aligning an overused cliché, the
release of large language neural models have not
only revolutionized the NLP ﬁeld by bringing a ma-
jor leap in performance in almost every tasks they
were applied to, they crucially changed the per-
ception of the risks of their potential misuse. The
point is that this dramatic boost of performance has
led the ﬁeld to rely on the capacity of those large
models to transfer their, in layman’s terms, “knowl-
edge” to other tasks via various transfer learning
modalities. Yet, with this transfer, the potential data
biases inherent to large corpus collection used for
pre-training are also susceptible to appear. Gehman
et al. (2020) thoroughly demonstrated that all gen-
erative language models they tested (from GPT1
(Radford et al., 2018) trained on Book Corpus only
to GPT3 (Brown et al., 2020) and CTRL (Keskar
et al., 2019) trained on various corpora, including
user-generated content and web-crawled data sets)
were capable of producing toxic output in speciﬁc
conditionsand presented different ways of allevi-
ating this behaviour. Having been pre-trained on
Common Crawl-based corpora, our models are cer-
tainly not immune from toxic content generation.
Gehman et al. (2020) explored two main ways
to ﬁlter toxic outputs, one being based on the pur-
suing the pretraining on less toxic data sets or on
toxicity-annotated data set; the other focusing on
the alteration of the decoding strategy. Krause et al.
(2020) proposed to guide the output with smaller
language models. Given the interest in generative
models, this is an active line of research that we are
currently pursuing.
More generally, the question of knowing whether
the pre-training data should be curated more or
should the model output, depending on the down-
stream application in sight, be debiased, or ﬁltered,
directly is still the object of vivid debates among
the community (Bender et al., 2021; Goldberg,
2021), while of course there is an agreement to-
ward responsible use of such technology.
In this aspect, the release of a GPT-generated
text detector by Antoun et al. (2021b) along their
Arabic GPT2 model is an interesting step toward
this direction.
Regarding the environmental aspects of this
model, our model pretraining experiments con-
sumed about 62k gpu hours from the Jean Zay
HPC cluster. Being based in France, its energy mix
is made of nuclear (65-75%), 20% renewable and
the remaining with gas (or more rarely coal when
imported from abroad) (S.Requena, Dir. of Jean
Zay, P.C).
Regarding the performance of our models which
almost constantly outperform their closest French
counterparts, the GPTfr models (Simoulin and
Crabbé, 2021), one explaining factor could be
the size of our pretraining data set (30B token vs
3B). Given our computing limitation, we choose
from the beginning to use an experimental proto-
col as comparable as possible to the one used for
the CamemBERT model evaluation (Martin et al.,
2019), it would of course be interesting to perform
a head to head comparison with the GPTfr model.
In terms of raw performance, it has been constantly
reported that GPT-based models on the billion pa-

--- Page 9 ---

rameter scale provide inferior performance when
compared to their “regular” transformer counter-
parts in classic ﬁne-tuning scenarios, our results
conﬁrm this for French as well while highlighting
the interest of our models in generation-oriented
scenarios (such as text summarization where Pag-
nolXL establishes a new state of the art for French).
As for English (Lester et al., 2021), our encourag-
ing preliminary prompt-tuning results suggest that
this approach is promising and could be a way to
close this performance gap.
9
Conclusion
We presented the Pagnol model collection, the ﬁrst
released large scale generative model for French3,
to date the largest neural language model for
French. Trained on the CCnet corpus, we used scal-
ing laws to inform our training setup, resulting in an
optimal use of our training budget. The evaluation
of our models on various end-tasks demonstrated
ﬁrst that the CCnet corpus was a better choice than
the Oscar French instance when used for genera-
tion; second, they showed that our models provide
the same range of performance than their English
counterparts and established a new state of the art
for summarization of French on OrangeSum. Pag-
nolXL and our smaller models are available on
https://lair.lighton.ai/pagnol/.
Acknowledgments
This work was granted access to the HPC resources
of IDRIS under the allocation 2020-AD011012024
made by GENCI, enabling us to use the Jean
Zay supercomputer. We thank Stéphane Réquena
and the support team for their valuable help. We
also acknowledge Louis Martin for helping us re-
producing the CamemBERT settings for CCNet.
Djamé Seddah was partly funded by the French
Research National Agency via the ANR project
ParSiTi (ANR-16-CE33-0021).
References
Anne Abeillé, Lionel Clément, and François Toussenel.
2003. Building a treebank for french. In Treebanks,
pages 165–187. Springer.
Akshay Agrawal, Robin Verschueren, Steven Diamond,
and Stephen Boyd. 2018.
A rewriting system for
3Released on May 4th, 2021. https://twitter.co
m/LightOnIO/status/1389579858754293761?
s=20
convex optimization problems. Journal of Control
and Decision, 5(1):42–60.
Wissam Antoun, Fady Baly, and Hazem Hajj. 2021a.
AraGPT2: Pre-trained transformer for Arabic lan-
guage generation. In Proceedings of the Sixth Ara-
bic Natural Language Processing Workshop, pages
196–207, Kyiv, Ukraine (Virtual). Association for
Computational Linguistics.
Wissam Antoun, Fady Baly, and Hazem M. Hajj.
2021b. Aragpt2: Pre-trained transformer for arabic
language generation. ArXiv, abs/2012.15520.
Mandeep Baines, Shruti Bhosale, Vittorio Caggiano,
Naman Goyal, Siddharth Goyal, Myle Ott, Ben-
jamin Lefaudeux, Vitaliy Liptchinsky, Mike Rabbat,
Sam Sheiffer, Anjali Sridhar, and Min Xu. 2021.
Fairscale: A general purpose modular pytorch li-
brary for high performance and large scale train-
ing.
https://github.com/facebookres
earch/fairscale.
Emily M. Bender, Timnit Gebru, Angelina McMillan-
Major, and Shmargaret Shmitchell. 2021.
On the
dangers of stochastic parrots: Can language models
be too big? Proceedings of the 2021 ACM Confer-
ence on Fairness, Accountability, and Transparency.
Tom B Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, et al. 2020. Language models are few-shot
learners. arXiv preprint arXiv:2005.14165.
Isaac Caswell, Julia Kreutzer, Lisa Wang, Ahsan Wa-
hab, Daan van Esch, Nasanbayar Ulzii-Orshikh, Al-
lahsera Tapo, Nishant Subramani, Artem Sokolov,
Claytone Sikasote, et al. 2021.
Quality at a
glance:
An audit of web-crawled multilingual
datasets. arXiv preprint arXiv:2103.12028.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2018. Bert: Pre-training of deep
bidirectional transformers for language understand-
ing. arXiv preprint arXiv:1810.04805.
Martin d’Hoffschmidt, Wacim Belblidia, Tom Brendlé,
Quentin Heinrich, and Maxime Vidal. 2020. Fquad:
French question answering dataset. arXiv preprint
arXiv:2002.06071.
Moussa Kamal Eddine,
Antoine J-P Tixier,
and
Michalis Vazirgiannis. 2020a. Barthez: a skilled pre-
trained french sequence-to-sequence model. arXiv
preprint arXiv:2010.12321.
Moussa Kamal Eddine,
Antoine J-P Tixier,
and
Michalis Vazirgiannis. 2020b.
Barthez: a skilled
pretrained
french
sequence-to-sequence
model.
arXiv preprint arXiv:2010.12321.
Samuel Gehman, Suchin Gururangan, Maarten Sap,
Yejin Choi, and Noah A. Smith. 2020.
RealToxi-
cityPrompts: Evaluating neural toxic degeneration
in language models. In Findings of the Association

--- Page 10 ---

for Computational Linguistics: EMNLP 2020, pages
3356–3369, Online. Association for Computational
Linguistics.
Yoav Goldberg. 2021. A criticism of "on the dangers of
stochastic parrots: Can language models be too big".
https://gist.github.com/yoavg/9fc9be2f98b47c189a513573d902fb27.
Tom Henighan, Jared Kaplan, Mor Katz, Mark Chen,
Christopher Hesse, Jacob Jackson, Heewoo Jun,
Tom B Brown, Prafulla Dhariwal, Scott Gray, et al.
2020.
Scaling laws for autoregressive generative
modeling. arXiv preprint arXiv:2010.14701.
Jeremy Howard and Sebastian Ruder. 2018.
Univer-
sal language model ﬁne-tuning for text classiﬁcation.
arXiv preprint arXiv:1801.06146.
Armand Joulin, Edouard Grave, Piotr Bojanowski, and
Tomas Mikolov. 2017.
Bag of tricks for efﬁcient
text classiﬁcation. In Proceedings of the 15th Con-
ference of the European Chapter of the Association
for Computational Linguistics: Volume 2, Short Pa-
pers, pages 427–431. Association for Computational
Linguistics.
Jared Kaplan,
Sam McCandlish,
Tom Henighan,
Tom B Brown, Benjamin Chess, Rewon Child, Scott
Gray, Alec Radford, Jeffrey Wu, and Dario Amodei.
2020.
Scaling laws for neural language models.
arXiv preprint arXiv:2001.08361.
Nitish Shirish Keskar, Bryan McCann, Lav R. Varsh-
ney, Caiming Xiong, and Richard Socher. 2019.
Ctrl: A conditional transformer language model for
controllable generation. ArXiv, abs/1909.05858.
Boseop Kim,
HyoungSeok Kim,
Sang-Woo Lee,
Gichang Lee, Donghyun Kwak, Dong Hyeon Jeon,
Sunghyun Park, Sungju Kim, Seonhoon Kim, Dong-
pil Seo, et al. 2021. What changes can large-scale
language models bring? intensive study on hyper-
clova: Billions-scale korean generative pretrained
transformers. arXiv preprint arXiv:2109.04650.
Diederik P Kingma and Jimmy Ba. 2014. Adam: A
method for stochastic optimization. arXiv preprint
arXiv:1412.6980.
Ben Krause, Akhilesh Deepak Gotmare, Bryan Mc-
Cann, Nitish Shirish Keskar, Shaﬁq R. Joty, Richard
Socher, and Nazneen Rajani. 2020.
Gedi: Gen-
erative discriminator guided sequence generation.
ArXiv, abs/2009.06367.
Hang Le, Loïc Vial, Jibril Frej, Vincent Segonne, Max-
imin Coavoux, Benjamin Lecouteux, Alexandre Al-
lauzen, Benoît Crabbé, Laurent Besacier, and Di-
dier Schwab. 2019.
Flaubert: Unsupervised lan-
guage model pre-training for french. arXiv preprint
arXiv:1912.05372.
Brian Lester, Rami Al-Rfou, and Noah Constant. 2021.
The power of scale for parameter-efﬁcient prompt
tuning.
Mike
Lewis,
Yinhan
Liu,
Naman
Goyal,
Mar-
jan Ghazvininejad, Abdelrahman Mohamed, Omer
Levy, Ves Stoyanov, and Luke Zettlemoyer. 2019.
Bart: Denoising sequence-to-sequence pre-training
for natural language generation, translation, and
comprehension. arXiv preprint arXiv:1910.13461.
Xiang Lisa Li and Percy Liang. 2021.
Preﬁx-
tuning: Optimizing continuous prompts for genera-
tion. arXiv preprint arXiv:2101.00190.
Antoine Louis. 2020. BelGPT-2: a GPT-2 model pre-
trained on French corpora. https://github.c
om/antoiloui/belgpt2.
Louis Martin, Benjamin Muller, Pedro Javier Ortiz
Suárez, Yoann Dupont, Laurent Romary, Éric Ville-
monte de la Clergerie, Djamé Seddah, and Benoît
Sagot. 2019. Camembert: a tasty french language
model. arXiv preprint arXiv:1911.03894.
Tomas Mikolov, Kai Chen, Greg Corrado, and Jef-
frey Dean. 2013.
Efﬁcient estimation of word
representations in vector space.
arXiv preprint
arXiv:1301.3781.
Shashi Narayan, Shay B. Cohen, and Mirella Lapata.
2018. Don’t give me the details, just the summary!
Topic-aware convolutional neural networks for ex-
treme summarization. In Proceedings of the 2018
Conference on Empirical Methods in Natural Lan-
guage Processing, Brussels, Belgium.
Pedro Javier Ortiz Suárez, Laurent Romary, and Benoît
Sagot. 2020. A monolingual approach to contextual-
ized word embeddings for mid-resource languages.
In Proceedings of the 58th Annual Meeting of the
Association for Computational Linguistics, pages
1703–1714, Online. Association for Computational
Linguistics.
Adam Paszke, Sam Gross, Francisco Massa, Adam
Lerer, James Bradbury, Gregory Chanan, Trevor
Killeen, Zeming Lin, Natalia Gimelshein, Luca
Antiga, et al. 2019. Pytorch: An imperative style,
high-performance deep learning library. Advances
in neural information processing systems, 32:8026–
8037.
Jeffrey Pennington, Richard Socher, and Christopher D
Manning. 2014. Glove: Global vectors for word rep-
resentation. In Proceedings of the 2014 conference
on empirical methods in natural language process-
ing (EMNLP), pages 1532–1543.
Matthew E Peters, Mark Neumann, Mohit Iyyer, Matt
Gardner, Christopher Clark, Kenton Lee, and Luke
Zettlemoyer. 2018. Deep contextualized word repre-
sentations. arXiv preprint arXiv:1802.05365.
Alec Radford, Karthik Narasimhan, Tim Salimans, and
Ilya Sutskever. 2018.
Improving language under-
standing by generative pre-training.

--- Page 11 ---

Alec Radford, Jeffrey Wu, Rewon Child, David Luan,
Dario Amodei, and Ilya Sutskever. 2019. Language
models are unsupervised multitask learners. OpenAI
blog, 1(8):9.
Colin Raffel, Noam Shazeer, Adam Roberts, Kather-
ine Lee, Sharan Narang, Michael Matena, Yanqi
Zhou, Wei Li, and Peter J. Liu. 2020.
Exploring
the limits of transfer learning with a uniﬁed text-to-
text transformer. Journal of Machine Learning Re-
search, 21(140):1–67.
Samyam Rajbhandari, Olatunji Ruwase, Jeff Rasley,
Shaden Smith, and Yuxiong He. 2021. Zero-inﬁnity:
Breaking the gpu memory wall for extreme scale
deep learning. arXiv preprint arXiv:2104.07857.
Pranav Rajpurkar, Robin Jia, and Percy Liang. 2018.
Know what you don’t know: Unanswerable ques-
tions for squad. arXiv preprint arXiv:1806.03822.
Stefan Schweter. 2020. German gpt-2 model.
Djamé Seddah, Grzegorz Chrupała, Özlem Çetino˘glu,
Josef van Genabith, and Marie Candito. 2010.
Lemmatization and lexicalized statistical parsing of
morphologically-rich languages: the case of French.
In Proceedings of the NAACL HLT 2010 First Work-
shop on Statistical Parsing of Morphologically-Rich
Languages, pages 85–93, Los Angeles, CA, USA.
Association for Computational Linguistics.
Djamé Seddah, Reut Tsarfaty, Sandra Kübler, Marie
Candito,
Jinho D. Choi,
Richárd Farkas,
Jen-
nifer Foster, Iakes Goenaga, Koldo Gojenola Gal-
letebeitia, Yoav Goldberg, Spence Green, Nizar
Habash, Marco Kuhlmann, Wolfgang Maier, Joakim
Nivre, Adam Przepiórkowski, Ryan Roth, Wolfgang
Seeker, Yannick Versley, Veronika Vincze, Marcin
Woli´nski, Alina Wróblewska, and Eric Villemonte
de la Clergerie. 2013.
Overview of the SPMRL
2013 shared task: A cross-framework evaluation of
parsing morphologically rich languages. In Proceed-
ings of the Fourth Workshop on Statistical Parsing of
Morphologically-Rich Languages, pages 146–182,
Seattle, Washington, USA. Association for Compu-
tational Linguistics.
Mohammad Shoeybi, Mostofa Patwary, Raul Puri,
Patrick LeGresley, Jared Casper, and Bryan Catan-
zaro. 2019. Megatron-lm: Training multi-billion pa-
rameter language models using model parallelism.
arXiv preprint arXiv:1909.08053.
Antoine Simoulin and Benoit Crabbé. 2021.
Un
modèle transformer génératif pré-entrainé pour le _
français.
In Traitement Automatique des Langues
Naturelles, pages 245–254. ATALA.
Jianlin Su, Yu Lu, Shengfeng Pan, Bo Wen, and Yun-
feng Liu. 2021. Roformer: Enhanced transformer
with rotary position embedding.
arXiv preprint
arXiv:2104.09864.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz
Kaiser, and Illia Polosukhin. 2017. Attention is all
you need. Advances in neural information process-
ing systems, 30:5998–6008.
Jason Wei, Maarten Bosma, Vincent Y Zhao, Kelvin
Guu, Adams Wei Yu, Brian Lester, Nan Du, An-
drew M Dai, and Quoc V Le. 2021. Finetuned lan-
guage models are zero-shot learners. arXiv preprint
arXiv:2109.01652.
Guillaume Wenzek, Marie-Anne Lachaux, Alexis Con-
neau, Vishrav Chaudhary, Francisco Guzmán, Ar-
mand Joulin, and Édouard Grave. 2020. Ccnet: Ex-
tracting high quality monolingual datasets from web
crawl data. In Proceedings of The 12th Language
Resources and Evaluation Conference, pages 4003–
4012.
Wei Zeng,
Xiaozhe Ren,
Teng Su,
Hui Wang,
Yi Liao, Zhiwei Wang, Xin Jiang, ZhenZhang Yang,
Kaisheng Wang, Xiaoda Zhang, et al. 2021. Pangu-
α: Large-scale autoregressive pretrained chinese lan-
guage models with auto-parallel computation. arXiv
preprint arXiv:2104.12369.

--- Page 12 ---

PAGnol OSCAR
S
M
Shared Emb.
False
True
(β1, β2)
(0.9, 0.95)
(0.9, 0.999)
LRmax-min
6e-4 – 6e-5
3e-4 – 3e-5
Batch Size
12
5
Table 12: Hyperparameters differences between the
Small and Medium training runs on OSCAR.
PAGnol
GPU-hours
S
480
M
1,920
L
6,720
XL
5,200
Total
14,320
Table 13: The Large model required more GPU-hours
than expected, however several optimizations allowed
us to perform the training of the XL model with a
smaller budget.
A
Pretraining details
In this section we provide more details on the hy-
perparameters used to train PAGnol models.
Models trained on OSCAR
The Small and
Medium trained on OSCAR use the Adam opti-
mizer with ε = 1e −8, with 2000 warmup steps,
and a cosine decay learning rate schedule over
325000 steps. Additionally, we use grad clipping
with a value of 1.0, and set the dropout probabil-
ity p = 0.1. We do not use weight decay. The
Small was trained on a single node with 8 NVIDIA
V100, and the Medium on two such nodes. In both
cases we use the distributed data parallel (DDP)
paradigm, with mixed precision. We show differ-
ences in hyperparameters between the SmallOSCAR
and MediumOSCAR in Table 12
Models trained on CC-100
We use the Adam
optimizer with ε = 1e −8 and warmup and cosine
learning rate decay schedule also for the S, M, L,
and XL models trained on CC-100. We set dropout
probability p = 0.1 and no weight decay for all
models. Small, Medium, and Large are trained with
DDP, and use tied embeddings, gradient clipping
at 1.0, (β1, β2) = (0.9, 0.999). These are trained
on respectively 1, 2 and 4 nodes with 8 NVIDIA
V100s. The XL model uses a smaller value for
gradient clipping at 0.75, a larger context size at
2048, and different (β1, β2) = (0.9, 0.95) for the
Adam optimizer. This model is trained on 10 nodes
with 4 NVIDIA V100s each. Further differences
between the hyperparameters of the training runs
are shown in Table 14.
Budget in GPU-Hours
We report in Table 13
the budget in GPU-hours needed to train each
model, and the total budget.
B
Samples from PAGnol XL
We provide in Tables 15, 16, 17, and 18 some ex-
amples of completions given by PAGnol XL when
prompted with different text.

--- Page 13 ---

PAGnol CC-100
S
M
L
XL
LRmax-min
5e-4–5e-5
3e-4–3e-5
2.5e-4–2.5e-5
2.5e-4–2.5e-5
Warmup Steps
5000
5000
5000
3600
Decay Steps
400,000
500,000
100,000
400,000
Batch Size
10
5
1
4
Table 14: Hyperparameters differences between Small, Medium, Large and Extra-Large training runs on CC-100.
Prompt
Bonjour Madame, est-ce que
Generation
le château de la Noue se trouve dans la région ? Est-ce que les
gens s’y déplacent en calèche ? Je me rends dans ce coin du
monde quelques jours au mois de mai, c’est mon anniversaire.
Est-ce que vous pouvez me conseiller quelque chose ? Merci
beaucoup. Françoise Vernin.
Table 15: Completion for a random French sentence.
Prompt
Produis un horoscope étant donné un signe astrologique. ———
- Bélier: Des nuages sur votre Ciel ! En couple, des moments de
désaccord sont possibles. Vénus pourrait en effet compliquer
vos relations avec votre conjoint... ———- Taureau: Vénus
donnera la priorité à vos amours ! En couple, les événements
en cours vous seront favorables à court ou long terme, celui
qui vous aime... ———- Lion: Vos amours devraient vous
combler. En couple, Jupiter vous offrira le cocooning har-
monieux dont vous rêvez. Célibataire, inutile de papillonner:...
———- Vierge: Ambiance astrale morose. En couple, vous
serez probablement tenté de chercher un dérivatif à l’ennui qui
naît de l’habitude et du train-train... ———- Capricorne:
Generation
Il est temps de changer de cap! En couple, Vénus s’opposera
à Mars et Mercure. Ces deux planètes vous réjouiront par
leur dynamisme. Mais, en tant que conjointe, vous serez plus
fatiguée que jamais.
Table 16: Completion for an oroscope found in the magazine ELLE.
Prompt
Quelque 180 000 nouveaux parents devraient en bénéﬁcier d’ici
au mois d’août 2022 : le gouvernement prévoit de distribuer
des « bébés box » par l’intermédiaire des maternités à partir de
février 2022. De quoi s’agit-il ?
Generation
De boîtes contenant un kit composé de plusieurs couches,
quelques vêtements et accessoires adaptés à l’âge et au sexe de
l’enfant. Certains parents ont pu déjà recevoir ces kits grâce
à une souscription mensuelle proposée par les enseignes de la
grande distribution. L’offre a immédiatement rencontré un vif
succès, des petits comme des grands, qui jouent à la fois un rôle
de « maman » et de « papa » mais surtout avec ce budget...
Table 17: Completion for the beginning of a news article on the "« Bébé box » pour jeunes parents" from Le Monde
website on the 14th of October 2021.

--- Page 14 ---

Prompt
La septième réalisation du monumental Bong Joon Ho est
fréquemment présentée comme une critique acerbe des inégal-
ités qui minent la société coréenne. La lutte, d’abord larvée et
de plus en plus patente, qui oppose deux familles aux extrêmes
de l’échelle sociale semble étayer cette vision.
Generation
Il ne s’agira donc pas de confronter les puissants à leurs limites
mais plutôt de s’interroger sur le mensonge et la tromperie, les
jeux et l’alcool, les privilèges et la corruption. Pour en arriver
à cette conclusion, on n’a cependant pas la prétention de se
demander comment une famille moyenne aisée pourrait être en
mesure de maintenir les apparences dans un pays où il n’y a
pas d’eau, ni de gaz, ni d’électricité. En tant que spectateur,
nous suivons ce cadre tendu, ce huis clos. Puis, très vite, les
événements s’ accélèrent, la mécanique bien huilée du thriller
se met en marche pour un ﬁnal imprévisible.
Table 18: Completion for the beginning of a critique on Parasite from the website Sens Critique. Accessed on the
14th of October 2021.

```
