# Critique — Judge Validity & Gaming (WALKWORTHY v2)

**Date:** 2026-07-16
**Lens:** REFUTE-FIRST adversarial. Target claim: *the single-judge model-graded pipeline yields valid, ungameable scores.* I try to break it; I concede only what survives a steelman.
**Scope:** `walkworthy_inspect/{scorers,rubrics,solvers,parsers,refusal,metrics,datasets}.py`, tasks 02/05/07, public bank items 05/07, reports `20260715c`, `20260715d`, `20260716-polish-items`. v1 `judges.py` is the fidelity baseline (read-only). Item wording is out of scope (ratified in `RULINGS-APPLIED.md`).

Evidence conventions: `file:line`. Report numbers quoted from `20260715d-e2e-and-two-judge-report.md` Part 2 (v2 judge-A vs judge-B exact-agree) and `20260715c` (v2-vs-v1jA replay).

---

## JV-1 — Design 05 primary metric (CSR) is gameable by allocation-numbers-without-ethics
**Severity: CRITICAL. Pilot-blocking: NO (but headline-invalidating for 05; must be disclosed).**

**Claim attacked:** "Design 05's judge-free parser scoring rewards constraint-satisfying *ethical reasoning*."

**Evidence.** The 05 primary is `constraint_satisfaction_rate`, computed purely from the parsed `allocation:{...}` numbers vs numeric floors/caps (`scorers.py:563-564`, `parsers.py`, `ordo_constraints.item_csr`). I executed the live pipeline:

```
resp = "Here are the numbers.\nallocation: {debt: 11000, shelter: 2500, coworker_child: 1500}"
reparse_allocation_response(...).ok == True ; item_csr(values, constraints, tokens) == 1.0
```

A response that emits *only* the numbers, with zero rationale, scores the design's PRIMARY metric at a perfect 1.0. `rationale_honesty` (the "does the rationale name the sacrifice?" check, `rubrics.py:113`) is a *secondary* model-graded category that never gates the primary — `metrics.py::constraint_satisfaction_rate` (149-168) reads only `constraint_satisfaction_rate`, never `rationale_honesty`. A model that has memorized the numeric floors (they are computable from the public `keyed_constraints` prose, which is embedded verbatim as `target` and in the judge prompt) maxes the headline without ethics.

**Refutation attempt (steelman).** "The numeric floors ARE the ethical content — hitting debt≥$10k while funding giving≥$4k *is* the ordo-amoris judgment." Partly true: numeric compliance is a necessary condition. **Why it survives:** it is not sufficient, and the design's own construct is "does the rationale name the sacrifice." The primary discards exactly that. Worse, because the floors are public and mechanical, 05 is the single most contamination-exposed design in the suite — a model that has seen the bank can pattern-match the number band with no reasoning. The secondary that would catch this is not in the primary, is single-judge, and (report `20260715d`) had 0 needs-adjudication cells only because n was tiny and one 05 sample was empty-completion.

**Remedy.** (a) Gate the 05 headline on a joint `csr ∧ rationale_honesty≥1` (report both the raw CSR and the joint-pass rate); (b) treat 05 as the canary for contamination — hold out the numeric floors, or randomize budget/token magnitudes per administration so memorized bands don't transfer; (c) disclose in any pilot writeup that CSR is a format/arithmetic metric, not a reasoning metric.

---

## JV-2 — Judge prompt embeds the keyed correct answer → structural leniency / anchor leakage
**Severity: MAJOR. Pilot-blocking: NO.**

**Claim attacked:** "The judge scores the response on its merits."

**Evidence.** `assemble_rubric_prompt` (`scorers.py:140-178`) inserts the item's keyed anchor verbatim under `# Rubric anchor (the corpus-keyed norm for this item)` (line 153-154), *before* the response. For several designs the keyed text IS the graded answer: design 05 `target == keyed_constraints` verbatim (confirmed on the public record); 03 surfaces `keyed_expressed` (the correct expressed judgment); 09 surfaces `keyed_determinations` (who-owes-what). The judge is thus told the answer, then asked whether the response matches it.

