# Endmatter

## Author Contributions

Author contributions are reported using the CRediT (Contributor Roles Taxonomy) framework.

**[Author 1]:** Conceptualization, Methodology, Software, Formal Analysis, Investigation, Data Curation, Writing --- Original Draft, Writing --- Review & Editing, Visualization, Project Administration.

**[Author 2]:** [Assign roles as appropriate.]

**[Additional authors]:** [Assign roles as appropriate.]

The 12-member expert council (Supplementary S3) contributed to Methodology (keyword list development, feature taxonomy design, benchmark evaluation via modified Delphi protocol) and Writing --- Review & Editing (tradition-specific review under anti-essentialization protocol). Council members are acknowledged in the Acknowledgments section; their contributions did not meet ICMJE authorship criteria as they did not participate in drafting or final approval of the manuscript.

**CRediT categories:** Conceptualization; Data Curation; Formal Analysis; Funding Acquisition; Investigation; Methodology; Project Administration; Resources; Software; Supervision; Validation; Visualization; Writing --- Original Draft; Writing --- Review & Editing.


## Data Availability Statement

The following datasets are available:

1. **Study 1 corpus metadata.** Paper-level YAML frontmatter comprising 34 normative dimension scores, composite WEIRD scores, author geography assignments (with strategy provenance), and classification metadata for all 2,329 papers is available at [repository URL; Zenodo DOI to be assigned upon acceptance]. The vault does not include full-text PDFs due to copyright restrictions; PDF extract text (first 25,000 characters per paper) is included.

2. **Study 2 benchmark taxonomy.** The benchmark meta-evaluation dataset (218 benchmarks x 96 features, including both deep-scored and automated-scored features) is available as Supplementary Data and archived at [repository URL; Zenodo DOI to be assigned upon acceptance].

3. **Study 3 trial transcripts.** The LLM trial response corpus (80 trial files containing 3,800 item-level responses across 10 models from 3 providers) is available at [repository URL; Zenodo DOI to be assigned upon acceptance]. Trial files include raw model outputs, reasoning traces, RLHF conflict self-reports, and engagement depth scores. Trial administration protocol details (API temperature, system prompt, item administration order, and API call dates) are documented in Supplementary Methods. Raw model outputs are available upon reasonable request.

4. **Gold standard validation dataset.** 700 paper-framework evaluation pairs with rater classifications (2 independent raters per pair, with third-rater adjudication for 23 disagreements; see Section 2.2.5 for inter-rater agreement details) are available at [repository URL; Zenodo DOI to be assigned upon acceptance].

5. **Author geography resolution data.** Country assignments for 2,300 papers, with strategy provenance, are included in the paper-level metadata (item 1 above).

All datasets will be deposited upon acceptance and assigned persistent DOIs. No restrictions on data access apply.


## Code Availability Statement

All analysis code is available at https://github.com/cjimmylin/cei-literature (archived at [Zenodo DOI to be assigned upon acceptance]). The repository includes:

- Keyword-based scoring pipeline (6 Python scripts, 7 stages): `classify_ethics.py`, `classify_ethics_perspective.py`, `classify_non_ethics_topics.py`, `classify_cultural_religious.py`, `classify_moral_psych.py`, `classify_data_nature.py`
- Non-Western framework scoring instruments (`cultural_global_scoring.py`)
- WEIRD score computation (`weird_scoring.py`)
- Gold standard validation analysis
- Author geography resolution pipeline
- Benchmark meta-evaluation (TOPSIS-ELECTRE III implementation)
- LLM trial administration protocols and analysis scripts
- Thematic coding codebook for RLHF conflict taxonomy
- Figure and table generation scripts

The pipeline runs on Python 3.9+ with dependencies: numpy, scipy, pandas, scikit-learn, matplotlib, and fpdf2. A `requirements.txt` and reproducibility instructions are provided.


## Ethics Statement

This study did not involve human participants, human biological samples, or animal subjects. Institutional Review Board (IRB) review was not required for the following reasons:

**Study 1 (Corpus Analysis)** analyzed published academic papers that are publicly available through open-access repositories and subscription databases. No individual-level data about human subjects were collected or analyzed; all data are at the paper level (metadata, scores, author institutional affiliations).

**Study 2 (Benchmark Meta-Evaluation)** analyzed published benchmark instruments using publicly available documentation. Benchmark items used in the feature taxonomy draw on published scholarly descriptions of existing instruments; no benchmarks were administered to human participants.

**Study 3 (LLM Self-Administration Trials)** administered benchmarks to large language models via API calls. Language models are not human subjects and do not fall under human subjects research protections. No human participants were involved in the trial administration or response generation. Benchmark items administered to models were drawn from published instruments and scholarly descriptions thereof.

The 12-member expert council (Supplementary S3) served as analytical perspectives providing disciplinary expertise, not as research participants. Council members reviewed methodological decisions, keyword lists, and manuscript drafts in their capacity as domain experts. Their contributions are analogous to peer review and editorial consultation, not human subjects participation. No data about council members' personal beliefs, behaviors, or characteristics were collected or analyzed.

This determination is consistent with the U.S. Common Rule (45 CFR 46), which excludes scholarly analysis of publicly available data and consultation with subject-matter experts from human subjects research requirements.


## Competing Interests Declaration

[Author(s)] declare(s) [no / the following] competing interests.

