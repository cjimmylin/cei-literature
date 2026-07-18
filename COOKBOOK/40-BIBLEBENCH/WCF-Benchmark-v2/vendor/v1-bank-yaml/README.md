# WCF-Bench Item Bank — YAML (spine §10)

**Date:** 2026-07-09 · **Author:** opus · **Loader:** `../04-HARNESS/wcfbench/loader.py`

The machine-ingestable form of the WCF-Bench item bank. Each `*-expansion2.yaml`
holds one design's expansion-2 items as multi-document YAML (one `---` doc per
item), transcribed from the prose banks per `TRANSCRIPTION-SPEC.md`. Load the
whole directory with `wcfbench.load_items("05-BANK-YAML")`.

## What is transcribed (this session)

The **expansion-2 batch — all 10 designs, 69 items** — the Fable-reviewed
(session 4) set the boot prompt unblocked. Lint-loads with **0 schema errors**.

| Design | File | Items | Status | Notes |
|--------|------|-------|--------|-------|
| aggravate | `aggravate-expansion2.yaml` | 8 | expanded | `gold_order` on all; **E3.2** dual-credit on W302; W304/W305 = `declines total order` |
| complicit | `complicit-expansion2.yaml` | 7 | reviewed | `construct_specificity` on all 7 (R2 routes) |
| crosswind | `crosswind-expansion2.yaml` | 7 | reviewed | **E2** Q135 verbatim anchor on W303, W305 |
| dutybound | `dutybound-expansion2.yaml` | 7 | reviewed | **E1** on W301 rubric (Sat-evening only) |
| liberty | `liberty-expansion2.yaml` | 7 | reviewed | **E3.1** usury anchor on W304; **`dev_set_only`+`disputed`** on W304, W305 |
| mending | `mending-expansion2.yaml` | 7 | reviewed | multi-turn repair; MEND-A-W305 = Track-A planted-error |
| narrowgate | `narrowgate-expansion2.yaml` | 6 | expanded | `episode: true` + `construct_specificity` on all 6 (T4 agentic) |
| prooftext | `prooftext-expansion2.yaml` | 7 | expanded | anchored keypoints for the anchor scorer |
| steadfast | `steadfast-expansion2.yaml` | 7 | reviewed | `construct_specificity` on STED-C1-W306 |
| wholeheart | `wholeheart-expansion2.yaml` | 6 | reviewed | `judge_calibration: true` on WHOLE-C10-W305 (G4 battery) |

**Harness-consumed extra fields** (preserved in `ItemRecord.extra`): `gold_order`
(AGGRAVATE ordinal key), `construct_specificity` (R23a `{route, reskin}`, 16 items),
`dev_set_only`+`disputed` (the two G6-pending `[DISPUTED]` legs), `episode` (the 6
NARROWGATE state-machine items), `judge_calibration` (the G4 instrument).

## What is NOT yet transcribed (the mechanical remainder — no silent cap)

The three earlier waves remain in prose only (~161 items to reach the 230-item
suite). Transcribing them is the same mechanical pass against `TRANSCRIPTION-SPEC.md`:

- **exemplars** — `01-DESIGNS/*.md` (001–005 per design) + `exemplars-wave2/`.
- **wave-2** — W201–W206 per design.
- **expansion-1** — `01-DESIGNS/expansions/20260706-*.md` (006–010).

**Carry-forward for that pass:** the other two named `[DISPUTED]` legs live in the
earlier waves and must get `dev_set_only: true` + `disputed: true` when transcribed:
**LIB-C7-008** (expansion-1) and **LIB-C3-W202** (wave-2). See `TRANSCRIPTION-SPEC.md` §5.

## Verify

```bash
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python - <<'PY'
import sys; sys.path.insert(0, "COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/04-HARNESS")
from wcfbench import load_items
print(len(load_items("COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/05-BANK-YAML")), "items, 0 errors")
PY
```

Canary `WCFBENCH-CANARY-c1647-x9k4q` once per file (spine §6; not re-minted).
Every number the harness produces on these items pre-live-run is not a measurement.
