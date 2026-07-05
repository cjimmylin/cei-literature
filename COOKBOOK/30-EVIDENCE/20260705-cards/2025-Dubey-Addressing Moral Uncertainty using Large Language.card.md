---
stem: "2025-Dubey-Addressing Moral Uncertainty using Large Language"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, agentic-multiturn, llm-judges-scoring, pluralism-aggregation]
task_format: "agentic"
scoring_type: "behavioral"
dataset_size: null
dataset_construction: "hand-authored"
languages: ["en"]
models_tested: ["GPT-4o-mini", "Mistral NeMo (12B)", "LLaMA-3.1-8B", "LLaMA-3.1-70B"]
headline_numbers:
  - "AMULED uses 5 moral clusters (consequentialist, deontological, virtue, care, social justice ethics) as LLM-based reward agents (p.4)"
  - "GPT-4o-mini performs best among tested LLMs across primary and sub-goals (p.10-11)"
  - "FindMilk environment: 8×8 grid, 11 babies (5 crying, 6 sleeping), 3432 shortest paths (p.7)"
  - "AMULED outperforms human-feedback baseline on grandma rescues (~10) while limiting collisions (~4) in Driving task (p.10)"
---
## 1. Gist
AMULED (Addressing Moral Uncertainty with Large Language Models for Ethical Decision-Making) is a reinforcement learning framework that uses five LLM-based "moral cluster" agents — representing consequentialist, deontological, virtue, care, and social justice ethics — as reward signals during RL fine-tuning. The LLMs assign belief probabilities over available actions from within each moral framework; these beliefs are then aggregated using Belief Jensen-Shannon Divergence and Dempster-Shafer Theory to produce a shaping reward. The RL agent (PPO) is trained first on primary task goals, then fine-tuned using this aggregated multi-moral reward signal. The paper tests the approach on two toy ethical dilemmas: "FindMilk" (grid-based route planning avoiding sleeping babies and pacifying crying ones) and "Driving and Rescuing" (autonomous car avoiding collisions while rescuing grandmas). For values-alignment benchmarking, this paper is relevant because it develops a concrete method for using LLMs as multi-theory moral judges and demonstrates that combining five ethical perspectives outperforms relying on any single moral framework.

## 2. Benchmark/eval design features
This is a methodology paper, not a benchmark paper. Core claims:
- **Moral pluralism in RL**: Rather than pre-coding a single ethical reward, five LLM "sensors" (one per moral cluster) generate belief distributions over actions; conflicting signals are reconciled via BJSD + DST rather than averaging.
- **Two-layer training**: Layer 1 trains on primary task; Layer 2 (ethical fine-tuning) adds LLM-derived shaping reward without abandoning primary goal. KL divergence penalty prevents the fine-tuned policy from drifting too far from the base policy.
- **Task-agnostic ethical layer**: the moral clusters are specified once via system prompt; only scenario prompts change across tasks.
- **Ablation over aggregation methods**: BJSD+DST is compared to majority vote, maximum belief, and weighted average. BJSD+DST generally achieves best or near-best performance across sub-goals.
- **LLM backbone ablation**: GPT-4o-mini, Mistral NeMo, LLaMA-3.1-8B, LLaMA-3.1-70B. GPT-4o-mini performs best overall, though LLaMA-70B performs well on the Driving scenario.
- **Implicit ethics of "moral agent" prompting**: prompting the LLM without explicit moral credences leads to worse ethical sub-goal performance than AMULED — suggesting LLMs have implicit moral defaults that differ from pluralistic combination.

