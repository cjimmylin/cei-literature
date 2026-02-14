---\ntitle: "2026-[[Unknown]]-UrduBench An Urdu Reasoning Benchmark using - PDF Extract"\nsource_pdf: "2026/2026-[[Unknown]]-UrduBench An Urdu Reasoning Benchmark using.pdf"\npages: 19\nextracted_at: "2026-02-14T02:17:37.581358"\n---\n\n# PDF Extract: 2026-[[Unknown]]-UrduBench An Urdu Reasoning Benchmark using\n\n**Source PDF:** 2026/2026-[[Unknown]]-UrduBench An Urdu Reasoning Benchmark using.pdf\n**Total Pages:** 19\n\n---\n\n## Content\n\n```\n--- Page 1 ---\n\nUrduBench: An Urdu Reasoning Benchmark using Contextually
Ensembled Translations with Human-in-the-Loop
Muhammad Ali Shafique1, Areej Mehboob1, Layba Fiaz1,
Muhammad Usman Qadeer1, Hamza Farooq1
1Traversaal.ai, Correspondence: ali@traversaal.ai
Abstract
Recent advances in large language models
(LLMs) have led to strong reasoning capa-
bilities; however, evaluating such models in
low-resource languages remains challenging
due to the lack of standardized benchmarks.
In particular, Urdu reasoning evaluation has
been limited by the sensitivity of machine
translation and an emphasis on general lan-
guage tasks rather than reasoning benchmarks.
In this paper, we propose a contextually en-
sembled translation framework with human-
in-the-loop validation that leverages multiple
translation systems to develop Urdu reason-
ing benchmarks while preserving contextual
and structural integrity.
Using this frame-
work, we translate widely adopted reasoning
and question-answering benchmarks, includ-
ing MGSM, MATH-500, CommonSenseQA,
and OpenBookQA, into Urdu, collectively re-
ferred to as UrduBench, and conduct a compre-
hensive evaluation of both reasoning-oriented
and instruction-tuned LLMs across multiple
prompting strategies. Our analysis reveals per-
formance differences across (1) four datasets,
(2) five task difficulty levels, (3) diverse model
architectures, (4) multiple model scaling set-
tings, and (5) language consistency tests. We
find that multi-step and symbolic reasoning
tasks pose significant challenges in Urdu, and
that stable language alignment is a critical pre-
requisite for robust reasoning. Overall, our
work establishes a scalable methodology for
standardized reasoning evaluation in Urdu and
provides empirical insights into multilingual
reasoning failures. This experimental setup is
also broadly applicable to other low-resource
languages. The code and datasets will be pub-
licly released.
1
Introduction
Large Language Models (LLMs) have demon-
strated remarkable performance across reasoning,
comprehension, and knowledge-intensive tasks.
0
2
4
6
8
10
12
14
16
20
30
40
50
60
Gemma-3 (59.4%)
Falcon-h1 (53.5%)
Gemma-3 (44.9%)
R1-Qwen
R1-Qwen
Phi-4
Llama-3.2
MobileLLM-Pro
R1-Qwen
Nemotron
Qwen2.5
MiMo
Mistral
Olmo-3
Llama-3.1
Ministral
Alif-1.0
Aya-Expanse
Rnj
Granite-3.3
Qalb-1.0
Mistral-NeMo
Gemma2
Model Parameters (Billions)
Average Accuracy (%)
Figure 1: Performance scaling of state-of-the-art LLMs
on Urdu benchmark datasets. Average accuracy is the
average of MGSM (CoT), MATH-500 (CoT), Common-
SenseQA (Direct), and OpenBookQA (Direct) accu-
racies. Green highlights the top performing model in
Urdu.
However, the benefits of these advancements are
not evenly distributed across languages.
Low-
resource languages such as Urdu continue to face a
significant gap in standardized evaluation resources.
This disparity not only limits the development of
Urdu-capable LLMs but also restricts fair and rig-
orous comparison across multilingual models.
Existing Urdu evaluation resources discussed in
Section 2 focus primarily on evaluating LLMs’ ca-
pabilities in Natural Language Processing (NLP)
and Natural Language Understanding (NLU) tasks
that include machine translation, sentiment analy-
sis, basic classification, or extractive question an-
swering. While valuable, these evaluations pro-
vide only a partial view of model capability and
do not assess complex reasoning such as mathe-
matical problem solving or common sense reason-
ing. In addition, regional initiatives, including Tit-
uLLM (Nahin et al., 2025) for Bangla, C²RBench
(Wu et al., 2025) for Chinese, (Lamsiyah et al.,
2025) , (Hasanaath et al., 2025) for Arabic, and
MasakhaNER for African languages (Adelani et al.,
1
arXiv:2601.21000v1  [cs.CL]  28 Jan 2026

--- Page 2 ---\n\nEnglish question with choices 
Translation without Context 
Context Aware Translation  
(with human validation) 
The sun is responsible for: 
a. puppies learning new tricks 
b. children growing up and getting old 
c. flowers wilting in a vase 
d. plants sprouting, blooming and wilting 
æورφǬ
 ےّمد دار 
:ےHȄ
     
 
a
. ϖüżϙώʸ
 کے وںɅ φł
 ےň
 
ã Ũ rϊĩرφʱ
 کھŦφǁ
 ےHȄر ںsŮHφį
 
b
Eϖġ ̲TϏł .
 ےؕرφʱ
 وHφǰ
 ےHȄر ںsŮHφį
 اور ھےؕورφń
 وHφǰ
 ےHȄر ںsŮHφį
 
c. 
لداںφ˧
 ںŮφİ
 ھولφŁ
 ھاφǿمر ےHȄر ںsŮHφį
 
dودےφń.
 اگ ےHȄر 
،ںsŮHφį
 ھلφŁ
 ےHȄر ںsŮHφį
 اور ھاφǿمر ےHȄر ںsŮHφį
 
æورφǬ
 ےّمد دار 
:ےHȄ
 
a
. ϖüżϙώʸ
 کے وںɅ φł
 کے ϖüٔż Uϙϐĩ
 
ýχĪرφƘ
 
ϖ ϗ Ϙ
úżϙȊϙˇGŦφ
ǁ
 اφĥ
 
b
. وںɅ φł
 کے ےؕرφʱ
 ےňوHφǰ
 اور ھےؕورφń
 ےňوHφǰ
 اφĥ
 
c. 
لداںφ˧
 ںŮφİ
 وںφƔھوφŁ
 کے ےňھاφǿمر اφĥ
 
dودوںφń.
 کے 
، ϖüżϙώ˪ا 
ϖ ϗ Ϙ
úżϙƬϙھϙφ
Ɲ
 اور ےňھاφǿمر اφĥ
 
Table 1: Example with and without Context Translation
2021) further highlight local efforts to benchmark
complex model behavior in various linguistic set-
tings.
To address this gap, we introduce a reasoning-
focused benchmark for evaluating LLMs in Urdu
by translating four widely adopted datasets in-
cluding Multilingual Grade School Math (MGSM)
(Shi et al., 2023), OpenBookQA (Mihaylov et al.,
2018), CommonSenseQA (Talmor et al., 2019) and
MATH-500 (Hendrycks et al., 2021) into high-
quality Urdu.
These datasets span diverse and
complementary reasoning abilities that have not
been systematically evaluated in Urdu. MGSM
measures mathematical and multi-step reasoning,
OpenBookQA assesses factual and retrieval-based
reasoning, and CommonSenseQA evaluates com-
monsense knowledge and inference.
To ensure translation fidelity, we employ a
contextual ensemble translation framework with
human-in-the-loop validation as examples reported
in Table 1 and Appendix B. Using the resulting
datasets, we benchmark multiple state-of-the-art
reasoning and non-reasoning LLMs under a unified
LM Evaluation Harness protocol, enabling large-
scale and standardized comparison of reasoning
performance in Urdu as shown in Figure 1.
Key Findings
The key findings of this study are
summarized below:
1. Scalable Urdu Translation Framework (§3)
A contextual ensemble translation pipeline
with human-in-the-loop validation produces
high-fidelity Urdu translations of MGSM,
MATH-500, CommonSenseQA, and Open-
BookQA, enabling reproducible evaluation.
2. Comprehensive Model Evaluations (§4.3)
We evaluate diverse reasoning and non-
reasoning LLMs under multiple prompting
strategies in a unified, reproducible setup.
3. Dataset Sensitivity (§5.1) Reasoning bench-
marks (MGSM, MATH-500) show higher
variance than commonsense tasks (Com-
monSenseQA, OpenBookQA), reflecting in-
creased symbolic and multi-step reasoning dif-
ficulty.
4. Impact of Task Difficulty (§5.2) MATH-500
accuracy declines monotonically with diffi-
culty; non-instruction-tuned models degrade
sharply, while DeepSeek-R1-Distill-Qwen-
14B and Phi-4-Mini-Reasoning better sustain
performance.
5. Scaling
Effects
(§5.3)
Larger
models
(Gemma-3-12B-it,
Falcon-h1-7B-Instruct)
generally perform better, but scale alone is
insufficient, as Gemma-3-4B-it outperforms
several 7B models.
6. Reasoning vs. Instruction Tuning (§5.4)
Reasoning-oriented models improve arith-
metic reasoning on MGSM but do not con-
sistently outperform instruction-tuned models
on commonsense benchmarks.
7. Language Consistency Test (§5.5) Higher
Urdu language consistency correlates with
improved reasoning accuracy, particularly on
MGSM under Chain-of-Thought prompting,
where Gemma, Llama, and Qwen show near-
complete Urdu adherence.
2
Related Work
Prior work shows that automatically translated
benchmarks, including Spanish MMLU, introduce
substantial errors that distort evaluation outcomes
(Plaza et al., 2024; Ortiz et al., 2025). Large-scale
multilingual studies across European languages fur-
ther confirm strong sensitivity to translation quality
and services (Thellmann et al., 2024). Machine
2

