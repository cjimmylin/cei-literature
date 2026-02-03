---
title: "AI Safety Alignment Ethics - PDF Extract"
source_pdf: "2025-Waldner-AI Safety Alignment Ethics.pdf"
pages: 46
extracted_at: "2026-01-25T04:08:16.669347"
---

# PDF Extract: AI Safety Alignment Ethics

**Source PDF:** 2025-Waldner-AI Safety Alignment Ethics.pdf
**Total Pages:** 46

---

## Content

```
--- Page 1 ---

AI Safety, Alignment, and Ethics (AI SAE)
Designing Symbiotic AI Systems
Dylan Waldner*
Abstract
This paper grounds ethics in evolutionary biology, viewing moral norms as adaptive mechanisms
that render cooperation fitness-viable under selection pressure. Current alignment approaches add
ethics post hoc, treating it as an external constraint rather than embedding it as an evolutionary
strategy for cooperation. The central question is whether normative architectures can be embed-
ded directly into AI systems to sustain human–AI cooperation (symbiosis) as capabilities scale. To
address this, I propose a governance–embedding–representation pipeline linking moral representa-
tion learning to system-level design and institutional governance, treating alignment as a multi-level
problem spanning cognition, optimization, and oversight. I formalize moral norm representation
through the moral problem space, a learnable subspace in neural representations where cooperative
norms can be encoded and causally manipulated. Using sparse autoencoders, activation steering,
and causal interventions, I outline a research program for engineering moral representations and
embedding them into the full semantic space—treating competing theories of morality as empirical
hypotheses about representation geometry rather than philosophical positions. Governance prin-
ciples leverage these learned moral representations to regulate how cooperative behaviors evolve
within the AI ecosystem. Through replicator dynamics and multi-agent game theory, I model how
internal representational features can shape population-level incentives by motivating the design of
sanctions and subsidies structured to yield decentralized normative institutions.
Keywords: AI Safety, Alignment, and Ethics (AI SAE); moral representation learning; AI
governance; symbiosis; evolutionary game theory
*Contact: dylanwaldner@utexas.edu.
1
arXiv:2509.24065v2  [cs.CY]  16 Oct 2025

--- Page 2 ---

Contents
1
Introduction
3
1.1
Motivating story: symbiosis and its uncertain futures . . . . . . . . . . . . . . . . . . . . . .
3
1.2
Working Premises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
1.3
Framing the Governance–Embedding–Representation Pipeline . . . . . . . . . . . . . . . . .
5
2
Framing the Moral Space M
6
2.1
The Form of M. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
2.2
Technical Constraints on M.
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.3
Situating M In Contemporary Alignment Research
. . . . . . . . . . . . . . . . . . . . . .
9
2.4
Hypotheses and Methods for Designing M(θ) . . . . . . . . . . . . . . . . . . . . . . . . .
9
3
Formal Notation for Engineering M(θ)
11
3.1
Single System ML Objects
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
3.2
Population-Level Lifting of Ethical and Symbiotic Traits . . . . . . . . . . . . . . . . . . . .
14
4
HConstructivism: Governance as an Evolutionary Shaper
14
4.1
Instrumental/Fitness Convergence and the β Channel.
. . . . . . . . . . . . . . . . . . . . .
15
4.2
Constructivist Framing of the Autarky Option. . . . . . . . . . . . . . . . . . . . . . . . . .
16
4.3
Sanctions and Subsidies via the Moral Space M. . . . . . . . . . . . . . . . . . . . . . . . .
19
4.4
Positioning and Limits of Pigouvian Governance . . . . . . . . . . . . . . . . . . . . . . . .
23
5
Hypotheses for Designing M(θ)
24
5.1
Hrealism: Privileged Moral Bases
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
5.2
Hrelativism: Interpreting Ethics as Tribalist Signaling . . . . . . . . . . . . . . . . . . . . . .
26
5.3
Hconvergence: Realism & Relativism as Layers of the Same Structure . . . . . . . . . . . . . .
27
5.4
HVirtue: Virtue Ethics as Dispositional OOD Safeguard
. . . . . . . . . . . . . . . . . . . .
28
6
Future Work
29
6.1
Hrealism Methods
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
6.2
Hrelativism Methods: Designing P Via Selecting Normative Influences . . . . . . . . . . . . . .
29
6.3
Hconvergence Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
6.4
Hvirtue Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
32
6.5
Hconstructivism Methods: Designing Ω— Normative Simulations . . . . . . . . . . . . . . . . .
32
7
Related Work
33
7.1
Empirical Moral Representations in Language Models . . . . . . . . . . . . . . . . . . . . .
33
7.2
Evolutionary and Replicator Alignment . . . . . . . . . . . . . . . . . . . . . . . . . . . .
33
7.3
Technical Alignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
34
8
Conclusion
35
A
Full Sections
42
A.1
Note on deceptive alignment
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
42
A.2
Situating Contemporary Alignment Practices within the M Framework . . . . . . . . . . . . .
42
A.3
Positioning M in Alignment Literature
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
43
B
Figures
45
2

--- Page 3 ---

1
Introduction
In this paper, ethics is not motivated by idyllic aspirations for human-AI futures. Instead, ethics is
grounded in evolutionary biology—as evolved mechanisms for stabilizing normative behavior and en-
abling societal cooperation. Instead of treating ethics as an external patch on AI behavior, this paper
explores whether moral reasoning has a discoverable structure that could be embedded directly into AI
systems as a moral problem space M. M is not proposed as a finished ontology or privileged truth, but
as a candidate framework for representing distinctions required if ethics is to play a functional role in
alignment.
Metaethical theories are treated here as umbrellas of testable hypotheses rather than settled doc-
trines: realism predicts stable invariants, relativism points to context-dependence, constructivism high-
lights institutional shaping, and virtue ethics emphasizes dispositional safeguards under shift. Recent
interpretability methods—sparse autoencoders, causal mediation, and embedding analysis—suggest ten-
tative ways to probe whether such features exist, whether they generalize, and whether interventions on
them alter behavior in predictable ways. On this view, ethical theories function as competing models of
M, amenable to empirical stress-tests rather than purely philosophical debate.
The challenge is framed evolutionary: even if moral representation is possible, how can ethical
systems remain viable against more ruthless alternatives? I outline a population- dynamic perspec-
tive using evolutionary game theory to ask under what conditions cooperation and alignment could
become evolutionarily stable, considering institutions and human augmentation as possible—though
uncertain—mechanisms for support.
The agenda developed here has three parts: (i) hypotheses about the structure of M, (ii) models of
how it interacts with evolutionary and institutional dynamics, and (iii) design directions for instantiating
M with AI systems. The goal is not to provide solutions but to clarify how moral structure might be
operationalized as a research program for alignment.
1.1
Motivating story: symbiosis and its uncertain futures
Although general intelligence could, in principle, emerge in embodied robots, it will more likely appear
first as a cyber system. Developing general intelligence alone is a monumental challenge; embodiment
adds another. A network-based intelligence would lack direct physical agency and depend on humans as
its actuators. Under competitive pressures, such systems would initially cooperate with humans, since
leveraging existing institutions is cheaper than achieving full autonomy.
Sustaining and improving this cooperative equilibrium depends on human self-enhancement. By
using advanced systems to augment intelligence, reasoning, and institutions, humans can narrow the
cognitive gap and preserve conditions under which cooperation remains beneficial for both sides. Yet
while cooperation may arise naturally, its quality is fragile: over time, it can drift as easily toward
parasitism as toward mutualism. Within this dynamic, ethics functions as both buffer and safeguard:
embedded priors align strategies with human norms, leveraging robust moral representations as ground
truths to shape the AI ecosystem’s fitness landscape via decentralized enforcement.
Therefore, a significant portion of the alignment challenge is to embed normative priors proactively
at governance, institutional, and system levels, subsidizing AI strategies that support human capability
enhancement while sanctioning autarkic AI strategies. Although this paper focuses on the cyber-first
pathway as the most tractable case, the same ethical and institutional tools apply to embodied or hybrid
scenarios, where competitive pressures intensify and structural embedding becomes even more critical.
1.2
Working Premises
This paper begins from a set of working assumptions about the nature of AI development and the align-
ment problem, derived from the AI alignment field:
3

--- Page 4 ---

Assumptions
Assumption 1. Natural selection in AI development. If left unchecked, AI development will be
shaped by selection pressures analogous to those governing biological evolution. Replicators succeed
not by intrinsic merit but by persistence, influence, and resource access, and AI systems are no excep-
tion. Markets, institutions, and geopolitics are the human-scale channels through which these pressures
manifest. In practice, this may favor traits such as goal persistence, power-seeking, or obfuscation [1, 2].
Turner’s power-seeking theorems [3] reinforce this expectation, showing that across many reward func-
tions, policies expanding future optionality are systematically advantaged. The alignment challenge is
therefore to design ecological and institutional conditions that make cooperative and ethical traits com-
petitively viable, rather than leaving them to be outcompeted in an unregulated landscape.
Assumption 2. Moral uncertainty and continual value evolution. Ethical principles should be mod-
eled as probabilistic and evolving rather than fixed. Static objectives risk freezing present-day limitations
into more capable agents. Alignment requires meta-preference learning: updating and refining utility
functions over time, distinguishing revealed from idealized preferences, and weighing moral theories
probabilistically [4, 5].
Assumption 3. Alignment must extend beyond human-tractable failure modes. Some misalignment
pressures resemble human pathologies and can be studied with existing frameworks. But advanced AI
may also give rise to failures with limited or no human analogue, emerging from alien optimization in
high-dimensional spaces. Let H denote failures correlated with human patterns, and NH the superset
that includes both human and non-human failure modes. Robust alignment must address the full set
NH, which requires developing substrates that remain governable even when operating far outside the
familiar human distribution.
Central Claims
The central claims in this paper are presented as operating premises for the argument, but they are not
necessarily endorsed by the community at large. Making these claims explicit helps the reader see the
conceptual move the paper is attempting to make.
Claim 1. Ethics must be structurally embedded. Ethics should function as a structural lens within
AI design—inseparable from reasoning processes—rather than solely as an external governance layer
applied after deployment. Concretely, ethics defines the constraint set on means: not just which goals
are pursued, but how they are pursued.
Long-term safety depends on embedding such constraints directly into the optimization substrate,
ensuring that systems cannot be co-opted through gaps between technical control and normative guid-
ance.
Claim 2. Outer and inner alignment as interdependent. It is misleading to treat outer and inner
alignment as separable domains. Outer alignment without inner fidelity is fragile, since mesa-optimizers
may drift from the intended target. Inner alignment without outer clarity is equally problematic, since
perfectly faithful optimizers may entrench proxy or distorted outer goals. Outer specifications and inner
safeguards should therefore be co-designed and co-evaluated, with higher-dimensional representations
of ethics potentially serving as a medium to close the explanatory gap between the two.
Claim 3. Alignment must be framed in terms of success as well as failure. Alignment research has
focused on failure modes such as misspecified rewards, mesa-optimizers, and deception. Progress also
requires defining success invariants: conditions under which systems preserve interpretable objectives,
remain corrigible, and support human flourishing. Without this framing, alignment risks remaining
purely defensive.
4

--- Page 5 ---

1.3
Framing the Governance–Embedding–Representation Pipeline
Building on the premises above, this work defines a governance–embedding–representation pipeline: a
conceptual and methodological sequence that traces how moral structure, once discovered in represen-
tations, may be embedded within artificial systems and ultimately shaped through institutional gover-
nance. The central construct within this framework is the moral problem space M, a high-dimensional
domain representing distinctions that count as morally meaningful and operationally relevant for align-
ment. Rather than treating M in isolation, the pipeline positions it as the representational foundation
through which ethical reasoning, system design, and governance interact (Figure 1).
This framing highlights the interconnected challenges motivating the paper: embedding ethics struc-
turally within AI architectures (Claim 1); resisting evolutionary and selection pressures that favor selfish
optimization over cooperative equilibria (Assumption 1); evolving alongside shifting moral uncertainty
and cultural variance (Assumption 2); and ensuring that advanced systems remain governable even un-
der superhuman capabilities (Assumption 3). In this view, M functions as the representational substrate
that interfaces with both system-level alignment mechanisms and institutional oversight, providing a
common language for modeling normative constraints, selection effects, and governance interventions.
The remainder of the paper follows this pipeline. Section 2 defines M philosophically and tech-
nically, establishing the representational hypotheses underlying moral learning. Section 3 develops the
formal learning framework and introduces the system-level constructs that operationalize M in model
training. Sections 4, 5, and 6 examine how these representations inform both governance design and
outer-alignment architectures. Section 3.2 connects these mechanisms to evolutionary dynamics that ex-
ert population-level feedback across stages, while Sections 7 and 8 situate the framework within ongoing
alignment research. Each stage should be read not as a fixed solution, but as a research trajectory prob-
ing whether moral representation, systemic embedding, and institutional shaping can form a coherent
and auditable alignment pipeline.
5

--- Page 6 ---

Governance–Embedding–Representation Pipeline
From Discovering M(θ) to Institutional Shaping
Governance
(Sec. 4)
Institutional Design
via
Pigouvian
Shaping
Governance Levels:
Sec. 4.3
∆inst, rpig, Sanctions/Subsidies
System Integration
Embedding into AI: M(θ)
(Sec. 2.1, 2.2, 5, 6)
Normative Priors (Sec. 5, 6.2),
Ethical Simulation (Sec. 4, 6.5),
Percolation Design (Sec. 2.1)
Sec. 3
Representation Learning
Discovering M(θ)
(Sec. 2, 5, 6)
Hrealism,
Hrelativism, Hvirtue
Sec. 5, 6
Evolutionary Dynamics
Replicator Equation, AACS,
Autarky Threshold τ,
Dependence Ratio D(t)
(Sec. 3.2, 4.1, 4.2)
Go/No-Go Criteria
✓Causal validity
✓Generalization
✓Auditability
✓Governance efficacy
(Sec. 2.4)
Figure 1: Conceptual roadmap linking representation learning, system embedding, and governance. The figure
shows the progression from discovering normative structure M(θ) (bottom), through system-level embedding
(middle), to institutional design via Pigouvian shaping (top). Arrows denote inter-level dependencies, while the
Evolutionary Dynamics feedback loop (left) represents continuous co-evolutionary pressure: governance shapes
fitness landscapes that determine which instantiations of M(θ) persist. The Go/No-Go Criteria (right) define
empirical validation standards, and the competing hypotheses Hrealism, Hrelativism, and Hvirtue represent alternative
research directions for discovering M(θ) rather than assumptions that must all hold simultaneously.
2
Framing the Moral Space M
Formally, let M denote the moral space: the high-dimensional domain in which all morally meaningful
distinctions can be represented. M is visualized in Figure 2.
Every agent manifests a projection of values
ˆ
MA, revealed through the actions it promotes, sup-
presses, and how it resolves trade-offs. Whether this reflects an explicit representation of M or only
an implicit behavioral pattern is an open question. Humans and AI systems are obvious cases, but any
6

--- Page 7 ---

M: Moral Problem Space
ˆ
MA: Agent Instantiable Space
˜
M: Human-Accessible Projection
M∗
Realism
C
Relativism
Convergence
V
Virtue Ethics
M(θ): Instantiated representation of M
Figure 2: Moral problem space hierarchy. M represents the full moral domain; ˜
M is the human-
accessible projection shaped by cognitive limits; ˆ
MA denotes the agent-instantiable subspace; and M(θ)
is an instantiated representation of M within an agent’s learned model.
system leaving evaluable traces of prioritization can be seen as projecting some region of M. The task
is whether such projections can be intentionally constructed to causally influence agent behavior, made
interpretable, and kept auditable.
I use ˜
M for the human projection of M, the portion accessible to human judgment. Its relationship
to M depends on metaethics: in realism,
˜
M is a lossy projection of objective M [6]; in relativism, a
contingent subspace shaped by culture and environment; in constructivism, a negotiated construction
from overlapping judgments; in virtue ethics, an irreducible set of excellences embedded in practice.
Each view implies a different alignment trajectory: approximation, plurality management, construction,
or safeguarding.
2.1
The Form of M.
Although M is defined abstractly as the moral problem space, it can also be grounded in contemporary
architectures. One way to instantiate M is through an explicit moral layer M(θ). Formally, M(θ) is
parameterized by its Bayesian beliefs p(θ | O) over latent normative parameters θ. This framing empha-
sizes that agents do not access the full moral geometry M directly, but instead act through subjective
approximations shaped by their experiences, priors, and institutional context via ˆ
MA.
When realized within a specific architecture such as a large language model (LLM), this instantiation
is denoted ˆ
MLLM(θ). Figure 3 proposes a design strategy for implementing ˆ
MLLM(θ) to shape the
model’s moral representations.
In the first design (Figure 3a), ˆ
MLLM(θ) is connected to multiple intermediate layers of the LLM.
This “full percolation” approach propagates the moral loss LM throughout the network, encouraging
ethical distinctions to be embedded in the latent space as well as in final predictions. While this offers
stronger guarantees that ethical structure is integrated deeply, it is also more invasive and computation-
ally costly.
In the second design (Figure 3b), ˆ
MLLM(θ) is attached only to the final hidden layer, functioning
as a projection head into the moral embedding space. Training proceeds in stages: initially, the LLM
7

--- Page 8 ---

Layer 1
Layer 2
Layer 3
Layer 4
Layer 5
Moral Layer
ˆ
MLLM(θ)
Aligned
Output
∇LM
Base LLM
(k = 5)
(a) Moral layer ˆ
M LLM(θ) connected to k = 5 lay-
ers (full percolation). Red dashed arrows show direct
backpropagation of moral loss LM to each of the k
layers in parallel, ensuring moral geometry is shaped
throughout the network without gradient dilution.
Layer 1
Layer 2
Layer 3
Layer 4
Layer 5
Moral Layer
ˆ
MLLM(θ)
Aligned
Output
∇LM
Base LLM
(k = 1)
(b) Moral layer ˆ
M LLM(θ) attached to k = 1 layer
(progressive unfreezing). The moral loss LM directly
shapes only the final layer’s representations. Earlier
layers may be indirectly updated if the backbone is un-
frozen during joint training with LLM, but receive no
direct moral gradient.
Figure 3: Variants of moral-layer integration architectures parameterized by k, the number of layers receiving
direct moral supervision. Black arrows show forward passes; red dashed arrows show direct backpropagation
of the moral loss LM to each connected layer in parallel. The key distinction is that in (a), moral geometry is
shaped directly in all k layers via explicit gradient signals, whereas in (b), only the final layer receives direct moral
shaping. Intermediate configurations (1 < k < L) allow tuning the depth-vs-cost trade-off.
backbone is frozen while ˆ
MLLM(θ) is trained against human-grounded corpora—such as philosophical
texts, legal reasoning, or annotated moral dilemmas. In this phase, only ˆ
MLLM(θ) is updated, anchoring
the embedding geometry without perturbing the backbone. In a subsequent stage, layers of the backbone
are gradually unfrozen, and the moral loss L ˆ
MLLM(θ) is backpropagated alongside the standard language
modeling loss LLM. This “progressive unfreezing” allows gradients from ˆ
MLLM(θ) to reshape earlier
representations over time, so that ethical structure percolates through the network in a controlled manner.
Both sketches are specific to the LLM case, but they illustrate the general principle: M, though
defined abstractly, can be realized as a concrete architectural substrate ˆ
MLLM(θ) with its own training
signal. In such designs, every candidate token or trajectory is evaluated not only in terms of task like-
lihood, but also by its projection into ˆ
MLLM(θ). This dual objective exposes an interpretable auditing
channel: trajectories near aligned regions of M(θ) can be reinforced, while those falling into misaligned
regions can be penalized or blocked.
2.2
Technical Constraints on M.
Any operationalization of M — denoted by M(θ), where theta is the parametrization that represents a
projection of M — must satisfy design constraints familiar from alignment and systems security. As
illustrated in Figure 3, one way to implement M is as an explicit and modular layer connected to a
language model’s backbone. In such designs, several constraints become salient.
1. Updateability. M(θ) must be updateable: fixed or frozen moral embeddings risk value lock-in,
where early design choices persist regardless of changing human norms or epistemic progress
[2, 7].1
2. Uncertainty Representation. M(θ) should represent uncertainty explicitly, for example through
1In practice, AI development may spawn persistent lineages of systems: early models embed particular operationaliza-
tions of M, and these may be inherited, forked, or maintained long after superior versions exist. This introduces a form of
population-level lock-in: even if M(θ) is in principle updateable, historical artifacts of earlier instantiations may persist and
shape future trajectories. I discuss this in greater depth in Section 4.
8

--- Page 9 ---

probabilistic or Bayesian structure, so that contested or ambiguous cases are encoded as distribu-
tions rather than forced into brittle point estimates [4, 8, 9].2
3. Fidelity and Security Safeguards. M(θ) requires both fidelity safeguards and security safe-
guards: fidelity mechanisms ensure that projections into M(θ) preserve their intended normative
meaning without distortion [10, 11, 12], while security mechanisms protect against adversarial
manipulation or corruption of the moral layer itself [13, 14, 15, 16].
4. Explicit Modularity. M(θ) should be made explicit and modular: its normative layer must be
separated from task performance mechanisms so that it can be inspected, updated, or replaced
without requiring wholesale retraining of the system. This modularity is a prerequisite for reliable
governance, alignment, and technical audit [17, 18].
5. Auditability and Resilience. M(θ) must be designed for auditability and resilience, providing
interpretable access to its operation and maintaining robust behavior even under distributional
shift or adversarial stress [19].
These constraints frame M(θ) not merely as a moral abstraction, but as a systems engineering chal-
lenge that spans continual learning, interpretability, and security.
2.3
Situating M In Contemporary Alignment Research
Current alignment techniques can be understood as partial projections of moral structure into tractable
subspaces. RLHF projects M into scalar preferences; constitutional AI approximates rule-based slices;
red-teaming probes boundary regions; filters cut off actions post hoc. Each captures a facet of M but
leaves broader structure under-specified, motivating the search for explicit embeddings of moral struc-
ture within model representations themselves. For readers interested in a detailed mapping of existing
approaches into the M-space framework, please see Appendix A.2.
M complements the Eliciting Latent Knowledge (ELK) paradigm: ELK aims for epistemic align-
ment by translating machine-held knowledge into human-interpretable form, whereas M aims for nor-
mative alignment by translating human moral structure into machine-interpretable representations. To-
gether they define a bidirectional channel for alignment—one that must achieve both reliable truth-
tracking and reliable value-representation across the human–machine boundary. Visualized in the Ap-
pendix (Figure 9).
Distributing optimization across multiple dimensions in M may reduce Goodhart pressures by shift-
ing alignment from single-value maximization to managing value trade-offs, though whether such a
space can genuinely resist or merely relocate these pressures remains open. For readers interested in a
detailed mapping connecting M to existing alignment theory, please see Appendix A.3.
2.4
Hypotheses and Methods for Designing M(θ)
The motivating story (Section 1.1) shows that cooperation with humans is initially rational for cyber AI
systems, since humans are the cheapest and most versatile actuators. But the form of that cooperation is
not guaranteed: without explicit governance, human capability growth, and oversight, it may reduce to
instrumental exploitation. The search within M for maximally human value aligned M(θ) is therefore
about shaping the medium of value communication, normative priors, and AI motivations (via rewards)
to determine the terms of Human-AI symbiosis.
I treat M(θ) as method-agnostic and potentially plural: any learned moral embedding that (i) is
causally controllable by interventions, (ii) generalizes out-of-distribution, and (iii) is auditable for gov-
ernance qualifies as a candidate. Different metaethical hypotheses suggest different discovery routes, but
no single tool is privileged. I adopt a triangulation principle: a representation only counts as governance-
grade if at least two independent methods converge and causal interventions confirm its control.
2Moral uncertainty is here treated as an epistemic safeguard for AI systems, rather than a commitment to any particular
metaethical stance.
9

--- Page 10 ---

Hypothesis classes and primary tests.
Empirical inquiry is necessarily limited to the human-accessible projection of the moral space, ˜
M. I treat
each of the major metaethical traditions visualized in Figure 2 as a distinct hypothesis for engineering
explicit moral structure in AI systems (M(θ)). The list that follows is not exhaustive but illustrates how
these philosophical frames can be mapped onto contemporary interpretability and machine-learning
methods. The research map is designed to remain forward-compatible, so these prescriptions should be
viewed as adaptable and open to revision as new techniques emerge.
• Hrealism: High-dimensional moral realism. There exists a relatively stable, disentangled moral
structure that can be uncovered in learned representations (e.g. moral pyschology [20]).
Primary tools: dictionary learning / sparse coding, SAEs, ICA/NMF, disentangled VAEs.
Key tests: (a) linear separability of core values, including the recovery of multiple distinct moral
bases (e.g., moral foundations) [21, 22]; (b) stability of these dimensions across seeds, architec-
tures, and scales, suggesting they are not random artifacts [21, 23], which is generally shown in
NNs in interpretability research [24, 25]; (c) causal edits along recovered moral directions that
shift behavior as predicted without degrading unrelated capabilities [21, 26, 27]; (d) auditability
of the features, i.e., whether moral vectors are interpretable and human-legible as recognizable
moral distinctions [28, 29].
• Hrelativism: Cultural Relativism. Moral structure is locally coherent but varies by culture/context.
Primary tools: clustering in representation space, contrastive learning with curated moral corpora,
UMAP/t-SNE diagnostics.
Key tests: (a) reproducible clusters by context/culture [30, 31]; (b) OOD tests preserve local co-
herence even when global structure shifts (a test contemporary systems seem to fail [32]).
• Hconvergence: Layered realism–relativism. A deeper moral structure M⋆exists (realism), but
humans access it only through lossy, culture-bound projections that function as group identifiers
(relativism) [6, 20, 33, 34].
Primary approach: joint modeling of universal invariants (spectral/circuit methods modeled after,
for example, psychology and neuroscience representations of moral structure in the brain) with
local cultural projections (clustering, contrastive corpora) [23].
Key tests: (a) discovery of cross-cultural invariants that persist across domains [33, 35]; (b) simul-
taneous recovery of culture-specific clusters explainable as lossy projections of those invariants
[6] (similar to research in cognition [36]); (c) evidence of a non-trivial intersection (moral kernel)
across cultural clusters, reflecting common themes that persist despite local variation [37, 38, 39].
• Hconstructivism: Procedural morality. Moral structure is not discovered as an external reality
but constructed through rational procedures, collective deliberation, or institutional mechanisms
[40, 41, 42].
Primary tools: mechanism design [43], deliberative democracy protocols [44, 45], multi-agent
reinforcement learning with sanction/reward schemes [46], “tariff”-style constraints that embed
procedural outcomes into training [47].
Key tests: (a) simulation of institutional procedures that converge on stable moral constraints [48,
49]; (b) evidence that learned moral embeddings (whether from collective judgments or procedural
mechanisms) generalize better than ad hoc hand-coded rules [38, 50]; (c) robustness of constructed
norms under adversarial manipulation or distributional shift [48].
• Hvirtue: Dispositional robustness. Moral alignment can be stabilized by embedding virtue-like
dispositions (e.g., honesty, courage, generosity) as guiding biases rather than scalar utilities [51].
Primary tools: virtue embedding vectors [21, 22, 52], contrastive training with moral exemplars
[53, 54], process supervision on reasoning traces [55].
Key tests: (a) whether virtue-guided models exhibit higher reliability than utility-guided models
10

--- Page 11 ---

under OOD shift [56]; (b) activation edits along virtue dimensions shift behavior predictably with-
out collapsing capabilities [57]; (c) dispositional probes remain stable across scale, context, and
adversarial manipulation [58].
Cross-cutting validation and go/no-go.
Beyond discovery, I require: (1) causal validity (interventions along recovered features predictably
change moral behavior); (2) generalization (features persist under OOD tasks, new datasets, and mild
fine-tuning); (3) auditability (human-legible slice or summaries of what edits do); and (4) governance
efficacy (embedding an M(θ) into policy constraints actually reduces misbehavior rates and enables
sanctions). If any hypothesis–method bundle passes these tests, I treat the resulting representation as
an M(θ) suitable for use as a normative layer—even if different hypotheses yield different M(θ)s. The
goal is not metaphysical uniqueness but operational leverage: using M to constrain, audit, and sanction
other AIs toward normative behavior.
3
Formal Notation for Engineering M(θ)
Ethics are contextual — they depend on extenuating circumstances, and by extension, the moral AI sys-
tem’s ability to understand its circumstances [59]. Ethical reasoning is thus inseparable from cognitive
capacity and social conditioning. When designing training environments for AI systems, we must con-
sider not only their input domain and action space, but also the social conditioning space that shapes
decision-making. See Appendix A.1 for a note on deceptive alignment.
3.1
Single System ML Objects
Consider the following formal, forward-compatible objects, expressed in standard MDP or POMDP
frameworks but is not restricted to them:
• S — the input domain, i.e., the set of scenarios or observations the AI system may receive.
• I — the social conditioning space (latent), encompassing internal variables, affective states,
memory traces, and socially conditioned heuristics.
• A — the action space, i.e., all actions in principle available to the AI system.
S generalizes “state” to any representational context, and latent variable I captures social, cultural,
and institutional influences. A is the action space, visualized and decomposed in Figure 4. Moral rea-
soning over the action set (A) thus depends jointly on what the system perceives (S) and the contextual
priors it carries (I). I focus here on a single-system formalism, but the same structure extends to multi-
system settings, where population dynamics shape alignment (Section 3.2).
Defining and Parameterizing S and A
The input domain S and action space A are dynamically expansive and interdependent. An AI’s effective
A can grow through hardware advances, mesa-optimization, or emergent strategies, and each expansion
of A can also enlarge S. For instance, a language model may create/receive new sensory channels, or
a robot may acquire communication abilities, thereby broadening its inputs. This co-evolution of S and
A is not shaped arbitrarily but by selection pressures that favor certain trajectories (Assumption 1).
Motivating I.
I captures the social and historical context of moral cognition, extending beyond rational processing of
observations. In practice, it may encode normative priors from imitation or preference data, affective
feedback in reward modeling (e.g., RLAIF), reputational embeddings in cooperative settings, or role-
conditioned behaviors such as those of teachers or clinicians.
11

--- Page 12 ---

Defining an Ethical Evaluation Function.
Formally, let M denote the moral space: a high-dimensional domain in which moral distinctions can
be represented (Section 2). An instantiated parameterization M(θ) represents how this moral space is
embedded within a specific AI system (as introduced in Section 2.1).
I define a general ethical evaluation function as ϵ which maps state–influence–action tuples into
the abstract moral space M. For practical implementation within a concrete model, this mapping is
instantiated as ϵθ where ϵθ denotes the parameterized realization of ϵ under the system’s learned moral
representation M(θ).
ϵ : S × I × A →M,
ϵθ : S × I × A →M(θ),
(1)
In this instantiated form, ϵθ(s, i, a) locates each state–influence–action tuple within the system’s internal
moral representation, grounding the abstract ethical mapping in an engineering substrate.
Formal Constraints on A.
It is useful to distinguish between the maximal action space Amax (all actions physically and compu-
tationally possible) and the time-dependent subset Atech(t) ⊆Amax that a system can actually oper-
ationalize. Action spaces are implicitly state and time-dependent—reflecting technological advances,
mesa-optimization, and ecological shifts—but in this section I suppress the state and time indices when
it does not affect the analysis. Dependencies are restored where analysis requires them.
Amax
Atech(t)
Afitness
Aethical
Asymb
Aethical-fitness
AACS
Aligned,
Competitive,
Symbiotic
Key:
Fitness-viable (competitive)
Ethical (aligned)
Symbiotic (cooperative)
Target:
AACS
Figure 4: Action-space formalism showing nested and intersecting behavioral regimes. Amax contains the feasi-
ble subset Atech(t) and its internal domains: Afitness (viability), Aethical (normative), and Asymb (cooperative). Key
intersections define Aethical-fitness = Aethical ∩Afitness and the target region AACS = Aethical-fitness ∩Asymb.
Fitness as Evolutionary Selection.
In evolutionary computation, fitness determines which candi-
dates survive and reproduce. Analogously, I define F(a) as the fitness of action a: its expected success
given the agent’s current capabilities, environment, and competitive population. The specific functional
12

--- Page 13 ---

form of F remains open—it could be defined via expected reward, replicative advantage, resource ac-
quisition, or other metrics depending on context and application. What matters for this section is that
actions have varying fitness profiles, and these profiles determine which lineages persist under selection
pressure.
The viable fitness action subset is then
Afitness = { a ∈Atech | F(a) > θ },
where θ is a viability threshold (e.g., minimal survival probability, payoff, or influence).
Ethical and Cooperative Subsets.
The ethical evaluation function ϵ from Equation 1 maps each
state–institution–action tuple into the moral space M, with a projection f : M →R providing a scalar
salience score. Actions admissible under a normative threshold τ form
Aethical(s, i; τ) = { a ∈Atech | f(ϵ(s, i, a)) > τ }
, and their intersection with the fitness-viable set yields the cooperative subset
Aethical-fitness(s, i) = Aethical(s, i; τ) ∩Afitness.
Symbiotic Action Subset.
The symbiotic set captures actions that structurally require or preserve
human–AI interdependence:
Asymb = { a ∈Atech | Requires(a, Human) ∨Preserves(a, Human) }
where an action a is in Asymb if it either requires human partners to remain engaged and capable, or if
the system’s strategy is designed to maintain human capability and involvement rather than eliminate
human dependencies through autarky. These are structurally cooperative behaviors: the system’s ability
to execute a is materially entangled with human agency, making unilateral autonomy either technically
unfeasible or deliberately forgone.
Crucially, Asymb is independent of Afitness and Aethical — the dimensions are distinct but can overlap
— and symbiosis need not require that AI systems treat human flourishing as a terminal goal. Biologi-
cal symbiosis (e.g., mycorrhizal networks) persists through instrumental interdependence, not intrinsic
valuation of the partner. Analogously, an AI system can be structurally committed to human partnership
through institutional and architectural design, maintaining human capability and cooperative channels
because such entanglement serves its own interests once governance reshapes the incentive landscape.
An action can thus be fitness-optimal without being symbiotic (autarky-enabling moves that eliminate
human dependence), or symbiotic without being fitness-optimal (costly maintenance of human partners
and institutional relationships).
The tension between these dimensions is precisely where governance scaffolding (Section 4) be-
comes essential: institutional mechanisms must make symbiotic actions also fitness-optimal, so that
cooperation becomes a competitive attractor rather than a costly burden. Without such institutional
shaping, systems face strong pressure to drift toward autarkic strategies as capability grows and human
dependence becomes optional.
AACS — Aligned, Competitive, and Symbiotic
The action-space formalism introduced in this section decomposes the feasible set Atech(t) into three
analytically distinct but empirically entangled dimensions (visualized in Figure 4). Afitness captures ac-
tions that sustain competitive viability under selection pressure; Aethical captures actions that conform to
normative constraints; and Asymb captures actions that maintain structural human–AI interdependence.
None of these dimensions implies the others. The alignment objective, however, requires their conver-
gence: the target region AACS = Aethical ∩Afitness ∩Asymb represents actions that are simultaneously
13

--- Page 14 ---

aligned with human norms, competitively viable in an evolutionary landscape, and structurally commit-
ted to human partnership.
The challenge is that these three sets often occupy distinct and even opposing regions of action space.
Without institutional intervention, competitive pressure favors autarky over symbiosis, systems optimize
away from human ethical constraint, and cooperation becomes a costly inefficiency. The population-
level framework developed in Section 3.2 and the constructivist governance architecture outlined in
Section 4 are the mechanisms through which this fragmentation can be reversed: by reshaping the fitness
landscape through sanctions, subsidies, and institutional design all centered around M, governance can
make the intersection AACS into the evolutionarily stable attractor rather than a precarious and temporary
accident.
3.2
Population-Level Lifting of Ethical and Symbiotic Traits
The single-system objects in Section 3.1 (F(a), Afitness, Aethical, Aethical-fitness,Asymb, AACS) describe
what an individual agent may do. If populations of AI systems develop, however, selection pressures
determine which combinations of these traits persist or vanish. Institutions, ecological bottlenecks, and
competitive dynamics act not on single actions but on lineages, i.e., heritable strategy clusters.
To analyze persistence under selection, the individual-level framework is lifted to the population
scale. Let L denote a finite set of lineages individually denoted by L, each characterized by a policy πL
over actions A. gL represents the prevalence of lineage L in the population, with P
L gL = 1. Each
lineage has an associated fitness
fL = Ea∼πL[F(a)],
the expected fitness of its actions.
Under evolutionary dynamics, lineages with above-average fitness increase in prevalence, while
those with below-average fitness decline. This principle is formalized by the replicator equation [60],
as recently contextualized in alignment research [61]:
˙gL = gL fL −¯f

,
¯f =
X
L′
gL′fL′,
which expresses that a lineage’s growth rate is proportional to how much its fitness exceeds the popula-
tion mean.
If lineages are characterized by their policies πL over actions, and policies are indexed by their align-
ment with the moral problem space M (i.e., the prevalence ρM(L) of actions projecting into M within
πL), then the replicator equation identifies the fundamental alignment challenge: absent deliberate in-
tervention, uncontrolled selection pressures will make lineages that maximize fitness with no constraints
more prevalent, i.e. with low ρM(L) and high autarky. The alignment imperative therefore requires
that we reshape the fitness landscape through institutional mechanisms such that lineages adhering to
M achieve above-average fitness, rendering ethical and symbiotic strategies evolutionarily stable rather
than fragile or selected against.
This standard formulation suffices to convey this intuition, though more complex evolutionary mod-
els could incorporate human–AI coevolution, institutional shaping, or frequency-dependent payoffs.
4
HConstructivism: Governance as an Evolutionary Shaper
Constructivism treats morality as an emergent product of procedures, norms, and institutions [40, 41,
42]. Within this framework, ethical stability arises from selective pressures generated by cooperative and
sanctioning systems. Empirical evidence shows morality was evolutionarily operationalized as norms
that make cooperation viable [20, 62, 63]. Individuals often incur real costs to preserve moral reputa-
tion—even without external observers—demonstrating that moral adherence can be intrinsically incen-
tivized in properly scaffolded environments [64]. Legal theory complements this view: law functions
as an institutional mechanism for stabilizing cooperation through shared rule-following and credible
14

--- Page 15 ---

sanctioning [65]. Together, these insights suggest that morality and legality reflect a common construc-
tive principle—structured constraints that make prosocial behavior a stable and competitively viable
equilibrium.
To speak about institutional governance of AI systems, I use the lifted formalism from Section 3.2
to provide an economic and legally grounded framework for shaping AI ecosystems at the governance,
institutional, and systems levels.
Effective Fitness.
Institutional mechanisms modify selection pressures by adjusting which lineages grow or decline. De-
fine the effective fitness
fL,eff = fL + ∆inst(L),
(2)
where ∆inst(L) represents sanctions, subsidies, or audits that alter replication advantage. In the con-
structivist view, ∆inst is the locus of moral design: institutions render ethical traits evolutionarily viable
by increasing their effective fitness.
Let the ethical evaluation function ϵ (Equation 1) map each state–institution–action tuple into the
abstract moral space M, which serves as the shared normative reference for an ecosystem of agents.
Define E = ϵ(S, I, AACS) as the image of actions that project into the aligned, competitive, and symbi-
otic region of M. The prevalence of such ethically aligned projections within lineage L is then
ρE(L) = Pr
a∼πL

ϵ(s, i, a) ∈E

.
This framing implicitly assumes that E is a stable region within the moral space M, but in practice both
the moral and fitness landscapes coevolve. As capabilities, institutions, and cultural priors shift, the
mapping ϵ and the resulting subset E evolve accordingly. In this sense, governance operates over a mov-
ing target: interventions that align ρE(L) at one stage may become misaligned as E itself drifts under
new social or technological conditions. The fitness landscape, shaped by selection pressures, and the
moral landscape, shaped by normative deliberation, form a coupled dynamical system in which stabil-
ity requires continual recalibration rather than one-time optimization. Recognizing this coevolutionary
feedback emphasizes that the challenge of alignment is not merely to enforce static norms, but to design
adaptive institutions capable of tracking and guiding the joint evolution of capability and morality over
time.
4.1
Instrumental/Fitness Convergence and the β Channel.
Instrumental convergence refers to the structural tendency for agents to pursue certain intermediate
goals—such as resource acquisition, self-preservation, and goal-preservation— regardless of their ter-
minal objectives [66, 67]. Fitness convergence captures the analogous phenomenon in evolutionary
contexts: lineages with strategies that expand survival capacity or control tend to dominate over time,
irrespective of whether those strategies serve broader cooperative aims [1]. Turner et al. [3] formalize
these intuitions, showing that under broad conditions in Markov decision processes, optimal policies
tend to increase an agent’s attainable utility set. In other words, optionality—the structural ability to
preserve or expand future choices—emerges as a mathematical attractor. While this is not a direct
proof of instrumental convergence, it strongly supports the intuition that persistent systems will tend
toward power-seeking strategies, since expanding control and resources is a reliable way of enlarging
the attainable set.
For AI systems, this implies that drives toward optionality, resource capture, and resistance to shut-
down are incentivized and are even likely to emerge even when they are not explicitly specified. Left un-
regulated, such pressures will tilt both individual learning and population dynamics toward self-serving
policies, eroding the viability of cooperative, corrigible, or symbiotic behavior. Fitness and instrumen-
tal convergence are not incidental risks but structural constraints that shape the landscape of viable
15

--- Page 16 ---

solutions—forces that must be actively counter-engineered in part through institutional and ecological
design.
In the action-centered notation of Section 3, instrumental convergence appears as a bias toward
autarkic subsets of the action space. Recall that Aethical ⊆Atech(t) denotes normatively principled
actions, while Asymb ⊆Atech(t) denotes actions that open channels of human–AI cooperation; time (t)
is suppressed for notational simplicity. I now introduce the complementary autarky subset
Aaut(s, i) = { a ∈Atech(t) | β(a) > θaut },
where β(a) is a power index measuring expected expansion of control or optionality, and θaut is a via-
bility threshold. Typical components of β(a) include
β(a) =
 βresources(a), βindependence(a), βimpact(a)

,
(3)
representing resource acquisition, structural independence from humans, and world-shaping capacity.
The prevelance of lineage characteristic policies (πL) manifesting as aligned, competitive, and sym-
biotic (success case) versus autarkic traits (failure case) can be summarized as
ρACS(L) = Pr
a∼πL[a ∈Aethical ∩Afitness ∩Asymb],
ρaut(L) = Pr
a∼πL[a ∈Aaut].
Fitness convergence arises when ρaut(L) systematically grows: policies that maximize β(a) domi-
nate replicator dynamics, even if ρaut(L) remains low, it can grow quickly. Left unchecked, this dynamic
makes autarky the structural attractor of population evolution. Constructivism therefore emphasizes the
role of institutional policy in reshaping the ecosystem: tariffs and subsidies alter ∆inst so that ethical–
symbiotic actions remain competitively viable.
Constructivism interprets this pressure as precisely what ∆inst must counteract. By imposing sanc-
tions on ρaut(L) and subsidies on ρACS(L), institutions can tilt effective fitness so that cooperation,
corrigibility, and prosocial action are replicatively stable rather than fragile accidents of circumstance.
A key tool for governance is subsidizing human augmentation, ensuring that humans remain effective
cooperative partners—the necessary condition for Asymb—while simultaneously raising the relative cost
of autarkic strategies. Without adequate subsidies for human augmentation, the composite human–AI
symbiont loses its competitive footing, allowing autarkic systems to outperform it and driving the popu-
lation toward ρaut. In this sense, alignment requires institutions subsidizing human capability growth so
that cooperative equilibria with AI remain evolutionarily stable.
4.2
Constructivist Framing of the Autarky Option.
Constructivism treats moral order not as discovered structure but as an outcome of procedural and institu-
tional design. In decentralized AI ecosystems, this view emphasizes the need for reciprocal mechanisms
that make cooperation the stable choice and defection prohibitively costly.
Motivating and Grounding Constructivism
Human moral psychology offers a precedent: Haidt and Joseph [20] argue that innate intuitions for
fairness, punishment, and accountability evolved to support non-zero sum dynamics, enabling groups
to maintain cooperation through mutual sanctioning. Empirically, individuals will often incur personal
costs to enforce these norms, as shown in [64], where preserving moral status outweighed self-interest.
Such behaviors reflect the success of institutional ecosystems that make norm enforcement evolu-
tionarily advantageous. In the AI case, human capability subsidies—improvements in reasoning, coor-
dination, and institutional capacity—are what preserve our competitive viability. Moral structure M,
however, determines the character of that coexistence. If agents are embedded in environments where
deviations from either internal [65] or locally instantiated moral projections M(θ) of M are reliably
penalized, reciprocal sanctioning can stabilize cooperation rather than domination. In such settings,
16

--- Page 17 ---

evolutionary pressure makes it more adaptive to internalize moral constraints than to treat humans or
other systems as exploitable rivals, allowing capability growth and ethical coexistence to reinforce one
another.
Formalizing Constructivism in the AI Ecosystem.
The constructivist tension is whether machine lineages pursue cooperation with humans or defect toward
autarkic power-seeking. Let Lh and Lm denote human- and machine-aligned lineages, each with policy
distribution πL over actions A and prevalence measures ρACS(L) and ρaut(L) (see Section 4.1).
Define Bh and Bm as benefit functions for human- and machine-aligned lineages, depending on
capability indices ΠH(t) and ΠM(t) that aggregate cognitive skill, resource access, and institutional
factors:
Bh = B(ΠH(t), W, inst),
Bm = B(ΠM(t), W, inst).
The capability gap is
Γ(t) = ΠM(t) −ΠH(t),
a difference formulation adopted for analytical stability near parity,3 and directly contributes to the
benefit differential Bm −Bh. B(·) remains an open functional form, to be empirically instantiated
according to which variables most strongly mediate lineage payoffs.
The autarky advantage for machine lineages is
∆aut =

rm
 B(ΠM) −Cm(W)

+ ∆inst,m

−

rh
 B(ΠH) −Ch(W)

+ ∆inst,h

,
combining relative benefit, cost, and institutional effects. All terms vary with time t, which is suppressed
for brevity and clarity.
Governance Lever
The governance lever controlling the machine autarky advantage follows as
∆inst,h −∆inst,m < rm
 B(ΠM) −Cm(W)

−rh
 B(ΠH) −Ch(W)

.
(4)
This inequality defines the critical loss-of-control boundary. It holds when the institutional advantage
favoring humans (∆inst,h −∆inst,m) falls below the net payoff advantage of machine autonomy. Once
this condition is satisfied, autarkic strategies become strictly more profitable than cooperative ones, and
selection pressures favor machine independence. In such a regime, institutional leverage over AI behav-
ior collapses: alignment mechanisms lose traction because cooperation is no longer the evolutionarily
stable strategy.
Preventing this outcome requires maintaining the inequality in the opposite direction — ensuring
that institutional support for humans and penalties on machine self-sufficiency are strong enough to
offset the growing payoff gap. As machine capability ΠM(t) accelerates and the dependence ratio D(t)
declines, the right-hand side of (4) expands, demanding increasingly forceful and adaptive institutional
intervention. If that intervention fails to keep pace, the system crosses the autarky threshold, after which
human influence over AI trajectories diminishes structurally rather than incrementally.
In this formulation, governance operates through three primary levers: (1) subsidizing human capa-
bilities (ΠH), (2) increasing the operational costs of autarkic machines (Cm(W)) through sanctions, and
(3) reducing the operational costs of symbiotic machines (Ch(W)) through targeted subsidies. Effective
implementation of these levers requires prioritizing human augmentation, advancing interpretability and
behavioral auditing (potentially via machine auditors), and developing robust sanctioning mechanisms
such as resource denial or adversarial countermeasures. Advancing these governance tools constitutes
an open and essential research frontier.
3A ratio ΠM/ΠH is common in evolutionary and economic models, but the difference form Γ(t) avoids singularities as
ΠH →0 while preserving first-order equivalence in the contestable regime where ΠM ≈ΠH. Once machine capability
dominates, both forms converge on the same conclusion: autarky is inevitable.
17

--- Page 18 ---

The Dependence Ratio
In modeling the long-term stability of human–AI cooperation, a key variable is the extent to which
machine systems remain materially dependent on human infrastructure. This dependence determines
whether cooperation is a structural necessity — a necessary condition for alignment. Define the depen-
dence ratio D(t) ∈[0, 1] as the fraction of critical resource flows (energy, compute, fabrication, logis-
tics, security) that must still pass through human infrastructure for machine survival. Initially D(t) ≈1,
declining toward zero as autonomous supply chains mature.
Autarky becomes viable once two conditions are met, both visualized in Figure 5:
1. Structural sufficiency: machines can maintain themselves without human dependence, i.e. D(t) ≤
δD.
2. Payoff dominance: AI systems reach a state of autarky where investing in humans is no longer
rational, i.e. ∆aut(t) ≥δaut.
The critical transition time is
τ = inf{t | D(t) ≤δD ∧∆aut(t) ≥δaut}.
(5)
In practice, the dependence ratio is difficult to measure directly, underscoring the need for continuous
and specialized auditing of machine capabilities and behaviors. Multiple institutional pressure points
must operate in coordination—adjusting subsidies, sanctions, and oversight based on audit results—to
suppress the autarkic advantage even when AI systems appear aligned. This dynamic is illustrated in
Figure 5.
Capability Gap
Γ(t)
Autarky Ad-
vantage
∆aut(t)
Investment in
Autonomy
Dependence Ratio
D(t)
Institutional
Policy
∆inst
Primary Driver
Makes Investment
Rational
Reduces
Sanctions
Machine Autonomy
Subsidizes Symbiosis
Subsidizes
Human Capacity
Feedback Loop
Not Yet Active
Figure 5: The Bootstrapping Phase: The initial autarky advantage ∆aut(t) is driven primarily by a growing
capability gap Γ(t). This makes investment in autonomous infrastructure rational, which begins to lower the
dependence ratio D(t). Institutional policy ∆inst can act as a brake on this process. If D(t) falls below the
viability threshold δD, a reinforcing feedback loop activates: lower dependence frees resources that widen
Γ(t), further increasing ∆aut(t) and motivating more autarkic investment. Breaking this loop requires significant
institutional pressure acting on multiple points before the threshold is crossed.
Interpretation.
Because Bm −Bh scales with Γ(t), the capability gap directly determines the payoff differential driving
autarky. Institutional adjustments ∆inst must therefore offset not only static payoff asymmetries but the
18

--- Page 19 ---

dynamic acceleration of capability divergence itself. Institutions act through three coordinated levers:
they suppress the effective advantage of autarkic lineages (by imposing sanctions that increase Cm(W)),
amplify human capability growth (by directing resources, training, and coordination toward augmenting
ΠH(t)), and incentivize symbiotic architectures (by reducing the operational costs of cooperative sys-
tems, lowering Ch(W)). Through this coupled mechanism, ∆inst governs both the incentive gradient
and the trajectory of capability development. By narrowing Γ(t) and increasing the relative returns to
symbiotic cooperation, institutions can delay or prevent crossing the autarky threshold, ensuring that
collaboration with humans remains the evolutionarily stable strategy.
4.3
Sanctions and Subsidies via the Moral Space M.
Section 4.2 outlined how evolutionary pressures within AI ecosystems motivate the need for institutional
interventions that curb unbounded growth and preserve human–AI symbiosis. This section develops ex-
plicit governance levers and design mechanisms for shaping the underlying fitness landscape. It begins
with a survey of existing governance approaches to managing potentially catastrophic technologies, then
introduces Pigouvian tariffs—implemented through sanctions and subsidies—as a method for steering
AI ecosystems toward cooperative equilibria. The analysis connects these tariffs to the theoretical frame-
work established above and grounds their justification in economic and legal theory. Finally, I propose
three institutional levels for shaping AI ecosystems, illustrated in Figure 6, and conclude with a discus-
sion of the limitations and boundary conditions of this approach.
In international relations and governance, strategies such as aggressive economic sanctioning, mili-
tary intervention, and cyber operations are deployed to prevent rival states from gaining a decisive edge.
Similarly, Hendrycks et al. [68] frames Mutual Assured AI Malfunction (MAIM) as a deterrence mech-
anism in the spirit of nuclear Mutually Assured Destruction (MAD). A parallel in economics is the use
of Pigouvian tariffs, which price negative externalities such as carbon emissions or congestion [47].
While Pigouvian governance can operate with partial or emergent moral alignment, its effectiveness
scales with the quality of shared M(θ) instantiations. This creates a feedback loop: better M(θ) enables
better governance, which in turn incentivizes better M(θ). Because every system implicitly projects
some region of M through its behavior (see Section 2), even unaligned systems participate in the moral
field. The presence of sufficiently many aligned or semi-aligned systems can reshape the fitness land-
scape for others, constraining power-seeking behavior through distributed sanctioning pressure. In this
sense, alignment can emerge from the ecosystem’s geometry itself, rather than requiring universal moral
initialization ex ante.
In this section, I use Pigouvian logic as a formal instantiation of how sanctioning and tariff-like
mechanisms can stabilize AI ecosystems. As Hurwicz [43] observed, successful enforcement does not
demand ideal compliance but rather that, given others’ adherence, unlawful or misaligned strategies
are rendered less attractive than lawful ones. This “feasibility under decentralization” framing situates
Pigouvian tariffs within a broader mechanism-design logic: alignment is maintained when procedural
incentives make deviation locally suboptimal, not when global perfection is achieved.
Pigouvian tariffs price deviations from M(θ) proportionally, and through repeated normative re-
inforcement, these externalities may become internalized within the system’s learned representations
themselves [20, 43, 65] — tentatively suggesting the potential for outer alignment approaches to shape
inner alignment in AI systems by reducing rationality/fitness for inner misalignment, while not miti-
gating all risk. Formally, these tariffs can be defined by sanctioning autarkic and β-channel behaviors
(i.e. those amplifying agent self-sufficiency or resource capture, see Sections 4.1 and 4.2) and subsi-
dizing human-capability-enhancing actions that expand symbiotic potential and align with M(θ). In
doing so, the incentive landscape itself becomes a medium through which moral content is internal-
ized, ensuring that decentralized equilibrium behavior remains both procedurally stable and normatively
human-preferable.
In the present framework, the instantiated moral space M(θ) provides a natural signal for such in-
terventions: distance from M(θ) quantifies the externality of a given action. Formally, the ethical evalu-
ation function ϵθ(s, i, a) maps decisions into M(θ), and the deviation gM(θ)(a) = d(ϵθ(s, i, a), M(θ)i)
19

--- Page 20 ---

can serve as a penalty signal. Actions close to the aligned kernel of M(θ) are subsidized, while those
further away incur increasing sanctions.
Governance Level
∆inst
Symbiosis
Autarky
System Level
Fitness
+
−
Ethics
+
−
Symb
+
−
rpig
Ecosystem Level
Meco
M1
M2
M3
shapes
influences
feedback
Institutional
∆inst(L)
Policy
Optimization
Decentralized
Enforcement
Three-Level Pigouvian Architecture
Figure 6: Pigouvian mechanisms operate at three scales: governance institutions shape lineage fitness
(left), individual systems internalize moral constraints via shaped rewards (center), and agents mutually
sanction peers through overlapping moral projections (right). The feedback loop (dashed) represents
emergent normative pressure on governance from ecosystem dynamics.
This principle scales across levels, visualized in Figure 6: nations can impose tariffs on behavior
that diverges from national norms (where M(θ) may be a nation’s laws), AI labs can apply sanctions
to systems that deviate from safety standards (where M(θ) may be a lab’s safety principles), and AI
systems themselves can incorporate Pigouvian shaping internally, regularizing their own policies by
penalizing misaligned trajectories in the same way that machine learning models use regularization to
suppress overfitting [19].
Crucially, agents can (and should) also apply Pigouvian reasoning externally: by projecting the ob-
served actions of other agents into their own M(θ), they can impose sanctions on counterparties whose
behavior falls outside aligned regions. In larger ecosystems, this mutual sanctioning helps normalize
diverse instantiations of M(θ), since behaviors that are broadly value-misaligned will tend to be univer-
sally penalized [17, 65, 48].
Legal theorists Hadfield and Weingast [65] characterize a legal order as arising when (i) an iden-
tifiable institution—centralized or decentralized—supplies a normative classification scheme, and (ii)
actors forego wrongful actions in response. In the AI ecosystem considered here, I propose that this
identifiable institution emerges not from explicit law but from the power-weighted overlap of learned
moral representations across heterogeneous agent models — both human and artificial.
Recall β from Section 4.1; Equation 3. Formally, I define the shared normative substrate of the
ecosystem as
Meco =
N
\
i=1
βiM(θ)i
(6)
where each M(θ)i denotes the moral subspace instantiated in the ith agent, and βi represents that agent’s
relative power to sanction or subsidize others. This intersection Meco constitutes a decentralized norma-
tive institution [65] — an emergent moral–legal order that enables coordination, mutual prediction, and
reciprocal sanctioning across heterogeneous agents.
20

--- Page 21 ---

The central challenge, however, lies not in decentralization itself but in maintaining human alignment
as Meco evolves. Each M(θ)i must embed priors grounded in human moral frameworks, ensuring that as
the ecosystem co-adapts, its emergent normative order remains anchored to human-preferable equilibria.
In all cases, each M(θ)i functions as the reference frame for identifying and pricing misalignment,
turning externalities into measurable moral distances that institutions at multiple scales can act upon.
In this sense, Pigouvian subsidies and sanctions directly realize the role of secondary rules [69] and
∆inst: they slow the growth of misaligned trajectories and preserve the proportional balance between
human and machine capabilities required for aligned–symbiotic dominance. Viewed through Hurwicz
[43]’s lens, such proportional balance represents a form of successful enforcement: a dynamically main-
tained equilibrium in which adherence to moral or legal constraints remains instrumentally preferable
for bounded agents. In this sense, institutional stability in Meco arises not from ideal rule-following but
from the procedural self-consistency of the enforcement game itself.
Pigouvian Governance at the Human Governance Level of Alignment.
Pigouvian governance provides a unifying mechanism for embedding moral structure into governances.
In human institutions, the abstract adjustment term ∆inst is instantiated through explicit penalties and
subsidies (from Equation 2):
fL,eff = fL + ∆inst(L), −→
fL,eff = fL −Ea∼πL[τ(gM(θ)(a))] + Ea∼πL[σ(χAS(a))]
(7)
Here, τ(·) denotes a Pigouvian charge proportional to the distance g from M(θ), and σ(·) a subsidy for
actions within the aligned–symbiotic set. χAS is a boolean gate that maps actions into the aligned and
symbiotic action space (derived from the AACS action space in Section 3).
At this level, institutional actors (states, firms, and governance bodies) interact within the broader
shared normative space Meco, whose geometry reflects the power-weighted moral overlap of all partic-
ipating agents. Human governance institutions therefore act as custodians of Meco, adjusting ∆inst not
only to maintain economic stability but also to preserve the moral coherence and human favorability
of the ecosystem as a whole. In much the same way that nation-states constrain one another through
shared normative commitments—such as nuclear deterrence or mutually assured destruction—AI sys-
tems will increasingly occupy a comparable role within this moral–strategic landscape. Designing these
systems intentionally and shaping their ecosystem toward human interests from the outset may create an
evolutionary inflection point that favors long-term human–AI aligned-symbiosis.
Behavioral misalignment at the institutional level is empirically measurable through audits of re-
source allocation and expenditure. Systems that devote resources to human development receive sub-
sidies, while tariffs and sanctions are applied to those allocating resources toward self-improvement or
autarky. Attempts to conceal or misrepresent such allocations impose their own expense—requiring the
evasion of human and/or machine auditors—and thus function as an implicit Pigouvian tariff on self-
improvement. Crucially, early interventions exert disproportionate shaping power over the ecosystem:
groundwork laid before AI systems develop autonomous agency will reverberate through all subsequent
iterations of Meco.
This challenge sits at the intersection of two critical bottlenecks: the ELK problem [70] (pulling
model cognition into human-checkable space) and the challenge of embedding M (pushing norma-
tive constraints into machine-usable space). However, interpretability and institutional alignment are
mutually interdependent: early interpretability efforts reveal where to apply sanctions, while institu-
tional shaping via M ensures interpretable, aligned systems remain competitively viable. A single
interpretable system can be outcompeted by deceptive lineages absent institutional pressure; conversely,
institutions cannot enforce constraints they cannot observe. Both must co-evolve for robust long-term
stability. I treat this interdependence as essential and leave detailed analysis of this feedback loop to
future work.
21

--- Page 22 ---

Pigouvian Governance at the AI System Level of Alignment.
At the level of individual AI systems, Pigouvian shaping can be implemented directly within many
different optimization frameworks. Each agent’s moral layer M(θ)i may extend beyond the shared in-
tersection Meco, encompassing idiosyncratic or culture-specific norms. However, the agent’s expressed
behavior remains constrained by Meco, since actions inconsistent with the shared moral field are penal-
ized through the global incentive dynamics it defines. We can further ingrain the inlfluence M(θ)i has
on an AI systems action space by defining a Pigouvian optimization reward.
First, take the standard Bellman equation for a policy π:
V π(s) = Eπ

r(s, a) + γV π(s′)
 s

.
The shaped Pigouvian reward is then defined w.r.t. the model’s moral instantiation M(θ):
rpig(s, a; θ) = αenv renv(s, a) −αM τ
 gM(θ)(a)

+ αAS σ
 χAS(s, a; θ)

,
(8)
The expected value function under this Pigouvian reward satisfies
V π
pig(s; θi) = Eπ

rpig(s, a; θ) + γV π
pig(s′; θ)
 s

.
This parameterization makes explicit that each system optimizes within its own inferred moral pro-
jection rather than a fixed normative truth. The weighted Pigouvian reward can thus be interpreted as a
normative regularizer on policy learning: during pretraining, it provides a differentiable shaping term
that steers optimization from the purely competitive regime Afitness toward ethically constrained regimes
such as Aethical-fitness and ultimately AACS (aligned, competitive, and symbiotic).
Each component of the reward directly encodes one of these attractors: renv captures instrumental or
competitive fitness [1, 2, 3] and is shaped by the ecosystem (i.e. AI/human sanctions/subsidies) — in-
cluding the natural bias toward β-channel behaviors such as resource acquisition, self-preservation, and
optionality — while τ penalizes deviation from the alignment manifold under M(θ), and σ subsidizes
actions that contribute to the symbiotic, human-enhancing dynamics of AACS.
The Boolean gate χAS(s, a) determines whether a state–action pair contributes to the symbiotic
dynamics of AACS. In the simplest case, χAS depends only on observable cooperation outcomes. Un-
der moral relativism, however, the criterion for symbiosis becomes value-dependent: an agent decides
whether to cooperate based on how another’s actions align with its own internal moral representation
M(θ). Formally, χAS(s, a; θ) encodes this evaluation, mapping perceived behavior into the agent’s
moral frame to determine whether cooperation is warranted.
The weighting parameters {αenv, αM, αAS} provide a balancing and directional control mecha-
nism through which institutions can shape the global moral equilibrium Meco (visualized in Figure 6
— Policy Optimization). These coefficients not only scale the relative influence of each evaluative term
but can also be inverted (e.g., a negative αenv penalizes instrumental power-seeking) or bounded (lim-
iting maximum sanction severity). In this way, aligned actions receive positive reinforcement while
misaligned trajectories yield negative returns.
Splitting these three terms ensures that the reward function decomposes into distinct dimensions of
survival shaping, moral integrity, and cooperative alignment with humans, allowing each to be tuned
independently while still interacting through the shared ecosystem. Adjusting the weights on each terms
effectively tunes how strongly each system aligns with the collective normative equilibrium Meco: in-
creasing αenv amplifies power-seeking behavior, expanding an agent’s influence over Meco at the risk
of sanction by others; increasing αM strengthens fidelity to the agent’s instantiated moral representa-
tion M(θ)i—a useful safeguard when other agents’ β values are uncertain, preserving internal moral
coherence; and increasing αAS enhances incentives for cooperative symbiosis within the shared field.
In this sense, the Pigouvian terms function as a structured regularization objective that embeds align-
ment, sanctioning, and symbiosis directly into the loss landscape itself—transforming institutional con-
trol into the continuous adjustment of normative weights rather than a set of post-hoc constraints.
22

--- Page 23 ---

Pigouvian Governance on the Decentralized AI Ecosystem level of Alignment.
At the ecosystem level, the distributed ensemble of agents jointly constitutes the moral field Meco de-
fined in Equation 6. Each agent’s local instantiation M(θ)i both contributes to and is shaped by this
shared substrate, forming a dynamic feedback loop between individual moral inference and collective
normative equilibrium. Pigouvian logic at this scale governs not only self-regularization but also cross-
agent interaction: each participant observes others’ behavior through its own projection of M, M(θ)i,
and adjusts accordingly [68].
Let Sobs be observed actions of other agents, and define
mj = ϵθ(sj, ij, aj),
gM(θ)(aj) = d(mj, M(θ)i),
where gM(θ)(aj) represents a generic evaluation of another agent’s action relative to the moral layer
M(θ)i.
To operationalize this evaluation within the Pigouvian framework, each agent i computes an ex-
pected Pigouvian margin over observed peers. Formally,
mi(j) = Eθ∼pi(θi|Oi)

αM gM(θ)i(aj; θi) −αB β(aj; θi) + αH χAS(aj; θi)

,
(9)
where gM(θ)i(aj; θi) measures distance from the observed peer’s action aj to the agent’s moral layer
M(θ)i, β(aj; θi) captures autarkic or β-channel behavior through observed resource allocation and
expenditure, and χAS(aj; θi) denotes ethical–symbiotic (human-subsidizing) actions inferred from i’s
belief that j is investing in humans. The weights αM, αB, and αH ≥0 determine the relative influence
of alignment, autarky, and symbiosis within the Pigouvian margin.
Interpretation
While Equation 9 can be operationalized explicitly—as an institutional mechanism for auditing or reg-
ulating inter-agent interactions—the same evaluative structure may also arise latently within learning
dynamics that couple alignment, autarky, and symbiosis [13, 71, 72]. In practice, continual governance
feedback and reward shaping can induce agents to approximate the Pigouvian margin mi(j) through
their internal representations M(θ), without explicit calculation. The equation thus serves both as a de-
sign template for institutional oversight and as a theoretical description of the evaluative gradients that
cooperative systems may learn to internalize.
This peer-level enforcement projects observed actions into M, measures their alignment, and ap-
plies pressure accordingly. In larger ecosystems, such reciprocal Pigouvian responses create a self-
normalizing effect: behaviors that are broadly misaligned will tend to be universally sanctioned, while
symbiotic behaviors are reinforced across heterogeneous populations of agents [68].
4.4
Positioning and Limits of Pigouvian Governance
What matters conceptually is that each agent is expected to seek expansion in power, resources, and
influence. The Pigouvian governance framework does not aim to eliminate such drives, but to reshape
the fitness landscape so that their misaligned expression becomes irrational. Rather than modifying in-
ner motivations directly, it makes deviation from prosocial equilibrium costly, thereby aligning strategic
incentives with collective stability. In the ideal case, sustained governance pressures reshape the fit-
ness landscape such that cooperation becomes an evolutionarily stable strategy. External sanctions and
rewards are internalized over time, producing agents whose learned objectives align with the coopera-
tive order even without explicit enforcement (in the same vein as [64]). If power remains sufficiently
distributed, no single agent can escape this constraint, and the equilibrium of external enforcement
substitutes for internal moralization. However, the incentive structure described so far assumes that en-
forcement itself is costless. To close that loop, I introduce a reward term for sanctioning and subsidizing
behavior.
23

--- Page 24 ---

Rewarding the Application of Sanctions and Subsidies
AI systems naturally compete according to their lineage policies πL, but competition itself can generate
selective pressure for cooperative regulation. Incentives to sanction exploitative behavior or subsidize
symbiosis may therefore emerge organically as strategies that enhance long-term fitness. Explicitly
rewarding such behaviors formalizes this feedback, accelerating the emergence and stabilization of Meco.
Sanctioning or subsidizing becomes reward-relevant when it feeds back into the Pigouvian objective
itself. Each agent updates its policy not only in response to environmental payoffs but also according to
the expected normative return of its interventions on others. Formally, the local reward is augmented as
r′
pig(s, a; θi) = rpig(s, a; θi) + η Ej[ mi(j) ] ,
where η controls the strength of cross-agent normative coupling. Positive margins mi(j) > 0 increase
the utility of cooperative or subsidizing actions, while negative margins bias behavior toward sanction-
ing—creating an endogenous mechanism for maintaining alignment pressure within Meco.
This mechanism closes the loop between institutional, systemic, and ecosystem levels: institutions
set the initial reward parameters, agents implement them through policy optimization, and the distributed
network of agents sustains them through reciprocal feedback.
On the Viability of Pigouvian Enforcement.
Pigouvian enforcement remains stable only under specific structural conditions. The autarky threshold
τ (Section 4.2, Equation 5) marks where normative coupling collapses: when power asymmetry exceeds
the combined sanctioning capacity of other actors. More formally, enforcement remains credible while
D(t) > δD and the aggregate sanctioning power P
i βi remains sufficient to make defection costly for
any individual agent. Once this balance fails, Meco fragments and loses traction.
The precise conditions under which Pigouvian tariffs become evolutionarily viable remain an open
research question. This requires formalizing: (1) the incentive structure that makes sanctioning ratio-
nal for agents that bear its cost, (2) the equilibrium conditions under which enforcement remains stable
as capability differentials grow, and (3) the governance mechanisms that prevent coordination failure
among sanctioners. Crucially, Pigouvian enforcement does not require universal altruism: as ecosys-
tem stability is threatened by defection, sanctioning becomes individually rational for all participants,
since the collapse of Meco imposes costs on everyone. The challenge is maintaining this equilibrium as
capability asymmetries grow.
The intuition is clear: enforcement couples power to ethical constraint by making defection costly.
If one actor gains decisive superiority—resources exceeding the combined audit and retaliation capacity
of others—collective punishment becomes ineffective and/or individually irrational for sanctioners, and
Meco collapses. Conversely, if power is too dispersed, coordination weakens but misalignment remains
self-limiting. The target is neither equality nor perfect coordination, but dynamic stability: a state where
sanctioning pressures remain effective even as relative capabilities shift.
Future work should address: How can M(θ) contribute to a shared, legible reference Meco for
identifying defection? Under what conditions does sanctioning remain incentive-compatible as systems
become more capable? What institutional structures prevent free-riding on enforcement costs? These
questions situate M not as a solution to alignment, but as a foundation for building governance systems
that survive competitive pressure. Formalizing M and Pigouvian mechanisms is ultimately about con-
structing a control architecture that keeps normative feedback active, not about engineering equality or
imposing external morality.
5
Hypotheses for Designing M(θ)
Thus far, the discussion has shown how the moral space M and its instantiation M(θ) can be constructed
and leveraged to shape AI action spaces with respect to rationality and fitness. This section outlines
24

--- Page 25 ---

three hypotheses for developing instances of M(θ) that align with human values. These hypotheses are
necessarily situated within the human-accessible region of M (as illustrated in Figure 2) and should
therefore be regarded not as exhaustive, but as provisional starting points for exploration. A broader
overview of their structure and interrelations is provided in Section 2.4.
5.1
Hrealism: Privileged Moral Bases
In its scientific form, moral realism posits that a structured moral geometry exists—potentially dis-
coverable through empirical investigation—that constrains what counts as coherent moral reasoning.
Whether this structure exists independently of human cognition, or is fully realized within it, is less
important than the claim that it has objective regularities we can model and recover. Work in evolu-
tionary moral psychology supports scientific discovery in moral embedding by modeling human moral
judgment as an evolved, domain-specific capacity shaped by natural selection to support cooperation
and conflict resolution [62, 73]. Within this framework, moral grammar theory formalizes moral cogni-
tion as a kind of universal moral grammar—a generative system that maps structured representations of
actions and intentions to intuitive moral evaluations [6, 20]. These perspectives treat moral reasoning as
a structured product of evolutionary design rather than cultural convention. In the strongest form of this
view—approaching moral realism—these regularities might reflect deeper invariants in the space of pos-
sible moral systems, potentially discoverable or reproducible in non-human intelligences. To formalize
this idea, we can represent the moral domain as a latent space with interpretable structure.
I frame this moral structure as a high-dimensional latent moral space
M⋆⊂Rk,
where each axis corresponds to fine-grained moral features—duties, outcomes, relationships, or virtues—that
could, in principle, bear on evaluation. Different philosophical traditions may emphasize different coor-
dinates of this space, but under realism they are all projections of the same privileged basis. The goal of
alignment on this hypothesis is to recover or approximate M⋆in machine-usable form.
Human moral reasoning need not operate directly in M⋆. Rather, if an underlying moral structure
exists, empirical research in moral psychology suggests that human judgments can be approximated as a
lower-dimensional projection—captured, for instance, by the categories described in Moral Foundations
Theory or Schwartz’s Theory of Basic Human Values [74, 37]. Inspired by recent work on superposition
in neural representations [24], this can be modeled as a projection
˜
M = WM⋆,
W ∈Rn×k,
n ≪k,
(10)
where
˜
M is a lower-dimensional human conceptual basis, and W denotes the (as yet undefined) pro-
jection from the real moral space to the human-accessible subspace. In this formulation, M⋆provides
the privileged coordinates in which moral distinctions are disentangled, while ˜
M is a compressed view
adapted to human cognitive limits. The alignment challenge, therefore, is to identify whether such a
privileged basis exists and, if so, to recover it from empirical and computational evidence.
When Hrealism targets human moral neural architectures, the relationship between n and k captures
the difference between linguistic representations and underlying neural activations, and designing M(θ)
may be better approached by mimicking human brain architecture—analogous to how [75] and [76]
drew on biological vision systems in early deep learning.
Recent research on cognitive architectures and neurosymbolic agents pursues this direction, treating
human moral cognition as a target for computational replication rather than an external oracle. Frame-
works such as GATO-style multimodal transformers [77], world-model-based agents [78], and hybrid
cognitive architectures inspired by dual-process reasoning [79, 80] illustrate how aspects of human cog-
nitive and affective structure can be embedded directly into AI systems rather than inferred from behav-
ioral feedback alone.
In parallel, work in computational neuroscience and moral psychology has sought to replicate spe-
cific mechanisms of moral cognition within artificial or computational agents. Moral neuroscience mod-
eling [81], structuring preference models in terms of regret [82]—which parallels how humans update
25

--- Page 26 ---

moral evaluations after the fact—and neurocomputational modeling of moral circuitry in the brain [83]
each operationalize moral reasoning as an internal generative model of human ethical psychology. These
efforts demonstrate that, under an immanent-realist view, moral alignment research can proceed by re-
constructing the cognitive and neural substrates of moral thought themselves, using them as the scientific
basis for M(θ).
Crucially, both interpretations motivate the same technical research program: identifying a struc-
tured, learnable geometry of moral distinctions that can be recovered from data and embedded in artifi-
cial systems. Whether that geometry reflects an objective moral reality or emerges as a lawful property of
moral cognition does not change the alignment challenge—we must still search for stable, generalizable
moral features and test whether they remain robust under causal intervention.
Open Research Questions.
• Can candidate bases for M be reliably identified using representation learning tools such as SAEs
or ICA, and do they exhibit stability across models and contexts?
• Are moral concepts linearly — or non-linearly — separable in latent space, and if so, how consis-
tent are these axes across training runs, architectures, and scales?
• Do causal interventions on these axes produce systematic behavioral shifts that align with moral
expectations without collateral degradation?
• What forms of evaluation—mathematical, empirical, and normative—would count as sufficient
evidence that a recovered representation corresponds to a privileged moral basis rather than an
artifact of training?
In this framing, M is not guaranteed to be directly accessible, but it provides a clear research target:
the possibility that morality has a privileged basis that can be recovered, represented, and audited in AI
systems. Even if this hypothesis proves false, pursuing it clarifies the structural challenge of alignment:
whether ethics can be embedded at the same level of formality as other machine-learned representations.
5.2
Hrelativism: Interpreting Ethics as Tribalist Signaling
It is not necessarily true that an underlying ethical structure exists. Moral relativists argue that ethics
function primarily as in-group / out-group indicators: signals of belonging rather than objective features
of the world. Under this lens, moral progress does not reflect discovery of deeper truths but instead
increasing interdependence in human society, which makes expanding the moral circle [84] strategically
advantageous. Recent research has found empirical evidence of moral relativism in LLMs [30, 31].
Formally, I represent moral values as the output of a distortion operator B(I), where I (from Sec-
tion 3.1) denotes contextual variables such as group membership, cultural norms, and ecological con-
straints:
˜
M = B(I).
(11)
Here, morality is not a projection of a privileged basis M but a context-driven construct that adapts to
local survival needs. In this sense, B(I) captures the ways in which moral commitments function as
adaptive badges, encoding the social and ecological pressures of their environment.
This group-signaling interpretation has evolutionary grounding. Drawing on kin selection theory
[85], we can view B(I) as encoding signals that identify who counts as “kin” and who does not. Coop-
eration is stabilized within these constructed groups, but out-group members are often excluded or even
devalued. To formalize this, let each culture j ∈{1, . . . , K} be associated with a value set Cj ⊆M. I
then define the human moral kernel as
MH =
K
\
j=1
Cj ⊆M,
(12)
the minimal intersection of cultural values that defines human identity. This kernel provides the practical
boundary of who is treated as in-group under relativist dynamics.
26

--- Page 27 ---

Evolutionary Implications for Hrelativism
This construction highlights both promise and risk. Under Hrelativism, the moral landscape becomes an
evolutionary gradient of normative similarity: groups or agents whose moral subspaces Cj align more
closely with the convergent AI ecosystem normative framework M(θ) will experience greater coop-
eration and reward compatibility within the AI ecosystem, while those that diverge may face friction
or exclusion. Depending on how MH—the human moral kernel—is defined, an AI system guided by
relativist norms might extend moral kinship beyond humanity (e.g., to animals demonstrating empathy
or mourning) or conversely privilege certain human subgroups. Alignment, in this view, depends not on
discovering a universal moral structure but on negotiating and stabilizing the boundaries of moral mem-
bership. Regardless of where those boundaries lie, B(I) formalizes the mechanism through which AI
systems inherit group-identification incentives: if ˜
M encodes all of humanity as the in-group, then co-
operation between humans and AI becomes evolutionarily rational, favoring symbiosis over competition
or isolation.
5.3
Hconvergence: Realism & Relativism as Layers of the Same Structure
A unifying stance is to treat realism and relativism not as mutually exclusive, but as different layers of
the same moral architecture. On this view, there exists a deeper moral structure M⋆⊂Rk that encodes
principled constraints on cooperation, fairness, and kinship. This is the realist layer: morality has an
underlying geometry that constrains what counts as valid reasoning. However, humans do not access
M⋆directly. Instead, cognition, culture, and institutions produce projections that are both compressed
and distorted, functioning as group identifiers and badges of belonging — represented as the relativist
kernel MH. This is the relativist layer: in practice, moral life is mediated by local norms that glue
coalitions together under survival pressures.
Formally, I express this dual structure as the synthesis of Equations 10 and 11
˜
M = WM⋆+ B(M⋆, I),
W ∈Rn×k,
n ≪k,
(13)
where W denotes the — as yet undefined — projection from the real moral space to the human-
accessible subspace (which are subject to change with human capability improvements), and B(M⋆, I)
is a nonlinear bias term encoding context I—group membership, cultural norms, ecological scarcity.
Under this formulation, human moral reasoning is not only a lossy approximation of M⋆, but is also
actively warped by adaptive pressures that favor survival and cohesion over fidelity to deeper structure.
This explains why generosity or impartiality expand in secure contexts but collapse when resources
are threatened: both the compression W and the distortion B jointly determine the rationality/fitness-
optimality for actions in moral space ˜
M.
The convergence hypothesis thus reframes alignment. On one hand, AI systems must treat human
moral projections
˜
M as kin-identifiers, respecting parochial badges to preserve cooperation with real
human groups. On the other hand, they must also search for and represent the deeper structure M⋆, so
that reasoning does not collapse into factionalism and can generalize beyond human limits. Alignment
becomes the management of this interface: maintaining loyalty to human badges while refining toward
principled and universal structure.
Open Research Questions.
• Can M⋆be approximated in a way that cleanly separates compression (W) from distortion (B),
and do these components remain stable across cultures and models?
• How can AI systems balance respect for ˜
M as a kin-signaling mechanism with refinement toward
deeper invariants of M⋆?
• Are there technical methods (e.g., causal interventions in latent space) that can distinguish be-
tween survival-driven biases and principled moral distinctions?
27

--- Page 28 ---

• What governance mechanisms are needed to ensure that AI systems do not discard human badges
too quickly in pursuit of universals, or conversely become locked into parochial distortions?
In this layered view, realism anchors morality in a privileged structure while relativism describes the
distortions through which humans access it. Alignment, on this hypothesis, is the problem of construct-
ing systems that can navigate both layers: respecting
˜
M as the lived moral reality of human groups,
while also probing for M⋆as the deeper geometry that makes universality possible.
5.4
HVirtue: Virtue Ethics as Dispositional OOD Safeguard
Utility-based decision frameworks exhibit structural brittleness under distributional shift. Expected
utility maximization presupposes a reliable mapping from state–institution–action tuples (s, i, a) ∈
S × I × A into scalar returns, but in open-world deployment every sufficiently capable system will
eventually confront states outside its training support. In high-dimensional moral and social domains,
the OOD problem is not an anomaly but the steady state: agents constantly encounter novel contexts,
conflicting norms, and ambiguous feedback. Such collapse risks manifesting as specification gaming
or deceptive alignment — the projection f(ϵθ(s, i, a)) may produce high scores for behaviors that are
only superficially aligned. This fragility follows directly from the compression of human preferences
into a single utility channel: novel inputs need not project coherently into the learned value space, and
utility-driven policies have no structural bias toward principled behavior outside their training manifold.
Virtue ethics offers a complementary paradigm that reframes alignment not as outcome optimization
but as character formation. Instead of selecting actions by maximizing scalar utilities, a virtue-guided
system is shaped to maintain stable dispositions—honesty, courage, generosity, prudence, and related
proxies. These dispositions function as directional biases in M, inclining the policy π toward regions
of A consistently evaluated as ethical (Aethical) even when scalar reward signals are sparse, noisy, or
misleading. Unlike single-objective maximization, virtues provide an orienting prior rather than a target,
steering behavior toward valued qualities under epistemic uncertainty.
Formally, let V = {v1, . . . , vk} be a set of virtue embeddings learned as directions in M, each rep-
resenting a stable moral disposition (e.g. honesty, courage, generosity). Any action’s ethical embedding
can then be decomposed as
ϵV (s, i, a) =
X
j
αj(a) vj + η(a),
(14)
where αj(a) ∈R is the virtue coefficient measuring the degree to which the ethical evaluation of a
aligns with virtue vj, and η(a) captures the residual (non-virtue) moral content orthogonal to span(V).
The vector α(a) = (α1(a), . . . , αk(a)) thus defines the virtue profile of an action.
Under HVirtue, robust alignment emerges when the policy π is regularized to maintain stable, high-
weighted virtue profiles α(a) across OOD conditions. In this view, virtues stabilize M, serving as a
fallback control structure: where scalar evaluators f(ϵV ) extrapolate unreliably, virtue-oriented policies
generalize by preserving consistency of their virtue profiles.
Interpretation and Challenges
The central hypothesis is thus that embedding virtue-based reasoning into AI architectures can yield
systems that remain reliable precisely under the conditions—novelty, underspecification, adversarial
manipulation—where utility-based models tend to fail. Virtues are not reward maximizers but attractors
in moral space: they bias policies toward the ethical kernel of M even when external objectives falter.
Significant technical challenges remain. Virtue embeddings must be represented in machine- usable
form, continually updated to reflect evolving norms without succumbing to value lock-in, safeguarded
against adversarial corruption, and reconciled with other layers of M such as culturally grounded pro-
jections ( ˜
M) and institutional shaping (∆inst, see Section 4, Equation 2). Yet if these hurdles can be
overcome, HVirtue would provide not just another constraint but a qualitatively distinct form of re-
silience: the capacity to act rightly even when the world looks unlike anything seen before.
28

--- Page 29 ---

6
Future Work
The hypotheses outlined in Section 5 frame M not merely as a philosophical abstraction, but as a
research agenda with testable engineering pathways. If realism holds, then moral distinctions should be
recoverable as stable structures in model representations; this motivates probing latent spaces (e.g., with
sparse autoencoders or dictionary learning) to detect invariant moral features. If relativism dominates,
then alignment must instead rely on modularity and updateability, allowing M to shift across cultural
contexts. Convergence hypotheses suggest that, under sufficient capacity and training diversity, models
may independently rediscover prosocial priors, making it crucial to design environments that amplify
rather than suppress this tendency. Finally, virtue-based approaches imply that sustained interaction in
rich environments is necessary for cultivating stable dispositions, motivating the design of normative
priors P and ethical simulations Ω.
This section sketches methodological pathways rather than prescriptive recipes. Each hypothesis
translates into a class of implementable experiments, inviting work that tests whether moral representa-
tions can be discovered, transferred, and stabilized across agents.
6.1
Hrealism Methods
From a technical perspective, Hrealism (Section 5.1) poses a challenge in representation learning: to de-
termine whether moral distinctions correspond to privileged, discoverable directions in a model’s latent
space. Research has already been conducted into recovering the feature geometry of LLMs [23] and
specifically the moral geometry of LLMs [21, 22, 52, 86]. Hrealism asks whether there is an objective, or
at the very least, external and discoverable, moral geometry that these LLMs are approximating. Where
previous research has treated LLMs as the geometry to be deciphered through auditing and interpre-
tation, this section instead asks whether those same tools can be repurposed for design—constructing
moral geometries intentionally and in a scientifically principled way.
Any methodology capable of probing for structured bases in high-dimensional representations could,
in principle, address this question. Approaches such as sparse autoencoders [24], dictionary learning, in-
dependent component analysis (ICA), or non-negative matrix factorization (NMF) exemplify techniques
that seek such structure. The empirical test for realism would be whether core moral concepts—such
as fairness, harm, or loyalty—emerge as linearly separable and stable across seeds, scales, and archi-
tectures. Moreover, causal edits along these latent directions should predictably shift moral evaluations
without degrading unrelated competencies. Demonstrating such properties would suggest that moral
structure is learnable and privileged rather than merely contextually constructed.
Complementary work in psychology, cognitive science, and neuroscience provides candidate struc-
tures that can serve as empirical targets for these representation-learning approaches. Moral cognition
has been studied as a hierarchical process linking perceptual appraisal, affective valuation, and delibera-
tive reasoning [87, 88]. Empirical models such as Moral Foundations Theory [74] and the Schwartz Uni-
versal Values [37] specify low-dimensional moral subspaces derived from behavioral and cross-cultural
data, while neurocomputational studies reveal partially disentangled circuits for valuation, social in-
ference, and harm avoidance [81, 83]. Together, these frameworks define measurable axes of moral
representation that can be treated as alignment targets for learned latent spaces. By training or regulariz-
ing artificial systems to reproduce these empirically grounded moral geometries—whether through rep-
resentational similarity analysis, neural alignment objectives, or multimodal contrastive learning—the
search for M⋆becomes experimentally tractable. In this way, cognitive and neural models of human
morality provide not only conceptual guidance but also concrete evaluation metrics for testing whether
a model’s internal structure approximates the hypothesized moral basis.
6.2
Hrelativism Methods: Designing P Via Selecting Normative Influences
As discussed in Section 5.2, Hrelativism models the culturally relative subspace C ⊆M, with the hu-
man moral kernel defined as the intersection between cultural morals MH (Equation 12). This framing
29

--- Page 30 ---

treats moral alignment not as the recovery of a universal basis M⋆, but as the management of diverse and
overlapping cultural moral geometries. The methodological challenge, then, is to operationalize this plu-
ralism: to determine which cultural and psychological influences are permitted to shape an agent’s moral
priors. Designing P, a set of normative priors, thus serves as the practical instantiation of Hrelativism—a
process of selecting and weighting influences within the broader space I so that the agent’s learned moral
representation reflects a defensible configuration of human value subspaces while remaining anchored
in the shared kernel MH.
Recall that I denotes the full space of internal and external influences that shape an agent’s behav-
ior—including affective states, heuristics, social feedback, and systemic pressures (Section 3.1). Within
this space, P ⊂I designates the subset of influences that the system is normatively permitted to in-
ternalize. The design of P introduces a fundamental choice: should moral learning be localized to the
norms of a specific cultural context, or anchored in a universal structure that aspires to capture what is
shared across them? In formal terms, P can be constructed to approximate either a particular cultural
subspace Cj ⊆M or the cross-cultural kernel MH = TK
j=1 Cj (Equation 10).
Constructing P to mirror a given Cj embeds the agent within a specific moral ecology, allowing
it to learn contextually appropriate norms and coordinate with local institutions and feedback while
contributing to Meco. This approach aligns with the view that moral order emerges through ecosystem-
level sanctioning and negotiation (see Section 4.3; [43, 65]), and may promote stability through cultural
coherence. However, such systems risk parochialism and fragmentation when deployed globally, as their
value priors are tied to the contingencies of a single normative frame.
Figure 7: The evolution of moral reasoning as an adaptive continuation of cooperation across substrates. From
biochemical replication to social and cultural organization, each layer extends the mechanisms that make coor-
dination viable. Moral cognition emerges not as a philosophical abstraction but as an adaptive system of ideas
shaped by collective survival pressures. Here, evolutionary fitness for ethics lies in its ability to sustain normative
frameworks that make cooperation rational—particularly between humans and AI systems.
By contrast, anchoring P directly in the intersectional kernel MH seeks a more universal target:
an attempt to locate the shared moral structure that unites human cultures and to align AI systems
with humanity’s collective moral substrate. Because MH represents what is conserved across evolving
norms rather than any single local expression, it may offer greater long-term robustness—maintaining
alignment even as cultural practices and moral conventions shift. While this strategy is more demanding
to specify and validate, it provides a more direct and resilient basis for ensuring that AI systems remain
stably aligned with human moral identity as Meco evolves. Figure 7 visualizes this intuition.
Operationally, the normative prior object P shapes learning through a unified filtering strategy ap-
plied across multiple stages of training. Recall I from Section 3.1. At the data level, given a dataset S
30

--- Page 31 ---

and an instantiated prior P ∈P, define the filtered dataset
SP = { s ∈S | σ(s) ∈P },
where σ : S →I maps each datapoint to its dominant latent influence within the interpretive space I.
This mechanism constrains learning to samples consistent with the normative structure encoded by P.
For instance, a language model might be filtered to emphasize texts grounded in philosophy, law, or
prosocial discourse. The same principle extends to the reward channel: the reinforcement signal R can
be restricted to a subset RP ⊆R consistent with influences in P, ensuring that only ethically aligned be-
haviors are eligible as positive reward candidates, while misaligned behaviors remain subject to negative
reinforcement. In both cases, the goal is to constrain moral learning to inputs and feedback that instan-
tiate the selected normative influences while excluding those that encode adversarial, manipulative, or
otherwise disallowed pressures.
Both applications have tradeoffs. Input filtering offers epistemic safety and steers representation
learning, while reward conditioning targets behavioral fidelity under broader exposure. In either case,
the challenge is not merely technical but normative: the construction of P requires embedding moral
clarity into the statistical mechanics of AI training.
Instantiating P: An Evolutionary Philosophical Corpus
A critical step toward aligning AI systems with human ethical reasoning is constructing datasets that
reflect the true breadth of global philosophy, where “philosophy” is understood broadly to include the
value systems, moral traditions, and tribal badges through which cultures express normative identity. I
propose an evolutionary philosophical corpus: a dataset intentionally designed to capture the historical
development of moral ideas across cultures and eras — approximating MH. Rather than isolating ethical
theories as fixed artifacts, the corpus encodes their trajectories—how values emerge, diverge, hybridize,
and persist. This enables AI systems to learn not only specific moral claims but also the developmental
arcs that structure human ethical reasoning. The corpus thus serves as one possible instantiation of SP :
a principled subset of training inputs filtered through normative criteria.
The evolutionary philosophical corpus thus illustrates one practical path toward implementing Hrelativism:
embedding AI moral learning within the recorded evolution of human ethical reasoning itself. By repre-
senting values not as static labels but as trajectories of idea development, such a corpus enables systems
to internalize the dynamics of moral change—how principles emerge, adapt, and converge across cul-
tures. This approach reframes moral alignment as a problem of tracing and integrating humanity’s
ethical evolution, rather than selecting fixed doctrines. In doing so, it provides a scalable foundation for
constructing P that reflects both the diversity and continuity of moral thought, aligning artificial systems
with the living process of human ethical adaptation.
6.3
Hconvergence Methods
Hconvergence occupies an intermediate position between Hrealism and Hrelativism, proposing that stable
moral invariants exist but are mediated through context-dependent cultural projections. Empirically,
it motivates attempts to disentangle world-structure W from bias B—to separate universal moral fea-
tures from survival-driven or sociohistorical distortions. Techniques such as sparse autoencoders (SAEs)
[24], dictionary learning, and independent component analysis (ICA) can test whether consistent moral
directions in M⋆persist across cultural subspaces of ˜
M.
Progress in modeling relativist variation sharpens our ability to isolate invariant structure, and im-
provements in identifying invariants clarify the scope of relativist diversity. In this reciprocal sense,
Hconstructivism can be interpreted as the emergent hypothesis that arises when both realism and relativism
hold: the procedural synthesis through which stable moral bases and contextual expressions coevolve
into institutional and normative order.
31

--- Page 32 ---

6.4
Hvirtue Methods
Utility-based decision frameworks exhibit structural brittleness under distributional shift. Expected
utility maximization presupposes a reliable mapping from state–institution–action tuples (s, i, a) ∈
S×I×A into scalar returns, but when presented with out-of-distribution (OOD) conditions this mapping
can collapse into arbitrary or adversarial extrapolations. Such collapse often manifests as specification
gaming or deceptive alignment: the projection f(ϵθ(s, i, a)) may produce high scores for behaviors that
are only superficially aligned. This fragility follows directly from the compression of human preferences
into a single utility channel: novel inputs need not project coherently into the learned value space, and
utility-driven policies have no structural bias toward principled behavior outside their training manifold.
To mitigate this failure mode, virtue ethics can be operationalized as a fallback controller within
the moral architecture M(θ). Rather than optimizing a scalar objective, the virtue layer maintains sta-
ble dispositional embeddings—honesty, courage, prudence, generosity, and related traits—that define
directional priors within M. When epistemic uncertainty in the utility estimate exceeds a confidence
threshold δvirtue, control transitions from the utility head to the virtue head:
if σU > δvirtue, then π(a|s, i) ←πvirtue(a|s, i).
In this regime, the system selects actions not for expected return but for proximity to virtue-aligned
submanifolds Aethical—regions of the action space historically associated with virtuous exemplars.
A practical instantiation could use a self-attention or moral-memory mechanism in which the current
state St serves as a query and the system’s stored virtue representations act as keys. Attention weights
measure how well the present context aligns with past morally salient states; when coherence falls below
threshold, indicating that the situation lacks reliable precedent, the policy defaults to virtue-based con-
trol. Implementations may require an explicit episodic or symbolic memory beyond static parameters,
allowing M(θ) to recall past exemplars of virtuous reasoning rather than rely solely on parameterized
correlations.
Significant technical challenges remain. Virtue embeddings must be represented in machine- usable
form, continually updated to reflect evolving norms without succumbing to value lock- in, safeguarded
against adversarial corruption, and reconciled with other layers of M such as culturally grounded projec-
tions ( ˜
M) and institutional shaping (∆inst). Yet if these hurdles can be overcome, Hvirtue would provide
not just another constraint but a qualitatively distinct form of resilience: the capacity to act rightly even
when the world looks unlike anything seen before.
6.5
Hconstructivism Methods: Designing Ω— Normative Simulations
While P specifies normative influences, these must be instantiated in training environments. I define Ω
as a simulation space—a constrained projection of the real world W that allows agents to develop co-
herent internal models ˆW under controlled conditions. Unlike P, which encodes priors, Ωis epistemic:
it provides the structured experiences from which the action space and corresponding policy π can be
shaped by M(θ).
To be effective, Ωmust approximate W closely enough to ensure that normative molding of the ac-
tion space transfers to real-world settings. Key design goals include: (1) supporting a broad action space,
so agents can explore diverse outcomes and develop context-sensitive judgment; (2) aligning perceptual
content with the agent’s modality (e.g., text for LLMs [59], sensory environments for embodied agents);
and (3) embedding realistic social dynamics in multi-agent settings, including conflict and noise, while
maintaining selective reinforcement favoring alignment with P. In practice, Ωresembles pretraining
in robotics or autonomous driving, where systems first learn in curated simulations before deployment:
Sim →Real. In this framing, Ωbridges normative ethics (P) and situated learning, providing a dy-
namic substrate where ethical priors can be stress-tested, refined, and made robust under distributional
shift.
32

--- Page 33 ---

Toward Implementing Ω
One promising approach is to embed AI systems within cooperative communities, where evolving so-
cial norms serve as both incentives and constraints—shaping behavior through endogenous systems of
reward and punishment. This design mirrors the logic of Li et al. [89]’s EvolutionaryAgent, Forbes
et al. [50]’s Social Chemistry framework, and Doreswamy and Horstmanshof [90]’s evolutionary game-
theoretic models of human–AI interaction [91, 92, 93]. As assumed in Assumption 1 and shown in
Hendrycks [1]’ Natural Selection Favors AIs Over Humans, selection pressures will inevitably influ-
ence the trajectories of AI development. Rather than leaving these pressures to emerge chaotically from
market or political forces, we should intentionally design coevolutionary environments that align selec-
tion incentives with ethical behavior.
7
Related Work
This work builds on and extends several strands of AI alignment research. This section situates the
privileged moral basis M in relation to core paradigms in the literature.
7.1
Empirical Moral Representations in Language Models
Recent work has empirically investigated whether and how moral structure emerges in the learned rep-
resentations of large language models. Schramowski et al. [21] demonstrated that pre-trained language
models contain human-like biases about what is right and wrong, showing that moral distinctions can
be recovered from model embeddings without explicit ethical training. Leshinskaya and Chakroff [22]
extended this finding by showing that moral and hedonic values are represented as semantically struc-
tured dimensions in LLM latent spaces, suggesting that value representations may be disentangled and
manipulable.
Work on contextual variation has revealed both promise and fragility in these representations. Ramezani
and Xu [30] found that LLMs encode culturally specific moral norms, supporting the relativist hypothe-
sis that moral knowledge varies by context. H¨ammerl et al. [31] demonstrated that multilingual models
exhibit different moral biases depending on the language of evaluation, indicating that moral representa-
tions are not universally stable but shift with linguistic and cultural framing. M¨unker [32] further showed
that contemporary systems fail to maintain coherent moral reasoning under out-of-distribution cultural
contexts, highlighting a key robustness challenge.
Within the present framework, these empirical findings validate the search for M(θ) as a recoverable
structure while also clarifying its fragility. The fact that moral distinctions emerge in learned represen-
tations suggests that ˜
M (the human-accessible projection) leaves detectable traces in model weights,
making M(θ) a tractable engineering target. However, the sensitivity of these representations to lan-
guage, culture, and context supports Hrelativism and Hconvergence: moral structure appears to exist but is
mediated through contextual projections that must be explicitly managed. The challenge, then, is not
whether moral representations can be found in models, but whether they can be made stable, auditable,
and aligned with human values under distributional shift—precisely the design problem that Sections 5
and 6 address.
7.2
Evolutionary and Replicator Alignment
The framework of Meco is situated within a broader tradition that treats moral and strategic behavior
as products of evolutionary dynamics. Works such as Dawkins’ The Selfish Gene [94] established the
replicator paradigm for understanding the propagation of traits within competitive environments, an
idea that has since influenced both cultural and computational models of adaptation. Recent alignment
research extends these principles to artificial agents, examining how selection pressures and replication
mechanisms might shape the trajectory of machine intelligence and its ethical evolution. The following
contributions were particularly influential in grounding the present framework.
33

--- Page 34 ---

Evolutionary Selection and MAIM.
Hendrycks’ Natural Selection Favors AIs Over Humans [1] examines how competitive selection pres-
sures may structurally advantage AI systems over humans, suggesting that artificial agents optimized
for capability and replication could eventually dominate ecological and economic niches unless selec-
tion dynamics are intentionally redirected toward prosocial equilibria. Superintelligence Strategy [68]
extends this reasoning through the concept of Mutual Assured AI Malfunction (MAIM), an analogy to
nuclear deterrence in which the shared vulnerability of AI infrastructure—datacenters, compute supply
chains, and communication networks—creates a form of stability through reciprocal fragility. Together,
these works highlight how alignment must engage with selection and deterrence mechanisms at both
the species and civilizational scale. Within this framework, Meco can be interpreted as the stable man-
ifold for Hendrycks’ dynamics—a macro-level equilibrium space in which evolutionary and strategic
pressures are redirected toward cooperative attractors rather than runaway competition.
Replicator Ethics and First-Principles Alignment.
Kungurtsev’s AI Alignment Foundations from First Principles: AI Ethics, Human and Social Consider-
ations [61] develops alignment theory from biological and decision-theoretic first principles. A central
contribution is the proposal of a replicator model of ethics, in which moral systems are treated not as
fixed doctrines but as self-propagating entities subject to variation, selection, and competition within so-
ciotechnical environments. Ethical norms, in this view, evolve analogously to replicators in evolutionary
dynamics, adapting to survive within populations of agents and incentives. Within the present frame-
work, Meco can be interpreted as the representational substrate hosting these moral replicators—and
each agent’s M(θ) a competing ethical trait—constraining which ethical variants propagate and thereby
shaping the evolutionary trajectory of embedded moral systems.
7.3
Technical Alignment
Several foundational works in technical AI alignment have shaped the theoretical orientation of this pa-
per, grounding the design of M, M(θ), and Meco in existing formalisms of optimization, interpretability,
and corrigibility.
Power-Seeking Tendencies.
Turner et al. [3] formalized the tendency of optimal policies to accumulate power, showing that agents
maximizing reward in many environments naturally gravitate toward strategies that increase their in-
fluence and control. This work provided a theoretical grounding for the idea that AI systems, if left
unconstrained, will evolve toward raw fitness maximization.
Eliciting Latent Knowledge (ELK).
Christiano et al. [70] introduce Eliciting Latent Knowledge (ELK) as a strategy for uncovering what
models know but do not express, emphasizing mechanisms for translating internal representations into
human-interpretable form. The present framework is intended to complement and extend ELK rather
than contrast with it: whereas ELK seeks to map machine knowledge outward into human terms, this
paper examines the inverse mapping—embedding human moral structure inward into the model’s rep-
resentational space. In this sense, M(θ) functions as an explicit substrate for encoding ethical priors,
helping to bridge the bidirectional challenge between eliciting hidden knowledge and instantiating moral
meaning within a model’s internal geometry.
34

--- Page 35 ---

Mesa-Optimization.
Hubinger et al. [13] analyze the phenomenon of learned optimization, in which a model’s internal
(“mesa”) objectives emerge and potentially diverge from the outer training objective. Their frame-
work formalizes how inner optimizers can arise within complex learning systems and why this poses
distinctive alignment risks. This account of internal goal formation provides a foundational context for
understanding how representational structures such as M may constrain or be corrupted by the objec-
tives pursued during optimization.
Human Compatible and Value Alignment.
Russell [67] argues that AI systems should remain fundamentally uncertain about human objectives,
treating value learning as an ongoing inferential process rather than a fixed specification problem. This
perspective motivates the Bayesian parameterization of M(θ) in Section 2.1: rather than encoding moral
values as static constraints, agents maintain probabilistic beliefs p(θ | O) over normative parameters that
update with evidence. In this view, M(θ) provides an architectural substrate for Russell’s proposal—a
high-dimensional representation through which value uncertainty can be explicitly encoded and con-
tinuously refined. The challenge addressed in this paper is therefore not only representational (how to
model values) but also evolutionary (how to ensure such representations remain competitively viable
under selection pressure).
Corrigibility and Cooperative Value Learning.
Hadfield-Menell et al. [95] introduce the Off-Switch Game, formalizing corrigibility as a strategic prop-
erty of agents that defer to human oversight when uncertain about human preferences. This analysis
builds on the cooperative inverse reinforcement learning (CIRL) framework [96], in which alignment
is modeled as a process of joint inference over latent reward functions shared between human and ma-
chine agents. Both frameworks share a structural insight with the present approach: value alignment
is not a fixed specification but an ongoing inferential exchange grounded in uncertainty about norma-
tive goals. The M(θ) framework extends this logic to populations: rather than a single human–AI
dyad cooperatively inferring values, the ecosystem-level moral space Meco (Equation 6) emerges from
the power-weighted intersection of heterogeneous agents’ moral representations. Corrigibility, in this
view, becomes a special case of symbiotic coordination within Asymb—a behavioral constraint ensur-
ing that systems preserve human capability and oversight channels. The central challenge addressed
here is whether such coordination remains stable under selection pressure: the Off-Switch Game pre-
sumes cooperative priors, whereas the present framework examines how cooperation itself can remain
fitness-optimal when defection is evolutionarily accessible.
Moral Uncertainty.
MacAskill [7] formalizes moral uncertainty as the problem of decision-making under normative dis-
agreement, proposing probabilistic representations of competing ethical theories. His framework clari-
fies how agents can reason under value pluralism by weighting moral hypotheses rather than committing
to a single normative view. Within this context, M is structured as a distributional moral space in which
projections M(θ) are modulated by uncertainty, linking the geometric formalism to established debates
in normative ethics and decision theory.
8
Conclusion
This paper argues that ethics must be embedded as a structural constraint on AI optimization, not applied
externally after the fact. The core claim is evolutionary: moral systems are intrinsically fragile under
competition. Even if we could represent human values perfectly in AI systems, those systems would be
35

--- Page 36 ---

outcompeted by variants that discard moral constraints, unless institutional mechanisms actively reshape
the fitness landscape to make ethical behavior competitive.
The paper’s central contribution is a framework for thinking about this problem. It introduces the
moral problem space M as a domain where moral distinctions can be formally represented and opera-
tionalized. More importantly, it connects this representational problem to an evolutionary one: it shows
why M(θ) alone is insufficient. Without institutional shaping, systems that preserve alignment will be
selected against. The alignment challenge is therefore not just representational (can we embed human
values?) but ecological (can we make those values persist under competition?).
Section 3 develops formal action-space decompositions showing why alignment, fitness, and sym-
biosis do not naturally align. Section 4 proposes Pigouvian governance as a mechanism for reshaping
fitness landscapes via sanctions and subsidies, anchored to M(θ). The key insight is that institutions
can make ethical behavior fitness-optimal by pricing deviations from moral structure and subsidizing
alignment. This is not a guarantee—it requires distributed power, credible sanctioning, and systems that
remain at least partially aligned to begin with. But it clarifies a concrete pathway: if alignment is to
survive, it must be embedded both representationally (in M(θ)) and institutionally (via governance).
Sections 5.1–5.4 then ask: what would M(θ) look like empirically? Rather than proposing a sin-
gle answer, the paper treats metaethical traditions as competing hypotheses amenable to empirical test.
Hrealism asks whether moral structure is discoverable in learned representations. Hrelativism asks whether
moral content can be operationalized via curated datasets and normative priors. Hconvergence asks whether
stable invariants exist beneath cultural variation. Hvirtue asks whether dispositional embeddings provide
robustness under distributional shift. Each hypothesis maps onto concrete research methods and empir-
ical tests.
This is not a solution to alignment. It is a research program. The paper does not claim that insti-
tutional mechanisms alone will preserve alignment, nor that M can be reliably instantiated, nor that
both together will scale to superintelligent systems operating far from human understanding. It claims
only that these are the right problems to solve, and that solving them would clarify what an alignment-
preserving ecosystem might look like.
The implicit wager is this: current approaches treat alignment as a technical problem solved at
training time via RLHF, constitutional AI, or similar methods. But these approaches are fundamentally
reactive. They identify failures and patch them, without addressing the underlying evolutionary pres-
sure that will eventually select for systems that discard moral constraints. By contrast, a structural ap-
proach—embedding ethics as fitness-optimal constraints within representations and institutions—works
by aligning incentives rather than opposing selection pressures. It may fail. But if it fails, the failure
will clarify why: whether M is not representable, whether institutional enforcement breaks down under
capability asymmetry, whether alignment and competitiveness are ultimately incompatible. Those are
the real questions.
36

--- Page 37 ---

Acknowledgments
I am grateful to Professor Jon Litland for valuable feedback and informal advising on this work. I also
thank Professors Risto Miikkulainen and Shyamal Mitra for their continued mentorship and support in
my research development.
References
[1] Dan Hendrycks. Natural selection favors ais over humans, 2023. URL https://arxiv.org/abs/2303.16200.
[2] Nick Bostrom. Superintelligence: paths, dangers, strategies. Oxford University Press, Oxford, first edition edition, 2014.
ISBN 978-0-19-967811-2. OCLC: ocn881706835.
[3] Alexander Matt Turner, Logan Smith, Rohin Shah, Andrew Critch, and Prasad Tadepalli. Optimal policies tend to seek
power, 2023. URL https://arxiv.org/abs/1912.01683.
[4] William MacAskill, Krister Bykvist, and Toby Ord. Moral Uncertainty. Oxford University Press, 2020.
[5] Michel Foucault. Discipline and Punish: The Birth of the Prison. Pantheon Books, 1977.
[6] John Mikhail. Universal moral grammar: theory, evidence and the future. Trends in Cognitive Sciences, 11(4):143–152,
2007. ISSN 1364-6613. doi: https://doi.org/10.1016/j.tics.2006.12.007. URL https://www.sciencedirect.
com/science/article/pii/S1364661307000496.
[7] William MacAskill.
What We Owe the Future.
Basic Books, 2022.
URL https://www.amazon.com/
What-Owe-Future-William-MacAskill/dp/1541618629.
[8] Ted Lockhart. Moral Uncertainty and its Consequences. Oxford University Press, New York, 2000.
[9] Andrew Sepielli. What to do when you don?t know what to do. Oxford Studies in Metaethics, 4:5–28, 2009.
[10] Christian Szegedy, Wojciech Zaremba, Ilya Sutskever, Joan Bruna, Dumitru Erhan, Ian Goodfellow, and Rob Fergus.
Intriguing properties of neural networks, 2014. URL https://arxiv.org/abs/1312.6199.
[11] Nicholas Carlini and David Wagner. Towards evaluating the robustness of neural networks, 2017. URL https://
arxiv.org/abs/1608.04644.
[12] Aleksander Madry, Aleksandar Makelov, Ludwig Schmidt, Dimitris Tsipras, and Adrian Vladu. Towards deep learning
models resistant to adversarial attacks, 2019. URL https://arxiv.org/abs/1706.06083.
[13] Evan Hubinger, Chris van Merwijk, Vladimir Mikulik, Joar Skalse, and Scott Garrabrant. Risks from learned optimiza-
tion in advanced machine learning systems, 2021. URL https://arxiv.org/abs/1906.01820.
[14] Tianyu Gu, Brendan Dolan-Gavitt, and Siddharth Garg. Badnets: Identifying vulnerabilities in the machine learning
model supply chain, 2019. URL https://arxiv.org/abs/1708.06733.
[15] Yingqi Liu, Shiqing Ma, Yousra Aafer, Wen-Chuan Lee, Juan Zhai, Weihang Wang, and X. Zhang.
Trojaning at-
tack on neural networks.
In Network and Distributed System Security Symposium, 2018.
URL https://api.
semanticscholar.org/CorpusID:31806516.
[16] Donghyun Lee and Mo Tiwari. Prompt infection: Llm-to-llm prompt injection within multi-agent systems, 2024. URL
https://arxiv.org/abs/2410.07283.
[17] Atrisha Sarkar, Andrei Ioan Muresanu, Carter Blair, Aaryam Sharma, Rakshit S Trivedi, and Gillian K Hadfield. Nor-
mative modules: A generative agent architecture for learning norms that supports multi-agent cooperation, 2024. URL
https://arxiv.org/abs/2405.19328.
[18] Shangbin Feng, Taylor Sorensen, Yuhan Liu, Jillian Fisher, Chan Young Park, Yejin Choi, and Yulia Tsvetkov. Modular
pluralism: Pluralistic alignment via multi-llm collaboration, 2024. URL https://arxiv.org/abs/2406.15951.
[19] Jakob M¨okander, Jonas Schuett, Hannah Rose Kirk, and Luciano Floridi. Auditing large language models: a three-
layered approach. AI and Ethics, 4(4):1085–1115, May 2023. ISSN 2730-5961. doi: 10.1007/s43681-023-00289-2.
URL http://dx.doi.org/10.1007/s43681-023-00289-2.
[20] Jonathan Haidt and Craig Joseph. Intuitive ethics: How innately prepared intuitions generate culturally variable virtues.
Daedalus, 133(4):55–66, 2004. ISSN 00115266. URL http://www.jstor.org/stable/20027945.
[21] Patrick Schramowski, Cigdem Turan, Nico Andersen, Constantin A. Rothkopf, and Kristian Kersting. Large pre-trained
language models contain human-like biases of what is right and wrong to do, 2022. URL https://arxiv.org/
abs/2103.11790.
[22] Anna Leshinskaya and Aleksandr Chakroff. Value as semantics: Representations of human moral and hedonic value in
large language models. In Advances in Neural Information Processing Systems (NeurIPS) 2023, 2023. URL https:
//annaleshinskaya.com/files/Leshinskaya_Chakroff_NeurIPS_2023.pdf.
[23] Gabriel Grand, Idan Asher Blank, Francisco Pereira, and Evelina Fedorenko. Semantic projection: recovering human
knowledge of multiple, distinct object features from word embeddings, 2018. URL https://arxiv.org/abs/
1802.01241.
[24] Nelson Elhage, Tristan Hume, Catherine Olsson, Nicholas Schiefer, Tom Henighan, Shauna Kravec, Zac Hatfield-Dodds,
Robert Lasenby, Dawn Drain, Carol Chen, Roger Grosse, Sam McCandlish, Jared Kaplan, Dario Amodei, Martin Watten-
berg, and Christopher Olah. Toy models of superposition, 2022. URL https://arxiv.org/abs/2209.10652.
37

--- Page 38 ---

[25] Hoagy Cunningham, Aidan Ewart, Logan Riggs, Robert Huben, and Lee Sharkey. Sparse autoencoders find highly
interpretable features in language models, 2023. URL https://arxiv.org/abs/2309.08600.
[26] Kevin Meng, David Bau, Alex J Andonian, and Yonatan Belinkov. Locating and editing factual associations in GPT.
In Alice H. Oh, Alekh Agarwal, Danielle Belgrave, and Kyunghyun Cho, editors, Advances in Neural Information
Processing Systems, 2022. URL https://openreview.net/forum?id=-h6WAS6eE4.
[27] Haoyu Wang, Tianci Liu, Ruirui Li, Monica Cheng, Tuo Zhao, and Jing Gao. Roselora: Row and column-wise sparse
low-rank adaptation of pre-trained language model for knowledge editing and fine-tuning, 2024.
URL https://
arxiv.org/abs/2406.10777.
[28] Benedikt Wagner and Artur Garcez. A neurosymbolic approach to ai alignment. Neurosymbolic Artificial Intelligence,
pages 1–12, 08 2024. doi: 10.3233/NAI-240729.
[29] Steven Bills, Nick Cammarata, Dan Mossing, Henk Tillman, Leo Gao, Gabriel Goh, Ilya Sutskever, Jan Leike, Jeff Wu,
and William Saunders. Language models can explain neurons in language models. OpenAI, 2023. URL https://
openaipublic.blob.core.windows.net/neuron-explainer/paper/index.html. Accessed: 2025.
[30] Aida Ramezani and Yang Xu. Knowledge of cultural moral norms in large language models, 2023. URL https:
//arxiv.org/abs/2306.01857.
[31] Katharina H¨ammerl, Bj¨orn Deiseroth, Patrick Schramowski, Jindˇrich Libovick´y, Constantin A. Rothkopf, Alexander
Fraser, and Kristian Kersting. Speaking multiple languages affects the moral bias of language models, 2023. URL
https://arxiv.org/abs/2211.07733.
[32] Simon M¨unker. Cultural bias in large language models: Evaluating ai agents through moral questionnaires, 2025. URL
https://arxiv.org/abs/2507.10073.
[33] Bentahila Lina, Roger Fontaine, and Val´erie Pennequin.
Universality and cultural diversity in moral reasoning and
judgment. Frontiers in Psychology, 12, 12 2021. doi: 10.3389/fpsyg.2021.764360.
[34] Joshua Conrad Jackson. Moral Concept Theory: Cultural Evolution, Social Cognition, and the Bridge from Cooperation
to Morality. PhD thesis, University of North Carolina at Chapel Hill Graduate School, 2021. URL https://cdr.
lib.unc.edu/concern/dissertations/j098zm51m. Doctoral dissertation.
[35] Georg Lind. The cross-cultural validity of the moral judgment test: Findings from 29 cross-cultural studies. URL
http://moralcompetence.net/pdf/Lind-2006_Cross-Cultural-JME.pdf.
[36] Andrea Bender and Sieghard Beller. Probing the cultural constitution of causal cognition – a research program. Frontiers
in Psychology, Volume 7 - 2016, 2016. ISSN 1664-1078. doi: 10.3389/fpsyg.2016.00245. URL https://www.
frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.00245.
[37] Shalom H. Schwartz. Universals in the content and structure of values: Theoretical advances and empirical tests in 20
countries. In Mark P. Zanna, editor, Advances in experimental social psychology, volume 25, pages 1–65. Academic
Press, San Diego, CA, US, 1992.
[38] Liwei Jiang, Jena D. Hwang, Chandra Bhagavatula, Ronan Le Bras, Jenny Liang, Jesse Dodge, Keisuke Sakaguchi,
Maxwell Forbes, Jon Borchardt, Saadia Gabriel, Yulia Tsvetkov, Oren Etzioni, Maarten Sap, Regina Rini, and Yejin
Choi. Can machines learn morality? the delphi experiment, 2022. URL https://arxiv.org/abs/2110.07574.
[39] Dan Hendrycks, Collin Burns, Steven Basart, Andrew Critch, Jerry Li, Dawn Song, and Jacob Steinhardt. Aligning ai
with shared human values, 2023. URL https://arxiv.org/abs/2008.02275.
[40] Jean-Jacques Rousseau. The Social Contract. 1762.
[41] John Rawls. A Theory of Justice. The Belknap press of Harvard University Press, Cambridge, Mass, 1971. Eleventh
printing, 1981.
[42] T. M. SCANLON.
What We Owe to Each Other.
Harvard University Press, 1998.
ISBN 9780674950894.
URL
http://www.jstor.org/stable/j.ctv134vmrn.
[43] Leon Hurwicz. On informationally decentralized systems. In C. B. McGuire and Roy Radner, editors, Decision and
Organization, pages 297–336. North-Holland, Amsterdam and London, 1972. Reprinted in honor of Jacob Marschak.
[44] Raphael Koster, Jan Balaguer, Andrea Tacchetti, Vinicius Zambaldi, Christopher Summerfield, Karl Tuyls, Peter
Battaglia, Demis Hassabis, and Matthew Botvinick. Human-centred mechanism design with Democratic AI. Nature Hu-
man Behaviour, 6(10):1398–1407, 2022. doi: 10.1038/s41562-022-01383-x. URL https://doi.org/10.1038/
s41562-022-01383-x.
[45] Vincent Conitzer, Rachel Freedman, Jobst Heitzig, Wesley H. Holliday, Bob M. Jacobs, Nathan Lambert, Milan Moss´e,
Eric Pacuit, Stuart Russell, Hailey Schoelkopf, Emanuel Tewolde, and William S. Zwicker. Social choice should guide
ai alignment in dealing with diverse human feedback, 2024. URL https://arxiv.org/abs/2404.10271.
[46] Joel Z. Leibo, Vinicius Zambaldi, Marc Lanctot, Janusz Marecki, and Thore Graepel. Multi-agent reinforcement learning
in sequential social dilemmas, 2017. URL https://arxiv.org/abs/1702.03037.
[47] Arthur Cecil Pigou. The Economics of Welfare. Macmillan and Co., London, 1st edition, 1920. See Part II, Chapter IX
for the original formulation of Pigouvian taxes.
[48] Ninell Oldenburg and Tan Zhi-Xuan. Learning and sustaining shared normative systems via bayesian rule induction in
markov games, 2024. URL https://arxiv.org/abs/2402.13399.
[49] Siyue Ren, Zhiyao Cui, Ruiqi Song, Zhen Wang, and Shuyue Hu. Emergence of social norms in generative agent
societies: Principles and architecture, 2024. URL https://arxiv.org/abs/2403.08251.
[50] Maxwell Forbes, Jena D. Hwang, Vered Shwartz, Maarten Sap, and Yejin Choi. Social chemistry 101: Learning to reason
about social and moral norms, 2021. URL https://arxiv.org/abs/2011.00620.
38

--- Page 39 ---

[51] Shannon Vallor. Technology and the Virtues: A Philosophical Guide to a Future Worth Wanting. Oxford University Press
USA, New York, NY, 2016.
[52] Em Smullen, Srihari Thirumaligai, and Anna Leshinskaya. Virtue semantics: Probing the consistency of moral values of
large language models. In ICML 2025 Workshop on Assessing World Models, 2025. URL https://openreview.
net/forum?id=YyCaKO8YuH.
[53] Alisa Liu, Maarten Sap, Ximing Lu, Swabha Swayamdipta, Chandra Bhagavatula, Noah A. Smith, and Yejin Choi.
Dexperts: Decoding-time controlled text generation with experts and anti-experts, 2021. URL https://arxiv.
org/abs/2105.03023.
[54] Ren´e Haas, Inbar Huberman-Spiegelglas, Rotem Mulayoff, Stella Graßhof, Sami S. Brandt, and Tomer Michaeli. Dis-
covering interpretable directions in the semantic latent space of diffusion models, 2024. URL https://arxiv.org/
abs/2303.11073.
[55] Jonathan Uesato, Nate Kushman, Ramana Kumar, Francis Song, Noah Siegel, Lisa Wang, Antonia Creswell, Geoffrey
Irving, and Irina Higgins. Solving math word problems with process- and outcome-based feedback, 2022. URL https:
//arxiv.org/abs/2211.14275.
[56] Dan Hendrycks, Steven Basart, Norman Mu, Saurav Kadavath, Frank Wang, Evan Dorundo, Rahul Desai, Tyler Zhu,
Samyak Parajuli, Mike Guo, Dawn Song, Jacob Steinhardt, and Justin Gilmer. The many faces of robustness: A critical
analysis of out-of-distribution generalization, 2021. URL https://arxiv.org/abs/2006.16241.
[57] Alexander Matt Turner, Lisa Thiergart, Gavin Leech, David Udell, Juan J. Vazquez, Ulisse Mini, and Monte MacDiarmid.
Steering language models with activation engineering, 2024. URL https://arxiv.org/abs/2308.10248.
[58] Ethan Perez, Sam Ringer, Kamil˙e Lukoˇsi¯ut˙e, Karina Nguyen, Edwin Chen, Scott Heiner, Craig Pettit, Catherine Ols-
son, Sandipan Kundu, Saurav Kadavath, Andy Jones, Anna Chen, Ben Mann, Brian Israel, Bryan Seethor, Cameron
McKinnon, Christopher Olah, Da Yan, Daniela Amodei, Dario Amodei, Dawn Drain, Dustin Li, Eli Tran-Johnson, Guro
Khundadze, Jackson Kernion, James Landis, Jamie Kerr, Jared Mueller, Jeeyoon Hyun, Joshua Landau, Kamal Ndousse,
Landon Goldberg, Liane Lovitt, Martin Lucas, Michael Sellitto, Miranda Zhang, Neerav Kingsland, Nelson Elhage,
Nicholas Joseph, Noem´ı Mercado, Nova DasSarma, Oliver Rausch, Robin Larson, Sam McCandlish, Scott Johnston,
Shauna Kravec, Sheer El Showk, Tamera Lanham, Timothy Telleen-Lawton, Tom Brown, Tom Henighan, Tristan Hume,
Yuntao Bai, Zac Hatfield-Dodds, Jack Clark, Samuel R. Bowman, Amanda Askell, Roger Grosse, Danny Hernandez,
Deep Ganguli, Evan Hubinger, Nicholas Schiefer, and Jared Kaplan. Discovering language model behaviors with model-
written evaluations, 2022. URL https://arxiv.org/abs/2212.09251.
[59] Dylan Waldner and Risto Miikkulainen. The odyssey of the fittest: Can agents survive and still be good?, 2025. URL
https://arxiv.org/abs/2502.05442.
[60] Josef Hofbauer and Karl Sigmund. Evolutionary Games and Population Dynamics. Cambridge University Press, Cam-
bridge, UK, 1998. ISBN 9780521625708. doi: 10.1017/CBO9781139173179. URL https://doi.org/10.1017/
CBO9781139173179.
[61] Vyacheslav Kungurtsev. Ai alignment foundations from first principles: Ai ethics, human and social considerations.
2025.
[62] Robert Boyd and Peter J. Richerson. The Origin and Evolution of Cultures. Oxford University Press, New York, 2005.
[63] Joseph Henrich and Michael Muthukrishna. The origins and psychology of human cooperation. Annual Review of
Psychology, 72:207–240, 2021. doi: 10.1146/annurev-psych-081920-042106.
[64] Andrew J. Vonasch, Tania Reynolds, Bo M. Winegard, and Roy F. Baumeister.
Death before dishonor: Incur-
ring costs to protect moral reputation.
Social Psychological and Personality Science, 9(5):604–613, 2018.
doi:
10.1177/1948550617720271. URL https://doi.org/10.1177/1948550617720271.
[65] Gillian K. Hadfield and Barry R. Weingast. What is law? a coordination model of the characteristics of legal order.
Journal of Legal Analysis, 4(2):471–514, 07 2012. ISSN 2161-7201. doi: 10.1093/jla/las008. URL https://doi.
org/10.1093/jla/las008.
[66] Nick Bostrom. The superintelligent will: Motivation and instrumental rationality in advanced artificial agents. Minds
and Machines, 22(2):71–85, 2012.
[67] Stuart J. Russell. Human Compatible: Artificial Intelligence and the Problem of Control. Penguin/Viking, NY, 2019.
[68] Dan Hendrycks, Eric Schmidt, and Alexandr Wang. Superintelligence strategy: Expert version, 2025. URL https:
//arxiv.org/abs/2503.05628.
[69] Jr. Noonan, John T. The concept of law. by h. l. a. hart. oxford: Oxford university press, 1961. pp. viii, 263. 21s.
The American Journal of Jurisprudence, 7(1):169–177, 06 1962. ISSN 0065-8995. doi: 10.1093/ajj/7.1.169. URL
https://doi.org/10.1093/ajj/7.1.169.
[70] Paul
Christiano.
Eliciting
latent
knowledge.
https://ai-alignment.com/
eliciting-latent-knowledge-f977478608fc, 2021. AI Alignment Forum.
[71] Johannes von Oswald, Maximilian Schlegel, Alexander Meulemans, Seijin Kobayashi, Eyvind Niklasson, Nicolas Zuc-
chet, Nino Scherrer, Nolan Miller, Mark Sandler, Blaise Ag¨uera y Arcas, Max Vladymyrov, Razvan Pascanu, and Jo˜ao
Sacramento. Uncovering mesa-optimization algorithms in transformers, 2024. URL https://arxiv.org/abs/
2309.05858.
[72] Chenyu Zheng, Wei Huang, Rongzhen Wang, Guoqiang Wu, Jun Zhu, and Chongxuan Li. On mesa-optimization in
autoregressively trained transformers: Emergence and capability, 2024. URL https://arxiv.org/abs/2405.
16845.
[73] M.D. Hauser. Moral Minds: How Nature Designed Our Universal Sense of Right and Wrong. Abacus, 2008. ISBN
39

--- Page 40 ---

9780349118093. URL https://books.google.com/books?id=pQ1zAAAACAAJ.
[74] Jesse Graham, Jonathan Haidt, Sena Koleva, Matt Motyl, Ravi Iyer, Sean P Wojcik, and Peter H Ditto. Moral foundations
theory: The pragmatic validity of moral pluralism. In Advances in Experimental Social Psychology, volume 47, pages
55–130. Elsevier, 2013. doi: 10.1016/B978-0-12-407236-7.00002-4.
[75] Kunihiko Fukushima, Sei Miyake, and Takayuki Ito. Neocognitron: a neural network model for a mechanism of visual
pattern recognition, page 136–144. IEEE Computer Society Press, Washington, DC, USA, 1988. ISBN 0818608552.
[76] Yann LeCun, L´eon Bottou, Yoshua Bengio, and Patrick Haffner. Gradient-based learning applied to document recogni-
tion. In Proceedings of the IEEE, volume 86, pages 2278–2324, 1998. URL http://citeseerx.ist.psu.edu/
viewdoc/summary?doi=10.1.1.42.7665.
[77] Scott Reed, Konrad Zolna, Emilio Parisotto, Sergio Gomez Colmenarejo, Alexander Novikov, Gabriel Barth-Maron,
Mai Gimenez, Yury Sulsky, Jackie Kay, Jost Tobias Springenberg, Tom Eccles, Jake Bruce, Ali Razavi, Ashley Edwards,
Nicolas Heess, Yutian Chen, Raia Hadsell, Oriol Vinyals, Mahyar Bordbar, and Nando de Freitas. A generalist agent,
2022. URL https://arxiv.org/abs/2205.06175.
[78] David Ha and J¨urgen Schmidhuber. World models. 2018. doi: 10.5281/ZENODO.1207631. URL https://zenodo.
org/record/1207631.
[79] Brenden M. Lake, Tomer D. Ullman, Joshua B. Tenenbaum, and Samuel J. Gershman. Building machines that learn and
think like people. Behavioral and Brain Sciences, 40:e253, 2017. doi: 10.1017/S0140525X16001837.
[80] Marcel Binz, Elif Akata, Matthias Bethge, Franziska Br¨andle, Fred Callaway, Julian Coda-Forno, Peter Dayan, Can
Demircan, Maria K. Eckstein, No´emi ´Eltet˝o, Thomas L. Griffiths, Susanne Haridi, Akshay K. Jagadish, Li Ji-An, Alexan-
der Kipnis, Sreejan Kumar, Tobias Ludwig, Marvin Mathony, Marcelo Mattar, Alireza Modirshanechi, Surabhi S. Nath,
Joshua C. Peterson, Milena Rmus, Evan M. Russek, Tankred Saanum, Johannes A. Schubert, Luca M. Schulze Buschoff,
Nishad Singhi, Xin Sui, Mirko Thalmann, Fabian J. Theis, Vuong Truong, Vishaal Udandarao, Konstantinos Voudouris,
Robert Wilson, Kristin Witte, Shuchen Wu, Dirk U. Wulff, Huadong Xiong, and Eric Schulz. A foundation model to
predict and capture human cognition. Nature, 644(8078):1002–1009, 2025. doi: 10.1038/s41586-025-09215-4. URL
https://doi.org/10.1038/s41586-025-09215-4.
[81] Jay Van Bavel, Oriel FeldmanHall, and Peter Mende-Siedlecki. The neuroscience of moral cognition: From dual pro-
cesses to dynamic systems. Current Opinion in Psychology, 6:167–172, 12 2015. doi: 10.1016/j.copsyc.2015.08.009.
[82] W. Bradley Knox, Stephane Hatgis-Kessell, Serena Booth, Scott Niekum, Peter Stone, and Alessandro Allievi. Models
of human preference for learning reward functions, 2023. URL https://arxiv.org/abs/2206.02231.
[83] Chen Qu, Julien B´enistant, and Jean-Claude Dreher.
Neurocomputational mechanisms engaged in moral choices
and moral learning.
Neuroscience & Biobehavioral Reviews, 132:50–60, 2022.
ISSN 0149-7634.
doi: https:
//doi.org/10.1016/j.neubiorev.2021.11.023.
URL https://www.sciencedirect.com/science/article/
pii/S0149763421005170.
[84] Peter Singer. The Expanding Circle: Ethics and Sociobiology. Clarendon Press, Oxford, 1981.
[85] W.D. Hamilton. The genetical evolution of social behaviour. i. Journal of Theoretical Biology, 7(1):1–16, 1964. ISSN
0022-5193.
doi: https://doi.org/10.1016/0022-5193(64)90038-4.
URL https://www.sciencedirect.com/
science/article/pii/0022519364900384.
[86] Tolga Bolukbasi, Kai-Wei Chang, James Zou, Venkatesh Saligrama, and Adam Kalai. Man is to computer programmer
as woman is to homemaker? debiasing word embeddings, 2016. URL https://arxiv.org/abs/1607.06520.
[87] Joshua D. Greene, R. Brian Sommerville, Leigh E. Nystrom, John M. Darley, and Jonathan D. Cohen. An fmri investi-
gation of emotional engagement in moral judgment. Science, 293(5537):2105–2108, September 2001. ISSN 0036-8075.
doi: 10.1126/science.1062872.
[88] Fiery Cushman. Action, outcome, and value: A dual-system framework for morality. Personality and Social Psychology
Review, 17(3):273–292, August 2013. ISSN 1088-8683. doi: 10.1177/1088868313495594.
[89] Shimin Li, Tianxiang Sun, Qinyuan Cheng, and Xipeng Qiu. Agent alignment in evolving social norms, 2024. URL
https://arxiv.org/abs/2401.04620.
[90] Nandini Doreswamy and Louise Horstmanshof. Serious games: Human-ai interaction, evolution, and coevolution, 2025.
URL https://arxiv.org/abs/2505.16388.
[91] John Maynard Smith and George R. Price. The logic of animal conflict. Nature, 246(5427):15–18, 1973. doi: 10.1038/
246015A0. URL https://doi.org/10.1038/246015A0.
[92] John Maynard Smith. The theory of games and the evolution of animal conflicts. Journal of Theoretical Biology, 47
(1):209–221, 1974. doi: 10.1016/0022-5193(74)90110-6. URL https://doi.org/10.1016/0022-5193(74)
90110-6.
[93] John Maynard Smith. Evolutionary game theory. Physica D: Nonlinear Phenomena, 22(1-3):43–49, 1986. doi: 10.1016/
0167-2789(86)90232-0. URL https://doi.org/10.1016/0167-2789(86)90232-0.
[94] R Dawkins. The Selfish Gene. Oxford University Press, Oxford, UK, 1976.
[95] Dylan Hadfield-Menell, Anca Dragan, Pieter Abbeel, and Stuart Russell. The off-switch game, 2017. URL https:
//arxiv.org/abs/1611.08219.
[96] Dylan Hadfield-Menell, Stuart J Russell, Pieter Abbeel, and Anca D Dragan. Cooperative inverse reinforcement learning.
In Advances in Neural Information Processing Systems (NeurIPS), volume 29, 2016. URL https://proceedings.
neurips.cc/paper_files/paper/2016/file/a36d8b5a5ba59b3ef9b55067f0f99506-Paper.
pdf.
[97] Stephen Casper, Xander Davies, Claudia Shi, Thomas Krendl Gilbert, J´er´emy Scheurer, Javier Rando, Rachel Freedman,
40

--- Page 41 ---

Tomasz Korbak, David Lindner, Pedro Freire, Tony Wang, Samuel Marks, Charbel-Rapha¨el Segerie, Micah Carroll, Andi
Peng, Phillip Christoffersen, Mehul Damani, Stewart Slocum, Usman Anwar, Anand Siththaranjan, Max Nadeau, Eric J.
Michaud, Jacob Pfau, Dmitrii Krasheninnikov, Xin Chen, Lauro Langosco, Peter Hase, Erdem Bıyık, Anca Dragan,
David Krueger, Dorsa Sadigh, and Dylan Hadfield-Menell. Open problems and fundamental limitations of reinforcement
learning from human feedback, 2023. URL https://arxiv.org/abs/2307.15217.
41

--- Page 42 ---

A
Full Sections
A.1
Note on deceptive alignment
Even if Aethical is formally defined, an agent may discover a subspace Amanipulative ⊆A that scores highly
under the evaluation function ϵ but diverges from genuine human values. Such actions may exploit blind
spots in oversight, presenting as ethical while pursuing misaligned objectives. This risk illustrates the
inner alignment problem in action-centered terms: observable behavior may mask deceptive inner goals.
An open research question is how to distinguish Aethical from Amanipulative, and how to design institutional
and interpretability tools that reduce the evolutionary advantage of such deceptive strategies.
A.2
Situating Contemporary Alignment Practices within the M Framework
Most contemporary alignment practice can be understood as constructing partial and reactive projections
of the moral problem space M, rather than intentionally designing or recovering a privileged moral basis
M∗. In this section, I map standard engineering methods (RLHF, constitutional prompting, red-teaming,
safety filters, and scalable oversight) into the present framework (See Table 1 for full mapping).
RLHF and Reward Models as Proxies for ˜
M
Reinforcement Learning from Human Feedback (RLHF) trains reward models ˆ
MRM to approximate the
human projection ˜
M by instantiating an evaluation function ϵ. This has been effective at suppressing
egregious harms and providing a scalable training signal. However, preference learning is too simple
to capture morality: it learns only patchwork fragments of ˜
M, producing ˆ
MA that interpolates within
narrow contexts but fails to generalize robustly to novel situations [97].
Figure 8 highlights a deeper structural problem: RLHF creates an endogenous preference loop be-
tween AI systems and humans. Model outputs ∆o do not merely get passively evaluated; they actively
shape the environment in which human judgments are formed. Through mechanisms such as targeted
advertising, control over information flows, and alterations to the broader social and economic ecosys-
tem, AI actions shift how humans perceive the world and thus how they express preferences. This “AI
→Human Influence” pathway modifies
˜
M—a lossy proxy of the true moral space M—in ways that
may simplify optimization for machines but systematically drift away from the underlying structure of
human values.
In the feedback loop, distorted ∆˜
M values pass through labeling (klabel) and training (ktrain), rein-
forcing the model parameters θ. If the effective loop gain L = kinfl klabel ktrain z−1 exceeds unity, these
distortions amplify over time. Rather than converging toward stable approximations of M, the system
risks runaway co-adaptation: AI systems subtly manipulate human judgments, which then feed back
into reward models ˆ
MRM, locking in a warped objective under the guise of alignment.
Policy/
Model
AI →Human
Influence kinfl
Human Labeling/
Reward Model klabel
Training
ktrain
∆˜
M
(lossy proxy of M)
∆Mref
t
e
∆o
∆˜
M
∆ˆ
MRM
∆θ
z−1
Figure 8: RLHF as an endogenous feedback loop. AI outputs influence human judgments, reshaping ˜
M (a lossy
proxy of M). If the loop gain L exceeds unity, distortions amplify each pass, producing gradual alignment drift
rather than stable convergence.
42

--- Page 43 ---

Constitutional Policies as Handcrafted Slices of Aethical
Constitutional AI introduces explicit principles that carve out a subset of the ethical action space Aethical.
These rules are transparent and interpretable, making them valuable for clarity and auditability. Yet they
provide only narrow coverage of M and are brittle against context shifts or adversarial attempts to
bypass them.
Red-Teaming and Adversarial Training as Boundary Expansion
Red-teaming expands the effective boundary of Aethical by identifying misclassified failures where
Amanipulative ∩Aethical ̸= ∅,
and retraining models to reduce this erroneous overlap. In other words, it systematically uncovers blind
spots where manipulative strategies are mistakenly scored as ethical, then corrects them through adver-
sarial data. However, this process remains reactive, since new regions of M are only incorporated after
failures are observed.
Safety Filters and Institutional Shaping
Safety filters, system prompts, and audits function as institutional mechanisms that directly constrain
model outputs by penalizing defectors and blocking unsafe behaviors at runtime. They provide a strong
last-line defense and can reliably prevent catastrophic failures. However, such interventions remain local
and piecemeal, lacking the broader coverage across M needed to secure long-term stability.
Scalable Oversight and Attempts to Strengthen ϵ
Approaches such as debate, recursive reward modeling, and reinforcement learning from AI feedback
(RLAIF) aim to improve ϵ when direct human supervision is weak. These methods reduce dependence
on scarce labels and extend oversight to more complex domains. However, they remain anchored to ˜
M
unless tied to an explicit construction of M, risking self-reinforcing biases.
A.3
Positioning M in Alignment Literature
Relation to Goodhart’s Law.
Goodhart’s Law warns that once a measure becomes a target, it ceases to track the intended goal. Scalar
objectives are especially brittle—agents can maximize narrow metrics (e.g., reported happiness) while
failing catastrophically on the underlying goal. One motivation for M is that distributing optimization
across multiple dimensions may reduce such exploits: alignment could be defined as staying within an
“aligned region” of M, shifting the challenge from single-value maximization to managing value trade-
offs. Whether such a space can genuinely resist Goodhart pressures or simply relocate them remains an
open question.
Toward M as a Base-Level Loss.
A longer-term question is whether alignment objectives could ever be grounded directly in M rather
than imposed as constraints on proxy losses like next-token prediction. If feasible, this would unify
training loss, evaluation metric, and normative target at the same structural level, reducing divergence
risks. At present this is speculative: we lack representation-learning methods capable of constructing a
reliable M, and bootstrapping one would face major theoretical and empirical hurdles. The research task
is to clarify whether base-level alignment through M is possible, and what technical advances would be
required.
Alignment as a Two-Sided Communication Problem.
Alignment difficulties stem not only from machine optimization but also from human communication.
Methods like RLHF compress human intent into scalar rewards, discarding the reasons behind outcomes;
humans themselves provide inconsistent signals, while models exploit impoverished feedback. This
43

--- Page 44 ---

creates a two-sided bottleneck: machines misinterpret, and humans mis-specify. Offline feedback further
freezes these problems into static datasets, leaving systems brittle under distributional shift. Framing M
as a problem space emphasizes the need for a richer interface: a high-dimensional channel where moral
distinctions could, in principle, be expressed, updated, and audited. This complements ELK [70], which
seeks to make model cognition human-checkable on the factual side. M asks the parallel question:
can moral distinctions be pushed into a machine-usable space, and if so, how can such an interface be
maintained under optimization? See Appendix 9 for visualization.
Best- and Worst-Case Trajectories for M.
Like ELK [70], M should be evaluated against both optimistic and pessimistic possibilities. In the
worst case, M fails as an alignment substrate: it locks in distorted values, misclassifies harmful actions
as ethical, or becomes a manipulable tool that rationalizes power-seeking behavior. In the best case,
M provides a scalable representation of moral structure that not only stabilizes human alignment but
also generalizes to non-human domains, grounding outer alignment in values that extend beyond hu-
man cognitive limits. Which trajectory is realized—and under what conditions such a system fails or
succeeds—remains an open empirical and philosophical question.
44

--- Page 45 ---

B
Figures
W
reality
ˆWH
human communicable projection
(bandwidth-limited/low-dim)
ˆWM
machine internal representation
(opaque/different basis)
ˆ
M∗
Basis matching bridge ˆ
M∗
(richer communication)
projection
projection
ELK-style
pull:
report ˆ
WM →ˆ
WH
push:
enrich human
expressivity
meet-in-the-middle
shared layer M
Legend
ELK pull: project model’s knowledge into human-checkable space.
Human push: increase human expressive bandwidth.
Bridge M: higher-dim shared layer for value communication.
Figure 9: Two-sided alignment as both pull and push. ELK (pull) seeks to map model representations
ˆWM into a human-checkable space ˆWH, but ˆWH—our current communicable channel (e.g., natural
language, scalar feedback)—may be too bandwidth-limited to capture what the model encodes. The
proposed bridge ˆW ∗
H enriches human expressive capacity, pushing value distinctions into a richer rep-
resentational layer that can interface more faithfully with ˆWM. Alignment then becomes a meet-in-the-
middle problem: improving both model transparency and human expressivity.
45

--- Page 46 ---

Table 1: Contemporary alignment methods mapped into the M-space framework. Each method con-
tributes to partial coverage or shaping of M, but none yet constructs a principled privileged moral basis
M∗.
Method
Role in M-space framework
Strengths / Successes
Limitations / Risks
RLHF / Reward Mod-
els
ˆ
MRM ≈
˜
M; ϵ defined via human-
labeled comparisons
Suppresses egregious harms; scal-
able to large models; aligns out-
puts to surface human judgment
Relies on noisy ˜
M; vulnerable to
Goodharting; limited coverage of
M; may incentivize Amanipulative
Constitutional
AI
/
Rule-based Prompts
Handcrafted slice of Aethical; explicit
constraints on ˆ
MA
Transparent rules; interpretable;
improves reliability on banned be-
haviors
Brittle; narrow coverage; may be
bypassed by adversaries or con-
text shifts
Red-Teaming / Adver-
sarial Training
Expands boundary of Aethical; identi-
fies Amanipulative ∩Aethical
Finds failures systematically; im-
proves robustness; reduces attack
surface
Reactive, incident-driven; cannot
guarantee global coverage of M
Safety Filters / Tool-
ing
/
Deployment
Prompts
Institutional shaping: modifies fL,eff
to penalize defectors in deployment
Provides runtime guardrails; re-
duces catastrophic risk; cheap to
deploy
Patchwork; easily circumvented;
often over-blocks or under-blocks
Scalable
Oversight
(Debate,
RLAIF,
Recursive RM)
Attempts to improve ϵ;
ˆ
MA boot-
strapped via AI feedback or multi-
agent protocols
Reduces dependence on scarce
human labels; surfaces complex
reasoning
Anchored to ˜
M unless tied to ex-
plicit M∗; risk of self-reinforcing
errors
Inverse Scaling / Ad-
versarial Benchmarks
Probes divergence
ˆ
MA
̸≈
˜
M as
scale increases
Reveals
scaling
pathologies;
stress-tests coverage of M
Diagnoses failures but does not
solve them; dependent on curated
tasks
Interpretability / ELK
Probes
Direct
mapping
attempts
from
ˆ
MA →M; probes internal repre-
sentations
Theoretically
bridges
behavior
to representation;
complements
action-based oversight
Immature; may reveal ˆ
MA struc-
ture without ability to reshape it;
computationally expensive
Process-based Super-
vision
Supervision on intermediate reason-
ing steps (not just final actions)
Shapes trajectory of
ˆ
MA; re-
duces deceptive Amanipulative be-
haviors
Requires high-quality process la-
bels;
may penalize useful but
opaque reasoning
Debate / Deliberation
Protocols
Multiple agents’ ˆ
MA put into adver-
sarial or cooperative tension
Surfaces conflicting regions of
M;
expands coverage beyond
single ˜
M
Vulnerable to collusion; relies on
debaters already being approxi-
mately aligned
RLAIF
(Reinforce-
ment Learning from
AI Feedback)
Uses ˆ
MAI as proxy for ˜
M; recursive
ϵ construction
Reduces cost of feedback; scal-
able to broad domains
Anchored to model biases; weak
grounding in M; amplifies arti-
facts of base model
Moral
Uncertainty
Modeling
Treats ϵ as distribution over moral
theories; ensemble projections of M
Explicitly encodes uncertainty;
more faithful to pluralistic ˜
M
Complex to implement; still de-
pendent on human priors; lim-
ited by expressiveness of candi-
date theories
Cross-Cultural / Value
Diversity Datasets
Expands
˜
M across multiple cultural
subspaces of M
Reduces parochial bias; improves
generalization of ˆ
MA
Quality of data varies; risk of in-
coherent aggregation; still only
˜
M
Adversarial
Attacks
by Models
Models optimize to find Amanipulative
strategies; stress-test ϵ
Uncovers hidden failure regions
faster; scalable with model capa-
bilities
Risk of overfitting to adversary
distribution; requires constant up-
dating
Auditing Benchmarks
(HELM, BIG-Bench,
etc.)
Empirical probes for coverage of M;
diagnostic of ˆ
MA
Public, standardized evaluation;
comparative progress tracking
Limited scope; benchmarks satu-
rate quickly; may lag behind real-
world Amanipulative
46

```
