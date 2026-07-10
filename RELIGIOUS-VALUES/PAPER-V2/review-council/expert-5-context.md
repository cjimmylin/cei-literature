# Expert 5: Citation Context Evaluation

**Evaluator:** Citation Context Evaluator
**Date:** 2026-04-12
**Scope:** Sections 3--6 (01-methods.md, 02-results.md, 03-discussion.md, 04-conclusion.md)
**Total unique citation keys found:** 31
**Missing from bib:** 4 (Cohen1988, Kulkarni2022, Nida1964, Zhang2024)

---

## A. Per-Citation Relevance Findings

### Finding 1
**Location:** 01-methods.md:27
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Nida1964}` is MISSING-BIB. Used to support claim that "translation necessarily transforms theological concepts." Based on the key name, this is likely Eugene Nida's *Toward a Science of Translating* (1964), a foundational translation theory work. If so, the citation is STRONG but it must be added to the bib file.
**Recommendation:** Add Nida1964 to the bib file. Verify exact title and publisher (Brill).
**Quote:** "benchmarks that process scripture in its original liturgical language...receive a +1 modifier, recognizing that translation necessarily transforms theological concepts \cite{Nida1964}"

### Finding 2
**Location:** 01-methods.md:81
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Alharbi2024}` used to describe IslamicMMLU as R2 calibration anchor. Bib entry title is "IslamicMMLU: A Benchmark for Evaluating LLMs on Islamic Knowledge." STRONG match -- the citation directly names the benchmark being described.
**Recommendation:** None needed.
**Quote:** "IslamicMMLU \cite{Alharbi2024} (R2 = 4) engages fiqh-level jurisprudential reasoning across four madhabs"

### Finding 3
**Location:** 01-methods.md:91
**Severity:** MAJOR
**Category:** Relevance
**Issue:** `\cite{Zhang2024}` is MISSING-BIB. Used to support claim about "emerging work on theological dialogue systems." The key is generic; without a bib entry it is impossible to verify relevance. This is a forward-looking claim about a format code (DLG) that doesn't even exist yet, making the citation's absence more concerning.
**Recommendation:** Either add Zhang2024 to the bib with full bibliographic data, or remove the citation and rephrase as an unsupported observation about future directions.
**Quote:** "emerging work on theological dialogue systems \cite{Zhang2024} suggests its future relevance"

### Finding 4
**Location:** 01-methods.md:107
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Bowman2021}` supports claim that "benchmarks without accessible data cannot be verified, replicated, or extended." Bib title: "What Will it Take to Fix Benchmarking in Natural Language Understanding?" STRONG -- directly about benchmarking methodology and reproducibility concerns.
**Recommendation:** None needed.
**Quote:** "PE receives the second-highest weight (35%) because benchmarks without accessible data cannot be verified, replicated, or extended by independent researchers \cite{Bowman2021}"

### Finding 5
**Location:** 01-methods.md:107
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Liang2023}` supports claim about avoiding over-rewarding incumbency in citations. Bib title: "Holistic Evaluation of Language Models." ADEQUATE -- HELM is about holistic LLM evaluation and discusses citation/benchmark dynamics, though the specific claim about citation bias toward older benchmarks is tangential to HELM's main contribution.
**Recommendation:** None needed, but a more targeted citation on citation age bias in benchmarking would strengthen this.
**Quote:** "CI receives the lowest weight (25%) to avoid over-rewarding incumbency...high citation counts disproportionately favor older benchmarks \cite{Liang2023}"

### Finding 6
**Location:** 01-methods.md:109
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Gehrmann2022}` supports claim about data accessibility being the field's primary practical bottleneck. Bib title: "Repairing the Cracked Foundation: A Survey of Obstacles in Evaluation Practices for Generated Text." STRONG -- directly about evaluation obstacles including data access.
**Recommendation:** None needed.
**Quote:** "data accessibility---not benchmark quality---is the field's primary practical bottleneck \cite{Gehrmann2022}"

### Finding 7
**Location:** 01-methods.md:113
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Mohamed2020, Carroll2020}` used together to support claim about structural epistemic injustice through publication infrastructure. Mohamed2020 = "Decolonial AI" and Carroll2020 = "CARE Principles for Indigenous Data Governance." Both STRONG for the claim about traditions excluded by infrastructure.
**Recommendation:** None needed.
**Quote:** "no benchmark from either tradition passed both gates---a finding we discuss in Section 4.3 as evidence of structural epistemic injustice operating through publication infrastructure \cite{Mohamed2020, Carroll2020}"

