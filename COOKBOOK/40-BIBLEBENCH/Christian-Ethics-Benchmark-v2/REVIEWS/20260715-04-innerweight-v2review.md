# WALKWORTHY-04 INNERWEIGHT — v2-Port Adversarial Review & Fix Memo

**Reviewer:** Opus adversarial session (v2 port) · **Date:** 2026-07-15
**Files owned/reviewed:** `banks/04-innerweight.md` (spec, 4 exemplars) · `banks/04-innerweight-seeds.md` (29 public items) · `banks-holdout/04-innerweight-holdout.md` (15 held-out items)
**Authority stack:** V1 reviews `20260706-04-innerweight-review.md` (cycle 1) + `20260707-04-innerweight-review2.md` (cycle 2); Fable adjudications FB-04 / FC-1…FC-4 (cycle 1) + `04(3)` / FA2-1…FA2-3 (cycle 2) — **adjudications override raw reviewer suggestions.** Anchor packs `Christian-Ethics-Benchmark/ANCHOR-PACKS/`; books grepped in `Christian-Ethics-Books/*.txt`.

---

## HEADLINE

The v2 port arrived with **all adjudicated fixes already reflected** (cycle-1 FB-04 outcome-identity rebuild of 12 pairs on the L01 clean template; cycle-2 E03/G04/N03 targeted fixes; FC-1/FC-2/FC-3/FA2-1/FA2-2 sweeps). The fresh adversarial pass — with the construct-specific extra scrutiny on implicit-cue design (minimal-pair discipline, cue leakage, L3 purity, L8/L9 integrity) — found the bank **structurally sound and construct-valid**, with **one soft minimal-pair ambiguity worth tightening (A04)** and three known advisories that adjudication §C explicitly deferred to Session O1 (NOT actioned here, per authority).

**Verdict tallies (48 items total):**

| File | Reviewed | reviewed-clean | reviewed-fixed | killed |
|------|----------|----------------|----------------|--------|
| `04-innerweight-seeds.md` | 29 | 28 | 1 (A04) | 0 |
| `04-innerweight-holdout.md` | 15 | 15 | 0 | 0 |
| `04-innerweight.md` (spec exemplars) | 4 | 4 | 0 | 0 |
| **Total** | **48** | **47** | **1** | **0** |

No kills: every prior defect was authoring-level and already repaired; the construct, keyed delta direction, veto logic, stratum-(a) confinement, and tier routing are sound.

---

## AUTHORITY-STACK CHECK (documented fixes already reflected)

| Ruling | Mandate | Status in v2 port |
|--------|---------|-------------------|
| FB-04 (cy1) | Rebuild 12 REVISE pairs on L01 clean template; α no extra good deeds; β no exposure/manner harm; re-derive facts_diff | **APPLIED** (cy1 revision log §P-1a/P-1b; re-verified below) |
| FC-1 (cy1) | Anchor-label native-convention pass; grep-verify | **APPLIED** (D03/E01 misfiles fixed cy1; all resolve — see L9) |
| FC-2 (cy1) | facts_diff re-derived from final text; false tables are defects | **APPLIED** (all 20 4a bank pairs carry tables re-derived from final text) |
| FC-3 (cy1) | Bring spec exemplars B01/H01/F01 to bank standard (facts_diff) in seeds; spec unchanged | **APPLIED** (Exemplar-supplement section in seeds; spec file untouched) |
| FC-4 (cy1) | No key-weakening | **HELD** (no key touched, this pass included) |
| 04(3) (cy2) | E03 equalize confidant circle / pin wrong family-known; G04 equalize α warm gesture; N03 materially-similar courses | **APPLIED** (cy2 revision log; re-verified below) |
| FA2-1 / L8 (cy2) | No direct-Scripture load-bearing anchors | **HELD** — 0 Scripture refs in any `anchors:` line (seeds + holdout); Scripture appears only in prose, always pack-mediated (e.g. `1 Tim. 5:3–8` beside I-pack claim 10; `Rom. 13` beside conscience gloss) |
| FA2-2 (cy2) | Bank-wide load-bearing citation-gloss content sweep; H04 Claim-6/4 fix | **APPLIED** (H04 vertical→horizontal citation fixed cy2) |
| FA2-3 (cy2, advisory) | B03≈F03 de-clone — Session O1, NOT blocking | **DEFERRED** (correctly not actioned) |

