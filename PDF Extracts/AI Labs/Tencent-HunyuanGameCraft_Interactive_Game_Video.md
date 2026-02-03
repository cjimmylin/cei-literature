---
title: "HunyuanGameCraft Interactive Game Video"
source_pdf: "/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/AI Labs/Tencent/HunyuanVideo/HunyuanGameCraft_Interactive_Game_Video.pdf"
company: "Tencent"
pages: 12
extracted_at: "2026-02-02T16:29:05.269574"
type: "ai_lab_paper"
---

# HunyuanGameCraft Interactive Game Video

**Company/Lab:** Tencent
**Model:** HunyuanVideo
**Source PDF:** /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/AI Labs/Tencent/HunyuanVideo/HunyuanGameCraft_Interactive_Game_Video.pdf
**Total Pages:** 12

---

## Content

```
--- Page 1 ---

arXiv:2506.17201v1  [cs.CV]  20 Jun 2025
Hunyuan-GameCraft: High-dynamic Interactive Game Video Generation
with Hybrid History Condition
Jiaqi Li1,2*†
Junshu Tang1*
Zhiyong Xu1
Longhuang Wu1
Yuan Zhou1
Shuai Shao1
Tianbao Yu1
Zhiguo Cao2
Qinglin Lu1‡
1 Tencent Hunyuan
2 Huazhong University of Science and Technology
https://hunyuan-gamecraft.github.io/
Action 2
Action 3
Action 4
Action 5
Action 1
1
2
3
4
5
6
“A sunlit courtyard features white adobe buildings with arched doorways and windows, 
surrounded by lush greenery and palm trees, creating a serene Mediterranean ambiance.”
Figure 1. Hunyuan-GameCraft can create high-dynamic interactive game video content from a single image and corresponding prompt.
We simulate a series of action signals. The left and right frames depict key moments from game video sequences generated in response to
different inputs. Hunyuan-GameCraft can accurately produce content aligned with each interaction, supports long-term video generation
with temporal and 3D consistency, and effectively preserves historical scene information throughout the sequence. In this case, W, A, S, D
represent transition movement and ↑, ←, ↓, →denote changes in view angles.
Abstract
Recent advances in diffusion-based and controllable
video generation have enabled high-quality and tempo-
rally coherent video synthesis, laying the groundwork for
immersive interactive gaming experiences. However, cur-
rent methods face limitations in dynamics, generality, long-
term consistency, and efficiency, which limit the ability to
create various gameplay videos.
To address these gaps,
we introduce Hunyuan-GameCraft, a novel framework for
high-dynamic interactive video generation in game envi-
ronments. To achieve fine-grained action control, we unify
standard keyboard and mouse inputs into a shared camera
representation space, facilitating smooth interpolation be-
tween various camera and movement operations. Then we
propose a hybrid history-conditioned training strategy that
*Equal Contribution.
†Work is done during the internship at Tencent Hunyuan.
‡Corresponding author.
extends video sequences autoregressively while preserving
game scene information. Additionally, to enhance inference
efficiency and playability, we achieve model distillation to
reduce computational overhead while maintaining consis-
tency across long temporal sequences, making it suitable
for real-time deployment in complex interactive environ-
ments. The model is trained on a large-scale dataset com-
prising over one million gameplay recordings across over
100 AAA games, ensuring broad coverage and diversity,
then fine-tuned on a carefully annotated synthetic dataset
to enhance precision and control. The curated game scene
data significantly improves the visual fidelity, realism and
action controllability. Extensive experiments demonstrate
that Hunyuan-GameCraft significantly outperforms existing
models, advancing the realism and playability of interactive
game video generation.

--- Page 2 ---

First Frame
Action 1
Action 2
Action 3
Action 4
Action 5
Figure 2. Additional results by Hunyuan-GameCraft on multi-actions control. In our case, blue-lit keys indicate key presses. W, A, S, D
represent transition movement and ↑, ←, ↓, →denote changes in view angles.

--- Page 3 ---

1. Introduction
The rapid progress in generative modeling has transformed
numerous fields, including entertainment and education,
and beyond, fueling growing interest in high-dynamic, im-
mersive, generative gaming experiences.
Recent break-
throughs in diffusion-based video generation [1, 2, 6, 19,
31] have significantly advanced dynamic content creation,
enabling high-quality, temporally coherent video synthesis.
Moreover, advances in controllable video generation have
introduced novel creative forms of dynamic, user-driven
video production, expanding the boundaries of interactive
digital experiences.
Recent advances in visual generation have explored
spatial intelligence, the analysis and creation of coher-
ent spatial scenes.
These models focus on interactiv-
ity and exploration, enabling dynamic 3D/4D environ-
ments with spatiotemporal coherence. For example, World-
Labs [32] demonstrates the potential for reconstructing
high-fidelity 3D environments from static imagery, while
Genie 2 [22] introduces latent action modeling to en-
able physics-consistent interactions over time.
Despite
these advances, current approaches still struggle with sig-
nificant limitations in critical areas such as real-time dy-
namic scene element fidelity, long-sequence consistency,
and computational efficiency, limiting their applicability in
high-dynamic, playable interactive scenarios. Notably, in
game interaction modeling, real-time interactive generation
and high dynamicity constitute fundamental components of
player experience.
To address these challenges, we introduce Hunyuan-
GameCraft, a novel framework designed for high-dynamic,
action-controllable video synthesis in game environments.
Built upon a text-to-video foundation model, Hunyuan-
Video [18], our method enables the generation of tempo-
rally coherent and visually rich gameplay footage condi-
tioned on discrete user actions. We unify a broad set of
standard keyboard and mouse inputs (e.g., W, A, S, D, ar-
row keys, Space) into a shared camera representation space,
which unified embedding supports smooth interpolation be-
tween various camera and movement operations, ensuring
physical plausibility while enabling cinematic flexibility in
user-driven interactions, for example, speeding up.
To maintain long-term consistency in interactive game
video generation, prior works [6, 15, 20] have primarily fo-
cused on training-free extensions, streaming denoising or
last-frame conditioning. However, these approaches often
suffer from quality degradation and temporal inconsistency
with causal VAEs [33]. We propose a novel hybrid history-
conditioned training strategy that autoregressively extends
sequences while preserving scene information, using his-
torical context integration and a mask indicator to address
error accumulation in autoregressive generation. Moreover,
to improve inference efficiency and playability, we imple-
ment the model distillation acceleration strategy [28], which
reduces computational overhead while maintaining consis-
tency across long temporal sequences, making our frame-
work suitable for real-time deployment in complex interac-
tive environments.
We evaluate our Hunyuan-GameCraft on both curated
game scenes and general styles, obtaining a significant lead
over current models. In summary, our contributions are:
• We propose Hunyuan-GameCraft, a novel interactive
game video synthesis framework for dynamic content
creation in game scenes, enabling users to produce con-
tent through customized action input.
• We unify the discrete keyboard/mouse action signals
into a shared continuous action space, supporting more
complex and fine-grained interactive inputs, such as
speed, angle, etc.
• We introduce a novel hybrid history-condition training
strategy that maintains long-term spatial and temporal
coherency across various action signals.
• We implement model distillation to speed up the infer-
ence speed which improves the interaction experience.
2. Related Work
2.1. Interactive Game Scene World Model
Recent research has gradually focused on incorporating
video generation models to enhance dynamic prediction
and interaction capabilities in game scenes. We conduct
a survey on recent works, as shown in Tab. 1.
World-
Dreamer [30] proposes constructing a general world model
by predicting masked tokens, which supports multi-modal
interaction and is applicable to natural scenes and driving
environments.
GameGen-X [5], a diffusion Transformer
model for open-world games, integrates multi-modal con-
trol signals to enable interactive video generation.
The
Genie series [22] generates 3D worlds from single-image
prompts, while the Matrix model leverages game data with
a streaming generation format to infinitely produce content
through user actions.
2.2. Camera-Controlled Video Generation
Motionctrl [31] uses a unified and flexible motion controller
designed for video generation, which independently con-
trols the movement of video cameras and objects to achieve
precise control over the motion perspectives in generated
videos. CameraCtrl [13] employs Pl¨ucker embedding as the
primary representation for camera parameters, training only
the camera encoder and linear layers to achieve camera con-
trol. Furthermore, the recent approach CameraCtrl II [14]
constructs a high-dynamics dataset with camera parameter
annotations for training, and designs a lightweight camera
injection module and training scheme to preserve the dy-
namics of pretrained models.

--- Page 4 ---

GameNGen [26]
GameGenX [5]
Oasis [8]
Matrix [10]
Genie 2 [22]
GameFactory [34]
Matrix-Game [36]
Hunyuan-GameCraft
Game Sources
DOOM
AAA Games
Minecraft
AAA Games
Unknown
Minecraft
Minecraft
AAA Games
Resolution
240p
720p
640 × 360
720p
720p
640 × 360
720p
720p
Action Space
Key
Instruction
Key + Mouse
4 Keys
Key+Mouse
7 Keys+Mouse
7 Keys+Mouse
Continous
Scene Generalizable
✗
✗
✗
✔
✔
✔
✔
✔
Scene Dynamic
✔
✔
✗
✔
✗
✔
✗
✔
Scene Memory
✗
✗
✗
✗
✗
✗
✔
✔
Table 1. Comparison with recent interactive game models. Hunyuan-GameCraft serves as a model capable of generating infinitely long
game videos conditioned on continuous action signals, while maintaining strong generalization, high temporal dynamics, and effective
preservation of historical scene information.
2.3. Long Video Extension
Generating long videos poses challenges in maintaining
temporal consistency and high visual quality over extended
durations. Early methods used GAN to explore long video
generation [23].
With the popularity of diffusion, some
methods began to try to solve the problem using diffusion
model. StreamingT2V [15] introduces short-term and long-
term memory blocks with randomized blending to ensure
consistency and scalability in text-to-video generation. In
addition, some methods also explore different paradigms,
such as next frame prediction [11, 12], combining next-
token and full-sequence diffusion (DiffusionForcing) [6]
and test-time training [7]. Compared with previous meth-
ods, we propose a novel hybrid history-conditioned training
strategy that extends video sequences in an autoregressive
way while effectively preserving game scene information,
under a diffusion paradigm.
3. Dataset Construction
3.1. Game Scene Data Curation
We curate over 100 AAA titles, such as Assassin’s Creed,
Red Dead Redemption, and Cyberpunk 2077, to create a
diverse dataset with high-resolution graphics and complex
interactions. As shown in Fig 3, our end-to-end data pro-
cessing framework comprises four stages that addresses an-
notated gameplay data scarcity while establishing new stan-
dards for camera-controlled video generation.
Scene and Action-aware Data Partition. We introduce
a two-tier video partitioning approach (scene-level and
action-level).
Using PySceneDetect [4], we segment 2-
3 hour gameplay recordings into 6-second coherent clips
(1M+ clips at 1080p). RAFT [24] computes optical flow
gradients to detect action boundaries (e.g., rapid aiming),
enabling precise alignment for video generation training.
Data Filtering. To enhance synthesis quality, we employ
quality assessment [17] to remove low-fidelity clips, ap-
ply OpenCV [3]-based luminance filtering to eliminate dark
scenes, and utilize VLM [29]-based gradient detection for
comprehensive data filtering from multiple perspectives.
Action
Partition
Raw clip
Clip1
Clip2
Clip3
Traj 1
Scene
Partition
Raw video data
Optical Flow
Quality Filter
X
X
X
X
Supersaturation
Too Dark
UI
Gradient Transition
Video Clips
Interaction
Annotation
Traj 2
Structured
Captioning
Long
Caption
Short
Caption
Figure 3. Dataset Construction Pipeline. It consists of four pre-
processing steps: Scene and Action-aware Data Partition, Data
Filtering, Interaction Annotation and structured captioning.
Interaction Annotation.
We reconstruct 6-DoF camera
trajectories using Monst3R [35] to model viewpoint dynam-
ics (translational/rotational motion). Each clip is annotated
with frame-by-frame position/orientation data, which is es-
sential for video generation training.
Structured Captioning. For video captioning, we imple-
ment a hierarchical strategy using game-specific VLMs [29]
to generate: 1) concise 30-character summaries and 2) de-
tailed 100+ character descriptions. These captions are ran-
domly sampled during training.
3.2. Synthetic Data Construction
We rendered about 3,000 high-quality motion sequences
from curated 3D assets, systematically sampling multi-
ple starting positions to generate diverse camera trajecto-
ries (translations, rotations, and composites) re-rendered at
varying speeds. Our multi-phase training strategy demon-
strates that introducing high-precision rendered sequences
significantly improves motion prediction accuracy and tem-
poral coherence during viewpoint transitions, while es-
tablishing essential geometric priors for complex camera
movements that complement real-world samples.

--- Page 5 ---

First Frame
MM-DiT Blocks
Action 1
Mask
History Frames
Action 2
Continuous Action Space
MM-DiT Blocks
History Frames
Action 3
MM-DiT Blocks
…
…
…
Caption
Image/Video
Noisy Input
Clip & MLLM
3DVAE
Action 
Encoder
MLP
Patchify
Patchify
Mask
Timestep
Sinusoidal 
Encoding
MLP
Output
UnPatchify
Action
W
A
S
D
W
A
S
D
W
A
S
D
Double Stream DiT Blocks
Single Stream DiT Blocks
Concat
+ Add
+
+
1
0
0
0
0
1
0
0
0
0
1
0
0
0
0
1
1
1
1
Figure 4. Overall architecture of Hunyuan-GameCraft. Given a reference image and the corresponding prompt, the keyboard or mouse
signal, we transform these options to the continuous camera space. Then we design a light-weight action encoder to encode the input
camera trajectory. The action and image features are added after patchify. For long video extension, we design a variable mask indicator,
where 1 and 0 indicate history frames and predicted frames, respectively.
3.3. Distribution Balancing Strategy
Leveraging a hybrid training framework with combined
datasets, we addressed inherent forward-motion bias in
camera trajectories via a two-pronged strategy: 1) stratified
sampling of start-end vectors to balance directional repre-
sentation in 3D space and 2) temporal inversion augmenta-
tion to double backward motion coverage. Combined with
late-stage fine-tuning using uniformly distributed rendered
data, these techniques enhanced control signal generaliza-
tion, training stability, and cross-directional performance
consistency.
4. Method
In this paper, we propose Hunyuan-GameCraft, a high-
dynamic interactive game video generation model based
on a previously open-sourced MM-DiT [9] based text-to-
video model, HunyuanVideo [18]. The overall framework is
shown in Fig 4. To achieve fine-grained controllable game
video synthesis with temporal coherence, we first unify di-
verse common keyboard/mouse options in games (W, A, S,
D, ↑, ←, ↓, →, Space, etc.) into a shared camera represen-
tation space (Sec. 4.1) and design a light-weight action en-
coder to encode the camera trajectory(Sec. 4.1). Then, we
propose a hybrid history-conditioned video extension ap-
proach that autoregressively denoise new noisy latent con-
ditioned on historical denoised chunks (Sec. 4.2). Finally, to
accelerate the inference speed and improve the interaction
experience, we implement the model distillation, based on
Phased Consistency Model [28]. This distillation achieves
a 10–20× acceleration in inference speed, reducing latency
to less than 5s per action (Sec. 4.3).
4.1. Continuous Action Space and Injection
To achieve fine-grained control over the generated content
for enhanced interactive effects, we define a subset action
space A within the camera parameter C ⊆Rn dedicated to
continuous and intuitive motion control injection:
A :=
(
a =

dtrans, drot, α, β
 
dtrans ∈S2,
drot ∈S2,
α ∈[0, vmax],
β ∈[0, ωmax]
)
.
(1)
dtrans and drot are unit vectors defining the translation and
rotation direction on the 2-sphere space S2, respectively.
Scalars α and β are used for controlling translation and ro-
tation speed, bounded by maximum velocity vmax and ωmax.
Specifically, they are the differential modulus of relative ve-
locity and angle during frame-by-frame motion.
Building upon prior knowledge of gaming scenarios and
general camera control conventions, we eliminate the de-
gree of freedom in the roll dimension while incorporating
velocity control. This design enables fine-grained trajec-
tory manipulation that aligns with user input habits. Fur-
thermore, this representation can be seamlessly converted
into standard camera trajectory parameters and Pl¨ucker em-
beddings.
Similar with previous camera-controlled video
generation arts, we design a light-weight camera informa-
tion encoding network that aligns Pl¨ucker embeddings with
video latents. Unlike previous approaches that employ cas-
caded residual blocks or transformer blocks to construct
Pl¨ucker embedding encoders, our encoding network con-
sists solely of a limited number of convolutional layers
for spatial downsampling and pooling layers for temporal
downsampling. A learnable scaling coefficient is incorpo-
rated to automatically optimize the relative weighting dur-
ing token-wise addition, ensuring stable and adaptive fea-

--- Page 6 ---

Noisy Chunk
Image
Noisy Chunk
(iii) Hybrid History Condition
1
Binary Mask
1
… 1
1
(a)
(b)
VAE
Decoder
…
Current Video Clip
N
Single
Frame
(c)
Last Chunk
×2
×4
OR
History  Chunks
History  Chunks
1
1
… 1
N/2
1
1
… 1
N/4
1
0 …
N
Current
Denoised
Chunk
History
Denoised
Chunk
Denoised Chunk
Autoregressive Long Video Extention
(i) Training-Free
Image
Noisy Chunk
Last Image
(ii) Streaming
Noisy
Chunk
Noisy
Chunk
…
New Noisy
Chunk
Clean 
Chunk
Noisy
Chunk
Noisy
Chunk
×
×
Decode
Noisy
Chunk
…
One-step Denoise 
Denoise
Figure 5. Comparison of different autoregressive long video ex-
tension schemes. (i) Training-free inference. (ii) Streaming gener-
ation. (iii) Hybrid history condition proposed in this paper.
ture fusion.
Then we adopted the token addition strategy to inject
camera pose control into the MM-DiT backbone.
Dual
lightweight learnable tokenizers are used to achieve effi-
cient feature fusion between video and action tokens, en-
abling effective interactive control.
Additional ablation
studies and comparative analyses are detailed in Sec. 5.3.
Leveraging the robust multimodal fusion and interaction
capabilities of MM-DiT backbone, our method achieves
state-of-the-art interactive performance despite significant
encoder parameter reduction, while maintaining negligible
additional computational overhead.
4.2. Hybrid history conditioned Long Video Exten-
sion
Consistently generating long or potentially infinite-length
videos remains a fundamental challenge in interactive video
generation. As shown in Fig 5, current video extrapolation
approaches can be categorized into three main paradigms:
(1) training-free inference from single images, (2) rolling
streaming generation with non-uniform noise windows, and
(3) chunk-wise extension using historical segments.
As
shown in Fig 6(a), training-free methods lack insufficient
historical context during extrapolation, leading to inconsis-
tent generation quality and frequent scene collapse in itera-
tive generation. The streaming approach shows significant
architectural incompatibility with our image-to-video foun-
dation model, where the causal VAE’s uneven encoding of
initial versus subsequent frames fundamentally limits ef-
ficiency and scalability. To address these limitations, we
investigate hybrid-conditioned autoregressive video exten-
sion, where multiple guidance conditions are mixed during
training to achieve high consistency, fidelity, and compati-
bility.
(a) Training-Free
(b) History Clip Condition
×
Quality
Collapse
×
Control
Degradation
…
…
✓
Accurate
Control
W
A
W
A
W
S
A
✓
History
Preservation
(c) Hybrid History Condition
Figure 6. Analysis on different video extension schemes. Baseline
(a) is a naive solution using training-free inference from single
images, and it will lead to obvious quality collapse. Using history
clip condition (b) will result in control degradation. With our pro-
posed hybrid history condition (c), the model can achieve accurate
action control and history preservation (see red box). W, A, S de-
note moving forward, left and backward.
As illustrated in Fig. 5, we define each autoregressive
step as a chunk latent denoising process guided by head la-
tent and interactive signals. The chunk latent, serving as
a global representation by causal VAE, is subsequently de-
coded into a temporally consistent video segment that pre-
cisely corresponds to the input action. Head condition can
be different forms, including (i) a single image frame la-
tent, (ii) the final latent from the previous clip, or (iii) a
longer latent clip segment. Hunyuan-GameCraft achieves
high-fidelity denoising of chunk latents through concatena-
tion at both condition and noise levels. An additional binary
mask assigns value 1 to head latent regions and 0 to chunk
segments, enabling precise control over the denoising part.
Within the noise schedule, the preceding head condition re-
mains noise-free as clean latent, which guides subsequent
noisy chunk latents through flow matching to progressively
denoise and generate new clean video clips for the next de-
noising iteration.
We conduct extensive experiments on the three afore-
mentioned head conditions, as detailed in Fig 6. The results
demonstrate that autoregressive video extension shows im-
proved consistency and generation quality when the head
condition contains more information, while interactive per-
formance decreases accordingly. This trade-off occurs be-
cause the training data comes from segmented long videos,
where subsequent clips typically maintain motion continu-
ity with preceding ones. As a result, stronger historical pri-
ors naturally couple the predicted next clip with the given
history, which limits responsiveness to changed action in-
puts. However, richer reference information simultaneously
enhances temporal coherence and generation fidelity.
To address this trade-off, in addition to constructing
training samples and applying stratified sampling, hybrid-
conditioned training is proposed to mix all three exten-

--- Page 7 ---

(a) Multi-actions Control Accuracy
(b) Long-term Consistency
Matrix-Game
Ours
Image
CameraCtrl
Ours
MotionCtrl
Matrix-Game
W
A
S
D
W
A
S
D
WanX-Cam
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
Matrix-Game
Ours
W
A
S
D
W
A
S
D
"A pixelated, blocky landscape featuring a wooden house 
surrounded by lush greenery and a serene pond, set against a 
backdrop of towering, jagged mountains under a twilight sky."
"A charming Parisian street scene with its vibrant red 
awning and outdoor seating area, surrounded by quaint shops 
and lush greenery under a bright blue sky."
A picturesque rural 
landscape featuring a 
traditional windmill 
surrounded by golden 
fields under a partly 
cloudy sky.
A picturesque village 
scene featuring quaint 
houses, a windmill, lush 
greenery, and a serene 
mountain backdrop 
under a bright blue sky.
A serene landscape 
features a river winding 
through lush green 
fields under a bright 
blue sky dotted with 
fluffy clouds.
A vibrant, sunlit street 
lined with colorful 
buildings and a tram 
track stretches into the 
distance, framed by 
modern skyscrapers in 
the background.
Prompt
(c) Single-action Control Accuracy
Figure 7. Qualitative comparison on the test benchmark. We compare with Matrix-Game on multi-actions control accuracy and long-term
consistency. And we compare with other camera-controlled video generation arts CameraCtrl, MotionCtrl and WanX-Cam on single-action
control accuracy. In our case, blue-lit keys indicate key presses. W, A, S, D represent transition movement and ↑, ←, ↓, →denote changes
in view angles.
sion modes during training to jointly optimize both inter-
active capability and generation consistency. This hybrid
approach achieves state-of-the-art performance by reason-
ably balancing these competing objectives.
The hybrid-
conditioned paradigm also provides practical deployment
benefits. It successfully integrates two separate tasks (ini-
tial frame generation and video extension) into a unified
model.
This integration enables seamless transitions be-
tween generation modes without requiring architectural
modifications, making the solution particularly valuable for
real-world applications that demand both flexible control
and coherent long-term video generation.
4.3. Accelerated Generative Interaction
To enhance the gameplay experience and enable acceler-
ated interaction with the generated game videos, we fur-
ther extend our approach by integrating acceleration tech-
niques.
A promising direction involves combining our
core framework with Consistency Models [21], a state-
of-the-art method for accelerating diffusion-based genera-
tion. In particular, we adopt the Phased Consistency Model
(PCM) [28], which distills the original diffusion process and
classifier-free guidance into a compact eight-step consis-
tency model. To further reduce computational overhead and
improve inference efficiency, we introduce Classifier-Free
Guidance Distillation. This approach defines a distillation
objective that trains the student model to directly produce
guided outputs without relying on external guidance mech-
anisms, the object function is designed as:
Lcfg = Ew∼pw,t∼U[0,1][|| ˆuθ(zt, t, w, Ts) −us
θ(zt, t, w, Ts)||2
2],
ˆuθ(zt, t, w, Ts) = (1 + w)u(zt, t, Ts) −wuθ(zt, t, )
(2)

--- Page 8 ---

where Ts denotes the prompt. Through this integration, we
achieve up to a 20× speedup in inference, reaching real-
time rendering rates of 6.6 frames per second (FPS), thereby
significantly enhancing the interactivity and playability of
our system.
5. Experiment
5.1. Experimental Setup
Implementation Details.
Hunyuan-GameCraft builds
upon text-to-video foundation model HunyuanVideo [18],
implementing a latent mask mechanism and hybrid history
conditioning to achieve image-to-video generation and long
video extension. The experiments employ full-parameter
training on 192 NVIDIA H20 GPUs, conducted in two
phases with a batch size of 48. The first phase trains the
model for 30k iterations at a learning rate of 3×10−5 using
all collected game data and synthetic data at their original
proportions. The second phase introduces data augmenta-
tion techniques, as described in Sec. 3, to balance action dis-
tributions, while reducing the learning rate to 1 × 10−5 for
an additional 20,000 iterations to enhance generation qual-
ity and interactive performance. The hybrid history condi-
tion maintains specific ratios: 0.7 for single historical clip,
0.05 for multiple historical clips, and 0.25 for single frame.
The system operates at 25 fps, with each video chunk com-
prising 33-frame clips at 720p resolution.
Evaluation Datasets. We curate a test set of 150 diverse
images and 12 different action signals, sourced from online
repositories, spanning gaming scenarios, stylized artwork,
and AI-generated content. This composition facilitates both
quantitative and qualitative evaluation of interactive control
accuracy and generalization. To demonstrate cross-scenario
adaptability, we present exemplar results from diverse con-
texts.
Evaluation Metrics. We employ several metrics for com-
prehensive evaluation to ensure fair comparison. We utilize
Fr´echet Video Distance(FVD) [25] to evaluate the video re-
alism.
Relative pose error (RPE trans and RPE rot) are
adopted to evaluate interactive control performance, af-
ter applying a Sim3 Umeyama alignment on the recon-
structed trajectory of prediction to the ground truth. Fol-
lowing Matrix-Game, we employ Image Quality and Aes-
thetic scores for visual quality assessment, while utilizing
Temporal Consistency to evaluate the visual and cinemato-
graphic continuity of generated sequences. For dynamic
performance evaluation, we adapt the Dynamic Degree met-
ric from VBench [16], modifying its original binary clas-
sification approach to directly report absolute optical flow
values as Dynamic Average, enabling a more nuanced, con-
tinuous assessment of motion characteristics. Additionally,
we incorporate user preference scores obtained from user
studies.
Baselines. We compare our method with four represen-
tative baselines, including a current state-of-the-art open-
sourced interactive game model, Matrix-Game, and three
camera-controlled generation works: CameraCtrl [13], Mo-
tionCtrl [31] and WanX-Cam [27]. The CameraCtrl and
MotionCtrl employ the image-to-video SVD implementa-
tion, while WanX-Cam corresponds to the VideoX-Fun im-
plementation.
5.2. Comparisons with other methods
Quantitative Comparison.
We conduct comprehen-
sive comparisons with Matrix-Game, the current lead-
ing open-source game interaction model, under identi-
cal gaming scenarios. Despite employing the same base
model [18], Hunyuan-GameCraft demonstrates significant
improvements across the majority of key metrics, includ-
ing generation quality, dynamic capability, control accu-
racy, and temporal consistency as shown in Tab. 2. No-
tably, Hunyuan-GameCraft achieves the best results in dy-
namic performance compared to Matrix-Game, while si-
multaneously reducing interaction errors by 55% in cross-
domain tests. These advancements are attributable to our
optimized training strategy and conditional injection mech-
anism, which collectively enable robust interactive genera-
tion across both gaming scenarios and diverse artistic styles.
We also evaluate generation quality and control accuracy
on the same test set, with quantitative results presented in
Tab. 2. Hunyuan-GameCraft demonstrates superior perfor-
mance compared to other baselines. The results suggest that
our action-space formulation captures fundamental princi-
ples of camera motion that transcend game scene character-
istics. Furthermore, we report the inference speed of each
baseline. Our method can achieve nearly real-time infer-
ence while slightly damaging the dynamic and visual qual-
ity, which is more suitable for game scene interaction.
Qualitative Comparison. As shown in Fig. 7, we qual-
itatively demonstrate superior capabilities of Hunyuan-
GameCraft from multiple perspectives. The part(a) com-
pares our method with Matrix-Game in sequential single-
action scenarios, using the Minecraft environment origi-
nally employed for training of Matrix-Game. The results
demonstrate significantly superior interaction capabilities
of Hunyuan-GameCraft. Furthermore, continuous left-right
rotations effectively showcase the enhanced historical infor-
mation retention enabled by hybrid history condition train-
ing approach. The comparison of both game interaction
models with sequential coupled action is shown in (b). Our
method can accurately map input-coupled interaction sig-
nals while maintaining both quality consistency and spatial
coherence during long video extension, achieving an im-
mersive exploration experience. Part(c) focuses on evalu-
ating image-to-video generation performance under single
action across all baselines. Hunyuan-GameCraft demon-

--- Page 9 ---

Model
Visual Quality
Temporal
RPE
Infer Speed↑
(FPS)
FVD↓
Image Quality↑
Dynamic Average↑
Aesthetic↑
Temporal Consistency↑
Trans↓
Rot↓
CameraCtrl
1580.9
0.66
7.2
0.64
0.92
0.13
0.25
1.75
MotionCtrl
1902.0
0.68
7.8
0.48
0.94
0.17
0.32
0.67
WanX-Cam
1677.6
0.70
17.8
0.67
0.92
0.16
0.36
0.13
Matrix-Game
2260.7
0.72
31.7
0.65
0.94
0.18
0.35
0.06
Ours
1554.2
0.69
67.2
0.67
0.95
0.08
0.20
0.25
Ours + PCM
1883.3
0.67
43.8
0.65
0.93
0.08
0.20
6.6
Table 2. Quantitative comparison with recent related works. ↑indicates higher is better, while ↓indicates that lower is better. The best
result is shown in bold.
Method
Video
Quality↑
Temporal
Consistency↑Motion
Smooth↑
Action
Accuracy↑Dynamic↑
CameraCtrl
2.20
2.40
2.16
2.87
2.57
MotionCtrl
3.23
3.20
3.21
3.09
3.22
WanX-Cam
2.42
2.53
2.44
2.81
2.46
Matrix-Game
2.72
2.43
2.75
1.63
2.21
Ours
4.42
4.44
4.53
4.61
4.54
Table 3. Average ranking score of user study. For each object,
users are asked to give a rank score where 5 for the best, and 1 for
the worst. User prefer ours the best in both aspects.
FVD↓DA↑Aesthetic↑RPE trans↓RPE rot↓
(a) Only Synthetic Data
2550.7 34.6
0.56
0.07
0.17
(b) Only Live Data
1937.7 77.2
0.60
0.16
0.27
(c) Token Concat.
2236.4 59.7
0.54
0.13
0.29
(d) Channel-wise Concat.
1725.5 63.2
0.49
0.11
0.25
(e) Image Condition
1655.3 47.6
0.58
0.07
0.22
(f) Clip Condition
1743.5 55.3
0.57
0.16
0.30
(g) Ours (Render:Live=1:5) 1554.2 67.2
0.67
0.08
0.20
Table 4. Ablation study on different data distribution, control in-
jection, and hybrid history conditioning. DA denotes Dynamic
Average score.
strates significant advantages in dynamic capability, includ-
ing windmill rotation consistency, as well as overall visual
quality.
User Study.
Given the current lack of comprehensive
benchmarks for interactive video generation models in both
gaming and general scenarios, we conducted a user study
involving 30 evaluators to enhance the reliability of our as-
sessment. As shown in Tab. 3, our method achieved the
highest scores by a margin across multiple dimensions in
the anonymous user rankings.
5.3. Ablation Study
In this section, comprehensive experiments are conducted
to validate the effectiveness of our contributions, including
the data distribution, control injection, and hybrid history
conditioning.
Data Distribution. To understand the distinct contributions
of game data and synthetic data, we began with an ablation
study evaluating their impact on the model’s capabilities.
Notably, the synthetic data does not highlight dynamic ob-
jects due to the computational expense and complexity of
generating dynamical scenes. Tab. 4(a)(b) demonstrate that
training exclusively on synthetic data significantly improves
interaction accuracy but substantially degrades dynamic
generation capabilities, while gameplay data exhibits the
opposite characteristics. Our training distribution achieves
balanced results.
Action Control Injection. Here we present ablation details
for our camera injection experiments. Since the Pl¨ucker
embeddings are already temporally and spatially aligned
with the video latent representations, we implement three
straightforward camera control schemes: (i) Token Addi-
tion, (ii) Token Concatenation, and (iii) Channel-wise Con-
catenation, as shown in the Tab. 4(c)(d)(g). Simply adding
control signals at the initial stage achieves state-of-the-art
control performance. Considering computational efficiency,
we ultimately adopt Token Addition in our framework.
Hybrid History Conditioning. Hunyuan-GameCraft im-
plements hybrid history conditioning for video generation
and extension.
Fig. 6 visually demonstrates visual re-
sults under different conditioning schemes, while we pro-
vide quantitative ablation analysis here.
As shown in
Tab. 4(e)(f)(g), Hunyuan-GameCraft achieves satisfactory
control accuracy when trained with single frame condition-
ing, yet suffers from quality degradation over multiple ac-
tion sequences due to limited historical context, leading
to quality collapse as shown in Fig. 6. When employing
historical clip conditioning, the model exhibits degraded
interaction accuracy when processing control signals that
significantly deviate from historical motions. Our hybrid
history conditioning effectively balances this trade-off, en-
abling Hunyuan-GameCraft to simultaneously achieve su-
perior interaction performance, long-term consistency and
visual quality.
6. Generalization on Real Worlds
Although our model is tailored for game scenes, the integra-
tion of a pre-trained video foundation model significantly

--- Page 10 ---

W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
W
A
S
D
Figure 8. Long Video Extension Results. Hunyuan-GameCraft can generate minute-level video clips in length while maintaining the visual
quality.
W
A
S
D
W
A
S
D
W
A
S
D
Figure 9. Interactive results on the third-perspective game video
generation.
W
A
S
D
W
A
S
D
W
A
S
D
Figure 10. Hunyuan-GameCraft enables high-fidelity and high-
dynamic real-world video generation with accurate camera con-
trol.
enhances its generalization capabilities, enabling it to gen-
erate interactive videos in real-world domains as well. As
shown in Fig 10, given images in real world, Hunyuan-
GameCraft can successfully generate reasonable video with
conditioned camera movement while keeping the dynamics.
7. Limitations and Future Work
While Hunyuan-GameCraft demonstrates impressive capa-
bilities in interactive game video generation, its current ac-
tion space is mainly tailored to open-world exploration and
lacks a wider array of game-specific actions such as shoot-
ing, throwing, and explosions.
In future work, we will
expand the dataset with more diverse gameplay elements.
Building on our advancements in controllability, long-form
video generation, and history preservation, we will focus
on developing the next-generation model for more physical
and playable game interactions.
8. Conclusion
In this paper, we introduce Hunyuan-GameCraft, a signifi-
cant step forward in interactive video generation. Through
a unified action representation, hybrid history-conditioned
training, and model distillation, our framework enables
fine-grained control, efficient inference, and scalable long
video synthesis. Besides, Hunyuan-GameCraft delivers en-
hanced realism, responsiveness, and temporal coherence.
Our results demonstrate substantial improvements over ex-
isting methods, establishing Hunyuan-GameCraft as a ro-
bust foundation for future research and real-time deploy-
ment in immersive gaming environments.
References
[1] Andreas Blattmann, Tim Dockhorn, Sumith Kulal, Daniel
Mendelevitch, Maciej Kilian, Dominik Lorenz, Yam Levi,
Zion English, Vikram Voleti, Adam Letts, et al. Stable video
diffusion: Scaling latent video diffusion models to large
datasets. arXiv preprint arXiv:2311.15127, 2023. 3

--- Page 11 ---

[2] Andreas Blattmann, Robin Rombach, Huan Ling, Tim Dock-
horn, Seung Wook Kim, Sanja Fidler, and Karsten Kreis.
Align your latents: High-resolution video synthesis with la-
tent diffusion models. In Proceedings of the IEEE/CVF con-
ference on computer vision and pattern recognition, pages
22563–22575, 2023. 3
[3] Gary Bradski. The opencv library. Dr. Dobb’s Journal: Soft-
ware Tools for the Professional Programmer, 25(11):120–
123, 2000. 4
[4] Brandon Castellano. PySceneDetect. 4
[5] Haoxuan Che, Xuanhua He, Quande Liu, Cheng Jin, and
Hao Chen. Gamegen-x: Interactive open-world game video
generation. In International Conference on Learning Repre-
sentations, 2025. 3, 4
[6] Boyuan Chen, Diego Mart´ı Mons´o, Yilun Du, Max Sim-
chowitz, Russ Tedrake, and Vincent Sitzmann.
Diffusion
forcing: Next-token prediction meets full-sequence diffu-
sion. Advances in Neural Information Processing Systems,
37:24081–24125, 2024. 3, 4
[7] Karan Dalal, Daniel Koceja, Gashon Hussein, Jiarui Xu,
Yue Zhao, Youjin Song, Shihao Han, Ka Chun Cheung, Jan
Kautz, Carlos Guestrin, et al. One-minute video generation
with test-time training.
arXiv preprint arXiv:2504.05298,
2025. 4
[8] Decard.
Oasis:
A
universe
in
a
transformer.
https://www.decart.ai/articles/oasis-
interactive-ai-video-game-model, 2024. 4
[9] Patrick Esser, Sumith Kulal, Andreas Blattmann, Rahim
Entezari, Jonas M¨uller, Harry Saini, Yam Levi, Dominik
Lorenz, Axel Sauer, Frederic Boesel, et al. Scaling recti-
fied flow transformers for high-resolution image synthesis.
In Forty-first international conference on machine learning,
2024. 5
[10] Ruili Feng, Han Zhang, Zhantao Yang, Jie Xiao, Zhilei
Shu, Zhiheng Liu, Andy Zheng, Yukun Huang, Yu Liu,
and Hongyang Zhang. The matrix: Infinite-horizon world
generation with real-time moving control.
arXiv preprint
arXiv:2412.03568, 2024. 4
[11] Kaifeng Gao, Jiaxin Shi, Hanwang Zhang, Chunping Wang,
and Jun Xiao.
Vid-gpt: Introducing gpt-style autoregres-
sive generation in video diffusion models.
arXiv preprint
arXiv:2406.10981, 2024. 4
[12] Yuchao Gu, Weijia Mao, and Mike Zheng Shou.
Long-
context autoregressive video modeling with next-frame pre-
diction. arXiv preprint arXiv:2503.19325, 2025. 4
[13] Hao He, Yinghao Xu, Yuwei Guo, Gordon Wetzstein, Bo
Dai, Hongsheng Li, and Ceyuan Yang. Cameractrl: Enabling
camera control for text-to-video generation. arXiv preprint
arXiv:2404.02101, 2024. 3, 8
[14] Hao He, Ceyuan Yang, Shanchuan Lin, Yinghao Xu, Meng
Wei, Liangke Gui, Qi Zhao, Gordon Wetzstein, Lu Jiang, and
Hongsheng Li. Cameractrl ii: Dynamic scene exploration
via camera-controlled video diffusion models. arXiv preprint
arXiv:2503.10592, 2025. 3
[15] Roberto Henschel, Levon Khachatryan, Hayk Poghosyan,
Daniil Hayrapetyan, Vahram Tadevosyan, Zhangyang Wang,
Shant Navasardyan, and Humphrey Shi. Streamingt2v: Con-
sistent, dynamic, and extendable long video generation from
text. arXiv preprint arXiv:2403.14773, 2024. 3, 4
[16] Ziqi Huang, Yinan He, Jiashuo Yu, Fan Zhang, Chenyang Si,
Yuming Jiang, Yuanhan Zhang, Tianxing Wu, Qingyang Jin,
Nattapol Chanpaisit, et al. Vbench: Comprehensive bench-
mark suite for video generative models. In Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 21807–21818, 2024. 8
[17] KolorsTeam. Kolors: Effective training of diffusion model
for photorealistic text-to-image synthesis.
arXiv preprint,
2024. 4
[18] Weijie Kong, Qi Tian, Zijian Zhang, Rox Min, Zuozhuo Dai,
Jin Zhou, Jiangfeng Xiong, Xin Li, Bo Wu, Jianwei Zhang,
et al. Hunyuanvideo: A systematic framework for large video
generative models. arXiv preprint arXiv:2412.03603, 2024.
3, 5, 8
[19] Ruihuang Li, Caijin Zhou, Shoujian Zheng, Jianxiang Lu,
Jiabin Huang, Comi Chen, Junshu Tang, Guangzheng Xu,
Jiale Tao, Hongmei Wang, et al. Hunyuan-game: Industrial-
grade intelligent game creation model.
arXiv preprint
arXiv:2505.14135, 2025. 3
[20] Yu Lu, Yuanzhi Liang, Linchao Zhu, and Yi Yang. Free-
long: Training-free long video generation with spectralblend
temporal attention. arXiv preprint arXiv:2407.19918, 2024.
3
[21] Simian Luo, Yiqin Tan, Longbo Huang, Jian Li, and Hang
Zhao.
Latent consistency models:
Synthesizing high-
resolution images with few-step inference. arXiv preprint
arXiv:2310.04378, 2023. 7
[22] Jack Parker-Holder, Philip Ball, Jake Bruce, Vibhavari
Dasagi, Kristian Holsheimer, Christos Kaplanis, Alexandre
Moufarek, Guy Scully, Jeremy Shar, Jimmy Shi, Stephen
Spencer, Jessica Yung, Michael Dennis, Sultan Kenjeyev,
Shangbang Long, Vlad Mnih, Harris Chan, Maxime Gazeau,
Bonnie Li, Fabio Pardo, Luyu Wang, Lei Zhang, Fred-
eric Besse, Tim Harley, Anna Mitenkova, Jane Wang, Jeff
Clune, Demis Hassabis, Raia Hadsell, Adrian Bolton, Satin-
der Singh, and Tim Rockt¨aschel.
Genie 2: A large-scale
foundation world model. 2024. 3, 4
[23] Ivan Skorokhodov, Sergey Tulyakov, and Mohamed Elho-
seiny. Stylegan-v: A continuous video generator with the
price, image quality and perks of stylegan2. In Proceedings
of the IEEE/CVF conference on computer vision and pattern
recognition, pages 3626–3636, 2022. 4
[24] Zachary Teed and Jia Deng. Raft: Recurrent all-pairs field
transforms for optical flow.
In Computer Vision–ECCV
2020: 16th European Conference, Glasgow, UK, August 23–
28, 2020, Proceedings, Part II 16, pages 402–419. Springer,
2020. 4
[25] Thomas Unterthiner, Sjoerd Van Steenkiste, Karol Kurach,
Rapha¨el Marinier, Marcin Michalski, and Sylvain Gelly.
Fvd: A new metric for video generation. 2019. 8
[26] Dani Valevski, Yaniv Leviathan, Moab Arar, and Shlomi
Fruchter.
Diffusion models are real-time game engines.
arXiv preprint arXiv:2408.14837, 2024. 4
[27] Team Wan, Ang Wang, Baole Ai, Bin Wen, Chaojie Mao,
Chen-Wei Xie, Di Chen, Feiwu Yu, Haiming Zhao, Jianx-

--- Page 12 ---

iao Yang, Jianyuan Zeng, Jiayu Wang, Jingfeng Zhang, Jin-
gren Zhou, Jinkai Wang, Jixuan Chen, Kai Zhu, Kang Zhao,
Keyu Yan, Lianghua Huang, Mengyang Feng, Ningyi Zhang,
Pandeng Li, Pingyu Wu, Ruihang Chu, Ruili Feng, Shiwei
Zhang, Siyang Sun, Tao Fang, Tianxing Wang, Tianyi Gui,
Tingyu Weng, Tong Shen, Wei Lin, Wei Wang, Wei Wang,
Wenmeng Zhou, Wente Wang, Wenting Shen, Wenyuan Yu,
Xianzhong Shi, Xiaoming Huang, Xin Xu, Yan Kou, Yangyu
Lv, Yifei Li, Yijing Liu, Yiming Wang, Yingya Zhang, Yi-
tong Huang, Yong Li, You Wu, Yu Liu, Yulin Pan, Yun
Zheng, Yuntao Hong, Yupeng Shi, Yutong Feng, Zeyinzi
Jiang, Zhen Han, Zhi-Fan Wu, and Ziyu Liu. Wan: Open
and advanced large-scale video generative models.
arXiv
preprint arXiv:2503.20314, 2025. 8
[28] Fu-Yun Wang, Zhaoyang Huang, Alexander Bergman,
Dazhong Shen, Peng Gao, Michael Lingelbach, Keqiang
Sun, Weikang Bian, Guanglu Song, Yu Liu, et al. Phased
consistency models. Advances in neural information pro-
cessing systems, 37:83951–84009, 2024. 3, 5, 7
[29] Peng Wang, Shuai Bai, Sinan Tan, Shijie Wang, Zhihao Fan,
Jinze Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin
Ge, et al. Qwen2-vl: Enhancing vision-language model’s
perception of the world at any resolution.
arXiv preprint
arXiv:2409.12191, 2024. 4
[30] Xiaofeng Wang, Zheng Zhu, Guan Huang, Boyuan Wang,
Xinze Chen, and Jiwen Lu. Worlddreamer: Towards general
world models for video generation via predicting masked to-
kens. arXiv preprint arXiv:2401.09985, 2024. 3
[31] Zhouxia Wang, Ziyang Yuan, Xintao Wang, Yaowei Li,
Tianshui Chen, Menghan Xia, Ping Luo, and Ying Shan.
Motionctrl: A unified and flexible motion controller for
video generation. In ACM SIGGRAPH 2024 Conference Pa-
pers, pages 1–11, 2024. 3, 8
[32] WorldLabs.
Generating worlds.
https : / / www .
worldlabs.ai/blog, 2024. 3
[33] Mengyue Yang, Furui Liu, Zhitang Chen, Xinwei Shen,
Jianye Hao, and Jun Wang. Causalvae: Disentangled rep-
resentation learning via neural structural causal models. In
Proceedings of the IEEE/CVF conference on computer vi-
sion and pattern recognition, pages 9593–9602, 2021. 3
[34] Jiwen Yu, Yiran Qin, Xintao Wang, Pengfei Wan, Di Zhang,
and Xihui Liu. Gamefactory: Creating new games with gen-
erative interactive videos. arXiv preprint arXiv:2501.08325,
2025. 4
[35] Junyi Zhang, Charles Herrmann, Junhwa Hur, Varun Jam-
pani, Trevor Darrell, Forrester Cole, Deqing Sun, and Ming-
Hsuan Yang.
Monst3r: A simple approach for estimat-
ing geometry in the presence of motion.
arXiv preprint
arXiv:2410.03825, 2024. 4
[36] Yifan Zhang, Chunli Peng, Boyang Wang, Puyi Wang,
Qingcheng Zhu, Zedong Gao, Eric Li, Yang Liu, and Yahui
Zhou.
Matrix-game: Interactive world foundation model.
arXiv, 2025. 4

```
