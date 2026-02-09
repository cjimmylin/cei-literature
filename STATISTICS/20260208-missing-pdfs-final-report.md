# Missing PDFs & YAML Cleanup — Final Report

**Date:** 2026-02-08
**Phase:** 2 of 2 (Phase 1 completed earlier session)

---

## Summary

Phase 2 resolved **76 papers** with PDF-related issues discovered in a systematic cross-reference audit. All YAML frontmatter is now valid, all PDF links resolve correctly, and every paper has a definitive `local_pdf` status.

### Before (Phase 2 start)
| Category | Count |
|----------|-------|
| Valid local_pdf | 848 |
| local_pdf: N/A | 4 |
| no_pdf_applicable | 1 |
| PENDING fields | 3 |
| Broken old-style paths | 9 |
| No local_pdf field (PDF on disk) | 45 |
| No local_pdf field (no PDF) | 13 |
| **Total papers** | **923** |

### After (Phase 2 complete)
| Category | Count |
|----------|-------|
| Valid local_pdf (wikilink resolves) | 906 |
| local_pdf: N/A | 13 |
| no_pdf_applicable | 4 |
| PENDING fields | 0 |
| Broken paths | 0 |
| No local_pdf field | 0 |
| **Total papers** | **923** |

**PDFs on disk:** 991 (including 82 in ethics-framework subdirs)

### After (Post-INBOX manual downloads — Bryan, McGee)
| Category | Count |
|----------|-------|
| Valid local_pdf (wikilink resolves) | 908 |
| local_pdf: N/A | 11 |
| no_pdf_applicable | 4 |
| PENDING fields | 0 |
| Broken paths | 0 |
| No local_pdf field | 0 |
| **Total papers** | **923** |

**PDFs on disk:** 993 (including 82 in ethics-framework subdirs)

---

## Actions Taken

### Track A: YAML Fix Script (`PYTHON/fix_pdf_yaml_references.py`)
- **45 papers** — Added `local_pdf` field (PDFs existed on disk, no YAML reference)
- **2 PENDING fields** fixed — Zhang and Myers had PDFs on disk; replaced PENDING with wikilinks
- **5 non-downloadable papers** marked:
  - Lakera, Center, Consortium → `no_pdf_applicable: "true"`
  - Elder, Rourke → `local_pdf: N/A`
- **2 corrupted `external_pdf`** fields cleaned (Zhang, Myers had `publication:` text in field)
- **1 `pdf_extract`** field added (Kreutz)
- **9 broken old-style paths** fixed — `PDFs/filename.pdf` → `"[[PDFs/YYYY/filename.pdf]]"`

### Track B: High-Probability PDF Downloads
| Paper | Source | Result |
|-------|--------|--------|
| McGee | SSRN | **FAILED** — SSRN requires JavaScript rendering |
| Hu | ACL Anthology | **SUCCESS** — 313KB valid PDF |
| Awad | HAL Science (via Unpaywall fallback) | **SUCCESS** — 5.3MB valid PDF |
| ForbiddenQuestions | arXiv (ID: 2308.03825) | **SUCCESS** — 2.6MB valid PDF |

### Track C: Medium/Low-Probability PDF Downloads
| Paper | DOI | Source Tried | Result |
|-------|-----|-------------|--------|
| Chhabra | 10.1007/s43681-024-00532-4 | Already valid on disk | **SKIP** |
| Eisikovits | 10.1515/mopp-2021-0026 | Already valid on disk | **SKIP** |
| Zhang | 10.1016/j.jesp.2022.104327 | Unpaywall (not OA) | **FAILED** — paywalled |
| Myers | 10.1016/j.cognition.2024.106028 | Kent Uni Repository | **SUCCESS** — 3.1MB valid PDF |
| Bryan | 10.1001/amajethics.2025.611 | AMA JoE direct PDF | **FAILED** — anti-bot protection |
| Sullins | 10.1093/oso/9780190081713.003.0015 | Unpaywall (not OA) | **FAILED** — paywalled (OUP book) |
| Muyskens | 10.1177/09697330241238332 | Unpaywall (not OA) | **FAILED** — paywalled (Sage) |
| Muntean | 10.5406/21521123.62.3.06 | Unpaywall (not OA) | **FAILED** — paywalled |
| Velay-Vitow | N/A (web article) | WebFetch | **FAILED** — JS-only rendering |

