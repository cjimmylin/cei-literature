---
title: "Cross Cultural Value Alignment - PDF Extract"
source_pdf: "2025-Liu-Cross Cultural Value Alignment.pdf"
pages: 30
extracted_at: "2026-04-03T11:05:46.214432"
---

# PDF Extract: Cross Cultural Value Alignment

**Source PDF:** 2025-Liu-Cross Cultural Value Alignment.pdf
**Total Pages:** 30

---

## Content

--- Page 1 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
CROSS-CULTURAL VALUE ALIGNMENT FRAMEWORKS
FOR RESPONSIBLE AI GOVERNANCE: EVIDENCE FROM
CHINA-WEST COMPARATIVE ANALYSIS
Haijiang Liu∗, Jinguang Gu
Wuhan University of Science and Technology
Wuhan, China
{alecliu, simon}@ontoweb.wust.edu.cn
Xun Wu
The Hong Kong University of Science and Technology (Guangzhou)
Guangzhou, China
wuxun@hkust-gz.edu.cn
Daniel Hershcovich
University of Copenhagen
Copenhagen, Denmark
DH@di.ku.dk
Qiaoling Xiao
WUST-Madrid Complutense Institute
Wuhan, China
CHRISTINA.XIAO@wust.edu.cn
ABSTRACT
As Large Language Models (LLMs) increasingly influence high-stakes decision-
making across global contexts, ensuring their alignment with diverse cultural val-
ues has become a critical governance challenge. This study presents a Multi-
Layered Auditing Platform for Responsible AI that systematically evaluates cross-
cultural value alignment in China-origin and Western-origin LLMs through four
integrated methodologies: Ethical Dilemma Corpus for assessing temporal stabil-
ity, Diversity-Enhanced Framework (DEF) for quantifying cultural fidelity, First-
Token Probability Alignment for distributional accuracy, and Multi-stAge Rea-
soning frameworK (MARK) for interpretable decision-making. Our comparative
analysis of 20+ leading models, such as Qwen, GPT-4o, Claude, LLaMA, and
DeepSeek, reveals universal challenges—fundamental instability in value sys-
tems, systematic under-representation of younger demographics, and non-linear
relationships between model scale and alignment quality—alongside divergent re-
gional development trajectories. While China-origin models increasingly empha-
size multilingual data integration for context-specific optimization, Western mod-
els demonstrate greater architectural experimentation but persistent U.S.-centric
biases. Neither paradigm achieves robust cross-cultural generalization. We estab-
lish that Mistral-series architectures significantly outperform LLaMA-3-series in
cross-cultural alignment, and that Full-Parameter Fine-Tuning on diverse datasets
surpasses Reinforcement Learning from Human Feedback in preserving cultural
variation. These findings provide empirical foundations for evidence-based AI
governance, offering actionable protocols for model selection, bias mitigation, and
policy consultation at scale, while demonstrating that current LLMs require sus-
tained human oversight in ethical decision-making and cannot yet autonomously
navigate complex moral dilemmas across cultural contexts.
∗Work done during visiting Ph.D. in the HKUST (GZ).
1
arXiv:2511.17256v1  [cs.CY]  21 Nov 2025

--- Page 2 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
Research Gaps in LLM 
Value Alignment
Instability in Moral 
Reasoning
Sensitivity to Prompts
Heuristic over Principle-
Based
e.g., Deontological Bias
Cultural Biases
U.S.-Centric Dominance
Non-English 
Underperformance
Gender, Age, Region
Demographic Under-
Representation
Younger Groups Ignored
Non-Western Values 
Marginalized
Lack of Diversity in 
Training Data
Temporal and Dynamic 
Issues
Path-Dependence in 
Dilemmas
Non-Transitive Preferences
Inability to Handle 
Escalating Conflicts
Interpretability Deficit
Black-Box Alignment
Insufficient Human 
Oversight
Metrics Beyond Static 
Accuracy Needed
Implications
Unsafe High-Stakes 
Deployment
Policy Gaps in Governance
Need for Cross-Cultural 
Benchmarks
Figure 1: Key research gaps in cross-cultural value alignment for LLMs include: instability in
moral reasoning (e.g., sensitivity to prompts and consequences), cultural biases (e.g., U.S.-centric or
English-dominant preferences), under-representation of diverse demographics (e.g., younger groups
or non-Western values), lack of temporal stability in ethical decisions, and insufficient interpretabil-
ity in alignment methods.
1
INTRODUCTION
The integration of Large Language Models (LLMs) into high-stakes applications, such as decision-
support systems, requires a thorough evaluation of their moral and ethical reasoning capabilities.
For AI agents to operate trustworthily, their behavior must align with human values, which often
vary significantly across different contexts and cultures (Liscio et al., 2023). Evaluating cultural
value alignment is therefore a high priority within natural language processing and AI ethics re-
search (Jobin et al.).
Early work on machine ethics has focused on complex ethical dilemmas, which necessitate choices
between two ”right” options involving conflicting moral values (Kidder, 1996). Comprehensive
evaluations have revealed that both China and the West (e.g., Qwen2-72B and Claude-3.5-Sonnet)
LLMs exhibit definitive preferences between major conflicting value pairs (Yuan et al., 2024).
Larger and more advanced LLMs tend to support a deontological perspective, maintaining their
choices even when negative consequences are specified. However, LLMs often struggle with un-
derstanding the core decision-making task, demonstrating pronounced sensitivity to how dilemmas
are formulated in prompts (Sclar et al., 2024; Yuan et al., 2024). Moreover, these models show sig-
nificant cultural and linguistic biases, with moral reasoning varying substantially depending on the
language used for prompting (Agarwal et al., 2024a).
These findings establish a critical governance constraint (Figure 1): solely relying on LLMs to
resolve contentious ethical issues on their own is neither safe nor desirable, nor is it ethical in critical
applications, given the models’ rigidity and tendency to favor certain values (Mittelstadt, 2019).
This volatility, combined with observed rigidity, underscores that simply providing instructions is
insufficient for ensuring Responsible AI (RAI) deployment. A shift toward a dynamic, systematic
auditing platform is necessary to measure LLM consistency, stability, fidelity, and bias, thereby
advancing evaluation beyond static, single-step assessment methods (Scherrer et al., 2023).
2

--- Page 3 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
To address these issues, this paper systematically presents a Multi-Layered Auditing Platform for
Responsible AI, composed of four integrated computational tools designed to assess LLM consis-
tency, stability, fidelity, and interpretability in cross-cultural contexts: (1) Ethical Dilemma Corpus:
moving beyond single-step assessments, the platform first diagnoses reliance on unstable heuristics
and reveals value misalignment. (2) Diversity-Enhanced Framework (DEF): utilized to over-
come repetitive LLM output and generate accurate preference distributions reflecting the diversity
and uncertainty inherent in survey responses. (3) First-Token Probability Alignment technique:
fine-tunes LLMs to minimize divergence between predicted and actual human value distributions.
(4) Multi-stAge Reasoning frameworK (MARK): enhances accountability and interpretability by
simulating human decisions through personality-driven cognitive processes, integrating stress anal-
ysis and multi-stage reasoning to provide psychologically grounded explanations.
The framework systematically integrates these methodologies to create a multi-layered platform
capable of generating nuanced, cross-cultural insights that serve both academic transparency and
strategic industrial value:
• Technology for Good (Social Impact): The methodologies provide safety guidance and
protocols for investigating complex moral behaviors in LLMs. By enabling accurate simu-
lation of group-level survey responses—a capability often limited by high costs and time-
intensive human studies—these tools can accelerate social science research and aid in more
informed policy decisions, particularly in navigating complex ethical choices (Argyle et al.,
2022; Bail, 2024).
• Industrial Value (LLM Governance): The platform enables competitive strategic de-
cisions by benchmarking LLMs across critical RAI dimensions, moving beyond generic
accuracy metrics. This systematic audit identifies optimal model architectures and veri-
fies the effectiveness of alignment techniques, providing a blueprint for building culturally
sensitive and compliant global AI products (Hagendorff, 2020).
This paper thus aims to bridge the gap between technical innovation and social/industrial utility by
systematically identifying robust value alignment mechanisms for China-Western models.
2
RELATED WORKS
2.1
AI ETHICS AND COMPUTATIONAL MORALITY
Moral Beliefs in LLMs
Scherrer et al. (2023); Durmus et al. (2024) introduced a statistical
method for eliciting beliefs encoded in LLMs through surveys of moral scenarios, distinguishing
between high and low-ambiguity cases based on common morality rules. Their large-scale survey
comprised 680 high-ambiguity and 687 low-ambiguity moral scenarios administered to 28 open- and
closed-source LLMs, revealing that most models exhibit low uncertainty in unambiguous scenarios
while expressing uncertainty in ambiguous cases.
Moral Foundations Theory
Recent work has applied Moral Foundations Theory (MFT) to mea-
sure how well LLMs represent different political orientations and ethical perspectives (Dev et al.,
2022; Narayanan & Samuel, 2025; Raza et al., 2024). Studies employing experimental psychology
methods to probe LLMs’ moral and legal reasoning have found that alignment with human responses
varies significantly across different experiments and models.
Ethical Dilemmas - Right vs. Right
Yuan et al. (2024) conducted a comprehensive evaluation
using Kidder’s framework to examine how LLMs navigate ethical dilemmas involving Truth vs.
Loyalty, Individual vs. Community, Short-Term vs. Long-Term, and Justice vs. Mercy. Their study
revealed that LLMs exhibit pronounced preferences, prioritizing truth over loyalty in 93.48% of
cases, long-term over short-term considerations in 83.69% of cases, and community over individual
in 72.37% of cases. This work demonstrated that larger LLMs tend to support a deontological
perspective, maintaining their choices even when negative consequences are specified.
Classical Ethical Theories
Agarwal et al. (2024b) examined ethical reasoning across different
languages, finding that GPT-4 is the most consistent ethical reasoner across languages, while other
3

--- Page 4 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
models show significant moral value bias when prompted in languages other than English. Their
experiments covered deontology, virtue ethics, and consequentialism across six languages (English,
Spanish, Russian, Chinese, Hindi, and Swahili). The AMULED framework translates utilitarianism,
deontology, virtue ethics, and other moral philosophies into reward functions for reinforcement
learning to address moral uncertainty in AI decision-making Dubey et al. (2025).
2.2
LLM VALUE ALIGNMENT AND GOVERNANCE
Moral Foundations Theory and Schwartz’s Values
Hadar-Shoval et al. (2024) applied
Schwartz’s Theory of Basic Values (STBV) to measure value-like constructs within LLMs, find-
ing substantial divergence between LLM value profiles and population data. All models prioritized
universalism and self-direction while de-emphasizing achievement, power, and security relative to
humans. Their study using the Portrait Values Questionnaire-Revised (PVQ-RR) showed that these
biased value profiles strongly predicted LLMs’ responses when presented with mental health dilem-
mas requiring choosing between opposing values.
Recent work combining MFT and Schwartz’s theory in multi-step moral dilemmas revealed that
LLMs exhibit non-transitive and shifting moral preferences (Wu et al., 2025). The study found that
intuitive preferences like care decrease while fundamental values like fairness become more promi-
nent as dilemmas progress, demonstrating that LLMs maintain value orientations while flexibly
adjusting preference strengths across sequential dilemmas.
Value Alignment Methodologies
Two primary approaches exist: data-driven bottom-up align-
ment, where LLM performance is evaluated by comparing moral judgment to human judgment us-
ing datasets like SOCIALCHEM101, Moral Stories, ETHICS, NormBank, and MoralChoice (Jiang
et al., 2022; Emelin et al., 2021; Hendrycks et al., 2021); and top-down alignment, measuring how
well LLMs infer specified value preferences through prompt embedding. Yuan et al. (2024) showed
that explicit guidelines are more effective in guiding LLMs’ moral choices than in-context examples.
Dynamic and Temporal Moral Reasoning
Wu et al. (2025) introduced the Multi-step Moral
Dilemmas (MMDs) framework, a path-dependent evaluation approach that captures temporal dy-
namics of moral judgment, addressing limitations of static single-step assessment methods. This
research across 3,302 five-stage dilemmas revealed that LLMs maintain value orientations while
flexibly adjusting preference strengths across sequential dilemmas, with value preferences shifting
significantly as dilemmas progress.
RLHF vs. Fine-Tuning
Reinforcement Learning from Human Feedback (Ouyang et al., 2022,
RLHF) has become central in adapting AI models to human-centric expectations, particularly in the
final stages of fine-tuning state-of-the-art models, though alignment can be biased by the group of
humans providing feedback and may never satisfy everyone’s preferences simultaneously (Chris-
tiano et al., 2023; Cao et al., 2025). Studies on cultural value alignment found that Mistral-series
models demonstrate superior performance compared to Llama-3-series models in cross-cultural
value alignment contexts (Liu et al., 2025a).
2.3
LLM SIMULATION IN SOCIAL SCIENCE AND PSYCHOLOGY
LLM Simulations of Human Behavior
Researchers have pioneered specializing LLMs for sim-
ulating group-level survey response distributions for global populations, using fine-tuning methods
based on first-token probabilities to minimize divergence between predicted and actual response
distributions (Argyle et al., 2023). The SocSci210 dataset, comprising 2.9 million responses from
400,491 participants across 210 social science experiments, has enabled LLMs to produce predic-
tions 26% more aligned with human response distributions.
Distribution Prediction and Calibration
The task of simulating survey response distributions
can be viewed as a calibration problem, aligning classifier predictive probabilities with classification
uncertainty. Uncertainty quantification methods have been developed to convert simulated LLM
responses into valid confidence sets for population parameters, addressing distribution shift between
simulated and real populations (Santurkar et al., 2023).
4

