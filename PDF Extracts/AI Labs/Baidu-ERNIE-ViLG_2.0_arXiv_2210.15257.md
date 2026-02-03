---
title: "ERNIE ViLG 2.0 arXiv 2210.15257"
source_pdf: "AI Labs/Baidu/ERNIE 4.5/ERNIE-ViLG_2.0_arXiv_2210.15257.pdf"
company: "Baidu"
pages: 19
extracted_at: "2026-01-31T17:32:29.849006"
type: "ai_lab_paper"
---

# ERNIE ViLG 2.0 arXiv 2210.15257

**Company/Lab:** Baidu
**Model:** ERNIE 4.5
**Source PDF:** AI Labs/Baidu/ERNIE 4.5/ERNIE-ViLG_2.0_arXiv_2210.15257.pdf
**Total Pages:** 19

---

## Content

```
--- Page 1 ---

ERNIE-ViLG 2.0: Improving Text-to-Image Diffusion Model with
Knowledge-Enhanced Mixture-of-Denoising-Experts
Zhida Feng1,2,*, Zhenyu Zhang1,∗, Xintong Yu1,∗, Yewei Fang1, Lanxin Li1, Xuyi Chen1, Yuxiang Lu1,
Jiaxiang Liu1, Weichong Yin1, Shikun Feng1, Yu Sun1, Li Chen2, Hao Tian1, Hua Wu1, Haifeng Wang1
1Baidu Inc.
2School of Computer Science and Technology, Wuhan University of Science and Technology
{fengzhida, zhangzhenyu07, yuxintong}@baidu.com
{liujiaxiang, yinweichong, fengshikun01, sunyu02}@baidu.com
一艘青花瓷质感的战舰
精致面容的古风少女，
头戴百鸟鲜花头冠
一只仙鹤站在平静的湖面上，
后面有一轮云雾缭绕的明月
穿西装的孙悟空的特写镜头
A warship with blue and white
porcelain texture
An ancient style girl with delicate face,
wearing a crown of birds and ﬂowers
A crane is standing on the calm lake,
with a bright moon surrounded by
clouds in the background
The close up of Sun Wukong
in a suit
狮子王身穿紫色皇家大衣，身披红
色皇家斗篷，正在发表史诗级的演说
雪地里的熊猫宝宝戴着红帽子、
黄手套，穿着绿毛衣和蓝裤子
一只欢快的柯基行走在夕阳里，
光从右边打来铺成一地金黄
泰迪熊穿着戏服，站在太和殿前唱京剧
The Lion King, wearing a purple
royal coat and a red royal cloak,
is delivering an epic speech
A baby panda in the snow,
wearing red hat, yellow gloves,
green sweater and blue pants
A cheerful Koji is walking in the sunset,
the golden light comes from the right side
and spreads all over the ground
A teddy bear, wearing a costume, is
standing in front of the Hall of Supreme
Harmony and singing Beijing opera
Figure 1. Selected 1024×1024 samples with various text inputs, which shows that ERNIE-ViLG 2.0 has powerful capabilities of ﬁne-grained
semantic control and high-resolution image synthesis, as well as to produce high-quality creative images of different styles.
Abstract
Recent progress in diffusion models has revolutionized the
popular technology of text-to-image generation. While exist-
* denotes equal contribution. Work done during Feng’s internship at Baidu.
ing approaches could produce photorealistic high-resolution
images with text conditions, there are still several open prob-
lems to be solved, which limits the further improvement of
image ﬁdelity and text relevancy. In this paper, we pro-
pose ERNIE-ViLG 2.0, a large-scale Chinese text-to-image
arXiv:2210.15257v2  [cs.CV]  28 Mar 2023

--- Page 2 ---

diffusion model, to progressively upgrade the quality of gen-
erated images by: (1) incorporating ﬁne-grained textual and
visual knowledge of key elements in the scene, and (2) utiliz-
ing different denoising experts at different denoising stages.
With the proposed mechanisms, ERNIE-ViLG 2.01 not only
achieves a new state-of-the-art on MS-COCO with zero-shot
FID-30k score of 6.75, but also signiﬁcantly outperforms
recent models in terms of image ﬁdelity and image-text align-
ment, with side-by-side human evaluation on the bilingual
prompt set ViLG-300.
1. Introduction
Recent years have witnessed incredible progress in text-to-
image generation. With large-scale training data and model
parameters, kinds of text-to-image generation models are
now able to vividly depict the visual scene described by a
text prompt, and enable anyone to create exquisite images
without sophisticated drawing skills. Among all types of
image generation approaches, diffusion models [9] are at-
tracting increasing attention due to their ability to produce
highly photorealistic images conditioned on text prompts.
Given a text prompt, the models transform a Gaussian noise
into an image that conforms to the prompt through iterative
denoising steps. In the past years, text-to-image diffusion
models such as LDM [25], GLIDE [18], DALL-E 2 [22], and
Imagen [26] have achieved impressive performance in both
text relevancy and image ﬁdelity. Despite these advances,
the exploration of diffusion models by existing methods is
still at the initial stage. When we go deep into the princi-
ple and implementation of text-to-image diffusion models,
there are still many opportunities to improve the quality of
generated images further.
First, during the learning process of each denoising step,
all text tokens interact with image regions and all the image
regions contribute equally to the ﬁnal loss function. How-
ever, a visual scene of text and image contains many ele-
ments (i.e., textual words and visual objects), and different
elements usually hold different importance for the expres-
sion of the scene semantics [42]. The indiscriminate learning
process may cause the model to miss some key elements and
interactions in the scene, thus facing the risk of text-image
misalignment, such as the attribute confusion problem, es-
pecially for text prompts containing multiple objects with
speciﬁc attributes [22]. Second, when opening the horizon
from individual step to the whole denoising process, we can
found that the requirements of different denoising stages
are also not identical. In the early stages, the input images
are highly noised, and the model is required to outline the
semantic layout and skeleton out of almost pure noise. By
contrast, in the later steps close to the image output, denois-
1https://wenxin.baidu.com/ernie-vilg
ing mainly means improving the details based on an almost
completed image [25]. In practice, existing models usually
use one U-Net for all steps, which means that the same set
of parameters has to learn different denoising capabilities.
In this paper, we propose ERNIE-ViLG 2.0, an improved
text-to-image diffusion model with knowledge-enhanced
mixture-of-denoising-experts, to incorporate extra knowl-
edge about the visual scene and decouple the denoising ca-
pabilities in different steps. Speciﬁcally, we employ a text
parser and an object detector to extract key elements of the
scene in the input text-image pair, and then guide the model
to pay more attention to their alignment in the learning pro-
cess, so as to hope the model could handle the relationships
among various objects and attributes. Moreover, we divide
the denoising steps into several stages and employ speciﬁc
denoising “experts” for each stage. With the mixture of
multiple experts, the model can involve more parameters
and learn the data distribution of each denoising stage better,
without increasing the inference time, as only one expert is
activated in each denoising step.
With the extra knowledge from the visual scene and the
mixture-of-denoising-experts mechanism, we train ERNIE-
ViLG 2.0 and scale up the model size to 24B parameters.
Experiments on MS-COCO show that our model exceeds
previous text-to-image models by setting a new state-of-the-
art of 6.75 zeros-shot FID-30k score, and detailed ablation
studies conﬁrm the contributions of each proposed strategy.
Apart from automatic metrics, we also collect 300 bilingual
text prompts that could assess the quality of generated im-
ages from different aspects and enable a fair comparison
between English and Chinese text-to-image models. The hu-
man evaluation results again indicate that ERNIE-ViLG 2.0
outperforms other recent methods, including DALL-E 2 [22]
and Stable Diffusion [25], by a signiﬁcant margin both in
terms of image-text alignment and image ﬁdelity.
To sum up, the main contributions of this work are: (1)
We incorporate textual and visual knowledge into the text-
to-image diffusion model, which effectively improves the
ability of ﬁne-grained semantic control and alleviates the
problem of object-attribute mismatching in generated images.
(2) We propose the mixture-of-denoising-experts mechanism
to reﬁne the denoising process, which can adapt to the char-
acteristics of different denoising steps and scale up the model
to 24B parameters, making it the largest text-to-image model
at present. (3) ERNIE-ViLG 2.0 achieves the state-of-the-art
zero-shot FID-30k score of 6.75 on MS-COCO, surpasses
DALL-E 2 and Stable Diffusion in human evaluation on the
Chinese-English bilingual prompt set ViLG-300.
2. Method
During the training process, the text-to-image diffusion
model receives paired inputs (x, y) consisting of an image x
with its text description y, and the ultimate goal is to gener-

--- Page 3 ---

𝑥!
object
detection
[ a ] 灰色的[ n ] 猫和[ a ] 棕色的[ n ] 狗，[ n ] 碗
a [a] grey [n] cat and a [a] brown [n] dog
, [n] bowl
textual knowledge: keywords
visual knowledge:
key objects
denoising loss ℒ
𝑥"",!
text encoder
training
preprocessing
猫
cat
𝑥$
𝑥!!
𝑥!"
𝑥!#
𝑥%
...
...
...
...
𝑥"",$
𝑥"",!!
𝑥"",!"
𝑥"",!#
𝑥!
...
𝑥"",%
𝑥"",!
Mixture-of-Denoising-Experts (MoDE)
append
狗
dog
碗
bowl
MoDE
...
...
𝜖!,#
𝜖!,$
𝜖!,%
Figure 2. The architecture of ERNIE-ViLG 2.0, which incorporates ﬁne-grained textual and visual knowledge of key elements in the scene
and utilizes different denoising experts at different denoising stages.
ate x based on y. To achieve this, a text encoder fθ(·) ﬁrst
encodes y as fθ(y), then a denoising network ϵθ(·) condi-
tioned on fθ(y) learns to generate x from a Gaussian noise.
To help the model generate high-quality images that accu-
rately match the text description (i.e., text prompt), ERNIE-
ViLG 2.0 enhances text encoder fθ(·) and denoising network
ϵθ(·) with textual and visual knowledge of key elements in
the scene. Furthermore, ERNIE-ViLG 2.0 employs mixture-
of-denoising-experts to reﬁne the image generation process,
where different experts are responsible for different genera-
tion steps in the denoising process. The overall architecture
of ERNIE-ViLG 2.0 is shown in Figure 2 and the details are
described in the following subsections.
2.1. Preliminary
Denoising diffusion probabilistic models (DDPM) are a
class of score-based generative models that have recently
shown delightful talents in the ﬁeld of text-to-image genera-
tion [9]. The diffusion process of DDPM aims to iteratively
add diagonal Gaussian noise to the initial data sample x and
turn it into an isotropic Gaussian distribution after T steps:
xt = √αtxt−1 +
√
1 −αtϵt,
t ∈{1, . . . , T}
(1)
where the sequence {xt} starts with x0 = x and ends with
xT ∼N(0, I), the added noise at each step is ϵt ∼N(0, I),
and {αt}1...T is a pre-deﬁned schedule [30,32]. The denois-
ing process is the reverse of diffusion, which converts the
Gaussian noise xT ∼N(0, I) back into the data distribution
x0 through iterative denoising steps t = T, . . . , 1. During
training, for a given image x, the model calculates xt by
sampling a Gaussian noise ϵ ∼N(0, I):
xt = √¯αtx0 +
√
1 −¯αtϵ,
(2)
where ¯αt = Qt
s=1 αs. Given xt, the target of the denoising
network ϵθ(·) is to restore x0 by predicting the noise ϵ. It is
learned via the loss function
L = Ex,ϵ∼N (0,I),t

||ϵ −ϵθ(xt, t)||2
2

.
(3)
With the predicted ϵθ(xt, t), we can have the prediction
of x0 at step t by converting Equation (2):
ˆx0,t =
1
√¯αt
(xt −
√
1 −¯αtϵθ(xt, t)).
(4)
In Figure 2, we visualize the sampled xt and the predicted
ˆx0,t for several timesteps during training. In the inference
process of DDPM, x0 is unknown, so the model iteratively
generates xt−1 based on xt and ˆx0,t:
xt−1 =1 −¯αt−1
1 −¯αt
√αtxt + 1 −αt
1 −¯αt
√¯αt−1ˆx0,t
+
r
(1 −¯αt−1)(1 −αt)
1 −¯αt
ϵ′
t,
t ∈{T, . . . , 1},
(5)
where ϵ′
t ∼N(0, I) is a sampled Gaussian noise.
The denoising network ϵθ(·) is typically implemented by
U-Net [9]. To allow ϵθ(·) to condition on text prompts,
a text encoder fθ(·) ﬁrst extracts the text representation
fθ(y) ∈Rny×dy, which is then fed into ϵθ(·) via a cross-
modal attention layer [18]. Formally, the U-Net represen-
tation ϕi(xt) ∈Rnx×d is concatenated with the text repre-
sentation fθ(y) after projection, and then goes through an
attention layer to achieve cross-modal interaction,
Q = ϕi(xt)W (i)
Q ,
K = [ϕi(xt)W (i)
Kx; fθ(y)W (i)
Ky],
V = [ϕi(xt)W (i)
Vx ; fθ(y)W (i)
Vy ],
(6)
Attention(Q, K, V ) = softmax
QK⊤
√
d

V,
(7)
where i is the index for U-Net layers, [; ] is the concatena-
tion operator, W (i)
Q , W (i)
Kx, W (i)
Vx ∈Rd×d and W (i)
Ky, W (i)
Vy ∈
Rdy×d are learnable projection layers, nx and ny are the
length of encoded image and text, respectively.
During inference, given a text prompt y, the denoising
U-Net ϵθ(·) predicts the image sample x conditioned on
the text y with classﬁer-free guidance [10] and Denoising
Diffusion Implicit Models (DDIM) sampling [31].

--- Page 4 ---

2.2. Knowledge-Enhanced Diffusion Model
The text-to-image model receives a text prompt that de-
scribes the scene of an image, then depicts it with crucial
objects and corresponding attribute details. In other words,
both text and image are intended to express a visual scene,
in which key elements have different expressions, such as
keywords in text or salient regions in image. However, naive
diffusion model does not distinguish the importance of el-
ements and indiscriminately iterates the denoising process.
ERNIE-ViLG 2.0 incorporates extra text and visual knowl-
edge into the learning stage, hoping to enhance the ﬁne-
grained semantic perception of diffusion model.
Textual Knowledge. An ideal text-to-image model is ex-
pected to focus on all the critical semantics mentioned in
the text prompt. To distinguish function words and words
describing key semantics, we adopt an off-the-shelf part-
of-speech toolkit to extract lexical knowledge of the input
prompt, and then improve the learning process by (1) insert-
ing special tokens into the input sequence and (2) increasing
the weight of tokens with speciﬁc part-of-speech tags in the
attention layer. Speciﬁcally, we selected 50% of samples
and inserted special tokens at the beginning of each word, in
which each part-of-speech tag corresponds to a special token.
For the selected samples, we also strengthen the attention
weight of keywords based on the lexical analysis results. In
this way, Equation (7) is modiﬁed to,
Attention(Q, K, V )′ = softmax
Wa · (QK⊤)
√
d

V,
(8)
where Wa ∈Rnx×(nx+ny) is an auxiliary weight matrix that
used to scale the vanilla attention, and
W ij
a =
 1 + wa
toki ∈{x}, tokj ∈{x, ykey}
1
otherwise.
(9)
Here wij
a is the scaling factor of the attention weight between
token toki and tokj, wa is a hyper-parameter, x refers to all
the image tokens, and ykey denotes the keywords in text2.
Figure 2 gives an example, where special tokens “[a]” and
“[n]” are inserted for adjectives and nouns, respectively.
Visual Knowledge. Similar to notional words in the text
prompt, there are also salient regions in an image, such as
people, trees, buildings, and objects mentioned in the in-
put. To extract such visual knowledge, we apply an object
detector [1] to 50% of training samples, and then select eye-
catching objects from the results with heuristic strategies.
Since the loss function of the diffusion model directly acts
on the image space, we can assign higher weights to corre-
sponding regions by modifying Equation (3), thus promoting
the model to focus on the generation of these objects:
L′ = Ez,ϵ∼N (0,I),t

Wl · ||ϵ −ϵθ(zt, t)||2
2

,
(10)
2The keywords is deﬁned as notional words in modern Chinese (i.e.,
nouns, verbs, adjectives, numerals, quantiﬁers, and pronouns).
W ij
l
=
 1 + wl
losij ∈{xkey}
1
otherwise.
(11)
Here Wl ∈Rnh×nw is the weight matrix, nh and nw are the
height and weight of image space, wl is a hyper-parameter,
losij is the loss item in i-th row and j-th column of image
space, xkey is the regions that corresponding to key objects.
As Figure 2 illustrates, the regions of “dog” and “cat” are
assigned with larger weights in the calculation of L′.
Now a new problem arises: as a kind of ﬁne-grained
knowledge, the selected objects may not appear in the text
prompt, thus perplexing the model in learning the alignment
between words and objects. An intuitive idea is ﬁrst to obtain
the object and attribute category of each region, then com-
bine corresponding class labels with the original text prompt
to achieve ﬁne-grained description, thus ensuring the input
contains both coarse and ﬁne granularity information. For
instance, as shown in Figure 2, the detected object “bowl”
is not included in the caption, so we append it to the original
description. Besides, we also employ an image captioning
model [38] to generate text for images, and randomly re-
place the original prompt with generated captions, because
the generated captions of many images are more concise and
reveal more accurate semantics than original prompts.
Most notably, the above strategies are only limited to the
training stage. By randomly selecting a part of samples to
equip these additional enhancement strategies, the model
is supposed to sense the hints of knowledge from various
perspectives, and generate higher quality images for the
given text in the inference stage, even without special tokens,
attention strengthening, or text reﬁnement.
2.3. Mixture-of-Denoising-Experts
Recall that the diffusion process is to iteratively corrupt
the image with Gaussian noises by a series of diffusion steps
t = 1, . . . , T, and DDPM [9] are trained to revert the diffu-
sion process by denoising steps t = T, . . . , 1. During the
denoising process, all steps aim to denoise a noised input,
and they together convert a completely random noise into
a meaningful image gradually. Although sharing the same
goal, the difﬁculty of these denoising steps varies according
to the noise ratio of input. Figure 2 illustrates such differ-
ence by presenting some examples of xt and the denoising
prediction ˆx0,t during training. For timesteps t near T, such
as t = T, tk, tj in the ﬁgure, the input of the denoising net-
work xt is highly noised, and the network of these steps
mainly tackles a generation task, i.e., generating an image
from a noise. On the contrary, for timesteps t near 1, such as
t = ti, 1, the input xt is close to the original image, and the
network of these steps needs to reﬁne the image details.
DDPM makes no speciﬁc assumption on the implementa-
tion of denoising network, that is, the denoising process does
not require the same denoising network for all steps in theory.
However, most of the previous text-to-image diffusion ap-

--- Page 5 ---

proaches [18,22,25,26] follow the vanilla implementation to
adopt a denoising network for the whole denoising process.
Considering that tasks of different timesteps are different,
we conjecture that using the same set of parameters to learn
different tasks might lead to suboptimal performance.
In view of this, we further propose Mixture-of-Denoising-
Experts (MoDE), where the primary motivation is to employ
multiple specialized expert networks to ﬁt different tasks at
different timesteps. Since the inputs of adjacent timesteps
are similar and so are the denoising tasks, we divide all
the timesteps uniformly into n blocks (S1, · · · , Si, · · · , Sn),
in which each block consists of consecutive timesteps and
is assigned to one denoising expert. In other words, the
timesteps in the same block are denoised by the same group
of network parameters. In practice, we share the same text
encoder for all denoising experts, and utilize different U-Net
experts for different timestep blocks:
ϵθ(xt, t) = {ϵθ,i(xt, t)},
t ∈Si,
(12)
where ϵθ,i(xt, t) is the i-th expert network. Herein, MoDE
improves the model performance by adopting expert net-
works to specially deal with different denoising stages.
Intuitively, when using more experts, each block contains
fewer timesteps, so each expert could better focus on learning
the characteristics of speciﬁc denoising steps assigned to it.
Meanwhile, as only one expert network is activated at each
step, increasing the number of experts does not affect the
computation overhead during inference. Therefore, ERNIE-
ViLG 2.0 can ﬂexibly scale up the parameters of diffusion
model, allowing the experts to ﬁt the data distribution better
without increasing inference time.
3. Experiments
In this section, we ﬁrst introduce the implementation
details of ERNIE-ViLG 2.0. Then we present the comparison
of models with automatic metrics and human evaluation.
Last, we further analyze the results with quantitative ablation
studies and qualitative showcases.
3.1. Implementation Details
To reduce learning complexity, we use diffusion models
to generate the representations of images in latent space of an
image auto-encoder following Latent Diffusion Models [25].
We ﬁrst pre-train an image encoder to transform an image
x ∈Rnh×nw×3 from pixel space into latent space ˆx ∈
Rnl
h×nl
w×4 and an image decoder to convert it back. Here
nh/nl
h and nw/nl
w denote the image’s original/latent height
and width, and we collectively refer to pixel space and hidden
space as image space in this paper. Then we ﬁx the auto-
encoder and train the diffusion model to generate ˆx from text
prompt y. During inference, we adopt the pre-trained image
decoder to turn ˆx into pixel-level image output.
Table 1. Comparison of ERNIE-ViLG 2.0 and representative text-to-
image generation models on MS-COCO 256 × 256 with zero-shot
FID-30k. We use classiﬁer-free guidance scale 2.1 for our diffusion
model and achieve the best performance.
Model
Zero-Shot FID-30k ↓
DALL-E [23]
27.50
CogView [2]
27.10
LAFITE [46]
26.94
LDM [25]
12.61
ERNIE-ViLG [45]
14.70
GLIDE [18]
12.24
Make-A-Scene [6]
11.84
DALL-E 2 [22]
10.39
CogView2 [3]
24.00
Imagen [26]
7.27
Parti [43]
7.23
ERNIE-ViLG 2.0
6.75
ERNIE-ViLG 2.0 contains a transformer-based text en-
coder with 1.3B parameters and 10 denoising U-Net experts
with 2.2B parameters each, which totally add up to about
24B parameters. For hyper-parameters to incorporate knowl-
edge, the attention weight scale wa is set to 0.01 and the loss
weight scale wl is set to 0.1 (both chosen from [0.01, 0.1,
0.5, 1]). For the MoDE strategy, all timesteps are divided
into 10 blocks. The model is optimized by AdamW [15],
with a ﬁxed learning rate 0.9 × 10−4, β1 = 0.9, β2 = 0.999,
and weight decay of 0.01. We train ERNIE-ViLG 2.0 on
320 Tesla A100 GPUs for 18 days. More training details are
introduced in Appendix A.
The training data consists of 170M image-text pairs, in-
cluding publicly available English datasets like LAION [28]
and a series of internal Chinese datasets. The image auto-
encoder is trained on the same set. For images with English
captions, we translate them with Baidu Translate API3 to get
the Chinese version.
3.2. Results
Automatic Evaluation on MS-COCO. Following previous
work [22, 25, 26], we evaluate ERNIE-ViLG 2.0 on MS-
COCO 256 × 256 with zero-shot FID-30k, where 30,000
images from the validation set are randomly selected and the
English captions are automatically translated to Chinese.
Table 1 shows that ERNIE-ViLG 2.0 achieves new state-
of-the-art performance of text-to-image generation, with
6.75 zero-shot FID-30k on MS-COCO. Inspired by DALL-
E [23] and Parti [43], we rerank the batch-sampled images
(with only 4 images per text prompt, comparing with 512 im-
ages used in DALL-E and 16 images used in Parti) based on
the image-text alignment score, calculated by a pre-trained
3https://fanyi.baidu.com

--- Page 6 ---

Alignment
Fidelity
0%
50%
100%
prefer ViLG 2.0
prefer DALL-E 2
(a) v.s. DALL-E 2.
Alignment
Fidelity
0%
50%
100%
prefer ViLG 2.0
prefer Sta. Diff.
(b) v.s. Stable Diffusion.
Figure 3. Comparison of ERNIE-ViLG 2.0 and DALL-E 2/Stable
Diffusion on ViLG-300 with human evaluation. We report the user
preference rates with 95% conﬁdence intervals.
ViLG 2.0
DALL-E 2
Sta. Diff.
(1) A green cup and a blue cell phone
(3) Zongzi and corn boiled in the pot
(2) A wine glass on top of a dog
(4) Cherry blossom, digital oil painting
Figure 4. Qualitative Comparison of ERNIE-ViLG 2.0 and DALL-
E 2/Stable Diffusion on ViLG-300. For 4 v.s. 4 comparison, refer
to the Figure 13 and 14 in appendix.
CLIP model [21], in which the text is the initial English
caption in MS-COCO and the image is generated from the
auto-translated Chinese caption. Besides, even without the
reranking strategy, we ﬁnd that ERNIE-ViLG 2.0 can also
beat the latest diffusion-based models like DALL-E 2 [22]
and Imagen [26], with the zero-shot FID-30k of 7.23. See
also Appendix B for a detailed comparison with regard to
model sizes and reranking strategies.
Human Evaluation on ViLG-300. ERNIE-ViLG 2.0 takes
Chinese prompts as input and generates high-resolution im-
ages, unlike recent English-oriented text-to-image models.
Herein, we introduce ViLG-3004, a bilingual prompt set
that supports the systematic evaluation and comparison of
Chinese and English text-to-image models. ViLG-300 con-
tains 300 prompts from 16 categories, composed of Draw-
Bench [26] (in English) and the prompt set used in ERNIE-
ViLG [45] (in Chinese). See Appendix C.1 for more details
about the construction process.
With ViLG-300, we can make convincing comparisons
4https : / / github . com / PaddlePaddle / ERNIE / tree /
ernie- kit- open- v1.0/Research/ERNIE- ViLG2/data/
ViLG-300.csv
0.285
0.290
0.295
0.300
0.305
CLIP Score
13
15
17
19
21
23
FID-10k
baseline
w/ object
w/ textual
w/ visual
w/ all
(a) Knowledge enhancement.
0.290
0.295
0.300
0.305
0.310
CLIP Score
11
13
15
17
19
21
FID-10k
1 expert
2 experts
5 experts
10 experts
(b) Mixture-of-denoising-experts.
Figure 5. Performance with various strategies in ERNIE-ViLG 2.0.
Here we draw pareto curves with guidance scale [2,3,4,5,6,7,8,9].
between ERNIE-ViLG 2.0 and DALL-E 25, Stable Diffu-
sion67. For evaluation, ﬁve raters are presented with two sets
of images generated by ERNIE-ViLG 2.0 and the compared
model. Next, they are asked to compare these images from
two dimensions of image-text alignment and image ﬁdelity,
and then select the model they prefer, or respond that there is
no measurable difference between two models. Throughout
the process, raters are unaware of which model the image is
generated from, and we do not apply any ﬁltering strategy to
the rating results. Figure 3 shows that human raters prefer
ERNIE-ViLG 2.0 over all other models in both image-text
alignment (56.5%±3.8% and 68.2%±3.8% when compared
to DALL-E 2 and Stable Diffusion, respectively) and image
ﬁdelity (58.8%±3.6% to DALL-E 2, 66.5%±3.5% to Stable
Diffusion, respectively), which again proves that ERNIE-
ViLG 2.0 can generate high-quality images that conform
to the text, with the help of knowledge enhancement and
mixture-of-denoising-experts strategies. We provide compar-
isons of separate categories in Appendix C.2. Beyond text
relevancy and image ﬁdelity, we also observe that ERNIE-
ViLG 2.0 can generate images with better sharpness and
textures than baseline models. See also Appendix D.3 for
detailed discussions.
3.3. Analysis
To examine the effectiveness of our design philosophy,
we conduct two groups of ablation studies. Similar to the
main experiment, we also provide both automatic metrics
and intuitive showcases to demonstrate the advantages of
each strategy in ERNIE-ViLG 2.0 here.
Knowledge Enhancement Strategies. In this part, we fo-
cus on the impact of various knowledge enhancement strate-
gies by training a series of lightweight models, with 500M
text encoders, 870M U-Nets, and 500M training samples.
The pareto curves in Figure 5a and convergence curves in
Figure 10 (Appendix D.1) demonstrate that incorporating
knowledge in the learning process brings signiﬁcant perfor-
mance gains in image ﬁdelity, image-text alignment, and
5https://openai.com/dall-e-2/
6https://beta.dreamstudio.ai/dream
7We use DALL-E 2 and Stable Diffusion interfaces to generate images
on October 25, 2022, before the CVPR 2023 submission deadline.

--- Page 7 ---

baseline
1 exp.
w/ txt.
2 exp.
w/ vis.
5 exp.
w/ all
10 exp.
(1) A white car and a red sheep
(2) A panda making latte art
(3) A small red ball in a big green block
(4) A burning ﬁsh
(1) A single clock is sitting on a table
(2) An umbrella on top of a spoon
(3) Wolf in a suit
(4) A rabbit with a fox’s head
Figure 6. Samples from ViLG-300 with different knowledge en-
hancement strategies (left) and different number of experts (right).
For more samples, refer to the Figure 15 and 16 in supplement.
t=1000
t=800
t=800
t=600
t=400
t=200
t=200
t=1
0.010
0.008
0.006
0.004
0.002
0.000
Figure 7. The visualization of cross-attention maps in different
denoising timesteps, where each value in the image space is the
average of attention from this image token to all text tokens.
convergence speed. Speciﬁcally, (1) the beneﬁts of textual
knowledge are mainly reﬂected in precise ﬁne-grained se-
mantic control (w/ textual), (2) only utilizing object
knowledge may not be able to steadily promote the perfor-
mance (w/ object), while taking synthetic descriptions
into consideration is an effective solution to make full use of
visual knowledge (w/ visual). Figure 6 provides more
visual comparisons to intuitively demonstrate the changes
brought by each strategy. When handling complex prompts,
baseline model faces problems such as the absence of key
objects or incorrect assignment of attributes. At this point,
textual knowledge helps the model accurately understand
the attributes of each object, but the generated images some-
times fall into a new problem of distortion. Complementarily,
visual knowledge promotes the generation of high-ﬁdelity
images, but it cannot well understand speciﬁc entities in text.
Eventually, the combination of two kinds of knowledge har-
moniously promotes the model from single- and multi-modal
views, which ensures high ﬁdelity and boost the image-text
alignment in ﬁne-grained visual scene. In Appendix D.1,
we also quantitatively measure the CLIP score improvement
brought by different knowledge sources, which corroborates
the qualitative observation.
Mixture-of-Denoising-Experts Strategies. Based on the
above lightweight settings, we further train the baseline
model with 500M samples, and then train 200M samples
for each denoising expert. Figure 5b shows that with the
increasing number of denoising experts, the overall perfor-
mance is gradually improved, proving that scaling the size
of U-Net is also an effective solution to achieve better image
quality. More showcases are provided in Figure 6. When the
number of experts increases from 1 to 10, the model can not
only better handle the coupling between different elements
but also generate images with more natural textures. For in-
stance, the numbers on clocks become clearer, the proportion
of wolf and suit becomes more harmonious, and the model
can generate more photorealistic pictures instead of cartoon
drawings. We also tried to analyze the impact of the amount
of denoising experts and training samples, and found that us-
ing more expert networks has better performance than using
a network to train more samples (see also Appendix D.2).
Figure 7 further visualizes the cross-attention maps from
image features to text representations in denoising experts
during 1,000-step denoising process, where these steps
shown are denoised by different experts. As shown in the
illustration, attentions of different denoising timesteps vary.
Speciﬁcally, the attention maps of timesteps t near 1,000 are
almost evenly distributed over the whole image, which is be-
cause the input of these steps is close to Gaussian noise and
the image layout is unclear, so all the image tokens have to
attend to the text prompt to generate image skeleton. When
the timesteps are close to 1, attention maps concentrate more
on foreground objects. For these timesteps, the input to de-
noising network is close to the ﬁnal image and the layout
is clear, and only a few parts of the image need to focus on
the text to ﬁll in the details of object. These observations
again illustrate the difference among denoising timesteps
and demonstrate the need to disentangle different timesteps
with multiple experts.
4. Related Work
Text-to-Image Generation. Text-to-image generation is the
task of synthesizing images according to natural language
descriptions. Early works adopted generative adversarial
networks [7] to produce images based on text [36,41,44,47].
Inspired by the success of transformers in generation
tasks [37], models such as ERNIE-ViLG [45], DALL-E [23],
Cogview [2], Make-A-Scene [6], and Parti [43] have also ex-
plored text-to-image generation as a sequence-to-sequence
problem, with auto-regressive transformers as generators
and text/image tokens as input/output sequences. Recently,
another line of works have applied diffusion models [30],
shaping it as an iterative denoising task [9, 27, 31]. By
adding text condition in the denoising steps, practices such as
LDM [25], DALL-E 2 [22], and Imagen [26] constantly set
new records in text-to-image generation. Based on diffusion
models as the backbone, ERNIE-ViLG 2.0 proposes incorpo-
rating knowledge of scene and mixture-of-denoising-experts
mechanism into the denoising process.
Knowledge-Enhanced Pre-trained Models. While trans-
formers beneﬁt from pre-training on large-scale data, many

--- Page 8 ---

attempts have been adding knowledge to guide them to focus
on key elements during learning. For language-based tasks,
knowledge-enhanced models used knowledge masking strat-
egy [11,34] or knowledge-aware pre-training tasks [33,35]
to understand the language data distribution. As for vision-
language multi-modal discrimination models, OSCAR [14],
ERNIE-ViL [42] and ERNIE-Layout [19] leveraged object
tags, scene graphs, and document layouts as extra knowl-
edge to help the models better align language and vision
modalities. Among multi-modal generation models, Make-
A-Scene [6] emphasized the importance of object and face re-
gions by integrating domain-speciﬁc perceptual knowledge.
While current text-to-image diffusion models suffer from at-
tribute misalignment problems [22], they have not employed
any speciﬁc knowledge of objects. Herein, ERNIE-ViLG 2.0
utilizes the knowledge of key elements in images and text
to enhance diffusion models, leading to better ﬁne-grained
image-text alignment in generated pictures.
Mixture-of-Expert. Mixture-of-Experts (MoE) in neural
networks means dividing speciﬁc parts of the parameters
into subsets, each of which is called an expert [4,29]. Dur-
ing the forward pass, a router assigns experts to different
input, and each input only interacts with the experts assigned
to. The router is a critical part of MoE. In language tasks, the
most common strategy is a matching algorithm that assigns
each text token to several experts in the linear feed-forward
layer [5, 8, 12, 24]. While most practices formulate multi-
ple experts in only the linear layers, some works also use
an entire language model as an expert [13]. Beyond the
natural language processing tasks, the idea of MoE have
also been applied to vision models [20] and Mixture-of-
Modality-Expert in multi-modal transformers [17, 39, 40].
In ERNIE-ViLG 2.0, the MoDE mechanism takes multiple
denoising U-Nets as experts. It uses the denoising step index
as the ﬁxed router to determine which expert to use.
5. Risks, Limitations, and Future Work
Model Usage and Data Bias. Text-to-image generation
models trained by large-scale image-text data have all faced
similar risks regarding to inappropriate usage of generation
and data bias [22, 25, 26]. Considering that text-to-image
models help people realize their imagination with less effort,
the malicious use of models may result in unexpected de-
ceptive or harmful outcomes. Moreover, since the models
are trained on datasets consisting of images and their alt-text
crawled from websites, the generated images may exhibit
social and cultural bias in the datasets and websites.
Character Rendering. Figure 8 shows two successful char-
acter rendering cases (a, b) and one failure case (c). Charac-
ter rendering is a challenging task for ERNIE-ViLG 2.0 for
two reasons. First, the training data contains both Chinese
text-image pairs and English text-image pairs translated into
Chinese. When a text prompt mentions characters, the char-
(a) 国风福字挂饰
(b) 生日蛋糕上有蜡烛“20”
(c) 国画葡萄
A hanging ornament with
“福” in Chinese fashion
A birthday cake with
candles of “20” on it
Chinese painting of grapes
Figure 8. Examples of character rendering. The model successfully
renders simple characters speciﬁed in the prompt, while for more
difﬁcult cases, the model only learns the position for now.
acters in the image could be in Chinese or English, and it is
hard for the model to learn corresponding characters in both
languages simultaneously. In the cases of successful charac-
ter rendering that we observed, the characters could be words
that are common in Chinese and do not have an exact match
in English, such as “福” (“blessing, happiness, good luck”
in English) in Figure 8a, or numbers which are the same
in English and Chinese images, such as “20” in Figure 8b.
The second reason that makes character rendering difﬁcult is
probably that Chinese characters are complex combinations
of strokes without basic components like English letters. In
Figure 8c, the model does learn that it should write some
Chinese characters in the top right corner, but it only paints
meaningless strokes there.
Variation of Mixture-of-Denoising-Experts. Section 3.3
shows that using more denoising experts leads to better
model performance. It indicates that using parallel U-Net
experts is an effective way to augment the denoising network.
Due to the computation limitation, we only try using up to
10 experts in this work, while we believe that exploring more
denoising experts and multiple text encoders as experts is a
meaningful future direction. Herein, we can further scale up
the model and allow it to learn data distribution better with
similar inference time.
6. Conclusions
We present ERNIE-ViLG 2.0, the ﬁrst Chinese large-scale
text-to-image generation model based on diffusion models.
To improve the ﬁne-grained control of scene semantics, we
incorporate visual and textual knowledge of the scene into
diffusion models. To disentangle the model parameters for
different denoising timesteps, we introduce MoDE and scale
up the model parameters to 24B with a relatively short infer-
ence time. Experiments show that ERNIE-ViLG 2.0 achieves
state-of-the-art on MS-COCO and each proposed mechanism
contributes to the ﬁnal results. To allow fair comparisons be-
tween Chinese and English text-to-image models, we collect
a bilingual prompt set ViLG-300, and human evaluation indi-
cates that ERNIE-ViLG 2.0 is preferred over strong baselines

--- Page 9 ---

in both text relevancy and image ﬁdelity. Further analysis
suggests that different knowledge sources improve the gen-
eration in different aspects, and using more experts results
in better image quality. In the future, we intend to enrich
external image-text alignment knowledge and expand the
usage of multiple experts to advance the generation. See also
Appendix for more details on training and evaluation.
Acknowledgement
This work was partly supported by
National Natural Science Foundation of China (62271359).
We thank Yehan Zheng for help on dataset collection; Weixin
Liu and Bin Shan for discussions on paper.
References
[1] Peter Anderson, Xiaodong He, Chris Buehler, Damien Teney,
Mark Johnson, Stephen Gould, and Lei Zhang.
Bottom-
up and top-down attention for image captioning and visual
question answering. In 2018 IEEE Conference on Computer
Vision and Pattern Recognition, CVPR 2018, Salt Lake City,
UT, USA, June 18-22, 2018, pages 6077–6086. Computer
Vision Foundation / IEEE Computer Society, 2018. 4, 12
[2] Ming Ding, Zhuoyi Yang, Wenyi Hong, Wendi Zheng,
Chang Zhou, Da Yin, Junyang Lin, Xu Zou, Zhou Shao,
Hongxia Yang, and Jie Tang. Cogview: Mastering text-to-
image generation via transformers. In Marc’Aurelio Ranzato,
Alina Beygelzimer, Yann N. Dauphin, Percy Liang, and Jen-
nifer Wortman Vaughan, editors, Advances in Neural Infor-
mation Processing Systems 34: Annual Conference on Neural
Information Processing Systems 2021, NeurIPS 2021, De-
cember 6-14, 2021, virtual, pages 19822–19835, 2021. 5,
7
[3] Ming Ding, Wendi Zheng, Wenyi Hong, and Jie Tang.
Cogview2: Faster and better text-to-image generation via
hierarchical transformers. CoRR, abs/2204.14217, 2022. 5
[4] William Fedus, Jeff Dean, and Barret Zoph. A review of
sparse expert models in deep learning. CoRR, abs/2209.01667,
2022. 8
[5] William Fedus, Barret Zoph, and Noam Shazeer. Switch
transformers: Scaling to trillion parameter models with simple
and efﬁcient sparsity. CoRR, abs/2101.03961, 2021. 8
[6] Oran Gafni, Adam Polyak, Oron Ashual, Shelly Sheynin,
Devi Parikh, and Yaniv Taigman.
Make-a-scene: Scene-
based text-to-image generation with human priors. CoRR,
abs/2203.13131, 2022. 5, 7, 8, 13
[7] Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing
Xu, David Warde-Farley, Sherjil Ozair, Aaron C. Courville,
and Yoshua Bengio.
Generative adversarial nets.
In
Zoubin Ghahramani, Max Welling, Corinna Cortes, Neil D.
Lawrence, and Kilian Q. Weinberger, editors, Advances in
Neural Information Processing Systems 27: Annual Confer-
ence on Neural Information Processing Systems 2014, Decem-
ber 8-13 2014, Montreal, Quebec, Canada, pages 2672–2680,
2014. 7
[8] Suchin Gururangan, Mike Lewis, Ari Holtzman, Noah Smith,
and Luke Zettlemoyer. Demix layers: Disentangling domains
for modular language modeling. In Marine Carpuat, Marie-
Catherine de Marneffe, and Iván Vladimir Meza Ruíz, editors,
Proceedings of the 2022 Conference of the North American
Chapter of the Association for Computational Linguistics:
Human Language Technologies, NAACL 2022, Seattle, WA,
United States, July 10-15, 2022, pages 5557–5576. Associa-
tion for Computational Linguistics, 2022. 8
[9] Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffu-
sion probabilistic models. In Hugo Larochelle, Marc’Aurelio
Ranzato, Raia Hadsell, Maria-Florina Balcan, and Hsuan-
Tien Lin, editors, Advances in Neural Information Processing
Systems 33: Annual Conference on Neural Information Pro-
cessing Systems 2020, NeurIPS 2020, December 6-12, 2020,
virtual, 2020. 2, 3, 4, 7
[10] Jonathan Ho and Tim Salimans. Classiﬁer-free diffusion
guidance. In NeurIPS 2021 Workshop on Deep Generative
Models and Downstream Applications, 2021. 3
[11] Mandar Joshi, Danqi Chen, Yinhan Liu, Daniel S. Weld,
Luke Zettlemoyer, and Omer Levy. Spanbert: Improving pre-
training by representing and predicting spans. Trans. Assoc.
Comput. Linguistics, 8:64–77, 2020. 8
[12] Dmitry Lepikhin, HyoukJoong Lee, Yuanzhong Xu, Dehao
Chen, Orhan Firat, Yanping Huang, Maxim Krikun, Noam
Shazeer, and Zhifeng Chen. Gshard: Scaling giant models
with conditional computation and automatic sharding. In 9th
International Conference on Learning Representations, ICLR
2021, Virtual Event, Austria, May 3-7, 2021. OpenReview.net,
2021. 8
[13] Margaret Li, Suchin Gururangan, Tim Dettmers, Mike Lewis,
Tim Althoff, Noah A. Smith, and Luke Zettlemoyer. Branch-
train-merge: Embarrassingly parallel training of expert lan-
guage models. CoRR, abs/2208.03306, 2022. 8
[14] Xiujun Li, Xi Yin, Chunyuan Li, Pengchuan Zhang, Xiaowei
Hu, Lei Zhang, Lijuan Wang, Houdong Hu, Li Dong, Furu
Wei, Yejin Choi, and Jianfeng Gao. Oscar: Object-semantics
aligned pre-training for vision-language tasks. In Andrea
Vedaldi, Horst Bischof, Thomas Brox, and Jan-Michael
Frahm, editors, Computer Vision - ECCV 2020 - 16th Euro-
pean Conference, Glasgow, UK, August 23-28, 2020, Proceed-
ings, Part XXX, volume 12375 of Lecture Notes in Computer
Science, pages 121–137. Springer, 2020. 8
[15] Ilya Loshchilov and Frank Hutter. Decoupled weight decay
regularization. In 7th International Conference on Learning
Representations, ICLR 2019, New Orleans, LA, USA, May
6-9, 2019. OpenReview.net, 2019. 5
[16] Gary Marcus, Ernest Davis, and Scott Aaronson. A very
preliminary analysis of DALL-E 2. CoRR, abs/2204.13807,
2022. 13
[17] Basil Mustafa, Carlos Riquelme, Joan Puigcerver, Rodolphe
Jenatton, and Neil Houlsby. Multimodal contrastive learning
with limoe: the language-image mixture of experts. CoRR,
abs/2206.02770, 2022. 8
[18] Alexander Quinn Nichol, Prafulla Dhariwal, Aditya Ramesh,
Pranav Shyam, Pamela Mishkin, Bob McGrew, Ilya Sutskever,
and Mark Chen. GLIDE: towards photorealistic image gener-
ation and editing with text-guided diffusion models. In Kama-
lika Chaudhuri, Stefanie Jegelka, Le Song, Csaba Szepesvári,

--- Page 10 ---

Gang Niu, and Sivan Sabato, editors, International Confer-
ence on Machine Learning, ICML 2022, 17-23 July 2022,
Baltimore, Maryland, USA, volume 162 of Proceedings of
Machine Learning Research, pages 16784–16804. PMLR,
2022. 2, 3, 5, 13
[19] Qiming Peng, Yinxu Pan, Wenjin Wang, Bin Luo, Zhenyu
Zhang, Zhengjie Huang, Teng Hu, Weichong Yin, Yongfeng
Chen, Yin Zhang, Shikun Feng, Yu Sun, Hao Tian, Hua Wu,
and Haifeng Wang. Ernie-layout: Layout knowledge en-
hanced pre-training for visually-rich document understanding.
CoRR, abs/2210.06155, 2022. 8
[20] Joan Puigcerver, Carlos Riquelme Ruiz, Basil Mustafa, Cé-
dric Renggli, André Susano Pinto, Sylvain Gelly, Daniel
Keysers, and Neil Houlsby. Scalable transfer learning with
expert models. In 9th International Conference on Learning
Representations, ICLR 2021, Virtual Event, Austria, May 3-7,
2021. OpenReview.net, 2021. 8
[21] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya
Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry,
Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen
Krueger, and Ilya Sutskever. Learning transferable visual
models from natural language supervision. In Marina Meila
and Tong Zhang, editors, Proceedings of the 38th Interna-
tional Conference on Machine Learning, ICML 2021, 18-24
July 2021, Virtual Event, volume 139 of Proceedings of Ma-
chine Learning Research, pages 8748–8763. PMLR, 2021.
6
[22] Aditya Ramesh, Prafulla Dhariwal, Alex Nichol, Casey Chu,
and Mark Chen. Hierarchical text-conditional image genera-
tion with CLIP latents. CoRR, abs/2204.06125, 2022. 2, 5, 6,
7, 8, 12, 13
[23] Aditya Ramesh, Mikhail Pavlov, Gabriel Goh, Scott Gray,
Chelsea Voss, Alec Radford, Mark Chen, and Ilya Sutskever.
Zero-shot text-to-image generation. In Marina Meila and
Tong Zhang, editors, Proceedings of the 38th International
Conference on Machine Learning, ICML 2021, 18-24 July
2021, Virtual Event, volume 139 of Proceedings of Machine
Learning Research, pages 8821–8831. PMLR, 2021. 5, 7, 13
[24] Stephen Roller, Sainbayar Sukhbaatar, Arthur Szlam, and
Jason Weston.
Hash layers for large sparse models.
In
Marc’Aurelio Ranzato, Alina Beygelzimer, Yann N. Dauphin,
Percy Liang, and Jennifer Wortman Vaughan, editors, Ad-
vances in Neural Information Processing Systems 34: Annual
Conference on Neural Information Processing Systems 2021,
NeurIPS 2021, December 6-14, 2021, virtual, pages 17555–
17566, 2021. 8
[25] Robin Rombach, Andreas Blattmann, Dominik Lorenz,
Patrick Esser, and Björn Ommer. High-resolution image syn-
thesis with latent diffusion models. CoRR, abs/2112.10752,
2021. 2, 5, 7, 8, 13
[26] Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li, Jay
Whang, Emily Denton, Seyed Kamyar Seyed Ghasemipour,
Burcu Karagol Ayan, S. Sara Mahdavi, Rapha Gontijo Lopes,
Tim Salimans, Jonathan Ho, David J. Fleet, and Mohammad
Norouzi. Photorealistic text-to-image diffusion models with
deep language understanding. CoRR, abs/2205.11487, 2022.
2, 5, 6, 7, 8, 12, 13
[27] Tim Salimans and Jonathan Ho. Progressive distillation for
fast sampling of diffusion models. In The Tenth International
Conference on Learning Representations, ICLR 2022, Virtual
Event, April 25-29, 2022. OpenReview.net, 2022. 7
[28] Christoph Schuhmann, Richard Vencu, Romain Beaumont,
Robert Kaczmarczyk, Clayton Mullis, Aarush Katta, Theo
Coombes, Jenia Jitsev, and Aran Komatsuzaki.
LAION-
400M: open dataset of clip-ﬁltered 400 million image-text
pairs. CoRR, abs/2111.02114, 2021. 5
[29] Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy
Davis, Quoc V. Le, Geoffrey E. Hinton, and Jeff Dean. Outra-
geously large neural networks: The sparsely-gated mixture-
of-experts layer. In 5th International Conference on Learning
Representations, ICLR 2017, Toulon, France, April 24-26,
2017, Conference Track Proceedings. OpenReview.net, 2017.
8
[30] Jascha Sohl-Dickstein, Eric A. Weiss, Niru Maheswaranathan,
and Surya Ganguli.
Deep unsupervised learning using
nonequilibrium thermodynamics. In Francis R. Bach and
David M. Blei, editors, Proceedings of the 32nd International
Conference on Machine Learning, ICML 2015, Lille, France,
6-11 July 2015, volume 37 of JMLR Workshop and Confer-
ence Proceedings, pages 2256–2265. JMLR.org, 2015. 3,
7
[31] Jiaming Song, Chenlin Meng, and Stefano Ermon. Denoising
diffusion implicit models. In 9th International Conference on
Learning Representations, ICLR 2021, Virtual Event, Austria,
May 3-7, 2021. OpenReview.net, 2021. 3, 7
[32] Yang Song, Jascha Sohl-Dickstein, Diederik P. Kingma, Ab-
hishek Kumar, Stefano Ermon, and Ben Poole. Score-based
generative modeling through stochastic differential equations.
In 9th International Conference on Learning Representations,
ICLR 2021, Virtual Event, Austria, May 3-7, 2021. OpenRe-
view.net, 2021. 3
[33] Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao
Pang, Junyuan Shang, Jiaxiang Liu, Xuyi Chen, Yanbin
Zhao, Yuxiang Lu, Weixin Liu, Zhihua Wu, Weibao Gong,
Jianzhong Liang, Zhizhou Shang, Peng Sun, Wei Liu, Xuan
Ouyang, Dianhai Yu, Hao Tian, Hua Wu, and Haifeng
Wang. ERNIE 3.0: Large-scale knowledge enhanced pre-
training for language understanding and generation. CoRR,
abs/2107.02137, 2021. 8
[34] Yu Sun, Shuohuan Wang, Yu-Kun Li, Shikun Feng, Xuyi
Chen, Han Zhang, Xin Tian, Danxiang Zhu, Hao Tian, and
Hua Wu. ERNIE: enhanced representation through knowl-
edge integration. CoRR, abs/1904.09223, 2019. 8
[35] Yu Sun, Shuohuan Wang, Yu-Kun Li, Shikun Feng, Hao
Tian, Hua Wu, and Haifeng Wang. ERNIE 2.0: A contin-
ual pre-training framework for language understanding. In
The Thirty-Fourth AAAI Conference on Artiﬁcial Intelligence,
AAAI 2020, The Thirty-Second Innovative Applications of
Artiﬁcial Intelligence Conference, IAAI 2020, The Tenth AAAI
Symposium on Educational Advances in Artiﬁcial Intelligence,
EAAI 2020, New York, NY, USA, February 7-12, 2020, pages
8968–8975. AAAI Press, 2020. 8
[36] Ming Tao, Hao Tang, Fei Wu, Xiaoyuan Jing, Bing-Kun Bao,
and Changsheng Xu. DF-GAN: A simple and effective base-
line for text-to-image synthesis. In IEEE/CVF Conference on

--- Page 11 ---

Computer Vision and Pattern Recognition, CVPR 2022, New
Orleans, LA, USA, June 18-24, 2022, pages 16494–16504.
IEEE, 2022. 7
[37] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkor-
eit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia
Polosukhin. Attention is all you need. In Isabelle Guyon,
Ulrike von Luxburg, Samy Bengio, Hanna M. Wallach, Rob
Fergus, S. V. N. Vishwanathan, and Roman Garnett, editors,
Advances in Neural Information Processing Systems 30: An-
nual Conference on Neural Information Processing Systems
2017, December 4-9, 2017, Long Beach, CA, USA, pages
5998–6008, 2017. 7
[38] Peng Wang, An Yang, Rui Men, Junyang Lin, Shuai Bai,
Zhikang Li, Jianxin Ma, Chang Zhou, Jingren Zhou, and
Hongxia Yang. OFA: unifying architectures, tasks, and modal-
ities through a simple sequence-to-sequence learning frame-
work. In Kamalika Chaudhuri, Stefanie Jegelka, Le Song,
Csaba Szepesvári, Gang Niu, and Sivan Sabato, editors, In-
ternational Conference on Machine Learning, ICML 2022,
17-23 July 2022, Baltimore, Maryland, USA, volume 162 of
Proceedings of Machine Learning Research, pages 23318–
23340. PMLR, 2022. 4
[39] Wenhui Wang, Hangbo Bao, Li Dong, Johan Bjorck, Zhiliang
Peng, Qiang Liu, Kriti Aggarwal, Owais Khan Mohammed,
Saksham Singhal, Subhojit Som, and Furu Wei. Image as a
foreign language: Beit pretraining for all vision and vision-
language tasks. CoRR, abs/2208.10442, 2022. 8
[40] Wenhui Wang, Hangbo Bao, Li Dong, and Furu Wei.
Vlmo: Uniﬁed vision-language pre-training with mixture-
of-modality-experts. CoRR, abs/2111.02358, 2021. 8
[41] Tao Xu, Pengchuan Zhang, Qiuyuan Huang, Han Zhang,
Zhe Gan, Xiaolei Huang, and Xiaodong He. Attngan: Fine-
grained text to image generation with attentional generative
adversarial networks. In 2018 IEEE Conference on Computer
Vision and Pattern Recognition, CVPR 2018, Salt Lake City,
UT, USA, June 18-22, 2018, pages 1316–1324. Computer
Vision Foundation / IEEE Computer Society, 2018. 7
[42] Fei Yu, Jiji Tang, Weichong Yin, Yu Sun, Hao Tian, Hua
Wu, and Haifeng Wang. Ernie-vil: Knowledge enhanced
vision-language representations through scene graphs. In
Thirty-Fifth AAAI Conference on Artiﬁcial Intelligence, AAAI
2021, Thirty-Third Conference on Innovative Applications of
Artiﬁcial Intelligence, IAAI 2021, The Eleventh Symposium on
Educational Advances in Artiﬁcial Intelligence, EAAI 2021,
Virtual Event, February 2-9, 2021, pages 3208–3216. AAAI
Press, 2021. 2, 8
[43] Jiahui Yu, Yuanzhong Xu, Jing Yu Koh, Thang Luong, Gunjan
Baid, Zirui Wang, Vijay Vasudevan, Alexander Ku, Yinfei
Yang, Burcu Karagol Ayan, Ben Hutchinson, Wei Han, Zarana
Parekh, Xin Li, Han Zhang, Jason Baldridge, and Yonghui
Wu. Scaling autoregressive models for content-rich text-to-
image generation. CoRR, abs/2206.10789, 2022. 5, 7, 12,
13
[44] Han Zhang, Jing Yu Koh, Jason Baldridge, Honglak Lee, and
Yinfei Yang. Cross-modal contrastive learning for text-to-
image generation. In IEEE Conference on Computer Vision
and Pattern Recognition, CVPR 2021, virtual, June 19-25,
2021, pages 833–842. Computer Vision Foundation / IEEE,
2021. 7
[45] Han Zhang, Weichong Yin, Yewei Fang, Lanxin Li, Boqiang
Duan, Zhihua Wu, Yu Sun, Hao Tian, Hua Wu, and Haifeng
Wang. Ernie-vilg: Uniﬁed generative pre-training for bidi-
rectional vision-language generation. CoRR, abs/2112.15283,
2021. 5, 6, 7, 12, 13
[46] Yufan Zhou, Ruiyi Zhang, Changyou Chen, Chunyuan Li,
Chris Tensmeyer, Tong Yu, Jiuxiang Gu, Jinhui Xu, and Tong
Sun. LAFITE: towards language-free training for text-to-
image generation. CoRR, abs/2111.13792, 2021. 5
[47] Minfeng Zhu, Pingbo Pan, Wei Chen, and Yi Yang. DM-
GAN: dynamic memory generative adversarial networks for
text-to-image synthesis. In IEEE Conference on Computer
Vision and Pattern Recognition, CVPR 2019, Long Beach, CA,
USA, June 16-20, 2019, pages 5802–5810. Computer Vision
Foundation / IEEE, 2019. 7

--- Page 12 ---

Algorithm 1 Training Process
Require: Paired (image, text) inputs, POS toolkit, object detector.
1: Find keywords in text and salient regions in image.
▷Pre-processing
2: For training step s in (0, 350000]:
▷First stage
3:
Sample a denoising timestep t from [0, 1000),
4:
Optimize both the text encoder and the denoising network.
5: Init 10 denoising networks with current parameters.
6: For training step s in (350000, 440000]:
▷Second stage
7:
Sample a denoising timestep t from [0, 1000),
8:
Optimize the ⌊
t
100 ⌋-th denoising network.
Table 2. Hyperparameters and Conﬁguration of ERNIE-ViLG 2.0.
Text Encoder (Transformer)
Vocab size
21128
Text encoder context
77
Text encoder width
2,048
Text encoder depth
24
Text encoder heads
32
Denoising Network (U-Net)
Noise schedule
linear
Diffusion steps
1,000
Sampling steps
50
Model channels
512
Head channels
64
Channel multiplier
[1,2,3,4]
Attention resolutions
[2,4,8]
ResNet number
3
Dropout
0
A. Detailed Training Process
Algorithm 1 shows the pseudo code for training ERNIE-
ViLG 2.0. With (image, text) pairs as input, we ﬁrst ﬁnd the
keywords in texts with an open-source POS toolkit “jieba”
and salient regions in images with an object detector [1].
These additional information are then used in the knowledge-
enhanced training. The training process consists of two
stages. In the ﬁrst stage, we train a U-Net with 2.2B param-
eters and a text encoder with 1.3B parameters for 350, 000
steps. In the second stage, the text encoder is shared, and
we train 10 denoising experts for 90, 000 steps that inherit
U-Net parameters from the ﬁrst stage. The unaccomplished
hyper-parameters we use for ERNIE-ViLG 2.0 is provided
in Table 2.
B. Detailed Automatic Evaluation
Table 3 presents a detailed comparison on the automatic
evaluation scores, including model sizes and reranking strate-
gies of models. At the end of the ﬁrst training stage, the
FID-30K metric of our 3.5B model with only one denoising
expert is 8.07 (w/o reranking), which is better than DALL-E
2 [22] (10.39) with a similar model size, and worse than
our ﬁnal 24B model with 10 experts (7.23 w/o reranking).
After the complete training process, our 24B model (6.75
w/ 4 reranking images) outperforms Parti [43] (7.23 w/ 16
reranking images) with a similar number of parameters and
a smaller number of reranking images. These comparisons
indicate that both extra knowledge and model scaling con-
tribute to the ﬁnal performance of our model.
C. Detailed Human Evaluation
In this section, we supplement the part about human eval-
uation omitted in main content, including the construction
process of ViLG-300, the performance comparison on vari-
ous categories, and the example qualitative comparison of
different models.
C.1. The Construction of ViLG-300
To construct ViLG-300, we ﬁrst remove the language-
related prompts in DrawBench [26] (text rendering,
rare words, misspelled prompts) and MS-COCO
prompts in ERNIE-ViLG [45], leaving 162 and 398 prompts,
respectively, then randomly sampled 150 prompts from these
two parts, manually translated and proofread these prompts
to achieve the ﬁnal parallel Chinese and English set. Specif-
ically, we remove language-related text prompts in Draw-
Bench since these are not comparable inputs for models in
different languages. For text rendering in Chinese, we also
have discussed in detail in Section 5. We also remove the
MS-COCO category in ERNIE-ViLG, because MS-COCO
has been used in the automatic evaluation, and the prompts
are relatively simple for current text-to-image models, espe-
cially when evaluating the models’ ability to understand com-
plex scene. Note that there are two similar categories (i.e.,
Conflicting and Counterfactual) in DrawBench
and ERNIE-ViLG that we do not align and merge. The rea-
son is that the Conflicting category focuses on the im-
possible combination of things, while Counterfactual
contains many prompts with negative descriptions, both of
which are now difﬁcult problems.
C.2. Detailed Results on ViLG-300
Figure 9 shows the detailed performance comparison be-
tween ERNIE-ViLG 2.0 and DALL-E 2/Stable Diffusion on
ViLG-300, and example qualitative comparisons are shown
in Figure 13 and 14. The most important conclusion is that
ERNIE-ViLG 2.0 is quite skilled in dealing with text prompts
with colors and complex scenes, and also has impressive per-
formance in many categories, such as Geography, Scene,
and Cartoon. Intuitively, we attribute the excellent per-
formance to the knowledge injection that endows the model
with the ability to perceive and understand various named en-
tities and detailed descriptions, as well as the increase in the
number of parameters brought by the mixture-of-denoising-
experts strategies also makes the model even more powerful.

--- Page 13 ---

Table 3. Detailed comparison of ERNIE-ViLG 2.0 and representative text-to-image generation models on MS-COCO 256 × 256 with
zero-shot FID-30k.
Model
#params
FID w/o reranking
FID/#reranking images
DALL-E [23]
12B
34.6
27.5/512
LDM [25]
1.45B
12.61
-
GLIDE [18]
6B
12.24
-
Make-A-Scene [6]
4B
11.84
-
DALL-E 2 [22]
4.5B
10.39
-
Imagen [26]
6.6B
7.27
-
Parti [43]
20B
-
7.23/16
ERNIE-ViLG 2.0 w/ 1 denoising expert
3.5B
8.07
7.62/4
ERNIE-ViLG 2.0 w/ 10 denoising experts
24B
7.23
6.75/4
Table 4. Detailed categories and statistics of ViLG-300.
Source
Category
Description
Number
DrawBench [26]
Color
objects with speciﬁed colors
22
Counting
objects with speciﬁed numbers
18
Positional
objects with speciﬁed spatial positioning
16
Conﬂicting
objects with conﬂicting interactions
10
Description
complex and long prompts describing an objects
20
DALL-E case
prompts from DALL-E [23]
19
Marcus
prompts from Marcus et al. [16]
9
Reddit
prompts from DALL-E 2 Reddit
36
ERNIE-ViLG [45]
Simple
single-object with speciﬁed attributes
18
Complex
multi-objects with speciﬁed attributes and relationships
23
Counterfactual
objects with impossible interactions or negative words
23
Geography
speciﬁc geographic entities
24
View
objects with speciﬁed view angles
16
Scene
objects with speciﬁed time and scenes
14
Style
objects with speciﬁed styles
16
Cartoon
anthropomorphic animals or cartoon characters
16
At the same time, we also propose that further understanding
of the number of objects and the relationship between them
can be the focus of future text-to-image models.
D. Detailed Ablation Study
Here we attach more analysis to the ablation study and
more showcases in Figure 15,16.
D.1. Knowledge Enhancement Ablation
Figure 10 provides the convergence curves of various
models, it is obvious that the knowledge enhancement strate-
gies signiﬁcantly accelerate the convergence process of diffu-
sion models. Notably, at the very beginning of training, the
knowledge-enhanced model reaches or even exceeds the per-
formance that the baseline model with two times of training
samples (i.e., 100M v.s. 200M, 200M v.s. 400M).
To quantitatively measure the improvement brought by
each knowledge source, we calculate the CLIP score between
ViLG-300 prompts and generated images8. Table 5 presents
the top ﬁve categories with maximum performance gain of
each strategy against baseline. It can be found that differ-
ent strategies result in improvements in different categories,
indicating that they help model absorb knowledge and im-
prove text-image alignment in complementary aspects. In
addition, we also notice that CLIP could not well capture the
relationships between multiple objects (e.g., counterfactual),
so we leave the accurate automatic evaluation method for
ﬁne-grained semantic control as a valuable future work.
D.2. Mixture-of-Denoising-Experts Ablation
To explore the impact of training samples or model size
(i.e., the number of denoising experts) on performance, we
train the setting of 1 expert with 400M/1B/2B samples
following Section 3.3, which aligns with the number of sam-
8We feed ERNIE-ViLG 2.0 with Chinese prompts and calculate the
CLIP score between generated images and corresponding English prompts.

--- Page 14 ---

Table 5. Top ﬁve ViLG-300 categories with the maximum CLIP Score improvement for each knowledge enhancement strategy.
No.
w/ textual
w/ visual
w/ all
Prompt category
∆CLIP Score
Prompt category
∆CLIP Score
Prompt category
∆CLIP Score
1
Counterfactual
0.0051
Counterfactual
0.0080
Complex
0.0074
2
Color
0.0041
Counting
0.0047
Counterfactual
0.0073
3
Marcus
0.0038
Color
0.0035
Cartoon
0.0069
4
Style
0.0022
Cartoon
0.0032
Color
0.0066
5
Positional
0.0018
Complex
0.0016
Style
0.0061
50%
Text-Image Alignment
Color
Counting
Positional
Conflicting
Description
DALL-E
Marcus
Reddit
Simple
Complex
Counterfactual
Geography
View
Scene
Style
Cartoon
50%
Image Fidelity
prefer ViLG 2.0
prefer DALL-E 2
indifferent
(a) ERNIE-ViLG 2.0 v.s. DALL-E 2
50%
Text-Image Alignment
Color
Counting
Positional
Conflicting
Description
DALL-E
Marcus
Reddit
Simple
Complex
Counterfactual
Geography
View
Scene
Style
Cartoon
50%
Image Fidelity
prefer ViLG 2.0
prefer Sta. Diff.
indifferent
(b) ERNIE-ViLG 2.0 v.s. Stable Diffusion
Figure 9. Detailed comparison of ERNIE-ViLG 2.0 and DALL-
E 2/Stable Diffusion on ViLG-300 with human evaluation. We do
not apply any ﬁltering strategy and report the initial results here.
ples trained by 2/5/10 experts. Figure 11 shows that
the performance of 1 expert with 400M and 2 experts
with 200M each is basically equal, while the performance of
1 expert lags behind that of 2 experts as training goes
on. This shows that decoupling the denoising capability of
different stages is an effective strategy, and reasonably scal-
ing the size of U-Net is able to further boost the performance
of text-to-image model.
0
100
200
300
400
500
Training Data (M)
10
15
20
25
FID-10k
0.27
0.28
0.29
0.30
0.31
CLIP Score
baseline
w/ object
w/ textual
w/ visual
w/ all
Figure 10. The convergence curves of various models with knowl-
edge enhancement strategies. We choose guidance scale 3 and 8 to
draw the curves of FID-10k and CLIP Score, respectively.
0.290
0.295
0.300
0.305
0.310
CLIP Score
11
13
15
17
19
21
FID-10k
2 experts
5 experts
10 experts
1 expert x 2
1 expert x 5
1 expert x 10
Figure 11. The performance comparison of different amount of
denoising experts and training samples, and models see the same
number of training samples at comparing points.
D.3. Comparison of Image Quality
Figure 12 compares the image details of ERNIE-ViLG 2.0
and baseline models by zooming in small regions of gener-
ated images. Technically, both ERNIE-ViLG 2.0 and Stable
Diffusion generate image latent representation with diffusion
models conditioned on text. While Stable Diffusion only
produces 512×512 sized images, ERNIE-ViLG 2.0 could
directly output images with 1024×1024 resolution. There-
fore, the magniﬁed parts of ERNIE-ViLG 2.0 are clearer
than those of Stable Diffusion. As for DALL-E 2, it employs
cascaded generation by ﬁrst producing 64×64 images with
text and then scaling it up to 1024×1024 resolution with
two super-resolution models. Although it generates images
of the same resolution as ERNIE-ViLG 2.0, the output of
DALL-E 2 sometimes contains unnatural textures, such as
ﬂuffy trees and rain drops in the magniﬁed regions. Contrary
to DALL-E 2, the textures of our model’s outcome are more
natural and photorealistic.

--- Page 15 ---

Stable Diffusion
DALLE-2
ERNIE-ViLG 2.0
青山绿水小船风景
雨中跳舞的小狗
Green mountains, green waters, boats, scenery
A puppy dancing in the rain
Figure 12. Comparison of image quality by magnifying parts of generated images. ERNIE-ViLG 2.0 enables the generation of sharper
1024×1024 images with more natural details.

--- Page 16 ---

一个绿色的杯子和一个蓝色的手机
一个红酒杯放在一条狗上面
A green cup and a blue cell phone
A wine glass on top of a dog
ERNIE-ViLG 2.0
DALL-E 2
Stable Diffusion
Figure 13. Example qualitative comparisons between ERNIE-ViLG 2.0 and DALL-E 2/Stable Diffusion on DrawBench prompts from
ViLG-300.

--- Page 17 ---

锅里煮着粽子和玉米
樱花数字油画
Zongzi and corn boiled in the pot
Cherry blossom, digital oil painting
ERNIE-ViLG 2.0
DALL-E 2
Stable Diffusion
Figure 14. Example qualitative comparisons between ERNIE-ViLG 2.0 and DALL-E 2/Stable Diffusion on ERNIE-ViLG prompts from
ViLG-300.

--- Page 18 ---

baseline
w/ textual
w/ visual
w/ all
一本黄色的书
和一个红色的
花瓶
一辆白色的汽
车和一只红色
的羊
制作拿铁拉花
的熊猫
熊猫宝宝戴着
红帽子、蓝手
套，穿着绿衬
衫和蓝裤子的
表情符号
日落时分，达
斯·维德在火
星上与浣熊
玩耍
客厅的沙发前
有一张木质茶
几
一个小红球在
一个大绿块
内部
身上着火的
鱼
A yellow book
and a red vase.
A white car and
a red sheep.
A panda making
latte art.
An emoji of a
baby panda
wearing
a red hat,
blue gloves,
green shirt,
and blue pants.
Darth Vader
playing with
raccoon in Mars
during sunset.
There is a
wooden tea
table in front
of the sofa
in the
living room
A small red ball
in a large
green block
A burning
ﬁsh
Figure 15. Samples from ViLG-300 with different knowledge enhancement strategies. It can be found that the impacts of textual and visual
knowledge do not seem to overlap, and the combination of them is an effective solution to facilitate accurate semantic control and high
image ﬁdelity.

--- Page 19 ---

1 expert
2 experts
5 experts
10 experts
桌子上放着一
只闹钟
三个立方体的
堆叠。红色在
上，红色在
中，绿色在下
切成七块排列
成一个环的梨
勺子上的伞
穿西服的狼
跳上桌子玩杯
子的布偶猫
一只狗在看书，
很厚的书
狐狸脑袋的
兔子
A single clock
is sitting
on a table
A stack of 3
cubes. The red
is on the top,
The red is
in the middle,
The green is
on the bottom
A pear cut
into seven
pieces arranged
in a ring
An umbrella
on top of
a spoon
Wolf in
a suit
A puppet cat
jumping on
the table to
play with cups
A dog is
reading a
thick book
A rabbit
with a
fox’s head
Figure 16. Samples from ViLG-300 with different number of denoising experts. When increasing the experts, the most noticeable evolution
is that the texture of generated image becomes more natural and photorealistic. Limited by the layout, we simplify the prompt in the second
column, and the input received by model actually is “三个立方体堆叠。一个红色立方体在顶部，放在一个红色立方体上。这个红色
立方体在中间，放在一个绿色立方体上。这个绿色立方体在底部。(A stack of 3 cubes. A red cube is on the top, sitting on a red cube.
The red cube is in the middle, sitting on a green cube. The green cube is on the bottom.)”.

```
