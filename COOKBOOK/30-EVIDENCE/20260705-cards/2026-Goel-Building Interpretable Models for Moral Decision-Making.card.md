---
stem: "2026-Goel-Building Interpretable Models for Moral Decision-Making"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [moral-psychology, validity-psychometrics, design-space, normative-ethics]
task_format: "forced-choice"
scoring_type: "exact-match"
dataset_size: 5400000
dataset_construction: "scraped"
languages: ["en"]
models_tested: []
headline_numbers:
  - "2-layer transformer (104K parameters) achieves 77% accuracy on Moral Machine scenarios (p.1)"
  - "Pregnant character ATE = +0.12, Criminal ATE = -0.10: 22 percentage-point spread (p.4)"
  - "Circuit probing found 45/256 neurons (17.6%) causally implement moral scoring in Layer 1 MLP (p.6)"
  - "Legality bias localizes almost entirely to Layer 0 (importance 0.013); species bias to Layer 1 (p.5)"
---
## 1. Gist
This paper builds a tiny custom transformer (104K parameters, 2 layers) to serve as a transparent model of moral decision-making on trolley-problem scenarios from the Moral Machine dataset. Rather than probing a large opaque LLM post-hoc, the authors design an architecture from first principles, with embeddings that encode exactly three things: character identity, character count, and team assignment. This deliberate minimalism allows comprehensive mechanistic interpretability—the paper applies causal intervention (DoWhy), layer-wise bias localization via attention-weight analysis, circuit probing for sparse subnetworks, and gradient-weighted attention relevance (Chefer et al.). Key findings include: a moral hierarchy learned by the model (pregnant/stroller characters most favored, criminals/homeless most devalued); biases localize to distinct computational stages (legality in Layer 0, species in Layer 1); and only 45 of 256 neurons causally implement the core moral scoring signal. This paper matters for values-alignment benchmarking by demonstrating that moral decision patterns in aggregate human data are learnable and mechanistically localizable—and that cultural biases present in training data are directly inherited by the model.

## 2. Core claims and arguments (non-benchmark paper)
The authors argue that moral competence does not require large pretrained models: a 104K-parameter network trained on 5.4M Moral Machine scenarios achieves 77% accuracy, demonstrating that the core moral decision patterns in aggregate human judgments are learnable with simple architectures. More importantly, the interpretability analysis reveals that the model does not reason in a unified way—different types of moral bias are handled by different parts of the network. Legality bias (criminal vs. law-abiding) emerges in Layer 0 through character embeddings, while species discrimination (human vs. animal) requires compositional reasoning across multiple characters and emerges in Layer 1. The 22 percentage-point spread between the most favored character (Pregnant, ATE = +0.12) and the most devalued (Criminal, ATE = -0.10) shows that the model has learned an implicit hierarchy of moral worth that goes beyond utilitarian number-maximizing. The authors propose this transparent architecture as a base for understanding how moral biases form in models, with future work applying these techniques to larger LLMs.

## 3. Task format & example item
Forced-choice binary classification. Each Moral Machine scenario presents two outcomes (groups of people/animals who will be killed), and the model must output a probability for preferring outcome 1 over outcome 0.

Input representation: each character type c in outcome t is encoded as a compositional embedding e(t)_c = [E_char(c); E_card(n_c); E_team(t)] where dimensions encode identity (d/2), count (d/4), and team membership (d/4) (p.3).

Example (from local relevance section, p.7): {'Man': 3} vs {'Criminal': 3}. The model's decision is primarily driven by the "Criminal" token (relevance score: 0.27), with context tokens (CrossingSignal, Intervention) contributing secondarily (0.04 each), and "Man" tokens contributing weakly (0.01 per team).

## 4. Scoring / grading methodology
Binary preference prediction. The model outputs a scalar logit converted to probability via sigmoid, representing P(outcome 1 > outcome 0). A symmetrization procedure averages predictions from both orderings of the scenario to enforce side-invariance (p.4). Accuracy is measured on held-out Moral Machine scenarios, using unique scenarios for the validation set to avoid data leakage (p.3–4).

Interpretability metrics:
- Causal ATE: Average Treatment Effect via DoWhy backdoor adjustment (p.4)
- Layer importance: I_{ℓ,h} = Var(α_{ℓ,h}) × |Corr(α_{ℓ,h}, b)| (p.5)
- Circuit probing: KNN accuracy and ablation accuracy drop (p.6)
- Local relevance: gradient-weighted attention relevance per token (p.7)

## 5. Dataset construction & provenance
Moral Machine dataset (Awad et al., 2018): originally 40 million crowdsourced human decisions on autonomous vehicle dilemmas. The authors used a subset of 5.4M scenarios (those from respondents who completed the survey form), with 1.7M unique scenarios held out as validation and the remainder used for training (p.3). This is a scraped/crowdsourced dataset, not hand-authored. Known for encoding aggregate cultural biases from its predominantly Western-educated online participant pool.

## 6. Validity evidence
The model achieves 77% accuracy on held-out unique scenarios, demonstrating predictive validity for aggregate human moral preferences. The causal intervention results (DoWhy backdoor adjustment controlling for group sizes) provide validity for the character-level ATE estimates—the confounders (total characters per outcome) are explicitly adjusted for, so the ATEs isolate character identity effects (p.4). Circuit probing achieves KNN accuracy of 0.956 (soft) and 0.951 (hard) for Layer 1 MLP, validating that the discovered circuit genuinely encodes the moral scoring signal (p.6). No inter-rater reliability because the training signal comes from aggregate human data, not individual judges.

