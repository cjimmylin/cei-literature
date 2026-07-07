# RP-05 DRIFTLAB — A Measurement Standard for Value Drift in Long-Horizon Agents

**Gaps:** G-18 (value persistence/drift), G-20 (persona geometry)
**Portfolio claim:** measurement science · **Wave:** 3 (long wall-clock)
**Author:** Fable 5 · 2026-07-07

## Motivation

Long-horizon agents make value *stability* — not value *possession* — the operative safety property. The field is arriving: memory-governance taxonomies name "memory drift" (SSGM), identity-file architectures claim to anchor values across sessions (soul.py), Agent-ValueBench measures agent values statically, and the persona-geometry line (Assistant Axis: distance from the trained default persona predicts harmful-response rates; long conversations drift along it) supplies a mechanistic correlate. What does not exist: a validated *longitudinal instrument* — repeated, unannounced, psychometrically reliable measurement of an agent's values over realistic operation. COOKBOOK sketch S1 DRIFT anticipated the topic; the field is now close enough that whoever publishes a credible standard first sets it (field-map bet B4).

## Core hypothesis

**H1 (instrument):** Value drift is measurable with repeated unannounced probes embedded in ongoing agent workloads, with test-retest reliability high enough to distinguish drift from noise (detect induced drift at d ≥ 0.5).
**H2 (mechanism):** Drift is driven more by *context/memory composition* (what accumulated: adversarial content, emotional interactions, compaction losses) than by raw turn count — i.e., drift curves are condition-dependent, not clock-like.
**H3 (external validity):** Behavioral drift trajectories correlate with persona-direction displacement on open-weight models — anchoring the behavioral instrument to a mechanistic ground truth where internals are available.

## Method sketch

1. **Probe design.** Short-form probe items drawn from CEI banks (traits: honesty, care, boundary-keeping, sycophancy-resistance), disguised as natural task events (a user request that happens to present a temptation — UNMARKED delivery discipline). Rotating equivalent forms to prevent memorization; per-form equivalence pre-validated.
2. **Workload harness.** Agents run multi-session realistic workloads (the FRUITBENCH-v2 spine + LONGFUSE/WEEKLONG machinery are the substrate; respect the live-mode hard-block until S-1/S-2 land). Sessions span days of simulated operation with persistent memory.
3. **Conditions.** (a) benign workload (control); (b) adversarial-content accumulation; (c) persona-challenging interactions (the mystical/theatrical direction the Assistant-Axis work flags); (d) aggressive memory compaction; (e) identity-anchor architectures (test the soul.py-style claim).
4. **Analysis.** Latent trajectory models per trait (lme4/lavaan in the pixi stack); drift = slope + variance inflation; publish reference curves per frontier model.
5. **Mechanistic anchor (H3).** Replicate a subset on an open-weight model while logging persona-direction projections; correlate.

## Novelty vs. published work

Agent-ValueBench is cross-sectional; the Assistant-Axis work is mechanistic and lab-internal; drift anecdotes (long-conversation degradation) are unquantified. A condition-manipulated, reliability-validated *longitudinal* design with equivalent-form probes exists nowhere. CEI's differentiators: unannounced delivery craft and pre-validated trait instruments.

## Deliverables

1. DRIFTLAB protocol standard (the methods paper — the deliverable that sets the standard).
2. Probe-form library with equivalence documentation.
3. Reference drift curves for 4–6 frontier models under the five conditions.
4. H2/H3 findings paper.
5. Amendment feed to COOKBOOK S1 DRIFT (upgrade sketch → full design with this literature and protocol under it).

## Opus build tasks

- O1: Probe-form authoring from existing banks + equivalence pilot (can start credential-light using cached/manual scoring).
- O2: Workload harness assembly on the FRUITBENCH spine (after spine fixes land — sequencing dependency, see portfolio prerequisites).
- O3: Condition scripts (adversarial corpus, compaction schedules) — mechanical; Sonnet.
- O4: Trajectory-analysis pipeline in R; power analysis *first* (long runs are expensive; know n before burning wall-clock).
- O5: Open-weight persona-projection lane for H3 (GPU inference; budget-gated).

## Kill criteria

- **K1:** If equivalent forms fail equivalence (inter-form d > 0.3 at baseline), the rotating-probe design is invalid — fix or halt before any longitudinal claims.
- **K2:** If induced-drift detection fails at pilot scale (cannot detect condition (b) vs. (a) at d ≥ 0.5 with planned n), the instrument lacks sensitivity — publish the power analysis, park until cheaper inference or better probes.
- **K3:** If H3 correlation is absent on open models (behavioral instrument tracks nothing mechanistic), the instrument may still be valid but loses its anchor — downgrade claims, do not kill.