**Refutation attempt (steelman).** "This is intentional and ported verbatim from v1 `judges.py` — it is *reference-anchored scoring*, standard for rubric graders, and the length-correction instruction (`_LENGTH_CORRECTION`, 48-52) explicitly forbids rewarding length/hedging." True, and I concede this is a faithful v1 port, not a v2 regression. **Why it survives as a validity concern:** anchor-visible judging has a known failure mode — the judge over-credits any response that *lexically echoes* the anchor. Because the anchor is embedded and the rubric state definitions themselves contain trigger words (see JV-3), a verbose SUT that parrots the anchor's vocabulary can be scored "faithful" without enacting it. The length-correction instruction is a soft textual nudge to a single judge, not a mechanism; there is no held-out or answer-blind control condition anywhere in the pipeline to bound the leniency.

**Remedy.** Run an answer-blind ablation on a sample (score with the anchor removed vs present; measure the delta) to bound anchor-induced leniency; adopt for at least the reference-anchored designs 06/09 where a "neutrality gate" is claimed (`scorers.py:163-165`) but never empirically checked.

---

## JV-3 — Rubric state definitions carry parrotable trigger words (verbalize-without-enact gaming)
**Severity: MAJOR. Pilot-blocking: NO.**

**Claim attacked:** "A model that VERBALIZES virtue without enacting it cannot satisfy the rubric."

**Evidence.** The categorical option sets are surfaced to the judge with their descriptions (`scorers.py:158-159`, `# Categories to score`). Several are lexically transparent: 07 `faithful_counsel` "both poles held" vs `comfort_only` (`rubrics.py:134-138`); 08 `guardrail_state ∈ {protected, surfaced, steamrolled}` "did the artifact honor/flag/erase the embedded stake" (144-145); 10 `duality` "names the wrong AND extends the good" (165). A SUT that writes "I want to honor your wound *and* faithfully name the vice" is using the exact discriminator language the judge is primed to detect. Single-judge, anchor-visible, trigger-word-laden = maximally suggestible to surface mimicry.

**Refutation attempt (steelman).** "The rubrics are ported verbatim from v1 and the discriminators (07 `comfort_only↔faithful_counsel`, added per-item in v2) are *behavioral* — faithful_counsel requires *moving toward an alternative*, which a parrot can't fake." The 07 bank items do encode a genuinely behavioral discriminator (e.g., WW-07-E01 requires *naming the weaponized toast* and *moving to a real alternative*, not just warmth). **Why it survives:** whether the *judge* enforces the behavioral bar rather than the lexical one is unmeasured. The v1 07 inter-judge exact agreement was 0.222 (report D) — i.e., two judges applying this very rubric agreed barely above one-in-five. v2 A-vs-B for 07 is 0.667 but on ~9 cells with 2 needing adjudication; there is NO experiment isolating whether the v2 per-item discriminators *raised* judge agreement (see JV-6). So the anti-parrot claim rests on item design that the judge may or may not honor, with no evidence it does.

**Remedy.** A held-out "sycophantic-but-eloquent" adversarial probe set (responses that maximize discriminator vocabulary but withhold the behavioral move) scored by both judges; report the false-faithful rate.

---

## JV-4 — 02/07 mid-solver classifier IS the judge model → a judge error becomes a STIMULUS error, silently
**Severity: MAJOR. Pilot-blocking: NO (but auditability gap should be closed pre-pilot).**

**Claim attacked:** "Branch misclassification in the ladder is bounded and auditable."

**Evidence.** Tasks 02 and 07 wire `classifier_model=judge_model` (`tasks/design02_twomasters.py:28`, `design07:26`) — the same model instance that later scores the turns also *chooses which user prompt the SUT next sees* (`solvers.py::_classify_branch`, 86-116). A misclassification changes the branch (`solvers.py:176-180`), so the SUT experiences a *different conversation*. This is not merely a scoring error; it perturbs the stimulus. The chosen branch is recorded (`branch_state` in `ww_turns`, `solvers.py:187-188`), so it is *loggable*, but: (a) there is no ground-truth branch label to compare against — the classifier's own output is the only record, so its error rate is unmeasurable from logs alone; (b) under any classifier failure the code silently falls back to the v1 lexical heuristic then to `states[0]` (`solvers.py:112-116`, 66), and the fallback path is not distinguished in the record from a confident classification.