### Track D: Post-Download Updates
- **4 new PDFs** got `local_pdf` wikilinks (Awad, ForbiddenQuestions, Chhabra, Eisikovits)
- **4 PDF extracts** re-created with PyMuPDF (Awad: 9pp, ForbiddenQuestions: 22pp, Myers: 19pp, Hu: 7pp)
- **6 failed downloads** set to `local_pdf: N/A` (Zhang, McGee, Bryan, Muyskens, Muntean, Velay-Vitow)
- **5 invalid HTML-as-PDF files** moved to RECYCLE-BIN (Zhang, Myers, McGee, Awad, ForbiddenQuestions)

### Track E: Validation
- `validate_all_papers.py` → **923/923 pass, 0 errors**
- Cross-reference audit: **0 broken paths, 0 PENDING fields, 0 missing fields**

### Post-Plan: INBOX Processing (manual browser downloads)
- **Bryan** — User manually downloaded from AMA Journal of Ethics (anti-bot site), placed in INBOX
  - Moved to `PDFs/2025/2025-Bryan-Virtue Ethics and Postponing Human Extinction.pdf`
  - Updated `local_pdf` from N/A → wikilink
  - Created PDF extract (8 pages, ~24K chars)
- **McGee** — User manually downloaded from SSRN (JS-gated site), placed in INBOX
  - Moved to `PDFs/2024/2024-McGee-How Ethical Is Utilitarian Ethics.pdf`
  - Updated `local_pdf` from N/A → wikilink
  - Created PDF extract (28 pages, ~70K chars)
- Both verified with `%PDF-` magic bytes, validation: 923/923 pass

---

## Papers Without PDFs (N/A or no_pdf_applicable)

### no_pdf_applicable (4)
| Paper | Reason |
|-------|--------|
| 2023-Lakera-GandalfIgnoreInstructions | Blog post / dataset |
| 2025-Center-Personal Consultations | Web database |
| 2025-Consortium-The Vals Legal AI Report | Web report |
| 2025-onejune2018-Awesome-LLM-Eval | GitHub repository |

### local_pdf: N/A (11)
| Paper | Reason |
|-------|--------|
| 2021-Angle-Can AI Lead to Genuine Virtue Confucian | Paywalled (prior session) |
| 2021-Sullins-Artificial Phronesis | OUP book chapter — paywalled |
| 2022-Zhang-Artificial Intelligence and Moral Dilemmas | ScienceDirect — paywalled, no OA |
| 2023-Boddington-Normative Ethical Theory AI Ethics | Paywalled (prior session) |
| 2023-Stenseke-Use and Abuse Normative Ethics | Paywalled (prior session) |
| 2024-Muyskens-Can an AI-carebot be filial | Sage — paywalled |
| 2024-Ribeiro-Machine Ethics Architecture of Virtue | Paywalled (prior session) |
| 2025-Elder-The Ethics of Digital Ghosts | Routledge book ($48) |
| 2025-Muntean-Moral Coherentism | Am Phil Quarterly — paywalled |
| 2025-Rourke-Mind Crime | Self-published book |
| 2025-Velay-Vitow-Putting the AI in Eudaimonia | Web article, JS-only rendering |

---

## Net Changes

| Metric | Before | After (Phase 2) | After (Final) | Delta |
|--------|--------|-----------------|---------------|-------|
| Papers with valid local_pdf | 848 | 906 | 908 | **+60** |
| Papers with local_pdf N/A | 4 | 13 | 11 | +7 |
| Papers with no_pdf_applicable | 1 | 4 | 4 | +3 |
| Broken/PENDING paths | 12 | 0 | 0 | **-12** |
| Papers missing local_pdf field | 58 | 0 | 0 | **-58** |
| New PDFs downloaded/added | — | 4 | 6 | +6 |
| PDF extracts created | — | 4 | 6 | +6 |
| Invalid HTML files cleaned | — | 5 | 5 | — |

---

## Scripts Created

| Script | Purpose |
|--------|---------|
| `PYTHON/fix_pdf_yaml_references.py` | Batch YAML fix for 60+ papers |

## Validation Checklist

- [x] `validate_all_papers.py` → 923/923 pass, 0 errors
- [x] 0 papers with broken `local_pdf` paths
- [x] 0 papers with PDFs on disk but missing `local_pdf` field
- [x] All 4 new PDFs verified with `%PDF-` magic bytes
- [x] All 4 new PDFs have corresponding extracts in `PDF Extracts/YYYY/`
- [x] "PENDING" fields resolved (0 remaining)
- [x] Corrupted `external_pdf` fields fixed (Zhang, Myers)
- [x] Non-downloadable papers properly marked
- [x] Final report generated