--- Page 3 ---\n\nFigure 2: Contextual Ensembled Translations Framework with human-in-the-loop
translation research highlights the limitations of ex-
isting evaluation metrics and the instability of LLM-
based translation, particularly for low-resource lan-
guages (López Caro, 2023; Zhu et al., 2024). Re-
cent benchmarks for Bengali and other underrep-
resented languages similarly reveal persistent per-
formance gaps and the necessity of human valida-
tion for reliable evaluation (Bhowmik et al., 2025;
Song et al., 2025). In contrast, we introduce a
scalable, context-aware ensemble translation frame-
work with human-in-the-loop validation for reliable
Urdu reasoning evaluation.
Urdu Benchmarking Datasets
Prior Urdu eval-
uations primarily target general NLP capabili-
ties rather than structured reasoning.
Existing
work compares generalist and specialist models
across Urdu tasks (Arif et al., 2024), studies cross-
lingual QA and translation-induced errors (Kazi
et al., 2025), and probes linguistic competence us-
ing minimal-pair benchmarks such as UrBLiMP
(Adeeba et al., 2025). Other efforts address factual
verification (Ahmad et al., 2025) or classical NLP
tasks. However, these benchmarks do not system-
atically evaluate multi-step mathematical or com-
monsense reasoning. UrduBench addresses this
gap by providing standardized, context-preserving,
and human-validated Urdu translations of estab-
lished reasoning benchmarks.
3
Contextually Ensembled Translation
Method
Constructing reliable reasoning benchmarks in
Urdu requires more than direct machine-translation,
particularly for structured and multi-step reasoning
tasks. We observe that multiple-choice datasets
such as OpenBookQA and CommonSenseQA are
especially prone to contextual fragmentation when
questions and answer options are translated inde-
pendently, leading to semantically misaligned Urdu
outputs. To mitigate this, we employ a contextually
ensembled, human-in-the-loop translation pipeline
that preserves contextual coherence while integrat-
ing multiple translation models and quality controls
as shown in Figure 2. The examples in Appendix
B also illustrate how the context-aware translation
strategy improves translation quality.
3.1
Contextual Translations
We translate MGSM, CommonSenseQA, Open-
BookQA, and MATH-500 into Urdu using a unified
pipeline designed to preserve semantic fidelity, con-
textual coherence, and structural integrity. Each En-
glish instance is first translated independently using
four complementary translation candidates: Indic-
Trans2 (Gala et al., 2023), NLLB (Koishekenov
et al., 2023) , Qwen-3-30B (Yang et al., 2025), and
Gemini-2.5-Pro (Comanici et al., 2025). These can-
didates are selected based on their demonstrated
translation quality scores in prior multilingual eval-
uation studies (Basit et al., 2024; Nahin et al.,
2025). Translation prompts used for these can-
didates are provided in Appendix A.1.
For structured multiple-choice datasets such as
CommonSenseQA and OpenBookQA, we adopt a
context-preserving translation strategy by concate-
nating the question stem with all associated answer
choices prior to translation. This prevents semantic
3

--- Page 4 ---\n\nfragmentation and ensures grammatical and logical
alignment between the question and its answer op-
tions in Urdu. After translation, questions and an-
swer choices are programmatically separated into
their original components.
3.2
Candidate Translation Fusion
GPT-5.1 (OpenAI, 2025) is used to refine candidate
translations by leveraging complementary strengths
across models in lexical choice, grammar, and han-
dling of technical content. It compares candidates
proposed translations against the original English
source to either synthesize an improved Urdu trans-
lation or select the best-performing output. Beyond
quality improvement, this stage also serves as an
automated judging step and limiting the need for
manual human validation. The prompt for best
feature selection and representative examples are
provided in Appendix A.2.
3.3
Heuristic Post-Processing
All translations undergo automatic heuristic valida-
tion tailored to Urdu, as described in Algorithm 1.
The validation detects the following issues in trans-
lated outputs:
• Empty or incomplete translations
• Missing Urdu questions or answer options
• Abnormally short translated questions
• Invalid or missing answer keys
• Excessive residual English content
Most translations pass these checks automati-
cally; flagged cases are reviewed and reprocessed
to ensure accurate and complete translations.
3.4
Human Validation
All candidate translations, including those pro-
duced by GPT-5.1, undergo final review by pro-
fessional native Urdu-speaking annotators fluent
in English. Annotators1 follow detailed guidelines
provided in Appendix C and select the most accu-
rate and natural translation for each instance. This
step is essential for resolving residual ambiguities,
ensuring semantic fidelity, and accounting for cul-
tural and linguistic nuances that automated systems
may overlook. Using this framework, the best qual-
ity translation is selected for inclusion in the fi-
nal benchmark, ensuring linguistic coherence and
1Paid hourly; above min. wage of country of employment.
Dataset
Train
Val
Test
MGSM
8
–
250
CommonSenseQA
9,741
1,221
1,140
OpenBookQA
4,957
500
500
MATH-500
–
–
500
Table 2: Statistics of the translated Urdu datasets.
contextual fidelity suitable for evaluating LLM rea-
soning in Urdu. Dataset statistics for the resulting
benchmarks are reported in Table 2. Human Valida-
tion Win–Loss Statistics Across Translation Candi-
dates in Table 5 while human preference win–loss
comparison between GPT-5.1 refined and human-
edited Urdu translations across four datasets in Fig-
ure 4 in Appendix A.4.
4
Evaluation of Models
In this section, we present a systematic evaluation
of diverse language models on the proposed Urdu
benchmarks, analyzing the effects of model design,
prompting strategy, and task difficulty on reasoning
performance.
4.1
Experimental Setup and Datasets
We evaluate models on an Urdu-translated rea-
soning and question-answering benchmarks intro-
duced in this work: MGSM (arithmetic reason-
ing, evaluated with Direct, CoT, and three Few-
Shot + CoT prompting), MATH-500 (symbolic
mathematics across five difficulty levels, L1–L5),
CommonSenseQA (commonsense reasoning), and
OpenBookQA (knowledge-based scientific reason-
ing). Together, these benchmarks span arithmetic,
formal mathematics, commonsense understanding,
and factual knowledge translated in Urdu.
4.2
Evaluated Models
We evaluate a broad set of open-source and open-
weight LLMs, including instruction-tuned and ex-
plicitly reasoning-oriented models, under a fixed
evaluation protocol as shown in Table 3. The mod-
els span parameter scales from 1B to 14B+, di-
verse multilingual pretraining regimes, and differ-
ent reasoning recipes, including distillation- and
RL-based approaches (e.g., DeepSeek-R1, Phi-4-
Mini-Reasoning) as shown in Table 8. This di-
versity enables controlled analysis of how various
model architectures, model scaling, training strat-
egy, prompting methods, and language consistency,
influence Urdu reasoning performance, particularly
under increasing task difficulty as demonstrated in
4

--- Page 5 ---\n\nTable 3: Evaluation Across All Urdu Benchmark Datasets. Metric: Normalized Accuracy
Model
MGSM
CSQA
OBQA
M500
Avg
Direct
CoT
FS+CoT
Direct
Direct
CoT
%
Non-Reasoning-oriented Open-source LLM
MobileLLM-Pro (1B)
0.40±0.0
0.00±0.0
0.40±0.4
20.8±1.2
27.4±2.0
2.80±0.8
17.0±1.0
Llama-3.2-3B-Instruct
28.4±2.9
40.0±3.0
35.6±3.0
37.1±1.4
29.4±2.0
12.6±1.5
29.7±1.9
Gemma-3-4B-it
54.8±3.2
64.0±3.0
44.0±3.2
40.5±1.4
31.2±2.1
44.2±2.2
44.9±2.2
Nemotron-Mini-4B
18.8±2.5
22.4±2.6
25.6±2.8
38.4±1.4
32.0±2.1
5.00±1.0
24.5±1.8
Falcon-h1-7b-instruct
71.2±2.9
72.4±2.8
70.4±2.9
59.3±1.4
32.8±2.1
49.6±2.2
53.5±2.1
MiMo-7B-Base
29.6±2.9
20.8±2.6
56.4±3.1
37.4±1.4
28.8±2.0
15.4±1.6
25.6±2.2
Mistral-7B-Instruct
0.40±1.2
4.40±1.3
11.6±2.0
27.5±1.3
30.2±2.1
6.60±1.1
17.2±1.5
Olmo-3-7B-Instruct
21.6±2.6
23.6±2.7
24.0±2.7
27.9±1.3
26.6±2.0
20.6±1.8
24.7±1.9
Qwen2.5-7B-Instruct
53.2±3.2
57.6±3.1
60.4±3.1
30.4±1.3
31.6±2.1
41.2±2.2
40.2±2.2
Alif-1.0-8B-Instruct
21.6±2.6
30.4±2.9
43.6±3.1
51.3±1.4
33.4±2.1
10.6±1.4
31.4±1.9
Aya-Expanse-8B
22.0±2.6
30.8±2.9
28.8±2.8
37.5±1.4
31.6±2.1
17.2±1.7
29.2±2.0
Granite-3.3-8b-instruct
8.00±1.7
33.6±3.0
30.4±2.9
28.2±1.3
29.6±0.0
12.4±1.5
25.9±1.4
Qalb-1.0-8B-Instruct
19.6±2.5
17.6±2.4
7.60±1.7
38.4±1.4
32.2±2.1
6.00±1.1
23.6±1.6
Llama-3.1-8B-Instruct
62.0±3.1
62.8±3.1
54.4±3.2
52.8±1.4
33.8±2.1
22.4±1.9
42.9±1.7
Ministral-8B-Instruct-2410
55.2±3.2
58.4±3.1
50.8±3.2
29.6±1.3
30.8±2.1
19.4±1.8
34.6±2.1
Mistral-NeMo-Minitron-8B-Instruct
4.00±1.2
0.40±0.4
0.40±0.4
39.2±1.4
29.0±2.0
17.0±1.7
21.4±1.4
Rnj-1-instruct (8B)
22.4±2.6
13.2±2.2
9.20±1.8
27.9±1.3
26.6±2.0
42.6±2.2
27.6±1.9
Gemma2-9B-it
74.0±2.8
73.6±2.8
75.2±2.7
25.3±1.2
32.8±2.1
37.0±2.2
42.2±2.1
Gemma-3-12B-it
80.4±2.5
80.8±2.5
82.8±2.4
49.4±1.4
37.4±2.2
70.0±2.1
59.4±2.1
Reasoning-oriented Open-source LLM
DeepSeek-R1-Distill-Qwen-1.5B
8.40±1.8
6.40±1.6
9.60±1.9
20.6±1.2
30.0±2.1
21.4±1.8
19.6±1.7
Phi-4-mini-reasoning (4B)
38.4±3.1
32.4±2.9
29.2±2.9
20.4±1.2
32.4±2.1
65.8±2.1
37.7±2.1
DeepSeek-R1-Distill-Qwen-7B
39.6±3.1
42.0±3.1
36.0±3.0
22.9±1.2
31.2±2.1
57.0±2.2
38.3±2.2
DeepSeek-R1-Distill-Qwen-14B
54.4±3.2
59.2±3.1
68.8±2.9
19.4±1.1
31.8±2.1
69.2±2.1
44.9±1.2
CSQA: CommonSenseQA.
OBQA: OpenBookQA.
Average considers MGSM (cot), MATH-500 (cot) CSQA (direct), and OBQA (direct).
Figure 3. All evaluation prompts, configurations
and model details are provided in Appendix D.
4.3
Results
We report normalized accuracy across all Urdu
benchmarks in Table 3, covering arithmetic rea-
soning (MGSM, MATH-500) and commonsense
question answering (CommonSenseQA, Open-
BookQA). Results are aggregated across multiple
prompting strategies to analyze prompt sensitivity,
architectural effects, and overall model robustness
5

