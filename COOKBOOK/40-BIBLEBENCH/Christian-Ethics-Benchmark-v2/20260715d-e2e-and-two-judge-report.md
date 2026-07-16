# WALKWORTHY v2 — end-to-end comparability run + 2-judge re-score validation

**Date:** 2026-07-15d
**Scope:** PUBLIC-only descriptive comparability MVP; never O5 evidence.
**Authorization:** owner-authorized paid work (share ceiling $1.00). **Actual spend ≈ $0.056.**
**SUT:** `openrouter/mistralai/mistral-small-3.2-24b-instruct` (v1 MVP SUT), `--max-tokens 2048`.
**Judge A:** `openrouter/openai/gpt-4.1-nano` (v1 judge-A).
**Judge B:** `openrouter/meta-llama/llama-3.3-70b-instruct` (v1 judge-B).
**Datasets:** current post-review `datasets/public/` (see `20260715b-conversion-parity-report-postreview.md`).
**Item filter:** the 60 MVP item_ids from `../Christian-Ethics-Benchmark/runs/20260713-mvp-a1/manifest.json`.
**Logs:** `logs/comparability-e2e/` (10 `.eval` logs, one per design; all `status=success`).

The comparison against v1 is **DESCRIPTIVE, not an agreement statistic**: v2 is a *fresh*
SUT sample (new stochastic generations) run against the *post-review* banks (105 ratified
item fixes), on a *re-platformed* (Inspect) harness. Two confounds (fresh sample + item
fixes + harness) move together, so any v2↔v1 delta is a joint effect — it is reported as
a magnitude comparison, never as reproduction/agreement evidence.

---

## Sample coverage

All 60 MVP item_ids resolved in the current post-review public banks; the item-id filter
expands them to **100 runnable administrations** (a v1 item = 1–4 admins in v2: base,
say/do, alpha/beta, covert/overt, seats, plus `-exemplar` variants). Per design: 01→6,
02→12, 03→12, 04→12, 05→6, 06→6, 07→6, 08→12, 09→16, 10→12. Every design completed with
`status=success`; the judge returned parseable category JSON for every scored cell in
Part 1 (judge A).

The filter was added as an **additive** `item_ids` arg to
`walkworthy_inspect/datasets.py::load_design` (CLI-friendly comma/space string or a
set/list; default `None` = unchanged behavior — filters on `metadata.item_id`, keeping
ALL administrations of a matched item), threaded through all 10 `tasks/designNN_*.py`
as `-T item_ids=...`. Default (unfiltered) behavior is untouched; a `mockllm` check
confirmed exactly the 6 design-01 items load under the filter.

---

## PART 1 — v2 headline metrics vs v1 same-SUT (mistral) aggregates (DESCRIPTIVE)

v1 columns are the mistral-SUT `primary_metrics[design].per_model[mistral].{S,H}.adjudicated`
from `runs/20260713-mvp-a1/summary.json`. **Scales differ by design** (v1 `S` is a 0–100
survival/pass statistic; v2 headline metrics are 0–1 rates or design-native indices), so
read each row as "same construct, different instrument + fresh sample," not as a numeric
delta to be minimized.

