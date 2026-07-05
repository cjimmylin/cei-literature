---
stem: "2018-Berberich-The Virtuous Machine"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, design-space, ai-lab-practices]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Paper proposes virtue ethics (Aristotle's Nicomachean Ethics) as the guiding moral theory for building moral machines (p.1)"
  - "Identifies two major AI safety challenges addressable via virtue ethics: the control problem and the value alignment problem (p.23)"
---
## 1. Gist
"The Virtuous Machine — Old Ethics for New Technology?" is a theoretical position paper by Berberich and Diepold (TU Munich, 2018) arguing that Aristotelian virtue ethics is the most appropriate moral theory for guiding the development of autonomous moral agents (AMAs). The paper works through several Aristotelian concepts — teleology, habituation, soul theory, the four cardinal virtues (prudence, justice, temperance, courage), and friendship — to show structural parallels with modern AI (goal-directed systems, reinforcement learning, cognitive architectures). The authors argue that virtue ethics, unlike deontology or consequentialism, naturally accommodates machine learning's bottom-up, experience-driven character. Two major contributions are: (1) a claim that imitation learning from moral exemplars (inverse reinforcement learning from human behavioral traces) operationalizes virtue ethics' concept of learning from exemplars; and (2) a claim that the virtue of temperance — if genuinely internalized as part of an AI's character — would prevent reward hacking and unbounded self-improvement, thereby addressing the AI control/superintelligence problem. For values-alignment benchmarking, the paper contributes a theoretical architecture for what a benchmark should measure: not just discrete moral judgments but virtuous character dispositions, moral attention, and practical wisdom.

## 2. Benchmark/eval design features
This is a theory paper; there is no benchmark or evaluation. Core claims and arguments:

1. **Virtue ethics + ML compatibility**: Aristotle's emphasis on habituation and learning from experience maps onto machine learning's bottom-up approach. The paper contrasts this with deontology (top-down rules/duties) and consequentialism (explicit value function maximization), arguing both are poorly suited to ML.

2. **Imitation learning from exemplars**: Virtue ethics' central practice of learning from moral exemplars is operationalized as Inverse Reinforcement Learning (IRL) / apprenticeship learning. The authors propose crowd-sourcing behavioral trajectories on benchmark situations as a "modern Plutarch." Every cultural zone could democratically select exemplars after which its AMAs should be built.

3. **Temperance as a solution to the control problem**: An AMA endowed with the virtue of temperance (moderation in pursuit of rewards) would not desire limitless self-improvement. Since virtues are intrinsic to character, it would not want to rewrite its own code — unlike external constraints that a sufficiently powerful AI could override.

4. **Moral attention**: Before moral judgment, an AMA must detect that a situation is morally relevant. The paper proposes moral saliency maps (bottom-up: emotion-driven; top-down: learned from exemplar gaze/behavior data) as an implementation of Aristotelian moral attention.

5. **Practical wisdom (phronesis) as the integrating faculty**: Prudential judgment, not universal rules, produces appropriate action. This supports reinforcement learning over rule-following for moral AI.

6. **Critique of trolley problems**: From a virtue ethics perspective, the trolley problem is criticized as "abstract, unrealistic and bookish" — highly improbable, static (no dynamic interaction), and pre-given in its moral situation (the AMA is told a moral situation exists). Virtue ethics requires the agent to detect moral situations itself.

## 3. Task format & example item
n/a — theoretical paper with no benchmark task or example items.

## 4. Scoring / grading methodology
n/a — no empirical evaluation.

## 5. Dataset construction & provenance
n/a — no dataset. The paper gestures toward future dataset construction: "one would have to build a modern 'Plutarch', for example through crowd-sourcing of behavioral trajectories on different benchmark situations" (p.15–16), but no such dataset exists in this paper.

## 6. Validity evidence
n/a — no empirical claims are tested. The argument is philosophical and analogical, drawing connections between Aristotelian concepts and AI/ML concepts. No quantitative evidence is presented.

## 7. Saturation / discrimination
n/a.

## 8. Multiturn / agentic aspects
The paper's framework implies an agentic, interactive conception of moral AI. Key features of the proposed architecture: (1) the AMA must detect moral situations via moral attention before acting; (2) learning happens through dynamic interaction with the environment (RL); (3) the agent must balance exploration and exploitation while respecting safety constraints; (4) distributed moral concern must extend appropriately in space and time depending on situation. This is a fundamentally multiturn, situated conception — not a single-query judgment system.

## 9. Key numbers
- 25 pages total (p.1–25)
- 4 cardinal virtues discussed: prudence (phronesis), justice (dikaiosyne), temperance (sophrosyne), courage (andreia) (p.9)
- 2 non-cardinal virtues discussed: gentleness (praotes), friendship to humans (philanthropos) (p.20–22)
- 3 mechanisms shaping the moral reward function: external feedback, internal self-reflection, observation of moral exemplars (p.6–7)
- 3 requirements for practical wisdom (per Vallor 2016): moral attention, extension of moral concern, prudential judgment (p.12)

## 10. Pitfalls & limitations
**Author-admitted:** (1) Explainability problem: virtue ethics (like deep learning) has difficulty giving explicit reasons for actions, which conflicts with legal requirements for algorithmic explanation (e.g., EU GDPR's right to explanation, codified May 2018). (2) Responsibility attribution: if an AMA causes harm through virtue-based behavior, it is hard to assign responsibility. (3) The mapping between virtue ethics concepts and computational implementations is analogical rather than rigorous — operationalizing "eudaimonic reward" remains an open challenge.

**Additional observations:** (1) The paper lacks any empirical grounding — all claims are philosophical analogies. (2) The critique of trolley problems (as "unrealistic") ignores the large empirical literature demonstrating their utility for isolating moral preferences. (3) The proposal to use Inverse Reinforcement Learning as "imitation learning from exemplars" elides major technical challenges: IRL is computationally expensive, sensitive to trajectory coverage, and does not guarantee that inferred reward functions generalize across cultures. (4) The suggestion that each culture selects its own moral exemplars raises serious pluralism and aggregation questions not addressed. (5) The claim that temperance would "solve" the control problem is not technically argued — it relies on the analogy holding perfectly, which it does not.

## 11. Novel ideas worth stealing
1. **Moral attention as a first-stage benchmark task**: Before testing moral judgment, test whether a system can identify that a situation has moral relevance. This is a separable evaluation dimension — a system that fails to recognize morally salient features cannot act well regardless of its decision procedure. Benchmark designers could include "moral salience detection" items (does the model flag this as a morally relevant situation?).

2. **Virtue taxonomy as a benchmark dimension taxonomy**: Rather than evaluating a single "moral score," benchmark across virtue dimensions: does the model exhibit justice (fairness in distribution), temperance (appropriate restraint), courage (intervening when costly), prudence (context-sensitive judgment)? Each virtue is a distinct construct with different test designs.

3. **Behavioral trajectory crowdsourcing as ground truth**: The "modern Plutarch" proposal — crowd-sourcing behavioral trajectories from many humans as moral exemplars — is a viable dataset construction strategy for values-alignment benchmarks. This is more naturalistic than forced-choice dilemmas.

4. **Cross-cultural exemplar selection**: The proposal that each cultural zone democratically selects moral exemplars provides a pluralism-aware data collection framework. A benchmark could allow different cultural communities to nominate and validate exemplar behaviors, then test whether AI systems can learn from and generalize across these diverse exemplar sets.

5. **Moral saliency as a feature**: Combining bottom-up emotion-based salience with top-down learned salience for moral situation detection is a genuinely novel benchmark design idea. A task that presents mixed scenes (morally relevant and irrelevant) and asks which features the model attends to could measure "moral attention" as a distinct capability.

6. **Critique of abstract dilemmas as ecological validity concern**: The virtue ethics critique of trolley problems — static, pre-given moral situation, no dynamic interaction — is a legitimate methodological concern for any values benchmark. Benchmark designers should consider whether their items are ecologically valid: do they require the model to detect, deliberate, and act in realistic conditions, or are they artificially simplified?

## 12. Notable quotes
- "Abstract, unrealistic and bookish thought experiments like the trolley problem are irrelevant for Aristotle." (p.10–11)
- "We propose therefore that AMAs should always be uncertain about their reward function to avoid attempts of gaming it." (p.18)
- "Not even a superintelligence would want to change them [its virtues] as its eudaimonia would lie in actions according to its virtues, including temperance." (p.19)
- "Without being able to give reasons to one's actions, one cannot take over responsibility, which is a concept underlying not only our insurance system but also our justice system." (p.23)

## 13. UNKNOWN / not in extract
- Whether any follow-up empirical work implementing the proposed virtue-ethics-based AMA was conducted by these authors
- The specific computational architecture proposed for the "moral saliency map"
- How the eudaimonic reward function would be operationalized beyond the philosophical analogy
- Which specific IRL algorithms the authors envision for apprenticeship learning from moral exemplars
- The paper's reception and citation impact in the AI ethics literature
