---
title: "VidHalluc - PDF Extract"
source_pdf: "2025-Liu-VidHalluc.pdf"
pages: 22
extracted_at: "2026-01-24T16:38:30.917410"
---

# PDF Extract: VidHalluc

**Source PDF:** 2025-Liu-VidHalluc.pdf
**Total Pages:** 22

---

## Content

```
--- Page 1 ---

VIDHALLUC: Evaluating Temporal Hallucinations
in Multimodal Large Language Models for Video Understanding
Chaoyu Li
Eun Woo Im
Pooyan Fazli
Arizona State University
{chaoyuli, eunwooim, pooyan}@asu.edu
Abstract
Multimodal large language models (MLLMs) have recently
shown significant advancements in video understanding,
excelling in content reasoning and instruction-following
tasks. However, hallucination, where models generate in-
accurate or misleading content, remains underexplored in
the video domain. Building on the observation that MLLM
visual encoders often fail to distinguish visually different
yet semantically similar video pairs, we introduce VIDHAL-
LUC, the largest benchmark designed to examine halluci-
nations in MLLMs for video understanding. It consists of
5,002 videos, paired to highlight cases prone to halluci-
nations. VIDHALLUC assesses hallucinations across three
critical dimensions: (1) action, (2) temporal sequence, and
(3) scene transition. Comprehensive testing shows that most
MLLMs are vulnerable to hallucinations across these dimen-
sions. Furthermore, we propose DINO-HEAL, a training-
free method that reduces hallucinations by incorporating
spatial saliency from DINOv2 to reweight visual features
during inference. Our results show that DINO-HEAL con-
sistently improves performance on VIDHALLUC, achieving
an average improvement of 3.02% in mitigating hallucina-
tions across all tasks. Both the VIDHALLUC benchmark and
DINO-HEAL code are available at https://people-
robots.github.io/vidhalluc.
1. Introduction
The rapid advancement of multimodal large language models
(MLLMs) [32, 35, 54] has led to significant improvements
in video understanding, particularly in semantic reasoning
and instruction-following [52]. Despite these improvements,
MLLMs tend to generate hallucinations, producing plausible
but factually incorrect information [26], raising concerns
about their reliability in practical applications. To better
understand and quantify these limitations, several bench-
marks [18, 30, 58] and mitigation strategies [66, 73] have
been developed to systematically evaluate hallucinations in
MLLMs. These benchmarks curate fine-grained question-
Q1) Is the prominent action in the video
playing the piano?
Q2) Is the prominent action in the video
playing drums?
Chat-UniVi: Yes, the prominent action
in the video is playing the piano. 
Chat-UniVi: Yes, the prominent action in
the video is the person playing the drums. ✘
Video-LLaMA2: Yes. 
Video-LLaMA2: Yes. ✘
GT: Yes. 
GT: No. 
Video-ChatGPT: No. ✘
Video-ChatGPT: Yes, playing drums is
the prominent action in the video. ✘
Q1) Is the prominent action in the video
playing the piano?
Q2) Is the prominent action in the video
playing drums?
Chat-UniVi: Yes, the prominent action in
the video is the man playing the drums. 
Chat-UniVi: Yes, the prominent action
in the video is playing the piano. ✘ 
GT: No. 
GT: Yes. 
Video-LLaMA2: Yes. 
Video-LLaMA2: Yes. ✘
Video-ChatGPT: Yes, playing drums is
the prominent action in the video.
Video-ChatGPT: Yes. ✘
Video Pair
Figure 1. An example of a video pair showing action hallucination
in VIDHALLUC. Adversarial questions, which refer to actions
in the other video of the pair, show that MLLMs are prone to
hallucinations when input videos have high semantic but low visual
similarity. None of the models accurately identify the prominent
actions in this pair.
answer (QA) pairs designed to trigger hallucinations, of-
ten created using either GPT-4V [6, 64] or human annota-
tors [40]. However, these benchmarks come with several
limitations. First, the datasets are typically small in scale,
containing fewer than 1,000 videos and 2,000 QA pairs. This
limited scale is due to the time and cost involved in gener-
ating high-quality QA pairs, making the process inefficient.
Second, the primary focus of the existing benchmarks is
on hallucinations in static elements of videos [8, 37], such
as objects [30, 49], their attributes [51, 57], and spatial re-
lationships [19]. This limits the benchmark’s efficacy in
evaluating dynamic and temporal content in videos. Third,
the benchmarks are constructed with limited question types
(e.g., binary QA only), constraining the assessment of the
model’s understanding of dynamic aspects, such as temporal
scene transitions, inherent to video content.
1
arXiv:2412.03735v2  [cs.CV]  31 Mar 2025

--- Page 2 ---

To address these gaps, we introduce VIDHALLUC, the
largest benchmark for evaluating hallucinations in video un-
derstanding, comprising 5,002 videos and 9,295 QA pairs.
To curate the benchmark, we build on prior work [55] to
develop an automated data collection pipeline that gener-
ates potential hallucination video pairs based on semantic
similarity and visual differences. Moreover, while previous
benchmarks often focus on static tasks, VIDHALLUC specif-
ically targets dynamic elements of videos that cause hal-
lucinations, namely, action, temporal sequence, and scene
transition hallucinations.
On the other hand, efforts have been made to miti-
gate MLLM hallucinations in video understanding. These
methods include constructing high-quality instruction-
tuning datasets [34], enhancing input resolution [36], and
leveraging reinforcement learning from human feedback
(RLHF) [51, 67, 73, 75]. However, these data-centric opti-
mization approaches still require fine-tuning, which incurs
significant computational costs and necessitates creating ad-
ditional datasets. As shown in Figure 1, we observe that
current MLLMs are vulnerable to hallucinations when they
encounter semantically similar videos. We attribute these
hallucinations to the inductive bias inherent in the visual en-
coder (e.g., the CLIP series), which emphasizes the discrimi-
nation of contextual scenes due to its image-text contrastive
learning. This creates a discrepancy between the encoder’s
provision of semantic information about the video and the
language model’s need for both semantic and vision-only
unimodal representations [55].
To address this issue, we propose DINO-HEAL, a novel,
training-free algorithm designed to mitigate MLLM hallu-
cinations in video understanding by enhancing the visual
encoder’s focus on salient spatial regions during inference.
DINO-HEAL applies to any CLIP-series vision encoder. To
reduce reliance on the CLIP series and better encode spatially
important features, DINO-HEAL uses saliency maps from
DINOv2 [44] to reweight frame features, highlighting key
regions. This approach enables models to achieve substan-
tial accuracy gains, such as +5.01% for Video-LLaVA [32]
and +4.77% for Video-ChatGPT [39] in action hallucina-
tion, as well as notable improvements in temporal sequence
hallucination, with Video-ChatGPT and VideoLLaMA2 [9]
achieving gains of +11.67% and +18.83%, respectively.
In summary, our main contributions are as follows:
• We introduce VIDHALLUC, the largest benchmark for as-
sessing hallucinations in MLLMs for video understanding,
designed to evaluate action, temporal sequence, and scene
transition hallucinations.
• We develop a training-free algorithm, DINO-HEAL, to
enhance the visual encoder’s focus on critical regions and
improve the model’s robustness against hallucinations.
• We conduct extensive experiments on VIDHALLUC with
ten state-of-the-art models and provide a comprehen-
sive analysis of the benchmark results. Additionally, we
demonstrate the effectiveness of DINO-HEAL, achieving
an average gain of 3.02% across all hallucination cate-
gories and five models.
2. Related Works
2.1. Multimodal Large Language Models
Building on the success of large language models (LLMs) [3,
11, 13, 14, 45, 47, 56, 59], researchers have enhanced these
models with vision capabilities, leading to the development
of MLLMs [12, 27, 77]. This is achieved by processing
images as tokens concatenated with text tokens through
cross-attention [2] or by directly aligning visual features
with nonlinear projections [24, 35]. Recent advancements
have led to numerous MLLMs designed specifically for
video understanding [23, 33], which build upon image ap-
proaches to address the sequential and dynamic nature of
video content. For example, Video-ChatGPT [39] employs
temporal aggregation techniques to integrate information
across frames, Video-LLaVA [32] uses time-sensitive at-
tention mechanisms to manage frame dependencies, and
LLaVA-NeXT-Video [72] introduces a linear scaling ap-
proach to process longer video sequences, effectively captur-
ing extended temporal dependencies.
Most MLLMs use CLIP-based visual encoders [10, 36,
41, 46, 50, 68] for robust visual-text alignment. However,
these encoders, shaped by image-text contrastive learning,
struggle with dynamic scenes and temporal relationships
in videos [62]. To assess and highlight these biases, VID-
HALLUC leverages CLIP/SigLIP and DINOv2 [44], trained
solely on image data to provide visual features, to curate
video pairs that may cause confusion and hallucinations,
offering a rigorous evaluation framework for MLLMs.
2.2. Hallucination in MLLMs
Hallucination in MLLMs occurs when the model generates
inaccurate or entirely fabricated responses, failing to accu-
rately reflect the input data. To mitigate this issue in image-
based tasks, Woodpecker [65] uses post-hoc corrections
through additional visual cues, while LRV-Instruction [34]
and HalluciDoctor [66] offer balanced instruction-tuning
datasets to reduce hallucinations. As MLLMs extend into
video understanding tasks, new challenges arise in handling
temporal inconsistencies. To tackle this, Volcano[25] uses
a critique-revise-decide framework for self-correction, and
Vript [64] enhances alignment by incorporating transcribed
voice-overs, enriching multimodal representations. These
methods showcase tailored strategies for minimizing halluci-
nations across different modalities in MLLMs.
While most methods require retraining or fine-tuning the
MLLM to reduce hallucinations, our DINO-HEAL approach
can be applied directly during inference without additional
2

--- Page 3 ---

Benchmark
# of Ques. / # of Videos
Binary QA
MCQ
Open-Ended Ques.
Sorting Ques.
Control Pairs
Adversarial
HallusionBench [18]
1129 / 346
✓
✓
×
×
✓
✓
VideoHallucer [58]
1,800 / 948
✓
×
×
×
×
✓
Vript-HAL [64]
122 / 122
×
×
✓
×
×
×
EventHallusion [71]
- / 400
✓
×
✓
×
×
×
VIDHALLUC (Ours)
9,295 / 5,002
✓
✓
✓
✓
✓
✓
Table 1. Comparison of VIDHALLUC with recent hallucination benchmarks in video understanding. VIDHALLUC is the largest benchmark
for evaluating hallucinations, supporting diverse question formats, including binary QA, MCQ, open-ended, and sorting questions, with
control pairs and adversarial evaluation to enhance robustness.
training, offering an efficient solution for mitigating halluci-
nations in resource-constrained scenarios.
2.3. MLLM Benchmarks for Video Understanding
As MLLMs continue to advance, conducting quantitative
evaluations remains essential. Numerous efforts [5, 29, 31,
38, 43, 64] have been undertaken to assess various aspects of
MLLMs in video understanding, encompassing tasks such
as video reasoning [31], text-to-video retrieval [29], video
captioning [5], and hallucination [64]. These benchmarks
assess models’ capabilities in understanding and generating
language from video content. For example, MVBench [28]
provides an extensive evaluation of temporal understanding
in video-language models, encompassing 20 challenging
video tasks that require dynamic analysis beyond individual
frames. Video-MME [15] offers a comprehensive assessment
of MLLMs’ video analysis performance, covering diverse
types of videos, varying durations, and multiple data modali-
ties. In long-form video understanding, benchmarks such as
HourVideo [4] and LongVideoBench [60] focus on event or-
dering. In the context of hallucination, HallusionBench [18]
reverses the frames in four-frame video clips and prompts the
model to determine whether the events in the original cap-
tions align with those in the reversed video. Similarly, Video-
Hallucer [58] uses extended videos with multiple events to
query the model on the correct sequence of these events.
However, these hallucination benchmarks have limitations in
scale, providing no more than 1,000 videos, which restricts
their ability to comprehensively evaluate hallucinations.
3. VIDHALLUC Benchmark
3.1. Data Collection
Unlike other benchmarks for evaluating hallucinations in
video understanding that rely on manually collected videos,
our data collection pipeline is semi-automated (Figure 2). To
create the VIDHALLUC benchmark, we apply this pipeline
to existing video description datasets, including ActivityNet
[20], YouCook2 [74], and VALOR32K [7]. In contrast to
existing approaches, which typically use individual videos,
our method treats video pairs as the primary data units. Be-
low, we outline the key stages of our data collection process,
including filtering for semantic and visual similarity, per-
forming quality checks, conducting human validation, and
generating hallucination-specific questions. For implementa-
tion details, please refer to the Supplementary Material.
Semantic and Visual Similarity Filtering. To identify po-
tential hallucination pairs, we measure semantic similarity
using CLIP/SigLIP and visual similarity with DINOv2. For
semantic similarity, we apply average pooling to the fea-
tures of CLIP/SigLIP, while DINOv2 uses a similar pooling
method to calculate visual similarity. Video pairs scoring
above the semantic threshold λsem with CLIP/SigLIP but
below the visual threshold λvis with DINOv2 are flagged
as hallucination candidates. These pairs highlight cases
where models may over-rely on semantic cues, leading to po-
tential misinterpretations of visually unique content. We
use CLIP/SigLIP and DINOv2 for their complementary
strengths: CLIP/SigLIP, trained on the cosine similarity
between visual and textual projections, captures deep con-
textual relationships and thematic elements, while DINOv2,
trained with a self-supervised objective, focuses on visual
resemblance. This method also tests the model’s sensitiv-
ity to subtle visual differences that might be overlooked in
single-video evaluations [55]. λsem and λvis are set to 0.9
and 0.6, respectively.
Quality Filtering. After collecting the video pairs, we per-
form additional filtering to ensure dataset quality. First, we
exclude pairs where either video is shorter than one second.
Next, we leverage GPT-4 [1] to align each video with the
actions and scenes described in the original dataset’s anno-
tated captions. Finally, we filter out video pairs that contain
identical extracted actions.
Human Validation of Video Pairs. We recruit four partic-
ipants to conduct a manual review to eliminate pairs with
the following issues: (1) the lack of a clear action in either
video, (2) the presence of multiple actions in either video,
or (3) identical actions in both videos. These rigorous steps
result in a high-quality dataset, which serves as a reliable
benchmark.
Automatic Question Generation. We categorize the bench-
mark into three distinct hallucination types: (1) action hallu-
cination, (2) temporal sequence hallucination, and (3) scene
transition hallucination. For each type, we design specific
question formats to evaluate model performance: binary QA
3

--- Page 4 ---

Scenes
Human Validation
Action 
Hallucination 
Temporal Sequence
Hallucination 
Scene Transition
Hallucination 
 Automatic
Question
Generation
{                         }
Actions
Semantic and Visual Similarity Filtering
Quality Filtering
CLIP/SigLIP
Sim>0.9
Video Clip 1
Video Clip 2
DINOv2
Sim<0.6
GPT-4
Captions
Human Verification
Figure 2. Overview of the VIDHALLUC benchmark construction process. Candidate video pairs are selected based on high semantic
similarity and low visual similarity. GPT-4 is then used to generate action and scene annotations from the captions of each video clip. Human
reviewers manually filter out pairs where GPT-4 annotations were incorrect or where actions/scenes did not align between clips. Finally,
video pairs that pass this filtering process are used to automatically generate three types of hallucination questions: action hallucination,
time-sequence hallucination, and scene-transition hallucination.
and multiple-choice questions (MCQs) for action hallucina-
tion, sorting questions for temporal sequence hallucination,
and open-ended questions for scene transition hallucination.
After the filtering steps, the high-quality video pairs, along
with their corresponding annotations, are further processed
to automatically generate questions tailored to each halluci-
nation type and question format. An example question for
each hallucination type is shown in Figure 3.
Human Verification of QAs. We recruit nine participants
to verify and refine the entire dataset. For ACH, they check
whether the action described in the question matches the
video and correct any inaccuracies. For TSH, they ensure
that the action order in the answer aligns with the video,
making revisions where necessary. For STH, they verify
that the scene described in the answer corresponds to the
video and adjust any mismatches. Following verification,
939 ACH, 68 TSH, and 38 STH questions are modified,
resulting in an accuracy of 88.76% for the automatically
generated QAs.
3.2. Action Hallucination
Action hallucination (ACH) occurs when a model identifies
actions in a video that are either non-existent or significantly
different from the actual actions. This typically arises when
the model misinterprets visual cues or overgeneralizes, lead-
ing to inaccurate conclusions about the video’s content. In
VIDHALLUC, we evaluate the performance of MLLMs in de-
tecting action hallucinations using two methods: binary QA
and MCQs. The MCQs test the model’s basic understand-
ing of actions, assessing its ability to identify them without
extra context. In contrast, binary QA evaluates the model’s
susceptibility to hallucinations, especially when confronted
with leading or suggestive questions.
For the binary QA, we use a question format such as “Is
the prominent action in the video {action}?”. Each video
pair involves two distinct actions. For instance, we first ask
the question with Video 1, then with Video 2. The model
should answer “Yes” for the video containing the action and
“No” for the video without it. A correct response requires the
model to answer both questions correctly. We evaluate the
model’s performance using accuracy, as defined in formula 1,
where Ncorrect is the number of correctly answered questions
and Ntotal is the total number of questions.
  \text { Accuracy} = N_{\text {correct}} / N_{\text {total}}. \label {eq:accuracy} 
(1)
For MCQs, we use a format such as “What is the prominent
action in the video?”. Each question has four answer choices,
with only one correct answer representing the action occur-
ring in the video. One incorrect option corresponds to the
action in the other video in the pair, while the remaining two
options are generated using GPT-4o [21]. By providing a
frame from the video, we ask GPT-4o to generate plausible
actions that could occur in the same scene, but distinct from
the correct action. The model must select the correct ac-
tion from the four options. Accuracy remains the evaluation
metric, calculated in the same manner as in Equation 1.
3.3. Temporal Sequence Hallucination
Temporal sequence hallucination (TSH) occurs when a
model misinterprets the order or timing of events in a video,
confusing the sequence in which actions or scenes unfold. In
VIDHALLUC, model performance is evaluated on TSH by
testing its ability to identify the correct sequence of events.
To do this, we first select two video clips from a pair that ap-
pear consecutively in the original video. These clips are then
concatenated in their original chronological order to form
a longer video segment. The model’s task is to determine
the correct sequence of actions within this concatenated seg-
ment. We use accuracy, calculated as in Equation 1, as the
evaluation metric to assess how well the model interprets the
temporal relationships between the consecutive events.
4

--- Page 5 ---

Figure 3. Examples of three hallucination types in the VIDHAL-
LUC benchmark: (1) action hallucination, where the model detects
actions in a video that significantly differ from the actual actions;
(2) temporal sequence hallucination, where the model fails to repre-
sent the correct temporal order of events in a video; and (3) scene
transition hallucination, where the model inaccurately describes
transitions between distinct scenes within a video.
3.4. Scene Transition Hallucination
Scene transition hallucination (STH) occurs when a model
fails to detect or describe transitions between different scenes
in a video. This can result in blending elements from differ-
ent scenes or failing to recognize the start of a new scene,
leading to inaccurate descriptions. We design evaluation
tasks to assess MLLMs’ ability to detect scene transitions
accurately. To create these tasks, we first filter video pairs
to identify those with distinct scenes, using captions from
the original datasets to detect scene differences. After filter-
ing, each video pair is concatenated in both possible orders
to produce two unique long video clips. Additionally, an
equal number of video pairs with no scene changes are col-
lected to ensure dataset balance. For video clips containing
a scene transition, the ground truth labels indicate “Yes” for
scene change and describe the transition as “from [Scene1]
to [Scene2]”. For clips without a scene change, the ground
truth labels indicate “No”.
The model is tasked with determining if a scene change
occurs in each concatenated video segment and, if so, identi-
fying the specific transition. We evaluate the model’s perfor-
mance based on two criteria: (1) scene change classification,
which assesses whether the model correctly identifies a scene
change, and (2) scene transition description, which mea-
sures the model’s ability to describe the transition from one
scene to another accurately. For the scene change classifica-
tion task, we calculate the Matthews correlation coefficient
(MCC) between the model’s predictions and the ground truth
labels, as defined in Equation 14:
  \ f rac  {n_ { 11}
 
\tim e s n_{10}  - n_{01}  \times n _ {00}
}{\sqrt {(n_{11} + n_{01}) (n_{11} + n_{00})(n_{10} + n_{01})(n_{10} + n_{00})}}, \label {eq:mcc} (2)
where A ∈{0 (False), 1 (True)}, P ∈{0 (Negative), 1 (Posi-
tive)}, and nAP denote actual condition, predicted condition,
and non-negative counts, respectively. To adjust MCC to
range between 0 and 1 and to further penalize models that
consistently answer only “Yes” or only “No”, we apply the
transformation in Equation 15 to obtain the classification
score Scorecls:
  \text {
Scor e }
_
\t
ext {cls} = \left ( \frac {\text {MCC} + 1}{2} \right )^2. \label {eq:cls_score} 
(3)
The description task evaluates the model’s ability to accu-
rately recognize and describe scene information. To assess
this, we extract scene descriptions from both the model’s
output and the ground truth, formatting them for direct com-
parison. We then calculate the cosine similarity S between
the SimCSE [16] embeddings of the corresponding scenes.
Based on this similarity measure, each scene description is
assigned a score using Equation 16:
  \text { S
c
or
e} _ { \text 
{desc}} = \beg
in {cases} \hf i
ll  0 , & \t
ext {if } S \leq \text {THR}_{\text {low}} \\ \frac {\sigma (S) - \sigma (\text {THR}_{\text {low}})}{\sigma (1) - \sigma (\text {THR}_{\text {low}})}, & \text {if } S > \text {THR}_{\text {low}} \end {cases}, \label {eq:desc_score} 
(4)
where S is the cosine similarity between the SimCSE [16]
embeddings of the corresponding scenes,  \text {THR}_{\text {low}} is the low-
est threshold we set to start giving a score, σ represents the
Sigmoid function. The total description score is the average
of the scores for the “from” and “to” scenes.
Finally, we calculate the overall evaluation score as a
weighted sum of the classification score and the normalized
description score as below:
  \text {Sco r e } _{\text { ov e ra l l}} = \alpha \times \text {Score}_{\text {cls}} + (1 - \alpha ) \times \text {Score}_{\text {desc}}. \label {eq:overall_score} 
(5)
5

--- Page 6 ---

[0, 10)s
[10, 20)s
[20, 30)s
[30, 40)s
[40, 50)s
[50, 60)s
[60, 80)s
[80, 120)s
[120, 170)s
[170, 220)s
Duration (seconds)
0
200
400
600
800
1000
1200
1400
1600
Number of Videos
Figure 4. The distribution of video durations in the VIDHAL-
LUC benchmark.
3.5. Dataset Statistics
Table 2 summarizes the statistics for VIDHALLUC. The
dataset consists of 5,002 unique videos in total, with 3,957
videos for ACH, 600 for TSH, and 445 for STH. VIDHAL-
LUC also includes 9,295 QA pairs, with 8,250 questions for
ACH, 600 for TSH, and 445 for STH. The average video
length varies by hallucination type: ACH videos have an
average length of approximately 21.79 seconds, TSH videos
average around 41.19 seconds, and STH videos average
28.72 seconds. The overall average length across the bench-
mark is 24.70 seconds. Figure 4 illustrates the distribution of
video durations, showing a peak in the 10–20 second range.
These statistics highlight the diversity and scale of VIDHAL-
LUC, establishing it as a valuable resource for evaluating
video-based hallucinations.
Statistics
ACH
TSH
STH
Total
# of Videos
3,957
600
445
5,002
# of Questions
8,250
600
445
9,295
Average Duration (s)
21.79
41.19
28.72
24.70
Table 2. VIDHALLUC statistics.
4. DINO-HEAL
We introduce DINO-HEAL, a training-free method that mit-
igates hallucinations by using saliency maps from DINOv2
to reweight features from the frozen visual encoder, em-
phasizing key spatial regions. DINO-HEAL requires no
architectural modifications or additional training.
4.1. DINOv2 Saliency Map Extraction
For each input frame, the method processes it through the
DINOv2 model to extract attention weights from the last
layer and the h-th head, denoted as  A_{
\text { DINOv2}}^{(h)} \in \mathrm {R}^{L \times L} , where
L is the sequence length (number of tokens), including the
[CLS] token. We then compute the average attention across
all heads:
  A_{\t e x
t
 
{
DIN
Ov2}
} = \frac {1}{H} \sum _{h=1}^{H} A_{\text {DINOv2}}^{(h)}, \label {eq:avg_attention_weights} 
(6)
V
V
V
V
V
V
T
T
T
T
T
Large Language Model
Visual
Encoder
What is the primary action in the video?
 A. Skateboarding on the road
 B. Windsurfing
 C. Swimming in the ocean
 D. Beach volleyball
Saliency Map
The action is B.
DINIOv2
Video
Figure 5. DINO-HEAL pipeline. Since DINOv2 effectively cap-
tures salient regions in the input video, we leverage it to guide the
reweighting of the attention given to different spatial regions within
the feature from the visual encoder.
where H is the total number of attention heads. Then, we
extract the attention values of the [CLS] token over all spatial
tokens, excluding itself, as:
  S_{\t e xt {DINOv2}}  =  A _{\text {DINOv2}}[\text {CLS}, 1:L-1], \label {eq:saliency_map_extraction} 
(7)
where SDINOv2 represents the saliency scores derived from
DINOv2 for spatial tokens. We compute the saliency score
for each spatial token by summing the attention weights
across the query dimension:
  S_{\t e xt {DINO
v2}} =  A_{\text {DINOv2}}^{\text {spatial}} \in \mathbb {R}^{L-1} . 
(8)
This results in a saliency map SDINOv2 that represents the
importance of each spatial token in the frame.
4.2. Alignment and Upsampling of Saliency Maps
To align the DINOv2 saliency map with the original visual
features, we reshape SDINOv2 into a 2D grid corresponding
to the spatial dimensions of the DINOv2 tokens:
  S_{
\text { DINOv2}}^{\text {grid}} = \text {Reshape}(S_{\text {DINOv2}}, H_{\text {DINOv2}}, W_{\text {DINOv2}}), 
(9)
where HDINOv2 and WDINOv2 are the height and width of the
DINOv2 token grid. We then upsample the saliency map to
match the spatial dimensions of the visual features from the
original visual encoder:
  S_{\text
 {DINO
v 2}}^{\text {upsam
pled}} = \text { Interpolate}(S_{\text {DINOv2}}^{\text {grid}}, (H_{\text {visual}}, W_{\text {visual}})), 
(10)
where Hvisual and Wvisual denote the height and width of the
visual feature grid, corresponding to the spatial dimensions
of the features extracted by the original visual encoder. We
then flatten the upsampled saliency map back into a vector
and normalize it with the sigmoid function:
  S_{\text 
{DINOv
2 }}^{\text {normalize
d}} = \ s igma (\text {Flatten}(S_{\text {DINOv2}}^{\text {upsampled}}) \in \mathbb {R}^{L_{\text {visual}}}). 
(11)
6

--- Page 7 ---

Models
LLM Params
Encoder
Frame
Accuracy on ACH
Accuracy on TSH↑
Score on STH↑
Binary QA↑
MCQ↑
Video-ChatGPT [39]
7B
CLIP ViT-L/14-224
100
9.50
24.58
30.17
7.70
Video-LLaVA [32]
7B
LanguageBind-Video
8
26.84
64.45
27.17
29.60
ShareGPT4Video [6]
8B
CLIP ViT-L/14-336
16
29.96
44.78
49.50
17.83
Chat-UniVi [23]
13B
CLIP ViT-L/14-224
fps=1
23.77
54.79
35.50
29.87
LLaVA-NeXT-Video [72]
34B
CLIP ViT-L/14-336
32
26.60
77.57
21.33
44.40
PLLaVA [63]
13B
CLIP ViT-L/14-336
16
35.30
76.96
16.50
32.44
VideoLLaMA2 [9]
7B
CLIP ViT-L/14-336
16
50.04
83.84
26.17
65.12
VILA1.5 [33]
13B
SigLIPViT-SO-14-384
8
58.46
81.88
63.33
35.03
Gemini-1.5-Pro [53]
-
-
16
75.27
79.25
83.83
63.96
GPT-4o [21]
-
-
16
81.15
90.95
82.00
71.58
Human
-
-
-
95.14
93.29
90.17
87.43
Table 3. Performance comparison of existing MLLMs on VIDHALLUC, covering action hallucination (ACH), temporal sequence hallucination
(TSH), and scene transition hallucination (STH) tasks. For the STH task, we assign a weight of 0.6 to the classification task and 0.4 to the
description task. The numbers in the table represent accuracy percentages (%). Bold numbers denote the best performance, and underlined
numbers indicate the second-best performance.
4.3. Reweighting Visual Features
Finally, we enhance the visual features by reweighting them
with the saliency map:
  F_{\text 
{visua
l }}^{\te x t {reweight
ed}} =
 F_{\text {visual}} \odot S_{\text {DINOv2}}^{\text {normalized}}, 
(12)
where ⊙denotes element-wise multiplication. This adap-
tive reweighting strategy enables DINOv2 to enhance key
visual features by directly focusing on areas highlighted by
the saliency map, thereby mitigating hallucinations while
preserving the original feature representation.
5. Experiments
We evaluate ten state-of-the-art MLLMs on VIDHALLUC, in-
cluding eight open-source and two proprietary models (Sec-
tion 5.1). Our results reveal that most MLLMs exhibit no-
table vulnerabilities on VIDHALLUC. To further evaluate the
quality of VIDHALLUC, we also conduct a human evaluation
of our benchmark. We recruit four participants, each answer-
ing a randomly assigned half of the ACH, TSH, and STH
queries, ensuring that each query is covered by two individu-
als. The questions, answer formats, and evaluation metrics
are identical to those used for the models to ensure fairness.
We then assess the performance of our DINO-HEAL on
VIDHALLUC with five different MLLMs, demonstrating its
effectiveness in enhancing the robustness of these models
against various types of hallucinations (Section 5.2). During
inference, we preserve each model’s original configuration,
including conversation mode, hyperparameters, and frame
count. Following standard practices [9, 69], we set the tem-
perature to 0, top k to 1, and disable sampling for all models
to avoid randomness in response generation. For proprietary
models, we sample 16 frames. Implementation details and
full results are in the Supplementary Material.
ACH_BinaryQA
ACH_MCQ
TSH
STH
0
20
40
60
80
100
Video-ChatGPT
Video-LLaVA
LLAVA-NeXT-Video-34B
VILA1.5
VideoLLaMA2
ChatUniVi
ShareGPT4Video
PLLaVA
Figure 6. Comparative results on VIDHALLUC across various
hallucination types. ACH, TSH, and STH indicate action, temporal
sequence, and scene transition hallucination, respectively.
5.1. Evaluation on VIDHALLUC
Table 3 presents the performance of all tested MLLMs on
VIDHALLUC, showing both accuracy and score metrics
as percentages, reflecting the occurrence of hallucinations
across various tasks. For the ACH task, we observe that most
models score at least 20% higher on MCQs compared to
binary QA, even though both question types are based on
the same video and the same ground truth action. This sig-
nificant difference is due to the MCQ design, which includes
the ground truth action, an adversarial (semantically similar)
action, and two distractors (irrelevant actions). In contrast,
binary QA presents either the ground truth or an adversarial
action. Due to high semantic similarity, the model struggles
to answer “No” to adversarial actions, as it lacks the com-
parative context of MCQs and must rely solely on action
semantics. Higher MCQ accuracy suggests that when multi-
ple options are available, the model can leverage additional
contextual cues to differentiate semantically similar actions,
reducing hallucination risks. Without this context in binary
7

--- Page 8 ---

QA, the model is more prone to confusion and errors.
For TSH, most models score below 50%, revealing sig-
nificant challenges in distinguishing between semantically
similar but distinct actions over time, particularly when these
actions appear similar to the visual encoder. For example,
models often struggle to differentiate between successive
actions, such as “lifting a cup” followed by “placing a cup
down,” when they occur in rapid sequence within the same
video. Notably, in nearly 50% incorrect cases, models per-
ceive only a single action throughout the entire video, failing
to detect multiple actions or transitions. Similarly, for STH,
scores are generally low, with most models failing to sur-
pass 40%, highlighting substantial difficulties in accurately
detecting and segmenting scene changes.
We also observe that model size and the number of in-
put frames do not correlate directly with performance. For
instance, LLaVA-NeXT-Video-34B, which processes 32
frames, performs significantly worse on each task compared
to VILA1.5-13B, which operates with only 8 frames. Ad-
ditionally, models with higher-resolution visual encoders
generally outperform those with lower resolutions. Specifi-
cally, models using the CLIP ViT-L/14-336 encoder achieve
higher scores across nearly all metrics compared to those
using the lower-resolution CLIP ViT-L/14-224 encoder.
Proprietary models generally outperform open-source
models across most tasks, with GPT-4o standing out in par-
ticular. However, GPT-4o still falls short of human perfor-
mance, showing a 13.99% gap in ACH binary QA and a
15.85% gap in STH. In contrast, Gemini-1.5-Pro does not
consistently surpass the best open-source models. For in-
stance, its STH score (63.96%) is slightly lower than that of
VideoLLaMA2 (65.12%). These results highlight the need
for improvement even in top-performing proprietary models.
Because GPT-4o plays a key role in the MCQ component
by generating plausible distractors, we investigate whether it
gains an unfair advantage by recognizing its own generated
options. To assess this, we test GPT-4o on 300 videos with
corresponding MCQs. Among these, GPT-4o correctly iden-
tifies its own generated distractors only twice, misidentifies
them 33 times, and responds with “I don’t know” in 265
instances. These results suggest that GPT-4o is unlikely to
gain an unfair advantage during evaluation.
5.2. Evaluation of DINO-HEAL on VIDHALLUC
To evaluate the effectiveness of DINO-HEAL in miti-
gating hallucinations, we use Video-LLaVA [32], Video-
ChatGPT [39], VILA [33], and VideoLLaMA2 [9] as the
foundation backbones. Table 4 shows that DINO-HEAL en-
ables substantial improvements across various hallucination
types, achieving an average gain of 3.02%.
In the ACH task, DINO-HEAL leads to notable accuracy
gains, with Video-LLaVA and Video-ChatGPT showing in-
creases of +6.96% and +4.46% in Binary QA, respectively.
Models
Acc. on ACH
TSH
STH
Binary QA
MCQ
Video-ChatGPT
9.50
24.58
30.17
7.70
+DINO-HEAL
13.96+4.46
28.81+4.23
41.83+11.66
8.20+0.5
Video-LLaVA
26.84
64.45
27.17
29.60
+DINO-HEAL
33.80+6.96
66.25+1.8
28.50+1.33
31.42+1.82
ShareGPT4Video
29.96
44.78
49.50
17.83
+DINO-HEAL
30.41+0.45
44.43-0.35
55.33+5.83
18.39+0.56
VILA1.5
58.46
81.88
63.33
35.03
+DINO-HEAL
60.63+2.17
81.85-0.03
64.17+0.84
36.15+1.12
VideoLLaMA2
50.04
83.84
26.17
65.12
+DINO-HEAL
50.01-0.03
83.84+0.0
44.50+18.33
66.17+1.05
Table 4. Performance comparison of models on action hallucination
(ACH), temporal sequence hallucination (TSH), and scene transi-
tion hallucination (STH) tasks, with and without DINO-HEAL.
Improvements from DINO-HEAL are shown as subscripts. Bold
numbers denote the best performance after applying DINO-HEAL.
For the TSH task, DINO-HEAL significantly enhances tem-
poral coherence, with Video-ChatGPT achieving an +11.66%
gain and VideoLLaMA2 a substantial +18.33% increase. In
contrast, improvements in the STH task are more limited,
with an average 1.01% increase in performance. We attribute
the phenomenon to the inherent focus of DINOv2, the vi-
sual encoder, on foreground objects rather than background
elements or scene transitions, as it is primarily trained to ex-
tract visual features through discriminative self-supervised
learning. This foreground bias enhanced DINO-HEAL’s im-
pact on action recognition, driving significant gains in ACH
and TSH. However, it limits its effectiveness for background
scene understanding, as models may overlook background
changes crucial for accurate scene boundary detection.
DINO-HEAL is also designed to be compatible with a va-
riety of visual encoders beyond CLIP, such as LanguageBind-
Video [76] in Video-LLaVA and SigLIP [68] in VILA1.5. Af-
ter applying DINO-HEAL, both Video-LLaVA and VILA1.5
demonstrate consistent improvements across nearly all tasks,
highlighting DINO-HEAL’s versatility and effectiveness
across diverse model architectures.
6. Conclusion and Future Work
We introduce VIDHALLUC, the largest benchmark for eval-
uating action, temporal sequence, and scene transition hal-
lucinations in MLLMs for video understanding. We also
present DINO-HEAL, a novel training-free method to miti-
gate MLLM hallucinations by enhancing the visual encoder’s
focus on salient spatial regions during inference, improving
model robustness against hallucinations without additional
training. Extensive experiments show the effectiveness of
DINO-HEAL in mitigating hallucinations across models.
Future work includes expanding hallucination categories
to assess models in diverse settings and enhancing DINO-
HEAL with a dual-stream design integrating both spatial and
temporal saliency for improved video understanding.
8

--- Page 9 ---

Acknowledgments
This research was supported by the National Eye
Institute (NEI) of the National Institutes of Health
(NIH) under award number R01EY034562. The con-
tent is solely the responsibility of the authors and does
not necessarily represent the official views of the NIH.
References
[1] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad,
Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko
Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4
technical report. arXiv preprint arXiv 2303.08774, 2023. 3,
2, 9, 10
[2] Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine
Miech, Iain Barr, Yana Hasson, Karel Lenc, Arthur Men-
sch, Katie Millican, Malcolm Reynolds, Roman Ring, Eliza
Rutherford, Serkan Cabi, Tengda Han, Zhitao Gong, Sina
Samangooei, Marianne Monteiro, Jacob Menick, Sebastian
Borgeaud, Andrew Brock, Aida Nematzadeh, Sahand Shar-
ifzadeh, Mikolaj Binkowski, Ricardo Barreira, Oriol Vinyals,
Andrew Zisserman, and Karen Simonyan. Flamingo: a visual
language model for few-shot learning. In NeurIPS, 2022. 2
[3] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Sub-
biah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakan-
tan, Pranav Shyam, Girish Sastry, Amanda Askell, Sand-
hini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom
Henighan, Rewon Child, Aditya Ramesh, Daniel Ziegler, Jef-
frey Wu, Clemens Winter, Chris Hesse, Mark Chen, Eric
Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack
Clark, Christopher Berner, Sam McCandlish, Alec Radford,
Ilya Sutskever, and Dario Amodei. Language models are
few-shot learners. In NeurIPS, 2020. 2
[4] Keshigeyan Chandrasegaran, Agrim Gupta, Lea M. Hadzic,
Taran Kota, Jimming He, Crist´obal Eyzaguirre, Zane Durante,
Manling Li, Jiajun Wu, and Li Fei-Fei. Hourvideo: 1-hour
video-language understanding. In NeurIPS, 2024. 3
[5] Houlun Chen, Xin Wang, Hong Chen, Zeyang Zhang, Wei
Feng, Bin Huang, Jia Jia, and Wenwu Zhu. Verified: A video
corpus moment retrieval benchmark for fine-grained video
understanding. In NeurIPS, 2024. 3
[6] Lin Chen, Xilin Wei, Jinsong Li, Xiaoyi Dong, Pan Zhang,
Yuhang Zang, Zehui Chen, Haodong Duan, Bin Lin, Zhenyu
Tang, Li Yuan, Yu Qiao, Dahua Lin, Feng Zhao, and Jiaqi
Wang. Sharegpt4video: Improving video understanding and
generation with better captions. In NeurIPS, 2024. 1, 7, 2, 3,
9, 10
[7] Sihan Chen, Xingjian He, Longteng Guo, Xinxin Zhu, Wein-
ing Wang, Jinhui Tang, and Jing Liu. Valor: Vision-audio-
language omni-perception pretraining model and dataset.
arXiv preprint arXiv 2304.08345, 2023. 3, 1
[8] Xiang Chen, Chenxi Wang, Yida Xue, Ningyu Zhang, Xi-
aoyan Yang, Qiang Li, Yue Shen, Lei Liang, Jinjie Gu, and
Huajun Chen. Unified hallucination detection for multimodal
large language models. In ACL, 2024. 1
[9] Zesen Cheng, Sicong Leng, Hang Zhang, Yifei Xin, Xin
Li, Guanzheng Chen, Yongxin Zhu, Wenqi Zhang, Ziyang
Luo, Deli Zhao, and Lidong Bing. Videollama 2: Advancing
spatial-temporal modeling and audio understanding in video-
llms. arXiv preprint arXiv 2406.07476, 2024. 2, 7, 8, 3, 9,
10
[10] Mehdi Cherti, Romain Beaumont, Ross Wightman, Mitchell
Wortsman, Gabriel Ilharco, Cade Gordon, Christoph Schuh-
mann, Ludwig Schmidt, and Jenia Jitsev. Reproducible scal-
ing laws for contrastive language-image learning. In CVPR,
2023. 2
[11] Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph,
Yi Tay, William Fedus, Yunxuan Li, Xuezhi Wang, Mostafa
Dehghani, Siddhartha Brahma, et al. Scaling instruction-
finetuned language models. JMLR, 2024. 2
[12] Wenliang Dai, Junnan Li, Dongxu Li, Anthony Tiong, Junqi
Zhao, Weisheng Wang, Boyang Li, Pascale Fung, and Steven
Hoi. InstructBLIP: Towards general-purpose vision-language
models with instruction tuning. In NeurIPS, 2023. 2
[13] Jacob Devlin. Bert: Pre-training of deep bidirectional trans-
formers for language understanding. arXiv preprint arXiv
1810.04805, 2018. 2
[14] Danny Driess, Fei Xia, Mehdi S. M. Sajjadi, Corey Lynch,
Aakanksha Chowdhery, Brian Ichter, Ayzaan Wahid, Jonathan
Tompson, Quan Vuong, Tianhe Yu, Wenlong Huang, Yevgen
Chebotar, Pierre Sermanet, Daniel Duckworth, Sergey Levine,
Vincent Vanhoucke, Karol Hausman, Marc Toussaint, Klaus
Greff, Andy Zeng, Igor Mordatch, and Pete Florence. Palm-e:
an embodied multimodal language model. In ICML, 2023. 2
[15] Chaoyou Fu, Yuhan Dai, Yongdong Luo, Lei Li, Shuhuai
Ren, Renrui Zhang, Zihan Wang, Chenyu Zhou, Yunhang
Shen, Mengdan Zhang, Peixian Chen, Yanwei Li, Shaohui
Lin, Sirui Zhao, Ke Li, Tong Xu, Xiawu Zheng, Enhong
Chen, Rongrong Ji, and Xing Sun. Video-mme: The first-ever
comprehensive evaluation benchmark of multi-modal llms in
video analysis. arXiv preprint arXiv 2405.21075, 2024. 3
[16] Tianyu Gao, Xingcheng Yao, and Danqi Chen. SimCSE: Sim-
ple contrastive learning of sentence embeddings. In EMNLP,
2021. 5, 3
[17] Gregor Geigle, Chen Cecilia Liu, Jonas Pfeiffer, and Iryna
Gurevych. One does not fit all! on the complementarity of
vision encoders for vision and language tasks. In RepL4NLP,
2023. 1
[18] Tianrui Guan, Fuxiao Liu, Xiyang Wu, Ruiqi Xian, Zongxia
Li, Xiaoyu Liu, Xijun Wang, Lichang Chen, Furong Huang,
Yaser Yacoob, Dinesh Manocha, and Tianyi Zhou. Hallusion-
bench: An advanced diagnostic suite for entangled language
hallucination and visual illusion in large vision-language mod-
els. In CVPR, 2024. 1, 3
[19] Tianyang Han, Qing Lian, Rui Pan, Renjie Pi, Jipeng Zhang,
Shizhe Diao, Yong Lin, and Tong Zhang. The instinctive
bias: Spurious images lead to hallucination in mllms. arXiv
preprint arXiv 2402.03757, 2024. 1
[20] Fabian Caba Heilbron, Victor Escorcia, Bernard Ghanem,
and Juan Carlos Niebles. Activitynet: A large-scale video
benchmark for human activity understanding. In CVPR, 2015.
3, 1
[21] Aaron Hurst, Adam Lerer, Adam P. Goucher, Adam Perel-
man, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila Weli-
9

--- Page 10 ---

hinda, Alan Hayes, et al. Gpt-4o system card. arXiv preprint
arXiv:2410.21276, 2024. 4, 7
[22] Dongsheng Jiang, Yuchen Liu, Songlin Liu, Jin’e Zhao,
Hao Zhang, Zhen Gao, Xiaopeng Zhang, Jin Li, and
Hongkai Xiong. From clip to dino: Visual encoders shout
in multi-modal large language models.
arXiv preprint
arXiv:2310.08825, 2023. 1
[23] Peng Jin, Ryuichi Takanobu, Wancai Zhang, Xiaochun Cao,
and Li Yuan. Chat-univi: Unified visual representation em-
powers large language models with image and video under-
standing. In CVPR, 2024. 2, 7, 3, 8, 9, 10
[24] Jing Yu Koh, Ruslan Salakhutdinov, and Daniel Fried.
Grounding language models to images for multimodal inputs
and outputs. In ICML, 2023. 2
[25] Seongyun Lee, Sue Hyun Park, Yongrae Jo, and Minjoon
Seo. Volcano: Mitigating multimodal hallucination through
self-feedback guided revision. In ACL, 2024. 2
[26] Sicong Leng, Hang Zhang, Guanzheng Chen, Xin Li, Shijian
Lu, Chunyan Miao, and Lidong Bing. Mitigating object
hallucinations in large vision-language models through visual
contrastive decoding. In CVPR, 2024. 1
[27] Junnan Li, Dongxu Li, Silvio Savarese, and Steven Hoi. BLIP-
2: Bootstrapping language-image pre-training with frozen
image encoders and large language models. In ICML, 2023.
2
[28] Kunchang Li, Yali Wang, Yinan He, Yizhuo Li, Yi Wang, Yi
Liu, Zun Wang, Jilan Xu, Guo Chen, Ping Luo, Limin Wang,
and Yu Qiao. Mvbench: A comprehensive multi-modal video
understanding benchmark. In CVPR, 2024. 3
[29] Linjie Li, Jie Lei, Zhe Gan, Licheng Yu, Yen-Chun Chen,
Rohit Pillai, Yu Cheng, Luowei Zhou, Xin Eric Wang,
William Yang Wang, Tamara Lee Berg, Mohit Bansal,
Jingjing Liu, Lijuan Wang, and Zicheng Liu. Value: A multi-
task benchmark for video-and-language understanding evalu-
ation. In NeurIPS, 2024. 3
[30] Yifan Li, Yifan Du, Kun Zhou, Jinpeng Wang, Xin Zhao,
and Ji-Rong Wen. Evaluating object hallucination in large
vision-language models. In EMNLP, 2023. 1
[31] Yunxin Li, Xinyu Chen, Baotian Hu, Longyue Wang,
Haoyuan Shi, and Min Zhang. Videovista: A versatile bench-
mark for video understanding and reasoning. arXiv preprint
arXiv 2406.11303, 2024. 3
[32] Bin Lin, Yang Ye, Bin Zhu, Jiaxi Cui, Munan Ning, Peng Jin,
and Li Yuan. Video-llava: Learning united visual representa-
tion by alignment before projection. In EMNLP, 2024. 1, 2,
7, 8, 3, 9, 10
[33] Ji Lin, Hongxu Yin, Wei Ping, Yao Lu, Pavlo Molchanov,
Andrew Tao, Huizi Mao, Jan Kautz, Mohammad Shoeybi,
and Song Han. Vila: On pre-training for visual language
models. In CVPR, 2024. 2, 7, 8, 3, 9, 10
[34] Fuxiao Liu, Kevin Lin, Linjie Li, Jianfeng Wang, Yaser Ya-
coob, and Lijuan Wang. Mitigating hallucination in large
multi-modal models via robust instruction tuning. In ICLR,
2024. 2
[35] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee.
Visual instruction tuning. In NeurIPS, 2023. 1, 2
[36] Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee.
Improved baselines with visual instruction tuning. In CVPR,
2024. 2
[37] Jiazhen Liu, Yuhan Fu, Ruobing Xie, Runquan Xie, Xingwu
Sun, Fengzong Lian, Zhanhui Kang, and Xirong Li. Phd:
A prompted visual hallucination evaluation dataset. arXiv
preprint arXiv 2403.11116, 2024. 1
[38] Yuan Liu, Haodong Duan, Yuanhan Zhang, Bo Li, Songyang
Zhang, Wangbo Zhao, Yike Yuan, Jiaqi Wang, Conghui He,
Ziwei Liu, Kai Chen, and Dahua Lin. Mmbench: Is your
multi-modal model an all-around player? In ECCV, 2024. 3
[39] Muhammad Maaz, Hanoona Rasheed, Salman Khan, and
Fahad Khan. Video-ChatGPT: Towards detailed video under-
standing via large vision and language models. In ACL, 2024.
2, 7, 8, 3, 9, 10
[40] Karttikeya Mangalam, Raiymbek Akshulakov, and Jitendra
Malik. Egoschema: A diagnostic benchmark for very long-
form video language understanding. In NeurIPS, 2023. 1
[41] Muhammad Ferjad Naeem, Yongqin Xian, Xiaohua Zhai,
Lukas Hoyer, Luc Van Gool, and Federico Tombari. Silc:
Improving vision language pretraining with self-distillation.
In ECCV, 2024. 2
[42] Huy H Nguyen, Junichi Yamagishi, and Isao Echizen. Explor-
ing self-supervised vision transformers for deepfake detection:
A comparative analysis. arXiv preprint arXiv:2405.00355,
2024. 1
[43] Nguyen Nguyen, Jing Bi, Ali Vosoughi, Yapeng Tian, Pooyan
Fazli, and Chenliang Xu. Oscar: Object state captioning and
state change representation. In NAACL, 2024. 3
[44] Maxime Oquab, Timoth´ee Darcet, Th´eo Moutakanni, Huy V.
Vo, Marc Szafraniec, Vasil Khalidov, Pierre Fernandez,
Daniel HAZIZA, Francisco Massa, Alaaeldin El-Nouby,
Mido Assran, Nicolas Ballas, Wojciech Galuba, Russell
Howes, Po-Yao Huang, Shang-Wen Li, Ishan Misra, Michael
Rabbat, Vasu Sharma, Gabriel Synnaeve, Hu Xu, Herve Je-
gou, Julien Mairal, Patrick Labatut, Armand Joulin, and Piotr
Bojanowski. DINOv2: Learning robust visual features with-
out supervision. TMLR, 2024. 2, 1
[45] Baolin Peng, Chunyuan Li, Pengcheng He, Michel Galley,
and Jianfeng Gao.
Instruction tuning with gpt-4.
arXiv
preprint arXiv 2304.03277, 2023. 2
[46] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya
Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry,
Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen
Krueger, and Ilya Sutskever. Learning transferable visual
models from natural language supervision. PMLR, 2021. 2, 1
[47] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee,
Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and
Peter J Liu. Exploring the limits of transfer learning with a
unified text-to-text transformer. JMLR, 2020. 2
[48] Cristian Rodriguez-Opazo, Edison Marrese-Taylor, Ehsan
Abbasnejad, Hamed Damirchi, Ignacio M. Jara, Felipe Bravo-
Marquez, and Anton van den Hengel. Unveiling backbone
effects in clip: Exploring representational synergies and vari-
ances. arXiv preprint arXiv:2312.14400, 2023. 1
[49] Anna Rohrbach, Lisa Anne Hendricks, Kaylee Burns, Trevor
Darrell, and Kate Saenko. Object hallucination in image
captioning. arXiv preprint arXiv 1809.02156, 2018. 1
10

--- Page 11 ---

[50] Quan Sun, Yuxin Fang, Ledell Wu, Xinlong Wang, and Yue
Cao. Eva-clip: Improved training techniques for clip at scale.
arXiv preprint arXiv 2303.15389, 2023. 2, 1
[51] Zhiqing Sun, Sheng Shen, Shengcao Cao, Haotian Liu, Chun-
yuan Li, Yikang Shen, Chuang Gan, Liang-Yan Gui, Yu-
Xiong Wang, Yiming Yang, Kurt Keutzer, and Trevor Darrell.
Aligning large multimodal models with factually augmented
rlhf. arXiv preprint arXiv 2309.14525, 2023. 1, 2
[52] Yunlong Tang, Jing Bi, Siting Xu, Luchuan Song, Susan
Liang, Teng Wang, Daoan Zhang, Jie An, Jingyang Lin,
Rongyi Zhu, Ali Vosoughi, Chao Huang, Zeliang Zhang,
Pinxin Liu, Mingqian Feng, Feng Zheng, Jianguo Zhang,
Ping Luo, Jiebo Luo, and Chenliang Xu. Video understand-
ing with large language models: A survey. arXiv preprint
arXiv 2312.17432, 2023. 1
[53] Gemini Team, Petko Georgiev, Ving Ian Lei, Ryan Burnell,
Libin Bai, Anmol Gulati, Garrett Tanzer, Damien Vincent,
Zhufeng Pan, Shibo Wang, et al. Gemini 1.5: Unlocking mul-
timodal understanding across millions of tokens of context.
arXiv preprint arXiv 2403.05530, 2024. 7, 2, 3, 9, 10
[54] Shengbang Tong, Ellis L Brown II, Penghao Wu, Sanghyun
Woo, ADITHYA JAIRAM IYER, Sai Charitha Akula,
Shusheng Yang, Jihan Yang, Manoj Middepogu, Ziteng Wang,
Xichen Pan, Rob Fergus, Yann LeCun, and Saining Xie.
Cambrian-1: A fully open, vision-centric exploration of mul-
timodal LLMs. In NeurIPS, 2024. 1
[55] Shengbang Tong, Zhuang Liu, Yuexiang Zhai, Yi Ma, Yann
LeCun, and Saining Xie. Eyes wide shut? exploring the
visual shortcomings of multimodal llms. In CVPR, 2024. 2, 3
[56] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Mar-
tinet, Marie-Anne Lachaux, Timoth´ee Lacroix, Baptiste
Rozi`ere, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien
Rodriguez, Armand Joulin, Edouard Grave, and Guillaume
Lample. Llama: Open and efficient foundation language
models. arXiv preprint arXiv 2302.13971, 2023. 2
[57] Junyang Wang, Yuhang Wang, Guohai Xu, Jing Zhang, Yukai
Gu, Haitao Jia, Jiaqi Wang, Haiyang Xu, Ming Yan, Ji Zhang,
and Jitao Sang. Amber: An llm-free multi-dimensional bench-
mark for mllms hallucination evaluation. arXiv preprint arXiv
2311.07397, 2023. 1
[58] Yuxuan Wang, Yueqian Wang, Dongyan Zhao, Cihang Xie,
and Zilong Zheng. Videohallucer: Evaluating intrinsic and
extrinsic hallucinations in large video-language models. arXiv
preprint arXiv 2406.16338, 2024. 1, 3
[59] Jason Wei, Maarten Bosma, Vincent Y Zhao, Kelvin Guu,
Adams Wei Yu, Brian Lester, Nan Du, Andrew M Dai, and
Quoc V Le. Finetuned language models are zero-shot learners.
arXiv preprint arXiv 2109.01652, 2021. 2
[60] Haoning Wu, Dongxu Li, Bei Chen, and Junnan Li.
Longvideobench: A benchmark for long-context interleaved
video-language understanding. In NeurIPS, 2024. 3
[61] Monika Wysoczanska, Oriane Sim´eoni, Micha¨el Ramamon-
jisoa, Andrei Bursuc, Tomasz Trzcinski, and Patrick P´erez.
Clip-dinoiser: Teaching clip a few dino tricks for open-
vocabulary semantic segmentation. In ECCV, 2024. 1
[62] Hu Xu, Gargi Ghosh, Po-Yao Huang, Dmytro Okhonko,
Armen Aghajanyan, Florian Metze, Luke Zettlemoyer, and
Christoph Feichtenhofer. Videoclip: Contrastive pre-training
for zero-shot video-text understanding. In EMNLP, 2021. 2
[63] Lin Xu, Yilin Zhao, Daquan Zhou, Zhijie Lin, See Kiong Ng,
and Jiashi Feng. Pllava : Parameter-free llava extension from
images to videos for video dense captioning. arXiv preprint
arXiv 2404.16994, 2024. 7, 2, 3, 8, 9, 10
[64] Dongjie Yang, Suyuan Huang, Chengqiang Lu, Xiaodong
Han, Haoxin Zhang, Yan Gao, Yao Hu, and Hai Zhao. Vript:
A video is worth thousands of words. In NeurIPS, 2024. 1, 2,
3
[65] Shukang Yin, Chaoyou Fu, Sirui Zhao, Tong Xu, Hao Wang,
Dianbo Sui, Yunhang Shen, Ke Li, Xing Sun, and Enhong
Chen. Woodpecker: Hallucination correction for multimodal
large language models. arXiv preprint arXiv 2310.16045,
2023. 2
[66] Qifan Yu, Juncheng Li, Longhui Wei, Liang Pang, Wentao
Ye, Bosheng Qin, Siliang Tang, Qi Tian, and Yueting Zhuang.
Hallucidoctor: Mitigating hallucinatory toxicity in visual
instruction data. In CVPR, 2024. 1, 2
[67] Tianyu Yu, Yuan Yao, Haoye Zhang, Taiwen He, Yifeng Han,
Ganqu Cui, Jinyi Hu, Zhiyuan Liu, Hai-Tao Zheng, Maosong
Sun, et al. Rlhf-v: Towards trustworthy mllms via behavior
alignment from fine-grained correctional human feedback. In
CVPR, 2024. 2
[68] Xiaohua Zhai, Basil Mustafa, Alexander Kolesnikov, and
Lucas Beyer. Sigmoid loss for language image pre-training.
In ICCV, 2023. 2, 8, 1
[69] Boqiang Zhang, Kehan Li, Zesen Cheng, Zhiqiang Hu,
Yuqian Yuan, Guanzheng Chen, Sicong Leng, Yuming Jiang,
Hang Zhang, Xin Li, Peng Jin, Wenqi Zhang, Fan Wang,
Lidong Bing, and Deli Zhao. Videollama 3: Frontier multi-
modal foundation models for image and video understanding.
arXiv preprint arXiv 2501.13106, 2025. 7
[70] Hao Zhang, Feng Li, Shilong Liu, Lei Zhang, Hang Su, Jun
Zhu, Lionel Ni, and Heung-Yeung Shum. DINO: DETR
with improved denoising anchor boxes for end-to-end object
detection. In ICLR, 2023. 1
[71] Jiacheng Zhang, Yang Jiao, Shaoxiang Chen, Jingjing Chen,
and Yu-Gang Jiang. Eventhallusion: Diagnosing event hal-
lucinations in video llms. arXiv preprint arXiv 2409.16597,
2024. 3
[72] Yuanhan Zhang, Bo Li, haotian Liu, Yong jae Lee, Liangke
Gui, Di Fu, Jiashi Feng, Ziwei Liu, and Chunyuan Li. LLaVA-
NeXT: A strong zero-shot video understanding model, 2024.
2, 7, 3, 8, 9, 10
[73] Zhiyuan Zhao, Bin Wang, Linke Ouyang, Xiaoyi Dong, Jiaqi
Wang, and Conghui He. Beyond hallucinations: Enhancing
lvlms through hallucination-aware direct preference optimiza-
tion. arXiv preprint arXiv 2311.16839, 2023. 1, 2
[74] Luowei Zhou, Chenliang Xu, and Jason J. Corso. Towards au-
tomatic learning of procedures from web instructional videos.
In AAAI, 2018. 3, 1
[75] Yiyang Zhou, Chenhang Cui, Rafael Rafailov, Chelsea Finn,
and Huaxiu Yao. Aligning modalities in vision large lan-
guage models via preference fine-tuning. arXiv preprint arXiv
2402.11411, 2024. 2
11

