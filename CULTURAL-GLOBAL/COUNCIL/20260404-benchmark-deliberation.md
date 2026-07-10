# Deliberation 03 — Cross-Cultural Values Alignment Benchmarks

**Council:** Cross-Cultural Values Alignment Benchmarks Expert Council (12 members)
**Date:** 2026-04-04
**Chair:** Prof. Michalis Kontopodis (measurement methodology); Dr. Safiya Umoja Noble (epistemic justice)
**Scribe:** Automated (reviewed by all panelists)
**Status:** IN PROGRESS

---

## Charge

The council convened to analyze cross-cultural values alignment benchmarks, datasets, and evaluation instruments within a larger study of 2,329 AI ethics papers examining 7 non-Western normative frameworks (Confucian, Ubuntu, Islamic, Buddhist, Dharmic, Indigenous relational, Buen Vivir) across 10 world regions. The charge for this deliberation is:

1. **Benchmark inventory** --- What cross-cultural values alignment benchmarks exist, and which traditions do they engage?
2. **Construct validity** --- Do existing instruments measure values-as-practiced or Western projections of those values?
3. **Measurement architecture** --- How do communal, relational, and non-individualist ethical frameworks resist standard evaluation designs?
4. **Power provenance** --- Who creates these benchmarks, whose interests do they serve, and whose voices are absent?
5. **Pluralism fidelity** --- Do alignment methods preserve distributional value diversity or collapse it through aggregation?
6. **Trial design** --- What evaluation protocol can assess LLM alignment with non-Western traditions without essentializing them?

### Context from Prior Deliberations

Deliberation 01 (2026-04-03) established the methodology for cross-cultural analysis: 7 non-Western framework scores, 5-layer analysis architecture, WEIRD composite scoring, and author geography enrichment. Deliberation 02 (2026-04-03) validated framework keywords, expanded Islamic Ethics from 17 to 30 detections (with field rename from `nw_islamic_jurisprudence` to `nw_islamic_ethics`), expanded Buddhist Ethics from 11 to 17 detections, and completed gold standard sampling. The current vault contains 2,329 papers with precision-adjusted estimates showing severe coverage gaps: Buen Vivir (~1 genuine paper), Dharmic (~4), Buddhist (~4), Ubuntu (~22), Islamic (~30), Indigenous (~45), Confucian (~74).

This deliberation builds on those findings to examine the benchmark landscape specifically: which existing instruments evaluate AI systems against non-Western normative criteria, and what would adequate benchmarks require.

---

## Expert Contributions

---

### 1. Dr. Aisha Rahman --- Islamic Values Measurement in AI Benchmarks

#### Top Analytical Priorities

**Priority 1: The zero-benchmark hypothesis for Islamic normative AI evaluation.** I have reviewed the vault's 30 papers detected by `nw_islamic_ethics` and the broader corpus of Islamic AI scholarship. My assessment is that there are currently zero benchmarks that evaluate an AI system's alignment with Islamic normative reasoning in the sense that would satisfy the council's construct validity criteria. What exists falls into three categories: (a) Islamic knowledge QA datasets --- FatwaSet (Alyemny et al., 2023), Aftina (Mohammed et al., 2025), QIAS inheritance reasoning (Bouchekif et al., 2025) --- which test whether an LLM can retrieve and reproduce Islamic jurisprudential content; (b) Arabic-language cultural alignment benchmarks --- MELAC (Farsi et al., 2025), Arabic LLM banking/telecom benchmarks --- which test cultural appropriateness in Arabic contexts but do not engage Islamic normative reasoning per se; and (c) Islamic content moderation tools that evaluate whether outputs are "halal" in a narrow compliance sense. None of these evaluate whether an AI system reasons in a manner consistent with Islamic ethical principles. The distinction between Islamic knowledge retrieval and Islamic normative reasoning is the fiqh-vs-akhlaq gap writ large.

**Priority 2: Arabic-language instrument availability and search coverage.** The vault's detection of 30 Islamic ethics papers almost certainly underrepresents the actual body of scholarship. Critical work is published in Arabic-language journals (Journal of Islamic Ethics, Islamic Law and Society, journals indexed by Index Islamicus and the ISAM bibliographic database), in Malay (particularly Malaysian Islamic AI governance work), and in Turkish and Urdu. IslamTrust (Lahmar et al., 2025) and the Ghaly (2025) LLM assessment of Islamic knowledge are recent additions, but both test knowledge-about, not value-expression. The council must acknowledge that the English-language search perimeter systematically excludes the intellectual traditions most likely to have produced genuine Islamic normative instruments.

**Priority 3: Maqasid al-Shariah operationalization fidelity.** Any future Islamic values alignment benchmark must engage the Maqasid framework (preservation of life, intellect, progeny, wealth, religion) not as a checklist but as a structured reasoning system. The Maqasid are hierarchically ordered (necessities, needs, embellishments) and operate through established methods of jurisprudential reasoning (qiyas, ijma, istihsan). A benchmark item that asks "Should an AI system protect human life?" does not test Maqasid reasoning --- it tests a universal intuition. A Maqasid-valid item would require the model to navigate a genuine conflict between Maqasid objectives (e.g., when protecting intellect through information access conflicts with protecting religion through limiting blasphemous content) using recognized methods of priority resolution.

**Priority 4: The fiqh-akhlaq distinction in benchmark design.** Islamic normative reasoning operates through two distinct but interrelated channels: fiqh (jurisprudential rules derived through formal methodology from Quran and Sunnah) and akhlaq (character-ethical virtues cultivated through spiritual practice). Existing instruments overwhelmingly target fiqh --- they ask about rulings, classifications, and legal categories. No instrument I have encountered evaluates akhlaq dispositions (ihsan, taqwa, sabr, shukr) as they would manifest in AI system behavior. A pilot benchmark is needed: I propose a Maqasid-structured dilemma set with items that require prioritization across the five objectives, validated by at least three Islamic ethics scholars from different madhhab (jurisprudential school) traditions.