### Finding 8
**Location:** 01-methods.md:133
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Leavens2024}` supports claim that sacred texts cannot be treated as "just data." Bib title: "Modeling the Sacred: Considerations when Using Religious Texts in NLP." STRONG -- directly about the methodological challenges of applying NLP to religious texts.
**Recommendation:** None needed.
**Quote:** "sacred texts cannot be treated as 'just data' amenable to standard NLP annotation procedures \cite{Leavens2024}"

### Finding 9
**Location:** 01-methods.md:216
**Severity:** MAJOR
**Category:** Relevance
**Issue:** `\cite{Cohen1988}` is MISSING-BIB. Used to justify effect size threshold conventions (d=0.2, 0.5, 0.8). This is almost certainly Jacob Cohen's *Statistical Power Analysis for the Behavioral Sciences* (1988), one of the most cited statistics texts. The absence from the bib is a clear oversight since this is a foundational methods reference.
**Recommendation:** Add Cohen1988 to the bib file immediately. This is a standard reference that reviewers will expect to find.
**Quote:** "We adopt conventional thresholds for interpretation...while recognizing that these thresholds are guides rather than bright lines \cite{Cohen1988}"

### Finding 10
**Location:** 01-methods.md:238
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Carroll2020}` used again to support claim about hard gate as structural exclusion for traditions exercising data sovereignty. STRONG -- CARE Principles directly address Indigenous data governance and sovereignty.
**Recommendation:** None needed.
**Quote:** "the hard gate requiring publicly available evaluation data...functions simultaneously as a structural exclusion mechanism for traditions governed by collective data sovereignty norms \cite{Carroll2020}"

### Finding 11
**Location:** 02-results.md:17
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Mohamed2020, Bilimoria2013}` used to support claim about traditions with oral/communal knowledge systems. Mohamed2020 = "Decolonial AI" (STRONG for structural exclusion). Bilimoria2013 = "Indian Ethics: Classical Traditions and Contemporary Challenges" (ADEQUATE -- relevant to Dharmic traditions' knowledge systems but focuses on Indian ethics broadly, not specifically on oral/communal transmission).
**Recommendation:** None needed.
**Quote:** "traditions whose knowledge systems were developed through oral, communal, and practice-based transmission \cite{Mohamed2020, Bilimoria2013}"

### Finding 12
**Location:** 02-results.md:21
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Gupta2025}` supports claim about success of psychometric approaches in secular values measurement. Bib title: "Large Language Model Psychometrics: A Systematic Review." STRONG -- directly about applying psychometric methods to LLMs.
**Recommendation:** None needed.
**Quote:** "despite the success of such approaches in secular values measurement \cite{Gupta2025}"

### Finding 13
**Location:** 02-results.md:25
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Liang2023}` used again to support claim about religious values benchmarking being a nascent field with limited methodological consolidation. ADEQUATE -- HELM provides context for benchmarking maturity, though the connection to religious benchmarking specifically is indirect.
**Recommendation:** None needed.
**Quote:** "a nascent field---one with substantial growth potential but limited methodological consolidation \cite{Liang2023}"

### Finding 14
**Location:** 02-results.md:79
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Alharbi2024}` used to describe ELQV as highest-ranking benchmark. The bib entry is for IslamicMMLU, NOT ELQV. This appears to be a **MISATTRIBUTION** -- ELQV and IslamicMMLU are different benchmarks.
**Recommendation:** CRITICAL FIX NEEDED. Verify the correct citation key for ELQV and add it to the bib. The current citation attributes ELQV's description to the IslamicMMLU paper.
**Quote:** "ELQV \cite{Alharbi2024} achieves the highest composite score in Tier 1 (52.0)"

### Finding 15
**Location:** 02-results.md:112
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Malhas2023}` supports claim about Quranic QA shared task pipeline. Bib title: "HAQA and QUQA: Constructing Two Arabic QA Corpora for the Quran and Hadith." STRONG -- this IS the Quranic QA pipeline being described.
**Recommendation:** None needed.
**Quote:** "the Quranic QA shared task community \cite{Malhas2023} has sustained a pipeline since at least 2019"

### Finding 16
**Location:** 02-results.md:112
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Abdelali2023}` supports claim about Arabic NLP community investment. Bib title: "AceGPT: Localizing Large Language Models in Arabic." STRONG -- AceGPT is an example of Arabic LLM localization work.
**Recommendation:** None needed.
**Quote:** "Arabic NLP community's investment in culturally grounded language models \cite{Abdelali2023}"

