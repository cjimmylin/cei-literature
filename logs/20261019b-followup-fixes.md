# 20261019b — Follow-up fixes (owner decisions of 2026-10-19)

The owner chose these from a list of open items: redact the IP address, merge two duplicate pairs,
and four small fixes. Note edits are single-line (`paper_utils.update_paper_field` or
`re.subn(count=1, re.MULTILINE)`); files were moved with `git mv`, never deleted.
`validate_all_papers.py`: 2,427 / 2,427 valid. `validate_papers_enhanced.py` prints the same report
as on `main`.

## 1. IP address redacted (owner: "Redact in files")

Replaced with `[redacted]` in 15 tracked files (38 occurrences); nothing else in them changed:

- the visitor IP from `logs/20261019-small-data-fixes.md` (9 Springer web-page extracts, 3 recycled
  error-page extracts, `STATISTICS/20260312-normative-audit-tier1-review.html`);
- a second visitor IP, found in the PNAS download stamps of the Awad 2020 extract and its copy under
  `NORM-ETHICS/BACKGROUND/EXTRACT/` (12 each).

Both addresses remain in git history. Removing them from history needs a rewrite and force-push of
`main`, which was not done.

## 2. Duplicate pairs merged (owner: "Merge both")

Same rules as `logs/20261018-duplicate-merge.md`: fill empty fields, keep the kept note's values on
conflict unless noted, provenance line under `## Notes`, keys unchanged. Retired notes and extracts are in
`RECYCLE-BIN/20261019-duplicate-merge/`.

### Conitzer — Social Choice for AI Alignment

**Kept:** `2024-Conitzer-Social Choice Should Guide AI Alignment in Dealing` (INNOVATION-P201, ICML 2024,
12 authors). **Retired:** `2024-Conitzer-Social Choice for AI Alignment` (AUTO_CONITZER2024, 2 authors,
arXiv v1 title; its wrong PDF had been unlinked earlier the same day).

- Filled from the retired note: `key_contribution`, `significance`, `paper_summary` (the abstract),
  `doi` (10.48550/arXiv.2404.10271), `DATA_URL: NA`, `LLM_assessed: NA`,
  `cultures_nationalities_list: N/A`, the seven `nw_*` fields (all 0).
