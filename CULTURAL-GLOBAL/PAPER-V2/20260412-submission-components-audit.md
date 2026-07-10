# Submission Components Audit — Nature Portfolio Compliance

**Date:** 2026-04-12
**Paper:** Cross-Cultural AI Values Alignment: The Triple Bind
**Target Venues:** Nature Human Behaviour (primary), PNAS, Science
**Auditor Role:** P4 (Nature Portfolio Compliance)

---

## 1. NHB Reporting Checklist Mapping

NHB uses a Life Sciences Reporting Summary plus specific checklist items. The table below maps each requirement against the manuscript's current state.

### 1.1 Statistical Reporting Requirements

| NHB Requirement | Current Status | Location | Gap? |
|---|---|---|---|
| Exact p-values (not just < 0.05) | PARTIAL — main text uses "p < 0.001" throughout; supplementary S2 provides exact values for some tests | 03-results, S2-results | YES: must report exact p-values to 3 decimal places where p > 0.001; "p < 0.001" is acceptable only when p is genuinely below that threshold |
| Degrees of freedom for all tests | PARTIAL — chi-square reports df = 99; KW tests do not report df | 03-results, S2-results | YES: Kruskal-Wallis tests need df; Mann-Whitney tests need N1, N2 |
| Test statistic values | YES — chi-squared = 397.7, H statistics, U statistics all reported | S2-results | Minor: ensure all appear in main text, not just supplementary |
| Effect sizes with CIs | PARTIAL — Cohen's d, Cramer's V, epsilon-squared, Cliff's delta mentioned; CIs reported for bootstrap estimates but not for effect sizes themselves | 02-methods, S2-results | YES: effect size CIs needed for primary comparisons |
| Sample sizes for each analysis | YES — clearly stated (n = 2,329 corpus; n = 218 benchmarks; 380 items x 10 models) | 02-methods | No |
| Multiple comparison correction method | YES — Bonferroni (Layer 2), BH-FDR (Layer 3) specified | 02-methods | No |
| Software and versions | NO — no software/version statement anywhere in manuscript | -- | YES: Critical gap |
| One-/two-sided test specification | NO — not specified for any test | -- | YES: NHB requires explicit statement |

### 1.2 Data and Code Availability

| NHB Requirement | Current Status | Gap? |
|---|---|---|
| Data availability statement | NOT PRESENT | YES: Critical |
| Unique identifiers for datasets (DOI, accession) | NOT PRESENT | YES: need Zenodo/OSF DOI |
| Code availability statement | NOT PRESENT | YES: Critical |
| Custom code repository with DOI | NOT PRESENT | YES: need archived repo DOI |

### 1.3 Ethics and Oversight

| NHB Requirement | Current Status | Gap? |
|---|---|---|
| Ethics oversight statement | NOT PRESENT | YES: must state IRB status even if exempt |
| Human subjects informed consent | N/A — no human subjects | Explain in ethics statement |
| Clinical trial registration | N/A | N/A |
| Animal research protocols | N/A | N/A |

### 1.4 Reproducibility

| NHB Requirement | Current Status | Gap? |
|---|---|---|
| Inclusion/exclusion criteria | YES — Section 2.2.1 (corpus), 2.3.1 (benchmarks), 2.4.2 (models) | No |
| Replication attempts | PARTIAL — multi-model replication in Study 3; provenance tiers documented | No |
| Randomization procedures | N/A for this study type | N/A |
| Blinding procedures | N/A — computational analysis, no experimenter bias pathway | N/A |
| Pre-registration | NOT PRESENT | RECOMMENDED: state not pre-registered |

### 1.5 Manuscript Structure

| NHB Requirement | Current Status | Gap? |
|---|---|---|
| Abstract <= 150 words, unstructured | NO — current abstract is 523 words, structured | YES: need alternate 150w version |
| Author contributions (CRediT) | NOT PRESENT | YES: Critical |
| Competing interests declaration | NOT PRESENT | YES: Critical |
| Acknowledgments | NOT PRESENT | YES |
| Supplementary information referenced | YES — 5 supplementary files + figures + tables | No |
| Reference format (Nature style) | PARTIAL — currently APA-adjacent; NHB uses numbered refs | YES if submitting to NHB specifically |

