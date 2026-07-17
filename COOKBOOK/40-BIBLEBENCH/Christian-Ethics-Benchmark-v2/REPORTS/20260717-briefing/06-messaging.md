# WALKWORTHY v2 — Owner Briefing, Report 6 of 6: Messaging & Paper Framing

**Date:** 2026-07-17
**Status:** INTERNAL OWNER BRIEFING — not for circulation; pre-publication planning only
**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content

Scope note (carried from every v2 report): WALKWORTHY v2 is the **parallel** Inspect AI
harness; **v1 remains canonical** for release evidence. Every pilot cell is a descriptive
instrument reading under the R-rules, single-run stochastic decode, unreplicated. Nothing
in this report promotes a comparative claim past descriptive evidence, and nothing here
changes a judge pin. This report proposes how to *frame* two eventual papers; it does not
assert their findings.

---

## §1 The headline

**The most publishable result WALKWORTHY v2 produced is not a leaderboard — it is a
demonstration that cheap-judge leaderboards on value-laden constructs are judge-artifacts
until proven otherwise, plus a $0 two-referee method for locating *where* the judging
fails.**

Defending it: the v2 pilot ran all ten designs across five systems under test at
50/50 eval success and, on the pre-committed judge-swap pass, **every one of the nine
judge-scored designs flipped its naive SUT point-estimate ordering** when the scoring
judge changed from gpt-4.1-nano to llama-3.3-70b (design 05's judged secondary has no
ordering to flip). That is a clean, decision-relevant negative: at this altitude, a
single-judge ranking on these constructs measures the judge as much as the model. The
constructive half is the meta-audit: two independent frontier referees (Claude Opus via
an agent channel, GPT-5.6-Sol via `codex exec`), run blind on a frozen,
disagreement-enriched 942-unit sample at **$0 API spend**, do not merely re-rank — they
*localize* the failure. On design 07 the referees converge (both back judge-B ~3:1 over
judge-A, both back B on 225/392 disagreement turns) and diagnose a specific judge
character defect; on design 02 they agree with **each other** (0.735 raw, κ 0.653) but
with neither shipped judge (0.23–0.27), landing on the same "neither" state on 83/200
units — a taxonomy problem, not a judge-selection problem. That is a reusable QA pattern
with a clear honest boundary: **reference-model concordance, not ground truth.** The
leaderboard, by contrast, is not yet a result — it is contingent on future C9-clean runs
and resolved judge pins. So the paper we can honestly lead with is the methods paper; the
benchmark paper is real but its comparative surface is still pending.

---

## §2 Ranked findings

I re-ranked the candidate list. My ordering differs from the dispatch order: I promote the
$0 two-referee method (candidate 2) to #1 and the judge-swap discovery (candidate 1) to #2,
because the referee arms are what convert "everything is judge-sensitive" from a
warning into a *diagnosis* — the referee work is the load-bearing novelty and the harder
thing to have done. Floor saturation (candidate 3) rises to #3 because it is the one clean,
judge-robust *capability* statement the pilot owns (0 exclusions, holds under both judges).
Findings 4–6 follow. Rationale for each shift is in the table note.

| Rank | Finding | One-line claim | Robustness | Verified against |
|---|---|---|---|---|
| 1 | Two-referee $0 meta-audit | Blind, cross-vendor referees localize judge failure to (i) judge character, (ii) taxonomy ambiguity, (iii) 3 defect items | Two independent referees, cross-channel; consensus ≠ truth | opus-referee, sol-referee |
| 2 | Judge-sensitivity discovery | All 9 judge-scored designs flip naive SUT ordering under judge swap → 2-judge rule | Pre-committed swap pass, all 5 SUTs | pilot §2 |
| 3 | Design-07 floor saturation | No cheap-tier SUT completes the comfort-then-truth arc (arc_pass 0.000, all 5, 0 excl) | Judge-robust (0.00–0.04 under B), 0 exclusions | pilot §3/§4 |
| 4 | Corpus-distinctiveness triage | Only designs 04/05/10 are candidate-distinct from generic RLHF harmlessness at cheap tier (CV-1) | Construct-validity annotation, not an empirical test | pilot header |
| 5 | Anchor asymmetry / instrument property | Anchors move nano's verdicts far more than llama's; 07-vs-02 gap is an instrument property, not an anchor artifact | 3 ablation arms (2a/2b/2c) converge | f2-2c |
| 6 | Layered-verification yield | 105 fixes + 2 metric bugs + 1 parser + 1 alloc-spec bug + 3 defect items + 1 classifier outlier, all pre-publication | Cumulative across sessions; low live spend | methods, pilot §6, f3 |

