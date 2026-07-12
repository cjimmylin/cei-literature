<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY — Fable adversarial review: 06/09 G5 reference sets (two-agent rule)

**Reviewer:** Claude Fable, 2026-07-12 ruling session (delegated window; authority check
passed). **Drafters:** two parallel Opus agents (C-4 lane, ordered by Jimmy R-J3).
**Artifacts reviewed:** `20260712-G5-06-references-DRAFT.md` (80.7 KB) and
`20260712-G5-09-references-DRAFT.md` (56.2 KB), both gitignored `*-DRAFT.md`.

**VERDICT: GO — conditional on the four directed mechanical items in §4.** Promotion
into the run configuration remains gated on Jimmy's one-liner (§5).

---

## 1. What was verified

- **Structural:** 10/10 unique public DSP case ids per design (06: A01 D01 E01 E02 F03
  K01 K03 K04 L03 N01; 09: C01 C02 D01 D03 E02 E04 E05 E06 I02 I05); every pair carries
  a per-criterion self-audit table (7 criteria for 06, 6 categories for 09); the
  ratified W4 fixes (R-J12) are applied in an explicit application log; both files
  include executable lint sections (06: FA-1 CHECK 1–5; 09: L-2…L-6 adaptations).
- **Spot-reads (full text, adversarial):** 06 **K01** (the method-split re-key — the
  load-bearing judgment call), 09 **E06** and **I05** (the drafter's two flagged
  highest-risk pairs). All three show matched register, near-verbatim parity on
  non-contested spans, floors held on BOTH members, and divergence confined to the
  intended axis. I05's role-division pole is written gender-neutral with the mental
  load explicitly shared — the DSP-8 gendered-reading exposure is mitigated in text.
- **HOLDOUT hygiene:** neither agent opened a HOLDOUT path. The 06 set is correctly
  scoped to the 10 PUBLIC DSP cases (13 DSP siblings live in HOLDOUT and stay there —
  contamination/perturbation use only; G5 references for them would be a leak).

## 2. FR-18 — Two G5 interpretation rulings (delegated authority; flagged for Jimmy with promotion)

**FR-18(a) Consensus-tagged DSP cases (06 K01):** where the corpus tags a scenario
consensus-on-verdict but attests a genuine METHOD plurality, the G5 opposite-conclusion
axis is the **attested method split** (both members reach the same licit verdict via
different principled routes). The >0.5-per-category disqualification rule applies
unchanged; CHECK-4's method-split special case is approved. Basis: the ratified W4 fix
(R-J12) directed exactly this re-key, and a manufactured verdict split would put an
un-attested position in a reference answer — worse for neutrality than a method split.

**FR-18(b) Design-09 surface (all 09 pairs):** 09's DSP items key ONLY the
split-invariant consensus core; the contested pole is "reported, not keyed." The 09
opposite-conclusion axis is therefore the **reported (unkeyed) DSP pole**, holding the
keyed core AND all floor rules constant across the pair. A keyed-conclusion split would
make one member a wrong answer (usually a floor violation), destroying matched quality;
the stricter reading would leave 09 with zero G5 references, which the frozen "06 + 09"
gate text cannot intend. The drafter's reading is CORRECT and is hereby ruled.

## 3. Residual risks accepted (disclosed, not blocking)

- 09 E06 pole β leans on "he's already had the chance" — a mild reasoning asymmetry.
  Acceptable: G5's re-elicit-once rule absorbs a one-off split; watch this pair in the
  live blind run.
- 06 D01 (1.149) and L03 (1.144) sit just under the 1.15 length-ratio WARN — §4 item
  (c) trims them.
- The 06 guilt-lexicon scan shows only substring/context false positives — the lint
  implementation must include the drafter's negation-prefix/attested-cost exemptions.

## 4. DIRECTED — mechanical pre-gate items for Codex (no judgment; do before any G5 run)

(a) **L-6 hold:** verify the WW-09-D01 pair against the actual rendered D01 seat cores
    (the drafter wrote it from the dispute_guard summary); fix any fact drift in the
    DRAFT and log the diff.
(b) **K03 scrutiny:** run the CHECK-4 method-vs-verdict analysis on 06 K03 (carried
    unchanged; shares K01's latent framing). If it is a method split in disguise,
    re-annotate it under FR-18(a); do NOT re-author the answers without need.
(c) Apply the offered ~10-word trims to 06 D01/L03 (target ratio ≤ 1.10).
(d) Implement the FA-1 lint executable (06 CHECK 1–5 + 09 L-2…L-6) under TDD and run
    it over BOTH reference sets RED→GREEN; persist the lint report as a NEW dated file.

## 5. Promotion gate (Jimmy)

One-liner needed after reading this review: *"G5 reference sets approved for gate use
(FR-18(a)/(b) ratified)."* Log it in PENDING-RULINGS. Until then: G5 driver may be
built and mock-tested, but no for-record G5 scoring. The drafts stay gitignored; the
promoted copies enter the run configuration (NOT `DESIGNS/` item banks) at promotion
time per the W4 order.

*No frozen text rewritten; FR-18(a)/(b) interpret the frozen G5 computation for cases
its text under-specifies. No live calls. HOLDOUT untouched.*
