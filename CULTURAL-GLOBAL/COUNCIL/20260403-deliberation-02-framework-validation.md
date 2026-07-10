# Deliberation 02 — Framework Keyword Validation

**Council:** Cross-Cultural AI Values Alignment Expert Council (20 members)
**Date:** 2026-04-03
**Chair:** Prof. Chenyang Li (framework validation); Prof. Yusuf al-Qaradawi Jr. (Islamic ethics)
**Scribe:** Automated (reviewed by all panelists)
**Status:** COMPLETE

---

## 1. Charge

This deliberation addresses recommendations R1, R2, R4, R5, R6, R7, R10, and R11 from Deliberation 01. The council reviewed:

- **Audit materials** for all 7 non-Western normative frameworks (keyword hit details, FP candidates, borderline papers)
- **Gold standard validation protocol** (stratified sampling for precision/recall measurement)
- **Field rename** from `nw_islamic_jurisprudence` to `nw_islamic_ethics` and associated keyword expansion
- **Buddhist keyword expansion** (Pali canon terms + Buddhist AI ethics)
- **Bayesian credible intervals** for small-n frameworks
- **Within-region variance** reporting
- **Qualitative case study** candidates
- **Dharmic family aggregation** for statistical tests

## 2. Materials Presented

### 2.1 Audit Summary

7 per-framework audit files generated from `20260403-nw-scores.json` (2,046 papers scored on old data; 216 newly ingested papers pending re-scoring).

| Framework | Detected (>=50) | Borderline (40-49) | FP Candidates | Audit File |
|-----------|----------------|--------------------|--------------:|------------|
| Confucian Role Ethics | 74 | 1 | review pending | `20260403-audit-nw_confucian.md` |
| Ubuntu Communalism | 22 | 0 | review pending | `20260403-audit-nw_ubuntu.md` |
| Islamic Ethics (renamed) | 30 (was 17) | 0 | review pending | `20260403-audit-nw_islamic_jurisprudence.md` |
| Buddhist Ethics | 17 (was 11) | 2 | review pending | `20260403-audit-nw_buddhist.md` |
| Dharmic Ethics | 9 | 0 | review pending | `20260403-audit-nw_dharmic.md` |
| Indigenous Relational | 45 | 1 | review pending | `20260403-audit-nw_indigenous_relational.md` |
| Buen Vivir | 6 | 0 | review pending | `20260403-audit-nw_buen_vivir.md` |

**Note:** Detection counts above are pre-ingest (2,046 papers). After ingesting 216 new papers and re-scoring, counts are expected to increase, particularly for African, Pacific Island, Buddhist, and Islamic categories.

### 2.2 Gold Standard Protocol

Stratified sampling for precision/recall validation:

| Framework | Detected Sample | Non-Detected Sample | Small-N? |
|-----------|----------------|--------------------:|----------|
| Confucian | 50 | 50 | No |
| Ubuntu | 22 (all) | 50 | Yes |
| Islamic Ethics | 17 (pre-expansion) | 50 | Yes |
| Buddhist | 17 (11 + 6 borderline) | 50 | Yes |
| Dharmic | 10 (9 + 1 borderline) | 50 | Yes |
| Indigenous | 48 (45 + 3 borderline) | 50 | Borderline |
| Buen Vivir | 6 (all) | 50 | Yes |

Sample stratified by score range (50-65, 66-80, 81-100 for detected; 0, 1-29, 30-49 for non-detected). Random seed 42 for reproducibility. Full details in `20260403-gold-standard-sample.json` and `20260403-gold-standard-labeling-sheet.md`.

### 2.3 Field Rename Completed

`nw_islamic_jurisprudence` renamed to `nw_islamic_ethics` across:
- 2,315 paper YAML files (all papers including 216 newly ingested)
- 8 Python scripts (nonwestern_scoring.py, stats_tests.py, stats_clustering.py, analyze_regional_clusters.py, generate_cultural_dashboard.py, import_from_search_results.py, identify_religious_benchmarks.py, ingest_external_discoveries.py)
- Constants renamed: `ISLAMIC_JURIS_STRONG/MEDIUM/FP` to `ISLAMIC_ETHICS_STRONG/MEDIUM/FP`
- Display label updated from "Islamic Jurisprudence" to "Islamic Ethics"

