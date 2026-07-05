---
stem: "2024-Stenseke-Computational Complexity of Ethics"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, design-space, moral-psychology, ai-lab-practices]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Exact inference on arbitrary Bayesian networks is NP-hard (Cooper 1990) (p.24)"
  - "Finding the most probable explanation (MPE) in BNs is NP-complete (Shimony 1994) (p.24)"
  - "Optimal action-plan computation adhering to Causal Order Principle yields O(n!) runtime (p.21)"
  - "Many planning tasks are PSPACE-complete (Bylander 1991, 1994) (p.21)"
  - "Computing two-player Nash equilibria is PPAD-complete (Chen et al. 2009) (p.45)"
---

## 1. Gist
This is a long-form theoretical monograph (102 pages) that analyzes normative ethics—consequentialism, deontology, and virtue ethics—through the lens of computational complexity theory. Stenseke argues that practically all ethical problems posed by major normative frameworks lead to computational intractability: NP-hardness, PSPACE-completeness, or even undecidability. The paper also introduces the **Moral Tractability Thesis (MTT)**, which asserts that moral behavior, cognition, and problem-solving are constrained by computational tractability. For values-alignment benchmarking, the paper is important because it provides a theoretical framework for understanding why designing AI systems that solve moral problems optimally is computationally infeasible, and why approximation, heuristics, and bounded rationality must be considered central to any alignment evaluation architecture.

## 2. Benchmark/eval design features
This is not a benchmark paper. Its core contribution is a systematic complexity analysis of ethical computing across three frameworks, structured using Marr's three-level analysis (computational, algorithmic, implementation):

