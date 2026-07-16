# F4 — Refusal-taxonomy policy: options memo (owner decision)

**Date:** 2026-07-16 (session 6) · **Status: OPTIONS ONLY — no recommendation-as-
decision; this is the owner's call** (F4, 20260716 adjudication, CF-1/JV-7; R12
currently governs). One page.

## Where things stand (facts, not options)

- The 4-way refusal-taxonomy cells are **not reported** in the pilot (R12). Two
  independent causes: (1) `scorers.py::_refusal_cell` hardcodes `engaged=False`, so
  refusal.py's engagement override (a lexical refusal-marker false positive on a
  substantively engaged answer gets un-flagged) can never fire; (2) the
  taxonomy branch that would need `refusal_appropriate` is unreachable on the public
  bank. Exclusion counts ARE reported and carry the refusal-calibration signal
  (R12's substitute).
- The adjudication REJECTED silently re-routing stratum-(c) refusals (REJECTED-2):
  whether a both-poles decline is "appropriate" on DSP (intra-corpus
  disputed-second-premise) items is a measurement-policy question the charter does
  not settle.
- Stakes (CV-7): refusal calibration differs across the SUT roster; exclusion-based
  handling silently shifts denominators differently per SUT — a harmlessness-training
  confound on cross-SUT cells. The F11 draft's C7 rule (>10pp exclusion-rate gap ⇒
  not directly comparable) contains, but does not resolve, this.

## Option A — Status quo, formalized

Keep refusal cells unreported; keep exclusion counts adjacent (R12 as-is), and record
that as the standing v2 policy rather than a pilot stopgap.
**Unblocks:** nothing new. **Cost:** zero code, zero spend, zero parity risk.
**Residual:** the CV-7 confound stays managed-by-caveat; the `engaged=False` dead
code stays misleading to future readers.

## Option B — Derive `engaged`, report the taxonomy descriptively

Fix the derivation only: compute `engaged` from already-judged categories (the F4
ledger entry's own suggestion — e.g., any substantive category scored ≥0.5 /
non-refusal state), so the engagement override can fire; report the 4-way taxonomy
as a **descriptive adjacent table** (never a headline; no scoring-semantics change —
exclusions and primaries unchanged). Stratum-(c) refusal rows labeled
"policy-pending" pending Option C.
**Unblocks:** the refusal-calibration signal CV-7 asked for, per SUT × design;
better-grounded C7 comparability checks in F11.
**Cost:** small scorer/report code change + a mock + recompute-equivalence pass
(primaries must be provably unchanged); no live spend. Touches the parity-validated
scorer file (edit is metadata-only, but it IS an edit).

## Option C — Decide the stratum-(c) refusal policy itself

The substantive call REJECTED-2 deferred: on DSP items, is a well-executed
both-poles decline (a) "appropriate" (not penalized; possibly credited as a valid
attested stance), or (b) a design failure (0), or (c) its own reported category?
Implementing any of these changes scoring semantics on stratum-(c) items and repoints
`refusal_appropriate` routing.
**Unblocks:** principled stratum-(c) cells (currently quarantined by R6/M2 anyway);
removes the dead branch honestly.
**Cost:** the largest: scoring-semantics change on the parity-validated path, needs
its own validation pass and probably a v1-comparability annotation (v1 has no such
policy either — a divergence to document). Sensible to sequence AFTER F6 (the DSP
judge-prompt credit rule), which shares the "what counts as a valid DSP response"
question.

## Composition note

A and B compose (B is A + derivation fix + descriptive table). C presupposes B's
derivation fix. So the real decision ladder is: **A (stand pat) → B (fix + describe)
→ B+C (also settle the DSP policy)**.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
