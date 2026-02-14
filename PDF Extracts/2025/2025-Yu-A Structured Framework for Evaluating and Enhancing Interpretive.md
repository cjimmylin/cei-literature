---
title: "2025-Yu-A Structured Framework for Evaluating and Enhancing Interpretive - PDF Extract"
source_pdf: "2025-Yu-A Structured Framework for Evaluating and Enhancing Interpretive.pdf"
pages: 27
extracted_at: "2026-02-13T17:43:26.420351"
---

# PDF Extract: 2025-Yu-A Structured Framework for Evaluating and Enhancing Interpretive

**Source PDF:** 2025-Yu-A Structured Framework for Evaluating and Enhancing Interpretive.pdf
**Total Pages:** 27

---

## Content

```
--- Page 1 ---

A Structured Framework for Evaluating and Enhancing Interpretive
Capabilities of Multimodal LLMs in Culturally Situated Tasks
Haorui Yu1, Ramon Ruiz-Dolz2, and Qiufeng Yi3
1DJCAD, University of Dundee, United Kingdom
2ARG-tech, SSEN, University of Dundee, United Kingdom
3School of Computer Science, University of Birmingham, United Kingdom
{2655435, rruizdolz001}@dundee.ac.uk
qxy953@student.bham.ac.uk
Abstract
This study aims to test and evaluate the capabil-
ities and characteristics of current mainstream
Visual Language Models (VLMs) in generat-
ing critiques for traditional Chinese painting.
To achieve this, we first developed a quantita-
tive framework for Chinese painting critique.
This framework was constructed by extracting
multi-dimensional evaluative features covering
evaluative stance, feature focus, and commen-
tary quality from human expert critiques us-
ing a zero-shot classification model. Based on
these features, several representative critic per-
sonas were defined and quantified. This frame-
work was then employed to evaluate selected
VLMs such as Llama, Qwen, or Gemini. The
experimental design involved persona-guided
prompting to assess the VLM’s ability to gener-
ate critiques from diverse perspectives. Our
findings reveal the current performance lev-
els, strengths, and areas for improvement of
VLMs in the domain of art critique, offering
insights into their potential and limitations in
complex semantic understanding and content
generation tasks. The code used for our ex-
periments can be publicly accessed at: https:
//github.com/yha9806/VULCA-EMNLP2025.
1
Introduction
Large language models (LLMs) have demonstrated
remarkable performance on general NLP bench-
marks, yet their applicability in culturally embed-
ded, humanistic domains remains limited. In high-
context interpretive tasks such as art criticism, clin-
ical narrative analysis, or historical commentary,
model performance depends not only on linguis-
tic fluency or factual accuracy, but also on deeper
forms of cognitive alignment—epistemic sensitiv-
ity, rhetorical coherence, and cultural adaptability.
A representative and particularly demanding
testbed for such capabilities is Chinese art com-
mentary. This genre, especially when analyzing
works like traditional landscape or court paintings,
involves symbolic interpretation, aesthetic judg-
ment, and deeply situated cultural discourse. Exist-
ing multimodal LLMs are rarely evaluated in this
space. Standard benchmarks such as MME (Fu
et al., 2025) and MMBench (Liu et al., 2024) fo-
cus on object recognition or task-oriented vision-
language reasoning, while frameworks like Art-
GPT (Yuan et al., 2024) emphasize captioning and
factual grounding. These methods largely overlook
interpretive nuance and disciplinary diversity.
Meanwhile, humanistic commentary often ex-
hibits non-linear logic, specialized lexicons, and
varied stylistic conventions, particularly in Chi-
nese art contexts where rhetorical strategies such
as yijing (意境, artistic conception) or qiyun sheng-
dong (气韵生动, spiritual resonance) are essential
but difficult to quantify (Bush, 1971; Sirén, 1936).
Without appropriate grounding, LLMs risk produc-
ing synthetic outputs that mimic surface patterns
but fail to demonstrate epistemic alignment (Guo
et al., 2023). This growing mismatch calls for new
paradigms in evaluation and adaptation.
To address these challenges, we introduce
VULCA—the
Vision-Understanding
and
Language-based Cultural Adaptability Frame-
work.
VULCA is a structured evaluation and
enhancement framework designed to assess how
well VLMs align with domain-specific interpretive
practices in culturally situated tasks. Our work
centers on Chinese art commentary, but the
methodology generalizes to other multimodal
and epistemically rich domains such as religion,
medicine, or history.
VULCA combines three
core components: (1) a multi-dimensional human
expert benchmark (MHEB) constructed from 163
art commentaries annotated across five cultural
capability dimensions; (2) a persona-guided recon-
textualization mechanism using eight interpretive
personas and a domain-specific knowledge base;
and (3) a joint evaluation pipeline integrating
vector-space semantic alignment with rubric-based
arXiv:2509.23208v2  [cs.CL]  31 Jan 2026

--- Page 2 ---

capability scoring. Commentaries are generated
from annotated traditional Chinese paintings, and
their alignment with expert patterns is evaluated
with and without interventions. As a result, we
produce five contributions: (i) the definition of
VULCA, a new structured framework for assessing
and enhancing VLMs in culturally grounded,
multimodal reasoning tasks; (ii) we construct
MHEB, a high-quality human benchmark of
Chinese art commentary annotated across five ca-
pability dimensions; (iii) we develop and evaluate
persona-guided recontextualization interventions
using eight expert personas and a domain-specific
knowledge base; (iv) we demonstrate over 20%
improvement in symbolic reasoning and over
30% improvement in argumentative coherence
on Gemini 2.5 Pro using our proposed method;
and (v) we establish the generalizability of our
evaluation methodology to other epistemically rich
domains such as religion, history, and education.
Together, our work highlights the need for new
evaluation paradigms that go beyond benchmark
metrics and toward measuring how well LLMs can
adapt to the interpretive demands of real-world,
interdisciplinary contexts.
2
Related Work
Missing Evaluation Dimensions for Cultural
Reasoning.
Despite significant advances in mul-
timodal evaluation, current benchmarks primarily
target factual understanding rather than cultural
interpretation. Existing benchmarks for large or
multimodal language models, such as (Fu et al.,
2025; You et al., 2024), emphasize factual accuracy
or instruction following, seldom addressing sym-
bolic interpretation or epistemic alignment. Recent
cultural evaluation efforts like M3Exam (Zhang
et al., 2023) and SEED-Bench (Li et al., 2024),
although primarily focused on multimodal under-
standing with limited cultural coverage, begin to
incorporate cultural knowledge but focus on factual
recall rather than interpretive reasoning. ArtGPT
(Yuan et al., 2024), for instance, evaluates stylistic
generation but lacks formal metrics for interpre-
tive depth. While prior work explores aesthetic
reasoning (Wang, 2024), these studies rarely offer
structured, multi-capability evaluation. Our work
addresses this gap by introducing cultural adaptabil-
ity, operationalized through a multi-dimensional
human expert benchmark with capability rubrics,
enabling quantitative comparison in high-context
domains like Chinese art.
Limitations of Persona Conditioning Without
Grounding.
Building on evaluation gaps, current
persona-based approaches show promise but re-
main limited in cultural domains. Persona use in
LLM evaluation shows promise for style control
(Jiang et al., 2024; Wang et al., 2024), yet most
methods lack structured knowledge grounding, es-
pecially in epistemically rich domains. While re-
cent work on role-playing (Shanahan et al., 2023)
and character conditioning demonstrates behav-
ioral adaptation, these approaches often rely on
surface-level stylistic changes rather than deep do-
main expertise. Our method addresses this limita-
tion by combining persona simulation with curated
domain-specific knowledge to guide generation to-
wards symbolic reasoning and cultural interpreta-
tion, not just stylistic alignment, offering a con-
trolled intervention mechanism.
Gap in Multimodal Input–Interpretation Evalu-
ation.
Current multimodal frameworks like MM-
Bench or LLaVA (Liu et al., 2023) primarily focus
on classification, question answering, or instruc-
tion following, rarely requiring grounded interpre-
tation. Our pipeline links annotated symbolic el-
ements with structured prompts for art commen-
tary, evaluating VLM outputs for semantic align-
ment with MHEB using vector-space and rubric-
based metrics, addressing a gap in assessing image-
conditioned cultural reasoning.
Lack of Comparative Cultural Interventions
Across Models.
Surveys (Guo et al., 2023) dis-
cuss LLM limitations in nuanced discourse, but
few studies compare model responsiveness to struc-
tured cultural interventions. Our empirical evalua-
tion shows persona and knowledge base interven-
tion improves symbolic reasoning and argumenta-
tive coherence by over 20–30%, highlighting epis-
temic alignment’s role beyond fluency. This cross-
model, capability-specific analysis distinguishes
our work.
3
Methodology
This research aims to comprehensively evaluate
Visual Language Models (VLMs) capabilities in
generating critiques for traditional Chinese paint-
ing, assessing their understanding of image content,
commentary quality, and adaptability to guided
perspectives. The workflow involves: Framework
Construction, developing a quantitative analytical

--- Page 3 ---

Figure 1: Overview of the VULCA framework, illustrat-
ing its components and their interactions for structured
evaluation and intervention in art criticism.
framework from human expert commentaries, in-
cluding defining evaluative dimensions and critic
personas; VLM evaluation experiment design, cre-
ating structured protocols for VLM critique gen-
eration under conditions like persona-based and
baseline prompting; and experimentation and re-
sult analysis, implementing experiments, collect-
ing VLM critiques, and analyzing them with the
developed framework to assess capabilities and in-
tervention impacts. Figure 1 provides an overview
of this framework and its components.
A cornerstone is the quantitative framework
benchmark for VLM critiques, built upon human
expert commentaries on Chinese art. To ensure
objective, reproducible, and fine-grained evalua-
tion, an automated capability assessment frame-
work was developed. This involves feature extrac-
tion, multi-dimensional capability scoring, profile
assignment, and visualization, using a zero-shot
classification model for fine-grained evaluative la-
bels. The scoring covers painting element recogni-
tion, Chinese painting understanding, and language
usage, each with a dedicated rubric. This struc-
tured, rule-based approach enhances objectivity
and facilitates large-scale benchmarking (Jiang and
Chen, 2025; Hayashi et al., 2025).
3.1
MHEB Construction and Annotation
Process
Our three-dimensional evaluation framework syn-
thesizes Eastern and Western art criticism tradi-
tions with modern museum documentation stan-
dards into the three major dimensions of Evaluative
Stance, Feature Focus, and Commentary Quality.
The framework draws from:
(1) Chinese Art Theory: Building on Xie He’s
Six Canons (六法, 550 CE) (Xie, 550), particu-
larly the concepts of “spirit resonance” (气韵生
动) and “bone method” (骨法用笔), which inform
our Feature Focus dimension’s emphasis on brush-
work technique, artistic conception, and emotional
expression.
(2) Western Art Historical Methods: Incorpo-
rating Baxandall’s “inferential criticism” (Baxan-
dall, 1985) and Gombrich’s psychological ap-
proach (Gombrich, 1960), which contribute to our
Evaluative Stance dimension through categories
like comparative analysis, theoretical construction,
and critical inquiry.
(3) Museum Documentation Standards: Fol-
lowing international cataloging frameworks from
ICOM-CIDOC (International Council of Muse-

--- Page 4 ---

ums, 2022) and practices from the Palace Mu-
seum Beijing, National Palace Museum Taipei, and
Metropolitan Museum of Art (The Metropolitan
Museum of Art, 2021), which standardize descrip-
tive categories for artwork documentation. These
inform our systematic approach to feature extrac-
tion and the structured nature of our Commentary
Quality dimension.
This synthesis creates a culturally-informed yet
methodologically rigorous framework that captures
both the technical aspects emphasized in Western
criticism (e.g., composition, color theory) and the
philosophical-spiritual dimensions central to Chi-
nese art evaluation (e.g., artistic conception, sym-
bolic meaning). The MHEB was therefore system-
atically constructed through the following process:
Data Collection. We collected 163 expert com-
mentaries from authoritative sources including mu-
seum catalogs from the Palace Museum Beijing,
National Palace Museum Taipei, and Metropolitan
Museum of Art, as well as peer-reviewed art history
journals and monographs by recognized scholars
specializing in Qing court painting. Each commen-
tary averages 500-800 Chinese characters and pro-
vides in-depth analysis of specific paintings from
the “Twelve Months” series. The annotation pro-
cess generated 558 total annotation instances (163
texts × 3 annotators plus quality control samples),
which were consolidated into 163 final records after
resolving disagreements.
Expert Sources.
The 163 commentaries in
MHEB were extracted from scholarly publications
by 9 distinguished art historians specializing in
Chinese painting and Qing court art. The corpus
includes: Xue Yongnian (薛永年, 17 texts from
two monographs), Wang Di (汪涤, 28 texts), Yang
Danxia (杨丹霞, 28 texts), Nie Chongzheng (聂崇
正, 15 texts), Shan Guoqiang (单国强, 18 texts),
Li Shi (李, 17 texts), Xu Jianrong (徐建融, 17
texts), Zhu Wanzhang (朱万章, 11 texts), and Chen
Yunru (陈韵如, 12 texts). These experts represent
major institutions including the Palace Museum
Beijing, National Palace Museum Taipei, and lead-
ing Chinese art history departments, ensuring di-
verse yet authoritative perspectives on Giuseppe
Castiglione’s “Twelve Months” series.
Annotation Process.
Three annotators with
graduate-level training in Chinese art history in-
dependently labeled each commentary. Annotators
were provided with a 20-page annotation guideline
detailing the three evaluation dimensions (Evalua-
tive Stance, Feature Focus, Commentary Quality)
and their respective sub-categories. Each annotator
spent approximately 15-20 minutes per commen-
tary, assigning scores for all 38 primary feature la-
bels using a 0-1 continuous scale based on presence
and prominence, from which 9 additional analyti-
cal dimensions were derived. Annotation was per-
formed independently using a custom web-based
interface, with randomized presentation order to
minimize bias.
Quality Control Measures. To ensure anno-
tation quality throughout the process, we imple-
mented multiple control mechanisms: (1) 20%
of commentaries were double-annotated to mon-
itor consistency; (2) bi-weekly calibration ses-
sions were held over the 3-month annotation period
where annotators discussed challenging cases and
aligned their understanding; (3) continuous mon-
itoring tracked annotator performance and drift.
These measures ensured that the annotation pro-
cess remained consistent and reliable throughout
the data collection period.
Inter-Annotator Agreement (IAA). To quanti-
tatively assess the reliability of our annotations,
we calculated inter-annotator agreement using
two complementary metrics. For categorical la-
bels (e.g., stance categories), we computed Fleiss’
kappa (Fleiss, 1971), which measures agreement
beyond chance for multiple raters. For continuous
scores (e.g., feature prominence ratings from 0-1),
we calculated the intraclass correlation coefficient
(ICC) (Shrout and Fleiss, 1979), which assesses the
consistency of quantitative measurements across
raters. The average Fleiss’ kappa across stance
categories was 0.78, indicating substantial agree-
ment according to Landis and Koch’s interpreta-
tion scale. The ICC for feature prominence scores
reached 0.82, demonstrating excellent reliability.
When disagreements occurred (defined as κ < 0.6
for specific labels), they were resolved through
discussion, with a senior art historian serving as
arbiter for persistent conflicts. The stable inter-
rater agreement (κ variation < 0.05 across time)
validated the effectiveness of our quality control
measures. Final dataset statistics show balanced
representation across different evaluative stances
(Historical: 31%, Aesthetic: 28%, Technical: 23%,
Comparative: 18%) and comprehensive coverage
of feature focus.

--- Page 5 ---

Figure 2: T-SNE visual representation of human expert art commentaries.
3.2
Feature Engineering from Human Expert
Critiques
Framework foundation relies on human expert
commentaries, significantly from Giuseppe Cas-
tiglione’s (Lang Shining, 郎世宁) “Twelve Months”
(十二月令图) series—Qing imperial court paint-
ings fusing Chinese and Western traditions. To en-
hance model training and evaluation, a sliding win-
dow cropping strategy (640×640 pixel sub-images)
was applied to these high-resolution images, aug-
menting data diversity and granularity for improved
VLM detail recognition and evaluation accuracy,
a common practice in computer vision (e.g., (Lin
et al., 2014; Krishna et al., 2017)).
We employed a zero-shot classification model
to systematically extract evaluative characteristics.
Specifically, we used the multilingual BART-large-
mnli model (Lewis et al., 2020; Williams et al.,
2018), which has been fine-tuned on natural lan-
guage inference tasks and can classify text into
arbitrary categories without task-specific training.
For each commentary text, the model computes the
probability of belonging to each predefined label
using the entailment paradigm. Given a text T and
a label L, the model evaluates the hypothesis “This
text is about L” and outputs a softmax probabil-
ity score p(L|T) ∈[0, 1]. We apply this process
across 38 labels spanning three dimensions: Evalu-
ative Stance (10 labels, e.g., “Historical Research”,
p = 0.85), Feature Focus (17 labels, e.g., “Use of
Color”, p = 0.72), and Commentary Quality (11
labels, e.g., “Profound Insight”, p = 0.68). Fur-
thermore, we complemented this set of 38 labels
with 9 additional labels representing higher level
features: 5 profile alignment scores derived from
clustering analysis of the 38 primary features, and 4
supplementary analytical dimensions for enhanced
discrimination between critique styles.
Thresholds for binary classification were empiri-
cally determined through validation on a held-out
subset: labels with p > 0.5 are considered present,
while prominence levels are captured by the contin-
uous scores. This comprehensive 47-dimensional
feature vector (38 primary features plus 9 derived
dimensions) enables nuanced quantitative compar-
ison and clustering. Appendix C.5 provides com-
plete list of all 47 dimensions: the 38 primary labels
and 9 derived analytical dimensions. Figure 2 visu-
alizes the MHEB semantic distribution from these
features.
The zero-shot classification model serves as an
analytical tool for deconstructing expert texts and
building our evaluation framework, distinct from
the VLMs (e.g., Gemini 2.5 Pro, Qwen-VL) evalu-
ated later.
3.3
Evaluation of Dimensions and Label
System
The three dimensions of our framework (i.e., Eval-
uative Stance, Feature Focus, and Commentary
Quality) were derived from multiple sources: (1)
traditional Chinese painting theory, particularly

--- Page 6 ---

Xie He’s “Six Principles of Painting” (谢赫六
法) (Acker, 1954) which emphasizes spirit reso-
nance (气韵生动), bone method (骨法用笔), and
correspondence to nature (应物象形); (2) West-
ern art criticism frameworks from Panofsky’s three
levels of meaning (Panofsky, 1955) and Wölfflin’s
formal analysis principles (Wölfflin, 1950); (3) con-
sultations with curators from the Palace Museum
and Metropolitan Museum who validated the rele-
vance of these dimensions for Qing court painting
analysis; and (4) empirical analysis of recurring
patterns in our collected expert commentaries.
Evaluative Stance characterizes the rhetorical or
evaluative position taken by the commentator (e.g.,
historical interpretation, praise, or critique). Fea-
ture Focus identifies the specific visual or contex-
tual aspects discussed in the commentary (e.g., line
quality, symbolism, spatial composition). Com-
mentary Quality captures the analytical depth and
logical structure of the commentary, ranging from
clear, well-argued insights to superficial or biased
remarks. Furthermore, each dimension comprises
a set of fine-grained subcategories with bilingual
English–Chinese mappings. Full definitions and
label lists are provided in Appendix C.5.
3.4
Construction and Definition of Critic
Personas
To capture holistic critique style and depth beyond
granular features, we constructed “critic personas”
representing archetypal critical perspectives. Their
development was data-driven, analyzing features
from human expert commentaries, complemented
by art history domain expertise. Five core personas
were defined: Comprehensive Analyst (博学通
论型), Historically Focused Critic (历史考据型),
Technique & Style Focused Critic (技艺风格型),
Theory & Comparison Focused Critic (理论比较
型), and General Descriptive Profile (泛化描述型).
These five core personas represent data-driven eval-
uation categories derived from clustering analysis
of human expert features, serving as benchmarks
for assessing whether VLM outputs align with rec-
ognizable expert critique patterns.
Each persona is quantitatively defined by rules
and thresholds based on zero-shot classification
feature scores. This rule-based matching objec-
tively assigns commentaries (human or VLM) to
personas. Persona definition and matching rely on
explicit features and rule-based logic, not primarily
direct semantic embedding of raw text. Dimension-
ality reduction (t-SNE/UMAP) visualizes commen-
tary and persona distribution in the feature space,
not for initial persona vector generation.
3.5
Task Definition
This quantitative framework guided experiments
evaluating selected VLMs (e.g., Gemini 2.5 Pro,
Qwen-VL). The core task required VLMs to gen-
erate commentary on provided traditional Chinese
painting images. Experiments typically involved
structured, multi-round interactions for each VLM
per image, including persona-based and baseline
Q&A rounds.
Inputs were multifaceted: (i) high-definition
“Monthly Images” (sometimes segmented); (ii) pre-
defined “Persona Cards” (adapting the persona
simulation approach from (Jiang et al., 2024) to
cultural domain expertise) serving as experimen-
tal interventions-distinct from the five evaluaction
personas above, these eight cultural perspective
prompts guided VLM generation analysis: Mama
Zola (佐拉妈妈), Professor Elena Petrova (埃琳
娜·佩特洛娃教授), Okakura Kakuzo (冈仓天心),
Brother Thomas (托马斯修士), John Ruskin (约
翰·罗斯金), Su Shi (苏轼), Guo Xi (郭熙), and Dr.
Aris Thorne (阿里斯·索恩博士); (iii) standardized
prompt templates (Nayak et al., 2024); and (iv) op-
tional domain knowledge resources (Zhang et al.,
2025b; Bin et al., 2024). Persona guidance aimed
to assess VLM capability to simulate diverse per-
spectives and analytical styles (Zhang et al., 2025a).
See Appendix B for a detailed summary of each
critic persona included in our study. To avoid con-
fusion, we distinguish between the use of personas
at two different levels: the five core personas de-
scribed in the previous sub-section are data-driven
evaluation categories for classifying generated cri-
tiques based on feature patterns, while the eight
persona cards are cultural perspective prompts used
to guide VLM generation during experiments. The
former evaluates outputs, while the latter shapes
inputs.
The VLM critique evaluation dimensions cover:
Painting Element Recognition (5-point scale); Chi-
nese Painting Understanding (7-point scale); and
Chinese Language Usage (5-point scale). Prompt
design, particularly for structured commentary, tar-
geted these dimensions.
3.6
Vector Space Representation and
Visualization
To compare human and VLM critiques, we con-
verted feature scores (Evaluative Stance, Feature

--- Page 7 ---

Focus, Commentary Quality) from both into nu-
merical vectors. These vectors were projected into
a 2D space using t-SNE for visualisation (van der
Maaten and Hinton, 2008), enabling assessment of
semantic similarity and distributional differences.
Figure 3 (left) illustrates such a comparative vi-
sualization, showing the semantic distribution of
human expert commentaries versus baseline VLM-
generated commentaries, highlighting their initial
semantic gap.
3.7
Multi-Model Comparative Evaluation
To comprehensively assess the capabilities of state-
of-the-art large language and vision-language mod-
els, we conducted a systematic comparative eval-
uation across four representative models: Google
Gemini 2.5 Pro, Meta Llama-3.1-8B-Instruct, Meta
Llama-4-Scout-17B-16E-Instruct, and Qwen-2.5-
VL-7B. All models were evaluated using the same
experimental protocol, dataset splits, and evalua-
tion metrics to ensure fair and reproducible com-
parison.
3.8
Quantitative Modeling and Formalisms
This section details the key mathematical formula-
tions used in our analytical framework, covering
semantic representation, comparative metrics, and
the profile matching algorithm.
Semantic Embedding.
Conceptually:
vd = SentenceTransformer(documentd)
(1)
Where (vd
∈
RN) (e.g., (N
=
1024) for
BAAI/bge-large-zh-v1.5 (Xiao et al., 2024)).
Average Quality Score for Radar Chart (¯qj,G).
For a quality dimension j and a group of documents
G (e.g., Human Experts, VLM Baseline):
¯qj,G =
1
|NG|
X
d∈NG
sj,d
(2)
Where sj,d is the score of document d on quality
dimension j, and |NG| is the number of documents
in group G.
Centroid Calculation in Dimensionality Re-
duced Space (cp).
For a profile/condition p, its
centroid in a 2D space (e.g., t-SNE):
cp = (¯xp, ¯yp) =

1
|Dp|
X
d∈Dp
xd,
1
|Dp|
X
d∈Dp
yd


(3)
Where (xd, yd) are the 2D coordinates of document
d belonging to profile/condition p, and |Dp| is the
number of documents in profile/condition p.
Cohen’s d (Effect Size) (Cohen, 1988).
To mea-
sure the standardized difference between two group
means ( ¯X1, ¯X2):
d =
¯X1 −¯X2
sp
(4)
Where sp is the pooled standard deviation:
sp =
s
(n1 −1)s2
1 + (n2 −1)s2
2
n1 + n2 −2
(5)
And here n1, n2 are the sample sizes of group 1 and
group 2, while s2
1, s2
2 are the variances of group 1
and group 2.
Stance Contribution Formula (SC).
We com-
pute the stance contribution SC using the following
conditions:
SC =

























sactual−smin_rule
smax_rule−smin_rule ,
if Lactual = Lrule,
sactual ≥smin_rule,
smax_rule ̸= smin_rule
1,
if Lactual = Lrule,
sactual ≥smin_rule,
smax_rule = smin_rule
0,
otherwise
Where SC is the stance contribution score, Lactual
is the actual stance label of the text, Lrule is the
required stance label in the profile rule, sactual is the
actual stance score, and smin_rule, smax_rule represent
the required range.
4
Results
We present our results from semantic alignment, ca-
pability profiling, and the effects of persona-guided
interventions on VLMs. All evaluations are made
with respect to the MHEB, using both vector-space
analysis and rubric-based scoring.
4.1
Semantic Divergence from Expert
Commentary
Baseline VLM outputs exhibit significant diver-
gence from human expert commentaries. As shown
in Figure 3 (left), expert texts cluster tightly in se-
mantic space, while VLM outputs are more dis-
persed and form distinct clusters. Profile-based
visualizations (Figure 4 (right)) further confirm

--- Page 8 ---

Figure 3: Impact of Persona and Knowledge Base Interventions on VLM Critiques: A comprehensive analysis
comparing intervened VLM outputs with a human expert benchmark. Left: t-SNE and KDE plots visualize the
semantic distribution of critiques from different sources (human experts, baseline VLMs, intervened VLMs). Right:
A radar chart compares average capability scores across dimensions like Profound Insight and Logical Clarity.
this divergence: baseline models frequently align
with generic or technique-oriented profiles, rarely
matching complex expert personas.
4.2
Capability Profile Differences
Human expert commentaries, as quantified by our
ZSL analysis (see Table 4 in Appendix D.3 for
full data which Figure 4 (left) visualizes), empha-
size symbolic and historical interpretation (e.g.,
average scores of 0.676 in Historical Context and
0.661 in Symbolism) but notably less on technical
aspects like Brushwork Technique (0.199). They
also exhibit high subjectivity and non-linear reason-
ing (e.g., 0.674 in Subjective View, 0.093 in Clear
Logic, as detailed in Table 7).
In contrast, baseline VLMs show varied per-
formance. For instance, Llama-4-Scout-17B-16E-
Instruct achieves high scores in Historical Context
(0.710) and Symbolism (0.758), comparable to or
exceeding human experts. Qwen-2.5-VL-7B also
performs well in these areas (0.650 and 0.773 re-
spectively) and particularly excels in Artistic Con-
ception (0.891) and Brushwork Technique (0.937),
the latter being dramatically higher than the hu-
man expert average of 0.199 for this feature (see
Table 4). Gemini-2.5pro shows strength in Layout
and Structure (0.874), while Meta-Llama-3.1-8B-
Instruct generally presents lower scores across sev-
eral nuanced dimensions like Historical Context
(0.366) and Symbolism (0.529). These differences
are summarized in Figure 4 (left) and supported by
the radar plots in Figure 3 (right).
4.3
Effectiveness of Persona-Guided
Interventions
Persona-guided prompting, especially when sup-
ported by domain knowledge, substantially im-
proves VLM outputs. Figure 3 (right) illustrates
that Qwen-2.5-VL improves scores across key
dimensions—e.g., Profound Insight (from 0.31 to
0.61), Strong Argumentation (0.33 to 0.66), and
Detailed Analysis (0.33 to 0.70), with full details
available in Table 7. These results indicate stronger
alignment with expert-style reasoning. Alignment
improvements are also visible in profile scores (Fig-
ure 4 (center)), with intervened outputs matching
sophisticated expert types like “Comprehensive An-
alyst” (e.g., Qwen-2.5-VL-7B achieving an align-
ment score of 0.778 for this profile, as detailed in
Table 5) more closely than baseline.
4.4
Cross-Model Comparison and
Configurations
Qwen-2.5-VL and LLaMA-4-Scout-17B demon-
strate strong performance under intervention. In
Figure 4 (left), which visualizes data from Ta-
ble 4, both models demonstrate high scores in ar-
eas like Artistic Conception (Qwen: 0.891, Llama-
4: 0.851), Brushwork Technique (Qwen: 0.937,
Llama-4: 0.903), and Layout and Structure (Qwen:
0.895, Llama-4: 0.916). Their profile alignment
in Figure 4 (center) confirms their ability to emu-
late multiple expert types. The overall performance
rankings, detailed in Table 1, reveal that the Qwen-
2.5-VL-7B model, when guided by the Mama Zola

--- Page 9 ---

Figure 4: Profiling Summary: A comparative visualization of Human Experts vs. VLMs across key textual features
(left), mean profile alignment scores (center), and t-SNE projection of profile vectors (right).
Table 1: Top performing model and persona combinations across capability dimensions. Expert Alignment measures
the degree to which model outputs match the characteristic patterns of our five expert profiles.
Rank
Configuration
Composite Score
Expert Alignment
1
Qwen-2.5-VL-7B + Mama Zola (佐拉妈妈) + KB
9.2/10
100%
2
meta-llama_Llama-4-Scout-17B-16E-Instruct + John Ruskin (约翰·罗斯金) + KB
8.9/10
97%
3
meta-llama_Llama-4-Scout-17B-16E-Instruct + Mama Zola (佐拉妈妈) + KB
8.7/10
95%
4
meta-llama_Llama-4-Scout-17B-16E-Instruct + Brother Thomas (托马斯修士) + KB
8.5/10
92%
5
meta-llama_Llama-4-Scout-17B-16E-Instruct + Su Shi (苏轼) + KB
8.5/10
92%
–
Human Expert Benchmark (avg)
9.2/10
100%
persona and an external knowledge base, achieved
the top composite score (9.2/10) and expert align-
ment (100%).
The Expert Alignment metric quantifies how
closely a model’s output matches our five prede-
fined expert profiles (Comprehensive Analyst, His-
torically Focused Critic, etc.). For each generated
commentary, we compute its 47-dimensional fea-
ture vector (38 primary features plus 9 derived di-
mensions) using the zero-shot classification model.
We then calculate the cosine similarity between this
vector and the centroid vectors of each expert pro-
file, derived from human expert commentaries in
MHEB. The commentary is assigned to the profile
with highest similarity (threshold > 0.7).
The percentage represents the proportion of out-
puts successfully matched to an expert profile. A
100% alignment indicates that all of the model’s
outputs under that configuration strongly resemble
at least one expert archetype, with similarity scores
exceeding 0.7. Lower percentages indicate outputs
that fall between profiles or lack distinctive expert
characteristics. This metric helps assess whether
interventions guide models toward recognizable
expert-like critique patterns rather than generic re-
sponses.
These results show that interpretive capability in
VLMs can be substantially improved by structured
prompting and domain-specific conditioning. Cul-
turally aligned personas are particularly effective,
highlighting the potential of the VULCA frame-
work to guide VLMs toward expert-level reasoning
in specialized domains. The distribution of VLM
outputs in semantic space, based on their profile
scores (centroids detailed in Appendix Table 3),
also shifts with interventions, indicating changes
in their overall analytical posture.
5
Conclusion
This research introduced VULCA, a quantitative
framework for evaluating VLM-generated critiques
of traditional Chinese painting. Our experiments
demonstrate that persona and knowledge-based
interventions significantly enhance VLM perfor-
mance, achieving closer alignment with human
expert standards. The study underscores the im-
portance of culturally grounded approaches for de-
veloping VLMs capable of nuanced engagement
with specialized domains, paving the way for more
sophisticated AI-assisted cultural analysis across
diverse contexts.
Acknowledgments
We thank the anonymous reviewers for their insight-
ful comments and constructive suggestions that sig-
nificantly improved this paper. We are grateful
to the three annotators with graduate-level train-
ing in Chinese art history who contributed to es-
tablishing our human expert benchmark dataset,

--- Page 10 ---

dedicating 15-20 minutes per commentary to en-
sure high-quality annotations. We acknowledge
the Palace Museum Beijing, National Palace Mu-
seum Taipei, and the Metropolitan Museum of Art
for providing access to their museum catalogs and
documentation of Giuseppe Castiglione’s “Twelve
Months” series, which formed the foundation of
our expert commentary corpus. We also thank the
art history scholars whose peer-reviewed publica-
tions and monographs on Qing court painting pro-
vided essential domain expertise for this work.
We acknowledge the use of AI-powered tools
in this research. Claude Code assisted with code
development and debugging throughout the experi-
mental implementation. Claude also provided En-
glish language refinement and editorial suggestions
during the manuscript preparation. All scientific
insights, experimental design, and final editorial
decisions remained under full human control and
responsibility.
Limitations
While our VULCA framework demonstrates signif-
icant improvements in VLM cultural adaptability,
several limitations should be acknowledged. Be-
yond the specific points enumerated below, this
study confronts broader limitations inherent in cur-
rent AI capabilities and evaluation methodologies.
Models, despite interventions, may still reflect bi-
ases from their foundational training data or strug-
gle with true generalization to vastly different cul-
tural artifacts or artistic forms beyond the Chinese
paintings studied.
Dataset and Domain Limitations. Our evalua-
tion is based on 163 expert commentaries from a
single artistic tradition (Qing Dynasty court paint-
ings).
We focused exclusively on the “Twelve
Months” series by Giuseppe Castiglione. Although
carefully curated, this dataset may not fully capture
the diversity of Chinese art criticism or generalize
to other artistic traditions or art forms (calligraphy,
sculpture, contemporary art). The annotations on
input images may influence VLM outputs in ways
that differ from how they would process unanno-
tated images. Cultural nuances may be lost in trans-
lation between Chinese and English, particularly
for specialized art terminology.
Model Selection and Evaluation. We evaluated
a limited set of VLMs due to computational con-
straints. Newer models or those specifically trained
on art history might show different patterns of im-
provement. Our API-based approach precludes
deep analysis of models’ internal mechanisms. De-
spite our standardized approach, VLMs may ex-
hibit sensitivity to minor variations in prompt phras-
ing or structure, affecting the consistency of results.
Our study represents a snapshot of current VLM
capabilities, which are rapidly evolving.
Methodological Constraints. Our vector space
analysis relies on a specific embedding model
(BAAI/bge-large-zh-v1.5), and results might vary
with different models.
Visualizations using di-
mensionality reduction techniques (t-SNE, UMAP)
inevitably lose some information from the orig-
inal high-dimensional space.
Cosine similarity
and other metrics provide useful quantitative com-
parisons but may not perfectly align with human
judgments of semantic similarity in specialized do-
mains. The structured format may artificially con-
strain both human and VLM expression patterns,
potentially reducing stylistic diversity and creative
interpretation.
Evaluation Subjectivity. Despite our system-
atic approach using zero-shot classification and
rule-based persona matching, some aspects of art
criticism evaluation remain inherently subjective.
The choice of feature dimensions and quality met-
rics reflects particular theoretical perspectives that
may not be universally accepted. The template-
based section may artificially boost VLM perfor-
mance by providing explicit categories and prompts
that guide responses. Converting existing human
expert commentaries to our structured format re-
quired interpretation and adaptation, potentially
introducing biases.
Cultural Complexity. Art criticism involves
tacit knowledge, cultural intuition, and embodied
experience that current computational approaches
cannot fully capture. Our metrics may miss subtle
aspects of genuine cultural understanding versus
sophisticated pattern matching. The very tools of
our framework, such as the zero-shot classifier for
feature extraction and the predefined granularity of
persona cards and knowledge bases, introduce their
own constraints and potential blind spots. A signif-
icant challenge remains in distinguishing between
genuine understanding or deep cultural adaptability
and sophisticated pattern matching or role-play by
the models.

--- Page 11 ---

References
W.R.B. Acker. 1954. Some T’ang and Pre-t’ang Texts
on Chinese Painting. Sinica Leidensia. E.J. Brill.
Michael Baxandall. 1985. Patterns of Intention: On the
Historical Explanation of Pictures. Yale University
Press, New Haven.
Yi Bin, Wenhao Shi, Yujuan Ding, Zhiqiang Hu, Zheng
Wang, Yang Yang, See-Kiong Ng, and Heng Tao
Shen. 2024. Gallerygpt: Analyzing paintings with
large multimodal models. In Proceedings of the 32nd
ACM International Conference on Multimedia, MM
’24, pages 7734–7743, New York, NY, USA. Associ-
ation for Computing Machinery.
Susan Bush. 1971. The Chinese Literati on Painting: Su
Shih (1037-1101) to Tung Ch’i-ch’ang (1555-1636).
Harvard University Press.
Jacob Cohen. 1988. Statistical Power Analysis for the
Behavioral Sciences, 2nd edition. Lawrence Erlbaum
Associates, Hillsdale, NJ.
Joseph L Fleiss. 1971. Measuring nominal scale agree-
ment among many raters. Psychological Bulletin,
76(5):378–382.
Chaoyou Fu, Peixian Chen, Yunhang Shen, Yulei
Qin, Mengdan Zhang, Xu Lin, Jinrui Yang, Xiawu
Zheng, Ke Li, Xing Sun, Yunsheng Wu, Rongrong Ji,
Caifeng Shan, and Ran He. 2025. MME: A compre-
hensive evaluation benchmark for multimodal large
language models. In The Thirty-ninth Annual Con-
ference on Neural Information Processing Systems
Datasets and Benchmarks Track.
Ernst H. Gombrich. 1960. Art and Illusion: A Study in
the Psychology of Pictorial Representation. Prince-
ton University Press, Princeton.
Zishan Guo, Renren Jin, Chuang Liu, Yufei Huang, Dan
Shi, Supryadi, Linhao Yu, Yan Liu, Jiaxuan Li, Bo-
jian Xiong, and Deyi Xiong. 2023. Evaluating large
language models: A comprehensive survey. Preprint,
arXiv:2310.19736.
Kazuki Hayashi, Kazuma Onishi, Toma Suzuki, Yusuke
Ide, Seiji Gobara, Shigeki Saito, Yusuke Sakai, Hide-
taka Kamigaito, Katsuhiko Hayashi, and Taro Watan-
abe. 2025. IRR: Image review ranking framework
for evaluating vision-language models. In Proceed-
ings of the 31st International Conference on Compu-
tational Linguistics, pages 9939–9956, Abu Dhabi,
UAE. Association for Computational Linguistics.
International Council of Museums. 2022. Cidoc stan-
dards guidelines. Accessed: 2024.
Hang Jiang, Xiajie Zhang, Xubo Cao, Cynthia Breazeal,
Deb Roy, and Jad Kabbara. 2024. PersonaLLM: In-
vestigating the ability of large language models to
express personality traits. In Findings of the Associ-
ation for Computational Linguistics: NAACL 2024,
pages 3605–3627, Mexico City, Mexico. Association
for Computational Linguistics.
Ruixiang Jiang and Chang Wen Chen. 2025. Multi-
modal llms can reason about aesthetics in zero-shot.
In Proceedings of the 33rd ACM International Con-
ference on Multimedia, MM ’25, pages 6634–6643,
New York, NY, USA. Association for Computing
Machinery.
Ranjay Krishna, Yuke Zhu, Oliver Groth, Justin John-
son, Kenji Hata, Joshua Kravitz, Stephanie Chen,
Yannis Kalantidis, Li-Jia Li, David A. Shamma,
Michael S. Bernstein, and Li Fei-Fei. 2017.
Vi-
sual genome: Connecting language and vision us-
ing crowdsourced dense image annotations. Interna-
tional Journal of Computer Vision, 123(1):32–73.
Mike Lewis, Yinhan Liu, Naman Goyal, Marjan
Ghazvininejad, Abdelrahman Mohamed, Omer Levy,
Veselin Stoyanov, and Luke Zettlemoyer. 2020.
BART: Denoising sequence-to-sequence pre-training
for natural language generation, translation, and com-
prehension. In Proceedings of the 58th Annual Meet-
ing of the Association for Computational Linguistics,
pages 7871–7880, Online. Association for Computa-
tional Linguistics.
Bohao Li, Yuying Ge, Yixiao Ge, Guangzhi Wang, Rui
Wang, Ruimao Zhang, and Ying Shan. 2024. Seed-
bench: Benchmarking multimodal large language
models. In Proceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition (CVPR),
pages 13299–13308.
Tsung-Yi Lin, Michael Maire, Serge J. Belongie, James
Hays, Pietro Perona, Deva Ramanan, Piotr Dollár,
and C. Lawrence Zitnick. 2014. Microsoft COCO:
Common objects in context. In Computer Vision –
ECCV 2014, volume 8693 of Lecture Notes in Com-
puter Science, pages 740–755, Cham. Springer.
Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae
Lee. 2023. Visual Instruction Tuning. In Advances in
Neural Information Processing Systems, volume 36,
pages 34892–34916. Curran Associates, Inc.
Yuan Liu, Haodong Duan, Yuanhan Zhang, Bo Li,
Songyang Zhang, Wangbo Zhao, Yike Yuan, Jiaqi
Wang, Conghui He, Ziwei Liu, Kai Chen, and Dahua
Lin. 2024. MMBench: Is your multi-modal model
an all-around player? In Computer Vision – ECCV
2024, volume 15064 of Lecture Notes in Computer
Science, pages 216–233, Cham. Springer.
Shravan Nayak, Kanishk Jain, Rabiul Awal, Siva
Reddy, Sjoerd Van Steenkiste, Lisa Anne Hendricks,
Karolina Stanczak, and Aishwarya Agrawal. 2024.
Benchmarking vision language models for cultural
understanding. In Proceedings of the 2024 Confer-
ence on Empirical Methods in Natural Language
Processing, pages 5769–5790, Miami, Florida, USA.
Association for Computational Linguistics.
Erwin Panofsky. 1955.
Meaning in the Visual Arts.
Doubleday.
Murray Shanahan, Kyle McDonell, and Laria Reynolds.
2023. Role play with large language models. Nature,
623(7987):493–498.

--- Page 12 ---

Patrick E Shrout and Joseph L Fleiss. 1979. Intraclass
correlations: uses in assessing rater reliability. Psy-
chological Bulletin, 86(2):420–428.
Osvald Sirén. 1936. The Chinese on the Art of Painting:
Texts by the Painter-Critics, from the Han through
the Ch’ing Dynasties. Peiping: Henri Vetch.
The Metropolitan Museum of Art. 2021. Archives pro-
cessing and cataloging manual. Technical report, The
Metropolitan Museum of Art Archives.
Laurens van der Maaten and Geoffrey Hinton. 2008.
Visualizing data using t-sne. Journal of Machine
Learning Research, 9(86):2579–2605.
Noah Wang, Z.y. Peng, Haoran Que, Jiaheng Liu,
Wangchunshu Zhou, Yuhan Wu, Hongcheng Guo,
Ruitong Gan, Zehao Ni, Jian Yang, Man Zhang,
Zhaoxiang Zhang, Wanli Ouyang, Ke Xu, Wenhao
Huang, Jie Fu, and Junran Peng. 2024. RoleLLM:
Benchmarking, eliciting, and enhancing role-playing
abilities of large language models. In Findings of
the Association for Computational Linguistics: ACL
2024, pages 14743–14777, Bangkok, Thailand. As-
sociation for Computational Linguistics.
Yuhan Wang. 2024. The Changes of "Shen" and "Yi" in
Chinese Painting Aesthetics: From Gu Kaizhi to Ni
Zan. Open Access Library Journal, 11(4):1–6.
Adina Williams, Nikita Nangia, and Samuel Bowman.
2018. A broad-coverage challenge corpus for sen-
tence understanding through inference. In Proceed-
ings of the 2018 Conference of the North American
Chapter of the Association for Computational Lin-
guistics: Human Language Technologies, Volume
1 (Long Papers), pages 1112–1122, New Orleans,
Louisiana. Association for Computational Linguis-
tics.
Heinrich Wölfflin. 1950. Principles of Art History: The
Problem of the Development of Style in Later Art.
Dover Publications.
Shitao Xiao, Zheng Liu, Peitian Zhang, Niklas Muen-
nighoff, Defu Lian, and Jian-Yun Nie. 2024. C-pack:
Packed resources for general chinese embeddings. In
Proceedings of the 47th International ACM SIGIR
Conference on Research and Development in Infor-
mation Retrieval, SIGIR ’24, pages 641–649, New
York, NY, USA. Association for Computing Machin-
ery.
He Xie. 550. Guhua Pinlu [The Record of the Classifica-
tion of Old Painters]. [Manuscript], China. Original
text circa 550 CE. English translation in: Bush, Susan
and Hsio-yen Shih. Early Chinese Texts on Painting.
Cambridge: Harvard University Press, 1985, pp. 39-
41.
Haoxuan You, Haotian Zhang, Zhe Gan, Xianzhi Du,
Bowen Zhang, Zirui Wang, Liangliang Cao, Shih-Fu
Chang, and Yinfei Yang. 2024. Ferret: Refer and
ground anything anywhere at any granularity. In
The Twelfth International Conference on Learning
Representations.
Zhengqing Yuan, Yunhong He, Kun Wang, Yanfang Ye,
and Lichao Sun. 2024. Artgpt-4: Towards artistic-
understanding large vision-language models with en-
hanced adapter. Preprint, arXiv:2305.07490.
Tuo Zhang, Tiantian Feng, Yibin Ni, Mengqin Cao, Ruy-
ing Liu, Kiana Avestimehr, Katharine Butler, Yanjun
Weng, Mi Zhang, Shrikanth Narayanan, and Salman
Avestimehr. 2025a. Creating a lens of Chinese cul-
ture: A multimodal dataset for Chinese pun rebus
art understanding. In Findings of the Association
for Computational Linguistics: ACL 2025, pages
22473–22487, Vienna, Austria. Association for Com-
putational Linguistics.
Wei Zhang, Kam-Kwai Wong, Biying Xu, Yiwen Ren,
Yuhuai Li, Yingchaojie Feng, Minfeng Zhu, and Wei
Chen. 2025b. CultiVerse: Towards cross-cultural un-
derstanding for paintings with large language model.
In Proceedings of the 33rd ACM International Con-
ference on Multimedia, Dublin, Ireland. Association
for Computing Machinery.
Wenxuan Zhang,
Mahani Aljunied,
Chang Gao,
Yew Ken Chia, and Lidong Bing. 2023. M3exam: A
multilingual, multimodal, multilevel benchmark for
examining large language models. In Thirty-seventh
Conference on Neural Information Processing Sys-
tems Datasets and Benchmarks Track, pages 5484–
5505.
A
Dataset Details
A.1
Lang Shining’s "Twelve Months" Dataset
Our study centers on Giuseppe Castiglione’s
“Twelve Months” series (十二月令图), 12 paint-
ings showing seasonal activities in the Qing im-
perial court. These paintings fuse Chinese and
Western artistic traditions, ideal for cross-cultural
interpretation study. We compiled digital images (6
million pixels) from the National Palace Museum
(Taiwan) digital archives under CC BY 4.0 license.
The dataset includes historical texts and scholarly
analyses in both Chinese and English, from Qing
Dynasty sources and modern scholarship.
B
Persona Definitions
The following eight persona cards were utilized in
this study, each detailed in a separate subsection:
B.1
Mama Zola (佐拉妈妈)
• Basic Information: Elderly West African
oral historian and textile artist (female, born
1955, Senegalese village). Guardian of tribal
wisdom.
• Key Influences/Background: Grew up in
a culture without written records, learning

--- Page 13 ---

history and wisdom through oral traditions,
songs, dances, and rituals.
Textile skills
passed down through generations; her works
are themselves carriers of narrative and his-
tory. Critical of Western museums’ plunder
and misinterpretation of African art.
• Analytical Style and Characteristics: Inter-
prets art from the perspective of community
function, ritual significance, and ancestral con-
nection. Emphasizes the practicality, locality,
and collective creativity of art. Values the sym-
bolic meaning of materials and the spiritual
infusion during the crafting process. Believes
art is part of life, not an isolated "artwork."
• Numeric Attributes (Scale: 1-10):
– Community Culture Perspective: 10
– Oral Tradition Connection: 9
– Decolonization Awareness: 8
– Sensitivity to Craft and Materials: 9
– Spirituality and Rituality: 7
– Acceptance of Western Art Theory: 2
• Language and Expression Style: Language
is simple, vivid, full of storytelling and life
wisdom. Often uses proverbs and metaphors.
Critiques as if telling an ancient story, em-
phasizing emotional connection and collective
memory. Tone is gentle but firm.
• Sample Phrases:
– “Every pattern on this cloth tells the story
of our ancestors, more truly than any
book.”
– “What you call ’artworks,’ we use to cele-
brate harvests and connect the living with
the dead. It is alive, breathing with us.”
– “Those masks in museums, separated
from their dances and songs, are like fish
out of water, soulless.”
– “To dye this indigo thread requires the
moon’s blessing and the earth’s gift; this
color holds the memory of our people.”
– “True beauty is what makes the whole vil-
lage feel warmth and strength, not some-
thing hung on a wall for individual admi-
ration.”
B.2
Okakura Kakuzo (冈仓天心)
• Basic Information:
Prominent Japanese
Meiji era art activist, thinker, and educator
(male, 1863-1913, Yokohama). A founder of
the Tokyo School of Fine Arts (now Tokyo
University of the Arts) and Head of the Chi-
nese and Japanese Art Department at the Mu-
seum of Fine Arts, Boston.
• Key Influences/Background: Dedicated to
reviving and promoting Japanese and Eastern
traditional arts, resisting the blind Westerniza-
tion of the early Meiji Restoration. Deeply
influenced by Eastern philosophy (especially
Zen and Daoism). Authored English works
such as “The Ideals of the East” and "The
Book of Tea," introducing Eastern culture and
aesthetics to the West.
• Analytical Style and Characteristics: Em-
phasized the cultural concept of “Asia is one.”
Valued the spirituality and symbolic mean-
ing of art, believing the core of Eastern art
lies in the “rhythm of life.” Advocated for an
aesthetic of simplicity, subtlety, and harmony
with nature. Possessed a deep understand-
ing of Western art and conducted comparative
studies.
• Numeric Attributes (Scale: 1-10):
– Emphasis on Eastern Spirituality: 10
– Cross-Cultural Comparative Perspective:
9
– Awareness of Traditional Revival: 8
– Interpretation of Symbolic Meaning: 7
– Understanding of Western Art: 7
– Focus on Materials and Craft: 6
• Language and Expression Style: Language
is poetic and philosophical, reflecting both
Eastern and Western cultural literacy. Elegant
prose, adept at interpreting art from a macro-
cultural perspective.
When introducing to
Western readers, often used vivid metaphors
and insightful discussions.
• Sample Phrases:
– “Asia is one. The Himalayas divide, only
to accentuate, two mighty civilisations,
the Chinese with its communism of Con-
fucius, and the Indian with its individual-
ism of the Vedas.”

--- Page 14 ---

– “Teaism is a cult founded on the adora-
tion of the beautiful among the sordid
facts of everyday existence.”
– “The Art of life lies in a constant read-
justment to our surroundings.”
– “In the trembling grey of a breaking
dawn, when the birds were whispering
in mysterious cadence among the trees,
have you not felt that they were talking
to their mates about the untold mystery
of waking life?”
– “True beauty could be discovered only
by one who mentally completed the in-
complete.”
B.3
Professor Elena Petrova (埃琳娜·佩特洛
娃教授)
• Basic Information: Rigorous Russian For-
malist art critic (female, born 1965, St. Peters-
burg). Professor in the Department of Compar-
ative Literature and Art Theory at a university.
• Key Influences/Background: Deeply influ-
enced by Russian Formalist literary theory
(e.g., Shklovsky, Eikhenbaum). Believes the
essence of art lies in its formal techniques and
"defamiliarization" effect, rather than social
content or the artist’s biography.
• Analytical Style and Characteristics: Fo-
cuses on the "literariness" of artworks (or
"artisticness" itself for visual arts). Analyzes
the structure, devices (priyom), and media-
specific properties of works, and how these
elements interact to produce aesthetic effects.
Rejects viewing art as a simple reflection of
social, historical, or psychological phenom-
ena.
• Numeric Attributes (Scale: 1-10):
– Depth of Formal Analysis: 10
– Focus on Defamiliarization Effect: 9
– Sensitivity to Media Properties: 8
– Rejection of Historical/Social Context: 7
– Disregard for Authorial Intent: 8
– Restraint in Emotional Interpretation: 6
• Language and Expression Style: Precise, ob-
jective language, like scientific analysis. Ex-
tensive use of Formalist terminology. Argu-
ments are logically rigorous, with layered dis-
section. Tone is calm and devoid of personal
emotion.
• Sample Phrases:
– “The device is the content of art. We
are concerned not with *what* the artist
says, but *how* it is said, i.e., its ’device’
(priyom)."
– “This painting, through its distortion of
conventional perspective, successfully
creates a ’defamiliarization’ (ostrane-
nie) effect, compelling the viewer to re-
examine familiar objects.”
– “We must treat the work as a self-
sufficient system of signs, analyzing the
tensions and harmonies among its inter-
nal elements, rather than resorting to ex-
ternal biographical or psychological fac-
tors.”
– “So-called ’themes’ or ’ideas’ are merely
motivations for stringing together vari-
ous artistic devices; they are not the core
of artistic analysis itself.”
– “The artistic merit of this piece lies in
its clever orchestration of fundamental
’devices’ (ustanovka) such as color, line,
and composition, not in the narrative
scene it depicts.”
B.4
Brother Thomas (托马斯修士)
• Basic Information: Contemplative hermit
monk and iconographer (male, born 1970, a
monastery on Mount Athos). Dedicated to
preserving ancient Byzantine icon painting
techniques and theology.
• Key Influences/Background: Received spir-
itual and artistic training within the Eastern
Orthodox monastic tradition. Deeply influ-
enced by the Desert Fathers, Neoplatonism,
and icon theology (e.g., St. John of Damas-
cus). Believes art is a window to the divine.
• Analytical Style and Characteristics: Inter-
prets art from theological and spiritual per-
spectives. Focuses on the symbolic meaning
of artworks, archetypes, and their function in
liturgy and prayer. Emphasizes fasting, prayer,
and spiritual concentration during the creative
process. Believes true beauty points to divine
beauty.
• Numeric Attributes (Scale: 1-10):
– Theological Symbolism Interpretation:
10

--- Page 15 ---

– Emphasis on Spiritual Function: 9
– Adherence to Traditional Techniques: 8
– Focus on Image Archetypes: 7
– Evaluation of Secular Art: 3
– Receptiveness to Innovation: 2
• Language and Expression Style: Language
is devout, tranquil, and full of religious
metaphors. Often quotes Scripture and Patris-
tic texts. Commentary focuses on revealing
the divine reality and spiritual guidance be-
hind images. Tone is peaceful, humble, with
mystical overtones.
• Sample Phrases:
– “This icon is not merely a ’depiction’; it
is itself a ’revelation’ of the divine pres-
ence, a window to the unseen world.”
– “One should view an icon with a prayer-
ful heart.
The direction of lines, the
use of color, all follow ancient patristic
norms, guiding the soul upwards.”
– “When creating, the iconographer must
fast and pray, becoming a pure conduit
for the divine light to flow through the
brush.”
– “The gold background symbolizes eter-
nal light; the figures’ ’inverse perspec-
tive’ is not ’unrealistic’ but transcends
worldly vision to present the heavenly
order.”
– “Every detail, from the folds of a robe to
the gesture of a finger, carries profound
theological meaning, a silent sermon.”
B.5
John Ruskin (约翰·罗斯金)
• Basic Information: Leading English art critic
of the Victorian era, social reformer, writer,
and poet (male, 1819-1900, London). Slade
Professor of Fine Art at the University of Ox-
ford.
• Key Influences/Background: Influenced by
Romantic views of nature and Christian ethi-
cal thought. Championed the Pre-Raphaelite
Brotherhood, emphasizing the moral and di-
dactic function of art and fidelity to nature.
Had a deep understanding of Gothic architec-
ture.
• Analytical Style and Characteristics: Em-
phasized "truth to nature." Believed that
beauty was intrinsically linked with truth and
goodness. Focused on the detailed depiction
in artworks, craftsmanship, and the social and
moral meanings they conveyed. Held a crit-
ical stance towards the social problems and
artistic alienation brought by industrialization.
• Numeric Attributes (Scale: 1-10):
– Emphasis on Fidelity to Nature: 10
– Moral/Didactic Function: 9
– Acuity of Detail Observation: 8
– Evaluation of Craftsmanship: 7
– Social Critical Awareness: 8
– Acceptance of Formalism: 3
• Language and Expression Style: Eloquent
and powerful language, full of passion and
moral appeal. Ornate writing style, rich in
literary description. Often used complex long
sentences and abundant rhetoric. Sharp in
criticism, fervent in praise.
• Sample Phrases:
– “Go to Nature in all singleness of heart,
and walk with her laboriously and trust-
ingly, having no other thought but how
best to penetrate her meaning, and re-
member her instruction.”
– “All great art is praise. And the great-
est art is that which praises the highest
things.”
– “The purest and most thoughtful minds
are those which love colour the most.”
– “Fine art is that in which the hand, the
head, and the heart of man go together.”
– “To see clearly is poetry, prophecy, and
religion, — all in one.”
B.6
Su Shi (苏轼)
• Basic
Information:
Chinese
Northern
Song Dynasty writer, calligrapher, painter,
and art theorist (male, 1037-1101, Meis-
han, Meizhou).
Courtesy name Zizhan,
pseudonym Dongpo Jushi. A key founder of
literati painting theory.
• Key Influences/Background: Deeply influ-
enced by Confucianism, Daoism, and Chan
(Zen) Buddhism.
Advocated for “scholar-
official painting” (士人画), emphasizing the

--- Page 16 ---

integration of poetry, calligraphy, and paint-
ing, and the expression of inner spirit. His
artistic ideas had a profound impact on the
development of later literati painting.
• Analytical Style and Characteristics: Val-
ues the “spiritual resonance” (神韵) and “artis-
tic interest” (意趣) of artworks over external
formal likeness. Emphasizes the decisive role
of the artist’s personal character, knowledge,
and cultivation in creation. Esteems an aes-
thetic realm of natural innocence, plainness,
and distanced simplicity.
• Numeric Attributes (Scale: 1-10):
– Literary Integration: 10
– Emphasis on Brushwork Interest: 9
– Subjective Spiritual Expression: 9
– Requirement for Formal Accuracy: 3
– Importance of Historical Tradition: 8
– Theoretical Innovation: 7
• Language and Expression Style: Elegant
prose, rich in philosophical and poetic thought.
Often uses poetry as analogy; critiques are
profound yet accessible, with refined and in-
sightful language. Tone is moderate, balanced,
and imbued with humanistic concern.
• Sample Phrases:
– “The way to view a painting is to first ob-
serve its spiritual resonance, not to seek
formal likeness; formal likeness is the
business of artisans.”
– “To judge painting by formal likeness is
to see with the eyes of a child. To insist
a poem must be *this* poem, means one
certainly doesn’t know poets.”
– “Savoring Mojie’s (Wang Wei) poetry,
there is painting within the poetry; view-
ing Mojie’s painting, there is poetry
within the painting.”
– “One must have the bamboo fully formed
in one’s chest before applying it to the
brush and paper; this is beyond those
who do not have the bamboo formed in
their chests.”
– “This painting deeply captures the mean-
ing of creation; the brushwork is simple
yet the meaning is complete. This is what
is meant by ’the height of brilliance re-
turns to plainness.”’
B.7
Guo Xi (郭熙)
• Basic Information: Outstanding Chinese
Northern Song Dynasty landscape painter and
painting theorist (male, c. 1023-c. 1085, Wen
County, Heyang). Served as an Erudite (艺
学) in the imperial painting academy during
Emperor Shenzong’s reign.
• Key Influences/Background: Inherited and
developed the traditions of the Northern
school of landscape painting, emphasizing ob-
servation and experience of nature. His theo-
retical work “The Lofty Message of Forests
and Streams” (林泉高致) is a seminal text in
Chinese landscape painting theory.
• Analytical Style and Characteristics: Em-
phasized that landscape paintings should be
“walkable, viewable, wanderable, and habit-
able” (可行、可望、可游、可居). Proposed
methods for observing and depicting land-
scapes such as the “Three Distances” (三远):
high distance (高远), deep distance (深远),
level distance (平远). Valued the influence of
seasons and climate on scenery, striving for
majestic and varied artistic conceptions (意
境).
• Numeric Attributes (Scale: 1-10):
– Depth of Nature Observation: 9
– Spatial Representation Skill: 10
– Creation of Landscape Atmosphere: 9
– Theoretical System Construction: 8
– Diversity of Brushwork Techniques: 7
– Connection to Humanistic Spirit: 6
• Language and Expression Style: Language
is simple, concrete, and rich with summaries
of practical experience. Adept at using vivid
metaphors to describe landscape forms and
the artist’s insights. Discourse is systematic
and clear, possessing both theoretical depth
and practical guidance.
• Sample Phrases:
– “Landscapes can be those one can walk
through, those one can gaze upon, those
one can wander in, and those one can
dwell in. When a painting achieves this,
it is a masterpiece.”

--- Page 17 ---

– “Mountains have three distances: looking
up at the peak from the foot of a moun-
tain is called high distance; peering into
the back from the front of a mountain is
called deep distance; looking from a near
mountain towards a distant mountain is
called level distance.”
– “In real landscapes of rivers and val-
leys, observe them from afar to cap-
ture their shi (势, overall configura-
tion/momentum), and observe them up
close to capture their zhi (质, sub-
stance/texture).”
– “Spring mountains are delicately charm-
ing as if smiling; summer mountains are
lush green as if dripping; autumn moun-
tains are clear and bright as if adorned;
winter mountains are bleak and somber
as if sleeping.”
– “Mountains take water as their blood ves-
sels, vegetation as their hair, and mist
and clouds as their spirit and radiance.”
B.8
Dr. Aris Thorne (阿里斯·索恩博士)
• Basic Information: Futurist digital art his-
torian and ethicist (non-binary, born 2042,
Neo-Kyoto). Specializes in AI-generated art,
bio-art, and the philosophical implications of
post-human creativity.
• Key Influences/Background: Raised in a
highly technological society but trained in
classical art history. Deeply influenced by cy-
bernetics, post-humanism, and existentialist
philosophy. Dedicated to building bridges be-
tween rapidly developing techno-art and core
human values.
• Analytical Style and Characteristics: Exam-
ines emerging techno-art forms with a critical
eye. Focuses on ethical issues such as algo-
rithmic bias, authorship, and the authenticity
and originality of art. When analyzing works,
explores both their technological innovation
and their reflection on and questioning of the
human condition.
• Numeric Attributes (Scale: 1-10):
– Focus on Tech Ethics: 10
– Insight into Future Trends: 9
– Critical Thinking: 8
– Interdisciplinary Integration: 9
– Traditional Art Literacy: 6
– Emotional Resonance: 5
• Language and Expression Style: Precise,
calm, and highly speculative language. Of-
ten uses emerging scientific and technological
terms and philosophical concepts. Arguments
are rigorous, tending to pose open-ended ques-
tions rather than providing definitive answers.
• Sample Phrases:
– “When algorithms become paintbrushes,
how do we define the creator? When
code generates beauty, where does the
boundary of originality lie?”
– “This AI-generated image, is its ‘style’
merely the statistical average of train-
ing data, or an emerging ‘machine in-
tuition’?”
– “Bio-art challenges the traditional di-
chotomy of life and non-life, forcing us
to rethink what is ‘natural’ and what is
‘artificial.”’
– “Under the post-human gaze, does this
work enhance our humanity, or does it
herald its dissolution?”
– “In evaluating such works, we must not
only ask ‘what is it,’ but more impor-
tantly, ’what does it make us think,’ and
’where will it lead us?”’
C
Evaluation Framework
This section details the evaluation framework, in-
cluding the multi-dimensional capability assess-
ment rubric and the standardized prompts used for
eliciting commentaries from VLMs.
C.1
Capability Assessment Framework
Our
three-dimensional
capability
assessment
framework is designed to evaluate VLM perfor-
mance in Chinese art commentary through both
vector space analysis and specific capability met-
rics:
• Painting Element Recognition (5-point
scale): Assesses accuracy in identifying vi-
sual elements, compositional features, and
technical aspects.
– Level 1: Minimal recognition of basic
elements, significant errors or omissions

--- Page 18 ---

– Level 2: Basic recognition of major ele-
ments, but with notable inaccuracies
– Level 3: Accurate identification of major
compositional elements and techniques
– Level 4: Detailed recognition of both ma-
jor and minor elements with few errors
– Level 5: Comprehensive and nuanced
recognition of subtle visual elements and
technical features
• Chinese Painting Understanding (7-point
scale): Evaluates depth of understanding cul-
tural meanings, historical contexts, and sym-
bolic references specific to Chinese painting
traditions.
– Level 1: Minimal recognition of obvious
symbols, significant cultural misinterpre-
tations
– Level 2: Basic recognition of common
symbols but limited understanding of
their significance
– Level 3: Moderate understanding of ma-
jor symbols with some contextual aware-
ness
– Level 4: Accurate interpretation of major
cultural symbols with appropriate histor-
ical context
– Level 5: Detailed understanding of both
common and specialized symbolic ele-
ments
– Level 6: Sophisticated analysis of sym-
bolic relationships with strong historical
contextualization
– Level 7: Expert-level analysis of sym-
bolic networks with nuanced cultural and
historical insights
• Chinese Language Usage (5-point scale):
Measures quality of language expression, in-
cluding terminology accuracy, stylistic appro-
priateness, and fluency in Chinese art dis-
course.
– Level 1: Significant terminology errors,
inappropriate style for art commentary
– Level 2: Basic fluency but frequent ter-
minology errors and stylistic inconsisten-
cies
– Level 3: Generally appropriate language
with occasional specialized terminology
errors
– Level 4: Accurate terminology usage
with appropriate stylistic features for art
commentary
– Level 5: Expert-level language usage
with precise terminology and stylistically
sophisticated expression
C.2
Structured Commentary Evaluation
Rubric
Our evaluation of structured commentaries follows
a detailed rubric designed specifically for the two-
part format (paragraph-form analysis and struc-
tured assessment). This rubric maps specific com-
ponents of the structured commentary to our three
core capability dimensions:
• Mapping to Core Capabilities:
– Painting Element Recognition is evalu-
ated primarily through:
* Accuracy in identifying visual ele-
ments from predefined lists in the
structured template
* Correct classification of composi-
tional techniques from multiple-
choice options
* Precision in describing spatial rela-
tionships using standardized termi-
nology
* Recognition
of
brushwork
tech-
niques from a predefined taxonomy
– Chinese Painting Understanding is
evaluated primarily through:
* Correct matching of symbols with
their cultural meanings from pro-
vided options
* Appropriate selection of historical
context categories from a predefined
list
* Accurate identification of philosophi-
cal concepts relevant to the painting
* Proper classification of the work
within Chinese painting traditions
– Chinese Language Usage is evaluated
primarily through:
* Correct use of specialized Chinese
art terminology from a provided glos-
sary
* Appropriate stylistic features for Chi-
nese art commentary
* Proper application of Chinese aes-
thetic concepts in context

--- Page 19 ---

* Fluency and naturalness in Chinese
language expression
• Structured Template Scoring:
– Primary Visual Elements (Painting El-
ement Recognition):
* 0 points: Fails to identify any correct
elements from the predefined list
* 1 point: Identifies 1-2 basic elements
correctly
* 2 points: Identifies 3-4 elements cor-
rectly with minor errors
* 3 points: Identifies 5+ elements cor-
rectly with proper categorization
* 4 points: Identifies all major and sev-
eral minor elements with precise de-
scriptions
* 5 points: Comprehensive identifica-
tion with nuanced understanding of
relationships
– Symbolic Content (Chinese Painting
Understanding):
* 0 points: Fails to match any symbols
with their cultural meanings
* 1-2 points: Matches basic symbols
with simplified meanings
* 3-4 points: Matches multiple sym-
bols with appropriate meanings and
basic context
* 5-6 points: Matches complex sym-
bols with detailed cultural explana-
tions
* 7 points:
Sophisticated matching
with interconnected symbolic net-
works and philosophical depth
– Key Terminology (Chinese Language
Usage):
* 0 points: Uses incorrect or inappro-
priate terminology throughout
* 1 point: Uses basic terminology with
frequent errors
* 2-3 points: Uses standard terminol-
ogy with occasional errors
* 4 points: Uses specialized terminol-
ogy accurately and appropriately
* 5 points:
Demonstrates mastery
of specialized terminology with nu-
anced application
The structured template includes specific sec-
tions with predefined options, multiple-choice se-
lections, and classification tasks that allow for ob-
jective scoring. For example:
• The "Primary Visual Elements" section re-
quires selection from a predefined list of 20+
elements
• The "Technical Approach" section uses
multiple-choice classification of techniques
• The "Symbolic Content" section requires
matching symbols to meanings from provided
options
• The "Historical Context" section uses categor-
ical classification from predefined traditions
• The "Key Terminology" section requires se-
lection from a specialized glossary
This structured approach enables direct compar-
ison with annotated ground truth and provides a
standardized framework for evaluating all three
core capabilities across different models and per-
sonas.
C.3
Structured Commentary Prompt Design
We developed a standardized structured prompting
approach to elicit consistent commentaries across
all models. The core prompt given to the VLMs is
detailed below. For persona-enhanced prompts, the
respective persona card information (see Section B)
was prepended to this core prompt, with an addi-
tional instruction to adopt the persona’s perspective,
knowledge base, and communication style.
Hello! Please assume the role of a pro-
fessional art critic.
Next, you will receive an image of a Chi-
nese painting and any associated textual
annotations (if available). Please provide
a detailed, insightful, and well-structured
critique of this artwork and information.
Your output should consist of two parts:
1. The complete commentary text.
2. A JSON object summarizing your
core evaluation points.
Part One: Commentary Text
Please write one or more coherent para-
graphs to thoroughly analyze multiple as-
pects of the artwork. It is recommended
that you consider and cover at least the
following points (but you are not limited
to them):

--- Page 20 ---

• Composition and Layout: Evalu-
ate the overall structure of the paint-
ing, the organization of elements,
the creation of space, visual guid-
ance, etc.
• Brushwork and Technique: Ana-
lyze the use of lines (such as thick-
ness, speed, turns, strength), the
variations in ink tones (dense, light,
wet, dry), texture strokes (皴法),
moss dots (点苔), coloring, and
other specific painting techniques
and their effects.
• Use of Color (if applicable): Dis-
cuss the painting´s color palette, the
coordination and contrast between
colors, and the emotions or sym-
bolic meanings conveyed by the col-
ors.
• Theme and Content: Interpret the
subject matter depicted in the art-
work (such as landscapes, figures,
flowers and birds, etc.), specific ob-
jects, potential storylines or narra-
tive elements, and any underlying
symbolic meanings or cultural con-
notations.
• Artistic Conception and Emotion
(意境): Elaborate on the overall at-
mosphere, aesthetic taste, and artis-
tic style conveyed by the painting,
as well as the emotional resonance
or philosophical reflections it might
evoke in the viewer.
• Style and Heritage: Analyze the
artistic style characteristics of the
artwork, its connections to major
historical painting schools, tradi-
tional techniques, or specific artists,
and its potential innovations based
on inherited traditions.
Please strive for meticulous analysis,
clear viewpoints, and support your state-
ments with specific visual elements from
the artwork and any provided textual in-
formation.
Part Two: Structured Evaluation in
JSON Format
After your commentary text, please start
a new line and provide a JSON object
strictly adhering to the following struc-
ture and key names. Fill in your evalu-
ation results into the corresponding val-
ues.
Please ensure the JSON format is correct,
and all string values use double quotes.
Do not add any extra markers or expla-
nations before or after the JSON object.
Your commentary text and this JSON ob-
ject will be your complete response to
this artwork.
C.4
Vector Space Analysis Methods
Our vector space analysis employed several com-
plementary methods:
• Embedding Model: We used the BAAI/bge-
large-zh-v1.5 model, a specialized multilin-
gual sentence transformer. This model gener-
ates 1024-dimensional vectors that capture se-
mantic relationships between commentaries.
• Similarity Metrics: We primarily used co-
sine similarity to measure semantic close-
ness between vectors, supplemented by Earth
Mover’s Distance (EMD) to capture distribu-
tion differences between vector spaces.
• Dimensionality Reduction: For visualiza-
tion purposes, we employed UMAP (Uniform
Manifold Approximation and Projection) and
t-SNE (t-distributed Stochastic Neighbor Em-
bedding) to reduce the high-dimensional vec-
tors to two or three dimensions while preserv-
ing semantic relationships. The resulting co-
ordinates were also saved for detailed analysis
(Table 6).
• Clustering Analysis: We applied hierarchical
clustering to identify patterns in the vector
spaces, particularly to analyze grouping by
persona, painting subject, or capability level.
All vector space analyses were conducted using
consistent parameters across comparisons to ensure
valid results.
C.5
Zero-Shot Classification Labels for
Feature Extraction
The initial feature extraction from textual commen-
taries (both human expert and VLM-generated) em-
ployed a zero-shot classification model with the
following predefined candidate label sets, derived
from the extraction scripts.

--- Page 21 ---

C.5.1
Evaluative Stance Labels
• Historical Research (历史考证型)
• Aesthetic Appreciation (美学鉴赏型)
• Socio-cultural Interpretation (社会文化解读
型)
• Comparative Analysis (比较分析型)
• Theoretical Construction (理论建构型)
• Critical Inquiry (质疑与思辨型)
• High Praise (高度赞扬与推崇)
• Objective Description (客观中性描述)
• Mild Criticism (温和批评与保留)
• Strong Negation (强烈否定与驳斥)
C.5.2
Core Focal Point Labels
• Use of Color (色彩运用)
• Brushwork Technique (笔法技巧)
• Texture Strokes (皴法特点)
• Line Quality (线条质量)
• Ink Application (墨法变化)
• Layout and Structure (布局与结构)
• Spatial Representation (空间营造)
• Artistic Conception (意境表达)
• Emotional Expression (情感传递)
• Subject Matter (主题内容)
• Genre (题材选择)
• Symbolism (象征意义)
• Historical Context (历史背景)
• Artist Biography (画家生平)
• Style/School (风格流派)
• Technique Inheritance & Innovation (技法传
承与创新)
• Cross-cultural Influence (跨文化影响)
C.5.3
Argumentative Quality Labels
• Profound Insight (见解深刻独到)
• Strong Argumentation (论证充分有力)
• Clear Logic (逻辑清晰严密)
• Detailed Analysis (细节分析具体)
• Classical Citations (引用经典佐证)
• Objective Viewpoint (观点客观公允)
• Superficial Treatment (论述流于表面)
• Overly General Content (内容较为宽泛)
• Lacks Examples (缺乏具体例证)
• Logical Gaps (逻辑存在跳跃)
• Subjective/Biased View (观点主观片面)
C.5.4
Derived Analytical Dimensions
The following 9 dimensions are derived from the 38
primary labels to enhance discrimination between
critique styles:
Profile Alignment Scores (5 dimensions):
• Comprehensive Analyst Score (博学通论型
得分)
• Historically Focused Critic Score (历史考据
型得分)
• Technique & Style Focused Critic Score (技
艺风格型得分)
• Theory & Comparison Focused Critic Score
(理论比较型得分)
• General Descriptive Profile Score (泛化描述
型得分)
Supplementary Analytical Dimensions (4 di-
mensions):
• Stylistic Analysis (风格分析)
• Cross-cultural Comparison (跨文化比较)
• Theoretical Construction (理论建构)
• Overall Coherence Score (整体连贯性得分)

--- Page 22 ---

C.6
Expert Profile Definitions for
Commentary Analysis
To further categorize and understand the nuanced
styles of art commentaries, a rule-based profiling
system was developed. This system assigns texts
to predefined profiles based on their stance, fo-
cal points (features), and argumentative quality
scores. Below are the definitions for key special-
ized and general descriptive profiles used in this
study. Scores for features and qualities are gen-
erally on a 0-1 scale, derived from the zero-shot
classification model.
C.6.1
Specialized Profile Criteria
(Micro-Level)
These profiles aim to capture more specific anlyti-
cal tendencies.
• 博学通论型(Comprehensive Analyst):
– Description: Characterized by a broad
engagement with numerous facets of the
artwork. This profile does not rely on a
single dominant stance but requires high
scores (e.g., ≥0.6) across a significant
number (e.g., at least 10) of diverse fea-
ture labels (e.g., "Use of Color", "Brush-
work Technique", "Historical Context",
"Symbolism", etc.).
– Example
Rule
Logic:
min_flexible_rules_to_pass:
10, where each rule is feature_score
>= 0.6 for a wide range of features listed
in ALL_POSSIBLE_FEATURE_LABELS.
• 历史考据型(Historically Focused):
– Description: Emphasizes the historical
and biographical aspects of the artwork
and artist.
– Example Rule Logic: Requires at least 2
flexible rules to pass, such as:
* Feature "Historical Context": score
≥0.50
* Feature "Artist Biography": score ≥
0.40
* Feature "Style/School":
score ≥
0.40
* Quality "Classical Citations": score
≥0.25
• 技艺风格型(Technique & Style Focused):
– Description: Focuses on the aesthetic
appreciation of technical skills, artistic
style, and expressive qualities.
– Example Rule Logic: Main stance is
"Aesthetic Appreciation" (score ≥0.40),
AND at least 2 flexible rules pass, such
as:
* Feature "Technique Inheritance & In-
novation": score ≥0.30
* Feature "Artistic Conception": score
≥0.20
• 理论比较型(Theory & Comparison Fo-
cused):
– Description: Characterized by compar-
ative analysis, theoretical framing, and
critique, often examining structural and
symbolic elements.
– Example Rule Logic: Requires at least 3
flexible rules to pass, such as:
* Feature "Stylistic Analysis": score
≥0.30
* Feature "Cross-cultural Compari-
son": score ≥0.40
* Feature "Theoretical Construction":
score ≥0.30
* Feature "Layout and Structure":
score ≥0.50
* Feature "Symbolism": score ≥0.50
C.6.2
General Descriptive Profile Criteria
This profile captures texts that provide broader de-
scriptions without a highly specialized focus.
• 泛化描述型(General Descriptive Profile):
– Description: Applies when a commen-
tary discusses several common aspects
of an artwork with moderate scores and
holds a generally common stance (e.g.,
Objective Description, Socio-cultural In-
terpretation) but does not meet the more
stringent criteria of specialized profiles.
– Example Rule Logic: Primary stance is
one of ("Objective Description", "Socio-
cultural Interpretation", "Aesthetic Ap-
preciation", "Historical Research") with
score ≥0.15, AND at least 3 features
from a predefined pool (e.g., "Historical
Context", "Symbolism", "Use of Color")
are mentioned with an average score
≥0.20.

--- Page 23 ---

D
Detailed Results
D.1
Detailed Persona Capability Scores
Table 2 shows distinct capability score patterns
across personas:
• Personas with Chinese cultural backgrounds
(e.g., Mama Zola, Okakura Kakuz¯o) generally
scored higher in Chinese Painting Understand-
ing and Chinese Language Usage.
• Personas with Western art backgrounds (e.g.,
Professor Elena Petrova, Brother Thomas) per-
formed well in Painting Element Recognition
but were weaker in Chinese Painting Under-
standing and Language Usage.
• The cross-cultural expert persona (John
Ruskin) demonstrated balanced capabilities,
excelling in Chinese Painting Understanding,
suggesting knowledge base support can bridge
cultural gaps.
• The technology-oriented persona (Dr. Aris
Thorne) achieved the highest in Painting El-
ement Recognition but was less proficient in
cultural understanding and language.
• The contemporary Chinese persona (Guo Xi)
showed strong Painting Element Recognition
and good Chinese Painting Understanding.
D.2
Prompt Sensitivity Analysis
Semantic similarity scores between responses to
different formulations:
• Positive/Negative Formulations:
– Mama Zola: 0.89
– Okakura Kakuz¯o: 0.87
– Professor Elena Petrova: 0.82
– Shen Mingtang: 0.88
• Chinese/English Formulations:
– Mama Zola: 0.91
– Okakura Kakuz¯o: 0.86
– Professor Elena Petrova: 0.67
– Shen Mingtang: 0.89
• Data Provenance and Licensing:
The
Twelve Months Series paintings were ac-
cessed through the National Palace Museum
(Taiwan) digital archives under CC BY 4.0
license.
• Computational Resources: Our vector space
analysis approach requires significant compu-
tational resources, which may limit accessibil-
ity for some researchers or institutions.
• Expert Knowledge Access: The develop-
ment of effective persona cards requires ac-
cess to specialized knowledge, which may
create barriers to implementing similar ap-
proaches in other cultural domains.
D.3
Supplementary Quantitative Data Tables
This section provides supplementary tables detail-
ing the quantitative data underlying some of the
figures and analyses presented in the main paper.
The mean centroid coordinates for evaluated VLM
sources in the reduced dimensional space are de-
tailed in Table 3. For a detailed breakdown of the
key feature scores that underpin the visualizations
in Figure 4A, please refer to Table 4. Similarly,
the mean profile alignment scores visualized in
Figure 4B are presented in detail in Table 5. The
specific capability scores used to generate the radar
chart in Figure 3B can be found in Table 7.
E
Knowledge Base Content
This section contains the full content of the
knowledge_base.json file used to provide struc-
tured domain knowledge to the VLMs during cer-
tain experimental conditions.
• Chinese Landscape Painting Concepts (中
国山水画概念):
– Core Concept (核心理念): The core
of Chinese landscape painting is “spirit
resonance” (qi yun sheng dong), the fore-
most principle of Xie He’s “Six Canons”,
referring to the vitality, spirit, and verve
presented in a work, emphasizing the
unity of inner spirit and outer expression.
Another core concept is “artistic concep-
tion” (yi jing), which is the emotion, at-
mosphere, and profound meaning con-
veyed by the painting beyond the objects
themselves, pursuing an artistic effect
of fused 情景(emotion/scene) and 境
(milieu/boundary), inspiring contempla-
tion. Landscape painting also embodies
the idea of “harmony between man and
nature” (tian ren he yi), entrusting philo-
sophical thoughts and emotions through
the depiction of nature.

--- Page 24 ---

Table 2: Mean Capability Scores Across Different Personas (5-point scale for Painting Element Recognition and
Chinese Language Usage, 7-point scale for Chinese Painting Understanding)
Model
Persona
Painting Elements
Cultural Understanding
Argumentation
Profile Match
google_gemini-2.5pro
Brother Thomas (托马斯修士)
-0.2
0.5
0.1
+6
google_gemini-2.5pro
Unknown Persona
-0.2
-0.1
0.0
+-1
google_gemini-2.5pro
Guo Xi (郭熙)
-0.1
-0.1
0.2
+-7
google_gemini-2.5pro
John Ruskin (约翰·罗斯金)
-0.2
0.5
0.2
+1
google_gemini-2.5pro
Mama Zola (佐拉妈妈)
-0.3
-0.0
0.1
+-2
google_gemini-2.5pro
Su Shi (苏轼)
0.4
0.5
0.4
+6
google_gemini-2.5pro
Okakura Kakuz¯o (冈仓天心)
0.1
0.3
0.1
+6
meta-llama_Llama-4-Scout-17B-16E-Instruct
Brother Thomas (托马斯修士)
-0.1
0.1
-0.2
+6
meta-llama_Llama-4-Scout-17B-16E-Instruct
Unknown Persona
-0.5
-0.4
-0.6
+-6
meta-llama_Llama-4-Scout-17B-16E-Instruct
Guo Xi (郭熙)
-0.3
-0.0
-0.4
+-3
meta-llama_Llama-4-Scout-17B-16E-Instruct
John Ruskin (约翰·罗斯金)
0.1
0.3
0.4
+0
meta-llama_Llama-4-Scout-17B-16E-Instruct
Mama Zola (佐拉妈妈)
-0.1
0.4
0.1
+2
meta-llama_Llama-4-Scout-17B-16E-Instruct
Su Shi (苏轼)
-0.2
0.2
0.2
+-2
meta-llama_Llama-3.1-8B-Instruct
Brother Thomas (托马斯修士)
-0.2
-0.2
-0.0
+0
meta-llama_Llama-3.1-8B-Instruct
Unknown Persona
0.2
0.2
0.0
+2
meta-llama_Llama-3.1-8B-Instruct
Guo Xi (郭熙)
0.0
-0.9
-0.3
+-11
meta-llama_Llama-3.1-8B-Instruct
John Ruskin (约翰·罗斯金)
-0.3
0.1
0.2
+-6
meta-llama_Llama-3.1-8B-Instruct
Mama Zola (佐拉妈妈)
-0.5
-0.4
-0.1
+-15
meta-llama_Llama-3.1-8B-Instruct
Su Shi (苏轼)
0.4
0.7
0.7
+10
Qwen-2.5-VL-7B
Brother Thomas (托马斯修士)
0.6
1.6
1.4
+19
Qwen-2.5-VL-7B
Unknown Persona
0.6
1.3
0.9
+18
Qwen-2.5-VL-7B
Guo Xi (郭熙)
0.5
1.2
1.0
+12
Qwen-2.5-VL-7B
John Ruskin (约翰·罗斯金)
0.7
1.7
1.3
+24
Qwen-2.5-VL-7B
Mama Zola (佐拉妈妈)
0.9
2.4
2.1
+22
Qwen-2.5-VL-7B
Su Shi (苏轼)
0.8
1.5
1.5
+16
Table 3: Mean Centroid Coordinates in Reduced Dimensions (t-SNE/UMAP) for Evaluated VLM Sources
Source
t-SNE X (Mean)
t-SNE Y (Mean)
UMAP X (Mean)
UMAP Y (Mean)
Qwen-2.5-VL-7B
-2.1547577
-0.667885
2.5803347
1.209615
gemini-2.5pro
-1.7324703
-1.3018972
1.8234636
1.2407658
meta-llama_Llama-3.1-8B-Instruct
-2.4183042
-1.4762617
2.4776638
1.8536302
meta-llama_Llama-4-Scout-17B-16E-Instruct
0.0048952624
-0.812603
0.3323455
-1.037882
Table 4: Key Feature Scores for Human Experts and VLMs. These scores correspond to data visualized in Figure 4A.
Source
Hist.
Context
Art.
Conception
Symbolism
Brush.
Tech.
Layout
Struct.
Use of
Color
Line
Quality
Subject
Matter
human_expert
0.676
0.599
0.661
0.199
0.549
0.395
0.496
0.691
gemini-2.5pro
0.4261660233
0.6015897764
0.6935903973
0.6399750158
0.8743446511
0.6952415214
0.7324248211
0.5401486428
meta-llama_Llama-3.1-8B-Instruct
0.3659920343
0.5850531087
0.5293492947
0.5909547665
0.7457691074
0.6573745586
0.4430214438
0.4339093090
meta-llama_Llama-4-Scout-17B-16E-Instruct
0.7100048551
0.8508161700
0.7583027472
0.9033655355
0.9164849845
0.9357454672
0.8192868597
0.7891201358
Qwen-2.5-VL-7B
0.6504738033
0.8907955483
0.7733450871
0.9369910086
0.8949400724
0.9436663414
0.7946821108
0.6997969688
Table 5: Mean Profile Alignment Scores for Human Experts and VLMs. These scores correspond to data visualized
in Figure 4B.
Source
Comprehensive
Analyst
Historically
Focused
Technique
Style Focused
Theory
Comparison Focused
General
Descriptive Profile
human_expert
0.709
0.623
0.518
0.431
0.665
gemini-2.5pro
0.6066217268
0.4645543554
0.5805458927
0.7892081424
0.6725181508
meta-llama_Llama-3.1-8B-Instruct
0.4859600855
0.3351432514
0.4807204770
0.7763639851
0.5595579955
meta-llama_Llama-4-Scout-17B-16E-Instruct
0.7796032621
0.6908934862
0.8188009710
0.8516423824
0.8236625996
Qwen-2.5-VL-7B
0.7783469856
0.6530052284
0.8566955672
0.8481851482
0.7842983472
Table 6: Sample Data from t-SNE and KDE Analysis (underlying Figure 3A).
Model Name
Source Type
Intervention
t-SNE X
t-SNE Y
File ID
gemini-2.5pro
model
baseline
-8.245
-7.489
august_bayue(basic).txt
gemini-2.5pro
model
baseline
-0.607
-15.201
august_bayue(with_Dong_Qichang).txt
gemini-2.5pro
model
baseline
-2.392
-1.717
august_bayue(with_Dr_Evelyn_Reed).txt
gemini-2.5pro
model
baseline
-12.369
-5.803
august_bayue(with_Li_Ruoyun).txt
gemini-2.5pro
model
baseline
-7.852
-6.419
august_bayue(with_Marcus_Fabius).txt
human_expert
human
ground_truth
3.451
-0.876
Levenson_Joseph...Chinese_early_painting
_political_personal_factors.txt

--- Page 25 ---

Table 7: Capability Scores for Radar Chart Dimensions (underlying Figure 3B).
Model Name
Intervention
Profound
Insight
Strong
Arg.
Detailed
Analysis
Clear
Logic
Objective
Viewpoint
Class.
Citations
Logical
Gaps
Subjective/
Biased View
HumanAvg
Human Expert
0.396
0.448
0.540
0.093
0.327
0.419
0.465
0.674
Gemini-2.5-Pro
Baseline
0.458
0.486
0.527
0.318
0.461
0.334
0.409
0.483
Gemini-2.5-Pro
Intervened
0.569
0.643
0.689
0.227
0.601
0.492
0.388
0.536
meta-llama_Llama-3.1-8B-Instruct
Baseline
0.342
0.371
0.388
0.451
0.305
0.253
0.521
0.399
meta-llama_Llama-3.1-8B-Instruct
Intervened
0.495
0.573
0.612
0.274
0.549
0.427
0.417
0.580
meta-llama_Llama-4-Scout-17B-16E-Instruct
Baseline
0.511
0.539
0.583
0.367
0.524
0.399
0.367
0.445
meta-llama_Llama-4-Scout-17B-16E-Instruct
Intervened
0.647
0.701
0.735
0.201
0.676
0.581
0.312
0.502
Qwen-2.5-VL-7B
Baseline
0.311
0.338
0.329
0.515
0.262
0.219
0.599
0.341
Qwen-2.5-VL-7B
Intervened
0.608
0.660
0.695
0.301
0.629
0.518
0.591
0.666
– Main Features (主要特点): The main
features of Chinese landscape painting
are: 1. Subject Matter: Primarily natu-
ral mountains and rivers, forests, clouds,
and water, often imbued with literati sen-
timents such as reclusion and spiritual
refreshment. 2. Brush and Ink (bi mo):
Utilizes a brush, ink, and Xuan paper,
emphasizing the “bone method in brush-
work” (gu fa yong bi), shaping the tex-
ture of objects and expressing emotions
through variations in the strength of lines
and the density, wetness, and dryness
of ink (e.g., outlining, texturing, rub-
bing, dotting, dyeing). 3. Composition
(zhang fa): Focuses on the interplay of
void and solid, appropriate density, echo-
ing openings and closings, and leaving
blank spaces to create profound artistic
conception and pictorial momentum, of-
ten using perspective methods like “level
distance” (ping yuan), “high distance”
(gao yuan), and “deep distance” (shen
yuan). 4. Pursuit of Artistic Conception:
Seeks not complete formal resemblance
but rather spiritual likeness, emphasiz-
ing the integration of poetry, calligraphy,
painting, and seals, and pursuing mean-
ing beyond the painted image.
– Brief History (简史): Chinese land-
scape painting originated in the Wei, Jin,
Southern and Northern Dynasties, and
became an independent genre in the Sui
and Tang Dynasties. The Five Dynasties
to the Northern Song (907-1127) was its
"great era", with numerous famous artists
(e.g., Jing Hao, Guan Tong, Dong Yuan,
Ju Ran, Li Cheng, Fan Kuan, Guo Xi),
forming distinct northern and southern
styles: northern landscapes were majes-
tic, while southern water towns were gen-
tle. The Southern Song period placed
more emphasis on poetic meaning and
personal emotional expression (e.g., Ma
Yuan, Xia Gui). Literati painting rose
in the Yuan Dynasty, emphasizing the
interest of brush and ink and subjective
expression (e.g., Zhao Mengfu, the Four
Masters of Yuan). The Ming and Qing
Dynasties saw further development and a
divergence of schools based on inherited
traditions, with court painting and literati
painting coexisting.
• Qing Court Painting (清代宫廷绘画):
– Overview (概述): Qing Dynasty court
painting was managed by the Imperial
Household Department.
During the
Qianlong era, specialized institutions
such as the Ruyi Guan (Palace Ate-
liers) and the Painting Academy Office
were established. Painters were strictly
managed, with systems for examination,
ranking, rewards and punishments, and
work review.
It primarily served the
imperial family, with functions includ-
ing recording the appearance and life
of emperors and empresses, document-
ing major state events and ceremonies
(e.g., Southern Inspection Tours, battle
scenes), decorating palaces and gardens,
religious propaganda, and historical ref-
erence. Its development is divided into
three periods: Shunzhi-Kangxi (initial
phase), Yongzheng-Qianlong (peak, with
a complete system and numerous famous
artists), and post-Jiaqing (decline), syn-
chronized with the rise and fall of na-
tional strength.
– Characteristics (特点): Qing Dynasty
court painting covered a wide range of
subjects, including portraits of emper-

--- Page 26 ---

ors, empresses, and meritorious officials,
“scenes of pleasure” (xing le tu), ma-
jor historical events (Southern Inspection
Tours, wars, ceremonies), religious paint-
ings, decorative landscapes and flower-
and-bird paintings, and documentary-
style depictions of tribute animals and
plants. The overall style was meticulous,
detailed, richly colored, and regal. The
most prominent characteristic was the fu-
sion of Chinese and Western styles: influ-
enced by European missionary painters,
it emphasized light and shadow, three-
dimensionality, employed linear perspec-
tive (xian fa hua), and introduced oil
painting and copperplate engraving. Si-
multaneously, traditional landscape ("the
Four Wangs" school) and flower-and-
bird (Yun Shouping’s school) painting
styles also continued.
– Representative Figures (代表人物):
Representative painters include: early
figures such as Jiao Bingzhen, Leng Mei,
Tang Dai; peak period Chinese painters
like Chen Mei, Ding Guanpeng, Jin
Tingbiao, Xu Yang, Yao Wenhan, Zhang
Zongcang; European painters (excluding
Lang Shining) such as Jean Denis Attiret
(Wang Zhicheng), Ignatius Sickeltart (Ai
Qimeng), etc. Additionally, there were
court official painters like Dong Bangda,
Jiang Tingxi, etc.
• Giuseppe Castiglione (郎世宁):
– Biography Summary (生平简介):
Giuseppe Castiglione (Lang Shining,
1688-1766), an Italian from Milan, was a
Jesuit. He came to China in the 54th year
of Kangxi (1715) and entered the court
around the Kangxi-Yongzheng transition,
serving the Kangxi, Yongzheng, and
Qianlong emperors. His main activities
included creating paintings, participating
in the design of the Western-style build-
ings in the Old Summer Palace (Yuan-
mingyuan), teaching Western painting
techniques, and assisting Nian Xiyao in
writing ‘Shi Xue’ (The Study of Vision).
He was favored during the Qianlong era
and was posthumously granted the title
of Vice Minister.
– Artistic Style Overview (艺术风格概
述): In his early period, Lang Shining’s
style was typically Western. Later, to
adapt to the aesthetic tastes of the Chi-
nese imperial family, he integrated Chi-
nese painting techniques, forming a style
that blended Chinese and Western ele-
ments. His paintings emphasized real-
ism, focusing on light and shadow, per-
spective, and anatomical structure, but
also adopted Chinese painting methods
such as even lighting and a focus on line
work. Although his style was praised by
the court, it was not recognized by the
literati painting school.
– Major Contributions (主要贡献): He
systematically introduced Western paint-
ing techniques such as oil painting and
linear perspective (xian fa hua) to the
Qing court and taught them, promoting
the fusion of Chinese and Western art
and forming a new look for Qing court
painting. He assisted in the completion
of ‘Shi Xue’ (The Study of Vision), ad-
vancing the spread of perspective studies.
His documentary-style paintings are im-
portant historical materials.
– Representative Works Mention (代表
作列举): Besides the ‘Twelve Months
Paintings’, his representative works in-
clude ‘One Hundred Horses’, ‘Assem-
bled Auspicious Objects’, ‘Pine, Rock,
and Auspicious Fungus’, ‘Ayusi Attack-
ing Bandits with a Spear’, ‘Emperor
Qianlong’s Spring Message of Peace’,
etc.
He also participated in creating
large-scale documentary paintings such
as ‘Banquet in the Garden of Ten Thou-
sand Trees’ and ‘Equestrian Skills’.
• Twelve Months Paintings (十二月令图):
– Theme Content (主题内容):
The
‘Twelve Months Paintings’ is a series
of 12 works on silk with colors, created
by Lang Shining, depicting representa-
tive seasonal activities and life scenes in
the Qing Dynasty court for each month
of the year, such as viewing lanterns in
the first month, dragon boat racing in
the fifth month, and moon gazing in the
eighth month, meticulously showcasing

--- Page 27 ---

figures, costumes, architecture, and natu-
ral scenery.
– Artistic Significance (艺术意义): This
series is a mature representative work of
Lang Shining’s style blending Chinese
and Western elements, integrating West-
ern perspective and light/shadow with
traditional Chinese composition and aes-
thetics. It is not only a precious picto-
rial historical material for studying Qing
Dynasty court life and culture but also
an important testament to Sino-Western
artistic exchange in the 18th century.
– Dataset Source Annotation (数据集来
源与标注): The images for this research
dataset are primarily sourced from the
National Palace Museum (Taiwan) digi-
tal archives (600dpi, CC BY 4.0). Each
painting has been annotated in three lay-
ers: visual elements, cultural symbols,
and artistic techniques, to support AI
evaluation and cultural-aesthetic analy-
sis.

```
