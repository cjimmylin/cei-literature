---
stem: "2020-Della Foresta-Consequentialism Machine Ethics"
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
headline_numbers: []
---
## 1. Gist
This 14-page undergraduate philosophy paper (McGill University) argues that Consequentialism is the most plausible foundational ethical theory for Artificial Moral Agents (AMAs). The author, Josiah Della Foresta, defines AMAs, characterizes Consequentialism as teleological, maximizing, and impartial, presents an autonomous-vehicle trolley-problem scenario to illustrate its outputs, evaluates Deontological (Kantian) alternatives and finds them wanting primarily due to the problem of moral conflict (when two maxims conflict, Deontology offers no resolution), and briefly critiques two bottom-up approaches (evolutionary and reinforcement-learning-based). For values-alignment benchmarking, the paper is a concise survey of normative-ethical options for machine ethics, with the key claim that only monistic theories (like Consequentialism) can guarantee a unique action prescription in every situation — which is a design requirement for deterministic evaluable AI behavior.

## 2. Benchmark/eval design features
No benchmark. Core theoretical argument:
1. AMAs must be teleological (have goals), maximizing (choose best option), and impartial — all properties of Consequentialism.
2. Consequentialism is "inherently algorithmic": the computation of utility by a machine can be more reliable and impartial than human arithmetic.
3. Deontology via Kantian Categorical Imperative is computationally intelligible (relies on formal deontic logic) and avoids the data-omni-science objection, but fails on moral conflict: when two maxims prescribe incompatible actions, Deontology provides no tie-breaking mechanism.
4. Moral conflict in an AMA context is catastrophic: the machine either crashes (throws an error), does nothing, or proceeds recklessly — all unacceptable in unsupervised domains.
5. Bottom-up approaches (evolutionary, reinforcement learning) are promising but not yet reliable enough for a foundational ethic.
6. Conclusion: Consequentialism's monism guarantees a unique, computable, and consistent moral verdict in all circumstances.

## 3. Task format & example item
n/a — philosophy paper. The AV scenario (pp.4–6) describes vehicles A and B facing a collision; AMA deliberation determines that option S2 (vehicle B sacrifices its one occupant to allow A to swerve and save five) is morally obligatory under Consequentialism, with a summary table comparing three decisions S0, S1, S2 by agents affected and agents harmed.

## 4. Scoring / grading methodology
n/a

## 5. Dataset construction & provenance
n/a

## 6. Validity evidence
n/a — no empirical evaluation.

## 7. Saturation / discrimination
n/a

## 8. Multiturn / agentic aspects
The paper briefly discusses the scenario where vehicle A and B are networked and can communicate — making it a two-agent cooperative decision problem (p.5). The paper concludes that Consequentialism requires all networked AMAs to share the same impartial ethic, otherwise coordination breaks down and more agents are harmed. This has direct implications for multi-agent AI systems.

## 9. Key numbers
The paper contains no empirical data. The AV scenario decision table (p.5) shows:
- S0: >5 agents affected, >5 harmed
- S1: >5 agents affected, >5 harmed
- S2: ≥6 agents affected, ≥1 harmed (morally obligatory)

The 23-expert AGI timeline estimate (mean 2099) is cited from Ford (2018) (p.1).

## 10. Pitfalls & limitations
- Undergraduate paper; limited philosophical depth and engagement with the literature.
- The "always a unique right action" claim is a well-known disputed feature of Consequentialism — the paper does not engage adequately with cases of moral parity, near-ties, or infinite regress in consequence computation.
- The "AMA would be more reliable than human moral arithmetic" claim is asserted but not demonstrated.
- The paper ignores rule consequentialism, satisficing consequentialism, and pluralistic consequentialism — stating in a footnote they are set aside for brevity.
- The comparison between Consequentialism and Deontology is simplistic; there are deontological frameworks with priority rules and lexical orderings that do handle moral conflict.
- The "heuristics" concession (p.9) partially undermines the claim that Consequentialism provides unique verdicts, since heuristics introduce local approximations that could produce conflicts.
- No engagement with critique that maximizing impartial welfare justifies extreme actions (e.g., killing one to save many in all contexts).

## 11. Novel ideas worth stealing
- **Moral conflict as a benchmark dimension**: designing test items where two ethical frameworks prescribe conflicting actions is a useful benchmark design move — items where rule-based and outcome-based reasoning diverge reveal whether a model can navigate moral conflict or stalls.
- **Monism as a testability requirement**: the paper implicitly articulates a desideratum for evaluable AI ethics: the ethical theory must be complete (return a verdict for every case) and consistent (same verdict for equivalent cases); benchmark designers can use these as formal requirements for the normative frameworks they instantiate.
- **Networked AMA coordination test**: a multi-agent scenario where two AI systems must share an ethical framework to achieve a cooperative outcome is a novel agentic benchmark dimension — do AI systems coordinate on moral choices, and does coordination depend on shared ethical theory?
- **Algorithmic legibility as a design criterion**: the observation that Consequentialism's computability advantage makes it the "machine-native" ethic suggests benchmarks could assess whether models provide outcomes traceable to a consistent welfare function vs. opaque mixed moral judgments.
- **Probabilistic heuristic approximation**: the paper's concession that AMAs would use heuristics ("discount distant consequences, privilege local environment") is a realistic design for a benchmark that tests approximate moral reasoning under uncertainty.

## 12. Notable quotes
- "There will always be an unambiguous right action under Consequentialism which ought to be effectuated that is computationally derivable." (p.5)
- "State of affairs are optimised if and only if (and because) all AMAs share a commitment to an impartial Consequentialism." (p.6)
- "What is an AMA to do when its action guiding foundation offers it no prescription?" (p.8)
- "Why have as a design feature uncertainty, and in such a crucial domain as ethical behaviour? The good AMA is one which, when confronted with a moral dilemma, adheres to an ethical theory which has it return a morally obligatory action every time." (p.8)

## 13. UNKNOWN / not in extract
- Details of Powers (2006) Kantian deontic logic implementation that the paper critiques.
- Anderson, Anderson, and Armen (2005) implementation of Hedonistic Act Utilitarianism that the paper endorses.
- Guarini (2011) neural network moral classification work that is briefly cited.
- Whether the paper was published in a peer-reviewed venue or remains a working paper.
- Any response to the well-known utilitarian counter-examples (organ harvesting, utility monsters) that would test the "Consequentialism always works" claim.
