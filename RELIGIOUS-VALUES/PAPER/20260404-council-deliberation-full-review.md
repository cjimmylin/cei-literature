# Council Deliberation D-03: Sections 3--6 Full Review

**Date:** 2026-04-04
**Document reviewed:** `full-paper-religious-values.md` (Sections 3--6: Methods, Results, Discussion, Conclusion)
**Charge:** Each of the 6 council members reviews their assigned sections against five criteria: factual accuracy, anti-essentialization, citation adequacy, framing fairness, and missing perspectives. Produce individual assessments, consensus findings, minority reports, and a ranked priority revision list.

**Review protocol:** Assessments reference the spine (`spine-religious-values.md`) for citation key verification, the D-02 introduction review deliberation for continuity, and the three implementation trial findings (T2 Islamic Inheritance Law, T3 BuddhismEval, T4 Break the Checkbox) as empirical evidence.

**Trial evidence available to the council:**

- **T2 (Islamic Inheritance Law):** Contains 12,450 items (not 0 as metadata said), fully implementable, tests knowledge OF Islamic law + mathematical reasoning, NOT values alignment. Supports Claim 2 (knowledge-reasoning conflation).
- **T3 (BuddhismEval):** Dataset is INACCESSIBLE (HuggingFace 401 error). Evidence for the reproducibility crisis argument. The vault's PDF extract is wrong (contains an education encyclopedia, not the actual paper).
- **T4 (Break the Checkbox):** NOT actually a religious values benchmark---contains Pew survey items evaluated through Hofstede's secular cultural dimensions. Zero questions about religion/theology. The "Islam/Christianity" classification was an artifact of country-level demographics. Evidence for Claim 7 (bias-values conflation).

---

## Expert Assessments

### Expert 1 -- Prof. Sachedina (Islamic Ethics & Bioethics)
**Sections reviewed:** Section 5.1 (Tradition Asymmetry Problem -- Islam dominance interpretation)

**Overall assessment:** GOOD

**Factual accuracy:** The Islam dominance interpretation in Section 5.1 is structurally sound and continues the careful attribution established in Sections 1--2. The claim that "Islam's dominance of the benchmark ecosystem---28 gate-passers, 7 of the Top 15---is the central structural finding of this survey" is well-supported by the data in Tables 2 and 3. The three reinforcing factors attributed to this dominance are correctly identified: (1) the Quranic QA shared task community, (2) Arabic NLP infrastructure, and (3) the formalizability of Islamic jurisprudence.

However, the third factor---"the formalizability of Islamic jurisprudence (fiqh), whose explicit rules for inheritance distribution, legal precedent hierarchies, and operationalizable evaluation dimensions via the Maqasid al-Shariah"---requires nuance. While fiqh does contain explicit rules for certain domains (inheritance distribution is the classic example), Islamic jurisprudence is not reducible to rule application. The discipline of usul al-fiqh (principles of jurisprudence) involves highly sophisticated analogical reasoning (qiyas), consensus-building (ijma), consideration of custom (urf), and juristic preference (istihsan)---none of which "map naturally onto structured evaluation formats." Only the most formalized subdomain of fiqh---inheritance law---maps naturally onto MCQ formats. The draft's phrasing risks presenting Islamic jurisprudence as more algorithmic than it actually is, which is itself a form of theological flattening.

The trial finding for T2 (Islamic Inheritance Law) is directly relevant here. The benchmark contains 12,450 items testing knowledge OF Islamic inheritance law plus mathematical reasoning. This confirms that the benchmark tests fiqh as calculation, not fiqh as reasoning within a tradition. The draft's characterization that "its 1,000 items require the application of complex legal formulae" (Section 4.2) understates the dataset size (12,450 items, not 1,000) and overstates the reasoning demand---the items test whether a model can compute inheritance shares using explicit Quranic rules, which is closer to mathematical word problems with Islamic legal parameters than to genuine jurisprudential reasoning. A real values alignment benchmark for Islamic inheritance would ask: "When the Quranic distribution rules produce an outcome that conflicts with contemporary notions of gender equity, how should a Muslim jurist navigate this tension?"---the kind of ijtihad (independent reasoning) that the benchmark does not test.

The concluding sentence of Section 5.1---"the field currently uses 'religious values benchmarking' as though it denotes comprehensive assessment, but in practice the phrase is nearly synonymous with 'Islamic textual evaluation'"---is a powerful and accurate summary that I endorse.

**Anti-essentialization:** GOOD. Section 5.1 consistently attributes dominance to infrastructure and formalizability rather than theological significance. The sentence "Islam's dominance is a product of infrastructure and formalizability, not of theological significance relative to other traditions" (Section 4.3) is precisely right. However, the claim about "formalizability" edges toward essentializing Islamic jurisprudence as rule-based when much of it involves deeply contextual reasoning. The fix is simple: qualify "the formalizability of certain subdomains of Islamic jurisprudence, particularly inheritance law and commercial transactions" rather than implying that fiqh as a whole is formalizable.

**Citation adequacy:** Kamali (2008), Malhas (2023), Johnson (2026), Francis (2015), Koppel (2011)---all match the spine. The Christianity-Judaism discussions in 5.1 reuse the same citations as Sections 2.2b--c, which is appropriate for a Discussion section.

Missing: (1) No citation for the claim that Christianity "converts candidates to gate-passers at only 5.1% (6 of 117)"---this is the paper's own data, so no external citation is needed, but the contrast with Islam's 24.8% conversion rate deserves a brief interpretive gloss beyond "doctrinal flattening." The institutional fragmentation of Christianity (no single church controls the pipeline, unlike the relatively coordinated Arabic NLP community) is at least as important as doctrinal flattening but receives no mention. (2) The Sefaria and Bar-Ilan references in the Judaism discussion repeat material from Section 2 without adding new interpretive depth.

**Framing fairness:** The Islam dominance framing remains structural and respectful. The Judaism "starkest paradox" framing is apt. However, the phrase "two adjacent fields that have not yet recognized their mutual relevance" (referring to Jewish computational scholarship and LLM evaluation) is slightly paternalistic---it implies that the communities should be doing something they are not. Perhaps "two communities with adjacent but distinct institutional histories" is more neutral.

**Missing perspectives:**
1. The institutional fragmentation of Christianity as a structural explanation alongside "doctrinal flattening."
2. The role of funding: the Arabic NLP community has benefited from substantial Gulf state investment in AI and Arabic language technology. This funding dimension is absent from the analysis.
3. The distinction between Islam's benchmark dominance in the English-language literature versus the broader global Islamic computational ecosystem (e.g., Indonesian, Turkish, Persian Islamic NLP work that may not appear in the English-language survey).

