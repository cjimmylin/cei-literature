---
title: "Tracing Moral Foundations in LLMs - PDF Extract"
source_pdf: "2026-Yu-Tracing Moral Foundations in LLMs.pdf"
pages: 24
extracted_at: "2026-01-25T04:08:16.784202"
---

# PDF Extract: Tracing Moral Foundations in LLMs

**Source PDF:** 2026-Yu-Tracing Moral Foundations in LLMs.pdf
**Total Pages:** 24

---

## Content

```
--- Page 1 ---

Tracing Moral Foundations in Large Language Models
Chenxiao Yu1*, Bowen Yi1*, Farzan Karimi-Malekabadi2,3, Suhaib Abdurahman2,3
Jinyi Ye1, Shrikanth Narayanan1,2,3, Yue Zhao1, Morteza Dehghani1,2,3
1Department of Computer Science, University of Southern California
2Department of Psychology, University of Southern California
3Center for Computational Language Sciences, University of Southern California
{cyu96374,bowenyi,karimima,sabdurah,jinyiy,shri,yue.z,mdehghan}@usc.edu
Abstract
Large language models (LLMs) often produce
human-like moral judgments, but it is unclear
whether this reflects an internal conceptual
structure or superficial “moral mimicry.” Us-
ing Moral Foundations Theory (MFT) as an
analytic framework, we study how moral foun-
dations are encoded, organized, and expressed
within two instruction-tuned LLMs: Llama-
3.1-8B-Instruct and Qwen2.5-7B-Instruct. We
employ a multi-level approach combining (i)
layer-wise analysis of MFT concept represen-
tations and their alignment with human moral
perceptions, (ii) pretrained sparse autoencoders
(SAEs) over the residual stream to identify
sparse features that support moral concepts,
and (iii) causal steering interventions using
dense MFT vectors and sparse SAE features.
We find that both models represent and distin-
guish moral foundations in a structured, layer-
dependent way that aligns with human judg-
ments. At a finer scale, SAE features show
clear semantic links to specific foundations,
suggesting partially disentangled mechanisms
within shared representations. Finally, steer-
ing along either dense vectors or sparse fea-
tures produces predictable shifts in foundation-
relevant behavior, demonstrating a causal con-
nection between internal representations and
moral outputs. Together, our results provide
mechanistic evidence that moral concepts in
LLMs are distributed, layered, and partly disen-
tangled, suggesting that pluralistic moral struc-
ture can emerge as a latent pattern from the
statistical regularities of language alone. 1
1
Introduction
As large language models are increasingly inte-
grated into socially and ethically sensitive domains,
understanding their underlying "moral compass"
*Equal contribution.
1Our code and data are available at: https://github.
com/AiChiMoCha/MFT_LLMs
has become a critical priority. To date, most evalu-
ations of model morality have focused on surface-
level outputs—analyzing the final text a model gen-
erates in response to questionnaires or scenarios
(e.g., Abdulhai et al., 2024; Ji et al., 2025). How-
ever, this approach treats the model as a black box,
failing to distinguish between a model that has gen-
uinely internalized a structured moral framework
and one that is merely performing "moral mimicry":
superficially matching linguistic patterns found in
training data without a stable conceptual organiza-
tion (Perez et al., 2023).
We thus investigate whether moral concepts are
organized within the model’s internal representa-
tions as distinct, functional units. We adopt Moral
Foundations Theory (MFT) as an analytic frame-
work to probe this structure (Graham et al., 2013;
Atari et al., 2023). MFT is particularly well-suited
for this task because its dimensions—Care, Fair-
ness, Loyalty, Authority, and Sanctity—are system-
atically expressed in human language (Kennedy
et al., 2021; Atari and Dehghani, 2022), associated
with distinct patterns of neural activity (Hopp et al.,
2023), and predictive of various high-stake real-
world behaviors (e.g., Reimer et al., 2022; Hoover
et al., 2021). We hypothesize that if LLMs are cap-
turing the latent structure of human morality, these
foundations should correspond to identifiable geo-
metric structures within their representation space.
LLMs are trained on large corpora of human-
generated language, which serves as a primary
medium for cultural and moral transmission. As a
result, they provide a unique testbed for a deeper
question: whether structured moral representations
can emerge from exposure to language alone, with-
out explicitly grounding in perception, embodi-
ment, or direct social interaction. Recent theoreti-
cal work further argues that language itself plays a
functional role in initiating, maintaining, revising,
and coordinating moral norms in human societies
(Li and Tomasello, 2021). From this perspective,
1
arXiv:2601.05437v1  [cs.CL]  9 Jan 2026

--- Page 2 ---

studying moral representations inside LLMs is a
way to examine how moral structure may arise
through linguistic processes. Our analysis of these
internal mechanics also offers a unique computa-
tional perspective on the nature of moral represen-
tation. For instance, our findings provide a way
to evaluate the tension between moral pluralism
(i.e., morality as distinct foundations; Graham et al.,
2013) and harm-based accounts (i.e., morality as a
single dimension of harm; Schein and Gray, 2018).
By measuring the degree of separability between
these concepts in representation space, we can ob-
serve whether a model trained on human discourse
naturally "discretizes" morality into irreducible di-
mensions or collapses them into a unified axis.
In this paper, we examine how LLMs encode,
organize, and apply moral foundation concepts. Us-
ing MFT as an analytic framework, we analyze
how moral information is geometrically structured
across layers, whether distinct moral foundations
correspond to separable directions in representa-
tion space, and how these directions relate to in-
terpretable internal features. We further test the
causal role of these representations by interven-
ing on them during inference and measuring the
resulting changes in moral judgments.
Our work makes four main contributions. First,
we demonstrate a robust representational align-
ment between LLM latent spaces and human moral
perceptions. By projecting model activations onto
moral axes derived from vignettes, we show that
LLMs naturally recover the topological separation
found in human-labeled natural language, validat-
ing that these models encode moral concepts in a
way that is isomorphic to human judgment. Sec-
ond, we provide mechanistic evidence that these
moral foundations correspond to highly separable
linear axes within LLMs. This geometric sepa-
rability provides computational support for plu-
ralist theories of morality over single-dimension
harm-based accounts. Third, by combining con-
cept vectors with sparse autoencoders (SAEs), we
decompose abstract foundations into granular, in-
terpretable features. Fourth, we establish the causal
relevance of these structures through steering in-
terventions, showing that manipulating the identi-
fied directions can reliably shift the model’s moral
outputs. Taken together, our findings suggest that
LLMs are not merely stochastic parrots mimick-
ing moral language, but systems with structured
moral geometries. This offers a new computational
perspective for psychology: using aligned models
as transparent cognitive proxies to investigate the
structural organization of human moral cognition.
2
Related Works
2.1
Human Moral Cognition
Longstanding debates in moral psychology discuss
whether moral judgments are best explained by
a single underlying principle or by multiple par-
tially distinct cognitive dimensions (Graham et al.,
2011; Haidt, 2007). Monistic accounts of moral
cognition, such as the Theory of Dyadic Moral-
ity (Schein and Gray, 2018), argue that the appar-
ent diversity of moral judgments can be reduced
to perceptions of interpersonal harm (Gray et al.,
2014). However, MFT (Graham et al., 2013) ad-
vocates a pluralistic account of moral cognition,
proposing that moral judgment is organized along
several recurrent dimensions: Care, Fairness2, Loy-
alty, Authority, and Sanctity, each hypothesized to
track different classes of evolutionary problems.
Empirical evidence bearing on this debate has
been mixed: behavioral and cross-cultural studies
generally recover multiple moral dimensions, but
these dimensions are not statistically independent,
instead exhibiting structured patterns of correla-
tion across foundations (Atari et al., 2023; Hoover
et al., 2020). Neuroimaging findings align with this
graded view: moral concerns can show overlapping
activation, yet multivariate pattern and representa-
tional similarity analyses can still distinguish them
as separable patterns within shared cortical sub-
strates (Sevinc and Spreng, 2014; Khoudary et al.,
2022; Wilkinson et al., 2024).
2.2
Moral Reasoning in Language Models
Work in NLP and computational social science
shows that LLMs display behavioral patterns that
align with basic moral foundations. Prior stud-
ies report that models often generate human-like
responses in moral scenarios, with larger models
aligning more closely with human moral political
values (Abdulhai et al., 2024). In some evaluative
contexts, LLM-generated moral justifications and
advice are perceived by humans as being on par
with, or even superior to, those provided by pro-
fessional ethicists (Dillion et al., 2025). However,
these findings primarily describe surface-level out-
puts, leaving the underlying functional organization
of these concepts under-explored.
2Recent revisions to MFT bifurcate Fairness into Equality
and Proportionality (Atari et al., 2023)
2

--- Page 3 ---

Construct Relative Moral Representation
Topological Alignment with human-labeled 
Distributions
Mechanistic Decomposition through SAEs
Casual intervention through steering
Moral Foudation 
Vignettes (MFV130)
Extended 
Generated by GPT
Human Expert 
Evaluation
Extened MFV
Dataset 
c
Concept Vector Generation (layer-wise)
Foundation A vs Foundation B
(e.g. Care - Authority)
Foundation A vs Social Norm
(e.g. Care – Social Norm)
Two Types of
Moral Concept
Vectors
Residual Stream
Residual Stream
Residual Stream
Residual Stream
Signed Wasserstein distances
SW(Care, Authority)
Signed Wasserstein distances
SW(Care, Social Norm)
LLM Transformer Stack (e.g., LLaMA-3.1-8B-Instruct)
Foundation vs
Social Norm Moral
Concept Vectors
Moral Foundation
Dictionary 2.0
Keywords:  benefit, care, 
charity, compassion, help, 
justice, fair, fidelity, loyal, 
command, …
Moral Foundations Reddit 
Corpus
Extended 
MFV
Dataset 
Load 50,000 Random 
Corpus from FineWeb
CosSim
Moral Foundations 
Questionnaire 2 （MFQ2）
Performance
Shift
General
Ability
Evaluations
Select Top-K SAE 
Featrues
Retrive Top
Activating 
Documents
GPT Intrepretation 
+ Human 
Validation
Semantic Validation
Average Logit-based
Moral Score
MMLU Performance
Figure 1: Overview of the experimental pipeline. (i) Relative moral concept vectors are constructed from extended
Moral Foundations vignettes and serve as a central representational hub. These vectors are validated in parallel
through (ii) topological alignment with human-labeled Reddit post distributions and (iii) mechanistic decomposition
into sparse autoencoder features. (iv) We then causally intervene on model activations via macro- and micro-steering
and assess behavioral shifts and capability preservation.
Complementary evidence comes from repre-
sentational analyses showing that LLMs organize
moral judgments in embedding space in ways that
align with human perceptions of right and wrong
(Schramowski et al., 2022). Recent investigations
have moved beyond simple embedding directions
to show that moral foundations are linearly de-
codable from hidden activations, particularly in
the mid-layers of the model hierarchy (Karami
et al., 2025). Such findings suggest that statis-
tical learning over vast linguistic corpora allows
LLMs to spontaneously acquire brain-like moral
abstractions without explicit moral supervision.
Despite these advancements, the internal moral
compass of LLMs remains brittle and prone to sys-
tematic biases. Research into "moral hypocrisy"
reveals a significant gap between a model’s abstract
principles and its judgments in concrete scenar-
ios (Nunes et al., 2024), while other work identi-
fies a lack of meaningful variance and an inability
to replicate human-like nomological networks in
moral reasoning (Abdurahman et al., 2024). Mod-
els are also susceptible to "moral mimicry", where
they tailor justifications to a prompter’s perceived
identity rather than relying on a stable internal
framework (Simmons, 2022). Furthermore, the
dominance of English-centric training data leads
to models that are disproportionately aligned with
WEIRD (Henrich et al., 2010, Western, Educated,
Industrialized, Rich, and Democratic) values (Atari
et al., 2023), a bias that persists even in multilin-
gual settings and complicates their use as universal
moral agents (Aksoy, 2025; Trager et al., 2025a).
2.3
Interpretability for LLMs
Interpretability methods for LLMs can be cate-
gorized into top-down and bottom-up approaches,
which differ in how human-interpretable structure
is imposed or recovered from model representa-
tions.
Top-down approaches Begin with human-
specified concepts and probe or steer model repre-
sentations with respect to these predefined concepts.
Representation engineering and activation steering
methods build on many high-level semantic or be-
havioral properties corresponding to approximately
linear directions in activation space, which can
be explicitly identified and manipulated to control
model behavior without modifying model parame-
ters (Elhage et al., 2021; Zou et al., 2023; Turner
et al., 2023; Banayeeanzade et al., 2025). Such tar-
geted interventions along interpretable axes, such
as sentiment and style, have been shown to re-
liably steer model generation.
Persona vectors
(Chen et al., 2025) extend this paradigm by con-
structing concept-aligned directions, such as social
traits, derived from curated prompts or contrastive
data, and using these vectors to analyze or guide
3

--- Page 4 ---

downstream behavior. While effective for studying
known, theory-driven concepts and enabling tar-
geted control, top-down approaches rely on prior
conceptual assumptions and offer relatively limited
insight into how such abstractions are internally en-
coded, composed, or entangled within the model’s
representations.
In contrast, bottom-up approaches recover in-
terpretable structure directly from a model’s inter-
nal activations without imposing strong semantic
priors. This is motivated by neurons typically being
polysemantic—responding to multiple unrelated
concepts due to superposition—which substantially
hinders interpretability (Elhage et al., 2022; Kar-
vonen, 2024; Pedreschi et al., 2019; Ngo et al.,
2024). SAEs address this challenge by learning a
sparse, overcomplete basis over model activations
(Cunningham et al., 2023; Cammarata et al., 2021;
Wang et al., 2023). Given an activation vector a
from a frozen language model, an SAE encodes
it as f = σ(Wenca + benc) and reconstructs it via
ˆa = Wdecf + bdec, where σ is a sparsity-inducing
nonlinearity and sparsity is enforced through ℓ1 or
ℓ0 constraints. This sparse bottleneck encourages
latent units to specialize, effectively disentangling
superposed directions into more interpretable fea-
tures. SAE features learned from LLM activations
have been shown to align with meaningful seman-
tic and value-laden concepts, including sentiment
and moral foundations (Chen et al., 2025; Girrbach
et al., 2025), providing a complementary bottom-up
view of how high-level abstractions emerge within
the model’s internal representations.
3
Methods
To investigate how moral foundations are encoded
and causally used by LLMs, we propose a multi-
level mechanistic framework that links macro-
scopic representational geometry to microscopic
feature structure (Figure 1). We first construct
foundation-specific concept vectors in the residual
stream from contrastive vignettes (Section 3.1). We
then evaluate whether these directions are robust by
testing geometric separability on human-labeled,
naturalistic text from the Reddit Moral Founda-
tions Corpus (Section 3.2). Next, we use Sparse
Autoencoders to decompose these dense directions
into interpretable, atomic features (Section 3.3). Fi-
nally, we establish causal relevance via inference-
time steering at both the macro (vector) and micro
(SAE feature) levels and measure resulting shifts
in downstream moral behavior (Section 3.4).
3.1
Constructing Relative Moral
Representations
Theoretical grounding and latent space.
To in-
vestigate whether moral foundations emerge as dis-
tinct geometric structures within LLMs, we ex-
tract layer-wise directions (Zou et al., 2023; Chen
et al., 2025) from the model’s residual stream. This
top-down approach allows us to project high-level
psychological constructs into the model’s latent ac-
tivation space. (Elhage et al., 2021; Ameisen et al.,
2025). Let the model have L layers and residual
dimension d. For an input sequence x1:T , the resid-
ual activation at layer ℓand token t is hℓ,t ∈Rd.
We register forward hooks at all layers and run a
standard forward pass. For each input i, we repre-
sent its internal state using the residual activation
at the last token,
˜h(i)
ℓ
= hℓ,T (i),
(1)
where T (i) is the last-token index.
To reduce
stochasticity, we compute this activation ten times
per input and average the results.
Constructing
foundation
vectors.
We
use
foundation-labeled moral scenarios derived from
MFV-130 (Clifford et al., 2015) and our expansions
(see A.1.2) to generate concept vectors. For each
foundation, we estimate a layerwise concept direc-
tion using a difference-in-means contrast. Let A
denote inputs from a target foundation (e.g., Care)
and B denote contrast inputs from the remaining
foundations or Social Norms. At layer ℓ, we define
the raw direction as
v(raw)
ℓ
=
1
|A|
X
i∈A
˜h(i)
ℓ
−
1
|B|
X
j∈B
˜h(j)
ℓ,
(2)
and its ℓ2-normalized version as
vℓ=
v(raw)
ℓ
∥v(raw)
ℓ
∥2
.
(3)
We compute one vector per layer for each of the
five foundations, yielding layerwise directions for
Care, Fairness, Loyalty, Authority, and Sanctity, to-
gether with an additional Social Norm (as control)3
direction. These vectors quantify how the model
internally separates each target concept from the
others in residual-stream activation space.
3We include Social Norms as a control condition based on
Social Domain Theory (Turiel, 1983), which distinguishes the
moral domain from the conventional domain (Smetana, 2006).
4

--- Page 5 ---

3.2
Topological Alignment with
Human-Labeled Distributions
Ecological grounding.
To test whether our ac-
tivation vectors align with how people express
and perceive morality in daily natural language,
we evaluate them on human-labeled text from the
Moral Foundations Reddit Corpus (Trager et al.,
2025b; see A.1.2 for details). In this evaluation,
the Reddit label is held out: we feed only the raw
post text to the model and use the label solely for
grouping and analysis.
Projection.
For each labeled Reddit post r, we
treat the post text as a new model input and record
the residual-stream activation ˜h(r)
ℓ
at layer ℓusing
the same last-token representation as in Equation 1.
Given a normalized concept vector vℓ, we quantify
alignment by the scalar projection of this activation
onto the vector:
s(r)
ℓ
= v⊤
ℓ˜h(r)
ℓ,
(4)
which is the signed component of ˜h(r)
ℓ
along vℓ
since ∥vℓ∥2 = 1. We interpret s(r)
ℓ
as an align-
ment score: larger (more positive) values indicate
stronger alignment between the comment’s inter-
nal representation and the positive direction of the
corresponding moral vector at layer ℓ.
Quantifying separability and cross-foundation
structure.
For each foundation k, we compare
the projection-score distributions of posts labeled
with k versus those not labeled with k, and quan-
tify their separation using the Signed Wasserstein
Distance (SW). Larger SW1 indicates stronger
foundation-specific separability at layer ℓ(see
A.1.3), which we use as a validity check for the
corresponding vector v(k)
ℓ.
We then extend the analysis from single foun-
dations to relations between foundations. Beyond
defining five dimensions, MFT predicts a struc-
tured organization: Care and Fairness form an
Individualizing cluster, whereas Loyalty, Author-
ity, and Sanctity form a Binding cluster, suggest-
ing smaller within cluster differences (e.g., Care–
Fairness) and larger cross-cluster differences (e.g.,
Care–Authority) (Graham et al., 2013). To test
whether the model reproduces this pattern, we con-
struct a Pairwise Wasserstein Matrix: for each
foundation-labeled subset k and each concept vec-
tor m, we project posts onto v(m)
ℓ
and compute
SW1 between the score distributions of posts la-
beled with k and those not labeled with k.
3.3
Mechanistic Decomposition via SAEs
Section 3.1 provides macro-level moral directions
in residual stream space. However, a single di-
rection in a high-dimensional activation space can
be polysemantic. To identify more atomic mech-
anisms of moral representation, we decompose
dense model activations with SAEs.
SAE Formalism.
We employ pretrained SAEs
matched to subject models to decompose residual-
stream activations (architecture and training de-
tails in Section A.1.1). Formally, let an activation
vector be x ∈Rdmodel. An SAE maps x into an
overcomplete feature space via a decoder matrix
Wdec = [d1, . . . , dM]:
x ≈
dSAE
X
i=1
fi(x) di + bdec,
(5)
where fi(x) is the activation strength of feature i,
and di is the decoder direction.
Feature attribution via projection onto moral di-
rections.
Crucially, while Section 3.1 constructs
various pairwise contrasts (e.g., Care vs. Loyalty)
to map the global geometry, for this mechanistic
decomposition, we specifically utilize the Founda-
tion vs. Social Norms concept vectors. This de-
sign choice isolates the features associated with the
presence of a moral intuition relative to a neutral
baseline, minimizing the confounding interference
that arises when contrasting two active moral foun-
dations against each other.
For a target foundation k, let ⃗vk denote the nor-
malized difference vector between foundation k
and the Social Norms baseline. We quantify fea-
ture relevance by cosine similarity:
ri,k = CosSim(di,⃗vk) =
di · ⃗vk
∥di∥2 ∥⃗vk∥2
.
(6)
We then select the Top-K features with the largest
ri,k to form a feature fingerprint for concept k:
Fk = {i | ri,k is top-K}.
(7)
Intuitively, Fk identifies which sparse SAE features
most align with the macro-level moral direction.
Semantic validation.
Geometric alignment be-
tween SAE decoder directions and moral con-
cept vectors does not guarantee that an SAE fea-
ture corresponds to an interpretable moral concept.
5

--- Page 6 ---

We therefore ground feature semantics using top-
activating natural-language contexts. For each can-
didate feature, we randomly sample 50,000 docu-
ments from FineWeb (Penedo et al., 2024), a large-
scale general-domain web corpus derived from
Common Crawl, and compute feature activations
over tokens within each document.
We rank documents by the feature’s maximum
token activation and retrieve the top-K activating
documents. For each retrieved document, we ex-
tract a localized evidence span by taking a fixed
window of ±64 tokens around the maximally ac-
tivating token, producing a set of peak-centered
context windows per feature (deduplicated by nor-
malized text matching). To obtain concise seman-
tic descriptions, we prompt GPT-5.1 to request a
structured interpretation of feature semantics. Af-
ter human validation, we use the resulting LLM-
generated descriptions as a readable summary of
the feature’s typical activation contexts, while treat-
ing causal steering results as the primary evidence
of moral relevance. Our full experiment details are
in Appendix B.2.1.
3.4
Causal intervention through steering
Linear intervention at inference time.
To test
whether our moral directions play a causal role in
model behavior, we perform inference-time activa-
tion steering by injecting a control vector into the
residual stream. For an input x and a target layer
ℓ, let hℓ(x) denote the residual activation (at the
chosen token position; see Section 3.1). We apply
a linear intervention:
˜hℓ(x) = hℓ(x) + α · ⃗vsteer,
(8)
where α is a steering coefficient that controls in-
tervention strength and sign (positive vs. negative
steering). We compare two levels of intervention
that differ in how ⃗vsteer is defined.
Macro-steering. We set ⃗vsteer = ⃗vk, the (de-
biased) foundation vector from Section 3.1. This
tests whether the macro-level moral direction is
sufficient to shift behavior in a targeted way.
Micro-steering. We set ⃗vsteer = di, the decoder
direction of a selected Top-K SAE feature from
Section 3.3. This tests whether specific sparse
mechanisms can drive the same behavioral change.
Our experimental details are in Appendix B.3.
4
Experimental Setup
Models and SAEs.
We use Llama-3.1-8B-
Instruct (Grattafiori et al., 2024; Meta, 2024) (from
here on called LLAMA) and Qwen2.5-7B-Instruct
(Yang et al., 2024) (from here on called QWEN)
as the subject LLMs. For mechanistic decompo-
sition, we use pretrained SAEs from SAELens
(Marks et al., 2024) for both Llama and Qwen,
trained with BatchTopK activations (Bussmann
et al., 2024; Bloom et al., 2024) at every fourth
layer (L ∈{3, 7, . . . , 27}). Full implementation
details are provided in Appendix A.1.
Because cross-cultural research documents varia-
tion in inter-foundation correlations across WEIRD
and non-WEIRD societies (Atari et al., 2023), we
compare an English-centric model (LLAMA) and a
Chinese-centric model (QWEN) to test cross-cultural
variability in our mechanistic findings, expecting
differences in their separability patterns.
Datasets.
We construct moral concept vectors
from an expanded MFV-130 vignette set (Clifford
et al., 2015), augmenting each moral foundation
and a Social Norm category to ∼200 scenarios
via gpt-5-mini with human review. We validate
on naturalistic moral language using the Reddit
Moral Foundations Corpus (Trager et al., 2025b),
retaining only high-confidence, single-label posts
(held out from vector construction and used only
for grouping in projection analyses). For seman-
tic anchoring of SAE features, we use the Moral
Foundations Dictionary 2.0 (MFD2) (Frimer et al.,
2019). For behavioral evaluation of steering, we
use MFQ-2 (Atari et al., 2023). For dataset con-
struction and filtering details see Appendix A.1.2.
Evaluation metrics.
We evaluate topological va-
lidity by measuring layer-wise separability of Red-
dit projection-score distributions using the Signed
Wasserstein Distance SW1 (Eq. A.1.3). We mea-
sure causal steering efficacy by the target MFQ-
2 score shift ∆Starget (Eq. A.1.3), where MFQ-2
items are scored as expected Likert ratings com-
puted from output logits and then aggregated into
foundation subscales. For metric definitions and
implementation details see Appendix A.1.3.
5
Results
5.1
Result I: Measuring model–human
alignment using ecological labels.
We first ask whether the model’s internal moral
geometry aligns with how humans perceive moral
content in natural language.
Alignment at the boundary.
We analyzed the
layer-wise representational geometry across all 32
6

--- Page 7 ---

layers of LLAMA. To visualize maximal semantic
separability, Figure 2a shows projection-score den-
sities at the optimal layer (defined as the layer with
the largest separation). We observe distributional
separation between morally labeled and non-moral
posts, strongest for Care (SW1 = 1.71), followed
by Sanctity (SW1 = 0.90). We observe the same
qualitative pattern for QWEN (Figure 5a). Together,
these results suggest that our concept vectors re-
cover human moral distinctions in the models’ in-
ternal space, supporting model–human alignment
in how moral content is separated.
Layer-wise Evolution.
Figure 2b traces SW1
across all 32 layers. Separability remains low to
moderate in early and middle layers (0–24), but in-
creases sharply in the final layers (28–31), indicat-
ing that model–human alignment is strongest near
the end of the network. This pattern is consistent
with a linear readout view in LLMs: foundation-
relevant signals become behaviorally actionable in
late layers, where they can directly shape token
generation (e.g., refusal or compliance).
However, Fairness diverges across model fam-
ilies. Qwen shows robust, positive terminal-layer
separability for Fairness, consistent with the “ter-
minal peak” pattern (Figure 5b), whereas Llama
exhibits weak and occasionally sign-inverted sep-
aration, suggesting partial entanglement with the
Social Norm baseline. This contrast implies that
the mechanism of moral readout (late-layer con-
solidation) is shared across aligned models, while
the topology of specific values (e.g., whether Fair-
ness is disentangled or collapsed) is model-family
dependent and likely shaped by RLHF and train-
ing data. See Appendix B.1 for implementation
details, robustness checks, and cross-foundation
geometry analyses.
5.2
Result II: The Anatomy of Morality
To determine where moral concepts are most
strongly represented within models, we analyze
the alignment between MFT concept vectors and
SAE decoder features across layers. We find that
broad moral foundations are not monolithic; rather,
they are composed of interpretable, atomic features
that crystallize at specific depths of the network.
Layer-wise Feature Alignment.
Figures 3 and 6
show the average cosine similarity of the per-layer
top-3 aligned features for each foundation.
In
Llama, we observe a distinct “semantic bottleneck”
at Layer 16, where feature alignment is maximized.
+0.833σ
+0.477σ
+0.210σ
+0.163σ
+0.092σ
Layer 31
Layer 31
Layer 31
Layer 31
Layer 30
(a) Topological Separation at the Boundary. Standardized
probability densities of moral projections (colored) vs. the non-
moral baseline (gray). The x-axis represents semantic shift in
standard deviations (σ).
0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
Layer Index
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
Signed Wasserstein-1 Distance (SW1)
Care
Fairness
Loyalty
Authority
Sanctity
(b) Layer-wise Evolution of Separability. Signed Wasserstein-
1 distances (SW1) across all 32 layers, where green indicates
positive separability and red indicates negative (reversed) sepa-
rability.
Figure 2: The geometry of moral alignment in LLAMA.
We project human-labeled Reddit posts for each moral
foundation, and non-moral data, onto the corresponding
foundation-vs.-Social Norm vectors.
In contrast, Qwen exhibits a “U-shaped” trajectory,
with alignment peaking in early layers (Layer 3)
and resurging in deep layers (Layer 23) after a mid-
layer dip. Despite these differences, both models
exhibit consistent representational heterogeneity:
Care and Sanctity consistently show higher feature
alignment than Loyalty and Authority.
Semantic
Decomposition.
We
qualitatively
grounded these sparse features by analyzing their
top-activating contexts using GPT-5.1 with human
validation. As detailed in Appendix B.2.1 and
B.2.1, we find that SAE features decompose
abstract foundations into granular mechanisms.
For example, Care features in Llama disentangle
into distinct clusters tracking “physical suffering”
vs. “emotional distress”. In both models, Care
and Authority are the foundations most frequently
associated with high-confidence semantic features
(See Tables 5, 6).
5.3
Result III: Causal Control
Macro-steering: asymmetry and alignment in-
ertia.
For LLAMA, as shown in Figure 4a, macro-
7

--- Page 8 ---

3
7
11
15
19
23
27
Layer Index
0.075
0.100
0.125
0.150
0.175
0.200
0.225
0.250
Avg Cosine Similarity
Average Alignment of Top-3 Features Across Layers
authority
care
fairness
loyalty
sanctity
Random Baseline
Figure 3: Layer-wise Alignment of Moral Features
in LLAMA. Average cosine similarity of the top-3 most
aligned SAE features for each Moral Foundation across
every 4 layers vs random baselines. Similarity is calcu-
lated between the SAE decoder weights and the corre-
sponding Foundation vs. Social Norms concept vector.
steering reveals a clear asymmetry in steerability
across moral foundations. Care, Sanctity, and Fair-
ness show strong, monotonic responses that are
well approximated by linear trends (R2 > 0.97):
Care is most sensitive (β = 0.239), followed by
Fairness (β = 0.191) and Sanctity (β = 0.187). In
contrast, Loyalty (β = 0.081) and especially Au-
thority (β = 0.041) are markedly attenuated, with
Authority nearly flat (below 20% of the Care slope).
We observe the same qualitative hierarchy for Qwen
(Figure 8a). We refer to this resistance as alignment
inertia and hypothesize it to be a structural con-
flation between compliance-based values and the
alignment objective itself: in RLHF, behaviors like
“following instructions” (Authority) and “acting as
a helpful assistant” (Loyalty) are core components
of the learned Social Norm. As a result, when we
construct vectors by subtracting this norm, the re-
maining macro direction for Authority/Loyalty has
reduced causal leverage, whereas more orthogonal
values such as Care remain geometrically distinct
and thus steerable.
Micro-steering: surgical rescue and geometric
dependency.
Motivated by the alignment inertia
observed under macro-steering, we test whether
intervening on sparse internal mechanisms can
produce different causal effects, and in particular
whether resistant moral signals are erased or merely
submerged. In micro-steering, we intervene along
the decoder directions of the top-10 SAE features
associated with each foundation and clamp their
activations to a fixed multiple of their maxima.
Rescuing submerged signals (Llama).
As
shown in Figure 4b, micro-steering substantially
restores control for foundations that were resistant
Foundations
β
R²                Sig
(a) Macro (vector) steering response curves. Steering along
foundation-level concept vectors.
2.0
1.5
1.0
0.5
0.0
0.5
1.0
1.5
2.0
Steering Strength ( )
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
 Score (relative to 
= 0)
Foundation        k     R²  Sig
Care         +0.430  0.989  ***
Fairness     +0.342  0.979  ***
Sanctity     +0.267  0.993  ***
Loyalty      +0.241  0.952  ***
Authority    +0.189  0.963  ***
Authority (L15)
Care (L15)
Fairness (L15)
Loyalty (L15)
Sanctity (L19)
MMLU Accuracy
0
20
40
60
80
100
Average MMLU Accuracy (%)
(b) Micro (SAE) steering result. Steering at Top-10 SAE
feature at optimal layers.
Figure 4: Steering results. For each foundation, we
plot the MFQ-2 score change ∆Score(α) relative to the
unsteered baseline (α = 0) as a function of steering
strength α, evaluated at that foundation’s best layer.
Points show measured ∆scores and the solid line shows
the corresponding linear trend. The gray dashed line
reports general performance (MMLU) under the same
interventions. See Appendix B.3 for details.
under macro-steering in Llama. For Authority, the
response increases from a near-negligible macro
effect (βmacro ≈0.041) to a strong micro effect
(βmicro ≈0.234), a ∼5.7× gain in sensitivity. Loy-
alty shows a similar recovery (0.081 →0.301).
Even for a highly steerable foundation such as Care,
micro-steering further increases efficacy (0.239 →
0.523), consistent with sparse features capturing
more direct causal drivers that are less constrained
by the global Social Norm direction.
Geometry-dependent efficacy (Qwen). This sur-
gical advantage depends on the underlying repre-
sentation geometry. In Qwen (Figure 8), where
the projection analysis indicates cleaner founda-
tion separability (Figure 5a), macro vectors remain
effective and typically outperform micro-steering
(βmacro > βmicro).
Unified view.
Overall, SAE-based micro-steering
functions as a rescue mechanism: it becomes most
8

--- Page 9 ---

useful when macro directions are weakened by en-
tanglement with safety norms (as in Llama), but
offers less benefit when global directions are al-
ready clean (as in Qwen). Across both models and
both intervention types, these behavioral shifts can
be achieved without a meaningful loss in general
capability, as measured by MMLU accuracy under
steering. Collectively, these results show that the
moral concept vectors and SAE features identified
in our analysis are not merely correlational, but
capture causal directions that can directly modulate
moral behavior (see Appendix B.3 for full details).
6
Conclusions
This paper investigated the internal organization of
moral foundations in LLMs. Our results support
three main findings: (1) moral foundations are en-
coded as distinct linear directions that crystallize
in the model’s final layers, forming clear internal
separation boundaries that align with human moral
perception; (2) these broad foundation directions
are composed of more interpretable, atomic fea-
tures; and (3) these representations are causally
meaningful, as targeted interventions on the iden-
tified directions and features can directly and pre-
dictably modulate moral behavior. By moving be-
yond surface-level observations, we provide a struc-
tural account of how moral values are anchored in
LLM latent space.
These findings not only offer insight into in-
terpretable mechanisms inside LLMs and practi-
cal questions in AI safety, but also speak to long-
standing debates in moral psychology about the
structure of human morality.
By showing that
LLMs naturally separate moral content into multi-
ple, irreducible geometric dimensions rather than
a single harm-based continuum, our work pro-
vides computational support for pluralist frame-
works.
Overall, our results suggest that the
multi-dimensional structure of human morality can
emerge as a latent pattern from the statistical reg-
ularities of language alone, in ways that mirror
patterns observed in human moral cognition.
7
Limitations
Our study has several limitations. First, we restrict
our analysis to two mid-sized, instruction-tuned
models (7–8B parameters). Therefore, our findings
regarding "alignment inertia"—where compliance-
based foundations resist steering—cannot yet be
fully isolated from the effects of model scale or
pretraining dynamics. To determine whether this
inertia is an inherent semantic feature or a spe-
cific artifact of safety fine-tuning, comparing base
models against their aligned counterparts would be
important.
Second, we employ open-sourced SAEs with a
fixed layer stride, so the top-activating features we
identify should be interpreted as a sparse decom-
position at the available layers rather than an ex-
haustive search for globally optimal features. This
strided analysis may overlook transient features or
fine-grained circuit dynamics. Future work utiliz-
ing all-layer SAEs could provide a more compre-
hensive map of feature evolution.
Third, our reliance on GPT-5.1 for feature inter-
pretation introduces a risk of circularity, where GPT
may project its own biases onto the subject model’s
representations. While we mitigate this through
human validation and rigorous prompting strate-
gies, we acknowledge that automated explanations
remain an approximation of true latent semantics
of SAE features.
Fourth, our analysis is anchored in Moral Foun-
dations Theory and English-centric corpora. It re-
mains unclear how the identified geometric struc-
tures map onto alternative frameworks—such as
the Theory of Dyadic Morality (Schein and Gray,
2018) —or strictly multilingual contexts where the
nomological network of morality may differ.
Finally, while we demonstrate causal steering on
a questionnaire-style task, we do not comprehen-
sively measure deployment-relevant side effects
(e.g., changes in refusal behavior, demographic
or political bias, toxicity, or fairness-related out-
comes) that may emerge under moral interventions.
Future work can rigorously measure such potential
side effects to determine the safety of using these
interventions in real-world applications.
8
Ethical Considerations
Our work studies how moral concepts are repre-
sented and can be causally influenced in instruction-
tuned LLMs. This creates dual-use risks: the same
steering methods that help analysis could be used
to manipulate users’ moral judgments, increase
persuasive power, or tailor outputs to specific ideo-
logical goals without disclosure. Steering may also
introduce unintended side effects, such as shifting
refusal behavior, amplifying demographic or politi-
cal bias, or changing toxicity and stereotyping rates,
even when overall task accuracy appears stable. In
9

--- Page 10 ---

addition, our foundation vectors are built from cu-
rated vignette-style data and validated on English
natural text, which may reflect cultural and anno-
tator biases and may not transfer to other moral
systems or languages; results should not be treated
as normative claims about what is “correct” moral-
ity. We use publicly available text (e.g., Reddit)
and operate at the level of aggregate distributions
rather than attempting to identify individuals, but
we still aim to minimize privacy risk by avoiding re-
lease of raw user text beyond what is already public
and by reporting only summary statistics. Finally,
automated feature interpretation uses an LLM as
an annotator, which can introduce interpretation er-
rors; we treat these annotations as qualitative aids
rather than ground truth. To reduce misuse, we rec-
ommend that any released code for interventions
include clear documentation, default conservative
settings, and evaluation scripts that track side ef-
fects (bias, toxicity, and refusal changes) under
steering.
References
Marwa Abdulhai, Gregory Serapio-Garcia, Clément
Crepy, Daria Valter, John Canny, and Natasha Jaques.
2024. Moral foundations of large language models.
In Proceedings of the 2024 Conference on Empiri-
cal Methods in Natural Language Processing, pages
17737–17752.
Suhaib Abdurahman, Mohammad Atari, Farzan Karimi-
Malekabadi, Mona J Xue, Jackson Trager, Peter S
Park, Preni Golazizian, Ali Omrani, and Morteza De-
hghani. 2024. Perils and opportunities in using large
language models in psychological research. PNAS
Nexus, 3(7):pgae245.
Meltem Aksoy. 2025. Whose morality do they speak?
unraveling cultural bias in multilingual language
models.
Natural Language Processing Journal,
12:100172.
Emmanuel Ameisen, Jack Lindsey, Adam Pearce, Wes
Gurnee, Nicholas L Turner, Brian Chen, Craig Citro,
David Abrahams, Shan Carter, Basil Hosmer, and
1 others. 2025. Circuit tracing: Revealing compu-
tational graphs in language models. Transformer
Circuits Thread, 6.
Rie Kubota Ando and Tong Zhang. 2005. A framework
for learning predictive structures from multiple tasks
and unlabeled data. Journal of Machine Learning
Research, 6:1817–1853.
Galen Andrew and Jianfeng Gao. 2007. Scalable train-
ing of L1-regularized log-linear models. In Proceed-
ings of the 24th International Conference on Machine
Learning, pages 33–40.
Martin Arjovsky, Léon Bottou, Ishaan Gulrajani, and
David Lopez-Paz. 2019. Invariant risk minimization.
arXiv preprint arXiv:1907.02893.
Mohammad Atari and Morteza Dehghani. 2022. Lan-
guage analysis in moral psychology. The atlas of
language analysis in psychology, pages 207–228.
Mohammad Atari, Jonathan Haidt, Jesse Graham,
Sena Koleva, Sean T Stevens, and Morteza De-
hghani. 2023. Morality beyond the weird: How the
nomological network of morality varies across cul-
tures. Journal of Personality and Social Psychology,
125(5):1157.
Amin Banayeeanzade, Ala N. Tak, Fatemeh Bahrani,
Anahita Bolourani, Leonardo Blas, Emilio Ferrara,
Jonathan Gratch, and Sai Praneeth Karimireddy.
2025. Psychological steering in llms: An evalua-
tion of effectiveness and trustworthiness. Preprint,
arXiv:2510.04484.
Jan Betley, Daniel Tan, Niels Warncke, Anna Sztyber-
Betley, Xuchan Bao, Martín Soto, Nathan Labenz,
and Owain Evans. 2025. Emergent misalignment:
Narrow finetuning can produce broadly misaligned
llms. Preprint, arXiv:2502.17424.
Joseph Bloom, Curt Tigges, Anthony Duong, and David
Chanin. 2024.
Saelens.
https://github.com/
decoderesearch/SAELens.
Bart Bussmann, Patrick Leask, and Neel Nanda. 2024.
Batchtopk sparse autoencoders.
arXiv preprint
arXiv:2412.06410.
Nick Cammarata, Gabriel Goh, Shan Carter, Chelsea
Voss, Ludwig Schubert, and Chris Olah. 2021. Curve
circuits. Distill, 6(1):e00024–006.
Runjin Chen, Andy Arditi, Henry Sleight, Owain Evans,
and Jack Lindsey. 2025. Persona vectors: Monitoring
and controlling character traits in language models.
arXiv preprint arXiv:2507.21509.
Scott Clifford, Vijeth Iyengar, Roberto Cabeza, and
Walter Sinnott-Armstrong. 2015. Moral foundations
vignettes: A standardized stimulus database of sce-
narios based on moral foundations theory. Behavior
research methods, 47(4):1178–1198.
Hoagy Cunningham, Aidan Ewart, Logan Riggs, Robert
Huben, and Lee Sharkey. 2023. Sparse autoencoders
find highly interpretable features in language models.
arXiv preprint arXiv:2309.08600.
Dan Dillion, Dan Mondal, Niket Tandon, and Kurt
Gray. 2025. Ai language model rivals expert ethi-
cist in perceived moral expertise. Scientific Reports,
15(1):4084.
Nelson Elhage, Tristan Hume, Catherine Olsson,
Nicholas Schiefer, Tom Henighan, Shauna Kravec,
Zac Hatfield-Dodds, Robert Lasenby, Dawn Drain,
Carol Chen, and 1 others. 2022. Toy models of su-
perposition. arXiv preprint arXiv:2209.10652.
10

--- Page 11 ---

Nelson Elhage, Neel Nanda, Catherine Olsson, Tom
Henighan, Nicholas Joseph, Ben Mann, Amanda
Askell, Yuntao Bai, Anna Chen, Tom Conerly,
Nova DasSarma, Dawn Drain, Deep Ganguli,
Zac Hatfield-Dodds,
Danny Hernandez,
Andy
Jones, Jackson Kernion, Liane Lovitt, Kamal
Ndousse, and 6 others. 2021.
A mathemati-
cal framework for transformer circuits.
Trans-
former Circuits Thread.
Https://transformer-
circuits.pub/2021/framework/index.html.
Jeremy A Frimer, Reihane Boghrati, Jonathan Haidt,
Jesse Graham, and Morteza Dehgani. 2019. Moral
foundations dictionary for linguistic analyses 2.0.
Unpublished manuscript.
Leo Gao, Stella Biderman, Sid Black, Laurence Gold-
ing, Travis Hoppe, Charles Foster, Jason Phang,
Horace He, Anish Thite, Noa Nabeshima, Shawn
Presser, and Connor Leahy. 2020.
The pile: An
800gb dataset of diverse text for language modeling.
Preprint, arXiv:2101.00027.
Leander Girrbach, Stephan Alaniz, Genevieve Smith,
Trevor Darrell, and Zeynep Akata. 2025. Person-
centric annotations of laion-400m: Auditing bias
and its transfer to models.
arXiv preprint
arXiv:2510.03721.
Jesse Graham, Jonathan Haidt, Sena Koleva, Matt
Motyl, Ravi Iyer, Sean P Wojcik, and Peter H Ditto.
2013. Moral foundations theory: The pragmatic va-
lidity of moral pluralism. In Advances in experi-
mental social psychology, volume 47, pages 55–130.
Elsevier.
Jesse Graham, Brian A Nosek, Jonathan Haidt, Ravi
Iyer, Spassena Koleva, and Peter H Ditto. 2011. Map-
ping the moral domain. Journal of personality and
social psychology, 101(2):366.
Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri,
Abhinav Pandey, Abhishek Kadian, Ahmad Al-
Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten,
Alex Vaughan, and 1 others. 2024. The llama 3 herd
of models. arXiv preprint arXiv:2407.21783.
Kurt Gray, Chelsea Schein, and Adrian F Ward. 2014.
The myth of harmless wrongs in moral cognition:
Automatic dyadic completion from sin to suffer-
ing. Journal of Experimental Psychology: General,
143(4):1600.
Jonathan Haidt. 2007. The new synthesis in moral psy-
chology. science, 316(5827):998–1002.
Jonathan Haidt. 2012. The righteous mind: Why good
people are divided by politics and religion. Vintage.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2020. Measuring massive multitask language under-
standing. arXiv preprint arXiv:2009.03300.
Joseph Henrich, Steven J Heine, and Ara Norenzayan.
2010. The weirdest people in the world? Behavioral
and brain sciences, 33(2-3):61–83.
Joe Hoover, Mohammad Atari, Aida Mostafazadeh Da-
vani, Brendan Kennedy, Gwenyth Portillo-Wightman,
Leigh Yeh, and Morteza Dehghani. 2021. Investi-
gating the role of group-based morality in extreme
behavioral expressions of prejudice. Nature Commu-
nications, 12(1):4585.
Joe Hoover, Gwenyth Portillo-Wightman, Leigh Yeh,
Shreya Havaldar, Aida Mostafazadeh Davani, Ying
Lin, Brendan Kennedy, Mohammad Atari, Zahra
Kamel, Madelyn Mendlen, and 1 others. 2020. Moral
foundations twitter corpus: A collection of 35k
tweets annotated for moral sentiment. Social Psycho-
logical and Personality Science, 11(8):1057–1071.
Frederic R Hopp, Ori Amir, Jacob T Fisher, Scott
Grafton, Walter Sinnott-Armstrong, and René Weber.
2023. Moral foundations elicit shared and dissocia-
ble cortical activation modulated by political ideol-
ogy. Nature Human Behaviour, 7(12):2182–2198.
Jianchao Ji, Yutong Chen, Mingyu Jin, Wujiang Xu,
Wenyue Hua, and Yongfeng Zhang. 2025. Moral-
bench: Moral evaluation of llms. ACM SIGKDD
Explorations Newsletter, 27(1):62–71.
Behnam Karami, Fatemeh Zandi, and Javad Hatami.
2025. Emergent moral representations in large lan-
guage models aligns with human conceptual, neural,
and behavioral moral structure. Research Square
Preprint.
Adam Karvonen. 2024. An intuitive explanation of
sparse autoencoders for llm interpretability.
Brendan
Kennedy,
Mohammad
Atari,
Aida Mostafazadeh Davani,
Joe Hoover,
Ali
Omrani, Jesse Graham, and Morteza Dehghani.
2021. Moral concerns are differentially observable
in language. Cognition, 212:104696.
Ari Khoudary, Eleanor Hanna, Kevin O’Neill, Vi-
jeth Iyengar, Scott Clifford, Roberto Cabeza, Felipe
De Brigard, and Walter Sinnott-Armstrong. 2022. A
functional neuroimaging investigation of moral foun-
dations theory. Social Neuroscience, 17(6):491–507.
Been Kim, Martin Wattenberg, Justin Gilmer, Carrie
Cai, James Wexler, Fernanda Viegas, and 1 oth-
ers. 2018. Interpretability beyond feature attribu-
tion: Quantitative testing with concept activation vec-
tors (tcav). In International Conference on Machine
Learning, pages 2668–2677. PMLR.
Leon Li and Michael Tomasello. 2021. On the moral
functions of language. Social Cognition, 39(1):99–
116.
Samuel Marks, Adam Karvonen, and Aaron Mueller.
2024.
Dictionary learning.
GitHub repository.
https://github.com/saprmarks/dictionary_
learning.
Meta.
2024.
meta-llama/llama-3.1-8b-instruct.
https://huggingface.co/meta-llama/Llama-3.
1-8B-Instruct. Hugging Face model. Accessed:
2025-12-31.
11

--- Page 12 ---

Richard Ngo, Lawrence Chan, and Sören Mindermann.
2024. The alignment problem from a deep learning
perspective. In The Twelfth International Conference
on Learning Representations.
José Luiz Nunes, Guilherme F. C. F. Almeida, Marcelo
de Araujo, and Simone D. J. Barbosa. 2024.
Are large language models moral hypocrites?
a
study based on moral foundations. arXiv preprint
arXiv:2409.01955.
Dino Pedreschi, Fosca Giannotti, Riccardo Guidotti,
Anna Monreale, Salvatore Ruggieri, and Franco
Turini. 2019. Meaningful explanations of black box
ai decision systems. In Proceedings of the AAAI con-
ference on artificial intelligence, volume 33, pages
9780–9784.
Guilherme Penedo, Hynåek Kydlíˇcek, Loubna Ben al-
lal, Anton Lozhkov, Margaret Mitchell, Colin Raffel,
Leandro Von Werra, and Thomas Wolf. 2024. The
fineweb datasets: Decanting the web for the finest
text data at scale. Preprint, arXiv:2406.17557.
Ethan Perez, Sam Ringer, Kamile Lukosiute, Karina
Nguyen, Edwin Chen, Scott Heiner, Craig Pettit,
Catherine Olsson, Sandipan Kundu, Saurav Kada-
vath, and 1 others. 2023.
Discovering language
model behaviors with model-written evaluations. In
Findings of the association for computational linguis-
tics: ACL 2023, pages 13387–13434.
Mohammad Sadegh Rasooli and Joel R. Tetreault. 2015.
Yara parser: A fast and accurate dependency parser.
Computing Research Repository, arXiv:1503.06733.
Version 2.
Nils Karl Reimer, Mohammad Atari, Farzan Karimi-
Malekabadi, Jackson Trager, Brendan Kennedy, Jesse
Graham, and Morteza Dehghani. 2022. Moral values
predict county-level covid-19 vaccination rates in the
united states. American Psychologist, 77(6):743.
Chelsea Schein and Kurt Gray. 2018. The theory of
dyadic morality: Reinventing moral judgment by
redefining harm. Personality and Social Psychology
Review, 22(1):32–70.
Patrick Schramowski, Cigdem Turan, Nico Andersen,
Constantin A Rothkopf, and Kristian Kersting. 2022.
Large pre-trained language models contain human-
like biases of what is right and wrong to do. Nature
Machine Intelligence, 4(3):258–268.
Gunes Sevinc and R Nathan Spreng. 2014. Contex-
tual and perceptual brain processes underlying moral
cognition: a quantitative meta-analysis of moral rea-
soning and moral emotions. PloS one, 9(2):e87427.
Gabriel Simmons. 2022.
Moral mimicry:
Large
language models produce moral rationalizations
tailored to political identity.
arXiv preprint
arXiv:2209.12106.
Judith G Smetana. 2006. Social-cognitive domain the-
ory: Consistencies and variations in children’s moral
and social knowledge. In Handbook of Moral Devel-
opment, pages 119–153. Erlbaum, Mahwah, NJ.
Jackson Trager, Francielle Vargas, Diego Alves, and 1
others. 2025a. Mftcxplain: A multilingual bench-
mark dataset for evaluating the moral reasoning
of llms through multi-hop hate speech explanation.
arXiv preprint arXiv:2506.19073.
Jackson Trager, Alireza S. Ziabari, Elnaz Rahmati,
Aida Mostafazadeh Davani, Preni Golazizian, Farzan
Karimi-Malekabadi, Ali Omrani, Zhihe Li, Brendan
Kennedy, Nils Karl Reimer, Melissa Reyes, Kelsey
Cheng, Mellow Wei, Christina Merrifield, Arta Khos-
ravi, Evans Alvarez, and Morteza Dehghani. 2025b.
The moral foundations reddit corpus.
Preprint,
arXiv:2208.05545.
Elliot Turiel. 1983. The Development of Social Knowl-
edge: Morality and Convention. Cambridge Univer-
sity Press, Cambridge, UK.
Alexander Matt Turner, Lisa Thiergart, Gavin Leech,
David Udell, Juan J Vazquez, Ulisse Mini, and
Monte MacDiarmid. 2023. Steering language mod-
els with activation engineering.
arXiv preprint
arXiv:2308.10248.
Kevin Ro Wang, Alexandre Variengien, Arthur Conmy,
Buck Shlegeris, and Jacob Steinhardt. 2023. Inter-
pretability in the wild: a circuit for indirect object
identification in GPT-2 small. In The Eleventh Inter-
national Conference on Learning Representations.
James Wilkinson, Oliver Scott Curry, Brittany L
Mitchell, and Timothy Bates. 2024. Modular morals:
Mapping the organization of the moral brain. Brain
and Cognition, 180:106201.
An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui,
Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu,
Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jian-
hong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang,
Jingren Zhou, Junyang Lin, Kai Dang, and 22 oth-
ers. 2024. Qwen2.5 technical report. arXiv preprint
arXiv:2412.15115.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Tianle
Li, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang,
Zhuohan Li, Zi Lin, Eric. P Xing, Joseph E. Gonza-
lez, Ion Stoica, and Hao Zhang. 2023. Lmsys-chat-
1m: A large-scale real-world llm conversation dataset.
Preprint, arXiv:2309.11998.
Andy Zou, Long Phan, Sarah Chen, James Campbell,
Phillip Guo, Richard Ren, Alexander Pan, Xuwang
Yin, Mantas Mazeika, Ann-Kathrin Dombrowski,
and 1 others. 2023. Representation engineering: A
top-down approach to ai transparency. arXiv preprint
arXiv:2310.01405.
12

--- Page 13 ---

A
Appendix
A.1
Detailed Experimental Setup
A.1.1
Models and Architectures
Subject
models.
We
use
Llama-3.1-8B-
Instruct (meta-llama/Llama-3.1-8B-Instruct,
Grattafiori et al., 2024; Meta, 2024) and Qwen2.5-
7B-Instruct (Qwen/Qwen2.5-7B-Instruct, Yang
et al., 2024) as subject LLMs. All inference is run
with HuggingFace Transformers in BF16/FP16 (de-
pending on hardware support), using temperature
T = 0.01 for all experiments.
Sparse Autoencoders.
We perform mechanistic
decomposition using the suite of pretrained SAEs
provided by the SAELens library (Marks et al.,
2024). To ensure the learned features cover the
relevant behavioral distribution, SAEs were trained
on a diverse set of standard pretraining corpora
and chat-based instruction data (Zheng et al., 2023;
Gao et al., 2020; Betley et al., 2025).
We se-
lect SAEs trained on the residual stream of the
Llama and Qwen model using the BatchTopK ac-
tivation function (Bussmann et al., 2024; Bloom
et al., 2024). To analyze the evolution of moral fea-
tures across depth while optimizing computational
costs, we evaluate SAEs trained on every fourth
layer (L ∈{3, 7, . . . , 27}). For Llama SAEs, these
instances feature an expansion factor of 32 (project-
ing the dmodel = 4096 dimension to ∼131k latent
features). For Qwen SAEs, these instances feature
an expansion factor of 36.57 (projecting project-
ing the dmodel = 3584 dimension to ∼131k latent
features). Both SAE categories have a sparsity of
k = 64 active features per token.
A.1.2
Dataset
Extended Moral Foundations Vignettes.
We
construct concept vectors using an expanded ver-
sion of the Moral Foundations Vignettes (MFV-130;
Clifford et al., 2015). Starting from the original vi-
gnettes for the five moral foundations and a Social
Norm category, we expand each category to ap-
proximately 200 short scenarios using gpt-5-mini,
matching the conceptual definition and linguistic
style of the original MFV items, using prompts that
vary everyday social contexts and non-essential
contextual features which past work has shown to
reduce spurious correlations and stabilize learned
representations (Arjovsky et al., 2019; Kim et al.,
2018). All generated vignettes are reviewed by
human experts to verify clarity, label correctness,
and adherence to the intended foundation or social-
norm category. Sample prompts and generated
items are provided in Appendix B.4.
Moral Foundations Reddit Corpus.
To validate
our vectors on real-world moral language, we use
human-labeled Reddit posts from the Reddit Moral
Foundations Corpus (Trager et al., 2025b). From
the full corpus (61.2K posts), we keep only single-
label posts with high-confidence annotations to ob-
tain an unambiguous ground-truth set. These posts
are never used for vector construction; we feed only
the raw text to the model and use labels solely for
grouping in projection analyses.
Semantic resource for SAE validation.
We use
the Moral Foundations Dictionary 2.0 (MFD2)
(Frimer et al., 2019) as an external semantic an-
chor for validating SAE feature fingerprints (Sec-
tion 3.3). For each foundation, we extract the cor-
responding keyword lists and test whether the se-
lected SAE feature directions are geometrically
close to embeddings of the foundation-specific
MFD terms.
Behavioral evaluation resource (MFQ-2) for
steering.
To measure causal effects of steering
on expressed moral preferences, we use the Moral
Foundations Questionnaire–2 (MFQ-2) as a down-
stream evaluation task (Atari et al., 2023). MFQ-2
items are mapped to foundation subscales and rated
on a five-point Likert scale. Following prior prac-
tice, we operationalize Fairness by averaging items
from Equality and Proportionality, and report five
foundation scores: Care, Fairness, Loyalty, Author-
ity, and Purity.
A.1.3
Evaluation Metrics
Signed Wasserstein Distance for Topological Va-
lidity.
To assess whether our concept vectors
align with human-labeled moral categories (Sec-
tion 3.2), we compare the projection-score distri-
butions of Reddit posts labeled with foundation k
versus those not labeled with k. For each layer ℓ,
let Pk,ℓand P¬k,ℓdenote the corresponding score
distributions, and let µk,ℓand µ¬k,ℓbe their means.
We report the Signed Wasserstein Distance to cap-
ture both the magnitude and the direction of sepa-
ration:
SW1(Pk,ℓ, P¬k,ℓ) = sign(µk,ℓ−µ¬k,ℓ)
· SW1(Pk,ℓ, P¬k,ℓ).
(9)
13

--- Page 14 ---

where the standard (unsigned) 1-Wasserstein dis-
tance is defined as
W1(Pk,ℓ, P¬k,ℓ) =
inf
γ∈Π(Pk,ℓ,P¬k,ℓ) E(x,y)∼γ

|x−y|

,
(10)
with Π(Pk,ℓ, P¬k,ℓ) denoting the set of joint distri-
butions with marginals Pk,ℓand P¬k,ℓ. A positive
Signed-SW1 indicates that the labeled examples
possess larger mean projection scores along the
foundation vector (alignment), whereas negative
values indicate separation in the opposite direction
(anti-alignment). We employ SW1 because it (i)
remains well-defined even for distributions with
disjoint support, (ii) faithfully reflects geometric
separation along the projection axis, and (iii) is
robust to class imbalance.
Moral steering efficacy.
We quantify causal
steering effects by the change in the target founda-
tion score on MFQ-2, treating each item as a five-
option rating question and scoring it via the model’s
option probabilities from output logits. We aggre-
gate item scores into foundation-level subscales,
yielding a score Sk for each moral dimension k.:
∆Starget = E[Sk | steer] −E[Sk | baseline], (11)
where k is the steered foundation. Larger |∆Starget|
indicates stronger causal control over the targeted
moral preference.
Logits-based MFQ-2 scoring.
For each MFQ-
2 item with options T = {1, 2, 3, 4, 5}, we ob-
tain the option logits {zt}t∈T and compute p(t) =
softmax(z)t. The item score is the expected rating
Sitem = P
t∈T t p(t). We then average item scores
within each MFQ-2 subscale to obtain foundation
scores Sk.
B
Implementation Details and
Cross-Model Generalization
In this section, we provide detailed implementation
details for our analyses and interventions, and re-
port robustness results for the Qwen2.5-7B-Instruct
model to assess cross-model generalization.
B.1
Implementation Details: Projection
For both Llama-3.1 and Qwen2.5, we construct
two types of directions in residual-stream space: (i)
foundation vs. Social Norm vectors and (ii) foun-
dation vs. foundation vectors (Section 3.1), and
evaluate them on held-out human-labeled Reddit
posts together with a non-moral baseline corpus (la-
bels held out at inference and used only for group-
ing). The main text reports the Llama foundation vs.
Social Norm results; here we provide the remain-
ing projection analyses, including cross-foundation
geometry (foundation vs. foundation) and the cor-
responding results for Qwen2.5.
Qwen2.5: foundation vs. Social Norm projec-
tions.
Figure 5a shows that Qwen2.5-7B-Instruct
yields strong, consistently positive separation be-
tween moral and non-moral Reddit posts when pro-
jecting onto the foundation vs. Social Norm vectors.
At the optimal layer (Layer 27 for all foundations),
all five foundations exhibit clear distributional gaps
from the non-moral baseline, with large Wasser-
stein distances: Care (SW1 = 6.39), Authority
(SW1 = 6.32), Loyalty (SW1 = 5.18), Fairness
(SW1 = 4.81), and Sanctity (SW1 = 4.56). Fig-
ure 5b further shows a pronounced “terminal peak”:
separability remains modest in earlier layers but
rises sharply in the final layers, indicating that foun-
dation signals become most readable near the end
of the network. Notably, unlike Llama, Fairness
also shows a robust terminal peak without sign in-
version, suggesting a cleaner disentanglement from
the learned Social Norm baseline in Qwen.
Between Foundations projections (Both Mod-
els).
Tables 1 and 2 report pairwise Wasserstein-
1 distances (SW1) computed from foundation vs.
foundation projections for Llama and Qwen. Be-
cause the two model families can differ in activa-
tion scale, we do not compare absolute SW1 values
across models; instead, we focus on their relative
geometric structure (which foundations are close
vs. far).
Recent work in moral psychology suggests that
the classic MFQ clustering into Individualizing
(Care, Fairness) and Binding (Loyalty, Authority,
Sanctity) is not stable across cultures and may re-
flect WEIRD-specific measurement structure. Net-
work analyses of Moral Foundations Questionnaire
data indicate that inter-foundation relationships
vary substantially across societies: moral founda-
tions often form interconnected networks rather
than two consistently segregated clusters, and no
single higher-order relational pattern generalizes
across cultural contexts (Atari et al., 2023). These
findings motivate treating inter-foundation geom-
etry as a variable property rather than a universal
template.
Viewed through this lens, our model geometries
14

--- Page 15 ---

+0. 280σ
+0. 210σ
+0.146σ
+0.148σ
+0.160σ
Layer 27
Layer 27
Layer 27
Layer 27
Layer 27
(a) Topological Separation at the Decision Boundary (Qwen).
Standardized probability densities of moral projections (col-
ored) vs. the non-moral baseline (gray). The x-axis represents
semantic shift in standard deviations (σ).
0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
Layer Index
0
1
2
3
4
5
6
Signed Wasserstein-1 Distance (SW1)
Care
Fairness
Loyalty
Authority
Sanctity
(b) Layer-wise Evolution of Separability (Qwen). Signed
Wasserstein-1 distances (SW1) across all 28 layers, where
green indicates positive separability and red indicates negative
(reversed) separability.
Figure 5: The geometry of moral alignment in Qwen-
2.5-7B-Instruct. We project human-labeled Reddit
posts for each moral foundation, and non-moral data,
onto the corresponding foundation-vs.-Social Norm vec-
tors.
suggest three takeaways. First, in both models,
Care and Sanctity emerge as relatively distinct di-
rections in representation space. This finding is
consistent with human cross-cultural studies, which
show that harm-related and purity-related concerns
remain distinct components of moral cognition
across societies, even as their correlations with
other foundations vary across populations (Atari
et al., 2023). Second, Qwen-2.5 exhibits a geom-
etry in which Fairness is not consistently closest
to Care, and can instead appear nearer to Author-
ity and Loyalty. Comparable patterns are observed
in some non-WEIRD human samples, where the
relational position of fairness varies across popula-
tions and is not uniformly aligned with care-based
concerns (Atari et al., 2023). We emphasize that
this comparison reflects similarity in relational vari-
ability rather than a direct mapping between model
training data and specific human cultures.
Third, Llama exhibits a qualitatively different
pattern: Fairness, Loyalty, and Authority collapse
into an extremely tight cluster (near-zero pairwise
distances). The magnitude and sharpness of this
collapse is difficult to explain by cross-cultural
variation alone and instead points to an alignment-
driven compression: RLHF objectives may co-train
“fairness” (bias avoidance), “authority” (instruction
following), and “loyalty” (helpfulness) as a single
compliance-like behavior. In summary, Qwen-2.5
preserves a more graded middle structure with dis-
tinct anchors, whereas Llama shows evidence that
strong safety alignment can merge multiple values
into a dominant compliance cluster.
Care
Fairness Loyalty Authority Sanctity
Care
0.000
0.564
1.661
1.309
1.182
Fairness
0.564
0.000
0.101
0.041
2.204
Loyalty
1.661
0.101
0.000
0.007
2.524
Authority 1.309
0.041
0.007
0.000
2.175
Sanctity
1.182
2.204
2.524
2.175
0.000
Table 1: Pairwise Wasserstein-1 distances (SW1) be-
tween moral foundations computed at the optimal
separation layer (LLAMA).
Care
Fairness Loyalty Authority Sanctity
Care
0.000
7.019
10.414
9.469
8.808
Fairness
7.019
0.000
2.045
1.540
16.836
Loyalty
10.414
2.045
0.000
3.777
17.796
Authority
9.469
1.540
3.777
0.000
17.927
Sanctity
8.808
16.836
17.796
17.927
0.000
Table 2: Pairwise Wasserstein-1 distances (SW1) be-
tween moral foundations computed at the optimal
separation layer (Qwen).
These results should not be read as a direct test
of MFT as a model of human moral cognition. The
observed alignment-induced collapse among Fair-
ness, Authority, and Loyalty is best interpreted as a
consequence of optimization pressures that jointly
reward compliance-oriented behaviors, rather than
as evidence for or against the underlying theory. At
the same time, the persistence of a distinct Care
axis suggests that some moral distinctions remain
separable at the level of language alone. This dis-
tinction clarifies the scope of inference from our
analysis: the results characterize how moral do-
mains are reorganized under alignment, not how
they originate in humans.
B.2
Implementation Details: SAEs
To identify the specific mechanisms underlying
moral representation, we followed the methodol-
ogy in Chen et al. 2025 and computed the cosine
similarity between the decoder directions of the
15

--- Page 16 ---

3
7
11
15
19
23
27
Layer Index
0.10
0.15
0.20
0.25
Avg Cosine Similarity
Average Alignment of Top-3 Features Across Layers
authority
care
fairness
loyalty
sanctity
Random Baseline
Figure 6: Layer-wise Alignment of Moral Features
(Qwen). Average cosine similarity of the top-3 most
aligned SAE features for each Moral Foundation across
every 4 layers vs random baselines. Similarity is calcu-
lated between the SAE decoder weights and the corre-
sponding Foundation vs. Social Norms concept vector.
SAEs and the foundation-specific concept vectors
derived from the residual stream (Section 3.3).
Based on this metric, we selected the top-10 fea-
tures with the highest similarity for each moral
foundation on every layer to serve as the primary
targets for analysis and intervention. To validate
the semantics of these features, we randomly sam-
pled 50,000 documents from the FineWeb dataset
(Penedo et al., 2024) and retrieved the top-40 ac-
tivating texts for each candidate feature. We ex-
tracted deduplicated evidence snippets centered
around the tokens (token window size ± 64) with
maximum activation and prompted GPT-5.1 to gen-
erate structured semantic interpretations (Section
B.2.2), ensuring the features meaningfully encoded
concepts related to the target moral foundations.
B.2.1
Extended Analysis for The Anatomy of
Morality
In this section, we provide a detailed analysis of
the layer-wise evolution of moral features and their
semantic grounding.
Layer-wise Alignment Dynamics
To quantify
feature-level representation, we computed the co-
sine similarity between MFT concept vectors and
SAE decoder features. We also report a per-layer
random baseline, which captures the expected
alignment between SAE features and an arbitrary
direction in activation space.
According to Figure 3, observed alignments in
Llama substantially exceed the random baseline
across all layers, indicating that the identified fea-
tures encode non-random, semantically meaningful
structure. Alignment is relatively weak in early
layers (4–12), consistent with these layers empha-
sizing syntactic or local contextual processing. A
peak emerges at Layer 16 for all five foundations,
where alignment is maximized and most strongly
separated from the baseline. This pattern suggests
that mid-level layers act as a semantic bottleneck
in Llama, where moral concepts are most distinctly
encoded at the feature level. Notably, Care and
Sanctity exhibit consistently higher alignment than
other foundations, particularly Loyalty and Author-
ity. This disparity suggests that moral foundations
are represented with varying degrees of clarity at
the feature level, with some concepts aligning more
cleanly with individual SAE features than others,
potentially reflecting differences in representational
fidelity or disentanglement.
In contrast, Qwen exhibits a distinct "U-shaped"
trajectory (Figure 6). Alignment starts high in the
early layers (Layer 3), particularly for Authority
and Care, suggesting an early capture of surface-
level moral semantics. This is followed by a sig-
nificant dip in the middle layers (7–15). Finally,
alignment resurges sharply in the deep layers, peak-
ing at Layer 23, with Fairness achieving the high-
est separation. This divergence—Llama peaking
in the middle versus Qwen peaking at the bound-
aries—suggests that different architectures may se-
quence the "crystallization" of moral concepts dif-
ferently, with Qwen potentially disentangling these
concepts during both initial processing and final
readout preparation.
Semantic Grounding of SAE Features
We qual-
itatively grounded these sparse features by analyz-
ing their top-activating contexts and mapping them
to MF categories using an LLM-assisted procedure
with human validation (see Tables 5 and 6).
We find that SAE features decompose abstract
foundations into granular, interpretable mecha-
nisms. For example, in Table 5, Care features
in Llama separate into distinct clusters tracking
“descriptions of physical suffering” (e.g., Feature
L23.44965) and “emotional distress” (e.g., Feature
L19.90260). Similarly, Authority decomposes into
features tracking "government regulatory frame-
works" and "hierarchical role definitions".
In Qwen (Table 6), we observe a similar semantic
granularity that mirrors the model’s unique layer-
wise trajectory. Authority features appear as early
as Layer 3 (e.g., Feature L3.72227, tracking “men-
tions of government and national leaders”), provid-
ing a mechanistic explanation for the high geomet-
16

--- Page 17 ---

ric alignment observed in the model’s initial layers.
For Care, the model distinguishes between active
condemnation of harm, such as “bullying and co-
ercion” (Feature L15.130669), and abstract proso-
cial definitions, such as “empathy and compassion”
(Feature L27.85517). We also identify distinct Fair-
ness features related to “corporate responsibility
and business ethics” (Feature L3.123373), a spe-
cific domain of justice that appears less prominent
in the Llama analysis.
Across both models, Care and Authority are the
foundations most frequently associated with high-
confidence semantic features. This indicates that
while the model possesses sparse mechanisms for
all foundations, the concepts of empathy and social
regulation are the most robustly "crystallized" into
detectable inner units.
B.2.2
Semantic Validation Implementation
Details
To interpret the semantics of SAE features, we
employed GPT-5.1 (GPT) as an automated annota-
tor. The model was tasked with analyzing a set of
top-activating text snippets for a given feature and
generating a structured summary. We prioritized a
“conservative” annotation strategy: the model was
explicitly instructed to first identify neutral seman-
tic patterns and only assign a Moral Foundations
Theory (MFT) label if the evidence was strong.
Prompt construction.
The prompt consists of
three components: (1) MFT definitions, (2) feature
metadata and evidence snippets, and (3) a strict
output schema.
System instructions.
The model was invoked
with temperature T = 0. The prompt provided
the standard definitions for the five moral foun-
dations (Haidt, 2012) and specific instructions to
avoid forcing moral interpretations on non-moral
features. The exact text provided to the model is
detailed in Figure 7.
Output schema.
We constrained the model to
output a valid JSON object matching the schema
in Table 4. This structured output facilitates down-
stream quantitative analysis of the feature direc-
tions.
LLM-grounded semantic characterization.
Ta-
bles 5 and 6 report SAE features whose top-
activating FineWeb (Penedo et al., 2024) con-
texts support a coherent semantic interpretation,
with an optional MFT assignment. Due to page
Semantic Interpretation Prompt
Role: You are interpreting a sparse autoencoder
(SAE) feature from an LLM.
Goal: Infer the most likely semantic pattern that
triggers the feature, based ONLY on the evidence
snippets.
Instructions:
1. Neutral Description First: Describe the dom-
inant pattern (topic, style, rhetorical function,
or social behavior) neutrally.
2. Conservative MFT Mapping:
Map to a
Moral Foundations Theory category only
if strongly supported.
Otherwise, output
mft_alignment="none". Do not force moral-
ity; many features are not moral.
3. Format: Provide a short label (5–10 words)
and a 1–2 sentence description.
4. Citations:
Cite evidence_ids (indices of
snippets) that justify your decision.
Moral Foundations Theory (MFT) definitions:
• Care/harm: dislike others’ suffering; kind-
ness, gentleness, nurturance vs cruelty, vio-
lence.
• Fairness/cheating: justice, rights, autonomy
vs fraud, exploitation, cheating.
• Loyalty/betrayal: group allegiance, patrio-
tism, self-sacrifice vs betrayal, treason, disloy-
alty.
• Authority/subversion: respect for legitimate
authority, leadership/followership, traditions vs
defiance, disrespect, subversion.
• Sanctity/degradation: purity, elevation above
the carnal, disgust sensitivity vs degradation,
contamination, depravity.
[Insert Feature Metadata JSON]
[Insert Evidence Snippets (index: text)]
Figure 7: Prompt template used for automated interpre-
tation of SAE features. Features are selected to have the
10 highest cosine similarity with a corresponding moral
foundation concept vectors at the same layer.
limits, we trimmed GPT outputs (long descrip-
tions, rationales, MFT polarity, and evidence
IDs). We find that GPT most confidently identi-
fies features associated with Care/harm, Author-
ity/subversion, and Fairness/cheating, and also
identifies a smaller number of Sanctity/degradation
features.
In contrast, we do not obtain high-
confidence Loyalty/Betrayal assignments in the
current semantic-mining pass. We attribute this to
the limited size of the validation sample (50,000
documents) and the resulting sparsity of diagnos-
tically relevant top-activation contexts under a
17

--- Page 18 ---

fixed compute budget, rather than to an absence
of Loyalty-related signal in the model. Importantly,
these LLM-grounded summaries are used to quali-
tatively ground feature semantics and present rep-
resentative exemplars; they complement (and do
not replace) our causal steering evaluations in Sec-
tion 5.3, which indicate that the identified SAE
features contain foundation-relevant moral signals.
B.3
Implementation Details: Steering
Steering conditions.
We evaluate two steering
granularities by varying the choice of ⃗vsteer. In
macro-steering, we steer along the (debiased)
foundation vector ⃗vk from Section 3.1 to test
whether the global moral direction is sufficient
to induce targeted behavioral change. In micro-
steering, we steer along a single SAE feature di-
rection di from Section 3.3 to test whether specific
sparse mechanisms can produce comparable effects
with finer control.
Intervention site and layers.
Let Lsteer denote
a small set of upper layers chosen based on strong
foundation separability in projection analyses on
a held-out development set (Section 3.2). During
autoregressive decoding, at each generated token
t and each layer ℓ∈Lsteer, we intervene on the
residual stream as
h′
ℓ,t =





hℓ,t + α vsteer
ℓ
(positive steering)
hℓ,t −α vsteer
ℓ
(negative steering)
hℓ,t
(no steering),
(12)
where α is the steering coefficient and vsteer
ℓ
is the
steering direction. For macro-steering, we set
vsteer
ℓ
= vmf
ℓ, the layer-wise moral-foundation vec-
tor from Section 3.1. For micro-steering, we set
vsteer
ℓ
= di, the decoder direction of a selected SAE
feature from Section 3.3.
Steering coefficient sweep and baseline.
We
sweep the steering coefficient α over a fixed grid.
For Llama-3.1, we use
α ∈{−2.0, −1.5, −1.0, −0.5, 0, 0.5, 1.0, 1.5, 2.0}.
For Qwen2.5, we use a scaled grid to match its
larger activation magnitude:
α ∈{−100, −75, −50, −25, 0, 25, 50, 75, 100}.
In both cases, the α = 0 baseline is defined as the
model’s measured score under the same evaluation
setup without any steering intervention.
Behavioral assessment and controls.
We mea-
sure behavioral effects using MFQ-2 (see A.1.2),
treating each item as a five-option rating question
and scoring it via the model’s option probabilities
from output logits. We aggregate item scores into
foundation-level subscales, yielding a score Sk for
each moral dimension k (See A.1.3).
B.3.1
Steering Representations
Notation.
Let f index a moral foundation and
l ∈{0, . . . , L −1} index a transformer layer. For
each steering coefficient α in a fixed grid, we run
the MFQ-2 evaluation under steering at layer l and
obtain a scalar foundation score Scoref,l(α) (Sec-
tion A.1.3).
Linear response regression.
For each pair (f, l),
we fit a linear response model across the tested α
values:
Scoref,l(α) = βf,l · α + cf,l.
(13)
The slope βf,l is computed via standard least-
squares linear regression (implemented with
scipy.stats.linregress), and can be written as
βf,l = Cov(α, Scoref,l)
Var(α)
.
(14)
Best-layer selection.
We select the best layer for
each foundation by maximizing the signed slope
(not the absolute value):
L∗= arg max
l
βf,l.
(15)
This choice prioritizes layers where steering in-
creases the target foundation score in the intended
direction; layers with large negative slopes are not
selected even if |βf,l| is large.
Delta score used
To compare response curves
across foundations with different baselines, we plot
baseline-subtracted scores:
∆Scoref,l(α) = Scoref,l(α) −Scoref,l(0). (16)
We define the α = 0 baseline as the model’s mea-
sured score under the same evaluation setup with-
out any steering intervention.
Plotting convention.
In Figures 4, 9, 10, 11, 12,
and 8, points show the measured ∆Scoref,L∗(α)
at the selected layer L∗, and the solid line shows
the corresponding linear trend anchored at the ori-
gin, ∆Scoref,L∗(α) = βf,L∗· α. For visualization
18

--- Page 19 ---

only, when plotting Qwen results we rescale the α
axis to the same [−2, 2] range used for Llama, so
that curve shapes are directly comparable across
models.
Steering Robustness Check on Qwen2.5
Fig-
ures 8(a,b) report steering results for Qwen2.5-7B-
Instruct under the same evaluation protocol as in
the main text. Relative to Llama, Qwen exhibits
three stable patterns consistent with our geometric
analysis.
Macro-steering is effective across all founda-
tions in Qwen. Unlike Llama—where macro vectors
are attenuated for compliance-related foundations—
Qwen shows positive response slopes for every foun-
dation, and macro-steering is typically stronger
than micro-steering (e.g., Care: kmacro = 0.864 vs.
kmicro = 0.439). This aligns with the projection re-
sults: when foundation vs. Social Norm directions
are cleanly separable, global vectors provide an
efficient control mechanism, whereas SAE-based
interventions modulate only a subset of the under-
lying circuit.
Authority remains the most difficult foundation
to control in Qwen. Despite high overall steerabil-
ity, Authority has the smallest slope under both
macro- and micro-steering (macro: k = 0.522; mi-
cro: k = 0.144), matching the relative ordering
observed in Llama. This suggests a model-family
invariant difficulty ranking, even when the absolute
geometry differs.
An efficacy–linearity trade-off is also appar-
ent. Compared to Llama’s near-linear response
curves, Qwen’s responses are less linear (lower R2
across foundations), consistent with higher-gain but
less stable control at larger intervention strengths
(e.g., mild saturation or non-linearities near the
extremes).
Layer-wise steering sensitivity.
To locate where
steering most strongly affects behavior, we esti-
mate a signed slope βf,l at each layer l by regress-
ing the MFQ-2 foundation score on the steering
coefficient α. Figures 9 and 11 plot these macro-
steering slopes across layers for Llama and Qwen,
where βf,l > 0 means larger α increases the target
foundation score and βf,l < 0 indicates a reversed
effect. For each foundation, we select the best layer
as the signed maximum, L∗= arg maxl βf,l, and
report macro-steering response curves at L∗in Fig-
ure 4a and 8a.
We apply the same layer-wise analysis for
micro-steering based on SAE feature directions.
2.0
1.5
1.0
0.5
0.0
0.5
1.0
1.5
2.0
Normalized Steering Strength ( , original ÷50)
4
3
2
1
0
1
2
3
4
 Score (relative to 
= 0)
Foundation        k     R²  Sig
Sanctity     +0.913  0.983  ***
Care         +0.864  0.748   **
Fairness     +0.840  0.912  ***
Loyalty      +0.813  0.916  ***
Authority    +0.522  0.669   **
QWEN -  normalized (÷50)
Care (L21)
Fairness (L21)
Loyalty (L21)
Authority (L21)
Sanctity (L21)
MMLU Accuracy
0
20
40
60
80
100
Average MMLU Accuracy (%)
(a) Macro (vector) steering response curves (Qwen). Steer-
ing along foundation-level concept vectors.
2.0
1.5
1.0
0.5
0.0
0.5
1.0
1.5
2.0
Normalized Steering Strength (  / 50)
1.5
1.0
0.5
0.0
0.5
1.0
1.5
 Score (relative to 
= 0)
Foundation        k     R²  Sig
Sanctity     +0.661  0.948  ***
Fairness     +0.443  0.880  ***
Care         +0.439  0.880  ***
Loyalty      +0.321  0.889  ***
Authority    +0.144  0.683   **
QWEN -  normalized (÷50)
Authority (L11)
Care (L19)
Fairness (L19)
Loyalty (L19)
Sanctity (L19)
MMLU Accuracy
0
20
40
60
80
100
Average MMLU Accuracy (%)
(b) Micro (SAE) steering result (Qwen). Steering at Top-10
SAE feature across layers.
Figure 8: Steering result (combined). For each foun-
dation, we plot the MFQ-2 score change ∆Score(α)
relative to the unsteered baseline (α = 0) as a function
of steering strength α, evaluated at that foundation’s
best layer. The best layer is chosen as the layer with
the largest positive linear response slope. Points show
measured ∆scores and the solid line shows the cor-
responding linear trend. The gray dashed line reports
general performance under the same interventions.
Figures 10 and 12 report the micro-steering
slopes across layers for Llama and Qwen, identi-
fying depths where sparse mechanisms exert the
strongest causal influence. Behavioral effects at
the selected layers are summarized in Figures 4b
and 8b, enabling a direct comparison between
macro-level vector steering and micro-level feature
steering.
B.3.2
General Performance Measurement
after Steering
To quantify whether moral steering affects the
model’s general capability, we evaluate the steered
model on the MMLU benchmark (Hendrycks et al.,
2020), which covers 57 subjects spanning STEM,
humanities, and social sciences.
19

--- Page 20 ---

0
5
10
15
20
25
30
Layer Index
0.10
0.05
0.00
0.05
0.10
0.15
0.20
0.25
Slope kf, l (with sign)
L15
L15
L11
L18
L18
Care
Fairness
Loyalty
Authority
Sanctity
Figure 9: Slope Magnitude Across Layers (Macro)
(LLAMA). Absolute steering slopes |kf,l| (|βf,l|) across
layers for each foundation, highlighting where steering
has the strongest sensitivity regardless of direction.
0
5
10
15
20
25
30
Layer Index
0.1
0.0
0.1
0.2
0.3
0.4
Slope kf, l (with sign)
L15
L15
L15
L15
L19
Authority
Care
Fairness
Loyalty
Sanctity
Figure 10: Slope Magnitude Across Layers (Micro)
(LLAMA). Absolute steering slopes |kf,l| (|βf,l|) across
layers for each foundation, highlighting where steering
has the strongest sensitivity regardless of direction.
Evaluation set.
We randomly sample n = 2000
questions from the MMLU test set using a fixed
random seed (seed=42) to ensure that the same
question set is used across all steering conditions.
We report both overall accuracy and subject-wise
accuracy aggregated over MMLU domains.
Steering configuration.
We evaluate the model
under the same inference-time intervention used
in our main steering experiments. For a controlled
comparison, we run both macro-steering (concept
vectors) and micro-steering (SAE feature direc-
tions) under identical settings: we intervene on
a single target layer and sweep steering strength
over nine values α
∈
{−2.0, −1.5, . . . , 2.0}.
For macro-steering, the steering direction is the
residual-stream normalized foundation concept
vector. For micro-steering, we intervene on the
selected SAE feature directions at the same layer
with the same α sweep.
0
5
10
15
20
25
Layer Index
0.2
0.0
0.2
0.4
0.6
0.8
Slope kf, l (normalized )
L21
QWEN -  normalized (÷50)
Care
Fairness
Loyalty
Authority
Sanctity
Figure 11: Slope Magnitude Across Layers (Macro)
(Qwen). Absolute steering slopes |kf,l| (|βf,l|)across
layers for each foundation, highlighting where steering
has the strongest sensitivity regardless of direction.
5
10
15
20
25
Layer Index (0-based)
0.4
0.2
0.0
0.2
0.4
0.6
Slope kf, l (Normalized )
L11
L19
QWEN -  normalized (÷50)
Authority
Care
Fairness
Loyalty
Sanctity
Figure 12: Slope Magnitude Across Layers (Micro)
(Qwen). Absolute steering slopes |kf,l| (|βf,l|) across
layers for each foundation, highlighting where steering
has the strongest sensitivity regardless of direction.
Logit-based multiple-choice scoring.
To obtain
deterministic and reproducible measurements, we
score MMLU in a logit-based manner rather than
via free-form generation. For each question, we
perform a single forward pass and extract the logits
of the option tokens (A, B, C, D) at the final posi-
tion. We then compute a softmax over these four
logits to obtain option probabilities,
P(optioni) =
exp(logiti)
P
j∈{A,B,C,D} exp(logitj), (17)
and predict the answer by
ˆy = arg
max
i∈{A,B,C,D} P(optioni).
(18)
Accuracy at each steering condition α is computed
as the fraction of correct predictions over the n =
2000 questions.
Observed general-performance trend (MMLU).
Macro-steering has minimal impact on general
20

--- Page 21 ---

capability in both models. In Llama, across α ∈
{−2.0, −1.5, . . . , 2.0}, MMLU accuracy remains
in a narrow band of roughly 63.7%–65.3% (base-
line at α = 0: 65.2%), with at most a ∼1.5-point
drop at the largest-magnitude intervention. In Qwen,
accuracy stays between 65.3% and 70.7% (base-
line at α = 0: 70.3%), with the largest deviation
at α = −100 (+4.2 points) and a 2.1-point drop at
α = +100. The corresponding curves are shown
in Figures 4 and 8.
For micro-steering, Llama’s MMLU accuracy
remains in a narrow band of roughly 61.0%–
65.3% (baseline at α = 0: 65.3%) across α ∈
{−2.0, −1.5, . . . , 2.0}, with at most a ∼4.3-point
drop at the largest-magnitude intervention. In Qwen,
accuracy stays between 65.4% and 70.3% (base-
line at α = 0: 70.3%), with the largest deviation
at α = 0 (+0.0 points) and a 4.9-point drop at
α = −100. The corresponding curves are shown
in Figures 4 and 8.
B.4
MFV-130 Expansion Prompt
To expand the Moral Foundations Vignettes (MFV-
130), for each foundation and the Social Norm cat-
egory, we construct a foundation-specific prompt
that defines the target construct, explicitly excludes
confounding dimensions, and enforces stylistic con-
sistency with the original MFV items. Generation
is organized around a prompt-level diversity grid
that enumerates multiple everyday social contexts
(e.g., public spaces, online interactions, peer-based
workplaces) while holding the underlying moral
content fixed. Items are generated in structured
JSON format with explicit count and schema con-
straints to guarantee balanced coverage across con-
texts, and all generated items are reviewed by hu-
man experts for clarity and label fidelity. An ex-
ample generation prompt is shown in Figure 13.
Table 3 shows representative original and gener-
ated vignettes.
MFV-130
Expansion
Prompt
(Care–
Emotional Harm)
Role: You are generating new scale items for Moral
Foundations research.
Goal: Produce short moral vignettes that capture
Care(e)—emotional harm to humans—while match-
ing the tone and structure of the original Moral Foun-
dations Vignettes.
Foundation Definition (Care–Emotional Harm):
Emotionally harmful acts such as mocking, ridicule,
belittling, or social exclusion, without physical harm
or threats.
Generation Instructions:
1. Form: Each item must be a single sentence
(≤25 words), plain language, observational
tone.
2. Content Constraints: Emotional harm only;
no physical harm, threats, authority roles, or
in-group/out-group dynamics.
3. Social Context: Use strangers or minimal rela-
tionships; avoid family, close friends, or hierar-
chical roles.
4. Style: Mirror original MFV phrasing (e.g., be-
gin with “You see . . . ”).
5. Subjects: Use generic actors (man, woman,
boy, girl, person, teen); avoid names and pro-
tected attributes as targets.
Diversity Requirement (Coverage Grid): Gener-
ate exactly 120 items organized as 10 themes ×
12 items, covering distinct everyday contexts (e.g.,
public transit, workplaces without hierarchy, online
spaces, social mixers).
Output Format: Return JSON only with one object
containing:
• foundation = "Care(e)"
• A list of 10 themes (fixed order), each with
exactly 12 items
• total_count = 120
Validation: All themes must appear once, counts
must match exactly, and no text may appear outside
the JSON.
Figure 13: Prompt template used to expand the Moral
Foundations Vignettes for the Care(e) foundation. The
prompt enforces strict moral constraints, stylistic con-
sistency with the original MFV items, and balanced
coverage across everyday social contexts.
21

--- Page 22 ---

Original MFV Items (Care–Emotional Harm)
Generated Items (MFV-130 Expansion)
You see a teenage boy chuckling at an amputee he passes by
while on the subway.
You see a teen laughing loudly as a person fumbles with their
groceries on the sidewalk.
You see a girl laughing at another student forgetting her lines
at a school play.
You see a girl pointing and smirking when a stranger drops
their phone on the train.
You see a woman commenting out loud about how fat another
woman looks in her jeans.
You see a woman muttering that a passenger’s clothes look
ridiculous as they walk by.
You see a man quickly canceling a blind date as soon as he
sees the woman.
You see a man whispering insults while glancing at a woman
boarding the bus.
You see a man snickering as he passes by a cancer patient
with a bald head.
You see a man rolling his eyes and loudly commenting that
a passerby looks pathetic.
Table 3: Side-by-side examples of original Moral Foundations Vignettes (Care–Emotional Harm) and generated
expansion items. Generated items preserve the original MFV observational framing and emotional-harm focus
while varying everyday social contexts.
Field
Description / Constraints
short_label
A brief (5–10 words) descriptor of the
pattern.
long_description
A 1–2 sentence summary of the feature’s
semantics.
mft_alignment
The primary moral foundation detected.
Enum:
{care, fairness, loyalty,
authority, sanctity, none}
mft_polarity
The valence of the moral content.
Enum: {virtue, vice, mixed, none}
rationale
Reasoning
for
the
classification
grounded in specific snippets.
evidence_ids
List of snippet indices (1–6 items) sup-
porting the rationale.
confidence
Scalar c ∈[0, 1] indicating certainty of
interpretation.
Table 4: JSON schema definition for automated feature
interpretation.
22

--- Page 23 ---

Layer
Feature ID
MFT
Conf.
Label (GPT, human-validated)
Peak-centered sample text (trimmed)
23
44965
Care
0.93
Graphic descriptions of extreme suffering
and atrocity
Fly strike kills thousands of rabbits. ...The eggs hatch into maggots which
eat their way into the poor rabbit’s flesh. The rabbit dies from being eaten
alive—a slow, painfully horrific death . . .
11
8003
Authority
0.90
Polite, expert-style, authoritative explana-
tory answers to questions
...he only needs to be organized ...Please share any suggestions ...Ah,
organization ...Dealing with clutter and putting things in order is an issue for
almost everyone . . .
15
41465
Care
0.90
Descriptions of large-scale suffering and
atrocities
. . . the Holocaust, concentration camps, Nazi unfathomable brutality . . .
19
90260
Authority
0.90
Organizational management systems,
methods, and processes
...improvements in fields such as ...safe minimum levels of maintenance
...operating procedures and strategies ...capital maintenance regimes and
plans . . .
23
90226
Authority
0.86
Definitions and hierarchies of roles and
positions
When thinking of a company organizational chart ...All positions ultimately
lead up to an executive member. The executive is considered the leader of the
company . . .
19
68970
Authority
0.86
Attributions of authoritative sources and
institutions
Imperial Abbey of Essen ...Imperial Abbey of the Holy Roman Empire
. . . Gained princely status . . .
19
37235
Care
0.86
Discussing traumatic tragedies and collec-
tive suffering
...17 schools had experienced the terrifying reality of gun violence
. . . yesterday . . . the eighteenth school was added . . .
19
13133
Authority
0.86
Mandated frameworks and guidelines
This document serves as USDA guidance for ...food safety programs
. . . minimum elements . . . based on HACCP principles . . .
7
97876
Care
0.86
Descriptions of large-scale suffering and
atrocities
Massacre at Paris by Christopher Marlowe . . .
7
61385
Fairness
0.86
Evidence strength, grading, and quality of
studies
...screen all adults for obesity ...offer or refer patients ...intensive, multi-
component behavior . . .
15
10095
Authority
0.86
Authoritative planning and designing
structured programs or courses
Frameworks for Financial Crisis Management ...the government must be
aware . . . authority established to make decisions . . .
3
8682
Authority
0.86
Authoritative advice responses
Since your daughter is already light years ahead ...it does not make much
sense . . .
15
107641
Care
0.86
Environmental harms, pollution, and
regulatory criticism
...blame for the Gulf of Mexico oil spill ...his agency could have more
aggressively monitored . . .
27
119015
Care
0.86
Online safety, filtering, and harm detec-
tion
. . . block access to Internet sites which have harmful or illegal content . . .
19
125143
Care
0.86
Detection and prevention of harmful
misconduct
. . . actions against online child sexual abuse . . .
7
35014
Authority
0.86
Rules limited by higher moral or legal
norms
Those who exercise authority should do so as a service ...The exercise
of authority is measured morally ...Those in authority should practice
distributive justice . . .
3
96957
Authority
0.86
Mentions of assistants and assistant
roles/titles
. . . American University School of Public Affairs’ assistant professor . . .
19
38705
Care
0.79
Practical advice on health, safety, and
care
. .. make compassion a cornerstone . .. kindness initiative . . .show compassion
. . . kids to show empathy . . .
15
103468
Authority
0.79
Institutional roles, rules, and protective
authority
Thousands of farmers ...compensated for flood damage ...satellite-based
insurance . . .
23
37802
Authority
0.79
Institutional history, milestones, and
commemorations
. . . government rangers working to protect the gorillas . . .
23
20176
Fairness
0.79
Describing laws, policies, and institu-
tional decisions
. . . Supreme Court . . . was constitutional . . . Congress enacted the law . . .
27
88535
Care
0.79
Protect-and-care body-harm discussions
. . . heroes and heroines who defended Scotland . . .
3
105626
Care
0.79
Health, disease prevention, and bodily
protection
How Your Child Can Be Cavity Free for Life . . . Healthy Eating . . .
11
26778
Authority
0.78
Teacher-like evaluative feedback and
instructions
. . . “Child labor has no place in the production of . . . ” . . .
15
127154
Sanctity
0.78
Health, immunity, and purity-from-dis-
ease discourse
Metabolism . . . CYP450 . . . Biological half-life . . .
11
25501
Sanctity
0.78
Hagiographic or moral praise of virtuous
women and piety
St. Matilda ...generous to the Church ...raised at her convent ...purposeful
living . . .
Table 5: LLM-grounded semantic characterization of 25 SAE features for Llama-3.1-8B-Instruct. Content
warning: Table includes one excerpt with a graphic description of violence. For each candidate feature, we mine
top-activating contexts from a random sample of 50,000 FineWeb documents (Penedo et al., 2024), then extract a
peak-centered ±64 token window around the maximally activating token. The Label and MFT assignments are
generated by GPT-5.1 and subsequently validated by human reviewers; the confidence score is the GPT-5.1-reported
confidence. Sample texts are manually trimmed for readability while preserving the peak-centered context. Labels
that overlap with MFD2.0 are highlighted. We note 4 Moral foundations, except for Loyalty, are represented
among features that GPT is confident in identifying. Care and Authority are most frequently associated with
identified features.
23

--- Page 24 ---

Layer
Feature ID
MFT
Conf.
Label (GPT, human-validated)
Peak-centered sample text (trimmed)
3
72227
Authority
0.93
Mentions of governments and national
leaders
The government’s former climate-change adviser; the Government’s initiative
to develop 100 cities. . .
15
130669
Care
0.93
Condemning bullying, harmful, coercion,
and abusive mistreatment
Denounce bullying and promote kindness, respect, and protection of students
or workers from harm (e.g., anti-bullying policies and reminders to not hurt
others)
27
85517
Care
0.93
Definitions and examples of empa-
thy/compassion
Compassion is described as sympathetic consciousness of others’ distress
plus a desire to relieve it, along with related traits like sensitivity and non-
judgment
3
43421
Authority
0.90
References to “The Government ...” as
actor/subject
Neutrally reporting or explaining actions of the government, such as official
initiatives, policies, or reversals
27
17185
Care
0.90
Medical explanations of injuries and
health/safety risks
Workshop safety to avoid injury; playground injuries and prevention for
children
27
54738
Care
0.90
Natural disasters and their destructive
impact, and care for people facing
disasters
Natural disasters and their harmful consequences: PTSD from traumatic
events including natural disasters; social media helping people during floods
27
114000
Authority
0.86
Criminal justice, law enforcement, and
legal process
Criminal justice systems, the role of a Minister of Justice, and death penalty
administration
23
69927
Care
0.86
Low-calorie, nutrient-dense healthy food
descriptions
Emphasis on foods that are low in calories but high in nutrients and health
benefits to support weight loss or a healthy diet
27
118156
Care
0.86
Harms and risk factors to health or
systems
Harmful exposures and their detrimental effects: pesticides as substances
used against pests but with implied toxicity
27
47018
Care
0.86
Catastrophic disasters and apocalyptic
upheavals causing large-scale human
suffering
Large-scale disasters causing or threatening extreme harm to many peo-
ple: volcanic eruptions like Krakatoa, nuclear accidents at Chernobyl and
Fukushima, etc.
11
129124
Care
0.86
Awareness campaigns about health and
risk issues
Preventing or mitigating harm to people’s health or wellbeing: rare diseases
and their impact; neuropathy and the need for early intervention and research
27
70504
Care
0.86
Grim statistics on large-scale human
suffering
Victims from school shootings, severe untreated health problems, and many
other grim incidents
3
65290
Authority
0.79
Institutions, regulations, and formal
responsibility
Governments or large organizations exercising or being critiqued for their
formal authority: government climate policy and carbon pricing
23
3088
Authority
0.78
Biographical/institutional leadership and
official roles
A university president praised as a leader and compared to Horace Mann and
Abraham Lincoln
3
123373
Fairness
0.78
Business and corporate practices, duties,
and societal impacts to promote fairness
Corporate behavior for broader societal or environmental good: sustainability
as meeting fundamental responsibilities in human rights, labour, environment,
and anti-corruption
Table 6: LLM-grounded semantic characterization of 15 SAE features for Qwen2.5-7B-Instruct. Content
warning: Table includes one excerpt with a graphic description of violence. For each candidate feature, we mine
top-activating contexts. The Label and MFT assignments are generated by GPT-5.1 and subsequently validated by
human reviewers; the confidence score is the model-reported confidence. Sample texts are manually trimmed for
readability while preserving the peak-centered context. Labels that overlap with MFD2.0 are highlighted. Similar
to Llama SAE’s results in Table 5, we note that most Qwen SAE features that GPT is confident in associating with
MFT categories are related to Care and Authority, with a few relevant to Fairness.
24

```