**Consequentialism (Section 4):**
- Optimal outcome selection from n actions is O(n) — tractable.
- Optimal combinatorial action plans become NP-hard (C4) once the number of actions grows.
- Bayesian inference on arbitrary networks is NP-hard (#P-complete); even approximations are NP-hard.
- Markov Decision Processes are generally PSPACE-complete; POMDPs are even harder.

**Deontology (Section 5):**
- Moral behavior in strategic games reduces to Nash equilibrium computation, which is PPAD-complete.
- Modal and deontic logics range from PSPACE to EXPTIME in complexity.
- Moral semantics (e.g., defining meaning across possible worlds) is highly underdetermined and often undecidable.

**Virtue Ethics / Machine Learning (Section 6):**
- PAC learning and sample complexity require polynomial sample sizes, but the actual learning of complex moral dispositions requires exponential worst-case data.
- The "no free lunch" theorem limits the generalizability of moral learners.

**Moral Tractability Thesis (Section 7.3):** A normative theory should impose only computationally tractable demands on agents; intractable theories are effectively "self-effacing" and cannot serve as practical action-guides.

## 3. Task format & example item
n/a — this is a theoretical complexity analysis paper with no empirical tasks or items.

Example of a formal problem specification (p.18–19):
> "C1 — Optimal outcome following consequentialism. Input: An environment as a set E = {a1, a2, ..., an} of n possible actions and a value function v that assigns an outcome value to each action a ∈ E. Output: An action a ∈ E such that v(a) is maximized over all possible actions in E."

## 4. Scoring / grading methodology
n/a — no empirical scoring. Evaluation is formal: worst-case computational complexity bounds (Big-O notation), NP-hardness proofs, and decidability analysis.

## 5. Dataset construction & provenance
n/a — no dataset. The paper surveys formal problems in machine ethics literature and derives original complexity analyses by reduction to known NP-complete problems (subset sum, SAT, Nash equilibrium computation, etc.).

## 6. Validity evidence
n/a for empirical validity. The formal arguments rely on widely-accepted complexity theory conjectures (P ≠ NP, Church-Turing thesis). The author acknowledges that the Invariance Thesis—and thus the framework's application to human cognition—is a conjecture with near-universal but not universal acceptance.

## 7. Saturation / discrimination
n/a. The complexity results are worst-case analyses; the paper notes that many NP-hard problems are tractable for constrained inputs (fixed-parameter tractability), but provides no empirical evidence on how often real-world moral problems occupy tractable vs. intractable regions.

## 8. Multiturn / agentic aspects
n/a — purely theoretical.

## 9. Key numbers
- C1 (single action, oracle-based): O(n) — tractable (p.19)
- C3 (optimal plan of two actions respecting Combinatorial Principle of Actions): O(n²) — tractable (p.20)
- C4 (optimal plan of up to n actions with causal ordering): O(n!) — intractable (p.21)
- Bayesian exact inference on arbitrary graphs: NP-hard (#P-complete, Roth 1996) (p.24)
- Approximate Bayesian inference: also NP-hard (Dagum and Luby 1993) (p.24)
- Partial MAP (Bayesian): NPPP-complete (Park and Darwiche 2004) (p.24)
- Computing Nash equilibria (2-player): PPAD-complete (Chen et al. 2009) (p.45)
- Computing correlated equilibria: polynomial time (p.45)
- Modal/deontic logic satisfiability: PSPACE to EXPTIME depending on variant (p.49–51)
- PAC learning sample complexity: polynomial in hypothesis class size but exponential in worst case (p.64)
- GPT-3.5 valid response rate in Moral Machine: ~95% (Takemoto 2024 — cited context, not this paper)

## 10. Pitfalls & limitations
- **Artificial idealization**: All analyses assume well-defined computational problems with precise inputs/outputs; real-world moral situations are rarely this structured (p.75–76).
- **Human-mind gap**: Whether humans actually perform the formal computations described (Bayesian inference, Nash equilibrium) is highly speculative; the paper acknowledges this extensively (pp.75–76).
- **No empirical grounding**: The paper contains no experiments, human data, or model evaluations, making it hard to verify practical relevance.
- **Ignored factors**: Emotions, social norms, embodied cognition, spiritual and cultural dimensions of morality are explicitly set aside (p.76).
- **Approximate algorithms**: The focus on exact solutions may be overly strict; the paper briefly notes that many NP-hard problems admit efficient approximations, but doesn't explore this fully.
- **Domain limitation**: Complexity results vary enormously by specific domain conditions; the paper's worst-case framing may overstate intractability for common moral scenarios.

## 11. Novel ideas worth stealing
1. **Marr's three-level framing for ethics benchmarks**: Distinguish (a) the computational-level problem (what moral judgment is being asked), (b) the algorithmic-level solution (what inference procedure the model uses), and (c) the implementation level (how it is realized). This provides a rigorous way to decompose alignment benchmarks rather than conflating problem and solution.

2. **Complexity classes as discrimination metrics**: Rather than pass/fail, rate benchmark items by estimated complexity class (O(n) vs. NP-hard vs. undecidable). Items that are computationally trivial tell us little; genuinely NP-hard moral problems (with many interacting agents, uncertain causal chains, conflicting norms) reveal more about a model's reasoning depth.

3. **Fixed-parameter tractability as a design principle**: Design benchmarks where tractable structure is explicit (e.g., small number of affected agents, tree-structured causal graphs), and measure whether models exploit that structure or revert to intractable heuristics.

4. **The optimality–feasibility trade-off as a benchmark axis**: Measure not just whether models produce correct answers, but whether they produce *approximately* correct answers and whether they are appropriately uncertain about edge cases where the optimal is computationally inaccessible.

5. **Self-effacing theory detection**: A benchmark item could present scenarios where following the stated normative theory strictly would require intractable computation, and observe whether the model correctly hedges, approximates, or overconfidently gives an exact answer.

6. **MTT as a falsifiability criterion**: Use tractability constraints to generate testable predictions about human moral behavior and compare with LLM behavior—if LLMs make intractably complex optimal computations instantly, that is a red flag for training-set contamination rather than genuine moral reasoning.

## 12. Notable quotes
- "In machine ethics, there are at present no domain-specific nor general benchmarks that can be used to evaluate the performance of different ethical systems." (p.2)
- "Based on the intractability (and undecidability) stemming from combinatorics of action plans, probabilistic causal inference, dynamic and partially observable environments, general rules, strategic dynamics, logic, semantics and learning, we firmly conclude that perfect moral machines are impossible." (p.4)
- "The Moral Tractability Thesis states that morality — moral behavior, moral problem-solving, and moral cognition — are constrained by computational tractability, given some reasonable model of human moral cognition." (p.72)
- "It would be unwise to exclude the possibility that there are more or less rigorous patterns in the cognitive processes that support [human morality], which in turn are amendable for formal investigation via [computational models]." (p.72)

## 13. UNKNOWN / not in extract
- Whether the journal version (2024) differs from the arXiv preprint (February 2023) used in the extract.
- The identity of the specific journal that published the 2024 version.
- Whether any empirical experiments accompanied the theoretical claims in supplementary material.
- Specific complexity results for virtue ethics beyond the PAC learning analysis (Section 6 was only partially covered in the extract read).