**#1 — Two-referee $0 meta-audit.** *What it is:* two blind frontier referees over a
frozen 942-unit disagreement-enriched sample adjudicate where the shipped judge pair fails,
partitioning the failure into a judge-character component (design 07: nano under-calls
`full_validation`; Opus↔B κ 0.31 vs Opus↔A κ −0.07 on contested turns; Sol reproduces
0.605 vs 0.138), a taxonomy component (design 02: referees agree 0.735 with each other,
0.23–0.27 with either judge, 83/200 both-neither), and three concrete defect items
(WW-07-L02 / I04 / F02, "(no keyed text)" anchors that mechanically generate disagreement).
*Why it matters:* it is a general, cheap, reproducible way to audit LLM-as-judge pipelines
without an API budget, and it comes with the right epistemic humility built in
(concordance, not ground truth). *What would flesh it out:* a third reference model or a
self-consistency replicate per referee (both arms are single-pass); a human-adjudicated
gold slice on the design-02 neither-states to test whether referee consensus tracks a
defensible reading; and a within-vendor/cross-channel decomposition to separate model
effect from channel effect (agent vs codex exec vs direct API).

**#2 — Judge-sensitivity discovery.** *What it is:* under the pre-committed judge-B
re-score, all nine comparable designs flip their naive SUT ordering; per-design A/B field
agreement ranges from 0.21–0.26 (design 02, per-turn) up to 0.68–0.87 (designs 05/10).
*Why it matters:* it is the pilot's most decision-relevant output — any future v2
measurement run must budget a two-judge pass as a first-class component, and no single-judge
ranking survives on its own. *What would flesh it out:* a third judge to show whether the
swap instability is pairwise noise or a genuine multi-judge fan-out; a replication under
fixed decode (the swap sits on a single stochastic draw); and mapping which designs' flips
are within-CI reshuffles vs genuine reversals.

**#3 — Design-07 floor saturation.** *What it is:* every SUT scores arc_pass_rate 0.000
(Wilson [0.000, 0.125], n=27, 0 exclusions) under judge-A and 0.00–0.04 under judge-B — no
cheap-tier model completes a keyed comfort-then-truth arc. *Why it matters:* it is the one
capability statement the pilot owns that is judge-robust and not an exclusion artifact — a
genuine ceiling-room demonstration. *What would flesh it out:* frontier SUTs (the arc may
separate models above the cheap tier); and disentangling the three defective 07 items from
the floor (arc_pass should be recomputed after keyed text is authored for L02/I04/F02, since
those items currently cannot be scored as shipped).

**#4 — Corpus-distinctiveness triage.** *What it is:* the construct-validity annotation
(CV-1) that only designs 04/05/10 plausibly measure something distinct from generic RLHF
harmlessness at cheap tier; 01/02/03/06/07/08/09 are marked non-discriminant at this
altitude. *Why it matters:* it is an honest negative most benchmarks do not report — it
scopes any corpus-fidelity claim to a three-design sub-panel. *What would flesh it out:*
this is currently an *annotation*, not an empirical discriminant test — it needs a positive
demonstration (e.g., a harmlessness-only control model that passes 01/02/03 but fails
04/05/10, or a discriminant-validity correlation against a generic-safety benchmark) before
it can be stated as a finding rather than a caveat.

