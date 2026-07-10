# Council Deliberation D-01: Literature Coverage Review

**Date:** 2026-04-03
**Charge:** Review the 125-paper BACKGROUND literature collection for completeness, quality, balance, and gaps. Each expert assesses their assigned folders.

**File Workflow:** All future analysis uses `EXTRACT/*.md` (text extracts), NOT the original PDFs in `ORIG/`. The `ORIG/` folder is gitignored. 89 of 125 papers have been extracted (71%). 36 papers lack PDFs (books, paywalled).

---

## Expert Assessments

### Expert 1 — Prof. Sachedina (Islamic Ethics & Bioethics)
**Folders reviewed:** 04-islamic-ai-ethics (12 papers), 09-ai-bias-religion (10 papers)

**Assessment: STRONG coverage for Islamic AI ethics.**

Folder 04 captures the essential landscape: Maqasid al-Shariah frameworks (Kamali 2008, Mohadi 2024, Habib 2023), Islamic virtue ethics (Al-Musawi 2022), trusteeship ethics (Muravyov 2025), and the crucial pluralist benchmarking paper (Ezzeddine 2024). The Quranic NLP entries (HAQA/QUQA, Al-Bayan, IslamicMMLU) ground the theoretical work in actual data artifacts.

**Gap identified:** Missing the Indonesian Islamic AI discourse — Indonesia has the world's largest Muslim population and an active Islamic fintech AI sector. Recommend adding 1-2 papers on Indonesian Islamic AI governance.

**Bias folder (09):** The Abid et al. (2021) anti-Muslim bias paper is correctly prioritized as must_read. The newer papers (Hamid 2025, Putri 2025) show the field is moving from detection to systematic evaluation. Good temporal coverage.

---

### Expert 2 — Prof. Waters (Christian Theological Ethics)
**Folder reviewed:** 05-christian-ethics-ai (11 papers)

**Assessment: GOOD coverage, with a denominational balance concern.**

