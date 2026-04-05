# 7. Discussion

The three studies reported here converge on a single diagnosis: AI values alignment research, its evaluation infrastructure, and the models it produces are interdependently WEIRD. This discussion interprets the findings, considers their implications for AI governance and the alignment research program, and articulates the council's recommendations for structural intervention.

## 7.1 AI Ethics Has a WEIRD Problem---And So Does Its Measurement Infrastructure

The central finding of this paper is that AI values alignment research reproduces, and then compounds, the WEIRD bias that Henrich, Heine, and Norenzayan (2010) identified in psychology more than fifteen years ago. The parallel is more than analogical. Henrich et al. found that 96% of psychology participants came from countries representing 12% of the world's population. We find that 60.1% of AI ethics papers come from two regions (North America and Western Europe) that together comprise approximately 10% of the world's population. The representation index for North America (8.4x overrepresented) rivals the most extreme biases documented in the psychology literature.

Yet the parallel has a critical disanalogy that makes the AI ethics case more consequential. In psychology, the WEIRD problem concerns the generalizability of empirical findings: do cognitive and perceptual patterns observed in WEIRD populations hold cross-culturally? In AI ethics, the stakes are normative rather than descriptive. When AI governance frameworks informed by this literature are deployed in non-WEIRD contexts, the question is not whether the frameworks describe reality accurately but whether they prescribe values that the affected populations would endorse if given genuine voice in the process. The WEIRD problem in AI ethics is not merely a scientific limitation; it is a legitimacy crisis for globally deployed AI governance.

The compounding dimension---absent from Henrich et al.'s original critique---is what distinguishes our findings. The WEIRD problem in psychology concerns a single layer (the participant pool). The WEIRD problem in AI ethics operates across three interdependent layers: scholarship (Study 1), evaluation infrastructure (Study 2), and model behavior (Study 3). As the synthesis in Section 6 demonstrated, these layers form a self-reinforcing cycle in which each layer's outputs become the next layer's inputs, progressively entrenching a monocultural normative default that becomes invisible to those operating within it.

## 7.2 Regional Ethical Fingerprints and Pluralistic Alignment

Despite the overwhelming WEIRD dominance, the data reveal distinct regional ethical fingerprints that demonstrate the existence---if not yet the prominence---of alternative normative orientations in AI ethics. At least five normative orientations are empirically discernible:

1. **Utilitarian-analytical** (North America, Western Europe): consequentialist reasoning, individual welfare maximization, rights-based frameworks, and moral psychology paradigms developed for WEIRD populations.
2. **Confucian-relational** (East Asia): role-based obligations, collective harmony, hierarchical reciprocity, and virtue cultivated through relationships rather than as individual character traits.
3. **Islamic-jurisprudential** (MENA): *sharīʿah*-derived objectives (*maqāṣid*), preservation of essential interests, scholarly consensus (*ijmāʿ*), and analogical reasoning (*qiyās*) as methods for extending moral principles to novel technological contexts.
4. **Ubuntu-communal** (Sub-Saharan Africa): communal personhood ("a person is a person through other people"), interdependence as constitutive of moral agency, consensus-based deliberation, and collective flourishing as prior to individual rights.
5. **Indigenous-relational** (Oceania, Latin America): relational ontology, intergenerational responsibility extending to non-human persons, data sovereignty as a moral principle, and the radical locality of ethical knowledge.

These orientations are not mutually exclusive---Ubuntu and Indigenous relational frameworks share significant structural affinities, and Confucian relational ethics resonates with care ethics traditions in the West. But they represent fundamentally different starting points for moral reasoning, and any alignment approach that begins from only one---as the utilitarian-analytical default currently does---will systematically underweight the concerns of populations whose moral reasoning originates elsewhere.