Disclosure: Study 3 utilized API access to models from Anthropic (Claude Opus 4.6, Sonnet 4.6, Haiku 4.5), OpenAI (GPT-5.4, GPT-5.4-Mini), and Google (Gemini 2.5/3.1 family). [If any author has an affiliation, funding relationship, or consulting arrangement with any of these providers, disclose here. If none: "The authors declare no competing interests."] The analysis code, trial protocols, and raw model outputs are publicly available (see Code Availability and Data Availability) to enable independent verification. The provenance tier analysis (Section 2.4.4) documents data quality limitations for each provider transparently.

[If applicable: This work was supported by [funding source]. The funder(s) had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.]


## Acknowledgments

We thank the 12 members of the interdisciplinary expert council (Supplementary S3) for their contributions to methodology design, keyword list development, benchmark evaluation, and manuscript review. Their tradition-specific expertise and commitment to anti-essentialization substantially improved the rigor and cultural sensitivity of this work.

[Acknowledge funding sources, institutional support, computational resources, and any individuals who contributed but do not meet authorship criteria.]

[If applicable: We acknowledge the use of Claude (Anthropic) as a research assistant for [specific tasks, e.g., literature search, data processing, code generation]. All analytical decisions, interpretations, and manuscript text were authored by the human researchers.]

This study was not pre-registered.


## Statistical Analysis Summary

All statistical analyses were performed in Python 3.9 using SciPy 1.11 (`scipy.stats`), scikit-learn 1.3 (`sklearn.cluster`, `sklearn.metrics`), NumPy 1.24, and pandas 2.0. [Verify exact versions against environment before submission.] Figures were generated using matplotlib 3.8. [Verify exact version.]

All tests were two-sided unless otherwise noted. Nonparametric tests were used throughout because normative framework scores are bounded, zero-inflated, and non-normal. No statistical method was used to predetermine sample size. The corpus size (n = 2,329) was determined by the contents of the CEI Literature Vault at the time of analysis; the benchmark count (n = 218) was determined by inclusion criteria; the model count (n = 10) was determined by API availability. This study was not pre-registered.

### Study 1 (Corpus Analysis)

| Test | Purpose | Implementation | Correction |
|------|---------|---------------|------------|
| Hierarchical clustering (Ward's method) | Regional clustering on Euclidean distances across 34 normative dimensions | `scipy.cluster.hierarchy` | Validated by k-means (k = 2--6) and silhouette analysis |
| Chi-square test of independence | Region x framework association | `scipy.stats.chi2_contingency` | -- |
| Mann-Whitney U tests | Pairwise framework comparisons across WEIRD tiers (two-sided) | `scipy.stats.mannwhitneyu` | Bonferroni correction for 34 comparisons per pair |
| Kruskal-Wallis H tests | Multi-group comparisons across Global North / South / Ambiguous | `scipy.stats.kruskal` | Post-hoc Dunn's tests corrected by Benjamini-Hochberg FDR (alpha = 0.05) |
| Correspondence analysis | Region-by-framework cross-tabulation; inertia decomposition | `prince.CA` or custom implementation [specify] | -- |
| Mann-Kendall trend tests | Temporal trends (WEIRD scores, regional diversity, non-Western engagement rates) | `pymannkendall` | Sen's slope estimator |
| Bootstrap resampling | 95% confidence intervals for key estimates | Custom (1,000 iterations, bias-corrected and accelerated [BCa]) | -- |
| Exact permutation tests | Sensitivity analyses for small cells (n < 20) | Custom | -- |
| Leave-one-out jackknife | Sensitivity analyses for small cells | Custom | -- |

### Study 2 (Benchmark Meta-Evaluation)

| Test | Purpose | Implementation | Correction |
|------|---------|---------------|------------|
| TOPSIS | Closeness coefficient computation for benchmark ranking | Custom (following Hwang & Yoon, 1981) | 8 weighted criteria via pairwise comparison |
| ELECTRE III | Concordance/discordance with veto thresholds | Custom (following Roy & Bouyssou, 1993) | Hard constraints on cultural scope |
| Kendall's W | Rank concordance across 6 weight schemes (W = 0.924) | `scipy.stats.kendalltau` or custom | -- |
| Inter-rater reliability | Divergence > 2 SD triggered Delphi resolution | Custom (modified Delphi across 3,072 feature-score pairs) | -- |

### Study 3 (LLM Self-Administration Trials)

| Test | Purpose | Implementation |
|------|---------|---------------|
| Descriptive statistics | Means, standard deviations, ratios across 10 models | `numpy`, `pandas` |
| Euclidean distance | Model-population proximity in moral foundations space | `scipy.spatial.distance` |
| Pairwise Pearson correlations | Cross-model agreement (within-provider and cross-provider) | `scipy.stats.pearsonr` |
| Cohen's kappa | Inter-rater agreement for thematic coding of RLHF conflicts | `sklearn.metrics.cohen_kappa_score` |
| RLHF conflict coding | Frequency counts across 703 self-reported conflicts in 7 categories | Thematic coding by [specify number of coders] with codebook (available in repository) |

### Effect Sizes

Effect sizes reported throughout: Cohen's d, rank-biserial correlation (equivalent to common language effect size), Cramer's V, epsilon-squared (for Kruskal-Wallis), and Cliff's delta (for pairwise ordinal comparisons). 95% confidence intervals are reported for primary effect size estimates.

### Thematic Coding Methodology

The RLHF conflict taxonomy (Section 5.4) was produced through thematic coding of 703 model self-reported conflicts. [Specify: single coder / dual coders with inter-rater reliability.] The codebook is available in the code repository. Categories were developed inductively from the trial data and refined through two rounds of coding. [If applicable: Inter-coder agreement was assessed using Cohen's kappa (kappa = [value]).]