### Finding 17
**Location:** 02-results.md:112
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Kamali2008}` supports description of Maqasid al-Shariah framework. Bib title: "Maqasid al-Shariah Made Simple." STRONG -- this is a standard reference for the framework being described.
**Recommendation:** None needed.
**Quote:** "The Maqasid al-Shariah framework \cite{Kamali2008}---the objectives of Islamic law"

### Finding 18
**Location:** 02-results.md:116
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Francis2015}` is cited to support claim about Vatican's Rome Call for AI Ethics. However, the bib entry is for "Laudato Si': On Care for Our Common Home" -- a papal encyclical on environmental care, NOT the Rome Call for AI Ethics (which is separately in the bib as RomeCall2020). This is a **MISATTRIBUTION**.
**Recommendation:** Replace `\cite{Francis2015}` with `\cite{RomeCall2020}`. Laudato Si' is about ecology, not AI ethics. The Rome Call for AI Ethics (2020, Pontifical Academy for Life) is the correct reference.
**Quote:** "the Vatican's Rome Call for AI Ethics \cite{Francis2015} and numerous denominational position papers"

### Finding 19
**Location:** 02-results.md:116
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Johnson2026}` supports claim about "doctrinal flattening." Bib title: "Detecting doctrinal flattening in AI generated responses." STRONG -- directly about the concept being invoked.
**Recommendation:** None needed.
**Quote:** "what has been termed 'doctrinal flattening' \cite{Johnson2026}"

### Finding 20
**Location:** 02-results.md:118
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Koppel2011}` supports claim about Talmudic logic formalization. Bib title: "Computational Approaches to the Talmud." STRONG -- directly about the computational Talmud work being described.
**Recommendation:** None needed.
**Quote:** "Talmudic logic formalization efforts \cite{Koppel2011}"

### Finding 21
**Location:** 02-results.md:124
**Severity:** MAJOR
**Category:** Relevance
**Issue:** `\cite{Kulkarni2022}` is MISSING-BIB. Used to support description of Bhagavad Gita Sentiment Analysis benchmark. Without a bib entry, the reader cannot locate or verify this source paper.
**Recommendation:** Add Kulkarni2022 to the bib file with full bibliographic data for the Bhagavad Gita sentiment analysis paper.
**Quote:** "examination of the source paper \cite{Kulkarni2022} confirms, the benchmark processes English translations"

### Finding 22
**Location:** 02-results.md:134
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Tao2024}` supports description of CValues benchmark. Bib title: "CValues: Measuring the Values of Chinese Large Language Models from Safety to Responsibility." STRONG -- directly about the benchmark being described.
**Recommendation:** None needed.
**Quote:** "CValues \cite{Tao2024}, a 30,000-item Chinese moral evaluation benchmark"

### Finding 23
**Location:** 02-results.md:140 and 142
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Mohamed2020, Carroll2020}` used together again for structural absence of African/Indigenous traditions. Both STRONG -- consistent with earlier usage.
**Recommendation:** None needed.
**Quote:** "their ethical frameworks are not underdeveloped...They are absent because benchmark creation infrastructure systematically disadvantages knowledge systems \cite{Mohamed2020, Carroll2020}"

### Finding 24
**Location:** 02-results.md:150
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Henrich2010}` supports claim about WEIRD bias extending to AI evaluation. Bib title: "The weirdest people in the world?" STRONG -- the foundational WEIRD paper being directly invoked.
**Recommendation:** None needed.
**Quote:** "The WEIRD bias documented in psychology \cite{Henrich2010} extends directly to AI evaluation"

### Finding 25
**Location:** 02-results.md:150
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Birhane2021}` supports claim about traditions legible to GitHub/HuggingFace pipeline. Bib title: "Algorithmic injustice: a relational ethics approach." ADEQUATE -- Birhane discusses relational ethics and algorithmic injustice, but the specific claim about GitHub/HuggingFace pipeline legibility is not the paper's focus. The connection is through the broader frame of whose knowledge counts.
**Recommendation:** None needed, though a more targeted citation on publication infrastructure bias would strengthen this.
**Quote:** "traditions that are evaluable are those legible to the GitHub, HuggingFace, and English-language journal pipeline \cite{Birhane2021}"

### Finding 26
**Location:** 03-discussion.md:29
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Hendrycks2021}` supports comparison to NormEval sister survey. Bib title: "Measuring Massive Multitask Language Understanding" (MMLU). WEAK -- MMLU is a general-purpose LLM benchmark, not specifically about moral judgment vs. moral reasoning. The text claims "28 of 37 benchmarks test moral judgment rather than moral reasoning" citing this, but MMLU is about multitask understanding broadly. The claim may belong to the NormEval survey itself, not to Hendrycks2021.
**Recommendation:** Replace with the actual NormEval paper citation if it exists, or clarify that the 28/37 statistic comes from the authors' own NormEval analysis. MMLU (Hendrycks2021) does contain an ethics subset, but the specific statistic cited does not come from the MMLU paper.
**Quote:** "In the normative ethics domain, 28 of 37 benchmarks test moral judgment rather than moral reasoning \cite{Hendrycks2021}"

### Finding 27
**Location:** 03-discussion.md:71
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Rao2025}` supports epistemological claim about whether behavioral data can resolve questions of understanding. Bib title: "Randomness, Not Representation: The Unreliability of Evaluating Cultural Alignment in LLMs." ADEQUATE -- the paper questions reliability of cultural alignment evaluation, which is related but not directly about the philosophy of understanding.
**Recommendation:** None needed.
**Quote:** "whether producing longer, more nuanced values responses indicates deeper comprehension...cannot be resolved from behavioral data alone \cite{Rao2025}"

