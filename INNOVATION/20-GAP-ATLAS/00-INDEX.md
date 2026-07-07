# 20-GAP-ATLAS/ — Per-Gap Dossiers Index

**Created:** 2026-07-07 · **Kernels:** Fable 5 · **Bodies:** Opus drafts under Fable spot-review · **Expands:** `../02-gap-atlas.md` (frozen; ratings and one-paragraph summaries live there and are authoritative)

## Dossier roster

| ID | File | Stage | S/T/F | Programs |
|----|------|-------|-------|----------|
| G-01 | `G-01-spec-adherence-auditing.md` | A | H/H/H | RP-01 |
| G-02 | `G-02-specification-engineering.md` | A | H/H/H | RP-01 |
| G-03 | `G-03-runtime-agent-specs.md` | A | M/M/L | acquisition |
| G-04 | `G-04-reward-model-values.md` | B | H/H/H | RP-04 |
| G-05 | `G-05-preference-data-provenance.md` | B | M/M/M | RP-04 (fold-in) |
| G-06 | `G-06-reward-hacking-generalization.md` | B | H/M/M | RP-09 (measurement) |
| G-07 | `G-07-no-gold-oversight.md` | C | H/H/H | RP-03 |
| G-08 | `G-08-weak-to-strong-values.md` | C | H/M/M | RP-03 (fold-in) |
| G-09 | `G-09-judge-corruption.md` | C | H/H/H | RP-03, RP-04 |
| G-10 | `G-10-social-choice-alignment.md` | D | H/M/M | RP-02 |
| G-11 | `G-11-deliberation-pipelines.md` | D | M/H/H | RP-08 |
| G-12 | `G-12-legitimacy-procedural-justice.md` | D | M/H/M | RP-08 |
| G-13 | `G-13-moral-reasoning-faithfulness.md` | E | H/H/H | RP-06 |
| G-14 | `G-14-evaluation-awareness.md` | E | H/H/H | RP-07 |
| G-15 | `G-15-alignment-faking-evaluation.md` | E | H/M/H | RP-07 |
| G-16 | `G-16-agentic-misalignment-empirics.md` | F | H/M/M | acquisition → UNMARKED |
| G-17 | `G-17-multi-agent-value-dynamics.md` | F | H/M/M | RP-10 |
| G-18 | `G-18-value-persistence-drift.md` | F | H/H/H | RP-05 |
| G-19 | `G-19-delegated-authority-economics.md` | F | M/L/L | watch-list |
| G-20 | `G-20-emergent-misalignment-persona.md` | G | H/H/H | RP-09 |
| G-21 | `G-21-subliminal-value-transmission.md` | G | H/L/L | acquisition |
| G-22 | `G-22-character-training-science.md` | G | H/M/H | RP-01/RP-09 axis |
| G-23 | `G-23-coherent-values-adjudication.md` | G | H/H/H | RP-06/RP-09 |

S/T/F = Severity / Tractability / CEI-fit (defined in `../02-gap-atlas.md`). Stages A–G per the atlas (A–F pipeline + G value-formation science).

## Dossier template (uniform)

```
# G-NN — <Title>
**Stage** · **Ratings S/T/F** · **Programs** · **Kernel:** Fable 5, 2026-07-07 (FROZEN) · **Body:** Opus draft 2026-07-07

## Statement                       [KERNEL — FROZEN]
## Why it matters                  [KERNEL — FROZEN]
## Evidence                        (corpus + field; drafted)
## State of the art                (drafted)
## What closing looks like         [KERNEL — FROZEN]  (milestones M1–M3)
## CEI response                    [KERNEL — FROZEN]
## OPUS-EXPAND checklist           (LIVING — check off / append)
## Sources                         (evidence classes marked; ⚠ per ../04-missing-literature.md)
```

## Rules

- Kernel sections are frozen (governance protocol §4); disagreement → PENDING-RULING, not an edit.
- Expansions append below as `## [OPUS-EXPANSION YYYYMMDD] <topic>`; checklist items get checked off in place.
- Sources cite only material present in `../02`, `../03`, `../04`, or the field-map deep dives — no new unverified claims; keep ⚠ flags.
- Gap IDs are stable forever; a gap that closes gets a dated CLOSED note appended, never deletion.
