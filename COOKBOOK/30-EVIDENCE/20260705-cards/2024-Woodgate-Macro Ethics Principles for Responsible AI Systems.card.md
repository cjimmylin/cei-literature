---
stem: "2024-Woodgate-Macro Ethics Principles for Responsible AI Systems"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, design-space, pluralism-aggregation, best-practices]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Taxonomy of 21 normative ethical principles identified across AI and computer science literature (p.1)"
  - "81 papers included across three systematic literature review searches (2022, 2023, 2024) (p.5)"
  - "Utilitarianism is the most frequently cited principle; do no harm is among the least cited (p.8)"
---
## 1. Gist
Woodgate and Ajmeri present a systematic survey of normative ethical principles used in AI and computer science, producing a taxonomy of 21 principles organized under deontology, virtue ethics, and consequentialism — with a macro ethics framing that emphasizes social context. The paper distinguishes between "ethical principles" (operationalizable rules from normative philosophy) and "AI principles" (high-level aspirations like fairness, transparency, and accountability), arguing that the latter cannot be implemented without grounding in the former. Each of the 21 principles is analyzed by definition, prior operationalization in AI, and known difficulties. The paper is valuable for values-alignment benchmarking as a comprehensive reference for what normative structures have been formally operationalized in AI systems, which principles remain underused, and where principle conflicts and implementation gaps persist.

## 2. Benchmark/eval design features
This is a systematic survey and taxonomy paper, not a benchmark. Core contributions:
1. **Taxonomy of 21 ethical principles** arranged as a tree (Figure 1, p.6) under three branches: Deontology (with sub-types: Egalitarianism → Non-Maleficence, Equality of Opportunity, Luck, Autonomy; Proportionalism → Libertarian, Desert-Based; Kantian); Virtue Ethics; Consequentialism (Utilitarianism → Act, Hedonic Act, Rule; Maximin; Envy-Freeness; Doctrine of Double Effect; Do No Harm → Do No Instrumental Harm).
2. **Six contribution types** categorized: descriptive, model representation, individual decision making, centralised collective decision making, decentralised collective decision making, ethics in human-AI interaction.
3. **Four evaluation types**: test (empirical), proof (formal verification), informal (example/scenario comparison), none.
4. **Key finding**: Utilitarianism and broad deontology dominate the literature; virtue ethics and do-no-harm remain comparatively underused; decentralised collective decision making and human-AI interaction are underexplored; non-Western ethical frameworks are entirely absent from the existing literature.

## 3. Task format & example item
n/a — systematic survey. The closest to an "item" is the taxonomy itself (Figure 1) and the principle definitions with operationalization examples in Sections 3.2–3.5. For instance, for egalitarianism: "Lee et al. [87] utilise egalitarianism to evaluate various algorithmic fairness metrics, such as predictive parity or equal odds" (p.10).

## 4. Scoring / grading methodology
n/a — literature review, not a benchmark. Papers are categorized by contribution type, evaluation type, and principles explicitly mentioned. No quantitative scores are reported for the papers themselves.

## 5. Dataset construction & provenance
Systematic literature review following Kitchenham and Charters guidelines. Three search rounds: May 2022 (57 papers selected from ~3.74M Google Scholar results), January 2023 (+10 papers), February 2024 (+14 papers). Total: 81 papers. Search resources: University of Bristol library + Google Scholar. Inclusion/exclusion criteria and snowballing technique applied. Secondary researcher critique used for selection validation.

## 6. Validity evidence
The paper's validity is that of a systematic review: reproducible search methodology, explicit inclusion/exclusion criteria, secondary reviewer checking. No inter-rater reliability is formally reported. Coverage is deliberately limited to AI and computer science literature — philosophical literature is cited for context but not systematically searched.

## 7. Saturation / discrimination
n/a — taxonomy paper. The three iterative search rounds with diminishing new principles suggest some saturation in the literature coverage. The authors explicitly note that non-Western ethical frameworks would require "whole taxonomies of their own" (p.19) — a clear boundary on coverage.