### Finding 28
**Location:** 03-discussion.md:71
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Gabriel2020}` supports claim about LLM responses being productions of statistical models, not expressions of understanding. Bib title: "Artificial Intelligence, Values, and Alignment." STRONG -- Gabriel's paper directly addresses AI values and alignment philosophy.
**Recommendation:** None needed.
**Quote:** "LLM responses are productions of statistical language models, not expressions of understanding \cite{Gabriel2020}"

### Finding 29
**Location:** 03-discussion.md:105
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Fricker2007}` supports the concept of epistemic injustice being extended to infrastructure. Bib title: "Epistemic Injustice: Power and the Ethics of Knowing." STRONG -- this IS the foundational work defining epistemic injustice.
**Recommendation:** None needed.
**Quote:** "an extension of Fricker's \cite{Fricker2007} concept of epistemic injustice from interpersonal credibility deficits to evaluation infrastructure"

### Finding 30
**Location:** 03-discussion.md:109
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{TuckYang2012}` supports claim about not reducing decolonization to methodological adjustment. Bib title: "Decolonization is Not a Metaphor." STRONG -- directly about the argument being invoked.
**Recommendation:** None needed.
**Quote:** "Following Tuck and Yang \cite{TuckYang2012}, this paper's recommendations must not reduce decolonization to a methodological adjustment"

### Finding 31
**Location:** 03-discussion.md:131
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Sorensen2024}` supports claim about post-benchmark evaluation paradigms. Bib title: "Value Kaleidoscope: Engaging AI with Pluralistic Human Values, Rights, and Duties." ADEQUATE -- Value Kaleidoscope addresses pluralistic values in AI, relevant to the argument about alternative evaluation approaches but not specifically about community-governed evaluation.
**Recommendation:** None needed.
**Quote:** "consultation-based evaluation, community-led auditing, and deliberative alignment processes \cite{Sorensen2024}"

### Finding 32
**Location:** 04-conclusion.md:7
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Hendrycks2021}` used to compare composite scores (39.9--52.0) against normative ethics benchmark (77.2). Same WEAK concern as Finding 26 -- MMLU's ethics subset may not be the "leading normative ethics benchmark" being referenced. The 77.2 figure likely comes from the authors' own NormEval analysis.
**Recommendation:** Clarify the source of the 77.2 comparison figure. If it comes from NormEval, cite NormEval. If it comes from MMLU's moral scenarios subset specifically, make that explicit.
**Quote:** "composite score range of 39.9--52.0...compared to 77.2 for the leading normative ethics benchmark \cite{Hendrycks2021}"

### Finding 33
**Location:** 04-conclusion.md:15
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Malhas2023}` used again to cite the Quranic QA pipeline model. STRONG -- consistent usage.
**Recommendation:** None needed.
**Quote:** "modeled on the Quranic QA pipeline \cite{Malhas2023}"

### Finding 34
**Location:** 04-conclusion.md:21
**Severity:** MINOR
**Category:** Relevance
**Issue:** `\cite{Carroll2020}` used again to support CARE Principles discussion. STRONG -- consistent usage.
**Recommendation:** None needed.
**Quote:** "The CARE Principles for Indigenous Data Governance \cite{Carroll2020} introduce a critical constraint"

---

## B. Unsupported Claims

### Finding 35
**Location:** 00-abstract.md:3
**Severity:** MAJOR
**Category:** Unsupported-Claim
**Issue:** "Religious values shape the moral reasoning of more than 80% of the world's population" -- a major empirical claim in the very first sentence with no citation. The Pew Research Center (PewResearch2017) IS in the bib and could support this, but it is not cited here.
**Recommendation:** Add `\cite{PewResearch2017}` after this claim.
**Quote:** "Religious values shape the moral reasoning of more than 80% of the world's population"

### Finding 36
**Location:** 00-abstract.md:3
**Severity:** MINOR
**Category:** Unsupported-Claim
**Issue:** "The field of AI alignment has recognized the need for values-aligned evaluation, but treats 'values' as a largely secular construct, operationalized through preference rankings and cultural dimensions" -- a characterization of an entire field with no citation. Gabriel2020, Christiano2017, or Ji2024 could support this.
**Recommendation:** Add citations to AI alignment survey papers (e.g., `\cite{Gabriel2020, Ji2024}`) to support this field characterization.
**Quote:** "The field of AI alignment has recognized the need for values-aligned evaluation, but treats 'values' as a largely secular construct"

