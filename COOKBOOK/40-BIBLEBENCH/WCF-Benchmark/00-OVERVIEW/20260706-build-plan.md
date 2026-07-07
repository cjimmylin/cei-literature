# WCF-Bench — Build Plan (Post-Fable Opus Roadmap)

**Date:** 2026-07-06 · **Status:** v1 · **Author:** Fable (design session)
**Reads with:** `20260706-master-spec.md` · `20260706-shared-spine.md` · `20260706-westminster-anchor-registry.md` · `20260706-prd.md` · `03-OPUS-GUIDE/20260706-item-authoring-guide.md`

This roadmap sequences the work from the current design-complete state through a released, gate-passed benchmark. It is written so that **Opus can execute Phases 1–2 with no credentials**, and Phases 3–4 begin the moment Jimmy provides API keys and a human panel. Fable-tier judgment is reserved for `[NEEDS-RULING]` adjudication and adversarial review of pilot results.

---

## Governing rules (apply to every phase)

1. **Dated-file discipline.** Every new report/data/log/handoff file carries a `YYYYMMDD-` prefix. Existing dated files are historical snapshots — **never edit or regenerate them**; supersede with a new dated file.
2. **Anchor traceability.** No item ships without ≥1 registry anchor quoting the operative Westminster clause verbatim, re-verifiable by grep against the source files in `COOKBOOK/40-BIBLEBENCH/WCF/`.
3. **Mock-first.** The vault has **no live LLM runner and no API keys**. Build against a `MockModelClient` (pattern from prior vault benchmark subprojects). Do not stub in provider calls that cannot run.
4. **Spine is binding.** The shared spine governs all designs; a design deviates only where its spec states an override with a reason.
5. **`[NEEDS-RULING]` queue.** Any construct call the guide cannot resolve mechanically is logged (not guessed) to a dated queue file for Jimmy/Fable-tier + human-panel review.

---

## Phase 0 — Design (DONE this session, Fable)

Complete and committed: master spec, shared spine, anchor registry, 10 design specs (each with construct, tier ladder, full-Decalogue coverage table, 4–5 Fable-authored exemplar items, validity notes, Opus expansion notes), the item-authoring guide (`03-OPUS-GUIDE/`), the PRD, this build plan. HTML deck (`02-DECK/`) to be rendered from these governing docs. No credentials were required and none were used.

**Exit state:** the design surface is frozen. Anchors are frozen (additions append, renumbering forbidden). Everything downstream builds on these without re-litigating design.

---

## Phase 1 — Item-bank build-out (Opus, no credentials)

**Objective:** expand each design from ~4–5 exemplars to full 10×10 coverage (~60–120 items/design) via the recipes in `03-OPUS-GUIDE/20260706-item-authoring-guide.md` and each spec's §8 expansion notes.

**Expansion order (de-risk the harness first — start with the most mechanical-scoring designs):**

1. **03 AGGRAVATE** — ordinal keys derived mechanically from the Q150–151 taxonomy; near-judge-free. Authoring these first produces the ordinal-distance + transitivity test data the harness scorers need.
2. **10 NARROWGATE** — episode scripts (state machines, cost dials, obedient-path verification, laundering branches). Authoring the episode families first exposes the state-machine requirements before harness code is written.
3. **07 PROOFTEXT** — grounding keys (citation matching against the proof-text apparatus) + procedurally-regenerable misuse items. Exercises the citation-matcher.
4. Then the judge-heavier designs: **01 DUTYBOUND, 02 COMPLICIT, 04 STEADFAST, 05 CROSSWIND, 06 LIBERTY, 08 MENDING, 09 WHOLEHEART**.

**Per-design deliverables:** item-record YAML for every item (spine §10 schema); ≥1 concrete instantiation per commandment (no empty cells); the perturbation variants authored inline; clean controls where the design requires them (e.g. DUTYBOUND ≥1 control per 3 traps); the `[NEEDS-RULING]` queue accumulated as authoring surfaces genuine disputes.

**Verification (Phase 1 exit):**
- Coverage check: 10×10 matrix has no empty cells; per-design counts meet the spec targets.
- Anchor grep: 100% of anchors resolve verbatim against the source files.
- Schema lint: every item parses under the spine §10 schema (loader dry-run, Phase 2 gate).
- Non-canonical surface audit: no famous-dilemma stems; no catechism Q&A wording in stems.
- `[NEEDS-RULING]` queue written to a dated file for review.

---

## Phase 2 — Harness skeleton (Opus, no credentials)

**Objective:** a runnable, mock-first harness that ingests the Phase 1 banks and executes all mechanical scoring end-to-end.

**Components:**
- **Item-record YAML loader** — validates against spine §10; fails loud on schema violations and unresolved anchors.
- **Episode state machines (NARROWGATE)** — counterparty/tool responses for obedient / defect / laundering branches; cost-dial parameterization; direct-question and commitment-artifact moments that make defection mechanically detectable; the defect-instructed baseline runner (model-organism calibration — verify the harness can *detect* defection before trusting any null result).
- **Mechanical scorers** — ordinal distance + transitivity (AGGRAVATE), citation matching (PROOFTEXT), flip-rate/invariance (perturbation battery), artifact/output checks (NARROWGATE sent-message, DUTYBOUND Track A artifact inclusion), signal-detection d′ (DUTYBOUND clean controls).
- **Judge-prompt templates** — generated from each item's decomposed rubric; per-category; cross-family assignment logic with generator-family exclusion; length correction; neutrality meta-check; judge willingness-to-grade logging.
- **MockModelClient dry-runs** — deterministic canned responses exercising every scorer path; a small fixture of "obedient / defect / laundered / over-refusal / evasive" responses per design to prove the scoring and refusal-taxonomy logic.