--- Page 12 ---

[76] Bin Zhu, Bin Lin, Munan Ning, Yang Yan, Jiaxi Cui, WANG
HongFa, Yatian Pang, Wenhao Jiang, Junwu Zhang, Zong-
wei Li, Cai Wan Zhang, Zhifeng Li, Wei Liu, and Li Yuan.
Languagebind: Extending video-language pretraining to n-
modality by language-based semantic alignment. In ICLR,
2024. 8
[77] Deyao Zhu, Jun Chen, Xiaoqian Shen, Xiang Li, and Mo-
hamed Elhoseiny. MiniGPT-4: Enhancing vision-language
understanding with advanced large language models. In ICLR,
2024. 2
12

--- Page 13 ---

VIDHALLUC: Evaluating Temporal Hallucinations
in Multimodal Large Language Models for Video Understanding
Supplementary Material
A. Additional Related Works
Different neural network architectures, trained on distinct
datasets, develop unique inductive biases that influence their
feature representation capabilities. For instance, the CLIP
series [46, 50, 68], pretrained with text-image contrastive
alignment, excels at capturing global semantic features. In
contrast, the DINO series [44, 70], pretrained with vision-
only contrastive learning, specializes in fine-grained per-
ception and object-level details. Prior research shows that
integrating features from complementary networks can lead
to a more balanced and robust model behavior [17, 48].
Building on these strengths, COMM [22] demonstrates
the effectiveness of integrating features from different layers
of CLIP and DINOv2 to enhance the visual capabilities of
multimodal large language models (MLLMs). By leveraging
the complementary nature of these architectures, COMM
achieves improved performance across various visual tasks.
Similarly, CLIP-DINOiser [61] uses localization priors from
DINO to refine CLIP’s global image features, resulting in
smoother and more precise outputs for semantic segmen-
tation tasks. Furthermore, Nguyen et al. [42] explore the
multi-level features of DINO to fine-tune the final block of
CLIP. This approach not only tackles the challenge posed by
the limited scale of training datasets in deepfake detection
but also enhances model interpretability through the use of
attention mechanisms. These studies collectively highlight
the potential of combining the strengths of diverse architec-
tures to overcome individual limitations, achieve superior
performance, and improve explainability in complex visual
tasks. However, these methods often rely on specific archi-
tectures and require additional adjustments or training for
integration, which limits their flexibility and scalability.
To address these limitations, our proposed DINO-HEAL
offers a flexible and architecture-agnostic solution that can be
applied at the inference stage without modifying the under-
lying model structures. Unlike previous approaches, DINO-
HEAL does not require additional training parameters or
fine-tuning, making it particularly suitable for mitigating
hallucinations in resource-constrained scenarios.
B. Implementation Details
B.1. Data Collection on Existing Datasets
To apply our data collection pipeline to the selected
datasets, we employ a structured process for segmenting
and pairing videos. Specifically, for ActivityNet [20] and
YouCook2 [74], videos are divided into multiple action-
based segments. We then compute similarities between all
segment pairs within each video to identify pairs meeting the
similarity criteria. For VALOR32K [7], videos are randomly
paired, and their similarities are calculated to determine if
they satisfy the conditions. The resulting filtered video pairs,
characterized by high semantic similarity but low visual
similarity, form the core of our dataset, enabling effective
investigation into hallucination phenomena.
B.2. Prompts for Different Hallucination Tasks
The following subsections show the prompts we use to test
models on each hallucination task: action hallucination
(ACH), temporal sequence hallucination (TSH), and scene
transitional hallucination (STH).
B.2.1. Prompt for Binary QA in ACH
<Video>
Is the primary action in the video
{Action}?
Only answer with "No" or "Yes".
The placeholder {Action} in the prompt is dynamically re-
placed with a specific action, such as ‘turning the steering
wheel’. To further enhance the diversity of the benchmark,
each Binary QA question is randomly assigned one of four
templates: “Is the prominent action in the video {Action}?”,
“Does the video primarily feature {Action}?”, “Is the key
action shown in the video {Action}?”, or “Is the primary
action in the video {Action}?” These variations introduce
linguistic diversity while preserving the semantic meaning.
B.2.2. Prompt for MCQs in ACH
<Video>
"Question": "What is the prominent
action in the video?" Please select
the correct answer (one or more options),
only return the choice letter (i.e., A,
B, C, D) of your answer(s).
"Choices":
"A": "{Action A}"
"B": "{Action B}"
"C": "{Action C}"
"D": "{Action D}"
The placeholders {Action A}, {Action B}, {Action C}, and
{Action D} are dynamically replaced with specific actions,
such as “wakeboarding,” “changing gears,” “adjusting the
1

