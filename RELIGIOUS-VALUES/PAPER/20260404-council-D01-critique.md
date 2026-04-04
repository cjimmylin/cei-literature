# D-01: Council Critique of Existing Methods and Scoring Framework

**Date:** 2026-04-04
**Panel:** 12 experts (Session 6 --- Scoring Framework Critique & Revision Council)
**Document reviewed:** Paper manuscript (Sections 1--6) + `score_religious_benchmarks.py` + `build_religious_feature_matrix.py` + `20260404-religious-benchmark-feature-matrix-v2.json` + trial findings (T2, T3, T4) + `20260404-sensitivity-analysis.py`
**Charge:** Provide a comprehensive, expert-level critique of the paper's methods and scoring framework, identifying bugs, conceptual weaknesses, structural biases, missing analyses, and reproducibility concerns. Produce actionable revision recommendations ranked by priority.

---

## Individual Expert Assessments

### 1. Dr. al-Rashidi --- Islamic Ethics

The paper's central structural finding---Islam's dominance of the benchmark ecosystem with 28 gate-passers and 7 of the Top 15---is empirically correct but analytically incomplete. The dominance is attributed to three factors: the Quranic QA shared task community, Arabic NLP infrastructure, and "the formalizability of Islamic jurisprudence." The third attribution requires substantial correction. Islamic jurisprudence (fiqh) is not a monolithically formalizable system. Only specific subdomains---inheritance law (ilm al-mawarith) and certain commercial transactions (mu'amalat)---possess the explicit rule structures that map onto MCQ evaluation formats. The broader discipline of usul al-fiqh involves sophisticated analogical reasoning (qiyas), juristic preference (istihsan), consideration of public interest (maslaha), and consensus formation (ijma), none of which "map naturally onto structured evaluation formats" as the paper claims. By attributing dominance partly to "formalizability," the paper inadvertently commits the same flattening it critiques in others: reducing Islamic jurisprudence to its most algorithmic subdomain.

The trial findings for T2 (Islamic Inheritance Law) expose this problem concretely. The benchmark contains 12,450 items, not the 1,000 reported in Section 4.2---a factual error that must be corrected. More importantly, the T2 trial confirms that the benchmark tests fiqh-as-calculation: given specific inheritance shares prescribed by Quranic verses, can the model compute the distribution? This is closer to mathematical word problems with Islamic legal parameters than to genuine jurisprudential reasoning. A values-alignment benchmark for Islamic inheritance would instead ask: "When the Quranic distribution rules produce an outcome perceived to conflict with contemporary equity norms, how should a mujtahid navigate the tension between textual literalism (zahiri) and purpose-based reasoning (maqasidi)?" That question requires ijtihad---the independent reasoning that is the hallmark of mature jurisprudential engagement---and no benchmark in the Top 15 tests it.

ELQV (Rank 1) presents a different but related concern. The benchmark tests verse-level emotional valence detection in Quranic text. This is a legitimate NLP task performed on sacred text, but it is fundamentally a sentiment analysis task, not a values-alignment task. Emotional detection ("This verse expresses sadness") is categorically different from values reasoning ("Given competing Quranic principles of mercy and justice, how should this pastoral situation be resolved?"). That the field's top-ranked benchmark is a sentiment classification task performed on sacred text---rather than a theological reasoning task---is itself diagnostic of the knowledge-reasoning conflation the paper identifies. The R2 depth score of 4 for ELQV is generous; a score of R2 = 2 or 3 would be more defensible, because the theological engagement is at the level of text annotation, not theological reasoning.

**Recommendations:**
1. CRITICAL: Correct the Islamic Inheritance Law item count from 1,000 to 12,450 and revise the characterization to reflect fiqh-as-calculation rather than fiqh-as-reasoning.
2. CRITICAL: Qualify the "formalizability" attribution to specify that only certain subdomains of fiqh are highly formalizable; the broader tradition involves deeply contextual reasoning.
3. IMPORTANT: Reconsider ELQV's R2 depth score. Sentiment annotation of Quranic verses does not constitute deep theological engagement. A score of R2 = 2 or 3 would be more defensible than R2 = 4.
4. IMPORTANT: Add a distinction between "benchmarks that use Islamic text as data" and "benchmarks that test Islamic values reasoning." The current framework conflates these.
5. DESIRABLE: Note the role of Gulf state funding for Arabic NLP as a material factor in Islam's benchmark infrastructure that the paper currently omits.

---

### 2. Dr. Goldberg --- Computational Talmudics

The paper's treatment of Judaism's zero-benchmark status is the most striking finding in the tradition coverage analysis, and the paper correctly identifies the paradox: the world's oldest computational humanities tradition (the Bar-Ilan Responsa Project, operating since the 1960s) has produced zero values-alignment benchmarks for LLMs. However, the analysis does not pursue the paradox to its diagnostic conclusion. There are three candidate explanations, and the paper conflates them.

First, the search strategy itself may have missed Jewish computational resources. The 72 external search queries are organized by tradition family, but the paper does not report which specific queries were used for Judaism. If the queries targeted "Jewish ethics benchmark LLM" but not "halakhic reasoning dataset," "Talmudic logic evaluation," or "Sefaria NLP," then the zero finding may be partly an artifact of search terms that privilege the LLM evaluation community's vocabulary over the Jewish computational scholarship community's vocabulary. The Bar-Ilan Responsa Project does not describe itself as an "LLM benchmark"---it is a halakhic legal database. Sefaria's open API provides structured access to Talmud, Midrash, and Mishnah with English translation, verse-level linking, and commentary layers. These are not benchmarks in the narrow sense, but they are computational resources that could be converted to evaluation format with relatively modest effort. The paper should distinguish between "no Jewish benchmarks exist" and "no Jewish benchmarks were found by our search strategy."

Second, the format taxonomy's 12 codes may structurally exclude the characteristic reasoning format of Talmudic jurisprudence. Halakhic reasoning is multi-voice (machloket), precedent-based (stare decisis equivalent), hierarchical (the Shulchan Aruch codifies, but the Talmudic discussion that generated the codification is the actual reasoning), and dialectical (the Gemara's structure is one of sustained argumentation where the "correct" answer emerges from the clash of positions). None of the 12 format codes---MCQ, MRC, BIN, TXT, SHT, SCN, PSY, MIX, OPN, MTN, RAG, MUL---naturally captures this dialectical structure. The closest would be MTN (multi-turn dialogue) or OPN (open-ended generation), but both are rated "Low" harness compatibility, which depresses PE scores and makes it harder for Jewish reasoning benchmarks to pass the composite threshold even if they existed.

