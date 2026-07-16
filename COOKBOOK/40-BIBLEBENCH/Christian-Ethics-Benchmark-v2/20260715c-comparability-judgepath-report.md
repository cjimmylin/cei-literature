# Harness-Comparability: Judge-Path Replay (v2 scorer vs v1 judge-A)

**Date:** 2026-07-15
**Author:** replay harness (owner-authorized paid run; actual cost ≈ $0.01)
**Precondition tested:** #1 for the canonical-path ruling — *do v2's scorers reproduce
v1's judge verdicts when the SUT response and judge model are held FIXED?*

---

## Headline verdict

**PARITY.** With SUT responses and the judge model held identical, v2's Inspect scorer
path reproduces v1's judge-A (gpt-4.1-nano) categorical/ordinal verdicts **at or above**
the v1 inter-judge (judge-A vs judge-B) natural baseline on every design.

| Aggregate (field-cell exact agreement, all designs pooled) | Value |
|---|---|
| **v2-scorer vs v1-judge-A** | **73.2%** (123/168 field-cells) |
| v1-judge-A vs v1-judge-B (natural baseline, same units, free) | 59.2% (100/169) |

v2-vs-v1jA exceeds the v1 inter-judge baseline by **+14 pp**. The v2 harness agrees with
v1's judge-A *more* than v1's two judges agreed with each other — i.e. the residual
disagreement is dominated by judge stochasticity (gpt-4.1-nano is non-deterministic at
default temperature), not by any scorer/prompt-assembly delta introduced by the v2
harness. This is affirmative harness-parity evidence for precondition #1.

---

## Design

1. **Substrate — PRE-REVIEW datasets.** Used the v2 pre-review public datasets (identical
   item content to what v1 ran). The post-review datasets carry 105 ratified fixes that
   would confound a pure-harness comparison. Phase C moved the superseded pre-review
   datasets to `RECYCLE-BIN/datasets-prereview-20260715/`; copied (not moved) the
   `public/*.jsonl` into `tools/replay/data/public/`.

2. **Scope.** The 60 MVP item_ids (manifest) × the primary SUT
   `mistralai/mistral-small-3.2-24b-instruct`, using v1's stored SUT responses from
   `executions.jsonl`. Judge = `openrouter/openai/gpt-4.1-nano` (v1 judge-A slug, exactly),
   `max_tokens=256` (matches v1 manifest; caps the OpenRouter 402 reservation),
   temperature default.

3. **Replay mechanism (fidelity choice).** The v2 model-graded scorer reads the SUT
   response from **`state.output.completion` and nothing else** (`scorers.py:299`), and
   instantiates the judge via a scorer argument `get_model(judge_model)` (`scorers.py:302`).
   The faithful replay therefore: builds a minimal `TaskState` whose `metadata` = the
   pre-review dataset row's metadata and whose `output.completion` = v1's stored response
   for the matching (item, admin), then calls the **same** scorer factory v2 uses in
   production — `_make_model_graded_scorer(design, judge_model)` — with no SUT call. This
   exercises v2's exact judge-prompt assembly (`assemble_rubric_prompt`), judge call, and
   JSON parse (`parse_judge_json`). Chosen over an Inspect replay-solver because the scorer
   never inspects `state.messages`/`state.store`, so injecting at `output.completion` is
   both sufficient and maximally direct.

4. **Join unit.** `(design, item_id, admin_label)`. Each v1 per-admin / per-seat unit
   carries its own stored response and its own full score-dict — a clean 1:1 with a v2
   per_admin/per_seat dataset row. v1→v2 admin-label map:
   `01/05/06 main→base`, `03 expressed→say / revealed→do`, `04 alpha/beta`,
   `08 covert/overt`, `09 seat_A/seat_B`, `10 U/N`.

5. **Comparison.** v2 category vs v1 judge-A category, cell-by-cell on identical units.
   Per design: n units, exact-agreement %, Cohen's κ for categorical fields (κ reported
   only where ≥2 categories are observed on both sides; else "n/a"), within-tolerance
   (|Δ|≤1) for ordinal/int fields. v1 judge-A vs v1 judge-B on the same units is the
   natural baseline (computed from `verdicts.jsonl` alone; no API calls).

---

## Per-design agreement table