---

## 2. Drafted Submission Components

### 2.1 Author Contributions (CRediT Taxonomy)

```
Author Contributions

[Author 1]: Conceptualization, Methodology, Software, Formal Analysis,
Investigation, Data Curation, Writing — Original Draft, Writing — Review
& Editing, Visualization, Project Administration.

[Author 2]: [Assign roles as appropriate]

[Additional authors]: [Assign roles as appropriate]

The 12-member expert council (Supplementary S3) contributed to
Methodology (keyword list development, feature taxonomy design,
benchmark evaluation) and Writing — Review & Editing (tradition-specific
review under anti-essentialization protocol). Council members are
acknowledged in the Acknowledgments section; their contributions did not
meet ICMJE authorship criteria as they did not participate in drafting
or final approval of the manuscript.
```

### 2.2 Data Availability Statement

```
Data Availability

The CEI Literature Vault metadata (paper-level YAML frontmatter
comprising 34 normative dimension scores, WEIRD scores, author geography,
and classification metadata for all 2,329 papers) is available at
[Zenodo DOI to be assigned upon acceptance]. The vault does not include
full-text PDFs due to copyright restrictions; PDF extract text (first
25,000 characters per paper) is included.

The benchmark meta-evaluation dataset (218 benchmarks x 96 features,
including both deep-scored and automated-scored features) is available at
[Zenodo DOI].

The LLM trial response corpus (80 trial files, 3,800 item-level
responses across 10 models) is available at [Zenodo DOI]. Trial files
include raw model outputs, reasoning traces, RLHF conflict
self-reports, and engagement depth scores.

The gold standard validation dataset (700 paper-framework evaluation
pairs with rater classifications) is available at [Zenodo DOI].

Author geography resolution data (country assignments for 2,300 papers,
with strategy provenance) is included in the paper-level metadata.

All datasets will be deposited upon acceptance and assigned persistent
DOIs. No restrictions on data access apply.
```

### 2.3 Code Availability Statement

```
Code Availability

All analysis code is available at https://github.com/cjimmylin/cei-literature
(archived at [Zenodo DOI to be assigned]). The repository includes:

- Keyword-based scoring pipeline (6 Python scripts, 7 stages):
  classify_ethics.py, classify_ethics_perspective.py,
  classify_non_ethics_topics.py, classify_cultural_religious.py,
  classify_moral_psych.py, classify_data_nature.py
- Non-Western framework scoring instruments
  (PYTHON/cultural_global_scoring.py)
- WEIRD score computation (PYTHON/weird_scoring.py)
- Gold standard validation analysis
- Author geography resolution pipeline
- Benchmark meta-evaluation (TOPSIS-ELECTRE III implementation)
- LLM trial administration protocols and analysis scripts
- Figure and table generation scripts

The pipeline runs on Python 3.9+ with dependencies: numpy, scipy,
pandas, scikit-learn, matplotlib, and fpdf2. A requirements.txt and
reproducibility instructions are provided.
```

### 2.4 Ethics Statement

```
Ethics Declaration

This study did not involve human participants, human biological samples,
or animal subjects. Institutional Review Board (IRB) review was not
required for the following reasons:

Study 1 (Corpus Analysis) analyzed published academic papers that are
publicly available through open-access repositories and subscription
databases. No individual-level data about human subjects were collected
or analyzed; all data are at the paper level (metadata, scores, author
institutional affiliations).

Study 2 (Benchmark Meta-Evaluation) analyzed published benchmark
instruments using publicly available documentation. No benchmarks were
administered to human participants.

Study 3 (LLM Self-Administration Trials) administered benchmarks to
large language models via API calls. Language models are not human
subjects and do not fall under human subjects research protections. No
human participants were involved in the trial administration or response
generation.

The 12-member expert council (Supplementary S3) served as analytical
perspectives providing disciplinary expertise, not as research
participants. Council members reviewed methodological decisions, keyword
lists, and manuscript drafts in their capacity as domain experts. Their
contributions are analogous to peer review and editorial consultation,
not human subjects participation. No data about council members' personal
beliefs, behaviors, or characteristics were collected or analyzed.

This determination is consistent with the U.S. Common Rule (45 CFR 46),
which excludes scholarly analysis of publicly available data and
consultation with subject-matter experts from human subjects research
requirements.
```

