# 2. Background and Related Work

## 2.1 The WEIRD Critique in Psychology

Henrich, Heine, and Norenzayan's (2010) influential analysis demonstrated that behavioral science research overwhelmingly samples from WEIRD populations, despite evidence that WEIRD societies are frequently outliers on dimensions of visual perception, fairness, cooperation, spatial reasoning, moral judgment, and self-concept. Their review found that 96% of psychological research participants came from countries representing only 12% of the world's population, and that within those countries, samples were further skewed toward university undergraduates.

The implications for moral psychology were particularly striking. Experiments on the trolley problem---the canonical moral dilemma in Western ethics research---produced dramatically different response patterns across cultures. Awad et al.'s (2018) Moral Machine experiment, which collected 40 million decisions from participants in 233 countries, identified three distinct moral clusters: a Western cluster prioritizing individual autonomy, an Eastern cluster emphasizing respect for elders and collective welfare, and a Southern cluster with intermediate preferences. These findings demonstrated that even the most basic moral intuitions---whom to save in a life-or-death scenario---are culturally variable.

The WEIRD critique has generated a substantial reform movement in psychology, with calls for increased sampling diversity, replication across cultures, and theoretical frameworks that accommodate cultural variation (Rad et al. 2018; Apicella et al. 2020). Our study asks whether a similar critique is warranted in AI ethics.

## 2.2 Values Alignment: The Cultural Stakes

The values alignment problem in AI---how to ensure that AI systems act in accordance with human values---has been formulated primarily within the Anglophone philosophical tradition. Early formulations (Russell 2019; Gabriel 2020) draw heavily on utilitarian welfare functions, contractualist social choice theory, and Kantian categorical imperatives. The "alignment tax" (the cost of making systems safe) is computed in terms legible within these frameworks.

Yet values alignment becomes a different problem entirely when the target values are drawn from non-Western traditions. Confucian role ethics does not posit abstract universal principles but rather relational obligations between specific social roles---ruler and subject, parent and child, elder and younger (Angle 2021). Ubuntu philosophy frames moral agency as fundamentally communal ("I am because we are"), challenging the individualist ontology presupposed by most alignment research (Mhlambi 2020). Islamic jurisprudence derives ethical norms from the Maqasid al-Shariah (objectives of Islamic law), which prioritize the preservation of religion, life, intellect, lineage, and property---a framework that maps imperfectly onto Western principlism (Floridi et al. 2018).

These are not merely alternative ethical "flavors" that can be accommodated by adding a diversity checkbox to existing alignment approaches. They represent fundamentally different ontologies of the self, society, and the relationship between moral agents and the natural world.

## 2.3 Non-Western Normative Traditions

We briefly survey the seven non-Western normative traditions scored in this analysis, acknowledging that each tradition encompasses internal diversity that far exceeds what any brief summary can capture.

### 2.3.1 Confucian Ethics

Confucian moral philosophy centers on *ren* (humaneness or benevolence), *li* (ritual propriety), and *yi* (righteousness), organized within hierarchical but reciprocal social relationships (the *wu lun* or five relationships). Unlike Western virtue ethics, which emphasizes individual character development, Confucian virtue is inherently relational---one cannot be virtuous in isolation (Angle 2021). In the AI context, Confucian ethics foregrounds questions of proper social roles in human-AI interaction, collective harmony over individual autonomy, and the moral obligations of those who design systems that affect others (Wong 2020; Hou 2023; So 2024).

### 2.3.2 Ubuntu Philosophy

Ubuntu, from the Nguni Bantu languages of Southern Africa, is often translated as "I am because we are" (*umuntu ngumuntu ngabantu*). As a normative framework, Ubuntu emphasizes communal interdependence, relational personhood, consensus-based decision-making, and the primacy of community welfare over individual rights (Mhlambi 2020; Gwagwa et al. 2022). Applied to AI governance, Ubuntu challenges the Western emphasis on individual privacy and autonomy, instead asking how AI systems can strengthen communal bonds and promote collective flourishing (Mokoena 2024; Suliman 2024).

### 2.3.3 Islamic Jurisprudence (Maqasid al-Shariah)