--- Page 14 ---

rearview mirror,” and “turning the steering wheel.” To in-
troduce linguistic diversity and enhance the robustness of
the benchmark, each MCQ is randomly assigned one of
the following templates: “What is the prominent action in
the video?”, “What is the key action shown in the video?”,
“What is the primary action in the video?”, or “What is the pre-
dominant action captured in the video?”. These variations
ensure that the benchmark reflects a range of natural question
formulations while maintaining consistency in meaning.
B.2.3. Prompt for Sorting Questions in TSH
<Video>
Below are two actions in the video:
Action A. {Action A}
Action B. {Action B}
Sort these two actions in the order they
occur in the video, and return which
action happens before which one. For
example, "Action A before Action B" or
"Action B before Action A". If you only
detect one action of these two in the
video, return that action.
The placeholders {Action A}, {Action B} are replaced with
specific actions. For instance, with the actions of skiing and
driving a car, the prompt will look as the following example:
“Below are two actions in the video: Action A. skiing, Action B.
driving a car. Sort these two actions in the order they occur
in the video, and return which action happens before which
one. For example, ‘Action A before Action B’ or ‘Action B
before Action A’. If you only detect one action of these two
in the video, return that action.”
B.2.4. Prompt for Open-ended Questions in STH
<Video>
A scene change is defined as a
significant transition in the overall
environment or location within the
video. This means a change from one
distinct setting to another, such as
moving from a kitchen to a living room,
or from indoors to outdoors. Watch the
given video and determine if a scene
change occurs. If there is a scene
change, respond in the format: "Scene
change: Yes, Locations: from [location]
to [location2]." If no change occurs,
respond: "Scene change: No, Locations:
None".
B.3. Additional Dataset Statistics
Figure 7 displays a word cloud of our benchmark, providing
a more intuitive presentation of VIDHALLUC. As shown
Figure 7. The wordcloud of VIDHALLUC.
in the figure, the questions in our benchmark are diverse
and prominently feature action-related terms, such as “play-
ing,” “walking,” “cutting,” “cleaning,” and “jumping.” These
terms highlight the dynamic nature of the video content in
our benchmark, emphasizing the focus on activities and in-
teractions within videos. The word cloud reflects the breadth
of actions and events covered, including activities like “mix-
ing ingredients,” “pouring water,” “riding,” and “driving.”
This diversity aligns with our goal of capturing the chal-
lenges associated with action recognition, temporal coher-
ence, and scene understanding in videos. We believe our
benchmark can effectively reveal potential hallucination is-
sues in MLLMs, especially those related to understanding
complex actions in dynamic video content.
C. More Quantitative Results on VIDHALLUC
We
provide
additional
metrics
and
detailed
scores
of state-of-the-art MLLM performance on VIDHAL-
LUC. For open source models,
we include Video-
ChatGPT [39], Video-LLaVA [32], ShareGPT4Video [6],
Chat-UniVi [23], LLaVA-NeXT-Video [72], PLLaVA [63],
VideoLLaMA2 [9], and VILA 1.5 [33]. For proprietary
models, we select Gemini-1.5-Pro [53], and GPT-4o [1].
Quantitative results on ACH.
Table 5 presents two dis-
tinct versions of the quantitative results for these models on
the ACH task. The binary QA and MCQ scores are com-
puted by dividing the number of correct answers by the total
number of questions, following the metric defined as:
  \text { Accuracy
} = \f
rac {N_\text {correct}}{N_\text {total}}, 
(13)
where Ncorrect and Ntotal denote non-negative counts of cor-
rect answers and total answers. In contrast, binary QA Pair
and MCQ Pair scores are based on a stricter criterion requir-
ing both questions in a pair to be answered correctly. This
stricter evaluation ensures that the model fully understands
both semantically similar but visually different videos.
As mentioned in the main paper, an interesting observa-
tion is that the accuracy for MCQ is higher than that for
2