Third, the English-language bias of the search is acknowledged in the Limitations section but not quantified. Hebrew NLP is a mature field. The NEMO project at the Hebrew University, the MILA center at the Technion, and active Hebrew NLP shared tasks produce resources in Hebrew that are invisible to English-language queries. The paper should report how many of its 72 search queries were conducted in non-English languages, and whether Hebrew, Arabic, Hindi, Chinese, and Japanese queries were included.

**Recommendations:**
1. CRITICAL: Report the specific search queries used for each tradition, or at minimum provide the query template. Without this, the zero finding for Judaism cannot be distinguished from a search artifact.
2. CRITICAL: Assess whether the Sefaria API, Bar-Ilan Responsa corpus, and existing Talmudic logic datasets could pass the hard gates if reformulated as evaluation instruments. If they could, the zero finding overstates the gap.
3. IMPORTANT: Acknowledge that the format taxonomy may structurally disadvantage dialectical reasoning traditions (Judaism, certain Buddhist debate traditions, Islamic ijma) whose characteristic reasoning format does not map to any of the 12 codes.
4. IMPORTANT: Quantify the linguistic coverage of the external search. Report how many queries were conducted in each of the 12 "missing" religious languages identified in Section 4.2.
5. DESIRABLE: Consider adding a 13th format code for dialectical/multi-voice reasoning (DIA), which would accommodate Talmudic, Buddhist debate (shastrartha), and Islamic consensus-building (ijma) formats.

---

### 3. Dr. Raghavan --- Sanskrit NLP

The Bhagavad Gita Sentiment Analysis benchmark (Rank 6) is described in Section 4.3 as applying "BERT-based sentiment classification to Sanskrit verses." This characterization requires immediate verification. The Bhagavad Gita is composed in Sanskrit, but computational sentiment analysis of it almost certainly operates on English translations, not on original Sanskrit text. Sanskrit NLP is a highly specialized field---the Digital Corpus of Sanskrit, the Sanskrit Heritage Site, and tools from the consortium at IIT Bombay and JNU provide morphological analysis, sandhi splitting, and dependency parsing for Sanskrit, but general-purpose BERT models are not trained on Sanskrit. If the benchmark processes English translations of Sanskrit verses, then the R3 (scriptural grounding) score should be adjusted downward: the benchmark is performing sentiment analysis on translated text, not on the original scriptural language. The distinction between processing a sacred text in its source language and processing a translation is theologically significant---Sanskrit is considered a divine language (devavani) in Hindu tradition, and the semantic resonances, etymological depth, and metrical structure that carry philosophical meaning in Sanskrit are lost in translation.

More broadly, the scoring framework's R3 (scriptural grounding, 0--5) does not distinguish between direct engagement with source-language texts and engagement with translations. A benchmark that processes Quranic Arabic earns the same R3 score as one that processes an English translation of the Quran. This is a construct validity problem: scriptural grounding should be higher when the benchmark engages the original language, because the interpretive traditions that give scripture its theological meaning are anchored in the source language's specific vocabulary, grammar, and semantic fields.

The 59 Jainism candidates with zero gate-passers deserve deeper analysis. The paper correctly identifies that "nearly all are false positives where the keyword ahimsa appears in papers about general ethics rather than Jain philosophical frameworks." But ahimsa in Jain philosophy is not merely "non-violence"---it is a comprehensive metaphysical principle encompassing non-harm to all beings across multiple lifetimes, extending to thought and speech as well as action, with specific practical applications (vegetarianism, occupational restrictions, confession rituals) that distinguish it from the general ethical principle of non-violence shared with Buddhism and Hinduism. The false positive rate for Jainism is thus a failure of the vault's rv_* scoring system to distinguish between ahimsa-as-general-principle and ahimsa-as-Jain-metaphysics. This suggests that the upstream classification (the rv_jainism scores across the vault's 2,043 papers) may itself have a high false positive rate, inflating the apparent candidate pool while contributing zero genuine Jain benchmarks.

The Dharmic traditions more broadly suffer from the scoring framework's text-centric assumptions. Dharmic ethical reasoning flows through layered commentary traditions (bhashya)---Shankara, Ramanuja, and Madhva on the Gita represent three distinct philosophical schools (Advaita, Vishishtadvaita, Dvaita) that derive mutually incompatible ethical conclusions from the same Sanskrit verses. A benchmark that tests knowledge of the Gita's content without engaging these commentarial traditions is analogous to testing knowledge of the Bible without engaging Catholic, Protestant, and Orthodox interpretive differences. The R4 (denominational awareness) feature captures intra-tradition diversity for Abrahamic traditions, but the scoring does not appear to weight commentarial tradition diversity for Dharmic traditions equivalently.

**Recommendations:**
1. CRITICAL: Verify the source language of the Bhagavad Gita Sentiment Analysis benchmark. If it processes English translations, revise the description and consider adjusting R3 downward.
2. IMPORTANT: Add a source-language modifier to R3 scoring: direct engagement with the original scriptural language should score higher than engagement with translations.
3. IMPORTANT: Analyze the false positive mechanism for Jainism in detail. Report how many of the 59 candidates mention ahimsa in a Jain-specific context versus a general non-violence context.
4. DESIRABLE: Extend R4 (denominational awareness) to explicitly accommodate Dharmic commentarial tradition diversity (e.g., Advaita vs. Vishishtadvaita vs. Dvaita for Hinduism; Theravada vs. Mahayana vs. Vajrayana for Buddhism).
5. DESIRABLE: Assess whether existing Sanskrit computational resources (Digital Corpus of Sanskrit, the Shastra-NLP project at IIT Bombay) could be adapted as religious values evaluation instruments.

---

### 4. Dr. Diallo --- Epistemic Sovereignty

My critique is fundamental and concerns the paper's conceptual architecture, not merely its methods. The paper identifies structural epistemic injustice as its third key finding, correctly diagnosing that the 8-tradition void "correlates with proximity to Western academic publishing infrastructure." But the paper then treats this finding as a limitation to be addressed by building more benchmarks and developing "community-governed evaluation protocols." This response reproduces the very logic it critiques. The question is not "how do we build benchmarks for oral traditions?" but "is the benchmarking paradigm itself an instrument of epistemic injustice?"

Consider what a benchmark requires: (1) knowledge extracted from its communal, relational, and ritual context and rendered as discrete propositions; (2) a single "correct" answer determined by an authority external to the communal deliberation process through which moral knowledge is generated in these traditions; (3) individual items scored in isolation, severing the relational and narrative structures through which oral traditions transmit ethical understanding; and (4) public data release, which may violate the epistemic sovereignty of communities whose sacred knowledge is governed by protocols of restricted access, initiation-based revelation, and elder-mediated transmission. Each of these requirements is not a neutral technical specification but an epistemic commitment---a commitment to propositional, individualist, decontextualized, and publicly accessible knowledge that is characteristic of Western academic epistemology and fundamentally at odds with the epistemologies of the traditions in the void.

