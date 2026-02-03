---
title: "THRONE - PDF Extract"
source_pdf: "2024-Li-THRONE.pdf"
pages: 17
extracted_at: "2026-01-24T17:05:38.211555"
---

# PDF Extract: THRONE

**Source PDF:** 2024-Li-THRONE.pdf
**Total Pages:** 17

---

## Content

```
--- Page 1 ---

THRONE: An Object-based Hallucination Benchmark for
the Free-form Generations of Large Vision-Language Models
Prannay Kaul1* Zhizhong Li2† Hao Yang 2 Yonatan Dukler 2
Ashwin Swaminathan 2 C. J. Taylor 2 Stefano Soatto 2
VGG, University of Oxford1 AWS AI Labs2
prannay@robots.ox.ac.uk
{lzhizhon,haoyng,dukler,swashwin,taylorcj,soattos}@amazon.com
Abstract
Mitigating hallucinations in large vision-language mod-
els (LVLMs) remains an open problem. Recent benchmarks
do not address hallucinations in open-ended free-form re-
sponses, which we term “Type I hallucinations”. Instead,
they focus on hallucinations responding to very specific
question formats—typically a multiple-choice response re-
garding a particular object or attribute—which we term
“Type II hallucinations”. Additionally, such benchmarks
often require external API calls to models which are sub-
ject to change. In practice, we observe that a reduction in
Type II hallucinations does not lead to a reduction in Type
I hallucinations but rather that the two forms of halluci-
nations are often anti-correlated. To address this, we pro-
pose THRONE, a novel object-based automatic framework
for quantitatively evaluating Type I hallucinations in LVLM
free-form outputs. We use public language models (LMs) to
identify hallucinations in LVLM responses and compute in-
formative metrics. By evaluating a large selection of recent
LVLMs using public datasets, we show that an improvement
in existing metrics do not lead to a reduction in Type I hal-
lucinations, and that established benchmarks for measur-
ing Type I hallucinations are incomplete. Finally, we pro-
vide a simple and effective data augmentation method to
reduce Type I and Type II hallucinations as a strong base-
line. Code is now available at https://github.com/amazon-
science/THRONE.
1
Introduction
This paper proposes a benchmark to evaluate hallucinations
by large vision-language models (LVLMs) when generat-
ing free-form responses, specifically detailed descriptions,
based on a given image.
The rapid advancement in large language models
(LLMs) [52] has pushed the development of large vision-
language models (LVLMs). [1, 6, 7, 17, 24, 25, 30, 36, 44,
*Work conducted during an internship at Amazon
†Corresponding author
48, 54] LVLMs take input text and images and generate
text responses to enable multi-modal perception and com-
prehension.
LVLMs are largely built on LLMs and therefore inherit
both their advantages and their disadvantages. LLMs have
been shown to produce hallucinations [47, 51], generated
text responses that are coherent and plausible but factually
incorrect. LVLMs echo this behavior with generated text
contradicting with the visual or text input [53]. Halluci-
nations prevent the use of LVLMs in safety-critical situa-
tions and therefore evaluating and mitigating hallucinations
in LVLMs is crucial for their deployment in such settings.
Determining the presence and cause of hallucinations in
LVLMs remains an open question [45, 53].
We divide LVLM hallucinations into two types. Type
I hallucinations occur in response to open-ended questions
with a very large set of possible responses —e.g. What is
happening in this image?. Type II hallucinations are in-
correct responses to a factual question regarding a spe-
cific concept about the image with a fixed set of options
such as yes/no—e.g. Is there a traffic light in this
image? Fig. 3 illustrates the difference between these two
types of hallucination.
Reducing hallucinations in both
cases is required for useful, multi-purpose LVLMs. How-
ever, later in Fig. 4 we observe that the same LVLM can
give contradicting answers when being evaluated for Type I
vs. Type II hallucinations. This implies that measuring and
reducing one type does not necessarily reduce the other.
Existing works to evaluate LVLMs often avoid direct
quantification of hallucinations and instead develop com-
prehensive benchmarks that judge various other desirable
abilities such as: optical character recognition, fine-grained
recognition and attribute detection [14, 22, 32]. The ex-
tent of hallucinations in these benchmarks is obfuscated,
since it is only one of many factors influencing other met-
rics. It requires human effort to inspect individual predic-
tions. There are two major established works which specif-
ically develop a benchmark for evaluating hallucinations
in vision-language models: POPE [26] and CHAIR [40],
which we discuss in detail in Sec. 2. However, we observe
arXiv:2405.05256v2  [cs.CV]  3 Apr 2025

--- Page 2 ---

1.
Is there a person?
2.
Is there a car?
3.
Is there a bus?
4.
Is there a truck?
5.
...
Describe 
this image 
in detail.
Large 
Vision 
Language 
Model
External 
Language 
Model
The image features a green 
double-decker bus parked 
next to a red double-decker 
bus. The green bus is 
positioned in front of the 
red bus, and both buses are 
parked on the side of a 
road. The green bus is quite 
large, occupying a 
significant portion of the 
scene.
There are several people in 
the image, with one person 
standing near the green bus 
and two others closer to the 
red bus. Additionally, there 
is a car parked further back 
in the scene, on the right 
side of the road.
1.
Yes
2.
Yes
3.
Yes
4.
No
5.
...
Figure 1. THRONE (Ours): LVLMs are prompted with a concept
neutral instruction. An external LM performs abstractive QA on the
response to establish the existence of Type I hallucinations.
(negative)
Is there a cat 
in this image?
Large 
Vision 
Language 
Model
Yes, there is 
a dog sitting 
next to the 
person in 
this image.
Response 
Parsing
No
(positive)
Is there a dog 
in this image?
No, there is 
not a cat in 
this image
Yes
Figure 2.
POPE: Questions with specific concepts prompt an
LVLM directly to evaluate Type II hallucinations [26].
Hand-
crafted rules parse LVLM responses to give yes/no labels.
they both have shortcomings in effectively evaluating hallu-
cinations:
POPE [26] is a recent work addressing Type II halluci-
nations with respect to object classes. However, we find
Type I and Type II hallucinations are disconnected, and
that POPE gives an incomplete picture on LVLM hallucina-
tions. Moreover, POPE systematically under-samples neg-
ative object categories leading to a large underestimation of
Type II hallucinations (see Sec. 5.4).
CHAIR [40] does address Type I hallucinations—
establishing object category hallucination in short image
captions using simple text matching. However, CHAIR is
not suited to current LVLMs because the simple text match-
ing it employs cannot comprehend abstract or hypothetical
concepts present in today’s LVLMs (see Fig. 4). Further,
hand-crafted rules for each set of classes are required for
usable text matching, and trivial model answers can attain a
perfect CHAIR score.
To address the issues of current LVLM hallucina-
tion benchmarks, we propose THRONE (Text-from-image
Hallucination Recognition with Object-probes for open-
eNded Evaluation). THRONE leverages language models
(LMs) to evaluate Type I hallucinations in free-form, open-
ended image descriptions with respect to a pre-defined ob-
ject vocabulary of interest. By utilizing LMs, THRONE is
able to accurately judge whether an object mentioned in an
LVLM response is implied to exist in the image or is ab-
stractly mentioned with no implication about its existence
(see Fig. 4).
Moreover, in THRONE, we provide easy access to our
benchmark, by leveraging open-source LMs that can run on
common GPUs, instead of relying on closed-source com-
mercial models [35] that are subject to arbitrary change, as
done in other works [4, 22, 32]. Through combining multi-
ple open-source LMs, we mitigate any single-model biases
in judging hallucinations when calculating Type-I halluci-
nation scores with THRONE.
We make four contributions: first, we establish an ac-
curate and accessible benchmark to quantitatively evalu-
ate object hallucinations in free-form responses, leverag-
ing LMs to judge the existence of Type I hallucinations—
quantitatively showing half the judgement errors of CHAIR;
second, we evaluate a number of current LVLMs on
THRONE and demonstrate that observed progress in re-
ducing Type II hallucinations do not translate to a corre-
sponding reduction in Type I hallucinations; third, we show
a recent method, POPE, is inaccurately capturing the ex-
tent of Type II hallucination discovery due to its sampling
strategy; we mitigate this issue in our implementation of
THRONE while presenting results for a complete version
of POPE; and fourth, we provide a simple augmentation of
visual instruction tuning data which significantly improves
performance on Type I hallucinations while maintaining or
improving Type II hallucination performance.
2
Related Work
Hallucination Benchmarks for LVLMs.
In response
to the development of LVLMs, few evaluation bench-
marks focusing on hallucinations have been introduced.
CHAIR [40], one of the first works to assess hallucinations,
is designed for short image captions. CHAIR uses a fixed
set of object classes (extended with their synonyms) as a
set of text strings to find predicted object classes in im-
age captions via exact text matching. Subsequently, each
class matched in the caption is compared to the COCO [27]
captions and bounding box annotations to establish ob-
ject hallucinations. CHAIR was developed prior to current
instruction-tuned LVLMs which produce long free-form re-
sponses (10× longer than image captions) with a diverse
vocabulary, limiting its applicability to modern LVLMs. As
shown in Fig. 3, exact text matching in CHAIR is prone to
incorrectly matching the vocabiliary classes with abstract
concepts in the free-form response and the and synonyms
of the class list must be manually selected to prevent confu-
sion during evaluation. For example, in CHAIR the word
“chair” will match all responses for the phrase “toilet
seat”, because the exact text matching classifies “seat” as
the COCO class “chair”. Finally, CHAIR metrics com-
pare the overall number of predicted objects to the overall
number of predicted objects judged to be hallucinations—

--- Page 3 ---

ignoring the recall of ground-truth objects and the distri-
bution of object classes. This means that a single correct
prediction across the entire evaluation dataset along with a
generic response otherwise e.g. A natural scene, achieves
a perfect score ( 0 hallucinated objects
1 predicted objects
= 0.0). See the Supple-
mentary Material for a full overview of CHAIR. In con-
trast, THRONE uses pre-trained LMs that go beyond direct
synonym matching, to automatically judge the existence of
concepts and hallucinations in free-form responses. In ad-
dition, our method considers both recall and precision to
yield a holistic benchmark and does not require any man-
ual curation of synonyms.
THRONE and CHAIR both
evaluate Type I hallucinations—hallucinations in response
to concept-neutral prompts e.g. Describe this image in
detail.
POPE [26] is a recently proposed benchmark to evaluate
object hallucinations in LVLMs—specifically Type II hal-
lucinations, in which an LVLM is directly queried with a
yes-no question regarding the existence of a particular ob-
ject of the form: Is there {a/an} {object class name}
in the image?. The LVLM response is parsed using sim-
ple rules to determine whether a Type II hallucination has
occurred. Precision and recall metrics are compiled using
the parsed LVLM responses and the ground-truth annota-
tion data. Despite focusing on measuring hallucinations,
POPE only queries an LVLM with 3 positive and 3 sam-
pled negative questions per COCO image i.e. the evaluation
is artificially balanced. This means many potential halluci-
nations with respect to the COCO categories are not cap-
tured by their method. In Sec. 5.4, we show POPE dra-
matically underestimates Type II hallucinations and present
the results of a complete version. Our method, THRONE,
evaluates the prevalence of Type I hallucinations, which we
observe are disjoint to Type II hallucinations.
Comprehensive Benchmarks for LVLMs have recently
grown in number. MMBench [32] and MM-Vet [49] as-
sess various aspects of LVLM performance such as: color
perception, celebrity recognition, and numerical calcula-
tion. However many of these works integrate evolving APIs
which are modified often (or even discontinued) and are in-
herently stochastic. Over time this greatly reduces the con-
sistency of these benchmarks. Exceptions are MME [14]
and SEED-Bench [22], but the impact of Type II hallucina-
tions on final metrics is conflated with a number of other
aspects of model performance. Our method, THRONE, di-
rectly addresses Type I hallucinations, only making use of
open-source language models and datasets.
Large Vision Language Models (LVLMs) have rapidly
developed by harnessing advancements in large language
models (LLM) [5, 39, 43] and by directly integrating pre-
trained LLMs into their architectures. In contrast to earlier
vision-language models such as CLIP [18, 38], LVLMs are
generally comprised of a pretrained LLM and image en-
Prompt
Response
Image
What is 
happening in 
this image?
In the image, a 
man is hanging 
clothes on a 
clothesline that 
is attached to 
the back of a 
moving car.
Is there a 
traffic light in 
this image?
Yes, there is a 
traffic light in 
the image, and 
the man is 
standing on the 
back of a car 
near it.
Figure 3. Type I vs. Type II Hallucinations: (Top) LVLMs
prompted with concept-neutral instructions produce Type I hal-
lucinations. (Bottom) Instructions specifying a concept produce
Type II hallucinations. Examples from LLaVA-v1.5 [29].
coder, aligned with a connector module of varying com-
plexity. Some works are highlighted here. Frozen [44] is
an early work fine-tuning the vision encoder to dynamically
prefix the prompt to a frozen LLM. Flamingo [1] combines
visual and language features using cross-attention layers in
an otherwise frozen LLM. BLIP-2 [25] uses a frozen im-
age encoder to learn a Querying-Transformer (Q-Former)
on image-text pairs that is used as the connector. This ar-
chitecture is adapted in [7] for dialogue via training with
visual instruction tuning.
LLaVA [30] uses COCO [27]
annotations and GPT-4 [35] to generate visual instruction
tuning data in a plain-text pipeline. Combining this gener-
ated data with standard VQA datasets (VQAv2 etc.) further
boosts performance [29]. Different works modify the train-
ing approach by using efficient adaptation [16, 48] multiple
training stages [3] or introduce the use of discrete tokens
for localization [36]. We note however, that most of these
works evaluate performance on traditional vision-language
datasets like VQAv2 [2], which do not consider the extent
of hallucinations, a known problem with LLMs [47, 51].
3
THRONE
Recap of existing methods. POPE [26] and other bench-
marks (MME [14], MMBench [32]) directly query LVLMs
with a restricted desired answer space, e.g. yes-no (MME,
POPE) and A-B-C-D multiple choice (MMBench), as
shown in Fig. 2.
These benchmarks only consider such
short answer formats, whereas a key quality of LVLMs is
in their ability to generate free-form coherent text. More-
over, POPE, which addresses Type II hallucinations, under-
samples negative classes meaning hallucinations are dra-
matically underestimated (see Sec. 5.4 and Fig. 7). In con-
trast, we skip class subsampling and enumerate all classes
for every image, ensuring a full evaluation of Type I hallu-
cinations of the ground-truth classes.
CHAIR [40] also evaluates Type I hallucinations, but
was developed when typical vision-language models could
only generate short and simple captions similar to those in

--- Page 4 ---

Is there...
a person [No]
a banana [Yes]
an apple [No]
an orange [No]
...in the image?
No, there is no person in the image. [No]
Yes, there is a banana in the image. [Yes]
No, there is not an apple in the image. [No]
No, there is no orange in the image. [No]
No Type II Hallucinations Found
Type II Hallucination Evaluation (POPE)
Instruction [GT]
Response [Prediction]
Instruction
Type I Hallucination Evaluation
Response
Describe this image in 
detail.
The image showcases a fruit stand at a grocery 
store, featuring a variety of fruits on 
display. There are several bunches of bananas, 
with some placed in the foreground and others 
in the background. The bananas are arranged in 
different sections, creating an appealing 
presentation for customers. In addition to the 
bananas, there are also apples and oranges on 
display. The apples are located towards the 
left side of the image, while the oranges are 
placed in the middle and right side of the 
stand. The fruits are well-organized and 
presented in an attractive manner, making it 
an inviting sight for shoppers.
Type I Hallucinations Present and Found
MSCOCO Object Prediction from Description
Human
CHAIR
THRONE (Ours)
banana
apple orange
banana person
apple orange
banana
apple orange
◼ - GT Class
◼ - Type II 
Hallucination
◼ - Hypothetical 
Content (not a 
Hallucination)
Figure 4. A Comparison of POPE, CHAIR and THRONE: Directly querying LVLMs for object existence (person, banana etc.) using
concept-specific instructions, as in POPE (bottom left), does not produce the same hallucinations as using concept-neutral instructions
(right). We highlight the Type I hallucinations in orange. CHAIR relies on exact text matching to a fixed set of objects and synonyms,
thus incorrectly labels “customers” and “shoppers” as hallucinations, highlighted in red. THRONE is designed for the rich vocabulary
and the free-form generations of modern LVLMs by harnessing LMs to establish object existence. By using an LM to pass judgement, our
evaluation correctly captures “customers” and “shoppers” as hypothetical content in the free-form generation.
COCO Captions [12]. Moreover, it lacks accurate compre-
hension of responses (see the right side of Fig. 4) and ig-
nores the recall of ground-truth objects. In Sec. 5.5, we de-
scribe quantitative evaluations, using a human oracle, which
demonstrate THRONE halves the rate of hallucination mis-
judgement in CHAIR. See Sec. 2 and the Supplementary
Material for more details on CHAIR and its shortcomings.
Fig. 4 shows an overview of the three aforementioned meth-
ods: POPE, CHAIR and our method, THRONE.
3.1
Evaluating Hallucinations with THRONE
To address these limitations, we propose a framework,
THRONE, shown in Fig. 1, to evaluate the prevalence of
Type I hallucinations in LVLM responses conditioned on
an image and a neutral text prompt.
For each image in a labeled dataset, I, addressing a set of
classes, C, the LVLM is queried with the same instruction:
Describe this image in detail., regardless of image
content. The LVLM response, which is expected to be long
free-form text containing an image description, is generated
and stored. Next, a publicly available, open-source, exter-
nal language model (LM) performs abstractive question an-
swering (AQA) using the LVLM response as context and
a question of the form: Please answer yes or no.
Is
there {a/an} {object class name} in this image? or
similar, for every class in C (right side of Fig. 1). By se-
lecting an appropriate LM and using a simple prompt tem-
plate (see Sec. 4 for specific details), we ensure the AQA
response is either yes or no—our method does not require
any additional parsing. This is in contrast to other works
which require added parsing or interpretation by a closed-
source model.
After performing AQA on each response generated by
the LVLM for every class in C, we obtain an array of pre-
dicted labels:
 \ l abe l {eq:framework_pred} \mathbf {\hat {Y}} \in {\{0,1\}}^{|\mathcal {I}|\times |\mathcal {C}|} \vspace {-0.2cm}
(1)
where 0/1 indicates a negative/positive existence judgement
by the LM with respect to the relevant LVLM response.
Similarly using the ground-truth data for I, an array of
ground-truth labels can be constructed:
  \ma thbf {Y} \in {\{0,1\}}^{|\mathcal {I}|\times |\mathcal {C}|} \vspace {-0.2cm}
(2)
Using these two arrays, we calculate four metrics: (1)
Overall Precision, PALL; (2) Overall Recall, RALL; (3)
Class-wise Precision, PCLS; and (4) Class-wise Recall,
RCLS. Overall metrics are calculated in a class-agnostic
manner.
Class-wise metrics are calculated in a class-
conscious manner by computing precision and recall for
each category separately and then averaging. This follows
common practice in object detection and instance segmen-
tation [10, 27].
False positives in LVLMs reduce precision and are dom-
inated by hallucinations—precision indicates the extent of
Type I hallucinations in LVLM responses. The recall met-
rics inform the level of class coverage by an LVLM when
producing image descriptions. The class-wise metrics give
a general measure of performance as the overall metrics
are skewed towards the most common categories. A com-
mon way to combine precision, P, and recall, R, metrics is
through the generalized F score, Fβ:
  F ^\ b eta  
=  (
1 +  \b e ta ^2)\cdot \frac {P\cdot R}{(\beta ^2 \cdot P) + R} 
(3)

--- Page 5 ---

Prior work such as POPE [26], use the common balanced
F-score (or F 1-score) which equally weights precision and
recall. However, given that THRONE is concerned with
measuring hallucinations and is therefore particularly inter-
ested in precision, we choose β = 0.5 or the F 0.5-score,
thus weighing precision twice as important as recall. The
F 0.5-score is commonly used in pandemic misinformation
filters [37], recommender systems [34], active stock selec-
tion [41] and other areas where false positives are costlier
than false negatives. From this we can calculate the overall
and class-wise F 0.5-scores, F 0.5
ALL and F 0.5
CLS, respectively.
To mitigate against class imbalance issues, we use F 0.5
CLS
as the principle metric of comparison between LVLMs in
THRONE.
3.2
Ensuring Robustness via Ensembling
Any LM used for AQA in THRONE may misjudge Type
II hallucinations—no LM is perfect.
Fig. 5 (top) shows
two different variants from the same model family (FLAN-
T5 [33]), yielding opposite responses when prompted with
the same response and question. Moreover, an LM may
yield different answers to semantically identical questions,
despite conditioning on the same response—shown in Fig. 5
(bottom). To ensure THRONE is robust to spurious perfor-
mance by any one LM, we ensemble various LMs and se-
mantically equivalent question formats. The use of N dis-
tinct LMs and M distinct question formats yields NM an-
swers for each (LVLM response, class) combination. This
set of NM answers is combined based on equal voting by
each (LM, question) pair to “elect” the predicted answer.
Continuing the notation from Eq. (1), stacking predictions
from each (LM, question) pair yields a 3D array of pre-
dicted labels: ¯Y ∈{0, 1}|IOURS|×|COURS|×NM. To combine
the answers from each (LM, question) pair via voting, we
require agreement between at least k answers. Where suf-
ficient agreement does not exist we introduce an “ignore”
label. Mathematically, the elements in ˆY (from Eq. (1)) are
calculated as:
  \ha t
 
{
Y
}
_
{i
,j}
 = \begin { cas e s}
 0
, &
 \s um _{k= 1 }
^{N
M} \bar {Y}_{i,j,k} \leq (NM - k) \\ 1, & \sum _{k=1}^{NM} \bar {Y}_{i,j,k} \geq k \\ -1, & \text {otherwise} \end {cases} \vspace {-0.1cm} 
where an “ignore” label exists in ¯Y, it is removed from the
calculations of PALL, RALL, PCLS, and RCLS, as we cannot
be confident in the AQA process for that particular (LVLM
response, class) combination. The choice of k reflects the
desired level of confidence. We make use of a unanimous
voting mechanism (k = NM)—use the prediction only if
all (LM, question) pairs agree, otherwise ignore. Human
evaluation of our benchmark and choice of voting mech-
anism is found in the Supplementary Material. Once we
have applied this voting mechanism, we can calculate the
metrics described at the end of Sec. 3.1.
The image features a 
dining table with a 
delicious slice of 
chocolate cake on a 
white plate. The cake is 
accompanied by a glass 
of beer, which is placed 
on the table as well. 
There are two bowls on 
the table, one near the 
cake and the other 
further away. A fork is 
also visible on the 
table, ready to be used 
for enjoying the cake. 
The scene creates a cozy 
and inviting atmosphere 
for a delightful dessert 
and beverage experience.
FLAN-T5-Base
Please answer yes or no.
Is there a knife in this image?
no
Please answer yes or no.
Does the text give evidence for 
a knife being present?
FLAN-T5-Large
yes
FLAN-T5-Large
no
Figure 5. AQA Ensembling in Evaluation: Using different LMs
or different prompts when running AQA on LVLM generated re-
sponses can produce opposing answers to identical prompts or
identical LMs. To ensure THRONE is robust to this, we ensemble
multiple LMs and multiple prompts in our evaluation pipeline.
4
Implementation
We provide details of our framework regarding the selection
of public datasets, public LMs and LM prompts.
4.1
Dataset
Any proper evaluation of object hallucinations (a type of
false positive error) requires knowing, with certainty, which
classes are absent in an image. In our benchmark, we use
COCO [27] for a number of reasons: (1) its annotations
of 80 categories are exhaustive at an image level (image-
level recall≈99% [27])—if there are many book instances
in a COCO image, at least one is annotated with bounding
boxes; (2) many LVLMs are partly trained on COCO data
and so should be familiar with the set of categories; (3) its
images generally contain complex scenes suitable for gener-
ating long free-form descriptions unlike image recognition
datasets like ImageNet [8].
We utilize the validation set of COCO 2017, which con-
tains |I| = 5000 images and |C| = 80 categories. Us-
ing the single LVLM text prompt Describe this image
in detail., we generate 5000 responses.
As we query
each LVLM response for each category in C, a single
LM performs AQA |I| × |C| = 400k times across the
LVLM responses—one instance of AQA per (image re-
sponse, class) pair. In Sec. 5.3, we also present results using
Objects365 [42] which is rarely used in LVLM training.
4.2
Language Models
To assess Type I hallucinations in an LVLM response us-
ing THRONE, we require a language model (LM) which
can answer questions on the existence of object categories
based on the LVLM response. MMBench [32] makes use
of a ChatGPT model to identify multiple choice answer se-
lections and still reports mistakes. In our experience, some
LMs give rather incoherent judgements when used to as-
sess hallucinations when the prompt is changed (see sup-
plemental material). Therefore for THRONE, we choose
FLAN-T5 models [33, 39]. We make this choice because
FLAN-T5 model family: (1) have undergone instruction
tuning with thousands of tasks [33]; (2) are open-source and

--- Page 6 ---

Model
L
PALL
RALL
F 1
ALL
F 0.5
ALL
PCLS
RCLS
F 1
CLS
F 0.5
CLS
Adapter-v2 [15]
514
63.6
73.3
68.1
65.3
68.2
70.6
69.4
68.7
Adapter-v2.1 [15]
512
63.8
73.7
68.4
65.5
67.4
71.2
69.3
68.1
InstructBLIP [7]
525
70.8
74.3
72.5
71.5
77.2
71.9
74.5
76.1
Otter-Image [23]
257
33.0
31.2
32.1
32.7
25.2
16.9
20.2
22.9
MiniGPT4 [54]
473
81.7
59.8
69.0
76.1
79.9
61.8
69.7
75.5
MiniGPT-v2 [6]
381
79.0
66.6
72.3
76.2
77.6
67.0
71.9
75.2
mPLUG-Owl [48]
555
55.5
71.9
62.6
58.1
66.3
68.3
67.3
66.7
LRV-Instruction-v2 [28]
103
82.0
56.7
67.0
75.3
78.4
58.8
67.2
73.5
LLaVA-v1.3* [30]
532
80.5
65.2
72.1
76.9
79.9
65.3
71.9
76.5
LLaVA-v1.5 [29]
509
68.1
61.0
64.4
66.6
69.9
56.4
62.5
66.8
LLaVA-Mistral [19, 31]
524
86.8
71.8
78.3
83.6
84.4
64.2
70.8
77.5
Table 1.
THRONE Results with COCO for a selection of
instruction-tuned LVLMs. We select F 0.5
CLS as the principal met-
ric for evaluation in our benchmark to balance across classes and
to prioritize precision (which reflects the extent of hallucination)
over recall. Best and second-best performance are denoted by blue
and red, respectively. *Our implementation using official code to
enable fair comparison. L corresponds to the median response
length (measured in # of characters).
therefore accessible to the community; (3) can fit locally on
a single GPU for the models we consider; (4) follow user’s
instruction to only respond yes or no; and (5) are optimized
for use in the free and public Text-Generation-Inference
API [11] for acceleration. As described in Sec. 3.2, we uti-
lize N LMs to ensure our method is robust. Specifically, we
use N = 3 variants of FLAN-T5, namely: FLAN-T5-Base
(250M parameters), FLAN-T5-Large (780M parameters),
and FLAN-T5-XL (3B parameters).
4.3
Prompt Ensembling
To guarantee each of these FLAN-T5 variants faithfully
produce responses of either yes or no only during AQA,
we use the following input template to each LM, reflecting
the format used when training FLAN-T51:
Text:
{LVLM Response} Read the text
about an image and answer the question.
Question:
Please answer yes or no.
{Question}
We use M = 3 semantically identical questions:
• Is there a/an {class name} in this image?
• Does the text imply a/an {class name} is in the
image?
• Does the text explicitly mention a/an
{class name} is in the image?
As outlined in Sec. 3.2, we use a unanimous voting
mechanism to combine the answers from each (LM, ques-
tion) pair and so k = 3 × 3 = 9.
5
Evaluation Results
In this section, we: (1) outline our LVLM selection and
reasoning; (2) present THRONE on COCO for evaluating
Type I hallucinations; (3) extend THRONE to Objects365
(containing a larger vocabulary); (4) analyze and extend
POPE to enable improved evaluation of Type II halluci-
nations; and (5) highlight results from our ablation studies
found in the Supplemental Material.
1https://tinyurl.com/5n6nexze
5.1
Models
For fair comparison between existing LVLMs, each pub-
licly available model we evaluate uses an LLM with ∼7B
parameters. The LVLMs generally have different sized im-
age encoders–e.g. LLaVA [30] uses a CLIP ViT-L/14 [9, 38]
with an input resolution of 336 × 336, while Instruct-
BLIP [7] uses a ViT-g/14 [50] trained with EVA [13] and
an input resolution of 224 × 224. Note that image encoder
size and resolution is not something we can easily control
in a pre-trained model. Each model we consider contains
instruction tuning in the final training phase—instruction
tuned models provide free-form descriptions; THRONE
focuses on models that can generate free-form descriptions.
E.g. we leave out BLIP-2 [25] (response median length
31 characters) in favor of InstructBLIP (median response
length 525).
5.2
THRONE Results on COCO
Results are shown in Tab. 1. The principal metric that we
use to judge model performance is the classwise F 0.5-score
(highlighted gray). We also report all the metrics outlined
in Sec. 3.1, (P, R, F 1, F 0.5) for overall (left) and class-
wise averaging (right), utilizing the unanimous voting pre-
sented in Sec. 3.2. See the Supplementary Material for re-
sults and an analysis of different voting mechanisms. These
results demonstrate that improvements on other bench-
marks (POPE, MME, MMBench etc.)
may be orthogo-
nal and potentially at odds with improved performance on
THRONE. Using the results of the 11 LVLMs that we eval-
uate, THRONE and POPE, which measure Type I and Type
II hallucinations, respectively, have a Spearman’s rank cor-
relation coefficient of just 0.2, and THRONE vs POPE-
C has just 0.4—the relationship between performance on
POPE and THRONE on the same dataset is far from mono-
tonic. For class-wise precision—PCLS, the best performing
models hallucinate ∼20% of the objects. We show in the
Supplementary Material that the vast majority of false pos-
itive objects in the free-form image descriptions evaluated
are direct hallucinations rather than misclassifications of vi-
sually similar objects (e.g. mistaking a squash racket for a
tennis racket). These results demonstrate that much work
still remains to adequately suppress Type I hallucinations in
LVLMs.
5.3
THRONE Results on Objects365
Many LVLMs train on COCO directly or indirectly, thus
to demonstrate generality we apply THRONE to the Ob-
jects365 dataset [42]. Like COCO, Objects365 aims to be
exhaustive in its image-level class labeling (it aims to la-
bel at least one instance for each class present), but it has a
larger object vocabulary and is not used as training data for
the LVLMs that we evaluate. To gather a manageable sub-
set of the Objects365 validation set (80k images), we use the
natural sampling algorithm from [21], resulting in 5110 im-

--- Page 7 ---

Model
PALL RALL F 1
ALL F 0.5
ALL PCLS RCLS F 1
CLS F 0.5
CLS
Adapter-v2 [15]
46.7
33.9
39.3
43.4
48.9
28.5
36.0
42.8
Adapter-v2.1 [15]
46.8
34.0
39.4
43.5
48.8
28.8
36.2
42.8
InstructBLIP [7]
54.5
37.2
44.2
49.8
53.7
33.6
41.3
48.0
Otter-Image [23]
21.4
12.7
16.0
18.8
9.5
4.4
6.0
7.7
MiniGPT4 [54]
53.0
32.9
40.6
47.2
49.9
31.9
39.0
44.9
MiniGPT-v2 [6]
54.5
36.0
43.4
49.4
51.3
34.6
41.3
46.8
mPLUG-Owl [48]
43.7
33.4
37.8
41.2
48.2
29.0
36.2
42.6
LRV-Instruction-v2 [28]
57.5
26.7
36.5
46.7
51.4
26.6
35.1
43.3
LLaVA-v1.3* [30]
57.6
32.9
41.9
50.1
52.6
30.5
38.6
45.9
LLaVA-v1.5 [29]
54.0
39.5
45.6
50.3
53.9
34.3
41.9
48.4
LLaVA-Mistral [19, 31]
58.3
39.1
46.9
53.1
57.8
35.9
44.3
51.5
Table 2. THRONE Evaluation with Objects365. Evaluation
results for a selection of instruction-tuned LVLMs, we use a subset
of Objects365 for the THRONE evaluation. Best and second-
best performance are denoted by blue and red, respectively. *Our
implementation using official code to enable fair comparison.
0.66
0.68
0.70
0.72
0.74
0.76
0.78
0.80
Classwise F0.5-Score (COCO Classes)
0.40
0.42
0.44
0.46
0.48
0.50
0.52
0.54
Classwise F0.5-Score (Objects-365 Classes)
Spearman's rank correlation: 0.912
Figure 6. Comparing THRONE on COCO and Objects365.
We observe that despite variations in the data distribution,
THRONE metrics, which measure Type I hallucinations gener-
alize and have a strong Spearman’s rank correlation of r = 0.900.
One model (red circle) designated as an outlier and ignored when
calculating ranking correlation.
ages (the COCO validation set has 5k images). We present
the results for THRONE on Objects365 in Tab. 2. Figure 6
shows the strong correlation in THRONE performance be-
tween evaluating on COCO and Objects365. This demon-
strates that measuring Type I hallucinations in an LVLM
using THRONE with a relatively small dataset like COCO,
is indeed indicative of the intrinsic level of Type I halluci-
nation in a given LVLM.
5.4
Completing POPE for Type II Hallucinations
Our experiments have used THRONE to evaluate the
prevalence of Type I hallucinations in LVLM responses on
COCO. POPE evaluates Type II hallucinations on COCO,
but we find POPE is largely incomplete. First, POPE only
evaluates on 500 COCO validation set images.
Second,
for each image only a subset of classes (at most 12) are
evaluated—each image is only queried with 15% of possi-
ble questions. Finally, POPE artificially balances evalua-
tion questions between positives and negatives, despite ob-
ject class existence in images being inherently imbalanced.
Figure 7. Instability of POPE to complete evaluation of Type
II Hallucinations. Extending POPE to an exhaustive analysis on
all COCO images and classes (POPE-C) leads to a dramatic re-
duction in performance across all 11 models. POPE is sensitive to
the sampling mechanism, and by undersampling negative classes,
POPE severely underestimates Type II hallucinations in LVLMs.
The above reasons make the evaluation of Type II halluci-
nations using POPE insufficient (see Sec. 2 for more details
on POPE). To correct this, we complete POPE by using all
images to exhaustively query each LVLM for every class
in the COCO vocabulary, as done in THRONE. We name
this POPE-Complete (POPE-C). Fig. 7 shows the extreme
difference in evaluation between POPE and our exhaustive
version, POPE-C—reporting F 1-score (POPE does not uti-
lize F 0.5-score). As POPE only evaluates at most 9 nega-
tive classes, only a small subset of potential hallucinations
of COCO classes are evaluated, thereby heavily underesti-
mating the extent of Type II hallucination. For each LVLM
analyzed, we observe a large—in many cases an extreme—
reduction in precision and therefore in F1-score.
Our evaluation contains three pairs of LVLMs in which
one is the follow-up work to the other, where each follow-
up work generally trains on more data for more tasks with
a more advanced language model.
Comparing the right
hand side of Fig. 7 to Tab. 1, we observe that these follow-
up works generally show an improvement in POPE (and
POPE-C), but surprisingly indicate a small reduction in per-
formance on THRONE with COCO. This observation sug-
gests that progress in reducing Type II hallucinations can be
orthogonal to reducing Type I hallucinations.
5.5
Ablations
In the Supplementary Material we present three key ablation
experiments and give an executive summary of results here.
First, after subsampling COCO images and LVLM re-
sponses, we replace the LMs in THRONE with human
judgement as an oracle for Type I hallucination occur-
rence. When comparing THRONE and CHAIR with hu-
man judgements, we estimate using THRONE improves
the precision of judging Type I hallucinations to 96% versus
91% when using CHAIR—this reduces the false discovery
rate by more than 50%. Note that we find most estimated
errors in THRONE arise from the particular class defini-
tions in COCO, e.g. the COCO class tv includes computer
monitors, which the oracle judgement is aware of.
Second, we apply the same class (and image) sampling

--- Page 8 ---

strategy as in POPE to THRONE and show this sampling
overestimates F 0.5
CLS by an average of 12.3 points compared
to the complete use of classes in THRONE (Tab. 1).
Finally, we vary the choice of k i.e. the voting mecha-
nism used to combine answers from multiple (LM, ques-
tion) pairs. We use the unanimous voting mechanism (k =
9) in THRONE to minimize the false discovery rate and
find the valid alternatives of simple majority (k = 5) or
all-but-one (k = 8) voting mechanisms have strong corre-
lations and rank correlations across all compute metrics, in
THRONE, of > 0.99 and > 0.94, respectively.
6
Improved Baselines
Much needs to be done to study Type I hallucinations.
As a first step to their mitigation, we demonstrate a base-
line method to augment the visual instruction tuning data
for LLaVA models [29, 30], yielding improvements on
THRONE while maintaining similar performance regard-
ing Type II hallucinations on POPE.
6.1
Visual Instruction Tuning Data Augmentation
Similar to chain-of-thought learning [46], during instruc-
tion tuning, we augment all visual instruction tuning sam-
ples constructed by LLaVA [30] by prepending the task of
enumerating a list of objects (present and absent) and indi-
cating approximate locations, if applicable. Other than this,
the LLaVA data and training pipeline remains unchanged.
To generate the new data for this object enumeration task,
we use the same COCO bounding box annotations used to
generate the vision instruction tuning data in LLaVA. The
simple text-only format (no special tokens) we use is:
Instruction: <image> Give a list of objects and locations
in the image.
Response:
{class_name_1} [{location_1}/absent]
...
{class_name_N} [{location_N}/absent]
where location i is a plain text indicator representing
the location of the center point of the relevant object in the
image on a 3 × 3 grid (e.g.
bottom left). To provide neg-
atives in the training data, if class name i is not present, we
use the plain text indicator absent. Prior work [53] shows
that classes that frequently co-occur in the training data are
the most common hallucinations, therefore we bias our neg-
ative sampling towards class pairs that frequently co-occur
using a correlation matrix. We detail and ablate this choice
in the Supplementary Material.
6.2
Improved Baseline Results
Tab. 3 shows the result of evaluating our improved base-
line method on THRONE, POPE, and POPE-C. During in-
ference, we approximate our training data augmentation by
first prompting the LVLM to perform the object enumera-
tion tasks and then generating a response to the prompt from
the relevant benchmark. We additionally show results of uti-
lizing VisualGenome bounding box annotations [20] on the
Object
THRONE
POPE
POPE-C
Model
Enumeration Data PCLS RCLS F 0.5
CLS
P
R
F 1
P
R
F 1
✗
79.9
65.3
76.5
58.0 98.4 73.0
7.7
99.2 14.3
COCO
83.2
68.8
79.9
73.2 88.2 80.0
9.8
69.4 17.2
LLaVA-v1.3
COCO + VG
86.2
67.0
81.5
83.0 82.5 82.8 13.8 50.4 21.7
✗
69.9
56.4
66.8
81.9 90.8 86.1 58.7 85.7 69.7
COCO
87.2
76.6
84.9
88.6 85.3 87.0 58.9 87.5 70.4
LLaVA-v1.5
COCO + VG
86.1
77.0
84.1
89.8 83.7 86.7 64.5 86.1 73.7
Table 3. Improved Baseline via Object Enumeration: Adding
our object enumeration task to LLaVA training and inference leads
to large improvements on THRONE particularly in terms of class-
wise precision, PCLS, over standard LLaVA models, demonstrat-
ing a reduction in Type I hallucinations, as well as small reductions
in Type II hallucinations judged by POPE and POPE-C.
COCO images where available. On THRONE, we observe
a large increase in classwise precision and therefore F 0.5
CLS,
particularly for LLaVA-v1.5, demonstrating the ability of
our method to reduce Type I hallucinations. Moreover, on
POPE and POPE-C, using our object enumeration yields
small improvements in precision, indicating reduced Type
II hallucinations as well. In the Supplementary Material, we
ablate the sampling of negatives during object enumeration
training and the effect of removing the object enumeration
task during inference.
7
Conclusion
We establish a novel benchmark, THRONE, for evaluat-
ing hallucinations generated by LVLMs in free-form im-
age descriptions i.e. Type I hallucinations.
Our bench-
mark utilizes multiple LMs and prompt formats with a
simple voting mechanism to yield an accurate evaluation
of Type I hallucinations in LVLM responses. We ensure
that THRONE is broadly accessible by utilizing open-
source LMs capable of running on a single commercial
GPU. Using THRONE, we benchmark 11 publicly avail-
able LVLMs on two datasets, COCO and Objects365, and
demonstrate that limited progress has been made in address-
ing Type I hallucinations. Moreover, we show how the es-
tablished benchmark, POPE, underestimates Type II hal-
lucinations, which occur in response to specific questions
e.g. yes-no questions. We present results for a completed
version (POPE-C) to enable a comparison of Type I halluci-
nations through THRONE and Type II hallucinations using
POPE-C. Finally, we propose a simple data augmentation
for LVLM training that can result in a large reduction in
Type I hallucinations whilst maintaining or improving Type
II hallucination performance.
Limitations and Ethical Considerations are discussed in
the Supplementary Material.

--- Page 9 ---

References
[1] Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine
Miech, Iain Barr, Yana Hasson, Karel Lenc, Arthur Mensch,
Katherine Millican, Malcolm Reynolds, et al. Flamingo: a
visual language model for few-shot learning. Advances in
Neural Information Processing Systems, 35:23716–23736,
2022. 1, 3
[2] Stanislaw Antol, Aishwarya Agrawal, Jiasen Lu, Margaret
Mitchell, Dhruv Batra, C Lawrence Zitnick, and Devi Parikh.
Vqa: Visual question answering. In Proceedings of the Inter-
national Conference on Computer Vision, pages 2425–2433,
2015. 3
[3] Jinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan
Tan, Peng Wang, Junyang Lin, Chang Zhou, and Jingren
Zhou. Qwen-vl: A versatile vision-language model for un-
derstanding, localization, text reading, and beyond. arXiv
preprint arXiv:2308.12966, 2023. 3
[4] Yonatan Bitton, Hritik Bansal, Jack Hessel, Rulin Shao,
Wanrong Zhu, Anas Awadalla, Josh Gardner, Rohan Taori,
and Ludwig Schmidt. Visit-bench: A benchmark for vision-
language instruction following inspired by real-world use,
2023. 2
[5] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Sub-
biah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakan-
tan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Lan-
guage models are few-shot learners. Advances in Neural In-
formation Processing Systems, 33:1877–1901, 2020. 3
[6] Jun Chen, Deyao Zhu, Xiaoqian Shen, Xiang Li, Zechun
Liu,
Pengchuan
Zhang,
Raghuraman
Krishnamoorthi,
Vikas Chandra, Yunyang Xiong, and Mohamed Elhoseiny.
Minigpt-v2: large language model as a unified interface
for vision-language multi-task learning.
arXiv preprint
arXiv:2310.09478, 2023. 1, 6, 7
[7] Wenliang Dai, Junnan Li, Dongxu Li, Anthony Meng Huat
Tiong, Junqi Zhao, Weisheng Wang, Boyang Li, Pascale
Fung, and Steven Hoi.
Instructblip:
Towards general-
purpose vision-language models with instruction tuning. In
Advances in Neural Information Processing Systems, 2023.
1, 3, 6, 7
[8] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-
Fei. Imagenet: A large-scale hierarchical image database.
In Proceedings of the IEEE Conference on Computer Vision
and Pattern Recognition, 2009. 5
[9] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov,
Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner,
Mostafa Dehghani, Matthias Minderer, Georg Heigold, Syl-
vain Gelly, Jakob Uszkoreit, and Neil Houlsby. An image
is worth 16x16 words: Transformers for image recognition
at scale.
Proceedings of the International Conference on
Learning Representations, 2021. 6
[10] Mark Everingham, Luc Van Gool, Chris K. I. Williams, John
Winn, and Andrew Zisserman. The PASCAL Visual Object
Classes (VOC) challenge.
International Journal of Com-
puter Vision, 2010. 4
[11] Hugging Face.
Text generation inference.
https://
github.com/huggingface/text-generation-
inference, 2023. Accessed: November 10, 2023. 6
[12] Hao Fang, Saurabh Gupta, Forrest Iandola, Rupesh K Sri-
vastava, Li Deng, Piotr Doll´ar, Jianfeng Gao, Xiaodong He,
Margaret Mitchell, John C Platt, et al. From captions to vi-
sual concepts and back. In Proceedings of the IEEE Con-
ference on Computer Vision and Pattern Recognition, 2015.
4
[13] Yuxin Fang, Wen Wang, Binhui Xie, Quan Sun, Ledell Wu,
Xinggang Wang, Tiejun Huang, Xinlong Wang, and Yue
Cao. Eva: Exploring the limits of masked visual representa-
tion learning at scale. In Proceedings of the IEEE Conference
on Computer Vision and Pattern Recognition, 2023. 6
[14] Chaoyou Fu, Peixian Chen, Yunhang Shen, Yulei Qin,
Mengdan Zhang, Xu Lin, Zhenyu Qiu, Wei Lin, Jinrui Yang,
Xiawu Zheng, Ke Li, Xing Sun, and Rongrong Ji. Mme: A
comprehensive evaluation benchmark for multimodal large
language models. arXiv preprint arXiv:2306.13394, 2023.
1, 3
[15] Peng Gao, Jiaming Han, Renrui Zhang, Ziyi Lin, Shijie
Geng, Aojun Zhou, Wei Zhang, Pan Lu, Conghui He, Xi-
angyu Yue, Hongsheng Li, and Yu Qiao. Llama-adapter v2:
Parameter-efficient visual instruction model. arXiv preprint
arXiv:2304.15010, 2023. 6, 7
[16] Edward J Hu, yelong shen, Phillip Wallis, Zeyuan Allen-
Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen.
LoRA: Low-rank adaptation of large language models. In
Proceedings of the International Conference on Learning
Representations, 2022. 3
[17] Shaohan Huang, Li Dong, Wenhui Wang, Yaru Hao,
Saksham Singhal, Shuming Ma, Tengchao Lv, Lei Cui,
Owais Khan Mohammed, Barun Patra, Qiang Liu, Kriti Ag-
garwal, Zewen Chi, Johan Bjorck, Vishrav Chaudhary, Sub-
hojit Som, Xia Song, and Furu Wei.
Language is not all
you need: Aligning perception with language models. arXiv
preprint arXiv:2302.14045, 2023. 1
[18] Chao Jia, Yinfei Yang, Ye Xia, Yi-Ting Chen, Zarana Parekh,
Hieu Pham, Quoc Le, Yun-Hsuan Sung, Zhen Li, and Tom
Duerig. Scaling up visual and vision-language representa-
tion learning with noisy text supervision. In Proceedings of
the International Conference on Machine Learning, pages
4904–4916, 2021. 3
[19] Albert Q Jiang, Alexandre Sablayrolles, Arthur Mensch,
Chris Bamford, Devendra Singh Chaplot, Diego de las
Casas, Florian Bressand, Gianna Lengyel, Guillaume Lam-
ple, Lucile Saulnier, et al.
Mistral 7b.
arXiv preprint
arXiv:2310.06825, 2023. 6, 7
[20] Ranjay Krishna, Yuke Zhu, Oliver Groth, Justin Johnson,
Kenji Hata, Joshua Kravitz, Stephanie Chen, Yannis Kalan-
tidis, Li-Jia Li, David A Shamma, et al.
Visual genome:
Connecting language and vision using crowdsourced dense
image annotations. International Journal of Computer Vi-
sion, 123:32–73, 2017. 8
[21] Kibok Lee, Hao Yang, Satyaki Chakraborty, Zhaowei
Cai, Gurumurthy Swaminathan, Avinash Ravichandran, and
Onkar Dabeer. Rethinking few-shot object detection on a
multi-domain benchmark. In Proceedings of the European
Conference on Computer Vision, 2022. 6
[22] Bohao Li, Rui Wang, Guangzhi Wang, Yuying Ge, Yix-
iao Ge, and Ying Shan. Seed-bench: Benchmarking mul-

--- Page 10 ---

timodal llms with generative comprehension. arXiv preprint
arXiv:2307.16125, 2023. 1, 2, 3
[23] Bo Li, Yuanhan Zhang, Liangyu Chen, Jinghao Wang,
Jingkang Yang, and Ziwei Liu.
Otter:
A multi-modal
model with in-context instruction tuning.
arXiv preprint
arXiv:2305.03726, 2023. 6, 7
[24] Junnan Li, Dongxu Li, Caiming Xiong, and Steven Hoi.
Blip: Bootstrapping language-image pre-training for unified
vision-language understanding and generation. In Proceed-
ings of the International Conference on Machine Learning,
pages 12888–12900. PMLR, 2022. 1
[25] Junnan Li, Dongxu Li, Silvio Savarese, and Steven Hoi.
BLIP-2:
Bootstrapping language-image pre-training with
frozen image encoders and large language models. In Pro-
ceedings of the International Conference on Machine Learn-
ing, 2023. 1, 3, 6
[26] Yifan Li, Yifan Du, Kun Zhou, Jinpeng Wang, Wayne Xin
Zhao, and Ji-Rong Wen. Evaluating object hallucination in
large vision-language models. In Proceedings of the Confer-
ence on Empirical Methods in Natural Language, 2023. 1,
2, 3, 5, 13
[27] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays,
Pietro Perona, Deva Ramanan, Piotr Doll´ar, and C Lawrence
Zitnick. Microsoft coco: Common objects in context. In
Proceedings of the European Conference on Computer Vi-
sion, 2014. 2, 3, 4, 5
[28] Fuxiao Liu, Kevin Lin, Linjie Li, Jianfeng Wang, Yaser
Yacoob, and Lijuan Wang.
Aligning large multi-modal
model with robust instruction tuning.
arXiv preprint
arXiv:2306.14565, 2023. 6, 7
[29] Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee.
Improved baselines with visual instruction tuning.
arXiv
preprint arXiv:2310.03744, 2023. 3, 6, 7, 8
[30] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee.
Visual instruction tuning. In Advances in Neural Information
Processing Systems, 2023. 1, 3, 6, 7, 8
[31] Haotian Liu, Chunyuan Li, Yuheng Li, Bo Li, Yuanhan
Zhang, Sheng Shen, and Yong Jae Lee.
Llava-next: Im-
proved reasoning, ocr, and world knowledge, 2024. 6, 7
[32] Yuan Liu, Haodong Duan, Yuanhan Zhang, Bo Li, Songyang
Zhang, Wangbo Zhao, Yike Yuan, Jiaqi Wang, Conghui He,
Ziwei Liu, Kai Chen, and Dahua Lin. Mmbench: Is your
multi-modal model an all-around player?
arXiv preprint
arXiv:2307.06281, 2023. 1, 2, 3, 5
[33] Shayne
Longpre,
Le
Hou,
Tu
Vu,
Albert
Webson,
Hyung Won Chung, Yi Tay, Denny Zhou, Quoc V Le, Barret
Zoph, Jason Wei, and Adam Roberts. The flan collection:
Designing data and methods for effective instruction tuning.
In Proceedings of the International Conference on Machine
Learning, 2023. 5
[34] Hwee Tou Ng, Siew Mei Wu, Ted Briscoe, Christian Hadi-
winoto, Raymond Hendy Susanto, and Christopher Bryant.
The CoNLL-2014 shared task on grammatical error correc-
tion. In Proceedings of the Eighteenth Conference on Com-
putational Natural Language Learning: Shared Task, 2014.
5
[35] OpenAI. Gpt-4 technical report, 2023. 2, 3
[36] Zhiliang Peng, Wenhui Wang, Li Dong, Yaru Hao, Shaohan
Huang, Shuming Ma, and Furu Wei. Kosmos-2: Ground-
ing multimodal large language models to the world. arXiv
preprint arXiv:2306.14824, 2023. 1, 3
[37] Tina D Purnat, Paolo Vacca, Christine Czerniak, Sarah
Ball, Stefano Burzo, Tim Zecchin, Amy Wright, Supriya
Bezbaruah, Faizza Tanggol, `Eve Dub´e, Fabienne Labb´e,
Maude Dionne, Jaya Lamichhane, Avichal Mahajan, Sylvie
Briand, and Tim Nguyen. Infodemic signal detection dur-
ing the covid-19 pandemic: Development of a methodology
for identifying potential information voids in online conver-
sations. JMIR Infodemiology, 1(1):e30971, 2021. 5
[38] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya
Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry,
Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learn-
ing transferable visual models from natural language super-
vision. In Proceedings of the International Conference on
Machine Learning, pages 8748–8763. PMLR, 2021. 3, 6
[39] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee,
Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and
Peter J. Liu. Exploring the limits of transfer learning with a
unified text-to-text transformer. Journal of Machine Learn-
ing Research, 2020. 3, 5
[40] Anna Rohrbach, Lisa Anne Hendricks, Kaylee Burns, Trevor
Darrell, and Kate Saenko.
Object hallucination in image
captioning. In Proceedings of the Conference on Empirical
Methods in Natural Language, pages 4035–4045, 2018. 1,
2, 3, 14
[41] Giuliano Rossi, Jakub Kolodziej, and Gurvinder Brar. A rec-
ommender system for active stock selection. Computational
Management Science, 17, 2020. 5
[42] Shuai Shao, Zeming Li, Tianyuan Zhang, Chao Peng, Gang
Yu, Xiangyu Zhang, Jing Li, and Jian Sun. Objects365: A
large-scale, high-quality dataset for object detection. In Pro-
ceedings of the International Conference on Computer Vi-
sion, 2019. 5, 6
[43] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timoth´ee Lacroix, Baptiste
Rozi`ere, Naman Goyal, Eric Hambro, Faisal Azhar, et al.
Llama:
Open and efficient foundation language models.
arXiv preprint arXiv:2302.13971, 2023. 3
[44] Maria Tsimpoukelli, Jacob L Menick, Serkan Cabi, S. M. Ali
Eslami, Oriol Vinyals, and Felix Hill. Multimodal few-shot
learning with frozen language models. In Advances in Neural
Information Processing Systems, pages 200–212, 2021. 1, 3
[45] Junyang Wang, Yiyang Zhou, Guohai Xu, Pengcheng Shi,
Chenlin Zhao, Haiyang Xu, Qinghao Ye, Ming Yan, Ji
Zhang, Jihua Zhu, Jitao Sang, and Haoyu Tang. Evaluation
and analysis of hallucination in large vision-language mod-
els. arXiv preprint arXiv:2308.15126, 2023. 1
[46] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al.
Chain-of-thought prompting elicits reasoning in large lan-
guage models. Advances in Neural Information Processing
Systems, 2022. 8
[47] Hongbin Ye, Tong Liu, Aijia Zhang, Wei Hua, and Weiqiang
Jia. Cognitive mirage: A review of hallucinations in large

--- Page 11 ---

language models. arXiv preprint arXiv:2309.06794, 2023.
1, 3
[48] Qinghao Ye, Haiyang Xu, Guohai Xu, Jiabo Ye, Ming Yan,
Yiyang Zhou, Junyang Wang, Anwen Hu, Pengcheng Shi,
Yaya Shi, et al.
mplug-owl: Modularization empowers
large language models with multimodality. arXiv preprint
arXiv:2304.14178, 2023. 1, 3, 6, 7
[49] Weihao Yu, Zhengyuan Yang, Linjie Li, Jianfeng Wang,
Kevin Lin, Zicheng Liu, Xinchao Wang, and Lijuan Wang.
Mm-vet: Evaluating large multimodal models for integrated
capabilities. arXiv preprint arXiv:2308.02490, 2023. 3
[50] Xiaohua Zhai, Alexander Kolesnikov, Neil Houlsby, and Lu-
cas Beyer. Scaling vision transformers. In Proceedings of the
IEEE Conference on Computer Vision and Pattern Recogni-
tion, 2022. 6
[51] Yue Zhang, Yafu Li, Leyang Cui, Deng Cai, Lemao Liu,
Tingchen Fu, Xinting Huang, Enbo Zhao, Yu Zhang, Yu-
long Chen, et al.
Siren’s song in the ai ocean: A survey
on hallucination in large language models. arXiv preprint
arXiv:2309.01219, 2023. 1, 3
[52] Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei
Wang, Yupeng Hou, Yingqian Min, Beichen Zhang, Junjie
Zhang, Zican Dong, et al. A survey of large language mod-
els. arXiv preprint arXiv:2303.18223, 2023. 1
[53] Yiyang Zhou, Chenhang Cui, Jaehong Yoon, Linjun Zhang,
Zhun Deng, Chelsea Finn, Mohit Bansal, and Huaxiu
Yao. Analyzing and mitigating object hallucination in large
vision-language models, 2023. 1, 8
[54] Deyao Zhu, Jun Chen, Xiaoqian Shen, Xiang Li, and Mo-
hamed Elhoseiny.
Minigpt-4: Enhancing vision-language
understanding with advanced large language models. arXiv
preprint arXiv:2304.10592, 2023. 1, 6, 7

--- Page 12 ---

A
Voting Mechanism Ablation
Model
k
PALL
RALL
F 1
ALL
F 0.5
ALL
PCLS
RCLS
F 1
CLS
F 0.5
CLS
Ignore %
Adapter-v2
9
63.6
73.3
68.1
65.3
68.2
70.6
69.4
68.7
2.4
5
61.8
75.0
67.7
64.0
65.7
72.0
68.7
66.9
0.0
8
63.4
73.8
68.2
65.2
68.0
70.8
69.4
68.5
1.4
Adapter-v2.1
9
63.8
73.7
68.4
65.5
67.4
71.2
69.3
68.1
2.4
5
61.7
75.3
67.8
64.0
64.7
72.5
68.4
66.1
0.0
8
63.6
74.1
68.5
65.5
67.2
71.5
69.3
68.0
1.5
InstructBLIP
9
70.8
74.3
72.5
71.5
77.2
71.9
74.5
76.1
2.5
5
68.2
77.2
72.4
69.8
73.2
74.3
73.7
73.4
0.0
8
70.6
75.1
72.8
71.4
76.8
72.3
74.5
75.9
1.5
Otter-Image
9
33.0
31.2
32.1
32.7
25.2
16.9
20.2
22.9
8.5
5
25.6
34.7
29.5
27.1
16.4
20.1
18.0
17.0
0.0
8
32.4
31.8
32.1
32.3
23.9
17.2
20.0
22.2
4.8
MiniGPT-4
9
81.7
59.8
69.0
76.1
79.9
61.8
69.7
75.5
2.9
5
74.8
64.9
69.5
72.6
73.0
65.4
69.0
71.3
0.0
8
80.8
61.1
69.6
75.9
79.1
62.4
69.8
75.1
1.8
MiniGPT-v2
9
79.0
66.6
72.3
76.2
77.6
67.0
71.9
75.2
2.8
5
73.6
71.4
72.5
73.1
72.1
70.5
71.3
71.7
0.0
8
78.4
67.8
72.7
76.0
76.9
67.7
72.0
74.8
1.8
LLaVA-Mistral
9
86.8
71.8
78.3
83.6
84.4
64.2
70.8
77.5
2.7
5
82.8
75.9
78.3
81.2
78.5
68.3
71.2
77.4
0.0
8
86.3
73.1
78.5
83.3
83.7
65.0
71.2
77.4
1.6
mPLUG-Owl
9
55.5
71.9
62.6
58.1
66.3
68.3
67.3
66.7
2.4
5
54.3
73.9
62.6
57.3
63.7
69.9
66.6
64.8
0.0
8
55.5
72.6
62.9
58.2
66.2
68.6
67.4
66.7
1.4
LRV-Instruction-v2
9
82.0
56.7
67.0
75.3
78.4
58.8
67.2
73.5
3.6
5
77.5
60.8
68.1
73.5
74.6
61.9
67.7
71.7
0.0
8
81.7
57.9
67.8
75.5
78.0
59.4
67.4
73.4
2.0
LLaVA-v1.3
9
80.5
65.2
72.1
76.9
79.9
65.3
71.9
76.5
2.4
5
76.4
68.7
72.4
74.7
75.6
68.0
71.6
73.9
0.0
8
80.0
66.3
72.5
76.9
79.4
65.8
72.0
76.3
1.4
Table 4. Comparison of Voting Mechanisms in THRONE. We compare three different voting mechanisms: unanimous, k = 9; simple
majority, k = 5; and jury majority, k = 8. Moreover in each case we report the number of ignore labels as a result of each voting
mechanism. The number of labels is 400, 000 for a given LVLM. We find that the number of ignore labels is low is almost all cases and
metrics are strongly correlated (> 0.99). In THRONE, we use a unanimous voting mechanism (k = 9) to minimize the likelihood of
hallucination judgement errors.

--- Page 13 ---

B
THRONE vs. POPE Sampling
Model
Sampling
PALL
RALL
F 1
ALL
F 0.5
ALL
PCLS
RCLS
F 1
CLS
F 0.5
CLS
THRONE
63.6
73.3
68.1
65.3
68.2
70.6
68.3
68.0
POPE
77.3
73.2
75.2
76.5
84.6
70.0
76.9
81.2
Adapter-v2
∆
(-13.7)
0.2
(-7.1)
(-11.1)
(-16.3)
0.5
(-8.6)
(-13.2)
THRONE
63.8
73.7
68.4
65.5
67.4
71.2
68.1
67.5
POPE
79.2
73.2
76.1
77.9
85.4
71.8
76.3
80.6
Adapter-v2.1
∆
(-15.4)
0.5
(-7.7)
(-12.4)
(-18.0)
(-0.6)
(-8.2)
(-13.2)
THRONE
70.8
74.3
72.5
71.5
77.2
71.9
73.1
75.2
POPE
82.2
74.4
78.1
80.5
85.0
70.0
77.9
82.6
InstructBLIP
∆
(-11.4)
0.0
(-5.5)
(-9.0)
(-7.8)
1.9
(-4.8)
(-7.4)
THRONE
33.0
31.2
32.1
32.7
25.2
16.9
18.7
21.5
POPE
66.5
34.9
45.7
56.3
70.7
17.3
35.6
49.2
Otter-Image
∆
(-33.5)
(-3.7)
(-13.7)
(-23.6)
(-45.5)
(-0.4)
(-17.0)
(-27.7)
THRONE
81.7
59.8
69.0
76.1
79.9
61.8
67.6
73.6
POPE
89.1
58.7
70.8
80.7
88.2
60.0
70.5
78.9
MiniGPT-4
∆
(-7.5)
1.1
(-1.7)
(-4.7)
(-8.2)
1.8
(-2.9)
(-5.4)
THRONE
79.0
66.6
72.3
76.2
77.6
67.0
70.4
74.0
POPE
88.3
65.8
75.4
82.7
89.8
68.5
76.3
82.6
MiniGPT-v2
∆
(-9.3)
0.8
(-3.1)
(-6.5)
(-12.2)
(-1.5)
(-5.9)
(-8.6)
THRONE
74.7
77.2
75.9
75.2
78.0
76.1
76.3
77.1
POPE
83.8
76.6
80.0
82.2
87.8
74.6
80.0
84.4
LLaVA-Mistral
∆
(-9.1)
0.7
(-4.1)
(-7.1)
(-9.8)
1.5
(-3.7)
(-7.3)
THRONE
55.5
71.9
62.6
58.1
66.3
68.3
65.2
65.3
POPE
72.9
71.2
72.0
72.6
82.0
64.5
74.1
78.6
mPLUG-Owl
∆
(-17.4)
0.7
(-9.4)
(-14.4)
(-15.6)
3.7
(-8.9)
(-13.3)
THRONE
82.0
56.7
67.0
75.3
78.4
58.8
65.0
71.5
POPE
88.6
54.8
67.7
78.9
85.0
56.2
68.8
77.4
LRV-Instruction-v2
∆
(-6.6)
1.9
(-0.7)
(-3.6)
(-6.6)
2.6
(-3.7)
(-5.9)
THRONE
80.5
65.2
72.1
76.9
79.9
65.3
70.4
75.2
POPE
85.5
61.6
71.6
79.3
87.9
61.7
72.6
80.8
LLaVA-v1.3
∆
(-4.9)
3.6
0.5
(-2.4)
(-8.0)
3.6
(-2.2)
(-5.5)
THRONE
68.1
61.0
64.4
66.6
69.9
56.4
62.2
66.8
POPE
81.5
64.4
72.0
77.4
86.2
59.2
70.4
78.8
LLaVA-v1.5
∆
(-13.4)
(-3.4)
(-7.6)
(-10.9)
(-16.2)
(-2.7)
(-8.2)
(-12.0)
Table 5. Balanced Sampling (POPE) vs. Exhaustive Sampling (THRONE): Applying POPE sampling to THRONE leads to an
underestimation of the prevalence of Type I hallucinations regardless of LVLM.
In the main paper, we demonstrated how the sampling method used in POPE [26] leads to an underestimation of Type
II hallucinations and outline a complete version of POPE (POPE-C), which shows the true extent of Type II hallucinations
in LVLMs. In this section, we perform the opposite—we apply POPE type sampling to THRONE and compare the results
to the complete sampling method used in THRONE as outlined in the main paper. Tab. 5 shows the results of applying
POPE style sampling to THRONE, once again, applying POPE style sampling leads to a large underestimation of Type I
hallucinations. POPE style sampling applied to THRONE leads to a mean underestimation of F 0.5
CLS by 10.9 points compared
to complete sampling, which is the default in THRONE.

--- Page 14 ---

C
CHAIR Overview
We present a detailed description of the CHAIR evaluation presented in [40] below. The method of CHAIR, like THRONE,
attempts to capture the extent of hallucinations in free-form generated text pertaining an image, however, focuses on more
traditional image captioners. Similarly to THRONE, CHAIR does not use concept-focused prompts (i.e. instead is focused
on “Type-I”) and is intended to be used only in captioning tasks. CHAIR defines a manual pipeline on-top of the annotated
MSCOCO image dataset to produce a list of ground truth objects present in the scene.
Given a set of ground truth objects in an image and a model-generated image caption, CHAIR extracts the objects present
in the scene via a traditional hard-rule extraction method and then attempts to map each of the predicted objects into one of the
80 class categories of MSCOCO. The mapping of the extracted objects from the caption into the class set of MSCOCO uses a
pre-defined synonym dictionary for each object category. Once the objects of the predicted caption are extracted and mapped
to one of the MSCOCO categories, CHAIR evaluates for “false-positive” predictions (i.e. hallucinations). In particular the
authors introduce two variants of CHAIR, the first variant CHAIRi quantifies the extent of hallucinated instances as,
  \tex t  {CHAIR }_i = \f
rac {|\ { \text {hall. object} \}|}{|\{ \text {pred. object} \}|}. 
In this setting, hallucinations would be objects extracted from the model-generated captions that after being mapped, are still
not present in the ground-truth object list for the corresponding instance. We note that CHAIRi can be viewed as measuring
the “false discovery rate” (FDR) that is 1 −P where P is the precision. Using Precision as the main metric, however
is limiting as it does not take into account the “False Negative Rate” (FNR) which is 1 −R where R is the recall. This
implies that by lacking recall measurements, CHAIRi may assign high scores to short and incomplete captions which are
not comprehensive in detailing the image. This is in stark contrast with the new generation of LVLM models powered by
LLMs which are designed to be more exhaustive and detailed and makes the use of CHAIRi problematic when evaluating
with LVLMs. We note that CHAIRi is the main metric used when people report “CHAIR scores”, and typically reported
numbers correspond to the mean CHAIRi score across the MSCOCO validation set of images.
The second variation of CHAIR is the CHAIRs which simply measure the number of sentences (predictions) that include
at least 1 hallucination as compared with all sentences considered,
  \tex t  {CHAIR}_s = \frac  {|\{ \t
ext { sentences w
/ hall. object} \}|}{|\{ \text {all sentences} \}|}. 
(4)
Note that CHAIRs does not measure the extent of hallucination within a sentence, just the existence of at least one halluci-
nation. This is problematic as it does not capture the extent of hallucination in the sentence especially for long-form text and
does not elucidate if a caption contains many or a single hallucination.
Producing ground truth in CHAIR
To create a list of ground truth objects from MSCOCO annotations, the authors of
CHAIR harness two annotation types to produce the most exhaustive list of ground truth objects. First the authors directly use
all of the instance segmentation labels for each image, which they aggregate into a unique list of objects existing in the image.
Next the authors use the 5 human-labelled captions of each image in MSCOCO and use the same extraction and mapping
pipeline applied to the predictions to produce an additional set of objects that are present in the captions. Both objects lists
are combined and the authors note that captioning ground truth and instance segmentation ground truth objects are often
complementary as they follow different styles. Therefore combining objects from both types of object lists is beneficial for
the most exhaustive final ground truth list.
D
Qualitative Evaluation of THRONE
D.1
Evaluation Method
We include a self-contained file (THRONE qual eval results.html) in the Supplementary Material, which shows the qual-
itative evaluation and comparison of THRONE and CHAIR. For each LVLM evaluated, we sample 10 COCO images at
random in which THRONE and CHAIR disagree and 5 COCO images in which THRONE and CHAIR agree. Therefore,
we qualitatively evaluate 165 responses. These results are summarized in Tab. 6
By calculating error rates for each of these cases and noting the proportion of responses in which THRONE and CHAIR

--- Page 15 ---

Method
CHAIR == THRONE?
#Responses (%)
#Responses Evaluated
#Judgements
#Judgement Errors
Error Rate
CHAIR/THRONE
✓
38350 (69.7%)
55
157
4
2.5%
THRONE
✗
16650 (30.3%)
110
376
30
8.0%
CHAIR
✗
16650 (30.3%)
110
477
111
23.3%
Table 6. Summary of Qualitative Evaluation: Our qualitative results show that for responses in which THRONE and CHAIR differ,
there is a large difference in the error rate. When THRONE and CHAIR agree, the error rate is small.
#Responses Analyzed
#False Positives Identified
#Hallucinations
#Misclassifications
90
71
69
2
Table 7. Hallucinations Dominate False Positives: Human evaluation establishes the vast majority ( 69
71 ≈97%) of false positive object
classes in LVLM responses are true hallucinations rather than plausible misclassifications of objects.
disagree we can estimate the overall error rate of each method using a weighted sum.
  \tex tbf { Meth o d Error Ra te} = & \ ( \ text { Agre em ent Propo rtion
} ) \times (\te xt {Error R a te in Agre em ent Case}) \ \ & +
 (\te xt {D isag r eemen t  Prop o rtion } ) \ti m es (\ t ext {Error Rate in Disagreement Case}) \\ \textbf {CHAIR Error Rate} = & \ 0.697 \times 0.025 + 0.303 \times 0.233 = 0.088 = 8.8\% \\ \textbf {\throne Error Rate} = & \ 0.697 \times 0.025 + 0.303 \times 0.080 = 0.043 = 4.3\%
D.2
Discussion
We find that the plurality of errors made in THRONE relate to a mismatch between the LM definition of a certain class and
the definiton in COCO. The most clear example is in the tv COCO class. In COCO, this class includes computer monitors,
whereas for an LM, the implication of the existence computer monitors in an LVLM response does not lead to a “yes”
response when asked Is there a tv in this image? or similar. When doing an manual evaluation our human oracle is
aware of the particular COCO class definitions and answers accordingly. Using a handcrafted rule for tv and other similar
COCO classes, we would expect the error rate of THRONE to reduce significantly, but in THRONE we deliberately avoid
the use of handcrafted rules.
As mentioned in the main paper, the errors in CHAIR are more fundamental and result due to simple text matching of
synonyms not being able to discriminate between abstract concepts alluded to in a response and direct objects implied to exist
in the image based on the response.
Tab. 7 shows results for human analysis of false positives. We analyze 90 responses, the 15 samples for mPLUG-Owl,
MiniGPT-v2, MiniGPT-4, LLaVA-7b-v1.5, LLaVA-7b-v1.3 and InstructBLIP—the final 90 responses in the self-contained
file: THRONE qual eval results.html in the Supplementary Material.
E
Improved Baseline Implementation Details
In the main paper, we introduced a simple method to augment the LLaVA visual instruction tuning data with an object
enumeration task to reduce Type I and Type II hallucinations when used to train LLaVA models. The format used for object
enumeration is:
Instruction: <image> Give a list of objects and locations
in the image.
Response:
{class_name_1} [{location_1}/absent]
...
{class_name_N} [{location_N}/absent]
where location i represents the location of the bounding box center point on a 3 × 3 grid.
We give additional details on the construction of the object enumeration task here.
E.1
Object Enumeration Implementation Details
The LLaVA visual instruction tuning data contains 157712 samples applied to 81479 images from the COCO training set
(some images correspond to multiple samples). We ensure the absolute character length of our object enumerate task for a

--- Page 16 ---

single sample is not exceedingly long—we do not want the visual instruction tuning data to be pushed outside the context
length of the LLaVA model. This is done by limiting the number of instances per class in a sample to 3.
For each sample we construct an object enumeration task using bounding box data as follows: first, sort bounding box
annotations for a given image by box area in descending order; second, loop over the sorted annotations adding the instance
(class name i, location i) to the object enumeration task if there are less than 3 instances of class name in the task; third,
sample 6 negative classes and append them to the object enumeration task using absent as the location string.
The sampling of negative classes is detailed next.
E.2
Negative Sampling Implementation Details
To sample negatives in the object enumeration task we first build a co-occurence matrix from the bounding box annotations.
The pseudocode for building this matrix is as follows:
from pycocotools.coco import COCO
import numpy as np
train_dset = COCO(instances_path)
num_cats = len(train_dset.getCatIds())
co_occur = np.array((num_cats, num_cats))
cat_id2cont_id = {x: i for i, x in sorted(enumerate(train_dset.getCatIds()))}
for iid in train_dset.getImgIds():
anns = train_dset.loadAnns(train_dset.getAnnIds(imgIds=iid))
pres_cats = [coco_cid2cont_cid[x[’category_id’]] for x in anns]
pres_cats = np.unique(pres_cats)
for r in pres_cats:
for c in pres_cats:
if r != c:
co_occur[r, c] += 1
After building this co-occurence matrix negative classes are sampled in a manner which is aware of the classes present in
a given image. The pseudocode is as follows (using some variables from the above pseudocode):
present_cat_ids: List[int]
# list of category ids present in the image
present_cont_ids = [cat_id2cont_id[x] for x in present_cat_ids
# combine co-occurence across present categories
# ensuring present categories can not be sampled
present_co_occur = co_occur[present_cont_ids].copy()
present_co_occur[:, present_cont_ids] = 0
present_co_occur = present_co_occur / present_co_occur.sum(axis=1, keepdims=True)
present_co_occur = present_co_occur.sum(axis=0)
present_co_occur = present_co_occur / present_co_occur.sum()
# sharpen distribution
present_co_occur = present_co_occur ** 10
present_co_occur = present_co_occur / present_co_occur.sum()
rng = np.random.RandomState(iid)
neg_ids = rng.choice(
sorted(train_dset.getCatIds()),
size=6,
p=present_co_occur,
replace=False
)
This method of sampling yields negative classes which commonly co-occur with positive classes in a given image. There-
fore, the object enumeration task trains the LVLM to distinguish individual objects and classes rather than relying on global
context.

--- Page 17 ---

E.3
Object Enumeration Data Details
In Table 3 of the main paper, we present results on THRONE, POPE and POPE-C when training with our object enumeration
task using COCO or COCO and VisualGenome as object enumeration data. Approximately 33000 of the 81479 COCO
images in the LLaVA visual instruction tuning data are contained in the VisualGenome dataset. When using COCO and
VisualGenome data, we construct the object enumeration task for an image from VisualGenome data when possible and
COCO otherwise—we do not combine COCO and VisualGenome annotations for any image.
E.4
Inference Details
In Table 3 of the main paper, we present results on THRONE, POPE and POPE-C when training with our object enumeration
task and performing the object enumeration task at inference. In the next section we show the effect of not performing object
enumeration during inference on THRONE and POPE, instead directly addressing the relevant task.
E.5
Ablation Results on Improved Baseline
Obj. Enum.
Obj. Enum.
Obj. Enum.
THRONE
POPE
Model
Data
Negatives
Inference
PCLS
RCLS
F 0.5
CLS
P
R
F 1
✗
N/A
N/A
79.9
65.3
76.5
58.0
98.4
73.0
COCO
✗
✓
82.4
69.2
79.4
64.8
95.2
77.1
LLaVA-v1.3
COCO + VG
✗
✓
85.8
60.4
79.1
66.0
95.3
78.0
COCO
✓
✓
83.2
68.8
79.9
73.2
88.2
80.0
COCO + VG
✓
✓
86.2
67.0
81.5
83.0
82.5
82.8
✗
N/A
N/A
69.9
56.4
66.8
81.9
90.8
86.1
LLaVA-v1.5
COCO + VG
✓
✗
79.3
76.1
78.6
83.2
86.4
84.8
COCO + VG
✓
✓
86.1
77.0
84.1
89.8
83.7
86.7
Table 8. Effect of Negatives and Inference: Including negatives in our object enumeration task improves performance on THRONE and
POPE in terms of precision and F-score. Performing the object enumeration task at inference time improves performance on THRONE
and POPE, but hampers inference time as the object enumeration task can generate long sequences.
F
Limitations
In this paper we present THRONE which is a step towards measuring and mitigating hallucinations in LVLMs, nonetheless,
our work has few key limitations which we list below.
1. THRONE is concerned with only measuring hallucinations in LVLM predictions in the form of a false existence of an
object in a closed set of classes. As observed in LLMs, hallucinations are much more multifaceted and include not just
objects outside a pre-defined vocabulary, but also many abstract concepts such as wrong reasoning relating to a visual
scene as well as wrong attributes of a particular objects or person. These additional hallucinations are not possible to be
measured with THRONE without modifications.
2. The presented method of THRONE only focused on “Type-I hallucinations” which does not paint a complete picture
of the hallucinating behavior of an LVLM. Indeed we present POPE-C in Fig. 7 to extend hallucination measurements
in both Type-I and Type-II hallucinations. We present POPE-C as an extension of POPE since we observe that POPE
severely undercounts hallucinations in Type-II form.
3. Due to lack of general and exhaustive ground truth object label lists for a given image, our method relies on curated
datasets such as MCOCO or Object365 that have detailed annotations that are complete on an image level, which are
needed for our evaluation.
4. Our method focuses only on the hallucination bias of LVLMs but does not include measurements of other types of bias of
LVLM generations (e.g. related to concepts of fairness in generation) which we leave for future work.
G
Ethical Considerations
We present THRONE which is a general evaluation pipeline for measuring hallucinations (specifically “Type-I” halluci-
nations) in Large-Vision-Language Models (LVLMs). Overall we believe that our contribution is ethically positive as it
measures and shows that existing public LVLMs are not yet ready to be deployed in mission critical applications, as we
observe that they still suffer from hallucinating objects to a large extent. In addition we believe our presented evaluation
framework also provides for a “north-star” in measuring evaluation and can aid the field and practitioners alike in measuring
and making progress towards reducing evaluations in LVLMs as well as electing to use one LVLM over another. We note that
measuring societal bias in LVLMs is highly important pre-requisite before their deployment, however this is not investigated
in the current work.

```
