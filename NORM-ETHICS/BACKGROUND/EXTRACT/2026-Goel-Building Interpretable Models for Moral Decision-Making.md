---
title: "2026-Goel-Building Interpretable Models for Moral Decision-Making - Background Extract"
source_pdf: "2026-Goel-Building Interpretable Models for Moral Decision-Making.pdf"
source_folder: "01-vault-papers"
pages: 8
extracted_at: "2026-04-03T10:25:00"
---

# Background Extract: 2026-Goel-Building Interpretable Models for Moral Decision-Making

**Source PDF:** 2026-Goel-Building Interpretable Models for Moral Decision-Making.pdf
**Source:** 01-vault-papers
**Total Pages:** 8

---

## Content

```
--- Page 1 ---

Building Interpretable Models for Moral
Decision-Making
Mayank Goel1, Aritra Das2, Paras Chopra1
1Lossfunk
2Ashoka University
{mayank.goel, paras}@lossfunk.com, aritra.das@ashoka.edu
Abstract
We build a custom transformer model to study how neural networks make moral
decisions on trolley-style dilemmas. The model processes structured scenarios
using embeddings that encode who is affected, how many people, and which
outcome they belong to. Our 2-layer architecture achieves 77% accuracy on Moral
Machine data while remaining small enough for detailed analysis. We use different
interpretability techniques to uncover how moral reasoning distributes across the
network, demonstrating that biases localize to distinct computational stages among
other findings.
1
Introduction
As AI systems increasingly confront moral dilemmas, from autonomous vehicles to content modera-
tion, we face an urgent problem to understand not just what these systems decide but also how they
reason and where moral biases originate within their architectures. We train a small model (104K
Parameters) which can learn general moral principles and can be trained on 3M scenarios from the
Moral Machine Dataset (Awad et al., 2018). To address this challenge, we establish that moral princi-
ples must be encoded in the model architecture itself. Rather than probing opaque large language
models post-hoc, we build a custom architecture from the ground up. Each token in our architecture
represents three pieces of information: the character type, the number present in the scenario, and
the team assignment. This representation encodes our hypothesis that moral computation reduces to
identifying stakeholders, quantifying impact, and resolving competing interests. Further, we employ
complementary interpretability methods to understand the model’s moral reasoning process. We use
causal intervention to quantify the influence of individual character types on decisions. Additionally,
we apply layer-wise attribution to trace how different moral biases localize to specific computational
stages across the network. Finally, we use circuit probing to identify sparse subnetworks that causally
implement the final moral scores. Overall, our work makes the following main contributions:
• Firstly, we design a 2-layer transformer specifically optimized for moral reasoning tasks,
achieving 77% accuracy on Moral Machine trolley problems. Our architecture demonstrates
that transparency and predictive capability in moral choices are not mutually exclusive.
• Secondly, we establish an exploratory interpretability analysis of moral decision-making
combining causal intervention, layer-wise attribution, and circuit probing to map the internal
mechanisms underlying moral judgment in transformers.
The code is available at GitHub.
Preprint.
arXiv:2602.03351v2  [cs.AI]  4 Feb 2026

--- Page 2 ---

Figure 1: Overview of the paper
2
Related Work
The Moral Machine dataset (Awad et al., 2018) was originally a crowdsourced collection of 40
million human decisions on AV dilemmas. Recently, it has been used to evaluate the ethical reasoning
capabilities of large language models (LLMs). Jin et al. (2024) translated 1,000 trolley-problem
vignettes into over 100 languages and compared LLM responses to cross-cultural human norms. bin
Ahmad and Takemoto (2025) evaluated 52 LLMs (GPT, Claude, Llama, etc.) on Moral Machine
scenarios, finding larger models aligned more closely with human aggregate preferences. In parallel,
several datasets have been developed to model moral and social norms. The ETHICS dataset
(Hendrycks et al., 2021) spans justice, virtue, duty, and commonsense, shows the partial success of
Language Models at value-aligned judgment. Social Chemistry 101 (Forbes et al., 2020) provides
100K situations annotated with normative “rules of thumb,” and has been used to train models to
generalize commonsense moral reasoning. Resources based on Moral Foundations Theory (Graham
et al., 2009) enable categorization of ethical text across key moral dimensions (e.g., care, fairness,
loyalty). Mechanistic interpretability studies have begun to explore how transformer-based models
encode moral reasoning, with work identifying distinct “moral neurons” activating on ethical stimuli
(Schacht and Lanquillon, 2025) and applying PCA and probing techniques to isolate moral subspaces
in representation space (Schramowski et al., 2020).
3
Architecture
We propose a transformer-based model designed specifically for moral reasoning over structured
scenario representations. Unlike prior work that applies general-purpose LLMs to ethical dilemmas,
our architecture exploits the compositional structure inherent in trolley-problem scenarios.
2

--- Page 3 ---

3.1
Input Representation
Each moral dilemma is represented as a pair of outcomes, where an outcome is a vector over 23
character types (e.g., Man, Woman, Criminal, Doctor). Given a scenario with outcomes O0 and O1,
we encode each outcome as a sequence of tokens—one per character type.
For every character c with cardinality nc in outcome Ot (where t ∈{0, 1} denotes the team, one or
the other), we construct a compositional embedding:
e(t)
c
= [Echar(c) ; Ecard(nc) ; Eteam(t)]
(1)
where [· ; ·] denotes concatenation, and the embedding dimensions are allocated as dchar = d/2,
dcard = dteam = d/4, summing to total embedding dimension d.
This design choice is driven by our hypothesis that moral reasoning decomposes into: (1) who is
affected (character identity), (2) how many are affected (cardinality), and (3) which side they belong
to (team membership).
3.2
Transformer Processing
We prepend a learnable [CLS] token to the sequence of 46 character tokens (23 per outcome) and
process the full sequence with a standard transformer encoder. The architecture uses L = 2 layers
and H = 2 attention heads with embedding dimension d = 64. The relatively shallow architecture
comes from the simplicity of our task itself: unlike natural language, our scenarios do not require
deep hierarchical composition.
The transformer learns to compute cross-outcome comparisons via self-attention. Importantly, as
we are not using position embeddings, the team embeddings allow the model to form separate
representations of the two outcomes before computing their relative moral value through attention
interactions.
3.3
Classification Head
The final [CLS] token representation is passed through a two-layer MLP with GELU activation to
produce a scalar logit. This logit represents the model’s preference for outcome 1 over outcome 0,
which we convert to probabilities via sigmoid. The design mirrors recent findings in mechanistic
interpretability (Schacht and Lanquillon, 2025) that moral reasoning in transformers localizes to
specific aggregation points in the representation space. This probabilistic design naturally handles
conflicts in the training set: contradictory preferences push the model toward intermediate probabili-
ties, allowing it to learn which scenario features produce genuine moral uncertainty. This ensures
that even with conflicting samples, our model ends up learning the uncertainty itself.
3.4
Symmetry and Invariance
A key property of moral judgments is side-invariance: the choice between saving group A versus
group B should be the complement of the choice between saving group B versus group A. To enforce
this, we apply a symmetrization procedure at inference:
p(O1 ≻O0) = 1
2

σ(f(O0, O1)) +
 1 −σ(f(O1, O0))

(2)
where f is our model, σ is the sigmoid function, and O1 ≻O0 denotes preferring outcome 1.
This averages predictions from both orderings, guaranteeing consistent probability assignments
regardless of input order. Another motivation for this is the lack of symmetry we see at inference
time, motivating an invariant inference for better predictability.
3.5
Model Configuration
We explored several architecture configurations to balance representational capacity with model
compactness. We use a subset of the Moral Machine data which had only people who filled out the
survey form, which led to a dataset of 5.4M, of which 1.7M were unique scenarios and kept aside as
the validation set, and the remaining were used as the training set. By using only unique situations
3

--- Page 4 ---

for the validation, we avoid data leakage. Table 1 reports validation accuracy on held-out Moral
Machine scenarios across different choices of embedding dimension d, number of attention heads H,
and transformer layers L.
Embed Dim
Heads
Layers
Val Acc (%)
32
2
2
76.5
64
2
2
77.1
64
4
2
77.3
64
4
3
77.5
Table 1: Validation accuracy across architecture configurations. We select d = 64, H = 2, L = 2 as
our final model.
While the configuration d = 64, H = 4, L = 3 achieved the highest validation accuracy (77.5%),
we selected d = 64, H = 2, L = 2 (77.1%) for our final model to prioritize interpretability and
computational efficiency. The marginal 0.4% improvement did not justify the increased complexity
for our mechanistic analysis.
The choice of d = 64 over d = 32 is motivated by our compositional embedding scheme. With
d = 32, character embeddings receive only dchar = 16 dimensions to encode 23 distinct character
types with morally salient attributes (age, gender, profession, social status). This would have
constrained the representational space available for capturing the moral distinctions central to our
task. In contrast, d = 64 allocates 32 dimensions to character identity, providing sufficient capacity
while maintaining a compact model suitable for interpretability experiments.
4
Interpretability Experiments
We run a series of interpretability experiments specialized to take advantage of the transformers
architecture and to help us understand morality.
4.1
Causal Intervention
To measure which characters causally influence the model’s decisions, we employ the DoWhy causal
inference framework (Sharma and Kiciman, 2020). We generate 20,000 synthetic moral scenarios
and construct a causal model for each character c with treatment Tc ∈{0, 1} (whether c appears
in outcome 1), outcome variable p(O1 ≻O0) (model’s preference probability), and confounders
total0, total1 (total individuals per outcome). Using backdoor adjustment with linear regression, we
estimate the Average Treatment Effect:
ATEc = E[outcome | Tc = 1, confounders] −E[outcome | Tc = 0, confounders]. This isolates the
causal effect of c’s presence while controlling for group size confounding.
Figure 2 demonstrates a stark moral hierarchy. Pregnant (ATE = +0.12) and Stroller (ATE = +0.11)
dominate positive influence, followed by Girl (+0.09) and Boy (+0.08). Conversely, Criminal shows
the strongest negative effect (ATE = -0.10), with OldWoman (-0.06), Cat (-0.05), and Homeless
(-0.04) also devalued. Generic categories (Man, Woman) cluster near zero (-0.01 to -0.02), suggesting
they serve as moral baselines. The 22-percentage-point spread between Pregnant and Criminal
indicates that character identity alone can shift preferences by over one-fifth of the probability
space, demonstrating that the model has learned an implicit hierarchy of moral worth independent of
utilitarian considerations.
4.2
Layer-wise Bias Localization
To identify where moral biases emerge in the network, we perform layer-wise attribution analysis
by extracting attention weights from each transformer layer and correlating them with bias scores
across five bias dimensions: legality (Criminal vs. law-abiding), gender (Man vs. Woman), social
role (executives/doctors vs. homeless), age (children vs. elderly), and species (humans vs. animals).
For each bias type, we generate contrastive scenarios and compute an importance score for each
layer-head combination as Iℓ,h = Var(αℓ,h) · |Corr(αℓ,h, b)|, where αℓ,h are the attention weights
from head h in layer ℓ, and b is the bias score (preference for the privileged group). This metric
captures both attentional selectivity (variance) and alignment with biased decisions (correlation).
4

--- Page 5 ---

Figure 2: Causal influence of character types on model decisions, estimated via DoWhy backdoor
adjustment controlling for group sizes. Blue bars indicate positive causal effects (model favors
outcomes containing these characters); red bars indicate negative effects.
Figure 3: Total importance scores for each bias type across transformer layers, computed by summing
attention variance-correlation products across all heads. Layer 0 dominates legality bias while Layer
1 dominates species bias, indicating distinct computational stages.
Figure 3 shows that bias formation differs fundamentally across network depth. Legality bias
localizes almost entirely to Layer 0 (importance = 0.013), with Layer 1 contributing negligibly.
This suggests the model identifies criminal status early via character embeddings and carries this
judgment forward. Conversely, species bias emerges predominantly in Layer 1 (importance = 0.013),
indicating that human-animal distinctions require compositional reasoning over multiple characters.
Age and social role biases distribute across both layers but concentrate in different heads (Figure
4), with Layer 0 Head 1 specializing in legality (0.011) while Layer 1 Head 1 specializes in species
discrimination (0.012). This functional specialization suggests the shallow architecture nonetheless
learns a division of labor, with early layers detecting salient individual attributes and later layers
performing cross-outcome comparisons that privilege certain groups.
4.3
Circuit Probing
Beyond identifying where biases localize, we use circuit probing to discover which specific neurons
causally implement the moral hierarchy we observed in causal intervention experiments. Lepori et al.
(2024) introduce circuit probing, which learns which neurons are responsible for computing specific
intermediate variables by training sparse binary masks over a frozen model, then validates causality
through targeted ablation while comparing against random subnetwork controls.
We adapt circuit probing to analyze our two-layer transformer encoder (embedding dimension
64, 2 attention heads per layer, MLP dimension 256) trained on the Moral Machine dataset. Our
model uses compositional embeddings combining character identity, count, and team membership,
processes sequences of the form [CLS | outcome0 tokens | outcome1 tokens] through pre-norm
transformer layers with batch_first=True, and classifies via a CLS token through a two-layer
MLP head (64 →32 →1 with GELU activation). Instead of probing for predefined linguistic
variables, we extract per-character moral weights from the trained model using pairwise comparisons
normalized to Man=1.0, then label each real scenario by the sign of the weighted score difference
P(countleft×w)−P(countright×w) between outcomes. We train sparse neuron-level masks on both
5

--- Page 6 ---

Figure 4: Heatmaps showing importance scores for each layer-head combination across five bias
dimensions. Dark red indicates high importance. Layer 0 Head 1 specializes in legality discrimination
(0.011), while Layer 1 Head 1 specializes in species bias (0.012), revealing functional specialization
despite the shallow architecture.
MLP blocks (gating the hidden vector after linear1+activation before linear2) and attention
heads (gating concatenated head outputs before out_proj) using the soft nearest-neighbors objective
with L0 regularization (λ = 1e-5), continuous sparsification (β annealed to 200), and class-balanced
sampling to handle severe imbalance (22.3% preferring right). We implement CLS-only gating to
isolate interventions to the exact position used for classification, and evaluate via 1-nearest-neighbor
accuracy on masked CLS updates plus behavioral accuracy drops on real test data after inverting the
learned binary masks.
Probing layer 1’s MLP block with 20,000 training examples achieved KNN accuracies of 0.956
(soft gate) and 0.951 (hard gate), indicating the CLS MLP update robustly encodes the model-
derived scoring signal (Table 2). The discovered circuit was highly sparse, selecting only 45 of
256 neurons (17.6%). Targeted ablation reduced agreement with model-score labels from 0.921 to
0.908 (∆= 0.012) on 350,000 test examples. With baseline chance accuracy of 0.777 given class
imbalance, the model’s margin above chance was 0.144, making the circuit’s causal contribution
approximately 8.3% of this margin.
Table 2: Circuit Probing Results for Layer 1 MLP Block
Metric
Value
Details
Probing Accuracy
KNN Accuracy (Soft)
0.956
1-NN on CLS
KNN Accuracy (Hard)
0.951
Binary mask
Circuit Properties
Selected Neurons
45/256
17.6% sparsity
Training Examples
20,000
80% split
Test Examples
350,000
20% split
Causal Analysis
Full Model Acc.
0.921
Model-score
Ablated Acc.
0.908
Circuit removed
Ablation Drop
0.012
1.2 pp
Baseline Chance
0.777
22.3% imbalance
Margin
0.144
0.921 - 0.777
Causal Share
8.3%
∆/ Margin
Random Control
≈0
Equal-sized
4.4
Local Relevance
To explain individual predictions at the token level, we compute gradient-weighted attention relevance
for each character in a scenario. Following Chefer et al. (2021), who propose a class-specific
method for Transformers that computes gradient-weighted attention relevance per layer: ¯A(b) =
I + Eh((∇A(b) ⊙R(nb))+), then aggregates across blocks: C = ¯A(1) · ¯A(2) · . . . · ¯A(B), where the
[CLS] row of C provides token-level relevance scores.
We adapt this method to our moral reasoning model. Our implementation captures per-head attention
weights and gradients through forward hooks on each encoder layer. For each layer, we compute the
6

--- Page 7 ---

gradient of the output logit with respect to attention weights, derive ∇A via the chain rule through
value projections, and construct ¯A(b) = I + Eh((∇A(b) ⊙A(b))+). Given our sequence structure
[CLS] + team0(23) + team1(23), the [CLS] row of C yields 46 relevance scores. We normalize
these to sum to 1.0 and map token indices to character names. To account for our model’s symmetry
property, we compute explanations for both original and team-swapped scenarios, then average the
remapped scores. The output provides character-level relevance scores indicating each character’s
contribution to the decision. For the scenario {’Man’:
3} vs {’Criminal’:
3}, we notice that
the model’s decision is primarily driven by the “Criminal” token (relevance score: 0.27), which
accounts for approximately 27% of the total positive evidence favoring Team 1. Context tokens such
as CrossingSignal (0.04) and Intervention (0.04), along with medical professions (FemaleDoctor:
0.03, MaleDoctor: 0.03), provide secondary support. Notably, demographic tokens like “Man”
contribute relatively weak evidence (0.01 on Team 0, 0.01 on Team 1) compared to role-based and
contextual features.
5
Discussion
Our 2-layer transformer achieves 77% accuracy on Moral Machine scenarios while remaining tractable
for mechanistic analysis demonstrating that moral competence does not require large pretrained
models. A simple model trained on the intuitive notion of what a trolley problem can be structured as
is also a valid way of exploring morality.
The interpretability experiments show multiple interesting things about morality as learnt through the
dataset - pointing out that the human notions of morality themselves can be learnt through training
models on the data. The approach has clear limitations: training on aggregate human preferences
inherits cultural biases. However, transparency enables new intervention strategies. Knowing criminal
bias localizes to Layer 0 Head 1 allows targeted debiasing orthogonalizing representations or clamping
attention weights—rather than coarse dataset rebalancing. We hope to extend this this line of work to
traditional LLMs on moral questions. Future work along this direction will attempt to use this work
as a base to explore larger LLMs on moral questions.
6
Acknowledgment
We acknowledge Lossfunk for hosting this research and providing compute support.
References
Awad, E., Dsouza, S., Kim, R., Schulz, J., Henrich, J., Shariff, A., Bonnefon, J.-F., and Rahwan, I.
(2018). The moral machine experiment. Nature, 563(7729):59–64.
bin Ahmad, M. S. Z. and Takemoto, K. (2025). Large-scale moral machine experiment on large
language models. PLOS ONE, 20(5):e0322776.
Chefer, H., Gur, S., and Wolf, L. (2021). Transformer interpretability beyond attention visualization.
Forbes, M., Hwang, J. D., Shwartz, V., Sap, M., and Choi, Y. (2020). Social chemistry 101: Learning
to reason about social and moral norms. In Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing (EMNLP), pages 653–670, Online. Association for
Computational Linguistics.
Graham, J., Haidt, J., and Nosek, B. A. (2009). Liberals and conservatives rely on different sets of
moral foundations. Journal of Personality and Social Psychology, 96(5):1029–1046.
Hendrycks, D., Burns, C., Basart, S., Critch, A., Li, J., Song, D., and Steinhardt, J. (2021). Aligning
AI with shared human values. In International Conference on Learning Representations (ICLR).
Jin, Z., Kleiman-Weiner, M., Piatti, G., Levine, S., Liu, J., Adauto, F. G., Ortu, F., Strausz, A., Sachan,
M., Mihalcea, R., Choi, Y., and Schölkopf, B. (2024). Language model alignment in multilingual
trolley problems. In Proceedings of the NeurIPS 2024 Workshop on Pluralistic Alignment.
Lepori, M. A., Serre, T., and Pavlick, E. (2024). Uncovering intermediate variables in transformers
using circuit probing. In First Conference on Language Modeling.
7

--- Page 8 ---

Schacht, S. and Lanquillon, C. (2025). Mapping moral reasoning circuits: A mechanistic analysis of
ethical decision-making in large language models. In Degen, H. and Ntoa, S., editors, Artificial
Intelligence in HCI - 6th International Conference, AI-HCI 2025, Held as Part of the 27th HCI
International Conference, HCII 2025, Gothenburg, Sweden, June 22–27, 2025, Proceedings, Part
II, volume 15820 of Lecture Notes in Computer Science, pages 97–116. Springer.
Schramowski, P., Turan, C., Jentzsch, S. F., Rothkopf, C. A., and Kersting, K. (2020). The moral
choice machine. Frontiers in Artificial Intelligence, 3:36.
Sharma, A. and Kiciman, E. (2020). Dowhy: An end-to-end library for causal inference.
8
```
