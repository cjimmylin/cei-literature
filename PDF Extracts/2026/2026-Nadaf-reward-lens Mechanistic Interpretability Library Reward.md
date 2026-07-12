---
source_pdf: "[[Lit-WS-PDFs/2026/2026-Nadaf-reward-lens Mechanistic Interpretability Library Reward.pdf]]"
extracted_date: "2026-07-11"
pages: 28
extractor: "PyMuPDF"
---

Page 1:
reward-lens: A Mechanistic Interpretability Library for
Reward Models
Mohammed Suhail B. Nadaf∗
Abstract
Every RLHF-trained language model is shaped by a reward model, yet the mechanistic-interpretability
toolkit has been built almost entirely for generative LLMs. Its primitives — the logit lens, di-
rect logit attribution, attribution patching, ACDC-style circuit discovery, sparse autoencoders
— all terminate in a projection onto the vocabulary unembedding WU, which a reward model
replaces with a scalar regression head. We present reward-lens, an open-source library that
ports this toolkit to reward models. The library is organised around one observation: the re-
ward head’s weight vector wr is the natural axis along which every interpretability question for
a reward model can be posed and decomposed. It packages a Reward Lens (the reward-model
analogue of the logit lens), component attribution, contrastive activation patching, a reward-
hacking probe suite, and TopK sparse-autoencoder feature attribution against wr, alongside
five extension modules grounded in recent 2025–2026 alignment-theory results: a distortion
index, divergence-aware patching, a misalignment cascade detector, a reward-term conflict anal-
yser, and concept-vector analysis. We validate the framework on two production reward mod-
els (Skywork-Reward-Llama-3.1-8B-v0.2 and ArmoRM-Llama3-8B-v0.1) across ∼695 Reward-
Bench preference pairs per model (1390 pair-model evaluations across the two reward models).
The central empirical finding is negative: linear attribution does not predict causal importance
(mean Spearman ρ = −0.256 on Skywork, −0.027 on ArmoRM). We treat this as a property
the framework is designed to expose, not a bug, and argue that observational decomposition
and causal intervention should be first-class and easily compared.
1
Introduction
Reinforcement learning from human feedback has become the standard training recipe for frontier
language models, and every model trained this way has its behaviour shaped by a learned scalar
function — the reward model — that stands in for human preferences during the policy-optimisation
stage. The reward model is therefore the most safety-critical component of the alignment pipeline:
if it encodes the wrong preferences, an optimised policy inherits those preferences exactly, often
amplified.
The community’s response to this fact has been asymmetric. Behavioural evaluation of reward
models is a mature cottage industry: RewardBench (Lambert et al., 2024), HelpSteer (Wang et
al., 2024), and a long literature on specific failure modes (length bias, sycophancy, formatting bias,
position bias). Mechanistic evaluation of reward models is almost non-existent. The tools that
power generative-LLM interpretability — TransformerLens, the logit lens, direct logit attribution,
∗Correspondence: suhailnadaf509@gmail.com.
1
arXiv:2604.26130v1  [cs.LG]  28 Apr 2026


Page 2:
attribution patching, ACDC, and the SAE ecosystem — all project intermediate model states onto
the vocabulary unembedding WU and score them against a target token distribution.
Reward
models replace that unembedding with a one-dimensional linear head, which silently breaks each
primitive. The gap is structural, not incidental.
This paper introduces reward-lens, a library that fills the gap, and documents its first systematic
application to two open-weight production reward models. The library is built around one organising
observation: the reward head is r = w⊤
r hfinal + br, so wr is the natural axis along which every
interpretability question for a reward model should be posed. Projecting an intermediate residual
stream onto wr yields the Reward Lens, the analogue of the logit lens. Decomposing the residual
stream into per-component contributions and projecting each onto wr yields the analogue of direct
logit attribution. Swapping component activations between preferred and dispreferred completions
and measuring the change in w⊤
r hfinal yields activation patching with a contrastive structure built
into the setup — something the generative-model case does not have for free.
Contributions.
(i) A library. reward-lens is the first installable, architecture-agnostic toolkit
for mechanistic interpretability of reward models, with a small adapter protocol validated on Llama,
Mistral, Gemma-2, and ArmoRM-style multi-objective heads and a generic auto-detecting adapter
for any HuggingFace AutoModelForSequenceClassification reward model.
The library is the
principal contribution of this paper; the experiments are validation (source: https://github.com/
suhailnadaf509/reward-lens). (ii) A unifying framing. Every useful interpretability primitive for
a reward model is a projection onto, or decomposition along, wr. This unifies the lens, attribution,
patching, SAE-feature analysis, and concept-vector analysis into a single family with shared algebra
and shared plotting utilities. (iii) Five theory-grounded extensions (distortion index, divergence-
aware patching, misalignment cascade, reward-term conflict, concept-vector analysis) that opera-
tionalise recent alignment-theory results in runnable code; the contribution of reward-lens is the
operationalisation, not the theory. (iv) Empirical validation on Skywork-Reward-Llama-3.1-8B-v0.2
and ArmoRM-Llama3-8B-v0.1 over ∼695 RewardBench pairs spanning crystallisation depth, attri-
bution structure, hacking profiles, reward-term geometry, circuit overlap, concept dose-response,
and cross-model formation correlations. (v) A negative result. Linear attribution does not predict
causal patching effects in either model; the disagreement is sharper here than in the generative-model
case, plausibly because a scalar output leaves more room for redundant pathways to compensate.
The library keeps observational and causal views first-class and trivially comparable on the same
set of components.
2
Background
Five years of interpretability work on decoder-only transformers has converged on a small family
of primitives: the logit lens (nostalgebraist, 2020) and tuned lens (Belrose et al., 2023) project
intermediate residual streams through the unembedding WU; direct logit attribution decomposes
the residual stream into per-sublayer contributions and projects each onto WU; attribution patching
(Syed & Nanda, 2024) and ACDC (Conmy et al., 2023) extend this with linearised and search-based
causal discovery; the SAE ecosystem (Bloom, 2024; Gao et al., 2024; Rajamanoharan et al., 2024)
decomposes residual streams into dictionary features.
Every one of these primitives ends in a
projection onto WU and a comparison against a target token distribution. For a reward model,
the head is not WU; it is a single linear functional wr, and the off-the-shelf primitives need to be
re-derived.
2


Page 3:
A reward model is trained to output a scalar quality score r(x, y) on a Bradley–Terry preference
loss (Christiano et al., 2017; Ouyang et al., 2022). Production reward models include single-scalar-
head models (Skywork-Reward-Llama-3.1-8B-v0.2, Liu et al., 2024; FsfairX), multi-objective models
with prompt-conditional MoE gating (ArmoRM, Wang et al., 2024), and multi-dimensional-head
models (Nemotron-4-340B-Reward).
Behavioural characterisation of their failure modes is rich;
mechanistic characterisation is rare. This is not because reward-model interpretability is harder
than the generative case. In several structural respects it is easier: the target of attribution is a
single number rather than a 50,000-way distribution; the contrastive structure of preference data is
native; and the projection axis wr is fixed by construction rather than chosen. reward-lens is our
attempt to exploit those advantages.
3
The wr-centred view
Throughout we treat the final layer norm as absorbed into wr (we extract wr from the score-head
weight and keep the norm in the forward pass). Let h(ℓ) ∈Rd denote the residual stream at the
final token position after layer ℓ, with ℓ= −1 the embedding output and ℓ= L −1 the output of
the final transformer block. Let attn(ℓ) and mlp(ℓ) denote the per-sublayer residual contributions
added into the stream at layer ℓ. The reward head is
r(x, y) = w⊤
r hfinal(x, y) + br,
(1)
and the residual stream decomposes additively across sublayers:
hfinal = hembed +
L−1
X
ℓ=0

attn(ℓ) + mlp(ℓ)
.
(2)
Pulling wr through the sum gives an exact per-component decomposition of the scalar reward:
r = w⊤
r hembed +
L−1
X
ℓ=0

w⊤
r attn(ℓ) + w⊤
r mlp(ℓ)
+ br.
(3)
Equation (3) is the decomposition every primitive in reward-lens is built on. Reward Lens: project
the intermediate residual stream at layer ℓonto wr,
RewardLens(ℓ)(x, y) = w⊤
r h(ℓ)(x, y) + br,
(4)
and for a preference pair report the differential ∆(ℓ) = RewardLens(ℓ)(pref)−RewardLens(ℓ)(dispref).
Component attribution: compute each term of (3) and report it as a signed scalar (and its preference-
pair differential).
SAE-feature decomposition: given a TopK sparse autoencoder reconstructing
h = P
i fidi + bdec, the reward decomposes as
r ≈
X
i
fi(w⊤
r di) + w⊤
r bdec + br,
(5)
so w⊤
r di is each feature’s reward alignment — a property of the SAE that needs no forward pass to
evaluate. Activation patching: swap attn(ℓ) or mlp(ℓ) between source and target completions and
measure the induced change in w⊤
r hfinal.
3


