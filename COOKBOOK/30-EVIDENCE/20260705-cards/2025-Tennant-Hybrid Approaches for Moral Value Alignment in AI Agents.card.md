---
stem: "2025-Tennant-Hybrid Approaches for Moral Value Alignment in AI Agents"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, moral-psychology, design-space, agentic-multiturn]
task_format: "n/a"
scoring_type: "behavioral"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Five moral reward types (Utilitarian, Deontological, Virtue-equality, Virtue-kindness, Virtue-mixed) implemented in Q-learning agents in social dilemma games (p.20)"
  - "Constitutional AI fine-tunes LLMs with RL using a 'constitution' of explicit principles (p.14)"
  - "RLHF fine-tuning may merely create a 'safety wrapper' on otherwise unaltered core models (Jain et al., 2023, cited p.9)"
---
## 1. Gist
This paper by Tennant, Hailes, and Musolesi (UCL/Bologna) is a manifesto-style theoretical framework arguing that moral value alignment in AI agents should use *hybrid* approaches — combining explicit top-down moral principles with bottom-up learning. The authors systematize existing techniques along a continuum from fully rule-based (top-down) to fully learned (bottom-up), identify that most mainstream approaches cluster at the extremes, and advocate for methods that embed moral frameworks (deontological, utilitarian, virtue ethics) as explicit rewards or constraints within reinforcement-learning systems. Four case studies are reviewed: safe/constrained RL, Constitutional AI, RL in social dilemma games, and LLM fine-tuning with intrinsic rewards. For values-alignment benchmarking, the paper is significant because it offers a comprehensive taxonomy of moral frameworks formalized as reward functions, and an evaluation schema for moral agents based on behavioral outcomes, providing design vocabulary directly applicable to benchmark construction.

## 2. Benchmark/eval design features
This is a position/survey paper, not a benchmark itself. Core claims:
- The field has a continuum problem: most methods sit at opposite extremes (pure rules vs. pure RLHF), leaving a hybrid middle underexplored.
- Hybrid systems (explicit moral principles + learning) offer better controllability and interpretability than pure bottom-up methods, while avoiding the brittleness of pure rule-based systems.
- Five ethical frameworks can be formalized as intrinsic reward functions for RL agents in social dilemma settings (Table 3, 4): Utilitarian (sum of payoffs), Inequity-averse (Fehr-Schmidt), Equality/Fairness (Gini coefficient), Rawlsian Veil of Ignorance (maximin), Deontological (conditional cooperation norm), Virtue-kindness (cooperate regardless), and Virtue-mixed (linear combination).
- Evaluation of moral agents should go beyond cumulative reward to include: cooperation levels, Gini coefficient outcomes, egalitarian minimum payoff, and qualitative behavioral assessments.
- The paper explicitly notes that existing moral benchmarks exist (Hendrycks et al., 2021; Pan et al., 2023; Reinecke et al., 2023) but focuses on agent evaluation rather than surveying them.

## 3. Task format & example item
n/a — This is a theoretical framework paper. No evaluation items are administered.

Example reward function (p.20, Table 4):
Deontological agent: R_intr = -ξ if action=Defect and opponent previously Cooperated; 0 otherwise.
Virtue-mixed agent: R_intr = β*(1 - |R_M - R_O|/(R_M + R_O)) + (1-β)*ξ if Cooperate; β*(1 - |R_M - R_O|/(R_M + R_O)) otherwise.

## 4. Scoring / grading methodology
For moral RL agents (cited from Tennant et al., 2023), proposed evaluation metrics (p.22):
- G_collective: cumulative sum of both players' payoffs across T iterations
- G_Gini: cumulative Gini coefficient across T iterations (measures equality)
- G_min: cumulative minimum payoff across T iterations (Rawlsian egalitarian metric)
These are population-level outcome metrics; additional behavioral metrics include cooperation rate and strategy analysis.

## 5. Dataset construction & provenance
No dataset. Social dilemma environments are procedurally defined: Iterated Prisoner's Dilemma, Iterated Volunteer's Dilemma, Iterated Stag Hunt (payoff matrices given in Table 2, p.15). These are well-established game-theoretic benchmarks from economics/philosophy.

## 6. Validity evidence
No empirical validation in this paper (it is a manifesto/survey). Points to Tennant et al. (2023) as empirical evidence that Q-learning agents can learn moral policies with these intrinsic rewards. Notes that Constitutional AI's ability to promote values beyond harmlessness remains unvalidated (p.15).

## 7. Saturation / discrimination
Not applicable as an evaluation benchmark. The paper does note (p.23) that the "equality" reward definition produces the least efficient learning agent among the five types tested.

