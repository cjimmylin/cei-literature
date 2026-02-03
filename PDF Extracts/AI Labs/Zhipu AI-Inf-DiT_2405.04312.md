---
title: "Inf DiT 2405.04312"
source_pdf: "AI Labs/Zhipu AI/Papers/Inf-DiT_2405.04312.pdf"
company: "Zhipu AI"
pages: 24
extracted_at: "2026-01-31T17:32:39.147102"
type: "ai_lab_paper"
---

# Inf DiT 2405.04312

**Company/Lab:** Zhipu AI
**Source PDF:** AI Labs/Zhipu AI/Papers/Inf-DiT_2405.04312.pdf
**Total Pages:** 24

---

## Content

```
--- Page 1 ---

Inf-DiT: Upsampling Any-Resolution Image with
Memory-Efficient Diffusion Transformer
Zhuoyi Yang1,⋆, Heyang Jiang1, Wenyi Hong1, Jiayan Teng1
Wendi Zheng1, Yuxiao Dong1, Ming Ding2, and Jie Tang1,⋆⋆
1 Tsinghua University 2 Zhipu.AI
Fig. 1: Selected ultra-high-resolution upsampling examples of Inf-DiT, based on SDXL,
DALL-E 3, and real images.
Abstract. Diffusion models have shown remarkable performance in im-
age generation in recent years. However, due to a quadratic increase
in memory during generating ultra-high-resolution images (e.g. 4096 ×
4096), the resolution of generated images is often limited to 1024×1024.
In this work. we propose a unidirectional block attention mechanism that
can adaptively adjust the memory overhead during the inference process
and handle global dependencies. Building on this module, we adopt the
DiT structure for upsampling and develop an infinite super-resolution
model capable of upsampling images of various shapes and resolutions.
Comprehensive experiments show that our model achieves SOTA perfor-
mance in generating ultra-high-resolution images in both machine and
⋆Done as intern at Zhipu AI, yangzy22@mails.tsinghua.edu.cn
⋆⋆Corresponding author jietang@tsinghua.edu.cn
arXiv:2405.04312v2  [cs.CV]  8 May 2024

--- Page 2 ---

2
Yang et al.
human evaluation. Compared to commonly used UNet structures, our
model can save more than 5× memory when generating 4096 × 4096
images. The project URL is https://github.com/THUDM/Inf-DiT.
Keywords: diffusion model · ultra-high-resolution generation · super-
resolution
1
Introduction
1024 2048
4096
8192
Resolution
10000
20000
30000
40000
50000
60000
70000
80000
Memory (MB)
OOM
Memory Usage vs. Resolution
SDXL
Ours
Fig. 2: Comparison of memory us-
age during inference at different
resolutions between our model and
the SDXL architecture.
Recent years have witnessed rapid advance-
ments in diffusion models, which significantly
propelling the field of image generation and
editing forward. Despite the advancements,
a critical limitation persists: the resolution
of images produced by existing image diffu-
sion models is generally confined to 1024 ×
1024 pixels or lower, posing a significant
challenge for generating ultra-high-resolution
images, which are indispensable in various
real-world applications including intricate de-
sign projects, advertising, and the creation of
posters and wallpapers, etc.
A commonly used approach for generat-
ing high resolution is cascaded generation [12],
which first produces a low-resolution image, then applies multiple upsampling
models to increase the image’s resolution step by step. This approach breaks
down the generation of high-resolution images into multiple tasks. Based on the
results generated in the previous stage, the models in the later stages only need
to perform local generation. Building upon the cascaded structure, both DALL-
E2 [21] and Imagen [23] can effectively generate images with 1024 resolution.
The biggest challenge for upsampling to much higher resolution images is the
significant GPU memory demands. For example, if utilizing the widely-adopted
U-Net architecture such as SDXL [18] for image inference (see Figure 2), we ob-
serve a dramatic escalation in memory consumption with increasing resolution.
Specifically, generating a 4096×4096 resolution image, which comprises over 16
million pixels requires more than 80GB of memory, exceeding the capacities of
standard RTX 4090 or A100 graphics cards. Furthermore, the process of train-
ing models for high-resolution image generation exacerbates these demands, as
it necessitates additional memory for storing gradients, optimizer states, etc.
LDM [21] reduces the memory consumption by utilizing Variational Autoen-
coder(VAE) to compress images and generating images in a smaller latent space.
However, it is also emphasized that an excessively high compression ratio can
substantially deteriorate the quality of generation, imposing severe limitations
on the reduction of memory consumption.
We observe that one common and critical problem among the aforementioned
models is the necessity to input the entire image to the model, which requires

--- Page 3 ---

Inf-DiT
3
keeping O(N 2) hidden states in memory, where N is the width(height) of the
image. Based on this observation, we propose a Unidirectional Block Attention
(UniBA) algorithm that can dramatically reduce the space complexity of gen-
eration from O(N 2) to O(N), increasing the highest available resolution for a
large margin (Fig. 2). Specifically, in every diffusion step, we split the image
into blocks and perform a sequential batch generation order among them, where
each batch simultaneously produces a subset of the blocks, and any amount of
blocks can be generated in parallel as long as the memory restriction allows. It is
worth noting that, though the model only inputs part of image into the model at
the same time, UniBA successfully preserves the ability to interact with hidden
states of faraway blocks and maintain high-level semantic consistency. This is
different from other block-based generation methods such as [2,14,29] that only
interact with blocks in pixel space or compressed latent space.
Based on this algorithm, we optimize diffusion transformer (DiT) and train
a model named Inf-DiT, which is capable of upsampling images of varying reso-
lution and shape. Furthermore, we design several techniques including providing
global image embedding to enhance the global semantic consistency and offer
zero-shot text control ability, and provision of all neighboring low-resolution(LR)
blocks through cross-attention mechanisms to further enhance the local consis-
tency. Evaluation results show that Inf-DiT achieved significantly superior re-
sults compared to other high-resolution generative models in both machine and
human evaluation.
To summarize, our main contributions are as follows:
1. We propose Unidirectional Block Attention (UniBA) algorithm, which re-
duces the minimum memory consumption from O(N 2) to O(N) during in-
ference, where N represents the edge length. This mechanism is also capable
of adapting to various memory restrictions by adjusting the number of blocks
generated in parallel, trading off between memory and time overhead.
2. Based on these methods, we train an image upsampling diffusion model,
Inf-DiT, a 700M model capable of upsampling images of varying resolutions
and shapes. Inf-DiT achieves state-of-the-art performance in both machine
(HPDv2 and DIV2K datasets) and human evaluation.
3. We design multiple techniques to further enhance local and global consis-
tency, and offer a zero-shot ability for flexible text control.
2
Methodology
2.1
Unidirectional Block Attention (UniBA)
We observe that the critical obstacle for generating ultra-high resolution images
is memory limitation. As the resolution of the image increases, the corresponding
hidden state’s size within the network expands quadratically. For example, a
single hidden state with the shape of 2048 × 2048 × 1280 in only one layer
requires 20GB of memory, making it formidable to generate very large images.

--- Page 4 ---

4
Yang et al.
Fig. 3: Left: Unidirectional block attention. In our implementation, each block directly
depends on the three blocks in each layer: the blocks in the upper left corner, on the
left, and on the top. Right: The inference process of Inf-DiT. Inf-DiT generates n × n
block each time, based on the memory size. During this process, only the KV-cache of
the blocks that subsequent blocks depend on are stored in memory.
How to avoid storing the entire image’s hidden state in memory becomes the
key issue.
Our main idea is to divide an image x ∈RH×W ×C into blocks xb ∈Rh×w×B2×C
, where B is block size and h = H
B , w = W
B . When the image is fed into the net-
work, the channel size and resolution of a block may change, but the layout and
the relative positional relationships between blocks will remain unchanged. If
there is a way to apply sequential batch generation of blocks where each batch
simultaneously produces a subset of the blocks, only a small number of block
hidden states have to be kept in memory simultaneously, making it possible to
generate ultra-high-resolution images.
Here we define that blockA is dependent on blockB if the generation of blockA
involves the hidden state of blockB in computation. It can be observed that
the dependencies between blocks are bidirectional in most previous structures
(UNet, DiT, etc.), in which case all blocks in the image must be generated
simultaneously. Take UNet as an example: two adjacent elements in neighboring
blocks use each other’s hidden state in the convolution operation, therefore all
pairs of neighboring blocks must be generated simultaneously. Given the aim
to save the memory of blocks’ hidden states, we hope to devise an algorithm
that allows the blocks in the same image to be divided into several batches for
generation, with each batch only needing to generate a portion of the blocks at
the same time, and the batches are generated in sequence. Generally, an image
generation algorithm can perform such a sequential batch generation among
blocks if it meets the following conditions:
1. The generative dependency between blocks are unidirectional, and can form
a directed acyclic graph (DAG).
2. Each block has only a few direct (1st-order) dependencies on other blocks,
since the hidden states of the block and its direct dependencies should si-
multaneously be kept in the memory.
Furthermore, to ensure consistency across the whole image, it also required that
the blocks have a large enough receptive field to manage long-range dependencies.

--- Page 5 ---

Inf-DiT
5
According to the conditions and analysis above, we choose an efficient im-
plementation illustrated in Fig. 3, Unidirectional Block Attention(UniBA). For
each layer, every block directly depends on three 1st-order neighboring blocks:
the block on the top, on the left, and in the upper left corner. For example, if we
adopt Diffusion Transformer (DiT) architecture which is the base architecture of
Inf-DiT, the dependency between blocks is attention operation, where the query
vectors of each block interact with the key, value vectors of 4 blocks: 3 blocks
located to its upper left and itself, illustrated in Fig. 3.
Formally, the UniBA process in the transformer can be formulated as
  \b
m {Q} &= \bm {z}^n_{(i, j)} \bm {W}^Q , \\ \bm {K} &= [\bm {z}^n_{(i, j)}+\bm {P}_1 ; \bm {z}^n_{(i-1, j)} + \bm {P}_2; \bm {z}^n_{(i, j-1)} + \bm {P}_3; \bm {z}^n_{(i-1, j-1)} + \bm {P}_4]\bm {W}^K , \\ \bm {V} &= [\bm {z}^n_{(i, j)} ; \bm {z}^n_{(i-1, j)}; \bm {z}^n_{(i, j-1)}; \bm {z}^n_{(i-1, j-1)}]\bm {W}^V , \\ \bm {z}^{n+1}_{(i,j)} &= \text {FFN}(\text {Attention}(\bm {Q},\bm {K},\bm {V})) ,
(4)
where zn
(i,j) is the hidden states of the block at row i, column j in layer n,and
Pi is the block-level relative position encoding. We also implement an efficient
approach to apply UniBA for full image in pytorch style, which is attached in
the Appendix A.
Note that, though each block only attends to a few number of neighboring
blocks in each layer, as features propagate layer by layer, blocks can indirectly
interact with faraway blocks, thereby capturing both long- and short-range re-
lationships. Our design shares a similar spirit with the natural language model
Transformer-XL [4], which can be viewed as a special form of ours in one dimen-
sion case.
Inference process with O(N) Memory Consumption Although our method
can generate each block sequentially, it differs from auto-regressive generative
models, in which the next block depends on the final output of the previous
block. Any number of blocks can also be generated in parallel in our model, as
long as the union of their dependent blocks has been generated. Based on this
property, we implement a simple but effective inference process. As illustrated
in Fig. 3, we generate n × n blocks at once, from the top-left to bottom-right.
After generating a set of blocks, we discard hidden states i.e. KV-cache that are
no longer used and append newly generated KV-cache to the memory.
It can be easily proved that the number of block KV-cache retained in mem-
ory during the process is always ≤w + n. Assume the space needed by the
model when generating a single block is M1, the space for one block’s KV-
cache is M2, and other essential space consumption (such as storing the raw
input image) is C, then the maximum space usage of the inference process is
n2M1 + (w + n)M2 + C. When n is much smaller than w, the memory consump-
tion is directly proportional to w. If w is bigger than h, we can easily change the
trajectory of generation to column-major.
In practical terms, despite the total FLOPs of image generation remaining
constant for various values of n, due to the overhead such as operator initial-

--- Page 6 ---

6
Yang et al.
ization time and memory allocation time, the generation time decreases when n
increases. Therefore, it’s optimal to choose the largest n allowed by the memory
limitation.
2.2
Basic Model Architecture
Fig. 4: (Left) Overall architecture of Inf-DiT. (Right) The inner structure of Inf-DiT
block. We do not depict the Layernorm that originally existed in the DiT for simplicity.
Figure 4 provides an overview of our model, Inf-DiT’s architecture. The
model uses a similar backbone as DiT [17], which applies Vision Transformer
(ViT) [6] to diffusion models and proves its efficacy and scalability. In addition
to its superior performance, compared to convolution-based architectures such as
UNet [22], DiT solely utilizes attention as the mechanism of interaction among
patches, which can conveniently implement unidirectional block attention. To
adapt to unidirectional block attention and enhance the performance of upsam-
pling, we make several modifications and optimizations detailed as follows.
Model input Inf-DiT first partitions input images into multiple non-overlapping
blocks, which are further divided into patches with a side length equal to the patch
size. Unlike DiT, considering the compression loss such as color shifting and de-
tail loss, the patchifying of Inf-DiT is conducted in RGB pixel space instead of
latent space. In the case of super-resolution by f times, Inf-DiT first upsamples
the low-resolution RGB image condition by a factor of f, then concatenates it
with the diffusion’s noised input on the feature dimension before feeding it to
the model.
Position Encoding Unlike UNet-based diffusion models [21] that can perceive
positional relationships through convolution operations, all operations including
self-attention, FFN in transformers are permutation invariant functions. There-
fore, transformer-based models require auxiliary input of explicit positional in-
formation to learn the relationships among patches. As recent research in LLMs

--- Page 7 ---

Inf-DiT
7
has shown that relative positional encoding is more effective in capturing word
position relevance compared to absolute positional encoding, we refer to the de-
sign of Rotary Positional Encoding (RoPE) [28], which performs well in the long
context generation, and adapt it into two-dimensional form for image genera-
tion. Specifically, we divide channels of hidden states in half, one for encoding
the x-coordinate and the other for the y-coordinate, and apply RoPE in both
halves.
We create a sufficiently large rope positional encoding table to ensure it
meets the requirements during generation. To ensure all parts of the positional
encoding table can be seen by the model during training, we employ the Random
Starting Point: For each training image, we randomly assign a position (x, y) for
the top-left corner of the image, instead of the default (0, 0).
In addition, considering the difference in interactions within the same block
and between different blocks, we additionally introduce block-level relative posi-
tion encoding P1∼4, which assigns a distinct learnable embedding based on the
relative position before attention.
2.3
Global and Local Consistency
Global Consistency with CLIP Image Embedding The global semantic
information within low-resolution (LR) images, such as artistic style and ob-
ject material, plays a crucial role during upsampling. However, compared to
text-to-image generation models, the upsampling model has an additional task:
understanding and analyzing the semantic information of LR images, which sig-
nificantly increases the model’s burden. This is particularly challenging when
training without text data, as high-resolution images rarely have high-quality
paired texts, making these aspects difficult for the model.
Inspired by DALL·E2 [20], we utilize the image encoder from pre-trained
CLIP [19] to extract image embedding ILR from low-resolution images, which
we refer to as Semantic Input. Since CLIP is trained on massive image-text pairs
from the Internet, its image encoder can effectively extract global information
from low-resolution images. We add the global semantic embedding to the time
embedding of the diffusion transformer and input it into each layer, enabling the
model to learn directly from high-level semantic information.
Another interesting advantage of global semantic embedding is that, using
the aligned image-text latent space in CLIP, we can use text to guide the direction
of generation, even if our model has not been trained on any image-text pairs.
Given a positive prompt Cpos and a negative prompt Cneg, we can update our
image embedding:
  \t i lde {\bm  {I}}_{LR} = \te x t {norm}(\bm {I}_{LR} + \alpha (\text {TextEnc}(C_{pos}) - \text {TextEnc}(C_{neg}))) ,
(5)
where α can control the intensity of the guidance. During inference, we can
simply use ˜ILR in place of ILR as the global semantic embedding to conduct
the control. For example, to get a more clear result set, Cpos = “clear” and
Cneg = “blur” sometimes help.

--- Page 8 ---

8
Yang et al.
Local Consistency with Nearby LR Cross Attention Although concate-
nating the LR image with noised input already provides a good inductive bias
for models to learn the local correspondence between LR and HR images, there
can still be continuity issues. The reason is that, there are several possibilities
of upsampling for a given LR block, which require analysis in conjunction with
several nearby LR blocks to select one solution. Assume that the upsampling is
only performed based on the LR blocks to its left and above, it may select an
HR generation solution that conflicts with the LR block to the right and below.
Then when upsampling the LR block to the right, if the model considers con-
forming to its corresponding LR block more important than being continuous
with the block to the left, a HR block discontinuous with previous blocks would
be generated. A naive solution is to input the entire LR image to every block,
but it’s too costly when the resolution of LR image is also big.
To handle this problem, we introduce Nearby LR Cross Attention. In the first
layer of the transformer, each block conducts cross-attention on the surrounding
3 × 3 LR blocks to capture nearby LR information. Our experiments show that
this approach significantly reduces the probability of generating discontinuous
images. It is worth noting that this operation will not change our inference
process since the entire LR image is known before generation.
We further devise techniques including continuity class-free guidance, LR-
based noise initialization, QK Normalization, etc., which are elaborated in detail
in the Appendix A.
3
Experiments
In this section, we first introduce the detailed training process of Inf-DiT, then
comprehensively evaluate Inf-DiT by both machine and human evaluation. The
results show that Inf-DiT surpasses all baselines, excelling in both ultra-high-
resolution image generation and upsampling tasks. Finally, we conduct ablation
studies to validate the effectiveness of our design.
Table 1: Quantitative comparison results with state-of-the-art methods of ultra-high-
resolution generation on HPDV2 dataset. The best results are marked in bold, and
the second best results are marked by underline.
Method
2048 × 2048
4096 × 4096
Mean ↓
FID ↓
FIDcrop ↓
FID ↓
FIDcrop ↓
Direct Inference
92.2
92.3
OOM
OOM
92.3
MultiDiffusion
99.7
109.3
OOM
OOM
104.5
SDXL+BSRGAN
66.3
81.7
66.0
85.0
74.8
ScaleCrafter
79.9
95.5
115.1
153.3
111.0
DemoFusion
67.5
72.0
70.8
82.6
73.2
SDXL+Inf-DiT(Ours)
66.0
71.9
67.0
76.2
70.3
3.1
Training Details
Datasets Our dataset comprises a subset of LAION-5B [25] with a resolution
higher than 1024×1024 and aesthetic score higher than 5, and 100 thousand high-

--- Page 9 ---

Inf-DiT
9
Table 2: Quantitative comparison results with state-of-the-art methods of super res-
olution on DIV2K dataset. The best results are marked in bold.
Setting
Method
FID ↓
FIDcrop ↓
PSNR ↑
SSIM ↑
Variable resolution
BSRGAN
35.0
143.2
25.9
0.73
Real-ESRGAN
35.5
127.6
25.2
0.72
Inf-DiT(Ours)
20.2
76.5
26.3
0.74
Fix resolution (512x512)
StableSR
74.8
112.6
22.0
0.60
Inf-DiT(Ours)
38.6
83.3
24.6
0.67
Fix resolution (256x256)
LDM
152.6
-
23.9
0.66
Inf-DiT(Ours)
86.8
-
24.6
0.67
resolution wallpapers from the Internet. Following the previous works [20,23,30],
we use fixed-size image crops of 512×512 resolution during training. Since upsam-
pling can be conducted with local information only, it can be directly employed at
higher resolution during inference, which is not easy for most generation models.
Data Processing Since the images generated by diffusion models often contain
residual noise and various detail inaccuracies, it becomes crucial to enhance
the robustness of the upsampling model to address these issues. We adopt the
approach similar to Real-ESRGAN [30] to perform a variety of degradation on
low-resolution input images within the training data.
When processing training images with a resolution higher than 512, there
are two alternative methods: directly performing a random crop, or resizing the
shorter side to 512 before performing a random crop. While the direct cropping
method preserves high-frequency features in high-resolution images, the resize-
then-crop method avoids frequently cropping out areas with a single color back-
ground, which is detrimental to the model’s convergence. Therefore, in practice,
we randomly select from these two processing methods to crop training images.
Training settings During training, We set block size = 128 and patch size = 4,
which means every training image is divided into 4 × 4 blocks and every block
has 32×32 patches. We employ the framework of EDM [15] for training, and set
the upsampling factor to 4×. Because the upsampling task is more concerned
with the high-frequency details of images, we adjusted the mean and std of
training noise distribution to −1.0 and 1.4. To address overflow problem during
training, we employed BF16 format due to its broader numerical range. Our
CLIP model is a ViT-L/16 pre-trained on Datacomp dataset [13]. Since the
CLIP can only process images with 224 × 224 resolution, we first resize LR
images to 224 × 224 and then input them to CLIP. Other hyperparameters are
listed in the Appendix A.
3.2
Machine Evaluation
In this part, we conduct quantitative comparisons of Inf-DiT against state-
of-the-art methodologies on ultra-high-resolution image generation tasks. The

--- Page 10 ---

10
Yang et al.
Direct
Patch
Scalecrafter
BSRGAN
Demofusion
Inf-DiT
Fig. 5: Qualitative comparison of different methods in detail at 2048 × 2048 resolution
Patch
Scalecrafter
BSRGAN
Demofusion
Inf-DiT
Fig. 6: Qualitative comparison of different methods in detail at 4096 × 4096 resolution
baselines encompass two main categories of high-resolution generation: 1. Direct
high-resolution image generation, including Direct Inference of SDXL [18], Mul-
tiDiffusion [2], ScaleCrafter [9], and 2. High-resolution image generation based
on super-resolution techniques, including BSRGAN [33], DemoFusion [7]. We
employ the FID (Fréchet Inception Distance) [10] to evaluate the quality of
ultra-high-resolution generation, which is widely used to evaluate the percep-

--- Page 11 ---

Inf-DiT
11
tual quality of images in image generation tasks [17,21,23]. To further validate
the super-resolution ability of our model, we additionally benchmark it against
renowned super-resolution models over classic super-resolution tasks.
Ultra-High-Resolution Generation We use the test set of HPDv2 [31] for
evaluation. It contains 3200 prompts and is divided into four categories: “An-
imation”, “Concept-art”, “Painting”, and “Photo”. This allows for a comprehen-
sive evaluation of the model’s generative capabilities across various domains and
styles. We test on two resolutions: 20482 and 40962. For super-resolution-based
models, we first use SDXL to generate a 10242 resolution image and upsam-
ple it without text. We use 2× and 4× versions of BSRGAN for 20482 and
40962 generation, respectively. Although Inf-DiT was trained in a setting with
4× upsample, we find that it can generalize well at lower upsampling multiples.
Therefore, for 20482 generation, we directly resize the LR image from 10242 to
20482 and concatenate it with the noise input. We random samples 3200 images
of 20482 and 40962 from LAION-5B as the distribution of real images.
As for the metrics, FID is designed to assess how closely generated images
mimic real image distributions, and has become one of the default metrics in eval-
uating image generation. However, the original implementation of FID needs to
downsample the input image to the resolution of 299×299 before the feature ex-
traction, which ignores high-resolution details and can be inaccurate in assessing
ultra-high-resolution image generation. Therefore, inspired by [3,7], we adopted
the idea of FIDcrop and randomly crops 299 × 299 patches from high-resolution
images for FID evaluation. Still, we retain the FID metric as it serves as an
indicator of overall consistency, which the FIDcrop might overlook.
The results in Tab. 1 demonstrate that our model achieves state-of-the-art
(SOTA) in three out of four metrics and surpasses all competitors in the mean
score. This showcases our model’s exceptional ability to generate high-resolution
details and harmonious global information. The sole exception is the FID at
40962, where it marginally trail behind BSRGAN by 1.0, but as discussed above,
FIDcrop is a more representative metric for high-resolution features and Inf-DiT
surpasses BSRGAN on FIDcrop on both 20482 and 40962 resolution. Our model
is capable of being applied to all generative models, not just SDXL. Examples
of upsampled images from other models are listed in the Appendix C.
Super-Resolution In addition to its ability to generate high-resolution im-
ages, Inf-DiT can also be used as a classic super-resolution model. We conduct
the evaluation on DIV2k valid dataset [1] which contains multiple real-world
high-resolution images in different scenarios. Following [21, 24], we fix image
degradation to bicubic interpolation with 4× downsampling. Before comparing
with fix-resolution models LDM [21] and StableSR [29], we center-crop specific-
sized patches from the high-resolution image as ground truth. Throughout this
process, we utilize both perceptual (FID, FIDcrop) and fidelity (PSNR, SSIM)
metrics to ensure a detailed and comprehensive assessment.

--- Page 12 ---

12
Yang et al.
As demonstrated in Tab. 2, our model achieves state-of-the-art (SOTA)
across all metrics. This signifies that, as a super-resolution model, ours not only
excels in performing super-resolution at arbitrary scales but also in optimally
preserving global and detailed information while restoring results that closely
resemble the original images.
3.3
Human Evaluation
To further evaluate Inf-DiT and more accurately reflect its generative quality
from a human perspective, we conduct a human evaluation. The comparison
settings are the same as in Sec. 3.2, except that we excluded MultiDiffusion
and Direct Inference to their non-competitive results. For each of the four cat-
egories, we randomly choose ten comparison sets, each encompassing outputs
from four models, culminating in a total of 40 sets that form the human evalu-
ation dataset. To ensure fairness, we randomize the sequence of model outputs
in each comparison set. Human evaluators are asked to evaluate models based
on three criteria: detail authenticity, global coherence, and consistency with the
original low-resolution input. Each evaluator receives 20 sets of images on aver-
age. Within each set, evaluators are required to rank the images generated by
four models from highest to lowest based on three criteria.
We ultimately collected 3,600 comparisons. As depicted in Fig. 7, our model
outperforms the other 3 methods in all the 3 criteria. It is particularly noteworthy
that each of the other three models ranks relatively lower on at least one of the
three evaluation criteria, while Inf-DiT achieves the highest score on all three cri-
teria: detail authenticity, global coherence, and consistency with low-resolution
input. This indicates that our model is the only one capable of excelling in both
high-resolution generation and super-resolution tasks simultaneously.
Fig. 7: Human evaluation results. After participants rank the images from different
models, We assign scores from 4 to 1 to models in order and finally calculate the
average of all the results. Inf-DiT gets the highest scores in all three categories.
3.4
Iterative Upsampling
Since our model can upsample images of arbitrary resolution, it’s a natural idea
to test if the model can iteratively upsample images generated by itself. In this
study, we experiment on generating a 20482 resolution image from a 322 resolu-
tion image , 64× upscale, through three times of iterative upsampling. Figure 8

--- Page 13 ---

Inf-DiT
13
Fig. 8: Generated samples of iterative upsampling. Top: Inf-DiT can upsample an
image generated by itself several times, and generate details of different frequencies
at corresponding resolution. Bottom: After failing to generate a pupul at the 1282
resolution, it is difficult for subsequent upsampling stages to correct this error.
illustrates two cases of this process. In the first case, the model successfully
produces a high-resolution image after three stages of upsampling. It generates
details of different frequencies in different resolution upsampling: the contour of
the face, the shape of the eyeball, and individual eyelashes. However, it is hard
for the model to correct inaccuracies generated in earlier stages, leading to the
accumulation of errors. An example of this issue is demonstrated in the second
sample. We leave this problem for our future work.
3.5
Ablation Study
Table 3: Ablation study on 2048 × 2048 resolution.
Method
FID FIDcrop
Ours
66.0
71.9
w/o Nearby LR Attention 66.7
73.6
w/o Semantic Input
66.2
72.8
Inner Block Attention
66.3
83.7
We conduct ablation studies
of our method on 20482 res-
olution. We test the model
performance on the HPDV2
dataset after separately re-
moving the Global Input and
Nearby LR attention. As a
result,
both
the
FID
and
FIDcrop of the model get worse to varying degrees. We also test Inner Block
Attention setting, i.e. removing the attention between blocks, and the FIDcrop
experiences a significant decline. We list more case studies and analysis in the
Appendix B.

--- Page 14 ---

14
Yang et al.
4
Related Work
4.1
Diffusion Image Generation
Diffusion models have emerged as a spotlight in the realm of image generation,
boasting an array of groundbreaking advancements in recent years. Initially in-
troduced in 2015 [26], and further developed through works such as DDPM [11]
and DDIM [27], these models leverage a stochastic diffusion process, conceptu-
alized as a Markov chain, to convert a simple prior distribution, like Gaussian
noise, into a complex data distribution. This methodology yield impressive out-
comes in terms of the quality and diversity of generated images.
Recent enhancements have markedly elevated the generation capabilities of
diffusion models. CDM [12] creates a cascade generation pipeline with multistage
super-resolution models, which can be applied to large pretrained models [20,23].
The introduction of Latent Diffusion Models (LDMs) [18, 21] represents a
pivotal extension, incorporating a latent space to boost both efficiency and scal-
ability. Alongside these advancements, there has been significant progress in
the optimization of network architectures. The advent of Diffusion Transformers
(DiT) [17] Replaces U-Net with ViT [6] for noise prediction.
4.2
Image Super-Resolution
Given a low-resolution (LR) image ILR degraded from high-resolution (HR)
observation IHR, image super-resolution (SR) aims to reconstruct a HR one
ˆIHR: ILR = D(IHR; δ),
ˆIHR = F(ILR; θ). Here D and F refer to degradation
process and the super-resolution model. \delta and \theta represent the parameters.
In recent years, Blind SR has been a major focus: in which the degradation
process is unknown and learnable. This perspective has led to the development
of effective modeling techniques, such as BSRGAN [33] and Real-ESRGAN [30].
Recently, diffusion-based SR methods have yielded exciting results. These
works focus on finetuning pre-trained text-to-image diffusion models to take ad-
vantage of their excellent generative ability. Specifically, DiffBir [16] employs
ControlNet [34] on pre-trained stable-diffusion models, whereas PASD [32] en-
hances it by executing pixel-aware cross-attention. Both approaches have gar-
nered considerable success in fixed resolution super-resolution but cannot be
directly used for higher resolution.
4.3
Ultra-High-Resolution Image Upsampler
Currently, image generation methods fall short in generating ultra-high-resolution
images owing to the constraints of memory and issues with training efficiency.
Under these circumstances, MultiDiffusion [2] and Mixture of Diffusers [14] bind
together multiple diffusion generation processes by dividing images into overlap-
ping blocks, processing each separately, and then stitching them together, aiming
to maintain continuity between blocks. However, because they only used the lo-
cal weighted averaging for aggregation, it leads to a low interaction efficiency
and makes it difficult to ensure the global consistency of the images.

--- Page 15 ---

Inf-DiT
15
Given this concern, DemoFusion [7] and ScaleCrafter [9] adapt dilated policies
including dilated sampling and dilated convolution kernels, aiming at acquiring
more global information. These methods indeed achieve improvement on a global
semantic level without the need for additional training. However, the huge dif-
ference between training and generation leads these methods to easily produce
illogical images.
5
Conclusion
In this work, we observe that the major obstable to generating ultra-high-
resolution images is the substantial memory occupied by model hidden states.
Based on this, We propose Unidirectional Block Attention mechanism (UniBA)
which can lower the space complexity by performing batch generation among
blocks. With UniBA, we train Inf-DiT, a 4× memory-efficient image upsam-
pler which achieves state-of-the-art performance in both generation and super-
resolution tasks.
References
1. Agustsson, E., Timofte, R.: Ntire 2017 challenge on single image super-resolution:
Dataset and study. In: Proceedings of the IEEE conference on computer vision and
pattern recognition workshops. pp. 126–135 (2017)
2. Bar-Tal, O., Yariv, L., Lipman, Y., Dekel, T.: Multidiffusion: Fusing diffusion paths
for controlled image generation (2023)
3. Chai, L., Gharbi, M., Shechtman, E., Isola, P., Zhang, R.: Any-resolution training
for high-resolution image synthesis. In: European Conference on Computer Vision.
pp. 170–188. Springer (2022)
4. Dai, Z., Yang, Z., Yang, Y., Carbonell, J., Le, Q.V., Salakhutdinov, R.:
Transformer-xl: Attentive language models beyond a fixed-length context. arXiv
preprint arXiv:1901.02860 (2019)
5. Dehghani, M., Djolonga, J., Mustafa, B., Padlewski, P., Heek, J., Gilmer, J.,
Steiner, A.P., Caron, M., Geirhos, R., Alabdulmohsin, I., et al.: Scaling vision
transformers to 22 billion parameters. In: International Conference on Machine
Learning. pp. 7480–7512. PMLR (2023)
6. Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner,
T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., et al.: An image is
worth 16x16 words: Transformers for image recognition at scale. arXiv preprint
arXiv:2010.11929 (2020)
7. Du, R., Chang, D., Hospedales, T., Song, Y.Z., Ma, Z.: Demofusion: Democratising
high-resolution image generation with no $$$. arXiv preprint arXiv:2311.16973
(2023)
8. Guttenberg, N.: Diffusion with offset noise (2023), https://www.crosslabs.org/
blog/diffusion-with-offset-noise
9. He, Y., Yang, S., Chen, H., Cun, X., Xia, M., Zhang, Y., Wang, X., He, R., Chen,
Q., Shan, Y.: Scalecrafter: Tuning-free higher-resolution visual generation with
diffusion models. In: The Twelfth International Conference on Learning Represen-
tations (2023)

--- Page 16 ---

16
Yang et al.
10. Heusel, M., Ramsauer, H., Unterthiner, T., Nessler, B., Hochreiter, S.: Gans trained
by a two time-scale update rule converge to a local nash equilibrium. Advances in
neural information processing systems 30 (2017)
11. Ho, J., Jain, A., Abbeel, P.: Denoising diffusion probabilistic models. Advances in
neural information processing systems 33, 6840–6851 (2020)
12. Ho, J., Saharia, C., Chan, W., Fleet, D.J., Norouzi, M., Salimans, T.: Cascaded dif-
fusion models for high fidelity image generation. The Journal of Machine Learning
Research 23(1), 2249–2281 (2022)
13. Ilharco, G., Wortsman, M., Wightman, R., Gordon, C., Carlini, N., Taori, R., Dave,
A., Shankar, V., Namkoong, H., Miller, J., Hajishirzi, H., Farhadi, A., Schmidt, L.:
Openclip (Jul 2021). https://doi.org/10.5281/zenodo.5143773, https://doi.
org/10.5281/zenodo.5143773, if you use this software, please cite it as below.
14. Jiménez, Á.B.: Mixture of diffusers for scene composition and high resolution image
generation. arXiv preprint arXiv:2302.02412 (2023)
15. Karras, T., Aittala, M., Aila, T., Laine, S.: Elucidating the design space of diffusion-
based generative models. Advances in Neural Information Processing Systems 35,
26565–26577 (2022)
16. Lin, X., He, J., Chen, Z., Lyu, Z., Fei, B., Dai, B., Ouyang, W., Qiao, Y., Dong,
C.: Diffbir: Towards blind image restoration with generative diffusion prior. arXiv
preprint arXiv:2308.15070 (2023)
17. Peebles, W., Xie, S.: Scalable diffusion models with transformers. In: Proceedings
of the IEEE/CVF International Conference on Computer Vision. pp. 4195–4205
(2023)
18. Podell, D., English, Z., Lacey, K., Blattmann, A., Dockhorn, T., Müller, J., Penna,
J., Rombach, R.: Sdxl: Improving latent diffusion models for high-resolution image
synthesis. arXiv preprint arXiv:2307.01952 (2023)
19. Radford, A., Kim, J.W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., Sastry, G.,
Askell, A., Mishkin, P., Clark, J., et al.: Learning transferable visual models from
natural language supervision. In: International conference on machine learning. pp.
8748–8763. PMLR (2021)
20. Ramesh, A., Dhariwal, P., Nichol, A., Chu, C., Chen, M.: Hierarchical text-
conditional image generation with clip latents. arXiv preprint arXiv:2204.06125
1(2), 3 (2022)
21. Rombach, R., Blattmann, A., Lorenz, D., Esser, P., Ommer, B.: High-resolution
image synthesis with latent diffusion models. In: Proceedings of the IEEE/CVF
conference on computer vision and pattern recognition. pp. 10684–10695 (2022)
22. Ronneberger, O., Fischer, P., Brox, T.: U-net: Convolutional networks for biomed-
ical image segmentation. In: Medical Image Computing and Computer-Assisted
Intervention–MICCAI 2015: 18th International Conference, Munich, Germany, Oc-
tober 5-9, 2015, Proceedings, Part III 18. pp. 234–241. Springer (2015)
23. Saharia, C., Chan, W., Saxena, S., Li, L., Whang, J., Denton, E.L., Ghasemipour,
K., Gontijo Lopes, R., Karagol Ayan, B., Salimans, T., et al.: Photorealistic text-
to-image diffusion models with deep language understanding. Advances in Neural
Information Processing Systems 35, 36479–36494 (2022)
24. Saharia, C., Ho, J., Chan, W., Salimans, T., Fleet, D.J., Norouzi, M.: Image super-
resolution via iterative refinement. IEEE Transactions on Pattern Analysis and
Machine Intelligence 45(4), 4713–4726 (2022)
25. Schuhmann, C., Beaumont, R., Vencu, R., Gordon, C.W., Wightman, R., Cherti,
M., Coombes, T., Katta, A., Mullis, C., Wortsman, M., Schramowski, P., Kun-
durthy, S.R., Crowson, K., Schmidt, L., Kaczmarczyk, R., Jitsev, J.: LAION-5b:

--- Page 17 ---

Inf-DiT
17
An open large-scale dataset for training next generation image-text models. In:
Thirty-sixth Conference on Neural Information Processing Systems Datasets and
Benchmarks Track (2022), https://openreview.net/forum?id=M3Y74vmsMcY
26. Sohl-Dickstein, J., Weiss, E., Maheswaranathan, N., Ganguli, S.: Deep unsuper-
vised learning using nonequilibrium thermodynamics. In: International conference
on machine learning. pp. 2256–2265. PMLR (2015)
27. Song, J., Meng, C., Ermon, S.: Denoising diffusion implicit models. arXiv preprint
arXiv:2010.02502 (2020)
28. Su, J., Ahmed, M., Lu, Y., Pan, S., Bo, W., Liu, Y.: Roformer: Enhanced trans-
former with rotary position embedding. Neurocomputing 568, 127063 (2024)
29. Wang, J., Yue, Z., Zhou, S., Chan, K.C., Loy, C.C.: Exploiting diffusion prior for
real-world image super-resolution. arXiv preprint arXiv:2305.07015 (2023)
30. Wang, X., Xie, L., Dong, C., Shan, Y.: Real-esrgan: Training real-world blind
super-resolution with pure synthetic data. In: Proceedings of the IEEE/CVF in-
ternational conference on computer vision. pp. 1905–1914 (2021)
31. Wu, X., Hao, Y., Sun, K., Chen, Y., Zhu, F., Zhao, R., Li, H.: Human preference
score v2: A solid benchmark for evaluating human preferences of text-to-image
synthesis. arXiv preprint arXiv:2306.09341 (2023)
32. Yang, T., Ren, P., Xie, X., Zhang, L.: Pixel-aware stable diffusion for realistic im-
age super-resolution and personalized stylization. arXiv preprint arXiv:2308.14469
(2023)
33. Zhang, K., Liang, J., Van Gool, L., Timofte, R.: Designing a practical degradation
model for deep blind image super-resolution. In: Proceedings of the IEEE/CVF
International Conference on Computer Vision. pp. 4791–4800 (2021)
34. Zhang, L., Rao, A., Agrawala, M.: Adding conditional control to text-to-image
diffusion models. In: Proceedings of the IEEE/CVF International Conference on
Computer Vision. pp. 3836–3847 (2023)

--- Page 18 ---

18
Yang et al.
A
Implementation Detail
A.1
Full List of Training Hyperparameters
Training Hyperparameters of Inf-DiT
Number of Layers
28
Attention heads
16
Hidden size
1280 Attention head size
80
FFN inner hidden size 5120 Dropout
0
Warmup Steps
10k
Peak Learning Rate
1e-4
Batch Size
320
Weight Decay
1e-4
Max Steps
1M
Learning Rate Decay Linear
Gradient Clipping
0.1
Adam ϵ
1e-8
Adam β1
0.9
Adam β2
0.099
Table 4: Hyperparameters for Inf-DiT Model
A.2
Efficient Implementation of UniBA
A
I
H
F
E
G
D
C
B
Slice & Concat
Slice & Concat
A
I
H
F
E
G
D
C
B
A
B
C
A
I
H
F
E
G
D
C
B
A
B
C
A
G
D
A
A
I
H
F
E
G
D
C
B
A
B
C
A
G
D
A
1
2
3
4
1
2
3
4
Attention
Slice & Concat
Reshape
A
B
…
I
A
A
…
E
A
B
…
F
A
A
…
H
A
B
…
I
Reshape
Group
Attention
Attention
First block
Last block
Fig. 9: Unidirectional Block Attention during whole image input
In Fig. 9 and Fig. 10, we demonstrate the efficient implementation of UniBA,
where input contains n×n blocks. It is particularly noteworthy that for the blocks
located in the first row and the first column, the number of blocks they depend

--- Page 19 ---

Inf-DiT
19
def get_cat_layers(x):
# Duplicate and prepend first row
cat_x = concat([x[:, 0:1], x], dim=1)
# Duplicate and prepend first column
cat_x = concat([cat_x[:, :, 0:1], cat_x], dim=2)
# Concat four group: self, left-top, left, top
x = concat([x, cat_x[:, :x.shape[1], :x.shape[2]],
cat_x[:, 1:, :x.shape[2]],
cat_x[:, :x.shape[1], 1:]], dim=3)
return x
# The shape of query, key, value :
# [batch_size, h/block_size, w/block_size, block_size*block_size, hidden_size]
key = get_cat_layers(key)
value = get_cat_layers(value)
output = attention(query, key, value)
Fig. 10: Pytorch-style code implementation of UniBA.
on is fewer than three. Due to the property Attention(xW Q, yW K, yW V ) =
Attention(xW Q, [yW K, yW K, ...], [yW V , yW V , ...]), our approach can correctly
handle these situations.
A.3
Stabilization of Training
Currently, many large diffusion models are trained under FP16 (16-bit precision)
to reduce GPU memory and computation time. In practice, however, a sudden
increase in loss often occurs after training for several thousand steps. We observe
that when the number of patches in a single attention window is too many (e.g.
there are 4096 patches with block size = 128 and patch size = 4), the attention
score QT K/
√
d can become very large, leading to unstable gradients or even
overflow. Drawing on the experience of training large-scale ViT [5], we apply
QK Normalization, which add an extra LayerNorm to Query and Key vector
before multiplication:
Attention(Q, K, V ) = Softmax(LN(Q)LN(K)T
√
d
)V
Also, we employed BF16 format during training to further address the issue
of overflow due to its broader numerical range.
A.4
Initial Noise during Inference
Previous experience [8] shows that the diffusion modal tends to generate im-
ages that are closely aligned with the initial noise, which may lead to color
mismatching with the original image during upsampling, e.g. Fig. 11. Fortu-
nately, for the setting of Inf-DiT, there is a natural prior that can control the
mean of the initial noise, the LR image. The idea is, to replace the initial noise
from xT ∼N(0, σ2
maxI) to xT ∼N(xLR, σ2
maxI)during sampling, where xLR

--- Page 20 ---

20
Yang et al.
is resized low-resolution input. However, this method can sometimes lead to the
generated images appearing somewhat blurred just like LR images.
Fig. 11: When upsampling an image of pure black, it is observed that the default initial
noise may generate blocks of other colors. This issue can be resolved by incorporating
LR information into the initial noise.
B
Ablation Study Analysis
In Fig. 12, we demonstrate the results of image generation after the removal of
various components. When attention is restricted to individual blocks, there is a
noticeable discontinuity between different blocks. The UniBA allows for gener-
ating continuous content across blocks, though occasional bad cases may arise.
Incorporating cross-attention to LR images can further reduce the probability
of discontinuous blocks. Additionally, the removal of semantic input, which cor-
responds to CLIP image embedding, results in the generation of textures that
are mismatched with the global semantics.
ALL
Inner Block Attention
W/o Semantic Input
W/o Nearby LR Attention
Fig. 12: Ablation study cases. The first three images separately remove cross-block
attention, Semantic Input (CLIP image embedding), and Nearby LR attention.

--- Page 21 ---

Inf-DiT
21
C
More show cases
C.1
Results based on different Generation Model
Inf-DiT is capable of performing upsampling on images generated by any gener-
ation model, we show more cases here.
Stable Diffusion V2
Fig. 13: Super-resolution applied with Stable Diffusion V2 model: upsampling image
to 2048 × 2048.
DALL-E2
Fig. 14: Super-resolution applied with DALL-E2 model: upsampling image to 2048 ×
2048. In order to reduce the size of the PDF, this part has been compressed by JPEG.
Access the project page to view the original image.
GLIDE
Fig. 15: Super-resolution applied with GLIDE model: upsampling image to 1024×1024
resolution.
C.2
Super-Resolution Cases
We present several cases to demonstrate the model’s super-resolution capabilities
and to compare its performance with other super-resolution models.

--- Page 22 ---

22
Yang et al.
Ours
Ours
BSRGAN
HR(1920*768)
Zoomed LR
Zoomed LR
HR(1920*1280)
BSRGAN
HR(512*512)
Ours
StableSR
Zoomed LR
Ours
LDM
Zoomed LR
HR(256*256)
Fig. 16: Comparison of super-resolution performance at different resolutions.(Zoom
in for details). Images are from DIV2K-valid dataset.

--- Page 23 ---

Inf-DiT
23
D
Human Evalutaion Detail
Here, we provide more details about our user study settings. We adopt Wen-
JuanXing as the evaluation platform. A simple example is shown in Fig. 17. A
single evaluator would receive 3 × 20 questions based on the given image and
prompt.
Fig. 17: human evaluation questionnaire.
At the beginning of the survey, we provide clear explanations for the criteria
used to evaluate each indicator. And we clarify some easily confusing cases, and
also provide examples of bad cases. Evaluators are strongly urged to zoom in on
the images before making their assessments.
To better showcase the results of manual evaluations, we conduct a preference
analysis on the rankings of our model versus other models across three criteria.
The results are visible in Fig. 18, Fig. 19 and Fig. 20. The results show that, on
any criterion, evaluators exhibit a strong preference for our model.

--- Page 24 ---

24
Yang et al.
Fig. 18: Preference comparison results with ScaleCrafter
Fig. 19: Preference comparison results with DemoFusion
Fig. 20: Preference comparison results with BSRGAN

```
