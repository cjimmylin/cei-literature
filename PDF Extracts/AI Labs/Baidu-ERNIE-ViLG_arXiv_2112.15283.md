---
title: "ERNIE ViLG arXiv 2112.15283"
source_pdf: "AI Labs/Baidu/ERNIE 4.5/ERNIE-ViLG_arXiv_2112.15283.pdf"
company: "Baidu"
pages: 15
extracted_at: "2026-01-31T17:32:29.966502"
type: "ai_lab_paper"
---

# ERNIE ViLG arXiv 2112.15283

**Company/Lab:** Baidu
**Model:** ERNIE 4.5
**Source PDF:** AI Labs/Baidu/ERNIE 4.5/ERNIE-ViLG_arXiv_2112.15283.pdf
**Total Pages:** 15

---

## Content

```
--- Page 1 ---

ERNIE-VILG: UNIFIED GENERATIVE PRE-TRAINING FOR
BIDIRECTIONAL VISION-LANGUAGE GENERATION
Han Zhang
Weichong Yin
Yewei Fang
Lanxin Li
Boqiang Duan
Zhihua Wu
Yu Sun
Hao Tian
Hua Wu
Haifeng Wang
Baidu Inc.
{zhanghan17, yinweichong, sunyu02}@baidu.com
ABSTRACT
Conventional methods for the image-text generation tasks mainly tackle the naturally bidirectional
generation tasks separately, focusing on designing task-speciﬁc frameworks to improve the quality
and ﬁdelity of the generated samples. Recently, Vision-Language Pre-training models have greatly
improved the performance of the image-to-text generation tasks, but large-scale pre-training models
for text-to-image synthesis task are still under-developed. In this paper, we propose ERNIE-ViLG, a
uniﬁed generative pre-training framework for bidirectional image-text generation with transformer
model. Based on the image quantization models, we formulate both image generation and text
generation as autoregressive generative tasks conditioned on the text/image input. The bidirectional
image-text generative modeling eases the semantic alignments across vision and language. For the
text-to-image generation process, we further propose an end-to-end training method to jointly learn
the visual sequence generator and the image reconstructor. To explore the landscape of large-scale
pre-training for bidirectional text-image generation, we train a 10-billion parameter ERNIE-ViLG
model on a large-scale dataset of 145 million (Chinese) image-text pairs which achieves state-of-the-
art performance for both text-to-image and image-to-text tasks, obtaining an FID of 7.9 on MS-COCO
for text-to-image synthesis and best results on COCO-CN and AIC-ICC for image captioning.
1
Introduction
“What I cannot create, I do not understand.”
Richard Feynman
Cross-modal generation, aiming at mapping or translating one modality to another, requires the model to fully
"understand" the source modality and to faithfully "create" (generate) the target modality with high semantic consistency
with the source [1]. As concerned with a big part of multimodal machine learning researches, the cross-modal generation
task has attracted dramatic attentions, for audio-linguistic [2, 3], visual-linguistic [4, 5, 6, 7, 8, 9], audio-visual [10, 11]
modalities. In this paper, we focus on the visual-linguistic generation tasks which mainly include image captioning
(describing the visual content of an image in natural language) and text-to-image synthesis (creating an image that
keeps semantic consistent with a textual description). As the intersection of computer vision and natural language
processing, the Vision-Language generation tasks attract much interest from both NLP and CV communities and have
achieved great progresses over the past several years.
Naturally, the text-image generation tasks are bidirectional and a reasonable model should have the capability of both
image captioning and text-to-image synthesis. However, due to the distinct generative architectures for language
generation and image generation, methods tackle the two tasks have developed separately. The conventional methods
for image captioning mainly adopt the encoder-decoder architecture [4] where the text is generated in a sequence
generation manner. The image is ﬁrst encoded into one or multiple vectors and then a decoder (e.g., LSTM) is utilized
arXiv:2112.15283v1  [cs.CV]  31 Dec 2021

--- Page 2 ---

to generate language tokens based on the encoder results. Recently, the transformer-based Vision-Language Pre-trained
models [7, 12] have signiﬁcantly improved the performance of image captioning beneﬁting from pre-training on
large-scale image-text aligned datasets. On the other hand, the dominant text-to-image synthesis methods are the
Generative Adversarial Networks (GANs) [13] variants where ConvNets are utilized as the basic architecture of the
generator. While various methods have been proposed to improve the quality and resolution of generated images, such
as StackGAN [14], XMC-GAN [8], it remains difﬁcult to generate images of complex scenes with multiple objects.
Inspired by the autoregressive models for the images [15, 16], recent works [9, 17] have proposed to formulate the
text-to-image synthesis as a sequence-to-sequence problem where the image tokens are learned through discrete VAE
[18, 9]. They model the text tokens and image tokens in the same transformer and have shown great improvement for
the image quality and the capability to construct complex scenes. And the text-to-image generation process usually
adopts a two-stage pipeline consisting of a generator (to generate the image tokens) and a reconstuctor (to build the
image from the generated image tokens), which are trained separately.
More recently, researchers have attempted to unify the bidirectional image-text generation tasks in a single model. Cho
et al. [19] attempt to enhance the existing Vision-Language Pre-training models with the capability of text-to-image
generation, utilizing image discrete tokens generated by K-means clustering of pre-trained image features and generating
the image sequence in a non-autoregressive manner. Based on this approach, Huang et al. [20] formulate both the tasks
as sequence generation tasks and further propose a sequence-level training task to improve the performance. Although
they unify the two tasks in one single transformer, they employ the non-autoregressive sampling to generate images
which enables a fast inference speed but leads to suboptimal performance compared to the autoregressive generative
models due to the removal of explicitly modeling of dependencies among the target tokens.
In the paper, we propose ERNIE-ViLG, a uniﬁed pre-training method for the bidirectional image-text generation with
transformer model. Based on image quantization techniques [18, 9, 21], both the image-to-text and text-to-image
generation are tackled in autoregressive manners within the same transformer. And we further propose an end-to-
end pre-training method for text-to-image synthesis which makes the traditionally separate two-stage generator and
reconstructor training jointly. To explore the landscape of large-scale pre-training for bidirectional text-image generation,
we pre-train a 10-billion parameter model on a large-scale dataset of 145 million high-quality Chinese image-text pairs.
It has shown superior performance for both text-to-image synthesis and image captioning tasks. Concretely, it achieves
the best FID on MS-COCO for text-to-image synthesis and obtains state-of-the-art performance on two Chinese image
captioning datasets. Moreover, we evaluate ERNIE-ViLG on a challenging generative Visual Question Answering
(VQA) task, and the excellent performance shows that our bidirectional generative model has captured the semantic
alignments across vision-language modalities and can also be transferred to tackle complex generative tasks besides
image-text generation.
Overall, our contributions include:
• We propose ERNIE-ViLG, a uniﬁed generative pre-training method for bidirectional image-text generation
tasks, where both the image and text generation are formulated as autoregressive generative tasks. And we
propose the ﬁrst end-to-end training method for text-to-image synthesis based on image discrete representation,
which enhances both the generator and reconstructor and outperforms the traditional two-stage approach.
• We train a 10-billion parameter ERNIE-ViLG model and obtain superior performance for both text-to-image
and image-to-text generation tasks, setting new SOTA results for text-to-image synthesis on MS-COCO and
obtaining SOTA results for image captioning on two popular Chinese datasets.
• Superior performance on the generative VQA task shows that our bidirectional generative model captures the
complex semantic alignments between the vision and the language modalities.
2
Related Work
2.1
Vision-Language Pre-training
Vision-Language Pre-training (VLP) models [22, 7, 23, 24, 25, 26, 27] have greatly improved the performance of
various Vision-Language tasks, such as VQA and cross-modal retrieval. Utilizing transformer architecture (two-stream
or single-stream) to fuse the visual modality and the linguistic modality, they propose various pre-training tasks, from
the conventional masked language modeling (MLM), masked region prediction (MRP), image-text matching (ITM) to
word-region alignment [23], scene graph prediction [24], multimodal conditional text generation [28], Preﬁx-LM [29],
etc. The pre-training datasets are also a big concern of VLP researches where early works utilize million-scale noisy
image-text datasets such as Conceptual Captions [30] and human labeled datasets such as COCO Captions [31] and
recent works scale up the pre-training with hundreds of millions and nearly billion-scale noisy image-text dataset [29].
2

--- Page 3 ---

While most of VLP methods focus on pre-training for the vision-language understanding tasks, some works have
noticed the importance of pre-training for improving the performance of cross-modal generation tasks, mainly image
captioning task. Zhou et al. [7] propose the ﬁrst uniﬁed model to improve the performance of both understanding and
generation tasks, where the bidirectional and sequence-to-sequence pre-training tasks utilize different attention masks.
Wang et al. [29] propose preﬁx-LM pre-training task, similar to image captioning, solely exploiting language modeling
objective. Hu et al. [32] study the scaling behavior of pre-training from both the data and model perspective for image
captioning.
While the image-to-text generation task has been advanced a lot due to the pre-training on large-scale image-text
datasets, the beneﬁt of pre-training for text-to-image synthesis task has not been fully explored. Cho et al. [19] propose
to enhance the VLP models with image generation capability based on discretized visual representation and ﬁne-tuned
for text-to-image synthesis. Wu et al. [33] attempt to construct a uniﬁed encoder-decoder pre-trained framework aiming
at both image and video synthesis tasks.
ERNIE-ViLG focuses on the pre-training for both the image-to-text and text-to-image generation tasks and simplifying
the pre-training objectives to the autoregressive sequence-to-sequence generation tasks for both image and text.
2.2
Vision-Language Generation
Image-to-Text Generation
The typical methods for image captioning adopt the encoder-decoder architecture for-
mulating the image-to-text problem as text sequence generation task with the context of the image. Vinyals et al. [4]
propose a simple LSTM-based architecture where the image is encoded into a single vector and used as the initial
hidden state of a single-layer LSTM. Utilizing the attention-mechanism, various methods [34, 6, 35] have been proposed
to improve the correlation between the visual image and the generated text sequence where the image is encoded
into multiple features and used via cross-modal attention to guide the generation process. Recently, researchers have
explored the potential of transformer-based model for image captioning [30, 36, 7]. Zhou et al. [7] propose to use a
uniﬁed transformer architecture to fuse the visual and textual modalities, for both encoding and decoding. Following
this, Li et al. [12] propose to include objects tags which are extracted from the image using an object detector into the
input for augmenting the semantic alignment between the image and text.
Text-to-Image Synthesis
Since the arise of generating images using Generative Adversarial Networks (GANs) [13],
the GANs based methods have been most popular ones for text-to-image synthesis. Reed et al. [5] ﬁrst extend the
conditional GANs to generate images from language descriptions. After that, Zhang et al. [14] propose StackGAN to
generate high-resolution images in a multi-stage manner. Zhu et al. [37] propose to use dynamic memory networks
to reﬁne image contents. Zhang et al. [8] propose to incorporate contrastive learning to improve the ﬁdelity of the
generated images to the textual input. Recently, inspired by the autoregressive generative models for pixel-by-pixel
image generation [16], the transformer-based methods [9, 17] have shown promising results for text-to-image synthesis.
Based on the discrete image tokens learned by various discrete VAE [18, 21], they try to model the image tokens and
text tokens in a single transformer framework, following a unidirectional manner for both the text input and the image
target.
3
Approach
In this section, we will introduce our uniﬁed generative pre-training framework for bidirectional Vision-Language
generation and the end-to-end method for text-to-image synthesis training. Also, we present the details of the collection
of the large-scale image-text dataset and the distributed training strategies for pre-training the 10-billion parameter
model.
3.1
A Uniﬁed Generative Framework for Bidirectional Image-text Generation
As shown in Figure 1, ERNIE-ViLG adopts a uniﬁed framework for the bidirectional image-text generation. The
image is represented as a sequence of discrete representation by vector quantization variational autoencoder (VQVAE)
[18]. The image discrete sequence is used as the input(output) of a parameter-sharing transformer for autoregressive
image-to-text (text-to-image) generation. Speciﬁcally, for the image-to-text generation, the transformer takes the image
discrete sequence as input to generate the corresponding textual sequence. Conversely, for the text-to-image synthesis,
the text is inputted to the transformer for generating the corresponding visual discrete sequence, and then the image
discrete sequence is used for reconstructing the image. Besides the traditional two-stage pipeline approach, we further
propose an end-to-end training method of jointly training the modules for discrete representation sequence generation
and image reconstruction to strengthen the ability of text-to-image synthesis.
3

--- Page 4 ---

Figure 1: The uniﬁed model architecture of ERNIE-ViLG for bidirectional image-text generation.
3.1.1
Image Discrete Representation
Discrete representation has achieved signiﬁcant improvements for image generation tasks recently, because it can be
better adapted to autoregressive modeling. VQVAE [18] proposes to represent images as latent discrete sequences using
vector quantization. It has stronger semantic representation ability than pixel clustering. VQVAE encodes the original
image x ∈RH×W ×3 by encoder E and quantizes it to z with codebook C. z is the discrete sequence with h × w indices,
and used to reconstruct x via decoder G and C. The loss function during training is shown in Equation 1-2.
LV QV AE =∥x −ˆx ∥2 + ∥sg[zemb] −E(x) ∥2
2 + ∥sg[E(x)] −zemb ∥2
2
(1)
ˆx = G(zemb) = G(C(z)) = G(q(E(x)))
(2)
The overall loss function contains two parts. The ﬁrst term of LV QV AE is reconstruction loss. The last two terms aim
to make E(x) (the encoder outputs) and zemb (the embeddings after the lookup of discrete sequence from codebook)
close to each other. sg[·] denotes the stop-gradient operation, and q[·] denotes the vector quantization. x and ˆx are
the original and reconstructed images. The discrete sequence z servers as the input (or output) of the bidirectional
generative model, and its length n is h × w.
3.1.2
Bidirectional Generative Model
For the generative model, we use a multi-layer transformer encoder for both image-to-text and text-to-image generation
tasks. Different from the decode-only [9, 17] or separate encoder-decoder [33] architectures, the encoder and decoder
of ERNIE-ViLG share parameters and use speciﬁc self-attention masks to control the contexts like UniLM [38] and
ERNIE-GEN [39], where the source tokens are allowed to attend all the source tokens and the target tokens are allowed
to attend the source tokens and the target tokens lie left to them. The bidirectional generation pre-training tasks are
modeled exact in the same model where we consider sharing of model space helps establish better semantic alignments
across vision and language modalities.
The visual tokens {z1, ..., zn} discretized from the image using VQVAE encoder and the textual tokens {t1, ..., tm}
tokenized from the text using WordPiece tokenizer are concatenated and fed into the transformer model. Therefore,
during training, the model takes the input stream of [t1, ..., tm, z1, ..., zn] for text-to-image generation task to predict
the image tokens autoregressively and [z1, ..., zn, t1, ..., tm] for image-to-text generation task. We use the following
multi-task loss for learning the image-text bidirectional generation tasks.
L = Ltxt2img + Limg2txt
(3)
Ltxt2img =
n
X
k=1
−log P(zk|t1, ..., tm, z1, ..., zk−1)
(4)
Limg2txt =
m
X
k=1
−log P(tk|z1, ...zn, t1, ..., tk−1)
(5)
4

--- Page 5 ---

Note that the length n of visual sequence z is often large (usually larger than 1024) to reduce the information loss of the
image, which causes a relatively high computation cost and memory consumption for the transformer model during
training and inference. As shown in Figure 2, we utilize a similar sparse attention mechanism as in [9]. Concretely,
we adopt row attention (i mod 4 != 2 ), column attention (i mod 4 = 2) and convolutional attention (the last layer)
for the i-th transformer layer. We implement the row attention and column attention as block-wise attention while
training. Several primary experiments verify that this sparse attention implementation can roughly increase the speed
by 25% and save 50% of GPU memory during training while keeping the convergence of loss consistent with dense
attention. And the improvement for predicting is much more signiﬁcant. While the sparse attentions in [9] are designed
for unidirectional modeling, we adapt them to the bidirectional modeling manner of the visual input tokens for the
image-to-text generation as shown in Figure 2(b).
IMG + img_tokens
row mask
col mask
conv mask
CLS + txt_tokens + SEP
CLS + txt_tokens + SEP
CLS + txt_tokens + SEP
IMG + img_tokens
IMG + img_tokens
(a) Sparse attention for text-to-image generation
IMG + img_tokens
CLS + txt_tokens + SEP
row mask
col mask
conv mask
CLS + txt_tokens + SEP
CLS + txt_tokens + SEP
IMG + img_tokens
IMG + img_tokens
(b) Sparse attention for image-to-text generation
Figure 2: Sparse attention for bidirectional text-image generation. For text-to-image generation, text tokens are visible
to each other and the image attention pattern is as same as DALL-E. But for image-to-text generation, the attention
pattern of image tokens in the same row, column or convolutional kernel is bidirectional rather than unidirectional. This
is a hypothetical version of our transformer with a maximum text length of 6 tokens, image length of 16 tokens (4×4),
and convolutional kernel size of 3×3. The actual kernel size of our model is 11×11 following DALL-E.
5

--- Page 6 ---

3.1.3
Text-to-Image Synthesis
Text-to-image synthesis based on image discrete sequence is usually tackled in a two-stage pipeline: discrete represen-
tation sequence generation and image reconstruction. As the red path in Figure 1, the generated discrete sequence is
looked up in the codebook to obtain a 3D tensor zemb ∈Rh×w×d. Then zemb is sent to the reconstructed decoder to be
restored into an image. The generator and the reconstructor are trained independently.
Besides the traditional two-stage pipeline mode, in the framework of ERNIE-ViLG, the text-to-image synthesis can also
use our newly proposed end-to-end training method as the green path in Figure 1. Hidden embeddings of image tokens
outputted by the last transformer layer are mapped to zemb nonlinearly. Gradients could be propagated backward from
the reconstructor to the generator since the non-derivable ID mapping operation is avoided. Therefore, the end-to-end
training can be carried out.
This method is designed to:
• provide more contextual features for the reconstructor. Compared with context-independent embedding in
codebooks, hidden embedding is encoded by a deep model and contains more image semantics. It also has
perception of the textual information through the attention interaction.
• enhance the generator with the reconstruction task. The hidden embedding receives both abstract and original
supervised signals from generation and reconstruction. It helps the generator learn better about image
representation.
Our experiments show that the end-to-end training can improve both generator and reconstructor compared with the
two-stage pipeline. Detailed experimental results are presented in Section 5.
3.1.4
Image-to-Text Generation
For the image-to-text generation task, the image is ﬁrst discretized into visual tokens using the encoder and the codebook
of the VQVAE. The image tokens are then fed into the Transformer to generate the text tokens autoregressively. In our
current implementation, the quantization modules are pre-trained and ﬁxed during the image-to-text generation training
task while they could also be updated jointly with the generative model, and we will explore it for the future work.
3.2
Large-scale Pre-training of ERNIE-ViLG
To explore the landscape of large-scale pre-training for bidirectional text-image generation, we train a 10-billion
parameter ERNIE-ViLG model, a 48-layer transformer encoder for both image-to-text and text-to-image generation.
The core issues of large-scale pre-training include collection of training data and distributed parallel training.
3.2.1
Large-scale Image-Text Dataset Collection
To pre-train a generative model with general capabilities of bidirectional text-image generation, from basic entities
to complex scenes, we build a large-scale image-text dataset consisting of over 145 million high-quality Chinese
image-text pairs. The sources of our dataset are listed as follows:
• Chinese Webpages. We crawl 800 million raw Chinese alt-text descriptions paired with images from various
Chinese webpages, conduct several steps of ﬁltering and totally harvest 70 million text-image pairs. The
ﬁltering rules mainly include: (1) Text-length: the number of words in alt-text is less than 15. (2) Text-content:
the alt-text must contain at least one noun and contain no special characters. (3) Image-text similarity: the
similarity score of between the alt-text and image (calculated by an in-house text-image matching model with
the score range from 0.0 to 1.0) is greater than 0.5.
• Image Search Engine. We collect roughly 60 million query texts and corresponding user-clicked images
from our internal image search engine. There is often a strong correlation between the query and user-clicked
images.
• Public image-text Dataset. We collect a total of 15 million text-image pairs from two public datasets, CC
[30] and CC12M [40]. The captions in these datasets are translated to Chinese through Baidu Translate API.
3.2.2
Distributed Training Strategies for Large-Scale Generative Models
The 10-billion parameter ERNIE-ViLG is implemented based on PaddlePaddle platform [41]. Serious challenges need
to be addressed to train such a large-scale model, such as limited device memory and computation efﬁciency. Also, it is
6

--- Page 7 ---

Figure 3: Hybrid parallelism of data parallelism and sharding in PaddlePaddle. We organize the cluster in two
dimensions: the data is sharded in column dimension while the model states (optimizer states, gradients, and parameters)
are sharded among row dimensions. All communication needed by sharding is conﬁned to the same machine.
rather demanding to ﬁt a 10B generative model into a single GPU, and it becomes more challenging considering our
bidirectional model’s structure which doubles the memory consumption of activations and gradients.
As shown in Figure 3, we adopt Group Sharded data parallelism techniques [42, 43] to eliminate memory redundancies
by partitioning the optimizer states, gradients, and parameters across multiple devices. In addition, activation recomputa-
tion [44] and mixed-precision [45] are applied to reduce the GPU memory footprint and increase throughput. Moreover,
Optimizer-ofﬂoad [46] is introduced to swap the sharded optimizer states and master parameters to the CPU which
largely reduces the GPU memory footprint. Furthermore, we combine Optimizer-ofﬂoad with Gradient Accumulation
to bring down the communication frequency between CPU and GPU, delivering a higher computation efﬁciency.
4
Experiments
We pre-train a 10-billion parameter ERNIE-ViLG model and verify its generation ability. We conduct experiments
on the conventional bidirectional image-text tasks: text-to-image synthesis and image captioning. Besides, in order
to further verify the cross-modal understanding ability of our model, we transfer ERNIE-ViLG for the challenging
generative VQA task to evaluate the alignments our model has captured across vision and language modalities.
4.1
Settings
We use VQGAN [21], an enhanced variant of VQVAE, as our "image tokenizer". By adding adversarial training
and perceptual loss, VQGAN enables clearer and more realistic image restoration from discrete representations. We
adopt the model of VQGAN with f = 8 and vocab size = 8192, where f denotes the reduction factor in the side-length.
We pre-process the original image to 256 * 256 through center crop, and thus the length of the visual discrete token
sequence n is 1024 (h × w, h = w = 32).
For the generator, we use a multi-layer transformer encoder for both image-to-text and text-to-image generation tasks,
which consists of 48 transformer layers with 4096 hidden units and 64 attention heads and totally has 10 billion
parameters. Considering the instability of the training of GAN-based models, we choose the two-stage text-to-image
synthesis mode when training this model and use the decoder of VQGAN as the image reconstructor directly.
4.2
Text-to-Image Synthesis
To generate images given the text, we follow the same sampling strategy as in [9] and the generated images are re-ranked
with an in-house contrastive learning-based image-text matching model. We carry out the automatic evaluations of
7

--- Page 8 ---

ERNIE-ViLG on a commonly used text-to-image synthesis dataset in both zero-shot and ﬁne-tuning settings. Moreover,
we conduct a human evaluation campaign to directly assess the quality of the images generated.
Table 1: Comparison of FID with previous text-to-image synthesis models on MS-COCO. Results of other models
are directly taken from their papers. "Pre-trained" means the model is obtained by vision-language pre-training,
"Supervised" illustrates the model is trained in a fully-supervised manner.
Model
FID ↓
Supervised (ﬁne-tuned)
AttnGAN [47]
35.5
DM-GAN [37]
32.6
DF-GAN [48]
21.4
XMC-GAN [8]
9.3
X-LXMERT [19]
37.4
Huang et al. [20]
29.9
NÜWA [33]
12.9
ERNIE-ViLG
7.9
Zero-shot
DALL-E [9]
27.5
CogView [17]
27.1
ERNIE-ViLG
14.7
Automatic Evaluation
For automatic evaluation, we compare ERNIE-ViLG with other strong methods on MS-
COCO [49]. MS-COCO is a publicly available benchmark for text-to-image synthesis, which is challenging for
containing many complex scenes that involve common objects. Following previous works, we randomly sample 30,000
images from the validation set and translate their corresponding captions to Chinese through Baidu Translate API. For
the generated images, we rerank the samples and select best of 60 samples for the zero-shot experiments for a fair
comparison with [17] and best of 10 samples when ﬁne-tuning. Fréchet Inception Distance (FID) [50] is adopted for
image quality assessment1.
The results illustrated in Table 1 compare our model with previous works. In the zero-shot setting, ERNIE-ViLG
surpasses DALL-E which is a 12-billion parameter model by a large margin, with a signiﬁcant FID improvement
of 12.8, even comparable to the fully-supervised models. It conﬁrms that ERNIE-ViLG acquires a general semantic
alignment between image and text, even for complex open-domain scenes. After ﬁne-tuning on the domain-speciﬁc
dataset, ERNIE-ViLG achieves the state-of-art result on MS-COCO, improving the FID metric by 5.0 and 1.4 over the
best transformer-based method and the best GAN-base method respectively.
Table 2: Average scores (1~5) of human evaluation.
Model
Image Clarity
Texture Quality
Relevance to the Text
CogView
3.867
2.623
2.203
ERNIE-ViLG
4.221
2.723
2.641
Human Evaluation
To obtain a direct assessment of the quality of images our model generated in zero-shot setting,
we build a diverse dataset for human evaluation, consisting of 500 texts for various circumstances. The text sentences
are collected from a variety of aspects to fully explore the general capability of ERNIE-ViLG, such as detailed attributes
for objects, combining multiple objects in a reasonable manner, etc. See more details about this dataset in Appendix A.
For the evaluations, three evaluators are asked to assess each image from three perspectives (image clarity, texture of
the image, relevance between the text and the image) with a quality score range from 1 to 5. We rerank and select the
best of 60 generated samples for each text and compare against CogView2. The average evaluation results are listed in
Table 2. ERNIE-ViLG achieves higher quality scores than CogView [17] from all three perspectives which shows that
our model acquires better zero-shot text-to-image generation capability.
1Same as previous works, we adopt evaluation code from https://github.com/MinfengZhu/DM-GAN
2Given texts, images generated by CogView are manually crawled from its ofﬁcial website.
8

--- Page 9 ---

悉尼歌剧院
Sydney Opera House
(a)
一只呆萌哈士奇
A cute husky
(b)
戴眼镜的泰迪熊毛绒玩具
Teddy bear plush toy
with glasses
(c)
美丽的鲜花围绕的农家小院
A farmyard surrounded
by beautiful flowers 
(d)
沿着铁轨行驶的
蓝黄相间的火车
A blue and yellow train
traveling down train
tracks
(e)
没有座的自行车
A bicycle without seat
(f)
Figure 4: Example images ERNIE-ViLG generated in zero-shot setting with texts from open domain. Figure 4(a)-Figure
4(b) show the generated images of simple objects. Figure 4(c)-Figure 4(e) exhibit generated images of complex scenes
with multiple objects. The example of creating image of non-existing objects is displayed in Figure 4(f).
北京天坛
the Temple of
Heaven in Beijing
None
卡通
cartoon
简笔画
brief strokes
中国画
traditional Chinese
painting
池塘里的莲花开了
The lotuses
blossom in the
pond
油画
oil painting
Figure 5: Images of different styles generated by ERNIE-ViLG. "None" indicates not adding any prompts about image
style.
Qualitative Results
ERNIE-ViLG has acquired the generation capability for various scenes, from basic objects to
complex combinations of objects. Some examples are shown in Figure 4. As can be seen in the examples, ERNIE-ViLG
can not only draw entities mentioned in the given text description, but also combine them together with the background
in a reasonable way. Surprisingly, we also ﬁnd two special skills ERNIE-ViLG develops. Firstly, ERNIE-ViLG can
generate images of different styles by simply adding text prompts without ﬁne-tuning like CogView does (Figure 5).
Secondly, our model can generate realistic images given Chinese ancient poetry which shows promising understanding
of brief and abstractive descriptions. Real concepts in the poetry are well-organized and artistic conception is well-
described (Figure 6).
日暮苍山远
At dusk, deep blue mountains
loom remote
长河落日圆
Past the long river the round
sun sinks low
清泉石上流
Over rocks and stones murmurs
spring water, so pure and clean
墙角数枝梅
At a wall corner some plum
trees grow
Figure 6: Generated images given Chinese ancient poetry.
9

--- Page 10 ---

4.3
Image Captioning
To fully assess the capability of ERNIE-ViLG for image captioning, we carry out automatic evaluations for a fair
comparison with previous methods and also evaluate the quality of generated captions through human judgement.
Automatic Evaluation
We conduct experiments on two commonly used Chinese image captioning datasets, AIC-ICC
[51] and COCO-CN [52]. For AIC-ICC, we ﬁne-tune ERNIE-ViLG on the training split and evaluate on the validation
split, following the same practice as [53]. And for the experiments on COCO-CN, we use the standard train/val/test split
and report results on the test split. We adopt the widely used metrics, BLEU@4, METEOR, ROUGE-L and CIDERr,
for all the evaluations.
As illustrated in Table 3 and Table 4, ERNIE-ViLG achieves the best results on both datasets. Speciﬁcally, compared to
the pre-training-based method [53], we obtain a signiﬁcant improvement of 2.1 BLEU@4 on AIC-ICC.
Table 3: Evaluation results for image captioning on COCO-CN test split. The results are all calculated at character-level
where the results of ’seq-learn’ are re-evaluated with their provided predictions.
Model
BLEU@4
METEOR
ROUGE-L
CIDERr
seq-learn [52]
48.4
29.5
59.2
128.4
ERNIE-ViLG
50.0
31.6
60.3
138.2
Table 4: Evaluation results for image captioning on AIC-ICC val split.
Model
BLEU@4
METEOR
ROUGE-L
CIDERr
BriVL [53]
66.1
41.1
71.9
220.7
ERNIE-ViLG
68.2
41.7
72.5
231.4
Human Evaluation
We also carry out a human evaluation campaign to assess the quality of captions generated by
ERNIE-ViLG. Given the image and generated predictions, the evaluator is asked to evaluate the caption quality from
three perspectives: ﬂuency (whether the caption is ﬂuent or not), relevance (whether the caption is related to the given
image or not) and richness (whether the caption adequately describe the whole content of the image or not) with a score
from 0 to 2 (higher is better). We randomly select 200 images from COCO-CN test set and make the predictions from
the zero-shot ERNIE-ViLG model and the ﬁne-tuned model.
The evaluation results are shown in Table 5. The ﬁne-tuned ERNIE-ViLG model obtains an average score of 1.62.
We also ﬁnd that zero-shot ERNIE-ViLG model obtains a high ﬂuency score, close to that of ﬁne-tuned model, but
the gap of the relevance score and the richness score between them are signiﬁcant. We consider that it is due to that
the web-crawled pre-training dataset tends to be noisy and most captions are less descriptive while the captions in
human-labeled captioning datasets (e.g., COCO-CN) are often descriptive which capture all the details of the image.
Some examples are illustrated in Figure 7.
Table 5: Human evaluation of the generated captions on the sampling images from COCO-CN test split.
Model
ﬂuency
relevance
richness
average score
ERNIE-ViLG (zero-shot)
1.82
1.09
0.76
1.22
ERNIE-ViLG
1.96
1.47
1.43
1.62
4.4
Generative Visual Question Answering
In the literature, the Visual Question Answering task is often converted to a multi-label classiﬁcation problem over a
predeﬁned candidate answer set. However, it is hard to deﬁne a closed set of candidate answers in real-world application,
which makes this simpliﬁcation remains a gap between research and practical application. In this paper, we study the
open-ended generative Visual Question Answering task, where the model is required to directly generate the answer,
given the image and question. An ideal generative model for this task needs to build semantic connections between the
image and the question based on visual and linguistic understanding, and generate ﬂuent textual answer. We conduct
10

--- Page 11 ---

Manual 
Caption
Zero-shot
Fine-tune
整洁的卧室里有一张床，一台电视机和一个沙发
There is a bed, a TV and a sofa in the tidy bedroom
酒店图片
A picture of hotel
一间干净整洁的房间里有一张沙发和一台电视
There is a sofa and a TV in a clean and tidy 
room
一个女人拿着冲浪板站在海滩上
A woman is standing on the 
beach with a surfboard
在海滩上放松的女人
A woman relaxing on the beach
一个女人抱着一个冲浪板站在海滩上
A woman was standing on the beach 
with a surfboard in her arms
一个专业的网球运动员在比赛中打了一个球
A professional tennis player played a 
ball in the game
网球运动员在比赛中击球
Tennis players hit the ball in the game
一个穿着白色上衣和黑色短裤的男子在网
球场上打网球
A man in a white coat and black shorts 
is playing tennis on the tennis court
Figure 7: Generated captions on COCO-CN. Although the zero-shot generated captions are various, it is sufﬁcient to
describe the image from the semantic perspective.
experiments on a public FMIQA [54] dataset, which has freestyle and diversiﬁed question-answer annotations. For the
evaluation, we conduct both Turing Test [54] (a human evaluator is asked to judge whether the answer is generated by a
machine or not) and answer quality evaluation (score from 0 to 2, higher is better) by human’s judgement.
We randomly select 200 samples from FMIQA validation split for the evaluations, as there is no ofﬁcial release of the
test set. We ﬁne-tune ERNIE-ViLG on the train split and use the ﬁne-tuned model to make predictions for the samples.
We also make the evaluation for the human-labeled answers to eliminate the bias of different evaluators compared to
[54]. The evaluation results can be seen in Table 6. ERNIE-ViLG achieves a Turing Text passing rate of 78.5%, which
signiﬁcantly surpasses that of mQA [54] and an answer score of 1.495 which clearly verify that our model has captured
the semantic alignments across vision and language modalities.
Table 6: Human evaluation on FMIQA. * means the evaluations on manual captions for our samples.
Model
Turing Test
Quality Evaluation
passing rate(%)
avg.score
Human annotations from [54]
94.8
1.918
mQA [54]
64.7
1.454
Human annotations *
97.5
1.870
ERNIE-ViLG
78.5
1.495
5
Analysis
To evaluate the beneﬁts our proposed end-to-end text-to-image synthesis method brings, we conduct experiments with
a lite version of transformer as the image discrete representation generator, which has about 300 million parameters
(24 transformer layers with 1024 hidden units and 16 attention heads). We utilize dVAE [9], rather than VQGAN, to
discretize the image to visual sequence and build the image from the visual tokens, considering the instability of the
training process of GAN. For the reconstructor, we use the same network architecture as dVAE. We develop a multi-task
learning process which assigns equal weights to the generation loss and the reconstruction loss. The models are trained
on a merged dataset of CC and CC12M and the evaluation is carried out on the MS-COCO validation set in zero-shot
setting.
We compare the results of our end-to-end training method with the two-stage pipeline baseline as shown in Table 7. For
the two-stage pipeline, we train a text-to-image generator and use the decoder of dVAE directly as the reconstructor.
The Two-stage G(R) refers to the separately trained generator(reconstructor), and the end-to-end G(R) refers to the
end-to-end trained generator(reconstructor). Our end-to-end method achieves a signiﬁcant FID improvement of 1.5
compared to the two-stage pipeline. We ﬁnd that combining the end-to-end trained generator (end-to-end G) and dVAE
11

--- Page 12 ---

decoder (two-stage R) also brings a FID improvement of 0.9 compared to that of two-stage pipeline, but falls behind
compared to the end-to-end methods. This indicates our proposed end-to-end method can improve both the performance
of the generator (two-stage G & two-stage R vs end-to-end G & two-stage R) and the reconstructor (end-to-end G &
two-stage R vs end-to-end G & end-to-end R).
We also input visual sequence of real images discretized by dVAE(gold image sequence) to the two reconstructors for
comparison. Experimental results (the last two lines in Table 7) show that the end-to-end trained reconstructor has more
obvious advantage in the reconstruction from real image discrete representation. We consider that end-to-end training
will be more effective on ERNIE-ViLG with 10 billion parameters, for the image discrete representation generated
by more capable generator is much closer to the real distribution, and hidden embeddings of larger model provides
more useful features for the reconstructor. Due to the instability of the training of both GAN and large-scale generative
model, we haven’t used end-to-end training for our 10-billion parameter model based on VQGAN. We will address the
instability issue for future work and improve the 10-billion parameter ERNIE-ViLG through end-to-end training.
Table 7: Comparison of the two-stage pipeline and end-to-end training.
Generator
Reconstructor
FID ↓
Two-stage G
Two-stage R
41.4
End-to-end G
Two-stage R
40.5
End-to-end G
End-to-end R
39.9
Gold image sequence
Two-stage R
21.7
Gold image sequence
End-to-end R
18.6
6
Conclusion
We propose ERNIE-ViLG to unify the bidirectional image-text generation tasks in one single generative model and
present an end-to-end training method for the text-to-image synthesis. Pre-trained on a large-scale image-text dataset,
ERNIE-ViLG captures the capabilities of bidirectional Vision-Language Generation and achieves superior performance
on various cross-modal generation tasks including text-to-image synthesis, image captioning and generative Visual
Question Answering. Overall, our model advances the uniﬁed pre-training for both the image-to-text and text-to-image
generation tasks further.
References
[1] Tadas Baltrušaitis, Chaitanya Ahuja, and Louis-Philippe Morency. Multimodal machine learning: A survey and
taxonomy. IEEE transactions on pattern analysis and machine intelligence, 41(2):423–443, 2018.
[2] Geoffrey Hinton, Li Deng, Dong Yu, George E Dahl, Abdel-rahman Mohamed, Navdeep Jaitly, Andrew Senior,
Vincent Vanhoucke, Patrick Nguyen, Tara N Sainath, et al. Deep neural networks for acoustic modeling in speech
recognition: The shared views of four research groups. IEEE Signal processing magazine, 29(6):82–97, 2012.
[3] Aaron van den Oord, Sander Dieleman, Heiga Zen, Karen Simonyan, Oriol Vinyals, Alex Graves, Nal Kalch-
brenner, Andrew Senior, and Koray Kavukcuoglu. Wavenet: A generative model for raw audio. arXiv preprint
arXiv:1609.03499, 2016.
[4] Oriol Vinyals, Alexander Toshev, Samy Bengio, and Dumitru Erhan. Show and tell: A neural image caption
generator. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 3156–3164,
2015.
[5] Scott Reed, Zeynep Akata, Xinchen Yan, Lajanugen Logeswaran, Bernt Schiele, and Honglak Lee. Generative
adversarial text to image synthesis. In International Conference on Machine Learning, pages 1060–1069. PMLR,
2016.
[6] Peter Anderson, Xiaodong He, Chris Buehler, Damien Teney, Mark Johnson, Stephen Gould, and Lei Zhang.
Bottom-up and top-down attention for image captioning and visual question answering. In Proceedings of the
IEEE conference on computer vision and pattern recognition, pages 6077–6086, 2018.
[7] Luowei Zhou, Hamid Palangi, Lei Zhang, Houdong Hu, Jason Corso, and Jianfeng Gao. Uniﬁed vision-language
pre-training for image captioning and vqa. In Proceedings of the AAAI Conference on Artiﬁcial Intelligence,
volume 34, pages 13041–13049, 2020.
12

--- Page 13 ---

[8] Han Zhang, Jing Yu Koh, Jason Baldridge, Honglak Lee, and Yinfei Yang. Cross-modal contrastive learning
for text-to-image generation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 833–842, 2021.
[9] Aditya Ramesh, Mikhail Pavlov, Gabriel Goh, Scott Gray, Chelsea Voss, Alec Radford, Mark Chen, and Ilya
Sutskever. Zero-shot text-to-image generation. arXiv preprint arXiv:2102.12092, 2021.
[10] Lele Chen, Sudhanshu Srivastava, Zhiyao Duan, and Chenliang Xu. Deep cross-modal audio-visual generation.
In Proceedings of the on Thematic Workshops of ACM Multimedia 2017, pages 349–357, 2017.
[11] Maciej ˙Zelaszczyk and Jacek Ma´ndziuk.
Audio-to-image cross-modal generation.
arXiv preprint
arXiv:2109.13354, 2021.
[12] Xiujun Li, Xi Yin, Chunyuan Li, Pengchuan Zhang, Xiaowei Hu, Lei Zhang, Lijuan Wang, Houdong Hu, Li Dong,
Furu Wei, et al. Oscar: Object-semantics aligned pre-training for vision-language tasks. In European Conference
on Computer Vision, pages 121–137. Springer, 2020.
[13] Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville,
and Yoshua Bengio. Generative adversarial nets. Advances in neural information processing systems, 27, 2014.
[14] Han Zhang, Tao Xu, Hongsheng Li, Shaoting Zhang, Xiaogang Wang, Xiaolei Huang, and Dimitris N Metaxas.
Stackgan: Text to photo-realistic image synthesis with stacked generative adversarial networks. In Proceedings of
the IEEE international conference on computer vision, pages 5907–5915, 2017.
[15] Aaron van den Oord, Nal Kalchbrenner, Oriol Vinyals, Lasse Espeholt, Alex Graves, and Koray Kavukcuoglu.
Conditional image generation with pixelcnn decoders. arXiv preprint arXiv:1606.05328, 2016.
[16] Mark Chen, Alec Radford, Rewon Child, Jeffrey Wu, Heewoo Jun, David Luan, and Ilya Sutskever. Generative
pretraining from pixels. In International Conference on Machine Learning, pages 1691–1703. PMLR, 2020.
[17] Ming Ding, Zhuoyi Yang, Wenyi Hong, Wendi Zheng, Chang Zhou, Da Yin, Junyang Lin, Xu Zou, Zhou
Shao, Hongxia Yang, et al. Cogview: Mastering text-to-image generation via transformers. arXiv preprint
arXiv:2105.13290, 2021.
[18] Aaron van den Oord, Oriol Vinyals, and Koray Kavukcuoglu. Neural discrete representation learning. arXiv
preprint arXiv:1711.00937, 2017.
[19] Jaemin Cho, Jiasen Lu, Dustin Schwenk, Hannaneh Hajishirzi, and Aniruddha Kembhavi. X-lxmert: Paint,
caption and answer questions with multi-modal transformers. arXiv preprint arXiv:2009.11278, 2020.
[20] Yupan Huang, Hongwei Xue, Bei Liu, and Yutong Lu. Unifying multimodal transformer for bi-directional image
and text generation. In Proceedings of the 29th ACM International Conference on Multimedia, pages 1138–1147,
2021.
[21] Patrick Esser, Robin Rombach, and Bjorn Ommer. Taming transformers for high-resolution image synthesis. In
Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 12873–12883,
2021.
[22] Jiasen Lu, Dhruv Batra, Devi Parikh, and Stefan Lee. Vilbert: Pretraining task-agnostic visiolinguistic representa-
tions for vision-and-language tasks. arXiv preprint arXiv:1908.02265, 2019.
[23] Yen-Chun Chen, Linjie Li, Licheng Yu, Ahmed El Kholy, Faisal Ahmed, Zhe Gan, Yu Cheng, and Jingjing Liu.
Uniter: Learning universal image-text representations. arXiv preprint arXiv:1909.11740, 2019.
[24] Fei Yu, Jiji Tang, Weichong Yin, Yu Sun, Hao Tian, Hua Wu, and Haifeng Wang. Ernie-vil: Knowledge enhanced
vision-language representations through scene graph. arXiv preprint arXiv:2006.16934, 1:12, 2020.
[25] Zhe Gan, Yen-Chun Chen, Linjie Li, Chen Zhu, Yu Cheng, and Jingjing Liu. Large-scale adversarial training for
vision-and-language representation learning. arXiv preprint arXiv:2006.06195, 2020.
[26] Wei Li, Can Gao, Guocheng Niu, Xinyan Xiao, Hao Liu, Jiachen Liu, Hua Wu, and Haifeng Wang. Unimo:
Towards uniﬁed-modal understanding and generation via cross-modal contrastive learning. arXiv preprint
arXiv:2012.15409, 2020.
[27] Pengchuan Zhang, Xiujun Li, Xiaowei Hu, Jianwei Yang, Lei Zhang, Lijuan Wang, Yejin Choi, and Jianfeng Gao.
Vinvl: Revisiting visual representations in vision-language models. In CVPR, 2021.
[28] Jaemin Cho, Jie Lei, Hao Tan, and Mohit Bansal. Unifying vision-and-language tasks via text generation. arXiv
preprint arXiv:2102.02779, 2021.
[29] Zirui Wang, Jiahui Yu, Adams Wei Yu, Zihang Dai, Yulia Tsvetkov, and Yuan Cao. Simvlm: Simple visual
language model pretraining with weak supervision. arXiv preprint arXiv:2108.10904, 2021.
13

--- Page 14 ---

[30] Piyush Sharma, Nan Ding, Sebastian Goodman, and Radu Soricut. Conceptual captions: A cleaned, hypernymed,
image alt-text dataset for automatic image captioning. In Proceedings of the 56th Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Papers), pages 2556–2565, 2018.
[31] Xinlei Chen, Hao Fang, Tsung-Yi Lin, Ramakrishna Vedantam, Saurabh Gupta, Piotr Dollár, and C Lawrence
Zitnick. Microsoft coco captions: Data collection and evaluation server. arXiv preprint arXiv:1504.00325, 2015.
[32] Xiaowei Hu, Zhe Gan, Jianfeng Wang, Zhengyuan Yang, Zicheng Liu, Yumao Lu, and Lijuan Wang. Scaling up
vision-language pre-training for image captioning. arXiv preprint arXiv:2111.12233, 2021.
[33] Chenfei Wu, Jian Liang, Lei Ji, Fan Yang, Yuejian Fang, Daxin Jiang, and Nan Duan. N\" uwa: Visual synthesis
pre-training for neural visual world creation. arXiv preprint arXiv:2111.12417, 2021.
[34] Kelvin Xu, Jimmy Ba, Ryan Kiros, Kyunghyun Cho, Aaron Courville, Ruslan Salakhudinov, Rich Zemel, and
Yoshua Bengio. Show, attend and tell: Neural image caption generation with visual attention. In ICML, 2015.
[35] Lun Huang, Wenmin Wang, Jie Chen, and Xiao-Yong Wei. Attention on attention for image captioning. In
Proceedings of the IEEE/CVF International Conference on Computer Vision, pages 4634–4643, 2019.
[36] Simao Herdade, Armin Kappeler, KoﬁBoakye, and Joao Soares. Image captioning: Transforming objects into
words. arXiv preprint arXiv:1906.05963, 2019.
[37] Minfeng Zhu, Pingbo Pan, Wei Chen, and Yi Yang. Dm-gan: Dynamic memory generative adversarial networks
for text-to-image synthesis. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 5802–5810, 2019.
[38] Li Dong, Nan Yang, Wenhui Wang, Furu Wei, Xiaodong Liu, Yu Wang, Jianfeng Gao, Ming Zhou, and Hsiao-
Wuen Hon. Uniﬁed Language Model Pre-training for Natural Language Understanding and Generation. In
NeurIPS, 2019.
[39] Xiao Dongling, Zhang Han, Li Yukun, Su Yu, Tian Hao, Wu Hua, and Wang Haifeng. ERNIE-GEN: An Enhanced
Multi-Flow Pre-training and Fine-tuning Framework for Natural Language Generation. In IJCAI, 2020.
[40] Soravit Changpinyo, Piyush Sharma, Nan Ding, and Radu Soricut. Conceptual 12m: Pushing web-scale image-text
pre-training to recognize long-tail visual concepts. In Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition, pages 3558–3568, 2021.
[41] Ma Yanjun, Yu Dianhai, Wu Tian, and Wang Haifeng. Paddlepaddle: An open-source deep learning platform
from industrial practice. Frontiers of Data and Domputing, pages 105–115, 2019.
[42] Rajbhandari S., Rasley J., Ruwase O., and He Y. Zero: Memory optimizations toward training trillion parameter
models. International Conference for High Performance Computing, Networking, Storage and Analysis, pages
1–16, 2020.
[43] Ao Yulong, Wu Zhihua, and Yu Dianhai. End-to-end adaptive distributed training on paddlepaddle. arXiv preprint
arXiv:2112.02752, 2021.
[44] T Chen, B Xu, and C Zhang. Training deep nets with sublinear memory cost. arXiv preprint arXiv:1604.06174,
2016.
[45] P Micikevicius, S Narang, and J Alben. Mixed precision training. arXiv preprint arXiv:1710.03740, 2017.
[46] J Ren, S Rajbhandari, and Y Aminabadi, R. Zero-ofﬂoad: Democratizing billion-scale model training. arXiv
preprint arXiv:2101.06840, 2021.
[47] Tao Xu, Pengchuan Zhang, Qiuyuan Huang, Han Zhang, Zhe Gan, Xiaolei Huang, and Xiaodong He. Attngan:
Fine-grained text to image generation with attentional generative adversarial networks. In Proceedings of the
IEEE conference on computer vision and pattern recognition, pages 1316–1324, 2018.
[48] Ming Tao, Hao Tang, Songsong Wu, Nicu Sebe, Xiao-Yuan Jing, Fei Wu, and Bingkun Bao. Df-gan: Deep fusion
generative adversarial networks for text-to-image synthesis. arXiv preprint arXiv:2008.05865, 2020.
[49] Tsung-Yi Lin, Michael Maire, Serge J Belongie, James Hays, Pietro Perona, Deva Ramanan, Piotr Dollár, and
C Lawrence Zitnick. Microsoft coco: Common objects in context. In ECCV (5), 2014.
[50] Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, and Sepp Hochreiter. Gans trained by
a two time-scale update rule converge to a local nash equilibrium. Advances in neural information processing
systems, 30, 2017.
[51] Jiahong Wu, He Zheng, Bo Zhao, Yixin Li, Baoming Yan, Rui Liang, Wenjia Wang, Shipei Zhou, Guosen Lin,
Yanwei Fu, Yizhou Wang, and Yonggang Wang. Ai challenger : A large-scale dataset for going deeper in image
understanding. arXiv preprint arXiv:1711.06475, 2017.
14

--- Page 15 ---

[52] Xirong Li, Chaoxi Xu, Xiaoxu Wang, Weiyu Lan, Zhengxiong Jia, Gang Yang, and Jieping Xu. Coco-cn for
cross-lingual image tagging, captioning, and retrieval. IEEE Transactions on Multimedia, 21(9):2347–2360, 2019.
[53] Yuqi Huo, Manli Zhang, Guangzhen Liu, Haoyu Lu, Yizhao Gao, Guoxing Yang, Jingyuan Wen, Heng Zhang,
Baogui Xu, Weihao Zheng, Zongzheng Xi, Yueqian Yang, Anwen Hu, Jinming Zhao, Ruichen Li, Yida Zhao,
Liang Zhang, Yuqing Song, Xin Hong, Wanqing Cui, Dan Yang Hou, Yingyan Li, Junyi Li, Peiyu Liu, Zheng
Gong, Chuhao Jin, Yuchong Sun, Shizhe Chen, Zhiwu Lu, Zhicheng Dou, Qin Jin, Yanyan Lan, Wayne Xin Zhao,
Ruihua Song, and Ji-Rong Wen. Wenlan: Bridging vision and language by large-scale multi-modal pre-training.
arXiv preprint arXiv:2103.06561, 2021.
[54] Haoyuan Gao, Junhua Mao, Jie Zhou, Zhiheng Huang, Lei Wang, and Wei Xu. Are you talking to a machine?
dataset and methods for multilingual image question answering. arXiv preprint arXiv:1505.05612, 2015.
A
Dataset for human evaluation of text-to-image synthesis
Table 8: Statistics of the dataset for human evaluation.
Description Angle
Number
1
MS-COCO
102
2
anthropomorphic animal / cartoon characters
49
3
geography
50
4
multi-object + attribute description + relationship description
68
5
single-object + attribute description
56
6
counter fact
54
7
different view angles
43
8
different styles
43
9
different time, different scenes
35
The dataset for human evaluation of text-to-image synthesis has 500 texts that are collected from 9 different aspects.
Details of this dataset is shown in Table 8. 102 texts are randomly selected from MS-COCO’s validation set, while the
others are manually designed.
15

```