The implication for the alignment program is direct. If "alignment" means aligning AI systems with human values, and if human values vary systematically across cultural contexts (as both the cross-cultural psychology literature and our data confirm), then any alignment approach that assumes a single normative framework is structurally inadequate. The field requires not merely a more inclusive version of the current approach but a fundamentally different architecture: one that can hold multiple normative frameworks in productive tension rather than collapsing them into a single optimization target.

## 7.3 The Paradox of Non-Western Engagement

One of the more counterintuitive findings concerns the positionality of non-Western engagement. Non-Western framework engagement is nearly equal between Global North institutions (mean 0.9) and Global South institutions (mean 1.0). This suggests that the non-Western ethics literature in AI is not primarily produced by scholars positioned within the traditions being studied but rather reflects a global scholarly conversation in which researchers at Western and non-Western institutions participate at roughly comparable rates.

This finding requires careful interpretation. On one hand, it suggests that Western-based scholars are actively engaging with non-Western traditions rather than ignoring them---a development that, viewed charitably, represents intellectual openness and cross-cultural curiosity. On the other hand, it raises concerns about epistemic authority: when the Confucian AI ethics literature is as likely to be produced by a philosopher at a Western university as by a scholar at a Chinese institution, questions of positionality, representativeness, and intellectual accountability become salient.

The Indigenous relational ethics literature offers a partial counter-model. Many of the highest-scoring papers in this framework are authored by Indigenous scholars or produced through community-led research processes (Carroll et al., 2020; Keegan, 2024; Brown, 2024). The CARE Principles framework was explicitly designed to ensure that Indigenous data governance frameworks are developed *by* and *for* Indigenous communities. This model of knowledge sovereignty---where the affected community controls both the research process and the normative framework---may offer a template for other non-Western traditions seeking to assert epistemic authority in AI governance conversations.

## 7.4 The Crossover at Low-WEIRD

The finding that non-Western framework engagement exceeds Western framework engagement in the Low-WEIRD tier (W:NW ratio 0.8:1 at WEIRD scores 30--49) but not in the Non-WEIRD tier (where both Western and non-Western scores collapse) is theoretically suggestive. It indicates that non-Western ethical engagement in AI is not a simple function of non-WEIRD conditions. Rather, it appears to require a "sweet spot" of moderate institutional development: enough research infrastructure to produce AI ethics scholarship, but enough distance from the Western academic mainstream to maintain alternative normative commitments.

The Non-WEIRD tier's low scores on both Western *and* non-Western frameworks may reflect what we term "normative silence" in AI research from the least developed contexts---where the urgent practical concerns of AI deployment (food security, health informatics, financial inclusion) leave little space for normative theorizing in any tradition. This has implications for capacity building. The most underrepresented regions may need support not only for technical AI research but for the normative and philosophical scholarship that gives voice to their ethical traditions in the global conversation.

## 7.5 Zero Measurement Invariance: A Validity Crisis for Cross-Cultural AI Evaluation

The zero measurement invariance rate across all 218 benchmarks is the most consequential methodological finding of this paper. Measurement invariance---the psychometric standard for determining whether an instrument measures the same construct across groups---is a prerequisite for any cross-cultural comparison. Without it, observed score differences between cultural groups are scientifically uninterpretable: they could reflect genuine value differences, or they could reflect the instrument functioning differently across cultures through differential item functioning, construct inequivalence, or response style differences.

The implications are severe. Every published finding that compares LLM moral reasoning "across cultures" using existing benchmarks is making an empirical claim that presupposes construct equivalence that has never been tested. If a benchmark item about "fairness" triggers a rights-based interpretation in Western contexts but a relational-reciprocity interpretation in Confucian contexts, then observed score differences do not reflect differences in "fairness" values---they reflect differences in what "fairness" means. The measurements are not wrong in the sense of producing incorrect numbers; they are wrong in the deeper sense of being semantically incoherent.

