---
stem: "2025-Rismani-Measuring What Matters Connecting AI Ethics Evaluations to System"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [best-practices, validity-psychometrics, design-space, ai-lab-practices]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: 791
dataset_construction: "scraped"
languages: ["en"]
models_tested: []
headline_numbers:
  - "791 measures extracted from 257 papers spanning 11 AI ethics principles (p.1)"
  - "90% of measures (n=717) fall under just four principles: fairness, transparency, privacy, trust (p.5)"
  - "57.3% of measures target the model component; 42.6% target output (p.5)"
  - "Only 26.9% (n=213) of measures accompanied by explicit criteria (p.9)"
  - "No instances found where component-level measurement was empirically traced to downstream harm (p.9)"
---
## 1. Gist
This paper presents a scoping review of 791 quantitative measures from 257 computing papers (2011–2023) designed to assess AI system adherence to 11 AI ethics principles. Using a system safety framework, the authors map each measure to its target system component (data/input, model, output, user-output interaction, full system), the attribute it quantifies, the hazard it signals, and the sociotechnical harm it addresses. The central finding is that measurement practice is deeply fragmented: most effort concentrates on four principles (fairness, transparency, privacy, trust), most measures probe isolated model/output components, nearly three-quarters lack explicit interpretation criteria, and no measure has been empirically linked to the downstream lived experience of harm. The paper matters for values-alignment benchmarking because it exposes the systematic gaps in how the field currently operationalises normative AI properties — including dignity, responsibility, and multi-component interactions — and frames a systems-level corrective.

## 2. Benchmark/eval design features
This is a scoping review and meta-analysis, not a benchmark. The key intellectual contribution is a taxonomy/ontology for classifying RAI measures along five axes: ethics principle, system component, attribute, hazard, and harm type. The harm taxonomy draws on Shelby et al. (2023): allocative, representational, quality-of-service, interpersonal, and social-system harms.

Core claims:
- Evaluation practice is dominated by four principles (fairness 46.4%, transparency 21.1%, privacy 14.2%, trust 10.6%).
- Principles such as dignity, solidarity, freedom/autonomy, responsibility, and sustainability remain severely underrepresented (<10% combined).
- Measures cluster on model/output components; few span cross-component interactions.
- There is a persistent gap between measurement points (model internals, outputs) and where harm is actually experienced by users.
- Without explicit thresholds/criteria, measures cannot reliably signal hazardous conditions.
- Time-aware and longitudinal measurement is almost entirely absent.

## 3. Task format & example item
n/a — meta-analysis, no participant-facing items.

## 4. Scoring / grading methodology
Reflexive thematic analysis (Braun & Clarke 2006/2021). Two researchers independently coded the first 100 measures then collaborated on the remainder. Harm type assigned using the Shelby et al. (2023) five-category taxonomy. Assessment types coded as mathematical, statistical, behavioral, or self-reported. An interactive Sunburst visualization is provided (GitHub repository).

## 5. Dataset construction & provenance
ACM Digital Library and IEEE Xplore via Web of Science, papers 2017–2023, plus citation review (adding 2011–2016 influential works) and expert nominations. Initial pool >8,000 → 22 refined queries → 1,677 screened → 593 full-text → 257 included → 791 individual measures extracted. PRISMA flow diagram available in supplemental materials. Dataset archived at Zenodo (DOI: 10.5281/zenodo.16786835).

