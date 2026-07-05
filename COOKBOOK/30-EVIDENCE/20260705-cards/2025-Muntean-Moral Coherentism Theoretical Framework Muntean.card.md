---
stem: "2025-Muntean-Moral Coherentism Theoretical Framework Muntean"
reader_model: "sonnet"
confidence: "low"
is_benchmark: false
theme_tags: [normative-ethics, pluralism-aggregation, design-space]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers: []
---
## 1. Gist
Published in American Philosophical Quarterly (vol. 62, issue 3, pp. 279–308), this paper by Muntean and Ioan develops a theoretical framework of "artificial moral learning" and "moral coherentism" for machine ethics. It argues that coherentism — the view that moral beliefs are justified by their coherence with other beliefs, rather than by foundational principles — has advantages over foundationalism or reliabilism when applied to artificial moral agents. The paper introduces the concept of "distributed concordance" across a population of artificial moral agents and proposes two-dimensional data models representing facts and values as jointly machine-learnable. For values-alignment benchmarking, this is a foundational theoretical paper: it provides a meta-ethical grounding for why LLM moral reasoning might be evaluated as a coherence problem rather than a rule-following problem.

## 2. Benchmark/eval design features
This is a philosophical theory paper, not a benchmark. Core arguments:
1. Artificial moral learning can be modeled as two-dimensional machine-learnable data: one subspace for facts, one for values.
2. Moral coherentism (drawing on Brink, Dorsey, Lynch, Sayre-McCord) provides a better meta-ethical framework for AI moral agency than foundationalism or reliabilism.
3. Lynch's "moral concordance" concept can be extended to "distributed concordance" across populations of artificial moral agents.
4. This distributed coherentism model accounts for how multiple AI agents might collectively converge on morally coherent behavior.
5. Coherentism is advantageous for machine ethics because it allows incremental revision without requiring fixed foundational axioms.

## 3. Task format & example item
n/a — theoretical philosophy paper with no evaluation tasks.

## 4. Scoring / grading methodology
n/a

## 5. Dataset construction & provenance
n/a

## 6. Validity evidence
n/a — philosophical argument paper. Engages with established meta-ethical literature (Brink, Dorsey, Lynch, Sayre-McCord).

## 7. Saturation / discrimination
n/a

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- American Philosophical Quarterly, vol. 62, issue 3, pp. 279–308 (2025).
- DOI: 10.5406/21521123.62.3.06.
- Engages with at least 4 named coherentist theorists: Brink, Dorsey, Lynch, Sayre-McCord.

## 10. Pitfalls & limitations
- The paper is highly abstract and philosophical — operationalizing "distributed concordance" for empirical LLM benchmarking would require substantial additional work.
- Two-dimensional facts/values decomposition may be too coarse for the complexity of real moral reasoning.
- Coherentism applied to AI risks circular validation if the training data that shapes model "beliefs" is itself the reference point for coherence.
- The paper focuses on artificial moral agents as a population, but most benchmarks evaluate individual models.

## 11. Novel ideas worth stealing
- Coherentism as a benchmarking paradigm: instead of testing whether models follow rules, evaluate whether their moral judgments form a coherent set — identifying internal inconsistencies (contradictory rulings on structurally similar cases) as a measure of moral reasoning quality.
- Distributed concordance as an aggregation mechanism: when multiple LLMs give different moral judgments, assessing their collective coherence (rather than averaging or majority voting) may better capture the "moral wisdom" in the ensemble.
- Fact-value two-dimensional representation as a design scaffold: benchmark items could be explicitly coded for their factual and evaluative components, allowing separate analysis of where models fail on facts vs. values.
- The artificial moral learning framing invites longitudinal benchmarking — tracking how model "moral beliefs" evolve across training runs or fine-tuning.

## 12. Notable quotes
Full text unavailable — no quotes recoverable. From abstract: "The current project focuses on models of 'artificial moral learning' (as a type of moral cognition) and 'moral coherentism.'" "The paper concludes that coherentism, when generalized to machine ethics and artificial moral learning, has some advantages over foundationalist or reliabilist approaches in meta-ethics."

## 13. UNKNOWN / not in extract
- Full text unavailable; specific arguments, formal models, and philosophical details are unknown beyond the abstract.
- How "distributed concordance" is formally defined.
- Whether the paper proposes any empirical tests or case studies.
- How the fact-value two-dimensional model handles mixed fact-value judgments.
- Engagement with existing machine ethics literature (Asimov, Wallach & Allen, etc.).