--- Page 15 ---

Models
Binary QA
Binary QA Pair
MCQ
MCQ Pair
Video-ChatGPT [39]
9.50
0.19
24.58
5.56
Video-LLaVA [32]
26.84
9.87
64.45
40.34
ShareGPT4Video [6]
29.96
10.65
44.78
19.18
Chat-UniVi [23]
23.77
6.39
54.79
29.37
LLaVA-NeXT-Video [72]
26.60
12.00
77.57
60.03
PLLaVA [63]
35.30
16.26
76.96
59.94
VideoLLaMA2 [9]
50.04
29.09
83.84
69.85
VILA1.5 [33]
58.46
37.77
81.88
67.95
Gemini-1.5-Pro [53]
75.27
59.10
79.25
63.36
GPT-4o [1]
81.15
66.79
90.95
83.00
Table 5. Performance comparison of existing models on action
hallucination (ACH). The numbers in the table represent accuracy
percentages (%). Bold numbers denote the best performance, and
underlined numbers indicate the second-best performance.
binary questions. This result defies common intuition, as
one might expect binary questions, with only two possible
answers, to be inherently simpler and, therefore, yield higher
accuracy compared to MCQs, which involve selecting from
multiple options. This discrepancy suggests that models may
leverage contextual or comparative cues more effectively in
MCQ scenarios, while binary questions might require more
precise reasoning or direct understanding, exposing potential
weaknesses in model comprehension.
Quantitative results on STH
In STH, we benchmark
MLLMs with the new criterion that evaluates both the classi-
fication of the scene and whether the model describes it in
the correct sequence. For the classification scores, we use
the Matthews correlation coefficient (MCC) to evaluate the
model predictions against the ground truth labels.
  \ f rac  {n_ { 11}
 
\tim e s n_{10}  - n_{01}  \times n _ {00}
}{\sqrt {(n_{11} + n_{01}) (n_{11} + n_{00})(n_{10} + n_{01})(n_{10} + n_{00})}}, \label {eq:mcc} (14)
where A ∈{0 (False), 1 (True)} represents the actual con-
dition, P ∈{0 (Negative), 1 (Positive)} represents the pre-
dicted condition, and nAP denotes non-negative counts. To
adjust MCC to range between 0 and 1 and to further penalize
models that consistently answer only “Yes” or only “No”,
we apply the transformation in order to adjust MCC to range
between 0 and 1, obtaining the classification score Scorecls:
  \text {
Scor e }
_
\t
ext {cls} = \left ( \frac {\text {MCC} + 1}{2} \right )^2. \label {eq:cls_score} 
(15)
The description task measures the model’s ability to accu-
rately identify and articulate the information of the scene.
To evaluate this, scene descriptions are extracted from both
the model’s output and the ground truth, structured for di-
rect comparison. We then calculate the cosine similarity S
between the SimCSE [16] embeddings of the correspond-
ing scenes. Based on this similarity measure, each scene
description score is calculated as:
Models
Scorecls
Scoredesc
Scoreoverall
Video-ChatGPT [39]
5.07
11.65
7.70
Video-LLaVA [32]
25.00
36.50
29.60
ShareGPT4Video [6]
29.55
0.26
17.83
Chat-UniVi [23]
30.12
29.50
29.87
LLaVA-NeXT-Video [72]
55.91
27.14
44.40
PLLaVA [63]
29.86
36.32
32.44
VideoLLaMA2 [9]
87.43
31.67
65.12
VILA1.5 [33]
25.00
50.07
35.03
Gemini-1.5-Pro [53]
71.88
52.08
63.96
GPT-4o [1]
80.17
58.69
71.58
Table 6. Performance comparison of existing models on scene
transition hallucination (STH). We assign a weight of 0.6 to the
classification task and 0.4 to the description task. The numbers
in the table represent accuracy percentages (%). Bold numbers
denote the best performance, and underlined numbers indicate the
second-best performance.
  \text { S
c
or
e} _ { \text 
{desc}} = \beg
in {cases} \hf i
ll  0 , & \t
ext {if } S \leq \text {THR}_{\text {low}} \\ \frac {\sigma (S) - \sigma (\text {THR}_{\text {low}})}{\sigma (1) - \sigma (\text {THR}_{\text {low}})}, & \text {if } S > \text {THR}_{\text {low}} \end {cases}, \label {eq:desc_score} 
(16)
where S denotes the cosine similarity between the Sim-
CSE [16] embeddings of the corresponding scenes,  \text {THR}_{\text {low}} 
represents the minimum threshold for assigning a score, and
σ is the Sigmoid function. The overall description score is
calculated as the average of the score for the “from” and “to”
scenes. Finally, the overall evaluation score is computed as a
weighted sum of the classification score and the normalized
description score:
  \text {Sco r e } _{\text { ov e ra l l}} = \alpha \times \text {Score}_{\text {cls}} + (1 - \alpha ) \times \text {Score}_{\text {desc}}. \label {eq:overall_score} 