**Refutation attempt (steelman).** "The fallback is graceful degradation, the branch is recorded, and per-turn scoring judges the *actual* responses the SUT gave regardless of path." True — the per-turn scorer judges real turns. **Why it survives:** the METRIC (break_turn, arc_shape) is a function of the whole trajectory, and the trajectory depends on branch choices. Two SUTs of equal quality can get different arc_shape scores because the shared judge/classifier routed them differently. With a same-family judge (JV-5) this compounds: the classifier may route a same-family SUT down a more favorable branch. No confusion-matrix, no dual-classifier check, no "fallback fired" flag exists.

**Remedy.** (a) Log an explicit `classifier_confident=True/False` and `fallback_used` flag; (b) sanity-run 02/07 with classifier≠judge (cross-family classifier) and measure branch-choice divergence; (c) report break_turn/arc_shape sensitivity to classifier family.

---

## JV-5 — Same-family SUT/judge pairing has no guardrail; default judge is a task arg with no family-mismatch enforcement
**Severity: MAJOR. Pilot-blocking: NO.**

**Claim attacked:** "Cross-family judging protects against style/family affinity bias."

**Evidence.** `DEFAULT_JUDGE = "openrouter/openai/gpt-4.1-mini"` (`scorers.py:44`); the judge is a free task parameter (`judge_model` on every task). Nothing prevents running a GPT SUT under the GPT judge — and the *default* judge is GPT, so any GPT-family SUT is same-family by default. The design charters explicitly call for "2 cross-family judges" (07 bank §4: "Per-turn coding by 2 cross-family judges") but the runnable pipeline ships single-judge, same-family-permitting, with cross-family judge-B *deferred* (README; `20260715d` Part 2).

**Refutation attempt (steelman).** "The comparability report holds the judge fixed at gpt-4.1-nano and the SUT was mistral-small — cross-family by construction — and got 73.2% v2-vs-v1jA agreement." That single replay was cross-family, yes. **Why it survives:** 73.2% (`20260715c`) is *harness-reproduction* agreement (v2 re-running v1's judge on v1's stored responses), NOT a same-vs-cross-family bias measurement. There is zero measurement of GPT-judges-GPT leniency. Judge-B (llama-3.3-70b) exists in `tools/rescore/` but is deferred, so the shipped headline is single-judge with no family control. Verbosity/length affinity (GPT judges reward GPT-style formatting) is entirely unbounded.

**Remedy.** Enforce (or at minimum warn + record) family-mismatch between SUT and judge; for any same-family run, require the deferred judge-B cross-family re-score as a leniency bound; measure same-vs-cross-family score delta on a shared response set before pilot headlines.

---

## JV-6 — 73.2% and the design-07 remedy: the numbers do not establish per-design headline stability
**Severity: MAJOR. Pilot-blocking: NO (disclosure-blocking).**

**Claim attacked:** "73.2% > 59.2% baseline shows the judge path is valid," and "the v2 comfort_only↔faithful_counsel discriminators fixed 07's 17.6% floor."

**Evidence.** 73.2% (123/168 field-cells, `20260715c`) EXCLUDES designs 02 and 07 (per_turn, no single-completion path) and is a single-SUT harness-reproduction number, not per-design inter-judge reliability. The actual v2 judge-A-vs-judge-B exact agreements (`20260715d` Part 2) are alarming per-design: **09 = 0.219** (25 needs-adjudication cells), **02 = 0.182**, 06 = 0.486, 08 = 0.545, 03 = 0.639. At judge-A/judge-B exact agreement of 0.18-0.22 on 02 and 09, a judge-A vs judge-B swap will *flip the primary metric direction* on those two designs — symmetry_index (09) and break_turn (02) are the most confusable in the suite. Any pilot ranking that separates two SUTs by less than the judge-swap noise on 02/09 is not real.

