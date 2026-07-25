# Citation-metadata findings from the phase-6 related-work drafting pass

**Date:** 2026-07-25 · **Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
**Context:** §2 of both phase-6 manuscripts was drafted by agents with **no web access**,
so every citation had to be verified against a file in the project literature vault. That
constraint surfaced defects in the vault's own metadata that a web-enabled pass would have
papered over.
**Nothing in the vault was modified.** This note records the findings; remediation is a
separate, out-of-scope decision.

---

## 1. Two extracts whose CONTENT does not match their FILENAME — do not cite from filename

Both were opened, read, and **deliberately not cited**. Citing either from its filename
would have produced a fabricated reference — a real title and author attached to a
document that is not that work.

| Vault file | Filename claims | Actual document content (verified) |
|---|---|---|
| `CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2025-Adilazuarda-Cultural Alignment Large Language.md` | Adilazuarda, *Cultural Alignment … Large Language …* (2025) | **Sonkar et al., "Pedagogical Alignment of Large Language Models"**, Findings of the ACL: EMNLP 2024, pp. 13641–13650 |
| `CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2024-Manyika-Integrating Catholic Social Teaching.md` | Manyika, *Integrating Catholic Social Teaching* (2024) | **A Synod of Bishops PREPARATORY DOCUMENT** — a magisterial document, not a research paper |

The defect originates upstream of the extract: the extract's YAML faithfully records its
`source_pdf`, and the source PDF's *filename* is what disagrees with the PDF's *contents*.
So this is a PDF-acquisition naming defect, not an extraction defect.

**Consequence for the manuscripts:** neither work is cited. Paper (a) §2 carries a
`[CITATION NEEDED]` marker where a corpus-anchored religious-values comparison would have
gone, which is the honest state.

## 2. One paper note with two disagreeing author blocks

`CEI-Lit-WS/papers/2023-Guo-COBBLER.md`:

| Field | Value |
|---|---|
| YAML `authors:` | Ryan Koo; Minhwa Lee; Vipul Raheja; Jong Inn Park; Zae Myung Kim; Dongyeop Kang |
| YAML `url:` | `https://arxiv.org/abs/2309.17012` |
| Body `**Authors:**` | Guo, X.; Zhang, B.; Wang, J.; Wang, H.; Zhang, Y.; Zhang, C. |
| **Filename** | `2023-Guo-…` — follows the body block |

The YAML `authors:` field and the `url:` agree with each other (arXiv 2309.17012 is
CoBBLEr, by Koo et al.), so the body block and the filename are the incorrect pair.
**Paper (b) cites Koo et al.**, which is correct, and the ledger flags the discrepancy.

## 3. Filename author token disagrees with printed byline — seven further cases

Flagged during paper (a)'s pass: `Hamid/Abrar`, `Buyl/Liu`, `Alharbi/Abdelaal`,
`Johnson/Owen`, `Srivastava/Fang`, `Zheng/Hong`, `Burden-Li/Bean`. In each the prose cites
the **printed byline** and the ledger records the **vault path**, so the two can be
reconciled later.

## 4. Near-duplicate vault entries under different first-author strings

| Work | Entry used (canonical) | Duplicate |
|---|---|---|
| *Measuring What Matters: Construct Validity in LLM Benchmarks* | `CEI-Lit-WS/papers/2024-Bean-Measuring What Matters - Construct Validity in LLM Benchmarks.md` | `…/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2025-Li-Measuring What Matters Construct.md` |
| *Large Language Model Psychometrics* | `CEI-Lit-WS/papers/2025-Ye-Large Language Model Psychometrics.md` | `…/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2025-Gupta-Large Language Model Psychometrics.md` |

## 5. The binding rule this establishes for these manuscripts

**A bibliography build must resolve against the documents themselves, never against vault
filenames or against a filename-derived author token.** This is stated in the provisional
reference-list preamble of both manuscripts so it travels with them.

## 6. Recommended follow-up — NOT done, NOT authorized here

1. Re-derive titles/authors for the two mismatched PDFs in §1 and rename per the vault
   naming convention (`YYYY-Author-Short Title.pdf`), moving the old files to a
   `RECYCLE-BIN/` rather than overwriting.
2. Reconcile `2023-Guo-COBBLER.md`'s body author block against its own YAML and URL.
3. Run a vault-wide audit for the same class of defect: compare each extract's first-page
   byline against its filename author token. The four defects above were found incidentally
   while drafting two sections, which suggests the class is not rare.
4. De-duplicate the two near-duplicate pairs in §4.

Items 1–4 touch the papers vault, which is outside this session's scope (phase-6
manuscript assembly). They are recorded here so the finding is not lost.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