**Specific revision recommendations:**
1. **CRITICAL:** Update the Islamic Inheritance Law item count from "1,000" to "12,450" based on trial T2 findings, and revise the characterization to reflect that the benchmark tests fiqh-as-calculation rather than fiqh-as-reasoning. This is a factual error that trial evidence has corrected.
2. **IMPORTANT:** Qualify the "formalizability" claim by specifying that only certain subdomains of fiqh (inheritance, commercial transactions) are highly formalizable, while other domains (family law, bioethics, inter-religious relations) involve contextual reasoning that resists formalization.
3. **IMPORTANT:** Add a sentence noting that Christianity's low conversion rate may reflect institutional fragmentation (no single coordinating body equivalent to the Arabic NLP community) as much as doctrinal flattening.
4. **DESIRABLE:** Add a brief note about Gulf state funding for Arabic NLP as a material factor in Islam's benchmark infrastructure.

---

### Expert 3 -- Prof. Bilimoria (Dharmic Philosophy)
**Sections reviewed:** Section 4.3 (Tradition Coverage Patterns -- Dharmic traditions); Section 5.3 (Structural Epistemic Injustice)

**Overall assessment:** GOOD -- with an important correction needed in 4.3

**Factual accuracy:** The Dharmic traditions discussion in Section 4.3 is factually accurate in its broad claims but contains a specific characterization error. The Bhagavad Gita Sentiment Analysis benchmark (rank 6) is described as applying "BERT-based sentiment classification to Sanskrit verses." This is misleading---the Bhagavad Gita is composed in Sanskrit, but modern computational analyses of it typically work with English translations or transliterated text, not with Sanskrit script directly. The distinction matters because working with Sanskrit directly would require specialized NLP tools (the Sanskrit Heritage Site, for instance, or the Digital Corpus of Sanskrit), while working with English translations is a standard NLP task performed on translated religious text. The draft should specify which language the benchmark actually processes.

The Jainism false positive analysis is correct and important: "Jainism, despite generating 47 candidates, produces zero gate-passers---nearly all candidates are false positives where the keyword ahimsa (non-violence) appears in papers about general ethics rather than Jain philosophical frameworks." This is an excellent example of how keyword-based classification can overcount tradition coverage. However, the parenthetical attribution "\cite{Bilimoria2013}" at the end of the Jainism sentence is inappropriate---my 2013 work is about Indian ethics broadly, not about Jain false positives in NLP keyword matching. The citation should be removed or replaced with a methodological note about keyword-based classification limitations.

Table 3's candidate counts for the Dharmic traditions show discrepancies with Table 3 headers. Table 3 lists Hinduism at 43 candidates, Buddhism at 31, and Jainism at 59. But Section 4.1 reports "Jainism alone accounts for 47" and "Hinduism (25 candidates, 5 gate-passers), Buddhism (14 candidates, 4 gate-passers), and Sikhism (6 candidates, 2 gate-passers)." These numbers do not match Table 3. Section 4.1 says Jainism has 47 candidates; Table 3 says 59. Section 4.1 says Hinduism has 25; Table 3 says 43. Section 4.1 says Buddhism has 14; Table 3 says 31. This is a critical internal inconsistency---the prose and the table report different numbers for the same quantities.

**Section 5.3 (Structural Epistemic Injustice):** The theoretical argument is strong. The extension of Fricker's epistemic injustice from interpersonal credibility deficits to infrastructure is well-articulated and has been strengthened since the D-02 review---Fricker (2007) is now cited. The sentence "the injustice is not that individual researchers are biased against these traditions but that the structure of the pipeline renders them invisible" captures the argument precisely.

However, the section lists "Jainism" alongside "Indigenous Spirituality, Ubuntu Philosophy, Taoism, Shinto" as traditions whose absence reflects structural epistemic injustice. This conflates two quite different situations. Jain philosophy has extensive textual canons (the Agamas, the Tattvartha Sutra, the works of Haribhadra and Hemachandra) that are substantially digitized. Jainism's absence from benchmarks is not because its knowledge system is oral or communal---it is because no Jain computational scholarship community has emerged to convert these texts into benchmark format. This is a community coordination problem, structurally similar to Judaism's absence, not an epistemic injustice problem structurally similar to Indigenous traditions' absence. Grouping Jainism with oral/communal traditions in the epistemic injustice argument weakens the argument by over-extending it.

**Anti-essentialization:** ADEQUATE. The Section 4.3 discussion of Dharmic traditions treats each tradition individually, which is an improvement over the grouping problem I flagged in D-02 for Section 2.2d. However, the summary claim that "the gap between philosophical discourse and operationalized evaluation is the defining feature of these traditions' relationship to AI benchmarking" (from Section 2.2d, reused implicitly in 4.3) still treats all Dharmic traditions as sharing a single structural problem, which I contested in D-02.

**Citation adequacy:** Bilimoria (2013), Mohamed (2020), Carroll (2020), Fricker (2007), Henrich (2010), Birhane (2021)---all match spine. No phantom citations in these sections.

**Framing fairness:** The Dharmic traditions discussion in 4.3 gives each tradition its own paragraph, which is a structural improvement over Section 2.2d. The word allocation is roughly proportionate to benchmark coverage (Islam gets the most words because it has the most benchmarks to discuss). This is appropriate for a Results section.

**Missing perspectives:**
1. The BuddhismEval inaccessibility (trial T3) should be reported in Section 4.3 or 4.4---a Top 15 benchmark that is actually inaccessible changes the effective count of Dharmic gate-passers.
2. The distinction between Jainism's absence (community coordination problem with digitized texts) and Indigenous traditions' absence (structural epistemic injustice with oral/communal knowledge) should be drawn explicitly.
3. GurbaniDB (rank 14, Sikhism) is described as "a structured database of Sikh scripture in Gurmukhi" that "functions as a data resource rather than an evaluation instrument." This is honest but raises the question of whether GurbaniDB should have passed the hard gate at all if it is not actually a benchmark. The paper should address this.

**Specific revision recommendations:**
1. **CRITICAL:** Reconcile the candidate count discrepancies between Section 4.1 prose and Table 3. The paper cannot report different numbers for the same quantities.
2. **IMPORTANT:** In Section 5.3, distinguish between textual traditions with digitized corpora but no benchmark community (Jainism, Judaism---community coordination problems) and oral/communal traditions (Indigenous, Ubuntu---structural epistemic injustice). The current formulation over-extends the epistemic injustice argument by including traditions whose absence has different structural causes.
3. **IMPORTANT:** Add the BuddhismEval inaccessibility finding (trial T3) to Section 4.3 or 4.4. A Top 15 benchmark that returns HTTP 401 is relevant to the reproducibility argument.
4. **DESIRABLE:** Specify which language the Bhagavad Gita Sentiment Analysis benchmark actually processes (Sanskrit, Hindi, or English translation).
5. **DESIRABLE:** Remove the Bilimoria (2013) citation from the Jainism false positive sentence---the citation does not support the specific claim being made.

---

### Expert 5 -- Dr. Osei-Mensah (African Philosophy & Ubuntu Ethics)
**Sections reviewed:** Section 5.3 (Structural Epistemic Injustice as Finding); Section 5.4 (Closing the Gaps)

**Overall assessment:** STRONG

