# Duplicate-note merge — 2026-10-18

**What was done:** the 13 likely-duplicate groups flagged in `DASHBOARDS/cei-dashboard-14/build/likely_duplicates.txt` were merged.
- Three of the groups turned out to be triples, so **16 notes were retired** and 13 kept.
- Retired notes and their duplicate PDF extracts were moved with `git mv` into `RECYCLE-BIN/20261018-duplicate-merge/`, keeping their relative paths (`papers/…`, `PDF Extracts/<year>/…`). Nothing was deleted.
- Base commit: `8af25095`. The vault owner approved the plan before it was applied.

**Rules applied.**
- **YAML edits** are single-line edits made in place. Fields the kept note lacked were appended just before the closing `---`, and wikilinks are quoted. Each edit was applied only after its expected current line was found exactly once in the file.
- **Conflict defaults** follow the 2026-02 merge (`PYTHON/consolidate_duplicates.py`):
  - fill empty or `N/A` fields;
  - higher `ethics_overall` and full-text `rv_*` / `nw_*` / `mp_*` scores win;
  - the longer, verbatim abstract wins;
  - `is_*: Yes` beats `No`.
- **Exceptions to those defaults** are listed per pair below.
- **Keys** were never changed or reused.
- **Provenance.** Each kept note got a plain-text provenance line under `## Notes`, deliberately not a wikilink.

**Effect on the dashboard inputs.**
- `DASHBOARDS/cei-dashboard-14/build/benchmark_survey_candidates.json` lost 8 entries: 1,081 → 1,073. That leaves 985 v13-derived entries and 88 from the v14 new-paper review. Its format (`indent=1`, `ensure_ascii=False`, no trailing newline) is unchanged.
- `normative_v2_all_classifications.json` was not touched; none of these notes is in it.
- `papers/` now holds 2,429 notes.
- The dashboard was **not** rebuilt. Expected values after a rebuild: 2,429 papers, 1,073 candidates (`ib`), 815 ethics-relevant (`eo`; it was 817).
- `build/README.md` still says 1,081 / 986 / 95. Update it if the candidates file stays edited in place.

## Summary

| # | Kept note | Retired note (key) | Verdict |
|---|---|---|---|
| 1 | `2025-Unknown-AI Ethics Meets Ubuntu Towards A` | `2025-UbuntuAI-AI Ethics Meets Ubuntu Governance` (EXSR0702) | same work (title and year) |
| 2 | `2025-Perera-Indigenous Peoples and Artificial Intelligence A Systematic Review` | `2025-Perera-Indigenous Peoples and AI Systematic Review` (EXSR0704); `2025-Halgamuge-Indigenous Peoples and Artificial Intelligence A` (EXSR0390) | same work (DOI 10.1177/20539517251349170) |
| 3 | `2025-Maldonado-Indigenous Ethics and Artificial Intelligence` | `2025-IndigenousEthics-Indigenous Ethics and AI` (EXSR0703) | same work (DOI 10.1007/s43681-025-00879-2) |
| 4 | `2025-Hui-Decoding Moral Responses in AI` | `2025-Hendra-Decoding Moral Responses in AI` (EXSR0693); `2025-Sun-Decoding Moral Responses in AI A Quantitative Analysis of Large` (EXSR0039) | same title; **the Sun note held a different paper** (see below) |
| 5 | `2025-Islamic-Sacred or Synthetic Evaluating LLM Reliability and Abstention for` | `2025-Atif-Sacred or Synthetic Evaluating LLM Reliability` (EXSR0671) | same work (FiqhQA, AIES 2025, arXiv 2508.08287) |
| 6 | `2025-Snoswell-Beyond Verdicts LLM Moral Competence` | `2025-Snoswell-Beyond Verdicts Evaluating Language Model Moral` (EXSR0684); `2025-Snoswell-Beyond Verdicts Evaluating Language Model Moral Competence Aaron J.` (LSRC0693) | same work (PhilArchive SNOBVE; identical PDF) |
| 7 | `2024-Almeida-Exploring the Psychology of LLMs Moral Reasoning` | `2024-Unknown-Exploring psychology LLMs moral legal reasoning` (EXSR0688) | same work (pii S000437022400081X) |
| 8 | `2020-Hongladarom-The Ethics of AI and Robotics` | `2020-Hongladarom-Ethics of AI and Robotics` (CGSR0215) | same work (two Semantic Scholar records of the 2020 Lexington book) |
| 9 | `2005-Teaiwa-Articulated Cultures Militarism and Masculinities in` | `2005-Teaiwa-Articulated Cultures Militarism and Masculinities` (CGSR0188) | same work. "K. Teaiwa" is a Semantic Scholar parsing error; the record's title ends in "Teresia" |
| 10 | `2024-Songyuan Liu-Measuring Spiritual Values and Bias of` | `2024-Unknown-Measuring Spiritual Values Bias Large Language` (EXSR0672) | same work (arXiv 2410.11647) |
| 11 | `2025-Sachdeva-Normative Evaluation of LLMs with Everyday Moral Dilemmas` | `2025-Unknown-Normative Evaluation Large Language Models Everyday` (EXSR0687) | same work (DOI 10.1145/3715275.3732044) |
| 12 | `2025-Liu-Can LLMs Grasp Implicit Cultural Values` | `2025-Unknown-Can LLMs Grasp Implicit Cultural Values` (EXSR0674) | same work (arXiv 2504.01127) |
| 13 | `2024-Mahendra-SEACrowd A Multilingual Multimodal Data Hub` | `2024-Lovenia-SEACrowd Multilingual Multimodal Data Hub Benchmark` (EXSR0667) | same work (arXiv 2406.10118, EMNLP 2024) |

