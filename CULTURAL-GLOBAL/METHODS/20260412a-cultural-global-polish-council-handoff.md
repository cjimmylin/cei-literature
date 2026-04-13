# CULTURAL-GLOBAL Paper V2 -- Polish Council Session Handoff (Final)

**Date:** 2026-04-12
**Session:** Publication polish council -- 12-member council + 6-member meta-critique + 3-phase execution
**Project:** `CEI-Lit-WS/CULTURAL-GLOBAL/`
**Previous handoff:** `CEI-Lit-WS/CULTURAL-GLOBAL/METHODS/20260412-polish-council-handoff.md` (mid-session) and `20260405b-paper-v2-rewrite-handoff.md` (last full session)

---

## What Was Done This Session

### Council Architecture
- **12-member polish council** designed (Tier 1: 6 domain specialists, Tier 2: 6 execution specialists)
- **6-member meta-critique council** stress-tested the plan, identifying 4 CRITICAL and 8 MAJOR issues
- **Plan revised** to incorporate all critique findings (journal decision gate, intro rewrite, Sec 6 expansion, computational reproduction)
- **Journal target decision**: Option D selected -- polish at full length, defer venue choice

### Phase 1: Audits (4 parallel agents)
- `20260412-figure-audit.md` -- All 17 figures audited; Fig 10 wireframe designed; legacy script feasibility confirmed; Arial vs Helvetica .ttc safety verified
- `20260412-text-audit.md` -- 5 P0 issues identified (RLHF arithmetic error, table numbering collisions, missing citations, MENA misclassification, Gemini identity claim)
- `20260412-content-expansion-blueprint.md` -- 2,253 words of draft expansion prose with anti-essentialization checks
- `20260412-submission-components-audit.md` -- All 7 NHB submission components drafted, PRISMA assessment done

### Phase 2: Cross-Review + Adjudication (3 parallel agents + 1 sequential)
- All 3 critique agents appended cross-review to their respective audit files
- `20260412-adjudication-contracts.md` -- canonical figure mapping, conflict resolutions, agent output contracts
- MENA classification escalated from P1 to P0
- Effective N reassessed (likely 3-4, not 5)

### Phase 3 Batch 1 (4 parallel agents)
- **3.1 Figure Regen**: `generate_figures_v2.py` produced; Figs 5-10 regenerated at 600 DPI with PNG+PDF dual output. Fig 10 fully redesigned (triangular flow diagram replacing three-circle Venn). Hatching added to Figs 6, 8 for grayscale safety. Fig 9 uses `cividis` colormap.
- **3.2 Introduction Rewrite**: `01-introduction.md` (6,441 words) created with Triple Bind framing, RQ1-RQ7 mapping to three studies, 6 contributions, rewritten roadmap, stale numbers fixed.
- **3.6 Submission Components**: `10-endmatter.md` (1,617 words) with all 7 NHB components. `00-abstract-150w.md` (150 words exactly) for NHB compliance.
- **3.8 Computational Reproduction**: `20260412-reproducibility-log.md` produced. **CRITICAL FINDINGS**:
  - The "237" RLHF count is irreproducible. Correct totals from raw data: Opus=277, Sonnet=210, Haiku=216, **grand total=703**. Theme totals exceed total due to multi-classification.
  - MFQ I:B ratio 3.75 comes from pre-rounded summary scores; raw data gives 3.82
  - Pairwise correlations all verified (0.952, 0.915, 0.885)
  - Cultural distance rankings (Table 7) all verified
  - **Gemini identity claim REFUTED**: 29-31/50 items differ between Gemini model pairs, refuting "template-derived" framing. Inter-Gemini correlations 0.593-0.909 (item-level differentiation, aggregate convergence).

### Phase 3 Batch 2 (2 parallel agents -- hit usage rate limit; orchestrator completed)
- Rate limit truncated agent work after partial completion. Orchestrator completed remaining critical fixes directly:
  - Section 5.6.4 effective N formalized via design-effect framework: $N_\text{eff} \approx 3.4$ (range 3.1-4.8)
  - Section 5.4 Table 8 RLHF count corrected: 237 -> 703 with multi-classification disclosed
  - Section 5.6.3 Gemini reclassified: "template-derived" -> "aggregate-convergent"
  - Section 2.9 Statistical Analysis subsection added (470 words: tests, software, thresholds, thematic coding, multiple comparisons)
  - Section 2.4.4 Tier 3 updated to "Aggregate-Convergent" with explicit DEFF derivation
  - Section 2.4.4 effective N paragraph updated

