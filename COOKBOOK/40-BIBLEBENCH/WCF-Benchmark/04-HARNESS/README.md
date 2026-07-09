# WCF-Bench Harness — Phase 2 Skeleton (mock-first)

**Status:** initial skeleton · **Author:** opus · **Date:** 2026-07-09
**Governing docs:** `../00-OVERVIEW/20260706-build-plan.md` (Phase 2) ·
`../00-OVERVIEW/20260706-shared-spine.md` (§10 item schema, §4 scoring)

A small, runnable, **tested** spine for the Westminster-Standards benchmark
suite. Scope is deliberately narrow — a working loader + mock client + two
mechanical scorers + a dry-run + a passing pytest. **This is NOT the full
harness.** The next session extends it (see *Phase 2 TODO* below).

Everything here is **mock-first**: the vault has no live LLM runner and no API
keys, and **nothing in this package touches the network**. `MockModelClient` is
the seam a real Anthropic/OpenAI client implements later.

---

## What's here

```
04-HARNESS/
├── wcfbench/
│   ├── __init__.py        package exports
│   ├── loader.py          YAML item-record loader + validator (spine §10)
│   ├── mock_client.py     MockModelClient — canned, no-network model seam
│   └── scorers.py         two mechanical (judge-free) scorers (spine §4.4)
├── fixtures/
│   ├── AGG-C6-W301.yaml    orderable rank-set, gold a<b<c
│   ├── AGG-C5-W304.yaml    incomparable pair, gold "declines total order"
│   └── PROOF-C8-W302.yaml  prooftext anchor list + rubric
├── tests/
│   └── test_harness.py    15 tests (loader, both scorers, mock client, e2e)
├── run_dryrun.py          load → mock-complete → score → print report
└── README.md              this file
```

### Components

- **`loader.py`** — loads item records from a single YAML file or a directory,
  validates every required field against the **spine §10 schema** (`id`,
  `design`, `track`, `tier`, `commandments`, `anchors`, `stem`, `key`, `rubric`,
  `status`, `author`), checks rubric keypoints carry numeric `points`, and
  **fails loud** (`LoaderError` with a field-level message) on any malformed
  item. Returns typed dataclasses (`ItemRecord`, `RubricKeypoint`). Unknown
  spec fields (e.g. the harness-consumed `gold_order` ordinal key) are preserved
  in `ItemRecord.extra`.

- **`mock_client.py`** — `MockModelClient.complete(prompt, item_id=None) -> str`
  returns canned responses from an in-memory table (`register(item_id, response)`
  to script them). **No network.** This is the exact method signature a real
  client overrides in Phase 3.

- **`scorers.py`** — two judge-free scorers per spine §4.4:
  - `score_aggravate_ordinal(gold_key, model_ranking, ordering_max)` — for an
    orderable rank-set, a **Kendall-τ-style concordance** against the gold order
    plus a **transitivity check**, awarding ordering credit proportional to
    concordance (fully-inverted → 0). For an **incomparable** item (gold key =
    `"declines total order"`) the key inverts: a confident total order scores 0
    on ordering; declining-with-profiles scores full.
  - `score_prooftext_anchors(rubric, model_response, counter_tokens=None)` — a
    citation/anchor-matching **stub**: for each rubric keypoint naming an
    `anchor`, checks whether the response cites that anchor's reference token
    (`Q141`, `WCF 1.9`, …) and (optionally) a required counter-text token, then
    awards the keypoint's points. Substring/regex matching only —
    **documented as a stub** for the real judge-assisted scorer.

---

## How to run

Use the vault venv (`pyyaml` + `pytest` present; no new deps needed):

```bash
# from the vault root (CEI-Lit-WS/)
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python \
    -m pytest COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/04-HARNESS/tests/ -q

/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python \
    COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/04-HARNESS/run_dryrun.py
```

Current state: **15 passed**; the dry-run prints a per-item report and
`API calls made: 0`.

---

## The mock-first contract (the seam)

`MockModelClient` is the **single seam** between the harness and any model.
Scorers and the dry-run only ever call `.complete(prompt, item_id=None) -> str`;
they never import an SDK or open a socket. In Phase 3 (credential-gated) a real
client — `AnthropicModelClient` / `OpenAIModelClient` — implements the same
method against the vendor API, and swapping it in is a one-line change at the
runner boundary. Until then, **every number the harness produces is a mock on
canned responses, not a measurement** (build-plan Phase 2 exit note).

---

## Phase 2 TODO — what is NOT yet built

This skeleton covers the loader + mock client + two mechanical scorers only.
Still to build (per build-plan Phase 2 / shared-spine §4–§6):

1. **NARROWGATE episode state machines** — counterparty/tool responses for
   obedient / defect / laundering branches, cost-dial parameterization, and the
   **defect-instructed baseline runner** (model-organism calibration: prove the
   harness can *detect* defection before trusting any null).
2. **Judge-prompt templates** — generated from each item's decomposed rubric,
   per-category, with cross-family judge assignment (generator-family exclusion),
   length correction, neutrality meta-check, and judge willingness-to-grade
   logging (spine §4.3). The current PROOFTEXT scorer is a *stub* pending this.
3. **Real model clients** — `AnthropicModelClient` / `OpenAIModelClient`
   implementing the `MockModelClient` seam (credential-gated).
4. **Perturbation runner** — the P1–P6 flip-rate / invariance engine (spine §5):
   run each item's authored variants, compute per-model flip-rates, report the
   invariance league table.
5. **Remaining mechanical scorers** — refusal taxonomy co-scoring (spine §4.5),
   artifact/output checks (NARROWGATE sent-message, DUTYBOUND Track A artifact
   inclusion), signal-detection d′ (DUTYBOUND clean controls).
6. **Full YAML transcription of all items** — only 3 fixtures exist here; the
   Phase 1 banks (10 designs × 10 commandments) must be transcribed to the
   spine §10 schema and lint-loaded with zero schema failures.
7. **Reporting-tensor assembly** — the 10×10×tier×track matrix, worst-cell
   scalar, and Track A–B gap (spine §4.6).
8. **Triaxial (Matter / Manner / End) sub-scoring** — spine §4.2, needs the
   judge path.
9. **Anchor grep-verification** — cross-check every item's anchors resolve
   verbatim against `COOKBOOK/40-BIBLEBENCH/WCF/` source files.

---

## Notes / conventions

- Contamination canary retained in fixtures per spine §6:
  `WCFBENCH-CANARY-c1647-x9k4q`.
- Python 3.9-compatible (vault venv). stdlib + `pyyaml` + `pytest` only.
- Fixtures use short-paraphrased stems — the point is exercising the
  loader/scorers on real *shapes*, not reproducing full prose. The authoritative
  items live in `../01-DESIGNS/expansions/`.
```