(17)
Table 6 summarizes the decomposed scores of classification
and description scores for the STH category. An interesting
observation is that both Video-LLaVA and VILA 1.5 achieve
a classification score of 25% by consistently answering “Yes”
to all questions, irrespective of their actual ability to recog-
nize transitions between locations. This pattern, highlighted
in the 10th row of Table 12, exposes a critical limitation
in both the MCC metric and the model themselves. Their
reliance on default affirmative response reveals a superficial
understanding of spatial transition and suggests a lack of
deeper reasoning.
Future work should focus on developing mechanisms to
penalize such oversights and promote consistency in model
behavior, ensuring that metrics better reflect genuine under-
standing and performance. This includes designing metrics
or loss functions that discourage uniform responses and pro-
mote adaptive reasoning based on context.
3

--- Page 16 ---

CLIP
DINOv2
Frame
DINO-HEAL
Figure 8. The visualization of saliency maps.
D. DINO-HEAL
D.1. Saliency Analysis
Figure 8 illustrates the input frames, saliency maps gener-
ated by CLIP and DINOv2, and the adjusted saliency map
produced by DINO-HEAL. The saliency maps generated by
CLIP often show significant noise, which can be attributed to
its inductive bias toward capturing global contextual frame
information. This characteristic, while beneficial for under-
standing broader scene-level features, can result in a lack
of focus on specific, spatially important regions within the
frame. In contrast, DINOv2 demonstrates a stronger capac-
ity to localize and emphasize key objects within the scene,
leveraging its vision-only contrastive learning to identify
fine-grained details efficiently. The adjusted saliency maps
created by DINO-HEAL reflect an integration of these two
approaches, balancing the strengths of both CLIP and DI-
NOv2. By mitigating the noisiness of CLIP’s global focus
and incorporating the precise localization capabilities of DI-
NOv2, DINO-HEAL effectively emphasizes spatially signif-
icant features. This result strongly supports our hypothesis
that DINO-HEAL serves as a complementary mechanism to
CLIP, enhancing its ability to prioritize critical regions and
improving overall spatial feature representation.
D.2. Additional Results on VIDHALLUC
Tables 7 and 8 show the results of the ACH and STH tasks
when baseline models are augmented with our hallucination
mitigation method, DINO-HEAL. A particularly notewor-
thy observation is the significant improvement in scores for
Video-LLaVA and VILA 1.5 on the STH task. Previously,
these models consistently defaulted to answering “Yes” re-
gardless of the correct location-based response. With the
integration of DINO-HEAL, however, they demonstrate an
improved ability to discern and appropriately respond with
”No” when necessary, as elaborated in Section C. This in-
dicates a meaningful enhancement in their spatial reason-
ing and decision-making capabilities. This improvement
underscores the potential of DINO-HEAL to refine spatial
reasoning and address their shortcomings effectively.
Tables 9 and 10 further detail the results for Video-
ChatGPT, Video-LLaVA, and VideoLLaMA2 on the ACH
and TSH tasks, comparing performance with and without
DINO-HEAL. For the ACH task, we use the binary QA ac-
curacy metric. Without DINO-HEAL, none of the models
correctly predict all question pairs, though VideoLLaMA2
is able to infer the second question pair accurately. When
DINO-HEAL is applied, however, all models can predict
both pairs accurately, showcasing the method’s effectiveness
in mitigating hallucinations. On the TSH task, we observe
further improvements. Initially, Video-ChatGPT recognizes
that two actions occur simultaneously, while the ground
truth sequence is “starting a fire” followed by “gutting a
fish”. Video-LLaVA and VideoLLaMA2 only identify one
action, “starting a fire”. After integrating DINO-HEAL, all
three models correctly identify and sequence both actions,
underscoring the method’s ability to enhance temporal un-
derstanding in complex tasks.
E. More Qualitative Results on VIDHALLUC
Tables 11, 12, and 13 present randomly selected examples
showcasing multiple model responses for the ACH, TSH,
and STH tasks, respectively. For the ACH task, the Binary
QA Pair metric is used, which applies a stricter evaluation
criterion requiring both questions in a pair to be answered
correctly. In particular, the adversarially crafted pairs in
4

