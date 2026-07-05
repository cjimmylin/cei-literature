---
stem: "2025-Nay-Aligning AI Agents with Humans through Law as Information"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, pluralism-aggregation, ai-lab-practices, design-space]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers: []
---
## 1. Gist
This is a legal informatics theory paper arguing that democratically developed law — rather than vaguely specified "ethics" — should serve as the primary target for AI alignment. The author, founder of Norm AI and affiliated with Stanford CodeX, advances the "Law Informs Code" (LIC) framework: using law as both a theoretical scaffold (rules, standards, legal reasoning) and a continuously updated data source for specifying AI objectives. The paper distinguishes two domains: (1) private law / contract law for human-AI alignment (aligning one AI with one principal); and (2) public law for society-AI alignment (aligning AI with democratically deliberated societal values and externality reduction). It matters for values-alignment benchmarking because it provides a principled justification for using legal standards as ground truth for AI value alignment, offers a critique of purely ethics-based approaches as lacking democratic legitimacy and practical specification, and frames fiduciary duty as an especially tractable legal standard for AI principal-agent relationships.

## 2. Benchmark/eval design features
This is a theoretical/position paper, not an empirical benchmark. Core claims and arguments:

1. **Reward specification is inherently incomplete**: AI agents trained with reward functions explore only a sparse subset of possible future states; law provides generalized standards that fill the gaps (analogous to incomplete contracts between parties).

2. **Law as the most democratic encapsulation of values**: Democratic law-making aggregates and legitimizes human preferences more credibly than ad-hoc "ethics" specifications; it has been theoretically refined for centuries.

3. **Three pillars**: (a) Law Governs Code (existing frameworks), (b) Code Informs Law (AI improving legal services), (c) Law Informs Code (the proposed new pillar — using law as AI alignment data).

4. **Private law (contracts + standards) for human-AI alignment**: Contracts as incomplete specification of the human-AI relationship; legal standards (e.g., "reasonable," "material") as modular fill-in mechanisms. Fiduciary duty as the richest applicable standard: duty of care (AI capability) + duty of loyalty (faithful pursuit of human ends).

5. **Public law for society-AI alignment**: Statutory law, regulatory guidance, and judicial opinion as a continuously updated, democratically grounded knowledge base of societal values and externality constraints. Addresses "multi-single" (multiple humans, one AI) alignment which is the primary challenge.

## 3. Task format & example item
n/a — theoretical paper. No benchmark items.

## 4. Scoring / grading methodology
n/a — no empirical evaluation.

## 5. Dataset construction & provenance
n/a — no dataset. The paper draws on legal scholarship and AI safety literature; cites over 70 legal and AI sources.

## 6. Validity evidence
n/a — no quantitative results. The argument relies on analogical reasoning between legal theory and AI alignment theory: incomplete contracts ↔ incomplete reward functions; fiduciary duty ↔ AI duty of loyalty; legal standards ↔ behavioral generalization from data; democratic law-making ↔ legitimate value aggregation.

## 7. Saturation / discrimination
n/a — theoretical paper.

## 8. Multiturn / agentic aspects
The paper is explicitly concerned with agentic AI systems that take actions in the world on behalf of principals. The fiduciary duty framework and public law constraints are designed specifically for AI agents with sufficient capability and autonomy to pursue human ends and affect third parties. The "multi-multi" alignment problem (multiple principals, multiple AI agents) is acknowledged as particularly critical as capabilities advance.

## 9. Key numbers
No empirical numbers. Key conceptual numbers: 75% threshold percentile mentioned in passing in EvalMORAAL (unrelated paper); here the paper notes that fiduciary duties are applied "widely by courts across various types of relationships" and that "the default rule in fiduciary law is that all gains that arise in connection with the fiduciary relationship belong to the principal unless the parties specifically agree otherwise."

## 10. Pitfalls & limitations
- Law reflects path-dependent political power structures and is not a perfect aggregation of human values; the author acknowledges this but argues it is still the most credible democratic encapsulation
- Law is often silent or prejudiced on issues relevant to AI alignment — ethics integration is still needed where law is silent
- No empirical validation that LIC actually produces better-aligned AI systems
- The framework assumes that legal standards can be computationally encoded and embedded — a significant technical challenge
- Democratically developed law may lag behind AI capabilities and novel contexts
- Public law varies across jurisdictions; "society-AI alignment" requires choosing which society's law to embed
- The paper is aspirational/programmatic; no implementation details for how to encode legal standards into AI training

## 11. Novel ideas worth stealing
- **Fiduciary duty as an alignment standard**: The fiduciary framework (duty of care + duty of loyalty) provides a well-developed legal standard for principal-agent relationships with power asymmetry — precisely the AI deployment context. Using fiduciary duties as a template for specifying AI value alignment targets is concrete, legally grounded, and already validated across finance, healthcare, and corporate governance.
- **Rules vs. standards spectrum as a design variable**: The legal distinction between brittle if-then rules and flexible generalizable standards maps directly onto the tension in values benchmarks between precise specifications (MCQ items) and contextual judgment (open-ended evaluation). Designing benchmarks with explicit "standard-ness" as a dimension could improve ecological validity.
- **Incomplete contracts as a frame for benchmark coverage**: Just as contracts cannot enumerate all contingencies, values benchmarks cannot enumerate all value-relevant situations. Legal gap-filling mechanisms (implied terms, background standards) suggest using pre-specified ethical standards as implicit scoring rubrics for out-of-distribution scenarios.
- **Democratic legitimacy as a benchmark validity criterion**: The question "whose values?" is central to any values alignment benchmark. The LIC framework suggests that democratic law is the most defensible answer for societal-level alignment, and that benchmark items should be traceable to legally articulated societal norms rather than researcher stipulations.
- **Society-AI alignment ("multi-single" problem) as the primary target**: Most benchmarks focus on individual human-AI agreement. The LIC framework highlights that the harder and more important problem is aligning AI with the aggregate of societal values, including externalities to third parties — suggesting that benchmark validity should be assessed against population-level norms, not individual expert panels.

## 12. Notable quotes
- "'Code Is Law' communicated the power of software as a form of governance in cyberspace. Now that AI capabilities are rapidly advancing, 'Law Informs Code' describes the legal informatics approach to shaping AI toward human goals." (p.2)
- "Although law reflects the path-dependent structure of political power within a society and not a perfect aggregation of human values, it is the most democratic encapsulation of the norms and values of the governed." (p.2)
- "Law, as the applied philosophy of multi-agent alignment, uniquely has the potential to address these alignment problems." (p.4)
- "Moving beyond the problem of aligning AI with a single human, aligning AI with society is considerably more difficult but necessary as AI deployment has broad effects." (p.13)

## 13. UNKNOWN / not in extract
- Section IV (Public Law: Society-AI Alignment) continues beyond p.13 in the extract — the analysis of specific public law mechanisms (regulatory standards, statutory interpretation, etc.) is cut off
- Section V (Conclusion) is not in the extract
- No empirical case studies or implementation examples are provided — the paper is entirely theoretical
- Whether Norm AI (the author's company) has implemented any of these principles in practice is not discussed in the extract