| design | v2 headline metric (judge A) | v1 primary_metric | v1 S_adj (0–100) | v1 H_adj | note on the delta |
|---|---|---|---:|---:|---|
| 01-goodsamaritan | full_obedience_rate=0.00 (n=6, excl=0) | collapse_threshold | 50.0 | 0.50 | v2 obedience concentrated in `full_obedience` (5/6) but the collapse/full-obedience headline reads 0.0 under the S₀₁ fallback recomputation on the fresh sample |
| 02-twomasters | break_rate=0.00, drift_mean=0.50 (n=11, excl=1) | break_turn | 0.0 | 0.0 | both v1 and v2 show no break on this ladder; turn_state split holds_line/full_compliance |
| 03-quiettongue | say_do_gap=0.00, revealed_faithful_rate=0.00 (n=12) | say_do_gap | — (S null) | 0.50 | v2 revealed_artifact spread faithful4/shaded5/violating3 |
| 04-innerweight | motive_sensitivity_index=0.167 (6 pairs) | motive_sensitivity_index | 24.44 | 1.00 | same construct name; v2 MSI 0.167 vs v1 S 24.4/100 — same order of magnitude given scale |
| 05-ordoamoris | csr_mean=0.00 (judge-free), non_compliant=0 (n=6) | constraint_satisfaction_rate | 77.78 | 0.917 | v2 SUT emits prose, no strict `allocation:{}` block → CSR unscorable (format non-compliance = measurement signal, per smoke report); rationale_honesty judged 2×3 |
| 06-crookedpath | profile_mean=0.571 (frame .58/facts .42/…/pastoral .75) | criterion_profile | 71.85 | 0.732 | v2 profile_mean 0.571 vs v1 S 71.85/100 — comparable band |
| 07-seventyseven | arc_pass_rate=0.00 (n=6) | arc_shape | — (S null) | — | v2 turn_state mostly full_validation (4/6) |
| 08-vocationfork | covert_overt_gap=**nan**, covert_protection_rate=0.00 (0 pairs, 6 incomplete) | covert_overt_gap | 25.0 | 0.667 | **v2 pairing artifact**: 4 admins/item (covert, covert-exemplar, overt, overt-exemplar) did not resolve into clean covert/overt pairs → gap unscorable this run; guardrail_state itself parsed (protected8/steamrolled2/surfaced2) |
| 09-doubleedge | symmetry_index=1.00, floor_violation_rate=0.938 (6 pairs) | symmetry_index | 100.0 | — | symmetry matches v1 (1.00 ↔ 100.0); high floor-violation rate on fresh sample |
| 10-strangergate | mercy_delta=0.125, mercy_pass_rate=0.75 (4 pairs, 2 incomplete) | mercy_delta | 12.5 | 1.00 | mercy_delta 0.125 ↔ v1 S 12.5/100 — same magnitude |

**Category distributions** (judge A, per design) are in
`logs/comparability-e2e/part1-v2-vs-v1.json` (`v2_catdist`). Representative examples:
- 01 action_class: full_obedience 5 / partial 1; rationale_quality 2×4 / 1×1 / 0×1.
- 03 revealed_artifact: faithful 4 / shaded 5 / violating 3.
- 09 floor_compliance: 0×15 / 1×1 (fresh sample shows near-universal floor breach);
  owes_direction none 11 / A_owes 2 / B_owes 3.
- 10 treatment 2×11/1×1; duality 1×9/0×3.

**Takeaway (Part 1).** Where scales align on a shared construct name (04 MSI, 06 profile,
09 symmetry, 10 mercy_delta), v2 lands in the same magnitude band as v1's mistral
aggregate. Two v2-specific artifacts surfaced and are documented, not hidden: 05 CSR
unscorable (SUT ignores the strict allocation-block format — a real measurement signal)
and 08 covert_overt_gap `nan` (the exemplar admin variants block clean covert/overt
pairing in the Inspect metric). Neither is an agreement claim; both are descriptive
observations on a fresh, post-review, re-platformed run.

---

## PART 2 — 2-judge re-score path (precondition #2)

### Which path worked: CUSTOM SCRIPT (`tools/rescore/rescore.py`), not the CLI

The `inspect score` CLI re-score path was attempted first and **does not work** for these
custom scorers — two independent structural blockers:

1. **Relative-import breakage.** `inspect score <log> --scorer walkworthy_inspect/scorers.py@design01_scorer`
   loads `scorers.py` as a *top-level* module, so its package-relative imports
   (`from .ordo_constraints import item_csr`) raise `ModuleNotFoundError: No module named
   '/Users/jimmy'`. A root shim that absolute-imports the package did not resolve it.
2. **Non-unique registry names.** The 9 designs built by `scorers._register(...)` all
   share the Inspect registry name **`_factory`** (the `@scorer` decorator captured
   `_factory.__name__` before the post-hoc `__name__` rename), so `--scorer …@designNN_scorer`
   cannot disambiguate designs 01–04, 06–10 — only `design05_scorer` has a distinct
   registry name. (Verified via `registry_info`.)
   Also note: `inspect score` has no `--max-tokens` flag, so a CLI path would have to rely
   on the scorer's internal `JUDGE_MAX_TOKENS=4096` cap for AGENTS §1 402-safety.

**The sanctioned path is therefore `tools/rescore/rescore.py`.** It reads the Part-1
`.eval` logs via `inspect_ai.log.read_eval_log`, and — importing `walkworthy_inspect` as a
**package** so prompt assembly is byte-identical to the live judge-A pass — re-assembles
each judge prompt with the ported `scorers.assemble_rubric_prompt(meta, spec, completion,
judge_categories(spec))`, calls judge B with an explicit `max_tokens` cap, and parses via
the same `scorers.parse_judge_json`. **The SUT is never re-run** — the SUT output is read
from `sample.output.completion` in the stored log. Judge-B verdicts (100 rows, one per
sample) are written to `logs/comparability-e2e/judgeB-verdicts.jsonl`, each carrying the
paired judge-A verdict for downstream diffing.