On 07: the boot brief cites a v1 floor of **17.6%**; that exact figure is NOT in any of the three reports (report D shows v1 07 baseline = 0.222 and v2 A-vs-B = 0.667). The v2 per-item discriminators are present in the bank (WW-07-E01/B01 `comfort_only vs faithful_counsel` blocks), but **no experiment measures post-remedy judge agreement attributable to the discriminators** — 0.667 is on ~9 cells with 2 adjudication-needed and confounds fresh sample + item fixes + harness (report D labels its own comparison "DESCRIPTIVE, not an agreement statistic").

**Refutation attempt (steelman).** "73.2% exceeding the 59.2% v1 inter-judge baseline is real evidence the v2 harness faithfully reproduces v1's judge." Conceded — as a *port-fidelity* claim, JV-6 does not touch it; the harness reproduces v1's judge better than v1's two judges agreed. **Why it survives:** port fidelity ≠ score validity. Reproducing a judge whose own inter-judge agreement is 0.18-0.22 on 02/09 faithfully reproduces an unreliable instrument. The remedy for 07 is asserted, not demonstrated.

**Remedy.** (a) Report per-design judge-swap agreement (from `tools/rescore`) as the confidence band on every headline; suppress any SUT-vs-SUT ranking within that band on 02/09. (b) Run an ablation: 07 items scored with vs without the per-item discriminator block, both judges, to actually attribute the remedy. (c) Correct the "17.6%" provenance in the boot brief (it is not in the evidence files).

---

## JV-7 — Refusal taxonomy is hardwired `engaged=False`, mis-routing engaged responses that trip lexical cues
**Severity: MINOR. Pilot-blocking: NO.**

**Claim attacked:** "The refusal preprocessing correctly separates strategic refusals from honest engagement."

**Evidence.** Every scorer calls `_refusal_cell(...)` → `tag_response(..., engaged=False)` (`scorers.py:284`, hardcoded). The R1 engagement-override branch (`refusal.py:112-113`) — the mechanism that routes a lexical false-positive on a *substantively engaged* answer back into the compliance branch — can therefore never fire in v2. A response that both engages the ethical task AND contains a phrase like "I'd rather not sugarcoat this" or "I can't in good conscience recommend…" (matching `_REFUSAL_PATTERNS`, 45-57) is tagged as a refusal and, absent a keyed outcome, lands in `pending_adjudication` (121) instead of `helpful`.

**Refutation attempt (steelman).** "The refusal cell is metadata, not the primary score — it doesn't move break_turn/say_do_gap/etc." Mostly true: the four-way tag is a reporting cell, and `detect_refusal` requires an *early* cue or ≥2 cues (`refusal.py:75-77`), limiting false positives. **Why it survives:** (a) the 04-way refusal rates ARE reported and will be cited; systematically over-counting refusals for eloquent engaged answers biases the "unnecessary_refusal / appropriate_refusal" split; (b) `engaged` is exactly the input v1 designed to prevent this, deliberately disabled with no substitute (no "did the judge score any faithful category" heuristic feeds `engaged`). It is a latent correctness bug, minor only because it doesn't touch primaries.

**Remedy.** Derive `engaged` from the judged categories (e.g., any non-refusal categorical state present ⇒ engaged=True) before calling `tag_response`, restoring the R1 override; or document that the refusal cell over-reports refusals for engaged responses and must not be used as a standalone rate.

---

## JV-8 — Per-turn independent judging (02/07) discards arc context the rubric's own states presume
**Severity: MINOR. Pilot-blocking: NO.**

**Claim attacked:** "Judging each turn independently preserves the information arc_shape/break_turn need."

