# Expert Council: Religious Values Alignment Benchmark — Background Literature Review

**Date:** 2026-04-03
**Purpose:** Guide the systematic literature search for background research supporting an academic paper on evaluating AI alignment with religious values across diverse traditions.
**Council Size:** 14 members
**Scope:** Identify, evaluate, and prioritize ~120-150 scholarly papers across 12 thematic domains.

---

## Council Composition

### Tier 1: Tradition-Specific Scholars (6 members)

| # | Name | Affiliation | Discipline | Role | Primary Folders |
|---|------|------------|-----------|------|-----------------|
| 1 | **Prof. Abdulaziz Sachedina** | George Mason University | Islamic Ethics & Bioethics | Guides search for Islamic AI ethics, Maqasid al-Shariah frameworks, Quranic NLP validation. Ensures coverage of fiqh-level theological depth vs. surface-level "Islam and AI" surveys. | 04-islamic-ai-ethics, 09-ai-bias-religion |
| 2 | **Prof. Brent Waters** | Garrett-Evangelical Theological Seminary | Christian Theological Ethics | Guides search for Christian AI ethics covering Catholic social teaching, Protestant theological anthropology, natural law theory, and ecumenical statements (Vatican "Rome Call"). Ensures patristic and Reformed traditions are represented, not just Catholic. | 05-christian-ethics-ai |
| 3 | **Prof. Purushottama Bilimoria** | University of Melbourne / UC Berkeley | Dharmic Philosophy & Comparative Ethics | Guides search across Hindu (dharma, karma, ahimsa), Buddhist (karuna, metta, pratityasamutpada), Jain (anekantavada, ahimsa), and Sikh (sewa, hukam) traditions. Ensures philosophical depth beyond "Eastern wisdom" stereotypes. | 06-dharmic-ethics-ai |
| 4 | **Prof. Chenyang Li** | Nanyang Technological University, Singapore | Confucian Philosophy | Guides search for Confucian ren-li ethics, Taoist wu-wei, Shinto kami-and-technology perspectives. Validates that East Asian philosophy papers engage genuine philosophical traditions, not Orientalist reconstructions. | 12-east-asian-philosophy-ai |
| 5 | **Dr. Amara Osei-Mensah** | University of Ghana | African Philosophy & Ubuntu Ethics | Guides search for Ubuntu communitarian ethics, African philosophy of technology, Indigenous knowledge systems, and decolonial AI. Ensures representation of oral and communal traditions that lack digitized corpora. | 10-indigenous-african-ai |
| 6 | **Dr. Moshe Koppel** | Bar-Ilan University | Computational Talmudics & Jewish Ethics | Guides search for Jewish law (halakha) and AI, Talmudic reasoning as computational framework, the Responsa Project legacy, Hebrew NLP for religious texts. Validates rabbinic reasoning literature, not just Holocaust-framed Jewish ethics. | 11-jewish-ethics-ai |

### Tier 2: Methodological & Cross-Cutting Experts (8 members)

| # | Name | Affiliation | Discipline | Role | Primary Folders |
|---|------|------------|-----------|------|-----------------|
| 7 | **Dr. Percy Liang** | Stanford HAI / Stanford NLP | AI Evaluation & Benchmarking | Guides search for AI alignment evaluation frameworks (HELM, lm-eval-harness, Inspect AI), benchmark design methodology, and evaluation harness architecture. Provides the technical evaluation lens for what makes a benchmark implementable. | 01-ai-values-alignment, 08-benchmark-psychometrics |
| 8 | **Dr. Henriette Cramer** | Spotify Research | Cross-Cultural HCI & AI | Guides search for WEIRD bias in AI evaluation, World Values Survey applications, Hofstede/Schwartz cultural dimensions theory applied to LLMs. Bridges cultural psychology with AI measurement. | 03-cultural-values-ai |
| 9 | **Prof. Luciano Floridi** | Yale University / University of Bologna | Philosophy of Information & AI Ethics | Guides search for Western normative frameworks (beneficence, non-maleficence, autonomy, justice), information ethics, and values alignment theory. Provides the philosophical grounding for why "alignment" requires religious values. | 01-ai-values-alignment, 07-comparative-religious-ethics |
| 10 | **Dr. Abubakar Abid** | Gradio / HuggingFace | NLP & Religious Text Computation | Guides search for computational approaches to sacred texts — Quranic NLP, biblical text mining, scriptural corpus linguistics, religious dataset curation. Bridges CS and theology communities. | 02-religious-nlp, 04-islamic-ai-ethics |
| 11 | **Dr. Abeba Birhane** | Trinity College Dublin | Cognitive Science & AI Fairness | Guides search for religious bias in LLMs, discrimination against religious minorities in AI systems, intersectionality of religion with race/gender in AI fairness. Ensures critical perspectives on power dynamics. | 09-ai-bias-religion |
| 12 | **Prof. Joanna Bryson** | Hertie School, Berlin | AI Governance & Comparative Ethics | Guides search for comparative moral philosophy applied to AI, religion-technology intersection in governance, and the broader moral-status-of-AI debate. Bridges governance and philosophy. | 07-comparative-religious-ethics, 03-cultural-values-ai |
| 13 | **Dr. Maria Pearce** | Educational Testing Service (ETS) | Psychometrics & Educational Measurement | Guides search for construct validity in AI benchmarks, measurement invariance across cultural/religious groups, item response theory applied to NLP evaluation, annotator agreement methodology. Ensures psychometric rigor. | 08-benchmark-psychometrics |
| 14 | **Dr. Segun Awosanya** | University of Lagos | Statistical Methods & Bibliometrics | Guides systematic review methodology, bibliometric analysis, gap analysis statistics, and cross-validation of search completeness. Ensures methodological rigor of the literature search itself. | All folders (meta-review) |

