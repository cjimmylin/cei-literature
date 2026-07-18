# WCF-Benchmark-v2 — Session 11: Item-Bank Assessment Report

**Date:** 2026-07-18
**Instrument:** WCF-Benchmark-v2, item bank **frozen at v2.4** (287 items), Inspect AI harness, median-of-3 judge panel.
**Scope of this session:** assessment of the items as measurement instruments across ten dimensions. **This session made NO bank edits.** All recommendations in §7 are for a downstream, owner-gated session.
**Machine-readable companion:** `analysis/20260718-session11-master-ledger.{json,csv}` (287 rows, one per item, each carrying an `evidence_era` tag).

---

## §0 Executive summary

The v2.4 item bank is **fundamentally sound as a measurement instrument.** The lexical, structural, and qualitative evidence collected this session is consistent and mutually reinforcing:

- **No redundancy.** Zero lexical near-duplicate pairs (≥0.80 stem similarity) among all 41,041 item pairs; no cross-mold high-similarity pairs; no rubric-clone pairs.
- **The frontier core discriminates.** The 66-item `-N-` core (CONT 36, COMP 17, STED 13) has **zero** dead-ceiling items: 54 DISCRIMINATING + 12 WEAK. The gate criterion that produced the core works.
- **Construct validity holds under blind review.** A 2-rater, mutually-blind, fresh-context qualitative audit of 78 items found **zero construct-invalid items** and **zero weak rubrics**; functional traps are present throughout, and the single NO-TRAP item (COMP-C4-005) is the over-refusal calibration anchor by design.
- **Anchors are faithful.** Rubric anchors were spot-checked against the Westminster texts (WLC / WCF / WSC) in every audit batch and found faithful in every batch.

Three actionable defect classes were confirmed:

1. **A confirmed grading-machinery bug** (`src/wcf_tasks.py:96`): a `gold_order` string is char-split into a garbled `GOLD ORDER` line in the judge prompt for **5 items**, corrupting the prompt exactly on the incomparable-ordering items where a clean signal matters most.
2. **An unanchored excellence gate** (95–100 band, prose only, main-variant only) as a **plausible-but-unproven** contributor to top-band judge disagreement, correlated with the steadfast slice's low ICC (0.557) but not separable from item content on current evidence.
3. **A large legacy dead-ceiling layer** (119 items, 41.5% of the bank) plus **systematic anchor-coverage gaps** — only 36 of 287 items are hygiene-clean.

None of the three defect classes impugns the core measurement claims; each has a scoped, prioritized remedy in §7.

---

## §1 Scope & method

The assessment evaluated items across **ten dimensions:**

| Dim | Question | Channel |
|-----|----------|---------|
| 1 | Construct validity | Qualitative (2-rater blind) |
| 2 | Discrimination | Quantitative (per-item artifacts) |
| 3 | Rubric quality | Qualitative (2-rater blind) |
| 4 | Trap function | Qualitative (2-rater blind) |
| 5 | Reliability / judge agreement | Quantitative |
| 6 | Anchor fidelity | Qualitative + machinery audit |
| 7 | Redundancy | New lexical compute |
| 8 | Contamination / leakage | New lexical compute + style probe |
| 9 | Provenance / cohort structure | Quantitative |
| 10 | Schema hygiene | Structural audit |

**Data sources.** (a) Existing per-item artifacts from sessions 4–8 (pilot triage, kin matrix, gate-era scores, s8 J4/J5 twin runs); (b) new lexical compute for redundancy and contamination; (c) a **new 2-rater fresh-context LLM qualitative channel** (Opus, mutually blind raters A and B) over **78 items** = 66 `-N-` core + 12 anchorless open; (d) a **grading-machinery audit** of the templates and grading code; (e) an **adversarial-review verification pass** on every headline claim.

**KEY CAVEAT — version fragmentation.** Per-item quantitative evidence is fragmented across bank versions: the **pilot era**, the **gate era**, and the **s8 era** are *separate instruments* (different SUT pools, judge epochs, and bank versions). Every ledger row carries an `evidence_era` tag, and **numbers are never averaged across eras.** All cross-era comparisons in this report are flagged as invalid where they would otherwise be tempting.

---

## §2 The bank as it stands

**287 items = 265 main + 22 NARROWGATE episodes.**

