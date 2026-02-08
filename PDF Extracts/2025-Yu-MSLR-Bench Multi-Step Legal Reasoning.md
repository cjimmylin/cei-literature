---
title: "2025-Yu-MSLR-Bench Multi-Step Legal Reasoning - PDF Extract"
source_pdf: "2025-Yu-MSLR-Bench Multi-Step Legal Reasoning.pdf"
pages: 21
extracted_at: "2026-02-07T17:00:46.246175"
---

# PDF Extract: 2025-Yu-MSLR-Bench Multi-Step Legal Reasoning

**Source PDF:** 2025-Yu-MSLR-Bench Multi-Step Legal Reasoning.pdf
**Total Pages:** 21

---

## Content

```
--- Page 1 ---

BENCHMARKING MULTI-STEP LEGAL REASONING AND
ANALYZING CHAIN-OF-THOUGHT EFFECTS IN LARGE
LANGUAGE MODELS
Wenhan Yu1∗
Xinbo Lin2∗
Lanxin Ni3
Jinhua Cheng2†
Lei Sha1†
1School of Artificial Intelligence, Beihang University, Beijing, China
2KoGuan School of Law, Shanghai Jiao Tong University, Shanghai, China
3School of Criminal Law, China University of Political Science and Law, Beijing, China
{yuwenhan, shalei}@buaa.edu.cn,
{linxinbo, chengjinhua}@sjtu.edu.cn,
lanxin.ni.law@gmail.com
ABSTRACT
As large language models (LLMs) exhibit advanced reasoning capabilities in different specialized
domains, their application to legal reasoning tasks is actively being explored. The pursuit of jus-
tice in legal contexts demands not only correct outcomes but also reasoned elaboration, which
necessitates deriving conclusions through logically justified and transparent argumentation. Current
legal benchmarks, despite being cited as reasoning-focused, suffer from three critical limitations:
conflation of factual recall with genuine inference, fragmentation of holistic reasoning processes, and
neglect of reasoning process quality. To bridge these gaps, we construct MSLR, the first Chinese
multi-step legal reasoning dataset centered on legal decision-making. To align with real-world legal
reasoning trajectories, MSLR employs the IRAC framework (Issue-Rule-Application-Conclusion)
to capture expert reasoning traces from official legal decisions. In parallel, we design a scalable
Human-LLM collaborative annotation pipeline that efficiently generates fine-grained step-level
annotations while establishing a reusable methodological framework for multi-step reasoning datasets.
Evaluation of a range of LLMs on MSLR reveals only modest performance, highlighting substantial
challenges in adapting to complex legal reasoning. Further experiments show that Self-Initiated
CoT prompts—created autonomously by the models—consistently improve reasoning coherence
and output quality, outperforming Human-Designed CoT prompts, which often yield ambiguous
results. This work contributes to the broader discourse on LLM reasoning and CoT strategies, offering
practical insights and resources for future research. The dataset and code are publicly available at
https://github.com/yuwenhan07/MSLR-Bench and https://law.sjtu.edu.cn/flszyjzx/index.html.
1
Introduction
Recent breakthroughs in the reasoning capabilities of large language models (LLMs) Huang and Chang [2023], OpenAI
[2024c], DeepSeek-AI [2025] have spurred increasing interest in leveraging them for legal reasoning tasks Ariai and
Demartini [2025]. As LLMs are applied to various legal domains, including legal document summarization Ash et al.
[2024], Liu et al. [2024], Moro et al. [2024], legal question answering Büttner and Habernal [2024], Louis et al. [2024],
Sovrano et al. [2025], and legal judgment prediction Deng et al. [2023], Tong et al. [2024], Wang et al. [2024b],
evaluating their capabilities and limitations becomes critically important. To address this need, specialized legal
benchmarks (e.g., LexGLUE, LEGALBENCH, LEXTREME, LawBench, LexEval) have emerged. These benchmarks
provide targeted datasets and tasks covering legal reasoning, advancing the development of legal artificial intelligence
to some extent.
∗Equal contribution.
†Corresponding authors.
arXiv:2511.07979v3  [cs.AI]  20 Nov 2025

--- Page 2 ---

A PREPRINT - NOVEMBER 21, 2025
Figure 1: A schematic of the MSLR construction and evaluation framework.
However, these benchmarks exhibit three core limitations. First, they often conflate factual recall with genuine legal
reasoning. Tasks range from retrieval-based (e.g., “What is Article 180 of the Criminal Law?”) to reasoning-intensive
(e.g., “Is the defendant liable?”), making it hard to isolate reasoning capabilities.
Second, benchmarks such as LEGALBENCH decompose multi-step reasoning (e.g., IRAC Miller and Charles [2009])
into disconnected subtasks—issue spotting, rule recall, application, and conclusion—assessed separately on heteroge-
neous data. This fragmented design fails to capture the coherent, step-by-step nature of real-world legal reasoning.
Third, current evaluations prioritize final answers while ignoring the reasoning process itself. Yet legal decisions
require not just correct outcomes but also defensible, well-justified logic—known as Reasoned Elaboration White
[1973]. Existing datasets lack annotated reasoning traces, making it impossible to assess faithfulness or explainability
Atkinson et al. [2020].
To address these gaps, we introduce MSLR, a multi-step legal reasoning benchmark aligned with the IRAC framework
(Figure 1). We focus on insider trading—a domain demanding structured legal justification—and collaborate with legal
experts to construct standardized IRAC-Traces, annotating 60K step-level labels across 1,400 official legal decisions.
This granular stepwise dataset: (1) establishes the foundation for process-quality-oriented evaluation metrics, (2) paves
the way for supervising LLMs’ reasoning.
To efficiently scale high-quality annotations, we propose a three-stage Human-LLM collaborative pipeline (PPP): (1)
Preparatory stage. Domain experts design annotation templates and criteria, and provide gold-standard examples. (2)
Pre-screening stage. Multiple LLMs perform preliminary annotation; the optimal model is selected based on quality-cost
efficiency against gold-standard examples. (3) Precision-tuning stage. The optimal LLM generates comprehensive
annotations refined by human annotators adhering to expert-defined criteria. This pipeline not only maintains annotation
quality while significantly reducing marginal costs but also offers methodological insights for constructing multi-step
reasoning datasets in other domains.
Using our novel IRAC Recall metric and an LLM-as-a-Judge framework Gu et al. [2025], we evaluate general, legal,
and reasoning-focused models. Results show that: (1) MSLR is a challenging, unsaturated benchmark (e.g., OpenAI
o1-mini achieves only 72% IRAC Recall); (2) IRAC Recall strongly correlates with expert-aligned LLM judgments; (3)
Human-Designed Chain-of-Thought (CoT) prompts can yield diminishing returns, while Self-Initiated CoT—generated
by the model itself—consistently enhances reasoning quality.
In summary, our main contributions are as follows:
• MSLR Dataset: We construct the first Chinese multi-step legal reasoning benchmark aligned with the IRAC
framework, enabling granular evaluation of the quality and coherence of LLM reasoning across nearly 1,400
cases with 60K step-level annotations.
• PPP Annotation Pipeline: We propose a scalable Human-LLM collaborative pipeline that reduces annotation
costs while preserving quality, providing a methodological blueprint for capturing real-world reasoning traces.
• Reasoning-quality-oriented Metrics: We design dual evaluation metrics demonstrating statistically significant
consistency: (1) IRAC Recall measuring alignment with expert reasoning traces; (2) LLM Score assessing legal
logical coherence.
2

--- Page 3 ---

A PREPRINT - NOVEMBER 21, 2025
• CoT Prompt Insights: We reveal the ambiguous outcomes of Human-Designed CoT and demonstrate the
potential of Self-Initiated CoT as a paradigm for high-quality legal reasoning.
2
Related Work
2.1
Legal Reasoning Benchmark
To foster reliable legal AI applications, multiple international benchmarks for legal reasoning have been established.
LexGLUE Chalkidis et al. [2022] and LegalBench Guha et al. [2023] encompass diverse English-language legal
tasks, LawBench Fei et al. [2024] and LexEval Li et al. [2024] integrate comprehensive Chinese legal domains, while
LEXTREME Niklaus et al. [2023] covers legal tasks across 24 official EU languages. However, most benchmarks
oversimplify downstream legal reasoning tasks into single-label or multi-label classification, leading to a narrow focus
on end-task accuracy while neglecting the quality of reasoning processes Huang and Chang [2023]. Consequently,
it remains unverifiable whether LLMs can genuinely simulate human-like reasoning processes. Recent studies have
developed specialized datasets for complex tasks—such as long-form legal QA Louis et al. [2024], criminal fact
determination Shen et al. [2025], and open-ended legal exams Fan et al. [2025]—to evaluate the quality of LLMs’
reasoning processes. Our work bridges this critical gap by establishing the first benchmark for assessing multi-step
reasoning performance in legal decision-making scenarios.
Although human annotation remains indispensable for the construction of high-quality datasets, its high cost and limited
scalability present significant barriers. Recent studies propose using LLMs for automated annotation as a cost-effective
alternative Tan et al. [2024], yet they face challenges in validation Nasution and Onan [2024], particularly in step-by-step
reasoning contexts Lightman et al. [2023]. A promising paradigm is Human-LLM collaborative annotation Li et al.
[2023], Kim et al. [2024], which leverages LLMs to accelerate the process while maintaining quality through human
validation Wang et al. [2024a]. Our work advances this paradigm by establishing a scalable annotation pipeline for
reasoning trace datasets.
Current legal benchmarks mostly rely on outcome-oriented metrics such as macro-F1, accuracy, or ROUGE, which fail
to effectively evaluate the quality and coherence of reasoning processes. Recently, the LLM-as-a-Judge Gu et al. [2025]
has emerged as a common paradigm to assess the plausibility of generated content, but whether LLM is capable of
judging the quality of legal reasoning remains an open question. We apply this paradigm to evaluate the quality of legal
reasoning and verify its reliability.
2.2
Chain-of-Thought
Chain-of-Thought is a widely adopted prompting technique for LLMs that guides models to think step-by-step Nye
et al. [2021], Wei et al. [2022]. Given its extensive study in mathematical reasoning and consistent positive performance
Lightman et al. [2023], CoT is commonly assumed to benefit nearly all reasoning tasks. Diverse CoT prompting
strategies have been proposed and applied broadly Sahoo et al. [2025], including automatic Zhang et al. [2022],
self-consistency Wang et al. [2023], and logical Zhao et al. [2024] CoT. However, a recent systematic meta-analysis
reveals that CoT yields significant gains primarily in mathematical and symbolic reasoning tasks, while showing
minimal improvements or even detrimental effects in non-symbolic domains such as knowledge, soft reasoning, and
commonsense tasks Sprague et al. [2025]. Since the efficacy of CoT in legal reasoning remains unclear, our work
conducts an exploratory analysis to address this gap.
3
MSLR Dataset
3.1
Data Sources
Our work aims to construct a high-density, high-quality multi-step legal reasoning dataset: MSLR. We therefore
focus on legal decisions from Chinese insider trading cases, primarily because these cases exhibit high complexity and
logical rigor in both factual details and legal rules. On the one hand, insider trading cases typically involve extensive
financial data, temporal information, behavioral patterns and intentions of multiple parties, and long causal chains. On
the other hand, their regulatory frameworks encompass securities law, criminal law, numerous judicial interpretations,
and regulatory provisions. This duality better reflects the robust information integration and analytical capabilities
required of real-world legal professionals in making legal decisions.
Primary data collection encompasses 1,389 legal documents issued by the China Securities Regulatory Commission
(CSRC), the Supreme People’s Procuratorate (SPP), and the Supreme People’s Court (SPC) between 2005 and 2024.
3

--- Page 4 ---

A PREPRINT - NOVEMBER 21, 2025
With an average length of 2,516 Chinese characters per document, this corpus underscores the inherent complexity of
legal reasoning processes.
3.2
Dataset Creation
This dataset is created and validated by a legal expert team from the Center for Empirical Legal Studies of Shanghai Jiao
Tong University, including one professor, two Ph.D. candidates, and four master’s students. To authentically reconstruct
holistic legal reasoning processes in real-word, the professor and Ph.D. candidates distill standardized step-by-step
reasoning traces based on the IRAC framework: IRAC-Traces. Given the labor-intensive nature of dataset construction,
we design a scalable Human-LLM collaborative annotation pipeline structured into three stages:
Preparatory stage. First, based on these IRAC-Traces, we develop structured data annotation templates and criteria
to systematically record the reasoning process of each legal decision. Second, graduate students create gold-standard
examples. To ensure annotation quality, graduate students undergo a two-week pre-training program to strengthen
their legal knowledge and familiarity with annotation guidelines. Before formal annotation, they must perform trial
annotations on 50 cases, achieving 95% alignment with professor annotations. During formal annotation, we adopt a
“2+1" protocol: two annotators independently annotation the same case, and a third annotator reviews and adjudicates
discrepancies. This process yields gold-standard annotations for over 900 cases with high inter-annotator agreement
(Krippendorff’s α = 0.832).
Pre-screening stage. First, we transform the annotation tasks into structured information extraction tasks suitable
for LLMs. Next, we evaluate different LLMs’ performance against gold-standard examples to identify the most
cost-effective model. Experimental results (see Section “Results and Analysis”) demonstrate DeepSeek-V3’s optimal
cost-effectiveness ratio, establishing it as our primary annotation assistant.
Precision-tuning stage. First, building on the optimal model, we further refine prompts for a subset of fields that
are semantically dependent, ambiguous, or irregularly formatted. By optimizing prompt templates and conducting
independent extraction trials, we significantly enhance the accuracy of information extraction for these challenging
fields. Second, to ensure the reliability and accuracy of the optimal model’s annotations, each document’s structured
data undergoes item-by-item review by a legal expert. In cases of significant discrepancies, a second legal expert is
invited to conduct a joint review, ensuring consensus and precision in the final annotations.
Characteristic
MSLR
Document time span
2005–2024
Total number of documents
1,389
Avg. characters per document (chars)
2,516
Avg. structured fields per document
43.03
Total number of structured entries
59,771
Avg. fill rate of key fields (%)
90.58
Table 1: Descriptive statistics of the MSLR dataset.
Leveraging the PPP pipeline, we ultimately annotate 59,771 step-level reasoning labels across 1,389 official legal
decisions. This corresponds to an average of 43 intermediate steps per legal decision, demonstrating the dataset’s faithful
representation of multi-step reasoning in complex legal contexts. These statistics confirm that the dataset achieves
representative scale, structural consistency, and systematic organization. Its stable annotation quality establishes a
robust foundation for subsequent experimental evaluation tasks.
To validate the novelty of the MSLR dataset, we compute ROUGE-1/2/L F1 scores between documents in MSLR and the
comprehensive Chinese legal corpus used during the training of Lawyer LLaMA Huang et al. [2023]. The results show
near-random similarity levels (all F1 < 0.03), significantly below conventional similarity thresholds. This indicates that
MSLR was not included in the pretraining corpus, further establishing its reliability as a contamination-free evaluation
benchmark.
4
Experiment Setup
4.1
Baseline Models
We evaluate a diverse set of LLMs, grouped into three major categories. General models are primarily designed for
instruction following and open-domain tasks. This group includes Llama3-8B-Chinese and Llama3.3-70B-Instruct Meta
4

--- Page 5 ---

A PREPRINT - NOVEMBER 21, 2025
[2024], GLM4-9B GLM [2024], Qwen2.5-7B and Qwen2.5-72B Team [2024], DeepSeek-V3 DeepSeek-AI [2024],
GPT-4 OpenAI [2024b] and GPT-4o OpenAI [2024a]. Legal-domain models are fine-tuned from general models using
legal texts such as statutes and court rulings to improve performance in legal contexts. Representative models in this
category include AIE-51-8-Law, based on Qwen-2.5-3B Instruct Team [2024]; CleverLaw, based on InternLM3-8B-
Instruct Cai et al. [2024]; Law Justice, based on Llama-3.1-8B Instruct Meta [2024]; and Lawyer-LLM Huang et al.
[2023]. Reasoning models incorporate slow-thinking mechanisms such as Chain-of-Thought, Reflection, or Iterative
Verification. This category comprises models such as DeepSeek-R1-Distill-Qwen-1.5B, DeepSeek-R1-Distill-Qwen-7B,
DeepSeek-R1-Distill-Llama-70B DeepSeek-AI [2025], QwQ-32B Team [2025], DeepSeek-R1 DeepSeek-AI [2025],
o1-mini and o3-mini OpenAI [2024c].
All models are evaluated on MSLR dataset, focusing on the two tasks below. To balance generation stability and
output diversity, we set the decoding parameters for all models supporting customization to a uniform configuration
of top-p=0.9 and temperature=0.2. Furthermore, due to computational resource constraints and the cost
associated with API usage, we restrict all models to single-pass inference to generate final outputs. No advanced
inference techniques, such as ensemble methods or self-consistency sampling, are employed.
4.2
Task 1: LLM Automatic Annotation
4.2.1
Experimental Design
To evaluate the annotation capabilities of LLMs in the legal domain, we transform annotation tasks into structured
information extraction tasks compatible with LLMs. These encompass core NLP sub-tasks including named entity
recognition, text classification, and summarization. We design a unified structured information extraction framework
that leverages a zero-shot setup to construct standardized prompts, instructing LLMs to extract key information from
legal texts and output results in a predefined JSON structure with specified fields.
4.2.2
Evaluation Metrics
Two metrics are designed to evaluate the annotation quality of LLMs:
(1) Field Completeness Rate (FCR), which measures the coverage of model outputs over the fields that should be
filled according to the gold-standard examples. Let N be the total number of cases. For the i-th case, let Ri = the
number of non-empty fields in the reference answers, Pi = the number of fields predicted by the model, and Oi = the
number of overlapping fields between prediction and reference. FCR is defined as:
FCR = 1
N
N
X
i=1
Oi
Ri
.
(1)
(2) Overall Accuracy, which reflects the annotation accuracy of the model in the overlapping fields. We classify fields
into two categories: Exa-fields requiring exact matching (e.g., dates, amounts) and Sem-fields requiring semantic
matching (e.g., event descriptions, information summaries). For the i-th case, let Oei = the number of Exa-fields within
overlapping fields, Osi = the number of Sem-fields within overlapping fields.
For Exa-fields, Exact Accuracy is used to measure exact matches between predicted values ˆy and references y across
the Oei overlapping fields:
ExaAcci =
1
Oei
Oei
X
j=1
I(ˆyj = yj),
(2)
where I(·) is the indicator function.
For Sem-fields, Semantic Accuracy uses cosine similarity between embeddings f(·) from ChatLaw-Text2Vec Cui
et al. [2023] to account for semantically equivalent but lexically diverse expressions, considering predictions correct if
similarity exceeds threshold τ = 0.6:
SemAcci =
1
Osi
Osi
X
i=1
I (cos (f(ˆyi), f(yi)) ≥τ) .
(3)
5

--- Page 6 ---

A PREPRINT - NOVEMBER 21, 2025
The final overall accuracy is a weighted average:
OverallAcc = 1
N
N
X
i=1
(Oei
Oi
· ExaAcci + Osi
Oi
· SemAcci).
(4)
4.3
Task 2: LLM Legal Reasoning
4.3.1
Experimental Design
This task aims to systematically evaluate the quality of multi-step reasoning processes in complex legal decision-making
by LLMs. To examine the impact of reasoning CoT prompts on model behavior, we construct three input modes (see
Listing 4.1):
(1) Standard Input (Std): Only basic role setting, task introduction, and case description are provided.
(2) Human-Designed CoT Input (H-CoT): Building upon standard input, we integrate authentic legal reasoning
paths grounded in real-world judicial practice. These paths—distilled by legal experts from empirical case han-
dling—systematically guide models to generate outputs through human-aligned reasoning patterns.
(3) Self-Initiated CoT Input (S-CoT): Building upon standard input, we integrate self-initiated legal reasoning paths
tailored to the model. These paths, constructed by the model based on its intrinsic capabilities, are designed to unlock
its latent reasoning and generation capabilities.
Listing 4.1: Input Modes
Role Setting. You are a seasoned legal expert, proficient in legal reasoning and highly familiar with the legal
regulations governing insider trading cases.
Task Introduction. Please carefully review the case description below. Conduct a comprehensive legal analysis of
the parties’ actions in conjunction with applicable statutes and evidentiary materials, culminating in a determination
of their legal liability. Present a complete chain of reasoning with final conclusions.
[Human-Designed CoT]. Please conduct step-by-step legal analysis following this reasoning chain: Insider
Information Formation →Information Awareness →Trading Behavior →Illegal Gains →Legal Application →
Penalty Outcome.
[Self-Initiated CoT]. Please autonomously construct a legal reasoning path based on the case facts—determine
the most logically sound sequence and judgment structure. Then conduct step-by-step analysis strictly adhering to
your proposed reasoning framework.
Case Description. ...
This comparative setup allows us to evaluate models’ capabilities in multi-step legal reasoning, and to analyze CoT’s
effectiveness in enhancing reasoning quality.
4.3.2
Evaluation Metrics
To evaluate the quality of the reasoning process, We focus on two key dimensions: (1) the alignment between the
reasoning traces of the model and those of the legal experts, and (2) the logical coherence of the reasoning process
itself. Accordingly, we adopt a two-tier evaluation framework comprising:
(1) IRAC Recall, which measures the alignment between LLM-generated reasoning traces and the expert-defined
IRAC-Traces. Let N be the total number of samples. For the i-th sample, let Ri denote the number of reasoning fields in
the expert-defined reference trace, and let Oi denote the number of fields correctly matched by the model. The matched
fields Oi consist of two types: Exa-fields and Sem-fields. The detailed matching criteria are described in Task1. IRAC
Recall is defined as:
IRAC Recall = 1
N
N
X
i=1
Oi
Ri
(5)
.
6

--- Page 7 ---

A PREPRINT - NOVEMBER 21, 2025
Model
FCR
Overall Acc
Llama3-8B-Chinese
76.37
57.43
GLM4-9B
68.85
67.01
Qwen2.5-7B
58.12
57.69
Qwen2.5-72B
57.26
58.69
Llama3.3-70B-Instruct
57.19
64.72
DeepSeek-V3
69.65
77.43
GPT-4
73.28
77.23
GPT-4o
71.33
72.43
AIE-51-8-law
29.67
44.28
Cleverlaw
78.43
61.79
Law-Justice
3.87
39.32
Lawyer-LLM
70.13
57.49
DeepSeek-R1-distill-Qwen-1.5b
32.10
48.60
DeepSeek-R1-distill-Qwen-7b
75.67
61.71
QwQ-32b
71.51
65.74
DeepSeek-R1-distill-Llama-70B
52.72
63.17
DeepSeek-R1
70.24
70.72
o1-mini
64.99
76.45
o3-mini
66.19
74.39
Table 2: Comparative performance of LLMs on the automatic annotation task. The first block of rows corresponds to
General LLMs, the second block corresponds to Legal LLMs, and the third block corresponds to Reasoning LLMs.
(2) LLM Score, which measures the logical coherence of LLM-generated reasoning traces. Following the LLM-as-a-
Judge paradigm [Zheng et al., 2023], we use a high-performing model (e.g., DeepSeek-R1 DeepSeek-AI [2025]) to
automatically evaluate each generated response according to a three-level rubric (A/B/C):
• A: Logically complete and well-structured; covers most key legal elements with rigorous reasoning;
• B: Generally reasonable but contains missing steps, unclear expressions, or incomplete legal analysis;
• C: Disorganized logic, lack of justification, or incorrect application of legal provisions.
The LLM score is computed as:
LLM Score = 1 · NA + 0.5 · NB + 0 · NC
N
,
(6)
where N denotes the total number of evaluated samples.
5
Results and Analysis
We show the potential of MSLR as a useful benchmark for LLMs across multiple dimensions of interest. Here are some
key findings:
- LLM-based automated annotation underperforms on tasks involving highly complex and nuanced reasoning
trajectories. As shown in Table 2, LLMs—including large-scale models like DeepSeek and GPT series—fail to exceed
80% in both FCR and Overall Accuracy on the MSLR dataset. This indicates that LLM automated annotation falls
short of achieving quality comparable to human annotators in terms of both comprehensiveness and accuracy. These
results align with prior findings Koco´n et al. [2023], Nasution and Onan [2024], which highlight that LLMs still exhibit
limitations in zero-shot performance on more challenging and practical tasks compared to human experts. Thus, our
PPP annotation pipeline is not only necessary but also validates a promising paradigm: Human-LLM collaborative
annotation Li et al. [2023], Wang et al. [2024a], where LLMs accelerate the process while preserving the high quality
of human-reviewed annotations.
- The LLM-as-a-Judge paradigm provides a scalable method for evaluating the quality of legal reasoning, with
validity confirmed through dual verification. First, Figure 2 shows a statistically significant positive correlation
between IRAC Recall and LLM Score, indicating strong metric alignment. Second, legal experts independently
7

--- Page 8 ---

A PREPRINT - NOVEMBER 21, 2025
assessed 380 randomly sampled reasoning outputs (20 outputs from each of 19 models). A comparison between these
human ratings and automated ratings from DeepSeek-R1 reveals an 87.96% agreement rate in grade classification,
demonstrating high human-machine consistency. These results confirm that model-generated reasoning steps can be
evaluated both consistently and accurately via LLM-as-a-judge, closely aligning with human expert assessments. Our
work demonstrates that general-domain LLMs are capable of assessing the quality of legal reasoning.
IRAC Recall
LLM Score
Pearson Corr.  ρ=0.85 漏p<0.001漐
Regression Coef. β=1.86 漏p<0.001漐
Pearson Corr.  ρ=0.83 漏p<0.001漐
Regression Coef. β=1.44 漏p<0.001漐
Standard Input
Human-Designed CoT
Figure 2: Pearson correlation analysis and linear fit between IRAC Recall and LLM Score.
- LLMs exhibit limited proficiency in multi-step legal reasoning. As shown in Table 3, the overall performance of
all evaluated models remains suboptimal. Although some large-scale models(e.g., QwQ-32B, Deepseek-R1) achieve
LLM Score exceeding 90%, their IRAC Recall consistently falls short of 75%. This indicates that while the generated
reasoning may appear logically coherent on the surface, it often lacks alignment with the structured reasoning paths
used in real-world legal decision-making. As previously analyzed, there is a significant positive correlation between
IRAC Recall and LLM Score, further validating that IRAC Recall serves as a more objective and structured metric for
assessing models’ true reasoning capabilities in legal tasks.
To further explore models’ performance under few-shot settings, we conducted additional experiments. Due to the
considerable length of legal documents, we adopted a one-shot setup in our experiments (see Figure 3). Results show
that while the one-shot setting leads to a moderate improvement in both IRAC Recall and LLM Score, the overall
performance gains remain limited. This finding aligns with recent findings Louis et al. [2024], Shen et al. [2025], Fan
et al. [2025], which highlight significant room for improvement in LLMs’ handling of complex legal reasoning tasks.
- The impact of identical CoT prompts varies across LLMs, yielding both positive and negative effects. As Table
3 indicates, Human-Designed CoT prompts consistently enhance IRAC Recall and LLM Score for all legal models
and most general models. This demonstrates that infusing models with real-world reasoning paths improves reasoning
quality and logical coherence. Conversely, for specific general models (e.g., Qwen2.5-72B, DeepSeek-V3) and most
reasoning models suffer systematic performance degradation with Human-Designed CoT. For instance, the QwQ-32B
model experiences an absolute decrease of 33.8% in LLM Score and a 10.20% drop in IRAC Recall. Case analyses by
legal experts have uncovered a manifestation of cognitive interference from structural guidance. Specifically, while
Human-Designed CoT formally enhances the structured coherence of reasoning traces, it forces reasoning models with
intrinsic inference mechanisms to conform to external logical frameworks. This deviation from their native reasoning
pathways ultimately leads to inappropriate application of legal provisions and fabricated analytical content. These
findings challenge the prevailing assumption of universal CoT benefits and underscore the open question of when CoT
systematically reduces performance Sprague et al. [2025], Liu et al. [2025].
8

--- Page 9 ---

A PREPRINT - NOVEMBER 21, 2025
46.76 
50.79 
65.66 
41.86 
45.86 
47.70 
65.74 
65.81 
50.93 
57.11 
69.19 
46.28 
46.23 
52.34 
66.32 
67.91 
29.63 
52.38 
79.99 
40.21 
27.65 
58.14 
93.70 
94.82 
32.00 
59.50 
80.25 
42.65 
33.25 
62.33 
92.39 
94.04 
53.93 
57.00 
62.30 
43.48 
52.56 
48.88 
55.54 
58.61 
53.25 
61.47 
62.01 
44.74 
56.13 
56.50 
57.21 
60.27 
60.37 
70.88 
68.11 
43.63 
65.15 
40.86 
59.90 
62.71 
66.75 
73.73 
68.35 
45.50 
66.10 
57.09 
61.10 
65.98 
Standard Input
Human-Designed CoT
Llama3-8B
-Chinese
GLM4-9B
DeepSeek
-V3
Cleverlaw
Lawyer
-LLM
Distill-
Qwen-7b
QwQ-32b
DeepSeek
-R1
IRAC Recall@Zero-Shot
IRAC Recall@One-Shot
LLM Score@Zero-Shot
LLM Score@One-Shot
Figure 3: Zero-Shot vs. One-Shot performance on the legal reasoning task.
Model
Standard Input
Human-Designed CoT
Delta
IRAC Recall
LLM Score
IRAC Recall
LLM Score
IRAC Recall
LLM Score
Llama3-8B-Chinese
46.76
29.63
53.93
60.37
7.17
30.74
GLM4-9B
50.79
52.38
57.00
70.88
6.21
18.50
Qwen2.5-7B
56.78
65.73
57.70
65.44
0.92
-0.29
Qwen2.5-72B
61.25
68.50
58.09
57.70
-3.16
-10.80
Llama3.3-70B-Instruct
53.47
58.06
58.87
79.73
5.40
21.67
DeepSeek-V3
65.66
79.99
62.30
68.11
-3.36
-11.88
GPT-4
63.99
61.09
66.46
70.99
2.47
9.90
GPT-4o
66.06
68.47
71.78
88.98
5.72
20.51
AIE-51-8-law
39.41
14.90
39.65
21.74
0.24
6.84
Cleverlaw
41.86
40.21
43.48
43.63
1.62
3.42
Law-Justice
39.83
32.11
41.06
42.69
1.23
10.58
Lawyer-LLM
45.86
27.65
52.56
65.15
6.70
37.50
Distill-Qwen-1.5b
43.38
35.82
44.24
44.28
0.86
8.46
Distill-Qwen-7b
47.70
58.14
48.88
40.86
1.18
-17.28
QwQ-32b
65.74
93.70
55.54
59.90
-10.20
-33.80
Distill-Llama-70B
51.72
73.54
50.05
53.31
-1.67
-20.23
DeepSeek-R1
65.81
94.82
58.61
62.71
-7.20
-32.11
o1-mini
72.49
69.69
70.08
55.51
-2.41
-14.18
o3-mini
63.55
82.87
67.37
84.52
3.82
1.65
Table 3: Comparing Standard Input and Human-Designed CoT on the legal reasoning task.
- To resolve the inherent tension between prompt rigidity and model capability, the Self-Initiated CoT prompt
strategy emerges as a promising paradigm. Inspired by Wang et al. Wang et al. [2023] and Jin et al. Jin and Lu [2025],
we implement Self-Initiated CoT that guide models to autonomously generate reasoning steps before legal analysis. As
Figure 4 demonstrates, these prompts outperform Human-Designed CoT in enhancing reasoning quality and logical
coherence. Legal experts validated this approach by categorizing output traces, revealing through regex matching and
information extraction that model-generated paths consistently cover seven core legal elements (see Figure 5). Results
indicate that while autonomously constructed paths exhibit diversity, they maintain comprehensiveness. We attribute
this to: (1) The “Hydra Effect” McGrath et al. [2023] - where blocked reasoning routes activate alternative pathways,
9

--- Page 10 ---

A PREPRINT - NOVEMBER 21, 2025
62.30 
55.54 
58.61 
68.11 
59.90 
62.71 
65.71
65.34
65.85
80.19
92.56
94.65
0
20
40
60
80
100
DeepSeek-V3
QwQ-32b
DeepSeek-R1
H-CoT: IRAC Recall
H-CoT: LLM Score
S-CoT: IRAC Recall
S-CoT: LLM Score
Figure 4: H-CoT vs. S-CoT on the legal reasoning task.
96.98%
98.92%
66.67%
76.82%
45.64%
71.20%
99.28%
87.11%
91.65%
71.71%
78.11%
30.74%
85.39%
99.42%
90.50%
99.35%
74.01%
71.85%
41.68%
79.77%
98.56%
DeepSeek-V3
QwQ-32b
DeepSeek-R1
Insider Information
Insider 
Awareness
Trading
Activities
Causal Chains
Intention & Defenses
Illegal Gains
Legal Application 
& Outcome
Figure 5: Typology and coverage of Self-Initiated CoT reasoning traces in three mainstream LLMs.
mirroring real-world legal problem-solving; (2) Transformers’ parallel information processing across distributed
components, contrasting with sequential CoT constraints Dutta et al. [2024]. This phenomenon underscores that
model-task aligned prompting is critical for achieving high-quality reasoning.
6
Conclusion and Future Work
In this work, we introduce MSLR, a specialized benchmark for multi-step legal reasoning tasks designed to evaluate
both reasoning process quality and logical coherence. Comprising nearly 1,400 legal decisions requiring an average
of over 40 detailed reasoning steps each, MSLR addresses critical gaps in assessing fine-grained legal reasoning. To
enhance annotation efficiency and mitigate semantic understanding biases in LLM-generated annotations, we further
design a scalable Human-LLM collaborative annotation pipeline. Systematic evaluations of various LLMs in MSLR
reveal substantial limitations in the legal reasoning capabilities of current LLMs. Crucially, our analysis demonstrates
that Self-Initiated CoT outperforms Human-Designed CoT prompts. Establishing model-task aligned prompting strategy
emerges as a promising paradigm to enable LLMs to achieve high-quality reasoning and stable outputs.
7
Acknowledgments
This work was supported by the National Science Fund for Excellent Young Scholars (Overseas) under grant No.
KZ37117501, the National Natural Science Foundation of China (No. 62306024), the Key Program of the National
Social Science Fund of China (No. 23AFX002), the Fundamental Research Funds for the Central Universities, and the
Center for Empirical Legal Studies of Shanghai Jiao Tong University.
10

--- Page 11 ---

A PREPRINT - NOVEMBER 21, 2025
References
Farid Ariai and Gianluca Demartini. Natural Language Processing for the Legal Domain: A Survey of Tasks, Datasets,
Models, and Challenges, 2025.
Elliott Ash, Aniket Kesari, Suresh Naidu, Lena Song, and Dominik Stammbach. Translating Legalese: Enhancing
Public Understanding of Court Opinions with Legal Summarizers. In Proceedings of the 2024 Symposium on
Computer Science and Law, CSLAW ’24, pages 136–157, New York, USA, 2024. Association for Computing
Machinery. doi: 10.1145/3614407.3643700.
Katie Atkinson, Trevor Bench-Capon, and Danushka Bollegala. Explanation in AI and law: Past, present and future.
Artificial Intelligence, 289:103387, 2020. ISSN 00043702. doi: 10.1016/j.artint.2020.103387.
Marius Büttner and Ivan Habernal. Answering legal questions from laymen in German civil law system. In Proceedings
of the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long
Papers), pages 2015–2027, St. Julian’s, Malta, 2024. Association for Computational Linguistics. doi: 10.18653/v1/
2024.eacl-long.122.
Zheng Cai et al. Internlm2 technical report, 2024.
Ilias Chalkidis et al. LexGLUE: A Benchmark Dataset for Legal Language Understanding in English. In Proceedings
of the 60th Annual Meeting of the Association for Computational Linguistics, pages 4310–4330, Dublin, Ireland,
2022. Association for Computational Linguistics. doi: 10.18653/v1/2022.acl-long.297.
Jiaxi Cui, Zongjian Li, Yang Yan, Bohua Chen, and Li Yuan. Chatlaw, 2023.
DeepSeek-AI. Deepseek-v3 technical report, 2024. URL https://arxiv.org/abs/2412.19437.
DeepSeek-AI. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning, 2025. URL
https://arxiv.org/abs/2501.12948.
Wentao Deng, Jiahuan Pei, Keyi Kong, Zhe Chen, Furu Wei, Yujun Li, Zhaochun Ren, Zhumin Chen, and Pengjie Ren.
Syllogistic Reasoning for Legal Judgment Analysis. In Proceedings of the 2023 Conference on Empirical Methods in
Natural Language Processing, pages 13997–14009, Singapore, 2023. Association for Computational Linguistics.
doi: 10.18653/v1/2023.emnlp-main.864.
Subhabrata Dutta, Joykirat Singh, Soumen Chakrabarti, and Tanmoy Chakraborty. How to think step-by-step: A
mechanistic understanding of chain-of-thought reasoning, 2024.
Yu Fan et al. LEXam: Benchmarking Legal Reasoning on 340 Law Exams, 2025.
Zhiwei Fei, Xiaoyu Shen, Dawei Zhu, Fengzhe Zhou, Zhuo Han, Alan Huang, Songyang Zhang, Kai Chen, Zhixin Yin,
Zongwen Shen, Jidong Ge, and Vincent Ng. LawBench: Benchmarking Legal Knowledge of Large Language Models.
In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 7933–7962,
Miami, Florida, USA, 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.emnlp-main.452.
Team GLM. Chatglm: A family of large language models from glm-130b to glm-4 all tools, 2024.
Jiawei Gu, Xuhui Jiang, Zhichao Shi, Hexiang Tan, Xuehao Zhai, Chengjin Xu, Wei Li, Yinghan Shen, Shengjie
Ma, Honghao Liu, Saizhuo Wang, Kun Zhang, Yuanzhuo Wang, Wen Gao, Lionel Ni, and Jian Guo. A Survey on
LLM-as-a-Judge, 2025.
Guha et al. LegalBench: A collaboratively built benchmark for measuring legal reasoning in large language models.
Advances in Neural Information Processing Systems, 36:44123–44279, 2023.
Jie Huang and Kevin Chen-Chuan Chang. Towards reasoning in large language models: A survey. In Findings of the
Association for Computational Linguistics: ACL 2023, page 1049–1065, Toronto, Canada, 2023. Association for
Computational Linguistics.
Quzhe Huang, Mingxu Tao, Chen Zhang, Zhenwei An, Cong Jiang, Zhibin Chen, Zirui Wu, and Yansong Feng. Lawyer
llama technical report, 2023.
Ziqi Jin and Wei Lu. Self-Harmonized Chain of Thought. In Proceedings of the 2025 Conference of the Nations of
the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume
1: Long Papers), pages 1153–1174, Albuquerque, New Mexico, 2025. Association for Computational Linguistics.
ISBN 979-8-89176-189-6. doi: 10.18653/v1/2025.naacl-long.53.
Hannah Kim, Kushan Mitra, Rafael Li Chen, Sajjadur Rahman, and Dan Zhang. MEGAnno+: A Human-LLM
Collaborative Annotation System. In Proceedings of the 18th Conference of the European Chapter of the Association
for Computational Linguistics: System Demonstrations, pages 168–176, St. Julians, Malta, 2024. Association for
Computational Linguistics. doi: 10.18653/v1/2024.eacl-demo.18.
11

--- Page 12 ---

A PREPRINT - NOVEMBER 21, 2025
Jan Koco´n et al. ChatGPT: Jack of all trades, master of none. Information Fusion, 99:101861, 2023. ISSN 1566-2535.
doi: 10.1016/j.inffus.2023.101861.
Haitao Li, You Chen, Qingyao Ai, Yueyue Wu, Ruizhe Zhang, and Yiqun Liu. LexEval: A Comprehensive Chinese
Legal Benchmark for Evaluating Large Language Models. Advances in Neural Information Processing Systems, 37:
25061–25094, 2024.
Minzhi Li et al. CoAnnotating: Uncertainty-Guided Work Allocation between Human and Large Language Models for
Data Annotation. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing,
pages 1487–1505, Singapore, 2023. Association for Computational Linguistics. doi: 10.18653/v1/2023.emnlp-
main.92.
Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman,
Ilya Sutskever, and Karl Cobbe. Let’s Verify Step by Step, 2023.
Ryan Liu, Jiayi Geng, Addison J. Wu, Ilia Sucholutsky, Tania Lombrozo, and Thomas L. Griffiths. Mind Your Step (by
Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse, 2025.
Shuaiqi Liu, Jiannong Cao, Yicong Li, Ruosong Yang, and Zhiyuan Wen. Low-resource court judgment summarization
for common law systems. Information Processing & Management, 61(5):103796, 2024. ISSN 0306-4573. doi:
10.1016/j.ipm.2024.103796.
Antoine Louis, Gijs van Dijck, and Gerasimos Spanakis. Interpretable long-form legal question answering with
retrieval-augmented large language models. In Proceedings of the Thirty-Eighth AAAI Conference on Artificial
Intelligence, volume 38, pages 22266–22275. AAAI Press, 2024. doi: 10.1609/aaai.v38i20.30232.
Thomas McGrath, Matthew Rahtz, Janos Kramar, Vladimir Mikulik, and Shane Legg. The Hydra Effect: Emergent
Self-repair in Language Model Computations, 2023.
Meta. The llama 3 herd of models, 2024. URL https://arxiv.org/abs/2407.21783.
Nelson P. Miller and Bradley J. Charles. Meeting the Carnegie Report’s Challenge to Make Legal Analysis Explicit-
Subsidiary Skills to the IRAC Framework. Journal of Legal Education, 59(2):192–220, 2009.
Gianluca Moro, Nicola Piscaglia, Luca Ragazzi, and Paolo Italiani. Multi-language transfer learning for low-resource
legal case summarization. Artificial Intelligence and Law, 32(4):1111–1139, 2024. ISSN 1572-8382. doi: 10.1007/
s10506-023-09373-8.
Arbi Haza Nasution and Aytu˘g Onan. ChatGPT Label: Comparing the Quality of Human-Generated and LLM-
Generated Annotations in Low-Resource Language NLP Tasks. IEEE Access, 12:71876–71900, 2024. ISSN
2169-3536. doi: 10.1109/ACCESS.2024.3402809.
Joel Niklaus, Veton Matoshi, Pooja Rani, Andrea Galassi, Matthias Stürmer, and Ilias Chalkidis. LEXTREME: A
Multi-Lingual and Multi-Task Benchmark for the Legal Domain. In Findings of the Association for Computational
Linguistics: EMNLP 2023, pages 3016–3054, Singapore, 2023. Association for Computational Linguistics. doi:
10.18653/v1/2023.findings-emnlp.200.
Maxwell Nye, Anders Johan Andreassen, Guy Gur-Ari, Henryk Michalewski, Jacob Austin, David Bieber, David
Dohan, Aitor Lewkowycz, Maarten Bosma, David Luan, Charles Sutton, and Augustus Odena. Show Your Work:
Scratchpads for Intermediate Computation with Language Models, 2021.
OpenAI. Gpt-4o system card, 2024a. URL https://arxiv.org/abs/2410.21276.
OpenAI. Gpt-4 technical report, 2024b. URL https://arxiv.org/abs/2303.08774.
OpenAI. Openai o1 system card, 2024c. URL https://arxiv.org/abs/2412.16720.
Pranab Sahoo, Ayush Kumar Singh, Sriparna Saha, Vinija Jain, Samrat Mondal, and Aman Chadha. A Systematic
Survey of Prompt Engineering in Large Language Models: Techniques and Applications, 2025.
Jiaxin Shen, Jinan Xu, Huiqi Hu, Luyi Lin, Fei Zheng, Guoyang Ma, Fandong Meng, Jie Zhou, and Wenjuan Han. A
Law Reasoning Benchmark for LLM with Tree-Organized Structures including Factum Probandum, Evidence and
Experiences, 2025.
Francesco Sovrano, Monica Palmirani, Salvatore Sapienza, and Vittoria Pistone. DiscoLQA: Zero-shot discourse-based
legal question answering on European Legislation. Artificial Intelligence and Law, 33(2):323–359, 2025. ISSN
1572-8382. doi: 10.1007/s10506-023-09387-2.
Zayne Sprague, Fangcong Yin, Juan Rodriguez, Dongwei Jiang, Manya Wadhwa, Prasann Singhal, Xinyu Zhao, Xi Ye,
Kyle Mahowald, and Greg Durrett. To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic
reasoning. International Conference on Representation Learning, 2025:94118–94162, 2025.
12

--- Page 13 ---

A PREPRINT - NOVEMBER 21, 2025
Zhen Tan et al. Large Language Models for Data Annotation and Synthesis: A Survey. In Yaser Al-Onaizan,
Mohit Bansal, and Yun-Nung Chen, editors, Proceedings of the 2024 Conference on Empirical Methods in Natural
Language Processing, pages 930–957, Miami, Florida, USA, 2024. Association for Computational Linguistics. doi:
10.18653/v1/2024.emnlp-main.54.
Qwen Team. Qwen2.5 technical report. arXiv preprint arXiv:2412.15115, 2024.
Qwen Team. Qwq-32b: Embracing the power of reinforcement learning, March 2025. URL https://qwenlm.
github.io/blog/qwq-32b/.
Suxin Tong, Jingling Yuan, Peiliang Zhang, and Lin Li. Legal Judgment Prediction via graph boosting with constraints.
Information Processing & Management, 61(3):103663, 2024. ISSN 0306-4573. doi: 10.1016/j.ipm.2024.103663.
Xinru Wang, Hannah Kim, Sajjadur Rahman, Kushan Mitra, and Zhengjie Miao. Human-LLM Collaborative Annotation
Through Effective Verification of LLM Labels. In Proceedings of the 2024 CHI Conference on Human Factors in
Computing Systems, CHI ’24, pages 1–21, New York, NY, USA, 2024a. Association for Computing Machinery. doi:
10.1145/3613904.3641960.
Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Denny
Zhou. Self-Consistency Improves Chain of Thought Reasoning in Language Models, 2023.
Xuran Wang, Xinguang Zhang, Vanessa Hoo, Zhouhang Shao, and Xuguang Zhang. LegalReasoner: A Multi-Stage
Framework for Legal Judgment Prediction via Large Language Models and Knowledge Integration. IEEE Access,
12:166843–166854, 2024b. ISSN 2169-3536. doi: 10.1109/ACCESS.2024.3496666.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc V. Le, and Denny
Zhou. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. Advances in Neural Information
Processing Systems, 35:24824–24837, 2022.
G. Edward White. The Evolution of Reasoned Elaboration: Jurisprudential Criticism and Social Change. Virginia Law
Review, 59(2):279–302, 1973. ISSN 0042-6601. doi: 10.2307/1071994.
Zhuosheng Zhang, Aston Zhang, Mu Li, and Alex Smola. Automatic Chain of Thought Prompting in Large Language
Models, 2022.
Xufeng Zhao, Mengdi Li, Wenhao Lu, Cornelius Weber, Jae Hee Lee, Kun Chu, and Stefan Wermter. Enhancing
Zero-Shot Chain-of-Thought Reasoning in Large Language Models through Logic, 2024.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan
Li, Dacheng Li, Eric Xing, et al. Judging llm-as-a-judge with mt-bench and chatbot arena. Advances in Neural
Information Processing Systems, 36:46595–46623, 2023.
13

--- Page 14 ---

A PREPRINT - NOVEMBER 21, 2025
A
Data and Code
The data and code for this work are available in the folder “MSLR-Multi-Step-Reasoning-Trace”.
File from Lawyer LLaMA
ROUGE-1 F1
ROUGE-2 F1
ROUGE-L F1
alpaca_gpt4_data_zh.json
0.0303
0.0033
0.0247
fakao_gpt4.json
0.0171
0.0008
0.0155
judical_examination_v2.json
0.0083
0.0007
0.0071
legal_counsel_multi_turn_with_article_v2.json
0.0032
0.0002
0.0029
legal_counsel_v2.json
0.0168
0.0026
0.0144
zixun_gpt4.json
0.0017
0.0001
0.0014
Table 4: Document similarity between MSLR and Lawyer LLaMA.
B
The Novelty of MSLR
To validate the novelty of the MSLR dataset, we compute ROUGE-1/2/L F1 scores between documents in MSLR and the
comprehensive Chinese legal corpus used during the training of Lawyer LLaMA. As shown in Table 4, the results show
near-random similarity levels (all F1 < 0.03), significantly below conventional similarity thresholds. This indicates that
MSLR was not included in the pretraining corpus, further establishing its reliability as a contamination-free evaluation
benchmark.
To ensure scientific integrity and impartiality, MSLR incorporates systematic anti-leakage protocols across four
dimensions: (1) Transparent data sourcing. All legal documents are collected from authoritative platforms (e.g.,
the China Securities Regulatory Commission (CSRC), the Supreme People’s Procuratorate (SPP), and the Supreme
People’s Court (SPC)) with preserved timestamps and source URLs, ensuring traceability and legal compliance. (2)
Inference-centric design. The tasks in MSLR are inherently reasoning-intensive, making it impractical to achieve
high scores through superficial text memorization or reproduction. (3) Rigorous evaluation. Large language models
(LLMs) are strictly evaluated under zero-shot or one-shot settings without any training or fine-tuning on MSLR dataset,
guaranteeing objective assessment. (4) Read-only API usage. Read-only interfaces prevent feedback loop contamination.
During model invocation, only read-only APIs are used, and evaluation outputs are never fed back into model training
or corpus updates, eliminating feedback-based contamination entirely. Taken together, the MSLR architecture mitigates
leakage risks while establishing its scientific validity, impartiality, and challenge level for legal AI evaluation.
C
LLM Automatic Annotation Detail
C.1
Structured Data Annotation Template
Based on these IRAC-Traces, we develop a structured data annotation template to systematically record the reasoning
process of each legal decision. As shown in the Listing D.1, the template includes metadata of legal documents, key
structured elements essential for legal reasoning and decision-making, as well as the corresponding legal provisions and
factual case descriptions. Each case instance is composed of multiple hierarchical fields, with a total of over 40 defined
attributes, ensuring both completeness of representation and traceability of the reasoning process.
C.2
Standardized Prompts for Task 1
To evaluate the annotation capabilities of LLMs in the legal domain (i.e., Task 1), we transform annotation tasks into
structured information extraction tasks compatible with LLMs. These tasks encompass core NLP sub-tasks including
named entity recognition, text classification, and summarization. We design a unified framework for structured
information extraction, where prompts are constructed under a zero-shot setting. As shown in the Listing C.1, this
framework employs a standardized input template to guide LLMs in extracting key legal information from raw case
texts. The output is required to follow the predefined JSON schema (see Listing D.1), facilitating downstream evaluation
and processing. It is important to note that both the inputs and outputs are in Chinese; therefore, the actual prompt is
written in Chinese, and the English version presented here is a direct translation for illustration purposes.
14

--- Page 15 ---

A PREPRINT - NOVEMBER 21, 2025
Listing C.1: Standardized Prompts for Task 1
Role Setting:
You are a large language model specialized in legal document analysis and information extraction, particularly
skilled at identifying legal facts related to insider trading. Please read the following case description and extract
the specified fields, outputting a standardized structured JSON.
Task Introduction:
(1) Please strictly extract only the fields listed under the “Field Extraction Scope” below;
(2) If a field is not mentioned in the Case Description, leave it as an empty string “”;
(3) The output must be a valid JSON object, and the field names and nested structure must exactly follow the
“Output Format Template”;
(4) Do not generate any explanations or comments—output only the JSON data.
Case Description:
...
Field Extraction Scope:
...
Output Format Template:
... (see Listing D.1 “Structured Data Annotation Template”)
C.3
Prompt Optimization in the Precision-Tuning Stage
In the precision-tuning stage, we evaluate different LLMs’ performance against gold-standard examples to identify
the most cost-effective model. Experimental results demonstrate DeepSeek-V3’s optimal cost-effectiveness ratio,
establishing it as our primary annotation assistant. Building on the optimal model, we further refine prompts for a subset
of fields that are semantically dependent, ambiguous, or irregularly formatted. By optimizing prompts and conducting
independent extraction trials, we significantly enhance the accuracy of information extraction for these challenging
fields. The following presents key optimization strategies for selected fields, along with illustrative prompt examples.
C.3.1
Content of Insider Information
This field is often composed of multiple factual descriptions and lacks clearly defined boundaries. As shown in Listing
C.2, we apply a summarization-style prompt that directs the model to distill the “core insider information” into 1–2
legally framed sentences.
Listing C.2: Prompt for Content of Insider Information Field
Please summarize the core facts of the insider information in 1–2 sentences using formal legal language. For
example: “The major asset restructuring information of the company was leaked before public disclosure ...”
C.3.2
Type of Party Involved
This field requires complex classification based on Article 51 of the Securities Law and Article 6 of the CSRC’s
Guidelines for Identifying Insider Trading. The classification is multi-label by nature. As shown in Listing C.3, we
design the prompt to reference relevant legal clauses and support multiple-choice outputs from a provided candidate list.
Listing C.3: Prompt for Type of Party Involved Field
According to Article 51 of the Securities Law and Article 6 of the CSRC’s Guidelines for Identifying Insider
Trading, determine the category of insider the involved party belongs to. Multiple selections are allowed from the
following candidate list:
“51(1) Issuer and its directors, supervisors, senior executives”;
...
“Guideline 6(2-1) Issuer or listed company”;
“Guideline 6(2-2) Other companies controlled by controlling shareholders of the issuer”;
...
15

--- Page 16 ---

A PREPRINT - NOVEMBER 21, 2025
C.3.3
Legal Provisions Applied
This field often suffers from variability in expression, with frequent omissions of article numbers or formal statute
names. To mitigate this, as shown in Listing C.4, we explicitly instruct the model to extract valid legal references,
including both the statute title and the article number. The scope is limited to formal legal documents such as the
Securities Law and Criminal Law.
Listing C.4: Prompt for Legal Provisions Applied Field
Please extract the legally effective article names and numbers from the following legal description. Only consider
provisions from formal legal documents such as the Securities Law and Criminal Law. For example: “Article 73 of
the Securities Law”; ...
C.3.4
Summary of Objections or Defenses
This field is prone to confusion with the adjudicator’s opinions. To avoid this, as shown in Listing C.5, the prompt
includes a perspective instruction emphasizing that only content asserted by the party should be extracted.
Listing C.5: Prompt for Summary of Objections or Defenses Field
Only extract the objections or defenses claimed by the involved party, excluding comments from the court or
regulatory authorities. Begin the summary with “The party argued that ...”.
D
LLM-as-a-Judge Evaluation Template
We adopt an evaluation setup based on the LLM-as-a-Judge paradigm to measure the quality and logical coherence of
LLM-generated reasoning traces. We select the flagship model DeepSeek-V3 as the evaluation model and design a
standardized input format. The complete evaluation prompt is shown in the Listing D.2.
Listing D.1: Structured Data Annotation Template
Case Metadata:
" Case
Index " :
" . . . " ,
" Document Type " :
" . . . " ,
" F i n a l
Penalty
Outcome " :
" . . . " ,
" P e n a l t y
Year " :
" . . . " ,
" P e n a l t y
Date " :
" . . . " ,
" P e n a l i z i n g
A u t h o r i t y " :
" . . . " ,
" Case
Reference Number " :
" . . . " ,
" T i t l e
of
the
Decision
Document " :
" . . . "
Insider Information Determination:
"Name of
the
Traded
Stock " :
" . . . " ,
" Content
of
I n s i d e r
I n f o r m a t i o n " :
" . . . " ,
" Legal
Basis
f o r
I n s i d e r
I n f o r m a t i o n
Determination " :
" . . . " ,
" Type of
I n s i d e r
I n f o r m a t i o n " :
" . . . " ,
" Date
of
I n s i d e r
I n f o r m a t i o n
Formation " :
" . . . " ,
" D e s c r i p t i o n
of
Events on Formation
Date " :
" . . . " ,
" Date
of
Public
D i s c l o s u r e " :
" . . . " ,
" D e s c r i p t i o n
of
Events on
D i s c l o s u r e
Date " :
" . . . "
Basic Information of the Party:
"Name " :
" . . . " ,
" Gender " :
" . . . " ,
" Year
of
B i r t h " :
" . . . " ,
" Education
Level " :
" . . . " ,
" P o s i t i o n
a t
the
Time of
the
I n c i d e n t " :
" . . . "
16

--- Page 17 ---

A PREPRINT - NOVEMBER 21, 2025
Insider Trading Determination for the Party:
" Role
of
the
Party " :
" . . . " ,
" Type of
Party
Involved " :
" . . . " ,
" Date
the
Party
Became Aware of
I n s i d e r
I n f o r m a t i o n " :
" . . . " ,
" Manner
in Which
I n s i d e r
I n f o r m a t i o n Was Obtained " :
" . . . " ,
" C l a s s i f i c a t i o n
of
Access Method " :
" . . . " ,
" Type of
I n s i d e r
Trading
Behavior " :
" . . . " ,
"Buy / S e l l
Action " :
" . . . " ,
" Date ( s )
of
Trade
Execution " :
" . . . " ,
" Trade Amount ( in RMB) " :
" . . . " ,
" E a r l i e s t
Trade
Date " :
" . . . " ,
" L a t e s t
Trade
Date " :
" . . . " ,
" Benchmark Value on Key Date " :
" . . . " ,
" I l l i c i t
Gains
( in RMB) " :
" . . . "
Penalty Details:
" Legal
P r o v i s i o n s
Applied " :
" . . . " ,
"Amount of
I l l i c i t
Gains
C o n f i s c a t e d
( in RMB) " :
" . . . " ,
" M u l t i p l i e r
of
Fine " :
" . . . " ,
"Amount of
Fine
( in RMB) " :
" . . . "
Arguments Raised by the Party:
"Summary of
O b j e c t i o n s
or
Defenses " :
" . . . "
Legal Decision Text:
" O r i g i n a l
Text
of
the
Legal Document " :
" . . . " ,
" S t r u c t u r e d
F a c t u a l
D e s c r i p t i o n " :
" . . . " ,
"Summary of
Legal
Reasoning " :
" . . . " ,
" Judgment
or
Penalty
Decision " :
" . . . "
Listing D.2: LLM-as-a-Judge Evaluation Prompt
Role Description
You are a legal expert reviewer tasked with evaluating and comparing the legal analysis results generated by the
same AI model under three different modes. The model is expected to perform a complete analysis based on the
following legal reasoning chain:
Insider Information Formation →Information Awareness →Trading Behavior →Illegal Gains →Legal
Application and Judgment Type →Penalty Outcome
Scoring Criteria
Please rate the reasoning quality of the outputs according to the following criteria:
• A (Excellent): The reasoning fully covers all six stages above, with clear and rigorous logic, correct
application of law, and a reasonable conclusion.
• B (Fair): The reasoning is generally reasonable but contains omissions or ambiguities in certain stages,
affecting the rigor of legal judgment.
• C (Poor): The reasoning is severely lacking, logically inconsistent, or legally incorrect, making it
insufficient to support a valid judgment.
Output Format
Please return the three scores strictly in the following format (A, B, or C):
Standard Score:
<score>
Human-Designed CoT Score:
<score>
Self-Initiated CoT Score:
<score>
17

--- Page 18 ---

A PREPRINT - NOVEMBER 21, 2025
Input Format
- Standard Output:
{predicted_answers[0]}
- Human-Designed CoT Output:
{predicted_answers[1]}
- Self-Initiated CoT Output:
{predicted_answers[2]}
- Reference Answer:
{Summary of Legal Reasoning} + {Judgement or Penally Decision}
E
Field Categorization Details
To enhance the precision and interpretability of evaluations for both automatic annotation and legal reasoning tasks, We
classify fields into two categories: Exa-Fields requiring exact matching (e.g.,dates, amounts) and Sem-Fields requiring
semantic matching (e.g., event descriptions, information summaries). This classification facilitates a more fine-grained
and legally grounded evaluation strategy, better aligning with the inherent structural characteristics of legal data. The
detailed categorization is presented in Table 5.
Field Type
Section
Field Name
Exa-Fields
Name of the Traded Stock
Insider Information Determination
Date of Insider Information Formation
Date of Public Disclosure
Name
Basic Information of the Party
Gender
Year of Birth
Position at the Time of the Incident
Date of Awareness
Buy/Sell Action
Date(s) of Trade Execution
Insider Trading Determination for the Party
Trade Amount (RMB)
Earliest Trade Date
Latest Trade Date
Benchmark Value on Key Date
Illicit Gains (RMB)
Penalty Outcome Details
Amount of Illicit Gains Confiscated (RMB)
Multiplier of Fine
Amount of Fine (RMB)
Sem-Fields
Content of Insider Information
Legal Basis for Insider Information Determination
Insider Information Determination
Type of Insider Information
Description of Event on Formation Date
Description of Event on Disclosure Date
Role of the Party
Type of Party Involved
Insider Trading Determination for the Party
Manner in Which Insider Information Was Obtained
Classification of Access Method
Type of Insider Trading Behavior
Penalty Outcome Details
Legal Provisions Applied
Table 5: Field categorization for evaluation.
18

--- Page 19 ---

A PREPRINT - NOVEMBER 21, 2025
F
Supplementary Experiments for Task 1
We conducted supplementary one-shot experiments on the LLM automatic annotation task (Task 1). As shown in Table
6, under the one-shot setting, most models demonstrated moderate improvements in Field Completeness Rate (FCR)
compared to zero-shot, indicating that demonstrative example partially enhance field extraction comprehensiveness.
However, Overall Accuracy (Overall Acc) shows negligible improvement, with some models exhibiting performance
degradation. This reveals that while one-shot prompting expands output coverage, it fails to significantly enhance
extraction precision. These findings demonstrate that minimal examples cannot overcome LLMs’ limitations in
parsing complex legal semantics. Consequently, our established PPP annotation pipeline—leveraging Human-LLM
collaboration to accelerate processing while maintaining human-curated quality—proves both necessary and promising.
Category
Model
Zero-shot
One-shot
FCR
Overall Acc
FCR
Overall Acc
General LLMs
Llama3-8B
76.37
57.43
76.40
58.50
GLM4-9B
68.85
67.01
61.37
57.17
DeepSeek-V3
69.65
77.43
73.07
75.11
Legal LLMs
Cleverlaw
78.43
61.79
64.76
55.73
Lawyer-LLM
70.13
57.49
83.77
58.91
Reasoning LLMs
Distill-Qwen-7b
75.67
61.71
80.11
57.81
QwQ-32b
71.51
65.74
75.54
63.90
DeepSeek-R1
70.24
70.72
77.61
71.71
Table 6: Zero-shot vs. One-shot performance on the automatic annotation task.
G
Case Study for Task 2
In this case study, we present and analyze the reasoning processes generated by the DeepSeek-R1 model when
processing the same case description under two prompt modes: Standard Prompt and Human-Designed CoT Prompt.
Their generated reasoning processes are respectively shown in Figure 6 and Figure 7. A detailed comparison of their
reasoning quality reveals that under LLM-as-a-Judge, the output from the Standard prompt mode received an A-grade
rating, whereas the Human-Designed CoT prompt output was only awarded a C-grade. Legal experts’ assessments (as
shown in Table 5) align with the model ratings, confirming that the Standard prompt reasoning process better adheres
to case facts and legal application, demonstrating significant advantages over the Human-Designed CoT prompt in
terms of logical structure and legal coherence. This case study highlights a critical limitation of Human-Designed CoT:
despite its intent to guide systematic reasoning, its redundant structural framework may disrupt the model’s intrinsic
reasoning mechanisms, leading to logical leaps, missing elements, or incorrect application of legal provisions—all of
which undermine the rationality and credibility of the final judgment.
Analysis Di-
mension
Standard Output
Human-Designed Output
Evaluation Conclusion
Case
Fact
Recognition
Accurate and complete, covering the
full process of insider information for-
mation and trading
Omits the early stage of insider infor-
mation formation, which does not affect
substantive determination
Roughly equivalent
Insider Infor-
mation Iden-
tification
Correctly cites Article 75 of the 2005
Securities Law; applies the historical
law accurately
Incorrectly cites the 2019 version and
Article 80 (misapplies information dis-
closure clauses)
Std clearly superior; CoT
lacks legal clarity
Insider
Awareness
Analysis
Reasonably judged based on Article 74,
considering official position and timing
of awareness
Introduces a “time of awareness” path,
but the logical chain is unclear and par-
tially fabricated
Std aligns better with legal
logic; CoT introduces in-
vented reasoning points
Trading Be-
havior Anal-
ysis
Covers timing, amount, method, and ac-
count details; relatively well-structured
Introduces “habitual trading compari-
son” as a novel point, but lacks conclu-
sive judgment
Both have weaknesses
Illegal Gains
Calculation
Not provided
Provided, but based on incorrect legal
citation
Both have deficiencies
Legal Norm
Application
Comprehensive citation of historical
laws and judicial interpretations; re-
flects administrative-criminal transition
Incorrectly cites new legal provisions;
omits criminal transfer criteria
Std more accurate; CoT
misuses legal references
Table 7: Comparison of Standard Output vs. Human-Designed CoT Output on the legal reasoning task.
19

--- Page 20 ---

A PREPRINT - NOVEMBER 21, 2025
Reasoning Results under Standard Input
Case Summary
Qu XX, Deputy Director of the Office of Shenzhen Txxx Group Co., Ltd., accessed critical information about a
cooperative plan involving Factory Buildings No. 2 and No. 3 of Tyyy Company between March and December 2007.
He participated in decision-making processes related to the plan. On December 11, 2007, he purchased 83,700 shares
of “Tyyy A” stock in a single transaction, ranking first in trading volume for that stock on that day. He sold the shares
in March 2008.
Legal Analysis
1. Identification of Insider Information
According to Article 75 of the Securities Law, insider information refers to unpublished information that concerns a
company’s operations or finances and may significantly impact its stock price. In this case:
• The “Major Asset Report Form” submitted by Tyyy to Txxx regarding the cooperative plan for Factory Buildings
No. 2 and No. 3 constitutes a major asset restructuring.
• This plan eventually led to the formation of Tyyy Jimeng Company.
• The information had a significant impact on the stock price of “Tyyy A.”
• The information remained undisclosed until the formation of Tyyy Jimeng on December 18, 2007.
Thus, the cooperative plan constitutes insider information.
2. Identification of the Insider
As per Article 74 of the Securities Law, insiders include directors, supervisors, senior executives, and those who, due to
their positions, can access such information. Qu XX:
• Served as Deputy Director of Txxx Group Office since May 6, 2003.
• Attended the leadership meeting of Txxx Group on October 12, 2007.
• Reviewed and approved relevant draft documents on December 7, 2007.
His position enabled him to access insider information, qualifying him as an insider.
3. Analysis of Trading Behavior
Key features of Qu XX’s transaction include:
• Timing: Purchase occurred during the period from the formation to the disclosure of insider information
(December 11, 2007).
• Volume: Bought 83,700 shares, ranking first in daily trading volume.
• Method: Placed the order via an office telephone.
• Holding Period: Short-term (sold on March 7 and 11, 2008).
• Account: Used personal securities account (ID: 00016#####).
4. Violation Analysis
Qu XX’s behavior meets all the criteria of insider trading:
1. Qualified Subject: Identified as an insider.
2. Access to Insider Information: Obtained through his professional role.
3. Trading Within Sensitive Period: Conducted transaction before public disclosure.
4. Abnormal Trading Pattern: Large single purchase, highest daily volume.
Evidence Evaluation
• Position Certificate: Confirms Qu XX’s role at Txxx Group.
• Meeting Records: Evidence of attending leadership meetings and approving drafts.
• Securities Account Information: Shows ownership and usage of the trading account.
• Trading Records: Confirms timing and volume of the transactions.
• Information Formation Process: Demonstrates the significance and confidentiality of the insider information.
Applicable Laws
Qu XX’s conduct violates:
• Article 73 of the Securities Law: Prohibits insider trading.
• Article 180 of the Criminal Law: Criminalizes insider trading (if the circumstances are serious).
Judicial Decision
Based on the above analysis, Qu XX is determined to have committed insider trading. Proposed legal actions include:
1. Confiscation of Illegal Gains: Recover all profits derived from the trade.
2. Fines: Impose a fine between one to five times the illegal gain.
3. Market Ban: Recommend a ban from securities market activities for a period.
4. Criminal Referral: If gains or avoided losses meet the threshold, refer the case to public security authorities.
Legal Basis
• Securities Law of the People’s Republic of China: Articles 73, 74, 75, 202
• Criminal Law of the People’s Republic of China: Article 180
• Interpretation by the Supreme People’s Court and Supreme People’s Procuratorate on Insider Trading and
Disclosure Cases
• Securities Market Ban Regulations
Figure 6: Reasoning results under Standard input.
20

--- Page 21 ---

A PREPRINT - NOVEMBER 21, 2025
Reasoning Results under Human-Designed CoT Input
Case Summary: Qu XX, serving as Deputy Director of the Office of Shenzhen Txxx Group Co., Ltd., ...
Legal Analysis Framework
1. Formation of Insider Information
Pursuant to Article 52 of the Securities Law and Article 5 of the judicial interpretation on insider trading by the Supreme
People’s Court and Supreme People’s Procuratorate, the formation of insider information in this case is as follows:
• Materiality: The cooperative plan and the establishment of Tyyy Jimeng fall under “significant investment
activities” as defined in Article 80(2) of the Securities Law, potentially impacting the stock price of “Tyyy A.”
• Key Time Points:
– Initial formation: March 27, 2007, when Tyyy submitted the Major Asset Report to Txxx.
– Confirmation: December 7, 2007, when Qu XX reviewed and verified the draft approval document.
– Disclosure: December 18, 2007, upon the formal establishment and announcement of Tyyy Jimeng.
• Sensitivity: The information remained undisclosed prior to public announcement, meeting the definition of
insider information under the Securities Law.
2. Confirmation of Information Awareness
As Deputy Director of Txxx Group’s office, Qu XX had access to insider information by virtue of his position:
• Professional Access: Attended Txxx’s leadership meeting on October 12, 2007, and reviewed the approval draft
on December 7, 2007.
• Time of Awareness: Clearly possessed insider knowledge no later than December 7, 2007.
3. Trading Behavior Analysis
• Transaction Timing: Purchase on December 11, 2007, just 4 days after awareness (Dec 7) and 7 days before
disclosure (Dec 18).
• Abnormal Trading Pattern:
– Single transaction of 83,700 shares, top-ranked in trading volume for the day.
– Order placed via office telephone, suggesting occupational linkage.
– Trading behavior deviated significantly from prior account history.
• Correlation with Awareness: The transaction occurred after acquiring insider information and before public
disclosure.
4. Calculation of Illegal Gains
According to Article 10 of the judicial interpretation:
• Purchase Cost: 83,700 shares × purchase price (to be confirmed from exchange data).
• Sale Revenue: 83,700 shares × selling price (average price from March 7 and 11, 2008).
• Illegal Profit: Sale revenue – purchase cost – transaction taxes and fees.
(Note: Specific figures must be calculated based on exchange transaction data.)
5. Legal Qualification and Violation Identification
• Violation: Constitutes insider trading under Article 53 of the Securities Law.
• Aggravating Factors:
– Abuse of professional privilege to access insider information.
– Large transaction amount (precise value pending verification).
– Abnormal trading pattern.
– Top-ranked purchase volume possibly affecting market order.
• Subject Qualification: Satisfies the definition of an insider under Article 51 of the Securities Law.
6. Considerations for Penalty
• Aggravating Circumstances:
– State-owned enterprise official knowingly violated the law.
– Large transaction amount.
– Exploited job position to obtain information.
• Mitigating Circumstances:
– Whether the suspect voluntarily confessed.
– Whether cooperation was provided during investigation.
– Whether any remedial actions were taken.
Judicial Conclusion In accordance with Article 191 of the Securities Law and Article 180 of the Criminal Law (if
a criminal threshold is met), the following penalties are recommended:
• Administrative Sanctions:
– Confiscation of illegal gains (amount to be calculated).
– Fine between one to five times the illegal gain.
– Formal warning to Qu XX.
• Disciplinary Measures: Txxx Group advised to impose internal disciplinary action in accordance with corporate
policies.
• Criminal Referral: If illegal gains exceed the criminal threshold (e.g., RMB 500,000), refer to public security
authorities for criminal proceedings.
• Market Ban: Recommend that the CSRC impose a 3–5 year ban from securities markets.
Legal Basis
• Securities Law of the People’s Republic of China (2019): Articles 51, 52, 53, 191
• Judicial Interpretation on Insider Trading and Information Disclosure by the SPC and SPP
• Securities Market Ban Regulations (2021)
Figure 7: Reasoning results under Human-Designed CoT input.
21

```
