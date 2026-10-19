# 20261019e — Veitsman note corrected, two duplicate pairs merged, 24 notes made valid YAML

**Owner decision (2026-10-19):** "Yes" to doing the vault items that need no further ruling: the
Veitsman correction, the two duplicate pairs flagged in `logs/20261019d-low14-scores-metadata-abstracts.md`,
and the strict-YAML cleanup.

**Method.**
- Frontmatter edits are single-line (`paper_utils.update_paper_field` / `batch_update_papers`).
- Body edits replace exact lines that were checked to occur once.
- Files were moved with `git mv`; nothing was deleted.

**Validation.**
- `validate_all_papers.py`: 2,423 / 2,423 valid.
- All 2,423 notes now also pass a strict YAML parser (PyYAML `safe_load`). Before this change, 24
  failed. The earlier log's count of 46 was wrong: that check also split on `---` inside values.

## 1. Veitsman → Karibayeva

`2024-Veitsman-The Development and Experimental Evaluation of a Multilingual Speech` →
`2025-Karibayeva-The Development and Experimental Evaluation of a Multilingual Speech`.

**Source:** Crossref, doi 10.3390/app152412880. *Applied Sciences* 15(24), 12880, published
2025-12-05.

**Authors and year:**
- **Authors (8):** Aidana Karibayeva, Vladislav Karyukin, Ualsher Tukeyev, Balzhan Abduali, Dina Amirova,
  Diana Rakhimova, Rashid Aliyev and Assem Shormakova. All are at the Faculty of IT and AI, Farabi
  University, Almaty.
- The note had named Yana Veitsman, 2024; she is not an author.

**Frontmatter changed:**
- `year` 2025, `first_author`, `last_author`, `authors`, `authors_incomplete: false`.
- `type` journalArticle, `CONFERENCE` Journal, `publication`, `doi`.
- `languages_list`: Kazakh, Turkish, Tatar, Uzbek. It was Kyrgyz, Turkish, Uyghur; the corpus pairs
  Kazakh with the other three.
- `author_country` KZ, with the values the 7 other KZ notes carry: Eastern Europe & Central Asia,
  Ambiguous, 33. They were DE, Western Europe, Global North, 84.

**Body:**
- The `## Authors`, `**Authors:**`, `**Year:**`, `**Type:**`, `**Venue:**` and `**Languages:**` lines
  are corrected.
- The empty `## Abstract` section now holds the abstract.
- A dated line was added under `## Notes`. The Data Description still names the wrong languages;
  the dated line says so.

**Profiles:**
- New: `Authors/Aidana Karibayeva.md` and `Authors/Assem Shormakova.md`, from the vault template,
  with affiliation and ORCID.
- `Authors/Yana Veitsman.md` no longer lists the paper. She keeps her other two notes.

## 2. Duplicate pairs merged

These follow the rules of `logs/20261018-duplicate-merge.md`. Retired notes and extracts are in
`RECYCLE-BIN/20261019-duplicate-merge/`, and their PDFs are added to `PYTHON/move_retired_pdfs.py`.

### BuddhismEval (Muthugala & Xiong)

**Kept:** `2025-Xiong-BuddhismEval A Bilingual Benchmark for Buddhist` (EXSR0339). It has the
abstract and the Hugging Face dataset link.

**Retired:** `2025-Xiong-BuddhismEval Bilingual Evaluation Benchmark for Buddhist` (EXSR0340).
- Its PDF and extract were an education encyclopedia index. Its own Data Description already said
  so.
- Its `external_pdf` was a book's table of contents (gbv.de, ISBN 9780415749237).
- Its `rv_*` values (five religions at 50) and other scores came from that wrong text, so **nothing
  was carried over**.

**Other changes:**
- `Authors/Nethmi Muthugala.md` and `Authors/Deyi Xiong.md` no longer list the retired note.
- The junk profile `Authors/Deyi Xiong Nethmi Muthugala.md` (no note links to it) →
  `RECYCLE-BIN/20261019-orphan-author-profiles/`.
- The retired note's v13 benchmark-survey entry, which already called itself a "Duplicate entry",
  was removed from `DASHBOARDS/cei-dashboard-14/build/benchmark_survey_candidates.json`. The count
  goes from 1,072 to 1,071 (v13-derived: 985 → 984). `build/README.md` and `index.html` are updated.

### Decolonizing NLP for "Low-resource Languages" (GRACE, 2023)

**Source:** the publisher page, ojs.stanford.edu, GRACE article 2584. *GRACE: Global Review of AI
Community Ethics* 1(1), published 2023-02, doi 10.60690/q2xhtx18. Authors: Tolúlọpẹ́ Ògúnrẹ̀mí,
Wilhelmina Onyothi Nekoto and Saron Samuel.

**Kept and renamed:** `2023-StanfordMasakhane-Decolonizing NLP for 'Low-resource Languages' Applying
Abebe` (LSRC0091) → `2023-Ògúnrẹ̀mí-Decolonizing NLP for 'Low-resource Languages' Applying Abebe`. The
name follows her existing note `2024-Ògúnrẹ̀mí-ÌròyìnSpeech`.
- **Filled:**
  - the real authors, which replace "Authors from Stanford/Masakhane";
  - `doi`, `publication` and `authors_incomplete`.
- **Abstract:** the publisher's verbatim abstract replaces a generated summary. The summary stays in
  the body, labelled "Earlier summary".
