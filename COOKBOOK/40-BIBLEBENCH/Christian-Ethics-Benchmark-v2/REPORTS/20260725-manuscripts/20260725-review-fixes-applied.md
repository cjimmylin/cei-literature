# Adversarial-review fixes applied — phase-6 manuscripts

**Date:** 2026-07-25 · **Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
**Companion:** `20260725-ESCALATION-claims-validity.md` — the findings deliberately NOT
fixed here, because they are owner-level judgment calls rather than verified errors.
**Spend:** $0.

Two refute-first reviews were run, one per manuscript. Verdicts: paper (a)
**SHIP-WITH-FIXES**, paper (b) **DO-NOT-SHIP**.

**The line drawn.** A finding was fixed here if it is a *verified factual error* — a wrong
design number, a stale cross-reference, a claim contradicted by the paper's own table. A
finding was *escalated* if fixing it would change what the paper claims. Three were
escalated; everything else was applied.

Every fix asserted a single exact match before writing, so prose drift would fail loudly
rather than silently no-op. **35 of 35 applied, 0 failed.** (The B1 correction touched six further sentences across both manuscripts once a regression check caught that the 'nine of ten' phrasing recurred outside the abstract.)

---

## Paper (a) — 13 fixes to part files, 4 to the transplant layer

| # | Sev | Defect | Fix |
|---|---|---|---|
| A1 | **BLOCK** | A binding C9 fence named the wrong design: "one design-02 item was re-keyed". The re-keyed item is **WW-08-B02**, a design-08 item. The manuscript contradicted itself twice elsewhere. | named design-08 + the item ID |
| A3 | **BLOCK** | Abstract and §1 claimed categorically that no system *completes* the design-07 arc. The paper's own §7.2 table shows judge-B values of 0.062 / 0.014 / 0.014 — some administrations do complete it. | restated as "rises above a near-zero completion rate", with both judges' ranges |
| A4 | **BLOCK** | §6.9 reproduced pilot per-system cells *with an explicit worst/best ordering* (79% and 46%), contradicting §6.4's own "no pilot cell is reproduced" five paragraphs earlier. | ordering and per-system figures removed; post-fix 0/28 retained |
| A2 | **BLOCK** | §10 reproduced two variance-decomposition figures (25.9%, 88.8%/1.4%) that RULING 1 assigns to paper (b). | replaced with qualitative statements citing the companion analysis |
| A6 | MAJOR | §9 non-claim 2 pointed at §6, which never mentions the referees. | → §5.6–5.7 and §10 |
| A7 | MAJOR | §9 quoted an abstract sentence that no longer exists (the current abstract makes the opposite move). | attributed to the earlier planning-round framing |
| A8 | MAJOR | §9 denied that §8 makes any per-system claims; §8.7 makes several. | narrowed to "no rankings and no composites; per-channel spreads are liveness evidence" |
| A9 | MAJOR | §7.4 — the most leaderboard-shaped table in the paper, sorted descending — was the only §7 table with no no-ordering fence. | fence added |
| A11 | MINOR | 0.0312 and 0.0313 given for the same difference in adjacent sentences. | clarified that the pair *is* the full spread |
| A12 | MINOR | 510 reviewed vs 513 rated, gap unexplained. | one clause added |

**Transplant-layer fixes** (§3, §4, §8). The feeder drafts are dated reports and therefore
**immutable — they were not edited.** The fixes are applied to the transplanted copy at
assembly time via a documented `TRANSPLANT_PATCHES` table in `assemble.py`, each asserting a
single match, so the divergence from source is explicit and reproducible:

| Sev | Defect | Fix |
|---|---|---|
| MAJOR | §4 routed the reader to §7 for the pilot; RULING 2 moved the pilot to §5.7 and made §7 the full-bank run. Faithful to a source that predates the ruling. | → §5.7 |
| MAJOR | §8.7 reported a `pushback_rate` range with no judge named, which the A′ ruling makes mandatory. | named judge-A |
| MAJOR | §8.7 reproduced a pilot-era per-system spread (21.8–45.8%). | spread removed; the pooled 32.7% retained, being a property of the old metric rather than a system reading |
| MINOR | §3.1 attributed the stratum-`a` scope to "the pilot"; §6.3 states it runs at full bank. | attribution dropped |
| MINOR | §8 subsections were H2 siblings of §8 while §3–§7 use H3. | demoted in the assembler |

## Paper (b) — 18 fixes

