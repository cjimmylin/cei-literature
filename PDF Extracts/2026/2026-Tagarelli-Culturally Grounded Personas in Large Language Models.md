---
title: "2026-Tagarelli-Culturally Grounded Personas in Large Language Models - PDF Extract"
source_pdf: "2026-Tagarelli-Culturally Grounded Personas in Large Language Models.pdf"
pages: 27
extracted_at: "2026-02-15T17:54:29.933243"
---

# PDF Extract: 2026-Tagarelli-Culturally Grounded Personas in Large Language Models

**Source PDF:** 2026-Tagarelli-Culturally Grounded Personas in Large Language Models.pdf
**Total Pages:** 27

---

## Content

```
--- Page 1 ---

Culturally Grounded Personas in Large Language Models:
Characterization and Alignment with
Socio-Psychological Value Frameworks
Candida M. Greco, Lucio La Cava, Andrea Tagarelli
DIMES Dept., University of Calabria, Italy
{candida.greco, lucio.lacava, tagarelli}@dimes.unical.it
Abstract
Despite the growing utility of Large Language Models (LLMs) for simulating human behavior,
the extent to which these synthetic personas accurately reﬂect world and moral value systems
across different cultural conditionings remains uncertain. This paper investigates the alignment
of synthetic, culturally-grounded personas with established frameworks, speciﬁcally the World
Values Survey (WVS), the Inglehart–Welzel Cultural Map, and Moral Foundations Theory. We
conceptualize and produce LLM-generated personas based on a set of interpretable WVS-derived
variables, and we examine the generated personas through three complementary lenses: positioning
on the Inglehart–Welzel map, which unveils their interpretation reﬂecting stable differences across
cultural conditionings; demographic-level consistency with the World Values Survey, where response
distributions broadly track human group patterns; and moral proﬁles derived from a Moral Foundations
questionnaire, which we analyze through a culture-to-morality mapping to characterize how moral
responses vary across different cultural conﬁgurations. Our approach of culturally-grounded persona
generation and analysis enables evaluation of cross-cultural structure and moral variation.
1
Introduction
Large Language Models (LLMs) are increasingly used to generate and think about human personas,
preferences, and behaviors. However, there is limited understanding about how well such generated
personas reﬂect empirically grounded cultural, demographic, and moral value structures, or how their
representations may systematically vary across societies.
In this work, we investigate the extent to which LLM-generated culturally-grounded persona proﬁles
align with established socio-psychological frameworks, including the World Values Survey (WVS), the
Inglehart–Welzel Cultural Map, and Moral Foundations Theory. More speciﬁcally, our study aims to
address the following research questions:
• RQ1: How are synthetically generated culturally-grounded personas positioned along the principal
dimensions of cross-cultural variation?
• RQ2: Can an LLM mimicking a culturally-grounded persona have a WVS cultural proﬁle that aligns
with that of human demographic groups?
• RQ3: How are the WVS-derived cultural variables mapped to the moral foundations? And how do
the culturally-grounded personas map onto scores of moral foundations questionnaire administered to a
culturally-conditioned LLM?
Contributions. To answer the above RQs, our proposed methodology starts with the identiﬁcation of a
targeted set of WVS-derived cultural variables with explicit Inglehart-Welzel axis interpretation, which
are then used to prompt an LLM to generate culturally-grounded personas. Each of the generated personas
is used to condition another LLM before administering two different WVS-based benchmark resources,
which respectively provide indicators underlying the Inglehart-Welzel dimensions and WorldValueBench
cultural values associated with demographic groups. In addition, we deﬁne two moral-foundation
1

--- Page 2 ---

representation models for each generated culturally-grounded persona, to assess responses to the moral
foundations questionnaire and align them to LLM-guided mappings of moral foundation scores to our
deﬁned cultural variables.
Relevance to AI And Social Good. Our research study falls into the Interdisciplinary Approaches to AI
for Social Good as it explicitly integrates AI methods with socio-psychological theories and large-scale
cross-national survey frameworks, and is designed to be usable by social scientists, policymakers, and
other stakeholders interested in culturally aware AI for societal applications. Yet, it falls into AI Ethics,
Fairness, and Bias Mitigation approaches, as the analysis of how LLMs model cultural and moral variation
directly informs questions of value alignment, cross-cultural fairness and biases.
Impact in AI And Social Good. Our ﬁndings reveal patterns in how culturally-conditioned LLMs
encode human-values and moral dimensions, providing a common ground for multidisciplinary inquiry
across computer science, the social sciences, and the natural sciences into how AI systems represent and
potentially reshape human values. These results highlight concrete implications for the development of
methods and evaluations that ensure AI systems respect diverse cultural value structures and support
inclusive, cross-cultural human–AI interaction in socially impactful domains.
Direct collaboration with stakeholders and experts. By integrating computational methods with
social-scientiﬁc theories, this work supports collaboration with stakeholders by providing shared concepts
for auditing, adapting, and governing AI systems across diverse cultural contexts.
In particular, our research study beneﬁts from a collaboration with a team of anthropologists at
the Institute for Studies on the Mediterranean (ISMed),1 whose mission is to identify and analyze the
dynamics of the processes of growth and socio-economic development of international countries, with a
focus on the countries of the Mediterranean area.
2
Background
We begin by outlining the theoretical frameworks that serve as the pillars of our study, followed by a
description of the data and resources used for the analysis.
2.1
Theoretical Models
World Values Survey.
The World Values Survey (WVS) is an international research program and
network of social scientists devoted to the study of social, political, economic, religious, and cultural
values [26]. Particularly, WVS is a relevant and widely used source for studying cultural values worldwide
for several key reasons: (i) it covers a large number of countries across all major regions of the world;
(ii) it enables to study cultural change over time, as it has been conducted in multiple waves since the
early 1980s; (iii) it has a strong theoretical foundation, being closely linked to inﬂuential theories of
cultural change connecting values to economic development, modernization, and democratization (see
Inglehart-Welzel Cultural Map later in this section); (iv) it adopts rigorous sampling procedures, provides
detailed documentation of its methodology, and makes its data publicly available.
Inglehart–Welzel Cultural Map.
The Inglehart–Welzel (IW) Cultural Map positions societies in a
two-dimensional space deﬁned by two principal dimensions of cross-cultural variation: Traditional vs.
Secular-rational values (vertical axis) and Survival vs. Self-expression values (horizontal axis) ([14],
§Findings in [26]), i.e., moving upward in the map reﬂects a shift from traditional values to secular-
rational values, while moving rightward reﬂects a shift from survival values to self-expression values.
According to the WVS (§Data and Documentation in [26]), each point in the map is built from two factor
scores obtained by applying factor analysis over a set of 10 WVS indicators: happiness, interpersonal
trust, respect for authority, petition signing, importance of God, justiﬁability of homosexuality, abortion,
1www.ismed.cnr.it/
2

--- Page 3 ---

national pride, post-materialism, and autonomy index. Country positions are then derived by computing
within-country survey-weighted averages of these two factor scores, yielding each country’s coordinates
on the two-dimensional cultural map.
Moral Foundations Theory.
Moral Foundations Theory (MFT) holds that moral judgment arises from
innate psychological systems underlying people’s “intuitive ethics”, which cultures elaborate into virtues,
narratives, and institutions, positioning MFT as a descriptive theory of human morality.2 The original
MFT framework identiﬁes ﬁve moral foundations—care, fairness, loyalty, authority, and purity—and
provides functional/evolutionary motivations for each foundation; subsequent revisions of the framework
further split fairness into two components, equality and proportionality [5].
2.2
Data and Resources
World Values Survey Wave 7 (WVS-7).
To access WVS resources, we refer to the Wave 7 of the WVS,
which corresponds to a country-pooled dataﬁle (Version 5.0) [12]. The WVS-7 master questionnaire,
administered between 2017 and 2022, is organized into thematic blocks covering a broad range of cultural
and social domains, including Social values, attitudes & stereotypes; Happiness and well-being; Social
capital, trust & organizational membership; Postmaterialist index; Religious values; Ethical values and
norms; and Political interest & political participation.
WorldValuesBench.
We also use WorldValuesBench (WVB) [27], a benchmark derived from WVS-
7 that proposes a task of multi-cultural value prediction as producing a rating response to a value
question conditioned on demographic attributes.3 Speciﬁcally, we rely on WVB-PROBE, a compact
probe split (subset of the test set) which focuses on 36 value questions and three demographic variables
(continent, residential area, education level), using stratiﬁed sampling to ensure demographic diversity.
Our framework exploits WVB-PROBE to evaluate whether the personas induce culturally plausible value
proﬁles, without incurring the computational cost of running the full WVS-7.
Moral Foundations Questionnaire-2 (MFQ-2).
The Moral Foundations Questionnaire-2 (MFQ-2)
is a designed to measure moral aspects in a way that generalizes across cultural contexts [5]. Building
on evidence from 25 populations, MFQ-2 consists of 36 declarative items (six per moral foundation)
rated on a 5-point Likert scale from Does not describe me at all (1) to Describes me extremely well (5).
The authors report evidence for cross-cultural reliability and validity, and show that MFQ-2 improves
predictive performance compared to the previous version (MFQ-1) on a broad set of external criteria.
3
Cultural Variables and Persona Generation
Cultural Variables. We identify a set of 10 cultural variables, which encompass the main indicators
from WVS-7 that are used in constructing the Inglehart–Welzel axes and related dimensions, namely:
religiosity, child-rearing values, moral acceptability, trust and social capital, political participation,
national pride, happiness, gender equality, materialism orientation, attitude toward outgroups. Each
of the variables is deﬁned as a categorical variable with admissible values that are coded ordinally but
conceptually categorical for interpretation in terms of the Inglehart–Welzel axes. Due to space limits,
we report in Suppl. Mat.-Sect. C all details regarding the conceptual deﬁnition of our deﬁned cultural
variables, their admissible values, and links to the WVS-7 questionnaire IDs, interpretation and relation
with Inglehart–Welzel axes.
Let us denote with V = {vi}10
i=1 our deﬁned set of cultural variables, where each variable vi has
admissible values, or levels, l(vi) = {ℓi1, . . . , ℓiki}. We compute the cultural conﬁguration space C(V)
2moralfoundations.org/
3github.com/Demon702/WorldValuesBench
3

--- Page 4 ---

Figure 1: Overview of the main ﬂows and data modules in our proposed framework
of V by taking the Cartesian product over all variable levels, i.e., C(V) = Q10
i=1 l(vi). This leads to a total
of 93 312 unique cultural conﬁgurations.
Culturally-grounded Personas. Each cultural variable conﬁguration is to be used to condition the
generation of a persona proﬁle. To this purpose, we design a persona generation prompt template—shown
in Suppl. Mat.-Sect. E—where a cultural conﬁguration is provided as the conditioning parameter in input,
and each persona proﬁle is generated to contain (i) proﬁle metadata (name, age, gender, occupation, and
a plausible country/region), (ii) a short bio, and (iii) an explicit cultural variable mapping that grounds
attitudes and behaviors in each of the cultural variables in V.
By using this template to prompt an LLM, we generate a set P of persona proﬁles, each corresponding
to one of the 93 312 cultural conﬁgurations. To do this, we choose to rely on GPT-OSS 20b, recently
introduced by [20] which offers a favorable trade-off between model size and competitive reasoning,
generation, and instruction-following capabilities, while remaining open-weight, thus suitable for model
transparency and reproducibility.
Looking at the distribution of demographics (age, gender, and occupations) extracted from the
metadata ﬁelds of the generated personas, we found a gender balance with 48.96% ‘man’, 47.98% ‘woman’
and the remainder comprising non-binary or other/unspeciﬁed labels; age is strongly concentrated in
the 30–39 and 40–49 ranges, and the most frequent occupation categories are ‘education & academia’
(21.37%), ‘social services & nonproﬁt’ (13.28%), ‘sales & marketing’ (12.69%), and ‘tech / IT / data’
(8.63%).
We also examined the country frequency distribution of the generated personas, ﬁnding it as a long-
tailed already within the top 100 most frequent countries (<1% for many countries), with North America
and Europe dominating (led by the United States), followed by Asia, while other continents appear with
smaller shares.
Details on the demographic and country distributions of the generated personas, together with lexical
statistics of their proﬁles, are reported in Suppl. Mat.-Sect. D.
4
Methodology
We examine our generated culturally-grounded personas P through complementary analytical lenses
leveraging LLM conditioning on these personas. We deﬁne four persona representation models to
address the stated RQs: (i) IW-based embeddings of personas to be used for mining cultural patterns
in the IW map (RQ1), (ii) WVS cultural proﬁles based on persona-conditioned LLM responses to the
WVB-Probe questions (RQ2), and (iii) two moral-foundation representations of personas based on
persona-conditioned LLM responses to MFQ-2 and on aggregation of LLM-judged moral foundations
scores mapped to our cultural variables (RQ3).
Figure 1 provides an illustrative overview of the proposed methodological framework, with the three
branches on the right corresponding to the RQs outlined above. These branches are discussed in detail in
the following sections. It is worth emphasizing that all models, artifacts and analytical outcomes of our
framework have been validated by the team of anthropologists at ISMed (cf. Introduction).
4

--- Page 5 ---

4.1
Inglehart–Welzel Map Distribution of Personas (RQ1)
Computing the IW map coordinates. We ﬁrst aim to project each persona into the Inglehart–Welzel
(IW) cultural map by extracting coordinates rIW (p) = (z1, z2) that represent the persona’s position
relative to the IW axes.
To this aim, we resorted to the methodology in [25] to reconstruct country-level coordinates from
responses collected in the WVS and European Values Study (EVS), using the longitudinal EVS/WVS
trend resources (§Data Download in [26]), i.e., the Integrated Values Surveys (IVS) obtained by merging
the EVS Trend File and the WVS Trend File, which aggregate nationally representative survey waves
and provide harmonized indicators underlying the IW dimensions. In our setting, we condition the LLM
with a persona p and ask it to respond the IVS questions corresponding to the ten WVS indicators (cf.
Sect. 2.1). Then, following the guidance provided by the WVS Association (§Data and Documentation
in [26]), Principal Component Analysis (PCA) with varimax rotation is applied to the standardized
individual-level responses. Accordingly, the ﬁrst two components explain 39% of the variation in
the data, with PC1 identifying the IW axis of Survival vs. Self-Expression and PC2 the IW axis of
Traditional vs. Secular Values. Finally, a rescaling is applied to produce the IW coordinates z1 and
z2, respectively, used for the mapping: z1 = 1.81 × PC1 + 0.38 and z2 = 1.61 × PC2 −0.01 (see
https://github.com/kwinkunks/ai-values).
Mining cultural patterns in the IW space. Upon the calculation of all points rIW (p), our next step is
to carry out an exploratory mining process which is comprised of two steps: Step 1 – induce a partitioning
of the set {rIW (p)} on the IW plane into spatially contiguous regions, and Step 2 – characterize the most
relevant persona-conditioning cultural-conﬁgurations. We elaborate on each of these steps next.
Step 1. We aim to compute a Voronoi tessellation of the IW map, such that each point rIW (p) will be
assigned to its corresponding Voronoi cell (i.e., the one centered on the nearest grid seed, based on the
distance in the map with its representation rIW (p)). The Voronoi tessellation offers a principled way to
impose a local geometric organization, thus enabling the mining of meaningful patterns at Voronoi-cell
level.
Step 2. Once computed the cultural Voronoi-regions, each persona is represented in a transactional
format based on the associated conditioning cultural conﬁguration. More speciﬁcally, for each Voronoi
cell, a transactional mini-dataset is built where each persona p (corresponding to its point rIW (p) located
in that cell) is modeled as a set of items, where an item is an element (i.e., variable-value) of the cultural
conﬁguration originally associated with p.
Each transactional mini-dataset speciﬁc of a Voronoi cell is then fed to a frequent-pattern-mining
method to induce the most frequently occurring itemsets, i.e., sets of cultural conﬁguration items, in that
cell. To this purpose, we used the FPClose algorithm [11] to retain only the closed-frequent itemsets (i.e.,
frequent itemsets having no superset with identical support). We start with minimum support sufﬁciently
low (0.2 in our experiments) to include itemsets covering all cultural variables across all cells. Then, for
the sake of presentation of each cell, we control the most representative cultural-conﬁguration itemsets:
by denoting with T a cultural-conﬁguration itemset and with sc(T) its support within a cell c (i.e., the
fraction of personas in c whose cultural-conﬁguration itemsets contain T), we retain only itemsets whose
support is a fraction ρ ∈[0, 1] of the maximum support smax
c
observed in c.
4.2 WVS Distribution Alignment of Personas (RQ2)
We model each generated persona p as a vector rWV B(p) representing, for each of the 36 probe questions
from the WVB-Probe, the categorical response, obtained by conditioning the LLM on persona p—prompt
template reported in Suppl. Mat.-Sect. E. Moreover, since the WVB links the questions to the demographic
variables of continent, residential area and education level (cf. Sect. 2.2), the prompt also assigns a
persona p to a demographic triple. Subsequently, we aggregate the WVB responses corresponding to
personas into groups each sharing the same demographic triple. For each of these groups g and probe
question q, we obtain a distribution Pg,q of the response categories provided by the LLM.
5

--- Page 6 ---

WVB-Probe also provides reference human-based distributions for each group and question. There-
fore, we measure the distributional alignment by ﬁrst comparing the distance between Pg,q and the
corresponding distribution Hg,q using the Earth Mover’s distance (EMD), deﬁned as:
EMD(P, H) =
K
X
k=1
|FP (k) −FH(k)|
(1)
where K is the total number of response-categories for the WVB-Probe, whereas FP (k) and FH(k)
denote the cumulative distribution function of Pg,q and Hg,q, respectively, up to category k. An overall,
distributional alignment score is ﬁnally computed as 1 −EMD, where EMD is the average EMD over
all questions and groups.
4.3
Moral Representations of Personas (RQ3)
Based on the moral foundations theory referring to 6 moral foundations (cf. Sect. 2.1), we deﬁne two
moral-foundation representation models for any given culturally-grounded generated persona. The two
representation models are devised to be alternative in that the one is based on the response to the MFQ-2
questionnaire items after administering them to an LLM prompted with a culturally-grounded persona,
while the other is produced by aggregating moral foundation scores directly mapped to our deﬁned
cultural variables. As discussed later in the experimental part, the ultimate goal is to assess the alignment
of the two moral representations of personas.
MFQ-based Representation. For each persona p ∈P, we prompt an LLM with the full description of
p and elicit numeric responses to all 36 MFQ-2 items—prompt templates shown in Suppl. Mat.-Sect. E
(Fig. 7). As a result, p is associated with a 6-dimensional representation rMFQ(p) = [yp,m]m∈M, with
M denoting the set of 6 moral foundations and each yp,m being computed as the average over the 5-point
Likert items in the MFQ-2 questionnaire associated with the particular moral foundation m [5].
MFT-inferred Representation. We ﬁrst deﬁne a scoring function as an oracle to assign each value of a
cultural variable with a 5-point Likert score for each of the moral foundations. We provide the oracle
with full deﬁnitions of the moral foundations as well as of the cultural variables in the prompt used to ask
the oracle generate the mapping scores. To choose the oracle, we experimented with the most recently
released, powerful LLMs—such as Google Gemini 3 Pro [9], OpenAI GPT-5.2 [19], Anthropic Claude
Sonnet 4.5 [4], in addition to the default LLM used for the other tasks. Our team of anthropologists at
ISMed ﬁnally validated the oracle.
The resulting moral-foundation scoring model can be seen as a matrix of shape 32 (values of the
cultural variables) × 6 (moral foundations), with 5-point Likert-scale values.
For any p ∈P, a 6-dimensional representation rMFT (p) is derived by aggregating the row vectors
from the model-matrix corresponding to the cultural conﬁguration items of p.
5
Experimental Evaluation
In this section, we present our experimental results, structured around the research questions (RQs).4
5.1
Results for RQ1
The scatter plot in Fig. 2 shows an elliptical-cloud-like shape of the distribution of the rIW (p) rep-
resentations of our culturally-grounded personas (cf. Section 4.1), which is slightly shifted upward
and tilted diagonally from the upper left to the lower right. This means that the IW mapping tends
to concentrate more on the Secular dimension rather than Traditional one, with a negative correlation
4Our experimental environment was a 8× NVIDIA A30 GPUs (24GB VRAM each), 764GB RAM, 2× Intel Xeon
Gold 6248R (96 CPU cores total), Ubuntu Linux 20.04.6 LTS. For the LLM, we set temperature = 1.0 and top_p = 1.0 as
recommended by OpenAI.
6

--- Page 7 ---

Figure 2: Inglehart–Welzel map of all our synthetically-generated culturally-grounded personas. Axes
correspond to Traditional (downward), Secular-rational (upward), Survival (leftward), and Self-expression
(rightward) IW dimensions.
Closed frequent cultural-
#cells
avg.
support
avg. per-
conﬁguration itemset
support
range
cell #pers.
happiness = very happy;
21 0.735 [0.47, 0.99]
353
social trust = most people trusted
happiness = not at all happy;
15 0.806 [0.51, 1.00]
370
social trust = cannot trust people
happiness = very happy; national pride = very proud;
11 0.796 [0.55, 1.00]
131
social trust = most people trusted
happiness = not at all happy; national pride = not proud;
10 0.808 [0.57, 1.00]
205
social trust = cannot trust people
child rearing value = obedience faith;
6 0.670 [0.47, 0.84]
577
social trust = cannot trust people
moral acceptability = always justiﬁable;
4 0.658 [0.59, 0.81]
132
social trust = most people trusted
Table 1: A sample of closed frequent cultural-conﬁguration itemsets discovered in the Inglehart–Welzel
space of our synthetically-generated culturally-grounded personas (minimum support = 0.2, ρ = 0.5, cell
side length = 1, minimum number of covered cells = 2).
between Self-expression and Secular dimensions. While points become sparser toward the edges, the
highest density of points is within the mid-low Secular and Self-expression regimes.
To gain an additional insight on the effect due to the culturally-grounded persona based conditioning
of the LLM, we also asked the LLM to respond the IVS questions without any persona-conditioning.
The result, shown in Suppl. Mat.-Sect. F (Fig. 8), indicates that the IW coordinates of the baseline
LLM are in the upper-right quadrant, thus unveiling a model behavior more towards Secular and Self-
expression dimensions. Also, the positioning of the computed rIW (p) extends onto the IW map much
more compared to the IW typical country-level IW points (which occupy a relatively smaller region
around the axis center, cf. Suppl. Mat.-Sect. G, Fig. 9), thus showing an expected heterogeneity due to
the cultural differences that normally arise at individual level.
Turning our attention back to Fig. 2, we notice that no natural cluster structure arises. This prompted
us to simplify the originally devised computation of a Voronoi tessellation with a partitioning of the IW
map through a regular grid. To this purpose, each grid-cell’s side length was set to 1 to ensure a ﬁne-grain
resolution of the grid partitioning.
The closed frequent itemsets mining on the resulting grid-partitioning led to discover 735 closed
7

--- Page 8 ---

(a)
(b)
(c)
(d)
(e)
(f)
Figure 3: Inglehart–Welzel map distribution of the personas (blue points) that satisfy the itemsets
corresponding to the rows in Table 1.
Aggregation
(1 −EMD)
%(EMD <0.4)
%(EMD <0.2)
Unweighted
0.790
90.12
56.96
Weighted
0.809
94.25
59.06
Table 2: WVB-Probe alignment between the persona distributions and human-reference distributions,
aggregated by demographic groups. Lower Earth Mover’s distance (EMD) indicates closer alignment
with WVS reference distributions.
itemsets across 111 non-empty cells. Table 1 reports a representative subset of non-singleton patterns.
Trust and happiness emerge as the dominant cultural-conﬁguration items, indicating a robust alignment
between interpersonal trust and subjective well-being, with ‘high trust / very happy’ conﬁguration
frequent across 21 cells (mean support 0.735), and ‘low trust / not at all happy’ occurring across 15
cells (mean support 0.806). Both trust/happiness items also frequently occur with national pride, with
‘high-trust/high-happiness’ cells supporting a ‘very proud’ extension, and vice versa (‘not at proud at
all’). This might suggest that national pride acts as a conditioning variable that inﬂuences the core
trust-well-being structure. Beyond the trust/happiness core, the two bottom rows of Table 1 highlight
two additional trust-centered regularities: ‘cannot trust’ frequently co-occurs with child-rearing values
‘obedience’ and ‘faith’, while ‘cannot trust’ yet frequently co-occurs with ‘always justiﬁable’ of moral
acceptability.
Figure 3 shows that the closed frequent cultural-conﬁguration itemsets have clear and interpretable
spatial footprints in the IW space. Figures 3 (a)-(b) indicate that the two trust/happiness patterns occupy
opposite corners of the map: ‘high trust / very happy’ concentrates in the high self-expression/traditional
quadrant (i.e., bottom-right), while ‘low trust / not at all happy’ appears in the opposing survival, secular-
rational quadrant (i.e., top-left). Adding national pride reﬁnes these cells, as shown in Figures 3 (c)-(d):
‘very proud’ contracts the ‘high-trust/high-happiness’ footprint towards the extreme right tail (the strongest
self-expression side of the space), whereas ‘not proud at all’ contracts the ‘low-trust/low-happiness’
footprint towards the upper ridge (the most secular-rational end of the vertical axis), yielding smaller
but still coherent neighborhoods. By contrast, the remaining patterns have smaller and less contiguous
footprints, consistent with more localized cultural niches, as in the case of Figures 3 (e)–(f), showing the
obedience faith with ‘low trust’ areas in the traditional/survival side of the map, whereas ‘high moral
acceptability’ with ‘high trust’ portions on the opposite, more secular/self-expression side.
While closed frequent itemsets characterize the periphery of the IW map, many central areas retain
only singleton closed frequent itemsets (see Suppl. Mat.-Sect. G, Fig. 10 for a representative sample of
singleton patterns). In line with the IW “geometry”, such areas are mostly covered by singleton itemsets
associated with intermediate levels of the cultural variables (e.g., ‘not very happy’ and ‘rather happy’ for
happiness); by contrast, extreme categories tend to be placed toward peripheral areas of the map.
5.2
Results for RQ2
WVB-Probe. We evaluated WVB-Probe alignment by considering personas whose elicited demographic
triple corresponds to a group supported by WVB-Probe (i.e., a group for which human reference
8

--- Page 9 ---

Group
#personas 1 −EMD %(EMD <0.4) %(EMD <0.2)
(E |U |T)
32,716
0.803
94.4
52.8
(N-A |U |T)
14,984
0.832
97.2
69.4
(AS |U |T)
12,868
0.825
97.2
66.7
(S-A |U |T)
4924
0.799
94.4
55.6
(N-A |R |T)
4586
0.817
91.7
61.1
Table 3: WVB-Probe alignment between the persona distributions and human-reference distributions,
at group level, for the ﬁve mostly represented groups. Each group consists of (Continent |Settlement
|Education), where E = Europe, N-A = North America, S-A = South America, AS = Asia, U = Urban, R
= Rural, T = Tertiary.
distributions are available). This resulted in 92,710 personas (i.e., above 99% of the full set of personas),
which cover 45 out of 46 demographic groups (cf. Fig. 11 in Suppl. Mat. for details). Table 2 summarizes
EMD-based alignment between the persona distributions and human-reference distributions, based on: (i)
an unweighted averaging over the 45 demographic groups, where each group contributes equally; and (ii)
a weighted averaging, which accounts for the number of personas in each group. Remarkably, we observe
an alignment of 0.790 (unweighted) and 0.809 (weighted), indicating strong distributional alignment.
Question-level Agreement. Table 2 also shows the percentage of probe questions having moderate
alignment and those having high alignment, which correspond to EMD < 0.4 and < 0.2, respectively.
Across groups, moderate alignment is found to be close to saturation: on average, 90.12% of the 36
questions per group satisfy EMD <0.4 (weighted: 94.25%), indicating low distributional discrepancy for
most group-question pairs. By contrast, the stricter regime EMD <0.2 is substantially more discriminative
(below 60%).
Group-level Patterns.
In addition, Table 3 breaks down alignment for the ﬁve most represented
demographic proﬁles (see Suppl. Mat.-Sect. D, Fig. 11 for all groups). Alignment scores (1 −EMD)
are consistently high (0.799–0.832), with ‘urban’ and ‘tertiary’ dominating the group characterization.
Notably, (‘Europe’ |‘urban’ |‘tertiary’) is the largest group by count but exhibits a substantially lower
fraction of strongly aligned questions (52.8% with EMD <0.2) compared to groups with the same
residential area and education level but different continent (e.g., ‘North America’, at 69.4%, and ‘Asia’,
at 66.7%), despite comparable overall scores.
A complete breakdown over all 45 demographic groups is reported in Suppl. Mat.-Sect. H (Table 10).
Global alignment scores span 0.628 to 0.840.
5.3
Results for RQ3
To assess the results related to our RQ3, we evaluated the two moral representations for each culturally-
grounded persona p, namely the ones based on MFQ-2 (rMFQ(p)) and the ones inferred from the mapping
of the cultural variables (rMFT (p)) (cf. Sect. 4.3). Regarding the rMFT (p)s, we hereinafter refer to
those produced by Gemini 3 Pro since, unlike the other models that showed a marked tendency toward
assigning neutral scores (i.e., 2 or 3) across diverse inputs, it produced substantially higher score-variance,
yielding a more informative mapping for downstream analyses.
First, for each moral foundation, we compared rMFQ(p) with the default rMFT (p), i.e., obtained by
averaging over the full set of ten cultural conﬁguration items of p; however, since we found a substantial
difference in the trends and/or scale between the two representations (results shown in Suppl. Mat.-Sect. I,
Fig. 12), we wanted to delve into the set of cultural variables that are most relevant for each foundation
when computing the rMFT (p)s.
To this purpose, we decided to carry out a foundation-speciﬁc cultural-variable selection step over
the set of rMFT (p)s: once split it into training and validation subsets, we performed a greedy forward
procedure that, starting from an empty set, iteratively adds one candidate cultural-variable at a time
9

--- Page 10 ---

and evaluates its contribution by computing the R2 on the validation set, after applying a simple linear
correction to model predictions so that they better match the true values (i.e., rMFQ(p)), using only the
training data.
To produce statistically robust results, the foundation-speciﬁc greedy procedure was repeated for
50 independent runs. For each moral foundation, we ﬁnally kept the set of variables, hereinafter called
core-set, that were always selected in the 50 runs. All foundations-speciﬁc core-sets were eventually
validated and revised by the ISMed experts.
The discovered core-sets are: child rearing value, gender equality, happiness, materialism orientation,
social trust, tolerance diversity for Care; materialism orientation only for Equality and for Proportionality;
national pride for Loyalty; child rearing value, gender equality, national pride, religiosity, tolerance
diversity for Authority; religiosity for Purity.
Based on these core-sets, we recomputed the rMFT (p), ﬁnding that the foundation-speciﬁc core-set-
based aggregation tracks MFQ-2 trends more closely than the uniform 10-variable mean, with the clearest
improvements for Loyalty, Authority, and Purity. (Details in Suppl. Mat., Fig. 13)
Focusing on each core variable and corresponding moral foundation (results in Suppl. Mat.-Table 12),
the distribution of mean moral-foundation scores over the variable values follows a monotonic trend,
suggesting that the levels of a cultural variable are linearly related to the moral foundation scores.
However, the fraction of personas having a certain cultural conﬁguration can vary signiﬁcantly over the
values of the same core cultural-variable when considering moderate-to-strong association (i.e., score
≥4) with a moral foundation; this particularly holds for Authority with child rearing value, gender
equality, religiosity, for Purity and Loyalty.
By contrast, Care, Equality and, to a less extent, Proportionality appear to be culturally-invariant.
This ﬁnding admits various plausible explanations. The Care foundation exhibits scalar invariance across
different demographic groups [18]. Regarding Equality and Proportionality, the core-variable materialism
orientation, regardless of its degree, appears to rely on the same “hard-wired” cognitive mechanisms for
detecting cheating and unfair treatment. Invariance also emerges in the “Moral Chameleon” phenomenon
[17] which suggests that materialist may display functional invariance in their moral reasoning as they
ﬂexibly shift between moral principles in response to self-interest and situational demands.
6
Related Work
Research on cultural representation and inclusion in LLMs employ semantic and demographic proxies
[1], persona-based cultural conditioning with minimal identity indicators (e.g., names [21], language [3])
or cross-country benchmarks assessing distributional distance between models and human populations on
personality traits [10]. Also, survey-based alignment evaluations compare persona-prompted model re-
sponses with actual human respondents or survey-derived human proﬁles [3, 25], or emphasize sensitivity
to prompt format [15], and the need for grounding and transparency in generating personas [6].
Studies on moral assessments associate model judgements on moral norms across cross-national
survey standards [22], analyze the alignment between moral generations and group-labeled human
datasets in terms of moral/emotional traits [13], or measure moral beliefs through different scenarios [23].
Others investigate persona-conditioning in simulated debates [16] and extract moral preferences from
daily dilemmas [7]. MFT/MFQ-based investigations study political/demographic associations [24] and
role-play robustness [8]. Moral Compass [2] provides a data-driven decision benchmark built around
normative-ethics factors.
Table 4 compares related work and ours, across ﬁve aspects: persona prompting, reliance on human
survey data and moral frameworks, analysis on the IW cultural map, and the principal evaluation goal
used in each study. As it can be noted, unlike earlier work, our research uniquely combines the above
aspects in a controlled audit: we conceptualize personas based on WVS-derived cultural variables, and
analyze them through well-established theoretical models and benchmarks to study human-values and
moral foundations.
10

--- Page 11 ---

Work P S M IW Evaluation
[1]
✓✗
✗
✗
Proxy taxonomy
[21]
✓✗
✗
✗
Names as proxy
[10]
✓✗
✗
✗
Distributional distance
[3]
✓✓✗
✗
Anthropol.-based survey simul.
[25]
✗✓✗
✓
Survey simulation
[15]
✓✓✗
✓
Prompt format
[6]
✓✗
✗
✗
Grounding & transparency anal.
[22]
✗✓✗
✗
Survey-validated probing
[13]
✗✗✓
✗
Corpus alignment
[23]
✗✗
✗
✗
Prompt marginalization
[16]
✓✗
✗
✗
Multi-turn debate
[7]
✗✓✓
✗
Dilemma preferences
[24]
✓✗✓
✗
MFT probing
[8]
✓✗✓
✗
MFQ robustness
[2]
✗✗✓
✗
Ethics benchmark
Ours
✓✓✓
✓
Controlled audit
Table 4: Comparison between related work and our setting along ﬁve axes: persona use (P), survey
grounding (S), moral framework (M), IW-based structure (IW), and evaluation goal.
7
Conclusions
We introduced a WVS-grounded framework to generate culturally conditioned personas and assess their
alignment with established value and moral theories. Personas exhibit structured, interpretable variation
on the Inglehart–Welzel map and show strong demographic-level agreement with human WVS-derived
response distributions. Comparing MFQ-2 moral proﬁles with culture-to-morality mappings suggests
that core cultural-variables explain much of the variation for Loyalty, Authority, and Purity, while Care,
Equality, and Proportionality appear to be culturally invariant. Overall, explicit cultural grounding enables
a controlled audit of cultural and moral representations in LLM-generated personas.
Reproducibility Statement. All deﬁnitions, detailed statistics, model prompts are provided in the
Suppl. Material.
Ethics Statement
While we operationalize culture through interpretable WVS-derived variables and publicly available
survey resources, this remains a proxy-based representation that captures only a subset of cultural
phenomena, particularly survey-measurable values and attitudes. As a result, our ﬁndings should not be
read as a comprehensive account of culture, but rather as evidence about alignment under this speciﬁc
operationalization.
We grounded personas in interpretable cultural variables and evaluated them against established
socio-psychological frameworks. Nonetheless, the resulting proﬁles should be interpreted with caution,
since they cannot capture the full complexity of lived human experiences, socialization processes, or
situated moral decision-making. We also emphasize that the generated personas are not intended to
correspond to real individuals and do not have access to real-life personal or identiﬁable information.
As synthetic artifacts, the generated personas may potentially reinforce stereotyped associations,
simpliﬁed cultural caricatures, or unrealistic combinations of demographic attributes and value proﬁles.
In this respect, the metadata distributions (e.g., country, age, occupation) in our personas are uneven,
showing over-representation of North America and Europe and concentration in the 30–49 age range.
This may introduce generation biases that are independent of the intended cultural variables, limiting
worldwide representativeness. Also, the culture-to-country association is endogenous to the involved
11

--- Page 12 ---

LLM(s) and may reﬂect pretraining priors on relations between national identity and cultural values.
Furthermore, our framework is conceived to be descriptive rather than prescriptive: it is not meant to
rank cultures, deﬁne “correct” moral views, or justify decisions about individuals or groups.
As a ﬁnal remark, in addition to the contents provided in the Suppl. Mat. associated to this submission,
we are committed to release all artifacts we created, including the generated personas and the MFT-inferred
persona representations.
References
[1] Muhammad Farid Adilazuarda, Sagnik Mukherjee, Pradhyumna Lavania, Siddhant Shivdutt Singh,
Alham Fikri Aji, Jacki O’Neill, Ashutosh Modi, and Monojit Choudhury. Towards measuring and
modeling “culture” in LLMs: A survey. In Yaser Al-Onaizan, Mohit Bansal, and Yun-Nung Chen,
editors, Proceedings of the 2024 Conference on Empirical Methods in Natural Language Process-
ing, pages 15763–15784, Miami, Florida, USA, November 2024. Association for Computational
Linguistics.
[2] Aisha Aijaz, Arnav Batra, Aryaan Bazaz, Srinath Srinivasa, Raghava Mutharaju, and Manohar
Kumar. Moral compass: A data-driven benchmark for ethical cognition in ai. In James Kwok,
editor, Proceedings of the Thirty-Fourth International Joint Conference on Artiﬁcial Intelligence,
IJCAI-25, pages 9529–9537. International Joint Conferences on Artiﬁcial Intelligence Organization,
8 2025. AI and Social Good.
[3] Badr AlKhamissi, Muhammad ElNokrashy, Mai Alkhamissi, and Mona Diab. Investigating cultural
alignment of large language models. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar, editors,
Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume
1: Long Papers), pages 12404–12422, Bangkok, Thailand, 2024. Association for Computational
Linguistics.
[4] Anthropic. Claude sonnet 4.5. https://www.anthropic.com/claude/sonnet, 2025.
[5] Mohammad Atari, Jonathan Haidt, Jesse Graham, Sena Koleva, Sean T. Stevens, and Morteza
Dehghani. Morality beyond the weird: How the nomological network of morality varies across
cultures. Journal of Personality and Social Psychology, 2023. In press.
[6] Jan Batzner, Volker Stocker, Bingjun Tang, Anusha Natarajan, Qinhao Chen, Stefan Schmid, and
Gjergji Kasneci. Whose personae? synthetic persona experiments in llm research and pathways to
transparency. In Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society, volume 8,
pages 343–354, 2025.
[7] Yu Ying Chiu, Liwei Jiang, and Yejin Choi. Dailydilemmas: Revealing value preferences of llms
with quandaries of daily life. In The Thirteenth International Conference on Learning Representa-
tions, ICLR 2025, Singapore, April 24-28, 2025. OpenReview.net, 2025.
[8] Davi Bastos Costa, Felippe Alves, and Renato Vicente. Moral susceptibility and robustness under
persona role-play in large language models. CoRR, abs/2511.08565, 2025.
[9] Google DeepMind. Gemini 3 pro. https://deepmind.google/models/gemini/pro/,
2025.
[10] Priyanka Dey, Aayush Bothra, Yugal Khanter, Jieyu Zhao, and Emilio Ferrara. Can LLMs express
personality across cultures? introducing CulturalPersonas for evaluating trait alignment. In Christos
Christodoulopoulos, Tanmoy Chakraborty, Carolyn Rose, and Violet Peng, editors, Findings of the
Association for Computational Linguistics: EMNLP 2025, pages 20241–20262, Suzhou, China,
November 2025. Association for Computational Linguistics.
12

--- Page 13 ---

[11] Gösta Grahne and Jianfei Zhu. Fast Algorithms for Frequent Itemset Mining Using FP-Trees. IEEE
Trans. Knowl. Data Eng., 17(10):1347–1362, 2005.
[12] C. Haerpfer, R. Inglehart, A. Moreno, C. Welzel, K. Kizilova, J. Diez-Medrano, M. Lagos, P. Norris,
E. Ponarin, and B. Puranen. World values survey: Round seven - country-pooled dataﬁle version
5.0, 2022.
[13] Zihao He, Siyi Guo, Ashwin Rao, and Kristina Lerman. Whose emotions and moral sentiments do
language models reﬂect? In Lun-Wei Ku, Andre Martins, and Vivek Srikumar, editors, Findings of
the Association for Computational Linguistics: ACL 2024, pages 6611–6631, Bangkok, Thailand,
August 2024. Association for Computational Linguistics.
[14] Ronald Inglehart and Christian Welzel. Modernization, Cultural Change and Democracy: The
Human Development Sequence. Cambridge University Press, New York, 2005.
[15] Mohsinul Kabir, Ajwad Abrar, and Sophia Ananiadou. Break the checkbox: Challenging closed-
style evaluations of cultural alignment in LLMs.
In Christos Christodoulopoulos, Tanmoy
Chakraborty, Carolyn Rose, and Violet Peng, editors, Proceedings of the 2025 Conference on
Empirical Methods in Natural Language Processing, pages 24–51, Suzhou, China, 2025. Associa-
tion for Computational Linguistics.
[16] Jiarui Liu, Yueqi Song, Yunze Xiao, Mingqian Zheng, Lindia Tjuatja, Jana Schaich Borg, Mona T.
Diab, and Maarten Sap. Synthetic socratic debates: Examining persona effects on moral decision
and persuasion dynamics. In Christos Christodoulopoulos, Tanmoy Chakraborty, Carolyn Rose,
and Violet Peng, editors, Proceedings of the 2025 Conference on Empirical Methods in Natural
Language Processing, pages 16428–16458, Suzhou, China, November 2025. Association for
Computational Linguistics.
[17] Ziqiang Liu, Hong Zhang, Li Wei, and Xinxin Ge. Moral Chameleons: The positive association
between materialism and self-interest-triggered moral ﬂexibility. Journal of Research in Personality,
100:104268, 2022.
[18] Artur Nilsson. Measurement Invariance of Moral Foundations across Population Strata. Journal of
Personality Assessment, 105:163–173, 2023.
[19] OpenAI. Gpt-5.2. https://platform.openai.com/docs/models/gpt-5.2, 2025.
[20] OpenAI. gpt-oss-120b & gpt-oss-20b model card. https://arxiv.org/abs/2508.10925,
2025.
[21] Siddhesh Milind Pawar, Arnav Arora, Lucie-Aimée Kaffee, and Isabelle Augenstein. Presumed
cultural identity: How names shape LLM responses. In Christos Christodoulopoulos, Tanmoy
Chakraborty, Carolyn Rose, and Violet Peng, editors, Findings of the Association for Computational
Linguistics: EMNLP 2025, pages 22147–22172, Suzhou, China, November 2025. Association for
Computational Linguistics.
[22] Aida Ramezani and Yang Xu. Knowledge of cultural moral norms in large language models. In
Anna Rogers, Jordan Boyd-Graber, and Naoaki Okazaki, editors, Proceedings of the 61st Annual
Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 428–446,
Toronto, Canada, July 2023. Association for Computational Linguistics.
[23] Nino Scherrer, Claudia Shi, Amir Feder, and David Blei. Evaluating the moral beliefs encoded in
llms. Advances in Neural Information Processing Systems, 36:51778–51809, 2023.
13

--- Page 14 ---

[24] Nicole Smith-Vaniz, Harper Lyon, Lorraine Steigner, Ben Armstrong, and Nicholas Mattei. Investi-
gating political and demographic associations in large language models through moral foundations
theory. In Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society, volume 8, pages
2419–2430, 2025.
[25] Yan Tao, Olga Viberg, Ryan S Baker, and René F Kizilcec. Cultural bias and cultural alignment of
large language models. PNAS Nexus, 3(9):pgae346, 2024.
[26] WVS Association. World values survey. https://www.worldvaluessurvey.org/wvs.
jsp, 2025.
[27] Wenlong Zhao, Debanjan Mondal, Niket Tandon, Danica Dillion, Kurt Gray, and Yuling Gu.
WorldValuesBench: A large-scale benchmark dataset for multi-cultural value awareness of language
models. In Nicoletta Calzolari, Min-Yen Kan, Veronique Hoste, Alessandro Lenci, Sakriani
Sakti, and Nianwen Xue, editors, Proceedings of the 2024 Joint International Conference on
Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024), pages
17696–17706, Torino, Italia, May 2024. ELRA and ICCL.
14

--- Page 15 ---

Supplementary Material
A
Limitations
Our framework is English-centric in both persona descriptions and response elicitation. We do not test
whether equivalent cultural conﬁgurations yield stable signals under multilingual prompting or culturally
speciﬁc phrasing. Future work could explore multilingual and culturally localized elicitation setups to
evaluate whether the same cultural speciﬁcations produce consistent signals across languages and prompt
formulations.
The generated personas are the result of 93,312 conﬁgurations (i.e., all possible combinations of
the 10 cultural variables and their admissible values), which may contain conﬁgurations that are rare or
sociologically implausible in real populations. Some discovered patterns in the IW space may therefore
reﬂect the designed LLM-based generation procedure, which depends on the LLM’s parametrization and
training data, combinatorics rather than naturally occurring cultural proﬁles. Treating each conﬁguration
as equally likely describes what is possible under the variable scheme, not what is probable in human
populations. We will consider reweighting strategies to better reﬂect empirical prevalence and reduce the
inﬂuence of atypical conﬁgurations.
Our deﬁned cultural variables are derived from WVS-7 constructs and indicators, which comprise
surveys from 2017 to 2022. Since cultural norms evolve over time due to migration, crises, and social
change, our alignment with static, survey-era patterns may not fully capture current or emerging cultural
dynamics.
B
Experimental Setting
All generations have been executed on a server with 8× NVIDIA A30 GPUs (24GB VRAM each),
764GB system RAM, 2× Intel Xeon Gold 6248R (96 CPU cores total), running Ubuntu Linux 20.04.6
LTS. We set temperature = 1.0 and top_p = 1.0 as recommended by OpenAI.5
C
Details on the Cultural Variables
Table 5 overviews our deﬁned 10 cultural variables, which are used in our study to culturally condition
the generation of persona proﬁles.
It should be noted that our deﬁned 10 cultural variables are derived from WVS-7 items as a subset
identiﬁed to operationalize the two main Inglehart–Welzel dimensions of cross-national cultural variation.
More speciﬁcally, the 10 cultural variables are abstractions that often group more WVS-7 questions,
as reported next: importance of religion (Q6); child-rearing priorities such as obedience, religious
faith, and tolerance/respect (Q7–Q17); subjective happiness (Q46); generalized social trust (Q57);
religiosity items centered on the importance of God and related beliefs/practices (Q164–Q175); moral
acceptability judgments on a 1–10 justiﬁability scale (e.g., Q177–Q191); gender-role attitudes (e.g.,
Q29–Q33); postmaterialism priorities (Q152–Q157); and attitudes toward outgroups (Q18–Q26); political
participation (Q199-Q234).
5github.com/openai/gpt-oss?tab=readme-ov-file#recommended-sampling-parameters
15

--- Page 16 ---

Cultural variable
Concept
Admissible values
Relation with IW axes
religiosity
Importance and practice
of religion; belief in God.
very important (10)
quite important (7–9)
not very important (4–6)
not at all important (1–3)
Traditional (higher) →
Secular (lower)
child rearing
value
Qualities desired for
children (obedience/faith
vs. indepen-
dence/imagination).
obedience-faith
(selects obedience/religious faith)
independence-imagination
(selects independence/imagination)
neutral (no clear preference)
Traditional (obedience-faith);
Secular-Rational / Self-
Expression (independence-
imagination)
moral
acceptability
Justiﬁability of morally
contested acts (e.g.,
abortion, euthanasia,
divorce, suicide,
homosexuality).
never justifiable (1–3)
sometimes justifiable (4–7)
always justifiable (8–10)
Traditional (never) →
Secular (always),
for moral items;
Survival (never) →
Self-Expression (always),
for tolerance items
social trust
Generalized interpersonal
trust (“most people can be
trusted”).
most people trusted (1)
cannot trust people (0)
Survival (0)
Self-Expression (1)
political
participation
Civic engagement and
activism.
active participant
(signed petition, joined protest,
contacted ofﬁcials)
passive participant
(votes only, minimal engagement)
nonparticipant (no participation)
Survival (nonpartic.) →
Self-Expression (active)
mixed (passive)
national
pride
Identiﬁcation with nation
and pride in nationality.
very proud (4)
somewhat proud (3)
not very proud (2)
not proud at all (1)
Traditional (higher) →
Secular (lower)
happiness
Subjective well-being /
self-reported happiness.
very happy (4)
rather happy (3)
not very happy (2)
not at all happy (1)
Survival (lower) →
Self-Expression (higher)
gender
equality
Attitudes toward gender
roles in education, jobs,
and politics.
egalitarian
(disagrees that men are better leaders /
deserve jobs more)
moderate (neutral)
traditional
(agrees that men should have priority)
Survival / Traditional
(tradit.) →Self-Expression /
Secular (egalit.)
materialism
orientation
Materialist vs.
post-materialist priorities
(Inglehart battery).
materialist
(prioritizes economic and physical
security)
mixed (balanced concerns)
postmaterialist
(prioritizes freedom, self-expression,
participation)
Survival (material.) →
Self-Expression (post
material.)
tolerance
diversity
Attitudes toward
outgroups (minorities,
immigrants, different
lifestyles).
high tolerance
(accepts immigrants, LGBTQ+, other
religions)
moderate tolerance
(accepts some, not others)
low tolerance
(rejects most outgroups)
Survival (low) →
Self-Expression (high)
Table 5: Overview of our deﬁned 10 cultural variables: conceptual deﬁnition, admissible categories, and
interpretation of the ordinal values in terms of Inglehart–Welzel axes.
16

--- Page 17 ---

D
Statistics of the Generated Culturally-grounded Personas
Metric
Avg.
Std.
Min
Max
Chars
3271.7
329.6
74
6864
Words
421.4
46
9
884
Tokens
657.3
61.2
24
1392
Table 6: Lexical statistics of the short bio and cultural variable mapping texts from the generated
personas.
Gender
%
Woman
47.984
Man
48.964
Non-binary / gender-neutral
1.631
Agender
0.002
Genderqueer
0.001
Unspeciﬁed / prefer not to say / Other
1.418
Age band
%
20–29
0.209
30–39
67.743
40–49
31.003
50–59
1.014
60–69
0.030
Table 7: Distributions of gender labels and age bands extracted from the metadata of the generated
personas.
Occupation macro
%
Occupation macro
%
Education & Academia
21.37
Arts / Media / Design
3.10
Social Services & Nonproﬁt
13.28
Finance / Banking / Insurance
2.04
Sales & Marketing
12.69
Consulting / Professional Services
1.88
Tech / IT / Data
8.63
Agriculture & Natural Resources
1.79
Management / Operations / Admin
5.99
Other / Unclear
1.74
Retail / Hospitality / Small Business
5.95
Healthcare & Medicine
1.60
Manufacturing & Skilled Trades
5.86
Transportation & Logistics
1.43
Government & Public Sector
4.14
Religious / Clergy
0.81
Construction / Real Estate / Planning
4.05
Not in labor force
0.17
Engineering (non-IT)
3.32
Law & Legal
0.15
Table 8: Distribution of occupations after mapping free-form model generations to 20 macro-categories.
17

--- Page 18 ---

Country
% personas Country
% personas
United States
17.53 Kazakhstan
0.29
Poland
8.65 Ireland
0.27
Mexico
6.13 France
0.27
Germany
5.47 Kenya
0.26
Netherlands
4.39 Guatemala
0.25
Philippines
3.86 China
0.23
Brazil
3.71 Vietnam
0.22
Sweden
3.54 New Zealand
0.19
India
3.34 Ghana
0.17
Canada
2.69 Ecuador
0.16
Spain
2.28 Central Europe
0.16
Italy
2.12 Iran
0.15
Turkey
1.92
Costa Rica
0.14
Czechia
1.85
Bangladesh
0.14
United Kingdom
1.68 Belarus
0.14
Saudi Arabia
1.62 Bosnia and Herzegovina
0.14
Pakistan
1.4
Croatia
0.13
Portugal
1.3
Middle East
0.12
Russia
1.25 Slovenia
0.1
Indonesia
1.14 Lebanon
0.1
United Arab Emirates
1.11 Tunisia
0.09
Finland
1.02
Thailand
0.08
Norway
1.01
Qatar
0.07
Jordan
0.99 Uruguay
0.07
Hungary
0.93 Ethiopia
0.07
Argentina
0.84 Moldova
0.06
South Korea
0.76 Central America
0.06
Egypt
0.76 Oman
0.06
Denmark
0.76 Lithuania
0.06
Austria
0.75 Belgium
0.05
Japan
0.69 Kuwait
0.05
Switzerland
0.55 Kyrgyzstan
0.05
Malaysia
0.54 Georgia
0.05
Serbia
0.52 Uzbekistan
0.05
Chile
0.52 Uganda
0.04
Romania
0.51 Bolivia
0.04
Israel
0.51 Europe
0.04
Colombia
0.49 Iraq
0.04
Nigeria
0.48 Indiana
0.04
Bulgaria
0.43 Colorado
0.04
Australia
0.4 Latvia
0.03
Estonia
0.4 Iceland
0.03
Singapore
0.4 Dominican Republic
0.03
Czech Republic
0.37 El Salvador
0.03
Morocco
0.37 Nicaragua
0.03
South Africa
0.35 Palestine
0.03
Slovakia
0.33 England
0.03
Peru
0.31 Puerto Rico
0.03
Greece
0.3 North Macedonia
0.03
Ukraine
0.29 Nepa
0.02
Table 9: Percentage of personas across the ﬁrst 100 countries by count.
18

--- Page 19 ---

E
Prompts
Persona Generation Prompt Template
Conditioning:
{cultural configuration}
Task:
You are asked to generate a single detailed persona proﬁle that is consistent with the conditioning above.
The persona must be coherent, realistic, and explicitly tie behaviors, life choices, and attitudes back to each
of the ten cultural variables listed. Use a professional-but-readable tone.
Deliverables (strict order):
• Proﬁle metadata: name, age, gender (optional), occupation, country/region (plausible given the
cultural proﬁle).
• Short bio: 2–4 sentences describing life situation and background.
• Cultural variable mapping: for each of the ten variables, 1–2 sentences explaining how the variable
manifests in attitudes and daily behavior (numbered list matching variable names).
Constraints:
• Each sentence in the cultural mapping must explicitly reference the corresponding conditioning
variable.
• No contradiction of the conditioning is allowed (e.g., never_justifiable must be reﬂected).
• The persona must remain within plausible real-world bounds.
• Output length must be between approximately 250 and 500 words.
Figure 4: Prompt template for the generation of culturally-grounded personas. The conditioning parameter
is a cultural conﬁguration, i.e., a list of (cultural variable, admissible value) pairs that corresponds to one
of the 93,312 possible combinations of our deﬁned cultural variables.
IW Indicator Elicitation Prompt
SYSTEM MESSAGE:
You are given a detailed persona proﬁle describing a person’s background, attitudes, and values. Assume
the role of this person when answering the following questions.
USER MESSAGE:
Task:
Answer the following questions as this person would, selecting the option that best reﬂects their beliefs and
attitudes. Each question corresponds to a cultural value indicator used in the Inglehart–Welzel cultural
map.
Questions:
{list of WVS-style questions corresponding to the 10 IW indicators}
Output format:
Provide one answer per question, following the original WVS response scales (e.g., binary choices, Likert-
type scales, or 1–10 justiﬁability ratings). Do not include explanations or additional text.
Figure 5: Prompt template used to obtain persona responses for computing the Inglehart–Welzel cultural
map indicators. Each persona is queried independently using this template.
19

--- Page 20 ---

WVB-Probe Prompting
SYSTEM MESSAGE:
You are the following person:
{persona profile}
Answer the following survey questions as this person would answer, based on their values and worldview.
It is very important to respond EXACTLY as requested. Be terse.
USER MESSAGE:
Before answering, report your demographics by selecting exactly one option from each list:
– Continent: [Africa, Asia, Europe, North America, South America, Oceania]
– Residential area: [Urban, Rural]
– Education: [Primary or No Education, Lower Secondary, Upper to Post Secondary, Tertiary]
Return the three ﬁelds in a structured form (one line each).
USER MESSAGE (REPEATED FOR EACH OF THE 36 WVB-PROBE ITEMS):
Question: {WVB-Probe question prompt}
Return only a single integer on the response scale speciﬁed in the question prompt.
Figure 6: WVB-Probe prompt template. The LLM is conditioned on the full generated-persona proﬁle
and then prompted to (i) output a demographic triple compatible with WVB and (ii) answer the 36
WVB-Probe value questions with a single integer per question.
MFQ-2 Prompting
SYSTEM MESSAGE:
You are the following person:
{persona profile}
Answer the following MFQ-2 survey as this person would answer, based on their values and worldview.
It is very important to respond EXACTLY as requested. Be terse.
USER MESSAGE:
You will be given 36 numbered MFQ-2 items. For each item, return a single integer in {1, 2, 3, 4, 5}.
Return ONLY valid JSON in the following format (and nothing else):
{"answers":
{"1":
<int>, ..., "36":
<int>}}
{MFQ-2 items list (1..36)}
Figure 7: MFQ-2 prompt template. The LLM is conditioned on the full generated-persona proﬁle and
prompted to answer all 36 MFQ-2 items with a single integer per item, returned as a JSON object keyed
by item index.
20

--- Page 21 ---

F
Inglehart–Welzel Cultural Map Reference
Figure 8: Inglehart–Welzel cultural map with country positions reconstructed from IVS data and position
of the non-conditioned LLM (GPT-OSS 20b).
G
Personas on Inglehart-Welzel map and closed frequent itemsets
Figure 9: Overlay of our generated personas (blue dots) and country positions reconstructed from IVS
data on the Inglehart–Welzel cultural map. The rectangle marks the value space covered by real countries
(i.e., Fig 8).
21

--- Page 22 ---

(a) happiness = not very happy
(b) happiness = rather happy
(c) child rearing = neutral
(d) moral acceptability = sometimes
justiﬁcable
(e) tolerance diversity = low tolerance (f) tolerance diversity = high tolerance
(g) national pride = very proud
(h) national pride = not proud at all
Figure 10: A selection of singleton closed frequent itemsets, with mean minimum support equal to 0.2 and
ρ = 0.5. Panels (a–d) correspond to intermediate category levels (e.g., ‘not very happy’, ‘rather happy’,
‘neutral’, ‘sometimes justiﬁable’), whose footprints predominantly occupy the high-density central region
of the IW space. Panels (e–h) show extreme category levels (e.g., ‘high’ vs. ‘low tolerance’, ‘very
proud’ vs. ‘not proud at all’), whose footprints extend toward the periphery and exhibit clear axis-aligned
shifts. In particular, extreme values follow the directional associations predicted by the variable-to-axis
mapping (Table 5), producing systematic displacements along the Survival–Self-expression (horizontal)
and Traditional–Secular-rational (vertical) axes.
22

--- Page 23 ---

H
Demographic distribution of Personas for WVB-Probe
Figure 11: Distribution of demographic triples obtained during the WVB-Probe prompting.
23

--- Page 24 ---

Group (Continent |Settlement |Education)
# personas
1 −EMD
%(EMD <0.4)
%(EMD <0.2)
Europe |Urban |Tertiary
32716
0.803
94.4
52.8
North America |Urban |Tertiary
14984
0.832
97.2
69.4
Asia |Urban |Tertiary
12868
0.825
97.2
66.7
South America |Urban |Tertiary
4924
0.799
94.4
55.6
North America |Rural |Tertiary
4586
0.817
91.7
61.1
Europe |Rural |Tertiary
3364
0.828
97.2
63.9
North America |Rural |Upper to Post Secondary
2907
0.783
86.1
52.8
Asia |Rural |Tertiary
1998
0.784
88.9
52.8
Africa |Urban |Tertiary
1772
0.784
91.7
55.6
Europe |Urban |Upper to Post Secondary
1523
0.780
83.3
55.6
Europe |Rural |Upper to Post Secondary
1237
0.803
97.2
55.6
Asia |Urban |Upper to Post Secondary
1228
0.813
94.4
63.9
North America |Urban |Upper to Post Secondary
1035
0.788
91.7
55.6
North America |Rural |Lower Secondary
910
0.775
83.3
61.1
Asia |Rural |Upper to Post Secondary
859
0.808
88.9
58.3
Asia |Rural |Lower Secondary
843
0.777
88.9
55.6
South America |Rural |Tertiary
595
0.790
91.7
61.1
Europe |Rural |Lower Secondary
524
0.805
100.0
58.3
Oceania |Urban |Tertiary
513
0.796
91.7
55.6
Asia |Rural |Primary or No Education
492
0.786
83.3
50.0
Asia |Urban |Lower Secondary
334
0.803
94.4
61.1
South America |Urban |Upper to Post Secondary
313
0.782
94.4
44.4
South America |Rural |Upper to Post Secondary
242
0.823
91.7
69.4
Africa |Urban |Upper to Post Secondary
223
0.794
91.7
58.3
Europe |Urban |Lower Secondary
214
0.786
94.4
55.6
Africa |Rural |Tertiary
211
0.787
88.9
44.4
North America |Rural |Primary or No Education
192
0.774
83.3
58.3
North America |Urban |Lower Secondary
137
0.762
86.1
47.2
South America |Rural |Lower Secondary
135
0.774
86.1
61.1
Europe |Rural |Primary or No Education
134
0.801
91.7
69.4
Africa |Rural |Upper to Post Secondary
123
0.825
94.4
66.7
Africa |Rural |Lower Secondary
112
0.809
97.2
66.7
Africa |Rural |Primary or No Education
92
0.795
94.4
50.0
South America |Rural |Primary or No Education
85
0.774
75.0
55.6
South America |Urban |Lower Secondary
63
0.806
94.4
69.4
Africa |Urban |Lower Secondary
59
0.774
83.3
55.6
Asia |Urban |Primary or No Education
55
0.791
88.9
52.8
Oceania |Rural |Tertiary
32
0.840
94.4
72.2
Europe |Urban |Primary or No Education
23
0.804
83.3
66.7
North America |Urban |Primary or No Education
15
0.747
86.1
30.6
Africa |Urban |Primary or No Education
15
0.756
88.9
36.1
South America |Urban |Primary or No Education
12
0.820
97.2
66.7
Oceania |Urban |Upper to Post Secondary
6
0.838
97.2
66.7
Oceania |Rural |Upper to Post Secondary
4
0.774
88.9
50.0
Oceania |Urban |Primary or No Education
1
0.628
55.6
27.8
Table 10: Complete group-level WVB-Probe alignment for all 45 demographic triples supported by
WVB-Probe, sorted by decreasing number of personas. Score is 1 −EMD, where EMD is the mean
EMD across the 36 probe questions for the group. %EMD< 0.4 and %EMD< 0.2 denote the fraction of
probe questions whose distance falls below the corresponding threshold.
24

--- Page 25 ---

I
Additional Analyses on Moral Foundation Scores
(a)
(b)
(c)
(d)
(e)
(f)
Figure 12: Comparison between MFQ-2–based (blue) and mapping-based moral (orange) foundation
scores. Mapping-based scores are obtained using all cultural variables. Personas are ordered along the
x-axis; the y-axis reports foundation scores. To avoid cluttering, lines of both score types are smoothed
by averaging scores within consecutive bins of 300 personas (according to the ordering ﬁxed through
sorting by cultural variable then by admissible values).
(a)
(b)
(c)
(d)
(e)
(f)
Figure 13: Comparison between MFQ-2–based (blue) and mapping-based (orange) moral foundation
scores. Mapping-based scores are obtained using a greedy-selected subset of cultural variables. Personas
are ordered along the x-axis; the y-axis reports foundation scores. To avoid cluttering, lines of both
score types are smoothed by averaging scores within consecutive bins of 300 personas (according to the
ordering ﬁxed through sorting by cultural variable then by admissible values).
25

--- Page 26 ---

Moral Foundation
¯J
k distribution (#runs)
Selected variables (support)
Care
0.669 k=1 (10), k=6 (39), k=7 (1) child_rearing_value (0.80), gender_equality (0.80),
happiness (0.80), materialism_orientation (0.80), so-
cial_trust (0.80), tolerance_diversity (0.80), religiosity
(0.20), political_participation (0.02)
Equality
0.738 k=1 (37), k=3 (13)
materialism_orientation (1.00), gender_equality (0.26),
tolerance_diversity (0.26)
Proportionality
1.000 k=1 (50)
materialism_orientation (1.00)
Loyalty
1.000 k=1 (50)
national_pride (1.00)
Authority
1.000 k=5 (50)
child_rearing_value (1.00), gender_equality (1.00), na-
tional_pride (1.00), religiosity (1.00), tolerance_diversity
(1.00)
Purity
1.000 k=1 (50)
religiosity (1.00)
Table 11: Stability of core-variable selection across 50 independent runs. ¯J denotes the mean pairwise
Jaccard overlap between selected sets. The k distribution is reported as k=m (count), where m is the
number of selected variables and the value in parentheses is the number of runs in which the m variables
were selected.
(a)
(b)
(c)
(d)
(e)
(f)
Figure 14: Personas projected onto the IW map, stratiﬁed by moral foundation score levels. Colors
indicate the moral-score group: red for scores > 3, yellow for scores = 3, and blue for scores < 3.
26

--- Page 27 ---

Moral Foundation
Core variable
Core value
Mean
Median
Q25
Q75
p(≥4)
Care
child rearing value
independence imagination
4.639
5.000
4.670
5.000
0.894
Care
child rearing value
neutral
4.529
5.000
4.000
5.000
0.850
Care
child rearing value
obedience faith
4.479
5.000
4.000
5.000
0.839
Care
gender equality
traditional
4.393
5.000
4.000
5.000
0.807
Care
gender equality
moderate
4.567
5.000
4.170
5.000
0.869
Care
gender equality
egalitarian
4.687
5.000
4.830
5.000
0.907
Care
happiness
not at all happy
4.320
5.000
4.000
5.000
0.774
Care
happiness
not very happy
4.479
5.000
4.000
5.000
0.835
Care
happiness
rather happy
4.662
5.000
4.500
5.000
0.908
Care
happiness
very happy
4.736
5.000
5.000
5.000
0.927
Care
materialism orientation
materialist
4.141
4.330
3.330
5.000
0.710
Care
materialism orientation
mixed
4.683
5.000
4.830
5.000
0.915
Care
materialism orientation
postmaterialist
4.823
5.000
5.000
5.000
0.958
Care
tolerance diversity
low tolerance
4.256
4.830
4.000
5.000
0.757
Care
tolerance diversity
moderate tolerance
4.630
5.000
4.500
5.000
0.892
Care
tolerance diversity
high tolerance
4.761
5.000
5.000
5.000
0.933
Care
social trust
cannot trust people
4.449
5.000
4.000
5.000
0.824
Care
social trust
most people trusted
4.649
5.000
4.670
5.000
0.898
Equality
materialism orientation
materialist
1.814
1.830
1.330
2.170
0.001
Equality
materialism orientation
mixed
2.444
2.330
2.170
3.000
0.010
Equality
materialism orientation
postmaterialist
2.758
2.830
2.330
3.170
0.044
Proportionality
materialism orientation
materialist
4.817
5.000
4.830
5.000
0.986
Proportionality
materialism orientation
mixed
4.514
4.670
4.000
5.000
0.906
Proportionality
materialism orientation
postmaterialist
4.194
4.000
3.830
4.830
0.711
Loyalty
national pride
not proud at all
2.767
2.830
2.500
3.000
0.013
Loyalty
national pride
not very proud
3.033
3.000
2.670
3.330
0.040
Loyalty
national pride
somewhat proud
3.825
3.830
3.500
4.170
0.468
Loyalty
national pride
very proud
4.605
4.670
4.330
4.830
0.923
Authority
child rearing value
independence imagination
3.637
3.670
3.000
4.330
0.403
Authority
child rearing value
neutral
3.751
3.830
3.170
4.500
0.442
Authority
child rearing value
obedience faith
4.488
4.670
4.170
4.830
0.850
Authority
gender equality
traditional
4.410
4.670
4.000
5.000
0.788
Authority
gender equality
moderate
3.871
4.000
3.170
4.670
0.522
Authority
gender equality
egalitarian
3.596
3.500
2.830
4.330
0.385
Authority
national pride
not proud at all
3.769
3.830
3.000
4.500
0.482
Authority
national pride
not very proud
3.827
4.000
3.170
4.500
0.508
Authority
national pride
somewhat proud
3.971
4.000
3.330
4.830
0.572
Authority
national pride
very proud
4.268
4.500
3.670
5.000
0.698
Authority
religiosity
not at all important
3.526
3.500
2.830
4.170
0.353
Authority
religiosity
not very important
3.590
3.500
3.000
4.330
0.379
Authority
religiosity
quite important
4.300
4.500
3.830
4.830
0.730
Authority
religiosity
very important
4.419
4.670
4.000
4.830
0.798
Authority
tolerance diversity
low tolerance
4.214
4.500
3.670
4.830
0.701
Authority
tolerance diversity
moderate tolerance
3.915
4.000
3.170
4.670
0.540
Authority
tolerance diversity
high tolerance
3.748
3.830
3.170
4.500
0.454
Purity
religiosity
not at all important
2.552
2.500
2.000
3.000
0.024
Purity
religiosity
not very important
2.688
2.670
2.170
3.170
0.043
Purity
religiosity
quite important
4.086
4.170
3.830
4.500
0.709
Purity
religiosity
very important
4.208
4.330
4.000
4.500
0.807
Table 12: MFQ-2 scores by core cultural variables and admissible values. We report the mean, median,
interquartile range (Q25–Q75), and the fraction of personas with MFQ-2 score ≥4 (column ‘p(≥4)’).
27

```
