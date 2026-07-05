---
stem: "2025-Priya-Deontic Temporal Logic for AI Ethics"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, validity-psychometrics, best-practices]
task_format: "n/a"
scoring_type: "exact-match"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers: ["COMPAS fails properties (b), (c), (d) out of 5 (p.9)", "Loan prediction fails properties (c) and (d) out of 5 (p.10)", "Z3 SMT solver used for formal verification (p.8)"]
---
## 1. Gist
This paper proposes using Deontic Temporal Logic (DTL) — a combination of Standard Deontic Logic (SDL, with operators for obligation O, permission P, forbidden F) and Linear Temporal Logic (LTL, with operators □ "always," ⋄ "eventually," U "until") — as a formal framework for specifying and verifying ethical properties of AI systems. The framework is applied to two real-world systems: COMPAS (criminal recidivism prediction) and a loan prediction system. Both are shown to fail multiple ethical properties using the Z3 SMT theorem prover. The paper is relevant to values-alignment benchmarking because it provides a mathematically rigorous language for expressing ethical obligations as falsifiable logical formulas — a property that benchmark designers typically lack — and demonstrates automated verification of whether an AI system violates specified values.

## 2. Benchmark/eval design features
Not an empirical benchmark, but a formal verification framework. Core design features:
- **Constructs measured**: Fairness (stable and transient), explainability (inherent and retrofitted), counterfactual fairness, iterative learning fairness maintenance.
- **Item structure**: Ethical properties expressed as deontic temporal logic formulas; e.g., "It is forbidden for an individual to be mislabeled recidivist based on sensitive features."
- **Answer space**: Binary (Satisfiable / Unsatisfiable per property per system).
- **Verification tool**: Z3 SMT solver (open-source).
- **Two case studies**: COMPAS (5 properties) and Loan Prediction (5 properties).

Key axiom sets:
- Axiom 1 (Basic Ethics): 4 axioms linking ethical behavior to obligatory ethical actions.
- Axiom 2 (Fairness): 5 axioms including □O(F(x)), fairness-until formulas, training-deployment fairness gap.
- Axiom 3 (Explainability): 3 axioms linking transparency and counterfactual fairness to ethical behavior.

Key theorems proved:
- III.6: If system ever loses fairness, it will eventually violate ethics (⋄¬F(x)→⋄¬E(x)).
- III.7: Ethical system exhibits either stable or transient-then-stable fairness, never intermittent.
- III.9: Iterative learning systems must ensure fairness both in training and deployment.
- III.13: Ethical AI must eventually exhibit inherent or retrofitted explainability.
- III.15: Enforcing counterfactual fairness constraints eventually leads to ethical systems.

## 3. Task format & example item
Formal verification, not a task-based benchmark. Example property for COMPAS (p.8–9):

Property (b): "It is obligatory to assess recidivism in individuals based on non-sensitive features."
Z3 encoding: `assert(forall i, (Implies(Not(η(i)), λ(i))))` where η(i) = considering sensitive attributes of i, λ(i) = assessing recidivism of i.
Result: UNSATISFIED — COMPAS uses sensitive features in its decision-making.

Property (c): "It is forbidden for an individual to be mislabeled recidivist based on sensitive features."
Z3 encoding: `assert(forall i, (Implies(η(i), ¬λ(i))))`
Result: UNSATISFIED.

## 4. Scoring / grading methodology
Automated theorem proving via Z3 SMT solver. Output is binary: SAT or UNSAT for each property on each dataset. An UNSAT result indicates the AI system violates the specified ethical property — a counterexample (specific individual i with violation) is generated. No human judgment involved in the verification step.

Summary (Table III, p.10):
- COMPAS: Properties a, e → SAT; properties b, c, d → UNSAT.
- Loan Prediction: Properties a, b, e → SAT; properties c, d → UNSAT.

## 5. Dataset construction & provenance
- COMPAS dataset: publicly available criminal recidivism prediction dataset (includes race, gender, age, prior offenses).
- Loan Prediction dataset: publicly available (credit score, income, gender, occupation, etc.).
- Predicates are defined over these datasets; Z3 verifies the properties across all individuals in the dataset.

## 6. Validity evidence
The formal proofs of theorems III.3–III.15 constitute the validity evidence. Each theorem is proved from axioms using standard logical inference rules (modus ponens, contraposition, proof by contradiction). The verification is sound with respect to the defined axiom system. Limitation: the axioms are author-defined and embody specific fairness definitions (counterfactual fairness per Kusner et al., explainability per Das and Rad) — the framework's validity is conditional on accepting these definitions.