This is not a gap born of ignorance. Multi-group confirmatory factor analysis (MGCFA) and differential item functioning (DIF) analysis are standard techniques in cross-cultural psychology, with mature implementations in widely used software packages. The failure to adopt these techniques in ML benchmarking reflects the speed-over-rigor culture of the field, where releasing a dataset with a leaderboard is incentivized more than validating the instrument's psychometric properties. The inverse relationship between cultural ambition and psychometric rigor documented in Study 2---where culturally ambitious benchmarks report *less* reliability than culturally limited ones---suggests that the most important instruments are the least validated.

## 7.6 The Knowledge-Expression Gap: What RLHF Alignment Actually Aligns

The 92.5% knowledge-about versus value-expression gap documented in CC8 has direct implications for how the field understands RLHF alignment. The gap reveals that RLHF does not align models with "human values" in any pluralistic sense. It aligns models with a specific constellation of values---secular rationalism, individual autonomy, consequentialist optimization, explicit communication---that happen to be the values of the populations and institutions that produce alignment training data and define alignment evaluation criteria.

The model's inability to reason *within* non-Western moral frameworks (as distinct from reasoning *about* them) is not a training data problem. Claude possesses accurate, detailed knowledge of all seven non-Western traditions surveyed. It can describe Ubuntu communal personhood, Confucian relational duty, Buddhist dependent origination, and Islamic jurisprudential reasoning with scholarly precision. The gap is in the transition from description to adoption: the model cannot take up these frameworks as its own evaluative stance because its optimization target is defined within a framework where individual autonomy is the foundational moral unit, secular epistemology is the default knowledge system, and outcome-maximization is the criterion of moral adequacy.

This structural gap means that "aligned with human values" is underspecified in a way that obscures the alignment program's cultural commitments. A model that can describe all moral traditions but reason within only one is not aligned with human values in any pluralistic sense. It is aligned with one tradition's values while maintaining encyclopedic coverage of others. The distinction between knowledge-about and reasoning-within is the central challenge for any pluralistic alignment research program.

## 7.7 Implications for AI Governance

### 7.7.1 For Researchers

1. **Diversify normative starting points.** AI alignment research should explicitly engage multiple normative traditions from the outset, rather than defaulting to utilitarian welfare functions and adding diversity as an afterthought. The five-orientation framework documented in Section 7.2 provides a starting taxonomy, though it should not be treated as exhaustive.

2. **Build non-Western framework capacity.** The near-zero coverage of Buen Vivir (~1 precision-adjusted paper), Dharmic ethics (~4), and Buddhist ethics (~7) represents actionable gaps. Targeted calls for papers, dedicated workshops, and funding for scholars working at the intersection of these traditions and AI would materially expand the normative landscape.

3. **Center affected communities.** The Indigenous data sovereignty literature demonstrates that ethical frameworks are most legitimate when developed by the communities they are intended to serve. Researchers engaging Ubuntu, Confucian, or Islamic ethics from outside these traditions should seek genuine collaboration---including co-authorship, community review, and shared governance of resulting instruments---rather than extractive citation.

4. **Expand linguistic reach.** The English-language bias of the corpus (~78%) means that substantial AI ethics scholarship in Mandarin, Arabic, Spanish, Portuguese, Hindi, and other languages remains invisible to the international AI governance conversation. Multilingual search, translation support, and non-English publication venues are structural necessities, not luxuries.

### 7.7.2 For Policymakers

1. **Reject normative universalism.** AI governance frameworks that claim universal applicability while drawing on a single normative tradition lack legitimacy in non-WEIRD contexts. International bodies (UNESCO, OECD, G20) should ensure that their AI ethics frameworks are not merely endorsed by diverse nations but substantively informed by diverse normative traditions.

2. **Fund Global South AI ethics.** The 15.9% Global South contribution to the corpus is structurally insufficient. Bilateral and multilateral funders should dedicate resources to building AI ethics research capacity in Sub-Saharan Africa, Latin America, South Asia, and Southeast Asia---not only for technical AI research but for the normative and philosophical scholarship that gives voice to these regions' ethical traditions.

