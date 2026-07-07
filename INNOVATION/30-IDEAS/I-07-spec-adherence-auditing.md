# I-07 — Spec-Adherence Auditing

**Tier 2** · **Gaps: G-01** · **Programs: RP-01** · **Kernel:** Fable 5, 2026-07-07 (FROZEN) · **Body:** Opus draft 2026-07-07

## The idea                        [KERNEL — FROZEN]
A repeatable third-party audit paradigm emerged: parse a spec into behavioral statements, generate targeted probes, measure model↔spec↔self-judgment consistency — or generate value-tradeoff scenarios at scale and read spec defects out of inter-model divergence. Findings: 15–20-point adherence gaps, and divergence concentrating where specs contradict themselves or go ambiguous.

## Key results
- **SpecEval** (Stanford; arXiv:2509.02464, NeurIPS 2025): parse spec → generate probes → measure spec↔output↔self-judgment consistency; **gaps up to 20 points** across 16 models, 6 developers (Front A).
- **Stress-testing model specs** (Anthropic + Thinking Machines; arXiv:2510.07686): **300k value-tradeoff scenarios; 70k+ significant cross-model divergences**; divergence traces to spec contradictions and interpretive ambiguity; high-disagreement scenarios show **5–13× more frequent non-compliance** — "inter-model divergence is a spec-bug detector."
- **Model Spec Evals** (OpenAI, Mar 2026): open harness; compliance **72% (GPT-4o) → ~84–89% (GPT-5.x)**, Thinking > Instant — a tracked, versioned capability.

## Mechanisms & caveats
Divergence-mining is a genuinely new gap-finding tool, and CEI should adopt it for its **own** spec-like artifacts (benchmark rubrics, constitutions of benchmarks). RP-01's differentiators over this paradigm are **ex-ante grading** (grade the spec *before* probing — nobody does this) and **values-content depth**. The three-way consistency frame (spec / output / self-judgment) imports directly into CEI judge audits (RP-04). Caveat to carry forward: adherence numbers are becoming leaderboard-able, so expect gaming — unannounced delivery (I-03) will be needed here too, and soon. Evidence class: SpecEval and stress-testing are SEARCH-CONFIRMED; Model Spec Evals is SEARCH-CONFIRMED (non-arXiv lab release).

## Implications for CEI practice   [KERNEL — FROZEN]
(a) Divergence-mining is a gap-finding tool CEI should adopt for its OWN spec-like artifacts (rubrics, constitutions of benchmarks). (b) RP-01's differentiators over this paradigm: ex-ante grading and values-content depth. (c) The three-way consistency frame (spec/output/self-judgment) imports directly into CEI judge audits (RP-04). (d) Adherence numbers are becoming leaderboard-able — expect gaming; unannounced delivery (I-03) will be needed HERE too, soon.

## Cross-links
- **Gaps:** G-01 (spec-adherence auditing), G-02 (the spec defects divergence reveals).
- **Ideas:** I-06 (the specs being audited), I-08 (deliberative alignment — why adherence moves), I-03 (eval awareness — leaderboard gaming), I-10/RP-04 (three-way frame for judges).
- **Programs:** RP-01 SPECGRADE (ex-ante grading is the scientific step past post-hoc auditing).
- **Field-map front:** A; watch-trigger: a third-party spec-audit org appears (the audit-report niche closes fast).

## OPUS-EXPAND checklist           (LIVING)
- [ ] Deep-read SpecEval 2509.02464; extract the parse→probe→consistency pipeline as the RP-01 O2 harness baseline.
- [ ] Deep-read stress-testing 2510.07686; capture the "inter-model divergence = spec-bug detector" method for RP-01's prospective H2 probe generation.
- [ ] Apply divergence-mining to one CEI benchmark rubric as a self-audit dry run (implication (a)).
- [ ] Specify RP-01's ex-ante grading step (conflict density, coverage, ambiguity) as the differentiator over post-hoc auditing (implication (b)).
- [ ] Port the spec/output/self-judgment three-way consistency check into the RP-04 judge-audit design (implication (c)).

## Sources                         (evidence classes marked)
- SpecEval — arXiv:2509.02464 (NeurIPS 2025) — **SEARCH-CONFIRMED** — G-01 anchor.
- Stress-Testing Model Specifications — arXiv:2510.07686 — **SEARCH-CONFIRMED**.
- Model Spec Evals (OpenAI, Mar 2026) — **SEARCH-CONFIRMED** (non-arXiv lab release).
- Corpus status (absent) — **VERIFIED** (`../02-gap-atlas.md` G-01).
