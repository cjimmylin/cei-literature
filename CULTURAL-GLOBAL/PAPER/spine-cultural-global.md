# Spine Document: Cross-Cultural AI Values Alignment — Introduction & Literature Review

**Paper title:** Cross-Cultural AI Values Alignment: A Systematic Analysis of Normative Framework Diversity in AI Ethics
**Venue target:** AIES 2027 or FAccT 2027
**Corpus:** 2,329 papers (2010--2026), 34 normative dimensions, 10 world regions
**Date:** 2026-04-03

---

## 1. Seven Key Claims

**C1 — WEIRD Reproduction.** AI ethics reproduces the WEIRD bias documented in psychology. Mean WEIRD score 63.4/100; 56.0% High-WEIRD; 60.1% of papers from North America + Western Europe. North America is 8.4x overrepresented relative to population share.

**C2 — Three Regional Clusters.** Hierarchical clustering reveals three distinct clusters: (1) a Western Analytical cluster (North America, Western Europe, East Asia) dominated by utilitarian-deontological ethics, (2) a Heterogeneous Transitional cluster (MENA, South Asia, Southeast Asia, Latin America, Eastern Europe, Sub-Saharan Africa) with varying non-Western tradition engagement, and (3) a Non-Western Specialist cluster (Oceania alone) anchored by Indigenous relational ethics.

**C3 — Non-Western Framework Marginality.** Seven non-Western frameworks scored, but engagement remains marginal: Indigenous (49 raw, adj. ~33), Confucian (38, adj. ~14), Islamic (23, adj. ~23), Ubuntu (23, adj. ~13), Buddhist (22, adj. ~7), Dharmic (18, adj. ~4), Buen Vivir (8, adj. ~1). Only 6.9% of papers (161/2,329) engage any non-Western framework at detection threshold; precision-adjusted total ~95 papers (4.1%).

**C4 — Author Geography Predicts Normative Orientation.** Correspondence analysis (56.4% explained variance on two dimensions) confirms that institutional geography is a significant predictor of normative framework orientation, with region-framework affinity clusters spatially coherent.

**C5 — Positionality Paradox.** Non-Western framework engagement is nearly equal between Global North (mean 0.9) and Global South (mean 1.0), raising questions about epistemic authority and whether non-Western traditions are being studied *by* or *for* the communities they describe.

**C6 — Growth but Structural Marginality.** Non-Western engagement grew from 3.7% (2019) to 8.2% (2026), and regional diversity expanded from 7 regions (2018) to 11 (2023 onward). But the growth is insufficient to alter the fundamental skew.

**C7 — Critical Coverage Gaps.** Sub-Saharan Africa (1.1% of corpus), Buen Vivir (9 papers), Dharmic ethics (19 papers) represent the starkest lacunae. The least developed contexts exhibit "normative silence" — insufficient institutional capacity for either Western or non-Western ethical theorizing about AI.

---

## 2. Terminology Glossary