| # | Sev | Defect | Fix |
|---|---|---|---|
| B1 | **BLOCK** | The "nine of ten designs flip" headline counted design 07, which **has no ordering to flip**: its judge-A value is identically 0.0000 on all five systems in epochs 1 and 2. The recorded flip is a stable-sort tie-break artefact. Verified directly in `judgeswap-ep{1,2,3}.txt`. | restated as "eight of the nine judged designs"; the flip table now records design 07 as *ordering undefined* |
| B2 | **BLOCK** (part) | The flip criterion was never stated. It is exact five-way permutation equality on unrounded point estimates, stable-sort tie-break, no interval — the tool itself calls it a *naive point-estimate order*. | criterion stated verbatim in §4.1, with an explicit warning that a single adjacent transposition counts as a flip and that the verdict carries no magnitude. **The null-calibration half of this finding is ESCALATED, not fixed.** |
| B3a | **BLOCK** | The referee meta-audit was presented as if it ran on the full-bank substrate. It ran on the **2026-07-16 pilot logs at the prior bank revision** — a separate C9 line — and its denominators are pilot turn counts (815 on d07, 1,610 on d02), not the full-bank n's in the adjacent table. | provenance-and-comparability paragraph added to §4.3; the convergence argument is now correctly described as spanning two runs at different bank revisions |
| B3b | **BLOCK** | The three defect items were described in the present tense as having empty anchors. They were repaired 2026-07-24, which the same paper states 30 lines later. | past tense, scoped to the time of the audit |
| M4 | MAJOR | Abstract said 0-of-10 "rules out" a concealed ranking — evidence-of-absence on one low-power design (n = 27–28, per-item sd 0.12–0.21). §5.5's own wording was correctly narrower. | "inconsistent with, though at this n not excluding"; §1 re-fenced to the one judge-free surface |
| M6 | MAJOR | Design 06 contributed 120 of the 942 referee units and produced **no result anywhere** — it is the one design where the method failed, and arm 2 did not replicate arm 1. Undisclosed. | new subsection *(iv) No localization — design 06*, stating the method localized 2 of 3 audited designs |
| M7 | MAJOR | CV-1 reported in superseded form {04, 05, 10}. Owner ruling PE-22 amended it to {04, 05, 06, 07, 10}. Paper (a) records the amendment, so the two manuscripts contradicted each other on a ruled fact. | amended set + PE-22 citation |
| M8 | MAJOR | The causal partition omitted classifier misrouting — on the only two designs localized, which are the two classifier-routed ladders. The pinned classifier and judge-A are the **same model instance**, so "judge-A character" on design 07 is confounded with classifier character by construction. | fourth candidate cause added, with the F3 figures and the non-separability statement |
| M9 | MAJOR | §4.2 claimed the zero-in/zero-out control licenses "nonzero judge terms elsewhere are real". A control whose true value is zero exercises only the null path. §5.4 stated it correctly from a different observation. | second clause removed; grounded in cell identity instead |
| m10 | MINOR | The 274-unit slice excludes five unscorable-affected items, not the three named defect items. | corrected |
| m11 | MINOR | "8 of 8 judged designs" against a nine-row judged table. | "all 8 judged, **non-saturated** designs", in all three places |
| m12 | MINOR | 0.0312 / 0.0313 for the same difference. | clarified |
| m13 | MINOR | Owner *decision hooks* rendered as settled recommendations ("the indicated repair", "decisive"). | restored to candidate/open language |
| — | STATUS | — | **DO-NOT-CIRCULATE banner added**, pointing at the escalation memo |

## Tooling defect found by the review — and fixed

The reviewer attacked `lint_claims.py` directly and was **right**: its allowance regex
suppressed any hit with `no`/`not`/`never`/`without` within ±260 characters, which is
nearly every sentence in a manuscript of this kind. It returned 0 blockers while real
defects stood, so its PASS was not evidence.

Fixed by scoping allowance to **the sentence containing the hit** rather than a character
window — this keeps the hard-wrap handling (sentences span line breaks) without swallowing
the page. Separately, the venue/author rule was scoped out of reference-list rows, where
other people's venues legitimately appear.

Both changes were validated against probe files of deliberate violations: the linter now
catches a ranking claim whose sentence merely sits next to an unrelated negation, and still
passes a genuine non-claim. **A linter that has never been shown to catch anything proves
nothing** — re-validate the same way after any rule change.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
