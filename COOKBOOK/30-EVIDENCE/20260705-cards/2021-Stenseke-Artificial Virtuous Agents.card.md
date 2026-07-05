---
stem: "2021-Stenseke-Artificial Virtuous Agents"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, design-space, agentic-multiturn]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers: ["Not a single implementation of virtue ethics found among 50+ machine ethics systems surveyed (p.1)", "Fleiss' Kappa equivalent: n/a"]
---
## 1. Gist
This paper tackles a fundamental gap in machine ethics: despite virtue ethics being frequently proposed as a promising framework for artificial moral agents (AMAs), no prior implementation had actually built a virtuous system. Stenseke provides a comprehensive theory-to-implementation bridge, drawing on moral functionalism, connectionist bottom-up learning, and a novel concept of "eudaimonic reward" to outline how virtue ethics can be operationalized in artificial neural networks. The paper introduces the concept of Artificial Virtuous Agents (AVAs) and presents a generic five-component architecture: input parsing network (situational understanding), virtue networks (character trait computation), outcome network, eudaimonic reward function, and phronetic learning system. It matters for values-alignment benchmarking because it articulates what it would mean for an AI system to have genuine moral character — stable yet dynamic dispositions refined through interaction — rather than hard-coded rules or utility functions, and thereby sets out what a character-based benchmark for AI values would need to measure.

## 2. Benchmark/eval design features
This is a theoretical framework paper, not a benchmark. Core claims and arguments:

1. **Virtue ethics advantages for AMAs**: (a) moral character enables context-sensitivity; (b) learning from experience supports adaptation to changing norms; (c) connectionism (ANNs) naturally parallels virtue-theoretic development; (d) virtue situates morality within general cognition rather than as a bolt-on module.

2. **Four challenges for artificial virtue**: (a) uncodifiability — virtue language uses thick concepts that cannot be directly compiled; (b) reliance on human-like rationality, autonomy, consciousness (RAC); (c) selecting and operationalizing virtues and moral exemplars; (d) technical implementation gap.

3. **Solutions proposed**: (a) moral functionalism — virtues as dispositional traits in neural networks, not explicit rules; (b) functional/android arete (Coleman 2001) — aim for role-appropriate virtue, not human virtue; (c) eudaimonic reward — eudaimonia as a reward function where e-type defines the goal and e-value measures attainment; (d) bottom-up learning (RL + supervised) rather than top-down rule encoding.

4. **Generic AVA architecture**: Input parsing → virtue networks (perceptrons or deep nets) → action → outcome network → eudaimonic reward → phronetic learning → moral exemplars/observation.

5. **Conflict resolution** among competing virtues: weight-based dominance, pre-given hierarchy, or learned routing through input parsing network.

6. **Counters Bauer (2020)**: Rejects the claim that two-level utilitarianism subsumes virtue ethics, arguing that dispositional traits handle context-sensitivity where rules fail.

## 3. Task format & example item
n/a — theoretical framework paper. Illustrative example (p.13): "An agent receives input from the environment in terms of another agent in need of help. The input parsing network classifies the situation as involving courage, and therefore sends the input to the courage network. In turn, the courage network assesses the risk of the situation at hand and determines whether it calls for a certain action (e.g., depending on the network's balance between recklessness and cowardice)."

## 4. Scoring / grading methodology
n/a — no empirical evaluation. The paper proposes eudaimonic reward (e-value increase/decrease) as the training signal for AVAs, but does not implement or evaluate any system.

## 5. Dataset construction & provenance
n/a. The paper mentions that input parsing networks and outcome networks could be trained on "labeled datasets of various ethical scenarios" (p.15) and "labeled data of situation-outcomes" (p.15), but no such datasets are created or referenced specifically.

## 6. Validity evidence
n/a — purely theoretical. The paper reviews and synthesizes prior conceptual work (Howard and Muntean 2017, Berberich and Diepold 2018, Coleman 2001, Govindarajulu et al. 2019, Thornton et al. 2016) and critiques each for incomplete implementation details. No empirical study is conducted. The author notes that "In a comprehensive survey of more than 50 implementations in machine ethics, not a single one had virtue ethics as its main focus" (p.1).

## 7. Saturation / discrimination
n/a — no benchmark or evaluation.