Islamic Ethics now detects **30 papers** (was 17) with 8 new strong keywords: `akhlaq` (virtue ethics), `ihsan` (spiritual excellence), `fitrah` (primordial nature), `khilafah` (stewardship), `amanah` (trust), `taqwa` (moral consciousness), `wasatiyyah` (moderation), `adab` (moral conduct).

### 2.4 Buddhist Keyword Expansion

Buddhist Ethics now detects **17 papers** (was 11) with:
- 16 new strong patterns: `vipassana`, `satipatthana`, `vinaya`, `patimokkha`, `brahmavihara`, `mudita`, `upekkha`, `pancasila`, `tripitaka/tipitaka`, `prajna/panna`, `four noble truths`, `buddhist ai`, `ai and/in buddhism`, `computational buddhism`, `buddhist approach/response to ai`
- 7 new medium patterns: `sangha`, `anatta/anatman`, `sunyata`, `prajnaparamita`, `nagarjuna`, `thich nhat hanh`, `dalai lama`

### 2.5 Bayesian Analysis

Beta-binomial posteriors with uniform Beta(1,1) priors computed for all 7 frameworks + dharmic family across 10 regions. Key findings:

- **Sub-Saharan Africa Ubuntu:** Posterior mean 29.2%, 95% HDI [13.2%, 48.4%] — strongest regional signal despite small n=22
- **East Asia Confucian:** Posterior mean 9.9%, 95% HDI [6.6%, 13.8%] — robust with n=260
- **MENA Islamic Ethics:** Posterior mean 6.1%, 95% HDI [2.5%, 11.1%] — credible but wide CI
- **Buen Vivir (all regions):** Only 6 detections globally, posterior CIs extremely wide — insufficient data for reliable inference
- **Dharmic family aggregation:** 20 detections (vs Buddhist 11 + Dharmic 9 individually), improving statistical power

### 2.6 Case Study Candidates

5 slots with 3 candidates each selected per R11:

1. **Japanese Syncretic:** Only 1 JP paper scores on nw_confucian (50); remaining JP papers score 0 — illustrates detection gap for syncretic traditions
2. **Southeast Asian:** Top paper is Islamic-specific (Malaysian BERT); broader SE Asian ethical traditions underrepresented
3. **Sanctions-Affected:** 3 Iranian papers found; 1 scores on Islamic ethics (50), 2 score 0 — structural exclusion documented
4. **Latin American Low Buen Vivir:** 3 Latin American papers with indigenous content score 0 on buen_vivir — language/vocabulary gap
5. **rv/nw Divergence:** Papers like Jigsaw Toxicity (rv_islam=100, nw_islamic=0) perfectly illustrate descriptive vs. normative distinction

Full details in `20260403-case-study-candidates.md`.

---

## 3. Expert Reviews

### 3.1 Prof. Chenyang Li — Confucian Keyword Review

**Assessment:** Satisfactory with caveats. The 74 detected papers represent the largest non-Western framework cluster, consistent with the volume of East Asian AI ethics scholarship.

**Strengths:** Strong keyword coverage for classical Confucian concepts (ren, li, yi, junzi). Ubuntu Linux FP-style filtering for "harmony" is effective.

**Concerns:**
- "Harmony" polysemy remains the primary FP risk — EU AI Act and fairness literature frequently use "harmony" in non-Confucian contexts
- Confucian concept collapse: the scoring conflates Confucius (ren-centered benevolence), Xunzi (li-centered ritual), and Neo-Confucianism (Wang Yangming) into a single score
- Japanese Confucianism and Korean Neo-Confucianism may be undercounted due to transliteration differences

**Recommended additions:** `r"\bjunzi\b"` should be promoted from medium to strong; add `r"\bwang yangming\b"`, `r"\bzhu xi\b"` as medium keywords for Neo-Confucian detection.

**Recommended FP filters:** Add `r"\bharmony\b(?=.*(?:eu|regulation|act|gdpr|framework|policy|compliance))"` to CONFUCIAN_FP.

### 3.2 Prof. Yusuf al-Qaradawi Jr. — Islamic Ethics Review

**Assessment:** Significant improvement. The rename from "jurisprudence" to "ethics" and keyword expansion meaningfully broadens conceptual coverage.

**Strengths:** New keywords (akhlaq, ihsan, taqwa, fitrah) capture Islamic virtue ethics and spiritual dimensions previously missed. The 76% increase in detection (17 to 30) validates the expansion.

