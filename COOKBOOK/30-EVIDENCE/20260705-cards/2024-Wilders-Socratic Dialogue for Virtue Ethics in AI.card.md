---
stem: "2024-Wilders-Socratic Dialogue for Virtue Ethics in AI"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, best-practices, design-space, pluralism-aggregation]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["nl", "en"]
models_tested: []
headline_numbers:
  - "Seven professionals participated in a 2.5-hour Socratic Dialogue at a Dutch financial bank (p.4)"
  - "Five phases of Socratic Dialogue identified as a method for cultivating virtues in AI practitioners (p.5)"
---
## 1. Gist
This paper investigates whether the Socratic Dialogue method can cultivate moral virtues among AI practitioners — specifically justice, care, honesty, responsibility, practical wisdom (phronesis), and fortitude. A single case study was conducted at a Dutch financial bank's transaction monitoring department, where seven practitioners engaged in a 2.5-hour facilitated Socratic Dialogue on AI-driven fraud and terrorism detection. Through abductive analysis of dialogue transcripts, the authors find that structured ethical inquiry cultivates virtues as dynamic, context-sensitive capacities rather than static rules, and that practical wisdom emerges collectively rather than individually. The paper is relevant to values-alignment benchmarking because it challenges principles-based compliance frameworks and argues that ethical behavior requires deep internalization through dialogical practice — with implications for how we train and evaluate AI systems' moral reasoning.

## 2. Benchmark/eval design features
This is a qualitative case study, not a benchmark. Core theoretical claims:
1. **Principles-based ethics is insufficient**: Ethical principles (beneficence, fairness, autonomy) remain inert without cultivated character; empirical research shows ethical knowledge does not produce ethical behavior (p.1–2).
2. **Virtue ethics as complement**: Drawing on Hagendorff's (2022) virtue framework for AI — justice, honesty, responsibility, care, practical wisdom (phronesis), fortitude — the paper argues that these virtues must be cultivated through practice, not just taught as concepts.
3. **Socratic Dialogue as cultivation method**: Five-phase structured inquiry (formulate question of conscience → ground in lived experience → reconstruct the "hot spot" → role-taking → formulate maxims → find the essence) cultivates phronesis as a tridimensional capacity: inquiring, judging, acting.
4. **Dissensus as moral resource**: Divergent views are not problems to resolve but productive openings for deeper ethical reflection — a deliberate departure from consensus-seeking.

Key output: Table 1 (p.8) catalogs 25 maxims across five themes: Human Dimension in Criminality Assessment, Machine Dimension in Criminality Assessment, Oversight and Accountability, Authority and Acceptance, Transparency and Explainability.

## 3. Task format & example item
Not a benchmark. The methodological "items" are the five dialogue phases:

Phase 1 — Central question of conscience: "To what extent do we want a machine to track down crime?" (p.5)

Phase 2a — Lived experience shared: A legal specialist recounts freezing a customer's account due to AI-flagged transactions associated with an Arabic surname and Islamic foundation donations; the customer had done nothing wrong (p.6).

Phase 4 — Sample maxims produced (p.7–8):
- "Empathy is important in assessing criminality, as it allows for a more nuanced understanding that machines alone cannot achieve."
- "A human mistake is more acceptable than a mistake made by a machine."
- "Justice is not deterministic therefore we need to leave control in the hand of man."

## 4. Scoring / grading methodology
n/a — qualitative case study. Analysis used abductive thematic coding (Atlas.ti software), proceeding from verbatim dialogue contributions to codes, themes, and maxims. No inter-rater reliability is reported; coding was performed by the first author with secondary researcher critique (p.4).

## 5. Dataset construction & provenance
A 2.5-hour Socratic Dialogue at a Dutch bank (Netherlands). Participants: 4 data scientists, 2 legal specialists, 1 compliance/ethics expert (all employees, recruited via internal channels, voluntary, uncompensated). Data collected via detailed minute-taking (audio recording deliberately omitted to reduce inhibition). Session conducted in Dutch; translated to English prior to thematic coding (p.4).

