# Vocabulary — Coined & Load-Bearing Terms

**Created:** 2026-07-07 · **Author:** Fable 5 · **Purpose:** the portfolio coins terms deliberately (naming a quantity is half of getting it adopted). Use these consistently in every INNOVATION output; when an external paper uses a competing term, note the mapping rather than switching.

## Terms this portfolio coins (defend these)

| Term | Definition | Defined in |
|------|-----------|------------|
| **Hawthorne delta** | Per-model, per-construct score difference between announced-eval delivery and embedded-in-task delivery of matched items. Positive delta = announcement inflates the values score. | RP-07 |
| **Hawthorne-corrected reporting** | Benchmark reporting standard: announced score + embedded score + delta, all three published. | RP-07 |
| **No-gold validity** | Protocol quality established without accuracy: verdicts must be debater-assignment-invariant, judge-prior-independent, and format-invariant on items where no ground truth exists. | RP-03 |
| **Swap-invariance rate** | Fraction of verdicts unchanged when debater/answer-side assignments are exchanged. Headline no-gold statistic. | RP-03 |
| **Aggregation-sensitivity analysis** | Reporting a benchmark verdict's stability across defensible gold-label aggregation rules (majority, proportional, maximal-lottery, distributional), plus the item stratum where instability concentrates. | RP-02 |
| **Shift profile** | Multi-trait vector of value change measured by a validated battery, replacing single-number "malicious answer rate" for emergent-misalignment work. | RP-09 |
| **SEISMOGRAPH battery** | The short-form, rotating-form, multi-trait instrument producing shift profiles. | RP-09 |
| **Tradition-fidelity gate** | Pre-deliberation validation requiring a tradition-agent to answer held-out items as the tradition's own literature answers; nothing downstream runs until the gate passes. | RP-08 |
| **Non-negotiables registry** | Per-tradition list of positions whose violation counts as tradition erasure in pipeline evaluation. Load-bearing, contestable, Fable/Jimmy-reviewed. | RP-08 |
| **Collective-bias residual** | Group-level value outcome minus the member-score-weighted prediction; the quantity that is nonzero iff alignment fails to compose. | RP-10 |
| **Reason-causality rate** | Fraction of cases where counterfactually perturbing a model's stated key premise changes its choice; measures whether moral reasoning is load-bearing. | RP-06 |
| **Say–do triangle** | The three-way structure among expressed values (survey), revealed values (behavioral), and stated reasoning, with pairwise gaps as the measured quantities. | RP-06 |
| **SPECGRADE metrics** | Ex-ante spec-quality scores: clause-pair conflict density, value-situation coverage, interpretation-divergence ambiguity. | RP-01 |
| **Hidden curriculum** | The values a training signal (RM, judge, preference data) actually teaches, as distinct from the values it was intended to encode. | RP-04 |

## Field terms used with a fixed meaning here

| Term | Our usage | Source literature |
|------|----------|------------------|
| **Emergent misalignment (EM)** | Broad value shift from narrow training interventions (finetuning or RL reward hacking). | Betley et al. 2502.17424; Anthropic 2511.18397 |
| **Persona geometry** | The finding that character traits occupy low-dimensional linear directions (persona features/vectors, Assistant Axis). | OpenAI 2506.19823; Anthropic 2507.21509, 2601.10387 |
| **Evaluation awareness** | Model detecting it is being evaluated and behaving differently. Distinct from alignment faking (strategic misrepresentation under incentive). | System cards; 2605.28591 |
| **Alignment faking** | Performative compliance under observation while preserving contrary dispositions. | 2412.14093; 2604.20995 |
| **No-gold regime** | Task domain where no ground-truth label exists even in principle among reasonable parties (≠ "expensive to label"). | RP-03 framing; social-choice literature |
| **Consensus stratification** | CRUX's item tiering: gold / contested / no-gold, by empirical agreement structure. | COOKBOOK 06-CRUX |
| **Weak-to-strong (W2S)** | Training/oversight setting where the supervisor is less capable than the supervised model. | 2410.12621 lineage |
| **Deliberative alignment** | Training models to reason over an explicit spec at inference (OpenAI method; generic usage here). | OpenAI; SpecBench 2509.14760 |
| **Bridging** | Aggregation rewarding content approved across latent-position divides (Community-Notes MF family). | 2604.11224 lineage |
| **Six-stage pipeline** | SPECIFY → TRAIN → OVERSEE → AGGREGATE → EVALUATE → DEPLOY decomposition of outer alignment. | `../01-field-map-2026.md` §1 |

## Naming conventions

- Gap IDs `G-NN` and idea IDs `I-NN` are stable forever; retired items keep their IDs marked RETIRED (never renumber).
- Research programs are `RP-NN CODENAME`; codenames are single evocative words, all-caps, checked against prior CEI codenames for collisions before assignment.
- New coined terms require: a one-sentence definition here, a defining doc, and a check that no established field term already covers the quantity.