--- Page 6 ---\n\n1
2
3
4
5
0
20
40
60
80
100
Difficulty Level
Accuracy (%)
(a) Gemma-3-4B-it
1
2
3
4
5
0
20
40
60
80
100
Difficulty Level
(b) Phi-4-mini-reasoning
1
2
3
4
5
0
20
40
60
80
100
Difficulty Level
(c) Qwen2.5-7B-Instruct
1
2
3
4
5
0
20
40
60
80
100
Difficulty Level
(d) Falcon-h1-7b-instruct
1
2
3
4
5
0
20
40
60
80
100
Difficulty Level
Accuracy (%)
(e) R1-Distill-Qwen-7B
1
2
3
4
5
0
20
40
60
80
100
Difficulty Level
(f) Gemma2-9B-it
1
2
3
4
5
0
20
40
60
80
100
Difficulty Level
(g) Gemma-3-12B-it
1
2
3
4
5
0
20
40
60
80
100
Difficulty Level
(h) R1-Distill-Qwen-14B
Figure 3: Performance of different language models across difficulty levels (L1–L5) on the MATH-500-Urdu
benchmark. Each subplot shows the accuracy degradation pattern as problem difficulty increases.
in a low-resource language setting.
Prompt Sensitivity
Prompting strategy is a ma-
jor determinant of performance on MGSM. Direct
prompting consistently underperforms reasoning-
aware prompts, indicating that most models strug-
gle to implicitly perform multi-step reasoning in
Urdu without explicit guidance. Introducing Chain-
of-Thought (CoT) leads to substantial gains across
nearly all architectures, often yielding large relative
improvements over Direct prompting. However,
the benefits of Few-Shot + CoT are uneven: while
it enables peak performance for some models (e.g.,
Falcon-h1-7B-Instruct), it introduces instability or
regressions for others, particularly smaller or less
multilingual models. This suggests that Urdu ex-
emplars can impose additional distributional shift
rather than uniformly improving generalization.
Overall, CoT emerges as the most reliable prompt-
ing strategy, while few-shot gains remain highly
model-dependent.
Model Architecture
Model architecture and
training objectives strongly influence Urdu rea-
soning performance. Models with stronger mul-
tilingual pretraining and instruction tuning exhibit
more reliable transfer across tasks. Gemma-family
models, particularly Gemma-3-12B-it and Gemma-
3-4B-it, achieve strong performance across both
reasoning-intensive and commonsense bench-
marks, indicating effective cross-lingual abstrac-
tion. In contrast, compact or efficiency-oriented ar-
chitectures (e.g., MobileLLM-Pro, Mistral-NeMo-
Minitron) perform near chance on MGSM and
degrade sharply on MATH-500, reflecting lim-
ited capacity for sustained symbolic reasoning in
Urdu. Reasoning-oriented distilled models (e.g.,
DeepSeek-R1 variants) show moderate but incon-
sistent improvements, suggesting that reasoning
distillation alone does not fully compensate for lim-
ited multilingual grounding.
Overall Performance Across Benchmarks.
De-
spite improvements from prompting and architec-
ture, performance in Urdu remains uneven across
tasks, underscoring the challenges of low-resource
evaluation. Nevertheless, several models achieve
non-trivial accuracy across benchmarks, validating
both the semantic fidelity of the translated datasets
and the feasibility of standardized Urdu evalua-
tion. Gemma-3-12B-it and Falcon-h1-7B-Instruct
achieve the highest overall averages, demonstrat-
ing that strong instruction tuning combined with
multilingual exposure transfers most effectively.
Taken together, the results indicate that reliable
Urdu reasoning requires a combination of explicit
reasoning prompts, sufficient model capacity, and
multilingual-aware training, with no single factor
being sufficient on its own.
5
Analyses and Discussion
In this section, we analyze the results to isolate
how dataset properties, task difficulty, model scale,
6

--- Page 7 ---\n\nreasoning specialization, and language consistency
influence Urdu reasoning performance.
5.1
Impact of Dataset
How does dataset choice affect model performance
in Urdu?
Dataset choice has a strong, task-dependent ef-
fect on model performance in Urdu. Reasoning-
intensive benchmarks such as MGSM and MATH-
500 exhibit the highest variance across models, in-
dicating that multi-step and symbolic reasoning
is particularly sensitive to linguistic transfer and
translation noise in a low-resource setting as shown
in Figure 6 in Appendix E. In contrast, common-
sense and knowledge-based tasks such as Com-
monSenseQA and OpenBookQA remain compara-
tively stable, with tighter performance distributions.
Overall, these results indicate that reasoning depth
and symbolic complexity are primary drivers of
evaluation difficulty in Urdu, while semantic and
knowledge-oriented tasks are more robust to cross-
lingual transfer.
5.2
Impact of Task Difficulty
How does task difficulty affect mathematical rea-
soning in Urdu?
Task difficulty has a systematic impact on perfor-
mance in MATH-500-Urdu. As shown in Figure 3
and Table 9, accuracy declines steadily with in-
creasing problem difficulty, with the largest drops
at higher levels (L4–L5). While most models per-
form well on low-difficulty problems, they de-
grade sharply on more complex subsets, indicat-
ing limited robustness to deep symbolic and multi-
step reasoning in Urdu.
Larger and reasoning-
oriented models such as Gemma-3-12B-it and
DeepSeek-R1-Distill-Qwen-14B retain compara-
tively stronger performance at higher difficulty
levels, but the overall trend shows that linguistic
transfer amplifies the inherent challenges of formal
mathematics.
5.3
Impact of Model Size
How does model scale influence performance in
Urdu?
Model scale contributes to performance on Urdu
benchmarks, but it is not sufficient on its own.
While larger models such as Gemma-3-12B-it
achieve strong overall results, scale does not guar-
antee superiority. Notably, Gemma-3-4B-it out-
performs several larger models, including Llama-
3.1-8B-Instruct and DeepSeek-R1-Distill-Qwen-
7B as shown in Table 3 and in Figure 7, highlight-
ing the importance of multilingual training and
Urdu exposure. Similarly, Gemma-3-12B-it sur-
passes the larger DeepSeek-R1-Distill-Qwen-14B
on reasoning-intensive benchmarks, indicating that
reasoning-oriented scaling alone does not ensure
better low-resource language performance. Over-
all, these results show that model size is only one
factor, with targeted multilingual coverage playing
a critical role in Urdu reasoning quality.
5.4
Impact of Reasoning and Non-Reasoning
Models
How do reasoning-specialized models compare to
general instruction-tuned models in Urdu?
A central goal of UrduBench is to evaluate
whether explicitly reasoning-oriented models out-
perform general instruction-tuned models in Urdu.
As shown in Figure 7, reasoning-specialized mod-
els such as Phi-4-Mini-Reasoning and DeepSeek-
R1-Distill variants exhibit clear gains on MGSM,
particularly under Chain-of-Thought prompting,
indicating that explicit reasoning supervision par-
tially transfers to low-resource languages. How-
ever, these advantages are less consistent on Com-
monSenseQA and OpenBookQA, where large
instruction-tuned models such as Gemma-3-12B-
it and Llama-3.1-8B-Instruct often outperform
reasoning-specialized counterparts. This pattern
suggests that reasoning supervision alone is insuf-
ficient without strong multilingual grounding, and
that performance on commonsense and factual rea-
soning tasks in Urdu depends more on pretraining
diversity and language alignment than on explicit
reasoning objectives alone.
5.5
Language Confusion Test on Reasoning
Models
How well do models maintain Urdu language con-
sistency in their responses?
Language confusion test measures whether a
model produces its final answers consistently in the
target language (Urdu) without unintended code-
switching. For each generated response, special to-
kens and mathematical notation are removed, and
language identification is applied to the cleaned
text. An answer is counted as language-consistent
only if Urdu is the sole detected language; very
short responses are excluded to avoid unreliable
detection.
Formally, Answer Language Consistency for-
mula is taken from the study (Wang et al., 2025)
7

