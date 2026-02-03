---
title: "Large AI Models in Health Informatics - PDF Extract"
source_pdf: "2023-Qiu-Large AI Models in Health Informatics.pdf"
pages: 15
extracted_at: "2026-01-24T17:05:17.105122"
---

# PDF Extract: Large AI Models in Health Informatics

**Source PDF:** 2023-Qiu-Large AI Models in Health Informatics.pdf
**Total Pages:** 15

---

## Content

```
--- Page 1 ---

arXiv:2303.11568v2  [cs.AI]  24 Sep 2023
1
Large AI Models in Health Informatics:
Applications, Challenges, and the Future
Jianing Qiu, Lin Li, Jiankai Sun, Jiachuan Peng, Peilun Shi,
Ruiyang Zhang, Yinzhao Dong, Kyle Lam, Frank P.-W. Lo, Bo Xiao,
Wu Yuan, Senior Member, IEEE, Ningli Wang, Dong Xu, and Benny Lo, Senior Member, IEEE
Abstract—Large
AI
models,
or
foundation models,
are models recently emerging with massive scales both
parameter-wise and data-wise, the magnitudes of which
can reach beyond billions. Once pretrained, large AI mod-
els demonstrate impressive performance in various down-
stream tasks. A prime example is ChatGPT, whose capa-
bility has compelled people’s imagination about the far-
reaching inﬂuence that large AI models can have and
their potential to transform different domains of our lives.
In health informatics, the advent of large AI models has
brought new paradigms for the design of methodologies.
The scale of multi-modal data in the biomedical and health
domain has been ever-expanding especially since the com-
munity embraced the era of deep learning, which pro-
vides the ground to develop, validate, and advance large
AI models for breakthroughs in health-related areas. This
article presents a comprehensive review of large AI models,
from background to their applications. We identify seven
key sectors in which large AI models are applicable and
might have substantial inﬂuence, including 1) bioinformat-
ics; 2) medical diagnosis; 3) medical imaging; 4) medical
Jianing Qiu is with the Department of Computing, Imperial College
London, U.K., and he is also with the Department of Biomedical Engi-
neering, The Chinese University of Hong Kong, Hong Kong SAR. He
was with Precision Robotics (Hong Kong) Ltd., Hong Kong SAR (e-mail:
jianing.qiu17@imperial.ac.uk).
Lin Li is with the Department of Informatics, King’s College London,
U.K. (e-mail: lin.3.li@kcl.ac.uk).
Jiankai Sun is with the School of Engineering, Stanford University,
USA (e-mail: jksun@stanford.edu).
Jiachuan Peng is with the Department of Engineering Science, Uni-
versity of Oxford, U.K. (e-mail: jiachuan.peng@seh.ox.ac.uk).
Peilun Shi and Wu Yuan are with the Department of Biomedical
Engineering, The Chinese University of Hong Kong, Hong Kong SAR
(e-mails: peilunshi@cuhk.edu.hk and wyuan@cuhk.edu.hk).
Ruiyang Zhang is with Precision Robotics (Hong Kong) Ltd., Hong
Kong SAR (e-mail: r.zhang@prhk.ltd).
Yinzhao Dong is with the Faculty of Engineering, The University of
Hong Kong, Hong Kong SAR (e-mail: dongyz@connect.hku.hk).
Kyle Lam is with the Department of Surgery and Cancer, Imperial
College London, U.K. (e-mail: k.lam@imperial.ac.uk).
Frank
P.-W.
Lo
and
Bo
Xiao
are
with
the
Hamlyn
Cen-
tre for Robotic Surgery, Imperial College London, U.K. (e-mails:
po.lo15@imperial.ac.uk and b.xiao@imperial.ac.uk).
Ningli Wang is with Beijing Tongren Eye Center, Beijing Tongren
Hospital, Capital Medical University, and also with Beijing Ophthal-
mology & Visual Sciences Key Laboratory, Beijing, China (e-mail: wn-
ingli@vip.163.com)
Dong Xu is with the Department of Electrical Engineering and Com-
puter Science, and the Christopher S. Bond Life Sciences Center,
University of Missouri, USA (e-mail: xudong@missouri.edu).
Benny Lo is with the Facualty of Medicine, Imperial College London,
U.K., and he is also with Precision Robotics (Hong Kong) Ltd., Hong
Kong SAR (e-mail: benny.lo@imperial.ac.uk).
Corresponding authors: Wu Yuan and Benny Lo
Fig. 1: Number of publications related to ChatGPT and SAM
in medical and health areas. Statistics were queried from
Google Scholar with the keywords “Medical ChatGPT” or
“Medical Segment Anything”, and the last entry was 31-th
Aug. 2023. From April to August, each month, there were over
200 publications about ChatGPT in medicine and healthcare.
informatics; 5) medical education; 6) public health; and 7)
medical robotics. We examine their challenges, followed by
a critical discussion about potential future directions and
pitfalls of large AI models in transforming the ﬁeld of health
informatics.
Index
Terms— artiﬁcial
intelligence;
bioinformatics;
biomedicine; deep learning; foundation model; health
informatics; healthcare; medical imaging
I. INTRODUCTION
T
HE introduction of ChatGPT [1] has triggered a new
wave of development and deployment of Large AI Mod-
els (LAMs) recently. As shown in Fig. 1, ChatGPT and
the phenomenal Segment Anything Model (SAM) [2] have
sparked active research in medical and health sectors since
their initial launch. Although groundbreaking, the AI commu-
nity has in fact started creating LAMs much earlier, and it was
the seminal work introducing the Transformer model [3] back
in 2017 that accelerated the creation of LAMs.

--- Page 2 ---

2
Fig. 2: The key features of large AI models lie in the following four aspects: 1) increased size (e.g., for large language models
(LLMs), the number of parameters is often billions); 2) trained with large-scale data (e.g., for LLMs, the data can contain
trillions of tokens; and for large vision models (LVMs), the data can contain billions of images); 3) able to process data of
multiple modalities; and 4) can perform well across multiple downstream tasks, especially on zero-, one-, and few-shot tasks.
The recent advances in data science and AI algorithms have
endowed LAMs with strengthened generative and reasoning
capabilities, as well as generalist intelligence across multiple
tasks with impressive zero- and few-shot performance, sig-
niﬁcantly distinguishing them from early deep models. For
example, when asked for medical advice, ChatGPT, based
on GPT-4 [4], demonstrates the capability of recalling prior
conversation and being able to contextualize the user’s past
medical history before answering, showing a new level of
intelligence way beyond that of a simple symptom checker [5].
One notable bottleneck of developing supervised medical
and clinical AI models is that they require annotated data
at scale for training a well-functioning model. However,
such annotations have to be conducted by domain experts,
which is often expensive and time-consuming. This causes the
curation of large-scale medical and clinical data with high-
quality annotations to be challenging. However, this may no
longer be a bottleneck for LAMs, as they can leverage self-
supervision and reinforcement learning in training, relieving
the annotation burden and workload of curating large-scale
annotated datasets [6]. With the ever-increasing proliferation
of medical Internet of things such as pervasive wearable
sensors, medical and clinical history such as electronic health
records (EHRs), prevalent medical imaging for diagnosis such
as computed-tomography (CT) scans, the growing genomic
sequence discovery, and more, the abundance of biomedical,
clinical, and health data fosters the development of the next
generation of AI models in the ﬁeld, which are expected
to have a large capacity for modeling the complexity and
magnitude of health-related data, and generalize to multiple
unseen scenarios to actively assist and engage in clinical and
medical decision-making.
Despite the homogeneity of the model architecture (current
LAMs are primarily based on Transformer [3]), LAMs inher-
ently are strong learners of heterogeneous data due to their
large capacity, uniﬁed input modeling of different modali-
ties, and improved multi-modal learning techniques. Multi-
modality is common in biomedical and health settings, and
the multi-modal nature of health data provides the natural and
promising ground for developing and evaluating LAMs.
The LAMs that this article discusses are mainly foundation
models [7]. However, this article also provides a retrospective
of the recent LAMs that are not necessarily considered foun-
dational at their current stage, but are seminal in advancing

--- Page 3 ---

QIU et al.: LARGE AI MODELS IN HEALTH INFORMATICS: APPLICATIONS, CHALLENGES, AND THE FUTURE
3
the future development of LAMs in the ﬁelds of biomedicine
and health informatics. Fig. 2 summarizes the key features of
LAMs, and highlights the paradigm shift it is introducing, i.e.,
1) large-scale model size; 2) large-scale training/pre-training;
and 3) large generalization.
Albeit inspirational, LAMs still face challenges and limi-
tations, and the rapid rise of LAMs brings new opportunities
as well as potential pitfalls. This article aims to provide a
comprehensive review of the recent developments of LAMs,
with a particular focus on their impacts on the biomedical and
health informatics communities. The remainder of this article
is organized as follows: Section II describes the background of
LAMs in general domains, such as natural language processing
(NLP) and computer vision (CV); Section III discusses current
progress and possible applications of LAMs in key sectors of
health informatics; Section IV discusses challenges, limitations
and risks of LAMs; Section V points out some potential
future directions of advancing LAMs in health informatics,
and Section VI concludes.
As this ﬁeld progresses very rapidly, and also due to the
page limit, there are a lot of works that this paper cannot
cover. It is our hope that the community can be updated with
the latest advances, so we refer readers to our website 1 for
the latest progress about LAMs.
II. BACKGROUND OF LARGE AI MODELS
The burgeoning AI community has devoted much effort to
developing large AI models (LAMs) in recent years by lever-
aging the massive inﬂux of data and computational resources.
Based on the pre-training data modality, this article categorizes
the current LAMs into three types and deﬁnes them as follows:
1) Large Language Model (LLM): LLMs are pre-trained
on language data and applied to language downstream
tasks. Language in different settings can have different
interpretations, e.g., protein is the language of life, and
code is the language of computers.
2) Large Vision Model (LVM): LVMs are pre-trained on
vision data and applied to vision downstream tasks.
3) Large Multi-modal Model (LMM): LMMs are pre-
trained on multi-modal data, e.g., language and vision
data, and applied to various single- or multi-modal
downstream tasks.
This section provides an overview of the background of
these three types of LAMs in general domains.
A. Large Language Models
The proposal of the Transformer architecture [3] heralds the
start of developing large language models (LLMs) in the ﬁeld
of NLP. Since 2018, following the birth of GPT (Generative
Pre-trained Transformer) [8] and BERT (Bidirectional Encoder
Representations from Transformers) [9], the development of
LLMs has progressed rapidly.
Broadly speaking, the recent LLMs [10]–[21], have the
following three distinct characteristics: 1) parameter-wise, the
number of learnable parameters of an LLM can be easily
1https://github.com/Jianing-Qiu/Awesome-Healthcare-Foundation-Models
scaled up to billions; 2) data-wise, a large volume of unlabelled
data are used to pre-train an LLM, and the amount can often
reach millions or billions if not more; 3) paradigm-wise, LLMs
are ﬁrst pre-trained often with weakly- or self-supervised
learning (e.g., masked language modeling [9] and next token
prediction [4]), and then ﬁne-tuned or adapted to various
downstream tasks such as question answering and dialogue in
which they are able to demonstrate impressive performance.
Recent advances reveal that LLMs are impressive zero-
shot, one-shot, and few-shot learners. They are able to extract,
summarize, translate, and generate textual information with
only a few or even no prompt/ﬁne-tuning samples [4]. Further-
more, LLMs manifest impressive reasoning capability, and this
capability can be further strengthened with prompt engineering
techniques such as Chain-of-Thought prompting [22].
There was an upsurge in the number of new LLMs from
2022 onwards. Despite the general consensus that scaling up
the number of parameters and the amount of data will lead
to improved performance, which leads to a dominant trend
of developing LLMs often with billions of parameters (e.g.,
LLMs such as PaLM [13] have already contained 540 billion
parameters) and even trillions of data tokens (e.g., LLaMa 2
was pre-trained with 2 trillion tokens [11], and the training data
of RETRO [23] had over 5 trillion tokens), there is currently
no concerted agreement within the community that if this
continuous growth of model and data size is optimal [10],
[14], and there is also lacking a veriﬁed universal scaling law.
To balance the data annotation cost and efﬁcacy, as well
as to train an LLM that can better align with human intent,
researchers have commonly used reinforcement learning from
human feedback (RLHF) [24] to develop LLMs that can
exhibit desired behaviors. The core idea of RLHF is to use
human preference datasets to train a Reward Model (RM),
which can predict the reward function and be optimized by RL
algorithms (e.g., Proximal Policy Optimization (PPO) [25]).
The framework of RLHF has attracted much attention and
become a key component of many LLMs, such as Instruct-
GPT [19], Sparrow [26], and ChatGPT [1]. Recently, Susano
Pinto et al. [27] have also investigated this reward optimization
in vision tasks, which can possibly advance the development
of future LVMs using RLHF.
B. Large Vision Models
In computer vision, it has been a common practice for years
to ﬁrst pre-train a model on a large-scale dataset and then
ﬁne-tune it on the dataset of interest (usually smaller than the
one for pre-training) for improved generalization [28]. The
fundamental changes driving this evolution of large models
lie in the scale of pre-training datasets and models, and
the pre-training methods. ImageNet-1K (1.28M images) [29]
and -21K (14M images) [30] used to be canonical datasets for
visual pre-training. ImageNet is manually curated for high-
quality labeling, but the prohibitive cost of curation severely
hindered further scaling. To push the scale beyond ImageNet’s,
datasets like JFT (300M [31] and 3B [32] images) and IG
(3.5B [33] and 3.6B [34] images) were collected from the web
with less or no curation. The quality of annotation is therefore

--- Page 4 ---

4
compromised, and the accessibility of datasets become limited
because of copyright issues.
The compromised annotation requires the pre-training
paradigm to shift from supervised learning to weakly-/self-
supervised learning or unsupervised learning. The latter meth-
ods include autoregressive modeling, generative modeling and
contrastive learning. Autoregressive modeling trains the model
to autoregressively predict the next pixel conditioned on the
preceding pixels [35]. Generative modeling trains the model
to reconstruct the entire original image, or some target regions
within it [36], from its corrupted [37] or masked [38] variants.
Contrastive learning trains the model to discriminate similar
and/or dissimilar data instances [39].
Vision Transformers (ViTs) and Convolutional Neural Net-
works (CNNs) are two major architectural families of LVMs.
For vision transformers, pioneering works ViT [40] and iGPT
[35] transferred the transformer architectures from NLP to
CV with minimal modiﬁcation, but the resulting architectures
incur high computational complexity, which is quadratic to the
image size. Later, works like TNT [41] and Swin Transformer
[42] were proposed to better adapt transformers to visual data.
Recently, ViT-G/14 [32], SwinV2-G [43] and ViT-22B [44]
substantially scaled the vision transformers up using a bag of
training tricks to achieve state-of-the-art (SOTA) accuracy on
various benchmarks. While ViTs may seem to gain more mo-
mentum than CNNs in developing LVMs, to improve CNNs,
the latest works such as ConvNeXt [45] and InternImage
[46] redesigned CNN architecture with inspirations from ViTs
and achieved SOTA accuracy on ImageNet. This refutes the
previous statement that CNNs are inferior to ViTs. Apart from
the above, recent works like CoAtNet [47] and ConViT [48]
merge CNNs and ViTs to form new hybrid architectures. Note
that ViT-22B is the largest vision model to date, whose scale is
signiﬁcantly larger than that (1.08B) of the current art of CNNs
(InternImage) but is still much behind that of the contemporary
LLMs.
Architecturally speaking, LVMs are largely-scaled-up vari-
ants of their base architectures. How they are scaled up can
signiﬁcantly impact the ﬁnal performance. Simply increasing
the depth by repeating layers vertically may be suboptimal
[49], so a line of studies [46], [50], [51] investigate the rules
for effective scaling. Furthermore, scaling the model size up
is usually combined with larger-scale pre-training [49], [52]
and efﬁcient parallelism [53] for improved performance.
LVMs also transform other fundamental computer vision
tasks beyond classiﬁcation. The latest breakthrough in seg-
mentation task is SAM [2]. SAM is built with a ViT-H image
encoder (632M), a prompt encoder and a transformer-based
mask decoder that predicts object masks from the output of the
above two encoders. Prompts can be points or bounding boxes
in images or text. SAM demonstrates a remarkable zero-shot
generalization ability to segment unseen objects and images.
Furthermore, to train SAM, a largest segmentation dataset to
date, SA-1B, with over 1B masks is constructed.
C. Large Multi-modal Models
This section describes large multi-modal models (LMMs).
While the primary focus is on one type of LMMs: large vision-
language models (LVLMs), multi-modality beyond vision and
language is also summarized in the end.
Training LVLMs like CLIP [54] requires more than hun-
dreds of millions of image-text pairs. Such large amount
of data was often closed source [54]–[56]. Until recently,
LAION-5B [57] was created with 5.85B data samples, match-
ing the size of the largest private dataset while being available
to the public.
LVLMs usually adopt a dual-stream architecture: input
text and image are processed separately by their respective
encoders to extract features. For representation learning, the
features from different modalities are then aligned through
contrastive learning [54]–[56] or fused into a uniﬁed repre-
sentation through another encoder on the top of all extracted
features [58]–[62]. Typically, the entire model, including uni-
modal encoder and multi-modal encoder if have, is pre-trained
on the aforementioned large-scale image-text datasets, and
ﬁne-tuned on the downstream tasks or to carry out zero-
shot tasks without ﬁne-tuning. The pre-training objectives
can be multi-modal tasks only or with unimodal tasks (see
Section II-B). Common multi-modal pre-training tasks contain
image-text contrastive learning [54]–[56], image-text matching
[58], [61], [63], autoregressive modeling [59], [62], masked
modeling [58], image-grounded text generation [61], [63], etc.
Recent studies suggest that scaling the unimodal encoders up
[60], [64] and pre-training with multiple objectives across uni-
and multi-modalities [61], [63] can substantially beneﬁt multi-
modal representation learning.
Recently, LVLMs made a major breakthrough in text-to-
image generation. There are generally two classes of methods
for such a task: autoregressive model [65]–[67] and diffusion
model [67]–[70]. Autoregressive model, like introduced in
Section II-B, ﬁrst concatenates the tokens (returned by some
encoders) of text and images together and then learns a model
to predict the next item in the sequence. In contrast, diffusion
model ﬁrst perturbs an image with random noise progressively
until the image becomes complete noise (forward diffusion
process) and then learns a model to gradually denoise the
completely noisy image to restore the original image (reverse
diffusion process) [71]. Text description is ﬁrst encoded by a
separate encoder and then integrated into the reverse diffusion
process as the input to the model so that the image generation
can be conditioned on the text prompt. It is common to reuse
those pre-deﬁned LLM and LVM architectures and/or their
pre-trained parameters as the aforementioned encoders. The
scale of these encoders and the generator can signiﬁcantly
impact the quality of generation and the ability of language
understanding [66], [70].
The paradigm of bridging language and vision modalities
can be beyond learning, e.g., using LLM to instruct other
LVMs to perform vision-language tasks [72]. Beyond vision
and language, recent development in LMMs seeks to unify
more modalities under one single framework, e.g., Image-
Bind [73] combines six whereas Meta-Transformer [74] uniﬁes
twelve modalities.

--- Page 5 ---

QIU et al.: LARGE AI MODELS IN HEALTH INFORMATICS: APPLICATIONS, CHALLENGES, AND THE FUTURE
5
III. APPLICATIONS OF LARGE AI MODELS IN HEALTH
INFORMATICS
In this section, we identify seven key sectors in which
LAMs will have substantial inﬂuence and bring a new
paradigm for tackling the problems and challenges in health
informatics. The seven key sectors include 1) bioinformatics;
2) medical diagnosis; 3) medical imaging; 4) medical infor-
matics; 5) medical education; 6) public health; and 7) medical
robotics. Table I compares current LAMs with previous SOTA
methods in these seven sectors.
A. Bioinformatics
Molecular biology studies the roles of biological macro-
molecules (e.g., DNA, RNA, protein) in life processes and
describes various life activities and phenomena including the
structure, function, and synthesis of molecules. Although many
experimental attempts have been made on this topic over
decades [75]–[77], they are still of high cost, long experiment
cycle, and high production difﬁculty. For example, the number
of experimentally determined protein structures stored in the
protein data bank (PDB) hardly rivals the number of protein
sequences that have been generated. Efﬁcient and accurate
computational methods are therefore needed and can be used
to accelerate the protein structure determination process. Due
to the huge number of parameters and learning capacity,
LAMs endow us with prospects to approach such a Herculean
task. Especially, LLMs’ outstanding representation learning
ability has been employed to implicitly model the biological
properties hidden in large-scale unlabeled data including RNA
and protein sequences.
When it comes to the ﬁeld of protein, starting from
amino acid sequences, we can analyze the spatial structure
of proteins and furthermore understand their functions, and
mutual interactions. AlphaFold2 [78] pioneered leveraging
the attention-based Transformer model [3] to predict protein
structures. Speciﬁcally, they treated structure prediction as
a 3D graph inference problem, where the network’s inputs
are pairwise features between residues, available templates,
and multi-sequence alignment (MSA) embeddings. Especially,
embeddings extracted from MSA can infer the evolutionary
information between aligned sequences. Evoformer and struc-
ture modules were proposed to update the input representation
and predict the ﬁnal 3D structure, the whole process of
which was recycled several times. Meanwhile, despite being
trained on single-protein chains, AlphaFold2 exhibits the abil-
ity to predict multimers. To further enable multimeric inputs
for training, DeepMind proposed AlphaFold-Multimer [79],
achieving impressive performance, especially in heteromeric
protein complexes structure prediction. Speciﬁcally, positional
encoding was improved to encode chains, and multi-chain
MSAs were paired based on species annotations and target
sequence similarity.
In spite of the groundbreaking endeavors aforementioned
works have contributed, to achieving optimal prediction, they
still heavily rely on MSAs and templates searched from ge-
netic and structure databases, which is time-consuming. Anal-
ogous to mining semantic information in natural language,
researchers managed to explore co-evolution information in
protein sequences in a self-supervised manner by employing
large-scale protein language models (PLMs), which learn the
global relation and long-range dependencies of unaligned and
unlabelled protein sequences. ProGen (1.2B) [80] utilized a
conditional language model to provide controllable generation
of protein sequences. By inputting desired tags (e.g., function,
organism), ProGen can generate corresponding proteins such
as enzymes with good functional activity. Elnaggar et al. [81]
devised ProtT5-XXL (11B) which was ﬁrst trained on BFD
[82] and then ﬁne-tuned on UniRef50 [83] to predict the
secondary structure. ESMfold [84] scaled the number of model
parameters up to 15B and observed a signiﬁcant prediction
improvement over AlphaFold2 (0.68 vs 0.38 for TM-score
on CASP14) with considerably faster inference speed when
MSAs and templates are unavailable. Similarly, from only
the primary sequence input, OmegaFold [85] can outperform
MSA-based methods [78], [86], especially when predicting
orphan proteins that are characterized by the paucity of
homologous structure. xTrimoPGLM [87] proposed a uniﬁed
pre-training strategy that integrates the protein understanding
and generation by optimizing masked language modelling
and general language modelling concurrently and achieved
remarkable performance over 13 diverse protein tasks with its
100B parameters. For instance, for GB1 ﬁtness prediction in
protein function task, xTrimoPGLM outperforms the previous
SOTA method: Ankh [88], with an 11% performance increase.
Moreover, for antibody structure prediction, xTrimoPGLM
outperformed AlphaFold2 (TM-score: 0.951) and achieved
SOTA performance (TM-score: 0.961) with signiﬁcantly faster
inference speed. We underscore that in the presence of MSA,
although the performance of PLMs is hardly on par with
Alphfold2, PLMs can make predictions several orders of
magnitude faster, which speeds up the process of related
applications such as drug discovery. In addition, because PLMs
implicitly understand the deep information implied in protein
sequences, they are promising to predict mutations in protein
structures and their potential impact to help guide the design
of next-generation vaccines.
In the context of RNA structure prediction, the number
of nonredundant 3D RNA structures stored in PDB is sig-
niﬁcantly less than that of protein structures, which hinders
the accurate and generalizable prediction of RNA structure
from sequence information using deep learning. To mitigate
the severe unavailability of labeled RNA data, Chen et al.
[89] proposed the RNA foundation model (RNA-FM), which
learns evolutionary information implicitly from 23 million
unlabeled ncRNA sequences [90] by recovering masked nu-
cleotide tokens, to facilitate multiple downstream tasks includ-
ing RNA secondary structure prediction and 3D closeness pre-
diction. Especially, for secondary structure prediction, RNA-
FM achieves 3-5% performance increase among three metrics
(i.e., Precision, Recall, and F1-score), compared to UFold [91]
which utilizes U-Net as the backbone. Furthermore, based
on RNA-FM, Shen et al. [92] pioneered predicting 3D RNA
structure directly.
Undoubtedly, these models are seminal and have reduced
the time and cost of molecule structure prediction by a

--- Page 6 ---

6
TABLE I: Comparison between state-of-the-art LAMs (second row) and prior arts (ﬁrst row) in typical tasks of seven biomedical
and health sectors. “−” denotes not applicable. “N/R” denotes not released in the original literature. For zero-shot medical
segmentation task, we tested the off-the-shelf Mask RCNN model to compare with SAM.
large margin. Thereby, this raises the question of whether
LAMs can completely replace experimental methods such as
Cryo-EM [75]. We deem that it still falls short from that
point. Speciﬁcally, the advance of LAMs builds upon big
data and large model capacity, which means they are still
data-driven, and hence their ability to predict unseen types
of data could sometimes be problematic. For instance, [93]
stated that AlphaFold can barely handle missense mutation
on protein structure due to the lack of a corresponding
dataset. Furthermore, how we can assess the quality of model
prediction for unknown protein structures remains unclear. In
turn, these unveriﬁed protein structures cannot be applied to,
for example, drug discovery. Therefore, protocols and metrics
need to be established to assess their quality and potential im-
pacts. There are mutual and complementary beneﬁts between
LAMs and conventional experimental techniques. LAMs can
be re-designed to predict the process of protein folding and
reveal their mutual interactions so as to facilitate experimental
methods. On the other hand, experimental information, such
as some physical properties of molecules, can be leveraged by
LAMs to further improve prediction performance, especially
when dealing with rare data (e.g., orphan protein).
B. Medical Diagnosis
As research has been carried out to improve the safety and
strengthen the factual grounding of LAMs, it is foreseeable
that LAMs will play a signiﬁcant role in medical diagnosis
and decision-making.
CheXzero [94], a zero-shot chest X-ray classiﬁer, has
demonstrated radiologist-level performance in classifying mul-
tiple pathologies which it never saw in its self-supervised
learning process. Recently, ChatCAD [95], a framework that
integrates multiple diagnostic networks with ChatGPT, demon-
strated a potential use case for applying LLMs in computer-

--- Page 7 ---

QIU et al.: LARGE AI MODELS IN HEALTH INFORMATICS: APPLICATIONS, CHALLENGES, AND THE FUTURE
7
aided diagnosis (CAD) for medical images. By stratifying the
decision-making process with specialized medical networks,
and followed by an iteration of prompts based on the outcomes
of those networks as the queries to an LLM for medical
recommendations, the workﬂow of ChatCAD offers an insight
into the integration of the LLMs that were pre-trained using a
massive corpus, with the upstream specialized diagnostic net-
works for supporting medical diagnosis and decision-making.
Its follow-up work ChatCAD+ [96], shows improved quality
of generating diagnostic reports with the incorporation of a
retrieval system. Using external knowledge and information
retrieval can potentially enable the resulting diagnostics more
factually-grounded, and such a design has also been favoured
and implemented in the ChatDoctor model [97]. By leveraging
a linear transformation layer to align two medical LAMs,
XrayGPT [98], a conversational chest X-ray diagnostic tool,
shows decent accuracy in responding to diagnostic summary.
While most LLMs are based on English, researchers have also
managed to ﬁne-tune LLaMa [10], an LLM, with Chinese
medical knowledge, and the resulting model shows improved
medical expertise in Chinese [99].
Apart from chest X-ray diagnostics and medical question
answering, LAMs have also been applied to other diagnostic
scenarios. HeartBEiT [100], a foundation model pre-trained
using 8.5 million electrocardiograms (ECGs), shows that large-
scale ECG pre-training could produce accurate cardiac diag-
nosis and improved explainability of the diagnostic outcome,
and the amount of annotated data for downstream ﬁne-tuning
could be reduced. Medical LAMs may also potentially produce
a more reliable forecast of treatment outcomes and the future
development of diseases using their strong reasoning capabil-
ity. For example, Li et al. [101] proposed BEHRT, which is
able to predict the most likely disease of a patient in his/her
next visit by learning from a large archive of EHRs. Rasmy
et al. [102] proposed Med-BERT, which is able to predict the
heart failure of diabetic patients.
With the ubiquity of internet, medical LAMs can also
offer remote diagnosis and medical consultation for people
at home, providing people in need with more ﬂexibility. We
also envision that future diagnosis of complex diseases may
also be conducted or assisted by a panel of clinical LAMs.
C. Medical Imaging
The adoption of medical imaging and vision techniques
has vastly inﬂuenced the process of diagnosis and treatment
of a patient. The wide use of medical imaging, such as CT
and MRI, has produced a vast amount of multi-modal, multi-
source, and multi-organ medical vision data to accelerate the
development of medical vision LAMs.
The recent success of SAM [2] has drawn much atten-
tion within the medical imaging community. SAM has been
extensively examined in medical imaging, especially on its
zero-shot segmentation ability. While research revealed that
for certain medical imaging modalities and targets, the zero-
shot performance of SAM is impressive (e.g., on endoscopic
and dermoscopic images, as these are essentially RGB images,
which are the same type as that of SAM’s pre-training images),
for imaging modalities that are medicine-speciﬁc such as
MRI and OCT (optical coherence tomograpy), SAM often
fails to segment targets in a zero-shot way [103], mainly
because the topology and presentation of a target in those
imaging modalities are much different from what SAM has
seen during pre-training. Nevertheless, after adaptation and
ﬁne-tuning, the medical segmentation accuracy of SAM can
surpass current SOTA with a clear margin [104], showing
the potential of extending versatility of general LVMs to
medical imaging with parameter-efﬁcient adaptation. Apart
from zero-shot segmentation, MedCLIP [105] was proposed, a
contrastive learning framework for decoupled medical images
and text, which demonstrated impressive zero-shot medical
image classiﬁcation accuracy. In particular, it yielded over 80%
accuracy in detecting Covid-19 infection in a zero-shot setting.
The recent PLIP model [106], built using image-text pairs
curated from medical Twitter, enables both image-based and
text-based pathology image retrieval, as well as enhanced zero-
shot pathology image classiﬁcation compared to CLIP [54].
Many
medical
imaging
modalities
are
3-dimensional
(3D), and thus developing 3D medical LVMs are crucial.
Med3D [107], a heterogeneous 3D framework that enables
pre-training on multi-domain medical vision datasets, shows
strong generalization capabilities in downstream tasks, such as
lung segmentation and pulmonary nodule classiﬁcation.
With the success of generative LAMs such as Stable
Diffusion [68] in the general domain, which can generate
realistic high-ﬁdelity images with text descriptions, Chambon
et al. [108] recently ﬁne-tuned Stable Diffusion on medical
data to generate synthetic chest X-ray images based on clinical
descriptions. The encouraging generative capability of Stable
Diffusion in the medical domain may inspire more future re-
search on using generative LAMs to augment medical data that
are conventionally hard to obtain, and expensive to annotate.
Nevertheless, some compromises are also evident in medical
vision LAMs. For example, the currently common practice of
training LVMs and LMMs often limits the size of the medical
images to shorten the training time and reduce the computa-
tional costs. The reduced size inevitably causes information
loss, e.g., some small lesions that are critical for accurate
recognition might be removed in a compressed downsampled
medical image, whereas doctors could examine the original
high-resolution image and spot these early-stage tumors. This
may cause performance discrepancies between current medical
vision LAMs and well-trained doctors. In addition, although
research has shown that increasing medical LAM size and data
size could improve medical domain performance of the model,
e.g., STU-Net [109], a medical segmentation model with 1.4
billion parameters, the best practice of model-data scaling is
yet to be conclusive in medical imaging and vision.
D. Medical Informatics
In medical informatics, it has been a topic of long-standing
interest to leverage large-scale medical information and signals
to create AI models that can recognize, summarize, and
generate medical and clinical content.
Over the past few years, with advances in the development
of LLMs [9], [13], [110], and the abundance of EHRs as

--- Page 8 ---

8
well as public medical text outlets such as PubMed [111],
[112], research has been carried out to design and propose
Biomedical LLMs. Since the introduction of BioBERT [113], a
seminal Biomedical LLM which outperformed previous SOTA
methods on various biomedical text mining tasks such as
biomedical named entity recognition, many different Biomed-
ical LLMs that stem from their general LLM counterparts
have been proposed, including ClinicalBERT [114], BioMega-
tron [115], BioMedRoBERTa [116], Med-BERT [117], Bio-
ELECTRA [118], PubMedBERT [119], BioLinkBERT [120],
BioGPT [121], and Med-PaLM [122].
The recent GatorTron [123] model (8.9 billion parameters)
pre-trained with de-identiﬁed clinical text (82 billion words)
revealed that scaling up the size of clinical LLMs leads to
improvements on different medical language tasks, and the
improvements are more substantial for complex ones, such
as medical question answering and inference. Previously, the
PubMedBERT work [119] also suggested that pre-training
an LLM with biomedical corpora from scratch can lead to
better results than continually training an LLM that has been
pre-trained on the general-domain corpora. While training
large number of parameters may seem daunting, parameter-
efﬁcient adaptation techniques such as low-rank adaptation
(LoRA) [124] have enabled researchers to efﬁciently adapt
a 13 billion LLaMa model to produce decent US Medical
Licensing Exam (USMLE) answers, and the performance of a
collection of such ﬁne-tuned models, called MedAlpaca [125]
also reveals that increasing model size and quality of data can
improve model’s medical domain expertise. As LLMs start
to show emergent abilities [126] with their size scaled up
increasingly, Agrawal et al. [127] revealed that recent LLMs
such as InstructGPT [19] and GPT-3 [110] can well extract
clinical information in a few-shot setting despite being not
explicitly trained for the clinical domain. Med-PaLM [122],
a Biomedical LLM with 540 billion parameters generated by
applying instruction prompt tuning on Flan-PaLM [12] (which
exhibited SOTA accuracy on MultiMedQA [122]), demon-
strated the ability to answer consumer medical questions that
are comparable to the performance of clinicians. Its follow-
up work, Med-PaLM 2 [128], further strengthens medical
reasoning, and as shown in Table I, it has reached an accuracy
of 86.5% on the MedQA benchmark. As prompt engineering
has become a key technique for investigating and improving
LLMs, Li´evin et al. [129] have also applied various prompt
engineering on the GPT-3.5 series such as InstructGPT [19]
to understand their abilities on medical question answering,
and their results suggested that increasing Chain-of-Thoughts
(CoTs) [22] per question can deliver better, more interpretable
medical question responses.
The impressive performance of Biomedical LLMs on med-
ical language tasks shows their potential to be used to assist
clinicians in processing, interpreting, and analyzing clinical
and medical data more efﬁciently, and also to vastly reduce the
time that clinicians have to spend on documenting EHRs. Patel
and Lam [130] recently shed insight on using ChatGPT [1] to
generate discharge summaries, which could potentially relieve
doctors from laborious writing and improve their clinical
productivity. Biomedical LLMs can also assist in the writing
of prior authorizations for insurance purposes, accelerating
treatment authorizations [131]. On the patient side, the zero-,
one-, and few-shot learning capability of LLMs may enable
them to provide personalized medical assistance based on
the medical history of each individual patient. In addition,
LLMs may also ﬁnd them applicable in clinical trial matching.
Based on candidates’ demographics and medical history, a
Biomedical LLM may effectively generate eligible matching,
which accelerates clinical trial recruitment and initiation.
E. Medical Education
It is likely that future medical education will also be
inﬂuenced by LAMs, as research continues to strengthen their
scientiﬁc grounding and creative generation. Many LAMs,
such as GPT-4 [4] and Med PaLM 2 [128], have already passed
USMLE with a score of over 86%, demonstrating sound
knowledge spectrum and reasonable capabilities in bioethics,
clinical reasoning, and medical management.
The generative capability of such LAMs may augment
medical student learning and help them gain additional insights
from AI-generated content as recently pointed out in [132]. A
LAM with wide knowledge and social compliance can act as
a companion learning assistant, answering medical questions
promptly and explaining intricate terms and practices in simple
sentences. For example, the recent GPT-4 model [4] can act
as a Socratic tutor, leading a student step-by-step to ﬁnd the
answers by themselves, which is an important step towards
practical adoption of LAMs in education as they can be steered
to teach/assist students in a desired manner. The OPTICAL
model proposed by Shue et al. [133] recently shows the
feasibility of using LLMs to guide beginners in analyzing
bioinformatics data. The sentence paraphrasing abilities of
LLMs [134] such as ChatGPT may also help students with
dyslexia in their learning. However, concerns about the ille-
gitimate uses of LAMs such as plagiarism are practical and
should raise awareness. A pilot study conducted by Mitchell
et al. [135] proposed a zero-shot detector named DetectGPT,
which is able to distinguish human-written or LLM-generated
text. This attempt may lead to more research into developing
reliable tools for verifying the content source and potentially
countering the side effects of LAMs in education.
For medical education givers, LAMs can potentially create
novel teaching and exam contents, and diversify the teaching
formats and their presentation. Based on the history of medical
study and outcomes, LAMs may also help design personalized
and precise course materials for students in need. In addi-
tion, LAMs may also help deliver remote medical education,
providing engaging learning experiences and opportunities for
students living in resource-poor areas or from underprivileged
families. LAMs can also serve as a grading and scoring system
in medical education, e.g., grading the surgical skill of a
surgeon operating a surgical robot.
In medical and clinical training such as nurse training, one
can imagine a domain-knowledgeable LAM can act as an
assistant or a trainer to supervise the training. For certain
frequent and tedious routine medical training courses, human
trainers tend to become less productive as training keeps re-
peating, and the quality of training delivery also varies among

--- Page 9 ---

QIU et al.: LARGE AI MODELS IN HEALTH INFORMATICS: APPLICATIONS, CHALLENGES, AND THE FUTURE
9
different human trainers. With a wide knowledge spectrum
and responsive interactions, training delivered by a LAM can
potentially be more engaging and productive, and the standard
of training can be maintained as equal and of high quality.
F. Public Health
As the American epidemiologist Larry Brilliant said “out-
breaks are inevitable, but pandemics are optional”, with
the world gradually returning to normal after the Covid-19
pandemic, if there is one thing that the world has to reﬂect on,
it is how we become prepared to prevent the next pandemic.
Based on past public policy and interventions to contain
the spread of infectious diseases and the speciﬁc current
situation, LLMs may help epidemiologists and policymakers
to draft targeted public policies and recommend effective
interventions. LLMs and other LAMs are also likely to be
used to monitor, track, forecast, and analyze the progress of
new outbreaks. LAMs have been actively researched for drug
discovery, e.g., the Pangu Drug model [136], and they can
potentially be used for the design of vaccine and drugs to treat
and save people from new outbreaks. Furthermore, another
potential usage of LAMs, as pointed out in [137], can be in
precision triage and diagnosis, in which they could play a
pivotal role as medical care workforce might be stretched when
encountering a new outbreak. An important aspect of tackling
an outbreak/epidemic is to handle misinformation. The study
conducted by Chen et al. [138] revealed that from 21 January
2020 to 21 March 2020, Twitter produced over 72 million
Covid-19-related tweets. If unveriﬁed media information pro-
liferates at scale, it inevitably causes complications in tackling
the outbreak. Although LAMs could be double-edged swords
when it comes to misinformation, with gradually complete
regulations and strengthened factual grounding of LAMs, they
can be used to effectively identify misinformation and tackle
public health infodemic.
Beyond their promising usage in preventing pandemics,
LAMs are also an effective tool for solving other public
health challenges, for example, providing large-scale dietary
monitoring and assessment [139], [140] to tackle the grow-
ing double burden of malnutrition [141] in many low- and
middle-income countries, and demystifying and proposing new
solutions for mental illnesses that are common in populations.
Researchers have recently proposed ClimaX [142], a founda-
tion model for forecasting weather and climate change. With
their remarkable forecasting capability, LAMs like ClimaX
and Pangu-Weather [143] can advance our understanding of
climate change and provide solutions to better address the
global health issues posed by climate change.
G. Medical Robotics
From surgical robots that allow surgeons to perform preci-
sion minimally invasive surgery, to wearable robots that assist
patients with health monitoring and rehabilitation, medical
robotics has seen rapid growth and advances over the past
few decades. LAMs have begun to show exciting prospects in
enhancing medical robotic vision, interaction, and autonomy.
1) Enhance Vision: The integration of LAMs into surgical
robots has the potential to enhance the vision of these systems
in surgery. Endo-FM [144], a foundation model with high
precision for endoscopic video classiﬁcation, segmentation,
and detection, could be one of these LAMs to provide robotic
surgery systems with enhanced vision. In addition to online
vision enhancement, LAMs can also potentially improve the
ofﬂine workﬂow analysis of robotic surgery, and more accu-
rately and objectively predict the likelihood of complications
and successful outcomes, which help surgeons better plan and
execute surgeries in the future. Furthermore, with their strong
generative capabilities, LAMs can be used to generate and
simulate surgical procedures, allowing surgeons to practice
and reﬁne their techniques before operating on a patient with
real surgical robots. Beyond surgical robots, the perception of
many companion and assistive robots can also be enhanced by
LAMs, e.g., enabling a companion robot to better understand
a patient’s emotion through accurate recognition of facial ex-
pressions [145], and enabling an assistive robot to offer safer,
more natural navigation for visually impaired people [146].
2) Improve Interaction: LAMs may signiﬁcantly improve the
interactive capabilities of many medical robots, by enabling
them to recognize human emotions, gestures, and speech,
and respond to high-level human language commands. For
example, this will be easier for patients undergoing rehabilita-
tion to communicate and engage with their robotic assistants,
improving their overall recovery experience. More intelligent
LAMs may also better understand human intentions and create
more human-like companionship, which could improve the
overall quality of care for the elderly [147]. Recently, Surgical-
GPT [148], a visual question answering model for surgery, has
shown great promise that future robotic surgery could become
more interactive between surgeons and the surgical robots.
3) Increase Autonomy: LAMs have the potential to turn
robotic pipelines from the current engineer in the loop to user
in the loop using high-level language commands [149], which
could enable surgeons with less programming proﬁciency to
easily adapt robotic manipulations to their target tasks. Studies
have proposed to use a single LAM to conduct diverse robotic
tasks, demonstrating impressive adaptability and generaliza-
tion skills [150]–[156]. These advancements can potentially
inspire the development of more autonomous medical robots.
IV. CHALLENGES, LIMITATIONS, AND RISKS
Despite the promising outcome of LAMs, there remain
many challenges and potential risks in developing and deploy-
ing LAMs in biomedical, clinical, and healthcare applications.
1) Data: Most existing public datasets for health informatics
are much smaller (please refer to Fig. 2 and Table II 2) than
those used in general domains and thus are likely insufﬁcient
to unlock the full potential of LAMs in biomedical and health
scenarios. Building large-scale high-quality medical datasets
are particularly challenging because (1) curation requires
domain-expertise to identify data of clinical relevance, and
quality assurance is very important with health data; (2) some
2References to the datasets in Table II and methods in Table I can be found
in https://github.com/Jianing-Qiu/Awesome-Healthcare-Foundation-Models.

--- Page 10 ---

10
TABLE II: Large-scale datasets in biomedical and health informatics
data modalities like MRI require special devices to collect,
which is inefﬁcient and expensive; (3) the collected data may
not be allowed to publish or use for training because of
consent, legal and privacy issues. Furthermore, the training
strategy RLHF of some LLMs like ChatGPT requires even
more intense engagement of human experts.
2) Computation: Training, or even ﬁne-tuning, contempo-
rary LAMs is extremely expensive in terms of time and
resource consumption, which is beyond the budget of most
researchers and organizations [157]. Taking LLaMa as an
example, an LLM with 65B parameters, it took about 21
days on 2048 A100 GPUs to train the model once on a
dataset of 1.4T tokens [10]. Furthermore, even inference can
be prohibitively costly due to the model size, making it
impractical for most hospitals to deploy these LAMs locally
using their computing devices at hand.
3) Reliability: The reliability threshold for translation into
clinical practice is signiﬁcantly higher [158]. Despite the
impressive performance, LLMs are still far from reliable [159]
and prone to hallucinate [4], [160], i.e., generating factually-
incorrect yet plausible content which misleads users. In ad-
dition, the unsatisfactory robustness of LAMs impairs their
credibility. LLMs are known to be sensitive to prompts [161].
LLMs as well as LMs for other modalities remain vulnerable
to out-of-distribution and adversarial examples [159], [162].
Improving the robustness of LAMs may require even more
data [163]. Therefore, caution is highly required when using
LAMs in healthcare practice to alleviate the potential danger
of over-reliance. In addition, LAMs, especially LLMs were
trained ofﬂine, in many clinical and health scenarios, using
up-to-date information is critical.
4) Privacy: First, LAMs have been reported to have ex-
cessive capacity to memorize their training data [164], and
more importantly, it is viable to extract sensitive information
in the memorized data using direct prompts [164], [165]. This
was later mitigated by ﬁne-tuning LAMs to refuse to answer
such prompts [166]. However, Li et al. [166] also show that
this mitigation can be bypassed through tricky prompts called
jailbreaking. Moreover, membership inference attacks [167]
could reveal if a sample is in the training set, e.g., if a patient
is in a cancer dataset. It has been recently demonstrated to
work even on the latest large diffusion models [168].
Second, the information provided by users to query LLM-
integrated applications may be leaked. According to the data
policy of OpenAI [169], they store the data that users provide
to ChatGPT or DALL-E to train their models. Unfortunately,
it has been reported that the stored personal information
can be leaked incidentally by a “chat history” bug [170] or
deliberately by indirect prompt injection attack [171].
5) Fairness: LAMs are data-driven approaches so they
could learn any bias from the training data. Unfortunately, bias
widely exists in the delivery of healthcare [172] and also the
data collected in this process [173]–[175]. Machine learning
models trained on such data are reported to mimic human
bias against race [173], gender [174], politics [176], etc. In
addition to these conventional biases, LLMs present language
bias as well, i.e., they perform better in particular languages
like English but worse in others [177] because training data is

--- Page 11 ---

QIU et al.: LARGE AI MODELS IN HEALTH INFORMATICS: APPLICATIONS, CHALLENGES, AND THE FUTURE
11
Fig. 3: Future directions of LAMs in health informatics
dominated by a few languages.
6) Toxicity: Current LAMs, even LLMs explicitly trained
with alignment, do not understand and represent human ethics
[178]. LLMs are reported to produce hate speech [179] that
causes offensive and psychologically harmful content and even
incites violence. Secondly, LAMs may endorse unethical or
harmful views and behaviors [178] and motivate users to
perform. Lastly, LAMs can be used intentionally to facilitate
harmful activities like spreading disinformation and encourag-
ing criminal activities. Although some countermeasures like
ﬁltering are applied, they can be circumvented by prompt
injection [177].
7) Transparency: Recently, some impactful LAMs like
ChatGPT and Med-PaLM 2 chose not to disclose the complete
technical details, the pre-trained models, and the used data.
This makes it impossible for others to independently repro-
duce, improve upon and audit their methods. This transparency
threat for LAMs can be more serious in healthcare as many
medical data is private and models built upon them are not
allowed to be open sourced.
8) Interpretability: LAMs inherently lack interpretability due
to their extremely dense hidden layers. Even worse, the behav-
ior of LAMs can be meaningless [180], [181], hard to predict
[182], [183] and thus mysterious. For example, DALL-E 2
generates the images of physical objects with absurd prompts
(e.g., “Apoploe vesrreaitais” for birds) [180]; the reasoning
ability of LLMs can be improved by simply adding a text of
“Let’s think step by step” to prompts [182]. There has been
little progress towards explaining LAMs. Chain-of-thought
prompts provide one way to reveal the intermediate reasoning
steps behind an output, but it remains unclear whether the
generated description of reasoning reﬂects the model’s true
internal reasoning. Alternatively, mechanistic interpretability
methods [183] reverse-engineer the computation of LAMs to
illuminate the model’s internal mechanism of reasoning.
9) Sustainability: Despite many beneﬁts, LAMs, if abused,
will negatively impact the sustainability of our society. LAMs
consume lots of computation resource [10] and energy [184]
and emit tons of carbon [184] in all activities in their lifecycle
(from training to deployment) because of their scale. For
example, as estimated by [185], training a GPT-3 model
consumes 1287 MWh and emits 552 tons of CO2. As the
paradigm moves towards LAMs in healthcare, more and more
research is expected to be conducted based on LAMs, which
could be environmentally unfriendly due to the cost and carbon
emission if right practices [184] are not established.
10) Regulation: Regulation is needed to ensure responsible
LAMs especially when some of the above issues cannot be
technically addressed. Particularly, data collection and usage
should be governed to protect the rights of data owner such as
copyright, privacy and “being forgotten” [186]. The liability
of LAMs’ creators/owners for the possible harm caused by
the model’s output should be clariﬁed. LAMs should be
deployed in critical healthcare services only if regulatory
approval is obtained and standardized safety assessment is
passed. Regulation today is much behind the development of
technology for LAMs, even for more general AI. Our webpage
lists some major legislation for reference if readers want to
know more about AI regulation.
V. FUTURE DIRECTIONS
In this section, we discuss some promising directions for
future work to advance LAMs in the ﬁeld of biomedical and
health informatics, and our discussion below is mainly focused
on two aspects: capability and responsibility.
A. Capability
The ﬁrst is to develop new LAMs for health informatics
with better capability. The better capability here refers to
either new abilities (e.g., a versatile medical task solver)
or improved existing abilities (e.g., higher diagnostic accu-
racy), compared to the prior paradigm. Interestingly, some
emergent new abilities may be unexpected or even unknown
to humans [126]. Among numerous approaches to LAMs,
some are perceived by us as most promising. Scaling up
the size of dataset and model are two widely recognized
approaches, but how to do it efﬁciently is of importance
and far from solved. Furthermore, pre-training with varied
tasks and modalities has achieved remarkable progress towards
versatility in performing downstream tasks. A huge beneﬁt is
foreseeable if diverse knowledge that exists in these varied
tasks (e.g., biology, medicine, etc.) and data modalities (e.g.,
medical corpora, imaging, physiological signals, etc.) can be
incorporated into a single foundation model as a world model
[187]. This world model boosts capability by complementing
the information missing in an input, e.g., offering biomedical
knowledge (acquired from other tasks) for diagnosing a disease
when only the symptom data is given as input. Note that
this is exactly how human doctors diagnose in practice, i.e.,
they comprehend information from the symptoms based on
their medical knowledge acquired from learning and clinical
practicing, i.e., multiple other tasks and sources.
The second is to reveal the hidden capabilities of existing
pre-trained LAMs. A capability is hidden if it has been
already developed in a pre-trained model but just unknown
to users. Discovering hidden capabilities involves nothing but
probing the model. A typical example is the substantially
improved reasoning ability of LLMs by simply adding a line
of “Let’s think step by step” to prompts [182]. There are still

--- Page 12 ---

12
many unknowns about existing LAMs as they have become in-
creasingly complex with enormously large sets of parameters.
It is unclear whether the full potential of existing LAMs has
been harnessed or not. Therefore, it is worth investigating if
those pre-trained LAMs possess hidden capabilities about the
health informatics tasks of interest. If so, discovering these
hidden capabilities provides a solution or improvement to the
tasks in a nearly cost-free way as it requires no further large-
scale training. Prompt engineering [188] as an emerging ﬁeld
is an effective approach to discovering hidden capabilities.
B. Responsibility
Responsible LAMs for social good is paramount [189].
We suggest two complementary strategies: development and
deployment, for future work to tackle challenges in LAM
reliability, fairness, transparency, and beyond. Development
strategy focuses on learning responsible LAMs, while deploy-
ment strategy emphasizes using LAMs responsibly.
Technically, responsible LAMs can be developed through
two perspectives: data and algorithms. As LAMs learn bias
from training data, an intuitive countermeasure is thus to
mitigate bias in training data. It can be done by ﬁltering
biased data [190], increasing underrepresented populations’
data, etc. Unfortunately, how to efﬁciently inspect large-scale
datasets remains challenging. Besides, training data should
encompass diverse distributions to robustify the model against
the distribution shifts in the wild, and human preference to
align the model with human values. Some of them like human
preference must be collected from human activities, while
the rest can be also generated by other algorithms like data
augmentation and generative models. Once we have high-
quality data, algorithms like RLHF and adversarial training
can be adopted to exploit these data to acquire the desired
properties for responsible LAMs.
In addition to training LAMs to be responsible, it is also
vital to use LAMs in a responsible way. Efforts should be
made to educate the users, especially those use LAMs for
critical healthcare services, about the basics and limitations of
LAMs being used. Human-LAM partnership should also be
researched for the effective, efﬁcient and responsible use of
LAMs, including how to query/instruct LAMs by prompt engi-
neering and assess/adopt the responses from LAMs. Besides, a
comprehensive veriﬁcation framework [191] covering various
desired properties for LAMs is critical for assessing how
irresponsible a LAM is, which is still lacking. We encourage
future work to design methods to better evaluate, verify
and benchmark LAMs. Last, rules and regulations should
be implemented to govern the development, deployment and
use of LAMs. This is a vital measure to enforce LAMs for
social good and prevent anti-social usage. Overall, building
responsible LAMs calls a closer collaboration in the future
among academia, industry and government.
VI. CONCLUSIONS
We highlight an ongoing paradigm shift within AI com-
munity, which is fostering large AI models for transforming
different biomedical and health sectors. The new paradigm
aims to learn a versatile foundation model on a large-scale
(multi-modal) dataset covering varied data distributions
and learning tasks. Boundaries between different intelligent
tasks, and even between different data modalities, are being
dismantled. With generalist intelligence and more unknown ca-
pabilities activated, we believe large AI models will augment,
instead of replacing, medical professionals and practitioners
in the future. Human-AI cooperation will become pervasive.
In this regard, the development of large AI models requires
even closer and more intense collaboration between domain
experts, as well as gradually established regulations.
REFERENCES
[1] OpenAI, “Chatgpt: Optimizing language models for dialogue,” 2022. [Online].
Available: https://openai.com/blog/chatgpt/
[2] A. Kirillov et al., “Segment anything,” arXiv preprint arXiv:2304.02643, 2023.
[3] A. Vaswani et al., “Attention is all you need,” NeurIPS, vol. 30, 2017.
[4] O. (2023), “Gpt-4 technical report,” arXiv:2303.08774, 2023.
[5] P. Lee, C. Goldberg, and I. Kohane, The AI Revolution in Medicine: GPT-4 and
Beyond.
Pearson Education, Limited, 2023.
[6] V. Gulshan, L. Peng, M. Coram et al., “Development and validation of a
deep learning algorithm for detection of diabetic retinopathy in retinal fundus
photographs,” jama, vol. 316, no. 22, pp. 2402–2410, 2016.
[7] R. Bommasani et al., “On the opportunities and risks of foundation models,”
arXiv:2108.07258, 2021.
[8] A. Radford et al., “Improving language understanding by generative pre-training,”
2018.
[9] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “Bert: Pre-training of deep
bidirectional transformers for language understanding,” arXiv:1810.04805, 2018.
[10] H. Touvron, T. Lavril, G. Izacard et al., “Llama: Open and efﬁcient foundation
language models,” arXiv:2302.13971, 2023.
[11] H. Touvron, L. Martin, K. Stone et al., “Llama 2: Open foundation and ﬁne-tuned
chat models,” arXiv preprint arXiv:2307.09288, 2023.
[12] H. W. Chung, L. Hou, S. Longpre et al., “Scaling instruction-ﬁnetuned language
models,” arXiv:2210.11416, 2022.
[13] A. Chowdhery, S. Narang, J. Devlin et al., “Palm: Scaling language modeling
with pathways,” arXiv:2204.02311, 2022.
[14] J. Hoffmann, S. Borgeaud, A. Mensch et al., “Training compute-optimal large
language models,” arXiv:2203.15556, 2022.
[15] S. Smith et al., “Using deepspeed and megatron to train megatron-turing nlg 530b,
a large-scale generative language model,” arXiv:2201.11990, 2022.
[16] T. L. Scao, A. Fan, C. Akiki et al., “Bloom: A 176b-parameter open-access
multilingual language model,” arXiv:2211.05100, 2022.
[17] R. Thoppilan, D. De Freitas, J. Hall et al., “Lamda: Language models for dialog
applications,” arXiv:2201.08239, 2022.
[18] S. Zhang, S. Roller, N. Goyal et al., “Opt: Open pre-trained transformer language
models,” arXiv:2205.01068, 2022.
[19] L. Ouyang, J. Wu, X. Jiang et al., “Training language models to follow instructions
with human feedback,” arXiv:2203.02155, 2022.
[20] J. W. Rae, S. Borgeaud, T. Cai et al., “Scaling language models: Methods, analysis
& insights from training gopher,” arXiv:2112.11446, 2021.
[21] V. Sanh, A. Webson, C. Raffel et al., “Multitask prompted training enables zero-
shot task generalization,” arXiv:2110.08207, 2021.
[22] J. Wei, X. Wang, D. Schuurmans et al., “Chain of thought prompting elicits
reasoning in large language models,” arXiv:2201.11903, 2022.
[23] S. Borgeaud, A. Mensch, J. Hoffmann et al., “Improving language models by
retrieving from trillions of tokens,” in ICML.
PMLR, 2022, pp. 2206–2240.
[24] P. F. Christiano, J. Leike, T. Brown et al., “Deep reinforcement learning from
human preferences,” NeurIPS, vol. 30, 2017.
[25] J. Schulman, F. Wolski, P. Dhariwal et al., “Proximal policy optimization
algorithms,” arXiv:1707.06347, 2017.
[26] A. Glaese, N. McAleese, M. Trebacz et al., “Improving alignment of dialogue
agents via targeted human judgements,” arXiv:2209.14375, 2022.
[27] A. Susano Pinto, A. Kolesnikov, Y. Shi et al., “Tuning computer vision models
with task rewards,” arXiv e-prints, pp. arXiv–2302, 2023.
[28] J. Yosinski et al., “How transferable are features in deep neural networks?”
NeurIPS, vol. 27, 2014.
[29] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei, “Imagenet: A large-
scale hierarchical image database,” in CVPR.
IEEE, 2009, pp. 248–255.
[30] T. Ridnik et al., “Imagenet-21k pretraining for the masses,” in NeurIPS.
[31] C. Sun et al., “Revisiting unreasonable effectiveness of data in deep learning era,”
in ICCV, 2017, pp. 843–852.
[32] X. Zhai et al., “Scaling vision transformers,” in CVPR, 2022, pp. 12 104–12 113.
[33] D. Mahajan et al., “Exploring the limits of weakly supervised pretraining,” in
ECCV, 2018, pp. 181–196.
[34] M. Singh et al., “Revisiting weakly supervised pre-training of visual perception
models,” in CVPR, 2022, pp. 804–814.
[35] M. Chen, A. Radford, R. Child et al., “Generative Pretraining From Pixels,” in
ICML.
PMLR, Nov. 2020.

--- Page 13 ---

QIU et al.: LARGE AI MODELS IN HEALTH INFORMATICS: APPLICATIONS, CHALLENGES, AND THE FUTURE
13
[36] M. Assran, Q. Duval, I. Misra et al., “Self-supervised learning from images with
a joint-embedding predictive architecture,” in CVPR, 2023, pp. 15 619–15 629.
[37] H. Chen, Y. Wang, T. Guo et al., “Pre-trained image processing transformer,” in
CVPR, 2021, pp. 12 299–12 310.
[38] K. He, X. Chen, S. Xie et al., “Masked Autoencoders Are Scalable Vision
Learners,” in CVPR, 2022.
[39] T. Chen, S. Kornblith, M. Norouzi, and G. Hinton, “A simple framework for
contrastive learning of visual representations,” in ICML, 2020, pp. 1597–1607.
[40] A. Dosovitskiy, L. Beyer, A. Kolesnikov et al., “An Image is Worth 16x16 Words:
Transformers for Image Recognition at Scale,” in ICLR, 2021.
[41] K. Han, A. Xiao, E. Wu et al., “Transformer in Transformer,” in NeurIPS, vol. 34,
2021, pp. 15 908–15 919.
[42] Z. Liu et al., “Swin transformer: Hierarchical vision transformer using shifted
windows,” in ICCV, 2021, pp. 10 012–10 022.
[43] Z. Liu, H. Hu, Y. Lin et al., “Swin Transformer V2: Scaling Up Capacity and
Resolution,” in ICCV, 2022.
[44] M. Dehghani, J. Djolonga, B. Mustafa et al., “Scaling vision transformers to 22
billion parameters,” ArXiv, vol. abs/2302.05442, 2023.
[45] Z. Liu et al., “A convnet for the 2020s,” in CVPR, 2022, pp. 11 976–11 986.
[46] W. Wang, J. Dai, Z. Chen et al., “Internimage: Exploring large-scale vision
foundation models with deformable convolutions,” in CVPR, 2023.
[47] Z. Dai, H. Liu, Q. V. Le, and M. Tan, “Coatnet: Marrying convolution and attention
for all data sizes,” NeurIPS, vol. 34, pp. 3965–3977, 2021.
[48] S. d’Ascoli et al., “Convit: Improving vision transformers with soft convolutional
inductive biases,” in ICML.
PMLR, 2021, pp. 2286–2296.
[49] A. Kolesnikov et al., “Big transfer (bit): General visual representation learning,”
in ECCV, 2020, pp. 491–507.
[50] M. Tan et al., “Efﬁcientnet: Rethinking model scaling for convolutional neural
networks,” in ICML, 2019, pp. 6105–6114.
[51] ——, “Efﬁcientnetv2: Smaller models and faster training,” in ICML, 2021, pp.
10 096–10 106.
[52] P. Goyal et al., “Self-supervised pretraining of visual features in the wild,”
arXiv:2103.01988, 2021.
[53] Y. Huang et al., “Gpipe: Efﬁcient training of giant neural networks using pipeline
parallelism,” NeurIPS, vol. 32, 2019.
[54] A. Radford et al., “Learning transferable visual models from natural language
supervision,” in ICML.
PMLR, 2021, pp. 8748–8763.
[55] C. Jia, Y. Yang, Y. Xia et al., “Scaling Up Visual and Vision-Language Repre-
sentation Learning With Noisy Text Supervision,” in ICML, Jul. 2021.
[56] L. Yuan, D. Chen, Y.-L. Chen et al., “Florence: A New Foundation Model for
Computer Vision,” Nov. 2021, arXiv:2111.11432 [cs].
[57] C. Schuhmann, R. Beaumont, R. Vencu et al., “LAION-5B: An open large-scale
dataset for training next generation image-text models,” in NeurIPS, Oct. 2022.
[58] A. Singh, R. Hu, V. Goswami et al., “FLAVA: A Foundational Language and
Vision Alignment Model,” in CVPR, 2022, pp. 15 638–15 650.
[59] Z. Wang, J. Yu, A. W. Yu et al., “SimVLM: Simple Visual Language Model
Pretraining with Weak Supervision,” in ICLR, Jan. 2022.
[60] X. Chen et al., “Pali: A jointly-scaled multilingual language-image model,”
arXiv:2209.06794, 2022.
[61] J. Li et al., “BLIP-2: Bootstrapping Language-Image Pre-training with Frozen
Image Encoders and Large Language Models,” Jan. 2023, arXiv:2301.12597 [cs].
[62] S. Huang, L. Dong, W. Wang et al., “Language Is Not All You Need: Aligning
Perception with Language Models,” Mar. 2023, arXiv:2302.14045 [cs].
[63] J. Li, D. Li, C. Xiong, and S. Hoi, “BLIP: Bootstrapping Language-Image Pre-
training for Uniﬁed Vision-Language Understanding and Generation,” in ICML.
PMLR, Jun. 2022, pp. 12 888–12 900, iSSN: 2640-3498.
[64] H. Pham, Z. Dai, G. Ghiasi et al., “Combined scaling for open-vocabulary image
classiﬁcation,” arXiv e-prints, pp. arXiv–2111, 2021.
[65] A. Ramesh, M. Pavlov, G. Goh et al., “Zero-Shot Text-to-Image Generation,” in
ICML, Jul. 2021.
[66] J. Yu, Y. Xu, J. Y. Koh et al., “Scaling autoregressive models for content-rich
text-to-image generation,” Transactions on Machine Learning Research, 2022.
[67] A. Ramesh, P. Dhariwal, A. Nichol et al., “Hierarchical text-conditional image
generation with clip latents,” arXiv:2204.06125, 2022.
[68] R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer, “High-resolution
image synthesis with latent diffusion models,” 2021.
[69] A. Q. Nichol et al., “Glide: Towards photorealistic image generation and editing
with text-guided diffusion models,” in ICML, 2022, pp. 16 784–16 804.
[70] C. Saharia et al., “Photorealistic text-to-image diffusion models with deep
language understanding,” arXiv:2205.11487, 2022.
[71] J. Sohl-Dickstein et al., “Deep unsupervised learning using nonequilibrium
thermodynamics,” in ICML.
PMLR, 2015, pp. 2256–2265.
[72] C. Wu, S. Yin, W. Qi et al., “Visual chatgpt: Talking, drawing and editing with
visual foundation models,” arXiv:2303.04671, 2023.
[73] R. Girdhar, A. El-Nouby, Z. Liu et al., “Imagebind: One embedding space to bind
them all,” in CVPR, 2023, pp. 15 180–15 190.
[74] Y. Zhang, K. Gong, K. Zhang et al., “Meta-transformer: A uniﬁed framework for
multimodal learning,” arXiv preprint arXiv:2307.10802, 2023.
[75] X.-C. Bai et al., “How cryo-em is revolutionizing structural biology,” Trends in
biochemical sciences, vol. 40, no. 1, pp. 49–57, 2015.
[76] K. W¨uthrich, “The way to nmr structures of proteins,” Nature structural biology,
vol. 8, no. 11, pp. 923–925, 2001.
[77] J. M. Grimes et al., “Where is crystallography going?” Acta Crystallographica
Section D: Structural Biology, vol. 74, no. 2, pp. 152–166, 2018.
[78] J. Jumper, R. Evans, A. Pritzel et al., “Highly accurate protein structure prediction
with alphafold,” Nature, vol. 596, no. 7873, pp. 583–589, 2021.
[79] R. Evans et al., “Protein complex prediction with alphafold-multimer,” BioRxiv,
pp. 2021–10, 2021.
[80] A. Madani, B. McCann, N. Naik et al., “Progen: Language modeling for protein
generation,” arXiv:2004.03497, 2020.
[81] A. Elnaggar et al., “Prottrans: Towards cracking the language of lifes code through
self-supervised deep learning and high performance computing,” IEEE TPAMI,
vol. PP, pp. 1–1, 07 2021.
[82] M. Steinegger and J. S¨oding, “Clustering huge protein sequence sets in linear
time,” Nature communications, vol. 9, no. 1, p. 2542, 2018.
[83] B. E. Suzek et al., “Uniref clusters: a comprehensive and scalable alternative
for improving sequence similarity searches,” Bioinformatics, vol. 31, no. 6, pp.
926–932, 2015.
[84] Z. Lin et al., “Evolutionary-scale prediction of atomic-level protein structure with
a language model,” Science, vol. 379, no. 6637, pp. 1123–1130, 2023.
[85] R. Wu, F. Ding, R. Wang et al., “High-resolution de novo structure prediction
from primary sequence,” BioRxiv, pp. 2022–07, 2022.
[86] M. Baek et al., “Accurate prediction of protein structures and interactions using
a three-track neural network,” Science, vol. 373, no. 6557, pp. 871–876, 2021.
[87] B. Chen, X. Cheng, L. ao Gengyang et al., “xtrimopglm: Uniﬁed 100b-scale
pre-trained transformer for deciphering the language of protein,” bioRxiv, 2023.
[88] A. Elnaggar et al., “Ankh: Optimized protein language model unlocks general-
purpose modelling,” bioRxiv, pp. 2023–01, 2023.
[89] J. Chen, Z. Hu, S. Sun et al., “Interpretable rna foundation model from unanno-
tated data for highly accurate rna structure and function predictions,” bioRxiv, pp.
2022–08, 2022.
[90] “Rnacentral 2021: secondary structure integration, improved sequence search and
new member databases,” Nucleic acids research, vol. 49, no. D1, pp. D212–D220,
2021.
[91] L. Fu, Y. Cao, J. Wu, Q. Peng, Q. Nie, and X. Xie, “Ufold: fast and accurate
rna secondary structure prediction with deep learning,” Nucleic acids research,
vol. 50, no. 3, pp. e14–e14, 2022.
[92] T. Shen, Z. Hu, Z. Peng et al., “E2efold-3d: End-to-end deep learning method for
accurate de novo rna 3d structure prediction,” arXiv:2207.01586, 2022.
[93] G. R. Buel and K. J. Walters, “Can alphafold2 predict the impact of missense
mutations on structure?” Nature Structural & Molecular Biology, vol. 29, no. 1,
pp. 1–2, 2022.
[94] E. Tiu, E. Talius, P. Patel et al., “Expert-level detection of pathologies from
unannotated chest x-ray images via self-supervised learning,” Nature Biomedical
Engineering, pp. 1–8, 2022.
[95] S. Wang et al., “Chatcad: Interactive computer-aided diagnosis on medical image
using large language models,” arXiv:2302.07257, 2023.
[96] Z. Zhao, S. Wang, J. Gu et al., “Chatcad+: Towards a universal and reliable
interactive cad using llms,” arXiv preprint arXiv:2305.15964, 2023.
[97] Y. Li, Z. Li, K. Zhang et al., “Chatdoctor: A medical chat model ﬁne-tuned on a
large language model meta-ai (llama) using medical domain knowledge,” Cureus,
vol. 15, no. 6, 2023.
[98] O. Thawkar, A. Shaker, S. S. Mullappilly et al., “Xraygpt: Chest radio-
graphs summarization using medical vision-language models,” arXiv preprint
arXiv:2306.07971, 2023.
[99] H. Wang, C. Liu, N. Xi et al., “Huatuo: Tuning llama model with chinese medical
knowledge,” arXiv preprint arXiv:2304.06975, 2023.
[100] A. Vaid, J. Jiang, A. Sawant et al., “A foundational vision transformer improves
diagnostic performance for electrocardiograms,” NPJ Digital Medicine, vol. 6,
no. 1, p. 108, 2023.
[101] Y. Li, S. Rao, J. R. A. Solares et al., “Behrt: transformer for electronic health
records,” Scientiﬁc reports, vol. 10, no. 1, pp. 1–12, 2020.
[102] L. Rasmy, Y. Xiang, Z. Xie et al., “Med-bert: pretrained contextualized embed-
dings on large-scale structured electronic health records for disease prediction,”
NPJ digital medicine, vol. 4, no. 1, p. 86, 2021.
[103] P. Shi, J. Qiu, S. M. D. Abaxi et al., “Generalist vision foundation models for
medical imaging: A case study of segment anything model on zero-shot medical
segmentation,” Diagnostics, vol. 13, no. 11, p. 1947, 2023.
[104] J. Wu, R. Fu, H. Fang et al., “Medical sam adapter: Adapting segment anything
model for medical image segmentation,” arXiv preprint arXiv:2304.12620, 2023.
[105] Z. Wang, Z. Wu, D. Agarwal, and J. Sun, “Medclip: Contrastive learning from
unpaired medical images and text,” arXiv:2210.10163, 2022.
[106] Z. Huang et al., “A visual–language foundation model for pathology image
analysis using medical twitter,” Nature Medicine, pp. 1–10, 2023.
[107] S. Chen, K. Ma, and Y. Zheng, “Med3d: Transfer learning for 3d medical image
analysis,” arXiv:1904.00625, 2019.
[108] P. Chambon et al., “Adapting pretrained vision-language foundational models to
medical imaging domains,” arXiv:2210.04133, 2022.
[109] Z. Huang, H. Wang, Z. Deng et al., “Stu-net: Scalable and transferable medical
image segmentation models empowered by large-scale supervised pre-training,”
arXiv preprint arXiv:2304.06716, 2023.
[110] T. Brown, B. Mann, N. Ryder et al., “Language models are few-shot learners,”
NeurIPS, vol. 33, pp. 1877–1901, 2020.
[111] “Pubmed
abstract,”
2023.
[Online].
Available:
https://pubmed.ncbi.nlm.nih.gov/download/
[112] “Pubmed central,” 2023. [Online]. Available: https://www.ncbi.nlm.nih.gov/pmc/
[113] J. Lee et al., “Biobert: a pre-trained biomedical language representation model
for biomedical text mining,” Bioinformatics, vol. 36, no. 4, pp. 1234–1240, 2020.
[114] E. Alsentzer et al., “Publicly available clinical bert embeddings,” arXiv, 2019.
[115] H.-C. Shin, Y. Zhang, E. Bakhturina et al., “Biomegatron: Larger biomedical
domain language model,” arXiv:2010.06060, 2020.

--- Page 14 ---

14
[116] S. Gururangan, A. Marasovi´c, S. Swayamdipta et al., “Don’t stop pretraining:
Adapt language models to domains and tasks,” arXiv:2004.10964, 2020.
[117] L. Rasmy, Y. Xiang, Z. Xie, C. Tao, and D. Zhi, “Med-bert: pretrained contextu-
alized embeddings on large-scale structured electronic health records for disease
prediction,” NPJ digital medicine, vol. 4, no. 1, p. 86, 2021.
[118] K. raj Kanakarajan, B. Kundumani, and M. Sankarasubbu, “Bioelectra: pretrained
biomedical text encoder using discriminators,” in Proceedings of the 20th Work-
shop on Biomedical Language Processing, 2021, pp. 143–154.
[119] Y. Gu, R. Tinn, H. Cheng et al., “Domain-speciﬁc language model pretraining for
biomedical natural language processing,” HEALTH, vol. 3, no. 1, pp. 1–23, 2021.
[120] M. Yasunaga, J. Leskovec, and P. Liang, “Linkbert: Pretraining language models
with document links,” arXiv:2203.15827, 2022.
[121] R. Luo et al., “Biogpt: generative pre-trained transformer for biomedical text
generation and mining,” Brieﬁngs in Bioinformatics, vol. 23, no. 6, 2022.
[122] K. Singhal, S. Azizi, T. Tu et al., “Large language models encode clinical
knowledge,” arXiv:2212.13138, 2022.
[123] X. Yang, A. Chen, N. PourNejatian et al., “A large language model for electronic
health records,” npj Digital Medicine, vol. 5, no. 1, p. 194, 2022.
[124] E. J. Hu, Y. Shen, P. Wallis et al., “Lora: Low-rank adaptation of large language
models,” arXiv preprint arXiv:2106.09685, 2021.
[125] T. Han, L. C. Adams, J.-M. Papaioannou et al., “Medalpaca–an open-source
collection of medical conversational ai models and training data,” arXiv preprint
arXiv:2304.08247, 2023.
[126] J. Wei et al., “Emergent abilities of large language models,” arXiv, 2022.
[127] M. Agrawal, S. Hegselmann, H. Lang, Y. Kim, and D. Sontag, “Large language
models are few-shot clinical information extractors,” arXiv:2205.12689, 2022.
[128] K. Singhal, T. Tu, J. Gottweis et al., “Towards expert-level medical question
answering with large language models,” arXiv preprint arXiv:2305.09617, 2023.
[129] V. Li´evin, C. E. Hother, and O. Winther, “Can large language models reason about
medical questions?” arXiv:2207.08143, 2022.
[130] S. B. Patel and K. Lam, “Chatgpt: the future of discharge summaries?” The Lancet
Digital Health, 2023.
[131] “Fairway health - process prior authorization faster,” 2023. [Online]. Available:
https://www.ycombinator.com/launches/IIu-fairway-health-process-prior-authorization-faster
[132] T. H. Kung, M. Cheatham, A. Medenilla et al., “Performance of chatgpt on usmle:
Potential for ai-assisted medical education using large language models,” PLOS
Digital Health, vol. 2, no. 2, p. e0000198, 2023.
[133] E. Shue, L. Liu, B. Li, Z. Feng, X. Li, and G. Hu, “Empowering beginners in
bioinformatics with chatgpt,” bioRxiv, pp. 2023–03, 2023.
[134] H. Dai, Z. Liu, W. Liao et al., “Chataug: Leveraging chatgpt for text data
augmentation,” arXiv:2302.13007, 2023.
[135] E. Mitchell et al., “Detectgpt: Zero-shot machine-generated text detection using
probability curvature,” arXiv:2301.11305, 2023.
[136] X. Lin, C. Xu, Z. Xiong et al., “Pangu drug model: learn a molecule like a
human,” bioRxiv, pp. 2022–03, 2022.
[137] D. M. Korngiebel and S. D. Mooney, “Considering the possibilities and pitfalls of
generative pre-trained transformer 3 (gpt-3) in healthcare delivery,” NPJ Digital
Medicine, vol. 4, no. 1, p. 93, 2021.
[138] E. Chen, K. Lerman, E. Ferrara et al., “Tracking social media discourse about the
covid-19 pandemic: Development of a public coronavirus twitter data set,” JMIR
public health and surveillance, vol. 6, no. 2, p. e19273, 2020.
[139] J. Peng et al., “Clustering egocentric images in passive dietary monitoring with
self-supervised learning,” in IEEE-EMBS BHI.
IEEE, 2022, pp. 01–04.
[140] J. Qiu et al., “Egocentric image captioning for privacy-preserved passive dietary
intake monitoring,” IEEE Transactions on Cybernetics, 2023.
[141] B. M. Popkin, C. Corvalan, and L. M. Grummer-Strawn, “Dynamics of the double
burden of malnutrition and the changing nutrition reality,” The Lancet, 2019.
[142] T. Nguyen, J. Brandstetter, A. Kapoor et al., “Climax: A foundation model for
weather and climate,” arXiv:2301.10343, 2023.
[143] K. Bi, L. Xie, H. Zhang et al., “Accurate medium-range global weather forecasting
with 3d neural networks,” Nature, pp. 1–6, 2023.
[144] Z. Wang, C. Liu, S. Zhang et al., “Foundation model for endoscopy video analysis
via large-scale self-supervised pre-train,” arXiv preprint arXiv:2306.16741, 2023.
[145] G. D’Onofrio, L. Fiorini, A. Sorrentino et al., “Emotion recognizing by a robotic
solution initiative (emotive project),” Sensors, vol. 22, no. 8, p. 2861, 2022.
[146] J. Qiu, L. Chen, X. Gu et al., “Egocentric human trajectory forecasting with a
wearable camera and multi-modal fusion,” IEEE Robotics and Automation Letters,
vol. 7, no. 4, pp. 8799–8806, 2022.
[147] P. Asgharian, A. M. Panchea, and F. Ferland, “A review on the use of mobile
service robots in elderly care,” Robotics, vol. 11, no. 6, p. 127, 2022.
[148] L.
Seenivasan,
M.
Islam,
G.
Kannan
et
al.,
“Surgicalgpt:
End-to-end
language-vision gpt for visual question answering in surgery,” arXiv preprint
arXiv:2304.09974, 2023.
[149] S.
Vemprala,
R.
Bonatti,
A.
Bucker,
and
A.
Kapoor,
“Chatgpt
for
robotics:
Design
principles
and
model
abilities,”
Microsoft,
Tech.
Rep.
MSR-TR-2023-8,
February
2023.
[Online].
Available:
https://www.microsoft.com/en-us/research/publication/chatgpt-for-robotics-design-principles-and-model-abilities/
[150] S. Reed et al., “A generalist agent,” TMLR, 2022.
[151] M. Shridhar et al., “Cliport: What and where pathways for robotic manipulation,”
in Conference on Robot Learning.
PMLR, 2022, pp. 894–906.
[152] ——, “Perceiver-actor: A multi-task transformer for robotic manipulation,”
arXiv:2209.05451, 2022.
[153] M. Ahn, A. Brohan, N. Brown et al., “Do as i can and not as i say: Grounding
language in robotic affordances,” in arXiv:2204.01691, 2022.
[154] D. Driess, F. Xia, M. S. M. Sajjadi et al., “Palm-e: An embodied multimodal
language model,” in arXiv:2303.03378, 2023.
[155] Y. Jiang, A. Gupta, Z. Zhang et al., “Vima: General robot manipulation with
multimodal prompts,” arXiv:2210.03094, 2022.
[156] A. Brohan, N. Brown, J. Carbajal et al., “Rt-1: Robotics transformer for real-world
control at scale,” arXiv:2212.06817, 2022.
[157] N. Ding, Y. Qin, G. Yang et al., “Parameter-efﬁcient ﬁne-tuning of large-scale
pre-trained language models,” Nature Machine Intelligence, vol. 5, no. 3, pp.
220–235, 2023.
[158] S. Gilbert, H. Harvey, T. Melvin et al., “Large language model ai chatbots require
approval as medical devices,” Nature Medicine, pp. 1–3, 2023.
[159] X. Shen, Z. Chen, M. Backes, and Y. Zhang, “In chatgpt we trust? measuring and
characterizing the reliability of chatgpt,” arXiv preprint arXiv:2304.08979, 2023.
[160] P. Lee, S. Bubeck, and J. Petro, “Beneﬁts, limits, and risks of gpt-4 as an ai
chatbot for medicine,” New England Journal of Medicine, vol. 388, no. 13, pp.
1233–1239, 2023.
[161] H. Nori, N. King, S. M. McKinney, D. Carignan, and E. Horvitz, “Capabilities of
gpt-4 on medical challenge problems,” arXiv preprint arXiv:2303.13375, 2023.
[162] J. Wang, X. Hu, W. Hou et al., “On the robustness of chatgpt: An adversarial and
out-of-distribution perspective,” arXiv:2302.12095, 2023.
[163] L. Li and M. W. Spratling, “Data augmentation alone can improve adversarial
training,” in ICLR, 2023.
[164] N. Carlini, F. Tramer, E. Wallace, M. Jagielski, A. Herbert-Voss, K. Lee,
A. Roberts, T. B. Brown, D. Song, U. Erlingsson et al., “Extracting training
data from large language models.” in USENIX Security Symposium, vol. 6, 2021.
[165] N. Carlini, D. Ippolito, M. Jagielski, K. Lee, F. Tramer, and C. Zhang,
“Quantifying memorization across neural language models,” arXiv preprint
arXiv:2202.07646, 2022.
[166] H. Li, D. Guo, W. Fan, M. Xu, and Y. Song, “Multi-step jailbreaking privacy
attacks on chatgpt,” arXiv preprint arXiv:2304.05197, 2023.
[167] R. Shokri, M. Stronati, C. Song, and V. Shmatikov, “Membership inference attacks
against machine learning models,” in 2017 IEEE symposium on security and
privacy (SP).
IEEE, 2017, pp. 3–18.
[168] J. Duan, F. Kong, S. Wang, X. Shi, and K. Xu, “Are diffusion models vulnerable
to membership inference attacks?” arXiv preprint arXiv:2302.01316, 2023.
[169] “How your data is used to improve model performance,” 2023. [Online]. Available:
https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance
[170] “March 20 chatgpt outage: Here’s what happened,” 2023. [Online]. Available:
https://openai.com/blog/march-20-chatgpt-outage
[171] K. Greshake, S. Abdelnabi, S. Mishra et al., “More than you’ve asked for: A
comprehensive analysis of novel prompt injection threats to application-integrated
large language models,” arXiv preprint arXiv:2302.12173, 2023.
[172] W. J. Hall, M. V. Chapman, K. M. Lee et al., “Implicit racial/ethnic bias among
health care professionals and its inﬂuence on health care outcomes: a systematic
review,” American journal of public health, vol. 105, no. 12, pp. e60–e76, 2015.
[173] Z. Obermeyer, B. Powers, C. Vogeli, and S. Mullainathan, “Dissecting racial bias
in an algorithm used to manage the health of populations,” Science, vol. 366, no.
6464, pp. 447–453, 2019.
[174] D. Cirillo, S. Catuara-Solarz, C. Morey et al., “Sex and gender differences
and biases in artiﬁcial intelligence for biomedicine and healthcare,” NPJ digital
medicine, vol. 3, no. 1, p. 81, 2020.
[175] D. S. Char, N. H. Shah, and D. Magnus, “Implementing machine learning in health
care—addressing ethical challenges,” The New England journal of medicine, vol.
378, no. 11, p. 981, 2018.
[176] J. Rutinowski, S. Franke, J. Endendyk, I. Dormuth, and M. Pauly, “The self-
perception and political biases of chatgpt,” arXiv:2304.07333, 2023.
[177] T. Y. Zhuo, Y. Huang, C. Chen et al., “Exploring ai ethics of chatgpt: A diagnostic
analysis,” arXiv:2301.12867, 2023.
[178] D. Hendrycks, C. Burns, S. Basart, A. Critch, J. Li, D. Song, and J. Steinhardt,
“Aligning ai with shared human values,” arXiv preprint arXiv:2008.02275, 2020.
[179] S. Gehman, S. Gururangan, M. Sap, Y. Choi, and N. A. Smith, “Realtoxi-
cityprompts: Evaluating neural toxic degeneration in language models,” arXiv
preprint arXiv:2009.11462, 2020.
[180] G. Daras and A. G. Dimakis, “Discovering the hidden vocabulary of dalle-2,”
arXiv preprint arXiv:2206.00169, 2022.
[181] Y. Wang, P. Shi, and H. Zhang, “Investigating the existence of” secret language”in
language models,” arXiv preprint arXiv:2307.12507, 2023.
[182] T. Kojima, S. S. Gu, M. Reid et al., “Large language models are zero-shot
reasoners,” Advances in neural information processing systems, vol. 35, pp.
22 199–22 213, 2022.
[183] N. Elhage, N. Nanda, C. Olsson et al., “A mathematical framework for transformer
circuits,” Transformer Circuits Thread, vol. 1, 2021.
[184] D. Patterson et al., “Carbon emissions and large neural network training,” arXiv
preprint arXiv:2104.10350, 2021.
[185] D. Patterson, J. Gonzalez, U. H¨olzle et al., “The carbon footprint of machine
learning training will plateau, then shrink,” Computer, vol. 55, no. 7, 2022.
[186] E. F. Villaronga, P. Kieseberg, and T. Li, “Humans forget, machines remember:
Artiﬁcial intelligence and the right to be forgotten,” Computer Law & Security
Review, vol. 34, no. 2, pp. 304–313, 2018.
[187] Y. LeCun, “A path towards autonomous machine intelligence version 0.9. 2, 2022-
06-27,” 2022.
[188] P. Liu, W. Yuan, J. Fu et al., “Pre-train, prompt, and predict: A systematic survey
of prompting methods in natural language processing,” ACM Computing Surveys,
vol. 55, no. 9, pp. 1–35, 2023.
[189] D. Leslie, “Understanding artiﬁcial intelligence ethics and safety,” arXiv preprint
arXiv:1906.05684, 2019.
[190] S. A. Siddiqui, N. Rajkumar, T. Maharaj et al., “Metadata archaeology: Unearthing
data subsets by leveraging training dynamics,” in ICLR, 2022.

--- Page 15 ---

QIU et al.: LARGE AI MODELS IN HEALTH INFORMATICS: APPLICATIONS, CHALLENGES, AND THE FUTURE
15
[191] X. Huang et al., “A survey of safety and trustworthiness of large language models
through the lens of veriﬁcation and validation,” arXiv:2305.11391, 2023.

```
