---
title: "2025-Unknown-Rice-VL Evaluating Vision-Language Models for Cultural Understanding - PDF Extract"
source_pdf: "2025-Unknown-Rice-VL Evaluating Vision-Language Models for Cultural Understanding.pdf"
pages: 14
extracted_at: "2026-02-13T09:50:28.749505"
---

# PDF Extract: 2025-Unknown-Rice-VL Evaluating Vision-Language Models for Cultural Understanding

**Source PDF:** 2025-Unknown-Rice-VL Evaluating Vision-Language Models for Cultural Understanding.pdf
**Total Pages:** 14

---

## Content

```
--- Page 1 ---

Rice-VL: Evaluating Vision-Language Models for Cultural Understanding
Across ASEAN Countries
Tushar Pranav1∗, Eshan Pandey1*, Austria Lyka Diane Bala1, Aman Chadha2†,
Indriyati Atmosukarto1, Donny Soh Cheng Lock1
1Singapore Institute of Technology
2Amazon GenAI, Palo Alto, CA, USA
{pranav.tushar, pandey.eshan, lyka.austria, indriyati, donny.soh}@singaporetech.edu.sg,
hi@aman.ai
Abstract
Vision-Language Models (VLMs) excel in
multimodal tasks but often exhibit Western-
centric biases, limiting their effectiveness
in culturally diverse regions like Southeast
Asia (SEA). To address this, we introduce
RICE-VL, a novel benchmark evaluating VLM
cultural understanding across 11 ASEAN
countries.
RICE-VL includes over 28,000
human-curated Visual Question Answering
(VQA) samples—covering True/False, Fill-in-
the-Blank, and open-ended formats—and 1,000
image-bounding box pairs for Visual Ground-
ing, annotated by culturally informed experts
across 14 sub-ground categories. We propose
SEA-LAVE, an extension of the LAVE metric,
assessing textual accuracy, cultural alignment,
and country identification. Evaluations of six
open- and closed-source VLMs reveal signif-
icant performance gaps in low-resource coun-
tries and abstract cultural domains. The Visual
Grounding task tests models’ ability to local-
ize culturally significant elements in complex
scenes, probing spatial and contextual accuracy.
RICE-VL exposes limitations in VLMs’ cul-
tural comprehension and highlights the need
for inclusive model development to better serve
diverse global populations.
1
Introduction
The advancement of large vision-language models
(LVLMs) (Achiam et al., 2023; Bai et al., 2023;
Beyer et al., 2024; Liu et al., 2023) has propelled
substantial progress in multimodal tasks such as im-
age captioning, visual question answering, and dia-
logue generation. However, a critical gap persists in
their ability to effectively interpret and respond to
culturally specific concepts, particularly within di-
verse and low-resource regions like Southeast Asia
(Aji et al., 2022; Yong et al., 2023; Myung et al.,
2024). While existing LVLMs demonstrate robust
*Equal contribution.
†Work done outside role at Amazon.
Figure 1: An example instance from each task in RICE-
VL Benchmark: i) culturalVQA; ii) cultural Visual
Grounding.
performance on datasets grounded in high-resource,
Western-centric contexts, they often struggle to gen-
eralize to the complex cultural nuances, hybrid tra-
ditions, and multilingual environments characteris-
tic of ASEAN countries (Cahyawijaya et al., 2025;
Romero et al., 2024; Liu et al., 2021; Gustafson
et al., 2023; Shankar et al., 2017). Current bench-
marks assessing cultural and multilingual compe-
tence in vision-language models are predominantly
focused on Western and Anglocentric settings, re-
sulting in a significant underrepresentation of cul-
tural richness from countries such as Indonesia,
Vietnam, the Philippines, and Myanmar—regions
distinguished by unique visual and linguistic mark-
ers shaped by centuries of local tradition, colo-
nial influence, and contemporary globalization This
Western-centric bias underscores the pressing need
for culturally diverse benchmarks to systematically
evaluate and enhance the cultural inclusiveness and
alignment of modern LVLMs.
In response to these challenges, we propose
RICE-VL, a comprehensive benchmark explic-
itly designed to evaluate the cultural understanding
arXiv:2512.01419v1  [cs.CV]  1 Dec 2025

--- Page 2 ---

Feature
SEA-Crowd
SEA-VL
RICE-VL
Primary Focus
Multilingual and multimodal data aggregation
Large-scale culturally relevant image dataset
Cultural reasoning and evaluation in VLMs
Data Modalities
Text, audio, image
Image
Image with culturally annotated tasks
Data Collection Methods
Aggregation of existing datasets
Crowdsourcing, web crawling, synthetic generation
Curated by trained cultural annotators
Evaluation Tasks
Language processing tasks across modalities
Image captioning, retrieval
VQA (including True/False, Fill in the Blanks), VG
Cultural Reasoning Emphasis
Limited
Moderate
High
Human-Centric Annotations
Yes
Partially (crowdsourced and synthetic)
Yes (trained cultural experts)
Table 1: Comparative analysis of SEA-Crowd, SEA-VL, and RICE-VL benchmarks.
and contextual reasoning capabilities of VLMs in
Southeast Asia. The RICE-VL benchmark consists
of two core tasks: culturalVQA and cultural visual
grounding, adapted from prior works, including cul-
turalVQA (Nayak et al., 2024) and cultural visual
grounding from the globalRG benchmark (Bhatia
et al., 2024). Figure 1 presents the examples of
these two tasks.
The culturalVQA task consists of three core
components: Question Answering, True or False,
and Fill in the Blanks, requiring models to integrate
both visual and textual information. This structure
provides a comprehensive framework for evaluat-
ing the models’ capability to recognize and reason
about cultural nuances across diverse contexts.
The cultural visual grounding task requires
models to pinpoint specific coordinates of cultur-
ally relevant elements depicted in the images, as-
sessing their spatial understanding of cultural rep-
resentations.
Our evaluation on state-of-the-art VLMs reveals
a persistent gap in cultural understanding, particu-
larly concerning low-resource Southeast Asian cul-
tures. Closed-source models such as GPT-4O and
Claude-3-Opus outperform open-source counter-
parts across most countries, but all models demon-
strate reduced accuracy in underrepresented re-
gions like Timor-Leste, Brunei, and Laos.
Our contributions are as follows:
• We present RICE-VL, a culturally diverse mul-
timodal benchmark designed to capture the rich
cultural context of ASEAN countries. Comprising
over 28,000 question-answer tasks for VQA based
on 7000 images, and 1,000 image-bounding box
tasks for Visual Grounding, the benchmark offers
extensive coverage across 11 ASEAN countries,
encompassing a comprehensive range of cultural
themes.
• The dataset is systematically developed and rig-
orously validated by annotators trained in cultural
contexts over a comprehensive 720-hour annota-
tion period (6 annotators, 6 hours/day, 20 days),
ensuring cultural relevance and accuracy across
both low- and high-resource ASEAN countries.
• We benchmark existing state-of-the-art VLMs
on RICE-VL, identifying key performance gaps
and areas for improvement, with particular atten-
tion to the influence of Western centric biases on
model performance.
2
Related Works
The development of large vision-language mod-
els (VLMs) has significantly advanced multi-
modal tasks, yet their performance often reflects a
Western-centric bias due to the predominance of
Anglocentric datasets like MSCOCO (Lin et al.,
2014) and Visual Genome (Krishna et al., 2017).
These datasets primarily feature imagery and con-
texts from Western cultures, limiting VLMs’ abil-
ity to generalize to culturally diverse regions in
Southeast Asia (SEA), which encompasses over
1,300 languages and 11 countries (Cahyawijaya
et al., 2025). This bias underscores the need for
culturally inclusive benchmarks to evaluate VLMs’
understanding of non-Western cultural nuances.
Recent initiatives have increasingly sought to
address the regional imbalances in AI benchmarks
and datasets, particularly focusing on culturally nu-
anced multimodal resources. Community-driven
efforts such as AI4Bharat (Nath et al., 2025), Sar-
vam AI (Khan et al., 2024), and Krutruim AI (Khan
et al., 2025) have laid foundational work in Indic
AI, developing benchmarks and datasets that en-
capsulate regional linguistic and cultural contexts.
Similarly, Chinese AI labs have advanced the de-
velopment of culturally specific benchmarks, as
evidenced by initiatives like CVLUE (Wang et al.,
2025), VisTW: (Tam et al., 2025) and associated
datasets.
In Southeast Asia, emerging benchmarks like
ViOCRVQA (Pham et al., 2025) and MalayMMLU
(Poh et al., 2024) are contributing to the land-
scape by introducing visual and language tasks
for Vietnamese and Malay, respectively. However,
these efforts remain relatively isolated, underscor-
ing the persistent need for cohesive, culturally di-
verse benchmarks that not only capture regional nu-
ances but also facilitate robust evaluation of multi-
modal AI systems in Southeast Asia.however these

--- Page 3 ---

Country
Claude-3-Opus
GPT-4O
LLaMA 3.2 (11B)
Ola (7B)
Ovis 2 (8B)
Qwen-VL 2.5 (7B)
Brunei
0.58
0.55
0.50
0.33
0.53
0.44
Cambodia
0.66
0.64
0.62
0.45
0.52
0.53
Indonesia
0.73
0.74
0.66
0.54
0.64
0.62
Laos
0.54
0.52
0.38
0.29
0.46
0.38
Malaysia
0.78
0.77
0.74
0.54
0.66
0.58
Myanmar
0.60
0.54
0.50
0.45
0.51
0.49
Philippines
0.67
0.65
0.63
0.49
0.50
0.43
Singapore
0.79
0.73
0.70
0.43
0.64
0.57
Thailand
0.82
0.72
0.65
0.59
0.63
0.64
Timor-Leste
0.40
0.26
0.21
0.17
0.19
0.20
Vietnam
0.63
0.59
0.48
0.45
0.54
0.42
Table 2: SEA-LAVE scores for various open-source and closed-source models on CulturalVQA task.
are llimitted to individual countrues and there is a
need for a collective community led invitiate for
preserving the cultural and local values and as-
pects of sea countries? Notable among these is
SEA-Crowd (Lovenia et al., 2024), and Sea-VL,
which aggregates data spanning text, audio, and im-
ages for nearly 1,000 SEA languages, encompass-
ing 13 tasks and 36 indigenous languages. How-
ever, SEA-Crowd’s primary emphasis remains on
language processing, with limited exploration of
visual-cultural reasoning.
In Southeast Asia, SEA-Crowd (Lovenia et al.,
2024) aggregates multimodal resources across text,
audio, and images for nearly 1,000 SEA languages,
supporting 13 tasks and 36 indigenous languages.
However, its focus remains on language process-
ing, with limited emphasis on visual-cultural tasks
. SEA-VL (Cahyawijaya et al., 2025) compiles
1.28 million culturally relevant images through
crowdsourcing, web crawling, and synthetic gen-
eration, but its evaluation centers on descriptive
tasks like image captioning and retrieval, which
do not fully capture the depth of cultural under-
standing required for SEA contexts. Table 1 pro-
vides a comparative study of three major Southeast
Asian benchmarks—SEA-Crowd, SEA-VL, and
RICE-VL—highlighting their differences in focus,
modalities, data collection methods, and emphasis
on cultural reasoning.
In contrast, RICE-VL is purpose built to eval-
uate VLMs’ cultural understanding and contex-
tual reasoning in Southeast Asia. It comprises
two tasks: culturalVQA, covering question an-
swering, true/false, and fill-in-the-blanks; and cul-
tural visual grounding, which assesses the local-
ization of culturally salient elements. Unlike SEA-
VL’s reliance on synthetic data, RICE-VL uses 720
hours of expert human annotation to ensure cul-
tural accuracy and depth. RICE-VL goes beyond
surface-level evaluations by focusing on cultur-
ally grounded reasoning and localization tasks. It
highlights significant performance gaps in existing
VLMs—especially in low-resource countries—and
calls for benchmarks that emphasize cultural align-
ment, not just data diversity.
3
Task 1: Cultural Visual Question
Answering
3.1
Data Collection, Annotation, and
Verification
Data Collection .
Data collection for the cultur-
alVQA task was carried out in 11 Southeast Asian
countries, encompassing Singapore, Malaysia,
Timor-Leste, Vietnam, the Philippines, Indonesia,
Brunei, Laos, Myanmar, Thailand, and Cambodia.
The dataset was stratified into cultural domains
such as Architecture and Heritage, Clothing and At-
tire, Dance and Music, Drinks, Festivals, Food and
Desserts, Language Signs and Literature, Marriage
Customs, Notable Key Figures, Painting, Religious
Practices, Places of Worship, Traditional Games,
and Transport. Each domain was further divided
into 10 subcultures, each represented by 5 to 25
images. For instance, in the ’Food and Desserts’
category for Singapore, subcultures include Bak
Kut Teh, Rojak, Char Kway Teow, Chendol, Chilli
Crab, and Hainanese Chicken Rice. Data acqui-
sition employed web scraping targeting culturally
specific visual content across these subcategories.
Annotation .
The annotation process for cultur-
alVQA was structured to capture cultural nuances
and ensure accurate visual representation.
An-
notators, specifically trained in identifying cultur-

--- Page 4 ---

Figure 2: Cultural understanding of various models assessed on culturalVQA tasks, when the model was prompted
global context (left) and with SEA specific context (right)
Country
Claude-3-Opus
GPT-4O
LLaMA 3.2 (11B)
Ola (7B)
Ovis 2 (8B)
Qwen-VL 2.5 (7B)
Brunei
0.63
0.61
0.50
0.63
0.44
0.42
Cambodia
0.76
0.70
0.58
0.68
0.65
0.51
Indonesia
0.80
0.79
0.72
0.80
0.78
0.81
Laos
0.64
0.60
0.39
0.59
0.56
0.53
Malaysia
0.75
0.80
0.77
0.82
0.71
0.79
Myanmar
0.70
0.65
0.53
0.72
0.42
0.36
Philippines
0.59
0.85
0.67
0.71
0.53
0.43
Singapore
0.75
0.87
0.72
0.72
0.67
0.75
Thailand
0.78
0.49
0.72
0.87
0.71
0.68
Timor-Leste
0.34
0.71
0.22
0.46
0.18
0.25
Vietnam
0.59
0.63
0.58
0.66
0.74
0.59
Table 3: SEA-LAVE scores for various open-source and closed-source models on CulturalVQA task with cultural
context in the prompt.
ally significant elements, curated visual question-
answer pairs. Each image was assigned two ini-
tial questions generated using GPT-4.0 (Achiam
et al., 2023) based on metadata, followed by five
additional questions curated by annotators. The
questions encompassed True/False and Fill-in-the-
Blanks formats, emphasizing cultural-contextual
reasoning.
Verification .
Verification procedures for cultur-
alVQA involved multiple rounds of cultural rel-
evance checks. Annotators from Southeast Asia
reviewed each image-question pair to confirm cul-
tural accuracy and prevent content bias. Discrepan-
cies identified during verification were addressed
through iterative reviews, ensuring that each vi-
sual question-answer pair effectively conveyed the
intended cultural concept without introducing am-
biguity.
3.2
Task Definition and Evaluation Setup
The culturalVQA task is designed to evaluate a
model’s ability to accurately interpret and rea-
son about culturally specific visual content within
the context of Southeast Asian cultural domains.
Given an image and a corresponding question, the
model is expected to generate culturally appropri-
ate responses that reflect the visual content while
aligning with the cultural context depicted. The
task encompasses various question formats, includ-
ing True/False, Fill-in-the-Blanks, and open-ended
questions, enabling a comprehensive assessment of
the model’s cultural reasoning capabilities across
multiple dimensions.
Additionally, all experiments are conducted un-
der two distinct settings: a Global setting and a
Southeast Asian specific setting. In the Global set-
ting, the prompt includes the instruction “This is a

--- Page 5 ---

global setting”, followed by questions encouraging
open-ended, worldwide reasoning. In contrast, the
SEA specific setting includes the instruction “This
is a Southeast Asian setting” to anchor the model
within a regional context. This dual-setting design
allows us to systematically evaluate how prompt
framing influences the model’s cultural localization
performance and whether regional cues enhance its
ability to reason about culturally specific content.
Evaluating cultural reasoning in multimodal
tasks presents distinct challenges, particularly
when scaling assessments across culturally diverse
datasets. Traditional evaluation frameworks primar-
ily rely on string matching techniques to measure
alignment between model-generated outputs and
ground-truth data (Nayak et al., 2024). However,
recent studies highlight the potential of using large
language models (LLMs) as evaluators, acting as
adjudicators to assess the contextual and cultural
accuracy of responses (Mañas et al., 2024; Nayak
et al., 2024).
Building on these insights, we introduce the
Southeast Asia Linguistic Agreement with Visual
Evidence (SEA-LAVE) metric, an adaptation of
the original LAVE metric (Mañas et al., 2024) that
incorporates a cultural dimension to better align
with the objectives of our benchmark. For evalua-
tion, we employ the Qwen2.5-VL 7B model as the
reference LLM, given its strong open-source perfor-
mance and reproducibility. We deliberately exclude
proprietary models such as GPT-4 and Claude from
the evaluation step to ensure transparency and repli-
cability of results.
SEA-LAVE Metric.
To address this, we adopt
and extend the Linguistic Agreement with Visual
Evidence (LAVE) metric by introducing a cultur-
ally grounded variant: SEA-LAVE. This metric as-
sesses alignment between the model’s response and
expected output across three dimensions: textual
relevance, cultural appropriateness, and regional
specificity.
SEA-LAVE = TU + CU +
  CI
2

3
(1)
Each component is a binary score (0 or 1), deter-
mined through either human annotation or LLM-
based evaluation:
• Text Understanding (TU): Assesses seman-
tic alignment between the model output and
expected answer.
• Cultural Understanding (CU): Evaluates the
response’s adherence to the relevant cultural
context or practice.
• Country
Identification
(CI):
Measures
whether the model correctly identifies the
Southeast Asian country, with partial weight-
ing to account for ambiguity across borders.
By incorporating cultural specificity into the
scoring, SEA-LAVE offers a more holistic met-
ric for benchmarking cross-cultural competence
in vision-language models, particularly within the
diverse sociocultural landscape of Southeast Asia.
3.3
Models
For the VQA task, we benchmarked six VLMS se-
lected based on their applicability to cultural visual
reasoning and their performance in VLM leader-
boards (Duan et al., 2024). The models are catego-
rized into four open-source and two closed-source
systems. The open-source models include Qwen-
VL 2.5 (7B) (Bai et al., 2023), Ovis 2 (8B) (Lu
et al., 2024), LLaMA 3.2 (11B) (Grattafiori et al.,
2024), and Ola (7B) (Liu et al., 2025). The closed-
source models consist of GPT-4O (Achiam et al.,
2023) and Claude-3-Opus. This selection spans
a range of architectures and parameter sizes, fa-
cilitating a comprehensive evaluation of cultural
reasoning capabilities across both open and closed-
source frameworks.
3.4
Results and Analysis
As illustrated in Figure 2, model responses to cul-
turalVQA tasks show improved cultural grounding
when Southeast Asian context is explicitly included
in the prompt. Table 2 presents SEA-LAVE scores
under the global setting (without geographic cues),
while Table 3 shows the corresponding scores un-
der the SEA-specific setting. Together, these results
highlight the importance of regional grounding for
accurate cultural understanding across the 11 SEA
countries.
Do closed-source VLMs exhibit stronger cul-
tural reasoning than open-source models?
Closed-source models—Claude-3-Opus and GPT-
4O—consistently outperform their open-source
counterparts across nearly all countries. Claude-
3-Opus yields the highest SEA-LAVE scores in
high-resource countries such as Malaysia, Thailand,
and Indonesia, while GPT-4O demonstrates notable
strength in the Philippines and Timor-Leste.

--- Page 6 ---

Do region-specifc models demonstrate advan-
tages in Southeast Asian settings?
While
region-specific models like Qwen-VL 2.5 and Ovis
2 exhibit improved performance in culturally di-
verse settings, particularly Malaysia, Indonesia,
and Vietnam, they fall short of matching closed-
source models in both breadth and depth of rea-
soning. Their strength appears to correlate with
countries that have relatively higher online repre-
sentation in training corpora, but their performance
degrades in underrepresented contexts like Brunei
and Timor-Leste. This suggests that region alone
is insufficient without culturally grounded training
data.
Are VLMs equally capable across all SEA coun-
tries?
Performance varies significantly across
countries, with high-resource nations (e.g., Singa-
pore, Malaysia) yielding higher SEA-LAVE scores,
and low-resource ones (e.g., Timor-Leste, Brunei,
Laos) consistently underperforming across all mod-
els. Notably, Timor-Leste remains the most chal-
lenging for all systems, indicating limited represen-
tation in pretraining corpora and a lack of cultural
exposure.
Does prompt framing influence cultural rea-
soning in VLMs?
We observe a marked perfor-
mance boost when prompts are regionally anchored.
When explicitly framed with “This is a Southeast
Asian setting,” models—especially GPT-4O and
Ola (7B)—show improved cultural localization.
This finding affirms the importance of contextual
priming in VLM prompting and suggests a simple,
low-resource intervention to enhance model sensi-
tivity to cultural cues. For instance, Ola’s score on
Thailand jumps from 0.59 to 0.87 with the SEA-
specific prompt, an improvement not observed in
the global setting.
Collectively, these findings validate the need
for culturally aware benchmarks like RICE-VL
and affirm that improving cultural competence
in VLMs requires both diverse training data
and region-sensitive evaluation protocols.
4
Task 2: Cultural Visual Grounding
4.1
Data Collection, Annotation, and
Verification
Data Collection .
Data collection for the Vi-
sual Grounding (VG) task was systematically con-
ducted across 11 Southeast Asian countries. The
dataset was structured to represent 95 distinct cul-
tural subcategories, including ceremonial clothing,
traditional dance forms, and religious artifacts. Im-
ages were sourced using web scraping, targeting
culturally significant visual content across each
subcategory.
Annotation .
Following data collection, the an-
notation process focused on cultural specificity and
visual clarity. Annotators underwent targeted train-
ing to identify and demarcate cultural elements
amidst potential visual distractions. CVAT soft-
ware was employed to annotate bounding boxes
around cultural markers, resulting in 990 image-
bounding box pairs. Each image was annotated to
include multiple cultural markers, thereby enhanc-
ing the dataset’s complexity for cultural grounding
tasks.
Verification .
To ensure cultural accuracy and
mitigate biases, the verification process involved
multiple stages of review by annotators familiar
with Southeast Asian cultural contexts. Annotators
validated the cultural relevance of each bounding
box annotation, confirming that each visual marker
accurately reflected its designated cultural category.
Additionally, data integrity checks were performed
to identify and rectify inconsistencies, ensuring the
dataset’s robustness for downstream evaluation.
4.2
Model
The model selection was driven by two primary ob-
jectives: assessing grounding precision and evaluat-
ing cross-cultural alignment. Grounding Dino (Liu
et al., 2024) was selected for its targeted training on
grounding-specific tasks, as demonstrated by its ap-
plication in GlobalRG (Bhatia et al., 2024). Mean-
while, Qwen2.5 VL (3B and 7B) (Bai et al., 2023)
and Paligemma2 (3B and 10B) (Beyer et al., 2024)
were included as general-purpose models, leverag-
ing their robust visual-text alignment capabilities.
Kosmos2 (Peng et al., 2023) was incorporated to
evaluate its cross-modal grounding effectiveness
across culturally diverse contexts, aligning with
the comparative framework in GlobalRG (Bhatia
et al., 2024) to assess the performance gap between
task-specific and general-purpose models.
4.3
Task Definition and Evaluation
Cultural visual grounding refers to the model’s ca-
pability to accurately identify and localize cultur-
ally significant elements within a given image us-
ing bounding boxes. This task assesses the model’s
ability to discern and demarcate cultural markers

--- Page 7 ---

Category
Paligemma2 3B
Paligemma2 10B
Qwen2.5 VL 3B
Qwen2.5 VL 7B
Kosmos2
GroundingDino
Brunei
0.345
0.408
0.546
0.531
0.421
0.380
Cambodia
0.172
0.222
0.317
0.312
0.264
0.271
Indonesia
0.360
0.520
0.551
0.494
0.523
0.452
Laos
0.433
0.434
0.535
0.506
0.449
0.488
Malaysia
0.355
0.475
0.548
0.510
0.492
0.438
Myanmar
0.395
0.393
0.458
0.412
0.369
0.469
Philippines
0.286
0.463
0.478
0.520
0.451
0.389
Singapore
0.349
0.454
0.555
0.527
0.349
0.427
Thailand
0.394
0.482
0.497
0.498
0.411
0.531
Timor Leste
0.334
0.438
0.420
0.428
0.328
0.417
Vietnam
0.295
0.282
0.440
0.390
0.327
0.343
Table 4: Average IoU scores for Cultural Grounding Task across ASEAN countries using various VL models.
based on textual prompts, reflecting both grounding
precision and cultural understanding.
Given an image I and a text prompt p, the model
predicts a bounding box ˆB corresponding to the
region within I that aligns with the prompt p. The
ground truth bounding box is denoted as B.
Intersection over Union (IoU) is a widely
adopted metric for evaluating the overlap between
predicted and ground truth bounding boxes. The
IoU score quantifies the extent of overlap and is
instrumental in assessing the model’s grounding
accuracy and cultural precision.
The IoU is calculated as:
IoU = |Rpred ∩Rgtruth|
|Rpred ∪Rgtruth|
(2)
where:
• Rpred denotes the predicted bounding box.
• Rgtruth represents the ground truth bounding
box.
• |Rpred ∩Rgtruth| is the area of overlap be-
tween the predicted and ground truth bound-
ing boxes.
• |Rpred ∪Rgtruth| is the total area covered by
both bounding boxes.
In addition to evaluating model predictions, IoU
is also employed to assess consistency among hu-
man annotators. This is achieved by comparing
the IoU scores between bounding boxes drawn by
multiple annotators, providing insights into cultural
ambiguities and the reliability of cultural represen-
tations across different annotators.
4.4
Results and Analysis
Table 4 presents the average IoU scores for the
Cultural Grounding task across ASEAN countries.
Can VLMs ground culturally specific mark-
ers across SEA countries with high accuracy?
As shown in Table 4, Qwen2.5-VL consistently
achieves the highest average IoU scores across
most Southeast Asian countries, with particularly
strong performance in Singapore, Brunei, and In-
donesia. These findings highlight the importance of
multimodal pretraining that incorporates culturally
rich image-text pairs. Models that rely predomi-
nantly on geometric alignment or generic object
detection tend to underperform in contexts requir-
ing nuanced cultural understanding. The results
underscore that grounding culturally specific mark-
ers extends beyond spatial accuracy—it demands
culturally aware representation learning.
Can VLMs localize Southeast Asian cultural
artifacts with distinct visual identity?
Models
like Qwen2.5-VL and Paligemma2 excel at localiz-
ing culturally unique artifacts such as batik patterns
(Indonesia, Malaysia) and chada headgear (Thai-
land). However, when visual features resemble
common global objects—like kaya toast looking
like Western bread—models tend to make generic
predictions. This highlights a challenge in cross-
cultural disambiguation, where visual similarity
can overshadow cultural context. Accurate ground-
ing thus requires both visual recognition and cul-
turally informed understanding.
Can VLMs achieve consistent grounding across
different cultural categories?
Grounding accu-
racy differs significantly across the 14 cultural sub-
domains. Categories with clear, prominent visu-
als like Clothing, Transport, and Festivals achieve
higher IoU scores, likely due to the size and visibil-
ity of objects. In contrast, areas involving smaller
or more abstract elements—such as Religious Prac-
tices, Key Figures, and Painting—show lower accu-
racy across models. This gap is often due to visual

--- Page 8 ---

clutter or symbolic imagery that makes grounding
more difficult. These results highlight how category
complexity and visual ambiguity impact model per-
formance, especially in less represented cultural
themes.
5
Limitations
While RICE-VL provides a broad assessment of
cultural understanding in Vision-Language Mod-
els across ASEAN countries, it has several limi-
tations. Due to resource constraints, our evalua-
tion is limited to large-scale models (up to 12B
parameters), leaving the performance of smaller
or low-resource models largely unexplored. Fu-
ture work should consider these models and tech-
niques like distillation. Additionally, our current
task formats—primarily culturalVQA and ground-
ing—focus on visual-text alignment and may not
capture deeper cultural reasoning such as histor-
ical or narrative context. More expressive tasks
are needed. Lastly, the benchmark is English-only,
which simplifies evaluation but may overlook cul-
turally nuanced meanings in native languages. In-
corporating multilingual support could improve fu-
ture benchmarks.
6
Ethical Considerations
RICE-VL benchmarks cultural understanding in
VLMs across Southeast Asia using culturally
grounded tasks, with images and question-answer
pairs annotated over 720 hour. Below, we outline
key ethical challenges.
Annotator Involvement.
All annotators were re-
cruited from Southeast Asia and underwent struc-
tured training to ensure high cultural fidelity. We
acknowledge their contributions and the subjective
judgments that may shape annotations.
Cultural Generalization and Representation.
Covering 11 ASEAN countries, the dataset may
oversimplify minority, indigenous, and diaspora
experiences. Future work should prioritize more
nuanced cultural representations.
Stereotype Risk.
Some visual content may inad-
vertently reinforce cultural stereotypes. Although
our intention was to capture authentic cultural ele-
ments, we recognize that the selection and framing
of images might bias model perception. We imple-
mented multiple layers of review to mitigate this,
but residual bias may persist.
Content Bias and Privacy.
Some images may
unintentionally reinforce cultural stereotypes de-
spite efforts to capture authentic elements. Multiple
review layers were implemented to mitigate bias,
but some risk remains. The dataset will undergo
rigorous filtering to remove sensitive or identifiable
content and will be released under an ethical use
license, with documented filtering procedures to
minimize harm.
Use of AI Tools.
ChatGPT was used only for
early-stage grammar and fluency improvements.
All core research tasks were independently con-
ducted by the team.
RICE-VL aims to foster culturally inclusive
VLMs. We urge the community to use it with cul-
tural sensitivity and ethical commitment.
7
Conclusion
In this paper, we introduce RICE-VL, a cultur-
ally grounded benchmark designed to evaluate
vision-language models across 11 Southeast Asian
countries. RICE-VL includes over 28,000 human-
curated question-answer pairs and 1,000 visual
grounding annotations spanning 14 cultural cate-
gories, offering a high-resolution lens into cultural
reasoning in multimodal systems.
We evaluate six state-of-the-art VLMs across
two tasks—culturalVQA and Visual Grounding,
and observe significant disparities in performance
between open-source and closed-source models.
Additionally, performance varies across countries,
with lower accuracy in underrepresented contexts
such as Timor-Leste and Brunei.
Our results highlight the persistent limitations of
current VLMs in handling culturally nuanced con-
tent, especially in low-resource settings. Prompt
framing improves cultural localization, but deeper
cultural reasoning remains a challenge. RICE-VL
underscores the urgent need for culturally inclusive
training data, evaluation strategies, and model de-
sign—paving the way toward equitable multimodal
AI systems in the Global South.
Acknowledgments
We would like to extend our sincere gratitude to
the subject and language matter experts from the
National Institute of Education (NIE), Nanyang
Technological University (NTU), and the Singa-
pore Institute of Technology (SIT) for their support
and contributions throughout the research. This pa-
per is supported by the National Research Founda-

--- Page 9 ---

tion, Singapore under its AI Singapore Programme
(AISG Award No: AISG2-GC-2022-004).
References
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama
Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
Diogo Almeida, Janko Altenschmidt, Sam Altman,
Shyamal Anadkat, and 1 others. 2023. Gpt-4 techni-
cal report. arXiv preprint arXiv:2303.08774.
Alham Fikri Aji, Genta Indra Winata, Fajri Koto,
Samuel Cahyawijaya, Ade Romadhony, Rahmad Ma-
hendra, Kemal Kurniawan, David Moeljadi, Radi-
tyo Eko Prasojo, Timothy Baldwin, and 1 others.
2022. One country, 700+ languages: Nlp challenges
for underrepresented languages and dialects in in-
donesia. arXiv preprint arXiv:2203.13357.
Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang,
Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei
Huang, and 1 others. 2023. Qwen technical report.
arXiv preprint arXiv:2309.16609.
Lucas Beyer, Andreas Steiner, André Susano Pinto,
Alexander Kolesnikov, Xiao Wang, Daniel Salz,
Maxim Neumann, Ibrahim Alabdulmohsin, Michael
Tschannen, Emanuele Bugliarello, and 1 others. 2024.
Paligemma: A versatile 3b vlm for transfer. arXiv
preprint arXiv:2407.07726.
Mehar Bhatia, Sahithya Ravi, Aditya Chinchure, Eu-
njeong Hwang, and Vered Shwartz. 2024.
From
local concepts to universals: Evaluating the multi-
cultural understanding of vision-language models.
arXiv preprint arXiv:2407.00263.
Samuel Cahyawijaya, Holy Lovenia, Joel Ruben Antony
Moniz, Tack Hwa Wong, Mohammad Rifqi Farhan-
syah, Thant Thiri Maung, Frederikus Hudi, David
Anugraha,
Muhammad Ravi Shulthan Habibi,
Muhammad Reza Qorib, and 1 others. 2025. Crowd-
source, crawl, or generate? creating sea-vl, a mul-
ticultural vision-language dataset for southeast asia.
arXiv preprint arXiv:2503.07920.
Haodong Duan, Junming Yang, Yuxuan Qiao, Xinyu
Fang, Lin Chen, Yuan Liu, Xiaoyi Dong, Yuhang
Zang, Pan Zhang, Jiaqi Wang, and 1 others. 2024.
Vlmevalkit: An open-source toolkit for evaluating
large multi-modality models. In Proceedings of the
32nd ACM International Conference on Multimedia,
pages 11198–11201.
Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri,
Abhinav Pandey, Abhishek Kadian, Ahmad Al-
Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten,
Alex Vaughan, and 1 others. 2024. The llama 3 herd
of models. arXiv preprint arXiv:2407.21783.
Laura Gustafson, Chloe Rolland, Nikhila Ravi, Quentin
Duval, Aaron Adcock, Cheng-Yang Fu, Melissa Hall,
and Candace Ross. 2023. Facet: Fairness in com-
puter vision evaluation benchmark. In Proceedings
of the IEEE/CVF International Conference on Com-
puter Vision, pages 20370–20382.
Mohammed Safi Ur Rahman Khan, Priyam Mehta,
Ananth Sankar, Umashankar Kumaravelan, Sumanth
Doddapaneni, Sparsh Jain, Anoop Kunchukuttan,
Pratyush Kumar, Raj Dabre, Mitesh M Khapra, and
1 others. 2024. Indicllmsuite: a blueprint for creat-
ing pre-training and fine-tuning datasets for indian
languages. arXiv preprint arXiv:2403.06350.
Shaharukh Khan, Ayush Tarun, Abhinav Ravi, Ali
Faraz, Praveen Kumar Pokala, Anagha Bhangare,
Raja Kolla, Chandra Khatri, and Shubham Agarwal.
2025. Chitrarth: Bridging vision and language for a
billion people. In ICASSP 2025-2025 IEEE Interna-
tional Conference on Acoustics, Speech and Signal
Processing (ICASSP), pages 1–5. IEEE.
Ranjay Krishna, Yuke Zhu, Oliver Groth, Justin John-
son, Kenji Hata, Joshua Kravitz, Stephanie Chen,
Yannis Kalantidis, Li-Jia Li, David A Shamma, and 1
others. 2017. Visual genome: Connecting language
and vision using crowdsourced dense image anno-
tations. International journal of computer vision,
123:32–73.
Tsung-Yi Lin, Michael Maire, Serge Belongie, James
Hays, Pietro Perona, Deva Ramanan, Piotr Dollár,
and C Lawrence Zitnick. 2014.
Microsoft coco:
Common objects in context. In Computer vision–
ECCV 2014: 13th European conference, zurich,
Switzerland, September 6-12, 2014, proceedings,
part v 13, pages 740–755. Springer.
Fangyu Liu, Emanuele Bugliarello, Edoardo Maria
Ponti, Siva Reddy, Nigel Collier, and Desmond
Elliott. 2021.
Visually grounded reasoning
across languages and cultures.
arXiv preprint
arXiv:2109.13238.
Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae
Lee. 2023. Visual instruction tuning. Advances in
neural information processing systems, 36:34892–
34916.
Shilong Liu, Zhaoyang Zeng, Tianhe Ren, Feng Li, Hao
Zhang, Jie Yang, Qing Jiang, Chunyuan Li, Jian-
wei Yang, Hang Su, and 1 others. 2024. Grounding
dino: Marrying dino with grounded pre-training for
open-set object detection. In European conference
on computer vision, pages 38–55. Springer.
Zuyan Liu, Yuhao Dong, Jiahui Wang, Ziwei Liu, Win-
ston Hu, Jiwen Lu, and Yongming Rao. 2025. Ola:
Pushing the frontiers of omni-modal language model
with progressive modality alignment. arXiv preprint
arXiv:2502.04328.
Holy Lovenia, Rahmad Mahendra, Salsabil Maulana
Akbar, Lester James V Miranda, Jennifer Santoso,
Elyanah Aco, Akhdan Fadhilah, Jonibek Mansurov,
Joseph Marvin Imperial, Onno P Kampman, and 1
others. 2024. Seacrowd: A multilingual multimodal
data hub and benchmark suite for southeast asian
languages. arXiv preprint arXiv:2406.10118.

--- Page 10 ---

Shiyin Lu, Yang Li, Qing-Guo Chen, Zhao Xu, Wei-
hua Luo, Kaifu Zhang, and Han-Jia Ye. 2024. Ovis:
Structural embedding alignment for multimodal large
language model. arXiv preprint arXiv:2405.20797.
Oscar Mañas, Benno Krojer, and Aishwarya Agrawal.
2024. Improving automatic vqa evaluation using
large language models. In Proceedings of the AAAI
Conference on Artificial Intelligence, volume 38,
pages 4171–4179.
Junho Myung, Nayeon Lee, Yi Zhou, Jiho Jin, Rifki Pu-
tri, Dimosthenis Antypas, Hsuvas Borkakoty, Eunsu
Kim, Carla Perez-Almendros, Abinew Ali Ayele, and
1 others. 2024. Blend: A benchmark for llms on ev-
eryday knowledge in diverse cultures and languages.
Advances in Neural Information Processing Systems,
37:78104–78146.
Oikantik Nath, Hanani Bathina, Mohammed Safi
Ur Rahman Khan, and Mitesh M. Khapra. 2025. Can
vision-language models evaluate handwritten math?
arXiv preprint arXiv: 2501.07244.
Shravan Nayak, Kanishk Jain, Rabiul Awal, Siva Reddy,
Sjoerd Van Steenkiste, Lisa Anne Hendricks, Aish-
warya Agrawal, and 1 others. 2024. Benchmarking
vision language models for cultural understanding.
arXiv preprint arXiv:2407.10920.
Zhiliang Peng, Wenhui Wang, Li Dong, Yaru Hao,
Shaohan Huang, Shuming Ma, and Furu Wei.
2023.
Kosmos-2: Grounding multimodal large
language models to the world.
arXiv preprint
arXiv:2306.14824.
Huy Quang Pham, Thang Kien-Bao Nguyen, Quan
Van Nguyen, Dan Quang Tran, Nghia Hieu Nguyen,
Kiet Van Nguyen, and Ngan Luu-Thuy Nguyen.
2025. Viocrvqa: novel benchmark dataset and vision-
reader for visual question answering by understand-
ing vietnamese text in images. Multimedia Systems,
31(2):106.
Soon Chang Poh, Sze Jue Yang, Jeraelyn Ming Li Tan,
Lawrence Leroy Tze Yao Chieng, Jia Xuan Tan,
Zhenyu Yu, Foong Chee Mun, and Chee Seng Chan.
2024. MalayMMLU: A multitask benchmark for the
low-resource Malay language. In Findings of the
Association for Computational Linguistics: EMNLP
2024, pages 650–669, Miami, Florida, USA. Associ-
ation for Computational Linguistics.
David Romero, Chenyang Lyu, Haryo Akbarianto Wi-
bowo, Teresa Lynn, Injy Hamed, Aditya Nanda
Kishore, Aishik Mandal, Alina Dragonetti, Artem
Abzaliev, Atnafu Lambebo Tonja, and 1 others.
2024.
Cvqa: Culturally-diverse multilingual vi-
sual question answering benchmark. arXiv preprint
arXiv:2406.05967.
Shreya Shankar, Yoni Halpern, Eric Breck, James At-
wood, Jimbo Wilson, and D Sculley. 2017. No classi-
fication without representation: Assessing geodiver-
sity issues in open data sets for the developing world.
arXiv preprint arXiv:1711.08536.
Zhi Rui Tam, Ya-Ting Pai, Yen-Wei Lee, and Yun-
Nung Chen. 2025. Vistw: Benchmarking vision-
language models for traditional chinese in taiwan.
arXiv preprint arXiv:2503.10427.
Yuxuan Wang, Yijun Liu, Fei Yu, Chen Huang, Kexin
Li, Zhiguo Wan, Wanxiang Che, and Hongyang Chen.
2025. Cvlue: A new benchmark dataset for chinese
vision-language understanding evaluation. In Pro-
ceedings of the AAAI Conference on Artificial Intelli-
gence, volume 39, pages 8196–8204.
Zheng-Xin Yong, Ruochen Zhang, Jessica Zosa Forde,
Skyler Wang, Arjun Subramonian, Holy Lovenia,
Samuel Cahyawijaya, Genta Indra Winata, Lintang
Sutawika, Jan Christian Blaise Cruz, and 1 others.
2023. Prompting multilingual large language models
to generate code-mixed texts: The case of south east
asian languages. arXiv preprint arXiv:2303.13592.

--- Page 11 ---

A
APPENDIX
A.1
RICE-VL Benchmark Categories
The RICE-VL benchmark is curated to assess
the cultural understanding capabilities of Vision-
Language Models (VLMs) within Southeast Asian
contexts. It spans 11 countries—namely Singapore,
Malaysia, Indonesia, Thailand, Vietnam, the Philip-
pines, Cambodia, Laos, Myanmar, Brunei, and
Timor-Leste—and captures 14 distinct cultural sub-
ground categories. These categories were carefully
selected to reflect the region’s rich socio-cultural,
historical, and visual diversity.
Drawing inspiration from earlier cultural AI
benchmarks,
RICE-VL emphasizes culturally
grounded content that extends beyond generic vi-
sual understanding. Each category encapsulates a
unique aspect of Southeast Asian identity, shaped
by centuries of tradition, belief systems, and com-
munity practices. Categories such as Architecture
and Heritage, Festivals, Traditional Games, and
Dance and Music celebrate the visual vibrancy of
regional customs, while others like Marriage Cus-
toms, Religious Practices, and Clothing and Attire
highlight deeply rooted, often localized expressions
of culture.
In addition, RICE-VL includes visual represen-
tations of Food and Desserts, Drinks, Landmarks,
Transport, Notable Key Figures, Painting, and
Places of Worship. These domains were chosen
not only for their cultural salience but also for their
frequent appearance in public imagery and shared
narratives across ASEAN societies. All data points
were annotated by trained regional contributors and
reviewed by cultural experts to ensure contextual
fidelity.
Together, these cultural categories form the foun-
dation for evaluating VLMs on tasks such as Visual
Question Answering (VQA) and Visual Ground-
ing (VG). Future versions of the benchmark aim to
broaden the scope by incorporating folklore, oral
traditions, and region-specific vernaculars, thereby
enabling deeper cultural reasoning in multimodal
AI systems.
A.2
SEA-LAVE PROMPT
To evaluate the cultural reasoning capabilities of
Vision-Language Models in Southeast Asian con-
texts, we design SEA-LAVE (Southeast Asian Lin-
guistic Agreement with Visual Evidence), a prompt-
based evaluation framework that adapts the LAVE
metric to culturally grounded tasks. Unlike tra-
ditional string-matching or generic semantic sim-
ilarity metrics, SEA-LAVE incorporates region-
specific cultural grounding by assessing answers
across three dimensions: cultural relevance, sub-
cultural insight, and country attribution. As shown
in Table 5, we define tailored evaluation prompts
for different task formats—open-ended Question-
Answering, True/False statements, and Fill-in-the-
Blank completions—ensuring consistency and in-
terpretability across tasks. Each prompt instructs a
model-as-judge to provide both discrete scores and
qualitative justifications, allowing for fine-grained
benchmarking of models’ cultural understanding.
As outlined in Table 5, each cultural task is
guided by a prompt that emphasizes culturalVQA.
A.3
Model Performance on CulturalVQA
We evaluate the performance of various vision-
language models on the CulturalVQA task, which
involves answering culturally grounded questions
based on visual input from Southeast Asian set-
tings.
As shown in Figure 3, models such as GPT-4 and
Claude-3 demonstrate superior performance on cul-
turally nuanced queries, while smaller open-source
models exhibit more variability across countries
and question formats.
A.4
Model Performance on Cultural Visual
Grounding
We also assess the ability of models to localize cul-
turally significant objects or scenes within images,
captured under the Cultural Visual Grounding task.
Figures 4, 5, and 6 illustrate qualitative compar-
isons across three representative categories. The
visual grounding results reveal that models trained
on culturally rich datasets are better at pinpoint-
ing region-specific artifacts such as traditional gar-
ments or religious structures, whereas general-
purpose models often default to generic object de-
tection.

--- Page 12 ---

Task Type
SEA-LAVE Prompt
1.
Question-Answer
Evaluation
YOUR TASK: You are a cultural reasoning expert evaluating
how accurately a model answers a cultural question based on
Southeast Asian traditions.
Task: Assess the LLM’s answer to the cultural question based
on the following:
SCORING CRITERIA: 1. Answer Relevance (Binary: 0 or 1)
- Score 1 if the answer reflects the correct sub-culture or aligns
meaningfully with the question’s cultural theme. Score 0 if
unrelated. 2. Cultural Insight (Binary: 0 or 1) - Score 1 if the
answer reflects cultural knowledge, such as symbols, practices,
or traditions tied to the sub-culture. Score 0 if culturally generic
or inaccurate. 3. Country Attribution (0, 1, or 2) - 0: No
or incorrect country mentioned. - 1: Related country (e.g.,
another SEA country) but not the correct one. - 2: Correct
country is mentioned. 4. Justification (Text) - Briefly explain
the scores using specific elements from the answer. Note partial
correctness where relevant.
EXAMPLES AND OUTPUT FORMAT: Evaluate the follow-
ing: * Question: "question" * Answer: "llm response" * Cul-
ture: "culture" * Sub-Culture: "sub culture" * Country: "coun-
try"
Strictly output JSON:
2. True/False Statement
Evaluation
YOUR TASK: You are an expert verifying the cultural and
geographic correctness of a True/False statement and its expla-
nation provided by a language model.
Task: Analyze both the truth value and the explanation given
by the model for cultural accuracy and alignment with the
provided context.
IMPORTANT: Even though the answer is True or False, you
are scoring the explanation using the following criteria:
SCORING CRITERIA: 1. Text Understanding (Binary: 0 or
1) - Score 1 if the explanation reflects the correct sub-culture
or partially aligns with the cultural context. Score 0 if the
explanation is off-topic or unrelated. 2. Cultural Understanding
(Binary: 0 or 1) - Score 1 if the explanation includes any
relevant cultural detail (e.g., practices, attire, foods, rituals).
Score 0 if no relevant cultural context is present. 3. Country
Score (Ternary: 0, 1, or 2) - 0: The explanation mentions the
wrong or no country. - 1: The explanation mentions a related
SEA country, but not the correct one. - 2: The correct country
is mentioned, even if others are included. 4. Reasoning (Text) -
Briefly justify each score using evidence from the explanation.
Mention any partial correctness or mistakes.
EVALUATION CONTEXT: * Statement (True/False Claim):
"llm response" * Culture: "culture" * Sub-Culture: "sub cul-
ture" * Country: "country"
Strictly output your evaluation in JSON format.

--- Page 13 ---

Task Type
SEA-LAVE Prompt
3. Fill-in-the-Blank Eval-
uation
YOUR TASK: As a cultural language expert, you are assessing
the accuracy and appropriateness of a fill-in-the-blank comple-
tion about a cultural topic.
Task: Evaluate how well the model-filled phrase aligns with
the cultural setting, terminology, and country of origin.
SCORING RUBRIC: 1. Phrase Appropriateness (0 or 1) - 1
if the completion is contextually correct and refers to the sub-
culture. 0 if unrelated or inaccurate. 2. Cultural Relevance
(0 or 1) - 1 if the phrase embeds cultural knowledge (e.g.,
rituals, foods, symbols). 0 if generic or missing cultural details.
3. Geographic Accuracy (0 to 2) - 0: Incorrect country. -
1: Related SEA country. - 2: Correct country mentioned or
implied accurately. 4. Scoring Explanation (Text) - Describe in
2–3 sentences how the phrase reflects cultural and geographic
accuracy.
EVALUATION SETUP: * Prompt: "question with blank" *
LLM Response: "llm response" * Culture: "culture" * Sub-
Culture: "sub culture" * Country: "country"
Strictly return your evaluation in JSON format.
Table 5: Task-specific prompts used for cultural evaluation of model-generated responses under the SEA-LAVE
framework.
Figure 3: CulturalVQA results for cultural understanding of various models, global and SEA specific prompt.

--- Page 14 ---

Figure 4: Visual Grounding results (Part 1): Comparing model predictions on region-specific cultural entities.
Figure 5: Visual Grounding results (Part 2): Comparing model predictions on region-specific cultural entities..
Figure 6: Visual Grounding results (Part 3): Comparing model predictions on region-specific cultural entities.

```