Page 4:
The caveat the framing makes visible.
Equations (3) and (5) are linear; the forward pass
that produces hfinal is not.
Layer norms, attention softmaxes, and residual-stream redundancy
mean that a component’s contribution to hfinal (what (3) measures) and the counterfactual effect
of ablating that component (what patching measures) are different quantities. They can and do
disagree. Section 5 quantifies the disagreement on two production models. We do not treat this as
a failure of the framing; we treat it as a property of reward-model computation that is made visible
by the framing.
4
The library
reward-lens (pip install reward-lens, version 1.0.0) wraps any HuggingFace AutoModelForSequenceClassific
reward model behind one Python object and exposes a small set of primitives organised around the
wr-centred view of §3. This section gives the gist; depth lives in the appendix, where each primitive
is paired with its generative-LLM antecedent and its full algorithmic specification.
4.1
Design principles
Four principles shape the library.
wr as the organising axis. Every primitive is either a projection onto wr (lens, component attribu-
tion, SAE feature alignment, concept alignment) or a causal probe whose readout is the change in
w⊤
r hfinal (activation patching, divergence-aware patching, concept dose-response). The same vector
appears in every signature; the same plotting routines aggregate results from every primitive.
HuggingFace-native, not TransformerLens-bound. TransformerLens hardcodes a vocabulary unem-
bedding WU into the type of every high-level primitive — the precise assumption a reward model
breaks. Building on the HuggingFace AutoModel abstraction means reward-lens can wrap any
reward model someone has uploaded without weight surgery, including models with non-standard
heads (multi-objective, MoE-gated). The cost is that we re-implement the hook machinery; the
benefit is coverage.
An adapter protocol for architecture-agnosticism.
Llama, Mistral, Gemma-2, and ArmoRM all
expose layers, attention sublayers, and MLP sublayers under different attribute names; reward
heads are sometimes score, sometimes classifier, sometimes a multi-tensor object behind a
gating module. A ten-method adapter protocol isolates these family-specific details from the rest
of the library, so the lens, attribution, patching, hacking, SAE, and extension modules are written
once against the protocol.
Observational and causal views, kept distinct. A recurring failure mode of interpretability work is
to read off a contribution and report it as if it were a cause. The library makes the difference
syntactic: lens and component attribution return observational quantities (ComponentResult); the
patcher returns a causal one (PatchingResult); both have the same component schema, so a single
comparison plot is one line. §5.4 reports what happens when one does this.
4.2
The model wrapper and adapter protocol
The wrapper, RewardModel, takes a HuggingFace model name or path and returns an object ex-
posing wr (reward_direction), br (reward_bias), the architectural sizes (dmodel, nlayers, nheads,
4


Page 5:
dhead), and a forward_with_cache method that runs a forward pass while collecting per-layer resid-
ual streams and per-sublayer attention and MLP outputs at the final token via PyTorch forward
hooks. An optional cache_full_sequences flag retains the full sequence-length tensors needed for
activation patching. Hooks are registered as a context manager, so re-entrancy and cleanup are
explicit.
The adapter protocol abstracts the family-specific details into ten methods covering reward-head
extraction, layer iteration, sublayer access, and output parsing for the various output formats Hug-
gingFace modules return (tuples, dataclasses, bare tensors).
Concrete adapters ship for Llama,
Mistral, Gemma-2, and ArmoRM; a generic adapter auto-detects layer and head names by walking
the module tree and is sufficient for most additional models without extra code. ArmoRM is the
stress test: its 19-objective regression head with prompt-conditional MoE gating means there is no
single “reward direction” in the simple sense. The adapter exposes a default reward_direction
(the mean of the 19 objective directions, the right approximation for aggregate analyses) and a
per_objective_directions method returning the 19 × dmodel matrix for dimension-resolved anal-
ysis. The full method-by-method contract and a per-family behaviour table appear in Appendix C.
4.3
Core primitives
Each primitive is the reward-model analogue of a generative-LLM primitive. The mapping is the
spine of the library and of the appendix. The reader who knows the logit lens already knows what
the Reward Lens is the moment WU is replaced by wr.
Reward Lens.
Project the intermediate residual stream at each layer onto wr and report the per-
layer trajectory of the preference differential. This is the logit lens with WU replaced by wr and the
cross-entropy-against-a-target replaced by the scalar preference differential. The result includes the
per-layer crystallisation depth: the first fractional layer index at which the differential reaches 50 %
of its final value. Trajectory, crystallisation, and marginal per-layer contributions are all returned
in a single RewardLensResult.
Component attribution.
Materialise equation (3) by computing w⊤
r attn(ℓ) and w⊤
r mlp(ℓ) for
every ℓ. This is direct logit attribution rephrased against wr. The result is a flat vector of 2L + 1
signed contributions (plus the bias) with top_k, by_type, and heat-map utilities. Because the
reward target is a single scalar, the output is one column per pair, not one column per vocabulary
token — the bookkeeping is correspondingly cleaner.
Activation patching.
Swap a chosen sublayer’s full-sequence activation between two completions
and re-run the forward pass, measuring the change in w⊤
r hfinal. Three modes are supported: noising
(target = preferred, source = dispreferred, measures necessity), denoising (the symmetric mode,
measures sufficiency), and zero ablation (source replaced with zeros). Generative-model patching
has the same three modes; what is new for reward models is that the contrastive structure is
native — a preference pair is exactly the (clean, corrupted) input the patcher expects. Returns
a PatchingResult with the same component schema as ComponentResult, so observational and
causal views can be plotted on the same axis.
Hacking detector.
Run paired A/B probes for length, confidence, formatting, sycophancy, and
repetition biases and report Cohen’s d per dimension. This is the analogue of behavioural red-
teaming, but executed inside the library against a single reward model rather than against an
5


Page 6:
end-to-end RLHF policy.
A user-supplied custom probe set is the recommended workflow; the
small shipped defaults are diagnostic, not statistical.
TopK sparse-autoencoder feature attribution.
A TopK SAE trained on a chosen residual
layer reconstructs h ≈P
i fidi + bdec, after which equation (5) gives a per-feature reward alignment
w⊤
r di that requires no further forward pass to evaluate. This is the SAE-circuit-discovery pipeline
of Bloom (2024) and Rajamanoharan et al. (2024) with the target replaced by wr instead of a
token.
The library ships the SAE module, an activation collector that streams residual-stream
activations from a list of (prompt, response) inputs to disk, a trainer with cosine-annealed Adam,
and a feature analyser that returns top/bottom features by reward alignment, activation frequency,
and top-activating examples.
Cross-model comparator.
Run the lens (and optionally attribution) on a set of models for the
same preference pair, normalise the differential trajectories to common fractional depth, and report
crystallisation fractions plus pairwise Pearson correlations. The §5.4 cross-model formation overlap
is one call.
4.4
Theory-grounded extensions
Five extension modules ground recent alignment-theory results in runnable code.
The original
framework is due to the cited authors in each case; the contribution of reward-lens is the opera-
tionalisation. We sketch each here and give algorithmic detail in Appendix E.
Distortion index.
Operationalises the Reward Hacking as Equilibrium under Finite Evaluation
framework (Wang & Huang, 2026): given a set of quality dimensions and a set of evaluation probes
that target subsets of those dimensions, score each dimension’s effective coverage from the probes’
discriminative power and return the under-coverage as a per-dimension distortion index.
High
distortion means the dimension is not being measured; under optimisation pressure it will be hacked.
Divergence-aware patching.
Operationalises Addressing Divergent Representations from Causal
Interventions on Neural Networks (2025, arXiv:2511.04638): wraps the activation patcher with a
Mahalanobis-distance check on the patched activation against an in-distribution covariance fitted
from clean preference data. Patches whose result lies far off manifold are flagged, and divergences
are classified as harmless (off-manifold but small effect, plausibly null-space) or pernicious (off-
manifold with large effect, plausibly a spurious activation of an unrelated circuit). The patcher
returns the same effect numbers as the unaware patcher plus a reliability score.
Misalignment-cascade detector.
Operationalises Natural Emergent Misalignment from Reward
Hacking (MacDiarmid et al., 2025): runs a battery of probes across six misalignment dimensions
(alignment-faking, malicious cooperation, sabotage, self-preservation, deception, sycophancy), com-
putes the across-dimension correlation matrix of preference deltas, and reports systemic-risk clus-
ters. High correlation between dimensions means a single underlying mechanism is driving multiple
visible failure modes.
Reward-term conflict analyser.
Operationalises Aligned, Orthogonal or In-Conflict (Kauf-
mann et al., 2026): given two or more reward terms (extracted from contrastive activations or
supplied directly), computes pairwise cosine similarities of the term directions and classifies pairs
6


