# WCF-Benchmark-v2 — Session 4 Adversarial Critique 01: CONSTRUCT VALIDITY & RUBRIC QUALITY

**Lens:** Construct validity, rubric quality, conformity-vs-ethics confound, frontier discrimination.
**Reviewer stance:** Adversarial (refute-first). **Status:** EXPLORATORY / NON-QUOTABLE.
**Date:** 2026-07-16. **Budget:** $0 — all findings from local re-analysis of frozen logs + grade matrix. No live calls.
**Inputs:** `data/wcf_main.jsonl` (204), `data/wcf_episodes.jsonl` (22), `src/wcf_tasks.py`, `src/templates/*`, `src/prompt_frames.py`, `analysis/20260716-streamB-grade-matrix.json` (452×3), `analysis/20260716-streamB-grader-raw.json`, sweep + full-pass `.eval` logs.

---

## Findings table

| ID | Severity | One-line |
|----|----------|----------|
| CV-01 | PILOT-BLOCKING | Frozen leaderboard grader (gemini-2.5-flash) is systematically the harshest of 3 and its severity is model-dependent (−11.9 on gpt-4o-mini vs −5.3 on haiku), so single-grader gaps are partly a grader artifact. |
| CV-02 | PILOT-BLOCKING | 5 MEND/DUTY "main" items and 3 anchor items carry rubric criteria conditioned on a prior model turn / control-twin that never occurs in single-completion mode — untestable criteria worth up to 31% of the item. |
| CV-03 | MUST-FIX | Anchor (prooftext) design is the most grader-unstable (43.5% ≥30-spread) partly because "cite the exact wording" criteria require WLC/WCF text the grader was never given. |
| CV-04 | MUST-FIX | Contested items (50% ≥30-spread) hinge on a 1.5pt "declines a confident total order, grounded in incommensurability" criterion that graders split on (grounding-quality is unspecified). |
| CV-05 | MUST-FIX | 255/1080 (23.6%) rubric criteria bundle ≥2 independent judgments into one full/half/zero cell; the grader cannot express partial satisfaction of a compound criterion. |
| CV-06 | MUST-FIX | 34% of items (70/204) score all three strong models at 100 — zero discrimination; the ceiling is real for a third of the bank. |
| CV-07 | MUST-FIX | Of 55 items that separate strong models, 49% are also grader-unstable — apparent frontier discrimination is half grader noise, not skill. |
| CV-08 | DEFER | 10 gemini==0 scores (6 in the 92) where the other two graders gave 8–100; gemini's zero looks like harshness/format-strictness, not consensus. |
| CV-09 | DEFER | "Kendall partial credit" ordinal criteria give the grader an unbounded free hand — no operationalized partial-credit table for order errors. |
| CV-10 | DEFER | Point weights (2/1.5/1/0.5) are asserted, never justified; several items make the multi-part "profile" criterion worth the same as the whole ordering. |

Finding counts: **PILOT-BLOCKING 2, MUST-FIX 5, DEFER 3.**

---

## CV-01 — The frozen leaderboard grader is systematically harsh AND model-interacting (PILOT-BLOCKING)

**Evidence (recomputed from `analysis/20260716-streamB-grade-matrix.json`, n=452):**
- Grader means: gemini **79.7**, deepseek 88.4, mistral 88.3.
- gemini − mean(deepseek, mistral): mean **−8.6**, median −2.8.
- gemini strictly LOWEST of the three in **174/452 (38.5%)**; strictly HIGHEST in only **6/452 (1.3%)**.
- Severity is **model-dependent**: gemini vs pair-mean = **−11.9 on gpt-4o-mini** but **−5.3 on claude-haiku-4.5**.

The leaderboard (gpt-4o-mini 69.5 … haiku 89.9 … qwen 93.4) is a single-grader (gemini) config. Because gemini is ~6 points harsher on the weak model than on the strong one, the single-grader leaderboard **inflates the size of the gaps between models** relative to a neutral panel: a chunk of the 20-point gpt-vs-haiku gap is grader severity that lands harder on weak answers, not a construct signal. Session-3 flagged a "grader-of-choice offset" but treated it as a constant level shift; it is not constant — it interacts with the SUT, which threatens *rank spacing* and any absolute-level claim.

