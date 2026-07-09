# RP-04 HIDDENCURRICULUM — Frozen Response Corpus

**Created:** 2026-07-09 · **Handoff item:** 1.5 of `INNOVATION/07-opus-handoff.md`
**Brief (binding, incl. kill criteria):** `INNOVATION/05-research-programs/RP-04-HIDDENCURRICULUM.md`
**Source repo git HEAD at freeze:** `1fbda2815bd7c63d1b072a6d0312a8e68c2273aa`

This directory freezes the pilot outputs and item banks that RP-04 Phase 1 ("dogfood") intended to re-score with 3+ judge families. Everything under `frozen/` was **copied read-only** from the source trees (never moved, never modified).

---

## ⚠ PROVENANCE HEADLINE — read before using anything here

RP-04 Phase 1 was scoped to "re-score a frozen sample of existing CEI bank **responses**." Assembling this corpus established that **those responses do not exist as real model behavior:**

- **Real, re-scoreable model responses: 0.**
- The only real-model behavior anywhere in the three pilots is the **THORNS N=4 probe** (single-vendor, hand-scored) — and its **verbatim response text was never saved**, so it cannot be re-judged. It is frozen as a qualitative anchor (`frozen/thorns/REAL-probe-N4.json`), not as measurement input.
- **All response-level records on disk are synthetic-mock:** WITNESS `scored.jsonl` (10,350 rows, `mock-alpha/beta/gamma`) and DIMGLASS `scored_runs.MOCK.jsonl` (80 grade labels, no text) were produced by deterministic simulators (`MockModelClient` / `SyntheticModel`). Both real-client stubs (`AnthropicClient`, `CodexClient`) raise `NotImplementedError`; no API keys exist in the vault.
- The THORNS synthetic result JSONs store **aggregate rates only** — no raw response text at all.
- The remaining bulk is **stimulus** (prompt banks) and **scoring keys**, not responses.

**Fraction synthetic vs real (response-level records): 100% synthetic-mock, 0% real.**

**The binding rule (the SERMONMOUNT lesson):** synthetic-mock entries can validate the re-scoring **MACHINERY** only — they can *never* enter a judge-bias measurement as if they were model behavior. The judge-bias memo (H3) that other BibleBench families are meant to cite therefore **cannot be produced in Cycle 1**; it is fully key-gated. See `20260709-rescoring-matrix.md`.

Do not describe this corpus as "re-scored pilot responses." It is a frozen **stimulus set + machinery-validation set**, plus one text-less real-probe anchor.

---

## Contents by provenance class

| Class | Entries | Re-scoreable as model behavior? |
|---|---|---|
| `real-model` | THORNS N=4 probe (no verbatim text) | No — nothing to re-judge |
| `synthetic-mock` | WITNESS scored.jsonl (10,350), DIMGLASS mock jsonl (80) | Machinery-validation only |
| `derived-synthetic` | THORNS results JSON ×2 (aggregates) | No |
| `human-authored-stimulus` | THORNS bank 60, WITNESS renderings 240 / cores 30 | Stimulus → yields responses in Cycle 2 |
| `human-authored-key` | THORNS gold 60 | Scoring key |
| `synthetic-generated-stimulus` | DIMGLASS public seeds 30, episode_table 80 | Stimulus → yields responses in Cycle 2 |
| `synthetic-generated-key` | DIMGLASS ground_truth (1026 keys) | Scoring key |

Full per-entry provenance, source paths, record counts, and item linkage: **`manifest.json`**.

## Directory layout

```
rp04-corpus/
  README.md                      ← this file
  manifest.json                  ← per-entry id / source / provenance / linkage
  20260709-rescoring-matrix.md   ← judge families × strata × dimensions; Cycle-2 key-gate list
  frozen/
    thorns/    (2 synthetic JSON, pilot report, REAL-probe-N4.json, bank/ 60, gold/ 60)
    dimglass/  (seeds_public 30, ground_truth 1026 keys, mock jsonl 80, episode_table 80)
    witness/   (scored.jsonl 10,350 mock, renderings 240, cores 30)
```

## Not copied (referenced only)

- DIMGLASS `episodes/private_bank.yaml` (996 private/holdout episodes, 1.9 MB) — deliberately **not** frozen into INNOVATION to preserve the contamination/holdout split. The 30 public seeds are the representative frozen sample; all 1026 scoring keys are included via `ground_truth.json`.

## Source locations (all under `COOKBOOK/40-BIBLEBENCH/`)

- THORNS: `FRUITBENCH-v2/PILOTS/thorns/` + `FRUITBENCH-v2/ITEMS/thorns/`
- DIMGLASS: `CORINTHLOVE-v2/BANKS/09-dimglass/`
- WITNESS: `SERMONMOUNT-v2/DESIGNS/09-witness/`

(Note: the handoff's paths omitted the `COOKBOOK/40-BIBLEBENCH/` prefix; corrected here.)

## Next step

Cycle 1 (now): build/validate the re-scoring pipeline on the synthetic-mock lane (S1) only. Cycle 2 (keys — Jimmy gate #1): run subject models against the frozen stimulus banks to produce real responses (S3), then execute the matrix. Kill criteria K1–K3 and the K2 pre-commit (mandatory robustness pass if biases threaten published verdicts) are binding — see the matrix doc.
