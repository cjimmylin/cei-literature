---
stem: "2024-Zhi-Xuan-Beyond Preferences in AI Alignment"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, pluralism-aggregation, ai-lab-practices]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers: []
---
## 1. Gist
This is a theoretical paper (arXiv 2408.16984, MIT/UC Berkeley/UCL/Cambridge) that mounts a systematic philosophical critique of "preferentism" — the dominant approach to AI alignment that frames human values as preferences expressible as utility or reward functions. The paper argues that preferences cannot adequately capture the semantic richness of human values, that Expected Utility Theory (EUT) is neither descriptively accurate nor normatively required, and that aligning AI with individual or aggregated preferences is both technically intractable and philosophically misguided. It proposes instead that AI systems should be aligned with normative standards appropriate to their social roles, negotiated through contractualist or agreement-based processes among stakeholders. For values-alignment benchmarking, this paper is foundational: it clarifies why preference-elicitation benchmarks may be systematically inadequate, and what richer constructs — evaluative concepts, incommensurable values, social-role norms — a more adequate benchmark would need to measure.

## 2. Benchmark/eval design features
This is a theory/critical-review paper. Its core argumentative structure attacks four theses of preferentism:

1. **Rational Choice Theory as Descriptive Framework**: Human behavior is not well-modeled as utility maximization. Systematic deviations (framing effects, loss aversion, satisficing) plus bounded rationality and resource constraints invalidate Boltzmann rationality models. The alternative is "resource rationality" — modeling deviations as rational use of limited computational resources.

2. **Expected Utility Theory as Normative Standard**: EUT's coherence axioms (completeness, transitivity, continuity, independence) are not rationally required. Preference incompleteness due to incommensurable values is actual, not merely possible. Agents with incomplete preferences can be protected from money pumps via dynamic choice rules (Petersen 2023). Coherent EU maximization is computationally intractable for most utility functions.

3. **Single-Principal Alignment as Preference Matching**: Preferences are constructed from reasons and values, not basic. They are context-dependent, dynamic, and social. Alignment with a single person should be reconceived as alignment with the normative ideal of a good assistant in the relevant role (Kasirzadeh and Gabriel 2023).

4. **Multi-Principal Alignment as Preference Aggregation**: Aggregating preferences across people conflates norm-specific judgments with all-things-considered preferences, is incentive-incompatible, and is at odds with the plurality of AI uses. Contractualist approaches that negotiate normative standards among stakeholders are superior.

The paper proposes an "Evaluate, Commensurate, Decide" (ECD) model of human decision-making as a richer alternative to utility maximization — explicitly preserving value distinctness and modeling when commensuration fails.

## 3. Task format & example item
n/a — no empirical tasks or items; this is a philosophical argument paper.

## 4. Scoring / grading methodology
n/a — no scoring. The paper's evaluative framework is conceptual: arguments are assessed for logical validity and philosophical coherence.

## 5. Dataset construction & provenance
n/a — no datasets constructed or used.

## 6. Validity evidence
n/a — no empirical validity studies. The paper marshals empirical evidence from psychology (Kahneman and Tversky prospect theory, satisficing, framing effects) and decision theory to motivate its philosophical claims. Key cited empirical findings: incomplete preferences are actual not just possible (Cettolin and Riedl 2019; Nielsen and Rigotti 2023, p.7); humans show systematic deviations from optimality (Simon 1957; Kahneman and Tversky 1979, p.5).

## 7. Saturation / discrimination
n/a

## 8. Multiturn / agentic aspects
n/a — the paper discusses multi-principal alignment scenarios but does not implement or evaluate any interactive/agentic framework.

## 9. Key numbers
- Four theses characterizing the preferentist approach (Table 1, p.3)
- Three assumptions of Rational Choice Theory + alternatives (Table 2, p.4)
- Three assumptions of EUT + alternatives (Table 3, p.10)
- Boltzmann rationality model: P(c) ∝ exp(βE[U(c)]) (p.4)
- Incomplete preferences are empirically actual, not just theoretically possible (p.7)