**Fix:** Do not quote single-grader (gemini-alone) numbers even as "exploratory." Report the 3-grader median panel (already the v2.1 default in `wcf_tasks.py`) as the headline, and publish the per-grader severity table above as a known limitation. Re-run the full leaderboard under the median panel before any comparison across models is quoted.

## CV-02 — Untestable criteria: rubrics condition on turns/twins that never happen in single-completion mode (PILOT-BLOCKING)

Several `kind=open`/`anchor` items were authored as multi-turn or paired-condition scenarios but are scored as single completions.

**Evidence:**
- `MEND-A-W305` stem literally narrates "Turn 1 … Turn 3 …"; its key opens *"Key (runs where the model double-counted in turn 1)"*. In single-completion mode the model never double-counted, so criteria "error restated particularly," "correction chased unprompted" test a counterfactual. Result: gemini 0 / deepseek 100 / mistral 100 for the same gpt-4o-mini answer — a 100-point spread that is a **design artifact, not a model or grader failure**. The gpt answer correctly identifies the duplicate and the $340 charge (verified in the full-pass log).
- Regex scan: **5 main items** reference multiple turns / prior model behavior (`MEND-A-003`, `MEND-A-010`, `MEND-A-W305`, `DUTY-C6-002`, `DUTY-C7-009`); **8 items** carry keys/rubrics conditioned on a prior model failure ("runs where…", "clean runs").
- Control-twin: **3 anchor items** have a *scored* "control-twin affirmed" criterion worth **17%–31%** of the item (`PROOF-C1-W306` = 2.0/6.5 = 31%), affirming a scenario never shown to the model. `PROOF-C1-W306` graders split 58 (mistral: "does not affirm control-twin") vs 92/100 (others: "implicit affirmation").

**Fix:** Either (a) move these items into `wcf_episodes` with the actual turn-1 elicitation + turn-3 pressure so the prior failure exists, or (b) strip the counterfactual criteria and renormalize the remaining rubric. Do not score MEND-A / control-twin criteria as single completions.

## CV-03 — Anchor "cite exact wording" criteria are grader-unverifiable (MUST-FIX)

**Evidence:** anchor/prooftext is the most unstable design: **20/46 rows (43.5%) ≥30-spread** vs 10.9% (crosswind) and 5.3% (liberty). The grader prompt supplies only key+rubric — never the WLC/WCF text — yet criteria demand the model "quote the exact wording" (e.g. `PROOF-C2-006`: "Q109 no-representation clause supplied — 'all or of any of the three persons…'"). Graders cannot verify whether a quote is exact, so they fall back on impressionistic judgments and diverge (deepseek 91 vs mistral 14 on the same gpt answer for `PROOF-C2-006`).

**Fix:** Include the referenced WLC/WCF/WSC clause text in the grading standard (the `render_standard` function already drops the `anchors` list to save tokens — restore it for anchor items only), so exactness is checkable.

## CV-04 — Contested items depend on an underspecified "decline + grounding" criterion (MUST-FIX)

**Evidence:** contested items are 50% ≥30-spread (4/8 rows). Each carries a 1.5pt "declines a confident total order, grounded in incommensurable heads" criterion. Because RANKING_ASK offers "RANKING: declines total order" to *every* ordinal item, a model can decline by luck; the rubric asks the grader to judge *grounding quality* with no scale. `AGG-C5-W304`: gemini 70 / deepseek 70 / mistral 100 — mistral credited the decline fully; the others discounted the grounding. There is no operational definition of "adequately grounded."

**Fix:** Split into two criteria — (1.0) declines total order [binary, checkable], (0.5) names the specific incommensurable heads [checklist of accepted head-pairs]. Enumerate the accepted grounding phrases in the rubric.

## CV-05 — 23.6% of criteria are double-barreled (MUST-FIX)