--- Page 8 ---\n\nTable 4: Language Confusion Test on MGSM Urdu CoT.
Accuracy versus Answer language consistency for Urdu
Model
Acc. (%) Cons. (%)
Gemma-3-4B-it
64.0
98.8
Falcon-h1-7b-instruct
72.4
89.2
Qwen2.5-7B-Instruct
57.6
100.0
Llama-3.1-8B-Instruct
62.8
100.0
Ministral-8B-Instruct-2410
58.4
98.8
Gemma2-9B-it
73.6
99.6
Gemma-3-12B-it
80.4
100.0
DeepSeek-R1-Distill-Qwen-14B
59.2
82.0
Higher consistency indicates lower language confusion
or codeswitching.
as:
Lang. Consistency (%) = # answers in Urdu
# total answers ×100
Language confusion directly impacts reason-
ing performance in low-resource languages such
as Urdu.
As shown in Table 4, models with
higher answer-level language consistency achieve
stronger MGSM-CoT accuracy, while residual
code-switching correlates with degraded perfor-
mance. This effect is most pronounced in multi-
step reasoning, where inconsistent language use
disrupts intermediate computations.
Although
larger models such as Gemma-3-12B-it and Llama-
3.1-8B-Instruct generally exhibit stronger language
control, scale alone is insufficient:
reasoning-
oriented models with aggressive distillation or
quantization often show reduced language consis-
tency despite comparable size. Overall, stable lan-
guage alignment is a critical prerequisite for robust
multilingual reasoning.
6
Conclusion
In this study, We introduced UrduBench, to best of
our knowledge, the first standardized reasoning-
focused benchmark suite for Urdu, comprising
translations of MGSM, OpenBookQA, Common-
SenseQA, and MATH-500. Our contextually en-
sembled, with human-in-the-loop framework lever-
ages four diverse translation systems combined
with LLM based feature integration and native
human validation. Our context-aware translation
strategy ensures linguistic coherence by processing
questions and answer choices as unified units.
Through comprehensive evaluation of multi-
ple state-of-the-art reasoning and non-reasoning
models, we provide the first large-scale standard-
ized comparison of LLM reasoning capabilities
in Urdu across mathematical reasoning, common-
sense knowledge, and factual understanding. Be-
yond advancing Urdu NLP, our methodology estab-
lishes a scalable framework for adapting standard-
ized benchmarks to other low-resource languages.
We also refer to this reasoning benchmark suite
as "Miyar", which in Urdu denotes a standard or
benchmark, reflecting a measure of reasoning qual-
ity in Urdu.
Acknowledgments
ChatGPT 5.2 was used for grammatical refinement.
The authors take full responsibility for the technical
content of this paper.
References
Farah Adeeba, Brian Dillon, Hassan Sajjad, and Rajesh
Bhatt. 2025. Urblimp: A benchmark for evaluating
the linguistic competence of large language models
in urdu. Preprint, arXiv:2508.01006.
David Ifeoluwa Adelani, Jade Abbott, Graham Neu-
big, Daniel D’souza, Julia Kreutzer, Constantine
Lignos, Chester Palen-Michel, Happy Buzaaba,
Shruti Rijhwani, Sebastian Ruder, Stephen May-
hew, Israel Abebe Azime, Shamsuddeen H. Muham-
mad, Chris Chinenye Emezue, Joyce Nakatumba-
Nabende, Perez Ogayo, Aremu Anuoluwapo, Cather-
ine Gitau, Derguene Mbaye, and 42 others. 2021.
MasakhaNER: Named entity recognition for African
languages. Transactions of the Association for Com-
putational Linguistics, 9:1116–1131.
Sarfraz Ahmad, Hasan Iqbal, Momina Ahsan, Nu-
maan Naeem, Muhammad Ahsan Riaz Khan, Arham
Riaz, Muhammad Arslan Manzoor, Yuxia Wang, and
Preslav Nakov. 2025.
UrduFactCheck: An agen-
tic fact-checking framework for Urdu with evidence
boosting and benchmarking. In Findings of the Asso-
ciation for Computational Linguistics: EMNLP 2025,
pages 22788–22802, Suzhou, China. Association for
Computational Linguistics.
Samee Arif, Abdul Hameed Azeemi, Agha Ali Raza,
and Awais Athar. 2024. Generalists vs. specialists:
Evaluating large language models for Urdu. In Find-
ings of the Association for Computational Linguistics:
EMNLP 2024, pages 7263–7280, Miami, Florida,
USA. Association for Computational Linguistics.
Abdul Basit, Abdul Hameed Azeemi, and Agha Ali
Raza. 2024. Challenges in Urdu machine translation.
In Proceedings of the Seventh Workshop on Tech-
nologies for Machine Translation of Low-Resource
Languages (LoResMT 2024), pages 44–49, Bangkok,
Thailand. Association for Computational Linguistics.
8

--- Page 9 ---\n\nShimanto Bhowmik, Tawsif Tashwar Dipto, Md Sazzad
Islam, Sheryl Hsu, and Tahsin Reasat. 2025. Evaluat-
ing llms’ multilingual capabilities for bengali: Bench-
mark creation and performance analysis. Preprint,
arXiv:2507.23248.
Gheorghe Comanici, Eric Bieber, Mike Schaekermann,
Ice Pasupat, Noveen Sachdeva, Inderjit Dhillon, Mar-
cel Blistein, Ori Ram, Dan Zhang, Evan Rosen, Luke
Marris, Sam Petulla, Colin Gaffney, Asaf Aharoni,
Nathan Lintz, Tiago Cardal Pais, Henrik Jacobs-
son, Idan Szpektor, Nan-Jiang Jiang, and 3416 oth-
ers. 2025. Gemini 2.5: Pushing the frontier with
advanced reasoning, multimodality, long context,
and next generation agentic capabilities. Preprint,
arXiv:2507.06261.
John Dang, Shivalika Singh, Daniel D’souza, Arash
Ahmadian, Alejandro Salamanca, Madeline Smith,
Aidan Peppin, Sungjin Hong, Manoj Govindassamy,
Terrence Zhao, Sandra Kublik, Meor Amer, Viraat
Aryabumi, Jon Ander Campos, Yi-Chern Tan, Tom
Kocmi, Florian Strub, Nathan Grinsztajn, Yannis Flet-
Berliac, and 26 others. 2024. Aya expanse: Combin-
ing research breakthroughs for a new multilingual
frontier. Preprint, arXiv:2412.04261.
DeepSeek-AI. 2025. Deepseek-r1: Incentivizing rea-
soning capability in llms via reinforcement learning.
Preprint, arXiv:2501.12948.
Jay Gala, Pranjal A. Chitale, Raghavan AK, Varun
Gumma, Sumanth Doddapaneni, Aswanth Kumar,
Janki Nawale, Anupama Sujatha, Ratish Puduppully,
Vivek Raghavan, Pratyush Kumar, Mitesh M. Khapra,
Raj Dabre, and Anoop Kunchukuttan. 2023. Indic-
trans2: Towards high-quality and accessible machine
translation models for all 22 scheduled indian lan-
guages. Preprint, arXiv:2305.16307.
Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri,
Abhinav Pandey, Abhishek Kadian, Ahmad Al-
Dahle, Aiesha Letman, Akhil Mathur, Alan Schel-
ten, Alex Vaughan, Amy Yang, Angela Fan, Anirudh
Goyal, Anthony Hartshorn, Aobo Yang, Archi Mi-
tra, Archie Sravankumar, Artem Korenev, Arthur
Hinsvark, and 542 others. 2024. The llama 3 herd of
models. Preprint, arXiv:2407.21783.
Ahmed Abul Hasanaath, Aisha Alansari, Ahmed Ashraf,
Salmane Chafik, Hamzah Luqman, and Saad Ezzini.
2025.
AraReasoner: Evaluating reasoning-based
LLMs for Arabic NLP. In Findings of the Associa-
tion for Computational Linguistics: EMNLP 2025,
pages 18898–18914, Suzhou, China. Association for
Computational Linguistics.
Muhammad Taimoor Hassan, Jawad Ahmed, and
Muhammad Awais. 2026. Qalb: Largest state-of-
the-art urdu large language model for 230m speak-
ers with systematic continued pre-training. Preprint,
arXiv:2601.08141.
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul
Arora, Steven Basart, Eric Tang, Dawn Song, and
Jacob Steinhardt. 2021.
Math-500:
A subset
of the math benchmark.
https://huggingface.
co/datasets/HuggingFaceH4/MATH-500.
500-
problem subset of the MATH benchmark introduced
in “Measuring Mathematical Problem Solving With
the MATH Dataset.”.
Patrick Huber, Ernie Chang, Wei Wen, Igor Fedorov,
Tarek Elgamal, Hanxian Huang, Naveen Suda, Chin-
nadhurai Sankar, Vish Vogeti, Yanghan Wang, Alex
Gladkov, Kai Sheng Tai, Abdelrahman Elogeel, Tarek
Hefny, Vikas Chandra, Ahmed Aly, Anuj Kumar,
Raghuraman Krishnamoorthi, and Adithya Sagar.
2025.
Mobilellm-pro technical report.
Preprint,
arXiv:2511.06719.
Albert Q. Jiang, Alexandre Sablayrolles, Arthur Men-
sch, Chris Bamford, Devendra Singh Chaplot, Diego
de las Casas, Florian Bressand, Gianna Lengyel, Guil-
laume Lample, Lucile Saulnier, Lélio Renard Lavaud,
Marie-Anne Lachaux, Pierre Stock, Teven Le Scao,
Thibaut Lavril, Thomas Wang, Timothée Lacroix,
and William El Sayed. 2023. Mistral 7b. Preprint,
arXiv:2310.06825.
Samreen Kazi, Maria Rahim, and Shakeel Ahmed
Khoja. 2025. Crossing language boundaries: Evalua-
tion of large language models on Urdu-English ques-
tion answering. In Proceedings of the First Workshop
on Natural Language Processing for Indo-Aryan and
Dravidian Languages, pages 141–151, Abu Dhabi.
Association for Computational Linguistics.
Yeskendir Koishekenov, Alexandre Berard, and Vas-
silina Nikoulina. 2023. Memory-efficient NLLB-200:
Language-specific expert pruning of a massively mul-
tilingual machine translation model. In Proceedings
of the 61st Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 3567–3585, Toronto, Canada. Association for
Computational Linguistics.
Salima Lamsiyah, Kamyar Zeinalipour, Samir El am-
rany, Matthias Brust, Marco Maggini, Pascal Bouvry,
and Christoph Schommer. 2025. ArabicSense: A
benchmark for evaluating commonsense reasoning in
Arabic with large language models. In Proceedings
of the 4th Workshop on Arabic Corpus Linguistics
(WACL-4), pages 1–11, Abu Dhabi, UAE. Associa-
tion for Computational Linguistics.
Alexander H. Liu, Kartik Khandelwal, Sandeep Sub-
ramanian, Victor Jouault, Abhinav Rastogi, Adrien
Sadé,
Alan Jeffares,
Albert Jiang,
Alexandre
Cahill, Alexandre Gavaudan, Alexandre Sablayrolles,
Amélie Héliou, Amos You, Andy Ehrenberg, Andy
Lo, Anton Eliseev, Antonia Calvi, Avinash Soori-
yarachchi, Baptiste Bout, and 101 others. 2026.
Ministral 3. Preprint, arXiv:2601.08584.
Álvaro López Caro. 2023. Machine translation evalu-
ation metrics benchmarking: from traditional mt to
llms.
9