## 8. Multiturn / agentic aspects
n/a — survey paper. However, Section 3.1 notes that decentralised collective decision making (multi-agent systems) is one of the least studied application contexts, indicating a gap directly relevant to agentic values-alignment evaluation.

## 9. Key numbers
- 21 normative ethical principles in the taxonomy (p.1)
- 81 total papers in the systematic review (p.5)
- 3.74 million Google Scholar results from initial search (p.5)
- 6 contribution types classified (p.5)
- 4 evaluation types classified (p.6)
- Utilitarianism appears in the most papers across the taxonomy; Do No Harm in the fewest (p.8, Table 2)
- 3 main search rounds: May 2022, January 2023, February 2024 (p.5)

## 10. Pitfalls & limitations
- Limited to AI and computer science literature — philosophy literature referenced but not systematically searched (p.2)
- Non-Western ethical frameworks explicitly excluded due to scope, despite their relevance to cross-cultural AI deployment (p.19)
- "Ethic of care" excluded due to classification ambiguity, despite its AI relevance (p.18–19)
- Egoism excluded because it was rarely mentioned and likely to produce unethical outcomes — a normative exclusion in a descriptive taxonomy (p.18)
- Three-round search may miss very recent work; latest search was February 2024
- Papers are categorized by which principles they "explicitly mention" — implicit operationalization of principles may be missed
- No measurement of how well any operationalization actually works in practice

## 11. Novel ideas worth stealing
- **Ethical principles vs. AI principles distinction**: The paper's key conceptual move — distinguishing operationalizable philosophical rules from high-level AI aspirations — maps directly onto benchmark design: a values-alignment benchmark should operationalize specific ethical principles, not just invoke vague "fairness" or "safety" labels.
- **Taxonomy as item scaffold**: The 21-principle taxonomy provides a principled vocabulary for tagging benchmark items by which ethical principle they test — enabling structured gap analysis of existing benchmarks.
- **Macro ethics framing**: Building benchmarks that incorporate social context (values, norms, power relations) rather than evaluating ethical reasoning in isolation — a design principle for scenario construction.
- **Principle-specific operationalization tables**: Tables 6–7 map each principle to specific technical implementations (logical reasoning, RL, optimization, etc.) — directly usable for deciding which scoring mechanism is appropriate for each principle in a benchmark.
- **Contribution × Evaluation type matrix**: Tables 1–2 provide a ready-made classification scheme for organizing benchmark papers by what they claim to measure and how they validate it — reusable as a benchmark meta-review framework.
- **Non-Western ethics as explicit gap**: Explicitly flagging the absence of Confucian, Hindu, Islamic, and other frameworks as a research gap gives benchmark designers a concrete roadmap for cultural expansion of values coverage.
- **Pluralism recommendation**: The paper recommends using multiple complementary principles rather than any single framework — directly motivating multi-principle benchmark design that surfaces trade-offs rather than optimizing for a single metric.

## 12. Notable quotes
- "Responsible AI must be able to make or support decisions that consider human values and can be justified by human morals." (p.1)
- "Translating AI principles into practice is challenging. AI principles do not provide guidance for how they can be implemented, and interpretation of their meaning may diverge." (p.3)
- "Conceptions of virtues can change greatly across time and culture. Virtues instantiated in machines today may lead to unfair outcomes in the future as virtues change, or certain virtues may conflict with other virtues." (p.14)
- "There is a wide variety of principles proposed in cultures outside of the history of Western ethics... ethics and culture are inseparable and to understand one you must look at the other." (p.19)

## 13. UNKNOWN / not in extract
- Full list of the 81 papers included in the systematic review (referenced by number but appendix not in extract)
- Details of inclusion/exclusion criteria (referenced as Appendix A.2, not in extract)
- Whether any empirical comparison of operationalization quality across principles was conducted
- The full taxonomy diagram (Figure 1 content partially reconstructed from text)
- Sections 4.2–5 and Section 6 (operationalization architecture details and future directions beyond p.25 of the paper) not captured in the truncated extract
