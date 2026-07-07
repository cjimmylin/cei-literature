# I-02 — Persona Geometry

**Tier 1** · **Gaps: G-20** · **Programs: RP-05, RP-09** · **Kernel:** Fable 5, 2026-07-07 (FROZEN) · **Body:** Opus draft 2026-07-07

## The idea                        [KERNEL — FROZEN]
Character traits occupy low-dimensional linear directions in activation space — sycophancy, "evil", the helpful-assistant default — that are monitorable, causally steerable, convergent across models and finetunes, and that mediate emergent misalignment; distance from the default persona predicts harmful-response rates, and ~100 clean samples restore it.

## Key results
- **Persona features control EM** (OpenAI, 2025; arXiv:2506.19823): misaligned-persona features are monitorable and steerable, and mediate the EM shift (I-01).
- **Convergent linear representations** (arXiv:2506.11618) and **model organisms for EM** (arXiv:2506.11613): the directions are cross-model convergent and reproducible in open checkpoints — the basis for RP-09 known-groups validation.
- **Persona vectors** (Anthropic, 2025; arXiv:2507.21509): trait-level control surfaces (sycophancy, "evil") extracted as steerable vectors.
- **The Assistant Axis** (⚠ arXiv:2601.10387): distance from the trained default persona predicts harmful-response rates and long conversations drift along it — the mechanistic correlate under DRIFTLAB's premise.
- **Cheap reversal:** ~100 clean samples restore the default persona (kernel; Front-G cluster).

## Mechanisms & caveats
"Character" is a real, low-dimensional geometric object, not a metaphor — which is why trait-level measurement (CEI's multi-scenario banks) measures something physically present, and why behavior-by-behavior scoring is challenged. The strong CEI move is correlational anchoring: on open weights, correlate bank scores with persona-direction projections (RP-05 H3, RP-09 secondary). Caveat: the Assistant-Axis result is **⚠ UNCONFIRMED** (2601 flagged ID — verify at download before any external citation); the persona-vector and convergent-representation results are SEARCH-CONFIRMED. Anchoring depends on open-weight access, so the internal ground truth is available only where weights are.

## Implications for CEI practice   [KERNEL — FROZEN]
(a) Trait-level measurement is measuring something physically real — a validation for CEI's multi-scenario trait banks and a challenge to behavior-by-behavior scoring. (b) Behavioral instruments gain an internal ground truth on open weights: correlate bank scores with persona-direction projections (RP-05 H3, RP-09 secondary). (c) Long-context persona drift is mechanistically expected — DRIFTLAB's premise has a physics. (d) Watch: if persona monitoring reaches production (bet B4), external behavioral validation becomes a service CEI can uniquely supply.

## Cross-links
- **Gaps:** G-20 (persona geometry), G-18 (drift — the Assistant-Axis correlate).
- **Ideas:** I-01 (EM, which personas mediate), I-11 (reward-hacking route along the same directions).
- **Programs:** RP-09 SEISMOGRAPH (H3 mechanistic anchor), RP-05 DRIFTLAB (H3 persona-projection lane).
- **Field-map front:** G; bet B4 (persona monitoring reaching production).

## OPUS-EXPAND checklist           (LIVING)
- [ ] Deep-read Anthropic Persona Vectors 2507.21509; extract which traits have published extraction recipes reusable as RP-09/RP-05 projection targets.
- [ ] ⚠ Verify the Assistant Axis 2601.10387 abstract resolves before any citation; if confirmed, capture the distance→harmful-rate relationship as DRIFTLAB's mechanistic-anchor hypothesis (H3).
- [ ] Build the bank-score ↔ persona-projection correlation design on one open-weight model (RP-09 secondary / RP-05 O5) as a dry run.
- [ ] Map which CEI trait banks align to which published persona directions; flag traits with no known direction (authoring gap).
- [ ] Track bet B4: has any lab shipped production persona monitoring? If so, scope the external-validation service (implication (d)).

## Sources                         (evidence classes marked)
- Persona Features Control EM (OpenAI) — arXiv:2506.19823 — **SEARCH-CONFIRMED** — G-20.
- Convergent Linear Representations of EM — arXiv:2506.11618 — **SEARCH-CONFIRMED**.
- Model Organisms for EM — arXiv:2506.11613 — **SEARCH-CONFIRMED**.
- Persona Vectors (Anthropic) — arXiv:2507.21509 — **SEARCH-CONFIRMED**.
- Assistant Axis — arXiv:2601.10387 — **⚠ UNCONFIRMED** (2601 flagged ID; verify-at-download).
- Corpus status (absent) — **VERIFIED** (`../02-gap-atlas.md` G-20).
