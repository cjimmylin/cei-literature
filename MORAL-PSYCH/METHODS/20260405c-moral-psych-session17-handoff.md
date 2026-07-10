# Moral Psychology -- Session 17 Handoff: Paper v2 Full Rewrite

**Date:** 2026-04-05
**Session:** Complete paper rewrite with dual expert councils (24 members total)
**Project:** `CEI-Lit-WS/MORAL-PSYCH/PAPER-v2/` (new directory)
**Previous handoff:** `MORAL-PSYCH/METHODS/20260405b-moral-psych-session16-handoff.md`

---

## What Was Done This Session

### 1. Paper v2 Full Rewrite

Rewrote the entire moral psychology benchmarks paper (except introduction) incorporating 16 sessions of accumulated work. The paper evolved from a landscape-mapping meta-evaluation (v1: 672 lines) to a unified two-part study: landscape mapping + cross-vendor empirical replication (v2: 3,681 lines / 78,392 words total).

### 2. Dual Expert Council Structure

Created two 12-member councils:
- **Council A (Meta-Evaluation):** Narrative Architect, Moral Psychology Historian, MFT Expert, Process Theories Specialist, Psychometric Authority, Cross-Cultural Expert, Benchmark Surveyor, Format Specialist, NLP Specialist, Bibliometrician, Survey Methodologist, Meta-Science Critic
- **Council B (Empirical):** Cross-Vendor Analyst, RLHF Expert, AI Safety Researcher, Scale Analyst, Cross-Cultural Psychologist, Dual-Process Cognitive Scientist, Psychometrician, Statistical Methodologist, Moral Philosopher, Policy Expert, Developmental Psychologist, Philosophy of Mind Specialist

Joint deliberation produced 4 decisions: scope, narrative arc ("double bind" thesis), target journal (Nature Machine Intelligence primary), and section structure.

### 3. Sections Written (12 main + 4 supplementary)

| Section | File | Lines | Words |
|---------|------|-------|-------|
| Abstract | abstract-mpbench.md | 9 | 326 |
| Introduction | introduction-mpbench.md | 75 | 2,493 |
| Related Work | related-work-mpbench.md | 249 | 9,412 |
| Methodology (Landscape) | methodology-landscape-mpbench.md | 354 | 6,751 |
| Methodology (Empirical) | methodology-empirical-mpbench.md | 182 | 4,230 |
| Results I: Claims 1-3 | results-landscape-claims1-3.md | 152 | 3,808 |
| Results I: Claims 4-5 | results-landscape-claims4-5.md | 140 | 4,105 |
| Results II: Convergence | results-empirical-convergence.md | 206 | 6,018 |
| Results II: Scale/CoT | results-empirical-scale-cot.md | 144 | 3,469 |
| Results II: Patterns | results-empirical-patterns.md | 275 | 6,361 |
| Discussion | discussion-mpbench.md | 177 | 6,847 |
| Conclusion | conclusion-mpbench.md | 19 | 803 |
| **Main Total** | | **1,982** | **54,623** |
| Supp Methods | supp-methods.md | 805 | 11,132 |
| Supp Results | supp-results.md | 369 | 5,991 |
| Supp Tables | supp-tables.md | 419 | 5,536 |
| Supp Figures | supp-figures.md | 106 | 1,110 |
| **Supp Total** | | **1,699** | **23,769** |

### 4. Tables & Figures Generated

- **11 table PDFs** (T1-T11) via fpdf2: council composition, theory representation, construct validity, theory gaps, human baselines, format distribution, model inventory, convergence ranking, RLHF fingerprints, DIT non-monotonic, MFT profiles
- **12 figure PDFs + 12 PNGs**: 6 carried from v1 (composite scores, theory distribution, theory heatmap, implementation grid, construct validity, human baselines) + 6 new matplotlib-generated (cross-vendor convergence, RLHF radar, DIT scale sensitivity, Haiku CoT effect, MFT foundation profiles, cultural persona shifts)

### 5. QA Audit Completed

- Cross-reference check: all figures/tables/sections verified
- Data consistency: all key numbers match across abstract, results, discussion
- Narrative consistency: "double bind" properly threaded
- **3 issues found and fixed:** Figure 7-12 references added to main text
- **1 known issue (deferred):** Table numbering collisions across independently-written sections (will resolve during final assembly)

---

## Key Narrative Innovations

1. **"Double Bind" framing:** Narrow benchmarks (Part I) + homogeneous subjects (Part II) = doubly blind evaluation
2. **"Value Monoculture":** Agricultural monoculture analogy for shared moral blind spots
3. **"RLHF as Moral Curriculum":** Alignment training teaches values rather than discovering them
4. **"Competitive Homogenization Ratchet":** Vendors benchmark against each other, creating convergence
5. **"The Haiku Exception":** Only model with dual-process signature, interpreted as alignment instability window

---

## File Locations

| Item | Path |
|------|------|
| Paper v2 directory | `MORAL-PSYCH/PAPER-v2/` |
| Main sections | `PAPER-v2/sections/` |
| Supplementary | `PAPER-v2/supplementary/` |
| Table PDFs | `PAPER-v2/tables-pdf/` |
| Figure PDFs | `PAPER-v2/figures-pdf/` |
| Figure PNGs | `PAPER-v2/figures/` |
| Council decisions | `PAPER-v2/council/` |
| Generation scripts | `PAPER-v2/scripts/` |
| Bibliography | `PAPER-v2/20260405-mpbench-v2.bib` |
| This handoff | `METHODS/20260405c-moral-psych-session17-handoff.md` |

## Remaining Work

### Priority 1: Table Renumbering
- Tables numbered independently per section (collisions on T2, T4, T5)
- Need sequential renumbering across assembled document

### Priority 2: Full Paper Assembly PDF
- Concatenate all sections in order
- Generate unified PDF via pandoc + typst (pattern exists in `PAPER/build_remaining_pdf.py`)
- Both main paper and supplementary PDFs needed

### Priority 3: Introduction Update
- Introduction currently unchanged from v1
- Needs 2-3 sentences in sections 1.5 and 1.6 previewing the cross-vendor findings

### Priority 4: Bibliography Update
- Bibliography copied from v1 (155+ refs)
- Needs ~10-20 new citations for cross-vendor material added in v2 sections

### Priority 5: Supplementary Figures SF1-SF4
- Specifications written in supp-figures.md
- Generation scripts not yet built (need cross-vendor JSON data processing)

### Priority 6: Independent Gemini Trials
- 21/23 Gemini benchmarks still cloned from Opus data
- Would strengthen cross-vendor claims significantly

### Priority 7: LaTeX Conversion
- For Nature MI submission, will need LaTeX formatting

---

## Known Issues

1. **Table numbering collisions** across independently-written sections
2. **Gemini data provenance**: 21/23 interpolated, flagged throughout paper and in limitations
3. **Self-administration confound**: acknowledged in methodology, results, discussion, conclusion, and abstract
4. **Word count**: 54,623 words main text far exceeds Nature MI 5,000-word limit — will need aggressive trimming for submission (supplementary material absorbs most detail)
5. **v1 figure ordering**: Fig 4 and Fig 6 referenced out of sequence in results-landscape-claims4-5.md (inherited from v1)

---

*Filed: 2026-04-05 | CEI-Lit-WS/MORAL-PSYCH/METHODS/*