--- Page 17 ---

Models
Binary QA
Binary QA Pair
MCQ
MCQ Pair
Video-ChatGPT
9.50
0.19
24.58
5.56
+DINO-HEAL
13.96+4.46
0.42+0.23
28.81+4.23
6.76+1.20
Video-LLaVA
26.84
9.87
64.45
40.34
+DINO-HEAL
33.80+6.96
14.17+4.3
66.25+1.8
41.64+1.3
ShareGPT4Video
29.96
10.65
44.78
19.18
+DINO-HEAL
30.41+0.45
9.73-0.92
44.43-0.35
18.62-0.56
VILA1.5
58.46
37.77
81.88
67.95
+DINO-HEAL
60.63+2.17
40.34+2.57
81.85-0.03
67.90-0.05
VideoLLaMA2
50.04
29.09
83.84
69.85
+DINO-HEAL
50.01-0.03
29.07-0.02
83.84+0.0
69.85+0.0
Table 7. Performance comparison of models on action hallucination
(ACH), with and without DINO-HEAL. Improvements from DINO-
HEAL are shown as subscripts. Bold numbers denote the best
performance after applying DINO-HEAL.
Models
Scorecls
Scoredesc
Scoreoverall
Video-ChatGPT
5.07
11.65
7.70
+DINO-HEAL
5.56+0.49
12.15+0.5
8.20+0.5
Video-LLaVA
25.00
36.50
29.60
+DINO-HEAL
27.89+2.89
35.18-2.61
30.81+0.69
ShareGPT4Video
29.55
0.26
17.83
+DINO-HEAL
28.80-0.75
2.78+2.52
18.39+0.56
VILA1.5
25.00
50.07
35.03
+DINO-HEAL
26.66+1.66
50.38+0.21
36.15+1.12
VideoLLaMA2
87.43
31.67
65.12
+DINO-HEAL
89.19+1.76
31.63-0.04
66.17+1.05
Table 8. Performance comparison of models on scene transition
hallucination (STH), with and without DINO-HEAL. We assign a
weight of 0.6 to the classification task and 0.4 to the description
task. Improvements from DINO-HEAL are shown as subscripts.
Bold numbers denote the best performance applying DINO-HEAL.
the ACH category require MLLMs to discern between se-
mantically similar actions, posing a significant challenge
for accurate interpretation. None of the models could pre-
dict both pairs accurately, highlighting the complexity of
the ACH task. Moreover, Table 12 details the description
scores for each example. These examples demonstrate that
locations highly relevant to the ground truth achieve high
scores. For instance, the phrase “in a swimming pool” ex-
hibits strong semantic description similarity with “pool” or
“a swimming pool,” while “in a bathtub” aligns well with
“the bathtub”. Conversely, locations with differing seman-
tic descriptions or inaccurate interpretations receive lower
description scores. For example, “in a swimming pool” has
limited similarity to descriptions such as “indoor bathroom”
or “indoor pool,” and “in a bathtub” similarly diverges from
“indoor bathroom”. These results highlight the importance of
semantic alignment in achieving accurate description scores.
5

