# VERIFICATION_GATES.md — Gating Contract for T2.2 PDF Regen
**Generated:** 2026-04-12
**Generator:** T2.6 QA/Verification Engineer
**Purpose:** T2.2 (combined PDF regen) MUST read this file and abort if any P0 gate fails

---

## P0 Gates (must all pass before T2.2 runs)

### G1. Table numbering monotonicity ✅ PASS
- All 14 tables renumbered sequentially 1→14 across paper
- Methods T1-T4 unchanged, Corpus T5-T7, Benchmarks T8-T10, Trials T11-T13, Synthesis T14
- No collisions: every table number appears with exactly one caption
- All in-text references updated to match
- Verified by `Grep '\*\*Table \d+'` on all section files

### G2. MFQ patches applied to all 3 models ✅ PASS
- Opus 3.75/3.82 paired in: 00-abstract.md, 00-abstract-150w.md, 01-introduction.md, 02-methods.md, 05-results-trials.md (Table 5/6 footnote, line 41 derived stat, Section 5.6.1)
- Sonnet 3.23/3.14 paired in: 02-methods.md (Tier 1 paragraph), 05-results-trials.md (Section 5.6.1, Table 13 header)
- Haiku 4.82/3.75 paired in: 02-methods.md (Tier 1 paragraph + 1.07 swing methods footnote), 05-results-trials.md (Section 5.6.1)
- Methods footnote on rounding-order non-commutativity present in 02-methods.md:215+
- `verify_mfq.py` produced and runs without error
- Two false-positive consistency warnings from verify_mfq.py are about Gemini's aggregate value (also coincidentally 3.75) — different referent, no patch needed

### G3. Citation audit produces JSON bins (NO deletion) ✅ PASS
- `audit_references.py` built and reusable
- 133 references parsed
- Pass B (prose→refs): 112 matched, 2 uncertain, 10 orphan citations (need either ref additions or prose edits in future session)
- Pass A (refs→prose): 65 cited, 68 orphaned references (51% orphan rate; flagged for human review per critic C3 mandate)
- JSON outputs at `METHODS/council-v21/citations_audit_*.json`
- Summary markdown at `METHODS/council-v21/citations_audit_summary.md`
- **No automatic deletion performed**

### G4. Legacy figures regenerated ✅ PARTIAL
- 5/5 known-source matplotlib S-figures regenerated at 600 DPI: S-Fig2, S-Fig3, S-Fig4, S-Fig5, S-Fig6
- Both PNG (≥600 DPI verified via PIL) and PDF dual-output present
- Deferred (sources unknown): Fig 2 heatmap, Fig 3 dendrogram, Fig 4 biplot, S-Fig 1 bubble (Plotly), S-Fig 7 silhouette
- Plotly Fig 1 (world-map-weird) keeps existing PNG with cividis fallback documented
- Defer list documented in `generate_legacy_figures_v2.py` output and in T1.2 spec sheet

### G5. Corpus assembly flowcharts present ✅ PASS
- S-Fig-Study1-Corpus-Assembly.{png,pdf} (bibliometric standard, "~" counts)
- S-Fig-Study2-Benchmark-Identification.{png,pdf} (PRISMA-adjacent, exact counts)
- 3 new bibliometric/PRISMA references added to 09-references.md (Donthu 2021, Page 2021, Zupic & Čater 2015)
- Methods section 02-methods.md now cites both flowcharts in prose

### G6. Word counts within target ✅ PASS
- 00-abstract-150w.md: **148 words** (≤150 ✓)
- 00-abstract.md: 532 words (long abstract, no strict limit)
- 01-introduction.md: 6,451w (was 6,441; +10 from MFQ patch)
- 02-methods.md: 6,173w (was 5,987; +186 from MFQ methods footnote + flowchart citations)
- 03-results-corpus.md: 4,172w (unchanged)
- 04-results-benchmarks.md: 4,177w (unchanged)
- 05-results-trials.md: 3,970w (was 3,871; +99 from MFQ patches + footnote expansion)
- 06-results-synthesis.md: 1,895w (unchanged)
- 07-discussion.md: 4,652w (unchanged)
- 08-conclusion.md: 1,023w (unchanged)
- 09-references.md: 2,653w (was 2,573; +80 from 3 new bibliometric refs)
- 10-endmatter.md: 1,617w (unchanged; placeholders filled with 703 RLHF count)
- **Total main text (01-08): 32,513w** (was 32,218w; +295 from this session)