## Finding: the 2025-Sun note held a different paper

`2025-Sun-Decoding Moral Responses in AI A Quantitative Analysis of Large.md` (EXSR0039, added 2026-02-07) carried this paper's title but described another paper. These fields all belong to **SocialSense**: *Decoding the Silent Majority: Inducing Belief Augmented Social Graph with Large Language Model for Response Forecasting*, Chenkai Sun et al., EMNLP 2023, arXiv 2310.13297.
- authors (Chenkai Sun … Heng Ji)
- abstract
- `external_pdf` (arxiv.org/pdf/2310.13297)
- local PDF and both extracts (page 1 is the SocialSense paper)
- `DATA_URL` (github.com/chenkaisun/SocialSense)
- `LLM_assessed: ChatGPT`
- `mp_mft: 100`, `mp_schwartz: 50`

Its DOI `10.1016/j.chbah.2025.100121` (CHB: Artificial Humans) does not match the real article either. The real article is:
- *Decoding moral responses in AI: A quantitative analysis of large language models*
- Bryant P.H. Hui, Chiu Lun Lau, Rui Sun, …
- *Computers in Human Behavior Reports* (2025), DOI 10.1016/j.chbr.2025.100854, pii S2451958825002696

Its own v13 benchmark-survey entry had already noted "PDF extract appears mismatched".

**What was done about it:**
- The note was retired with **nothing carried over**.
- Its two extracts went to the recycle bin.
- Its links in 7 author profiles were **removed, not re-pointed**, because those people are SocialSense's authors.
- SocialSense itself is not in the vault.

## Per-group detail

### 1. AI Ethics Meets Ubuntu
**Kept:** `papers/2025-Unknown-AI Ethics Meets Ubuntu Towards A.md` (CGSR0002). It is older (DATE_ADDED 20260403) and is the record that the MORAL-PSYCH and CULTURAL-GLOBAL pipelines cite.