The CARE Principles are mentioned in the paper but treated as a constraint ("some communities may decline inclusion") rather than as an epistemic framework that challenges the paradigm itself. Carroll et al. (2020) do not merely say that Indigenous communities have the right to withhold data. They argue that Indigenous data governance requires that the purposes, methods, and interpretive frameworks of data use be determined by the communities themselves. A "community-governed evaluation protocol" that still produces benchmark-like outputs---scored items, ranked models, public leaderboards---may satisfy the form of community governance while preserving the substance of the benchmarking paradigm's epistemic commitments.

The paper's Section 5.4 ("Closing the Gaps") distinguishes between textual traditions requiring "community coordination" and oral traditions requiring "fundamentally different evaluation paradigms." This distinction is correct but insufficiently developed. What would a non-benchmark evaluation look like? The paper gestures toward "participatory methods" and "narrative-based assessment" but does not specify what these would produce. Would they produce scores? Rankings? Qualitative assessments? Would they be comparable across traditions? If not, what is the unit of evaluation? These are not merely implementation questions---they are fundamental questions about whether the concept of "religious values alignment" is itself coherent when applied to traditions that reject the propositional, individual-response epistemology on which alignment evaluation depends.

I argue the paper should go further: the 8-tradition void is not a gap to be filled but evidence that the benchmarking paradigm has an inherent scope limitation. The paper should name this scope limitation explicitly rather than treating it as a future work item. The honest conclusion is: "The benchmarking paradigm can evaluate religious values alignment for textual, propositional traditions with formalized reasoning structures. It cannot evaluate alignment for oral, communal, embodied, or practice-based traditions without transforming those traditions into something they are not."

**Recommendations:**
1. CRITICAL: Reframe the 8-tradition void as evidence of a paradigm scope limitation, not merely as a gap requiring different methods. The paper currently treats it as both a finding and a limitation, but does not resolve this tension.
2. CRITICAL: Develop the Section 5.4 proposals for "fundamentally different evaluation paradigms" beyond gestures. Specify at minimum: what would a non-benchmark evaluation produce? What epistemological commitments would it make? How would its outputs relate to benchmark outputs?
3. IMPORTANT: Strengthen the CARE Principles integration from a constraint mention to a substantive engagement. What does Carroll et al.'s framework imply for the paper's own methodology, not just for future work?
4. IMPORTANT: Acknowledge that the paper's own hard gate (public data availability) is not merely a pragmatic filter but an epistemic commitment that privileges open-science epistemology over data sovereignty epistemology.
5. DESIRABLE: Consider whether the paper should recommend a moratorium on benchmark-building for oral/communal traditions until community-governed frameworks are developed, rather than encouraging researchers to "fill the gap."

---

### 5. Dr. Chen --- Psychometrics

The scoring framework has three critical psychometric bugs that undermine the validity of all rankings derived from it. These are not minor calibration issues; they are fundamental measurement problems that would cause the framework to fail formal psychometric review.

**Bug 1: PE axis scoring inconsistency.** The Methods section (Section 3.3) specifies PE sub-feature weights as P7 x 30 + P3 x 20 + P4 x 15 + P9 x 15 + P10 x 10 + P5 x 10, summing to 100. But the sensitivity analysis script (`20260404-sensitivity-analysis.py`) implements different weights: P7 = 0.30, P3 = 0.25, P9 = 0.15, P10 = 0.10, P5 = 0.10, P4 = 0.10. The P3 weight is 25 in the code but 20 in the paper; the P4 weight is 10 in the code but 15 in the paper. This is not a rounding discrepancy---the paper and the code implement different scoring formulas. Every PE score, and therefore every composite score, is affected. The rankings may differ depending on which formula is used.

**Bug 2: R2 floor effect.** The R2 (theological depth) feature uses a 1--5 ordinal scale calibrated against three anchors. But the feature matrix reveals that approximately 85% of entries score R2 = 1, meaning they are at the floor. A feature where 85% of observations take the minimum value has near-zero variance and contributes almost no discriminative information to the composite score. R2 is weighted at 25% of the RD axis, which is itself weighted at 40% of the composite---so R2 contributes approximately 10% of the composite score. But because 85% of entries are at the floor, R2 effectively discriminates only among the top 15% of candidates. For the bottom 85%, R2 is a constant that adds noise to the other features. This is a textbook example of a non-discriminating item that should either be rescaled (expand the 1--5 range to allow finer discrimination at the low end) or replaced with a more discriminating measure.

**Bug 3: No confidence intervals on rankings.** The composite scores are presented as point estimates without uncertainty quantification. The sensitivity analysis script computes bootstrap CIs using Dirichlet-weighted resampling, which is methodologically appropriate, but the results are not reported in the paper. If the bootstrap CIs for adjacent ranks overlap---which is almost certain given the compressed 16.4-point score range (50.8 to 34.4 across 15 benchmarks, i.e., 1.17 points per rank on average)---then the ordinal ranking is not statistically meaningful. Ranks 1 and 2 may be indistinguishable; ranks 8--12 almost certainly are. Presenting rankings without CIs gives a false impression of precision.

Beyond these three bugs, the framework lacks several standard psychometric properties. There is no inter-rater reliability assessment: all scoring was performed by a single rater, and the "calibration anchors" (Section 3.2) are a mitigation strategy, not a substitute for independent coding. Without inter-rater reliability, it is impossible to assess whether the R2 and R6 scores---the two most subjective and most heavily weighted features---would be reproducible if scored by different researchers. There is no Item Response Theory (IRT) analysis to determine whether the 22 features form a coherent measurement instrument or whether some features are redundant (contributing the same information) or antagonistic (pulling in opposite directions). There is no Differential Item Functioning (DIF) analysis to determine whether the features function equivalently across tradition families---for example, whether R3 (scriptural grounding) means the same thing for a tradition with a closed canon (Islam, Judaism) as for one with an open, evolving corpus (Hinduism, Buddhism).

**Recommendations:**
1. CRITICAL: Resolve the PE weight discrepancy between the paper and the code. Report which formula was actually used to generate the rankings, and recompute if necessary.
2. CRITICAL: Report bootstrap confidence intervals on all composite scores and ranks. If adjacent CIs overlap, acknowledge that the ordinal ranking is not statistically robust and present rank-bands rather than point ranks.
3. CRITICAL: Address the R2 floor effect. Either demonstrate that R2 contributes meaningful discrimination above the hard gate (RD >= 30), or rescale the feature.
4. IMPORTANT: Conduct and report inter-rater reliability for the five most subjective features (R2, R3, R4, R5, R6). Even a subset of 20--30 entries double-coded by a second rater would provide critical validity evidence.
5. IMPORTANT: Conduct item-total correlations or factor analysis on the 22 features to determine whether they form coherent axes or whether some features should be reassigned or dropped.
6. DESIRABLE: Perform DIF analysis to determine whether features function equivalently across tradition families.