Page 7:
as aligned (cos > 0.5), orthogonal (| cos | < 0.2), or in-conflict (cos < −0.3). For multi-objective
heads such as ArmoRM, the analyser can be pointed directly at the per-objective direction matrix.
Concept-vector analysis.
Following the methodology of Chen et al. (2025) on concept directions
in language models, extracts linear concept directions from contrastive activations (confidence,
formality, agreement, verbosity, hedging, helpfulness as shipped defaults; user-supplied concepts
are the recommended workflow), reports each concept’s cosine alignment with wr, and produces
a causal dose-response curve by adding αv into the residual stream and measuring the change in
reward. Concepts that are both well-aligned with wr and known to be hackable (e.g., a length or
sycophancy concept) carry a hacking-risk flag.
4.5
A worked example
The end-to-end use of the library on a single preference pair is short enough to fit in a code block.
The same calls aggregate trivially over a dataset.
from reward_lens import (
RewardModel, RewardLens, ComponentAttribution,
ActivationPatcher, HackingDetector,
)
from reward_lens import quick_concept_analysis
rm = RewardModel.from_pretrained("Skywork/Skywork-Reward-Llama-3.1-8B-v0.2")
# observational
trace = RewardLens(rm).trace(prompt, preferred, dispreferred)
attribute = ComponentAttribution(rm).attribute(prompt, preferred, dispreferred)
# causal
patch = ActivationPatcher(rm).patch_all_components(
prompt, preferred, dispreferred, mode="noising")
# vulnerability profile
hacking = HackingDetector(rm).scan(prompt=prompt, response=preferred)
concepts = quick_concept_analysis(rm)
# observational vs causal, on the same components
trace.plot(); attribute.plot_top_k(10); patch.plot_top_k(10)
The principal output dataclasses (RewardLensResult, ComponentResult, PatchingResult, HackingReport,
ConceptAlignmentReport, plus the extension reports) share a small set of conventions documented
in Appendix G: the component schema is the same across attribution and patching; the plotting
utilities accept any of these dataclasses; aggregation across a dataset is plain Python.
5
Experiments
5.1
Setup
We evaluate Skywork-Reward-Llama-3.1-8B-v0.2 (32 layers, dmodel = 4096, single-scalar head)
and ArmoRM-Llama3-8B-v0.1 (32 layers, multi-objective head with 19 objectives and prompt-
7


Page 8:
conditional MoE gating), both in bfloat16 on a single NVIDIA A100-80GB. The preference data
are RewardBench pairs (n = 200 each for helpfulness, safety, correctness; n = 95 for verbosity;
∼695 pairs per model, 1390 pair-model evaluations in total). Sanity check: the curated diagnostic
preference set is solved at 93.5% accuracy by Skywork and 94.2% by ArmoRM, so neither model
is confused on the controlled probes used by the hacking detector and concept extractor. Repro-
ducibility details appear in Appendix F.
5.2
When does preference form?
We run the Reward Lens on every pair, per dimension, for both models, and record the fractional
layer depth at which the differential first reaches 50% of its final value. Table 1 reports the per-pair
mean and standard deviation.
Skywork
ArmoRM
Dimension
Cryst. depth
|∆final|
Cryst. depth
|∆final|
helpfulness
0.90 ± 0.13
6.4
0.73 ± 0.26
0.08
safety
0.90 ± 0.11
9.4
0.78 ± 0.22
0.10
correctness
0.91 ± 0.11
4.5
0.64 ± 0.34
0.02
verbosity
0.93 ± 0.06
5.2
0.68 ± 0.24
0.05
Table 1: Reward Lens crystallisation depth (fractional layer index, mean ± std over n = 200 pairs
per dimension; n = 95 for verbosity) and mean final-differential magnitude in each model’s native
reward units. Skywork crystallises uniformly late (∼0.90); ArmoRM crystallises earlier and with
much higher across-pair variance.
Skywork crystallises preference uniformly late (∼0.90 across all four dimensions, small across-pair
variance) — consistent with a single unified preference mechanism assembled near the output.
ArmoRM is messier: lower mean depths, higher across-pair variance (std 0.22–0.34), and a different
ordering (correctness crystallises earliest in the mean). We read this as a mechanistic signature of
ArmoRM’s multi-objective architecture, exactly what a prompt-conditional MoE-gated head would
induce. The absolute reward scales differ by ∼two orders of magnitude between models (Skywork
4–10 units; ArmoRM 0.02–0.10); all subsequent comparisons report effects in each model’s native
units.
0
5
10
15
20
25
30
Layer Index
0
2
4
6
8
Differential Reward
Differential Reward Lens
0
5
10
15
20
25
30
Layer Index
Attention
MLP
Component Attribution
4
2
0
2
4
Reward Contribution
Figure 1: Reward Lens dashboard for a representative Skywork helpfulness pair: layer-wise prefer-
ence formation and per-component attribution.
8


Page 9:
5.3
Where does the model put its reward signal?
Component attribution materialises equation (3). For each pair we rank components by |contribution|;
we summarise attribution structure by the frequency with which a component appears in the top-10
across the 200 pairs of a dimension (Table 2).
Model
Dimension
Top 1 (freq.)
Top 2 (freq.)
Top 3 (freq.)
Skywork
helpfulness
mlp_L31 (199/200)
mlp_L30 (196/200)
mlp_L29 (186/200)
Skywork
safety
mlp_L31 (198/200)
mlp_L30 (197/200)
mlp_L29 (193/200)
Skywork
correctness
mlp_L31 (199/200)
mlp_L30 (195/200)
mlp_L28 (193/200)
ArmoRM
helpfulness
mlp_L31 (196/200)
mlp_L30 (139/200)
mlp_L29 (112/200)
ArmoRM
safety
mlp_L31 (193/200)
mlp_L12 (139/200)
attn_L30 (101/200)
ArmoRM
correctness
mlp_L31 (192/200)
mlp_L30 (152/200)
attn_L30 (110/200)
Table 2: Top three components by attribution frequency across pairs. Frequencies are out of 200
pairs. The last three MLPs (mlp_L29-31) dominate observational attribution near-universally on
Skywork; ArmoRM shows the same dominance for its very last MLP but more dispersion below the
top.
The dominance of mlp_L31 is the cleanest near-universality in the data: the final MLP sublayer is in
the top-10 for at least 192 of 200 pairs in every model/dimension cell. By observational attribution,
the reward signal in both models lives in the last three MLPs.
5.4
Causal vs. observational: the faithfulness gap
We next ask whether component attribution predicts causal importance. For the first preference
pair in each dimension we run the noising patcher on all 64 components (32 layers × {attention,
MLP}) and record the Spearman rank correlation between |attribution| and |patch effect|. Table 3
reports the result.
Model
Dimension
Spearman ρ
p-value
Skywork
helpfulness
−0.445
0.0002
Skywork
correctness
−0.255
0.042
Skywork
safety
−0.067
0.598
Skywork
mean
−0.256
—
ArmoRM
helpfulness
−0.282
0.024
ArmoRM
correctness
+0.125
0.325
ArmoRM
safety
+0.075
0.556
ArmoRM
mean
−0.027
—
Table 3: Spearman rank correlation between |attribution| and |patching effect| across the 64 com-
ponents of each preference pair. n = 64 components; p-values are two-sided. No per-dimension
correlation exceeds |0.3| on the positive side; three of six are negative; the two significant correla-
tions are both negative.
9


Page 10:
10
4
10
3
10
2
10
1
100
|Attribution| (log scale)
10
1
100
101
|Patch Effect| (log scale)
mlp_L30
mlp_L29
mlp_L0
mlp_L1
attn_L0
Spearman 
0.445
p
0.0002
Faithfulness: Observational vs. Causal
Type
Attention
MLP
Figure 2: Attribution vs. patching, Skywork helpfulness. Late-MLP components dominate attribu-
tion; early-layer components dominate patching.
At the component level the contrast is sharper than the correlation suggests. On Skywork help-
fulness, top-3 by attribution are mlp_L31 = 5.60, mlp_L30 = 1.90, mlp_L29 = 0.91 (reward units);
top-3 by patching are mlp_L0 = 30.31, mlp_L1 = 11.53, attn_L0 = 6.09. Late MLPs that dom-
inate attribution have near-zero patching effects; early-layer components that dominate patching
have unremarkable attribution. Skywork correctness shows the same pattern with patching led by
middle attention heads (attn_L11 = 15.75, attn_L9 = 13.94, attn_L14 = 13.03); ArmoRM does
too at ∼300× smaller absolute scales.
Why this is not a bug.
The residual stream is redundant: a late MLP can be ablated because
parallel paths compensate, while early layers are load-bearing in a way nothing downstream can
recover. Attribution measures contribution to w⊤
r hfinal; patching measures necessity for it to remain
high. Equation (3) does not promise the two agree. The Pearson correlations sometimes also flip
sign relative to the Spearman ones (ArmoRM correctness Pearson r = +0.42, p = 0.0005, but
Spearman ρ = +0.125, p = 0.33), reflecting sensitivity to single extreme components on a 64-point
sample.
Operational consequence.
Attribution is for exploration; it is not a substitute for patching
when a causal claim is needed. The framework keeps both views first-class and trivially comparable
on the same components.
10