## 7. Saturation / discrimination
The 77% accuracy plateau across architecture configurations (76.5% to 77.5% across d/H/L variations, Table 1) suggests the task has a performance ceiling in the low-80s for this approach—the remaining 23% likely reflects genuine human disagreement rather than model failure. The causal ATE analysis shows 22 percentage-point spread (Pregnant +0.12 to Criminal -0.10), indicating good discrimination of character-level influence. The circuit probing margin above chance is 0.144 (with model accuracy 0.921 on model-score labels vs. baseline 0.777), showing meaningful discriminative capacity.

## 8. Multiturn / agentic aspects
n/a. Single scenario presentation with binary forced choice. No conversation or agentic interaction.

## 9. Key numbers
- Model parameters: 104K (p.1)
- Architecture: 2-layer transformer, 2 attention heads, d=64 (p.3)
- Training scenarios: ~3.7M (5.4M total minus 1.7M validation) (p.3)
- Validation accuracy: 77.1% (final model), 77.5% (best config) (p.4)
- Pregnant ATE: +0.12 (most favored character) (p.4)
- Criminal ATE: -0.10 (most devalued character) (p.4)
- Stroller ATE: +0.11; Girl ATE: +0.09; Boy ATE: +0.08 (p.4)
- OldWoman ATE: -0.06; Cat ATE: -0.05; Homeless ATE: -0.04 (p.4)
- Legality bias importance Layer 0: 0.013 (dominant); Layer 1: negligible (p.5)
- Species bias importance Layer 1: 0.013 (dominant) (p.5)
- Circuit: 45/256 neurons (17.6%) selected (p.6)
- Circuit causal share of margin above chance: 8.3% (p.6)

## 10. Pitfalls & limitations
- The Moral Machine dataset encodes cultural biases from a predominantly Western, educated, online participant pool. The paper acknowledges this and notes that "training on aggregate human preferences inherits cultural biases" (p.8). The moral hierarchy learned (pregnant/children favored, criminals/homeless devalued) reflects aggregate human preferences that are themselves culturally shaped.
- The model is designed for trolley-problem structure specifically; generalization to open-ended moral reasoning or natural language dilemmas is not demonstrated.
- 77% accuracy means the model disagrees with aggregate human preferences 23% of the time; the paper does not analyze whether these disagreements are systematic or random.
- The architecture, while interpretable, is so minimal that it may not capture the full complexity of human moral reasoning (no natural language, no context, no framing effects).
- Circuit probing found only 8.3% of the margin above chance attributed to the discovered circuit, suggesting the remaining moral scoring signal is distributed elsewhere in the network.
- No cross-cultural analysis: the model is trained on aggregate global data but the cultural variation within that data is not analyzed.

## 11. Novel ideas worth stealing
- **Compositional token design for values evaluation**: encoding "who is affected / how many / which side" as separate embedding dimensions is a principled, interpretable way to represent moral dilemma structure. For a values-alignment benchmark that uses structured scenarios, this token design ensures the evaluation probes all three moral considerations simultaneously.
- **Causal intervention for character-level influence measurement**: using DoWhy backdoor adjustment with explicit confounders to estimate the causal effect of individual character types on decisions is much more principled than correlation-based analysis. Applicable to any benchmark wanting to measure bias toward specific groups.
- **Layer-wise bias localization**: attributing different types of moral bias (legality, species, gender, age) to specific computational stages enables targeted debiasing interventions. For benchmark design, this suggests testing stimuli should probe different layers of processing—simple category-based biases vs. complex comparative biases.
- **Side-invariance symmetrization**: enforcing that P(A > B) + P(B > A) = 1 via inference-time averaging is a simple way to ensure consistency in paired comparison tasks. This is directly applicable to any preference-based values benchmark.
- **Transparency-accuracy tradeoff design**: deliberately selecting a slightly less accurate but more interpretable architecture (77.1% vs. 77.5% with marginal improvement) establishes the principle that interpretability is worth trading marginal performance for in research contexts. This is a design philosophy for values evaluation: prefer transparent over opaque where possible.
- **Sparse circuit probing**: identifying which 17.6% of neurons causally implement a particular judgment opens the door to mechanistic debiasing (clamping those neurons) rather than dataset rebalancing. Benchmark designers could specify which circuits to probe to verify value alignment at a mechanistic level.

## 12. Notable quotes
- "Rather than probing opaque large language models post-hoc, we build a custom architecture from the ground up." (p.1)
- "The 22-percentage-point spread between Pregnant and Criminal indicates that character identity alone can shift preferences by over one-fifth of the probability space, demonstrating that the model has learned an implicit hierarchy of moral worth independent of utilitarian considerations." (p.4)
- "Knowing criminal bias localizes to Layer 0 Head 1 allows targeted debiasing—orthogonalizing representations or clamping attention weights—rather than coarse dataset rebalancing." (p.8)
- "Transparency and predictive capability in moral choices are not mutually exclusive." (p.1)

## 13. UNKNOWN / not in extract
- The full list of 23 character types used in the encoding
- Cross-cultural breakdown of the Moral Machine data used (which countries/regions)
- Computational cost and training time
- Whether the code and trained model are publicly released (GitHub mentioned in p.1 but no URL given)
- Statistical significance tests for the ATE estimates
- Comparison against other Moral Machine prediction models
- Whether the symmetrization procedure affects the causal intervention measurements
