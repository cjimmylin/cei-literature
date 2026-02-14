---
title: "2024-Yang-Large Language Models Meet Text-Centric Multimodal Sentiment Analysis - PDF Extract"
source_pdf: "2024-Yang-Large Language Models Meet Text-Centric Multimodal Sentiment Analysis.pdf"
pages: 40
extracted_at: "2026-02-13T17:43:18.666994"
---

# PDF Extract: 2024-Yang-Large Language Models Meet Text-Centric Multimodal Sentiment Analysis

**Source PDF:** 2024-Yang-Large Language Models Meet Text-Centric Multimodal Sentiment Analysis.pdf
**Total Pages:** 40

---

## Content

```
--- Page 1 ---

. RESEARCH PAPER .
Large Language Models Meet Text-Centric
Multimodal Sentiment Analysis: A Survey
Hao YANG1*, Yanyan ZHAO1*, Yang WU1, Shilong WANG1, Tian ZHENG1,
Hongbo ZHANG1, Zongyang Ma2, Wanxiang CHE1 & Bing QIN1
1Harbin Institute of Technology, Harbin 150001, China;
2Chinese Academy of Sciences, Beijing 100190, China
Abstract
Compared to traditional sentiment analysis, which only considers text, multimodal sentiment analysis needs
to consider emotional signals from multimodal sources simultaneously and is therefore more consistent with
the way how humans process sentiment in real-world scenarios. It involves processing emotional information
from various sources such as natural language, images, videos, audio, physiological signals, etc. However,
although other modalities also contain diverse emotional cues, natural language usually contains richer con-
textual information and therefore always occupies a crucial position in multimodal sentiment analysis. The
emergence of ChatGPT has opened up immense potential for applying large language models (LLMs) to
text-centric multimodal tasks. However, it is still unclear how existing LLMs can adapt better to text-centric
multimodal sentiment analysis tasks. This survey aims to (1) present a comprehensive review of recent re-
search in text-centric multimodal sentiment analysis tasks, (2) examine the potential of LLMs for text-centric
multimodal sentiment analysis, outlining their approaches, advantages, and limitations, (3) summarize the
application scenarios of LLM-based multimodal sentiment analysis technology, and (4) explore the challenges
and potential research directions for multimodal sentiment analysis in the future.
Keywords
Text-Centric, Multimodal Sentiment Analysis, Large Langauge Models, Survey
1
Introduction
Text-based sentiment analysis is a crucial research task in the field of natural language processing, aiming
at automatically uncovering the underlying attitude that we hold towards textual content. However,
humans often process emotions in a multi-modal environment, which differs from text-based scenarios in
the following ways:
1) Humans have the ability to acquire and integrate multimodal fine-grained signals.
Humans often find themselves in multimodal scenarios, manifested as seamlessly understanding others’
intentions and emotions through the combined effects of language, images, sound, and physiological
signals. When processing emotions, humans have the ability to sensitively capture and integrate fine-
grained sentiment signals from multiple modalities, and correlate them for emotional reasoning.
2) Multimodal expression ability. The ways in which humans express emotions include language,
facial expressions, body movements, speech, etc. For example, in daily conversations, our natural lan-
guage expressions may be vague (such as someone saying “okay”), but when combined with other modal
information, like visual modalities (e.g. a happy facial expression) or audio modalities (e.g. a prolonged
intonation), the emotions expressed are different.
It is evident that the study of sentiment analysis within a multimodal context brings us closer to
authentic human emotion processing. Research into multimodal sentiment analysis technologies [5, 109]
with human-like emotion processing capabilities will provide technical support for real-world applications
such as high-quality intelligent companions, customer service, e-commerce, and depression detection.
In recent years, large language models (LLMs) [2–4] have demonstrated astonishing human-machine
* Corresponding author (email: hyang@ir.hit.edu.cn, yyzhao@ir.hit.edu.cn)
arXiv:2406.08068v2  [cs.CL]  16 Aug 2024

--- Page 2 ---

Author Hao YANG, et al.
2
Text-Centric Multimodal Sentiment Analysis with Large Language Models
Introduction
 Large Language Models
Background 
Large Language
Models
Large
Multimodal 
Models
Text-Centric Multimodal Sentiment Analysis Tasks
Coarse-grained
Level
Fine-grained 
Level
Audio-Image-Text
Sentiment Analysis
Image-Text
Sentiment
Classification
Image-Text
Sarcasm Detection
Image-Text 
Emotion
Classification
Multimodal Aspect-Based
Sentiment Classification
Joint Multimodal Aspect-
Based Sentiment Analysis
Video-based 
Emotion
Classification
Multimodal Sentiment
Analysis Evaluations
Prompting
Strategy
Evaluation
Metrics
 Reference
Results
Applications of
Multimodal  Sentiment
Analysis
Comment Analysis
Multimodal
Intelligent Human-
machine Interaction
Basic Concepts of
Multimodal Sentiment
Analysis
Image-Text Sentiment
Analysis
Multimodal Aspect Term
Extraction
Video-based
Sarcasm Detection
Video-based
Sentiment
Classification
Multimodal Sarcasm
Detection
Figure 1
Organization of the review article.
conversational capabilities and showcased impressive performance across a wide range of natural language
processing tasks, indicating their rich knowledge and powerful reasoning abilities. At the same time, large
multimodal models (LMM) that increase the ability to understand modalities such as images also provide
new ideas for multimodal-related tasks.
They can directly perform tasks with zero-shot or few-shot
context learning, requiring no supervised training [7, 10–12]. While there have been some attempts to
apply LLMs in text-based sentiment analysis [6–9, 108], there is a lack of systematic and comprehensive
analysis regarding the application of LLMs and LMMs in multimodal sentiment analysis. Therefore, it
remains unclear to what extent existing LLMs and LMMs can be used for multimodal sentiment analysis.
Given the crucial role of natural language in multi-modal sentiment analysis and its essential input for
current LLMs and LMMs, we concentrate on text-centric multimodal sentiment analysis tasks that can
leverage LLMs to enhance performance, such as image-text sentiment classification, image-text emotion
classification, audio-image-text (video) sentiment classification, etc. In this work, we aim to provide a
comprehensive review of the current state of text-centric multimodal sentiment analysis methods based on
LLMs and LMMs. Specifically, we focus on the following questions: 1) How do LLMs and LMMs perform
in a variety of multimodal sentiment analysis tasks? 2) What are the differences among approaches to
utilize LLMs and LMMs in various multimodal sentiment analysis tasks, and what are their respective
strengths and limitations? 3) What are the future application scenarios of multimodal sentiment analysis?
To this end, we first introduce the tasks and the most recent advancements in text-centric multimodal
sentiment analysis. We also outline the primary challenges faced by current technologies and propose
potential solutions. We examine a total of 14 multimodal sentiment analysis tasks, which have tradi-
tionally been studied independently. We analyze the distinct characteristics and commonalities of each
task. The structure of the review study is depicted in Figure 1. Since LMMs are also based on LLMs,
for convenience of presentation, the methods based on LLMs below include methods based on LMMs.
The rest of the sections of this paper are organized as follows. Section 2 introduces the background
of LLMs and LMMs.
In Section 3, we conduct an extensive survey on a wide range of text-centric
multimodal sentiment analysis tasks, detailing the task definitions, related datasets and the latest meth-
ods. We also summarize the advantages and advancements of LLM compared to previous techniques in
multimodal sentiment analysis tasks, as well as the challenges still faced. In Section 4, We introduced
the prompt settings, evaluation metrics, and reference results related to LLMs-based text-centric multi-

--- Page 3 ---

Author Hao YANG, et al.
3
modal sentiment analysis methods. In Section 5, we look forward to the future application scenarios of
multimodal sentiment analysis, followed by concluding remarks in Section 6.
2
Background on Large Language Models
2.1
Large Language Models
Generally, LLMs refer to transformer models with hundreds of billions (or more) of parameters, which
are trained on large amounts of text data at a high cost, such as GPT-3 [2], PaLM [22], Galactica
[23], and LLaMA2 [24]. LLMs typically possess extensive knowledge and demonstrate strong abilities in
understanding, generating natural language, and solving complex tasks in practical. LLMs exhibit some
abilities that are not present in small models, which is the most prominent feature that distinguishes
LLM from previous pre-trained language models(PLMs), for example, in-context learning (ICL) capacity.
Assuming that the language model has been provided with natural language instructions and several task
demonstrations, it can generate the expected output of the test instance by completing the word sequence
of the input text without additional training or gradient updates; Instruction following. By fine-tuning
the mixture of multi-task datasets formatted through natural language descriptions (known as instruction
adaptation), LLM performs well on unseen tasks also described in instruction form. Through fine-tuning
instructions, LLM is able to follow task instructions for new tasks without using explicit examples,
thus improving generalization ability. Step-by-step reasoning. For small language models(SLMs), it is
often difficult to solve complex tasks involving multiple reasoning steps, such as mathematical word
problems. Instead, using the chain-of-thought (CoT) cueing strategy [25–27], LLMs can solve such tasks
by leveraging a cueing mechanism that involves intermediate reasoning steps to derive the final answer.
There have been some preliminary attempts to evaluate LLMs for text sentiment analysis tasks. In [7],
the authors observed that the zero-shot performance of LLMs can be compared with fine-tuning BERT
models [105]. In addition, in [8], the authors conducted preliminary research on some sentiment analysis
tasks using ChatGPT, specifically studying its ability to handle polarity changes, open-domain scenarios,
and emotional reasoning problems. In [9], the authors comprehensively tested the effectiveness of LLMs
in text sentiment analysis datasets. In [28], the authors tested the effectiveness of commercial LLMs
on a multimodal video-based sentiment analysis dataset. Despite these existing efforts, their scope is
often limited to partial tasks and involves different datasets and experimental designs. Our goal is to
comprehensively summarize the performance of LLMs in the field of multimodal sentiment analysis.
2.2
Large Multimodal Models
Large multimodal models (LMMs) are created to handle and integrate various data types, such as text,
images, audio, and video. LMMs extend the capabilities of LLMs by incorporating additional modalities,
allowing for a more comprehensive understanding and generation of diverse content. The development of
LMMs is driven by the need to more accurately reflect the multimodal nature of human communication
and perception.
While traditional LLMs like GPT-4 are primarily text-based, LMMs are capable of
processing and generating outputs across various data types. For instance, they can interpret visual
inputs, generate textual descriptions from images, and even handle audio data, thus bridging the gap
between different forms of information. One of the critical advancements in LMMs is the ability to create a
unified multimodal embedding space. This involves using separate encoders for each modality to generate
data-specific representations, which are then aligned into a cohesive multimodal space.
This unified
approach allows the models to integrate and correlate information from different sources seamlessly.
Notable examples include Gemini [111], GPT-4V, and ImageBind [110]. These models showcase the
ability to process text, images, audio, and video, enhancing functionalities such as translation, image
recognition, and more. In addition to these well-known models, other emerging models are also making
significant strides: BLIP-2 [112] introduces a novel approach to integrate a frozen pre-trained visual
encoder with a frozen large language model using a Q-former module. This module employs learnable
input queries that interact with image features and the LLM, allowing for effective cross-modal learning.
This setup helps maintain the versatility of the LLM while incorporating visual information effectively.
LLava [113] is a represent large multimodal model integrating a pre-trained CLIP [116] visual encoder
(ViT-L/14), the Vicuna [115] language model, and a simple linear projection layer. Its training involves

--- Page 4 ---

Author Hao YANG, et al.
4
two stages: feature alignment pre-training, where only the projection layer is trained using 595K image-
text pairs from Conceptual Captions dataset [118], and end-to-end fine-tuning, where the projection
layer and LLM are fine-tuned using 158K instruction-following data and the ScienceQA dataset [117].
This setup ensures effective integration of visual and textual information, enabling LLava to excel in
image captioning, visual question answering, and visual reasoning tasks.
Qwen-VL [114] is a strong
performer in the multimodal domain.
Qwen-VL excels in tasks such as zero-shot image captioning
and visual question answering, supporting both English and Chinese text recognition. Qwen-VL-Chat
enhances interaction capabilities with multi-image inputs and multi-round question answering, showcasing
significant improvements in understanding and generating multimodal content.
2.3
Usage of Large Language Models
In [208], the authors summarize two paradigms for utilizing LLMs: Parameter-frozen application
directly applies prompting approach on LLMs without the need for parameter tuning. This category
includes zero-shot and few-shot learning, depending on whether the few-shot demonstrations is required.
Parameter-tuning application refers to the need for tuning parameters of LLMs. This category includes
both full-parameter and parameter-efficient tuning, depending on whether fine-tuning is required for all
model parameters.
In zero-shot learning, LLMs leverage the instruction following capabilities to solve downstream tasks
based on a given instruction prompt, which is defined as:
P = Prompt(I),
(1)
where I and P denote the input and output of prompting, respectively.
Few-shot learning uses in-context learning capabilities to solve the downstream tasks imitating few-
shot demonstrations. Formally, given some demonstrations E, the process of few-shot learning is defined
as:
P = Prompt(E, I).
(2)
In the full-parameter tuning approach, all parameters of the model M are fine-tuned on the training
dataset D:
c
M = Fine-tune(M|D),
(3)
where c
M is the fine-tuned model with the updated parameters.
Parameter-efficient tuning (PET) involves adjusting a set of existing parameters or incorporating ad-
ditional tunable parameters (like Bottleneck Adapter [209], Low-Rank Adaptation (LoRA) [210], Prefix-
tuning [211], and QLoRA [212]) to efficiently adapt models for specific downstream tasks. Formally,
parameter-efficient tuning first tunes a set of parameters W, denoting as:
c
W = Fine-tune(W|D, M),
(4)
where c
W stands for the trained parameters.
3
Text-Centric Multimodal Sentiment Analysis Tasks
Text-centered multimodal sentiment analysis mainly includes image-text sentiment analysis and audio-
image-text (video) sentiment analysis. Among them, according to different emotional annotations, the
two most common tasks are sentiment classification tasks (such as the most common three label clas-
sification tasks of positive, neutral, and negative) and emotion classification tasks (including emotional
labels such as happy, sad, angry, etc). Similar to text-based sentiment classification, text-centered multi-
modal sentiment analysis can also be categorized into coarse-grained multimodal sentiment analysis (e.g.,
sentence-level) and fine-grained multimodal sentiment analysis (e.g., aspect-level) based on the granularity
of the opinion targets. Existing fine-grained multimodal sentiment analysis usually focuses on image-text
pair data, and includes multimodal aspect term extraction (MATE), multimodal aspect-based sentiment
classification (MASC), and joint multimodal aspect-sentiment analysis (JMASA). Additionally, multi-
modal sarcasm detection has also become a widely discussed task in recent years.
Due to the need

--- Page 5 ---

Author Hao YANG, et al.
5
to analyze conflicts between different modalities of sentiment, it highlights the importance of non-text
modalities in sentiment judgment in real-world scenarios. We will introduce these tasks in the following
subsections, and summarize them in Table 1.
Table 1
Categorization and representative methods for text-centric multimodal sentiment analysis.
Category
Task
Datasets
Methods
Image-Text
Coarse-grained
Image-Text Sentiment Classification
MVSA [121], MEMOTION 2 [123], MSED [140]
[31, 130–137, 168, 169]
Image-Text Emotion Classification
TumEoM [127], MEMOTION 2 [123], MSED [140]
[127, 137, 139, 168, 169]
Image-Text Sarcasm Detection
MMSD [120], MMSD2.0 [205]
[55, 194–200, 202, 203, 205–207]
Fine-grained
Multimodal Aspect Term Extraction
Twitter-15 [79], Twitter-17 [79]
[96, 145–150]
Multimodal Aspect Sentiment Classification
Multi-ZOL [77], Twitter-15 [79], Twitter-17 [79]
[32, 77–79, 98, 160, 168, 169]
Joint Multimodal Aspect-Sentiment Analysis
Twitter-15 [79], Twitter-17 [79]
[80, 161–167, 170, 171]
Video
Video-based Sentiment Classification
ICT-MMMO [193],CMU-MOSI [99],
CMU-MOSEI [100], CMU-MOSEAS [125],
CH-SIMS [101], CH-SIMS 2 [173], MELD [122]
[33–43, 181–192, 204]
Video-based Emotion Classification
MELD [122],IEMOCAP [126],CMU-MOSEI [100],
M3ED [174],MER2023 [175],
EMER [177],ER2024 [176]
[122, 126, 174–177, 184]
[186–188, 190, 192]
Video-based Sarcasm Detection
MUStARD [124]
[53, 54, 57]
3.1
Basic Concepts of Multimodal Sentiment Analysis
Multimodal sentiment analysis (MSA) differs from traditional text-based sentiment analysis in that it
combines multiple modalities, such as images and speech, to enhance the accuracy of sentiment classifi-
cation. The most common multimodal sentiment analysis scenarios include “image-text”, “audio-image”
and “audio-image-text” (video). For example, the sentence ”That’s great!” expresses a positive emotion
when analyzed as text alone, but when combined with an eye-rolling expression and a sharp tone of
voice, the overall sentiment is sarcastically negative. Additionally, multimodal scenarios can also extend
to more modalities that can reflect human emotions, such as “physiological signals” (skin conductance,
electromyography, blood pressure, electroencephalography, respiration, pulse, electrocardiogram, etc.).
In the following chapters of this paper, we will primarily focus on key tasks and techniques for text-
centric multimodal sentiment analysis in “image-text” and “audio-image-text” (video) scenarios that can
leverage large language models (LLMs). Since the “physiological signals” modality is interdisciplinary,
encompassing fields like neuroscience and psychology, and has wide-ranging application potential, we will
also provide a brief overview of it.
Although multimodal data contains richer information, effectively integrating multimodal information
is a key challenge in current multimodal sentiment analysis tasks. Unlike sentiment expression in text-
only modalities, sentiment expression in a multimodal context has its own particularities, including:
1) Complexity of sentiment semantic representation. In multimodal scenarios, sentiment semantics are
derived from the representations of each participating modality. However, each single modality can have
various representation methods, making the selection of which representation to use and how to fuse
the representations from multiple modalities complex. 2) Complementarity of sentiment elements. Due
to the participation of other modalities, the textual modality often has shorter and less informative
expressions. Fine-grained sentiment elements from other modalities can provide effective supplements.
3) Inconsistency in sentiment expression: There can be conflicts in sentiment expressions among different
modalities in the same scenario, with irony being the most common example.
Therefore, the core of multimodal sentiment analysis includes independent representation of single-
modal sentiment semantics and fusion of multimodal sentiment semantic representations.
Independent representation of multimodal semantics refers to encoding each type of modality data
separately. The encoding for each modality may take different forms and may not exist in the same
semantic space. With the development of deep learning, deep learning techniques have shown outstanding
performance in fields such as natural language processing, computer vision, and speech recognition. One
of the greatest advantages is that many deep learning models (such as CNN [85]: Convolutional Neural
Network) and concepts can be used across these three research areas, significantly lowering the research
threshold for researchers and breaking down the barriers to joint representation of multimodal semantics.
Each modality can be represented as vector information through deep learning models, and simple vector
concatenation and addition can achieve the most basic multimodal semantic fusion, which serves as
the basis for completing other multimodal downstream tasks. Additionally, researchers have found that

--- Page 6 ---

Author Hao YANG, et al.
6
each modality’s representation is an independent modality space representation, residing in different
vector spaces.
Although rigid concatenation and addition have shown some effects, their theoretical
significance is hard to justify.
Therefore, scholars have begun to think about how to unify multiple
modality representations into the same semantic space. For example, CLIP [116] uses techniques like
contrastive learning and pre-training to obtain unified representations of images and text. This unified
representation of multimodal semantics is also referred to as multimodal semantic fusion.
The fusion of multimodal sentiment semantic representation typically includes feature layer fusion,
algorithm layer fusion, and decision layer fusion [119]. Feature layer Fusion (Early Fusion). This refers to
the straightforward method of feature concatenation directly after extracting features from each modality.
Algorithm Layer Fusion (Model-level Fusion). This refers to thoroughly integrating each modality within
different algorithmic frameworks. For example, two modalities can undergo nonlinear transformations
through their respective deep learning models to achieve more abstract representations, sharing the same
loss function to achieve comprehensive modality fusion. Decision Layer Fusion (Late Fusion). This refers
to combining each modality’s representations with specific classification tasks to obtain independent
representations for each modality and then using these to make the final classification decision. These
approaches aim to address how to eliminate conflicts between modalities and how to achieve information
complementarity among them.
Table 2
Datasets of text-centric multimodal sentiment analysis task. We use ’Emotions’ to indicate that the dataset includes
emotional labels, for example, happy, surprise, sad, angry, etc. And numeric intervals to represent the sentiment scoring annotations
of the dataset.
Dataset
Language
Source
year
Size
Modalities
Labels
ICT-MMMO [172]
English
YouTube
2011
340
A+V+T
[-2,2]
IEMOCAP [126]
English
Shows
2008
10,039
A+V+T
Emotions
CMU-MOSI [99]
English
YouTube
2016
2,199
A+V+T
Neg, Neu, Pos
CMU-MOSEI [100]
English
YouTube
2018
23,453
A+V+T
Neg, Neu, Pos and Emotions
MELD [122]
English
Movies, TVs
2019
1,443
A+V+T
Neg, Neu, Pos and Emotions
CH-SIMS [101]
Chinese
Movies, TVs
2020
2,281
A+V+T
[-1,1]
CH-SIMS 2 [173]
Chinese
Movies, TVs
2022
4,406
A+V+T
[-1,1]
M3ED [174]
Chinese
Movies, TVs
2022
24,449
A+V+T
Emotions
MER2023 [175]
Chinese
Movies, TVs
2023
3,784
A+V+T
Emotions
EMER [177]
Chinese
Movies, TVs
2023
100
A+V+T
Emotions, Reasoning
MER2024 [176]
Chinese
Movies, TVs
2024
6,199
A+V+T
Emotions
CMU-MOSEAS [125]
Spanish, Portuguese,
German, French
YouTube
2021
40,000
A+V+T
[-3,3], [0,3]
UR-FUNNY [178]
English
Speech Video
2023
16,514
A+V+T
Funny
TumEoM [127]
English
Tumblr
2020
195,264
V+T
Emotions
MVSA [121]
English
Twitter
2021
19,598
V+T
Neg, Neu, Pos
Multi-ZOL [77]
Chinese
ZOL.com
2019
5,288
V+T
[1,10]
MEMOTION 2 [123]
English
Reddit, Facebook
2022
10,000
V+T
Neg, Neu, Pos
MSED [140]
English
Getty Image, Flickr
and Twitter
2022
9,190
V+T
Neg, Neu, Pos and Emotions
Twitter-2015 [79]
English
Twitter
2019
5,338
V+T
Neg, Neu, Pos
Twitter-2017 [79]
English
Twitter
2019
5,972
V+T
Neg, Neu, Pos
MMSD [120]
English
Twitter
2019
24,635
V+T
Neg, Pos
MMSD2.0 [205]
English
Twitter
2023
24,635
V+T
Neg, Pos
MUStARD [124]
English
Movies, TVs
2021
690
A+V+T
Neg, Pos
3.2
Image-Text Sentiment Analysis
3.2.1
Coarse-grained Level
Image-text coarse-grained sentiment analysis primarily encompasses two tasks: emotion classification
and sentiment classification. Given an image-text pair, the emotion classification task aims to identify
emotional labels such as happiness, sadness, surprise, etc, inspired by the text-based emotion classification
task. Sentiment classification aims to identify the sentiment label, which usually includes three categories
(positive, neutral, negative). Problem formalization as follows:
Given a set of multimodal posts from social media, P = {(T1, V1), ..., (TN, VN)}, where Ti is the text
modality and Vi is the corresponding visual information, N represents the number of posts. We need to

--- Page 7 ---

Author Hao YANG, et al.
7
learn the model f : P −→L to classify each post (Ti, Vi) into the predefined categories Li. For polarity clas-
sification, Li ∈{Positive, Neutral, Negative}; for emotion classification, Li ∈{Angry, Bored, Calm,
Fear, Happy, Love, Sad}.
The earliest image-text sentiment classification models were feature-based. In [130], the authors used
SentiBank to extract 1200 adjective-noun pairs (ANPs) as visual semantic features and employed Sen-
tiStrength [129] to compute text sentiment features for handling multimodal tweet sentiment analysis.
In [131], the authors presented a cross-media bag-of-words model to represent the text and image of a
Weibo tweet as a unified bag-of-words representation. Then some neural network models showed better
performance. In [132, 133], the authors used convolutional neural network (CNN) models to get the
representation of text and image. In [134], the authors believed that more detailed semantic information
in the image is important and constructed HSAN, a hierarchical semantic attentional network based on
image caption for coarse-level multimodal sentiment analysis. MultiSentiNet [135] focused on the corre-
lation between images and text, aggregating the representation of informative words with visual semantic
features, objects, and scenes. Considering the mutual influence between image and text, Co-Mem [136] is
designed to iteratively model the interactions between visual contents and textual words for multimodal
sentiment analysis.
In [31], the authors found that images play a supporting role to text in many sentiment detection cases,
and proposed VistaNet which instead of using visual information as features only rely on visual informa-
tion as alignment for pointing out the important sentences of a document using attention. With respect
to each image representation f v
j , the goal is to learn the attention weights βj,i for text representations
f t
j:
pj = tanh(Wpf v
j + bp),
(5)
qi = tanh(Wqf t
i + bq),
(6)
vj,i = V T (pj ⊙qi + qi),
(7)
βj,i =
exp(vj,i)
P
i exp(vj,i)
(8)
where Wp, Wq, bp, bq are learnable parameters, firstly, projecting both image representation and text
representation onto an attention space followed by a non-linear activation function tanh. Then, let the
image projection pj interact with the sentence projection qi in two ways: element-wise multiplication and
summation.
CLMLF [138] applies contrastive learning and data augmentation to align and fuse the token-level
features of text and image. In addition to focusing on sentiment, emotions are equally important. In [127],
the authors built an image-text emotion dataset, named TumEmo, and further proposed MVAN for
multi-modal emotion analysis. In [137], the authors observed that multimodal emotion expressions have
specific global features and introduced a graph neural network, proposing an emotion-aware multichannel
graph neural network method called MGNNS. MULSER [139] is also a graph-based fusion method that
not only investigates the semantic relationship among objects and words respectively, but also explores
the semantic relationship between regional objects and global concepts, which has also yielded effective
results.
Traditional multimodal sentiment analysis methods often rely on superficial information, lacking the
depth provided by contextual world knowledge. This limits their ability to accurately interpret the sen-
timent conveyed in multimodal content (images and text). WisdoM [141] leverage the contextual world
knowledge induced from the LMMs for enhanced multimodal sentiment analysis. As shown in Figure 2,
the process involves three stages: 1) Prompt Templates Generation: Using ChatGPT to create templates
that help LMMs understand the context better. 2) Context Generation: Feeding these templates into
LMMs along with the sentence and image to generate rich contextual information. 3) Contextual Fusion:
Combining this contextual information with the original sentiment predictions to enhance accuracy, par-
ticularly for difficult samples. A training-free module called Contextual Fusion is introduced to minimize
noise in the contextual data, ensuring that only relevant information is considered during sentiment analy-
sis. WisdoM significantly outperforms existing state-of-the-art methods in MSED dataset, demonstrating
its effectiveness in integrating contextual knowledge for improved sentiment classification. In addition,
inspired by the success of textual prompt-based fine-tuning approaches in few-shot scenario, the au-
thors [168] introduce a multi-modal prompt-based fine-tuning approach UP-MPF and the authors [169]
propose a prompt-based vision-aware language modeling (PVLM) for multimodal sentiment analysis.

--- Page 8 ---

Author Hao YANG, et al.
8
Provide prompts or templates 
that can make you provide more 
information about image and 
corresponding sentence.
1. Describe the image, and provide any accompanying text. You can analyze ...
2. Give you an image and text, you can provide historical context, important … 
3. Share an image and related text, and you can provide an interpretation of …
Stage 1: Prompt Templates Generation
Stage 2: Context Generation
The two images highlights the devastating impact of the war on the city and 
its residents. Aleppo, once a thriving and historic city, has been severely 
affected by the ongoing Syrian Civil War. The conflict has led to the 
destruction of infrastructure, displacement of residents, and loss of life… 
LVLM
Give you an image and sentence, you
can
provide
historical
context,
important... Sentence: “ R T
@
AHedengren : # Aleppo before and
after.”
Stage 3: Contextual Fusion
Sentence: “RT @ AHedengren : # 
Aleppo before and after.”
Sentence: “RT @ AHedengren : # 
Aleppo before and after.” Context:
“The two images highlights the
devastating impact of the war …”
MSA
model
Negative: 0.4
Neutral: 0.5
Positive: 0.1
Negative: 0.7
Neutral: 0.2
Positive: 0.1
Negative: 0.5
Neutral: 0.4
Positive: 0.1
Prompt templates
Context
MSA
model
Contextual 
Fusion
Figure 2
Overview of WisdoM framework [171] architecture for coarse-grained image-text sentimen.
We summarize the commonly used datasets for coarse-grained image-text sentiment and emotion anal-
ysis, including TumEom, MVSA, MEMOTION 2, and MSED:
TumEmo is a multimodal weak-supervision emotion dataset containing a large amount of image-text
data crawled from Tumblr. The dataset contains 195,265 image-text pairs with 7 emotion labels: Angry,
Bored, Calm, Fearful, Happy, Loving, Sad.
MVSA dataset is collected from image-text pairs on the Twitter platform and is manually annotated
with three sentiment labels: positive, neutral, and negative. The MVSA dataset consists of two parts:
MVSA-Single, where each sample is annotated by a single annotator, comprising 4,869 image-text pairs,
and MVSA-Multiple, where each sample is annotated by three annotators with three emotion labels,
totaling 19,598 image-text pairs. The MVSA corpus is another example of coarse-grained multimodal
sentiment classification dataset.
MEMOTION 2 is a dataset focused on classifying emotions and their intensities into discrete labels.
It includes 10,000 memes collected from various social media sites. These memes are typically humorous
and aim to evoke a response. Overall Sentiment (positive, neutral, negative), Emotion (humour, sarcasm,
offence, motivation), and Scale of Emotion are all annotated for each meme (0–4 levels).
MSED comprises 9,190 pairs of text and images sourced from diverse social media platforms, including
but not limited to Twitter, Getty Images, and Flickr. Each piece of multi-modal sample is manually
annotated with desire category, sentiment category (i.e., positive, neutral and negative) and emotion
category (happiness, sad, neutral, disgust, anger and fear).
3.2.2
Fine-grained Level
Image-text fine-grained sentiment analysis focuses on analyzing sentiment elements that are finer than
sentence-level, such as aspect term (a) and sentiment polarity (p) , or their combinations. It has received
widespread attention in recent years and mainly includes three subtasks: Multimodal Aspect Term
Extraction (MATE), Multimodal Aspect-based Sentiment Classification (MASC) and Joint Multimodal
Aspect-Sentiment Analysis (JMASA). We illustrate the definitions of all the sub-tasks with a specific
example in Figure 3.
Multimodal Aspect Term Extraction.
As shown in Figure 3, MATE aims to extract all the
aspect terms mentioned in a sentence. Given the multimodal input includes a n-words sentence S =
(w1, w2, . . . , wn) and a corresponding image I, the goal of MATE is to predict the label of each word in

--- Page 9 ---

Author Hao YANG, et al.
9
Sentence: Some of that [Dodger]ǅ1
ǔ1: ǔ표푠푖ǘ푖怀 baseball ☀︎⚾︎ @[alyssajacinto]ǅ2
ǔ2: ǔ표푠푖ǘ푖怀.
                                   Image:
Sub-tasks
Input
Output
Multimodal Aspect Term
Extraction (MATE)
S+I
ǅ1, ǅ2
Multimodal Aspect-Oriented
Sentiment Classification (MASC) 
S+I+ǅ1
ǔ1
S+I+ǅ2
ǔ2
Joint Multimodal Aspect-Sentiment
Analysis (JMASA)
S+I
(ǅ1, ǔ1), (ǅ2, ǔ2)
Figure 3
Image-text fine-grained sentiment analysis tasks.
scheme yi ∈{B, I, O}, where B indicates the beginning, I indicates the inside and the end of an aspect
term, O means non-target words.
Inspired by text-based aspect term extraction methods [142–144], MATE approaches usually view this
task as a sequence labeling problem. How to utilize visual information to improve the accuracy of aspect
term recognition is the key to this task. Some studies [145, 149] focused on named entity recognition
suggest using ResNet encoding to leverage whole image information to enhance the representation of
each word. Various neural network-based methods have been developed, including those using recurrent
neural networks [145, 146], Transformers [96, 147, 148], and graph neural networks [150]. Conditional
Random Fields (CRF) are widely used in sequence labeling tasks because CRF considers the correlations
between labels in neighborhoods. For example, an adjective has a greater probability of being followed
by a noun than a verb in POS tagging task. Using Y = (y1, y2, . . . , yn) represents a generic sequence of
labels for input S. Given sequence S, all the possible label sequences Y can be calculated by the following
equation:
p(Y |S) =
Qn
i=1 Ω(yi−1, yi, X)
P
y′∈Y
Qn
i=1 Ω(y
′
i−1, y
′
i, X),
(9)
where Ω(yi−1, yi, X) and Ω(y
′
i−1, y
′
i, X) are potential functions.
However, these methods are relatively independent and often focus more on entity information while
neglecting the emotional information of the target. Therefore, as research progresses, more scholars in
multimodal scenarios are not only extracting aspect terms but also jointly performing corresponding
sentiment classification.
For example, inspired by the fuzzy span universal information extraction (FSUIE) framework [152]
which focuses on the limited span length features in information extraction and proposes fuzzy span
loss and fuzzy span attention, DQPSA [151] addresses MATE and MASC under a unified framework as
span recognition, dispensing with the complex sequence generation structure. As shown in Figure 5, To
capture the semantical relevance of start and end boundaries within a span, DQPSA introduce the idea
of Energy Based Model [216] to give better span scores and propose the Energy based Pairwise Expert
that predicts span based on pairwise stability.
Multimodal Aspect-based Sentiment Classification.
As shown in Figure 3, MASC aims to
identify the sentiment polarity of a given aspect term in a sentence. Problem formalization as follows:
Given a set of multimodal samples S = {X1, X2, ..., X|S|}, where |S| is the number of samples. And for

--- Page 10 ---

Author Hao YANG, et al.
10
Figure 4
Illustration of exact boundary and fuzzy boundary.
each sample, we are given an image V ∈R3×H×W where 3, H and W represent the number of channels,
height and width of the image, and an N-word textual content T = (w1, w2, ..., wN) which contains an
M-word sub-sequence as target aspect A = (w1, w2, .., wM). The goal of MASC is to learn a sentiment
classifier to predict a sentiment label y ∈{Positive, Negative, Neutral} for each sample X = (V, T, A).
Different from text-based aspect sentiment classification [153–155], it is challenging to effectively dis-
cover visual sentiment information and fuse it with textual sentiment information. In [77], the authors
constructed the Multi-ZOL dataset for the MASC task. This dataset collects and organizes comments
about smartphones from the ZOL.com business portal website. At the same time, they proposed a multi-
modal interactive memory network(MIMN) based on an attention mechanism to capture the information
interaction between different modalities. In addition, other researchers [78, 79] have proposed models like
the LSTM-based ESAFN model and the Transformer-based TomBERT model for the MASC task, en-
hancing the interaction of inter-modal and intra-modal sentiment information is the core of these models.
The TomBERT model treat the hidden states of the target aspect A as queries, and the regional image
features HV as keys and values, such that the target is leveraged to guide the model to align it with the
appropriate regions.
ATTi(A, HV ) = softmax([WQiA]T [WKiHV ]
p
d//m
)[WViHV ]T ,
(10)
where WQi, WKi, WVi ∈Rd/m×d are parameters, m represent the attention head number, d is the input
embeddings dimension.
Compared with other multimodal tasks such as image and text retrieval, the sentiment annotation
used in the MASC task lack strong supervision signals for cross-modal alignment. This issue makes it
difficult for MASC models to learn cross-modal interactions and causes models to learn the bias brought
by the image. In [32], the authors propose a new method to utilize visual modalities, the image caption
generation module in their model undertakes the task of cross-modal alignment. They convert images
into text descriptions based on the idea of cross-modal translation.
C = Caption Transformer(V ),
(11)
where C and Captiontransformer denote the output image captions and the transformer-based image
caption generator, respectively. In sentence-pair classification mode, input to pre-trained language model
takes the sentence-pair form
[CLS]wT
1 , wT
2 ...wT
T.len[SEP]wC
1 , wC
2 ...wC
C.len[PAD]...[PAD],
(12)
where wT
i are the tokens of the input text, and wC
i
are the tokens of the image caption. In [98], the
authors continued with the idea of modal transformation and employed facial emotions as a supervised
signal for learning visual emotions.
As large language models evolve, LLMs and LMMs have adapted to various tasks [156–159], but their
use in the MASC task is still in its initial stages. In [160], the authors attempt to apply the instruction

--- Page 11 ---

Author Hao YANG, et al.
11
Figure 5
Overview of DQPSA model [151] architecture.
tuning paradigm to the MASC task and utilize the capabilities of LMMs to mitigate the limitations of text
and image modality fusion. As shown in Figure 6, to address the potential irrelevance between aspects
and images, a plug-and-play selector is proposed to autonomously choose the most suitable instruction
from the instruction pool, thereby reducing the impact of irrelevant image noise on the final sentiment
classification outcome.
Joint Multimodal Aspect-Sentiment Analysis. As shown in Figure 3, JMASA aims to extract
all aspect terms and their corresponding sentiment polarities simultaneously. Problem formalization as
follows: Given a collection of multimodal sentence-image pairs, denoted as M.
Each pair mi ∈M
comprises a sentence Si = (w1, w2, . . . , wn) and a corresponding image vi. The objective of JMASA is to
predict the corresponding aspect-sentiment pair y = (y1, y2, . . . , yn) for each sentence-image pair. Here,
yi ∈{B-POS, I-POS, B-NEG, I-NEG, B-NEU, I-NEU} ∪O. In this case, B refers to the initial token
of the aspect term, I indicates tokens within the specific aspect term and O indicates words “outside” the
specific aspect. Moreover, POS, NEU, and NEG are abbreviations for positive, neutral, and negative
sentiments associated with the specific aspect.
As a pioneer, in [161], the authors proposed joint multimodal aspect-sentiment analysis, which jointly
performs multimodal aspect term extraction and multimodal aspect sentiment classification. Since it is
a joint task with aspect terms extraction and aspect sentiment classification, the authors calculate two
different sets of loss simultaneously as follows:
L = −
k
X
i=1
ys
i log pstr
i
−
k
X
i=1
ye
i log pend
i
−
m
X
t=1
ϵ
X
i=1
yp
ti log pp
ti
(13)
where ys, ye, yp are one-hot labels indicating golden start, end positions, true sentiment polarity sepa-
rately, and a, m are the number of sentence tokens, aspects respectively.
Benefiting from the advancements in visual-language pre-train models, in [80], the authors have de-
signed multimodal sentiment pre-training tasks and develop a unified multimodal encoder-decoder archi-
tecture pre-training model for JMASA. In [162], the authors utilize a Cross-Modal Multi-Task Transformer

--- Page 12 ---

Author Hao YANG, et al.
12
Figure 6
Overview of A2II model [160] architecture for MASC task.
(CMMT) to derive sentiment-aware features for each modality and dynamically control the impact of
visual information on textual content during inter-modal interaction. However, the innate semantic gap
between visual and language modalities remains a huge challenge for the use of these methods, in [163],
the authors believe that the aesthetic attributes of images potentially convey a more profound emotional
expression than basic image features and propesd Atlantis. Some scholars [164] have also noticed the
impact of image-text pair quality, finding that many studies have overestimated the importance of images
due to the presence of many noise images unrelated to text in the datasets. Drawing from the concept
of curriculum learning, they proposed a Multi-grained Multi-curriculum Denoising Framework (M2DF),
which achieves denoising by adjusting the order of the training data. AOM [165] is designed with an
aspect-aware attention module that simultaneously selects text tokens and image blocks semantically
related to the aspect to detect semantic and emotional information related to the aspect, thereby re-
ducing noise introduced during the cross-modal alignment process. RNG [166] to simultaneously reduce
multi-level modality noise and multigrained semantic gap, design three constraints: (i) Global Relevance
Constraint (GR-Con) based on text-image similarity for instance-level noise reduction, (ii) Information
Bottleneck Constraint (IB-Con) based on the Information Bottleneck (IB) principle for feature-level noise
reduction, and (iii) Semantic Consistency Constraint (SC-Con) based on mutual information maximiza-
tion in a contrastive learning way for multi-grained semantic gap reduction. To bridge the semantic gap
between modal spaces and address the interference of irrelevant visual objects at different scales, in [167],
the authors proposed a Multi-level Text-Visual Alignment and Fusion Network (MTVAF).
With the help of LLMs, the JMASA task has also seen further development in recent years. In [170], the
authors found that compared to converting MASC into a masked language modeling (MLM) task based
on limited sentiment categories with PVLM [169] and UP-MPF [168], MLM is not suitable for JMASA
and MATE tasks. They proposed a novel Generative Multimodal Prompt (GMP) model. In [171], the
authors explored the potential of using the representative large language model ChatGPT for In-Context
Learning (ICL) on the JMASA task. As shown in Figure 7, they developed a versatile ICL framework,
incorporating zero-shot learning task instructions and expanded it to few-shot learning by adding some
demonstration samples to the prompts. Additionally, to enhance the ICL framework’s performance in few-
shot learning scenarios, they further developed an entity-aware contrastive learning model to effectively
retrieve demonstration samples similar to each test sample.
We summarize the commonly used datasets for fine-grained image-text sentiment analysis, including
Multi-ZOL, Twitter-15 and Twitter-17:
Multi-ZOL collects and organizes comments about smartphones from the ZOL.com business portal
website. Multi-ZOL dataset includes sentiment ratings for six aspects, such as price-performance ratio,
performance configuration, battery life, appearance and feeling, photographing effect, and screen. For
each aspect, the comment has an integer sentiment score from 1 to 10, which is used as the sentiment
label.
Twitter-2015 and Twitter-2017 datasets are commonly used datasets for fine-grained image-text
sentiment analysis tasks. These datasets are collected from English tweets on the social media platform
Twitter and are in the form of image-text pairs. The datasets provide annotations for aspects mentioned in

--- Page 13 ---

Author Hao YANG, et al.
13
Figure 7
Overview of versatile ICL framework [171] architecture for JMASA task.
the text. Sentiment labels are categorized into three classes: positive, neutral and negative. Specifically,
the Twitter-2015 dataset contains 5,338 tweets with images, while the Twitter-2017 dataset contains
5,972 tweets with images.
3.3
Audio-Image-Text Sentiment Analysis
Audio-image-text (video) sentiment analysis differs from image-text sentiment analysis in two main as-
pects: 1) Different data emphasis. Existing text-image sentiment datasets are drawn from social media
and e-commerce platforms, covering a wide range of content. In contrast, visual information in video
sentiment datasets often focuses on the facial expressions and body movements of speakers. 2) Videos can
be considered as temporal sequences of text-image pairs, necessitating considerations of intra-modal emo-
tional factors in audio sequences and video frame sequences, as well as alignment relationships between
text, video frames, and audio over time. Video-based sentiment analysis primarily includes sentiment clas-
sification and emotion classification tasks. Sentiment classification involves three, five, or seven-category
classification tasks, while emotion classification comprises multi-label emotion recognition (where each
sample corresponds to multiple emotion labels) and single-label emotion recognition. Common emotion
labels include happiness, surprise, and anger. Problem formalization as follows:
In audio-image-text sentiment analysis tasks, the input is utterance consisting of three modalities:
textual, acoustic and visual modality, where m ∈{t, a, v} . The sequences of these three modalities
are represented as triplet (T, A, V ), including T ∈RNt×dt, A ∈RNa×da and V ∈RNv×dv where Nm
denotes the sequence length of corresponding modality and dm denotes the dimensionality. The goal of
audio-image-text sentiment analysis tasks is to learn a mapping f(T, A, V ) to infer the sentiment score
ˆy ∈R.
As the audio-image-text sentiment analysis methods proposed by scholars in recent years generally
cater to both sentiment classification and emotion classification tasks, this paper will review the exist-
ing multimodal sentiment analysis methods around two core themes: cross-modal sentiment semantic
alignment and multimodal sentiment semantic fusion.
3.3.1
Cross-modal Sentiment Semantic Alignment
Cross-modal sentiment semantic alignment methods aim to explore the associations between emotional
information across different modalities, analyze the corresponding relationships between them (align-
ment relationship modeling), and reduce the semantic distance between representations across modalities

--- Page 14 ---

Author Hao YANG, et al.
14
(semantic representation alignment). Cross-modal sentiment semantic alignment methods can help over-
come the challenges brought by the semantic gap of heterogeneous modalities and are a prerequisite for
multimodal sentiment semantic fusion methods. Specifically, by exploring the alignment relationships
between different modal sentient semantic representations, these methods can help the fusion model ig-
nore irrelevant information and focus on modeling effective information. By bringing emotional semantic
representations closer in the representation space, these methods can reduce modal differences between
representations, lower the difficulty of fusion, and increase fusion efficiency. This paper surveys existing
cross-modal sentiment semantic alignment methods and categorizes them into three types based on differ-
ent alignment strategies and purposes: attention-based alignment, contrastive learning-based alignment,
and cross-domain transfer learning-based alignment.
Attention-based alignment. The attention mechanism has been proven to be an effective method
for cross-modal semantic alignment in the field of multimodal learning [179]. Not only can the attention
mechanism learn to adapt the alignment relationships for specific tasks through the optimization of task-
specific objective functions, but it can also provide a degree of interpretability by outputting attention
weights. For example, in the field of image captioning, the attention mechanism focuses on relevant areas
when generating text words [180], demonstrating the alignment relationship between words and image
regions. Inspired by related research in the multimodal learning field, in [43], the authors proposed using
a cross-modal attention mechanism to learn the alignment relationships between pairs of modalities and
developed a transformer-based multimodal sentiment analysis model named MulT. The core of the MulT
model lies in modeling cross-modal alignment relationships by inserting cross-modal attention layers into
the transformer module, allowing dynamic alignment and fusion of fine-grained sentiment information
from various modalities. First, use α and β to represent two different modalities, define the Querys
as Qα = XαWQα, Keys as Kβ = XβWKβ, and Values as Vβ = XβWVβ, where WQα ∈Rdα×dk, WKβ ∈
Rdβ×dk and WVβ ∈Rdβ×dv are weights. The latent adaptation from β to α is presented as the crossmodal
attention Yα := CMβ→α(Xα, XB) ∈RTα×dv:
Yα = CMβ→α(Xα, Xβ) = softmax
 
QαK⊤
β
√dk
!
Vβ = softmax
 
XαWQαW ⊤
KβX⊤
β
√dk
!
XβWVβ.
(14)
Note that Yα has the same length as Qα, but is meanwhile represented in the feature space of Vβ.
Specifically, the scaled (by √dk) softmax computes a score matrix softmax (·) ∈RTα×Tβ, whose (i, j)-th
entry measures the attention given by the i-th time step of modality α to the j-th time step of modality
β. Hence, the i-th time step of Yα is a weighted summary of Vβ, with the weight determined by i-th row
in softmax(·).
Building on the cross-modal attention mechanism designed in MulT, in [181], the authors introduced
the cubic attention mechanism, which generates a three-dimensional attention tensor through parameter
computations, representing the alignment information among the three modal representations.
Contrastive learning-based alignment. Contrastive learning achieves cross-modal representation
alignment by bringing the representations of positive examples closer together and pushing the represen-
tations of negative examples farther apart. A classic model in the field of multimodal learning, CLIP [116],
uses contrastive learning to align the semantic representations of text and image modalities, significantly
enhancing the quality of image representations and achieving excellent results in tasks such as zero-shot
image classification. Inspired by this, the field of audio-image-text sentiment analysis has adopted con-
trastive learning methods for sentiment semantic representation alignment. In [182], the authors proposed
achieving cross-modal emotional semantic alignment by bringing closer the representations of different
modalities within the same sample. In [183], the authors suggested using the text-audio and text-image
modal information of input samples to predict the corresponding image and audio representations of the
samples, then aligning the predicted representations with the actual ones and distancing representations
from different samples, thereby aligning the semantic representations of different modalities within the
same sample. The proposed model contains two key modules, the uni-modal coding drive the model
to focus on informative features which then implicitly filter out inherent noise and produces robust and
effective uni-modal representation for acoustic and visual modalities.
Given a batch set Funi = {F 0
u, F 1
u, ..., F n−1
u
}, noted that there is a single positive key F †
u (as k+) that
each encoded query F i
u (as q, i ∈[1, n]) matches, while the other representations F j
u (j ∈[0, n] and
j ̸= i) in the same batch are considered as negative key samples k−. With the similarity measured by

--- Page 15 ---

Author Hao YANG, et al.
15
dot product, the uni-modal instance contrastive loss Luni in:
Lu
uni ≜−log
exp(q · k+/τ)
Pn
i=1 exp(q · qi/τ) = −E
Funi

log
exp(Fu · F †
u/τ)
Pn
i=1 exp(Fu · F iu/τ)

(15)
where τ is a temperature hyper-parameter that controls the probability distribution over distinct in-
stances. Due to u ∈{a, v}, the final uni-modal instance contrastive loss Luni = La
uni + Lv
uni.
The cross-modal prediction captures commonalities among different modalities and outputs predictive
representation full of interaction dynamics. Each query q has a corresponding key as k+ while the other
representations in the same batch are seen as k−. Similar with uni-modal instance contrastive loss Luni,
the cross-modal instance contrastive loss Lcross is presented as:
Lcross ≜−
E
Fcross

log
exp(Fc · F +
c /τ)
Pn
i=1 exp(Fc · F ic/τ)

(16)
where Fc\F +
c
∈{Pu, Gu}, Pu represent the prediction while Gu represent the target, u ∈{a, v} and
Fcross = {F 1
c , ..., F n
c }.
Cross-domain transfer learning-based alignment. The field of cross-domain transfer learning
primarily studies how to align the sample spaces of target domains with those of source domains so that
classifiers trained in the source domains can be directly reused in the target domains. The objectives
of this field align broadly with those of cross-modal sentiment representation alignment, hence some
studies have explored using cross-domain transfer learning methods for sentiment semantic representation
alignment.
In [184], considering the rich information content of textual representations, the authors
proposed using Deep Canonical Correlation Analysis (DCCA) to align audio and visual representations
with textual representations, thereby enhancing the audio and visual representations. In [185], the authors
explored using a metric-based domain transfer method, utilizing Central Moment Discrepancy (CMD)
to design a loss function that aligns the representations of the three modalities within the same sample.
The overall learning of the model is performed by minimizing:
L = Ltask + α Lsim + β Ldiff + γ Lrecon
(17)
Here, α, β, γ are the interaction weights that determine the contribution of each regularization component
to the overall loss L. Minimizing the similarity loss Lsim reduces the discrepancy between the shared
representations of each modality. This helps the common cross-modal features to be aligned together in
the shared subspace. Difference Loss Ldiff is to ensure that the modality-invariant and -specific represen-
tations capture different aspects of the input. As the difference loss is enforced, there remains a risk of
learning trivial representations by the modality-specific encoders. To avoid this situation, the authors add
a reconstruction loss Lrecon that ensures the hidden representations to capture details of their respective
modality. The task-specific loss Ltask estimates the quality of prediction during training.
In [186] the authors have employed adversarial learning methods to align sentiment semantic represen-
tations across different modalities.
3.3.2
Multimodal Sentiment Semantic Fusion
Multimodal sentiment semantic fusion aims to efficiently aggregate sentiment information from different
modalities to achieve comprehensive and accurate sentiment understanding.
The challenge of fusion
lies in how to fully capture the complex interactions among multimodal sentiment semantic information,
thereby facilitating sentiment reasoning and prediction. This paper surveys existing multimodal sentiment
semantic fusion methods and categorizes them into three types: tensor-based fusion, fine-grained temporal
interaction modeling fusion, and pre-trained model-based fusion.
Tensor-based fusion. In the early stages of audio-image-text sentiment analysis research, consid-
ering the small scale of datasets and limited computational resources, researchers represented the raw
inputs of each modality as a single emotional semantic representation before proceeding to multimodal
emotional semantic representation fusion. The simplest fusion strategy was to directly concatenate the
emotional semantic representations of different modalities, but this method did not explicitly model the
higher-order interactions between emotional information from different modalities. To address this issue,
in [33], the authors proposed using the outer product of vectors to fuse different modal representations,

--- Page 16 ---

Author Hao YANG, et al.
16
thereby modeling interactions among unimodal, bimodal, and trimodal emotional semantic representa-
tions simultaneously. However, this method, due to the complexity of the outer product operation being
tied to the product of input vector dimensions, resulted in high computational costs and slow efficiency.
Subsequent work has made efficiency improvements.
In [187], the authors proposed the LMF fusion
method, which accelerates the fusion process of multimodal emotional representations through low-rank
decomposition.
5>
(S)
⨂
+
+ ⋯
5#
(S)
5> 
(T)
⨂
5#
(T)
V
⨂
E
E
!>
!#
g
E
=
ℎ
Figure 8
Decomposing weight tensor into low-rank factors [187].
In [188], the authors introduced a three-stage multimodal emotional representation fusion strategy con-
sisting of representation slice grouping, intra-group representation slice fusion, and global representation
fusion. Representation slice grouping involves splitting the representations of each modality into the same
fixed number of small groups, numbering them, and then locally fusing representation slices of the same
number from different modalities together. This approach reduces the dimensions of representations to
be fused later, thereby enhancing fusion efficiency. Intra-group representation slice fusion uses the outer
product method to fuse the representation slices of the three modalities within the group, which, due
to the smaller feature dimensions, significantly speeds up the fusion process. Finally, Long Short-Term
Memory (LSTM) networks are used to perform global representation fusion of the different groups after
fusion. This method reduces the computational complexity of the tensor outer product fusion method to
some extent through block processing.
Fine-grained temporal interaction modeling fusion.
This type of fusion method focuses on
capturing more localized, fine-grained interactions of multimodal information. These methods first ob-
tain fine-grained representations corresponding to each time step of each modality, and then perform
multimodal sentiment semantic fusion based on these representations to capture the interactions between
cross-modal and cross-temporal sentiment information. In [34], the RAVEN model is a typical method in
this series of research. The authors found that the same words can convey different emotional messages
when accompanied by different tones or expressions. Driven by this motivation, they designed a network
that improves the word representations by dynamically integrating the fine-grained representations of
visual and auditory modalities into each word vector through a cross-modal gating mechanism, thereby
achieving the goal of infusing non-verbal emotional information into word representations. For a word
L(i), the nonverbal shift vector h(i)
m is calculated as follows:
h(i)
m = w(i)
v
· (Wvh(i)
v ) + w(i)
a · (Wah(i)
a ) + b(i)
h
(18)
where Wv and Wa are weight matrices for the visual and acoustic embedding and b(i)
h is the bias vector.
In[189], considering that audio and visual inputs might contain noise at certain time steps, like back-
ground noise in speech, the authors proposed a reinforcement learning-based gating unit to control the
information fusion between fine-grained representations of different modalities. The gating mechanism al-
lows for dynamic sentiment representation fusion by controlling whether the representation of the current
word incorporates information from a particular modality. Unlike the previous two works, which focus
on capturing interactions of multimodal fine-grained sentiment representations associated with individual
words, in [190], the authors model the feature interactions between multimodal fine-grained sentiment
representations of multiple consecutive words within a window and use a memory neural network to
model global information.
Pre-trained model-based fusion. Pre-trained language models have demonstrated strong language
understanding capabilities, and researchers believe they also hold great potential for multimodal language

--- Page 17 ---

Author Hao YANG, et al.
17
understanding. To explore the capabilities of pre-trained language models in the field of multimodal
sentiment analysis, in [191] the authors, inspired by the RAVEN method, designed a gating mechanism
for pre-trained language models.
The aim is to inject multimodal information into the intermediate
layer word representations of the pre-trained language models to fully leverage their strong language
modeling capabilities for efficient multimodal emotional understanding. In [192], the authors proposed a
cross-modal efficient attention mechanism that uses the output representations of pre-trained language
models to compress the input sequences of visual and audio features, thereby enhancing the model’s
computational efficiency.
Figure 9
Overview of the VLP2MSA [204] architecture(a) and the Inter-frame Hybrid Transformer module(b).
The model
receives the original text and video frames as input and consists of a text encoder, a video encoder, a prompt module, a video-text
contrastive, and a multimodal integration encoder. we propose an adapted and extended video encoder and a new fusion scheme
that prompts and aligns before interacting to reduce the influence of modality heterogeneity on the fusion results.
To effectively extend LLMs and LMMs to multimodal sentiment analysis tasks and address two pressing
challenges in the field: (1) the low contribution rate of the visual modality and (2) the design of an
effective multimodal fusion architecture, scholars [204] have proposed an inter-frame hybrid transformer.
As shown in Figure 9, this transformer extracts spatiotemporal features from sparsely sampled video
frames, focusing not only on facial expressions but also capturing body movement information.
3.3.3
Audio-image-text Sentiment Analysis Datasets
We summarize the commonly used datasets for audio-image-text image-text sentiment analysis, including
ICT-MMMO, IEMOCAP, CMU-MOSI, CMU-MOSEI, MELD, CH-SIMS, CH-SIMS 2, M3ED, MER2023,
EMER, MER2024, CMU-MOSEAS and UR-FUNNY.
ICT-MMMO dataset is collected from the YouTube website and defines seven sentiment labels based
on sentiment polarity and intensity: positive (strong), positive, positive (weak), neutral, negative (weak),
negative, and negative (strong). In [193], the authors first addressed the task of tri-modal sentiment
analysis and demonstrated that it is a feasible task that can benefit from the combined use of image,
audio, and text modalities. This dataset forms the basis of their research.
IEMOCAP dataset is a multimodal video dialogue dataset collected by the SAIL lab at the University
of Southern California. It contains about 12 hours of multimodal data, including video, audio, facial
motion capture, and transcribed text. The dataset was collected through dialogues by 5 professional
male actors and 5 professional female actors in pairs, engaging in either improvised or scripted dialogues,
with a focus on emotional expression. The dataset includes a total of 4,787 improvised dialogues and
5,255 scripted dialogues, with an average of 50 sentences per dialogue and an average duration of 4.5
seconds per sentence. Each sentence in the dialogue segments is annotated with specific emotional labels,
divided into ten categories including anger, happiness, sadness, and neutral.

--- Page 18 ---

Author Hao YANG, et al.
18
CMU-MOSI and CMU-MOSEI are two commonly used datasets in the multimodal sentiment
analysis area. The data is sourced from video blogs (vlogs) on the online sharing platform YouTube.
These datasets primarily focus on coarse-grained multimodal sentiment classification tasks. CMU-MOSI
dataset comprises 2,199 video segments extracted from 93 distinct videos. The video content consists
of English comments posted by individual speakers. There are 41 female and 48 male speakers, mostly
between the ages of 20 and 30, coming from diverse backgrounds (Caucasian, Asian, etc.). The videos
are annotated by five annotators from the Amazon Mechanical Turk platform, and the annotations are
averaged. Annotations cover seven categories of emotional tendencies ranging from -3 to +3. The CMU-
MOSEI dataset is larger than the CMU-MOSI dataset, containing 23,453 video segments from 1,000
different speakers across 250 topics, with a total duration of 65 hours. The dataset includes both emotion
labels and sentiment labels. Emotion labels include happiness, sadness, anger, fear, disgust, and surprise,
while sentiment labels include sentiment binary classification, five classification, and seven classification
annotations.
MELD dataset originates from the classic TV series Friends. It comprises a total of 1,443 dialogues and
13,708 utterances, with an average of 9.5 sentences per dialogue and an average duration of 3.6 seconds
per sentence. Each sentence in the dialogue segments is annotated with one of seven emotional labels,
including anger, disgust, sadness, happiness, neutral, surprise, and fear. Additionally, each sentence is
also assigned a sentiment label, categorized as positive, negative, or neutral.
CH-SIMS dataset is a Chinese multimodal sentiment classification dataset with the unique feature of
having both unimodal and multimodal sentiment labels. It consists of 60 original videos collected from
movie clips, TV series, and various performance shows. These videos were clipped at the frame level to
obtain 2,281 video segments. Annotators labeled each video segment for four modalities: text, audio,
silent video, and multimodal. To avoid cross-modal interference during annotation, annotators could
only access information from the current modality. They first performed unimodal labeling, followed by
multimodal labeling. Although the dataset provides labels for each modal, its primary purpose is coarse-
grained multimodal sentiment classification. The CH-SIMS 2 dataset expands the CH-SIMS dataset.
This dataset is larger in scale and more difficult, requiring the model to accurately integrate information
from different modalities to predict the correct answer.
M3ED dataset includes 990 Chinese dialogue videos, totaling 24,449 sentences.
Each sentence is
annotated for six basic emotions (happiness, surprise, sadness, disgust, anger, and fear), as well as
neutral emotion.
MER2023 includes four subsets: Train & Val, MERMULTi, MER-NOISE, and MER-SEMI. In the
last subset, besides the labeled samples, it also contains a large amount of unlabeled data. The dataset
annotates sentiment labels on each sample and focuses on challenges such as multi-label learning, noise
robustness, and semi-supervised learning. Furthermore, they built upon MER2023 to create the EMER
dataset, which not only annotates sentiment labels on each sample but also the reasoning process be-
hind the labels. In MER2024, they expanded the dataset size and included a subset with multi-label
annotations, attempting to describe the emotional states of characters as accurately as possible.
CMU-MOSEAS is the first large-scale multimodal language dataset for Spanish, Portuguese, German
and French, with 40, 000 total labelled sentences. It covers a diverse set topics and speakers, and carries
supervision of 20 labels including sentiment (and subjectivity), emotions, and attributes.
UR-FUNNY dataset is tailored for humor detection tasks, which are closely related to multimodal
sentiment analysis. The dataset was collected from the TED website, selecting 8,257 humorous snippets
from 1,866 videos and their transcribed texts, and additionally, 8,257 non-humorous segments were ran-
domly chosen. The total duration of the dataset is 90.23 hours, encompassing 1,741 different speakers
and 417 distinct topics.
3.4
Multimodal Sarcasm Detection
Sarcasm detection task initially only focused on the textual context [49–51], with scholars noting that
common ironic sentences often juxtapose positive phrases with negative contexts. For example, in the
sentence “I’m so happy I’m late for work”, the presence of the positive phrase “happy” within the
negative context of being late for work makes it easily recognizable as sarcasm.
In most cases, the
sentiment signals conveyed by different modalities in multimodal data are consistent. However, there
are instances of inconsistency, necessitating sentiment disambiguation across modalities.
Multimodal
sentiment disambiguation is essentially a classification task. Multimodal sentiment inconsistency can be

--- Page 19 ---

Author Hao YANG, et al.
19
categorized into two types: complete sentiment conflict, defined as multimodal irony recognition tasks,
and instances where some modalities convey ’neutral’ sentiment polarities while others convey positive or
negative sentiment polarities, which are typical cases of implicit sentiment expression. The multimodal
sarcasm detection task formalization as follows:
Multimodal sarcasm detection aims to identify if a given text associated with an image has sarcastic
meaning. Formally, given a set of multimodal samples D, for each sample d ∈D, it contains a sentence
T with n words {t1, t2, t3, ..., tn} and an associated image I. The goal of model is to learn a multimodal
sarcasm detection classifier to correctly predict the results of unseen samples.
In [53], the authors introduced a multimodal sarcasm detection task for videos and compiled a cor-
responding dataset from television series. Considering the correlation between sentiment classification
and sarcasm detection, in [54], the authors proposed a multi-task framework to simultaneously recognize
sarcasm and classify sentiment polarity. In [57], the authors suggested identifying sarcasm by capturing
incongruent emotional semantic cues across modalities, such as rolling one’s eyes while uttering praise.
Additionally, some researchers have studied sarcasm in text and images; for example, in [55], the authors
introduced a multimodal sarcasm detection task for text and images and designed a multi-level fusion
network to detect sarcasm. In [194], the authors proposed the multimodal sarcasm detection model using
two different computational frameworks based on SVM and CNN that integrate text and visual modalities.
Identifying inconsistencies between modalities is key to multimodal sarcasm detection, and recent models
can be categorized into those based on attention mechanisms and those using Graph Neural Networks
(GNN). For example, in [195], the authors introduced a BERT-based model with a cross-modal attention
mechanism and a text-oriented co-attention mechanism to capture inconsistencies within and between
modalities. In [196], the authors designed a 2D internal attention mechanism based on BERT and ResNet
to extract relationships between words and images. In [197], the authors proposed a Transformer-based
architecture to fuse textual and visual information. In terms of GNN, scholars in [198] built heterogeneous
intramodal and cross-modal graphs (InCrossMG) for each multimodal example to determine the emotional
inconsistencies within specific modalities and between different modalities, and introduced an interactive
graph convolutional network structure to learn the relationships of inconsistencies in a joint and interactive
manner within modal and cross-modal graphs. In [199], the authors constructed heterogeneous graphs
containing fine-grained object information of images for each instance and designed a cross-modal graph
convolutional network.
Figure 10
Different processing procedures for positive(sarcasm) and negative(non-sarcasm) samples in knowledge-based word-
level cross-modal semantic similarity detection module [200].
Additionally, some scholars [200] have proposed incorporating prior knowledge into multimodal sar-
casm detection. They introduced KnowleNet, which utilizes the ConceptNet [201] knowledge base to
integrate prior knowledge, and determines the relevance between images and text through sample-level
and word-level cross-modal semantic similarity detection. They also incorporated contrastive learning
to improve the spatial distribution of sarcastic (positive) and non-sarcastic (negative) samples. In [202],
the authors propose a lightweight multimodal interaction model with knowledge enhancement based on
deep learning. In [203], the authors proposed to introduce emotional knowledge into sarcasm detection
and used sentiment dictionaries to obtain the sentiment vectors by evaluating the words extracted from
various modalities, and then combined them with each modality. In [205], the authors propsed multi-view
CLIP that is capable of leveraging multi-grained cues from multiple perspectives (i.e., text, image, and

--- Page 20 ---

Author Hao YANG, et al.
20
LM Decoder
Layer
Cross Attention
Add
...
Corss-Modality Text Decoder Layer
Image
Cross
Attention
Text
Cross
Attention
Self-
Attention
Corss-Modality Image Decoder Layer
The tweet is sarcastic because
it is a play on the idea of a
train driver being a "tough
job." ...
Given a tweet that consists
of a text {T} and an image
{I}, please give me a
rationale of why the tweet
is ...
sarcastic
The tweet is not sarcastic
because it is a straightforward
observation of the train
driver's job...
non-sarcastic
Divergent Thinking
with LMM
Text
Encoder
Image
Encoder
Query
Selection
Bi-attention
Block
Cross-Modality
Text Decoder
Cross-Modality
Image Decoder
The tweet is
sarcasic.
never seen a # dlr train driver before.
looks like a tough job # london
Coarser-Grained Pre-Training
 Finer-Grained Fine-Tuning
dlr train driver
Textual Target:
Visual Target:
Encoding and Fusion
Figure 11
An overview of CofiPara for multimodal sarcasm target identification [207].
textimage interaction view) for multi-modal sarcasm detection.
In [206], the authors tested the performance of some existing open-source LLMs and LMMs in the
multimodal sarcasm detection task and proposed a generative multi-media sarcasm model consisting of a
designed instruction template and a demonstration retrieval module based on the large language model.
In [207], the authors proposed a versatile framework with a coarse-to-fine paradigm, by augmenting
sarcasm explainability with reasoning and pre-training knowledge.
We summarize the commonly used datasets for multimodal sarcasm detection, including MMSD,
MMSD2.0 and MUStARD.
MMSD dataset is collected from the Twitter platform by searching for tweets in English that contain
special tags indicating sarcasm, such as #sarcasm, #sarcastic, #irony, #ironic, to gather sarcastically
labeled data, and collecting other tweets without these tags as non-sarcastic data. The dataset is an-
notated with a binary classification of “sarcastic/non-sarcastic”. MMSD2.0 fixed the shortcomings of
MMSD, by removing the spurious cues and re-annotating the unreasonable samples.
MUStARD is a multimodal sarcasm detection dataset primarily sourced from English sitcoms, includ-
ing Friends, The Big Bang Theory, The Golden Girls, and non-sarcastic video content from the MELD
dataset. The authors collected a total of 6,365 video clips from these sources and annotated them, in-
cluding 345 sarcastic video clips. To balance the categories, an equal number of 345 non-sarcastic video
clips were selected from the remaining clips, resulting in a dataset comprising 690 video segments. The
annotations include the dialogue, speaker, context dialogue and its speaker, the source TV show, and a
label indicating whether it is sarcastic. The rich annotation allows researchers to conduct a variety of
learning tasks, including studying the impact of context and speakers on the task of sarcasm detection.
3.5
The Usage of LLMs in Multimodal Sentiment Analysis
Figure 12 contrasts the workflow of multimodal sentiment analysis that leverages LLMs with the previous
workflow. In the previous workflow, as shown in Figure 12 (a), multimodal data was obtained from mul-
timodal source like websites, and then being cleaned and selected. Various feature extraction algorithms
are then employed to generate feature vectors for different modalities. Based on various multimodal
fusion models and classification algorithms, sentiment prediction results were obtained and applied to
specific applications. However, under LLMs, to leverage the rich knowledge and robust reasoning capa-
bilities of LLMs and enable text-oriented LLMs to understand multimodal signals, there are primarily
two strategies. One, as shown in Figure 12 (b), is to textualize non-text inputs, allowing the LLMs to
comprehend the textualized multimodal signals, such as converting images into text by image caption
model. The other strategy, as shown in Figure 12 (c), involves using a multimodal encoder to obtain
multimodal features and then learning feature alignment mappings, aligning multimodal signals with text
in the feature space, enabling LLMs to utilize multimodal features for sentiment analysis.
In Table 3 we have summarized some representative multimodal sentiment analysis methods assisted
by LLMs, analyzing the strategies used with LLMs as well as their advantages and disadvantages. After
analysis, we have found that most existing research tends to view LLMs as knowledge sources. Operating

--- Page 21 ---

Author Hao YANG, et al.
21
Table 3
Some text-centric multimodal sentiment analysis methods that have utilized LLMs.
Method
Usage of LLMs
Advantage
Disadvantage
WisdoM [141]
Zero-shot Learning:
1)
Using ChatGPT to pro-
vide prompt templates.
2) Prompting LMMs to
generate
context
using
the
prompt
templates
with image and sentence.
Leverage the contextual
world knowledge induced
from the LMMs for en-
hanced Image-text Senti-
ment Classification.
Due to hallucinations in
LLMs,
the
contextual
knowledge supplemented
by
LLMs
and
LMMs
as
knowledge
sources
may
not
be
accurate.
The adaptive incorpora-
tion of context requires
further exploration.
ChatGPT-
ICL [171]
Zero-shot Learning and
Few-shot Learning: Us-
ing ChatGPT to predict
final sentiment labels.
This work explores the
potential
of
ICL
with
ChatGPT
for
Multi-
modal
Aspect-based
sentiment
analysis,
achieves
competitive
performance while uti-
lizing
a
significantly
smaller sample size.
The
ICL
framework
exhibits
a
relatively
limited
capability
for
aspect term extraction
tasks when compared to
fine-tuned methods.
A2II [160]
Full-Parameter
Tuning:
leverage the ability of
LMMs to alleviate the
limitation of cross-modal
fusion
This
work
explored
an
instruction
tuning
modeling
approach
for
multimodal aspect-based
sentiment
classification
task,
and
achieved
impressive performance.
The visual features ex-
tracted by the Q-Former
structure, which queries
based on aspect, may be
mismatched, leading to
the neglect of some vi-
sual emotional signals.
CofiPara [207]
Zero-shot Learning: Us-
ing potential sarcastic la-
bels as prompts to cul-
tivate
divergent
think-
ing in LMMs, eliciting
the relevant knowledge
in
LMMs
for
judging
irony.
Note the negative im-
pact
of
the
inevitable
noise in LMMs, and use
competitive principles to
align the sarcastic con-
tent generated by LMMs
with their original multi-
modal features to reduce
the noise impact.
View
LMMs as modal convert-
ers, transforming visual
information into text to
help cross-modal align-
ment.
Viewing
LMMs
as
a
knowledge source largely
depends
on
the
capa-
bilities
of
the
LMMs
themselves.
Although
effective measures have
been
taken
to
reduce
the impact of noise from
LMMs, a certain propor-
tion of erroneous judg-
ments are still caused by
LMMs.

--- Page 22 ---

Author Hao YANG, et al.
22
Textual Input
Non-textual Input
Multimodal Source
Textual Feature
Extractor
Non-textual Feature
Extractor
Fusion Model
Textual Features
Non-textual Features
Sentiment
Polarity
Application 1
Application 2
...
Textual Input
Non-textual Input
Multimodal Source
 Convert to Text
LLMs
Sentiment
Polarity
Application 1
Application 2
...
Textual Input
Textual Input
Non-textual Input
Multimodal Source
LLMs
Sentiment
Polarity
Application 1
Application 2
...
Multimodal Encoder
Non-textual Features
(a)
(b)
(c)
Features Alignment
Non-textual Features
Figure 12
Conceptual illustration of multimodal sentiment analysis using LLMs: (a) multimodal sentiment analysis method
without using LLMs, (b) modal transformation-based method, and (c) multimodal encoder-based method.
under a parameter-fixd paradigm, these studies leverage zero-shot and few-shot strategies to endow
smaller models with additional worldly knowledge in multimodal sentiment analysis tasks, resulting in
performance improvements. Here are further advantages and methods of utilizing LLMs in text-centric
multimodal sentiment analysis:
• LLMs can supplement richer knowledge, such as knowledge of different languages and cultures, to
promote the progress of multimodal sentiment analysis towards multilingualism.
• Leveraging the robust multimodal capabilities of LMMs, models like GPT-4V and LLava, known for
their strong image captioning abilities, can transform image data into textual format, simplifying
the challenge of modal alignment.
• Utilizing the powerful reasoning capabilities of LLMs, existing work has shown that effective In-
Context Learning (ICL) can enhance the emotional reasoning capabilities of LLMs, significantly
improving their ability to trace and guide emotional understanding.
• Fine-tuning with high-quality multimodal sentiment data using a parameter-tuning paradigm, such
as the A2II model, has also been successful. Although it used the smaller-scale Flan-T5-base model,
there is anticipation for methods that adopt parameter-efficient fine-tuning strategy in larger-scale
LLMs.
• Additionally, the use of LLMs as tools in multimodal sentiment analysis holds a promising outlook.
However, there are also disadvantages of using LLMs in multimodal sentiment analysis, including:
• LLMs have to face hallucination problems, and the inevitable generation of erroneous knowledge
may lead to incorrect judgments. Enhancing the accuracy and completeness of sentiment judgment-
related knowledge from LLMs while reducing the negative noise caused by biases and hallucinations
remains a pressing challenge.

--- Page 23 ---

Author Hao YANG, et al.
23
• The sensitivity of LLMs to prompts is significant, as different prompts can drastically influence the
output. Choosing the appropriate prompt is challenging.
• Not all LLMs excel in emotional intelligence; as the training of LLMs and LMMs currently aims to
develop a broad range of capabilities, emotional intelligence is just one of many focal points. There-
fore, the emotional capabilities of most models may not be exceptional, and careful consideration
is needed when selecting LLMs for assisting in multimodal sentiment analysis.
• Existing LMMs still lack support for additional modalities. While most LMMs focus on text and
image modalities, and some have video processing capabilities, there is a lack of capacity to handle
other modalities like physiological signals, limiting their use in multimodal sentiment analysis.
• Methods based on the parameter-tuning paradigm face significant costs, requiring several times the
computational resources and time compared to traditional multimodal sentiment analysis models.
Figure 13
Prompt examples for video-based sentiment analysis (Video SA), image-text sentiment classification (Image-Text
SA), and multimodal aspect-based sentiment classification(Image-Text ABSA) respectively. The text inside the dashed box are
demonstration of the few-shot setting and would be removed under the zero-shot setting
4
Evaluations of LLMs-based Multimodal Sentiment Analysis Methods
4.1
Prompting Strategy
When using LLMs, we employ prompts (a specific type of input text) to trigger the model’s response.
Since LLMs are highly sensitive to prompts, even slight variations in semantics can elicit vastly differ-
ent responses. Therefore, prompt design is of paramount importance. Figure 13 shows some prompt
examples.
As shown in Figure 13, in the zero-shot setting, the prompts include the task name, task definition,
and output format. The task name is used to identify and specify the task, while the task definition
provides an explanation of the task, enabling the model to understand the input-output format of the
task and providing a candidate label space for outputs. The output format defines the expected structure
of the output, guiding the model to generate content in the expected format.
In the few-shot setting, additional demonstration sections are added to assist in model inference learn-
ing.

--- Page 24 ---

Author Hao YANG, et al.
24
4.2
Evaluation Metrics
This section discusses the various commonly used metrics used in the field of text-centric multimodal
sentiment analysis tasks [215].
Accuracy is a measure that indicates the proportion of instances correctly predicted out of the total
number of instances. Further, Weighted Accuracy accounts for class imbalances by assigning different
weights to each class.
Accuracy =
TP + TN
TP + TN + FP + TN ,
(19)
Weighted-Accuracy = 1
N
N
X
i=1
wi ·
TPi + TNi
TPi + TNi + FPi + TNi
(20)
where TP represents True Positives, TN represents True Negatives, FP represents False Positives, FN
represents False Negatives, N represents Total Number of Instances, wi represents Weight for Class i.
Precision evaluates the fraction of true positive predictions among instances that have been predicted
as positive.
Precision =
TP
TP + FP
(21)
Recall, which is sometimes referred to as Sensitivity or True Positive Rate, quantifies the proportion
of true positive instances that are accurately predicted.
Recall =
TP
TP + FN
(22)
The F1-Score merges precision and recall to offer a well-rounded assessment of the model’s accuracy.
Additionally, the Weighted F1-Score accounts for class imbalances.
F1-Score = 2 · Precision · Recall
Precision + Recall,
(23)
Weighted-F1-Score = 1
N
N
X
i=1
wi · 2 · Precisioni · Recalli
Precisioni + Recalli
(24)
4.3
Reference Results
With the in-depth development of LLMs in the field of multimodal sentiment analysis, it is necessary
to compare the performance of LLMs on multimodal sentiment analysis datasets. However, testing on
commercial LLMs such as ChatGPT is often expensive. Some works [141, 160, 171, 206, 207, 213, 214, 217]
have demonstrated the performance of some LLMs on multimodal sentiment analysis tasks, We have
organized the relevant results in the table 4.
5
Applications of text-centric multimodal sentiment analysis
The research in text-centric multimodal sentiment analysis has its roots in the flourishing development of
multimodal data and the advancements in deep learning technologies. It is also driven by a wide range of
practical applications. In this section we explore the application of LLM-based text-centric multimodal
sentiment analysis.
5.1
Comment analysis
One of the earliest and most impactful applications of sentiment analysis was in the field of e-commerce
for comment analysis. This research area not only attracted numerous computer scientists who delved
into algorithm development but also drew the interest of management scientists exploring marketing and
management strategies. Initially, these studies primarily revolved around textual comments, analyzing
user reviews to gather feedback on products or services. However, as e-commerce evolved, relying solely

--- Page 25 ---

Author Hao YANG, et al.
25
Table 4
An overview of the performance of existing LLMs and LMMs on text-centric multimodal sentiment analysis benchmarks.
∗indicates the model results after training on the MMSD and MMSD2.0 dataset. Italicized words represent the few-shot results,
and the rest are zero-shot results. Bold represents the best zero-shot results.
Method
MVSA-S
MVSA-M
TumEmo
Twitter-2015
Twitter-2017
MMSD
MMSD2.0
MOSI-2
MOSEI
CH-SIMS
M3ED
Acc.
Acc.
Acc.
Acc.
F1
Acc.
F1
Acc.
F1
Acc.
F1
Acc.
F1
Acc.
F1
Acc.
F1
Acc.
F1
ChatGPT
56.55
53.18
48.17
65.28
63.12
62.47
62.34
69.02
-
-
-
86.13
85.92
85.60
84.43
79.66
78.78
44.47
40.40
Claude
-
-
-
-
-
-
-
-
-
-
-
87.04
86.55
85.83
84.81
88.70
87.44
34.90
34.83
LLaMA1-7B
67.23
60.72
38.26
58.53
-
46.43
-
58.99
-
-
-
82.01
-
75.62
-
-
-
-
-
LLaMA1-13B
66.88
68.82
44.68
52.07
-
47.24
-
57.53
-
-
-
72.10
-
79.55
-
-
-
-
-
LLaMA2-7B
66.99
69.22
40.28
58.53
-
46.60
-
56.33
-
-
-
67.68
-
77.30
-
-
-
-
-
LLaMA2-13B
66.02
68.69
45.78
60.37
-
48.54
-
60.23
-
-
-
81.86
-
81.66
-
-
-
-
-
Mixtral-AWQ
54.37
55.59
43.94
55.45
-
60.21
-
64.38
-
-
-
87.92
-
79.30
-
-
-
-
-
Gemma
67.72
61.61
43.10
54.29
-
52.43
-
60.07
-
-
-
81.65
-
77.05
-
-
-
-
-
Flan-T5-XXL
64.81
66.01
49.56
72.13
-
63.70
-
71.40
-
-
-
89.60
-
86.52
-
-
-
-
-
ChatGLM2-6B
-
-
-
-
-
-
-
-
-
-
-
84.12
84.12
-
-
77.58
75.95
45.68
30.52
ChatGLM2-6B*
-
-
-
-
-
-
-
94.02
93.76
78.41
78.23
-
-
-
-
-
-
-
-
LLaMA2-7B*
-
-
-
-
-
-
-
93.97
93.72
82.52
82.27
-
-
-
-
-
-
-
-
GPT-4V
76.19
71.05
50.58
53.85
-
60.16
-
76.76
-
-
-
90.91
-
87.10
-
-
-
-
-
Claude3-V
80.95
69.08
46.15
38.46
-
54.47
-
71.37
-
-
-
78.79
-
79.93
-
-
-
-
-
Gemini-V
72.73
70.18
51.65
54.51
-
59.32
-
56.83
-
-
-
88.34
-
87.14
-
-
-
-
-
OpenFlamingo
55.58
61.15
29.47
57.28
-
46.19
-
52.68
-
-
-
79.97
-
77.30
-
-
-
-
-
Fromage
29.85
28.19
22.76
19.96
-
27.31
-
40.68
-
-
-
57.19
-
47.41
-
-
-
-
-
LLaVA-v0-7B
69.42
65.42
30.44
35.10
-
44.57
-
43.21
-
-
-
74.69
-
74.65
-
-
-
-
-
LLaVA-v0-13B
73.06
69.61
38.51
37.99
-
48.46
-
44.29
-
-
-
80.18
-
76.58
-
-
-
-
-
LLaVA-v1.6-7B
59.95
67.23
45.12
59.31
-
52.84
-
59.61
-
-
-
85.63
-
81.62
-
-
-
-
-
LLaVA-v1.6-13B
64.56
60.43
53.22
58.73
-
56.08
-
62.31
-
-
-
86.39
-
78.26
-
-
-
-
-
MiniGPT4
71.12
70.78
50.29
47.16
-
49.43
-
57.49
-
-
-
83.99
-
83.38
-
-
-
-
-
mPLOG-Owl
51.94
50.36
33.37
33.75
-
38.74
-
49.73
-
-
-
68.75
-
58.10
-
-
-
-
-
mPLOG-Owl2.1
53.64
63.11
47.02
60.66
-
55.11
-
60.48
-
-
-
85.63
-
73.47
-
-
-
-
-
AdapterV2
73.54
70.13
39.14
37.32
-
48.38
-
57.20
-
-
-
86.43
-
82.02
-
-
-
-
-
VPGTrans
64.32
69.54
46.17
42.62
-
44.81
-
65.04
-
-
-
76.22
-
76.76
-
-
-
-
-
MultiGPT
52.91
62.03
30.26
58.53
-
46.35
-
59.82
-
-
-
68.35
-
72.76
-
-
-
-
-
LaVIN-7B
39.32
40.75
26.84
37.22
-
33.06
-
60.48
-
-
-
71.41
-
69.97
-
-
-
-
-
LaVIN-13B
53.64
48.79
32.77
35.39
-
40.68
-
57.58
-
-
-
79.97
-
73.54
-
-
-
-
-
Lynx
64.32
67.71
42.79
46.00
-
47.00
-
43.96
-
-
-
74.77
-
73.72
-
-
-
-
-
Fuyu-8B
48.54
55.46
46.34
58.82
-
50.81
-
61.44
-
-
-
83.49
-
78.37
-
-
-
-
-
LaVIT
61.65
68.74
41.78
36.84
-
43.36
-
56.00
-
-
-
73.09
-
64.10
-
-
-
-
-
Qwen-VL-Chat
62.38
69.06
49.29
65.48
-
59.72
-
61.10
-
-
-
85.93
-
80.41
-
-
-
-
-
BLIP
66.26
68.22
51.06
70.78
-
64.42
-
72.02
-
-
-
88.99
-
86.88
-
-
-
-
-
InstructBLIP
71.60
70.37
52.36
57.57
59.63
60.37
35.96
73.10
-
-
-
88.68
-
85.98
-
-
-
-
-
LLaVA-v1.5-7B*
-
-
-
-
-
-
-
93.67
93.40
85.18
85.11
-
-
-
-
-
-
-
-
mPLUG-Owl2
-
-
-
76.80
72.30
74.20
73.00
-
-
-
-
-
-
-
-
-
-
-
-
MMICL-14B
-
-
-
76.00
72.70
74.10
74.00
-
-
-
-
-
-
-
-
-
-
-
-
LLaVA-v1.5-13B
-
-
-
77.90
74.30
74.60
74.30
-
-
51.06
43.02
-
-
-
-
-
-
-
-
Qwen-VL-v1.0
-
-
-
-
-
-
-
-
-
76.63
69.03
-
-
-
-
-
-
-
-
on text-based sentiment analysis proved insufficient. User-generated comments often include multimedia
elements, making multimodal data more prominent compared to pure text comments.
With the increasing availability of multimodal data on social networks, some of the challenges that
puzzled researchers can be alleviated in a multimodal interactive context, enabling comprehensive senti-
ment analysis. For instance, one challenging problem is sarcasm recognition, which can be easily resolved
with the addition of multimodal information. For example, when a comment like “It’s such a surprise”
is accompanied by a picture of a disappointed face, sarcasm recognition becomes straightforward. In
the field of management, multimodal data, enriched with additional modal factors, can influence user
decisions and consequently impact marketing and management strategies.
In practical applications, fine-grained sentiment analysis is more effective. In text-based analysis stud-
ies, user textual comment data can be broken down into fine-grained segments (e.g., sentences, clauses),
with each segment evaluating different aspects of the main entity (e.g., price, quality, appearance). In
contrast, fine-grained analysis of multimodal data is still in its emerging stages but presents greater chal-
lenges. For instance, extracting object-level information from complex multimodal data and modeling
fine-grained element correspondences between multimodal elements are ongoing research topics that need
exploration with LLMs in the future.
5.2
Multimodal intelligent human-machine interaction
Multimodal sentiment analysis can be applied to human-computer interaction, enabling real-time under-
standing and analysis of emotional communication for more natural interactions. There are three main
categories of applications:
1) Customer Service Conversations.
In this domain, multimodal data consists of audio data
and text data transformed from Automatic Speech Recognition (ASR) technology. It mainly serves two
tasks: customer satisfaction analysis and detection of customer abnormal emotions. Customer satisfaction
analysis involves using multimodal emotion computing technology to analyze the content of conversations
between customers and service representatives to assess the level of customer satisfaction. Customer

--- Page 26 ---

Author Hao YANG, et al.
26
abnormal emotion detection monitors customer emotions in real time through the analysis of customer
dialogue data and prompts timely intervention when abnormal emotional changes occur.
2) Emotional Companionship. Emotional companionship is a crucial aspect of chatbot applica-
tions. Currently, most companion chatbots do not utilize multimodal emotion computing technology,
meaning they do not fully possess human-like multimodal processing capabilities. Ideally, companion
chatbots should be capable of recognizing and generating multimodal emotional features, such as ex-
pressing emotions through language, exhibiting emotional fluctuations in speech, or displaying facial
expressions.
3) Smart Furniture The development of artificial intelligence has given rise to smart homes, which
enhance convenience and comfort in daily life and are increasingly popular among consumers. Many tech
companies worldwide have entered the smart home market, proposing a range of solutions like Apple’s
HomeKit, Xiaomi’s Mi Home, and Haier’s U-Home. While smart homes have made life more convenient,
they are currently primarily focused on home automation, with users controlling home devices through
voice commands based on keyword recognition. This approach does not fully embody the intelligence of
smart homes, and there is substantial potential for further development, particularly in voice interaction
and automatic environment detection.
With the assistance of LLMs, AI technologies based on multimodal sentiment analysis methods can
elevate the intelligence of smart homes in the future. True smart home scenarios involve multiple modal-
ities, where smart home products can provide appropriate feedback by calculating the user’s emotions
(e.g., happiness, anger, sadness) or states (e.g., fatigue, restlessness). For example, based on a user’s
fatigue state in a multimodal scenario, the system could ask if they want the lights dimmed. In conver-
sational scenarios, the system can detect the user’s emotional state and provide empathetic responses.
Smart in-car systems can promptly detect abnormal user emotions or states (e.g., road rage, fatigue)
and provide appropriate reminders. Designing these functionalities poses significant challenges, but it
also represents a significant opportunity for multimodal emotion computing to enter the smart furniture
domain.
6
Conclusions
In this survey, we introduced the latest advancements in text-centric multimodal sentiment analysis area
and summarized the primary challenges and potential solutions. Additionally, we reviewed the existing
ways of applying LLMs in multimodal sentiment analysis tasks and summarized their advantages and
disadvantages. We believe that leveraging LLMs in multimodal sentiment analysis has several potential
advantages: 1) Knowledge Source: LLMs trained on massive datasets and can be treated as a knowledge
source, that can capture a broader range of patterns, linguistic cues, and contextual information related
to emotions, potentially improving recognition performance. 2) Interpretability: LLMs can potentially
elucidate the reasoning behind their decisions, enhancing the interpretability and transparency of the
emotion recognition process. 3) Cross-Domain Applications: LLMs have the potential to be applied across
various domains, as they are trained on a wide range of data sources. This allows them to understand
emotions expressed in various domains, from customer reviews to conversational data, thus achieving
broader applicability. However, LLMs-based methods also have to face problems such as hallucinations
and high fine-tuning costs. The emergence of LLMs provides new ideas and challenges for multimodal
sentiment analysis. We hope that this survey can help and encourage further research in this field.

--- Page 27 ---

Author Hao YANG, et al.
27
References
1
Hatzivassiloglou V, McKeown KR. Predicting the semantic orientation of adjectives. InProc. of the
EACL’97. Morristown: ACL, 1997. 174-181.
2
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-
Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey
Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray,
Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever,
and Dario Amodei. 2020. Language models are few-shot learners. In Advances in Neural Information
Processing Systems 33: Annual Conference on Neural Information Processing Systems 2020, NeurIPS
2020, December 6-12, 2020, virtual.
3
Jack W. Rae, Sebastian Borgeaud, Trevor Cai, Katie Millican, Jordan Hoffmann, H. Francis Song,
John Aslanides, Sarah Henderson, Roman Ring, Susannah Young, Eliza Rutherford, Tom Henni-
gan, Jacob Menick, Albin Cassirer, Richard Powell, George van den Driessche, Lisa Anne Hendricks,
Maribeth Rauh, Po-Sen Huang, Amelia Glaese, Johannes Welbl, Sumanth Dathathri, Saffron Huang,
Jonathan Uesato, John Mellor, Irina Higgins, Antonia Creswell, Nat McAleese, Amy Wu, Erich Elsen,
Siddhant M. Jayakumar, Elena Buchatskaya, David Budden, Esme Sutherland, Karen Simonyan,
Michela Paganini, Laurent Sifre, Lena Martens, Xiang Lorraine Li, Adhiguna Kuncoro, Aida Ne-
matzadeh, Elena Gribovskaya, Domenic Donato, Angeliki Lazaridou, Arthur Mensch, JeanBaptiste
Lespiau, Maria Tsimpoukelli, Nikolai Grigorev, Doug Fritz, Thibault Sottiaux, Mantas Pajarskas,
Toby Pohlen, Zhitao Gong, Daniel Toyama, Cyprien de Masson d’Autume, Yujia Li, Tayfun Terzi,
Vladimir Mikulik, Igor Babuschkin, Aidan Clark, Diego de Las Casas, Aurelia Guy, Chris Jones,
James Bradbury, Matthew J. Johnson Blake A. Hechtman, LauraWeidinger, Iason Gabriel, William
S. Isaac, Edward Lockhart, Simon Osindero, Laura Rimell, Chris Dyer, Oriol Vinyals, Kareem Ay-
oub, Jeff Stanway, Lorrayne Bennett, Demis Hassabis, Koray Kavukcuoglu, and Geoffrey Irving. 2021.
Scaling language models: Methods, analysis & insights from training gopher. CoRR, abs/2112.11446.
4
OpenAI. 2023. GPT-4 technical report. CoRR , abs/2303.08774.
5
Chao Zhang, Zichao Yang, Xiaodong He and Li Deng. Multimodal Intelligence: Representation
Learning, Information Fusion, and Applications. IEEE JOURNAL OF SELECTED TOPICS IN
SIGNAL PROCESSING. 2020, 14(3): 478-493.
6
Xiang Deng, Vasilisa Bashlovkina, Feng Han, Simon Baumgartner, and Michael Bendersky. 2023.
Llms to the moon? reddit market sentiment analysis with LLMs. In Companion Proceedings of the
ACM Web Conference 2023, WWW2023, pages 1014-1019.
7
Qihuang Zhong, Liang Ding, Juhua Liu, Bo Du, and Dacheng Tao. 2023. Can chatgpt understand
too? A comparative study on chatgpt and fine-tuned BERT. CoRR, abs/2302.10198.
8
Zengzhi Wang, Qiming Xie, Zixiang Ding, Yi Feng, and Rui Xia. 2023. Is chatgpt a good sentiment
analyzer? A preliminary study. CoRR, abs/2304.04339.
9
Zhang W, Deng Y, Liu B, et al. Sentiment Analysis in the Era of Large Language Models: A Reality
Check[J]. arXiv preprint arXiv:2305.15005, 2023.
10
Yejin Bang, Samuel Cahyawijaya, Nayeon Lee, Wenliang Dai, Dan Su, Bryan Wilie, Holy Lovenia,
Ziwei Ji, Tiezheng Yu, Willy Chung, Quyet V. Do, Yan Xu, and Pascale Fung. 2023. A multitask,
multilingual, multimodal evaluation of chatgpt on reasoning, hallucination, and interactivity. CoRR,
abs/2302.04023.
11
Junjie Ye, Xuanting Chen, Nuo Xu, Can Zu, Zekai Shao, Shichun Liu, Yuhan Cui, Zeyang Zhou,
Chao Gong, Yang Shen, Jie Zhou, Siming Chen, Tao Gui, Qi Zhang, and Xuanjing Huang. 2023. A
comprehensive capability analysis of GPT-3 and GPT-3.5 series models. CoRR, abs/2303.10420
12
Jingfeng Yang, Hongye Jin, Ruixiang Tang, Xiaotian Han, Qizhang Feng, Haoming Jiang, Bing Yin,
and Xia Hu. 2023. Harnessing the power of llms in practice: A survey on chatgpt and beyond. CoRR,
abs/2304.13712.

--- Page 28 ---

Author Hao YANG, et al.
28
13
Richard Socher, Alex Perelygin, Jean Wu, Jason Chuang, Christopher D. Manning, Andrew Y. Ng,
and Christopher Potts. 2013. Recursive deep models for semantic compositionality over a sentiment
treebank. In Proceedings of the 2013 Conference on Empirical Methods in Natural Language Process-
ing, EMNLP 2013, 18-21 October 2013, Grand Hyatt Seattle, Seattle, Washington, USA, A meeting
of SIGDAT, a Special Interest Group of the ACL, pages 1631-1642.
14
Tadas Baltrus aitis, Chaitanya Ahuja, and Louis-Philippe Morency. Multimodal machine learning: A
survey and taxonomy. IEEE transactions on pattern analysis and machine intelligence. 2018, 41(2):
423-443.
15
Paul Mc Kevitt. MultiModal Semantic Representation[C]// Tilburg University. First Working Meet-
ing of the SIGSEM Working Group on the Representation of MultiModal Semantic Information.
Tilburg: Tilburg University, 2003: 1-16.
16
Yi Tay, Mostafa Dehghani, Vinh Q. Tran, Xavier Garcia, Dara Bahri, Tal Schuster, Huaixiu Steven
Zheng, Neil Houlsby, and Donald Metzler. 2022. Unifying language learning paradigms. CoRR,
abs/2205.05131.
17
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothee
Lacroix, Baptiste Roziere, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand
Joulin, Edouard Grave, and Guillaume Lample. 2023. Llama: Open and efficient foundation language
models. CoRR, abs/2302.13971.
18
Zhu D, Chen J, Shen X, et al. Minigpt-4: Enhancing vision-language understanding with advanced
large language models[J]. arXiv preprint arXiv:2304.10592, 2023.
19
Liu H, Li C, Wu Q, et al. Visual instruction tuning[J]. arXiv preprint arXiv:2304.08485, 2023.
20
Wenliang Dai and Junnan Li and Dongxu Li and Anthony Meng Huat Tiong and Junqi Zhao and
Weisheng Wang and Boyang Li and Pascale Fung and Steven Hoi. InstructBLIP: Towards General-
purpose Vision-Language Models with Instruction Tuning[J]. arXiv preprint arXiv:2305.06500, 2023.
21
https://www.bing.com.
22
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam
Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, Parker Schuh,
Kensen Shi, Sasha Tsvyashchenko, Joshua Maynez, Abhishek Rao, Parker Barnes, Yi Tay, Noam
Shazeer, Vinodkumar Prabhakaran, Emily Reif, Nan Du, Ben Hutchinson, Reiner Pope, James
Bradbury, Jacob Austin, Michael Isard, Guy Gur-Ari, Pengcheng Yin, Toju Duke, Anselm Levskaya,
Sanjay Ghemawat, Sunipa Dev, Henryk Michalewski, Xavier Garcia, Vedant Misra, Kevin Robinson,
Liam Fedus, Denny Zhou, Daphne Ippolito, David Luan, Hyeontaek Lim, Barret Zoph, Alexander
Spiridonov, Ryan Sepassi, David Dohan, Shivani Agrawal, Mark Omernick, Andrew M. Dai, Thanu-
malayan Sankaranarayana Pillai, Marie Pellat, Aitor Lewkowycz, Erica Moreira, Rewon Child, Olek-
sandr Polozov, Katherine Lee, Zongwei Zhou, Xuezhi Wang, Brennan Saeta, Mark Diaz, Orhan Firat,
Michele Catasta, Jason Wei, Kathy Meier-Hellstern, Douglas Eck, Jeff Dean, Slav Petrov, and Noah
Fiedel. 2022. Palm: Scaling language modeling with pathways. CoRR, abs/2204.02311.
23
Taylor R, Kardas M, Cucurull G, et al. Galactica: A large language model for science[J]. arXiv
preprint arXiv:2211.09085, 2022.
24
Meta A I. Introducing LLaMA: A foundational, 65-billion-parameter large language model[J]. Meta
AI. https://ai. facebook. com/blog/large-language-model-llama-meta-ai, 2023.
25
Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du,
Andrew M. Dai, and Quoc V. Le. 2022a. Finetuned language models are zero-shot learners. In The
Tenth International Conference on Learning Representations, ICLR 2022, Virtual Event, April 25-29,
2022. OpenReview.net.

--- Page 29 ---

Author Hao YANG, et al.
29
26
Victor Sanh, Albert Webson, Colin Raffel, Stephen H. Bach, Lintang Sutawika, Zaid Alyafeai, An-
toine Chaffin, Arnaud Stiegler, Arun Raja, Manan Dey, M Saiful Bari, Canwen Xu, Urmish Thakker,
Shanya Sharma Sharma, Eliza Szczechla, Taewoon Kim, Gunjan Chhablani, Nihal V. Nayak, Deba-
jyoti Datta, Jonathan Chang, Mike Tian-Jian Jiang, Han Wang, Matteo Manica, Sheng Shen, Zheng
Xin Yong, Harshit Pandey, Rachel Bawden, Thomas Wang, Trishala Neeraj, Jos Rozen, Abheesht
Sharma, Andrea Santilli, Thibault Fevry, Jason Alan Fries, Ryan Teehan, Teven Le Scao, Stella Bi-
derman, Leo Gao, Thomas Wolf, and Alexander M. Rush. 2022. Multitask-prompted training enables
zero-shot task generalization. In The Tenth International Conference on Learning Representations,
ICLR 2022, Virtual Event, April 25-29, 2022. OpenReview.net.
27
Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi
Wang, Mostafa Dehghani, Siddhartha Brahma, Albert Webson, Shixiang Shane Gu, Zhuyun Dai,
Mirac Suzgun, Xinyun Chen, Aakanksha Chowdhery, Sharan Narang, Gaurav Mishra, Adams Yu,
Vincent Y. Zhao, Yanping Huang, Andrew M. Dai, Hongkun Yu, Slav Petrov, Ed H. Chi, Jeff Dean,
Jacob Devlin, Adam Roberts, Denny Zhou, Quoc V. Le, and Jason Wei. 2022. Scaling instruction-
finetuned language models. CoRR, abs/2210.11416.
28
Zhang Z, Peng L, Pang T, et al. Refashioning Emotion Recognition Modelling: The Advent of
Generalised Large Models[J]. arXiv preprint arXiv:2308.11578, 2023.
29
Cao D, Ji R, Lin D, et al. A Cross-media Public Sentiment Analysis System for Microblog[J]. Multi-
media Systems, 2016, 22(4): 479-486.
30
You Q, Cao L, Jin H, et al. Robust Visual-textual Sentiment Analysis: When Attention Meets Tree-
structured Recursive Neural Networks[C]// In Proceedings of the 24th ACM international conference
on multimedia. New York: ACM, 2016: 1008-1017.
31
Truong Q T, Lauw H W. Vistanet: Visual Aspect Attention Network for Multimodal Sentiment
Analysis[C]// In Proceedings of the AAAI Conference on Artificial Intelligence. Palo Alto, California
USA: AAAI Press, 2019, 33(1): 305-312.
32
Khan Z, Fu Y. Exploiting BERT For Multimodal Target Sentiment Classification Through Input
Space Translation[C]// In Proceedings of the 29th ACM International Conference on Multimedia.
2021: 3034-3042.
33
Zadeh A, Chen M, Poria S, et al. Tensor Fusion Network for Multimodal Sentiment Analysis[C] //
In Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing. [S.l.]:
Association for Computational Linguistics, 2017: 1103-1114.
34
Wang Y, Shen Y, Liu Z, et al. Words can shift: Dynamically adjusting word representations using
nonverbal behaviors[C]// In Proceedings of the AAAI Conference on Artificial Intelligence. 2019,
33(01): 7216-7223.
35
Hazarika D, Zimmermann R, Poria S. MISA: Modality-Invariant and -Specific Representations for
Multimodal Sentiment Analysis // In Proceedings of the 28th ACM International Conference on
Multimedia. New York: ACM, 2020: 1122-1131.
36
Chen M, Wang S, Liang P P, et al. Multimodal Sentiment Analysis with WordLevel Fusion and
Reinforcement Learning // In Proceedings of the 19th ACM International Conference on Multimodal
Interaction. New York: ACM, 2017: 163-171.
37
Rahman W, Hasan M K, Lee S, et al. Integrating Multimodal Information in LargePretrained Trans-
formers[C]// In Proceedings of the 58th Annual Meeting of the Association for Computational Lin-
guistics. [S.l.]: Association for Computational Linguistics, 2020: 2359-2369.
38
Li L, Chen Y C, Cheng Y, et al. Hero:
Hierarchical Encoder for Video+ Language Omni-
representation Pre-training[C]// In Proceedings of the 2020 Conference on Empirical Methods in
Natural Language Processing (EMNLP). [S.l.]: Association for Computational Linguistics, 2020:
2046-2065.

--- Page 30 ---

Author Hao YANG, et al.
30
39
Cao D, Ji R, Lin D, et al. A Cross-media Public Sentiment Analysis System for Microblog[J]. Multi-
media Systems, 2016, 22(4): 479-486.
40
Yu W, Xu H, Yuan Z, et al. Learning modality-specific representations with self-supervised multi-task
learning for multimodal sentiment analysis[J]. arXiv preprint arXiv:2102.04830, 2021.
41
Wu Y, Zhao Y, Yang H, et al. Sentiment Word Aware Multimodal Refinement for Multimodal
Sentiment Analysis with ASR Errors[J]. arXiv preprint arXiv:2203.00257, 2022.
42
Liang B, Lou C, Li X, et al. Multi-Modal Sarcasm Detection with Interactive In-Modal and Cross-
Modal Graphs[C]// In Proceedings of the 29th ACM International Conference on Multimedia. 2021:
4707-4715.
43
Tsai Y H H, Bai S, Liang P P, et al. Multimodal transformer for unaligned multimodal language
sequences[C]// Association for Computational Linguistics. Proceedings of the 57th Annual Meeting
of the Association for Computational Linguistics. Florence, Italy: Association for Computational
Linguistics, 2019: 6558-6569.
44
Torres, E.P.; Torres, E.A.; Hernandez-Alvarez, M.; Yoo, S.G. EEG-Based BCI Emotion Recognition:
A Survey. Sensors 2020, 20, 5083. https://doi.org/10.3390/s20185083.
45
Xiao-Wei Wang, Dan Nie, and Bao-Liang Lu. Eeg-based emotion recognition using frequency domain
features and support vector machines. In International conference on neural information processing,
pages 734-743. Springer, 2011.
46
Fatemeh Bahari and Amin Janghorbani. Eeg-based emotion recognition using recurrence plot anal-
ysis and k nearest neighbor classifier. In 2013 20th Iranian Conference on Biomedical Engineering
(ICBME), pages 228-233. IEEE, 2013.
47
Jia, Ziyu & Lin, Youfang & Cai, Xiyang & Chen, Haobin & Gou, Haijun & Wang, Jing. (2020).
SST-EmotionNet: Spatial-Spectral-Temporal based Attention 3D Dense Network for EEG Emotion
Recognition. 2909-2917. 10.1145/3394171.3413724.
48
Deng, Xiangwen & Yang, Shangming & Zhu, Junlin. (2021). SFE-Net: EEG-based Emotion Recog-
nition with Symmetrical Spatial Feature Extraction.
49
Riloff E, Qadir A, Surve P, et al. Sarcasm as Contrast between a Positive Sentiment and Nega-
tive Situation[C]// Proceedings of the 2013 Conference on Empirical Methods in Natural Language
Processing. [S.l.]: Association for Computational Linguistics, 2013: 704-714.
50
Yi Tay, Anh Tuan Luu, Siu Cheung Hui, and Jian Su. Reasoning with sarcasm by reading in between.
Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics. 2018:
1010-1020.
51
Xiong T, Zhang P, Zhu H, et al. Sarcasm Detection with Self-matching Networks and Low-Rank
Bilinear Pooling[C]// The World Wide Web Conference. New York: ACM, 2019: 2115-2124.
52
Cheang H S, Pell M D. The Sound of Sarcasm[J]. Speech Communication, 2008, 50(5): 366-381.
53
Santiago Castro, Devamanyu Hazarika, Veronica PerezRosas, Roger Zimmermann, Rada Mihalcea,
and Soujanya Poria. Towards multimodal sarcasm detection (an obviously perfect paper). Proceedings
of the 57th Annual Meeting of the Association for Computational Linguistics. 2019: 4619-4629.
54
Dushyant Singh Chauhan, SR Dhanush, Asif Ekbal, and Pushpak Bhattacharyya. Sentiment and
emotion help sarcasm? a multi-task learning framework for multi-modal sarcasm, sentiment and
emotion analysis. Proceedings of the 58th Annual Meeting of the Association for Computational
Linguistics. 2020: 4351-4360.
55
Yitao Cai, Huiyu Cai, and Xiaojun Wan. Multimodal sarcasm detection in twitter with hierarchi-
cal fusion model. Proceedings of the 57th Annual Meeting of the Association for Computational
Linguistics. 2019: 2506-2515.

--- Page 31 ---

Author Hao YANG, et al.
31
56
Tang D, Qin B, Feng X, et al. Effective LSTMs for target-dependent sentiment classification[J]. arXiv
preprint arXiv:1512.01100, 2015.
57
Wu, Yang & Zhao, Yanyan & Lu, Xin & Qin, Bing & Wu, Yin & Sheng, Jian & Li, Jinlong. (2021).
Modeling Incongruity between Modalities for Multimodal Sarcasm Detection. IEEE MultiMedia. PP.
1-1. 10.1109/MMUL.2021.3069097.
58
Jennifer Woodland and Daniel Voyer. Context and intonation in the perception of sarcasm. Metaphor
and Symbol. 2011, 26(3):227-239.
59
Ma D, Li S, Zhang X, et al. Interactive attention networks for aspect-level sentiment classification[J].
arXiv preprint arXiv:1709.00893, 2017.
60
Zhang C, Li Q, Song D. Aspect-based sentiment classification with aspect-specific graph convolutional
networks[J]. arXiv preprint arXiv:1909.03477, 2019.
61
Zeng B, Yang H, Xu R, et al. Lcf: A local context focus mechanism for aspect-based sentiment
classification[J]. Applied Sciences, 2019, 9(16): 3389.
62
Wang Y, Qian S, Hu J, et al. Fake news detection via knowledge-driven multimodal graph convolu-
tional networks[C]//Proceedings of the 2020 International Conference on Multimedia Retrieval. 2020:
540-547.
63
Mesnil G, He X, Deng L, et al. Investigation of recurrent-neural-network architectures and learning
methods for spoken language understanding[C]//Interspeech. 2013: 3771-3775.
64
Liu P, Joty S, Meng H. Fine-grained opinion mining with recurrent neural networks and word embed-
dings[C]//Proceedings of the 2015 conference on empirical methods in natural language processing.
2015: 1433-1443.
65
Mitchell M, Aguilar J, Wilson T, et al. Open domain targeted sentiment[C]//Proceedings of the 2013
Conference on Empirical Methods in Natural Language Processing. 2013: 1643-1654.
66
Cho K, Van Merrienboer B, Gulcehre C, et al. Learning phrase representations using RNN encoder-
decoder for statistical machine translation[J]. arXiv preprint arXiv:1406.1078, 2014.
67
Sutskever I, Vinyals O, Le Q V. Sequence to sequence learning with neural networks[J]. Advances in
neural information processing systems, 2014, 27.
68
Chen K, Wang J, Pang J, et al. MMDetection: Open mmlab detection toolbox and benchmark[J].
arXiv preprint arXiv:1906.07155, 2019.
69
Y.
Wu,
A.
Kirillov,
F.
Massa,
W.-Y.
Lo,
and
R.
Girshick,
”Detec-
tron2,”https://github.com/facebookresearch/ detectron2, 2019.
70
Yang X, Feng S, Zhang Y, et al. Multimodal Sentiment Detection Based on Multi-channel Graph
Neural Networks[C]//Proceedings of the 59th Annual Meeting of the Association for Computational
Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1:
Long Papers). 2021: 328-339.
71
Amos B, Ludwiczuk B, Satyanarayanan M. Openface: A general-purpose face recognition library
with mobile applications[J]. CMU School of Computer Science, 2016, 6(2): 20.
72
Wu, Yang & Zhao, Yanyan & Lu, Xin & Qin, Bing & Wu, Yin & Sheng, Jian & Li, Jinlong. (2021).
Modeling Incongruity between Modalities for Multimodal Sarcasm Detection. IEEE MultiMedia. PP.
1-1. 10.1109/MMUL.2021.3069097.
73
Tian Y L, Kanade T, Cohn J F. Facial expression analysis[M]//Handbook of face recognition.
Springer, New York, NY, 2005: 247-275.
74
Tsai Y H H, Bai S, Liang P P, et al. Multimodal transformer for unaligned multimodal language
sequences[C] //Proceedings of the conference. Association for Computational Linguistics. Meeting.
NIH Public Access, 2019, 2019: 6558.

--- Page 32 ---

Author Hao YANG, et al.
32
75
Degottex G, Kane J, Drugman T, et al. COVAREP-A collaborative voice analysis repository for
speech technologies[C]//2014 ieee international conference on acoustics, speech and signal processing
(icassp). IEEE, 2014: 960-964.
76
Wenmeng Yu, Hua Xu, Fanyang Meng, Yilin Zhu, Yixiao Ma, Jiele Wu, Jiyun Zou and Kaicheng
Yang. CH-SIMS: A Chinese Multimodal Sentiment Analysis Dataset with Fine-grained Annotations
of Modality. Proceedings of the 58th Annual Meeting of the Association for Computational Linguis-
tics. 2020: 3718-3727.
77
Nan Xu, Wenji Mao, Guandan Chen. Multi-interactive memory network for aspect based multimodal
sentiment analysis. Proceedings of the AAAI Conference on Artificial Intelligence. 2019: 371-378.
78
Yu J, Jiang J, Xia R. Entity-sensitive attention and fusion network for entity-level multimodal senti-
ment classification[J]. IEEE/ACM Transactions on Audio, Speech, and Language Processing, 2019,
28: 429-439.
79
Yu J, Jiang J. Adapting BERT for target-oriented multimodal sentiment classification[C]. IJCAI,
2019.
80
Ling Y, Yu J, Xia R. Vision-language pre-training for multimodal aspect-based sentiment analysis[J].
arXiv preprint arXiv:2204.07955, 2022.
81
Hu J, Liu Y, Zhao J, et al. MMGCN: Multimodal fusion via deep graph convolution network for
emotion recognition in conversation[J]. arXiv preprint arXiv:2107.06779, 2021.
82
Wang Z, Ji H. Open Vocabulary Electroencephalography-To-Text Decoding and Zero-shot Sentiment
Classification[J]. arXiv preprint arXiv:2112.02690, 2021.
83
Vinyals O, Toshev A, Bengio S, et al. Show and tell:
A neural image caption genera-
tor[C]//Proceedings of the IEEE conference on computer vision and pattern recognition. 2015: 3156-
3164.
84
Xu K, Ba J, Kiros R, et al. Show, attend and tell: Neural image caption generation with visual
attention[C]//International conference on machine learning. PMLR, 2015: 2048-2057.
85
Chen, Long, et al. ”SCA-CNN: Spatial and Channel-wise Attention in Convolutional Networks for
Image Captioning.” (2016):6298-6306.
86
P. Anderson, X. He, C. Buehler, D. Teney, M. Johnson, S. Gould, and L. Zhang. Bottom-up and
top-down attention for image captioning and visual question answering. In CVPR, volume 3, page
6, 2018.
87
Zhou H, Huang M, Zhang T, et al. Emotional chatting machine: Emotional conversation generation
with internal and external memory[C]//Proceedings of the AAAI Conference on Artificial Intelligence.
2018, 32(1).
88
Nezami O M, Dras M, Wan S, et al. Senti-attend: image captioning using sentiment and attention[J].
arXiv preprint arXiv:1811.09789, 2018.
89
Yu C, Lu H, Hu N, et al. Durian: Duration informed attention network for multimodal synthesis[J].
arXiv preprint arXiv:1909.01700, 2019.
90
Lewis M, Liu Y, Goyal N, et al. Bart: Denoising sequence-to-sequence pre-training for natural lan-
guage generation, translation, and comprehension[J]. arXiv preprint arXiv:1910.13461, 2019.
91
Wu, Yang & Zhao, Yanyan & Lu, Xin & Qin, Bing & Wu, Yin & Sheng, Jian & Li, Jinlong. (2021).
Modeling Incongruity between Modalities for Multimodal Sarcasm Detection. IEEE MultiMedia. PP.
1-1. 10.1109/MMUL.2021.3069097.
92
J. Guo, J. Tang, W. Dai, Y. Ding, and W. Kong, “Dynamically adjust word representations using
unaligned multimodal information,” in Proc. the 30th ACM International Conference on Multimedia
(MM), Lisbon, Portugal, 2022, pp. 3394-3402.

--- Page 33 ---

Author Hao YANG, et al.
33
93
J. Tang, K. Li, X. Jin, A. Cichocki, Q. Zhao, and W. Kong, “CTFN: hierarchical learning for
multimodal sentiment analysis using coupled-translation fusion network,” in Proc. the 59th Annual
Meeting of the Association for Computational Linguistics (ACL), Virtual, 2021, pp. 5301-5311.
94
A. Joshi, A. Bhat, A. Jain, A. V. Singh, and A. Modi, “COGMEN: contextualized GNN based multi-
modal emotion recognition”, in Proc. Conference of the North American Chapter of the Association
for Computational Linguistics: Human Language Technologies (NAACL), Seattle, WA, 2022, pp.
4148-4164.
95
W. Yu, H. Xu, F. Meng, Y. Zhu, Y. Ma, J. Wu, J. Zou, and K. Yang, “CH-SIMS: A Chinese
multimodal sentiment analysis dataset with fine-grained annotation of modality,” in Proc. the 58th
Annual Meeting of the Association for Computational Linguistics (ACL), Virtual, 2020, pp. 3718-
3727.
96
Zheng Z, Zhang Z, Wang Z, Fu R, Liu M, Wang Z, Qin B. Decompose, Prioritize, and Elimi-
nate: Dynamically Integrating Diverse Representations for Multimodal Named Entity Recognition.
InProceedings of the 2024 Joint International Conference on Computational Linguistics, Language
Resources and Evaluation (LREC-COLING 2024) 2024 May (pp. 4498-4508).
97
Yang X, Feng S, Zhang Y, et al. Multimodal sentiment detection based on multi-channel graph
neural networks[C]// In Proceedings of the 59th Annual Meeting of the Association for Computational
Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1:
Long Papers). 2021: 328-339.
98
Yang H, Zhao Y, Qin B. Face-Sensitive Image-to-Emotional-Text Cross-modal Translation for Mul-
timodal Aspect-based Sentiment Analysis[C]// In Proceedings of the 2022 Conference on Empirical
Methods in Natural Language Processing. 2022: 3324-3335.
99
Amir Zadeh, Rowan Zellers, Eli Pincus, and LouisPhilippe Morency. 2016a. Mosi:
Multimodal
corpus of sentiment intensity and subjectivity analysis in online opinion videos. arXiv preprint
arXiv:1606.06259.
100
AmirAli Bagher Zadeh, Paul Pu Liang, Soujanya Poria, Erik Cambria, and Louis-Philippe Morency.
2018b. Multimodal language analysis in the wild: Cmu-mosei dataset and interpretable dynamic fu-
sion graph. In Proceedings ofthe 56th Annual Meeting ofthe Association for Computational Linguistics
(Volume 1: Long Papers), pages 2236-2246.
101
Wenmeng Yu, Hua Xu, Fanyang Meng, Yilin Zhu, Yixiao Ma, Jiele Wu, Jiyun Zou and Kaicheng
Yang. CH-SIMS: A Chinese Multimodal Sentiment Analysis Dataset with Fine-grained Annotations
of Modality. In Proceedings of the 58th Annual Meeting of the Association for Computational Lin-
guistics. 2020: 3718-3727.
102
http://yelp.com/dataset.
103
T. Niu, S. A. Zhu, L. Pang and A. El Saddik, Sentiment Analysis on Multi-view Social Data,
MultiMedia Modeling (MMM), pp: 15-27, Miami, 2016.
104
Yu J, Jiang J. Adapting BERT for target-oriented multimodal sentiment classification[C]. IJCAI,
2019.
105
Vaswani A, Shazeer N, Parmar N, et al. Attention is all you need[J]. Advances in neural information
processing systems, 2017, 30.
106
Chen K, Wang J, Pang J, et al. MMDetection: Open mmlab detection toolbox and benchmark[J].
arXiv preprint arXiv:1906.07155, 2019.
107
Y.
Wu,
A.
Kirillov,
F.
Massa,
W.-Y.
Lo,
and
R.
Girshick,
“Detectron2,”
https://github.com/facebookresearch/ detectron2, 2019.
108
Zhao, Weixiang, Yanyan Zhao, Xin Lu, Shilong Wang, Yanpeng Tong, and Bing Qin. ”Is ChatGPT
Equipped with Emotional Dialogue Capabilities?.” arXiv preprint arXiv:2304.09582 (2023).

--- Page 34 ---

Author Hao YANG, et al.
34
109
Soleymani M, Garcia D, Jou B, Schuller B, Chang SF, Pantic M. A survey of multimodal sentiment
analysis. Image and Vision Computing. 2017 Sep 1;65:3-14.
110
Girdhar R, El-Nouby A, Liu Z, Singh M, Alwala KV, Joulin A, Misra I. Imagebind: One embedding
space to bind them all. InProceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition 2023 (pp. 15180-15190).
111
Team G, Anil R, Borgeaud S, Wu Y, Alayrac JB, Yu J, Soricut R, Schalkwyk J, Dai AM, Hauth A,
Millican K. Gemini: a family of highly capable multimodal models. arXiv preprint arXiv:2312.11805.
2023 Dec 19.
112
Li J, Li D, Savarese S, Hoi S. Blip-2: Bootstrapping language-image pre-training with frozen image
encoders and large language models. InInternational conference on machine learning 2023 Jul 3 (pp.
19730-19742). PMLR.
113
Liu H, Li C, Wu Q, Lee YJ. Visual instruction tuning. Advances in neural information processing
systems. 2024 Feb 13;36.
114
Bai J, Bai S, Yang S, Wang S, Tan S, Wang P, Lin J, Zhou C, Zhou J. Qwen-vl: A frontier large
vision-language model with versatile abilities. arXiv preprint arXiv:2308.12966. 2023 Aug 24.
115
Chiang WL, Li Z, Lin Z, Sheng Y, Wu Z, Zhang H, Zheng L, Zhuang S, Zhuang Y, Gonzalez
JE, Stoica I. Vicuna: An open-source chatbot impressing gpt-4 with 90%* chatgpt quality. See
https://vicuna. lmsys. org (accessed 14 April 2023). 2023 Mar;2(3):6.
116
Radford A, Kim JW, Hallacy C, Ramesh A, Goh G, Agarwal S, Sastry G, Askell A, Mishkin P, Clark
J, Krueger G. Learning transferable visual models from natural language supervision. InInternational
conference on machine learning 2021 Jul 1 (pp. 8748-8763). PMLR.
117
Lu P, Mishra S, Xia T, Qiu L, Chang KW, Zhu SC, Tafjord O, Clark P, Kalyan A. Learn to
explain: Multimodal reasoning via thought chains for science question answering. Advances in Neural
Information Processing Systems. 2022 Dec 6;35:2507-21.
118
Sharma P, Ding N, Goodman S, Soricut R. Conceptual captions: A cleaned, hypernymed, image
alt-text dataset for automatic image captioning. InProceedings of the 56th Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers) 2018 Jul (pp. 2556-2565).
119
Zhao H, Yang M, Bai X, Liu H. A Survey on Multimodal Aspect-Based Sentiment Analysis. IEEE
Access. 2024 Jan 16.
120
Cai Y, Cai H, Wan X. Multi-modal sarcasm detection in twitter with hierarchical fusion model.
InProceedings of the 57th annual meeting of the association for computational linguistics 2019 Jul
(pp. 2506-2515).
121
Niu T, Zhu S, Pang L, El Saddik A. Sentiment analysis on multi-view social data. InMultiMe-
dia Modeling: 22nd International Conference, MMM 2016, Miami, FL, USA, January 4-6, 2016,
Proceedings, Part II 22 2016 (pp. 15-27). Springer International Publishing.
122
Poria S, Hazarika D, Majumder N, Naik G, Cambria E, Mihalcea R. Meld: A multimodal multi-
party dataset for emotion recognition in conversations. arXiv preprint arXiv:1810.02508. 2018 Oct
5.
123
Ramamoorthy S, Gunti N, Mishra S, Suryavardan S, Reganti A, Patwa P, DaS A, Chakraborty T,
Sheth A, Ekbal A, Ahuja C. Memotion 2: Dataset on sentiment and emotion analysis of memes.
InProceedings of De-Factify: Workshop on Multimodal Fact Checking and Hate Speech Detection,
CEUR 2022.
124
Castro S, Hazarika D, P´erez-Rosas V, Zimmermann R, Mihalcea R, Poria S. Towards multimodal
sarcasm detection (an obviously perfect paper). arXiv preprint arXiv:1906.01815. 2019 Jun 5.

--- Page 35 ---

Author Hao YANG, et al.
35
125
Zadeh A, Cao YS, Hessner S, Liang PP, Poria S, Morency LP. CMU-MOSEAS: A multimodal
language dataset for Spanish, Portuguese, German and French. InProceedings of the Conference on
Empirical Methods in Natural Language Processing. Conference on Empirical Methods in Natural
Language Processing 2020 Nov (Vol. 2020, p. 1801). NIH Public Access.
126
Busso C, Bulut M, Lee CC, Kazemzadeh A, Mower E, Kim S, Chang JN, Lee S, Narayanan SS.
IEMOCAP: Interactive emotional dyadic motion capture database. Language resources and evalua-
tion. 2008 Dec;42:335-59.
127
Yang X, Feng S, Wang D, Zhang Y. Image-text multimodal emotion classification via multi-view
attentional network. IEEE Transactions on Multimedia. 2020 Nov 2;23:4014-26.
128
Cai Y, Cai H, Wan X. Multi-modal sarcasm detection in twitter with hierarchical fusion model.
InProceedings of the 57th annual meeting of the association for computational linguistics 2019 Jul
(pp. 2506-2515).
129
M. Thelwall, K. Buckley, G. Paltoglou, D. Cai, and A. Kappas, ”Sentiment strength detection in
short informal text,” Journal of the American Society for Information Science and Technology, vol.
61, pp. 2544-2558, 2010.
130
D. Borth, R. Ji, T. Chen, T. Breuel, and S.-F. Chang, ”Large-scale visual sentiment ontology and
detectors using adjective noun pairs,” in Proceedings of the 21st ACM international conference on
Multimedia, 2013, pp. 223-232.
131
M. Wang, D. Cao, L. Li, S. Li, and R. Ji, ”Microblog sentiment analysis based on cross-media
bag-of-words model,” in Proceedings of international conference on internet multimedia computing
and service, 2014, p. 76.
132
G. Cai and B. Xia, ”Convolutional Neural Networks for Multimedia Sentiment Analysis,” in National
CCF Conference on Natural Language Processing and Chinese Computing, 2015, pp. 159-167.
133
Y. Yu, H. Lin, J. Meng, and Z. Zhao, ”Visual and Textual Sentiment Analysis of a Microblog Using
Deep Convolutional Neural Networks,” Algorithms, vol. 9, p. 41, 2016.
134
Xu N. Analyzing multimodal public sentiment based on hierarchical semantic attentional network.
In2017 IEEE international conference on intelligence and security informatics (ISI) 2017 Jul 22 (pp.
152-154). IEEE.
135
Xu N, Mao W. Multisentinet: A deep semantic network for multimodal sentiment analysis. InPro-
ceedings of the 2017 ACM on Conference on Information and Knowledge Management 2017 Nov 6
(pp. 2399-2402).
136
Xu N, Mao W, Chen G. A co-memory network for multimodal sentiment analysis. InThe 41st
international ACM SIGIR conference on research & development in information retrieval 2018 Jun
27 (pp. 929-932).
137
Yang X, Feng S, Zhang Y, Wang D. Multimodal sentiment detection based on multi-channel graph
neural networks. InProceedings of the 59th Annual Meeting of the Association for Computational
Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1:
Long Papers) 2021 Aug (pp. 328-339).
138
Li, Z., Xu, B., Zhu, C., & Zhao, T. (2022). CLMLF: A contrastive learning and multi-layer fusion
method for multimodal sentiment detection. arXiv preprint arXiv:2204.05515.
139
Tong
Zhu,
Leida
Li,
Jufeng
Yang,
Sicheng
Zhao,
Xiao
Xiao,
Multimodal
emotion
classification
with
multi-level
semantic
reasoning
network,
IEEE
Trans.
Multim.
(2022)
http://dx.doi.org/10.1109/TMM.2022.3214989, Early Access.
140
Jia A, He Y, Zhang Y, Uprety S, Song D, Lioma C. Beyond emotion: A multi-modal dataset for
human desire understanding. InProceedings of the 2022 Conference of the North American Chapter
of the Association for Computational Linguistics: Human Language Technologies 2022 Jul (pp. 1512-
1522).

--- Page 36 ---

Author Hao YANG, et al.
36
141
Wang W, Ding L, Shen L, Luo Y, Hu H, Tao D. WisdoM: Improving Multimodal Sentiment Analysis
by Fusing Contextual World Knowledge. arXiv preprint arXiv:2401.06659. 2024 Jan 12.
142
Ma D, Li S, Wu F, Xie X, Wang H. Exploring sequence-to-sequence learning in aspect term extrac-
tion. InProceedings of the 57th annual meeting of the association for computational linguistics 2019
Jul (pp. 3538-3547).
143
Chen Z, Qian T. Enhancing aspect term extraction with soft prototypes. InProceedings of the
2020 Conference on Empirical Methods in Natural Language Processing (EMNLP) 2020 Nov (pp.
2107-2117).
144
Karamanolakis G, Hsu D, Gravano L. Leveraging just a few keywords for fine-grained aspect detec-
tion through weakly supervised co-training. arXiv preprint arXiv:1909.00415. 2019 Sep 1.
145
Z. Wu, C. Zheng, Y. Cai, J. Chen, H.-f. Leung, Q. Li, Multimodal representation with embedded
visual guiding objects for named entity recognition in social media posts, in: Proceedings of the 28th
ACM International Conference on Multimedia, 2020, pp. 1038–1046.
146
Q. Zhang, J. Fu, X. Liu, X. Huang, Adaptive co-attention network for named entity recognition in
tweets, in: Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 32, 2018.
147
L. Sun, J. Wang, K. Zhang, Y. Su, F. Weng, RpBERT: a text-image relation propagation-based
BERT model for multimodal NER, in: Proceedings of the AAAI Conference on Artificial Intelligence,
Vol. 35, 2021, pp. 13860–13868.
148
Yu J, Jiang J, Yang L, Xia R. Improving multimodal named entity recognition via entity span
detection with unified multimodal transformer. Association for Computational Linguistics.
149
Moon S, Neves L, Carvalho V. Multimodal named entity recognition for short social media posts.
arXiv preprint arXiv:1802.07862. 2018 Feb 22.
150
Zhang D, Wei S, Li S, Wu H, Zhu Q, Zhou G. Multi-modal graph fusion for named entity recognition
with targeted visual guidance. InProceedings of the AAAI conference on artificial intelligence 2021
May 18 (Vol. 35, No. 16, pp. 14347-14355).
151
Peng T, Li Z, Wang P, Zhang L, Zhao H. A Novel Energy Based Model Mechanism for Multi-Modal
Aspect-Based Sentiment Analysis. InProceedings of the AAAI Conference on Artificial Intelligence
2024 Mar 24 (Vol. 38, No. 17, pp. 18869-18878).
152
Peng T, Li Z, Zhang L, Du B, Zhao H. FSUIE: A Novel Fuzzy Span Mechanism for Universal
Information Extraction. arXiv preprint arXiv:2306.14913. 2023 Jun 19.
153
Sundararaman MN, Ahmad Z, Ekbal A, Bhattacharyya P. Unsupervised aspect-level sentiment
controllable style transfer. InProceedings of the 1st Conference of the Asia-Pacific Chapter of the
Association for Computational Linguistics and the 10th International Joint Conference on Natural
Language Processing 2020 Dec (pp. 303-312).
154
Ji Y, Liu H, He B, Xiao X, Wu H, Yu Y. Diversified multiple instance learning for document-level
multi-aspect sentiment classification. InProceedings of the 2020 conference on empirical methods in
natural language processing (EMNLP) 2020 Nov (pp. 7012-7023).
155
Liang B, Yin R, Gui L, Du J, Xu R. Jointly learning aspect-focused and inter-aspect relations with
graph convolutional networks for aspect sentiment analysis. InProceedings of the 28th international
conference on computational linguistics 2020 Dec (pp. 150-161).
156
Wei J, Bosma M, Zhao VY, Guu K, Yu AW, Lester B, Du N, Dai AM, Le QV. Finetuned language
models are zero-shot learners. arXiv preprint arXiv:2109.01652. 2021 Sep 3.
157
Ouyang L, Wu J, Jiang X, Almeida D, Wainwright C, Mishkin P, Zhang C, Agarwal S, Slama K,
Ray A, Schulman J. Training language models to follow instructions with human feedback. Advances
in neural information processing systems. 2022 Dec 6;35:27730-44.

--- Page 37 ---

Author Hao YANG, et al.
37
158
Wang Y, Kordi Y, Mishra S, Liu A, Smith NA, Khashabi D, Hajishirzi H. Self-instruct: Aligning
language models with self-generated instructions. arXiv preprint arXiv:2212.10560. 2022 Dec 20.
159
Dai W, Li J, Li D, Tiong AM, Zhao J, Wang W, Li B, Fung PN, Hoi S. Instructblip: Towards
general-purpose vision-language models with instruction tuning. Advances in Neural Information
Processing Systems. 2024 Feb 13;36.
160
Feng J, Lin M, Shang L, Gao X. Autonomous Aspect-Image Instruction a2II: Q-Former Guided
Multimodal Sentiment Classification. InProceedings of the 2024 Joint International Conference on
Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024) 2024 May
(pp. 1996-2005).
161
Ju X, Zhang D, Xiao R, Li J, Li S, Zhang M, Zhou G. Joint multi-modal aspect-sentiment analysis
with auxiliary cross-modal relation detection. InProceedings of the 2021 conference on empirical
methods in natural language processing 2021 Nov (pp. 4395-4405).
162
Yang L, Na JC, Yu J. Cross-modal multitask transformer for end-to-end multimodal aspect-based
sentiment analysis. Information Processing & Management. 2022 Sep 1;59(5):103038.
163
Xiao L, Wu X, Xu J, Li W, Jin C, He L. Atlantis: Aesthetic-oriented multiple granularities fu-
sion network for joint multimodal aspect-based sentiment analysis. Information Fusion. 2024 Feb
15:102304.
164
Zhao F, Li C, Wu Z, Ouyang Y, Zhang J, Dai X. M2DF: Multi-grained Multi-curriculum Denoising
Framework for Multimodal Aspect-based Sentiment Analysis. arXiv preprint arXiv:2310.14605. 2023
Oct 23.
165
Zhou R, Guo W, Liu X, Yu S, Zhang Y, Yuan X. AoM: Detecting aspect-oriented information for
multimodal aspect-based sentiment analysis. arXiv preprint arXiv:2306.01004. 2023 May 31.
166
Liu Y, Zhou Y, Li Z, Zhang J, Shang Y, Zhang C, Hu S. RNG: Reducing Multi-level Noise
and Multi-grained Semantic Gap for Joint Multimodal Aspect-Sentiment Analysis. arXiv preprint
arXiv:2405.13059. 2024 May 20.
167
Li Y, Ding H, Lin Y, Feng X, Chang L. Multi-level textual-visual alignment and fusion network for
multimodal aspect-based sentiment analysis. Artificial Intelligence Review. 2024 Apr;57(4):1-26.
168
Yu Y, Zhang D, Li S. Unified multi-modal pre-training for few-shot sentiment analysis with prompt-
based learning. InProceedings of the 30th ACM International Conference on Multimedia 2022 Oct
10 (pp. 189-198).
169
Yu Y, Zhang D. Few-shot multi-modal sentiment analysis with prompt-based vision-aware language
modeling. In2022 IEEE International Conference on Multimedia and Expo (ICME) 2022 Jul 18 (pp.
1-6). IEEE.
170
Yang X, Feng S, Wang D, Qi S, Wu W, Zhang Y, Hong P, Poria S. Few-shot joint multimodal
aspect-sentiment analysis based on generative multimodal prompt. arXiv preprint arXiv:2305.10169.
2023 May 17.
171
Yang L, Wang Z, Li Z, Na JC, Yu J. An empirical study of Multimodal Entity-Based Sentiment
Analysis with ChatGPT: Improving in-context learning via entity-aware contrastive learning. Infor-
mation Processing & Management. 2024 Jul 1;61(4):103724.
172
Morency LP, Mihalcea R, Doshi P. Towards multimodal sentiment analysis: Harvesting opinions
from the web. InProceedings of the 13th international conference on multimodal interfaces 2011 Nov
14 (pp. 169-176).
173
Liu Y, Yuan Z, Mao H, Liang Z, Yang W, Qiu Y, Cheng T, Li X, Xu H, Gao K. Make acoustic and
visual cues matter: CH-SIMS v2. 0 dataset and AV-Mixup consistent module. InProceedings of the
2022 International Conference on Multimodal Interaction 2022 Nov 7 (pp. 247-258).

--- Page 38 ---

Author Hao YANG, et al.
38
174
Zhao J, Zhang T, Hu J, Liu Y, Jin Q, Wang X, Li H. M3ED: Multi-modal multi-scene multi-label
emotional dialogue database. arXiv preprint arXiv:2205.10237. 2022 May 9.
175
Lian Z, Sun H, Sun L, Chen K, Xu M, Wang K, Xu K, He Y, Li Y, Zhao J, Liu Y. Mer 2023:
Multi-label learning, modality robustness, and semi-supervised learning. InProceedings of the 31st
ACM International Conference on Multimedia 2023 Oct 26 (pp. 9610-9614).
176
Lian Z, Sun H, Sun L, Wen Z, Zhang S, Chen S, Gu H, Zhao J, Ma Z, Chen X, Yi J. MER 2024: Semi-
Supervised Learning, Noise Robustness, and Open-Vocabulary Multimodal Emotion Recognition.
arXiv preprint arXiv:2404.17113. 2024 Apr 26.
177
Lian Z, Sun L, Xu M, Sun H, Xu K, Wen Z, Chen S, Liu B, Tao J. Explainable multimodal emotion
reasoning. arXiv preprint arXiv:2306.15401. 2023 Jun 27.
178
Hasan MK, Rahman W, Zadeh A, Zhong J, Tanveer MI, Morency LP. UR-FUNNY: A multimodal
language dataset for understanding humor. arXiv preprint arXiv:1904.06618. 2019 Apr 14.
179
Wei X, Zhang T, Li Y, Zhang Y, Wu F. Multi-modality cross attention network for image and
sentence matching. InProceedings of the IEEE/CVF conference on computer vision and pattern
recognition 2020 (pp. 10941-10950).
180
Anderson P, He X, Buehler C, Teney D, Johnson M, Gould S, Zhang L. Bottom-up and top-down
attention for image captioning and visual question answering. InProceedings of the IEEE conference
on computer vision and pattern recognition 2018 (pp. 6077-6086).
181
Huang J, Pu Y, Zhou D, Shi H, Zhao Z, Xu D, Cao J. Multimodal Sentiment Analysis Based on 3D
Stereoscopic Attention. InICASSP 2024-2024 IEEE International Conference on Acoustics, Speech
and Signal Processing (ICASSP) 2024 Apr 14 (pp. 11151-11155). IEEE.
182
Mai S, Zeng Y, Zheng S, Hu H. Hybrid contrastive learning of tri-modal representation for multi-
modal sentiment analysis. IEEE Transactions on Affective Computing. 2022 May 3.
183
Lin R, Hu H. Multimodal contrastive learning via uni-Modal coding and cross-Modal prediction for
multimodal sentiment analysis. arXiv preprint arXiv:2210.14556. 2022 Oct 26.
184
Sun Z, Sarma P, Sethares W, Liang Y. Learning relationships between text, audio, and video via
deep canonical correlation for multimodal language analysis. InProceedings of the AAAI Conference
on Artificial Intelligence 2020 Apr 3 (Vol. 34, No. 05, pp. 8992-8999).
185
Hazarika D, Zimmermann R, Poria S. Misa: Modality-invariant and-specific representations for mul-
timodal sentiment analysis. InProceedings of the 28th ACM international conference on multimedia
2020 Oct 12 (pp. 1122-1131).
186
Mai S, Hu H, Xing S. Modality to modality translation: An adversarial representation learning
and graph fusion network for multimodal fusion. InProceedings of the AAAI Conference on Artificial
Intelligence 2020 Apr 3 (Vol. 34, No. 01, pp. 164-172).
187
Liu Z, Shen Y, Lakshminarasimhan VB, Liang PP, Zadeh A, Morency LP. Efficient low-rank mul-
timodal fusion with modality-specific factors. arXiv preprint arXiv:1806.00064. 2018 May 31.
188
Mai S, Hu H, Xing S. Divide, conquer and combine: Hierarchical feature fusion network with local
and global perspectives for multimodal affective computing. InProceedings of the 57th annual meeting
of the association for computational linguistics 2019 Jul (pp. 481-492).
189
Chen M, Wang S, Liang PP, Baltruˇsaitis T, Zadeh A, Morency LP. Multimodal sentiment analysis
with word-level fusion and reinforcement learning. InProceedings of the 19th ACM international
conference on multimodal interaction 2017 Nov 3 (pp. 163-171).
190
Zadeh A, Liang PP, Mazumder N, Poria S, Cambria E, Morency LP. Memory fusion network for
multi-view sequential learning. InProceedings of the AAAI conference on artificial intelligence 2018
Apr 27 (Vol. 32, No. 1).

--- Page 39 ---

Author Hao YANG, et al.
39
191
Rahman W, Hasan MK, Lee S, Zadeh A, Mao C, Morency LP, Hoque E. Integrating multimodal
information in large pretrained transformers. InProceedings of the conference. Association for Com-
putational Linguistics. Meeting 2020 Jul (Vol. 2020, p. 2359). NIH Public Access.
192
Dai W, Cahyawijaya S, Liu Z, Fung P. Multimodal end-to-end sparse model for emotion recognition.
arXiv preprint arXiv:2103.09666. 2021 Mar 17.
193
Morency LP, Mihalcea R, Doshi P. Towards multimodal sentiment analysis: Harvesting opinions
from the web. InProceedings of the 13th international conference on multimodal interfaces 2011 Nov
14 (pp. 169-176).
194
Schifanella R, De Juan P, Tetreault J, Cao L. Detecting sarcasm in multimodal social platforms.
InProceedings of the 24th ACM international conference on Multimedia 2016 Oct 1 (pp. 1136-1145).
195
H. Pan, Z. Lin, P. Fu, Y. Qi, W. Wang, Modeling intra and inter-modality incongruity for multi-
modal sarcasm detection, in: Findings of the Association for Computational Linguistics, EMNLP
2020, 2020, pp. 1383–1392.
196
X. Wang, X. Sun, T. Yang, H. Wang, Building a bridge: A method for image-text sarcasm detection
without pretraining on image-text data, in: Proceedings of the First International Workshop on
Natural Language Processing beyond Text, 2020, pp. 19–29.
197
D. Tom´as, R. Ortega-Bueno, G. Zhang, P. Rosso, R. Schifanella, Transformer-based models for
multimodal irony detection, J. Ambient Intell. Humaniz. Comput. (2022) 1–12.
198
B. Liang, C. Lou, X. Li, L. Gui, M. Yang, R. Xu, Multi-modal sarcasm detection with interactive
in-modal and cross-modal graphs, in: Proceedings of the 29th ACM International Conference on
Multimedia, 2021, pp. 4707–4715.
199
B. Liang, C. Lou, X. Li, M. Yang, L. Gui, Y. He, W. Pei, R. Xu, Multi-modal sarcasm detection
via cross-modal graph convolutional network, in: Proceedings of the 60th Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers), 2022, pp. 1767–1777.
200
Yue T, Mao R, Wang H, Hu Z, Cambria E. KnowleNet: Knowledge fusion network for multimodal
sarcasm detection. Information Fusion. 2023 Dec 1;100:101921.
201
Speer R, Chin J, Havasi C. Conceptnet 5.5: An open multilingual graph of general knowledge.
InProceedings of the AAAI conference on artificial intelligence 2017 Feb 12 (Vol. 31, No. 1).
202
H. Liu, B. Yang, Z. Yu, A multi-view interactive approach for multimodal sarcasm detection in
social internet of things with knowledge enhancement, Appl. Sci. 14 (5) (2024) 2146.
203
H. Fu, H. Liu, H. Wang, L. Xu, J. Lin, D. Jiang, Multi-modal sarcasm detection with sentiment
word embedding, Electronics 13 (5) (2024) 855.
204
Yi G, Fan C, Zhu K, Lv Z, Liang S, Wen Z, Pei G, Li T, Tao J. Vlp2msa: expanding vision-language
pre-training to multimodal sentiment analysis. Knowledge-Based Systems. 2024 Jan 11;283:111136.
205
Qin L, Huang S, Chen Q, Cai C, Zhang Y, Liang B, Che W, Xu R. MMSD2. 0: Towards a Reliable
Multi-modal Sarcasm Detection System. arXiv preprint arXiv:2307.07135. 2023 Jul 14.
206
Leveraging
Generative
Large
Language
Models
with
Visual
Instruction
and
Demonstration
Retrieval
for
Multimodal
Sarcasm
Detection.
openreview
Dec.2023.
https://openreview.net/forum?id= 98UHlfKejb
207
Lin H, Chen Z, Luo Z, Cheng M, Ma J, Chen G. CofiPara: A Coarse-to-fine Paradigm for Multimodal
Sarcasm Target Identification with Large Multimodal Models. arXiv preprint arXiv:2405.00390. 2024
May 1.
208
Qin L, Chen Q, Feng X, Wu Y, Zhang Y, Li Y, Li M, Che W, Yu PS. Large Language Models Meet
NLP: A Survey. arXiv preprint arXiv:2405.12819. 2024 May 21.

--- Page 40 ---

Author Hao YANG, et al.
40
209
Houlsby N, Giurgiu A, Jastrzebski S, Morrone B, De Laroussilhe Q, Gesmundo A, Attariyan M,
Gelly S. Parameter-efficient transfer learning for NLP. InInternational conference on machine learning
2019 May 24 (pp. 2790-2799). PMLR.
210
Hu EJ, Shen Y, Wallis P, Allen-Zhu Z, Li Y, Wang S, Wang L, Chen W. Lora: Low-rank adaptation
of large language models. arXiv preprint arXiv:2106.09685. 2021 Jun 17.
211
Li XL, Liang P. Prefix-tuning:
Optimizing continuous prompts for generation. arXiv preprint
arXiv:2101.00190. 2021 Jan 1.
212
Dettmers T, Pagnoni A, Holtzman A, Zettlemoyer L. Qlora: Efficient finetuning of quantized llms.
Advances in Neural Information Processing Systems. 2024 Feb 13;36.
213
Zhang Z, Peng L, Pang T, Han J, Zhao H, Schuller BW. Refashioning emotion recognition modelling:
The advent of generalised large models. IEEE Transactions on Computational Social Systems. 2024
May 30.
214
Peng L, Zhang Z, Pang T, Han J, Zhao H, Chen H, Schuller BW. Customising General Large Lan-
guage Models for Specialised Emotion Recognition Tasks. InICASSP 2024-2024 IEEE International
Conference on Acoustics, Speech and Signal Processing (ICASSP) 2024 Apr 14 (pp. 11326-11330).
IEEE.
215
Geetha AV, Mala T, Priyanka D, Uma E. Multimodal Emotion Recognition with deep learning:
advancements, challenges, and future directions. Information Fusion. 2024 May 1;105:102218.
216
LeCun Y, Chopra S, Hadsell R, Ranzato M, Huang F. A tutorial on energy-based learning. Predicting
structured data. 2006 Aug 19;1(0).
217
Yang X, Wu W, Feng S, Wang M, Wang D, Li Y, Sun Q, Zhang Y, Fu X, Poria S. MM-InstructEval:
Zero-Shot Evaluation of (Multimodal) Large Language Models on Multimodal Reasoning Tasks.
arXiv preprint arXiv:2405.07229. 2024 May 12.

```