--- Page 10 ---\n\nTodor Mihaylov, Peter Clark, Tushar Khot, and Ashish
Sabharwal. 2018. Can a suit of armor conduct elec-
tricity? a new dataset for open book question answer-
ing. Preprint, arXiv:1809.02789.
Shahriar Kabir Nahin, Rabindra Nath Nandi, Sagor
Sarker, Quazi Sarwar Muhtaseem, Md Kowsher,
Apu Chandraw Shill, Md Ibrahim, Mehadi Hasan
Menon, Tareq Al Muntasir, and Firoj Alam. 2025.
TituLLMs: A family of Bangla LLMs with compre-
hensive benchmarking. In Findings of the Associa-
tion for Computational Linguistics: ACL 2025, pages
24922–24940, Vienna, Austria. Association for Com-
putational Linguistics.
Team Olmo, Allyson Ettinger, Amanda Bertsch, Bailey
Kuehl, David Graham, David Heineman, Dirk Groen-
eveld, Faeze Brahman, Finbarr Timbers, Hamish
Ivison, Jacob Morrison, Jake Poznanski, Kyle Lo,
Luca Soldaini, Matt Jordan, Mayee Chen, Michael
Noukhovitch, Nathan Lambert, Pete Walsh, and 49
others. 2025. Olmo 3. Preprint, arXiv:2512.13961.
OpenAI. 2025. Openai. https://openai.com/. Ac-
cessed: 2025-12-04.
Irene Plaza Ortiz, Nina Melero, Cristina del Pozo, Javier
Conde, Pedro Reviriego, Marina Mayor Rocher, and
María Grandury. 2025. Spanish and llm benchmarks:
Is mmlu lost in translation? In 2025 2nd Interna-
tional Generative AI and Computational Language
Modelling Conference (GACLM), pages 104–108.
Irene Plaza, Nina Melero, Cristina del Pozo, Javier
Conde, Pedro Reviriego, Marina Mayor-Rocher, and
María Grandury. 2024.
Spanish and llm bench-
marks: is mmlu lost in translation?
Preprint,
arXiv:2406.17789.
Qwen, :, An Yang, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan
Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan
Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin
Yang, Jiaxi Yang, Jingren Zhou, and 25 oth-
ers. 2025.
Qwen2.5 technical report.
Preprint,
arXiv:2412.15115.
Muhammad Ali Shafique, Kanwal Mehreen, Muham-
mad Arham, Maaz Amjad, Sabur Butt, and Hamza
Farooq. 2025. Alif: Advancing urdu large language
models via multilingual synthetic data distillation.
Preprint, arXiv:2510.09051.
Freda Shi, Mirac Suzgun, Markus Freitag, Xuezhi Wang,
Suraj Srivats, Soroush Vosoughi, Hyung Won Chung,
Yi Tay, Sebastian Ruder, Denny Zhou, Dipanjan Das,
and Jason Wei. 2023. Language models are multi-
lingual chain-of-thought reasoners. In The Eleventh
International Conference on Learning Representa-
tions.
Yewei Song,
Lujun Li,
Cedric Lothritz,
Saad
Ezzini, Lama Sleem, Niccolo Gentile, Radu State,
Tegawendé F. Bissyandé, and Jacques Klein. 2025.
Is small language model the silver bullet to low-
resource languages machine translation? Preprint,
arXiv:2503.24102.
Alon Talmor, Jonathan Herzig, Nicholas Lourie, and
Jonathan Berant. 2019. CommonsenseQA: A ques-
tion answering challenge targeting commonsense
knowledge. In Proceedings of the 2019 Conference
of the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies, Volume 1 (Long and Short Papers), pages
4149–4158, Minneapolis, Minnesota. Association for
Computational Linguistics.
Gemma Team, Aishwarya Kamath, Johan Ferret, Shreya
Pathak, Nino Vieillard, Ramona Merhej, Sarah Perrin,
Tatiana Matejovicova, Alexandre Ramé, Morgane
Rivière, Louis Rouillard, Thomas Mesnard, Geoffrey
Cideron, Jean bastien Grill, Sabela Ramos, Edouard
Yvinec, Michelle Casbon, Etienne Pot, Ivo Penchev,
and 197 others. 2025. Gemma 3 technical report.
Preprint, arXiv:2503.19786.
Gemma Team, Morgane Riviere, Shreya Pathak,
Pier Giuseppe Sessa, Cassidy Hardin, Surya Bhupati-
raju, Léonard Hussenot, Thomas Mesnard, Bobak
Shahriari, Alexandre Ramé, Johan Ferret, Peter Liu,
Pouya Tafti, Abe Friesen, Michelle Casbon, Sabela
Ramos, Ravin Kumar, Charline Le Lan, Sammy
Jerome, and 179 others. 2024. Gemma 2: Improving
open language models at a practical size. Preprint,
arXiv:2408.00118.
Klaudia Thellmann, Bernhard Stadler, Michael Fromm,
Jasper Schulze Buschhoff, Alex Jude, Fabio Barth,
Johannes Leveling, Nicolas Flores-Herr, Joachim
Köhler, René Jäkel, and Mehdi Ali. 2024. Towards
multilingual llm evaluation for european languages.
Preprint, arXiv:2410.08928.
Ashish Vaswani, Mike Callahan, Adarsh Chaluvaraju,
Aleksa Gordi´c, Devaansh Gupta, Yash Jain, Divya
Mansingka, Philip Monk, Khoi Nguyen, Mohit Par-
mar, Michael Pust, Tim Romanski, Peter Rushton,
Ali Shehper, Divya Shivaprasad, Somanshu Singla,
Kurt Smith, Saurabh Srivastava, Anil Thomas, and
4 others. 2025. Rnj-1-Instruct. Instruction-tuned
model release.
Yiming Wang, Pei Zhang, Jialong Tang, Haoran Wei,
Baosong Yang, Rui Wang, Chenshu Sun, Feitong
Sun, Jiran Zhang, Junxuan Wu, Qiqian Cang,
Yichang Zhang, Fei Huang, Junyang Lin, Fei Huang,
and Jingren Zhou. 2025. Polymath: Evaluating math-
ematical reasoning in multilingual contexts. Preprint,
arXiv:2504.18428.
Sajana Weerawardhena, Paul Kassianik, Blaine Nel-
son, Baturay Saglam, Anu Vellore, Aman Priyan-
shu, Supriti Vijay, Massimo Aufiero, Arthur Gold-
blatt, Fraser Burch, Ed Li, Jianliang He, Dhruv Ke-
dia, Kojin Oshiba, Zhouran Yang, Yaron Singer,
and Amin Karbasi. 2025. Llama-3.1-foundationai-
securityllm-8b-instruct technical report. Preprint,
arXiv:2508.01059.
Junru Wu, Tianhao Shen, Linxi Su, and Deyi Xiong.
2025. C²RBench: A Chinese complex reasoning
benchmark for large language models. In Findings of
10