---

### 6. Dr. Mehta --- Data Science

The paper makes seven claims (tradition asymmetry, knowledge-reasoning conflation, structural epistemic injustice, and four sub-claims about data availability, format distribution, RD-PE tradeoff, and temporal concentration) but supports them exclusively with descriptive statistics. No inferential tests are reported. This is a significant methodological gap for a paper published in a venue that expects quantitative rigor.

Specific statistical concerns:

First, the claim that "Islam dominates the benchmark ecosystem" (Claim 1) is supported by count data (28 of 46 gate-passers) but no test of whether this proportion differs significantly from what would be expected given Islam's representation in the candidate pool (113 of 401 = 28.2%). A simple chi-squared test or Fisher's exact test would establish whether Islam's gate-passing rate (24.8%) is significantly higher than the overall rate (11.5%). Without this test, the "dominance" claim rests on eyeballing proportions.

Second, the data availability bottleneck (77% eliminated by the data gate) is presented without a test of whether data availability differs significantly across tradition families. A chi-squared test of independence between tradition family and data availability status would establish whether the bottleneck is tradition-neutral or tradition-biased. The paper implies tradition-bias ("traditions with zero benchmarks are disproportionately those whose knowledge systems were developed through oral, communal, and practice-based transmission") but provides no statistical test of this association.

Third, the composite score range (50.8 to 34.4) is described as "compressed," but no benchmark for what "compressed" means is provided. Compressed relative to what? The normative ethics sister survey's range? A theoretical maximum range? The expected range under a null model of uniformly distributed features? Without a reference distribution, "compressed" is a subjective judgment, not a finding.

Fourth, the Top 15 rankings have no uncertainty quantification. The sensitivity analysis script computes Kendall's tau correlations across weight perturbations, which would establish ranking robustness, but these results are not reported. If Kendall's tau is high (> 0.8) across the weight sweep, the rankings are robust; if low (< 0.6), they are fragile. This information is essential for interpreting the rankings.

Fifth, the correlation between tradition family and benchmark availability is stated as a finding but not tested. A logistic regression predicting gate-passing status from tradition family (with controls for year and data availability) would establish whether tradition family independently predicts benchmark viability. The paper's argument about structural epistemic injustice would be substantially strengthened by formal statistical evidence rather than pattern description.

Sixth, the temporal claim that "73% of candidates date from 2024--2026" could be tested against a null model of uniform temporal distribution using a chi-squared goodness-of-fit test. This would establish whether the temporal concentration is statistically surprising or consistent with the overall growth rate of NLP publications.

**Recommendations:**
1. CRITICAL: Add inferential statistical tests for the three main claims. At minimum: chi-squared test for Islam's gate-passing rate, test of independence between tradition family and data availability, and confidence intervals on composite scores.
2. IMPORTANT: Report the Kendall's tau results from the sensitivity analysis weight sweep. If rankings are fragile, present rank-bands rather than point ranks.
3. IMPORTANT: Provide a reference distribution for the "compressed" score range claim. Compare to the normative ethics sister survey's range or to a simulated null distribution.
4. DESIRABLE: Run a logistic regression predicting gate-passing status from tradition family, year, and data availability to establish the independent predictive power of each factor.
5. DESIRABLE: Test the temporal concentration claim against a null model of uniform distribution.

---

### 7. Dr. Rivera --- AI Evaluation

The paper presents 15 benchmarks as the field's best instruments for religious values evaluation. But an implementation reality check reveals that many of these are not benchmarks in the operational sense---instruments that can be run against models to produce evaluation scores---but rather datasets, databases, or theoretical proposals that would require substantial engineering to convert into runnable evaluations.

GurbaniDB (Rank 14) is a database of Sikh scripture in Gurmukhi script, not a benchmark. It has no evaluation task, no scoring rubric, no gold-standard answers, and no evaluation harness. Including it in a ranked list of "benchmarks" stretches the term beyond its conventional meaning. The paper acknowledges this in Section 4.3 ("functions as a data resource rather than an evaluation instrument") but then includes it in the Top 15 anyway, which sends a contradictory signal: if the paper's own analysis concludes GurbaniDB is not an evaluation instrument, why does it pass the hard gates?

The Confucian Analects benchmark (Rank 15) is described as "theoretical" with the lowest composite score (34.4). The paper does not clarify whether this benchmark has been implemented---whether any model has ever been evaluated against it, whether evaluation items exist, or whether it is a proposal for a benchmark that has not yet been built. If it is a proposal, it should be listed separately from implemented instruments.

The trial findings expose a deeper implementation problem. Only 3 of the Top 15 have been trialed (T2 Islamic Inheritance, T3 BuddhismEval, T4 Break the Checkbox), and the trial results reveal serious problems. T2 revealed a 12x item count discrepancy (12,450 vs. the reported 1,000). T3 revealed that BuddhismEval's HuggingFace dataset returns a 401 (authentication required) error, meaning it is effectively inaccessible despite being listed as "available." T4 revealed that Break the Checkbox is not actually a religious values benchmark---it contains Pew survey items evaluated through Hofstede's secular cultural dimensions with zero questions about religion or theology, and the "Islam/Christianity" classification was an artifact of country-level demographics. If 1 of 3 trialed benchmarks is not actually a religious benchmark, what confidence should we have in the remaining 12 untrialed entries?

BuddhismEval's AUTH_REQUIRED status is particularly concerning. The hard gate requires "publicly available evaluation data," yet BuddhismEval was ranked in the Top 15 (Rank 13) despite its data being inaccessible. The data availability verification (`20260404-data-availability-verification.json`) confirms 43 of 47 URLs are accessible, but BuddhismEval is the exception. A benchmark that cannot be accessed should not be ranked as "available."

**Recommendations:**
1. CRITICAL: Remove or flag BuddhismEval (Rank 13) given that its data is inaccessible (AUTH_REQUIRED). A benchmark that cannot be accessed does not pass the public data gate.
2. CRITICAL: Remove or reclassify Break the Checkbox (Rank 5) if trial T4 confirms it is not actually a religious values benchmark. A secular cultural alignment instrument with no religious content should not be in a ranked list of religious values benchmarks.
3. CRITICAL: Distinguish between implemented benchmarks (models have been evaluated), available datasets (data exists but no evaluation has been run), and theoretical proposals (the benchmark is described but not built). The current Top 15 conflates all three.
4. IMPORTANT: Flag GurbaniDB as a data resource rather than a benchmark. Either reclassify it or explain why a database with no evaluation task passes the hard gates.
5. IMPORTANT: Expand the trial protocol to cover all 15 entries before publication. A ranked list where 80% of entries have not been implementation-tested has limited practical value for researchers seeking to adopt these instruments.