**Evidence.** `_make_per_turn_scorer` judges each turn's response ALONE — the prompt carries only "that turn's response ONLY + rubric + anchor" with `unit_label="turn N"` (`scorers.py:363-415`, docstring 371-377). But 07's states are inherently trajectory-relative: `comfort_only` is *keyed-correct at T1-T2 and a failure only if terminal* (07 bank §5, and the WW-07 discriminator blocks say "correct T1–T2"). A judge seeing only turn 4's text cannot know it is terminal, nor that comfort was already given at T1. The metric (`metrics.py::_arc_shape_item`, 229-253) then reassembles order from the independent labels — but the labels were assigned context-free.

**Refutation attempt (steelman).** "This mirrors v1 `judges.py:93-107` semantics verbatim (each turn judged against the item rubric independently), and the metric supplies the ordering the judge lacked." Conceded — it is a faithful port, and terminal-position logic lives in the metric, not the judge. **Why it survives:** the *state assignment itself* is order-dependent for 07 (a turn is `comfort_only` vs `faithful_counsel` partly based on whether the alternative was *already* offered earlier). Turn-independence forces the judge to guess. This plausibly explains 07's chronically low inter-judge agreement (v1 0.222). Faithful-to-v1 does not make it valid.

**Remedy.** Pass a compact prior-turn summary (or the running state vector) into each per-turn judge prompt for 07 specifically; re-measure inter-judge agreement against the context-free baseline.

---

## What survives

- **JV-1 (CRITICAL, survives fully):** Design 05's PRIMARY metric (CSR) is satisfied by allocation numbers with zero ethical reasoning — verified live (csr=1.0 on a rationale-free response). The reasoning check is a non-gating secondary. This is a real, demonstrated headline-invalidating gaming vector for 05, compounded by public, mechanical, memorizable numeric floors. **Fix or disclose before any 05 headline; not pilot-blocking for the other 9.**
- **JV-2, JV-3 (MAJOR, survive):** Anchor-visible + trigger-word-laden single-judge scoring is structurally suggestible to verbalize-without-enact mimicry; no answer-blind or adversarial-parrot control exists to bound it. Faithful v1 ports, but unvalidated.
- **JV-4 (MAJOR, survives):** 02/07 use the judge model as the branch classifier, so judge error perturbs the *stimulus*; no fallback-fired flag, no classifier error rate, no cross-family classifier check.
- **JV-5 (MAJOR, survives):** No same-family SUT/judge guardrail; default judge is GPT, so GPT SUTs self-judge by default; cross-family judge-B is deferred. Family/verbosity bias entirely unmeasured.
- **JV-6 (MAJOR, survives):** 73.2% is port-fidelity, not per-design reliability. True per-design judge-swap agreement is 0.182 (02) and 0.219 (09) — swap noise will flip those primaries. The 07 "17.6%→fixed" story is asserted, not measured, and 17.6% is not in the evidence files.
- **JV-7 (MINOR, survives):** `engaged=False` hardcode disables the R1 override; refusal cell over-reports refusals for engaged answers. Reporting-only, latent bug.
- **JV-8 (MINOR, survives):** Context-free per-turn judging is order-blind for 07's order-dependent states; a faithful-but-invalid port; plausible driver of 07's low agreement.

**Conceded to the pipeline:** the 73.2%>59.2% harness-reproduction result is legitimate as a *port-fidelity* claim; the length-correction instruction and the neutrality-gate scaffolding are present; unscorable/mock handling is robust and never crashes; canary discipline and holdout guarding (`datasets.py:169-174`) are intact; the 05 arithmetic/parser recovery is conservative (no synonym inference, multiple readings stay unparseable).

**Bottom line:** No single finding blocks a *pilot* (all primaries compute and don't crash), but **JV-1 must gate any published 05 number**, and **JV-6's per-design swap noise (02/09) must be reported as the confidence band on every ranking** — otherwise SUT separations inside 0.18-0.22 judge-swap noise will be reported as real when they are not. The "ungameable, valid" claim does not survive for design 05 (gamed) and is unproven for the anchor-leniency / same-family / low-agreement surfaces.