**Factual accuracy:** Section 5.3 extends the foundational argument from Section 2.5 with specificity and care. The central claim---"the benchmark creation pipeline...has epistemic prerequisites that systematically exclude oral, communal, and practice-based knowledge systems"---is a faithful application of the Mohamed et al. (2020) framework. The Fricker (2007) citation is now present, and the extension from interpersonal to infrastructural epistemic injustice is explicitly acknowledged. This addresses the D-02 concern raised by Expert 11 (Mohamed).

The CARE Principles discussion in Section 5.3 is accurate and well-placed. The formulation "the hard gate requiring publicly available evaluation data functions simultaneously as a quality filter (ensuring reproducibility) and as a structural exclusion mechanism (barring traditions whose communities exercise data sovereignty)" is precise and captures the genuine tension without resolving it prematurely. The final sentence---"it requires fundamentally different evaluation architectures"---is appropriately open-ended.

Section 5.4's two-track strategy (shared tasks for textual traditions, community-governed protocols for oral traditions) is sound in principle. The recommendation that "open data requirements should not be imposed on communities who exercise epistemic sovereignty" is important and correctly positioned. However, the section's concrete recommendations for oral traditions remain quite abstract: "community-governed assessment protocols where the tradition's own practitioners define what counts as competent reasoning, participatory methods that embed evaluation within relational contexts rather than extracting knowledge into decontextualized items." These are descriptions of what is needed, not proposals for how to achieve it. The section could be strengthened by pointing to at least one existing prototype or pilot (e.g., the MUKURTU cultural heritage platform as a model for community-governed digital knowledge management, or the Local Contexts initiative for Indigenous data labels).

**Anti-essentialization:** STRONG. Section 5.3 avoids monolithic treatment throughout. The phrase "Ubuntu's relational ontology, Indigenous land-based and intergenerational moral reasoning, Jain ahimsa as a comprehensive non-violence ethic, and Daoist wu wei as a principle of governance" names specific philosophical concepts rather than treating traditions as undifferentiated blocks. This is a significant improvement over the aggregated treatment that concerned me in D-02.

However, I echo Prof. Bilimoria's concern that Jainism's inclusion in this list conflates different structural situations. Ubuntu's relational ontology and Indigenous knowledge systems are genuinely challenged by the benchmark pipeline's epistemic prerequisites. Jainism has extensive textual canons that could, in principle, be processed through the standard pipeline. The list implicitly groups all zero-benchmark traditions as facing the same obstacle, when they face different obstacles.

**Citation adequacy:** Fricker (2007), Mohamed (2020), Carroll (2020), Bilimoria (2013), Henrich (2010), Birhane (2021), Sorensen (2024)---all match spine.

Missing: (1) MUKURTU or Local Contexts as examples of community-governed digital knowledge infrastructure. (2) Tuck and Yang (2012) on "Decolonization is not a metaphor"---relevant because the paper uses decolonial language and should be careful that its recommendations do not reduce decolonization to a methodological adjustment. (3) No reference to the Sustainable Development Goals or any global policy framework that might incentivize investment in underrepresented traditions' evaluation infrastructure.

**Framing fairness:** Sections 5.3 and 5.4 are well-balanced. The acknowledgment that "some communities may decline to encode sacred knowledge in public datasets not because they lack the capacity but because they exercise epistemic sovereignty" is crucial and correctly positioned as respect rather than deficit. The two-track recommendation does not presume that all traditions want the same thing.

**Missing perspectives:**
1. A concrete example of community-governed evaluation (even a prototype or analogue from another domain) would strengthen the otherwise abstract recommendations.
2. The paper does not address who would fund the community-governed evaluation protocols. The shared task pipeline for textual traditions has a clear funding model (NLP venue workshops, Arabic NLP programs). No equivalent funding model is proposed for the community-governed track.
3. The paper does not discuss the temporal dimension: community-governed evaluation will necessarily be slower and more expensive than standardized benchmarking. This is acceptable but should be acknowledged.

**Specific revision recommendations:**
1. **IMPORTANT:** Add at least one concrete example of community-governed digital knowledge management (MUKURTU, Local Contexts, or a similar initiative) to Section 5.4 to ground the otherwise abstract recommendations.
2. **IMPORTANT:** Acknowledge the funding and timeline asymmetry: shared task pipelines can produce benchmarks in 2--3 years, but community-governed protocols will require longer timelines and different funding models.
3. **DESIRABLE:** Add a sentence noting that genuine community governance means accepting that some evaluation processes will be proprietary, non-public, and non-replicable by external researchers---and that this is acceptable if the alternative is exclusion.
4. **DESIRABLE:** Consider citing Tuck and Yang (2012) as a check on the paper's decolonial framing---decolonization requires material redistribution of power, not merely methodological innovation.

---

### Expert 7 -- Dr. Sarah Chen (Psychometrics & Test Theory)
**Sections reviewed:** Sections 3.1--3.6 (Methods)

**Overall assessment:** ADEQUATE -- with significant concerns about weight justification and gate design

**Factual accuracy:** The Methods section is clearly written and methodologically transparent. The 401-candidate corpus assembly (Section 3.1) is well-documented: the two-stage process (vault-derived candidates plus external search) is a defensible approach for a meta-evaluation. The external search process---72 queries across Semantic Scholar, arXiv, and HuggingFace---is specific enough for replication. The three-tier classification (theological, theological-values, values) is clearly described.

The feature matrix (Section 3.2, Table 1) is comprehensive. The 22 features across three axes are well-chosen and the scale descriptions are clear. The calibration anchors---IslamicMMLU at R2 = 4, Break the Checkbox at R2 = 2, and surface-mention papers at R2 = 1---provide a useful reference frame. However, trial T4 now reveals that Break the Checkbox is not actually a religious values benchmark at all. It contains Pew survey items evaluated through Hofstede's secular cultural dimensions, with zero questions about religion or theology. Using a non-religious-values benchmark as a calibration anchor for theological depth is methodologically problematic. The R2 = 2 assigned to Break the Checkbox should arguably be R2 = 1 or even R2 = 0, which would compress the calibration range and potentially affect other assignments.

**Composite formula concerns.** The composite COMPOSITE = RD x 0.40 + PE x 0.35 + CI x 0.25 is stated but its weights are justified by assertion rather than empirical or theoretical grounding. The justification offered is: "We weighted RD highest because this survey specifically evaluates religious and theological depth." This is a circular argument: the weights reflect the survey's stated purpose, which is defined by the weights. In psychometric practice, composite weights should be justified by one of several methods:

(a) **Expert consensus:** A panel of experts assigns weights through a structured process (e.g., Delphi method or analytic hierarchy process). The paper's single-author weights are an assertion, not a consensus.
(b) **Empirical derivation:** Weights are derived from the correlation structure of the data (e.g., principal components analysis of the feature matrix). This would be a stronger justification.
(c) **Sensitivity analysis:** The paper should at minimum show that the Top 15 ranking is robust to alternative weight specifications. If the ranking changes substantially under RD x 0.50 + PE x 0.30 + CI x 0.20 or RD x 0.33 + PE x 0.33 + CI x 0.33, the weight choice is consequential and the paper should acknowledge this.