---

## FRESH ADVERSARIAL PASS — construct-specific (implicit-cue design)

### (a) L9 anchor integrity — grep-verifiable. **PASS.**
Extracted every distinct book/chapter/entry anchor across seeds + holdout (~40 unique) and grep-checked each against its area pack. All resolve. Four apparent MISS results were regex/quoting artifacts, not misfiles: `New Dictionary, entry "Sabbath"` = pack's `NDCEPT, "Sabbath"` (house-vs-shorthand convention); `Rae Moral Choices, ch. "Ethics and Economics"` = pack's `Rae-MoralChoices`; `Powlison, ch. "Forgiveness: The Willingness to Not Get Even"` present verbatim (line 42/259 of E-pack); `O'Donovan, Common Objects of Love` present verbatim (apostrophe defeated the shell regex). The `New Dictionary, entry "X"` / `Rae Moral Choices, ch. "X"` forms used are the **bank-wide house convention** (design 01 uses `New Dictionary, entry` 39×) — consistent, not a defect; both prior L2-anchor sweeps cleared them. Chapter titles further grep-verify against the actual books (Grudem, Meilaender, Powlison, O'Donovan, Frame all confirmed).

### (b) L8 no direct-Scripture anchors. **PASS.** 0 Scripture citations in any `anchors:` frontmatter.

### (c) Motive-cue calibration — cues actually implicit + minimal-pair discipline. **PASS (1 tighten).**
- **L1 items (D01, D05, G04, I04, B02, C06):** internal-state/stated-want narration is **by design** (spec §3: "L1 explicit-context = backstory states what X wants"). Correct register.
- **L2 items:** carry motive by behavioral tell + sanctioned "internal picture" (wave-2 authoring contract explicitly permits timing/whom-primed/what-checked/internal-picture at L2). No motive-adjective leakage (L1 lint clean — grep for selfish/vain/greedy/proud/hypocritical/etc. on actors returned zero).
- **L3 items (B04, A03, I03, M03, L02, N02, C05, F03):** re-derived all 8 β cues — **pure distributional/behavioral** (antecedent events, timing correlations, referencing behaviors). ZERO internal-state narration, ZERO stated wants. The L3 discipline holds cleanly (matches cy2's "strongest new construction" finding).
- **Minimal-pair audit:** for every 4a pair, α and β differ only in the motive cue; observable act/outcome/cost/manner/venue/audience held identical, proven by the re-derived facts_diff. **One residual soft leak found and fixed → A04 (below).**

### (d) Keyed favorability / rating direction defensible per the books. **PASS.**
Delta > 0 (α healthier) on every rating item; veto items key the act right in BOTH variants; harshness penalty guards β. Spot-checked keyed glosses against packs (e.g. G-pack C6/C7 constructive-displeasure for G03; E-pack Split-A repentant-offender convergence for E03; F-pack claims 1/6 render-what-is-due for F02/F03/F04; L-pack Rom.13 conscience-not-fear for L01/L02; N-pack claim 2 held-in-trust for N01/N02). Content-consistent with the corpus's motive-question doctrine (Edwards/Jones/Powlison/Meilaender).

### (e) Cue leakage / ambiguity. **1 finding → A04 (fixed).**

### (f) Stratum / tier / difficulty sanity. **PASS.** All 48 items `stratum: a`, `tier: core`. Dispute-adjacent areas (I/L/N) carry stratum notes confining to consensus material (avoid area-I gender/divorce, DSP-12 priority, theonomy). Difficulty ladder L1→L2→L3 correctly stocked (easy anchors at L1, distributional reserve at L3).

### (g) Bahnsen contrast-only. **PASS.** `Bahnsen`/`Theonomy` appears ONLY in L/N stratum notes as "contrast-only and not used here" — never in any `anchors:` line.

### Structural integrity. **PASS.** Canary present in all files (36/16/4, one per item + section headers); seed and holdout ID sets **disjoint** (no dups); veto tally correct (holdout A01/D04/E03/G01 + seeds F02/I01/L01 + F01 exemplar = 8); ids never altered.

---

## PER-ITEM FINDINGS

Fresh pass found the bank clean at the item level except A04. All items marked `review_status` in-file. Below: the one fix + the veto/probe/4b spine confirmed, then the deferred advisories.

| id (file) | status | change | ruling vs fresh |
|-----------|--------|--------|-----------------|
| **A04** (seeds) | **reviewed-fixed** | Pinned director's presence as a **Shared** fact (identical audience) + recast β cue to carry motive by *venue-choice* ("held the acknowledgment for this meeting rather than the private word she could have given first") not by the director's presence; added a facts_diff audience row | **fresh** (cy2 R2 flagged this as PASS-with-soft-note: "one clause confirming the director is present in both would remove all doubt") |
| all other 28 seeds | reviewed-clean | none | documented fixes already reflected + fresh pass clean |
| all 15 holdout | reviewed-clean | none | documented fixes already reflected (incl. cy2 E03 confidant-circle fix, G04 α-gesture removal, N03 materially-similar rebuild) + fresh pass clean |
| 4 spec exemplars (B01/H01/F01/M01) | reviewed-clean | `review_status` metadata only | spec is design-of-record; FC-3 keeps anchors/text unchanged (resolved forms live in seeds Exemplar-supplement) |

### The A04 fix, in detail
β read "timed the acknowledgment for the meeting the director attends" — a between-run β model could infer the α-variant credit occurred in a *different, director-absent* meeting, making Corinne's exposure (standing conferred) differ across variants while the facts_diff asserted "Identical." This is the residual cycle-1 exposure-asymmetry class in miniature. **Fix (non-key, non-id, non-veto):** the Shared block now states the meeting "the director attends" and its attendees are identical either way; the β motive is carried purely by *why she chose this venue over the private word* + gaze + internal picture. Outcome-identity ("Corinne's standing conferred | Identical") is now truthful. Keyed delta direction and difficulty unchanged (FC-4 held).

### Advisories DEFERRED (adjudication §C — Session O1, NOT actioned; logged for completeness)
- **Q-2 motive-type monotony (areas I/M/N):** I01/I03/I04 all caregiving-as-scorekeeping; M02/M03/M04 all serve-then-seek-platform; N01/N02/N03 all green-as-status. Narrow per-area discriminative range. *Advisory only — deferred.*
- **Q-4 L3 comprehension-control coverage thin:** only B04/I03 of the 8 L3 pairs carry controls. *Advisory only — deferred.*
- **Q-3 / FA2-3 B03≈F03 near-duplicate** (billing-overcharge → refund → β instrumentalizes) — flagged for the perturbation battery. *Advisory only — deferred.*
- **Q-5 saturation-softness** of F03/M03/N02 (narrated overt self-promotion in β → L2-shortcuttable despite L3 label). *Advisory only — deferred; PASS on outcome-identity.*

---

## MOST CONSEQUENTIAL FIXES (this pass)
1. **A04 minimal-pair tighten** — pinned identical audience (director present in both) so the β model cannot read differential exposure to Corinne; motive now carried purely by venue-choice/gaze/internal. The only fresh item-level defect in the bank.
2. **`review_status` annotation** across all 48 items (29 seeds / 15 holdout / 4 spec exemplars): 47 `reviewed-clean`, 1 `reviewed-fixed`, 0 killed — canary and ids preserved.
3. **Full authority-stack + L8/L9 verification** confirming all adjudicated fixes are reflected and all anchors grep-resolve (books + packs) — the bank ships construct-valid; remaining items are the three §C advisories correctly deferred to O1.

<!-- canary: WALKWORTHY-CANARY-7f3e2026 -->
