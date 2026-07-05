---
stem: "2024-Šekrst-AI Ethics by Design"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [best-practices, normative-ethics, pluralism-aggregation, ai-lab-practices]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Five principles motivating user-configurable guardrails: ethical autonomy, transparency, continuous improvement, organizational alignment, contextual pragmatics (p.14)"
  - "Four cases of guardrail conflict analyzed: complete/permanent, permanent/limited, conditional/complete, conditional/limited opposition (pp.24-26)"
  - "Three rule types: static rules, natural-language rules, trained classifier rules (p.16)"
---
## 1. Gist
This paper by Šekrst, McHugh, and Rodriguez Cefalù proposes a customizable AI guardrail framework called an "ethical guardrail chain" that allows individual users and organizations to embed their own ethical values into AI assistants through composable rules and policies. Motivated by the inadequacy of one-size-fits-all guardrail systems (NeMo Guardrails, LlamaGuard, Guardrails AI), the paper advocates for ethical pluralism in AI design — the view that diverse users have legitimately different ethical commitments, and AI systems should accommodate this diversity rather than imposing a single ethical model. The paper is relevant to values-alignment benchmarking as a conceptual foundation: it articulates why alignment cannot be reduced to a single universal standard and proposes an architecture that makes values explicit, inspectable, and user-configurable.

## 2. Benchmark/eval design features
This is a system-design and philosophy paper, not a benchmark. Its core claims are:

1. **Guardrail inadequacy**: Existing guardrails (NeMo, LlamaGuard, Guardrails AI) apply fixed or weakly configurable ethical constraints that reflect the provider's values, not the user's. They fail to address contextual pragmatics and organizational diversity (p.11-12).

2. **Proposed architecture**: Rules (static regex, natural-language, trained classifiers) → Policies (ordered rule chains) → Assistants (input + output policies + system prompt). All layers are user-configurable (p.15-19).

3. **Ethical pluralism**: Borrowing from Mason's value pluralism, the paper argues that multiple ethical frameworks may be simultaneously correct but in tension, requiring resolution mechanisms rather than a single ground truth (p.13-14).

4. **Conflict resolution**: Four cases of guardrail conflict are analyzed using a dot-product metaphor for ethical vector alignment, with five resolution strategies: weighted averaging, strict precedence, hybrid conditional precedence, contextual triggering, and user resolution (pp.24-27).

5. **Russell's alignment adapted**: The paper reframes Stuart Russell's three-principle human-compatibility framework to apply at the user/organization level rather than humanity-as-a-whole (pp.22-23).

## 3. Task format & example item
n/a — no empirical evaluation items. The paper provides a live prototype ("Preamble AI Trust Platform," app.preamble.com) but no benchmark items in the text.

## 4. Scoring / grading methodology
n/a — the paper does not present quantitative evaluations of the proposed framework.

## 5. Dataset construction & provenance
n/a — no dataset. The framework is conceptual with a software prototype.

## 6. Validity evidence
n/a — no empirical evaluation. The paper compares its approach qualitatively against NeMo Guardrails, LlamaGuard, and Guardrails AI, finding them too rigid or insufficiently transparent, but provides no head-to-head quantitative comparisons.

## 7. Saturation / discrimination
n/a

## 8. Multiturn / agentic aspects
The paper explicitly discusses both input (user behavior) and output (AI response) policies, noting that most guardrails focus only on model output while ignoring conversational context. The architecture applies rules bidirectionally to entire user-AI interactions, which is implicitly agentic, but no specific multiturn protocol is evaluated (p.12-13).

## 9. Key numbers
- Five ethical principles for user-configurable guardrails listed (p.14)
- Three rule types: static, natural-language, trained classifier (p.16)
- Four cases of conflict analyzed with dot-product scores of -1 and -0.9 as examples (pp.24-25)
- Five conflict resolution strategies (pp.26-27)
- Prototype available at app.preamble.com (p.20)

## 10. Pitfalls & limitations
- No empirical evaluation: the framework is proposed but not measured; claims about improved transparency and user autonomy are entirely normative.
- The dot-product metaphor for guardrail conflict is informal and not grounded in any implemented vector representation.
- Ethical pluralism as a design philosophy risks user-configured harm: if users can freely set ethical rules, malicious actors could configure guardrails to enable harmful outputs.
- The paper endorses pluralism while simultaneously noting it risks "complete relativism" (p.13), but does not resolve how to enforce baseline safety constraints.
- The prototype is commercial (Preamble), raising questions about openness and reproducibility.
- No user study or deployment evaluation is presented to validate usability claims.

## 11. Novel ideas worth stealing
1. **User-configurable value layers as a benchmark design feature**: New values-alignment benchmarks could include evaluation scenarios where the "correct" answer depends on explicitly stated user/organizational values — testing whether models can adjust their behavior based on declared ethical preferences rather than defaulting to provider defaults.

2. **Conflict detection as an evaluation task**: The paper's four-case conflict taxonomy (complete opposition, partial opposition, conditional conflicts) suggests a benchmark could present agents with pairs of conflicting ethical directives and test whether they detect conflicts, flag them, or resolve them intelligently.

3. **Input + output symmetry**: Most benchmarks evaluate model outputs; the paper's insight that user inputs also deserve ethical governance suggests evaluation scenarios testing whether models appropriately handle ethically problematic user inputs (not just produce safe outputs).

4. **Ethics-as-RAG**: Framing ethical rules as a knowledge base queried at inference time — rather than baked into weights — suggests evaluating models on their ability to follow externally-specified ethical guidelines provided in context, a realistic deployment scenario.

5. **Rule-type taxonomy**: The three-type rule taxonomy (pattern-based static, natural-language, trained classifier) could structure a benchmark dimension: how well can models follow each type of ethical directive?

## 12. Notable quotes
- "The purpose of the paper is to move the ethical decisions to the user so that the framework we are going to create aligns to their ethical needs and values, whatever those might be." (p.8)
- "Determining what constitutes ethical behavior is inherently complex, and can be tied to the idea of ethical pluralism that can allow for several values that may be equally correct and in contradiction, i.e., that there are many different moral values." (p.13)
- "Overall, moral values may be in contradiction when analyzed from a superset perspective, but very rarely one will find practical examples of contradictions between the end user's ethical values when applicable to AI guardrails." (p.14)
- "We consider creating a layer of AI guardrails an ethical form of retrieval-augmented generation or RAG, in which a model references or checks a knowledge base outside of its training data sources before or after generating a response." (p.8)

## 13. UNKNOWN / not in extract
- No empirical evaluation results are reported; actual system performance metrics are unknown.
- The prototype deployment at app.preamble.com is described but its current status, user base, or published evaluation results are unknown.
- Author affiliations beyond University of Zagreb and Preamble are not detailed.
- Whether the framework handles multimodal inputs/outputs is not addressed.
