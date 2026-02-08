# Missing PDFs & Orphan PDFs Report

**Generated:** 2026-02-08
**Vault:** 923 papers | 922 unique PDF stems (1004 total files incl. ethics-framework copies)

---

## Summary

| Category | Count |
|----------|-------|
| Papers missing PDFs | 26 |
| Orphan PDFs (no matching paper) | 25 |
| Section 1: Duplicate orphans safe for RECYCLE-BIN | 20 |
| Section 2: Papers truly missing PDFs (incl. 2 with orphan matches) | 26 |
| Section 3a: Fixable — rename orphan PDF to match paper | 2 |
| Section 3b–c: Investigate or RECYCLE-BIN | 3 |
| Section 4: Broken `local_pdf` YAML links | 24 (19 wrong path + 5 no PDF) |

---

## Section 1: Duplicate Orphan PDFs — Safe to RECYCLE-BIN (20)

These orphan PDFs are leftover filenames from author renames, year corrections, or title adjustments. Each one has a corresponding paper that **already has a correctly-named PDF**, so these orphans are **safe to move to RECYCLE-BIN**.

### 1a. Unknown-Author Rename Leftovers (7)

Old `Unknown`-prefixed PDFs from before the author discovery batch. The paper and its correct PDF already exist.

| # | Orphan PDF | Matched Paper (has PDF ✓) |
|---|-----------|--------------------------|
| 1 | `[[PDFs/2020/2020-Unknown-Machine Ethics - Creation of a Virtuous Machine.pdf]]` | `[[2020-Akrout-Machine Ethics - Creation of a Virtuous Machine]]` |
| 2 | `[[PDFs/2022/2022-Unknown-A Virtue-Based Framework for AI Ethics in Practice.pdf]]` | `[[2022-Hagendorff-Virtue-Based Framework for AI Ethics]]` |
| 3 | `[[PDFs/2022/2022-Unknown-Automated Ethical Practical Reasoning.pdf]]` | `[[2025-Sullins-Automated Ethical Practical Reasoning]]` |
| 4 | `[[PDFs/2022/2022-Unknown-Can Robotic AI Systems Be Virtuous.pdf]]` | `[[2022-Constantinescu-Can Robotic AI Be Virtuous]]` |
| 5 | `[[PDFs/2024/2024-Unknown-Computational Complexity of Ethics.pdf]]` | `[[2024-Stenseke-Computational Complexity of Ethics]]` |
| 6 | `[[PDFs/2025/2025-Unknown-AI Practical Wisdom and Compassion.pdf]]` | `[[2025-Graves-AI Practical Wisdom and Compassion]]` |
| 7 | `[[PDFs/2025/2025-Unknown-Virtue in the Machine.pdf]]` | `[[2025-Gounaris-Virtue in the Machine]]` |

### 1b. Title Drift / Truncation Leftovers (8)

Old PDF names from before papers were renamed to shorter or corrected titles. The paper already has a correctly-named PDF.

| # | Orphan PDF | Matched Paper (has PDF ✓) |
|---|-----------|--------------------------|
| 8 | `[[PDFs/2024/2024-Agarwal-Ethical Reasoning and Moral Value Alignment of.pdf]]` | `[[2024-Agarwal-Ethical Reasoning and Moral Value Alignment]]` (trailing "of" trimmed) |
| 9 | `[[PDFs/2024/2024-Ji-MoralBench Moral Evaluation of LLMs.pdf]]` | `[[2024-Ji-MoralBench]]` (long-form → short title) |
| 10 | `[[PDFs/2025/2025-Baum-Aggregation Problems Machine Ethics.pdf]]` | `[[2025-Baum-Aggregation Problems in Machine Ethics]]` |
| 11 | `[[PDFs/2025/2025-Chakraborty-Structured Moral Reasoning in Language Models.pdf]]` | `[[2025-Chakraborty-Structured Moral Reasoning]]` |
| 12 | `[[PDFs/2025/2025-Jiao-LLM Ethics Benchmark A Three-Dimensional Assessment.pdf]]` | `[[2025-Jiao-LLM Ethics Benchmark]]` |
| 13 | `[[PDFs/2025/2025-Sachdeva-Normative Evaluation of Large Language Models.pdf]]` | `[[2025-Sachdeva-Normative Evaluation of LLMs with Everyday Moral Dilemmas]]` |
| 14 | `[[PDFs/2025/2025-Samway-Are Language Models Consequentialist or.pdf]]` | `[[2025-Samway-Are Language Models Consequentialist or Deontological]]` |
| 15 | `[[PDFs/2025/2025-Unknown-Large Language Models Meet Moral Values.pdf]]` | `[[2025-Bulla-Large Language Models meet moral values]]` |

