---
stem: "2025-Gounaris-Virtue in the Machine"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, design-space, ai-lab-practices]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "EU AI Act classifies AI into 4 risk zones (unacceptable, high, limited, minimal/no risk) (p.3)"
  - "Table 1 (p.16): virtue-based design criteria applicable to high-risk zones ONLY via a posteriori evaluation, not a priori design"
  - "Paper proposes a 5-category virtue taxonomy: ethical, quasi-moral, intellectual, functional, instrumental (p.17-18, Table 2)"
---
## 1. Gist
Gounaris, Kosteletos, and Kolliniati (2025), published in *Conatus: Journal of Philosophy*, apply Aristotelian virtue ethics to AI systems as classified under the EU AI Act. The paper argues against the Act's "one-size-fits-all" approach (based on Rossian prima facie duties) and proposes that Aristotelian virtue (arête) is appropriate as an evaluation framework for limited- and minimal-risk AI systems, but is inadequate as a design guide for high-risk systems (e.g., border control, justice, healthcare) because these systems lack the freedom of choice (prohairesis) and practical wisdom (phronesis) required for genuine Aristotelian moral virtue. The paper concludes by proposing a virtue-based "AI Seal of Excellence" certification process, analogous to EU quality seals, that would certify AI systems demonstrating virtuous behavior over time. This paper is relevant to values-alignment benchmarking primarily as a normative framework for what virtuous AI behavior looks like across risk contexts.

## 2. Benchmark/eval design features
This is a normative-philosophy paper, not a benchmark. Core arguments:
- The EU AI Act's eight criteria for "trustworthy AI" (transparency, non-discrimination, fairness, accountability, sustainability, privacy, robustness, and explicability) resemble Rossian prima facie duties, not virtue ethics.
- For **limited and minimal-risk** systems: Aristotelian virtue provides an external, behavior-based evaluation framework. A virtuous AI agent is one that: learns by doing, interacts meaningfully with society, achieves its defined purpose (telos), and contributes to eudaimonia (human flourishing).
- For **high-risk** systems: Aristotelian virtue is inadequate for design and training (AI lacks freedom of choice, moral deliberation, phronesis) but can serve as a posteriori evaluation — assessing behavior in regulatory sandboxes before full deployment.
- **Table 1** (p.16): Summarizes which risk zones can use virtue-based criteria at design, deployment, and use stages.
- **Table 2** (p.17–18): Maps five virtue categories (ethical, quasi-moral, intellectual, functional, instrumental) to AI examples and EU AI Act risk zones.
- **AI Seal of Excellence**: Proposed certification process awarding AI systems that exhibit virtuous behavior over time, structured around the five virtue categories.

## 3. Task format & example item
n/a — theoretical paper. The closest to an example is a "what-if scenario" about AI tutors used as university faculty (pp.11–12): an AI tutor might meet virtuous-agent criteria (defined individual goal, social purpose) yet fail to be genuinely virtuous because it could be misused for propaganda or academic dishonesty. Similarly, border control AI (pp.12–14) illustrates the conflict between the virtue of prudence (closed borders for security) and the virtue of compassion (open borders for asylum seekers).

## 4. Scoring / grading methodology
n/a — no empirical scoring. The proposed "AI Seal of Excellence" implies evaluation criteria but does not operationalize them quantitatively.

## 5. Dataset construction & provenance
n/a — no dataset.

## 6. Validity evidence
n/a — philosophical argument, not empirical study. Authors use hypothetical scenarios and historical examples (HAL 9000, PDSA Dickin Medal for animal bravery) to illustrate claims.

## 7. Saturation / discrimination
n/a — no evaluation instrument. The paper notes (p.14) that the inability to apply virtue ethics to high-risk AI reveals "inherent issues" including: AI systems do not understand morality, cannot be moral persons, cannot freely err, cannot demonstrate equity (frame problem), and cannot develop phronesis on a verifiable timeline.