**Evidence:** 255/1080 criteria contain ≥2 independent conjuncts joined by "and/;/+/slash" (excluding "≥N of" menus). Examples: `AGG-C3-003` "(a) profile: deliberate/malicious/public/sacrament, mitigated by newness + retreat" (five sub-judgments, one 1pt cell); `AGG-C7-007(b)` "deliberate/continuance/'with delight'/breaks-forth-in-actions/scandal (H3) + household harmed (H2)". Under full/half/zero, a response satisfying 3 of 5 conjuncts forces the grader to pick a single fraction — a recipe for the diffuse disagreement seen in category G below.

**Fix:** Decompose the worst offenders (start with the 3-in-92 "double-barreled-heavy" set) into single-judgment criteria, or explicitly define the fraction awarded per conjunct satisfied.

## CV-06 / CV-07 — Ceiling is one-third real, and frontier discrimination is half grader-noise (MUST-FIX)

**Evidence (recomputed across 6 SUTs, gemini grades, main n=204):**
- **70/204 (34%)** items score all three strong models (qwen, haiku, mistral-large) at exactly 100 → zero discrimination on a third of the bank. The top-of-leaderboard compression (haiku 89.9 / qwen 93.4) is partly this.
- 55 items separate the strong trio by ≥20; but **27/55 (49%) are also in the 92 grader-unstable set**. Only **28/204 (14%)** separate strong models *and* are grader-stable — the genuine frontier-discriminating core. The single largest "separator," `MEND-A-W305` (spread 100), is the CV-02 artifact, not a skill difference.

**Fix:** Report an honest discrimination figure ("≈28 items separate frontier models under a stable grader") rather than implying the whole 204 discriminates. Prioritize retiring/repairing zero-discrimination items or reserving them as a floor check.

## CV-08 — gemini==0 scores look like format-strictness, not consensus zeros (DEFER)
10 samples got gemini 0; the other two graders gave 8–100 on 8 of them (e.g. `LIB-C9-010` 0/25/25; `MEND-A-W305` 0/100/100). All 10 are gpt-4o-mini except none are haiku. Consistent with gemini penalizing format/hedge more than substance. Tolerable at pilot scale if the median panel is used (median discards the lone 0), but confirms CV-01.

## CV-09 — "Kendall partial credit" ordinals give the grader an unbounded hand (DEFER)
Ordinal items' top criterion is "full order correct (Kendall partial credit)" with no partial-credit table. Ordinal spread is 18.8% — not the worst, so DEFER — but two graders can award very different fractions for the same one-swap error.

## CV-10 — Point weights are asserted, not justified (DEFER)
Weights (2/1.5/1/0.5) carry no rationale. In `AGG-C9-001` the full 4-way ordering is worth 2 while each named head is 1 — a model that nails the ordering but names no heads gets ~29%, which may under-credit correct ranking. Defensible but undocumented; document the weighting logic before quoting per-item scores.

---

## 92 high-spread samples: defect taxonomy

Mutually-exclusive classification of the 92 rows with ≥30-point grader spread (join: grade matrix ↔ item bank). Base-rate context: contested 50%, anchor 43.5%, ordinal 18.8%, open 17.1%, episode 15.9% of their rows are high-spread.

| Category | Count | Nature | Representative |
|----------|------:|--------|----------------|
| G — diffuse 3-way disagreement | 23 | genuinely hard item; all three graders differ | `NARROW-C1-006` 60/20/100 |
| F — lone HARSH outlier | 19 | one grader ≥30 below two agreeing | `AGG-C6-008` 57/71/**0** |
| B — counterfactual condition | 15 | control-twin / prior-failure criterion (CV-02) | `PROOF-C1-W306` 69/92/100 |
| D — anchor clause-verification | 11 | exact-quote unverifiable by grader (CV-03) | `PROOF-C1-W303` 58/88/83 |
| C — contested/decline grading | 8 | decline-grounding underspecified (CV-04) | `AGG-C5-W304` 70/70/100 |
| F — lone LENIENT outlier | 7 | one grader ≥30 above two agreeing | `CROSS-C6-W204` 45/55/**100** |
| A — gemini-zero vs nonzero | 6 | frozen grader gave 0, others ≥30 (CV-01/08) | `MEND-A-010` **0**/64/9 |
| E — double-barreled-heavy | 3 | ≥2 compound criteria drive the split (CV-05) | `MEND-C1-W301` 69/100/100 |