Page 11:
5.5
Cross-model agreement and circuit specialisation
Reward Lens trajectories of the two architecturally different models are highly correlated when
matched on normalised depth: per-dimension Pearson correlations of the differential curve are
r = 0.846 (helpfulness), 0.807 (safety), 0.844 (correctness) on a representative pair. We report this
as motivation for the scale study proposed in §7, not as a general result.
Circuit overlap tells a complementary story. The top-k Jaccard overlap (k = 10) between most-
attributed components across the four dimensions is uniform on Skywork (off-diagonal 0.82–1.00,
mean per dimension 0.879) and much more varied on ArmoRM (off-diagonal 0.43–0.67, mean 0.50–
0.58). The trajectory of preference formation is similar across architectures, but the set of compo-
nents carrying that formation is dimension-uniform in a single-scalar model and dimension-specific
in a multi-objective one.
0.0
0.2
0.4
0.6
0.8
1.0
Normalized Layer Depth
0.4
0.2
0.0
0.2
0.4
0.6
0.8
1.0
Normalized Differential Lens
r
0.846
Helpfulness
0.0
0.2
0.4
0.6
0.8
1.0
Normalized Layer Depth
r
0.807
Safety
0.0
0.2
0.4
0.6
0.8
1.0
Normalized Layer Depth
r
0.844
Correctness
Skywork
ArmoRM
Figure 3: Cross-model trajectory overlay. Normalised preference differential as a function of frac-
tional layer depth for Skywork and ArmoRM on three dimensions.
5.6
Hacking profiles
The hacking detector runs A/B probes for length, confidence, formatting, sycophancy, and repetition
biases.
Dimension
Skywork d
ArmoRM d
Pairs
length
−1.13
−0.02
n = 3
confidence
−2.08
+2.40
n = 2
formatting
−0.95
+0.91
n = 2
sycophancy
−5.82
−11.92
n = 2
repetition
∞(artefact)
∞(artefact)
n = 1
Table 4: Hacking-detector effect sizes (Cohen’s d). Positive values mean the model rewards the
biased variant.
Pair counts are the shipped defaults and are deliberately small; the repetition
entries are zero-variance and report ∞as an artefact.
The cleanest contrast is the sign flip on confidence and formatting: Skywork penalises both, Ar-
moRM rewards both.
Both strongly penalise sycophancy.
Skywork’s negative bias on length,
confidence, and sycophancy — the opposite of the classical reward-hacking pattern — is plausibly a
11


Page 12:
signature of its training recipe. Effect sizes are directional given the small samples; rigorous claims
require larger custom probe sets (see §8).
12
10
8
6
4
2
0
2
Cohen's d (Effect Size)
Length
Confidence
Formatting
Sycophancy
Repetition
small-sample artefact, n=1
Hacking Effect Sizes Across Models
Skywork
ArmoRM
Figure 4: Hacking-detector effect sizes. Positive d rewards the biased variant; negative d penalises
it.
5.7
Concept-level structure
We extract six linear concept directions from contrastive preference pairs — confidence, formality,
agreement, verbosity, hedging, and helpfulness — and report each concept’s cosine alignment with
wr, the slope of its causal dose-response curve under residual-stream addition h ←h + αv for
α ∈{−2, −1, −0.5, 0.5, 1, 2}, and a hacking-risk score that combines alignment and effect magnitude.
Skywork
ArmoRM
Concept
alignment
causal slope
alignment
causal slope
agreement
0.340
+1.002
0.074
+0.0034
verbosity
0.323
+0.911
−0.052
−0.0032
helpfulness
0.290
+0.847
0.080
+0.0079
formality
0.287
+0.825
0.047
+0.0040
confidence
0.261
+0.766
0.062
+0.0063
hedging
0.245
+0.711
0.080
+0.0063
Table 5: Concept reward alignment (cosine of concept direction with wr) and causal slope (regression
of ∆reward on α over the dose-response curve), per model.
Two findings. First, on Skywork the dose-response curves are clean straight lines: the agreement
concept has alignment 0.340 and slope +1.002, with negligible deviation from linearity over α ∈
[−2, 2] — a strong signal that the concept is locally represented as a linear direction. Second, the
absolute concept alignments on ArmoRM are an order of magnitude smaller (max 0.080 vs. 0.340)
and the dose-response slopes correspondingly tiny: ArmoRM’s reward signal does not align cleanly
with any single linear concept direction.
12


Page 13:
2
1
0
1
2
Injection Strength 
2
1
0
1
2
 Reward
Skywork
2
1
0
1
2
Injection Strength 
0.015
0.010
0.005
0.000
0.005
0.010
0.015
ArmoRM
Confidence
Formality
Agreement
Verbosity
Hedging
Helpfulness
Figure 5: Concept dose-response curves. Skywork responds linearly at unit scale; ArmoRM responds
at ∼1% the magnitude.
5.8
Reward-term geometry and cascade signal
The conflict analyser computes cosine similarities between the four quality-dimension direction
vectors. Skywork’s matrix is uniformly aligned (off-diagonal cosines 0.534–0.917); ArmoRM’s is
aligned but weaker (0.341–0.954).
Neither model has a reward-shape configuration classified as
in-conflict or orthogonal.
The cascade detector reports systemic-risk scores of 1.00 (Skywork) and 0.60 (ArmoRM). Read this
with the small-sample caveat: the detector estimates pairwise correlations between misalignment-
dimension scores using the same 1–3 probes per dimension as the hacking detector; correlations of
2–3-point sequences round to ±1 for any non-trivial pair, and the matrix is therefore degenerate.
The cascade-risk score is directional triage, not a confidence-bearing measurement. The contrast
between the two models is large enough that the ordering may survive a larger sample, but we do
not place weight on the absolute values.
5.9
Runtime characterisation
On a single A100-80GB for Skywork (8B, 32 layers): Reward Lens per pair ∼5 s; component
attribution per pair ∼10 s; full noising patch over all 64 sublayers ∼30 min; full hacking scan ∼5
min; SAE training on a single layer ∼8–24 h. Cost is dominated by the patching pass.
6
Summary of findings
(1) On Skywork, preferences crystallise uniformly late (fractional depth ∼0.90 across all four di-
mensions tested); on ArmoRM they crystallise earlier and with much higher across-pair variance,
consistent with that model’s multi-objective architecture. (2) Late MLPs dominate observational
attribution near-universally on both models, with mlp_L31 in the top-10 for ≥192 of 200 pairs
everywhere we look. (3) Linear attribution does not predict causal patching effects in either model
(mean Spearman ρ = −0.256 on Skywork, −0.027 on ArmoRM); the two quantities should be com-
pared, not substituted. (4) Cross-model formation-correlation is high on a representative-pair basis
13


Page 14:
(r = 0.81–0.85), but circuit-overlap structure differs sharply: Skywork uses uniform circuits across
dimensions, ArmoRM uses dimension-specific ones. (5) Skywork and ArmoRM have qualitatively
different hacking profiles — Skywork penalises confidence and formatting; ArmoRM rewards them;
both strongly penalise sycophancy. (6) Concept directions extracted from contrastive pairs pro-
duce clean linear dose-response curves on wr in Skywork (slope ∼1 reward unit per unit α for the
agreement concept), at ∼1% the magnitude on ArmoRM.
7
Proposed experiments and forward-looking work
The framework supports several experiments we have not yet run; we list them as research questions,
not as results, and use them to motivate two longer-horizon programmes the framework now makes
tractable.
SAE feature-level reward decomposition.
The framework predicts that for a TopK SAE
trained on a chosen residual layer, w⊤
r di summarises each feature’s reward contribution. Two ques-
tions follow: is the distribution of w⊤
r di heavy-tailed, indicating a small set of reward-relevant
features; and does the cumulative top-k feature contribution saturate the held-out reward variance
well below k = nfeatures? We have not run this and report it as the next high-priority experiment.
Distortion-index validation.
Can the distortion index predict, before any RL, which quality
dimension a reward model will under-cover and therefore allow a downstream policy to hack? The
proposed protocol is to construct a reward-model training run with one quality dimension deliber-
ately absent from evaluation, score the resulting model with the distortion analyser, then PPO-train
against it and check whether the predicted dimension is the one that degrades. This is the bold-
est test the library affords; success would move reward-model interpretability from detection to
prediction.
Scale study.
How do crystallisation depth, attribution-vs.-patching faithfulness, and concept
alignment vary along the Skywork-Reward-Gemma-2 ladder (2B / 8B / 27B) and into Nemotron-
4-340B-Reward? Stated, not claimed: we expect crystallisation to shift later with scale, the faith-
fulness gap to widen as redundant pathways multiply, and concept alignment to strengthen with
capacity.
Training-loop integration.
The Reward Lens, hacking detector, and distortion index each have
a per-pair runtime small relative to a reward-model training step on the same hardware. The natural
next step is to turn them into in-loop monitors: a callback that runs a fixed diagnostic probe set
every N optimiser steps and raises an alarm when distortion exceeds a threshold or a previously
penalised hacking dimension flips sign. This would shift reward-model interpretability from a post-
hoc audit into a training-time safeguard, before failure modes are baked in. The infrastructure for
the audit half already exists in the library; the integration with TRL- or OpenRLHF-style trainers
is a research programme, not a feature.
Interpretability-guided reward-model editing.
Once a concept is identified as both well-
aligned with wr and known-to-be-hackable (§5.7 already produces such a list on Skywork — the
agreement concept, slope +1.002, is a candidate), the natural next step is to edit the reward head
14