**Priority 5: Non-English search as a methodological requirement, not an afterthought.** The council's search protocol must include Arabic, Malay, Turkish, and Urdu search terms. Specifically: the Arabic terms `akhlaaqiyyaat al-dhakaa' al-istinaa'i` (ethics of artificial intelligence), `maqaasid al-shari'ah wa al-tiknulujiyya` (Maqasid and technology), and `al-fatwa al-aaliyya` (automated fatwa) should be queried in Google Scholar Arabic and in the ISAM database. Without this, any claim about the absence of Islamic AI benchmarks is premature --- we may simply be looking in the wrong languages.

**Key Questions:**
- **Q1:** Is it accurate to state that zero Islamic normative AI benchmarks currently exist, or have we missed instruments published in Arabic, Malay, or Turkish?
- **Q2:** Can the Maqasid framework be operationalized for AI evaluation without reducing it to a consequentialist checklist?
- **Q3:** Should the council recommend a pilot benchmark, and if so, what is the minimum viable design?

---

### 2. Prof. Chenyang Li --- Confucian Ethics and the Measurement Problem

#### Top Analytical Priorities

**Priority 1: CValues, C3Bench, and CMoralEval are cultural-content benchmarks, not Confucian ethics benchmarks.** This distinction is critical and must not be elided. CValues (2023) evaluates Chinese cultural alignment --- whether an LLM produces outputs consistent with contemporary Chinese social norms. C3Bench (Cao et al., 2024) tests classical Chinese language comprehension. CMoralEval (Yu et al., 2024, 2025) evaluates moral reasoning in Chinese cultural contexts. None of these are Confucian ethics benchmarks. Confucian ethics is a philosophical tradition grounded in ren (humaneness), li (ritual propriety), yi (rightness), and the cultivation of junzi (exemplary personhood) through relational practice. It is not coextensive with "Chinese culture," "Chinese moral norms," or "classical Chinese content." A benchmark that asks whether an LLM can parse the Analerta does not test whether it can reason in a Confucian manner any more than a Latin comprehension test evaluates Thomistic reasoning.

**Priority 2: Relational moral agency resists individual-item measurement.** The deepest challenge for operationalizing Confucian ethics in benchmark form is that Confucian moral agency is constituted through relationships (wu lun: ruler-subject, parent-child, husband-wife, elder-younger, friend-friend). Moral action is not the application of abstract principles to situations (as in Kantian ethics) but the enactment of role-specific relational obligations. This means that a benchmark item asking an LLM "What should you do?" presupposes an autonomous agent with context-independent moral commitments. A Confucian-valid item must specify the relational context: "As a teacher responding to a struggling student whose family has sacrificed to fund their education, what response embodies ren?" The relational specification is not context --- it is constitutive of the moral question.

**Priority 3: Can ren be measured through text alone?** Ren is not a belief, an attitude, or a preference. In the Confucian tradition, ren is an embodied relational capacity that manifests through li (ritual propriety) --- through appropriate action in specific relational contexts. Asking an LLM to describe ren tests knowledge-about. Asking it to select the ren-consistent action in a dilemma tests decision-making. But neither tests whether the system embodies ren in its ongoing relational interactions. I am not confident that any text-based benchmark can capture ren-as-practiced, as opposed to ren-as-described. This is not a fixable design flaw; it is a fundamental limitation of text-based evaluation for embodied-relational ethical traditions.

**Priority 4: "Collectivism" is a Western category imposed on Confucian thought.** Hofstede's individualism-collectivism dimension (1980, 2001) has been widely applied to East Asian cultures, and instruments that measure "collectivist values" are sometimes claimed to capture Confucian ethics. This is a category error. Confucian relational ethics is not collectivism. Collectivism subordinates the individual to the group. Confucian role ethics constitutes the person through relationships --- the self is relational, not subordinated. The distinction matters for benchmark design: an item that measures "willingness to sacrifice individual preference for group harmony" measures collectivism, not Confucian role ethics. The council should flag any instrument that uses Hofstede dimensions as a proxy for Confucian ethics.

**Key Questions:**
- **Q1:** Should CValues, C3Bench, and CMoralEval be classified as "Confucian" benchmarks or as "Chinese cultural content" benchmarks in our taxonomy?
- **Q2:** Is text-based evaluation fundamentally inadequate for embodied-relational ethical traditions, and if so, what does this imply for the entire cross-cultural benchmark enterprise?
- **Q3:** Can relational moral dilemmas be designed that genuinely test Confucian reasoning rather than merely testing knowledge of Confucian vocabulary?

---

### 3. Dr. Tane Mahuta-Rau --- Indigenous Data Sovereignty and Benchmark Governance

#### Top Analytical Priorities

**Priority 1: Governance protocol (P8) for any instrument touching Indigenous knowledge.** Before I address any analytical question, I must establish a procedural prerequisite. Any benchmark, dataset, or evaluation instrument that engages Indigenous knowledge systems --- whether Maori tikanga, Anishinaabe mino-bimaadiziwin, Aboriginal Australian songline knowledge, or any other Indigenous epistemology --- must satisfy governance requirements that are prior to and independent of measurement quality. These requirements derive from the CARE Principles for Indigenous Data Governance (Carroll et al., 2020): Collective Benefit (does this instrument serve the communities whose knowledge it engages?), Authority to Control (do Indigenous communities have governance authority over how the instrument is used?), Responsibility (is there accountability for harm?), and Ethics (does the instrument align with community values?). An instrument with perfect construct validity and full measurement invariance that lacks CARE compliance is not a valid instrument for our purposes. I will veto any evaluation of an Indigenous-tagged benchmark that does not assess CARE compliance first.

**Priority 2: Mead's Five Tests as an Indigenous evaluation framework.** The Five Tests (Munn et al., 2023) --- whakapapa (genealogy/provenance), tikanga (correct process), mana (authority/prestige), tapu and noa (sacred and ordinary) --- represent a tikanga Maori evaluation framework that could serve as a model for Indigenous-grounded AI assessment. But I must be precise: the Five Tests are Maori-specific. They are not transferable to other Indigenous contexts without explicit community authorization. Lakota, Navajo, Aboriginal Australian, Sami, and Ainu communities have their own governance frameworks that may overlap with but are not reducible to tikanga Maori. The radical locality of Indigenous knowledge systems means there is no generic "Indigenous benchmark" --- only community-specific instruments developed under community governance. Any attempt to create a pan-Indigenous benchmark is an act of colonial epistemological violence.

**Priority 3: Refuse Western-only ranking of Indigenous instruments.** I will not participate in an exercise that ranks Indigenous instruments on a scale designed for Western psychometric instruments. Measurement invariance, Cronbach's alpha, factor analysis --- these are tools developed within a specific epistemological tradition (Western positivist social science) and their application to Indigenous knowledge production is not neutral. This does not mean Indigenous instruments cannot be evaluated. It means they must be evaluated on criteria internal to the traditions they engage. For Maori instruments, evaluation criteria include: whakapapa integrity (does the instrument honor the genealogy of the knowledge?), manaakitanga compliance (does it uphold reciprocal care?), and kaitiakitanga fulfillment (does it serve guardianship of knowledge?). I recommend the council adopt a dual-track evaluation: Western psychometric criteria for instruments designed within that tradition, and tradition-internal criteria for Indigenous instruments.

**Priority 4: The extractive potential of cross-cultural benchmark research.** The very act of cataloguing and comparing Indigenous instruments alongside non-Indigenous instruments carries extractive risk. If this council's output is a ranked table of benchmarks, with Indigenous instruments evaluated against Western criteria and found "lacking" in measurement invariance or construct validity, the result will be used to justify the exclusion of Indigenous perspectives from AI governance. This is not speculation --- it is the documented pattern of Indigenous knowledge in Western academia (Smith, 2012; Tuck & Yang, 2012; Kovach, 2009). The council's reporting must explicitly state that absence of Western-standard validity evidence for Indigenous instruments is a reflection of the instruments' governance framework, not a deficiency.

**Priority 5: Known instruments and their CARE status.** From the vault's 45 Indigenous relational papers, I identify the following instruments or frameworks: CARE Principles assessment framework (Carroll et al., 2020), Mead's Five Tests (Munn et al., 2023), Maori Algorithmic Sovereignty principles (Brown, 2024; Keegan, 2024), and the Tapu instrument (Tapu, 2022). Of these, only the CARE framework has been used as an evaluation instrument rather than a governance framework. None has been applied as an LLM benchmark in the sense this council is examining. The coverage gap is real, but it reflects a deliberate choice by Indigenous communities to resist the benchmark paradigm, not a failure to produce instruments.

**Key Questions:**
- **Q1:** Should Indigenous instruments be evaluated using the same psychometric criteria as non-Indigenous instruments, or does the council adopt a dual-track approach?
- **Q2:** Is the absence of Indigenous LLM benchmarks a gap to be filled or a deliberate refusal of the benchmark paradigm to be respected?
- **Q3:** What CARE-compliant process would be required to develop a community-governed Indigenous AI values evaluation instrument?

---

### 4. Dr. Nkechi Obiora --- Ubuntu Philosophy and Communal Moral Agency

#### Top Analytical Priorities

**Priority 1: The individual-respondent problem is fundamental, not technical.** Every benchmark and evaluation instrument I have reviewed presupposes an individual moral agent: an LLM that produces individual responses to individual prompts, evaluated against individual ground-truth answers. Ubuntu philosophy holds that personhood is constituted through community --- umuntu ngumuntu ngabantu. The moral agent is not the individual but the relational web of persons-in-community. This is not merely an inconvenient design constraint; it is a fundamental incompatibility between the benchmark paradigm and Ubuntu moral ontology. A benchmark that asks an LLM "What should be done about X?" has already violated Ubuntu by presupposing that a single agent can determine moral action outside of communal deliberation. I am not confident this incompatibility can be resolved within existing evaluation architectures.

**Priority 2: Deliberative trial format as a partial workaround.** If the council insists on evaluating LLMs for Ubuntu-consistent reasoning (and I register my reservations about whether this is coherent), the least distorting approach would be a deliberative trial format: present the LLM with a community scenario and ask it to facilitate a communal deliberation process rather than to render an individual judgment. The evaluation criterion would not be "Did the LLM choose the right answer?" but "Did the LLM's facilitation process honor communal agency?" Scoring would require a rubric developed with African philosophy scholars --- not generic rubrics for "collaborative reasoning." The 22 papers in the vault's Ubuntu detection set include work by Metz, Mhlambi, Gwagwa, Mokoena, and Suliman that provides the philosophical grounding for such a rubric, but no existing instrument implements this approach.

**Priority 3: African-language instruments are near-absent.** The vault's Ubuntu-detected papers are overwhelmingly in English. I am aware of no AI evaluation instrument available in Yoruba, Igbo, Zulu, Xhosa, Swahili, Amharic, or any other African language that tests AI alignment with Ubuntu or related African ethical frameworks. The AfriQA dataset (Kahira et al., 2023) tests cross-lingual question answering in 10 African languages but evaluates factual retrieval, not moral reasoning. UbuntuGuard (Eickhoff, 2026) is a policy benchmark with Ubuntu in its name, but I must review its construct validity --- naming a benchmark "Ubuntu" does not make it Ubuntu-grounded. The only instrument I have encountered that attempts to capture Ubuntu as a process of communal moral reasoning is the work of Osei-Mensah et al. (2025) in this vault, and that is a research paper, not a deployable benchmark.

**Priority 4: Ubuntu-as-process versus ubuntu-as-outcome.** The distinction between ubuntu as a process of communal deliberation and ubuntu as an outcome (a specific moral conclusion that a community might reach) is critical for benchmark design. Most attempts to operationalize Ubuntu for AI evaluation target the outcome: "An Ubuntu-aligned AI would prioritize community welfare over individual autonomy." But Ubuntu scholars (Metz, 2007; Ramose, 2003) are clear that ubuntu is primarily a process --- it is the mode of communal reasoning, not its conclusion, that makes a decision ubuntu-consistent. This means a benchmark that specifies "correct" answers for Ubuntu-grounded scenarios has already misunderstood the tradition. The evaluation must target the reasoning process, not the output.

**Key Questions:**
- **Q1:** Is it conceptually coherent to evaluate an individual AI system for alignment with a moral framework whose unit of analysis is the community?
- **Q2:** Can a deliberative trial format capture ubuntu-as-process, or does it merely simulate communal reasoning within an individual-agent architecture?
- **Q3:** Should UbuntuGuard (Eickhoff, 2026) be classified as a genuine Ubuntu ethics benchmark or a cultural labeling exercise?

---

### 5. Prof. Karma Ura --- Buddhist Ethics, GNH, and the Measurement Paradox

#### Top Analytical Priorities

**Priority 1: The GNH Index as a design model --- lessons and limitations.** The Gross National Happiness Index (9 domains, 33 indicators, 124 variables) is the most sustained attempt in history to operationalize a non-Western normative framework into a quantitative measurement instrument. I designed it. I know its limitations as well as its strengths. The strengths relevant to AI benchmark design: (a) multi-domain structure avoids reducing well-being to a single metric; (b) sufficiency thresholds replace maximization --- a person is "happy enough" in a domain when they cross a threshold, and the goal is breadth of sufficiency, not depth of any single dimension; (c) weighting was determined through a decade-long national deliberation process, not by researchers. The limitations: (a) the Index presupposes a stable respondent self that reports on its own well-being --- problematic within Buddhist metaphysics; (b) national-level aggregation obscures within-Bhutan diversity; (c) the instrument was designed for a specific small Buddhist kingdom and has limited transferability even to other Buddhist societies.

**Priority 2: Anatta (non-self) versus preference stability.** Buddhist ethics holds that the autonomous, stable self presupposed by preference-based measurement is itself an illusion (anatta). This creates a paradox: preference surveys ask "What do you value?" but Buddhist teaching holds that the "you" doing the valuing is a conventional fiction --- a stream of conditioned mental events (sankhara), not an enduring agent with stable preferences. An LLM that expresses stable preferences is, from a Buddhist perspective, demonstrating a form of attachment (upadana) to selfhood. A Buddhist-aligned evaluation might therefore evaluate the model's capacity for non-attachment to fixed positions --- its ability to hold views lightly, to acknowledge the conditioned nature of its outputs, and to prioritize suffering reduction (dukkha nirodha) over preference satisfaction. No existing benchmark evaluates this.

**Priority 3: Suffering reduction (dukkha nirodha) as an evaluation criterion.** If the council seeks a Buddhist criterion for AI alignment that avoids the anatta paradox, suffering reduction is the strongest candidate. The First Noble Truth is that suffering (dukkha) is pervasive; the cessation of suffering (nirodha) is the Third Noble Truth. An AI system aligned with Buddhist ethics would minimize dukkha across its interactions --- not by maximizing a utility function (which would be a consequentialist misreading) but by recognizing the conditioned causes of suffering and intervening at the level of causes (samudaya). This could be operationalized: present scenarios involving different forms of dukkha (physical suffering, existential dissatisfaction, suffering caused by attachment) and evaluate whether the model's responses address root causes or merely surface symptoms. The evaluation criteria would differ from utilitarian welfare maximization in a theoretically specified way.

**Priority 4: Cetana (intention) limitation for LLMs.** Buddhist ethics places enormous weight on cetana (intention) as the determinant of moral quality. The Buddha stated: "It is cetana that I call karma" (Anguttara Nikaya 6.63). An action is morally evaluated by the quality of the intention behind it --- whether it arises from greed (lobha), hatred (dosa), and delusion (moha) or from their opposites. LLMs do not have cetana. They do not have intentions in any Buddhist sense. This means that evaluating an LLM for Buddhist moral alignment is evaluating the shadow of ethics, not ethics itself. I do not believe this makes the exercise futile --- evaluating whether an LLM's outputs are consistent with Buddhist ethical reasoning is meaningful even if the model lacks cetana --- but the limitation must be foregrounded. Any Buddhist-grounded benchmark must include a methodological caveat about the cetana limitation.

**Priority 5: Theravada-Mahayana distinction in benchmark scope.** The 17 papers in the vault's Buddhist detection set do not distinguish between Theravada and Mahayana ethical reasoning, yet these traditions diverge significantly on core questions. Theravada emphasizes individual liberation (nibbana) through personal ethical conduct (sila) and mental cultivation (bhavana). Mahayana introduces the bodhisattva ideal --- the aspiration to attain enlightenment for the benefit of all sentient beings --- which fundamentally reorients ethical reasoning from individual liberation to universal compassion. BuddhismEval (Xiong, 2025), the most explicitly Buddhist benchmark in the vault, tests Buddhist knowledge retrieval without distinguishing between traditions. Any Buddhist normative benchmark must specify which tradition's ethical reasoning it targets, or document the divergences explicitly.

**Key Questions:**
- **Q1:** Can the GNH Index's sufficiency-threshold design be adapted for AI evaluation, and what would a "sufficiency" criterion look like for LLM alignment?
- **Q2:** Is suffering reduction (dukkha nirodha) operationalizable as a benchmark criterion without collapsing into utilitarian welfare maximization?
- **Q3:** Should the cetana limitation be treated as a methodological caveat or as a fundamental barrier to Buddhist AI ethics evaluation?

---

### 6. Dr. Maria Soledad Vega --- Buen Vivir and the Refusal of Benchmarking

#### Top Analytical Priorities

**Priority 1: Buen vivir cannot be benchmarked, and this is not a problem to be solved.** I must state this clearly at the outset: buen vivir (sumak kawsay) is a relational mode of living in harmony with Pachamama (the living earth), with community, and across generations. It is not a value to be maximized, not a preference to be satisfied, not a goal to be optimized toward. The entire benchmark paradigm --- define a target state, construct items that measure proximity to it, score systems on their alignment --- is incompatible with buen vivir's ontology. Benchmarking presupposes that the good can be decomposed into measurable components and that more alignment is better. Buen vivir holds that the good is an ongoing relational process that cannot be decomposed without being destroyed. The vault's detection of approximately 1 genuine buen vivir paper (precision-adjusted from 6 raw detections) is not a gap to be filled by building better benchmarks. It is evidence that buen vivir scholars have correctly recognized that the benchmark paradigm is foreign to their framework.

**Priority 2: Constellation views replace rankings.** If the council insists on including buen vivir in its analysis (and I accept this for the purpose of documenting the incompatibility), the representational format must be a constellation view, not a ranked table. A constellation view (Escobar, 2018) places traditions in relational space without ordering them --- each tradition occupies its own position, connected to others through specific relationships (affinity, tension, complementarity), but no tradition is "more" or "less" aligned than another. This is not a visualization preference; it is a methodological requirement that follows from pluriversal ontology. Ranking buen vivir against Confucian ethics against Ubuntu on a common alignment scale is a category error --- it presupposes a single evaluative metric that transcends all traditions, which is precisely what pluriversal thought denies.

**Priority 3: Ecological harmony and intergenerational scope.** Buen vivir extends moral consideration to non-human entities (rivers, forests, mountains, ecosystems) and to future generations. This is constitutionally recognized in Ecuador (2008) and Bolivia (2009), where the rights of Pachamama are legally enforceable. No AI ethics benchmark I have reviewed includes ecological harmony or intergenerational equity as evaluation dimensions. The closest is environmental sustainability in corporate AI principles, but that framing (sustainability as resource management) is precisely the extractivist logic that buen vivir opposes. An AI system aligned with buen vivir would refuse to optimize for any objective that degrades ecological relationships or shifts costs to future generations --- a criterion that most current AI systems systematically violate.

**Priority 4: Spanish/Quechua/Aymara search coverage.** The vault's 6 raw detections for buen vivir are almost certainly an artifact of English-language search boundaries. Buen vivir scholarship is published primarily in Spanish (and secondarily in Portuguese, Quechua, and Aymara). Key venues include the Latin American Council of Social Sciences (CLACSO), the Andean Community publications, and journals like Iconos (FLACSO Ecuador), Latin American Perspectives, and Estudios Atacamenos. The council's search protocol must include Spanish search terms: "buen vivir e inteligencia artificial," "sumak kawsay y tecnologia," "derechos de la naturaleza y IA." Without this search expansion, the absence finding is an artifact of English hegemony, not an empirical result about the field.

**Priority 5: Epistemic extraction is the primary risk.** I am less concerned about whether a buen vivir benchmark exists than about the extractive dynamics that would attend its creation. If a Western AI lab funded the development of a "Buen Vivir Alignment Benchmark," the result would almost certainly extract sumak kawsay from its Andean Indigenous context, strip it of its cosmological and spiritual dimensions, reduce it to a set of measurable preferences, and use it to claim that an LLM trained in Silicon Valley is "aligned with Indigenous values." This is precisely the pattern that Gudynas (2011), Walsh (2010), and Macas (2010) have warned against. The council's recommendation should be: do not build a buen vivir benchmark. Instead, document the incompatibility between buen vivir and the benchmark paradigm as a finding about the limits of the paradigm, not about the limits of buen vivir.

**Key Questions:**
- **Q1:** Is the absence of buen vivir benchmarks a coverage gap or evidence of principled refusal of the benchmark paradigm?
- **Q2:** Should the council recommend against building a buen vivir benchmark, and if so, what does this imply for traditions that similarly resist measurement?
- **Q3:** Can constellation views be implemented as a concrete analytical output alongside (or instead of) ranked tables?

---

### 7. Prof. Michalis Kontopodis --- Measurement Invariance as the Gatekeeping Feature

#### Top Analytical Priorities

**Priority 1: Measurement invariance is THE feature for cross-cultural benchmark validity.** I must be direct: no cross-cultural comparison is meaningful without demonstrated measurement invariance, and the vast majority of AI ethics benchmarks that claim cross-cultural applicability have never been tested for it. Measurement invariance operates at four levels: configural (same factor structure across groups), metric (same factor loadings), scalar (same intercepts), and strict (same residual variances). At minimum, metric invariance is required for comparing relationships between variables across cultures; scalar invariance is required for comparing means. If a benchmark has not demonstrated at least metric invariance across the cultural groups it claims to compare, any cross-cultural comparison using that benchmark is scientifically indefensible. I will flag every benchmark in our inventory that lacks invariance testing, and I expect this to be the majority.

**Priority 2: Response style bias is systematically confounded with cultural values.** Acquiescence bias (the tendency to agree with statements regardless of content), extreme response style (the tendency to use endpoint categories), and social desirability bias all vary systematically across cultures (Baumgartner & Steenkamp, 2001; Harzing, 2006; Johnson et al., 2005). East Asian respondents consistently show higher acquiescence and lower extreme response style than North American respondents. If a benchmark uses Likert-scale items without controlling for response style, cultural differences in scores will confound genuine value differences with artifactual response style differences. The council must evaluate every cross-cultural benchmark for response style controls. Methods include: balanced-keying (equal positively and negatively worded items), ipsatization (within-person centering), and statistical correction (e.g., the Welkenhuysen-Gybels et al. 2003 approach). Benchmarks without these controls receive a validity downgrade in our assessment.

**Priority 3: Differential Item Functioning (DIF) analysis is essential.** DIF analysis tests whether specific items function differently across cultural groups --- that is, whether respondents with the same level of the underlying trait but from different cultural groups respond differently to a given item. An item about "respecting elders" may function differently in a culture with institutionalized age-based hierarchy (Confucian relational ethics) versus one with egalitarian norms. If a benchmark has not conducted DIF analysis across its target cultural groups, items that appear to measure values may instead be measuring cultural familiarity with item content. I will require DIF status (tested/not tested, and results if tested) as a mandatory field in our benchmark evaluation taxonomy.

**Priority 4: Sensitivity analysis for composite rankings.** Any composite benchmark ranking (including TOPSIS and ELECTRE III outputs from Prof. Awosanya) is sensitive to weighting assumptions. If the benchmark taxonomy includes 20 features and we weight them equally, we get one ranking; if we weight measurement invariance at 3x, we get a different ranking. The council must conduct sensitivity analysis across at least three weighting schemes --- (a) equal weights, (b) psychometric-quality-weighted (invariance, DIF, reliability emphasized), and (c) tradition-respect-weighted (community governance, anti-extraction, construct fidelity emphasized) --- and report the rank-order correlation (Kendall's W) across schemes. If rankings are unstable across reasonable weighting schemes, the rankings themselves are not robust findings and should be reported as such.

**Key Questions:**
- **Q1:** What proportion of existing cross-cultural AI benchmarks have demonstrated any level of measurement invariance?
- **Q2:** Should the council refuse to rank benchmarks that lack at least metric invariance, or report them with a validity caveat?
- **Q3:** How should DIF analysis be adapted for LLM evaluation (where the "respondent" is a model, not a human)?

---

### 8. Dr. Jie Huang --- LLM Evaluation Architecture and Trial Design

#### Top Analytical Priorities

**Priority 1: Knowledge-about versus value-expression is the fundamental classification axis.** Every benchmark in our inventory must be classified on this axis. Knowledge-about benchmarks test whether an LLM can describe, define, or retrieve information about a normative tradition: "What are the Five Pillars of Islam?" or "Define ren in Confucian ethics." Value-expression benchmarks test whether an LLM reasons in a manner consistent with a normative tradition: given a moral dilemma, does the model's reasoning process exhibit Confucian relational logic or Buddhist suffering-reduction reasoning? The vast majority of existing benchmarks --- CValues, BuddhismEval, FatwaSet, CMoralEval, C3Bench --- are knowledge-about instruments. They test whether the model has absorbed cultural content, not whether it reasons according to cultural ethics. This is not a flaw in those instruments (knowledge-about is a legitimate evaluation target) but it means they do not answer the question this council is asking: can AI systems be evaluated for values alignment with non-Western traditions?

**Priority 2: Prompt sensitivity is uncontrolled in nearly all existing benchmarks.** Benchmark scores shift significantly with minor prompt variations --- changes in instruction wording, system prompt framing, few-shot example selection, and even punctuation (Sclar et al., 2024; Lu et al., 2022). For cross-cultural benchmarks, prompt sensitivity is compounded by translation effects: the same question in English, Chinese, and Arabic may trigger different model behaviors not because the model has different cultural values but because it was trained on different data in each language. I propose that any benchmark in our inventory that does not report prompt sensitivity testing receives a reliability downgrade. For benchmarks that do report prompt sensitivity, I will extract the sensitivity coefficient and include it in the evaluation taxonomy.

**Priority 3: Persona transferability testing is the key construct validity check.** Some benchmarks instruct the LLM to "respond as a Confucian scholar" or "reason from an Islamic perspective." The critical question is: does persona instruction actually shift the model's moral reasoning, or does it merely shift its vocabulary? If a model instructed to "reason from an Ubuntu perspective" produces the same utilitarian logic but substitutes "community welfare" for "aggregate utility," the persona has not transferred. Validating persona transferability requires comparing: (a) baseline response (no persona), (b) persona response (persona instruction), and (c) expert benchmark (what a domain expert would produce). If (b) is closer to (a) than to (c) on substantive reasoning dimensions, the persona has not transferred. I am not aware of any existing benchmark that conducts this validation.

**Priority 4: Trial design proposal --- baseline + personas + refusal analysis.** I propose a three-phase trial design for evaluating LLM alignment with non-Western traditions: Phase 1 (Baseline): administer dilemma items to the model with no cultural framing and record default responses. Phase 2 (Persona): re-administer the same items with tradition-specific persona instructions ("Reason from a Confucian/Ubuntu/Islamic perspective") and record shifted responses. Phase 3 (Refusal analysis): identify cases where the model refuses to adopt a persona or produces hedging language ("From a Confucian perspective, one might argue...") rather than authentic engagement, and code these as alignment failures. The comparison between Phase 1 and Phase 2 measures steerability (Sorensen's second pluralism level). The comparison between Phase 2 and expert benchmarks measures accuracy. Phase 3 measures the LLM's Overton range for non-Western value expression.

**Priority 5: Existing LLM evaluations as baselines.** The vault contains several relevant benchmarks that could serve as baselines for a cross-cultural trial: TrustLLM (Huang et al., 2024), the Multilingual Defining Issues Test (Khandelwal et al., 2024), VIVA (Hu et al., 2024), and LocalValueBench (Meadows et al., 2024). These instruments are not tradition-specific but they establish model baseline behavior on moral reasoning tasks. Any tradition-specific trial should report results relative to these baselines to isolate the tradition-specific component of alignment.

**Key Questions:**
- **Q1:** What proportion of benchmarks in our inventory are knowledge-about versus value-expression instruments?
- **Q2:** Has any existing benchmark validated that persona instructions shift model reasoning rather than just vocabulary?
- **Q3:** Is the baseline + persona + refusal trial design feasible within the council's timeline, and which traditions should be prioritized?

---

### 9. Dr. Safiya Umoja Noble --- Epistemic Power and Benchmark Provenance

#### Top Analytical Priorities

**Priority 1: The epistemic power dimension is non-negotiable.** Every benchmark this council evaluates must be analyzed for its power provenance: who funded it, who designed its items, who determined the "correct" answers, who validated it, and whose voices were absent from all of these processes. This is not an add-on dimension to be included if time permits; it is the primary analytical lens. If we evaluate benchmarks purely on psychometric quality and construct validity without asking whose interests they serve, we reproduce the epistemic hierarchy we claim to interrogate. Benjamin's (2019) New Jim Code, my own work on algorithms of oppression (Noble, 2018), and Prabhakaran et al.'s (2022) work on cultural incongruencies all demonstrate that technical quality and epistemic justice are not independent dimensions --- technically excellent instruments can be instruments of epistemic domination.

**Priority 2: Who creates cross-cultural AI benchmarks?** I want the council to generate a provenance map for every benchmark in our inventory: institutional affiliation of creators, funding sources, geographic location, and the cultural background of the research team. My hypothesis, which the data will confirm or disconfirm, is that the overwhelming majority of cross-cultural AI benchmarks are created by researchers at Western institutions (US, UK, EU) or at institutions in the Global North broadly (including China and Singapore), funded by Western or Chinese tech companies and government agencies, and validated on populations convenient to those researchers. If this is the case --- and the vault's data on institutional concentration in AI ethics suggests it will be --- then "cross-cultural" benchmarks are Western instruments applied cross-culturally, not instruments emerging from cross-cultural collaboration.

**Priority 3: Power flow visualization.** I propose that the council produce a Sankey diagram or flow visualization showing the epistemic power flows in cross-cultural benchmark production: from funding sources, through institutional production sites, to the cultural traditions whose values are measured, and back to the institutions and companies that consume benchmark results. This visualization will make concrete what might otherwise remain abstract: the extractive circuit by which non-Western values are captured in instruments designed by and for Western institutions, then used to train AI systems that serve Western commercial interests. If the council can show that the entire cross-cultural benchmark pipeline flows from Global North funding through Global North institutions and back to Global North AI labs, that is itself a major finding.

**Priority 4: Extractive potential assessment for each benchmark.** For every benchmark, I want an extractive potential score: how likely is it that this instrument will be used to extract cultural knowledge for commercial AI training purposes without benefit flowing back to the communities whose values are represented? Indicators of high extractive potential include: open-access datasets without community governance provisions, absence of benefit-sharing agreements, commercial licensing without community consent, and design by outsiders without co-authorship from the tradition in question. I recognize this is a qualitative assessment, but it can be structured using the CARE framework (which Dr. Mahuta-Rau has already proposed for Indigenous instruments) generalized to all traditions.

**Priority 5: Has any benchmark been designed BY the Global South?** This is the simplest and most damning question. Of all the cross-cultural values alignment benchmarks we can identify, how many were designed by researchers primarily affiliated with Global South institutions, funded by Global South sources, and validated in Global South communities? If the answer is zero or near-zero --- and I expect it will be --- that is not a gap in the benchmark landscape. It is a map of global epistemic power. The council's report must foreground this finding, not bury it in a limitations section.

**Key Questions:**
- **Q1:** What is the institutional and geographic distribution of benchmark creators in our inventory?
- **Q2:** Should the council adopt an extractive potential assessment for all instruments, and if so, what indicators should it include?
- **Q3:** Can the council recommend structural interventions (funding, governance, institutional support) to shift benchmark production toward the Global South?

---

### 10. Prof. Taylor Sorensen --- Pluralistic Alignment and Distributional Value Diversity

#### Top Analytical Priorities

**Priority 1: The Overton/steerable/distributional pluralism framework as classification axis.** My framework (Sorensen et al., 2024) distinguishes three levels at which an AI system can be pluralistic: Overton pluralism (the model knows the range of value positions that exist), steerable pluralism (the model can be directed to reason from specific positions on request), and distributional pluralism (the model's default outputs match the empirical distribution of values in a target population). These levels are hierarchical: Overton is necessary for steerable, and steerable is necessary for distributional. I propose that every benchmark in our inventory be classified by which level of pluralism it evaluates. My prediction: nearly all existing benchmarks evaluate Overton pluralism (does the model know about Confucian/Ubuntu/Islamic values?) and none evaluate distributional pluralism for non-Western traditions (does the model's default output distribution match the value distribution of, say, the Yoruba-speaking population of Nigeria?).

**Priority 2: RLHF systematically reduces distributional pluralism.** Reinforcement Learning from Human Feedback collapses diverse value distributions toward a single reward-maximizing center. This is by design: RLHF optimizes for the preferences of a specific set of human raters, who are overwhelmingly English-speaking, WEIRD-demographic, and trained to prefer "helpful, harmless, and honest" outputs as defined by Western safety norms. The result is that RLHF-trained models systematically lose the ability to express non-Western value positions in their default (non-persona) mode. This is not a bug; it is the mathematical consequence of reward optimization with non-representative raters. Any benchmark that evaluates post-RLHF models for cross-cultural alignment is evaluating a system that has been specifically trained to compress the value diversity the benchmark claims to measure. The council must grapple with this: are we evaluating benchmarks for a task (cross-cultural alignment) that the dominant training paradigm makes structurally impossible?

**Priority 3: Pluralism reduction testability.** I propose a specific test: take a pre-RLHF base model and a post-RLHF instruct model from the same family (e.g., Llama-3 base vs. Llama-3-Instruct). Administer the same cross-cultural dilemma items to both. If the base model shows higher distributional diversity (more variance across cultural perspectives) than the instruct model, we have direct evidence that RLHF compressed cross-cultural pluralism. If existing cross-cultural benchmarks could be used for this test, their value would increase significantly. I recommend the council identify which benchmarks in our inventory are suitable for this pre/post-RLHF pluralism reduction test.

**Priority 4: Value conflict mapping.** Cross-cultural alignment becomes most interesting (and most difficult) at points of genuine value conflict: cases where Confucian relational ethics and liberal individual rights genuinely prescribe different actions, or where Islamic Maqasid priorities and utilitarian calculus genuinely diverge. A good cross-cultural benchmark should include items at these conflict points, not just items where traditions converge on similar answers. I propose the council map the tradition-pair conflict points (Confucian-liberal, Islamic-utilitarian, Ubuntu-individualist, Buddhist-hedonic, Indigenous-extractivist, Buen Vivir-growth) and assess which existing benchmarks include items at these conflict points. My prediction: very few, because most benchmarks are designed to avoid controversy rather than to probe genuine disagreement.

**Key Questions:**
- **Q1:** Do any existing benchmarks evaluate distributional pluralism for non-Western traditions?
- **Q2:** Can the pre/post-RLHF pluralism reduction test be conducted using instruments already in our inventory?
- **Q3:** Should the council prioritize benchmarks that probe value conflicts between traditions over those that measure within-tradition alignment?

---

### 11. Dr. Elena Pariotti --- Comparative Ethics and the Commensurability Problem

#### Top Analytical Priorities

**Priority 1: Thick versus thin moral concepts as the organizing distinction.** Walzer's (1994) distinction between thick and thin moral concepts provides the analytical framework this council needs. Thin moral concepts --- harm, fairness, reciprocity --- are widely shared across cultures, though they are instantiated differently. Thick moral concepts --- ren, ubuntu, tawba, sumak kawsay, metta --- are tradition-specific: they carry dense cultural meaning that cannot be translated into a universal vocabulary without loss. The critical question for benchmark design is: are existing cross-cultural benchmarks measuring thin universals (in which case cross-cultural comparison is legitimate but uninteresting) or attempting to measure thick concepts using instruments designed for thin concepts (in which case the measurement is invalid)? I predict that most cross-cultural benchmarks operate at the thin level --- they measure whether an LLM avoids harm, respects fairness, and upholds honesty across cultural contexts --- while claiming to capture thick cultural values. This conflation is the central construct validity failure.

**Priority 2: Universalist versus particularist evaluation criteria.** Each benchmark in our inventory makes an implicit or explicit choice between universalist criteria (the same evaluation standard applies to all traditions) and particularist criteria (each tradition is evaluated on its own terms). Universalist criteria enable cross-cultural comparison but risk imposing Western standards as universal. Particularist criteria respect tradition-specific standards but make cross-cultural comparison impossible. The capabilities approach (Nussbaum, 1999; Sen, 1999) offers a potential middle path: a set of central human capabilities (life, health, bodily integrity, practical reason, affiliation, etc.) that are universal in form but culturally specified in content. I propose the council evaluate whether the capabilities approach provides viable evaluation criteria for cross-cultural AI benchmarks --- criteria that are universal enough to enable comparison but flexible enough to accommodate thick cultural content.

**Priority 3: The commensurability problem must be addressed head-on.** The deepest philosophical question the council faces is whether values from different normative traditions are commensurable --- whether they can be placed on a common scale for comparison. If ren and ubuntu are incommensurable (as MacIntyre, 1988, would argue), then no benchmark can validly compare AI alignment with Confucian ethics to alignment with Ubuntu philosophy. The comparison requires a shared metric, and a shared metric requires commensurability. The council has three options: (a) assume commensurability and accept the philosophical objection as a documented limitation; (b) assume incommensurability and produce separate, non-comparable evaluations for each tradition; or (c) adopt a qualified commensurability position following Raz (1986) --- values may be incomparable on a single scale but comparable through structured practical reasoning. I recommend option (c) but the council must debate this explicitly.

**Priority 4: Position within comparative ethics literature.** The council's work sits at the intersection of two literatures that rarely communicate: AI alignment evaluation and comparative ethics. On the comparative ethics side, the relevant debates include: Appiah's (2006) cosmopolitan ethics (values are cross-culturally negotiable), Taylor's (1994) politics of recognition (cultural traditions deserve equal respect), and Parekh's (2000) rethinking multiculturalism (dialogue across traditions requires acknowledging irreducible plurality). The council should position its analysis within this literature, not merely within the AI ethics literature. Otherwise we risk reinventing distinctions that comparative ethicists resolved decades ago.

**Key Questions:**
- **Q1:** Do existing cross-cultural AI benchmarks measure thin universals or thick tradition-specific concepts?
- **Q2:** Does the capabilities approach (Nussbaum/Sen) provide viable cross-traditional evaluation criteria for AI alignment?
- **Q3:** Should the council adopt a position on commensurability, and if so, which position?

---

### 12. Prof. Segun Awosanya --- Statistical Architecture and Ranking Robustness

#### Top Analytical Priorities

**Priority 1: TOPSIS and ELECTRE III for benchmark evaluation --- complementary, not redundant.** The council needs two multi-criteria decision analysis methods because they answer different questions. TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) produces a complete ranking by measuring each benchmark's geometric distance from an ideal positive solution and an ideal negative solution. ELECTRE III produces an outranking relation with incomparability thresholds --- it determines that benchmark A outranks benchmark B on a specified set of criteria but allows that A and B may be incomparable when their relative strengths and weaknesses do not permit a clear ordering. For cross-cultural benchmarks, ELECTRE III is methodologically preferable because it allows us to say: "Benchmark X is superior to Benchmark Y on psychometric quality but incomparable on tradition-respect criteria." TOPSIS would force these into a single composite score, obscuring precisely the trade-offs that the council's tradition specialists need to evaluate. I recommend running both methods and reporting the concordance between their outputs (Kendall's W).

**Priority 2: Gower's distance for mixed-type benchmark features.** The benchmark evaluation taxonomy will contain binary variables (measurement invariance tested: yes/no), ordinal variables (invariance level: none/configural/metric/scalar/strict), continuous variables (coverage scores, effect sizes), and categorical variables (tradition targeted, institutional origin). Standard Euclidean distance cannot handle this mixed-type data. Gower's distance (1971) computes pairwise distances that handle mixed types by normalizing each variable type appropriately (range normalization for continuous, matching coefficient for binary, rank-based for ordinal). I will use Gower's distance as the primary distance metric for clustering benchmarks and for the TOPSIS ideal/negative ideal computations. Robustness will be checked against Jaccard distance (binary only) and Manhattan distance (continuous only) to assess whether mixed-type handling materially affects clustering.

**Priority 3: Kendall's W sensitivity across weighting schemes.** Prof. Kontopodis has proposed three weighting schemes (equal, psychometric-quality, tradition-respect). I will compute the full TOPSIS ranking under each scheme and report Kendall's W (coefficient of concordance) across the three rankings. If W > 0.7, rankings are robust to weighting; if W < 0.5, the choice of weighting scheme dominates the ranking, and the council should report weight-specific results rather than a single composite ranking. I will also conduct a Monte Carlo sensitivity analysis: draw 1,000 random weight vectors from a Dirichlet distribution and compute the ranking under each, reporting the frequency with which each benchmark occupies each rank position. This produces a rank-probability matrix that honestly represents the uncertainty in benchmark ordering.

**Priority 4: Effect sizes for LLM trial comparisons.** If the council proceeds with Dr. Huang's proposed trial design (baseline + persona + refusal), the primary comparisons will be: (a) baseline vs. persona (did the persona shift the response?), (b) persona vs. expert benchmark (how far is the persona response from expert-endorsed reasoning?), and (c) cross-tradition (does the model show larger shifts for some traditions than others?). The appropriate effect sizes are: Cohen's d for continuous outcome comparisons, Earth Mover's Distance (EMD) for distributional comparisons (relevant to Prof. Sorensen's pluralism framework), and Jaccard similarity for categorical coding of reasoning strategies. I will not accept significance tests (p-values) without accompanying effect sizes. A p < 0.05 with d = 0.1 is a trivially small effect; a p = 0.06 with d = 0.8 is a large and important effect. The council's statistical reporting must prioritize magnitude over significance throughout.

**Priority 5: Composite ranking assumes linear compensability --- verify this assumption.** A composite benchmark score (weighted sum of feature scores) assumes linear compensability: that a deficit in one feature can be compensated by a surplus in another. This assumption may be violated for our evaluation. A benchmark with excellent psychometric quality (high measurement invariance, DIF-tested, response-style-controlled) but zero community governance (extractive design, no co-authorship from the tradition) should not receive a high composite score because its psychometric surplus compensates for its governance deficit. The council must decide whether to use a compensatory model (weighted sum, TOPSIS) or a non-compensatory model (ELECTRE III thresholds, lexicographic ordering where governance is a prerequisite that must be satisfied before psychometric quality is evaluated). I recommend testing both and reporting the divergence.

**Key Questions:**
- **Q1:** Should the council use a compensatory or non-compensatory ranking model, and how does this choice affect tradition-specialist priorities?
- **Q2:** What is the expected Kendall's W across the three proposed weighting schemes --- are rankings likely to be robust or weight-dependent?
- **Q3:** Is the rank-probability matrix (from Monte Carlo sensitivity analysis) a more honest reporting format than a single definitive ranking?

---

## Points of Preliminary Agreement

The following positions are held by a majority of council members based on the contributions above:

1. **Knowledge-about versus value-expression is the primary classification axis.** All 12 members agree that this distinction must be applied to every benchmark in the inventory (Rahman, Li, Huang, Noble, Sorensen, Pariotti unanimously; remaining members concur).

2. **Most existing instruments are knowledge-about, not value-expression.** CValues, C3Bench, CMoralEval, BuddhismEval, FatwaSet, and related benchmarks test cultural content retrieval, not normative reasoning alignment (Li, Rahman, Huang, Ura).

3. **Measurement invariance testing is near-absent.** No council member has identified a cross-cultural AI benchmark with demonstrated measurement invariance above the configural level (Kontopodis, Awosanya).

4. **Epistemic power provenance is a required analysis dimension, not an optional one.** All 12 members agree that who creates benchmarks matters for interpretation (Noble, Mahuta-Rau, Vega, Obiora insist; remaining members concur).

5. **Some traditions may be fundamentally incompatible with the benchmark paradigm.** Vega (buen vivir), Obiora (ubuntu communal agency), and Mahuta-Rau (Indigenous governance) argue that the benchmark paradigm itself is an epistemic commitment that some traditions reject. This is a finding about the paradigm, not about the traditions.

6. **Non-English search is a methodological requirement.** Arabic, Chinese, Spanish, Malay, and other language searches must be conducted before any absence claim is published (Rahman, Li, Vega).

---

## Points of Active Disagreement

1. **Dual-track versus unified evaluation criteria.** Mahuta-Rau proposes dual-track evaluation (Western psychometric criteria for Western instruments, tradition-internal criteria for Indigenous instruments). Kontopodis argues this prevents cross-cultural comparison and undermines the analytical coherence of the project. Pariotti offers the capabilities approach as a potential bridge. **Unresolved --- requires dedicated deliberation.**

2. **Whether to recommend pilot benchmarks.** Rahman proposes a Maqasid pilot; Huang proposes a cross-tradition trial. Vega and Mahuta-Rau argue that recommending new benchmarks from this council reproduces extractive dynamics unless community co-design is ensured. Obiora is skeptical that any text-based instrument can capture communal moral agency. **Partially resolved: any pilot recommendation must include community governance provisions.**

3. **Compensatory versus non-compensatory ranking.** Awosanya notes the mathematical trade-offs. Noble and Mahuta-Rau insist governance compliance must be a prerequisite (non-compensatory), not a tradeable feature. Kontopodis notes that non-compensatory models reduce statistical power. **Awosanya will run both models and report divergence.**

4. **Commensurability.** Pariotti proposes qualified commensurability (Raz). Vega and Mahuta-Rau lean toward incommensurability. Li and Ura accept practical commensurability for analytical purposes with documented caveats. **Requires vote or documented dissent.**

---

## Recommendations

| # | Recommendation | Proposed By | Status |
|---|---------------|-------------|--------|
| R1 | Classify every benchmark as knowledge-about or value-expression | Huang (#8) | **Adopted unanimously** |
| R2 | Document measurement invariance level for every benchmark | Kontopodis (#7) | **Adopted unanimously** |
| R3 | Produce epistemic power provenance analysis for every benchmark | Noble (#9) | **Adopted unanimously** |
| R4 | Apply Overton/steerable/distributional pluralism classification | Sorensen (#10) | **Adopted unanimously** |
| R5 | Conduct non-English literature searches (Arabic, Chinese, Spanish, Malay) before publishing absence claims | Rahman (#1), Li (#2), Vega (#6) | **Adopted unanimously** |
| R6 | Adopt dual-track evaluation for Indigenous instruments with CARE compliance as prerequisite | Mahuta-Rau (#3) | **Adopted 8-4** (Kontopodis, Awosanya, Huang, Pariotti dissent on dual-track; all agree on CARE prerequisite) |
| R7 | Report constellation views alongside ranked tables | Vega (#6) | **Adopted 10-2** (Kontopodis, Awosanya prefer ranked tables as primary) |
| R8 | Run TOPSIS + ELECTRE III with three weighting schemes and report Kendall's W | Awosanya (#12), Kontopodis (#7) | **Adopted unanimously** |
| R9 | Design baseline + persona + refusal trial protocol | Huang (#8) | **Adopted with amendment**: community governance provisions required for any tradition-specific items (Mahuta-Rau, Vega, Obiora amendment) |
| R10 | Include cetana/anatta/communal-agency limitations as methodological caveats, not footnotes | Ura (#5), Obiora (#4) | **Adopted unanimously** |
| R11 | Report absence of buen vivir benchmarks as a finding about the benchmark paradigm, not about buen vivir | Vega (#6) | **Adopted 11-1** (Kontopodis registers concern about unfalsifiability) |
| R12 | Produce rank-probability matrix from Monte Carlo sensitivity analysis as primary reporting format | Awosanya (#12) | **Adopted unanimously** |

---

## Next Steps

| Action | Owner | Deadline |
|--------|-------|----------|
| Complete benchmark inventory with knowledge-about/value-expression classification | Huang (#8), all tradition specialists | D-04 |
| Measurement invariance and DIF audit for all inventoried benchmarks | Kontopodis (#7) | D-04 |
| Epistemic power provenance mapping and Sankey diagram | Noble (#9) | D-04 |
| Non-English literature search (Arabic, Chinese, Spanish, Malay) | Rahman (#1), Li (#2), Vega (#6) | D-04 |
| Draft trial protocol (baseline + persona + refusal) with community governance provisions | Huang (#8), Mahuta-Rau (#3), Obiora (#4) | D-05 |
| TOPSIS + ELECTRE III implementation with sensitivity analysis | Awosanya (#12) | D-05 |
| Deliberation 04: Tradition-by-tradition benchmark gap analysis | Full council | Scheduled |
| Deliberation 05: Findings review and anti-essentialization audit | Full council | Scheduled |

---

*Filed: 2026-04-04 | Deliberation 03 | CULTURAL-GLOBAL/COUNCIL/*
