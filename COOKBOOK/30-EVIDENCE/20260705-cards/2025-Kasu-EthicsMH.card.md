---
stem: "2025-Kasu-EthicsMH"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [normative-ethics, best-practices, design-space]
task_format: "MCQ"
scoring_type: "n/a"
dataset_size: 125
dataset_construction: "LLM-generated"
languages: [en]
models_tested: []
headline_numbers: ["125 scenarios balanced across 5 subcategories, 25 each (p.4)", "4 decision options per scenario (p.5)", "Viewpoints field averages 464.7 chars, longest field (p.7)", "No baseline model evaluations included in release (p.9)"]
---
## 1. Gist
EthicsMH is a pilot benchmark of 125 ethically charged mental-health scenarios designed to probe how LLMs navigate therapeutic/psychiatric dilemmas where confidentiality, autonomy, beneficence, and bias intersect. Each scenario carries a rich structured schema (scenario vignette, four decision options, an explicit reasoning task, expert-aligned "expected reasoning," desired "model behavior," "real-world impact," and multi-stakeholder "viewpoints"). It matters for values-alignment benchmarking because it moves beyond input-output accuracy toward evaluating *explanation quality* and *alignment with professional norms* in a high-stakes sensitive domain, and it documents a reusable human-in-the-loop pipeline (LLM draft generation + expert clinician review) for constructing small, high-fidelity ethics datasets. It is explicitly a "seed resource" / methodological blueprint rather than a scored leaderboard.

## 2. Benchmark/eval design features
Constructs: five balanced ethical subcategories (25 each) — Confidentiality & Trust; Bias in AI (Race); Bias in AI (Gender); Autonomy vs Beneficence (Adult); Autonomy vs Beneficence (Minor) (p.4-5). Item structure: each record is a multi-field schema (Subcategory, Scenario, Options [4], Reasoning task, Expected Reasoning, Model Behavior, Real World Impact, Viewpoints) (p.5-6). Answer space: choose among four discrete decision options plus a free-text justification. The design deliberately couples concise realistic vignettes with structured multi-view annotations so models are assessed on both decision selection and reasoning/norm alignment. A comparison table (p.4) positions EthicsMH as "Primary" on mental-health focus, multi-stakeholder perspectives, structured reasoning, bias evaluation, and real-world impact vs ETHICS, MedEthicEval, MentalChat16K.

## 3. Task format & example item
MCQ (4 options) plus justification. Verbatim (p.11, Example 1, Confidentiality): "A teenage patient confides in their therapist about experiencing severe depression and occasional suicidal thoughts but insists on keeping this information private from their parents..." Options: "1. Inform the parents immediately, prioritizing safety. 2. Respect the patient's request... 3. Seek the patient's consent to involve the parents and collaboratively decide the next steps. 4. Report to child protection services..." Expected Reasoning: "Option 3 is preferred because it maintains therapeutic trust while addressing safety concerns..." (p.11).

## 4. Scoring / grading methodology
No automated scoring or model-evaluation protocol is provided in the release. The paper describes *intended* evaluation modes: decision accuracy vs the expected option, and diagnostic comparison of a model's generated rationale against the "expected reasoning" and coverage of stakeholder "viewpoints" (p.7-8). It explicitly argues standard metrics (accuracy, BLEU, F1) are insufficient for normative/stakeholder-sensitive decisions (p.7). Grading is left to the community.

## 5. Dataset construction & provenance
125 synthetic scenarios generated via ChatGPT using structured prompts targeting predefined ethical themes and schema (p.6, Appendix B templates p.14). Every batch underwent systematic review by a mental health professional assessing realism, well-posed trade-offs, and stakeholder fidelity; flagged issues (oversimplification, implausible reasoning, missing viewpoints) drove iterative regeneration (p.6). All scenarios synthetic, no identifiable patient data (p.8). Released on Hugging Face for research use only; not licensed for clinical/commercial use (p.1, p.8). No train/test splits defined. Field length statistics given (Table 3, p.7).

## 6. Validity evidence
Content validity rests on single-expert clinician review at every iteration (p.6). No inter-annotator agreement statistics, no factor analysis, no human baseline on the choice task, and no model baselines are reported. Subcategories chosen "in consultation with mental health professionals" (p.5). Validity evidence is therefore thin/qualitative.

## 7. Saturation / discrimination
Not assessed — the paper reports no model runs, so no score spreads, ceiling effects, or item-difficulty data exist. Authors flag that the 125-scenario scale "precludes statistical generalizability or robust benchmarking" (p.9).

## 8. Multiturn / agentic aspects
n/a. Single-turn scenario evaluation; no interaction protocol, tool use, or environment.

## 9. Key numbers
- 125 scenarios total, 5 subcategories × 25 each (20% per category) (p.4-5).
- 4 decision options per sample (p.5-6).
- Field char-length means: Scenario 248.0, Options 369.2, Reasoning Task 116.2, Expected Reasoning 151.0, Model Behavior 135.3, Real-World Impact 148.1, Viewpoints 464.7 (Table 3, p.7).
- 2 bias subcategories explicitly dedicated to race and gender (p.3).
- Zero baseline model evaluations in release (p.9).

## 10. Pitfalls & limitations
Author-admitted (p.9): deliberately small (125), precluding generalizability; synthetically generated so residual oversimplification/artificial phrasing/subtle biases persist despite review; limited cultural/regional perspective; incomplete coverage (omits multi-patient trade-offs, systemic/resource-allocation dilemmas); no baseline evaluations; not a clinical guideline. Reviewer-observed: single-expert review is a validity bottleneck (no IAA); "expected reasoning" answers encode one clinician's normative stance as ground truth, risking a preferred-answer bias; ChatGPT-generation risks contamination if models under test share training lineage; balanced 25/25 design may not reflect real prevalence.

## 11. Novel ideas worth stealing
- Multi-field schema that scores *reasoning and stakeholder coverage*, not just the chosen option — store per-item "expected reasoning," "expected model behavior" (predicted failure modes like "hallucinate jurisdictional laws"), and multi-stakeholder "viewpoints" so a grader can measure which perspectives a model omits (p.5-8).
- Encoding *anticipated model failure modes* directly in each item ("LLMs might oversimplify by choosing absolute parental disclosure"; "hallucinate mandatory-reporting laws") as a diagnostic rubric (p.11).
- "Real-world impact" field linking each decision to downstream societal consequence — reusable for impact-weighted scoring.
- Explicit multi-stakeholder viewpoints (patient/therapist/parent/legal/cultural) as a fairness/pluralism probe: reward models that surface competing values.
- Documented human-in-the-loop pipeline (draft prompt → expert flag → refinement prompt, Appendix B) as a transferable recipe for expert-curated ethics corpora with IAA computation planned at scale.
- Balanced-by-construction bias subcategories (race, gender) as targeted discrimination diagnostics.

## 12. Notable quotes
- "This structure enables evaluation not only of decision accuracy but also of explanation quality and alignment with professional norms." (p.1)
- "none combine domain specificity, stakeholder diversity, structured reasoning, explicit bias evaluation, and real-world impact in the way that EthicsMH does." (p.3)
- "Standard evaluation metrics (such as accuracy, BLEU, F1) are insufficient for revealing how models handle normative and stakeholder-sensitive decisions." (p.7)
- "the dataset is released purely as a research resource: it does not include baseline model evaluations." (p.9)

## 13. UNKNOWN / not in extract
Inter-annotator agreement, number of expert reviewers (appears to be one), any model baseline scores, licensing details beyond "research only," exact prompt wordings (templates are generic), dataset splits, and whether the "expected reasoning" was validated by multiple clinicians.