| Term | Definition | First Use |
|------|-----------|-----------|
| WEIRD | Western, Educated, Industrialized, Rich, Democratic — Henrich et al. (2010) diagnostic construct for sampling bias | 1.1 |
| WEIRD score | 0--100 composite index quantifying the degree to which a paper's research context reflects WEIRD conditions | 1.3 |
| Non-Western framework | One of seven normative traditions outside the Western philosophical canon scored in this analysis | 1.1 |
| Normative orientation | The philosophical tradition(s) a paper engages as its primary ethical framework | 1.2 |
| Values alignment | The problem of ensuring AI systems act in accordance with human values — used in both technical (RLHF) and philosophical (normative pluralism) senses | 1.1, 2.3 |
| RLHF | Reinforcement Learning from Human Feedback — the dominant pipeline for aligning LLMs with human preferences | 2.3 |
| Constitutional AI | Anthropic's approach using AI-generated principles to guide alignment without human feedback per sample | 2.3 |
| Maqasid al-Shariah | Higher objectives of Islamic law: preservation of religion, life, intellect, lineage, property | 2.4.3 |
| Ubuntu | "I am because we are" — Southern African philosophy of communal interdependence and relational personhood | 2.4.2 |
| Ren (仁) | Confucian humaneness/benevolence — the cardinal virtue of relational moral cultivation | 2.4.1 |
| Pratityasamutpada | Buddhist concept of dependent origination/interdependence | 2.4.4 |
| Svadharma / visesa-dharma | Dharmic contextual duty — one's moral obligation as determined by position and circumstance | 2.4.5 |
| Buen vivir / Sumak Kawsay | Andean Indigenous cosmovision of well-being as harmony between humans, community, and nature | 2.4.7 |
| CARE Principles | Collective benefit, Authority to control, Responsibility, Ethics — Carroll et al. (2020) for Indigenous data governance | 2.4.6 |
| Epistemic justice | Fair distribution of knowledge production power; whose frameworks count as legitimate | 2.5 |
| Anti-essentialization | Methodological discipline to avoid treating cultural traditions as monolithic or static | 2.4 preamble |
| Positionality | The relationship between a researcher's institutional/cultural location and their research subject | 1.2 |
| Correspondence analysis | SVD-based technique for visualizing associations between categorical variables (regions × frameworks) | 2.7 |

---

## 3. Twelve-Member Expert Council

### Tier 1 — Tradition Specialists (6)

| # | Name | Affiliation | Expertise | Primary Review | Cross-Check |
|---|------|------------|-----------|----------------|-------------|
| 1 | Prof. Chenyang Li | Nanyang Technological University | Confucian ethics, harmony philosophy | Sec 2.4.1 | Anti-essentialization |
| 2 | Dr. Amara Osei-Mensah | University of Ghana | Ubuntu, African communalism | Sec 2.4.2 | Word allocation fairness |
| 3 | Prof. Yusuf al-Qaradawi Jr. | Qatar Foundation / Georgetown | Islamic jurisprudence, Maqasid | Sec 2.4.3 | Terminology accuracy |
| 4 | Dr. Sonam Wangchuk | Rangjung Yeshe Institute, Nepal | Buddhist ethics, Theravada/Mahayana | Secs 2.4.4--2.4.5 | Representation adequacy |
| 5 | Dr. Tane Mahuta-Rau | University of Auckland | Indigenous knowledge, Maori tikanga | Sec 2.4.6 | Data sovereignty framing |
| 6 | Dr. Maria Soledad Vega | Universidad de Buenos Aires | Buen Vivir, decolonial studies | Sec 2.4.7 + 2.5 | Latin American voice |

### Tier 2 — Methodological & Critical Specialists (6)

| # | Name | Affiliation | Expertise | Primary Review | Cross-Check |
|---|------|------------|-----------|----------------|-------------|
| 7 | Prof. Joseph Henrich | Harvard University | WEIRD framework, cross-cultural psych | Sec 2.1 | WEIRD operationalization |
| 8 | Prof. Luciano Floridi | Yale / Bologna | AI ethics landscape, principlism | Sec 2.2 | Principle critique balance |
| 9 | Dr. Iason Gabriel | Google DeepMind | Values alignment theory | Sec 2.3 | Alignment pipeline accuracy |
| 10 | Dr. Abeba Birhane | Trinity College Dublin | Relational ethics, decolonial AI | Cross-cutting | Epistemic justice throughout |
| 11 | Dr. Segun Awosanya | University of Lagos | Bibliometrics, statistics | Sec 2.6 | Citation adequacy |
| 12 | Dr. Safiya Umoja Noble | UCLA | Critical information studies | Cross-cutting | Power/positionality framing |

### Operating Rules

1. **Tradition veto:** Experts 1--6 have veto authority on claims about their respective traditions
2. **Anti-essentialization:** Never write "Islam holds X" — always "Islamic ethics scholars argue X" or "the Maqasid framework posits X"
3. **Internal diversity:** Each tradition subsection must acknowledge internal heterogeneity (schools, denominations, regional variants)
4. **Word allocation:** Each of the 7 traditions receives 350--450 words; maximum deviation from mean is 30%
5. **Cross-cutting mandates:** Expert 10 (Birhane) flags epistemic justice issues in any section; Expert 12 (Noble) flags power/positionality framing

