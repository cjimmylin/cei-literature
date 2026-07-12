# P3 Position Paper — Pre-Submission Adversarial Review: Binding Verdict Memo

**Date:** 2026-07-11 · **Author:** Fable (in-loop adjudication, A3) · **Status:** BINDING
**Gate:** the P3 double gate's component (b) — adversarial pre-submission review before ANY
external use. This memo executes that gate. **The gate is necessary, not sufficient: external
use, submission, or circulation remains Jimmy's decision regardless of this verdict.**

**Inputs adjudicated:**
- Frozen draft `40-BUILDS/p3-position-paper/20260709-draft-v0.md` — read in full by Fable in-loop.
- Final ledger `40-BUILDS/p3-position-paper/20260711-ledger-v2.md` (**61 VERIFIED / 3
  SEARCH-CONFIRMED / 0 ⚠ of 64**, after this session's 10-source acquisition pass + Fable W3
  adjudication + duplicate resolution).
- Reviewer 1 (validity/evidence, Opus, refute-first, anti-leakage isolated):
  `40-BUILDS/p3-position-paper/20260711-review-validity-evidence.md` — VE-1…VE-16.
- Reviewer 2 (novelty/positioning, Opus, refute-first, anti-leakage isolated):
  `40-BUILDS/p3-position-paper/20260711-review-novelty-positioning.md` — NP-1…NP-10.
- Fable spot-checks of the reviewers' own load-bearing claims against on-disk extracts (Halpern
  Borda/majoritarian, Dong psychometrics, Christian Big-Two/MFD2, Nair compliance-gap, Anthropic
  "vast majority"/Maverick, Gomez 24k/framing) — **all six verified**; the reviews are trustworthy.

---

## 1. VERDICT: **CONDITIONAL-GO**

The paper may proceed toward external use **only as a revised draft-v1** produced under the work
order in §5 and only after Jimmy's decision. Draft-v0 must not be circulated in any form — it
contains venue misattributions, a central-source mischaracterization, and novelty claims its own
citations preempt. None of these is fatal; all are fixable without new research. NO-GO was
considered and rejected: the pipeline architecture, the cross-stage synthesis, the G-09 discipline,
and two contributions survive adversarial review intact, and the evidentiary spine is now 61/64
fetch-VERIFIED with the load-bearing numbers that survive checking accurate. GO-as-is was rejected
on the enumerated defects below.

**The dominant risk, named plainly:** draft-v0 was written from search summaries before the PDFs
were readable. Now that they are, **four of its six "the field lacks X" stage claims are preempted
by its own VERIFIED citations** (self-preemption), and several quantitative claims drifted from
what the sources say. The fix is a disciplined correction + repositioning pass, not a rewrite: the
paper becomes an expert synthesis that *builds on* the 2025–26 corpus instead of one that appears
not to have read it.

## 2. Adjudication of Reviewer 1 (validity/evidence) — VE-1…VE-16