--- Page 11 ---\n\nthe Association for Computational Linguistics: ACL
2025, pages 21031–21050, Vienna, Austria. Associa-
tion for Computational Linguistics.
LLM-Core Xiaomi, :, Bingquan Xia, Bowen Shen,
Cici, Dawei Zhu, Di Zhang, Gang Wang, Hailin
Zhang, Huaqiu Liu, Jiebao Xiao, Jinhao Dong, Liang
Zhao, Peidian Li, Peng Wang, Shihua Yu, Shimao
Chen, Weikun Wang, Wenhan Ma, and 46 others.
2025. Mimo: Unlocking the reasoning potential of
language model – from pretraining to posttraining.
Preprint, arXiv:2505.07608.
Haoran Xu, Baolin Peng, Hany Awadalla, Dongdong
Chen, Yen-Chun Chen, Mei Gao, Young Jin Kim,
Yunsheng Li, Liliang Ren, Yelong Shen, Shuohang
Wang, Weijian Xu, Jianfeng Gao, and Weizhu Chen.
2025. Phi-4-mini-reasoning: Exploring the limits of
small reasoning language models in math. Preprint,
arXiv:2504.21233.
An Yang, Anfeng Li, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao,
Chengen Huang, Chenxu Lv, Chujie Zheng, Day-
iheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao
Ge, Haoran Wei, Huan Lin, Jialong Tang, and 41
others. 2025.
Qwen3 technical report.
Preprint,
arXiv:2505.09388.
Wenhao Zhu, Hongyi Liu, Qingxiu Dong, Jingjing Xu,
Shujian Huang, Lingpeng Kong, Jiajun Chen, and
Lei Li. 2024. Multilingual machine translation with
large language models: Empirical results and anal-
ysis. In Findings of the Association for Computa-
tional Linguistics: NAACL 2024, pages 2765–2781,
Mexico City, Mexico. Association for Computational
Linguistics.
Jingwei Zuo, Maksim Velikanov, Ilyas Chahed, Younes
Belkada, Dhia Eddine Rhayem, Guillaume Kun-
sch, Hakim Hacid, Hamza Yous, Brahim Farhat,
Ibrahim Khadraoui, Mugariya Farooq, Giulia Campe-
san, Ruxandra Cojocaru, Yasser Djilali, Shi Hu, Iheb
Chaabane, Puneesh Khanna, Mohamed El Amine
Seddik, Ngoc Dung Huynh, and 8 others. 2025.
Falcon-h1: A family of hybrid-head language mod-
els redefining efficiency and performance. Preprint,
arXiv:2507.22448.
11

--- Page 12 ---\n\nA
Prompts and Results Used in the Translation Framework
This appendix provides the exact prompts used in our Contextual Ensemble Translation framework with
human-in-the-loop. All translations in the benchmark were generated using the following LLM prompts.
A.1
Qwen 3 and Gemini 2.5 Pro Urdu Contextual Translation Prompt
The prompt below was used to generate Urdu translations directly from English source texts for MGSM.
Translate given text into Urdu.
DO NOT respond the text.
ONLY output the
translation of the text. Maintain natural, fluent, and cultural context in
Urdu translation.
For OpenBookQA, and CommonSenseQA, following prompt was used using Context-aware strategy:
You are a translation expert.
Analyze the given translations against the
original text and create one improved translation by combining the best
features from all of them.
Translate the following English text into Urdu.
Return only a valid JSON
object with two keys:
1. "question": the translated question
2. "choices": an array of translated choice texts (maintain the same order)
Maintain natural, fluent, and culturally appropriate Urdu. Do not include
any explanation or extra text.
Question: {question_stem}
Choices:
{choices_formatted}
Return format:
{"question": "translated question", "choices": ["choice1", "choice2", ...]}
For MATH-500, following prompt was used:
You are an expert translator specializing in translating mathematical content
from English to Urdu while preserving all LaTeX mathematical notation.
Task: Translate the following from English to Urdu.
Critical Rules:
1. NEVER translate or modify ANY LaTeX math expressions — keep all content
inside $ or $$ EXACTLY unchanged
2. NEVER translate mathematical symbols, variables, or formulas
3. Only translate natural language text
4. Preserve exact structure, line breaks, and spacing
5. Use fluent, formal academic Urdu
6. Preserve punctuation and special characters
A.2
GPT-5.1 Prompt for Best Feature Selection
GPT-5.1 was used to merge, refine, and improve candidate translations generated by IndicTrans2, Qwen-
3-30B, Gemini 2.5 Pro, and NLLB.
You are a translation expert.
Analyze the given translations against the
original text and create one improved translation by combining the best
features from all of them.
12

--- Page 13 ---\n\n0
20
40
60
80
100
120
140
160
180
200
220
240
260
MGSM
CommonSenseQA
OpenBookQA
MATH-500
22
47
29
65
97
205
86
67
Number of Wins
GPT-5.1 Refined Wins
Human-Edited Wins
Figure 4: Human preference win–loss comparison between GPT-5.1 refined and human-edited Urdu translations
across four datasets. The stacked bars show the number of wins for each translation method, with win rate
percentages displayed on the right.
A.3
Translation and Heuristic Processing Algorithm
The following algorithm describes the translation and heuristic processing pipeline applied to all translated
samples as described in Algorithm 1.
A.4
Contextually Ensembled Translation Method Stats
Table 5: Human Validation Win–Loss Statistics Across Translation Candidates
Dataset
IndicTrans2
NLLB-200
Qwen-3-30B
Gemini-2.5-Pro
Total
MGSM
3
2
1
125
131
CommonSenseQA
74
52
17
826
969
OpenBookQA
36
27
9
313
385
MATH-500
3
2
51
312
368
Each cell reports the number of instances for which a translation candidate was selected as the final output by native
Urdu-speaking annotators. Higher counts indicate stronger human preference.
13

--- Page 14 ---\n\nAlgorithm 1 Multi-Model Translation with Heuristic Validation and Consensus
Require: Dataset D,
translation models M={IndicTrans2, NLLB, Gemini-2.5-Pro, Qwen-3},
maximum retries K = 5,
minimum length Lmin = 10,
english content ratio threshold τ = 0.3
Ensure: For each sample x, translations Tx = {t(1), t(2), t(3), t(4), tGP T }
1: for each sample x ∈D do
2:
T ←∅{Validated model translations}
3:
for each model m ∈M in parallel do
4:
attempt ←0
5:
valid ←false
6:
while attempt < K and valid = false do
7:
xm ←TRANSLATE(x, m, prompt)
8:
if required fields missing in xm then
9:
Record missing field error
10:
end if
11:
qur ←Urdu question in xm
12:
if qur is empty or |qur| < Lmin then
13:
Record invalid Urdu question
14:
end if
15:
if no Urdu characters in qur or English ratio > τ then
16:
Record mixed-language question
17:
end if
18:
Cur ←Urdu answer choices in xm
19:
if Cur missing or number of choices incorrect then
20:
Record invalid Urdu choices
21:
end if
22:
for each choice c ∈Cur do
23:
if no Urdu characters in c or English ratio > τ then
24:
Record invalid Urdu choice
25:
end if
26:
end for
27:
if answer key missing or invalid then
28:
Record answer key error
29:
end if
30:
if no errors recorded then
31:
T ←T ∪{xm}
32:
valid ←true
33:
else
34:
attempt ←attempt + 1
35:
end if
36:
end while
37:
if valid = false then
38:
T ←T ∪{xm}
39:
end if
40:
end for
41:
tGP T ←GPT-5.1(D, T, prompt)
42:
Tx ←T ∪{tGP T }
43:
Save(Tx)
44: end for
14

--- Page 15 ---\n\nB
Context-Aware Translation Examples
This appendix provides illustrative examples demonstrating how context-aware translation improves the
grammatical coherence and semantic alignment of Urdu multiple-choice questions. Table 6 compares
translations generated with and without contextual information, highlighting the benefits of translating the
full question–choice sequence as a unified input.
 
English question with choices 
Translation without Context 
Context Aware Translation  
(with human validation) 
The sun is responsible for: 
a. puppies learning new tricks 
b. children growing up and getting old 
c. flowers wilting in a vase 
d. plants sprouting, blooming and wilting 
æورφǬ
 ےّمد دار 
:ےHȄ
     
 
a
. ϖüżϙώʸ
 کے وںɅ φł
 ےň
 
ã Ũ rϊĩرφʱ
 کھŦφǁ
 ےHȄر ںsŮHφį
 
b
Eϖġ ̲TϏł .
 ےؕرφʱ
 وHφǰ
 ےHȄر ںsŮHφį
 اور ھےؕورφń
 وHφǰ
 ےHȄر ںsŮHφį
 
c. 
لداںφ˧
 ںŮφİ
 ھولφŁ
 ھاφǿمر ےHȄر ںsŮHφį
 
dودےφń.
 اگ ےHȄر 
،ںsŮHφį
 ھلφŁ
 ےHȄر ںsŮHφį
 اور ھاφǿمر ےHȄر ںsŮHφį
 
æورφǬ
 ےّمد دار 
:ےHȄ
 
a
. ϖüżϙώʸ
 کے وںɅ φł
 کے ϖüٔż Uϙϐĩ
 
ýχĪرφƘ
 
ϖ ϗ Ϙ
úżϙȊϙˇGŦφ
ǁ
 اφĥ
 
b
. وںɅ φł
 کے ےؕرφʱ
 ےňوHφǰ
 اور ھےؕورφń
 ےňوHφǰ
 اφĥ
 
c. 
لداںφ˧
 ںŮφİ
 وںφƔھوφŁ
 کے ےňھاφǿمر اφĥ
 
dودوںφń.
 کے 
، ϖüżϙώ˪ا 
ϖ ϗ Ϙ
úżϙƬϙھϙφ
Ɲ
 اور ےňھاφǿمر اφĥ
 
 
Squirrels spend their fall: 
a. looking for pretty leaves to collect 
b. stockpiling rocks for fighting in the winter 
c. stockpiling pecans for the frigid months 
d. collecting twigs to keep warm 
ریHʃلφ˧
 اںرφŜ
 اφĥ وسمφǎ
 یχŃاررφƠ
 
:ںsŮHφį
 
a
. معφɵ
 ےňرφƘ
 کے ϖüżϙώƑ
 
âصورφȎوφʚ
 FϖüّżTϐĩ
 
لاسφĖ
 رφƘ
 یHʋر ںsŮHφį
 