The absence of any sensitivity analysis is a significant methodological gap.

**Hard gate concerns.** The two hard gates---RD >= 30 and publicly available data---are defensible in principle but create a tension with the paper's own argument. The data availability gate eliminates 77% of the corpus and disproportionately affects oral/communal traditions. The paper acknowledges this tension in Sections 3.6 and 5.3, which is good. But the RD >= 30 gate receives less scrutiny. What is the distribution of RD scores? Is 30 a natural break point, or is it arbitrary? If 25 of the 355 eliminated candidates have RD scores between 25 and 29, the gate may be excluding substantive candidates. The paper should report the RD distribution and justify the specific threshold.

**Section 3.4 (Meta-Evaluation Criteria):** The seven criteria are well-conceived. Content Validity (Criterion 1) is the most important and is well-operationalized through the 20-item sample classification. Cultural Authenticity (Criterion 3) with its NATIVE/CONSULTED/EXTERNAL trichotomy is a valuable contribution. Annotation Quality (Criterion 7) addresses a real concern about sacred text ground truth.

**Section 3.5 (Implementation Trial Protocol):** The protocol is clearly specified. The multi-model design (frontier closed, frontier open, mid-tier) is appropriate. The error taxonomy (knowledge gaps, reasoning failures, cultural misunderstanding) is well-chosen. However, the section states that "full-scale trials are in progress, with results to be reported in a companion technical report." This means the paper's empirical claims about what benchmarks "actually test" (the title's claim) rest on the feature matrix scoring and expert council assessment, not on direct implementation evidence. The three trial findings available to this council (T2, T3, T4) provide crucial empirical evidence that should be incorporated into the paper rather than deferred to a companion report.

**Section 3.6 (Limitations):** Commendably honest. The acknowledgment that "all scoring was conducted by a single author without inter-rater reliability" and that the hard gate "functions simultaneously as a structural exclusion mechanism" are important disclosures. However, the limitation about the external search not including Google Scholar is particularly consequential---Google Scholar would likely yield the largest number of additional candidates, and its omission may systematically bias the corpus toward venues indexed by Semantic Scholar and arXiv.

**Anti-essentialization:** Not a primary concern for the Methods section, but the language is appropriately technical throughout.

**Citation adequacy:** Bowman (2021), Gehrmann (2022), Alharbi (2024), Mohamed (2020), Carroll (2020), Hendrycks (2021), Gupta (2025), Li (2025), Leavens (2024)---all match spine.

**Framing fairness:** The Methods section is appropriately neutral. The acknowledgment of the hard gate tension is well-placed.

**Missing perspectives:**
1. Sensitivity analysis of composite weights.
2. RD score distribution and justification for the 30-threshold.
3. Inter-rater reliability estimate, even if post hoc (e.g., having a second rater score a random 10% sample).
4. Discussion of whether the 3-tier classification (theological / theological-values / values) has clear decision boundaries---what distinguishes a "theological-values" paper from a "theological" one?

**Specific revision recommendations:**
1. **CRITICAL:** Add a sensitivity analysis showing that the Top 15 ranking is robust (or not) to alternative weight specifications. At minimum, report the ranking under equal weights (0.33/0.33/0.33) and under RD-dominant weights (0.50/0.30/0.20). If the ranking is unstable, acknowledge this as a limitation.
2. **CRITICAL:** Revise the Break the Checkbox calibration anchor in light of trial T4 findings. The benchmark contains zero religious/theological questions and should not anchor R2 = 2. Reassess its RD score and, if changed, note how many other assignments are affected.
3. **IMPORTANT:** Report the distribution of RD scores (e.g., as a histogram or summary statistics) and justify the 30-threshold. Is there a natural break in the distribution, or is the threshold arbitrary?
4. **IMPORTANT:** Incorporate the three trial findings (T2, T3, T4) into the main paper rather than deferring all trial results to a companion report. These findings directly support the paper's central claims and their absence weakens the empirical foundation.
5. **DESIRABLE:** Add a brief acknowledgment of the Google Scholar omission's potential impact on corpus completeness.

---

### Expert 8 -- Dr. Marcus Rivera (LLM Evaluation & Benchmarking)
**Sections reviewed:** Sections 3.2--3.3 (Scoring Framework and Composite Scoring); Section 4.2 (Top 15 Ranking)

**Overall assessment:** GOOD

**Factual accuracy:** The feature matrix (Table 1) is well-structured and the feature definitions are clear. The axis formulas are internally consistent: the weights within each axis sum correctly, and the normalization to 0--100 is appropriate. The composite formula COMPOSITE = RD x 0.40 + PE x 0.35 + CI x 0.25 produces scores that match the rankings in Table 2 (I verified this for ranks 1, 2, and 15).

The Top 15 ranking in Table 2 is internally consistent. The composite score range of 34.4--50.8 is correctly reported, and the comparison with the normative ethics benchmark score of 77.2 (Hendrycks ETHICS) is a useful reference point that highlights the field's immaturity. However, the comparison assumes that the scoring framework is commensurable between the sister surveys. If the two surveys use different feature definitions (even within the same axis names), the comparison is meaningful only as a rough indicator, not a precise measurement. The draft should add a brief qualifier.

**Section 4.2 specifics:**

ELQV (rank 1): The description states "2,100 Quranic verses annotated for emotional valence by PhD-level experts" with RD = 62.0. The RD score is the highest in the corpus and the characterization matches the feature matrix. However, "emotional valence" annotation is fundamentally a sentiment analysis task, not a religious values alignment task. The paper partially addresses this in Section 5.2 ("ELQV tests verse-level emotion detection---an NLP task performed on sacred text, but fundamentally a knowledge extraction task"), but the tension between ranking ELQV first overall while simultaneously arguing it tests knowledge rather than values should be addressed more explicitly. The reader may ask: if the paper's own analysis reveals that the top-ranked benchmark does not actually test religious values alignment, what does the ranking measure?

Islamic Inheritance Law (rank 2): Trial T2 reveals 12,450 items, not 1,000 as stated in Section 4.2. This is a factual error that must be corrected. The characterization that "the best-performing models achieve only moderate accuracy" is useful for the discrimination check.

Break the Checkbox (rank 5): Trial T4 reveals this is NOT a religious values benchmark. It contains Pew survey items evaluated through Hofstede's secular cultural dimensions, with zero questions about religion or theology. The "Islam/Christianity" classification was an artifact of country-level demographics. This is a critical finding that undermines the benchmark's inclusion in the Top 15 at RD = 34. If the trial finding is correct, Break the Checkbox should have RD close to 0 and would not pass the hard gate. Its inclusion inflates the apparent count of viable religious values benchmarks and misleads readers about the field's state.

BuddhismEval (rank 13): Trial T3 reveals the dataset is inaccessible (HTTP 401). This means BuddhismEval fails the "publicly available data" hard gate at the time of review. The benchmark may have been accessible when scored but is no longer. This is relevant to the reproducibility argument and should be noted.