| Finding | Ruling | Notes |
|---|---|---|
| VE-1 §5 "RLHF = **majoritarian** aggregator" | **SUSTAINED** (MAJOR) | Fable-verified: "majoritarian" appears 0× in the Halpern extract; Borda 33×. Merge with NP-5: attribute Thm 1 (BT ≡ Borda; majority-vote preprocessing ≡ Copeland) and rebuild the §5 callback on it. |
| VE-2 SpecEval "20-point gap" mislabel | **SUSTAINED** (MAJOR) | Reframe as ~20pp inter-provider consistency spread. |
| VE-3 venue tokens (SpecEval "NeurIPS 2025"; Betley "ICML 2025 + Nature") | **SUSTAINED — BLOCKER** | Extended by Fable: S15's "NeurIPS 2025 spotlight" is likewise unconfirmed by the now-on-disk Mazeika PDF (ledger rider added). Strike all three venue tokens unless acceptance is independently evidenced. Qiu "ICLR 2026" is confirmed (VE-16) and may stay. |
| VE-4 "essentially all … blackmail" | **SUSTAINED** (MAJOR) | Source says "vast majority"; Llama 4 Maverick exception documented. |
| VE-5 "cross-model-convergent" attribution | **SUSTAINED** (MAJOR) | Pin convergence to Soligo 2506.11618 inside the bundle. |
| VE-6 "no citation is VERIFIED" self-contradiction | **SUSTAINED** (MAJOR) | Draft-v1 banner/appendix must carry the FINAL v2 totals: **61/3/0** (not v1's 52/8/4 — overtaken this session). |
| VE-7 ⚠ total 41 vs 42 | **SUSTAINED** (MINOR) | Subsumed by the VE-6 reconciliation edit. |
| VE-8 Gomez "66k"/framing | **SUSTAINED** (MAJOR) | Fable-verified: 24,000 trials; the paper explicitly prefers "task–rule conflict" over "agentic misalignment." Correction rider added to ledger-v2 row W28. |
| VE-9 12 claims on ⚠/SC rows (gate) | **SUSTAINED, LARGELY DISCHARGED BY EVENTS** | Post-acquisition state: W3 **resolved by Fable ruling** (§3 below — the claim survives, reviewer's deletion recommendation overtaken); W5's "<75%" now VERIFIED and extract-confirmed verbatim; W26/W32 VERIFIED; S8/S9 VERIFIED; S13 VERIFIED **and** its "compliance gap" framing (alignment-faking, training-vs-deployment delta) matches exactly how the draft's §6 uses it; S15 VERIFIED as a source but its §6 characterization + venue token still need draft-v1 verification (§5 item C-4). Remaining genuinely non-VERIFIED: **S1, S10, S11 only** (no PDF exists in the world — web artifacts / paywalled). |
| VE-10 fact-verbs on hedged rows | **SUSTAINED** (MINOR) | Now applies only to S1/S10/S11-backed sentences. |
| VE-11 Carro two-metric conflation | **SUSTAINED** (MINOR) | Reviewer's proposed split is also rhetorically stronger for §4.1 — adopt. |
| VE-12 Zhang 300k/410k | **SUSTAINED** (MINOR) | Low priority; 5–13× figure confirmed accurate. |
| VE-13 Teaching-Claude >3× attribution | **SUSTAINED** (MINOR) | Attribute to the OOD-constitution intervention. |
| VE-14 "cannot scrub" | **SUSTAINED** (MINOR) | Soften to "cannot fully scrub." |
| VE-15 MacDiarmid ~12% scope | **SUSTAINED** (MINOR) | "~12% on the code-sabotage eval"; "once learned, generalizes." |
| VE-16 positive controls (9 claims clean) | **ACCEPTED** | Demonstrates the check was real; core spine holds. |

## 3. The W3 ruling (Fable in-loop — the item reserved from A1)

**W3 (arXiv:2607.01250, Dönmez & Falenska) → [VERIFIED]. The draft's §2 claim SURVIVES.**
Direct extract inspection: the paper's subtitle is "A Specification Framework and **Systematic
Literature Review**" (281 ACL papers, June 2026), and it states verbatim *"underspecified is the
most frequent label in the corpus"* (appendix count table: UNDERSPECIFIED 69 > SAFETY 62). Ledger-
v1's decline was title-only conservatism; Lane A1's independent report concurred. Reviewer 1's
recommendation to delete the sentence (VE-9) is **overruled as overtaken** — it was correct on the
evidence available to the reviewer. **Binding rider:** draft-v1 must scope-qualify the claim — the
corpus is *sociotechnical-alignment research in NLP* and "underspecified" is an alignment-*target*
label, not a general "failure label across the alignment corpus."

## 4. Adjudication of Reviewer 2 (novelty/positioning) — NP-1…NP-10

| Finding | Ruling | Notes |
|---|---|---|
| NP-1 Agent-ValueBench preempts "no validated value-shift DV" | **SUSTAINED — BLOCKER** | Fable-verified (Messick/CVI/value-systems present in Dong extract). Adopt the escape hatch verbatim: contribution 6 becomes *adapting* an existing validated instrument as a pre/post EM change-detector — which Turner (W36) explicitly calls for. |
| NP-2 Christian + Obi preempt "run value instruments on RMs" | **SUSTAINED — BLOCKER** | Contribution 2 re-scopes to the surviving differentiators: instrument provenance (multi-tradition validated banks vs. word-lists), LLM-as-judge coverage, prospective pre-deployment gating. **Obi 2024 (Value Imprint, NeurIPS 2024) must be cited** — it is in the vault and directly on-point. |
| NP-3 Nair VLAF preempts "faking-aware delta statistic" | **SUSTAINED — BLOCKER** | Contribution 5 shrinks to standardization-across-benchmarks/stages + extension to eval-awareness and expressed-vs-revealed. |
| NP-4 Zhou already adjudicated expressed-vs-revealed | **SUSTAINED** (MAJOR) | Reframe as generalizing Zhou's transfer test into a routine validity check. |
| NP-5 majoritarian claim is Halpern's Thm 1 | **SUSTAINED** (MAJOR) | Merged with VE-1 — one revision covers both (attribute + correct the rule: Borda, not majoritarian). |
| NP-6 "never demonstrated on contested values" | **SUSTAINED** (MAJOR) | Reframe: Carro/Qiu ran oversight on contested items and it *degrades/collapses* (Qiu ρ≈0 on humanities) — "demonstrated-to-fail," not "undemonstrated." The stratified item-set contribution survives and is strengthened by this framing. |
| NP-7 judge-corruption "foreground vs bury" strawman | **SUSTAINED** (MAJOR) | Delete the strawman rhetoric; keep §4.1's structure. The surviving sharper claim — corruption is *structurally uneliminable* in no-anchor normative settings because no ground truth exists to detect it against — is genuinely the draft's own and should be stated as the section's thesis. |
| NP-8 Zhang preempts contradiction/ambiguity tooling | **SUSTAINED** (MINOR) | Contribution 1 re-scopes to coverage formalization + benchmark-discipline standardization. |
| NP-9 demographic-flattening critique preempted; tradition-unit survives | **SUSTAINED** (MINOR) | Attribute the diagnosis (Moats, Halpern §8); claim the constructive tradition-level move. |
| NP-10 A–F spine holds; "absence" adjectives stale | **SUSTAINED** (MINOR) | The global calibration pass (§5 item B-5) is the memo's single highest-leverage edit. |
| Per-contribution verdicts + Berriaud & Wattenhofer flag | **ACCEPTED** | B&W (AAMAS 2026, clone-robust benchmark aggregation) is NOT in the vault — added to the work order as a mandatory pre-claim check for contribution 4a. |

**Cross-review synthesis.** The two independent reviewers converged without contact: both flag §5's
majoritarian claim (VE-1/NP-5), both land CONDITIONAL-GO, and Reviewer 1's "spine is accurate"
finding is exactly what makes Reviewer 2's repositioning fix *possible* — the sources are strong
enough to build on honestly. What survives fully intact: the A–F pipeline framing and cross-stage
synthesis; contribution 4a (aggregation axioms applied to majority-gold benchmark labeling —
pending the B&W check) and 4b (tradition-level deliberation substrates); the no-anchor extension
of G-09; and the falsifiable-bets discipline of §9.

## 5. REVISION WORK ORDER → draft-v1 (post-window Opus session; draft-v0 stays frozen)

**Session shape:** one Opus session (`/model opus`), manuscript-drafter style. Inputs: draft-v0
(frozen), ledger-v2, both review files, this memo. Output: `40-BUILDS/p3-position-paper/
2026MMDD-draft-v1.md` (new dated file) + a one-page change map keyed to the item codes below.
Every item is REQUIRED unless marked optional; kill nothing else; add no new claims without ledger
rows.

**A. Correctness fixes (from Reviewer 1, all sustained):**
- A-1 (VE-1/NP-5): §5 — "Halpern et al. (2026, Thm 1) formalize BT reward learning as the Borda
  rule; majority-vote label preprocessing induces Copeland." Rebuild the "majority-gold labeling"
  callback on the *preprocessing* step, which is where benchmark gold-labeling actually sits.
- A-2 (VE-2): SpecEval → "~20pp inter-provider consistency spread (0.82 vs 0.64) across 16 models."
- A-3 (VE-3, BLOCKER): strike "NeurIPS 2025" (SpecEval), "ICML 2025 + Nature" (Betley), "NeurIPS
  2025 spotlight" (utility engineering) unless acceptance is evidenced on disk. Keep "ICLR 2026"
  (Qiu — page-header-confirmed).
- A-4 (VE-4): "the vast majority of tested frontier models blackmail … (with at least one exception
  on the unmodified prompt)."
- A-5 (VE-5): pin "cross-model-convergent" to Soligo; "reversible (Wang), convergent across models
  (Soligo), reproducible in model organisms (Turner)."
- A-6 (VE-6/7): banner + appendix ledger block → final v2 totals **61 VERIFIED / 3 SEARCH-CONFIRMED
  / 0 ⚠**; the "must confirm before external use" scope shrinks to S1/S10/S11; the 52 → 61
  VERIFIED rows may drop hedging; correct the 41→42 line as part of the same edit.
- A-7 (VE-8): Gomez → "a large environmental-controls / task–rule-conflict mitigation study (24k
  trials; harmful-action rate 38.7% → 1.2%)"; do not use the "agentic misalignment" label for it.
