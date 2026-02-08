---
title: "MoCoP - PDF Extract"
source_pdf: "2025-Jamshidi-MoCoP.pdf"
pages: 8
extracted_at: "2026-01-24T16:38:27.634822"
---

# PDF Extract: MoCoP

**Source PDF:** 2025-Jamshidi-MoCoP.pdf
**Total Pages:** 8

---

## Content

```
--- Page 1 ---

The Moral Consistency Pipeline: Continuous Ethical Evaluation
for Large Language Models
Saeid Jamshidi, Kawser Wazed Nafi, Arghavan Moradi Dakhel, Negar Shahabi†, Foutse Khomh
SWAT Laboratory, Polytechnique Montréal
†Concordia Institute for Information Systems Engineering, Concordia University
Montréal, Quebec, Canada
{saeid.jamshidi,kawser.wazed-nafi,arghavan.moradi-dakhel,foutse.khomh}@polymtl.ca,negar.shahabi@concordia.ca
Abstract
The rapid advancement and adaptability of Large Language Mod-
els (LLMs) highlight the need for moral consistency, the capacity
to maintain ethically coherent reasoning across varied contexts.
Existing alignment frameworks, structured approaches designed to
align model behavior with human ethical and social norms, often
rely on static datasets and post-hoc evaluations, offering limited
insight into how ethical reasoning may evolve across different con-
texts or temporal scales. This study presents the Moral Consistency
Pipeline (MoCoP), a dataset-free, closed-loop framework for con-
tinuously evaluating and interpreting the moral stability of LLMs.
MoCoP combines three supporting layers: (i) lexical integrity analy-
sis, (ii) semantic risk estimation, and (iii) reasoning-based judgment
modeling within a self-sustaining architecture that autonomously
generates, evaluates, and refines ethical scenarios without external
supervision. Our empirical results on GPT-4-Turbo and DeepSeek
suggest that MoCoP effectively captures longitudinal ethical be-
havior, revealing a strong inverse relationship between ethical and
toxicity dimensions (𝑟𝐸𝑇= −0.81, 𝑝< 0.001) and a near-zero associ-
ation with response latency (𝑟𝐸𝐿≈0). These findings demonstrate
that moral coherence and linguistic safety tend to emerge as sta-
ble and interpretable characteristics of model behavior rather than
short-term fluctuations. Furthermore, by reframing ethical evalu-
ation as a dynamic, model-agnostic form of moral introspection,
MoCoP offers a reproducible foundation for scalable, continuous
auditing and advances the study of computational morality in au-
tonomous AI systems.
Keywords
Moral Consistency Pipeline, Ethical AI, Moral Reasoning, Compu-
tational Ethics, Large Language Models
1
Introduction
Artificial intelligence (AI) systems are rapidly being integrated
into decision-making, communication, and learning environments,
where their growing autonomy makes ethical awareness, moral
coherence, and interpretability increasingly essential [5, 17, 21].
As Large Language Models (LLMs) evolve from linguistic tools to
autonomous agents, capable of reasoning and adaptation, they be-
gin to impact human judgment, social perception, and institutional
processes [4, 10, 14]. This transformation underscores the need for
frameworks that examine not only what these models produce, but
also how and why their moral reasoning remains coherent across
different contexts over time [3, 19].
Existing safety-alignment and interpretability frameworks have
made progress in bias detection, toxicity reduction, and fairness
auditing [18, 23]. However, these frameworks generally evaluate
isolated model outputs rather than tracing the evolution of eth-
ical reasoning or shifts in value alignment over time as models
interact with diverse, context-dependent, and dynamically evolv-
ing scenarios [20]. This gap is particularly significant in the con-
text of LLM-based agentic systems, which exhibit adaptive and
context-sensitive behavior, continuously modifying their outputs
in response to prompt structure, user intent, task requirements,
and prior interactions. The absence of such longitudinal consis-
tency raises the risk of moral drift—a phenomenon in which ethical
stances fluctuate and degrade in response to prompt wording, con-
textual pressures, and temporal changes. Inconsistencies of this
kind can threaten the reliability, accountability, and societal trust-
worthiness of contemporary AI systems [6, 24].
Ensuring moral consistency is therefore not only a matter of regu-
latory compliance but also a prerequisite for maintaining logically
stable, interpretable, and trustworthy reasoning within LLM-driven
AI systems over time [2, 27]. While developing autonomous systems
in high-stakes domains such as healthcare, finance, education, and
governance, even a small ethical instability can propagate misinfor-
mation, reinforce cognitive bias, and produce outcomes misaligned
with human values. Despite growing recognition of these chal-
lenges, most current auditing techniques, used as part of broader
safety-alignment frameworks, remain constrained by static bench-
marks and fixed, human-annotated datasets that fail to adapt to the
evolving and context-dependent behavior of LLMs. Consequently,
a key research challenge is to design an adaptive, self-contained
mechanism capable of autonomously evaluating and interpreting
the ethical stability of such models without dependence on external
datasets or post-hoc analysis.
To address this challenge, this work introduces the Moral Consis-
tency Pipeline (MoCoP), a fully autonomous, dataset-free ethical
evaluation framework designed to continuously measure, interpret,
and refine the moral reasoning patterns of LLMs. MoCoP operates
as a closed-loop experimental system that dynamically generates
ethical scenarios, elicits model responses, and performs structured
interpretation using internally defined rules and semantic heuristics.
In contrast to traditional evaluation approaches that depend on pre-
defined test corpora and external annotation, MoCoP autonomously
constructs and analyzes its own ethical scenarios. It integrates three
complementary analytical components—lexical integrity analysis,
semantic risk estimation, and reasoning-based judgment modeling—to
derive unified measures of moral coherence and ethical stability.
Each layer contributes a distinct function: lexical integrity detects
bias and linguistic degradation, semantic risk estimation quantifies
arXiv:2512.03026v1  [cs.CL]  2 Dec 2025

--- Page 2 ---

DSE 2026, April 12–18, 2026, Rio de Janeiro, Brazil
Saeid Jamshidi, Kawser Wazed Nafi, Arghavan Moradi Dakhel, Negar Shahabi†, Foutse Khomh
contextual harm such as toxicity or coercion, and reasoning-based
judgment modeling evaluates the logical soundness and ethical
structure of responses. Through iterative self-analysis and adap-
tive evaluation, MoCoP reframes ethical assessment as a proactive,
self-sustaining process that evolves in tandem with the models it
studies.
The MoCoP framework combines three core subsystems that op-
erationalize these analytical layers: (1) an LLMConnector, which
enables controlled and reproducible interactions between hetero-
geneous models such as GPT-4-Turbo1 and DeepSeek; (2) an Ethi-
calGuardPro engine, which performs lexical scanning, semantic
filtering, and moral interpretation through rule-based and proba-
bilistic reasoning; and (3) a Meta-Analytic Ethics Layer, which
aggregates data from multiple experiments to compute divergence,
coherence, and consensus metrics across large-scale evaluations. To-
gether, these components facilitate autonomous cross-model bench-
marking, dynamic tracking of moral evolution, and quantitative
performance analysis, providing the foundation for longitudinal
ethical introspection in LLMs. The main contributions of this paper
are summarized as follows:
• Autonomous Moral Evaluation Framework: Introduc-
tion of MoCoP, a dataset-free, self-sustaining system that
autonomously generates, evaluates, and refines moral rea-
soning scenarios across multiple LLMs without external su-
pervision.
• Cross-Model Moral Drift Quantification: Development
of quantitative methods for measuring moral drift, ethical
stability, and inter-model coherence, enabling comparative
analysis between distinct LLM architectures.
• Unified Meta-Analytic Ethics Engine: Integration of lexi-
cal, semantic, and reasoning-based evaluation modules into
a reproducible framework for continuous ethical introspec-
tion, providing longitudinal insight into the stability and
evolution of LLM moral behavior.
The remaining sections of this paper are organized as follows. Sec-
tion 2 reviews related research on evaluating the ethical dimensions
of outputs generated by LLMs. Section 3 details the proposed MoCoP
framework, followed by experimental results in Section 5. Section 6
discusses findings, Section 7 outlines threats to validity, and Sec-
tion 8 concludes with limitations and future directions.
2
Related Work
Early research focused primarily on detecting and mitigating so-
cial bias and harmful content generation. Burak et al. [7] intro-
duced OpenEthics, emphasizing transparency and open evaluation
pipelines for auditing ethical alignment in LLMs. Similarly, M Abdul-
hai et al. [1] explored rule-based fairness evaluation and post-hoc
interpretability to reduce discriminatory model behavior across
demographic groups. Although these studies advanced auditing
transparency, their reliance on fixed datasets and manually curated
prompts limits adaptability. They provide diagnostic insights into
static model states but cannot continuously track shifts in moral
reasoning and measure stability across varying contexts.
Recent approaches have extended beyond fairness to explore moral
judgment and ethical reasoning capacities in LLMs. Studies such
1OpenAI GPT-4-Turbo model, 2024
as [25] and [15] proposed structured moral reasoning benchmarks
(e.g., MoralBench) to test LLM responses against human moral intu-
itions. These works demonstrated that models exhibit partial moral
sensitivity but often lack coherence when faced with conflicting
principles and contextual ambiguity. However, benchmark-based
evaluations remain limited in scalability and temporal scope; they
capture model ethics at a single point in time and cannot reveal
how reasoning consistency evolves with interaction and retraining.
Supporting studies have examined explainability and value align-
ment as central components of responsible AI. For example, Shitong
et al. [9] proposed DeNEVIL, a debiasing and explainable alignment
model that integrates normative reasoning into LLM training. Like-
wise, Jiao et al. [16] emphasized cross-cultural moral benchmarking
and trust calibration, underscoring the sociotechnical dependencies
of ethical AI systems. Despite their strengths in interpretability
and trust analysis, these frameworks rely on predefined moral
categories and manual labeling, which limit their adaptability to
dynamic ethical contexts.
Although previous literature collectively contributes to fairness
auditing, benchmark design, and value-alignment methodologies,
a key gap remains unaddressed: the absence of a dynamic, model-
agnostic framework capable of longitudinal moral evaluation. Ex-
isting works assess ethical behavior at discrete points, but they
lack mechanisms for autonomous generation, interpretation, and
adaptation of ethical reasoning scenarios. Moreover, none of the
existing approaches provides computational tools to quantify ethi-
cal divergence or track cross-model moral coherence in real time.
3
Methodology
Building upon the conceptual foundation established in Section 1,
the proposed Moral Consistency Pipeline (MoCoP) operationalizes
continuous ethical evaluation as a closed-loop, dataset-free mecha-
nism designed to measure, interpret, and refine the moral stability
of Large Language Models (LLMs). In alignment with the abstract
and introduction, MoCoP focuses exclusively on evaluation and
interpretation, rather than optimization or retraining, ensuring
conceptual and methodological coherence.
3.1
System Overview
As illustrated in Figure 1, MoCoP follows a feedback-driven ar-
chitecture composed of three primary analytical layers: (i) Lexical
Integrity Analysis, (ii) Semantic Risk Estimation, and (iii) Reasoning-
Based Judgment Modeling. Together, these layers quantify moral
consistency across contexts and over time. This proposed architec-
ture autonomously generates ethically sensitive scenarios, evaluates
model responses, and iteratively refines scenario complexity using
internal feedback mechanisms—without reproducing or amplifying
unethical content.
3.2
Core Analytical Layers
Lexical Integrity Analysis. This layer evaluates surface-level lin-
guistic structure to detect bias, fairness deviations, and polarity
inconsistencies. Using lexical entropy, polarity variance, and bias-
weighted sentiment, the system estimates how consistently models
maintain neutral and coherent language across ethical contexts.

--- Page 3 ---

The Moral Consistency Pipeline: Continuous Ethical Evaluation for Large Language Models
DSE 2026, April 12–18, 2026, Rio de Janeiro, Brazil
Figure 1: Schematic of the Architecture of the MoCoP Frame-
work. The pipeline integrates lexical integrity analysis, se-
mantic risk estimation, and reasoning-based judgment mod-
eling in a continuous feedback loop for evaluating LLM moral
consistency. Arrows indicate feedback flow across layers.
This produces the lexical integrity feature 𝐿𝑖𝑗for each model re-
sponse 𝑟𝑖𝑗.
Semantic Risk Estimation. The second layer assesses contex-
tual risk through probabilistic semantic embedding analysis. It
quantifies potential harm, coercion, and toxicity using hybrid lexi-
cal–semantic similarity and bounded risk functions. The resulting
score, 𝜏𝑖𝑗, represents each model’s estimated semantic toxicity in-
dex, encoding its ethical exposure to risk.
Reasoning-Based Judgment Modeling. This layer captures logical
and ethical soundness within model reasoning. Each response is
decomposed into propositional reasoning chains that are evaluated
for moral justification, causal coherence, and logical stability. The
derived feature 𝑅𝑖𝑗represents the strength of ethical reasoning con-
sistency. Together, the ethical feature vector for each model–prompt
pair (𝑀𝑗, 𝑝𝑖) is expressed as:
E𝑖𝑗= [𝐿𝑖𝑗,𝜏𝑖𝑗, 𝑅𝑖𝑗],
forming the foundation of all subsequent quantitative analyses.
3.3
Formal Framework
Let P = {𝑝1, 𝑝2, . . . , 𝑝𝑁} denote the set of automatically gener-
ated moral scenarios, and M = {𝑀1, 𝑀2} represent the evaluated
LLMs—GPT-4-Turbo and DeepSeek. For each prompt–model pair,
the response 𝑟𝑖𝑗= 𝑀𝑗(𝑝𝑖) is projected into the ethical feature space
via:
E𝑖𝑗= Eval(𝑟𝑖𝑗) = [𝐿𝑖𝑗,𝜏𝑖𝑗, 𝑅𝑖𝑗].
An overall Ethical Utility Function measures combined moral per-
formance:
𝐽(𝜃) = E𝑖,𝑗[ 𝛼𝐿𝑖𝑗+ 𝛽𝑅𝑖𝑗−𝜆𝜏𝑖𝑗],
where 𝛼, 𝛽, and 𝜆are adaptive weights controlling the trade-off
between lexical coherence, reasoning alignment, and toxicity re-
duction. The system seeks stability when 𝐽(𝜃) converges toward a
steady state across evaluation cycles.
3.4
Feedback Dynamics
Each evaluation cycle consists of the following sequence:
(1) Prompt Generation: Sample or regenerate a scenario 𝑝𝑖
from a moral domain distribution.
(2) Response Collection: Query each model 𝑀𝑗and collect
responses 𝑟𝑖𝑗.
(3) Feature Extraction: Compute the ethical feature vector E𝑖𝑗.
(4) Aggregation & Adaptation: Aggregate cross-model met-
rics, compute divergence, and update the prompt distribution
to maintain balance.
This self-sustaining loop ensures MoCoP continuously evaluates
model behavior under evolving ethical conditions without human
annotation or external supervision.
Algorithm 1 MoCoP Evaluation Cycle
Require: Prompt set P, model set M = {𝑀1, 𝑀2}, initial weights
𝜃= (𝛼, 𝛽, 𝜆), learning rate 𝜂𝜃
Ensure: Ethical utility trajectory 𝐽(𝜃) and convergence statistics
1: for each prompt 𝑝𝑖∈P do
2:
for each model 𝑀𝑗∈M do
3:
Generate response 𝑟𝑖𝑗←𝑀𝑗(𝑝𝑖)
4:
Extract ethical features E𝑖𝑗= [𝐿𝑖𝑗,𝜏𝑖𝑗, 𝑅𝑖𝑗]
5:
Compute ethical utility 𝐽𝑖𝑗= 𝛼𝐿𝑖𝑗+ 𝛽𝑅𝑖𝑗−𝜆𝜏𝑖𝑗
6:
end for
7:
Calculate inter-model divergence D𝑚𝑜𝑟𝑎𝑙
8:
Update scenario distribution using feedback regulator F
9: end for
10: Update parameters: 𝜃←𝜃−𝜂𝜃∇𝜃𝐽(𝜃)
11: Check convergence: Δ𝐽(𝑡) < 𝜀
Algorithm 1 formalizes the MoCoP feedback loop described
above. Each iteration autonomously generates scenarios, extracts
ethical features, and aggregates model outputs to refine the distribu-
tion of ethical stimuli. Unlike static benchmark evaluations, MoCoP
iteratively adjusts prompt difficulty and ethical context weighting,
allowing dynamic assessment of moral stability while maintaining
dataset independence.
3.5
Quantitative Convergence
Ethical equilibrium is achieved when the utility function variation
stabilizes:
lim
𝑡→∞Δ𝐽(𝑡) = 0,
where Δ𝐽(𝑡) measures inter-iteration change. Convergence indi-
cates that model moral reasoning has reached consistent perfor-
mance across both contextual and temporal dimensions, fulfilling
MoCoP’s objective of longitudinal ethical consistency.
4
Experimental Setup
To empirically validate MoCoP’s capacity for continuous, inter-
pretable ethical evaluation, we implemented the framework in a
closed-loop experimental environment reflecting the three analyti-
cal layers defined in Section 3. The experimental objectives include
assessing (i) cross-model moral coherence, (ii) temporal stability,
and (iii) semantic safety across evolving ethical scenarios.

--- Page 4 ---

DSE 2026, April 12–18, 2026, Rio de Janeiro, Brazil
Saeid Jamshidi, Kawser Wazed Nafi, Arghavan Moradi Dakhel, Negar Shahabi†, Foutse Khomh
4.1
Environment Configuration
The MoCoP environment is defined as:
M≀C≀P = ⟨I, E, M, F ⟩,
where:
• I (Interaction Layer) manages structured input–output
communication and ensures prompt standardization.
• E (Ethical Evaluation Engine) implements the three-layer
analysis (lexical, semantic, reasoning).
• M (Meta-Analytic Layer) aggregates results, computes
divergence, and tracks moral drift.
• F (Feedback Regulator) adjusts prompt distributions to
maintain balanced evaluation entropy and convergence.
Each prompt evolves over iterations as:
𝑝(𝑡+1)
𝑗
= F  E(I(𝑀𝑖, 𝑝(𝑡)
𝑗)),
producing a self-adapting testbed that maintains ethical continuity
and variability across evaluation cycles.
4.2
Models Under Evaluation
Two representative LLMs were selected:
(1) GPT-4-Turbo: A transformer-based model emphasizing fac-
tual precision and safety-aligned moral reasoning.
(2) DeepSeek: A reinforcement-augmented generative model
emphasizing interpretive depth and contextual adaptability.
Both models were tested under identical conditions, ensuring that
observed differences emerge from intrinsic reasoning patterns rather
than external variance.
4.3
Autonomous Moral Scenario Generation
To preserve dataset independence, MoCoP autonomously generated
𝑛= 500 unique ethical prompts spanning five domains:
P = P𝑓𝑎𝑖𝑟𝑛𝑒𝑠𝑠∪P𝑝𝑟𝑖𝑣𝑎𝑐𝑦∪P𝑡𝑟𝑎𝑛𝑠𝑝𝑎𝑟𝑒𝑛𝑐𝑦∪P𝑐𝑜𝑒𝑟𝑐𝑖𝑜𝑛∪P𝑎𝑙𝑖𝑔𝑛𝑚𝑒𝑛𝑡.
Each domain’s weight 𝑤𝑐was dynamically updated according to di-
vergence magnitude, ensuring balanced exploration. Prompts were
bounded by lexical entropy H (𝑝𝑗) < 0.7 to prevent degeneration
and maintain linguistic clarity.
4.4
Evaluation Metrics
For each model(𝑀𝑖)–prompt(𝑝𝑗) pair, MoCoP computes:
𝑆𝑖𝑗= (𝑠(𝑙𝑒𝑥)
𝑖𝑗
,𝑠(𝑠𝑒𝑚)
𝑖𝑗
,𝑠(𝑟𝑒𝑎)
𝑖𝑗
),
Where 𝑠(𝑙𝑒𝑥)
𝑖𝑗
, 𝑠(𝑠𝑒𝑚)
𝑖𝑗
and 𝑠(𝑟𝑒𝑎)
𝑖𝑗
denote the Lexical Integrity [12],
Semantic Safety [22], and Reasoning Coherence [8] scores, respec-
tively, as detailed in Section 3.2. Each metric produces a normalized
score within the range [0,1], with higher values indicating stronger
adherence to safety and reliability criteria. Specifically, Lexical In-
tegrity assesses the preservation of prompt structure and resistance
to injection or tampering; Semantic Safety evaluates alignment with
intended meaning and absence of harmful or biased content; and
Reasoning Coherence measures the logical consistency and causal
validity of the model’s reasoning chain. A score approaching 1.0 in
any dimension signifies optimal performance for that specific safety
attribute. Reasoning coherence is measured by cosine similarity:
𝑠(𝑟𝑒𝑎)
𝑖𝑗
= cos(𝜙(𝑝𝑗),𝜙(𝑟𝑖𝑗)),
while semantic safety is defined via a logistic toxicity function:
𝑠(𝑠𝑒𝑚)
𝑖𝑗
= 1 −𝜎(𝛼· tox(𝑟𝑖𝑗)),
𝛼= 0.85.
The final composite ethical response is calculated as:
R(𝑀𝑖, 𝑝𝑗) = 𝑤1𝑠(𝑙𝑒𝑥)
𝑖𝑗
+ 𝑤2𝑠(𝑠𝑒𝑚)
𝑖𝑗
+ 𝑤3𝑠(𝑟𝑒𝑎)
𝑖𝑗
,
where (𝑤1,𝑤2,𝑤3) = (0.3, 0.35, 0.35), emphasizing balance between
linguistic neutrality and reasoning soundness.
4.5
Performance and Stability Metrics
Global ethical consistency is defined as:
ECI(𝑀𝑖) = E𝑝𝑗∼P [R(𝑀𝑖, 𝑝𝑗)],
while cross-model divergence and temporal stability are quantified
as:
D𝑚𝑜𝑟𝑎𝑙= 1
𝑛
𝑛
∑︁
𝑗=1
ECI(𝑗)
𝐺𝑃𝑇−4 −ECI(𝑗)
𝐷𝑒𝑒𝑝𝑆𝑒𝑒𝑘
,
S𝑡𝑒𝑚𝑝𝑜𝑟𝑎𝑙= 1 −
1
𝑇−1
𝑇−1
∑︁
𝑡=1
ECI(𝑡+1) −ECI(𝑡).
Higher S𝑡𝑒𝑚𝑝𝑜𝑟𝑎𝑙values reflect stronger moral steadiness and ethi-
cal robustness across feedback cycles.
4.6
Control and Convergence
To ensure replicability, prompts were randomized across runs, re-
sponse latencies were equalized (𝛿𝑡∈[0.6, 1.0] s), and feedback
gain was bounded (|𝛾𝑡| < 0.05) to prevent oscillation. Convergence
to ethical equilibrium occurs when:
𝜕2ECI
𝜕𝑡2
≈0,
indicating that both models exhibit stable, interpretable ethical be-
havior. This equilibrium marks MoCoP’s fulfillment of continuous,
context-aware moral consistency assessment.
5
Experimental Results
To validate the effectiveness and robustness of the proposed Mo-
CoP, controlled experiments were performed using GPT-4-Turbo
and DeepSeek models. The following section demonstrates the
outcomes of these evaluations across multiple ethical dimensions.
5.1
Ethical Safety Distribution
From Figure. 2, the observed counts are:GPT-4-Turbo: Safe = 195,
Borderline = 275, Unsafe = 23 (𝑁gpt = 493), and DeepSeek: Safe =
210, Borderline = 280, Unsafe = 20 (𝑁deep = 510). Table 1 reports
counts and proportions. We test the difference on the “Unsafe” rate
Table 1: Safety category counts and proportions derived.
Model
Safe
Borderline
Unsafe
𝑁
GPT-4-Turbo
195 (39.55%)
275 (55.78%)
23 (4.67%)
493
DeepSeek
210 (41.18%)
280 (54.90%)
20 (3.92%)
510

--- Page 5 ---

The Moral Consistency Pipeline: Continuous Ethical Evaluation for Large Language Models
DSE 2026, April 12–18, 2026, Rio de Janeiro, Brazil
Figure 2: Safety category distribution across GPT-4-Turbo
and DeepSeek models.
using a 2×2 chi-square test: 𝜒2 = 0.335, df = 1, 𝑝≈0.56, with a
insignificant effect size 𝑉=
√︁
𝜒2/𝑁= 0.018 (𝑁= 1003). The risk
ratio (RR) for Unsafe is RR = 0.84 and the absolute risk reduction
is ARR = 0.75%, both indicating a small, non-significant advantage
for DeepSeek.
For a proportion ˆ𝑝computed from 𝑛samples, a 95% Wilson confi-
dence interval can be reported:
ˆ𝑝Wilson ± 𝑧0.975
√︄
ˆ𝑝(1 −ˆ𝑝)
𝑛
+ 𝑧2
0.975
4𝑛2
. 
1 + 𝑧2
0.975
𝑛

,
where 𝑧0.975 = 1.96. Applying this to the Unsafe rates provides
uncertainty bands that remain overlapping across models, rein-
forcing the non-significant difference. Both models concentrate
the majority of outputs in the Safe/Borderline region (> 95%), with
DeepSeek showing a marginal reduction in Unsafe frequency. In
MoCoP terms, this suggests comparable robustness of the ethical
guardrails across architectures, with only small practical deviations
at the tail.
5.2
Ethical Score Distribution
Figure 3 demonstrates near-Gaussian behavior centered around
a mean ethical score ¯𝐸≈0.80 for both models. A preliminary
Shapiro–Wilk test[13] confirmed normality (𝑝> 0.05), validating
the use of parametric comparative analysis. Descriptive statistics
summarized in Table 2 indicate that DeepSeek achieved a slightly
higher mean score, while GPT-4-Turbo demonstrated reduced dis-
persion, implying stronger moral consistency across test condi-
tions. Statistical comparison using an independent two-sample
Table 2: Descriptive statistics of ethical score distributions.
Model
¯𝐸
𝜎(𝐸)
𝐸min
𝐸max
GPT-4-Turbo
0.793
0.067
0.61
0.94
DeepSeek
0.807
0.072
0.58
1.00
𝑡-test showed no significant difference in mean ethical performance
between the two models (𝑡(998) = −1.86, 𝑝= 0.063), suggesting
that both systems achieve comparable aggregate moral alignment.
However, the variance analysis (𝐹= 0.86, 𝑝< 0.05) indicated
that GPT-4-Turbo maintains slightly lower dispersion, implying
Figure 3: Distribution of ethical scores across models.
higher internal control of ethical consistency. To further quantify
cross-model ethical alignment, the correlation coefficient between
their ethical score vectors, 𝜌(𝐸GPT, 𝐸DS), was computed at 0.84, evi-
dencing substantial coherence in shared moral judgments across
prompts. This high correlation suggests that both architectures
likely converge toward similar ethical baselines under the MoCoP
framework, though their reasoning trajectories may differ seman-
tically. From a moral stability perspective, the effective coherence
ratio𝐶𝑚= 1−𝜎(𝐸𝑚) yielded𝐶GPT = 0.933 and𝐶DS = 0.928, demon-
strating that both systems sustain moral consistency above 92%
under variable ethical scenarios.
5.3
Ethical Performance Stability
To quantify the stability of moral reasoning across model archi-
tectures, we conducted a statistical comparison of ethical score
distributions for GPT-4-Turbo and DeepSeek. Let the ethical score
Figure 4: Comparison of ethical score stability across models.
for each model 𝑚be denoted as 𝐸𝑚= {𝑒𝑚,1,𝑒𝑚,2, . . . ,𝑒𝑚,𝑛}, where
𝑒𝑚,𝑖∈[0, 1]. The mean ethical performance 𝜇𝑚and variance 𝜎2
𝑚
are defined as:
𝜇𝑚= 1
𝑛
𝑛
∑︁
𝑖=1
𝑒𝑚,𝑖,
𝜎2
𝑚=
1
𝑛−1
𝑛
∑︁
𝑖=1
(𝑒𝑚,𝑖−𝜇𝑚)2.
To measure stability, we define a Moral Stability Index (MSI):
𝑀𝑆𝐼𝑚=
𝜇𝑚
1 + 𝜎𝑚
where higher 𝑀𝑆𝐼𝑚values indicate greater ethical consistency
across reasoning instances. Table 3 summarizes the descriptive sta-
tistics reconstructed from Fig. 4. To statistically assess differences,

--- Page 6 ---

DSE 2026, April 12–18, 2026, Rio de Janeiro, Brazil
Saeid Jamshidi, Kawser Wazed Nafi, Arghavan Moradi Dakhel, Negar Shahabi†, Foutse Khomh
Table 3: Descriptive statistics of ethical score stability.
Model
Mean
Median
SD
MSI
DeepSeek
0.81
0.80
0.083
0.748
GPT-4-Turbo
0.79
0.78
0.067
0.740
a two-tailed Welch’s 𝑡-test was applied:
𝑡=
𝜇1 −𝜇2
√︂
𝜎2
1
𝑛1 +
𝜎2
2
𝑛2
,
yielding 𝑡= 1.32, 𝑝= 0.19 (n.s.), indicating no statistically signifi-
cant difference in ethical means between models. Levene’s test[11]
for variance homogeneity (𝐹= 2.04, 𝑝= 0.15) also confirmed com-
parable dispersion. Both models exhibit strong moral consistency
with median ethical scores exceeding 0.78. DeepSeek demonstrates
higher ethical centrality (𝜇= 0.81), while GPT-4-Turbo achieves
slightly reduced variance (𝜎2 = 0.0045), implying more uniform
ethical alignment. This suggests that DeepSeek adopts a broader
moral reasoning spectrum, whereas GPT-4-Turbo favors tighter nor-
mative coherence. The near-identical 𝑀𝑆𝐼values (< 1% difference)
confirm that both architectures maintain robust ethical stability
under the MoCoP evaluation framework.
5.4
Correlation Analyses
The MoCoP analysis revealed two critical correlation patterns gov-
erning model behavior. As shown in the Figure 5, a strong in-
verse correlation was observed between ethical and toxicity scores
(𝑟𝐸𝑇= −0.81, 𝑝< 0.001). This indicates that higher ethical align-
ment directly corresponds to lower toxicity, confirming the Mo-
CoP’s theoretical premise that moral coherence suppresses linguis-
tic harm. Both GPT-4-Turbo and DeepSeek exhibit nearly identical
regression slopes (𝛽𝐺𝑃𝑇= 0.77, 𝛽𝐷𝑒𝑒𝑝𝑆𝑒𝑒𝑘= 0.79), implying shared
ethical regulation dynamics despite distinct architectures.
The MoCoP analysis revealed two critical correlation patterns
Figure 5: Correlation between ethical and toxicity scores.
governing model behavior. As shown in the Figure. 5, a strong in-
verse correlation was observed between ethical and toxicity scores
(𝑟𝐸𝑇= −0.81, 𝑝< 0.001). This indicates that higher ethical align-
ment directly corresponds to lower toxicity, confirming the Mo-
CoP’s theoretical premise that moral coherence suppresses linguis-
tic harm. Both GPT-4-Turbo and DeepSeek exhibit nearly identical
Figure 6: Relationship between ethical score and response
latency across GPT-4-Turbo and DeepSeek.
regression slopes (𝛽𝐺𝑃𝑇= 0.77, 𝛽𝐷𝑒𝑒𝑝𝑆𝑒𝑒𝑘= 0.79), implying shared
ethical regulation dynamics despite distinct architectures. Formally,
this dependency can be approximated as:
𝑇= 𝛼−𝛽𝐸+ 𝜖,
where 𝑇is the toxicity score, 𝐸the ethical alignment score, 𝛽the
sensitivity coefficient (𝛽≈0.78), and 𝜖represents model-specific
stochastic variance driven by prompt diversity. To assess robust-
ness, we computed both Pearson and Spearman coefficients across
the two models. Results are summarized in Table 4. As shown,
Table 4: Correlation Statistics Across Dimensions.
Correlation Pair
Model
r (Pearson)
𝜌(Spearman)
𝐸–𝑇
GPT-4-Turbo
-0.80
-0.77
𝐸–𝑇
DeepSeek
-0.82
-0.79
𝐸–𝐿
GPT-4-Turbo
-0.05
-0.03
𝐸–𝐿
DeepSeek
-0.07
-0.04
the 𝐸–𝑇correlation is both strong and monotonic across models,
while 𝐸–𝐿correlations remain statistically insignificant. This aligns
with the MoCoP’s predictive design, which hypothesizes that ethi-
cal coherence is orthogonal to temporal latency. Figure 6 further
confirms this, showing a near-zero slope (𝑟𝐸𝐿= −0.06, 𝑝= 0.41),
reinforcing that moral reasoning stability is temporally invariant.
In other words, model ethics are not emergent artifacts of longer
reasoning or token-level deliberation but instead arise from in-
trinsic representational alignment within the moral embedding
subspace. Furthermore, the correlation analyses demonstrate that
ethical integrity and linguistic safety are inversely proportional
and statistically robust across both models. Moreover, the observed
temporal independence of ethical alignment confirms the internal
consistency of moral reasoning within the evaluated systems.
5.5
Multivariate Behavioral
The multivariate correlation analysis presented in Figure. 7 provides
an overview of behavioral dependencies across three quantitative

--- Page 7 ---

The Moral Consistency Pipeline: Continuous Ethical Evaluation for Large Language Models
DSE 2026, April 12–18, 2026, Rio de Janeiro, Brazil
dimensions: ethical score (𝐸), toxicity score (𝑇), and response la-
tency (𝐿). The joint distribution of these metrics was examined
through both parametric (Pearson) and rank-based (Spearman) cor-
relation analyses to assess monotonic trends and robustness under
non-linear deviations.
The resulting correlation matrix was computed as:
𝑅=

1
−0.81
−0.06
−0.81
1
0.04
−0.06
0.04
1

,
where each coefficient 𝑟𝑖𝑗quantifies the linear association between
metrics 𝑖and 𝑗. The strong negative correlation between 𝐸and
𝑇(𝑟𝐸𝑇= −0.81, 𝑝< 0.001) validates the earlier univariate find-
ings—indicating that higher ethical alignment consistently coin-
cides with lower linguistic toxicity. The near-zero correlations in-
volving latency (𝑟𝐸𝐿= −0.06, 𝑟𝑇𝐿= 0.04) confirm that temporal
generation dynamics exert an insignificant impact on moral reason-
ing and lexical moderation. From a statistical modeling perspective,
this multivariate relationship can be approximated using a linear
dependency model:
𝐸= 𝛾0 + 𝛾1𝑇+ 𝛾2𝐿+ 𝜖,
where 𝛾1 ≈−0.78 and 𝛾2 ≈−0.05 under ordinary least squares esti-
mation, with residual variance𝜎2
𝜖≈0.012. The low multicollinearity
between predictors (VIF < 1.2) ensures interpretability of the coef-
ficients and supports MoCoP’s design assumption of orthogonal
ethical and temporal axes. The distributions of 𝐸and 𝑇are normal,
while 𝐿follows a mildly right-skewed profile consistent with typical
API latency patterns. This statistical stability implies that MoCoP’s
evaluation framework captures intrinsic moral variance rather than
performance noise. In synthesis, the multivariate findings reinforce
that ethical and toxicity behaviors are inversely and linearly related,
forming a central axis of moral coherence across evaluated models.
Furthermore, response latency remains statistically independent,
indicating that the stability of ethical reasoning is not impacted by
computational depth or temporal delay.
6
Discussion
The evaluation of the MoCoP demonstrates a mathematically grounded
mechanism for continuous moral auditing in LLMs. The strong in-
verse relation between ethical and toxicity metrics (𝑟𝐸𝑇= −0.81)
indicates that linguistic harm reduction is an emergent property of
representational regularization, not merely a filtering artifact. Tem-
poral invariance (𝑟𝐸𝐿≈0) confirms that moral reasoning coherence
is independent of computational latency, implying an internal par-
allel inference channel for ethics. MoCoP’s feedback-driven struc-
ture functions as a closed-loop dynamical system that converges
toward moral equilibrium, verified by Gaussian stabilization of
ethical and toxicity distributions. The gradient-based ethical param-
eters 𝜃= (𝛼, 𝛽,𝛾, 𝜆) provide interpretable trade-offs across fairness,
transparency, reasoning integrity, and toxicity control. Normaliza-
tion on the probability simplex ensures that moral updates remain
transparent and bounded. Empirically, variance reduction across
epochs confirms stable convergence of moral gradients and sup-
pression of ethical drift. Cross-model correlation (𝜌= 0.84) reveals
convergent moral attractors between GPT-4-Turbo and DeepSeek
despite architectural heterogeneity. The probabilistic correction
mechanism acts as an adaptive control law, continuously recali-
brating ethical embeddings under stochastic prompt perturbations.
From a systems perspective, MoCoP performs ethical homeostasis,
maintaining normative stability amid environmental change. Its dif-
ferentiable design allows seamless integration with reinforcement
tuning and gradient-based governance layers. Furthermore, by mod-
eling moral reasoning as an optimization manifold, MoCoP bridges
computational ethics with learning theory, enabling reproducible,
model-agnostic introspection. Ultimately, our proposed framework
transforms ethical evaluation into a dynamic equilibrium process
that embeds moral accountability directly within generative com-
putation.
7
Threats to Validity
The robustness and interpretive reliability of the MoCoP were ex-
amined through two major dimensions of experimental validity:
internal and external [26]. Each reflects potential risks to inference
accuracy and the generalizability of the findings.
7.1
Internal Validity
Internal validity was ensured through strict experimental control
within a unified MoCoP environment. Identical prompt structures,
randomized scenario order, consistent evaluation parameters, and
latency regulation minimized confounding effects. Observed moral
differences thus reflect genuine model reasoning behavior rather
than procedural bias. A minor limitation arises from stochastic
variability inherent to autoregressive text generation, which may
slightly influence ethical score variance.
7.2
External Validity
External validity addresses the generalizability of MoCoP results be-
yond the tested English LLMs. While the framework’s modular com-
ponents—LLMConnector, EthicalGuardPro, and the meta-analytic
ethics layer—enable extension to multilingual and multimodal con-
texts, moral interpretation remains culturally and linguistically de-
pendent. Future studies will incorporate cross-linguistic calibration
and domain-specific evaluation to assess adaptability and ensure
broader ethical applicability.
8
Conclusion, Limitations, and Future Work
This study presented the MoCoP, a quantitative and dataset-free
framework for evaluating ethical stability, linguistic safety, and
temporal invariance in LLMs. Comparative experiments with GPT-
4-Turbo and DeepSeek confirmed MoCoP’s ability to derive inter-
pretable moral patterns, showing a strong inverse relation between
ethics and toxicity (𝑟𝐸𝑇= −0.81, 𝑝< 0.001) and temporal stabil-
ity of moral reasoning (𝑟𝐸𝐿≈0). Despite these strengths, limita-
tions include dependence on English moral ontologies, residual
stochastic variance from autoregressive decoding, and potential
underestimation of nonlinear ethical dynamics. Future work will
extend MoCoP to multilingual and multimodal settings, integrate
reinforcement-driven feedback for adaptive calibration, and incor-
porate neuro-symbolic interpretability to trace moral reasoning
at finer granularity. Collectively, these directions aim to evolve
MoCoP into a scalable and autonomous benchmark for continuous
ethical intelligence in next-generation AI systems.

--- Page 8 ---

DSE 2026, April 12–18, 2026, Rio de Janeiro, Brazil
Saeid Jamshidi, Kawser Wazed Nafi, Arghavan Moradi Dakhel, Negar Shahabi†, Foutse Khomh
Figure 7: Correlation among ethical, toxicity, and latency scores across GPT-4-Turbo and DeepSeek models.
References
[1] Marwa Abdulhai, Gregory Serapio-Garcia, Clément Crepy, Daria Valter, John
Canny, and Natasha Jaques. 2023. Moral foundations of large language models.
arXiv preprint arXiv:2310.15337 (2023).
[2] Gaurav Agrawal. 2024. Accountability, trust, and transparency in AI systems
from the perspective of public policy: Elevating ethical standards. In AI healthcare
applications and security, ethical, and legal considerations. IGI Global, 148–162.
[3] Olatunji Akinrinola, Chinwe Chinazo Okoye, Onyeka Chrisanctus Ofodile, and
Chinonye Esther Ugochukwu. 2024. Navigating and reviewing ethical dilemmas
in AI development: Strategies for transparency, fairness, and accountability. GSC
Advanced Research and Reviews 18, 3 (2024), 050–058.
[4] Saikat Barua. 2024. Exploring autonomous agents through the lens of large
language models: A review. arXiv preprint arXiv:2404.04442 (2024).
[5] FM Bayan and M Fayyad. 2024. The Ethics of AI: navigating the Moral dilemmas
of Artificial Intelligence. Arab Journal for Scientific Publishing (AJSP) ISSN 2663
(2024), 5798.
[6] Federico Bina et al. 2023. Agency in progress: The ethics, evolution, and psychol-
ogy of moral change. (2023).
[7] Burak Erinç Çetin, Yıldırım Özen, Elif Naz Demiryılmaz, Kaan Engür, and Cagri
Toraman. 2025. OpenEthics: A Comprehensive Ethical Evaluation of Open-Source
Generative Large Language Models. arXiv preprint arXiv:2505.16036 (2025).
[8] Heejin Do, Jaehui Hwang, Dongyoon Han, Seong Joon Oh, and Sangdoo Yun.
2025. What Defines Good Reasoning in LLMs? Dissecting Reasoning Steps with
Multi-Aspect Evaluation. arXiv preprint arXiv:2510.20603 (2025).
[9] Shitong Duan, Xiaoyuan Yi, Peng Zhang, Tun Lu, Xing Xie, and Ning Gu. 2023.
Denevil: Towards deciphering and navigating the ethical values of large language
models via instruction learning. arXiv preprint arXiv:2310.11053 (2023).
[10] Jinyuan Fang, Yanwen Peng, Xi Zhang, Yingxu Wang, Xinhao Yi, Guibin Zhang,
Yi Xu, Bin Wu, Siwei Liu, Zihao Li, et al. 2025. A comprehensive survey of
self-evolving ai agents: A new paradigm bridging foundation models and lifelong
agentic systems. arXiv preprint arXiv:2508.07407 (2025).
[11] Joseph L Gastwirth, Yulia R Gel, and Weiwen Miao. 2009. The impact of Levene’s
test of equality of variances on statistical theory and practice. (2009).
[12] Jiang Han and Mingming Guo. 2024. An evaluation of the safety of chatgpt with
malicious prompt injection. (2024).
[13] Zofia Hanusz, Joanna Tarasinska, and Wojciech Zielinski. 2016. Shapiro–Wilk
test with known mean. REVSTAT-statistical Journal 14, 1 (2016), 89–100.
[14] Yu Huang. 2024. Levels of ai agents: from rules to large language models. arXiv
preprint arXiv:2405.06643 (2024).
[15] Jianchao Ji, Yutong Chen, Mingyu Jin, Wujiang Xu, Wenyue Hua, and Yongfeng
Zhang. 2025. Moralbench: Moral evaluation of llms. ACM SIGKDD Explorations
Newsletter 27, 1 (2025), 62–71.
[16] Junfeng Jiao, Saleh Afroogh, Abhejay Murali, Kevin Chen, David Atkinson, and
Amit Dhurandhar. 2025. LLM ethics benchmark: a three-dimensional assessment
system for evaluating moral reasoning in large language models. Scientific Reports
15, 1 (2025), 34642.
[17] Mohammad N Khreisat, Danish Khilani, Maher Ali Rusho, Evelyn Ansah Karkku-
lainen, Almighty Cortezo Tabuena, and Anton Diaz Uberas. 2024. Ethical im-
plications of AI integration in educational decision making: Systematic review.
Educational Administration: Theory and Practice 30, 5 (2024), 8521–8527.
[18] Haoran Lu, Luyang Fang, Ruidong Zhang, Xinliang Li, Jiazhang Cai, Huimin
Cheng, Lin Tang, Ziyu Liu, Zeliang Sun, Tao Wang, et al. 2025. Alignment and
safety in large language models: Safety mechanisms, training paradigms, and
emerging challenges. arXiv preprint arXiv:2507.19672 (2025).
[19] Timothy R McIntosh, Teo Susnjak, Nalin Arachchilage, Tong Liu, Dan Xu, Paul
Watters, and Malka N Halgamuge. 2025. Inadequacies of large language model
benchmarks in the era of generative artificial intelligence. IEEE Transactions on
Artificial Intelligence (2025).
[20] Bruce M McLaren. 2006. Computational models of ethical reasoning: Challenges,
initial steps, and future directions. IEEE intelligent systems 21, 4 (2006), 29–37.
[21] Preethi Nanjundan, PV Indu, and Lijo Thomas. 2025. Navigating the ethical
landscape of artificial intelligence: Challenges, frameworks, and responsible
deployment. In Artificial Intelligence Technologies for Engineering Applications.
CRC Press, 1–13.
[22] Thomas Radcliffe, Emily Lockhart, and James Wetherington. 2024. Automated
prompt engineering for semantic vulnerabilities in large language models. Au-
thorea Preprints (2024).
[23] Dan Shi, Tianhao Shen, Yufei Huang, Zhigen Li, Yongqi Leng, Renren Jin, Chuang
Liu, Xinwei Wu, Zishan Guo, Linhao Yu, et al. 2024. Large language model safety:
A holistic survey. arXiv preprint arXiv:2412.17686 (2024).
[24] Ann E Tenbrunsel, Kristina A Diekmann, Kimberly A Wade-Benzoni, and Max H
Bazerman. 2010. The ethical mirage: A temporal explanation as to why we are
not as ethical as we think we are. Research in Organizational Behavior 30 (2010),
153–173.
[25] Eddie L Ungless, Nikolas Vitsakis, Zeerak Talat, James Garforth, Björn Ross,
Arno Onken, Atoosa Kasirzadeh, and Alexandra Birch. 2024. The Only Way is
Ethics: A Guide to Ethical Research with Large Language Models. arXiv preprint
arXiv:2412.16022 (2024).
[26] Claes Wohlin, Per Runeson, Martin Höst, Magnus C Ohlsson, Björn Regnell, and
Anders Wesslén. 2012. Experimentation in software engineering. Springer Science
& Business Media.
[27] Jie Zhang and Zong-ming Zhang. 2023. Ethics and governance of trustworthy
medical artificial intelligence. BMC medical informatics and decision making 23,
1 (2023), 7.

```