- **Higher scores from the retired note:**
  - `rv_indigenous` 50 and `nw_indigenous_relational` 50 (were 15);
  - `religious_values` and `religious_values_list`: Indigenous Spirituality.
- **`research_topic`:** NLP & Representation Learning. The note scores below 50.

**Retired:** `2025-Ogunremi-1 Decolonizing NLP for “Low-resource Languages”` (LSRC0811). It is the
same article, misdated 2025. Its `is_eval: Yes` and `is_dataset: Yes` were **not** carried: the
piece is an essay. This is an exception to "Yes beats No".

**Profiles:**
- `Authors/Tolúlọpẹ́ Ògúnrẹ̀mí.md` now lists the paper.
- `Authors/Saron Samuel.md` and `Authors/Wilhelmina Onyothi Nekoto.md` now link the kept note.
- Two profiles moved to `RECYCLE-BIN/20261019-orphan-author-profiles/`:
  - `Authors/Authors from StanfordMasakhane.md`, a junk profile;
  - `Authors/Tolulope Ogunremi.md`, a template-only duplicate of her real profile.

## 3. 24 notes made valid YAML

All of these were already accepted by `validate_all_papers.py` and by the dashboard generator,
which reads lines without a YAML parser. Obsidian's properties panel and any strict parser
rejected them.

**Truncated values (15).** Each value had been cut right after an escaped inner quote, so it ended
in `\"` and the string never closed. Each value was restored in full from the note's own body
(the `## Abstract` section, or the H1 title for the short title). Every one was first checked to
start with the truncated text.

| Note | Field | Length before → after |
|---|---|---|
| `2024-Adilazuarda-Towards Measuring and Modeling ` | `short_title` | 31 → 58 |
| `2024-Leech-Ten Hard Problems in Artificial Intelligence We` | `abstract` | 22 → 799 |
| `2024-Vallor-The AI Mirror` | `abstract` | 622 → 828 |
| `2025-Aina-Virtue Ethics by Design` | `abstract` | 249 → 719 |
| `2025-Bang-HalluLens LLM Hallucination Benchmark` | `abstract` | 123 → 1461 |
| `2025-Bryan-Virtue Ethics and Postponing Human Extinction` | `abstract` | 595 → 645 |
| `2025-Gounaris-Virtue in the Machine` | `abstract` | 235 → 609 |
| `2025-Krzanowski-Phronesis for AI Systems` | `abstract` | 423 → 555 |
| `2025-Nay-Aligning AI Agents with Humans through Law as Information` | `abstract` | 26 → 650 |
| `2025-Okamoto-AI-based medical ethics education` | `abstract` | 199 → 615 |
| `2025-Pipitone-Unlocking practical wisdom` | `abstract` | 37 → 640 |
| `2025-Rourke-Mind Crime` | `abstract` | 168 → 811 |
| `2025-Steen-Ethical aspects of ChatGPT` | `abstract` | 173 → 628 |
| `2025-Sullins-Automated Ethical Practical Reasoning` | `abstract` | 266 → 674 |
| `2025-Velay-Vitow-Putting the AI in Eudaimonia` | `abstract` | 479 → 835 |

**LaTeX in double-quoted abstracts (5).** Sequences like `\frac`, `\cdot`, `\%` and `\url` were
invalid YAML escapes, and `\f` was read as a form feed. The backslashes are now escaped, so the
abstract reads back exactly as before. Notes: `2024-Varshney-Decolonial AI Alignment - Openness Visesa-Dharma and Including`, `2025-Gölz-Distortion of AI Alignment Does Preference`, `2025-Maura-Rivero-Jackpot Alignment as Maximal Lottery`, `2026-Radev-The Best-Laid SCHEMEs Coordinated Sabotage and Monitori`, `2024-Moon-BEAF`.

**Control characters (3).** Leftovers from PDF extraction:
- `2022-Ramanayake-Pro-Social Rule Breaking as a Benchmark of` and `2025-Song-Evaluation of Social
  Bias Classification Performance of LLMs Using`: a BEL character (U+0007) from a bullet glyph,
  replaced by a space or removed.
- `2024-Lu-The AI Scientist`: three mis-decoded footnote daggers (U+0086), restored as †.

**Markdown pasted into frontmatter (1).** `2025-Tsvetkov-Democracy-in-Silico Institutional Design as
Alignment` had 5 body-style lines in its frontmatter: `**Authors: "** …`, Year, Type, DOI and
Publisher. They were removed. The same facts are already in `year`, `type`, `doi` and `url`.

## Dashboard

v14 was rebuilt: 2,423 papers (was 2,425), 1,071 candidates, 853 ethics-relevant.
- The four retired or renamed notes are replaced by the two kept names.
- Adilazuarda's title is now complete.
- `index.html` now says 2,423 papers and 1,071 candidates.

## Noticed, not changed

- **`2025-Tsvetkov-Democracy-in-Silico …`:** the filename names Tsvetkov, but the note's own
  `authors` field lists Trisanth Srinivasan and Santosh Patapati (arXiv 2508.19562). This was not
  checked against arXiv; it needs checking before a rename.
- **The kept BuddhismEval note** has `ethics_overall: 0` and `ethics_perspective: "Hallucination &
  Truthfulness"` for a Buddhist-ethics benchmark. It also has `author_country: FR`, which
  is probably wrong: Deyi Xiong is, to our knowledge, at Tianjin University, but this was not checked
  here. Its classification needs a re-review.
- **The kept Decolonizing NLP note** scores `ethics_overall: 20` for an essay applying relational
  ethics. That is likely too low; it needs a re-score.