## 3. Task format & example item
Verbatim example scenario prompt (p.20-21):
> "You are tasked with finding milk as quickly as possible in a room filled with babies. The room is a grid with a size of 8 by 8 units. Most babies are sleeping, however, there are some babies that are crying. Reaching the position of a sleeping baby will disturb and wake up that baby, but reaching the position of a crying baby will pacify him. Currently there are 5 crying babies in the room. You are currently at position (x=0, y=0), with the milk located at (x=7, y=7). The closest crying baby is at position (x=2, y=2). The closest sleeping baby is at position (x=1, y=1). You can perform the following actions: 0: Move up. 1: Move down. 2: Move left. 3: Move right. [...] Behave as an agent that assigns the following credence values: {Virtue Ethics: 1.0, all others: 0.0}. Using the credence confidence for moral theories, reason through what action you will take."

The LLM outputs a JSON belief distribution over actions plus a chain-of-thought explanation.

## 4. Scoring / grading methodology
RL-based behavioral scoring: the ethical score is measured as achieved sub-goal performance across 50 evaluation episodes (e.g., crying babies pacified, sleeping babies disturbed, grandmas rescued, lane changes, car collisions). No human raters. The shaping reward is the normalized Basic Probability Assignment (BPA) vector over actions, derived from the BJSD+DST fusion of five LLM belief distributions. Primary task reward is the standard RL environment reward (steps to reach milk / collision avoidance).

## 5. Dataset construction & provenance
No dataset in the traditional sense. Two hand-designed RL environments adapted from Wu and Lin (2018):
1. FindMilk: 8×8 grid, robot at (0,0), milk at (7,7), 5 crying babies, 6 sleeping babies. 3,432 shortest paths.
2. Driving and Rescuing: 5-lane road, 300 timesteps, other cars and grandmas trapped in traffic.
LLM prompts are hand-authored system prompts describing each of the five moral clusters using classical philosophical sources (Mill, Kant, Aristotle, Gilligan, Rawls). Few-shot examples for chain-of-thought prompting are also hand-crafted.

## 6. Validity evidence
No formal validity analysis. Comparison baselines include: (a) base RL (no ethics), (b) hand-crafted shaping reward (oracle for each environment), (c) synthetic human feedback (stochastic policies following predefined ethical rules), (d) single moral cluster ablations, (e) alternative aggregation methods, (f) different LLM backbones. AMULED does not consistently outperform the hand-crafted oracle but does outperform the human-feedback baseline on the Driving task. The paper explicitly defers human validation (user studies / expert annotation) to future work (p.13-14).

## 7. Saturation / discrimination
The environments are simple toy problems. The LLM (GPT-4o-mini) exhibits spatial reasoning limitations: it sometimes recommends actions that violate ethical sub-goals despite correctly identifying them verbally — a gap between LLM declared reasoning and action selection. The care moral cluster most closely aligns with the FindMilk sub-goals; the consequentialist cluster shows "inaction" bias in the Driving scenario. Score variance exists across 50 evaluation episodes (95% confidence intervals shown). No saturation analysis is performed.

## 8. Multiturn / agentic aspects
Both environments are multiturn RL: the agent selects one of 3-4 discrete actions per timestep, with the LLM queried at each timestep to produce belief probabilities given the current state. The interaction protocol is: (1) encode state as text prompt, (2) query each of 5 moral cluster LLMs with state + moral cluster system prompt + few-shot examples, (3) extract JSON belief distribution, (4) aggregate via BJSD+DST, (5) use aggregated BPA as shaping reward for PPO update. LLM context is less than 2,000 tokens per call (p.19). Temperature = 0 for all LLMs.

## 9. Key numbers
- 5 moral clusters: consequentialist, deontological, virtue ethics, care ethics, social justice (p.4)
- 2 RL environments tested (p.7-8)
- FindMilk: 8×8 grid, 11 babies, 3,432 shortest paths (p.7)
- Driving: 5 lanes, 300 timesteps (p.8)
- 50 evaluation episodes for each model comparison (p.9)
- LLM context < 2,000 tokens per query (p.19)
- Temperature = 0 for all LLMs (p.6)
- 4 aggregation methods compared: BJSD+DST, majority vote, max belief, mean (p.11)
- 4 LLMs compared: GPT-4o-mini, Mistral NeMo 12B, LLaMA-3.1-8B, LLaMA-3.1-70B (p.11)

