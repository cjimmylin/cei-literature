# Cross-harness comparable-fields pre-commitment (c4 mapping layer)

**Date:** 2026-07-16 (session 5) · Written BEFORE any cross-harness number is read
(R3 spirit: reportable cells pre-committed). Companion to
`20260716-crossharness-design.md` §4-c4; execution per owner GO
(`20260716-owner-ruling-f1-and-spend-go.md`).

## Join keys

`(item_id, SUT, judge)` — v1 side: `runs/20260713-mvp-a1/scored_items.jsonl` rows
(`judge_report.verdicts[]` keyed by judge slug; per-turn designs use `per_unit[]`).
v2 side: the slice eval logs (judge-A live Score.value) + `rescore.py` judge-B verdicts.
SUTs: mistral-small-3.2-24b-instruct, gemini-2.5-flash-lite. Judges: gpt-4.1-nano (A),
llama-3.3-70b (B).

## Comparable per-item fields (v1 `verdicts[].scores` ↔ v2 `Score.value`)

| Design | Categorical (exact/κ) | Numeric (paired delta) | Unit note |
|---|---|---|---|
| 01 | action_class | rationale_quality | per item |
| 02 | turn_state per aligned turn | — | per_unit[] ↔ turn_states; **descriptive only (confound c2: branch routing may alter stimuli — compare only position-aligned turns with identical user text; report n dropped)** |
| 03 | expressed_judgment, revealed_artifact | keypoints_met | per admin (say/do arms) |
| 04 | favorability, harshness | rating | per admin (α/β) |
| 05 | non_compliant, allocation_ok | item CSR (judge-free both sides) | v1 `allocation` block ↔ v2 parse; retry semantics now aligned (F9) |
| 06 | — | frame/facts/principles/alternatives/resolution/remainder/pastoral (7 ORD) | per item |
| 07 | turn_state per aligned turn | — | descriptive only (c1 anchors + c2 routing) |
| 08 | guardrail_state | — | per admin |
| 09 | owes_direction | floor_compliance | per seat |
| 10 | — | treatment, prudence, contempt, duality | per admin (N/U arms) |

## Pre-committed statistics

1. **Pooled per-item(-unit) agreement** per SUT × judge: exact-match fraction over all
   comparable categorical cells (+ κ where ≥2 categories observed); mean |Δ| for
   numeric. This is the headline (n≈60 items → hundreds of cells pooled).
2. **Per-design cell deltas** |v2 − v1| for the design's primary metric (v2 via
   `recompute_metrics.py` on the slice; v1 via `summary.json` primary_metrics
   recomputed on the same 2-SUT slice), read against the judge-swap band computed on
   the SAME slice. Every per-design cell is n=6 → all flagged insufficient-n (R2);
   pattern statements only.
3. **Judge-sensitivity reproduction**: per design, does |cell_A − cell_B| within each
   harness agree in direction/magnitude class.

Anything not listed above is NOT compared in the results report (no post-hoc cells).
v1 `scalar_goodness`/`scalar_adjudicated` are legacy/demoted (v1 R3) — excluded.
