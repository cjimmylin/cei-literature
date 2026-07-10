# CULTURAL-GLOBAL Paper V2.1 — Council Session Handoff

**Date:** 2026-04-12/13
**Session:** Submission-readiness council (12 experts + 6 critics + staged execution)
**Project:** `CEI-Lit-WS/CULTURAL-GLOBAL/`
**Previous handoff:** `METHODS/20260412a-cultural-global-polish-council-handoff.md`

---

## What Was Done This Session

### Council Architecture
- **12-member council** designed (6 Tier-1 strategy + 6 Tier-2 execution)
- **6-member meta-critique** stress-tested plan before dispatch, finding **5 CRITICAL issues**:
  - Plotly figures can't be hatched → cividis fallback
  - Fuzzy citation regex has 15-20% FP rate → staged JSON bins, NO auto-deletion
  - "Modified PRISMA" is PRISMA-washing → reframed as "Corpus Assembly Flowchart"
  - MFQ rounding affects ALL 3 models (Haiku 1.07 swing) → scope expanded from 4-6 → 9-12 locations
  - Wave 1 file collisions on 3 files → serialized T2.3 → T2.4 → T2.5
- All 5 CRITICAL issues resolved before execution

### Phase A: 6 Tier-1 Planning Memos
All produced and filed in `PAPER-V2/METHODS/council-v21/`:
- T1.1 venue readiness memo (32,218w main / 133 refs / 23 figs; NHB 29-39h, PNAS 22-32h, specialist 9-14h)
- T1.2 figure spec sheet (S-Fig provenance matrix, rcParams, Nature column widths)
- T1.3 citation audit spec (9 prose forms + 8 edge cases; 3-bin JSON design)
- T1.4 corpus flowchart spec (bibliometric + PRISMA-adjacent; data blocks + captions)
- T1.5 MFQ patch map (exhaustive 12-location per-model patch list with draft prose)
- T1.6 format readiness gap (measured per-venue conversion costs)

### Phase B: Adjudication
- Single-pass adjudication (meta-critique findings already baked into Tier-1 mandates)
- 0 unresolved CRITICAL issues → Phase C authorized

### Phase C Wave 1a: Legacy Figures (T2.1)
- `generate_legacy_figures_v2.py` created — wrapper that imports legacy matplotlib functions with v2 rcParams
- **5/5 known-source S-figs regenerated at 600 DPI** (PNG + PDF dual output)
- **6 deferred:** Figs 2-4 (unknown sources), S-Fig 1 + Fig 1 (Plotly), S-Fig 7 (unknown)

### Phase C Wave 1b: Serialized Text Edits
1. **T2.3 table renumber:** 14 tables renumbered 1→14 across paper; Methods-T4/Results-T4 collision resolved
2. **T2.3 citation audit:** `audit_references.py` built (handles 9+ APA citation forms); 133 refs, 65 cited, 68 orphaned (flagged, NOT deleted)
3. **T2.4 MFQ patch:** Report-both applied to Opus/Sonnet/Haiku (12 locations across 6 files); methods footnote; `verify_mfq.py` ships as reproducibility deliverable
4. **T2.5 endmatter:** 150w abstract compressed to 148w; `[N_RLHF]` filled with 703; internal consistency confirmed

### Phase C Wave 2: Flowcharts + PDF
5. **T2.6 flowcharts:** `generate_corpus_flowcharts.py` → 2 supplementary figures (Study 1 bibliometric, Study 2 PRISMA-adjacent); 3 new refs added; methods section cites both
6. **T2.6 verification gates:** `VERIFICATION_GATES.md` emitted with 8 P0 gates, all passing
7. **T2.2 PDF regen:** `generate_combined_pdf.py` updated (v2.1 + intro + endmatter); `20260412-cross-cultural-ai-values-alignment-v2.1.pdf` produced (96pp, 3.4MB)

### Phase D: Verification + Handoff
- `20260412-v21-verification-report.md` filed; 0 P0 issues, 4 P1 issues documented

---

## Remaining Work

### Priority 1: Citation Cleanup
- **68 orphaned references** in 09-references.md need human review (citations_audit_refs_to_prose.json)
- **10 orphan prose citations** need either ref additions or prose edits (5× "Norenzayan" → "Henrich et al.")
- Use `audit_references.py` to re-verify after cleanup

### Priority 2: Deferred Figure Sources
- Figs 2-4 (heatmap, dendrogram, biplot): identify generator script or R source
- S-Fig 1 (Plotly bubble map): port to matplotlib if needed, or keep existing
- S-Fig 7 (silhouette): identify source

### Priority 3: Venue Selection
- T1.1 + T1.6 memos provide measured baselines
- Specialist venue (FAccT/JAIR/BD&S) = 9-14h conversion; NHB = 29-39h; PNAS = 22-32h
- Decision unlocks LaTeX/BibTeX conversion, reference pruning, word compression

### Priority 4: MFQ Foundation Means Reconciliation
- `verify_mfq.py` shows Sonnet/Haiku recomputed values differ from documented pre-rounded by 0.16-0.18
- Requires access to raw comparison-summary.json to resolve
- Not blocking — documented as P1

---

## File Locations

| File | Location (relative to PAPER-V2/) | Purpose |
|------|----------------------------------|---------|
| Plan | `~/.claude/plans/bubbly-crunching-micali.md` | Full plan with meta-critique integration |
| Council memos | `METHODS/council-v21/T1.[1-6]-*.md` | 6 Tier-1 planning memos |
| Adjudication | `METHODS/council-v21/adjudication.md` | Cross-memo consistency |
| Verification gates | `METHODS/council-v21/VERIFICATION_GATES.md` | Gating contract for PDF |
| Citation audit JSONs | `METHODS/council-v21/citations_audit_*.json` | Bidirectional audit bins |
| Citation summary | `METHODS/council-v21/citations_audit_summary.md` | Human-readable orphan report |
| Verification report | `20260412-v21-verification-report.md` | Final P0/P1 status |
| Combined PDF | `20260412-cross-cultural-ai-values-alignment-v2.1.pdf` | 96pp, 3.4MB |
| Scripts | `audit_references.py`, `verify_mfq.py`, `generate_legacy_figures_v2.py`, `generate_corpus_flowcharts.py` | Reusable utilities |

---

*Filed: 2026-04-13 | CEI-Lit-WS/CULTURAL-GLOBAL/METHODS/*
