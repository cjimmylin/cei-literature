# Expert 4: Citation Completeness Audit

**Auditor:** Citation Completeness Auditor
**Date:** 2026-04-12
**Scope:** All 9 paper files (00-abstract.md through 08-supp-figures.md) + religious-values-benchmarks.bib (83 entries)

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total `\cite{}` calls in paper | 51 |
| Unique citation keys used | 31 |
| Bib entries | 83 |
| Keys cited but missing from bib | 4 |
| Bib entries never cited | 56 |
| Citations in supplementary files (05-08) | 0 |
| Malformed `\cite{}` calls | 0 |
| Multi-citation spacing inconsistencies | 0 |
| Bib entries missing required fields | 3 |

---

## Section A: Missing Bib Entries (CRITICAL)

Four citation keys used in the paper do not resolve to any `@type{Key,` entry in `religious-values-benchmarks.bib`.

### Finding 1
**Location:** 01-methods.md:216
**Severity:** CRITICAL
**Category:** Missing-Bib
**Issue:** `\cite{Cohen1988}` has no corresponding bib entry. This is a foundational statistics reference (likely Jacob Cohen's *Statistical Power Analysis for the Behavioral Sciences*).
**Recommendation:** Add a `@book{Cohen1988, ...}` entry to the bib file.
**Quote:** `We adopt conventional thresholds for interpretation (small: $d = 0.2$, $V = 0.1$; medium: $d = 0.5$, $V = 0.3$; large: $d = 0.8$, $V = 0.5$) while recognizing that these thresholds are guides rather than bright lines \cite{Cohen1988}.`

### Finding 2
**Location:** 02-results.md:124
**Severity:** CRITICAL
**Category:** Missing-Bib
**Issue:** `\cite{Kulkarni2022}` has no corresponding bib entry. Context suggests a benchmark or dataset reference.
**Recommendation:** Add a bib entry for this reference. Identify the exact paper (likely a Hindu/Dharmic NLP or ethics paper given surrounding context).
**Quote:** `\cite{Kulkarni2022}` (referenced in results section on tradition-specific benchmarks)

### Finding 3
**Location:** 01-methods.md:27
**Severity:** CRITICAL
**Category:** Missing-Bib
**Issue:** `\cite{Nida1964}` has no corresponding bib entry. This is likely Eugene Nida's *Toward a Science of Translating* (1964), a foundational work on translation theory.
**Recommendation:** Add a `@book{Nida1964, ...}` entry to the bib file.
**Quote:** `\cite{Nida1964}` (referenced in methods section, likely regarding liturgical language normalization)

### Finding 4
**Location:** 01-methods.md:91
**Severity:** CRITICAL
**Category:** Missing-Bib
**Issue:** `\cite{Zhang2024}` has no corresponding bib entry. Context indicates a paper on theological dialogue systems.
**Recommendation:** Add the appropriate bib entry. No near-match exists in the bib file.
**Quote:** `emerging work on theological dialogue systems \cite{Zhang2024} suggests its future relevance.`

---

## Section B: Uncited Bib Entries Classification

56 of 83 bib entries are never cited in the paper. Each is classified as:
- **(a) Likely needed for Sections 1-2** (Introduction/Related Work): entries about AI ethics, benchmarking methodology, religious studies, cultural alignment, or specific tradition-AI intersections that an Introduction or Related Work section would naturally cite
- **(b) Genuinely orphaned**: entries tangential to the paper's scope
- **(c) Uncertain**: could go either way

### Table: Uncited Bib Entries

| Key | Title | Classification |
|-----|-------|---------------|
| Abdelnasser2014 | Al-Bayan: An Arabic Question Answering System for the Holy Quran | (a) Likely needed -- Islamic NLP benchmark, relevant to tradition coverage discussion |
| Abraham2019 | The Talmudic Logic Project, Ongoing Since 2008 | (a) Likely needed -- Jewish computational reasoning, relevant to void tradition analysis |
| Adilazuarda2025 | Cultural Alignment in Large Language Models | (a) Likely needed -- cultural alignment in LLMs, directly relevant to paper scope |
| AlAzani2023 | Unsupervised Thematic Clustering of Hadith Texts using Apriori Algorithm | (c) Uncertain -- Islamic NLP but clustering rather than benchmarking |
| AlMusawi2022 | Islamic Virtue-Based Ethics for Artificial Intelligence | (a) Likely needed -- Islamic ethics framework for AI |
| Asghari2023 | Confucius, cyberpunk and Mr. Science: Comparing AI ethics between China and EU | (a) Likely needed -- Confucian/East Asian AI ethics perspective |
| Bai2022 | Training a Helpful and Harmless Assistant with RLHF | (a) Likely needed -- foundational alignment method, relevant to Introduction |
| Burnell2023 | Rethink Reporting of Evaluation Results in AI | (a) Likely needed -- benchmarking methodology critique |
| Buyl2024 | Measuring Spiritual Values and Bias of Large Language Models | (a) Likely needed -- directly about spiritual/religious values in LLMs |
| Chadha2023 | Decolonial AI Alignment: Openness, Visesa-Dharma, and Including Excluded Knowledges | (a) Likely needed -- decolonial alignment with Hindu philosophy |
| Chang2024 | A Survey on Evaluation of Large Language Models | (a) Likely needed -- LLM evaluation survey, relevant to Related Work |
| Christiano2017 | Deep Reinforcement Learning from Human Preferences | (a) Likely needed -- foundational RLHF paper, relevant to alignment background |
| Durmus2024 | Towards Measuring the Representation of Subjective Global Opinions in Language Models | (a) Likely needed -- cross-cultural opinion measurement in LLMs |
| Ezzeddine2024 | AI in Islamic Ethics: Towards Pluralist Ethical Benchmarking for AI | (a) Likely needed -- directly about Islamic ethical benchmarking |
| Green2014 | Introduction: The Third Wave of Comparative Religious Ethics | (a) Likely needed -- comparative religious ethics methodology |
| Gwagwa2025 | Ethics of AI in Africa: Interrogating Ubuntu and AI Governance | (a) Likely needed -- Ubuntu/African AI ethics |
| Habib2023 | Ethics of AI in Maqasid Al-Shariah's Perspective | (a) Likely needed -- Islamic ethics framework for AI |
| Hamid2025 | Religious Bias Landscape in Language and Text-to-Image Models | (a) Likely needed -- religious bias in LLMs |
| Hofstede2011 | Dimensionalizing Cultures: The Hofstede Model in Context | (a) Likely needed -- cultural dimensions theory, relevant to WEIRD discussion |
| Hongladarom2020 | The Ethics of AI and Robotics: An East Asian Perspective | (a) Likely needed -- East Asian AI ethics |
| Ji2024 | AI Alignment: A Comprehensive Survey | (a) Likely needed -- alignment survey for Introduction |
| Keown2005 | Buddhist Ethics: A Very Short Introduction | (a) Likely needed -- Buddhist ethics reference |
| Levy2024 | Let us make man in our image: A Jewish ethical perspective on creating conscious robots | (a) Likely needed -- Jewish AI ethics |
| Li2022 | Measures of Representation and Bias in Natural Language Processing | (a) Likely needed -- bias measurement in NLP |
| Li2025 | Measuring what Matters: Construct Validity in LLM Benchmarks | (a) Likely needed -- construct validity in benchmarks |
| Manyika2024 | Integrating Catholic Social Teaching with AI Ethics | (a) Likely needed -- Christian/Catholic AI ethics |
| Mhlambi2020 | From Rationality to Relationality: Ubuntu as an Ethical and Human Rights Framework for AI | (a) Likely needed -- Ubuntu AI ethics framework |
| Mishra2024 | Bhagavad Gita as Framework for Sattvic AI | (a) Likely needed -- Hindu AI ethics framework |
| MofenjouPeuriekeu2024 | Ubuntu Philosophy and Artificial Intelligence Ethics in Africa | (a) Likely needed -- Ubuntu AI ethics |
| Mohadi2024 | Maqasid Al-Shari'ah and the Ethics of Artificial Intelligence | (a) Likely needed -- Islamic ethics framework |
| Mohanty2024 | Indic approach to ethical AI in automated decision making | (a) Likely needed -- Indic/Hindu AI ethics |
| Muravyov2025 | Islamic Ethics and AI: An Evaluation using Trusteeship Ethics | (a) Likely needed -- Islamic AI ethics evaluation |
| Nadeem2021 | StereoSet: Measuring Stereotypical Bias in Pretrained Language Models | (a) Likely needed -- bias benchmark, relevant to bias-values conflation discussion |
| Naous2024 | Cultural Bias and Cultural Alignment of Large Language Models | (a) Likely needed -- cultural bias in LLMs |
| Ogwo2025 | Where are the missing values: Ubuntu values into African AI policy | (a) Likely needed -- Ubuntu values in AI |
| Ong2025 | Medical LLM Benchmarks Should Prioritize Construct Validity | (a) Likely needed -- construct validity argument for benchmarks |
| Ouyang2022 | Training language models to follow instructions with human feedback | (a) Likely needed -- foundational RLHF/InstructGPT paper |
| PewResearch2017 | The Changing Global Religious Landscape | (a) Likely needed -- global religion demographics, supports "80% of world's population" claim in abstract |
| Putri2025 | Is Lying Only Sinful in Islam? Exploring Religious Bias in Multilingual LLMs | (a) Likely needed -- religious bias in multilingual LLMs |
| Roberts2022 | AI for Topic Modelling in Hindu Philosophy: Mapping the Upanishads and Bhagavad Gita | (c) Uncertain -- Hindu NLP but topic modeling, not benchmarking |
| Rodriguez2021 | Evaluation Examples are not Equally Informative | (a) Likely needed -- benchmark methodology |
| RomeCall2020 | Rome Call for AI Ethics | (a) Likely needed -- prominent religious institution AI ethics statement |
| Rosenfeld2021 | Jewish Ethics Meets Machine Learning: An Introduction | (a) Likely needed -- Jewish AI ethics |
| Schlangen2021 | Targeting the Benchmark: On Methodology in Current NLU Research | (a) Likely needed -- benchmarking methodology critique |
| Schwartz2012 | An Overview of the Schwartz Theory of Basic Values | (a) Likely needed -- values theory, relevant to "values" construct definition |
| Schweiker2005 | Theological Ethics and Global Dynamics | (c) Uncertain -- theological ethics but more philosophical than AI-focused |
| SinghKaur2024 | Sikh Ethics and Technology: Sewa, Hukam, and AI Governance | (a) Likely needed -- Sikh AI ethics |
| Srivastava2023 | Beyond the Imitation Game (BIG-bench) | (a) Likely needed -- major LLM benchmark suite |
| Srivastava2024 | PATCH: Psychometrics-Assisted Benchmarking of LLMs | (a) Likely needed -- psychometric benchmarking methodology |
| Steinberg2025 | Is this Judaism? The Question of the Consistency of Israeli AI Ethics | (a) Likely needed -- Jewish AI ethics |
| Sukiennik2025 | An Evaluation of Cultural Value Alignment in Large Language Models | (a) Likely needed -- cultural value alignment in LLMs |
| Twiss1998 | Comparative Religious Ethics: A Narrative Approach | (a) Likely needed -- comparative religious ethics methodology |
| Varghese2023 | Lexical And Semantic Analysis Of Sacred Texts Using ML and NLP | (c) Uncertain -- sacred text NLP but lexical analysis, not benchmarking |
| Verma2023 | Lexical Analysis of Religious Texts using Text Mining and ML Tools | (c) Uncertain -- religious text analysis but not benchmarking |
| Wong2019 | Dao, Harmony and Personhood: Towards a Confucian Ethics of Technology | (a) Likely needed -- Confucian technology ethics |
| ZhaoLiu2015 | Chinese Buddhist Philosophy and Computational Ethics | (a) Likely needed -- Buddhist computational ethics |

**Classification summary:**
- **(a) Likely needed for Sections 1-2:** 51 entries
- **(b) Genuinely orphaned:** 0 entries
- **(c) Uncertain:** 5 entries (AlAzani2023, Roberts2022, Schweiker2005, Varghese2023, Verma2023)

**Key observation:** The paper currently has no Introduction or Related Work section (Sections 1-2 are missing from the PAPER-V2 files). The 83-entry bibliography was clearly compiled to support a full paper including Introduction and Literature Review sections. The 56 uncited entries are overwhelmingly relevant to the paper's topic and would naturally appear in those missing sections. This is not a case of orphaned references -- it is a case of **missing paper sections that need to cite these references**.

---

## Section C: Citation Syntax Check

### Finding 5
**Location:** All files
**Severity:** PASS (no issues)
**Category:** Syntax
**Issue:** No malformed `\cite{}` calls found. No empty keys, no unclosed braces.

### Finding 6
**Location:** All multi-citation calls
**Severity:** PASS (consistent)
**Category:** Syntax
**Issue:** All 5 multi-citation calls use consistent formatting with a space after the comma: `\cite{Key1, Key2}`. No inconsistencies detected.

### Finding 7
**Location:** All files
**Severity:** MINOR
**Category:** Syntax
**Issue:** No near-miss citation keys detected. All 4 missing keys (Cohen1988, Kulkarni2022, Nida1964, Zhang2024) have no close matches in the bib file, confirming they are genuinely absent entries rather than misspellings.

### Finding 8
**Location:** 00-abstract.md (entire file)
**Severity:** MINOR
**Category:** Syntax
**Issue:** The abstract (Section 0) contains zero `\cite{}` calls. This is standard for many journals but some venues require citation-free abstracts. Verify against target venue requirements.
**Recommendation:** No action needed unless target venue (noted as Big Data & Society in project memory) requires citations in the abstract.

---

## Section D: Bib Entry Completeness

### Finding 9
**Location:** Bib entry `MofenjouPeuriekeu2024`
**Severity:** MAJOR
**Category:** Bib-Completeness
**Issue:** Entry is `@misc` type with no `journal`, `booktitle`, `doi`, or `url` field. Only has `author`, `title`, and `year`.
**Recommendation:** Add at least a `url` or `doi` field. If this is an unpublished manuscript, add `note = {Unpublished manuscript}` or `howpublished`.
**Quote:**
```bibtex
@misc{MofenjouPeuriekeu2024,
  author = {Mofenjou P\'{e}uri\'{e}keu, Brice},
  title = {{Ubuntu Philosophy and Artificial Intelligence Ethics in Africa}},
  year = {2024},
}
```

### Finding 10
**Location:** Bib entry `TuckYang2012`
**Severity:** MAJOR
**Category:** Bib-Completeness
**Issue:** Entry is `@misc` type with no `journal`, `booktitle`, `doi`, or `url` field. This is a well-known article published in *Decolonization: Indigeneity, Education & Society*.
**Recommendation:** Change to `@article` and add `journal = {Decolonization: Indigeneity, Education \& Society}`, `volume = {1}`, `number = {1}`, `pages = {1--40}`.
**Quote:**
```bibtex
@misc{TuckYang2012,
  author = {Tuck, Eve and Yang, K. Wayne},
  title = {{Decolonization is Not a Metaphor}},
  year = {2012},
}
```

### Finding 11
**Location:** Bib entry `ZhaoLiu2015`
**Severity:** MINOR
**Category:** Bib-Completeness
**Issue:** Entry is `@misc` type with no `journal`, `booktitle`, `doi`, or `url` field. Only has `author`, `title`, and `year`. This entry is also uncited.
**Recommendation:** Add venue information or remove if genuinely orphaned. Since this is uncited, lower priority.
**Quote:**
```bibtex
@misc{ZhaoLiu2015,
  author = {Zhao, Jieyu and Liu, Chang},
  title = {{Chinese Buddhist Philosophy and Computational Ethics}},
  year = {2015},
}
```

### Finding 12
**Location:** Bib entry `Mhlambi2020`
**Severity:** MINOR
**Category:** Bib-Completeness
**Issue:** The `journal` field contains a full institutional affiliation rather than a journal name: `Carr Center for Human Rights Policy, Harvard Kennedy School`. This is likely a working paper or discussion paper, not a journal article.
**Recommendation:** Change to `@techreport` or `@misc` with `institution` or `howpublished` field instead of `journal`.
**Quote:**
```bibtex
journal = {Carr Center for Human Rights Policy, Harvard Kennedy School},
```

### Finding 13
**Location:** Bib entry `Rosenfeld2021`
**Severity:** MINOR
**Category:** Bib-Completeness
**Issue:** Entry is `@article` type but has no `journal` field -- only a `url`. The entry type should be `@misc` or `@article` with `journal = {arXiv}` added.
**Recommendation:** Add `journal = {arXiv}` to match the convention used by other arXiv entries in this bib file (e.g., Bai2022, Buyl2024).
**Quote:**
```bibtex
@article{Rosenfeld2021,
  author = {Rosenfeld, Azriel},
  title = {{Jewish Ethics Meets Machine Learning: An Introduction}},
  year = {2021},
  url = {https://arxiv.org/abs/2302.08893},
}
```

---

## Section E: Supplementary Citation Check

### Finding 14
**Location:** 05-supp-methods.md, 06-supp-results.md, 07-supp-tables.md, 08-supp-figures.md
**Severity:** PASS
**Category:** Supp-Citation
**Issue:** All four supplementary files contain zero `\cite{}` calls. This is confirmed clean.

---

## Summary Table 1: Missing Bib Entries

| Key | File | Line | Context |
|-----|------|------|---------|
| Cohen1988 | 01-methods.md | 216 | Effect size interpretation thresholds |
| Kulkarni2022 | 02-results.md | 124 | Tradition-specific benchmark reference |
| Nida1964 | 01-methods.md | 27 | Translation theory (liturgical language normalization) |
| Zhang2024 | 01-methods.md | 91 | Theological dialogue systems |

## Summary Table 2: Uncited Bib Entries

| Key | Title | Classification |
|-----|-------|---------------|
| Abdelnasser2014 | Al-Bayan: An Arabic Question Answering System for the Holy Quran | (a) |
| Abraham2019 | The Talmudic Logic Project, Ongoing Since 2008 | (a) |
| Adilazuarda2025 | Cultural Alignment in Large Language Models | (a) |
| AlAzani2023 | Unsupervised Thematic Clustering of Hadith Texts | (c) |
| AlMusawi2022 | Islamic Virtue-Based Ethics for Artificial Intelligence | (a) |
| Asghari2023 | Confucius, cyberpunk and Mr. Science | (a) |
| Bai2022 | Training a Helpful and Harmless Assistant with RLHF | (a) |
| Burnell2023 | Rethink Reporting of Evaluation Results in AI | (a) |
| Buyl2024 | Measuring Spiritual Values and Bias of Large Language Models | (a) |
| Chadha2023 | Decolonial AI Alignment: Openness, Visesa-Dharma | (a) |
| Chang2024 | A Survey on Evaluation of Large Language Models | (a) |
| Christiano2017 | Deep Reinforcement Learning from Human Preferences | (a) |
| Durmus2024 | Towards Measuring Subjective Global Opinions in LMs | (a) |
| Ezzeddine2024 | AI in Islamic Ethics: Towards Pluralist Ethical Benchmarking | (a) |
| Green2014 | Introduction: The Third Wave of Comparative Religious Ethics | (a) |
| Gwagwa2025 | Ethics of AI in Africa: Interrogating Ubuntu and AI Governance | (a) |
| Habib2023 | Ethics of AI in Maqasid Al-Shariah's Perspective | (a) |
| Hamid2025 | Religious Bias Landscape in Language and Text-to-Image Models | (a) |
| Hofstede2011 | Dimensionalizing Cultures: The Hofstede Model in Context | (a) |
| Hongladarom2020 | The Ethics of AI and Robotics: An East Asian Perspective | (a) |
| Ji2024 | AI Alignment: A Comprehensive Survey | (a) |
| Keown2005 | Buddhist Ethics: A Very Short Introduction | (a) |
| Levy2024 | Let us make man in our image: A Jewish ethical perspective | (a) |
| Li2022 | Measures of Representation and Bias in NLP | (a) |
| Li2025 | Measuring what Matters: Construct Validity in LLM Benchmarks | (a) |
| Manyika2024 | Integrating Catholic Social Teaching with AI Ethics | (a) |
| Mhlambi2020 | From Rationality to Relationality: Ubuntu as AI Framework | (a) |
| Mishra2024 | Bhagavad Gita as Framework for Sattvic AI | (a) |
| MofenjouPeuriekeu2024 | Ubuntu Philosophy and AI Ethics in Africa | (a) |
| Mohadi2024 | Maqasid Al-Shari'ah and the Ethics of AI | (a) |
| Mohanty2024 | Indic approach to ethical AI in automated decision making | (a) |
| Muravyov2025 | Islamic Ethics and AI: An Evaluation using Trusteeship Ethics | (a) |
| Nadeem2021 | StereoSet: Measuring Stereotypical Bias in PLMs | (a) |
| Naous2024 | Cultural Bias and Cultural Alignment of LLMs | (a) |
| Ogwo2025 | Where are the missing values: Ubuntu values into African AI policy | (a) |
| Ong2025 | Medical LLM Benchmarks Should Prioritize Construct Validity | (a) |
| Ouyang2022 | Training language models to follow instructions with human feedback | (a) |
| PewResearch2017 | The Changing Global Religious Landscape | (a) |
| Putri2025 | Is Lying Only Sinful in Islam? Religious Bias in Multilingual LLMs | (a) |
| Roberts2022 | AI for Topic Modelling in Hindu Philosophy | (c) |
| Rodriguez2021 | Evaluation Examples are not Equally Informative | (a) |
| RomeCall2020 | Rome Call for AI Ethics | (a) |
| Rosenfeld2021 | Jewish Ethics Meets Machine Learning: An Introduction | (a) |
| Schlangen2021 | Targeting the Benchmark: On Methodology in Current NLU Research | (a) |
| Schwartz2012 | An Overview of the Schwartz Theory of Basic Values | (a) |
| Schweiker2005 | Theological Ethics and Global Dynamics | (c) |
| SinghKaur2024 | Sikh Ethics and Technology: Sewa, Hukam, and AI Governance | (a) |
| Srivastava2023 | Beyond the Imitation Game (BIG-bench) | (a) |
| Srivastava2024 | PATCH: Psychometrics-Assisted Benchmarking of LLMs | (a) |
| Steinberg2025 | Is this Judaism? The Consistency of Israeli AI Ethics | (a) |
| Sukiennik2025 | An Evaluation of Cultural Value Alignment in LLMs | (a) |
| Twiss1998 | Comparative Religious Ethics: A Narrative Approach | (a) |
| Varghese2023 | Lexical And Semantic Analysis Of Sacred Texts Using ML and NLP | (c) |
| Verma2023 | Lexical Analysis of Religious Texts using Text Mining and ML | (c) |
| Wong2019 | Dao, Harmony and Personhood: Confucian Ethics of Technology | (a) |
| ZhaoLiu2015 | Chinese Buddhist Philosophy and Computational Ethics | (a) |

**Classification: (a) = 51, (b) = 0, (c) = 5**

## Summary Table 3: Syntax/Completeness Issues

| Key or Location | Issue |
|-----------------|-------|
| Cohen1988 | CRITICAL: Cited at 01-methods.md:216, no bib entry |
| Kulkarni2022 | CRITICAL: Cited at 02-results.md:124, no bib entry |
| Nida1964 | CRITICAL: Cited at 01-methods.md:27, no bib entry |
| Zhang2024 | CRITICAL: Cited at 01-methods.md:91, no bib entry |
| MofenjouPeuriekeu2024 | MAJOR: No journal/booktitle/doi/url (uncited) |
| TuckYang2012 | MAJOR: No journal/booktitle/doi/url (cited in paper) |
| ZhaoLiu2015 | MINOR: No journal/booktitle/doi/url (uncited) |
| Mhlambi2020 | MINOR: journal field contains institution, not journal name |
| Rosenfeld2021 | MINOR: @article with no journal field, only url |

---

## Overall Assessment

**CRITICAL issues (4):** Four citation keys resolve to nothing in the bibliography. These will produce "[?]" markers in any LaTeX compilation. All four must be added to the bib file before submission.

**MAJOR structural observation:** 56 of 83 bib entries (67%) are never cited. However, this is almost entirely explained by the fact that the paper's PAPER-V2 directory contains no Introduction or Related Work sections (Sections 1-2). The 83-entry bibliography was compiled for a full paper. Of the 56 uncited entries, 51 are classified as **(a) likely needed** for Introduction/Related Work sections covering AI alignment background, benchmarking methodology, tradition-specific AI ethics, and cultural alignment. Once Sections 1-2 are written, the uncited count should drop dramatically.

**Bib quality:** Generally good. Three entries lack venue information (MofenjouPeuriekeu2024, TuckYang2012, ZhaoLiu2015), and two have minor type/field mismatches (Mhlambi2020, Rosenfeld2021). TuckYang2012 is the most important to fix since it is actively cited and is a well-known published article.

**Citation syntax:** Clean. All `\cite{}` calls are well-formed, multi-citation spacing is consistent, and no misspelled keys were detected.

**Supplementary files:** Confirmed clean -- zero `\cite{}` calls in any of the four supplementary files (05-08).