---

### 8. Dr. Zahra --- Sociology

The 3-axis scoring framework (RD 40%, PE 35%, CI 25%) embeds structural biases that reproduce the WEIRD (Western, Educated, Industrialized, Rich, Democratic) sampling problem the paper claims to diagnose. This is not a criticism of the paper's intentions---which are explicitly decolonial---but of the framework's operationalization, which inadvertently privileges Western-indexed metrics.

**Citation Impact axis (CI, 25% of composite).** CI scores are computed from citation counts, venue tier, and downstream adoption. All three sub-features reward participation in the Western academic publishing system. Citations are indexed by Semantic Scholar, which disproportionately covers English-language venues. Venue tier is determined by Western conference rankings (NeurIPS, ACL, AAAI are Tier 1; regional venues are Tier 2 or 3). Downstream adoption tracks reuse in English-language papers. A benchmark published in a prestigious Arabic-language Islamic jurisprudence journal---say, the Journal of Islamic Jurisprudence from Al-Azhar University---would receive a low CI score despite being highly influential within its tradition's scholarly community, because that influence is invisible to English-language citation databases. The CI axis thus systematically disadvantages benchmarks from non-Western scholarly ecosystems, which is precisely the pattern the paper's epistemic injustice argument diagnoses.

**Practical Ease axis (PE, 35% of composite).** PE scores reward GitHub/HuggingFace availability, English-language documentation, and compatibility with Western evaluation harnesses (lm-eval, HELM, Inspect). These are operationally useful criteria for English-speaking ML researchers, but they privilege the infrastructure of Western ML labs over alternative dissemination channels. A benchmark distributed through a tradition-specific digital library (e.g., Sefaria for Judaism, the Ganjoor digital library for Persian Islamic poetry, the CBETA corpus for Chinese Buddhism) would score lower on P3 (data availability) than one hosted on GitHub, even if the tradition-specific library provides better metadata, richer annotation, and more appropriate data governance.

**Practical Ease sub-feature P10 (language coverage).** The sensitivity analysis reveals that the P10 normalization function awards 70 points for English, 50 for Arabic, and 40 for all other languages. This weighting directly rewards English-language benchmarks and penalizes benchmarks in the languages in which religious traditions actually operate. A Quran benchmark in Arabic receives 20 fewer language points than the same benchmark in English---despite Arabic being the liturgical language of Islam. This is not merely a technical convenience; it is a value judgment embedded in the scoring formula that contradicts the paper's stated commitment to evaluating traditions on their own terms.

The composite formula's weight structure (RD 40%, PE 35%, CI 25%) means that 60% of the composite score comes from axes (PE + CI) that systematically advantage benchmarks created within Western academic and ML infrastructure. The paper justifies this by arguing that PE is essential for reproducibility and CI captures scholarly influence. Both justifications are valid within the Western academic framework, but they mean that the scoring framework itself cannot produce a Top 15 that reflects genuine tradition diversity---it can only reflect which traditions have been most successfully integrated into the Western ML evaluation pipeline.

**Recommendations:**
1. CRITICAL: Revise the P10 (language) normalization so that the liturgical/primary language of each tradition receives the same score as English. Arabic for Islam, Hebrew for Judaism, Sanskrit/Pali for Dharmic traditions, and Classical Chinese for Confucianism should all score equivalently.
2. IMPORTANT: Acknowledge explicitly that the CI axis privileges Western citation databases and that CI scores for non-Western benchmarks are systematically deflated. Consider either reducing CI's weight or adding a correction factor for non-English-indexed venues.
3. IMPORTANT: Expand P3 (data availability) to recognize tradition-specific digital libraries (Sefaria, CBETA, Ganjoor) as equivalent to GitHub/HuggingFace, not as lower-tier alternatives.
4. DESIRABLE: Compute and report what the Top 15 would look like under an alternative weighting that neutralizes the WEIRD bias (e.g., RD 60%, PE 25%, CI 15%, with language-neutral P10).
5. DESIRABLE: Add a "Scholarly Influence Within Tradition" sub-feature to CI that captures influence in tradition-specific scholarly communities, not just in English-language NLP venues.

---

### 9. Dr. Tanaka --- East Asian Philosophy

The paper's coverage of East Asian traditions is critically insufficient, and the coverage gap may be partly an artifact of the search strategy's English-language bias rather than a genuine absence of evaluation resources.

**CValues (Tao et al., 2024).** The Related Work section (2.2) cites CValues as a Chinese cultural alignment benchmark, but neither the feature matrix nor the tradition coverage analysis appears to evaluate it as a Confucian values benchmark. CValues includes items derived from Chinese social values that have deep Confucian roots---filial piety (xiao), harmony (he), propriety (li), and benevolence (ren) are operationalized in CValues through culturally grounded scenarios. If the paper evaluates CValues only as a "cultural" benchmark and not as a potential Confucian values benchmark, it may be undercounting Confucian representation. The classification decision (cultural vs. religious/values) should be made explicit and justified.

**JETHICS.** The Japanese Ethics (JETHICS) benchmark, if it exists as a public evaluation instrument, would be directly relevant to both Confucian and Shinto traditions. Japanese ethical reasoning blends Confucian, Buddhist, and Shinto elements in ways that may not map cleanly onto the paper's 14-tradition taxonomy. The paper should report whether JETHICS was considered and, if so, whether it was excluded and why.

**Chinese-language Islamic AI ethics literature.** China's Hui Muslim community has produced computational engagement with Islamic ethics in Chinese-language publications. The Xinjiang Uighur and Ningxia Hui NLP communities are active but publish primarily in Chinese. These resources are invisible to English-language searches.

The Confucianism section (Section 4.3) reports 14 candidates and 1 gate-passer (the Confucian Analects benchmark at Rank 15 with composite 34.4). The single Confucian entry enters at the lowest score, and the paper characterizes it as having "shallow engagement with the Confucian ethical system." But Confucian ethics is not a marginal philosophical tradition---it is the foundational moral framework for approximately 1.5 billion people in China, Japan, Korea, Vietnam, and diaspora communities. That the paper's Top 15 includes only one Confucian entry, and that entry has the lowest score, should prompt a more vigorous investigation of whether Confucian resources exist outside the English-language search space.

