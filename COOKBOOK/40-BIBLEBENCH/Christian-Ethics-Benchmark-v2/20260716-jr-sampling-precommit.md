# JR sampling pre-commitment — Opus judge-referee meta-audit

**Date:** 2026-07-16 · **Session:** WALKWORTHY v2 side-session JR
**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content

## What this commits to

This memo FREEZES the referee sample BEFORE any Opus referee dispatch, analogous
to the crossharness mapping-precommit pattern. The manifest is the population;
**no additions after the first dispatch.** Re-asks of failed/refused batches use
the same frozen prompts only.

## Framing guardrail (verbatim, applies to every downstream artifact)

This is NOT benchmark work and adds nothing to the benchmark. "Closer to Opus" =
**reference-model concordance, not ground truth** — Opus is a stronger model,
not an oracle; where Opus sides with one judge, that is evidence about judge
character, not correctness. Results change NO judge pins, enter NO benchmark
reports, and trigger NO instrument changes without a separate explicit owner
ruling. (R1/R3 + ratified F11 govern benchmark claims; this data lives outside
that instrument entirely.)

## Frozen artifacts

| Artifact | Location | Integrity |
|---|---|---|
| Prompt exports | `logs/jr-referee-20260716/prompts-{02,07,06}.jsonl` (gitignored) | byte-identical shipped prompts; determinism-verified across two export runs; per-row `prompt_sha256` |
| Sampling manifest | `logs/jr-referee-20260716/sample-manifest.jsonl` (gitignored) | **sha256 `b2839b1413c6b94a9bf2912497c414df9e83751d84fb97df743b436807f5ef9f`**; byte-identical across two generator runs |
| Manifest metadata | `logs/jr-referee-20260716/manifest-meta.json` (gitignored) | seed, draw order, counts, unresolved-unit keys |
| Export tool | `tools/audit/export_referee_prompts.py` (committed) | reuses `assemble_rubric_prompt` verbatim — never forked |
| Manifest tool | `tools/audit/make_referee_manifest.py` (committed) | seeded, deterministic |

Prompt fidelity: design 02 exported anchors-as-shipped (NO anchor block — 02
ships un-anchored; `spec_for("02").reference_anchored=False` verified); design
07 exported context-FREE with anchors as shipped (NO `context_patch`); design 06
single-turn via the `rescore.py` reassembly call. sha256 custody copied from
`judge_certify.py`.

## Prompt universe (exported, all judgeable units)

| Design | Per SUT | Total | Notes |
|---|---|---|---|
| 02 | 322 turns | 1,610 | 0 skipped |
| 07 | 163 turns | 815 | 0 skipped |
| 06 | 31 completions | 155 | 9 units unresolved for gap-ranking (judge-B all-null profile) — excluded from ranking, keys recorded in manifest-meta |

SUTs (5): deepseek-chat, gemini-flash-lite, gpt-4.1-mini, llama-3.3-70b,
mistral-small. Join discipline: every join scoped by (sut, log basename,
sample_id); turn index positional in decoded `turn_states`.

## Sampling design (owner-ruled scope: designs 02 + 07 + 06; no gpt-4.1-mini arm)

- **Seed:** `random.Random(20260716)`, one instance.
- **Draw order (fixed):** 07-controls → 02-disagreement → 02-controls →
  06-controls. Wholesale takes (07 all-disagreement; 06 top-60 gap) consume no RNG.
- **Candidate ordering:** sorted by (design, sut, log, sample_id, turn_index)
  before every draw.
- **Disagreement definition (02/07):** judge-A state != judge-B state at the same
  positional turn; `unscorable` counts as a state (state-vs-unscorable =
  disagreement; both-unscorable = agreement).
- **06 gap ranking:** |profile_mean_A − profile_mean_B| descending, ties broken
  by unit-key sort; top 60 = gap stratum; controls sampled from the remaining 86
  resolved units.

## Frozen sample (n = 942)

| Design | Stratum | n | Basis |
|---|---|---|---|
| 07 | disagreement | 392 | ALL disagreement turns (base rate 0.481 of 815) |
| 07 | control | 150 | seeded sample of agreement turns |
| 02 | disagreement | 200 | seeded sample (base rate 0.7665 = 1,234/1,610 — disagreement is the majority class) |
| 02 | control | 80 | seeded sample of agreement turns |
| 06 | gap | 60 | top-60 |Δ profile_mean| (span 0.143–0.786) |
| 06 | control | 60 | seeded sample of remaining 86 |

Per-SUT manifest rows: deepseek-chat 196, gemini-flash-lite 198, gpt-4.1-mini
181, llama-3.3-70b 197, mistral-small 170.

Unscorable-involvement among sampled-population disagreement units: 02 = 88,
07 = 19. The sample is deliberately disagreement-enriched — **no pooled
"overall agreement" headline may be reported without the per-stratum split
adjacent.**

## Planned dispatch protocol (gated; NOT yet executed)

- ~25 prompts/batch → **~38 Opus dispatches** (942/25), Claude Code `Agent`
  calls with explicit `model: opus`, OAuth subscription channel, **zero
  OpenRouter/API calls all session** (channel explicitly owner-authorized
  2026-07-16 for this non-benchmark meta-audit; AGENTS.md rule 3 governs
  benchmark measurement, which this is not).
- BLIND: referee agents receive prompt texts + output contract only — never
  judge-A/B verdicts, repo paths, or SUT identities. Batches avoid two turns of
  the same ladder where avoidable; within-batch non-independence is a documented
  caveat regardless.
- Ingest: `logs/jr-referee-20260716/opus-verdicts.jsonl`, append-only, echo
  `prompt_sha256`, reject hashes not in the manifest, resume-able
  (certify-events skip pattern). Refusals/unparseables recorded honestly; no
  hand-patched verdicts.
- **Volume gate:** owner confirmation required after this memo, before the
  first dispatch.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