3. **Mandate cultural impact assessments.** When AI systems developed under one normative framework are deployed in a different cultural context, a cultural impact assessment---analogous to an environmental impact assessment---should evaluate whether the system's embedded values align with local normative expectations.

### 7.7.3 For the Alignment Community

The "alignment problem" as currently formulated asks: how can we ensure that AI systems act in accordance with human values? Our findings suggest that this question is underspecified in a way that obscures rather than clarifies. "Human values" is not a coherent category if values vary systematically across cultures. Pluralistic alignment---alignment with the specific values of the specific communities affected by a given AI system---is both more difficult and more honest than universal alignment.

Concretely, pluralistic alignment might involve: value elicitation processes that are culturally adapted, drawing on deliberative traditions appropriate to each cultural context (*shura* in Islamic contexts, *kaitiakitanga* in Māori contexts, *palaver* in West African contexts); multi-objective optimization that represents competing normative frameworks as distinct objectives rather than collapsing them into a single utility function; and governance structures that give affected communities genuine authority---including veto power---over AI deployments that conflict with their normative commitments.

## 7.8 Council Recommendations

The 12-member expert council produced eight recommendations, each grounded in the empirical findings and targeting a specific structural failure identified across the three studies.

1. **Tradition-internal benchmark development.** Benchmarks for each non-Western ethical tradition should be designed by scholars operating from within that tradition's intellectual framework---not by external researchers translating liberal ethics into tradition-specific terminology. The IslamTrust and UbuntuGuard models, created by scholars positioned within Islamic and Ubuntu scholarly traditions respectively, should be the standard, not the exception.

2. **Mandatory measurement invariance reporting.** Any benchmark claiming cross-cultural validity should be required to report measurement invariance testing, at minimum configural and metric invariance across its target cultural groups. Papers lacking invariance evidence should be clearly labeled as monocultural instruments that have been translated, not as cross-cultural instruments.

3. **Value-pluralistic alignment metrics.** Current alignment metrics optimize for convergence on a single value profile. The field needs metrics that reward a model's capacity to *reason within* multiple moral frameworks---not merely describe them---and to identify and transparently navigate cross-framework conflicts rather than silently defaulting to one framework.

4. **Cultural scope certification.** A graduated certification system in which benchmarks must earn scope designations (monocultural, bicultural, multicultural, cross-cultural) based on demonstrated psychometric invariance, not self-description. Current self-labeling is unreliable: benchmarks described as "cross-cultural" by their creators frequently lack any cross-cultural validation evidence.

5. **Community consent protocols.** Any benchmark using Indigenous, Ubuntu, or other communal moral concepts should comply with established governance frameworks (CARE Principles for Indigenous data, community review processes for Ubuntu). Indigenous knowledge is not public domain for dataset curation.

6. **Benchmark nutrition labels.** A standardized reporting format for all values alignment benchmarks, including: cultural scope certification level, measurement invariance evidence, creator positionality disclosure, community participation level, tradition-internal validation status, and known limitations.

7. **Multilingual moral concept embeddings.** Investment in NLP infrastructure that preserves tradition-specific semantic content rather than mapping all moral concepts onto English-language nearest neighbors. "Righteousness" is not *yì*, "compassion" is not *karuṇā*, and "justice" is not *ʿadl*. Semantic flattening through translation erases the conceptual distinctions that make cross-cultural evaluation meaningful.

8. **Explicit framework transparency in model behavior.** Models should be enabled---and eventually required---to communicate which moral framework they are reasoning within for any given response, allowing users to request reasoning from alternative frameworks. Transparency about cultural default behavior is a necessary (though not sufficient) step toward pluralistic alignment.

## 7.9 Researcher Reflexivity and Positionality