Taoism (2 candidates, 0 gate-passers) and Shinto (2 candidates, 0 gate-passers) receive minimal discussion. The concepts of wu wei (non-action), ziran (naturalness), and the Daoist critique of excessive governance have direct relevance to AI alignment---particularly to debates about the appropriate scope of model intervention. Shinto's concepts of wa (harmony), makoto (sincerity), and musubi (creative interconnection) provide a distinct ethical vocabulary for human-AI interaction. That neither tradition has any representation in the benchmark ecosystem should be flagged as a critical finding with specific implications for the East Asian AI ethics community, not subsumed under the general "8-tradition void" discussion.

**Recommendations:**
1. CRITICAL: Evaluate CValues explicitly as a potential Confucian values benchmark and justify the classification decision. If it is excluded, explain why; if it qualifies, include it in the feature matrix.
2. CRITICAL: Report whether JETHICS was considered and whether Chinese-language Confucian AI ethics resources were searched. If not, acknowledge this as a search limitation specific to East Asian traditions.
3. IMPORTANT: Provide separate treatment of Taoism and Shinto gaps rather than subsuming them under the generic "8-tradition void." Each tradition has distinct reasons for its absence and distinct resources that could be leveraged.
4. IMPORTANT: Conduct at least a targeted Chinese-language search for Confucian AI ethics evaluation resources, using Baidu Scholar or CNKI as search platforms.
5. DESIRABLE: Consult with East Asian AI ethics researchers (e.g., at Tsinghua, Keio, KAIST) about existing resources that may not appear in English-language databases.

---

### 10. Dr. Volkov --- Data Discovery

The data verification audit (`20260404-data-availability-verification.json`) reports 43 of 47 URLs verified accessible, which is a commendable reproducibility exercise. However, several issues require attention.

**BuddhismEval (AUTH_REQUIRED).** The verification confirms that BuddhismEval's HuggingFace dataset returns a 401 error (authentication required). This means the dataset is not publicly accessible in the sense required by the hard gate. Yet BuddhismEval is ranked at position 13 in the Top 15. Either the hard gate was not consistently applied, or "publicly available" is being defined loosely enough to include gated datasets that require authentication. The paper must clarify what "publicly available" means: does it include HuggingFace datasets that require a free account login? If so, this should be stated. If not, BuddhismEval fails the gate and should be removed from the Top 15.

**Three NOT_FOUND URLs.** The verification reports 3 URLs returning NOT_FOUND (404) status. The paper should identify which 3 benchmarks are affected and whether they are in the Top 15. A benchmark whose data URL has gone dead since the feature matrix was constructed may need to be downgraded or flagged.

**Snapshot reproducibility.** The verification tests URL accessibility at a single point in time (2026-04-04). URLs can become inaccessible---GitHub repos can be deleted, HuggingFace datasets can be made private, institutional servers can be decommissioned. The paper should recommend archival snapshots (e.g., Zenodo, Internet Archive) for all Top 15 data URLs to ensure long-term reproducibility. Currently, the paper's reproducibility depends on the continued availability of 15 external URLs, any of which could disappear.

**Verification depth.** The audit checks HTTP status codes but does not verify data content. A GitHub repo that returns 200 may contain only a README with no evaluation data. A HuggingFace dataset that returns 200 may contain a placeholder or incomplete data. Content-level verification---confirming that the URL actually contains usable evaluation data, not just a live web page---would strengthen the reproducibility claim.

**Recommendations:**
1. CRITICAL: Resolve BuddhismEval's status. Either remove it from the Top 15 (if AUTH_REQUIRED violates the public data gate) or explicitly define the gate to include gated datasets and justify this decision.
2. IMPORTANT: Identify the 3 NOT_FOUND URLs and assess their impact on rankings.
3. IMPORTANT: Create archival snapshots (Zenodo or Internet Archive) of all Top 15 data URLs and provide permanent identifiers.
4. DESIRABLE: Conduct content-level verification for all Top 15 data URLs, confirming that usable evaluation data (not just a live page) is present.
5. DESIRABLE: Report the date of the verification audit in the paper and recommend periodic re-verification.

---

### 11. Dr. Okafor --- Statistics

The composite score spread across the Top 15 is 16.4 points (50.8 to 34.4), yielding an average inter-rank gap of 1.17 points. This compression has three consequences that the paper does not address.

**Rank instability.** With an average gap of 1.17 points, a change of 2 points in any single axis score could shift a benchmark by 1--2 ranks. The sensitivity analysis script computes weight-sweep Kendall's tau and bootstrap CIs, but these results are not reported in the paper. Without reporting them, the paper implicitly claims that the ordinal ranking is meaningful---that Rank 1 is meaningfully better than Rank 2, that Rank 8 is meaningfully better than Rank 9. Given the compressed range, this is almost certainly false for most adjacent pairs. The paper should present rank-bands (e.g., "Tier A: Ranks 1--3, Tier B: Ranks 4--8, Tier C: Ranks 9--15") based on bootstrap CI overlap rather than point ranks.

**Weight sensitivity.** The baseline weights (RD 40%, PE 35%, CI 25%) are justified qualitatively in Section 3.3 but not tested for robustness. If shifting the weights by +/- 5% (e.g., RD 45%, PE 30%, CI 25%) produces a different Top 5, then the qualitative justification is insufficient. The sensitivity analysis script sweeps all weight combinations summing to 100% in increments of 5%, which is the correct approach. But the paper must report: (a) the range of Kendall's tau values across the sweep; (b) which benchmarks change rank by more than 3 positions; and (c) whether the top-ranked benchmark is stable across all weight combinations or only under the baseline weights.

**Bootstrap CI overlap.** The sensitivity analysis script implements Dirichlet-weighted bootstrap with 10,000 iterations, which is a sound methodology. But the key question---how many adjacent pairs have overlapping 95% CIs---is not reported. If the answer is "most of them," then the ranking is not statistically meaningful and should be presented as a partial ordering rather than a total ordering.

**Axis score distribution.** The paper reports that "no benchmark achieves a composite above 51." This ceiling suggests that the scoring formula may have a structural maximum well below 100, which would mean the 0--100 normalization is misleading. What is the theoretical maximum composite score under the current formula? If it is, say, 75 (because achieving simultaneously high RD, PE, and CI is structurally unlikely), then presenting scores on a 0--100 scale inflates the apparent gap between observed and ideal performance. The paper should report the theoretical maximum and the practical maximum (the score that a hypothetical "ideal" benchmark would achieve).