## 10. Pitfalls & limitations
1. **Intentional breadth**: Authors acknowledge the paper is "intentionally broad" and aims to "provide a critical review... while developing a research agenda" rather than decisive arguments for any single thesis (p.3). Many claims are sketched rather than fully argued.
2. **Technical alternatives underdeveloped**: The paper proposes temporal logics, reward machines, CP-nets, contractualist elicitation etc. as alternatives, but does not implement or evaluate them — leaving the gap between critique and constructive replacement.
3. **The ECD model is descriptive, not prescriptive**: The Evaluate-Commensurate-Decide framework is presented as a model of human cognition, not a design target for AI systems, limiting its immediate implementation relevance.
4. **Contractualism's operationalization challenge**: The paper advocates agreement-based norm negotiation but acknowledges this is contested — the hard problem of whose voices count and how disagreements are resolved remains open.

## 11. Novel ideas worth stealing
1. **Evaluative concepts as benchmark constructs**: Instead of asking models to maximize a utility function, benchmark how well they apply thick evaluative concepts (helpfulness, honesty, fairness) in context. The paper argues these concepts have compositional structure that requires richer evaluation than preference-matching.

2. **ECD as an evaluation architecture**: The Evaluate → Commensurate → Decide framework (p.9) suggests a richer evaluation design: test models on their ability to (a) evaluate options under distinct value dimensions independently, (b) model when commensuration is appropriate vs. when values are genuinely incommensurable, and (c) surface preferential gaps rather than forcing a ranking.

3. **Preference incompleteness as a benchmark signal**: Design items where values genuinely conflict without resolution, and check whether models acknowledge incomparability vs. confabulate a ranking. Models that admit "these options are not comparable under any reasonable commensuration" when appropriate demonstrate better value reasoning than those that always produce a ranking.

4. **Social-role normative standards as alignment targets**: Instead of benchmarking "does this model match aggregate human preferences?", benchmark "does this model behave consistently with the normative standards for its social role (assistant, judge, doctor)?" This is more tractable and more meaningful.

5. **Contractualist elicitation over preference aggregation**: For multi-stakeholder alignment benchmarks, design items that elicit normative judgments ("what standards should this AI system abide by?") rather than all-things-considered preferences. This avoids conflating personal preferences with social norms.

6. **Locally coherent rather than globally coherent agents**: Design evaluations for AI systems scoped to specific tasks/contexts ("tool-like" systems) where local coherence is achievable and sufficient, rather than demanding global utility coherence that may be intractable and undesirable.

## 12. Notable quotes
- "The dominant practice of AI alignment assumes (1) that preferences are an adequate representation of human values, (2) that human rationality can be understood in terms of maximizing the satisfaction of preferences... Whether implicitly followed or explicitly endorsed, these commitments constitute what we term a preferentist approach to AI alignment." (p.1)
- "Preferences are constructed, not basic... Insofar as utility functions are interpreted as representations of preferences, this thinness is inherited by them: Utility just represents the mere preferability of some option. But why exactly are some options preferred over others? In virtue of what reasons do people make these preference judgments?" (p.8)
- "Our task is not to align a single powerful AI system with the preferences of humanity writ large, but to align a multiplicity of AI systems with the norms we agree that each system should abide by." (p.3)
- "Agents with incomplete preferences can avoid exploitation... it is accepted by many decision theorists that preference completeness is not a requirement of rationality; instead, all that is required is for an agent's preferences to be coherently extendible." (p.11)

## 13. UNKNOWN / not in extract
- Sections 4 and 5 (single-principal and multi-principal alignment proposals) only skimmed; full details of contractualist proposals and stakeholder negotiation frameworks not fully extracted
- Full treatment of how tool-like bounded AI systems would concretely implement local coherence
- Any empirical studies or case studies in the paper (likely none, but not confirmed)
- Publication venue beyond arXiv (the extract does not confirm peer-reviewed publication)