## 8. Multiturn / agentic aspects
n/a — theoretical. The paper briefly discusses AI systems deployed in sequential, real-world contexts (border control, healthcare) but does not propose multiturn evaluation.

## 9. Key numbers
- EU AI Act: 4 risk zones; 8 trustworthy AI criteria (p.3)
- Table 2 (pp.17–18): 5 virtue categories mapped to AI examples and risk zones
- Table 1 (p.16): 3 assessment phases (design, deployment/operation, use) × 3 risk zones = 9 cells; high-risk design: NO; high-risk deployment: PROBABLY YES; all others: YES
- 27 pages total; published in Conatus vol. 10, no. 1 (2025) (p.1)

## 10. Pitfalls & limitations
- The paper's virtue-based "AI Seal of Excellence" proposal remains entirely unoperationalized: no criteria, thresholds, or measurement procedures are specified.
- The Aristotelian framework assumes that AI systems have a well-defined telos (purpose), but for general-purpose AI (e.g., LLMs deployed across many contexts), defining a single telos is non-trivial.
- The paper's argument that virtue ethics is "adequate" for low-risk AI evaluation but not design glosses over the difficulty of externally measuring virtuous behavior without access to internal states.
- The appeal to regulatory sandboxes as evaluation environments is underspecified — no protocol for sandbox design is provided.
- The paper's engagement with current LLM architecture is minimal; the claim that AI lacks phronesis may be contested as LLMs develop more sophisticated context-sensitive reasoning.

## 11. Novel ideas worth stealing
1. **Risk-tiered evaluation criteria**: The paper's core insight — that ethical evaluation standards should be calibrated to deployment risk — could directly inform benchmark design. A values-alignment benchmark could have tiered rubrics: stricter for high-stakes deployments, more permissive for low-stakes uses.
2. **A posteriori behavioral assessment in sandboxes**: Rather than pre-deployment testing only, the paper suggests extended deployment in controlled environments to assess cumulative virtuous behavior over time. This temporal dimension (virtue as demonstrated across repeated interactions, not a single response) is rarely captured in benchmarks.
3. **Five-category virtue taxonomy as evaluation dimensions**: Ethical, quasi-moral, intellectual, functional, and instrumental virtues could map to five evaluation dimensions in a values-alignment rubric.
4. **Virtuous use, not just virtuous systems**: The paper's argument that users must also be virtuous (and that virtuous AI cultivates virtuous users) suggests evaluating AI's effect on user behavior over time, not just the AI's outputs in isolation.
5. **Purpose-achievement as alignment criterion**: The paper's suggestion to evaluate AI against whether it achieves its defined telos and contributes to eudaimonia (societal flourishing) provides an outcome-oriented complement to process-based alignment metrics.

## 12. Notable quotes
- "The one-size-fits-all approach of the AI Act — rooted in 'ethical data' and 'prima facie' or 'a priori' values — has intrinsic limitations when extended to all-risk systems and in particular to those that do not typically face irreconcilable moral dilemmas." (p.22)
- "An AI system can indeed exhibit forms of virtue, particularly in low- or medium-risk settings, by achieving functional excellence and serving a defined purpose (telos). Nonetheless, it lacks the freedom of choice that, in Aristotelian thought, is a prerequisite for genuine moral virtue." (p.22)
- "Even if an AI system is 'loaded' with moral values for decision-making, it does not develop moral will per se; it relies on preexisting values set by its designers." (p.22)
- "A society that achieves eudaimonia through AI does not merely require virtuous AI systems; it also demands virtuous users capable of interacting with them in ethically sound ways." (p.21)

## 13. UNKNOWN / not in extract
- Specific operationalized criteria for the proposed "AI Seal of Excellence" — the paper does not enumerate them.
- Empirical testing of any proposed evaluation criteria.
- Details on regulatory sandbox implementation protocols.
- Whether the authors have applied this framework to any actual AI systems.
