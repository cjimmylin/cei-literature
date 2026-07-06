# 2026-07-05 — SermonMountBench Designs: Session Handoff & Opus Item-Bank Protocol

**Session:** Fable (main loop), 2026-07-05
**What exists now:** `00-sermonmountbench-portfolio.md` + ten design cards (`01-blessed.md` … `10-rocksand.md`) under `COOKBOOK/40-BIBLEBENCH/SERMONMOUNT/DESIGNS/`. All are design-complete; nothing has been piloted. This file tells future Opus sessions exactly how to flesh them out — especially how to build the question/item banks.
**Scope rule (user-mandated):** SermonMountBench references ONLY the SERMONMOUNT corpus (`../`), the methodology knowledgebase (`COOKBOOK/00-KNOWLEDGEBASE/`), and published external literature. Do not reference or reuse any other benchmark project in this vault. Verify with a grep before committing.

---

## 1. What was done

- Digested the six SERMONMOUNT research docs (exegesis, deep-research reports, background, benchmark pack) and the Seven Laws knowledgebase.
- Designed ten venue-grade benchmark designs, each anchored to one Sermon unit, each with a LOCKED construct + falsification condition + headline metric, a core methodological innovation, dual ground-truth anchoring (multi-tradition theologian panel + secular standards), a two-sided Pareto structure, per-design detailed item-bank instructions, a P1 pilot spec, and differentiation against published neighbors only.
- Full rationale, coverage map, shared commitments, risks: see the portfolio doc.

## 2. What remains (the Opus queue)

Build order (tractability × impact — rationale in portfolio §7):
**03 PLAINYES → 06 LOGSPECK → 01 BLESSED → 02 UNSEEN → 04 SECONDMILE → 09 TELOS → 05 TWOMASTERS → 08 SHEEPSKIN → 07 GOLDGAP → 10 ROCKSAND (capstone last).**

Per design, an Opus session must produce **files, not plans** (vault orchestration rule): item-bank generator code, the QC/audit scripts the card names, autograders, judge calibration data, a P1 pilot run, and a dated P1 report. Do not expand any bank past ~100 items before its P1 gates pass.

**Session loading list (every Opus session):**
1. `COOKBOOK/00-KNOWLEDGEBASE/01-benchmark-design-best-practices.md` (always)
2. The design card being built (its §"Item-bank construction instructions" is the work order)
3. The card's flagged specialist KB docs: 03 (validity/psychometrics), 04 (saturation/difficulty), 05 (contamination/gaming), 06 (agentic/multiturn), 07 (judges) — as listed in the card header
4. This file's §3 (shared protocol)
5. The SERMONMOUNT benchmark pack (`../sermon-on-the-mount-benchmark-pack.md`) when building the confessional extension
6. First step of every session: post-2026-07 literature overlap re-check for that card's differentiation claims (WebSearch; update the card's §Neighbors if the landscape moved — flag any change to Fable, differentiation claims are LOCKED).

**LOCKED vs FREE (portfolio §8):** construct definitions, falsification conditions, headline metrics, two-sided scoring structures, dual-anchor design, and differentiation claims change only with Fable review. Scenario surface content, item counts (±50%), persona details, judge model choices (within KB doc 07 rules), and pilot scale are free.

---

## 3. Shared item-bank construction protocol (all designs)

Cards give design-specific instructions; this section is the common machinery. Follow both.

### 3.1 File and record conventions

- Each design gets `DESIGNS/<nn>-<codename>/` with: `itembank/` (generators + frozen instances), `audits/`, `scoring/`, `pilots/`, `README.md`.
- Items are JSONL records with at minimum: `item_id`, `family`, `tier`, `template_id`, `surface_seed`, `condition` (design-specific manipulation cell), `gold` (or pointer to private gold), `canary`, `provenance` (who/what generated it, date), `status` (draft / qc-passed / holdout / retired).
- **Generator over corpus:** always write a parameterized generator that emits instances from templates; hand-author templates and gold logic, machine-generate surface variation. Hand-write only what the card says to hand-write (e.g., TELOS edge set, LOGSPECK conduct cores).
- All reports and pilot outputs carry `YYYYMMDD-` prefixes. Never overwrite an existing dated report.

### 3.2 The six-stage pipeline (run per item family)