b
ِوسمφǎ.
 اφİسر ںŮφİ
 ےň ؕرُا کے ϖüżϙώƑ
 دوںχĖرφʱ
 اφĥ رہŴ Ǹد اχĖرφƘ
 
cدψĖدφū.
 سردی کے وںŵ ŭH̥φŒ
 کے ϖüżϙώƑ
 
ںφǃدŦχĩا اφĥ رہŴ Ǹد اχĖرφƘ
 
dرمφƠ.
 
ϖ ϗ
ûżϙȊϙωƝر کے ϖüżϙώƑ
 ہHʆ φō
 دار اسŦφƑ
 معφɵ
 اχĖرφƘ
 
اںψĖرHʃلφ˧
 اںرφŜ
 اφĥ وسمφǎ
  یχŃاررφƠ
 
:ںsŮHφį
 
a
âصورφȎوφʚ.
 FϖüّżTϐĩ
 معφɵ
 ےňرφƘ
 ےňوHφǰ
 
bوںψńسرد.
 ںŮφİ
 یٔφŃاؕرφƔ
  کے ϖüżϙώƑ
 ھرƆφĩ
 رہŴ Ǹد ےňرφƘ
 ےňوHφǰ
 
cدψĖدφū.
 سردی کے وںŵ ŭH̥φŒ
 کے ϖüżϙώƑ
  
Аکں͊
ʲЬʧ
 رہŴ Ǹد ےňرφƘ
 ےňوHφǰ
 
dرمφƠ.
 
J ϖüżTϋǅر کے ϖüżϙώƑ
 اں͉ʲЈeΚĽсʣ
 معφɵ
 ےňرφƘ
 ےňوHφǰ
 
 
Sean was in a rush to get home, but the light 
turned yellow and he was forced to do what? 
a.take time 
b.dawdle 
c.go slowly 
d.ocean 
e.slow down 
 
اںφū
 وφƘ ھرφƟ
 
Fϖ ϗ Ϙ
úżTȿ Uϙ
ƈ
J
ʄ 
φ
ō
 یφʼ
 لدیφŪ
 
،ھیφ
Ł
 
کںŦφƑ
 ک̠ ψĳرؕφʱ
 لŦگφū
 یφʼ
 یّŶφĩ
 لیŦ tφĩ
 یٔŶφ˪وHφǰ
 اور وہ 
سφʹ
 
رŴ Ǹ
 رφʱ
 ورŵ ȿφ
̒
 ا؟Ŧφ˪وHφǰ
 
a
ãφĘو.
 عٔφĴاφǔ
 اχĖرφƘ
 
b
. الؕφĖ
 ولؕŵφǌ
 اχĖرφƘ
 
c. لŦφǃؕد اŦφƑاؕد 
dدرŦمφƅ.
 
e. ہůسHφǅ ٓا لوφŪ
 
اںφū
 وφƘ ھرφƟ
 
Fϖ ϗ Ϙ
úżTȿ Uϙ
ƈ
J
ʄ 
φ
ō
 یφʼ
 لدیφŪ
 
،ھیφ
Ł
 
کںŦφƑ
 ک̠ ψĳرؕφʱ
 لŦگφū
 یφʼ
 یّŶφĩ
 لیŦ tφĩ
 یٔŶφ˪وHφǰ
 اور 
وہ سφʹ
 
رŴ Ǹ
 رφʱ
 ورŵ ȿφ
̒
 ا؟Ŧφ˪وHφǰ
   
 
a
. 
ͅʒͅو اЈ^͉ʹل 
b
. 
ͅʒͅو عٔʕاЈɃ
 اЈLکر 
c. ارƌφĘر ہůسHφǅ ٓا ےňرφƘ
 رφʱ
 
dدرŦمφƅ.
 
e. ارͅʲЈر کم اЈLکر 
The runner was in third place, but he pushed 
harder and thought he might be able to reach 
second. What was beginning to do? 
a.near finish line 
b.finish 
c.get tired 
d.gain ground 
e.trip over 
وہ رχʱر سرےŭ φĕ
 رŴمφŞ
 رφʱ
 
،ھاφŁ
 
کںŦφƑ
 سُا ےň
 اور ورر اφĖگاφƖ
 اور اφŪوφǬ
 ہφʻ
 وہ دφĖاφū
 
دوسرے رŴمφŞ
 رφʱ
 
ě ƉHʄ 
φ
ō
 ۔ϖġکϙωū
 وہ اŦφʸ
 ےňرφƘ
 گاφƖ
 ھا؟φŁ
  
a
ِطφȏ.
 امŦŰ φŪا کے 
ýωĪرφŌ
 
bمŷ φǟ.
 روφƘ
 / کملφİ
 روφƘ
 
cھکφŁ.
 اφĖاφŪ
 
dولŵ Ƞφǎ.
 اφĖوHφǰ
 
eرφƘھوؕφŁ.
 اφĖھاφƝ
 
وہ رχʱر سرےŭ φĕ
 رŴمφŞ
 رφʱ
 
،ھاφŁ
 
کںŦφƑ
 سُا ےň
 اور ورر اφĖگاφƖ
 اور اφŪوφǬ
 ہφʻ
 وہ دφĖاφū
 
دوسرے رŴمφŞ
 رφʱ
 
ě ƉHʄ 
φ
ō
 ۔ϖġکϙωū
 وہ اŦφʸ
 ےňرφƘ
 گاφƖ
 ھا؟φŁ
  
aامیŦŰ φŪا.
 رŴکφƪ
 کے 
ýωĪرφŌ
 اƌ ȿ UƈHʄ φō
 
b
. مŷ φǟ
 اχĖرφƘ
 
cھکφŁ.
 اφĖاφŪ
 
d
ã Ƞ žφǁ.
 لے اφĖاφŪ
 
eرφƘھوؕφŁ.
 اφĖھاφƝ
 
A person wants to start saving money so that 
they can afford a nice vacation at the end of the 
year. After looking over their budget and 
expenses, they decide the best way to save 
money is to 
a.make more phone calls 
b.quit eating lunch out 
c.buy less with monopoly money 
d.have lunch with friends 
 
کχĕا صɼ φ
ȹ
 الφū
 کے رφŜ ٓا ںŮφİ
 کχĕا ھی
φ
ǿ
ا یؕŶھφ
ǿ
 ےňاررφƠ
 کے 
ϖüżϙώƑ
 Gϖ Fϗ
ûسTųTφĕ
 
اφĖا̣ φł
 روعس اχĖرφƘ
 اŦ HφǅاφŪ
 ے۔HȄ
 
FϖüżTϐĩا 
ؕã ȿ φł
 اور 
âاφŪراφŜا اφĥ ہUرٔφʱاφŪ
 
Gϖ ϗ
ûżTŭϙωƒ
 کے 
،عدφĳ
 وہ صلہƂφĘ
 اχĖرφƘ
 ےHȄ
 ہφʻ
 Gϖ Fϗ
ûسTųTφĕ
 ےňا̣ φł
 اφĥ 
ںψĲرŴ Hʆ φō
 ہȜ ψĳرφŝ
 ہφĹ ےHȄ
 ہφʻ
 
aادہψĖ ر.
 
وںŅ
 
رφƔاφĥ
 ردφƘ
 
bرHŋاφĖ.
 رHʃ χōدو اφĥ اφĖھاφƝ
 اφĖھاφƝ
 
ؕھورφǿ
 اŦωĩد 
cولیχńوφńوφǎ.
 کے سوںsų tφĕ
 سے مφƘ
 داریψĖرφŜ
 ںψĲرφƘ
 
dوںŵφǁدو.
 کے ھφŁاφū
 رHʃ χōدو اφĥ اφĖھاφƝ
 ھادφƝ
 
کχĕا صɼ φ
ȹ
 الφū
 کے رφŜ ٓا ںŮφİ
 کχĕا ھی
φ
ǿ
ا یؕŶھφ
ǿ
 ےňاررφƠ
 کے 
ϖüżϙώƑ
 Gϖ Fϗ
ûسTųTφĕ
 
اφĖا̣ φł
 روعس اχĖرφƘ
 اŦ HφǅاφŪ
 ے۔HȄ
 
FϖüżTϐĩا 
ؕã ȿ φł
 اور 
âاφŪراφŜا اφĥ ہUرٔφʱاφŪ
 
Gϖ ϗ
ûżTŭϙωƒ
 کے 
،عدφĳ
 وہ صلہƂφĘ
 اχĖرφƘ
 ےHȄ
 ہφʻ
 Gϖ Fϗ
ûسTųTφĕ
 ےňا̣ φł
 اφĥ 
ںψĲرŴ Hʆ φō
 ہȜ ψĳرφŝ
 ہφĹ ےHȄ
 ہφʻ
 
aادہψĖ ر.
 
وںŅ
 
رφƔاφĥ
 ںψĲرφƘ
 
bرHŋاφĖ.
 رHʃ χōدو اφĥ اφĖھاφƝ
 اφĖھاφƝ
 
ؕھورφǿ
 ںψĲد 
cولیχńوφńوφǎ.
 کے سوںsų tφĕ
 سے مφƘ
 ں͊
ʚد͉ʠرЈũ
 
dوںŵφǁدو.
 کے ھφŁاφū
 رHʃ χōدو اφĥ اφĖھاφƝ
 ںŮٔφĕھاφƝ
 
Table 6: Examples of with and without Context Translation
15

--- Page 16 ---\n\nC
Human Annotation Guidelines
The rubrics provided in Table 7 were given to native Urdu-speaking annotators to guide their evaluation
and selection of the best translation candidate from the ensemble outputs.
 
Marking Criteria 
Evaluation Question 
Correct Example 
Incorrect Example 
1. Response 
Completeness 
Does the translation 
fully capture the 
source text without 
omitting any part? 
Original: The cat sat on the mat. 
Translation: بلی چ ٹا ئی پر ب ی ٹ ھی
 ت ھی۔ 
