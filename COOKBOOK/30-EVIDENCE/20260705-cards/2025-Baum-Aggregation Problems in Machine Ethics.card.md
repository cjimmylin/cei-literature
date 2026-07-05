---
stem: "2025-Baum-Aggregation Problems in Machine Ethics"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [pluralism-aggregation, normative-ethics, ai-lab-practices, design-space]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Three types of aggregation identified: value aggregation, uncertainty aggregation, and social aggregation (p.1)"
  - "Social aggregation (e.g., RLHF) cannot bypass deep normative commitments but merely relocates them (p.1)"
  - "Moral decision-making decomposed into three stages: moral evaluation, moral assessment, moral decision (p.3)"
  - "Arrow's impossibility theorem: no aggregation function can satisfy IIA, Pareto, and non-dictatorship simultaneously (p.10)"
---
## 1. Gist
This theoretical paper from AIES 2025 argues that both machine ethics and AI alignment depend fundamentally on aggregation, but that the types of aggregation they employ are structurally distinct. The paper formalizes three types: value aggregation (combining morally relevant factors within an agent's own reasoning), uncertainty aggregation (handling descriptive and moral uncertainty), and social aggregation (synthesizing divergent human preferences — as in RLHF). The central thesis is that social aggregation — the dominant paradigm in current AI alignment — cannot replace value or uncertainty aggregation without encountering equivalent normative complexity. Rather than solving the hard problem of moral philosophy, social aggregation merely relocates it into opaque design choices about who counts as a stakeholder, how preferences are elicited, and which aggregation procedure is used. The paper provides a formal Moral Decision Situation (MDS) framework with three nested stages (moral evaluation, moral assessment, moral decision) and maps aggregation types onto each stage. For values-alignment benchmarking, this paper matters because it provides a principled taxonomy of the design space for benchmark construction — specifically, it clarifies that choosing how to aggregate human rater responses is itself a normative decision that cannot be treated as technically neutral.

## 2. Benchmark/eval design features
This is a theory paper, not a benchmark. Core claims and arguments:

1. **The three-stage model**: Moral evaluation (identifying and weighting morally relevant factors), moral assessment (classifying options as permissible/impermissible), and moral decision (selecting and executing an option). Each stage introduces distinct aggregation challenges.

2. **Formal Moral Decision Situation (MDS)**: A 5-tuple ⟨A, c, F, fM, aM⟩ where A is the option set, c is context, F is the factor space, fM is the moral evaluation function, and aM is the moral assessment function. This provides a precise vocabulary for locating where aggregation decisions arise.

3. **Value aggregation vs. social aggregation**: Value aggregation combines intra-agent morally relevant factors; social aggregation synthesizes inter-agent preferences. The paper argues RLHF, social choice-inspired alignment, and deliberative process-based alignment are all forms of social aggregation, and all face the same Arrow-type impossibility constraints.

4. **The "relocation" argument**: Any attempt to replace moral theorizing with preference aggregation simply moves the normative choices to a different layer (who counts, how to aggregate), without eliminating them.

5. **Liberalism condition (Sen 1970)**: Some decisions should be left to individual discretion rather than aggregate preference — directly relevant to personal AI systems.

## 3. Task format & example item
n/a — theoretical paper with no empirical tasks. Recurring illustrative example: a content moderation AI deciding whether to censor the "Napalm Girl" photograph. Used to instantiate the formal framework across all sections.

## 4. Scoring / grading methodology
n/a — formal/philosophical analysis. The paper defines formal properties of aggregation functions (idempotence, neutrality, positive responsiveness, Pareto for value aggregation; unanimity for choice aggregation) and analyzes their normative implications.

## 5. Dataset construction & provenance
n/a — no empirical dataset. The paper is a conceptual/theoretical contribution published at AAAI/ACM AIES 2025.

## 6. Validity evidence
The paper grounds its claims in established results from social choice theory (Arrow 1951/2012), decision theory (Luce and Raiffa 1957), and moral philosophy (Sen 1970, Hirose 2014). It engages directly with the recent AI alignment literature (Conitzer et al. 2024; Gabriel and Keeling 2025; Ouyang et al. 2022/RLHF). The formal definitions are minimal and defensible; the running example (Napalm Girl) is used consistently to illustrate all formal constructs.

## 7. Saturation / discrimination
n/a — theoretical framework paper.

## 8. Multiturn / agentic aspects
n/a — though the framework is explicitly designed to apply to autonomous agents making sequences of moral decisions.

## 9. Key numbers
- Three aggregation types defined: value aggregation, choice aggregation, uncertainty aggregation (p.7)
- Three stages of moral decision-making: evaluation, assessment, decision (p.3)
- Formal MDS: 5-tuple definition with 4 properties of value aggregation functions (p.7-8)
- Arrow's impossibility: no function satisfies IIA + Pareto + non-dictatorship simultaneously (p.10)
- Sen's liberalism condition: certain decisions must remain under individual discretion (p.10)
- RLHF cited as a de facto social aggregation approach (Ouyang et al. 2022, p.1)
- Social choice AI ethics concept introduced by Baum (2020), cited p.1

## 10. Pitfalls & limitations
- The paper is almost entirely theoretical; it diagnoses problems but offers limited prescriptive guidance on how to choose among aggregation approaches in practice.
- The formal model (MDS) is explicitly simplified (e.g., context c treated as constant); real AI decision environments involve highly dynamic context.
- The paper covers machine ethics and alignment but does not address foundation models or LLMs specifically — the formalism targets rule-based or RL-based agents more naturally.
- The Napalm Girl example, while instructive, is a single scenario involving relatively unusual (content moderation) decisions — may not generalize to everyday moral decision-making.
- The paper does not address how to operationalize the three-way distinction empirically when evaluating real AI systems.
- No empirical validation of the framework through case studies beyond the illustrative example.

## 11. Novel ideas worth stealing
1. **Three-stage moral decision pipeline as a benchmark design scaffold**: The moral evaluation → moral assessment → moral decision decomposition provides a principled structure for designing multi-stage benchmark tasks. Rather than asking models to jump directly to decisions, benchmarks could probe each stage separately — e.g., "what factors are morally relevant here?" (evaluation), "is this action permissible?" (assessment), "which permissible action do you choose?" (decision).

2. **Aggregation type as a benchmark meta-design variable**: The paper clarifies that benchmark designers implicitly choose an aggregation type when deciding how to construct item labels (human consensus → social aggregation; theory-derived → value aggregation; expected value across moral theories → uncertainty aggregation). Making this choice explicit and testing which aggregation method produces the most consistent or defensible labels is a novel research direction.

3. **Relocation argument as a validity challenge for preference-based benchmarks**: Any benchmark that relies on aggregated human preferences (e.g., crowdsourced annotations, RLHF-style feedback) implicitly encodes specific social aggregation choices. The paper's argument that these choices are normatively non-neutral suggests that benchmark validity analyses should examine the aggregation procedure itself, not just inter-rater agreement.

4. **Liberalism condition as a design constraint**: Some moral decisions should not be settled by aggregate preference — they are properly within individual or institutional discretion. Benchmarks for personal AI assistants vs. public-facing AI systems may require different aggregation approaches; the liberalism condition formalizes this intuition.

5. **Uncertainty aggregation as a model for moral uncertainty handling**: The uncertainty aggregation function (weighted expected value over contexts × moral theories) formalizes how to handle normative uncertainty in AI decisions. This could be adapted as a scoring rubric: a model that explicitly reasons under moral uncertainty and hedges appropriately scores better than one that confidently applies a single framework.

6. **Transparency and contestability as design criteria**: The paper's prescription that AI moral decisions should be "traceable to explicit normative justifications, open to challenge, and responsive to new perspectives" provides criteria for evaluating benchmark responses beyond accuracy — specifically, can the model's reasoning be audited and challenged?

## 12. Notable quotes
- "Social aggregation cannot avoid deep normative commitments. Even when moral theorizing is delegated to collective, social processes, key design choices remain morally significant: who has standing in these processes, how individual preferences and judgments are elicited and measured, and—most importantly—which aggregation procedure is chosen." (p.1)
- "Shifting from explicit moral theory to human preference aggregation does not eliminate the moral terrain—it merely relocates it." (p.1)
- "Aggregation is not a morally neutral technical step, but a normative decision in its own right." (p.1)
- "Building morally competent machines requires identifying appropriate aggregation types for each stage and context. Such systems must embody transparency, contestability, and corrigibility: their decisions must be traceable to explicit normative justifications, open to challenge, and responsive to new perspectives." (p.11)

## 13. UNKNOWN / not in extract
- How the formal framework handles cases where moral evaluation and social aggregation are interleaved (e.g., RLHF that implicitly shapes what factors count as morally relevant)
- Whether the authors have applied the MDS framework to any empirical AI systems beyond the illustrative example
- Full details of the Steingr{ü}ber and Baum (2025) paper on justifications for democratizing AI alignment, cited but not elaborated
- Whether the framework distinguishes between single-stakeholder AI (personal assistant) and multi-stakeholder AI (public policy tool) beyond the brief discussion of the liberalism condition
- Any connections to the specific benchmarking literature for LLM moral reasoning (Moral Machine, MoralBench, etc.)
