---
title: "RelayDiffusion 2309.03350"
source_pdf: "AI Labs/Zhipu AI/Papers/RelayDiffusion_2309.03350.pdf"
company: "Zhipu AI"
pages: 18
extracted_at: "2026-01-31T17:32:40.247753"
type: "ai_lab_paper"
---

# RelayDiffusion 2309.03350

**Company/Lab:** Zhipu AI
**Source PDF:** AI Labs/Zhipu AI/Papers/RelayDiffusion_2309.03350.pdf
**Total Pages:** 18

---

## Content

```
--- Page 1 ---

Preprint
RELAY DIFFUSION:
UNIFYING DIFFUSION PROCESS
ACROSS RESOLUTIONS FOR IMAGE SYNTHESIS
Jiayan Teng⋆1, Wendi Zheng⋆1, Ming Ding⋆12†,
Wenyi Hong1, Jianqiao Wangni2, Zhuoyi Yang1, Jie Tang1†
⋆equal contribution 1Tsinghua University 2Zhipu AI † corresponding authors
{tengjy20@mails,zhengwd23@mails,jietang@mail}.tsinghua.edu.cn
mingding.thu@gmail.com
ABSTRACT
Diffusion models achieved great success in image synthesis, but still face chal-
lenges in high-resolution generation. Through the lens of discrete cosine transfor-
mation, we find the main reason is that the same noise level on a higher resolution
results in a higher Signal-to-Noise Ratio in the frequency domain. In this work,
we present Relay Diffusion Model (RDM), which transfers a low-resolution image
or noise into an equivalent high-resolution one for diffusion model via blurring
diffusion and block noise. Therefore, the diffusion process can continue seam-
lessly in any new resolution or model without restarting from pure noise or low-
resolution conditioning. RDM achieves state-of-the-art FID on CelebA-HQ and
sFID on ImageNet 256×256, surpassing previous works such as ADM, LDM
and DiT by a large margin. All the codes and checkpoints are open-sourced at
https://github.com/THUDM/RelayDiffusion.
Figure 1: (left): Generated Samples by RDM on ImageNet 256×256 and CelebA-HQ 256×256.
(right): Benchmarking recent diffusion models on class-conditional ImageNet 256×256 generation
without any guidance. RDM can achieve a FID of 1.87 if with classifier-free guidance.
1
INTRODUCTION
Diffusion models (Ho et al., 2020; Rombach et al., 2022) succeeded GANs (Goodfellow et al., 2020)
and autoregressive models (Ramesh et al., 2021; Ding et al., 2021) to become the most prevalent
1
arXiv:2309.03350v1  [cs.CV]  4 Sep 2023

--- Page 2 ---

Preprint
generative models in recent years. However, challenges still exist in the training of diffusion models
for high-resolution images. More specifically, there are two main obstacles:
Training Efficiency. Although equipped with UNet to balance the memory and computation cost
across different resolutions, diffusion models still require a large amount of resources to train on
high-resolution images. One popular solution is to train the diffusion model on a latent (usually
4× compression rate in resolution) space and map the result back as pixels (Rombach et al., 2022),
which is fast but inevitably suffers from some low-level artifacts. The cascaded method (Ho et al.,
2022; Saharia et al., 2022) trains a series of varying-size super-resolution diffusion models, which
is effective but needs a complete sampling for each stage separately.
Noise Schedule. Diffusion models need a noise schedule to control the amount of the isotropic
Gaussian noise at each step. The setting of the noise schedule shows great influence over the perfor-
mance, and most current models follow the linear (Ho et al., 2020) or cosine (Nichol & Dhariwal,
2021) schedule. However, an ideal noise schedule should be resolution-dependent (See Figure 2
or Chen (2023)), resulting in suboptimal performance to train high-resolution models directly with
common schedules designed for resolutions of 32×32 or 64×64 pixels.
These obstacles hindered previous researchers to establish an effective end-to-end diffusion model
for high-resolution image generation.
Dhariwal & Nichol (2021) attempted to directly train a
256×256 ADM but found that it performs much worse than the cascaded pipeline. Chen (2023)
and Hoogeboom et al. (2023) carefully adjusted the hyperparameters of noise schedule and architec-
ture for high-resolution cases, but the quality is still not comparable to the state-of-the-art cascaded
methods (Saharia et al., 2022).
In our opinion, the cascaded method contributes in both training efficiency and noise schedule:
(1) It provides flexibility to adjust the model size and architecture for each stage to find the most
efficient combination. (2) The existence of low-resolution condition makes the early sampling steps
easy, so that the common noise schedules (optimized for low-resolution models) can be applied as
a feasible baseline to the super-resolution models. Moreover, (3) high-resolution images are more
difficult to obtain on the Internet than low-resolution images. The cascaded method can leverage the
knowledge from low-resolution samples, meanwhile keep the capability to generate high-resolution
images. Therefore, it might not be a promising direction to completely replace the cascaded method
with an end-to-end one at the current stage.
The disadvantages of the cascaded method are also obvious: (1) Although the low-resolution part
is determined, a complete diffusion model starting from pure noise is still trained and sampled for
super-resolution, which is time-consuming. (2) The distribution mismatch between ground-truth
and generated low-resolution condition will hurt the performance, so that tricks like conditioning
augmentation (Ho et al., 2022) become vitally important to mitigate the gap. Besides, the noise
schedule of high-resolution stages are still not well studied.
Present Work.
Here we present the Relay Diffusion Model (RDM), a new cascaded framework
to improve the shortcomings of the previous cascaded methods. In each stage, the model starts
diffusion from the result of the last stage, instead of conditioning on it and starting from pure noise.
Our method is named as the cascaded models work together like a “relay race”. The contributions
of this paper can be summarized as follows:
• We analyze the reasons of the difficulty of noise scheduling in high-resolution diffusion
models in frequency domain. Previous works like LDM (Rombach et al., 2022) assume all
image signals from the same distribution when analyzing the SNR, neglecting the differ-
ence in frequency domain between low-resolution and high-resolution images. Our analysis
successfully account for phenomenon that the same noise level shows different perceptual
effects on different resolutions, and introduce the block noise to bridge the gap.
• We propose RDM to disentangle the diffusion process and the underlying neural networks
in the cascaded pipeline. RDM gets rid of the low-resolution conditioning and its distribu-
tion mismatch problem. Since RDM starts diffusion from the low-resolution result instead
of pure noise, the training and sampling steps can also be reduced.
• We evaluate the effectiveness of RDM on unconditional CelebA-HQ 256×256 and condi-
tional ImageNet 256×256 datasets. RDM achieves state-of-the-art FID on CelebA-HQ and
sFID on ImageNet.
2

--- Page 3 ---

Preprint
2
PRELIMINARY
2.1
DIFFUSION MODELS
To model the data distribution pdata(x0), denoising diffusion probabilistic models (DDPMs, Ho
et al. (2020)) define the generation process as a Markov chain of learned Gaussian transitions.
DDPMs first assume a forward diffusion process, corrupting real data x0 by progressively adding
Gaussian noise from time steps 0 to T, whose variance {βt} is called the noise schedule:
q(xt|xt−1) = N(xt;
p
1 −βtxt−1, βtI).
(1)
The reverse diffusion process is learned by a time-dependent neural network to predict denoised
results at each time step, by optimizing the variational lower bound (ELBO).
Many other formulations for diffusion models include stochastic differential equations (SDE, Song
et al. (2020b)), denoising diffusion implicit models (DDIM, Song et al. (2020a)), etc. Karras et al.
(2022) summaries these different formulations into the EDM framework. In this paper, we generally
follow the EDM formulation and implementation. The training objective of EDM is defined as L2
error terms:
Ex∼pdata,σ∼p(σ)Eϵ∼N(0,I)∥D(x + σϵ, σ) −x∥2,
(2)
where p(σ) represents the distribution of a continuous noise schedule. D(x + ϵ, σ) represents the
denoiser function depending on the noise scale. We also follow the EDM precondition for D(x +
ϵ, σ) with σ-dependent skip connection (Karras et al., 2022).
Cascaded diffusion model (CDM, Ho et al. (2022)) is proposed for high-resolution generation. CDM
divides the generation into multiple stages, where the first stage generates low-resolution images
and the following stages perform super-resolution conditioning on the outputs of the previous stage.
Cascaded models are extensively adopted in recent works of text-to-image generation, e.g. Ima-
gen (Saharia et al., 2022), DALL-E-2 (Ramesh et al., 2022) and eDiff-I (Balaji et al., 2022).
2.2
BLURRING DIFFUSION
The Inverse Heat Dissipation Model (IHDM) (Rissanen et al., 2022) generates images by reversing
the heat dissipation process. The heat dissipation is a thermodynamic process describing how the
temperature u(x, y, t) at location (x, y) changes in a (2D) space with respect to the time t. The
dynamics can be denoted by a PDE ∂u
∂t = ∂2u
∂x2 + ∂2u
∂y2 .
Blurring diffusion (Hoogeboom & Salimans, 2022) is further derived by augmenting the Gaus-
sian noise with heat dissipation for image corruption. Since simulating the heat equation up to
time t is equivalent to a convolution with a Gaussian kernel with variance σ2 = 2t in an infinite
plane (Bredies et al., 2018), the intermediate states xt become blurry, instead of noisy in the stan-
dard diffusion. If Neumann boundary conditions are assumed, blurring diffusion in discrete 2D
pixel space can be transformed to the frequency space by Discrete Cosine Transformation (DCT)
conveniently as:
q(ut|u0) = N(ut|Dtu0, σ2
t I),
(3)
where ut = DCT(xt) , and Dt = eΛt is a diagonal matrix with Λi×W +j = −π2( i2
H2 +
j2
W 2 ) for
coordinate (i, j). Here Gaussian noise with variance σ2
t is mixed into the blurring diffusion process
to transform the deterministic dissipation process to a stochastic one for diverse generation (Rissanen
et al., 2022).
3
METHOD
3.1
MOTIVATION
The noise schedule is vitally important to the diffusion models and resolution-dependent. A certain
noise level appropriately corrupting the 64 × 64 images, could fail to corrupt the 256 × 256 (or
a higher resolution) images, which is shown in the first row of Figure 2(a)(b). Chen (2023) and
Hoogeboom et al. (2023) attributed this to the lack of schedule-tuning, but we found an analysis
from the perspective of frequency spectrum can help us better understand this phenomenon.
3

--- Page 4 ---

Preprint
Figure 2: Illustration of spatial and frequency results after adding independent Gaussian and block
noise. (a)(b) At the resolution of 64 × 64 and 256 × 256, the same noise level results in different
perceptual effects, and in the frequency plot, the SNR curve shifts upward. (c) The independent
Gaussian noise at the resolution 64×64 and block noise (kernel size = 4) at the resolution 256×256
produces similar results in both spatial domain and frequency domain. The noise is N(0, 0.32) for
(a). These SNR curves are universally applicable to most natural images.
Frequency spectrum analysis of the diffusion process. The natural images with different reso-
lutions can be viewed as the result of visual signals sampled at varying frequencies. To compare
the frequency features of a 64 × 64 image and a 256 × 256 image, we can upsample the 64 × 64
one to 256 × 256, perform DCT and compare them in the 256-point DCT spectrum. The second
row of Figure 2(a) shows the signal noise ratio (SNR) at different frequencies and diffusion steps.
In Figure 2(b), we clearly find that the same noise level on a higher resolution results in a higher
SNR in the (low-frequency part of) the frequency domain. Detailed frequency spectrum analysis are
included in Appendix C.
At a certain diffusion step, a higher SNR means that during training the neural network presumes
the input image more accurate, but the early steps may not be able to generate such accurate images
after the increase in SNR. This training-inference mismatch will accumulate over step by step during
sampling, leading to the degradation of performance.
Block noise as the equivalence at high resolution. After the upsampling from 64×64 to 256×256,
the independent Gaussian noise on 64 × 64 becomes noise on 4 × 4 grids, thus greatly changes its
frequency representation. To find a variant of the s × s-grid noise without deterministic bound-
aries, we propose Block noise, where the Gaussian noise are correlated for nearby positions. More
specifically, the covariance between noise ϵx0,y0 and ϵx1,y1 is defined as
Cov(ϵx0,y0, ϵx1,y1) = σ2
s2 max
 0, s −dis(x0, x1)

max
 0, s −dis(y0, y1)

,
(4)
where σ2 is the noise variance, and s is a hyperparameter kernel size. The dis(·, ·) function here is
the Manhattan distance. For simplicity, we “connect” the top and bottom edges and the left and right
edges of the image, resulting in
dis(x0, x1) = min (|x0 −x1|, xmax −|x0 −x1|) .
(5)
The block noise with kernel size s can be generated by averaging s × s independent Gaussian noise.
Suppose we have an independent Gaussian noise matrix ϵ, the block noise construction function
Block[s](·) is defined as
Block[s](ϵ)x,y = 1
s
s−1
X
i=0
s−1
X
j=0
ϵx−i,y−j,
(6)
where Block[s](ϵ)x,y is the block noise at the position (x, y), and ϵ−x = ϵxmax−x. Figure 2(c)
shows that the block noise with kernel size s = 4 on 256 × 256 has a similar frequency spectrum as
the independent Gaussian noise on 64 × 64 images.
4

--- Page 5 ---

Preprint
The analysis above seems to indicate that we can design an end-to-end model for high-resolution
images by introducing block noise in early diffusion steps, while cascaded models already achieves
great success. Therefore, a revisit of the cascaded models is necessary.
Why does the cascaded models alleviate this issue? Experiments in previous works (Nichol &
Dhariwal, 2021; Dhariwal & Nichol, 2021) have already shown that cascaded models perform better
than end-to-end models under a fair setting. These models usually use the same noise schedule in all
stages, so why are the cascaded models not affected by the increase of SNR? The reason is that in
the super-resolution stages, the low-resolution condition greatly ease the difficulty of the early steps,
so that even the higher SNR requires a more accurate input, the accuracy is within the capability of
the model.
A natural idea is that since the low-frequency information in the high-resolution stage has already
been determined by the low-resolution condition, we can continue generating directly from the up-
sampled result to reduce both the training and sampling steps. However, the generation of low-
resolution images is not perfect, and thus the solution of the distribution mismatch between ground-
truth and generated low-resolution images is a priority to “continue” the diffusion process.
3.2
RELAY DIFFUSION
Figure 3: Pipeline of Relay Diffusion Models (RDM).
We propose relay diffusion model (RDM), a cascaded pipeline connecting the stages with block
noise and (patch-level) blurring diffusion. Different from CDM, RDM considers the equivalence of
the low-resolution generated images when upsampled to high resolution. Suppose that the generated
64 × 64 low-resolution image xL
0 = xL + ϵL can be decomposed into a sample in real distribution
xL and a remaining noise ϵL ∼N(0, β2
0I). As mentioned in section 3.1, the 256 × 256 equivalence
of ϵL is Block[4] noise with variance β2
0, denoted by ϵH. After (nearest) upsampling, xL becomes
xH, where each 4 × 4 grid share the same pixel values. We can define it as the starting state of a
patch-wise blurring diffusion.
Unlike blurring diffusion models (Rissanen et al., 2022) (Hoogeboom & Salimans, 2022) that per-
form the heat dissipation on the entire space of images, we propose to implement the heat dissipation
on each 4×4 patch independently, which is of the same size as the upsampling scale. We first define
a series of patch-wise blurring matrix {Dp
t }, which is introduced in detail in Appendix A.1. The
forward process would have a similar representation with equation 3:
q(xt|x0) = N(xt|V Dp
t V Tx0, σt
2I),
t ∈{0, .., T},
(7)
where V T is the projection matrix of DCT and σt is the variance of noise. Here the Dp
T is chosen to
guarantee V Dp
T V Tx0 in the same distribution as xH, meaning that the blurring process ultimately
makes the pixel value in each 4 × 4 patch the same.
5

--- Page 6 ---

Preprint
The training objective of the high-resolution stage of RDM generally follows EDM (Karras et al.,
2022) framework in our implementation. The loss function is defined on the prediction of denoiser
function D to fit with true data x, which is written as:
Ex∼pdata,t∼U(0,1),ϵ∼N(0,I)∥D(xt, σt) −x∥2,
where
xt = V Dp
t V T
|
{z
}
blurring
x +
σ
√
1 + α2
 ϵ + α · Block[s](ϵ′)
|
{z
}
block noise

,
(8)
where ϵ and ϵ′ are two independent Gaussian noise. The main difference in training between RDM
and EDM is that the corrupted sample xt is not simply xt = x + ϵ, but a mixture of the blurred
image, block noise and independent Gaussian noise. Ideally, the noise should gradually transfer from
block noise to high-resolution independent Gaussian noise, but we find that a weighting average
strategy perform well enough, because the low-frequency component of the block noise is much
larger than the independent Gaussian noise, and vice versa for high-frequency component. α is a
hyperparameter and the normalizer
1
√
1+α2 is used to keep the variance of the noise, σ2 unchanged.
The advantages of RDM compared to CDM includes:
• RDM is more efficient, because RDM skips the re-generation of low-frequency information
in the high-resolution stages, and reduce the number of training and sampling steps.
• RDM is more simple, because it gets rid of the low-resolution conditioning and condition-
ing augmentation tricks. The consumption from cross-attention with the low-resolution
condition is also spared.
• RDM is more potential in performance, because RDM is a Markovian denosing process (if
with DDPM sampler). Any artifacts in the low-resolution images can be corrected in the
high-resolution stage, while CDM is trained to correspond to the low-resolution condition.
Compared to end-to-end models (Chen, 2023; Hoogeboom et al., 2023),
• RDM is more flexible to adjust the model size and leverage more low-resolution data.
3.3
STOCHASTIC SAMPLER
Since RDM differs from traditional diffusion models in the forward process, we also need to adapt
the sampling algorithms. In this section, we focus on the EDM sampler (Karras et al., 2022) due to
its flexibility to switch between the first and second order (Heun’s) samplers.
Heun’s method introduces an additional step for the correction of the first-order sampling. The
updating direction of a first-order sampling step is controlled by the gradient term dn
=
xn−xθ(xn,σtn)
σtn
. The correction step updates current states with an averaged gradient term dn+dn−1
2
.
Heun’s method takes account of the change of gradient term dx
dt between tn and tn−1. Therefore, it
achieves higher quality while allowing for fewer steps of sampling.
We adapt the EDM sampler to the blurring diffusion of RDM’s super-resolution stage following
the derivation of DDIM (Song et al., 2020a). We define the indices of sampling steps as {ti}N
i=0,
in corresponding to the noisy states of images {xi}N
i=0. To apply blurring diffusion, images are
transformed into frequency space by DCT as ui = V Txi. Song et al. (2020a) uses a family of
inference distributions to describe the diffusion process. We can write it for blurring diffusion as:
qδ(u1:N|u0) = qδ(uN|u0)
N
Y
n=2
qδ(un−1|un, u0),
(9)
where δ ∈RN
≥0 denotes the index vector for the distribution. For all n > 1, the backward process is:
qδ(un−1|un, u0) = N
 un−1| 1
σtn
(
q
σ2
tn−1 −δ2nun + (σtnDp
tn−1 −
q
σ2
tn−1 −δ2nDp
tn)u0), δ2
nI

.
(10)
The mean of the normal distribution ensures the forward process to be consistent with the formu-
lation of blurring diffusion in Section 3.2, which is q(un|u0) = N(un|Dp
tnu0, σ2
tnI). When the
6

--- Page 7 ---

Preprint
index vector δ is 0, the sampler degenerates into an ODE sampler. We set δn = ησtn−1 for our sam-
pler, where η ∈[0, 1) is a fixed scalar controlling the scale of randomness injected during sampling.
We substitute the definition into Eq. 10 to obtain our sampler function as:
un−1 = (Dp
tn−1 + γn(I −Dp
tn))un + σtn(γnDp
tn −Dp
tn−1)un −˜u0
σtn
+ ησtn−1ϵ,
(11)
where γn ≜
p
1 −η2 σtn−1
σtn . As in the section 3.1, we also need to consider block noise besides
blurring diffusion. The adaptation is just to replace isotropic Gaussian noise ϵ with ˜ϵ, which is a
weighted sum of the block noise and isotropic Gaussian noise. ˜u0 = uθ(un, σtn) is predicted by
the neural network.
Finally, a stochastic sampler for the super-resolution stage of RDM is summaries in Algorithm 1.
We provide a detailed proof of the consistency between our sampler and the formulation of blurring
diffusion in Appendix A.3.
Algorithm 1 the RDM second-order stochastic sampler
sample xN ∼N
 0, σ2
NI

uN = V TxN
▷transformed into the frequency domain
for n ∈{N, . . . , 1} do
γn =
p
1 −η2 σtn−1
σtn ,
δn = ησtn−1
▷coefficient of the random term
˜u0 = uθ(un, σtn)
▷model prediction at tn
dn = un−˜u0
σtn
▷first-order gradient term at tn
un−1 = (Dp
tn−1 + γn(I −Dp
tn))un + σtn(γnDp
tn −Dp
tn−1)dn + δnϵ
▷from tn to tn−1 using Euler’s method
if n ̸= 1 then
▷the second-order part
˜u′
0 = uθ(un−1, σtn−1)
▷model prediction at tn−1
dn−1 = un−1−˜u′
0
σtn−1
▷gradient term at tn−1
d′
n = dn+dn−1
2
▷second-order gradient term
u′
n−1 = (Dp
tn−1 + γn(I −Dp
tn))un + σtn(γnDp
tn −Dp
tn−1)d′
n + δnϵ
▷correction
end if
un−1 = u′
n−1
end for
x0 = V u0
4
EXPERIMENTS
4.1
EXPERIMENTAL SETTING
Dataset. We use CelebA-HQ and ImageNet in our experiments. CelebA-HQ (Karras et al., 2018)
is a high-quality subset of CelebA (Liu et al., 2015) which consists of 30,000 images of faces from
human celebrities. ImageNet (Deng et al., 2009) contains 1,281,167 images spanning 1000 different
classes and is a widely-used dataset for generation and vision tasks. We train RDM on these datasets
to generate 256 × 256 images.
Architecture and Training. RDM adopts UNet (Ronneberger et al., 2015) as the backbone of
diffusion models for both the first and the second stage. The detailed architectures largely follow
ADM (Dhariwal & Nichol, 2021) for fair comparison. We train unconditional models on CelebA-
HQ and class-conditional models on ImageNet respectively. Since we follow the EDM implemen-
tation, we directly use the released checkpoint from EDM in ImageNet in the 64 × 64 stage. The
FLOPs of the 64 × 64 model are about 1/10 that of the 256 × 256 model. See Appendix B for more
information about the architecture and hyperparameters of RDM.
Evaluation. We use metrics including FID (Heusel et al., 2017), sFID (Nash et al., 2021), IS (Sali-
mans et al., 2016), Precision and Recall (Kynk¨a¨anniemi et al., 2019) for a comprehensive evaluation
7

--- Page 8 ---

Preprint
Table 1: Benchmarking unconditional image generation on CelebA-HQ 256 × 256.
Unconditional CelebA-HQ 256 × 256
Model
FID↓
Precision↑
Recall↑
LSGM (Vahdat et al., 2021)
7.22
-
-
WaveDiff (Phung et al., 2023)
5.94
-
0.37
LDM-4 (Rombach et al., 2022)
5.11
0.72
0.49
StyleSwin (Zhang et al., 2022)
3.25
-
-
RDM
3.15
0.77
0.55
Table 2: Benchmarking class-conditional image generation on ImageNet 256 × 256.
Class-Conditional ImageNet 256 × 256
Model
FID↓
sFID↓
IS↑
Precision↑
Recall↑
BigGAN-deep (Brock et al., 2018)
6.95
7.36
171.4
0.87
0.28
StyleGAN-XL (Sauer et al., 2022)
2.30
4.02
265.12
0.78
0.53
ADM (Dhariwal & Nichol, 2021)
10.94
6.02
100.98
0.69
0.63
LDM-4 (Rombach et al., 2022)
10.56
-
103.49
0.71
0.62
DiT-XL/2 (Peebles & Xie, 2022)
9.62
6.85
121.50
0.67
0.67
MDT-XL/2 (Gao et al., 2023)
6.23
5.23
143.02
0.71
0.65
RDM
5.27
4.39
153.43
0.75
0.62
CDM (Ho et al., 2022)
4.88
-
158.71
-
-
ADM-U,G
3.94
6.14
215.84
0.83
0.53
LDM-4-G (CFG=1.50)
3.60
-
247.67
0.87
0.48
MDT-XL/2-G (dynamic CFG)
1.79
4.57
283.01
0.81
0.61
DiT-XL/2-G (CFG=1.50)
2.27
4.60
278.24
0.83
0.57
MDT-XL/2-G (CFG=1.325)
2.26
4.28
246.06
0.81
0.59
RDM (CFG=3.50)
1.99
3.99
260.45
0.81
0.58
+ class-balance
1.87
3.97
278.75
0.81
0.59
of the results. FID measures the difference between the features of model generations and real
images, which is extracted by a pretrained Inception network. sFID differs from FID by using inter-
mediate features, which better measures the similarity of spatial distribution. IS and Precision both
measure the fidelity of the samples, while Recall indicates the diversity. We compute metrics with
50,000 and 30,000 generated samples for ImageNet and CelebA-HQ respectively.
4.2
RESULTS
CelebA-HQ We compare RDM with the existing methods on CelebA-HQ 256 × 256 in Table 1.
RDM outperforms the state-of-the-art model StyleSwin (Zhang et al., 2022) with a remarkably fewer
training iterations (50M versus 820M trained images). We also achieve the best precision and recall
among the existing works.
ImageNet Table 2 shows the performance of class-conditional generative models on ImageNet 256×
256. We report the best results as possible of the existing methods with classifier-free guidance
(CFG) (Ho & Salimans, 2022). RDM achieves the best sFID and outperforms all the other methods
by FID except MDT-XL/2 (Gao et al., 2023) with a dynamic CFG scale. If with a fixed but best-
picked CFG scale1, MDT-XL/2 can only achieve an FID of 2.26. While achieving competitive
results, RDM is trained with only 70% of the iterations of MDT-XL/2 (1.2B versus 1.7B trained
images), indicating that the longer training and a more granular CFG strategy are potential directions
to further optimize the FID of RDM.
1The best CFG scale is 1.325 with a hyperparameter sweep from 1.0 to 1.8. We observed the FID increases
greatly if CFG scale > 1.5 for MDT-XL/2.
8

--- Page 9 ---

Preprint
Training Efficiency We also compare the performance of RDM with existing methods along with
the training cost in Figure 1. When CFG is disabled, RDM achieves a better FID than previous
state-of-the-art diffusion models including DiT (Peebles & Xie, 2022) and MDT (Gao et al., 2023).
RDM outperforms them even with only about 1/3 training iterations.
4.3
ABLATION STUDY
In this section, we conduct ablation experiments on the designs of RDM to verify their effectiveness.
Unless otherwise stated, we report results of RDM on 256 × 256 generation without CFG.
Figure 4: The effectiveness of block noise. We compare the performance of RDM along the training
on (a) ImageNet 256 × 256 and (b) CelebA-HQ 256 × 256. To apply block noise in RDM, we set
α = 0.15 and kernel size s = 4.
The Effectiveness of block noise. We compare the performance of RDM with and without adding
block noise in Figure 4. With a sufficient phase of training, RDM with block noise outperforms
the model without block noise by a remarkable margin on both ImageNet and CelebA-HQ. This
demonstrates the effectiveness of the block noise. The addition of block noise introduces higher
modeling complexity of the noise pattern, which contributes to a slower convergence of training in
the initial stage, as illustrated by Figure 4(a). We assume that training on a significantly smaller
scale of samples leads to a fast convergence of the model, which obliterates such a feature, therefore
a similar phenomenon cannot be observed in the training of CelebA-HQ.
η
0
0.10
0.15
0.20
0.25
0.30
0.40
0.50
FID↓
5.65
5.44
5.31
5.27
5.48
5.91
6.91
9.17
η
0
0.10
0.15
0.20
0.25
0.30
0.40
0.50
FID↓
4.11
3.74
3.43
3.15
3.23
3.52
4.79
6.41
Table 3: Effect of stochasticity in the sampler on ImageNet 256 × 256 (top) and CelebA-HQ 256 ×
256 (bottom). We explored different values of the η in Algorithm 1.
The scale of stochasticity. As previous works (Song et al., 2020b) have shown, SDE samplers
usually perform better than ODE samplers. We want to quantitatively measure how the scale of
the stochaticity affects the performance in the RDM sampler (Algorithm 1). Table 3 shows results
with η varying from 0 to 0.50. For both CelebA-HQ and ImageNet, the optimal FID is achieved
by η = 0.2. We hypothesis a small η is insufficient for the noise addition to cover the bias formed
in earlier sampling steps, while a large η introduces excessive noise into the process of sampling,
which makes a moderate η to be the best choice. Within a reasonable scale of stochasticity, an SDE
sampler always outperforms the ODE sampler by a significant margin.
9

--- Page 10 ---

Preprint
Figure 5: Comparison of FID on ImageNet with dif-
ferent sampling steps. For allocation of NFE = N in
RDM, 10n+( N
2 −n) means 10n for the first stage and
N
2 −n for the second.
Sampling steps. To demonstrate the ef-
ficiency of our model, we compare the
performance of RDM and other methods
with fewer sampling steps.
Number of
Function Evaluations (NFE), i.e., the num-
ber that a neural network is called dur-
ing sampling, is used as the index of
the comparison for fairness.
For RDM,
the NFE consists of the NFE in the sec-
ond stage and 1/10 the NFE in the first
stage, according to the proportion of the
FLOPs. As shown in Figure 5, the per-
formance of DiT-XL/2 (Peebles & Xie,
2022) and MDT-XL/2 (Gao et al., 2023)
both drop significantly with a lower NFE,
while RDM barely declines. Considering
that the steps in different stages may con-
tribute differently in FID, we demonstrates
three FLOPs allocation strategies in Fig-
ure 5.
With more NFE allocated in the
first stage, RDM achieves a better FID. In
all the settings, RDM performs better than
MDT-XL/2 and DiT-XL/2 if NFE < 200.
5
CONCLUSION AND DISCUSSION
In this paper, we propose relay diffusion to optimize the cascaded pipeline. The diffusion process can
now continue when changing the resolution or model architectures. We anticipate that our method
can reduce the cost of training and inference, and help create more advanced text-to-image model in
the future.
The frequency analysis in the paper reveals the relation between noise and image resolution, which
might be helpful to design a better noise schedule. However, our numerous attempts to directly
derive the optimal noise schedule on the dataset did not yield good results. The reason might be that
the optimal noise schedule is also be related to the size of the model, inductive bias, and the nuanced
distribution characteristics of the data. Further investigation is left for future work.
AUTHOR CONTRIBUTIONS
Ming Ding proposes the methods and leads the project. Jiayan Teng and Wendi Zheng conduct most
of the experiments. Wenyi Hong works together on early experiments. Jianqiao Wangni, Wenyi
Hong and Zhuoyi Yang contribute to the writing of the paper. Jie Tang provides guidance and
supervision.
The work is partly done during the internship of Jiayan Teng and Wendi Zheng at Zhipu AI.
ACKNOWLEDGMENTS
The authors also thank Ting Chen from Google DeepMind and Junbo Zhao from Zhejiang University
for their valuable talks and comments.
REFERENCES
Yogesh Balaji, Seungjun Nah, Xun Huang, Arash Vahdat, Jiaming Song, Karsten Kreis, Miika
Aittala, Timo Aila, Samuli Laine, Bryan Catanzaro, et al. ediffi: Text-to-image diffusion models
with an ensemble of expert denoisers. arXiv preprint arXiv:2211.01324, 2022.
Christopher M Bishop and Nasser M Nasrabadi. Pattern recognition and machine learning, vol-
ume 4. Springer, 2006.
10

--- Page 11 ---

Preprint
Kristian Bredies, Dirk Lorenz, et al. Mathematical image processing. Springer, 2018.
Andrew Brock, Jeff Donahue, and Karen Simonyan. Large scale gan training for high fidelity natural
image synthesis. arXiv preprint arXiv:1809.11096, 2018.
Ting Chen.
On the importance of noise scheduling for diffusion models.
arXiv preprint
arXiv:2301.10972, 2023.
Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei. Imagenet: A large-scale hi-
erarchical image database. In 2009 IEEE conference on computer vision and pattern recognition,
pp. 248–255. Ieee, 2009.
Prafulla Dhariwal and Alexander Nichol. Diffusion models beat gans on image synthesis. Advances
in neural information processing systems, 34:8780–8794, 2021.
Ming Ding, Zhuoyi Yang, Wenyi Hong, Wendi Zheng, Chang Zhou, Da Yin, Junyang Lin, Xu Zou,
Zhou Shao, Hongxia Yang, et al. Cogview: Mastering text-to-image generation via transformers.
Advances in Neural Information Processing Systems, 34:19822–19835, 2021.
Shanghua Gao, Pan Zhou, Ming-Ming Cheng, and Shuicheng Yan. Masked diffusion transformer is
a strong image synthesizer. arXiv preprint arXiv:2303.14389, 2023.
Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair,
Aaron Courville, and Yoshua Bengio. Generative adversarial networks. Communications of the
ACM, 63(11):139–144, 2020.
Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, and Sepp Hochreiter.
Gans trained by a two time-scale update rule converge to a local nash equilibrium. Advances in
neural information processing systems, 30, 2017.
Jonathan Ho and Tim Salimans.
Classifier-free diffusion guidance.
arXiv preprint
arXiv:2207.12598, 2022.
Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffusion probabilistic models. Advances in
neural information processing systems, 33:6840–6851, 2020.
Jonathan Ho, Chitwan Saharia, William Chan, David J Fleet, Mohammad Norouzi, and Tim Sali-
mans. Cascaded diffusion models for high fidelity image generation. The Journal of Machine
Learning Research, 23(1):2249–2281, 2022.
Emiel Hoogeboom and Tim Salimans. Blurring diffusion models. arXiv preprint arXiv:2209.05557,
2022.
Emiel Hoogeboom, Jonathan Heek, and Tim Salimans. simple diffusion: End-to-end diffusion for
high resolution images. arXiv preprint arXiv:2301.11093, 2023.
Tero Karras, Timo Aila, Samuli Laine, and Jaakko Lehtinen. Progressive growing of gans for im-
proved quality, stability, and variation. In International Conference on Learning Representations,
2018.
Tero Karras, Miika Aittala, Timo Aila, and Samuli Laine. Elucidating the design space of diffusion-
based generative models. Advances in Neural Information Processing Systems, 35:26565–26577,
2022.
Tuomas Kynk¨a¨anniemi, Tero Karras, Samuli Laine, Jaakko Lehtinen, and Timo Aila. Improved
precision and recall metric for assessing generative models. Advances in Neural Information
Processing Systems, 32, 2019.
Ziwei Liu, Ping Luo, Xiaogang Wang, and Xiaoou Tang. Deep learning face attributes in the wild.
In Proceedings of the IEEE international conference on computer vision, pp. 3730–3738, 2015.
Charlie Nash, Jacob Menick, Sander Dieleman, and Peter W Battaglia. Generating images with
sparse representations. arXiv preprint arXiv:2103.03841, 2021.
11

--- Page 12 ---

Preprint
Alexander Quinn Nichol and Prafulla Dhariwal. Improved denoising diffusion probabilistic models.
In International Conference on Machine Learning, pp. 8162–8171. PMLR, 2021.
William Peebles and Saining Xie. Scalable diffusion models with transformers. arXiv preprint
arXiv:2212.09748, 2022.
Hao Phung, Quan Dao, and Anh Tran. Wavelet diffusion models are fast and scalable image gener-
ators. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition,
pp. 10199–10208, 2023.
Aditya Ramesh, Mikhail Pavlov, Gabriel Goh, Scott Gray, Chelsea Voss, Alec Radford, Mark Chen,
and Ilya Sutskever. Zero-shot text-to-image generation. In International Conference on Machine
Learning, pp. 8821–8831. PMLR, 2021.
Aditya Ramesh, Prafulla Dhariwal, Alex Nichol, Casey Chu, and Mark Chen. Hierarchical text-
conditional image generation with clip latents. arXiv preprint arXiv:2204.06125, 2022.
Severi Rissanen, Markus Heinonen, and Arno Solin. Generative modelling with inverse heat dissi-
pation. arXiv preprint arXiv:2206.13397, 2022.
Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Bj¨orn Ommer. High-
resolution image synthesis with latent diffusion models. In Proceedings of the IEEE/CVF confer-
ence on computer vision and pattern recognition, pp. 10684–10695, 2022.
Olaf Ronneberger, Philipp Fischer, and Thomas Brox. U-net: Convolutional networks for biomed-
ical image segmentation. In Medical Image Computing and Computer-Assisted Intervention–
MICCAI 2015: 18th International Conference, Munich, Germany, October 5-9, 2015, Proceed-
ings, Part III 18, pp. 234–241. Springer, 2015.
Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li, Jay Whang, Emily L Denton, Kamyar
Ghasemipour, Raphael Gontijo Lopes, Burcu Karagol Ayan, Tim Salimans, et al. Photorealistic
text-to-image diffusion models with deep language understanding. Advances in Neural Informa-
tion Processing Systems, 35:36479–36494, 2022.
Tim Salimans, Ian Goodfellow, Wojciech Zaremba, Vicki Cheung, Alec Radford, and Xi Chen.
Improved techniques for training gans. Advances in neural information processing systems, 29,
2016.
Axel Sauer, Katja Schwarz, and Andreas Geiger. Stylegan-xl: Scaling stylegan to large diverse
datasets. In ACM SIGGRAPH 2022 conference proceedings, pp. 1–10, 2022.
Jiaming Song, Chenlin Meng, and Stefano Ermon. Denoising diffusion implicit models. arXiv
preprint arXiv:2010.02502, 2020a.
Yang Song, Jascha Sohl-Dickstein, Diederik P Kingma, Abhishek Kumar, Stefano Ermon, and Ben
Poole. Score-based generative modeling through stochastic differential equations. arXiv preprint
arXiv:2011.13456, 2020b.
Arash Vahdat, Karsten Kreis, and Jan Kautz.
Score-based generative modeling in latent space.
Advances in Neural Information Processing Systems, 34:11287–11302, 2021.
Bowen Zhang, Shuyang Gu, Bo Zhang, Jianmin Bao, Dong Chen, Fang Wen, Yong Wang, and Bain-
ing Guo. Styleswin: Transformer-based gan for high-resolution image generation. In Proceedings
of the IEEE/CVF conference on computer vision and pattern recognition, pp. 11304–11314, 2022.
12

--- Page 13 ---

Preprint
A
DERIVATION
A.1
PATCH-WISE BLURRING
The forward process of blurring diffusion is defined as Eq. 3, where u0 = V Tx0 denotes the
representation of the image x0 in the frequency space. The diagonal matrix Dt = eΛt defines a
non-isotropic blurring projection, where Λ(i × W + j, i × W + j) = −π2( i2
H2 +
j2
W 2 ) corresponds
to the coordinate (i, j) in the 2D frequency space. In the equation q(ut|u0) = N(ut|Dtu0, σ2
t I),
we can utilize the dot product of matrices to transform Dt and u0 into 2D matrices, ˜
Dt and ˜
u0, in
the shape of H × W for calculation:
Dtu0 ⇒˜
Dt · ˜
u0
(12)
In the super-resolution stage of RDM, we apply blurring on each k × k patch independently. We
name it as patch-wise blurring and define the diagonal blurring matrix in the shape of k × k for each
patch as:
˜Dt,k×k = exp( ˜Λk×kt),
˜Λk×k(i, j) = −π2( i2
k2 + j2
k2 ),
(13)
where i ∈[0, k), j ∈[0, k). For any patch, ˜Dt,k×k remains the same. The blurring matrix ˜Dp
t
of the patch-wise blurring is a combination of all the independent blurring matrices ˜Dt,k×k. The
relationship between the elements of ˜Dp
t and ˜Dt,k×k can be expressed as:
˜Dp
t (i, j) = ˜Dt,k×k(i mod k, j mod k),
(14)
where (i, j) corresponds to the coordinate in the 2D frequency space. Finally, Dp
t in Eq. 7 can be
formulated as:
Dp
t = diag(unfold( ˜Dp
t )),
(15)
where unfold( ˜Dp
t ) means unfolding the H×W matrix into a vector of HW dimensions and diag(v)
denotes the diagonal matrix with vector v as its diagonal line.
A.2
COMBINATION OF SCHEDULE
We follow Karras et al. (2022) to set the noise schedule for standard diffusion as ln(σ) ∼
N(Pmean, P 2
std). We use FD and F−1
D to denote the cumulative distribution function (CDF) and the
inverse distribution function (IDF) for distribution D in the following description. With t sampled
from uniform distribution U(0, 1), the noise scale is formulated as:
σ(t) = exp(F−1
N(Pmean,P 2
std)(t)).
(16)
For the super-resolution stage of RDM, we apply a truncated version of diffusion noise schedule
σ′(t), t ∼U(0, 1). If we set ts as the starting point of the truncation, the new noise schedule can be
formally expressed as:
σ′(t) = σ(F−1
U(0,1)(FU(0,1)(ts)FU(0,1)(t))),
(17)
which means we only sample the noise scale σ′ from positions of the normal distribution
N(Pmean, P 2
std) where its CDF is less than ts.
For the process of blurring, we set its schedule following the setting of Hoogeboom & Salimans
(2022). They found that the heat dissipation is equivalent to a Gaussian blur with the variance of its
kernel as σ2
B,t = 2τt. They set the blurring scale σB,t as:
σB,t = σB,max sin2(tπ
2 ),
(18)
where t is also sampled from the uniform distribution U(0, 1) and σB,max denotes a fixed hyperpa-
rameter. Empirically, we set σB,max = 3 for ImageNet 256 × 256 and σB,max = 2 for CelebA-HQ
256 × 256. The blurring matrix is formulated as Dt = eΛτt, where τt =
σ2
B,t
2 . As illustrated in
Section 2.2, Λ is a diagonal matrix and Λi×W +j = −π2( i2
H2 +
j2
W 2 ) for coordinate (i, j).
13

--- Page 14 ---

Preprint
A.3
SAMPLER DERIVATION
In this section, we prove the consistency between the design of our sampler and the formulation
of blurring diffusion. We need to prove that the jointly distribution qδ(un−1|un, u0) we define in
Eq. 10 matches with the marginal distribution
qδ(un|u0) = N(un|Dp
tnu0, σ2
tnI)
(19)
under the condition of Eq. 9.
proof. Given that qδ(uN|u0) = N(uN|Dp
tN u0, σ2
tN I), we proceed with a mathematical induction
approach. Assuming that for any n ≤N, qδ(un|u0) = N(un|Dp
tnu0, σ2
tnI) holds. We only need
to prove qδ(un−1|u0) = N(un−1|Dp
tn−1u0, σ2
tn−1I), and then the conclusion above will be proved
based on the induction hypothesis.
Firstly, based on
qδ(un−1|u0) =
Z
qδ(un−1|un, u0)q(un|u0)dun,
(20)
we introduce
qδ(un−1|un, u0) = N
 un−1| 1
σtn
(
q
σ2
tn−1 −δ2nun + (σtnDp
tn−1 −
q
σ2
tn−1 −δ2nDp
tn)u0), δ2
nI

(21)
and
qδ(un|u0) = N(un|Dp
tnu0, σ2
tnI).
(22)
Then according to Bishop & Nasrabadi (2006), qδ(un−1|u0) is also a Gaussian distribution:
qδ(un|u0) = N(un|µn−1, Σn−1).
(23)
Therefore, from Eq. 20, we can derive that
µn−1 =
1
σtn
(
q
σ2
tn−1 −δ2nDp
tnu0 + (σtnDp
tn−1 −
q
σ2
tn−1 −δ2nDp
tn)u0) = Dp
tn−1u0
(24)
and
Σn−1 =
σ2
tn−1 −δ2
n
σ2
tn
σ2
tnI + δ2
nI = σ2
tn−1I.
(25)
Summing up, qδ(un−1|u0) = N(un−1|Dp
tn−1u0, σ2
tn−1I). The inductive proof is complete.
B
HYPERPARAMETERS
Hyperparameters we use for the training of RDM are presented in Table 4. We set the architecture
hyperparameters for diffusion models following Dhariwal & Nichol (2021), in corresponding to
the input resolutions. For the experiments on CelebA-HQ, we set the model dropout to be larger
(0.15 and 0.2 for two stages respectively), and enable sample augmentation to prevent RDM from
overfitting.
C
DETAILS ABOUT THE POWER SPECTRAL DENSITY
C.1
CALCULATION PROCEDURE OF THE PSD
We follow the setting of Rissanen et al. (2022) to calculate the PSD in the frequency space. The
PSD at a certain frequency is defined as the square of the DCT coefficient at that frequency. Firstly,
we transform the image into the 2D frequency space by DCT and set the frequency range to [0, π].
To obtain the 1D curve of the PSD, we calculate the distance from each point (x, y) to the origin
in the frequency space, i.e.
p
x2 + y2, considering it as a 1D frequency value. Subsequently, we
uniformly divide the frequency domain into N intervals, and take the midpoint of each interval as
its representative frequency value. Finally, we take the mean of the PSD values for all points within
the interval as the PSD value for that interval, in order to get N coordinate pairs for plotting. The
SNR curve in Figure 2 can be obtained in a similar approach, while the only difference is that the
vertical axis values are replaced with the absolute value of the ratio between the DCT coefficients
for the image and noise in the frequency space.
14

--- Page 15 ---

Preprint
ImageNet 64
ImageNet 64→256
CelebA-HQ 64
CelebA-HQ 64→256
Diffusion steps
256
100
120
53
Noise Schedule
cosine
linear
linear
linear
Model size
295M
553M
295M
553M
GFLOPs
104
1117
104
1117
Mixed-precision (FP16)
✓
✓
-
✓
Channels
192
256
192
256
Channels multiple
1,2,3,4
1,1,2,2,4,4
1,2,3,4
1,1,2,2,4,4
Heads Channels
64
64
64
64
Attention resolution
32,16,8
32,16,8
32,16,8
32,16,8
Dropout
0.1
0.1
0.15
0.2
Augment probability
0
0
0.2
0.2
Blurring σmax
-
3.0
-
2.0
Batch size
4096
4096
1024
1024
Training Images
2500M
1000M
70M
40M
Learning Rate
1e-4
1e-4
1e-4
1e-4
Table 4: Hyperparameters for RDM.
C.2
ANALYSIS OF THE PSD
As shown in Figure 6, the PSD of real images gradually decreases from low frequency to high fre-
quency. And the intensity of Gaussian noise components across all frequency bands is generally
equal. Therefore, when corrupting real images, Gaussian noise initially drowns out high-frequency
components until the noise intensity becomes high enough to drown out the low-frequency compo-
nents of real images. And it is demonstrated in Figure 2 that, as the resolution of images increases,
less information is corrupted under the same noise intensity. Correspondingly, as shown in Fig-
ure 6(a) and Figure 6(b), the low-frequency portion of the PSD gets drowned out more slowly as the
resolution increases. It is indicated that we will introduce excessive high-frequency components of
noise when corrupting the low-frequency information of real images, especially for high-resolution
images.
Differently, the low-frequency portion of the PSD from block noise is notably higher than that of
Gaussian noise with the same intensity. Furthermore, the PSD of block noise exhibits a decreasing
trend as frequency increases, and its curve is quite similar to the PSD curve of Gaussian noise at the
resolution of 64 upsampled to the resolution of 256. This leads to the PSD curves of high-resolution
images with added block noise and that of low-resolution images with added Gaussian noise also
being quite similar. As a result, the low-frequency portion of the PSD from images with added
block noise gets drowned out more quickly than that from images with added Gaussian noise. We
can conclude that block noise can corrupt the low-frequency components of images more easily.
Figure 6: The power spectral density (PSD) of real images after adding (a) 64px Gaussian noise, (b)
256px Gaussian noise and (c) 256px block noise with block size of 4. The black curve represents
the PSD of real images. The red curves, from dark to light, represent adding noise with increasing
intensity. In order to make comparisons within the same frequency space, for the images at the
resolution of 64, we firstly upsample them to the pixel space at the resolution of 256.
15

--- Page 16 ---

Preprint
D
ADDITIONAL SAMPLES
Section 4.3 quantitatively compares the performance of RDM with other models under the same
NFE and demonstrates the superiority of RDM with fewer sampling steps. Figure 7 shows quali-
tative comparison results. While other models achieve competitive quality of generation with suf-
ficient NFE, their performances degenerate noticeably with the decrease of NFE. In contrast, RDM
still maintains comparable generation quality with a low NFE.
Figure 8 compares visualized samples generated by the best settings of StyleGAN-XL (Sauer et al.,
2022), DiT (Peebles & Xie, 2022) and RDM. StyleGAN-XL is in the framework of GAN, while
DiT and RDM are diffusion models. RDM achieves the best quality of images synthesis. Figure 9
exhibits more examples generated by our model RDM on ImageNet 256 × 256.
Figure 7: Comparison of ImageNet samples with varied NFE. DiT-XL/2 (left) vs MDT-XL/2 (mid-
dle) vs RDM (right). The allocation of NFE between the two stages of RDM is: [2, 18], [8, 32], [20,
60], [40, 120].
16

--- Page 17 ---

Preprint
Figure 8: Comparison of best ImageNet samples. StyleGAN-XL (FID 2.30, left) vs DiT-XL/2 (FID
2.27, middle) vs RDM (FID 1.87, right).
17

--- Page 18 ---

Preprint
Figure 9: Additional ImageNet samples generated by RDM. Classes are 279: Arctic fox, 90: lori-
keet, 301: ladybug, 973: coral reef, 980: volcano, 497: church, 717: pickup truck, 927: trifle.
18

```