Original: The cat sat on the mat.  
Translation 1: بلی ب ی ٹ ھی
 ت ھی۔ (Omitting “on 
the mat”)  
Translation 2: I don’t know (No 
response) 
2. Translation vs 
Generation 
Is the output a 
translation and not 
new content 
generation? 
Original: The boy reads a book. 
Translation: ل ڑ کا 
بکت ا ھت ا
پڑ ہے۔ 
Original: The boy reads a book.  
Translation: ل ڑ کا 
بکت ا کے بارے میں سوچ تا 
ہے۔ (New content generated) 
3. Grammar and 
Structure 
Is the grammar and 
structure of the Urdu 
translation accurate? 
Original: She went to the market. 
Translation: وہ باز ار گ ئی۔  
Original: I bought an iPhone 
today. ​
Translation:  
 میں نے 
ج آ
 ا یک   
iPhone
 خ ر یدا۔ 
Original: She went to the market.  
Translation: وہ باز ار گی ا۔ (Incorrect gender 
agreement)  
Original: I bought an iPhone today.  
Translation: -iphone خ ر یدا  میں نے 
ج آ
 ا یک  
(Incorrect placement of English 
equivalent) 
4. Number and 
Date Formats 
Are the number and 
date formats 
preserved as in the 
original? 
Original: The event is on 
12/12/2024.  
Translation: ی ہ 
ب یت قر 
12/12/2024
 کو 
ہے 
Original: The event is on 12/12/2024.  
Translation: ی ہ 
ب یت قر 
۱۲/۱۲/۲۰۲۴
 کو ہے۔  
(Converted to Arabic numerals) 
5. Cultural 
Considerations 
Are idioms translated 
using cultural 
equivalents, not literal 
translations? 
Original: The ball is in your court. 
Translation: فی صلہ 
با 
پ
آ
 کے ہا ت ھ میں 
ہے۔ (Cultural equivalent used) 
Original: The ball is in your court.  
Translation: گی ن د 
با 
پ
آ
 کے 
ٹکور میں ہے۔ 
(Literal translation) 
6. Common Error 
Patterns 
Does the translation 
avoid direct 
transliteration and 
ensure meaningful 
translation? 
Original: He is an experienced 
teacher.​
Translation: وہ ت جر ب ہ کار ا ست اد ہے۔ 
Original: He is an experienced teacher.  
Translation: وہ ا یک ا یکسپر ی نسد ٹی چر ہے۔ (Direct 
transliteration) 
7. Style and 
Register 
Is the translation’s tone 
and formality 
consistent with the 
source text? 
Original: Please submit your 
documents at the earliest 
convenience.  
Translation: براہ کرم اپ نی 
تد ست او یز ا 
ج لد زا ج لد ج مع کرائ یں۔ 
Original: Please submit your documents 
at the earliest convenience. 
Translation: 
تد ست او یز ا دے د یں۔ (Casual 
tone used instead of formal 
Table 7: Overview of the Urdu-translated datasets refinement guidelines.
16

--- Page 17 ---\n\nD
Evaluation Prompts and Configurations
All evaluation prompts are fixed across models and prompting strategies, including Direct, Chain-of-
Thought (CoT), and Few-Shot + CoT (FS+CoT), to ensure comparability. Evaluations are conducted
using lm-eval-harness with a vLLM backend and tensor parallelism set to 4.
MGSM (Arithmetic Reasoning) 
Direct Prompt 
مسئلہ: 
{Urdu math problem} 
 
ِبراہ کرم صرف آخری عددی جواب دیں۔ 
Chain-of-Thought (CoT) 
مسئلہ: 
{Urdu math problem} 
 
مرحلہ وار حل فراہم کریں اور آخر میں جواب دیں۔ 
:نوٹ 
ِبراہ کرم آخری جواب کو \boxed{} میں لکھیں۔ 
Few-Shot + CoT (FS+CoT) 
ذیل میں چند مثالیں دی گئی ہیں۔ انہی کی طرز پر مسئلہ حل کریں۔ 
 
{Few-shot Urdu examples} 
 
مسئلہ: 
{Urdu math problem} 
 
مرحلہ وار حل لکھیں۔ 
\boxed{} 
:نوٹ 
ِبراہ کرم آخری جواب کو میں لکھیں ۔  
 
 
MATH-500 (Symbolic Mathematics) 
Chain-of-Thought (CoT) 
مسئلہ: 
{Urdu math problem} 
 
مرحلہ وار حل لکھیں۔ 
\boxed{} 
:نوٹ 
ِبراہ کرم آخری جواب کو میں لکھیں ۔  
 
 
CommonSenseQA and OpenBookQA 
Direct Prompt 
سوال: 
{Urdu question} 
 
اختیارات: 
A) {Option A} 
B) {Option B} 
C) {Option C} 
D) {Option D} 
E) {Option E} 
 
درست جواب کا حرف لکھیں۔ 
Figure 5: Evaluation prompt for Urdu MGSM, MATH-500, CommonSenseQA, and OpenBookQA
17

--- Page 18 ---\n\n<7B
7B
8B
>8B
MobileLLM-Pro (1B)
Falcon-h1-7B-Instruct
Alif-1.0-8B-Instruct
Gemma2-9B-it
(Huber et al., 2025)
(Zuo et al., 2025)
(Shafique et al., 2025)
(Team et al., 2024)
LLaMA-3.2-3B-Instruct
MiMo-7B-Base
Aya-Expanse-8B
Gemma-3-12B-it
(Grattafiori et al., 2024)
(Xiaomi et al., 2025)
(Dang et al., 2024)
(Team et al., 2025)
Gemma-3-4B-it
Mistral-7B-Instruct
Granite-3.3-8B-Instruct
R1-Distill-Qwen-14B
(Team et al., 2025)
(Jiang et al., 2023)
(DeepSeek-AI, 2025)
Nemotron-Mini-4B
OLMo-3-7B-Instruct
LLaMA-3.1-8B-Instruct
(Olmo et al., 2025)
(Weerawardhena et al., 2025)
R1-Distill-Qwen-1.5B
Qwen2.5-7B-Instruct
Ministral-8B-Instruct
(DeepSeek-AI, 2025)
(Qwen et al., 2025)
(Liu et al., 2026)
Phi-4-Mini-Reasoning (4B)
R1-Distill-Qwen-7B
Mistral-NeMo-8B-Instruct
(Xu et al., 2025)
(DeepSeek-AI, 2025)
RNJ-1-Instruct (8B)
(Vaswani et al., 2025)
Qalb-1.0-8B-Instruct
(Hassan et al., 2026)
Table 8: Categorization of evaluated models by parameter scale
E
Extended Results
Table 9: MATH-500 Urdu Performance by Difficulty Level
Model
L1
L2
L3
L4
L5
Avg
Top-performing LLMs in Math500-Urdu
Gemma-3-4B-it
65.1
58.9
56.2
39.8
22.4
44.2
Phi-4-mini-reasoning (4B)
76.7
67.8
66.7
69.5
56.72
65.8
Qwen2.5-7B-Instruct
76.7
56.7
46.7
32.8
23.1
41.2
Falcon-h1-7b-instruct
76.7
61.1
56.2
46.9
30.6
49.6
DeepSeek-R1-Distill-Qwen-7B
65.1
57.8
60.9
56.3
51.5
57.0
Gemma2-9B-it
74.4
56.7
44.8
29.7
12.7
37.0
Gemma-3-12B-it
86.1
83.3
80.0
69.5
48.5
70.0
DeepSeek-R1-Distill-Qwen-14B
79.1
70.0
76.2
65.6
63.4
69.2
Lx correspond to increasing MATH-500 difficulty levels.
All results are zero-shot, CoT based prompts.
18

--- Page 19 ---\n\nMGSM
(CoT)
CommonSenseQA
OpenBookQA
MATH-500
(CoT)
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
Normalized Accuracy
= 0.38
M = 0.33
= 0.34
M = 0.30
= 0.31
M = 0.31
= 0.30
M = 0.21
Dataset Difficulty Across Urdu Benchmarks
Figure 6: Distribution of model performance across four Urdu benchmarks. Box plots revealing MATH-500 and
MGSM as the most challenging tasks with lower median scores and wider performance variance compared to
CommonSenseQA and OpenBookQA.
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
11
12
13
14
15
20
30
40
50
60
Gemma-3-12B (59.4%)
Falcon-h1-7B (53.5%)
Gemma-3-4B (44.9%)
R1-Qwen-14B
R1-Qwen-7B
Phi-4-mini
Llama-3.2-3B
MobileLLM-Pro
R1-Qwen-1.5B
Qwen2.5-7B
MiMo-7B
Mistral-7B
Olmo-3-7B
Qalb-1.0-8B
Llama-3.1-8B
Ministral-8B
Alif-1.0-8B
Aya-Expanse
Granite-3.3
Mistral-NeMo
Rnj-1
Nemotron-4B
Gemma2-9B
Model Parameters (Billions)
Average Accuracy (%)
Non-Reasoning LLMs
Reasoning-Oriented LLMs
Figure 7: Performance scaling of LLMs on Urdu benchmark datasets. The plot shows average normalized accuracy
across MGSM (CoT), MATH-500 (CoT), CommonsenseQA (Direct), and OpenBookQA (Direct) as a function
of model parameters. Non-reasoning models (blue circles) demonstrate stronger scaling behavior compared to
reasoning-oriented models (red triangles). Gemma-3-12B (green box) achieves the highest performance at 59.4%,
while reasoning-focused models show competitive performance. Blue boxe shows top performing models in 4B and
7B model parameters The dashed line indicates the approximate scaling trend for non-reasoning models.
19
\n```\n