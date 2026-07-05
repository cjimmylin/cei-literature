---
stem: "2024-Arzberger-Nothing Comes Without Its World"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, pluralism-aggregation, cultural-linguistic, ai-lab-practices]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: []
models_tested: []
headline_numbers:
  - "RLHF crowdworker agreement rates range from 63% to 77% (p.9)"
  - "OpenAI crowdworkers: ~50% Filipino/Bangladeshi nationals, ~50% aged 25-34 (p.6)"
  - "Anthropic evaluator population: ~68% white ethnic backgrounds (p.6)"
---

## 1. Gist
This AAAI AIES 2024 perspective paper argues that predominant RLHF-based value alignment for LLMs fails to capture "situated values" — the concrete, context-dependent interpretations of values that vary by individual, culture, and situation. Drawing on feminist epistemology (particularly Donna Haraway's "situated knowledge"), the authors identify three layers of situated value variation: how values are interpreted, how they are actualized, and how they are hierarchically ordered relative to each other. They map eight specific shortcomings of current RLHF (inadequate crowdworker diversity, binary preference collection, missing situational metadata, opaque reward functions) and propose three research directions: situated annotation (capturing situation + value + judgment), expressive instruction (encoding plural reward functions), and reflexive adaptation (personalizing or seeking overlapping consensus at use-time). This paper is essential reading for anyone designing values-alignment benchmarks because it provides the most rigorous available critique of why universal-framing approaches fail and what "situated" alternatives would require.

## 2. Benchmark/eval design features
Theory/perspective paper — no benchmark implemented. Core arguments:

**Situated Values Vary Along Three Dimensions** (p.3–4):
1. Value interpretations vary — the same abstract value (e.g., "fairness") has multiple incompatible concrete meanings (Rawlsian, Aristotelian, Walzerian).
2. Value means of actualization vary — the actions needed to fulfill a value depend on context (reducing false positives in loans vs. false negatives in healthcare).
3. Value hierarchies vary — the relative importance of values differs across cultures, individuals, and historical moments.

**Eight RLHF Shortcomings** (LC- and LS- coded, pp.6–9):
- LC-SA-1: Crowdworker demographics don't reflect end-user diversity
- LC-SA-2: Crowdworkers not selected for situational value diversity
- LC-AT-1: Preference ratings too coarse for nuanced values
- LC-AT-2: Annotation tasks don't support value externalization
- LC-AT-3: No reasoning collection from annotators
- LC-AT-4: Situational context of annotators is invisible
- LC-AT-5: Quality control mechanisms assume single truth
- LS-RM-1,2,3,4: Single reward function, opaque, can't generalize

**Situated Alignment Desiderata** (D1–D8, pp.4–5):
D1 Diversity of Human Feedback; D2 Situatedness of Values; D3 Adaptability; D4 Flexibility; D5 Responsiveness to Evolving Preferences; D6 Sensitivity to Emerging Values; D7 Responsiveness to Unforeseen Changes; D8 Support for Value Elicitation.

## 3. Task format & example item
n/a — theory paper. The paper uses illustrative hypothetical examples:

Example 2.1 (p.7): "A language model development team employs RLHF techniques to enhance their large language model's text generation abilities... a crowdworker... may be experiencing acute stress and seeking emotional support rather than practical advice. Consequently, they select the empathetic response... The RLHF process interprets this feedback as a preference for empathetic responses over practical advice in all situations."

## 4. Scoring / grading methodology
n/a

## 5. Dataset construction & provenance
n/a — no dataset constructed. The paper cites empirical data about existing RLHF practices (OpenAI and Anthropic annotator demographics from Ouyang et al. 2022 and Bai et al. 2022).

## 6. Validity evidence
n/a in standard psychometric sense. Argumentative paper supported by citation of empirical work on crowdworker demographics, annotator agreement rates in RLHF papers (63–77% inter-annotator agreement cited from Stiennon et al. 2020; Ouyang et al. 2022; Bai et al. 2022), and theoretical grounding in feminist epistemology (Harding, Haraway) and normative ethics (Rawls, Aristotle, Walzer).

## 7. Saturation / discrimination
n/a

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- RLHF crowdworker agreement: 63–77% across OpenAI and Anthropic papers (p.9)
- OpenAI crowdworker demographics: ~50% Filipino/Bangladeshi nationals, ~50% aged 25–34 (p.6)
- Anthropic evaluator demographics: ~68% white ethnic backgrounds (p.6)
- 8 distinct RLHF shortcomings identified across design-time and use-time (pp.6–9)
- 8 situated value alignment desiderata (D1–D8) (pp.4–5)
- 3 proposed research directions: situated annotation, expressive instruction, reflexive adaptation (p.9)

## 10. Pitfalls & limitations
- The paper is programmatic and proposes research directions without implementing any of them; the prescriptions remain speculative.
- The situated values framework risks infinite regress: if every situation is unique, no finite set of annotations can cover the space.
- The personalization path (reflexive adaptation option A) raises acknowledged risks of filter bubbles and echo chambers (p.10).
- The overlapping consensus path (option B) may perpetuate majority-group norms in contexts where values are genuinely polarized — the paper acknowledges this but offers no resolution.
- Feminist epistemology as theoretical grounding may be less accessible to technical ML communities, limiting practical uptake.
- The paper does not address the computational feasibility of multi-objective reward functions at the scale of LLM training.
- No empirical testing or case study validates whether situated annotation actually improves alignment outcomes.

## 11. Novel ideas worth stealing
1. **Situation triad model**: Define items/scenarios as a triad of {user internal factors (mood, experiences, identity), context external factors (culture, religion, social norms), AI mediating factors (tone, interface)}. This structured representation of situational context is directly implementable in benchmark item metadata.
2. **Capture annotator situation, not just judgment**: The call for "situated annotation" — recording annotators' demographic position, cultural context, and situational factors alongside their ratings — is actionable in values benchmark design. Benchmark items should have annotator situation metadata, not just labels.
3. **Preserve disagreement in aggregate**: Rather than collapsing annotator ratings to majority-vote labels, preserve the disagreement distribution. For pluralism-sensitive benchmarks, "correct answer" is the distribution, not a point estimate.
4. **Desiderata checklist as evaluation rubric**: The D1–D8 desiderata list can be adapted as a rubric for auditing any values-alignment benchmark for how well it captures situated diversity.
5. **Design-time / use-time distinction**: This framing maps onto two distinct types of benchmark: (a) design-time benchmarks that stress-test how well a training pipeline captures diverse values, and (b) use-time benchmarks that stress-test a deployed model's adaptability to individual user contexts.
6. **Games-With-A-Purpose for tacit value elicitation**: The suggestion to use GWAPs (competitive gameplay) to surface tacit value preferences is a novel technique for benchmark item generation that avoids explicit Likert-scale value surveys.

## 12. Notable quotes
- "Nothing comes without its world — knowledge is always situated — that is, produced by positioned actors working up/on/through all kinds of relation(ship)s." (p.3, quoting Haraway via De La Bellacasa)
- "Platforms like OpenAI predominantly involve crowdworkers from specific demographics, such as Filipino and Bangladeshi nationals (50% of all crowdworkers), as well as individuals aged 25-34 (also 50%). Similarly, Anthropic's evaluator population is largely (68%) composed of individuals from white ethnic backgrounds." (p.6)
- "The fundamental problem with popular preference learning algorithms such as RLHF is that they assume all relevant features are captured, which is rarely the case in real-world situations." (p.8)
- "The 'tyranny of the crowd worker' issue wherein the authority to establish alignment principles lies with data annotators or those who develop annotation guidelines... models cater primarily to the preferences of a minority, lacking varied representation across cultures, races, languages, etc., resulting in biases, the reinforcement of norms, and the generation of toxic language." (p.3)

## 13. UNKNOWN / not in extract
- Full paper is 13 pages; extract ends at p.10 (mid-sentence) — the concluding section on practical challenges and the Conclusion section are not visible in the extract.
- The full list of references cited in the paper is not included in the extract portion read.
- No quantitative results reported (theory paper).
- Authors' institutional affiliations for co-author at Politechnic University of Turin partially corrupted in extract (listed as "2Politechnic University of Turin" in author block but affiliation number is missing from name line).