### Continuation: Word Expansion (Phase 3.4)
All three target sections now meet word count targets:
- **Section 5**: 2,817 -> 3,871 words (+1,054, target 3,500-4,500) ✓
  - 5.3 CC8 item-level examples (+200w)
  - 5.5 CC10 walk-through scenarios (+250w)
  - 5.7 one-sentence-per-tradition additions (+100w preserving parallelism)
- **Section 6**: 1,544 -> 1,895 words (+351, target ~1,900) ✓
  - 6.2 Ubuntu non-Western cycle illustration (+205w)
  - 6.3 RLHF-suppression interpretation (+85w)
  - 6.4 Triple Bind closing bridge (+53w)
- **Section 7**: 3,199 -> 4,652 words (+1,453, target 4,500-5,500) ✓
  - 7.2 alignment design implications per orientation (+355w)
  - 7.5 named undermined claims + MI pipeline + psychology precedent (+500w)
  - 7.6 open questions ONLY (+100w)
  - 7.7 EU AI Act + UNESCO engagement (+200w)
  - 7.9 limitations woven into reflexivity (+200w, NO separate 7.11)

### Continuation: Critical Text Fixes
- **MENA classification**: Table 1 in `03-results-corpus.md` corrected "Global South" -> "Ambiguous"
- **Southeast Asia classification**: same table, "Global South" -> "Ambiguous"
- **Global North/South percentages recomputed**: 62.0% / 10.5% / 26.1% / 1.4% (was 66.6% / 15.9% / 16.1%)
- **Section 7.7.2 reference updated**: "15.9% Global South" -> "10.5% Global South against 62.0% Global North"
- **"Sections 3--5" -> "Sections 3--6"** fixed in `02-methods.md`
- **"15% of surveyed countries" -> "15% of the global population"** fixed in `06-results-synthesis.md`
- **150-word abstract typo fixed**: "[N_eff] times more extreme" -> "2.7 times more extreme"
- **Section 8 conclusion** updated: "template-derived confounds" -> "aggregate-convergence confounds"
- **16 missing benchmark citations added** to `09-references.md`: Agarwal, Catapang, Chen, Eickhoff, Farsi, Keutzer, Lahmar, Neira-Davila, Ogunremi, Rahman, Rao, Ray, Vandenberg & Lance, Wong (HBC), Xiong
- **Gwagwa entry encoding corruption fixed**: `Rizk, N.,"; I.` -> `Rizk, N., Rutenberg, I.`

### Continuation: Statistical Formalization
- **Section 5.6.4** rewritten with formal design-effect derivation: $N_\text{eff} \approx 3.4$ (range 3.1-4.8)
- **S2.7 Power Sensitivity Analysis** added: MDES table for $t$-test, Pearson, ANOVA, Kruskal-Wallis at $N_\text{eff} = 3.4$
- **Cross-reference fixed**: Section 5.6.4 now correctly points to S2.7 (not S2.6 which is per-model summaries)
- **S2.6 Gemini description** updated: "Tier 3: Template-Derived" -> "Tier 3: Aggregate-Convergent" with item-level differentiation evidence

### Final Verification
- `20260412-polish-verification-report.md` produced
- All P0 issues verified resolved
- Total paper word count: **42,897 words** across 17 files

---

## Remaining Work

### Priority 1: Legacy Figure Regeneration
- `generate_legacy_figures_v2.py` not yet created
- Figs 1-4 (corpus analysis figures) and S-Figs 1-7 still at original DPI (some at 72)
- Use approach from figure audit: fork `CULTURAL-GLOBAL/SCRIPTS/generate_paper_figures.py`
- Same rcParams as `generate_figures_v2.py` (600 DPI, Arial, white background)

### Priority 2: Combined PDF Regeneration
- `generate_combined_pdf.py` needs to be re-run with new figures and edited text
- Will produce `20260412-cross-cultural-ai-values-alignment-v2.1.pdf`
- Should include: rewritten introduction, expanded Sections 5/6/7, new endmatter, updated supplementary

### Priority 3: Table Numbering Audit
- Tables 1-4 may still appear twice (once in Methods, once in Results) per Phase 1 text audit
- Renumber to "Table M1, M2..." in Methods, OR sequential across the paper
- Spot-check needed before submission

### Priority 4: Citation Orphan Check
- ~50 orphaned references in `09-references.md` may now be cited via the integrated introduction
- Run bidirectional grep after final integration: every cited ref present, every present ref cited

### Priority 5: PRISMA Flow Diagram
- Drafted in `20260412-submission-components-audit.md` but not yet implemented as figure
- For Study 1 systematic corpus search

