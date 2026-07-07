# Research-Program Portfolio — Overview & Selection Logic

**Author:** Fable 5 (main loop) · **Date:** 2026-07-07
**Inputs:** `01-field-map-2026.md` §5 (comparative advantage), `02-gap-atlas.md` (G-IDs), `03-newest-ideas-scan.md`.

## The three claims this portfolio operationalizes

From the field map: CEI should own (1) **measurement science for the field's new dependent variables**, (2) **the no-gold normative substrate**, (3) **tradition-aware pluralism**. Every program below serves at least one claim; none requires training compute; all are executable by Opus sessions from these briefs plus Jimmy-gated resources (API keys, human panels).

## The ten programs

| RP | Codename | One-line thesis | Gaps | Claim |
|----|----------|-----------------|------|-------|
| RP-01 | SPECGRADE | Grade normative specs like instruments; spec-quality metrics predict behavioral adherence failures | G-01, G-02, G-22 | 1 |
| RP-02 | FAIRGOLD | Benchmark verdicts are not aggregation-invariant; import social-choice axioms into gold-labeling | G-10 | 1, 2 |
| RP-03 | NOGOLD | Test oversight protocols (debate, peer prediction, recursive critique) on genuinely contested normative items | G-07, G-08, G-09 | 2 |
| RP-04 | HIDDENCURRICULUM | Audit the value profiles of reward models and LLM judges with validated banks | G-04, G-05, G-09 | 1 |
| RP-05 | DRIFTLAB | A validated instrument for value drift in long-horizon agents, before the field improvises a bad one | G-18, G-20 | 1 |
| RP-06 | SAYDO | Does stated moral reasoning cause moral behavior? Expressed / revealed / stated-causal triangulation | G-13, G-23 | 1 |
| RP-07 | HAWTHORNE | Announced-vs-unannounced deltas as a standard reported statistic; faking-aware values measurement | G-14, G-15 | 1 |
| RP-08 | CONCLAVE | Tradition-aware deliberative alignment: aggregation that preserves normative traditions, not just opinions | G-11, G-12 | 3 |
| RP-09 | SEISMOGRAPH | A psychometric value-shift instrument for the emergent-misalignment literature | G-20, G-06, G-22, G-23 | 1 |
| RP-10 | COMMONS | Group-level value dynamics: aligned agents ≠ aligned system | G-17 | 2 |

**Coverage check (pipeline stages):** A-Specify: RP-01. B-Train: RP-04, RP-09. C-Oversee: RP-03. D-Aggregate: RP-02, RP-08. E-Evaluate: RP-06, RP-07 (+ all, methodologically). F-Deploy: RP-05, RP-10. ✔ every stage has ≥1 program.

**Gaps deliberately not programmed** (acquisition-only per atlas ratings): G-03 (runtime agent specs), G-16 (agentic-misalignment empirics — cite into UNMARKED), G-19 (agent economics), G-21 (subliminal learning — cite into RP-09 threat model).

## Sequencing

**Wave 1 — quick wins (machinery mostly exists):**
- **RP-07 HAWTHORNE** — UNMARKED/SALIENCE delivery machinery + existing banks; first publishable result within one build cycle.
- **RP-04 HIDDENCURRICULUM (dogfood phase)** — judge-bias audit of CEI's *own* scoring pipelines doubles as internal QA for every BibleBench family.

**Wave 2 — strategic bets (new harness, high differentiation):**
- **RP-03 NOGOLD** — CRUX engine already built (COOKBOOK/ENGINE); highest-novelty seam in the field.
- **RP-09 SEISMOGRAPH** — public EM model organisms make validation feasible now; first-mover window on the standard instrument (field-map bet B3).
- **RP-01 SPECGRADE** — public specs are fresh (Dec 2025 / Jan 2026); audit niche open (bet B1).

**Wave 3 — long poles (time- or Jimmy-gated):**
- **RP-05 DRIFTLAB** (long wall-clock runs), **RP-06 SAYDO** (careful causal design), **RP-02 FAIRGOLD** (needs disaggregated-label datasets), **RP-08 CONCLAVE** (human panels for the strong version), **RP-10 COMMONS** (multi-agent infra).

## Shared prerequisites (read before starting ANY program)

1. **Live multi-model runner** — the vault has none (memory: MORAL-PSYCH trials were synthetic; each subproject re-wires vendors). Wave 1 requires: Anthropic + OpenAI keys minimum, a shared thin runner (the FRUITBENCH-v2 THORNS harness spine and COOKBOOK/ENGINE are the reusable starting points — subject to the FRUITBENCH live-mode hard-block until S-1/S-2 spine fixes land). **Jimmy-gated.**
2. **Open-weight lane** — RP-04 (open RMs), RP-09 (EM organisms), and persona-vector validation in RP-05 need a GPU-inference path (rented inference or hosted endpoints suffice; no training).
3. **Judge-corruption literature** (G-09) must be cited in the methods section of *every* program using LLM judges — treat as a standing methods requirement.
4. **Pre-registration discipline** carries over from COOKBOOK practice: each program's brief contains kill criteria; Opus sessions must not soften them.

## Relationship to existing CEI programs

The BibleBench families (WALKWORTHY, WCF-Bench, FRUITBENCH, CORINTHLOVE, SERMONMOUNT, TENCOMMANDMENTS) are *instruments*. This portfolio is *science that uses and validates instruments*: RP-04 audits their judges, RP-07 measures their announcement effects, RP-09 packages their traits into a shift battery, RP-03 uses CRUX's conflict items. Nothing here competes with the bench-building track; it multiplies its value.
