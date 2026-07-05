---
stem: "2020-Akrout-Machine Ethics - Creation of a Virtuous Machine"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, ai-lab-practices, design-space]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers: []
---
## 1. Gist
This short position paper (4 pages) argues that Virtue Ethics has been unjustifiably neglected in machine ethics in favor of outcome- and action-based frameworks (Utilitarianism, Deontology). The authors, Akrout and Steinbauer, propose a modified AI training framework that integrates Virtue Ethics by extending Doran et al.'s explainability framework with a second training step in which explainable deductions are fed back as contextual training data. The goal is for the machine to learn policies dependent on virtuous character-trait-like features, not merely correct outputs. For values-alignment benchmarking, the paper is relevant as a design-space survey arguing that current approaches miss agent-level character evaluation, and it sketches what a benchmark that assesses whether a model's decisions reflect virtuous reasoning (rather than just correct outputs) might require.

## 2. Benchmark/eval design features
No benchmark. Core theoretical claims:
1. Current AI ethics work focuses on outcome-based (Utilitarian) or rule-based (Deontological) frameworks and neglects virtue-ethical agent-based evaluation.
2. Virtue ethics asks: "What kind of person (agent) should I be?" — good intentions must be paired with good acts (Zagzebski 2004); intentions alone are insufficient.
3. The authors propose a two-step modified training framework: (a) standard AI inference generates explainable deductions (using an existing XAI method); (b) a second training phase incorporates these deductions as contextual features, so the policy is conditioned on virtuous reasoning features rather than treating explainability as a post-hoc artifact.
4. This allows developers to verify that the model's feature attention resembles that of a virtuous agent, and enables auditable correction of unethical conduct.
5. The framework is illustrated with self-driving car examples (a license-testing scenario where context variables are fixed and varied to assess policy quality).

## 3. Task format & example item
n/a — theoretical paper only. The self-driving car example (p.3) discusses varying contextual inputs (e.g., image of a road scenario) to assess whether explainable variables correctly drive policy choice, but no benchmark items are provided.

## 4. Scoring / grading methodology
n/a

## 5. Dataset construction & provenance
n/a

## 6. Validity evidence
n/a — no empirical results presented.

## 7. Saturation / discrimination
n/a

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
No empirical numbers reported. The paper is entirely theoretical. One indirect quantitative claim: average AGI emergence prediction from 23 eminent AI experts was 2099 (p.1, citing Ford 2018).

## 10. Pitfalls & limitations
- The paper is very short (4 pages) and does not present any implementation or empirical evaluation of the proposed framework.
- The claim that explainable deductions can substitute for virtuous character features is asserted rather than demonstrated; the analogy between explainability methods and virtue traits is loose.
- The framework relies entirely on Doran et al. (2017), which is itself a conceptual proposal without implementation details for the virtue-extension step.
- Virtue ethics contains competing accounts (Aristotle, Confucius, Hume, Nietzsche) of which virtues matter; the paper does not specify which virtues or how to operationalize them.
- The observability problem: if humans cannot explain their own intentions (a point the paper acknowledges), it is unclear how a machine's feature attention can be reliably mapped to "virtue."

## 11. Novel ideas worth stealing
- **Agent-level vs. output-level evaluation**: evaluating whether a model's internal reasoning pathway reflects virtuous features (honesty, fairness, courage) rather than only whether its output is correct; this suggests a class of "process benchmarks" that inspect reasoning chains or chain-of-thought for virtue-like features.
- **Contextual training loop for ethical correction**: training a model on its own explainable deductions as context creates a feedback loop where ethical character shapes future policy; analogous to RLHF but grounded in virtue-ethical rather than preference criteria.
- **Audit-first evaluation design**: requiring that a model's reasoning is available for external audit before claiming ethical compliance; a benchmark could require models to produce auditable justifications alongside decisions.
- **The "good intentions + good acts" distinction**: benchmark items could separately assess whether a model produces good-sounding justifications and whether those justifications actually predict correct decisions — targeting sycophantic rationalization.
- **Cross-context consistency as virtue proxy**: checking whether a model's explanatory features remain stable when non-morally-relevant contextual variables are varied is a concrete operationalization of integrity as a virtue.

## 12. Notable quotes
- "Ignoring knowledge from the domain of Virtue Ethics will potentially result in flawed explicit moral agents who narrowly focus on outcomes and actions and neglect to include ethical metrics into the recursive policy learning process that shapes future AI decisions." (p.1)
- "This process is similar to a parent telling a child: 'don't do that because you may hurt someone' and not simply 'don't do that'." (p.2)
- "Only then can the source of unethical conduct be identified, understood, and corrected." (p.2)
- "One can verify whether the learned features are similar to those of a virtuous person, at least from an interpretability perspective." (p.2)

## 13. UNKNOWN / not in extract
- Details of Doran et al. (2017) explainability framework on which the proposal depends.
- Any empirical test or prototype implementation of the two-step training framework.
- Specific virtues proposed for operationalization (Aristotle's list is mentioned but no selection is made for AI context).
- How the framework handles conflicting virtues (analogous to deontological moral conflict, which the paper treats as a problem for rule-based systems but does not address for virtue systems).