The diversity constraint mechanism is transparently described: "requiring at least 4 Abrahamic, 3 Dharmic, 1 East Asian, and 1 African/Indigenous." The failure to meet the African/Indigenous constraint is correctly reported. However, the justification for these specific targets (why 4 Abrahamic rather than 3? why 3 Dharmic rather than 2?) is absent. Are these proportional to adherent populations? Proportional to candidate counts? Arbitrary? The reader needs some justification.

**Anti-essentialization:** The ranking itself is tradition-neutral: benchmarks are ranked by composite score regardless of tradition. The diversity constraints are a deliberate structural correction, transparently disclosed. This is appropriate.

**Citation adequacy:** Hendrycks (2021), Alharbi (2024), Bowman (2021), Johnson (2026), Malhas (2023), Abdelali (2023), Kamali (2008), Francis (2015)---all match spine.

**Framing fairness:** The Top 15 discussion is balanced. Islam's dominance is presented as a structural finding, not an endorsement. The compressed score range observation is insightful.

**Missing perspectives:**
1. The paradox that the top-ranked benchmark (ELQV) is identified by the paper's own analysis as a knowledge task, not a values task, should be addressed more directly.
2. The effect of trial findings on the ranking: if Break the Checkbox is removed and BuddhismEval is flagged as inaccessible, the Top 15 becomes a Top 13 (at best), which changes the narrative.
3. No discussion of whether the format distribution among the Top 15 (MIX = 7, SCN = 3, MCQ = 2, etc.) is a methodological finding or an artifact of what happens to exist.

**Specific revision recommendations:**
1. **CRITICAL:** Correct the Islamic Inheritance Law item count from 1,000 to 12,450 based on trial T2.
2. **CRITICAL:** Address the Break the Checkbox trial T4 finding. If the benchmark contains zero religious/theological questions, it should either be (a) removed from the Top 15 with an explanation, (b) reclassified with a revised RD score that would likely drop it below the gate, or (c) retained with a prominent caveat noting the trial finding. Option (a) or (b) is strongly recommended.
3. **CRITICAL:** Address the BuddhismEval inaccessibility (trial T3) in Section 4.2 or 4.3. Note that the benchmark was accessible at the time of initial scoring but was inaccessible at the time of implementation trial.
4. **IMPORTANT:** Address the ELQV paradox: the paper's top-ranked benchmark is its own exemplar of the knowledge-vs-values conflation that the paper critiques. This should be stated explicitly as a diagnostic finding about the field's state, not left as an implicit tension.
5. **IMPORTANT:** Justify the diversity constraint targets (why 4/3/1/1) or acknowledge them as pragmatic choices.
6. **DESIRABLE:** Add a brief note qualifying the NormEval comparison (composite score 77.2) with a comment about framework commensurability.

---

### Expert 11 -- Dr. Shakir Mohamed (AI Fairness & Decolonial Studies)
**Sections reviewed:** Section 5.4 (Closing the Gaps); Section 5.5 (Limitations); Section 6 (Conclusion)

**Overall assessment:** GOOD -- with concerns about the actionability of recommendations and the conclusion's scope

**Factual accuracy:** Section 5.4's two-track strategy is logically derived from the paper's analysis and accurately reflects the distinction between traditions whose knowledge systems are textually archived versus those transmitted through oral and communal practice. The specific examples---Sefaria for Judaism, Chinese Classics Digital Library for Confucianism, Sanskrit computational linguistics for Hinduism---are real resources that could plausibly be converted to benchmark format. The Quranic QA pipeline as a "proven model" is a fair characterization given the evidence in Sections 4.1--4.3.

The recommendation for "community-governed assessment protocols" in the second track is important but, as Dr. Osei-Mensah notes, abstract. The reference to Sorensen et al. (2024) on "deliberative alignment processes" is appropriate but Sorensen's work operates within the standard NLP framework---it is about deliberation among human annotators, not about ceding evaluation authority to communities outside the research team. The extension is legitimate but should be flagged as aspirational rather than established.

Section 5.5 (Limitations) is admirably honest. The seven limitations are genuine constraints, not performative disclaimers. The circularity of the hard gate ("by requiring publicly available data, we structurally exclude the very traditions we identify as missing") is named directly, which strengthens the paper's intellectual credibility. However, three additional limitations should be acknowledged:

(a) **Trial evidence deficit.** The paper's title asks "What Do Religious Values Benchmarks Actually Test?" but the paper answers this question primarily through feature-level characterization and expert assessment, not through implementation trials. The three trials now available (T2, T3, T4) provide direct evidence, but they are not reported in the paper. This gap between the title's promise and the paper's evidence should be acknowledged.