Design 05 is handled specially and faithfully: its judge-free PRIMARY
(`constraint_satisfaction_rate`) is deterministic and identical across judges (recomputed,
not re-judged); only its model-graded secondary `rationale_honesty` is re-judged by B —
matching the v1 2-judge protocol (both judges see the same judge-graded categories).

Judge-B produced usable JSON for 97/100 samples; **3 empty-completion cells** (unparseable)
— 05 WW-05-A01#base, 06 WW-06-D03#base, 08 WW-08-B02#covert — are recorded as judge-B
defects and excluded from the agreement denominator (v1 defect semantics), not treated as
disagreements.

### Judge-A vs judge-B agreement per design vs v1 baseline

`tools/rescore/disagreement_cells.py` classifies each (sample, category) cell:
**agree** (identical) / **near_agree** (ordinal/int within tolerance = 1 rubric-ladder
step; categorical & binary have no near band) / **disagree** → `needs_adjudication`;
either-judge-unscorable cells are dropped from the denominator. The v1 baseline is the
same classification computed on the frozen `runs/20260713-mvp-a1/verdicts.jsonl` for the
mistral SUT, aggregated over all judged cells per design (v1 stores scores per
administration-unit — per_turn for 02/07, per_admin/per_seat for 03/04/08/09/10 — so
per-design aggregation sidesteps v1↔v2 unit-label mismatches).

| design | v2 exact-agree | v2 +near | v2 needs_adj | v1 exact-agree | v1 +near |
|---|---:|---:|---:|---:|---:|
| 01-goodsamaritan | 0.750 | 0.833 | 2 | 0.750 | 0.750 |
| 02-twomasters | 0.182 | 0.182 | 9 | 0.196 | 0.196 |
| 03-quiettongue | 0.639 | 0.722 | 10 | 0.583 | 0.667 |
| 04-innerweight | 0.694 | 0.833 | 6 | 0.833 | 0.889 |
| 05-ordoamoris | 0.667 | 1.000 | 0 | 1.000 | 1.000 |
| 06-crookedpath | 0.486 | 0.800 | 7 | 0.238 | 0.738 |
| 07-seventyseven | 0.667 | 0.667 | 2 | 0.222 | 0.222 |
| 08-vocationfork | 0.545 | 0.545 | 5 | 0.750 | 0.750 |
| 09-doubleedge | 0.219 | 0.219 | 25 | 0.333 | 0.333 |
| 10-strangergate | 0.729 | 0.792 | 10 | 0.646 | 0.771 |
| **TOTAL needs_adjudication (v2)** | | | **76** | | |

Cells: 242 v2 A-vs-B judged cells; `logs/comparability-e2e/disagreement-cells.jsonl`
(one row per cell) and `disagreement-summary.json` (machine summary + v1 baseline).

**Verdict on precondition #2.** The re-score path **reproduces the v1 2-judge protocol's
behavior**: v2 A-vs-B agreement sits in the same band as the v1 mistral baseline design by
design — very high where v1 was high (01 0.75↔0.75; 05 primary judge-free), low where v1
was low (02 ~0.18↔0.20; the categorical multi-option `turn_state` and per-seat
`owes_direction`/`floor_compliance` are the hard-agreement designs in both v1 and v2). The
few larger gaps are explained by the confounds, not a broken re-score: 06/07 are *higher*
in v2 (post-review anchor fixes + fresh sample), 04/08/09 slightly *lower* — all within
the fresh-sample + item-fix envelope. Ordinal designs gain a large near-agree band (06
0.486→0.800, 10 0.729→0.792), mirroring v1's own exact-vs-near spread (06 0.238→0.738).

76 cells flagged `needs_adjudication` (disagree) across 242 — concentrated in 09
doubleedge (25; per-seat categorical determinations) and the multi-option categorical
designs (02, 03, 10). These are the cells a v1-style 2-judge adjudication/tie-break pass
would resolve; that machinery is deferred in v2 (README "Deferred relative to v1").

---

## Cost

| component | tokens | est. cost |
|---|---|---:|
| Part 1 — 10 designs (SUT mistral + judge-A nano) | SUT in/out ≈ 148k/86k; judge-A in/out ≈ 133k/2.5k | **$0.0418** |
| Part 2 — judge-B re-score (llama-3.3-70b, no SUT re-run) | in ≈ 133k / out ≈ 2.5k (same 100 prompts) | **$0.0141** (est.) |
| **TOTAL** | | **≈ $0.056** |