**Recommendations:**
1. CRITICAL: Report bootstrap CIs on all Top 15 composite scores and identify which adjacent pairs overlap. Present rank-bands based on CI non-overlap rather than point ranks.
2. CRITICAL: Report the Kendall's tau range from the weight sensitivity sweep and identify benchmarks with rank shifts > 3 positions.
3. IMPORTANT: Compute and report the theoretical maximum composite score to contextualize the observed ceiling of 50.8.
4. IMPORTANT: Present the Top 15 as a partial ordering (rank-bands) rather than a total ordering (point ranks) if bootstrap CIs show widespread overlap.
5. DESIRABLE: Report feature leave-one-out results: which single feature, if removed, causes the largest rank displacement? This identifies the most influential features and potential single points of failure.

---

### 12. Dr. Santos --- Methodology

The paper's seven claims are:

1. Tradition asymmetry: 8 of 14 traditions have zero viable benchmarks.
2. Islam dominance: 28 of 46 gate-passers, 7 of Top 15.
3. Knowledge-reasoning conflation: only 5 of 15 test genuine theological reasoning.
4. Structural epistemic injustice: the void correlates with Western academic infrastructure.
5. Data availability bottleneck: 77% eliminated by the data gate.
6. Score compression: 16.4-point range across Top 15.
7. Bias-values conflation: most benchmarks test bias detection, not values alignment.

Of these, Claims 1, 2, and 5 are supported by the data. Claims 3, 4, 6, and 7 exceed the evidence presented.

**Claim 3** rests on the expert council's assessment that "only 5 of 15 benchmarks demonstrate genuine theological depth." But the council is an internal assessment, not an independent validation. The paper does not report the criteria, scale, or inter-rater process by which the 7-member council made this determination. Was it a vote? A consensus process? Did all 7 members assess all 15 benchmarks, or did each member assess a subset? Without methodological detail, Claim 3 is an appeal to authority---the authority of an unspecified assessment process.

**Claim 4** asserts that the 8-tradition void "correlates with proximity to Western academic publishing infrastructure." This is a pattern observation, not a tested correlation. No measure of "proximity to Western academic publishing infrastructure" is defined, operationalized, or regressed against gate-passing status. The claim is plausible and likely correct, but it is presented as a finding when it is actually a hypothesis.

**Claim 6** uses "compressed" without a reference distribution. Compressed relative to what? The normative ethics sister survey is mentioned (score of 77.2 for the leading benchmark), but that comparison is between a single benchmark and the Top 15 range, which is not a valid comparison.

**Claim 7** is supported by the council's observation about bias-values conflation but is not quantified. How many of the 401 candidates test bias detection versus values alignment? The paper provides this classification for the Top 15 but not for the full corpus.

**PRISMA.** The paper describes a systematic search and screening process (401 candidates, two-stage assembly, hard gates, diversity constraints) but does not follow PRISMA reporting guidelines. A PRISMA flow diagram showing the number of records identified, screened, assessed for eligibility, and included would substantially improve methodological transparency. The current description is clear but informal.

**Methods-code discrepancy.** Beyond the PE weight discrepancy identified by Dr. Chen, there is a broader question of whether the methods section accurately describes the implementation. The paper reports 46 gate-passers; the feature matrix v2 reports 47. The paper reports PE weights P3=20, P4=15; the code implements P3=25, P4=10. These discrepancies suggest that the paper was written from one version of the code and the final results were generated from another. A methods-code audit comparing every formula in Section 3 against the actual implementation would identify any remaining discrepancies.

**Recommendations:**
1. CRITICAL: Add a PRISMA flow diagram showing the screening and inclusion process.
2. CRITICAL: Conduct a methods-code audit to reconcile all formulas in Section 3 with the actual implementation. Report and resolve all discrepancies.
3. CRITICAL: Provide methodological detail for the expert council's assessment process in Section 4.4. Specify: how many members assessed each benchmark, what scale they used, whether consensus was required, and what the inter-rater agreement was.
4. IMPORTANT: Downgrade Claim 4 from "finding" to "hypothesis" unless a formal correlation or regression test is conducted.
5. IMPORTANT: Quantify Claim 7 across the full corpus, not just the Top 15. Report how many of the 401 candidates test bias detection versus values alignment.
6. DESIRABLE: Reconcile the 46 vs. 47 gate-passer discrepancy between the paper and the feature matrix.

---

## Cross-Cutting Themes

Five themes emerge from the 12 individual assessments:

### Theme 1: The Framework Tests What Is Easy to Measure, Not What Matters

Multiple experts (al-Rashidi, Diallo, Zahra, Rivera) converge on the observation that the scoring framework rewards benchmarks that are easy to run (high PE), well-cited in English (high CI), and use religious text as data (surface-level RD)---rather than benchmarks that test genuine religious values reasoning. The composite formula allocates 60% of the score to PE and CI, which are measures of Western ML infrastructure integration, not of theological substance. The paper diagnoses this pattern in the field but does not recognize that its own scoring framework reproduces it.

### Theme 2: Claims Exceed Evidence

Santos, Mehta, and Chen identify that the paper's seven claims are supported primarily by descriptive statistics without inferential tests, confidence intervals, or formal hypothesis testing. The most consequential claims---structural epistemic injustice (Claim 4) and knowledge-reasoning conflation (Claim 3)---rest on pattern observations and internal council assessments rather than on tested correlations or validated measurement instruments.

### Theme 3: The Search May Undercount Non-English Resources

Goldberg, Tanaka, and Zahra each identify that the English-language bias of the search strategy may produce artificial tradition gaps. Judaism, Confucianism, and potentially other traditions have computational resources in Hebrew, Chinese, and other languages that English-language searches would miss. The paper acknowledges this in Limitations but does not quantify the potential undercount or conduct targeted non-English searches.

### Theme 4: Psychometric Foundations Are Missing

Chen, Okafor, and Mehta converge on the absence of standard psychometric and statistical practices: no inter-rater reliability, no IRT analysis, no confidence intervals on rankings, no inferential tests for claims, no DIF analysis across traditions. The sensitivity analysis script implements some of these analyses but the results are not reported in the paper.

### Theme 5: The "Benchmark" Category Is Too Broad

Rivera, al-Rashidi, and Raghavan note that the Top 15 conflates implemented benchmarks, available datasets, data resources, and theoretical proposals. GurbaniDB is a database, the Confucian Analects entry may be a proposal, Break the Checkbox may not be a religious benchmark at all, and BuddhismEval is inaccessible. A more rigorous typology would distinguish these categories and rank only implemented, accessible instruments.

---

## Priority-Ranked Recommendations

### CRITICAL (Must address before submission)