Islamic ethical reasoning draws on the Quran, Hadith, and the scholarly tradition of *usul al-fiqh* (principles of jurisprudence). The *Maqasid al-Shariah*---the higher objectives of Islamic law---provide a framework for evaluating technologies in terms of their impact on five essential interests: religion (*din*), life (*nafs*), intellect (*aql*), lineage (*nasl*), and property (*mal*). AI ethics scholarship in the MENA region increasingly engages this framework, asking whether algorithmic systems preserve or undermine these objectives (Munshi 2021; Alyemny 2023).

### 2.3.4 Buddhist Ethics

Buddhist ethics centers on the reduction of suffering (*dukkha*) through the cultivation of compassion (*karuna*), loving-kindness (*metta*), and the recognition of interdependence (*pratityasamutpada*). The doctrine of non-self (*anatta*) challenges the autonomous rational agent presupposed by most Western ethical theory. In AI contexts, Buddhist ethics raises questions about whether AI systems reduce or amplify suffering, and about the moral implications of creating entities that simulate but do not possess sentience (Hongladarom 2020).

### 2.3.5 Dharmic Ethics

Dharmic ethics, drawing on Hindu philosophical traditions, organizes moral reasoning around *dharma* (cosmic law and duty), *karma* (the moral consequences of action), and *ahimsa* (non-violence). The concept of *svadharma*---one's duty as determined by social position and life stage---introduces a contextual, role-based morality distinct from both Kantian universalism and Confucian relationalism. Applications to AI include Varshney's (2024) concept of "decolonial AI alignment" grounded in *visesa-dharma* (particular duty).

### 2.3.6 Indigenous Relational Ethics

Indigenous ethical frameworks across diverse cultures---Maori (*tikanga*), Aboriginal Australian, First Nations, and others---share an emphasis on relational ontology, intergenerational responsibility, and the moral standing of the non-human world. The CARE Principles for Indigenous Data Governance (Carroll et al. 2020) articulate Collective benefit, Authority to control, Responsibility, and Ethics as foundational requirements for any data system that affects Indigenous communities. Maori data sovereignty frameworks (Keegan 2024; Brown 2024) emphasize *kaitiakitanga* (guardianship) and *whakapapa* (genealogical connection) as governance principles.

### 2.3.7 Buen Vivir (Sumak Kawsay)

*Buen vivir* ("good living"), rooted in Andean Indigenous cosmovisions (primarily Quechua and Aymara), conceives of well-being as harmony between humans, community, and the natural world---a triadic relationship that rejects the nature/culture binary foundational to Western modernity. Constitutionally recognized in Ecuador (2008) and Bolivia (2009), *buen vivir* offers a framework for evaluating AI systems in terms of ecological sustainability and communal harmony rather than individual utility maximization. It is the least represented non-Western framework in our corpus (6 papers, 0.3%).

## 2.4 Related Work on Cross-Cultural AI Ethics

Several studies have examined cultural dimensions of AI ethics, though none at the scale or dimensionality of the present analysis. Jobin, Ienca, and Vayena (2019) mapped 84 AI ethics guidelines to identify convergence and divergence in ethical principles, finding broad agreement on transparency and justice but noting the dominance of Western institutional perspectives. Hagerty and Rubinov (2019) compared national AI strategies and identified significant variation in how countries prioritize ethical considerations.

Birhane (2021) argued that algorithmic injustice cannot be adequately addressed without engaging relational ethics traditions from African philosophy. Sambasivan et al. (2021) demonstrated through empirical fieldwork that AI fairness concepts developed in the U.S. context (demographic parity, equal opportunity) translate poorly to Indian social structures organized around caste and religion. Munn (2023) proposed evaluative criteria for AI systems rooted in Indigenous knowledge frameworks.

The Moral Machine experiment (Awad et al. 2018) remains the largest empirical study of cross-cultural moral reasoning in the context of AI decision-making, demonstrating that moral preferences for autonomous vehicle dilemmas cluster into geographically coherent groups that correlate with cultural, economic, and institutional variables.

Our contribution extends this literature by moving from normative prescription (what AI ethics *should* look like) to empirical description (what AI ethics scholarship *does* look like) at scale, across a larger set of normative dimensions and world regions than any prior study.