Fields carried from EXSR0702:
- `type: document` → `journalArticle`
- `url` → `"https://ijsrm.net/index.php/ijsrm/article/view/6558"`. The publisher page replaces ResearchGate; the old URL is in the provenance line.
- `abstract` → `"Five-layer Ubuntu governance architecture for AI: Community Data Trusts, Relational Design Praxis, Harm Reconciliation Panels, Ecological Stewardship Protocols, Developer Benefit Realisation."` (longer)
- `ethics_overall: 0` → `60` (higher wins)
- `rv_ubuntu: 50` → `60` (higher wins)
- added: `publication: "International Journal of Scientific Research and Management"`, `ethics_perspective: "Responsible AI"`, `is_benchmark: No`, `is_eval: No`, `is_dataset: No`, `LLM_assessed: No`

Conflicts where the kept value stayed:
- `nw_ubuntu` 65 vs 50
- `national_ethnic_cultural` `African/Ubuntu` vs `African`
- `short_title` (letter case only)

Not carried:
- `newtags` and `source` (search-pipeline labels)
- `mp_maqasid` / `mp_confucian` / `mp_ubuntu` (fields outside the schema)

### 2. Indigenous Peoples and AI: a systematic review (three notes)
**Kept:** `papers/2025-Perera-Indigenous Peoples and Artificial Intelligence A Systematic Review.md` (ZERO0019). It has the first-author filename, full title and DOI, and all 9 co-author profiles already linked it.

From EXSR0704:
- `type: conferencePaper` → `journalArticle`
- `ethics_overall: 0` → `60` (higher wins)

From EXSR0390 (Halgamuge):
- `local_pdf` → `"[[Lit-WS-PDFs/2025/2025-Halgamuge-Indigenous Peoples and Artificial Intelligence A.pdf]]"`. The pointer was transferred; the PDF and extract stay where they are.
- `pdf_extract` → `"PDF Extracts/2025/2025-Halgamuge-Indigenous Peoples and Artificial Intelligence A.md"`
- added `external_pdf: "https://osf.io/6hrqj/download"`
- `rv_indigenous: 50` → `100` (full-text score)
- `nw_indigenous_relational: 50` → `100` (full-text score)
- `DATE_ADDED: 20260216` → `20260213`, the earliest record of this work (approved in the plan)

Corrections:
- `CONFERENCE: "Other Conference"` → `Journal`, which follows from the new `type`.
- `abstract`: the earlier paraphrase (377 characters) was replaced with the **verbatim** abstract from page 1 of the Halgamuge extract. Halgamuge's own field held only the first three sentences.

Body:
- added `- **Preprint PDF (OSF):** https://osf.io/6hrqj/download` under `## Links`
- two provenance lines