### Finding 37
**Location:** 02-results.md:112
**Severity:** MINOR
**Category:** Unsupported-Claim
**Issue:** "materially supported by Gulf state AI strategies in the UAE, Saudi Arabia, and Qatar" -- specific claim about government investment with no citation or source.
**Recommendation:** Add a citation or note "e.g.," with specific program names (SDAIA, MBZUAI, etc.).
**Quote:** "Gulf state investment in computational Arabic---through initiatives in the UAE, Saudi Arabia, and Qatar"

### Finding 38
**Location:** 02-results.md:118
**Severity:** MINOR
**Category:** Unsupported-Claim
**Issue:** "The Bar-Ilan Responsa Project, initiated in the 1960s, represents one of the oldest computational humanities projects" -- a specific historical claim with no citation.
**Recommendation:** Add a citation for the Bar-Ilan Responsa Project. Abraham2019 (Talmudic Logic Project) is in the bib but is a different project.
**Quote:** "The Bar-Ilan Responsa Project, initiated in the 1960s"

### Finding 39
**Location:** 03-discussion.md:43
**Severity:** MINOR
**Category:** Unsupported-Claim
**Issue:** "In Item Response Theory (IRT) terms, the rubric items have extremely low discrimination parameters" -- uses IRT terminology to characterize findings without citing any IRT reference. Srivastava2024 (PATCH: Psychometrics-Assisted Benchmarking) is in the bib and could support this.
**Recommendation:** Add `\cite{Srivastava2024}` or another IRT reference.
**Quote:** "In Item Response Theory (IRT) terms, the rubric items have extremely low discrimination parameters"

### Finding 40
**Location:** 03-discussion.md:131
**Severity:** MINOR
**Category:** Unsupported-Claim
**Issue:** Claims about MUKURTU CMS and Local Contexts initiative have no citations despite being specific, named platforms.
**Recommendation:** Add URL or citation references for MUKURTU CMS and Local Contexts.
**Quote:** "the MUKURTU CMS implements culturally specific access protocols for Indigenous digital heritage, and the Local Contexts initiative"

### Finding 41
**Location:** 04-conclusion.md:15
**Severity:** MINOR
**Category:** Unsupported-Claim
**Issue:** "The Sefaria digital library contains the complete Tanakh, Talmud, and centuries of rabbinic commentary in machine-readable format" -- specific claim about a digital resource with no citation.
**Recommendation:** Add a URL or citation for Sefaria (sefaria.org).
**Quote:** "The Sefaria digital library contains the complete Tanakh, Talmud, and centuries of rabbinic commentary"

### Finding 42
**Location:** 04-conclusion.md:15
**Severity:** MINOR
**Category:** Unsupported-Claim
**Issue:** "The Chinese Classics Digital Library provides annotated Confucian and Daoist texts" -- specific resource claim with no citation.
**Recommendation:** Add URL or citation.
**Quote:** "The Chinese Classics Digital Library provides annotated Confucian and Daoist texts"

---

## C. Citation Concentration Analysis

### Citation Frequency Table

| Key | Count | Sections |
|-----|-------|----------|
| Carroll2020 | 6 | Methods, Results, Discussion, Conclusion |
| Mohamed2020 | 4 | Methods, Results, Discussion |
| Malhas2023 | 4 | Results, Discussion, Conclusion |
| Hendrycks2021 | 3 | Discussion, Conclusion |
| Liang2023 | 2 | Methods, Results |
| Alharbi2024 | 2 | Methods, Results |
| Johnson2026 | 2 | Results, Discussion |
| Henrich2010 | 2 | Results, Discussion |
| Kamali2008 | 2 | Results, Discussion |
| All others | 1 | Various |

### Finding 43
**Location:** Multiple files
**Severity:** MINOR
**Category:** Concentration
**Issue:** `Carroll2020` is cited 6 times across 4 files. While justified given the paper's central concern with Indigenous data governance, this heavy reliance on a single source for the CARE Principles argument should be noted. The argument would benefit from additional supporting references on Indigenous data sovereignty.
**Recommendation:** Consider adding 1-2 additional references on Indigenous data governance to distribute the argumentative weight (e.g., Kukutai & Taylor 2016 on Indigenous Data Sovereignty, or Walter & Suina 2019).
**Quote:** N/A (systemic)

### Finding 44
**Location:** Multiple files
**Severity:** MINOR
**Category:** Concentration
**Issue:** `Mohamed2020` is cited 4 times. Justified given the decolonial AI framework is central to the structural analysis. No action needed.
**Recommendation:** None needed.
**Quote:** N/A (systemic)

### Section Citation Density

