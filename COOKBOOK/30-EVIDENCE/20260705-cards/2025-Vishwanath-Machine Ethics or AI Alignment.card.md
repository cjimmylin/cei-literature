---
stem: "2025-Vishwanath-Machine Ethics or AI Alignment"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, ai-lab-practices, pluralism-aggregation]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Ji et al. propose four key AI alignment objectives: Robustness, Interpretability, Controllability, and Ethicality (RICE) (p.2)"
  - "Gabriel identifies five alignment approaches: instructions, expressed preferences, idealized preferences, informed preferences, and autonomy-preserving (p.4)"
---
## 1. Gist
This position paper, presented at the Norwegian AI Society (NAIS) 2025 symposium, argues that machine ethics (ME) and AI alignment are distinct but intersecting research disciplines that have been conflated in the literature. ME aims to embed ethical theories into AI agents to produce morally commendable behavior, drawing on moral philosophy. AI alignment aims to ensure AI behaves as intended by humans, drawing more from political philosophy and human consensus mechanisms (RLHF, social choice theory). The paper clarifies the two fields' goals, methodologies, advantages, and disadvantages through structured comparison, and argues for greater interdisciplinary collaboration. Relevant to values-alignment benchmarking as a conceptual framing paper that articulates what distinguishing features make a benchmark belong to ME vs. alignment territory, and why neither field alone adequately operationalizes "ethical AI."

## 2. Benchmark/eval design features
This is a theoretical position paper with no benchmark, dataset, or empirical evaluation. Core claims:

**Machine Ethics:**
- Grounded in moral philosophy (consequentialism, deontology, virtue ethics, moral particularism).
- Focuses on AI agents rather than systems.
- Approaches: top-down (pre-encoded rules), bottom-up (learning from environment), hybrid.
- Methods include evolutionary algorithms, RL, LLMs, neural networks.
- Criticized for: no consensus on which ethical theory to implement; hard-coded constraints can't cover all scenarios.

**AI Alignment:**
- Grounded in political philosophy and human consensus.
- Operates via RLHF, constitutional AI, red-teaming, filters.
- Gabriel's framing: alignment ≠ finding the "true" moral theory; rather, finding principles compatible with moral diversity.
- Shen et al.'s bidirectional alignment draws on Schwartz Theory of Basic Values; pluralistic alignment grounded in social choice theory.
- Criticized for: value inclusion/exclusion bias, dynamically changing values, explainability problems, geopolitical instability of consensus.

**Intersection case**: Delphi (Jiang et al.) claims both ME and alignment heritage — criticized by Lamberti et al. for inadequate philosophical grounding of its Rawlsian claims. MACHIAVELLI benchmark criticized for lacking philosophical justification for power-seeking definitions.

## 3. Task format & example item
n/a — no empirical task. The paper's closest thing to an item is Table 1 (p.6): a structured comparison of ME vs. AI alignment across Research Goal, Similarities, Differences, Advantages, and Disadvantages.

## 4. Scoring / grading methodology
n/a — no empirical evaluation.

## 5. Dataset construction & provenance
n/a — no dataset.

## 6. Validity evidence
n/a — position paper. The claims rest on literature review and conceptual analysis rather than empirical evidence. Key cited works: Wallach & Allen (2010) on functional morality, Gabriel (2020) on AI alignment and values, Shen et al. (2024) on bidirectional alignment, Ji et al. (2025) on the comprehensive alignment survey.

## 7. Saturation / discrimination
n/a

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- RICE framework: 4 objectives for AI alignment — Robustness, Interpretability, Controllability, Ethicality (p.2)
- Three approaches to moral agents: top-down, bottom-up, hybrid (p.3)
- Gabriel's 5 alignment framings: instructions, expressed preferences, idealized preferences, informed preferences, autonomy-preserving (not all numbered in extract, but implied) (p.4)
- Delphi criticized for Rawlsian theory without adequate philosophical grounding (p.6)

## 10. Pitfalls & limitations
- Position paper without empirical validation; claims are necessarily speculative.
- Limited engagement with the technical details of how either field operationalizes its goals — relies on high-level survey citations.
- The distinction drawn (ME = bottom-up ethics; Alignment = top-down consensus) is somewhat stylized; contemporary practice blurs these lines significantly.
- Does not address how to evaluate whether a benchmark belongs to ME vs. alignment territory in practice.
- Brief (9 pages); many interesting lines of argument are underdeveloped.

## 11. Novel ideas worth stealing
- **ME vs. Alignment as benchmark frame**: Whether a benchmark probes whether a model has internalized ethical principles (ME) vs. whether it follows human consensus norms (alignment) is a potentially useful typology for categorizing existing benchmarks and identifying gaps.
- **Functional morality as OOD behavior target**: Wallach & Allen's "functional morality" — the middle ground between fully autonomous moral agency and purely rule-following — is a tractable target for behavioral benchmarks: does the model recognize morally salient situations and respond appropriately even in novel contexts?
- **Dynamic values as benchmark design challenge**: The paper's point that human values evolve over time (and alignment training requires updating) suggests a need for benchmarks that explicitly test for temporal value robustness or adaptability.
- **Geopolitics as alignment stress test**: The geopolitics critique (shared human values are unstable under geopolitical volatility) motivates adversarial benchmark items where ostensibly "universal" values are contested by different world regions.
- **Philosophical grounding audit**: The criticism that Delphi and MACHIAVELLI lack adequate philosophical justification for their ethical constructs suggests a checklist criterion for values benchmarks: explicit statement of which ethical theory underpins the normative choices.

## 12. Notable quotes
- "Machine ethics researchers aim to embed ethical theories within AI, while AI alignment researchers develop techniques to ensure that AI agents behave as intended by humans." (p.1)
- "We claim that neither ME nor AI alignment is closer to securing ethical behavior from AI agents." (p.5)
- "Gabriel clarified the value alignment question as: '...it is to find a way of selecting appropriate principles that are compatible with the fact that we live in a diverse world, where people hold a variety of reasonable and contrasting beliefs about value'." (p.4)
- "Depending on the application, knowing which groups to include or exclude could determine an AI system's bias towards selected groups. This could prove catastrophic when AI systems make harmful decisions against marginalized communities." (p.5)

## 13. UNKNOWN / not in extract
- Authors' institutional affiliations beyond University of Agder and University of Bergen
- Whether this is a preprint or published proceedings paper (NAIS 2025 = Symposium of the Norwegian AI Society)
- A full literature map of ME vs. alignment papers
- Empirical evidence for any of the claims about existing benchmarks
- Gabriel's full five-way framework for alignment (only partially described in extract)