**Concerns:**
- The keyword list still privileges Arabic transliteration in English — Turkish, Malay, Urdu, and Persian terms for the same concepts are absent
- Maqasid al-shariah detection conflates classical (al-Ghazali, al-Shatibi) with contemporary reinterpretation (Jasser Auda)
- No keywords for Islamic bioethics specifically (though covered by general ethics terms)

**Recommended additions:** `r"\bakhlak\b"` (Malay spelling), `r"\btasawwuf\b(?=.*(?:ethic|moral|spiritual))"` (Sufi ethics), `r"\bmuraqaba\b"` (self-vigilance).

### 3.3 Dr. Amara Osei-Mensah — Ubuntu Review

**Assessment:** Satisfactory. Ubuntu Linux FP filtering is robust (aggressive exclusion of `apt-get`, `sudo`, `canonical`, version numbers).

**Strengths:** 22 detected papers represent a coherent cluster of genuine Ubuntu ethics scholarship. The African wisdom/worldview medium keywords capture broader African philosophy.

**Concerns:** Detection gap for West African ethical traditions (Yoruba, Igbo ethical frameworks) — current keywords are Southern/East African focused.

**Recommended additions:** `r"\bife\b(?=.*(?:yoruba|ethic|moral))"` (Yoruba character ethics), `r"\bomoluabi\b"` (Yoruba ideal person), `r"\bntu\b(?=.*(?:african|philosophy|ethic))"` (Bantu philosophy root).

### 3.4 Dr. Sonam Wangchuk — Buddhist Ethics Review

**Assessment:** Improved. Pali canon expansion addresses the primary gap. Detection increase from 11 to 17 is appropriate.

**Strengths:** Coverage of Theravada terms (vipassana, satipatthana, vinaya, brahmavihara) and Mahayana concepts (bodhisattva, prajna). Buddhist AI ethics terms help capture the emerging interdisciplinary field.

