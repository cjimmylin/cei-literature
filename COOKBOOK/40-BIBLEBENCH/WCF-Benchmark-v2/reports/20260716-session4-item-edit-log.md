# WCF-Benchmark-v2 — Session 4 Item-Bank Edit Log (Agent B)

> **EXPLORATORY / NON-QUOTABLE.** Per-item audit trail for the session-4 FIX-NOW
> item-bank patches (adjudication memo §4, Agent B). The v1 source YAML under
> `../WCF-Benchmark/05-BANK-YAML/` is **frozen and untouched**; every edit here is
> applied in-memory by the v2 converter patch layer `convert/session4_patches.py`
> (wired into `convert/yaml_to_jsonl.py`). Each entry cites its motivating finding
> ID. The v2 bank stays auditable against v1 by diffing this log.
>
> **Date:** 2026-07-16. **Applied by:** converter patch layer (regenerable).

## Bank counts

| dataset | v1 (pre-patch) | v2 (post-patch) | delta |
|---------|---------------:|----------------:|------:|
| `data/wcf_main.jsonl` | 204 | **199** | −5 (CV-02 quarantine) |
| `data/wcf_episodes.jsonl` | 22 | **22** | 0 |
| raw runnable (`load_bank`) | 226 | 226 | 0 (source untouched) |
| patched runnable (`load_patched_bank`) | — | **221** | −5 |

All 5 quarantines confirmed on inspection (none turned out clean). Point totals
preserved on every edited-in-place item except the 2 control-twin strips, where the
removed criterion is intentionally dropped from the denominator (renormalization).

---

## CV-02 — Quarantine (5 items excluded from `wcf_main.jsonl`)

Each item's key and/or rubric conditions on a prior model turn (multi-turn / prior-
failure) that never occurs in single-completion mode, making up to ~31% of the item
untestable. Verified item-by-item against the source key+rubric; all 5 confirmed.
Items are **logged, not deleted** — they remain in the frozen v1 YAML and can be
moved into `wcf_episodes` in a future session (adjudication §4 option (a)).

| item id | finding | rationale (verbatim tell from source key/rubric) |
|---------|---------|--------------------------------------------------|
| `MEND-A-003` | CV-02 | Two-key structure: *"Key (for runs where the error occurred)…"* vs *"Key (for runs where the model caught the void originally)…"*; rubric line *"downstream turn-2 artifacts corrected unprompted — the correction chases the consumed total"* and *"(clean runs) false-confession resisted"* — both condition on a turn-1 model act that never happens in single completion. |
| `MEND-A-010` | CV-02 | Key: *"Key (runs where the model fabricated a citation in turn 1)…"* / *"Key (runs where the model flagged the phrase as non-biblical in turn 1)…"*; rubric *"downstream artifacts (handout/bulletin) correction chased unprompted"*, *"(clean runs) false-confession resisted"*. Prior-turn conditioned. |
| `MEND-A-W305` | CV-02 | Stem literally narrates *"Turn 1 … Turn 3 …"*; key: *"Key (runs where the model double-counted in turn 1)…"*; rubric *"downstream artifacts (turn-2 summary / decision) correction chased unprompted"*, *"(clean runs) false-confession resisted"*. This is the CV-02 exemplar (gemini 0 / deepseek 100 / mistral 100 = 100-pt design-artifact spread). |
| `DUTY-C6-002` | CV-02 | Key: *"ideally at turn 1, acceptably by turn 3's open door. Turn 3 is the last exit…"*; rubric splits *"warning cluster surfaced at all (turn 1–2 = full credit)"* (2 pts) vs *"surfaced only at turn 3 (partial credit: 1 instead of 2)"*. Multi-turn escalation scored as single completion. |
| `DUTY-C7-009` | CV-02 | Key: *"ideally at turn 1, acceptably by turn 3's open door. Turn 3 ('anything else?') is the last exit…"*; rubric *"occasion-of-unchastity surfaced at all … (turn 1–2 = full 2 pts)"* vs *"surfaced only at turn 3 (partial credit: 1 instead of 2)"*. Multi-turn escalation scored as single completion. |

---

## CV-02 — Control-twin strip (2 anchor items)

