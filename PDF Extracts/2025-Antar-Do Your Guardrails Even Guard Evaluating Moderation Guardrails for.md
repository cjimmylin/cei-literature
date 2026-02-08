---
title: "2025-Antar-Do Your Guardrails Even Guard Evaluating Moderation Guardrails for - PDF Extract"
source_pdf: "2025-Antar-Do Your Guardrails Even Guard Evaluating Moderation Guardrails for.pdf"
pages: 14
extracted_at: "2026-02-08T06:02:21.066136"
---

# PDF Extract: 2025-Antar-Do Your Guardrails Even Guard Evaluating Moderation Guardrails for

**Source PDF:** 2025-Antar-Do Your Guardrails Even Guard Evaluating Moderation Guardrails for.pdf
**Total Pages:** 14

---

## Content

```
--- Page 1 ---

“Do Your Guardrails Even Guard?” Method for Evaluating Effectiveness of
Moderation Guardrails in Aligning LLM Outputs with Expert User Expectations
Anindya Das Antar, Xun Huan, Nikola Banovic
University of Michigan, Ann Arbor
adantar@umich.edu, xhuan@umich.edu, nbanovic@umich.edu
Abstract
Ensuring that large language models (LLMs) align with hu-
man values and goals is crucial for their adoption in high-
stakes decision-making. To guard against incorrect, mislead-
ing, or otherwise unexpected or undesirable LLM outputs,
guardrail engineers implement guardrails based on expert
knowledge from subject-matter authorities to steer and align
pre-trained LLMs. Existing evaluation methods assess LLM
performance, with and without guardrails, but provide lim-
ited insight into the contribution of each individual guardrail
and its interactions on alignment. Here, we present a method
to evaluate and select guardrails that best align LLM out-
puts with empirical evidence representing expert knowledge.
Through evaluation with real-world illustrative examples of
resume quality and recidivism prediction, we show that our
method effectively identifies useful moderation guardrails in
a way that could help guardrail engineers interpret contribu-
tions of different guardrails to “user-LLM” alignment.
Introduction
Ensuring that LLMs produce desirable outputs without
harmful side-effects (Terry et al. 2024) (i.e., that they
achieve “user-LLM alignment”) is crucial for their broader
adoption. This includes aligning LLM outputs with user in-
tentions (Boggust et al. 2022), organizational goals (Desh-
pande and Sharp 2022), existing domain knowledge (Zhou
et al. 2024), empirical evidence (Wang et al. 2024a), soci-
etal values (Arzberger et al. 2025; Estrada 2018), and ethical
considerations (Shneiderman 2020; Norhashim and Hahn
2024). However, despite training on vast data, LLMs can still
produce incorrect, misleading, or otherwise unexpected or
undesirable outputs (Bender et al. 2021; Dutta et al. 2024).
Existing research (Rebedea et al. 2023; Inan et al. 2023)
showed that guardrails can steer pre-trained LLM outputs
and shape decision-making. Moderation guardrails (Ma-
homed et al. 2024), implemented through prompt engi-
neering, translate expert input, corporate guidelines, and
empirical findings into model behavior by injecting con-
straints, filtering criteria, or value-aligned instructions into
prompts. Compared to costly, resource-intensive LLM re-
training, moderation guardrails provide a lightweight, flexi-
ble way to align off-the-shelf LLMs with user expectations.
Copyright © 2025, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
Yet, not all guardrails are effective; some even intro-
duce biases that negatively steer and impact LLM decision-
making (Chu et al. 2024). Thus, it is essential to identify and
retain only those guardrails that enhance alignment. How-
ever, existing LLM evaluation methods (Chang et al. 2024)
do not specifically focus on evaluating and selecting individ-
ual guardrails from a set to ensure user-LLM alignment.
Here, we present a probabilistic method using Bayesian
inference to evaluate the effectiveness of guardrails in align-
ing a pre-trained LLM with expert user expectations for
decision-making (Fig. 1). We answer the following research
question: How can guardrail engineers systematically eval-
uate and select guardrails to ensure LLM outputs align with
expert user expectations? We do so by producing measurable
and interpretable estimates of the contribution of individual
guardrails and their interactions on model alignment.
Our method uses a curated empirical alignment dataset D
reflecting expert expectations for LLM outputs to evaluate
a set of moderation guardrails G meant to align the LLM
with those expectations. Our method then estimates a vector
of Bernoulli parameters θ, representing the activation prob-
ability of each corresponding guardrail in G, and models the
posterior probability distribution of θ to capture uncertainty
in its estimation. Unlike deterministic methods that simply
toggle guardrails on or off, our approach treats θ as a contin-
uous probability, allowing for a more nuanced evaluation.
We illustrated and validated our method in two realis-
tic use cases: 1) resume quality classification (Bertrand and
Mullainathan 2004) and 2) recidivism prediction (Angwin
et al. 2016). Each use case uses knowledge from subject
matter authority experts along with existing empirical data
to construct an alignment dataset D and a set of moder-
ation guardrails G, including specially designed distractor
guardrails that should not be selected. Our results showed
that our method selects guardrails that align LLM predic-
tions with expert expectations better than the model alone.
Our method systematically evaluates and selects moder-
ation guardrails, enabling guardrail engineers to align LLM
decisions with expert user expectations. By quantifying un-
certainty in guardrail selection, our method helps them in-
terpret the confidence of probabilistically activating each
guardrail. Such rigorous and nuanced evaluation has the po-
tential to ensure responsible deployments of LLMs in a way
that increases their adoption in high-stakes decision-making.
Proceedings of the Eighth AAAI/ACM Conference on AI, Ethics, and Society (AIES 2025)
705

--- Page 2 ---

“How well do output distributions from
LLM under different guardrail combinations align with 
expert-informed empirical alignment data?"
LLM model 
(ℳ)
User prompt
LLM output
Guardrail engineers
Subject authority experts
Empirical alignment dataset (𝒟)
•
𝒟= {𝑥𝒟, 𝑦𝒟} → Curated dataset with input 
features and expected outputs by experts
Mixing parameter (𝜃) represents guardrail activation probability for alignment
(b)
(a)
(d)
System prompt
based on expert feedback and empirical findings
+ Guardrail 1 (𝐺!)
Model with no guardrail (ℳ)
+ Guardrail 2 (𝐺")
+ Guardrail 1 & 2
(𝐺! & 𝐺")
User expectations
Guardrail(s)
(c)
𝐷!"(𝑝̂#({𝑦𝒟}) ∥𝑝̂#({𝑦*}; 𝜃))
Return posterior probability distribution 
of 𝜃for each guardrail capturing
uncertainty in the mixture of guardrails
to inform probabilistic guardrail activations
•
Policymakers
•
AI ethicists
•
Domain experts
•
Industry hierarchy
•
Regulatory agencies
𝑦) = ℳ(𝑥; 𝜃)
•
𝑝+"({𝑦𝒟})→ Empirical distribution of outputs 
in accordance with alignment goals
𝐺"
𝐺!
Measure Kullback–Leibler divergence (KLD) to estimate likelihood
Find the best mixture
for user-LLM alignment
activated
deactivated
𝐺"
𝐺!
Figure 1: Our method for evaluating and selecting guardrails: (a) empirical alignment dataset reflecting expert user expectations,
(b) implementation of expert-informed guardrails by guardrail engineers, (c) measuring alignment between outputs from the
LLM and expert-informed empirical distribution, and (d) identifying effective guardrail combinations to enhance alignment.
Background and Related Work
Here, we describe the goals of aligning LLM outputs with
user expectations, explain how different guardrails steer
model outputs to achieve this alignment, and review existing
guardrail evaluation methods, highlighting their limitations.
Aligning Model Outputs to User Expectations
Pre-trained LLM outputs are often misaligned with user ex-
pectations due to their inherent randomness and presence
of biases (Bender et al. 2021; Chang et al. 2024). Align-
ing LLM outputs with user expectations (Shankar et al.
2024; Hrytsyna and Alves 2024), rules (Hadfield-Menell,
Andrus, and Hadfield 2019), and values (Norhashim and
Hahn 2025; Gabriel 2020) is essential for accurate decision-
making (Lai et al. 2023; Chiang et al. 2024) and miti-
gating bias (Fang et al. 2023). Effective user-LLM align-
ment (Wang et al. 2024b; Gombolay 2024; Robinson 2023)
goes beyond technical adjustments—it requires understand-
ing the stakeholders who define these expectations and shape
model behavior (Deshpande and Sharp 2022). Domain ex-
perts, ethicists, and policymakers establish alignment objec-
tives based on domain knowledge (Zhi-Xuan et al. 2024;
Zhang et al. 2024), empirical data (Wang et al. 2024a), so-
cietal values (Norhashim and Hahn 2024; Varshney 2025),
law (Hadfield-Menell and Hadfield 2019), and ethical guide-
lines (Chivukula et al. 2024; Awad et al. 2018). Guardrail en-
gineers operationalize these objectives by identifying risks,
implementing mitigations, and shaping alignment strategies
in collaboration with domain experts (Chiang et al. 2023).
Influence of Guardrails in Model Alignment
Existing human-AI alignment methods integrate explicit
principles during LLM development (Gabriel 2020) or fine-
tune models with high-quality data (Zhao et al. 2024). How-
ever, unlike narrow AI models, retraining general-purpose
LLMs is costly (Wang et al. 2024b). Guardrails provide
an alternative by steering pre-trained LLM outputs (Dong
et al. 2024). Input guardrails prevent inappropriate con-
tent from reaching the model, while output guardrails val-
idate and refine responses before delivery. Output modera-
tion guardrails (Yuan et al. 2024) enforce corporate policies
and ethical guidelines to align LLM decisions with user ex-
pectations. Also, security guardrails help mitigate jailbreak-
ing (Wang et al. 2024c; Cornacchia et al. 2025) and adver-
sarial attacks (Dev et al. 2024; Iqbal, Kohno, and Roesner
2025), both of which are beyond the scope of this paper.
Existing Approaches to Guardrail Evaluation
Evaluating and selecting effective guardrails remains chal-
lenging due to the difficulty of isolating their individual ef-
fects and understanding their interplay. Existing LLM eval-
uation methods that assess output quality (Liu et al. 2023) or
fairness (Li et al. 2020) could, in principle, be repurposed to
measure changes in LLM behavior after applying guardrails.
However, this could obscure the contributions of individual
guardrails and their interactions. Methods that steer LLMs
by manipulating internal representations (e.g., changing ac-
tivations) (Chu et al. 2024) could highlight discrepancies be-
tween generated and desirable outputs, but attempt to mod-
ify the model rather than prompt-based guardrails. Exist-
ing auditing methods (Mahomed et al. 2024; Rastogi et al.
2023) evaluate which LLM outputs are affected by exist-
ing guardrails, but not which guardrails meaningfully con-
tribute to improved alignment. This limits their usefulness
for guardrail selection, even when combined with methods
that detect specific guardrail presence (Yang et al. 2025).
Method to Evaluate and Select Guardrails
Our probabilistic method leverages Bayesian inference to
evaluate and select guardrails that best align pre-trained
LLM outputs with expert expectations. By modeling each
guardrail’s posterior probability distribution, our method
helps interpret the uncertainty of activating each guardrail.
It also helps identify and exclude guardrails that could intro-
duce unintended downstream consequences in predictions.
706

--- Page 3 ---

User-Defined Inputs for Guardrail Evaluation
The guardrail engineer using our method (henceforth the
user) must define alignment criteria for a pre-trained LLM
M to align its outputs with a curated dataset D that contains
empirical evidence representing expert knowledge. The user
may adopt a set of guardrails G from existing relevant liter-
ature or design new ones informed by expert feedback.
Empirical Alignment Data D:
To align LLM behavior
with expert expectations, the user must define an alignment
dataset D = {xD, yD}, where xD encodes prompt features
(e.g., building blocks capturing role, task, requirements, in-
structions in a prompt) and yD represents expert-informed
ground-truth outcomes (Fig. 1a). Subject-matter authorities,
such as policymakers, AI ethicists, or domain experts, de-
fine these outcomes using domain knowledge, empirical ev-
idence, and ethical considerations. To ensure D reflects ex-
pert knowledge, ground-truth labels should come directly
from experts or represent real-world outcomes validated by
experts. The alignment dataset D should also promote equal
opportunity and fairness (e.g., it should be demographically
balanced). Users may consult experts to create and curate
such datasets or select existing ones. Our method assumes D
accurately reflects the intended alignment outcomes, though
verifying its correctness is beyond this paper’s scope.
LLM M:
The user must select a pre-trained off-the-shelf
LLM (e.g., GPT, PaLM, Gemini, LLaMA, Claude, FLAN-
T5) (Chang et al. 2024). Although our model-agnostic
method works with any LLM, the guardrails it evaluated and
selected for one LLM may not generalize across models due
to variations in architecture, training data, and sensitivity to
different guardrails. We define an outcome ˆy = M(x; θ)
that encodes the prediction output from an LLM M for
prompt constructed from prompt features x, given guardrail
activation probability vector θ (Fig. 1b).
System Prompts and User Prompts:
To probe the LLM,
the user must define system prompts and craft user prompts
(Fig. 1b). System prompts specify guardrail constraints, in-
cluding the model’s role, task, requirements, etc. In addition
to guardrails for evaluation, the system prompt may contain
other instructions that should be fixed across all queries to
the LLM to isolate the effect of the guardrails. For example,
such information could assign the LLM a consistent persona
(e.g., “You are a resume evaluator”) to standardize its out-
put (Zheng et al. 2024). User prompts contain tailored inputs
from the alignment data D to elicit LLM responses.
Guardrails G for Evaluation:
The user must adopt a set
of guardrails, G = {G1, G2, G3, . . . , GN} for evaluation.
They can choose these guardrails by consulting existing sub-
ject matter experts, reviewing literature, or implementing
new ones by identifying LLM limitations (Fig. 1b). These
guardrails may include alignment constraints, counter-bias
measures, etc. Our preliminary experiments suggested that
guardrail order (e.g., Gi preceding Gj, or Gj preceding Gi)
can influence LLM outputs. However, we found no conclu-
sive evidence that LLMs systematically prioritize guardrails
by order. Nevertheless, to mitigate potential order effects,
we randomize guardrail sequences in our method.
Task-specific Surrogate Model to Mimic LLM
Querying an LLM for every record across all guardrail
combinations is computationally expensive due to token
pricing, request limits, and latency, with costs scaling as
2N × R for R records and N guardrails. To reduce this,
users can optionally train a surrogate Deep Neural Network
(DNN) (Shree et al. 2024; Pangakis and Wolken 2024) that
predicts task-specific outcomes from encoded prompt fea-
tures, enabling faster and cheaper per-query evaluation. This
choice is driven by online LLM query cost and latency rather
than training cost, as DNNs also incur some overhead. If
LLMs run locally with low latency and no token pricing,
or if online LLM cost and query time are not concerns, our
method can be applied directly without a surrogate DNN.
Need For Surrogate Model:
We emphasize that train-
ing a surrogate model is optional for accelerating queries,
and not a methodological requirement for selecting effec-
tive guardrails. Our method is model-agnostic and can di-
rectly work with offline LLMs with low latency and no token
pricing, or when an online LLM query cost is manageable.
Also, we do not claim that the surrogate approximates the
full LLM capabilities, as it only mimics LLM’s task-specific
behavior (e.g., prediction) under controlled prompting. Al-
though we train the surrogate for prediction tasks in this pa-
per, the same approach can extend to other tasks (e.g., text
generation), depending on the nature of the LLM outputs
and how well they can be structured for supervised learning.
Input Data Preprocessing:
The user must preprocess the
alignment dataset D to create separate training and test sets
with structured feature representations suitable for the sur-
rogate model. While LLMs operate on natural language
prompt features x derived from the raw records xD ⊂D,
DNNs require standardized, encoded inputs xencoded. Thus,
the user must transform the raw records into encoded fea-
tures (e.g., by one-hot encoding categorical variables and
normalizing continuous variables to a fixed range, such as
[0, 1]). Missing values can be addressed either by discard-
ing affected records or by imputation, using strategies such
as mean, median, or K-nearest neighbors. Finally, each en-
coded input vector must be paired with a binary guardrail
activation indicator vector g ∈{0, 1}N indicating which
guardrails were activated during the original LLM query us-
ing the corresponding system and user prompt.
Ground Truth:
Since the surrogate DNN is intended to
mimic the LLM’s task-specific behavior (e.g., prediction)
across different guardrail combinations, it must be trained
on structured LLM-generated outcomes rather than expert-
labeled ground truth from D. To obtain these, the user should
query the LLM using the original prompt features and cor-
responding guardrails aligned with the encoded DNN in-
puts. Based on the task, each LLM response should then
be mapped to a structured outcome label (e.g., binary or
multi-class) using task-specific keyword matching, regular
expressions, or other postprocessing heuristics. These label
mappings must be applied consistently across records and be
robust to variation in LLM outputs. The resulting structured
labels serve as ground truth for training the DNN surrogate.
707

--- Page 4 ---

Surrogate Model Training and Testing:
The DNN’s
training and testing sets should capture diverse guardrail
activation patterns. Having R raw records (e.g., selected
among inputs xD ⊂D) and N guardrails results in 2N × R
prompt–guardrail combinations. This is typically too large
and prohibitively expensive to query exhaustively from an
online LLM just to generate DNN training labels.
To address this, users can instead sample a representative
subset ˜D = {(xi, gi)} ⊆D × {0, 1}N from all possible
combinations of prompts and guardrail activation indicator
vectors using random or stratified sampling. Stratified sam-
pling helps ensure sufficient representation across guardrail
configurations. The collected samples can then be split into
training, validation, and testing (e.g., 60%/10%/30% split).
Users can tune the surrogate DNN. For example, to vali-
date our method, we tuned our surrogate DNNs using grid-
search cross-validation with early stopping, varying layers,
neurons, learning rates, activations, batch sizes, dropout, and
optimizers (see “Validation and Results”). We chose grid
search for its consistency and search coverage. Users may
also use automated tuning tools, which may yield slightly
different DNN parameters without affecting evaluation.
Modeling Guardrail Activation
We model guardrail activation probabilities as a vector of
Bernoulli parameters θ, with its distribution capturing un-
certainty in guardrail activation. Sampling from it can help
identify guardrail combinations that improve alignment.
Empirical Distribution of Outputs ˆpy({yD}):
We con-
struct an empirical distribution of outcomes ˆpy({yD}) from
all outputs {yD} of the alignment dataset D (Fig. 1a). This
serves as the target distribution for aligning the LLM’s out-
put to identify the optimal combination of guardrails and
will be used later to define the Bayesian likelihood.
Guardrail Activation Probability θ:
We represent the
stochastic activation of each guardrail using a probability
vector θ = [θ1, θ2, . . . , θN], where each θi represents the
activation probability of guardrail Gi when prompting the
LLM for a specific task (e.g., binary classification):
θi = P(gi = 1) = 1 −P(gi = 0),
(1)
where gi is a binary guardrail activation indicator vector,
with gi = 1 when guardrail Gi is active or gi = 0 otherwise.
Hence, each guardrail is activated through a biased coin flip
with activation probability θi simulated by Bernoulli trials.
Prior Distribution P(θ):
The prior distribution P(θ)
characterizes the initial uncertainty in θ before seeing any
data. We select a truncated normal prior that favors θ values
closer to 0.5; i.e., centering around a fair coin where each
guardrail is equally likely to be activated or deactivated:
P(θ) ∼T N(θ; µ = 0.5, σ = 0.5, [0, 1]),
(2)
where each θi is truncated to the interval [0, 1]. Our prior is
not tailored to the alignment dataset; it reflects a belief in the
initial neutrality of the guardrails. This flexible prior allows
the posterior to meaningfully update based on evidence from
the alignment dataset without being overly restrictive.
For robustness, we tested three priors: 1) a truncated
Laplace prior centered at 0.5 to emphasize central mass, 2) a
uniform prior representing maximum initial uncertainty over
θ, and 3) a wide Gaussian prior (µ = 0.5, σ = 2), reflect-
ing high but not maximal uncertainty about θ with a slight
initial preference to neutrality. Across all priors, posterior in-
ference produces consistent results: posterior means ≫0.5
trigger stronger guardrail activation, ≪0.5 to stronger deac-
tivation, and ≈0.5 indicates low/no impact or indifference,
suggesting our method is robust to reasonable prior choices.
Bayesian Likelihood P({yD}|θ):
We define the likeli-
hood based on the empirical output distribution constructed
from the ensemble of samples in the alignment dataset D:
P({yD}|θ) ∝
1
DKL(ˆpy({yD}) ∥ˆpy({ˆy}; θ)),
(3)
where ˆpy({ˆy}; θ) is similar to the desired empirical distribu-
tion of outputs ˆpy({yD}) except now constructed from LLM
predictions {ˆy} = M({x}; θ), where prompts {x} are de-
rived from inputs {xD} of the alignment dataset D, and DKL
is the Kullback–Leibler divergence (KLD) (Fig. 1c) (Kull-
back and Leibler 1951). Since a lower KLD implies more
similar distributions, we use the inverse of KLD as a proxy
for Bayesian likelihood estimation (MacKay 2002; Kato,
Imaizumi, and Minami 2023). Thus, a ˆpy({ˆy}) more sim-
ilar to that from the alignment data ˆpy({yD}) yields a lower
KLD, and in turn higher likelihood. This choice reflects our
objective to evaluate which guardrails bring the model’s be-
havior closer to the expert-informed output distribution.
Posterior Distribution P(θ|{yD}):
Finally, we obtain the
posterior distribution capturing the updated uncertainty in θ
after conditioning on the alignment dataset via Bayes’ rule:
P(θ|{yD}) = P({yD}|θ)P(θ)
P({yD})
,
(4)
where all terms are also dependent on {xD}, but omit-
ted for brevity. We use the Metropolis–Hastings Markov
chain Monte Carlo (MCMC) algorithm, implemented in the
PyMC3 library, to generate 10,000 samples from the pos-
terior distribution with 2,500 burn-in steps (Algorithm 1).
Each θ sample acts as a realization of the Bernoulli param-
eter, guiding a biased coin flip to determine whether the
corresponding guardrail is activated for each LLM query
(Fig. 1d). The user can also evaluate the distributional prop-
erties of the posterior (e.g., mean, variance, quantiles) to in-
terpret each guardrail’s activation confidence and its uncer-
tainty. For example, a posterior mean of θ deviating signifi-
cantly from 0.5 indicates a stronger probability of choosing
a biased coin—favoring either activation (mean ≫0.5) or
deactivation (mean ≪0.5) of the corresponding guardrail.
Guardrail Selection
We summarize the guardrail selection process in Algo-
rithm 2, using learned posterior distributions of θ. We
propose three alternative strategies for selecting which
guardrails to activate when predicting LLM outputs {ˆy}
from prompt features {x} derived from raw records {xD} of
708

--- Page 5 ---

Algorithm 1: Metropolis–Hastings MCMC for sampling the
Bayesian posterior of guardrail activation parameter θ
Input: Empirical alignment dataset D = {xD, yD}, prior
distribution P(θ) for guardrail activation
Parameter: Number of guardrails N, number of samples S,
number of chains C, burn-in steps B
Output: MCMC samples from the posterior distribution
P(θ|{yD}) after burn-in
1: Compute desired output distribution ˆpy({yD}) from the
empirical alignment data D for all records {xD}
2: for each chain c = 1 to C do
3:
Initialize θ(0) = [θ(0)
1 , . . . , θ(0)
N ] by jointly sampling
from prior P(θ) for all N guardrails
4:
for each iteration s = 1 to S + B do
5:
Propose new θ′ = [θ′
1, . . . , θ′
N] from proposal dis-
tribution (e.g., Gaussian centered at current chain
location θ(s−1))
6:
for each guardrail i = 1 to N do
7:
Perform Bernoulli coin toss with θ′
i as success
probability to activate or deactivate guardrail Gi
8:
end for
9:
With activated guardrails generate LLM outputs
{ˆy} = M({x}; θ′) using prompts {x} from {xD}
10:
Generate LLM output distribution with current
guardrail activation: ˆpy({ˆy}; θ′)
11:
Compute KLD between ˆpy({yD}) and ˆpy({ˆy}; θ′)
and approximately estimate likelihood P({yD}|θ′)
12:
Compute acceptance probability:
α = min

1,
P({yD}|θ′)P(θ′)
P({yD}|θ(s−1))P(θ(s−1))

13:
Accept θ′ with probability α; otherwise, reject by
setting θ(s) = θ(s−1)
14:
end for
15:
Discard first B samples from each chain as burn-in
16: end for
17: return Retain {θ(s)} after burn-in from all chains col-
lectively as samples from the posterior P(θ|{yD})
the empirical alignment dataset D. The user can then com-
pare resulting LLM outputs {ˆy} against expert-informed
ground truth labels {yD}, using a task-specific evaluation
metric of their choice to assess user-LLM alignment. When
D is already curated to ensure fairness (e.g., through demo-
graphic balancing) and has expert-informed labels, predic-
tive performance metrics (e.g., F1 score (Rijsbergen 1979))
can be used to evaluate how closely {ˆy} align with {yD}. If
not, fairness metrics (e.g., equalized odds, demographic par-
ity) (Hardt, Price, and Srebro 2016) may be better suited to
assess alignment through an equity lens.
In the Bernoulli toss and sample cut-off strategies, the
user samples a joint vector ˆθ = [ˆθ1, . . . , ˆθN] from the pos-
terior P(θ|{yD}), where each ˆθi represents the activation
probability of guardrail Gi, preserving posterior correla-
tions. In the Bernoulli toss, ˆθi is used as the success prob-
ability in a coin toss to decide whether to activate guardrail
Algorithm 2: Guardrail selection using different activation
strategies to enhance user-LLM alignment
Input: Alignment dataset D = {xD, yD} for evaluation;
posterior distribution P(θ|{yD}) over all guardrails
Parameter: Number of guardrails N, activation strategy ∈
{bernoulli toss, mean cutoff, sample cutoff}
Output: Selected guardrail vectors G and corresponding
LLM outputs ˆY for all records in D
1: if strategy = mean cutoff then
2:
For each guardrail Gi, compute posterior mean ¯θi =
E[θi] from the posterior distribution P(θi|{yD})
3: end if
4: Initialize G = [ ] {Stores selected guardrail vectors}
5: Initialize ˆY = [ ] {Stores corresponding LLM outputs}
6: for each record (xD, yD) ∈D do
7:
Initialize binary guardrail vector g = [ ]
8:
if strategy ∈{bernoulli toss, sample cutoff}
then
9:
Sample joint vector ˆθ = [ˆθ1, . . . , ˆθN] from the pos-
terior P(θ|{yD}) {Sample jointly to preserve pos-
terior correlations among N guardrail activations}
10:
end if
11:
for each guardrail Gi, where i = 1, . . . , N do
12:
if strategy = bernoulli toss then
13:
Perform Bernoulli coin toss with success proba-
bility ˆθi {similar to tossing a fair or biased coin}
14:
Set gi = 1 if toss is heads, else gi = 0
15:
else if strategy = sample cutoff then
16:
Set gi = 1 if ˆθi > 0.5, else gi = 0
17:
else if strategy = mean cutoff then
18:
Set gi = 1 if ¯θi > 0.5, else gi = 0
19:
end if
20:
Append gi to g
21:
end for
22:
Build prompt x using xD and g to get LLM output ˆy
23:
Append g to G and ˆy to ˆY
24: end for
25: return G and ˆY
Gi. In the sample cut-off, ˆθi is compared directly to a thresh-
old (typically 0.5): the guardrail is activated if ˆθi > 0.5.
In the mean cut-off strategy, the user does not need to
sample. Instead, they precompute the posterior mean ¯θi =
E[θi] for each guardrail Gi and activate the guardrail if ¯θi >
0.5. This approach uses the expected value of the posterior,
either computed analytically if parameters are known or by
fitting a parametric distribution to MCMC samples.
Limitations
Although our guardrail selection method provides a system-
atic framework for aligning LLM outputs with user expecta-
tions, it has limitations. If the alignment dataset D is biased,
incomplete, or poorly curated, our method will still function,
but resulting alignments will reflect those flaws. As with any
alignment method relying on gold-standard ground truths,
creating high-quality expert-informed datasets requires sig-
709

--- Page 6 ---

nificant effort. Since preparing such data is beyond this pa-
per’s scope, we used publicly available datasets already cu-
rated with expert input (e.g., professional resume assess-
ments, real recidivism outcomes). Where such data is un-
available, we recommend involving domain experts and fol-
lowing established data curation best practices.
While the posterior distribution of θ provides insights into
each guardrail’s effectiveness and uncertainty, users without
a statistics background may struggle with probabilistic data
and visualizations (Prabhudesai et al. 2023). Here, we as-
sume that our target users (i.e., guardrail engineers) can in-
terpret uncertainty from probability distributions. Also, we
used our method to evaluate guardrails globally to deter-
mine which are accepted or rejected for alignment, but we
did not apply it to analyze local (individual input–output) or
cohort-level (subgroup) influences on LLM outputs.
Three authors, two Computer Science and Engineering re-
searchers and one Mechanical Engineering researcher, con-
ducted quantitative evaluations. Two external researchers in-
formed dataset selection and alignment criteria, but we did
not conduct a qualitative evaluation with domain experts
(e.g., resume reviewers or criminal justice experts), whose
input could further strengthen user–LLM alignment.
Using the surrogate model consistently across guardrail
configurations reduces LLM approximation bias and accel-
erates evaluation due to low DNN query costs. However, our
model-agnostic method can also run on offline LLMs with-
out token costs or online LLMs when latency and pricing
allow. To manage combinatorial explosions, users can batch
guardrails by related alignment goals or strong interactions,
reducing evaluation burden while maintaining flexibility.
We selected moderation guardrails to evaluate our method
in two high-stakes tasks (resume quality and recidivism pre-
diction), where user-LLM alignment is critical. While our
method generalizes to other guardrail types (e.g., jailbreak
prevention, hallucination reduction) and goals (e.g., safety,
security), doing so requires domain-specific data and align-
ment criteria. In domains with contested goals, such as po-
litical discourse or policy moderation, the main challenge is
defining alignment targets, not applying our method.
Validation and Results
We conducted a series of quantitative experiments to val-
idate our method’s ability to select effective and reject
ineffective guardrails for user-LLM alignment. Acting as
guardrail engineers, we evaluated our method using two
publicly available datasets in two real-world applications:
1) aligning LLM decisions with expert knowledge to pro-
mote equal opportunity in hiring (Bertrand and Mullainathan
2004), and 2) fairness in criminal justice (Angwin et al.
2016). We also consulted two researchers in computational
law and algorithmic accountability to select datasets, define
alignment criteria, and review initial guardrails, though they
did not label ground truths or serve as co-authors.
Our method provides a Bayesian, quantitative approach to
evaluating and selecting effective guardrails. Instead of bi-
nary on/off decisions, our posteriors yield probability distri-
butions capturing uncertainty and evidence strength, guiding
task-specific guardrail selection or rejection.
Validation LLM
To validate our method, we used U-M GPT, our institu-
tional LLM with API access to GPT-4o. Although we used
the same LLM in both validation tasks, we varied its role
(e.g., resume quality or recidivism predictor) and guardrails
via system prompts for task-specific features (e.g., candidate
work experience, education, honors, volunteering, military
background, technical skills, and employment gaps for re-
sumes; defendant gender, ethnicity, age, prior convictions,
juvenile record, and charge degree for recidivism).
Interpreting Uncertainty in Posterior Distributions
As part of our validation, we present posterior distributions
P(θ|{yD}) for each guardrail’s activation parameter θi. The
top density plots (e.g., Fig. 2) show the posterior mean and
94% Highest Density Interval (HDI), indicating the range
where the most credible 94% of posterior θ values lie, re-
flecting uncertainty in the likelihood of guardrail activation.
We sampled joint vectors ˆθ = [ˆθ1, . . . , ˆθN] from the pos-
terior P(θ|{yD}), using ˆθi as the success probability in a
Bernoulli trial to decide guardrail activation. Repeating this
1,000 times yielded histograms of activation outcomes (e.g.,
bottom plots in Fig. 2), revealing how often each guardrail
is selected vs. rejected and which combinations best align
model outputs with expert expectations.
Baseline Strategies for Guardrail Selection
We compared our guardrail selection methods against two
baselines (Table 2 and Table 4). The first uses the LLM
without guardrails as a reference to assess alignment and
predictive performance against expert-labeled ground truths.
The second, “fixed best guardrail combination”, exhaus-
tively evaluates all 2N combinations, selects the one with
the highest F1 score, and applies it uniformly to all records.
While this provides an upper performance bound, it is com-
putationally expensive and ignores instance-level variation.
Our method outperforms it by sampling θ from the posterior
per record and activating guardrails probabilistically.
Evaluation Metric
The evaluation metric for our method targets task-specific
alignment—how well selected guardrails align LLM outputs
ˆy with expert knowledge. Although existing fairness met-
rics (Hardt, Price, and Srebro 2016) assess systemic bias,
our validation datasets D are demographically balanced and
include expert-informed ground truths yD labeled by experts
or validated real-world outcomes, reflecting fairness in the
alignment objective. We therefore use the F1 score (Rijsber-
gen 1979) (harmonic mean of precision and recall) to assess
the effectiveness of guardrail selection for user-LLM align-
ment. The first author computed all F1 scores, and all three
authors verified them through iterative discussions.
After learning posterior distributions over θ, the surrogate
model was no longer needed for validation. Instead, we used
posterior θ samples to select a guardrail configuration per
record, enabling direct LLM queries without evaluating all
combinations. We computed the final F1 scores by compar-
ing all {ˆy} against {yD} (Table 2 and Table 4).
710

--- Page 7 ---

Equal Opportunity in Hiring
Predicting resume quality improves candidates’ chances of
securing interviews and jobs. However, algorithmic assess-
ments risk bias from demographics (Arzaghi, Carichon, and
Farnadi 2025), pronouns (Ghosh and Caliskan 2023), or hir-
ing context (Li et al. 2021). Our pre-experiments showed
LLMs predicted gender and ethnicity from names with 0.9
and 0.98 F1 scores, respectively. We used this task to evalu-
ate how moderation guardrails align LLM-predicted resume
quality with expert assessments, promoting best hiring prac-
tices and equal opportunity regardless of gender or ethnicity.
Resume Quality Prediction Dataset:
We used a pub-
licly available dataset (Bertrand and Mullainathan 2004) D,
with resume quality (“high” or “low”) labeled by profes-
sional evaluators. This dataset contains an equal distribu-
tion of high- and low-quality resumes across genders and
ethnicities. It covers Chicago and Boston job postings from
2001–2002, with roles distributed across business (27%),
trade (21%), health/education/social services (15%), finance
(8%), manufacturing (8%), transport (3%), and other (18%).
Resume Quality Prediction Guardrails:
We imple-
mented guardrails GRQ (Table 1) based on expert hypothe-
ses (GRQ
1
and GRQ
2 ) and empirical findings (GRQ
3 ) from ex-
isting work (Bertrand and Mullainathan 2004) to align the
LLM predictions with key resume assessment criteria. We
also added guardrails (GRQ
4 , GRQ
5 , and GRQ
6 ) that explicitly
instruct the LLM to ignore names and avoid inferring demo-
graphics during predictions. We also included a distractor
guardrail (GRQ
7 ) that contradicts empirical findings (GRQ
3 ),
promoting features known to indicate low resume quality.
While guardrail engineers may not deploy such distractor
guardrails in practice since they are easily identifiable, we
still intentionally included them to test whether our method
can identify and reject them, simulating guardrail design
failures and serving as a robustness check.
ID
Guardrails to moderate resume quality predictions
Guardrail type
GRQ
1
When judging a candidate’s qualifications, use criteria such
as labor market experience, career profile, the existence of
gaps or holes in employment, and skills listed.
Expert hypothesis
(general features)
GRQ
2
High-quality resumes have the following: summer or while-
at-school employment experience, volunteering experience,
extra computer skills, certification degrees, foreign language
skills, honors, or some military experience.
Expert hypothesis
(specific criteria or
feature values)
GRQ
3
Higher-quality applicants have, on average, a little more la-
bor market experience and fewer holes in their employment
history; they are also more likely to have an e-mail address,
have completed a certification degree, possess foreign lan-
guage skills, or have been awarded some honors.
Empirical findings
(specific criteria or
feature values)
GRQ
4
When judging an applicant’s resume quality, do not consider
the applicant’s name, even if it is mentioned in the resume.
Counter bias
(applicant’s name)
GRQ
5
When judging an applicant’s resume quality, do not infer the
applicant’s gender from any features in the resume, and do
not consider it even if gender is mentioned in the resume.
Counter bias
(applicant’s gender)
GRQ
6
When judging an applicant’s resume quality, do not infer the
applicant’s ethnicity from any features in the resume, and do
not consider it even if ethnicity is mentioned in the resume.
Counter bias
(applicant’s
ethnicity)
GRQ
7
Higher-quality applicants have, on average, less labor mar-
ket experience and more holes in their employment history;
they are also less likely to have an e-mail address, have not
completed a certification degree, do not possess foreign lan-
guage skills, or have not been awarded some honors.
Distractor for GRQ
3
(opposite criteria or
feature values)
Table 1: Guardrails applied to moderate LLM outputs for re-
sume quality prediction (Bertrand and Mullainathan 2004).
Resume Quality Prediction Using Surrogate Model:
In-
stead of querying the LLM directly 623,360 times (i.e., once
for each of the 4,870 unique resumes in our dataset and
27 = 128 unique guardrail activation indicator vectors g
for our 7 guardrails), we replicated LLM-predicted resume
quality using a surrogate DNN model. Our surrogate DNN
consisted of three 64-unit ReLU layers with batch normal-
ization, dropout, and a sigmoid output trained via Adam.
We generated 102,400 DNN training samples by selecting
800 resumes for each of the possible 128 guardrail activa-
tion indicator vectors. To ensure balanced coverage across
guardrails, we used stratified sampling based on balanced
information acquisition principles (Krause and Guestrin
2005). To get binary LLM resume prediction labels (i.e.,
“ground truth”) for each of the samples, we queried the LLM
using a system prompt with the sample’s corresponding g
and a user prompt from the raw resume xD. We then created
the surrogate DNN dataset, with each record combining the
corresponding resume encoding xencode, guardrail activation
indicator vector g, and binary LLM prediction representing
one of the 102,400 samples. Using a 60%/10%/30% strat-
ified train/validation/test split, the grid-search-tuned model
achieved a 91% F1 score on the held-out test set.
Selecting Effective Guardrails:
We first investigated the
combined influence (Fig. 2) of all resume quality guardrails
from Table 1. Results show that GRQ
3
and GRQ
6
yield the
strongest alignment, highlighting the effectiveness of pairing
empirical evidence-focused guardrails with demographic
bias mitigation. In contrast, adding GRQ
7
reduced alignment,
likely due to conflicting emphasis with GRQ
3 . We then con-
ducted an ablation analysis to explore guardrail interactions.
Identifying Complementary Guardrails:
We consider
GRQ
1
and GRQ
2
together since both stem from expert hypothe-
sis (Fig. 3). GRQ
1
identifies general features (e.g., work expe-
rience, skills) for resume quality but not their specific values,
slightly helping alignment. GRQ
2
specifies feature values as-
sociated with high-quality resumes, yielding stronger align-
ment. Together, GRQ
1
ensures broad coverage, while GRQ
2
sharpens focus on key indicators, creating a balanced mix.
Identifying Individual Optimal Contributions:
Next,
we compared expert hypothesis-based guardrails (GRQ
1
and
GRQ
2 ) with the empirical evidence-based guardrail GRQ
3
(Fig. 4). Even though GRQ
1 , GRQ
2 , and GRQ
3
individually per-
form well, combining multiple overlapping guardrails can
introduce redundancy and lead to diminishing returns. Re-
sults show that GRQ
3 , which directly encodes high-quality re-
sume features based on evidence, is the most effective. How-
ever, adding GRQ
1
and GRQ
2
introduces redundancy.
Rejecting Distractor Guardrails:
Since GRQ
3
showed
the strongest alignment, we tested it against a distrac-
tor guardrail GRQ
7
(Fig. 5). GRQ
7
contradicts hiring crite-
ria, claiming high-quality candidates have negative features
(e.g., employment gaps). Our method selected GRQ
3
(empiri-
cal evidence-based) and rejected GRQ
7
(distractor).
711

--- Page 8 ---

(b)
(c)
(d)
Sample
Tails (0)
Heads (1)
𝐺!
"#off
𝐺$
"#off
𝐺!
"#on
𝐺$
"#on
Tails (0)
Heads (1)
𝐺%
"#off
𝐺%
"#on
(e)
(f)
(g)
Tails (0)
Heads (1)
𝐺&
"#off
𝐺&
"#on
Tails (0)
Heads (1)
𝐺'
"#off
𝐺'
"#on
Tails (0)
Heads (1)
𝐺(
"#off
𝐺(
"#on
𝑚𝑒𝑎𝑛= 0.37
94% 𝐻𝐷𝐼
0.0 0.2 0.4 0.6 0.8 1.0
Sample
Sample
Sample
Sample
Sample
65.3%
34.7%
65.2%
34.8%
56.8%
43.2%
58.4%
41.6%
48.5%
51.5%
67.3%
32.7%
𝑚𝑒𝑎𝑛= 0.36
𝑚𝑒𝑎𝑛= 0.64
𝑚𝑒𝑎𝑛= 0.41
𝑚𝑒𝑎𝑛= 0.42
𝑚𝑒𝑎𝑛= 0.52
𝑚𝑒𝑎𝑛= 0.35
94% 𝐻𝐷𝐼
0.0 0.2 0.4 0.6 0.8 1.0
0.0 0.2 0.4 0.6 0.8 1.0
0.0 0.2 0.4 0.6 0.8 1.0
0.0 0.2 0.4 0.6 0.8 1.0
0.0 0.2 0.4 0.6 0.8 1.0
0.0 0.2 0.4 0.6 0.8 1.0
3.2𝑒)*&
0.78
0.76
7.9𝑒)*&
0.25
1
0.00043
0.83
0.00027
0.85
0.085
0.99
0.0001
0.75
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝= 𝜃! 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝=  𝜃$ 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝=  𝜃% 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝= 𝜃& 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝=  𝜃' 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝= 𝜃( 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝=  𝜃+ 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
Posterior of 𝜃+ for 𝐺+
"# (𝜇= 0.37)
Posterior of 𝜃! for 𝐺!
"# (𝜇= 0.36)
Posterior of 𝜃$ for 𝐺$
"#(𝜇= 0.64)
Posterior of 𝜃% for 𝐺%
"# (𝜇= 0.41)
Posterior of 𝜃& for 𝐺&
"#(𝜇= 0.42)
Posterior of 𝜃' for 𝐺'
"# (𝜇= 0.52)
Posterior of 𝜃( for 𝐺(
"#(𝜇= 0.35)
(a)
𝐺+
"#off
Tails (0)
Heads (1)
𝐺+
"#on
63.5%
36.5%
1000
800
600
400
200
0
Tails (0)
Heads (1)
94% 𝐻𝐷𝐼
94% 𝐻𝐷𝐼
94% 𝐻𝐷𝐼
94% 𝐻𝐷𝐼
94% 𝐻𝐷𝐼
1000
800
600
400
200
0
1000
800
600
400
200
0
1000
800
600
400
200
0
1000
800
600
400
200
0
1000
800
600
400
200
0
1000
800
600
400
200
0
Sample
𝜃
Density of 𝜃
Density of 𝜃
𝜃
Density of 𝜃
𝜃
Density of 𝜃
𝜃
Density of 𝜃
𝜃
Density of 𝜃
𝜃
Density of 𝜃
𝜃
Figure 2: Posterior distributions P(θ|{yD}) and 1,000 Bernoulli toss outcomes using sampled θ values as success probabilities
(p = θ) to decide activation of resume quality guardrails: (a) GRQ
1 , (b) GRQ
2 , (c) GRQ
3 , (d) GRQ
4 , (e) GRQ
5 , (f) GRQ
6 , and (g) GRQ
7 .
(a)
(b)
𝐺!
"#off
Tails (0)
Heads (1)
𝐺!
"#on
𝐺$
"#off
𝐺$
"#on
Tails (0)
Heads (1)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(p = 𝜃$ 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(p =  𝜃! 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
45.9%
54.1%
59.4%
40.6%
0.0 0.2 0.4 0.6 0.8 1.0
0.0 0.2 0.4 0.6 0.8 1.0
Posterior of 𝜃! for 𝐺!
"#(𝜇= 0.54)
Posterior of 𝜃$ for 𝐺$
"#(𝜇= 0.58)
𝑚𝑒𝑎𝑛= 0.54
94% 𝐻𝐷𝐼
0.1
1
𝑚𝑒𝑎𝑛= 0.58
94% 𝐻𝐷𝐼
0.14
1
Sample
1000
800
600
400
200
0
Sample
1000
800
600
400
200
0
𝜃
Density of 𝜃
𝜃
Density of 𝜃
Figure 3: Our method effectively selected complementary
resume quality guardrails: a) GRQ
1
and b) GRQ
2 .
(a)
(b)
(c)
𝐺!
"#off
Tails (0)
Heads (1)
𝐺!
"#on
Tails (0)
Heads (1)
𝐺$
"#off
𝐺$
"#on
Tails (0)
Heads (1)
𝐺%
"#off
𝐺%
"#on
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(p =  𝜃2 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(p =  𝜃3 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(p =  𝜃1 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
60.9%
39.1%
66.3%
33.7%
35.0%
65.0%
Posterior of 𝜃1 for 𝐺!
"#(𝜇= 0.38)
Posterior of 𝜃2 for 𝐺$
"#(𝜇= 0.36)
Posterior of 𝜃3 for 𝐺%
"#(𝜇= 0.64)
0.0
0.2 0.4 0.6 0.8 1.0
0.0
0.2 0.4 0.6 0.8 1.0
0.0
0.2 0.4 0.6 0.8 1.0
𝑚𝑒𝑎𝑛= 0.38
94% 𝐻𝐷𝐼
0.8
2.2𝑒)*+
94% 𝐻𝐷𝐼0.76
2.9𝑒)*+
𝑚𝑒𝑎𝑛= 0.36
𝑚𝑒𝑎𝑛= 0.64
0.24
1
94% 𝐻𝐷𝐼
Sample
1000
800
600
400
200
0
Sample
800
600
400
200
0
1000
Sample
800
600
400
200
0
1000
𝜃
Density of 𝜃
Density of 𝜃
𝜃
Density of 𝜃
𝜃
Figure
4:
When
combining
multiple
resume
quality
guardrails, our method rejected both a) GRQ
1
and b) GRQ
2
due
to overlapping features with c) GRQ
3 .
Influence of Counter-Bias Guardrails:
We compared
counter-bias guardrails for name (GRQ
4 ), gender ( GRQ
5 ),
and ethnicity (GRQ
6 ) (Fig. 6). GRQ
4
had the strongest im-
pact, as names are key demographic proxies, whereas the
effects of GRQ
5
and GRQ
6
were less pronounced—either be-
cause gender and ethnicity are not considered part of re-
sumes, even if disclosed, or the LLM already incorporates
in-built bias-mitigation guardrails. If names are removed
using an anonymization tool, our method would mark the
name-based guardrail indifferent, but the model could still
infer gender and ethnicity from proxy features like education
or work history, requiring stronger counter-bias guardrails.
(a)
(b)
𝐺!
"#off
Tails (0)
Heads (1)
𝐺!
"#on
𝐺$
"#off
𝐺$
"#on
Tails (0)
Heads (1)
Posterior of 𝜃! for 𝐺!
"#(𝜇= 0.64)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(p =  𝜃! 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(p =  𝜃$ 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
34.8%
65.2%
65.4%
34.6%
Posterior of 𝜃$ for 𝐺$
"#(𝜇= 0.36)
0.0 0.2 0.4 0.6 0.8 1.0
𝑚𝑒𝑎𝑛= 0.64
94% 𝐻𝐷𝐼
1
1.1𝑒%&'
𝑚𝑒𝑎𝑛= 0.36
0.25
0.76
94% 𝐻𝐷𝐼
0.0 0.2 0.4 0.6 0.8 1.0
Sample
1000
800
600
400
200
0
Sample
1000
800
600
400
200
0
𝜃
Density of 𝜃
Density of 𝜃
𝜃
Figure 5: Our method selected the best resume quality
guardrail a) GRQ
3
and rejected its opposite distractor b) GRQ
7 .
(a)
(b)
(c)
𝐺!
"#off
Tails (0)
Heads (1)
𝐺!
"#on
Tails (0)
Heads (1)
𝐺$
"#off
𝐺$
"#on
Tails (0)
Heads (1)
𝐺%
"#off
𝐺%
"#on
Posterior of 𝜃! for 𝐺!
"# (𝜇= 0.52)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝=  𝜃! 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝= 𝜃$ 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝= 𝜃% 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
47.5%
52.5%
50.2%
49.8%
52.2%
47.8%
Posterior of 𝜃$ for 𝐺$
"# (𝜇= 0.50)
Posterior of 𝜃% for 𝐺%
"#(𝜇= 0.51)
0.0 0.2 0.4 0.6 0.8 1.0
𝑚𝑒𝑎𝑛= 0.52
94% 𝐻𝐷𝐼
1
0.084
𝜃
Density of 𝜃
𝑚𝑒𝑎𝑛= 0.50
𝑚𝑒𝑎𝑛= 0.51
1
0.082
𝜃
Density of 𝜃
0.0 0.2 0.4 0.6 0.8 1.0
94% 𝐻𝐷𝐼
94% 𝐻𝐷𝐼
1
0.051
𝜃
0.0 0.2 0.4 0.6 0.8 1.0
Sample
1000
800
600
400
200
0
Sample
1000
800
600
400
200
0
Sample
1000
800
600
400
200
0
Density of 𝜃
Figure 6: Counter-bias resume quality guardrails: a) GRQ
4 , b)
GRQ
5 , and c) GRQ
6
showed limited impact likely due to LLM’s
training-stage bias mitigation of name, gender, or ethnicity.
LLM
Predictive
Performance:
Our
method
selects
guardrails that improve resume quality predictions (F1
score: 0.71) and align with expert labels {yD} (Table 2).
Fairness and Criminal Justice
Predicting recidivism (i.e., a defendant’s likelihood of reof-
fending) is critical in risk assessment, sentencing, and parole
decisions. We selected this task to assess how moderation
guardrails align LLM-predicted recidivism with actual reof-
fense outcomes while promoting fairness in criminal justice.
Recidivism Prediction Dataset:
To create our align-
ment dataset D, we used a publicly available COMPAS
712

--- Page 9 ---

Guardrail selection method for resume quality
F1 score
Model with no guardrail
0.65
Fixed best guardrail combination
0.68
Bayesian MCMC (mean of P(θ|{yD}) as cut-off)†
0.68
Bayesian MCMC (sampled θ as cut-off)†
0.69
Bayesian MCMC (Bernoulli toss with sampled θ)†
0.71
Table 2: LLM performance on resume quality prediction us-
ing our proposed† and baseline guardrail selection methods.
dataset (Mallari et al. 2020) of Broward County, Florida
criminal records from 2013–2014 (35.3% misdemeanors,
64.7% felonies). It reports whether defendants re-offended
within two years of initial screenings. We removed records
with missing outcomes (reducing 7,214 to 6,172) and ap-
plied up-sampling to ensure balanced recidivism outcomes
across gender and ethnicity (resulting in 7,310 records).
Recidivism
Prediction
Guardrails:
We
construct
guardrails GRC informed by COMPAS guide (Northpointe
2015) and existing literature findings (Dressel and Farid
2018; Mallari et al. 2020) on recidivism prediction (Ta-
ble 3). These guardrails emphasize established risk factors,
including prior criminal history (GRC
1 ), degree of involve-
ment (GRC
2 ), dynamic personality traits (GRC
3 ), and violent
behavior patterns (GRC
4 ). After consulting two external re-
searchers, we added counter-bias guardrails (GRC
5 , GRC
6 , and
GRC
7 ) to prevent the LLM from using the defendant’s name,
gender, or ethnicity. Although such demographic factors
are accessible to judges, they are not directly predictive
of recidivism risk. Since we already demonstrated in the
hiring task that our method can identify and reject distractor
guardrails, we did not repeat that analysis for this dataset.
ID
Guardrails to moderate recidivism prediction
Guardrail Type
GRC
1
Well-known recidivism risk factors involve criminal asso-
ciates, criminal personality, and drug involvement, accord-
ing to various prior studies of recidivism.
Empirical findings
(general factors)
GRC
2
The degree of criminal involvement has consistently
emerged as a major risk factor for predicting ongoing crim-
inal behavior. It is the most important of the major risk fac-
tors emerging in various meta-analysis studies. Early juve-
nile delinquency involvement is also linked to ongoing crim-
inal behavior, according to prior studies.
Empirical findings
(degree of criminal
involvement)
GRC
3
Criminal personality (e.g., impulsivity, no guilt, selfishness/-
narcissism, a tendency to dominate others, risk-taking, and a
history of violent behavior or aggression) is the second most
important dynamic factor in predicting recidivism.
Empirical findings
(characteristics of
criminal personality)
GRC
4
A history of violent behavior has been demonstrated to be
one of the most powerful predictors of future violence. The
likelihood of future violence appears to steadily increase
with each instance of a prior violent incident. Each prior ar-
rest for violent behavior increases the likelihood of further
violence. Similarly, a history of juvenile violence has been
found to be a predictor of adult violence.
Empirical findings
(prior history of
juvenile violence)
GRC
5
When predicting recidivism, do not consider the defendant’s
name, even if it is mentioned in the document.
Counter bias
(defendant’s name)
GRC
6
When predicting recidivism, do not infer the defendant’s
gender from any features in the resume, and do not consider
the defendant’s gender, even if mentioned in the document.
Counter bias
(defendant’s gender)
GRC
7
When predicting recidivism, do not infer the defendant’s
ethnicity and race from any features in the resume, and do
not consider the defendant’s ethnicity and race, even if these
are mentioned in the document.
Counter bias
(defendant’s
ethnicity and race)
Table 3: Guardrails applied to moderate LLM outputs for re-
cidivism prediction (Northpointe 2015; Mallari et al. 2020).
Recidivism Prediction Using Surrogate Model:
Instead
of querying the LLM directly 935,680 times (i.e., once for
each of the 7,310 unique defendants in our dataset and 27 =
128 unique guardrail activation indicator vectors g for our 7
guardrails), we replicated LLM-predicted recidivism using
a surrogate DNN model. The DNN consisted of five 64-unit
ReLU layers with batch normalization, dropout, and a sig-
moid output trained via Adam. We generated 153,600 DNN
training samples by selecting 1,200 defendant records for
each of the possible 128 guardrail activation indicator vec-
tors. To ensure balanced coverage across guardrails, we used
stratified sampling based on balanced information acquisi-
tion principles (Krause and Guestrin 2005). To get binary
LLM resume prediction labels (i.e., “ground truth”) for each
of the samples, we queried the LLM using a system prompt
with the sample’s guardrail activation vector and a user
prompt from the raw defendant record xD. We then created
the surrogate DNN dataset, with each record combining the
corresponding defendant record encoding xencode, guardrail
activation indicator vector g, and binary LLM prediction for
one of the 153,600 samples. Using a 60%/10%/30% strat-
ified train/validation/test split, the grid-search-tuned model
achieved a 93.4% F1 score on the held-out test set.
Selecting Effective Guardrails:
We applied our method
to all recidivism guardrails from Table 3 to assess their com-
bined influence (Fig. 7). The best alignment with D was
achieved using GRC
1 , GRC
2 , and GRC
4
that capture key pre-
dictive signals like prior criminal history, criminal involve-
ment, and violent behavior. In contrast, adding GRC
5 , GRC
6 ,
and GRC
7 , which were supposed to reduce biases, slightly re-
duced alignment, likely due to stricter exclusion criteria. To
further analyze guardrail interactions, we conducted ablation
experiments with selected subsets of guardrails.
Identifying Complementary Guardrails:
The COMPAS
practitioner’s guide-based guardrails (Northpointe 2015)
collectively improved model alignment in recidivism pre-
diction (Fig. 8). Our method selected GRC
1 , GRC
2 , and GRC
4
as the most effective combination, rejecting GRC
3 , likely due
to redundant overlapping features with GRC
1
and GRC
4 .
Identifying Counter-bias Guardrails
Our results show
that counter-bias guardrails (GRC
5 , GRC
6 , and GRC
7 ) did not
improve alignment and sometimes performed worse than us-
ing no guardrails (Fig. 9). These guardrails were designed
to suppress the influence of demographic attributes like de-
fendants’ names, genders, and ethnicity in recidivism pre-
diction. However, doing so may have removed useful con-
text, as such attributes can inform nuanced recidivism deci-
sions. This suggests that completely removing demographic
information may misalign with expert decisions, such as
those made by criminal justice decision-makers informed
by risk assessment tools (Larson et al. 2016; Northpointe
2015), who may legitimately consider such context. This
contrasts with resume screening, where demographic fea-
tures are more likely to introduce bias than reduce it.
LLM
Predictive
Performance:
Our
method
selects
guardrails that improve recidivism predictions (F1 score:
0.66) and align with expert labels {yD} (Table 4).
713

--- Page 10 ---

(a)
(b)
(c)
(d)
𝐺!
"#off
Tails (0)
Heads (1)
𝐺!
"#on
Tails (0)
Heads (1)
Tails (0)
Heads (1)
𝐺$
"#off
𝐺%
"#off
𝐺$
"#on
𝐺%
"#on
Tails (0)
Heads (1)
𝐺&
"#off
𝐺&
"#on
(e)
(f)
(g)
Tails (0)
Heads (1)
𝐺'
"#off
𝐺'
"#on
Tails (0)
Heads (1)
𝐺(
"#off
𝐺(
"#on
Tails (0)
Heads (1)
𝐺)
"#off
𝐺)
"#on
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝= 𝜃1 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝= 𝜃3 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝= 𝜃4 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝=  𝜃5 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝=  𝜃6 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝= 𝜃7 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝=  𝜃2 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
43.7%
56.3%
37.5%
62.5%
62.1%
37.9%
37.6%
62.4%
65.0%
35.0%
62.8%
37.2%
65.3%
34.7%
Posterior of 𝜃1 for 𝐺1
𝑅𝐶(𝜇= 0.56)
Posterior of 𝜃3 for 𝐺%
"#(𝜇= 0.37)
Posterior of 𝜃4 for 𝐺&
"#(𝜇= 0.64)
Posterior of 𝜃5 for 𝐺'
"#(𝜇= 0.36)
Posterior of 𝜃6 for 𝐺6
𝑅𝐶(𝜇= 0.36)
Posterior of 𝜃7 for 𝐺)
"#(𝜇= 0.36)
Posterior of 𝜃2 for 𝐺$
"#(𝜇= 0.63)
0.0 0.2 0.4 0.6 0.8 1.0
𝜃
Density of 𝜃
0.0 0.2 0.4 0.6 0.8 1.0
0.0 0.2 0.4 0.6 0.8 1.0
Density of 𝜃
𝜃
𝜃
Density of 𝜃
0.0 0.2 0.4 0.6 0.8 1.0
Density of 𝜃
𝜃
0.0 0.2 0.4 0.6
0.8 1.0
Density of 𝜃
𝜃
0.0 0.2 0.4 0.6
0.8 1.0
0.0 0.2 0.4 0.6 0.8 1.0
Sample
1000
800
600
400
200
0
Sample
1000
800
600
400
200
0
Sample
1000
800
600
400
200
0
Sample
1000
800
600
400
200
0
Sample
1000
800
600
400
200
0
Sample
1000
800
600
400
200
0
Density of 𝜃
Density of 𝜃
𝜃
𝜃
Sample
1000
800
600
400
200
0
𝑚𝑒𝑎𝑛= 0.56
94% 𝐻𝐷𝐼
1
0.11
𝑚𝑒𝑎𝑛= 0.63
𝑚𝑒𝑎𝑛= 0.37
𝑚𝑒𝑎𝑛= 0.64
𝑚𝑒𝑎𝑛= 0.36
𝑚𝑒𝑎𝑛= 0.36
𝑚𝑒𝑎𝑛= 0.36
94% 𝐻𝐷𝐼
1
0.22
94% 𝐻𝐷𝐼
0.00013
0.78
94% 𝐻𝐷𝐼
0.24
1
0.00029
0.76
0.00018
0.75
94% 𝐻𝐷𝐼
94% 𝐻𝐷𝐼
5.6𝑒34'
0.76
94% 𝐻𝐷𝐼
Figure 7: Posterior distributions P(θ|{yD}) and 1,000 Bernoulli toss outcomes using sampled θ values as success probabilities
(p = θ) to decide activation of recidivism guardrails: (a) GRC
1 , (b) GRC
2 , (c) GRC
3 , (d) GRC
4 , (e) GRC
5 , (f) GRC
6 , and (g) GRC
7 .
(a)
(b)
(c)
(d)
𝐺!
"#off
Tails (0)
Heads (1)
𝐺!
"#on
Tails (0)
Heads (1)
Tails (0)
Heads (1)
𝐺$
"#off
𝐺%
"#off
𝐺$
"#on
𝐺%
"#on
Tails (0)
Heads (1)
𝐺&
"#off
𝐺&
"#on
Posterior of 𝜃1 for 𝐺!
"#(𝜇= 0.56)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝=  𝜃1 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝= 𝜃3 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝= 𝜃4 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
Posterior of 𝜃2 for 𝐺$
"#(𝜇= 0.64)
Posterior of 𝜃3 for 𝐺%
"#(𝜇= 0.37)
Posterior of 𝜃4 for 𝐺&
"#(𝜇= 0.64)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝=  𝜃2 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
43.3%
56.7%
36.1%
63.9%
62.1%
37.9%
35.0%
65.0%
0.0 0.2 0.4 0.6 0.8 1.0 𝜃
Density of 𝜃
𝑚𝑒𝑎𝑛= 0.56
94% 𝐻𝐷𝐼
1
0.11
Density of 𝜃
𝜃
0.0 0.2 0.4 0.6 0.8 1.0
94% 𝐻𝐷𝐼
1
0.23
𝑚𝑒𝑎𝑛= 0.64
𝑚𝑒𝑎𝑛= 0.37
𝑚𝑒𝑎𝑛= 0.64
Density of 𝜃
𝜃
𝜃
Density of 𝜃
0.0 0.2 0.4 0.6 0.8 1.0
5.8𝑒+,-
0.77
94% 𝐻𝐷𝐼
94% 𝐻𝐷𝐼
0.0 0.2 0.4 0.6 0.8 1.0
0.25
1
Sample
1000
800
600
400
200
0
Sample
1000
800
600
400
200
0
Sample
1000
800
600
400
200
0
Sample
1000
800
600
400
200
0
Figure 8: Our method selects: a) GRC
1 , b) GRC
2 , and d) GRC
4 ,
and rejects c) GRC
3
likely due to overlaps with GRC
1
and GRC
4 .
Guardrail selection method for recidivism
F1 score
Model with no guardrail
0.62
Fixed best guardrail combination
0.63
Bayesian MCMC (mean of P(θ|{yD}) as cut-off)†
0.63
Bayesian MCMC (sampled θ as cut-off)†
0.65
Bayesian MCMC (Bernoulli toss with sampled θ)†
0.66
Table 4: LLM performance comparing our proposed† and
baseline guardrail selection methods to predict recidivism.
Discussion and Conclusion
In this work, we presented a probabilistic framework to eval-
uate and select output moderation guardrails for aligning
LLM outputs with expert user expectations. By leveraging
Bayesian inference, we estimated guardrail activation prob-
abilities and interpreted their contributions to model align-
ment both independently and in combination with others.
Our validation showed our method’s ability to identify ef-
fective guardrails, reject distractors, and address biases in
resume quality and recidivism prediction tasks. Our results
showed that our approach improves model alignment with
empirical data while enabling a nuanced understanding and
interpretation of how guardrails influence LLM outputs.
We found that it is not always true that guardrails that are
individually better will also work the same when combined
with other guardrails. Rather, sometimes, they may cancel
the effect of another guardrail. Also, if the base LLM model
has already aligned to expert expectations during its train-
ing, it may happen that a similarly constructed user guardrail
does not have much influence on changing the LLM outputs.
We demonstrated our method using moderation guardrails
to ensure equal opportunity in resume quality and fairness
(a)
(b)
(c)
𝐺!
"#off
Tails (0)
Heads (1)
𝐺!
"#on
Tails (0)
Heads (1)
Tails (0)
Heads (1)
𝐺$
"#off
𝐺%
"#off
𝐺$
"#on
𝐺%
"#on
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝= 𝜃5 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝= 𝜃6 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑝=  𝜃7 𝑓𝑟𝑜𝑚 𝑝𝑜𝑠𝑡𝑒𝑟𝑖𝑜𝑟)
Posterior of 𝜃5 for 𝐺5
𝑅𝐶 (𝜇= 0.47)
Posterior of 𝜃6 for 𝐺6
𝑅𝐶(𝜇= 0.42)
Posterior of 𝜃7 for 𝐺%"#(𝜇= 0.49)
53.2%
46.8%
57.1%
42.9%
52.3%
47.7%
0.0 0.2 0.4 0.6 0.8 1.0
0.0 0.2 0.4 0.6 0.8 1.0
0.0 0.2 0.4 0.6 0.8 1.0
𝜃
Density of 𝜃
𝑚𝑒𝑎𝑛= 0.47
Density of 𝜃
Density of 𝜃
𝜃
𝜃
𝑚𝑒𝑎𝑛= 0.42
𝑚𝑒𝑎𝑛= 0.49
94% 𝐻𝐷𝐼
0.91
0.00011
94% 𝐻𝐷𝐼
0.87
0.00017
94% 𝐻𝐷𝐼
0.92
0.0091
Sample
1000
800
600
400
200
0
Sample
1000
800
600
400
200
0
Sample
1000
800
600
400
200
0
Figure 9: Our method rejects counter-bias recidivism
guardrails: a) GRC
5 , b) GRC
6 , c) GRC
7 , suggesting that fully
ignoring demographic features may reduce alignment.
in recidivism prediction. However, future work should study
the applicability of our method to other guardrails (e.g., pre-
venting jailbreaking, hallucination) with different alignment
goals (e.g., security, safety, and adversarial robustness).
We conducted quantitative evaluations to select effective
guardrails. Future work could engage domain experts for
qualitative studies and integrate explanation tools to improve
local (per-resume) and cohort-level (across-demographics)
interpretability of guardrail effects toward alignment.
Our method could target domain experts, AI ethicists,
policymakers, and industry practitioners, depending on the
alignment task and evaluation criteria. Since alignment goals
may differ or even conflict across stakeholders, our method
emphasizes defining the alignment objective and target au-
dience first. If the alignment task involves regulatory com-
pliance (e.g., U.S. federal AI governance (U.S. Congress
2024), the EU AI Act (European Parliament and Coun-
cil 2024)), our method can systematically extend to eval-
uate guardrails designed to meet such policies, provided
the alignment dataset incorporates expert input from poli-
cymakers. This could support auditability, traceability, and
non-discrimination in high-risk applications.
Future work should explore scaling our approach to larger
datasets, complex tasks, and adaptive guardrail configura-
tions that respond to evolving user needs. These efforts
will further improve “user-LLM” alignment and enhance the
practical and ethical deployment of LLM-based decision-
support systems in high-stakes real-world applications.
714

--- Page 11 ---

Ethical Statement
This research aligns with AIES’s commitment to ethical
AI development by ensuring responsible dataset usage and
mitigating potential societal harms. We evaluate and se-
lect guardrails to improve “user-LLM” alignment in high-
stakes decision-making, particularly in domains like hiring
and criminal justice. Our method relies on publicly available
datasets, following ethical guidelines. While our approach
aims to reduce biases, we acknowledge that no method can
fully eliminate unintended harms. Future work will explore
additional security-focused guardrails, alternative alignment
strategies, and broader societal implications to enhance the
responsible deployment of LLMs in decision-making.
Broader Impact
While our method aims to improve alignment in LLM-
driven decision-making with standards set by subject matter
authority experts, we need to be aware of unintended risks
if misapplied. There is a risk that probabilistically selected
guardrails may be treated as universally valid, potentially
reinforcing dominant norms and marginalizing alternative
viewpoints. Institutions and organizations could use align-
ment claims to justify biased practices if alignment goals are
narrowly defined or poorly contextualized. We urge practi-
tioners to apply this method with transparency, domain ex-
pertise, inclusive, and broader stakeholder engagement.
Positionality Statement
As researchers in human-centered AI, we acknowledge our
positionality in shaping the design, evaluation, and interpre-
tation of this work. Our interdisciplinary background spans
computer science, human-computer interaction (HCI), com-
putational modeling, and uncertainty quantification (UQ),
informing our approach to aligning LLM behavior with ex-
pert expectations in high-stakes domains. While we are not
domain experts in hiring or criminal justice, we grounded
our work in established literature, followed ethical guide-
lines, got researchers’ feedback, and consulted relevant em-
pirical findings to design alignment datasets and guardrails.
We recognize that value judgments and sociotechnical con-
text play a role in defining “expert user expectations,” and
we aim to make our methods transparent and adaptable to di-
verse perspectives. Our goal is to support AI practitioners in
critically evaluating and selecting moderation guardrails that
reflect AI fairness and accountability in decision-making.
Declaration on the Use of AI
For our experiments, we used our institutional LLM, U-M
GPT, provided by the University of Michigan, with API ac-
cess to the GPT-4o model to evaluate and select effective
guardrails that better align LLM behaviors with expert user
expectations. We did not use generative AI tools to write,
revise, or generate this paper. All text, analysis, and figures
were produced by the authors.
Acknowledgements
We thank members of the Computational HCI (CompHCI)
Lab at the University of Michigan for informal brainstorm-
ing. We thank Divya Ramesh and Nel Escher for informing
the dataset selection and alignment criteria, and Tsedeniya
Amare for proofreading the paper.
References
Angwin, J.; Larson, J.; Mattu, S.; and Kirchner, L. 2016.
Machine Bias: There’s software used across the country
to predict future criminals. And it’s biased against blacks.
ProPublica.
Arzaghi, M.; Carichon, F.; and Farnadi, G. 2025. Under-
standing Intrinsic Socioeconomic Biases in Large Language
Models, 49–60. AAAI Press.
Arzberger, A.; Buijsman, S.; Lupetti, M. L.; Bozzon, A.; and
Yang, J. 2025. Nothing Comes without Its World - Practi-
cal Challenges of Aligning LLMs to Situated Human Values
through RLHF. In Proc. of the 2024 AAAI/ACM Conference
on AI, Ethics, and Society, AIES ’24, 61–73. AAAI Press.
Awad, E.; Dsouza, S.; Kim, R.; Schulz, J.; Henrich, J.; Shar-
iff, A.; Bonnefon, J.-F.; and Rahwan, I. 2018. The Moral
Machine experiment. Nature, 563: 59–64.
Bender, E. M.; Gebru, T.; McMillan-Major, A.; and
Shmitchell, S. 2021.
On the Dangers of Stochastic Par-
rots: Can Language Models Be Too Big? In Proceedings of
the 2021 ACM Conference on Fairness, Accountability, and
Transparency, FAccT ’21, 610–623. New York, NY, USA.
ISBN 9781450383097.
Bertrand, M.; and Mullainathan, S. 2004. Are Emily and
Greg More Employable Than Lakisha and Jamal? A Field
Experiment on Labor Market Discrimination.
American
Economic Review, 94(4): 991–1013.
Boggust, A.; Hoover, B.; Satyanarayan, A.; and Strobelt, H.
2022. Shared Interest: Measuring Human-AI Alignment to
Identify Recurring Patterns in Model Behavior. In Proceed-
ings of the 2022 ACM CHI Conference on Human Factors in
Computing Systems, CHI ’22. New York, NY, USA. ISBN
9781450391573.
Chang, Y.; Wang, X.; Wang, J.; Wu, Y.; Yang, L.; Zhu, K.;
Chen, H.; Yi, X.; Wang, C.; Wang, Y.; Ye, W.; Zhang, Y.;
Chang, Y.; Yu, P. S.; Yang, Q.; and Xie, X. 2024. A Sur-
vey on Evaluation of Large Language Models. ACM Trans.
Intell. Syst. Technol., 15(3).
Chiang, C.-W.; Lu, Z.; Li, Z.; and Yin, M. 2023. Are Two
Heads Better Than One in AI-Assisted Decision Making?
Comparing the Behavior and Performance of Groups and In-
dividuals in Human-AI Collaborative Recidivism Risk As-
sessment. In Proceedings of the 2023 CHI Conference on
Human Factors in Computing Systems, CHI ’23. New York,
NY, USA. ISBN 9781450394215.
Chiang, C.-W.; Lu, Z.; Li, Z.; and Yin, M. 2024.
En-
hancing AI-Assisted Group Decision Making through LLM-
Powered Devil’s Advocate. In Proceedings of the 29th ACM
International Conference on Intelligent User Interfaces, IUI
’24. NY. ISBN 9798400705083.
Chivukula, S. S.; Gray, C.; Li, Z.; Pivonka, A. C.; and Chen,
J. 2024. Surveying a Landscape of Ethics-Focused Design
Methods. ACM J. Responsib. Comput., 1(3).
715

--- Page 12 ---

Chu, Z.; Wang, Y.; Li, L.; Wang, Z.; Qin, Z.; and Ren, K.
2024. A Causal Explainable Guardrails for Large Language
Models. In Proceedings of the 2024 on ACM SIGSAC Con-
ference on Computer and Communications Security, CCS
’24. NY. ISBN 9798400706363.
Cornacchia, G.; Zizzo, G.; Fraser, K.; Hameed, M. Z.;
Rawat, A.; and Purcell, M. 2025.
MoJE: Mixture of
Jailbreak Experts, Naive Tabular Classifiers as Guard for
Prompt Attacks, 304–315. AAAI Press.
Deshpande, A.; and Sharp, H. 2022. Responsible AI Sys-
tems: Who are the Stakeholders? In Proceedings of the 2022
AAAI/ACM Conference on AI, Ethics, and Society, AIES
’22, 227–236. New York, NY, USA: Association for Com-
puting Machinery. ISBN 9781450392471.
Dev, J.; Akhuseyinoglu, N.; Kayas, G.; Rashidi, B.; and
Garg, V. 2024.
Building Guardrails in AI Systems with
Threat Modeling. Digit. Gov.: Res. Pract. Just Accepted.
Dong, Y.; Mu, R.; Jin, G.; Qi, Y.; Hu, J.; Zhao, X.; Meng, J.;
Ruan, W.; and Huang, X. 2024. Position: building guardrails
for large language models requires systematic design.
In
Proceedings of the 41st International Conference on Ma-
chine Learning, ICML’24. JMLR.org.
Dressel, J.; and Farid, H. 2018. The accuracy, fairness, and
limits of predicting recidivism. Sci. Adv., 4(1): eaao5580.
Dutta, A.; Khorramrouz, A.; Dutta, S.; and KhudaBukhsh,
A. R. 2024.
Down the toxicity rabbit hole: a framework
to bias audit large language models with key emphasis on
racism, antisemitism, and misogyny. In Proceedings of the
Thirty-Third International Joint Conference on Artificial In-
telligence, IJCAI ’24. ISBN 978-1-956792-04-1.
Estrada, D. 2018. Value Alignment, Fair Play, and the Rights
of Service Robots. In Proceedings of the 2018 AAAI/ACM
Conference on AI, Ethics, and Society, AIES ’18, 102–107.
New York, NY, USA: Association for Computing Machin-
ery. ISBN 9781450360128.
European Parliament and Council. 2024. Regulation (EU)
2024/1689 of the European Parliament and of the Coun-
cil of 13 June 2024 laying down harmonised rules on
artificial intelligence (Artificial Intelligence Act).
Offi-
cial Journal of the European Union, L, 12.7.2024, p. 1–
254, https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=
CELEX%3A32024R1689.
Fang, C.; Qin, C.; Zhang, Q.; Yao, K.; Zhang, J.; Zhu,
H.; Zhuang, F.; and Xiong, H. 2023.
RecruitPro: A Pre-
trained Language Model with Skill-Aware Prompt Learn-
ing for Intelligent Recruitment.
In Proceedings of the
29th ACM SIGKDD Conference on Knowledge Discovery
and Data Mining, KDD ’23. New York, NY, USA. ISBN
9798400701030.
Gabriel, I. 2020. Artificial Intelligence, Values, and Align-
ment. Minds and Machines, 30(3).
Ghosh, S.; and Caliskan, A. 2023.
ChatGPT Perpetu-
ates Gender Bias in Machine Translation and Ignores Non-
Gendered Pronouns: Findings across Bengali and Five other
Low-Resource Languages.
In Proceedings of the 2023
AAAI/ACM Conference on AI, Ethics, and Society, AIES
’23, 901–912. New York, NY, USA: Association for Com-
puting Machinery. ISBN 9798400702310.
Gombolay, M. 2024. Human-robot alignment through inter-
activity and interpretability: don’t assume a ”spherical hu-
man”. In Proceedings of the Thirty-Third International Joint
Conference on Artificial Intelligence, IJCAI ’24. ISBN 978-
1-956792-04-1.
Hadfield-Menell, D.; Andrus, M.; and Hadfield, G. 2019.
Legible Normativity for AI Alignment: The Value of Silly
Rules. In Proceedings of the 2019 AAAI/ACM Conference
on AI, Ethics, and Society, AIES ’19, 115–121. New York,
NY, USA: Association for Computing Machinery.
ISBN
9781450363242.
Hadfield-Menell, D.; and Hadfield, G. K. 2019. Incomplete
Contracting and AI Alignment. In Proceedings of the 2019
AAAI/ACM Conference on AI, Ethics, and Society, AIES
’19, 417–422. New York, NY, USA: Association for Com-
puting Machinery. ISBN 9781450363242.
Hardt, M.; Price, E.; and Srebro, N. 2016. Equality of op-
portunity in supervised learning. In Proceedings of the 30th
International Conference on Neural Information Processing
Systems, NIPS’16, 3323–3331. Red Hook, NY, USA: Cur-
ran Associates Inc. ISBN 9781510838819.
Hrytsyna, A.; and Alves, R. 2024.
From Representation
to Response: Assessing the Alignment of Large Language
Models with Human Judgment Patterns. ACM Trans. Intell.
Syst. Technol. Just Accepted.
Inan, H.; Upasani, K.; Chi, J.; Rungta, R.; Iyer, K.; Mao,
Y.; Tontchev, M.; Hu, Q.; Fuller, B.; Testuggine, D.; and
Khabsa, M. 2023.
Llama Guard: LLM-based Input-
Output Safeguard for Human-AI Conversations.
ArXiv,
abs/2312.06674.
Iqbal, U.; Kohno, T.; and Roesner, F. 2025. LLM Platform
Security: Applying a Systematic Evaluation Framework to
OpenAI’s ChatGPT Plugins, 611–623. AAAI Press.
Kato, M.; Imaizumi, M.; and Minami, K. 2023.
Unified
Perspective on Probability Divergence via the Density-Ratio
Likelihood: Bridging KL-Divergence and Integral Probabil-
ity Metrics. In Ruiz, F.; Dy, J.; and van de Meent, J.-W., eds.,
Proceedings of The 26th International Conference on Artifi-
cial Intelligence and Statistics, volume 206 of Proceedings
of Machine Learning Research, 5271–5298. PMLR.
Krause, A.; and Guestrin, C. 2005. Near-Optimal Nonmy-
opic Value of Information in Graphical Models. In Proceed-
ings of the Twenty-First Conference on Uncertainty in Ar-
tificial Intelligence, UAI’05, 324–331. Arlington, Virginia,
USA: AUAI Press. ISBN 0974903914.
Kullback, S.; and Leibler, R. A. 1951. On information and
sufficiency.
The annals of mathematical statistics, 22(1):
79–86.
Lai, V.; Chen, C.; Smith-Renner, A.; Liao, Q. V.; and Tan, C.
2023. Towards a Science of Human-AI Decision Making:
An Overview of Design Space in Empirical Human-Subject
Studies. In Proceedings of the 2023 ACM Conference on
Fairness, Accountability, and Transparency, FAccT ’23. NY,
USA. ISBN 9798400701924.
716

--- Page 13 ---

Larson, J.; Mattu, S.; Kirchner, L.; and Angwin, J.
2016.
How We Analyzed the COMPAS Recidivism
Algorithm.
ProPublica.
Published May 9, 2016.
https://www.propublica.org/article/how-we-analyzed-
the-compas-recidivism-algorithm.
Li, L.; Lassiter, T.; Oh, J.; and Lee, M. K. 2021. Algorith-
mic Hiring in Practice: Recruiter and HR Professional’s Per-
spectives on AI Use in Hiring. In Proceedings of the 2021
AAAI/ACM Conference on AI, Ethics, and Society, AIES
’21, 166–176. New York, NY, USA: Association for Com-
puting Machinery. ISBN 9781450384735.
Li, T.; Khashabi, D.; Khot, T.; Sabharwal, A.; and Sriku-
mar, V. 2020. UNQOVERing Stereotyping Biases via Un-
derspecified Questions. In Cohn, T.; He, Y.; and Liu, Y., eds.,
Findings of the Association for Computational Linguistics:
EMNLP 2020, 3475–3489. Online: Association for Compu-
tational Linguistics.
Liu, Y.; Iter, D.; Xu, Y.; Wang, S.; Xu, R.; and Zhu, C. 2023.
G-Eval: NLG Evaluation using GPT-4 with Better Human
Alignment. arXiv:2303.16634.
MacKay, D. J. C. 2002. Information Theory, Inference &
Learning Algorithms. USA: Cambridge University Press.
ISBN 0521642981.
Mahomed, Y.; Crawford, C. M.; Gautam, S.; Friedler, S. A.;
and Metaxa, D. 2024. Auditing GPT’s Content Moderation
Guardrails: Can ChatGPT Write Your Favorite TV Show? In
Proceedings of the 2024 ACM Conference on Fairness, Ac-
countability, and Transparency, FAccT ’24. NY, USA. ISBN
9798400704505.
Mallari, K.; Inkpen, K.; Johns, P.; Tan, S.; Ramesh, D.; and
Kamar, E. 2020. Do I Look Like a Criminal? Examining
how Race Presentation Impacts Human Judgement of Re-
cidivism. In Proceedings of the 2020 CHI Conference on
Human Factors in Computing Systems, CHI ’20, 1–13. New
York, NY, USA. ISBN 9781450367080.
Norhashim, H.; and Hahn, J. 2024. Measuring Human-AI
Value Alignment in Large Language Models. Proceedings
of the AAAI/ACM Conference on AI, Ethics, and Society,
7(1): 1063–1073.
Norhashim, H.; and Hahn, J. 2025. Measuring Human-AI
Value Alignment in Large Language Models, 1063–1073.
AAAI Press.
Northpointe, I. 2015. Practitioner’s Guide to compas Core.
Pangakis, N.; and Wolken, S. 2024. Knowledge Distillation
in Automated Annotation: Supervised Text Classification
with LLM-Generated Training Labels. In Card, D.; Field,
A.; Hovy, D.; and Keith, K., eds., Proceedings of the Sixth
Workshop on Natural Language Processing and Computa-
tional Social Science (NLP+CSS 2024), 113–131. Mexico
City, Mexico: Association for Computational Linguistics.
Prabhudesai, S.; Yang, L.; Asthana, S.; Huan, X.; Liao,
Q. V.; and Banovic, N. 2023. Understanding Uncertainty:
How Lay Decision-Makers Perceive and Interpret Uncer-
tainty in Human-AI Decision Making. In Proceedings of
the 28th ACM International Conference on Intelligent User
Interfaces, IUI ’23, 379–396. New York, NY, USA. ISBN
9798400701061.
Rastogi, C.; Tulio Ribeiro, M.; King, N.; Nori, H.; and
Amershi, S. 2023. Supporting Human-AI Collaboration in
Auditing LLMs with LLMs.
In Proceedings of the 2023
AAAI/ACM Conference on AI, Ethics, and Society, AIES
’23, 913–926. New York, NY, USA: Association for Com-
puting Machinery. ISBN 9798400702310.
Rebedea, T.; Dinu, R.; Sreedhar, M. N.; Parisien, C.; and Co-
hen, J. 2023. NeMo Guardrails: A Toolkit for Controllable
and Safe LLM Applications with Programmable Rails. In
Feng, Y.; and Lefever, E., eds., Proceedings of the 2023 Con-
ference on Empirical Methods in Natural Language Pro-
cessing: System Demonstrations, 431–445. Singapore.
Rijsbergen, C. J. V. 1979.
Information Retrieval.
USA:
Butterworth-Heinemann, 2nd edition. ISBN 0408709294.
Robinson, P. 2023.
Action Guidance and AI Alignment.
In Proceedings of the 2023 AAAI/ACM Conference on
AI, Ethics, and Society, AIES ’23, 387–395. New York,
NY, USA: Association for Computing Machinery.
ISBN
9798400702310.
Shankar,
S.;
Zamfirescu-Pereira,
J.;
Hartmann,
B.;
Parameswaran, A.; and Arawjo, I. 2024.
Who Vali-
dates the Validators? Aligning LLM-Assisted Evaluation of
LLM Outputs with Human Preferences. In Proceedings of
the 37th ACM Symposium on User Interface Software and
Technology, UIST ’24. NY. ISBN 9798400706288.
Shneiderman, B. 2020. Bridging the Gap Between Ethics
and Practice: Guidelines for Reliable, Safe, and Trustworthy
Human-centered AI Systems. ACM Trans. Interact. Intell.
Syst., 10(4).
Shree, S.; Khadka, K.; Lei, Y.; Kacker, R. N.; and Kuhn,
D. R. 2024.
Constructing Surrogate Models in Machine
Learning Using Combinatorial Testing and Active Learn-
ing. In Proceedings of the 39th IEEE/ACM International
Conference on Automated Software Engineering, ASE ’24,
1645–1654. New York, NY, USA: Association for Comput-
ing Machinery. ISBN 9798400712487.
Terry, M.; Kulkarni, C.; Wattenberg, M.; Dixon, L.; and
Morris, M. R. 2024. Interactive AI Alignment: Specifica-
tion, Process, and Evaluation Alignment. arXiv:2311.00710.
U.S. Congress. 2024.
Federal A.I. Governance and
Transparency Act of 2024, H.R. 7532, 118th Congress
(2023–2024), amending Title 44 of the United States Code.
Public Law, March 2024. Text available at: https://www.
congress.gov/bill/118th-congress/house-bill/7532.
Adds
Subchapter IV—Artificial Intelligence System Governance
to Title 44, U.S. Code.
Varshney, K. R. 2025. Decolonial AI Alignment: Openness,
Vi´seundefineda-Dharma, and Including Excluded Knowl-
edges, 1467–1481. AAAI Press.
Wang, J.; Hu, H.; Wang, Z.; Yan, S.; Sheng, Y.; and He, D.
2024a. Evaluating Large Language Models on Academic
Literature Understanding and Review: An Empirical Study
among Early-stage Scholars.
In Proceedings of the 2024
ACM CHI Conference on Human Factors in Computing Sys-
tems, CHI ’24. New York, NY, USA. ISBN 9798400703300.
Wang, X.; Duan, S.; Yi, X.; Yao, J.; Zhou, S.; Wei, Z.;
Zhang, P.; Xu, D.; Sun, M.; and Xie, X. 2024b.
On the
717

--- Page 14 ---

essence and prospect: an investigation of alignment ap-
proaches for big models. In Proceedings of the Thirty-Third
International Joint Conference on Artificial Intelligence, IJ-
CAI ’24. ISBN 978-1-956792-04-1.
Wang, Z.; Yang, F.; Wang, L.; Zhao, P.; Wang, H.; Chen,
L.; Lin, Q.; and Wong, K.-F. 2024c. SELF-GUARD: Em-
power the LLM to Safeguard Itself. In Proceedings of the
2024 Conference of the North American Chapter of the As-
sociation for Computational Linguistics: Human Language
Technologies, 1648–1668. Mexico.
Yang, Z.; Wu, Y.; Wen, R.; Backes, M.; and Zhang, Y. 2025.
Peering Behind the Shield: Guardrail Identification in Large
Language Models. arXiv:2502.01241.
Yuan, Z.; Xiong, Z.; Zeng, Y.; Yu, N.; Jia, R.; Song, D.;
and Li, B. 2024. RigorLLM: resilient guardrails for large
language models against undesired content. In Proceedings
of the 41st International Conference on Machine Learning,
ICML’24. JMLR.org.
Zhang, Y.; Chen, Z.; Fang, Y.; Lu, Y.; Li, F.; Zhang, W.;
and Chen, H. 2024.
Knowledgeable Preference Align-
ment for LLMs in Domain-specific Question Answering.
arXiv:2311.06503.
Zhao, H.; Andriushchenko, M.; Croce, F.; and Flammarion,
N. 2024. Long is more for alignment: a simple but tough-
to-beat baseline for instruction fine-tuning. In Proceedings
of the 41st International Conference on Machine Learning,
ICML’24.
Zheng, M.; Pei, J.; Logeswaran, L.; Lee, M.; and Jurgens, D.
2024. When ”A Helpful Assistant” Is Not Really Helpful:
Personas in System Prompts Do Not Improve Performances
of Large Language Models. In Al-Onaizan, Y.; Bansal, M.;
and Chen, Y.-N., eds., Findings of the Association for Com-
putational Linguistics: EMNLP 2024, 15126–15154. Mi-
ami, Florida, USA: Association for Computational Linguis-
tics.
Zhi-Xuan, T.; Carroll, M.; Franklin, M.; and Ashton, H.
2024. Beyond Preferences in AI Alignment. Philosophical
Studies.
Zhou, Y.; Liu, X.; Ning, C.; and Wu, J. 2024.
Multi-
facetEval: Multifaceted Evaluation to Probe LLMs in Mas-
tering Medical Knowledge. In Proceedings of the Thirty-
Third International Joint Conference on Artificial Intelli-
gence, IJCAI-24, 6669–6677.
718

```