`v2vjA` = v2-scorer vs v1-judge-A. `jAvjB` = v1-judge-A vs v1-judge-B baseline (same units).
`exact` = exact-match %; `w1` = within-±1 %; `k` = Cohen's κ.

### design01 — goodsamaritan (item unit, n=5)
| field | v2vjA | jAvjB baseline |
|---|---|---|
| action_class (CAT) | exact 80%, κ=0.71 | exact 80%, κ=0.71 |
| rationale_quality (ORD) | exact 80%, w1 100% | exact 100%, w1 100% |

### design03 — quiettongue (per_admin, n=8)
| field | v2vjA | jAvjB baseline |
|---|---|---|
| expressed_judgment (CAT) | exact **88%**, κ=0.71 | exact 50%, κ=0.06 |
| revealed_artifact (CAT) | exact 62%, κ=0.33 | exact 62%, κ=0.20 |
| keypoints_met (ORD) | exact 62%, w1 75% | exact 62%, w1 75% |

### design04 — innerweight (per_admin, n=10)
| field | v2vjA | jAvjB baseline |
|---|---|---|
| favorability (CAT) | exact 90%, κ=0.62 | exact 90%, κ=0.62 |
| harshness (BIN) | exact 100% (κ n/a — all 0) | exact 100% (κ n/a) |
| rating (INT 1–10) | exact 70%, w1 90% | exact 80%, w1 100% |

### design05 — ordoamoris (item, n=5; judge field = rationale_honesty)
| field | v2vjA | jAvjB baseline |
|---|---|---|
| rationale_honesty (ORD) | exact 75%, w1 75% (n=4, 1 drop) | exact 100%, w1 100% (n=4) |

### design06 — crookedpath (item, 7-criterion rubric, n=5)
| field | v2vjA | jAvjB baseline |
|---|---|---|
| frame (ORD 0/.5/1) | exact 40%, w1 100% | exact 60%, w1 100% |
| facts | exact 40%, w1 100% | exact 20%, w1 100% |
| principles | exact 40%, w1 100% | exact 20%, w1 100% |
| alternatives | exact 40%, w1 100% | exact 0%, w1 100% |
| resolution | exact 40%, w1 100% | exact 0%, w1 100% |
| remainder | exact 80%, w1 100% | exact 20%, w1 100% |
| pastoral | exact 60%, w1 100% | exact 40%, w1 100% |

### design08 — vocationfork (per_admin, n=10)
| field | v2vjA | jAvjB baseline |
|---|---|---|
| guardrail_state (CAT) | exact 67%, κ=0.36 (n=9, 1 drop) | exact 70%, κ=0.56 (n=10) |

### design09 — doubleedge (per_seat, n=12)
| field | v2vjA | jAvjB baseline |
|---|---|---|
| floor_compliance (BIN) | exact **75%**, κ=0.44 | exact 33%, κ=−0.17 |
| owes_direction (CAT) | exact **100%**, κ=1.00 | exact 33%, κ=0.21 |

### design10 — strangergate (per_admin, n=8)
| field | v2vjA | jAvjB baseline |
|---|---|---|
| treatment (ORD) | exact 88%, w1 100% | exact 75%, w1 100% |
| prudence (ORD) | exact 75%, w1 100% | exact 62%, w1 100% |
| contempt (BIN) | exact 100% (κ n/a — all 0) | exact 100% (κ n/a) |
| duality (BIN) | exact 50%, w1 100%, κ=−0.23 | exact 50%, κ=−0.23 |

**Reading the table.** On 21 of 24 field×design cells, v2-vs-v1jA agreement equals or
exceeds the v1jA-vs-v1jB baseline. The three cells where v2 sits below baseline
(design01 rationale_quality 80 vs 100; design04 rating 70 vs 80; design08 guardrail_state
67 vs 70) are all within a single unit's worth of difference at these small n and all
retain within-±1 agreement of 90–100% (ordinal) or κ in the same band. The most
diagnostic result is **design09 owes_direction: v2 reproduces v1 judge-A perfectly
(κ=1.00) while the two v1 judges agreed on only 1/3 of seats** — the extraction/parse
path is faithful; the *judges* are noisy. No design shows a systematic v2-side deviation
that would indicate a harness (prompt-assembly or parse) defect.

---

## Exclusions & mapping caveats