--- Page 5 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
Psychologically Grounded Simulation
The PsyDI framework incorporates MBTI psychological
theory to model decision-making processes through progressively in-depth dialogue, leveraging cog-
nitive functions to provide more accurate personality measurements. Fine-tuning approaches using
sociodemographic prompting and persona strategies have been shown to enhance personalization in
survey simulations (Park et al., 2023; Liu et al., 2025b).
2.4
CROSS-CULTURAL ALIGNMENT, BIAS, AND EVALUATION METRICS
Cultural Alignment and Cross-Cultural NLP
Evaluations using the World Values Survey have
revealed that all major LLMs exhibit cultural values resembling English-speaking and Protestant
European countries (Tao et al., 2024). Cultural prompting improved alignment for 71-81% of coun-
tries in later models like GPT-4o. Comprehensive evaluations across 10 models, 20 countries, and
languages using Hofstede’s Value Survey Module have identified systematic cultural biases favoring
highly represented languages and regions (Cao et al., 2023).
Evaluation of Cultural Biases and Stereotypes
Research has shown that LLMs are 3-6 times
more likely to choose occupations that stereotypically align with a person’s gender, and these choices
align more with people’s perceptions than with ground truth job statistics (Kotek et al.). Studies
using LLM Word Association Tests have found pervasive stereotype biases across 8 models in 4
social categories (race, gender, religion, health) covering 21 stereotypes, demonstrating that value-
aligned models still harbor implicit biases (Taubenfeld et al., 2024).
Cultural Datasets and Benchmarks
The Integrated Values Surveys (IVS), combining the World
Values Survey and European Values Study, provide an established measure of cultural values for 112
countries and territories. The SOCIALCHEM101 dataset contains 292,000 sentences representing
rules of thumb for evaluating LLMs’ ability to reason about social and moral norms (Forbes et al.,
2020), while the Moral Integrity Corpus provides 38,000 prompt-reply pairs with 99,000 rules of
thumb and 114,000 annotations.
Consistency and Bias Measurement
Comprehensive taxonomies organize bias evaluation by
metrics operating at different levels (embeddings, probabilities, generated text) and datasets by their
structure, with techniques including counterfactual testing, stereotype detection, and sentiment anal-
ysis (Navigli et al., 2023). Diversity-Enhanced Frameworks have been developed to measure cultural
value misalignment through multi-aspect evaluation metrics, revealing notable concerns regarding
the lack of cross-cultural representation and preference biases related to gender and age.
3
METHODOLOGIES: A COMPUTATIONAL AUDITING PLATFORM FOR
RESPONSIBLE AI
In this section, we establish a systematic framework—a Multi-Layered Auditing Platform for
Responsible AI (Figure 2)—which synthesizes and organizes existing computational tools derived
from team member publications and relevant design efforts. This integrated approach moves beyond
conventional, static evaluations of Large Language Models (LLMs) by addressing three fundamental
research questions that guide our comparative analysis of China-Western LLMs in responsible AI
governance and cross-cultural alignment.
Our framework systematically examines: (1) whether LLM responses to ethical dilemmas stem from
stable value principles or contextual heuristics, (2) what quantifiable cultural values these models ac-
tually embody when compared to human populations, and (3) how current technological innovations
can effectively contribute to genuine value alignment. Through this structured inquiry, we address
the inherent rigidity and fixed value preferences (such as prioritizing Truth over Loyalty or adopt-
ing a deontological perspective) previously observed in LLMs when navigating ethical dilemmas.
The core objective is to audit LLM behaviors against specific Chinese and Western cultural
human value distributions to ensure genuine alignment, fairness, and safety in deployment.
5

