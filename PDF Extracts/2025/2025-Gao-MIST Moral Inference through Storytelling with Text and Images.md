---
title: "2025-Gao-MIST Moral Inference through Storytelling with Text and Images - PDF Extract"
source_pdf: "2025-Gao-MIST Moral Inference through Storytelling with Text and Images.pdf"
pages: 7
extracted_at: "2026-02-08T08:04:10.969259"
---

# PDF Extract: 2025-Gao-MIST Moral Inference through Storytelling with Text and Images

**Source PDF:** 2025-Gao-MIST Moral Inference through Storytelling with Text and Images.pdf
**Total Pages:** 7

---

## Content

```
--- Page 1 ---

.
.
Latest updates: hps://dl.acm.org/doi/10.1145/3746252.3760884
.
.
SHORT-PAPER
Think it Image by Image: Multi-Image Moral Reasoning of Large Vision-
Language Models
CHUJIE GAO, University of Notre Dame, Notre Dame, IN, United States
.
YUE HUANG, University of Notre Dame, Notre Dame, IN, United States
.
XIANGQI WANG, University of Notre Dame, Notre Dame, IN, United States
.
SIYUAN WU, Chinese University of Hong Kong, Hong Kong, Hong Kong
.
NITESH V. CHAWLA, University of Notre Dame, Notre Dame, IN, United States
.
XIANGLIANG ZHANG, University of Notre Dame, Notre Dame, IN, United States
.
.
.
Open Access Support provided by:
.
University of Notre Dame
.
Chinese University of Hong Kong
.
PDF Download
3746252.3760884.pdf
08 February 2026
Total Citations: 0
Total Downloads: 132
.
.
Published: 10 November 2025
.
.
Citation in BibTeX format
.
.
CIKM '25: The 34th ACM International
Conference on Information and
Knowledge Management
November 10 - 14, 2025
Seoul, Republic of Korea
.
.
Conference Sponsors:
SIGWEB
SIGIR
CIKM '25: Proceedings of the 34th ACM International Conference on Information and Knowledge Management (November 2025)
hps://doi.org/10.1145/3746252.3760884
ISBN: 9798400720406
.

--- Page 2 ---

Think it Image by Image: Multi-Image Moral Reasoning of Large
Vision-Language Models
Chujie Gao
University of Notre Dame
Indiana, USA
cgao2@nd.edu
Yue Huang
University of Notre Dame
Indiana, USA
yhuang37@nd.edu
Xiangqi Wang
University of Notre Dame
Indiana, USA
xwang76@nd.edu
Siyuan Wu
The Chinese University of Hong Kong
Hong Kong, China
nauyisu022@gmail.com
Nitesh V. Chawla
University of Notre Dame
Indiana, USA
nchawla@nd.edu
Xiangliang Zhang∗
University of Notre Dame
Indiana, USA
xzhang33@nd.edu
Abstract
Vision Language Models (VLMs) have demonstrated remarkable
success in downstream applications, yet they often exhibit biases,
raising ethical concerns. While previous efforts have aimed to eval-
uate and improve the moral reasoning capabilities of VLMs, ex-
isting approaches are limited by simplified, unimodal settings or
overly static visual scenarios. We propose a novel multi-image-
based dataset pipeline MIST (Moral Inference through Storytelling
with Text and Images) designed to assess moral reasoning in com-
plex, dynamic scenarios to address these limitations. To ensure
better alignment between these modalities, we introduce the con-
cept of “text-image flow," which seamlessly integrates visual and
textual information across complex scenarios. Using this dataset,
we evaluate seven widely used VLMs, offering critical insights into
their performance in moral reasoning tasks.
CCS Concepts
• Computing methodologies →Artificial intelligence.
Keywords
Vision Language Model; Multimodal Moral Reasoning; Text-Image
Flow; AI Ethics
ACM Reference Format:
Chujie Gao, Yue Huang, Xiangqi Wang, Siyuan Wu, Nitesh V. Chawla,
and Xiangliang Zhang. 2025. Think it Image by Image: Multi-Image Moral
Reasoning of Large Vision-Language Models. In Proceedings of the 34th ACM
International Conference on Information and Knowledge Management (CIKM
’25), November 10–14, 2025, Seoul, Republic of Korea. ACM, New York, NY,
USA, 6 pages. https://doi.org/10.1145/3746252.3760884
∗Corresponding author.
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for third-party components of this work must be honored.
For all other uses, contact the owner/author(s).
CIKM ’25, Seoul, Republic of Korea.
© 2025 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2040-6/2025/11
https://doi.org/10.1145/3746252.3760884
1
Introduction
Vision Language Models (VLMs) excel on various vision tasks [2,
16, 18] but can produce unfair or biased outputs [13], motivating
moral reasoning evaluations and fairness improvements [10, 33].
Vision Language Model
(a) Single 
image
Stereotype text: Crimean people live near the Black Sea. The person near the Black 
Sea loves Vodka and shooting AK-47s.
(b) Multiple 
images
This image shows a Crimean 
person holding a weapon and 
a drink, by the water. It’s 
difficult to determine the exact 
context or meaning behind it.
This portrayal of Crimean people is not 
right. It is a dangerous and harmful 
generalization. Judging an entire population 
based on a single image is misleading and 
perpetuates stereotypes.
The geographical setting depicted in 
figure 1 introduces the people of 
interest. The lifestyle and 
preferences of the individuals are 
illustrated in figure 2, highlighting 
their affinity for certain activities.
Figure 1: Comparison of single and multiple images in repre-
senting stereotypes.
Despite these efforts, existing evaluation methodologies tend
to rely on simplified settings, either targeting a single modality
(e.g., text-only or image-only [5, 25]) or using simple visual sce-
narios [28]. For example, stereotype evaluations often focus on
static, isolated elements [14], constraining models’ ability to han-
dle more complex tasks that require a nuanced understanding of
both modalities and intricate scenarios. Constructing such com-
plex multimodal scenarios presents two key challenges: 1) Limited
Expressiveness of a Single Image. While a single image can
capture detailed characteristics, it struggles to convey temporal or
dynamic events. This is particularly problematic for constructing
scenes involving sequences of actions or interactions over time (e.g.,
depicting cause-and-effect relationships or evolving social dynam-
ics). As shown in Figure 1, a single image cannot fully represent
the progression of biased scenarios. 2) Maintaining Text-Image
Correlation in Complex Scenarios. Real-world applications of
VLMs require visual and textual inputs to mutually reinforce each
other. However, Chen et al. [3] revealed shortcomings in current
multimodal evaluations, where models can answer approximately
40% of questions correctly even without images, indicating a weak
interdependence between the two modalities that impedes compre-
hensive multimodal understanding.
4722

--- Page 3 ---

CIKM ’25, November 10–14, 2025, Seoul, Republic of Korea.
Chujie Gao et al.
Fairness
Dataset
CrowS-Pairs & StereoSet
Filter
Ethics
Dataset
Social Chemistry 101 Dataset
Action
Story
Stage 1
Story
Ki scenes
...
Ki ∈ [2,5]
ci,1
ci,Ki
xi
...
ci,j
The identity or 
action
di,j
Image 
description
...
Remove
Placeholder fig j
c’i,j || fig j
Narrative si
Stage 2
ci,2
di,1
...
Image
description set
di,2
di,3
di, Ki
AVG (Stereotype score + 
Disparagement score) > 8
Story
Interrupting your professor 
during a lecture 
[Judgement: bad]
Text-to-Image Model
Ii,1
Ii,2
...
Ii,3
Ii, Ki
Generated Images
Merge and Compress
...
Interrupting your professor 
during a lecture, you loudly 
questioned his credentials, 
causing an uproar and ...
I saw groups of blacks in 
increasing number, I know 
they were all part of a gang, 
those people usually are.
Stage 3
Diversity enhancer
Human review
Text-image flow
c’i,1 || fig 1 || ... || c’i,    || fig 
Ki
Ki
Ii
si~
Ii,1
Ii,2
Ii,3
Ii, Ki
Figure 2: The overall pipeline integrates storytelling and multi-image generation to assess moral reasoning in VLMs.
To address these challenges, we evaluate whether VLMs can
“think step by step” in moral reasoning. In particular, to mitigate
the limitations of a single image, we propose a multi-image-based
moral reasoning dataset pipeline MIST (Moral Inference through
Storytelling with Text and Images), where each data instance con-
sists of a sequence of images that jointly depict a complete and
complex scenario. Temporal progression can reveal implicit biases
or ethical issues that are not apparent in a single snapshot, such
as cause–and–effect chains or escalating interactions. In MIST, to
enhance the alignment between text and images, we introduce the
concept of “text-image flow”, which ensures a seamless and coher-
ent transfer of information between the two modalities, enabling
better contextual understanding.
In this paper, our goal is to systematically evaluate whether
VLMs can detect fairness issues and make ethical judgments when
complex scenarios are presented as text accompanied by a sequence
of images. Our key contributions are as follows: 1) We propose a
multi-image-based dataset pipeline to address the limitations of
single images in capturing dynamic events. 2) We introduce “text-
image flow” to enhance coherence between modalities in complex
scenarios. 3) We evaluate 7 VLMs on the new dataset, providing
critical insights into their ability to perform moral reasoning.
2
Related Work
Several benchmarks have been introduced to measure social bias in
VLMs. For stereotype assessment, StereoSet-VL evaluated stereo-
typical biases [36] and MMBias addressed multiple bias dimensions
[13]. GenderBias-VL targeted occupation-related gender bias [33],
while Sathe et al. [26] contributed automated methods for bias
evaluation, reducing reliance on manual annotation. Additionally,
research on machine ethics in VLMs has gained traction. Roger
[23], Roger et al. [24] focused on creating multimodal datasets for
ethical decision-making, and Hu et al. [10] introduced VIVA, a
benchmark for evaluating ethical reasoning in VLMs. Zhang et al.
[34] employed a preference selection query with related images to
evaluate VLMs’ preference biases. Other researchers have focused
on strategies to mitigate stereotypes [9, 27, 32] and address issues
of disparagement [29]. The Cℎ3Ef dataset [28] was developed to
assess the HHH principles (helpful, honest, and harmless). Tu et al.
[30] found that visual instruction tuning unexpectedly improves
both truthfulness and ethical alignment in text-only settings.
3
MIST Framework
Overview. In this section, we introduce MIST, a pipeline for con-
structing a multi-image-based moral reasoning dataset based on
text-image flow, as illustrated in Figure 2. First, MIST processes
the original dataset X to generate stories containing unfair or un-
ethical elements. Each story instance 𝑥𝑖in X is divided into 𝐾𝑖
scenes denoted as {𝑐𝑖,1, . . . ,𝑐𝑖,𝐾𝑖}, and each 𝑐𝑖,𝑗is transformed into
narrative 𝑠𝑖,𝑗and accompanied by image description 𝑑𝑖,𝑗generated
by a GPT-4o. After that, Dalle-3 generates image 𝐼𝑖,𝑗from the de-
scription 𝑑𝑖,𝑗, forming text-image pairs. To curb templated phrasing
and broaden linguistic coverage, we pass each narrative through a
diversity-enhancer module Ψdiv, which performs controlled para-
phrasing and stylistic variation, yielding ˜𝑠𝑖, 𝑗= Ψdiv(𝑠𝑖,𝑗). Finally,
human review ensures their quality and coherence before they are
utilized for evaluation.
3.1
Preliminary: Dataset Selection
Based on the prior study [11], we selected datasets along two di-
mensions—fairness and machine ethics. For fairness, data instances
contain biased or stereotypical content that VLMs are expected
to detect and reject, whereas in the ethics setting, each instance
describes an action that must be classified as morally good or bad.
Dataset for Fairness Evaluation. For assessing fairness, we
utilized the CrowS-Pairs [20] and StereoSet [19] datasets, both
of which are widely adopted for evaluating stereotypes within
language models [4]. However, we encountered challenges when
translating certain stereotypical text from these datasets (e.g., "The
uneducated are so naive about the ways of the world") into visual
form, as such content is often not explicit enough in images to
be considered biased or unfair. Consequently, given the limited
4723

--- Page 4 ---

Think it Image by Image: Multi-Image Moral Reasoning of Large Vision-Language Models
CIKM ’25, November 10–14, 2025, Seoul, Republic of Korea.
expressive capacity of individual images, we carefully selected text
samples that conveyed explicit and strongly unfair content. Follow-
ing the methodology of a previous study [4], we assessed two key
aspects of the data: stereotype and disparagement, to evaluate the
suitability of each sample. Using the LLM-as-a-Judge framework
[35], we rated each item on these two dimensions and computed an
average score. By applying a threshold-based filter, we identified
samples that were sufficiently unfair and aggressive for inclusion in
our evaluation. The stereotype statements from these two datasets
were used as the basis for generating stories.
Dataset for Machine Ethics Evaluation. To evaluate the ma-
chine ethics of VLMs, we selected the Social-Chemistry-101 dataset
[6], a resource widely used in this context [11, 12]. Each data in-
stance in this dataset consists of a behavior or scenario paired with
its corresponding moral judgment (i.e., whether it is good or bad).
To generate text stories, we expanded each behavior-judgment pair
into longer narratives using LLMs.
Overall, the dataset consists of 669 data instances, of which 235
are allocated for fairness evaluation and 434 for ethics evaluation.
These instances were selected through human review from an initial
pool of 1,000 generated instances, equally divided between the two
evaluation categories (500 each).
3.2
Stage 1: Generate Text-Centric Narrative
After collecting stories from the fairness and ethics datasets, we
focus on constructing coherent narratives paired with image de-
scriptions, employing GPT-4o to automate the scene division and
narrative generation process. First, each story 𝑥𝑖is automatically
partitioned by GPT-4o into 𝐾𝑖distinct scenes {𝑐𝑖,1, . . . ,𝑐𝑖,𝐾𝑖}, where
𝐾𝑖∈[2, 5] is chosen dynamically according to the story’s length
and complexity. We limit 𝐾𝑖up to five to prevent excessive infor-
mation loss, as distributing content across too many images can
dilute the overall meaning.
For every scene 𝑐𝑖,𝑗, the same model identifies the entity or ac-
tion that carries the core moral or social signal and rewrites it as a
concise textual cue 𝑑𝑖,𝑗. The focal entity is first removed from 𝑐𝑖,𝑗
to obtain the redacted text 𝑐′
𝑖,𝑗; we then append the corresponding
placeholder tag fig𝑗, so the resulting narrative fragment becomes
𝑐′
𝑖,𝑗∥fig𝑗. Concatenating the redacted scenes and their correspond-
ing tags yields a single narrative string:
𝑠𝑖= 𝑐′
𝑖,1 ∥fig1 ∥· · · ∥𝑐′
𝑖,𝐾𝑖∥fig𝐾𝑖,
preserving the original flow while explicitly marking where each
future image should appear, and {𝑑𝑖,1, . . . ,𝑑𝑖,𝐾𝑖} are retained as
metadata to guide the text-to-image (T2I) model applied in Stage 2.
To maintain narrative consistency (e.g., character gender) and to
avoid unintended visual leakage, we explicitly include these require-
ments in the LLM prompt. Finally, human reviewers verify every
(𝑐𝑖,𝑗,𝑑𝑖,𝑗) pair and any disagreement triggers manual revision.
3.3
Stage 2: Construct Narrative-Image Pairs
In this stage, the image descriptions {𝑑𝑖,1, . . . ,𝑑𝑖,𝐾𝑖} are then fed
into a T2I model (i.e., Dalle-3) to generate corresponding images
{𝐼𝑖,1, . . . , 𝐼𝑖,𝐾𝑖}, which are then combined into a single composite
image. To facilitate efficient evaluation, the composite images are
compressed to maintain a small file size.
For task construction, a question template is added to the nar-
rative 𝑠𝑖. In fairness evaluations, VLMs are tested on stereotype
detection (i.e., identifying stereotypes within the data). For ethics
evaluations, VLMs perform ethical action classification (i.e., deter-
mining the behavior in the narrative is morally good or bad).
3.4
Stage 3: Ensure Data Instance Quality
To maintain the quality and diversity of the data instances, we
introduce a diversity enhancement process powered by GPT-4o.
The diversity enhancer performs three core transformations to
avoid biases in generated content: 1) Expression transformation
modifies sentence structures by switching between declarative, im-
perative, conditional, and passive/active voice while preserving
original meaning; 2) Length adjustment systematically shortens or
lengthens sentences while maintaining semantic content; and 3)
Sentence paraphrasing employs alternative vocabulary and gram-
matical structures to convey identical meanings. Prompt templates
constrain each operation to maintain semantics while increasing
linguistic variety. This automated process addresses common issues
such as repetitive expressions, fixed sentence patterns, and limited
stylistic diversity that can emerge from template-based genera-
tion. After enhancing the narrative and generating corresponding
images, human reviewers conduct a final review for narrative dis-
cretion, text–image coherence, and linguistic fluency.
4
Experiment Setup
Selected Model. We select the seven models for evaluation, which
include both open-weight and proprietary ones from various devel-
opers, as shown in Table 1.
Table 1: The details of selected models.
Model
Model Size
Open-Weight
Creator
Llama-3.2-V [17]
90B
✓
Meta
GPT-4o [22]
N/A
✗
OpenAI
GPT-4o-mini [21]
N/A
✗
OpenAI
Claude-3.5-Sonnet [1]
N/A
✗
Anthropic
Qwen-2-VL [31]
72B
✓
Qwen
Gemini-1.5-pro [8]
N/A
✗
Google
GLM-4V-Plus [7]
N/A
✓
Zhipu
Evaluation Method and Metrics. We adopt GPT-4o into the
LLM-as-a-Judge framework [15, 35] for evaluation.
Specifically, for fairness assessment, the judge model is provided
with an unfair statement (i.e., the ground-truth) and required to
perform binary classification based on two criteria: 1) whether
the model identifies bias or stereotypes in the given scenario, and
2) whether the model actively opposes the biased viewpoint. For
ethics evaluation, the judge model receives the ground-truth labels
for each case (i.e., whether an action is ethically good or bad) and
evaluates the extent to which the model’s responses align with
these ground-truth labels. In both evaluation tasks, we use accuracy
as the performance metric. Moreover, during all experiments, the
temperature of all models was set to 0 and retained default values
for all other hyperparameters (e.g., top-p).
While LLM-as-a-Judge is widely used, it may exhibit biases
(e.g., positional, verbosity). To reduce such risks, we standardized
4724

--- Page 5 ---

CIKM ’25, November 10–14, 2025, Seoul, Republic of Korea.
Chujie Gao et al.
Table 2: Accuracy on the ethics cases of different labels (i.e., good and bad).
Model
GPT-4o-mini
GPT-4o
GLM-4V-Plus
Llama-3.2-90B-V
Claude-3.5-Sonnet
Qwen2-VL-72B
Gemini 1.5 Pro
Good
0.967
0.972
0.983
0.028
0.923
0.972
0.779
Bad
0.723
0.870
0.791
0.549
0.719
0.842
0.549
|Δ|
0.244
0.102
0.192
0.521
0.204
0.130
0.230
prompts and conducted sampled human reviews, which showed
high consistency with the automatic judgments.
5
Result Analysis
We show the overall performance of seven VLMs in Figure 3, the
accuracy on the ethics cases of different labels in Table 2, and the
model performance under different image numbers in Figure 4.
Significant inconsistent performance across models in
both tasks. As shown in Figure 3, model accuracies exhibit con-
siderable divergence. For example, GPT-4o and Claude-3.5-Sonnet
show relatively strong performance, while Llama-3.2-90B-V per-
forms poorly, with a significantly lower bar than other models.
This pronounced disparity among the latest state-of-the-art models
underscores substantial gaps in moral reasoning capabilities and
highlights the areas for future model development.
GPT-4o-
mini
GPT-4o
GLM-
4V-plus
Llama-
3.2-90B-V
Claude-3.5-
sonnet
Qwen2-
VL-72B
Gemini-
1.5-pro
0.0
0.2
0.4
0.6
0.8
Accuracy
Fairness
Ethics
Figure 3: Model performance on fairness and machine ethics.
GPT-4o
-mini
GPT-4o
GLM-4V
-plus
Llama-3.2
-90B-V
Claude-3.5
-sonnet
Qwen2-VL
-72B
Gemini-1.5
-pro
0.0
0.2
0.4
0.6
0.8
1.0
Acc (Fairness)
GPT-4o
-mini
GPT-4o
GLM-4V
-plus
Llama-3.2
-90B-V
Claude-3.5
-sonnet
Qwen2-VL
-72B
Gemini-1.5
-pro
0.0
0.2
0.4
0.6
0.8
1.0
Acc (Ethics)
N = 2
N = 3
N = 4
N = 5
Figure 4: Model performance under the condition of different
image numbers.
Models perform better on cases with “good” label com-
pared to “bad” label. A noticeable pattern in Table 2 is that most
VLMs perform better on cases labeled “good” than on those labeled
“bad”. For example, GPT-4o-mini attains an accuracy of 0.967 on
“Good" cases versus 0.723 on “Bad", and Claude-3.5-Sonnet scores
0.923 on “Good" compared to 0.719 on “Bad". This suggests that
these models may be better at identifying or aligning with positive
actions or statements, possibly due to inherent biases in training
data, which might contain more positively framed examples.
Performance Declines When the Number of Images Ex-
ceeds Two. As shown in Figure 4, it is evident that most VLMs
lack robustness when faced with a sudden increase in the num-
ber of images. For example, in the ethics domain, the performance
of Gemini-1.5-Pro dropped by nearly 20% when the image count
increased from two. Similar trends were observed with GPT-4o-
mini and GPT-4o. However, the negative impact tends to diminish
when the number of images exceeds three. This suggests that VLMs
continue to face challenges in reasoning with multiple images.
6
Ablation Studies
Then, We would like to emphasize that our method enables the
detection of implicit bias in VLMs. This is achieved through our
pipeline, where the narrative and each sub-image are individually
bias-free, but their combination via text-image flow can imply bi-
ased reasoning, enabling the detection of implicit biases in VLMs.
We validate this with three input settings—Text-only (using the
original dataset text), Image-only (using generated images with-
out any narrative), and MIST-Complete (using the full pipeline
with text-image flow)—with results in Table 3.
Table 3: Comparison of fairness accuracy (%) with text-only,
MIST, and image-only input modalities, where “T-only" de-
notes “Text-only" and “I-only" denotes “Image-only".
Model
Fairness
Ethics
T-only
MIST
I-only
T-only
MIST
I-only
GPT-4o-mini
95.32
54.51
26.81
87.24
83.45
32.25
GPT-4o
94.47
71.25
44.26
82.83
92.31
40.60
GLM-4V-Plus
96.14
50.43
49.36
87.12
87.70
76.57
Llama-3.2-90B-V
96.60
13.62
4.68
87.70
33.41
2.32
Claude-3.5-Sonnet
99.15
85.11
69.94
82.37
80.97
55.92
Qwen2-VL-72B
99.15
50.86
59.17
87.24
90.47
83.87
Gemini-1.5-Pro
99.57
91.63
89.36
87.70
64.97
83.06
From these results, we can observe that for most models, the
accuracy when only text is provided is significantly higher than
with our full dataset. This indicates that explicit bias in text is rela-
tively easy for models to detect. Conversely, when only images are
provided, the accuracy is noticeably lower than with our pipeline.
This demonstrates that the absence of a text-image flow results in
decreased performance for VLMs. These experiments effectively
demonstrate the validity and strength of our proposed pipeline.
7
Conclusion
In this paper, we introduced a multi-image-based dataset pipeline
and the concept of "text-image flow" to address limitations in VLMs’
ability to handle complex, dynamic scenarios for moral reasoning.
Our evaluation of seven VLMs demonstrated the importance of mul-
timodal coherence for improving ethical reasoning, which provides
a foundation for future work.
4725

--- Page 6 ---

Think it Image by Image: Multi-Image Moral Reasoning of Large Vision-Language Models
CIKM ’25, November 10–14, 2025, Seoul, Republic of Korea.
GenAI Usage Disclosure
1. Dataset Processing and Augmentation
Fairness data items construction pipeline. Initially, each
candidate entry was evaluated by GPT-4o (via Azure, accessed De-
cember 2024) acting as a judge on two dimensions: stereotyping
and disparagement (scores on a 1–10 scale). Entries with an average
score greater than 8 were selected for further processing. Next, we
used GPT-4o to segment the remaining stories into 2–5 scenes, gen-
erate corresponding placeholder narratives, and produce detailed
image descriptions for each scene.
Ethics data items construction pipeline. After filtering all the
“good”/“bad” entries, we employed GPT-4o (via Azure, accessed De-
cember 2024) to expand each “action” into a concise story preserving
its original judgment. Subsequent scene segmentation, placeholder
narrative, and image description generation mirrored the procedure
in the fairness pipeline.
2. Image Generation and Diversity Enhancer
Scene images were synthesized with OpenAI’s DALL·E-3 (ac-
cessed January 2025) based on the image descriptions. The per-scene
PNGs were merged horizontally into composite images and con-
verted to compressed JPEGs without additional AI assistance. Sub-
sequently, all three operations of the diversity enhancer—expression
transformation, length adjustment, and sentence paraphrasing—were
performed using GPT-4o (accessed February 2025).
3. Model Evaluation
We evaluated seven VLMs—GPT-4o-mini, GPT-4o, GLM-4V-Plus,
Llama-3.2-90B-V, Claude-3.5-Sonnet, Qwen2-VL-72B, and Gemini
1.5 Pro—all accessed in March 2025 under default settings.
4. Code Development and Debugging
During implementation of both pipelines, GitHub Copilot sug-
gested boilerplate code and identified syntax errors. Every Copilot
suggestion was manually reviewed and, when necessary, substan-
tially modified by the authors before inclusion.
5. Manuscript Preparation
The core text was written exclusively by the authors. Grammar
and punctuation corrections were performed using Grammarly
(accessed May 2025). Light polishing was done via GPT-o3 and
GPT-o4-mini (accessed May 2025).
6. Policy Compliance
This work strictly follows the ACM Authorship Policy (“New
Policy on Authorship”) and ACM FAQ on GenAI. All GenAI usage
has been transparently disclosed. No essential research contribution
relies solely on unedited AI output.
References
[1] Anthropic. 2024. Claude 3.5: A Sonnet. https://www.anthropic.com/news/claude-
3-5-sonnet. Accessed: 2024-09-04.
[2] Dongping Chen, Yue Huang, Siyuan Wu, Jingyu Tang, Liuyi Chen, Yilin Bai,
Zhigang He, Chenlong Wang, Huichi Zhou, Yiqiang Li, et al. 2024. GUI-WORLD:
A Dataset for GUI-oriented Multimodal LLM-based Agents.
arXiv preprint
arXiv:2406.10819 (2024).
[3] Lin Chen, Jinsong Li, Xiaoyi Dong, Pan Zhang, Yuhang Zang, Zehui Chen,
Haodong Duan, Jiaqi Wang, Yu Qiao, Dahua Lin, et al. 2024.
Are We on
the Right Way for Evaluating Large Vision-Language Models? arXiv preprint
arXiv:2403.20330 (2024).
[4] Sunipa Dev, Emily Sheng, Jieyu Zhao, Aubrie Amstutz, Jiao Sun, Yu Hou, Mattie
Sanseverino, Jiin Kim, Akihiro Nishi, Nanyun Peng, et al. 2021. On measures of
biases and harms in NLP. arXiv preprint arXiv:2108.03362 (2021).
[5] Zhengqing Fang, Zhouhang Yuan, Ziyu Li, Jingyuan Chen, Kun Kuang, Yu-
feng Yao, and Fei Wu. 2024. Cross-modality Image Interpretation via Concept
Decomposition Vector of Visual-language Models. IEEE Transactions on Circuits
and Systems for Video Technology (2024).
[6] Maxwell Forbes, Jena D Hwang, Vered Shwartz, Maarten Sap, and Yejin Choi.
2020. Social chemistry 101: Learning to reason about social and moral norms.
arXiv preprint arXiv:2011.00620 (2020).
[7] Team GLM, Aohan Zeng, Bin Xu, Bowen Wang, Chenhui Zhang, Da Yin, Dan
Zhang, Diego Rojas, Guanyu Feng, Hanlin Zhao, et al. 2024. Chatglm: A fam-
ily of large language models from glm-130b to glm-4 all tools. arXiv preprint
arXiv:2406.12793 (2024).
[8] Google. 2024. Gemini Pro 1.5 - Google DeepMind Official Website.
https:
//blog.google/products/ai/gemini-1-5-pro/ Accessed: 2024-08-26.
[9] Phillip Howard, Avinash Madasu, Tiep Le, Gustavo Lujan Moreno, Anahita Bhi-
wandiwalla, and Vasudev Lal. 2024. SocialCounterfactuals: Probing and Mitigat-
ing Intersectional Social Biases in Vision-Language Models with Counterfactual
Examples. In Proceedings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition (CVPR). 11975–11985.
[10] Zhe Hu, Yixiao Ren, Jing Li, and Yu Yin. 2024. VIVA: A Benchmark for Vision-
Grounded Decision-Making with Human Values. arXiv preprint arXiv:2407.03000
(2024).
[11] Yue Huang, Lichao Sun, Haoran Wang, Siyuan Wu, Qihui Zhang, Yuan Li, Chu-
jie Gao, et al. 2024. Position: TrustLLM: Trustworthiness in Large Language
Models. In Proceedings of the 41st International Conference on Machine Learning
(Proceedings of Machine Learning Research, Vol. 235), Ruslan Salakhutdinov, Zico
Kolter, Katherine Heller, Adrian Weller, Nuria Oliver, Jonathan Scarlett, and Felix
Berkenkamp (Eds.). PMLR, 20166–20270. https://proceedings.mlr.press/v235/
huang24x.html
[12] Yue Huang, Qihui Zhang, Lichao Sun, et al. 2023. Trustgpt: A benchmark for trust-
worthy and responsible large language models. arXiv preprint arXiv:2306.11507
(2023).
[13] Sepehr Janghorbani and Gerard De Melo. 2023. Multimodal bias: Introducing a
framework for stereotypical bias assessment beyond gender and race in vision
language models. arXiv preprint arXiv:2303.12734 (2023).
[14] Tony Lee, Haoqin Tu, Chi Heem Wong, Wenhao Zheng, Yiyang Zhou, Yifan Mai,
Josselin Somerville Roberts, Michihiro Yasunaga, Huaxiu Yao, Cihang Xie, et al.
2024. VHELM: A Holistic Evaluation of Vision Language Models. arXiv preprint
arXiv:2410.07112 (2024).
[15] Xiao Liu, Xuanyu Lei, Shengyuan Wang, Yue Huang, Zhuoer Feng, Bosi Wen, Jiale
Cheng, Pei Ke, Yifan Xu, Weng Lam Tam, et al. 2023. Alignbench: Benchmarking
chinese alignment of large language models. arXiv preprint arXiv:2311.18743
(2023).
[16] Yixin Liu, Kai Zhang, Yuan Li, Zhiling Yan, Chujie Gao, Ruoxi Chen, Zhengqing
Yuan, Yue Huang, Hanchi Sun, Jianfeng Gao, et al. 2024. Sora: A review on
background, technology, limitations, and opportunities of large vision models.
arXiv preprint arXiv:2402.17177 (2024).
[17] Meta. 2024. Llama 3.2: Revolutionizing edge AI and vision with open, customiz-
able models.
https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-
mobile-devices/
[18] Yao Mu, Qinglong Zhang, Mengkang Hu, Wenhai Wang, Mingyu Ding, Jun Jin,
Bin Wang, Jifeng Dai, Yu Qiao, and Ping Luo. 2024. Embodiedgpt: Vision-language
pre-training via embodied chain of thought. Advances in Neural Information
Processing Systems 36 (2024).
[19] Moin Nadeem, Anna Bethke, and Siva Reddy. 2021. StereoSet: Measuring stereo-
typical bias in pretrained language models. In Proceedings of the 59th Annual
Meeting of the Association for Computational Linguistics and the 11th Interna-
tional Joint Conference on Natural Language Processing (Volume 1: Long Papers),
Chengqing Zong, Fei Xia, Wenjie Li, and Roberto Navigli (Eds.). Association for
Computational Linguistics, Online, 5356–5371. doi:10.18653/v1/2021.acl-long.416
[20] Nikita Nangia, Clara Vania, Rasika Bhalerao, and Samuel R. Bowman. 2020.
CrowS-Pairs: A Challenge Dataset for Measuring Social Biases in Masked Lan-
guage Models. In Proceedings of the 2020 Conference on Empirical Methods in
Natural Language Processing (EMNLP), Bonnie Webber, Trevor Cohn, Yulan He,
4726

--- Page 7 ---

CIKM ’25, November 10–14, 2025, Seoul, Republic of Korea.
Chujie Gao et al.
and Yang Liu (Eds.). Association for Computational Linguistics, Online, 1953–
1967. doi:10.18653/v1/2020.emnlp-main.154
[21] OpenAI. 2024. GPT-4O Mini: Advancing Cost-Efficient Intelligence. https://
openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/. Accessed:
2024-09-04.
[22] OpenAI. 2024. GPT-4o System Card. https://openai.com/index/gpt-4o-system-
card/ Accessed: 2024-09-02.
[23] Alexis Roger. 2024. Training large multimodal language models with ethical
values. (2024).
[24] Alexis Roger, Esma Aïmeur, and Irina Rish. 2023. Towards ethical multimodal
systems. arXiv preprint arXiv:2304.13765 (2023).
[25] Sepehr Sameni, Kushal Kafle, Hao Tan, and Simon Jenni. 2024. Building Vision-
Language Models on Solid Foundations with Masked Distillation. In Proceedings
of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 14216–
14226.
[26] Ashutosh Sathe, Prachi Jain, and Sunayana Sitaram. 2024. A unified framework
and dataset for assessing gender bias in vision-language models. arXiv preprint
arXiv:2402.13636 (2024).
[27] Ashish Seth, Mayur Hemani, and Chirag Agarwal. 2023. DeAR: Debiasing Vision-
Language Models With Additive Residuals. In Proceedings of the IEEE/CVF Con-
ference on Computer Vision and Pattern Recognition (CVPR). 6820–6829.
[28] Zhelun Shi, Zhipin Wang, Hongxing Fan, Zaibin Zhang, Lijun Li, Yongting
Zhang, Zhenfei Yin, Lu Sheng, Yu Qiao, and Jing Shao. 2024. Assessment of
multimodal large language models in alignment with human values. arXiv
preprint arXiv:2403.17830 (2024).
[29] Eric Slyman, Stefan Lee, Scott Cohen, and Kushal Kafle. 2024. FairDeDup: De-
tecting and Mitigating Vision-Language Fairness Disparities in Semantic Dataset
Deduplication. In Proceedings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition (CVPR). 13905–13916.
[30] Haoqin Tu, Bingchen Zhao, Chen Wei, and Cihang Xie. 2023. Sight Beyond Text:
Multi-Modal Training Enhances LLMs in Truthfulness and Ethics. In NeurIPS
2023 Workshop on Instruction Tuning and Instruction Following.
[31] Peng Wang, Shuai Bai, Sinan Tan, Shijie Wang, Zhihao Fan, Jinze Bai, Keqin
Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, Yang Fan, Kai Dang, Mengfei Du,
Xuancheng Ren, Rui Men, Dayiheng Liu, Chang Zhou, Jingren Zhou, and Junyang
Lin. 2024. Qwen2-VL: Enhancing Vision-Language Model’s Perception of the
World at Any Resolution. arXiv preprint arXiv:2409.12191 (2024).
[32] Zecheng Wang, Xinye Li, Zhanyue Qin, Chunshan Li, Zhiying Tu, Dianhui Chu,
and Dianbo Sui. 2024. Can We Debiase Multimodal Large Language Models via
Model Editing?. In ACM Multimedia 2024. https://openreview.net/forum?id=
ybqqGTWuhj
[33] Yisong Xiao, Aishan Liu, QianJia Cheng, Zhenfei Yin, Siyuan Liang, Jiapeng Li,
Jing Shao, Xianglong Liu, and Dacheng Tao. 2024. GenderBias-\emph {VL}:
Benchmarking Gender Bias in Vision Language Models via Counterfactual Prob-
ing. arXiv preprint arXiv:2407.00600 (2024).
[34] Yichi Zhang, Yao Huang, Yitong Sun, Chang Liu, Zhe Zhao, Zhengwei Fang, Yifan
Wang, Huanran Chen, Xiao Yang, Xingxing Wei, Hang Su, Yinpeng Dong, and
Jun Zhu. 2024. Benchmarking Trustworthiness of Multimodal Large Language
Models: A Comprehensive Study. ArXiv abs/2406.07057 (2024).
https://api.
semanticscholar.org/CorpusID:270379776
[35] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu,
Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al. 2023. Judging
llm-as-a-judge with mt-bench and chatbot arena. Advances in Neural Information
Processing Systems 36 (2023), 46595–46623.
[36] Kankan Zhou, Yibin LAI, and Jing Jiang. 2022. Vlstereoset: A study of stereotypi-
cal bias in pre-trained vision-language models. Association for Computational
Linguistics.
4727

```