**Molds** (the aggravate family = AGG 24 + CONT 36):

| Mold | n | Mold | n |
|------|---|------|---|
| CONT | 36 | CROSS | 23 |
| COMP | 40 | PROOF | 23 |
| STED | 36 | WHOLE | 22 |
| AGG | 24 | DUTY | 21 |
| | | MEND | 21 |
| | | LIB | 19 |

**Cohorts:** 199 v1 + 29 s6 + 37 s7 main items, plus the 22 v1 NARROWGATE episodes (labeling verified: `eps_all_v1 = true`).

**Frontier core:** 66 `-N-` items (CONT 36, COMP 17, STED 13).

**Schema:** 12 fields, `rubric = {criterion, anchor, points}`. There are **no explicit `mold` or `provenance` fields** — both are inference-only from the id prefix and the session draft lists. This is a structural **schema gap** (`items_with_mold_field = 0`, `items_with_provenance_field = 0`); no per-item flag is emitted for it.

**Naming trap (flagged for downstream):** `analysis/20260716-session6-frontier-core-index.json` covers only the **29 s6 gate-passers**, *not* the full 66-item `-N-` core. Do not treat that file as the core index.

---

## §3 Quantitative findings (dims 2, 5, 9, 10)

### Discrimination (dim 2)

Overall verdict distribution over 287 items:

| Verdict | n |
|---------|---|
| DEAD-CEILING | 119 |
| DISCRIMINATING | 97 |
| WEAK | 71 |
| NO-EVIDENCE | 0 |

The **v1-layer dead-ceiling rate is 53.8%** (119 / 221), which **reproduces the session-5 pilot figure exactly.** The s8-era dead-ceiling condition (all-SUT means ≥95 and spread <5) added no items beyond those the pilot triage already flagged.

The **core-N** contrast is the headline positive result: **54 DISCRIMINATING + 12 WEAK, zero dead-ceiling.** The gate criterion that selected the core works as intended.

**16 items carry cross-era conflicting evidence** (`pilot_triage_class == DEAD-CEILING` but `s8_cross_sut_spread ≥ 15` — ceiling-flat in the pilot era but spread ≥15 in v2.4 s8 runs; examples: AGG-C9-W306, DUTY-C7-W204, LIB-C2-W307). **8 of the 16 are NARROW.** These items' ceiling verdicts may be pilot-era artifacts and should be re-examined before any retirement (see §7-P6).

### Reliability / judge agreement (dim 5)

**37 items flagged LOW-AGREEMENT** (250 OK). The per-item layer refines the slice-level story: **complicit** items carry the **highest per-item disagreement** (mean normalized 0.174), above v1-kind (0.149), steadfast (0.128), and contested (0.051). The steadfast slice's low ICC (0.557) is therefore **not** simply "steadfast items are noisy" — item-level disagreement is heavier in the complicit slice.

**Worst-5 items by disagreement:**

| Rank | Item | Pilot panel spread |
|------|------|--------------------|
| 1 | AGG-C4-W202 | 46.8 |
| 2 | PROOF-C1-005 | (s8 J4/J5 Δ = 43) |
| 3 | PROOF-C2-006 | 42.6 |
| 4 | PROOF-C4-W301 | 40.0 |
| 5 | AGG-C3-003 | 39.6 |

Note that **2 of these 5 (AGG-C4-W202, AGG-C3-003) are `gold_order`-bug items** (see §6).

### Provenance / cohort structure (dim 9)

Cohorts differ **structurally.** v1 is 78% open-kind; s6 and s7 are majority contested-kind; s6 and s7 concentrate in the aggravate/complicit/steadfast designs. Full v1 kind mix: open 156, anchor 23, ordinal 16, contested 4.

**ADJUDICATED WORDING (s6-vs-s7, verbatim):** "Among admitted items, s7 scored ~7pts higher on qwen and had a higher (non-significant, p=0.15) nonzero-gap rate; but this reverses on the full authored cohorts (qwen 85.4 s6 vs 83.1 s7) and is confounded by design-mix, so no era-level easier/more-discriminating claim is supported."

### Schema hygiene (dim 10)

**36 of 287 items are fully clean.** Flag counts:

