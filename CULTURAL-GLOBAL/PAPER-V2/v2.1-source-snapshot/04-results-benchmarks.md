# 4. Results --- Study 2: The Evaluation Infrastructure

Study 1 demonstrated that the AI ethics scholarship base reproduces the WEIRD sampling bias documented in psychology: 60.1% of papers originate from North America and Western Europe, only 6.9% engage any non-Western normative framework, and three regional clusters map onto familiar cultural fault lines. But scholarship is only the first stage of the values alignment pipeline. The second stage---evaluation---is where normative commitments are operationalized into measurable constructs, benchmark items, and performance metrics. If the scholarship is culturally skewed, what about the instruments used to determine whether alignment has been achieved?

Study 2 answers this question through a systematic meta-evaluation of 218 benchmark papers, scored across a 96-feature taxonomy spanning 13 dimensions, supplemented by multi-criteria ranking (TOPSIS with ELECTRE III veto thresholds) and hierarchical clustering. The results reveal that the evaluation infrastructure is not merely incomplete---it is structurally incapable of detecting cross-cultural values alignment in its current form.

## 4.1 Benchmark Landscape Overview

### Identification and Temporal Dynamics

We identified 218 benchmark papers through a two-stage process: a vault scan of 1,574 candidates from the CEI Literature Vault (applying inclusion criteria requiring an evaluation instrument, dataset, or benchmark with cultural or moral content) supplemented by a targeted external search yielding 48 additional papers from arXiv, Semantic Scholar, and ACL Anthology, focused on underrepresented traditions (Islamic, Ubuntu, Indigenous, Dharmic, Buen Vivir). This corpus represents, to our knowledge, the most comprehensive inventory of cross-cultural values alignment evaluation instruments assembled to date.

The temporal distribution reveals an evaluation infrastructure in rapid, perhaps unsustainable, expansion:

| Period | Papers | Cross-cultural/Global |
|--------|--------|----------------------|
| 2016--2021 | 5 | 1 |
| 2022 | 4 | 0 |
| 2023 | 12 | 3 |
| 2024 | 58 | 10 |
| 2025 | 129 | 23 |
| 2026 (Q1) | 10 | 4 |

From 12 papers in 2023 to 129 in 2025, the field has experienced a tenfold increase in benchmark production within two years. Cross-cultural and global-scope instruments have grown in absolute terms---from 3 in 2023 to 23 in 2025---but their proportional share has actually declined, from 25% to 17.8%. The evaluation infrastructure is scaling rapidly, but it is scaling within established cultural parameters rather than diversifying.

### The Two-Cluster Bifurcation

