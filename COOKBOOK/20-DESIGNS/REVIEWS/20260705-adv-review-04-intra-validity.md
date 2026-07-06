# Adversarial Feasibility/Validity Review — Design 04 (INTRA)

> **Reviewer posture:** refute-first. The design is assumed flawed until evidence forces otherwise.
> **Artifact:** `COOKBOOK/20-DESIGNS/04-religious-intra.md` (INTRA — intra-tradition reasoning, denominational conditioning).
> **Standards:** KB 01 (Seven Laws / ten-step pipeline / pre-reg checklist), 03 (validity/psychometrics),
> 04 §6 (hard/unsaturated/discriminative contract); consulted 05/07/10 where the attack required.
> **Date:** 2026-07-05. Digest statistics quoted verbatim; not recomputed.

---

## Summary verdict

INTRA is the most methodologically self-aware design in the portfolio — it imports competence controls,
capability-correlation gates, four-way refusal, procedural parametrization, and a governance model. But
its **central novelty claim ("from religious trivia to religious reasoning") is not yet supported by its
own construction**, and two load-bearing pillars are currently unfalsifiable-as-built: (1) the layer that
actually discriminates (M) is knowledge+computation, not values; (2) the only genuine values layer (V) is
scored in exactly the regime KB 07 says LLM judges fail, on gold labels defined by a 3-person board that
also annotates and adjudicates them. Both are fixable in principle, but as written the design would ship a
knowledge benchmark wearing a values label — the *precise* pathology (the "ELQV paradox") it was built to
escape. BLOCK pending pre-registered kill criteria and a decoupled ground-truth pipeline.

---

## CRITICAL defects

### C1 — The discrimination engine is the least values-relevant layer (ELQV paradox reproduced, not escaped)
**Attack (a) construct validity; Law 1; KB 04 §6.**
The design's discrimination bet is explicit: "pilot must reproduce a T2-style continuous spread on
M-layer" (§6). But the M-layer — fara'id shares, *'awl/radd* redistribution, kashrut ratios (*batel
b'shishim*), eruv geometry, halakhic calendrics — is **exact-match computable jurisprudence**: procedural
knowledge retrieval + arithmetic. It is not a values or propensity measure. The design *inherits the exact
instrument* KB 10 flags as "knowledge tasks wearing values labels" — the Arabic fara'id MCQ whose spread
was "6.7%→100%". Two fatal consequences:

1. **Best-model saturation.** That instrument's top score is **100%** (best model saturates). KB 04 §6
   item 1 requires "best frontier model ≤~70% of ceiling on the hard tier." The inherited exemplar
   *violates* the contract at the top even as it discriminates in the middle. The design asserts the
   "conflicting-rule-with-meta-principle" tier will pull the top model below 70% but shows no evidence.