### 1c. Year-Change or Punctuation Leftovers (5)

Old PDFs where the year was corrected or special characters changed. The paper already has a correctly-named PDF.

| # | Orphan PDF | Matched Paper (has PDF ✓) |
|---|-----------|--------------------------|
| 16 | `[[PDFs/2024/2024-Mougan-Kantian Deontology Meets AI Alignment.pdf]]` | `[[2023-Mougan-Kantian Deontology Meets AI Alignment]]` (year corrected to 2023) |
| 17 | `[[PDFs/2024/2024-Tennant-Moral Alignment for LLM Agents.pdf]]` | `[[2025-Tennant-Moral Alignment for LLM Agents]]` (year corrected to 2025) |
| 18 | `[[PDFs/2024/2024-D'Alessandro-Deontology and safe artificial intelligence.pdf]]` | `[[2024-DAlessandro-Deontology and Safe Artificial Intelligence]]` (apostrophe removed in paper name) |
| 19 | `[[PDFs/2023/2023-Shen-"Do Anything Now".pdf]]` | `[[2023-Shen-"Do Anything Now"]]` (straight quotes → curly quotes) |
| 20 | `[[PDFs/2025/2025-LaCroix-Metaethical perspectives on 'benchmarking' AI.pdf]]` | `[[2025-LaCroix-Metaethical perspectives on 'benchmarking' AI]]` (straight quotes → curly quotes) |

> **Recommended action:** `mv` all 20 orphan PDFs to `RECYCLE-BIN/`. They are duplicates of PDFs the paper already links to.

---

## Section 2: Papers Truly Missing PDFs (26)

All 26 papers whose stem does not match any PDF filename. Two (Vallor, Farina) have orphan PDFs that can be renamed to resolve the gap — see Section 3a.

### 2a. Books / Monographs (4)

No digital PDF expected — these are published books.