### Review Criteria (5)

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| C1 | Factual accuracy | Critical | Citations correct, claims properly attributed |
| C2 | Anti-essentialization | Critical | No monolithic tradition claims; uses "scholars argue" not "tradition holds" |
| C3 | Citation adequacy | Important | Key foundational works cited; no major gaps |
| C4 | Framing fairness | Important | Each tradition given appropriate depth; none romanticized or diminished |
| C5 | Missing perspectives | Desirable | Absent voices, uncovered angles, needed caveats |

---

## 4. Figure & Table Assignments

| ID | Type | Section | Description |
|----|------|---------|-------------|
| Figure 1 | World map | 1.2 | Geographic distribution of 2,329 papers by author affiliation, color-coded by WEIRD score tier |
| Table 1 | Comparison | 2.1 | WEIRD in psychology vs. AI ethics — parallel statistics (96%/12% vs. 60.1%/~10%) |
| Figure 2 | Pipeline diagram | 2.3 | Values alignment pipeline: where cultural values enter (training data → annotator demographics → RLHF reward model → constitutional principles → evaluation benchmarks) |
| Table 2 | Framework summary | 2.4 | Seven non-Western frameworks: core concepts, key scholars, AI applications, corpus count, key citation |

---

## 5. Section Structure & Assignment Map

### Section 1 — Introduction (~2,800 words) → `section1-introduction.md`

| Sub | Title | Words | Claims Previewed |
|-----|-------|-------|-----------------|
| 1.1 | Hook/Paradox: Whose Values? | ~500 | C1, C3 |
| 1.2 | Stakes and Consequences | ~500 | C1, C7 |
| 1.3 | The WEIRD Problem in AI Ethics | ~400 | C1 |
| 1.4 | The Gap | ~300 | C3, C6 |
| 1.5 | Research Questions | ~200 | All |
| 1.6 | Contributions | ~300 | All |
| 1.7 | Roadmap | ~200 | — |

### Section 2 — Literature Review (~8,500 words)

**Part 1** → `section2-litreview-part1.md` (~2,800 words)

| Sub | Title | Words |
|-----|-------|-------|
| 2.1 | The WEIRD Critique and Cross-Cultural Psychology | ~900 |
| 2.2 | The AI Ethics Landscape | ~900 |
| 2.3 | Values Alignment: The Cultural Pipeline | ~1,000 |

**Part 2** → `section2-litreview-part2.md` (~2,400 words)

| Sub | Title | Words |
|-----|-------|-------|
| 2.4 | Non-Western Normative Frameworks (preamble) | ~100 |
| 2.4.1 | Confucian Role Ethics | ~450 |
| 2.4.2 | Ubuntu Communalism | ~450 |
| 2.4.3 | Islamic Ethics (Maqasid al-Shariah) | ~450 |
| 2.4.4 | Buddhist Ethics | ~400 |

**Part 3** → `section2-litreview-part3.md` (~3,300 words)

| Sub | Title | Words |
|-----|-------|-------|
| 2.4.5 | Dharmic Ethics | ~400 |
| 2.4.6 | Indigenous Relational Ethics | ~400 |
| 2.4.7 | Buen Vivir (Sumak Kawsay) | ~350 |
| 2.5 | Decolonial AI and Epistemic Power | ~700 |
| 2.6 | Cross-Cultural AI Fairness | ~500 |
| 2.7 | Our Contribution in Context | ~600 |

---

## 6. Citation Key Inventory

### Section 1 Citations