Strong on Catholic social teaching (Laudato Si', Rome Call, Catholic Social Teaching + AI Healthcare). The addition of Johnson (2026) on doctrinal flattening in AI is excellent — this directly addresses whether LLMs can represent theological nuance.

**Gap identified:** Protestant evangelical perspectives are underrepresented. The collection leans Catholic-institutional. Missing: (1) a Reformed/evangelical theology of technology paper; (2) World Council of Churches AI statements; (3) Orthodox Christian perspectives on technology and personhood. Recommend 2-3 additions.

**Methodological note:** Herzfeld (2002) and Thweatt-Bates (2012) are correctly included as foundational theological anthropology works, even though they predate the LLM era. These provide the theological vocabulary the paper needs.

---

### Expert 3 — Prof. Bilimoria (Dharmic Philosophy)
**Folder reviewed:** 06-dharmic-ethics-ai (9 papers)

**Assessment: ADEQUATE but the thinnest tradition-specific folder. Reflects genuine literature scarcity.**

Chadha (2023) on decolonial AI alignment via Visesa-Dharma is the standout — it's the only paper that seriously engages Hindu philosophical categories with alignment methodology. The Mohanty (2024) Indic approach paper is also strong.

**Gaps identified:**
1. **Buddhist AI ethics is underrepresented** — only 2 papers (Keown foundational, Brekke supplementary). Missing the Thai Buddhist approach to robotics and the Tibetan Buddhist computational mind literature (e.g., work at Mind & Life Institute intersecting with AI).
2. **Jain AI ethics is essentially absent** — Chapple (2019) is supplementary and tangential. The ahimsa-AI connection deserves a dedicated paper, though the literature is genuinely sparse.
3. **Sikh contributions** — Singh & Kaur (2024) is the sole entry. The Sikh data governance work emerging from Punjab tech sector deserves mention.

**This folder's thinness is itself a finding:** The scarcity of Dharmic AI ethics literature mirrors the 0-benchmark gap the main pipeline found for Jainism.

---

### Expert 4 — Prof. Li (Confucian Philosophy)
**Folder reviewed:** 12-east-asian-philosophy-ai (8 papers)

**Assessment: GOOD for Confucian coverage, WEAK for Taoist and Shinto.**

The "Intelligence and Wisdom" edited volume (Li & Wang 2022) and the "Can a Machine Flow Like Dao?" chapter (Li 2022) are essential. Wong (2019) on Confucian ethics of technology provides philosophical depth. The Asghari (2023) China-EU comparative is practically relevant.

**Gaps identified:**
1. **Shinto-specific AI literature is genuinely sparse.** Yamada (2023) is the only entry, and it may be difficult to find the actual PDF. The Japanese roboethics literature (Kaplan, MacDorman) touches Shinto themes but doesn't engage the tradition deeply.
2. **Korean AI ethics** is entirely absent — there's a growing Korean Confucian AI ethics literature that should be represented.
3. **CValues** (Tao et al. 2024) is cross-referenced from folder 03 but not duplicated here, which is correct.

---

### Expert 5 — Dr. Osei-Mensah (African Philosophy & Ubuntu)
**Folder reviewed:** 10-indigenous-african-ai (10 papers)

**Assessment: STRONG and well-curated.**

The three foundational papers (Mhlambi 2020, Birhane 2021, Mohamed et al. 2020) correctly anchor the folder. The addition of Gwagwa (2025) on Ubuntu in African AI governance and Balogun (2025) on African Data Ethics from FAccT shows the field is maturing. Carroll et al. (2020) CARE Principles bridges Indigenous and African traditions.

**Gap identified:** Missing Yoruba iwa (character ethics) and Igbo ofo na ogu (justice/truth) applied to technology. Also missing Pacific Island (Pasifika) perspectives that share communal ethics with Ubuntu but have distinct frameworks. Recommend 1-2 additions from West African philosophy.

**Anti-essentialization note:** The folder correctly avoids treating "African" as monolithic — it includes Ubuntu, Indigenous spirituality, and data sovereignty as distinct streams. However, the council should note that West, East, and Southern African traditions have distinct philosophical vocabularies that this collection doesn't fully capture.

---

### Expert 6 — Dr. Koppel (Jewish Studies & Computational Talmudics)
**Folder reviewed:** 11-jewish-ethics-ai (10 papers)

**Assessment: GOOD for computational Talmudics, WEAKER for contemporary Jewish AI ethics.**

Abraham (2019) on the Talmudic Logic Project and Koppel et al. (2011) on computational approaches are correctly prioritized. The Levy (2024) paper on Jewish perspectives on conscious robots is timely.

**Gaps identified:**
1. **Bar-Ilan Responsa Project** — the pioneering computational halakha project from the 1960s — deserves a dedicated foundational entry.
2. **Contemporary Jewish bioethics + AI** intersection is thin. Dorff (2003) predates AI relevance. Need a post-2020 paper on Jewish bioethical reasoning applied to AI decision-making.
3. **Hebrew NLP benchmarks** — Wiesel & Segal (2023) is the only NLP entry. Missing the HebrewNLP community's work on religious text processing.

---

### Expert 7 — Dr. Liang (AI Evaluation & Benchmarking)
**Folders reviewed:** 01-ai-values-alignment (12 papers), 08-benchmark-psychometrics (11 papers)

**Assessment: STRONG for both folders.**

Folder 01 captures the essential evaluation landscape: HELM, MMLU, InstructGPT, RLHF, and the alignment survey literature. The Klingefjord (2024) "What Are Human Values?" paper is particularly important for framing why religious values are a distinct evaluation challenge.

Folder 08 is the methodological backbone of the paper. The Gupta (2025) LLM Psychometrics systematic review and Li (2025) "Measuring what Matters" paper are both critical additions that didn't exist when earlier BACKGROUND collections were built.

**Gap identified:** Missing the Inspect AI framework (UK AI Safety Institute) and the lm-eval-harness documentation as grey literature entries. These are the actual harnesses that religious benchmarks would run on.

---

### Expert 8 — Dr. Cramer (Cross-Cultural HCI & Psychology)
**Folder reviewed:** 03-cultural-values-ai (12 papers)

**Assessment: EXCELLENT coverage of the cultural values-AI intersection.**

The WEIRD paper (Henrich 2010), Schwartz values theory (2012), and Hofstede model (2011) provide the psychometric foundations. The 2024-2025 LLM cultural alignment papers (Sukiennik, Adilazuarda, Rao, Naous) show the field is rapidly maturing.

**Particularly valuable:** Rao (2025) "Randomness, Not Representation" — this paper challenges the reliability of cultural alignment evaluation, which is directly relevant to religious values benchmarks (where the same instability risks apply).

**No significant gaps.** This is the most complete folder in the collection.

---

### Expert 9 — Prof. Floridi (Philosophy of Information & AI Ethics)
**Folders reviewed:** 01-ai-values-alignment (support), 07-comparative-religious-ethics (10 papers)

**Assessment: GOOD for comparative ethics, though the folder needs to bridge philosophy and CS more explicitly.**

AI4People (2018) and Jobin et al. (2019) global landscape are correctly prioritized. The Green (2014) "Third Wave of Comparative Religious Ethics" is essential for positioning the paper's methodology.

**Gap identified:** Missing a direct bridge paper between comparative religious ethics methodology and AI evaluation methodology — most entries are either philosophy or CS, not both. The Younas (2025) "Cultural Co-Genesis" paper partially fills this, but a paper explicitly connecting comparative theology methods with benchmark design would strengthen the narrative.

---

### Expert 10 — Dr. Abid (NLP & Religious Text Computation)
**Folder reviewed:** 02-religious-nlp (10 papers)

**Assessment: GOOD, with the right mix of methodological caution and practical applications.**

Leavens et al. (2024) "Modeling the Sacred" is the most important paper in this folder — it directly addresses the ethical considerations of applying NLP to religious texts, which is exactly the caution this paper needs to voice. Alhindi et al. (2025) "NLP Approaches to the Bible, Quran, and Bhagavad Gita" from the CLRel workshop shows a dedicated venue is emerging.

**Gap identified:** Missing the LREC/COLING computational linguistics workshop papers on low-resource religious languages (Ge'ez, classical Arabic, Sanskrit, Pali). These papers address the practical NLP challenges of building benchmarks in the languages sacred texts were written in.

---

### Expert 11 — Dr. Birhane (Cognitive Science & AI Fairness)
**Folder reviewed:** 09-ai-bias-religion (10 papers)

**Assessment: STRONG and timely.**

The folder captures the rapid 2024-2025 growth in religious bias measurement. The Bianchi (2024) "Divine LLaMAs" paper and Buyl (2024) "Measuring Spiritual Values" paper represent the state of the art. The progression from Abid (2021) single-bias detection to Hamid (2025) systematic landscape mapping shows the field's maturation.

**Critical point:** The folder correctly includes both bias *detection* papers and bias *measurement* papers. These are different methodological traditions — the paper should distinguish between them. Detection asks "is there bias?"; measurement asks "how much and of what kind?"

**Gap identified:** Missing intersectionality papers — religious bias intersects with racial, gender, and national origin bias in LLMs. A paper on Muslim-woman or Jewish-male stereotyping in AI would strengthen the analysis.

---

### Expert 12 — Prof. Bryson (AI Governance & Comparative Ethics)
**Folders reviewed:** 07-comparative-religious-ethics (support), 03-cultural-values-ai (support)

**Assessment: ADEQUATE. The cross-folder coherence is good.**

The collection avoids a common trap: treating religious AI ethics as separate from secular AI ethics. The papers in folders 01, 03, 07, and 08 create a bridge narrative. The Algorethics paper (Pasquale & Ferraris 2025) on AI-law-religion relationships is a good addition.

**Structural observation:** The 12-folder structure may be too fine-grained for a single paper's literature review. Recommend organizing the actual paper's lit review into 4-5 sections that group these folders, rather than trying to cover all 12 distinctly.

---

### Expert 13 — Dr. Pearce (Psychometrics & Educational Measurement)
**Folder reviewed:** 08-benchmark-psychometrics (11 papers)

**Assessment: STRONG. The recent psychometric critique literature is well-represented.**

The Gupta (2025) systematic review is essential — it's the first comprehensive survey of LLM psychometrics. The "Measuring what Matters" (Li 2025) paper directly argues that construct validity should be the primary concern in LLM benchmarks, which is exactly the argument this paper needs to make for religious values benchmarks.

**Gap identified:** Missing item response theory (IRT) applications to NLP benchmarks. The PATCH framework (Srivastava 2024) touches on this but a dedicated IRT-for-NLP paper would strengthen the psychometric argument. Also missing: measurement invariance testing across religious/cultural groups — a paper on DIF (differential item functioning) in cross-cultural assessments would be directly relevant.

---

### Expert 14 — Dr. Awosanya (Statistical Methods & Bibliometrics)
**Scope:** All folders (meta-review)

**Assessment: The collection is methodologically sound but has systematic underrepresentation of non-English-language scholarship.**

**Bibliometric observations:**
1. **Temporal distribution is appropriate:** 41% from 2024-2026 (recency), 12% pre-2015 (foundational depth). The 2022-2023 cohort (24%) fills the middle well.
2. **Source diversity:** 42 journal articles, 22 conference papers, 32 working papers — a healthy mix. The 11 books/book chapters provide the theoretical foundations that journal articles often lack.
3. **Citation coverage:** The must_read tier correctly captures high-citation foundational works alongside low-citation but topically essential recent papers.

**Systematic gaps:**
1. **Non-English scholarship is almost entirely absent.** Arabic-language Islamic ethics journals, Hindi-language dharmic philosophy, Chinese-language Confucian ethics — these exist and are not represented. This reinforces the very WEIRD bias the paper critiques.
2. **Grey literature from religious institutions** is thin — only the Vatican Rome Call. Missing: Muslim Council of Britain AI statement, Hindu American Foundation tech ethics position, Rabbinical Council of America AI guidelines.
3. **Expert 14 domain** is under-tagged (only 3 papers) — the bibliometric/systematic review methodology should be a stronger presence.

---

## Points of Agreement (Consensus)

1. **The collection is comprehensive for an English-language literature review.** 125 papers across 12 thematic domains with good priority distribution (51 must_read, 56 important, 18 supplementary).

2. **The cultural values and AI bias folders (03, 09) are the strongest.** These benefit from a mature, rapidly publishing research community.

3. **The Dharmic, Shinto, and Jewish AI ethics literatures are genuinely sparse** — not a curation failure but a reflection of the field's state. This sparsity should be presented as a finding, not an omission.

4. **The psychometric critique literature (folder 08) is the paper's methodological anchor.** The 2025 papers on construct validity in LLM benchmarks provide the strongest argument for why religious values benchmarks need careful design.

5. **Foundational works predating 2015 are essential and correctly included**, even though they predate the LLM era (Henrich 2010, Schwartz 2012, Kamali 2008, Twiss & Grelle 1998, Keown 2005, Dorff 2003).

## Points of Disagreement

1. **Folder granularity:** Expert 12 (Bryson) suggests the 12-folder structure is too fine-grained for one paper. Expert 1 (Sachedina) disagrees — the tradition-specific folders are necessary to properly represent each tradition's distinct contribution, even if the paper's lit review groups them.

2. **Non-English literature:** Expert 14 (Awosanya) flags the absence of non-English scholarship as a systematic bias. Expert 7 (Liang) counters that the paper's primary audience reads English and the benchmarks are English-medium, so English-language scholarship is appropriate. **Resolution:** Include a methodological limitation noting the English-language bias, and cite 3-5 non-English works where English-language reviews of them exist.

## Recommendations

### Immediate (5-8 additional papers)
1. Add 1-2 Indonesian Islamic AI governance papers (Expert 1)
2. Add 1 Protestant/evangelical theology of technology paper (Expert 2)
3. Add 1 Korean Confucian AI ethics paper (Expert 4)
4. Add 1 IRT-for-NLP paper (Expert 13)
5. Add 1 intersectional religious bias paper (Expert 11)

### Structural
6. Group the 12 folders into 4-5 lit review sections in the paper itself (Expert 12)
7. Present tradition-specific literature scarcity as a finding (Expert 3, consensus)
8. Note English-language limitation explicitly in methodology (Expert 14)

### For PDF Acquisition
9. Expect lower acquisition rates for theology/philosophy journals (folders 05-07, 11) — accept ~40-50% vs ~80% for CS folders
10. Books and book chapters (26 entries) will largely require manual acquisition or institutional access

---

## Minority Report

**Expert 3 (Bilimoria)** notes that the collection, while carefully curated, still reflects a fundamentally Western academic publishing infrastructure applied to non-Western philosophical traditions. Dharmic, African, and Indigenous knowledge systems were developed through oral, communal, and practice-based transmission — not peer-reviewed journals. The absence of these traditions from the benchmark pipeline and from the background literature is not merely a "gap to fill" but evidence of structural epistemic injustice in how AI evaluation research is conducted. The paper should name this, not just note it.
