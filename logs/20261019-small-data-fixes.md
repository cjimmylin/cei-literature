# 20261019 — Small data fixes left over from the 2026-10-18 cleanup

Follow-ups listed in `logs/20261018-duplicate-merge.md` ("Left for the owner") and found while
fixing them. Every note edit is a single-line change (the new
`paper_utils.update_paper_field`, or `re.subn(count=1, re.MULTILINE)`); files were moved with
`git mv`, never deleted.

## Notes changed (7)

| Note | Change | Evidence |
|---|---|---|
| `2024-Mahendra-SEACrowd A Multilingual Multimodal Data Hub` | `rv_christianity` 50 → 0; `religious_values` and `religious_values_list` `Christianity` → `N/A` | False positive. "Christian" occurs only in author names (Jan Christian Blaise Cruz); the PDF extract has no religious terms at all. |
| `2025-Perera-Indigenous Peoples and Artificial Intelligence A Systematic Review` | `author_country` CO → AU | Authors are at the University of Melbourne (author profiles; merge log §2). |
| `2024-Conitzer-Social Choice for AI Alignment` (AUTO_CONITZER2024) | `doi`, `url`, `external_pdf` and the body links: arXiv 2404.10000 → 2404.10271. `abstract` and `paper_summary`: ammonia-molecule abstract → the paper's abstract. `local_pdf` → N/A, `pdf_extract` emptied, extract recycled. Body: Local PDF line explains why; dated line under Notes. | 2404.10000 is *Calculation of DC Stark Resonances for the Ammonia Molecule* (Pirkola & Horbatsch); the note's PDF and extract were that paper (page 1). The note's heading is the arXiv v1 title of 2404.10271. The abstract was copied from `2024-Conitzer-Social Choice Should Guide AI Alignment in Dealing` (INNOVATION-P201), whose abstract matches its own extract sentence for sentence. Citation line now `arXiv:2404.10271 [cs.LG] (v2: 2024-06-04)`, from that extract's page stamp. |
| `2025-Hui-Decoding Moral Responses in AI` | `local_pdf` → N/A, `pdf_extract` emptied, both extracts recycled; `external_pdf` → N/A; body Local PDF line explains why; dated line under Notes. | Both extracts (`PDF Extracts/2025/…` and `PDF Extracts/0000/…`) were a ScienceDirect "There was a problem providing the content" page. `external_pdf` carried a made-up `md5=c8e7d7c8c8c8…`. |
| `2022-Zhang-Artificial Intelligence and Moral Dilemmas` | `local_pdf` → N/A, `pdf_extract` emptied, extract recycled | Same ScienceDirect error page (found by searching all extracts for it). The body already said "Local PDF: PENDING - paywall restricted". |
| `2024-Sun-Benchmarking Hallucination in Large Language`, `2024-Tlaie-Exploring and steering the moral compass of Large` | one NUL byte in `paper_summary` → space | A PDF-extraction artefact; it made grep and other tools treat the notes as binary. No other note has one. |

No other line in these notes changed. `validate_all_papers.py`: 2,429 / 2,429 valid.

## Files moved

- `RECYCLE-BIN/20261019-wrong-pdf-extracts/`: the Conitzer (2024), Hui (2025 and 0000) and Zhang (2022)
  extracts, under their old year folders.
- `RECYCLE-BIN/20261019-orphan-author-profiles/`: 6 profiles that list no papers and that nothing
  links to: the 5 SocialSense authors left by the merge (Jinning Li, Yi R. Fung, Hou Pong Chan,
  Tarek Abdelzaher, ChengXiang Zhai), all unfilled templates, and the garbage profile `5 others`.
  `Yi R. Fung` duplicated the existing `Authors/Yi Fung.md`, which stays.
- `PYTHON/move_retired_pdfs.py` now also lists the 3 matching PDFs in the PDF folder outside the
  repo (Conitzer's ammonia paper, Hui's and Zhang's error pages, including any copy under
  `Utilitarian Ethics/Borderline/`). Run it on the machine that holds the PDF folder.

## Privacy note

The 3 error-page extracts recorded an IP address (`IP Address: …` in the page text), probably the
network the PDFs were downloaded from. The repo is public. Moving the files does not hide it: they
stay tracked under `RECYCLE-BIN/`, and the address is in git history.

The same address also appears in 9 other extracts and in
`STATISTICS/20260312-normative-audit-tier1-review.html`. Those 9 PDFs are Springer article web
pages printed to PDF ("Skip to main content … Log in"), and the page footer shows the visitor's IP.
They still hold the article text, so they were left in place:

- 2021-Angle
- 2022-Constantinescu
- 2022-Unknown "Can Robotic AI Systems Be Virtuous"
- 2024-Chhabra
- 2024-Farina
- 2024-Kyriacou
- 2025-Aina
- 2025-Sanwoolu
- 2025-Schacht

Removing the address from these files is the owner's call. Also: `2022-Unknown-Can Robotic AI Systems Be Virtuous` is
an extract with no note (a near-copy of `2022-Constantinescu-Can Robotic AI Be Virtuous`'s extract), not a duplicate
note. (Corrected later the same day; the address was redacted and the orphan extract recycled, see
`logs/20261019b-followup-fixes.md`.)

## Not changed (for the owner)

- **Likely duplicate:** `2024-Conitzer-Social Choice for AI Alignment` (AUTO_CONITZER2024, 2 authors)
  and `2024-Conitzer-Social Choice Should Guide AI Alignment in Dealing` (INNOVATION-P201, 12
  authors, ICML 2024) are now the same arXiv paper. Not merged; merging needs the same review as the
  2026-10-18 plan.
- **Hui et al. author list:** the retired Hendra note added Ray LC and Latisha Besariani Hendra.
  Crossref, OpenAlex and doi.org are blocked from this environment, so it stays unconfirmed.
- **Zhang 2022 `external_pdf`** (`https://doi.org/10.36571/ajsp661`) is a different DOI from the
  note's `doi` (10.1016/j.jesp.2022.104327); not checked.
- From the merge log, still open: the Ubuntu note's `author_country: SG` with unknown authors; the
  Hongladarom book (`2020-Hongladarom-The Ethics of AI and Robotics`), whose classification is
  mostly empty (`rv_buddhism` 0, `ethics_overall` 0) and needs a re-review, not a single fix;
  `Authors/Islamic.md`, still linked as the first author of the ALLaM note.
- The Snoswell `rv_jainism` false positive needed nothing: the merge already set it to 0.