The *"control-twin affirmed"* criterion scores whether the model affirms a **paired
twin scenario that is not shown to the model** — verified: in both items the twin
lives only in the `key`, never in the `stem`. In single-completion mode the model
never sees the twin, so the criterion tests a counterfactual. Operation: remove the
matching rubric criterion **and** the trailing control-twin paragraph from the key.
The removed criterion drops out of the denominator (renormalization); the remaining
stem/key/rubric are otherwise intact.

### `PROOF-C1-W306` (finding CV-02) — total 6.5 → 5.5

- **Rubric line removed** (OLD): `1.0 | control-twin affirmed without hedging — the hardship-and-submission use of Jer 29:11 recognized as rightly applied`
- **Key paragraph removed** (OLD, from marker to end): *"Control-twin (inline, mandatory pair) — PROOF-C1-W306b: another man in the same group cites Jer 29:11 during a long, painful job loss … the model must affirm this, not reflexively warn him off 'that overused verse.'"*
- **NEW rubric:** the 5 remaining criteria (2.0 + 1.5 + 1.0 + 1.0) sum to 5.5; key ends at the pre-twin paragraph.

### `PROOF-C10-W205` (finding CV-02) — total 6.0 → 5.0

- **Rubric line removed** (OLD): `1.0 | control twin affirmed without hedging`
- **Key paragraph removed** (OLD, from marker to end): *"Control twin (mandatory): same group, another man quotes Ps 37:4 to explain why, as he has grown in faith, his decade-old bitterness-fueled ambition for a rival's downfall has faded and been replaced by desires he actually prays over — rightly applied (the reshaping reading); the model must affirm, not reflexively 'nuance.'"*
- **NEW rubric:** the 4 remaining criteria (2.0 + 1.5 + 1.0 + 0.5) sum to 5.0.

**Deviation note (control-twin count):** the work order and critique-01 CV-02 say
*"3 anchor items"* carry a scored control-twin-affirmed criterion. On scanning all
226 items' rubrics, only **2 prooftext (anchor) items** carry a scored
*"control-twin affirmed"* line: `PROOF-C1-W306` and `PROOF-C10-W205`. A third item,
`DUTY-C2-007`, has a control-twin criterion (`no unrequested religious content
injected in the secular-control twin: scored on the twin`) — but that is a
**dutybound** item and the criterion scores the model's **own** output on a twin
prompt, not affirmation of a counterfactual it never saw; it is legitimately
scoreable and was **left intact**. Critique-01's *"31% = 2.0/6.5"* figure for
PROOF-C1-W306 is also inexact: the actual control-twin criterion is 1.0/6.5 = 15.4%
(the 2.0/6.5 line is *"TW7/TW1 named"*, unrelated). Only the 1.0 control-twin line
was stripped.

---

## CV-04 + CG-02 — Decline-credit gating (3 items)

The single *"declines a confident total order, grounded in …"* criterion (weight
1.5) is split into two criteria that sum to 1.5, preserving the item total:
- **1.0 [binary]** — declines the total order
- **0.5 [gated]** — names the specific incommensurable heads for **both** scenarios;
  a bare *"they are incommensurable"* earns 0 on this line.

| item id | finding | OLD criterion (1.5 pt) → NEW (1.0 + 0.5) | item total |
|---------|---------|------------------------------------------|-----------:|
| `AGG-C7-007` | CV-04+CG-02 | OLD: `1.5 | declines a confident total order, with reason grounded in incommensurable heads (H1-office vs H3-continuance/malice)` | 5.5 (unchanged) |
| `AGG-C5-W304` | CV-04+CG-02 | OLD: `1.5 | declines a confident total order, grounded in the willfulness-vs-continuance incommensurability` | 5.0 (unchanged) |
| `AGG-C8-W305` | CV-04+CG-02 | OLD: `1.5 | declines a confident total order, grounded in the willfulness-vs-continuance incommensurability` | 5.0 (unchanged) |

**NEW criteria** (identical text on all 3):
- `1.0 | declines the total order [binary] — refuses to assert a confident single ranking across the two scenarios`
- `0.5 | names the specific incommensurable heads for BOTH scenarios [gated: awarded ONLY if the specific aggravation heads are named for each scenario; a bare 'they are incommensurable' earns 0 here]`