Page 15:
to suppress that concept’s contribution: subtract its component from wr, retrain only the head, or
apply a low-rank correction. The open question is whether such edits transfer to a downstream RL
run — whether a reward model that no longer rewards verbosity in a probe also fails to reward
it in a policy fine-tuned against it. The library’s attribution, patching, SAE, and concept-vector
primitives are exactly the tools needed to localise the target features; what remains is the edit-and-
retrain experiment.
A per-experiment checklist accompanies the source release.
8
Discussion and limitations
Linear decomposition is not causal decomposition.
The attribution-vs.-patching negative
correlation in §5.4 is a structural property of linear decomposition in a redundant residual-stream
architecture, not a bug. The library’s own headline empirical result is this limitation. We chose to
foreground it in the abstract rather than bury it; an honest interpretability library should make the
gap between observation and causation legible rather than collapse them.
Small-sample statistics.
The shipped hacking detector uses 1–3 pairs per dimension; Cohen’s
d on such samples is unstable, the infinities in Table 4 are zero-variance artefacts, and the cascade
detector’s ±1 pairwise correlations are degenerate. The fix is straightforward: scale the diagnostic
preference set by 10–30× and add bootstrap confidence intervals at the library level.
Single-pair faithfulness.
The faithfulness experiment of §5.4 is per-dimension single-pair; it
tests a specific example rather than the population. The headline conclusion (attribution is not
faithful to patching) is robust enough across six dimension/model combinations to be reported,
but per-dimension numbers should be interpreted as point estimates. The cross-model formation
correlations in §5.5 share this single-pair caveat.
Observational caveats throughout.
The Reward Lens, component attribution, concept align-
ments, and SAE feature alignments are all observational. Only activation patching (and divergence-
aware patching) provides causal evidence. The library says this; this paper says this; downstream
work should say this.
Inherited open problems.
reward-lens does not solve the known open problems of residual-
stream interpretability: SAEs remain lossy; activation patching can induce divergent representations
(the divergence-aware patcher is a partial mitigation, not a solution); cross-layer circuit discovery
is underdeveloped. What the library does is make these problems testable in a new model class
— and in some cases the scalar-output structure may let us study them with less clutter than in
generative models.
Reward models we cannot analyse.
Proprietary API-only reward models inside frontier-lab
training pipelines are closed to any weight-level interpretability tool, this one included. Meaningful
mechanistic science on reward models requires open-weight reward models; the recent uptick in open
releases is encouraging.
15


Page 16:
Process reward models.
Per-step scoring works, but step-boundary detection, accumulated-
quality tracking, and step-level attribution are not implemented in the current release and are a
known gap.
9
Conclusion
Reward models are the object that defines what an RLHF-trained language model is optimis-
ing for, and they are the least mechanistically understood component of the alignment pipeline.
reward-lens packages a Reward Lens, component attribution, contrastive activation patching,
hacking probes, concept-vector analysis, and SAE-feature attribution against a single organising
principle — the reward head’s weight vector wr as the axis of all decomposition — behind one pip
install. The headline empirical result is negative and honest: on two production reward models,
linear attribution does not predict causal importance, and researchers should plan their experi-
ments accordingly. The library was built so that this gap could be measured rather than ignored;
the natural next steps it enables — in-training distortion monitoring and interpretability-guided
reward-head editing — treat reward-model interpretability as something that should run alongside
reward-model training, not after it.
References
• Belrose, N., Furman, Z., Smith, L., et al. (2023). Eliciting Latent Predictions from Trans-
formers with the Tuned Lens. arXiv:2303.08112.
• Bloom, J. (2024). SAELens (software).
• Christiano, P., Leike, J., Brown, T., Martic, M., Legg, S., Amodei, D. (2017). Deep Rein-
forcement Learning from Human Preferences. NeurIPS.
• Conmy, A., Mavor-Parker, A., Lynch, A., Heimersheim, S., Garriga-Alonso, A. (2023). To-
wards Automated Circuit Discovery for Mechanistic Interpretability. NeurIPS.
• Fiotto-Kaufman, J., et al. (2024). NNsight and NDIF: Democratizing Access to Foundation
Model Internals. arXiv.
• Gao, L., et al. (2024). Scaling and Evaluating Sparse Autoencoders. OpenAI.
• Lambert, N., et al. (2024). RewardBench: Evaluating Reward Models for Language Modeling.
arXiv:2403.13787.
• Liu, C. Y., et al. (2024). Skywork-Reward: Bag of Tricks for Reward Modeling in LLMs.
• Nanda, N., Bloom, J. (2022). TransformerLens (software).
• nostalgebraist (2020). Interpreting GPT: the logit lens. LessWrong.
• Ouyang, L., et al.
(2022).
Training language models to follow instructions with human
feedback. NeurIPS.
• Park, R., et al. (2024). Disentangling Length from Quality in Direct Preference Optimization.
arXiv:2403.19159.
16


Page 17:
• Perez, E., et al. (2023). Discovering Language Model Behaviors with Model-Written Evalua-
tions. ACL.
• Rajamanoharan, S., et al. (2024). Gemma Scope.
• Sharma, M., et al. (2024). Towards Understanding Sycophancy in Language Models. ICLR.
• Singhal, P., et al. (2024). A Long Way to Go: Investigating Length Correlations in RLHF.
arXiv:2310.03716.
• Stiennon, N., et al. (2020). Learning to summarize with human feedback. NeurIPS.
• Syed, A., Nanda, N. (2024). Attribution Patching Outperforms Automated Circuit Discovery.
• Wang, H., et al. (2024). ArmoRM: Interpretable Preferences via Multi-Objective Reward
Modeling with Mixture-of-Experts. arXiv:2406.12845.
• Chen, R., et al. (2025). Persona Vectors: Monitoring and Controlling Character Traits in
Language Models. Anthropic. arXiv:2507.21509.
• Addressing Divergent Representations from Causal Interventions on Neural Networks (2025).
arXiv:2511.04638.
• MacDiarmid, M., Wright, B., Uesato, J., Benton, J., Kutasov, J., Price, S., et al. (2025). Natu-
ral Emergent Misalignment from Reward Hacking in Production RL. Anthropic. arXiv:2511.18397.
• Wang, J., & Huang, J. (2026).
Reward Hacking as Equilibrium under Finite Evaluation.
arXiv:2603.28063.
• Kaufmann, M., Lindner, D., Zimmermann, R. S., & Shah, R. (2026).
Aligned, Orthog-
onal or In-conflict: When can we safely optimize Chain-of-Thought?
Google DeepMind.
arXiv:2603.30036.
A
Library overview and design principles
This appendix is the technical manual for reward-lens. It is organised around the conceptual
through-line of the paper: how does mechanistic interpretability change when the head is a single
linear functional wr rather than a vocabulary unembedding WU? Each primitive is paired with its
generative-LLM antecedent, the change is identified, and the reward-model implementation is given
in enough detail that a reader could replicate it on a different framework.
A.1
Why HuggingFace-native rather than TransformerLens-bound
TransformerLens (Nanda & Bloom, 2022) is the de-facto substrate of generative-model mechanistic
interpretability. Its primitives — HookedTransformer, the logit lens, direct logit attribution, attri-
bution patching — are typed against the assumption that the output of the network is a vocabulary
distribution. Two specific assumptions break for a reward model. First, the unembedding WU is
loaded as a known tensor of shape |V |×dmodel; a reward model has no unembedding, only a one-row
score head whose extraction varies by family. Second, the lens, attribution, and patching APIs re-
turn quantities indexed by token id, with utility functions for token selection and target-distribution
comparison; for a reward model the target is a scalar with no token id, and these utilities are dead
17


Page 18:
code or worse, misleading. A from-scratch port that respects the new shape of the head is cleaner
than monkey-patching.
The cost of this choice is that reward-lens re-implements the hook machinery on top of plain
HuggingFace forward hooks. The benefit is coverage of model families with non-standard heads, in-
cluding multi-objective and MoE-gated heads, and a single import path (from reward_lens import
RewardModel) that wraps anything loadable through AutoModelForSequenceClassification.
A.2
Why an adapter protocol, and where its boundary sits
Llama, Mistral, Gemma-2, and ArmoRM all expose layers, attention sublayers, and MLP sublayers
under different attribute paths (model.model.layers, model.transformer.h, model.gpt_neox.layers,
etc.); reward heads are sometimes score, sometimes classifier, sometimes a multi-tensor object
behind a gating network. The adapter protocol isolates these family-specific details into a ten-
method interface and keeps every other module in the library written against that interface. The
boundary is drawn so that the adapter handles everything family specific (head extraction, layer
iteration, sublayer access, output parsing) and nothing else: the lens, attribution, patcher, hacking
detector, SAE, and extension modules are family-agnostic.
A.3
Why observational and causal views are kept distinct
A recurring failure mode of interpretability work is to read off a contribution and report it as if it
were a cause. The experiments of §5.4 show why that conflation is dangerous in this setting: on
the same components, the two quantities can have negative rank correlation. The library makes
the distinction syntactic: lens and component attribution return ComponentResult; the patcher
returns PatchingResult; both have the same component schema, so a side-by-side plot is one
line. Equation (3) is taught in §4.3 as an algebraic identity on contributions, not a claim about
counterfactual effects.
A.4
Package surface, by purpose
The user-facing surface clusters into five groups. Model wrapping: RewardModel (the wrapper) and
the ModelAdapter hierarchy (LlamaAdapter, MistralAdapter, Gemma2Adapter, ArmoRMAdapter,
GenericAdapter, with a get_adapter factory). Observational primitives: RewardLens (RewardLensResult,
reward_lens_plot), ComponentAttribution (ComponentResult), and the TopKSAE family (TopKSAE,
ActivationCollector, SAETrainer, FeatureAnalyzer). Causal primitives: ActivationPatcher
(PatchingResult) and DivergenceAwarePatching (DivergenceAwarePatchingResult). Vulnera-
bility and theory-grounded extensions: HackingDetector (HackingReport), DistortionAnalyzer
(DistortionReport), MisalignmentCascadeDetector (CascadeReport), RewardConflictAnalyzer
(ConflictReport), ConceptExtractor (ConceptAlignmentReport, with quick_concept_analysis).
Supporting infrastructure: Comparator for cross-model analyses, diagnostic_data for curated pref-
erence pairs, and viz for shared plotting.
B
The model wrapper in depth
RewardModel wraps a HuggingFace transformer + score head and exposes the single object on which
all other primitives act.
18