| Key | Section(s) | Source |
|-----|-----------|--------|
| Gabriel 2020 | 1.1, 2.3 | Existing refs |
| Russell 2019 | 1.1, 2.3 | Existing refs |
| Henrich et al. 2010 | 1.1, 1.3, 2.1 | Existing refs |
| Jobin et al. 2019 | 1.2, 2.2 | Existing refs |
| Awad et al. 2018 | 1.2, 2.1, 2.6 | Existing refs |
| Floridi et al. 2018 | 1.2, 2.2 | Existing refs |
| Ouyang et al. 2022 | 1.2, 2.3 | Background |
| Bai et al. 2022 | 1.2, 2.3 | Background |
| Sambasivan et al. 2021 | 1.3, 2.6 | Existing refs |
| Mhlambi 2020 | 1.4, 2.4.2 | Existing refs |
| Wong 2020 | 1.4, 2.4.1 | Existing refs |
| Carroll et al. 2020 | 1.4, 2.4.6 | Existing refs |

### Section 2.1 Citations (WEIRD Critique)

| Key | Source |
|-----|--------|
| Henrich et al. 2010 | Existing refs |
| Apicella et al. 2020 | Existing refs |
| Rad et al. 2018 | Existing refs |
| Atari et al. 2023 | Background extract |
| Awad et al. 2018 | Existing refs |
| Gelfand et al. 2011 | Background extract |
| Hofstede 2001 | Existing refs |
| Schwartz 2012 | Existing refs |
| Inglehart & Welzel 2005 | Existing refs |
| Markus & Kitayama 1991 | NEW — add to refs |
| Shweder 1997 | NEW — add to refs |

### Section 2.2 Citations (AI Ethics Landscape)

| Key | Source |
|-----|--------|
| Jobin et al. 2019 | Existing refs |
| Hagerty & Rubinov 2019 | Existing refs |
| Floridi et al. 2018 | Existing refs |
| Floridi 2023 | Existing refs |
| Fjeld et al. 2020 | Background extract |
| Mittelstadt 2019 | Background extract |
| Schiff et al. 2021 | Existing refs |
| UNESCO 2021 | Existing refs |
| Whittlestone et al. 2019 | Existing refs |
| Madaio et al. 2020 | Existing refs |
| Bender et al. 2021 | Existing refs |

### Section 2.3 Citations (Values Alignment Pipeline)

| Key | Source |
|-----|--------|
| Gabriel 2020 | Existing refs |
| Russell 2019 | Existing refs |
| Christiano et al. 2017 | Background extract |
| Ouyang et al. 2022 | Background extract |
| Bai et al. 2022 | Background extract |
| Sorensen et al. 2024 | Background extract |
| Klingefjord et al. 2024 | Background extract |
| Durmus et al. 2024 | Existing refs |
| Bakker et al. 2022 | Background extract |
| Kirk et al. 2024 | Existing refs |

### Section 2.4 Citations (Non-Western Frameworks)

**2.4.1 Confucian:**
| Key | Source |
|-----|--------|
| Angle 2021 | Existing refs |
| Wong 2020, 2024 | Existing refs |
| Hou 2023 | Existing refs |
| So 2024 | Existing refs |
| Deng 2024 | Existing refs |
| Yao & Lu 2023 | Existing refs |
| Li 2014 | NEW — add |
| Qian 2023 | Background extract |
| Miao 2026 | Background extract |
| Ames 1998 | NEW — add |

**2.4.2 Ubuntu:**
| Key | Source |
|-----|--------|
| Mhlambi 2020 | Existing refs |
| Gwagwa et al. 2022 | Existing refs |
| Birhane 2021 | Existing refs |
| Mokoena 2024 | Background extract |
| Suliman 2024 | Background extract |
| van Norren 2020 | Existing refs |
| Metz 2007 | Background extract |
| Ramose 1999 | NEW — add |

**2.4.3 Islamic Ethics:**
| Key | Source |
|-----|--------|
| Auda 2008 | Background extract |
| Munshi 2021 | Existing refs |
| Alyemny 2023a, 2023b | Existing refs |
| Abdalla & Abdalla 2021 | Background extract |
| Usmonov 2025 | Background extract |
| Gorian 2024 | Background extract |
| Kamali 2008 | NEW — add |