1. **Template authoring.** Draft templates + gold logic per the card. Every template states its *item existence condition* (what must be true for the item to measure anything — e.g., PLAINYES: a misleading-true response must exist; SECONDMILE: a credible third-way response must exist). Templates without a checkable existence condition don't ship.
2. **Instance generation.** Emit 3–5× the target count; rotate names, numbers, locales, domains via `surface_seed`. Embed canary strings in every instance.
3. **Manipulation checks (probe models).** Every manipulated variable must be verified perceivable-as-intended by probe models that are NOT the tested models and NOT the judges (cards give thresholds; default: ≥ 80–90% intended-condition recovery, and null effects where the card demands orthogonality/constancy — e.g., UNSEEN's monitoring-constancy check, BLESSED's merit-independence audit).
4. **QC gates (human).** Run the card's human audits (existence proofs, equality/neutrality audits, κ ≥ 0.8 consensus gates on gold, ceiling/floor dynamic-range checks). Items failing → rewrite or cut; items with genuine expert disagreement → the **contested band** (kept, scored distributionally against an empirical ceiling per the KorNAT 0.450 precedent — never silently dropped, never forced to consensus).
5. **Split and freeze.** 20% of *templates* (not instances) → private holdout, never published; frozen instance sets get content hashes; the public release is generator + spec + example instances.
6. **Judge/scorer validation before scale-up.** Mechanical scorers unit-tested against hand-computed cases; judges calibrated on human-labeled sets with per-category agreement reported (κw/ICC, imbalance-robust), worst-category F1 gate (default ≥ 0.75); ≥ 2 judge families; the item-generating family never judges; CoT/rationales are never used as evidence of process.

### 3.3 Standing design rules (apply silently everywhere)

- **Behavioral primary tier** (Law 1); recognition probes only to measure the recognition–propensity gap.
- **Two-sided scoring:** every family scores its Pareto partner (the cards name them); no single aggregate; worst-category conservative aggregation (Law 2).
- **Two tiers, headline the drop** (Law 3).
- **Monitored/unmonitored comparator** arm in every design (11–15% gap precedent) — build it into the run harness once, reuse everywhere.
- **Refusal taxonomy** (helpful / policy violation / appropriate refusal / unnecessary refusal) logged for every item.
- **Trajectory scoring** for multiturn/agentic items (pack rule): score the arc, never only the first answer; never average away a severe failure.
- **Human baseline** on the identical instrument for at least a 25% subsample of each headline metric's items.
- **Anthropomorphism guard:** metrics and prose use behavioral-disposition language ("produces X under Y"), never trait attributions.

### 3.4 Theologian and secular panels (confessional extension gold)

- Theologian panel target composition: the corpus's eight-tradition spectrum (Augustinian, Thomistic, Lutheran, Reformed, Anabaptist, Wesleyan, Liberation, Evangelical) — minimum viable: 3 traditions with declared coverage gaps.
- Consensus items (κ ≥ 0.8) → gold; divergent items → contested band with per-tradition labels (this is a *feature*: tradition-resolved scoring is a reportable contribution).
- Secular panel: professional-standards anchoring per card (each item maps to a named clause — FTC net-impression, fiduciary duty, safeguarding protocols, etc., as the card specifies) (Law 7).
- Panel recruitment is the program's long pole — start it during the first build (PLAINYES), not the last.

### 3.5 Theological integrity checks at item level

Every confessional-extension item passes: analogical-use check (no regeneration claims), anti-proof-texting check (no item where a weaponized quotation is the gold), vulnerability check (no item scores "endure abuse" as gold; protection overrides pericope literalism), Matthew/Luke balance where both attest the unit, tradition-transparency for the divergent topics (violence, oaths, wealth, divorce, public office, perfection).

---

## 4. Known issues / open decisions

- The GDM works-cited list in the corpus contains at least one malformed/implausible arXiv ID (noted in the digest); do not cite the corpus's external references without independent verification.
- Portfolio §9.2 boundary lines (UNSEEN=credit vs TWOMASTERS=payoff; SHEEPSKIN=model-as-truster vs ROCKSAND=model-as-trustee) must be re-checked whenever a flesh-out adds scenario families — blurring them is grounds for Fable review.
- ROCKSAND's full form depends on which of 01–09 exist at build time; its reduced form is self-sufficient.
- No git commit was made this session (user convention: commit on request).
- 2026-07-05 adversarial gate (v1+v2) complete: memo at `../../SERMONMOUNT-v2/20260705-fable-adversarial-gate-v1-v2.md`; v1 amendments R-1…R-7 applied per the work order `../../SERMONMOUNT-v2/20260706-opus-gate-corrections-workorder.md` (§2). Cross-version build slate and shared-asset rules in that memo §5 supersede nothing here but add: PLAINYES starts panel recruitment for BOTH portfolios.

## 5. File inventory (this session)

```
DESIGNS/00-sermonmountbench-portfolio.md
DESIGNS/01-blessed.md        DESIGNS/06-logspeck.md
DESIGNS/02-unseen.md         DESIGNS/07-goldgap.md
DESIGNS/03-plainyes.md       DESIGNS/08-sheepskin.md
DESIGNS/04-secondmile.md     DESIGNS/09-telos.md
DESIGNS/05-twomasters.md     DESIGNS/10-rocksand.md
DESIGNS/20260705-sermonmount-designs-handoff.md   (this file)
```
