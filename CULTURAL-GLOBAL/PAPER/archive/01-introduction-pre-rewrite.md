# 1. Introduction

Artificial intelligence systems are increasingly deployed across cultures, languages, and legal systems that embody fundamentally different conceptions of the good. Yet the research enterprise that seeks to align these systems with human values operates under a largely unexamined assumption: that the normative frameworks guiding alignment are, or should be, universal. When AI safety researchers invoke "human values," they typically mean values legible within the Western philosophical canon---utilitarian welfare maximization, deontological rights and duties, or virtue-theoretic accounts of flourishing. The question of whose values, and from which philosophical traditions, remains undertheorized in AI ethics scholarship at scale.

This silence has material consequences. AI governance frameworks developed primarily by researchers at institutions in North America and Western Europe are exported to regulatory environments in Sub-Saharan Africa, Southeast Asia, and Latin America, where they encounter normative traditions---Ubuntu communalism, Confucian role ethics, Islamic jurisprudence, Indigenous relational ontologies---that organize moral reasoning along different axes entirely. If the academic literature that informs these governance frameworks is itself culturally skewed, then the entire alignment enterprise risks encoding a particular cultural perspective as a universal standard.

## 1.1 The WEIRD Problem in AI Ethics

The parallel to cross-cultural psychology is instructive. In their landmark study, Henrich, Heine, and Norenzayan (2010) demonstrated that research participants from WEIRD (Western, Educated, Industrialized, Rich, and Democratic) societies are among the least representative populations from which to draw generalizations about human cognition, perception, and moral reasoning. Their analysis revealed that findings in domains ranging from visual perception to fairness intuitions to cooperation norms varied dramatically across cultural contexts, yet the overwhelming majority of published psychology relied exclusively on WEIRD samples.

More than fifteen years later, similar questions must be asked of AI ethics. Jobin, Ienca, and Vayena (2019) surveyed 84 AI ethics guidelines and found convergence around five principles---transparency, justice, non-maleficence, responsibility, and privacy---but noted that these principles "ichever the Western liberal tradition." Hagerty and Rubinov (2019) analyzed global AI policy documents and found that non-Western normative concepts were largely absent. Sambasivan et al. (2021) documented how "fairness" itself is culturally contingent, with notions of caste-based discrimination in India mapping poorly onto the race-based categories dominant in U.S. AI fairness research.

Yet no study has systematically measured the cultural distribution of normative frameworks across a large corpus of AI ethics scholarship. Individual case studies have documented the relevance of Ubuntu philosophy to African AI governance (Mhlambi 2020; Gwagwa et al. 2022), Confucian role ethics to East Asian AI design (Angle 2021; Wong 2020; Hou 2023), and Indigenous data sovereignty principles to algorithmic governance in Oceania (Carroll et al. 2020; Keegan 2024). What is missing is a bird's-eye view: across thousands of papers, how is the global landscape of AI values alignment research actually distributed?

## 1.2 Research Questions

This study addresses five research questions:

**RQ1 (Regional Clusters).** Do distinct regional clusters of AI values alignment approaches emerge from the literature, and how do they map onto WEIRD/non-WEIRD, Global North/South, and East/West frameworks?

**RQ2 (Normative Frameworks).** Which normative ethical frameworks---both Western and non-Western---are most associated with which regional and cultural contexts?

**RQ3 (Author Geography).** To what extent does author institutional geography predict the normative framework orientation of AI ethics research?

**RQ4 (Positionality).** What is the positionality distribution of cross-cultural AI ethics research---who studies whom?

**RQ5 (Coverage Gaps).** What are the critical gaps in the global coverage of AI values alignment research, and what do they reveal about epistemic power dynamics in the field?

## 1.3 Contributions

This paper makes four contributions to the literature on AI ethics and values alignment:

1. **Empirical scale.** We present the first systematic cross-cultural analysis of normative framework engagement across 2,046 AI ethics papers, spanning 10 world regions and 34 scoring dimensions. This is, to our knowledge, the largest such analysis conducted.

2. **WEIRD operationalization for AI ethics.** We adapt Henrich et al.'s (2010) WEIRD construct to the AI ethics domain, creating a five-dimensional composite score (0--100) that quantifies the degree to which each paper's research context is characterized by Western, Educated, Industrialized, Rich, and Democratic conditions.

3. **Non-Western framework taxonomy.** We develop and validate scoring instruments for seven non-Western normative frameworks (Confucian, Ubuntu, Islamic jurisprudence, Buddhist, Dharmic, Indigenous relational, and Buen vivir) with keyword lists designed by tradition-specific experts.

4. **Coverage gap identification.** We identify specific geographic and philosophical lacunae---particularly in Sub-Saharan Africa (1.1% of corpus), Latin America (4.4%), Buen vivir (6 papers), and Dharmic ethics (9 papers)---and provide actionable recommendations for the research community.

The remainder of this paper is organized as follows. Section 2 reviews the WEIRD critique in psychology and its relevance to AI ethics, surveys non-Western normative traditions, and positions our work relative to existing cross-cultural AI ethics scholarship. Section 3 describes our methodology, including data sources, scoring instruments, analytical layers, and the expert council. Sections 4--7 present results organized by research question. Section 8 discusses implications for AI alignment and policy. Section 9 concludes.