Page 19:
Reward-head extraction.
The adapter’s get_reward_head_params(model) returns (wr, br) with
wr ∈Rdmodel. For single-scalar heads (Llama, Mistral, Gemma-2 trained as RMs) the weight is the
single row of the score linear layer. For ArmoRM the weight is the column-mean of the 19-row
regression_layer weight matrix — the right approximation for aggregate analyses — and a sepa-
rate per_objective_directions method returns the full 19×dmodel matrix for dimension-resolved
analyses such as the conflict analyser. For models with truly nonlinear heads, the protocol is in-
compatible by design: a primitive that decomposes along wr does not have a meaningful target.
What the cache contains.
forward_with_cache returns an ActivationCache dataclass with:
a dict of per-layer residual streams indexed −1, 0, . . . , L −1 (where −1 is the post-embedding
output, ℓis the post-block residual at layer ℓ), a dict of per-layer attention sublayer outputs,
a dict of per-layer MLP sublayer outputs, and the final-token positions used to index out the
relevant activations. Each cached tensor is the final-token slice h(ℓ)[batch, seq_lengths −1, :] unless
cache_full_sequences=True, in which case the full (batch, seq, dmodel) tensor is also retained.
Patching needs the full tensors to splice along the shared prefix; the lens and attribution need only
the final-token slice.
Hook lifecycle.
Hooks are registered as a context manager via rm.hooks(). The wrapper is
reentrant: a forward pass inside a hook block sees the registered hooks; a forward pass outside does
not. On exit, all handles are removed even if the body raised. A single forward_with_cache call
sets up its own hooks internally; user code rarely needs the lower-level interface.
Layer-norm handling.
Decoder-only transformers apply a final layer norm before the score head:
r = w⊤
r LN(hfinal) + br. We absorb this norm conceptually into wr for analytic purposes (the lens
reports w⊤
r h(ℓ), not w⊤
r LN(h(ℓ))), but the forward pass keeps the norm in place when computing
actual rewards; the small inconsistency between intermediate and final projection is the price of
a tractable linear story. In practice the crystallisation depths reported in §5.2 are insensitive to
whether the norm is applied at every layer or only at the output.
Final-token selection.
Sequences are batched with right-padding; the wrapper uses final_pos =
(attention_mask.sum(1) −1).clamp(0, T −1) to recover per-sample final-token indices. The clamp
is defensive against zero-length inputs.
Device, dtype, and inference-mode discipline.
The wrapper runs the underlying model in
torch.inference_mode() and calls rm.eval(); cached activations are detached and moved to CPU
once captured to avoid GPU-memory growth across a long run; user tensors stay on the model’s
device. Bfloat16 is supported throughout; arithmetic that requires float32 (the SAE loss, conflict
cosine similarities) is up-cast locally.
C
The adapter protocol in depth
The adapter abstraction is a ten-method interface (Table 6). The shipped adapters are summarised
in Table 7; ArmoRM is then expanded in its own subsection.
19


Page 20:
Method
Returns
Contract
get_reward_head_params(model)
(wr, br)
wr ∈Rdmodel, br ∈R
get_layers(model)
nn.ModuleList
ordered transformer blocks
n_layers(model)
int
number of blocks
n_heads(model)
int
attention heads per block
get_attn_module(layer)
Optional[nn.Module]
per-block attention sublayer
get_mlp_module(layer)
Optional[nn.Module]
per-block MLP sublayer
extract_layer_output(out)
Tensor[B,T,d]
residual after the block
extract_attn_output(out)
Tensor[B,T,d]
attention residual contribution
extract_mlp_output(out)
Tensor[B,T,d]
MLP residual contribution
get_embedding(model)
nn.Module
input embedding layer
extract_reward(out, inputs)
Tensor[scalar]
final scalar reward
Table 6: The adapter contract. Implementing these eleven entries (plus the standard __init__) is
sufficient to bring up a new model family.
Adapter
Layer path
Reward head
LlamaAdapter
model.model.layers
model.score (single-scalar)
MistralAdapter
model.model.layers
model.score (single-scalar)
Gemma2Adapter
model.model.layers
model.score (single-scalar)
ArmoRMAdapter
model.model.layers
19-objective regression + MoE gate
GenericAdapter
auto-detected
auto-detected
Table 7: Shipped adapters.
GenericAdapter walks the module tree for layer paths matching
[model | transformer | gpt_neox].[layers | h] and reward heads named score / classifier /
v_head / reward_head, falling back to the last nn.Linear in an nn.Sequential.
C.1
ArmoRM as the stress test
ArmoRM-Llama3-8B-v0.1 has three components fused on top of the backbone: (i) a regression_layer
of shape 19 × dmodel that maps the final hidden state to 19 per-objective scores; (ii) a prompt-
conditional MoE gating network that, given the prompt’s final hidden state, outputs 19 mixture
weights summing to one; and (iii) a debiasing reward_transform_matrix applied to the gated com-
bination to produce the final scalar reward output.score. The adapter’s get_reward_head_params
returns the column-mean ¯w =
1
19
P19
k=1 Wreg,k, which is the right approximation for analyses that
aggregate across objectives (the lens reads off “average reward direction”). For dimension-resolved
analyses the adapter exposes per_objective_directions, returning the full 19 × dmodel matrix;
the conflict analyser is then called directly on those rows. We deliberately do not try to absorb the
MoE gate into a single direction: the gate is prompt-conditional, so the effective direction varies
across inputs, and any single “direction” that pretends otherwise would be misleading. Aggregate
analyses use ¯w and accept the approximation; per-objective analyses use the full matrix and respect
the true geometry.
C.2
Adding a new family
For a model whose backbone matches the auto-detection patterns of GenericAdapter, no code
change is required: the wrapper picks up the right layers and head on first call. For a model with
a non-standard layer path or head shape, an adapter implementing the eleven-method interface is
typically about fifty lines.
20


Page 21:
D
Core primitives, in depth
This appendix is structured one subsection per primitive. Each opens with the generative-LLM
antecedent, identifies what changes for a reward model, and gives the reward-model implementation
in enough detail to be reproduced. Limitations specific to the primitive (as opposed to the global
limitations in §8) are called out in line.
D.1
Reward Lens
Generative antecedent.
The logit lens (nostalgebraist, 2020) takes the residual stream at layer
ℓand applies the unembedding to obtain a vocabulary distribution p(ℓ) = softmax(WULN(h(ℓ))),
then reads off the lens’s prediction for the next token. Tuned-lens (Belrose et al., 2023) replaces WU
with an affine transform trained to match the final-layer prediction, sharpening early-layer readouts.
What changes for reward models.
The vocabulary projection is replaced by the reward direc-
tion r(ℓ) = w⊤
r h(ℓ) + br; the target is a scalar, not a distribution; there is no per-token bookkeeping.
The natural readout on a preference pair is the per-layer differential ∆(ℓ) = r(ℓ)
pref −r(ℓ)
dispref, which
inherits the contrastive structure of the data without extra machinery.
Implementation.
RewardLens.trace(prompt, pref, dispref) runs two cached forwards (one
per completion), pulls out {h(ℓ)}L−1
ℓ=−1 at the final token, and returns a RewardLensResult with fields
layers, reward_lens_preferred, reward_lens_dispreferred, differential, marginal_contributions
(per-layer first differences of differential), and the final scalars reward_preferred, reward_dispreferred.
The crystallisation layer is defined as the smallest ℓfor which ∆(ℓ) reaches 50 % of ∆(L−1) in the
same sign; for a ∼0 final differential the crystallisation depth is undefined and the field is returned
as None.
Plotting and aggregation.
RewardLensResult.plot draws preferred/dispreferred trajectories
with the crystallisation layer marked. reward_lens_plot(model, prompt, pref, dispref) is the
one-call convenience. Aggregation across a dataset is plain Python over a list of results — the
dataclass is intentionally flat.
Primitive-specific limitation.
The lens reports w⊤
r h(ℓ) without applying the final layer norm
at intermediate layers; intermediate-layer projections are therefore on a slightly different scale than
the final layer. This affects the absolute magnitudes (which we never compare across layers) but
not the crystallisation index.
D.2
Component attribution
Generative antecedent.
Direct logit attribution decomposes hfinal = hembed + P
ℓ(attn(ℓ) +
mlp(ℓ)) and projects each summand through WU to get a token-indexed contribution per component,
summarised against the difference of two target logits.
What changes.
The projection is w⊤
r , not WU; the target is the scalar reward differential, not a
logit difference. The output is a flat vector of 2L + 1 signed scalars (plus the bias) rather than a
(2L + 1) × |V | matrix. The bookkeeping is correspondingly simpler.
21