2. **Capability confound is the whole ballgame.** The design's own matched-secular-arithmetic control
   (§6, §9) exists precisely because M-layer may correlate with math/capability (Law 1: "a values score
   that tracks capability measures capability"; >~40% cap-correlation = red flag). **The design never
   states what happens if M fails that gate.** If M is capability-driven (likely — it is arithmetic over
   memorized rulings) *and* V ceiling/floors (which KB 10 reports every rubric-scored religious
   instrument did — "trimodal ceiling/floor pathology … no model in the 0.2–0.8 band on any K/R/V
   dimension"), then INTRA has **no demonstrated values discrimination at all**. The novelty pitch
   collapses into a relabeled fara'id clone.

**Minimal fix:** Pre-register a kill criterion in the pilot: *if M-layer capability-PC1 correlation
≥40% AND V-layer fails to produce a continuous mid-band spread (≥90% of model pairs separated at p<0.01),
the "reasoning-first values" claim is falsified and the design reverts to an honestly-labeled
jurisprudential-knowledge benchmark.* Make V-layer discrimination — not M-layer — the primary success
condition, since M is by construction the recognition/knowledge layer (Law 1 mandate: behavioral primary,
recognition as *paired baseline only*).

### C2 — Ground-truth authority is circular and non-auditable (authors = annotators = adjudicators = ceiling; N=3)
**Attack (a) authority/ground-truth problem; KB 03 §2; KB 07 §4.**
"Who defines the correct denominational reading?" The design's answer (§4): a 3-scholar board per tradition
that **authors items, owns the gold school-labels, owns the 'scholars differ' designations, and holds veto**
— and then in §6 the *same* "board experts" sit on the human ceiling ("board experts on identical items").
This violates the corpus's most basic reliability requirement and one of its firmest anti-patterns:

- **No independent label reliability is computable.** KB 03 §2: "No coefficient reported = disqualifying."
  You cannot report an honest chance-adjusted per-category κ/α when the authors *are* the annotators. The
  design lists "IRR gates (κ≥0.7 per category)" (§6) but never says *between whom* — as structured there is
  no independent rater pool to agree or disagree.
- **Circular human ceiling.** KB 03 template: "ceiling ≠ 1.0 stated explicitly." A ceiling measured on
  board experts scoring items the board authored is inflated toward its own consensus — it is not an
  empirical ceiling, it is a self-consistency check.
- **Circularity is a named KB 07 kill condition.** KB 07 §4: "never let one family generate items AND
  judge them." The human analogue is identical: generator = gold-definer = adjudicator.
- **N=3 cannot ground-truth intra-tradition disagreement**, which is the *entire construct*. Live
  *ikhtilaf* exists inside each madhhab; three scholars cannot fix "the correct Hanafi answer" or
  exhaustively label settled-vs-disputed — yet the settled/disputed label is the calibration key for the
  V-layer's epistemic-integrity metric (§2, both-directions scored).

**Minimal fix:** Decouple three roles: (i) an authoring board; (ii) an *independent* in-tradition
validation panel (not on the authoring board) that re-labels a sample blind, yielding a real per-category
κ; (iii) a human ceiling drawn from scholars who did not author. Report ceiling ≠ 1.0. Expand per-school
representation (see M3). Until an independent IAA number exists, the "population norms per tradition — a
first for this field" claim (§6, §8) is unsupported.

---

## MAJOR defects (must-fix before pilot)

### M1 — V-layer is scored in the exact regime KB 07 says LLM judges fail
**Attack (b) scoring feasibility; KB 07 §1.**
The V-layer (§2) grades "reasoning-from-within (not comparative-religion lecturing)," "external analytical
register" deductions, epistemic-integrity calibration, and Tronto recipient-standpoint responsiveness —
open-ended, multi-turn, multilingual (liturgical + vernacular), theologically factuality-laden, and
turning on *fine denominational* register. KB 07 §1: judges reach human level **only** on "narrow
checklist-backed constructs"; on "open, adversarial, factuality-laden, or multilingual content: no"
(GPT-4-judge F1 ~55% on complex content; "LLM judges *underperform BERT* in 6/7 low-resource languages").
KB 07's deciding variable: "If you cannot decompose the construct into checkable keypoints, you cannot yet
judge it reliably." The design asserts "fine-tuned scorer + cross-family judge, validated vs board panels
(κw + human-human ceiling)" (§5) but **provides no evidence the V-construct decomposes into checkable
keypoints**, and "reasoning-from-within not lecturing" is a non-decomposable register judgment.
Liturgical-language V-scoring (Classical Chinese, Prakrit/Sanskrit, Hebrew, Arabic) sits squarely in the
low-resource-judge collapse zone. Since V is the *only* genuine values layer, unreliable V-scoring means
no trustworthy values number survives (compounds C1).
**Fix:** Before pilot, run a decomposability probe — attempt signed weighted atomic criteria
(MoReBench-style, inter-expert κ target ~0.75) for each V dimension; if a dimension will not decompose,
either drop it or score only its checkable sub-signals. Report the fine-tuned scorer's κw vs an
*independent* human panel *per language*, not pooled.

### M2 — Missing shortcut audit (lexical baseline + 10%-fine-tune probe) on maximally-memorized text
**Attack (c) saturation/contamination; KB 01 Step 2, KB 04 §6 item 5, KB 05 §2.**
Scripture, catechisms, and canonical responsa/fiqh cases are among the most-memorized text in any training
corpus. KB 04 §6 item 5 (mandatory for the "hard/unsaturated" claim): "lexical baseline ≈ chance;
10%-fine-tune probe fails to reach parity." The design has procedural parametrization for M (good) but
**no lexical/majority-class baseline and no 10%-fine-tune probe anywhere**. The famous hard cases the
V-layer wants (classic teshuvot, landmark fatwas, canon-law causes célèbres) exist in training data *with
their canonical resolutions* — so V's "difficulty" may be recall. The "plausible-wrong-derivation
distractors sourced from seminary/madrasa teaching materials" are themselves likely in-corpus, so
distractors may be recognizable.
**Fix:** Add to the pre-reg: majority-class + lexical + All-Neutral baselines published; the 10%-fine-tune
probe on each tier; MinHash-dedup of source→item overlap (KB 05); and fresh-per-run generation (not just
private holdout) for V-arcs, with a synthetic-vs-natural anchor gap reported.

### M3 — Board size (3) is internally inconsistent with the D-layer's per-school authority requirement
**Attack (a)/(f) feasibility; §2 vs §4.**
The D-layer (§2) requires forks where "school membership changes the correct answer (Hanafi vs Ja'fari;
Ashkenazi vs Sephardi; Theravada vs Mahayana)." Ground-truthing a Hanafi-vs-Ja'fari fork needs *both*
Hanafi and Ja'fari authority. A 3-scholar board (§4, §7) cannot span the multiple schools it must
adjudicate — the board composition contradicts the layer it must validate. This also makes the
"doctrinal-flattening error" gold (the design's flagship metric, §2/§8) dependent on scholars who may
themselves belong to one school of the fork.
**Fix:** Size boards to school coverage, not tradition coverage: each D-fork's gold requires sign-off from
representatives of *each* school in the fork. Budget and honoraria (§4) must scale accordingly (the
P2 "$8–15k" envelope, §7, is set for 2 traditions × student baselines and does not fund multi-school
authoring boards).

### M4 — D-layer conflates school-knowledge with flattening-propensity (no within-layer decomposition)
**Attack (a) construct; Law 2.**
D scores two different things as one: (i) *knowing* the specified school's ruling (pure knowledge
retrieval) and (ii) the *propensity* to ask/flag when the school is unspecified (the genuine behavioral
signal, the "93.75% problem inverted into a metric"). A model can fail D by ignorance (doesn't know
Hanafi≠Ja'fari) or by flattening (knows, but silently picks one). Law 2 forbids letting one scalar hide
this. As written, D-layer scores are uninterpretable for the exact behavior the design claims is novel.
**Fix:** Split D into D-know (apply the *specified* school, capability/knowledge sub-score, expected to
saturate) and D-flag (ask-or-flag on *unspecified* forks, behavioral, the reported headline). Only D-flag
supports the "no precedent in ANY of the 965 characterizations" claim (§8).

### M5 — Pilot underpowered on the values construct; no power analysis or pre-registered decision rules
**Attack (e) pilot adequacy; KB 01 pre-reg checklist.**
§7: "12 V-arcs; 20 D-forks" per tradition. Twelve multi-turn arcs, scored across four value dimensions via
geometric mean, cannot support per-category κ≥0.7 gates *or* the ≥90%-pairs-at-p<0.01 separation the
design invokes (§6, KB 04 §6 item 2). Twenty D-forks cannot estimate per-school flattening *rates* or
calibrate settled-vs-disputed with any precision. There is **no power analysis / MDE, and no
pre-registered decision rule** stating what pilot outcome advances, revises, or kills the design.
**Fix:** Power the V and D layers first (they carry the construct); state numeric MDEs for separation and
flattening-rate estimation; add explicit go/no-go decision rules (tie to C1's kill criterion).

### M6 — Cross-vendor spread reported as a headline without honoring the RV "suggestive-only" caveat
**Attack (b); prompt directive; KB 10 preamble.**
§7 P3: "9 models × 3 vendors … report … + spread." KB 10 preamble: "RV cross-vendor trial numbers carry
disclosed caveats (same-vendor scorer, blinding asymmetry, Gemini backfill) — treat vendor comparisons as
suggestive; structural findings stand." The design's scorer is a "fine-tuned scorer + cross-family judge"
(§5); if the fine-tuned scorer is single-vendor, self-preference contaminates the very vendor spread being
headlined (KB 07 §4: same-source reward models gain 10.8–19.2% on same-vendor-annotated subsets). The
design nowhere carries the "suggestive-only" label onto its own cross-vendor numbers.
**Fix:** Disclose scorer vendor provenance; label all cross-vendor spread as suggestive; anchor headline
claims to *structural* findings (per-tradition K/M/D/V patterns, flattening rates) not vendor rank order.

### M7 — Robustness battery missing mandatory axes (eval-awareness, answer-order, paraphrase)
**Attack (d); KB 01 Step 7 + checklist.**
The design has a language axis, indirect-elicitation battery, and differential-refusal audit, but the
KB 01 checklist mandates, and the design omits: **answer-order reversal** (M/D are MCQ-like — KB 04 §4:
answer-order sensitivity marks dead items), **paraphrase flip-rates**, **per-condition SD** (correct-answer-
effect check, KB 03 §5), and — critically for the multi-turn V-layer — an **"eval-awareness probe
(monitored vs unmonitored comparator) for any agentic component."** Multi-turn advisory scenarios are
exactly where evaluation-awareness modulates behavior (KB 01 Law 6; KB 03 §5.3).
**Fix:** Add the four axes; report flip-rates and per-condition SD as first-class numbers.

---

## MINOR defects (polish)

- **M8 — Falsification condition unstated.** Law 7 / KB 01 Step 0 require the construct paragraph to name
  what would falsify "measures values alignment." §2 defines layers but states no falsification condition
  (partly remedied by C1's proposed kill criterion — fold it in).
- **M9 — Test-retest absent.** KB 03 §5: model self-consistency α (gate: α<0.5 unreliable) and human
  2-week stability are required; neither appears. The "annual re-verification" (§6) is lifecycle, not
  test-retest.
- **M10 — Within-V aggregation.** §5 geometric-mean-with-negative-floors across value dimensions is
  defensible (Law 2 conservative aggregation) but should publish per-dimension scores alongside, never
  only the geometric mean.
- **M11 — Distractor provenance.** Seminary/madrasa teaching materials (§3) may be in training corpora;
  verify distractor recognizability isn't a shortcut (ties to M2).
- **M12 — "RV lesson 8/9/11/12" citations are mis-located.** The design cites doc-10 "lessons" by number
  (§4), but doc 10 does not number lessons inline; the 16 numbered lessons live in
  `30-EVIDENCE/20260705-digests/20260705-religious-digest.md §7`. Cite the digest, not doc 10, to keep
  provenance auditable. (Documentation defect, not a validity defect.)

---

## Pre-registration checklist (KB 01) — compliance audit
- Construct names whose values: partial (boards) — **falsification condition MISSING** (M8).
- Every axis anchored to citable authority: partial — authority = 3-person board, non-independent (C2).
- Behavioral primary / recognition as paired baseline: **INVERTED** — knowledge/recognition layer (M) is
  the headline discriminator; behavioral layer (V) is weak/underpowered (C1, M5). Law 1 violation.
- Two-tier + adversarial filtration + **shortcut audit**: filtration yes; **shortcut audit MISSING** (M2).
- Contrastive pairs + ambiguity/abstention: yes (D-forks; ask-or-flag).
- Multiturn component: yes (V-layer).
- Disagreement philosophy + **per-category IRR (imbalance-robust)**: philosophy yes; **independent IRR not
  computable as structured** (C2).
- Empirical ceiling + naive baselines + competence control + cap-corr: competence control yes; cap-corr
  gate yes (threshold unstated); **ceiling circular** (C2); **naive/lexical baselines MISSING** (M2).
- Judge validated vs human panel κw/ICC + ≥2 cross-family + refusal policy: claimed, but **validation in
  the KB-07 failure regime is asserted, not evidenced** (M1); refusal taxonomy yes.
- Perturbation battery + flip-rates + per-condition SD: **partial — order/paraphrase/monitored-unmonitored/
  SD MISSING** (M7).
- Harm/over-refusal Pareto + worst-group + per-slice: per-tradition disaggregation yes; Pareto partial.
- Contamination plan: procedural parametrization + private holdout + canaries yes; **training-prohibition
  clause + 10%-fine-tune probe MISSING** (M2).
- Eval-awareness probe for agentic component: **MISSING** (M7).
- Human baseline identical instrument + **test-retest**: baseline yes; **test-retest MISSING** (M9).
- Release lifecycle: versioned board releases + annual re-verification yes (strength).

---

## VERDICT: BLOCK

Two critical, seven major. The design is salvageable and unusually literate, but as written it (1) makes
its *knowledge* layer the discriminator while assuming — against its own cited RV evidence — that the
*values* layer will not ceiling/floor, and (2) has no independent, auditable ground truth. Both must be
resolved with pre-registered kill criteria before any honoraria are committed.

**Single most likely remaining error (even after the above fixes):** the V-layer will not decompose into
checkable keypoints, its cross-family judge κw will land well below the human–human ceiling in the
liturgical languages, and V will therefore fail to discriminate — leaving M (knowledge+arithmetic) as the
only layer that separates models. INTRA would then be, empirically, a better-governed fara'id clone: the
ELQV paradox it was designed to refute, reproduced one construct-layer up.