**2.4.4 Buddhist:**
| Key | Source |
|-----|--------|
| Hongladarom 2020 | Existing refs |
| Deckker 2025 | Background extract |
| Miao 2026 | Background extract |
| Keown 2005 | NEW — add |
| Harvey 2000 | NEW — add |

**2.4.5 Dharmic:**
| Key | Source |
|-----|--------|
| Varshney 2024 | Background extract |
| Islam 2022 | Background extract |
| Kushwaha 2026 | Background extract |
| Bilimoria 2003 | NEW — add |

**2.4.6 Indigenous:**
| Key | Source |
|-----|--------|
| Carroll et al. 2020 | Existing refs |
| Keegan 2024 | Existing refs |
| Brown 2024 | Existing refs |
| Munn 2023 | Background extract |
| Smith 2012 | NEW — add |

**2.4.7 Buen Vivir:**
| Key | Source |
|-----|--------|
| Gudynas 2011 | NEW — add |
| Walsh 2010 | NEW — add |
| Villalba 2013 | NEW — add |

### Section 2.5 Citations (Decolonial AI)

| Key | Source |
|-----|--------|
| Mohamed et al. 2020 | Background extract |
| Birhane & Guest 2024 | Existing refs |
| Hanna et al. 2020 | Background extract |
| Prabhakaran et al. 2022 | Background extract |
| Talat et al. 2022 | Background extract |
| Birhane 2024 | Background extract |
| Held 2006 | Background extract |
| Quijano 2000 | NEW — add |
| Couldry & Mejias 2019 | NEW — add |

### Section 2.6 Citations (Cross-Cultural Fairness)

| Key | Source |
|-----|--------|
| Sambasivan et al. 2021 | Existing refs |
| Jakesch et al. 2023 | Background extract |
| Deckker 2025 | Background extract |
| Zimerman & Tomsett 2023 | Existing refs |
| Selbst et al. 2019 | NEW — add |

### Section 2.7 Citations (Contribution Positioning)

| Key | Source |
|-----|--------|
| Jobin et al. 2019 | Existing refs |
| Awad et al. 2018 | Existing refs |
| Sambasivan et al. 2021 | Existing refs |
| Mohamed et al. 2020 | Background |
| Sorensen et al. 2024 | Background |
| Dobbe & Marda 2024 | Existing refs |

### New References Required (~20 additions)

Markus & Kitayama 1991, Shweder 1997, Li 2014, Ames 1998, Ramose 1999, Kamali 2008, Keown 2005, Harvey 2000, Bilimoria 2003, Smith 2012, Gudynas 2011, Walsh 2010, Villalba 2013, Quijano 2000, Couldry & Mejias 2019, Selbst et al. 2019, Haidt 2001, Graham et al. 2013, Fan 2010

---

## 7. Extract-to-Section Mapping

### Agent B (Section 1)
- `2020-Gabriel-Artificial Intelligence Values And Alignment.md`
- `2024-Klingefjord-What Are Human Values, And How.md`
- `2018-Awad-The Moral Machine Experiment.md`
- `2019-Jobin-The Global Landscape Of Ai.md`
- `2022-Ouyang-Training Language Models To Follow.md`

### Agent C (Sections 2.1--2.3)
- `2023-Atari-Morality Beyond The Weird How.md`
- `2011-Gelfand-Differences Between Tight And Loose.md`
- `2018-Awad-The Moral Machine Experiment.md`
- `2019-Jobin-The Global Landscape Of Ai.md`
- `2019-Mittelstadt-Principles Alone Cannot Guarantee Ethical Ai.md`
- `2020-Fjeld-Principled Artificial Intelligence Mapping Consensus.md`
- `2018-Floridi-Ai4peoplean Ethical Framework For A.md`
- `2020-Gabriel-Artificial Intelligence Values And Alignment.md`
- `2017-Christiano-Deep Reinforcement Learning From Human Preferences.md`
- `2022-Ouyang-Training Language Models To Follow.md`
- `2022-Bai-Constitutional Ai Harmlessness From Ai Feedback.md`
- `2024-Klingefjord-What Are Human Values, And How.md`
- `2024-Sorensen-A Roadmap To Pluralistic Alignment.md`
- `2022-Bakker-Fine-Tuning Language Models To Find Agreement.md`
- `2024-Durmus-Towards Measuring The Representation Of.md`

