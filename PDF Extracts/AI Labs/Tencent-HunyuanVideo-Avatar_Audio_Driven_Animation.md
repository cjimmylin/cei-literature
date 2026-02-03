---
title: "HunyuanVideo Avatar Audio Driven Animation"
source_pdf: "/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/AI Labs/Tencent/HunyuanVideo/HunyuanVideo-Avatar_Audio_Driven_Animation.pdf"
company: "Tencent"
pages: 20
extracted_at: "2026-02-02T16:29:05.102065"
type: "ai_lab_paper"
---

# HunyuanVideo Avatar Audio Driven Animation

**Company/Lab:** Tencent
**Model:** HunyuanVideo
**Source PDF:** /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/AI Labs/Tencent/HunyuanVideo/HunyuanVideo-Avatar_Audio_Driven_Animation.pdf
**Total Pages:** 20

---

## Content

```
--- Page 1 ---

arXiv:2505.20156v2  [cs.CV]  3 Jun 2025
HunyuanVideo-Avatar: High-Fidelity Audio-Driven
Human Animation for Multiple Characters
Tencent Hunyuan
Page:
https://hunyuanvideo-avatar.github.io
Model:
https://huggingface.co/tencent/HunyuanVideo-Avatar
Code:
https://github.com/Tencent-Hunyuan/HunyuanVideo-Avatar
Mutiple Characters
Emotion Control
Diverse Character Styles
Happy
Sad
Angry
Figure 1: HunyuanVideo-Avatar can generate videos using a character image and audio as input.
HunyuanVideo-Avatar enables the creation of multi-character, highly consistent, and dynamic human
animations that accurately reflect the emotions expressed in the audio.
Abstract
Recent years have witnessed significant progress in audio-driven human animation.
However, critical challenges remain in (i) generating highly dynamic videos while
preserving character consistency, (ii) achieving precise emotion alignment between
characters and audio, and (iii) enabling multi-character audio-driven animation. To
address these challenges, we propose HunyuanVideo-Avatar, a multimodal diffu-
sion transformer (MM-DiT)-based model capable of simultaneously generating
dynamic, emotion-controllable, and multi-character dialogue videos. Concretely,
HunyuanVideo-Avatar introduces three key innovations: (i) A character image
injection module is designed to replace the conventional addition-based character
conditioning scheme, eliminating the inherent condition mismatch between training
and inference. This ensures the dynamic motion and strong character consistency;
(ii) An Audio Emotion Module (AEM) is introduced to extract and transfer the
emotional cues from an emotion reference image to the target generated video,

--- Page 2 ---

enabling fine-grained and accurate emotion style control; (iii) A Face-Aware Audio
Adapter (FAA) is proposed to isolate the audio-driven character with latent-level
face mask, enabling independent audio injection via cross-attention for multi-
character scenarios. These innovations empower HunyuanVideo-Avatar to surpass
state-of-the-art methods on benchmark datasets and a newly proposed wild dataset,
generating realistic avatars in dynamic, immersive scenarios.
1
Introduction
In recent years, Diffusion Transformers (DiT) have significantly advanced video generation. Among
these developments, text-to-video and image-to-video techniques [2, 43, 3, 4, 9, 42, 10, 34, 12, 5, 37,
27, 19, 31, 22] have gained increasing attention due to their near-practical applicability. Audio-driven
human animation, in particular, has experienced explosive growth, as it enables realistic human video
synthesis with minimal input. Recent DiT-based approaches [40, 33, 24, 7, 21] have demonstrated
superior performance in audio-driven generation compared to existing methods.
Current audio-driven human animation methods can be broadly categorized into two paradigms:
portrait animation and full-body animation. Portrait animation methods [40, 33, 24, 7, 21] focus
exclusively on facial movements while maintaining static or simplistic backgrounds. This narrow
scope creates a fundamental disconnect between animated characters and their environments, often
resulting in outputs that fail to meet practical expectations for immersive video content. Full-body
animation methods [13, 20, 21] address this spatial limitation by extending motion to the full body.
However, they face persistent challenges including unnatural character movements, misalignment
between audio emotions and facial expressions, and an inability to drive multi-character scenes
with audio. These limitations currently represent the most significant barrier to developing truly
convincing audio-driven human animations.
Recent advances in audio-driven human animation have achieved significant progress, yet critical
challenges persist in motion quality, character consistency, emotion alignment, and multi-character
audio-driving. For instance, Hallo-3 [7], a DiT-based portrait animation method, generates only
facial movements while neglecting body motion. CyberHost [20] employs region attention and
ReferenceNet to control facial and hand motions but often produces unrealistic movements in both
the human body and background. OmniHuman-1 [21] introduces a multimodal motion-conditioned
hybrid training strategy to mitigate data scarcity issues, yet it still struggles with emotion-audio
misalignment and multi-character scene generation. These limitations underscore the need for more
robust solutions. To address these gaps, our work focuses on three key objectives: (i) improving
dynamic expressiveness while preserving character identity, (ii) ensuring precise emotion synchro-
nization between audio and video, and (iii) enabling realistic multi-character dialogue generation for
real-world applications.
First, current audio-driven human animation methods typically rely on reference images during
inference to enforce consistency between the generated video and the reference. However, this
approach often leads to unnatural motion, as the model tends to replicate expressions and poses
from the reference rather than generating dynamic, audio-aligned movements. To overcome this
limitation, we propose a character image injection module, which transforms human image features
into representations more amenable to model learning. By injecting these features along the channel
dimension, we avoid the trade-off between dynamism and consistency that arises from direct latent
space usage, ensuring coherence between training and inference.
Second, we introduce an Audio Emotion Module (AEM) to align video characters’ emotions with
those conveyed in the audio. This module leverages reference images to guide emotion mapping,
ensuring that facial expressions accurately reflect the audio’s affective content, thereby improving
realism in human animation.
Finally, to address the challenge of multi-character animation, we propose a Face-Aware Audio
Adapter (FAA). This module applies a face mask to latent features extracted from the input, generating
face-masked video latents that are then fused with audio information. Since the audio primarily
influences the masked face region, we can independently drive different characters using distinct
audio inputs, enabling realistic multi-character dialogue generation for cinematic applications.
2

--- Page 3 ---

Extensive experiments demonstrate that our framework effectively drives multi-person scenarios with
audio, significantly improving both dynamism and consistency in generated videos. The key modules
of HunyuanVideo-Avatar are as follows:
• A character image injection module that resolves the dynamism-consistency trade-off caused
by reference image usage, enhancing overall motion quality in foreground and background
regions.
• An Audio Emotion Module (AEM) that aligns video characters’ emotions with audio-driven
affective cues, improving realism in facial expressions.
• A Face-Aware Audio Adapter (FAA) that enables localized audio-driven animation for
multiple characters by masking targeted face regions in the latent space, facilitating multi-
character dialogue generation.
2
Related work
Audio-conditioned portrait animation. SadTalker [40] generates 3D motion coefficients (including
head pose and expression) from audio and implicitly modulates a novel 3D-aware face rendering
technique, addressing issues of unnatural head movement, distorted expressions, and identity modi-
fication in existing talking head video generation, demonstrating superior performance in terms of
motion and video quality. Hallo [39] proposes an innovative hierarchical audio-driven visual synthe-
sis approach based on diffusion models, which seamlessly integrates generative models, denoisers,
temporal alignment techniques, and a reference network to achieve precise synchronization between
audio inputs and visual outputs, thereby enhancing the performance of portrait image animation in
terms of image quality, lip-sync accuracy, and motion diversity. V-Express [33] balances strong and
weak control signals through progressive drop operations, enabling effective use of weak signals
like audio in portrait video generation while considering pose, input image, and audio. Experiments
validate its effectiveness. EchoMimic [24] innovatively uses both audio and facial landmarks for
training, addressing the instability and unnatural results of using audio or landmarks alone, enabling
the generation of more natural portrait videos. Loopy [16] learns natural motion and improves
audio-portrait movement correlation through designed temporal modules and an audio-to-latents
module, eliminating the need for manual motion templates to generate more realistic and high-quality
videos. Hallo3 [7] is designed with a Transformer-based identity reference network to ensure facial
identity consistency, and explores speech audio conditions and motion frame mechanisms to enable
the model’s voice-driven capabilities. In OmniHuman-1 [21], a multimodal motion condition hybrid
training strategy is introduced, enabling the model to benefit from data augmentation with mixed
conditions, thereby overcoming the challenges faced by previous end-to-end methods due to the
scarcity of high-quality data.
Audio-conditioned full-body animation. DiffTED [13] is a novel one-shot audio-driven framework
that leverages a diffusion model to generate synchronized and diverse talking head animations with
natural co-speech gestures from a single image, using keypoint-guided Thin-Plate Spline motion
modeling for temporally coherent and expressive video synthesis. CyberHost [20] includes two
aspects: the Region Attention Module (RAM) maintains identity-independent latent features and
combines identity-specific local visual features to enhance synthesis in key areas. Additionally, by
introducing human prior-based conditions, it incorporates human structural priors into the model,
reducing uncertainty in motion generation and improving video stability.
3
Methods
Given a reference image, a driving audio, and a facial mask of the character, our method can generate
talking videos of single or multiple characters based on the driving audio. The overall framework of
our method is illustrated in the figure 2. Specifically, we adopt HunyuanVideo [17] as our backbone.
It is a video generation model built upon the MM-DiT architecture.
In Section 3.1, we briefly introduced some preliminary knowledge. In Section 3.2, we explore a
character image injection module, which can maintain both character consistency and vividness.
Then, in Section 3.3, we discuss how to apply an audio adapter to face region to enable multi-character
audio-driven animation. In Section 3.4 we discuss an emotion alignment module. In Section 3.5, we
briefly introduce the long video generation mechanism.
3

--- Page 4 ---

Double Block
Single Block
Double Block
Double Block
Single Block
3D
Encoder
Tokenizers
Ref Image
GT Video
Repeat
3D
Encoder
Tokenizers
Copy weight
Projection
Hunyuan Video
3D
Decoder
The women is 
extremely happy. A 
Women is singing 
while siting. 
Tuning Weight
Frozen Weight
Element Add
(HAPPY)
Emotion Ref Image
Projection
LLaVA
Double Block
3D
Encoder
Saptial
CrossAttention
Audio Emotion
Module
Text Token
Video Token
Image Token
Face Mask
Video
Latent
K
V
Saptial CrossAttention
Audio
Face-Aware Audio Adapter
Whisper
Q
Face Masked 
Video Latent
Figure 2: The framework of HunyuanVideo-Avatar. It consists of three parts: (1) Character Image
Injection Module, which ensures high consistency of the character while maintaining high dynamics;
(2) Audio Emotion Module, which aligns the character’s facial expressions in the video with the
emotions in the audio; and (3) Face-aware Audio Adapter, which enables audio-driven multiple
characters.
3.1
Preliminaries
Firstly, we resize the target image to match the dimensions of the video frames. We then use the
pretrained 3D VAE from HunyuanVideo to map the reference image R from image space to the latent
space, obtaining the reference image latent vR ∈Rw×h×c, where w and h denote the width and height
of the latent, and c is the feature dimension. Similarly, we encode the noise video using the 3D VAE
to obtain the video latent vnoise ∈Rf×w×h×c, where f is the the number of video frames. Next, we
process vR and vnoise with Tokenizer2 K2 to obtain tR ∈Rwh×c and tnoise ∈Rfwh×c, respectively.
We then replicate the reference image T times (where T is the original video length) to obtain ir, and
use the 3D VAE together with Tokenizer1 K1 (initialized with the weights of Tokenizer2) to obtain
tr ∈Rfwh×c. We add tr and tnoise element-wise, and concatenate the result with tR along the token
dimension to form the final input p, as shown below:
p = TokenCat ({K1(tr) + K2(z0)} , tR)
(1)
Thanks to the strong temporal modeling prior of HunyuanVideo, identity information can be efficiently
propagated along the time axis. Therefore, we assign 3D-RoPE [28] positional encoding to the
concatenated image latent. In the original HunyuanVideo, video latents are assigned 3D-RoPE along
the time, width, and height axes; for a pixel at position (l, i, j) (where l is the frame index, i is the
width, and j is the height), the RoPE is RoPE(l, i, j). For the image latent, to enable effective
broadcasting of identity information along the temporal sequence, we place it at the −1-th frame, i.e.,
before the first frame with time index 0. Furthermore, inspired by Omnicontrol [29] in controllable
image generation, to prevent the model from simply copying and pasting the target image into the
generated frames, we introduce a spatial shift for the image latent, as follows:
RoPEzI(l, i, j) = RoPE(−1, i + w, j + h).
(2)
During the training process, we employ the Flow Matching [23] framework to optimize our video
generation model. Specifically, we first extract the latent representation of the video, denoted as
z1, along with its corresponding reference image R. To introduce stochasticity, we sample a time
step t ∈[0, 1] from a logit-normal distribution [8]. We then initialize the noise vector z0 ∼N(0, I)
from a standard Gaussian distribution. The training sample at time t, zt, is constructed by linearly
interpolating.
The model is trained to predict the velocity ut = dzt
dt at each time step to guide the sample zt towards
z1. During optimization, the model outputs a predicted velocity λt, and the parameters are updated
4

--- Page 5 ---

QKV Concat
Q
K
V
Attention
Projection
Projection
Tokenizer
Tokenizer1
Tokenizer2
Tokenizer1
QKV Concat
Q
K
V
Attention
Projection
QKV Concat
Q
K
V
Attention
Projection
Tokenizer2
Image Repeat T times
Repeat
(a) Token Concat
(b) Token Concat + Channel Concat
(c) Ours
Text 
Token
Video
Token
Image
Token
Image Token
Figure 3: Three types of Character Image Injection Module.
by minimizing the mean squared error between λt and the ground-truth velocity ut. The overall
generation loss is defined as:
Lgeneration = Et,z0,z1 ∥λt −ut∥2 .
(3)
This training strategy enables the model to effectively learn the underlying data distribution and
generate high-quality, customized video content conditioned on the reference image.
3.2
Character Image Injection Module
In previous I2V methods, padding frames were often used for video inference. While this approach
ensures good integrity and consistency of characters, backgrounds, and foregrounds, it also limits
the motion dynamics of the generated video. Additionally, padding frames can lead to misalignment
between the training and inference processes. Removing padding frames for video inference results
in better motion dynamics but severely compromises character consistency and integrity. Therefore,
we explored three character image injection mechanisms, as illustrated in Figure 3: (a) the reference
image and video are processed through the same tokenizer, and the generated latents are concatenated
in the token dimension; (b) the character image is first repeated T times (T represents the length of the
video) and concatenated with the original video in the channel dimension, then fed into tokenizer1,
while the character reference image is fed into tokenizer2, and both are concatenated in the token
dimension before fed to the model; (c) the reference image is first repeated T times and fed into
tokenizer2, then added directly to the video latent through a projection module composed of fully
connected layers fed to the model. The mechanism (c) shows better results compared to mechanisms
(a) and (b), as it improves the dynamics of motion while ensuring the consistency and integrity of
characters, backgrounds, and foregrounds in the video, significantly enhancing video quality. For
specific ablation comparisons experience, please refer to the experiment section. Since the backbone’s
tokenizer1 is specifically trained for video, we need to add an extra tokenizer2 to fit the image branch.
The weights of this tokenizer are copied from the backbone’s tokenizers, and we found that this
approach accelerates model convergence.
3.3
Face-aware Audio Adapter
In terms of audio conditioning, we use Whisper [25] for audio feature extraction, and for face masks,
we employ the InsightFace [26] method to detect the bounding box of the facial region. Given an
audio-video sequence consisting of n′ frames, we extract audio features for each frame, yielding a
feature tensor of shape n′ × 10 × d, where 10 denotes the number of tokens per audio frame. The
corresponding video latent representations are temporally compressed by a pretrained 3D VAE into n
frames, with n =
j
n′
4
k
+ 1—where the additional 1 accounts for the initial, uncompressed frame,
and 4 is the temporal compression ratio. Furthermore, to incorporate identity information, an identity
image is concatenated at the beginning, resulting in a video latent of n + 1 frames.
5

--- Page 6 ---

To ensure temporal alignment between the audio features and the compressed video latent, we first
pad the audio feature sequence prior to the initial frame, producing a total of (n+1)×4 audio frames.
We then aggregate every four consecutive audio frames into one, resulting in a temporally aligned
audio feature tensor gA that matches the structure of the video latent representation:
gA = Rearrange(gA,0) : [b, (n + 1) × 4, 10, d] →[b, (n + 1), 40, d].
(4)
To ensure temporal alignment between the face mask and the compressed video latent, we set the
face mask corresponding to the initial frame to 1, and also make it contain a total of (n + 1) × 4
mask frames. This results in a mask gM that is both temporally and spatially aligned with the video
latent. With the temporally aligned audio features gA, we introduce audio information into the video
latent representation yt using a cross-attention mechanism. To prevent interference across different
time steps, we adopt a spatial cross-attention strategy that performs audio injection separately for
each time step. Specifically, each audio frame interacts only with the spatial tokens of its temporally
aligned video frame, and cross-attention is applied independently at each temporal index. To this
end, we decouple the temporal dimension from the spatial dimensions of the video latent and apply
attention solely along the spatial axes:
y′
t,A = Rearrange(yt) :[b, (n + 1)wh, d] →[b, n + 1, wh, d],
y′′
t,A = y′
t,A+αA × CrossAttn(gA, y′
t) × gM,
yt,A = Rearrange(y′′
t,A) :[b, n + 1, wh, d] →[b, (n + 1)wh, d],
(5)
where αA is a weight to control the influence of the audio feature.
3.4
Audio Emotion Module
To align the emotion conveyed in the audio with the character’s facial expression, we compress the
emotional reference image into features using a pretrained 3D VAE, and then inject these features into
the Double Block of HunyuanVideo through an FC layer and spatial cross-attention mechanism.
Specifically, the reference image features serve as the Key and Value, while the original video
latent representation serves as the Query. This approach fuses information from the emotional
reference image with the masked video latent yt,A, enabling the model to better understand the
relationship between audio emotion and facial expressions. To formalize this process, we first encode
the emotional reference image Eref = Encoder(Iref), where Eref denotes the encoded feature of the
emotional reference image Iref. Next, to integrate these features into the video latent representation,
we perform the following steps: We first reshape the video latent yt,A into temporal-spatial dimensions
as y
′
t,A, then apply an FC layer and spatial cross-attention to inject emotional features: y′′
t,A,E, and
finally restore the original structure:
y
′
t,A = Rearrange(yt,A) :[b, (n + 1)wh, d] →[b, n + 1, wh, d],
y′′
t,A,E = y′
t,A+γE × CrossAttn(FC(Eref), y
′
t,A),
yt,A,E = Rearrange(y
′
t,A,E) :[b, n + 1, wh, d] →[b, (n + 1)wh, d],
(6)
where γE is a learnable scaling factor that controls the influence of the emotional reference features
on the video latent. Notably, we found that inserting this module into a Single Block does not
allow the model to effectively learn emotional cues. In contrast, integrating it into a Double Block
enables the model to better drive and express character emotions. This suggests that the Double
Block architecture plays a crucial role in capturing and representing emotional details during complex
emotion-to-expression mapping tasks.
3.5
Long Video Generation
The HunyuanVideo-13B model [17] can only generate videos with 129 frames, which is often
shorter than the audio length. To tackle the challenge of generating long videos, we use the Time-
aware Position Shift Fusion method from Sonic [15]. We successfully adapt this method to the
HunyuanVideo-13B model, which is based on the MM-DiT architecture, and achieve good results.
6

--- Page 7 ---

This fusion strategy is simple yet effective, as it does not add any extra inference or training costs. It
helps to reduce issues like jitter and abrupt transitions during video generation.
As shown in Algorithm 1, at each timestep, the model takes a segment of the audio as input to predict
the corresponding latent. It uses a starting offset to smoothly connect with the segment from the
previous timestep, shifting forward by α steps each time. We set the offset α to 3-7 at each timestep,
and our experiments show that this is an effective choice. This approach allows HunyuanVideo-Avatar
to naturally bridge the context, enabling continuous video generation that follows the audio prompts.
Algorithm 1 Long Video Fusion
Require: Audio embedding v[0,l]
a
with length l, denoising steps T, initial noisy latent z[0,l]
T
, pretrained
HunyuanVideo-Avatar model HVA(·) for sequence length f, position-shift offset α < f < l.
Ensure: Denoised latent z[0,l]
0
.
1: Initialize accumulated shift offset αβ = 0.
2: for t = T, · · · , 1 do
3:
// Denoising loop
4:
Initialize start point s = αβ, end e = s + f, processed
length n = 0.
// Start from new position for each timestep.
5:
while n < l do
6:
// Sequence loop
7:
z[s,e]
t−1 = HVA(z[s,e]
t
, v[s,e]
a
, t)
8:
s ←−s + f, e ←−e + f, n ←−n + f.
// Move to next clip non-overlapping
9:
if s > l or e > l then
10:
s ←−s%l, e ←−e%l.
// Padding circularly
11:
end if
12:
end while
13:
αβ ←−αβ + α.
// Accumulate shift offset
14: end for
15: return Denoised latent z[0,l]
0
.
4
Experiment
4.1
Experiment Settings
Hallo
EchoMimic
Hallo3
Ours
Sonic
EchoMimic2
Reference 
Image
Reference 
Image
Figure 4: Qualitative comparison on the HTDF dataset.
Implementation Details.
We use HunyuanVideo-I2V [17] as the base model for HunyuanVideo-
Avatar. The training process consists of two distinct stages. In the first stage, we train exclusively on
audio-only data to establish fundamental audio-visual alignment. In the second stage, we implement
a mixed training regime combining audio and image data in a 1:1.5 ratio to enhance motion stability.
The resolution of the training data ranged from 704 × 704 to 704 × 1216. Throughout the training, we
7

--- Page 8 ---

woman audio
man audio
Emotion(Sad and Happy)
Diverse Character Styles
MutipleCharacter
Figure 5: Visualization of videos generated by HunyuanVideo-Avatar on the wild dataset.
Ours
OmniHuman
FantasyTalking
Reference 
Image
Figure 6: Qualitative comparison on the wild body dataset.
maintain fixed parameters for both LLaVA and 3D VAE while updating all other learnable parameters.
We use 160 GPUs with 96GB of memory each, set the global batch size to 40, and the learning rate
to 1e-5.
Datasets.
To obtain high-quality training data, we use LatentSync [18] to filter out audio-visual
asynchronous data and employ tools such as Koala-36M [36] to filter out data with low brightness or
low aesthetics. Through this standardized data selection process, we obtain 500,000 samples with
character audio for training, with a total duration of approximately 1,250 hours. During the testing
stage, we select the publicly available portrait datasets CelebV-HQ [44] (a dataset containing diverse
scenes) and HDTF [41] (A dataset containing high-resolution videos and a larger number of subjects.)
to evaluate the portrait animation capabilities of various methods. In addition, since there is currently
no publicly available full-body animation test set, we construct our own full-body animation test set,
which contains 250 videos covering 200 identities, involving different races, ages, genders, styles,
and initial actions.
Evaluation Metrics and Compared Baselines.
We use the Q-align [38] visual language model
(VLM) to evaluate video quality (IQA) and aesthetic metrics (ASE), and use FID [11] and FVD [30]
8

--- Page 9 ---

to assess the distance between generated videos and real videos. In addition, we use the smoothness
metric from VBench [14] to evaluate video motion stability, and employ Sync-C [6] to assess audio-
visual synchronization. Apart from objective metrics, we also conducted a subjective evaluation with
30 users. The thirty users rated the generated results across four dimensions: lip synchronization(LS),
Identity Preservation (IP), Full-body Naturalness(FBN), and Facial Naturalness(FCN). To compre-
hensively assess the advancement of our method, we compared it with the current state-of-the-art
audio-driven portrait animation methods, including Sonic [15], EchoMimic [24], EchoMimic-V2 [24],
Hallo-3 [7], and Omnihuman-1 [21]. For audio-driven full-body animation, we first compared
Hallo3 [7], FantasyTalking [35] and Omnihuman-1 on our proposed full-body animation test set.
4.2
Comparison with State-of-the-Art Methods
Qualitative Results.
We conducted qualitative comparisons with existing methods. For audio-
driven portrait animation, we mainly compared our approach with Sonic, EchoMimic, EchoMimicV2,
and Hallo-3 on the HDTF dataset, which primarily focuses on lip synchronization and facial expres-
sion accuracy. As shown in the figure 4, our method produces results with higher video quality, more
natural and vivid facial expressions, and more aesthetically pleasing video effects on this dataset.
For audio-driven full-body animation, The figure 4 demonstrates the effectiveness of our model across
various styles of characters, emotion control, and audio-driven multi-character scenarios, showcasing
the validity of our approach. Then we mainly compared our method with Hallo3, FantasyTalking,
and OmniHuman-1 on the wild full-body dataset. As illustrated in the figure 6, our method generates
videos that exhibit more natural variations in the foreground, background, and character movements,
while also achieving more accurate lip synchronization and better character consistency, resulting
in higher overall video quality. These improvements are attributed to our method’s focus on the
audio adapter module for audio-driven human animation and the character image injection module.
Therefore, our approach is better suited to meet the demands of practical application scenarios. More
comparative results and visual results are provided in the Appendix.
Quantitative Results.
To thoroughly validate the superiority of our method in audio-driven portrait
animation, we compared our approach with baseline methods on various evaluation metrics using the
CelebV-HQ and HDTF test sets. As shown in the table 1, the results demonstrate that our method
achieves the best performance in FID, FVD, IQA, ASE, and Sync-C, proving the effectiveness of our
approach in audio-driven portrait animation and showcasing its capability in audio synchronization.
Meanwhile, to verify the superiority of our method in audio-driven full-body animation, we conducted
a comparison with baseline methods on various evaluation metrics using our proposed test set. As
shown in Table 1, the experimental results demonstrate that our method achieves the best performance
on most evaluation metrics, proving its effectiveness in audio-driven portrait animation generation
and showcasing its capability in audio-visual synchronization.
User Study.
To further validate the effectiveness of our proposed method, we conducted a subjective
evaluation on the wild full-body animation dataset. Each participant assessed four key dimensions:
lip synchronization(LS), Identity Preservation (IP), Full-body Naturalness(FBN), and Facial Natural-
ness(FCN). A total of 30 participants rated each aspect on a scale from 1 to 5. As shown in the table 2,
the results indicate that HunyuanVideo-Avatar outperforms existing baseline methods in the IP and
LS evaluation dimensions, which is attributed to the enhancements brought by our Character Image
Injection Module and Face-aware Audio Adapter. Since OmniHuman-1 is not open source and its
online services include super-resolution operations, there is a natural visual advantage in subjective
evaluations. In addition, our effect also inherits some inherent problems of Hunyuanvideo. Therefore,
on FCN and FBN, our indicators have certain deficiencies compared with Omnihuman-1.
4.3
Ablation Study And Discussion
Ablation on Character Image Injection Module.
We subjectively evaluated three Character
Image Injection Modules across four dimensions: Lip Synchronization (LS), Video Quality (VQ),
Identity Preservation (IP), and Motion Diversity (MD). The results in the table 3 indicate that our
method performs better in terms of video dynamics and character consistency.
9

--- Page 10 ---

Table 1: Quantitative comparisons with audio-driven portrait and full-body animation baselines.
Methods
IQA ↑
ASE↑
Sync-C↑
FID↓
FVD↓
CelebV-HQ / HDTF
Sonic
3.60 / 3.86
2.43 / 2.41
5.58 / 5.81
49.28 / 40.50
415.04 / 413.94
EchoMimic
3.39 / 3.64
2.25 / 2.23
3.41 / 4.07
46.74 / 45.38
450.98 / 410.05
EchoMimic-V2
2.75 / 3.36
1.97 / 2.15
4.11 / 3.39
46.37 / 39.73
862.24 / 487.75
Hallo-3
3.57 / 3.77
2.38 / 2.35
4.57 / 4.87
45.69 / 39.07
444.92 / 380.31
Ours
3.70 / 3.99
2.52 / 2.54
4.92 / 5.30
43.42 / 38.01
445.02 / 358.71
Methods
Full-body Test Set
Hallo3
4.34
2.77
5.13
50.12
629.94
Fantasy
4.63
3.02
3.68
58.24
677.67
OmniHuman-1
4.65
2.99
5.34
49.68
719.40
Ours
4.66
3.03
5.56
49.38
650.54
Table 2: User Study results.
Methods
FCN ↑
FBN ↑
IP ↑
LS ↑
Hallo3
2.91
2.59
4.28
3.61
Fantasy
3.43
3.49
4.65
4.21
Omnihuman-1
4.11
4.18
4.79
4.61
Ours
3.91
3.88
4.84
4.65
Table 3: Ablation Study.
Methods
VQ ↑
MD ↑
IP ↑
LS ↑
Token
2.86
3.58
4.402
4.239
Token + Channel
4.4
2.336
4.576
4.43
Token + Add
4.16
4.127
4.28
4.161
Ablation on Audio Emotion Module.
The figure 7(a) evaluates the impact of using the Audio
Emotion Module on the facial emotions of video characters. The results show that if only text is used
to guide the character’s emotions without the Audio Emotion Module, the model cannot effectively
understand or apply the emotions to the character’s face. After injecting the emotion reference image
into the model through the Audio Emotion Module, we find that the model can better transfer the
emotional information from the reference image to the character’s face, which helps us better align
the emotions conveyed by the audio with the character’s facial expressions.
Ablation on Face-Awared Audio Adapter.
The figure 7(b) evaluates the impact of using the
Face-Aware Audio Adapter for audio-driven animation of multiple characters. The results show that
without restricting the region affected by audio using a Face Mask, both characters in the reference
image are influenced by the audio information, causing the model to drive all characters with the
audio. When the Face Mask is applied, we can see that the model drives only one specific character
according to the mask, and as the Face Mask moves, the audio information is applied to the face of
another character, thus enabling audio-driven multiple characters.
5
Conclusion
In this paper, we propose HunyuanVideo-Avatar, an audio-driven human animation method that
achieves both high character consistency and dynamic motion. We introduce a character image
injection module resolves the inherent trade-off between dynamism and consistency by adaptively
balancing these objectives, significantly enhancing the naturalness and diversity of generated videos.
To ensure alignment between the audio’s emotional tone and character expressions, we introduce
the Audio Emotion Module which transfers affective cues from emotion reference images to the
target animation. For multi-character scenarios, our method employs latent-space masking to localize
audio-driven animation to specific face regions, enabling independent control of different characters
through targeted mask modulation. Extensive qualitative and quantitative experiments demonstrate
10

--- Page 11 ---

w/o AEM
w AEM
Ref Image
Emotion 
Ref Image
Prompt
The gril is extremely happy. A 
young girl in traditional Chinese 
attire is writing calligraphy at a 
table filled with books and fruits, 
singing in a vivid way
（a）
w/o FAA
w FAA
（b）
Figure 7: (a) Ablation on Audio Emotion Module. (b)Ablation on Face-Aware Audio Adapter.
that HunyuanVideo-Avatar outperforms existing methods in video dynamism, subject consistency,
lip-sync accuracy, audio-emotion-expression alignment, and multi-character scenarios.
6
Appendix
6.1
More Visualization Results
Figure 8 shows the results of our method in multiple characters scenarios such as crosstalk, singing,
and walking conversations, demonstrating the robustness of our model.
Figure 9 presents visualizations of realistic human images. From this scene, it can be seen that our
model is able to maintain good character consistency while enhancing dynamics, further demonstrat-
ing the effectiveness of our character image injection module.
Figure 10 showcases the generation results of our method applied to characters with diverse styles.
The results show that our method generalizes well across various styles, including LEGO, chinese
painting, anime, and pencil sketch.
Figure 11 demonstrates the precise control of emotions achieved by our method. It can be seen that
our model has a good understanding of emotions such as happiness, sadness, excitement, and anger.
This enables us to generate human animation videos that better align with the emotions conveyed
by the audio, further demonstrating the unique capabilities of our model compared to previous
audio-driven human animation methods.
In summary, compared to previous audio-driven human animation methods [35, 21, 16, 7, 15], our
approach offers more practical features such as multi-character and emotion control audio-driven
human animation. At the same time, it also outperforms previous methods in terms of character
consistency and video dynamics. These advancements highlight the state-of-the-art performance and
innovative design of our model.
6.2
Limitations and Societal Impacts
Limitations. Firstly, our current approach relies on emotion reference images to drive the character’s
emotions, rather than allowing the model to infer and generate emotions directly from the audio. This
leads to two main issues: (1) increased complexity for users during operation, and (2) the inability
to reflect dynamic emotional changes within the video. Since each reference image corresponds
to only one emotion, multiple emotions in a single audio segment may result in generation errors.
Therefore, exploring methods to directly extract emotions from audio and generate corresponding
emotional character videos is a promising direction for future research. Secondly, we currently
11

--- Page 12 ---

use HunyuanVideo-13B [17] as our base model, while FantasyTalking [35] employs Wan2.1 [32].
Regardless of the base model, the inference process is time-consuming. For instance, generating a
10s video at 720×1216 resolution (with 50 inference steps) takes approximately 60 minutes, which is
far from meeting the requirements of real-time applications. Thus, improving the model’s generation
speed to achieve real-time performance is one of our key future objectives. This will facilitate the
application of our model in scenarios with higher real-time demands, such as live streaming and
interactive real-time applications. Finally, exploring interactive human animation capable of real-time
feedback is a promising research direction. This is expected to further expand the application of our
method for users. This direction requires our model not only to possess strong content generation
capabilities but also to have a solid understanding and contextual awareness, enabling fast and
contextually appropriate responses to users.
Societal Impacts. Real-time interactive digital humans [1] have become a major focus in the fields of
artificial intelligence. However, their development has not yet reached its full potential due to several
technical limitations. On one hand, current generative models still struggle to produce diverse and
natural actions and expressions, making it difficult to achieve truly lifelike interactions. On the other
hand, many high-performance models are extremely large in terms of parameter count, resulting
in slow inference speeds that cannot meet the demands of real-time generation. These challenges
significantly hinder the practical deployment of interactive digital humans.
7
Contributors
• Project Leaders: Qinglin Lu, Qin Lin, Yuan Zhou
• Core Contributors: Yi Chen, Sen Liang, Zixiang Zhou, Ziyao Huang,
Yifeng Ma, Junshu Tang
• Contributors: Zhentao Yu, Zhengguang Zhou, Teng Hu, Zhiyao Sun, Yubin
Zeng, Junxin Huang, Zhaokang Chen, Bin Wu, Xu Chen, Junwei Zhu,
Chengjie Wang, Yuang Zhang, Junqi Cheng, Jiaxi Gu, Fangyuan Zou
12

--- Page 13 ---

Figure 8: More visualizations on multi-character audio-driven human animation.
13

--- Page 14 ---

Ref Image
Output Video
Figure 9: More visualizations on realistic scenarios.
14

--- Page 15 ---

Ref Image
Output Video
Figure 10: More visualizations on diverse character styles
15

--- Page 16 ---

Emotion Happy
Emotion Angry
Emotion Sad
Emotion Excited
Figure 11: More visualizations on emotion control.
16

--- Page 17 ---

References
[1] T. Ao. Body of her: A preliminary study on end-to-end humanoid agent. arXiv
preprint arXiv:2408.02879, 2024.
[2] O. Bar-Tal, H. Chefer, O. Tov, C. Herrmann, R. Paiss, S. Zada, A. Ephrat,
J. Hur, Y. Li, T. Michaeli, et al. Lumiere: A space-time diffusion model for
video generation. arXiv preprint arXiv:2401.12945, 2024.
[3] A. Blattmann, T. Dockhorn, S. Kulal, D. Mendelevitch, M. Kilian, D. Lorenz,
Y. Levi, Z. English, V. Voleti, A. Letts, et al. Stable video diffusion: Scaling la-
tent video diffusion models to large datasets. arXiv preprint arXiv:2311.15127,
2023.
[4] A. Blattmann, R. Rombach, H. Ling, T. Dockhorn, S. W. Kim, S. Fidler, and
K. Kreis. Align your latents: High-resolution video synthesis with latent
diffusion models. In Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition, pages 22563–22575, 2023.
[5] T. Brooks, J. Hellsten, M. Aittala, T.-C. Wang, T. Aila, J. Lehtinen, M.-Y. Liu,
A. Efros, and T. Karras. Generating long videos of dynamic scenes. Advances
in Neural Information Processing Systems, 35:31769–31781, 2022.
[6] J. S. Chung and A. Zisserman. Out of time: automated lip sync in the wild.
In Computer Vision–ACCV 2016 Workshops: ACCV 2016 International Work-
shops, Taipei, Taiwan, November 20-24, 2016, Revised Selected Papers, Part II
13, pages 251–263. Springer, 2017.
[7] J. Cui, H. Li, Y. Zhan, H. Shang, K. Cheng, Y. Ma, S. Mu, H. Zhou, J. Wang,
and S. Zhu. Hallo3: Highly dynamic and realistic portrait image animation
with diffusion transformer networks. arXiv preprint arXiv:2412.00733, 2024.
[8] P. Esser, S. Kulal, A. Blattmann, R. Entezari, J. Müller, H. Saini, Y. Levi,
D. Lorenz, A. Sauer, F. Boesel, et al. Scaling rectified flow transformers for
high-resolution image synthesis. In Forty-first international conference on
machine learning, 2024.
[9] Y. Guo, C. Yang, A. Rao, Z. Liang, Y. Wang, Y. Qiao, M. Agrawala, D. Lin,
and B. Dai. Animatediff: Animate your personalized text-to-image diffusion
models without specific tuning. arXiv preprint arXiv:2307.04725, 2023.
[10] A. Gupta, L. Yu, K. Sohn, X. Gu, M. Hahn, L. Fei-Fei, I. Essa, L. Jiang,
and J. Lezama. Photorealistic video generation with diffusion models. arXiv
preprint arXiv:2312.06662, 2023.
[11] M. Heusel, H. Ramsauer, T. Unterthiner, B. Nessler, and S. Hochreiter. Gans
trained by a two time-scale update rule converge to a local nash equilibrium.
Advances in neural information processing systems, 30, 2017.
[12] J. Ho, T. Salimans, A. Gritsenko, W. Chan, M. Norouzi, and D. J. Fleet. Video
diffusion models. Advances in Neural Information Processing Systems, 35:
8633–8646, 2022.
17

--- Page 18 ---

[13] S. Hogue, C. Zhang, H. Daruger, Y. Tian, and X. Guo. Diffted: One-shot
audio-driven ted talk video generation with diffusion-based co-speech gestures.
In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 1922–1931, 2024.
[14] Z. Huang, Y. He, J. Yu, F. Zhang, C. Si, Y. Jiang, Y. Zhang, T. Wu, Q. Jin,
N. Chanpaisit, et al. Vbench: Comprehensive benchmark suite for video
generative models. In Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition, pages 21807–21818, 2024.
[15] X. Ji, X. Hu, Z. Xu, J. Zhu, C. Lin, Q. He, J. Zhang, D. Luo, Y. Chen, Q. Lin,
et al. Sonic: Shifting focus to global audio perception in portrait animation.
arXiv preprint arXiv:2411.16331, 2024.
[16] J. Jiang, C. Liang, J. Yang, G. Lin, T. Zhong, and Y. Zheng. Loopy: Taming
audio-driven portrait avatar with long-term motion dependency. arXiv preprint
arXiv:2409.02634, 2024.
[17] W. Kong, Q. Tian, Z. Zhang, R. Min, Z. Dai, J. Zhou, J. Xiong, X. Li, B. Wu,
J. Zhang, et al.
Hunyuanvideo: A systematic framework for large video
generative models. arXiv preprint arXiv:2412.03603, 2024.
[18] C. Li, C. Zhang, W. Xu, J. Xie, W. Feng, B. Peng, and W. Xing.
La-
tentsync: Audio conditioned latent diffusion models for lip sync. arXiv preprint
arXiv:2412.09262, 2024.
[19] Y. Li, M. Min, D. Shen, D. Carlson, and L. Carin. Video generation from text.
In Proceedings of the AAAI conference on artificial intelligence, volume 32,
2018.
[20] G. Lin, J. Jiang, C. Liang, T. Zhong, J. Yang, and Y. Zheng. Cyberhost: Taming
audio-driven avatar diffusion model with region codebook attention. arXiv
preprint arXiv:2409.01876, 2024.
[21] G. Lin, J. Jiang, J. Yang, Z. Zheng, and C. Liang. Omnihuman-1: Rethinking the
scaling-up of one-stage conditioned human animation models. arXiv preprint
arXiv:2502.01061, 2025.
[22] S. Lin, X. Xia, Y. Ren, C. Yang, X. Xiao, and L. Jiang. Diffusion adversarial
post-training for one-step video generation. arXiv preprint arXiv:2501.08316,
2025.
[23] Y. Lipman, R. T. Chen, H. Ben-Hamu, M. Nickel, and M. Le. Flow matching
for generative modeling. arXiv preprint arXiv:2210.02747, 2022.
[24] R. Meng, X. Zhang, Y. Li, and C. Ma. Echomimicv2: Towards striking,
simplified, and semi-body human animation. arXiv preprint arXiv:2411.10061,
2024.
[25] A. Radford, J. W. Kim, T. Xu, G. Brockman, C. McLeavey, and I. Sutskever.
Robust speech recognition via large-scale weak supervision. In International
conference on machine learning, pages 28492–28518. PMLR, 2023.
18

--- Page 19 ---

[26] X. Ren, A. Lattas, B. Gecer, J. Deng, C. Ma, and X. Yang. Facial geometric
detail recovery via implicit representation. In 2023 IEEE 17th International
Conference on Automatic Face and Gesture Recognition (FG), 2023.
[27] U. Singer, A. Polyak, T. Hayes, X. Yin, J. An, S. Zhang, Q. Hu, H. Yang,
O. Ashual, O. Gafni, et al. Make-a-video: Text-to-video generation without
text-video data. arXiv preprint arXiv:2209.14792, 2022.
[28] J. Su, M. Ahmed, Y. Lu, S. Pan, W. Bo, and Y. Liu. Roformer: Enhanced
transformer with rotary position embedding. Neurocomputing, 568:127063,
2024.
[29] Z. Tan, S. Liu, X. Yang, Q. Xue, and X. Wang. Ominicontrol: Minimal and
universal control for diffusion transformer. arXiv preprint arXiv:2411.15098,
3, 2024.
[30] T. Unterthiner, S. van Steenkiste, K. Kurach, R. Marinier, M. Michalski, and
S. Gelly. Fvd: A new metric for video generation.
[31] R. Villegas, M. Babaeizadeh, P.-J. Kindermans, H. Moraldo, H. Zhang, M. T.
Saffar, S. Castro, J. Kunze, and D. Erhan. Phenaki: Variable length video
generation from open domain textual descriptions. In International Conference
on Learning Representations, 2022.
[32] A. Wang, B. Ai, B. Wen, C. Mao, C.-W. Xie, D. Chen, F. Yu, H. Zhao, J. Yang,
J. Zeng, et al. Wan: Open and advanced large-scale video generative models.
arXiv preprint arXiv:2503.20314, 2025.
[33] C. Wang, K. Tian, J. Zhang, Y. Guan, F. Luo, F. Shen, Z. Jiang, Q. Gu, X. Han,
and W. Yang. V-express: Conditional dropout for progressive training of
portrait video generation. arXiv preprint arXiv:2406.02511, 2024.
[34] J. Wang, H. Yuan, D. Chen, Y. Zhang, X. Wang, and S. Zhang. Modelscope
text-to-video technical report. arXiv preprint arXiv:2308.06571, 2023.
[35] M. Wang, Q. Wang, F. Jiang, Y. Fan, Y. Zhang, Y. Qi, K. Zhao, and M. Xu. Fan-
tasytalking: Realistic talking portrait generation via coherent motion synthesis.
arXiv preprint arXiv:2504.04842, 2025.
[36] Q. Wang, Y. Shi, J. Ou, R. Chen, K. Lin, J. Wang, B. Jiang, H. Yang, M. Zheng,
X. Tao, et al.
Koala-36m: A large-scale video dataset improving consis-
tency between fine-grained conditions and video content.
arXiv preprint
arXiv:2410.08260, 2024.
[37] Y. Wang, P. Bilinski, F. Bremond, and A. Dantcheva. Imaginator: Conditional
spatio-temporal gan for video generation. In Proceedings of the IEEE/CVF
Winter Conference on Applications of Computer Vision, pages 1160–1169,
2020.
[38] H. Wu, Z. Zhang, W. Zhang, C. Chen, L. Liao, C. Li, Y. Gao, A. Wang,
E. Zhang, W. Sun, et al. Q-align: Teaching lmms for visual scoring via discrete
text-defined levels. arXiv preprint arXiv:2312.17090, 2023.
19

--- Page 20 ---

[39] M. Xu, H. Li, Q. Su, H. Shang, L. Zhang, C. Liu, J. Wang, L. Van Gool, Y. Yao,
and S. Zhu. Hallo: Hierarchical audio-driven visual synthesis for portrait image
animation. arXiv preprint arXiv:2406.08801, 2024.
[40] W. Zhang, X. Cun, X. Wang, Y. Zhang, X. Shen, Y. Guo, Y. Shan, and F. Wang.
Sadtalker: Learning realistic 3d motion coefficients for stylized audio-driven
single image talking face animation. In Proceedings of the IEEE/CVF Confer-
ence on Computer Vision and Pattern Recognition, pages 8652–8661, 2023.
[41] Z. Zhang, L. Li, Y. Ding, and C. Fan. Flow-guided one-shot talking face
generation with a high-resolution audio-visual dataset. In Proceedings of
the IEEE/CVF conference on computer vision and pattern recognition, pages
3661–3670, 2021.
[42] D. Zhou, W. Wang, H. Yan, W. Lv, Y. Zhu, and J. Feng. Magicvideo: Efficient
video generation with latent diffusion models. arXiv preprint arXiv:2211.11018,
2022.
[43] Y. Zhou, Q. Wang, Y. Cai, and H. Yang. Allegro: Open the black box of
commercial-level video generation model. arXiv preprint arXiv:2410.15458,
2024.
[44] H. Zhu, W. Wu, W. Zhu, L. Jiang, S. Tang, L. Zhang, Z. Liu, and C. C. Loy.
Celebv-hq: A large-scale video facial attributes dataset. In European conference
on computer vision, pages 650–667. Springer, 2022.
20

```