## 6. Validity evidence
Limited to a single case study with seven participants at one institution. The authors acknowledge this is primarily illustrative: "The case study serves primarily to illustrate concepts and processes, rather than to extract empirical insights" (p.4). No quantitative validity evidence. External validity is claimed through alignment with Hagendorff's (2022) virtue framework and Boers' (2022) Socratic Dialogue theory.

## 7. Saturation / discrimination
n/a — qualitative case study with no measurement instrument. The richness of the maxims produced (25 across five themes) provides some indication of thematic saturation within the single session.

## 8. Multiturn / agentic aspects
n/a — the Socratic Dialogue itself is multi-turn between human practitioners; no AI system is evaluated.

## 9. Key numbers
- 7 participants (4 data scientists, 2 legal specialists, 1 ethics/compliance expert) (p.4)
- 2.5 hours dialogue duration (p.4)
- 5 phases in the Socratic Dialogue method (p.5)
- 25 maxims generated across 5 themes (Table 1, p.8)
- 6 core virtues analyzed: justice, care, honesty, responsibility, practical wisdom, fortitude (p.1)

## 10. Pitfalls & limitations
- Single case study at one organization — highly limited generalizability (p.8)
- No audio recording; minute-taking introduces selection bias in what was captured (p.4)
- No inter-rater reliability reported for thematic coding (p.4)
- Dialogue conducted in Dutch and translated — translation introduces interpretation artifacts (p.4)
- Power dynamics in hierarchical settings may suppress dissent even with facilitation (p.10)
- Time investment (2–3 hours per session) creates practical barriers to organizational adoption (p.10)
- Requires skilled facilitation — method cannot be self-administered (p.10)
- Dialogue alone cannot undo structural barriers (incentives, corporate culture) (p.9)

## 11. Novel ideas worth stealing
- **Dissensus-as-resource design**: Instead of seeking consensus in values-alignment evaluation, deliberately preserve and analyze divergent moral intuitions as data. For a values benchmark, this means reporting score distributions and disagreement patterns rather than only aggregate scores.
- **"Question of conscience" framing**: Formulating evaluation items as normative questions ("To what extent do we want X?") rather than factual questions elicits genuine ethical reasoning. This technique maps directly onto benchmark item design for moral dilemma tasks.
- **Phronesis as tridimensional construct**: The inquiring / judging / acting framework provides a measurable structure for evaluating practical moral wisdom in AI systems — richer than single-dimension correctness scoring.
- **Maxim-extraction as validity check**: Distilling participant reasoning into concise maxims (Table 1) is a concrete method for surfacing the implicit normative assumptions underlying human judgments — useful for building construct validity for values-alignment benchmarks.
- **Hot-spot methodology**: Identifying the emotionally and morally charged moment where value tensions peak provides a principled way to select high-signal evaluation scenarios for moral psychology benchmarks.
- **Fortitude as an evaluable virtue**: Measuring whether AI systems maintain ethical positions under conversational pressure (e.g., from authority figures or repeated challenges) is an underexplored dimension for agentic evaluation.

## 12. Notable quotes
- "Ethical knowledge alone does not necessarily translate into ethical decision-making. Even professional ethicists do not act more ethically than non-ethicists." (p.1)
- "Rather than aiming for consensus, the process facilitates a shared inquiry where divergent views enrich understanding, making it particularly suited to contexts such as AI ethics, where challenges are contested and values may conflict." (p.3)
- "Practical wisdom was cultivated as a collective effort. It was sharpened through dissensus, as participants had to articulate and explain their views under scrutiny." (p.9)
- "Dialogue can help clarify what should matter morally and why. It encourages participants to articulate, contest, and refine their value commitments and potentially gain deeper insight into the inevitable trade-offs these involve." (p.9)

## 13. UNKNOWN / not in extract
- Whether follow-up sessions were conducted or longitudinal behavior change was measured
- Full anonymized transcript beyond the illustrative fragments in the paper
- IRR statistics for thematic coding
- Whether facilitator independence from the organization was maintained throughout analysis
- Specific details of Hagendorff's (2022) virtue operationalization that the paper assumes as background