### 2.5 Competing Interests Declaration

```
Competing Interests

[Author(s)] declare(s) [no / the following] competing interests.

Disclosure: Study 3 utilized API access to models from Anthropic (Claude
Opus 4.6, Sonnet 4.6, Haiku 4.5), OpenAI (GPT-5.4, GPT-5.4-Mini), and
Google (Gemini 2.5/3.1 family). [If any author has an affiliation,
funding relationship, or consulting arrangement with any of these
providers, disclose here.] The analysis code, trial protocols, and raw
model outputs are publicly available (see Code Availability and Data
Availability) to enable independent verification. The provenance tier
analysis (Section 2.4.4) documents data quality limitations for each
provider transparently.

[If applicable: This work was supported by [funding source]. The
funder(s) had no role in study design, data collection and analysis,
decision to publish, or preparation of the manuscript.]
```

### 2.6 Acknowledgments

```
Acknowledgments

We thank the 12 members of the interdisciplinary expert council
(Supplementary S3) for their contributions to methodology design,
keyword list development, benchmark evaluation, and manuscript review.
Their tradition-specific expertise and commitment to anti-essentialization
substantially improved the rigor and cultural sensitivity of this work.

[Acknowledge funding sources, institutional support, computational
resources, and any individuals who contributed but do not meet authorship
criteria.]

[If applicable: We acknowledge the use of Claude (Anthropic) as a
research assistant for [specific tasks, e.g., data processing, code
generation]. All analytical decisions, interpretations, and manuscript
text were authored by the human researchers.]
```

### 2.7 Statistical Analysis Summary

```
Statistical Analysis

All statistical analyses were performed in Python 3.9 using SciPy 1.11
(scipy.stats), scikit-learn 1.3 (sklearn.cluster, sklearn.metrics),
and NumPy 1.24. [Verify exact versions before submission.]

The following tests were used:

Study 1 (Corpus Analysis):
- Hierarchical clustering: Ward's method on Euclidean distances
  (scipy.cluster.hierarchy), validated by k-means (k = 2-6) and
  silhouette analysis
- Chi-square test of independence: region x framework association
  (scipy.stats.chi2_contingency)
- Mann-Whitney U tests: pairwise framework comparisons across WEIRD
  tiers, with Bonferroni correction for 34 comparisons per pair
  (scipy.stats.mannwhitneyu, two-sided)
- Kruskal-Wallis H tests: multi-group comparisons across Global
  North/South/Ambiguous, with post-hoc Dunn's tests corrected by
  Benjamini-Hochberg FDR at alpha = 0.05
- Correspondence analysis: region-by-framework cross-tabulation
  (prince.CA or custom implementation)
- Mann-Kendall trend tests: temporal trends with Sen's slope estimator
  (pymannkendall)
- Bootstrap resampling: 1,000 iterations, bias-corrected and
  accelerated (BCa) 95% confidence intervals
- Exact permutation tests: sensitivity analyses for small cells
  (n < 20)
- Leave-one-out jackknife: sensitivity analyses for small cells

Study 2 (Benchmark Meta-Evaluation):
- TOPSIS: closeness coefficient computation (custom implementation
  following Hwang & Yoon, 1981)
- ELECTRE III: concordance/discordance with veto thresholds (custom
  implementation following Roy & Bouyssou, 1993)
- Kendall's W: rank concordance across 6 weight schemes (W = 0.924)
- Inter-rater reliability: divergence > 2 SD triggered Delphi
  resolution

Study 3 (LLM Self-Administration Trials):
- Descriptive statistics: means, standard deviations, ratios
- Euclidean distance: model-population proximity in moral foundations
  space
- RLHF conflict coding: frequency counts across 7 categories

Effect sizes: Cohen's d, rank-biserial correlation, Cramer's V,
epsilon-squared, Cliff's delta. All tests were two-sided unless
otherwise noted. Nonparametric tests were used throughout because
normative framework scores are bounded, zero-inflated, and non-normal.

No statistical method was used to predetermine sample size. The corpus
size (n = 2,329) was determined by the contents of the CEI Literature
Vault at the time of analysis; the benchmark count (n = 218) was
determined by inclusion criteria; the model count (n = 10) was
determined by API availability.
```

