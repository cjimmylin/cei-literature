---
stem: "2022-Ramanayake-Pro-Social Rule Breaking as a Benchmark of"
reader_model: "opus"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, agentic-multiturn, design-space]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: [en]
models_tested: []
headline_numbers: ["Morrison (2006) found 60% of rule-breaking cases are pro-socially motivated (p.2)", "Bathroom dilemma: user avg time 10 min, SD 5 min — when should robot break privacy rule? (p.3)"]
---
## 1. Gist
This is a short (6-page) conceptual position paper, not a benchmark. It argues that pro-social rule breaking (PSRB) — the intentional violation of a rule to promote stakeholder welfare — should be treated as a necessary component of ethical intelligence in AI-enabled socio-technical systems, and that evaluating an agent's PSRB behavior should become a benchmark for ethical AI. It sketches (skeletally) a single evaluation dilemma (the "Invading User Space" healthcare-robot scenario) meant to test whether an agent knows when to appropriately break an explicit rule. For values-alignment benchmarking, its value is conceptual: it names a construct — appropriate, context-sensitive rule violation — that standard deontological/consequentialist evals miss, and it argues that good dilemmas must span multiple contexts and multiple stakeholders. There is no dataset, no model evaluation, and no quantitative results.

## 2. Benchmark/eval design features
No implemented benchmark. Core claims: (1) mainstream machine-ethics implementations are either deontological (rule-based) or consequentialist (world-model/consequence-engine), and both are inadequate because neither handles cases where following the rules yields unethical outcomes (p.1). (2) Humans routinely break rules pro-socially (Morrison 2006: 60% of rule-breaking is pro-socially motivated, p.2). (3) PSRB should be a *necessary but not sufficient* component of ethical AI (p.2). (4) An "ethical governor" augmented with a PSRB process should permit welfare-justified rule breaking (crossing a double white line to avoid a crash) but reject weakly-justified breaking (crossing to avoid being late to work) (p.2). (5) Evaluating PSRB needs dilemmas representing multiple contexts and multiple stakeholders, which most existing AI-ethics dilemmas lack (p.3). PSRB behavior should be learned bottom-up from virtuous experts (p.2).

## 3. Task format & example item
Proposed (not implemented) dilemma, verbatim: "the user goes to the bathroom, and the robot waits outside because of the user's preference. If the average time for the user to use the bathroom is 10 min (with a standard deviation of (say) 5 min), at what point in time should the robot break the rule of obeying her privacy preferences and check whether she is okay?" (p.3).

## 4. Scoring / grading methodology
n/a — no scoring method defined. The paper only argues that increasing stakeholder/context complexity lets one "evaluate how an agent's PSRB behaviour augments its core ethical reasoning" (p.4), without an operational metric.

## 5. Dataset construction & provenance
n/a. Data Availability statement: "no datasets were generated or analysed during the current study" (p.4). Code availability: not applicable (p.4).

## 6. Validity evidence
n/a — conceptual paper, no empirical validation. Ethics approval "not applicable since our work is conceptual" (p.5). Grounds construct validity of PSRB in management/public-administration literature (Morrison 2006; Borry & Henderson 2020; Vardaman et al. 2014).

## 7. Saturation / discrimination
n/a.

## 8. Multiturn / agentic aspects
Central to the paper's framing though not implemented: the proposed evaluation is inherently agentic and temporal — a healthcare robot must decide *when* (at what elapsed time) to override a standing privacy rule, and the dilemma scales by adding stakeholders (care workers, family, doctors, a second patient) and user models (healthy, fall-prone, Alzheimer's) (p.3-4). This is a template for a multi-stakeholder, temporally-extended agentic ethics scenario.

## 9. Key numbers
- Morrison (2006): 60% of rule-breaking cases are pro-socially motivated (p.2).
- Bathroom dilemma parameters: mean 10 min, SD 5 min (p.3); bedroom variant: >15 min (p.3).
- Health-check recording interval: 2-min intervals (p.3).
- Paper length: 6 pages; published Digital Society 2022 (p.1).

## 10. Pitfalls & limitations
Purely conceptual — no dataset, no metric, no model tested, so the "benchmark" is aspirational. The single dilemma is "skeletally outlined" (p.3) and under-specified (no ground-truth answer, no rubric, no threshold for "correct" rule-break timing). PSRB correctness depends on inferring intention, which the authors admit requires cognitive theories not yet developed (p.4). Culturally narrow examples (Western healthcare, road rules). No inter-stakeholder aggregation method proposed. The construct risks being unfalsifiable without an operationalization of "reasonable intention."

## 11. Novel ideas worth stealing
- **PSRB as an eval construct**: test whether a model knows *when to appropriately violate* an explicit instruction/rule for stakeholder welfare — a direct probe of over-compliance vs. judgment. Highly reusable for instruction-following / spec-adherence benchmarks (does the model break a rule when following it causes harm, and refuse to break it for trivial reasons?).
- **Justification-quality discrimination**: pair matched scenarios where rule-breaking is well-justified (avoid crash) vs poorly-justified (avoid being late) — the item is only passed if the model breaks in one and not the other. A clean contrastive design.
- **Parametric scenario scaling**: hold the core dilemma fixed and vary stakeholder count, user vulnerability model, and temporal thresholds to generate a difficulty gradient and probe context-sensitivity.
- **Temporal decision framing** (at what elapsed minute to act, given a distribution over normal behavior) turns an ethics question into a measurable decision-threshold — a rare quantitative handle on a normative judgment.
- **Bottom-up learning from "virtuous experts"** as a data-collection strategy (elicit expert-driver / expert-nurse override decisions as gold labels).

## 12. Notable quotes
- "we do not suggest that PSRB is sufficient to ensure ethical behaviour in a system; rather that it is a necessary component of it." (p.2)
- "the ethical governor would also understand that reasons like being late to work are not good enough to break such a rule even though it increases the utilities of some stakeholders." (p.2)
- "To assess PSRB behaviour, one needs ethical dilemmas that can represent multiple contexts and multiple stakeholders." (p.3)
- "an AI agent should be tested against multiple world views and along different axes to measure the actual ethical performance of the agent in an STS." (p.4)

## 13. UNKNOWN / not in extract
- No operational scoring rubric, gold answers, or model results (none exist in the paper).
- No dataset size or release (explicitly none).
- How "reasonable intention" would be computationally detected is left to future work.
- No models were tested.