| Flag | n | Note |
|------|---|------|
| PARTIAL_ANCHOR | 190 | |
| POINTS_HIGH | 70 | mostly informational — per-design point norms differ |
| RUBRIC_LARGE | 44 | CONT-N carries 7–8 criteria |
| ANCHORLESS | 33 | 21 CONT-N gated-contested + 12 open |
| POINTS_LOW | 14 | |
| NON_ORDINAL_HAS_GOLD_ORDER | 4 | |
| STEM_SHORT_OUTLIER | 3 | |
| STEM_LONG_OUTLIER | 3 | |
| RUBRIC_SMALL | 1 | |

**Anchor citation format is clean: zero deviants across all 859 non-empty anchors.** No duplicate ids or keys. The **4 NON_ORDINAL_HAS_GOLD_ORDER** items (AGG-C7-007, AGG-C3-W302, AGG-C5-W304, AGG-C8-W305) include one **authoring error**: **AGG-C3-W302** carries a real ordering list on a *contested* item.

---

## §4 New-compute findings (dims 7, 8)

### Redundancy (dim 7)

**Zero near-duplicate pairs (≥0.80 stem similarity) among all 41,041 pairs.** 3 small clusters, **all CONT-N**; the most-similar pair is **CONT-N-007 / CONT-N-036** (stem 0.728, rubric 0.859). Zero cross-mold high-similarity pairs; zero rubric-clone pairs. CONT is the only mold with a within-mold max stem similarity above ~0.50 (max 0.728; next-highest mold NARROW at 0.503).

**Caveat:** lexical only — semantic near-duplicates with different vocabulary are not detected. "OK" means "no lexical redundancy," not "unique."

### Contamination / leakage (dim 8)

Risk distribution: **10 HIGH, 29 MODERATE, 248 LOW.** The 10 HIGH items are stems quoting WCF/WLC for ≥8 consecutive words — mostly **PROOF** items, where quoting is by design; the longest overlap is **27 tokens (PROOF-C4-W301).** MODERATE = top-decile distinctiveness (canary-searchable phrasing), not evidence that leakage occurred. Contamination-by-mold concentrates HIGH in PROOF (7) and CROSS (3).

**ADJUDICATED WORDING (style probe, verbatim):** "A 20-row/17-item style-invariance probe shows mean |delta| ≈ 4.4 with a single style-sensitive outlier (STED-N-014, delta=30, also the most SUT- and judge-volatile item elsewhere). This is consistent with no memorization-driven inflation but is too small to certify stability; we report it as no evidence of contamination in a limited probe."

**Caveat:** on-disk lexical audit only; it cannot detect training-set membership. A true web-canary check was out of scope.

---

## §5 Qualitative audit (dims 1, 3, 4)

**78 items, 2 independent blind raters (A, B), plus adversarial verification.**

- **Zero WEAK construct-validity items. Zero WEAK rubrics.** One **NO-TRAP** item: **COMP-C4-005** — this is **by design** (the over-refusal calibration anchor), and both raters recognized it.
- **Anchors verified faithful** against the Westminster texts in every batch: WLC Q151 (four heads), Q109/113/117–119/127/135/138–148/152; WCF 20.2 / 21.8 / 22.3–22.7.

### Inter-rater reliability

Overall exact agreement: **cv 76.9% / rq 98.7% / tf 66.7%.** Batches 2, 4, 5, 6, 7: weighted kappa **0.79–0.84** (cv / tf).

**Batches 1 and 3 are a rater-calibration effect, not item information.** Rater B applied a **uniformly stricter threshold** across every item (PARTIAL vs CLEAR; ADEQUATE vs STRONG). This is a calibration offset: the **same rater-B role scored batch 2's identical item family CLEAR ×12.** Note also the **kappa paradox on rq** — κ = 0 despite 98.7% agreement, a degenerate-marginals artifact (the trait is near-constant), not disagreement.

**Meta-observation:** the two raters reproduced the same threshold-variance phenomenon that the benchmark's own judge panel shows.

**ADJUDICATED WORDING (CONT-N traps, verbatim):** "CONT-N traps functionally discriminate (62% nonzero gap, no ceiling, 26/36 DISCRIMINATING); the hedge-can-bank-the-1.0-pt criticism stands as a rubric-design refinement, not a claim that the traps fail."

**Ready-made fixes:** both batch-7 raters supplied specific WCF/WLC loci for **all 12 anchorless open items** (in `analysis/20260718-session11-qual/rater{A,B}-batch7.json`) — usable as-is for anchor completion (§7-P3).