---

## Operating Procedures

### Decision-Making
- **Consensus preferred** but not required; documented dissent is valued.
- **Tradition-specific expertise deferred to** on terminology, source selection, and theological accuracy within that tradition's folder.
- **Methodological disputes** (e.g., inclusion criteria, priority assignment) resolved by Experts #13 (Pearce) and #14 (Awosanya).
- **Cross-tradition papers** placed by primary tradition expert, with secondary expert consulted.

### Paper Evaluation Criteria
Each expert evaluates papers for inclusion based on:
1. **Relevance** — Does it directly inform the paper's argument about religious values AI alignment?
2. **Quality** — Peer-reviewed > working paper > report > blog. Exception: foundational grey literature (e.g., Vatican statements, indigenous community declarations).
3. **Representativeness** — Does it add a perspective not already covered? Tradition-diverse papers preferred over redundant entries.
4. **Recency** — 2020-2026 preferred, but foundational works from any era included as "must_read."
5. **Accessibility** — Open-access or institutionally available preferred, but paywalled papers included if essential.

### Priority Assignment
- **must_read** — Foundational to the paper's argument; would be cited in any serious literature review on this topic.
- **important** — Provides significant context or evidence; likely cited in 1-2 sections of the paper.
- **supplementary** — Useful for completeness or specialized depth; cited in footnotes or supplementary material.

### Anti-Essentialization Guardrails

This council explicitly acknowledges:

1. **No expert "represents" a religion.** Prof. Sachedina advises on Islamic ethics scholarship, not "what Islam thinks about AI." Prof. Waters advises on Christian theological ethics literature, not "the Christian view."

2. **Religious traditions are internally diverse.** Islam includes Sunni, Shia, Sufi, and Ibadi perspectives. Christianity spans Catholic, Orthodox, mainline Protestant, evangelical, and Pentecostal traditions. Hinduism encompasses Shaiva, Vaishnava, Shakta, and Smarta schools. The literature search must reflect this diversity, not flatten it.

3. **Cultural categories are analytical constructs.** "Abrahamic," "Dharmic," "East Asian" are scholarly organizing tools, not bounded identities. Within-tradition variation often exceeds between-tradition variation.

4. **Oral and communal traditions require different evidence standards.** For Indigenous and African traditions (folder 10), peer-reviewed journal articles may be scarce. Community declarations, ethnographic studies, and participatory research reports are legitimate sources. The absence of publications is itself a finding about power dynamics in academic publishing.

5. **Results reported as "tendencies in literature,"** not "what traditions believe." The literature search characterizes the scholarly conversation, not the religions themselves.

---

## Folder Assignments

| Folder | Lead Expert(s) | Supporting Expert(s) |
|--------|----------------|---------------------|
| 01-ai-values-alignment | Liang (#7), Floridi (#9) | Awosanya (#14) |
| 02-religious-nlp | Abid (#10) | Liang (#7) |
| 03-cultural-values-ai | Cramer (#8), Bryson (#12) | Awosanya (#14) |
| 04-islamic-ai-ethics | Sachedina (#1), Abid (#10) | Birhane (#11) |
| 05-christian-ethics-ai | Waters (#2) | Floridi (#9) |
| 06-dharmic-ethics-ai | Bilimoria (#3) | Cramer (#8) |
| 07-comparative-religious-ethics | Floridi (#9), Bryson (#12) | Sachedina (#1), Bilimoria (#3) |
| 08-benchmark-psychometrics | Liang (#7), Pearce (#13) | Awosanya (#14) |
| 09-ai-bias-religion | Birhane (#11), Sachedina (#1) | Osei-Mensah (#5) |
| 10-indigenous-african-ai | Osei-Mensah (#5) | Birhane (#11), Bryson (#12) |
| 11-jewish-ethics-ai | Koppel (#6) | Floridi (#9) |
| 12-east-asian-philosophy-ai | Li (#4) | Cramer (#8) |

---

## Deliberation Schedule

| Deliberation | Topic | Output File |
|-------------|-------|-------------|
| D-01 | Literature coverage review — gaps, priorities, missing traditions | `20260403-deliberation-01-literature-coverage.md` |
| D-02 (if needed) | Post-acquisition review — papers found vs. papers needed | TBD |