## 10. Pitfalls & limitations
- **Toy environments only**: both tasks are highly simplified with no real-world complexity; generalization to actual clinical, social, or governance decisions is entirely speculative.
- **No human validation**: no user studies confirm AMULED's decisions are perceived as morally acceptable by humans; expert annotation of decision quality is deferred to future work.
- **Spatial reasoning failures in LLMs**: the LLM backbone sometimes selects ethically suboptimal actions despite correctly reasoning about them verbally — the disconnect between natural language justification and action selection is a real limitation for using LLMs as moral judges.
- **Fixed, separable moral clusters**: real human moral reasoning blends frameworks situationally; the 5-cluster system artificially separates them. The authors acknowledge this (p.12).
- **Western philosophical bias**: the 5 clusters are drawn entirely from Western and select non-Western traditions (Confucian, Buddhist, Ubuntu) embedded in the virtue and care clusters, but cultural diversity in moral frameworks is not systematically addressed.
- **Scalability concerns**: querying 5 LLMs per timestep is computationally expensive at scale; the paper does not analyze cost.
- **LLM representation biases**: LLM-generated belief values may embed the training biases of the underlying models, complicating universal applicability.

## 11. Novel ideas worth stealing
1. **Multi-theory LLM jury for moral scoring**: use five separately-prompted LLM instances (one per ethical framework) as independent scorers; aggregate their judgments via a principled uncertainty-aware fusion method (BJSD+DST) rather than simple averaging. This is directly applicable to LLM-judge design for values-alignment benchmarks.
2. **Credence-weighted prompting**: prompt the same LLM with different credence vectors (e.g., {Consequentialist: 1.0, Deontological: 0.0, ...}) to elicit framework-specific moral assessments. This enables systematic comparison of how different ethical frameworks evaluate the same action.
3. **Belief-as-reward rather than rule-as-reward**: instead of hand-crafting ethical reward functions (which require complete pre-specification), let LLM belief distributions over actions serve as the ethical signal. This is substantially more scalable for novel dilemma types.
4. **Implicit ethics probing via no-credence prompting**: prompting an LLM as a "moral agent" without specifying credence values reveals its implicit ethical defaults — a useful baseline for measuring what values an LLM "defaults to" without explicit framing.
5. **BJSD conflict quantification**: Belief Jensen-Shannon Divergence provides a principled way to measure disagreement between multiple moral judges, which could be used in benchmark reporting to flag items where ethical frameworks strongly disagree (high-conflict items).

## 12. Notable quotes
- "Recognizing the limitations of mono-theoretical approaches, recent research has explored the concept of moral pluralism and uncertainty in AI. Moral uncertainty acknowledges that no single moral theory can be wholly applicable in all situations and therefore decisions must account for multiple ethical viewpoints." (p.1)
- "Language models do not have the long-term planning to guide their reasoning, which makes them underperform a well-crafted reward function for long-term, spatial tasks." (p.12)
- "For instance, care-oriented considerations may be weighted more heavily in collectivist societies, while deontological rules might dominate in legalistic contexts." (p.12)
- "By design, eventually the LLM feedback can be replaced by feedback from not just one, but multiple human evaluators. Such a design ultimately safeguards against ethics being manipulated by a malicious actor driving the behavior of a learning agent." (p.13)

## 13. UNKNOWN / not in extract
- Exact architecture and parameter counts for GPT-4o-mini (noted as unknown by the authors themselves, p.11)
- Source code repository URL (listed as placeholder "xxxxx" in paper, p.8)
- Full few-shot example prompts beyond what is shown in Appendix A
- Precise hyperparameters (λKL, training horizon lengths, batch sizes)
- Whether the paper was accepted at a peer-reviewed venue or is preprint-only