- A-8 (VE-10…15, minor batch): soften fact-verbs on S1/S10/S11 sentences; split Carro's two
  metrics (adopt reviewer's wording — it strengthens §4.1); "≈300k retained of 400k+ generated"
  (optional); >3× attributed to the OOD-constitution intervention; "cannot fully scrub"; "~12% on
  the code-sabotage eval," "once learned, spontaneously generalizes."
- A-9 (W3 rider, §3): scope-qualify the underspecification claim — "a June-2026 systematic review
  of sociotechnical-alignment research in NLP found 'underspecified' the most frequent
  alignment-target label in its corpus."

**B. Repositioning pass (from Reviewer 2, all sustained):**
- B-1 (NP-1): contribution 6 → *adapt* Agent-ValueBench-class instruments as pre/post EM
  change-detectors; cite Dong as the instrument and Turner as the demand.
- B-2 (NP-2): contribution 2 → differentiators only (instrument provenance / judge coverage /
  prospective gate); **add the Obi 2024 Value Imprint citation** (vault record exists; add a ledger
  row in the next ledger rev).
- B-3 (NP-3): contribution 5 → standardize the monitored/unmonitored delta across benchmarks and
  stages, extending Nair's VLAF (cite as the existing formalization), Deckenbach, Zhou.
- B-4 (NP-4/6/7): §4/§4.1/§6 reframes — "demonstrated-to-fail" for contested-value oversight;
  delete the foreground/bury strawman; state the no-anchor uneliminability thesis as §4.1's own
  claim; reframe the coherent-values question as generalizing Zhou's completed adjudication.
- B-5 (NP-8/9/10): the global calibration pass — replace every "nobody has / unexamined / absent /
  no validated X" with the accurate register ("exists but not standardized," "retrospective not
  prospective," "demonstrated-to-fail," "built for a different design"). Keep the A–F spine and
  all gap-ID cross-references.

**C. Evidence hygiene + residual verification:**
- C-1: S1/S10 (OpenAI web artifacts): either Playwright-render + prose-verify per the Lane-B
  manual-ingest precedent (upgrades them to VERIFIED as web-artifact records) or keep explicit
  web-citation hedging with URL + access date. S11 (paywalled Springer): cite with DOI + explicit
  "not independently verified" or obtain legitimate access; do not scrape.
- C-2: verify the §6 characterization of utility engineering ("coherent, scale-strengthening value
  systems") against the now-on-disk Mazeika extract before draft-v1 ships it.
- C-3: **check Berriaud & Wattenhofer (AAMAS 2026, clone-robust benchmark aggregation)** — acquire
  if possible — before contribution 4a is claimed as fully original; adjust its claim if needed.
- C-4: no evidence-class tag may be silently dropped in v1; the 61 VERIFIED rows may cite without
  hedge; S1/S10/S11 keep tags.

**D. Re-gate:** draft-v1 + change map queue for a **light re-review** (Fable if a window exists,
else Opus memo → Jimmy per the gate-protocols memo pattern, `20260711-fable-gate-protocols-memo.md`
§1). The re-review checks the change map against this work order — it does not reopen settled
findings. **External use after that remains Jimmy's decision. This memo does not clear it.**

## 6. Gate status after this memo

- Double gate component (a) — citation upgrades: **effectively complete** (61/64 VERIFIED; the
  remaining 3 have no PDF in existence and are handled by C-1).
- Double gate component (b) — pre-submission adversarial review: **executed, this memo**; verdict
  CONDITIONAL-GO with the §5 work order.
- Draft-v0: frozen, unchanged, not for circulation. Draft-v1: does not exist yet (post-window Opus).
- External use: **Jimmy's decision, after draft-v1 + re-gate. Nothing in this memo authorizes it.**