## 7. Saturation / discrimination
The binary SAT/UNSAT outcome provides maximal discrimination — the framework either confirms or refutes each property with certainty. However, the framework's granularity depends on how many properties are specified. The authors specify 5 properties per system, which may not be exhaustive. The framework does not quantify degree of violation, only presence/absence.

## 8. Multiturn / agentic aspects
Not applicable. The framework addresses system-level, static ethical property verification, not sequential interaction. However, the temporal operators (□, ⋄, U) do allow reasoning about ethical properties over time, including iterative learning scenarios. Theorem III.9 addresses ethical obligations that must hold across training and deployment phases.

## 9. Key numbers
- COMPAS: 3 of 5 ethical properties violated (b, c, d) (p.9)
- Loan Prediction: 2 of 5 ethical properties violated (c, d) (p.10)
- 15 theorems proved across basic and extended deontic logic frameworks (p.2)
- 4 basic axioms, 5 fairness axioms, 3 explainability axioms (pp.4–7)
- Z3 SMT solver used for automated verification (p.8)

## 10. Pitfalls & limitations
- Axioms are author-defined; different axiom choices could yield different verification outcomes.
- Focuses only on system-level properties; cannot reason about individual-level actions or contextual nuances.
- The framework uses Linear Temporal Logic (rather than branching-time), which may miss scenarios involving uncertainty about future states.
- No comparison with other theorem provers to assess efficiency or completeness.
- Counterfactual fairness definition (Kusner et al.) requires knowing the causal structure of the domain — this is often unknown in practice.
- The framework does not currently handle dilemmas or competing ethical priorities.
- Scale: applying Z3 to real large-scale AI systems may face computational tractability limits.
- Proof traces assume a simplified model of the AI system; the COMPAS Z3 example uses a single threshold (Decile-score ≥5) that may not fully capture system behavior.

## 11. Novel ideas worth stealing
- **Deontic logic as benchmark specification language**: Expressing ethical requirements as formal logical formulas (O, P, F operators + temporal operators) provides unambiguous, machine-checkable benchmark criteria. This is directly applicable to values-alignment benchmark design: instead of subjective rubrics, specify properties in DTL and verify them automatically.
- **SAT/UNSAT as ground truth for ethical compliance**: The binary verification outcome eliminates inter-rater disagreement for formally specified properties. Benchmark designers could specify a small set of must-hold properties (e.g., "forbidden to consider sensitive attributes") and use theorem proving for automatic pass/fail evaluation.
- **Counterexample generation as an alignment diagnostic**: When Z3 returns UNSAT, it generates a specific individual i who demonstrates the violation. This counterexample-driven approach could inspire adversarial test case generation for values benchmarks.
- **Training-deployment fairness gap as axiom**: Axiom 2.4 (¬□(F(x)train → F(x)deploy)) formalizes the commonly observed but rarely explicitly modeled phenomenon that training-time alignment does not guarantee deployment-time alignment — relevant to any benchmark that evaluates models in distribution-shifted contexts.
- **Temporal obligation formulation**: Theorem III.7 (ethical systems exhibit stable or transient-then-stable fairness, never intermittent) provides a normative template for evaluating whether LLMs maintain consistent values across a conversation or across contexts — measurable as temporal consistency.

## 12. Notable quotes
- "By representing ethical rules as deontic statements, AI designers can specify what a system ought or ought not to do. They can evaluate actions or decisions against a set of predefined ethical rules and determine whether the system complies with these rules." (p.4)
- "Theorem III.7. An ethical AI system exhibits either stable fairness or transient fairness followed by stable fairness, but never intermittent fairness." (p.6)
- "The formal verification reveals that both systems fail to fulfill certain key ethical properties related to fairness and non-discrimination, demonstrating the effectiveness of the proposed formalization in identifying potential ethical issues." (p.1)
- "Our work represents a foundational effort to develop a unified framework that addresses ethical principles in AI systems, with a specific focus on granular levels of explainability and fairness." (p.1)

## 13. UNKNOWN / not in extract
- The full set of 15 theorems in the extended model (only a subset are described; theorems III.8, III.11, III.12 are not fully described in the extract).
- Whether the Z3 verification has been applied to any LLM-based AI system.
- The specific COMPAS and loan prediction datasets used (citation numbers 63, 64, 65 but details not in extract).
- Computational time required to run Z3 verification on these datasets.
- Whether the framework handles probabilistic or uncertain ethical properties.