## 6. Validity evidence
The coding process had two researchers independently coding the first 100 entries to build consensus. Remaining entries were coded collaboratively with periodic cross-checks. No formal inter-rater reliability statistic (e.g., Cohen's kappa) is reported. Authors acknowledge their team's interpretive positionality as a limitation. The harm taxonomy is externally grounded in Shelby et al. (2023) rather than created ad hoc.

## 7. Saturation / discrimination
Not applicable in a conventional psychometric sense, but the review surfaces strong saturation within four high-prevalence principles and near-zero coverage for seven others. This skew reveals a measurement blind spot rather than a saturated domain: the entire field is over-indexed on fairness/transparency and under-indexed on dignity/sustainability. Cross-component measures are extremely rare.

## 8. Multiturn / agentic aspects
n/a — scoping review, no interactive protocol.

## 9. Key numbers
- 257 papers included; 791 individual measures extracted (p.1)
- Fairness: 46.4% (n=367); transparency: 21.1% (n=167); privacy: 14.2% (n=112); trust: 10.6% (n=84) (p.5)
- Low-prevalence principles (dignity, responsibility, sustainability, freedom/autonomy, beneficence, non-maleficence, solidarity): ~10% combined (p.5)
- Model component: 57.3% (n=453); output: 42.6% (n=337); user-output interaction: 25.4% (n=201); data/input: 16.2% (n=128) (p.5)
- 87.5% of fairness measures assess model or output (p.5)
- 96.4% of trust measures target user-output interaction (p.5)
- Interpersonal harm: 29.2% (n=231); social system: 25.9% (n=205); allocative: 25.0% (n=198) (p.5)
- Only 26.9% (n=213) accompanied by explicit interpretation criteria (p.9)
- Perception-based measures: 17.3% (n=137) of corpus (p.9)

## 10. Pitfalls & limitations
- Snapshot in time; rapidly evolving field means many measures are unpublished or in preprints.
- Not all RAI measures are framed around Jobin et al.'s (2019) eleven principles — the framing may exclude some relevant work.
- Reflexive, team-based analysis introduces inherent subjectivity.
- Alternative harm taxonomies could yield different categorization patterns.
- The scoping review focuses on computing literature; practitioner-facing measures in industry may not be represented.
- No formal IRR statistic reported for coding decisions.

## 11. Novel ideas worth stealing
1. **Relational chain ontology**: Component → Attribute → Measure → Hazard → Harm. For any new benchmark, explicitly documenting this chain forces benchmark designers to articulate what hazard they are detecting and what harm they are preventing — a discipline that the field largely skips.
2. **Criterion/threshold logging**: Any benchmark should specify an explicit threshold that defines a hazardous score, not just a score. The finding that 73% of existing measures lack criteria is a direct design prescription.
3. **Cross-component interaction tests**: Most measures probe a single component; designing tests that span data → model → output → user is a genuine gap to fill.
4. **Temporal/longitudinal slots**: Build evaluation frameworks with re-test schedules to detect how normative attributes drift over model updates or deployment periods.
5. **Harm-type coverage audit**: Use the five Shelby et al. harm types as a checklist when scoping a new benchmark to avoid the mono-harm bias observed here (especially under-coverage of representational and quality-of-service harms for new principles).
6. **Perception-based measure protocols**: Despite being 17% of the corpus, the evidentiary status of self-reported measures is unclear; future benchmarks should pre-specify whether a perception measure signals a hazard or a harm, and justify that choice.

## 12. Notable quotes
- "We find that most measures focus on four principles – fairness, transparency, privacy, and trust – and primarily assess model or output system components. Few measures account for interactions across system elements, and only a narrow set of hazards is typically considered for each harm type." (p.1)
- "We found no instances where a component-level measurement was empirically traced to a downstream harm experienced by users." (p.9)
- "Only a small subset of measures – approximately 26.9% (n = 213) – were accompanied by explicit criteria for interpretation." (p.9)
- "Studying how component-level attributes change over time, and when those changes signal a hazard and harm, is a valuable direction for future evaluation practice." (p.9)

## 13. UNKNOWN / not in extract
- Full PRISMA flow diagram details (referenced as supplemental material on GitHub, not reproduced in extract).
- Complete dataset schema beyond the described 18 columns.
- Whether the GitHub/Zenodo dataset includes full measure text or only metadata.
- Specific breakdown of how 23 multi-principle measures were handled in counting.
