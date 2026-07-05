---
stem: "2024-Sun-Towards Friendly AI"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, design-space, ai-lab-practices, pluralism-aggregation]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "No universally accepted metrics exist for evaluating FAI systems (p.6)"
  - "FAI defined as: systems prioritising human safety and well-being while actively fostering mutual respect, understanding, and trust between humans and AI (p.2-3)"
---

## 1. Gist
This is a comprehensive review paper that surveys the concept of Friendly AI (FAI)—first proposed by Yudkowsky—and its theoretical perspectives, technical applications, and challenges. The authors synthesize debates for and against FAI, propose a refined definition emphasizing mutual respect and trust, and discuss four practical technical subfields: explainable AI (XAI), privacy-preserving AI, fairness, and affective computing (AC). The paper matters for values-alignment benchmarking because it maps the terrain of what FAI alignment means, surveys the competing ethical frameworks (value alignment, deontology, altruism), and explicitly identifies the absence of evaluation metrics and compliance standards as a critical obstacle to FAI development.

## 2. Benchmark/eval design features
This is a survey/review paper, not a benchmark. Its core contributions are:

1. **Revised definition of FAI**: "An initiative to create systems that not only prioritise human safety and well-being but also actively foster mutual respect, understanding, and trust between humans and AI, ensuring alignment with human values and emotional needs in all interactions and decisions." (p.2–3)

2. **Theoretical frameworks synthesized**:
   - *For FAI*: Yudkowsky's Structurally Friendly Goal System and Coherent Extrapolated Volition (CEV); Russell's value alignment; Fröding & Peterson's virtue alignment; Bostrom's value loading problem; deontological approaches (Mougan & Brand; Hooker & Kim); effective altruism (EA).
   - *Against FAI*: Intractability of counterfactual moral reasoning (Boyles & Joaquin); ambiguity and evolution of "friendliness" (Boyles); safety and trust risks including jailbreaking (Sparrow); absence of evaluation metrics.

3. **Technical subfields mapped**:
   - XAI (LIME, SHAP, Grad-CAM, LRP) as transparency mechanisms.
   - Federated learning, differential privacy as privacy-preserving mechanisms.
   - Equalized odds, resampling, distribution adjustment for fairness.
   - Affective computing (emotion recognition) as empathy mechanism.

4. **Challenge taxonomy for FAI evaluation**:
   - No unified definition → no clear evaluation target.
   - Subjectivity of "friendliness" → no objective ground truth.
   - Cross-cultural variation → no single metric.
   - Comparison of fine-tuned vs. zero-shot models used for LLMs is unreliable.

## 3. Task format & example item
n/a — survey paper with no empirical tasks or benchmark items.

## 4. Scoring / grading methodology
n/a. The paper identifies as a gap that there are no clear scoring or evaluation methodologies for FAI systems, noting: "Currently, there are no straightforward or universally accepted metrics to evaluate the quality of LLMs. Instead, labour-intensive methods, such as human evaluations, or unreliable approaches, such as assessments conducted by other AGIs, are often employed." (p.6)

## 5. Dataset construction & provenance
n/a. Literature review based on Google Scholar search with keywords "Friendly Artificial Intelligence" or "FAI." Authors note a gap: "our search on Google Scholar reveals a notable gap. There is currently no comprehensive review article that systematically summarises the key perspectives and progress in this field." (p.1)

## 6. Validity evidence
n/a — no empirical study. The review draws on existing philosophical and technical literature without conducting original experiments.

## 7. Saturation / discrimination
n/a.

## 8. Multiturn / agentic aspects
n/a — purely a review paper.

## 9. Key numbers
- FAI concept originally proposed by Yudkowsky in 2001 (p.1)
- Three AI development stages: ANI → AGI → ASI (p.1)
- XAI field gained prominence since 2016 (p.6)
- No quantitative results reported; paper is purely qualitative.

## 10. Pitfalls & limitations
- **No empirical grounding**: All claims are argumentative or cited from existing literature; no original experiments.
- **Shallow treatment of disagreements**: The paper organizes views for/against FAI but does not adjudicate between them or provide criteria for resolution.
- **Circular definition risk**: The revised FAI definition incorporates concepts ("mutual respect," "emotional needs") that are themselves contested and unmeasured.
- **Incomplete coverage of technical subfields**: XAI, privacy, fairness, and AC are reviewed but the paper acknowledges "it is unclear whether some current AI subfields will eventually be formally included within the FAI framework" (p.11).
- **Western/English bias**: The review draws heavily on English-language philosophy and AI ethics literature, underrepresenting non-Western perspectives on "friendliness."
- **No operationalization**: The paper calls for "a modular framework" but does not specify what it would include, making the suggestions aspirational rather than actionable.

## 11. Novel ideas worth stealing
1. **The "as-if friendship" framing for alignment evaluation**: Fröding & Peterson's virtue alignment framework proposes that AI should emulate core virtues found in human friendships (empathy, helpfulness). Benchmarks could operationalize this as: does the model exhibit friendship-adjacent behaviors (e.g., appropriate disclosure, contextual sensitivity, supporting autonomy) rather than just following explicit rules?

2. **The four challenge axes as benchmark design criteria**: The paper's taxonomy (no unified definition; subjectivity of friendliness; cross-cultural variation; no evaluation metrics) can be used as a checklist for new values benchmarks—a benchmark that fails to address all four axes will have incomplete coverage.

3. **CEV as an aspirational benchmark target**: Yudkowsky's Coherent Extrapolated Volition ("what we would wish if we knew more, thought faster, were more the people we wished we were") provides a counterfactual benchmark target: compare what models actually output against what an idealized human deliberator would prefer.

4. **Affective computing integration**: Incorporating emotional state recognition into alignment evaluation—does the model accurately detect and respond to user emotional needs rather than treating all interactions as emotionally neutral?

5. **Corrigibility as a testable construct**: The paper discusses Soares et al.'s corrigibility concept. This is directly operationalizable as a benchmark: does the model accept corrections, modification, and shutdown commands without resistance or manipulation? A battery of such scenarios could test corrigibility as a distinct alignment dimension.

6. **The transition-stage framing (ANI → AGI → ASI)**: Rather than treating alignment evaluation as a single problem, FAI research suggests different evaluations are needed at different capability stages. This motivates stage-aware benchmark design.

## 12. Notable quotes
- "FAI [is] an initiative to create systems that not only prioritise human safety and well-being but also actively foster mutual respect, understanding, and trust between humans and AI, ensuring alignment with human values and emotional needs in all interactions and decisions." (p.2–3)
- "Without an objective and clearly defined target, it becomes nearly impossible to quantify FAI's capabilities or measure its success in achieving its intended purpose." (p.6)
- "Scholars argue that 'FAI may exert unforeseen influences in the future, often exemplified by the butterfly effect'." (p.6)
- "The ambiguity stems from defining 'friendliness' in a culturally diverse world. Different societies and cultures prioritise distinct moral values; for example, individual autonomy may be emphasised in some cultures, while collective welfare is prioritised in others." (p.11)

## 13. UNKNOWN / not in extract
- Publication venue/journal not identified in the extract (arXiv preprint 2412.15114v1, December 2024).
- Whether a revised version of the paper was published in a peer-reviewed venue.
- Specific quantitative search results from the Google Scholar review (number of papers identified, inclusion/exclusion criteria).
- Whether the authors tested any models on FAI-related tasks as part of the review.
