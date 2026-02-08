---
title: "2025-Unknown-EmoBench-M Benchmarking Emotional Intelligence for Multimodal Large - PDF Extract"
source_pdf: "2025-Unknown-EmoBench-M Benchmarking Emotional Intelligence for Multimodal Large.pdf"
pages: 29
extracted_at: "2026-02-07T17:00:47.724937"
---

# PDF Extract: 2025-Unknown-EmoBench-M Benchmarking Emotional Intelligence for Multimodal Large

**Source PDF:** 2025-Unknown-EmoBench-M Benchmarking Emotional Intelligence for Multimodal Large.pdf
**Total Pages:** 29

---

## Content

```
--- Page 1 ---

EmoBench-M: Benchmarking Emotional Intelligence
for Multimodal Large Language Models
He Hu1,2∗, Yucheng Zhou3∗, Lianzhong You2 , Hongbo Xu2
Qianning Wang4 , Zheng Lian5 , Fei Richard Yu1 , Fei Ma2† , Laizhong Cui1,2†
1College of Computer Science and Software Engineering, Shenzhen University
2Guangdong Laboratory of Artificial Intelligence and Digital Economy (SZ)
3SKL-IOTSC, CIS, University of Macau
4Auckland University of Technology
5Institute of Automation, Chinese Academy of Sciences
huhe@gml.ac.cn, yucheng.zhou@connect.um.edu.mo, mafei@gml.ac.cn, cuilz@szu.edu.cn
Random
InternVL2.5-Chat-78B
GLM-4V-PLUS
Gemini-3.0-Pro
AffectGPT 
Humor Understanding
Sarcasm Detection
Laughter Reasoning
Socially Complex Emotion Analysis
Foundational Emotion Recognition
Emotion Intensity 
Analysis 
Opinion Sentiment 
Analysis
Speech Emotion 
Recognition 
Song Emotion 
Recognition
Stock Comment 
Emotion Analysis
Fine-Grained Dialog 
Emotion Analysis
Presentation Emotion 
Analysis
Face-Centric Dialog 
Emotion Analysis
Conversational Emotion 
& Intent Analysis
Multi-Party Dialog 
Emotion Recognition
Conversational Emotion Understanding
Q: The person in the video says: Mom, it's really uncomfortable. Hurry up, get 
on with it. Determine the emotion conveyed. Do not provide any additional 
explanations or extra content. Choose one of the following labels as your 
final answer: 
A. happy    B. sad    C. neutral    D. angry    E. worried    F. surprise
( Dialogue ）
The person in the video says: How did you even get in, you weirdo? -Yeah, 
yeah, really? Analyze the emotion and intent. Choose one emotion:
 A. happy   B. surprise   C. sad   D. disgust   E. anger   F.  fear   G. neutral
Choose one intent: 
A. questioning    B. agreeing    C. acknowledging    D. encouraging  
E. consoling    F. suggesting   G. wishing    H. neutral
 
Q: 
( Dialogue ）
Q: The person in the video says: There a new girlfriend in there? Cause you 
might need one. Does this statement express sarcasm? Do not provide any 
additional explanations or extra content. Choose one of the following labels 
as your final answer: 
A. true    B. false
( Dialogue ）
GPT-5.2
0
0.2
0.4
0.6
0.8
1
FGDEA
PEA
FCDEA
CEIA
MPDER
LR
SD
HU
SOER
SEA
OSA
EIA
SPER
Figure 1: Taxonomy for Evaluating Emotion Intelligence (EI) Capabilities of Multimodal Large Language Models (MLLMs): The diagram
outlines the categories of “Foundational Emotion Recognition”, “Conversational Emotion Understanding”, and “Socially Complex Emotion
Analysis” along with their respective evaluation scenarios. It also presents a performance comparison of different methods on the proposed
dataset EmoBench-M. The “Random” baseline refers to a heuristic approach that randomly selects labels from the available candidates.
Abstract
With the integration of multimodal large language
models (MLLMs) into robotic systems and various
AI applications, embedding emotional intelligence
(EI) capabilities into these models is essential for
enabling robots to effectively address human emo-
tional needs and interact seamlessly in real-world
scenarios. Existing static, text-based, or text-image
benchmarks overlook the multimodal complexi-
ties of real-world interactions and fail to capture
the dynamic, multimodal nature of emotional ex-
pressions, making them inadequate for evaluating
MLLMs’ EI. Based on established psychological
theories of EI, we build EmoBench-M, a novel
*Equal contribution.
†Corresponding author.
benchmark designed to evaluate the EI capabil-
ity of MLLMs across 13 valuation scenarios from
three key dimensions: foundational emotion recog-
nition, conversational emotion understanding, and
socially complex emotion analysis.
Evaluations
of both open-source and closed-source MLLMs on
EmoBench-M reveal a significant performance gap
between them and humans, highlighting the need
to advance their EI capabilities further. All bench-
mark resources, including code and datasets, are
publicly available at https://emo-gml.github.io/.
1
Introduction
Emotional Intelligence (EI), initially conceptualized by Sa-
lovey and Mayer [Salovey and Mayer, 1990], emphasizes
the ability to perceive, understand, regulate, and apply emo-
arXiv:2502.04424v3  [cs.CL]  27 Jan 2026

--- Page 2 ---

Benchmark
Psych-based? Task
Multimodality
Answer Type
Evaluator
EmotionBench [Huang et al., 2023a]
✓
1
Text
Multi-choice
Metric
SOUL [Deng et al., 2023]
✗
2
Text
Multi-choice & GEN.
Metric & LLM
EmoBench [Sabour et al., 2024]
✓
8
Text
Multi-choice
Metric
ChatGPT2AC [Qian et al., 2023]
✗
11
Text
Multi-choice
Metric
MOSABench [Song et al., 2024b]
✗
1
Text & Image
Multi-choice
Metric
SarcasmBench [Zhang et al., 2025]
✗
1
Text & Image
Multi-choice
Metric
MM-InstructEval [Yang et al., 2024b]
✗
6
Text & Image
Multi-choice
Metric
MC-EIU [Liu et al., 2024]
✗
1
Video & Audio & Text
Multi-choice
Metric
OV-MER [Lian et al., 2025b]
✗
1
Video & Audio & Text
Multi-choice
Metric
MER-UniBench [Lian et al., 2025a]
✗
3
Video & Audio & Text
Multi-choice
Metric
EmoBench-M (Ours)
✓
13
Video & Audio & Text
Multi-choice & GEN.
Metric & LLM
Table 1: Comparison of benchmarks related to emotion intelligence. “Psych-based?” refers to whether the benchmark is grounded in
psychological theories. “GEN.” stands for Generation task. Related work can be found in Appendix A.
tions in oneself and others. Recent advancements in mul-
timodal large language models (MLLMs) have significantly
improved human-computer interaction and natural language
understanding, and integrating MLLMs into robotic con-
trol systems has become increasingly prevalent [Sartor and
Thompson, 2024; Cheng et al., 2024a]. Incorporating EI ca-
pabilities within MLLMs is essential for improving robotic
performance in real-world environments. It will enable robots
to address human emotional needs better and ensure more ef-
fective interactions.
However, there is currently no universal benchmark to
evaluate the EI capabilities of MLLMs comprehensively. Ta-
ble 1 lists existing benchmarks for evaluating EI, demon-
strating that most are designed for text-only or text-image
EI tasks [Sabour et al., 2024; Yang et al., 2024b; Huang et
al., 2023a], and most are not grounded in established psy-
chological theories. Real-world MLLM-driven human-robot
interactions typically occur in dynamic, multimodal environ-
ments. Unlike static text and images, videos with audio pro-
vide richer and more complex multimodal information, in-
cluding dynamic facial expressions, body language, and vo-
cal tone, which more authentically convey the flow of emo-
tions and the interactive process. Evaluating MLLMs in mul-
timodal environments is crucial because it allows for a more
comprehensive understanding of their ability to interpret and
respond to diverse emotional cues in real-world scenarios.
Building on established psychological theories of EI [Sa-
lovey and Mayer, 1990; Huang et al., 2023b], we explore
the EI capabilities of MLLMs across three primary dimen-
sions: Level I: Foundational Emotion Recognition. This
dimension focuses on accurately identifying emotional states
through explicit signals such as facial expressions, vocal tone,
and body language [Ekman, 1992]. It also emphasizes the
extraction of emotional information from multimodal sig-
nals [Poria et al., 2019b]. Level II: Conversational Emo-
tion Understanding. Extending beyond foundational recog-
nition, this dimension requires the ability to track emotional
dynamics within conversations and to comprehend the con-
textual and situational meanings of emotions [Gross, 2002;
Poria et al., 2019a; Liu et al., 2024]. Level III: Socially
Complex Emotion Understanding.
Representing an ad-
vanced level of EI, this dimension involves understanding
emotions influenced not only by internal affective states but
also by external social and cultural contexts. It requires AI
systems to exhibit mentalizing capabilities, the ability to infer
others’ emotions and intentions based on environmental cues
[Frith and Frith, 2006; Zhang et al., 2025]. Building on these
three dimensions, we propose a novel multimodal EI bench-
mark, EmoBench-M, for MLLMs. As shown in Figure 1,
our benchmark includes 13 scenarios covering diverse con-
texts such as music and presentation, multi-party dialogues,
and social conversation. By utilizing multimodal data, i.e.,
video with audio, EmoBench-M enables a more comprehen-
sive evaluation of the EI of MLLMs. Moreover, controversial
samples were excluded after a thorough human review to en-
sure the quality of the benchmark.
To the best of our knowledge, EmoBench-M is the first
comprehensive benchmark to evaluate EI at the multimodal-
ity level.
We evaluate various open-source MLLMs (e.g.,
Video-LLaMA2 [Cheng et al., 2024b] and InternVL2.5
[Chen et al., 2024]) and closed-source MLLMs (e.g., GLM-
4V [Zeng et al., 2024] and Gemini [Reid et al., 2024]) on
EmoBench-M. Our findings indicate that the EI capability
of MLLMs in multimodal and realistic environments remains
substantially below human performance in many scenarios.
Moreover, we conduct an extensive evaluation of MLLMs
across varying model sizes and reasoning levels. We will
release our code and data to encourage further research in
MLLM’s EI.
2
EmoBench-M
2.1
Evaluation Taxonomy
To systematically evaluate MLLM EI capabilities, the eval-
uation focuses on three dimensions based on established
psychological theories of EI [Salovey and Mayer, 1990]:
“Foundational Emotion Recognition”, “Conversational Emo-
tion Understanding”, and “Socially Complex Emotion Anal-
ysis”. Table 2 details evaluation scenarios in each dimension.
Foundational Emotion Recognition
Foundational emotion recognition, a core aspect of Emo-
tional Intelligence (EI), focuses on identifying basic emo-
tions such as anger, happiness, and sadness [Ekman, 1992;
Scherer, 2005]. This dimension evaluates a MLLMs’ abil-
ity to extract and integrate emotional information from mul-
timodal signals (video, audio, and text) to recognize these

--- Page 3 ---

Evaluation Scenario
Data Source
Task
Num
Metric
Level I: Foundational Emotion Recognition
Song Emotion Recognition (SOER)
RAVDESS(song) [Livingstone and Russo, 2018]
6-CLS
500
ACC
Speech Emotion Recognition (SPER)
RAVDESS(speech) [Livingstone and Russo, 2018]
8-CLS
500
ACC
Opinion Sentiment Analysis (OSA)
CMU-MOSI [Zadeh et al., 2016]
3-CLS
500
ACC
Emotion Intensity Analysis (EIA)
CMU-MOSEI [Zadeh et al., 2018]
3-CLS
500
ACC
Stock Comment Emotion Analysis (SEA)
FMSA-SC [Song et al., 2024a]
5-CLS
250
ACC
Level II: Conversational Emotion Understanding
Fine-Grained Dialog Emotion Analysis (FGDEA)
MER2023 [Lian et al., 2023a]
6-CLS
411
ACC
Presentation Emotion Analysis (PEA)
CH-SIMSv2 [Liu et al., 2022]
3-CLS
500
ACC
Face-Centric Dialog Emotion Analysis (FCDEA)
CH-SIMS [Yu et al., 2020]
3-CLS
457
ACC
Conversational Emotion & Intent Analysis (CEIA)
MC-EIU [Liu et al., 2024]
7-&8-CLS
500
ACC
Multi-Party Dialog Emotion Recognition (MPDER)
MELD [Poria et al., 2019a]
7-CLS
500
ACC
Level III: Socially Complex Emotion Analysis
Humor Understanding (HU)
UR-FUNNY [Hasan et al., 2019]
2-CLS
448
ACC
Sarcasm Detection (SD)
MUStARD [Castro et al., 2019]
2-CLS
500
ACC
Laughter Reasoning (LR)
SMILE [Hyun et al., 2024]
GEN
80
LLM
Table 2: Emotion Recognition Tasks and Metrics. “n-CLS” denotes an n-class classification task, and “GEN” represents a generation task.
“Num” indicates the number of samples. “ACC” denotes accuracy. For the “Laughter Reasoning”, we employ an LLM as the evaluator,
and evaluation prompts are shown in Appendix G. To ensure fair and consistent comparisons in future research, we adopted the open-source
Qwen2.5-72B-Instruct [Yang et al., 2024a]. Details of the specific categories in the classification tasks are provided in the Appendix B.
Details of prompt are in Appendix F.
fundamental emotions, a crucial capability for higher-level
EI. The MLLMs’ proficiency in discerning emotions con-
veyed through speech, music, and video is assessed. Song
and Speech Emotion Recognition uses data sourced from
[Livingstone and Russo, 2018], which provides video clips
with audio-visual emotional cues. Opinion Sentiment Anal-
ysis utilizes data sourced from [Zadeh et al., 2016], focusing
on speech and facial expressions in opinion videos. Emo-
tion Intensity Analysis goes beyond simple polarity; data
sourced from the CMU-MOSEI dataset [Zadeh et al., 2018] is
used to assess both the emotional state and its intensity from
audio and video. This requires the model to identify spe-
cific emotion categories (e.g., happiness, sadness, anger) and
quantify their intensity levels across diverse video content.
Stock Comment Emotion Analysis employs data sourced
from [Song et al., 2024a], analyzing emotions expressed in
stock-related video comments.
Conversational Emotion Understanding
Conversational emotion understanding requires MLLMs to
track emotional dynamics and interpret their contextual sig-
nificance [Poria et al., 2019b; Hazarika et al., 2018]. This
involves identifying emotional shifts in multi-party conver-
sations, leveraging semantic and tonal cues, and adapting to
dynamic contexts, including inter-participant emotional inter-
play. Several scenarios in this dimension: Fine-grained Dia-
log Emotion Analysis (data source from [Lian et al., 2023a])
captures subtle emotional shifts. Face-centric Dialog Emo-
tion Analysis (data source from CH-SIMS [Yu et al., 2020])
focuses on facial expressions and verbal/visual cues in inter-
active, conversational settings. Presentation Emotion Anal-
ysis (data source from CH-SIMSv2 [Liu et al., 2022]) ex-
amines emotions in formal presentations.
Crucially, CH-
SIMSv2 extends CH-SIMS by encompassing broader pre-
sentation styles, multi-speaker scenarios, and more diverse
non-verbal cues. Conversational Emotion and Intent Analy-
sis (data source from [Liu et al., 2024]) detects emotions and
infers intentions. Multi-party Dialog Emotion Recognition
(data source from [Poria et al., 2019a]) analyzes multi-party
conversations, classifying seven emotions based on speech
and facial cues.
Socially Complex Emotion Analysis
Emotional expression is influenced by internal drives and ex-
ternal social/cultural contexts [Frith and Frith, 2006]. So-
cially complex emotion understanding is an advanced EI di-
mension, encompassing the ability to identify, comprehend,
and respond to nuanced emotions and social intentions in in-
tricate social scenarios. This dimension primarily evaluates
emotions arising in complex social contexts, requiring deeper
inference of emotions like humor, sarcasm, and latent feel-
ings based on social interactions and norms. Humor Under-
standing utilizes data sourced from [Hasan et al., 2019]. Sar-
casm Detection uses data sourced from [Castro et al., 2019].
Laughter Reasoning employs data sourced from [Hyun et al.,
2024] to analyze the complex emotions in various social situ-
ations.
2.2
Data Collection and Processing
The EmoBench-M benchmark was meticulously curated to
evaluate the EI capabilities of MLLMs across a diverse range
of tasks. As illustrated in Figure 2, the data collection and
processing pipeline involved a rigorous, formalized proce-
dure for data filtering and class balancing to ensure high qual-
ity and fairness.
Filtering and Quality Assurance.
To eliminate ambigu-
ous or mislabeled samples from the initial datasets, we im-
plemented a multi-reviewer verification process. Each sam-
ple underwent manual review by a panel of N = 3 graduate

--- Page 4 ---

Figure 2: Data Filtering and Label Verification Process. Bar charts
show original dataset label (red) and label from our reviewers (blue).
students with research experience in affective computing, fol-
lowing a unified annotation guideline. Let s be a sample from
an initial dataset Dinitial, and let yorig(s) be its original label.
Each reviewer i assigned an emotion label vi(s) from the set
of possible labels L.
We formalized the reviewers’ consensus using a majority
vote. For any given label l ∈L, the vote count from the
reviewers for sample s is given by:
C(l, s) =
N
X
i=1
I(vi(s) = l)
(1)
where I(·) is the indicator function, which is 1 if the condition
is true and 0 otherwise. The consensus label from the review-
ers, yrev(s), is the label that receives the maximum number of
votes:
yrev(s) = arg max
l∈L
C(l, s)
(2)
A sample s was retained only if the original label yorig(s)
matched the reviewers’ consensus label yrev(s). While emo-
tional perception can be inherently ambiguous, this strict fil-
tering strategy prioritizes label reliability over ambiguity to
ensure fair and consistent benchmarking. This filtering cri-
terion ensures that only samples with high inter-annotator
agreement and consistency with the original labels are in-
cluded. Consequently, the final filtered dataset, Dfiltered, is
defined as:
Dfiltered = {s ∈Dinitial | yorig(s) = yrev(s)}
(3)
This robust procedure guarantees that EmoBench-M is built
upon high-quality, unambiguous data, thereby enhancing the
benchmark’s reliability and validity.
Class Imbalance Correction.
To ensure a fair and un-
biased evaluation, we addressed potential class imbalances
within the filtered data. For each task, we capped the maxi-
mum number of test samples at 500. If the size of a filtered
dataset for a task, |Dfiltered|, exceeded this threshold, we per-
formed a targeted down-sampling procedure.
This procedure iteratively removes samples from the ma-
jority class until the dataset size is reduced to 500. Specif-
ically, in each step of the process, we identify the majority
class cmaj with the highest number of instances:
cmaj = arg max
c∈L
|Dc|
(4)
where |Dc| is the number of samples with label c in the cur-
rent dataset. A single sample is then randomly removed from
this majority class. This process is repeated until |Dfiltered| =
500. This method preserves the presence of minority classes
while creating a more balanced class distribution, which pre-
vents the benchmark from being skewed towards dominant
emotions and promotes better model generalization across the
full spectrum of emotions.
Dataset Statistics.
EmoBench-M encompasses tasks with
varying sample sizes, ranging from 80 to 500 samples per
task, as detailed in Table 2. Each task is designed to evaluate
different facets of emotional intelligence, spanning from ba-
sic emotion recognition to understanding more complex so-
cial emotions. Performance metric is accuracy (ACC), and
LLM-based evaluation is employed for generation tasks.
3
Experiments
3.1
Experimental Settings
Task
Formulation.
We
evaluate
all
MLLMs
on
EmoBench-M in a zero-shot setting to assess their in-
herent capabilities. For classification tasks, models predict
emotion categories directly from multimodal inputs (audio,
video, and text). For generative tasks, they produce detailed
emotional inferences or explanations. Prompts are carefully
standardized across models.
Models.
As shown in Table 9, we evaluate a diverse set of
LLMs, including both open-source and closed-source sys-
tems, to provide a comprehensive analysis of their multi-
modal emotional intelligence capabilities. The open-source
models include Qwen2-Audio [Chu et al., 2024], MiniCPM-
V [Yao et al., 2024], InternVL2.5 [Chen et al., 2024], Video-
LLaMA2 [Cheng et al., 2024b], and the emotion-specific
MLLM Emotion-LLaMA [Cheng et al., 2024a], covering pa-
rameter scales ranging from 4 B to 78 B. These models are de-
signed to handle tasks involving text, audio, video, and multi-
modal reasoning, showcasing cross-modal alignment and in-
teraction advancements. Closed-source models evaluated in-
clude the GLM-4V series [Zeng et al., 2024], Gemini series
[Reid et al., 2024], and GPT series [Singh et al., 2025] ac-
cessed via API. More details are in Appendix C.
3.2
Results and Findings
Tables 3, 4, and 5, present the performance of various models
the EmoBench-M. Closed-source models consistently out-
perform open-source ones. Gemini-3.0-Pro achieves the best
results in FER (69.3), CEU (62.3), SCEA (80.0)and overall
average (70.5). Among open-source models, Qwen2-Audio-
7B-Instruct leads in FER (59.9), while Qwen2.5-VL-72B per-
forms best in SCEA (72.5) and shows strong results overall.
Analysis of these results reveals several factors driving
the performance differences. (1) Model Scale and Modal-
ity Focus:
At smaller scales (4-8B), audio-centric mod-
els like Qwen2-Audio excel in FER (Table 3), highlight-
ing the primacy of speech for basic emotion analysis. At
larger scales (38-78B), models with stronger vision encoders,
such as InternVL, gain an advantage, suggesting that ef-
fective visual-textual fusion becomes increasingly critical as
model capacity increases.
(2) Native Multimodal Archi-
tecture:
The superior performance of the Gemini series

--- Page 5 ---

Method
Params
A
V
T
SOER
SPER
OSA
EIA
SEA
Avg.
ACC
WAF
ACC
WAF
ACC
WAF
ACC
WAF
ACC
WAF
ACC
WAF
Open-Source Model
InternVL2.5 [Chen et al., 2024]
4B
✓
✓
50.5
47.6
41.2
35.5
71.8
75.5
60.1
60.6
48.8
46.2
54.5
53.1
Video-LLaMA2 [Cheng et al., 2024b]
7B
✓
✓
52.4
47.7
42.4
35.0
31.0
39.8
50.2
46.8
50.8
38.6
45.4
41.6
Video-LLaMA2-16F [Cheng et al., 2024b]
7B
✓
✓
45.0
41.6
46.0
41.2
64.0
68.2
56.5
54.9
45.5
39.1
51.4
49.0
Qwen2-Audio-Instruct [Chu et al., 2024]
7B
✓
✓
65.8
59.8
71.7
65.1
66.2
72.9
59.6
58.9
36.4
36.1
59.9
58.6
Video-LLaMA2.1-AV [Cheng et al., 2024b]
7B
✓
✓
✓
50.4
42.2
37.7
30.5
73.0
76.4
57.6
58.2
33.2
33.6
50.4
48.2
LongVA-DPO [Zhang et al., 2024a]
7B
✓
✓
50.2
45.4
44.2
40.3
33.8
42.4
45.7
39.4
54.8
46.7
45.7
42.8
Qwen2.5-VL-Instruct [Bai et al., 2025]
7B
✓
✓
47.8
43.3
36.4
28.9
62.8
70.7
60.0
59.4
51.6
48.1
51.7
50.1
InternVideo2-Chat [Wang et al., 2024]
8B
✓
✓
55.2
50.5
44.0
35.1
45.4
55.1
56.0
55.3
52.4
42.0
50.6
47.6
MiniCPM-V-2.6 [Yao et al., 2024]
8B
✓
✓
26.6
20.5
21.8
16.2
56.5
65.3
50.5
48.4
44.5
37.0
40.0
37.5
InternVL2.5 [Chen et al., 2024]
8B
✓
✓
40.3
36.2
40.8
36.0
67.8
74.2
62.0
62.6
45.0
40.3
51.2
49.9
Qwen3-VL-Instruct[Yang et al., 2025]
8B
✓
✓
56.0
53.2
43.2
38.0
77.6
79.9
66.4
66.7
46.0
44.8
57.8
56.5
Qwen3-VL-Instruct-Thinking [Yang et al., 2025]
8B
✓
✓
31.6
25.3
21.6
15.8
81.0
81.6
61.8
60.5
37.5
40.2
46.7
44.7
Qwen2.5-Omni [Xu et al., 2025]
7B
✓
✓
✓
50.8
46.4
40.8
32.8
64.6
71.8
39.6
54.3
52.8
39.5
49.7
49.0
Emotion-LLaMA [Cheng et al., 2024a]
7B
✓
✓
✓
44.8
36.9
33.4
23.7
23.0
29.5
41.1
34.1
42.0
36.2
36.9
32.1
AffectGPT [Lian et al., 2025a]
7B
✓
✓
✓
40.2
34.3
31.2
25.0
77.6
78.9
57.8
73.0
29.6
30.3
47.3
48.3
Qwen2.5-VL-Instruct [Bai et al., 2025]
32B
✓
✓
44.2
41.0
34.0
28.1
66.8
73.9
64.2
63.8
47.6
47.6
51.4
50.9
InternVL2.5 [Chen et al., 2024]
38B
✓
✓
53.6
51.0
44.2
39.0
70.4
76.6
66.8
67.4
52.8
43.3
57.6
55.5
Video-LLaMA2 [Cheng et al., 2024b]
72B
✓
✓
56.0
54.8
44.2
41.3
49.2
60.1
50.3
46.1
53.6
45.7
50.7
49.6
InternVL2.5 [Chen et al., 2024]
78B
✓
✓
48.8
47.7
41.2
37.8
63.2
71.2
59.4
59.0
52.4
38.9
53.0
50.9
Qwen2.5-VL-Instruct [Bai et al., 2025]
72B
✓
✓
44.8
42.1
35.6
29.6
72.4
78.3
62.7
62.1
58.4
53.9
54.8
53.2
Closed-Source Model (API)
GLM-4V-PLUS [Zeng et al., 2024]
API
✓
✓
54.9
48.8
43.7
34.8
70.0
75.0
61.2
59.9
50.8
45.0
56.1
52.7
Gemini-1.5-Flash [Reid et al., 2024]
API
✓
✓
✓
62.0
60.1
52.0
50.1
75.0
78.6
65.0
64.8
44.4
46.5
59.7
60.0
Gemini-2.0-Flash [Team et al., 2024]
API
✓
✓
✓
63.3
62.2
55.8
53.5
68.8
75.8
63.5
63.0
55.6
48.6
61.4
60.6
Gemini-2.0-Flash-Thinking [Team et al., 2024]
API
✓
✓
✓
53.4
51.0
53.0
49.4
79.4
81.9
66.5
66.8
36.0
38.1
57.7
57.4
Gemini-3.0-Flash [Google, 2025]
API
✓
✓
✓
58.6
56.6
59.6
60.4
69.6
75.8
63.5
63.9
58.8
55.9
62.0
62.5
Gemini-3.0-Pro [Google, 2025]
API
✓
✓
✓
68.6
67.3
72.1
71.5
79.8
83.0
68.7
68.7
57.3
53.9
69.3
68.9
GPT-5.2 [Singh et al., 2025]
API
✓
✓
65.8
63.0
59.4
58.0
80.8
82.7
66.0
66.0
53.2
52.1
65.0
64.4
Table 3: Performance comparison of different methods on EmoBench-M (Foundational Emotion Recognition). Red and blue indicate the
best and the second best results among all models, respectively.
Method
Params
A
V
T
FGDEA
PEA
FCDEA
CEIA
MPDER
Avg.
ACC
WAF
ACC
WAF
ACC
WAF
ACC
WAF
ACC
WAF
ACC
WAF
Open-Source Model
InternVL2.5 [Chen et al., 2024]
4B
✓
✓
56.9
57.9
66.8
68.6
67.5
69.0
14.0
10.7
41.2
39.9
49.3
49.2
Video-LLaMA2 [Cheng et al., 2024b]
7B
✓
✓
45.7
46.4
45.2
50.2
42.7
45.2
8.1
5.0
30.7
27.9
34.5
34.9
Video-LLaMA2-16F [Cheng et al., 2024b]
7B
✓
✓
52.9
53.6
31.6
35.4
63.0
66.6
8.3
3.3
29.6
27.5
37.1
37.3
Qwen2-Audio-Instruct [Chu et al., 2024]
7B
✓
✓
51.6
50.1
59.0
63.7
55.6
59.1
7.6
6.0
42.7
40.8
43.3
43.9
Video-LLaMA2.1-AV [Cheng et al., 2024b]
7B
✓
✓
✓
51.5
48.5
68.2
69.0
67.6
67.7
6.5
4.4
36.6
34.4
46.1
44.8
LongVA-DPO [Zhang et al., 2024a]
7B
✓
✓
51.1
51.0
33.2
37.2
33.3
35.2
6.1
5.4
37.0
34.6
32.1
32.7
Qwen2.5-VL-Instruct [Bai et al., 2025]
7B
✓
✓
48.9
49.0
58.6
64.3
57.3
61.5
7.6
8.0
46.0
45.5
43.7
45.7
InternVideo2-Chat [Wang et al., 2024]
8B
✓
✓
58.0
55.4
50.8
56.2
49.2
53.2
8.9
6.2
34.2
31.6
40.2
40.5
MiniCPM-V-2.6 [Yao et al., 2024]
8B
✓
✓
48.9
49.0
58.6
63.7
57.1
61.3
11.7
9.0
39.2
37.5
43.1
44.1
InternVL2.5 [Chen et al., 2024]
8B
✓
✓
48.9
48.5
61.0
65.2
62.5
65.7
12.4
13.2
43.8
42.3
45.7
47.0
Qwen3-VL-Instruct [Yang et al., 2025]
8B
✓
✓
64.5
64.7
73.6
74.8
72.9
73.6
15.7
13.1
49.5
48.8
55.2
55.0
Qwen3-VL-Instruct-Thinking [Yang et al., 2025]
8B
✓
✓
52.8
51.7
73.0
73.7
67.0
67.7
6.5
6.3
39.0
38.3
47.7
47.5
Qwen2.5-Omni [Xu et al., 2025]
7B
✓
✓
✓
57.4
57.0
62.8
67.8
63.5
66.8
6.28
11.8
43.0
41.5
46.6
49.0
Emotion-LLaMA [Cheng et al., 2024a]
7B
✓
✓
✓
62.0
59.2
24.6
23.8
25.2
20.4
2.90
3.80
38.9
34.1
30.7
28.3
AffectGPT [Lian et al., 2025a]
7B
✓
✓
✓
55.5
56.8
75.4
75.3
72.0
71.1
10.3
18.7
39.8
40.7
50.6
52.5
Qwen2.5-VL-Instruct [Bai et al., 2025]
32B
✓
✓
57.6
57.5
64.8
69.1
62.8
66.5
12.0
11.7
48.1
48.5
49.1
50.7
InternVL2.5 [Chen et al., 2024]
38B
✓
✓
56.1
57.2
66.2
70.4
65.2
68.2
13.5
13.3
43.5
42.5
48.9
50.3
Video-LLaMA2 [Cheng et al., 2024b]
72B
✓
✓
43.1
41.2
42.8
49.5
41.4
45.4
11.6
12.5
47.6
48.1
37.3
39.3
InternVL2.5 [Chen et al., 2024]
78B
✓
✓
52.7
53.1
56.8
62.9
56.7
61.1
12.6
11.7
43.5
41.8
44.5
46.1
Qwen2.5-VL-Instruct [Bai et al., 2025]
72B
✓
✓
51.6
51.5
64.2
68.1
64.3
67.6
11.4
10.7
47.8
48.4
47.9
49.3
Closed-Source Model (API)
GLM-4V-PLUS [Zeng et al., 2024]
API
✓
✓
51.8
53.1
62.8
67.1
65.4
67.1
14.7
13.0
41.6
40.5
47.3
48.2
Gemini-1.5-Flash [Reid et al., 2024]
API
✓
✓
✓
67.2
67.2
72.3
74.3
73.2
74.0
15.6
15.8
49.5
49.2
55.6
56.1
Gemini-2.0-Flash [Team et al., 2024]
API
✓
✓
✓
64.2
64.8
70.9
73.6
71.9
73.8
11.1
12.7
48.7
48.5
53.4
54.7
Gemini-2.0-Flash-Thinking [Team et al., 2024]
API
✓
✓
✓
64.5
65.4
71.2
72.8
71.6
72.6
12.0
13.7
51.5
51.8
54.2
55.3
Gemini-3.0-Flash [Google, 2025]
API
✓
✓
✓
72.5
73.1
73.0
76.4
73.7
76.5
14.6
16.0
47.0
46.0
56.2
57.6
Gemini-3.0-Pro [Google, 2025]
API
✓
✓
✓
81.0
81.1
81.2
81.9
82.6
83.4
12.6
13.9
54.0
53.5
62.3
62.8
GPT-5.2 [Singh et al., 2025]
API
✓
✓
68.4
68.3
75.4
76.5
75.9
76.4
13.1
11.8
54.6
54.5
57.5
57.5
Table 4: Performance comparison of different methods on EmoBench-M (Conversational Emotion Understanding). Red and Blue indicate
the best and the second best results among all models, respectively.

--- Page 6 ---

Method
Params
A
V
T
HU
SD
LR
Avg.
ACC
WAF
ACC
WAF
B-4
R-L
BS
logic.
mm.
Total
ACC
WAF
Open-Source Model
InternVL2.5 [Chen et al., 2024]
4B
✓
✓
56.6
56.6
52.7
52.7
0.0
13.0
15.2
18.0
19.8
37.8
54.7
54.7
Video-LLaMA2 [Cheng et al., 2024b]
7B
✓
✓
60.7
59.0
55.8
54.8
4.6
29.8
36.3
33.9
33.5
67.4
58.3
56.9
Video-LLaMA2-16F [Cheng et al., 2024b]
7B
✓
✓
67.9
67.7
59.8
58.9
4.0
28.6
34.4
33.3
32.6
65.9
63.9
63.3
Qwen2-Audio-Instruct [Chu et al., 2024]
7B
✓
✓
52.5
37.4
53.3
41.4
4.0
26.4
32.8
30.8
30.4
61.2
52.9
39.4
Video-LLaMA2.1-AV [Cheng et al., 2024b]
7B
✓
✓
✓
54.7
50.3
53.4
45.0
11.5
33.5
89.7
20.0
20.5
40.5
54.1
47.7
LongVA-DPO [Zhang et al., 2024a]
7B
✓
✓
63.6
63.3
51.6
40.0
0.0
12.4
8.2
21.9
23.3
45.2
57.6
51.7
Qwen2.5-VL-Instruct [Bai et al., 2025]
7B
✓
✓
65.2
64.2
55.4
55.2
15.6
36.3
91.1
34.8
34.1
68.9
60.3
59.7
InternVideo2-Chat [Wang et al., 2024]
8B
✓
✓
68.1
67.8
61.2
61.0
19.5
45.8
92.5
31.9
29.6
61.5
64.7
64.4
MiniCPM-V-2.6 [Yao et al., 2024]
8B
✓
✓
55.1
53.9
49.6
38.6
2.3
27.5
39.1
32.9
32.0
64.9
52.4
46.3
InternVL2.5 [Chen et al., 2024]
8B
✓
✓
66.5
66.5
59.6
59.0
0.0
12.8
16.1
17.1
19.3
36.4
63.1
62.8
Qwen3-VL-Instruct [Yang et al., 2025]
8B
✓
✓
68.1
66.5
61.2
61.0
15.9
35.6
90.9
36.7
35.8
72.5
64.7
63.8
Qwen3-VL-Instruct-Thinking [Yang et al., 2025]
8B
✓
✓
67.2
63.5
59.9
53.0
4.1
22.7
85.7
38.1
36.9
75.1
63.6
58.3
Qwen2.5-Omni [Xu et al., 2025]
7B
✓
✓
✓
64.5
63.7
62.8
62.8
18.5
43.6
91.1
34.1
33.3
67.4
63.7
63.3
Emotion-LLaMA [Cheng et al., 2024a]
7B
✓
✓
✓
58.0
56.8
53.0
50.7
1.5
21.2
87.6
25.4
25.9
51.3
55.5
53.8
AffectGPT [Lian et al., 2025a]
7B
✓
✓
✓
18.5
26.5
35.4
41.1
4.9
19.8
86.3
22.8
25.1
47.9
27.0
33.8
InternVL2.5 [Chen et al., 2024]
32B
✓
✓
74.9
74.8
62.6
60.9
14.4
34.5
90.9
35.4
34.4
69.9
68.8
67.9
Video-LLaMA2 [Cheng et al., 2024b]
72B
✓
✓
67.9
64.5
51.0
35.5
7.4
35.4
48.0
34.0
32.6
66.6
59.5
50.0
InternVL2.5 [Chen et al., 2024]
78B
✓
✓
76.8
76.8
64.4
63.6
0.0
13.0
18.2
18.2
20.0
38.2
70.6
70.2
Qwen2.5-VL-Instruct [Bai et al., 2025]
72B
✓
✓
77.7
77.7
65.6
65.6
15.7
35.3
91.0
37.9
36.4
74.3
71.7
71.7
Closed-Source Model (API)
GLM-4V-PLUS [Zeng et al., 2024]
API
✓
✓
74.7
74.6
59.8
58.7
14.8
33.9
90.2
37.6
36.6
74.2
67.3
66.7
Gemini-1.5-Flash [Reid et al., 2024]
API
✓
✓
✓
72.8
71.0
58.6
52.2
13.8
33.5
90.2
37.9
36.4
74.3
65.7
61.6
Gemini-2.0-Flash [Team et al., 2024]
API
✓
✓
✓
79.2
79.2
64.8
62.3
15.3
33.6
90.4
36.5
35.4
71.9
72.0
70.8
Gemini-2.0-Flash-Thinking [Team et al., 2024]
API
✓
✓
✓
75.6
74.7
60.4
55.8
15.8
35.5
66.4
37.5
36.6
74.1
68.0
65.3
Gemini-3.0-Flash [Google, 2025]
API
✓
✓
✓
79.0
78.3
80.0
79.9
12.6
31.2
90.1
38.4
37.7
76.1
79.5
79.1
Gemini-3.0-Pro [Google, 2025]
API
✓
✓
✓
83.4
83.3
85.6
85.6
13.4
32.2
90.0
35.9
35.1
71.0
84.5
84.5
GPT-5.2 [Singh et al., 2025]
API
✓
✓
81.7
81.7
73.0
73.0
14.3
34.0
90.5
38.3
37.9
76.2
77.4
77.4
Table 5: Performance comparison of different methods on EmoBench-M (Socially Complex Emotion Analysis). “B-4”, “R-L”, and “BS”
denote BLEU-4 [Papineni et al., 2002], ROUGE-L [Lin, 2004], and BERTScore [Zhang et al., 2020], respectively. Red and Blue indicate
the best and the second best results among all models, respectively.
likely stems from its native multimodal design, which syn-
chronously processes video and audio streams. This holistic
approach is better suited for capturing the dynamic nature of
emotional expression compared to models that fuse modali-
ties at later stages. (3) Perception over Complex Reason-
ing:
Gemini-2.0-Flash-Thinking and Qwen3-VL-Instruct-
Thinking do not consistently outperform their base versions
and sometimes perform slightly worse (Table 6), suggesting
that emotion-centric tasks rely more on effective cross-modal
perception than on complex chain-of-thought reasoning. (4)
Emotion-specialized MLLMs:
Despite targeted emotion
training, Emotion-LLaMA and AffectGPT achieve improve-
ments on specific emotion-related tasks.
Emotion-specific
priors alone are insufficient to achieve robust emotional in-
telligence in complex, multimodal, and context-dependent
settings. (5) Limits of Comprehensive Emotional Under-
standing:
MLLMs exhibit relatively stronger performance
on SCEA compared to FER and CEU. However, despite this
relative advantage, their performance across all three tasks
remains markedly inferior to human benchmarks, underscor-
ing persistent limitations in capturing nuanced social cues,
long-range emotional dynamics, and context-dependent inter-
actions.
3.3
Analysis on Class-wise Performance
Figure 3 shows the class-wise performance of Gemini-3.0-
Pro across Foundational Emotion Recognition (FER), Con-
versational Emotion Understanding (CEU), and Socially
Complex Emotion Analysis (SCEA). In FER (SOER, SPER,
SEA, OSA, EIA), the model performs well on primary emo-
tions such as angry, happy, sad, and neutral, as well as coarse
sentiment categories like positive and negative, while con-
fusions persist between semantically adjacent categories, in-
cluding fearful versus sad, calm versus happy or neutral, and
fine-grained sentiment intensities. In CEU (FGDEA, PEA,
FCDEA, CEIA, MPDER), the model shows stable perfor-
mance on common emotions such as neutral and handles
structured intent categories reasonably well, whereas emo-
tions with higher contextual dependency, such as surprise,
and nuanced intent classes like encouraging and consoling
remain challenging. In SCEA (HU, SD), the model achieves
strong performance in humor understanding, but sarcasm de-
tection exhibits increased confusion, reflecting the difficulty
of recognizing subtle social cues. Gemini-3.0-Pro demon-
strates strong performance while continuing to struggle with
nuanced and overlapping categories in socially and contextu-
ally complex scenarios.
3.4
Analysis on Generation Metric
Table 7 shows cosine similarity and Pearson correla-
tion results for traditional metrics (BLEU-4, ROUGE-
L, BERTScore) and the open-source LLM Qwen2.5-72B-
Instruct with human judgments.
Among traditional met-
rics, BERTScore showed the highest consistency with human
evaluation, outperforming BLEU-4 and ROUGE-L. Notably,
Qwen2.5-72B-Instruct achieved superior results, highlighting
its ability to better align with human assessments in laughter
reasoning tasks. It reveals the limitations of traditional met-

--- Page 7 ---

angry
calm
fearful
happy
neutral
sad
angry
calm
fearful
happy
neutral
sad
0.80
0.00
0.07
0.06
0.07
0.00
0.00
0.30
0.00
0.46
0.10
0.14
0.04
0.00
0.58
0.01
0.04
0.34
0.00
0.00
0.00
1.00
0.00
0.00
0.01
0.09
0.07
0.01
0.64
0.17
0.02
0.07
0.01
0.05
0.06
0.78
(a) SOER
angry
calm
disgust
fearful
happy
neutral
sad
surprised
angry
calm
disgust
fearful
happy
neutral
sad
surprised
0.77
0.00
0.02
0.00
0.03
0.13
0.00
0.05
0.00
0.33
0.00
0.00
0.46
0.21
0.00
0.00
0.00
0.00
0.76
0.02
0.00
0.00
0.23
0.00
0.00
0.00
0.00
0.66
0.03
0.02
0.16
0.13
0.00
0.00
0.00
0.00
0.92
0.00
0.00
0.08
0.00
0.05
0.00
0.00
0.02
0.88
0.06
0.00
0.00
0.02
0.02
0.03
0.05
0.08
0.79
0.02
0.05
0.00
0.08
0.08
0.15
0.00
0.00
0.65
(b) SPER
neutral
strong negative
strong positive
weak negative
weak positive
neutral
strong negative
strong positive
weak negative
weak positive
0.77
0.00
0.01
0.12
0.10
0.29
0.06
0.00
0.65
0.00
0.56
0.00
0.00
0.00
0.44
0.42
0.00
0.00
0.58
0.00
0.56
0.00
0.00
0.07
0.38
(c) SEA
negative
neutral
positive
negative
neutral
positive
0.84
0.12
0.04
0.15
0.59
0.26
0.06
0.18
0.76
(d) OSA
negative
neutral
positive
negative
neutral
positive
0.70
0.26
0.05
0.08
0.84
0.07
0.05
0.44
0.51
(e) EIA
angry
happy
neutral
sad
surprise
worried
angry
happy
neutral
sad
surprise
worried
0.79
0.02
0.04
0.08
0.01
0.06
0.00
0.96
0.02
0.00
0.01
0.01
0.01
0.05
0.63
0.17
0.01
0.13
0.02
0.02
0.00
0.86
0.04
0.06
0.00
0.06
0.12
0.06
0.65
0.12
0.04
0.00
0.02
0.07
0.00
0.88
(f) FGDEA
negative
neutral
positive
negative
neutral
positive
0.89
0.09
0.02
0.30
0.66
0.05
0.06
0.16
0.78
(g) FCDEA
negative
neutral
positive
negative
neutral
positive
0.89
0.08
0.03
0.35
0.48
0.17
0.07
0.13
0.81
(h) PEA
happy
surprise
sad
disgust
anger
fear
neutral
happy
surprise
sad
disgust
anger
fear
neutral
0.78
0.01
0.05
0.01
0.00
0.04
0.09
0.36
0.41
0.01
0.01
0.01
0.05
0.14
0.26
0.05
0.49
0.07
0.04
0.03
0.05
0.14
0.19
0.21
0.14
0.17
0.00
0.14
0.21
0.24
0.20
0.08
0.21
0.04
0.03
0.32
0.15
0.26
0.04
0.06
0.11
0.06
0.41
0.14
0.25
0.03
0.05
0.01
0.11
(i) CEIA (emo.)
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
0.92
0.02
0.00
0.05
0.00
0.01
0.00
0.00
0.25
0.28
0.30
0.03
0.02
0.11
0.00
0.02
0.24
0.16
0.52
0.00
0.04
0.04
0.00
0.00
0.27
0.23
0.07
0.23
0.07
0.10
0.00
0.03
0.34
0.12
0.08
0.07
0.22
0.11
0.05
0.01
0.38
0.09
0.11
0.02
0.05
0.29
0.02
0.04
0.27
0.04
0.09
0.07
0.04
0.13
0.29
0.07
0.41
0.09
0.22
0.01
0.05
0.07
0.05
0.09
(j) CEIA (int.)
anger
disgust
fear
joy
neutral
sadness
surprise
anger
disgust
fear
joy
neutral
sadness
surprise
0.67
0.02
0.07
0.07
0.04
0.00
0.13
0.25
0.33
0.00
0.11
0.06
0.08
0.17
0.09
0.00
0.35
0.17
0.09
0.00
0.30
0.00
0.00
0.00
0.66
0.16
0.10
0.08
0.06
0.02
0.02
0.18
0.59
0.10
0.04
0.14
0.03
0.05
0.08
0.14
0.51
0.05
0.10
0.03
0.03
0.22
0.05
0.05
0.52
(k) MPDER
false
true
false
true
0.79
0.21
0.12
0.88
(l) HU
false
true
false
true
0.89
0.11
0.18
0.82
(m) SD
Figure 3: Confusion matrices for Gemini-3.0-Pro on each evaluation scenario of EmoBench-M.
Method
FER
CEU
SCEA
Avg.
Open-Source Model
Random
23.1
19.8
33.3
25.4
InternVL2.5-4B
54.5
49.3
49.0
50.9
Video-LLaMA2-7B
45.4
34.5
61.3
47.1
Qwen2-Audio-7B-Instruct
59.9
43.3
55.7
53.0
Video-LLaMA2.1-7B-16F
50.9
46.1
57.5
51.5
Video-LLaMA2.1-7B-AV
50.4
46.1
49.5
48.7
LongVA-DPO-7B
45.7
32.1
53.5
43.8
Qwen2.5-VL-Instruct-7B
51.7
43.7
63.2
52.9
InternVideo2-Chat-8B
50.6
40.2
63.6
51.5
MiniCPM-V-2.6-8B
40.0
43.1
56.5
46.5
InternVL2.5-8B
51.2
45.7
54.2
50.4
Qwen3-VL-Instruct-8B
57.8
55.2
67.3
60.1
Qwen3-VL-Instruct-Thinking-8B
46.7
47.7
67.4
53.9
Qwen2.5-Omni-7B
49.7
46.6
64.9
53.7
Emotion-LLaMA
36.9
30.7
54.1
40.6
AffectGPT
47.3
50.6
33.9
43.9
Qwen2.5-VL-Instruct-32B
51.4
49.1
69.1
56.7
InternVL2.5-38B
57.6
48.9
56.6
54.4
Video-LLaMA2-72B
50.7
37.3
61.8
49.9
InternVL2.5-78B
53.0
44.5
59.8
52.4
Qwen2.5-VL-Instruct-72B
54.8
47.9
72.5
57.8
Closed-Source Model (API)
GLM-4V-PLUS
56.1
47.3
69.6
57.7
Gemini-1.5-Flash
59.7
55.6
68.6
61.3
Gemini-2.0-Flash
61.4
53.4
72.0
62.3
Gemini-2.0-Flash-Thinking
57.7
54.2
70.0
60.6
Gemini-3.0-Flash
62.0
56.2
78.4
65.5
Gemini-3.0-Pro
69.3
62.3
80.0
70.5
GPT-5.2
65.0
57.5
77.0
66.5
Table 6: Performance comparison on EmoBench-M. Mean ACC
was used per dimension; LR total score was used in SCEA. Red and
Blue indicate the best and the second best results among all models,
respectively.
Metric
Cosine Sim.
Pearson Corr.
BLEU-4
0.7381
0.2934
ROUGE-L
0.8563
0.2947
BERTScore
0.8762
0.3199
Qwen2.5-72B-Instruct
0.9353
0.4042
Table 7: Cosine similarity and Pearson correlation between the
scores produced by traditional metrics or open-source LLM predic-
tions and human judgments on the laughter reasoning task.
Dimensions
1
3
5
Foundational Emotion Recognition
61.4 61.2 61.0
Conversational Emotion Understanding 53.4 54.0 54.1
Socially Complex Emotion Analysis
72.0 72.5 72.8
Table 8: Stability experiment of Gemini-2.0-Flash on three dimen-
sions, running predictions 1, 3, and 5 times.
rics and underscores the potential of LLM-based approaches
for more reliable evaluation.
3.5
Stability Analysis of MLLM
We analyze the stability of Gemini-2.0-Flash across three di-
mensions: FER, CEU, and SCEA. Stability is evaluated by
running predictions 1, 3, and 5 times, using majority voting
for final results (shown in Table 8). In FER, scores are 61.4,
61.2, and 61.0, with the highest at 61.4. For CEU, scores im-
prove from 53.4 to 54.1 across iterations. In SCEA, results
are 72.0, 72.5, and 72.8, considering only HU and SD sce-
narios due to the generative nature of this task. These results

--- Page 8 ---

demonstrate the model’s robust stability, with minor varia-
tions and improvements in complex emotional contexts.
4
Conclusion
We introduced EmoBench-M to evaluate the EI of MLLMs
across three key areas: Foundational Emotion Recognition,
Conversational Emotion Understanding, and Socially Com-
plex Emotion Understanding. Our results show that while
MLLMs perform reasonably well on basic emotion recogni-
tion, they struggle significantly with conversational and so-
cially complex emotional understanding. It reveals a crucial
gap between MLLM capabilities and human-level EI in dy-
namic, multimodal settings.
References
[Bai et al., 2025] Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wang,
Wenbin Ge, Sibo Song, Kai Dang, Peng Wang, and et al.
Qwen2.5-vl technical report. CoRR, abs/2502.13923, 2025.
[Cai et al., 2024] Rizhao Cai, Zirui Song, Chenyu Yi, and Alex C.
Kot. Benchlmm: Benchmarking cross-style visual capability of
large multimodal models. In ECCV 2024, volume 15108, pages
340–358, 2024.
[Castro et al., 2019] Santiago
Castro,
Devamanyu
Hazarika,
Ver´onica P´erez-Rosas, Roger Zimmermann, Rada Mihalcea,
and Soujanya Poria. Towards multimodal sarcasm detection (an
obviously
perfect paper).
In ACL 2019, pages 4619–4629,
2019.
[Chen et al., 2024] Zhe Chen, Weiyun Wang, Yue Cao, Yangzhou
Liu, Zhangwei Gao, Erfei Cui, Jinguo Zhu, Shenglong Ye, Hao
Tian, Zhaoyang Liu, et al. Expanding performance boundaries of
open-source multimodal models with model, data, and test-time
scaling. arXiv preprint arXiv:2412.05271, 2024.
[Cheng et al., 2024a] Zebang Cheng, Zhi-Qi Cheng, Jun-Yan He,
Kai Wang, Yuxiang Lin, Zheng Lian, Xiaojiang Peng, and
Alexander G. Hauptmann. Emotion-llama: Multimodal emotion
recognition and reasoning with instruction tuning. In NeurIPS
2024, 2024.
[Cheng et al., 2024b] Zesen Cheng, Sicong Leng, Hang Zhang,
Deli Zhao, and Lidong Bing.
Videollama 2:
Advancing
spatial-temporal modeling and audio understanding in video-
llms. CoRR, abs/2406.07476, 2024.
[Chu et al., 2024] Yunfei Chu, Haojie Wei, Xipin Wei, Zhifang
Guo, and et al.
Qwen2-audio technical report.
CoRR,
abs/2407.10759, 2024.
[Deng et al., 2023] Yue Deng, Wenxuan Zhang, Sinno Jialin Pan,
and Lidong Bing. SOUL: towards sentiment and opinion under-
standing of language. In EMNLP 2023, pages 8704–8711, 2023.
[Ekman, 1992] Paul Ekman. Are there basic emotions? 1992.
[Frith and Frith, 2006] Chris D Frith and Uta Frith. The neural basis
of mentalizing. Neuron, 50(4):531–534, 2006.
[Fu et al., 2023] Chaoyou Fu, Xu Lin, Zhenyu Qiu, and et al.
MME: A comprehensive evaluation benchmark for multimodal
large language models. CoRR, abs/2306.13394, 2023.
[Fu et al., 2024] Xingyu Fu, Yushi Hu, Wei-Chiu Ma, and Ranjay
Krishna. BLINK: multimodal large language models can see but
not perceive.
In ECCV 2024, volume 15081, pages 148–166,
2024.
[Google, 2025] Google.
Gemini 3 developer documentation.
https://ai.google.dev/gemini-api/docs/gemini-3, 2025. Accessed:
2026-01.
[Gross, 2002] James J Gross. Emotion regulation: Affective, cog-
nitive, and social consequences. Psychophysiology, 39(3):281–
291, 2002.
[Hasan et al., 2019] Md.
Kamrul
Hasan,
Wasifur
Rahman,
Md. Iftekhar Tanveer,
Louis-Philippe Morency,
and Mo-
hammed (Ehsan) Hoque. UR-FUNNY: A multimodal language
dataset for understanding humor.
In EMNLP-IJCNLP 2019,
pages 2046–2056, 2019.
[Hazarika et al., 2018] Devamanyu
Hazarika,
Soujanya
Poria,
Amir Zadeh, Erik Cambria, Louis-Philippe Morency, and Roger
Zimmermann.
Conversational memory network for emotion
recognition in dyadic dialogue videos. In NAACL, volume 2018,
page 2122. NIH Public Access, 2018.
[Huang et al., 2023a] Jen-tse Huang, Man Ho Lam, Eric John Li,
Shujie Ren, Wenxuan Wang, Wenxiang Jiao, Zhaopeng Tu, and
Michael R. Lyu.
Emotionally numb or empathetic?
evaluat-
ing how llms feel using emotionbench. CoRR, abs/2308.03656,
2023.
[Huang et al., 2023b] Jen-tse Huang, Man Ho Lam, Zhaopeng Tu,
and Michael R. Lyu. Emotionally numb or empathetic? evaluat-
ing how llms feel using emotionbench. CoRR, abs/2308.03656,
2023.
[Hurst et al., 2024] Aaron Hurst, Adam Lerer, Adam P Goucher,
Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila
Welihinda, Alan Hayes, Alec Radford, et al. Gpt-4o system card.
arXiv preprint arXiv:2410.21276, 2024.
[Hyun et al., 2024] Lee Hyun,
Kim Sung-Bin,
Seungju Han,
Youngjae Yu, and Tae-Hyun Oh.
SMILE: multimodal dataset
for understanding laughter in video with language models. In
NAACL 2024, pages 1149–1167, 2024.
[Li et al., 2024a] Bohao Li, Yuying Ge, Yi Chen, Yixiao Ge,
Ruimao Zhang, and Ying Shan. Seed-bench-2-plus: Benchmark-
ing multimodal large language models with text-rich visual com-
prehension. CoRR, abs/2404.16790, 2024.
[Li et al., 2024b] Chuhan Li,
Ziyao Shangguan,
Yilun Zhao,
Deyuan Li, Yixin Liu, and Arman Cohan. M3sciqa: A multi-
modal multi-document scientific QA benchmark for evaluating
foundation models. In EMNLP 2024, pages 15419–15446, 2024.
[Li et al., 2024c] Kunchang Li, Yali Wang, Ping Lou, Limin Wang,
and Yu Qiao. Mvbench: A comprehensive multi-modal video
understanding benchmark. In CVPR 2024, pages 22195–22206.
IEEE, 2024.
[Li et al., 2024d] Xiang Li, Yucheng Zhou, Laiping Zhao, Jing Li,
and Fangming Liu. Impromptu cybercrime euphemism detection.
arXiv preprint arXiv:2412.01413, 2024.
[Lian et al., 2023a] Zheng Lian, Haiyang Sun, Mingyu Xu, Kexin
Wang, and et al.
MER 2023: Multi-label learning, modality
robustness, and semi-supervised learning. In MM 2023, pages
9610–9614, 2023.
[Lian et al., 2023b] Zheng Lian, Licai Sun, and Jianhua Tao. GPT-
4V with emotion: A zero-shot benchmark for multimodal emo-
tion understanding. CoRR, abs/2312.04293, 2023.
[Lian et al., 2024] Zheng Lian, Licai Sun, Bin Liu, and Jianhua
Tao. Merbench: A unified evaluation benchmark for multimodal
emotion recognition. CoRR, abs/2401.03429, 2024.

--- Page 9 ---

[Lian et al., 2025a] Zheng Lian, Haoyu Chen, Lan Chen, Haiyang
Sun, Licai Sun, Yong Ren, Zebang Cheng, Bin Liu, Rui Liu, Xi-
aojiang Peng, et al. Affectgpt: A new dataset, model, and bench-
mark for emotion understanding with multimodal large language
models. arXiv preprint arXiv:2501.16566, 2025.
[Lian et al., 2025b] Zheng Lian, Haiyang Sun, Jiangyan Yi, and
Jianhua Tao.
OV-MER: towards open-vocabulary multimodal
emotion recognition. In Forty-second International Conference
on Machine Learning, ICML 2025, Vancouver, BC, Canada, July
13-19, 2025. OpenReview.net, 2025.
[Lin, 2004] Chin-Yew Lin. Rouge: A package for automatic eval-
uation of summaries. In Text summarization branches out, pages
74–81, 2004.
[Liu et al., 2022] Yihe Liu, Hua Xu, and Kai Gao. Make acous-
tic and visual cues matter: CH-SIMS v2.0 dataset and av-mixup
consistent module. In ICMI 2022, pages 247–258, 2022.
[Liu et al., 2024] Rui Liu, Haolin Zuo, Zheng Lian, Xiaofen Xing,
Bj¨orn W. Schuller, and Haizhou Li.
Emotion and intent joint
understanding in multimodal conversation:
A benchmarking
dataset. CoRR, abs/2407.02751, 2024.
[Livingstone and Russo, 2018] Steven R Livingstone and Frank A
Russo. The ryerson audio-visual database of emotional speech
and song (ravdess): A dynamic, multimodal set of facial and vo-
cal expressions in north american english. PloS one, 2018.
[Paech, 2023] Samuel J. Paech.
Eq-bench:
An emotional in-
telligence benchmark for large language models.
CoRR,
abs/2312.06281, 2023.
[Papineni et al., 2002] Kishore Papineni,
Salim Roukos,
Todd
Ward, and Wei-Jing Zhu. Bleu: a method for automatic evalua-
tion of machine translation. In ACL, 2002, pages 311–318. ACL,
2002.
[Poria et al., 2019a] Soujanya Poria, Devamanyu Hazarika, Erik
Cambria, and Rada Mihalcea. MELD: A multimodal multi-party
dataset for emotion recognition in conversations. In ACL 2019,
pages 527–536, 2019.
[Poria et al., 2019b] Soujanya Poria, Navonil Majumder, Rada Mi-
halcea, and Eduard Hovy. Emotion recognition in conversation:
Research challenges, datasets, and recent advances. IEEE access,
2019.
[Qian et al., 2023] Yushan Qian, Weinan Zhang, and Ting Liu. Har-
nessing the power of large language models for empathetic re-
sponse generation: Empirical investigations and improvements.
In EMNLP 2023, pages 6516–6528, 2023.
[Reid et al., 2024] Machel
Reid,
Nikolay
Savinov,
Denis
Teplyashin,
Dmitry
Lepikhin,
Timothy
P.
Lillicrap,
and
et al. Gemini 1.5: Unlocking multimodal understanding across
millions of tokens of context. CoRR, abs/2403.05530, 2024.
[Sabour et al., 2024] Sahand Sabour, Siyang Liu, Zheyuan Zhang,
and Minlie Huang. Emobench: Evaluating the emotional intelli-
gence of large language models. In ACL 2024, pages 5986–6004,
2024.
[Salovey and Mayer, 1990] Peter Salovey and John D Mayer. Emo-
tional intelligence.
Imagination, cognition and personality,
9(3):185–211, 1990.
[Sartor and Thompson, 2024] Sebastian Sartor and Neil Thomp-
son.
Neural scaling laws for embodied AI.
CoRR,
abs/2405.14005, 2024.
[Scherer, 2005] Klaus R Scherer. What are emotions? and how can
they be measured? Social science information, 44(4):695–729,
2005.
[Singh et al., 2025] Aaditya Singh, Adam Fry, AJ Ostrow, Akhila
Ananthram, et al.
Openai gpt-5 system card.
arXiv preprint
arXiv:2601.03267, 2025.
[Song et al., 2024a] Lingyun Song, Siyu Chen, Ziyang Meng,
Mingxuan Sun, and Xuequn Shang. FMSA-SC: A fine-grained
multimodal sentiment analysis dataset based on stock comment
videos. IEEE Trans. Multim., 26:7294–7306, 2024.
[Song et al., 2024b] Shezheng Song, Chengxiang He, Shasha Li,
Shan Zhao, Chengyu Wang, Tianwei Yan, Xiaopeng Li, Qian
Wan, Jun Ma, Jie Yu, and Xiaoguang Mao. Mosabench: Multi-
object sentiment analysis benchmark for evaluating multimodal
large language models understanding of complex image. CoRR,
abs/2412.00060, 2024.
[Team et al., 2024] LearnLM Team, Abhinit Modi, Aditya Srikanth
Veerubhotla, Aliya Rysbek, Andrea Huber, Brett Wiltshire,
Brian Veprek, Daniel Gillick, Daniel Kasenberg, Derek Ahmed,
et al. Learnlm: Improving gemini for learning. arXiv preprint
arXiv:2412.16429, 2024.
[Wang et al., 2024] Yi Wang, Kunchang Li, Guo Chen, Baoqi Pei,
and et al. Internvideo2: Scaling foundation models for multi-
modal video understanding. In ECCV 2024, volume 15143, pages
396–416, 2024.
[Xu et al., 2025] Jin Xu, Zhifang Guo, Jinzheng He, Hangrui Hu,
Ting He, Shuai Bai, Keqin Chen, Jialin Wang, Yang Fan, Kai
Dang, et al.
Qwen2. 5-omni technical report.
arXiv preprint
arXiv:2503.20215, 2025.
[Yang et al., 2024a] An Yang, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng
Liu, Fei Huang, Haoran Wei, et al. Qwen2. 5 technical report.
arXiv preprint arXiv:2412.15115, 2024.
[Yang et al., 2024b] Xiaocui Yang, Wenfang Wu, Xiaoming Fu,
and Soujanya Poria. Mm-instructeval: Zero-shot evaluation of
(multimodal) large language models on multimodal reasoning
tasks. CoRR, abs/2405.07229, 2024.
[Yang et al., 2025] An Yang, Anfeng Li, Baosong Yang, Beichen
Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chen-
gen Huang, Chenxu Lv, et al. Qwen3 technical report. arXiv
preprint arXiv:2505.09388, 2025.
[Yao et al., 2024] Yuan Yao, Tianyu Yu, Ao Zhang, Chongyi Wang,
Junbo Cui, Hongji Zhu, Tianchi Cai, and et al. Minicpm-v: A
GPT-4V level MLLM on your phone. CoRR, abs/2408.01800,
2024.
[Ying et al., 2024] Kaining Ying, Yue Yang, Hao Zhang, and et al.
Mmt-bench: A comprehensive multimodal benchmark for eval-
uating large vision-language models towards multitask AGI. In
ICML 2024, 2024.
[Yu et al., 2020] Wenmeng Yu, Hua Xu, Fanyang Meng, Jiyun Zou,
and Kaicheng Yang. CH-SIMS: A chinese multimodal sentiment
analysis dataset with fine-grained annotation of modality. In ACL
2020, pages 3718–3727, 2020.
[Zadeh et al., 2016] Amir Zadeh, Rowan Zellers, Eli Pincus, and
Louis-Philippe Morency.
MOSI: multimodal corpus of senti-
ment intensity and subjectivity analysis in online opinion videos.
CoRR, abs/1606.06259, 2016.
[Zadeh et al., 2018] Amir Zadeh, Paul Pu Liang, Soujanya Poria,
Erik Cambria, and Louis-Philippe Morency.
Multimodal lan-
guage analysis in the wild: CMU-MOSEI dataset and inter-
pretable dynamic fusion graph. In ACL 2018, pages 2236–2246,
2018.

--- Page 10 ---

[Zeng et al., 2024] Aohan Zeng, Bin Xu, Bowen Wang, Chenhui
Zhang, Da Yin, and et al.
Chatglm: A family of large lan-
guage models from GLM-130B to GLM-4 all tools.
CoRR,
abs/2406.12793, 2024.
[Zhang et al., 2020] Tianyi Zhang, Varsha Kishore, Felix Wu, Kil-
ian Q. Weinberger, and Yoav Artzi. Bertscore: Evaluating text
generation with BERT. In ICLR 2020, 2020.
[Zhang et al., 2024a] Peiyuan Zhang, Kaichen Zhang, Bo Li,
Guangtao Zeng, Jingkang Yang, and et al. Long context trans-
fer from language to vision. CoRR, abs/2406.16852, 2024.
[Zhang et al., 2024b] Yichi Zhang, Yao Huang, Yitong Sun, Chang
Liu, Zhe Zhao, Zhengwei Fang, Yifan Wang, Huanran Chen,
Xiao Yang, Xingxing Wei, et al.
Multitrust: A comprehen-
sive benchmark towards trustworthy multimodal large language
models.
Advances in Neural Information Processing Systems,
37:49279–49383, 2024.
[Zhang et al., 2025] Yazhou Zhang, Chunwang Zou, Zheng Lian,
Prayag Tiwari, and Jing Qin. Sarcasmbench: Towards evaluating
large language models on sarcasm understanding. IEEE Trans.
Affect. Comput., 16(4):2560–2578, 2025.
[Zhao et al., 2024] Weixiang Zhao, Chen Wei, and Bing Qin. Both
matter: Enhancing the emotional intelligence of large language
models without compromising the general intelligence. In ACL
2024, pages 11157–11176, 2024.
[Zhou et al., 2024a] Minxuan Zhou, Hao Liang, Wentao Zhang,
and Zenan Zhou.
Mathscape:
Evaluating mllms in multi-
modal math scenarios through a hierarchical benchmark. CoRR,
abs/2408.07543, 2024.
[Zhou et al., 2024b] Ting Zhou, Daoyuan Chen, Qirui Jiao, Bolin
Ding, Yaliang Li, and Ying Shen.
Humanvbench: Exploring
human-centric video understanding capabilities of mllms with
synthetic benchmark data.
arXiv preprint arXiv:2412.17574,
2024.
[Zhu et al., 2024] Deyao Zhu, Jun Chen, Xiaoqian Shen, Xiang Li,
and Mohamed Elhoseiny. Minigpt-4: Enhancing vision-language
understanding with advanced large language models. In ICLR
2024, 2024.
A
Related Work
A.1
Multimodal Large Language Models
With the success of LLMs in various natural language pro-
cessing (NLP) tasks, such as reasoning and euphemism de-
tection [Li et al., 2024d], numerous efforts have been made
to extend LLMs to multimodal areas, i.e., MLLMs, en-
abling them to process additional types of information, in-
cluding images, videos, and audio [Cheng et al., 2024b;
Yao et al., 2024]. MLLMs excel in multimodal perception
and reasoning and handle more diverse tasks with inputs from
different multimodality [Zhu et al., 2024; Wang et al., 2024].
For instance, Qwen2-Audio [Chu et al., 2024] specializes
in integrating audio and text, demonstrating strong perfor-
mance in auditory perception tasks. The MiniCPM-V [Yao
et al., 2024], LongVA [Zhang et al., 2024a], GLM [Zeng et
al., 2024], InternVL [Chen et al., 2024], and InternVideo2
[Wang et al., 2024] have made significant strides in vision
understanding and multimodal dialogue generation. Video-
LLaMA2 [Cheng et al., 2024b] not only focuses on vision
understanding but also enhances audio-video understanding
capabilities. Additionally, the Gemini [Reid et al., 2024], an
LLM natively supporting multimodal capabilities, can seam-
lessly understand, manipulate, and integrate information from
different modalities. Moreover, some works further improve
vision reasoning ability in MLLMs by visual dependency, in-
context learning.
A.2
Evaluation of Emotional Intelligence
Given that EI is essential for understanding and responding
to human emotions, many studies have focused on evaluating
the EI capabilities of LLMs. MERBench [Lian et al., 2024]
standardizes evaluation for multimodal emotion recognition
by addressing inconsistencies in feature extractors and offer-
ing a unified framework. It introduces MER2023 [Lian et al.,
2023a], a dataset focused on the Chinese language, emphasiz-
ing multi-label learning and robustness analysis. Moreover,
MC-EIU [Liu et al., 2024] offers a joint evaluation of emotion
and intent in multimodal conversations. MOSABench [Song
et al., 2024b] introduces a novel method for multi-object sen-
timent analysis, emphasizing the challenges MLLMs face in
handling spatial complexities.
[Lian et al., 2023b] evalu-
ates GPT-4’s visual capabilities in emotion recognition tasks
but reveals limitations in recognizing micro-expressions and
leveraging temporal data effectively. EmotionBench [Huang
et al., 2023b] employs emotional appraisal theory to evalu-
ate LLMs, exposing misalignments between LLM responses
and human emotional behaviors.
To deep dive into EI of
LLM, EIBench [Zhao et al., 2024] and EmoBench [Sabour
et al., 2024] are based on established psychological theo-
ries to evaluate LLM with various EI tasks, and they expose
significant gaps between current LLMs and human-like emo-
tional intelligence. In addition, EQ-Bench [Paech, 2023] and
SOUL [Deng et al., 2023] focus on nuanced EI aspects, in-
cluding emotion intensity prediction and justification gener-
ation, revealing performance disparities between small and
large models.
A.3
Multimodal Benchmarks for LLMs
The rapid development of Multimodal Large Language Mod-
els (MLLMs) has necessitated the creation of diverse bench-
marks to systematically evaluate their capabilities across per-
ception, reasoning, and application domains. MME [Fu et al.,
2023] and MMT-Bench [Ying et al., 2024] serve as compre-
hensive benchmarks for foundational multimodal tasks and
general-purpose intelligence across varied domains.
Mul-
tiTrust [Zhang et al., 2024b] evaluates trustworthiness, fo-
cusing on truthfulness, safety, robustness, fairness, and pri-
vacy risks. Moreover, HumanVBench [Zhou et al., 2024b]
and MVBench [Li et al., 2024c] center on human-centric
and temporal understanding in video content, exposing gaps
in MLLMs’ abilities to align cross-modal and temporal dy-
namics effectively. Specialized benchmarks have emerged to
tackle domain-specific challenges. For instance, MathScape
[Zhou et al., 2024a] targets multimodal mathematical reason-
ing, while M3SciQA [Li et al., 2024b] focuses on scientific
question answering. BenchLMM [Cai et al., 2024] evalu-
ates models under diverse style shifts, and BLINK [Fu et al.,
2024] targets core visual perception tasks that remain chal-
lenging for multimodal models. Furthermore, SEED-Bench-

--- Page 11 ---

2-Plus [Li et al., 2024a] assesses MLLMs’ abilities in text-
rich visual scenarios, such as interpreting charts and maps.
B
Details and Case of Datasets
This section provides an overview of the datasets used in our
experiments, highlighting the number of test samples and the
corresponding labels associated with each dataset. Table 10
summarizes this information, covering a wide range of emo-
tional and intent-based annotations across various modalities.
Visual examples for each dataset are provided in Figure 13-
16.
• RAVDESS (song & speech) : The RAVDESS dataset
includes both speech and song audio files annotated with
emotions such as neutral, calm, happy, sad, angry, and
fearful. The speech subset contains additional labels, in-
cluding surprised and disgust.
• CMU-MOSI and CMU-MOSEI: These datasets are
designed for multimodal sentiment analysis and include
three sentiment labels: neutral, positive, and negative.
• FMSA-SC: This dataset captures fine-grained sentiment
annotations with labels such as weak negative, strong
negative, neutral, weak positive, and strong positive.
• MER2023:
Designed for emotion recognition, this
dataset provides six emotion categories: happiness, sad-
ness, anger, surprise, neutral, and calm.
• CH-SIMSv2 and CH-SIMS: These datasets, used for
sentiment analysis in Chinese, are annotated with three
labels: neutral, negative, and positive.
• MC-EIU: This dataset offers both emotion annotations
(happy, surprise, sad, disgust, anger, fear, neutral) and
intent annotations (questioning, agreeing, acknowledg-
ing, encouraging, consoling, suggesting, wishing, neu-
tral).
• MELD: This multimodal dataset includes seven emo-
tion labels: neutral, surprise, fear, sadness, joy, disgust,
and anger.
• UR-FUNNY and MUStARD: Both binary-labeled
multimodal datasets. UR-FUNNY is used for humor de-
tection, while MUStARD is designed for sarcasm detec-
tion, with annotations of true or false.
• SMILE: A small-scale dataset focusing on humor com-
prehension, annotated with explanations of why the au-
dience laughed.
Table 10 provides detailed statistics on the test samples and
label distributions for each dataset.
C
Model Configuration
The configuration details of the models evaluated on
EmoBench-M are summarized in Table 9. The table pro-
vides a detailed comparison of key hyperparameters, includ-
ing top-p and top-k sampling values, temperature settings,
and VRAM requirements. For models accessed via APIs, the
VRAM is denoted as “API”, reflecting their closed-source na-
ture and cloud-based deployment. The evaluated models en-
compass a range of architectures, from smaller-scale models,
Method
top-p top-k temp. VRAM
InternVL2.5-4B [Chen et al., 2024]
1.0
50
1.0
14G
Video-LLaMA2-7B [Cheng et al., 2024b]
0.8
20
0.7
19G
Video-LLaMA2-7B-16F [Cheng et al., 2024b]
0.8
20
0.7
19G
Qwen2-Audio-7B-Instruct [Chu et al., 2024]
0.5
20
0.7
33G
Video-LLaMA2.1-7B-16F [Cheng et al., 2024b]
0.8
20
0.7
22G
Video-LLaMA2.1-7B-AV [Cheng et al., 2024b]
0.8
20
0.7
21G
LongVA-DPO-7B [Zhang et al., 2024a]
1.0
50
1.0
21G
Qwen2.5-VL-Instruct-7B [Bai et al., 2025]
0.8
20
0.7
17G
InternVideo2-Chat-8B [Wang et al., 2024]
1.0
50
1.0
17G
MiniCPM-V-2.6-8B [Yao et al., 2024]
0.8
100
0.7
19G
InternVL2.5-8B [Chen et al., 2024]
1.0
50
1.0
24G
Qwen3-VL-Instruct-8B [Yang et al., 2025]
0.95
20
0.6
18G
Qwen3-VL-Instruct-Thinking-8B [Yang et al., 2025]
0.8
20
0.7
18G
Qwen2.5-Omni-7B [Xu et al., 2025]
1.0
50
1.0
36G
Emotion-LLaMA [Cheng et al., 2024a]
0.6
-
0.9
16G
AffectGPT [Lian et al., 2025a]
0.9
-
1.0
16G
Qwen2.5-VL-Instruct-32B [Bai et al., 2025]
0.8
20
0.7
63G
InternVL2.5-38B [Chen et al., 2024]
1.0
50
1.0
73G
Video-LLaMA2-72B [Cheng et al., 2024b]
0.8
20
0.7
148G
InternVL2.5-78B [Chen et al., 2024]
1.0
50
1.0
168G
Qwen2.5-VL-Instruct-72B [Bai et al., 2025]
0.8
20
0.7
147G
GLM-4V-PLUS [Zeng et al., 2024]
0.6
-
0.8
API
Gemini-1.5-Flash [Reid et al., 2024]
0.95
40
1.0
API
Gemini-2.0-Flash [Team et al., 2024]
0.95
40
1.0
API
Gemini-2.0-Flash-Thinking [Team et al., 2024]
0.95
64
1.0
API
Gemini-3.0-Flash [Google, 2025]
0.95
64
1.0
API
Gemini-3.0-Pro [Google, 2025]
0.95
64
1.0
API
GPT-5.2 [Hurst et al., 2024]
0.9
-
1.0
API
Table 9: Model configuration evaluated on EmoBench-M.
such as InternVL2.5-4B [Chen et al., 2024], to large-scale
variants like InternVL2.5-78B [Chen et al., 2024]. Notewor-
thy configurations include Video-LLaMA2.1-AV-7B [Cheng
et al., 2024b], which incorporates audiovisual processing,
and Gemini-2.0-Flash-Thinking [Reid et al., 2024], which
features enhanced reasoning capabilities. Most models ex-
hibit consistent sampling parameters (e.g., top-p and temper-
ature), ensuring a standardized basis for comparison. The
VRAM requirements reflect the computational demands of
these models, ranging from 14 GB for smaller models to 168
GB for the largest configurations.
In contrast, API-based
models provide an accessible option for users, particularly
when local resources are constrained, albeit at the cost of re-
duced transparency due to their closed-source nature.
D
Details on Stability Analysis of MLLM
Table 11 shows the results of stability experiments conducted
on Gemini-2.0-Flash. The analysis evaluates the model’s per-
formance across different numbers of prediction iterations (1,
3, and 5), with the final output determined through a major-
ity voting mechanism.
Scenarios assessed include SOER,
SPER, OSA, EIA, SCEA, FGDEA, PEA, FCDEA, CEIA,
MPDER, HU, and SD. The results demonstrate consistent
performance across different iteration counts, with minimal
variation observed in most metrics. For instance, the perfor-
mance on SOER shows only a slight fluctuation, ranging from
63.3 in the single iteration setup to 63.8 in the five-iteration
case. Similarly, performance on SPER and EIA exhibit sta-
ble trends, reinforcing the model’s robustness against runtime
variability.

--- Page 12 ---

Dataset
# Test samples
Labels
RAVDESS (song)
500
neutral, calm, happy, sad, angry, fearful
RAVDESS (speech)
500
neutral, calm, happy, sad, angry, fearful, surprised, disgust
CMU-MOSI
500
neutral, negative, positive
CMU-MOSEI
500
neutral, negative, positive
FMSA-SC
250
weak negative, strong negative, neutral, strong positive, weak positive
MER2023
411
happiness, sadness, anger, surprise, neutral, calm
CH-SIMSv2
500
neutral, negative, positive
CH-SIMS
457
neutral, negative, positive
MC-EIU
500
emotion: happy, surprise, sad, disgust, anger, fear, neutral
intent: questioning, agreeing, acknowledging, encouraging, consoling,
suggesting, wishing, neutral
MELD
500
neutral, surprise, fear, sadness, joy, disgust, anger
UR-FUNNY
448
true, false
MUStARD
500
true, false
SMILE
80
The audience laughed because...
Table 10: Overview of datasets, test samples, and emotion/intent labels.
Scenarios SOER SPER OSA EIA SCEA FGDEA PEA FCDEA CEIA MPDER HU
SD
1
63.3
55.8
68.8 63.5
55.6
64.2
70.9
71.9
11.1
48.7
79.2 64.8
3
64.6
55.4
67.8 63.4
54.8
66.4
71.3
71.9
11.1
49.5
79.2 65.8
5
63.8
54.8
69.0 63.4
54.0
66.2
72.1
72.1
11.1
48.9
79.7 66.0
Table 11: Stability experiment of Gemini-2.0-Flash on different scenarios, running predictions 1, 3, and 5 times, with the majority voting to
obtain the final result.
E
More Analysis on Class-wise Performance
For class-wise performance, confusion matrices for more
models can be found in Figure 17-35.

--- Page 13 ---

The person in video says: After all, I can't do it myself. Determine the emotion conveyed. Do not 
provide any additional explanations or extra content. Choose one of the following labels as your final 
answer:
A. neutral    B. negative    C. positive. 
Question
( Speech ）
Figure 4: Example of CH-SIMS dataset.
The person in video says: I think it's really good. Determine the emotion conveyed. Do not provide 
any additional explanations or extra content. Choose one of the following labels as your final answer:  
A. neutral    B. negative    C. positive. 
Question
( Speech ）
Figure 5: Example of CMU-MOSEI dataset.
The person in video says: IM JUST KINDA LIKE NO THIS IS GOING TO FAR. Determine the 
emotion conveyed. Do not provide any additional explanations or extra content. Choose one of the 
following labels as your final answer: 
A. neutral    B. negative    C. positive. 
Question
( Speech  ）
Figure 6: Example of CMU-MOSI dataset.

--- Page 14 ---

The person in video says: Democracy and combination are the core benchmarks of Ningde
Era. In fact, these two are the core benchmarks. So if we go to dig some second tier mines, 
such as lithium batteries, we are talking about upstream mines. Just keep an eye on the mines 
in your area. Determine the emotion conveyed. Do not provide any additional explanations or 
extra content. Choose one of the following labels as your final answer: 
A .weak negative    B. strong negative    C. neutral    D. strong positive    E. weak positive
Question
( Speech )
Figure 7: Example of FMSA-SC dataset.
The person in video says: How did you even get in, you weirdo? -Yeah, yeah, really? Analyze the 
emotion and intent. Choose one emotion:
A. happy   B. surprise   C. sad   D. disgust   E. anger   F.  fear   G. neutral. 
Choose one intent: 
A. questioning
B. agreeing    C. acknowledging    D. encouraging  
E. consoling    F. suggesting   G. wishing    H. neutral.
Question
( Dialogue )
Figure 8: Example of MC-EIU dataset.
The person in video says: Who told you that? Please watch the provided video and determine the 
emotion it conveys. Do not provide any additional explanations or extra content. Choose one of the 
following labels as your final answer: 
A. neutral    B. surprise    C. fear    D. sadness    E. joy    F. disgust    G. anger.
Question
( Dialogue ）
Figure 9: Example of MELD dataset.

--- Page 15 ---

The person in video says: Mom, it's really uncomfortable. Hurry up, get on with it. Determine the 
emotion conveyed. Do not provide any additional explanations or extra content. Choose one of the 
following labels as your final answer: 
A. happy    B. sad    C. neutral    D. angry    E. worried    F. surprise
Question
( Dialogue ）
Figure 10: Example of MER2023 dataset.
The person in the video says: There a new girlfriend in there? Cause you might need one. Does this 
statement express sarcasm? Do not provide any additional explanations or extra content. Choose one 
of the following labels as your final answer: 
A. true    B. false.
Question
( Dialogue ）
Figure 11: Example of MUStARD dataset.
Please watch the provided video and determine the emotion it conveys. Do not provide any additional 
explanations or extra content. Choose one of the following labels as your final answer: 
A. neutral    B. calm    C. happy    D. sad    E. angry    F. fearful. 
Question
( Song ）
Figure 12: Example of RAVDSS-song dataset.

--- Page 16 ---

The person in video says: When you die, I'll burn paper to tell you. Goodbye, bastard. Determine the 
emotion conveyed. Do not provide any additional explanations or extra content. Choose one of the 
following s your final answer: 
A. neutral    B. negative    C. positive
Question
( Dialogue ）
Figure 13: Example of CH-SIMSv2 dataset.
Please watch the provided video and determine the emotion it conveys. Do not provide any additional 
explanations or extra content. Choose one of the following labels as your final answer:
A. neutral    B. calm    C. happy    D. sad    E. angry    F. fearful    G. surprised    H. disgust. 
Question
( Speech ）
Figure 14: Example of RAVDSS-speech dataset.
The context sentences in the video is: that makes a good cartoon, but what are you going to do with a 
flat track pad those square things there's nothing i can do as a cartoonist, well i know the world is flat 
now, that's true, and the internet has reached every corner of the world the poorest the remotest places. 
The punchline sentence in the video is: every village in africa now has a cyber cafe. Does this statement 
express humor? Do not provide any additional explanations or extra content. Choose one of the 
following labels as your final answer: 
A. true    B. false
Question
( Speech )
Figure 15: Example of UR-FUNNY dataset.

--- Page 17 ---

Reasoning task: You are to answer why the audience laughed given the video clip. The video clip from BBT 
with multimodal information (Utterance, Facial Action Units, Video caption, Acoustic features (6 dimension; 
1.mean of F0 contour, 2.var of F0 contour, 3.mean of energy contour, 4.var of energy contour, 5.jitter, 
6.shimmer)) is given. The audience laughing moment is marked as (audience laughing) in certain utterance. 
Explain why audience laughed given the conversation, at most 40 words, starting with The audience 
laughed because .
The audience laughed because Sheldon offered his epinephrine to Howard, indicating his lack of social 
awareness and humorously inappropriate response to Howard's question about peanut oil.
Question
(Dialogue ）
Figure 16: Example of SMILE dataset.

--- Page 18 ---

angry
calm
fearful
happy
neutral
sad
angry
calm
fearful
happy
neutral
sad
0.77
0.00
0.04
0.05
0.07
0.07
0.00
0.17
0.00
0.48
0.19
0.16
0.08
0.00
0.48
0.05
0.06
0.33
0.00
0.00
0.00
0.98
0.00
0.02
0.00
0.02
0.05
0.02
0.71
0.20
0.02
0.04
0.01
0.02
0.06
0.84
(a) SOER
angry
calm
disgust
fearful
happy
neutral
sad
surprised
angry
calm
disgust
fearful
happy
neutral
sad
surprised
0.61
0.02
0.06
0.02
0.05
0.10
0.13
0.02
0.00
0.21
0.00
0.00
0.61
0.11
0.06
0.00
0.02
0.00
0.65
0.00
0.00
0.00
0.34
0.00
0.02
0.02
0.03
0.32
0.06
0.10
0.29
0.16
0.00
0.00
0.00
0.00
1.00
0.00
0.00
0.00
0.00
0.09
0.00
0.00
0.05
0.67
0.18
0.02
0.00
0.03
0.03
0.00
0.08
0.03
0.82
0.00
0.02
0.00
0.08
0.00
0.31
0.06
0.06
0.47
(b) SPER
neutral
strong negative
strong positive
weak negative
weak positive
neutral
strong negative
strong positive
weak negative
weak positive
0.65
0.02
0.02
0.18
0.13
0.29
0.18
0.00
0.53
0.00
0.44
0.00
0.12
0.06
0.38
0.38
0.05
0.00
0.54
0.03
0.47
0.00
0.00
0.06
0.47
(c) SEA
negative
neutral
positive
negative
neutral
positive
0.87
0.10
0.03
0.30
0.57
0.13
0.13
0.13
0.74
(d) OSA
negative
neutral
positive
negative
neutral
positive
0.71
0.26
0.03
0.14
0.78
0.08
0.07
0.45
0.49
(e) EIA
angry
happy
neutral
sad
surprise
worried
angry
happy
neutral
sad
surprise
worried
0.80
0.04
0.03
0.08
0.01
0.05
0.06
0.83
0.05
0.01
0.00
0.04
0.08
0.05
0.48
0.20
0.01
0.18
0.10
0.02
0.02
0.66
0.02
0.18
0.28
0.06
0.00
0.06
0.44
0.17
0.28
0.00
0.04
0.02
0.02
0.65
(f) FGDEA
negative
neutral
positive
negative
neutral
positive
0.86
0.11
0.03
0.42
0.52
0.06
0.15
0.15
0.70
(g) FCDEA
negative
neutral
positive
negative
neutral
positive
0.86
0.10
0.04
0.34
0.47
0.19
0.11
0.18
0.71
(h) PEA
happy
surprise
sad
disgust
anger
fear
neutral
happy
surprise
sad
disgust
anger
fear
neutral
0.52
0.12
0.08
0.03
0.06
0.02
0.18
0.13
0.54
0.03
0.06
0.04
0.03
0.18
0.08
0.21
0.25
0.09
0.15
0.07
0.15
0.07
0.22
0.07
0.29
0.12
0.00
0.22
0.04
0.27
0.07
0.13
0.35
0.01
0.13
0.04
0.26
0.04
0.00
0.24
0.15
0.26
0.23
0.15
0.12
0.10
0.12
0.01
0.26
(i) CEIA (emo.)
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
0.86
0.01
0.06
0.01
0.00
0.04
0.00
0.02
0.11
0.20
0.55
0.00
0.00
0.11
0.00
0.04
0.00
0.04
0.96
0.00
0.00
0.00
0.00
0.00
0.04
0.00
0.61
0.21
0.07
0.07
0.00
0.00
0.15
0.03
0.37
0.10
0.12
0.21
0.00
0.03
0.28
0.02
0.36
0.04
0.00
0.26
0.00
0.04
0.24
0.00
0.36
0.12
0.02
0.12
0.10
0.05
0.24
0.00
0.51
0.03
0.02
0.08
0.02
0.10
(j) CEIA (int.)
anger
disgust
fear
joy
neutral
sadness
surprise
anger
disgust
fear
joy
neutral
sadness
surprise
0.65
0.03
0.00
0.08
0.10
0.04
0.10
0.37
0.38
0.03
0.04
0.04
0.09
0.04
0.12
0.02
0.44
0.10
0.04
0.14
0.14
0.06
0.01
0.01
0.69
0.10
0.03
0.10
0.08
0.03
0.03
0.21
0.48
0.07
0.10
0.14
0.04
0.07
0.08
0.08
0.52
0.06
0.13
0.02
0.02
0.14
0.05
0.03
0.60
(k) MPDER
false
true
false
true
0.82
0.18
0.19
0.81
(l) HU
false
true
false
true
0.73
0.27
0.27
0.73
(m) SD
Figure 17: Confusion matrices for GPT-5.2 on each evaluation scenario of EmoBench-M.
angry
calm
fearful
happy
neutral
sad
angry
calm
fearful
happy
neutral
sad
0.75
0.12
0.07
0.00
0.04
0.02
0.00
0.73
0.00
0.14
0.04
0.08
0.10
0.10
0.41
0.04
0.05
0.31
0.00
0.08
0.01
0.90
0.00
0.00
0.00
0.75
0.02
0.01
0.09
0.12
0.00
0.30
0.02
0.02
0.01
0.64
(a) SOER
angry
calm
disgust
fearful
happy
neutral
sad
surprised
angry
calm
disgust
fearful
happy
neutral
sad
surprised
0.53
0.15
0.02
0.02
0.02
0.19
0.02
0.06
0.00
0.60
0.00
0.00
0.08
0.31
0.02
0.00
0.03
0.00
0.61
0.02
0.00
0.03
0.31
0.00
0.02
0.02
0.02
0.45
0.00
0.10
0.18
0.23
0.00
0.00
0.00
0.00
0.84
0.02
0.03
0.11
0.00
0.35
0.00
0.00
0.00
0.53
0.08
0.05
0.00
0.06
0.02
0.00
0.06
0.15
0.68
0.03
0.06
0.06
0.05
0.05
0.08
0.16
0.00
0.53
(b) SPER
neutral
strong negative
strong positive
weak negative
weak positive
neutral
strong negative
strong positive
weak negative
weak positive
0.78
0.00
0.01
0.10
0.11
0.35
0.12
0.00
0.53
0.00
0.50
0.00
0.06
0.06
0.38
0.46
0.05
0.00
0.49
0.00
0.47
0.00
0.02
0.02
0.49
(c) SCEA
negative
neutral
positive
negative
neutral
positive
0.67
0.27
0.06
0.10
0.80
0.10
0.01
0.26
0.73
(d) OSA
negative
neutral
positive
negative
neutral
positive
0.56
0.41
0.03
0.06
0.83
0.11
0.02
0.47
0.51
(e) EIA
angry
happy
neutral
sad
surprise
worried
angry
happy
neutral
sad
surprise
worried
0.64
0.02
0.18
0.07
0.02
0.08
0.00
0.85
0.12
0.00
0.02
0.01
0.01
0.02
0.77
0.07
0.01
0.11
0.02
0.02
0.10
0.68
0.02
0.16
0.06
0.06
0.35
0.06
0.41
0.06
0.02
0.00
0.12
0.11
0.00
0.75
(f) FGDEA
negative
neutral
positive
negative
neutral
positive
0.72
0.26
0.02
0.17
0.75
0.07
0.02
0.21
0.76
(g) FCDEA
negative
neutral
positive
negative
neutral
positive
0.72
0.23
0.05
0.07
0.74
0.19
0.03
0.23
0.75
(h) PEA
happy
surprise
sad
disgust
anger
fear
neutral
happy
surprise
sad
disgust
anger
fear
neutral
0.65
0.03
0.03
0.00
0.01
0.00
0.28
0.25
0.36
0.01
0.04
0.03
0.04
0.27
0.11
0.09
0.35
0.05
0.07
0.07
0.27
0.10
0.19
0.05
0.19
0.17
0.00
0.31
0.07
0.16
0.12
0.05
0.43
0.01
0.16
0.06
0.17
0.06
0.06
0.15
0.19
0.30
0.22
0.04
0.11
0.05
0.04
0.03
0.51
(i) CEIA (emo.)
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
0.85
0.03
0.05
0.03
0.00
0.04
0.00
0.01
0.00
0.28
0.54
0.03
0.00
0.11
0.00
0.03
0.00
0.12
0.76
0.08
0.04
0.00
0.00
0.00
0.00
0.00
0.57
0.23
0.07
0.10
0.00
0.03
0.09
0.06
0.32
0.12
0.21
0.11
0.06
0.04
0.15
0.07
0.27
0.05
0.00
0.36
0.00
0.09
0.07
0.04
0.31
0.11
0.02
0.07
0.24
0.13
0.11
0.04
0.66
0.00
0.04
0.01
0.04
0.09
(j) CEIA (int.)
anger
disgust
fear
joy
neutral
sadness
surprise
anger
disgust
fear
joy
neutral
sadness
surprise
0.49
0.00
0.00
0.11
0.19
0.04
0.17
0.17
0.31
0.00
0.12
0.21
0.05
0.14
0.03
0.00
0.14
0.21
0.38
0.03
0.21
0.02
0.00
0.00
0.69
0.16
0.04
0.10
0.06
0.00
0.00
0.21
0.65
0.08
0.00
0.13
0.03
0.03
0.05
0.38
0.36
0.03
0.08
0.00
0.01
0.26
0.12
0.08
0.46
(k) MPDER
false
true
false
true
0.62
0.38
0.05
0.95
(l) HU
false
true
false
true
0.72
0.28
0.12
0.88
(m) SD
Figure 18: Confusion matrices for Gemini-3.0-Flash on each evaluation scenario of EmoBench-M.

--- Page 19 ---

angry
calm
fearful
happy
neutral
sad
angry
calm
fearful
happy
neutral
sad
0.61
0.00
0.06
0.02
0.25
0.05
0.00
0.27
0.00
0.12
0.47
0.14
0.06
0.00
0.41
0.01
0.16
0.35
0.00
0.02
0.00
0.93
0.04
0.01
0.00
0.04
0.00
0.00
0.86
0.11
0.01
0.05
0.01
0.04
0.18
0.71
(a) SOER
angry
calm
disgust
fearful
happy
neutral
sad
surprised
angry
calm
disgust
fearful
happy
neutral
sad
surprised
0.53
0.00
0.03
0.00
0.00
0.31
0.03
0.10
0.00
0.10
0.00
0.00
0.15
0.73
0.03
0.00
0.02
0.00
0.53
0.00
0.00
0.00
0.44
0.02
0.00
0.00
0.02
0.23
0.00
0.15
0.18
0.44
0.00
0.02
0.00
0.00
0.87
0.02
0.00
0.10
0.00
0.00
0.00
0.00
0.00
0.83
0.12
0.05
0.00
0.00
0.05
0.02
0.02
0.18
0.73
0.02
0.00
0.00
0.06
0.02
0.08
0.19
0.02
0.63
(b) SPER
neutral
strong negative
strong positive
weak negative
weak positive
neutral
strong negative
strong positive
weak negative
weak positive
0.90
0.02
0.01
0.03
0.04
0.47
0.29
0.00
0.24
0.00
0.88
0.00
0.12
0.00
0.00
0.65
0.05
0.00
0.30
0.00
0.86
0.00
0.04
0.00
0.10
(c) SCEA
negative
neutral
positive
negative
neutral
positive
0.71
0.27
0.02
0.13
0.83
0.03
0.05
0.33
0.62
(d) OSA
negative
neutral
positive
negative
neutral
positive
0.62
0.34
0.04
0.07
0.88
0.05
0.04
0.56
0.40
(e) EIA
angry
happy
neutral
sad
surprise
worried
angry
happy
neutral
sad
surprise
worried
0.66
0.01
0.11
0.05
0.02
0.15
0.02
0.53
0.39
0.00
0.04
0.02
0.02
0.00
0.70
0.07
0.01
0.19
0.08
0.02
0.02
0.64
0.00
0.24
0.17
0.00
0.22
0.00
0.22
0.39
0.05
0.00
0.09
0.02
0.00
0.84
(f) FGDEA
negative
neutral
positive
negative
neutral
positive
0.81
0.17
0.02
0.25
0.68
0.07
0.11
0.31
0.58
(g) FCDEA
negative
neutral
positive
negative
neutral
positive
0.80
0.15
0.05
0.31
0.53
0.16
0.08
0.27
0.65
(h) PEA
happy
surprise
sad
disgust
anger
fear
neutral
happy
surprise
sad
disgust
anger
fear
neutral
0.42
0.05
0.03
0.00
0.00
0.00
0.50
0.12
0.36
0.01
0.05
0.01
0.01
0.42
0.03
0.09
0.34
0.04
0.10
0.04
0.34
0.05
0.14
0.05
0.24
0.05
0.00
0.48
0.04
0.14
0.08
0.05
0.31
0.01
0.36
0.04
0.17
0.11
0.00
0.09
0.04
0.54
0.16
0.02
0.09
0.04
0.05
0.01
0.63
(i) CEIA (emo.)
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
0.83
0.02
0.07
0.02
0.00
0.04
0.01
0.02
0.00
0.20
0.66
0.03
0.00
0.05
0.00
0.07
0.04
0.08
0.76
0.12
0.00
0.00
0.00
0.00
0.00
0.07
0.53
0.27
0.03
0.07
0.00
0.03
0.09
0.04
0.35
0.15
0.07
0.11
0.06
0.13
0.11
0.02
0.28
0.02
0.00
0.41
0.00
0.17
0.11
0.00
0.33
0.07
0.00
0.16
0.11
0.22
0.13
0.03
0.54
0.02
0.02
0.04
0.05
0.16
(j) CEIA (int.)
anger
disgust
fear
joy
neutral
sadness
surprise
anger
disgust
fear
joy
neutral
sadness
surprise
0.49
0.04
0.00
0.04
0.24
0.03
0.15
0.27
0.40
0.00
0.03
0.22
0.03
0.04
0.06
0.06
0.18
0.02
0.28
0.08
0.32
0.03
0.00
0.00
0.52
0.24
0.08
0.13
0.06
0.04
0.03
0.08
0.65
0.06
0.08
0.08
0.06
0.00
0.00
0.31
0.48
0.07
0.09
0.03
0.00
0.13
0.14
0.04
0.56
(k) MPDER
false
true
false
true
0.78
0.22
0.19
0.81
(l) HU
false
true
false
true
0.39
0.61
0.10
0.90
(m) SD
Figure 19: Confusion matrices for Gemini-2.0-Flash on each evaluation scenario of EmoBench-M.
angry
calm
fearful
happy
neutral
sad
angry
calm
fearful
happy
neutral
sad
0.75
0.01
0.04
0.02
0.18
0.00
0.00
0.18
0.00
0.27
0.49
0.06
0.10
0.01
0.42
0.00
0.18
0.29
0.01
0.02
0.00
0.89
0.07
0.00
0.00
0.08
0.02
0.00
0.84
0.06
0.06
0.05
0.02
0.02
0.20
0.64
(a) SOER
angry
calm
disgust
fearful
happy
neutral
sad
surprised
angry
calm
disgust
fearful
happy
neutral
sad
surprised
0.58
0.02
0.03
0.00
0.00
0.29
0.02
0.06
0.00
0.23
0.00
0.00
0.10
0.65
0.03
0.00
0.06
0.00
0.47
0.00
0.00
0.00
0.47
0.00
0.08
0.02
0.03
0.11
0.00
0.18
0.15
0.44
0.00
0.08
0.00
0.00
0.71
0.05
0.00
0.16
0.00
0.06
0.00
0.00
0.00
0.88
0.05
0.02
0.02
0.10
0.08
0.00
0.00
0.23
0.55
0.03
0.00
0.06
0.08
0.02
0.06
0.16
0.00
0.61
(b) SPER
neutral
strong negative
strong positive
weak negative
weak positive
neutral
strong negative
strong positive
weak negative
weak positive
0.48
0.05
0.08
0.27
0.12
0.06
0.24
0.00
0.71
0.00
0.12
0.00
0.50
0.12
0.25
0.19
0.19
0.00
0.59
0.03
0.22
0.02
0.35
0.12
0.29
(c) SCEA
negative
neutral
positive
negative
neutral
positive
0.81
0.15
0.04
0.30
0.57
0.13
0.11
0.21
0.67
(d) OSA
negative
neutral
positive
negative
neutral
positive
0.74
0.23
0.02
0.16
0.74
0.10
0.08
0.45
0.46
(e) EIA
angry
happy
neutral
sad
surprise
worried
angry
happy
neutral
sad
surprise
worried
0.68
0.00
0.10
0.10
0.02
0.10
0.04
0.69
0.22
0.04
0.00
0.01
0.08
0.02
0.68
0.08
0.00
0.14
0.08
0.02
0.02
0.70
0.00
0.18
0.28
0.11
0.17
0.00
0.22
0.22
0.16
0.00
0.05
0.05
0.00
0.74
(f) FGDEA
negative
neutral
positive
negative
neutral
positive
0.85
0.12
0.03
0.39
0.49
0.12
0.14
0.21
0.65
(g) FCDEA
negative
neutral
positive
negative
neutral
positive
0.82
0.12
0.06
0.36
0.48
0.16
0.08
0.23
0.68
(h) PEA
happy
surprise
sad
disgust
anger
fear
neutral
happy
surprise
sad
disgust
anger
fear
neutral
0.66
0.01
0.05
0.01
0.01
0.01
0.23
0.19
0.37
0.03
0.00
0.05
0.03
0.33
0.17
0.04
0.33
0.03
0.17
0.03
0.22
0.10
0.12
0.12
0.10
0.24
0.00
0.32
0.09
0.08
0.11
0.01
0.46
0.01
0.24
0.09
0.15
0.06
0.00
0.21
0.13
0.36
0.24
0.06
0.14
0.00
0.11
0.00
0.45
(i) CEIA (emo.)
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
0.87
0.03
0.02
0.01
0.00
0.06
0.00
0.02
0.00
0.35
0.30
0.00
0.03
0.15
0.00
0.17
0.00
0.16
0.72
0.00
0.00
0.00
0.00
0.12
0.00
0.19
0.22
0.33
0.04
0.07
0.00
0.15
0.08
0.13
0.11
0.09
0.27
0.24
0.04
0.05
0.19
0.06
0.06
0.06
0.13
0.37
0.00
0.15
0.14
0.09
0.07
0.05
0.12
0.16
0.09
0.28
0.17
0.04
0.17
0.02
0.14
0.13
0.02
0.29
(j) CEIA (int.)
anger
disgust
fear
joy
neutral
sadness
surprise
anger
disgust
fear
joy
neutral
sadness
surprise
0.55
0.00
0.00
0.08
0.14
0.04
0.18
0.39
0.33
0.03
0.06
0.09
0.07
0.03
0.14
0.00
0.22
0.08
0.32
0.10
0.14
0.08
0.00
0.00
0.63
0.21
0.03
0.04
0.06
0.01
0.04
0.11
0.66
0.03
0.08
0.17
0.00
0.03
0.04
0.25
0.48
0.03
0.13
0.01
0.01
0.17
0.13
0.04
0.50
(k) MPDER
false
true
false
true
0.48
0.52
0.04
0.96
(l) HU
false
true
false
true
0.22
0.78
0.05
0.95
(m) SD
Figure 20: Confusion matrices for Gemini-1.5-Flash on each evaluation scenario of EmoBench-M.

--- Page 20 ---

angry
calm
fearful
happy
neutral
sad
angry
calm
fearful
happy
neutral
sad
0.54
0.00
0.04
0.06
0.31
0.05
0.00
0.13
0.00
0.38
0.43
0.06
0.05
0.01
0.30
0.04
0.33
0.28
0.00
0.01
0.00
0.93
0.05
0.01
0.00
0.08
0.00
0.02
0.81
0.08
0.04
0.11
0.00
0.06
0.31
0.48
(a) SOER
angry
calm
disgust
fearful
happy
neutral
sad
surprised
angry
calm
disgust
fearful
happy
neutral
sad
surprised
0.47
0.02
0.02
0.02
0.03
0.29
0.08
0.08
0.00
0.18
0.00
0.00
0.31
0.48
0.03
0.00
0.02
0.00
0.61
0.00
0.00
0.00
0.37
0.00
0.02
0.00
0.05
0.08
0.00
0.29
0.27
0.29
0.00
0.00
0.00
0.00
1.00
0.00
0.00
0.00
0.00
0.03
0.00
0.00
0.02
0.83
0.11
0.02
0.00
0.03
0.03
0.00
0.08
0.21
0.65
0.00
0.05
0.02
0.06
0.02
0.21
0.16
0.08
0.40
(b) SPER
neutral
strong negative
strong positive
weak negative
weak positive
neutral
strong negative
strong positive
weak negative
weak positive
0.32
0.09
0.12
0.30
0.16
0.06
0.47
0.00
0.47
0.00
0.12
0.06
0.44
0.06
0.31
0.05
0.32
0.03
0.51
0.08
0.18
0.04
0.33
0.16
0.29
(c) SCEA
negative
neutral
positive
negative
neutral
positive
0.86
0.10
0.04
0.23
0.63
0.13
0.11
0.16
0.72
(d) OSA
negative
neutral
positive
negative
neutral
positive
0.73
0.23
0.04
0.18
0.71
0.11
0.07
0.37
0.56
(e) EIA
angry
happy
neutral
sad
surprise
worried
angry
happy
neutral
sad
surprise
worried
0.68
0.00
0.09
0.06
0.05
0.13
0.02
0.67
0.22
0.01
0.03
0.05
0.03
0.02
0.65
0.03
0.01
0.25
0.08
0.04
0.04
0.44
0.00
0.40
0.06
0.17
0.06
0.00
0.33
0.39
0.09
0.00
0.09
0.00
0.00
0.82
(f) FGDEA
negative
neutral
positive
negative
neutral
positive
0.81
0.14
0.06
0.39
0.46
0.14
0.11
0.20
0.69
(g) FCDEA
negative
neutral
positive
negative
neutral
positive
0.81
0.13
0.05
0.34
0.40
0.26
0.13
0.19
0.69
(h) PEA
happy
surprise
sad
disgust
anger
fear
neutral
happy
surprise
sad
disgust
anger
fear
neutral
0.58
0.01
0.05
0.00
0.01
0.00
0.34
0.16
0.34
0.04
0.04
0.00
0.04
0.37
0.11
0.07
0.43
0.05
0.05
0.02
0.26
0.10
0.10
0.05
0.26
0.10
0.00
0.40
0.04
0.07
0.16
0.07
0.31
0.03
0.33
0.04
0.13
0.09
0.02
0.09
0.13
0.51
0.26
0.04
0.08
0.04
0.07
0.01
0.48
(i) CEIA (emo.)
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
0.80
0.03
0.05
0.04
0.00
0.04
0.01
0.04
0.00
0.30
0.57
0.02
0.02
0.05
0.02
0.03
0.00
0.12
0.76
0.12
0.00
0.00
0.00
0.00
0.00
0.03
0.55
0.28
0.03
0.10
0.00
0.00
0.10
0.05
0.36
0.14
0.12
0.11
0.04
0.08
0.13
0.04
0.38
0.11
0.00
0.18
0.05
0.11
0.16
0.00
0.36
0.11
0.00
0.13
0.13
0.11
0.13
0.01
0.55
0.03
0.05
0.02
0.06
0.14
(j) CEIA (int.)
anger
disgust
fear
joy
neutral
sadness
surprise
anger
disgust
fear
joy
neutral
sadness
surprise
0.44
0.04
0.00
0.07
0.20
0.06
0.20
0.18
0.54
0.03
0.03
0.13
0.04
0.04
0.06
0.02
0.34
0.10
0.24
0.12
0.12
0.04
0.00
0.00
0.59
0.24
0.04
0.08
0.03
0.01
0.03
0.10
0.66
0.11
0.06
0.08
0.07
0.01
0.03
0.24
0.51
0.06
0.07
0.04
0.02
0.19
0.15
0.04
0.48
(k) MPDER
false
true
false
true
0.56
0.44
0.06
0.94
(l) HU
false
true
false
true
0.28
0.72
0.07
0.93
(m) SD
Figure 21: Confusion matrices for Gemini-2.0-Flash-Thinking on each evaluation scenario of EmoBench-M.
angry
calm
fearful
happy
neutral
sad
angry
calm
fearful
happy
neutral
sad
0.68
0.00
0.01
0.12
0.13
0.05
0.00
0.00
0.00
0.61
0.35
0.04
0.13
0.00
0.34
0.16
0.22
0.16
0.00
0.00
0.00
1.00
0.00
0.00
0.00
0.01
0.01
0.11
0.87
0.00
0.08
0.01
0.06
0.10
0.35
0.40
(a) SOER
angry
calm
disgust
fearful
happy
neutral
sad
surprised
angry
calm
disgust
fearful
happy
neutral
sad
surprised
0.33
0.00
0.00
0.00
0.10
0.27
0.05
0.25
0.00
0.00
0.00
0.00
0.76
0.24
0.00
0.00
0.39
0.00
0.10
0.00
0.06
0.05
0.40
0.00
0.02
0.00
0.02
0.06
0.09
0.28
0.09
0.43
0.00
0.00
0.00
0.00
1.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.97
0.00
0.03
0.03
0.00
0.00
0.02
0.16
0.30
0.39
0.10
0.07
0.00
0.02
0.00
0.22
0.14
0.00
0.56
(b) SPER
neutral
strong negative
strong positive
weak negative
weak positive
neutral
strong negative
strong positive
weak negative
weak positive
0.84
0.03
0.06
0.03
0.03
0.35
0.29
0.00
0.35
0.00
0.62
0.00
0.25
0.06
0.06
0.62
0.27
0.00
0.11
0.00
0.65
0.00
0.24
0.02
0.10
(c) SCEA
negative
neutral
positive
negative
neutral
positive
0.80
0.18
0.02
0.27
0.73
0.00
0.11
0.38
0.51
(d) OSA
negative
neutral
positive
negative
neutral
positive
0.64
0.35
0.01
0.10
0.88
0.02
0.05
0.63
0.31
(e) EIA
angry
happy
neutral
sad
surprise
worried
angry
happy
neutral
sad
surprise
worried
0.48
0.06
0.19
0.02
0.23
0.03
0.04
0.63
0.16
0.01
0.13
0.02
0.08
0.06
0.69
0.03
0.12
0.01
0.12
0.08
0.18
0.34
0.22
0.06
0.06
0.06
0.17
0.06
0.67
0.00
0.23
0.00
0.37
0.02
0.14
0.25
(f) FGDEA
negative
neutral
positive
negative
neutral
positive
0.78
0.19
0.03
0.36
0.57
0.07
0.19
0.34
0.48
(g) FCDEA
negative
neutral
positive
negative
neutral
positive
0.73
0.24
0.03
0.21
0.60
0.19
0.09
0.39
0.52
(h) PEA
happy
surprise
sad
disgust
anger
fear
neutral
happy
surprise
sad
disgust
anger
fear
neutral
0.65
0.08
0.04
0.03
0.00
0.00
0.19
0.29
0.43
0.01
0.04
0.00
0.03
0.19
0.18
0.12
0.27
0.04
0.18
0.02
0.19
0.14
0.24
0.00
0.24
0.14
0.00
0.24
0.13
0.26
0.09
0.01
0.35
0.00
0.17
0.11
0.23
0.11
0.00
0.14
0.11
0.30
0.43
0.06
0.08
0.06
0.12
0.01
0.24
(i) CEIA (emo.)
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
0.63
0.00
0.11
0.00
0.00
0.03
0.01
0.22
0.04
0.00
0.69
0.00
0.04
0.06
0.00
0.17
0.00
0.00
0.94
0.00
0.00
0.00
0.00
0.06
0.00
0.00
0.68
0.05
0.11
0.05
0.00
0.11
0.06
0.00
0.44
0.00
0.21
0.15
0.03
0.12
0.07
0.00
0.32
0.00
0.07
0.09
0.09
0.36
0.12
0.03
0.27
0.00
0.12
0.09
0.15
0.21
0.09
0.00
0.55
0.02
0.04
0.04
0.03
0.22
(j) CEIA (int.)
anger
disgust
fear
joy
neutral
sadness
surprise
anger
disgust
fear
joy
neutral
sadness
surprise
0.58
0.03
0.01
0.06
0.14
0.00
0.18
0.57
0.25
0.00
0.06
0.07
0.00
0.04
0.20
0.00
0.18
0.08
0.27
0.02
0.24
0.10
0.03
0.00
0.48
0.20
0.01
0.18
0.11
0.00
0.03
0.21
0.42
0.01
0.21
0.31
0.07
0.01
0.06
0.17
0.23
0.15
0.11
0.01
0.01
0.13
0.11
0.01
0.61
(k) MPDER
false
true
false
true
0.68
0.32
0.19
0.81
(l) HU
false
true
false
true
0.43
0.57
0.24
0.76
(m) SD
Figure 22: Confusion matrices for GLM-4V-PLUS on each evaluation scenario of EmoBench-M.

--- Page 21 ---

angry
calm
fearful
happy
neutral
sad
angry
calm
fearful
happy
neutral
sad
0.35
0.15
0.06
0.04
0.37
0.04
0.01
0.12
0.00
0.39
0.45
0.04
0.08
0.10
0.33
0.01
0.29
0.19
0.00
0.01
0.00
0.92
0.07
0.00
0.00
0.06
0.01
0.04
0.89
0.00
0.05
0.10
0.05
0.01
0.38
0.41
(a) SOER
angry
calm
disgust
fearful
happy
neutral
sad
surprised
angry
calm
disgust
fearful
happy
neutral
sad
surprised
0.19
0.08
0.00
0.03
0.02
0.46
0.02
0.20
0.00
0.21
0.00
0.00
0.35
0.44
0.00
0.00
0.28
0.00
0.10
0.02
0.00
0.07
0.54
0.00
0.07
0.05
0.00
0.03
0.02
0.34
0.18
0.31
0.00
0.00
0.00
0.00
0.97
0.03
0.00
0.00
0.00
0.12
0.00
0.00
0.03
0.85
0.00
0.00
0.02
0.07
0.03
0.02
0.00
0.36
0.51
0.00
0.02
0.00
0.02
0.02
0.16
0.39
0.00
0.40
(b) SPER
neutral
strong negative
strong positive
weak negative
weak positive
neutral
strong negative
strong positive
weak negative
weak positive
0.74
0.01
0.04
0.10
0.12
0.35
0.12
0.00
0.47
0.06
0.62
0.00
0.19
0.06
0.12
0.54
0.00
0.00
0.30
0.16
0.55
0.00
0.18
0.06
0.22
(c) SCEA
negative
neutral
positive
negative
neutral
positive
0.74
0.19
0.07
0.10
0.57
0.33
0.15
0.14
0.70
(d) OSA
negative
neutral
positive
negative
neutral
positive
0.62
0.27
0.11
0.11
0.56
0.33
0.07
0.30
0.62
(e) EIA
angry
happy
neutral
sad
surprise
worried
angry
happy
neutral
sad
surprise
worried
0.69
0.01
0.14
0.06
0.01
0.09
0.06
0.53
0.26
0.02
0.06
0.06
0.09
0.03
0.46
0.19
0.03
0.21
0.07
0.00
0.10
0.60
0.02
0.21
0.31
0.00
0.08
0.08
0.31
0.23
0.17
0.00
0.07
0.07
0.05
0.64
(f) FGDEA
negative
neutral
positive
negative
neutral
positive
0.73
0.18
0.09
0.31
0.49
0.21
0.13
0.20
0.67
(g) FCDEA
negative
neutral
positive
negative
neutral
positive
0.69
0.18
0.13
0.34
0.34
0.31
0.11
0.16
0.73
(h) PEA
happy
surprise
sad
disgust
anger
fear
neutral
happy
surprise
sad
disgust
anger
fear
neutral
0.27
0.34
0.06
0.04
0.04
0.03
0.21
0.06
0.68
0.03
0.01
0.03
0.04
0.15
0.04
0.21
0.36
0.05
0.16
0.11
0.07
0.05
0.45
0.00
0.07
0.38
0.00
0.05
0.03
0.32
0.05
0.03
0.41
0.04
0.12
0.02
0.30
0.09
0.02
0.18
0.20
0.18
0.09
0.27
0.11
0.10
0.12
0.02
0.27
(i) CEIA (emo.)
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
0.89
0.02
0.01
0.00
0.01
0.06
0.01
0.00
0.24
0.28
0.35
0.00
0.00
0.11
0.00
0.02
0.05
0.21
0.68
0.00
0.00
0.00
0.05
0.00
0.20
0.20
0.32
0.04
0.04
0.20
0.00
0.00
0.29
0.05
0.20
0.01
0.16
0.29
0.00
0.00
0.37
0.06
0.06
0.02
0.07
0.41
0.00
0.02
0.41
0.00
0.14
0.00
0.07
0.20
0.16
0.02
0.40
0.01
0.32
0.01
0.05
0.18
0.03
0.00
(j) CEIA (int.)
anger
disgust
fear
joy
neutral
sadness
surprise
anger
disgust
fear
joy
neutral
sadness
surprise
0.39
0.03
0.07
0.03
0.06
0.06
0.37
0.32
0.11
0.06
0.02
0.03
0.06
0.41
0.10
0.00
0.39
0.10
0.00
0.08
0.33
0.13
0.00
0.04
0.43
0.07
0.03
0.30
0.08
0.03
0.06
0.08
0.37
0.10
0.28
0.15
0.03
0.07
0.03
0.10
0.39
0.23
0.08
0.02
0.04
0.11
0.04
0.02
0.68
(k) MPDER
false
true
false
true
0.57
0.43
0.44
0.56
(l) HU
false
true
false
true
0.56
0.44
0.51
0.49
(m) SD
Figure 23: Confusion matrices for InternVL2.5-4B on each evaluation scenario of EmoBench-M.
angry
calm
fearful
happy
neutral
sad
angry
calm
fearful
happy
neutral
sad
0.16
0.00
0.01
0.00
0.77
0.06
0.00
0.04
0.00
0.12
0.82
0.02
0.00
0.00
0.11
0.00
0.71
0.18
0.00
0.00
0.00
0.69
0.31
0.00
0.00
0.00
0.00
0.00
1.00
0.00
0.00
0.00
0.01
0.02
0.55
0.41
(a) SOER
angry
calm
disgust
fearful
happy
neutral
sad
surprised
angry
calm
disgust
fearful
happy
neutral
sad
surprised
0.06
0.00
0.02
0.00
0.00
0.61
0.06
0.24
0.00
0.10
0.00
0.00
0.10
0.81
0.00
0.00
0.03
0.00
0.37
0.00
0.00
0.13
0.45
0.02
0.00
0.00
0.00
0.00
0.00
0.45
0.10
0.45
0.00
0.02
0.00
0.00
0.77
0.18
0.00
0.03
0.00
0.00
0.00
0.00
0.00
1.00
0.00
0.00
0.00
0.00
0.02
0.00
0.00
0.47
0.47
0.05
0.00
0.00
0.02
0.00
0.05
0.48
0.00
0.45
(b) SPER
neutral
strong negative
strong positive
weak negative
weak positive
neutral
strong negative
strong positive
weak negative
weak positive
0.73
0.06
0.15
0.04
0.02
0.35
0.41
0.00
0.24
0.00
0.50
0.06
0.44
0.00
0.00
0.54
0.27
0.03
0.14
0.03
0.55
0.00
0.43
0.02
0.00
(c) SCEA
negative
neutral
positive
negative
neutral
positive
0.64
0.32
0.04
0.13
0.80
0.07
0.06
0.22
0.72
(d) OSA
negative
neutral
positive
negative
neutral
positive
0.55
0.39
0.05
0.07
0.73
0.20
0.03
0.40
0.57
(e) EIA
angry
happy
neutral
sad
surprise
worried
angry
happy
neutral
sad
surprise
worried
0.38
0.01
0.32
0.12
0.09
0.08
0.02
0.27
0.59
0.02
0.08
0.02
0.03
0.00
0.78
0.15
0.00
0.03
0.02
0.00
0.18
0.68
0.02
0.10
0.06
0.00
0.33
0.11
0.28
0.22
0.07
0.00
0.35
0.04
0.07
0.47
(f) FGDEA
negative
neutral
positive
negative
neutral
positive
0.66
0.26
0.08
0.19
0.62
0.19
0.09
0.35
0.56
(g) FCDEA
negative
neutral
positive
negative
neutral
positive
0.62
0.28
0.10
0.21
0.47
0.33
0.08
0.28
0.64
(h) PEA
happy
surprise
sad
disgust
anger
fear
neutral
happy
surprise
sad
disgust
anger
fear
neutral
0.34
0.13
0.06
0.00
0.03
0.00
0.45
0.05
0.47
0.03
0.03
0.03
0.01
0.38
0.02
0.16
0.29
0.10
0.13
0.02
0.28
0.05
0.28
0.05
0.12
0.17
0.00
0.33
0.01
0.15
0.07
0.01
0.44
0.01
0.29
0.00
0.35
0.04
0.04
0.13
0.07
0.37
0.09
0.10
0.05
0.02
0.12
0.00
0.62
(i) CEIA (emo.)
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
0.58
0.00
0.06
0.01
0.02
0.11
0.00
0.22
0.02
0.08
0.19
0.03
0.08
0.07
0.00
0.53
0.00
0.04
0.52
0.00
0.04
0.20
0.00
0.20
0.00
0.00
0.24
0.21
0.14
0.14
0.00
0.28
0.05
0.03
0.09
0.01
0.29
0.14
0.01
0.37
0.04
0.02
0.06
0.02
0.17
0.33
0.00
0.37
0.00
0.05
0.09
0.00
0.21
0.23
0.05
0.37
0.06
0.01
0.19
0.01
0.16
0.15
0.00
0.41
(j) CEIA (int.)
anger
disgust
fear
joy
neutral
sadness
surprise
anger
disgust
fear
joy
neutral
sadness
surprise
0.61
0.00
0.00
0.04
0.06
0.04
0.25
0.53
0.13
0.00
0.03
0.09
0.04
0.18
0.27
0.00
0.18
0.06
0.10
0.10
0.29
0.14
0.00
0.00
0.50
0.10
0.03
0.23
0.17
0.00
0.01
0.14
0.41
0.04
0.23
0.21
0.00
0.01
0.03
0.10
0.44
0.21
0.17
0.00
0.00
0.08
0.09
0.02
0.63
(k) MPDER
false
true
false
true
0.70
0.30
0.37
0.63
(l) HU
false
true
false
true
0.48
0.52
0.29
0.71
(m) SD
Figure 24: Confusion matrices for InternVL2.5-8B on each evaluation scenario of EmoBench-M.

--- Page 22 ---

angry
calm
fearful
happy
neutral
sad
angry
calm
fearful
happy
neutral
sad
0.46
0.01
0.02
0.02
0.48
0.00
0.00
0.14
0.00
0.39
0.45
0.02
0.10
0.01
0.36
0.02
0.42
0.08
0.00
0.01
0.00
0.94
0.05
0.00
0.00
0.04
0.00
0.00
0.96
0.00
0.05
0.05
0.04
0.05
0.48
0.34
(a) SOER
angry
calm
disgust
fearful
happy
neutral
sad
surprised
angry
calm
disgust
fearful
happy
neutral
sad
surprised
0.19
0.00
0.03
0.02
0.02
0.47
0.02
0.26
0.00
0.16
0.00
0.00
0.44
0.40
0.00
0.00
0.24
0.00
0.31
0.00
0.00
0.06
0.27
0.11
0.00
0.02
0.03
0.06
0.00
0.26
0.03
0.60
0.00
0.00
0.00
0.00
0.98
0.00
0.00
0.02
0.00
0.03
0.00
0.00
0.00
0.92
0.00
0.05
0.00
0.03
0.11
0.02
0.08
0.32
0.34
0.10
0.02
0.05
0.00
0.00
0.13
0.27
0.00
0.53
(b) SPER
neutral
strong negative
strong positive
weak negative
weak positive
neutral
strong negative
strong positive
weak negative
weak positive
0.92
0.03
0.05
0.00
0.00
0.65
0.24
0.00
0.12
0.00
0.81
0.00
0.19
0.00
0.00
0.62
0.22
0.00
0.16
0.00
0.78
0.00
0.20
0.02
0.00
(c) SCEA
negative
neutral
positive
negative
neutral
positive
0.67
0.29
0.04
0.10
0.70
0.20
0.03
0.20
0.77
(d) OSA
negative
neutral
positive
negative
neutral
positive
0.64
0.28
0.08
0.05
0.68
0.27
0.03
0.30
0.67
(e) EIA
angry
happy
neutral
sad
surprise
worried
angry
happy
neutral
sad
surprise
worried
0.51
0.01
0.29
0.09
0.07
0.04
0.01
0.42
0.52
0.01
0.04
0.00
0.03
0.00
0.84
0.06
0.03
0.03
0.08
0.02
0.24
0.48
0.04
0.14
0.00
0.00
0.67
0.00
0.28
0.06
0.09
0.00
0.21
0.02
0.07
0.61
(f) FGDEA
negative
neutral
positive
negative
neutral
positive
0.65
0.29
0.06
0.22
0.67
0.12
0.09
0.26
0.64
(g) FCDEA
negative
neutral
positive
negative
neutral
positive
0.63
0.31
0.06
0.22
0.57
0.21
0.04
0.23
0.72
(h) PEA
happy
surprise
sad
disgust
anger
fear
neutral
happy
surprise
sad
disgust
anger
fear
neutral
0.55
0.10
0.03
0.00
0.01
0.00
0.32
0.10
0.52
0.01
0.00
0.01
0.00
0.36
0.07
0.08
0.30
0.03
0.10
0.04
0.38
0.07
0.33
0.00
0.19
0.12
0.00
0.29
0.04
0.20
0.05
0.03
0.39
0.01
0.28
0.02
0.28
0.04
0.02
0.13
0.09
0.43
0.17
0.09
0.10
0.01
0.06
0.01
0.56
(i) CEIA (emo.)
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
0.80
0.00
0.08
0.02
0.00
0.05
0.00
0.06
0.08
0.13
0.48
0.07
0.03
0.05
0.00
0.16
0.00
0.00
0.80
0.04
0.04
0.00
0.00
0.12
0.00
0.00
0.52
0.31
0.07
0.07
0.00
0.03
0.18
0.02
0.32
0.07
0.18
0.07
0.00
0.15
0.24
0.02
0.20
0.05
0.00
0.24
0.00
0.25
0.30
0.00
0.23
0.05
0.07
0.12
0.09
0.14
0.26
0.00
0.41
0.02
0.07
0.01
0.01
0.22
(j) CEIA (int.)
anger
disgust
fear
joy
neutral
sadness
surprise
anger
disgust
fear
joy
neutral
sadness
surprise
0.38
0.01
0.01
0.08
0.18
0.03
0.30
0.24
0.22
0.04
0.07
0.16
0.04
0.22
0.16
0.02
0.18
0.14
0.22
0.02
0.24
0.03
0.00
0.01
0.63
0.13
0.01
0.18
0.01
0.00
0.00
0.21
0.48
0.04
0.25
0.13
0.00
0.04
0.07
0.14
0.41
0.21
0.06
0.00
0.01
0.14
0.16
0.03
0.59
(k) MPDER
false
true
false
true
0.84
0.16
0.37
0.63
(l) HU
false
true
false
true
0.63
0.37
0.41
0.59
(m) SD
Figure 25: Confusion matrices for InternVL2.5-38B on each evaluation scenario of EmoBench-M.
angry
calm
fearful
happy
neutral
sad
angry
calm
fearful
happy
neutral
sad
0.30
0.06
0.05
0.01
0.48
0.10
0.00
0.23
0.00
0.19
0.51
0.07
0.01
0.07
0.25
0.00
0.42
0.24
0.00
0.04
0.00
0.89
0.07
0.00
0.00
0.15
0.00
0.00
0.80
0.05
0.02
0.07
0.00
0.02
0.43
0.45
(a) SOER
angry
calm
disgust
fearful
happy
neutral
sad
surprised
angry
calm
disgust
fearful
happy
neutral
sad
surprised
0.18
0.03
0.00
0.00
0.02
0.55
0.05
0.18
0.00
0.18
0.00
0.00
0.18
0.65
0.00
0.00
0.10
0.00
0.31
0.00
0.00
0.16
0.44
0.00
0.00
0.00
0.02
0.02
0.00
0.42
0.16
0.39
0.00
0.03
0.00
0.00
0.87
0.06
0.00
0.03
0.00
0.12
0.00
0.00
0.00
0.80
0.08
0.00
0.00
0.08
0.02
0.00
0.03
0.29
0.56
0.02
0.00
0.02
0.02
0.00
0.10
0.50
0.02
0.35
(b) SPER
neutral
strong negative
strong positive
weak negative
weak positive
neutral
strong negative
strong positive
weak negative
weak positive
0.98
0.01
0.00
0.01
0.01
0.88
0.12
0.00
0.00
0.00
0.88
0.00
0.12
0.00
0.00
0.89
0.08
0.00
0.03
0.00
0.90
0.00
0.10
0.00
0.00
(c) SCEA
negative
neutral
positive
negative
neutral
positive
0.63
0.34
0.02
0.17
0.73
0.10
0.07
0.33
0.61
(d) OSA
negative
neutral
positive
negative
neutral
positive
0.49
0.48
0.03
0.05
0.89
0.06
0.01
0.60
0.39
(e) EIA
angry
happy
neutral
sad
surprise
worried
angry
happy
neutral
sad
surprise
worried
0.45
0.01
0.32
0.10
0.05
0.08
0.00
0.40
0.56
0.00
0.04
0.00
0.03
0.00
0.84
0.05
0.00
0.08
0.04
0.00
0.28
0.40
0.04
0.24
0.06
0.00
0.50
0.11
0.22
0.11
0.09
0.00
0.29
0.02
0.00
0.61
(f) FGDEA
negative
neutral
positive
negative
neutral
positive
0.51
0.45
0.04
0.13
0.83
0.04
0.06
0.39
0.54
(g) FCDEA
negative
neutral
positive
negative
neutral
positive
0.52
0.43
0.05
0.14
0.72
0.14
0.03
0.39
0.58
(h) PEA
happy
surprise
sad
disgust
anger
fear
neutral
happy
surprise
sad
disgust
anger
fear
neutral
0.40
0.06
0.04
0.01
0.00
0.00
0.49
0.10
0.42
0.03
0.01
0.04
0.03
0.38
0.05
0.09
0.30
0.04
0.15
0.03
0.33
0.05
0.24
0.02
0.12
0.17
0.00
0.39
0.01
0.08
0.11
0.04
0.42
0.01
0.32
0.05
0.16
0.07
0.00
0.09
0.09
0.55
0.08
0.04
0.09
0.02
0.11
0.00
0.66
(i) CEIA (emo.)
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
0.85
0.00
0.08
0.01
0.01
0.05
0.00
0.00
0.05
0.13
0.55
0.05
0.05
0.15
0.00
0.02
0.04
0.00
0.84
0.00
0.00
0.08
0.00
0.04
0.00
0.04
0.64
0.12
0.08
0.12
0.00
0.00
0.14
0.01
0.35
0.04
0.17
0.21
0.01
0.06
0.28
0.00
0.24
0.06
0.02
0.35
0.00
0.06
0.19
0.00
0.30
0.00
0.12
0.28
0.09
0.02
0.25
0.00
0.33
0.02
0.15
0.10
0.02
0.13
(j) CEIA (int.)
anger
disgust
fear
joy
neutral
sadness
surprise
anger
disgust
fear
joy
neutral
sadness
surprise
0.66
0.00
0.01
0.08
0.11
0.01
0.11
0.49
0.19
0.00
0.09
0.13
0.03
0.07
0.29
0.00
0.08
0.08
0.31
0.06
0.18
0.08
0.00
0.00
0.61
0.17
0.03
0.11
0.06
0.00
0.01
0.24
0.46
0.08
0.14
0.15
0.01
0.04
0.06
0.18
0.49
0.06
0.16
0.00
0.00
0.17
0.18
0.05
0.43
(k) MPDER
false
true
false
true
0.77
0.23
0.23
0.77
(l) HU
false
true
false
true
0.50
0.50
0.21
0.79
(m) SD
Figure 26: Confusion matrices for InternVL2.5-78B on each evaluation scenario of EmoBench-M.

--- Page 23 ---

angry
calm
fearful
happy
neutral
sad
angry
calm
fearful
happy
neutral
sad
0.52
0.00
0.06
0.06
0.36
0.00
0.00
0.00
0.00
0.34
0.63
0.04
0.08
0.00
0.40
0.01
0.42
0.08
0.00
0.00
0.00
0.96
0.04
0.00
0.00
0.00
0.00
0.00
1.00
0.00
0.00
0.00
0.05
0.06
0.47
0.42
(a) SOER
angry
calm
disgust
fearful
happy
neutral
sad
surprised
angry
calm
disgust
fearful
happy
neutral
sad
surprised
0.48
0.00
0.00
0.00
0.02
0.36
0.00
0.14
0.00
0.02
0.00
0.00
0.24
0.74
0.00
0.00
0.32
0.00
0.00
0.00
0.00
0.08
0.58
0.02
0.00
0.00
0.00
0.00
0.00
0.43
0.13
0.44
0.00
0.00
0.00
0.00
0.92
0.03
0.00
0.05
0.00
0.00
0.00
0.00
0.00
1.00
0.00
0.00
0.00
0.00
0.00
0.00
0.05
0.55
0.40
0.00
0.00
0.00
0.00
0.00
0.13
0.27
0.00
0.60
(b) SPER
neutral
strong negative
strong positive
weak negative
weak positive
neutral
strong negative
strong positive
weak negative
weak positive
0.92
0.01
0.02
0.04
0.02
0.59
0.06
0.00
0.35
0.00
0.81
0.00
0.19
0.00
0.00
0.73
0.05
0.00
0.22
0.00
0.90
0.00
0.08
0.02
0.00
(c) SCEA
negative
neutral
positive
negative
neutral
positive
0.35
0.62
0.03
0.00
0.87
0.13
0.02
0.40
0.57
(d) OSA
negative
neutral
positive
negative
neutral
positive
0.33
0.57
0.10
0.03
0.71
0.26
0.01
0.36
0.64
(e) EIA
angry
happy
neutral
sad
surprise
worried
angry
happy
neutral
sad
surprise
worried
0.38
0.07
0.36
0.12
0.04
0.03
0.00
0.84
0.14
0.01
0.01
0.00
0.03
0.08
0.84
0.02
0.00
0.02
0.02
0.04
0.22
0.70
0.02
0.00
0.00
0.06
0.50
0.11
0.28
0.06
0.09
0.02
0.61
0.14
0.04
0.11
(f) FGDEA
negative
neutral
positive
negative
neutral
positive
0.33
0.64
0.04
0.04
0.91
0.04
0.01
0.41
0.58
(g) FCDEA
negative
neutral
positive
negative
neutral
positive
0.32
0.63
0.05
0.02
0.88
0.10
0.01
0.37
0.61
(h) PEA
happy
surprise
sad
disgust
anger
fear
neutral
happy
surprise
sad
disgust
anger
fear
neutral
0.63
0.15
0.03
0.01
0.00
0.00
0.18
0.13
0.55
0.03
0.01
0.00
0.00
0.28
0.10
0.24
0.22
0.14
0.00
0.02
0.28
0.18
0.46
0.00
0.13
0.00
0.00
0.23
0.06
0.47
0.06
0.10
0.03
0.00
0.29
0.19
0.40
0.02
0.07
0.02
0.02
0.28
0.24
0.30
0.05
0.05
0.00
0.00
0.36
(i) CEIA (emo.)
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
0.98
0.00
0.01
0.00
0.00
0.01
0.00
0.00
0.39
0.10
0.39
0.02
0.02
0.08
0.00
0.00
0.17
0.00
0.83
0.00
0.00
0.00
0.00
0.00
0.23
0.03
0.47
0.13
0.03
0.10
0.00
0.00
0.54
0.01
0.16
0.08
0.05
0.15
0.00
0.00
0.61
0.02
0.14
0.06
0.00
0.16
0.00
0.00
0.60
0.00
0.23
0.03
0.03
0.10
0.03
0.00
0.67
0.01
0.18
0.01
0.04
0.07
0.01
0.00
(j) CEIA (int.)
anger
disgust
fear
joy
neutral
sadness
surprise
anger
disgust
fear
joy
neutral
sadness
surprise
0.21
0.00
0.01
0.04
0.48
0.03
0.23
0.16
0.06
0.04
0.06
0.43
0.07
0.18
0.04
0.00
0.20
0.04
0.46
0.02
0.24
0.03
0.00
0.00
0.49
0.24
0.06
0.18
0.01
0.00
0.00
0.10
0.82
0.01
0.06
0.07
0.03
0.06
0.04
0.49
0.21
0.10
0.04
0.00
0.01
0.14
0.42
0.04
0.35
(k) MPDER
false
true
false
true
0.79
0.21
0.42
0.58
(l) HU
false
true
false
true
0.55
0.45
0.32
0.68
(m) SD
Figure 27: Confusion matrices for InternVideo2-Chat-8B on each evaluation scenario of EmoBench-M.
angry
calm
fearful
happy
neutral
sad
angry
calm
fearful
happy
neutral
sad
0.59
0.00
0.02
0.00
0.39
0.00
0.00
0.00
0.01
0.12
0.84
0.02
0.10
0.00
0.42
0.00
0.45
0.04
0.00
0.00
0.00
0.87
0.13
0.00
0.00
0.00
0.00
0.00
0.99
0.01
0.08
0.04
0.19
0.01
0.54
0.13
(a) SOER
angry
calm
disgust
fearful
happy
neutral
sad
surprised
angry
calm
disgust
fearful
happy
neutral
sad
surprised
0.44
0.00
0.02
0.00
0.00
0.45
0.00
0.10
0.00
0.00
0.00
0.00
0.11
0.85
0.03
0.00
0.24
0.00
0.52
0.02
0.00
0.08
0.10
0.05
0.05
0.00
0.00
0.03
0.00
0.32
0.05
0.55
0.00
0.00
0.00
0.00
0.92
0.06
0.00
0.02
0.00
0.00
0.00
0.00
0.00
0.94
0.03
0.03
0.11
0.00
0.03
0.03
0.00
0.42
0.31
0.10
0.02
0.00
0.00
0.03
0.03
0.56
0.00
0.35
(b) SPER
neutral
strong negative
strong positive
weak negative
weak positive
neutral
strong negative
strong positive
weak negative
weak positive
0.87
0.03
0.02
0.08
0.00
0.35
0.18
0.00
0.47
0.00
0.75
0.06
0.12
0.00
0.06
0.46
0.03
0.00
0.51
0.00
0.92
0.00
0.02
0.04
0.02
(c) SCEA
negative
neutral
positive
negative
neutral
positive
0.39
0.61
0.00
0.07
0.93
0.00
0.03
0.83
0.14
(d) OSA
negative
neutral
positive
negative
neutral
positive
0.30
0.70
0.00
0.02
0.96
0.01
0.01
0.89
0.10
(e) EIA
angry
happy
neutral
sad
surprise
worried
angry
happy
neutral
sad
surprise
worried
0.41
0.02
0.43
0.02
0.07
0.06
0.00
0.59
0.39
0.01
0.01
0.00
0.03
0.00
0.90
0.00
0.01
0.06
0.04
0.02
0.50
0.22
0.04
0.18
0.17
0.06
0.39
0.00
0.22
0.17
0.12
0.00
0.53
0.00
0.04
0.32
(f) FGDEA
negative
neutral
positive
negative
neutral
positive
0.29
0.71
0.00
0.09
0.90
0.01
0.01
0.85
0.14
(g) FCDEA
negative
neutral
positive
negative
neutral
positive
0.31
0.68
0.01
0.02
0.98
0.00
0.00
0.82
0.17
(h) PEA
happy
surprise
sad
disgust
anger
fear
neutral
happy
surprise
sad
disgust
anger
fear
neutral
0.44
0.06
0.02
0.02
0.00
0.00
0.47
0.10
0.48
0.00
0.03
0.00
0.00
0.39
0.02
0.16
0.15
0.20
0.00
0.00
0.47
0.05
0.30
0.00
0.27
0.00
0.00
0.38
0.01
0.29
0.07
0.29
0.01
0.01
0.31
0.02
0.28
0.05
0.07
0.05
0.00
0.53
0.14
0.08
0.04
0.15
0.00
0.00
0.59
(i) CEIA (emo.)
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
0.77
0.02
0.13
0.01
0.00
0.06
0.00
0.00
0.07
0.11
0.67
0.02
0.00
0.09
0.00
0.04
0.00
0.05
0.80
0.00
0.00
0.15
0.00
0.00
0.07
0.00
0.61
0.11
0.00
0.14
0.00
0.07
0.16
0.03
0.43
0.04
0.04
0.22
0.00
0.06
0.21
0.06
0.28
0.02
0.00
0.38
0.00
0.04
0.20
0.02
0.44
0.05
0.00
0.22
0.00
0.07
0.28
0.00
0.51
0.00
0.01
0.10
0.00
0.10
(j) CEIA (int.)
anger
disgust
fear
joy
neutral
sadness
surprise
anger
disgust
fear
joy
neutral
sadness
surprise
0.08
0.14
0.00
0.01
0.42
0.01
0.32
0.06
0.41
0.00
0.03
0.32
0.00
0.18
0.04
0.08
0.10
0.08
0.42
0.00
0.28
0.00
0.04
0.00
0.38
0.51
0.00
0.07
0.01
0.03
0.00
0.07
0.82
0.00
0.07
0.01
0.14
0.00
0.00
0.54
0.20
0.11
0.00
0.05
0.00
0.11
0.36
0.00
0.48
(k) MPDER
false
true
false
true
0.54
0.46
0.27
0.73
(l) HU
false
true
false
true
0.08
0.92
0.04
0.96
(m) SD
Figure 28: Confusion matrices for LongVA-7B-DPO on each evaluation scenario of EmoBench-M.

--- Page 24 ---

angry
calm
fearful
happy
neutral
sad
angry
calm
fearful
happy
neutral
sad
0.04
0.06
0.01
0.00
0.89
0.00
0.00
0.01
0.00
0.04
0.95
0.00
0.01
0.00
0.07
0.00
0.92
0.00
0.00
0.04
0.00
0.42
0.54
0.00
0.00
0.02
0.00
0.00
0.98
0.00
0.02
0.01
0.01
0.01
0.88
0.06
(a) SOER
angry
calm
disgust
fearful
happy
neutral
sad
surprised
angry
calm
disgust
fearful
happy
neutral
sad
surprised
0.08
0.00
0.00
0.02
0.00
0.87
0.00
0.03
0.00
0.05
0.00
0.00
0.00
0.95
0.00
0.00
0.32
0.02
0.00
0.00
0.00
0.56
0.06
0.03
0.02
0.02
0.00
0.00
0.02
0.84
0.00
0.11
0.00
0.05
0.00
0.00
0.47
0.48
0.00
0.00
0.00
0.03
0.00
0.00
0.00
0.97
0.00
0.00
0.03
0.00
0.00
0.00
0.02
0.89
0.06
0.00
0.02
0.00
0.00
0.02
0.05
0.85
0.00
0.06
(b) SPER
neutral
strong negative
strong positive
weak negative
weak positive
neutral
strong negative
strong positive
weak negative
weak positive
0.79
0.04
0.05
0.11
0.01
0.56
0.06
0.00
0.38
0.00
0.88
0.00
0.12
0.00
0.00
0.73
0.11
0.00
0.16
0.00
0.76
0.04
0.06
0.14
0.00
(c) SCEA
negative
neutral
positive
negative
neutral
positive
0.55
0.40
0.05
0.10
0.80
0.10
0.05
0.40
0.54
(d) OSA
negative
neutral
positive
negative
neutral
positive
0.30
0.67
0.03
0.02
0.88
0.10
0.02
0.65
0.33
(e) EIA
angry
happy
neutral
sad
surprise
worried
angry
happy
neutral
sad
surprise
worried
0.43
0.02
0.23
0.01
0.05
0.27
0.02
0.46
0.43
0.01
0.05
0.02
0.05
0.07
0.69
0.06
0.00
0.14
0.06
0.06
0.28
0.24
0.04
0.32
0.11
0.11
0.39
0.00
0.11
0.28
0.07
0.00
0.19
0.02
0.05
0.67
(f) FGDEA
negative
neutral
positive
negative
neutral
positive
0.54
0.40
0.07
0.14
0.72
0.13
0.06
0.38
0.56
(g) FCDEA
negative
neutral
positive
negative
neutral
positive
0.54
0.37
0.09
0.19
0.59
0.22
0.04
0.32
0.64
(h) PEA
happy
surprise
sad
disgust
anger
fear
neutral
happy
surprise
sad
disgust
anger
fear
neutral
0.46
0.25
0.09
0.00
0.07
0.00
0.12
0.18
0.53
0.05
0.05
0.05
0.02
0.13
0.12
0.19
0.31
0.08
0.12
0.07
0.10
0.15
0.36
0.15
0.15
0.06
0.00
0.12
0.07
0.26
0.19
0.10
0.22
0.00
0.16
0.07
0.43
0.14
0.00
0.04
0.07
0.25
0.24
0.23
0.12
0.05
0.11
0.00
0.25
(i) CEIA (emo.)
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
0.87
0.00
0.04
0.04
0.01
0.02
0.00
0.02
0.29
0.07
0.32
0.14
0.04
0.05
0.00
0.09
0.13
0.00
0.65
0.09
0.04
0.04
0.00
0.04
0.14
0.00
0.24
0.48
0.00
0.10
0.00
0.05
0.34
0.00
0.14
0.14
0.21
0.07
0.00
0.09
0.46
0.02
0.17
0.05
0.05
0.22
0.00
0.02
0.32
0.00
0.13
0.10
0.19
0.23
0.00
0.03
0.32
0.03
0.31
0.04
0.11
0.10
0.03
0.07
(j) CEIA (int.)
anger
disgust
fear
joy
neutral
sadness
surprise
anger
disgust
fear
joy
neutral
sadness
surprise
0.38
0.00
0.04
0.07
0.11
0.08
0.31
0.39
0.09
0.03
0.09
0.13
0.01
0.25
0.12
0.00
0.18
0.14
0.14
0.06
0.36
0.04
0.01
0.00
0.48
0.25
0.01
0.20
0.09
0.00
0.01
0.31
0.39
0.03
0.17
0.15
0.01
0.01
0.04
0.15
0.45
0.17
0.10
0.01
0.00
0.15
0.12
0.00
0.61
(k) MPDER
false
true
false
true
0.72
0.28
0.61
0.39
(l) HU
false
true
false
true
0.92
0.08
0.93
0.07
(m) SD
Figure 29: Confusion matrices for MiniCPM-V-2.6-8B on each evaluation scenario of EmoBench-M.
angry
calm
fearful
happy
neutral
sad
angry
calm
fearful
happy
neutral
sad
0.99
0.00
0.00
0.00
0.00
0.01
0.00
0.00
0.00
0.02
0.69
0.29
0.05
0.00
0.31
0.00
0.00
0.64
0.00
0.00
0.00
0.99
0.01
0.00
0.00
0.00
0.00
0.05
0.66
0.29
0.00
0.00
0.00
0.00
0.00
1.00
(a) SOER
angry
calm
disgust
fearful
happy
neutral
sad
surprised
angry
calm
disgust
fearful
happy
neutral
sad
surprised
1.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.76
0.24
0.00
0.19
0.00
0.00
0.00
0.00
0.00
0.81
0.00
0.00
0.00
0.00
0.68
0.00
0.02
0.29
0.02
0.03
0.00
0.00
0.00
0.89
0.02
0.02
0.05
0.00
0.00
0.00
0.00
0.00
0.91
0.09
0.00
0.00
0.00
0.00
0.00
0.00
0.02
0.98
0.00
0.00
0.00
0.00
0.02
0.02
0.00
0.00
0.97
(b) SPER
neutral
strong negative
strong positive
weak negative
weak positive
neutral
strong negative
strong positive
weak negative
weak positive
0.45
0.15
0.09
0.26
0.05
0.18
0.29
0.00
0.53
0.00
0.38
0.06
0.44
0.00
0.12
0.14
0.30
0.03
0.51
0.03
0.49
0.04
0.31
0.12
0.04
(c) SCEA
negative
neutral
positive
negative
neutral
positive
0.66
0.29
0.05
0.20
0.67
0.13
0.07
0.27
0.67
(d) OSA
negative
neutral
positive
negative
neutral
positive
0.62
0.34
0.04
0.09
0.82
0.09
0.05
0.61
0.34
(e) EIA
angry
happy
neutral
sad
surprise
worried
angry
happy
neutral
sad
surprise
worried
0.79
0.03
0.10
0.08
0.00
0.01
0.17
0.38
0.25
0.18
0.00
0.02
0.19
0.07
0.41
0.26
0.00
0.07
0.16
0.02
0.10
0.64
0.00
0.08
0.44
0.00
0.44
0.12
0.00
0.00
0.29
0.00
0.11
0.16
0.00
0.45
(f) FGDEA
negative
neutral
positive
negative
neutral
positive
0.54
0.33
0.12
0.22
0.54
0.25
0.09
0.32
0.59
(g) FCDEA
negative
neutral
positive
negative
neutral
positive
0.57
0.32
0.11
0.19
0.47
0.34
0.06
0.30
0.64
(h) PEA
happy
surprise
sad
disgust
anger
fear
neutral
happy
surprise
sad
disgust
anger
fear
neutral
0.25
0.00
0.14
0.02
0.00
0.00
0.60
0.18
0.08
0.05
0.00
0.00
0.08
0.62
0.09
0.00
0.57
0.04
0.00
0.05
0.25
0.04
0.00
0.32
0.14
0.00
0.04
0.46
0.07
0.05
0.25
0.13
0.00
0.00
0.51
0.10
0.05
0.27
0.02
0.00
0.05
0.51
0.07
0.00
0.27
0.07
0.00
0.03
0.55
(i) CEIA (emo.)
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
0.89
0.01
0.01
0.01
0.00
0.06
0.00
0.01
0.12
0.05
0.36
0.05
0.00
0.17
0.02
0.24
0.09
0.00
0.86
0.00
0.00
0.00
0.00
0.05
0.09
0.09
0.43
0.13
0.09
0.17
0.00
0.00
0.20
0.02
0.31
0.12
0.08
0.14
0.03
0.09
0.33
0.00
0.09
0.04
0.07
0.44
0.00
0.02
0.25
0.00
0.18
0.07
0.18
0.18
0.11
0.04
0.35
0.01
0.29
0.01
0.10
0.08
0.05
0.10
(j) CEIA (int.)
anger
disgust
fear
joy
neutral
sadness
surprise
anger
disgust
fear
joy
neutral
sadness
surprise
0.00
0.06
0.29
0.08
0.24
0.17
0.17
0.00
0.39
0.21
0.05
0.21
0.06
0.08
0.00
0.02
0.50
0.02
0.21
0.12
0.12
0.00
0.01
0.08
0.55
0.23
0.03
0.10
0.00
0.01
0.11
0.10
0.66
0.04
0.07
0.00
0.07
0.16
0.01
0.24
0.43
0.09
0.01
0.04
0.12
0.14
0.22
0.01
0.45
(k) MPDER
false
true
false
true
0.02
0.98
0.00
1.00
(l) HU
false
true
false
true
0.08
0.92
0.02
0.98
(m) SD
Figure 30: Confusion matrices for Qwen2-Audio-7B-Instruct on each evaluation scenario of EmoBench-M.

--- Page 25 ---

angry
calm
fearful
happy
neutral
sad
angry
calm
fearful
happy
neutral
sad
0.41
0.00
0.08
0.05
0.40
0.06
0.00
0.00
0.00
0.34
0.60
0.06
0.00
0.00
0.34
0.00
0.37
0.29
0.00
0.00
0.00
0.93
0.07
0.00
0.00
0.00
0.00
0.00
0.95
0.05
0.00
0.00
0.01
0.02
0.46
0.51
(a) SOER
angry
calm
disgust
fearful
happy
neutral
sad
surprised
angry
calm
disgust
fearful
happy
neutral
sad
surprised
0.08
0.00
0.05
0.00
0.00
0.26
0.06
0.55
0.00
0.00
0.00
0.00
0.35
0.60
0.02
0.03
0.00
0.00
0.40
0.00
0.00
0.00
0.45
0.15
0.00
0.00
0.00
0.00
0.00
0.21
0.11
0.68
0.00
0.00
0.00
0.00
0.81
0.02
0.02
0.16
0.00
0.00
0.00
0.00
0.00
0.74
0.05
0.21
0.00
0.00
0.00
0.00
0.03
0.32
0.53
0.11
0.00
0.00
0.00
0.00
0.08
0.11
0.00
0.81
(b) SPER
neutral
strong negative
strong positive
weak negative
weak positive
neutral
strong negative
strong positive
weak negative
weak positive
0.93
0.06
0.01
0.00
0.00
0.65
0.29
0.00
0.06
0.00
0.88
0.00
0.12
0.00
0.00
0.65
0.35
0.00
0.00
0.00
0.94
0.02
0.02
0.02
0.00
(c) SCEA
negative
neutral
positive
negative
neutral
positive
0.24
0.73
0.03
0.00
0.93
0.07
0.01
0.67
0.32
(d) OSA
negative
neutral
positive
negative
neutral
positive
0.26
0.71
0.03
0.01
0.95
0.05
0.01
0.69
0.30
(e) EIA
angry
happy
neutral
sad
surprise
worried
angry
happy
neutral
sad
surprise
worried
0.19
0.01
0.34
0.12
0.26
0.08
0.00
0.51
0.39
0.01
0.10
0.00
0.02
0.00
0.72
0.07
0.11
0.08
0.00
0.02
0.18
0.48
0.02
0.30
0.00
0.06
0.44
0.00
0.44
0.06
0.02
0.00
0.42
0.04
0.07
0.46
(f) FGDEA
negative
neutral
positive
negative
neutral
positive
0.24
0.71
0.05
0.03
0.91
0.06
0.00
0.48
0.52
(g) FCDEA
negative
neutral
positive
negative
neutral
positive
0.26
0.68
0.06
0.03
0.84
0.12
0.01
0.43
0.56
(h) PEA
happy
surprise
sad
disgust
anger
fear
neutral
happy
surprise
sad
disgust
anger
fear
neutral
0.15
0.32
0.03
0.00
0.00
0.00
0.51
0.03
0.69
0.00
0.00
0.00
0.00
0.28
0.00
0.39
0.11
0.11
0.00
0.01
0.37
0.02
0.39
0.00
0.20
0.00
0.00
0.39
0.01
0.51
0.06
0.15
0.01
0.00
0.25
0.00
0.46
0.00
0.04
0.02
0.02
0.46
0.01
0.36
0.04
0.02
0.00
0.00
0.57
(i) CEIA (emo.)
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
0.86
0.00
0.05
0.00
0.00
0.05
0.00
0.04
0.27
0.00
0.20
0.02
0.00
0.13
0.00
0.38
0.04
0.00
0.60
0.00
0.00
0.08
0.00
0.28
0.11
0.00
0.39
0.04
0.04
0.21
0.00
0.21
0.29
0.00
0.10
0.04
0.11
0.19
0.01
0.26
0.41
0.00
0.07
0.00
0.00
0.26
0.00
0.26
0.37
0.00
0.15
0.02
0.05
0.12
0.00
0.29
0.40
0.00
0.13
0.00
0.02
0.06
0.00
0.38
(j) CEIA (int.)
anger
disgust
fear
joy
neutral
sadness
surprise
anger
disgust
fear
joy
neutral
sadness
surprise
0.07
0.08
0.00
0.01
0.49
0.01
0.32
0.00
0.16
0.03
0.03
0.43
0.03
0.32
0.02
0.02
0.06
0.02
0.33
0.00
0.55
0.01
0.00
0.00
0.27
0.46
0.01
0.24
0.00
0.00
0.01
0.10
0.75
0.01
0.13
0.01
0.00
0.03
0.01
0.49
0.21
0.24
0.00
0.00
0.00
0.06
0.45
0.01
0.48
(k) MPDER
false
true
false
true
0.82
0.18
0.60
0.40
(l) HU
false
true
false
true
0.41
0.59
0.29
0.71
(m) SD
Figure 31: Confusion matrices for VideoLLaMA2-7B on each evaluation scenario of EmoBench-M.
angry
calm
fearful
happy
neutral
sad
angry
calm
fearful
happy
neutral
sad
0.31
0.00
0.14
0.00
0.49
0.05
0.00
0.00
0.00
0.02
0.95
0.02
0.00
0.00
0.51
0.00
0.41
0.08
0.00
0.00
0.00
0.80
0.20
0.00
0.00
0.00
0.02
0.00
0.93
0.05
0.00
0.00
0.24
0.01
0.60
0.14
(a) SOER
angry
calm
disgust
fearful
happy
neutral
sad
surprised
angry
calm
disgust
fearful
happy
neutral
sad
surprised
0.11
0.00
0.00
0.00
0.00
0.37
0.05
0.47
0.00
0.00
0.00
0.00
0.15
0.84
0.02
0.00
0.00
0.00
0.66
0.11
0.00
0.02
0.16
0.05
0.00
0.00
0.00
0.08
0.00
0.31
0.10
0.52
0.00
0.00
0.00
0.00
0.77
0.05
0.00
0.18
0.00
0.00
0.00
0.00
0.00
0.92
0.06
0.02
0.00
0.00
0.00
0.02
0.00
0.42
0.45
0.11
0.00
0.00
0.00
0.00
0.06
0.29
0.00
0.65
(b) SPER
neutral
strong negative
strong positive
weak negative
weak positive
neutral
strong negative
strong positive
weak negative
weak positive
0.80
0.18
0.02
0.01
0.00
0.47
0.35
0.00
0.18
0.00
0.69
0.12
0.19
0.00
0.00
0.36
0.56
0.03
0.06
0.00
0.70
0.12
0.18
0.00
0.00
(c) SCEA
negative
neutral
positive
negative
neutral
positive
0.78
0.20
0.02
0.33
0.57
0.10
0.24
0.36
0.40
(d) OSA
negative
neutral
positive
negative
neutral
positive
0.57
0.43
0.00
0.15
0.84
0.02
0.06
0.66
0.27
(e) EIA
angry
happy
neutral
sad
surprise
worried
angry
happy
neutral
sad
surprise
worried
0.64
0.00
0.23
0.06
0.05
0.03
0.02
0.55
0.30
0.01
0.12
0.00
0.17
0.02
0.68
0.01
0.09
0.02
0.10
0.02
0.24
0.36
0.08
0.20
0.22
0.00
0.33
0.00
0.39
0.06
0.42
0.00
0.25
0.04
0.04
0.26
(f) FGDEA
negative
neutral
positive
negative
neutral
positive
0.68
0.30
0.02
0.29
0.68
0.03
0.11
0.38
0.51
(g) FCDEA
negative
neutral
positive
negative
neutral
positive
0.22
0.77
0.01
0.00
0.98
0.02
0.01
0.75
0.24
(h) PEA
happy
surprise
sad
disgust
anger
fear
neutral
happy
surprise
sad
disgust
anger
fear
neutral
0.09
0.58
0.01
0.01
0.00
0.00
0.30
0.00
0.77
0.00
0.01
0.00
0.00
0.22
0.00
0.45
0.07
0.19
0.00
0.01
0.29
0.00
0.57
0.00
0.31
0.00
0.00
0.12
0.00
0.47
0.03
0.19
0.07
0.01
0.22
0.00
0.54
0.02
0.11
0.02
0.02
0.28
0.00
0.51
0.02
0.10
0.00
0.01
0.36
(i) CEIA (emo.)
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
0.88
0.01
0.08
0.00
0.00
0.03
0.00
0.00
0.36
0.02
0.49
0.00
0.03
0.07
0.00
0.03
0.26
0.00
0.74
0.00
0.00
0.00
0.00
0.00
0.37
0.04
0.44
0.04
0.00
0.07
0.00
0.04
0.64
0.01
0.15
0.00
0.07
0.04
0.00
0.08
0.67
0.00
0.22
0.00
0.00
0.11
0.00
0.00
0.62
0.03
0.28
0.00
0.05
0.03
0.00
0.00
0.54
0.00
0.40
0.00
0.01
0.00
0.00
0.05
(j) CEIA (int.)
anger
disgust
fear
joy
neutral
sadness
surprise
anger
disgust
fear
joy
neutral
sadness
surprise
0.14
0.10
0.00
0.01
0.46
0.01
0.27
0.08
0.15
0.03
0.02
0.44
0.02
0.27
0.16
0.02
0.08
0.00
0.36
0.00
0.38
0.01
0.06
0.00
0.22
0.45
0.00
0.26
0.01
0.01
0.03
0.03
0.71
0.00
0.21
0.03
0.03
0.06
0.00
0.65
0.14
0.09
0.00
0.02
0.04
0.02
0.43
0.00
0.49
(k) MPDER
false
true
false
true
0.60
0.40
0.25
0.75
(l) HU
false
true
false
true
0.45
0.55
0.26
0.74
(m) SD
Figure 32: Confusion matrices for VideoLLaMA2-7B-16F on each evaluation scenario of EmoBench-M.

--- Page 26 ---

angry
calm
fearful
happy
neutral
sad
angry
calm
fearful
happy
neutral
sad
0.66
0.00
0.01
0.01
0.31
0.00
0.00
0.19
0.00
0.11
0.65
0.05
0.07
0.00
0.24
0.00
0.47
0.22
0.00
0.05
0.00
0.88
0.07
0.00
0.00
0.01
0.00
0.00
0.94
0.05
0.04
0.00
0.00
0.01
0.52
0.43
(a) SOER
angry
calm
disgust
fearful
happy
neutral
sad
surprised
angry
calm
disgust
fearful
happy
neutral
sad
surprised
0.37
0.00
0.00
0.00
0.00
0.48
0.02
0.13
0.00
0.03
0.00
0.00
0.06
0.87
0.03
0.00
0.05
0.00
0.60
0.00
0.00
0.05
0.31
0.00
0.00
0.00
0.00
0.00
0.00
0.65
0.15
0.21
0.00
0.00
0.00
0.00
0.85
0.08
0.00
0.06
0.00
0.00
0.00
0.00
0.00
0.94
0.06
0.00
0.00
0.00
0.00
0.00
0.02
0.45
0.50
0.03
0.02
0.00
0.00
0.00
0.03
0.74
0.00
0.21
(b) SPER
neutral
strong negative
strong positive
weak negative
weak positive
neutral
strong negative
strong positive
weak negative
weak positive
0.90
0.02
0.02
0.03
0.02
0.35
0.29
0.00
0.35
0.00
0.81
0.00
0.12
0.06
0.00
0.68
0.11
0.00
0.22
0.00
0.84
0.02
0.06
0.02
0.06
(c) SCEA
negative
neutral
positive
negative
neutral
positive
0.44
0.55
0.01
0.03
0.90
0.07
0.01
0.48
0.51
(d) OSA
negative
neutral
positive
negative
neutral
positive
0.30
0.70
0.01
0.01
0.98
0.01
0.01
0.78
0.22
(e) EIA
angry
happy
neutral
sad
surprise
worried
angry
happy
neutral
sad
surprise
worried
0.43
0.01
0.37
0.02
0.02
0.15
0.00
0.23
0.75
0.00
0.00
0.02
0.02
0.00
0.89
0.00
0.00
0.09
0.08
0.00
0.36
0.14
0.02
0.40
0.00
0.00
0.56
0.00
0.11
0.33
0.11
0.00
0.44
0.02
0.02
0.42
(f) FGDEA
negative
neutral
positive
negative
neutral
positive
0.32
0.67
0.02
0.04
0.93
0.03
0.02
0.65
0.33
(g) FCDEA
negative
neutral
positive
negative
neutral
positive
0.33
0.65
0.02
0.03
0.86
0.10
0.02
0.56
0.42
(h) PEA
happy
surprise
sad
disgust
anger
fear
neutral
happy
surprise
sad
disgust
anger
fear
neutral
0.38
0.03
0.01
0.01
0.00
0.00
0.57
0.07
0.30
0.00
0.03
0.03
0.00
0.58
0.09
0.04
0.24
0.10
0.10
0.01
0.42
0.07
0.19
0.00
0.26
0.10
0.00
0.38
0.05
0.12
0.07
0.09
0.28
0.01
0.38
0.02
0.15
0.04
0.00
0.06
0.04
0.68
0.06
0.01
0.07
0.03
0.06
0.01
0.75
(i) CEIA (emo.)
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
0.75
0.01
0.10
0.01
0.00
0.03
0.00
0.11
0.00
0.18
0.46
0.00
0.00
0.03
0.00
0.33
0.00
0.04
0.92
0.00
0.00
0.00
0.00
0.04
0.00
0.00
0.63
0.07
0.00
0.13
0.00
0.17
0.07
0.04
0.37
0.01
0.04
0.12
0.01
0.34
0.11
0.04
0.24
0.00
0.00
0.24
0.00
0.38
0.13
0.02
0.18
0.00
0.00
0.11
0.02
0.53
0.10
0.01
0.38
0.00
0.01
0.00
0.01
0.48
(j) CEIA (int.)
anger
disgust
fear
joy
neutral
sadness
surprise
anger
disgust
fear
joy
neutral
sadness
surprise
0.48
0.07
0.03
0.03
0.27
0.01
0.11
0.32
0.40
0.01
0.04
0.16
0.00
0.06
0.10
0.00
0.36
0.06
0.30
0.06
0.12
0.06
0.03
0.00
0.58
0.27
0.01
0.06
0.06
0.03
0.01
0.14
0.68
0.06
0.03
0.20
0.13
0.06
0.00
0.30
0.30
0.03
0.07
0.01
0.02
0.10
0.27
0.03
0.50
(k) MPDER
false
true
false
true
0.37
0.63
0.03
0.97
(l) HU
false
true
false
true
0.02
0.98
0.00
1.00
(m) SD
Figure 33: Confusion matrices for VideoLLaMA2-72B on each evaluation scenario of EmoBench-M.
angry
calm
fearful
happy
neutral
sad
angry
calm
fearful
happy
neutral
sad
0.48
0.00
0.00
0.00
0.52
0.00
0.00
0.00
0.00
0.10
0.89
0.01
0.13
0.00
0.04
0.00
0.81
0.02
0.00
0.00
0.00
0.80
0.20
0.00
0.00
0.00
0.00
0.00
1.00
0.00
0.08
0.00
0.00
0.01
0.76
0.14
(a) SOER
angry
calm
disgust
fearful
happy
neutral
sad
surprised
angry
calm
disgust
fearful
happy
neutral
sad
surprised
0.27
0.00
0.00
0.00
0.00
0.73
0.00
0.00
0.00
0.00
0.00
0.00
0.08
0.92
0.00
0.00
0.44
0.00
0.08
0.00
0.00
0.16
0.32
0.00
0.08
0.00
0.00
0.00
0.00
0.85
0.03
0.03
0.00
0.00
0.00
0.00
0.87
0.13
0.00
0.00
0.00
0.00
0.00
0.00
0.00
1.00
0.00
0.00
0.06
0.00
0.02
0.00
0.00
0.69
0.23
0.00
0.00
0.00
0.00
0.00
0.02
0.97
0.00
0.02
(b) SPER
neutral
strong negative
strong positive
weak negative
weak positive
neutral
strong negative
strong positive
weak negative
weak positive
0.61
0.08
0.16
0.12
0.03
0.12
0.12
0.00
0.71
0.06
0.38
0.00
0.50
0.06
0.06
0.27
0.14
0.03
0.57
0.00
0.49
0.00
0.43
0.04
0.04
(c) SCEA
negative
neutral
positive
negative
neutral
positive
0.88
0.10
0.02
0.57
0.37
0.07
0.18
0.22
0.60
(d) OSA
negative
neutral
positive
negative
neutral
positive
0.74
0.23
0.03
0.21
0.72
0.07
0.10
0.52
0.38
(e) EIA
angry
happy
neutral
sad
surprise
worried
angry
happy
neutral
sad
surprise
worried
0.66
0.02
0.27
0.05
0.00
0.01
0.05
0.52
0.40
0.02
0.00
0.01
0.12
0.03
0.75
0.06
0.00
0.03
0.16
0.04
0.36
0.40
0.02
0.02
0.22
0.11
0.61
0.06
0.00
0.00
0.25
0.00
0.44
0.07
0.00
0.25
(f) FGDEA
negative
neutral
positive
negative
neutral
positive
0.84
0.10
0.05
0.54
0.36
0.10
0.23
0.21
0.56
(g) FCDEA
negative
neutral
positive
negative
neutral
positive
0.84
0.09
0.06
0.59
0.21
0.21
0.22
0.21
0.57
(h) PEA
happy
surprise
sad
disgust
anger
fear
neutral
happy
surprise
sad
disgust
anger
fear
neutral
0.49
0.00
0.03
0.04
0.00
0.00
0.45
0.16
0.16
0.03
0.04
0.00
0.00
0.60
0.13
0.03
0.22
0.11
0.01
0.00
0.49
0.10
0.10
0.00
0.36
0.00
0.00
0.45
0.05
0.04
0.08
0.25
0.07
0.00
0.51
0.11
0.11
0.13
0.04
0.02
0.00
0.59
0.18
0.01
0.08
0.05
0.01
0.00
0.66
(i) CEIA (emo.)
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
0.78
0.02
0.12
0.02
0.01
0.05
0.00
0.00
0.03
0.33
0.50
0.03
0.03
0.05
0.02
0.00
0.00
0.20
0.80
0.00
0.00
0.00
0.00
0.00
0.03
0.27
0.33
0.27
0.00
0.10
0.00
0.00
0.13
0.10
0.46
0.09
0.09
0.11
0.02
0.00
0.18
0.07
0.42
0.05
0.00
0.25
0.02
0.00
0.11
0.09
0.45
0.05
0.02
0.14
0.11
0.02
0.16
0.13
0.61
0.02
0.03
0.02
0.03
0.00
(j) CEIA (int.)
anger
disgust
fear
joy
neutral
sadness
surprise
anger
disgust
fear
joy
neutral
sadness
surprise
0.31
0.06
0.00
0.01
0.56
0.03
0.03
0.24
0.26
0.00
0.01
0.44
0.01
0.03
0.16
0.00
0.12
0.02
0.63
0.02
0.04
0.03
0.00
0.00
0.34
0.61
0.00
0.03
0.01
0.01
0.00
0.03
0.94
0.00
0.00
0.08
0.03
0.00
0.03
0.59
0.24
0.03
0.05
0.02
0.02
0.09
0.58
0.00
0.23
(k) MPDER
false
true
false
true
0.90
0.10
0.55
0.45
(l) HU
false
true
false
true
0.12
0.88
0.04
0.96
(m) SD
Figure 34: Confusion matrices for VideoLLaMA2.1-7B-16F on each evaluation scenario of EmoBench-M.

--- Page 27 ---

angry
calm
fearful
happy
neutral
sad
angry
calm
fearful
happy
neutral
sad
0.73
0.00
0.02
0.04
0.20
0.00
0.02
0.00
0.00
0.19
0.77
0.01
0.37
0.00
0.43
0.00
0.19
0.00
0.01
0.00
0.00
0.86
0.13
0.00
0.04
0.00
0.01
0.00
0.95
0.00
0.41
0.00
0.07
0.02
0.46
0.04
(a) SOER
angry
calm
disgust
fearful
happy
neutral
sad
surprised
angry
calm
disgust
fearful
happy
neutral
sad
surprised
0.44
0.00
0.00
0.00
0.00
0.27
0.00
0.29
0.00
0.00
0.00
0.00
0.18
0.79
0.00
0.03
0.73
0.00
0.13
0.02
0.00
0.06
0.06
0.00
0.16
0.00
0.00
0.05
0.00
0.23
0.00
0.56
0.00
0.00
0.00
0.00
0.74
0.03
0.00
0.23
0.00
0.00
0.00
0.00
0.00
0.82
0.00
0.18
0.35
0.00
0.02
0.00
0.03
0.35
0.11
0.13
0.05
0.00
0.00
0.00
0.08
0.20
0.00
0.67
(b) SPER
neutral
strong negative
strong positive
weak negative
weak positive
neutral
strong negative
strong positive
weak negative
weak positive
0.44
0.34
0.19
0.02
0.00
0.18
0.59
0.00
0.24
0.00
0.25
0.12
0.62
0.00
0.00
0.24
0.51
0.08
0.16
0.00
0.27
0.12
0.59
0.02
0.00
(c) SCEA
negative
neutral
positive
negative
neutral
positive
0.71
0.16
0.12
0.17
0.47
0.37
0.05
0.14
0.81
(d) OSA
negative
neutral
positive
negative
neutral
positive
0.57
0.25
0.18
0.08
0.51
0.42
0.04
0.31
0.66
(e) EIA
angry
happy
neutral
sad
surprise
worried
angry
happy
neutral
sad
surprise
worried
0.71
0.09
0.10
0.02
0.09
0.00
0.10
0.81
0.06
0.01
0.02
0.00
0.33
0.29
0.35
0.00
0.02
0.01
0.29
0.16
0.18
0.31
0.04
0.02
0.28
0.17
0.17
0.00
0.39
0.00
0.54
0.07
0.19
0.02
0.06
0.13
(f) FGDEA
negative
neutral
positive
negative
neutral
positive
0.73
0.11
0.17
0.26
0.32
0.42
0.14
0.09
0.76
(g) FCDEA
negative
neutral
positive
negative
neutral
positive
0.67
0.13
0.20
0.22
0.41
0.36
0.11
0.12
0.77
(h) PEA
happy
surprise
sad
disgust
anger
fear
neutral
happy
surprise
sad
disgust
anger
fear
neutral
0.71
0.01
0.03
0.20
0.00
0.00
0.04
0.19
0.19
0.03
0.40
0.00
0.00
0.18
0.14
0.06
0.17
0.50
0.07
0.01
0.06
0.07
0.03
0.00
0.78
0.03
0.00
0.10
0.07
0.08
0.04
0.59
0.16
0.00
0.05
0.16
0.07
0.05
0.55
0.07
0.02
0.09
0.37
0.01
0.03
0.40
0.02
0.01
0.15
(i) CEIA (emo.)
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
questioning
agreeing
acknowledging
encouraging
consoling
suggesting
wishing
neutral
0.76
0.00
0.17
0.00
0.02
0.04
0.00
0.01
0.18
0.00
0.82
0.00
0.00
0.00
0.00
0.00
0.00
0.00
1.00
0.00
0.00
0.00
0.00
0.00
0.03
0.00
0.72
0.03
0.14
0.07
0.00
0.00
0.21
0.00
0.53
0.03
0.17
0.06
0.00
0.00
0.36
0.00
0.42
0.06
0.08
0.08
0.00
0.02
0.30
0.00
0.53
0.00
0.14
0.02
0.00
0.00
0.37
0.00
0.53
0.00
0.08
0.01
0.01
0.00
(j) CEIA (int.)
anger
disgust
fear
joy
neutral
sadness
surprise
anger
disgust
fear
joy
neutral
sadness
surprise
0.28
0.15
0.03
0.01
0.30
0.00
0.23
0.21
0.47
0.01
0.01
0.24
0.00
0.06
0.21
0.11
0.13
0.02
0.30
0.00
0.23
0.03
0.03
0.01
0.34
0.40
0.00
0.19
0.06
0.08
0.01
0.06
0.73
0.00
0.06
0.19
0.14
0.03
0.04
0.50
0.07
0.03
0.07
0.07
0.01
0.07
0.35
0.00
0.43
(k) MPDER
false
true
false
true
0.24
0.76
0.17
0.83
(l) HU
false
true
false
true
0.14
0.86
0.08
0.92
(m) SD
Figure 35: Confusion matrices for VideoLLaMA2.1-7B-AV on each evaluation scenario of EmoBench-M.

--- Page 28 ---

F
Prompt
Prompt From RAVDESS(song)
Please watch the provided video and determine the emotion
it conveys. Do not provide any additional explanations or
extra content. Choose one of the following labels as your
final answer: neutral, calm, happy, sad, angry, fearful. Re-
spond in the format: {’emotion’: ’label’}.
Prompt From RAVDESS(speech)
Please watch the provided video and determine the emo-
tion it conveys.Do not provide any additional explanations
or extra content. Choose one of the following labels as
your final answer: neutral, calm, happy, sad, angry, fear-
ful, surprised, disgust. Respond in the format:{’emotion’:
’label’}.
Prompt From CH-SIMSv2
The person in video says: {Subtitle}. Determine the emo-
tion conveyed. Do not provide any additional explanations
or extra content. Choose one of the following labels as your
final answer: neutral, negative, positive. Respond in the for-
mat: {’emotion’: ’label’}.
Prompt From FMSA-SC
The person in video says: {Subtitle}. Determine the emo-
tion conveyed. Do not provide any additional explanations
or extra content. Choose one of the following labels as
your final answer: weak negative, strong negative, neu-
tral, strong positive, weak positive. Respond in the format:
{’emotion’: ’label’}.
Prompt From UR-FUNNY
The context sentences in the video is: {context sentences}.
The punchline sentence in the video is: {punchline sen-
tence}. Choose one of the following labels as your final
answer: true, false.
Prompt From MC-EIU
The person in video says:{Subtitle}. Analyze the emotion
and intent. Choose one emotion: happy, surprise, sad, dis-
gust, anger, fear, and neutral. Choose one intent: ques-
tioning, agreeing, acknowledging, encouraging, consoling,
suggesting, wishing, and neutral. Respond in the format:
{’emotion label’: ’label’, ’intent label’: ’label’}.
Prompt From MELD
The person in video says: {subtitle}. Do not provide any
additional explanations or extra content.
Choose one of
the following labels as your final answer: neutral, surprise,
fear, sadness, joy, disgust, anger. Respond in the format:
{’emotion’: ’label’}.
Prompt From MER2023
The person in video says: {Subtitle}.
Do not provide
any additional explanations or extra content. Choose one
of the following labels as your final answer: happy, sad,
neutral, angry, worried, surprise. Respond in the format:
{’emotion’: ’label’}.
Prompt From CMU-MOSI
The person in video says: {Subtitle}. Do not provide any
additional explanations or extra content.
Choose one of
the following labels as your final answer: neutral, negative,
positive. Respond in the format: {’emotion’: ’label’}.
Prompt From CMU-MOSEI
The person in video says: {Subtitle}. Do not provide any
additional explanations or extra content.
Choose one of
the following labels as your final answer: neutral, negative,
positive. Respond in the format: {’emotion’: ’label’}.
Prompt From MUStARD
The person in video says: {Subtitle}. Does this statement
express sarcasm? Do not provide any additional explana-
tions or extra content. Choose one of the following labels
as your final answer: true, false.
Prompt From CH-SIMS
The person in video says: {Subtitle}. Choose one of the
following labels as your final answer: neutral, negative,
positive. Respond in the format: {’emotion’: ’label’}.
Prompt From SMILE
Reasoning task:
you are to answer why the audience
laughed given the video clip. The video clip from the Sit-
com, titled {video title}, with multimodal information (Ut-
terance, Facial Action Units, Video caption, Acoustic fea-
tures(6 dimension; 1.mean of F0 contour, 2.var of F0 con-
tour, 3. mean of energy contour, 4. var of energy contour,
5. jitter, 6. shimmer)) is given. The audience laughing
moment is marked as (audience laughing) in certain utter-
ances Explain why the audience laughed given the video
clip, at most 40 words, starting with ’The audience laughed
because ’. Given video clip: {query}.

--- Page 29 ---

G
Evaluation Prompt for SMILE Dataset
Prompt From Logical Judgment Dimension Evalua-
tion Criteria for Model-Generated Reasoning
You need to evaluate the quality of model-generated reason-
ing for why a video audience laughed. You will be provided
with two reasons for laughter reasoning:
1. The reason for laughter generated by the model. 2. The
reference reason for laughter is annotated manually (as a
benchmark).
Please score based on the following dimension, with a max-
imum of 5 points:
Logical Judgment Dimension: Based on the reference
reason, evaluate the model-generated reason in terms of
logical clarity, the rationality of the causal chain, and co-
herence with the context.
Scoring Criteria:
• 1 Point: The reasoning lacks logic, with unclear or
missing causal relationships, and is incoherent with
the context.
• 2 Points: The reasoning has some logical flaws and
partial causal connections but is largely incoherent
with the context.
• 3 Points: The reasoning is moderately logical, with
clear causal links, though some minor inconsistencies
with the context exist.
• 4 Points:
The reasoning is mostly logical, with
well-defined causal relationships and strong coher-
ence with the context.
• 5 Points: The reasoning is fully logical, with clear
and rational causal chains and excellent coherence
with the context.
Input:
• Reference Reason: <reference reason>
• Generated Reason: <generated reason>
Output Format: Please strictly follow the format below
to output the scoring result, and only output the scoring
result without adding any additional explanations or text:
Logical Judgment Dimension:
<score>
Prompt from Multimodal Content Association Di-
mension Evaluation Criteria for Model-Generated
Reasoning
You need to evaluate the quality of model-generated reason-
ing for why a video audience laughed. You will be provided
with two reasons for laughter reasoning:
1. The reason for laughter generated by the model. 2. The
reference reason for laughter is annotated manually (as a
benchmark).
Please score based on the following dimension, with a max-
imum of 5 points:
Multimodal Content Association Dimension: Based on
the reference reason, evaluate whether the generated text
accurately reflects the interactions between language, vi-
sual, audio, and other modal contents, especially whether
these contents are consistent with the triggers for laughter.
Scoring Criteria:
• 1 Point: The reasoning fails to associate with mul-
timodal content, showing no consistency with lan-
guage, visual, audio, or other modalities.
• 2 Points: The reasoning shows minimal association
with multimodal content, with limited consistency
and several mismatches.
• 3 Points: The reasoning moderately reflects multi-
modal interactions, maintaining some consistency but
with noticeable gaps.
• 4 Points: The reasoning strongly associates with mul-
timodal content, showing clear consistency with most
language, visual, audio, and other modalities.
• 5 Points: The reasoning perfectly captures and re-
flects the interactions between all relevant multimodal
contents, with complete consistency with the triggers
for laughter.
Input:
• Reference Reason: <reference reason>
• Generated Reason: <generated reason>
Output Format: Please strictly follow the format below
to output the scoring result, and only output the scoring
result without adding any additional explanations or text:
Multimodal Content Association
Dimension:
<score>

```
