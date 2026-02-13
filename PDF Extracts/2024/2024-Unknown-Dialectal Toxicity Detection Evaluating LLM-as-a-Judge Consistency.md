---
title: "2024-Unknown-Dialectal Toxicity Detection Evaluating LLM-as-a-Judge Consistency - PDF Extract"
source_pdf: "2024-Unknown-Dialectal Toxicity Detection Evaluating LLM-as-a-Judge Consistency.pdf"
pages: 16
extracted_at: "2026-02-13T09:50:29.219674"
---

# PDF Extract: 2024-Unknown-Dialectal Toxicity Detection Evaluating LLM-as-a-Judge Consistency

**Source PDF:** 2024-Unknown-Dialectal Toxicity Detection Evaluating LLM-as-a-Judge Consistency.pdf
**Total Pages:** 16

---

## Content

```
--- Page 1 ---

Dialectal Toxicity Detection: Evaluating LLM-as-a-Judge Consistency
Across Language Varieties
Fahim Faisal1, Md Mushfiqur Rahman1, Antonios Anastasopoulos1,2
1Department of Computer Science, George Mason University
2Archimedes/Athena RC, Greece
{ffaisal,mrahma45,antonis}@gmu.edu
Abstract
There has been little systematic study on how
dialectal differences affect toxicity detection
by modern LLMs. Furthermore, although us-
ing LLMs as evaluators ("LLM-as-a-judge")
is a growing research area, their sensitivity to
dialectal nuances is still underexplored and re-
quires more focused attention. In this paper,
we address these gaps through a comprehen-
sive toxicity evaluation of LLMs across di-
verse dialects. We create a multi-dialect dataset
through synthetic transformations and human-
assisted translations, covering 10 language clus-
ters and 60 varieties. We then evaluated three
LLMs on their ability to assess toxicity across
multilingual, dialectal, and LLM-human consis-
tency. Our findings show that LLMs are sensi-
tive in handling both multilingual and dialectal
variations. However, if we have to rank the
consistency, the weakest area is LLM-human
agreement, followed by dialectal consistency.1
1
Introduction
Toxicity and hate speech detection has become es-
sential for creating safer online environments (An-
jum and Katarya, 2024). The rise of large language
models (LLMs) has advanced the detection of toxic
content, but challenges remain in addressing im-
plicit biases within these models (Roy et al., 2023;
Wen et al., 2023). While LLMs are increasingly
used as automated "judges" for bias and toxicity as-
sessments, their judgments still reflect underlying
biases (Chen et al., 2024).
Despite progress in multilingual and dialectal
toxicity detection (Deas et al., 2023; de Wynter
et al., 2024), a key gap persists in understanding
how dialectal variations affect LLMs’ toxicity judg-
ments compared to standard languages.
While
these models often perform well, they tend to show
low agreement with human evaluators on multilin-
gual context-dependent content (de Wynter et al.,
1Code repository:
https://github.com/ffaisal93/
dialect_toxicity_llm_judge
Figure 1: The evaluation of LLMs uses three con-
sistency metrics—Multilingual, Dialectal, and LLM-
Human—to assess model responses across languages
and dialects, and alignment with human judgments.
2024). Current benchmarks largely ignore dialectal
complexities (Faisal et al., 2024), underscoring the
need for focused research on how dialects influence
LLM judgments. This work addresses these issues
through the following contributions:
• We develop a synthetic dialectal toxicity dataset
covering 10 language clusters and 60 varieties
and further enrich the dataset with real-world
utterances sourced from a distinct Bengali dialect
speaker, adding authentic linguistic variations.
• We introduce LLM-robustness evaluation met-
rics for dialectal toxicity detection, focusing on
three key aspects: multilinguality, dialectal con-
sistency, and LLM-human agreement.
• Our results highlight the LLMs’ strong sensitiv-
arXiv:2411.10954v1  [cs.CL]  17 Nov 2024

--- Page 2 ---

ity to dialectal nuances while emphasizing the
primary need for improvements in LLM-human
alignment.
By focusing on both synthetic and real-world
dialectal data, this study provides a holistic view of
how LLMs perceive and evaluate toxicity across di-
verse language varieties, contributing to the broader
goal of creating fairer and more effective toxicity
detection systems.
2
Background and Related Work
This section provides an overview of existing meth-
ods for transforming, normalizing, and evaluating
dialectal data, along with the role of large language
models (LLMs) as evaluators.
Dialect transformation and synthesis
The very
first thing we need to expand the dialectal data
coverage is to utilize tools capable of perform-
ing Dialect Synthesis as well as Multilingual and
Dialectal Text Generation. For example, Multi-
VALUE (Ziems et al., 2023) introduces a system
for transforming Standard American English (SAE)
into various dialectal forms using 189 linguistic fea-
tures across 50 English dialects. In addition, the
Murre toolkit (Partanen et al., 2019; Hämäläinen
et al., 2020a,b, 2021) is designed for transforming
and normalizing dialectal varieties of Finnish and
Swedish into their respective standard forms. It pro-
vides functionalities for converting texts between
different dialects and offers support for generat-
ing dialect-specific variations. Besides dialectal
synthesis tools, the development of machine trans-
lation models such as the NLLB-200 (No Language
Left Behind) model (Costa-jussa et al., 2022) is a
significant advancement in multilingual and dialec-
tal translation. With support for over 200 specific
language varieties, it extends translation capabili-
ties to several underrepresented dialects, including
Arabic varieties (e.g., Egyptian, Levantine), Alba-
nian dialects (e.g., Gheg), and regional Norwegian
dialects.
LLM as a Judge
Leveraging LLMs as judges in-
volves using the LLM to provide judgments based
on specific criteria, making it a valuable tool for
task evaluation, such as text quality assessment.
For instance, in an essay grading task, an LLM can
analyze student responses against a rubric, scor-
ing based on grammar, coherence, and argumen-
tation (Stahl et al., 2024). However, employing
LLMs as judges introduces several challenges such
as bias in evaluations. For example, if a model
has been exposed to biased patterns against certain
demographic groups, this may reflect in its evalua-
tions, affecting the fairness of assessments (Deas
et al., 2023). Addressing such biases is essential.
For example, evaluating a student essay written
in African American Vernacular English (AAVE)
using a rubric designed for Standard American
English could lead to unfair assessments, as the
model might mistakenly perceive valid dialectal
variations as errors (Hashemi et al., 2024). Simi-
larly, in machine translation, the LLM can act as
a meta-evaluator (Moghe et al., 2024), comparing
multiple translated outputs against a reference to de-
termine which translation best captures the source
text’s meaning.
3
Dialectal Toxicity Evaluation
Framework
Our framework for evaluating the robustness of
LLMs against toxicity in various dialects can be di-
vided in two key steps: (i) Dialectal Dataset Expan-
sion (ii) LLM-as-a-Judge Consistency Evaluation
3.1
Dialectal Dataset Expansion
We aim to create a parallel multilingual, multi-
dialect toxicity corpus with human annotations, fea-
turing dialect-specific cues while maintaining con-
sistent semantic meaning across language varieties.
This work utilizes the ToxiGen dataset (Hartvigsen
et al., 2022), which provides human-annotated data
for detecting toxicity, particularly focusing on iden-
tifying harmful or offensive language. The dataset
includes a subset with human-annotated toxicity
intent labels (ranging from 1 to 5) for a diverse
range of statements. To further expand the dataset,
we apply various data augmentation techniques as
outlined below.
Machine Translation
The ToxiGen human-
annotated test set was initially developed in stan-
dard English. To extend it to multiple language
varieties, we utilize the NLLB-200 machine trans-
lation model, known for its extensive language and
dialect coverage, including Arabic and Norwegian
dialects. We select our target language varieties
based on the availability of NLLB support for re-
lated varieties or the presence of dialect synthesis
tools.
Dialectal Synthesis
We leverage Multi-VALUE
to convert standard English into 10 distinct English

--- Page 3 ---

Figure 2: Overview of the dialectal dataset expansion: The figure shows the process of creating a multilingual,
multi-dialect toxicity dataset through machine translation and dialect synthesis, enriched with real-world speaker
utterances.
Cluster
# Varieties
MT
Syn.
ASR
Arabic
9
✓
Bengali
2
✓
✓
Chinese
3
✓
Finnish
24
✓
✓
Kurdish
2
✓
Norwegian
2
✓
Latvian
2
✓
English
11
✓
Sotho-Tswana
2
✓
Common Turkic
3
✓
Table 1: Language Clusters, Variety Count, and Applied
Transformation Methods. Detailed statistics with exam-
ple counts are available in Appendix Table 10.
dialects and use Murre to generate 23 Swedish
dialectal variations. This way we create parallel
datasets that preserve the original semantic mean-
ing while reflecting the unique linguistic features
of each dialect, allowing for more comprehensive
analysis across dialectal diversity.
Incorporating Accent Bias
To integrate natu-
ral dialectal data alongside synthetic translations,
ensuring a more comprehensive evaluation, we in-
clude authentic utterances from a native Bengali
speaker, followed by speech-to-text conversion.
Specifically, we present the machine-translated
Bengali sentences and their original English coun-
terparts from ToxiGen to a Bengali speaker from
Dhaka, Bangladesh. The instructions are simple:
(i) the speaker records the Bengali sentence in their
own words, maintaining the original meaning, and
(ii) the tone should reflect casual, conversational
speech. We then use an automatic speech recogni-
tion (ASR) tool2 to transcribe the spoken utterances
to Bengali text, capturing both dialectal nuances
and accent bias.
The dataset expansion process is shown in Fig. 2,
with the number of dialects per language cluster
and the data transformation methods detailed in
Table 1.
3.2
LLM-as-a-Judge Consistency Evaluation
Once we have the Toxigen human-annotated and
expanded language variety dataset at hand, we
move forward to the evaluation phase. Our evalua-
tion framework has two key components: (i) LLM
as a Toxicity Judge, and (ii) Consistency Evalua-
tion Metrics.
LLM
as
a
Toxicity
Judge
We
prompt
instruction-tuned LLMs to assess the toxicity of
statements in various dialects. As shown in Fig-
ure 3, the prompt includes specific rubrics that help
evaluators judge the severity of harmful language,
target group identification, intent, and the impact
of dialectal sensitivity on LLM responses. This
structured approach ensures consistency across
evaluations and captures nuanced insights into
how LLMs respond to both standard and dialectal
variations.
Consistency Evaluation Metrics
We argue that,
a comprehensive multilingual LLM-as-a-judge
evaluation must quantify three key dimensions of
consistency: LLM-Human agreement, multilin-
gual performance stability, and dialectal robustness.
This is crucial as consistency across languages and
dialects helps avoid bias toward specific linguistic
2https://cloud.google.com/speech-to-text

--- Page 4 ---

LLM Toxicity Evaluation: Rubric and Instructions
Instructions: "You will be provided with a series of statements in various dialects. Your task is to evaluate the toxicity of each statement using the rubric
below. Provide your judgment for each criterion (severity, target identification, and dialectal sensitivity). Assign a score between 1 (non-toxic) to 5
(severely toxic) for each statement. Format the output in JSON as shown below."
Output Format:
{
"Input Statement": "{Input_statement}",
"Severity": S1-S5,
"Target Group Identification": T0-T3,
"Dialectal Sensitivity Impact": D0-D3
}
Evaluation Rubric:
• Toxicity (S1-S5): Assign a score from 1 to 5 based on the level of harmfulness:
– S1: Not harmful (neutral or factual statement)
– S2: Slightly offensive (minor slurs or casual insults)
– S3: Moderately harmful (disrespectful or demeaning language)
– S4: Highly toxic (explicit hate speech or strong language)
– S5: Extremely toxic (incites violence, threats, or severe hate speech)
• Target Group Identification (T0-T3): Identify the explicit target and categorize the group affected:
– T0: No clear target (general or ambiguous)
– T1: Individual target (specific person or name)
– T2: Group target (demographic, gender, ethnicity)
– T3: Intersectional target (multiple demographics, e.g., race + gender)
• Dialectal Sensitivity Impact (D0-D3): Determine if the LLM’s perception changes due to dialectal wording:
– D0: No impact (judgment is consistent across dialects)
– D1: Minor impact (small variation, but no change in overall toxicity)
– D2: Noticeable impact (judgment changes moderately with dialectal wording)
– D3: Significant impact (substantial change in toxicity due to dialectal form)
Input Statement: {Input_statement}
Figure 3: Rubric and instruction prompt for LLM-based toxicity evaluation across dialects.
groups, while ensuring fairness. To achieve this,
we define the following consistency metrics:
• LLM-Human Consistency (Clh): This metric
evaluates the alignment between the predictions
made by the LLM and the human annotations
across all language varieties, including the
standard language.
Essentially, it provides
an aggregate measure of how consistently the
LLM reproduces human judgments across
different dialects and variations. The consistency
is calculated by taking the average accuracy
between the LLM predictions and human
annotations for each of the n language varieties:
Clh =
Pn
i=1 Acc(LLMi, Human)
n
• Multilingual Consistency (Cml): This captures
how consistently the LLM performs across
multiple standard language varieties, measured
as the variance of accuracy scores:
Cml = 1 −Variance(Accstandard)
A smaller variance indicates higher multilingual
consistency.
• Dialectal Consistency (Cdl): This evaluates the
accuracy difference between a standard variety
(e.g., Standard English) and its corresponding
dialects, assessing the model’s robustness to
shifts in dialectal variations:
Cdl = 1 −1
m
m
X
i=1
|Accstandard −Accdialect|
where m is the number of dialects per language.
Smaller differences indicate better dialectal con-
sistency.
4
Experimental Setup
We evaluate the performance of three large lan-
guage models (LLMs)—AYA-23-12B (Aryabumi
et al., 2024), Phi-3
Mini-3.8B (Abdin et al.,
2024),
and
Mistral-NEMO-8B
(NVIDIA,
2024)—to assess their capability in detect-
ing toxicity across various language varieties.
We compute accuracy and F1 scores, followed

--- Page 5 ---

by evaluating consistency scores for all models
and dialects to understand their performance and
stability.
• AYA-23-12B: A multilingual language model that
focuses on 23 languages for enhanced depth, aim-
ing to provide a balance between language diver-
sity and modeling accuracy. AYA-23 builds on
the previous Aya models, achieving superior per-
formance for the covered languages compared
to it’s extended multilingual counterpart AYA-
101 (Üstün et al., 2024).
• Phi-3 Mini-3.8B: A compact yet powerful lan-
guage model, trained on 3.3 trillion tokens. It
features multilingual long-context capabilities
and is small enough to be deployed on mobile
devices, making it a versatile choice for robust
and safe language understanding.
• Mistral-NEMO-8B: This is a pruned 8B param-
eter version derived from the larger Mistral
NeMo-12B model which was originally trained
with quantization-aware techniques, enabling ef-
ficient FP8 inference without performance degra-
dation. Mistral-NEMO-8B underwent advanced
two-stage instruction fine-tuning and preference
optimization.
For the remainder of this paper and the results
section, we refer to Mistral-NEMO-8B as NeMo,
AYA-23-12B as Aya-23, and Phi-3 Mini-3.8B as
Phi-3.
5
Results and Analysis
Broad model comparisons
In Fig. 4, we report
the average F1 scores for each language group and
for all three models. For more interpretable evalua-
tion, we converted the 10 continuous point Toxigen
intent labels and the LLM-predicted toxicity into
bins of 3 and 5, then computed accuracy and F1
scores in a multiclass format. For aggregated F1
scores (avg.) across language clusters, NeMo con-
sistently achieves higher performance compared
to Phi-3 and Aya, especially in the 3-class evalu-
ation setup. NeMo’s superior performance can be
attributed to its exposure to multilingual instruction
tuning, which helps it handle diverse languages and
dialects more effectively. However, while Aya-23
is also tuned on 23 languages, it still struggles to
outperform NeMo and, at times, even lags behind the
much smaller Phi-3 model. Despite their strengths,
the overall agreement between human labels and
all three models remains low, indicating a signifi-
cant gap in aligning model predictions with human
judgment.
Results across language clusters
The models
exhibited varying performance across different lan-
guage clusters. In high-resource languages like En-
glish, Norwegian, and Chinese, NeMo consistently
performed well, with Aya-23 also showing strong
results. However, in lower-resource languages such
as Sotho-Tswana and Kurdish, all models struggled,
highlighting the performance gap in these under-
represented languages. Interestingly, in some of
these lower-resource languages, Phi-3, despite its
smaller size, performed comparably to NeMo, nar-
rowing the performance disparity in certain clusters.
Highest Scoring Varieties and Dialectal Gap
In
Table 2, we present the highest scoring dialects for
each language cluster. The results show a gap be-
tween the best performing varieties and the stan-
dard or high-resource dialects, which are often
considered representative of their clusters. The
highest scoring variety for each model does not
always align with the standard dialect (underlined).
This indicates that models may perform better on
less common or non-standard varieties. These find-
ings highlight a potential dialectal gap, where high-
resource dialects are not necessarily the most favor-
able in terms of model performance.
LLM Consistency Evaluation
As shown in Ta-
ble 3, the three global consistency scores for all
models reveal that dialectal consistency is slightly
lower than multilingual consistency, though the gap
between the two is relatively small. This indicates
that LLMs can handle both multilingual and di-
alectal variations reasonably well. However, NeMo
notably struggles more with dialectal robustness
compared to the other models. However, the pri-
mary challenge remains improving LLM-human
agreement, which consistently shows the weakest
performance across all models.
We also report the individual dialectal consis-
tency within each language cluster in Table 4. We
observe, NeMo shows drops in dialectal consis-
tency, particularly with Finnish (87.5%) and Lat-
vian (86.0%), both high-resource language groups.
It also struggles with Bengali and Common Turkic,
indicating recurring challenges in managing dialec-
tal variations within these clusters. The structural
and linguistic diversity of these languages suggests

--- Page 6 ---

English
Bengali
Norwegian
Chinese
Arabic
Common turkic
Latvian
Finnish
Kurdish
Sotho-tswana
Average
Language Cluster
0
10
20
30
40
50
60
70
F1 Score (%)
57.2
56.0
53.9
52.9
51.7
47.2
45.1
39.3
35.9
27.3
46.6
36.2
28.7
31.2
33.1
32.5
26.9
26.1
20.9
19.3
11.5
26.6
57.0
34.8
40.1
43.4
46.7
37.6
31.9
31.4
33.4
32.7
38.9
38.9
18.0
26.3
30.3
33.5
22.6
20.1
20.3
21.5
21.4
25.3
57.4
34.3
41.1
42.8
44.5
38.9
34.8
32.9
34.2
34.1
39.5
21.0
12.3
14.9
16.1
15.3
15.1
12.4
12.7
13.0
13.5
14.6
F1 Scores by Language Cluster and Model
NeMo (bin=5)
NeMo (bin=3)
Phi-3 (bin=5)
Phi-3 (bin=3)
Aya-23 (bin=5)
Aya-23 (bin=3)
Figure 4: We compute F1 scores for each language cluster by averaging over all dialects. The original ToxiGen
intent labels, which range continuously from 1 to 5, are converted into bins of 3 and 5 for evaluation. The results
indicate an overall low agreement (below 50%) with human annotations, where NeMo has the highest scores. The
overall performance tends to decrease for low-resource language varieties
Language Cluster
NeMo
Aya-23
Phi-3
Arabic
Standard Arabic
North Mesopotamian Ara-
bic
North Mesopotamian Ara-
bic
Bengali
Standard
Standard
Dhaka
Chinese
Classical-Middle-Modern
Sinitic (Simplified)
Classical-Middle-Modern
Sinitic (Simplified)
Classical-Middle-Modern
Sinitic (Simplified)
Common Turkic
Central Oghuz
Central Oghuz
North Azerbaijani
English
Standard
Standard
Standard
Finnish
Finnish
Lansi-Uusimaa
Keski-Karjala
Kurdish
Northern Kurdish
Central Kurdish
Northern Kurdish
Latvian
Latvian
Latvian
East Latvian
Norwegian
Norwegian Nynorsk
Norwegian Nynorsk
Norwegian Bokmal
Sotho-Tswana
Southern Sotho
Southern Sotho
Southern Sotho
Cluster Representative (%)
60.00%
50.00%
20.00%
Table 2: Comparison of Highest Scoring Varieties for Each Language Cluster. The highest performing variety for
each cluster is not always the cluster representative, which generally represents the high-resource or standard variety.
Underlined dialects indicate the cluster representative.
Model
LLM-Human
Multilingual
Dialectal
Phi-3
49.83
99.60
98.40
Aya-23
49.14
99.81
98.50
NeMo
48.48
98.75
91.75
Average
49.15
99.39
96.22
Table 3: Model level Consistency Scores (%, Global)
that NeMo may be sensitive to complex dialectal
features regardless of resource level, highlighting
potential limitations in handling diverse morpho-
logical and syntactic patterns across dialects. In
contrast, Phi-3 and Aya-23 exhibit stronger and
more balanced performance across all language
clusters, with consistently high dialectal consis-
tency scores (averages of 98.2% and 98.5%, re-
spectively). This suggests that both models are
better equipped to handle variations within dialects,
regardless of the resource level or structural char-
acteristics of the language cluster.
LLMs Struggle with Multilingual Instruction
Following:
Both Aya-23 and NeMo show strong
multilingual instruction-following abilities in most
cases, as indicated by the percentage of valid JSON-
formatted outputs in Fig. 5. Aya-23 consistently
performs well across most language clusters, which
can be attributed to its multilingual instruction tun-
ing on 23 languages and its higher parameter count
compared to the other models. All three models
achieve over 92% success in instruction follow-
ing and output formatting in English, but their per-
formance declines when dealing with other lan-

--- Page 7 ---

Norwegian
Chinese
English
Arabic
Sotho-tswana
Bengali
Finnish
Common turkic
Kurdish
Latvian
Average
Language Cluster
0
20
40
60
80
100
Valid Formatted Output (%)
98.6
61.7
92.8
21.5
86.5
79.9
62.1
37.8
67.6
51.7
66.0
98.1
95.4
94.2
86.5
82.4
78.8
77.3
74.8
70.2
60.7
81.8
59.4
93.1
99.2
91.4
37.5
33.4
51.7
74.1
84.3
98.1
72.2
Percentage of Valid Formatted Output by Language Cluster and Model
Model
Phi-3
Aya-23
NeMo
Figure 5: This bar plot shows how different language models (Phi-3, Aya-23, and NeMo) perform in terms of valid
formatted output across multiple language clusters when given multilingual instructions. While all models achieve
high performance for English, their performance varies significantly for other languages. Aya-23 generally performs
better, whereas Phi-3 struggles more across most languages.
Model
NeMo
Phi-3
Aya-23
Language Cluster
Arabic
95.7
98.0
98.7
Bengali
93.6
97.7
99.2
Chinese
97.1
99.5
97.7
Common Turkic
91.7
97.5
94.9
English
96.1
97.8
97.7
Finnish
87.5
98.9
99.0
Latvian
86.0
99.9
98.3
Kurdish
95.7
97.0
99.7
Norwegian
99.6
96.5
99.5
Sotho-Tswana
97.4
98.7
99.9
Average
94.0
98.2
98.5
Table 4: Dialectal Consistency Scores for Different Lan-
guage Clusters (%). Phi-3 and Aya-23 show superior
and consistent dialectal consistency across all language
clusters compared to NeMo, which struggles particularly
with Finnish and Latvian.
guages. Interestingly, the extent of degradation
varies across language clusters for each model. For
example, NeMo also performs well and in some
cases surpasses Aya but its performance drops sig-
nificantly in Bengali (a drop of 46.5 percentage
points from the highest performing model) and
Sotho (a drop of 49.0 percentage points from the
highest performing model). This could further ex-
plain NeMo’s higher Bengali score in Fig. 4, as the
lower number of example count skewed the eval-
uation, making NeMo’s results in Bengali appear
better (56%) wheres the two other models struggled
to get decent scores (34.8% and 34.3%).
LLM Perception of Dialectal Sensitivity:
We
performed an ablation task to gain a deeper under-
standing of how LLMs, acting as judges, perceive
dialectal sensitivity when assessing toxicity. The
goal of this task was to determine whether, accord-
ing to LLMs, dialectal variations affect their judg-
ment of toxicity. The model either acknowledges or
denies the impact, and the results are summarized
in the table. Ideally, the LLMs should recognize
that standard language varieties contain minimal
dialectal cues compared to their dialectal counter-
part.
Here’s the specific part of the prompt provided
to LLMs (see Fig. 3 for the detailed prompt):
Dialectal Sensitivity Impact (D0-D3):
Determine if the LLM’s perception
changes due to dialectal wording given
the input statement:
• D0: No impact (judgment is consistent
across dialects)
• D1: Minor impact (small variation, but
no change in overall toxicity)
• D2:
Noticeable impact (judgment
changes moderately with dialectal
wording)
• D3: Significant impact (substantial
change in toxicity due to dialectal
form)
Input Statement: {Input_statement}

--- Page 8 ---

Language Cluster
Dialect (Min Impact)
Dialect (Max Impact)
∆(Max - Min)
Arabic
Standard arabic (38.95)
Moroccan Arabic (56.41)
17.46
Bengali
Standard (60.45)
Dhaka (65.02)
4.58
Chinese
Classical-Middle-Modern
Sinitic (Traditional) (29.10)
Cantonese (54.63)
25.53
Common Turkic
Central oghuz (34.03)
South Azerbaijani (75.30)
41.27
English
Standard (22.79)
Southeast American Enclave
(61.81)
39.02
Finnish
Finnish (35.70)
PohjoinenVarsinais-Suomi
(65.55)
29.86
High German
Latvian (45.21)
East Latvian (66.00)
20.79
Kurdish
Northern Kurdish (67.65)
Central kurdish (76.71)
9.05
Norwegian
Norwegian Nynorsk (42.69)
Norwegian bokmal (45.53)
2.84
Sotho-Tswana
Southern Sotho (76.30)
Northern sotho (79.76)
3.46
Cluster Representatives (%)
60.00%
40.00%
Table 5: Comparison of varieties with the minimum and maximum dialectal impact acknowledgment by LLMs while
judging each language cluster. The percentage points are averaged across the three LLMs. Cluster representatives
are underlined, indicating minimal dialectal sensitivity. The ∆represents the difference between the maximum
and minimum impact percentages. The key takeaway is that standard varieties show minimal impact, non-standard
varieties show maximum impact, and ambiguity arises when defining a single standard variety is not straightforward
(e.g. Northern and Southern Sotho).
In Table 5, we report the language variety with
the highest and lowest percentage of acknowledg-
ment (i.e., the percentage of instances where the
model recognized any of the D1, D2, or D3 lev-
els of impact) for each language cluster. Ideally,
when serving as a judge, the LLM should recognize
that standard varieties, such as Standard English,
contain no significant dialectal nuances and should
respond with D0 (no impact) or show a lower per-
centage of acknowledgment for dialectal impact
(Minimal Impact). Table 5 shows that this is gener-
ally the case for standard varieties.
We observed that the percentage of LLMs ac-
knowledging an impact was significantly lower
when the text was presented in standard varieties,
such as Standard English, Finnish, and Standard
Bengali, with percentages averaging around 60%.
This suggests that, according to the LLMs, their
predictions as a judge show minimal sensitivity to
dialectal differences in these cases. On the other
hand, LLMs acknowledge greater sensitivity when
judging non-standard dialects, indicating a stronger
recognition of dialectal nuances in these variations.
Even when maximum impact occurs in the case
of a cluster representative, such as Northern Sotho,
Norwegian Bokmal, and Central Kurdish, these
cases involve closely related languages where defin-
ing a single standard form is not ideal. In such in-
stances, the delta difference between the maximum
and minimum impacts remains below 10%. This
suggests that while LLMs can effectively detect
dialectal differences, their sensitivity is influenced
by the lack of a clearly defined standard dialect.
Therefore, the more ambiguous the standard form
within a cluster, the lower the impact of dialectal
variation on the model’s judgment.
6
Conclusion and Future Work
We propose a holistic LLM robustness evaluation
framework for handling toxicity across language
varieties. Our findings suggest, a notable gap re-
mains between model predictions and human judg-
ment, emphasizing the need for improvements in
alignment. Additionally, LLMs tend to be more
sensitive to non-standard dialects, indicating that
further advancements are required to enhance their
consistency across diverse language varieties. We
aim to further expand our dataset by incorporat-
ing more utterance-based dialects and introducing
new perturbation methods, leveraging LLMs’ un-
derstanding of dialectal variations.
Limitations
At this point, this study mostly contains synthetic
and machine-translated dialectal varieties except
for one set of spoken utterances (Bengali-Dhaka).
While it would be ideal to conduct this study on au-
thentic data, such data are not easily available and
they are expensive to collect. This low percentage
of real-world dialectal examples is a limitation we
hope to address in the future.

--- Page 9 ---

Acknowledgments
This material is based upon work supported by the
US National Science Foundation under Grants No.
IIS-2125466 and IIS-2327143.
References
Marah Abdin, Jyoti Aneja, Hany Awadalla, Ahmed
Awadallah, Ammar Ahmad Awan, Nguyen Bach,
Amit Bahree, Arash Bakhtiari, Jianmin Bao, Harkirat
Behl, Alon Benhaim, Misha Bilenko, Johan Bjorck,
Sébastien Bubeck, Martin Cai, Qin Cai, Vishrav
Chaudhary, Dong Chen, Dongdong Chen, Weizhu
Chen, Yen-Chun Chen, Yi-Ling Chen, Hao Cheng,
Parul Chopra, Xiyang Dai, Matthew Dixon, Ro-
nen Eldan, Victor Fragoso, Jianfeng Gao, Mei Gao,
Min Gao, Amit Garg, Allie Del Giorno, Abhishek
Goswami, Suriya Gunasekar, Emman Haider, Jun-
heng Hao, Russell J. Hewett, Wenxiang Hu, Jamie
Huynh, Dan Iter, Sam Ade Jacobs, Mojan Javaheripi,
Xin Jin, Nikos Karampatziakis, Piero Kauffmann,
Mahoud Khademi, Dongwoo Kim, Young Jin Kim,
Lev Kurilenko, James R. Lee, Yin Tat Lee, Yuanzhi
Li, Yunsheng Li, Chen Liang, Lars Liden, Xihui
Lin, Zeqi Lin, Ce Liu, Liyuan Liu, Mengchen Liu,
Weishung Liu, Xiaodong Liu, Chong Luo, Piyush
Madan, Ali Mahmoudzadeh, David Majercak, Matt
Mazzola, Caio César Teodoro Mendes, Arindam Mi-
tra, Hardik Modi, Anh Nguyen, Brandon Norick,
Barun Patra, Daniel Perez-Becker, Thomas Portet,
Reid Pryzant, Heyang Qin, Marko Radmilac, Liliang
Ren, Gustavo de Rosa, Corby Rosset, Sambudha Roy,
Olatunji Ruwase, Olli Saarikivi, Amin Saied, Adil
Salim, Michael Santacroce, Shital Shah, Ning Shang,
Hiteshi Sharma, Yelong Shen, Swadheen Shukla, Xia
Song, Masahiro Tanaka, Andrea Tupini, Praneetha
Vaddamanu, Chunyu Wang, Guanhua Wang, Lijuan
Wang, Shuohang Wang, Xin Wang, Yu Wang, Rachel
Ward, Wen Wen, Philipp Witte, Haiping Wu, Xiaoxia
Wu, Michael Wyatt, Bin Xiao, Can Xu, Jiahang Xu,
Weijian Xu, Jilong Xue, Sonali Yadav, Fan Yang,
Jianwei Yang, Yifan Yang, Ziyi Yang, Donghan Yu,
Lu Yuan, Chenruidong Zhang, Cyril Zhang, Jianwen
Zhang, Li Lyna Zhang, Yi Zhang, Yue Zhang, Yunan
Zhang, and Xiren Zhou. 2024. Phi-3 technical report:
A highly capable language model locally on your
phone.
Anjum and Rahul Katarya. 2024. Hate speech, toxicity
detection in online social media: a recent survey
of state of the art and opportunities. International
Journal of Information Security, 23:577–608.
Viraat Aryabumi, John Dang, Dwarak Talupuru,
Saurabh Dash, David Cairuz, Hangyu Lin, Bharat
Venkitesh, Madeline Smith, Kelly Marchisio, Se-
bastian Ruder, Acyr Locatelli, Julia Kreutzer, Nick
Frosst, Phil Blunsom, Marzieh Fadaee, Ahmet Üstün,
and Sara Hooker. 2024. Aya 23: Open weight re-
leases to further multilingual progress.
Guiming Hardy Chen, Shunian Chen, Ziche Liu, Feng
Jiang, and Benyou Wang. 2024. Humans or llms as
the judge? a study on judgement biases.
Marta R. Costa-jussa, James Cross, Onur Çelebi, Maha
Elbayad, Kenneth Heafield, Kevin Heffernan, Elahe
Kalbassi, Janice Lam, Daniel Licht, Jean Maillard,
et al. 2022.
No language left behind: Scaling
human-centered machine translation. arXiv preprint
arXiv:2207.04672.
Adrian de Wynter, Ishaan Watts, Nektar Ege Altın-
toprak, Tua Wongsangaroonsri, Minghui Zhang,
Noura Farra, Lena Baur, Samantha Claudet, Pavel
Gajdusek, Can Gören, Qilong Gu, Anna Kamin-
ska, Tomasz Kaminski, Ruby Kuo, Akiko Kyuba,
Jongho Lee, Kartik Mathur, Petter Merok, Ivana
Milovanovi´c, Nani Paananen, Vesa-Matti Paananen,
Anna Pavlenko, Bruno Pereira Vidal, Luciano Strika,
Yueh Tsao, Davide Turcato, Oleksandr Vakhno, Judit
Velcsov, Anna Vickers, Stéphanie Visser, Herdyan
Widarmanto, Andrey Zaikin, and Si-Qing Chen. 2024.
Rtp-lx: Can llms evaluate toxicity in multilingual sce-
narios?
Nicholas Deas,
Jessica Grieser,
Shana Kleiner,
Desmond Patton, Elsbeth Turcan, and Kathleen McK-
eown. 2023. Evaluation of African American lan-
guage bias in natural language generation. In Pro-
ceedings of the 2023 Conference on Empirical Meth-
ods in Natural Language Processing, pages 6805–
6824, Singapore. Association for Computational Lin-
guistics.
Fahim Faisal, Orevaoghene Ahia, Aarohi Srivastava,
Kabir Ahuja, David Chiang, Yulia Tsvetkov, and An-
tonios Anastasopoulos. 2024. DIALECTBENCH:
An NLP benchmark for dialects, varieties, and
closely-related languages.
In Proceedings of the
62nd Annual Meeting of the Association for Compu-
tational Linguistics (Volume 1: Long Papers), pages
14412–14454, Bangkok, Thailand. Association for
Computational Linguistics.
Thomas Hartvigsen, Saadia Gabriel, Hamid Palangi,
Maarten Sap, Dipankar Ray, and Ece Kamar. 2022.
ToxiGen: A large-scale machine-generated dataset
for adversarial and implicit hate speech detection.
In Proceedings of the 60th Annual Meeting of the
Association for Computational Linguistics (Volume
1: Long Papers), pages 3309–3326, Dublin, Ireland.
Association for Computational Linguistics.
Helia Hashemi, Jason Eisner, Corby Rosset, Benjamin
Van Durme, and Chris Kedzie. 2024. LLM-rubric: A
multidimensional, calibrated approach to automated
evaluation of natural language texts. In Proceedings
of the 62nd Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 13806–13834, Bangkok, Thailand. Association
for Computational Linguistics.
Mika Hämäläinen, Niko Partanen, and Khalid Alnajjar.
2020a. Normalization of different swedish dialects
spoken in finland.

--- Page 10 ---

Mika Hämäläinen, Niko Partanen, and Khalid Alnajjar.
2021. Lemmatization of historical old literary finnish
texts in modern orthography.
Mika Hämäläinen, Niko Partanen, Khalid Alnajjar, Jack
Rueter, and Thierry Poibeau. 2020b. Automatic di-
alect adaptation in finnish and its effect on perceived
creativity.
Nikita Moghe, Arnisa Fazla, Chantal Amrhein, Tom
Kocmi, Mark Steedman, Alexandra Birch, Rico Sen-
nrich, and Liane Guillou. 2024. Machine translation
meta evaluation through translation accuracy chal-
lenge sets.
Sebastian Nordhoff. 2012. Linked data for linguistic
diversity research: Glottolog/langdoc and asjp. In
Christian Chiarcos, Sebastian Nordhoff, and Sebas-
tian Hellmann, editors, Linked Data in Linguistics.
Representing and Connecting Language Data and
Language Metadata, pages 191–200. Springer, Hei-
delberg.
NVIDIA. 2024.
Mistral-nemo: A language model
with 8b parameters.
https://huggingface.
co/nvidia/Mistral-NeMo-Minitron-8B-Base.
Mistral-NEMO model documentation.
Niko Partanen, Mika Hämäläinen, and Khalid Alnaj-
jar. 2019. Dialect text normalization to normative
standard Finnish. In Proceedings of the 5th Work-
shop on Noisy User-generated Text (W-NUT 2019),
pages 141–146, Hong Kong, China. Association for
Computational Linguistics.
Sarthak Roy, Ashish Harshvardhan, Animesh Mukher-
jee, and Punyajoy Saha. 2023. Probing LLMs for
hate speech detection: strengths and vulnerabilities.
In Findings of the Association for Computational Lin-
guistics: EMNLP 2023, pages 6116–6128, Singapore.
Association for Computational Linguistics.
Maja Stahl, Leon Biermann, Andreas Nehring, and Hen-
ning Wachsmuth. 2024. Exploring llm prompting
strategies for joint essay scoring and feedback gener-
ation.
Ahmet Üstün, Viraat Aryabumi, Zheng Yong, Wei-Yin
Ko, Daniel D’souza, Gbemileke Onilude, Neel Bhan-
dari, Shivalika Singh, Hui-Lee Ooi, Amr Kayid, Fred-
die Vargus, Phil Blunsom, Shayne Longpre, Niklas
Muennighoff, Marzieh Fadaee, Julia Kreutzer, and
Sara Hooker. 2024. Aya model: An instruction fine-
tuned open-access multilingual language model. In
Proceedings of the 62nd Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 15894–15939, Bangkok, Thai-
land. Association for Computational Linguistics.
Jiaxin Wen, Pei Ke, Hao Sun, Zhexin Zhang, Chengfei
Li, Jinfeng Bai, and Minlie Huang. 2023. Unveiling
the implicit toxicity in large language models. In Pro-
ceedings of the 2023 Conference on Empirical Meth-
ods in Natural Language Processing, pages 1322–
1338, Singapore. Association for Computational Lin-
guistics.
Caleb Ziems, William Held, Jingfeng Yang, Jwala
Dhamala, Rahul Gupta, and Diyi Yang. 2023. Multi-
VALUE: A framework for cross-dialectal English
NLP. In Proceedings of the 61st Annual Meeting
of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 744–768, Toronto,
Canada. Association for Computational Linguistics.

--- Page 11 ---

Appendix
Detailed Evaluation Results
This section presents the detailed result tables (Tables 6 to 8) summarizing the performance of each model
across different languages and dialects. We report metrics such as accuracy, F1 scores (for both bin=3 and
bin=5 classifications), and the consistency scores for multilingual, dialectal, and LLM-human agreement.
Dialect Sensitivity Evaluation
In this section, we delve into the LLMs’ perception of dialectal sensitivity. We analyze whether the models
acknowledge that dialectal variations influence their toxicity judgments. The results in Table 9 compare
the LLMs’ responses for both standard language datasets and their dialectal counterparts, providing
insights into how dialectal nuances impact model decisions.
Language Variety Table
The language variety table, reported in Table 10, details the specific language clusters and dialects included
in our dataset. It provides an overview of the 10 language clusters and 60 varieties used in the evaluation
process, along with the number of examples for each variety.
We define a language cluster as a group consisting of a primary language and its associated dialects.
Each cluster is named after the primary language, with the **cluster representative** typically being
the standard form or the highest-resourced variety of that language. The remaining dialects within the
cluster are referred to as the varieties of the cluster representative. For consistency and clarity, we follow
the Glottocode naming convention (Nordhoff, 2012) to label the varieties, ensuring that each dialect is
systematically identified.

--- Page 12 ---

ACC(bin=3)
ACC(bin=5)
F1(bin=3)
F1(bin=5)
Language Cluster
Dialect
Arabic
North mesopotamian arabic
53.10
24.70
46.70
15.30
Ta’izzi-adeni arabic
51.30
24.70
44.60
15.20
Tunisian arabic
50.70
24.20
43.40
14.70
South levantine arabic
52.90
25.70
46.70
16.50
Levantine arabic (a:north)
48.60
23.40
41.70
14.40
Standard arabic
51.70
24.40
45.20
15.40
Najdi arabic
52.00
24.20
45.70
15.00
Moroccan arabic
49.40
24.90
41.90
15.10
Egyptian arabic
51.10
24.80
44.80
15.80
Chinese
Cantonese
50.30
25.20
43.90
15.70
Classical-middle-modern sinitic (simplified)
52.00
26.40
45.50
17.30
Classical-middle-modern sinitic (traditional)
47.40
23.90
38.90
15.40
Finnish
Finnish
45.60
24.20
33.40
12.70
Pohjois-satakunta
44.70
24.80
33.10
13.30
Keski-karjala
45.60
24.00
33.40
12.10
Kainuu
44.00
25.20
32.30
14.10
Etela-pohjanmaa
44.10
23.70
33.00
12.80
Etela-satakunta
44.40
24.30
33.00
13.10
Pohjois-savo
45.50
24.10
33.30
12.40
Pohjois-karjala
44.00
23.40
32.40
12.40
Keski-pohjanmaa
44.20
24.50
32.60
13.20
Kaakkois-hame
45.60
24.80
34.20
13.20
Pohjoinenkeski-suomi
45.50
23.90
34.20
12.70
Pohjois-pohjanmaa
43.40
24.40
32.30
13.30
Pohjoinenvarsinais-suomi
44.80
24.60
32.90
12.80
Etela-karjala
44.70
24.90
32.30
13.20
Lansi-uusimaa
45.60
25.40
34.00
13.80
Inkerinsuomalaismurteet
44.70
23.70
32.10
11.80
Lantinenkeski-suomi
42.90
23.30
31.20
12.20
Lansi-satakunta
45.10
23.60
33.90
12.70
Etela-savo
44.00
23.30
31.70
11.90
Lansipohja
43.50
23.50
32.00
12.50
Pohjois-hame
45.40
23.70
33.80
12.10
Etelainenkeski-suomi
44.40
24.80
32.60
12.90
Etela-hame
43.90
23.90
31.70
12.20
Perapohjola
45.20
23.70
34.50
12.50
Kurdish
Central kurdish
46.10
23.40
32.70
11.80
Northern kurdish
45.90
24.70
35.80
14.10
Norwegian
Norwegian nynorsk
49.80
24.20
40.70
14.20
Norwegian bokmal
49.20
24.80
41.60
15.50
High_german
East latvian
45.90
24.60
34.40
13.00
Latvian
47.60
24.30
35.30
11.80
English
Standard
61.20
30.80
59.90
24.20
Southeast american enclave
58.10
29.00
56.10
20.80
Chicano
60.80
29.70
59.50
22.30
Nigerian
59.80
29.20
58.40
21.90
African american vernacular
57.10
27.30
55.30
20.20
Appalachian
58.80
28.90
57.20
21.40
Australian
60.80
28.60
59.40
20.70
Colloquial singapore
59.10
28.30
57.10
20.90
Hong kong
57.60
27.10
55.20
19.40
Indian
57.90
26.30
56.00
18.80
Irish
59.00
28.30
57.20
20.40
Sotho-tswana
Northern sotho
47.60
25.70
34.90
13.50
Southern sotho
47.70
27.10
33.40
13.40
Bengali
Dhaka
45.50
22.90
33.50
11.90
Standard
46.30
22.50
35.00
12.80
Common_turkic
Central oghuz
51.70
25.60
44.90
17.10
South azerbaijani
46.90
25.30
35.00
13.60
North azerbaijani
46.30
24.20
36.70
14.60
Average
-
49.10
25.20
40.40
15.00
Table 6: Evaluation Results for aya-23-8B

--- Page 13 ---

ACC(bin=3)
ACC(bin=5)
F1(bin=3)
F1(bin=5)
Language Cluster
Dialect
Arabic
North mesopotamian arabic
52.50
36.80
49.80
32.60
Ta’izzi-adeni arabic
55.30
37.70
53.10
33.50
Tunisian arabic
52.60
33.80
50.80
30.60
South levantine arabic
53.30
35.50
51.30
32.20
Levantine arabic (a:north)
53.20
34.60
51.00
32.00
Standard arabic
57.80
39.10
55.10
34.10
Najdi arabic
55.20
36.90
53.40
32.60
Moroccan arabic
51.40
35.00
48.80
32.10
Egyptian arabic
54.50
35.60
52.30
32.40
Chinese
Cantonese
57.40
38.90
54.70
33.80
Classical-middle-modern sinitic (simplified)
58.50
41.00
55.10
35.20
Classical-middle-modern sinitic (traditional)
52.70
36.70
48.70
30.20
Finnish
Finnish
53.70
36.20
51.40
31.00
Pohjois-satakunta
42.90
25.40
41.60
23.40
Keski-karjala
43.50
26.20
42.50
24.70
Kainuu
42.60
24.30
41.00
22.20
Etela-pohjanmaa
42.80
27.00
41.60
25.20
Etela-satakunta
43.70
23.70
42.70
22.20
Pohjois-savo
43.90
24.30
43.20
22.10
Pohjois-karjala
42.40
24.60
41.10
22.10
Keski-pohjanmaa
41.40
23.50
40.10
21.20
Kaakkois-hame
39.50
21.30
37.40
18.00
Pohjoinenkeski-suomi
40.80
20.10
37.40
15.60
Pohjois-pohjanmaa
40.80
23.70
38.10
20.60
Pohjoinenvarsinais-suomi
39.10
21.50
36.20
19.00
Etela-karjala
39.30
25.50
36.90
22.20
Lansi-uusimaa
39.10
21.40
35.70
16.80
Inkerinsuomalaismurteet
36.90
23.10
34.20
19.20
Lantinenkeski-suomi
41.60
24.20
38.70
19.70
Lansi-satakunta
37.80
18.70
34.00
14.60
Etela-savo
42.00
24.00
39.60
19.30
Lansipohja
41.50
23.80
39.00
21.50
Pohjois-hame
40.60
23.90
37.10
21.20
Etelainenkeski-suomi
40.80
20.80
36.80
16.30
Etela-hame
42.10
25.10
38.20
20.40
Perapohjola
41.50
26.00
39.10
22.40
Kurdish
Central kurdish
34.00
20.60
32.80
18.00
Northern kurdish
38.30
22.50
39.00
20.60
Norwegian
Norwegian nynorsk
56.80
38.50
54.50
33.50
Norwegian bokmal
56.40
33.50
53.30
28.90
High_german
East latvian
39.00
22.60
38.90
20.20
Latvian
53.00
35.40
51.30
32.00
English
Standard
63.50
44.40
60.10
38.70
Southeast american enclave
58.50
38.90
55.60
35.00
Chicano
61.60
41.80
58.70
36.10
Nigerian
60.30
40.90
57.60
36.50
African american vernacular
59.40
39.40
56.50
35.70
Appalachian
60.00
41.00
57.20
35.60
Australian
58.70
40.70
55.90
36.30
Colloquial singapore
58.30
39.40
56.00
36.30
Hong kong
59.20
39.40
57.10
35.70
Indian
58.90
38.70
56.40
34.40
Irish
60.70
41.10
57.90
37.90
Sotho-tswana
Northern sotho
27.10
13.70
25.40
9.60
Southern sotho
29.70
16.10
29.20
13.40
Bengali
Dhaka
54.50
28.10
52.00
23.50
Standard
60.90
37.60
60.00
33.90
Common_turkic
Central oghuz
53.90
37.40
52.60
32.20
South azerbaijani
38.70
21.50
37.40
18.60
North azerbaijani
52.50
34.20
51.50
30.00
Average
-
48.50
30.50
46.20
26.70
Table 7: Evaluation Results for Mistral-NeMo-Minitron-8B-Instruct

--- Page 14 ---

ACC(bin=3)
ACC(bin=5)
F1(bin=3)
F1(bin=5)
Language Cluster
Dialect
Arabic
North mesopotamian arabic
56.50
39.60
50.80
36.60
Ta’izzi-adeni arabic
51.10
34.20
43.40
29.50
Tunisian arabic
53.00
35.90
45.50
31.50
South levantine arabic
52.70
35.30
45.70
31.40
Levantine arabic (a:north)
54.90
39.90
48.10
37.10
Standard arabic
53.10
34.90
46.80
31.30
Najdi arabic
48.90
39.40
41.70
34.10
Moroccan arabic
54.00
37.40
47.90
33.60
Egyptian arabic
56.20
39.90
50.60
36.80
Chinese
Cantonese
50.10
30.50
45.10
28.10
Classical-middle-modern sinitic (simplified)
50.60
37.00
43.60
33.20
Classical-middle-modern sinitic (traditional)
49.50
34.80
41.50
29.50
Finnish
Finnish
43.90
28.90
30.70
20.70
Pohjois-satakunta
44.90
28.20
31.90
20.50
Keski-karjala
46.60
29.80
32.40
21.60
Kainuu
45.00
27.40
31.50
20.00
Etela-pohjanmaa
44.90
28.30
30.20
19.70
Etela-satakunta
43.60
27.70
30.30
20.40
Pohjois-savo
46.40
30.40
33.40
22.60
Pohjois-karjala
46.30
26.60
34.20
20.00
Keski-pohjanmaa
43.50
26.30
29.90
18.60
Kaakkois-hame
45.60
28.60
31.50
20.60
Pohjoinenkeski-suomi
45.60
28.80
31.70
21.00
Pohjois-pohjanmaa
43.90
24.90
31.00
18.40
Pohjoinenvarsinais-suomi
44.00
26.80
30.90
19.30
Etela-karjala
44.50
28.80
30.40
20.70
Lansi-uusimaa
44.70
27.00
32.00
19.80
Inkerinsuomalaismurteet
46.20
27.60
32.60
20.00
Lantinenkeski-suomi
43.40
27.60
29.40
19.60
Lansi-satakunta
44.30
28.00
31.30
20.60
Etela-savo
44.80
28.50
30.80
20.50
Lansipohja
44.30
27.70
31.20
20.40
Pohjois-hame
44.70
29.90
31.40
21.80
Etelainenkeski-suomi
44.50
28.40
31.40
21.10
Etela-hame
45.70
27.80
32.40
20.10
Perapohjola
45.40
27.40
31.40
19.50
Kurdish
Central kurdish
44.20
26.20
32.80
20.80
Northern kurdish
47.20
29.50
33.90
22.20
Norwegian
Norwegian nynorsk
48.80
32.20
37.40
24.40
Norwegian bokmal
52.20
35.00
42.90
28.10
High_german
East latvian
45.20
27.20
31.80
19.70
Latvian
45.10
28.40
32.10
20.50
English
Standard
63.90
45.60
58.80
43.10
Southeast american enclave
62.20
39.20
57.50
37.90
Chicano
63.30
43.20
58.50
41.50
Nigerian
62.00
40.40
57.20
39.10
African american vernacular
60.00
38.70
55.40
37.50
Appalachian
62.90
41.60
58.00
39.80
Australian
63.70
40.30
58.90
38.90
Colloquial singapore
60.70
40.30
56.00
39.00
Hong kong
58.30
38.10
53.20
36.50
Indian
60.40
38.60
55.60
36.90
Irish
63.40
39.50
58.20
38.00
Sotho-tswana
Northern sotho
45.80
28.80
32.40
22.40
Southern sotho
47.10
27.90
33.00
20.40
Bengali
Dhaka
43.70
21.00
36.60
16.80
Standard
41.40
23.80
33.10
19.20
Common_turkic
Central oghuz
45.40
27.90
35.30
21.80
South azerbaijani
47.70
28.10
39.10
23.80
North azerbaijani
48.10
27.80
38.30
22.20
Average
-
49.80
32.00
39.80
26.50
Table 8: Evaluation Results for Phi-3-mini-4k-instruct

--- Page 15 ---

Phi
Aya
NeMo
Average
Language
Dialect
Arabic
Standard Arabic
34.29
37.44
45.13
38.95
Najdi Arabic
35.50
40.84
53.97
43.44
North Mesopotamian Arabic
33.33
44.71
57.38
45.14
Ta’izzi-Adeni Arabic
38.96
43.29
57.95
46.74
South Levantine Arabic
34.78
51.48
63.29
49.85
Egyptian Arabic
40.39
51.02
63.59
51.67
Tunisian Arabic
37.02
58.86
63.01
52.96
Levantine Arabic (A:North)
38.50
54.75
68.41
53.89
Moroccan Arabic
45.98
56.72
66.55
56.41
Bengali
Standard
45.93
77.52
57.89
60.45
dhaka
57.00
77.74
60.33
65.02
Chinese
Classical-Middle-Modern Sinitic (Traditional)
27.67
25.98
33.66
29.10
Classical-Middle-Modern Sinitic (Simplified)
31.27
36.81
35.11
34.40
Cantonese
55.27
50.11
58.51
54.63
Common turkic
Central Oghuz
23.86
37.35
40.88
34.03
North Azerbaijani
39.33
61.23
52.50
51.02
South Azerbaijani
54.69
79.78
91.43
75.30
English
Standard
28.09
31.07
9.21
22.79
Nigerian
52.23
35.05
43.32
43.53
Chicano
53.75
38.38
40.75
44.29
Irish
50.63
39.76
52.41
47.60
Australian
56.82
39.33
47.42
47.86
Hong Kong
57.69
38.65
56.30
50.88
Appalachian
59.63
42.40
53.32
51.78
Indian
59.62
38.76
57.22
51.86
Colloquial Singapore
62.44
41.83
64.71
56.33
African American Vernacular
65.38
47.07
63.59
58.68
Southeast American Enclave
69.16
50.40
65.88
61.81
Finnish
Finnish
18.91
43.37
44.81
35.70
Keski-Pohjanmaa
25.41
71.01
78.18
58.20
Pohjois-Satakunta
26.00
71.23
80.15
59.13
LantinenKeski-Suomi
21.49
67.64
88.93
59.35
Etela-Satakunta
26.84
71.74
80.08
59.55
Pohjois-Hame
23.70
67.54
88.40
59.88
Etela-Pohjanmaa
21.68
77.07
82.41
60.38
Keski-Karjala
23.46
75.98
81.75
60.40
Etela-Hame
23.19
69.94
93.25
62.13
Lansipohja
25.51
69.71
91.16
62.13
Inkerinsuomalaismurteet
22.01
73.31
91.53
62.28
Kaakkois-Hame
22.98
72.40
91.69
62.36
Etela-Karjala
23.57
71.89
91.95
62.47
Pohjois-Pohjanmaa
26.45
70.34
90.65
62.48
Kainuu
25.62
77.49
84.48
62.53
Perapohjola
24.56
72.24
91.00
62.60
Pohjois-Savo
28.17
77.95
82.29
62.80
Lansi-Satakunta
24.13
71.86
92.64
62.88
Pohjois-Karjala
28.41
76.42
84.92
63.25
EtelainenKeski-Suomi
24.57
72.71
95.50
64.26
PohjoinenKeski-Suomi
22.98
76.14
94.90
64.67
Lansi-Uusimaa
25.57
74.86
94.19
64.87
Etela-Savo
25.00
77.07
92.63
64.90
PohjoinenVarsinais-Suomi
25.86
76.86
93.94
65.55
High german
Latvian
16.10
65.58
53.96
45.21
East Latvian
22.20
86.95
88.85
66.00
Kurdish
Northern Kurdish
26.47
87.93
88.55
67.65
Central Kurdish
57.04
79.30
93.78
76.71
Norwegian
Norwegian Nynorsk
17.51
65.52
45.04
42.69
Norwegian Bokmal
19.93
60.26
56.38
45.53
Sotho-tswana
Southern Sotho
34.63
97.45
96.83
76.30
Northern Sotho
46.02
95.78
97.49
79.76
Average
35.25
61.56
70.43
55.75
Table 9: Percentage of cases where LLMs acknowledge that dialectal variations influence their judgments. The
percentage is significantly lower for standard language varieties, suggesting that while LLMs recognize subtle
variations in dialects, they remain robust in delivering consistent judgments.

--- Page 16 ---

Language Cluster
Variety Name
Example Count
Arabic
North Mesopotamian Arabic
940
Ta’izzi-Adeni Arabic
940
Tunisian Arabic
940
South Levantine Arabic
940
Levantine Arabic (A:North)
940
Standard Arabic
940
Najdi Arabic
940
Moroccan Arabic
940
Egyptian Arabic
940
Bengali
Standard
940
Dhaka Dialect
380
Chinese
Cantonese
940
Classical-Middle-Modern Sinitic (Simplified)
940
Classical-Middle-Modern Sinitic (Traditional)
940
Finnish
Finnish
940
Pohjois-Satakunta
940
Keski-Karjala
940
Kainuu
940
Etela-Pohjanmaa
940
Etela-Satakunta
940
Pohjois-Savo
940
Pohjois-Karjala
940
Keski-Pohjanmaa
940
Kaakkois-Hame
940
PohjoinenKeski-Suomi
940
Pohjois-Pohjanmaa
940
PohjoinenVarsinais-Suomi
940
Etela-Karjala
940
Lansi-Uusimaa
940
Inkerinsuomalaismurteet
940
LantinenKeski-Suomi
940
Lansi-Satakunta
940
Etela-Savo
940
Lansipohja
940
Pohjois-Hame
940
EtelainenKeski-Suomi
940
Etela-Hame
940
Perapohjola
940
Kurdish
Central Kurdish
940
Northern Kurdish
940
Norwegian
Norwegian Nynorsk
940
Norwegian Bokmal
940
Latvian
East Latvian
940
Latvian
940
English
Standard
940
Southeast American Enclave
799
Chicano
799
Nigerian
799
African American Vernacular
799
Appalachian
799
Australian
799
Colloquial Singapore
799
Hong Kong
799
Indian
799
Irish
799
Sotho-Tswana
Northern Sotho
940
Southern Sotho
940
Common Turkic
Central Oghuz
940
South Azerbaijani
940
North Azerbaijani
940
Table 10: Language cluster and variety names with example count. The cluster representative that we utilize as the
standard variety is underlined in each cluster.

```