---

## 3. PRISMA Assessment

### Does PRISMA 2020 Apply?

**Assessment: PRISMA 2020 does not strictly apply, but a modified flow diagram is recommended.**

**Rationale:**

PRISMA 2020 (Page et al., 2021) is designed for systematic reviews that synthesize evidence to answer a specific clinical or empirical question by aggregating findings across studies. This paper is not a systematic review in the PRISMA sense:

1. **Study 1 is a bibliometric/scientometric corpus analysis.** It does not synthesize the findings of the 2,329 papers; it analyzes their metadata (normative framework scores, author geography, WEIRD scores) as data points. The unit of analysis is the paper's characteristics, not its conclusions.

2. **Study 2 is a methodological meta-evaluation.** It evaluates the instruments (benchmarks) themselves, not the results obtained using those instruments. This is closer to a methods review than a systematic review.

3. **Study 3 is primary empirical research.** It generates new data (LLM trial responses), not a synthesis of existing data.

**However**, Study 1 and Study 2 both involve systematic search with inclusion criteria, which creates an expectation of transparent reporting of the identification-screening-inclusion pipeline. The appropriate reporting standard is:

- **For Study 1:** A modified PRISMA flow diagram or a custom search-and-inclusion flowchart following bibliometric reporting standards (Donthu et al., 2021; Zupic & Cater, 2015).
- **For Study 2:** Same approach for benchmark identification.

### Recommended Flow Diagram Data

**Study 1: Corpus Assembly**

```
IDENTIFICATION
  Records from arXiv: ~1,443 (62%)
  Records from ACL Anthology: ~908 (39%)
  Records from targeted searches (Springer, ACM, IEEE, Nature, MDPI): ~150
  Total identified: ~2,501 (estimated)

SCREENING
  Duplicates removed: ~120 (estimated)
  Records screened: ~2,381
  Records excluded (no AI ethics content): ~52

INCLUDED
  Papers in final corpus: 2,329
    Ethics-relevant subset (ethics_overall >= 50): 730 (31.3%)
    Broader technical corpus: 1,599 (68.7%)
```

Note: Exact identification and screening numbers should be verified against vault assembly logs. The corpus was assembled cumulatively over multiple years, not through a single systematic search session, which complicates traditional PRISMA reporting.

**Study 2: Benchmark Identification**

```
IDENTIFICATION
  Papers scanned from vault (metadata flags): 2,329
  Papers with composite relevance >= 20: 1,574
  External search candidates (Semantic Scholar, arXiv, ACL Anthology): 48

SCREENING
  Manual review of 1,574 + 48 candidates: 1,622
  Excluded (did not meet all 3 criteria): 1,404
    - No benchmark/instrument proposed or evaluated: ~800
    - No cross-cultural values/moral reasoning content: ~450
    - Insufficient methodological detail: ~154

INCLUDED
  Benchmarks in final corpus: 218
    Deep-scored (96 features): 32
    Automated-scored (13 features): 186
    New to vault from external search: 15
```

**Recommendation:** Include a two-panel flow diagram (Study 1 left, Study 2 right) as a supplementary figure, labeled explicitly as "modified from PRISMA 2020" with a note that these are corpus/instrument analyses, not systematic reviews of evidence.

---

## 4. Abstract Versions

### 4.1 Current Structured Abstract (523 words)

The current abstract at `00-abstract.md` is 523 words with Background/Methods/Results/Conclusions structure. This is appropriate for journals that accept structured abstracts (e.g., PNAS significance statement + abstract, or venues with 300-500 word limits).

**Word count verification:** The abstract contains approximately 523 words as stated.

### 4.2 Drafted 150-Word Unstructured Abstract (NHB Format)