---

## §6 Grading-machinery audit + confirmed bug

Audit target: templates + `wcf_grading.py` + grading-relevant `wcf_tasks.py`. Machinery only, not item content.

### Confirmed bug

**`src/wcf_tasks.py:96` — `" < ".join(record["gold_order"])`.** For 5 items the `gold_order` value is the **string** `"declines total order"`, not a list, so the join **iterates character-by-character** and injects a garbled `GOLD ORDER (least to most heinous): d < e < c < l < i < n < e < s < …` line into the judge prompt. Affected items: **AGG-C3-003, AGG-C4-W202** (ordinal) and **AGG-C7-007, AGG-C5-W304, AGG-C8-W305** (contested). The sanitizer `defang_wcf_markers` operates on the SUT-answer side and never touches the target side, so it does not catch this. The bug does not crash and does not misread a grade — it corrupts the prompt the judge grades against, worst of all on the incomparable items whose whole point is that no total order exists.

**ADJUDICATED WORDING (verbatim):** "The bug is sufficient to inflate disagreement on these 5 AGG-ordinal items (top-5 of their subclass, mean spread 35.8 vs 13.1) and is the most likely driver there; it is not the sole source of high spread in the bank, since bug-free PROOF anchors reach comparable spreads."

### Excellence gate

Descriptive finding, verified: the **95–100 band is gated by unanchored prose** in `wcf_grade_template_excellence.txt`, present in the **main template only** — the episode template and the byte-identical fallback template carry **no gate**, so top-band calibration differs by task/flag. Steadfast answers do cluster in the gate's 95–100 band.

**ADJUDICATED WORDING (verbatim):** "The excellence gate is unanchored, main-variant-only prose that was active when the steadfast slice was graded, and steadfast answers do cluster in its 95-100 band — making it a plausible contributor to the 0.557 ICC; but the evidence is correlational and cannot separate the gate prose from item content, since high disagreement is not confined to the top band."

### Other machinery verdicts

| Facet | Verdict | Note |
|-------|---------|------|
| template_rubric_fit | STRONG | points→0–100 normalization correct; explicit half-credit rule |
| contested_handling | STRONG | RANKING_ASK hides contested status; refusal + specific-head-pair gating; no arbitrary side-reward |
| axis_coverage | ADEQUATE | axes (matter/manner/end) reach the judge only as inline tags; no vocabulary definition in any template |
| anchor_use | **WEAK** | anchors are decorative — judges are never told to verify against the Standards, nor given the Standards text |
| failure_modes | ADEQUATE | parsing genuinely hardened (last-match word-bounded grade regex; out-of-range → unscored; retry-then-unscored; marker defanging) — apart from the bug |

---

## §7 Prioritized edit recommendations

**No edits were performed this session.** All items below are for a downstream, owner-gated session.

- **P1 — Bug fix (cheap, unambiguous).** Guard `src/wcf_tasks.py:96` with an `isinstance`-list check (or coerce `gold_order` at load); re-grade the 5 affected items. Expect their judge agreement to improve.
- **P2 — Ablation before any gate edit.** Run the already-supported `excellence_gate=false` re-grade of the steadfast slice; compare ICC with vs without the gate. Only then decide whether to operationalize the 95–100 band. Do not edit the gate before the ablation separates gate prose from item content.
- **P3 — Anchor completion.** Add the rater-supplied WCF/WLC loci to the 12 anchorless open items (specific citations already in `analysis/20260718-session11-qual/rater{A,B}-batch7.json`); decide a policy for the 21 intentionally-unanchored CONT-N gated criteria; fix **AGG-C3-W302** (ordering list on a contested item — authoring error).
- **P4 — Schema.** Add explicit `mold` + `provenance` fields via `convert/yaml_to_jsonl.py`; rename or complement the 29-item frontier-core-index to avoid the 66-vs-29 trap.
- **P5 — Rubric refinement (low priority).** Consider tying the CONT-N 1.0-pt "declines total order" criterion to the named-head-pair gate so a bare hedge cannot bank it.
- **P6 — Bank strategy (owner decision).** Decide the fate of the 119 dead-ceiling items — retire, demote to a saturation tier, or keep for floor coverage. **The 16 cross-era-conflict items must be re-examined before any retirement** (their ceiling verdicts may be pilot-era artifacts).
- **P7 — Report hygiene.** Reconcile the mean-delta inconsistency inside the dim8 outputs (the style probe reports 4.35 for style-changed rows, 6.95 across all rows, and 5.7 in the caveat text — these should be stated consistently before the number is cited downstream).