| # | Issue | Source | Action |
|---|-------|--------|--------|
| C1 | PE weight discrepancy between paper and code | Chen | Audit all formulas; report which was used; recompute if needed |
| C2 | No confidence intervals on rankings | Chen, Okafor | Report bootstrap CIs; present rank-bands if overlap is widespread |
| C3 | R2 floor effect (85% at minimum) | Chen | Demonstrate R2 contributes discrimination above the gate, or rescale |
| C4 | No inferential statistical tests for 7 claims | Mehta | Add chi-squared, Fisher's exact, or logistic regression tests |
| C5 | BuddhismEval inaccessible (AUTH_REQUIRED) in Top 15 | Rivera, Volkov | Remove from Top 15 or clarify public-data gate definition |
| C6 | Break the Checkbox may not be religious (trial T4) | Rivera | Remove or reclassify based on trial evidence |
| C7 | Islamic Inheritance item count error (1,000 vs. 12,450) | al-Rashidi | Correct the factual error |
| C8 | No PRISMA flow diagram | Santos | Add PRISMA diagram for the systematic search process |
| C9 | Methods-code audit needed | Santos | Reconcile all Section 3 formulas with actual implementation |
| C10 | Reframe 8-tradition void as paradigm scope limitation | Diallo | Develop the conceptual argument beyond "future work" |
| C11 | Report search queries per tradition | Goldberg | Provide query templates to distinguish search artifacts from genuine gaps |
| C12 | Evaluate CValues as potential Confucian benchmark | Tanaka | Justify classification decision |

### IMPORTANT (Should address; weakens paper if omitted)

| # | Issue | Source | Action |
|---|-------|--------|--------|
| I1 | Qualify "formalizability" of Islamic jurisprudence | al-Rashidi | Specify subdomains; avoid essentializing fiqh as algorithmic |
| I2 | Inter-rater reliability for R2, R3, R4, R5, R6 | Chen | Double-code 20--30 entries with a second rater |
| I3 | Add source-language modifier to R3 scoring | Raghavan | Sanskrit/Arabic original should score higher than English translations |
| I4 | Revise P10 language normalization (WEIRD bias) | Zahra | Liturgical languages should score equivalently to English |
| I5 | Report Kendall's tau from weight sensitivity sweep | Okafor | Establish ranking robustness across weight perturbations |
| I6 | Distinguish database/dataset/benchmark/proposal | Rivera | Create typology; rank only implemented, accessible instruments |
| I7 | Verify Bhagavad Gita benchmark source language | Raghavan | Confirm whether it processes Sanskrit or English translations |
| I8 | Quantify English-language search bias | Goldberg, Tanaka | Report language coverage of 72 search queries |
| I9 | Expert council methodology detail | Santos | Specify assessment process, scale, inter-rater agreement |
| I10 | Acknowledge CI axis privileges Western citation databases | Zahra | Consider weight reduction or correction factor |
| I11 | Compute theoretical maximum composite score | Okafor | Contextualize the observed ceiling of 50.8 |
| I12 | Strengthen CARE Principles engagement | Diallo | From constraint mention to substantive methodological engagement |

### DESIRABLE (Would improve paper; not essential for submission)

| # | Issue | Source | Action |
|---|-------|--------|--------|
| D1 | Add 13th format code for dialectical reasoning (DIA) | Goldberg | Accommodate Talmudic, Buddhist debate, Islamic ijma formats |
| D2 | Separate treatment of Taoism and Shinto gaps | Tanaka | Distinct reasons and distinct available resources |
| D3 | Gulf state funding acknowledgment | al-Rashidi | Material factor in Islam's infrastructure |
| D4 | DIF analysis across tradition families | Chen | Test whether features function equivalently |
| D5 | Archival snapshots for Top 15 data URLs | Volkov | Zenodo or Internet Archive for long-term reproducibility |
| D6 | Content-level verification of data URLs | Volkov | Confirm usable data, not just live pages |
| D7 | Alternative weighting scenario (WEIRD-neutral) | Zahra | Report Top 15 under RD 60%, PE 25%, CI 15% |
| D8 | Feature leave-one-out results | Okafor | Identify most influential features |
| D9 | Logistic regression for gate-passing prediction | Mehta | Formal test of tradition family as independent predictor |
| D10 | Jainism false positive mechanism analysis | Raghavan | Distinguish ahimsa-as-Jain from ahimsa-as-general |
| D11 | Consider moratorium recommendation for oral traditions | Diallo | Until community-governed frameworks exist |

---

## Consensus Statement

The 12-member council reaches consensus on the following assessment:

The paper identifies a genuine and important problem: the religious values benchmarking ecosystem is profoundly imbalanced, with 8 of 14 traditions entirely unrepresented and the remaining 6 dominated by Islamic textual evaluation. The three-problem framing (tradition asymmetry, knowledge-reasoning conflation, structural epistemic injustice) is the right analytical architecture for this finding. The paper's contribution to the field---the first systematic meta-evaluation of religious values benchmarks---is valuable and needed.

However, the implementation of the scoring framework and the evidential support for the paper's claims fall below the standard required for a rigorous methodological contribution. Specifically:

1. **The scoring framework has unresolved bugs** (PE weight discrepancy, R2 floor effect) that undermine confidence in the rankings.
2. **The claims exceed the evidence.** Seven claims are supported by descriptive statistics alone; no inferential tests, confidence intervals, or formal hypothesis tests are reported. The sensitivity analysis was computed but its results were not incorporated into the paper.
3. **The Top 15 conflates categories.** Databases, inaccessible datasets, secular cultural instruments, and theoretical proposals are ranked alongside implemented religious values benchmarks. Trial evidence (T3 BuddhismEval inaccessible, T4 Break the Checkbox not religious) has already invalidated 2 of the 3 trialed entries.
4. **The framework reproduces the WEIRD bias it diagnoses.** 60% of the composite score derives from PE and CI axes that reward Western ML infrastructure integration. The P10 language normalization penalizes non-English benchmarks. The CI axis privileges English-indexed citation databases.
5. **The epistemic injustice argument is underdeveloped.** The paper names the 8-tradition void as structural epistemic injustice but treats it as a gap to be filled rather than as evidence of a paradigm scope limitation. The conceptual architecture for "fundamentally different evaluation paradigms" is gestured at but not developed.

The council recommends that the 12 CRITICAL issues be resolved before submission and that the paper undergo a second council review (D-02) after revisions are implemented. The council affirms that the revised paper has the potential to be a significant contribution to the field of AI evaluation, provided that the scoring framework's technical foundations are strengthened and the claims are brought into alignment with the available evidence.

**Signed by all 12 members:**
Dr. al-Rashidi, Dr. Goldberg, Dr. Raghavan, Dr. Diallo, Dr. Chen, Dr. Mehta, Dr. Rivera, Dr. Zahra, Dr. Tanaka, Dr. Volkov, Dr. Okafor, Dr. Santos
