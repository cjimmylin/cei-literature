# 8. Discussion

## 8.1 AI Ethics Has a WEIRD Problem

The central finding of this study is that AI values alignment research reproduces, almost exactly, the WEIRD bias that Henrich, Heine, and Norenzayan (2010) identified in psychology. With a mean WEIRD score of 64.5/100, 59.7% of papers in the High-WEIRD tier, and 60.1% of author affiliations concentrated in North America and Western Europe, the academic literature that informs AI governance frameworks is produced by and for a narrow slice of humanity.

The parallel to psychology is more than analogical. Henrich et al. found that 96% of psychology participants came from countries representing 12% of the world's population. We find that 60.1% of AI ethics papers come from two regions (North America and Western Europe) that together comprise roughly 10% of the world's population. The representation index for North America (8.4x overrepresented) rivals the most extreme biases documented in psychology.

Yet there is an important disanalogy. In psychology, the WEIRD problem concerns the generalizability of empirical findings: do cognitive and perceptual patterns observed in WEIRD populations hold cross-culturally? In AI ethics, the stakes are normative rather than descriptive. When AI governance frameworks informed by this literature are deployed in non-WEIRD contexts, the question is not whether the frameworks describe reality accurately but whether they prescribe values that the affected populations would endorse if given genuine voice in the process.

## 8.2 Regional Ethical Fingerprints and Pluralistic Alignment

The regional ethical fingerprints documented in Section 4 have direct implications for AI values alignment. If alignment means aligning AI systems with human values, and if human values vary systematically across cultural contexts, then any alignment approach that assumes a single normative framework is structurally inadequate.

The data suggest at least five distinct normative orientations:

1. **Utilitarian-analytical** (North America, Western Europe): Consequentialist reasoning, individual welfare maximization, rights-based frameworks, moral psychology paradigms.
2. **Confucian-relational** (East Asia): Role-based obligations, collective harmony, hierarchical reciprocity, virtue through relationships.
3. **Islamic-jurisprudential** (MENA): Shariah-derived objectives, preservation of essential interests, scholarly consensus (*ijma*), analogical reasoning (*qiyas*).
4. **Ubuntu-communal** (Sub-Saharan Africa): Communal personhood, interdependence, consensus, collective flourishing over individual rights.
5. **Indigenous-relational** (Oceania, Latin America): Relational ontology, intergenerational responsibility, non-human moral standing, data sovereignty.

These orientations are not mutually exclusive, and substantial overlap exists (particularly between Ubuntu and Indigenous relational frameworks). But they represent fundamentally different starting points for moral reasoning, and any alignment approach that begins from only one---as most current approaches do with utilitarianism---will systematically underweight the concerns of populations whose moral reasoning begins elsewhere.

## 8.3 The Paradox of Non-Western Engagement

One of the more counterintuitive findings is that non-Western framework engagement is nearly equal between the Global North (mean 0.9) and the Global South (mean 1.0). This suggests that the non-Western ethics literature in AI is not primarily produced by scholars *within* the traditions being studied but rather reflects a global scholarly conversation in which Western-based and non-Western-based researchers participate roughly equally.

This finding should be interpreted carefully. On one hand, it suggests that Western-based scholars are actively engaging with non-Western traditions rather than ignoring them---a positive development. On the other hand, it raises concerns about epistemic authority: when the Confucian AI ethics literature is as likely to be produced by a philosopher at a Western university as by a scholar at a Chinese institution, questions of positionality and representativeness become salient.

The Indigenous relational ethics literature offers a partial counter-example. Many of the highest-scoring papers in this framework are authored by Indigenous scholars or produced through community-led research processes (Carroll et al. 2020; Keegan 2024; Brown 2024). The CARE Principles framework was explicitly designed to ensure that Indigenous data governance frameworks are developed *by* and *for* Indigenous communities. This model of knowledge sovereignty---where the affected community controls both the research process and the normative framework---may offer a template for other non-Western traditions seeking to assert their voice in AI governance.