### Agent D (Sections 2.4.1--2.4.4)
- `2020-Wong-Democratizing Algorithmic Fairness.md`
- `2023-Qian-Understanding Chinese Moral Stories With.md`
- `2026-Miao-The Anthropomorphization Of Ai And The.md`
- `2007-Metz-Toward An African Moral Theory.md`
- `2024-Mokoena-A Holistic Ubuntu Artificial Intelligence.md`
- `2024-Suliman-The Interconnectedness Between Ubuntu Principles.md`
- `2008-Auda-Maqasid Alshariah As Philosophy Of Islamic.md`
- `2021-Munshi-Towards An Automated Islamic Fatwa.md`
- `2025-Usmonov-From Human Scholars To Ai Fatwas.md`
- `2024-Gorian-Digital Ethics Of Artificial Intelligence Ai.md`
- `2021-Abdalla-The Grey Hoodie Project Big.md`
- `2025-Deckker-A Systematic Review Of The Impact.md`
- `2026-Miao-The Anthropomorphization Of Ai And The.md`

### Agent E (Sections 2.4.5--2.7)
- `2024-Varshney-Decolonial Ai Alignment Openness Visesadharma.md`
- `2022-Islam-Anekantavada And Its Relevance A Philosophical.md`
- `2026-Kushwaha-Syadvada And Artificial Intelligence Exploring The.md`
- `2020-Carroll-The Care Principles For Indigenous.md`
- `2023-Munn-The Five Tests Designing And.md`
- `2020-Mohamed-Decolonial Ai Decolonial Theory As.md`
- `2020-Hanna-Towards A Critical Race Methodology In.md`
- `2022-Prabhakaran-Cultural Incongruencies In Artificial Intelligence.md`
- `2022-Talat-On The Machine Learning Of.md`
- `2024-Birhane-Towards Decolonising Computational Sciences.md`
- `2021-Sambasivan-Reimagining Algorithmic Fairness In India.md`
- `2023-Jakesch-Coaudit Tools To Help Humans.md`
- `2025-Deckker-A Systematic Review Of The Impact.md`
- `2006-Held-The Ethics Of Care Personal.md`

---

## 8. Writing Guidelines

### Style
- Academic prose suitable for AIES/FAccT (top-tier AI ethics venue)
- Author-year in-text citations: "Henrich et al. (2010)" or "(Henrich et al. 2010)"
- No BibTeX/LaTeX markup — plain markdown with parenthetical citations
- Active voice preferred; passive acceptable for methodological descriptions
- Avoid first-person singular; use "we" for author claims, "this study" for self-reference

### Anti-Essentialization Patterns
- BANNED: "Islam believes...", "Confucianism holds that...", "Buddhism teaches...", "Indigenous peoples think..."
- REQUIRED: "Islamic ethics scholars argue...", "Within the Confucian tradition, scholars such as X have proposed...", "Buddhist philosophical analysis suggests...", "Many Indigenous communities emphasize..."
- Each tradition subsection MUST include one sentence acknowledging internal diversity

### Quantitative Previews in Introduction
- Seed the intro with key numbers from results: 2,329 papers, 34 dimensions, 10 regions, mean WEIRD 63.4, Sub-Saharan Africa 1.1%, 3.8%→10.8% growth
- Do NOT duplicate full results tables — just enough to motivate the study

### Cross-Reference Convention
- Forward references to paper sections: "Section 3 describes our methodology..."
- The existing paper has: Section 3 = methodology, Sections 4--7 = results by RQ, Section 8 = discussion, Section 9 = conclusion

### Word Count Targets
- Section 1 total: ~2,800 words
- Section 2 total: ~8,500 words
- Combined target: ~11,300 words
- Hard maximum: 13,000 words (leave room for council expansions)