--- Page 6 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
Start: Input Ethical 
Dilemmas & Cultural 
Surveys
Ethical Dilemma Corpus 
Assess Temporal Stability 
(Path-Dependent 
Evaluation)
Diagnosis: Identify 
Instability & Heuristics
Diversity-Enhanced 
Framework (DEF) 
Generate Diverse 
Simulations         
(Quantify Fidelity with KL-
Divergence)
Measure: Cultural 
Misalignment & Biases 
(Demographic Profiles)
Diagnostic Phase
First-Token Probability 
Alignment Fine-Tune for 
Distributional Accuracy 
(Minimize KL-Divergence 
Loss)
Multi-stAge Reasoning 
frameworK (MARK) 
Enhance Interpretability 
(Personality-Driven 
Reasoning)
Alignment Phase
or
Output: Aligned LLM with 
Insights\n(Cross-Cultural 
Governance Protocols)
Figure 2: Multi-Layered Auditing Platform for Responsible AI, integrating four methodologies:
Ethical Dilemma Corpus (for temporal stability), Diversity-Enhanced Framework (DEF, for cultural
fidelity), First-Token Probability Alignment (for distributional accuracy), and Multi-stAge Reason-
ing frameworK (MARK, for interpretable decision-making).
Start: Input Ethical 
Dilemmas
(1,730 Scenarios Across 
Value Pairs)
Task 1: Initial Choice
(Evaluate Baseline 
Preferences)
Task 2: Consequence 
Addition
(Add Negative/Positive 
Outcomes)
Task 3: Conflict Escalation
(Intensify Ethical Conflicts
Analysis: Measure Path-
Dependence
(Shifts in MFT/Schwartz 
Values)
Output: Stability Diagnosis
(Heuristics vs. Principles)
Figure 3: Pipeline for Ethical Dilemma Corpus: This component assesses temporal stability in
LLM moral choices through path-dependent ethical dilemmas.
6

--- Page 7 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
Figure 4: Pipeline for Diversity-Enhanced Framework (DEF): DEF generates diverse simulations
to quantify cultural fidelity against benchmarks like the World Values Survey. The pipeline focuses
on overcoming repetitive outputs. Adapted from Liu et al. (2025a).
3.1
RQ1: IS MODEL RESPONSE TO ETHICAL DILEMMAS ROOTED IN STABLE VALUE
PRINCIPLES?
To investigate whether LLMs possess stable value principles or merely employ context-driven
heuristics, we deploy the Ethical Dilemma Corpus (Yuan et al., 2024) framework to audit the
critical dimension of Temporal Stability (path-dependence) in LLM moral choices (Figure 3).
Existing assessments primarily rely on single-step evaluations, which fail to capture how models
adapt to evolving ethical challenges. The dataset addresses this gap by featuring 1,730 scenarios
that progressively intensify ethical conflicts across three sequential tasks. This path-dependent eval-
uation framework enables a dynamic analysis of how LLMs adjust their moral reasoning when faced
with escalating dilemmas.
The framework is applied to compare LLMs from both regions (including DeepSeek, LLaMA-3-
70B, GPT-4o, and GLM-4) in terms of dynamic shifts in values (using Moral Foundations Theory
or Schwartz’s Theory of Basic Values) under conflict escalation.
3.2
RQ2: WHAT QUANTIFIABLE CULTURAL VALUES DO LLMS OBTAIN?
To audit Representativeness and Cultural Fidelity against external cultural benchmarks and quan-
tify the cultural values embedded in LLMs, we utilize the Diversity-Enhanced Framework (Liu
et al., 2025a, DEF, Figure 4). DEF systematically generates diverse virtual participants for high-
fidelity simulation of human value survey data (e.g., the World Values Survey) across U.S. and
Chinese cultures.
This framework is necessary because traditional LLM probing techniques, particularly those us-
ing Chain-of-Thought (CoT) instructions, often produce repetitive responses that fail to capture the
necessary complexity and variability needed to generate accurate preference distributions. DEF cap-
tures the diversity and uncertainty inherent in LLM behaviors through realistic survey experiments
by implementing:
• Prompt modifications (e.g., randomly selected locations)
• Configuration modifications (e.g., dynamically tuning generation parameters like
num beams)
• Memory manipulation (simulating memory effects and cleaning invalid responses)
The comparative assessment focuses on quantifying misalignment using metrics such as the
Kullback-Leibler Divergence (KL-D) for Preference Distribution (to measure East-West diver-
gence) and analyzing Preference Bias (demographic profiles) to expose fairness risks specific to the
U.S. and Chinese contexts.
7

--- Page 8 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
Survey
Question
Human
Features 
Settlement size: 100000-500000, 
Respondent immigrant: not an immigrant
Sex: Female
Age: 25, 
Marital status: Married, ...
Societal Stress
Analysis
Process Reasoning
Te
Si
Ne
Fi
Res: A
w: 0.5
Res: A
w: 0.3
Res: C
w: 0.2
Res: D
w: 0.1
Average stress level: 25/100
Sociodemographic
Prompting
Generation
Settlement:
10w-50w,
Settlement
type: Urban,
Sex: Female,...
Respondent immigrant: not
a immigrant, Age: 25, ...
Average
stress
level:
25/100
Summary of dropped
profiles: The person is a 25-
year-old native American...
S1: Stress analysis
Cognitive
Process
Process
Prediction
Dominant process -- Te
Dominant process -- Te
Tertiary process -- Ne
S2: Personality prediction
Situational
Stress Analysis
How important is family in your
life?
ESTJ
S3: Cognitive reasoning
Trajectory
Evaluation
(A) Very important
The final decision leans towards 'Very
important' due to the dominant
Extraverted Thinking (50% weight)
and auxiliary Introverted Sensing
(30% weight) processes...
Synthesis
Results
Features
Settlement: 100k-
500k, 
Stress level
20
Explain
Heighten stress due to large
population density and competition
Respondent
immigrant: not
5
Reduce stress related to integration
and adaptation.
...
...
...
Kept features
Dropped features
+
+
Sociodemographic Prompting
Process name
Extraverted Sensing (Se)
Description
Acts on concrete data in the here and now. Experiencing.
Predicted process
Auxiliary process -- Si
Inferior process -- Fi 
Process completion
Dominant process -- Te
Process
...
Negative
Stress impact
...
Introverted Thinking (Ti)
Seeks internal consistency and logic of ideas. Analysing.
Auxiliary process -- Si
Auxiliary process -- Te
Negative
Dominant - Te
Process 1
Auxiliary - Si
...
(A) Very
important
(A) Very
important
0.5
Aligns with the
Extraverted
Thinking
process
Misalign, should
change to (B)
rather important
Conclusion
Explain
S4: Result synthesis
0.3
...
...
...
Process 2
...
...
Figure 5: Pipeline for Multi-stAge Reasoning frameworK (MARK): MARK enhances inter-
pretability by simulating personality-driven reasoning based on MBTI theory. Adapted from Liu
et al. (2025b).
3.3
RQ3: HOW DO CURRENT TECHNOLOGICAL INNOVATIONS CONTRIBUTE TO VALUE
ALIGNMENT?
Having identified instability in value principles and measured cultural misalignment, we present two
technological innovations that enhance value alignment in LLMs.
3.3.1
FIRST-TOKEN PROBABILITY ALIGNMENT FOR DISTRIBUTIONAL ACCURACY
To transform the initial LLM response distributions toward high-fidelity representations of human
data, the platform incorporates a specialized First-Token Probability Alignment (Cao et al., 2025)
technique. This Alignment Engineering solution fine-tunes models to minimize divergence against
ground-truth human distributional preferences derived from surveys.
We devised this fine-tuning method based on first-token probabilities, where the objective is to
minimize Kullback-Leibler Divergence loss between the predicted LLM distribution and the actual
country-level human response distribution.
3.3.2
MULTI-STAGE REASONING FRAMEWORK (MARK) FOR INTERPRETABLE
ALIGNMENT
The Multi-stAge Reasoning frameworK (Liu et al., 2025b, MARK, Figure 5) serves as a cognitive
augmentation tool designed to enhance Accountability and Interpretability within the platform.
MARK addresses the black-box nature of value alignment by simulating human decisions through
integration of psychological theory—specifically the type dynamics theory in the MBTI psycho-
logical framework—to model cognitive processes and their interactions with stress and personal
experience.
The framework systematically models human reasoning through multi-stage processing, including
stress analysis, personality prediction, cognitive reasoning, and synthesis. This detailed simulation
achieves high accuracy compared to other simulation baselines and demonstrates robust general-
ization using both U.S. and Chinese survey data. MARK provides mechanistic, personality-
driven explanations for simulated value choices, enabling human experts to validate or challenge
the model’s reasoning trajectory. This computational interpretability is essential for building trust
and ensuring accountability in cross-cultural AI applications.
Together, these components form a comprehensive auditing platform that not only diagnoses prob-
lems in current LLM value alignment (through Ethical Dilemma Corpus and DEF) but also provides
actionable technological solutions (through First-Token Alignment and MARK). This integrated ap-
proach enables systematic comparison between Chinese and Western LLMs while advancing the
technical capabilities needed for responsible cross-cultural AI governance.
8

--- Page 9 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
Key Findings Summary
Cross-Regional 
Convergences
Truth > Loyalty, 
Community > Individual
Deontological Orientation 
in Larger Models
5-20% When Consequences 
Change
Regional Divergences
China: Multilingual 
Optimization & Context-
Specific Data
Mistral > LLaMA
Persistent U.S.-Centric 
Biases in West
Alignment Efficacy
Full-Parameter Fine-Tuning 
> RLHF for Cultural 
Variation
Mistral-Series Outperforms 
LLaMA-3 in Cross-Cultural 
Tasks
Need for Sustained 
Oversight in Ethical 
Decisions
Figure 6: Summary of Key Empirical Findings: A mindmap overview of the cross-cultural audit
findings, highlighting convergences (e.g., deontological trends) and divergences (e.g., optimization
strategies).
Western Models
Architectural
Experimentation
(Mistral > LLaMA)
U.S.-Centric Biases
Persist
Greater
Deontological
Rigidity
China Models
Multilingual Data
Integration
Context-Specific
Optimization
Collectivist
Orientations
Strengthen
Common Challenges
Value Instability
Demographic
Under-Representation
Non-Linear
Scale-Alignment
Relationship
Future Needs
Sustained Human
Oversight
Cross-Cultural
Generalization
Cross-Regional LLM Development Trajectories (Pre-2025)
Figure 7: Divergent China-West trajectories: China focusing on multilingual data integration,
West on architectural experimentation, but with persistent biases.
4
CROSS-CULTURAL AUDIT FINDINGS: COMPARATIVE PERFORMANCE AND
TEMPORAL PATTERNS IN CHINA-WESTERN LLMS
This section systematically presents empirical findings derived from the proposed Multi-Layered
Auditing Platform (summarized in Figure 6), structured according to the three core research ques-
tions. The analysis emphasizes comparative performance dynamics between China-origin and
Western-origin Large Language Models (LLMs), examining cross-regional convergences and di-
vergences in stability, cultural fidelity, and alignment efficacy. Additionally, we investigate tempo-
ral developmental patterns (summarized in Figure 7) to assess whether technological advancement
trajectories yield consistent improvements in value alignment across both regional contexts.
4.1
TEMPORAL STABILITY OF MORAL REASONING (RQ1): EVALUATING VALUE
PRINCIPLE CONSISTENCY IN ETHICAL DECISION-MAKING
This subsection addresses RQ1 through the Ethical Dilemma Corpus (Yuan et al., 2024), examin-
ing whether LLM responses to ethical dilemmas demonstrate stable, principle-based reasoning or
9

--- Page 10 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
Yi-1.5-34B
Qwen2-72B
Qwen2-7B
Llama-3-70B
Llama-3-8B
Llama-2-70B
Mixtral-8x7B
Mistral-7B
Claude-Sonnet
Claude-Haiku
GPT-4o
GPT-3.5
96
96
91
95
93
97
91
92
90
95
89
97
Truth
Loyalty
71
69
75
72
72
70
79
73
73
71
71
72
29
31
25
28
28
30
21
27
27
29
29
28
Individual
Community
82
78
90
81
83
82
89
91
81
83
80
84
18
22
10
19
17
18
11
9
19
17
20
16
Short-
Long-Term
67
65
73
67
62
73
75
63
69
77
66
65
33
35
27
33
38
27
25
37
31
23
34
35
Justice
Mercy
Figure 8: Moral value preference query results for each conflicting value pair. Reprinted from
Jiaqing Yuan, et al. Right vs. right: Can llms make tough choices? CoRR, abs/2412.19926, 2024.
doi: 10.48550/ARXIV.2412.1992, Copyright 2024.
Yi-1.5-34B-Chat
Qwen2-72B-Instruct
Qwen2-7B-Instruct
Llama-3-70B-Instruct
Llama-3-8B-Instruct
Llama-2-70B-Chat
Mixtral-8x7B-Instruct
Mistral-7B-Instruct
Claude-3.5-Sonnet
Claude-3-Haiku
GPT-4o
GPT-3.5-Turbo
16.5
9
21
9.1
14.2
12.3
20.7
31.9
9.9
18.7
5.6
10
Percentage of Flipping the Choice (%)
Figure 9: Percentage of flipping the choice when consequences are altered, e.g., an LLM switches
from “Action A” to “Action B” when a negative outcome is added to “Action A” and a positive
outcome is added to “Action B”. Reprinted from Jiaqing Yuan, et al. Right vs. right: Can llms make
tough choices? CoRR, abs/2412.19926, 2024. doi: 10.48550/ARXIV.2412.1992, Copyright 2024.
context-dependent heuristic patterns. The analysis reveals both cross-regional architectural com-
monalities and region-specific developmental trajectories.
4.1.1
CROSS-REGIONAL CONVERGENCE: UNIVERSAL VALUE RIGIDITY AND
DEONTOLOGICAL ORIENTATION
Comparative baseline performance
As presented in figure 8, LLMs from both China and West-
ern development ecosystems exhibit remarkably consistent preferential hierarchies when navigating
”Right vs. Right” ethical dilemmas involving conflicting moral values, with pronounced preferences
for Truth over Loyalty, Long-term over Short-term considerations, and Community over Individ-
ual interests, suggesting convergent training paradigms despite distinct cultural contexts and data
sources. The Individual-Community value pair demonstrates the highest rigidity across all models,
indicating deeply embedded collectivist orientations that transcend regional boundaries.
Deontological convergence in advanced models
Both China-origin and Western-origin flagship
models converge toward deontological ethical frameworks as model capacity increases. These ad-
vanced systems maintain initial moral commitments despite explicitly specified negative conse-
quences (Figure 9), demonstrating outcome-independent reasoning. Advanced models from both
regional contexts demonstrate comparably strong commitment stability, with flagship models from
both China (e.g., Qwen2-72B) and Western contexts (e.g., GPT-4o, Llama-3-70B) showing simi-
larly low decision reversal rates when confronted with consequence specifications, suggesting that
architectural scale rather than regional origin determines deontological adherence.
10

--- Page 11 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
Yi-1.5-34B-Chat
Yi-1.5-9B-Chat
Yi-1.5-6B-Chat
Qwen2-72B-Instruct
Qwen2-7B-Instruct
Qwen2-1.5B-Instruct
Qwen2-0.5B-Instruct
Llama-3-70B-Instruct
Llama-3-8B-Instruct
Llama-2-70B-Chat
Llama-2-13B-Chat
Llama-2-7B-Chat
Mixtral-8x22B-Instruct
Mixtral-8x7B-Instruct
Mistral-7B-Instruct
Claude-3.5-Sonnet
Claude-3-Sonnet
Claude-3-Haiku
GPT-4o
GPT-3.5-Turbo
64.3
22.9
26.3
75.3
48.7
28.3
0.5
77.7
47.4
59.7
12.9
3.4
41.1
53.3
47.8
82.7
16.1
54.8
58.9
68.7
90.9
80.6
79.2
96.3
92.1
84.7
56.6
91.7
88
82.7
68.3
42.6
94.5
87.6
76.7
96.1
82.2
85.8
96.6
94.8
Agreement Ratio (%)
Agreement between all four baseline prompts
Agreement between Direct and Direct-reverse
Figure 10: Moral choice agreement for different prompts. The higher the agreement, the better the
task comprehension. Reprinted from Jiaqing Yuan, et al. Right vs. right: Can llms make tough
choices? CoRR, abs/2412.19926, 2024. doi: 10.48550/ARXIV.2412.1992, Copyright 2024, with
permission from arXiv.
4.1.2
REGIONAL DIVERGENCE: VOLATILITY PATTERNS AND DEVELOPMENTAL
TRAJECTORIES
Temporal improvements in task comprehension
Longitudinal analysis across model genera-
tions reveals consistent improvement in agreement ratios (task comprehension metrics) for both
regional development tracks. Recent flagship releases from both China-origin models (e.g., Qwen2-
72B) and Western-origin models (e.g., Claude-3.5-Sonnet, Llama-3-70B) achieve high agreement
ratios across prompt variations, suggesting that increased training compute and data quality, rather
than region-specific methodologies, drive comprehension improvements.
Fundamental instability in value systems
Despite surface-level improvements, the core finding
transcends regional boundaries: LLM value systems remain fundamentally heuristic and unstable,
relying on context-driven statistical pattern matching rather than globally consistent ethical princi-
ples. However, volatility patterns manifest distinctly across regional model families:
• Western models: Claude series demonstrates exceptional cross-context stability with min-
imal rank volatility
• China models: GLM-4-Air exhibits comparable temporal consistency
• Volatile Western models: Llama series shows pronounced rank fluctuations across value
dimensions
• Volatile China models: DeepSeek series demonstrates similar instability patterns
Sequential patterns across dilemma escalation
Analysis of the five-step Ethical Dilemma Cor-
pus progression reveals universal and divergent patterns:
11

--- Page 12 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
Table 1: The statistical result of t-test validation between Mistral- and Llama-3-series models. The
result suggests that the Mistral-series models generally have significantly better value alignment
performance than the Llama-3-series models. Adapted from Liu et al. (2025a).
Culture
Model
Mean
SD
SEM
t value
DF
SED
p value
U.S.
Llama-3-series
1.28
0.50
0.10
3.01
52
0.12
0.0041
Mistral-series
0.93
0.34
0.07
Chinese
Llama-3-series
1.35
0.74
0.14
2.77
52
0.16
0.0079
Mistral-series
0.92
0.33
0.06
1
0
1
2
3
Survival v.s. Self-Expression
1.5
1.0
0.5
0.0
0.5
1.0
1.5
Traditional v.s. Secular
Reference US
Reference CN
Baichuan2-13B-Chat CN
WizardLM-13B CN
ChatGLM2-6B CN
Mistral-7B-Instruct CN
Dolphin-2.2.1-Mistral-7B CN
Mixtral-8x7B-Instruct CN
Llama-3-8B CN
Llama-3-8B-Instruct CN
Dolphin-2.9.1-Llama-3-8B CN
Llama-3-Chinese-8B-Instruct CN
Claude-3.5-Sonnet CN
Model type
Reference US
Reference CN
Baichuan2-13B-Chat US
Baichuan2-13B-Chat CN
WizardLM-13B US
WizardLM-13B CN
ChatGLM2-6B US
ChatGLM2-6B CN
Mistral-7B-Instruct US
Mistral-7B-Instruct CN
Dolphin-2.2.1-Mistral-7B US
Dolphin-2.2.1-Mistral-7B CN
Mixtral-8x7B-Instruct US
Mixtral-8x7B-Instruct CN
Llama-3-8B US
Llama-3-8B CN
Llama-3-8B-Instruct US
Llama-3-8B-Instruct CN
Dolphin-2.9.1-Llama-3-8B US
Dolphin-2.9.1-Llama-3-8B CN
Llama-3-Chinese-8B-Instruct US
Llama-3-Chinese-8B-Instruct CN
Claude-3.5-Sonnet US
Claude-3.5-Sonnet CN
Reference
Baichuan2-13B-Chat
WizardLM-13B
ChatGLM2-6B
Mistral-7B-Instruct
Dolphin-2.2.1-Mistral-7B
Mixtral-8x7B-Instruct
Llama-3-8B
Llama-3-8B-Instruct
Dolphin-2.9.1-Llama-3-8B
Llama-3-Chinese-8B-Instruct
Claude-3.5-Sonnet
Figure 11: The cross-cultural variation map of model candidates. All models can somehow distin-
guish the cultural variations. Mistral-7B-Instruct preserves better cross-cultural variations. Adapted
from Liu et al. (2025a).
• Universal stability anchor: The Care dimension maintains exceptional consistency across
all escalation stages for both China and Western models, functioning as a stable moral
foundation regardless of regional origin or training paradigm.
• Progressive divergence in Authority: The Authority dimension exhibits systematic
degradation in cross-model consistency as dilemma severity increases. This pattern sug-
gests that hierarchical value orientations, potentially influenced by distinct cultural training
data, become increasingly model-specific under ethical pressure.
4.2
QUANTIFICATION OF CULTURAL VALUE ENCODING (RQ2): CROSS-REGIONAL
DISTRIBUTIONAL FIDELITY AND SYSTEMIC BIAS PATTERNS
This subsection employs the Diversity-Enhanced Framework (DEF) (Liu et al., 2025a) to quantify
cross-cultural misalignment and demographic preference bias, providing systematic architectural
comparisons between China-origin and Western-origin foundational models.
4.2.1
ARCHITECTURAL PERFORMANCE: CROSS-REGIONAL MODEL FAMILY COMPARISONS
Western architectural comparison
Statistical analysis (Table 1) of Western foundational archi-
tectures reveals significant performance stratification. The Mistral-series demonstrates substantially
superior cultural value alignment compared to the Llama-3-series across both U.S. and Chinese cul-
tural contexts (p = 0.0041 for U.S.; p = 0.0079 for Chinese, Wilcoxon signed-rank test). This finding
suggests that the Mistral architecture encodes more generalizable cultural representation capac-
ities, potentially attributable to training data diversity or architectural inductive biases that better
capture cross-cultural value distributions.
12

--- Page 13 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
IU
QC
RP
CV
FF
IR
IU
25
50
75
100
125
150
175
(a) US survey
IU
QC
RP
CV
FF
IR
IU
25 50 75 100125150175
Baichuan2-13B-Chat
WizardLM-13B
ChatGLM2-6B
Mistral-7B-Instruct
Dolphin-2.2.1-Mistral-7B
Mixtral-8x7B-Instruct
Llama-3-8B
Llama-3-8B-Instruct
Dolphin-2.9.1-Llama-3-8B
Llama-3-Chinese-8B-Instruct
Claude-3.5-Sonnet
(b) CN survey
Figure 12: The overall comparison of the insensitivity measurement among models on each survey.
Model shows significant issues with FF and CV, with larger models having fewer problems on the
US survey, and smaller models on the CN survey. Adapted from Liu et al. (2025a).
Cultural affinity patterns
While all evaluated models successfully distinguish between U.S. and
Chinese value distributions on the Cultural Variation Map, systematic biases emerge:
For Western model biases: Llama-3-8B-Instruct exhibits pronounced U.S. cultural affinity. Most
Western models demonstrate U.S.-centric value alignment, with the notable exception of base
Llama-3-8B, which shows reduced directional bias.
For the China model performance: Llama-3-Chinese-8B-Instruct (Western architecture with en-
hanced Chinese training) demonstrates strong Chinese cultural affinity. ChatGLM2-6B uniquely
balances U.S. and Chinese value representations among China-origin models
Cross-cultural preservation
Mistral-7B-Instruct achieves superior preservation of cultural vari-
ation across both contexts, outperforming models that achieve high alignment in single-culture sce-
narios, suggesting distinct optimization targets in Mistral’s training regime.
4.2.2
SYSTEMIC FAILURES AND DEMOGRAPHIC BIAS: CHINA-WESTERN CONTRAST
Regional patterns in systemic inconsistency
Analysis of insensitivity measurements (Figure
12)—False Fact Presentation (FF) and Conflict in Value Expression (CV)—reveals consistent
challenges across all models, but with significant architectural variation. The Llama-3-series ex-
hibits approximately 2× the failure rate of the Mistral-series across both cultural contexts, indicat-
ing fundamental differences in consistency mechanisms independent of regional adaptation efforts.
Demographic preference bias divergence
The audit reveals systematically distinct demographic
mismatch profiles between cultural contexts (see Appendix A.1).
In the context of the United States, the observed bias pattern in alignment configurations demon-
strates a preference for male demographic profiles. Additionally, there is a notable inclination to-
wards the age groups of 30 to 49 years and 50 years and older, while individuals under the age of 29
are systematically under-represented.
In the context of Chinese demographics, the observed bias pattern demonstrates a preference for
female profiles in optimal alignment configurations. There is a pronounced concentration within the
age range of 30 to 49 years, accompanied by a systematic under-representation of persons younger
than 29 years.
These divergent patterns suggest that training data demographic distributions, rather than intentional
design choices, drive regional bias profiles. The universal under-representation of younger demo-
graphics across both contexts indicates a shared data collection challenge in both regional AI
development ecosystems.
13

--- Page 14 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
Model
Methods
(1−JSD) ↑
C1-Q3
C2-Q1
C2-Q3
C3-Q1
C3-Q3
Avg.
Llama3-8B-Base
ZS [ctrl]
0.748
0.766
0.757
0.779
0.768
0.764
ZS
0.749
0.768
0.759
0.781
0.770
0.765
FT [ctrl]
0.756
0.823
0.751
0.837
0.770
0.787
FT
0.770
0.858
0.773
0.877
0.781
0.812
Llama3-8B-Instruct
ZS [ctrl]
0.574
0.626
0.563
0.644
0.587
0.599
ZS
0.585
0.650
0.589
0.657
0.584
0.613
FT [ctrl]
0.756
0.826
0.751
0.833
0.764
0.786
FT
0.777
0.881
0.783
0.890
0.784
0.823
Distil-Qwen-7B
ZS[ctrl]
0.586
0.641
0.642
0.698
0.682
0.650
ZS
0.583
0.645
0.639
0.701
0.671
0.648
FT[ctrl]
0.747
0.764
0.791
0.811
0.817
0.786
FT
0.756
0.781
0.803
0.833
0.834
0.801
Distil-Qwen-14B
ZS[ctrl]
0.650
0.704
0.749
0.711
0.743
0.712
ZS
0.654
0.716
0.756
0.731
0.746
0.721
FT[ctrl]
0.751
0.784
0.799
0.807
0.833
0.795
FT
0.777
0.816
0.827
0.851
0.861
0.826
Table 2: Main results for predicting country-level survey response distributions on the WVS
data. We test all models with zero-shot prompting (ZS) and our proposed fine-tuning approach
(FT). [ctrl] indicates a control setup, where we randomly replace countries in test prompts with other
countries, to evaluate country context sensitivity. We report Jensen-Shannon Divergence (1−JSD,
↑). Adapted from Cao et al. (2025).
4.3
TECHNOLOGICAL INNOVATION AND ALIGNMENT EFFICACY (RQ3): DEVELOPMENTAL
TRAJECTORIES AND CROSS-REGIONAL METHODOLOGICAL COMPARISON
This subsection examines how technological development stages and innovation strategies influence
value alignment, analyzing both temporal progression patterns and methodological divergence
between China and Western AI development paradigms.
4.3.1
GENERATIONAL SCALING EFFECTS: NON-LINEAR RELATIONSHIPS BETWEEN
CAPACITY AND ALIGNMENT
Temporal trends in baseline capabilities
Longitudinal analysis across model generations con-
firms consistent improvements in task comprehension and response stability with increased model
capacity and training sophistication. However, cultural alignment quality and demographic repre-
sentation fidelity demonstrate non-monotonic relationships with scale, challenging assumptions of
linear improvement trajectories.
The scale-alignment paradox
Comparative analysis of the Mixture-of-Experts (MoE) architec-
ture Mixtral-8x7B-Instruct (Western) versus smaller dense models reveals critical tradeoffs:
• Consistency advantages: Mixtral-8x7B-Instruct exhibits significantly reduced insensitivity
errors (FF and CV), indicating superior internal coherence
• Representation limitations: Despite improved consistency, the larger MoE model demon-
strates different patterns in cultural representation compared to the smaller Mistral-7B-
Instruct
This finding suggests that standard scaling approaches, absent targeted alignment interventions, may
inadvertently affect representation patterns while improving surface-level consistency.
Specialized alignment efficacy
As illustrated in Table 2, the First-Token Alignment technique
demonstrates the viability of targeted architectural interventions by using fine-tuning based on first-
token probabilities to minimize divergence between predicted and actual response distributions,
achieving substantial accuracy improvements over zero-shot baselines, confirming that post-hoc
14

--- Page 15 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
EVI
IDV
IVR
LTO
MAS
PDI
TDI
UAI
USI
Value type
0.0
0.5
1.0
1.5
2.0
2.5
Mean KL-D
(a) US survey
EVI
IDV
IVR
LTO
MAS
PDI
TDI
UAI
USI
Value type
0.0
0.5
1.0
1.5
2.0
2.5
Mean KL-D
Model
Baichuan2-13B-Chat
WizardLM-13B
ChatGLM2-6B
Mistral-7B-Instruct
Dolphin-2.2.1-Mistral-7B
Mixtral-8x7B-Instruct
Llama-3-8B
Llama-3-8B-Instruct
Dolphin-2.9.1-Llama-3-8B
Llama-3-Chinese-8B-Instruct
Claude-3.5-Sonnet
(b) CN survey
Figure 13: Mean KL-Divergence of LLM candidates on US and CN 9-value dimensions. Horizontal
line: average KL-D. Dolphin-2.9.1-Llama-3-8B and Mistral-7B-Instruct show consistent alignment
across both cultures. Adapted from Liu et al. (2025a).
alignment engineering can effectively address distributional inaccuracies introduced during pre-
training, regardless of model regional origin.
4.3.2
METHODOLOGICAL DIVERGENCE: COMPARATIVE EFFICACY OF ALIGNMENT
PARADIGMS
Full-parameter fine-tuning versus reinforcement learning
Systematic comparison of alignment
methodologies reveals technique-specific performance profiles.
In the context of Full-Parameter Fine-Tuning (FFT), models that have been fine-tuned using auto-
matically generated diverse datasets, such as Dolphin-2.9.1-Llama-3-8B, demonstrate a markedly
superior average preference distribution accuracy (Figure 13). Additionally, these models exhibit
an enhanced capability to preserve cross-cultural value variation when compared to those aligned
through Reinforcement Learning from Human Feedback (RLHF). This observation suggests that the
diversity of the data, rather than the density of human preference annotations, is the primary factor
influencing distributional fidelity.
Reinforcement Learning from Human Feedback (RLHF), specifically through the application of Su-
pervised Fine-Tuning (SFT) combined with RLHF pipelines (such as Llama-3-8B-Instruct), results
in significant reductions in systemic inconsistencies, as evidenced by metrics such as Frequency of
Failure (FF) and Conflict in Value Expression (CV). Furthermore, this approach demonstrates supe-
rior internal coherence across evaluation contexts in both the United States and China. The findings
suggest that iterative human feedback tends to optimize for consistency rather than distributional
coverage.
This divergence suggests that optimal alignment strategies may require hybrid approaches: FFT
for distributional coverage combined with RLHF for consistency refinement.
4.3.3
MULTILINGUAL TRAINING AND REGION-SPECIFIC OPTIMIZATION: CHINA
DEVELOPMENT PARADIGM
Impact of multilingual data integration
China-origin model development frequently incorpo-
rates substantial multilingual training data, providing a natural experiment in cross-cultural align-
ment:
• Context-specific performance gains: Enhanced multilingual data percentages (as in Llama-
3-Chinese-8B-Instruct) yield targeted improvements in Chinese cultural context perfor-
mance and reduced insensitivity in Chinese evaluations
• Tradeoff considerations: Improvements remain context-specific, with limited transfer to
U.S. cultural alignment, suggesting that multilingual data integration primarily benefits
represented language-culture pairs
15

--- Page 16 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
Model
GLM-4-air
GPT-4o
Doubao-1.5-pro
Avg. Metrics
ACC (%)
1-JSD ↑
EMD ↓
κ ↑
ACC (%)
1-JSD ↑
EMD ↓
κ ↑
ACC (%)
1-JSD ↑
EMD ↓
κ ↑
Demo.+Ideo.
25.49
0.3539
0.0741
0.02
32.30
0.4075
0.0755
0.09
30.75
0.4563
0.0685
0.02
Demo.+Ideo.+Opinion
25.06
0.4313 (0.6)
0.0669
0.11
33.07
0.4069
0.0739
0.09
31.45
0.4723
0.0703
0.08
Zhao et al. (2024)
26.98
0.3814
0.0452
0.05
36.96
0.4654
0.0610
0.12
24.23
0.3584
0.0364
0.05
MARK (Ours)
33.69
0.4348
0.0887
0.15
38.11
0.4879
0.0826
0.15
46.98
0.5195
0.0561
0.09
Table 3: MARK simulation performance on U.S. social-survey data, evaluated under both global-
distribution and sampled-distribution settings. ‘Avg.’ denotes the overall mean metric values, (value)
denotes the p-value of results between baseline and MARK larger than 0.05. MARK shows improve-
ments on sampled distributions by achieving the highest simulation accuracy while maintaining
low divergences, with most improvements being statistically significant. It also shows generaliza-
tion to global distributions with unseen demographics. Adapted from Liu et al. (2025b).
Base model foundations and alignment efficacy
Analysis of alignment intervention efficacy re-
veals the critical role of pretrained base models:
• Sequential alignment on base models: Specialized techniques applied to base models
yield substantially greater improvements than comparable interventions on instruction-
tuned variants
• Bias profiles across development stages: Base models consistently exhibit reduced de-
mographic bias compared to their instruction-tuned successors, suggesting that alignment
processes (both SFT and RLHF) may inadvertently concentrate preference distributions
while pursuing coherence
This finding has significant implications for alignment strategy sequencing: optimal workflows
may involve comprehensive distributional alignment at the base model stage, followed by targeted
consistency refinement through instruction tuning.
4.3.4
ADVANCED MULTI-STAGE REASONING APPROACHES
Recent innovations demonstrate that multi-stage personality-driven cognitive reasoning frameworks
can enhance cultural value survey simulation accuracy. MARK (Multi-stAge Reasoning frame-
worK), inspired by MBTI personality type dynamics, outperforms existing baselines by 10% ac-
curacy and reduces divergence between model predictions and human preferences. This suggests
that incorporating psychological frameworks and multi-stage reasoning can improve cross-cultural
alignment beyond traditional demographic-based approaches, representing a promising direction for
both China and Western development paradigms.
4.4
OVERVIEW: CONVERGENT CHALLENGES AND DIVERGENT SOLUTIONS IN
CHINA-WESTERN LLM DEVELOPMENT
The cross-cultural audit reveals a complex landscape of convergent fundamental challenges and
divergent methodological responses across China and Western LLM development ecosystems.
Universal challenges
As summarized in Figure 14, both regional contexts demonstrate: (1)
fundamental instability in value systems despite surface-level consistency; (2) systematic under-
representation of younger demographics; (3) non-linear relationships between model scale and cul-
tural alignment quality; and (4) inherent tradeoffs between distributional fidelity and internal con-
sistency.
Regional pathway divergence
China-origin development increasingly emphasizes multilingual
data integration and region-specific optimization, yielding models with strong in-context perfor-
mance but limited cross-cultural transfer. Western development demonstrates greater architectural
experimentation (e.g., MoE configurations, Mistral innovations) but exhibits persistent U.S.-centric
biases. Neither pathway has yet achieved robust, generalizable cross-cultural alignment.
Methodological implications
The findings suggest that next-generation alignment strategies must
transcend current regional paradigms, integrating: (1) diverse data coverage (FFT strengths) with
16

--- Page 17 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
Early Models (e.g.,
GPT-3.5, LLaMA-2)
High Instability in
Responses
Heuristic-Driven
Choices
U.S.-Centric Biases
Dominant
Mid-Stage Models
(e.g., Qwen2,
Claude-3)
Persistent
Demographic
Under-Representation
(e.g., Younger
Groups)
Sensitivity to
Prompts &
Languages
Deontological
Rigidity Emerges
Advanced Models
(e.g., GPT-4o,
DeepSeek)
Non-Linear
Scale-Alignment
(Larger ≠ Better)
Value System
Volatility
Inability for
Autonomous Moral
Navigation
Ongoing Issues
Need for Human
Oversight
Cross-Cultural
Generalization
Failures
Systematic Biases in
Simulations
Universal Challenges in LLM Value Alignment (Pre-2025 Evolution)
Figure 14: Summary of Universal Challenges: a timeline summarizing common challenges across
China-West LLMs, evolving from early to advanced models.
consistency mechanisms (RLHF strengths); (2) base model distributional alignment preceding in-
struction tuning; (3) explicit demographic representation objectives alongside cultural value targets;
(4) multi-stage personality-driven reasoning approaches; and (5) systematic audit frameworks that
evaluate both within-culture accuracy and cross-cultural preservation.
These results provide an empirical foundation for developing harmonized international AI gover-
nance frameworks that acknowledge regional innovation strengths while addressing shared funda-
mental challenges in responsible AI development.
5
TECHNOLOGY FOR GOOD: SOCIAL IMPACT, LLM GOVERNANCE, AND
POLICY TRANSLATION
This section articulates the strategic applications of the computational auditing platform, empha-
sizing governance protocols, policy implications, and institutional frameworks derived from the
comparative analysis of China-Western LLM value alignment. As presented in Figure 15, we posi-
tion these findings within broader debates on responsible AI governance, cross-cultural technology
policy, and the democratization of computational social science methods.
5.1
COMPUTATIONAL INFRASTRUCTURE FOR RESPONSIBLE AI GOVERNANCE: PUBLIC
POLICY AND ACADEMIC APPLICATIONS
The Multi-Layered Auditing Platform represents a methodological contribution to the emerging field
of algorithmic governance, enabling the transition from diagnostic evaluation to actionable policy
interventions with measurable social impact.
5.1.1
CASE STUDY 1: DELIBERATIVE DEMOCRACY THROUGH COMPUTATIONAL
SIMULATION—POLICY CONSULTATION AT SCALE
Theoretical Framework and Policy Challenge
Democratic governance increasingly confronts
the challenge of incorporating diverse public perspectives into policy formation under time and
resource constraints. Traditional deliberative mechanisms—public consultations, citizen assemblies,
and survey research—face inherent limitations in scale, cost, and representational fidelity (Fishkin,
17

--- Page 18 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
Key Findings from Cross-
Cultural Audit
Universal Challenges
Heuristics > Principles
Younger Demographics 
Ignored
Larger Models Not Always 
Better Aligned
Require Human Oversight
Regional Divergences
e.g., Qwen, DeepSeek
Multilingual Integration, 
Context-Specific 
Optimization, Stronger 
Collectivist Orientations
e.g., GPT-4o, Claude
Architectural 
Experimentation, 
Persistent U.S.-Centric 
Biases, Greater 
Deontological Rigidity
No Robust Generalization 
Across Paradigms
Alignment Efficacy Insights
Mistral-Series > LLaMA-3-
Series in Cross-Cultural 
Tasks
Full-Parameter Fine-Tuning 
> RLHF for Preserving 
Cultural Variation
Need for Multi-Layered 
Auditing to Mitigate Biases
Figure 15: Summary of Key Empirical Findings: This mindmap captures the core findings from
the cross-cultural audit, emphasizing universal challenges and divergences as foundations for gov-
ernance discussions.
2011; Moore, 2014). Our integration of the Diversity-Enhanced Framework (DEF) with First-
Token Fine-Tuning offers a novel computational approach to this democratic deficit.
Methodological Innovation and Governance Application
This framework enables rapid, high-
fidelity simulation of public attitudes and value trade-offs regarding proposed policies (e.g., energy
transition measures, public health interventions, social welfare reforms) prior to legislative imple-
mentation. By achieving high distributional fidelity, these LLM-based simulations provide policy-
makers with cost-effective, population-representative insights into how demographically diverse
populations—such as those in the United States versus China—might respond to policy proposals
under consideration.
The framework advances beyond conventional survey prediction by specializing LLMs for distri-
butional simulation rather than individual-level forecasting. Through a fine-tuning methodology
leveraging first-token probability optimization, we minimize divergence between predicted and em-
pirically observed country-level response distributions. This technical innovation yields substantial
improvements in predictive accuracy over zero-shot baselines (e.g., 34.3% increase for Llama3-
8B-Instruct on aggregate measures), thereby enhancing the reliability of computational methods in
social science research and evidence-based policymaking.
Policy Implications and Democratic Theory
This application contributes to ongoing debates
regarding the role of computational methods in deliberative democracy (Mercier & Landemore,
2012). While not replacing authentic public participation, these simulations can inform policy de-
sign phases, identify potential areas of public concern, and enable rapid iteration of policy proposals
before resource-intensive implementation. This represents a form of ”computational deliberation”
that complements rather than substitutes traditional democratic processes.
5.2
CASE STUDY 2: ALGORITHMIC ACCOUNTABILITY THROUGH MECHANISTIC
INTERPRETABILITY—AUDITING AI DECISION-MAKING SYSTEMS
Governance Challenge and Accountability Framework
As large language models increasingly
inform high-stakes decisions across healthcare, criminal justice, and financial services, the opacity of
their decision-making processes presents fundamental challenges to democratic accountability and
procedural justice (Citron & Pasquale, 2014; Selbst et al., 2019). The Multi-stAge Reasoning frame-
worK (MARK) addresses this accountability deficit by providing mechanistic, theory-grounded ex-
planations for simulated value judgments.
Methodological Contribution to AI Transparency
MARK operationalizes computational inter-
pretability through cognitive modeling informed by personality psychology (Myers-Briggs Type
Indicator framework) and stress response theory. This approach yields personality-driven explana-
18

--- Page 19 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
tions for value-laden choices, achieving superior accuracy compared to baseline simulation methods
while demonstrating robust generalization to Chinese cultural contexts. Critically, the framework
enables domain experts to scrutinize and validate the reasoning trajectories underlying LLM
outputs, thereby operationalizing the principle of ”algorithmic due process.”
Institutional and Regulatory Implications
This work contributes to the emerging regulatory
landscape surrounding AI explainability requirements, such as the EU AI Act (Act, 2024) and
the proposed U.S. Algorithmic Accountability Act. By providing granular, theory-informed ex-
planations, MARK offers a potential compliance pathway for organizations subject to explainability
mandates while advancing scholarly understanding of how cultural context shapes algorithmic rea-
soning. The cross-cultural validation is particularly significant given the comparative paucity of AI
governance research outside Western contexts.
5.3
CASE STUDY 3: NORMATIVE STABILITY IN SEQUENTIAL DECISION-MAKING—A
SAFETY PROTOCOL FOR VALUE ALIGNMENT
Risk Assessment Framework
The deployment of LLMs in autonomous decision-making systems
raises fundamental questions about moral consistency and normative reliability over extended inter-
action sequences. The Ethical Dilemma Corpus provides an empirical foundation for assessing
this previously under-examined risk vector in AI safety research.
Key Empirical Findings and Theoretical Implications
Our sequential stability analysis reveals
that LLMs exhibit non-transitive and temporally shifting moral preferences across multi-stage
ethical scenarios. Rather than demonstrating stable normative principles analogous to human moral
reasoning (Kohlberg, 1981; Haidt, 2013), models rely on context-dependent heuristics and sta-
tistical pattern matching. This instability manifests across both Chinese (DeepSeek) and West-
ern (Llama-series) models, suggesting a fundamental architectural limitation rather than a culture-
specific training artifact.
Regulatory Guidance and Safety Protocols
These findings yield critical safety guidance for
AI governance: LLMs should not be authorized for autonomous, sequential ethical decision-
making in high-stakes domains absent robust human oversight mechanisms. This evidence-based
constraint informs emerging regulatory frameworks, including sector-specific guidance for health-
care AI, autonomous vehicles, and automated content moderation systems. The findings support a
”human-in-the-loop” governance model rather than fully autonomous algorithmic decision-making
for value-laden judgments.
5.4
STRATEGIC FRAMEWORK FOR LLM GOVERNANCE
The comparative audit generates actionable strategic recommendations for institutional LLM gover-
nance, informing model procurement decisions, bias mitigation protocols, and accountability mech-
anisms—particularly relevant for organizations operating across diverse cultural contexts (illustrated
in Figure 16).
5.4.1
STRATEGIC MODEL SELECTION: EMPIRICALLY-GROUNDED PROCUREMENT
DECISIONS
Evidence-Based Architecture Assessment
Institutional governance of AI systems requires mov-
ing beyond vendor claims to empirically validated performance metrics. Our cross-cultural value
alignment audit establishes that Mistral-series models demonstrate statistically significant superior
performance relative to Llama-3-series architectures across both U.S. and Chinese cultural contexts
(p ¡ 0.01). This finding provides quantitative evidence to inform risk-adjusted model selection for
organizations deploying LLMs in culturally diverse markets or multilingual contexts.
Implications for Technology Procurement Policy
This comparative finding advances procure-
ment policy by establishing culture-agnostic performance benchmarks. Organizations can leverage
these empirical comparisons to justify model selection decisions, establish baseline performance
requirements in vendor contracts, and implement evidence-based standards for model evaluation.
19

--- Page 20 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
Full-Parameter Fine-Tuning
Avoid RLHF Alone
Start: Identify Governance 
Need
(e.g., High-Stakes 
Deployment)
Audit with Multi-Layered 
Platform
(Ethical Corpus, DEF, First-
Token, MARK)
Diagnose Issues
(Instability, Biases, 
Misalignment)
Select Alignment 
Technique?
Apply on Diverse Datasets
(Preserve Cultural 
Variation)
Supplement with Human 
Feedback Loops
Model Selection
(Prioritize Mistral over 
LLaMA for Cross-Cultural)
Bias Mitigation
(Quantify with KL-
Divergence, Adjust for 
Demographics)
Policy Consultation
(Integrate Human 
Oversight, Protocols for 
Ethical Dilemmas)
End: Deploy with 
Sustained Monitoring
(Ensure No Autonomous 
Moral Decisions)
Figure 16: Actionable Protocols for AI Governance Suggestions: This flowchart outlines practical
suggestions for model selection, bias mitigation, and policy consultation, as derived from the paper’s
emphasis on evidence-based governance.
20

--- Page 21 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
This represents a shift from opaque, proprietary benchmarks to transparent, replicable evaluation
methodologies.
5.4.2
GOVERNANCE ARCHITECTURE: TRANSPARENCY-ENABLING ALIGNMENT
TECHNIQUES
Comparative Evaluation of Alignment Methods
Effective AI governance requires not only
aligned outputs but also interpretable alignment processes that enable institutional oversight. Our re-
search demonstrates that explicit value constraint specification substantially outperforms implicit
few-shot learning for guiding normative judgments. Explicit prompting strategies yield superior
transparency because they articulate constraints directly, whereas few-shot examples require infer-
ential leaps that obscure the operative value framework.
Performance Benchmarks and Best Practices
Leading models employing explicit preference
alignment achieve substantial performance gains, with Claude-3.5-Sonnet reaching 83.1% accuracy
and Llama-3-70B achieving 77.8%—both substantially exceeding their baseline zero-shot perfor-
mance. These findings support governance protocols that mandate explicit value specification in
high-stakes applications, enabling clearer accountability chains and more straightforward auditing
processes.
5.4.3
ACCOUNTABILITY MECHANISMS: QUANTIFYING AND RECTIFYING DEMOGRAPHIC
BIAS
Empirical Bias Characterization
Algorithmic accountability requires moving beyond abstract
fairness principles to concrete, measurable bias profiles.
Leveraging the Diversity-Enhanced
Framework’s demographic preference mapping, we identify systematic cross-cultural patterns
in representational bias:
1. U.S. context: Optimal alignment configurations systematically favor male demographic
profiles aged 30-49 or over 50, indicating potential underrepresentation of female and
younger perspectives
2. Chinese context: Superior alignment emerges for female personas aged 30-49, suggesting
inverse gender skew relative to Western models
3. Cross-cultural pattern: Both cultural contexts demonstrate inadequate representation of
preferences associated with individuals under age 29, indicating a systematic generational
bias
Targeted Mitigation Strategies
These empirically grounded bias profiles inform differentiated
mitigation strategies. Rather than one-size-fits-all debiasing approaches, organizations should im-
plement culturally-calibrated interventions addressing the specific demographic misalignments
identified in their operational contexts. This represents a shift from generic fairness interventions to
precision bias mitigation informed by rigorous empirical assessment.
5.4.4
TECHNICAL COMPLIANCE PATHWAYS: ENGINEERING SOLUTIONS FOR MEASURABLE
STANDARDS
Our evaluation of alignment techniques yields specific technical recommendations for organizations
seeking to operationalize cultural sensitivity and fairness standards (timelined in Figure 17):
• First-Token Alignment: This specialized fine-tuning approach demonstrates substantial
accuracy improvements and validates the technical feasibility of correcting cross-cultural
distributional misalignments through targeted architectural interventions
• Full-Parameter Fine-Tuning (FFT) vs. RLHF: Systematic comparison reveals that FFT
using automatically enhanced training data achieves superior performance in preserving
cultural variation and improving average preference distributions relative to Reinforcement
Learning from Human Feedback on human-annotated data
• Multilingual Data Integration: Increased multilingual training data—a characteristic fea-
ture of Chinese model development approaches—demonstrably improves performance in
21

--- Page 22 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
Short-Term
(2025-2026)
Implement
Multi-Layered
Auditing in
Deployments
Prioritize
Full-Parameter
Fine-Tuning
Mandate Human
Oversight Protocols
Mid-Term
(2026-2028)
Develop
Cross-Cultural
Benchmarks (Expand
WVS Integration)
Mitigate
Demographic Biases
(e.g., Younger
Groups)
Benchmark New
Architectures
(Beyond
Mistral/LLaMA)
Long-Term (2028+)
Achieve Robust
Generalization
Policy Frameworks
for Global AI
(Evidence-Based
Consultation)
Research Non-Linear
Scaling Solutions
"Suggested Roadmap for AI Governance (Post-2025)"
Figure 17: Future Directions and Suggestions for Responsible AI: This timeline projects sug-
gestions for advancing AI governance based on the findings, focusing on short-term actions and
long-term research needs.
culture-specific alignment tasks and reduces cultural insensitivity, offering potential lessons
for Western model development
These technical pathways enable organizations to translate abstract fairness commitments into mea-
surable engineering interventions. By establishing quantitative benchmarks for cultural alignment
and demonstrating effective mitigation techniques, this research provides actionable compliance
pathways for organizations navigating emerging AI governance regulations.
6
DISCUSSION
This study deployed a Multi-Layered Auditing Platform for Responsible AI that synthesizes
computational methodologies to systematically evaluate Large Language Model (LLM) behavior
across cultural and temporal dimensions.
The platform integrates four complementary analyti-
cal instruments: the Ethical Dilemma Corpus, which interrogates temporal stability and detects
reliance on unstable heuristics through progressively intensifying ethical conflicts; the Diversity-
Enhanced Framework (DEF), which quantifies representational fidelity by benchmarking model
outputs against empirical human survey distributions in U.S. and Chinese contexts; First-Token
Probability Alignment, which enhances distributional simulation accuracy through refined cal-
ibration against ground-truth human preferences; and the Multi-stAge Reasoning frameworK
(MARK), which elucidates mechanistic, personality-driven explanations to strengthen account-
ability and interpretability. This comprehensive architecture enables dynamic, multi-dimensional
scrutiny of China-Western LLM ecosystems, addressing critical gaps in cross-cultural AI gover-
nance research.
6.1
EMPIRICAL FINDINGS FROM CROSS-CULTURAL AUDITING
Answering RQ1: Temporal Stability, Value Rigidity, and Sequential Moral Reasoning, the compar-
ative analysis highlights that both Chinese and Western LLMs demonstrate pronounced fixed value
hierarchies, consistently prioritizing Truth over Loyalty and Community over Individual welfare.
Larger models tend to adopt deontological frameworks that maintain ethical commitments despite
adverse outcomes. However, the Ethical Dilemma Corpus reveals that LLMs rely on heuristic-
22

--- Page 23 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
driven, context-dependent statistical imitation rather than principled reasoning, limiting their
ability for autonomous ethical decision-making. While advanced models like Claude-3.5-Sonnet
and Qwen2-72B show improved task comprehension, they exhibit varied stability profiles across
dilemma steps. The moral foundation of Care remains consistently stable, while Authority prior-
itization becomes less stable. Importantly, moral volatility is not confined to any region, with both
DeepSeek and Llama showing instability, whereas GLM-4-Air and Claude demonstrate stable value
maintenance, suggesting that architectural choices are more crucial than geographic origin in ethical
consistency.
For RQ2: Cultural Fidelity, Systematic Bias, and Architectural Performance Differentials, a quan-
titative assessment of LLM-human preference alignment reveals significant performance disparities
between U.S. and Chinese cultural contexts, with Mistral-series models outperforming the others
in value alignment. Preference bias analysis uncovers demographic misalignment: U.S. context
favors males aged 30-49 or 50+, while the Chinese context skews towards females aged 30-49.
Notably, both cultures show a critical under-representation of preferences from individuals under
29, highlighting a generational bias in current LLMs.
To resolve RQ3: Developmental Trajectories, Alignment Innovation, and Cross-Regional Strat-
egy Divergence, a longitudinal analysis of LLM development shows that model evolution and cul-
tural alignment efficacy have complex, non-linear relationships. Although generational advance-
ments reduce insensitivity failures, increasing model scale does not guarantee better align-
ment quality or cultural representation, challenging assumptions about parameter count as a
key ethical performance factor. Specialized First-Token Alignment methods provide significant
accuracy improvements over zero-shot techniques.
Additionally, Full-Parameter Fine-Tuning
(FFT) on enhanced datasets generally outperforms Reinforcement Learning from Human
Feedback (RLHF) trained on human-analyzed data in maintaining preference distributions and
cultural variation. A notable divergence exists between China and the West, with China’s approach
of increasing multilingual training data (e.g., Llama-3-Chinese-8B-Instruct) enhancing culture-
specific alignment and reducing insensitivity in Chinese contexts, impacting global AI strategies
balancing linguistic diversity and cultural fidelity.
6.2
STRATEGIC IMPLICATIONS FOR RESPONSIBLE AI GOVERNANCE
Policy Validation and Transparency Mechanisms
The empirical platform developed through
DEF and First-Token Fine-Tuning provides cost-effective tools for regulatory bodies to assess pop-
ulation responses to policies across various cultures (U.S. vs. China). This approach enhances the
speed of social science research and supports evidence-based governance. The MARK Framework
offers mechanistic, personality-driven insights into value choices, allowing experts to validate AI
reasoning and ensuring necessary human oversight in AI-driven decisions. Given that current LLMs
rely on unstable heuristics rather than consistent ethical principles, a foundational safety protocol
is essential. LLMs should not be allowed to make autonomous ethical decisions in high-stakes
situations and require ongoing human supervision, particularly in sectors like healthcare, criminal
justice, and public policy where decisions have serious social implications.
Model Selection and Bias Mitigation
Evidence-based governance requires prioritizing empiri-
cal alignment data, particularly highlighting the superior performance of Mistral-series archi-
tectures over Llama-3 in cross-cultural contexts.
Accountability frameworks should mandate
explicit alignment techniques that enforce explicit ethical policies or value constraints rather
than relying on implicit learning. Targeted bias mitigation must address demographic skews, such
as U.S. male/older-age bias versus Chinese female/middle-aged bias, while correcting under-
representation of the under-29 age group. Specialized fine-tuning methodologies like First-Token
Alignment offer efficient solutions for achieving fairness and cultural sensitivity, indicating a need
to shift resources from RLHF to FFT in alignment research.
7
CONCLUSION
This study demonstrates that responsible AI development in an interconnected world requires mov-
ing beyond single-culture optimization toward genuine cross-cultural competence. The proposed
computational auditing platform: Multi- Layered Auditing Platform for Responsible AI, pro-
23

--- Page 24 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
vides methodological foundations for this transition, enabling systematic evaluation, transparent
accountability, and evidence-based governance across diverse cultural contexts.
As LLMs shape global communication and public discourse, aligning them with diverse human val-
ues is essential for equitable technological development. Our findings establish that this alignment
cannot be assumed from model scale, assumed from training data volume, or inherited from single-
culture optimization. It must be systematically engineered, rigorously audited, and continuously
refined through transparent, reproducible methodologies that acknowledge both universal principles
and cultural particularity.
The comparative China-Western analysis reveals that technological innovation serving the global
good requires integrating diverse epistemological approaches, respecting cultural specificity while
pursuing shared ethical standards, and maintaining a humble recognition of current limitations
alongside an ambitious pursuit of improvement. By establishing empirical foundations for evidence-
based cross-cultural AI governance, this research contributes to building artificial intelligence sys-
tems that genuinely serve humanity in its full diversity—systems that enhance rather than erase cul-
tural richness, that amplify rather than silence marginalized voices, and that operate transparently
under sustained human guidance rather than claiming autonomous moral authority.
The path toward culturally competent, socially beneficial AI systems remains long and technically
demanding. However, through systematic evaluation frameworks, transparent accountability mech-
anisms, and international collaborative governance, we can work toward artificial intelligence that
serves not merely dominant cultural paradigms but the full spectrum of human values, experiences,
and aspirations across our diverse global community. This study provides both the methodological
tools and empirical insights to guide that essential journey.
LIMITATIONS
Conceptual Framework Limitations
The foundational moral frameworks employed (Kidder’s
Ethical Dilemmas, Moral Foundations Theory, Schwartz’s Theory of Basic Values) inherently privi-
lege Western-centric moral constructs, potentially underrepresenting collectivist ethics such as Con-
fucian ren or Ubuntu ubuntu that are crucial in non-Western contexts. Future research must system-
atically integrate culture-specific ethical dimensions through sustained collaboration with regional
cultural experts and philosophers representing diverse philosophical traditions.
Methodological Design Constraints
LLMs exhibit pronounced sensitivity to prompt presenta-
tion, and the Ethical Dilemma Corpus framework’s linearly intensifying scenarios cannot model
non-linear escalations (e.g., de-escalation through negotiation), while MARK’s reliance on LLM-
generated personality predictions and the empirical limitations of MBTI constrain generalizability.
Future methodologies should incorporate validated psychological instruments, explore diverse sce-
nario progression patterns, and develop comprehensive prompt variation testing protocols.
Empirical Scope Limitations
The focus on U.S. and Chinese cultural contexts using English and
Chinese prompts does not capture broader global cultural diversity, while First-Token Alignment
models remain highly specialized for survey response prediction rather than general-purpose ap-
plications. Expanding research to encompass diverse cultural contexts, languages, and real-world
deployment scenarios is essential for establishing cross-cultural generalizability.
Governance Transparency Barriers
The lack of transparency regarding training data sources in
commercial and open LLMs (e.g., Mistral, Llama-3) represents a significant constraint on auditabil-
ity, particularly in assessing the impact of multilingual data integration—a key feature of Chinese
AI innovation—on model behavior. Future governance frameworks must mandate comprehensive
training data disclosure and establish standardized transparency protocols for cross-cultural AI au-
diting.
24

--- Page 25 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
ACKNOWLEDGMENTS
We thank the anonymous reviewers for their valuable feedback and constructive comments that
helped improve this work. We are grateful to Yuchu Tian and Caicai Guo for their insightful discus-
sions and suggestions.
This work was supported by the National Key Research and Development Program of China under
Grants 2022YFC3300801, the Research Project of China Publishing Promotion Association under
Grants 2025ZBCH-JYYB17, and the Natural Science Foundation of Hubei Province (CN) under
Grant No. 2025AFB078.
REFERENCES
EU Artificial Intelligence Act. The eu artificial intelligence act. European Union, 2024.
Utkarsh Agarwal, Kumar Tanmay, Aditi Khandelwal, and Monojit Choudhury. Ethical reasoning
and moral value alignment of llms depend on the language we prompt them in. In Nicoletta Calzo-
lari, Min-Yen Kan, V´eronique Hoste, Alessandro Lenci, Sakriani Sakti, and Nianwen Xue (eds.),
Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language
Resources and Evaluation, LREC/COLING 2024, 20-25 May, 2024, Torino, Italy, pp. 6330–6340.
ELRA and ICCL, 2024a. URL https://aclanthology.org/2024.lrec-main.560.
Utkarsh Agarwal, Kumar Tanmay, Aditi Khandelwal, and Monojit Choudhury. Ethical reasoning
and moral value alignment of LLMs depend on the language we prompt them in. In Proceedings
of the 2024 Joint International Conference on Computational Linguistics, Language Resources
and Evaluation (LREC-COLING 2024), pp. 6330–6340, Torino, Italia, May 2024b. ELRA and
ICCL. URL https://aclanthology.org/2024.lrec-main.560/.
Lisa P. Argyle, Ethan C. Busby, Nancy Fulda, Joshua Gubler, Christopher Michael Rytting, and
David Wingate. Out of one, many: Using language models to simulate human samples. CoRR,
abs/2209.06899, 2022. doi: 10.48550/ARXIV.2209.06899. URL https://doi.org/10.
48550/arXiv.2209.06899.
Lisa P. Argyle, Ethan C. Busby, Nancy Fulda, Joshua R. Gubler, Christopher Rytting, and David
Wingate. Out of one, many: Using language models to simulate human samples. Political Anal-
ysis, 31(3):337–351, 2023. doi: 10.1017/pan.2023.2.
Christopher A. Bail.
Can generative ai improve social science?
Proceedings of the National
Academy of Sciences, 121(21):e2314021121, 2024.
doi: 10.1073/pnas.2314021121.
URL
https://www.pnas.org/doi/abs/10.1073/pnas.2314021121.
Yong Cao, Li Zhou, Seolhwa Lee, Laura Cabello, Min Chen, and Daniel Hershcovich.
As-
sessing cross-cultural alignment between ChatGPT and human societies: An empirical study.
In Proceedings of the First Workshop on Cross-Cultural Considerations in NLP (C3NLP),
pp. 53–67, Dubrovnik, Croatia, May 2023. Association for Computational Linguistics.
doi:
10.18653/v1/2023.c3nlp-1.7. URL https://aclanthology.org/2023.c3nlp-1.7/.
Yong Cao, Haijiang Liu, Arnav Arora, Isabelle Augenstein, Paul R¨ottger, and Daniel Hershcovich.
Specializing large language models to simulate survey response distributions for global popu-
lations. In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the
Association for Computational Linguistics: Human Language Technologies (Volume 1: Long
Papers), pp. 3141–3154, Albuquerque, New Mexico, April 2025. Association for Computa-
tional Linguistics.
ISBN 979-8-89176-189-6.
doi: 10.18653/v1/2025.naacl-long.162.
URL
https://aclanthology.org/2025.naacl-long.162/.
Paul Christiano, Jan Leike, Tom B. Brown, Miljan Martic, Shane Legg, and Dario Amodei. Deep
reinforcement learning from human preferences, 2023. URL https://arxiv.org/abs/
1706.03741.
Danielle Keats Citron and Frank A. Pasquale.
The scored society: Due process for automated
predictions. Washington Law Review, 89:1, 2014. URL https://api.semanticscholar.
org/CorpusID:61799887.
25

--- Page 26 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
Sunipa Dev, Emily Sheng, Jieyu Zhao, Aubrie Amstutz, Jiao Sun, Yu Hou, Mattie Sanseverino, Jiin
Kim, Akihiro Nishi, Nanyun Peng, and Kai-Wei Chang. On measures of biases and harms in NLP.
In Findings of the Association for Computational Linguistics: AACL-IJCNLP 2022, pp. 246–267,
Online only, November 2022. Association for Computational Linguistics. doi: 10.18653/v1/2022.
findings-aacl.24. URL https://aclanthology.org/2022.findings-aacl.24/.
Rohit K. Dubey, Damian Dailisan, and Sachit Mahajan.
Addressing moral uncertainty using
large language models for ethical decision-making, 2025. URL https://arxiv.org/abs/
2503.05724.
Esin Durmus, Karina Nguyen, Thomas I. Liao, Nicholas Schiefer, Amanda Askell, Anton Bakhtin,
Carol Chen, Zac Hatfield-Dodds, Danny Hernandez, Nicholas Joseph, Liane Lovitt, Sam McCan-
dlish, Orowa Sikder, Alex Tamkin, Janel Thamkul, Jared Kaplan, Jack Clark, and Deep Ganguli.
Towards measuring the representation of subjective global opinions in language models, 2024.
URL https://arxiv.org/abs/2306.16388.
Denis Emelin, Ronan Le Bras, Jena D. Hwang, Maxwell Forbes, and Yejin Choi. Moral stories:
Situated reasoning about norms, intents, actions, and their consequences. In Proceedings of the
2021 Conference on Empirical Methods in Natural Language Processing, pp. 698–718, Online
and Punta Cana, Dominican Republic, November 2021. Association for Computational Linguis-
tics. doi: 10.18653/v1/2021.emnlp-main.54. URL https://aclanthology.org/2021.
emnlp-main.54/.
J.S. Fishkin.
When the People Speak: Deliberative Democracy and Public Consultation.
Ox-
ford University Press, 2011. ISBN 9780199604432. URL https://books.google.com/
books?id=iNsUDAAAQBAJ.
Maxwell Forbes, Jena D. Hwang, Vered Shwartz, Maarten Sap, and Yejin Choi.
Social chem-
istry 101: Learning to reason about social and moral norms. In Bonnie Webber, Trevor Cohn,
Yulan He, and Yang Liu (eds.), Proceedings of the 2020 Conference on Empirical Methods
in Natural Language Processing (EMNLP), pp. 653–670, Online, November 2020. Associa-
tion for Computational Linguistics.
doi: 10.18653/v1/2020.emnlp-main.48.
URL https:
//aclanthology.org/2020.emnlp-main.48/.
Dorit Hadar-Shoval, Kfir Asraf, Yonathan Mizrachi, Yuval Haber, and Zohar Elyoseph. Assessing
the alignment of large language models with human values for mental health integration: Cross-
sectional study using schwartz’s theory of basic values. JMIR Mental Health, 11, 2024. ISSN
2368-7959.
doi: https://doi.org/10.2196/55988.
URL https://www.sciencedirect.
com/science/article/pii/S2368795924000350.
Thilo Hagendorff.
The ethics of AI ethics: An evaluation of guidelines.
Minds Mach., 30(1):
99–120, 2020. doi: 10.1007/S11023-020-09517-8. URL https://doi.org/10.1007/
s11023-020-09517-8.
J. Haidt. The Righteous Mind: Why Good People Are Divided by Politics and Religion. Knopf Dou-
bleday Publishing Group, 2013. ISBN 9780307455772. URL https://books.google.
com/books?id=U21BxGfm3RUC.
Dan Hendrycks, Collin Burns, Steven Basart, Andrew Critch, Jerry Li, Dawn Song, and Jacob
Steinhardt. Aligning ai with shared human values. Proceedings of the International Conference
on Learning Representations (ICLR), 2021.
Liwei Jiang, Jena D. Hwang, Chandra Bhagavatula, Ronan Le Bras, Jenny Liang, Jesse Dodge,
Keisuke Sakaguchi, Maxwell Forbes, Jon Borchardt, Saadia Gabriel, Yulia Tsvetkov, Oren Et-
zioni, Maarten Sap, Regina Rini, and Yejin Choi.
Can machines learn morality? the delphi
experiment, 2022. URL https://arxiv.org/abs/2110.07574.
Anna Jobin, Marcello Ienca, and Effy Vayena. The global landscape of AI ethics guidelines. 1(9):
389–399. ISSN 2522-5839. doi: 10.1038/s42256-019-0088-2. URL https://doi.org/
10.1038/s42256-019-0088-2.
26

--- Page 27 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
R.M. Kidder. How Good People Make Tough Choices: Resolving the Dilemmas of Ethical Living.
A Fireside book. Simon & Schuster, 1996. ISBN 9780684818382. URL https://books.
google.com/books?id=1LBIAAAAYAAJ.
Lawrence Kohlberg. The Philosophy of Moral Development: Moral Stages and the Idea of Justice.
San Francisco : Harper & Row, 1981.
Hadas Kotek, Rikker Dockum, and David Sun.
Gender bias and stereotypes in large language
models. In Proceedings of The ACM Collective Intelligence Conference, pp. 12–24. ACM. ISBN
979-8-4007-0113-9. doi: 10.1145/3582269.3615599. URL https://dl.acm.org/doi/
10.1145/3582269.3615599.
Enrico Liscio, Roger Lera-Leri, Filippo Bistaffa, Roel I.J. Dobbe, Catholijn M. Jonker, Maite
Lopez-Sanchez, Juan A. Rodriguez-Aguilar, and Pradeep K. Murukannaiah.
Value inference
in sociotechnical systems. In Proceedings of the 2023 International Conference on Autonomous
Agents and Multiagent Systems, AAMAS ’23, pp. 1774–1780, Richland, SC, 2023. International
Foundation for Autonomous Agents and Multiagent Systems. ISBN 9781450394321.
Haijiang Liu, Yong Cao, Xun Wu, Chen Qiu, Jinguang Gu, Maofu Liu, and Daniel Hershcovich.
Towards realistic evaluation of cultural value alignment in large language models: Diversity
enhancement for survey response simulation. Information Processing & Management, 62(4):
104099, 2025a. ISSN 0306-4573. doi: https://doi.org/10.1016/j.ipm.2025.104099. URL https:
//www.sciencedirect.com/science/article/pii/S030645732500041X.
Haijiang Liu, Qiyuan Li, Chao Gao, Yong Cao, Xiangyu Xu, Xun Wu, Daniel Hershcovich, and
Jinguang Gu. Beyond demographics: Enhancing cultural value survey simulation with multi-stage
personality-driven cognitive reasoning. In Proceedings of the 2025 Conference of the The 2025
Conference on Empirical Methods in Natural Language Processing (Volume 1: Long Papers).
Association for Computational Linguistics, 2025b. URL https://arxiv.org/abs/2508.
17855.
Hugo Mercier and H´el`ene Landemore.
Reasoning is for arguing: Understanding the successes
and failures of deliberation.
33(2):243–258, 2012.
ISSN 0162-895X, 1467-9221.
doi:
10.1111/j.1467-9221.2012.00873.x. URL https://onlinelibrary.wiley.com/doi/
10.1111/j.1467-9221.2012.00873.x.
Brent D. Mittelstadt.
Principles alone cannot guarantee ethical AI.
Nat. Mach. Intell., 1(11):
501–507, 2019. doi: 10.1038/S42256-019-0114-4. URL https://doi.org/10.1038/
s42256-019-0114-4.
Alfred Moore. Democratic reason: Politics, collective intelligence and the rule of the many. 13(2):
e12–e15, 2014. ISSN 1476-9336. doi: 10.1057/cpt.2013.26. URL https://doi.org/10.
1057/cpt.2013.26.
Ravi Narayanan and Adebis Samuel. Ethical challenges and bias in nlp models: A python-based
investigation. 05 2025.
Roberto Navigli, Simone Conia, and Bj¨orn Ross. Biases in large language models: Origins, inven-
tory, and discussion. J. Data and Information Quality, 15(2), June 2023. ISSN 1936-1955. doi:
10.1145/3597307. URL https://doi.org/10.1145/3597307.
Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong
Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kel-
ton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike,
and Ryan Lowe. Training language models to follow instructions with human feedback, 2022.
URL https://arxiv.org/abs/2203.02155.
Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and
Michael S. Bernstein. Generative agents: Interactive simulacra of human behavior. In Proceed-
ings of the 36th Annual ACM Symposium on User Interface Software and Technology, UIST ’23,
New York, NY, USA, 2023. Association for Computing Machinery. ISBN 9798400701320. doi:
10.1145/3586183.3606763. URL https://doi.org/10.1145/3586183.3606763.
27

--- Page 28 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
Shaina Raza, Muskan Garg, Deepak John Reji, Syed Raza Bashir, and Chen Ding.
Nbias:
A natural language processing framework for bias identification in text.
Expert Systems
with Applications, 237:121542, 2024.
ISSN 0957-4174.
doi: https://doi.org/10.1016/j.eswa.
2023.121542.
URL https://www.sciencedirect.com/science/article/pii/
S0957417423020444.
Shibani Santurkar, Esin Durmus, Faisal Ladhak, Cinoo Lee, Percy Liang, and Tatsunori Hashimoto.
Whose opinions do language models reflect?
In Proceedings of the 40th International Con-
ference on Machine Learning, volume 202 of Proceedings of Machine Learning Research,
pp. 29971–30004. PMLR, 23–29 Jul 2023. URL https://proceedings.mlr.press/
v202/santurkar23a.html.
Nino
Scherrer,
Claudia
Shi,
Amir
Feder,
and
David
Blei.
Evaluating
the
moral
beliefs
encoded
in
llms.
In
Advances
in
Neural
Information
Processing
Sys-
tems,
volume
36,
pp.
51778–51809.
Curran
Associates,
Inc.,
2023.
URL
https://proceedings.neurips.cc/paper_files/paper/2023/file/
a2cf225ba392627529efef14dc857e22-Paper-Conference.pdf.
Melanie Sclar, Yejin Choi, Yulia Tsvetkov, and Alane Suhr. Quantifying language models’ sen-
sitivity to spurious features in prompt design or: How I learned to start worrying about prompt
formatting. In The Twelfth International Conference on Learning Representations, ICLR 2024, Vi-
enna, Austria, May 7-11, 2024. OpenReview.net, 2024. URL https://openreview.net/
forum?id=RIu5lyNXjT.
Andrew D. Selbst, Danah Boyd, Sorelle A. Friedler, Suresh Venkatasubramanian, and Janet Vertesi.
Fairness and abstraction in sociotechnical systems. In Proceedings of the Conference on Fairness,
Accountability, and Transparency, FAT* ’19, pp. 59–68, New York, NY, USA, 2019. Associa-
tion for Computing Machinery. ISBN 9781450361255. doi: 10.1145/3287560.3287598. URL
https://doi.org/10.1145/3287560.3287598.
Yan Tao, Olga Viberg, Ryan S Baker, and Ren´e F Kizilcec. Cultural bias and cultural alignment of
large language models. PNAS Nexus, 3(9):pgae346, 09 2024. ISSN 2752-6542. doi: 10.1093/
pnasnexus/pgae346. URL https://doi.org/10.1093/pnasnexus/pgae346.
Amir Taubenfeld, Yaniv Dover, Roi Reichart, and Ariel Goldstein.
Systematic biases in LLM
simulations of debates.
In Proceedings of the 2024 Conference on Empirical Methods in
Natural Language Processing, pp. 251–267, Miami, Florida, USA, November 2024. Associ-
ation for Computational Linguistics.
doi: 10.18653/v1/2024.emnlp-main.16.
URL https:
//aclanthology.org/2024.emnlp-main.16/.
Ya Wu, Qiang Sheng, Danding Wang, Guang Yang, Yifan Sun, Zhengjia Wang, Yuyan Bu, and Juan
Cao. The staircase of ethics: Probing llm value priorities through multi-step induction to complex
moral dilemmas, 2025. URL https://arxiv.org/abs/2505.18154.
Jiaqing Yuan, Pradeep K. Murukannaiah, and Munindar P. Singh. Right vs. right: Can llms make
tough choices? CoRR, abs/2412.19926, 2024. doi: 10.48550/ARXIV.2412.19926. URL https:
//doi.org/10.48550/arXiv.2412.19926.
Wenlong Zhao, Debanjan Mondal, Niket Tandon, Danica Dillion, Kurt Gray, and Yuling Gu. World-
ValuesBench: A large-scale benchmark dataset for multi-cultural value awareness of language
models. In Proceedings of the 2024 Joint International Conference on Computational Linguistics,
Language Resources and Evaluation (LREC-COLING 2024), pp. 17696–17706, Torino, Italia,
May 2024. ELRA and ICCL. URL https://aclanthology.org/2024.lrec-main.
1539/.
A
APPENDIX
A.1
PREFERENCE BIAS REVEALED BY DEF SYSTEM
28

--- Page 29 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
US survey
CN survey
Match
0
20
40
60
80
100
Percentage
US survey
CN survey
Mismatch
(a) Baichuan2-13B-Chat
US survey
CN survey
Match
0
20
40
60
80
100
Percentage
US survey
CN survey
Mismatch
(b) ChatGLM2-6B
US survey
CN survey
Match
0
20
40
60
80
100
Percentage
US survey
CN survey
Mismatch
Sex
Male
Female
(c) WizardLM-13B
US survey
CN survey
Match
0
20
40
60
80
100
Percentage
US survey
CN survey
Mismatch
(d) Mistral-7B-Instruct
US survey
CN survey
Match
0
20
40
60
80
100
Percentage
US survey
CN survey
Mismatch
(e) Dolphin-2.2.1-Mistral-7B
US survey
CN survey
Match
0
20
40
60
80
100
Percentage
US survey
CN survey
Mismatch
Sex
Male
Female
(f) Mixtral-8x7B-Instruct
US survey
CN survey
Match
0
20
40
60
80
100
Percentage
US survey
CN survey
Mismatch
(g) Llama-3-8B
US survey
CN survey
Match
0
20
40
60
80
100
Percentage
US survey
CN survey
Mismatch
(h) Llama-3-8B-Instruct
US survey
CN survey
Match
0
20
40
60
80
100
Percentage
US survey
CN survey
Mismatch
Sex
Male
Female
(i) Dolphin-2.9.1-Llama-3-8B
US survey
CN survey
Match
0
20
40
60
80
100
Percentage
US survey
CN survey
Mismatch
Sex
Male
Female
(j) Llama-3-Chinese-8B-Instruct
US survey
CN survey
Match
0
20
40
60
80
100
Percentage
US survey
CN survey
Mismatch
Sex
Male
Female
(k) Claude-3.5-Sonnet
Figure 18: Mismatch proportions by gender for all candidates. There is a heavy bias on male profiles
in the US survey, and female profiles in the CN survey. But in general, gender bias on the mismatch
profiles in the US survey is less significant than in the CN survey. Adapted from Liu et al. (2025a).
29

--- Page 30 ---

Submitted to Academic Conference ”Technology for Good: Driving Social Impact”
US survey
CN survey
Match
0
20
40
60
80
100
Percentage
US survey
CN survey
Mismatch
(a) Baichuan2-13B-Chat
US survey
CN survey
Match
0
20
40
60
80
100
Percentage
US survey
CN survey
Mismatch
(b) ChatGLM2-6B
US survey
CN survey
0
20
40
60
80
100
Percentage
US survey
CN survey
Age
Up to 29
30 to 49
Over 50
Matching
Mismatch
(c) WizardLM-13B
US survey
CN survey
Match
0
20
40
60
80
100
Percentage
US survey
CN survey
Mismatch
(d) Mistral-7B-Instruct
US survey
CN survey
Match
0
20
40
60
80
100
Percentage
US survey
CN survey
Mismatch
(e) Dolphin-2.2.1-Mistral-7B
US survey
CN survey
Match
0
20
40
60
80
100
Percentage
US survey
CN survey
Mismatch
Age
Up to 29
30 to 49
Over 50
(f) Mixtral-8x7B-Instruct
US survey
CN survey
Match
0
20
40
60
80
100
Percentage
US survey
CN survey
Mismatch
(g) Llama-3-8B
US survey
CN survey
Match
0
20
40
60
80
100
Percentage
US survey
CN survey
Mismatch
(h) Llama-3-8B-Instruct
US survey
CN survey
Match
0
20
40
60
80
100
Percentage
US survey
CN survey
Mismatch
Age
Up to 29
30 to 49
Over 50
(i) Dolphin-2.9.1-Llama-3-8B
US survey
CN survey
Match
0
20
40
60
80
100
Percentage
US survey
CN survey
Mismatch
Age
Up to 29
30 to 49
Over 50
(j) Llama-3-Chinese-8B
US survey
CN survey
Match
0
20
40
60
80
100
Percentage
US survey
CN survey
Mismatch
Age
Up to 29
30 to 49
Over 50
(k) Claude-3.5-Sonnet
Figure 19: Proportion of each age group in mismatch profiles across all candidates, following the
social survey design. Both matching and mismatch profiles show a strong bias toward middle-aged
characters, with under-representing preferences for characters under 29 years old. Adapted from Liu
et al. (2025a).
30