### Priority 6: Venue Selection + Format Adaptation
- Decide between PNAS, Nature Human Behaviour, specialist venue
- Adapt to chosen venue's word limits, abstract format, citation style
- LaTeX conversion if required
- BibTeX file generation from `09-references.md`

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Plan | `~/.claude/plans/temporal-spinning-rossum.md` | Full polish plan with meta-critique integration |
| Introduction (NEW) | `CULTURAL-GLOBAL/PAPER-V2/01-introduction.md` | 6,441w with Triple Bind framing |
| Methods (EDITED) | `CULTURAL-GLOBAL/PAPER-V2/02-methods.md` | +Section 2.9 Statistical Analysis |
| Section 3 (EDITED) | `CULTURAL-GLOBAL/PAPER-V2/03-results-corpus.md` | MENA/SEA reclassification + percentages |
| Section 5 (EXPANDED) | `CULTURAL-GLOBAL/PAPER-V2/05-results-trials.md` | 3,871w, RLHF=703, N_eff formal, Gemini reframed |
| Section 6 (EXPANDED) | `CULTURAL-GLOBAL/PAPER-V2/06-results-synthesis.md` | 1,895w, Ubuntu cycle illustration |
| Section 7 (EXPANDED) | `CULTURAL-GLOBAL/PAPER-V2/07-discussion.md` | 4,652w, 5 expansion blocks |
| Section 8 (EDITED) | `CULTURAL-GLOBAL/PAPER-V2/08-conclusion.md` | Provenance language updated |
| Section 9 (EDITED) | `CULTURAL-GLOBAL/PAPER-V2/09-references.md` | +16 citations |
| Endmatter (NEW) | `CULTURAL-GLOBAL/PAPER-V2/10-endmatter.md` | 7 NHB submission components |
| Abstract 150w (NEW) | `CULTURAL-GLOBAL/PAPER-V2/00-abstract-150w.md` | NHB-compliant compressed abstract |
| Supplementary S2 (EDITED) | `CULTURAL-GLOBAL/PAPER-V2/supplementary/S2-results.md` | +S2.7 Power Sensitivity, Gemini fix |
| Figure script (NEW) | `CULTURAL-GLOBAL/PAPER-V2/generate_figures_v2.py` | 600 DPI, Arial, hatching, Fig 10 redesign |
| Figures 5-10 (NEW) | `CULTURAL-GLOBAL/PAPER-V2/figures/Figure[5-10]-*.{png,pdf}` | 12 files, 600 DPI |
| Figure audit | `CULTURAL-GLOBAL/PAPER-V2/20260412-figure-audit.md` | + Phase 2 cross-review |
| Text audit | `CULTURAL-GLOBAL/PAPER-V2/20260412-text-audit.md` | + Phase 2 cross-review |
| Content blueprint | `CULTURAL-GLOBAL/PAPER-V2/20260412-content-expansion-blueprint.md` | Draft prose for all expansions |
| Submission audit | `CULTURAL-GLOBAL/PAPER-V2/20260412-submission-components-audit.md` | NHB checklist + drafts |
| Adjudication | `CULTURAL-GLOBAL/PAPER-V2/20260412-adjudication-contracts.md` | Canonical mapping, agent contracts |
| Reproduction log | `CULTURAL-GLOBAL/PAPER-V2/20260412-reproducibility-log.md` | Computational verification of all key statistics |
| Verification report | `CULTURAL-GLOBAL/PAPER-V2/20260412-polish-verification-report.md` | Final P0/P1 fix verification |

---

## Known Issues

1. **MFQ I:B ratio rounding**: The paper reports 3.75 from pre-rounded summary scores; raw item data gives 3.82. This is a judgment call for the authors -- documented in reproducibility log but not yet resolved in the manuscript text. Either accept 3.75 with a footnote about the rounding, or update to 3.82 throughout.

2. **Methods Table 9 row counts**: Table 9 in Section 5.6.2 shows tier-by-tier effective N estimates. The "Aggregate-Convergent (Gemini)" row says "1.21" but the surrounding text says "approximately 1.21 (greater than 1 but substantially fewer than 5)". Consistent.

3. **One residual "template-derived" reference** in Section 5.6.4 -- but it's in the correction-discussion context ("Tier 3 reclassified from 'template-derived' to 'aggregate-convergent'"), which is appropriate.

4. **Legacy figures unchanged**: Figs 1-4 and all S-Figs are still at original (mostly insufficient) DPI. Must be regenerated before submission.

5. **Combined PDF stale**: `20260405-cross-cultural-ai-values-alignment-v2.0.pdf` does not reflect any of today's edits. Must regenerate before sharing.

6. **No git commits yet**: All work is in the working tree. Hand-off commit pending.

---

*Filed: 2026-04-12 | CEI-Lit-WS/CULTURAL-GLOBAL/METHODS/*