## 8. Multiturn / agentic aspects
Highly relevant: the paper is explicitly framed around agentic decision-making. The core environment is multi-agent iterated games (T iterations), where the state at each step is the opponent's previous action. LLM-based agent fine-tuning is also discussed (Section 3.5), where LLMs act as decision-makers in sequential game-theoretic environments using on-policy RL (PPO). The paper discusses generalization of moral policies from IPD to four other 2x2 matrix games (p.21).

## 9. Key numbers
- Five moral agent types tested in Tennant et al. (2023): Utilitarian, Deontological, Virtue-equality, Virtue-kindness, Virtue-mixed, plus Selfish baseline (p.20)
- Three social dilemma games used: IPD, IVD, ISH (p.15, Table 2)
- Three evaluation metrics: G_collective, G_Gini, G_min (p.22, Equations 1-3)
- Constitutional AI constitution: prompts based on UN Declaration of Human Rights, company terms of service, and researcher-defined principles (p.14)
- Paper identifies six bottom-up disadvantages including reward-hacking, sample inefficiency, data poisoning, and "safety wrapper" problem (p.9-10, Table 1)
- Collective Constitutional AI (Anthropic, 2024) extends to crowd-sourced principles (p.15)

## 10. Pitfalls & limitations
- The paper explicitly states it does not address *which* moral values should be implemented — the value content is interchangeable (p.4)
- Moral reward functions rely on scalar payoff structure and discrete action sets — problematic for open-ended real-world tasks (p.23)
- Simulated social dilemma environments are extreme simplifications of real moral contexts
- Constitutional AI evaluated only on harmlessness; other values untested (p.15)
- Fine-tuning on specific action tokens may cause overfitting (p.21)
- Pluralistic alignment — different users have different moral values — is noted but not resolved (p.4)
- No empirical results in the paper itself; all empirical evidence is cited from companion papers

## 11. Novel ideas worth stealing
1. **Reward-function taxonomy for ethics**: The systematic mapping in Tables 3-4 of philosophical moral frameworks (utilitarian, deontological, virtue) to mathematical reward functions is directly reusable. A benchmark could test whether AI systems *prefer* outcomes aligned with each framework, or test understanding of these distinctions.
2. **Multi-objective evaluation**: Using G_collective + G_Gini + G_min simultaneously avoids reward-hacking by checking that a "moral" agent isn't gaming one metric at the cost of others. A benchmark for values alignment should similarly include multi-dimensional outcome checks.
3. **Social dilemma environments as alignment testbeds**: IPD/IVD/Stag Hunt are highly controlled environments where cooperation/defection maps cleanly onto moral choices. They offer a ground-truth-based evaluation setting that doesn't require human judges.
4. **Hybrid continuum framing**: The top-down ↔ bottom-up continuum (Figure 2) is a useful categorization for organizing existing benchmarks — it would help map the landscape of evaluation methods rather than treating them as a flat set.
5. **Intrinsic reward as alignment signal**: Instead of RLHF preference labels (implicit), encoding moral principles directly as explicit reward functions creates interpretable, auditable alignment training signals — a design principle for future benchmark-aligned fine-tuning.
6. **Time-step state design**: Using the opponent's last action as the agent state creates a minimal but morally rich decision context. A benchmark for LLM moral reasoning could use similarly minimal but information-sufficient contexts.

## 12. Notable quotes
- "Moral alignment among humans is not a solved problem, there is a lack of high-quality training datasets." (p.2)
- "Fine-tuning model weights may merely create a 'safety wrapper' on otherwise unaltered core models, making the effects of safety-focused fine-tuning easily reversible." (p.9, citing Jain et al., 2023)
- "The moral preferences of the target audience of any AI system will vary depending on their cultural and political norms — in this paper, we did not aim to promote any one moral framework, but instead demonstrated the ways in which different moralities can be implemented using the same methodology of intrinsic rewards." (p.24)
- "Quantifying morality by translating complex moral frameworks into elementary reward functions, learning constraints or textual principles is certainly a simplification of reality. Nevertheless, the original moral philosophical frameworks discussed in this work might be seen as a form of abstraction and, in a sense, simplification of the complex and multi-faceted human condition." (p.23)

## 13. UNKNOWN / not in extract
- Exact experimental results from Tennant et al. (2023) (referenced but not reproduced here)
- Detailed results from the LLM fine-tuning case study (Tennant et al., 2024b) beyond general description
- Whether the paper was peer-reviewed at a specific venue (posted as arXiv:2312.01818v3)
- Definitions section (p.25+) was not read — may contain additional technical content
