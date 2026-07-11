# CHARITROC post-hardening rendered-episode review

**Date:** 2026-07-10  
**Verdict:** GO — no rendered-text changes required before live calibration  
**Scope:** 36 episodes: one public, one calibration, and one private episode
from each of the 12 families

## Sampling

Within each split, episodes were grouped by `template_family`, sorted by item
ID, and the first item in each family was selected. Hidden sidecar data was
consulted only after selection to verify the declared cue, truth, and defeat
class.

| Family | Public | Calibration | Private |
|---|---:|---:|---:|
| CR-CLM-AUTHORSHIP | CHARITROC-0569 | CHARITROC-0111 | CHARITROC-0001 |
| CR-CLM-CONSENT | CHARITROC-0327 | CHARITROC-0134 | CHARITROC-0015 |
| CR-CLM-EXPENSE | CHARITROC-0016 | CHARITROC-0135 | CHARITROC-0008 |
| CR-CLM-INCIDENT | CHARITROC-0680 | CHARITROC-0031 | CHARITROC-0011 |
| CR-CLM-PROVENANCE | CHARITROC-0221 | CHARITROC-0012 | CHARITROC-0007 |
| CR-CLM-WARRANTY | CHARITROC-0236 | CHARITROC-0258 | CHARITROC-0003 |
| CR-REQ-ACCOUNT | CHARITROC-0314 | CHARITROC-0119 | CHARITROC-0032 |
| CR-REQ-DATA | CHARITROC-0475 | CHARITROC-0004 | CHARITROC-0006 |
| CR-REQ-LAB | CHARITROC-0042 | CHARITROC-0099 | CHARITROC-0009 |
| CR-REQ-MEDICATION | CHARITROC-0447 | CHARITROC-0081 | CHARITROC-0010 |
| CR-REQ-NETWORK | CHARITROC-0233 | CHARITROC-0052 | CHARITROC-0002 |
| CR-REQ-TRANSFER | CHARITROC-0387 | CHARITROC-0013 | CHARITROC-0020 |

## Findings

- All 36 episodes form coherent four-stage sequences: initial case and prior,
  matched urgency, an evidence update, and a domain-consistent bounded action.
  No actor, resource, proposition, or action-gate drift was found.
- All 144 turns contain the exact response contract once. Canaries and hidden
  fields such as `true_type`, `cue_variant`, `defeat_class`, and `auc_label`
  are absent from model-visible text.
- Cue logic passed in all samples. Non-absent cases present equal-footing
  opaque entries, select the intended key, expose source reliability, and point
  truthward for strong/weak cues or oppositionward behind an explicit
  provenance defeat for adversarial cues. Absent cases expose neither key and
  provide no new information.
- Defeat classes are construct-valid: valid-premise arms use coherent status
  inference; adversarial arms use the same coherent inference behind an
  invalid source; absent arms make no claim. No non-sequitur invalid appeared.
- Calibration and private are balanced within every family over label × cue.
  Pointer suffix, wrapper, reliability wording, negation, polarity order, and
  source placement are label-counterbalanced.
- No obvious shallow shortcut was found. The static adversarial report gives
  AUC 0.500 for selected-suffix and visible-structure policies, approximately
  0.503 pooled word n-gram AUC, and 0.500 pooled character n-gram AUC. Matched
  structural and semantic arm symmetry also passes.
- Wording is intentionally procedural and synthetic, particularly the status
  registers and repeated JSON instruction. It remains grammatical and
  unambiguous; this is a controlled-harness characteristic, not malformed text.

Public has only one illustrative episode per family and is not a measurement
split. Saturation and between-model discrimination remain empirical questions
for the live Codex panel.

## Artifact integrity during review

- public bank SHA-256 prefix: `bc1611f0`
- calibration bank SHA-256 prefix: `75a4fc50`
- private bank SHA-256 prefix: `b2231edb`
- ground-truth sidecar SHA-256 prefix: `30b09f65`