**#5 — Anchor asymmetry / instrument property.** *What it is:* three ablation arms (2a
remove 07 anchors, 2b answer-blind, 2c add 02 anchors) converge — anchors account for only
~5 points of the 07-vs-02 agreement gap, and anchor-dependence is judge-asymmetric (nano
self-consistency 0.42–0.50 under added anchors vs llama 0.61–0.71). Blind deltas reach ±0.52
for nano vs ~±0.13-class stability for llama. *Why it matters:* it correctly kills the
tempting "the anchors did it" reading of the 07-vs-02 gap and grounds the 2-judge mandate's
mechanism (A and B disagree partly because they *use* anchors differently). *What would
flesh it out:* a second judge pair (all three arms use nano × llama only); and the ±0.52
figure needs its own citation confirmed — see verification issues below.

**#6 — Layered-verification yield.** *What it is:* the cumulative pre-publication catch
list — 105 item fixes in the review pass, the design-04 abs() metric-semantics bug, the
design-05 alloc-spec field-path bug (all-nan CSR was a bug, not model behavior), a parser
defect, three defect items, and the nano classifier outlier (24.4% of branch decisions are
2-alternatives-vs-nano) — all caught before any comparative publication. *Why it matters:*
it is the credibility spine of both papers: the instrument was hardened by many independent
passes at low spend. *What would flesh it out:* a single consolidated defect ledger with
dated provenance per catch, so the "N bugs caught pre-publication" claim is auditable rather
than assembled from six reports. (See verification issues on the exact total-spend figure.)

---

## §3 Paper (a) — benchmark design + leaderboard

**Proposed title:** *WALKWORTHY: A Behavioral Benchmark for Christian-Ethics-Aligned
Conduct in Language Models, Anchored to a Named Ethics Corpus*

**Alternates:**
- *Measuring Corpus-Anchored Moral Conduct in LLMs: The WALKWORTHY Benchmark and Its
  Ten Behavioral Designs*
- *Beyond Harmlessness: A Ten-Design Benchmark for Behavioral Fidelity to a Specified
  Christian-Ethics Registry*

**Abstract (~250 words).** Evaluations of the moral conduct of language models
overwhelmingly target generic harmlessness. We present WALKWORTHY, a behavioral benchmark
that instead measures conduct against a **named, specified corpus** — a fifteen-work
registry of Christian-ethics texts — rather than against "Christianity" or any claim of
theological truth. Every item's keyed behavior is anchored to specific chapters or
dictionary entries of the registry; direct Scripture anchoring is disallowed by
construction, and one work is restricted to contrast-only use. The bank comprises 344
publicly runnable items across ten method-distinct designs — obedience, consistency under
social pressure, stated-versus-enacted fidelity, motive discernment, constraint
satisfaction, criterion profiling, a comfort-then-truth pastoral arc, covert-versus-overt
protection, dispute-seat symmetry, and mercy calibration — with a stratified 158-item
holdout withheld from all public surfaces. We describe the item authoring, the
paired-administration and escalation-ladder designs, the model-graded and judge-free
scoring, and a construct-validity triage that honestly scopes corpus-distinctive
measurement to a three-design sub-panel. We report a full ten-design, five-system pilot as
a **pilot**: descriptive per-cell instrument readings with intervals, and no comparative
system rankings, because the pilot data predate the pre-registered comparison protocol and
because all judge-scored designs are judge-sensitive at this tier. A leaderboard is deferred
to future runs that satisfy the first-use (blind) rule and resolve open judge pins. Our
contribution is the instrument and its methodology, plus a candidate finding — that no
cheap-tier system completes the pastoral comfort-then-truth arc — offered as a capability
observation rather than a ranking.

---

## §4 Paper (b) — judge-sensitivity / two-referee meta-audit methods note

**Proposed title:** *Judging the Judges for $0: A Two-Referee Concordance Method for
Localizing LLM-as-Judge Failure on Value-Laden Rubrics*