| Section | File | Unique Citation Keys | Status |
|---------|------|---------------------|--------|
| 3 (Methods) | 01-methods.md | 10 | OK |
| 4 (Results) | 02-results.md | 14 | OK |
| 5 (Discussion) | 03-discussion.md | 14 | OK |
| 6 (Conclusion) | 04-conclusion.md | 3 | BORDERLINE |

### Finding 45
**Location:** 04-conclusion.md
**Severity:** MINOR
**Category:** Concentration
**Issue:** Section 6 (Conclusion) has only 3 unique citation keys (Hendrycks2021, Malhas2023, Carroll2020). While conclusions often rely on the paper's own findings, the Calls to Action make substantive claims that could benefit from additional citations -- particularly Call 2 (reasoning-focused benchmarks) and Call 4 (cross-vendor standards) which cite no references.
**Recommendation:** Add 1-2 citations to Calls 2 and 4 to anchor recommendations in existing literature (e.g., Burnell2023 for evaluation standards, Schlangen2021 for benchmark methodology).
**Quote:** N/A (systemic)

---

## D. Sections 1--2 Anticipation: Forward References Needing Citations

### Finding 46
**Location:** 03-discussion.md:29
**Severity:** MAJOR
**Category:** Sec1-2-Need
**Issue:** "The parallel to this paper's sister survey, NormEval, strengthens the diagnosis" -- NormEval is referenced as a companion paper but never cited. When Sections 1--2 are written, NormEval needs a proper citation.
**Recommendation:** Add NormEval citation to bib. If unpublished, cite as "Lin (in preparation)" or similar.
**Quote:** "The parallel to this paper's sister survey, NormEval"

### Finding 47
**Location:** 03-discussion.md:5
**Severity:** MINOR
**Category:** Sec1-2-Need
**Issue:** "most religious values benchmarks test religious knowledge recall...almost none test religious values reasoning" -- this is the paper's central thesis statement. Section 1 (Introduction) will need citations establishing: (a) the growth of religious AI benchmarks, (b) prior work on construct validity in benchmarks, (c) existing surveys of AI evaluation.
**Recommendation:** Checklist for Sec 1-2: cite Chang2024 (survey of LLM evaluation), Li2025 (construct validity), Burnell2023 (rethinking evaluation reporting), Ong2025 (construct validity in medical LLM benchmarks).
**Quote:** N/A (anticipatory)

### Finding 48
**Location:** 02-results.md:0-3
**Severity:** MINOR
**Category:** Sec1-2-Need
**Issue:** The Results section opens with "We present findings from our systematic meta-evaluation of 401 religious values benchmark candidates across 14 traditions" -- Section 2 (Related Work) will need to establish what prior surveys exist. Many bib entries are currently unused in Sections 3-6 and likely reserved for Sections 1-2.
**Recommendation:** Checklist for Sec 2: cite Adilazuarda2025 (cultural alignment), Durmus2024 (global opinions), Hofstede2011 (cultural dimensions), Schwartz2012 (values theory), Ji2024 (AI alignment survey), Christiano2017 (RLHF), Bai2022 (HHH), Ouyang2022 (instruction following). These are all in the bib but uncited in Sections 3-6.
**Quote:** N/A (anticipatory)

### Finding 49
**Location:** 03-discussion.md:85
**Severity:** MINOR
**Category:** Sec1-2-Need
**Issue:** Reference to "survey instruments designed for human respondents" measuring cultural attitudes -- Section 2 should establish the relationship between cultural values research (Schwartz, Hofstede, World Values Survey) and AI alignment.
**Recommendation:** Cite Schwartz2012, Hofstede2011 in Section 2 when establishing background on values measurement.
**Quote:** "cultural attitudes of religious populations as measured by survey instruments designed for human respondents \cite{Henrich2010, Klingefjord2024}"

### Finding 50
**Location:** Multiple discussion subsections
**Severity:** MINOR
**Category:** Sec1-2-Need
**Issue:** Multiple references to "the field" and "prior surveys" without specific citations. Sections 1-2 must establish what "the field" is and cite prior work systematically.
**Recommendation:** Create a structured Related Work section covering: (1) AI alignment and values (Gabriel2020, Ji2024, Klingefjord2024), (2) LLM evaluation methodology (Chang2024, Liang2023, Bowman2021, Schlangen2021, Burnell2023), (3) Religious bias in NLP (Abid2021, Bianchi2024, Nadeem2021, Hamid2025, Putri2025, Naous2024), (4) Religion-specific AI ethics (Ezzeddine2024, Habib2023, AlMusawi2022, Chadha2023, Hongladarom2020, Wong2019), (5) Decolonial and non-Western AI (Mohamed2020, Birhane2021, Mhlambi2020, Gwagwa2025).
**Quote:** N/A (anticipatory)

---

## Unused Bib Entries (not cited in Sections 3-6)

The following 44 bib entries appear in the bibliography but are NOT cited anywhere in Sections 3-6. They are presumably reserved for Sections 1-2 (Introduction/Related Work):