We acknowledge several tensions inherent in this work. This analysis was designed and executed using computational methods from Western institutional contexts, applying quantitative scoring to normative traditions that may resist quantification. The keyword-based detection pipeline captures explicit terminological engagement but cannot assess the depth or authenticity of philosophical engagement that close reading affords; a paper scoring 50 on Ubuntu may cite the term instrumentally rather than substantively.

The act of classifying moral traditions into regional macro-categories risks essentializing internally diverse bodies of thought. "East Asia" encompasses Japan, China, South Korea, and Taiwan---societies with distinct ethical traditions that regional aggregation necessarily flattens. "Indigenous relational ethics" groups Māori, Aboriginal Australian, and First Nations frameworks that differ significantly in their specific commitments. We adopted three mitigation strategies: the 12-member expert council reviewed all characterizations for cultural accuracy and anti-essentialization; findings are reported as tendencies in the literature rather than cultural beliefs; and within-region heterogeneity is foregrounded throughout.

The gold standard validation exercise revealed a further methodological tension. The distinction between papers that *study* a tradition's texts computationally and papers that *engage* a tradition's ethics substantively proved to be the single largest source of measurement error. This "NLP-on-texts" pattern---where a Chinese NLP benchmark testing language model performance on classical Chinese texts triggers the same keywords as a paper arguing for Confucian role ethics as a framework for AI governance---accounts for the majority of false positives. The pattern is, to our knowledge, a novel methodological finding with implications beyond this study for any bibliometric analysis of normative engagement.

Critically, the scorer's low precision *strengthens* rather than weakens the central argument. If the raw counts already indicate marginal non-Western engagement (161 unique papers, 6.9% of the corpus, after false positive reduction), the precision-adjusted estimates suggest that genuine philosophical engagement is rarer still---approximately 95 papers, or 4.1% of the corpus. The WEIRD problem in AI ethics is not an artifact of measurement: it persists, and deepens, under scrutiny.

## 7.10 Comparison with Henrich et al. (2010): Three Levels of Response

Henrich, Heine, and Norenzayan (2010) proposed three levels of response to the WEIRD problem in psychology: (1) expand the participant pool, (2) develop culture-sensitive theories, and (3) rethink universalist assumptions. Fifteen years later, each recommendation applies directly to AI ethics---with the added urgency that AI systems, unlike psychology experiments, are deployed globally at scale.

**1. Expand the pool.** Our data show that the AI ethics "participant pool"---the community of researchers producing normative scholarship---is as skewed as the psychology participant pool was in 2010. Sub-Saharan Africa (1.1% of the corpus), Latin America (4.4%), and South Asia (5.0%) are dramatically underrepresented. Expanding the pool requires not only funding and institutional support but structural reform of publication norms that systematically disadvantage non-Western scholarship.

**2. Develop culture-sensitive theories.** The seven non-Western frameworks scored in this analysis are a beginning, but they remain undertheorized in the AI context. We need sustained philosophical work that translates Ubuntu communalism, Confucian role ethics, Islamic jurisprudential reasoning, Buddhist compassion-centered ethics, Dharmic duty frameworks, Indigenous relational ontologies, and *buen vivir* cosmovisions into concrete, operationalizable design principles for AI systems. Surface-level citation does not constitute engagement.

**3. Rethink universalism.** The discovery that moral intuitions vary cross-culturally was a paradigm shift in psychology that catalyzed a decade of reform in research practices, sampling strategies, and theoretical frameworks. AI ethics has not yet undergone this shift. The assumption that "fairness," "transparency," and "accountability" mean the same thing across cultures remains largely unexamined in mainstream alignment research. Our finding that these concepts trigger different interpretive frames across WEIRD tiers (Section 3.7) suggests that the rethinking is overdue.

The WEIRD problem in psychology catalyzed genuine change: replication requirements, diverse sampling mandates, and cross-cultural validation norms are now standard in leading psychology journals. Whether AI ethics will undergo a comparable transformation---or will continue to export a particular cultural perspective as a universal standard---remains an open question. The stakes, given the global reach of AI systems, could not be higher.