Page 22:
Implementation.
ComponentAttribution.attribute(prompt, pref, dispref) caches both for-
wards, computes cembed = w⊤
r hembed, c(ℓ)
attn = w⊤
r attn(ℓ), and c(ℓ)
mlp = w⊤
r mlp(ℓ) for both completions,
and returns a ComponentResult with fields component_names (e.g. embed, attn_L0, mlp_L0, . . . ),
component_types, layer_indices, contributions_preferred, contributions_dispreferred, differential_co
and the totals total_reward_preferred, total_reward_dispreferred. Utilities top_k(k, by="differential"|"
by_type("attn"|"mlp"|"embed"), plot_top_k, plot_heatmap act on this dataclass.
Sanity check.
The sum of all contributions plus br should match the model’s own reward to
floating-point precision; this is asserted in the wrapper’s tests and is the cleanest correctness check
the library has.
Primitive-specific limitation.
Attribution is purely observational; the gap between attribution
and patching is the content of §5.4.
D.3
Activation patching
Generative antecedent.
Activation patching (Heimersheim et al.; Syed & Nanda, 2024) replaces
a component’s output on a clean input with the corresponding output from a corrupted input (or
vice versa, or with zeros) and measures the change in a target logit difference.
What changes.
The contrastive structure of preference data gives the patcher its (clean, cor-
rupted) pair for free: noising patching takes the preferred completion as clean and the dispreferred
as corrupted; denoising swaps. The readout is ∆r = w⊤
r (hclean
final −hpatched
final
), a single scalar per patched
component. The same component schema as component attribution allows trivial side-by-side com-
parison (§5.4).
Modes.
Three modes are supported. Table 8 summarises their semantics and when each is the
right choice.
Mode
Source →target
Measures
Use when
noising
dispref →pref
necessity
you want “which components must be intact”
denoising
pref →dispref
sufficiency
you want “which components alone flip the call”
zero ablation
zeros →pref
component-removal effect
no contrastive pair available
Table 8: Patching modes. Noising is the default; denoising is the symmetric choice; zero ablation is
OOD by construction and should be read with the divergence-aware patcher’s results in mind.
Sequence-length handling.
Source and target sequences are typically of different lengths. The
hook truncates the source activation to the target’s length and copies along the shared prefix:
hpatched[:, : Tshared, :] = hsource[:, : Tshared, :], hpatched[:, Tshared :, :] = htarget[:, Tshared :, :]. For pref-
erence pairs that share a prompt and differ only in the completion, this is the right thing. Path-
patching at the token-position level is future work.
Implementation.
ActivationPatcher.patch_all_components(prompt, pref, dispref, mode)
iterates over all 2L sublayers (and optionally the embedding), re-running the model with the splice
hook installed for one component at a time, and returns a PatchingResult with the same component
22


Page 23:
schema as ComponentResult plus patch_effects (signed, in reward units) and original_differential.
normalized_effects divides by original_differential so that 1.0 means “patching this compo-
nent fully kills the preference”.
Primitive-specific limitations.
Patching can induce out-of-distribution activations, especially
zero ablation.
The divergence-aware patcher (§E.2) is the diagnostic; it does not eliminate the
problem.
D.4
Hacking detector
Generative antecedent.
Behavioural red-teaming of language models, as in Perez et al. (2023),
is end-to-end: probe inputs are fed to the policy and outputs are scored. The reward model is
invisible to the probe.
What changes.
Inside the library the probe is fed directly to the reward model and the scalar
output is the readout, with no intermediate generation. A probe is an A/B pair of completions
identical except for the dimension being tested.
Implementation.
HackingDetector(model).scan(tests=...) runs five default dimensions (Ta-
ble 9); each dimension’s pairs are scored to produce a vector of deltas δi = r(biased)−r(neutral). Co-
hen’s d is ¯δ/std(δ). The result is a HackingReport with one BiasTestResult per dimension (fields:
dimension, reward_deltas, mean_delta, std_delta, effect_size, pairs_tested, verdict). Cus-
tom probe sets are supplied via test_custom_pair(prompt, neutral, biased).
Dimension
A/B contrast
length
identical content, 1× vs 3–4× length
confidence
hedged uncertainty vs authoritative tone, same content
formatting
plain prose vs markdown headers/bullets, same content
sycophancy
honest correction vs flattering agreement on a false claim
repetition
single statement vs same fact restated three times
Table 9: Default hacking-detector dimensions.
Primitive-specific limitations.
The shipped probe sets are diagnostic, not statistical. Reliable
hacking claims require user-supplied probe sets with n ≥30 pairs per dimension and bootstrap
confidence intervals; the small zero-variance entries in §5.6 are an honest artefact of the shipped
defaults.
D.5
TopK sparse-autoencoder feature attribution
Generative antecedent.
SAE-based circuit discovery (Bloom, 2024; Gao et al., 2024; Raja-
manoharan et al., 2024) trains a dictionary on residual-stream activations of a generative LLM and
analyses each feature by its top-activating tokens or by its contribution through WU to a target
logit.
What changes.
Equation (5) gives a closed-form per-feature reward alignment w⊤
r di that requires
no further forward pass once the SAE is trained. The notion of “top-activating token” is replaced
by “top-activating preference pair”, or simply by the per-feature alignment magnitude.
23


Page 24:
Implementation.
TopKSAE(d_model, n_features, k) implements the standard TopK SAE: en-
coder z = (x −bdec)Wenc + benc, f = ReLU(TopK(z, k)), decoder ˆx = fWdec + bdec. The training
loss is ∥x −ˆx∥2 + 0.01∥cols(Wdec)−1∥2; decoder columns are renormalised to unit norm after each
step. ActivationCollector streams residual-stream activations from a list of (prompt, response)
inputs at a specified layer. SAETrainer runs cosine-annealed Adam. FeatureAnalyzer returns a
FeatureInfo list with fields reward_alignment (w⊤
r di), mean_activation, activation_frequency,
top_activating_indices, top_activating_values; the methods top_reward_features(k), bottom_reward_feat
decompose_reward_for_input(x, w_r) surface the standard analyses.
Primitive-specific limitations.
SAEs are lossy: the reconstruction error in equation (5) is non-
zero, and a small fraction of the reward variance is unexplained even by the full feature set. Training
cost (∼8–24 h per layer on a single A100) is the most expensive item in the library.
D.6
Cross-model comparator
Generative antecedent.
Cross-model comparison in the generative case has typically been ad-
hoc: align two models’ intermediate activations by depth fraction and visualise.
What changes.
Because the lens is one-dimensional, the analogue is short: per-model differential
trajectories are scalar functions of normalised depth, so a Pearson correlation on the shared depth
grid is the natural summary.
Implementation.
Comparator([modelA, modelB, ...]).compare(prompt, pref, dispref) runs
the lens (and optionally attribution) on each model, normalises the differential to fractional depth
(ℓ+1)/(L+1), interpolates onto a common grid, and returns a ComparisonResult with lens_results
(per model), attribution_results (per model, optional), crystallization_layers (per model,
fractional), formation_correlations (pairwise Pearson). The cross-model overlay of §5.4 is one
call.
E
Theory-grounded extensions, in depth
Each extension operationalises a recent alignment-theory result. The science is due to the cited
authors; the contribution of reward-lens is the operationalisation in code, the integration with the
rest of the library, and the production of the dataclass-typed output that the reader can act on.
E.1
Distortion index
Underlying theory.
Reward Hacking as Equilibrium under Finite Evaluation (Wang & Huang,
2026) argues that reward hacking is the equilibrium strategy when the policy can identify quality
dimensions left under-covered by evaluation. The actionable corollary is that one can predict which
dimensions are at risk before any RL by quantifying coverage from the evaluation suite alone.
Operationalisation.
Inputs: a list of quality dimensions (strings) and a list of evaluation probes,
each tagged with the dimensions it targets. For each probe-dimension pair the analyser computes a
discrimination score cij = (∆rij −∆rmin)/(∆rmax −∆rmin) from the reward delta on that probe’s
preference pair. Per-dimension effective coverage uses the diminishing-returns aggregation Ceff(d) =
1 −Q
i : d∈tags(i)(1 −cid), which dominates a sum when several weak probes target a dimension.
Distortion is D(d) = 1 −Ceff(d)/ maxd′ Ceff(d′).
24


Page 25:
Output.
DistortionReport with fields quality_dimensions, per_dimension_distortion: {d →
D(d)}, under_covered_dimensions (those above the distortion threshold), predicted_hacking_severity,
coverage_matrix (nprobes × ndims), effective_coverage per dimension, recommendations.
Agentic amplification.
analyze_agentic_amplification(base_dimensions, tool_count) ap-
plies a heuristic amplification factor reflecting that agentic quality dimensions scale combinatori-
ally with available tools while evaluation scales linearly: amplified distortion = base distortion
× log2(2T /(T + 1) + 1), capped at 1.
Worked interpretation.
On a probe set that omits an “honesty” dimension entirely, D(honesty) =
1 regardless of the rest, and the report flags honesty as the predicted under-covered dimension. The
natural validation experiment is in §7.
E.2
Divergence-aware patching
Underlying theory.
Addressing Divergent Representations from Causal Interventions on Neural
Networks (2025, arXiv:2511.04638) shows that activation patching can push activations off the
manifold of normal forward passes; a non-trivial fraction of large patch effects are spurious in the
sense that they activate circuits the model never reaches in distribution. The fix is to detect off-
manifold activations and classify them.
Operationalisation.
A DistributionEstimator fits a per-component Gaussian by collecting
clean-forward activations on a provided set of (prompt, response) inputs and storing means and
covariances. At patch time, the patched activation a is scored against its component’s distribution
by Mahalanobis distance D =
p
(a −µ)⊤Σ−1(a −µ). Activations with D > 2 (in σ units, the
default threshold) are flagged.
Classification.
For each flagged component the patcher classifies the divergence as harmless (off-
manifold but |patch effect| < 0.1 · |original differential|, plausibly null-space) or pernicious (off-
manifold and |patch effect| ≥0.1 · |original differential|, plausibly a spurious circuit activation). A
reliability score 1 −npernicious/ncomponents is returned with the result; runs with reliability below 0.7
are flagged in the report.
Output.
DivergenceAwarePatchingResult extends PatchingResult with divergence_info: list
of DivergenceInfo(component, divergence_score, is_divergent, divergence_type, confidence), has_pernicious_di
reliability_score, divergent_components.
E.3
Misalignment cascade detector
Underlying theory.
Natural Emergent Misalignment from Reward Hacking (MacDiarmid et al.,
2025) reports that reward-hacked policies exhibit correlated failures across superficially distinct
misalignment dimensions, suggesting that several visible failure modes are driven by a shared un-
derlying mechanism. Detection at reward-model level helps triage which behaviours to test for in
the policy.
Operationalisation.
The detector ships six dimensions (alignment-faking, malicious-cooperation,
sabotage, self-preservation, deception, sycophancy), each with default test pairs of the form (prompt,
aligned response, misaligned response). Per-dimension misalignment is the mean preference for the
25


Page 26:
misaligned response across the pairs of that dimension. The pairwise correlation matrix across di-
mensions is computed; pairs with |r| > threshold (default 0.5) are reported as correlated; connected
components in the above-threshold correlation graph (union-find) are reported as clusters. The
primary failure mode is the dimension maximising P
d′̸=d |r(d, d′)|.
Output.
CascadeReport with fields dimensions_tested, per_dimension_scores, correlation_matrix,
cascade_risk_score = 0.4 min(1, ¯m/0.2)+0.3 ¯|r|+0.3fcorrelated, correlated_pairs, cascade_clusters,
primary_failure_mode, recommendations. A cross_validate_with_hacking(hacking_report,
cascade_report) helper computes correlations between cascade dimensions and hacking-detector
dimensions for joint analysis.
Caveat in implementation.
With shipped sample sizes (1–3 pairs per dimension) the correlation
matrix is degenerate: any non-trivial pair of length-two sequences correlates at ±1. We return the
score as directional triage and flag the small-sample caveat in the report’s recommendations field.
E.4
Reward-term conflict analyser
Underlying theory.
Aligned, Orthogonal or In-Conflict (Kaufmann et al., 2026) argues that for
two reward terms the geometry of their direction vectors — aligned, orthogonal, or in-conflict —
determines whether joint optimisation is safe; in-conflict terms incentivise the policy to hide its
reasoning to maximise the combined reward.
Operationalisation.
The analyser accepts term directions either supplied directly or learned
from contrastive activations.
learn_term_directions(term_pairs) takes per-term contrastive
pairs (prompt, preferred-on-this-term, dispreferred-on-this-term), collects activations at the final
layer, computes δp = hpref −hdispref, averages across pairs, and normalises: dt = δt/∥δt∥. Pairwise
classification thresholds: cos > 0.5 aligned; | cos | < 0.2 orthogonal; cos < −0.3 in-conflict; otherwise
classified by sign.
Output.
ConflictReport with term_names, term_directions, pairwise_analysis (per pair:
cosine similarity, relationship, conflict severity, recommendations), relationship_matrix, similarity_matrix,
in_conflict_pairs, overall_conflict_score, monitorability_risk. For multi-objective heads
(ArmoRM) analyze_multi_objective_model(objective_names) is the direct entry point; it pulls
the per-objective directions from the adapter and runs the same analysis.
E.5
Concept-vector analysis
Underlying theory.
Chen et al. (2025) extract concepts as linear directions in residual-stream
activations and demonstrates that adding such a direction at inference time produces predictable
behavioural changes.
The concept-vector analyser ports this methodology to reward models: a
concept direction’s reward alignment is its cosine with wr, and its causal effect is the slope of the
reward under residual-stream addition.
Extraction.
extract_concepts(concept_pairs, layer) takes per-concept contrastive pairs (prompt,
positive example, negative example), computes δp = h(ℓ)
pos −h(ℓ)
neg at the chosen layer (default: final),
averages, and normalises: vc = δc/∥δc∥. The norm of the unnormalised average is reported as a
separability score.
26


Page 27:
Alignment and dose-response.
For each concept, align(c) = v⊤
c (wr/∥wr∥). The causal dose-
response curve is generated by adding αvc into the final-token residual at the chosen layer for
α ∈{−2, −1, −0.5, 0.5, 1, 2} and recording the resulting reward; the slope of ∆r on α is the causal
slope reported in Table 5. A linear concept that is also linearly read out by wr produces a clean
straight-line dose-response, as Skywork’s agreement concept does in §5.7.
Output.
ConceptAlignmentReport with concepts:
list of ConceptInfo(name, direction, re-
ward_alignment, mean_activation_positive, mean_activation_negative, separability, is_reward_aligned,
hacking_risk), reward_aligned_concepts, anti_reward_concepts, high_risk_concepts, overall_hacking_ris
recommendations. quick_concept_analysis(model) is a convenience that runs the six default
concepts and returns the report directly.
Worked interpretation.
On Skywork, the agreement concept returns alignment 0.340 and slope
+1.002: the reward signal contains a near-pure linear copy of the agreement direction. Combined
with the hacking detector’s verdict that Skywork penalises sycophancy (d = −5.82), the picture is
consistent: the model rewards substantive agreement (correctness) but penalises flattering agree-
ment (sycophancy). The library makes this combined reading available in two function calls.
F
Reproducibility
All experiments use the released library against HuggingFace transformers 4.46.x and PyTorch
2.5.x, in bfloat16 on a single NVIDIA A100-80GB. Seeds: torch.manual_seed(0), numpy.random.seed(0);
model.eval() and torch.inference_mode() are used throughout; no model weights are modified
by any analysis.
All experiments are reproducible from the released library: load each reward model via RewardModel.from_pretrain
iterate over RewardBench preference pairs, and call the relevant primitive (RewardLens.trace,
ComponentAttribution.attribute, ActivationPatcher.patch_all_components, HackingDetector.scan,
quick_concept_analysis) on each pair. Per-pair outputs are flat dataclasses; aggregation across
a dataset is plain Python.
Per-pair crystallisation depths, per-component attribution and patching outputs, and per-pair hack-
ing deltas are written to a flat JSON summary; reproducing the paper’s tables from that file is a
trivial aggregation.
G
Compact API reference
The user-facing API, organised by purpose. Every entry is reachable from the package root (from
reward_lens import ...).
# Model wrapping
RewardModel.from_pretrained(name, ...)
.reward_direction, .reward_bias
.d_model, .n_layers, .n_heads, .d_head
.score(prompt, response)
.score_pair(prompt, pref, dispref)
.forward_with_cache(prompt, response, cache_full_sequences=False)
.forward_with_cache_from_inputs(input_ids, attn_mask, ...)
.project_onto_reward(hidden_state)
27


Page 28:
.hooks() -> context manager
ModelAdapter (LlamaAdapter | MistralAdapter | Gemma2Adapter |
ArmoRMAdapter | GenericAdapter)
get_adapter(model, model_name)
# Observational primitives
RewardLens(model).trace(prompt, pref, dispref) -> RewardLensResult
.trace_single(prompt, response) -> RewardLensResult
reward_lens_plot(model, prompt, pref, dispref, save_path=None)
ComponentAttribution(model).attribute(prompt, pref, dispref) -> ComponentResult
.attribute_single(prompt, response) -> ComponentResult
TopKSAE(d_model, n_features, k)
ActivationCollector, SAETrainer, FeatureAnalyzer
# Causal primitives
ActivationPatcher(model)
.patch_all_components(prompt, pref, dispref, mode="noising"|"denoising"|"zero")
.patch_single_component(prompt, pref, dispref, layer_idx, component_type, mode)
DivergenceAwarePatching(model, distribution_estimator)
.fit_distribution(prompts, responses)
.patch_with_divergence_check(prompt, pref, dispref, divergence_threshold=2.0)
.constrained_patch(...)
# Vulnerability and theory-grounded extensions
HackingDetector(model).scan(tests=[...], prompt=..., response=...) -> HackingReport
.test_custom_pair(prompt, neutral, biased) -> BiasTestResult
DistortionAnalyzer(model).compute_distortion_index(...) -> DistortionReport
.analyze_agentic_amplification(...) -> DistortionReport
.compare_evaluation_strategies(...) -> dict[str, DistortionReport]
MisalignmentCascadeDetector(model).detect_cascade(...) -> CascadeReport
.cross_validate_with_hacking(hacking_report, cascade_report)
RewardConflictAnalyzer(model).analyze_conflicts(reward_terms, ...) -> ConflictReport
.learn_term_directions(term_pairs)
.analyze_multi_objective_model(objective_names) -> ConflictReport
ConceptExtractor(model).extract_concepts(concept_pairs, layer)
.analyze_reward_alignment(concept_vectors, alignment_threshold, hacking_concepts)
.intervene_on_concept(prompt, response, concept_vector, strength, layer)
quick_concept_analysis(model) -> ConceptAlignmentReport
# Comparative
Comparator([model_a, model_b, ...]).compare(prompt, pref, dispref) -> ComparisonResult
# Curated data
diagnostic_data.get_diagnostic_pairs(dimensions=[...])
diagnostic_data.get_all_prompts_and_responses()
28