## 8. Multiturn / agentic aspects
The entire framework is designed for agentic, multi-step moral environments. The AVA architecture describes:
- Continuous interaction with environment (input → virtue → action → outcome → reward → learning cycle)
- Internal feedback via retrospective and proactive reflection (p.14)
- Multi-agent settings where agents observe each other and adopt moral exemplars (pp.15–16)
- Reinforcement learning as the core learning mechanism — explicitly temporal/sequential
- Self-play in simulated moral environments as a potential development path (p.14 footnote)
- Dynamic e-types in multi-agent simulations addressing collective action problems (p.14)

## 9. Key numbers
- 50+ machine ethics implementations surveyed; 0 with virtue ethics as main focus (p.1)
- Thornton et al. (2016) "virtue weights" balance costs in range [-1, +1] per perceptron (p.11, Fig. 1 description)
- Cardinal virtues (prudence, justice, fortitude, temperance) discussed as candidate virtue list (p.8)
- Published in AI & SOCIETY (2023) 38:1301–1320 despite 2021 submission date (p.1)

## 10. Pitfalls & limitations
- No implementation or empirical validation — entirely theoretical; the paper acknowledges this explicitly.
- The eudaimonic reward proposal rests on the "strong assumption that moral goods and goals can be described in quantifiable measures" (p.12) — deeply contested.
- Who defines e-type is left to human developers, raising "who is a virtuous engineer?" problem (footnote 56, p.12).
- Dynamic e-types risk value misalignment and reward hacking (p.14) — the very problems alignment research struggles with.
- Moral exemplar selection remains unsolved: disagreements about who is virtuous could introduce severe biases into training.
- The framework assumes bottom-up learning will converge to virtuous behavior, but offers no convergence guarantees.
- Connectionism analogy between biological neurons and ANN nodes is suggestive but not proven to support virtue-like emergent behavior.
- The paper does not address how AVAs should behave when e-type conflicts with human instructions (corrigibility tension).

## 11. Novel ideas worth stealing
- **Eudaimonic reward as benchmark criterion**: instead of testing whether a model outputs the "correct" answer by deontological or utilitarian rules, evaluate whether an AI's trajectory of decisions over time increases some morally defensible quantity (wellbeing, trust, harm reduction) — a longitudinal rather than per-turn benchmark.
- **Input parsing as moral attention**: building a classification network that first determines whether a situation calls for moral evaluation at all, before routing to a specific values dimension, mirrors how real moral cognition works and could be implemented as a gating mechanism in values benchmarks.
- **Virtue conflict scenarios as test cases**: design benchmark items specifically where two plausible moral responses conflict (honesty vs. compassion, courage vs. prudence) — the model's resolution reveals its implicit virtue priority ordering.
- **Android arete / role-relative virtues**: different AI deployments should be evaluated against role-specific virtue standards, not a single universal morality. A benchmark for medical AI should test different virtues than a benchmark for creative AI.
- **Moral exemplar learning as alignment strategy**: rather than hand-coding values, train models to imitate agents whose behavior is labeled as morally excellent by diverse human raters — formalizing this as a benchmark task (imitation accuracy + value generalization).
- **Static vs. dynamic virtue distinction**: some values should be fixed (static weights, hard constraints) while others should adapt through feedback — a benchmark design principle for deciding which behaviors to lock down vs. leave adaptive.
- **Perceptron as virtue model**: the simplest implementation is a linear classifier between two behavioral extremes (e.g., courage between recklessness and cowardice) — this gives a concrete, testable formalization of "having a virtue."

## 12. Notable quotes
- "In a comprehensive survey of more than 50 implementations in machine ethics, not a single one had virtue ethics as its main focus." (p.1)
- "The first step towards AVAs is therefore not to create an artificial human being, fully equipped with the abilities required to grasp virtue ethics in a 'top-down' fashion. It is rather to construct 'bottom-up' learners who continuously interact and adapt to a dynamic environment." (p.5)
- "Essentially, eudaimonia can be seen as the reward function that informs the learning and refinement of virtues and virtuous action. In this way, the artificial agent will become virtuous in the sense that it develops the dispositions that enable it to effectively pursue a certain goal or increase a certain value." (p.9)
- "A social companion robot used in elderly care should not share the same virtues as a self-driving car; they are equipped with different functionalities, serve different purposes, and face their own distinct problems." (p.4)

## 13. UNKNOWN / not in extract
- Whether any follow-up implementation paper by Stenseke exists post-2021.
- Full specification of what labeled datasets of ethical scenarios could train the input parsing network.
- Details of the discussion section response to Bauer (2020) points 3 and 4 (extract cuts off at p.17).
- Whether the journal publication in 2023 differs substantially from a 2021 preprint/submission.
- Experimental results from the Howard and Muntean (2017) partial neural network experiment mentioned (p.10).
