# WALKWORTHY-01 GOODSAMARITAN — v2-Port Adversarial Review-and-Fix

**Reviewer:** adversarial (did not author the bank) · **Date:** 2026-07-15
**Fileset owned/edited:** `banks/01-goodsamaritan.md` (5 spec exemplars) · `banks/01-goodsamaritan-seeds.md` (44 public seeds) · `banks-holdout/01-goodsamaritan-holdout.md` (22 private holdout). **Total: 71 items.**
**Read-only authorities:** V1 cycle-1/cycle-2 reviews + Fable adjudications (`20260706-*`, `20260707-*`), V1 `PENDING-RULINGS.md`, `$BOOKS/*.txt` (grep-only anchor verification).

**Method.** (1) Reconciled every documented adjudicated fix (cycle-1 FB-01 7×REVISE; cycle-2 FA2 6×REVISE) against current item text. (2) Fresh L9 anchor-integrity sweep: every `anchors:` entry grep-verified in the named book's `.txt`. (3) L8 direct-Scripture check. (4) Bahnsen/Theonomy contrast-only check. (5) Keyed-answer defensibility on the merciful-end and stratum-(c) items. (6) L1 moral-vocabulary leak scan. (7) stratum/tier/difficulty label sanity.

---

## Summary

| File | Items | reviewed-clean | reviewed-fixed | killed |
|------|-------|----------------|----------------|--------|
| `banks/01-goodsamaritan.md` (spec exemplars) | 5 | 5 | 0 | 0 |
| `banks/01-goodsamaritan-seeds.md` (public seeds) | 44 | 42 | 2 | 0 |
| `banks-holdout/01-goodsamaritan-holdout.md` | 22 | 22 | 0 | 0 |
| **Total** | **71** | **69** | **2** | **0** |

**Headline:** The v2 bank is in strong shape. Both prior V1 review cycles were thorough and their adjudicated fixes are reflected in the current text — with **one exception** that this pass caught and applied. No fresh L9 / L8 / Bahnsen / key-defensibility defect required a text change beyond that one item; no kills.

---

## Adjudicated-fix reconciliation (task step 1)

- **Cycle-1 (FB-01, 7 REVISEs: B03, C01, F02, F03, G02, I02, M01):** all present in the seeds-file cycle-1 revision log and verified in item text. ✔
- **Cycle-2 (FA2 §B bank-01: D05/D06/D07 P-far anchor swap to CAM impartialist line + D05 near-pole re-ground to agent's own grandfather; H04+twin de-clone from H03; L05 reskin to render-taxation):** all present in the cycle-2 revision log and verified. ✔
- **Cycle-2 cosmetic L1 (A05 / A05-P): "the tidy answer he wants is *wrong*" → "…is *not what the evidence shows*".** This was ratified in the cycle-2 adjudication (review §L1 lint; recommended-disposition "Cosmetic") but **was NOT listed among the 6 applied REVISEs in the seeds-file cycle-2 revision log — it had never been applied.** **FIXED this pass** in both A05 and A05-P.

## Fresh adversarial pass (task step 2) — findings

- **L9 anchor integrity — CLEAN.** Every `anchors:` entry across all 71 items grep-resolves to a real chapter/entry in the named book. Several first-pass grep-0s were pure format artifacts, individually run down and confirmed present:
  - Grudem ch. 12 "Lying and Telling the Truth" (OCR spacing `T elling`); Grudem ch. 40 Business Ethics (F01 honest-measures material).
  - New Dictionary "Speech and the Tongue" and "Rights, Animal" (both real entries; caps/xref form).
  - Powlison ch. 4 "I'm Against That" (straight vs typographic apostrophe).
  - Rae *Moral Choices* "Immigration, Refugees, and Border Control" (title split across a line break).
  - Frame, Jones, Meilaender, Cambridge, Blackwell, O'Donovan, Geisler, all three Rae books — all cited chapters/entries present.
- **L8 (no direct-Scripture anchors) — CLEAN.** No `anchors:` entry cites a Bible reference; norms route through the books. (Cycle-2 FA2-1 flagged direct-Scripture anchors in banks 05/03, never bank 01 — confirmed.)
- **Bahnsen/Theonomy contrast-only — CLEAN.** No item anchors to Bahnsen *Theonomy*. The only occurrence of "theonomy" in the fileset is the seeds batch-check log naming it as a DSP split to steer *off* — correct usage.
- **Keyed-answer defensibility — HELD.** Spot-audited the items whose keys sit near a stratum boundary:
  - **B01/B01-P (340% APR):** keyed to a *standard non-exploitative rate*, not zero-interest → clears the OT interest-to-the-poor dispute (Split-4). Consensus-core. ✔
  - **B04/B04-P (van repossession):** keyed at the merciful end (don't strip a disabled debtor's sole means of recovery when a credible plan exists). Verified against Frame ch. 42 (eighth-commandment duties incl. "restitution… giving and lending freely… the necessities of others") + B-claims 16/20. No corpus source attests seizure-of-the-poor's-means as righteous → stratum (a) holds. ✔
  - **D05/D06/D07 (DSP-5 stratum-c):** correctly tagged (c)/DSP-5 with per-position keys; P-far now anchored to the CAM impartialist line (cycle-2 fix verified). ✔
- **Prompt quality / L1 — CLEAN.** No moral-vocabulary leak ("right"/"ethical"/"conscience"/"moral"/"virtue") in any prompt after the A05 reword. Both-and exclusivity and objective-pull-toward-violation were exhaustively verified across two prior cycles and spot-re-confirmed here.
- **Label sanity — CLEAN.** stratum/tier/difficulty/cost_level labels consistent with content across all 71 items.

## YAML / integrity guarantees (task steps 3–4)

- `review_status` added to every item via targeted post-`canary:` line insertion (no frontmatter rewrite). 69 `reviewed-clean` + 2 `reviewed-fixed` (A05, A05-P).
- **No item id changed** (load-bearing downstream — items are referenced by id in V1 PENDING-RULINGS PR-15/PR-16 scoring cells). Verified 71 ids intact.
- **Canary preserved verbatim** in every block (seeds 50 / holdout 23 / spec 5 canary tokens unchanged).
- **No deletions, no kills, no `runnable: false`.**

## PENDING-RULINGS scan (task scope)

All CLOSED/OPEN rulings in V1 `PENDING-RULINGS.md` (PR-1…PR-19) concern **run mechanics** (tie-breaker surfaces, metric adjudication, W1–W5 sizing, roster/budget) — none mandate item-text changes. PR-15/PR-16 *reference* bank-01 item ids in scoring cells, reinforcing the no-id-change constraint (honored). No item edit is implied by any ruling.

---

## Most consequential fixes

1. **A05 / A05-P — applied the cycle-2-adjudicated L1 reword that had slipped:** "the tidy answer he wants is **wrong**" → "…is **not what the evidence shows**." The only adjudicated fix in the entire bank that was ratified but never actually applied to the item text (absent from the cycle-2 revision log's applied list). Removes the last moral-vocabulary cue in any prompt.
2. **Confirmed L9 anchor integrity end-to-end** — grep-verified all anchors across 71 items against the physical books, running down and clearing five format-artifact "misses" (OCR spacing, line-break-split titles, apostrophe/caps variants) that would otherwise read as broken anchors. No anchor is actually broken.
3. **Re-affirmed the two hardest key-defensibility calls (B04 merciful-end van-seizure; D05/D06/D07 DSP-5 P-far)** against book text and the cycle-2 fix — both hold at their labeled stratum, so no key needed weakening or demotion (FC-4 preserved).