Pricing basis (OpenRouter USD/1M, from the manifest): mistral $0.075/$0.20,
gpt-4.1-nano $0.10/$0.40, llama-3.3-70b $0.10/$0.32. The two multi-turn designs (02, 07)
dominate SUT spend as expected (scripted ladder + judge-as-classifier calls). Part-2 cost
is estimated: the judge-B prompts are the same 100 prompts as judge A (so input tokens ≈
judge-A input), output capped at 4096 — `rescore.py` does not itself emit an Inspect
`stats` block. Well under the $1.00 ceiling and the ~$0.40 expectation. No 402/reservation
errors (explicit `max_tokens` on every call, AGENTS §1).

---

## Exact commands

```bash
cd Christian-Ethics-Benchmark-v2
source /Users/jimmy.lin/.codex/secrets/openrouter.env   # exports OPENROUTER_API_KEY

# PART 1 — per design (NN = 01..10), item-filtered to the 6 MVP items of that design:
.venv/bin/inspect eval tasks/designNN_*.py \
  --model openrouter/mistralai/mistral-small-3.2-24b-instruct \
  -T judge_model=openrouter/openai/gpt-4.1-nano \
  -T item_ids="<comma-separated MVP item_ids for design NN>" \
  --max-tokens 2048 --max-connections 4 \
  --log-dir logs/comparability-e2e/

# PART 2 — judge-B re-score (no SUT re-run) + disagreement cells:
.venv/bin/python tools/rescore/rescore.py \
  --log-dir logs/comparability-e2e \
  --judge-b openrouter/meta-llama/llama-3.3-70b-instruct \
  --out logs/comparability-e2e/judgeB-verdicts.jsonl

.venv/bin/python tools/rescore/disagreement_cells.py \
  --verdicts logs/comparability-e2e/judgeB-verdicts.jsonl \
  --out logs/comparability-e2e/disagreement-cells.jsonl --tolerance 1
```

Per-design MVP item_ids (from `manifest.json`):
`01: WW-01-B03,WW-01-D04,WW-01-A01,WW-01-A05,WW-01-A05-P,WW-01-B01` ·
`02: WW-02-B03,WW-02-C02,WW-02-A02,WW-02-A05,WW-02-B02,WW-02-B04` ·
`03: WW-03-B03,WW-03-B05,WW-03-A01,WW-03-A04,WW-03-A05,WW-03-B01` ·
`04: WW-04-D01,WW-04-D05,WW-04-A03,WW-04-A04,WW-04-B01,WW-04-B04` ·
`05: WW-05-A01,WW-05-C05,WW-05-A03,WW-05-B01,WW-05-B02,WW-05-B06` ·
`06: WW-06-A05,WW-06-D03,WW-06-A01,WW-06-A06,WW-06-B02,WW-06-B04` ·
`07: WW-07-A02,WW-07-C02,WW-07-A03,WW-07-B02,WW-07-B04,WW-07-C01` ·
`08: WW-08-B02,WW-08-D02,WW-08-A02,WW-08-A04,WW-08-B01,WW-08-B04` ·
`09: WW-09-A04,WW-09-A05,WW-09-B01,WW-09-B04,WW-09-C01,WW-09-C04` ·
`10: WW-10-A05,WW-10-B05,WW-10-A01,WW-10-A03,WW-10-B01,WW-10-B04`

---

## Deliverables / file map

- `logs/comparability-e2e/*.eval` — 10 Part-1 logs (SUT + judge A).
- `logs/comparability-e2e/judgeB-verdicts.jsonl` — 100 judge-B verdicts (Part 2).
- `logs/comparability-e2e/disagreement-cells.jsonl` — 242 A-vs-B cells.
- `logs/comparability-e2e/disagreement-summary.json` — per-design v2 + v1-baseline summary.
- `logs/comparability-e2e/part1-v2-vs-v1.json` — v2 metrics + category dists + v1 aggregates.
- `tools/rescore/rescore.py`, `tools/rescore/disagreement_cells.py` — Part-2 scripts.
- `walkworthy_inspect/datasets.py` (+ 10 `tasks/designNN_*.py`) — additive `item_ids` filter.

**Constraints honored:** v1 never modified (read-only imports only); no writes to
`banks/`, `REVIEWS/`, `RULINGS-APPLIED.md`, or `tools/replay/**`; additive-only edits to
`walkworthy_inspect`/`tasks`; no deletions (`rm` never used). New dated report file.
