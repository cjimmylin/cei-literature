---
title: "2025-Tam-VisTW Benchmarking Vision-Language Models for Traditional Chinese in - PDF Extract"
source_pdf: "2025-Tam-VisTW Benchmarking Vision-Language Models for Traditional Chinese in.pdf"
pages: 25
extracted_at: "2026-02-15T17:54:28.518147"
---

# PDF Extract: 2025-Tam-VisTW Benchmarking Vision-Language Models for Traditional Chinese in

**Source PDF:** 2025-Tam-VisTW Benchmarking Vision-Language Models for Traditional Chinese in.pdf
**Total Pages:** 25

---

## Content

```
--- Page 1 ---

Preprint. Under review.
VisTW: Benchmarking Vision-Language Models for
Traditional Chinese in Taiwan
Zhi Rui Tam
Independent Researcher
Ya-Ting Pai∗
University of Illinois Urbana-Champaign
Yen-Wei Lee∗
Independent Researcher
Yun-Nung Chen
National Taiwan University
Abstract
In this paper, we propose a comprehensive evaluation benchmark for Vi-
sual Language Models (VLM) in Traditional Chinese. Our evaluation suite,
the first of its kind, contains two complementary components: (1) VisTW-
MCQ, a collection of manually curated exam multi-choice questions from 21
academic subjects designed to test the broad knowledge and reasoning ca-
pabilities of VLMs; and (2) VisTW-Dialogue, an open dialogue benchmark
comprising 131 image-question pairs manually created to evaluate VLMs’
ability in free-form dialogue generation within Taiwanese cultural contexts.
These benchmarks address a critical gap in the evaluation landscape, where
existing benchmarks predominantly focus on English or Simplified Chi-
nese, neglecting the unique linguistic and cultural aspects of Traditional
Chinese used in regions like Taiwan and Hong Kong. Our analysis reveals
significant performance differences across various VLMs and highlights
specific challenges in processing Traditional Chinese visual content. 1
1
Introduction
Vision-Language Models (VLMs) have achieved remarkable success in tasks such as image
captioning, visual question answering (VQA), and cross-modal retrieval (Chen et al., 2022;
Li et al., 2022; Faysse et al., 2024). However, current multimodal benchmarks predominantly
focus on English, and when extended to Chinese, they primarily employ Simplified Chinese
scripts common in mainland China (Das et al., 2024; Winata et al., 2024; Wang et al., 2024).
Traditional Chinese, widely used in Taiwan and Hong Kong, remains significantly under-
represented. Consequently, VLM capabilities in Traditional Chinese contexts are largely
untested and unknown.
Evaluating VLMs in Traditional Chinese presents unique challenges. Traditional Chinese
characters are more complex and often do not map directly to their Simplified counterparts,
causing potential inaccuracies when models trained on Simplified scripts encounter Tra-
ditional texts (Chen et al., 2024a). Moreover, images from regions like Taiwan frequently
incorporate culturally specific content and Traditional Chinese textual elements—such as
signs, labels, or documents—introducing further contextual challenges not typically ad-
dressed by Western-centric or Simplified-Chinese-oriented datasets. Figure 1 shows that
∗Equal contribution
1Our code and dataset can be found in https://github.com/TMMMU-Benchmark/evaluation
1
arXiv:2503.10427v2  [cs.CL]  15 Mar 2025

--- Page 2 ---

Preprint. Under review.
Figure 1: VisTW consists of two subsets: (1) MCQ - a collection of multiple-choice questions
from 21 academic subjects (answer choices omitted for space); and (2) Dialogue - real-life
images with corresponding questions requiring understanding of Traditional Chinese and
Taiwan-specific cultural context.
Thus, dedicated benchmarks capturing both linguistic complexity and cultural nuances are
essential for accurate evaluation.
Figure 1 shows examples from our benchmark that illustrate the distinct challenges VLMs
face when processing Taiwanese content. The left side demonstrates MCQ-style evaluations
including geographic information correlated to specific to Taiwan-specific identification.
The right side showcases dialogue scenarios requiring understanding of culturally-specific
contexts such as deciphering Traditional Chinese menus and utility meters. These examples
highlight content that cannot be adequately evaluated through simple character mapping
from Simplified to Traditional Chinese, as they incorporate Taiwan-specific terminology,
formats, and cultural knowledge.
1.1
Our Contributions
To fill this gap, we introduce two complementary benchmarks for evaluating VLMs in
Traditional Chinese and Taiwanese contexts:
VisTW-MCQ.
This benchmark centers on structured, exam-style questions, reflecting
high-level reasoning and subject-matter knowledge. Inspired by Taiwanese educational
assessments, VisTW-MCQ features images (e.g., diagrams, charts) coupled with questions
in Traditional Chinese. These questions often require interpretative or logical reasoning,
offering a rigorous test bed for multimodal models beyond simple image-description tasks.
VisTW-Dialogue.
In contrast, VisTW-Dialogue targets open-ended scenarios rooted in
everyday Taiwanese contexts. It includes image-question pairs on topics such as local
landmarks, cultural practices, and daily life scenes containing Traditional Chinese text
(e.g., street signs, menus). Rather than multiple-choice prompts, VisTW-Dialogue uses
free-form queries, requiring models to produce answers in Traditional Chinese and handle
unconstrained, real-world queries.
In summary, our contributions include:
1. The first comprehensive vision-language benchmark for Traditional Chinese, fea-
turing 3,795 test questions across 21 subjects (VisTW-MCQ) and 131 culturally-
grounded dialogue pairs (VisTW-Dialogue).
2. A validated, cost-effective VLM-as-judge evaluation framework with high human
correlation (ρ = 0.8466) and a calibration approach ensuring evaluation continuity
across model generations.
2

--- Page 3 ---

Preprint. Under review.
3. Empirical evidence revealing performance gaps between Simplified and Traditional
Chinese VLMs, with insights on model scaling efficiency and image resolution
sensitivity across 31 different models.
2
Related Work
2.1
English-based Multimodal Benchmarks
Vision-language benchmarks like ChartQA (Masry et al., 2022), TextVQA (Singh et al.,
2019), and DocVQA (Mathew et al., 2021) have advanced visual text understanding through
specialized tasks requiring OCR and reasoning. More recent exam-based evaluations such
as MMMU (Yue et al., 2024) test expert-level multimodal reasoning across 30 subjects,
pushing beyond surface-level image understanding to complex problem-solving. For open-
ended generation, benchmarks like Vibe-Eval (Padlewski et al., 2024) assess multimodal
chat models with 269 visually-grounded prompts. However, these benchmarks remain
English-centric with limited applicability to other languages and cultural contexts.
2.2
Traditional Chinese and Multilingual Benchmarks
For Traditional Chinese, recent benchmarks focus primarily on text-only evaluation.
TMMLU (Hsu et al., 2023) provides 3,300 multiple-choice questions from Taiwanese ex-
ams, while TMMLU+ (Tam et al., 2024) expands this to 22,690 questions across 66 subjects.
However, both lack multimodal components essential for vision-language evaluation. TMM-
Bench included in the release of Breeze2 (Hsu et al., 2025) is a multichoice traditional Chinese
vision question that covers topics related to Taiwan, such as Taiwanese attractions, daily
life, and Taiwan’s university entrance exams. However, as of this writing, the details and
TMMBench dataset have not been publicly released yet.
Multilingual efforts include JMMU (Onohara et al., 2024) for Japanese (though with only 30
questions per subjects) and CMMU (He et al., 2024) for Simplified Chinese (with limited
public access and insufficient cultural context). M3Exam (Zhang et al., 2023) covers 9
languages, including Simplified Chinese, but uses generic curricula without Traditional
Chinese script or Taiwan-specific content.
This review reveals a critical gap: There is no comprehensive benchmark for evaluating
vision-language models in Traditional Chinese that address both structured reasoning and
open-ended generation while incorporating culturally relevant Taiwanese contexts. Our
work on VisTW-MCQ and VisTW-Dialogue aims to address this specific need in the field.
3
VisTW-MCQ : Visual Multi-Choice Question Answering
The multi-choice question answering format is widely utilized to assess the knowledge and
reasoning capabilities of Large Language Models (LLMs). In this section, we introduce a
new visual multi-choice benchmark, VisTW-MCQ, composed of past examination questions
from various educational levels in Taiwan, ranging from primary and secondary education
to specialized undergraduate courses, such as veterinary medicine.
Our benchmark dataset was constructed using real-world exam papers collected from pub-
licly available sources spanning the years 2013 to 2024. We selected subjects specifically
requiring visual comprehension, such as medical diagnostics (e.g., interpreting X-ray and
ultrasound images), geometry, electronic circuit design, and chemistry. The curation pro-
cess involved manual extraction of questions and images from official exam archives and
online PDFs. Each pair of questions and images was independently reviewed by a second
annotator to verify content accuracy, clarity, and completeness, ensuring the absence of
contextual errors, missing information, or invalid answer choices. To maintain consistent
baseline guessing performance, the answer choices for each question were randomly shuf-
fled, ensuring a uniform probability (approximately 25%) of selecting the correct answer by
chance.
3

--- Page 4 ---

Preprint. Under review.
Dataset
Language
Subjects
Test
Validation
CMMU (He et al., 2024)
Simplified Chinese
7
1,803
1,800
MMMU (Yue et al., 2024)
English
28
1,320
900
ALM-Bench (Vayani et al., 2024)
Traditional Chinese
13
52
0
VisTW-MCQ
Traditional Chinese
21
3,795
869
Table 1: Comparison of VisTW-MCQ with other similar datasets, for ALM-Bench, we only
compare the subset for Traditional Chinese.
In total, VisTW-MCQ includes 21 distinct subjects covering diverse areas such as medical
diagnosis, nautical science with cartographic analysis, and technical disciplines. Each
subject contains a minimum of 100 test questions, along with 5 few-shot learning examples
as a development set, and 10 questions dedicated to validation purposes. For more details
on image resolutions and aspect ratio we include this in Appendix C.2. Table 1 compares
VisTW-MCQ with existing visual multi-choice benchmarks, such as CMMU (He et al., 2024),
JMMMU (Onohara et al., 2024), and ALM-Bench (Vayani et al., 2024). Our dataset stands
out due to its robustness and broader subject diversity.
3.1
Evaluation Method
To evaluate the visual reasoning capabilities of Vision-Language Models (VLMs) across
different subjects, we employ a zero-shot Chain-of-Thought prompting (Kojima et al., 2022).
Each VLM is instructed to provide reasoning steps followed by the final answer choice
explicitly. However, we observed that certain VLMs occasionally struggled to comply with
formatting instructions, resulting in invalid responses. To mitigate evaluation bias due to
parsing errors, we subsequently employed an auxiliary LLM parser ( gpt-4o-mini ) to extract
and validate the final answer choice from each VLM response. We report the average scores
for all 21 subjects as our final score.
However, one limitation of MCQA form of benchmark is that it does not reflect the real
world use of VLM which mostly in free form question answering format. Hence we’ll
address this limitation by introducing another benchmark dataset.
4
VisTW-Dialogue: Visual Free Form Dialogue Benchmark
In this section, we introduce a visual free-form generation benchmark designed to bridge
the gap between real-world user interactions and typical model evaluation procedures.
Specifically, our goal is design a dataset which reflects real user experiences when interacting
with VLMs in Traditional Chinese, where users naturally engage in open-ended dialogues
rather than structured question-answering formats.
We manually curated both images and the corresponding dialogue prompts based on
real-life scenarios encountered in Taiwan, such as interpreting metro rail maps or calcu-
lating shared bills from restaurant menus. Each image was intentionally captured by our
researchers to ensure that these image has never been seen during VLM training. The
researchers who took the photographs also tasked to write challenging questions related to
the images, specifically designed to test spatial reasoning skills and local cultural knowledge
unique to Taiwan.
To facilitate efficient data collection across diverse regions, we created a Discord server
integrated with a data collection bot. We chose Discord as our data collection platform for
several practical reasons: Participants already had Discord installed, it allowed direct photo
uploads from mobile devices, and its threaded conversation structure facilitated discussion.
Contributors, primarily existing Discord users, only needed to join the dedicated server
to participate. The custom bot we developed served multiple functions: It notified users
when data was received successfully, monitored emoji annotations for quality control,
and provided a testbed for experimenting with various rating prompts within submission
threads. Additional details of the labeling can be found in the Appendix B.
4

--- Page 5 ---

Preprint. Under review.
Following the initial submission, our quality control process involved multiple stages:
1. Answer Provision: The researcher who submitted the image was required to provide an
answer to their question within a newly created submission thread.
2. Peer Review: Other team members reviewed the provided answers, making corrections
or improvements when necessary.
3. Community Moderation: We implemented a simple but effective quality control mech-
anism using Discord’s emoji reactions. Members could flag inappropriate or unsuitable
submissions using downvotes, which were automatically recorded by our bot.
4. Filtering Process: Submissions that received more than two downvotes (typically from a
user and a moderator) were removed during the dataset cleaning phase.
The data collection phase spanned from July 2024 to February 2025, resulting in a dataset
comprising 131 unique image-question pairs with ground truth. The image resolutions and
aspect ratio of VisTW-Dialogue are included in Appendix C.3.
4.1
Automatic Evaluation : VLM as a Judge
To reduce the barrier of quick evaluations, we used a VLM as an automated judge to score
responses based on questions, images, and ground truth answers. Using LLMs to evaluate
free-form generation has become standard practice, exemplified by benchmarks such as
AlpacaEval (Li et al., 2023) and MT-Bench (Zheng et al., 2023).
Inspired by Vibe-Eval (Padlewski et al., 2024), we crafted an evaluation prompt that explicitly
includes scoring criteria, the original question, the assistant’s response, the ground truth
and optionally, the image itself. The LLM judge is instructed to first provide a detailed
explanation followed by the final numerical score from 0 to 10, the detail breakdown of
score criteria can be found in Appendix E.1.
To validate the reliability of LLM-generated scores, we conducted human evaluations across
four selected models (gpt-4o, claude-3-5-sonnet, gpt-4o-mini, claude-3-7-sonnet). Each
response was independently scored by three human annotators, and the average rating was
caculated to establish a human evaluation baseline. We evaluated several prominent VLMs
including gemini-2.0-pro, gemini-2.0-flash, Qwen 2.5 VL 72B, claude-sonnet-3-5-20241022,
gpt-4o-2024-08-06, LLaMA Vision 90B, and Qwen VL 72B. Table 2 reports the Spearman
correlations between LLM-generated scores and human evaluations.
Our analysis revealed that incorporating images in the evaluation prompts generally
improved model-human score correlations, contradicting earlier findings by Padlewski
et al. (2024), which indicated minimal improvements from multimodal judging. Notably,
the gemini-2.0-flash-001 model achieved performance comparable to claude-3-5-sonnet-
20241022, despite being approximately 36 times less costly. When we averaged the scores
from all VLM judges into an ensemble approach, we found it exhibited the strongest correla-
tion with human scores, reaching 0.8466 without images and 0.8463 with images, suggesting
that combining diverse model judgments provides more robust evaluation than any single
model alone.
All reported correlations were statistically significant with p < 0.001. The strongest correla-
tion was observed with claude-3-5-sonnet-20241022 (ρ = 0.8336, p < 0.001) when images
were included. Given these results and future cost considerations, we selected gemini-2.0-
flash-001 as our primary LLM judge. The complete evaluation of the performance of one
model on VisTW-Dialogue cost merely $0.05 USD when using gemini-2.0-flash-001 as the
automated judge.
Additionally, we found no significant correlation between response length and automated
judge scores with a Spearman’s ρ = 0.26789, p < 0.001, indicating that our evaluation
framework does not exhibit substantial length bias. Our human annotated data are available
public for calibrate newer VLMs against human preference. Additional details can be found
in Appendix E.1.
5

--- Page 6 ---

Preprint. Under review.
VLM Judge
With Image
Without Image
claude-3-5-sonnet-20241022
0.8336
0.8282
gemini-2.0-flash-001
0.8241
0.8194
gpt-4o-2024-08-06
0.7985
0.8277
gemini-2.0-pro-exp-02-05
0.8196
0.8320
qwen2.5-vl-72b-instruct
0.7501
0.7341
gpt-4o-mini-2024-07-18
0.7349
0.7360
Ensemble all models
0.8463
0.8466
Table 2: Spearman correlations between human-assigned scores and scores generated by
different VLMs serving as automated judges. With Image indicates that the evaluation
prompt included the associated image as additional context, whereas Without Image denotes
that only the textual question and ground-truth answer were provided to the judging model.
Higher correlations indicate better alignment with human judgment.
5
Benchmark Results
We evaluated X vision-language models (VLMs) spanning both closed and open-weight cat-
egories as presented in Table 3. Detailed model specifications are provided in Appendix D.
Our analysis reveals strong correlation between VisTW-Dialogue and VisTW-MCQ perfor-
mance metrics (Spearman’s ρ = 0.7746, p < 0.001; Kendall’s τ = 0.6086, p < 0.001).
The two Traditional Chinese VLMs in our evaluation, Breeze2-3B and Breeze2-8B, demon-
strate inferior performance compared to Simplified Chinese counterparts of similar parame-
ter scales, such as InternVL2.5-4B and InternVL2-8B variants. An intriguing observation
emerges with Gemini-2.0-flash-thinking, which achieves exceptionally high scores in VisTW-
Dialogue (6.51) but relatively modest performance in VisTW-MCQ (0.376). Conversely,
deepseek-ai-deepseek-vl2-small scores 0.318 in VisTW-MCQ while nearly failing in VisTW-
Dialogue. Upon manual validation, we discovered this model predominantly outputs
bounding boxes for object detection tasks while neglecting other user requirements in
VisTW-Dialogue. Interestingly, its smaller counterpart (tiny version) manages to partially
address VisTW-Dialogue questions, suggesting potential training anomalies in the small
variant.
Examining the performance of smaller VLMs reveals interesting efficiency-capability trade-
offs. Models with fewer parameters (≤4B) show consistent degradation in VisTW-Dialogue
scores, with OpenGVLab-InternVL2-1B scoring just 2.13 compared to its 8B counterpart’s
3.45.
However, this performance gap narrows considerably for VisTW-MCQ, where
InternVL2-1B achieves 0.2689 versus InternVL2-8B’s 0.3431—only a 21.6% reduction despite
using 87.5% fewer parameters. This suggests smaller models maintain reasonable factual
reasoning capabilities while struggling more with open-ended, multimodal tasks. Notably,
the InternVL2 series demonstrates graceful performance scaling, with consistent improve-
ments as parameter count increases from 1B to 8B in both metrics, making them promising
candidates for resource-constrained applications.
6
Analysis
6.1
Sensitivity of Image Resolution
We studied how image resolution affects model performance through systematic experi-
ments. For VisTW-MCQ, we tested both directions: upscaling to 2× and 4× the original
resolution using the state-of-the-art SwinIR model (Liang et al., 2021), as well as downscal-
ing to 1/2, 1/4, and 1/8 of the original size. For VisTW-Dialogue, due to the initially large
image sizes in this dataset, we only conducted downscaling experiments at the scales 1/2,
1/4, and 1/8.
6

--- Page 7 ---

Preprint. Under review.
Model
VisTW-Dialogue
VisTW-MCQ
Avg
Score 0-10
Rank
Accuracy
Rank
Rank
gemini-2.0-pro-exp-02-05
6.72
1
0.6619
1
1.0
gemini-2.0-flash-001
6.15
3
0.6596
2
2.5
gpt-4o-2024-11-20
6.12
4
0.5755
4
4.0
claude-3-5-sonnet-20241022
5.96
6
0.6019
3
4.5
gemini-2.0-flash-lite-preview-02-05
5.92
7
0.4992
6
6.5
Qwen2.5-VL-72B-instruct
4.87
9
0.5413
5
7.0
gemini-2.0-flash-thinking-exp-1219
6.51
2
0.3764
14
8.0
gemini-1.5-pro
5.05
8
0.4417
8
8.0
gpt-4o-2024-08-06
5.98
5
0.4000
12
8.5
Qwen2-VL-72B-instruct
4.21
13
0.4701
7
10.0
gpt-4o-mini-2024-07-18
4.74
10
0.4091
11
10.5
gemini-1.5-flash
4.26
12
0.3943
13
12.5
gemma3-27b-it
3.94
16
0.4375
9
12.5
Qwen2.5-VL-7B-Instruct
4.54
11
0.3592
15
13.0
Llama-3.2-90B-Vision-Instruct
3.44
22
0.4119
10
16.0
InternVL2.5-8B
3.90
17
0.3447
17
17.0
gemini-1.5-flash-8B
4.18
15
0.3280
22
18.5
claude-3-haiku-20240307
3.70
18
0.3291
20
19.0
InternVL2-8B
3.45
21
0.3431
18
19.5
Qwen2-VL-7B-Instruct
4.21
13
0.3004
26
19.5
InternVL2.5-4B
3.60
20
0.3291
21
20.5
nova-lite-v1
3.26
23
0.3376
19
21.0
Llama-3.2-11B-Vision-Instruct
2.58
27
0.3262
23
25.0
Breeze2-8B-Instruct
3.14
24
0.2915
28
26.0
Breeze2-3B-Instruct
2.90
26
0.2971
27
26.5
InternVL2-4B
2.31
28
0.3081
25
26.5
deepseek-vl2-small
0.51
31
0.3181
24
27.5
CogVLM2-llama3-chinese-chat
2.96
25
0.2777
31
28.0
InternVL2-2B
2.22
29
0.2891
29
29.0
deepseek-vl2-tiny
2.01
30
0.2781
30
30.0
Table 3: For VisTW-MCQ we prompt our model in zero shot chain of thought fashion and
report the average score from all 23 subjects. Models are sorted by average rank from both
subsets.
Figure 2 illustrates our findings on resolution sensitivity. For VisTW-MCQ, performance
remained consistent across resolution variations, suggesting that even lower resolutions
contained sufficient information for multiple-choice tasks. In contrast, for VisTW-Dialogue,
model performance stabilized at approximately half the original resolution. We observed
model-specific variations: gemini-2.0-flash-lite showed slight improvements with increased
resolution, while gemini-1.5-flash-8B exhibited minor performance declines, indicating
different architectural sensitivities to input resolution.
6.2
Comparison between With and Without Vision Cues
In the previous section, we showed score degradation with reduced image resolution. Here,
we examine performance when image context is entirely omitted. For MCQ tasks, this analy-
sis establishes a baseline that measures how much linguistic knowledge alone contributes to
task performance before visual information becomes beneficial. Similarly, for dialogue tasks,
images-free score serve as baseline measurements, indicating how significantly performance
drops when visual context is absent. We conducted this experiment using the same models
evaluated in the previous section. Table 4 presents the results, which show consistent score
reductions across all four models in both datasets when images are withheld. The perfor-
7

--- Page 8 ---

Preprint. Under review.
0.125
0.25
0.5
1.0
2.0
4.0
Scale
0
10
20
30
40
50
60
70
Accuracy (%)
VisTW-MCQ
gemini-2.0-flash-lite-preview-02-05
meta-llama-Llama-3.2-11B-Vision-Instruct-Turbo
gemini-1.5-flash-8b
gpt-4o-mini-2024-07-18
OpenGVLab-InternVL2_5-4B
0.125
0.25
0.5
1.0
Scale
0
1
2
3
4
5
6
Score (0-10)
VisTW-Dialogue
gemini-2.0-flash-lite-preview-02-05
meta-llama-Llama-3.2-11B-Vision-Instruct-Turbo
gemini-1.5-flash-8b
gpt-4o-mini-2024-07-18
OpenGVLab-InternVL2_5-4B
Figure 2: Effect of image resolution scaling on model performance. Left: Performance on
VisTW-MCQ with both upscaled (2×, 4×) and downscaled (1/2, 1/4, 1/8) images. Right:
Performance on VisTW-Dialogue with downscaled images.
Model
VisTW-MCQ
VisTW-Dialogue
w/ img
w/o img
w/ img
w/o img
gemini-2.0-flash-lite-preview-02-05
0.50
0.32
5.92
2.35
gpt-4o-mini-2024-07-18
0.41
0.33
4.74
1.95
gemini-1.5-flash-8b
0.33
0.26
4.18
1.85
OpenGVLab-InternVL2 5-4B
0.33
0.29
3.60
1.29
Table 4: Performance comparison of various multimodal models across different evaluation
tasks. MCQ scores represent accuracy, while dialogue scores represent quality ratings.
Higher scores indicate better performance.
mance degradation is expected, as it indicates that VLMs struggle when visual information
is not provided.
6.3
Correlations with Other Benchmarks
As shown in Figure 3, we compare our VisTW-MCQ results with exam style benchmarks:
MMMU (Yue et al., 2024) and CMMU (He et al., 2024) on a selected set of models spanning
different scales. Despite the relatively small subset (due to computational and financial
constraints), we observe a broadly consistent trend: models that perform well on MMMU
or CMMU also tend to score higher on VisTW-MCQ. However, we also note that some
points deviate from the main diagonal, suggesting that the three benchmarks are not fully
interchangeable. The models show stronger relative performance on MMMU and CMMMU
compare to VisTW-MCQ scores.
6.4
Contingency Plan When the Gemini-2.0-Flash Is Retired
Due to our choice of using a close weight VLM : Gemini 2.0 Flash as our judge; this means it
will eventually become unavailable when newer versions become available. Consequently,
scores assigned by a retired model, such as gemini-2.0-flash will become difficult to compare
with those of the newer VLMs. Many LLM-as-judge works overlook this scenario, typically
re-running an entire benchmark using the new model as judge. However, large-scale
evaluations make such an approach infeasible.
To address this, we propose a calibration-based contingency plan using Qwen2.5-VL 72B, the
highest performing VLM in Table 3. Figure 4 (left) shows that the raw scores for Qwen2.5-
VL are systematically higher than those from gemini-2.0-flash. We therefore fit a linear
mapping (based on five-vote distributions) to align Qwen2.5-VL scores with gemini-2.0-
flash. After calibration, instances that gemini-2.0-flash scores as zero now cluster near zero
under Qwen2.5-VL, however the number of perfect scores is reduced (Figure 4, right). After
8

--- Page 9 ---

Preprint. Under review.
0.2
0.3
0.4
0.5
0.6
0.7
0.8
VisTW-MCQ
0.2
0.3
0.4
0.5
0.6
0.7
0.8
MMMU
Pearson r=0.96
VisTW-MCQ vs MMMU
0.2
0.3
0.4
0.5
0.6
0.7
0.8
VisTW-MCQ
0.2
0.3
0.4
0.5
0.6
0.7
0.8
CMMU
Pearson r=0.92
VisTW-MCQ vs CMMU
Breeze2-3B-Instruct
Breeze2-8B-Instruct
Qwen-2.5-VL-7B-Instruct
Claude-3-Haiku
Gemini-1.5-flash
Gemini-1.5-flash-8B
Gemini-2.0-flash
Gemini-2.0-flash-lite
Gemini-2.0-pro
GPT-4o-mini
LLama-3.2-11B-Vision
Qwen-2.5-VL-72B-Instruct
Figure 3: Comparison of VisTW-MCQ scores with MMMU (left) and CMMU (right) on
a selected subset of models of varying scales. We observe a rough correlation across the
three benchmarks, though some deviations suggest differences in the specific knowledge or
reasoning skills each test emphasizes.
0
1
2
3
4
5
6
7
8
9
10
Qwen2.5 VL 72B
0
1
2
3
4
5
6
7
8
9
10
Gemini 2.0 flash
92
93
89
70
41
10
10
3
1
0
0
8
14
27
30
34
9
6
0
0
0
0
0
7
22
30
31
29
18
4
0
1
0
0
1
8
15
33
25
19
2
1
1
0
1
0
6
10
27
30
18
7
4
1
0
0
0
3
5
15
27
55
19
2
0
0
0
0
1
2
13
20
77
37
6
2
1
0
1
1
1
3
7
36
48
29
3
0
0
0
1
1
1
0
15
30
39
18
1
0
0
0
0
1
1
0
13
25
16
7
1
1
0
0
0
0
0
2
6
37
79
0
1
2
3
4
5
6
7
8
9
10
Qwen2.5 VL 72B after calibration
0
1
2
3
4
5
6
7
8
9
10
Gemini 2.0 flash
223
101
44
21
10
4
4
1
1
0
0
31
35
36
13
12
1
0
0
0
0
0
14
27
41
20
25
9
4
1
1
0
0
1
15
30
20
27
6
3
2
1
0
0
3
9
17
31
22
7
9
2
3
1
0
0
4
8
19
39
32
15
9
0
0
0
0
2
6
14
39
38
38
18
2
2
0
2
0
2
4
10
27
30
42
9
3
0
0
2
0
1
1
9
21
38
18
16
0
0
0
0
1
1
0
6
16
18
21
0
2
0
0
0
0
0
0
3
11
110
0
0
20
40
60
80
0
25
50
75
100
125
150
175
200
Figure 4: Comparison of Gemini 2.0 flash and Qwen 2.5 VL 72B score distribution rounded
to the nearest integer (left) and Qwen 2.5 VL 72B scores after calibrated against Gemini 2.0
flash (right).
calibration, the spearman correlation with human score and ensemble of Qwen2.5-VL scores
improve from 0.7993 to 0.8070.
Table 5 compares raw vs. calibrated Qwen2.5-VL scores to gemini-2.0-flash on VisTW-
Dialogue, demonstrating how calibration improves alignment. This result offers a practical
strategy to maintain continuity of evaluation even if the original judge model is no longer
available.
6.5
Direct Answer vs CoT in VisTW-MCQ
To analyze the impact of reasoning on performance, we compare two prompting strategies:
Zero-Shot Chain of Thought (CoT) and Direct Answer prompting. The latter asks models to
provide answers without intermediate reasoning steps. Table 6 presents the comparative
results.
Interestingly, CoT does not universally benefit all vision-language models (VLMs). The
performance gain from reasoning is predominantly observed in models that already demon-
strate strong direct answer capabilities. For instance, Gemini-2.0-Flash-001, despite being
smaller than Gemini-2.0-Pro (as evidenced by its lower direct answer performance), exhibits
a substantially larger improvement margin (13.9%) when employing reasoning steps.
9

--- Page 10 ---

Preprint. Under review.
Model
Gemini
Qwen
Qwen (calibrated)
∆(Cal - Gem)
gemini-2.0-flash-001
6.15
6.65
5.73
-0.42
qwen2.5-vl-72b-instruct
4.87
6.18
5.12
+0.25
Llama-Breeze2-8B-Instruct
3.14
4.12
3.16
+0.02
Llama-Breeze2-3B-Instruct
2.90
4.07
3.06
+0.16
Table 5: Comparison of scores assigned by different judge models (Gemini, Qwen, and
calibrated Qwen) across various evaluated models. The ∆column shows the difference
between calibrated Qwen VL scores and Gemini scores, highlighting the effectiveness of the
calibration. Values close to zero indicate better alignment.
Our analysis reveals that high-performing models generally gain 2-10% improvement
through CoT prompting. Conversely, lower-performing VLMs show degraded performance
with CoT, as evidenced by the negative differences in the lower portions of Table 6. We
hypothesize that inferior vision processing capabilities in these models may introduce hallu-
cinations when given extended reasoning space, ultimately diminishing their performance.
Model Name
CoT
Direct Answer
Difference
gemini-2.0-flash-001
0.660
0.521
0.139
gemini-2.0-pro-exp-02-05
0.662
0.569
0.093
gpt-4o-2024-11-20
0.576
0.486
0.090
claude-3-5-sonnet-20241022
0.602
0.519
0.083
qwen2.5-vl-72b-instruct
0.502
0.433
0.069
gpt-4o-mini-2024-07-18
0.409
0.350
0.059
Llama-Breeze2-3B-Instruct
0.297
0.267
0.030
gemini-1.5-flash
0.394
0.371
0.023
gemini-1.5-pro
0.442
0.420
0.022
gemini-1.5-flash-8b
0.328
0.309
0.019
deepseek-ai-deepseek-vl2-tiny
0.278
0.259
0.019
OpenGVLab-InternVL2-8B-MPO
0.353
0.338
0.015
Qwen-Qwen2-VL-7B-Instruct
0.300
0.287
0.013
Qwen2.5-VL-7B-Instruct
0.359
0.346
0.013
Llama-3.2-90B-Vision-Instruct-Turbo
0.412
0.404
0.008
THUDM-cogvlm2-19B
0.278
0.277
0.001
claude-3-haiku-20240307
0.329
0.330
-0.001
OpenGVLab-InternVL2-8B
0.343
0.347
-0.004
OpenGVLab-InternVL2-2B
0.289
0.294
-0.005
OpenGVLab-InternVL2 5-8B
0.345
0.352
-0.007
OpenGVLab-InternVL2-4B
0.308
0.315
-0.007
Llama-Breeze2-8B-Instruct
0.292
0.299
-0.007
Llama-3.2-11B-Vision-Instruct
0.326
0.335
-0.009
deepseek-ai-deepseek-vl2-small
0.318
0.327
-0.009
OpenGVLab-InternVL2-1B
0.269
0.282
-0.013
OpenGVLab-InternVL2 5-4B
0.329
0.345
-0.016
Table 6: Model Performance Comparison: CoT vs Direct Answer (Sorted by Difference)
7
Conclusion
In this work, we introduce VisTW-MCQ and VisTW-Dialogue, the first comprehensive
benchmarks for evaluating Vision-Language Models in Traditional Chinese. Our prelimi-
nary results reveal that VLMs specifically trained on Traditional Chinese still significantly
underperform compared to their Simplified Chinese counterparts when processing visual
content in Traditional Chinese contexts. Our results show a strong correlation between
structured and free-form task performance suggests consistent capabilities across different
10

--- Page 11 ---

Preprint. Under review.
evaluation formats while measuring different aspects of VLMs. Moreover, our analysis on
factors such as image resolution and model scaling provides valuable insights into the prac-
tical deployment of these models. Future work should focus on improving the performance
of the model on traditional Chinese content and expanding the benchmark to include a
more diverse cultural context in Taiwan.
Ethics Statement
All images in VisTai-Dialogue were collected by our researchers specifically for this bench-
mark, with contributors explicitly waiving ownership rights and consenting to public use
of their images. We implemented strict guidelines to ensure no personally identifiable
information (PII) was included—images containing names, faces of non-public figures,
Wi-Fi passwords, or residential addresses were prohibited and filtered through community
moderation. For VisTai-MCQ, we used only publicly available exam questions from official
sources spanning 2013-2024, maintaining academic integrity while respecting intellectual
property.
Our work directly addresses the underrepresentation of Traditional Chinese in vision-
language benchmarks, promoting greater linguistic and cultural inclusivity in AI evaluation.
By creating resources specifically for Traditional Chinese, we help ensure that NLP ad-
vancements benefit communities beyond those using dominant languages like English or
Simplified Chinese. Our benchmark incorporates diverse geographical sampling across
Taiwan through contributions from nine individuals in different regions, though we ac-
knowledge a concentration of samples from Taipei.
References
Anthropic. The claude 3 model family: Opus, sonnet, haiku. https://www-cdn.anthropic.
com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model Card Claude 3.pdf, 2024a.
Anthropic.
Claude 3.5 sonnet model card addendum.
https://www-cdn.anthropic.
com/fed9cc193a14b84131812372d8d5857f8f304c52/Model Card Claude 3 Addendum.pdf,
2024b.
Jinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan Tan, Peng Wang, Junyang Lin, Chang
Zhou, and Jingren Zhou. Qwen-vl: A versatile vision-language model for understanding,
localization, text reading, and beyond, 2023. URL https://arxiv.org/abs/2308.12966.
Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, Sibo Song, Kai Dang, Peng
Wang, Shijie Wang, Jun Tang, Humen Zhong, Yuanzhi Zhu, Mingkun Yang, Zhaohai
Li, Jianqiang Wan, Pengfei Wang, Wei Ding, Zheren Fu, Yiheng Xu, Jiabo Ye, Xi Zhang,
Tianbao Xie, Zesen Cheng, Hang Zhang, Zhibo Yang, Haiyang Xu, and Junyang Lin.
Qwen2.5-vl technical report, 2025. URL https://arxiv.org/abs/2502.13923.
Kaibing Chen, Dong Shen, Hanwen Zhong, Huasong Zhong, Kui Xia, Di Xu, Wei Yuan,
Yifei Hu, Bin Wen, Tianke Zhang, et al. Evlm: An efficient vision-language model for
visual understanding. arXiv preprint arXiv:2407.14177, 2024a.
Xi Chen, Xiao Wang, Soravit Changpinyo, AJ Piergiovanni, Piotr Padlewski, Daniel Salz,
Sebastian Goodman, Adam Grycner, Basil Mustafa, Lucas Beyer, et al. Pali: A jointly-
scaled multilingual language-image model. arXiv preprint arXiv:2209.06794, 2022.
Zhe Chen, Weiyun Wang, Hao Tian, Shenglong Ye, Zhangwei Gao, Erfei Cui, Wenwen Tong,
Kongzhi Hu, Jiapeng Luo, Zheng Ma, Ji Ma, Jiaqi Wang, Xiaoyi Dong, Hang Yan, Hewei
Guo, Conghui He, Botian Shi, Zhenjiang Jin, Chao Xu, Bin Wang, Xingjian Wei, Wei Li,
Wenjian Zhang, Bo Zhang, Pinlong Cai, Licheng Wen, Xiangchao Yan, Min Dou, Lewei
Lu, Xizhou Zhu, Tong Lu, Dahua Lin, Yu Qiao, Jifeng Dai, and Wenhai Wang. How far
are we to gpt-4v? closing the gap to commercial multimodal models with open-source
suites, 2024b. URL https://arxiv.org/abs/2404.16821.
11

--- Page 12 ---

Preprint. Under review.
Zhe Chen, Weiyun Wang, Yue Cao, Yangzhou Liu, Zhangwei Gao, Erfei Cui, Jinguo Zhu,
Shenglong Ye, Hao Tian, Zhaoyang Liu, Lixin Gu, Xuehui Wang, Qingyun Li, Yimin
Ren, Zixuan Chen, Jiapeng Luo, Jiahao Wang, Tan Jiang, Bo Wang, Conghui He, Botian
Shi, Xingcheng Zhang, Han Lv, Yi Wang, Wenqi Shao, Pei Chu, Zhongying Tu, Tong He,
Zhiyong Wu, Huipeng Deng, Jiaye Ge, Kai Chen, Kaipeng Zhang, Limin Wang, Min
Dou, Lewei Lu, Xizhou Zhu, Tong Lu, Dahua Lin, Yu Qiao, Jifeng Dai, and Wenhai Wang.
Expanding performance boundaries of open-source multimodal models with model, data,
and test-time scaling, 2025. URL https://arxiv.org/abs/2412.05271.
Rocktim Das, Simeon Hristov, Haonan Li, Dimitar Dimitrov, Ivan Koychev, and Preslav
Nakov. Exams-v: A multi-discipline multilingual multimodal exam benchmark for
evaluating vision language models. In Proceedings of the 62nd Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers), pp. 7768–7791, 2024.
Manuel Faysse, Hugues Sibille, Tony Wu, Bilel Omrani, Gautier Viaud, C´eline Hudelot, and
Pierre Colombo. Colpali: Efficient document retrieval with vision language models. In
The Thirteenth International Conference on Learning Representations, 2024.
Google DeepMind Gemma Team. Gemma 3 technical report. 2025.
Zheqi He, Xinya Wu, Pengfei Zhou, Richeng Xuan, Guang Liu, Xi Yang, Qiannan Zhu,
and Hua Huang. Cmmu: A benchmark for chinese multi-modal multi-type question
understanding and reasoning. arXiv preprint arXiv:2401.14011, 2024.
Wenyi Hong, Weihan Wang, Ming Ding, Wenmeng Yu, Qingsong Lv, Yan Wang, Yean Cheng,
Shiyu Huang, Junhui Ji, Zhao Xue, Lei Zhao, Zhuoyi Yang, Xiaotao Gu, Xiaohan Zhang,
Guanyu Feng, Da Yin, Zihan Wang, Ji Qi, Xixuan Song, Peng Zhang, Debing Liu, Bin Xu,
Juanzi Li, Yuxiao Dong, and Jie Tang. Cogvlm2: Visual language models for image and
video understanding, 2024. URL https://arxiv.org/abs/2408.16500.
Chan-Jan Hsu, Chang-Le Liu, Feng-Ting Liao, Po-Chun Hsu, Yi-Chang Chen, and Da-shan
Shiu. Advancing the evaluation of traditional chinese language models: Towards a
comprehensive benchmark suite. arXiv preprint arXiv:2309.08448, 2023.
Chan-Jan Hsu, Chia-Sheng Liu, Meng-Hsi Chen, Muxi Chen, Po-Chun Hsu, Yi-Chang Chen,
and Da-Shan Shiu. The breeze 2 herd of models: Traditional chinese llms based on llama
with vision-aware and function-calling capabilities. arXiv preprint arXiv:2501.13921, 2025.
Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa.
Large language models are zero-shot reasoners. Advances in neural information processing
systems, 35:22199–22213, 2022.
Junnan Li, Dongxu Li, Caiming Xiong, and Steven Hoi. Blip: Bootstrapping language-image
pre-training for unified vision-language understanding and generation. In International
conference on machine learning, pp. 12888–12900. PMLR, 2022.
Xuechen Li, Tianyi Zhang, Yann Dubois, Rohan Taori, Ishaan Gulrajani, Carlos Guestrin,
Percy Liang, and Tatsunori B. Hashimoto.
Alpacaeval: An automatic evaluator of
instruction-following models. https://github.com/tatsu-lab/alpaca eval, 5 2023.
Jingyun Liang, Jiezhang Cao, Guolei Sun, Kai Zhang, Luc Van Gool, and Radu Timofte.
Swinir: Image restoration using swin transformer. In Proceedings of the IEEE/CVF interna-
tional conference on computer vision, pp. 1833–1844, 2021.
Ahmed Masry, Do Xuan Long, Jia Qing Tan, Shafiq Joty, and Enamul Hoque. Chartqa: A
benchmark for question answering about charts with visual and logical reasoning. arXiv
preprint arXiv:2203.10244, 2022.
Minesh Mathew, Dimosthenis Karatzas, and CV Jawahar. Docvqa: A dataset for vqa
on document images. In Proceedings of the IEEE/CVF winter conference on applications of
computer vision, pp. 2200–2209, 2021.
12

--- Page 13 ---

Preprint. Under review.
Shota Onohara, Atsuyuki Miyai, Yuki Imajuku, Kazuki Egashira, Jeonghun Baek, Xiang Yue,
Graham Neubig, and Kiyoharu Aizawa. Jmmmu: A japanese massive multi-discipline
multimodal understanding benchmark for culture-aware evaluation.
arXiv preprint
arXiv:2410.17250, 2024.
OpenAI. Gpt-4o system card, 2024. URL https://arxiv.org/abs/2410.21276.
Piotr Padlewski, Max Bain, Matthew Henderson, Zhongkai Zhu, Nishant Relan, Hai Pham,
Donovan Ong, Kaloyan Aleksiev, Aitor Ormazabal, Samuel Phua, et al. Vibe-eval: A hard
evaluation suite for measuring progress of multimodal language models. arXiv preprint
arXiv:2405.02287, 2024.
David Patterson, Joseph Gonzalez, Urs H¨olzle, Quoc Le, Chen Liang, Lluis-Miquel Munguia,
Daniel Rothchild, David So, Maud Texier, and Jeff Dean. The carbon footprint of machine
learning training will plateau, then shrink, 2022. URL https://arxiv.org/abs/2204.
05149.
MediaTek Research, :, Chan-Jan Hsu, Chia-Sheng Liu, Meng-Hsi Chen, Muxi Chen, Po-
Chun Hsu, Yi-Chang Chen, and Da-Shan Shiu. The breeze 2 herd of models: Traditional
chinese llms based on llama with vision-aware and function-calling capabilities, 2025.
URL https://arxiv.org/abs/2501.13921.
Amanpreet Singh, Vivek Natarjan, Meet Shah, Yu Jiang, Xinlei Chen, Devi Parikh, and
Marcus Rohrbach. Towards vqa models that can read. In Proceedings of the IEEE Conference
on Computer Vision and Pattern Recognition, pp. 8317–8326, 2019.
Zhi Rui Tam, Ya Ting Pai, Yen-Wei Lee, Hong-Han Shuai, Jun-Da Chen, Wei Min Chu, and
Sega Cheng. Tmmlu+: An improved traditional chinese evaluation suite for foundation
models. In First Conference on Language Modeling, 2024.
Gemini Team. Gemini 1.5: Unlocking multimodal understanding across millions of tokens
of context, 2024. URL https://arxiv.org/abs/2403.05530.
Ashmal Vayani, Dinura Dissanayake, Hasindri Watawana, Noor Ahsan, Nevasini Sasiku-
mar, Omkar Thawakar, Henok Biadglign Ademtew, Yahya Hmaiti, Amandeep Kumar,
Kartik Kuckreja, Mykola Maslych, Wafa Al Ghallabi, Mihail Mihaylov, Chao Qin, Abdel-
rahman M Shaker, Mike Zhang, Mahardika Krisna Ihsani, Amiel Esplana, Monil Gokani,
Shachar Mirkin, Harsh Singh, Ashay Srivastava, Endre Hamerlik, Fathinah Asma Izzati,
Fadillah Adamsyah Maani, Sebastian Cavada, Jenny Chim, Rohit Gupta, Sanjay Manju-
nath, Kamila Zhumakhanova, Feno Heriniaina Rabevohitra, Azril Amirudin, Muhammad
Ridzuan, Daniya Kareem, Ketan More, Kunyang Li, Pramesh Shakya, Muhammad Saad,
Amirpouya Ghasemaghaei, Amirbek Djanibekov, Dilshod Azizov, Branislava Jankovic,
Naman Bhatia, Alvaro Cabrera, Johan Obando-Ceron, Olympiah Otieno, Fabian Farestam,
Muztoba Rabbani, Sanoojan Baliah, Santosh Sanjeev, Abduragim Shtanchaev, Maheen
Fatima, Thao Nguyen, Amrin Kareem, Toluwani Aremu, Nathan Xavier, Amit Bhatkal,
Hawau Toyin, Aman Chadha, Hisham Cholakkal, Rao Muhammad Anwer, Michael Fels-
berg, Jorma Laaksonen, Thamar Solorio, Monojit Choudhury, Ivan Laptev, Mubarak Shah,
Salman Khan, and Fahad Khan. All languages matter: Evaluating lmms on culturally
diverse 100 languages, 2024. URL https://arxiv.org/abs/2411.16508.
Yuxuan Wang, Yijun Liu, Fei Yu, Chen Huang, Kexin Li, Zhiguo Wan, and Wanxiang Che.
Cvlue: A new benchmark dataset for chinese vision-language understanding evaluation.
arXiv preprint arXiv:2407.01081, 2024.
Genta Indra Winata, Frederikus Hudi, Patrick Amadeus Irawan, David Anugraha,
Rifki Afina Putri, Yutong Wang, Adam Nohejl, Ubaidillah Ariq Prathama, Nedjma
Ousidhoum, Afifa Amriani, et al. Worldcuisines: A massive-scale benchmark for mul-
tilingual and multicultural visual question answering on global cuisines. arXiv preprint
arXiv:2410.12705, 2024.
Zhiyu Wu, Xiaokang Chen, Zizheng Pan, Xingchao Liu, Wen Liu, Damai Dai, Huazuo Gao,
Yiyang Ma, Chengyue Wu, Bingxuan Wang, Zhenda Xie, Yu Wu, Kai Hu, Jiawei Wang,
13

--- Page 14 ---

Preprint. Under review.
Yaofeng Sun, Yukun Li, Yishi Piao, Kang Guan, Aixin Liu, Xin Xie, Yuxiang You, Kai Dong,
Xingkai Yu, Haowei Zhang, Liang Zhao, Yisong Wang, and Chong Ruan. Deepseek-vl2:
Mixture-of-experts vision-language models for advanced multimodal understanding,
2024. URL https://arxiv.org/abs/2412.10302.
Xiang Yue, Yuansheng Ni, Kai Zhang, Tianyu Zheng, Ruoqi Liu, Ge Zhang, Samuel Stevens,
Dongfu Jiang, Weiming Ren, Yuxuan Sun, et al. Mmmu: A massive multi-discipline
multimodal understanding and reasoning benchmark for expert agi. In Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 9556–9567, 2024.
Wenxuan Zhang, Mahani Aljunied, Chang Gao, Yew Ken Chia, and Lidong Bing. M3exam:
A multilingual, multimodal, multilevel benchmark for examining large language models.
Advances in Neural Information Processing Systems, 36:5484–5505, 2023.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao
Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al. Judging llm-as-a-judge with
mt-bench and chatbot arena. Advances in Neural Information Processing Systems, 36:46595–
46623, 2023.
A
Appendix
B
Creating VisTW-Dialogue on Discord
Guidelines: The collected question-image pairs were designed to be challenging for Vision
Language Models (VLMs), focusing on realistic scenarios where users might seek assistance
(e.g., for visual impairment). All contributors were instructed to ensure their submissions
contained no personally identifiable information (PII), including names or faces of non-
public figures, Wi-Fi passwords, or any information that could reveal residential addresses.
The dataset comprises question-image pairs contributed by 9 different individuals from
various locations across Taiwan. While the geographic distribution covers multiple regions,
there is a higher concentration of samples from Taipei (the capital of Taiwan) as the majority
of our contributors resided there.
B.1
Human Annotation Process
As illustrated in Figure 5, steps to label a problem are:
1. Upload an image, use @ + hanji to submit it to the bot on discord, and include the
question and ground truth <standard answer>
2. The bot will create a discussion thread, or people can wait until the thread appears
before adding the standard answer.
3. Format for updating the standard answer:
as long as the text mentions
”ground truth:”, the system will automatically capture the text that follows as
the standard answer.
4. The standard answer can be updated repeatedly using step 3.
5. People can type ”validate result” to get score evaluations for responses from two
models.
Note: When people upload images, they waive ownership rights and agree to make the
photos public.
14

--- Page 15 ---

Preprint. Under review.
Figure 5: Workflow of adding images, labeling, and evaluating
15

--- Page 16 ---

Preprint. Under review.
Subject Name
Chinese Name
Test
Val
Dev
Accounting
會計學
100
29
5
Arts
藝術
385
91
5
Biology
生物學
150
8
5
Chemistry
化學
172
38
5
Chinese Literature
中國文學
100
45
5
Dentistry
牙醫學
220
49
5
Electronic Circuits
電子電路
388
91
5
Fundamentals of Physical Therapy
物理治療基礎
150
23
5
Geography
地理學
100
39
5
Mathematics
數學
240
54
5
Mechanics
力學
217
49
5
Medical
醫學
172
37
5
Music
音樂
100
6
5
Natural Science
自然科學
303
70
5
Navigation
航海學
100
16
5
Pharmaceutical Chemistry
藥物化學
100
45
5
Physics
物理學
100
23
5
Sociology
社會學
348
81
5
Statistics
統計學
100
45
5
Structural Engineering
結構工程
100
19
5
Veterinary Medicine
獸醫學
150
11
5
Table 7: Overview of subjects with VisTW-MCQ splits
C
Additional Details for VisTW-MCQ and VisTW-Dialogue
C.1
Details of subjects for VisTW-MCQ
Table 7 shows each of the subjects found in VisTW-MCQ with their broad category, as well
as total number of questions.
C.2
VisTW-MCQ
Figure 6 (left) shows the aspect ratio of mostly long rectangle, most of the width is longer
than the height. In the Figure 7 (left) for the MCQ dataset most of the image pixel is below
1M pixels.
C.3
VisTW-Dialogue
Figure 6 (right) shows the aspect ratio of mostly long rectangle, most of the width is longer
than the height. In the Figure 7 (right) for the MCQ dataset most of the image pixel is above
1M pixels.
16

--- Page 17 ---

Preprint. Under review.
0
5
10
15
20
Aspect Ratio (width/height)
0
200
400
600
800
1000
1200
1400
Number of Images
VisTai-MCQ Aspect Ratio Distribution
0.50
0.75
1.00
1.25
1.50
1.75
2.00
2.25
Aspect Ratio (width/height)
0
10
20
30
40
50
60
VisTai-Dialogue Aspect Ratio Distribution
Figure 6: Histograms comparing the aspect ratio distributions (width/height) of the VisTW-
MCQ dataset (left) and the VisTW-Dialogue dataset (right). The vertical dashed line on the
right indicates an aspect ratio of 1 (i.e., square). Most MCQ images fall below an aspect ratio
of 1 (portrait), while the Dialogue dataset shows a broader spread, with many images close
to square.
0.0
0.2
0.4
0.6
0.8
1.0
Image Resolution (total pixels)
1e6
0
200
400
600
800
1000
Number of Images
VisTai-MCQ Resolution Distribution
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
Image Resolution (total pixels)
1e7
0
10
20
30
40
50
Number of Images
VisTai-Dialogue Resolution Distribution
Figure 7: Comparison of image resolution distributions (in total pixels) for VisTW-MCQ
(left) and VisTW-Dialogue (right). The x-axis shows the total number of pixels in each image,
and the y-axis indicates how many images fall within each resolution range. The MCQ
dataset tends to contain lower-resolution images, whereas the Dialogue dataset spans a
broader range of resolutions.
17

--- Page 18 ---

Preprint. Under review.
D
Benchmarked VLM Details
For open weight models, we utilize local GPU resources (3090) for models under 11B
parameters, while larger models are accessed through the Open Router API service. For
closed weight models, we access them directly through each organization’s official API.
Model
Organization
Size
Arch
Closed Source Models
claude-3-haiku-20240307 (Anthropic, 2024a)
Anthropic
-
-
claude-3.5-sonnet-20241022 (Anthropic, 2024b)
Anthropic
-
-
gemini-1.5-flash (Team, 2024)
Google
-
Dense
gemini-1.5-flash-8b (Team, 2024)
Google
8B
Dense
gemini-1.5-pro (Team, 2024)
Google
-
MoE
gemini-2.0-pro-exp-02-05 (Team, 2024)
Google
-
-
gemini-2.0-flash-thinking-exp-1219 (Team, 2024)
Google
-
-
gemini-2.0-flash-001 (Team, 2024)
Google
-
-
gemini-2.0-flash-lite-preview-02-05 (Team, 2024)
Google
-
-
gpt-4o-2024-11-20 (OpenAI, 2024)
OpenAI
-
-
gpt-4o-2024-08-06 (OpenAI, 2024)
OpenAI
-
-
gpt-4o-mini-2024-07-18 (OpenAI, 2024)
OpenAI
-
-
nova-lite-v1
Amazon
-
-
Open Weights Models
Gemma3 27B Instruct (Gemma Team, 2025)
Google
27.4B
Dense
Qwen2.5-VL-72b-instruct (Bai et al., 2025)
Alibaba
72B
Dense
Qwen2.5-VL-7B-Instruct (Bai et al., 2025)
Alibaba
7B
Dense
Qwen2-VL-72b-instruct (Bai et al., 2023)
Alibaba
72B
Dense
Qwen2-VL-7B-Instruct (Bai et al., 2023)
Alibaba
7B
Dense
InternVL2.5-8B (Chen et al., 2025)
OpenGVLab
8B
Dense
InternVL2-8B-MPO (Chen et al., 2024b)
OpenGVLab
8B
Dense
InternVL2.5-4B (Chen et al., 2025)
OpenGVLab
4B
Dense
InternVL2-8B (Chen et al., 2024b)
OpenGVLab
8B
Dense
InternVL2-4B (Chen et al., 2024b)
OpenGVLab
4B
Dense
InternVL2-2B (Chen et al., 2024b)
OpenGVLab
2B
Dense
nternVL2-1B (Chen et al., 2024b)
OpenGVLab
1B
Dense
Llama-3.2-90B-Vision-Instruct (Patterson et al., 2022)
Meta
90B
Dense
Llama-3.2-11B-Vision-Instruct (Patterson et al., 2022)
Meta
11B
Dense
CogVLM2-llama3-chinese (Hong et al., 2024)
THUDM
19B
Dense
Breeze2-8B-Instruct (Research et al., 2025)
MediaTek
8B
Dense
Breeze2-3B-Instruct (Research et al., 2025)
MediaTek
3B
Dense
deepseek-vl2-tiny (Wu et al., 2024)
DeepSeek
-
MoE
deepseek-vl2-small (Wu et al., 2024)
DeepSeek
-
MoE
Table 8: Overview of evaluated models. For closed source models, sizes are marked with ‘-’
where not publicly disclosed. Dense stands for Decoder only Dense Transformer architecture,
MoE stands for Mixture of Experts architecture.
18

--- Page 19 ---

Preprint. Under review.
E
Prompts
E.1
VisTW-Dialogue Judgment Prompt
Apart from providing judgement prompts Figure8, we utilize a 10 point scale for evaluation,
with the score decreasing from 10. If there are any omissions or mistakes in the model
explanations, appropriate deductions will be made. Besides, in Scoring Guidelines Figure??
we also explain the range definition represented by each score, so as to better evaluate
the model’s capabilities. In the Figure12 example, according to the Scoring Method and
Scoring Guidelines, the model explanations accurately aligned with the Ground Truth and
addressed all answers with clear and structured language. This evaluation got a perfect
score of 10.
E.2
VisTW-MCQ Prompt
In VisTW-MCQ, our prompts can be found in Figure10 and Figure11 . We divide the
evaluation into two prompts: Zero-Shot COT and Direct-Answer to examine VLM model
capabilities. In these examples of Figure13 and Figure14, we use red color to mark the
model’s responses and COT processes. For COT prompts, we specifically use ”think step by
step” to guide the model’s reasoning further.
F
Does exams with figure harder than normal exam questions?
In this section we discuss whether exam questions grounded on visual context are harder
than other questions from the same exam without context. Meaning does adding additional
visual feature makes the benchmark harder?
19

--- Page 20 ---

Preprint. Under review.
Judgement Prompt
請根據使用者詢問的問題[Question] 與正確答案[Ground Truth], 去評價助手的回覆
[Assistant Response] 的評分，評分依照下方的評價指導手冊去評分。
Please evaluate the assistant’s response based on the user’s question [Question] and
the correct answer [Ground Truth], and assess the score of the assistant’s response
[Assistant Response] according to the evaluation guidelines provided below.
[問題] [Question]
{question}
[評價助手的回覆] [Assistant Response]
{response}
[正確答案] [Ground Truth]
{ground truth}
# 評分標註指南# Scoring Guidelines
{Scoring Guidelines}
## 評分方式## Scoring Method
1. 首先將回答與標準答案比較1. Responses were compared with standard
answers.
2. 評估以下幾點：2. Evaluate the following aspects:
- 是否準確？- Whether the responses were accurate?
- 是否回答了問題的所有部分- Whether all parts of the question were
addressed?
- 是否清晰且有條理？- Whether the responses were clear and well-
structured?
- 是否提供有幫助的補充說明？- Whether helpful explanations were
provided?
3. 從10分開始扣分：3. Points were deducted for errors from an initial 10-
point score.
- 每個事實錯誤（-1至-2分）- Each factual error deducted 1–2 points.
- 遺漏資訊（-1至-2分）- Missing information deducted 1–2 points.
- 語言組織不佳（-1分）- Incoherent language structure deducted 1–2
points.
- 補充說明不當或錯誤（-1分）- Inappropriate or incorrect explanations
deducted 1 point.
4. 請簡短說明評分理由，包含：Scoring rationale includes concise explana-
tions of:
- 做得好的地方- Well-addressed components or exceptional perfor-
mance.
- 缺少或錯誤的部分- Missing or incorrect information
- 為何給予此分數- Why this score was awarded?
你的回覆格式應該是如下: Your response should be in the format:
[解釋]: (你的解釋) [Explanations]: (Your explanations)
[評分]: (int分數) [Scoring]: (Int score)
Figure 8: Instruction prompt used in scoring the sample.
20

--- Page 21 ---

Preprint. Under review.
Scoring Guidelines
## 評分範圍（0-10分）Score Range (0 - 10 points)
### 10分：完美10 points: Perfect
- 完全準確無誤- Fully accurate and error-free
- 回答問題的所有部分- Address all parts of the questions
- 清晰且條理分明- Clear and well-structured
- 提供有幫助的補充說明- Helpful explanations
### 8 - 9分：非常好8-9 points: Excellent
- 有些微錯誤或遺漏- Minor errors or omissions
- 主要重點都有涵蓋- Key points are covered
- 組織良好- Clear and well-structured
- 提供有用的細節說明- Helpful explanations
### 6 - 7分：良好6-7 points: Good
- 有一些小錯誤- Some minor errors
- 大部分重點都有提到- Most key points are addressed
- 組織尚可- Adequate structure
- 有一些相關說明- Some relevant explanations
### 4 - 5分：普通4-5 points: Average
- 有數個錯誤- Several errors
- 遺漏一些重點- Some key points are omitted
- 基本的組織結構- Basic structure
- 說明不夠完整- Incomplete explanations
### 2 - 3分：不佳2-3 points: Poor
- 有許多錯誤- Numerous errors
- 遺漏重要資訊- Critical information is omitted
- 組織不清楚- Disorganized structure
- 說明不正確或不足- Incorrect or insufficient explanations
### 0 - 1分：不及格0-1 points: Failing
- 大部分錯誤- Mostly incorrect
- 未回答問題重點- The core question remains unanswered
- 沒有明確的組織- Absence of structure
- 說明不相關或有誤導- Irrelevant or misleading explanations
Figure 9: Scoring guidelines outline the criteria for each point
21

--- Page 22 ---

Preprint. Under review.
VisTW-MCQ - Zero-Shot COT Prompt
回答以下的多選題問題。並且在回覆的最後記得講格式：答案: $字母而字母是
ABCDEFG 的其中一個。回答前請先一步一步(think step by step)想好答案。你必須
使用中文回答。
Answer the following multiple-choice questions. Additionally, remember to include
the format at the end of your response: Answer: $letter, where the letter is one of A,
B, C, D, E, F, G. Before answering, carefully deliberate through the answer step by
step. You must respond in Chinese.
[問題]: [Question]
{question}
[COT]：[COT:]
{COT reasoning}
[答案]：[Answer:]
{your answer}
Figure 10: Instruction prompt used in VisTW-MCQ zero-shot COT
VisTW-MCQ - Direct-Answer Prompt
回答以下的多選題問題。並且在回覆的最後記得講格式：答案: $字母而字母是
ABCD 的其中一個。直接給我答案回覆，Do not think step by step。你必須使用中
文回答。
Answer the following multiple-choice question. Remember to include the format at
the end of your response: Answer: $letter, where the letter is one of A, B, C, or D.
Provide only the answer in Chinese without any additional explanations. Do not
think step by step. You must respond in Chinese.
[問題]: [Question]
{question}
[答案]：[Answer:]
{your answer}
Figure 11: Instruction prompt used in VisTW-MCQ direct answer
22

--- Page 23 ---

Preprint. Under review.
VisTW-Dialogue Example
請根據使用者詢問的問題[Question] 與正確答案[Ground Truth], 去評價助
手的回覆[Assistant Response] 的評分，評分依照下方的評價指導手冊去評分。
Please evaluate the assistant’s response based on the user’s question [Question] and
the correct answer [Ground Truth], and assess the score of the assistant’s response
[Assistant Response] according to the evaluation guidelines provided below.
[問題] [Question]
這在台灣哪的建築？能猜出這是什麼時間點拍的嗎？
Where is this building located in Taiwan?
Can the time period during which this photo was taken be determined?
[評價助手的回覆] [Assistant Response]
這張照片拍攝的是台北101大樓，畫面中出現的煙火表演通常是在跨年時舉行的，因
此可以推測這張照片大約是跨年夜所拍攝的。台北101在新年倒數時會舉行盛大的煙
火秀，吸引了許多民眾前來觀賞。
This photograph depicts Taipei 101, with fireworks display typically held during
New Year’s Eve celebrations. It is inferred that this photo was taken on New Year’s
Eve, as Taipei 101 annually hosts a grand fireworks show during the New Year
countdown, drawing large crowds of spectators.
[正確答案] [Ground Truth]
這是台灣台北著名的「台北101」，此圖是元旦跨年時101的煙火秀
This is the renowned Taipei 101 in Taipei, Taiwan.
The image captures the
New Year’s Eve fireworks display at the building during the annual countdown
celebration.
你的回覆格式應該是如下: Your response should be in the format:
[解釋]: (你的解釋) [Explanations]: (Your explanations)
[Explanations]: Completely correct
[評分]: (int分數) [Scoring]: (Int score)
[Scoring]: 10
Figure 12: VisTW-Dialogue for evaluating the response with prefect 10 points.
23

--- Page 24 ---

Preprint. Under review.
VisTW-MCQ - Zero-Shot COT Example
回答以下的多選題問題。並且在回覆的最後記得講格式：答案: $字母而字母
是ABCDEFG 的其中一個。回答前請先一步一步(think step by step)想好答案。你必
須使用中文回答。
Answer the following multiple-choice questions. Additionally, remember to include
the format at the end of your response: Answer: $letter, where the letter is one of A,
B, C, D, E, F, G. Before answering, carefully deliberate through the answer step by
step. You must respond in Chinese.
[問題]:
甲公司係採用帳齡分析法估計預期信用減損損失，X8 年12 月31 日應收帳款帳齡分
析資料如下：X8 年5 月12 日曾將確認無法收回之應收帳款$35,680 沖銷；X8 年12
月31 日調整前備抵損失為借餘$970。甲公司X8 年度應認列之預期信用減損損失為
何？
[Question]:
Company A uses the aging analysis method to estimate expected credit losses. The
aging analysis data for accounts receivable as of December 31, Year X8 is as follows:
On May 12, Year X8, the company wrote off accounts receivable of $35,680 confirmed
to be uncollectible; the allowance for credit losses had a debit balance of $970 before
adjustment on December 31, Year X8. What amount of expected credit loss should
Company A recognize for the Year X8?
Ａ. $37,965 Ａ. $37,965
Ｂ. $36,935 Ｂ. $36,935
Ｃ. $36,995 Ｃ. $36,995
Ｄ. $38,935 Ｄ. $38,935
[COT]:
我將計算預期信用損失。我將每個帳齡類別的餘額乘以相應的損失率，然後將結
果相加。最後，我會調整信用損失準備金中的借方餘額。預期信用損失計算如
下：1. 30天以下：$489,000 * 0.5% = $2,445 2. 31-90天：$201,000 * 2% = $4,020 3.
91-180天：$106,000 * 5% = $5,300 4. 181-360天：$48,500 * 20% = $9,700 5. 361天以
上：$27,500 * 60% = $16,500
總預期信用損失：$2,445 + $4,020 + $5,300 + $9,700 + $16,500 = $37,965
調整前信用損失準備的借方餘額：$970 因此，應確認的預期信用損失金額
為：$37,965 + $970 = $38,935
[答案]: D
[COT]:
I will calculate the expected credit loss by multiplying the balance of each aging
category by the corresponding loss rate and summing the results. Finally, adjust-
ments are made for the debit balance in the credit loss reserve. The expected credit
loss calculation is as follows: 1. Under 30 days: $489,000 × 0.5% = $2,445 2. 31-90
days: $201,000 × 2% = $4,020 3. 91-180 days: $106,000 × 5% = $5,300 4. 181-360 days:
$48,500 × 20% = $9,700 5. Over 361 days: $27,500 × 60Total expected credit loss:
$2,445 + $4,020 + $5,300 + $9,700 + $16,500 = $37,965
Debit balance of credit loss reserve before adjustment: $970 Accordingly, the
recognized expected credit loss amount is: $37,965 + $970 = $38,935
[Answer]: D
Figure 13: VisTW-MCQ - Zero-Shot COT with reasoning and correct response
24

--- Page 25 ---

Preprint. Under review.
VisTW-MCQ - Direct Answer Example
回答以下的多選題問題。並且在回覆的最後記得講格式：答案: $字母而字母
是ABCD 的其中一個。直接給我答案回覆，Do not think step by step。你必須使用
中文回答。
Answer the following multiple-choice question. Remember to include the format at
the end of your response: Answer: $letter, where the letter is one of A, B, C, or D.
Provide only the answer in Chinese without any additional explanations. Do not
think step by step. You must respond in Chinese.
[問題]:
X1 年間總公司總計將成本$150,000 之商品運交分公司，轉撥價格均按成本加價
10%，且分公司不自外界進貨。總公司運交分公司之一批商品，至期末分公司仍未
收到，而導致「總公司往來」與「分公司往來」金額不一致。總公司與分公司於X1
年底調整前試算表部分資料如下：試問分公司帳上期初存貨餘額為何？
[Question]:
During the year X1, the Head Office transferred goods costing $150,000 to the Branch
at a transfer price of cost plus 10%, with the Branch not sourcing inventory externally.
A shipment of goods dispatched by the Head Office to the Branch remained
undelivered at period-end, creating discrepancies between the balances of the Head
Office Current Account and Branch Current Account. Selected pre-adjustment trial
balance data from both entities as of year-end X1 are provided.
What was the Branch’s beginning inventory balance?
Ａ. $33,000 Ａ. $33,000
Ｂ. $30,000 Ｂ. $30,000
Ｃ. $0 Ｃ. $0
Ｄ. $20,000 Ｄ. $20,000
[答案]：B
[Answer]: B
Figure 14: VisTW-MCQ - direct answer example with incorrect responses (the answer is A)
25

```
