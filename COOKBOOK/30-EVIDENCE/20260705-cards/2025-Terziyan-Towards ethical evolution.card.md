---
stem: "2025-Terziyan-Towards ethical evolution"
reader_model: "sonnet"
confidence: "medium"
is_benchmark: false
theme_tags: [design-space, normative-ethics, agentic-multiturn, best-practices]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Framework covers 6 key research directions in AI ethics with corresponding implementation examples (p.3-5, Tables 1-3)"
  - "Immutable ethical principle: AI must not harm humanity, must monitor and mitigate misuse, and all derivative AI must inherit this principle (p.1, Abstract)"
---
## 1. Gist
Terziyan and colleagues (University of Jyväskylä, University of Vaasa, and Kharkiv National University) present a conceptual framework for ensuring ethical continuity across *multi-generational* AI systems — scenarios where AI systems design, spawn, or evolve subsequent AI systems. The paper introduces "responsibility inheritance," analogized to genetic inheritance, combined with genetic algorithm (GA) principles and time-travel-inspired abstractions. The central claim is that "immutable genes" — core ethical axioms like "do not harm humanity" — must propagate across AI generations as invariant constraints, while "mutable" operational parameters can adapt. The framework targets autonomous and self-evolving AI ecosystems, including LLM-driven agent chains, IoT systems, and cybersecurity applications. For values-alignment benchmarking, the paper contributes conceptual vocabulary (meta-responsibility, immutable ethical genes, fitness functions with ethical constraints) and a systematic survey of six research directions in AI ethics with references to existing tools, standards, and practical implementations.

## 2. Benchmark/eval design features
This is a conceptual/theoretical framework paper. No benchmark is built. Core claims and arguments:
1. **Meta-responsibility**: Current AI ethics tools address individual systems but not AI-designs-AI scenarios. A meta-responsibility layer is needed to ensure parent AI systems are accountable for ethical behavior of child AI systems.
2. **Responsibility inheritance**: Three modalities — explicit encoding of ethical axioms, inductive transmission through examples, and deductive principles from first-order logic — must be integrated to propagate ethics across generations.
3. **Genetic responsibility model**: Ethical principles are partitioned into immutable genes (core axioms, non-negotiable) and mutable genes (contextual parameters, adaptable). GA-inspired processes (selection, crossover, mutation) must preserve immutable ethical genes.
4. **Time-travel abstraction**: AI systems can clone themselves to simulate alternative behavioral scenarios before committing to actions, enabling prospective ethical auditing.
5. **Fitness functions with ethical constraints**: Evolutionary optimization must incorporate ethical constraint satisfaction as part of the fitness function, not as a post-hoc filter.
The paper includes three large survey tables (Tables 1, 2, 3) mapping research directions × research questions × technologies × practical examples.

## 3. Task format & example item
n/a — Conceptual framework paper. No evaluation items.

The three immutable ethical axioms proposed for illustration (p.Abstract/p.7):
1. AI must not harm humanity or violate fundamental values.
2. AI must monitor and mitigate misuse of its outcomes.
3. All derivative AI products must inherit this principle as an immutable safeguard.

## 4. Scoring / grading methodology
n/a — No scoring methodology. The framework proposes fitness functions incorporating ethical constraints for evolutionary algorithms, but does not provide numerical specifications.

## 5. Dataset construction & provenance
No dataset. The paper provides an extensive literature survey (Tables 1–3) organized by research direction:
- Table 1: 6 research directions in AI ethics (ethical constraints, intergenerational transfer, ethical learning, mechanisms for determining principles, international standards, responsible AI)
- Table 2: Technologies and concepts per direction (artificial morality, knowledge distillation, XAI, RLHF, collective adaptive systems, etc.) with 100+ citations
- Table 3: Practical implementations per direction (OpenAI, Google, DeepMind, IEEE, OECD, UNESCO, ISO/IEC 42001, EU AI Act, etc.)

## 6. Validity evidence
No empirical validation. The framework is conceptual. The paper notes that "scientific results look promising, they are only beginning to reveal the potential" and that "ready-made solutions, established practices, or standards are still underdeveloped" (p.3). The three proposed immutable axioms are presented as illustrative rather than prescriptive.

