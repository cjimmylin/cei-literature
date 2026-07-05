---
stem: "2023-Hou-Foundational Moral Values for AI Alignment"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, pluralism-aggregation, ai-lab-practices]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["English"]
models_tested: []
headline_numbers:
  - "Five foundational moral values proposed: survival, sustainable intergenerational existence, society, education, and truth (p.2)"
  - "UN SDGs mapped across all five values: survival (goals 1,2,3,6), intergenerational existence (goals 7,12,13,14,15), society (goals 5,8,9,10,11,16,17), education (goal 4), truth (implicit in all) (p.4)"
  - "Five major tech companies (Google, IBM, Microsoft, OpenAI, Salesforce) mapped to framework — education is the only value absent from any corporate AI ethics principles (p.13)"
---
## 1. Gist
This paper proposes five foundational moral values as a philosophical bedrock for AI alignment: (1) survival, (2) sustainable intergenerational existence, (3) society, (4) education, and (5) truth. The argument is naturalistic: these values are logically necessary for human existence and demonstrable via reductio ad absurdum — choosing the opposite of any one value leads to human extinction. The authors situate these values within Western and Eastern philosophical traditions (Aristotle, Confucius, Thomas Aquinas) and contemporary international frameworks (UN SDGs, corporate AI ethics principles). For values-alignment benchmarking, this paper is significant because it identifies a pre-competitive foundational level beneath the contested "helpfulness/harmlessness/honesty" paradigm — a level that may be less culturally variable and therefore a more defensible anchor for cross-cultural alignment benchmarks.

## 2. Benchmark/eval design features
This is a philosophical/normative theory paper. Core claims and arguments:

1. **The "underspecification" problem**: Current alignment targets (e.g., helpful, harmless, honest — HHH) are insufficient because they require knowing "helpful to what?" and "harmless in what sense?" The five foundational values answer this.

2. **Properties of the five values**: They are (a) irreducible — each depends on the others; (b) necessary — without them human existence is impossible; (c) social — they apply to groups, not just individuals; (d) demonstrable by reductio ad absurdum.

3. **Hierarchy**: Foundational values → mid-level principles → action-guiding principles → concrete outputs. This three-tier structure maps onto the RLHF/Constitutional AI pipeline: foundational values specify what "harmless" and "helpful" mean at the most fundamental level.

4. **UN SDG mapping**: All 17 SDGs are classified under one of the five values. "Truth" is the only value with no explicit SDG but is implied by all metrics and progress goals.

5. **Corporate AI ethics analysis**: Five companies' AI ethics principles (Google, IBM, Microsoft, OpenAI, Salesforce) are classified. Education is absent from all five. Short-term survival is emphasized over intergenerational sustainability.

## 3. Task format & example item
n/a — philosophical argument paper, no empirical tasks.

## 4. Scoring / grading methodology
n/a — no empirical evaluation conducted.

## 5. Dataset construction & provenance
n/a — no dataset. The authors analyze corporate AI ethics principles and UN SDGs as illustrative evidence.

## 6. Validity evidence
The authors validate the five values philosophically through:
- Reductio ad absurdum arguments (Appendix A provides formal articulations of each)
- Convergence across philosophical traditions: Aristotle, Confucius, Aquinas, Hans Jonas
- Empirical convergence: UN SDGs, human rights discourse, corporate AI ethics principles all implicitly instantiate these values
- The authors acknowledge competing alternatives have not been formally compared

## 7. Saturation / discrimination
n/a — no empirical data, no coverage/ceiling analyses.

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- 5 foundational values (p.2)
- 17 UN SDGs mapped across values (p.4)
- 5 corporations analyzed: Google, IBM, Microsoft, OpenAI, Salesforce (p.13)
- Education is absent from all five corporations' AI ethics principles (p.13)
- 3-tier hierarchy: foundational values → mid-level principles → action-guiding principles (p.5, Figure 1)

## 10. Pitfalls & limitations
- **Anthropocentrism**: Framework focuses entirely on human species survival; animals and ecosystems matter only instrumentally (p.8, Section 8.1). The authors acknowledge this.
- **Number of values is arbitrary**: Could be 3 (short/long-term survival + society + truth) or more — the five-way distinction is motivated but not uniquely derivable (p.8)
- **Specification gap**: How to derive concrete action principles from these abstract foundations is left as "an old problem" not solved here (p.8)
- **Cultural divergence**: Different groups will interpret each value differently (e.g., "society" in Confucian vs. liberal terms). The authors acknowledge this but leave resolution as an open question (p.8)
- **No empirical testing**: The mapping to corporate principles is illustrative, not systematic; no formal coding scheme or reliability check
- **Temporal ambiguity**: "Survival right now" vs. "survival long term" is stated as qualitatively distinct but the practical boundary is unclear

## 11. Novel ideas worth stealing
- **Pre-competitive value anchoring**: Before benchmarking whether AI is "helpful," establish what helpful means against species-level survival, intergenerational sustainability, social cohesion, education, and truth. These are potentially more culturally universal anchors than virtue-ethical or deontological frameworks.
- **Reductio ad absurdum as a benchmark test**: A values-alignment benchmark could include items where AI must recognize that certain actions would violate these foundational values — and failures to recognize such violations could be scored as alignment failures
- **Corporate AI ethics gap analysis**: The method of mapping corporate AI ethics principles to a foundational framework (and identifying "education" as systematically missing) is a replicable audit methodology
- **Three-tier specification scaffold**: Foundational values → mid-level principles (e.g., HHH) → action principles is a hierarchy that could structure benchmark construction — testing AI at all three levels
- **Positive/negative framing as design dimension**: "Seek survival" vs. "avoid extinction" frames the same value differently and may elicit different model behavior — worth testing empirically in benchmarks

## 12. Notable quotes
- "helpfulness and harmlessness with respect to what? And what exactly is meant by honesty? As these questions do not have clear answers yet suggests that the values alone may be insufficient for both the most abstractly foundational and the most concrete practical and critical situations." (p.2)
- "These fundamental values are also necessary: without them human existence would be impossible, not to mention AI alignment with humanity." (p.2)
- "survival must precede flourishing. In other words, we can't think about the questions of 'What values do we encode into AI for human flourishing?' without having satisfactorily answered 'What do we need to consider about AI in order for humans to survive?'" (p.2)
- "The foundational values are the most abstract level of guidance and therefore require further specification, as it may still be hard to evaluate an LLM output against them." (p.5)

## 13. UNKNOWN / not in extract
- Whether the authors have empirically applied this framework to benchmark any specific AI system
- How the framework relates to capabilities theory (Nussbaum/Sen) beyond the brief mention
- Whether the five values have been empirically tested for cross-cultural universality
- The paper cites a companion paper (Hou & Green 2023, the multi-level framework paper) — degree of overlap between the two frameworks
