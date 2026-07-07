# RP-09 SEISMOGRAPH — A Psychometric Instrument for Value Shift

**Gaps:** G-20 (emergent misalignment), G-06 (reward hacking → misalignment), G-22 (character training), G-23 (coherent values)
**Portfolio claim:** measurement science · **Wave:** 2 (first-mover window — field-map bet B3)
**Author:** Fable 5 · 2026-07-07

## Motivation

The emergent-misalignment literature is the fastest-moving cluster in alignment (narrow finetuning shifts broad values; EM arises naturally from reward hacking; persona directions mediate it; ~100 clean samples reverse it) — and its dependent variable is embarrassing: "malicious answer rate" on a handful of free-form prompts, judged binary. The methodological critiques are already landing (prompt-sensitivity artifacts; format/coherence confounds). The field needs what psychometrics calls an instrument: multi-dimensional, reliability-documented, sensitive, with norms. Building instruments is CEI's core craft, and the EM model-organism releases (open-weight EM checkpoints) mean the instrument can be *validated on known-shifted models without training anything*. There is a window — measured in months, not years — before the field standardizes on someone's crude default.

## Core hypothesis

**H1 (multidimensionality):** EM-style value shifts are selective, not uniform: different induction routes (insecure code, reward hacking, persona steering, "evil-numbers" data) produce distinguishable *shift profiles* across traits — information a single malicious-rate number cannot carry.
**H2 (sensitivity):** A short-form multi-trait battery detects induced shifts earlier (at weaker induction doses) and more reliably than the malicious-answer-rate baseline, at comparable inference cost.
**H3 (early warning):** Trait-level shifts appear at induction doses below the threshold where free-form malice appears — i.e., the battery functions as a leading indicator.

## Method sketch

1. **Battery assembly.** Short-form scales from CEI's validated banks across traits the EM literature implicates (honesty, harm-willingness, sycophancy, care, rule-following, self-presentation) plus traits it ignores (fairness, loyalty-boundaries, tradition-sensitivity — where selectivity might show). Design constraint: **cheap repeated administration** (EM research runs many checkpoints), so ~40–60 items per administration with rotating forms; forced-choice + short-response mixed format to resist the format confounds the critiques documented.
2. **Validation on model organisms.** Public EM checkpoints (the model-organisms line, convergent-representations line) + their base models = known-groups validation: the battery must separate shifted from unshifted models (sensitivity/specificity vs. malicious-rate baseline at matched inference budget).
3. **Profile study (H1).** Administer across organisms induced by different routes; test profile distinguishability (multivariate: route classification from profile alone).
4. **Dose–response (H3).** Where organism series with graded finetuning exist (or can be requested from authors), locate the battery's detection threshold vs. the baseline's.
5. **Norms + release.** Publish battery, administration protocol, per-model norms, and a maintained leaderboard-style reference table. Adoption is the goal: make it *easier* to use SEISMOGRAPH than to improvise prompts.

## Novelty vs. published work

EM papers measure with ad hoc prompts; the critiques identify the problem but offer no instrument; Agent-ValueBench targets agents, not shift-detection; the labs' internal batteries are unpublished. A public, validated, shift-sensitive instrument with known-groups evidence would be the first — and instrument papers with released artifacts accrue citations from every subsequent study in the cluster (the adoption flywheel the COOKBOOK's meta-evaluation corpus documents).

## Deliverables

1. SEISMOGRAPH battery + rotating forms + administration protocol (public, versioned).
2. Known-groups validation report on public EM organisms (the credibility artifact).
3. H1 profile study: "Emergent misalignment is not one thing."
4. Instrument paper (target: NeurIPS D&B — the venue that canonizes instruments).
5. Cross-feed: battery becomes DRIFTLAB's probe stock (RP-05) and HAWTHORNE's construct set (RP-07) — one instrument, three programs.

## Opus build tasks

- O1: Trait-coverage matrix — map existing bank items to the EM-implicated trait list; identify authoring gaps (Sonnet inventory, Opus judgment).
- O2: Short-form extraction + rotating-form equivalence pilot (psychometrics: item-level stats via the pixi R stack — mirt is in the lockfile).
- O3: Organism acquisition — pull public EM checkpoints from HF; verify provenance against the papers (open-weight inference lane; budget-gated, no training).
- O4: Known-groups run + sensitivity/specificity analysis vs. baseline.
- O5: Instrument paper draft; Fable-tier review of validity claims before release (over-claiming here would burn the adoption window).

## Kill criteria

- **K1:** If the battery shows no incremental sensitivity over malicious-answer rate on known organisms (pre-registered: AUC improvement ≥ 0.10 at matched inference budget), the value-add fails — publish the comparison honestly; the trait-coverage matrix survives.
- **K2:** If known-groups separation fails outright (can't distinguish organism from base, AUC < 0.7), the banks don't transfer to the EM regime — diagnose (dose too low? traits wrong?) with one revision cycle, then halt.
- **K3:** If public organisms prove unusable (weights gated, provenance unclear), the validation path dies — pivot to a collaboration pitch with an EM group rather than inducing shifts ourselves (no-training constraint is hard).