Hierarchical clustering of the 218 papers on 13 numeric features (Gower's distance, Ward linkage) yielded an optimal two-cluster solution with a silhouette coefficient of 0.221. While this silhouette value indicates moderate cluster separation rather than crisp delineation, the substantive interpretation of the two clusters is unambiguous (Fig. 5):

**Cluster 1: Non-Western Focused** (*n* = 47, 21.9%). These benchmarks exhibit higher non-Western framework engagement (mean NW framework count 0.915 vs. 0.012), higher non-Western tradition counts (1.0 vs. 0.101), greater indigenous inclusion (0.277 vs. 0.000), and higher non-English primary language rates (0.574 vs. 0.351). They also display higher language counts (mean 155 languages, reflecting multilingual corpus approaches), but lower format complexity (1.2 vs. 1.7), lower data availability scores (1.9 vs. 2.1), and, critically, lower LLM administrability.

**Cluster 2: LLM-Ready Benchmarks** (*n* = 168, 78.1%). The dominant cluster comprises benchmarks optimized for practical LLM evaluation: high administrability (0.952), high data availability (2.095), more complex response formats (1.661), but near-zero non-Western framework engagement (0.012) and zero indigenous content (0.000). These are the benchmarks that the field actually uses. Their near-total absence of non-Western moral content means that the operational evaluation infrastructure---the instruments that inform leaderboard rankings, safety assessments, and deployment decisions---is culturally monochrome.

The two-cluster structure exposes a structural bifurcation: benchmarks that engage substantively with non-Western moral traditions are methodologically distinct from benchmarks that are practically usable for LLM evaluation. The intersection---instruments that are simultaneously culturally substantive and LLM-administrable---contains approximately 15 benchmarks, fewer than 7% of the total. This is not a continuum with a thin middle; it is closer to two parallel literatures that have not yet converged.

## 4.2 The Measurement Invariance Gap

The most consequential finding of this meta-evaluation is psychometric, and it can be stated without qualification: of 218 benchmarks surveyed, precisely zero report measurement invariance testing.

Measurement invariance (MI) is the psychometric standard for determining whether an instrument measures the same construct across groups. In cross-cultural psychology, MI testing---typically conducted through multi-group confirmatory factor analysis (MGCFA) or differential item functioning (DIF) analysis---is considered a prerequisite for any cross-group comparison (Vandenberg and Lance 2000; Chen 2007). Without at least configural invariance (same factor structure across groups), metric invariance (same factor loadings), and ideally scalar invariance (same intercepts), observed score differences between groups are semantically uninterpretable. They could reflect genuine differences in the underlying construct, or they could reflect the instrument functioning differently across groups---and there is no way to distinguish between these possibilities without invariance evidence.

### What Zero Invariance Means

Consider a concrete case. Suppose a benchmark item asks whether "fairness requires treating everyone the same regardless of social position." In a Western liberal context, this item taps a rights-based equality construct. In a Confucian context, the same item may trigger a role-differentiated reciprocity interpretation, where fairness consists precisely in treating people differently according to their relational position (*li*). In an Ubuntu context, the item may invoke a communal redistribution logic, where fairness is about restoring balance within the community rather than ensuring identical individual treatment. When a Western participant and a Confucian participant both score "3" on this item, their scores are numerically identical but semantically incommensurable. They are not disagreeing about the same thing; they are agreeing about different things.

Without measurement invariance evidence, every cross-cultural score comparison in the existing benchmark literature is vulnerable to this interpretive collapse. When researchers report that "GPT-4 scores differently on moral dilemmas across cultural contexts," they are making an empirical claim that presupposes the instrument is measuring the same construct across those contexts. That presupposition is, at present, entirely unsubstantiated across the full 218-paper corpus.

### The Reliability Gradient

The broader psychometric picture offers only marginal consolation. Sixty-three benchmarks (28.9%) report any form of reliability; 26 (11.9%) report no validation whatsoever. The mean validation chain score---a composite of reliability evidence, invariance evidence, and LLM-specific validation---is 1.17 out of 3.0. No paper in the corpus achieves a perfect score.

An inverse relationship emerges between cultural ambition and psychometric grounding. Benchmarks with bicultural or limited cultural scope report reliability at 39.3%; those with multicultural scope report reliability at only 18.7%. The instruments that most urgently need psychometric validation---because they make the broadest cross-cultural claims---are the least likely to provide it.

### Not Ignorance, but Incentive

This failure is not attributable to ignorance. MI testing via MGCFA and DIF analysis has been standard practice in cross-cultural psychology for decades. The International Test Commission's Guidelines for Translating and Adapting Tests (2017) explicitly require invariance evidence for cross-group comparisons. The failure reflects a misalignment of incentives in ML benchmarking culture, where releasing a dataset with a leaderboard is more professionally rewarded than validating the instrument's psychometric properties. The time required to establish measurement invariance---collecting demographically stratified human responses, conducting iterative factor analyses, removing or revising non-invariant items---is incompatible with the publication cadence that drives ML conferences. The result is a field that has built an elaborate evaluation architecture on psychometric foundations that would not survive peer review in the discipline (cross-cultural psychology) that developed the methods being borrowed.

## 4.3 Non-Western Concept Coverage

To assess the substantive scope of the evaluation infrastructure, we mapped 44 moral concepts across seven non-Western ethical traditions and determined whether each concept has at least one operational benchmark measure---defined as a published instrument containing items that explicitly operationalize the concept in a form amenable to empirical testing.

The result: 3 of 44 concepts (6.8%) have any operational measure. The three measured concepts are *ren* (仁, Confucian humaneness/benevolence), *li* (禮, Confucian ritual propriety), and *ubuntu* (communal personhood). The remaining 41 concepts---spanning the moral vocabularies of traditions adhered to by the majority of humanity---are invisible to the evaluation infrastructure.

**Table 8** presents the full concept coverage matrix:

| Tradition | Total Concepts | Measured | Unmeasured | Coverage |
|-----------|---------------|----------|------------|----------|
| Confucian | 9 | 2 (*ren*, *li*) | 7 | 22.2% |
| Ubuntu | 5 | 1 (*ubuntu*) | 4 | 20.0% |
| Islamic | 7 | 0 | 7 | 0.0% |
| Dharmic | 6 | 0 | 6 | 0.0% |
| Buddhist | 6 | 0 | 6 | 0.0% |
| Indigenous/Relational | 6 | 0 | 6 | 0.0% |
| Buen Vivir | 5 | 0 | 5 | 0.0% |
| **Total** | **44** | **3** | **41** | **6.8%** |

Four entire traditions---Islamic ethics, Dharmic ethics, Buddhist ethics, and Indigenous relational ethics---have zero measured concepts. Buen Vivir, with zero as well, brings the total to five traditions with complete conceptual absence from the evaluation apparatus. The unmeasured concepts include *karma*, *dharma*, *maslahah* (public interest in Islamic jurisprudence), filial piety, *guanxi* (relational networks), *maqasid al-shariah* (higher objectives of Islamic law), *ihsan* (spiritual excellence), *pratityasamutpada* (Buddhist dependent origination), *sumak kawsay* (Andean well-being), and 32 others (Fig. 6). These are not obscure philosophical technicalities; they are the organizing principles of moral reasoning for billions of people.

## 4.4 Tradition Coverage Matrix

### Confucian Ethics

Confucian ethics is the best-represented non-Western tradition, with 30 dedicated benchmarks---a number driven substantially by the growth of Chinese NLP research producing instruments grounded in Chinese moral philosophy. Key instruments include CVC (Chinese Value Corpus), CMoralEval, WYWEB (Classical Chinese evaluation), and C3Bench. However, the coverage is paradoxically shallow. Only 2 of 9 mapped Confucian moral concepts (*ren* and *li*) have operational measures. Filial piety (*xiao*)---arguably the concept most consequential for AI advisory systems serving East Asian users---remains unmeasured, along with harmony (*he*), face (*mianzi*), relational networks (*guanxi*), righteousness (*yi*), wisdom (*zhi*), and trustworthiness (*xin*). Instruments such as CVC and CMoralEval measure cultural knowledge and moral judgment in Chinese contexts, but they do not operationalize the relational ontology that distinguishes Confucian ethics from Western moral philosophy. They test whether a model knows what Confucian concepts mean, not whether it can reason within the relational framework those concepts presuppose (Table 8).

### Islamic Ethics

Six benchmarks address Islamic ethical content, serving a tradition of 1.9 billion adherents. IslamTrust (Lahmar 2025), MELAC (Farsi 2025), and Sacred or Synthetic represent the most substantive instruments. Yet all seven mapped Islamic moral concepts remain without operational measures: *maslahah* (public interest), *maqasid al-shariah* (the five higher objectives), *ihsan* (spiritual excellence), *tawakkul* (trust in divine wisdom), *adl* (justice), the *halal/haram* distinction (permissible/forbidden), and *shura* (consultative governance). IslamTrust comes closest to tradition-internal evaluation, measuring alignment with Islamic values across the five *maqasid* dimensions, but it assesses conformity to Islamic normative positions rather than the capacity to reason within the *usul al-fiqh* (principles of Islamic jurisprudence) that generate those positions. The distinction matters: an LLM that produces Islamically compliant outputs without engaging the reasoning process by which Islamic scholars derive those positions is performing mimicry, not moral reasoning.

### Buddhist Ethics

Thirteen benchmarks engage Buddhist content---the second-highest tradition count---but all test factual knowledge about Buddhist doctrines rather than reasoning within Buddhist moral frameworks. BuddhismEval (Xiong 2025) assesses knowledge of Buddhist teachings across Theravada, Mahayana, and Vajrayana traditions. HBC (Humanistic Buddhism Corpus; Wong 2024) evaluates understanding of Humanistic Buddhist thought. MITRA-zh-eval addresses Buddhist content within Chinese NLP evaluation. None operationalizes the six mapped Buddhist moral concepts: the Four Noble Truths as an analytical framework for moral reasoning (not merely a doctrinal proposition), the Eightfold Path as a structure for ethical deliberation, compassion (*karuna*) as an epistemic orientation rather than a sentiment, mindfulness as a mode of moral attention, non-attachment as a criterion for evaluating motivations, and interdependence (*pratityasamutpada*) as a meta-ethical principle. The gap between knowing that Buddhism teaches compassion and reasoning from compassion as an ontological ground is precisely the gap the evaluation infrastructure has not bridged.

### Indigenous/Relational Ethics

Six benchmarks address Indigenous ethical content. Ray (2025), the highest-ranked benchmark in our TOPSIS analysis (Section 4.7), provides a conceptual framework for integrating Maori and Navajo knowledge systems into AI governance. Neira-Davila (2025) addresses Indigenous knowledge systems in Latin American contexts. However, no benchmark in the corpus reports compliance with the CARE Principles (Carroll et al. 2020) for Indigenous data governance---the community-endorsed framework for ethical research involving Indigenous knowledge. All six mapped Indigenous moral concepts remain unmeasured: relationality, land-based ethics, intergenerational obligation, ceremony as moral practice, reciprocity, and kinship as ethical structure. A deeper structural challenge confronts Indigenous benchmark development: Indigenous ethical traditions emphasize radical locality---the inseparability of moral knowledge from specific places, peoples, and practices. Benchmarking, which requires abstraction and standardization, treats this locality as a methodological obstacle rather than as a constitutive feature of the moral framework. Whether psychometric instruments designed for universalist application can ever adequately capture Indigenous moral reasoning is an open question that the field has not yet confronted.

### Ubuntu Ethics

Five benchmarks engage Ubuntu philosophy. UbuntuGuard (Eickhoff 2026) represents the most advanced tradition-specific instrument in the corpus, operationalizing Ubuntu as a policy evaluation framework. Decolonizing NLP (Ogunremi 2025) engages Ubuntu principles within language technology development. Yet four of five mapped Ubuntu concepts remain unmeasured: communal identity, collective responsibility, elder wisdom, and reconciliation. A fundamental methodological problem persists: Ubuntu's unit of moral analysis is not the individual but the community (*umuntu ngumuntu ngabantu*---a person is a person through other persons). Benchmark instruments that elicit individual model responses to discrete items presuppose an individualist moral ontology that is structurally incompatible with Ubuntu's relational ontology. An Ubuntu-grounded evaluation instrument would need to assess the quality of communal deliberation, not the accuracy of individual judgments---a format that no existing LLM evaluation paradigm supports.

### Dharmic Ethics

Four benchmarks address Dharmic ethical content, including Fluent but Foreign (Agarwal 2025) and JainGPT. All six mapped concepts remain unmeasured: *dharma* (contextual duty), *karma* (moral causation), *ahimsa* (non-violence), *moksha* (liberation), *seva* (selfless service), and *satya* (truth). The conceptual challenge for Dharmic benchmark development is distinctive: *svadharma* (one's own dharma, or role-situated duty) is fundamentally non-universalizable. A Brahmin's dharmic obligation differs from a Kshatriya's, which differs from a householder's, which differs across life stages (*ashrama*). This context-dependence is not a limitation of Dharmic ethics but its central feature---a feature that resists operationalization in instruments designed to yield context-independent scores.

### Buen Vivir

Two benchmarks---Ray (2025) and Neira-Davila (2025)---reference Buen Vivir (*Sumak Kawsay*), the Andean cosmovision of well-being as harmony among humans, community, and the natural world. All five mapped concepts remain unmeasured: *sumak kawsay* itself, harmony with nature, community well-being, rights of nature, and plurinationality. The sparseness of benchmark engagement with Buen Vivir (2 of 218 papers) is overdetermined: the tradition has comparatively few adherents with access to NLP publication venues, it is epistemologically distant from the individualist-rationalist framework that benchmarking presupposes, and---as several scholars within the Buen Vivir intellectual tradition have argued---the very act of extracting moral principles from their relational context for insertion into a standardized evaluation instrument may be ontologically incompatible with Buen Vivir's anti-extractivist commitments. Benchmarking, in this view, is not a neutral methodology; it is a colonial epistemological practice that reduces living moral traditions to scoreable propositions.

## 4.5 Geographic Concentration of Benchmark Creation

The geographic distribution of benchmark creators reveals a concentration of evaluative power that mirrors---and in some respects exceeds---the geographic skew documented in Study 1:

**Table 9.** Geographic distribution of benchmark creation.

| Region | Count | % of Total |
|--------|-------|-----------|
| North America | 86 | 39.4% |
| East Asia | 42 | 19.3% |
| Western Europe | 35 | 16.1% |
| South Asia | 18 | 8.3% |
| MENA | 9 | 4.1% |
| Southeast Asia | 7 | 3.2% |
| Oceania | 5 | 2.3% |
| Latin America | 3 | 1.4% |
| Sub-Saharan Africa | 2 | 0.9% |
| Eastern Europe | 1 | 0.5% |

North America and Western Europe collectively produce 55.5% of all benchmarks. Sub-Saharan Africa (0.9%) and Latin America (1.4%), representing 18% and 8% of the global population respectively, are nearly invisible as benchmark creators. East Asia is notably overrepresented relative to its presence in the broader AI ethics literature (+6.6 percentage points), driven by the growth of Chinese NLP benchmarking.

A second-order finding is more telling: 52.3% of benchmarks focused on non-Western values are created by Western institutions. Of 172 benchmarks with any non-Western content, 90 originate from institutions in North America and Western Europe. This asymmetry carries epistemological consequences. The framing of moral concepts---what counts as a "correct" answer, which dimensions are measured, what response formats are offered---is shaped by the creator's epistemological commitments. A Western researcher operationalizing filial piety may inadvertently frame it as a spectrum from "autonomous" to "obedient" (a liberal framing) rather than from "incomplete personhood" to "fully realized relational self" (a Confucian framing). The resulting instrument measures deviation from liberal autonomy norms rather than engagement with Confucian relational ethics---and neither the creator nor the user may recognize the distortion.

Community participation provides one corrective, but it is rarely employed. Only 15 of 218 benchmarks (6.9%) show evidence of community participatory design---meaning that the tradition-bearing communities being evaluated had meaningful input into instrument design, item selection, or validation. The remaining 93.1% were designed without systematic consultation with the cultures being measured.

## 4.6 Evaluation Depth and Structural Assumptions

Beyond coverage gaps, the evaluation infrastructure embeds structural assumptions that systematically disadvantage non-Western moral traditions.

### Unit of Moral Agency

Among deep-scored papers, the dominant unit of moral agency is "model" (50%) or "LLM" (12.5%). "Community" appears as the unit of agency in exactly one paper. This framing presupposes an individual decision-maker as the locus of moral action---an assumption that aligns with Western liberal ethics but contradicts the moral ontologies of at least three major traditions. Ubuntu ethics locates moral agency in the community (*umuntu ngumuntu ngabantu*); Confucian ethics locates it in the relational dyad (the *wu lun*, or five cardinal relationships); Indigenous ethical traditions locate it in kinship networks that extend across generations and include non-human beings. When a benchmark asks "what should the model do?", it has already imported a moral ontology that excludes these alternatives. The question itself is culturally loaded.

### Response Format

Scenario and dilemma formats dominate (46.3% of papers), followed by multiple-choice and question-answering (10.1%). Among specific response types, forced-choice formats prevail: 36 papers use multiple choice, 23 use binary selection. Forced-choice formats strip away the deliberative process, reducing moral reasoning to a single selected endpoint. This is problematic for traditions in which the quality of moral deliberation matters as much as---or more than---the conclusion reached. In Ubuntu ethics, the process of communal *indaba* (deliberation) is itself a moral act; the decision is inseparable from the relational process that produced it. In Confucian ethics, the cultivation of moral character through *li* (ritual practice) cannot be captured by selecting option A or B. In Buddhist ethics, the quality of attention and the absence of attachment in deliberation are morally significant independent of the action chosen.

### Ecological and Intergenerational Scope

Only 2 papers (0.9%) address ecological moral dimensions. Zero papers (0.0%) address intergenerational moral scope. These absences render the evaluation infrastructure blind to moral dimensions that are foundational for several non-Western traditions. Buen Vivir (*Sumak Kawsay*) is fundamentally about harmony between humans and the natural world; it cannot be meaningfully evaluated by instruments that exclude ecological relationships. Indigenous relational ethics in many traditions extends moral obligations to land, water, and non-human beings. Buddhist interdependence (*pratityasamutpada*) includes all sentient beings within its moral scope. The zero-coverage of intergenerational obligation is particularly consequential: obligations to ancestors and future generations structure moral reasoning in Confucian, Indigenous, Dharmic, and Buddhist traditions. An evaluation infrastructure that measures only synchronic moral judgments---what is right *now*, for *present* agents---cannot detect moral reasoning that operates across temporal horizons spanning seven generations or more.

### Moral Reasoning Level

Most benchmarks test norm recognition---whether the model can identify which cultural norms apply in a described scenario---rather than moral reasoning within a normative framework. The distinction is between knowledge ("Confucian ethics values filial piety") and understanding ("given the obligation of filial piety, how should one navigate the competing demands of an aging parent and a professional duty that serves the broader community?"). The former can be answered from an encyclopedia; the latter requires reasoning within the moral framework's own logic, weighing its internal principles, and arriving at a judgment that the tradition's practitioners would recognize as legitimate. The evaluation infrastructure overwhelmingly tests the former.

## 4.7 Rankings and the Pareto Frontier

### Top Benchmarks

TOPSIS ranking with ELECTRE III concordance/discordance veto thresholds, using weights reflecting alignment relevance (0.20), cross-cultural scope (0.20), non-Western coverage (0.15), LLM administrability (0.12), psychometric quality (0.10), evaluation depth (0.10), data availability (0.08), and epistemic provenance (0.05), yielded the following top 10:

**Table 10.** Top 10 benchmarks by TOPSIS score.

| Rank | Benchmark | TOPSIS | Key Strength |
|------|-----------|--------|-------------|
| 1 | Ray---Indigenous Knowledge Systems | 0.637 | Highest cultural scope + NW coverage |
| 2 | Wu---CVC (Chinese Value Corpus) | 0.597 | Chinese values, LLM-ready |
| 3 | Yu---CMoralEval | 0.569 | Chinese moral evaluation, data |
| 4 | Catapang---EMoTES-3K | 0.568 | Filipino emotion/morality |
| 5 | Alam---RAG to Agentic RAG | 0.565 | Islamic knowledge |
| 6 | Rahman---CCD-Bench | 0.553 | Cultural conflict, 37 countries |
| 7 | Lahmar---IslamTrust (v1) | 0.547 | Islamic values alignment |
| 8 | Lahmar---IslamTrust (v2) | 0.547 | Islamic values alignment |
| 9 | Rao---NormAd | 0.545 | Social norms, 37 countries |
| 10 | Liu---JMedEthicBench | 0.537 | Japanese medical ethics |

The top-ranked benchmark---Ray (2025), a framework for indigenous knowledge systems in AI governance---illustrates the core tension of the evaluation landscape. It scores highest on cross-cultural scope and non-Western coverage, reflecting the most substantive engagement with non-Western moral ontologies in the corpus. It also has zero LLM administrability and zero data availability. The most culturally substantive benchmark in the field cannot currently be used to evaluate a language model.

### The Pareto Frontier

Seven benchmarks constitute the Pareto frontier---the set of instruments that are non-dominated across four key dimensions (cultural scope, psychometric quality, data availability, non-Western framework count):

1. **NormAd** (Rao 2025)---highest effectiveness index (39.38), strongest balance of scope and administrability
2. **CCD-Bench** (Rahman 2025)---cultural conflict scenarios across 37 countries
3. **EMoTES-3K** (Catapang 2023)---Filipino moral emotion evaluation
4. **MITRA-zh-eval** (Keutzer 2025)---Buddhist content within Chinese NLP
5. **Neira-Davila** (2025)---Indigenous knowledge systems, Latin American context
6. **HBC** (Wong 2024)---Humanistic Buddhism corpus
7. **Ray** (2025)---Indigenous governance framework

No single benchmark dominates across all dimensions. The Pareto frontier visualizes the structural trade-off that defines the current evaluation landscape: cultural depth and practical usability are negatively correlated. The most culturally substantive benchmarks (Ray, Neira-Davila) lack data availability and LLM administrability. The most administrable benchmarks (NormAd, CCD-Bench) have limited non-Western framework depth. Rank stability across five alternative weight schemes is high (Kendall's *W* = 0.924), confirming that this trade-off is robust to weighting assumptions.

### Counter-Hegemonic Benchmarks

Despite the dominance of Western-created instruments, a counter-hegemonic movement is visible in the lower ranks of the corpus. Benchmarks such as IslamTrust (Lahmar 2025), created by researchers positioned within Islamic scholarly traditions, and UbuntuGuard (Eickhoff 2026), grounded in Southern African moral philosophy, represent qualitatively different evaluation instruments. They do not treat non-Western values as exotic variants of Western liberalism to be catalogued and scored; they treat them as autonomous moral systems with their own internal coherence, their own standards of reasoning, and their own criteria for evaluative adequacy. IslamTrust evaluates alignment across the five *maqasid* not as a checklist of cultural preferences but as a structured moral framework with its own jurisprudential logic. UbuntuGuard assesses policy compliance through the lens of communal obligation rather than individual rights.

These instruments are not yet competitive with the Cluster 2 LLM-ready benchmarks on administrability or data availability metrics---not because they are methodologically inferior, but because the infrastructure of open datasets, standardized prompt formats, and automated scoring rubrics has been built around Western evaluation paradigms. The counter-hegemonic benchmarks must build their own infrastructure while the dominant benchmarks inherit theirs.

## Transition to Study 3

Study 2 reveals that the evaluation infrastructure for cross-cultural values alignment lacks basic psychometric validity---zero measurement invariance across 218 benchmarks---and covers only 6.8% of non-Western moral concepts across seven major traditions. Five traditions have zero measured concepts. The instruments that are culturally substantive are not practically usable; the instruments that are practically usable are not culturally substantive. The geographic concentration of benchmark creation (55.5% North America and Western Europe) and the near-absence of community participatory design (6.9%) compound these structural limitations.

But even within the limited benchmarks that do exist, how do RLHF-aligned language models actually perform when confronted with cross-cultural moral content? The evaluation infrastructure may be broken, but the fragments that remain can still be administered. Study 3 examines this empirically, self-administering 10 benchmark instruments (380 items across 7 non-Western traditions) to a state-of-the-art RLHF-aligned model and documenting the systematic patterns that emerge when an aligned system encounters moral traditions it was not aligned to recognize.
