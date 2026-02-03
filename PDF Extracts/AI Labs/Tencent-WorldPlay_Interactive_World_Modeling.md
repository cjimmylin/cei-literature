---
title: "WorldPlay Interactive World Modeling"
source_pdf: "/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/AI Labs/Tencent/HunyuanVideo/WorldPlay_Interactive_World_Modeling.pdf"
company: "Tencent"
pages: 18
extracted_at: "2026-02-02T16:29:05.091810"
type: "ai_lab_paper"
---

# WorldPlay Interactive World Modeling

**Company/Lab:** Tencent
**Model:** HunyuanVideo
**Source PDF:** /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/AI Labs/Tencent/HunyuanVideo/WorldPlay_Interactive_World_Modeling.pdf
**Total Pages:** 18

---

## Content

```
--- Page 1 ---

WorldPlay: Towards Long-Term Geometric Consistency for Real-Time
Interactive World Modeling
Wenqiang Sun* 1,3, Haiyu Zhang* 2,3, Haoyuan Wang* 3, Junta Wu3, Zehan Wang3,
Zhenwei Wang3, Yunhong Wang2, Jun Zhang† 1, Tengfei Wang† 3, Chunchao Guo† 3
1Hong Kong University of Science and Technology
2Beihang University
3 Tencent Hunyuan
b) Stylized World 
W
D
A
S
c) Third-Person
d) 3D Reconstruction
Point Cloud
W
W
W
W
e) Promptable Event
Smoke Spread
W
W
S
S
a) Real World 
Figure 1. WorldPlay is a real-time, interactive world model that achieves long-term geometric consistency. It responds to user
navigation commands in a streaming fashion, while maintaining scenes remain coherent when revisiting (shown in red boxes). Our model
shows remarkable generalization across diverse scenes, including (a) real world, (b) stylized world, and (c) third-person agent control.
Furthermore, it supports (d) 3D scene generation via reconstruction and (e) dynamic world events triggered by text-based manipulation.
Abstract
This paper presents WorldPlay, a streaming video diffusion
model that enables real-time, interactive world modeling
with long-term geometric consistency, resolving the trade-
off between speed and memory that limits current methods.
WorldPlay draws power from three key innovations. 1) We
use a Dual Action Representation to enable robust action
control in response to the user’s keyboard and mouse in-
puts. 2) To enforce long-term consistency, our Reconsti-
*Equal contribution. †Corresponding author.
tuted Context Memory dynamically rebuilds context from
past frames and uses temporal reframing to keep geomet-
rically important but long-past frames accessible, effec-
tively alleviating memory attenuation. 3) We also propose
Context Forcing, a novel distillation method designed for
memory-aware model. Aligning memory context between
the teacher and student preserves the student’s capacity
to use long-range information, enabling real-time speeds
while preventing error drift.
Taken together, WorldPlay
generates long-horizon streaming 720p video at 24 FPS
with superior consistency, comparing favorably with exist-
ing techniques and showing strong generalization across
1
arXiv:2512.14614v1  [cs.CV]  16 Dec 2025

--- Page 2 ---

diverse scenes.
Project page and online demo can be
found: https://3d-models.hunyuan.tencent.com/world/ and
https://3d.hunyuan.tencent.com/sceneTo3D.
1. Introduction
World models are driving a pivotal shift in computational
intelligence, moving beyond language-centric tasks towards
visual and spatial reasoning. By simulating dynamic 3D en-
vironments, these models empower agents to perceive and
interact with complex surroundings, opening up new possi-
bilities for embodied robotics and game development.
At the forefront of world modeling is real-time interac-
tive video generation, which aims at autoregressively pre-
dicting future video frames (or chunks) to deliver instant
visual feedback in response to every user’s keyboard com-
mand.
Despite significant progress, a fundamental chal-
lenge persists: how to simultaneously achieve real-time
generation (speed) and long-term geometric consistency
(memory) in interactive world modeling. One class of meth-
ods [9, 17, 49] prioritizes speed with distillation but neglects
memory, resulting in inconsistency where scenes change
upon revisit. The other class preserves consistency with
explicit [32, 52] or implicit [67, 74] memory, but complex
memory makes distillation non-trivial (Sec. 3.4). As sum-
marized in Table 1, the simultaneous achievement of both
low latency and high consistency remains an open problem.
To tackle this challenge, we develop WorldPlay, a real-
time and long-term consistent world model for general
scenes.
We consider this problem as a next chunk (16
frames) prediction task for generating streaming videos
conditioned on action from users. Building upon autore-
gressive diffusion models, WorldPlay draws power from the
model’s three key ingredients below.
The first is Dual Action Representation for control over
agent and camera movement. Previous works [9, 17, 49]
typically rely on discrete keyboard inputs (e.g., W, A, S,
D) as action signals, which afford plausible, scale-adaptive
movement but suffer from ambiguity for memory retrieval
that requires revisiting exact locations. Conversely, continu-
ous camera poses (R, T) provide spatial locations but cause
training instability due to scene scale variance in training
data. To combine the best of both worlds, we convert ac-
tion signals into continuous camera poses and discrete keys,
achieving robust control and accurate location caching.
The second key design is Reconstituted Context Mem-
ory for maintaining long-term geometric consistency. We
actively reconstitute the memory through a two-stage pro-
cess, moving beyond simple retrieval [67, 74]. It first dy-
namically rebuilds a context set by querying past frames
based on spatial and temporal proximity.
To overcome
the long-range decay (the fading influence of distant to-
kens in Transformers [58]), we propose temporal reframing
to rewrite positional embeddings of these retrieved frames.
This operation effectively “pulls” geometrically important
but long-past memories closer in time, forcing the model
to treat them as recent. This process keeps the influence of
relevant long-range information preserved, enabling robust
free extrapolation with strong geometric consistency.
The final key ingredient is Context Forcing, a novel
distillation method designed for memory-aware models to
enable real-time generation.
Existing distillation meth-
ods [6, 21, 70] fail to keep long-term memory as there is
a fundamental distribution mismatch: training a memory-
aware autoregressive student to mimic a memory-less bidi-
rectional teacher.
Even when augmenting teacher with
memory, mismatched memory context will cause distribu-
tion diverge. We solve this by aligning the memory con-
text for teacher and student during distillation. This align-
ment facilitates effective distribution matching, enabling
real-time speed without eroding the memory while allevi-
ating error accumulation over long sequences.
Taken together, WorldPlay achieves real-time, interac-
tive video generation at 24 FPS (720p) while maintaining
long-term geometric consistency under streaming user con-
trol. The model is built on a large-scale, curated dataset of
320K real and synthetic videos with a custom rendering and
processing platform. As shown in Fig. 1, WorldPlay shows
superior generation quality and remarkable generalization
across diverse scenes including first- and third-person real
and stylized worlds, and supports applications ranging from
3D reconstruction and promptable events.
2. Related Work
Video Generation.
Diffusion models [19, 41, 57] have
emerged as the state-of-the-art approach in video genera-
tive modeling. [7, 15, 69] adopt the latent diffusion model
(LDM) [53] to learn video distribution in the latent space,
achieving efficient video generation. Recently, autoregres-
sive video generation models [6, 18, 26] theoretically en-
able one to generate unlimited length videos, laying the
foundation for world models.
With the advancement of
powerful architectures [50] and sophisticated data pipelines,
[10, 13, 28, 30, 47, 62], which are trained on web-scale
datasets, have demonstrated emergent zero-shot capabilities
to perceive, model, and manipulate the visual world [65],
making it feasible to simulate the physical world.
Interactive and Consistent World Models. World mod-
els aim to predict future states based on current and past
observations and actions.
Studies such as [1–3, 16, 29,
31, 33, 46, 48, 59–61, 64, 75] adopt discrete or continu-
ous action signals to enable agents to navigate and interact
with virtual environments. Subsequent works that aim to
achieve geometric consistency can be categorized into two
types: explicit 3D reconstruction and implicit conditioning.
[4, 32, 42, 52, 73, 76, 77] try to ensure spatial consistency
2

--- Page 3 ---

Oasis [9]
Matrix-Game
2.0 [17]
GameGenX [5]
GameCraft [31]
WorldMem [67]
VMem [32]
WorldPlay
Resolution
360P
360p
720p
720p
360P
576p
720p
Action Space
Discrete
Discrete
Discrete
Continuous
Discrete
Continuous
Continuous +
Discrete
Real-time
✔
✔
✗
✗
✗
✗
✔
Long-term
Consistency
✗
✗
✗
✗
✔
✔
✔
Long-Horizon
✗
✔
✔
✗
✗
✗
✔
Domain
Minecraft
General
General
General
Minecraft
Static Scene
General
Table 1. Comparison with recent interactive world models. WorldPlay distinguishes itself as a general-domain model that simultaneously
achieves long-horizon video generation, flexible action control, real-time interactivity, and long-term geometric consistency.
by explicitly reconstructing 3D representations and render-
ing condition frames from these representations. However,
they heavily rely on reconstruction quality, making it chal-
lenging to maintain long-term consistency.
Other recent
works [23] construct 3D world models explicitly, without
relying on video generation models. Although achieving
promising 3D generation results, these lines of methods
can not be performed in real-time usage cases.
In con-
trast, [67, 74] achieve implicit conditioning by leveraging
field-of-view (FOV) to retrieve relevant context from his-
torical frames, demonstrating strong scalability. However,
developing a real-time world model that maintains geomet-
ric consistency remains an open question.
Distillation. Real-time capability is also an essential prop-
erty for world models. For video diffusion models, existing
approaches typically employ distillation [12, 14, 35, 54, 78]
to achieve few-step inference, thereby achieving real-time
generation. For instance, [24, 37–39, 55, 56] adopt adver-
sarial training strategies to enable few-step inference, how-
ever, they often suffer from training instability and mode
collapse. [45, 70, 71] utilize Variational Score Distillation
(VSD) [63] to achieve outstanding few-step generation per-
formance. In addition, CausVid [72] proposes distilling a
causal student model from a bidirectional teacher diffusion
model to achieve real-time autoregressive generation. Fur-
thermore, Self-Forcing [21] addresses exposure bias by re-
fining the rollout strategy of CausVid. Our method proposes
context forcing to preserve both the interactivity and geo-
metric consistency while achieving real-time generation.
3. Method
Our goal is to construct a geometry-consistent and real-
time interactive world model Nθ(xt|Ot−1, At−1, at, c) pa-
rameterized by θ, which can generate next chunk xt (a
chunk is a few frames) based on past observations Ot−1 =
{xt−1, ..., x0}, action sequences At−1 = {at−1, ..., a0},
and current action at. Here, c is a text prompt or image
that describes the world.
For simplicity of notation, we
omit A, a, c in following sections. We first introduce the
relevant preliminaries in Sec. 3.1. In Sec. 3.2, we discuss
the action representation for control. Sec. 3.3 describes our
reconstituted context memory to ensure long-term geomet-
ric consistency, followed by Sec. 3.4 covering our context
forcing, which mitigates exposure bias and enables few-step
generation while maintaining long-term consistency.
Fi-
nally, Sec. 3.5 details additional optimizations for real-time
streaming generation. The pipeline is shown in Fig. 2.
3.1. Preliminaries
Full-sequence Video Diffusion Model. Current video dif-
fusion models [28, 62] typically consist of a causal 3D
VAE [27] and a Diffusion Transformer (DiT) [50], where
each DiT block is composed of 3D self-attention, cross-
attention, and feedforward network (FFN). The diffusion
timestep is processed by positional embedding (PE) and a
Multi-Layer Perceptron (MLP) to modulate the DiT blocks.
The model is trained using flow matching [41].
Specif-
ically, given a video latent z0 encoded by the 3D VAE,
a random noise z1 ∼N(0, I), and a diffusion timestep
k ∈[0, 1], an intermediate latent zk is obtained through
linear interpolation. The model is trained to predict the ve-
locity vk = z0 −z1,
LFM(θ) = Ek,z0,z1
Nθ(zk, k) −vk

2
.
(1)
Chunk-wise Autoregressive Generation.
However, the
full-sequence video diffusion model is a non-causal archi-
tecture, which limits its ability for infinite-length interactive
generation. Inspired by Diffusion Forcing [6], we finetune
it into a chunk-wise autoregressive video generation model.
Specifically, for video latent z0 ∈RC×T ×H×W , we divide
it into T
4 chunks {zi
0 ∈RC×4×H×W |i = 0, ..., T
4 −1}, and
thus each chunk (4 latents) can be decoded into 16 frames.
During training, we add different noise levels ki for each
chunk and modify the full-sequence self-attention to block
3

--- Page 4 ---

Figure 2. Method overview. Given a single image or text prompt to describe a world, WorldPlay performs a next chunk (16 video frames)
prediction task to generate future videos conditioned on action from users. For the generation of each chunk, we dynamically reconstitute
context memory from past chunks to enforce long-term temporal and geometric consistency.
Figure 3.
Detailed architecture of our autoregressive diffusion
transformer. The discrete key is incorporated with time embed-
ding, while the continuous camera pose is injected into causal self-
attention through PRoPE [33].
causal attention. The training loss is similar to Eq. 1.
3.2. Dual Action Representation for Control
Existing methods use keyboard and mouse inputs as ac-
tion signals and inject the action control via MLP [9, 67]
or attention blocks [17, 74].
This enables the model to
learn physically plausible movements across scenes with di-
verse scales (e.g. very large and small scenes). However,
they struggle to provide precise previous locations for spa-
tial memory retrieval. In contrast, camera poses (rotation
matrix and translation vector) provide accurate spatial loca-
tions that facilitate precise control and memory retrieval, but
training only with camera poses faces challenges in training
stability due to the scale variance in the training data. To ad-
dress this, we propose a dual action representation that com-
bines the best of both worlds as shown in Fig. 3. This design
not only caches spatial locations for our memory module in
Sec. 3.3, but also enables robust and precise control. Specif-
ically, we employ PE and a zero-initialized MLP to encode
discrete keys and incorporate it into the timestep embed-
ding, which is then used to modulate the DiT blocks. For
continuous camera pose, we leverage relative positional en-
coding, i.e., PRoPE [33], which offers greater generalizabil-
ity than commonly used raymaps, to inject complete cam-
era frustums into self-attention blocks. The original self-
attention computation is as follows,
Attn1 = Attn(R⊤⊙Q, R−1 ⊙K, V ),
(2)
where R represents the 3D rotary PE (RoPE) [58] for video
latents. To encode frustum relationships between cameras,
we utilize an additional attention computation,
Attn2 =Dproj ⊙Attn((Dproj)⊤⊙Q,
(Dproj)−1 ⊙K, (Dproj)−1 ⊙V ),
(3)
here, Dproj is derived from the camera’s intrinsic and ex-
trinsic parameters, as described in [33]. Finally, the result
of each self-attention block is Attn1 + zero init(Attn2).
3.3. Reconstituted ContextMemory for Consistency
Maintaining long-term geometric consistency requires re-
calling past frames, ensuring content remains unchanged
when revisiting to a previous location. However, naively
4

--- Page 5 ---

(a) Full context
(b) Absolute indices
(c) Relative indices
Figure 4. Memory mechanism comparisons. The red and blue
blocks represent the memory and current chunk, respectively. The
number in each block represents the temporal index in RoPE. For
simplicity of illustration, each chunk only contains one frame.
using all past frames as context (Fig. 4a) is computation-
ally intractable and redundant for long sequences. To ad-
dress this, we rebuild a memory context Ct from past
chunks Ot−1 for each new chunk xt. Our approach ad-
vances beyond prior work [67, 74] by combining both short-
term temporal cues and long-range spatial references: 1) A
temporal memory (CT
t ) comprises L most recent chunks
{xt−L, ..., xt−1} to ensure short-term motion smoothness.
2) A spatial memory (CS
t ) samples from non-adjacent past
frames to prevent geometric drift over long sequences,
where CS
t ⊆Ot−1 −CT
t . This sampling is guided by ge-
ometric relevance scores that incorporate both FOV overlap
and camera distance.
Once memory context is rebuilt, the challenge shifts to
applying them to enforce consistency. Effectively using re-
trieved context requires overcoming a fundamental flaw in
positional encodings. With standard RoPE (Fig.4b), the dis-
tance between the current chunk and past memory grows
unbounded over time. This growing relative distance can
eventually exceed the trained interpolation range in RoPE,
causing extrapolation artifacts [58].
More critically, the
growing perceived distance to these long-past spatial mem-
ory would weaken their influence on the current prediction.
To resolve this, we propose Temporal Reframing (Fig.4c).
We discard the absolute temporal indices, and dynamically
re-assign new positional encodings to all context frames, es-
tablishing a fixed, small relative distance to the current, irre-
spective of their actual temporal gap. This operation effec-
tively “pulls” important past frames closer in time, ensuring
they remain influential and enabling robust extrapolation for
long-term consistency.
3.4. Context Forcing
Autoregressive models often suffer from error accumulation
during long video generation, leading to degraded visual
quality over time [21, 72]. Moreover, the multi-step denois-
ing of diffusion models is too slow for real-time interaction.
Recent methods [8, 21, 43, 68] address these challenges by
distilling a powerful bidirectional teacher diffusion model
Figure 5.
Context forcing is a novel distillation method that
employs memory-augmented self-rollout and memory-augmented
bidirectional video diffusion to preserve long-term consistency,
enable real-time interaction, and mitigate error accumulation.
into a fast, few-step autoregressive student.
These tech-
niques force the student’s output distribution pθ(x0:t) to
align with the teacher’s, thereby improving generation qual-
ity by employing a distribution matching loss [70]:
∇θLDMD = Ek(∇θKL(pθ(x0:t)||pdata(x0:t))),
(4)
where the gradient of the reverse KL can be approximated
by the score difference derived from teacher model.
However, these methods are incompatible with memory-
aware models due to a critical distribution mismatch. Stan-
dard teacher diffusion models are trained on short clips
and are inherently memory-less. Even if a teacher is aug-
mented with memory, its bidirectional nature inevitably dif-
fers from the student’s causal, autoregressive process. This
means that without a meticulously designed memory con-
text to mitigate this gap, the difference in memory con-
text will make their conditional distributions p(x|C) mis-
aligned, which in turn causes distribution matching to fail.
We thus propose context forcing as shown in Fig. 5,
which alleviates the memory context misalignment between
teacher and student for distillation. For the student model,
we self-rollouts 4 chunks conditioned on the memory con-
text pθ(xj:j+3|x0:j−1) =
j+3
Q
i=j
pθ(xi|Ci).
To construct our teacher model Vβ, we augment a stan-
dard bidirectional diffusion model with memory, and struc-
ture its context by masking xj:j+3 from student’s memory
context,
pdata(xj:j+3|x0:j−1) = pβ(xj:j+3|Cj:j+3 −xj:j+3), (5)
where Cj:j+3 denotes all context memory chunks corre-
sponding to student’s self-rollout xj:j+3. By aligning the
memory context with the student model, we enforce the dis-
tributions represented by the teacher to be as close as pos-
sible to the student model, which enables more effectively
distribution matching. Moreover, this avoids training Vβ on
long videos and redundant context, facilitating the learning
5

--- Page 6 ---

W
W
A
A
D
D
D
D
S
S
S
S
Ours
GameCraft
D
S
Ours
Gen3C
Ours
GameCraft
D
D
D
A
A
A
D
D
D
A
A
A
W
W
D
D
D
D
W
W
D
D
D
D
Ours
Matrix-Game 2.0
W
S
W
S
Ours
Matrix-Game 2.0
W
S
A
D
W
S
A
D
W
S
A
D
W
S
A
D
W
S
A
D
Figure 6. Qualitative comparisons with existing methods. WorldPlay achieves the state-of-the-art long-term consistency (shown in red
boxes) and visual quality across diverse scenes, including both first- and third-person real and stylized worlds.
of long-term visual distribution. Through context forcing,
we preserve long-term consistency in real-time generation
with 4-denoising steps, and mitigate error accumulation.
3.5. Streaming Generation with Real-Time Latency
We augment context forcing with a suite of optimizations to
minimize latency, unlocking an interactive streaming expe-
rience at 24 FPS and 720p resolution on 8×H800 GPUs.
Mixed parallelism method for DiT and VAE. Unlike the
conventional parallelism method that replicates the entire
model or adapting sequence parallelism on the temporal di-
mension, our parallelism method combines sequence par-
allelism [34] and attention parallelism, which partitions
the tokens of each entire chunk across devices. This de-
sign ensures that the computational workload for generating
each chunk is distributed evenly, substantially reducing per-
chunk inference time while maintaining generation quality.
Streaming deployment and progressive decoding.
To
minimize time-to-first-frame and enable seamless interac-
tion, we adopt a streaming deployment architecture using
NVIDIA Triton Inference Framework and implement a pro-
gressive multi-step VAE decoding strategy that decodes and
streams frames in smaller batches. Upon generating latent
representations from the DiT, frames are progressively de-
coded, allowing users to observe generated content while
subsequent frames are still being processed. This streaming
pipeline ensures smooth, low-latency interaction even under
varying computational loads.
Quantization and efficient attention.
Furthermore, we
employ a comprehensive suite of quantization strategies.
Specifically, we adopt Sage Attention [79], float quanti-
zation, and matrix multiplication quantization to improve
the inference performance. Additionally, we use KV-cache
mechanisms for attention modules to eliminate redundant
computations during autoregressive generation.
6

--- Page 7 ---

Short-term (61 frames)
Long-term (≥250 frames)
Real-time
PSNR ↑
SSIM ↑
LPIPS ↓
Rdist ↓
Tdist ↓
PSNR ↑
SSIM ↑
LPIPS ↓
Rdist ↓
Tdist ↓
CameraCtrl [16]
✗
17.93
0.569
0.298
0.037
0.341
10.09
0.241
0.549
0.733
1.117
SEVA [80]
✗
19.84
0.598
0.313
0.047
0.223
10.51
0.301
0.517
0.721
1.893
ViewCrafter [77]
✗
19.91
0.617
0.327
0.029
0.543
9.32
0.277
0.661
1.573
3.051
Gen3C [52]
✗
21.68
0.635
0.278
0.024
0.477
15.37
0.431
0.483
0.357
0.979
VMem [64]
✗
19.97
0.587
0.316
0.048
0219
12.77
0.335
0.542
0.748
1.547
Matrix-Game-2.0 [17]
✔
17.26
0.505
0.383
0.287
0.843
9.57
0.205
0.631
2.125
2.742
GameCraft [31]
✗
21.05
0.639
0.341
0.151
0.617
10.09
0.287
0.614
2.497
3.291
Ours (w/o Context Forcing)
✗
21.27
0.669
0.261
0.033
0.157
16.27
0.425
0.495
0.611
0.991
Ours (full)
✔
21.92
0.702
0.247
0.031
0.121
18.94
0.585
0.371
0.332
0.797
Table 2.
Quantitative comparisons.
We compare against both methods without memory, i.e., CameraCtrl [16], SEVA [80],
ViewCrafter [77], Matrix-Game-2.0 [17], and GameCraft [31], and methods with memory, i.e., Gen3C [52], VMem [32]. Our method
achieves superior results, particularly in long-term settings, which more clearly demonstrate the long-term consistency.
4. Experiments
Dataset. WorldPlay is trained on a comprehensive dataset
comprising approximately 320K high-quality video sam-
ples derived from both real-world footage and synthetic en-
vironments. For real-world videos, we start with publicly
available real video sources [36, 40] and remove short, low-
quality clips, as well as samples containing watermarks, UI,
dense crowds, or erratic camera movement. To mitigate the
monotonous motion common in original videos, we adopt
3D Gaussian Splatting [25] for 3D reconstruction on cu-
rated videos. We then render customized videos from these
3D scenes using novel revisit trajectories. The renderings
are further refined using Difix3D+ [66] to repair floating ar-
tifacts, yielding an additional 100K high-quality real video
clips. For synthetic data, we collect hundreds of UE scenes
and generate 50K video clips by rendering complex, cus-
tomized trajectories. Also, we build a game recording plat-
form and invite dozens of players to collect 170k samples
from 1st/3rd-person AAA games with designed trajectories.
We segment each video into clips and use a vision-language
model [81] to generate text annotations. For videos without
action annotations, we employ VIPE [20] to label.
Evaluation Protocol.
Our test set comprises 600 cases
sourced from DL3DV, game videos, and AI-generated im-
ages spanning a range of styles. For the short-term setting,
we utilize the camera trajectories from the test videos as the
input pose. The generated video frames are directly com-
pared against the Ground-Truth (GT) frames to assess vi-
sual quality and camera pose accuracy. For the long-term
setting, we test the long-term consistency using various cus-
tom cycle camera trajectories designed to enforce revisiting.
Each model generates frames along a customize trajectory
and then returns along the same path, metrics are evaluated
on the return path by comparing the generated frame to the
corresponding frame generated during the initial pass. We
employ LPIPS, PSNR, and SSIM to measure visual quality
and Rdist and Tdist to quantify action accuracy.
Baselines. We conduct comprehensive comparisons against
various baselines, which mainly fall into two categories: 1)
Action-controlled diffusion models without memory: Cam-
eraCtrl [16], SEVA [80], ViewCrafter [77], Matrix-Game
2.0 [17] and GameCraft [31]; 2) Action-controlled diffusion
models with memory: Gen3C [52] and VMem [32]. More
evaluation results can be found in our appendix.
4.1. Main Result
Quantitative Results. As shown in Table 2, in the short-
term regime, our approach achieves superior visual fi-
delity and maintains competitive control accuracy.
Al-
though methods leveraging explicit 3D representations (i.e.
ViewCrafter [77], Gen3C [52]) realize more accurate rota-
tion, they suffer from issues such as the inaccurate depth
estimation and inconsistent scale when performing move-
ment translations. For more challenging long-term scenar-
ios, where action accuracy generally degrades, our method
remains more stable and achieves the best performance.
Regarding long-term geometric consistency, Matrix-Game-
2.0 [17] and GameCraft [31] exhibit poor performance due
to the lack of memory mechanism. Although VMem [32]
and Gen3C [52] employ explicit 3D cache to maintain con-
sistency, they are constrained by depth accuracy and align-
ment, making it difficult to achieve robust long-term con-
sistency. Benefiting from Reconstituted Context Memory,
we achieve improved long-term consistency.
Moreover,
through context forcing, we further prevent error accumu-
lation, resulting in better visual quality and action accu-
racy. Crucially, WorldPlay concurrently achieves the req-
uisite real-time interactivity for immersive simulation.
Qualitative Results. We provide qualitative comparisons
with baselines in Fig. 6. The explicit 3D cache used in
Gen3C [52] is highly sensitive to the quality of interme-
diate outputs and limited by the accuracy of depth estima-
tion. Conversely, our reconstituted context memory guaran-
tees long-term consistency with more robust implicit prior,
achieving superior scene generalizability.
Matrix-Game-
2.0 [17] and GameCraft [31] fail to support free exploration
due to the lack of memory. Furthermore, they do not gen-
7

--- Page 8 ---

Action
PSNR↑
SSIM↑
LPIPS↓
Rdist ↓
Tdist ↓
Discrete
21.47
0.661
0.248
0.103
0.615
Continuous
21.93
0.665
0.231
0.038
0.287
Full
22.09
0.687
0.219
0.028
0.113
Table 3. Ablation for action representation. We conduct valida-
tion using the bidirectional model.
a) RoPE
b) Reframed RoPE (Ours)
W
W
D
D
Error Accumulation
A
A
A colossal stone Buddha statue 
dominates the center of the image, 
nestled between towering, mist-
shrouded cliffs. A burning incense 
burner sits in the foreground on a 
snow-covered ground.
Geometric Inconsistency
a) RoPE
b) Reframed RoPE (Ours)
W
W
A
A
S
S
Figure 7.
RoPE design comparisons.
Upper: Our reframed
RoPE avoids exceeding the the positional range in standard RoPE,
alleviating error accumulation. Bottom: By maintaining a small
relative distance to long-range spatial memory, it achieves better
long-term consistency.
eralize well to third-person scenarios, making it difficult to
control agents within the scene and limiting their applica-
bility. In contrast, WorldPlay successfully extends its ef-
ficacy to these scenarios and maintains high visual fidelity
and long-term geometric consistency.
4.2. Ablation
Action Representation. Table. 3 validates the effective-
ness of the proposed dual-action representation. When us-
ing only discrete keys as action signals, the model strug-
gles to achieve fine-grained control, such as the distance of
movement or the degree of rotation, resulting in poor perfor-
mance on Rdist and Tdist metrics. Using continuous camera
poses yields better results but converges more difficult due
to scale variance. By employing the dual-action representa-
tion, we achieve the best overall control performance.
RoPE Design.
Table. 4 presents the quantitative results
of different RoPE designs within the memory mechanism,
showing that reframed rope outperforms naive counterparts,
especially on visual metrics. As illustrated in the upper part
of Fig. 7, RoPE is more prone to error accumulation. It
also increases the distance between memory and predicted
chunk due to absolute temporal indices, resulting in weaker
geometric consistency, as shown in the lower part of Fig. 7.
Context Forcing.
To verify the importance of memory
alignment, we train the teacher model following [74], where
the memory is selected at latent level rather than at chunk
level. Although this may reduce the number of memory
context in the teacher model, it also introduce misaligned
PSNR↑
SSIM↑
LPIPS↓
Rdist ↓
Tdist ↓
RoPE
14.03
0.358
0.534
0.805
1.341
Reframed RoPE
16.27
0.425
0.495
0.611
0.991
Table 4. Ablation for positional encoding design in memory.
The results are evaluated on the long-term test data.
a) Misaligned Context
b) Self-rollout Context
c) Ours
W
S
S
W
S
S
W
S
S
Figure 8. Ablation for context forcing. a) When the teacher
and student have misaligned context, it leads to distillation failure,
resulting in collapsed outputs. b) Self-rollout historical context
can introduce artifacts. Zoom in for details.
Balloon Appears
A wide open meadow stretches to 
the horizon, covered with colourful
wildflowers swaying gently in the 
wind. The scene feels bright and calm 
under the midday sun.
Rainbow Arches
W
W
W
W
W
W
W
W
Figure 9. Promptable event. Our method supports text-based
manipulation during streaming.
context between the teacher and student model, leading to
collapsed results as shown in Fig. 8a.
Additionally, for
the past chunks x0:j−1, we attempt to self-rollout histori-
cal chunks as context following the inference-time recipe as
in [68]. However, this may cause the bidirectional diffusion
model to provide inaccurate score estimation, as it is trained
using clean chunks as memory. Consequently, this discrep-
ancy introduces artifacts as illustrated in Fig. 8b. We ob-
tain historical chunks by sampling from real videos, which
yields superior results as shown in Fig. 8c.
4.3. Application
3D Reconstruction. Benefiting from the long-term geo-
metric consistency, we can integrate a 3D reconstruction
model [44] to produce high-quality point clouds, as pre-
sented in Fig. 1 (d).
Promptable Event. Beyond navigation control, WorldPlay
supports text-based interaction to trigger dynamic world
events. As shown in Fig. 9 and Fig. 1 (e), users can prompt
at any time to responsively alter the ongoing stream.
5. Conclusion
WorldPlay is a powerful world model with real-time inter-
action and long-term geometric consistency. It empowers
8

--- Page 9 ---

users to customize unique worlds from a single image or
text prompt. While focused on navigation control, its ar-
chitecture has shown potential for richer interaction like
dynamic, text-triggered events. By providing a systematic
framework for control, memory, and distillation, WorldPlay
marks a critical step toward creating consistent and interac-
tive virtual worlds. Extending it to generate longer videos
with multi-agent interaction and complex physical dynam-
ics would be fruitful future directions.
References
[1] Eloi Alonso, Adam Jelley, Vincent Micheli, Anssi Kan-
ervisto, Amos J Storkey, Tim Pearce, and Franc¸ois Fleuret.
Diffusion for world modeling: Visual details matter in atari.
Advances in Neural Information Processing Systems, 37:
58757–58791, 2024. 2
[2] Sherwin Bahmani, Ivan Skorokhodov, Guocheng Qian, Ali-
aksandr Siarohin, Willi Menapace, Andrea Tagliasacchi,
David B Lindell, and Sergey Tulyakov. Ac3d: Analyzing
and improving 3d camera control in video diffusion trans-
formers. In CVPR, pages 22875–22889, 2025.
[3] Amir Bar, Gaoyue Zhou, Danny Tran, Trevor Darrell, and
Yann LeCun. Navigation world models. In CVPR, pages
15791–15801, 2025. 2
[4] Chenjie Cao, Jingkai Zhou, Shikai Li, Jingyun Liang,
Chaohui Yu, Fan Wang, Xiangyang Xue, and Yanwei Fu.
Uni3c:
Unifying precisely 3d-enhanced camera and hu-
man motion controls for video generation. arXiv preprint
arXiv:2504.14899, 2025. 2
[5] Haoxuan Che, Xuanhua He, Quande Liu, Cheng Jin, and
Hao Chen. Gamegen-x: Interactive open-world game video
generation. arXiv preprint arXiv:2411.00769, 2024. 3
[6] Boyuan Chen, Diego Mart´ı Mons´o, Yilun Du, Max Sim-
chowitz, Russ Tedrake, and Vincent Sitzmann.
Diffusion
forcing: Next-token prediction meets full-sequence diffu-
sion. Advances in Neural Information Processing Systems,
37:24081–24125, 2024. 2, 3
[7] Haoxin Chen, Yong Zhang, Xiaodong Cun, Menghan Xia,
Xintao Wang, Chao Weng, and Ying Shan. Videocrafter2:
Overcoming data limitations for high-quality video diffusion
models. In CVPR, pages 7310–7320, 2024. 2
[8] Justin Cui, Jie Wu, Ming Li, Tao Yang, Xiaojie Li, Rui
Wang, Andrew Bai, Yuanhao Ban, and Cho-Jui Hsieh. Self-
forcing++: Towards minute-scale high-quality video genera-
tion. arXiv preprint arXiv:2510.02283, 2025. 5
[9] Etched Decart. Oasis: A universe in a transformer. https:
//oasis-model.github.io/, 2024. 2, 3, 4
[10] Google Deepmind. Veo3 video model, 2025. https://
deepmind.google/models/veo/. 2
[11] Haoyi Duan, Hong-Xing Yu, Sirui Chen, Li Fei-Fei, and Ji-
ajun Wu. Worldscore: A unified evaluation benchmark for
world generation. arXiv preprint arXiv:2504.00983, 2025. 6
[12] Kevin Frans, Danijar Hafner, Sergey Levine, and Pieter
Abbeel.
One step diffusion via shortcut models.
arXiv
preprint arXiv:2410.12557, 2024. 3
[13] Yu Gao, Haoyuan Guo, Tuyen Hoang, Weilin Huang, Lu
Jiang, Fangyuan Kong, Huixia Li, Jiashi Li, Liang Li, Xi-
aojie Li, et al. Seedance 1.0: Exploring the boundaries of
video generation models. arXiv preprint arXiv:2506.09113,
2025. 2
[14] Zhengyang Geng, Mingyang Deng, Xingjian Bai, J Zico
Kolter, and Kaiming He. Mean flows for one-step genera-
tive modeling. arXiv preprint arXiv:2505.13447, 2025. 3
[15] Yuwei Guo, Ceyuan Yang, Anyi Rao, Zhengyang Liang,
Yaohui Wang, Yu Qiao, Maneesh Agrawala, Dahua Lin, and
Bo Dai. Animatediff: Animate your personalized text-to-
image diffusion models without specific tuning. In ICLR,
2024. 2
[16] Hao He, Yinghao Xu, Yuwei Guo, Gordon Wetzstein, Bo
Dai, Hongsheng Li, and Ceyuan Yang. Cameractrl: Enabling
camera control for text-to-video generation. In ICLR, 2025.
2, 7
[17] Xianglong He, Chunli Peng, Zexiang Liu, Boyang Wang,
Yifan Zhang, Qi Cui, Fei Kang, Biao Jiang, Mengyin An,
Yangyang Ren, et al.
Matrix-game 2.0: An open-source,
real-time, and streaming interactive world model.
arXiv
preprint arXiv:2508.13009, 2025. 2, 3, 4, 7
[18] Roberto Henschel, Levon Khachatryan, Hayk Poghosyan,
Daniil Hayrapetyan, Vahram Tadevosyan, Zhangyang Wang,
Shant Navasardyan, and Humphrey Shi. Streamingt2v: Con-
sistent, dynamic, and extendable long video generation from
text. In CVPR, pages 2568–2577, 2025. 2
[19] Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising dif-
fusion probabilistic models. Advances in neural information
processing systems, 33:6840–6851, 2020. 2
[20] Jiahui Huang, Qunjie Zhou, Hesam Rabeti, Aleksandr Ko-
rovko, Huan Ling, Xuanchi Ren, Tianchang Shen, Jun Gao,
Dmitry Slepichev, Chen-Hsuan Lin, et al.
Vipe: Video
pose engine for 3d geometric perception.
arXiv preprint
arXiv:2508.10934, 2025. 7, 2
[21] Xun Huang, Zhengqi Li, Guande He, Mingyuan Zhou,
and Eli Shechtman.
Self forcing:
Bridging the train-
test gap in autoregressive video diffusion.
arXiv preprint
arXiv:2506.08009, 2025. 2, 3, 5, 1
[22] Ziqi Huang, Yinan He, Jiashuo Yu, Fan Zhang, Chenyang Si,
Yuming Jiang, Yuanhan Zhang, Tianxing Wu, Qingyang Jin,
Nattapol Chanpaisit, et al. Vbench: Comprehensive bench-
mark suite for video generative models. In Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 21807–21818, 2024. 5, 6
[23] Team HunyuanWorld. Hunyuanworld 1.0: Generating im-
mersive, explorable, and interactive 3d worlds from words
or pixels. arXiv preprint, 2025. 3
[24] Minguk Kang, Richard Zhang, Connelly Barnes, Sylvain
Paris, Suha Kwak, Jaesik Park, Eli Shechtman, Jun-Yan Zhu,
and Taesung Park. Distilling diffusion models into condi-
tional gans. In ECCV, pages 428–447. Springer, 2024. 3
[25] Bernhard Kerbl, Georgios Kopanas, Thomas Leimk¨uhler,
and George Drettakis.
3d gaussian splatting for real-time
radiance field rendering. ACM Trans. Graph., 42(4):139–1,
2023. 7
[26] Jihwan Kim, Junoh Kang, Jinyoung Choi, and Bohyung Han.
Fifo-diffusion: Generating infinite videos from text without
9

--- Page 10 ---

training. Advances in Neural Information Processing Sys-
tems, 37:89834–89868, 2024. 2
[27] Diederik P Kingma and Max Welling. Auto-encoding varia-
tional bayes. arXiv preprint arXiv:1312.6114, 2013. 3
[28] Weijie Kong, Qi Tian, Zijian Zhang, Rox Min, Zuozhuo Dai,
Jin Zhou, Jiangfeng Xiong, Xin Li, Bo Wu, Jianwei Zhang,
et al. Hunyuanvideo: A systematic framework for large video
generative models. arXiv preprint arXiv:2412.03603, 2024.
2, 3, 1
[29] Xin Kong, Shikun Liu, Xiaoyang Lyu, Marwan Taher, Xi-
aojuan Qi, and Andrew J Davison. Eschernet: A generative
model for scalable view synthesis. In CVPR, pages 9503–
9513, 2024. 2
[30] Kuaishou.
Kling video model, 2024.
https : / /
klingai.com/global/. 2
[31] Jiaqi Li, Junshu Tang, Zhiyong Xu, Longhuang Wu, Yuan
Zhou, Shuai Shao, Tianbao Yu, Zhiguo Cao, and Qinglin Lu.
Hunyuan-gamecraft: High-dynamic interactive game video
generation with hybrid history condition.
arXiv preprint
arXiv:2506.17201, 2025. 2, 3, 7
[32] Runjia Li, Philip Torr, Andrea Vedaldi, and Tomas Jakab.
Vmem: Consistent interactive video scene generation with
surfel-indexed view memory. In ICCV, 2025. 2, 3, 7
[33] Ruilong Li, Brent Yi, Junchen Liu, Hang Gao, Yi Ma, and
Angjoo Kanazawa. Cameras as relative positional encoding.
arXiv preprint arXiv:2507.10496, 2025. 2, 4
[34] Shenggui Li, Fuzhao Xue, Chaitanya Baranwal, Yongbin Li,
and Yang You. Sequence parallelism: Long sequence train-
ing from system perspective. In Proceedings of the 61st An-
nual Meeting of the Association for Computational Linguis-
tics (Volume 1: Long Papers), pages 2391–2404, Toronto,
Canada, 2023. Association for Computational Linguistics. 6
[35] Xinyang Li, Tengfei Wang, Zixiao Gu, Shengchuan Zhang,
Chunchao Guo, and Liujuan Cao.
Flashworld:
High-
quality 3d scene generation within seconds. arXiv preprint
arXiv:2510.13678, 2025. 3
[36] Zhen Li, Chuanhao Li, Xiaofeng Mao, Shaoheng Lin, Ming
Li, Shitian Zhao, Zhaopan Xu, Xinyue Li, Yukang Feng,
Jianwen Sun, et al. Sekai: A video dataset towards world
exploration. arXiv preprint arXiv:2506.15675, 2025. 7, 2
[37] Shanchuan Lin, Anran Wang, and Xiao Yang.
Sdxl-
lightning:
Progressive adversarial diffusion distillation.
arXiv preprint arXiv:2402.13929, 2024. 3
[38] Shanchuan Lin, Xin Xia, Yuxi Ren, Ceyuan Yang, Xuefeng
Xiao, and Lu Jiang. Diffusion adversarial post-training for
one-step video generation. 2025.
[39] Shanchuan Lin, Ceyuan Yang, Hao He, Jianwen Jiang, Yuxi
Ren, Xin Xia, Yang Zhao, Xuefeng Xiao, and Lu Jiang.
Autoregressive adversarial post-training for real-time inter-
active video generation. arXiv preprint arXiv:2506.09350,
2025. 3
[40] Lu Ling, Yichen Sheng, Zhi Tu, Wentian Zhao, Cheng Xin,
Kun Wan, Lantao Yu, Qianyu Guo, Zixun Yu, Yawen Lu,
et al.
Dl3dv-10k: A large-scale scene dataset for deep
learning-based 3d vision.
In CVPR, pages 22160–22169,
2024. 7, 2
[41] Yaron Lipman, Ricky TQ Chen, Heli Ben-Hamu, Maximil-
ian Nickel, and Matt Le. Flow matching for generative mod-
eling. In ICLR, 2023. 2, 3
[42] Fangfu Liu, Wenqiang Sun, Hanyang Wang, Yikai Wang,
Haowen Sun, Junliang Ye, Jun Zhang, and Yueqi Duan. Re-
conx: Reconstruct any scene from sparse views with video
diffusion model. arXiv preprint arXiv:2408.16767, 2024. 2
[43] Kunhao Liu, Wenbo Hu, Jiale Xu, Ying Shan, and Shijian
Lu. Rolling forcing: Autoregressive long video diffusion in
real time. arXiv preprint arXiv:2509.25161, 2025. 5
[44] Yifan Liu, Zhiyuan Min, Zhenwei Wang, Junta Wu, Tengfei
Wang, Yixuan Yuan, Yawei Luo, and Chunchao Guo. World-
mirror: Universal 3d world reconstruction with any-prior
prompting. arXiv preprint arXiv:2510.10726, 2025. 8
[45] Yanzuo Lu, Yuxi Ren, Xin Xia, Shanchuan Lin, Xing Wang,
Xuefeng Xiao, Andy J Ma, Xiaohua Xie, and Jian-Huang
Lai. Adversarial distribution matching for diffusion distilla-
tion towards efficient image and video synthesis. In ICCV,
pages 16818–16829, 2025. 3
[46] Xiaofeng Mao, Shaoheng Lin, Zhen Li, Chuanhao Li, Wen-
shuo Peng, Tong He, Jiangmiao Pang, Mingmin Chi, Yu
Qiao, and Kaipeng Zhang. Yume: An interactive world gen-
eration model. arXiv preprint arXiv:2507.17744, 2025. 2
[47] Minimax.
Hailuo video model, 2024.
https://
hailuoai.video. 2
[48] Takeru Miyato, Bernhard Jaeger, Max Welling, and Andreas
Geiger.
Gta: A geometry-aware attention mechanism for
multi-view transformers. In ICLR, 2024. 2
[49] Jack Parker-Holder, Philip Ball, Jake Bruce, Vibhavari
Dasagi, Kristian Holsheimer, Christos Kaplanis, Alexandre
Moufarek, Guy Scully, Jeremy Shar, Jimmy Shi, Stephen
Spencer, Jessica Yung, Michael Dennis, Sultan Kenjeyev,
Shangbang Long, Vlad Mnih, Harris Chan, Maxime Gazeau,
Bonnie Li, Fabio Pardo, Luyu Wang, Lei Zhang, Fred-
eric Besse, Tim Harley, Anna Mitenkova, Jane Wang, Jeff
Clune, Demis Hassabis, Raia Hadsell, Adrian Bolton, Satin-
der Singh, and Tim Rockt¨aschel.
Genie 2: A large-scale
foundation world model. 2024. 2
[50] William Peebles and Saining Xie. Scalable diffusion models
with transformers. In ICCV, pages 4195–4205, 2023. 2, 3
[51] Joseph Redmon, Santosh Divvala, Ross Girshick, and Ali
Farhadi. You only look once: Unified, real-time object de-
tection. In Proceedings of the IEEE Conference on Computer
Vision and Pattern Recognition (CVPR), 2016. 2
[52] Xuanchi Ren, Tianchang Shen, Jiahui Huang, Huan Ling,
Yifan Lu, Merlin Nimier-David, Thomas M¨uller, Alexan-
der Keller, Sanja Fidler, and Jun Gao. Gen3c: 3d-informed
world-consistent video generation with precise camera con-
trol. In CVPR, pages 6121–6132, 2025. 2, 7
[53] Robin Rombach, Andreas Blattmann, Dominik Lorenz,
Patrick Esser, and Bj¨orn Ommer. High-resolution image syn-
thesis with latent diffusion models. In CVPR, pages 10684–
10695, 2022. 2
[54] Tim Salimans and Jonathan Ho.
Progressive distillation
for fast sampling of diffusion models.
arXiv preprint
arXiv:2202.00512, 2022. 3
10

--- Page 11 ---

[55] Axel Sauer, Frederic Boesel, Tim Dockhorn, Andreas
Blattmann, Patrick Esser, and Robin Rombach. Fast high-
resolution image synthesis with latent adversarial diffusion
distillation. In SIGGRAPH Asia, pages 1–11, 2024. 3
[56] Axel Sauer, Dominik Lorenz, Andreas Blattmann, and Robin
Rombach. Adversarial diffusion distillation. In ECCV, pages
87–103. Springer, 2024. 3
[57] Yang Song, Jascha Sohl-Dickstein, Diederik P Kingma, Ab-
hishek Kumar, Stefano Ermon, and Ben Poole. Score-based
generative modeling through stochastic differential equa-
tions. In ICLR, 2021. 2
[58] Jianlin Su, Murtadha Ahmed, Yu Lu, Shengfeng Pan, Wen
Bo, and Yunfeng Liu. Roformer: Enhanced transformer with
rotary position embedding. Neurocomputing, 568:127063,
2024. 2, 4, 5
[59] Wenqiang Sun, Shuo Chen, Fangfu Liu, Zilong Chen, Yueqi
Duan, Jun Zhang, and Yikai Wang. Dimensionx: Create any
3d and 4d scenes from a single image with controllable video
diffusion. arXiv preprint arXiv:2411.04928, 2024. 2
[60] Wenqiang Sun, Fangyun Wei, Jinjing Zhao, Xi Chen, Zi-
long Chen, Hongyang Zhang, Jun Zhang, and Yan Lu.
From virtual games to real-world play.
arXiv preprint
arXiv:2506.18901, 2025.
[61] Dani Valevski, Yaniv Leviathan, Moab Arar, and Shlomi
Fruchter. Diffusion models are real-time game engines. In
ICLR, 2025. 2
[62] Team Wan, Ang Wang, Baole Ai, Bin Wen, Chaojie Mao,
Chen-Wei Xie, Di Chen, Feiwu Yu, Haiming Zhao, Jianxiao
Yang, et al. Wan: Open and advanced large-scale video gen-
erative models. arXiv preprint arXiv:2503.20314, 2025. 2,
3, 1
[63] Zhengyi Wang, Cheng Lu, Yikai Wang, Fan Bao, Chongxuan
Li, Hang Su, and Jun Zhu. Prolificdreamer: High-fidelity and
diverse text-to-3d generation with variational score distilla-
tion. Advances in neural information processing systems, 36:
8406–8441, 2023. 3
[64] Zhouxia Wang, Ziyang Yuan, Xintao Wang, Yaowei Li,
Tianshui Chen, Menghan Xia, Ping Luo, and Ying Shan.
Motionctrl: A unified and flexible motion controller for
video generation. In ACM SIGGRAPH, pages 1–11, 2024.
2, 7
[65] Thadd¨aus Wiedemer, Yuxuan Li, Paul Vicol, Shixiang Shane
Gu, Nick Matarese, Kevin Swersky, Been Kim, Priyank
Jaini, and Robert Geirhos. Video models are zero-shot learn-
ers and reasoners. arXiv preprint arXiv:2509.20328, 2025.
2
[66] Jay Zhangjie Wu, Yuxuan Zhang, Haithem Turki, Xuanchi
Ren, Jun Gao, Mike Zheng Shou, Sanja Fidler, Zan Goj-
cic, and Huan Ling. Difix3d+: Improving 3d reconstructions
with single-step diffusion models. In CVPR, pages 26024–
26035, 2025. 7, 2
[67] Zeqi Xiao, Yushi Lan, Yifan Zhou, Wenqi Ouyang, Shuai
Yang, Yanhong Zeng, and Xingang Pan. Worldmem: Long-
term consistent world simulation with memory.
arXiv
preprint arXiv:2504.12369, 2025. 2, 3, 4, 5
[68] Shuai Yang, Wei Huang, Ruihang Chu, Yicheng Xiao,
Yuyang Zhao, Xianbang Wang, Muyang Li, Enze Xie, Ying-
cong Chen, Yao Lu, et al. Longlive: Real-time interactive
long video generation.
arXiv preprint arXiv:2509.22622,
2025. 5, 8, 6
[69] Zhuoyi Yang, Jiayan Teng, Wendi Zheng, Ming Ding, Shiyu
Huang, Jiazheng Xu, Yuanming Yang, Wenyi Hong, Xiao-
han Zhang, Guanyu Feng, et al. Cogvideox: Text-to-video
diffusion models with an expert transformer. In ICLR, 2024.
2
[70] Tianwei Yin, Micha¨el Gharbi, Taesung Park, Richard Zhang,
Eli Shechtman, Fredo Durand, and Bill Freeman.
Im-
proved distribution matching distillation for fast image syn-
thesis. Advances in neural information processing systems,
37:47455–47487, 2024. 2, 3, 5
[71] Tianwei Yin, Micha¨el Gharbi, Richard Zhang, Eli Shecht-
man, Fredo Durand, William T Freeman, and Taesung Park.
One-step diffusion with distribution matching distillation. In
CVPR, pages 6613–6623, 2024. 3
[72] Tianwei Yin, Qiang Zhang, Richard Zhang, William T Free-
man, Fredo Durand, Eli Shechtman, and Xun Huang. From
slow bidirectional to fast autoregressive video diffusion mod-
els. In CVPR, pages 22963–22974, 2025. 3, 5
[73] Hong-Xing Yu, Haoyi Duan, Charles Herrmann, William T
Freeman, and Jiajun Wu. Wonderworld: Interactive 3d scene
generation from a single image. In CVPR, pages 5916–5926,
2025. 2
[74] Jiwen Yu, Jianhong Bai, Yiran Qin, Quande Liu, Xintao
Wang, Pengfei Wan, Di Zhang, and Xihui Liu. Context as
memory: Scene-consistent interactive long video generation
with memory retrieval.
arXiv preprint arXiv:2506.03141,
2025. 2, 3, 4, 5, 8
[75] Jiwen Yu, Yiran Qin, Xintao Wang, Pengfei Wan, Di Zhang,
and Xihui Liu. Gamefactory: Creating new games with gen-
erative interactive videos. In ICCV, 2025. 2
[76] Mark YU, Wenbo Hu, Jinbo Xing, and Ying Shan.
Tra-
jectorycrafter: Redirecting camera trajectory for monocular
videos via diffusion models. In ICCV, 2025. 2
[77] Wangbo Yu, Jinbo Xing, Li Yuan, Wenbo Hu, Xiaoyu Li,
Zhipeng Huang, Xiangjun Gao, Tien-Tsin Wong, Ying Shan,
and Yonghong Tian. Viewcrafter: Taming video diffusion
models for high-fidelity novel view synthesis. arXiv preprint
arXiv:2409.02048, 2024. 2, 7
[78] Haiyu Zhang, Xinyuan Chen, Yaohui Wang, Xihui Liu,
Yunhong Wang, and Yu Qiao.
Accvideo:
Accelerating
video diffusion model with synthetic dataset. arXiv preprint
arXiv:2503.19462, 2025. 3
[79] Jintao Zhang, Jia Wei, Pengle Zhang, Jun Zhu, and Jianfei
Chen. Sageattention: Accurate 8-bit attention for plug-and-
play inference acceleration. In ICLR, 2025. 6
[80] Jensen Zhou, Hang Gao, Vikram Voleti, Aaryaman Vasishta,
Chun-Han Yao, Mark Boss, Philip Torr, Christian Rup-
precht, and Varun Jampani. Stable virtual camera: Gener-
ative view synthesis with diffusion models. arXiv preprint
arXiv:2503.14489, 2025. 7
[81] Jinguo Zhu, Weiyun Wang, Zhe Chen, Zhaoyang Liu, Shen-
glong Ye, Lixin Gu, Hao Tian, Yuchen Duan, Weijie Su,
Jie Shao, et al. Internvl3: Exploring advanced training and
test-time recipes for open-source multimodal models. arXiv
preprint arXiv:2504.10479, 2025. 7
11

--- Page 12 ---

WorldPlay: Towards Long-Term Geometric Consistency for Real-Time
Interactive World Modeling
Supplementary Material
A. Training and Inference Details
We adopt the pretrained DiT-based video diffusion mod-
els [28, 62] as the backbone. For the chunk-wise autore-
gressive diffusion transformer, we group 4 latents into a
chunk. For the memory context, we set the temporal mem-
ory length to 3 chunks and the spatial memory length to
1 chunk. For the bidirectional teacher model Vβ, we also
adopt the dual-action representation and construct the mem-
ory context as described in Sec.3.4. The training consists of
three stages.
Stage One: Action Control. In the first stage, we focus on
injecting action control into the pretrained model. We em-
ploy the dual action representation to the pretrained model
and train the bidirectional action model for 30K iterations.
Then, we replace the 3D self-attention with block causal at-
tention and train for an additional 30K iterations as our AR
action model. We find that this enables the AR action model
to converge more easily. In this stage, the model is trained
on 61 frames (4 chunks) using the Adam optimizer with a
learning rate of 1e −5 and a batch size of 64.
Stage Two: Memory. In the second stage, we train the bidi-
rectional action model and the AR action model with con-
text memory as described in Sec.3.3 and Sec.3.4, respec-
tively. The training is performed on longer videos, while
other settings remain the same as in the first stage.
Stage Three: Context Forcing. In the final stage, we use
the bidirectional model as the teacher and the AR model as
the student for distillation. To stabilize the distillation pro-
cess, we employ a progressive training strategy that gradu-
ally increases the maximum length of the generated latents.
For the student model, the learning rate is set to 1e −6,
while for the bidirectional model, which is used to compute
the fake score, the learning rate is set to 2e −7. The mod-
els are trained for 2K iteration with a batch size of 64. All
other hyperparameters follow [21]. For the details of con-
text forcing, see Algorithm 1.
Finally, our AR model can produce multiple chunks in a
streaming fashion with KV cache as shown in Algorithm 2.
When the user provides only camera poses, we first com-
pute the relative translations and rotations between consec-
utive poses, and then apply a thresholding mechanism to
identify and convert them into discrete actions. Conversely,
when only discrete actions are available, we use the prede-
fined relative translations and rotations associated with each
action to convert them into camera poses.
Algorithm 1 Context Forcing Training
Require: Number of denoising timesteps d and chunks n = 4
Require: Dataset D (encoded by 3D VAE)
Require: AR diffusion model Nθ
Require: Bidirectional diffusion model V fake
β
and V real
1: loop
2:
Progressively increase maximum chunk length m
3:
Sample chunk length j ∼Uniform(0, 1, . . . , m)
4:
Sample context x0:j−1 ∼D
5:
for i = j, . . . , j + n −1 do
6:
Initialize xinit
i
∼N(0, I)
7:
Reconstitute context memory Ci ⊆{x0, . . . , xi−1}
8:
Sample s ∼Uniform(1, 2, . . . , d)
9:
Self-rollout xi using Nθ with Ci and s denoising steps
10:
end for
11:
Align context memory Ctea ←Cj:j+n−1 −xj:j+n−1
12:
Sample diffusion timestep k ∼[0, 1]
13:
ˆxj:j+n−1 ←AddNoise(xj:j+n−1, k)
14:
Compute fake score Sfake ←V fake
β
(ˆxj:j+n−1, Ctea, k)
15:
Compute real score Sfake ←V real(ˆxj:j+n−1, Ctea, k)
16:
Update θ via distribution matching loss
17:
Update β via flow matching loss as in [21]
18: end loop
Algorithm 2 Inference with KV Cache
Require: Number of inference chunks nc
Require: Denoise timesteps {k1, . . . , kd}
Require: Number of inference chunks nc
Require: AR diffusion model Nθ (returns KV embeddings via
N KV
θ )
1: Initialize model output Xθ ←[]
2: Initialize KV cache KV ←[]
3: for i = 0, . . . , nc −1 do
4:
Initialize xi ∼N(0, I)
5:
Reconstitute context memory Ci ⊆{x0, . . . , xi−1}
6:
for s = d, . . . , 1 do
7:
if s = d and i > 1 then
8:
Reset KV ←N KV
θ (Ci, 0)
9:
end if
10:
Denoise xi ←Nθ(xi, KV, ks)
11:
end for
12:
Add output Xθ.append(xi)
13: end for
14: return Xθ
B. Dataset
Table 5 provides a comprehensive breakdown of our
dataset. We deliberately curate a diverse and high-quality
1

--- Page 13 ---

Category
Data Source
Annotation (discrete, continuous)
# Clips
Ratios
Real-World Dynamics
Sekai [36]
(✗, ✗)
40K
12.5%
Real-World 3D Scene
DL3DV [40]
(✔, ✔)
60K
18.75%
Synthetic 3D Scene
UE Rendering
(✗, ✔)
50K
15.625%
Simulation Dynamics
Game Video Recordings
(✔, ✗)
170K
53.125%
Table 5. Data organization. The table details the four categories of data, their sources, the availability of action annotations (discrete and
continuous), the number of clips, and their corresponding ratio in the final dataset.
Figure 10. Camera trajectories included in our collected dataset.
collection, encompassing data from the simulation engine
and real world, as well as static and dynamic environments,
to guarantee the strong generalization of our model.
For Real-World Dynamics,
we employ the Sekai
dataset [36]. However, the original videos often suffer from
scene clutter and high dynamics. To address these issues,
we implement a rigorous filtering pipeline. Specifically, we
apply a state-of-the-art object detection model (YOLO [51])
to identify the presence of crowds and vehicles. By setting
an empirical threshold, we filter out clips with high densi-
ties of moving objects, thereby ensuring annotation accu-
racy and stable training.
Regarding the Real-World 3D Scene data (DL3DV [40]),
the original videos lack diversity in camera movement
speed and trajectory complexity. To overcome this, we im-
plement a sophisticated processing workflow: 3D Scene
Reconstruction →Customized Trajectory Rendering →Vi-
sual Quality Filtering →Video Repair Post-processing (us-
ing Difix3D+ [66]). This procedure yields additional 60K
high-quality real video clips featuring balanced movement
speed. During the customized trajectory rendering stage,
we deliberately design diverse revisit trajectories to facili-
tate the learning of long-term geometric consistency. The
discrete actions and continuous camera poses in these ren-
dered data are highly accurate, which helps the model learn
well-structured action patterns.
For Synthetic 3D Scene (UE Rendering) data, we col-
lect hundreds of UE scenes and obtain 50K video clips by
rendering complex, customized trajectories. For Simulation
Dynamics (Game Video Recordings), we establish a dedi-
cated game recording platform and invite players to record
170K video clips from 1st/3rd-person AAA games.
We segment the original long videos into 30 to 40 sec-
onds clips and employ a vision-language model to produce
descriptive text annotations for every clip. Subsequently,
we leverage VIPE [20] to generate high-quality camera
poses for clips without camera annotations. However, given
the long duration and high scene diversity of our dataset, we
observe that pose estimation could be inaccurate, i.e., pose
collapse. Therefore, we filter out videos whose adjacent
frames exhibit erratic camera positions or rotation angles.
Finally, for clips lacking discrete action annotations, we de-
rive them from the continuous camera poses: we project
the rotation and translation components onto the x, y, z axes
and apply a threshold to map these continuous values into
corresponding discrete action states.
Fig. 10 illustrates the camera trajectories. Our dataset
contains complex and diverse trajectories, including a large
number of revisit trajectories, which enables our model to
learn precise action control and long-term geometric con-
sistency.
C. Additional Experimental Results
C.1. More Qualitative Results
Fig. 11 illustrates the results of WorldPlay under various ac-
tions and virtual environments. As shown in the first three
rows, we can interact with complex composite actions, e.g.,
various combinations of movements. Moreover, WorldPlay
can follow intricate trajectories, such as complex rotations
and alternating sequences of rotations and movements as
demonstrated in the middle six rows. This enhanced con-
trol capability is enabled by our dual action representation,
which allows for more precise and reliable action guidance.
2

--- Page 14 ---

Figure 11. More qualitative results.
Furthermore, WorldPlay exhibits strong generalization, en-
abling it to control different types of agents, e.g., human or
animals, to roam within the scenes as shown in the last two
rows. For more intuitive perspectives, please refer to the
supplementary videos.
C.2. Long Video Generation
Fig. 12 presents long video generation results from World-
Play, we maintain long-term consistency, e.g., frame 1 and
frame 252 in the top two examples, and preserve high vi-
sual quality throughout the entire sequence. Moreover, our
3

--- Page 15 ---

Figure 12. Long video generation.
4

--- Page 16 ---

a) Student (AR)
b) Teacher (Bidirectional)
c) Final (Distilled)
Figure 13. Visualization of different models under context forcing.
NFE
PSNR↑
SSIM↑
LPIPS↓
Rdist ↓
Tdist ↓
Student (AR)
100
16.27
0.425
0.495
0.611
0.991
Teacher (Bidirectional)
100
19.31
0.599
0.383
0.209
0.717
Final (Distilled)
4
18.94
0.585
0.371
0.332
0.797
Table 6. Comparison of Models under Context Forcing. The
results are evaluated on the long-term test data.
Student (AR)
denotes the AR model before distillation, Teacher (bidirectional)
refers to the memory-augmented bidirectional video diffusion
model, and Final (distilled) represents the AR model after distilla-
tion. NFE denotes the number of function evaluations.
context memory ensures that the generation time for each
chunk remains constant and does not increase as the video
length grows, enabling real-time interactivity and enhanc-
ing the user’s immersive experience.
C.3. Comparison of Models under Context Forcing
We provide a comprehensive comparison of different mod-
els under context forcing in Table 6 and Fig. 13. The teacher
model exhibits better control capability and visual qual-
ity due to the bidirectional nature, which provides reliable
guidance during distillation. However, this limits its real-
time interactivity.
Through context forcing, we mitigate
error accumulation while maintaining and even surpassing
long-term consistency of the student model, yielding im-
proved overall performance. In addition, context forcing
reduces the student model’s inference steps, enabling real-
time interaction.
C.4. Ablation for Memory Size
Table 7 evaluates the effect of different memory sizes. Us-
ing a larger spatial memory size leads to slightly better
PSNR metric, while a larger temporal memory size better
preserves the pretrained model’s temporal continuity, result-
ing in better overall performance. Moreover, a larger spatial
memory size may significantly increase the teacher model’s
memory size, as the spatial memory of adjacent chunks may
completely differ, while their temporal memory overlaps.
This not only increases the difficulty of training the teacher
model but also poses challenges for distillation.
C.5. Evaluation on VBench
We evaluate our model on VBench [22] across diverse met-
rics. For each baseline, we provide the same image and ac-
Spa.
Tem.
PSNR↑
SSIM↑
LPIPS↓
Rdist ↓
Tdist ↓
3
1
16.41
0.418
0.502
0.634
1.054
1
3
16.27
0.425
0.495
0.611
0.991
Table 7. Ablation for memory size. Spa. and Tem. denote the
number of chunks in spatial memory and temporal memory, re-
spectively.
Dynamic Degree
Color
Temporal Flickering
Spatial Relationship
Subject Consistency
Overall Consistency
Temporal Style
Appearance Style
Scene
Background Consistency
Motion Smoothness
Human Action
Multiple Objects
Object Class
Imaging Quality
Aesthetic Quality
20
40
60
80
VBench metrics and comparison with previous state-of-the-art methods.
Ours
Gen3C
ViewCrafter
GameCraft
Matrix-Game-2.0
Figure 14. VBench evaluation.
0
20
40
60
80
100
Preference Rate (%)
Ours
Ours
Ours
Ours
Ours
Teacher 
 (Bidirectional)
Gen3C
ViewCrafter
Matrix-Game-2.0
GameCraft
48.1%
51.9%
72.9%
27.1%
92.1%
7.9%
78.4%
21.6%
88.5%
11.5%
Preference Study Results
Figure 15. Human evaluation.
tion to generate long-horizon videos. The results presented
in Fig. 14 demonstrate the superior performance of World-
Play. Notably, our method achieves outstanding results in
key aspects such as consistency, motion smoothness, and
scene generalizability.
D. User Study
We conduct a comprehensive user study across multiple di-
mensions, including visual quality, control accuracy, and
long-term consistency. In our setup, users are presented
with two videos, generated from the same initial image and
action inputs, and asked to select their preference based
on the specified criteria. To ensure the robustness of our
5

--- Page 17 ---

Video Continuation
Sky Darkens
Flame Erupts
S
S
S
S
S
Promptable Event
Traveler Walks
Dog Roams
W
W
W
W
W
Figure 16. Visualization of promptable event and video continuation.
Point Cloud
S
S
S
A
W
W
Figure 17. 3D reconstruction results.
evaluation, we select 300 cases from diverse benchmarks
such as VBench [22] and WorldScore [11], and 300 cus-
tomized trajectories. The final results are then evaluated by
a panel of 30 assessors. As shown in Fig. 15, compared to
other baselines, our distilled model achieves superior gener-
ation quality across all aforementioned evaluation metrics,
clearly demonstrating our model’s capability for both real-
time interaction and long-term consistency.
E. Additional Applications
E.1. 3D Reconstruction
Fig. 17 presents additional 3D reconstruction results. With
our reconstituted context memory, we maintain temporal
consistency and ensure long-term geometric consistency,
which is essential for reliable 3D reconstruction. This is
further validated by the consistency and compactness in
the reconstructed point clouds. By generating diverse 3D
scenes, this provides the potential to augment the scarce 3D
datasets.
E.2. Promptable Event
Due to the autoregressive nature of WorldPlay, we can mod-
ify the text prompt at any time to control the subsequent
generated content. Specifically, inspired by LongLive [68],
we employ a KV-recache technique to refresh the cached
key–value states whenever the text prompt is modified. This
effectively erases residual information from the previous
prompt while preserving the motion and visual cues neces-
sary to maintain temporal continuity. As shown in the upper
part of Fig. 16, we can change the weather and trigger a fire
eruption, or introduce new objects and characters. Through
promptable event, we can generate various complex and un-
common scenarios, which can benefit agent learning by en-
abling agents to handle these unexpected situations.
E.3. Video Continuation
As shown at the bottom of Fig. 16, WorldPlay can gener-
ate follow-up content that remains highly consistent with
a given initial video clip in terms of motion, appearance,
and lighting. This enables stable video continuation, effec-
tively extending the original video while preserving spatial-
temporal consistency and content coherence, which opens
up new possibilities in creative video generation and virtual
environment construction.
6

--- Page 18 ---

F. Limitations
While WorldPlay demonstrates strong performance, ex-
tending the framework to generate videos with longer dura-
tions, multi-agent interactions, and more complex physical
dynamics still requires further investigation. Moreover, Ex-
panding the action types to a broader set is another promis-
ing direction. These challenges remain open for future re-
search.
7

```