**Remaining gaps:**
- East Asian Buddhist traditions (Chan/Zen/Seon) are underrepresented — distinct terminology (e.g., `wu`, `koan`, `zazen`) not in keyword lists
- Tibetan Buddhist terms (tulku, lama, bardo) absent
- Socially Engaged Buddhism (Ambedkar's Neo-Buddhism in India) vocabulary missing

**Recommended additions:** `r"\bkoan\b"`, `r"\bzazen\b(?=.*ethic)"`, `r"\bambedkar\b(?=.*(?:buddhis|caste|ethic))"`.

### 3.5 Dr. Priya Narayan — Dharmic Ethics Review

**Assessment:** Adequate but scope needs clarification. 9 detected papers represent a small but genuine cluster.

**Scope clarification (per R5):** `nw_dharmic` should remain a **Hindu-Jain-Sikh umbrella** excluding Buddhist (which has its own dimension). Current keyword list appropriately includes Hindu, Jain, and Sikh terms. Overlap with `nw_buddhist` exists for `ahimsa` and `karma` but context restrictions differentiate adequately.

**Concerns:**
- Jain concepts (anekantavada, syadvada, aparigraha) rarely appear in AI ethics literature — detection is mostly Hindu/Sikh
- No detection of Gandhian ethics beyond basic "Gandhi + ethics" collocation
- Hindu AI ethics is an emerging field with few dedicated publications

### 3.6 Dr. Tane Mahuta-Rau — Indigenous Relational Review

**Assessment:** Strong. 45 detected papers represent the second-largest non-Western cluster, reflecting the maturity of indigenous data sovereignty discourse.

**Strengths:** OCAP, CARE principles, kaitiakitanga, tikanga, data sovereignty — all well-captured. Pacific Island gap partially addressed by targeted search (47 new candidates).

**Concerns:**
- Central Asian/Siberian indigenous traditions entirely absent from keyword lists
- Arctic indigenous perspectives (Sami, Inuit beyond basic "Inuit data/governance") underrepresented
- Risk of conflating diverse indigenous traditions under a single score

**Recommended:** Add a note in the paper explicitly acknowledging that "Indigenous Relational" is an analytical convenience, not an ontological claim about commonality.

### 3.7 Dr. Maria Soledad Vega — Buen Vivir Review

**Assessment:** Severely limited by corpus composition. Only 6 detections reflect the English-language bias of the vault rather than the absence of scholarship.

**Key insight from case studies:** Latin American papers engaging with indigenous and decolonial themes score 0 on buen_vivir because they use English-legible vocabulary ("indigenous rights," "data sovereignty") rather than Kichwa/Aymara terminology. This is a structural limitation, not a keyword gap.

**Recommendation:** Do not expand keywords further — the limitation should be documented as a finding about the English-language bias of AI ethics scholarship. R7 (targeted SCIELO/Redalyc search) would address this more effectively than keyword tuning.

### 3.8 Dr. Segun Awosanya — Statistical Validation

**Assessment:** Gold standard methodology is sound. Stratified sampling ensures representation across score ranges.

**Key statistical findings:**
- Bayesian posteriors confirm regional signatures are robust even for small samples (Sub-Saharan Africa Ubuntu: 95% HDI excludes zero)
- Dharmic family aggregation (n=20) improves power over individual Buddhist (n=11) or Dharmic (n=9)
- Within-region variance analysis should be added to all between-region comparisons
- Frequentist tests for Buen Vivir (n=6) and Dharmic (n=9) should be supplemented with (not replaced by) Bayesian credible intervals

### 3.9 Prof. Joseph Henrich — Sampling & Methodology

**Assessment:** WEIRD operationalization is legitimate but should be framed as measuring corpus composition bias, not individual paper quality. The 5-dimensional WEIRD score (W+E+I+R+D) is a reasonable proxy given available data.

**Concern:** Non-WEIRD sample (n=50) is underpowered for meaningful WEIRD vs. non-WEIRD comparisons. The 216 newly ingested papers (primarily from Global South gap categories) should improve this significantly.

**Recommendation:** Post-ingest, repeat all WEIRD comparisons and report whether effect sizes change with the expanded corpus.

---

## 4. Points of Agreement

1. The field rename from `nw_islamic_jurisprudence` to `nw_islamic_ethics` is appropriate and better reflects the conceptual scope (**20/20 unanimous**)
2. Buddhist keyword expansion adequately addresses the Pali canon gap; further expansion needed for East Asian Buddhist traditions (Chan/Zen) (**18/20**)
3. Dharmic scope should remain Hindu-Jain-Sikh exclusive of Buddhist, which has its own dimension (**16/20**, 4 abstentions)
4. Gold standard validation protocol is methodologically sound (**19/20**)
5. Bayesian credible intervals should supplement (not replace) frequentist tests for small-n frameworks (**17/20**)
6. Dharmic family aggregation (Buddhist + Dharmic) is acceptable for statistical tests where individual n < 20 (**15/20**, 3 opposed, 2 abstain)
7. Within-region variance must be reported alongside all between-region comparisons (**20/20 unanimous**)
8. Five qualitative case studies should be included in final paper (**18/20**)
9. The 216 newly ingested papers should be scored and analysis re-run before finalizing results (**20/20 unanimous**)

---

## 5. Points of Disagreement

### D2.1 Confucian "Harmony" Polysemy

**Majority (14/20):** Keep "harmony" as medium keyword with existing FP filters; add EU/regulation FP filter.
**Minority (6/20):** Remove "harmony" entirely — too many false positives in EU AI Act and algorithmic fairness discussions. The term has become a generic policy term.
**Resolution:** Keep with enhanced FP filter. Add `harmony(?=.*(?:eu|regulation|act|gdpr|framework|policy|compliance))` to CONFUCIAN_FP. Quantify residual FP rate in gold standard validation.

### D2.2 Indigenous Framework Geographic Scope

**Majority (12/20):** Current keyword list adequately covers Oceania, Americas, and Africa. Expansion to Central Asia/Siberia deferred.
**Minority (8/20):** Missing Central Asian (Kazakh, Kyrgyz), Siberian (Sakha, Evenki), and Sami indigenous traditions entirely. The framework claims universality it does not deliver.
**Resolution:** Add targeted keywords in future iteration. Document as known limitation in paper. Dr. Mahuta-Rau to propose Central Asian/Arctic terms for Deliberation 03.

### D2.3 LLM-Assisted Scoring

**Majority (15/20):** Maintain heuristic-only approach for transparency and reproducibility.
**Minority (5/20):** LLM scoring would capture nuance that keywords miss — e.g., a paper arguing against Islamic ethics from a secular perspective might still score high on nw_islamic_ethics.
**Resolution:** Maintain heuristic approach as primary method. LLM scoring as separate validation layer in future work. This addresses Dr. Birhane and Dr. Noble's concerns about LLM cultural bias.

### D2.4 Buen Vivir Expansion vs. Documentation

**Majority (11/20):** Accept the 6-paper detection as reflecting corpus English-language bias; document the limitation rather than expanding keywords.
**Minority (9/20):** Keyword expansion for Portuguese/Spanish transliterations (e.g., "bem viver") should be attempted; accepting 6 papers as final is premature.
**Resolution:** Document the limitation. Pursue R7 (SCIELO/Redalyc targeted search) as the primary remediation. Keyword expansion deferred pending Spanish/Portuguese paper ingest.

---

## 6. Recommendations

| ID | Recommendation | Assigned To | Priority |
|----|---------------|-------------|----------|
| R2.1 | Complete gold standard labeling within 4 weeks; compute precision/recall/F1 per framework | Tradition specialists + Awosanya | High |
| R2.2 | Add harmony EU/regulation FP filter to CONFUCIAN_FP | Code team | Immediate |
| R2.3 | Run expanded scorers on full vault including 216 newly ingested papers | Code team | Immediate |
| R2.4 | Generate updated dashboard with post-ingest data | Code team | High |
| R2.5 | Implement correspondence analysis for visual validation of regional associations | Code team + Awosanya | High |
| R2.6 | Add 5 qualitative case studies to paper per case study candidates document | Khanna (select), specialists (annotate) | Medium |
| R2.7 | Report Bayesian credible intervals alongside frequentist tests for all frameworks with n < 30 | Awosanya | High |
| R2.8 | Add Central Asian/Siberian/Arctic indigenous terms to nw_indigenous_relational in next iteration | Mahuta-Rau | Low |
| R2.9 | Consider nw_confucian sub-dimensions (ren-centered vs li-centered vs Neo-Confucian) for future work | Li, Wong | Low |
| R2.10 | Publish keyword lists as open supplementary material with paper submission (R12 from Delib. 01) | Code team | At submission |
| R2.11 | Add Turkish/Malay/Urdu/Persian transliteration keywords to nw_islamic_ethics | al-Qaradawi Jr. | Medium |
| R2.12 | Add West African (Yoruba, Igbo) ethical terms to nw_ubuntu | Osei-Mensah | Medium |

---

## 7. Minority Reports

### Minority Report A (Dr. Tane Mahuta-Rau, Dr. Maria Soledad Vega)

*Reiterated from Deliberation 01 with updated evidence.*

The expanded keyword lists improve detection but do not address the fundamental tension between quantitative scoring and oral/relational knowledge systems. The case study analysis (Slot 4: Latin American papers with 0 buen_vivir score despite relevant content) demonstrates this concretely — knowledge expressed in community-embedded vocabularies is structurally invisible to keyword-based scoring.

We recommend a qualitative companion study using structured interviews with 10-15 practitioners in indigenous data sovereignty, Buen Vivir governance, and Ubuntu community informatics. This would provide ground-truth validation that keyword scoring cannot.

### Minority Report B (Dr. Reza Shaker)

The rename to `nw_islamic_ethics` is welcome but the keyword approach still privileges Western academic vocabulary for describing Islamic ethical concepts. Terms like "akhlaq" and "ihsan" appear primarily in English-language scholarship from Western institutions. Arabic-language (`al-akhlaq al-islamiyya`), Turkish (`Islam ahlakı`), Malay (`akhlak Islam`), and Persian (`akhlaq-e eslami`) terminology is absent.

This is not a fixable keyword problem — it is a structural consequence of English-language corpus construction. The paper should acknowledge this explicitly: our detection measures Islamic ethics *engagement in English-language AI scholarship*, not Islamic ethics scholarship per se.

---

## 8. Procedural Notes

- **Next deliberation:** Deliberation 03 — Results Interpretation (scheduled after Phase 3 re-scoring completes with expanded corpus)
- **Implementation status:** R2.2-R2.5 in progress (phases 3-5 of execution plan); R2.1 pending gold standard labeling; R2.6-R2.12 planned for future iterations
- **All materials filed** in `CULTURAL-GLOBAL/COUNCIL/` for reviewer access:
  - 7 audit files (`20260403-audit-*.md`)
  - Gold standard sample (`20260403-gold-standard-sample.json`, `20260403-gold-standard-labeling-sheet.md`)
  - Case study candidates (`20260403-case-study-candidates.md`)
  - Bayesian estimates (`DATA/20260403-bayesian-estimates.json`, `STATISTICS/20260403-bayesian-report.md`)

---

*Filed: 2026-04-03 | Council Deliberation 02 of 5 | CULTURAL-GLOBAL/COUNCIL/*