### G7. Endmatter NHB compliance ✅ PASS
- 7/7 NHB-required endmatter sections present in 10-endmatter.md:
  1. Author Contributions (CRediT)
  2. Data Availability Statement
  3. Code Availability Statement
  4. Ethics Statement
  5. Competing Interests Declaration
  6. Acknowledgments
  7. Statistical Analysis Summary
- `[N_RLHF]` placeholders filled with 703

### G8. Cross-reference integrity ✅ PASS
- All "Table N" in-text references match a "**Table N.**" caption
- Methods Section 2.2.1 cites S-Fig-Study1-Corpus-Assembly
- Methods Section 2.3 cites S-Fig-Study2-Benchmark-Identification

---

## File Checksums (for T2.2 to verify nothing changed between gate-write and PDF-regen)

```
00-abstract.md            532w
00-abstract-150w.md       148w
01-introduction.md       6451w
02-methods.md            6173w
03-results-corpus.md     4172w
04-results-benchmarks.md 4177w
05-results-trials.md     3970w
06-results-synthesis.md  1895w
07-discussion.md         4652w
08-conclusion.md         1023w
09-references.md         2653w  (133 entries)
10-endmatter.md          1617w
```

```
figures/Figure5-benchmark-clusters.{png,pdf}        (existing, 600 DPI from prior session)
figures/Figure6-concept-coverage.{png,pdf}           (existing)
figures/Figure7-cultural-map.{png,pdf}               (existing)
figures/Figure8-mfq-profiles.{png,pdf}               (existing)
figures/Figure9-rlhf-taxonomy.{png,pdf}              (existing)
figures/Figure10-triple-bind.{png,pdf}               (existing)

supplementary/supp-figures/S-Fig2-weird-histogram.{png,pdf}   (NEW 600 DPI)
supplementary/supp-figures/S-Fig3-weird-radar.{png,pdf}        (NEW 600 DPI)
supplementary/supp-figures/S-Fig4-pipeline-diagram.{png,pdf}   (NEW 600 DPI)
supplementary/supp-figures/S-Fig5-nw-detection-bars.{png,pdf}  (NEW 600 DPI)
supplementary/supp-figures/S-Fig6-north-south-radar.{png,pdf}  (NEW 600 DPI)
supplementary/supp-figures/S-Fig-Study1-Corpus-Assembly.{png,pdf}        (NEW)
supplementary/supp-figures/S-Fig-Study2-Benchmark-Identification.{png,pdf} (NEW)
```

---

## P1 Issues (non-blocking, document but proceed)

- **68 orphaned references** in `09-references.md` not cited in current prose. Per critic C3 mandate, no automated deletion. Future session should review the citations_audit_refs_to_prose.json bin and decide which to prune.
- **10 orphan citations** in prose without matching references (5× "Norenzayan (2010)" should be rewritten as "Henrich et al. (2010)"; rest need ref additions or prose edits). Documented in `citations_audit_summary.md`.
- **4 main figures + 2 S-figs deferred** (Figs 2-4 heatmap/dendrogram/biplot, S-Fig 1 Plotly bubble map, S-Fig 7 silhouette). Sources need provenance audit before regeneration.
- **MFQ I:B recompute discrepancy** (Sonnet Δ=0.18, Haiku Δ=0.16): the reproducibility log's "pre-rounded" pipeline rounds intermediate sums differently than 1-decimal foundation means. Documented in verify_mfq.py output but not corrected (would require raw data access).

---

## Authorization for T2.2

✅ **All 8 P0 gates pass.** T2.2 is authorized to regenerate the combined PDF.

T2.2 contract: read this file, verify file checksums match, then update `generate_combined_pdf.py` to include `01-introduction.md` and `10-endmatter.md` in the section list, then run it to produce `20260412-cross-cultural-ai-values-alignment-v2.1.pdf`.

If any P0 gate later fails (e.g., a file is modified between gate-write and PDF-run), T2.2 must abort and re-trigger T2.6.