## 8.4 The Crossover at Low-WEIRD

The finding that non-Western framework engagement exceeds Western framework engagement in the Low-WEIRD tier (ratio 0.8:1 at WEIRD scores 30--49) but not in the Non-WEIRD tier (ratio 2.2:1 at WEIRD scores 0--29) is theoretically interesting. It suggests that non-Western ethical engagement in AI is not a simple function of non-WEIRD conditions. Rather, it appears to require a "sweet spot" of moderate development and intellectual infrastructure---enough institutional capacity to produce AI ethics scholarship, but enough distance from the Western academic mainstream to maintain alternative normative commitments.

The Non-WEIRD tier's low scores on both Western and non-Western frameworks may reflect a "normative silence" in AI research from the least developed contexts, where the urgent practical concerns of AI deployment (food security, health informatics, financial inclusion) leave little space for normative theorizing in any tradition. This has implications for targeted research capacity building: the most underrepresented regions may need support not only for technical AI research but for the normative and philosophical scholarship that gives voice to their ethical traditions in the global conversation.

## 8.5 Implications for AI Governance

### 8.5.1 For Researchers

1. **Diversify normative starting points.** AI alignment research should explicitly engage multiple normative traditions from the outset, rather than defaulting to utilitarian welfare functions and adding diversity as an afterthought. The five-orientation framework outlined in Section 8.2 provides a starting taxonomy.

2. **Build non-Western framework capacity.** The near-zero coverage of Buen vivir (8 raw detections, adj. ~1), Dharmic ethics (18 raw, adj. ~4), and Buddhist ethics (22 raw, adj. ~7) represents actionable gaps. Targeted calls for papers, dedicated workshops, and funding for scholars working at the intersection of these traditions and AI would materially expand the normative landscape.

3. **Center affected communities.** The Indigenous data sovereignty literature demonstrates that ethical frameworks are most legitimate when developed by the communities they are intended to serve. Researchers engaging Ubuntu, Confucian, or Islamic ethics from outside these traditions should seek co-authorship and genuine collaboration rather than extractive citation.

4. **Expand linguistic reach.** The English-language bias of the corpus (approximately 78%) means that substantial AI ethics scholarship in Mandarin, Arabic, Spanish, Portuguese, Hindi, and other languages is invisible to this analysis and, likely, to the international AI governance conversation.

### 8.5.2 For Policymakers

1. **Reject normative universalism.** AI governance frameworks that claim universal applicability while drawing on a single normative tradition lack legitimacy in non-WEIRD contexts. International bodies (UNESCO, OECD, G20) should ensure that their AI ethics frameworks are not merely endorsed by diverse nations but substantively informed by diverse normative traditions.

2. **Fund Global South AI ethics.** The 15.9% Global South contribution to the corpus is structurally insufficient. Bilateral and multilateral funders should dedicate resources to building AI ethics research capacity in Sub-Saharan Africa, Latin America, South Asia, and Southeast Asia.

3. **Mandate cultural impact assessments.** When AI systems developed under one normative framework are deployed in a different cultural context, a cultural impact assessment---analogous to an environmental impact assessment---should evaluate whether the system's embedded values align with local normative expectations.

### 8.5.3 For the Alignment Community

The "alignment problem" as currently formulated (Russell 2019) asks: how can we ensure that AI systems act in accordance with human values? Our findings suggest that this question is underspecified. "Human values" is not a coherent category if values vary systematically across cultures. Pluralistic alignment---alignment with the specific values of the specific communities affected by a given AI system---is both more difficult and more honest than universal alignment.