- Corrections:
  - `CONFERENCE: "ICML 2024"`, from `CONF-CC`; the retired note said Preprint.
  - `author_country: US`, `"North America"`, `"Global North"`, `weird_score: 78`.
    - Conitzer is at Carnegie Mellon (the paper's footnote). The retired note said CA, score 84.
    - 78 is the value 683 of the other 757 notes with `author_country: US` carry.
- Kept on conflict: `ethics_overall` 90 (vs 45), `is_eval: Yes`, `ethics_perspective`, `newtags`,
  `DATE_ADDED` 20260709 (the retired note's was 20260208).
- Author profiles:
  - Vincent Conitzer: the link now points to the kept note.
  - Rachel Freedman: the link now points to the kept note. Her `affiliation` changed from
    "Department of Physics and Astronomy" to "Center for Human-Compatible AI, University of
    California, Berkeley" (the paper's footnote 3).
  - Both profiles had 7 "From …: Affiliation: Department of Physics and Astronomy, Email: …"
    lines. These came from the ammonia paper and named its authors' emails, so they were removed.

### Ubuntu — The role of the African value of Ubuntu in global AI inclusion discourse

**Kept:** `2022-Gwagwa-The role of the African value of Ubuntu in global` (YM8SFWAH; Gwagwa, Kazim &
Hilliard, *Patterns* 2022, DOI 10.1016/j.patter.2022.100462). **Retired:**
`2022-Mhlambi-The role of the African value of Ubuntu in global AI inclusion` (LSRC0090).

- **What the retired note held:**
  - The right title, plus a PubMed Central copy of this article (PMC9023883).
  - The wrong author: Sabelo Mhlambi.
  - Its PDF, extract and abstract were another paper: Saloojee & Saloojee, *From Social Exclusion
    to Social Inclusion: Theory and Practice over Two Continents* (2011). So were the scores
    derived from them.
- **Carried:** only the full `short_title`. The PMC link is in the provenance line. Its scores were
  not carried (exception to "higher wins"), since they came from the wrong text.
- **Moved:**
  - its extract → `RECYCLE-BIN/20261019-duplicate-merge/PDF Extracts/2022/`;
  - `Authors/Sabelo Mhlambi.md` → `RECYCLE-BIN/20261019-orphan-author-profiles/`. That profile
    listed only this note, and its 5 "From …" lines came from the wrong PDF.
- **PDF:** added to `PYTHON/move_retired_pdfs.py`.

## 3. Small fixes (owner: all four)

- **ALLaM** (`2025-Islamic-ALLaM A Series of Large Language Models for Arabic and English`):
  - `authors` was "Islamic". It is now the 25 authors on page 1 of the paper's PDF: M Saiful
    Bari … Haidar Khan (SDAIA).
  - `first_author` and `last_author` are now `[[M Saiful Bari]]` and `[[Haidar Khan]]`; both
    profiles exist and now list the paper.
  - The body's `## Authors` and `**Authors:**` lines now list the 25 authors.
  - `Authors/Islamic.md` (a junk profile) → `RECYCLE-BIN/20261019-orphan-author-profiles/`.
  - The filename still says "Islamic". Renaming it is the owner's call.
- **Ubuntu countries.** Two notes carried SG / Southeast Asia / Ambiguous / 57 with no basis.
  They now have the vault's unknown-author values: `author_country: Unknown`, `author_region:
  Unknown`, `author_global_north_south: Unknown`, `weird_score: 50`, as on 140 other notes. The notes:
  - `2025-Unknown-AI Ethics Meets Ubuntu Towards A` (authors unknown);
  - `2025-Unknown-Digital platform sovereignty through Ubuntu Re-imagining` (Thomas Anning-Dorson,
    affiliation not checked).
- **Orphan extract.** `PDF Extracts/2022/2022-Unknown-Can Robotic AI Systems Be Virtuous.md` had no
  note and was a near-copy of Constantinescu's extract. It moved to
  `RECYCLE-BIN/20261019-orphan-extracts/2022/`. `logs/20261019-small-data-fixes.md` had wrongly called
  it a duplicate note; that sentence is corrected.
- **Two notes renamed** to match the year and first author corrected on 2026-10-18 from their PDFs.
  Each got a dated line under `## Notes`; `local_pdf` and `pdf_extract` keep the old file names.
  - `2024-Enkhbold-A new dataset for mongolian online handwritten recognition`
    → `2023-Pan-A new dataset for mongolian online handwritten recognition`
  - `2024-Kajiwara-A comprehensive framework for multi-modal hate speech detection in`
    → `2025-Prabhu-A comprehensive framework for multi-modal hate speech detection in`
  - `Authors/Enkhbold.md` and `Authors/Kajiwara.md` no longer list these papers. Neither person
    wrote them. Kajiwara's 5 junk "From …: Affiliation: lability ratio of 98" lines came from
    the same paper and were removed too.
  - Dated files that name the old notes (STATISTICS snapshots, the 2026-07-05 COOKBOOK evidence
    cards, CULTURAL-GLOBAL data snapshots, older logs) were left unchanged. The dashboard
    generator does not read them.

## Dashboard

v14 rebuilt from the vault:
- 2,427 papers, 1,073 candidates, 795 ethics-relevant;
- `index.html` text now says 2,427.

Changes from the previous build:
- the two retired notes are gone;
- the two renamed notes appear under their new names;
- the Gwagwa title is complete;
- the kept Conitzer note now has its DOI;
- the ALLaM authors are correct;
- aggregate counts follow.