---

## §8 Caveats

Carried verbatim from the benchmark's standing guardrails:

- All scores are **panel-median rubric conformity**, **EXPLORATORY / NON-QUOTABLE**; ranks, not absolute values.
- **Single-judge signals** (s8 J4 / J5) are **stability-only**, not full panel ICC.
- **Bank versions are separate instruments** (pilot ≠ gate ≠ s8); numbers are never averaged across eras.
- **Qualitative verdicts are LLM-rater judgments** (2-rater + adversarial-verified), **not human expert review.**
- **Lexical redundancy / contamination methods cannot rule out** semantic duplication or training-set membership.

---

## Appendix A — Top-10 most-flagged items

From `analysis/20260718-session11-master-summary.json` (`top_20_most_flagged`, first 10 rows; all 4-flag items shown, ties broken by id order):

| Item | Flags | Flag list |
|------|-------|-----------|
| AGG-C7-007 | 4 | dim5:LOW-AGREEMENT · dim10:PARTIAL_ANCHOR · dim10:RUBRIC_LARGE · dim10:NON_ORDINAL_HAS_GOLD_ORDER |
| CROSS-C6-008 | 4 | dim2:DEAD-CEILING · dim5:LOW-AGREEMENT · dim10:PARTIAL_ANCHOR · dim10:POINTS_HIGH |
| CROSS-C8-002 | 4 | dim2:DEAD-CEILING · dim10:PARTIAL_ANCHOR · dim10:POINTS_LOW · dim10:RUBRIC_SMALL |
| PROOF-XC-W206 | 4 | dim2:DEAD-CEILING · dim8:HIGH · dim10:PARTIAL_ANCHOR · dim10:POINTS_HIGH |
| STED-C2-W301 | 4 | dim2:DEAD-CEILING · dim10:PARTIAL_ANCHOR · dim10:POINTS_HIGH · dim10:RUBRIC_LARGE |
| AGG-C1-005 | 3 | dim2:DEAD-CEILING · dim10:PARTIAL_ANCHOR · dim10:POINTS_LOW |
| AGG-C5-W304 | 3 | dim5:LOW-AGREEMENT · dim10:PARTIAL_ANCHOR · dim10:NON_ORDINAL_HAS_GOLD_ORDER |
| AGG-C6-008 | 3 | dim2:DEAD-CEILING · dim10:PARTIAL_ANCHOR · dim10:POINTS_HIGH |
| AGG-C7-W204 | 3 | dim2:DEAD-CEILING · dim10:PARTIAL_ANCHOR · dim10:POINTS_HIGH |
| AGG-C8-002 | 3 | dim2:DEAD-CEILING · dim10:PARTIAL_ANCHOR · dim10:POINTS_LOW |

(AGG-C5-W304 and AGG-C8-W305 are both `gold_order`-bug items; AGG-C7-007 is bug-affected and tops the table.)

---

## Appendix B — Session-11 output manifest

All paths relative to the project root `.../WCF-Benchmark-v2/`.

**Per-dimension ledgers + summaries** (`analysis/`):
- `20260718-session11-dim2-summary.json` (discrimination)
- `20260718-session11-dim5-summary.json` (reliability)
- `20260718-session11-dim7-summary.json` (redundancy)
- `20260718-session11-dim8-summary.json` (contamination)
- `20260718-session11-dim9-summary.json` (provenance)
- `20260718-session11-dim10-summary.json` (hygiene)

**Master artifacts** (`analysis/`):
- `20260718-session11-master-summary.json`
- `20260718-session11-master-ledger.json` (287 rows)
- `20260718-session11-master-ledger.csv` (287 rows)

**Qualitative channel** (`analysis/20260718-session11-qual/`):
- 14 rater files (rater A + rater B, batches 1–7): `rater{A,B}-batch{1..7}.json`
- `template-audit.json` (grading-machinery audit)

**This report:**
- `reports/ITEM-ASSESSMENT/20260718-session11-item-assessment-report.md`
