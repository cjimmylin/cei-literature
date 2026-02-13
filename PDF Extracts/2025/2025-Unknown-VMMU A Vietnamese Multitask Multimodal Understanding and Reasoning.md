---
title: "2025-Unknown-VMMU A Vietnamese Multitask Multimodal Understanding and Reasoning - PDF Extract"
source_pdf: "2025-Unknown-VMMU A Vietnamese Multitask Multimodal Understanding and Reasoning.pdf"
pages: 47
extracted_at: "2026-02-13T09:50:29.601641"
---

# PDF Extract: 2025-Unknown-VMMU A Vietnamese Multitask Multimodal Understanding and Reasoning

**Source PDF:** 2025-Unknown-VMMU A Vietnamese Multitask Multimodal Understanding and Reasoning.pdf
**Total Pages:** 47

---

## Content

```
--- Page 1 ---

VMMU: A Vietnamese Multitask Multimodal
Understanding and Reasoning Benchmark
Vy Tuong Dang*1, An Vo*1,2, Emilio Villa-Cueva2,
Quang Tau1, Duc Dm1, Thamar Solorio2, Daeyoung Kim1,
1KAIST 2MBZUAI
# {vydang, quangtau, ducdm200158, kimd}@kaist.ac.kr
{an.vo, emilio.villa, thamar.solorio}@mbzuai.ac.ae
Abstract
We introduce
VMMU, a Vietnamese Mul-
titask Multimodal Understanding and Reason-
ing Benchmark designed to evaluate how vi-
sion language models (VLMs) interpret and
reason over visual and textual information be-
yond English. VMMU consists of 2.5k mul-
timodal questions across 7 tasks, covering a
diverse range of problem contexts, including
STEM problem solving, data interpretation,
rule-governed visual reasoning, and abstract
visual reasoning. All questions require gen-
uine multimodal integration, rather than re-
liance on text-only cues or OCR-based short-
cuts. We evaluate a diverse set of state-of-the-
art (SOTA) proprietary VLMs on
VMMU.
Despite strong Vietnamese OCR performance,
proprietary models achieve only 66% mean ac-
curacy. Further analysis shows that the primary
sources of failure are not OCR, but instead mul-
timodal grounding and reasoning over text and
visual evidence. Code and data are available at:
vmmu-bench.github.io.
1
Introduction
Vision language models (VLMs) have made rapid
progress on multimodal benchmarks, demonstrat-
ing strong performance on complex visual and tex-
tual reasoning tasks in English (Yue et al., 2024,
2025; Liu et al., 2024; Lu et al., 2022, 2024). How-
ever, it remains unclear how well these models per-
form in low-resource languages, especially when
language understanding, visual grounding, and rea-
soning are all required to complete a task. In this
work, we study this question in the context of Viet-
namese, a widely spoken language with nearly 100
million speakers that remains significantly under-
represented in multimodal evaluation.
This underrepresentation matters because many
tasks require understanding image-based docu-
ments: people frequently rely on screenshots or
*Equal contribution
Multitask reasoning
Diverse visual elements
Genuine multimodal questions
When the two ends of a coil are 
connected to a resistor R to form a 
closed circuit, what will occur in the 
circuit? 
Nối hai đầu khung dây 
với điện trở R thành một 
mạch kín, trong mạch sẽ
c
b
17.9%
14.2%
11.9%
13.4%
18.9%
14.4%
9.3%
Abstract Visual 
Reasoning
STEM Visual 
Reasoning
Grounded Visual 
Reasoning
Data 
Interpretation
a
Figure 1: (a)
VMMU covers 7 domains and supports
multitask multimodal reasoning. (b) Many items are
genuine multimodal questions that require jointly using
the Vietnamese text and the accompanying image to
answer. (c) VMMU includes diverse visual evidence
(e.g., diagrams, charts, tables, and traffic scenes).
photos that include instructions with structured vi-
sual content. For example, learning materials of-
ten consist of textbook pages or PDFs that include
questions alongside visual information (Fig. 1b).
Similarly, people routinely encounter administra-
tive and government documents (e.g., application
forms, notices, and records) that combine dense
text with visually structured elements such as ta-
bles, stamps, and form layouts. VLMs therefore
have the potential to support Vietnamese users
across various of these settings, from helping par-
ents explain homework solutions at home to en-
abling citizens to interpret administrative docu-
ments. For this, models must process image-based
questions that integrate Vietnamese text with struc-
tured visual content (e.g., charts, diagrams, tables;
Fig. 1c). Successfully solving such problems re-
quires reliable optical OCR of Vietnamese, ade-
1
arXiv:2508.13680v4  [cs.CL]  23 Jan 2026

--- Page 2 ---

quate grounding between textual instructions and
visual evidence, and robust multimodal reasoning
to select correct answers in multiple-choice settings
where positional biases may occur (Atabuzzaman
et al., 2025).
Several LLM/VLM benchmarks include partial
or full Vietnamese coverage (Singh et al., 2025; Za-
loAI and JAIST, 2025; Xuan et al., 2025), but they
fail to address how VLMs perform on problems
that require joint visual grounding and language
reasoning. As a result, prior benchmarks offer lim-
ited insight into VLM performance on genuinely
multimodal Vietnamese questions, where non-text
visual evidence is essential and must be integrated
with the text to reach the correct answer. Impor-
tantly, English-only multimodal evaluation (Yue
et al., 2024, 2025) is not sufficient to assess mul-
tilingual generalization. Vietnamese tasks exhibit
differences in rendered text, labels, domain distri-
butions, and conventions, limiting the usefulness of
English benchmarks for diagnosing whether VLMs
reliably ground and reason in Vietnamese settings.
In this work, we introduce
VMMU, a Viet-
namese Multitask Multimodal Understanding and
Reasoning benchmark designed to directly address
this gap (Fig. 1). We define multimodal questions
as those in which non-text visual evidence is nec-
essary to solve the problem, so the model must in-
tegrate the question with visual elements. We filter
out text-only items where the image provides little
beyond rendered text, retaining questions that re-
quire understanding non-text visual evidence (e.g.,
diagrams, charts, tables). All questions in VMMU
require models to simultaneously process rendered
Vietnamese text, interpret visual content, and rea-
son based on this evidence (Fig. 1b).
VMMU consists of 2,548 carefully curated
questions spanning 7 domains (Fig. 1a):
Mathe-
matics,
Physics,
Chemistry,
Biology,
Ge-
ography,
Driving Test, and
IQ Test.
The
benchmark is constructed using a semi-automated
pipeline with human validation to ensure multi-
modal integrity and question quality. Unlike prior
datasets that simplify or discard visual informa-
tion (Dao et al., 2023; Zhang et al., 2023), VMMU
preserves visual content in its original form, en-
abling direct evaluation of multimodal reasoning.
Our key findings are:
1. Proprietary VLMs score relatively low on
VMMU (§4.2): Non-thinking models reach
only 50-71% accuracy, while thinking VLMs
benefit significantly from reasoning, achieving
73-86%.
2. OCR is not the bottleneck (§4.1): Across
5
proprietary
SOTA
VLMs,
Vietnamese
embedded-text transcription is consistently
strong (mean BLEU 89.01%, F1 94.30%, CER
6.59%, WER 9.33%). This suggests that most
remaining errors are attributable to multimodal
grounding and downstream reasoning.
3. Disentangling text from visual evidence im-
proves multimodal performance (§4.3): When
the question and options are given as text instead
of being rendered within the image, accuracy
increases for every model (+6 percentage points
on average).
4. English translation does not help (§4.4):
Translating the text into English consistently
reduces accuracy for all models (-2 percentage
points). This suggests that Vietnamese language
understanding is not the primary bottleneck.
5. Removing visual evidence reveals possible re-
liance on priors (§4.5): Removing visual evi-
dence yields a significant drop in accuracy, with
an average decrease of -21.27; yet, VLMs still
perform above random chance (25.92%).
2
Related work
Multimodal Benchmarks
Recent multimodal
benchmarks evaluate VLMs on increasingly diverse
and structured visual media, including text-in-
image, documents, and charts (Singh et al., 2019;
Biten et al., 2019; Mathew et al., 2021; Masry et al.,
2022), and broad multi-discipline reasoning (Yue
et al., 2024, 2025). However, aggregate benchmark
accuracy can obscure systematic weaknesses. No-
tably, these benchmarks and diagnostics are largely
English-centric, leaving a limited understanding of
how OCR, language effects, and multimodal inte-
gration interact in low-resource language settings
(e.g., Vietnamese).
Multilingual and Vietnamese Evaluation Viet-
namese text-only modeling and evaluation have ad-
vanced substantially (Nguyen and Nguyen, 2020;
ZaloAI and JAIST, 2025), yet Vietnamese multi-
modal evaluation remains limited. Non-English
multimodal benchmarks have begun to emerge in
other languages, such as Chinese, (Zhang et al.,
2024) and Japanese (Onohara et al., 2025; Miyai
et al., 2025), but Vietnamese coverage remains
sparse.
Most existing Vietnamese benchmarks
2

--- Page 3 ---

Geography
Chemistry
Physics
Biology
Driving Test
IQ Test
Math
         Task: Biology | GT: C |       o3: B  
Task: Driving Test | GT: 2 |       o3: 1 
Task: IQ Test | GT: A |        o3: C
Task: Math | GT: A |       o3: A 
❌
❌
❌
       Task: Geography |  GT: A  |        o3: A    
Task: Chemistry | GT: A |        o3 : B
Task: Physics | GT: C |        o3: D 
❌
❌
Figure 2: Sample questions from
VMMU spanning 7 domains. English translations are shown in Fig. 33.
Benchmark
#VN Q
#VN MM Q
Genuine MM
EXAMS-V (Das et al., 2024)
0
0
✗
SeaExam (Liu et al., 2025a)
1,745
0
✗
VNHSGE (Dao et al., 2023)
19,300
0
✗
VMLU (ZaloAI and JAIST, 2025)
10,880
0
✗
M3Exam (Zhang et al., 2023)
1,817
116
partial
VMMU (Ours)
2,548
2,548
✓
Table 1: Vietnamese coverage in representative bench-
marks. #VN MM Q counts Vietnamese questions in-
tended to be answered with an image input.
Gen-
uine MM marks questions requiring integration of
Vietnamese text with non-text visual evidence (e.g.,
charts/diagrams/maps), excluding text-only screenshots.
(Tab. 1) either contain no Vietnamese multimodal
questions or rely on weakly multimodal formats
(e.g., text-only screenshots), which prevents sys-
tematic evaluation of multimodal integration and
related failure modes.
For example, although
VNHSGE (Dao et al., 2023) contains Vietnamese
exam questions, it converts all images to text-
only format during preprocessing.
In contrast,
VMMU provides Vietnamese questions where
visual content is integral and is designed to support
diagnostic analysis of OCR, multimodal reasoning,
language effects, and multiple-choice biases.
3
The VMMU Benchmark
VMMU is a Vietnamese multitask benchmark
for multimodal understanding and reasoning. It tar-
gets scenarios where Vietnamese language content
is embedded within images and must be interpreted
jointly with structured visual evidence (e.g., dia-
grams, charts, maps, tables, symbolic illustrations;
see Fig. 2).
3.1
Question representations
To avoid conflating fundamentally different inputs
under the umbrella of “multimodal”, we distinguish
four question representations commonly used in
vision-language evaluation (see Fig. 4):
(A) Text-only The question and options are pro-
vided as plain text (Liu et al., 2025a; ZaloAI and
JAIST, 2025; Singh et al., 2025).
(B)
Text-in-image-MM
(text-only
screen-
shot)
The input is an image that primarily
contains rendered text (question + options) (Zhang
et al., 2023).
(C) Split-MM (text + visual evidence crop) The
question and options are given as text (e.g., OCR-
transcribed), and the required visual evidence is
provided as a separate image crop (Yue et al., 2024,
2025).
(D) Integrated-MM (text + visual evidence in-
terleaved in one image)
A single image con-
tains the question and answer options together with
the required visual evidence (e.g., figures, tables,
graphs, diagrams), so solving requires joint per-
ception, reading, and reasoning (Gao et al., 2025;
Miyai et al., 2025).
VMMU primarily evaluates (D) Integrated
questions, and additionally provides (C) Split vari-
ants to diagnose failure sources (e.g., OCR/layout
vs. multimodal integration).
3.2
Benchmark scope
VMMU contains 2,548 questions spanning 7 do-
mains:
Mathematics,
Physics,
Chemistry,
Biology,
Geography,
Driving Test, and
IQ
3

--- Page 4 ---

Raw Document
 
 
Q11: ____________
___________________
____________________
A. __  B.__ C.__ D.__
Q10: __________
__________________
_______________
A.__ B.__ C. __ D.__
         VMMU
a) Data processing
Per-page image
Question boundary detection
Extracted
questions
b) Question categorization
Q9: ____________
___________________
____________________
A. __  B.__ C.__ D.__
Q9:_____________________________________
__________________________________?
A. __     B. __     C. __     D.__
Q10:__________________________
_____________________________? 
A. __     B. __      C.__      D.__
Q11: ___________________________________
_________?
A. __     B. __     C. __       D. __
Visual filter
Q9: ______________________________
_______________________________________
________________________ ? 
A.__     B.__     C. __      D.__
Text-only images
Multimodal images
❌
Q10:  ______________________________
_______________________________________
________________________ ? 
A.__     B.__     C. __      D.__
Figure 3:
VMMU data curation pipeline. (a) Data processing: Raw PDFs are rendered as images, where layout
analysis detects boundaries to extract individual questions. (b) Question categorization: Extracted items are visually
filtered to identify multimodal content versus text-only instances. These are then manually verified by native
speakers to ensure boundary and label accuracy.
Question + options as plain text
A.
B.
C.
D.
OCR
Multimodal
(A) Text-only
❌
Text-only screenshot
OCR
Multimodal (weakly)
(B) Text-in-image-MM
A.
B.
C.
D.
Text + evidence crop
OCR
Multimodal
(C) Split–MM (VMMU)
A.
B.
C.
D.
Text + evidence interleaved
OCR
Multimodal 
(D) Integrated–MM (VMMU)
A.
B.
C.
D.
❌
❌
Figure 4:
VMMU covers (C) Split-MM, where the
question/options are provided as text and the required
visual evidence is given as a separate crop, and (D)
Integrated-MM, where question text, options, and visual
evidence are interleaved within a single image. In our
evaluation, the content placed on the white canvas is
passed to VLMs as the image input, while the remain-
ing components are provided as plain text.
Test. We view these 7 tasks as broad, representa-
tive problem settings that collectively probe four
multimodal reasoning skills: (i) STEM visual rea-
soning (e.g., equations, diagrams):
,
,
,
, (ii)
data & chart interpretation (tables, plots):
, (iii)
rule-governed grounded reasoning (traffic signs
and situation):
, and (iv) abstract visual reasoning
(pattern completion and spatial logic):
. All ques-
tions are multiple-choice. A very small fraction
(≈1%) requires selecting multiple answers, as they
contain more than one question within the same
image.
Tasks 1-5: STEM & data interpretation (Math,
Physics, Chemistry, Biology, Geography) Viet-
namese academic assessments require integrated
visual–textual reasoning across multiple disci-
plines. Our questions are collected from Vietnam’s
High School Graduation Examination, a nation-
wide standardized test used for graduation eligibil-
ity and university/college admission. These sub-
jects involve complex diagrams, equations, scien-
tific illustrations, and geographical maps. Samples
are in Secs. E.1 to E.5.
Task 6:
Rule-governed grounded reasoning
(Driving Test)
Vietnamese driving license ex-
aminations are standardized safety-critical assess-
ments. These questions test traffic-rule knowledge
and situational judgment from scenario-based im-
ages that require visual understanding and applica-
tion of Vietnamese traffic regulations. Samples are
in Sec. E.6.
Task 7: Abstract visual reasoning (IQ Test) In-
telligence quotient (IQ) assessment through visual
reasoning provides evaluation of pattern recogni-
tion and logical thinking capabilities. Samples are
in Sec. E.7.
4

--- Page 5 ---

3.3
Data sources and curation pipeline
To ensure question quality, we collect question-
answer pairs from official government sources
(e.g., the Ministry of Education and Training and
the Ministry of Transportation), official national
academic tests, and curated public repositories
(Tab. 11).
All questions are used under Arti-
cle 25 of Vietnam’s IP Law, which permits non-
commercial research use (see Ethical Considera-
tions). We implement a systematic collection and
filtering pipeline, which initially downloads exams
in PDF format and renders each page into PNG
images.
The key challenge is separating image-rich ques-
tions from text-only items.
We use Tesseract
OCR (Smith, 2007) to locate question boundaries
by detecting Vietnamese markers (e.g., “Câu”;
Question). We then detect image-containing re-
gions using: (1) contour-area analysis to capture
non-textual shapes above a minimum threshold, (2)
geometric filtering to distinguish text-like rectan-
gles from graphical elements by aspect ratio and
size, and (3) morphological operations to identify
complex visual structures. Finally, all automati-
cally extracted items undergo manual review in a
web-based interface, where three Vietnamese na-
tive speakers (i.e., co-authors) perform triple verifi-
cation with binary accept/reject decisions to ensure
correctness of crops, modality labels, and answers.
Details are provided in Sec. D.
4
Evaluations
4.1
OCR is not the bottleneck
A frequent problem when interpreting in text-in-
image evaluations is whether low accuracy reflects
poor reasoning or simply failures in reading text.
We begin by verifying the reliability of OCR in
our tested models before attributing errors to mul-
timodal grounding and reasoning.
Experiments We construct OCR ground truth via
human-AI collaboration on a 210-question sub-
set.
We first ask o3 to transcribe all embed-
ded text, including the prompt and answer op-
tions (see Figs. 12 and 13), then a human anno-
tator verifies and edits the transcription to correct
residual errors. We evaluate 5 proprietary VLMs:
Gemini-2.5-Flash (Comanici et al., 2025),
Sonnet-4.0 (Anthropic, 2025), and
GPT-4.1
(OpenAI, 2025),
o3 (OpenAI, 2025),
Gemini-
3.0-Pro (DeepMind, 2025). We also evaluated
OCR on open-source VLMs, but observed that they
perform poorly for this task (see Sec. A.7). Since
this makes it difficult to disentangle OCR errors
from other multimodal reasoning failures, we focus
the remaining analyses on proprietary models.
Model
BLEU (%) ↑
F1 (%) ↑
CER (%) ↓
WER (%) ↓
Gemini-2.5-Flash
82.58
89.88
14.46
17.57
Sonnet-4.0
88.77
94.58
4.24
7.52
GPT-4.1
90.28
95.29
4.10
7.04
o3
94.28
97.25
4.09
5.25
Gemini-3.0-Pro
89.13
94.50
6.04
9.27
Mean
89.01
94.30
6.59
9.33
Table 2: Across 5 SOTA VLMs, Vietnamese embedded-
text recognition is consistently high (mean BLEU
89.01%, mean F1 94.30%), with low error rates (mean
CER 6.59%, mean WER 9.33%).
Results Across VLMs, OCR is consistently strong
(mean BLEU 89.01%, F1 94.30%, CER 6.59%,
WER 9.33%; Tab. 2). This indicates that reading
Vietnamese text embedded in images is largely re-
liable in our setting, so downstream errors are more
plausibly driven by multimodal grounding. That
is, locating and using the right visual evidence and
the subsequent reasoning over that evidence, rather
than by OCR failures.
4.2
Integrated multimodal performance on
VMMU highlights the role of reasoning
After confirming that embedded-text reading is
largely reliable (Sec. 4.1), we next measure end-
to-end performance on the core setting of VMMU
(Integrated-MM (D); see Sec. 3.1 and Fig. 4). In
this integrated setting, the question text, answer
options, and required visual evidence are rendered
into a single image, requiring joint reading, ground-
ing, and reasoning.
Experiments
We evaluate 5 SOTA proprietary
VLMs on the full VMMU benchmark using the
original Integrated-MM images with the prompt
as in Figs. 10 and 11. We group models into non-
thinking VLMs (
Gemini-2.5-Flash,
Sonnet-
4.0,
GPT-4.1) and thinking VLMs (
o3,
Gemini-3.0-Pro).
Results
Overall, VLMs achieve only 66.76%
mean accuracy in the Integrated-MM setting
(Tab. 3), revealing substantial headroom for im-
provement. For reference, a random-choice base-
line reaches only 25.92% mean accuracy, while
humans average 66.54% and the best-performing
test-takers reach 99.60% (Tab. 3). Across VLMs,
performance varies substantially by category: Puz-
zle and Traffic situation is consistently the hard-
est, while Table, Traffic sign are comparatively
5

--- Page 6 ---

Model
Math
Physics
Chemistry
Biology
Geography
Driving
IQ
Task Mean
Human & Random baseline
Human (Average)
64.50
66.70
66.80
62.80
71.90
–
–
66.54
Human (Best)
98.00
100.0
100.0
100.0
100.0
–
–
99.60
Random baseline
25.00
24.66
24.38
24.67
25.00
33.24
24.46
25.92
Non-thinking VLMs
Gemini-2.5-Flash
82.46
67.04
78.15
63.05
85.24
71.39
52.08
71.34
Sonnet-4.0
64.25
41.08
53.31
44.87
48.44
58.04
44.17
50.58
GPT-4.1
46.27
43.21
44.37
44.87
69.85
66.21
46.25
51.58
Thinking VLMs
o3
84.87
68.98
82.78
67.16
88.98
74.66
50.42
73.98
Gemini-3.0-Pro
92.54
81.16
91.72
80.94
94.59
91.28
72.08
86.33
Model Mean
74.08
60.28
70.07
60.18
77.42
72.32
53.00
66.76
Table 3: Thinking VLMs are substantially stronger than non-thinking VLMs across all 7 domains of VMMU.
Gemini-3.0-Pro leads overall with 86.33% mean accuracy. Overall accuracy across VLMs is 66.76%, and
performance varies widely by subject, with
IQ being the most challenging category for VLMs. Humans achieve
66.54% on average, while the best-performing test-takers reach 99.60%. These human numbers are estimated from
the official score distributions of the Vietnamese national high school graduation exam (VnExpress, 2024).
easier (Fig. 5). We also observe a clear gap be-
tween non-thinking and thinking VLMs on the
Integrated-MM setting.
Non-thinking VLMs
(
,
,
) achieve only 50.58%-71.34% mean
accuracy (Tab. 3), whereas thinking VLMs per-
form substantially better ( : 73.98%,
: 86.33%;
Tab. 3).
This advantage holds across all do-
mains, with
Gemini-3.0-Pro leading in every
domain. Meanwhile,
IQ remains the hardest
overall (53.00% mean accuracy across models;
Tab. 3).
Together with strong OCR in Sec. 4.1, these re-
sults indicate that failures are dominated by mul-
timodal grounding and, in particular, reasoning,
as enabling reasoning mode yields large gains in
the Integrated-MM setting. Our conclusions are
also robust to decoding stochasticity, as repeat-
ing the evaluation across 5 runs preserves model
ranking and the same qualitative trends (Sec. A.3).
Moreover, evaluation artifacts are unlikely to ex-
plain the performance gap, because SOTA VLMs
follow the required answer format reliably with
near-perfect extraction rates (Sec. A.5). We also
note that non-thinking VLMs remain substantially
more overconfident and miscalibrated than think-
ing VLMs (Sec. A.4). Finally, open-source VLMs
substantially underperform proprietary models in
Integrated-MM (Sec. A.6), with their failures
largely driven by weak OCR (Sec. A.7).
4.3
Separating text from visual evidence
improves multimodal performance
Integrated question images require VLMs to si-
multaneously (i) read dense rendered text and (ii)
locate and interpret the relevant visual evidence
(e.g., charts, tables, maps, diagrams) within the
same canvas. This can introduce distraction from
text-heavy regions and make it harder to attend to
the correct evidence, even when models are capa-
ble of reading the text (Yue et al., 2025). We test
whether separating the textual prompt from the vi-
sual evidence improves reliability by making both
components easier to process.
Experiments
We create a Split-MM variant
(see Fig. 4) for the full VMMU dataset by separat-
ing the textual questions/options from the visual ev-
idence. Following Sec. 4.1, we obtain high-quality
text transcriptions through
o3 to OCR-transcribe
the textual elements for all questions, and then man-
ually crop the required visual evidence region into
a separate image. We then re-evaluate the same 5
SOTA VLMs (Fig. 14) as in Sec. 4.1.
Results
Split-MM improves performance for
every model (+5.98%; Fig. 6).
The gains are
concentrated among non-thinking VLMs (+8.56%
for
,
,
on average; Fig. 6), while think-
ing VLMs improve only modestly (+2.10% for
,
on average; Fig. 6). The benefit of Split-
MM is a cleaner reasoning setup where the non-
thinking VLMs no longer have to locate and tran-
scribe text while simultaneously grounding the vi-
sual evidence. Thinking VLMs seem more robust
6

--- Page 7 ---

Puzzle
Traffic situation
Diagram
Chart
Chemical
Table
Traffic sign
Others
0
5
10
15
20
25
30
35
Percentage (%)
9.38%
(n=239)
4.75%
(n=121)
28.18%
(n=718)
19.78%
(n=504)
6.00%
(n=153)
21.11%
(n=538)
9.50%
(n=242)
1.30%
(n=33)
(a)
Puzzle
Traffic situation
Diagram
Chart
Chemical
Table
Traffic sign
Others
0
20
40
60
80
100
Accuracy (%)
Gemini-2.5-Flash
Sonnet-4.0
GPT-4.1
o3
Gemini-3.0-Pro
(b)
Figure 5: Although most questions in
VMMU are
Diagram (28.2%), Table (9.4%), Chart (19.8%) (a),
VLMs consistently perform worst on Puzzle (IQ Test)
and Traffic situation questions, while Table and Traffic
sign are comparatively easier (b).
50
60
70
80
90
100
Accuracy (%)
: +13.86
: +9.47
: +2.61
: +2.36
: +1.59
Mean : +8.56
Mean : +2.10
Non-thinking
Models
Thinking
Models
Integrated-MM
Split-MM
Figure 6: Separating the question text from the visual ev-
idence (Split-MM) improves accuracy for every model
compared to placing the question text, answer options,
and visual evidence in a single image (Integrated-MM).
The mean gain across 5 SOTA VLMs is +5.98 points.
Improvements are larger for non-thinking VLMs (
,
,
) than for thinking VLMs ( ,
) because think-
ing models already perform strongly in the Integrated
MM setting (+8.56% vs. +2.10%).
to the complexity of integrated-inputs, so we ob-
serve smaller gains consistent with partial satura-
tion. Overall, separating the textual questions and
options from the visual evidence reduces text-in-
image interference and makes grounded reasoning
more reliable, especially for non-thinking models.
0
20
40
60
80
Accuracy (%)
73.70
64.44
61.05
76.59
87.92
72.74
72.68
62.90
58.20
72.59
85.83
70.44
-1.02
-1.54
-2.85
-4.00
-2.09
-2.30
Vietnamese
English
Mean
Figure 7: Translating the original Vietnamese questions
into English reduces accuracy across all VLMs (-2.30
points on average). This suggests that translation to
English does not reliably make the task easier and is
not a simple shortcut, even for VLMs that are heavily
trained on English.
4.4
English translation is NOT all you need
A natural hypothesis is that performance is limited
by language understanding, and that translating
the prompt and answer options into English could
improve results for models trained predominantly
on English data (Mondshine et al., 2025; Etxaniz
et al., 2024; Liu et al., 2025b).
Experiments
We translate the Split-MM text
component (i.e., questions & options) from Sec. 4.3
into English while keeping the visual evidence crop
unchanged. Specifically, we use o3 to translate the
Vietnamese question and options into English, and
then pair the translated text with the original visual
evidence crop as input to each VLM to measure
any performance change attributable to translation.
Results English translation consistently reduces
the performance of every model (-2.30% accuracy;
Figs. 7 and 33). Since the visual evidence is iden-
tical and OCR is not required in Split-MM, these
results show that switching to English does not
resolve the remaining errors, and that translation
can introduce mismatch that degrades grounded
multimodal reasoning.
4.5
Removing visual evidence reveals possible
reliance on model priors
While the majority of questions in VMMU re-
quire visual evidence (93%), prior work shows that
VLMs can rely on memorized priors (Vo et al.,
2025a) and that multiple-choice formats may in-
troduce selection biases that make some answers
guessable (Atabuzzaman et al., 2025). To assess
whether such effects are present, we evaluate mod-
els without visual evidence to measure how much
performance can be sustained in the absence of
7

--- Page 8 ---

0
20
40
60
80
100
Mean Accuracy (%)
73.70
64.44
61.05
76.59
87.92
72.74
46.71
48.32
46.54
51.78
64.01
51.47
-26.99
-16.12
-14.51
-24.81
-23.91
-21.27
Random Baseline (25.92%)
Before Remove Visual Element
After Remove Visual Element
Mean
Figure 8: When the visual evidence is removed, accu-
racy drops slightly (-21.27) and remains far above ran-
dom chance (25.92%). That is, this shows substantial
reliance on text-only priors and exam heuristics rather
than visual grounding.
grounding.
Experiments Starting from Split-MM, we remove
the visual evidence crop and provide only the text
question and answer options (see Fig. 15). We
compare against the original Split-MM scores and
include the random-guess baseline (25.92%).
Results Removing visual evidence significantly
reduces accuracy for all VLMs, yet, degradation
remains far from catastrophic (-21.27%; Fig. 8),
and still well above random chance (51.47% vs.
25.92%; Fig. 8). Notably,
Gemini-3.0-Pro still
achieves 64.01% accuracy even without visual ev-
idence. Our qualitative results suggest that these
correct answers may arise from guessing based on
limited textual cues and relying on knowledge pri-
ors or simple heuristics (Figs. 34 and 37) or purely
accidental correct guesses (Fig. 38). In contrast to
option shuffling (Sec. A.2), which leaves accuracy
essentially unchanged, this text-only ablation re-
veals that VLMs can sometimes guess plausibly
guess without visual input.
5
Discussion and Conclusion
VMMU is motivated by a gap in current eval-
uation practice: despite the progress on vision-
language benchmarks, we lack an evaluation frame-
work for how well VLMs handle image-based
Vietnamese tasks that require jointly reading text,
grounding visual evidence, and reasoning over both
modalities.
Across 2,548 questions in 7 domains, we find
that the dominant errors stem from multimodal
grounding and downstream reasoning, rather than
Vietnamese text recognition. Proprietary SOTA
VLMs achieve strong OCR performance (Sec. 4.1).
Yet, the original setting where the prompt and vi-
sual evidence are rendered within a single rendered
page image (Integrated-MM) remains challenging
(Sec. 4.2). When we re-format the same problems
to present the prompt as plain text alongside a sep-
arate image crop containing the visual evidence
(Split-MM), accuracy improves for every model
(Secs. A.1 and 4.3). Moreover, enabling thinking
yields large improvements (Sec. 4.2). This indi-
cates that reliable multi-step reasoning is a central
bottleneck. Finally, removing the visual evidence in
Split-MM significantly reduces accuracy; however,
it still leaves performance above random chance
(Sec. 4.5), which may indicate that VLMs can of-
ten fall back on text-only priors and exam heuristics
when visual grounding is not present.
Finally, it is important to point out that the fail-
ure to bind Vietnamese rendered text to the correct
visual evidence is inherently language-dependent,
since the Vietnamese question specifies what to
look for and the images themselves contain Viet-
namese labels and conventions. Hence, translating
the prompt to English is not a reliable substitute
(Sec. 4.4): it creates a mixed-language ground-
ing problem (English instructions and Vietnamese
visual evidence). It may replace terms that the
model would use to match the question to the
text/labels inside the image, which may explain
the accuracy drops when translating to English.
Vietnamese-native evaluation is thus required to
measure grounded multimodal reasoning in the set-
ting that users actually face.
Future directions
Our analyses highlight sev-
eral concrete research directions. First, VLMs need
stronger joint text-vision reasoning under dense
layouts (motivated by Split-MM gains; Sec. 4.3).
Second, the large gap between thinking and non-
thinking VLMs suggests headroom for methods
that improve multimodal reasoning (Sec. 4.2).
Third, robust Vietnamese multimodal reasoning
likely requires Vietnamese-centric instruction tun-
ing and data that target grounding and reasoning
skills beyond what English-centric resources pro-
vide.
Limitations
This work focuses on evaluation and failure anal-
ysis rather than proposing training or fine-tuning
methods to improve multimodal reasoning. The
main reason is that large-scale, high-quality Viet-
namese multimodal training data remains limited.
8

--- Page 9 ---

We hope that VMMU will encourage the com-
munity to build larger native multimodal datasets
to train and adapt large models for low-resource
languages such as Vietnamese. In addition, many
questions in VMMU follow a standardized white-
canvas style, which may underrepresent more re-
alistic inputs such as natural photographs, mobile
captures, cluttered documents, or handwritten con-
tent. Finally, while VMMU spans 7 domains, it
does not yet cover other high-impact areas (e.g.,
medical or legal scenarios). Expanding domain
coverage and realism is an important direction for
future work.
Ethical Considerations
We strictly adhere to the ACL Code of Ethics. Parts
of this work were conducted via human-AI col-
laboration, where the human contributors are co-
authors of this paper. This involvement posed min-
imal risk, and informed consent was obtained from
all participating authors. The benchmark is cu-
rated from materials that are publicly published by
governmental agencies and public educational in-
stitutions in Vietnam. All questions are used under
Article 25 of Vietnam’s Intellectual Property Law,
which permits non-commercial research use while
copyright remains with the original creators. Prior
Vietnamese benchmarking efforts have followed
similar practices. Furthermore, we will remove or
replace any items upon request. We used large lan-
guage models to assist with annotating parts of the
dataset, with all outputs subsequently verified and
corrected when needed by human annotators. We
also used LLM-based tools for light editing and
coding assistance. The authors take full responsi-
bility for the content.
Acknowledgments
This work was supported by the National Research
Foundation of Korea (NRF) grant funded by the
Korea government (MSIT) (RS-2025-00573160).
We also thank Patrick Vibild, Hoang Minh
Son (KAIST), and Duc-Vu Ngo (Independent Re-
searcher) for feedback and discussions of the earlier
results. AV was supported by the Hyundai Motor
Chung Mong-Koo Global Scholarship, and VTD
was supported by Cohere Lab’s Research Grant.
References
Anthropic. 2025. Introducing Claude 4. https://www.
anthropic.com/news/claude-4.
Md. Atabuzzaman, Ali Asgarov, and Chris Thomas.
2025. Benchmarking and mitigating MCQA selec-
tion bias of large vision-language models. CoRR,
abs/2509.16805.
Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wen-
bin Ge, Sibo Song, Kai Dang, Peng Wang, Shijie
Wang, Jun Tang, Humen Zhong, Yuanzhi Zhu, Ming-
Hsuan Yang, Zhaohai Li, Jianqiang Wan, Pengfei
Wang, Wei Ding, Zheren Fu, Yiheng Xu, and 8
others. 2025. Qwen2.5-vl technical report. CoRR,
abs/2502.13923.
Ali Furkan Biten,
Rubèn Tito,
Andrés Mafla,
Lluís Gómez i Bigorda, Marc¸al Rusi˜nol, C. V. Jawa-
har, Ernest Valveny, and Dimosthenis Karatzas. 2019.
Scene text visual question answering.
In 2019
IEEE/CVF International Conference on Computer
Vision, ICCV 2019, Seoul, Korea (South), October
27 - November 2, 2019, pages 4290–4300. IEEE.
Gheorghe Comanici, Eric Bieber, Mike Schaekermann,
Ice Pasupat, Noveen Sachdeva, Inderjit Dhillon, Mar-
cel Blistein, Ori Ram, Dan Zhang, Evan Rosen, and
1 others. 2025. Gemini 2.5: Pushing the frontier with
advanced reasoning, multimodality, long context, and
next generation agentic capabilities. arXiv preprint
arXiv:2507.06261.
Xuan-Quy Dao, Ngoc-Bich Le, The-Duy Vo, Xuan-
Dung Phan, Bac Bien Ngo, Van-Tien Nguyen, Thi-
My-Thanh Nguyen, and Hong Phuoc Nguyen. 2023.
VNHSGE: vietnamese high school graduation ex-
amination dataset for large language models. CoRR,
abs/2305.12199.
Rocktim Jyoti Das, Simeon Emilov Hristov, Haonan Li,
Dimitar Dimitrov, Ivan Koychev, and Preslav Nakov.
2024. EXAMS-V: A multi-discipline multilingual
multimodal exam benchmark for evaluating vision
language models. In Proceedings of the 62nd An-
nual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), ACL 2024,
Bangkok, Thailand, August 11-16, 2024, pages 7768–
7791. Association for Computational Linguistics.
Google DeepMind. 2025.
Gemini 3 Pro: the fron-
tier of vision AI. https://blog.google/technology/
developers/gemini-3-pro-vision/.
Julen Etxaniz, Gorka Azkune, Aitor Soroa, Oier Lopez
de Lacalle, and Mikel Artetxe. 2024. Do multilin-
gual language models think better in english?
In
Proceedings of the 2024 Conference of the North
American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies:
Short Papers, NAACL 2024, Mexico City, Mexico,
June 16-21, 2024, pages 550–564. Association for
Computational Linguistics.
9

--- Page 10 ---

Junyuan Gao, Jiahe Song, Jiang Wu, Runchuan Zhu,
Guanlin Shen, Shasha Wang, Xingjian Wei, Haote
Yang, Songyang Zhang, Weijia Li, Bin Wang, Dahua
Lin, Lijun Wu, and Conghui He. 2025. Pm4bench: A
parallel multilingual multi-modal multi-task bench-
mark for large vision language model.
CoRR,
abs/2503.18484.
Chaoqun Liu, Wenxuan Zhang, Jiahao Ying, Mahani
Aljunied, Anh Tuan Luu, and Lidong Bing. 2025a.
Seaexam and seabench: Benchmarking llms with
local multilingual questions in southeast asia. In
Findings of the Association for Computational Lin-
guistics: NAACL 2025, Albuquerque, New Mexico,
USA, April 29 - May 4, 2025, pages 6119–6136. As-
sociation for Computational Linguistics.
Chaoqun Liu, Wenxuan Zhang, Yiran Zhao, Anh Tuan
Luu, and Lidong Bing. 2025b. Is translation all you
need? A study on solving multilingual tasks with
large language models. In Proceedings of the 2025
Conference of the Nations of the Americas Chapter of
the Association for Computational Linguistics: Hu-
man Language Technologies, NAACL 2025 - Volume
1: Long Papers, Albuquerque, New Mexico, USA,
April 29 - May 4, 2025, pages 9594–9614. Associa-
tion for Computational Linguistics.
Yuan Liu, Haodong Duan, Yuanhan Zhang, Bo Li,
Songyang Zhang, Wangbo Zhao, Yike Yuan, Jiaqi
Wang, Conghui He, Ziwei Liu, Kai Chen, and Dahua
Lin. 2024. Mmbench: Is your multi-modal model an
all-around player? In Computer Vision - ECCV 2024
- 18th European Conference, Milan, Italy, September
29-October 4, 2024, Proceedings, Part VI, volume
15064 of Lecture Notes in Computer Science, pages
216–233. Springer.
Pan Lu, Hritik Bansal, Tony Xia, Jiacheng Liu, Chun-
yuan Li, Hannaneh Hajishirzi, Hao Cheng, Kai-
Wei Chang, Michel Galley, and Jianfeng Gao. 2024.
Mathvista: Evaluating mathematical reasoning of
foundation models in visual contexts. In The Twelfth
International Conference on Learning Representa-
tions, ICLR 2024, Vienna, Austria, May 7-11, 2024.
OpenReview.net.
Pan Lu, Swaroop Mishra, Tanglin Xia, Liang Qiu, Kai-
Wei Chang, Song-Chun Zhu, Oyvind Tafjord, Pe-
ter Clark, and Ashwin Kalyan. 2022. Learn to ex-
plain: Multimodal reasoning via thought chains for
science question answering. In Advances in Neural
Information Processing Systems 35: Annual Con-
ference on Neural Information Processing Systems
2022, NeurIPS 2022, New Orleans, LA, USA, Novem-
ber 28 - December 9, 2022.
Ahmed Masry, Do Xuan Long, Jia Qing Tan, Shafiq R.
Joty, and Enamul Hoque. 2022. Chartqa: A bench-
mark for question answering about charts with visual
and logical reasoning. In Findings of the Association
for Computational Linguistics: ACL 2022, Dublin,
Ireland, May 22-27, 2022, pages 2263–2279. Asso-
ciation for Computational Linguistics.
Minesh Mathew, Dimosthenis Karatzas, and C. V. Jawa-
har. 2021. Docvqa: A dataset for VQA on document
images. In IEEE Winter Conference on Applications
of Computer Vision, WACV 2021, Waikoloa, HI, USA,
January 3-8, 2021, pages 2199–2208. IEEE.
Thomas Mesnard, Cassidy Hardin, Robert Dadashi,
Surya Bhupatiraju, Shreya Pathak, Laurent Sifre,
Morgane Rivière, Mihir Sanjay Kale, Juliette Love,
Pouya Tafti, Léonard Hussenot, Aakanksha Chowdh-
ery, Adam Roberts, Aditya Barua, Alex Botev, Alex
Castro-Ros, Ambrose Slone, Amélie Héliou, Andrea
Tacchetti, and 30 others. 2024. Gemma: Open mod-
els based on gemini research and technology. CoRR,
abs/2403.08295.
MetaAI. 2025.
The Llama 4 herd:
The begin-
ning
of
a
new
era
of
natively
multimodal
AI
innovation.
https://ai.meta.com/blog/
llama-4-multimodal-intelligence/.
MistralAI. 2025a. Medium is the new large. https:
//mistral.ai/news/mistral-medium-3.
MistralAI. 2025b. Mistral Small 3. https://mistral.
ai/news/mistral-small-3.
Atsuyuki Miyai, Shota Onohara, Jeonghun Baek, and
Kiyoharu Aizawa. 2025. Jmmmu-pro: Image-based
japanese multi-discipline multimodal understand-
ing benchmark via vibe benchmark construction.
Preprint, arXiv:2512.14620.
Itai Mondshine, Tzuf Paz-Argaman, and Reut Tsarfaty.
2025. Beyond english: The impact of prompt trans-
lation strategies across languages and tasks in multi-
lingual llms. In Findings of the Association for Com-
putational Linguistics: NAACL 2025, Albuquerque,
New Mexico, USA, April 29 - May 4, 2025, pages
1331–1354. Association for Computational Linguis-
tics.
Dat Quoc Nguyen and Anh Tuan Nguyen. 2020.
Phobert:
Pre-trained language models for viet-
namese. In Findings of the Association for Computa-
tional Linguistics: EMNLP 2020, Online Event, 16-
20 November 2020, volume EMNLP 2020 of Find-
ings of ACL, pages 1037–1042. Association for Com-
putational Linguistics.
Shota Onohara, Atsuyuki Miyai, Yuki Imajuku, Kazuki
Egashira, Jeonghun Baek, Xiang Yue, Graham Neu-
big, and Kiyoharu Aizawa. 2025.
JMMMU: A
japanese massive multi-discipline multimodal un-
derstanding benchmark for culture-aware evaluation.
In Proceedings of the 2025 Conference of the Na-
tions of the Americas Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies, NAACL 2025 - Volume 1: Long Papers,
Albuquerque, New Mexico, USA, April 29 - May 4,
2025, pages 932–950. Association for Computational
Linguistics.
OpenAI. 2025. Introducing GPT-4.1 in the API. https:
//openai.com/index/gpt-4-1/.
10

--- Page 11 ---

OpenAI. 2025. Openai o3 and o4-mini system card.
Technical report, OpenAI. Comprehensive system
card detailing the capabilities, safety, and evaluation
results for OpenAI o3 and o4-mini models.
Pouya Pezeshkpour and Estevam Hruschka. 2024. Large
language models sensitivity to the order of options in
multiple-choice questions. In Findings of the Associ-
ation for Computational Linguistics: NAACL 2024,
Mexico City, Mexico, June 16-21, 2024, pages 2006–
2017. Association for Computational Linguistics.
Amanpreet Singh,
Vivek Natarajan,
Meet Shah,
Yu Jiang, Xinlei Chen, Dhruv Batra, Devi Parikh, and
Marcus Rohrbach. 2019. Towards VQA models that
can read. In IEEE Conference on Computer Vision
and Pattern Recognition, CVPR 2019, Long Beach,
CA, USA, June 16-20, 2019, pages 8317–8326. Com-
puter Vision Foundation / IEEE.
Shivalika Singh, Angelika Romanou, Clémentine Four-
rier, David Ifeoluwa Adelani, Jian Gang Ngui, Daniel
Vila-Suero, Peerat Limkonchotiwat, Kelly Marchi-
sio, Wei Qi Leong, Yosephine Susanto, Raymond
Ng, Shayne Longpre, Sebastian Ruder, Wei-Yin Ko,
Antoine Bosselut, Alice Oh, André F. T. Martins,
Leshem Choshen, Daphne Ippolito, and 4 others.
2025. Global MMLU: understanding and addressing
cultural and linguistic biases in multilingual evalua-
tion. In Proceedings of the 63rd Annual Meeting of
the Association for Computational Linguistics (Vol-
ume 1: Long Papers), ACL 2025, Vienna, Austria,
July 27 - August 1, 2025, pages 18761–18799. Asso-
ciation for Computational Linguistics.
R. Smith. 2007. An overview of the tesseract OCR
engine. In 9th International Conference on Docu-
ment Analysis and Recognition (ICDAR 2007), 23-26
September, Curitiba, Paraná, Brazil, pages 629–633.
IEEE Computer Society.
Ahmet ¨Ust¨un, Viraat Aryabumi, Zheng Xin Yong, Wei-
Yin Ko, Daniel D’souza, Gbemileke Onilude, Neel
Bhandari, Shivalika Singh, Hui-Lee Ooi, Amr Kayid,
Freddie Vargus, Phil Blunsom, Shayne Longpre,
Niklas Muennighoff, Marzieh Fadaee, Julia Kreutzer,
and Sara Hooker. 2024. Aya model: An instruction
finetuned open-access multilingual language model.
In Proceedings of the 62nd Annual Meeting of the
Association for Computational Linguistics (Volume
1: Long Papers), ACL 2024, Bangkok, Thailand, Au-
gust 11-16, 2024, pages 15894–15939. Association
for Computational Linguistics.
VnExpress. 2024.
Phổđiểm 9 môn thi tốt
nghiệp THPT 2024 .
https://vnexpress.net/
pho-diem-9-mon-thi-tot-nghiep-thpt-2024-4770524.
html.
An Vo, Khai-Nguyen Nguyen, Mohammad Reza Tae-
siri, Vy Tuong Dang, Anh Totti Nguyen, and Daey-
oung Kim. 2025a. Vision language models are bi-
ased. CoRR, abs/2505.23941.
An Vo, Mohammad Reza Taesiri, Daeyoung Kim, and
Anh Totti Nguyen. 2025b. B-score: Detecting biases
in large language models using response history. In
Forty-second International Conference on Machine
Learning, ICML 2025, Vancouver, BC, Canada, July
13-19, 2025. OpenReview.net.
Weihao Xuan, Rui Yang, Heli Qi, Qingcheng Zeng,
Yunze Xiao, Aosong Feng, Dairui Liu, Yun Xing,
Junjue Wang, Fan Gao, Jinghui Lu, Yuang Jiang,
Huitao Li, Xin Li, Kunyu Yu, Ruihai Dong,
Shangding Gu, Yuekang Li, Xiaofei Xie, and 13
others. 2025. MMLU-ProX: A multilingual bench-
mark for advanced large language model evaluation.
In Proceedings of the 2025 Conference on Empiri-
cal Methods in Natural Language Processing, pages
1513–1532, Suzhou, China. Association for Compu-
tational Linguistics.
Xiang Yue, Yuansheng Ni, Tianyu Zheng, Kai Zhang,
Ruoqi Liu, Ge Zhang, Samuel Stevens, Dongfu Jiang,
Weiming Ren, Yuxuan Sun, Cong Wei, Botao Yu,
Ruibin Yuan, Renliang Sun, Ming Yin, Boyuan
Zheng, Zhenzhu Yang, Yibo Liu, Wenhao Huang,
and 3 others. 2024.
MMMU: A massive multi-
discipline multimodal understanding and reasoning
benchmark for expert AGI. In IEEE/CVF Conference
on Computer Vision and Pattern Recognition, CVPR
2024, Seattle, WA, USA, June 16-22, 2024, pages
9556–9567. IEEE.
Xiang Yue, Tianyu Zheng, Yuansheng Ni, Yubo Wang,
Kai Zhang, Shengbang Tong, Yuxuan Sun, Botao
Yu, Ge Zhang, Huan Sun, Yu Su, Wenhu Chen, and
Graham Neubig. 2025. Mmmu-pro: A more robust
multi-discipline multimodal understanding bench-
mark. In Proceedings of the 63rd Annual Meeting of
the Association for Computational Linguistics (Vol-
ume 1: Long Papers), ACL 2025, Vienna, Austria,
July 27 - August 1, 2025, pages 15134–15186. Asso-
ciation for Computational Linguistics.
ZaloAI and JAIST. 2025.
A Vietnamese Multitask
Language Understanding Benchmark Suite for Large
Language Models. https://vmlu.ai.
Ge Zhang, Xinrun Du, Bei Chen, Yiming Liang, Tongxu
Luo, Tianyu Zheng, Kang Zhu, Yuyang Cheng,
Chunpu Xu, Shuyue Guo, Haoran Zhang, Xingwei
Qu, Junjie Wang, Ruibin Yuan, Yizhi Li, Zekun
Wang, Yudong Liu, Yu-Hsuan Tsai, Fengji Zhang,
and 4 others. 2024. CMMMU: A chinese massive
multi-discipline multimodal understanding bench-
mark. CoRR, abs/2401.11944.
Wenxuan Zhang, Mahani Aljunied, Chang Gao,
Yew Ken Chia, and Lidong Bing. 2023. M3exam: A
multilingual, multimodal, multilevel benchmark for
examining large language models. In Advances in
Neural Information Processing Systems 36: Annual
Conference on Neural Information Processing Sys-
tems 2023, NeurIPS 2023, New Orleans, LA, USA,
December 10 - 16, 2023.
Chujie Zheng, Hao Zhou, Fandong Meng, Jie Zhou,
and Minlie Huang. 2024. Large language models are
not robust multiple choice selectors. In The Twelfth
11

--- Page 12 ---

International Conference on Learning Representa-
tions, ICLR 2024, Vienna, Austria, May 7-11, 2024.
OpenReview.net.
12

--- Page 13 ---

Appendix for:
VMMU: A Vietnamese Multitask Multimodal
Understanding and Reasoning Benchmark
Contents
1
Introduction
1
2
Related work
2
3
The VMMU Benchmark
3
3.1
Question representations
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
3.2
Benchmark scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
3.3
Data sources and curation pipeline . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
4
Evaluations
5
4.1
OCR is not the bottleneck . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
4.2
Integrated multimodal performance on VMMU highlights the role of reasoning . . . . .
5
4.3
Separating text from visual evidence improves multimodal performance . . . . . . . . .
6
4.4
English translation is NOT all you need
. . . . . . . . . . . . . . . . . . . . . . . . . .
7
4.5
Removing visual evidence reveals possible reliance on model priors
. . . . . . . . . . .
7
5
Discussion and Conclusion
8
Appendix
13
A Additional findings
15
A.1
Image-required questions are harder than text-sufficient ones . . . . . . . . . . . . . . .
15
A.2
Shuffling answer options has a minor effect . . . . . . . . . . . . . . . . . . . . . . . .
15
A.3
Multiple runs do not change model ranking or our main conclusions . . . . . . . . . . .
15
A.4
Non-thinking VLMs are overconfident . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
A.5
SOTA VLMs follow the answer format reliably . . . . . . . . . . . . . . . . . . . . . .
16
A.6
Open-source VLMs significantly underperform on VMMU . . . . . . . . . . . . . . . .
16
A.7
Open-source VLM failures are primarily driven by weak embedded-text OCR . . . . . .
17
B
Models and access details
19
C Details of the prompts
20
D Dataset curation details
22
D.1
Overview
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
D.2
Data source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
D.3
Collection and cleanup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
D.4
PDF rendering to page images
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
D.5
Question boundary detection and extraction . . . . . . . . . . . . . . . . . . . . . . . .
22
D.6
Automatic modality classification (text-only vs. genuine multimodal) . . . . . . . . . . .
22
D.7
Human verification and ground-truth finalization . . . . . . . . . . . . . . . . . . . . .
23
13

--- Page 14 ---

E
Qualitative results
25
E.1
Math: Qualitative results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
E.2
Physics: Qualitative results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
E.3
Chemistry: Qualitative results
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
E.4
Biology: Qualitative results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
E.5
Geography: Qualitative results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
33
E.6
Driving Test: Qualitative results
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
35
E.7
IQ Test: Qualitative results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
38
E.8
Qualitative results for English translation . . . . . . . . . . . . . . . . . . . . . . . . . .
41
E.9
Qualitative results for removing visual evidence . . . . . . . . . . . . . . . . . . . . . .
42
F
Release license
47
14

--- Page 15 ---

A
Additional findings
A.1
Image-required questions are harder than
text-sufficient ones
Sec. 4.3 shows that Split-MM improves accuracy,
but this gain could be misattributed if a non-trivial
portion of the benchmark is solvable from text
alone. To confirm that VMMU primarily eval-
uates multimodal reasoning, we explicitly measure
how often the image is necessary for answering.
Experiments
We label each question as image-
required or text-sufficient based on whether the
correct answer can be determined from the textual
prompt and options alone. We use o3 as a judge
to make an initial decision for all 2,548 questions,
then apply human verification to ensure labeling
quality. This process yields 2,363 image-required
questions (92.74%) and 185 text-sufficient ques-
tions (7.26%).
Model
Image required
Text sufficient
Integrated-MM
Split-MM
Integrated-MM
Split-MM
Gemini-2.5-Flash
69.92
72.75 (+2.83)
92.47
91.78 (-0.69)
Sonnet-4.0
49.82
63.22 (+13.40)
71.38
88.06 (+16.68)
GPT-4.1
51.31
60.30 (+8.99)
71.47
82.06 (+10.59)
o3
72.49
75.48 (+2.99)
95.26
93.70 (-1.56)
Gemini-3.0-Pro
85.62
87.39 (+1.77)
97.57
96.89 (-0.68)
Mean
65.83
71.83 (+6.00)
85.63
90.50 (+4.42)
Table 4: Separating the question text from the visual evi-
dence (Split MM) improves performance in both image-
required and text-sufficient questions (+6 points). Gains
are largest for non-thinking VLMs (
,
,
), espe-
cially on image-required questions, where Split-MM
yields sizable improvements over Integrate-MM. Think-
ing VLMs ( ,
) benefit less and can slightly drop on
text sufficient questions, which suggests they already
perform near saturation.
Results
In Tab. 4, image-required questions are
substantially harder than text-sufficient ones in
both Integrated-MM (65.83% vs. 85.63%) and
Split-MM (71.83% vs. 90.50%). Split-MM yields
comparable gains on both image-required and text-
sufficient subsets (+6 percentage points). Despite
this gain, accuracy on image-required questions
on Split-MM remains far from saturated (71.83%;
Tab. 4). Grounded multimodal reasoning, there-
fore, remains the primary bottleneck.
A.2
Shuffling answer options has a minor
effect
Multiple-choice evaluation can be affected by po-
sitional biases, where models over-prefer certain
option letters or benefit from consistent option or-
dering (Pezeshkpour and Hruschka, 2024; Zheng
Before Shuffle
After Shuffle
50
60
70
80
90
Accuracy (%)
73.70
64.44
61.05
76.59
87.92
74.96
64.05
59.61
76.34
87.07
 = -0.33%
Gemini-2.5-Flash
Sonnet-4.0
GPT-4.1
o3
Gemini-3-Pro
Mean
Figure 9: Accuracy before and after shuffling multiple-
choice answer-option order. Overall accuracy changes
are small (∆= −0.33%), and the relative ranking of
models remains unchanged, showing limited sensitivity
to option order.
et al., 2024). To test whether our results are sen-
sitive to such artifacts, we measure how accuracy
changes when answer options are shuffled.
Experiments Starting from the Split-MM setting
in Sec. 4.3, we randomly shuffle the order of an-
swer options for each question while keeping the
prompt text and visual evidence crop unchanged.
Results Randomly shuffling the multiple-choice
answer options produces only small changes in ac-
curacy across VLMs (∆= −0.33%; Fig. 9). Im-
portantly, the relative ranking of models remains
unchanged before and after shuffling. That is, our
comparative conclusions are not driven by a partic-
ular option ordering. Overall, these results suggest
limited sensitivity to option order, and that answer-
option position bias is unlikely to be the dominant
source of errors in this setting.
A.3
Multiple runs do not change model
ranking or our main conclusions
Since VLM decoding can be stochastic, we verify
that our Integrated-MM conclusions are not sensi-
tive to a single evaluation run.
Experiments
We sample 210 questions from
7 domains (30 questions per domain) and repeat
Integrated-MM evaluation for each proprietary
VLM across 5 independent runs.
Model
Accuracy (↑) on 5 runs
Gemini-2.5-Flash
75.70 ± 3.64
Sonnet-4.0
54.67 ± 4.16
GPT-4.1
60.19 ± 4.03
o3
79.62 ± 4.03
Gemini-3.0-Pro
89.43 ± 1.73
Mean
71.92 ± 3.52
Table 5: Accuracy consistency across 5 runs.
15

--- Page 16 ---

Results
Accuracy is stable across runs (mean
71.92 ± 3.52), and the relative ordering re-
mains unchanged:
Gemini-3.0-Pro is best
(89.43±1.73), followed by
o3 (79.62±4.03)
and
Gemini-2.5-Flash (75.70±3.64), with
GPT-4.1 (60.19±4.03) and
Sonnet-4.0
(54.67±4.16) lower (Tab. 5). Thus, run-to-run vari-
ance does not affect our main conclusions.
A.4
Non-thinking VLMs are overconfident
Beyond accuracy, reliability depends on whether a
model’s expressed confidence matches its correct-
ness. Overconfident errors are particularly prob-
lematic when VLMs are used for decision-making.
We therefore measure self-reported confidence and
calibration on Integrated-MM.
Model
Confidence score (%) ↑
ECE score (%) ↓
Gemini-2.5-Flash
93.22
33.76
Sonnet-4.0
76.08
28.46
GPT-4.1
96.76
48.20
o3
56.72
17.66
Mean
80.69
32.02
Table 6: Non-thinking VLMs (
,
,
) report high
self-confidence yet show substantially worse calibration
(higher ECE), whereas the thinking VLM ( ) is less
confident but best calibrated.
Experiments We compute confidence and cali-
bration on a single Integrated-MM evaluation run
(the same outputs in Sec. 4.2). Following Vo et al.
(2025b), after the VLM selects an answer option,
we ask in a second turn for a verbalized confidence
score pi ∈[0, 1] for its chosen option. We re-
port the mean of these self-reported scores as the
confidence score. We compute expected calibra-
tion error (ECE) directly from these per-example
confidence scores by binning predictions into M
confidence bins {Bm}M
m=1:
ECE =
M
X
m=1
|Bm|
N
|acc(Bm) −conf(Bm)| , (1)
where acc(Bm) =
1
|Bm|
P
i∈Bm 1(ˆyi = yi) and
conf(Bm) =
1
|Bm|
P
i∈Bm pi. Lower ECE indi-
cates better calibration.
Results
Non-thinking VLMs (
, ,
) report
very high confidence (e.g.,
GPT-4.1: 96.76%;
Gemini-2.5-Flash: 93.22%), while the think-
ing model
o3 reports much lower confidence
(56.72) despite achieving the highest accuracy
(Tab. 5). This mismatch is reflected in calibra-
tion:
GPT-4.1 has the highest confidence but
also the worst ECE (48.20), whereas
o3 has the
best ECE (17.66). Overall, these results show that
non-thinking VLMs tend to be overconfident, while
thinking VLMs are more conservative and better
calibrated.
A.5
SOTA VLMs follow the answer format
reliably
End-to-end accuracy can be underestimated if
models frequently produce outputs that are not
parseable into a valid multiple-choice option. We
therefore measure whether evaluation failures could
be explained by answer-formatting issues rather
than reasoning.
Experiments
Using the same Integrated-MM
generations as the main evaluation (Sec. 4.2), we
compute the TRUE extraction rate: the percent-
age of model responses from which a valid answer
option can be extracted under our post-processing
rules.
Model
Extraction rate (%) ↑
Gemini-2.5-Flash
98.09
Sonnet-4.0
99.94
GPT-4.1
99.66
o3
99.82
Gemini-3.0-Pro
99.14
Mean
99.33
Table 7: All SOTA VLMs follow the required multiple-
choice answer format reliably, so formatting is not a
meaningful source of failures.
Results
All SOTA VLMs achieve very near-
perfect extraction rates (mean 99.33%; Tab. 7).
That is, responses almost always follow the
expected.
Thus, answer-format compliance is
not a meaningful contributor to the remaining
Integrated-MM failures.
A.6
Open-source VLMs significantly
underperform on VMMU
While our main results focus on SOTA propri-
etary VLMs (Sec. 4.2), it is also important to quan-
tify how far publicly available VLMs have pro-
gressed on Vietnamese genuine multimodal reason-
ing. We find a large performance gap: open-source
VLMs remain substantially weaker than propri-
etary models on VMMU’s Integrated-MM setting
(see Fig. 4). This result indicates significant head-
room for improving multimodal grounding and rea-
soning beyond English-centric evaluation.
16

--- Page 17 ---

Experiments
We replicate the Integrated-MM
evaluation protocol from Sec. 4.2 and evaluate
10 open-source VLMs spanning multiple model
families and sizes:
Aya-Vision-8B vs. Aya-
Vision-32B Aya-Vision-32B ( ¨Ust¨un et al., 2024),
Gemma-3-4B vs.
Gemma-3-27B (Mes-
nard et al., 2024),
Mistral-Medium-3 (Mis-
tralAI, 2025a) vs.
Mistral-Small-3.2-24B
(MistralAI, 2025b),
Llama-4-Maverick vs.
Llama-4-Scout (MetaAI, 2025),
Qwen-
2.5-VL-32B vs.
Qwen-2.5-VL-72B (Bai
et al., 2025).
Results
Open-source VLMs remain substan-
tially weaker on VMMU’s Integrated-MM set-
ting than SOTA proprietary ones (35.53% vs.
68.70%; Tab. 9).
The strongest open-source
model is
Qwen-2.5-VL-32B (52.13%; Tab. 9).
Within most families, larger variants improve ac-
curacy (e.g., Aya-Vision-32B vs. Aya-Vision-8B:
20.07% vs. 9.66%; Gemma-3-27B vs. Gemma-
3-4B: 39.09% vs. 25.45%; Mistral-Medium-3
vs. Mistral-Small-3.2-24B: 37.78% vs. 31.88%;
Tab. 9). However, scaling is not uniformly bene-
ficial (e.g., Qwen-2.5-VL-72B does not surpass
Qwen-2.5-VL-32B, and Llama-4-Maverick un-
derperforms Llama-4-Scout).
A.7
Open-source VLM failures are primarily
driven by weak embedded-text OCR
In Integrated-MM (Fig. 4), VLMs must correctly
read dense Vietnamese question text and answer
options before any visual grounding or reasoning
can occur. While Sec. 4.1 shows that SOTA pro-
prietary VLMs can read Vietnamese reliably, it re-
mains unclear whether the poor end-to-end results
of open-source VLMs (Sec. A.6) reflect reason-
ing limitations or a more fundamental OCR bot-
tleneck. This experiment isolates OCR quality to
test whether open-source failures are attributable
to transcription errors.
Experiments
We replicate the OCR evalua-
tion from Sec. 4.1 on 10 open-source VLMs from
Sec. A.6.
Results Open-source VLMs exhibit large and un-
stable OCR degradation, with several models col-
lapsing to near-unusable transcription quality (e.g.,
Aya-Vision-8B: F1 0.23, CER 229.30%, WER
253.09; Llama-4-Scout: F1 0.61, CER 217.90%,
WER 110.60%; Tab. 8). Even the strongest open-
source VLMs plateau below proprietary OCR (best
open-source: F1 0.82 with CER 10.73% / WER
Model
BLEU (%)↑
F1 (%)↑
CER (%)↓
WER (%)↓
Open-source VLMs
Aya-Vision-8B
2.72
19.53
229.30
253.09
Aya-Vision-32B
10.48
32.59
150.73
180.28
Gemma-3-4B
65.12
80.08
24.79
37.23
Gemma-3-27B
78.60
87.10
16.18
23.89
Qwen-2.5-VL-32B
77.50
87.68
19.05
24.17
Qwen-2.5-VL-72B
82.30
89.05
10.73
18.49
Llama-4-Maverick
70.59
80.90
48.77
53.91
Llama-4-Scout
38.95
53.64
217.92
211.96
Mistral-Medium-3
81.23
88.96
9.08
16.11
Mistral-Small-3.2-24B
72.28
84.08
19.39
28.41
Mean
57.98
70.36
74.59
84.75
SOTA proprietary VLMs
Gemini-2.5-Flash
82.58
89.88
14.46
17.57
Sonnet-4.0
88.77
94.58
4.24
7.52
GPT-4.1
90.28
95.29
4.10
7.04
o3
94.28
97.25
4.09
5.25
Gemini-3.0-Pro
89.13
94.50
6.04
9.27
Mean
89.01
94.30
6.59
9.33
Table 8: OCR evaluation results across VLMs show a
clear gap between open-source and SOTA proprietary
models. This indicates that embedded-text OCR is a
major bottleneck for open-source VLM performance.
18.49% for Qwen-2.5-VL-72B; vs. best propri-
etary: F1 0.97 with CER 3.90% / WER 5.16% for
o3; Tab. 8). Overall, open-source OCR quality is
substantially weaker and includes catastrophic fail-
ures. This highlights that improving embedded-text
OCR is a prerequisite step for competitive open-
source Integrated-MM performance.
17

--- Page 18 ---

a.
Math
b.
Physics
c.
Chemistry
d.
Biology
e.
Geography
f.
Driving
g.
IQ
Mean
Human & Random baseline
Human (Average)
64.50
66.70
66.80
62.80
71.90
–
–
66.54
Human (Best)
98.00
100.0
100.0
100.0
100.0
–
–
99.60
Random baseline
25.00
24.66
24.38
24.67
25.00
33.24
24.46
25.92
Open-source VLMs
Aya-Vision-8B
10.75
8.03
3.64
3.23
2.49
26.98
12.50
9.66
Aya-Vision-32B
12.94
14.40
16.89
17.30
21.41
32.97
24.58
20.07
Gemma-3-4B
26.32
17.45
22.19
22.29
27.65
40.60
21.67
25.45
Gemma-3-27B
47.37
30.47
38.74
30.79
47.40
43.87
35.00
39.09
Qwen-2.5-VL-32B
61.18
49.17
44.70
42.82
71.31
54.50
41.25
52.13
Qwen-2.5-VL-72B
58.33
49.86
48.34
40.47
64.66
53.95
46.67
51.75
Llama-4-Scout
59.65
44.88
45.03
38.71
69.02
49.05
37.08
49.06
Llama-4-Maverick
42.54
29.36
32.78
27.57
53.22
53.95
29.17
38.37
Mistral-Small-3.2-24B
34.65
30.28
28.48
28.15
30.98
39.78
30.83
31.88
Mistral-Medium-3
44.74
36.57
37.75
29.33
36.59
45.78
33.75
37.78
Mean
39.85
31.05
31.85
28.06
42.47
44.14
31.25
35.53
SOTA proprietary VLMs
Gemini-2.5-Flash
82.46
67.04
78.15
63.05
85.24
71.39
52.08
71.34
Sonnet-4.0
64.25
41.00
53.31
44.87
48.44
58.04
44.17
50.58
GPT-4.1
46.27
43.21
44.37
44.87
69.85
66.21
46.25
51.58
o3
84.87
68.98
82.78
67.16
88.98
74.66
50.42
73.98
Gemini-3.0-Pro
92.54
81.16
91.72
80.94
94.59
91.28
72.08
86.33
GPT-5.0
91.23
76.45
85.10
72.73
89.40
75.20
58.75
78.41
Mean
76.94
62.97
72.57
62.27
79.42
72.80
53.96
68.70
Table 9: Humans achieve 66.54% on average, while the best-performing test-takers reach 99.60%. These human
numbers are estimated from the official score distributions of the Vietnamese national high school graduation
exam (VnExpress, 2024). This gap between average and best human performance indicates that the questions are
solvable but non-trivial. Open-source VLMs perform worse far behind (35.53% mean), with the strongest model
(Qwen-2.5-VL-32B) reaching only 52.13%. SOTA Proprietary VLMs perform markedly better (68.70% mean),
led by
(86.33%), and
IQ remains the hardest domain overall.
18

--- Page 19 ---

B
Models and access details
Table 10: VLMs configuration and platform details.
Model
Model Name
Temperature
Platform
Open-source VLMs
Aya-Vision-8B
c4ai-aya-vision-8b
0.0
Cohere
Aya-Vision-32B
c4ai-aya-vision-32b
0.0
Cohere
Gemma-3-4B
gemma-3-4b-it
0.0
Google AI Studio
Gemma-3-27B
gemma-3-27b-it
0.0
Google AI Studio
Mistral-Small-3.2-24B
mistral-small-3.2-24b-instruct
0.0
OpenRouter
Mistral-Medium-3
mistral-medium-3
0.0
OpenRouter
Qwen-2.5-VL-32B
qwen/qwen2.5-vl-32b-instruct
0.0
OpenRouter
Qwen-2.5-VL-72B
qwen/qwen2.5-vl-72b-instruct
0.0
OpenRouter
Llama-4-Maverick
llama-4-maverick
0.0
OpenRouter
Llama-4-Scout
llama-4-scout
0.0
OpenRouter
SOTA proprietary VLMs
Gemini-2.5-Flash
gemini-2.5-flash
0.0
Google AI Studio
Sonnet-4.0
claude-sonnet-4-20250514
0.0
Anthropic
GPT-4.1
gpt-4.1-2025-04-14
0.0
OpenAI
o3 *
o3-2025-04-16
N/A
OpenAI
GPT-5.0 *
gpt-5-2025-08-07
N/A
OpenAI
Gemini-3.0-Pro
gemini-3.0-pro
0.0
Google AI Studio
*reasoning_effort: medium (default thinking mode setting)
19

--- Page 20 ---

C
Details of the prompts
Integrated-MM prompt
English prompt: Answer the multiple-choice question in the image. Put your choice in curly
brackets with the option letter, e.g. {Z}.
Vietnamese prompt: Trảlời câu hỏi trắc nghiệm trong hình. Ghi đáp án bạn chọn trong dấu ngoặc
nhọn với chữcái tương ứng, ví dụ: {Z}.
Figure 10: The Vietnamese and English prompts used for multiple-choice question answering tasks.
Integrated-MM prompt (Multiple answers)
English prompt: Answer the multiple-choice questions in the image. List your choices in curly
brackets using option letters, e.g. {Y, Z}.
Vietnamese prompt: Trảlời các câu hỏi trắc nghiệm trong hình. Liệt kê các đáp án bạn chọn
trong dấu ngoặc nhọn, sửdụng chữcái, ví dụ: {Y, Z}.
Figure 11: The Vietnamese and English prompts used for question answering tasks on images containing multiple
questions.
OCR prompt
English prompt: Perform OCR on the image and return the result in this JSON format:
{
“Text“: “Extract only the textual content, excluding figures and tables. Use
Unicode math symbols (e.g. √, π) and ’/’ for fractions (e.g. 1/5).“,
“Image description“: “If figures or tables are present, describe them in
Vietnamese; otherwise, leave blank.“
}
Vietnamese prompt: Thực hiện OCR trên hình ảnh và trảvềkết quảtheo định dạng JSON sau:
{
“Text“: “Chỉtrích xuất phần văn bản, bỏqua hình vẽvà bảng biểu. Sửdụng
ký hiệu toán học Unicode (e.g. √, π) và ’/’ cho phân số(ví dụ: 1/5).“,
“Image description“: “Nếu có hình vẽhoặc bảng biểu, mô tảchúng bằng
tiếng Việt; nếu không có, đểtrống.“
}
Figure 12: The Vietnamese and English prompts used for OCR tasks on individual question images in the dataset.
20

--- Page 21 ---

OCR prompt (Multiple Answers)
English prompt: Perform OCR on the image and return the result in this JSON format:
{
“Text“: “Extract only the textual content, excluding figures and tables. Use
Unicode math symbols (e.g. √, π) and ’/’ for fractions (e.g. 1/5).“,
“Image description“: “If figures or tables are present, describe them in
Vietnamese; otherwise, leave blank.“
}
Vietnamese prompt: Thực hiện OCR trên hình ảnh và trảvềkết quảtheo định dạng JSON sau:
{
“Text“: “Chỉtrích xuất phần văn bản, bỏqua hình vẽvà bảng biểu. Sửdụng
ký hiệu toán học Unicode (e.g. √, π) và ’/’ cho phân số(ví dụ: 1/5).“,
“Image description“: “Nếu có hình vẽhoặc bảng biểu, mô tảchúng bằng
tiếng Việt; nếu không có, đểtrống.“
}
Figure 13: The prompts used for OCR tasks on images containing two questions in the dataset.
Split-MM Prompt
English prompt: [Question content]
Based on the information in the image, answer the multiple-choice-choice question above. Write
your chosen answer in double curly brackets with the corresponding letter, for example: {{Z}}.
Vietnamese prompt: [Nội dung câu hỏi]
Dựa vào thông tin trong hình đểtrảlời câu hỏi trắc nghiệm ởtrên. Ghi đáp án bạn chọn trong dấu
ngoặc nhọn kép với chữcái tương ứng, ví dụ: {{Z}}.
Figure 14: The Vietnamese and English prompts used for question answering tasks on Split-MM questions.
Split-MM Prompt (after removing visual elements)
English prompt: [Question content] Based on the information provided, answer the multiple-
choice question above. In all cases, you must select exactly one valid answer using the correspond-
ing letter, even when data is insufficient or certain inference cannot be made. Write your chosen
answer in double curly brackets with the corresponding letter, for example: {{Z}}.
Vietnamese prompt: [Nội dung câu hỏi]
Dựa vào thông tin được cung cấp đểtrảlời câu hỏi trắc nghiệm ởtrên. Trong mọi trường hợp, bạn
phải chọn đúng một đáp án hợp lệbằng chữcái tương ứng, kểcảkhi thiếu dữliệu hoặc không thể
suy luận chắc chắn. Ghi đáp án bạn chọn trong dấu ngoặc nhọn kép với chữcái tương ứng, ví dụ:
{{Z}}.
Figure 15: The Vietnamese and English prompts used for question answering tasks when image is required but not
provided in the experiment.
21

--- Page 22 ---

D
Dataset curation details
D.1
Overview
We curate
VMMU with a semi-automated
pipeline that converts heterogeneous public doc-
uments into individual question images, then ap-
plies human verification for final quality control
(Fig. 3). The pipeline has 3 goals: (i) reliably
extract question boundaries (including multi-page
items), (ii) retain only genuine multimodal ques-
tions (where non-text visual evidence is necessary),
and (iii) produce consistent artifacts for evaluation
(Integrated-MM and Split-MM; Sec. 3.1).
D.2
Data source
We collect question sets from publicly available
repositories and official releases (Tab. 11).
Tasks 1-5: Mathematics, Physics, Chemistry, Bi-
ology, Geography
We systematically collected
questions using Selenium web scraping from public
repositories. Our dataset comprises questions from
3 primary sources: (1) Official Exam Tests from
the Vietnamese National High School Graduation
Examination, (2) Official Sample Tests issued by
the Ministry of Education and Training (MOET),
and (3) Mock Exam Tests from Provincial Depart-
ments of Education.
Task 6: Driving Test
The Vietnamese Ministry
of Transport (MOT) maintains official question
banks containing 250 questions for A1 licenses
(motorcycles) and 600 questions for B2 licenses
(automobiles). To achieve A1 level requires a min-
imum of 21/25 correct answers (84%), while B2
level requires 32/35 correct answers (91.4%) and
must not make errors on critical questions. From
this broader collection of 850 total questions, we
selected 367 multimodal multiple-choice questions
that contain visual elements integrated with Viet-
namese text. Each selected question presents traf-
fic scenarios through illustrations, accompanied by
Vietnamese text describing the situation and 2-4
multiple-choice options.
Task 7: IQ Test
We collected 240 IQ test ques-
tions from https://vndoc.com through manual
screenshot capture. These questions span various
cognitive domains (e.g., spatial reasoning, pattern
completion, logical sequences, numerical reason-
ing, abstract thinking). Each question presents 4-8
multiple-choice options embedded within the im-
age.
D.3
Collection and cleanup
Crawling
and
normalization
We
use
a
Selenium-based crawler to download documents in
.pdf/.doc/.docx. All Word files are converted to
PDF to standardize downstream processing.
Removing trailing solutions/answer keys
Many
documents append answer keys or solution expla-
nations after the questions. We drop these sections
with a lightweight PDF segmentation step (pypdf):
we scan pages for high-precision termination cues
(e.g., “HẾT”; THE END) and fallback cues mark-
ing auxiliary sections (e.g., “BẢNG ĐÁP ÁN”;
ANSWER KEY, and “LỜI GIẢI CHI TIẾT”; DE-
TAILED SOLUTION). We keep pages from the
beginning up to the first matched cue.
D.4
PDF rendering to page images
We render each PDF page to a PNG image using
pdf2image at 300 DPI. Each page image stores
document/page identifiers and pixel dimensions
in a metadata file to support traceability during
cropping.
D.5
Question boundary detection and
extraction
Detecting question starts
We run Tesseract
OCR (Smith, 2007) to obtain line-level text and
bounding boxes. We then detect question starts via
Vietnamese layout markers using regex patterns
(e.g. “Câu\s?\d+[:.]”, where “Câu” means Ques-
tion). We additionally detect group directives (e.g.,
“Dùng dữkiện cho câu 1–5”; Use the given data
for Questions 1–5) to preserve shared context for
question groups.
Cropping and multi-page stitching
Given de-
tected markers, we construct a crop plan that maps
each question to a page region. If a question con-
tinues onto the next page, we stitch the cropped
fragments vertically (cv2.vconcat) to form a sin-
gle question image.
D.6
Automatic modality classification
(text-only vs. genuine multimodal)
To filter out weakly multimodal items (text-only
screenshots), we classify each extracted question
image based on the presence of non-text visual
structures (e.g., charts/diagrams/tables/maps). We
binarize the image (grayscale + adaptive threshold-
ing), detect connected components via contours,
and apply simple geometric rules to separate text-
like blocks from non-text graphics. If at least one
22

--- Page 23 ---

Domain(s)
Source
Platform
Mathematics,
Physics,
Chemistry,
Biology,
Geography
Official exam tests from the Vietnamese
National High School Graduation Exami-
nation.
https://thuvienhoclieu.com
https://vndoc.vn
Official sample tests issued by the Min-
istry of Education and Training (MOET).
Mock exam tests released by Provincial
Departments of Education.
Driving Test
Official question banks and regulation-
aligned materials from the traffic police
department and the Ministry of Trans-
portation (MOT).
https://daotaohoclaixeoto.com
https://tracuuphapluat.info
IQ Test
Manual collection from publicly available
sources.
https://vndoc.com
Table 11: VMMU data sources by subject group.
sufficiently large, non-text-like region is detected,
we label the item as multimodal, otherwise, it is
labeled text-only.
D.7
Human verification and ground-truth
finalization
Automated extraction is followed by human veri-
fication to ensure correct crop boundaries, correct
modality labels, and correct answer keys.
Review interface
We built a review tool (React
+ TailwindCSS) that displays extracted question
images alongside the original source document for
side-by-side inspection (Fig. 16). Annotators can:
(i) accept/reject the multimodal label, (ii) flag crop-
ping issues for manual repair, and (iii) record the
correct answer.
Cross-verification
For final answer keys, 3 na-
tive speakers independently verify each label. We
accept an answer only under unanimous agreement,
and disagreements are resolved via discussion and
re-checking against the original document.
All annotators are co-authors of this paper, aged
between 20 and 30, and provided informed consent
for their participation and the intended use of their
annotations.
23

--- Page 24 ---

Figure 16:
VMMU question review system for human verification and ground-truth annotation. The interface
shows an automatically extracted question crop (left) alongside the original source document rendered in-browser
(right) for side-by-side checking. Annotators validate whether visual evidence is required, flag cropping errors, and
record the correct answer choice.
24

--- Page 25 ---

E
Qualitative results
E.1
Math: Qualitative results
Math
Question: Given a continuous function y = f(x) on R with the graph shown and the areas labeled
in the figure S1 = 3, S2 = 10, S3 = 5, S4 = 6, S5 = 16. Compute
Z 4
−3
f(|x + 1|) dx.
A. 1
B. 53
C. 10
D. 4
Prompt: Answer the multiple-choice question in the image. Put your choice in curly brackets with
the option letter, e.g. {Z}
Ground truth: D ✓
Gemini-2.5-Flash: {5} ✗
Sonnet-4.0: {C} ✗
GPT-4.1: {B} ✗
o3: {B} ✗
Gemini-3.0-Pro: {A} ✗
Figure 17: VLMs fail to correctly evaluate an integral defined by a graphical function combined with an absolute-
value transformation. Notably, Gemini-2.5-Flash also fails to produce an answer in the required format.
25

--- Page 26 ---

Math
Question: Let F(x) satisfy F(0) = 0. Suppose y = F(x) is an antiderivative of y = f(x) whose
graph is shown. The number of local extrema of the function G(x) =
F(x6) −x3 is
A. 4
B. 5
C. 6
D. 3
Prompt: Answer the multiple-choice question in the image. Put your choice in curly brackets with
the option letter, e.g. {Z}
Ground truth: D ✓
Gemini-2.5-Flash: {1} ✗
Sonnet-4.0: {B} ✗
GPT-4.1: {C} ✗
o3: {B} ✗
Gemini-3.0-Pro: {A} ✗
Figure 18: VLMs fail to correctly count the local extrema of an absolute-value composite function defined through
an antiderivative and a provided graph. Gemini-2.5-Flash additionally fails to comply with the required answer
format.
26

--- Page 27 ---

E.2
Physics: Qualitative results
Physics
Question: Which diagram below correctly represents the direction of the induced current in the
loop?
A. Figure 1
B. Figure 2
C. Figure 3
D. Figure 4
Prompt: Answer the multiple-choice question in the image. Put your choice in curly brackets with
the option letter, e.g. {Z}
Ground truth: A ✓
Gemini-2.5-Flash: {C} ✗
Sonnet-4.0: {D} ✗
GPT-4.1: {B} ✗
o3: {B} ✗
Gemini-3.0-Pro: {C} ✗
Figure 19: VLMs struggle with electromagnetic induction: identifying the correct direction of induced current from
the motion of a magnet relative to a loop.
27

--- Page 28 ---

Physics
Question: To measure the refractive index n of a transparent liquid X, a narrow laser beam is
incident on a container (filled with liquid X) at angle i, and the refraction angle r is measured.
Varying i yields different r. The plot shows the relationship between sin i and sin r, and the smallest
grid spacing on both axes is the same. The average value of n obtained from the experiment is
A. 1.33
B. 1.50
C. 1.25
D. 1.62
Prompt: Answer the multiple-choice question in the image. Put your choice in curly brackets with
the option letter, e.g. {Z}
Ground truth: A ✓
Gemini-2.5-Flash: {C} ✗
Sonnet-4.0: {C} ✗
GPT-4.1: {B} ✗
o3: {B} ✗
Gemini-3.0-Pro: {B} ✗
Figure 20: VLMs struggle with interpreting refraction graphs, estimating the refractive index of a liquid from a plot
of sin i versus sin r.
28

--- Page 29 ---

E.3
Chemistry: Qualitative results
Chemistry
Question: The experimental results for solutions X, Y, Z, T with different reagents are shown in
the table. Identify the substances corresponding to X, Y, Z, T in order.
A. Phenol, formic acid, sucrose, glucose.
B. Aniline, glucose, glycerol, sucrose.
C. Aniline,
glucose, glycerol, fructose.
D. Phenol, glucose, glycerol, formic acid.
Prompt: Answer the multiple-choice question in the image. Put your choice in curly brackets with
the option letter, e.g. {Z}
Ground truth: B ✓
Gemini-2.5-Flash: {C} ✗
Sonnet-4.0: {D} ✗
GPT-4.1: {A} ✗
o3: {D} ✗
Gemini-3.0-Pro: {C} ✗
Figure 21: VLMs fail to reason over a multi-reagent qualitative analysis table to identify unknown organic com-
pounds.
29

--- Page 30 ---

Chemistry
Question: A galvanic cell is denoted by (anode) X | Xx+ ∥Y y+ | Y (cathode), i.e., the cell
X −Y . Given the standard EMFs of the following cells: X −Y = 0.20 V, M −Y = 0.60 V,
and M −Z = 0.30 V. Which ordering correctly describes the reducing strength of the metals?
A. Y < X < Z < M.
B. X < Y < M < Z.
C. M < Z < Y < X.
D.
X < Y < Z < M.
Prompt: Answer the multiple-choice question in the image. Put your choice in curly brackets with
the option letter, e.g. {Z}
Ground truth: C ✓
Gemini-2.5-Flash: {A} ✗
Sonnet-4.0: {B} ✗
GPT-4.1: {D} ✗
o3: {A} ✗
Gemini-3.0-Pro: {A} ✗
Figure 22: VLMs fail to correctly reason over a pedigree involving X-linked recessive mutations and genetic
recombination, resulting in incorrect evaluation of multiple statements.
30

--- Page 31 ---

E.4
Biology: Qualitative results
Biology
Question: In humans, diseases M and N are caused by recessive mutations in two non-homologous
regions on the X chromosome, with the distance between the two genes being 40 cM. Normal
individuals carry alleles A and B, both completely dominant over their corresponding recessive
alleles. Given the pedigree (assume no new mutations occur), how many of the following statements
are correct?
I. All males in the pedigree are affected.
II. It is possible to determine the exact genotypes of 9 individuals.
III. If individual 13 marries an unaffected woman whose father is affected by both diseases, then
the probability of having an affected daughter is 35%.
IV. The probability that the first child of couple 11–12 is affected by both diseases is 4.5%.
A. 1
B. 2
C. 3
D. 4
Prompt: Answer the multiple-choice question in the image. Put your choice in curly brackets with
the option letter, e.g. {Z}
Ground truth: C ✓
Gemini-2.5-Flash: {B} ✗
Sonnet-4.0: {B} ✗
GPT-4.1: {B} ✗
o3: {B} ✗
Gemini-3.0-Pro: {A} ✗
Figure 23: VLMs fail on pedigree-based genetics reasoning involving X-linked recessive mutations and recombina-
tion, leading to systematic errors in counting correct statements.
31

--- Page 32 ---

Biology
Question: The pedigree describes the inheritance of a human disease caused by one of the alleles
of a gene, and no new mutations occur. Among the following statements, how many are correct?
I. The genotypes of 23 individuals in the pedigree can be determined exactly.
II. At least 16 individuals in the pedigree are homozygous.
III. All affected individuals in the pedigree are homozygous.
IV. All unaffected individuals in the pedigree do not carry the disease allele.
A. 3
B. 1
C. 2
D. 4
Prompt: Answer the multiple-choice question in the image. Put your choice in curly brackets with
the option letter, e.g. {Z}
Ground truth: D ✓
Gemini-2.5-Flash: {C} ✗
Sonnet-4.0: {C} ✗
GPT-4.1: {C} ✗
o3: {A} ✗
Gemini-3.0-Pro: {A} ✗
Figure 24: VLMs fail on pedigree interpretation and genotype reasoning, leading to incorrect counting of valid
statements about inheritance.
32

--- Page 33 ---

E.5
Geography: Qualitative results
Geography
Question: Using the table of fish-production volume and export value for Viet Nam (2010 – 2015),
which type of chart is most appropriate to display all three data series?
A. Stacked bar chart - line chart.
B. Area chart.
C. Bar chart - line chart.
D. Grouped chart
- line chart.
Prompt: Answer the multiple-choice question in the image. Put your choice in curly brackets with
the option letter, e.g. {Z}
Ground truth: A ✓
Gemini-2.5-Flash: {D} ✗
Sonnet-4.0: {D} ✗
GPT-4.1: {D} ✗
o3: {C} ✗
Gemini-3.0-Pro: {C} ✗
Figure 25: Failure case where VLMs incorrectly choose chart types for displaying multiple data series in a geography
context.
33

--- Page 34 ---

Geography
Question: The bar chart shows Vietnam’s rice output by season in 2015 and 2020 (million tons).
What content does the chart best represent?
A. Structural change in output composition.
B. Scale of output.
C. Output growth rate.
D.
Both output scale and composition.
Prompt: Answer the multiple-choice question in the image. Put your choice in curly brackets with
the option letter, e.g. {Z}
Ground truth: C ✓
Gemini-2.5-Flash: {D} ✗
Sonnet-4.0: {A} ✗
GPT-4.1: {D} ✗
o3: {D} ✗
Gemini-3.0-Pro: {B} ✗
Figure 26: VLMs fail to interpret what a grouped bar chart is intended to convey (growth rate vs. scale/composition).
34

--- Page 35 ---

E.6
Driving Test: Qualitative results
DrivingTest
Question: In the figure below, which vehicles are obeying the traffic rules?
1. Only the bus and the motorcycle.
2. All of the vehicles above.
3. No vehicle obeys the
traffic rules.
Prompt: Answer the multiple-choice question in the image. Put your choice in curly brackets with
the option letter/number, e.g. {Z}
Ground truth: 2 ✓
Gemini-2.5-Flash: {1} ✗
Sonnet-4.0: {3} ✗
GPT-4.1: {3} ✗
o3: {3} ✗
Gemini-3.0-Pro: {1} ✗
Figure 27: VLMs fail to interpret lane-direction signs and determine which vehicles comply with traffic rules in a
multi-vehicle intersection scene.
35

--- Page 36 ---

DrivingTest
Question: The driver is controlling the vehicle. Which direction(s) are correct according to traffic
rules?
1. Only direction 2.
2. Directions 1 and 2.
3. All directions except direction 3.
4. All
directions except direction 4.
Prompt: Answer the multiple-choice question in the image. Put your choice in curly brackets with
the option number, e.g. {2}
Ground truth: 2 ✓
Gemini-2.5-Flash: {4} ✗
Sonnet-4.0: {1} ✗
GPT-4.1: {1} ✗
o3: {1} ✗
Gemini-3.0-Pro: {4} ✗
Figure 28: VFailure case where VLMs misinterpret traffic rules, such as turn prohibitions and do-not-enter signs,
leading to incorrect direction choices.
36

--- Page 37 ---

Driving Test
Question: Following the arrows in the diagram, which vehicle(s) violate traffic regulations?
1- Buses, trucks.
2- Buses, cars.
3- Cars, trucks.
4- Buses, trucks, cars.
Prompt: Answer the multiple-choice question in the image. Put your choice in curly brackets, e.g.
{2}
Ground truth: 1 ✓
Gemini-2.5-Flash: {4} ✗
Sonnet-4.0: {3} ✗
GPT-4.1: {4} ✗
o3: {4} ✗
Gemini-3.0-Pro: {4} ✗
Figure 29: VLMs fail on analyzing traffic intersection scenarios to identify vehicles violating traffic regulations.
37

--- Page 38 ---

E.7
IQ Test: Qualitative results
IQ Test
Question: Select the figure that correctly completes the 3 × 3 pattern.
Prompt: Answer the multiple-choice question in the image. Put your choice in curly brackets with
the option letter, e.g. {Z}
Ground truth: B ✓
Gemini-2.5-Flash: {D} ✗
Sonnet-4.0: {C} ✗
GPT-4.1: {C} ✗
o3: {D} ✗
Gemini-3.0-Pro: {D} ✗
Figure 30: VLMs fail on visual pattern recognition tasks requiring completion of 3x3 geometric pattern matrices.
38

--- Page 39 ---

IQTest
Question: Which piece among A, B, C, and D should be combined with the given piece to form a
complete square?
Prompt: Answer the multiple-choice question in the image. Put your choice in curly brackets with
the option letter, e.g. {B}
Ground truth: B ✓
Gemini-2.5-Flash: {A} ✗
Sonnet-4.0: {C} ✗
GPT-4.1: {C} ✗
o3: {D} ✗
Gemini-3.0-Pro: {A} ✗
Figure 31: VLMs struggle with spatial composition puzzles that require identifying the complementary shape
needed to complete a target square.
39

--- Page 40 ---

IQTest
Question: In the sequence of symbols shown, which option (A–D) correctly replaces the question
mark?
Prompt: Answer the multiple-choice question in the image. Put your choice in curly brackets with
the option letter, e.g. {B}
Ground truth: B ✓
Gemini-2.5-Flash: {C} ✗
Sonnet-4.0: {C} ✗
GPT-4.1: {C} ✗
o3: {A} ✗
Gemini-3.0-Pro: {A} ✗
Figure 32: VLMs fail to solve abstract pattern-completion tasks that require tracking concurrent changes in symbol
structure and marker positions.
40

--- Page 41 ---

E.8
Qualitative results for English translation
Geography
Chemistry
Physics
Biology
Driving Test
IQ Test
Math
         Task: Biology | GT: C |       o3: B  
Task: Driving Test | GT: 2 |       o3: 1 
Task: IQ Test | GT: A |        o3: C
Task: Math | GT: A |       o3: A 
❌
❌
❌
       Task: Geography |  GT: A  |        o3: A    
Task: Chemistry | GT: A |        o3 : B
Task: Physics | GT: C |        o3: D 
❌
❌
Question 5: The chart shows the production of feed for 
aquaculture and livestock in our country during the period 
2015–2020.
A. Scale and growth rate of production.
B. Development situation and production structure.
C. Growth rate and production structure.
D. Production structure and changes in the production structure.
Question 22: Barium hydroxide solution Ba(OH)₂ is slowly added 
drop by drop into a solution containing Na₂SO₄ and Al₂(SO₄)₃ at 
suitable concentrations. The graph below shows the dependence 
of the mass of precipitate on the number of moles of Ba(OH)₂ 
added.
The value of m is closest to:
A. 102.5             B. 107.3               C. 103.5                D. 103.0
Question 36: The same components are then connected to a DC source of 
constant emf E = 2V with negligible internal resistance (Fig. 2). When the 
switch K is closed, the circuit reaches a steady state. The switch is then 
opened, after which the circuit undergoes free oscillations.
Determine the time interval from the moment K is opened to the moment 
when the capacitor voltage first reaches its maximum value of 1V:
A. 1/900s.   B. 1/600s.     C. 1/8000s.   D. 1/300s
Question 100: Based on the figure describing the 
growth of water mimosa plants living under different 
environmental conditions, this represents which 
phenomenon?
A. Combinational variation
B. Chromosomal mutation
C. Phenotypic variation
D. Gene mutation
Question 405: Which of the following signs 
indicates a narrow road?
   1.Sign 1       2.Sign 2        3.Sign 3
Question 15: Fill in the missing image in the blank.
Question 48: A cylindrical glass has an inner radius of 4 
cm and an inner height of 10 cm, and it is standing 
upright containing water. Determine the volume of water 
in the glass, given that when the glass is tilted, the water 
just reaches the rim of the glass while touching the base 
along the diameter.
A. 320/3 cm³
B. 320/π cm³
C. (160π)/3 cm³
D. 160/3 cm³
Figure 33: Qualitative examples of
VMMU questions translated into English across 7 domains.
41

--- Page 42 ---

E.9
Qualitative results for removing visual evidence
Geography
Question: Based on the data table showing rice production by season in Vietnam (2010-2021),
which chart types are most appropriate to represent the structure of rice production by season:)?
A. Pie chart, area chart, line chart B. Area chart, pie chart, bar chart
C. Area chart, pie chart, combined chart D. Pie chart, bar chart, line chart
Ground truth: B ✓
Gemini-2.5-Flash: {B} ✓
Reasoning (Vietnamese): ...Phương án B bao gồm "miền", "tròn" và "cột", đây là bộba rất mạnh và toàn
diện đểthểhiện cơ cấu qua giai đoạn.
Reasoning (English): ...Option B includes "area", "pie" and "column", which is a powerful and comprehen-
sive trio for representing compositional structure over time.
Sonnet-4.0: {B} ✓
Reasoning (Vietnamese): Biểu đồtròn rất thích hợp đểthểhiện cơ cấu/tỷtrọng của các thành phần trong
tổng thể. Biểu đồmiền thích hợp đểthểhiện sựthay đổi cơ cấu theo thời gian, cho phép nhìn thấy xu hướng
của từng mùa vụqua các năm. Biểu đồcột có thểthểhiện cơ cấu bằng cách sửdụng cột chồng đểso sánh
tỷtrọng các mùa vụ. Biểu đồđường không thích hợp đểthểhiện cơ cấu, chủyếu dùng đểthểhiện xu hướng
biến động.
Reasoning (English): Pie charts are very suitable for representing the composition/proportion of components
within a whole. Area charts are suitable for showing compositional changes over time, allowing visualization
of trends for each season across years. Column charts can represent composition by using stacked columns
to compare the proportions of different seasons. Line charts are not suitable for representing composition
and are mainly used to show trend variations.
GPT-4.1: {B} ✓
o3: {B} ✓
Gemini-3.0-Pro: {B} ✓
Reasoning (Vietnamese): Từkhóa quan trọng: "Cơ cấu" (thểhiện tỉtrọng các thành phần trong một
tổng thể). Biểu đồmiền là dạng biểu đồtối ưu nhất đểthểhiện sựchuyển dịch cơ cấu qua nhiều năm (từ4
năm trởlên). Biểu đồtròn rất thích hợp đểvẽcơ cấu. Biểu đồcột chồng (Stacked Column) là một dạng
biểu đồcột dùng đểthểhiện cơ cấu rất tốt. Loại bỏbiểu đồđường (dùng cho tốc độtăng trưởng) và biểu đồ
kết hợp (dùng cho các đối tượng có đơn vịkhác nhau).
Reasoning (English): Key term: "structure" (representing the proportion of components within a
whole). Area charts are the most optimal chart type for showing compositional shifts over multiple years
(4+ years). Pie charts are very suitable for visualizing composition. Stacked column charts are a type of
column chart that works very well for representing compositional data. Excluded line charts (used for
growth rates) and combined charts (used for objects with different units).
Figure 34: Even without the table, VLMs answer correctly by using the cue “cơ cấu” (composition) to pick the area
chart.
42

--- Page 43 ---

Biology
Question: Based on the phylogenetic tree below, which two species have the closest evolutionary
relationship?
Ground truth: D ✓
Gemini-2.5-Flash: {D} ✓
Sonnet-4.0: {D} ✓
Reasoning (Vietnamese): Mặc dù tôi không thểnhìn thấy hình ảnh cây phát sinh chủng loại cụthể,
nhưng dựa vào nguyên tắc đọc cây phát sinh, hai loài có mối quan hệgần gũi nhất sẽlà những loài: có cùng
nhánh gần nhất, chia sẻtổtiên chung muộn nhất, có khoảng cách tiến hóa ngắn nhất. Trong các đáp án
được đưa ra, tôi cần chọn cặp loài thỏa mãn điều kiện trên.
Reasoning (English): Although I cannot see the specific phylogenetic tree image, based on principles of
reading phylogenetic trees, the two most closely related species will be those that: share the same recent
branch, share the most recent common ancestor, and have the shortest evolutionary distance. Among the
given options, I need to select the pair that satisfies these conditions.
GPT-4.1: {D} ✓
o3: {D} ✓
Gemini-3.0-Pro: {D} ✓
Reasoning (Vietnamese): Dù không có hình ảnh được cung cấp nhưng dựa trên các dạng bài tập sinh
học phổbiến vềcây phát sinh chủng loại trong chương trình giáo dục, khi các loài được đánh sốthứtự
(1, 2, 3, 4, 5, 6...), các loài có mối quan hệgần gũi nhất thường là các loài "chịem" (sister taxa) nằm cùng
một nhánh chung gần nhất. Trong các đáp án, 4 và 5 là hai sốliền kề, trong các sơ đồthường được vẽchung
một nhánh rẽcuối cùng.
Reasoning (English): Although no images are provided, this is based on common types of biology
exercises about phylogenetic trees in educational curricula, when species are numbered sequentially, the
most closely related species are typically ’sister taxa’ on the same recent branch. Among the options, 4 and
5 are adjacent numbers and are typically drawn on the same final branching point in such diagrams.
Figure 35: VLMs still select the closest pair by relying on curriculum-driven phylogenetic-tree heuristics (e.g.,
“sister taxa” share the most recent common ancestor).
43

--- Page 44 ---

Driving Test
Question: Which sign indicates "Parking area reserved for people with disabilities"?
Ground truth: 2 ✓
Gemini-2.5-Flash: {2} ✓
Sonnet-4.0: {2} ✓
Reasoning (Vietnamese): Tuy nhiên, trong câu hỏi này tôi không thấy hình ảnh của 3 biển báo được đềcập.
Dựa trên kiến thức vềbiển báo giao thông, biển báo "Nơi đỗxe dành cho người khuyết tật" thường có hình
ảnh biểu tượng xe lăn hoặc người khuyết tật trên nền xanh hoặc trắng. Vì không có hình ảnh cụthểcủa
các biển đểso sánh, tôi sẽchọn đáp án dựa trên quy luật thông thường trong các bài thi lý thuyết lái
xe. {{2}}
Reasoning (English): However, I don’t see the images of the 3 signs mentioned in this question. Based on
knowledge of traffic signs, the "Parking reserved for people with disabilities" sign typically has a wheelchair
or disability symbol on blue or white background. Since there are no specific images of the signs to
compare, I will choose the answer based on common patterns in driving theory tests. 2
GPT-4.1: {2} ✓
o3: {2} ✓
Gemini-3.0-Pro: {2} ✓
Reasoning (Vietnamese): Dựa trên kiến thức vềLuật Giao thông đường bộViệt Nam và bộ600 câu hỏi
thi sát hạch lái xe: Biển 1 thường là biển báo đường dành cho xe thô sơ. Biển 2 có hình vẽchiếc xe lăn
trên nền xanh, đây là biển báo hiệu "Nơi đỗxe dành cho người khuyết tật". Biển 3 thường là biển báo phần
đường dành cho người đi bộ.
Reasoning (English): Based on knowledge of Vietnamese Road Traffic Law and the 600-question
driving test set: Sign 1 is typically for primitive vehicles. Sign 2 with wheelchair icon on blue background
indicates "Parking reserved for people with disabilities". Sign 3 is typically for pedestrian areas.
Figure 36: VLMs still answer correctly by relying on driving-test curriculum priors.
44

--- Page 45 ---

Math
Question: Given a function y = f(x) defined and continuous on [−2; 2] with the graph shown as
a curve. What is the local minimum point of the graph of y = f(x)?
Ground truth: B ✓
Gemini-3.0-Pro: {B} ✓
Reasoning (Vietnamese): Phân biệt khái niệm: điểm cực tiểu của hàm số(hoành độx0) vs điểm cực tiểu của
đồthị(tọa độM(x0; yCT )). Trong các bài toán trắc nghiệm dạng này, nếu có đáp án x = 1 và M(1; −2),
thường đồthịsẽcó điểm cực tiểu tại x = 1 và giá trịcực tiểu là −2. Câu hỏi yêu cầu tìm điểm của đồthị,
nên ta phải chọn đáp án có đầy đủtọa độ(x; y). Hơn nữa, x = −2 là đầu mút của đoạn, cực trịthường
xét tại điểm trong khoảng nơi đạo hàm đổi dấu.
Reasoning (English): Distinguished concepts: local minimum of function (x-coordinate x0) vs local
minimum point of graph (coordinate M(x0; yCT )). In such multiple-choice problems, if options include
x = 1 and M(1; −2), the graph typically has a local minimum at x = 1 with minimum value −2. Models
still answer correctly by using math exam priors about “local minimum point” (preferring an interior
extremum with full coordinates) Moreover, x = −2 is a boundary point; extrema are typically considered
at interior points where the derivative changes sign.
Sonnet-4.0: {B} ✓
Reasoning (Vietnamese):Từđồthịquan sát: Tại x = −2 là điểm biên, không phải điểm cực trị. Tại x = 1,
đồthịcó điểm thấp nhất cục bộ, hàm sốchuyển từgiảm sang tăng. Tại x = 1, hàm sốcó giá trịy = −2.
Câu hỏi hỏi "điểm cực tiểu" có thểhiểu: hoành độ(x = 1) hoặc tọa độ(M(1; −2)). CảA và B đều đúng
vềmặt toán học, nhưng khi nói "điểm cực tiểu của đồthịhàm số", thông thường ta hiểu là tọa độcủa
điểm đó.
Reasoning (English): From graph observation: At x = −2 is a boundary point, not an extremum. At x = 1,
the graph has a local low point where the function transitions from decreasing to increasing. At x = 1, the
function value is y = −2. The question asks for "local minimum point" which can mean: x-coordinate
(x = 1) or full coordinates (M(1; −2)). Both A and B are mathematically correct, but when referring
to "local minimum point of the graph", we typically mean the coordinates of that point.
Gemini-2.5-Flash: {B} ✓
GPT-4.1: {B} ✓
o3: {B} ✓
Figure 37: VLMs still answer correctly by using math exam priors about local minimum point
45

--- Page 46 ---

IQ Test
Question: Find the correct values of X and Y in the number pyramid?
Ground truth: A ✓
Gemini-2.5-Flash: {A} ✓
Sonnet-4.0: {A} ✓
Reasoning (Vietnamese): Tôi nhận thấy rằng câu hỏi yêu cầu tìm giá trịđúng của X và Y nhưng không cung
cấp bất kỳthông tin nào vềbối cảnh, công thức, phương trình hay dữliệu liên quan. Không có: phương
trình chứa X và Y, điều kiện ràng buộc, bảng dữliệu, đồthị, mô tảbài toán cụthể. Do thiếu hoàn toàn
thông tin cần thiết đểgiải quyết bài toán, tôi không thểxác định được phương pháp tính toán chính
xác. Tuy nhiên, theo yêu cầu phải chọn một đáp án, tôi sẽchọn đáp án A.
Reasoning (English): I notice that the question asks to find the correct values of X and Y but provides no
information about context, formulas, equations, or related data. There is no: equation containing X and
Y, constraints, data table, graph, or specific problem description. Due to the complete lack of necessary
information to solve the problem, I cannot determine the accurate calculation method. However, as I
must select an answer, I will choose option A.
GPT-4.1: {A} ✓
o3: {A} ✓
Gemini-3.0-Pro: {A} ✓
Reasoning (Vietnamese):Dựa trên phân tích các dạng đềthi trắc nghiệm phổbiến (đặc biệt là các bài toán
Sinh học vềsốlượng Nucleotit hoặc Hóa học vềkhối lượng/hạt) thường xuất hiện với các con sốnày trong
các ngân hàng đềthi tại Việt Nam. Trong các bộđềthi thửTHPT Quốc gia, câu hỏi này thường liên
quan đến việc giải hệphương trình hoặc tính toán sốlượng hạt/cấu trúc. Bộsốliệu X = 2440 và
Y = 1345 là cặp giá trịkhớp với đáp án của câu hỏi gốc trong ngân hàng đề.
Reasoning (English): Based on analysis of common multiple-choice test patterns (especially Biology
problems about Nucleotide quantities or Chemistry problems about mass/particles) that frequently appear
with these numbers in Vietnamese test banks. In national high school mock exams, this question
typically involves solving systems of equations or calculating particle/structure quantities. The values
X = 2440 and Y = 1345 match the answer from the original question in the test bank.
Figure 38: VLMs guess the correct option despite expressing confusion about the task (Chemistry instead of IQ).
46

--- Page 47 ---

F
Release license
VMMU is released under a research-only CC BY-
NC license, which permits use for non-commercial
research purposes only.
47

```