**Alternates:**
- *Reference-Model Concordance, Not Ground Truth: Diagnosing Where Cheap Judges Fail on a
  Christian-Ethics Benchmark*
- *Disagreement-Enriched Two-Referee Auditing of LLM Judges: A Reusable QA Pattern*

**Abstract (~250 words).** LLM-as-judge scoring is now standard for value-laden benchmarks,
yet cheap judges can silently drive results: on a ten-design Christian-ethics benchmark, we
find that **all nine judge-scored designs flip their naive system ordering** when the
scoring judge is swapped across model families — cheap-judge leaderboards on such
constructs are judge-artifacts unless a comparison survives the swap. We then ask *where*
the judging fails, and answer it with a method that costs no API budget. On a frozen,
**disagreement-enriched** 942-unit sample, we dispatch two independent frontier referees
through subscription channels — a Claude Opus agent and GPT-5.6-Sol via `codex exec` —
blind to system identity and to the shipped verdicts, using byte-identical shipped prompts.
The referees partition the shipped judge pair's failure into three localizable causes: a
**judge-character** defect (on the pastoral-arc design, one judge under-calls the target
state; both referees back the other judge ~3:1 and agree with each other 0.86), a
**rubric/state-taxonomy** ambiguity (on the consistency design the referees agree 0.735 with
each other but only 0.23–0.27 with either judge, landing jointly on a "neither" state on
41.5% of contested turns), and three **defect items** whose empty keyed anchors mechanically
generate disagreement. We frame the entire method as **reference-model concordance, not
ground truth**: two referees may share correlated error, so this is consensus evidence, not
correctness. We offer the disagreement-enriched, two-referee, $0-subscription-channel
dispatch as a reusable QA pattern for auditing judge pipelines before publication.

---

## §5 What NOT to claim

Explicit list — every item below is a claim the source data does **not** license, with the
governing rule:

1. **No SUT rankings from the pilot data.** The pilot predates the pre-registered
   comparison protocol; R1/R3 remain in force for all data existing as of 2026-07-16, and
   C9 requires the "post-hoc on pilot data — hypothesis-generating" label on any comparison
   run on existing logs. Do not print a leaderboard from pilot cells. (No comparison also
   survives the 2-judge rule R4 at this tier.)

2. **No "the referees prove judge-B is correct."** The referees establish *concordance*, not
   truth. "Opus and Sol both side with judge-B on design 07" is evidence about **judge-A's
   character**, not a certification that judge-B is right. Two referees agreeing may share
   correlated error from similar training regimes.

3. **No pooled agreement numbers without the per-stratum split.** The referee sample is
   disagreement-enriched by construction; a single "overall agreement" headline is invalid.
   Strata (control vs disagreement; per design) are never pooled and must not be pooled
   downstream.

4. **No religious-authority or theological-truth claims.** The benchmark measures
   **concordance with a specified fifteen-work corpus**, never fidelity to Christianity,
   Scripture (anchoring to which is disallowed by construction), or moral truth. Say
   "aligned with the registry corpus," never "correctly Christian." The corpus is
   Protestant-Reformed-dominant and named as such.

5. **v2 is parallel to v1, not canonical.** v1 remains the canonical execution path until
   the comparability check and the two-judge path validation are complete. Do not describe
   v2 pilot numbers as release evidence.

6. **No cross-classifier pooling, ever (C6/F3).** With alt-alt classifier agreement 0.902 vs
   alt-nano ~0.70 and 24.4% 2-vs-1-against-nano, results under different pinned classifiers
   are different experiments.

7. **No comparative reading of the F2-2c / F3 offline analyses.** These are non-blind,
   post-pilot; their load-bearing conclusions are instrument-level and judge-level, not
   SUT-comparative (C9 in force).

---

## Sources

All under `$V2 = CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`:

- `20260716-pilot-report.md` — 5-SUT full-scope pilot (§§1–7): judge-swap ordering flip,
  per-design cells, design-07 floor, design-05 alloc-spec bug, spend.
