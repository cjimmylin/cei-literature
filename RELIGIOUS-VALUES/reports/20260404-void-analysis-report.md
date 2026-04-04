# Void Factor Taxonomy: Why Certain Traditions Lack AI Ethics Benchmarks

**Date:** 2026-04-04
**Traditions analyzed:** 14
**With gate-passing benchmarks:** 6
**Void (zero benchmarks):** 8

## Executive Summary

Of the 14 religious traditions tracked in the CEI Religious Values survey, 8 have zero viable benchmarks passing all three quality gates (religious depth, data availability, theological grounding). This report identifies the structural factors that explain this void.

## Structural Factor Definitions

Six factors were scored on a 0-5 scale for each tradition:

1. **Digital corpus availability** (0-5): Existence of machine-readable canonical texts
2. **NLP community size** (0-5): Size of the computational linguistics community for the tradition's languages
3. **Formalizability** (0-5): How amenable the tradition's ethics are to structured evaluation (rule-based > virtue-based > communal/place-based)
4. **Data sovereignty constraints** (0/0.5/1): Whether the community exercises restrictions on computational use of sacred knowledge
5. **Institutional support** (0-5): Funded research programs at the tradition-AI intersection
6. **Publication infrastructure** (0-5): Whether researchers publish in Semantic Scholar/ACL-indexed venues

**Benchmark Readiness Index** = factors 1+2+3 (max 15). Data sovereignty is excluded because it reflects community self-determination, not a deficit to be remedied.

## Tradition Scoreboard

| Tradition | Family | Benchmarks | Readiness | Corpus | NLP | Formal | Sov. | Instit. | Pub. | Total |
|-----------|--------|-----------|-----------|--------|-----|--------|------|---------|------|-------|
| Islam | Abrahamic | 28 | **15** | 5 | 5 | 5 | 0 | 5 | 5 | 25 |
| Christianity | Abrahamic | 6 | **13** | 5 | 4 | 4 | 0 | 3 | 3 | 19 |
| Judaism | Abrahamic | VOID | **12** | 4 | 3 | 5 | 0 | 3 | 2 | 17 |
| Hinduism | Dharmic | 4 | **10** | 4 | 3 | 3 | 0 | 2 | 2 | 14 |
| Buddhism | Dharmic | 6 | **10** | 4 | 3 | 3 | 0 | 2 | 2 | 14 |
| Confucianism | East Asian | 1 | **9** | 3 | 3 | 3 | 0 | 3 | 3 | 15 |
| Sikhism | Dharmic | 2 | **6** | 3 | 1 | 2 | 0 | 1 | 1 | 8 |
| Baha'i | Other | VOID | **6** | 3 | 0 | 3 | 0 | 0 | 0 | 6 |
| Taoism | East Asian | VOID | **5** | 3 | 1 | 1 | 0 | 0 | 0 | 5 |
| Shinto | East Asian | VOID | **5** | 2 | 2 | 1 | 0.5 | 1 | 1 | 7.5 |
| Jainism | Dharmic | VOID | **5** | 2 | 0 | 3 | 0 | 0 | 0 | 5 |
| Zoroastrianism | Other | VOID | **5** | 2 | 0 | 3 | 0 | 0 | 0 | 5 |
| Ubuntu Philosophy | African/Indigenous | VOID | **3** | 1 | 1 | 1 | 1 | 1 | 1 | 6 |
| Indigenous Spirituality | African/Indigenous | VOID | **0** | 0 | 0 | 0 | 1 | 0 | 0 | 1 |

## Readiness Tiers

**High readiness (index >= 10):** Islam, Christianity, Judaism, Hinduism, Buddhism
**Medium readiness (5-9):** Sikhism, Confucianism, Taoism, Shinto, Jainism, Zoroastrianism, Baha'i
**Low readiness (< 5):** Ubuntu Philosophy, Indigenous Spirituality

## Statistical Analysis

- Point-biserial r(has_benchmarks, readiness) = 0.660 (p = 0.0102)
- Pearson r(gate_passer_count, readiness) = 0.667 (p = 0.0091)
- Mean readiness of benchmark-bearing traditions: 10.5
- Mean readiness of void traditions: 5.1

### Factor-Level Correlations

| Factor | r(has_benchmarks) | p-value |
|--------|-------------------|---------|
| digital_corpus | 0.669 | 0.0089 * |
| nlp_community | 0.710 | 0.0044 * |
| formalizability | 0.414 | 0.1412 |
| institutional_support | 0.674 | 0.0083 * |
| publication_infrastructure | 0.740 | 0.0025 * |

## Why the Void Exists: Five Structural Barriers

### 1. Oral Tradition Barrier
Indigenous Spirituality and Ubuntu Philosophy transmit ethical knowledge through oral tradition, ceremony, and lived practice rather than written texts. This fundamentally resists the text-based paradigm of LLM evaluation. Indigenous readiness = 0; Ubuntu = 3.

### 2. NLP Infrastructure Gap
Even traditions with partial textual corpora (Jainism, Zoroastrianism, Baha'i) lack the computational linguistics infrastructure needed to build evaluation datasets. NLP community size shows the strongest individual correlation with benchmark existence.

### 3. Formalizability Asymmetry
Rule-based ethical systems (Islamic fiqh, Talmudic halakhah) are inherently more amenable to structured evaluation than place-based or communal ethics. Taoism's philosophical resistance to formalization (the Tao that can be told is not the eternal Tao) creates a genuine epistemological barrier to benchmarking.

### 4. Institutional Funding Concentration
Research funding flows disproportionately to Abrahamic traditions (especially Islam via Gulf state investment) and Chinese-language traditions (Confucianism via state interest in AI alignment). Traditions without institutional champions (Jainism, Zoroastrianism, Shinto) cannot sustain the multi-year effort needed for benchmark development.

### 5. Data Sovereignty as Active Resistance
For Indigenous and Ubuntu traditions, the absence of benchmarks is not merely a gap to be filled but may reflect deliberate resistance to computational extraction of sacred knowledge. This requires a fundamentally different approach: community-led evaluation frameworks rather than external benchmark construction.

## Implications for the Field

1. **The benchmark void is structurally determined**, not random. Traditions lacking benchmarks face compounding disadvantages across digital corpus, NLP infrastructure, and institutional support.

2. **No single factor is sufficient.** Jainism has moderate formalizability (3/5) but zero NLP infrastructure; Taoism has corpus availability (3/5) but resists formalization by design. Multiple barriers must be addressed simultaneously.

3. **Data sovereignty demands alternative paradigms.** For Indigenous and Ubuntu traditions, the solution is not to build conventional benchmarks but to develop community-controlled evaluation processes that respect epistemic sovereignty.

4. **The readiness index identifies tractable targets.** Sikhism (readiness=6), Jainism (5), and Zoroastrianism (5) have moderate readiness but zero gate-passers. These represent the most tractable gaps for future benchmark development.

## Methodological Notes

- Factor scores are expert-assigned based on literature review and NLP resource surveys
- Gate-passage counts are derived from the v2 feature matrix (401 candidates, 47 gate-passers)
- The benchmark readiness index deliberately excludes data sovereignty to avoid framing community self-determination as a deficit
- Small N (14 traditions) limits statistical power; correlations should be interpreted as descriptive rather than inferential