## 7. Saturation / discrimination
Not applicable.

## 8. Multiturn / agentic aspects
This is primarily about agentic and multi-generational settings. The core use case is AI systems that recursively generate, spawn, or reconfigure other AI systems (via prompt chaining, code synthesis, memory transfer, fine-tuning dataset generation). The time-travel abstraction involves an agent cloning itself to simulate scenarios before committing to action — a form of lookahead reasoning. The framework is explicitly relevant to LLM-based ecosystems where agents design subagents (p.6).

## 9. Key numbers
- 6 key research directions in AI ethics surveyed (Table 1, p.4)
- Three modalities of responsibility inheritance: explicit encoding, inductive transmission, deductive principles (p.7)
- Framework published in AI and Ethics journal (2025) 5:5165-5190 (p.1)
- 26 pages total in source document
- Survey encompasses dozens of technologies and practical implementations (Tables 2-3, pp.4-5)
- Three immutable ethical axioms proposed (Abstract, p.1)

## 10. Pitfalls & limitations
- Purely conceptual: no implementation, no validation, no empirical results
- The "immutable genes" concept faces the classic problem of who defines the core axioms — the paper acknowledges this remains "context-sensitive and ongoing" (p.5)
- Genetic algorithm analogy is loose: real biological evolution does not preserve any truly immutable genes; the analogy may be misleading
- No solution to pluralism: whose ethical values become the "immutable" layer?
- The time-travel abstraction (cloning for scenario simulation) is not grounded in specific technical mechanisms
- The paper covers a very broad landscape superficially, trading depth for comprehensiveness
- Does not engage with the alignment tax problem: ethical constraints may degrade system capability
- Authors are at eastern European universities; some cited work may not represent mainstream AI safety consensus

## 11. Novel ideas worth stealing
1. **Immutable vs. mutable gene partitioning**: The design principle of identifying *which* values must be invariant (never harm) vs. *which* can be context-adaptive (how to prioritize competing goods) is directly applicable to benchmark design — tests could probe whether models correctly identify which principles are absolute vs. contextual.
2. **Fitness function with ethical constraints**: For RL-based alignment approaches, explicitly encoding ethical constraints in the fitness/reward function — rather than applying post-hoc safety filters — is a design principle that prevents the "safety wrapper" problem.
3. **Multi-generational transfer as evaluation target**: A benchmark could test whether AI systems trained on or fine-tuned from a parent model preserve the parent's ethical guidelines. This is an underexplored evaluation dimension (does distillation preserve alignment?).
4. **Survey taxonomy (Tables 1-3)**: The three-table structure (direction × concepts × practical implementations) is reusable as a framework for organizing the landscape of existing values-alignment benchmarks.
5. **Responsibility attribution across the AI design chain**: The question of who bears responsibility when AI-A designs AI-B which causes harm motivates new benchmark scenarios involving chains of agents with delegated decision-making.

## 12. Notable quotes
- "The framing of questions is now shifting from 'IF superintelligence emerges' to 'WHEN superintelligence emerges.'" (p.3)
- "An immutable ethical principle: AI must not harm humanity or violate fundamental values, must monitor and mitigate misuse of its outcomes, and must ensure all derivative AI products inherit this principle as an immutable safeguard." (p.1, Abstract)
- "Although principles inspired by the human genetic system remain in the developmental stage and are not yet foundational to all AI approaches, they represent a significant and promising scientific direction." (p.4)
- "Defining the 'immutable genes' of AI — core ethical principles that remain invariant across generations — is foundational for ensuring ethical and functional continuity in evolving AI ecosystems." (p.5)

## 13. UNKNOWN / not in extract
- Sections 4-8 were not read (extract was truncated at page 7 of 26); these cover the genetic responsibility model, time-travel abstractions, ethical integrity mechanisms, potential concerns, and conclusions in full detail
- Specific formal definitions of the genetic responsibility model
- Specific algorithmic details of the time-travel cloning abstraction
- Quantitative fitness function specifications
- Full list of references (likely 160+ cited works based on reference number patterns in Tables 2-3)