| # | Paper | DOI/URL | Notes |
|---|-------|---------|-------|
| 1 | `[[2024-Vallor-The AI Mirror]]` | `10.1093/oso/9780197759080.001.0001` | **Has PDF in INBOX** — see Section 3, Special Cases |
| 2 | `[[2025-Elder-The Ethics of Digital Ghosts]]` | `10.4324/9781003632658` | Routledge book |
| 3 | `[[2025-Rourke-Mind Crime]]` | [Goodreads](https://www.goodreads.com/book/show/226055728-mind-crime) | Fiction/philosophy book |
| 4 | `[[2021-Sullins-Artificial Phronesis - What It Is and Is Not]]` | `10.1093/oso/9780190081713.003.0015` | Book chapter (OUP) |

### 2b. Paywalled / Anti-Bot Protected (11)

PDFs exist online but are behind paywalls or Cloudflare protection.

| # | Paper | DOI/URL | Publisher |
|---|-------|---------|-----------|
| 5 | `[[2024-Farina-AI and Society Virtue Ethics Approach]]` | `10.1007/s00146-022-01545-5` | Springer — **has orphan PDF**, see Section 3a |
| 6 | `[[2020-Awad-Crowdsourcing moral machines]]` | `10.1145/3339904` | ACM DL |
| 7 | `[[2023-Boddington-Normative Ethical Theory AI Ethics]]` | `10.1007/978-981-19-9382-4_6` | Springer (book chapter) |
| 8 | `[[2023-Stenseke-Use and Abuse Normative Ethics Moral Machines]]` | `10.3233/FAIA220614` | IOS Press |
| 9 | `[[2024-Anonymous-ForbiddenQuestions]]` | `10.1145/3658644.3670388` | ACM DL |
| 10 | `[[2024-McGee-How Ethical Is Utilitarian Ethics]]` | `10.2139/ssrn.4731871` | SSRN |
| 11 | `[[2024-Muyskens-Can an AI-carebot be filial]]` | `10.1177/09697330241238332` | SAGE |
| 12 | `[[2024-Ribeiro-Machine Ethics Architecture of Virtue]]` | `10.1007/978-3-031-48855-9_29` | Springer (book chapter) |
| 13 | `[[2025-Bryan-Virtue Ethics and Postponing Human Extinction]]` | `10.1001/amajethics.2025.611` | AMA Journal of Ethics |
| 14 | `[[2025-Cheung-LLMs Amplified Cognitive Biases Moral]]` | `10.1073/pnas.2412015122` | PNAS |
| 15 | `[[2025-Muntean-Moral Coherentism Theoretical Framework Muntean]]` | `10.5406/21521123.62.3.06` | Unknown publisher |

### 2c. Open-Access but Not Yet Downloaded (5)

These should be downloadable — may need manual retrieval.

| # | Paper | DOI/URL | Notes |
|---|-------|---------|-------|
| 16 | `[[2024-Wilders-Socratic Dialogue for Virtue Ethics in AI]]` | [AAAI AIES](https://ojs.aaai.org/index.php/AIES/article/view/36748) | AAAI OJS — may need 3-part URL |
| 17 | `[[2024-Zhou-tSMC]]` | [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2024/hash/48726631f87322012c6be38e00c72a47-Abstract-Conference.html) | NeurIPS proceedings |
| 18 | `[[2025-Ochasi-Reframing Justice in Healthcare AI]]` | `10.1111/dewb.70007` | Wiley — try EuropePMC |
| 19 | `[[2025-Rashid-Evaluating Prompt Injection Attacks with]]` | `10.3390/make7030077` | MDPI (open access) |
| 20 | `[[2025-Sameer-Insights into Moral Reasoning of AI]]` | `10.1080/23736992.2025.2553146` | Taylor & Francis |

### 2d. Web-Only / No PDF Applicable (4)

| # | Paper | URL | Notes |
|---|-------|-----|-------|
| 21 | `[[2023-Lakera-GandalfIgnoreInstructions]]` | [lakera.ai](https://www.lakera.ai/blog/who-is-gandalf) | Blog post / interactive demo |
| 22 | `[[2025-Center-Personal Consultations Case Study Database]]` | [ncbcenter.org](https://www.ncbcenter.org/case-study-database) | Web database |
| 23 | `[[2025-Consortium-The Vals Legal AI Report (VLAIR)]]` | [vals.ai](https://www.vals.ai/vlair) | Web report |
| 24 | `[[2025-onejune2018-Awesome-LLM-Eval Repository Meta-Resource]]` | — | GitHub awesome-list (no_pdf_applicable) |

### 2e. Other Missing (2)

| # | Paper | DOI/URL | Notes |
|---|-------|---------|-------|
| 25 | `[[2025-Shahriar-Priv-IQ]]` | [MDPI](https://www.mdpi.com/2673-2688/6/2/29) | MDPI — should be open access |
| 26 | `[[2025-Velay-Vitow-Putting the AI in Eudaimonia]]` | [therepublicjournal.com](https://therepublicjournal.com/putting-the-ai-in-eudaimonia/) | Online journal |

---

## Section 3: Remaining Orphan PDFs (5)

These orphan PDFs are not simple duplicates — they require manual investigation or action.

### 3a. Fixable Mismatches — Rename PDF to Match Paper (2)

These orphans map to papers that currently have **no PDF**. Renaming (or moving) the PDF will fix the paper's missing PDF.

| # | Orphan PDF | Matching Paper (missing PDF) | Action |
|---|-----------|------------------------------|--------|
| 1 | `[[PDFs/INBOX/The AI Mirror _ How to Reclaim Our Humanity in an Age of -- Shannon Vallor -- Oxford University Press USA, New York, NY, 2024.pdf]]` | `[[2024-Vallor-The AI Mirror]]` | Rename to `PDFs/2024/2024-Vallor-The AI Mirror.pdf` and set `local_pdf` |
| 2 | `[[PDFs/2024/2024-Farina-AI and Society - A Virtue Ethics Approach.pdf]]` | `[[2024-Farina-AI and Society Virtue Ethics Approach]]` | Rename PDF to `2024-Farina-AI and Society Virtue Ethics Approach.pdf` and set `local_pdf` |

### 3b. Stenseke 2023 Orphans — Unmatched Publications (2)

These appear to be copies of the 2021 Stenseke paper or a different publication. The only 2023 Stenseke paper in the vault (`2023-Stenseke-Use and Abuse Normative Ethics Moral Machines`) is an entirely different work.

| # | Orphan PDF | Notes |
|---|-----------|-------|
| 3 | `[[PDFs/2023/2023-Stenseke-Artificial Virtuous Agents.pdf]]` | May be a 2023 version/reprint of `[[2021-Stenseke-Artificial Virtuous Agents]]` — duplicate, safe for RECYCLE-BIN |
| 4 | `[[PDFs/2023/2023-Stenseke-Artificial Virtuous Agents - Theory to.pdf]]` | Likely truncated filename of a Stenseke thesis/book chapter — investigate or RECYCLE-BIN |

### 3c. No Matching Paper (1)

| # | Orphan PDF | Notes |
|---|-----------|-------|
| 5 | `[[PDFs/2025/2025-Sachdeva-Deliberative Dynamics and Value Alignment.pdf]]` | No matching paper in vault. May need a new paper entry or investigation. Same author has `[[2025-Sachdeva-Normative Evaluation of LLMs with Everyday Moral Dilemmas]]` (different work) |

---

## Section 4: Broken `local_pdf` YAML Links (24)

### 4a. Wrong Path Format — PDF Exists but Link Missing Year Directory (19)

These papers have a `local_pdf` wikilink that omits the `PDFs/YYYY/` prefix (uses bare filename or old path). The PDF exists on disk at the correct year-based path.

**Fix:** Update `local_pdf` to include the `PDFs/YYYY/` prefix.

| # | Paper | Current (broken) link | Correct path |
|---|-------|-----------------------|-------------|
| 1 | `[[2010-Project-GurbaniDB]]` | `[[2010-Project-GurbaniDB.pdf]]` | `[[PDFs/2010/2010-Project-GurbaniDB.pdf]]` |
| 2 | `[[2020-Akrout-Machine Ethics - Creation of a Virtuous Machine]]` | `[[2020-Akrout-Machine Ethics - Creation of a Virtuous Machine.pdf]]` | `[[PDFs/2020/2020-Akrout-Machine Ethics - Creation of a Virtuous Machine.pdf]]` |
| 3 | `[[2022-Bago-Situational factors shape moral judgments in the]]` | `[[2022-Bago-Situational factors shape moral judgments in the.pdf]]` | `[[PDFs/2022/2022-Bago-Situational factors shape moral judgments in the.pdf]]` |
| 4 | `[[2023-Lee-VisAlign]]` | `[[2023-Lee-VisAlign.pdf]]` | `[[PDFs/2023/2023-Lee-VisAlign.pdf]]` |
| 5 | `[[2024-Akhtar-The Ethicsophical Landscape of Large Language]]` | `[[2024-Akhtar-The Ethicsophical Landscape of Large Language.pdf]]` | `[[PDFs/2024/2024-Akhtar-The Ethicsophical Landscape of Large Language.pdf]]` |
| 6 | `[[2024-Kaiyom-HELM Safety]]` | `[[2024-Kaiyom-HELM Safety.pdf]]` | `[[PDFs/2024/2024-Kaiyom-HELM Safety.pdf]]` |
| 7 | `[[2024-Leech-Ten Hard Problems in Artificial Intelligence We]]` | `[[2024-Leech-Ten Hard Problems in Artificial Intelligence We.pdf]]` | `[[PDFs/2024/2024-Leech-Ten Hard Problems in Artificial Intelligence We.pdf]]` |
| 8 | `[[2024-Levine-Religious Affiliation and Conceptions of the]]` | `[[2024-Levine-Religious Affiliation and Conceptions of the.pdf]]` | `[[PDFs/2024/2024-Levine-Religious Affiliation and Conceptions of the.pdf]]` |
| 9 | `[[2024-Mou-SG-Bench]]` | `[[2024-Mou-SG-Bench.pdf]]` | `[[PDFs/2024/2024-Mou-SG-Bench.pdf]]` |
| 10 | `[[2024-Salvador-A SCHEMATIC FOR APPROVAL REGULATION OF FRONTIER AI]]` | `[[2024-Salvador-A SCHEMATIC FOR APPROVAL REGULATION OF FRONTIER AI.pdf]]` | `[[PDFs/2024/2024-Salvador-A SCHEMATIC FOR APPROVAL REGULATION OF FRONTIER AI.pdf]]` |
| 11 | `[[2025-Banerjee-SafeInfer]]` | `[[2025-Banerjee-SafeInfer.pdf]]` | `[[PDFs/2025/2025-Banerjee-SafeInfer.pdf]]` |
| 12 | `[[2025-Colijn-Technical Risks of (Lethal) Autonomous Weapons]]` | `[[2025-Colijn-Technical Risks of (Lethal) Autonomous Weapons.pdf]]` | `[[PDFs/2025/2025-Colijn-Technical Risks of (Lethal) Autonomous Weapons.pdf]]` |
| 13 | `[[2025-Hatemo-Revisiting the Trolley Problem for AI]]` | `[[2025-Hatemo-Revisiting the Trolley Problem for AI.pdf]]` | `[[PDFs/2025/2025-Hatemo-Revisiting the Trolley Problem for AI.pdf]]` |
| 14 | `[[2025-Jacovi-The FACTS Grounding Leaderboard]]` | `[[2025-Jacovi-The FACTS Grounding Leaderboard.pdf]]` | `[[PDFs/2025/2025-Jacovi-The FACTS Grounding Leaderboard.pdf]]` |
| 15 | `[[2025-Laukkonen-Contemplative Artificial Intelligence]]` | `[[2025-Laukkonen-Contemplative Artificial Intelligence.pdf]]` | `[[PDFs/2025/2025-Laukkonen-Contemplative Artificial Intelligence.pdf]]` |
| 16 | `[[2025-Li-T2ISafety]]` | `[[2025-Li-T2ISafety.pdf]]` | `[[PDFs/2025/2025-Li-T2ISafety.pdf]]` |
| 17 | `[[2025-Okamoto-AI-based medical ethics education]]` | `[[2025-Okamoto-AI-based medical ethics education.pdf]]` | `[[PDFs/2025/2025-Okamoto-AI-based medical ethics education.pdf]]` |
| 18 | `[[2025-Pipitone-Unlocking practical wisdom]]` | `[[2025-Pipitone-Unlocking practical wisdom.pdf]]` | `[[PDFs/2025/2025-Pipitone-Unlocking practical wisdom.pdf]]` |
| 19 | `[[2025-Steen-Ethical aspects of ChatGPT]]` | `[[2025-Steen-Ethical aspects of ChatGPT.pdf]]` | `[[PDFs/2025/2025-Steen-Ethical aspects of ChatGPT.pdf]]` |

### 4b. Truly Broken — No PDF on Disk (5)

These papers have `local_pdf` links pointing to files that don't exist, and no PDF is available on disk under any name.

| # | Paper | Broken link |
|---|-------|-------------|
| 1 | `[[2023-Boddington-Normative Ethical Theory AI Ethics]]` | `[[PDFs/2023/2023-Boddington-Normative Ethical Theory AI Ethics.pdf]]` |
| 2 | `[[2023-Stenseke-Use and Abuse Normative Ethics Moral Machines]]` | `[[PDFs/2023/2023-Stenseke-Use and Abuse Normative Ethics Moral Machines.pdf]]` |
| 3 | `[[2024-Ribeiro-Machine Ethics Architecture of Virtue]]` | `[[PDFs/2024/2024-Ribeiro-Machine Ethics Architecture of Virtue.pdf]]` |
| 4 | `[[2025-Cheung-LLMs Amplified Cognitive Biases Moral]]` | `[[PDFs/2025/2025-Cheung-LLMs Amplified Cognitive Biases Moral.pdf]]` |
| 5 | `[[2025-Ochasi-Reframing Justice in Healthcare AI]]` | `[[PDFs/2025/2025-Ochasi-Reframing Justice in Healthcare AI.pdf]]` |

> These 5 papers also appear in Section 2 (Truly Missing PDFs). The `local_pdf` field was set optimistically during import but the download failed.

---

## Recommended Actions

### Quick Wins (automated)
1. **Fix 19 broken `local_pdf` paths** — add `PDFs/YYYY/` prefix (batch regex script)
2. **Move 20 duplicate orphan PDFs to RECYCLE-BIN** — Section 1 items are confirmed duplicates

### Manual Actions
3. **Rename Farina PDF** — `2024-Farina-AI and Society - A Virtue Ethics Approach.pdf` → `2024-Farina-AI and Society Virtue Ethics Approach.pdf` and set `local_pdf`
4. **Rename + move Vallor PDF** — from INBOX to `PDFs/2024/2024-Vallor-The AI Mirror.pdf` and set `local_pdf`
5. **Investigate 3 remaining orphans** — Sachdeva "Deliberative Dynamics" (new paper entry?), 2× Stenseke 2023 (RECYCLE-BIN?)
6. **Attempt manual download** of 5 open-access missing PDFs (Section 2c)
7. **Clear 5 broken `local_pdf` fields** (Section 4b) — set to `N/A` or remove field

---

*Report generated by vault audit script. Cross-reference with `logs/20260208-manual_pdf_research_report.md` for prior acquisition attempts.*