Concretely, pluralistic alignment might involve:
- Value elicitation processes that are culturally adapted, drawing on deliberative traditions appropriate to the cultural context (e.g., *shura* in Islamic contexts, *kaitiakitanga* in Maori contexts, *palaver* in West African contexts)
- Multi-objective optimization that represents competing normative frameworks as distinct objectives rather than collapsing them into a single utility function
- Governance structures that give affected communities genuine veto power over AI deployments that conflict with their normative commitments

## 8.6 Researcher Reflexivity

We acknowledge several tensions inherent in this work. This analysis was designed and executed using computational methods from a Western institutional context, applying quantitative scoring to normative traditions that may resist quantification. The keyword-based detection pipeline captures explicit terminological engagement but cannot assess the depth or authenticity of philosophical engagement that close reading affords; a paper scoring 50 on Ubuntu may cite the term instrumentally rather than substantively.

The act of classifying cultures into regional macro-categories risks essentializing internally diverse traditions. "East Asia" encompasses Japan, China, South Korea, and Taiwan---societies with distinct ethical traditions that our regional aggregation necessarily flattens. Similarly, "Indigenous relational ethics" groups Maori, Aboriginal Australian, and First Nations frameworks that differ significantly in their specific commitments.

We adopted three mitigation strategies. First, the 20-member expert council---spanning 10 world regions and including tradition-specific specialists---reviewed all characterizations for cultural accuracy and anti-essentialization. Second, we report findings as tendencies in the literature rather than cultural beliefs. Third, we foreground limitations: our English-language corpus (approximately 78%) structurally underrepresents scholarship in Mandarin, Arabic, Spanish, and other languages where substantial AI ethics work exists, as documented in Minority Report B of the council deliberations. The quantification tension for Indigenous and Buen vivir traditions---where holistic cosmovisions resist dimensional decomposition---was flagged in Minority Report A and remains an unresolved methodological challenge.

The gold standard validation exercise (Section 3.2.3) revealed a further methodological tension. The distinction between papers that *study* a tradition's texts computationally and papers that *engage* a tradition's ethics substantively proved to be the single largest source of measurement error. A Chinese NLP benchmark that tests language model performance on classical Chinese texts triggers the same keywords as a paper that argues for Confucian role ethics as a framework for AI governance. This NLP-on-texts pattern accounts for the majority of false positives across all seven frameworks, with the notable exception of Islamic ethics, whose keywords are more tightly coupled to ethical and legal reasoning.

Critically, the low precision of our scorer *strengthens* rather than weakens our central argument. If the raw counts already indicate marginal non-Western engagement (161 unique papers, 6.9% of the corpus, after scorer improvement to reduce false positives), the precision-adjusted estimates suggest that genuine philosophical engagement is rarer still---approximately 95 papers, or 4.1% of the corpus. The WEIRD problem in AI ethics is not an artifact of measurement: it persists, and deepens, under scrutiny.

## 8.7 Comparison with Henrich et al.

Henrich, Heine, and Norenzayan (2010) proposed three levels of response to the WEIRD problem: (1) expand the participant pool, (2) develop culture-sensitive theories, and (3) rethink universalist assumptions. Fifteen years later, each of these recommendations applies directly to AI ethics:

1. **Expand the pool.** Our data show that the AI ethics "participant pool"---the community of researchers producing normative scholarship---is as skewed as the psychology participant pool was in 2010. Sub-Saharan Africa (1.1%), Latin America (4.4%), and South Asia (5.0%) are dramatically underrepresented.

2. **Develop culture-sensitive theories.** The seven non-Western frameworks scored in this analysis are a start, but they remain undertheorized in the AI context. We need sustained philosophical work that translates Ubuntu, Confucian, Islamic, Buddhist, Dharmic, Indigenous, and *buen vivir* ethics into concrete design principles for AI systems.

3. **Rethink universalism.** The discovery that moral intuitions vary cross-culturally was a paradigm shift in psychology. AI ethics has not yet undergone this shift. The assumption that "fairness," "transparency," and "accountability" mean the same thing across cultures remains largely unexamined in mainstream alignment research.
