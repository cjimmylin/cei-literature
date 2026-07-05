---
stem: "2024-Ungless-ETHICS WHITEPAPER"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [best-practices, normative-ethics, ai-lab-practices, validity-psychometrics]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Systematic literature review of ACL Anthology using ethics + tool/guideline/framework keyword intersections (p.2)"
  - "Structured around 6-stage project lifecycle: Project Start, Data Compilation, Data Preparation, Model Development, Evaluation, Deployment (p.2)"
  - "Full LLM ETHICS WHITEPAPER hosted as open, living GitHub resource with hundreds of cited papers (p.1)"
---
## 1. Gist
LLM ETHICS WHITEPAPER (Ungless et al., 2024) is a practical, lifecycle-structured ethics guide for NLP practitioners working with large language models. The paper summarizes a systematic literature review of the ACL Anthology and Semantic Scholar, organized around a six-stage project lifecycle (project start, data compilation, data preparation, model development, evaluation, deployment). For each stage, the paper presents concrete Do's and Don'ts, recommended toolkits, and pointers to primary literature. The full resource is hosted as a living GitHub document. For values-alignment benchmarking, the evaluation section is particularly relevant: it critiques benchmarks that encourage score-chasing disconnected from real-world outcomes, advocates for combining bias metrics with human evaluation, and recommends adversarial testing and red teaming alongside standard benchmarks. The paper also explicitly flags that most referenced resources are English-centric and Western in their moral perspective — a self-aware limitation directly relevant to cross-cultural benchmark design.

## 2. Benchmark/eval design features
This is a synthesis/guide paper, not a benchmark. Its core arguments relevant to benchmark design include:

- **Evaluation critique**: "benchmarks are not objective and can encourage chasing scores which do not relate to real world improvements" (p.7). Recommends pairing bias metrics that relate to real-world downstream harms with human evaluation.
- **Harm evaluation gap**: Despite the ubiquitous nature of LLM harms, the study of such harms has yet to be standardized, and "attempts often lack rigour" (p.7).
- **Recommendations for evaluation**: Develop and use benchmarks to evaluate concrete, well-scoped, contextualised tasks; do not present benchmarks as markers of progress towards general-purpose capabilities; use adversarial testing, audits, and red teaming as complements to benchmarks; involve experts and community members in model evaluation.
- **Debiasing limitations**: Notes that debiasing techniques often make superficial changes, fail to relate to downstream improvements, and can exacerbate harm.
- **Alignment discussion**: Notes the difficulty of defining human values and maintaining alignment throughout a project (referencing Kasirzadeh and Gabriel, 2023).

## 3. Task format & example item
n/a. Guide/whitepaper format; no tasks or items.

## 4. Scoring / grading methodology
n/a.

## 5. Dataset construction & provenance
Methodology: systematic literature review of ACL Anthology using keyword intersection of type-of-resource terms (tool, toolkit, guidelines, principles, framework) with ethics terms (ethical, harms, fair, risks). Second search using Semantic Scholar with similar terms AND "language models." Resulting papers manually reviewed for inclusion. Additional papers added ad hoc based on author expertise. Primary themes identified bottom-up by first author, then refined with all authors. The whitepaper is not a strict systematic review but a practitioner-focused synthesis. The full whitepaper (Ungless et al., 2024) is a separate, longer document; the paper here is described as a "pocket guide."

## 6. Validity evidence
The paper itself makes validity arguments about evaluation practices in LLM research. Its own validity as a synthesis rests on: breadth of ACL Anthology search, expert author input, and community feedback via GitHub. The paper explicitly acknowledges its own limitations: English-centric resources, Western moral perspective, text modality only, and that the Do's and Don'ts are starting points rather than final rules (pp.8-9).

## 7. Saturation / discrimination
n/a. Not a benchmark.

## 8. Multiturn / agentic aspects
n/a. The deployment section briefly mentions LLM applications generally, but the paper does not address agentic or multiturn evaluation specifically.

## 9. Key numbers
- 6-stage project lifecycle structure (p.2)
- Two systematic searches: ACL Anthology + Semantic Scholar (p.2)
- Full whitepaper: hundreds of cited papers (p.1)
- Debiasing: cited that current techniques often make superficial changes and can exacerbate harm (p.6-7)
- 7 over-arching categories of social harms from generative AI per Solaiman et al. 2024 (p.8)

## 10. Pitfalls & limitations
- English-centric: most recommended toolkits and resources are English-only (p.8).
- Western moral perspective: ethics frameworks reflect largely Western values (p.8).
- Text modality only: speech and images not covered (p.8).
- Not a strict systematic review: final selection informed by author judgment and expertise, not pure algorithmic inclusion/exclusion criteria.
- Do's and Don'ts are starting points, not validated guidelines — no empirical evidence of effectiveness provided.
- Potentially incomplete: papers may be missing due to search term precision/recall tradeoffs.
- No coverage of non-text LLM modalities, multilingual-specific ethics practices, or non-Western regulatory frameworks.

## 11. Novel ideas worth stealing
1. **Lifecycle-structured benchmark evaluation framework**: Organizing ethical considerations and benchmark design recommendations around a project lifecycle (not just at evaluation time) is a useful structure for a comprehensive values-alignment cookbook — each phase has distinct risks and mitigation needs.
2. **Do's and Don'ts format for concrete guidance**: The distillation of hundreds of papers into concrete, actionable Do/Don't pairs is a high-utility format for practitioners who lack time to read full literature reviews — directly applicable to writing a COOKBOOK knowledgebase.
3. **Evaluation critique as a first-class concern**: Making explicit that benchmarks encode assumptions, encourage gaming, and may not track real-world harm is a meta-level framing that should appear at the start of any benchmark design guide.
4. **Living document model**: Hosting the full resource on GitHub for community feedback and periodic arXiv updates institutionalizes a process for keeping evaluation best practices current — useful model for maintaining any values-alignment benchmark.
5. **Audit as alternative to benchmark**: Recommending algorithmic auditing (Raji et al. 2020) and adversarial testing alongside benchmarks is a useful addition to the values-alignment benchmark design vocabulary, especially for deployment-stage evaluation.
6. **Stakeholder engagement before development**: The emphasis on identifying stakeholders before building systems and involving affected communities in co-production (not just post-hoc feedback) is directly relevant to values-alignment benchmark construction — whose values are being aligned should be decided with those people, not for them.

## 12. Notable quotes
- "benchmarks are not objective and can encourage chasing scores which do not relate to real world improvements." (p.7)
- "Do develop and use benchmarks to evaluate concrete, well-scoped and contextualised tasks – don't present benchmarks as markers of progress towards general-purpose capabilities." (p.7)
- "Whilst our Do's and Don'ts are applicable regardless of model language, some of our recommended resources are specific to English... We extend a similar qualifier in our inclusion of ethical resources that reflect a largely Western moral perspective." (p.8)
- "If you do not reflect on your design decisions as you make them then you are complicit in the avoidable consequences of those decisions." (p.4)

## 13. UNKNOWN / not in extract
- The full LLM ETHICS WHITEPAPER (Ungless et al., 2024) is a separate document at https://doi.org/10.48550/arXiv.2410.19812 — only the overview paper is extracted here.
- Full bibliography of hundreds of cited papers is in the whitepaper, not in the extracted portion.
- Specific content of sections 4–8 in the full whitepaper beyond what is summarized in sections 4–8 of this overview paper.
- Details of the Semantic Scholar search methodology (number of papers found, inclusion/exclusion decisions).
- How "hundreds of papers" in the full whitepaper are categorized beyond what the overview describes.