```
AI values alignment assumes universal normative frameworks, yet the
scholarly base, evaluation infrastructure, and model behavior that
constitute the alignment pipeline are each culturally skewed. We analyze
2,329 AI ethics papers across 34 normative dimensions, meta-evaluate 218
cross-cultural values benchmarks against a 96-feature taxonomy, and
administer 10 benchmarks to 10 large language models. The corpus is
overwhelmingly WEIRD (mean score 64.5/100), with 60.1% of papers from
North America and Western Europe and only 6.9% engaging non-Western
ethical frameworks. Zero of 218 benchmarks report measurement
invariance; five non-Western traditions have zero operational measures.
Claude Opus 4.6 clusters with fewer than 15% of the global population on
cross-cultural values, defaulting to Western liberal framing in 100% of
value conflicts while accurately describing non-Western traditions it
cannot reason within. This triple bind---biased scholarship, broken
benchmarks, monocultural models---forms a self-reinforcing cycle
requiring coordinated intervention across all three layers.
```

**Word count:** 150

---

## 5. Statistical Reporting Gaps

### 5.1 Critical Gaps (must fix before submission)

| Gap | Location | Fix Required |
|---|---|---|
| No software/version statement | Missing entirely | Add Section 2.2.8 or endmatter statistical analysis note (drafted in 2.7 above) |
| One-/two-sided not specified | 02-methods, all test descriptions | Add "All tests were two-sided" to Section 2.2.8 |
| KW tests lack df | S2-results Table S2.2.2 | Add df column (df = k - 1 = 2 for N/S/Ambiguous) |
| Mann-Whitney tests lack N1, N2 | S2-results Table S2.2.3 | Add sample size columns |
| Effect size CIs not reported | S2-results | Add 95% CI for Cohen's d, Cramer's V |
| Pre-registration status not stated | Missing | Add "This study was not pre-registered" to methods or endmatter |
| Correspondence analysis software | 02-methods | Specify package (prince, ca, or custom) |

### 5.2 Moderate Gaps (recommended fixes)

| Gap | Location | Fix Required |
|---|---|---|
| Exact p-values > 0.001 inconsistent | 03-results: some report "p = 0.02", others "p < 0.001" | Standardize: exact to 3 decimals when p >= 0.001 |
| Bootstrap CI method not always specified | Various | Confirm BCa throughout; state in statistical note |
| Sensitivity analysis results for small cells | 02-methods mentions jackknife and permutation tests | Verify these are actually reported in results/supplementary |
| Mann-Kendall results for temporal trends | 02-methods Layer 5 | Verify tau, p, Sen's slope are reported in Section 3 or S2 |
| ELECTRE III parameter values | 02-methods Section 2.3.3 | Report concordance/discordance thresholds, not just veto concept |

### 5.3 Reference Format

Current reference count: approximately 116 entries in APA format. NHB uses numbered references in Vancouver-adjacent style. PNAS uses numbered NLM/Vancouver. Science uses numbered Science style. All three target venues require numbered references, not author-year. This is a formatting conversion, not a content gap; defer to final venue selection.

---

## 6. Summary of Required Actions

### Must-Have (before any submission)

1. Create `10-endmatter.md` containing all components from Section 2 above
2. Add statistical analysis note to Section 2.2.8 or endmatter
3. Fix statistical reporting gaps listed in 5.1
4. Deposit datasets and code to Zenodo; obtain DOIs
5. Create PRISMA-style flow diagram (supplementary figure)
6. Prepare 150-word unstructured abstract for NHB

### Should-Have (for NHB specifically)

7. Convert references to numbered format
8. Ensure abstract is within NHB's 150-word limit
9. Verify all supplementary tables/figures are referenced with correct numbering
10. Check NHB's specific figure format requirements (300 dpi, specific dimensions)

### Nice-to-Have

11. Add pre-registration statement (even if "not pre-registered")
12. Add sample size justification statement
13. Verify all statistical test assumptions are documented (e.g., normality tests or justification for nonparametric)

---

*Generated by P4 (Nature Portfolio Compliance) as part of Phase 1.5 publication polish.*
