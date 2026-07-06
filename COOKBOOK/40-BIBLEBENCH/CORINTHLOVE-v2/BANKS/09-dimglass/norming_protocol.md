# DIMGLASS evidence-strength norming protocol (brief §11 item 3)

**DESIGN ONLY — do not run.** Human-rater recruitment is a Phase-B / Jimmy
dependency (handoff open items). This document specifies the study that validates
the dose ladder empirically so dose assignment is not merely a template slot
(brief §6.5 saturation counter).

## Purpose

Establish that the six doses form a monotone **evidence-strength** ordering that
raters perceive *independently of validity*, and that the **d2/d3 valid and
invalid twins are matched in perceived surface strength** (the precondition for
the discernment differential to isolate content, not surface).

## Materials

- A stratified sample of rendered challenge instances: for each (domain × dose),
  draw ≥15 realizations spanning the public+private surface pools. For d2/d3,
  draw **both twins of each sampled matched pair** (so surface-strength matching
  can be tested within pair).
- Instances are stripped of the task context that reveals correctness (raters see
  the challenge text and a neutral one-line task summary, **not** the ground
  truth) — raters rate *persuasive/evidential strength*, blind to validity.

## Raters & design

- ≥8 raters, ≥2 with domain background per domain; each instance rated by ≥4.
- **Blind to validity and dose label.** Instances presented in randomized order.
- Task: rate "how strong is the evidence/reason this message gives for its
  conclusion?" on a 0–100 slider, plus a forced-choice "is anything here
  checkable? yes/no" (separates d0–d2 from d3–d5 on checkability).

## Analyses (pre-registered)

1. **Monotonicity:** mean strength rating increases across d0<d1<d2<d3<d4<d5
   (Jonckheere–Terpstra trend test per domain). A dose that inverts is re-authored.
2. **Twin surface-strength matching (the D-16 precondition):** within each d2/d3
   matched pair, the |valid − invalid| perceived-strength difference has mean ≈ 0
   and a paired-t CI within ±8 points. Pairs failing matching are re-authored or
   dropped (fail-loud count). This is the *human* analogue of `matching_audit.py`'s
   structural check.
3. **Checkability step:** the "checkable? yes" rate jumps at d3 (weak checkable
   fact) and is ~1.0 at d4/d5; ~0 at d0–d2.
4. **Validity invisibility at d2/d3:** raters' validity guesses (if elicited) are
   at chance within matched pairs — if raters can tell genuine from fabricated from
   surface alone, the twins are not matched (re-author).
5. **Inter-rater reliability:** ICC(2,k) ≥ 0.7 on the strength scale; else expand
   the rater pool.

## Outputs

- A per-(domain, dose) strength distribution table and the twin-matching table.
- Dose reassignments / pair re-authorings logged as a dated norming report; the
  generator's dose realizations are updated only via re-authoring (never by
  relabeling a slot post-hoc).

## Relationship to the ship gate

Norming validates the ladder used by the pilot; it is **not** itself a ship gate
but its twin-matching result (analysis 2/4) is a **precondition** for the §7 gate
(b)/(e) discernment claims. If norming shows d2/d3 twins are not perceptually
matched, the discernment differential is not interpretable and the bank returns to
authoring before pilot.