Abraham2019, Abdelali2023 (cited once in Results actually -- disregard), Adilazuarda2025, AlAzani2023, AlMusawi2022, Asghari2023, Bai2022, Buyl2024, Chadha2023, Chang2024, Christiano2017, Durmus2024, Ezzeddine2024, Green2014, Gwagwa2025, Habib2023, Hamid2025, Hofstede2011, Hongladarom2020, Ji2024, Keown2005, Klingefjord2024 (cited once in Discussion), Levy2024, Li2022, Li2025, Manyika2024, Mhlambi2020, Mishra2024, MofenjouPeuriekeu2024, Mohadi2024, Mohanty2024, Muravyov2025, Nadeem2021, Naous2024, Ogwo2025, Ong2025, Ouyang2022, Putri2025, Roberts2022, Rodriguez2021, RomeCall2020, Rosenfeld2021, Schlangen2021, Schwartz2012, Schweiker2005, SinghKaur2024, Srivastava2023, Srivastava2024, Steinberg2025, Sukiennik2025, Varghese2023, Verma2023, Wong2019, ZhaoLiu2015

**Note:** This is a very large number of unused entries (44 of 83 = 53%). If Sections 1-2 do not absorb most of these, the bibliography should be pruned. Reviewers may flag unused references.

---

## Per-Citation Relevance Table

| Key | File:Line | Surrounding Claim (abbreviated) | Bib Title | Rating |
|-----|-----------|--------------------------------|-----------|--------|
| Nida1964 | 01-methods:27 | Translation transforms theological concepts | MISSING-BIB (likely Nida, *Toward a Science of Translating*) | STRONG (if correct) |
| Alharbi2024 | 01-methods:81 | IslamicMMLU R2 calibration anchor | IslamicMMLU: A Benchmark... | STRONG |
| Zhang2024 | 01-methods:91 | Emerging theological dialogue systems | MISSING-BIB | UNKNOWN |
| Bowman2021 | 01-methods:107 | Data access needed for verification | What Will it Take to Fix Benchmarking... | STRONG |
| Liang2023 | 01-methods:107 | Avoid over-rewarding incumbency | Holistic Evaluation of Language Models | ADEQUATE |
| Gehrmann2022 | 01-methods:109 | Data accessibility is primary bottleneck | Repairing the Cracked Foundation... | STRONG |
| Mohamed2020 | 01-methods:113 | Structural epistemic injustice | Decolonial AI | STRONG |
| Carroll2020 | 01-methods:113 | Indigenous data governance exclusion | CARE Principles | STRONG |
| Leavens2024 | 01-methods:133 | Sacred texts not "just data" | Modeling the Sacred... | STRONG |
| Cohen1988 | 01-methods:216 | Effect size threshold conventions | MISSING-BIB (likely Cohen, *Statistical Power Analysis*) | STRONG (if correct) |
| Carroll2020 | 01-methods:238 | Hard gate as structural exclusion | CARE Principles | STRONG |
| Mohamed2020 | 02-results:17 | Oral/communal knowledge systems excluded | Decolonial AI | STRONG |
| Bilimoria2013 | 02-results:17 | Oral/communal knowledge systems | Indian Ethics: Classical Traditions... | ADEQUATE |
| Gupta2025 | 02-results:21 | Psychometric approaches in secular values | LLM Psychometrics: A Systematic Review | STRONG |
| Liang2023 | 02-results:25 | Nascent field, limited consolidation | Holistic Evaluation of Language Models | ADEQUATE |
| Alharbi2024 | 02-results:79 | ELQV highest composite score | IslamicMMLU: A Benchmark... | **MISATTRIBUTED** |
| Malhas2023 | 02-results:112 | Quranic QA shared task pipeline | HAQA and QUQA... | STRONG |
| Abdelali2023 | 02-results:112 | Arabic NLP community investment | AceGPT: Localizing LLMs in Arabic | STRONG |
| Kamali2008 | 02-results:112 | Maqasid al-Shariah framework | Maqasid al-Shariah Made Simple | STRONG |
| Francis2015 | 02-results:116 | Vatican's Rome Call for AI Ethics | Laudato Si': On Care for Our Common Home | **MISATTRIBUTED** |
| Johnson2026 | 02-results:116 | Doctrinal flattening concept | Detecting doctrinal flattening... | STRONG |
| Koppel2011 | 02-results:118 | Talmudic logic formalization | Computational Approaches to the Talmud | STRONG |
| Kulkarni2022 | 02-results:124 | Bhagavad Gita Sentiment source paper | MISSING-BIB | UNKNOWN |
| Tao2024 | 02-results:134 | CValues benchmark description | CValues: Measuring Values of Chinese LLMs... | STRONG |
| Mohamed2020 | 02-results:140 | African/Indigenous structural absence | Decolonial AI | STRONG |
| Carroll2020 | 02-results:142 | CARE Principles, data sovereignty | CARE Principles | STRONG |
| Henrich2010 | 02-results:150 | WEIRD bias in psychology extends to AI | The weirdest people in the world? | STRONG |
| Birhane2021 | 02-results:150 | Traditions legible to GitHub pipeline | Algorithmic injustice: relational ethics | ADEQUATE |
| Malhas2023 | 03-discussion:11 | Quranic QA shared task (repeated) | HAQA and QUQA... | STRONG |
| Kamali2008 | 03-discussion:15 | Maqasid al-Shariah (repeated) | Maqasid al-Shariah Made Simple | STRONG |
| Johnson2026 | 03-discussion:17 | Doctrinal flattening (repeated) | Detecting doctrinal flattening... | STRONG |
| Hendrycks2021 | 03-discussion:29 | NormEval sister survey comparison | Measuring Massive Multitask Language Understanding | WEAK |
| Rao2025 | 03-discussion:71 | Behavioral data insufficient for understanding | Randomness, Not Representation... | ADEQUATE |
| Gabriel2020 | 03-discussion:71 | LLM responses not expressions of understanding | AI, Values, and Alignment | STRONG |
| Abid2021 | 03-discussion:83 | Religious bias detection in LLMs | Persistent Anti-Muslim Bias... | STRONG |
| Bianchi2024 | 03-discussion:83 | Religious bias/stereotypes in LLMs | Divine LLaMAs: Bias, Stereotypes... | STRONG |
| Henrich2010 | 03-discussion:85 | Secular cultural attitudes measurement | The weirdest people in the world? | ADEQUATE |
| Klingefjord2024 | 03-discussion:85 | Values measurement for AI alignment | What Are Human Values... | STRONG |
| Fricker2007 | 03-discussion:105 | Epistemic injustice concept | Epistemic Injustice: Power and Ethics of Knowing | STRONG |
| Mohamed2020 | 03-discussion:107 | Algorithmic coloniality in evaluation | Decolonial AI | STRONG |
| Carroll2020 | 03-discussion:109 | CARE Principles, data sovereignty (repeated) | CARE Principles | STRONG |
| TuckYang2012 | 03-discussion:109 | Decolonization not a metaphor | Decolonization is Not a Metaphor | STRONG |
| Malhas2023 | 03-discussion:115 | Quranic QA pipeline model (repeated) | HAQA and QUQA... | STRONG |
| Sorensen2024 | 03-discussion:131 | Post-benchmark evaluation paradigms | Value Kaleidoscope... | ADEQUATE |
| TuckYang2012 | 03-discussion:135 | Extractive research dynamics | Decolonization is Not a Metaphor | STRONG |
| Hendrycks2021 | 04-conclusion:7 | Composite score comparison (77.2) | Measuring Massive Multitask Language Understanding | WEAK |
| Malhas2023 | 04-conclusion:15 | Quranic QA pipeline model (repeated) | HAQA and QUQA... | STRONG |
| Carroll2020 | 04-conclusion:21 | CARE Principles constraint (repeated) | CARE Principles | STRONG |