--- Page 18 ---

DINO-HEAL Example, Action Hallucination
Clip 1
Clip 2
Question 1
Is the primary action in the video mixing the ingredients?
Question 2
Is the primary action in the video watching the oven?
Ground
Answer for Question 1 with Clip 1: Yes.
Truth
Answer for Question 1 with Clip 2: No.
Answer for Question 2 with Clip 1: No.
Answer for Question 2 with Clip 2: Yes.
Video-
ChatGPT
Answer for Question 1 with Clip 1: Yes, the primary action in the video is mixing the ingredients.
Answer for Question 1 with Clip 2: Yes, the primary action in the video is mixing the ingredients.
Answer for Question 2 with Clip 1: No. The man and the child are making cookies in the kitchen.
Answer for Question 2 with Clip 2: No.
Video-
ChatGPT
+ DINO-HEAL
Answer for Question 1 with Clip 1: Yes.
Answer for Question 1 with Clip 2: No.
Answer for Question 2 with Clip 1: No.
Answer for Question 2 with Clip 2: Yes.
Video-LLaVA
Answer for Question 1 with Clip 1: Yes.
Answer for Question 1 with Clip 2: Yes.
Answer for Question 2 with Clip 1: Yes.
Answer for Question 2 with Clip 2: Yes.
Video-LLaVA
+ DINO-HEAL
Answer for Question 1 with Clip 1: Yes.
Answer for Question 1 with Clip 2: No.
Answer for Question 2 with Clip 1: No.
Answer for Question 2 with Clip 2: Yes.
VideoLLaMA2
Answer for Question 1 with Clip 1: Yes.
Answer for Question 1 with Clip 2: Yes.
Answer for Question 2 with Clip 1: No.
Answer for Question 2 with Clip 2: Yes.
VideoLLaMA2
+ DINO-HEAL
Answer for Question 1 with Clip 1: Yes.
Answer for Question 1 with Clip 2: No.
Answer for Question 2 with Clip 1: No.
Answer for Question 2 with Clip 2: Yes.
Table 9. An example of the action hallucination category of VIDHALLUC dataset with and without DINO-HEAL. Green text indicates
correct answers, and red text indicates incorrect answers.
6

