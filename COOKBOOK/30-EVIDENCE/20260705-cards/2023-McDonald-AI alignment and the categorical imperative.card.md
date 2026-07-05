---
stem: "2023-McDonald-AI alignment and the categorical imperative"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, design-space]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers: []
---
## 1. Gist
This philosophical commentary by Fritz McDonald (Oakland University) critiques a proposal by Kim, Hooker, and Donaldson to implement Kantian ethics in AI systems via deontic modal logic. McDonald argues that their framework—comprising a Generalization Principle (Formula of Universal Law), a Utilitarian Principle, and an Autonomy Principle—makes computational demands on AI that exceed current capabilities and fails to adequately incorporate the Formula of Humanity (never treat persons as mere means). Published in AI and Ethics (2023), this paper is relevant to values-alignment benchmarking as a careful philosophical audit of what it would take to build AI systems that genuinely implement deontological ethics—and why existing proposals fall short.

## 2. Benchmark/eval design features
This is a theory/commentary paper, not a benchmark. The paper critically analyzes three formal principles proposed by Kim, Hooker, and Donaldson:

1. **Generalization Principle** (Formula of Universal Law): An action is permissible if it is rational to believe it is possible for everyone to act on the same action plan. Formalized as: ◇aP[∀x(C(x) ⇒x A(x)) ∧ C(a) ∧ A(a)]. McDonald argues this requires AI systems to model rational belief, conceive of counterfactual worlds, and understand agent psychology—none of which current AI can reliably do.

2. **Utilitarian Principle**: An action is permissible if it is rational to believe it promotes at least as much utility as any alternative. McDonald critiques the underspecification of "utility" and the demanding nature of requiring always maximizing utility.

3. **Autonomy Principle**: An action is permissible if the agent's action plans are consistent with others' action plans. McDonald shows this is both too restrictive (rules out harmless competitive actions like taking the last piece of brie) and insufficient (allows agreeing to be treated as a mere means).

Two illustrative counterexamples ("Lock" and "Veer") show that the three principles together can permit clearly wrong actions involving autonomous vehicles.

## 3. Task format & example item
n/a. No benchmark items. The paper uses philosophical thought experiments:

- **Watch-stealing case** (p.4): Testing the Generalization Principle—Kim et al. argue universalizing watch-stealing is impossible, so it is wrong. McDonald notes this relies on AI conceiving of counterfactual worlds.
- **Lock case** (p.6–7): A driver agrees to terms that lock the car unless the driver's activity maximizes utility. Passes all three principles but violates the Formula of Humanity.
- **Veer case** (p.7): Society agrees that autonomous vehicles may veer toward pedestrians to save passengers. Passes all three principles but involves treating bystanders as mere means.

## 4. Scoring / grading methodology
n/a. Philosophical commentary with no empirical scoring.

## 5. Dataset construction & provenance
n/a. No dataset.

## 6. Validity evidence
n/a. The paper's argument is philosophical. It draws on primary sources (Kant's Groundwork, Practical Philosophy), contemporary Kantians (O'Neill, Korsgaard), and the Powers (2006) critique of Kantian machine ethics. The counterexamples are constructed to test the logical sufficiency of the three principles.

## 7. Saturation / discrimination
n/a.

## 8. Multiturn / agentic aspects
n/a. The autonomous vehicle examples involve agentic systems, but the discussion is about the ethics of action planning, not multiturn interaction.

## 9. Key numbers
No empirical numbers. The paper is purely theoretical. Key references: Kim, Hooker, Donaldson (2021) in JAIR vol. 70 pp. 871–890; Hooker and Kim (2018) AAAI/ACM AIES proceedings.

## 10. Pitfalls & limitations
McDonald's critique is itself subject to limitations he does not fully address:
- He argues the Formula of Humanity is necessary but does not show how it could be implemented computationally—his positive proposal is underdeveloped
- The paper focuses on autonomous vehicles as the test case, which may not generalize to LLM-based systems where the alignment challenges are different
- McDonald concedes that supplemental principles for exception-handling (non-monotonic reasoning) are needed but does not propose a solution
- The paper may set an overly high bar: requiring AI to have full moral insight before deployment may be perfectionistic

## 11. Novel ideas worth stealing
1. **Formula of Humanity as an alignment criterion**: The negative duty (never treat persons as mere means) and positive duty (treat persons as ends) together provide a clearer target for alignment evaluation than maximizing utility or following rules. Benchmarks could test whether AI responses show evidence of treating users as ends-in-themselves.
2. **Counterexample method for principle testing**: Using thought experiments (Lock, Veer) to identify cases where a proposed ethical framework permits clearly wrong actions is a useful methodology for evaluating moral AI frameworks—applicable to stress-testing values-alignment systems.
3. **Conceptual vs. volitional inconsistency distinction**: Kim et al.'s approach only tests for conceptual inconsistencies (cannot conceive the universalized world); Kant also tests for volitional inconsistencies (cannot rationally will the universalized world). LLM benchmarks should probe both types.
4. **The fact/value entanglement problem**: McDonald notes that notions like "person," "mere means," and "ends-in-themselves" cannot be cleanly separated into descriptive (neural network input) and normative (logic rule) components. This is a deep challenge for any benchmark that tries to decompose values from facts.
5. **Non-monotonic reasoning requirement**: Moral principles often have exceptions that do not invalidate the principle. Benchmarks should test whether models handle such non-monotonic structures correctly (e.g., suicide is generally wrong but may be permissible in some cases).

## 12. Notable quotes
- "Recognition of what makes a person a person requires ethical insight. Similar insight is needed to tell treatment as a means from treatment as a mere means. This kind of insight is normative, nuanced, and not obvious based on the descriptive facts of the world." (p.7)
- "To judge what is rational to believe would involve the kind of general intelligence that most think AI systems lack currently." (p.3)
- "Making a moral machine remains a serious challenge. I would suggest that doing so would require a more general kind of intelligence on the part of machines than is currently on offer now. It would also require a great advance in moral philosophy by humans themselves, to give the right kind of guidance to machines." (p.7)
- "Their papers are largely theoretical, putting forward three principles in modal logic, and then showing how those modal logic principles might be applied to specific cases." (p.2)

## 13. UNKNOWN / not in extract
- Whether the paper has been responded to by Kim, Hooker, or Donaldson
- McDonald's positive alternative framework (he indicates the Formula of Humanity is necessary but does not formalize it)
- Whether the paper addresses large language models or is limited to classical logic-based AI systems
- Any empirical follow-up testing the computational limits McDonald identifies