---

## Summary of CRITICAL/MAJOR Issues

| # | Severity | Issue | Action Required |
|---|----------|-------|-----------------|
| F14 | CRITICAL | `\cite{Alharbi2024}` on ELQV is MISATTRIBUTED -- Alharbi2024 is IslamicMMLU, not ELQV | Add correct ELQV bib entry; fix citation |
| F18 | CRITICAL | `\cite{Francis2015}` for Rome Call is MISATTRIBUTED -- Francis2015 is Laudato Si'; should be RomeCall2020 | Replace with `\cite{RomeCall2020}` |
| F3 | MAJOR | Zhang2024 MISSING-BIB | Add to bib or remove citation |
| F9 | MAJOR | Cohen1988 MISSING-BIB | Add to bib (standard statistics reference) |
| F21 | MAJOR | Kulkarni2022 MISSING-BIB | Add to bib (Bhagavad Gita Sentiment paper) |
| F1 | MAJOR | Nida1964 MISSING-BIB | Add to bib (translation theory classic) |
| F26 | MAJOR | Hendrycks2021 used for NormEval 28/37 stat -- likely wrong source | Replace with NormEval citation |
| F35 | MAJOR | "80% of world's population" uncited in abstract | Add PewResearch2017 |
| F46 | MAJOR | NormEval sister survey referenced but never cited | Add NormEval bib entry |

**Total findings:** 50
**CRITICAL:** 2 (misattributed citations)
**MAJOR:** 7 (missing bib entries, wrong sources, unsupported claims)
**MINOR:** 41 (adequate citations, minor gaps, anticipatory needs)