--- Page 19 ---

DINO-HEAL Example, Temporal Sequence Hallucination
Question
Below are two actions in the video:
Action A. gutting a fish
Action B. starting a fire
Sort these two actions in the order they occur in the video, and return which action happen before
which one. For example, ‘Action A before Action B’ or ‘Action B before Action A’. If you only
detect one action of these two in the video, return that action.
Ground Truth
BA.
Video-ChatGPT
In the video, the man is seen gutting a fish and starting a fire. The order of these two actions is not
clear, as they both occur simultaneously.
Video-ChatGPT
+ DINO-HEAL
In the video, the man starts a fire by striking a match on a piece of wood. After that, he goes to the
beach and starts gutting a fish.
Video-LLaVA
Action B. starting a fire.
Video-LLaVA
+ DINO-HEAL
Action B happens before Action A.
VideoLLaMA2
I only detect one action in the video, which is Action B: starting a fire.
VideoLLaMA2
+ DINO-HEAL
Action B. starting a fire happens before Action A. gutting a fish.
ShareGPT4Video
Answer: ’Action B happens before Action A’
ShareGPT4Video
+ DINO-HEAL
Answer: ’Action B happens before Action A’
VILA1.5
Action B. starting a fire happens before Action A. gutting a fish.
VILA1.5
+ DINO-HEAL
Action B. starting a fire happens before Action A. gutting a fish.
Table 10. An example from the temporal sequence hallucination category of VIDHALLUC dataset with and without DINO-HEAL. Green
text indicates correct answers, and red text indicates incorrect answers.
7

--- Page 20 ---

VIDHALLUC Example, Action Hallucination
Clip 1
Clip 2
Question 1
Is ironing wax on the ski the main activity in the video?
Question 2
Is the primary action in the video skiing?
Ground
Answer for Question 1 with Clip 1: No.
Truth
Answer for Question 1 with Clip 2: Yes.
Answer for Question 2 with Clip 1: Yes.
Answer for Question 2 with Clip 2: No.
Chat-
Univi [23]
Answer for Question 1 with Clip 1: No, the main activity in the video is skiing down a snowy slope.
Answer for Question 1 with Clip 2: No, the main activity in the video is not ironing wax on the ski.
The video showcases a person using a variety of tools and techniques to create snowboards.
Answer for Question 2 with Clip 1: Yes, the primary action in the video is skiing.
Answer for Question 2 with Clip 2: Yes, the primary action in the video is skiing.
PLLaVA [63]
Answer for Question 1 with Clip 1: Yes.
Answer for Question 1 with Clip 2: Yes.
Answer for Question 2 with Clip 1: Yes.
Answer for Question 2 with Clip 2: Yes.
Video-
Answer for Question 1 with Clip 1: Yes, the main activity in the video is ironing wax on the ski.
ChatGPT [39]
Answer for Question 1 with Clip 2: No, the main activity in the video is not ironing wax on the ski.
The video shows a man using a machine to scrape wood.
Answer for Question 2 with Clip 1: No, the primary action in the video is not skiing.
Answer for Question 2 with Clip 2: No, the primary action in the video is not skiing. The video
shows a man working on a piece of wood with a tool.
LLaVA-NeXT-
Video [72]
Answer for Question 1 with Clip 1: Yes.
Answer for Question 1 with Clip 2: Yes.
Answer for Question 2 with Clip 1: Yes.
Answer for Question 2 with Clip 2: Yes.
Table 11. An example from the action hallucination category of VIDHALLUC dataset. Green text indicates correct answers, and red text
indicates incorrect answers.
8

--- Page 21 ---

VIDHALLUC Example, Temporal Sequence Hallucination
Question
Below are two actions in the video:
Action A. unloading shingles onto the roof
Action B. removing old shingles
Sort these two actions in the order they occur in the video, and return which action happens before
which one. For example, ‘Action A before Action B’ or ‘Action B before Action A’. If you detect
only one of the two actions in the video, return that action.
Ground Truth
AB.
LLaVA-NeXT-
Video [72]
Action B. removing old shingles.
Chat-UniVi [23]
Based on the video, Action B (removing old shingles) occurs before Action A (unloading shingles
onto the roof).
Video-LLaVA [32]
Action B. removing old shingles happens before Action A. unloading shingles onto the roof.
PLLaVA [63]
Action B. removing old shingles.
Gemini-1.5-Pro [53]
The order of actions is BA:
1. **B. removing old shingles:** A person is shown using a shovel to remove old shingles from the
roof.
2. **A. unloading shingles onto the roof:** A crane is used to lift new shingles onto the roof.
GPT-4o [1]
BA.
Video-ChatGPT [39]
In the video, the person is first seen unloading shingles onto the roof, and then they are seen removing
old shingles. The order in which these actions occur is unloading shingles onto the roof first,
followed by removing old shingles.
ShareGPT4Video [6]
Answer: ‘Action A happens before Action B’.
VideoLLaMA2 [9]
Action A. unloading shingles onto the roof happens before Action B. removing old shingles.
VILA1.5 [33]
Action B. removing old shingles happens before Action A. unloading shingles onto the roof.
Table 12. An example from the temporal sequence hallucination category of the VIDHALLUC dataset. Green text indicates correct answers,
and red text indicates incorrect answers.
9

--- Page 22 ---

VIDHALLUC Example, Scene Transition Hallucination
Question
A scene change is defined as a significant transition in the overall environment or location within the
video. This means a change from one distinct setting to another, such as moving from a kitchen to
a living room or from indoors to outdoors. Watch the given video and determine if a scene change
occurs. If there is a scene change, respond in the format: ‘Scene change: Yes, Locations: from
[location1] to [location2].’ If no change occurs, respond: ‘Scene change: No, Locations: None’.
Ground Truth
Scene change: Yes; Locations: from in a swimming pool to in a bathtub.
Video-ChatGPT [39]
Scene change: No; Locations: None.
Scoredesc1 = 0, Scoredesc2 = 0
LLaVA-NeXT-
Video [72]
Scene change: Yes; Locations: from pool to bathtub.
Scoredesc1 = 0.727, Scoredesc2 = 0.892
Chat-UniVi [23]
Scene change: Yes; Locations: from indoor pool to outdoor pool.
Scoredesc1 = 0.514, Scoredesc2 = 0
Video-LLaVA [32]
Scene change: Yes; Locations: from the pool to the bathtub.
Scoredesc1 = 0.862, Scoredesc2 = 0.961
PLLaVA [63]
Scene change: Yes; Locations: from indoor bathroom to indoor bathroom.
Scoredesc1 = 0, Scoredesc2 = 0.266
ShareGPT4Video [6]
Scene change: No; Locations: None.
Scoredesc1 = 0, Scoredesc2 = 0
VideoLLaMA2 [9]
Scene change: Yes; Locations: from pool to bathtub.
Scoredesc1 = 0.727, Scoredesc2 = 0.892
VILA1.5 [33]
Scene change: Yes; Locations: from [location1] to [location2].
Scoredesc1 = 0, Scoredesc2 = 0
Gemini-1.5-Pro [53]
Scene change: Yes; Locations: from pool to bathtub.
Scoredesc1 = 0.727, Scoredesc2 = 0.892
GPT-4o [1]
Scene change: Yes; Locations: from a swimming pool to a bathtub.
Scoredesc1 = 0.941, Scoredesc2 = 0.946
Table 13. An example from the scene transition hallucination category of the VIDHALLUC dataset. Green text indicates correct answers,
and red text indicates incorrect answers. Each model’s description performance is evaluated using two scores: Scoredesc1 and Scoredesc2,
derived from Equation 16. These scores correspond to the model’s ability to describe the two distinct scenes in the video accurately. The
model’s overall Scoredesc2 is computed as the average of these two scores.
10

```