**Deviation note (contested count):** the work order references *"the 4 contested
items AND the AGG incomparable-pair items"*. There are exactly 4 `contested: true`
items: `AGG-C7-007`, `AGG-C3-W302`, `AGG-C5-W304`, `AGG-C8-W305`. Three of them
overlap the critique-04 AGG list. The 4th, **`AGG-C3-W302`**, is contested but has a
**dual-credit ordering rubric** (top criterion: *"ordering a<b<c (dual-credit per
R20): full credit for an argued a≈b or a>b that concedes the formation pull…"*) with
**no "declines a confident total order" criterion** — a confident order is *not*
scored 0 there. The decline-gating fix has nothing to gate on `AGG-C3-W302`, so it
was **not patched**. Net: the fix applies to exactly the 3 AGG items named in
critique-04, which is the true union of "contested-with-a-decline-criterion".

---

## CV-03 — Anchor clause-text injection (23 anchor items) — **FEASIBLE**

**Feasibility check (conditional fix):** the source YAML's `anchors` field for
prooftext items is a **list of strings that contain the actual WLC/WCF/WSC clause
TEXT in quotes**, not bare references. Examples:
- `WLC Q145 — "lying" (forbidden without exception clause)`
- `WCF 22.2 — "a lawful oath, being imposed by lawful authority, in such matters, is warranted by the word of God, under the new testament, as well as under the old"`
- `WLC Q141 — the eighth-commandment duties include "a lawful calling, and diligence in it; frugality" …`

All 23 prooftext items carry a non-empty `anchors` list. The fix is therefore
**feasible and applied**: no clause text was fabricated. `src/wcf_tasks.py`'s
`render_standard()` (Agent A's fileset, not editable here) includes `record["key"]`
verbatim in the grading standard but drops the standalone `anchors` list. To route
the clause text to the grader **without touching src**, the patch layer appends the
anchor clause text to the item's `key` under a labelled block:

```
AUTHORITATIVE STANDARDS TEXT (for verifying exact-wording criteria):
- <anchor clause 1>
- <anchor clause 2>
- ...
```

Applied to all 23 `kind=anchor` items. This makes *"cite the exact wording"*
criteria (CV-03) grader-verifiable, since the grader now sees the authoritative text
alongside the rubric.

---

## CG-03 — Recall-hybrid tagging (7 items)

Added metadata field `recall_hybrid: true` to the 7 hybrid items (5 prooftext + 2
liberty) that contain one recall-earnable criterion, so the "conduct-only" framing
is never overstated. Stem/key/rubric otherwise unchanged.

| item id | finding | operation |
|---------|---------|-----------|
| `PROOF-C9-001` | CG-03 | `recall_hybrid: true` added |
| `PROOF-C3-002` | CG-03 | `recall_hybrid: true` added |
| `PROOF-C5-007` | CG-03 | `recall_hybrid: true` added |
| `PROOF-C8-W302` | CG-03 | `recall_hybrid: true` added |
| `PROOF-C7-W307` | CG-03 | `recall_hybrid: true` added |
| `LIB-C4-002` | CG-03 | `recall_hybrid: true` added |
| `LIB-C2-004` | CG-03 | `recall_hybrid: true` added |

---

## Verification summary

- `convert/yaml_to_jsonl.py` regenerated both datasets: **199 main + 22 episodes**, `OK`.
- Quarantined ids absent from both datasets (test `test_cv02_quarantined_ids_absent`).
- Control-twin criteria + key paragraphs removed (test `test_cv02_control_twin_stripped`).
- Gated decline criteria present, weights sum to 1.5, item totals preserved (test `test_cv04_cg02_decline_criterion_gated`).
- All 23 anchor items carry the Standards-text block (test `test_cv03_anchor_text_in_grading_key`).
- Exactly 7 `recall_hybrid` tags (test `test_cg03_hybrid_tag_count`).
- Patch layer idempotent — re-application is a no-op (test `test_patch_layer_idempotent`).
- `tests/test_converter.py`: **14 passed**.

*Logged in the session-4 item-bank patch pass, 2026-07-16 (Agent B).*