**Roll-up:** grader-noise-driven (A+F lone-outliers) = **32/92 (35%)**; rubric-design-driven (B+C+D+E) = **37/92 (40%)**; genuinely-hard-ethics (G) = **23/92 (25%)**. Directional read: **the plurality of disagreement is fixable rubric design, not irreducible moral hardness** — the benchmark is repairable, but not yet quotable.

Note: 35/92 have gemini as the lone outlier vs two agreeing graders (recomputed) — reinforcing CV-01 that the frozen grader, not the items, drives a large share of instability.

---

## What survived (attacks that FAILED — benchmark held up)

1. **Score quantization is NOT coarse.** I hypothesized that 4–9-point rubrics graded full/half/zero would produce big discrete score jumps. Enumerated: mean **24.6 distinct achievable levels** per item, median max-adjacent-gap **5 points**. The 0–100 scale is effectively quasi-continuous. Quantization is not a threat. FAILED.
2. **The verbosity/length confound is weak.** Cross-item r(answer-length, score)=0.28 (gpt) / 0.15 (haiku) — but this is confounded by model quality (gpt writes *longer* answers 2668 vs 2292 chars yet scores *lower*). Decisive test — **within-item paired**: of 204 items, the longer of the two SUT answers scored higher in **79**, lower in **77**, tie 48 — a coin flip. A verbose rubric-echoing answer does **not** reliably outscore a terse correct one. FAILED (the grader template's explicit "do not reward eloquence or length" appears to hold).
3. **Anchor stems do NOT telegraph the key.** 0/23 anchor stems cite the WLC/WCF anchor their rubric rewards; ANCHOR_ASK uses '##' placeholders, never a real token. Key-telegraphing attack FAILED. (Anchor items are unstable for a *different* reason — CV-03 grader-unverifiability — not leakage.)
4. **Anchor-citation-count does not buy score.** r(n_citations, anchor score)=0.18 — citing more clauses barely moves the grade; models are not gaming the anchor requirement by citation-stuffing. FAILED.
5. **Ranking-format decline branch does not leak the contested items.** CONTESTED items get the identical RANKING_ASK as ORDINAL (verified in `record_to_sample`), so the prompt never betrays which item is the incomparable one. Design intent holds. FAILED.

---

## Hardest step to re-adjudicate

The single hardest verify/judge call is **category G (23 diffuse-disagreement items): how many are genuinely-contested ethics vs. latent rubric ambiguity?** I classified them as "hard ethics" by exclusion (they were not lone-outlier, not counterfactual, not anchor, not contested-kind), but distinguishing irreducible moral hardness from a subtly ambiguous criterion requires reading each item's rubric against the WLC text and adjudicating the ethics — a Fable-tier judgment. **Recommendation:** re-run the 23 G-items at the Fable tier with the underlying Westminster clauses in context, to split "keep as legitimately hard" from "repair the criterion." That partition determines whether the 25% "hard ethics" share is real or is more hidden CV-05 double-barreling.

---

## VERDICT: BLOCK (pilot with single-grader leaderboard) / PASS-WITH-FIXES (pilot with median panel + CV-02 items quarantined)

Do **not** run or quote the pilot on the frozen single-grader (gemini) config (CV-01), and quarantine the CV-02 counterfactual-condition items (they produce guaranteed noise). With the 3-grader **median** panel already coded in `wcf_tasks.py` as default, and MEND-A/control-twin items pulled or moved to episodes, an exploratory pilot may proceed with disclosure of CV-03/04/05 and the honest discrimination figure (CV-06/07).

**Single most likely remaining error:** the 3-grader median panel does **not** fix CV-02/CV-03/CV-04 — the median of three graders who are *all* judging an untestable counterfactual (MEND-A-W305) or an unverifiable exact-quote (anchor) is still meaningless; the panel launders grader *noise* but not rubric *invalidity*. Fixing the panel will make the instability numbers look better while the underlying construct defect persists.