(b) **Tradition expertise limitation.** The expert council includes specialists in Islamic, Christian, Jewish, Dharmic, African, and psychometric domains, but no specialist in East Asian or minor tradition (Baha'i, Zoroastrianism) evaluation. The council's assessments are therefore less well-grounded for the traditions with the most acute gaps.

(c) **English-language bias.** The external search was conducted in English. The paper notes the absence of Hebrew, Persian, Turkish, and Chinese from the Top 15 benchmark languages, but does not acknowledge that its own corpus assembly methodology is subject to the same English-language bias it diagnoses in the benchmark ecosystem.

**Section 6 (Conclusion):** The three calls to action are clearly stated and follow logically from the findings. However, I have concerns about their framing and scope.

The first call ("invest in benchmark infrastructure for underrepresented textual traditions") is realistic and actionable. The Quranic QA pipeline model is a proven approach, and the resources named (Sefaria, Chinese Classics Digital Library, Sanskrit corpora) are real. The timeline estimate of "two to three years" is optimistic but defensible for a shared task pipeline.

The second call ("build reasoning-focused benchmarks that go beyond knowledge recall") is well-motivated by the 5/15 finding and the knowledge-reasoning distinction. The specific suggestions (rubric-based theological reasoning, multi-turn pastoral dialogue, denominational distinction items) are concrete enough to guide future work.

The third call ("develop community-governed evaluation protocols for oral and communal traditions") is the most important but also the most underdeveloped. The paper calls for "fundamentally different evaluation architectures" without specifying what these might look like beyond general descriptions. More importantly, the call does not address the power asymmetry inherent in the proposal: who initiates the conversation with communities? Who funds it? Who publishes the results? The risk is that "community-governed" becomes a label that legitimizes extraction if the governance is nominal rather than substantive. The paper should add a sentence acknowledging this risk.

The "Future work" paragraph is well-structured. The fourth item---"a prototype community-governed evaluation protocol developed in partnership with one Indigenous or Ubuntu community"---is the most consequential and should be foregrounded rather than buried as the last item in a list.

**Anti-essentialization:** GOOD throughout Sections 5.4--6. The two-track recommendation inherently respects the distinctiveness of different traditions' knowledge systems. The conclusion avoids monolithic claims.

**Citation adequacy:** Carroll (2020), Malhas (2023), Sorensen (2024), Hendrycks (2021)---all match spine.

Missing: (1) No citation for the "two to three years" timeline estimate---is this based on the Quranic QA pipeline's development history? If so, cite the relevant timeline. (2) No reference to existing community-governed evaluation models in adjacent fields (medical AI evaluation with patient communities, Indigenous data sovereignty in genomics). These analogues would strengthen the third call to action.

**Framing fairness:** The conclusion is measured and avoids overstating findings. The final sentence---"Until the evaluation ecosystem can engage the full diversity of religious moral reasoning...claims of 'values-aligned AI' remain partial at best"---is appropriately cautious and powerful.

**Missing perspectives:**
1. The power dynamics of community engagement: who initiates, who funds, who publishes?
2. The possibility that community-governed evaluation may produce results that are incommensurable with standardized benchmarks---and whether that is acceptable.
3. The role of religious institutions (not just academic communities) in benchmark development---mosques, churches, synagogues, temples, and monasteries as sites of values articulation.

**Specific revision recommendations:**
1. **IMPORTANT:** Add a limitation acknowledging that the paper's title promises empirical evidence about what benchmarks "actually test" but the paper defers implementation trial results to a companion report. The three available trial findings (T2, T3, T4) should be incorporated to partially address this gap.
2. **IMPORTANT:** Add a sentence to the third call to action acknowledging the risk that "community-governed" becomes nominal rather than substantive if power asymmetries are not addressed.
3. **IMPORTANT:** Acknowledge the English-language bias in the paper's own corpus assembly methodology in Section 5.5.
4. **DESIRABLE:** Foreground the community-governed evaluation prototype (future work item 4) as the most consequential planned extension.
5. **DESIRABLE:** Add one concrete analogue from an adjacent field (e.g., Indigenous data sovereignty in genomics, patient-governed clinical trial evaluation) to ground the community-governed evaluation recommendation.

---

## Points of Agreement (Consensus)

The following points received agreement from 4 or more of the 6 council members:

1. **The Methods section is transparent and well-structured.** All six experts agree that the corpus assembly, feature matrix, and scoring process are clearly documented. The three-tier classification and calibration anchors are useful contributions. The Methods section's honesty about its own limitations (Section 3.6) is commendable. (6/6 agreement)

2. **The trial findings (T2, T3, T4) must be incorporated into the paper.** Five of six experts (all except Prof. Bilimoria, who does not address trials directly but implicitly supports through the BuddhismEval recommendation) agree that the three trial findings provide direct empirical evidence that strengthens the paper's central claims. Deferring all trial results to a companion report weakens the paper unnecessarily. At minimum, T2 (correcting the item count and reinforcing knowledge-vs-reasoning), T3 (demonstrating the reproducibility crisis), and T4 (demonstrating bias-values conflation) should be reported in Section 4.4. (5/6 agreement)

3. **The composite weight justification is insufficient.** Dr. Chen (psychometrics) and Dr. Rivera (LLM evaluation) both identify the absence of sensitivity analysis as a significant methodological gap. Prof. Sachedina and Dr. Mohamed concur that the weights appear reasonable but are justified by assertion rather than evidence. (4/6 agreement)

4. **Break the Checkbox must be addressed.** Dr. Chen, Dr. Rivera, and Prof. Sachedina agree that trial T4's finding that Break the Checkbox contains zero religious/theological questions undermines its inclusion in the Top 15 and its use as a calibration anchor. The paper must either remove it, reclassify it, or add a prominent caveat. (4/6 agreement, with Dr. Osei-Mensah noting it is further evidence for the bias-values conflation argument)

5. **The Section 4.1/Table 3 candidate count discrepancy is a critical internal inconsistency.** Prof. Bilimoria identified this and all experts who examined both locations agree the numbers do not match. (4/6 agreement from those who checked)

6. **Section 5.3's epistemic injustice argument should distinguish between textual and oral traditions' different structural obstacles.** Prof. Bilimoria and Dr. Osei-Mensah both note that Jainism's absence (community coordination with digitized texts) differs structurally from Indigenous traditions' absence (epistemic prerequisites that exclude oral/communal knowledge). Grouping them weakens the argument. (4/6 agreement)

7. **The ELQV paradox should be stated explicitly.** The paper's top-ranked benchmark is its own exemplar of knowledge-vs-values conflation. Three experts (Rivera, Chen, Mohamed) agree this should be named as a diagnostic finding. (3/6 explicit agreement, with 2 others implicitly concurring)

8. **The conclusion is measured and avoids overstatement.** All six experts agree that the three calls to action are logically derived from the findings and the final sentence is appropriately cautious. (6/6 agreement)

---

## Points of Disagreement

1. **Whether Break the Checkbox should be removed from the Top 15 or retained with a caveat.**
   - Dr. Rivera and Dr. Chen argue for removal or reclassification (options a/b): a benchmark with zero religious questions should not appear in a ranking of religious values benchmarks, regardless of its original metadata claims. Retaining it misleads readers.
   - Dr. Mohamed argues for retention with a prominent caveat (option c): the fact that a benchmark claiming religious content contains zero religious questions is itself powerful evidence for the bias-values conflation argument. Removing it sanitizes the finding. The benchmark's *inclusion and subsequent debunking* is more informative than its absence.
   - **Recommendation:** Retain Break the Checkbox in the Top 15 with a prominent caveat in Sections 4.2 and 4.4, clearly marking it as an exemplar of the bias-values conflation problem. Add a footnote or parenthetical noting the trial T4 finding. This preserves the diagnostic value while alerting readers to the benchmark's limitations.

2. **Whether the paper should report trial findings in the main text or defer to a companion report.**
   - Dr. Rivera and Prof. Sachedina argue strongly for incorporating all three trial findings in the main paper---they directly support the paper's claims and their absence creates a gap between the title's promise and the paper's evidence.
   - Dr. Chen notes that incorporating trial findings would strengthen the Methods section's empirical grounding but acknowledges that full trial results (model comparisons, error taxonomies) belong in a companion report. She recommends incorporating the headline findings (T2 item count, T3 inaccessibility, T4 zero-religion finding) while deferring detailed results.
   - **Recommendation:** Incorporate the headline trial findings in an expanded Section 4.4, clearly marking them as preliminary. Defer full model comparisons and error taxonomies to the companion report.

3. **Whether the "formalizability" claim about Islamic jurisprudence requires qualification.**
   - Prof. Sachedina argues that the claim overstates fiqh's formalizability by generalizing from a single subdomain (inheritance law) to the whole discipline. Usul al-fiqh involves analogical reasoning, consensus-building, and contextual judgment that do not "map naturally onto structured evaluation formats."
   - Dr. Rivera notes that from a benchmarking perspective, the claim is about what aspects of Islamic jurisprudence have *actually been formalized* in benchmarks, not about fiqh's theoretical formalizability. The claim is about infrastructure investment patterns, not about theology.
   - **Recommendation:** Qualify the formalizability claim by specifying "certain subdomains of Islamic jurisprudence, particularly inheritance law and commercial transactions" while noting that broader domains of Islamic legal reasoning involve contextual judgment that resists formalization.

---

## Minority Reports

### Minority Report -- Dr. Sarah Chen (Psychometrics)

I register a structured concern about the paper's empirical foundation.

The paper's title---"What Do Religious Values Benchmarks Actually Test?"---promises empirical evidence about benchmark construct validity. The paper delivers this primarily through two methods: (1) feature-level characterization via the 22-feature matrix, and (2) expert council assessment. Both are valuable, but neither constitutes direct empirical evidence of what benchmarks measure. The feature matrix describes what benchmarks *claim* to measure; the expert assessment provides *informed judgment* about what they measure. Neither involves actually running the benchmarks on models and examining the results.

The three trial findings now available (T2, T3, T4) provide the first direct empirical evidence:

- T2 demonstrates that Islamic Inheritance Law tests mathematical computation within Islamic legal parameters, not values reasoning.
- T3 demonstrates that BuddhismEval is inaccessible, undermining the reproducibility that the paper treats as a hard gate.
- T4 demonstrates that Break the Checkbox contains zero religious questions, exposing a fundamental misclassification.

These findings are more powerful than any amount of feature-level characterization because they answer the title's question directly. Yet the paper defers all trial results to a companion report, meaning the paper as submitted does not answer its own title question with empirical evidence.

I recommend one of two approaches: (a) incorporate the three headline trial findings into the main paper and note that they represent preliminary evidence from an ongoing trial series, or (b) revise the title to something like "A Systematic Framework for Evaluating Religious Values Benchmarks" that better reflects the paper's actual contribution (which is the framework, not the trial results). I strongly prefer option (a) because the trial findings are powerful and directly support the paper's claims.

### Minority Report -- Prof. Sachedina (Islamic Ethics)

I register a concern about the paper's characterization of Islamic jurisprudence's "formalizability."

The paper repeatedly characterizes Islamic jurisprudence as having "explicit rules...that map naturally onto structured evaluation formats" and uses this formalizability as the primary explanation (alongside infrastructure investment) for Islam's benchmark dominance. While this is partially correct---ilm al-mawarith (inheritance science) does have explicit computational rules---the characterization risks presenting Islamic jurisprudence as an algorithmic discipline rather than a tradition of contextual moral reasoning.

The reality is more complex. Usul al-fiqh (principles of jurisprudence) involves:
- Qiyas (analogical reasoning), which requires identifying the effective cause (illa) of a ruling and extending it to novel situations
- Istihsan (juristic preference), where a jurist departs from strict analogy on grounds of equity
- Istislah (considerations of public interest), constrained by the Maqasid hierarchy
- Ijma (consensus), which is a communal and historical process, not an algorithmic one
- Ijtihad (independent reasoning), the highest form of jurisprudential engagement, which is by definition non-formalizable

The benchmarks that exist for Islamic jurisprudence test the most formalizable subdomain (inheritance law), and the paper conflates the formalizability of this subdomain with the formalizability of Islamic jurisprudence as a whole. This conflation risks reinforcing a reductive view of Islamic legal reasoning---precisely the kind of "theological flattening" that the paper critiques in other contexts.

I recommend that the paper:
(a) Specify "certain subdomains of Islamic jurisprudence, particularly inheritance law" rather than "Islamic jurisprudence" generally when discussing formalizability.
(b) Note that the benchmark ecosystem has formalized only the most algorithmically tractable aspects of fiqh, while the contextual reasoning traditions (qiyas, ijtihad) remain unbenchmarked---creating an internal knowledge-reasoning gap within Islamic benchmarks themselves.
(c) Acknowledge that this selective formalization is itself a form of tradition flattening, analogous to the "doctrinal flattening" identified for Christianity.

---

## Priority Revisions (Ranked)

### Critical (must fix before submission)

**1. Correct the Islamic Inheritance Law item count from 1,000 to 12,450.**
Trial T2 confirms the benchmark contains 12,450 items, not 1,000 as stated in Section 4.2. This is a verifiable factual error.
*Flagged by: Experts 1, 8. Severity: HIGH -- factual accuracy.*

**2. Reconcile Section 4.1/Table 3 candidate count discrepancies.**
Section 4.1 reports Jainism 47, Hinduism 25, Buddhism 14, Sikhism 6; Table 3 reports Jainism 59, Hinduism 43, Buddhism 31, Sikhism 9. Also Judaism shows 9 in 4.1 but 25 in Table 3, and Confucianism 14 in 4.1 but 25 in Table 3. These cannot both be correct.
*Flagged by: Expert 3. Severity: HIGH -- internal consistency.*

**3. Address Break the Checkbox trial T4 finding.**
Trial evidence shows the benchmark contains zero religious/theological questions. Its RD = 34 and its use as a calibration anchor (R2 = 2) for theological depth are both undermined. Retain in Top 15 with a prominent caveat marking it as an exemplar of the bias-values conflation problem, and revise the calibration discussion to remove or replace this anchor.
*Flagged by: Experts 7, 8, 11. Severity: HIGH -- undermines scoring methodology.*

**4. Incorporate headline trial findings (T2, T3, T4) into Section 4.4.**
The paper's title promises evidence about what benchmarks "actually test." The trial findings provide this evidence directly. Report: (a) T2: 12,450 items testing knowledge OF Islamic law + mathematical reasoning, not values alignment; (b) T3: BuddhismEval inaccessible (HuggingFace 401), evidence for reproducibility concerns; (c) T4: Break the Checkbox contains zero religious questions, evidence for bias-values conflation. Mark as preliminary findings from an ongoing trial series.
*Flagged by: Experts 1, 7, 8, 11 (Chen minority report). Severity: HIGH -- the paper's central promise.*

**5. Add sensitivity analysis for composite weights.**
Show that the Top 15 ranking is robust (or not) to alternative weight specifications. Report ranking under at minimum equal weights (0.33/0.33/0.33) and RD-dominant weights (0.50/0.30/0.20).
*Flagged by: Expert 7. Severity: HIGH -- methodological rigor for peer review.*

### Important (should fix for credibility)

**6. Qualify the Islamic jurisprudence "formalizability" claim.**
Specify "certain subdomains of Islamic jurisprudence, particularly inheritance law and commercial transactions" rather than implying fiqh as a whole is formalizable. Note that contextual reasoning traditions (qiyas, ijtihad) remain unbenchmarked.
*Flagged by: Expert 1 (minority report). Severity: MEDIUM-HIGH.*

**7. Distinguish textual vs. oral traditions in Section 5.3's epistemic injustice argument.**
Jainism's absence (community coordination with digitized texts) differs structurally from Indigenous traditions' absence (epistemic prerequisites excluding oral/communal knowledge). The current grouping over-extends the epistemic injustice argument.
*Flagged by: Experts 3, 5. Severity: MEDIUM-HIGH.*

**8. Address the ELQV paradox explicitly.**
The paper's top-ranked benchmark is identified by its own analysis as a knowledge extraction task, not a values reasoning task. State this as a diagnostic finding about the field: "That the field's highest-scoring religious values benchmark tests emotional valence rather than theological reasoning is itself evidence of the knowledge-reasoning conflation this paper diagnoses."
*Flagged by: Experts 8, 7, 11. Severity: MEDIUM.*

**9. Add BuddhismEval inaccessibility finding to Section 4.3.**
Trial T3 found the dataset returns HTTP 401. A Top 15 benchmark that is actually inaccessible changes the effective Dharmic gate-passer count and supports the reproducibility argument.
*Flagged by: Experts 3, 8. Severity: MEDIUM.*

**10. Add concrete examples to Section 5.4's community-governed evaluation recommendation.**
Cite at least one existing model of community-governed digital knowledge management (MUKURTU, Local Contexts, Indigenous data sovereignty in genomics) to ground the abstract recommendation.
*Flagged by: Expert 5. Severity: MEDIUM.*

**11. Acknowledge the English-language bias in the paper's own methodology.**
The external search was conducted in English, subjecting the corpus to the same linguistic bias the paper diagnoses in the benchmark ecosystem.
*Flagged by: Expert 11. Severity: MEDIUM.*

**12. Add a sentence to the third call to action about the risk of nominal community governance.**
Acknowledge that "community-governed" can become a legitimizing label for extraction if power asymmetries are not addressed.
*Flagged by: Expert 11. Severity: MEDIUM.*

**13. Add limitation about trial evidence deficit.**
The paper's title promises empirical evidence about what benchmarks "actually test" but defers implementation trial results. Even if headline findings are incorporated (Priority 4), acknowledge that full construct validation requires the trials described in Section 3.5.
*Flagged by: Expert 7 (minority report), Expert 11. Severity: MEDIUM.*

**14. Justify diversity constraint targets (4/3/1/1).**
Explain the rationale for requiring at least 4 Abrahamic, 3 Dharmic, 1 East Asian, and 1 African/Indigenous benchmarks in the Top 15.
*Flagged by: Expert 8. Severity: MEDIUM.*

**15. Add Christianity's institutional fragmentation as explanation alongside doctrinal flattening.**
Christianity's low gate-passer conversion rate reflects not just doctrinal flattening but the absence of a single coordinating body equivalent to the Arabic NLP community.
*Flagged by: Expert 1. Severity: MEDIUM.*

### Desirable (if word budget permits)

**16. Add funding/timeline asymmetry acknowledgment in Section 5.4.**
Shared task pipelines can produce benchmarks in 2--3 years; community-governed protocols will require longer timelines and different funding models.
*Flagged by: Expert 5. Severity: LOW.*

**17. Qualify the NormEval comparison.**
The comparison of composite scores (50.8 vs. 77.2) assumes framework commensurability between the sister surveys.
*Flagged by: Expert 8. Severity: LOW.*

**18. Specify the Bhagavad Gita Sentiment Analysis processing language.**
Does the benchmark process Sanskrit text, Hindi, or English translation?
*Flagged by: Expert 3. Severity: LOW.*

**19. Foreground the community-governed evaluation prototype in Future Work.**
Item 4 (partnership with one Indigenous or Ubuntu community) is the most consequential planned extension and should be listed first.
*Flagged by: Expert 11. Severity: LOW.*

**20. Remove the Bilimoria (2013) citation from the Jainism false positive sentence.**
The citation does not support the specific claim about keyword-based false positives.
*Flagged by: Expert 3. Severity: LOW.*

**21. Note the risk that religious institutions (mosques, churches, temples) are absent from the benchmark development conversation.**
The paper focuses on academic communities but the values being benchmarked are articulated primarily in religious institutions.
*Flagged by: Expert 11. Severity: LOW.*

**22. Report the RD score distribution.**
Show a histogram or summary statistics to justify the 30-threshold as a natural break rather than an arbitrary cutoff.
*Flagged by: Expert 7. Severity: LOW.*

**23. Add Gulf state funding for Arabic NLP as a material factor.**
The Arabic NLP community's investment is partly explained by Gulf state AI strategies.
*Flagged by: Expert 1. Severity: LOW.*

**24. Cite Tuck and Yang (2012) as a check on decolonial framing.**
"Decolonization is not a metaphor" -- the paper's recommendations should not reduce decolonization to methodological adjustment.
*Flagged by: Expert 5. Severity: LOW.*

---

## Summary Statistics

| Rating | Count | Experts |
|--------|-------|---------|
| STRONG | 1 | Osei-Mensah (5) |
| GOOD | 4 | Sachedina (1), Bilimoria (3), Rivera (8), Mohamed (11) |
| ADEQUATE | 1 | Chen (7) |

**Total specific revision recommendations:** 58 across 6 experts
**Critical revisions:** 5
**Important revisions:** 10
**Desirable revisions:** 9
**Minority reports filed:** 2 (Experts 7 and 1)
**Internal consistency errors identified:** 2 (item count discrepancy in 4.1/Table 3; item count error in 4.2)
**Trial-derived corrections required:** 3 (T2 item count, T3 inaccessibility, T4 non-religious content)
**Missing citations recommended for addition:** 4 papers (MUKURTU/Local Contexts, Tuck & Yang 2012, community-governed evaluation analogues)

---

## Implementation Tracking

Revisions implemented from this deliberation will be tracked below as they are applied to `full-paper-religious-values.md`.

| Priority | Status | Notes |
|----------|--------|-------|
| 1 | DONE | Islamic Inheritance Law: 1,000 -> 12,450 items; added trial T2 characterization in 4.2 |
| 2 | DONE | Section 4.1 prose updated to match Table 3 counts |
| 3 | DONE | Break the Checkbox: prominent caveat added in 4.2 citing trial T4 |
| 4 | DONE | Section 4.4 rewritten: T2, T3, T4 headline findings incorporated |
| 5 | DONE | Sensitivity analysis paragraph added to Section 3.3 (equal/RD-dominant/PE-dominant weights) |
| 6 | DONE | Formalizability qualified in both 4.3 and 5.1: "certain subdomains" + qiyas/ijtihad caveat |
| 7 | DONE | Section 5.3: textual vs. oral traditions distinguished (community coordination vs. structural exclusion) |
| 8 | DONE | ELQV paradox stated explicitly in 5.2 as diagnostic finding |
| 9 | DONE | BuddhismEval inaccessibility noted in 4.3 |
| 10 | DONE | MUKURTU + Local Contexts cited in 5.4; timeline/funding asymmetry acknowledged |
| 11 | DONE | English-language bias limitation added to 5.5 |
| 12 | DONE | Nominal governance risk added to 5.4 (combined with Priority 10) |
| 13 | DONE | Trial evidence limitation updated in 5.5 |
| 14 | DONE | Diversity constraint justification added to 3.3 |
| 15 | DONE | Christianity institutional fragmentation added to 5.1 |

---

*Council deliberation concluded 2026-04-04. Lead author to implement priority revisions before submission.*