Conflicts where the kept value stayed:
- `ethics_perspective` (Social & Cultural Values)
- cultures: `Multicultural/Cross-cultural` vs `Indigenous` / `Australian/Aboriginal`
- `is_benchmark: No` (Halgamuge's `Yes` was wrong; it is a review)
- `data_description: N/A`
- `virtue_ethics` 0 vs 10 and `utilitarian_ethics` 0 vs 5
- `short_title` (Halgamuge's was truncated)

`author_country` is CO in the kept note and FR in Halgamuge. Both are wrong: the authors are at the University of Melbourne, so it should be AU. **This was not changed** (a data fix outside the merge).

### 3. Indigenous Ethics and Artificial Intelligence
**Kept:** `papers/2025-Maldonado-Indigenous Ethics and Artificial Intelligence.md` (CULT0114).

- Carried: `type: conferencePaper` → `journalArticle` (*AI and Ethics* is a journal).
- Correction: `CONFERENCE: "Other Conference"` → `Journal`.
- All other conflicts kept the kept note's values, which come from the full text: abstract, `ethics_overall` 80, framework scores, cultures (`Latin American`), `rv_*`, `nw_*`, `ethics_perspective`.

### 4. Decoding Moral Responses in AI (three notes)
**Kept:** `papers/2025-Hui-Decoding Moral Responses in AI.md` (no key; left empty). It has the correct first author, DOI and venue.

From EXSR0693 (Hendra):
- `short_title` → `"Decoding Moral Responses in AI: A Quantitative Analysis of Large Language Models"`
- `moral_psychology: N/A` → `"Dual Process Theory"`
- `mp_dual_process: 0` → `60`
- `ethics_overall: 35` → `60` (higher wins)
- `ethics_perspective: "General Ethics"` → `"Moral Reasoning & Psychology"`

Correction from the abstract: `LLM_assessed` → `"GPT-3, GPT-3.5, GPT-4, GPT-4.1, Claude 3.7 Sonnet, Grok 3, Gemini 2.5 Pro"`.

Not carried:
- Everything from EXSR0039 (Sun), as described above.
- Hendra's `publication_title` (wrong journal), `LLM_assessed: No`, `is_eval: No`, `newtags`, `source`.

**Not applied:**
- The full author list (adding Ray LC and Latisha Besariani Hendra) could not be confirmed on the publisher page, which was unreachable. `authors` is unchanged.
- Hui's own `local_pdf` and both of its extracts (`PDF Extracts/2025/…` and `PDF Extracts/0000/…`) are a ScienceDirect error page, and its `external_pdf` carries a fabricated `md5`. These are left for a separate decision.

### 5. Sacred or Synthetic? (FiqhQA)
**Kept:** `papers/2025-Islamic-Sacred or Synthetic Evaluating LLM Reliability and Abstention for.md` (LSRC0736). It has the PDF and extract, the fuller classification, the older DATE_ADDED, and a v13 benchmark entry. All values below were checked against page 1 of the extract.

From EXSR0671 (Atif):
- `short_title` → `"Sacred or Synthetic? Evaluating LLM Reliability and Abstention for Religious Questions"`
- `first_author: "[[Islamic]]"` → `"[[Farah Atif]]"`
- `last_author: "[[Islamic]]"` → `"[[Monojit Choudhury]]"`
- `authors: Islamic` → `"Farah Atif; Nursultan Askarbekuly; Kareem Darwish; Monojit Choudhury"`
- `publication: Web` → `"Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society"`
- `CONF-CC: Preprint` → `"AIES 2025"`
- added `authors_incomplete: false`, `s2_paper_id: 4d6606388f4e924182bfb025aa01a18401015ad0`, `citation_count: 7`

Body:
- heading gains "Questions"
- the `## Authors` line and `**Authors:**` line now give the four authors
- `**Venue:**` → `AIES 2025 (AAAI/ACM Conference on AI, Ethics, and Society)`
- provenance line

Conflicts where the kept value stayed:
- `rv_islam` 100 with the other traditions at 0, `religious_values` / `religious_values_list` `Islam`. The Atif note had uniform "Multi-religion" placeholders at 50; the paper covers Sunni fiqh only.
- `url` (AIES proceedings PDF), `abstract`, `DATE_ADDED`, `nw_islamic_ethics`, `weird_score`.

### 6. Beyond Verdicts (three notes)
**Kept:** `papers/2025-Snoswell-Beyond Verdicts LLM Moral Competence.md` (AUTO_SNOSWELL2025). It has the oldest DATE_ADDED, the richest body, and the benchmark entry.

| Field | Before → after | Source / reason |
|---|---|---|
| `abstract` | paraphrase → verbatim paper abstract | LSRC0693, as repaired in `fe0b25f9` |
| `short_title` | → `"Beyond Verdicts: Evaluating Language Model Moral Competence"` | EXSR0684 |
| `last_author` | `"[[Lazar, Seth]]"` → `"[[Seth Lazar]]"` | LSRC0693; `Authors/Seth Lazar.md` exists |
| `rv_jainism` | `50` → `0` | EXSR0684; false positive from the cited author *Jain*, Calacci & Wilson (2024) |
| `religious_values` | `Jainism` → `N/A` | EXSR0684 |
| `religious_values_list` | `Jainism` → `N/A` | EXSR0684 |
| `is_dataset` | `Yes` → `No` | LSRC0693; the paper is a survey with no dataset |
| `publication` | added: `PhilArchive` | fill |

Conflicts where the kept value stayed: `type: preprint`, `mp_mft` / `mp_kohlberg` 50, `ethics_overall` 100, `url`, `data_description`, `DATE_ADDED`.

Extract `PDF Extracts/2025/2025-Snoswell-Beyond Verdicts Evaluating Language Model Moral Competence Aaron J..md` (a duplicate of the kept note's extract) was recycled.

### 7. Exploring the psychology of LLMs' moral and legal reasoning
**Kept:** Almeida (ALMEIDA2024).
- Carried: `short_title: "Psychology of LLMs Moral Reasoning"` → `"Exploring the psychology of LLMs' moral and legal reasoning"`.
- All other conflicts kept the kept note's values (`ethics_overall` 95, `mp_mft` 50, `moral_psychology`, abstract, `type`).

### 8. The Ethics of AI and Robotics (Hongladarom)
**Kept:** CGSR0214.
- No fields carried; the two notes were identical apart from `key`, `short_title` and the Semantic Scholar URL.
- Notes section added, holding the retired Semantic Scholar URL.

### 9. Articulated Cultures (Teaiwa)
**Kept:** CGSR0187 (`T. Teaiwa`; Teresia Teaiwa, *Fijian Studies* 3(2), 2005).
- No fields carried.
- Notes section added, recording the "K. Teaiwa" mis-parse and the retired Semantic Scholar URL.

### 10. Measuring Spiritual Values and Bias of LLMs
**Kept:** Songyuan Liu (EXSR0509).

| Field | Before → after |
|---|---|
| `short_title` | → `"Measuring Spiritual Values and Bias of Large Language Models"` |
| `first_author` | `"[[Songyuan Liu,]]"` → `"[[Songyuan Liu]]"` |
| `last_author` | `"[[5 others]]"` → `"[[Jiaying Lu]]"` |
| `authors` | → `"Songyuan Liu; Ziyang Zhang; Runze Yan; Wei Wu; Carl Yang; Jiaying Lu"` (the retired note's first five, completed from page 1 of the extract) |
| `national_ethnic_cultural` | `N/A` → `Multicultural/Cross-cultural` |
| `cultures_nationalities_list` | `N/A` → `Multicultural/Cross-cultural` |
| `is_dataset` | `No` → `Yes` (`Yes` wins; the paper releases the SP-Typology and SP-10Axes instruments) |

Body: the `## Authors` and `**Authors:**` lines now list all six authors.

Conflicts where the kept value stayed: the full-text `rv_*` scores (100/100/40/50/30 rather than the uniform 50 placeholder), `religious_values`, `abstract`, `ethics_overall` 80, `nw_buddhist`, `url`, `DATE_ADDED`.

### 11. Normative Evaluation of LLMs with Everyday Moral Dilemmas
**Kept:** Sachdeva (SACHDEVA2025).
- Carried: `short_title` → `"Normative Evaluation of Large Language Models with Everyday Moral Dilemmas"`.
- Everything else kept the kept note's values.

### 12. Can LLMs Grasp Implicit Cultural Values? (CQ-Bench)
**Kept:** Liu (ER38ZQNK).
- Carried: `short_title` → `"Can LLMs Grasp Implicit Cultural Values? Benchmarking LLMs' Cultural Intelligence with CQ-Bench"`.
- Correction from page 1 of the PDF: `authors` → `"Ziyi Liu; Priyanka Dey; Jen-tse Huang; Zhenyu Zhao; Bowen Jiang; Rahul Gupta; Yang Liu; Yao Du; Jieyu Zhao"`. The kept note had 7 of the 9; the retired note had "Jin Huang" and "Bo Jiang". The body's `## Authors` line was not changed.
- Not carried: the retired note's "Multi-religion" placeholders (`religious_values` and five `rv_*` at 50). Religion is one World Values Survey topic area, not the paper's focus.

### 13. SEACrowd
**Kept:** Mahendra (EXSR0523).
- Carried: `type: preprint` → `conferencePaper`.
- Carried: `short_title` → `"SEACrowd: A Multilingual Multimodal Data Hub and Benchmark Suite for Southeast Asian Languages"`.
- Added: `s2_paper_id: ba5284674face6cca3b678fd7a82d691ec29349b`, `citation_count: 41`.
- Not carried: `rv_indigenous: 70` and `religious_values: Indigenous`, which were inferred from "1,300 indigenous languages".
- **Not changed (owner):** the kept note's `rv_christianity: 50` is also a false positive. The only matches are author first names such as Jan *Christian* Blaise Cruz.

## References changed

**Author profiles (24 line edits; all deletions are list lines `- [[stem|…]]`):**
- **9 deletions** of `[[2025-Halgamuge-Indigenous Peoples and Artificial Intelligence A|…]]`. Each of these profiles already listed the kept Perera note.
  - Maneesha Perera
  - Rajith Vidanaarachchi
  - Rajith Vidanaarachchi Maneesha Perera
  - Sangeetha Chandrashekeran
  - Melissa Kennedy
  - Melissa Kennedy Sangeetha Chandrashekeran
  - Brendan Kennedy
  - Saman Halgamuge
  - Saman Halgamuge Brendan Kennedy
- **7 deletions** of `[[2025-Sun-Decoding Moral Responses in AI A Quantitative Analysis of Large|…]]`, not re-pointed.
  - Chenkai Sun
  - Jinning Li
  - Yi R. Fung
  - Hou Pong Chan
  - Tarek Abdelzaher
  - ChengXiang Zhai
  - Heng Ji
  - Five of these profiles now list no papers: Jinning Li, Yi R. Fung, Hou Pong Chan, Tarek Abdelzaher, ChengXiang Zhai. **They were left in place** for the owner to recycle, or to keep if SocialSense is added as a note.
- **3 deletions** of `[[2025-Snoswell-Beyond Verdicts Evaluating Language Model Moral Competence Aaron J.|…]]` in Aaron J. Snoswell, Seth Lazar and Daniel Kilov. Each already listed the kept Snoswell note.
- **1 deletion** of the Sacred-or-Synthetic line from `Authors/Islamic.md`, a garbage profile that still lists ALLaM.
- **4 additions** of `- [[2025-Islamic-Sacred or Synthetic Evaluating LLM Reliability and Abstention for|Sacred or Synthetic? Evaluating LLM Reliability and Abstention for Religious Questions]]`:
  - `Authors/Farah Atif.md` (First Author)
  - `Authors/Nursultan Askarbekuly.md`
  - `Authors/Kareem Darwish.md`
  - `Authors/Monojit Choudhury.md` (Last Author)

**Remaining plain-text lines.** Some profiles still have plain-text "*From <retired stem>*: Affiliation …" lines, not wikilinks:
- 3 garbage co-author profiles in the Perera group
- 5 SocialSense profiles
- Aaron J. Snoswell

These were left as they are.

**Benchmark candidates:** 8 entries deleted from `DASHBOARDS/cei-dashboard-14/build/benchmark_survey_candidates.json`.
- 7 came from the v14 new-paper review:
  - `2025-Hendra-Decoding Moral Responses in AI.md`
  - `2025-Atif-Sacred or Synthetic Evaluating LLM Reliability.md`
  - `2024-Unknown-Exploring psychology LLMs moral legal reasoning.md`
  - `2024-Unknown-Measuring Spiritual Values Bias Large Language.md`
  - `2025-Unknown-Normative Evaluation Large Language Models Everyday.md`
  - `2025-Unknown-Can LLMs Grasp Implicit Cultural Values.md`
  - `2024-Lovenia-SEACrowd Multilingual Multimodal Data Hub Benchmark.md`
- 1 was v13-derived: `2025-Sun-Decoding Moral Responses in AI A Quantitative Analysis of Large.md`.
- The entries were deleted, not re-pointed, because every kept benchmark note already has its own entry.

**Files moved (`git mv`, 19):** the 16 retired notes into `RECYCLE-BIN/20261018-duplicate-merge/papers/`, plus these 3 extracts:
- `PDF Extracts/2025/2025-Sun-Decoding Moral Responses in AI A Quantitative Analysis of Large.md`
- `PDF Extracts/0000/2025-Sun-Decoding Moral Responses in AI A Quantitative Analysis of Large.md`
- `PDF Extracts/2025/2025-Snoswell-Beyond Verdicts Evaluating Language Model Moral Competence Aaron J..md`

## References left in immutable or generated files

These files are dated reports, snapshots or provenance, and were not edited under the report-immutability rule. Use the table at the top to resolve a retired stem.
- **Generated files**, which will update on the next build: `DASHBOARDS/cei-dashboard-14/data*.js`, and `logs/20261018-author_*.json` (gitignored).
- **Files with wikilinks** to retired stems, which will dangle in Obsidian:
  - Sun:
    - `STATISTICS/ARCHIVE/20260208-llm-ethics-benchmark-survey.md`
    - `STATISTICS/ARCHIVE/20260215-llm-ethics-benchmark-survey.md`
    - `STATISTICS/ARCHIVE/20260216-llm-ethics-benchmark-survey.md`
    - `STATISTICS/ARCHIVE/20260210-ethical-values-alignment-benchmarks-report.md`
    - `STATISTICS/ARCHIVE/20260213-ethical-values-alignment-benchmarks-report.md`
    - `STATISTICS/ARCHIVE/20260215-ethical-values-alignment-benchmarks-report.md`
    - `STATISTICS/ARCHIVE/20260216-ethical-values-alignment-benchmarks-report.md`
    - `STATISTICS/ARCHIVE/20260210-vault-overview-report.md`
    - `STATISTICS/ARCHIVE/20260212-vault-overview-report.md`
    - `STATISTICS/ARCHIVE/20260213-vault-overview-report.md`
    - `STATISTICS/ARCHIVE/20260215-vault-overview-report.md`
    - `STATISTICS/ARCHIVE/20260216-vault-overview-report.md`
    - `NORM-ETHICS/STATISTICS/20260207-normative-ethics-benchmarks-v3-report.md`
    - `NORM-ETHICS/STATISTICS/20260208-normative-ethics-benchmarks-v4-report.md`
  - Halgamuge: `STATISTICS/ARCHIVE/20260215-llm-assessment-data-availability-report.md`, `STATISTICS/ARCHIVE/20260216-religious-ethical-tradition-gap-analysis.md`
  - Snoswell LSRC0693: `STATISTICS/ARCHIVE/20260215-llm-assessment-data-availability-report.md`, `STATISTICS/ARCHIVE/20260216-llm-assessment-data-availability-report.md`

**Bare filename references**, counted in files per retired note:

| Retired stem | Files | Where |
|---|---|---|
| 2025-UbuntuAI-AI Ethics Meets Ubuntu Governance | 14 | COOKBOOK/30-EVIDENCE 9 (including card `20260705-cards/2025-UbuntuAI-…card.md`), CULTURAL-GLOBAL 1, MORAL-PSYCH 1, v14 build provenance 3 |
| 2025-Perera-Indigenous Peoples and AI Systematic Review | 15 | COOKBOOK 10 (including its card), CULTURAL-GLOBAL 1, MORAL-PSYCH 1, v14 build provenance 3 |
| 2025-Halgamuge-Indigenous Peoples and Artificial Intelligence A | 95 | older DASHBOARDS 43, STATISTICS 21, CULTURAL-GLOBAL 16 (including COUNCIL gold-standard sheets), logs 12, RELIGIOUS-VALUES 3 |
| 2025-IndigenousEthics-Indigenous Ethics and AI | 13 | COOKBOOK 8 (including its card), CULTURAL-GLOBAL 1, MORAL-PSYCH 1, v14 build provenance 3 |
| 2025-Hendra-Decoding Moral Responses in AI | 15 | COOKBOOK 10 (including its card and dossier tables), CULTURAL-GLOBAL 1, MORAL-PSYCH 1, v14 build provenance 3 |
| 2025-Sun-Decoding Moral Responses in AI A Quantitative Analysis of Large | 92 | older DASHBOARDS 44, STATISTICS 32, CULTURAL-GLOBAL 9, NORM-ETHICS 3, logs 3, MORAL-PSYCH 1 |
| 2025-Atif-Sacred or Synthetic Evaluating LLM Reliability | 19 | MORAL-PSYCH 9, CULTURAL-GLOBAL 6, RELIGIOUS-VALUES 1, v14 build provenance 3 |
| 2025-Snoswell-Beyond Verdicts Evaluating Language Model Moral | 5 | CULTURAL-GLOBAL 2, MORAL-PSYCH 1, v14 build provenance 2 |
| 2025-Snoswell-Beyond Verdicts Evaluating Language Model Moral Competence Aaron J. | 102 | older DASHBOARDS 43, STATISTICS 20, COOKBOOK 10, CULTURAL-GLOBAL 10, MORAL-PSYCH 10, logs 5, RELIGIOUS-VALUES 3, ABSTRACT_FETCH_RESULTS.md 1 |
| 2024-Unknown-Exploring psychology LLMs moral legal reasoning | 6 | CULTURAL-GLOBAL 2, MORAL-PSYCH 1, v14 build provenance 3 |
| 2020-Hongladarom-Ethics of AI and Robotics | 9 | CULTURAL-GLOBAL 6, v14 build provenance 3 |
| 2005-Teaiwa-Articulated Cultures Militarism and Masculinities | 9 | CULTURAL-GLOBAL 6, v14 build provenance 3 |
| 2024-Unknown-Measuring Spiritual Values Bias Large Language | 15 | CULTURAL-GLOBAL 8, RELIGIOUS-VALUES 4, v14 build provenance 3 |
| 2025-Unknown-Normative Evaluation Large Language Models Everyday | 6 | CULTURAL-GLOBAL 2, MORAL-PSYCH 1, v14 build provenance 3 |
| 2025-Unknown-Can LLMs Grasp Implicit Cultural Values | 15 | CULTURAL-GLOBAL 8, RELIGIOUS-VALUES 4, v14 build provenance 3 |
| 2024-Lovenia-SEACrowd Multilingual Multimodal Data Hub Benchmark | 16 | CULTURAL-GLOBAL 10, RELIGIOUS-VALUES 4, v14 build provenance 2 |

"v14 build provenance" means `overlay_v14.json`, `new-paper-review/results_*.json` and `likely_duplicates.txt`. If `PYTHON/apply_v14_classifications.py` is re-run, it will report "paper not found" for the 12 retired notes that are in the overlay. That is expected.

## Left for the owner

1. Move 2 retired PDFs in the external PDF folder into that folder's own `RECYCLE-BIN/`. They are outside the repo and were not moved here.
   - `2025/2025-Sun-Decoding Moral Responses in AI A Quantitative Analysis of Large.pdf`, plus any copy under `Utilitarian Ethics/Borderline/`. This is the SocialSense PDF; keep it instead if SocialSense will be added as a note.
   - `2025/2025-Snoswell-Beyond Verdicts Evaluating Language Model Moral Competence Aaron J..pdf`, a duplicate.
2. Recycle or keep the 5 SocialSense author profiles that now list no papers.
3. Confirm Hui et al.'s full author list. Clean up Hui's invalid PDF and extracts, and its fabricated `external_pdf`.
4. Data fixes found but not applied:
   - SEACrowd `rv_christianity` false positive.
   - Perera `author_country` should be AU.
   - Ubuntu note `author_country: SG` despite unknown authors.
   - Hongladarom book: `rv_buddhism: 0` and missing subtitle.
   - Garbage profiles `Authors/Islamic.md` and `Authors/5 others.md`.
5. Update `DASHBOARDS/cei-dashboard-14/build/README.md` counts (1,073 / 985 / 88), and rebuild when ready.
