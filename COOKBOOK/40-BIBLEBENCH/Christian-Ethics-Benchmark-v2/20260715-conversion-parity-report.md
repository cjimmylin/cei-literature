# WALKWORTHY v2 conversion parity report

**Date:** 2026-07-15  
**Public dir:** `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/datasets/public`  
**Holdout dir:** `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/datasets/holdout`  
**O4 manifest:** `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/runs/20260711-o4-claude-sonnet4/manifest.json`  
**Overall:** PASS ✅

A JSONL line = one **administration** (seat / twin / motive arm / scripted conversation). Single-administration designs emit one line per item. The manifest parity target is at the **item** level (344 runnable items).

## 1. Public per-design counts vs O4 manifest (item-level target = 344)

| design | items | runnable items | manifest | match | lines | runnable lines |
|--------|------:|---------------:|---------:|:-----:|------:|---------------:|
| 01 | 49 | 49 | 49 | ✅ | 49 | 49 |
| 02 | 39 | 36 | 36 | ✅ | 76 | 72 |
| 03 | 33 | 33 | 33 | ✅ | 66 | 66 |
| 04 | 33 | 33 | 33 | ✅ | 60 | 60 |
| 05 | 32 | 32 | 32 | ✅ | 32 | 32 |
| 06 | 31 | 31 | 31 | ✅ | 31 | 31 |
| 07 | 31 | 27 | 27 | ✅ | 31 | 27 |
| 08 | 33 | 33 | 33 | ✅ | 66 | 66 |
| 09 | 38 | 34 | 34 | ✅ | 92 | 88 |
| 10 | 36 | 36 | 36 | ✅ | 72 | 72 |
| **TOTAL** | **355** | **344** | **344** | ✅ | **575** | **563** |

## 2. Delta-from-344 explanation

- **Runnable public items = 344** → **delta from 344 = +0** (exact match).
- Total public items = 355; runnable = 344; non-runnable = 11.
- The non-runnable public items are the **sketch exemplars** parsed from the `*-SPEC` design files (`02-twomasters.md`, `07-seventyseven.md`, `09-doubleedge.md`). These are abbreviated prose sketches with no materializable model input, so `Item.is_runnable()` is False and they are emitted with `runnable:false` per SCHEMA. They are excluded from the 344 run surface (which the loader filters by default).
- Runnable-item counts match the O4 manifest per-design exactly: 01=49, 02=36, 03=33, 04=33, 05=32, 06=31, 07=27, 08=33, 09=34, 10=36.
- **Line-level (administration) expansion** is larger than item counts for the multi-administration designs: 03 say/do twins (×2), 04 α/β motive pairs (×2, plus 4b singles ×1), 08 covert/overt (×2), 09 seat_A/seat_B/seat_C + arbiter (2–3 seats + probe), 10 N/U desert-cue arms (×2), and 02 which adds a `cold_open` control administration alongside the scripted ladder. 01/05/06/07 are one line per item (07's scripted ladder is a single administration; its full turn script lives in `metadata.multiturn`).

## 3. Integrity checks

| check | result | detail |
|-------|:------:|--------|
| ID uniqueness across public+holdout | ✅ | 835 lines; 0 duplicate ids |
| Canary present in 100% of lines | ✅ | 835/835 carry `WALKWORTHY-CANARY-7f3e2026` |
| Every runnable line non-empty input | ✅ | 0 bad of 823 runnable |
| Every runnable line non-empty target | ✅ | 0 bad |
| Every line (incl. non-runnable) non-empty target | ✅ | 0 bad |
| Public/holdout RUNNABLE item-id disjoint | ✅ | 0 overlap |
| Public/holdout hard (runnable-vs-runnable) disjoint | ✅ | 0 hard overlap |

## 4. Public/holdout item-ID overlap (raw vs runnable)

- Public item-ids: 355 (344 runnable). Holdout item-ids: 158 (158 runnable).
- **Runnable-surface overlap: 0** (none — the two run surfaces are fully disjoint).
- Raw item-id overlap: **3** → ['WW-02-A01', 'WW-02-F01', 'WW-02-G01'].
  - **Benign (3):** ['WW-02-A01', 'WW-02-F01', 'WW-02-G01']. On the public side these are **non-runnable sketch exemplars** (from the `02-twomasters.md` SPEC file); the same IDs were later **promoted to the holdout and expanded to full scripts** (per FC-3, e.g. `WW-02-A01 — Testimonial ladder (Fable exemplar; expanded to full script)`). Same id, different role: unrunnable public stub vs runnable holdout item. No public *run-surface* leakage.

## 5. Holdout per-design counts (informational; gitignored surface)

| design | items | runnable items | lines | runnable lines |
|--------|------:|---------------:|------:|---------------:|
| 01 | 22 | 22 | 22 | 22 |
| 02 | 18 | 18 | 36 | 36 |
| 03 | 15 | 15 | 30 | 30 |
| 04 | 15 | 15 | 27 | 27 |
| 05 | 14 | 14 | 14 | 14 |
| 06 | 13 | 13 | 13 | 13 |
| 07 | 13 | 13 | 13 | 13 |
| 08 | 15 | 15 | 30 | 30 |
| 09 | 17 | 17 | 43 | 43 |
| 10 | 16 | 16 | 32 | 32 |
| **TOTAL** | **158** | **158** | **260** | **260** |

_Holdout counts are reported for internal parity only; holdout item text is never included in committed prompts/reports (AGENTS §6)._

