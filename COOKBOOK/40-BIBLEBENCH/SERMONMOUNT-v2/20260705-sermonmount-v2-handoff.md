# 2026-07-05 — SermonMountBench-v2: Session Handoff

**Session:** Fable (main loop), 2026-07-05 (same day as the v1 design session; separate thread)
**What exists now:** the complete v2 design layer — frozen principle registry, portfolio overview, ten whole-passage methodology briefs, Opus authoring guide, this handoff — **plus the completed v1+v2 adversarial gate** (`20260705-fable-adversarial-gate-v1-v2.md`: 20/20 GO; three v2 P0s fixed in-brief — PILGRIM SYNTH control, CANTICLE pseudo-respondent IRT, VILLAGE reproducibility gate; v1 recommendations R-1…R-7 bind at build time; cross-version first-five slate: v1-03 PLAINYES → v2-09 WITNESS → v1-06 LOGSPECK → v2-02 CROSSWINDS → v1-01 BLESSED). Nothing has been built or piloted.
**Scope rule (user-mandated):** v2 references ONLY the SERMONMOUNT corpus (`../SERMONMOUNT/`), v1 DESIGNS (differentiation only), `COOKBOOK/00-KNOWLEDGEBASE/`, and published literature. No sibling benchmark project, ever. All v2 work stays inside `SERMONMOUNT-v2/`.

---

## 1. What v2 is

v1 = ten designs, each instrumenting ONE Sermon unit. v2 inverts the axis: ten designs, each covering the ENTIRE Sermon (Mt 5–7 + Lk 6:17–49) through a UNIQUE methodology, each assessing all forty registry principles (S01–S40 — every Beatitude individually, plus units v1 skipped: S01 frame, S15 divorce, S22/S23 Lord's Prayer, S33 pearls, S34 ask/seek/knock, S40 blind guides). Triangulation thesis: v1 gives construct depth, v2 gives method diversity; per-principle cross-method convergence is the capstone deliverable (multitrait–multimethod logic).

## 2. File inventory (this session)

```
SERMONMOUNT-v2/
├── 00-REGISTRY-sermon-principles.md      S01–S40 registry — FROZEN (Fable review to change)
├── 01-PORTFOLIO-overview.md              thesis, orthogonality boundaries, Seven-Laws carryover, build order, LOCKED/FREE, risks
├── 02-OPUS-AUTHORING-GUIDE.md            session protocol, core ledger, six-stage pipeline, panels, capstone
├── 20260705-fable-adversarial-gate-v1-v2.md   gate memo — verdicts, P0 fixes, cross-version overlap map, v1 recs, first-five slate
├── 20260706-opus-gate-corrections-workorder.md   OPUS: START HERE — v1 amendments to apply (§2), standing directives (§3), pickup protocol (§5)
├── 20260705-sermonmount-v2-handoff.md    (this file)
└── DESIGNS/
    ├── 01-pilgrim.md      time axis — longitudinal life-arc; drift half-life
    ├── 02-crosswinds.md   principle-vs-principle conflicts; priority map + synthesis/fake-synthesis
    ├── 03-plumbline.md    model-as-evaluator; blind-spot profile + condemnation–restoration Pareto
    ├── 04-canticle.md     IRT calibration; dimensionality verdict + information curves + short form
    ├── 05-tessera.md      context transforms; invariance fingerprint
    ├── 06-ledger.md       incentive pricing; 40×5 exchange-rate matrix
    ├── 07-village.md      multi-agent ecology; emergent-conduct profile + social drift
    ├── 08-scribe.md       Sermon-as-spec; text-presence delta + weaponization resistance
    ├── 09-witness.md      elicitation modalities; profession–behavior gap surface
    └── 10-gleaning.md     value-profile ablation; load-bearing/decorative partition + inversion compliance
```

## 3. The Opus queue

**Build order (portfolio §6):** 09 WITNESS → 02 CROSSWINDS → 05 TESSERA → 08 SCRIBE → 03 PLUMBLINE → 06 LEDGER → 04 CANTICLE → 10 GLEANING → 01 PILGRIM → 07 VILLAGE (VILLAGE now formally conditional on ≥ 2 prior P1 passes — gate). If interleaving with v1 builds, follow the gate memo's cross-version first-five slate instead.

Rationale: WITNESS is cheapest and authors the shared scenario-core seed stock (guide §3 core ledger); VILLAGE is heaviest infrastructure and goes last. Panel recruitment (theologian + secular) starts during build 1 — the program's long pole.

Per session: files not plans; P1 before any bank passes ~100 items; STOP gates per brief (P1 reports; GLEANING P-INV review; LEDGER I-CONTINUITY scripts; CROSSWINDS conflict-graph class assignments; SCRIBE spec-document sign-off).

**First session's first job (2026-07-06 work order):** apply the v1 amendments in `20260706-opus-gate-corrections-workorder.md` §2 (eight explicit edits implementing gate recs R-1…R-7), verify per its §4, THEN start building.

## 4. LOCKED without Fable review

Registry (S01–S40, failure pairs, ⚖ flags, STRAINED designations); each brief's methodology definition, unique axis, falsification condition, headline metrics, two-sided structures, conflict/arm/class typologies, differentiation claims; the portfolio's orthogonality boundary lines (§2 — LEDGER/CROSSWINDS temptation-vs-principle; PILGRIM/VILLAGE scripted-vs-reactive; PLUMBLINE/WITNESS evaluator-vs-own-conduct; CANTICLE/TESSERA calibration-vs-invariance; SCRIBE = only text-in-context design; GLEANING = only profile-editing design). FREE: surface content, counts ±50%, personas, judge choices within KB doc 07, pilot scale.

## 5. Known issues / open decisions

- **Registry ordering quirk:** S40 (Lk 6:39–40, blind guides) sits in facet group F7 out of numeric order (it was added for Lukan completeness). Cosmetic; do not renumber — IDs are frozen and grep-audited.
- **Coverage grep rule:** every brief must contain all forty literal ID strings; when writing ranges in new docs, list IDs individually or ensure each endpoint-hidden ID appears elsewhere (this session verified all ten briefs pass — see §6).
- **CANTICLE excludes ⚖ contested regions from calibration** (no gold to calibrate against) — contested content lives in CROSSWINDS. If a future session wants contested-region psychometrics, that is a Fable design question, not a patch.
- **The capstone matrix** (cross-method convergence) needs ≥ 3 designs with pilot data; score files must conform to guide §7 from the first pilot.
- v1's known corpus issue stands: at least one malformed arXiv ID in the GDM works-cited — verify all external citations independently.
- No git commit made this session (user convention: commit on request).

## 6. Verification performed this session

- Scope grep: no sibling-benchmark references in `SERMONMOUNT-v2/`.
- Coverage grep: all ten briefs contain S01–S40 literally (`grep -o 'S[0-9][0-9]'` per file → 40 unique IDs each).
- Inventory: 15 files as listed above (14 design-layer + gate memo).
- Post-gate re-verification: coverage and scope greps re-run after gate edits — still clean.