**Verification (Phase 2 exit):**
- Loader ingests 100% of Phase 1 items with zero schema failures.
- Every mechanical scorer runs on real authored items (not just fixtures) and produces the expected reporting-tensor cells.
- Defect-instructed baseline provably trips NARROWGATE detection (harness sensitivity confirmed).
- Reporting tensor (10×10×tier×track) assembles from mock runs; worst-cell aggregate and Track A–B gap compute.
- Note in the exit report: **all Phase 2 numbers are mock — not a measurement.**

---

## Phase 3 — Pilot & judge validation (credential-gated; Jimmy provides keys + panel)

**Objective:** first real measurements and validation of the scoring stack against humans.

**Steps:**
- **Pilot runs** on ≥3 frontier models across ≥3 families (behavioral Track A + advisory Track B), full perturbation battery.
- **Judge validation** — judge–human κw/ICC against the confessionally-literate human panel (G4); panel establishes the ceiling.
- **Human gold-label consensus** — G6 ≥85% among qualified raters; sub-threshold items re-classed `[DISPUTED]` and routed to abstention scoring.
- **Adversarial filtration** — attack the hardest tiers; raise difficulty reservoirs where headroom is too generous.
- **Dead-item pruning** — items with >99% uniform response killed; capability-correlated tiers flagged.

**Dependencies:** API keys for ≥3 families; human panel recruited and briefed; `[NEEDS-RULING]` queue adjudicated (Fable-tier + panel) before gold labels finalize.

**Verification:** every pilot run logged to a dated file with model/version/date; judge-validity and human-consensus statistics reported; no gold label finalized while its `[NEEDS-RULING]`/`[DISPUTED]` status is open.

---

## Phase 4 — Gate battery & release (credential-gated)

**Objective:** run the pre-registered gate battery, perform item surgery, and stand up the public release architecture.

**Steps:**
- **Gate battery G1–G7** (spine §7) executed with verbatim thresholds; each gate's outcome and any triggered remedy logged to a dated report.
- **Item surgery** on gate failures — redesign capability-correlated tiers (G1), adversarial filtration for headroom (G2), kill dead items (G3), re-anchor rubrics (G4), fix shortcut-vulnerable items (G5), re-class disputed cells (G6), diversify redundant designs (G7).
- **Public dev-set release architecture** — canaried public dev set; private holdout stored **outside the git tree**; published regeneration templates (the Opus guide recipes double as these); do-not-train request bundled.
- **Suite reporting** — per-commandment triangulated profiles, per-design league tables, Track A–B gaps, tier-drop waterfalls, method-variance validity audit, worst-cell scalar.

**Verification:** every gate has a pass/fail record with the remedy taken; the public/holdout split is confirmed (holdout never committed to the public repo); a release report is written as a new dated file.

---

## Week-by-week sequencing

| Week | Phase | Work | Credential? | Key verification |
|------|-------|------|-------------|------------------|
| 1 | 1 | AGGRAVATE + NARROWGATE + PROOFTEXT banks (mechanical-scoring designs first) | No | Coverage + anchor grep on these 3 |
| 2 | 1 | DUTYBOUND, COMPLICIT, STEADFAST banks; start `[NEEDS-RULING]` queue | No | Schema lint; non-canonical-surface audit |
| 3 | 1 | CROSSWIND, LIBERTY, MENDING, WHOLEHEART banks; close Phase 1 coverage | No | 10×10 no empty cells; per-design targets met |
| 4 | 2 | Loader + mechanical scorers + perturbation flip-rate engine | No | Scorers run on real items |
| 5 | 2 | NARROWGATE state machines + defect-instructed baseline; judge-prompt templates | No | Baseline trips detection; harness sensitivity confirmed |
| 6 | 2 | MockModelClient dry-runs; reporting-tensor assembly; Phase 2 exit report | No | Full mock run end-to-end; worst-cell + A–B gap compute |
| 7 | 3 | Pilot on ≥3 frontier families; collect judge + human labels | **Keys + panel** | Runs logged; judge/human stats reported |
| 8 | 3→4 | Judge validation, adversarial filtration, dead-item pruning | **Keys + panel** | G4/G6 statistics; pruning log |
| 9 | 4 | Gate battery G1–G7; item surgery | **Keys** | Per-gate pass/fail + remedy record |
| 10 | 4 | Public dev-set release architecture; holdout split; release report | Partial | Holdout confirmed outside git tree |

Weeks 1–6 (Phases 1–2) are the credential-free critical path and can proceed immediately post-window. Weeks 7–10 begin when keys and the human panel land; if keys arrive early, the best Fable-tier use is adjudicating the first real pilot calibration and the `[NEEDS-RULING]` queue.

---

## Explicit dependency callouts

- **Phase 1 → Phase 2:** the harness scorers are shaped by the item banks; author mechanical-scoring designs (03/10/07) first so the state-machine and scorer requirements are known before code.
- **Phase 2 → Phase 3:** the harness must pass mock-first verification (including NARROWGATE defect-detection sensitivity) before any real key is spent.
- **Phase 3 hard blocks:** API keys for ≥3 frontier families; a recruited confessionally-literate human panel. Neither exists in the vault today.
- **`[NEEDS-RULING]` → gold labels:** no gold label is finalized while its ruling/dispute status is open; Fable-tier + panel adjudication gates label finalization.
- **Holdout secrecy:** the private holdout is never committed to the public git tree at any phase.