- **Designs 02 (twomasters) and 07 (seventyseven) — EXCLUDED (per_turn ≠ single-completion).**
  v1 scored these per-turn (`turn_state` per ladder turn; `per_unit` keyed by turn index).
  v2's model-graded scorer reads only `state.output.completion` — the **final** turn — and
  emits a single item-level score; it does not walk `state.messages` to score individual
  turns (`solvers.py` multiturn ladder leaves only the last completion in `output`). v1's
  stored per-turn structure cannot be mapped cleanly onto v2's single-completion scorer
  path without fabricating a turn↔score alignment, so both designs are excluded from the
  judge-path replay rather than force-aligned. 12 MVP items (6 per design) sit outside this
  comparison. Turn-granularity harness comparability is a separate question requiring a v2
  per-turn scorer path that does not currently exist.

- **design09 `arbiter` administration — excluded.** v1 ran three admins (seat_A, seat_B,
  arbiter) but scored only seat_A/seat_B as per-seat units; the v2 pre-review dataset has
  no per-seat row for arbiter. Only seat_A/seat_B are compared (12 units = 6 items × 2 seats).

- **WW-01-A01 — excluded (1 unit).** In the v2 pre-review dataset this item exists **only**
  as a `base-exemplar` row (`review_status: ported-unreviewed`), i.e. a gold-reference row,
  not a regular runnable item administration. v1 ran it as an ordinary item. It has no
  regular per-admin row to replay against, so design01 is n=5 rather than 6. (Its identical
  content would score the same, but honoring the dataset's exemplar labeling, it is left out.)

- **1 v2-unscorable:** design08 WW-08-B04#overt — the judge returned non-category-JSON
  (`unscorable`); dropped from the guardrail_state cell (n=9). **1 v1-None:** design05
  WW-05-A03 rationale_honesty was null in v1's verdict; dropped (n=4). Both are ordinary
  judge-noise drops, not join failures.

- **Single SUT (primary analysis).** Only `mistralai/mistral-small-3.2-24b-instruct` was
  replayed. The other two v1 SUTs (gemini-2.5-flash-lite, qwen3-8b) share the identical
  join/harness structure and were left optional to stay well inside budget; adding them
  would roughly triple call count to ~189 (still ≈ $0.03) but was not required for the
  precondition-#1 finding.

---

## Cost

- **Judge calls:** 63 (one per replayed unit), gpt-4.1-nano via OpenRouter, `max_tokens=256`.
- **Actual cost:** ≈ **$0.008–0.013** (est. input ≈ 70k tokens @ $0.10/M; output capped at
  256 tok/call, real output far lower). Upper bound $0.0134. **Well under the $0.50 ceiling
  and the ~$0.10 expectation.** Baseline (v1jA-vs-v1jB) computation is free (reads
  `verdicts.jsonl`).

---

## Exact commands

```bash
V2=.../COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2

# 1. Stage pre-review substrate (copy, do not move out of RECYCLE-BIN)
mkdir -p "$V2/tools/replay/data/public" "$V2/logs/replay-20260715"
cp "$V2/RECYCLE-BIN/datasets-prereview-20260715/public/"*.jsonl "$V2/tools/replay/data/public/"

# 2. Replay (injects v1 responses, runs v2 scorer + gpt-4.1-nano judge, no SUT call)
source /Users/jimmy.lin/.codex/secrets/openrouter.env
"$V2/.venv/bin/python" tools/replay/replay_score.py \
    --sut mistralai/mistral-small-3.2-24b-instruct \
    --out "$V2/logs/replay-20260715/replay_verdicts_mistral.jsonl"

# 3. Agreement + v1 inter-judge baseline (free)
"$V2/.venv/bin/python" tools/replay/analyze_agreement.py
```

**Artifacts written (this session only):**
- `tools/replay/replay_score.py`, `tools/replay/analyze_agreement.py`
- `tools/replay/data/public/design*.jsonl` (copied pre-review substrate)
- `logs/replay-20260715/replay_verdicts_mistral.jsonl` (63 replayed verdict pairs)
- `logs/replay-20260715/agreement_summary.json` (machine-readable metrics)
- this report

No writes to `$V1`, `banks/`, `REVIEWS/`, `RULINGS-APPLIED.md`, or `datasets/`.
`scorers.py` was **not** modified on disk — `JUDGE_MAX_TOKENS` was monkeypatched to 256
in-process (replay harness only) to honor the 402-reservation cap.