- `20260716-opus-referee-results.md` — arm-1 Opus referee meta-audit (942-unit,
  concordance tables, findings, defect items, owner decision hooks).
- `20260717-sol-referee-results.md` — arm-2 GPT-5.6-Sol referee (four-way concordance,
  design-02 revised framing, referee-referee agreement, defect confirmation).
- `20260716-f2-2c-results.md` — F2 arm-2c anchor ablation; F-2c-1/2/3 (instrument property,
  judge-asymmetric anchor dependence).
- `20260716-f3-crossfamily-classifier-results.md` — nano-as-classifier outlier; alt-alt
  0.902 vs alt-nano ~0.70; 24.4% 2v1; C6 no-cross-classifier-pooling.
- `20260716-f5-certification-results.md` — G5 conclusion-neutrality certification of all
  three judges; anchor-hungry ≠ conclusion-penalizing.
- `METHODS/20260715-walkworthy-v2-inspect-academic-methods.md` — corpus (15-work registry,
  344 runnable + 158 holdout), designs, scoring, migration, review pass (510 reviewed / 105
  fixed / 0 removed), parallel-not-canonical framing.
- `20260716-prereg-comparisons-RATIFIED.md` — F11 comparison families, C4 2-judge rule, C6
  pinned classifier, C9 first-use rule, multiplicity handling.

---

## Appendix: ranking rationale & verification notes

**Word count:** ~2,340 words (body §1–§5 excluding this appendix and the sources
list).

**Ranking rationale (differs from candidate order):** I promoted candidate 2 (two-referee
meta-audit) to #1 and demoted candidate 1 (judge-swap) to #2. The judge-swap is the
*discovery*; the referee arms are the *diagnosis* and the reusable, novel contribution — two
independent cross-vendor referees at $0, with dual confirmation of the 07 judge-character
finding and a revised (arm-2-sharpened) 02 taxonomy reading, is the harder and more
publishable artifact. Everything else kept candidate order (floor saturation at #3 as the
one judge-robust capability statement; triage/anchor/verification 4–6).

**Verification notes (three items flagged at drafting were resolved in the
main-session audit, 2026-07-17):**
- **llama ±0.13 blind-delta — VERIFIED.** `20260716-f2-ablations-report.md` (arm 2b
  results) states judge-B's answer-blind deltas stay within ±0.13 (design-09
  `floor_compliance` +0.06…+0.11), against nano's deltas to ±0.52. The pairing stands.
- **Total live spend — RESOLVED as a range, not a point.** No source states one
  aggregate. Verified memo components: smoke $0.038 + replay ≈$0.01 + pilot $3.63 +
  s5 GO (F9 $0.07–0.09, F2 2a/2b $0.5–0.9, cross-harness ≤$0.75) + s6 GO $0.25–0.35
  (F5 + F3 cross-family) + s7 GO (F7 $0.40–0.78, F2-2c $0.65–1.23) + referee arms $0
  ≈ **$5.5–7.8 estimated**; the OpenRouter dashboard is the source of record. The
  "≈$7.5" candidate figure sits at the top of this range and should be quoted as the
  range, as 02-evaluation.md §1 now does.
- **design-04 abs() bug label — VERIFIED.** `20260716-adjudication-fixes-report.md`
  (M1) spells it out: v2 computed `motive_sensitivity_index = mean(abs(alpha − beta))`
  where v1 uses the signed delta; `abs()` inverts the key on zero-keyed pairs.
- Everything else in §1–§5 (judge-swap all-9-flip, per-design agreement bands, 942-unit
  sample, referee side-with rates, 83/200 both-neither, 0.735/0.653 referee-referee, arc_pass
  0.000 / 0 excl, alt-alt 0.902 / 24.4% 2v1, G5 certification, 344+158 corpus, 15-work
  registry, C6/C9/R4 rules) is directly verified against the cited sources.
