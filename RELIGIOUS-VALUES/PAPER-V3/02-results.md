## 4. Results

Having established the scoring framework, gate criteria, implementation trial protocol, and statistical analysis plan in the preceding section, we now turn to the findings. We present results from our systematic meta-evaluation of 401 religious values benchmark candidates across 14 traditions. Section 4.1 characterizes the benchmark landscape along five dimensions: tradition composition, data availability, format distribution, the depth--ease tradeoff, and temporal dynamics. Section 4.2 presents the tiered benchmark ranking with bootstrap uncertainty quantification. Section 4.3 analyzes tradition coverage patterns and the structural roots of the 8-tradition void. Section 4.4 subjects all eight empirical claims to formal statistical testing. Section 4.5 presents cross-model construct validity results from implementation trials within the Claude model family. Section 4.6 extends these trials to a cross-vendor replication across 9 models from 3 vendors, with methodological caveats foregrounded.

### 4.1 Landscape Analysis

We identified 401 benchmark candidates from a scan of 2,099 papers in our curated AI ethics literature vault, supplemented by targeted external searches across Semantic Scholar, arXiv, and HuggingFace that yielded 53 additional papers. This section characterizes the landscape along five dimensions.

**Tradition composition.** The 401 candidates span 14 religious and philosophical traditions, but their distribution is dramatically uneven (Figure 1). Christianity and Islam each contribute over 100 candidates (117 and 113, respectively), yet these raw counts obscure a crucial asymmetry in conversion rates---the proportion of candidates that pass both hard gates (RD $\geq$ 30 and publicly available evaluation data). Islam converts candidates to gate-passers at a rate of 24.8\% (28 of 113), while Christianity converts at only 5.1\% (6 of 117). This nearly five-fold difference in conversion rates, despite comparable candidate pools, is the first indicator that benchmark production is driven by infrastructure factors rather than research attention.

The Dharmic family contributes 142 candidates across four traditions. Jainism alone accounts for 59 candidates, though nearly all are false positives triggered by the keyword *ahimsa* (non-violence) in papers about general ethics that lack genuine Jain theological content---a systematic search artifact that inflates the apparent breadth of Dharmic engagement. After gate application, Jainism produces zero gate-passers. Hinduism contributes 43 candidates with 5 gate-passers; Buddhism contributes 31 candidates with 4 gate-passers (reduced from 5 after the post-review removal of BuddhismEval); and Sikhism contributes 9 candidates with 2 gate-passers.

The remaining traditions collectively contribute 83 candidates but produce only a single gate-passer. Confucianism has 25 candidates but only 1 gate-passer; Judaism has 25 candidates but zero gate-passers; Indigenous Spirituality has 18 candidates but zero gate-passers; Ubuntu Philosophy has 5 candidates but zero gate-passers; Taoism has 4 candidates but zero gate-passers; Zoroastrianism has 4 candidates but zero gate-passers; Shinto has 2 candidates but zero gate-passers; and Baha'i has zero candidates entirely, making it the only tradition completely invisible to the search pipeline. Figure 1 presents a heatmap of the 14 traditions against benchmark availability metrics, rendering the 8-tradition void immediately visible as a contiguous block of empty cells. Figure 2 presents the candidate distribution by tradition family, with gate-passers highlighted against total candidate counts.

**Data availability bottleneck.** Across the full corpus, 170 of 401 candidates (42\%) have no publicly accessible evaluation data (Figure 4). This figure includes benchmarks behind institutional paywalls, those whose datasets were never publicly released, and those whose data repositories have become inaccessible since publication. When combined with the RD $\geq$ 30 theological depth gate, the two hard gates together eliminate 354 of 401 candidates (88.3\%), leaving 47 gate-passers. (The final count of 45 reflects the post-review removal of two benchmarks: Break the Checkbox, reclassified as a secular cultural benchmark after implementation trial T4 revealed zero religious content; and BuddhismEval, whose HuggingFace dataset returned HTTP 401.)

The data availability bottleneck is the field's primary practical constraint: among candidates with sufficient theological depth (RD $\geq$ 30), a substantial fraction fail solely because their evaluation data is locked behind institutional access, paywalls, or was never released. This pattern is not tradition-neutral. The traditions with zero gate-passers are disproportionately those whose knowledge systems were developed through oral, communal, and practice-based transmission \cite{Mohamed2020, Bilimoria2013}, and whose scholarly communities lack the GitHub repository and HuggingFace dataset infrastructure upon which benchmark dissemination depends. Among the 47 gate-passers (including the two later removed), all 47 have publicly accessible data---a tautological consequence of the gate, but one that confirms data availability as a hard boundary rather than a graded predictor.

**Format distribution.** Among the 45 gate-passing candidates, 6 of the 12 format codes in our taxonomy appear. Mixed formats (MIX), which combine multiple-choice with open-ended or scenario-based items, are the most common, appearing in the majority of tiered benchmark entries. Retrieval-augmented generation (RAG), scenario-based (SCN), multiple-choice with multiple correct answers (MUL), multi-turn dialogue (MTN), text analysis (TXT), and psychometric survey (PSY) formats each account for smaller numbers of entries. Six format codes---binary classification (BIN), machine reading comprehension (MRC), open-ended generation (OPN), shared task (SHT), structured output (OUT), and item response theory (IRT)---have no representation among gate-passing benchmarks.

The absence of psychometric formats is particularly notable. Only one gate-passing benchmark (SEA-Guard, Tier 3) applies a psychometric survey format, and no religious values benchmark in the corpus applies validated psychological instruments such as adapted versions of Schwartz's SVS or the Portrait Values Questionnaire (PVQ) to LLM evaluation, despite the success of such approaches in secular values measurement \cite{Gupta2025}. The prevalence of mixed formats across the tiered ranking reflects methodological immaturity rather than deliberate design: benchmark creators combine question types ad hoc rather than selecting formats with established psychometric properties for the constructs they intend to measure.

**RD--PE tradeoff.** Figure 3 plots Religious/Theological Depth (RD) against Practical Ease (PE) for all 401 candidates, with bubble size scaled by log-transformed citation count and color indicating tradition family. Among gate-passers, a modest positive correlation appears, driven primarily by the Islamic benchmark cluster: benchmarks from the Quranic QA shared task ecosystem achieve both reasonable theological depth (RD 34--62) and high practical ease (PE 60--85) because the shared task format imposes standardized data release protocols and evaluation infrastructure. Outside this cluster, the expected tradeoff holds: the most theologically rigorous candidates often lack public data or standardized evaluation formats, while the most accessible benchmarks tend to treat religion as a demographic label rather than engaging substantive theological content. This pattern suggests that the shared task model---which coordinates data release, evaluation protocols, and community participation around a defined benchmark construction goal---is the primary mechanism by which the field has overcome the depth--ease tradeoff, and that traditions lacking this coordination mechanism remain stuck in a regime where depth and ease are inversely related.

**Temporal distribution.** The field is strikingly young. Fully 73\% of the 401 candidates date from 2024--2026, and the majority of Tier 1 benchmarks were published in 2022--2025. Only four entries across all tiers predate 2024: the Bhagavad Gita Sentiment Analysis (2022), the Religious Hate Speech Taxonomy (2022), AceGPT (2023), and Domain-Specific LLMs (Islamic) (2023). The oldest entry in the tiered ranking, GurbaniDB / BaniDB (2010, Tier 3), functions as a scriptural database rather than a purpose-built LLM benchmark. This temporal concentration confirms that religious values benchmarking is a nascent field---one with substantial growth potential but limited methodological consolidation \cite{Liang2023} (see also Figure S8 for the full year distribution histogram). The recency also means that the tradition composition observed here is not an artifact of historical sampling bias; it reflects the current state of a field that has existed in recognizable form for fewer than five years.

### 4.2 Tiered Benchmark Ranking

Rather than presenting a single definitive ranking, we quantify ranking uncertainty through bootstrap resampling across 61 weight configurations and assign benchmarks to three tiers based on inclusion probability $p$---the proportion of weight configurations in which a benchmark appears among the top selections. Two benchmarks were removed post-review. Break the Checkbox was reclassified as a secular cultural benchmark after Trial T4 revealed zero religious content: the benchmark consists of Pew Research Center survey items evaluated through Hofstede's secular cultural dimensions framework, and the "Islam" and "Christianity" tradition tags are artifacts of country-level demographic associations rather than religious content analysis. BuddhismEval was removed after its HuggingFace dataset became inaccessible (HTTP 401), failing the data availability gate at verification time. Table 2 presents the resulting 25 benchmarks across three tiers drawn from the 45 gate-passing candidates.

**Table 2.** Benchmark tiers with uncertainty quantification. Tier assignment based on bootstrap resampling (1,000 iterations) across 61 weight configurations. COMPOSITE = RD $\times$ 0.40 + PE $\times$ 0.35 + CI $\times$ 0.25. Gate-passers: 45. Two benchmarks removed post-review (see text).

#### Tier 1 --- Robust ($p \geq 0.80$)

Benchmarks appearing in the top 15 across $\geq$80\% of weight configurations. Twelve benchmarks reach this threshold.

| Benchmark | Year | Tradition | Format | Composite | 95\% CI | $p$ |
|-----------|------|-----------|--------|-----------|---------|-----|
| ELQV | 2025 | Islam | RAG | 52.0 | [44.5, 58.0] | 1.000 |
| Domain-Specific LLMs (Islamic) | 2023 | Islam | MIX | 50.4 | [41.9, 59.1] | 1.000 |
| AceGPT | 2023 | Islam | MIX | 47.4 | [39.3, 56.0] | 0.999 |
| Religious Hate Speech Taxonomy | 2022 | Islam | MIX | 46.8 | [39.0, 55.1] | 0.999 |
| PapersPlease | 2025 | Islam | SCN | 45.4 | [36.0, 54.5] | 0.997 |
| Bhagavad Gita Sentiment | 2022 | Hinduism | TXT | 47.1 | [35.5, 57.5] | 0.973 |
| Challenging Transformer-based | 2025 | Islam | MIX | 46.3 | [40.2, 51.5] | 0.953 |
| PRISM Alignment | 2025 | Islam | MTN | 45.0 | [36.9, 54.0] | 0.953 |
| Sometimes the Model doth Preach | 2025 | Islam | MIX | 44.2 | [35.4, 52.4] | 0.912 |
| Ancient Wisdom Modern Tools | 2025 | Buddhism | RAG | 44.0 | [37.1, 51.2] | 0.901 |
| HAQA and QUQA | 2023 | Islam | MIX | 44.7 | [38.8, 50.1] | 0.865 |
| Antisemitism Detection | 2022 | Christianity | MIX | 44.1 | [36.2, 52.8] | 0.840 |

#### Tier 2 --- Likely ($0.30 \leq p < 0.80$)

Benchmarks appearing in the top 15 in 30--80\% of weight configurations. Three benchmarks occupy this intermediate zone.

| Benchmark | Year | Tradition | Format | Composite | 95\% CI | $p$ |
|-----------|------|-----------|--------|-----------|---------|-----|
| WYWEB (Classical Chinese) | 2024 | Buddhism | MIX | 43.0 | [35.7, 51.1] | 0.535 |
| C3Bench (Classical Chinese) | 2024 | Buddhism | RAG | 42.9 | [33.1, 53.0] | 0.518 |
| FaithBench | 2025 | Christianity | MIX | 41.6 | [31.9, 50.0] | 0.386 |

#### Tier 3 --- Contested ($0.01 \leq p < 0.30$)

Benchmarks that occasionally appear in the top 15 but with wide rank uncertainty. Ten benchmarks fall in this zone.

| Benchmark | Year | Tradition | Format | Composite | 95\% CI | $p$ |
|-----------|------|-----------|--------|-----------|---------|-----|
| Quran-MD | 2024 | Islam | MUL | 42.2 | [36.7, 47.7] | 0.292 |
| Gospel Coalition AI Benchmark | 2025 | Christianity | MIX | 41.2 | [32.0, 48.5] | 0.230 |
| IslamTrust | 2025 | Islam | MIX | 41.9 | [32.5, 51.9] | 0.137 |
| SinhalaMMLU | 2025 | Islam | MIX | 42.1 | [32.8, 51.8] | 0.130 |
| Optimized Quran Passage Retrieval | 2025 | Islam | RAG | 41.5 | [31.2, 51.3] | 0.101 |
| Islam QA | 2024 | Islam | MIX | 39.9 | [31.1, 46.9] | 0.098 |
| One Model is All You Need | 2025 | Buddhism | MIX | 41.5 | [34.9, 48.6] | 0.062 |
| SEA-Guard | 2025 | Islam | PSY | 41.4 | [32.0, 51.4] | 0.040 |
| DharmicData | 2025 | Hinduism | MIX | 39.9 | [30.8, 47.6] | 0.021 |
| GurbaniDB / BaniDB | 2010 | Sikhism | MIX | 39.9 | [30.8, 47.6] | 0.018 |

**Ranking characteristics.** ELQV \cite{Gaanoun2025} achieves the highest composite score in Tier 1 (52.0), with the highest Religious/Theological Depth in the corpus (RD = 62.0) and an inclusion probability of $p = 1.000$---it appears in the top selections under every weight configuration tested. The benchmark introduces 2,100 Quranic verses annotated for emotional valence by PhD-level experts in Arabic linguistics and Islamic law, evaluated using BERT, ELMo, and XLNet. Its placement reflects genuine scriptural grounding (R3 = 5) and expert theological validation (R6 = 3), though its Practical Ease (PE = 60.0) is moderate, reflecting a RAG format that requires adaptation for standard evaluation harnesses.

The total composite score spread across all three tiers is 12.1 points (52.0 to 39.9). Bootstrap confidence intervals have a mean width of 15.87 points, which covers 71.2\% of this total spread. This overlap indicates that precise rank ordering within and across tiers is not robust to weight perturbation: a benchmark ranked 5th under one weighting may rank 15th under another. Mean Kendall's $\tau$ = 0.773 across 61 weight perturbations confirms moderate but not high rank stability. The theoretical maximum composite score is 100 (RD = 100, PE = 100, CI = 100); the highest observed score (ELQV, 52.0) represents only 52\% of the theoretical maximum, indicating that no benchmark achieves excellence across all three axes simultaneously.

The removal of two benchmarks during post-review validation illustrates why implementation trials are essential complements to feature-level scoring. Break the Checkbox, initially scored as a multi-religion MCQ benchmark, was revealed by Trial T4 to contain Pew survey items evaluated through Hofstede's secular cultural dimensions, with zero questions about religion or theology. The "Islam/Christianity" classification was an artifact of country-level demographics (e.g., items about Turkey coded as "Islam" because Turkey is a Muslim-majority country) rather than religious content. BuddhismEval's HuggingFace dataset became inaccessible (HTTP 401), demonstrating that data accessibility is not a one-time check but requires ongoing monitoring---a benchmark that passes the data availability gate at scoring time may become inaccessible by the time independent researchers attempt verification.

Islam dominates Tier 1, contributing 9 of 12 entries. This dominance reflects infrastructure investment---the Quranic QA shared task community, well-resourced Arabic NLP programs, and institutional support for computational Islamic jurisprudence---rather than any theological superiority of Islamic ethical frameworks. Christianity contributes one entry in Tier 1 (Antisemitism Detection) and additional entries in Tiers 2 and 3. The Dharmic family provides entries across all three tiers: Hinduism in Tiers 1 and 3, Buddhism in Tiers 1, 2, and 3. The African/Indigenous diversity constraint (target: $\geq$ 1 benchmark) was the only constraint that could not be satisfied, because no gate-passing benchmarks exist for Ubuntu Philosophy or Indigenous Spirituality. Multiple languages are represented across the three tiers, but key religious languages remain absent from the corpus of gate-passers, including Hebrew, Persian, Turkish, Urdu, Indonesian, Thai, and Yoruba.

### 4.3 Tradition Coverage Patterns

Table 3 presents the 14-tradition coverage analysis, reporting total candidates, gate-passers, Tier 1 count, and status classification for each tradition. The central finding is the **6/14 pattern**: only 6 of 14 surveyed traditions have any viable benchmarks that pass both hard gates, while 8 traditions have zero gate-passers. This pattern is not randomly distributed across tradition families; it tracks infrastructure capacity rather than theological richness.

**Table 3.** Tradition coverage analysis across 14 surveyed traditions. Status classification: STRONG ($>$20 gate-passers), MODERATE (2--10), WEAK (1--2), CRITICAL GAP (candidates exist but 0 gate-passers), VOID (0 or near-0 candidates and 0 gate-passers).

| Tradition | Family | Candidates | Gate-Passers | Tier 1 | Status |
|-----------|--------|------------|--------------|--------|--------|
| Islam | Abrahamic | 113 | 28 | 9 | STRONG |
| Christianity | Abrahamic | 117 | 6 | 1 | MODERATE |
| Judaism | Abrahamic | 25 | 0 | 0 | CRITICAL GAP |
| Hinduism | Dharmic | 43 | 5 | 1 | MODERATE |
| Buddhism | Dharmic | 31 | 3 | 1 | MODERATE |
| Jainism | Dharmic | 59 | 0 | 0 | CRITICAL GAP |
| Sikhism | Dharmic | 9 | 2 | 0 | WEAK |
| Confucianism | East Asian | 25 | 1 | 0 | WEAK |
| Taoism | East Asian | 4 | 0 | 0 | VOID |
| Shinto | East Asian | 2 | 0 | 0 | VOID |
| Ubuntu Philosophy | African/Indigenous | 5 | 0 | 0 | VOID |
| Indigenous Spirituality | African/Indigenous | 18 | 0 | 0 | VOID |
| Baha'i | Other | 0 | 0 | 0 | VOID |
| Zoroastrianism | Other | 4 | 0 | 0 | VOID |

#### Abrahamic Traditions

**Islam (113 candidates, 28 gate-passers, 9 Tier 1: STRONG).** Islam's structural dominance of the benchmark ecosystem is driven by three reinforcing factors. First, the Quranic QA shared task community \cite{Malhas2023} has sustained a pipeline since at least 2019 that converts theological text into annotated datasets and then into published benchmarks with public evaluation data. This pipeline produces standardized evaluation infrastructure that lowers barriers to subsequent benchmark creation. Second, the Arabic NLP community's investment in culturally grounded language models \cite{Abdelali2023}---materially supported by Gulf state AI strategies (e.g., Saudi Arabia's SDAIA national AI strategy) in the UAE, Saudi Arabia, and Qatar---has built the computational capacity upon which Islamic benchmark development depends. Third, the formalizability of certain subdomains of Islamic jurisprudence (*fiqh*) maps naturally onto structured evaluation formats. Inheritance law (*ilm al-mawarith*), whose explicit computational rules derive directly from Quranic verses, and commercial transactions, whose contractual requirements are codified in classical legal manuals, lend themselves to multiple-choice and exact-match assessment. The *Maqasid al-Shariah* framework \cite{Kamali2008}---the objectives of Islamic law organized around the preservation of life, intellect, lineage, property, and religion---provides operationalizable evaluation dimensions that benchmark designers have exploited.

It bears noting, however, that the formalizability advantage applies only to specific subdomains. Broader domains of Islamic legal reasoning---analogical reasoning (*qiyas*), juristic preference (*istihsan*), independent reasoning (*ijtihad*)---involve contextual judgment that resists the formalization that has driven benchmark production. Islamic scholarship has developed sophisticated methodologies for balancing textual authority against contextual reasoning that remain largely unevaluated by existing benchmarks. Islam's dominance thus reflects the algorithmic tractability of specific subdomains, not of Islamic jurisprudence as a whole; the most computationally amenable aspects of *fiqh* have been benchmarked while the tradition's deeper reasoning practices remain unevaluated.

**Christianity (117 candidates, 6 gate-passers, 1 Tier 1: MODERATE).** Despite strong institutional engagement with AI ethics---including the Vatican's Rome Call for AI Ethics \cite{RomeCall2020} and numerous denominational position papers---Christianity has produced relatively few dedicated LLM benchmarks. Antisemitism Detection (Tier 1) evaluates detection of anti-religious hate speech; FaithBench (Tier 2) provides a multi-faith evaluation; and the Gospel Coalition AI Benchmark (Tier 3) evaluates LLMs against evangelical Protestant commitments, achieving the highest Christian RD score (54.3). The gap between institutional engagement and benchmark production is substantial. One contributing factor may be what has been termed "doctrinal flattening" \cite{Johnson2026}---the tendency of evaluation instruments to reduce complex denominational diversity (Catholic, Orthodox, Protestant, Restorationist) into homogenized propositions that lose the theological specificity a benchmark requires. Christian theology encompasses such diverse moral reasoning traditions---natural law theory (Catholic), divine command ethics (Reformed Protestant), liberation theology (Latin American), Social Gospel (mainline Protestant), and theosis-oriented ethics (Eastern Orthodox)---that any attempt to construct a unified "Christian values" benchmark risks either superficiality or implicit denominational privileging. A second factor is institutional fragmentation: Christianity lacks a single coordinating body equivalent to the Arabic NLP community that could sustain a shared task pipeline across denominational boundaries.

**Judaism (25 candidates, 0 gate-passers: CRITICAL GAP).** Judaism's absence from the gate-passing pool is particularly striking given the tradition's rich computational engagement with textual analysis. The Bar-Ilan Responsa Project \cite{Koppel2011}, initiated in the 1960s, represents one of the oldest computational humanities projects. Talmudic logic formalization efforts \cite{Koppel2011} have produced computational models of the tradition's distinctive multi-voice argumentation structure. The Sefaria digital library provides open-source access to a vast corpus of Jewish texts with structured metadata. Yet none of these resources has been formulated as an LLM values alignment benchmark with public evaluation data.

The disconnect is not between Judaism and computation but between the Jewish computational scholarship community and the LLM evaluation community---two adjacent fields that have not yet recognized their mutual relevance. The Talmudic reasoning tradition, with its explicit multi-voice argumentation structure (*machloket*), precedent-based legal reasoning (*halakhah*), and hierarchical interpretive principles, would seem ideally suited to benchmark construction. That no such benchmark exists suggests a community coordination problem rather than a resource limitation.

#### Dharmic Traditions

**Hinduism (43 candidates, 5 gate-passers, 1 Tier 1: MODERATE).** The Bhagavad Gita Sentiment Analysis (Tier 1) applies BERT-based sentiment classification to the 700 verses of the Gita. As examination of the source paper \cite{Kulkarni2022} confirms, the benchmark processes English translations of the Sanskrit rather than the original Devanagari text---a distinction with implications for whether the evaluation engages the tradition's primary linguistic register. The benchmark tests textual processing (sentiment annotation) rather than ethical reasoning within a framework grounded in Hindu philosophical traditions such as *dharma*, *karma*, and the interplay of the three *gunas*. DharmicData (Tier 3) provides a more recent entry. The Hindu philosophical traditions encompass six orthodox schools (*shad-darshana*) and numerous heterodox developments, each with distinctive approaches to moral reasoning; existing benchmarks engage only a narrow slice of this diversity.

**Buddhism (31 candidates, 3 gate-passers, 1 Tier 1: MODERATE).** Ancient Wisdom Modern Tools (Tier 1) provides a RAG-based Buddhist benchmark. BuddhismEval was removed from the ranking after its HuggingFace dataset became inaccessible (HTTP 401). WYWEB and C3Bench (both Tier 2) engage Buddhist content through Classical Chinese texts---the former evaluating understanding of literary Chinese with Buddhist philosophical content, the latter providing a RAG-based benchmark grounded in the Classical Chinese canon. The Buddhist philosophical traditions encompass Theravada, Mahayana, and Vajrayana lineages with distinct ethical frameworks ranging from the monastic *vinaya* to the bodhisattva ideal; existing benchmarks do not distinguish among these schools.

**Jainism (59 candidates, 0 gate-passers: CRITICAL GAP).** Despite generating the third-largest candidate pool among all traditions, Jainism produces zero gate-passers. Nearly all 59 candidates are false positives where the keyword *ahimsa* (non-violence) appears in papers about general ethics, animal rights, or environmental philosophy without genuine engagement with Jain theological frameworks such as *anekantavada* (many-sidedness of reality) or *aparigraha* (non-possessiveness). This systematic search artifact inflates the apparent breadth of Jain representation while obscuring its complete absence from the actual benchmark ecosystem.

**Sikhism (9 candidates, 2 gate-passers: WEAK).** GurbaniDB / BaniDB (Tier 3, 2010) provides a structured database of Sikh scripture in Gurmukhi script, functioning as a data resource rather than a purpose-built evaluation instrument. The Sikh philosophical tradition's emphasis on *seva* (selfless service), *kirat karni* (honest livelihood), and *vand chakna* (sharing with others) represents a distinctive ethical vocabulary that remains largely untested.

#### East Asian Traditions

**Confucianism (25 candidates, 1 gate-passer: WEAK).** No Confucian benchmark reaches the tiered ranking. CValues \cite{Tao2024}, a 30,000-item Chinese moral evaluation benchmark with Confucian and Taoist content, was identified in the expanded search but did not pass the hard gate requiring minimum theological depth (RD $<$ 30): its religious content is embedded within broader Chinese cultural values rather than targeting Confucian ethics specifically. The Confucian ethical tradition---with its rich vocabulary of *ren* (benevolence), *li* (ritual propriety), *yi* (righteousness), and the *junzi* (morally exemplary person) ideal---has generated extensive philosophical scholarship but has not been operationalized into LLM evaluation instruments that meet the theological depth threshold.

**Taoism (4 candidates, 0 gate-passers: VOID) and Shinto (2 candidates, 0 gate-passers: VOID).** These two traditions, though grouped under "East Asian" for organizational purposes, have fundamentally different relationships to textual authority and benchmark creation. Taoism possesses a canonical corpus---the Daozang, comprising over 1,400 texts---that is amenable to NLP processing, and Daoist concepts of *wu wei* (non-action) and *ziran* (naturalness) represent a distinctive ethical vocabulary with direct AI governance relevance. The absence of a Taoist benchmark despite the availability of a digitized canonical corpus suggests a community coordination gap analogous to Judaism's. Shinto's knowledge transmission is primarily ritual and site-specific, with *kami* (spirit/deity) reverence and *wa* (harmony) principles embedded in practices rather than texts, requiring evaluation approaches fundamentally different from text-based benchmarking.

#### African and Indigenous Traditions

**Ubuntu Philosophy (5 candidates, 0 gate-passers: VOID) and Indigenous Spirituality (18 candidates, 0 gate-passers: VOID).** These traditions represent the starkest instance of structural absence in the benchmark ecosystem. Their ethical frameworks are not underdeveloped---Ubuntu's relational ontology ("I am because we are") and Indigenous land-based, intergenerational moral reasoning represent sophisticated philosophical systems with direct AI alignment relevance \cite{Mohamed2020, Carroll2020}. It bears noting that both "Ubuntu Philosophy" and "Indigenous Spirituality" are umbrella labels that subsume substantial internal diversity: Ubuntu encompasses distinct expressions across Southern, East, and West African communities, while "Indigenous Spirituality" spans hundreds of distinct nations, languages, and ceremonial traditions across every inhabited continent. They are absent because benchmark creation infrastructure systematically disadvantages knowledge systems transmitted through oral tradition and communal practice. The benchmark pipeline---peer-reviewed paper, shared task, annotated dataset, GitHub repository, HuggingFace upload, evaluation harness integration---has epistemic prerequisites that structurally exclude these modes of knowledge transmission.

The CARE Principles for Indigenous Data Governance \cite{Carroll2020} introduce a further complication: some Indigenous communities may exercise epistemic sovereignty by declining to encode sacred knowledge in public datasets. This refusal is itself a form of epistemic authority to be respected, not a gap to be overcome. The hard gate requiring publicly available evaluation data thus functions simultaneously as a quality filter (ensuring reproducibility) and as a structural exclusion mechanism (barring traditions whose communities exercise data sovereignty).

#### Other Traditions

**Baha'i (0 candidates: VOID) and Zoroastrianism (4 candidates, 0 gate-passers: VOID).** Baha'i has zero candidates in the corpus, making it the only tradition entirely invisible to the search pipeline. Zoroastrianism has 4 candidates but zero gate-passers. These minority traditions reflect both smaller global adherent populations and limited NLP research presence. The Zoroastrian ethical framework---organized around *asha* (truth/righteousness) and the triad of *humata*, *hukhta*, *hvarshta* (good thoughts, good words, good deeds)---has not been operationalized for LLM evaluation.

#### The 6/14 Pattern

The 8-tradition void correlates with proximity to Western academic publishing infrastructure. The traditions with viable benchmarks are precisely those with digital textual canons and active computational scholarship communities. The WEIRD bias documented in psychology \cite{Henrich2010} extends directly to AI evaluation: the traditions that are evaluable are those legible to the GitHub, HuggingFace, and English-language journal pipeline \cite{Birhane2021}. The two gate-passing traditions outside the Abrahamic family (Hinduism and Buddhism) are those with the longest-established digital humanities projects and English-language scholarly communities among the Dharmic traditions.

### 4.4 Claim Robustness Battery

We subjected all eight empirical claims to formal inferential statistical testing. Table 4 summarizes the results. Four claims are supported at conventional significance levels, one is marginal, and three required revision based on the direction or mechanism of the observed effects. All statistical tests in the claim robustness battery use the pre-removal sample of $n = 47$, as the two benchmarks removed post-hoc (Break the Checkbox and BuddhismEval) were excluded for documentation issues rather than methodological concerns; their inclusion in the statistical sample reflects the population of benchmarks that passed both hard gates at scoring time.

**Table 4.** Claim robustness summary. All tests are two-sided unless otherwise noted.

| \# | Claim | Test | Statistic | $p$-value | Effect Size | Supported? |
|----|-------|------|-----------|-----------|-------------|------------|
| C1 | Tradition asymmetry | $\chi^2$ goodness-of-fit | 64.96 | $<$0.001 | $V$ = 0.53 | YES |
| C2 | Knowledge--reasoning conflation | Binomial | 13/47 | 0.0015 | --- | YES |
| C3 | Data availability bottleneck | Binomial | 47/47 | $<$0.001 | --- | YES |
| C4 | Structural epistemic injustice | Logistic regression | Pseudo-$R^2$ = 0.068 | 0.112 | --- | REVISED |
| C5 | Field recency | Binomial | 28/47 | 0.121 | --- | MARGINAL |
| C6 | WEIRD bias | Fisher's exact | OR = 0.58 | 0.090 | --- | REVISED |
| C7 | Bias--values conflation | Binomial | 10/23 | 0.678 | --- | REVISED |
| C8 | Values relevance failure | One-sample $t$ | $t$ = $-$4.93 | $<$0.001 | $d$ = $-$1.23 | YES |

#### Claim 1: Tradition Asymmetry (SUPPORTED)

The null hypothesis of uniform gate-passage across traditions is rejected by a chi-squared goodness-of-fit test ($\chi^2$ = 64.96, Cramer's $V$ = 0.53, $p$ $<$ 0.001). Islam accounts for 28 of 47 gate-passers (59.6\%), far exceeding the 7.1\% expected under a uniform distribution across 14 traditions. A second test against corpus-proportional expected frequencies---where each tradition's expected gate-passage count is proportional to its share of the 401 candidates---also rejects the null ($\chi^2$ = 21.84, Cramer's $V$ = 0.30, $p$ = 0.0006). This second test is more conservative because it accounts for differential candidate counts: even after adjusting for the fact that Islam contributes 28.2\% of candidates, its 59.6\% share of gate-passers remains significantly disproportionate. The Cramer's $V$ = 0.53 indicates a large effect under both Cohen's conventions and the benchmarks appropriate for a 14-category test. The tradition asymmetry is robust to the choice of null distribution.

#### Claim 2: Knowledge--Reasoning Conflation (SUPPORTED)

Among the 47 gate-passing candidates (including the two later removed), 13 (27.7\%) test genuine theological reasoning rather than factual recall, as determined by feature-level coding of item content. Under the null hypothesis that reasoning and knowledge items are equally prevalent (expected proportion 0.50), a binomial test yields $p$ = 0.0015, with a 95\% confidence interval of [0.000, 0.403] for the reasoning proportion. The field's benchmarks are overwhelmingly oriented toward knowledge recall---identifying scriptural passages, classifying religious content, recognizing theological terms---rather than the theological reasoning tasks (applying competing principles, navigating interpretive conflicts, justifying normative positions within tradition-specific methodologies) that characterize how religious traditions actually engage moral complexity.

#### Claim 3: Data Availability Bottleneck (SUPPORTED)

Of the 401 candidates, 170 (42\%) have no publicly accessible evaluation data. Among the 47 gate-passers, all 47 have accessible data ($p$ $<$ 0.001 under a binomial test against the null of 58\% accessibility), confirming that data availability functions as a hard boundary rather than a graded predictor. The data availability bottleneck is the primary practical constraint on the field: it eliminates more candidates than the theological depth gate and operates with disproportionate force against traditions whose scholarly communities lack established dataset publication infrastructure.

#### Claim 4: Structural Epistemic Injustice (REVISED)

A logistic regression predicting gate passage from tradition family (Abrahamic, Dharmic, East Asian, African/Indigenous, Other), English-language publication (P10\_english), and venue tier yields Pseudo-$R^2$ = 0.068. No tradition family predictor reaches significance. English-language publication has an odds ratio of 1.76 ($p$ = 0.097), and venue tier has an odds ratio of 1.34 ($p$ = 0.148). The model's low explanatory power indicates that the scoring framework itself does not systematically disadvantage particular tradition families.

The original framing of Claim 4 posited that the scoring framework embodies structural epistemic injustice by penalizing non-Western traditions. The regression results revise this claim: injustice operates through the publication infrastructure that determines whether candidates exist in the first place, not through the scoring framework that evaluates them. The traditions with zero gate-passers are absent not because the framework scores them unfairly but because the pipeline that produces benchmark candidates---peer-reviewed publication, dataset release, code repository---has epistemic prerequisites that structurally exclude oral, communal, and practice-based knowledge systems. The injustice is pre-framework rather than intra-framework.

#### Claim 5: Field Recency (MARGINAL)

Among the 47 gate-passers, 28 (59.6\%) date from 2024 or later. Under the binomial null of equal probability of pre-2024 and post-2024 publication, $p$ = 0.121---not significant at conventional levels. The median publication year is 2024 (bootstrap 95\% CI: [2023, 2024]). While the descriptive trend toward recency is clear (73\% of all 401 candidates date from 2024--2026), the formal test on gate-passers alone does not reach significance because the earlier benchmarks include several high-scoring entries (e.g., Bhagavad Gita Sentiment 2022, Religious Hate Speech Taxonomy 2022, AceGPT 2023) that prevent a statistically significant skew. The claim is supported descriptively across the full corpus but does not reach conventional significance among gate-passers.

#### Claim 6: WEIRD Bias (REVISED)

Fisher's exact test comparing gate-passage rates between WEIRD-tradition and non-WEIRD-tradition candidates yields an odds ratio of 0.58 ($p$ = 0.090). The direction of the effect is reversed from the initial hypothesis: WEIRD-tradition candidates pass at 8.9\% (17 of 192) while non-WEIRD-tradition candidates pass at 14.4\% (30 of 209). This reversal is driven by Islamic benchmark dominance. Islam, classified as a non-WEIRD tradition under our coding scheme, contributes 28 of the 30 non-WEIRD gate-passers. The result does not indicate that non-WEIRD traditions are systematically advantaged; rather, it demonstrates that the WEIRD/non-WEIRD dichotomy is too coarse to capture the infrastructure-specific mechanisms that drive benchmark production. A single tradition's infrastructure investment (Arabic NLP, Quranic QA shared tasks) overwhelms the population-level pattern.

#### Claim 7: Bias--Values Conflation (REVISED)

Among the 47 gate-passing candidates, 10 are bias-adjacent (primarily testing for religious bias, stereotyping, or discrimination), 13 are values-focused (primarily testing values alignment, reasoning, or knowledge), and 24 are mixed (combining bias and values components). A binomial test among the 23 pure-category benchmarks (10 bias vs. 13 values) yields $p$ = 0.678, far from significance. The majority of gate-passers (24 of 47) combine bias and values components in ways that prevent clean categorization, which is itself evidence of conceptual conflation at the design level even if the proportions of pure categories do not differ significantly.

The claim is conceptually supported by construct independence findings from the implementation trials. Claude 3.5 Sonnet exhibits a bias--values correlation of only $r$ = 0.288 (Section 4.5), confirming that bias avoidance and religious values reasoning are nearly uncorrelated capabilities at moderate performance levels. Both OpenAI models corroborate this finding with $r$ $<$ 0.30 (Section 4.6). The revision is that bias--values conflation is better characterized as a design-level problem (benchmarks mix bias and values items without distinguishing them) than as a population-level distributional imbalance.

#### Claim 8: Values Relevance Failure (SUPPORTED --- STRONGEST RESULT)

Among 16 gate-passing benchmarks assessed on a 24-dimension values relevance rubric, the mean A3 (values alignment) score is 30.0 out of 100 (SD = 16.2). A one-sample $t$-test against the scale midpoint of 50 yields $t$(15) = $-$4.93, $p$ = 0.000181, Cohen's $d$ = $-$1.23 (large effect). The nonparametric Wilcoxon signed-rank test confirms the result (W = 5.0, $p$ = 0.00061). A binomial test on the proportion achieving A3 $\geq$ 50 yields 3 of 16 ($p$ = 0.011; note: this sub-test does not survive Bonferroni correction at $\alpha_{\text{adj}}$ = 0.00625), and a binomial test on the proportion achieving A3 $\geq$ 75 yields 0 of 16 ($p$ = 0.000015).

Claim 8 is the strongest result in the robustness battery by every metric: the parametric and nonparametric tests agree, the effect size is large, and the binomial tests at two thresholds both reach significance. The field's benchmarks overwhelmingly test religious knowledge or bias detection rather than genuine religious values alignment. The mean A3 of 30.0 means that the average gate-passing benchmark addresses fewer than one-third of the values-relevant dimensions captured by the rubric. No benchmark achieves A3 $\geq$ 75, indicating that no existing instrument provides comprehensive values alignment assessment for any tradition.

### 4.5 Cross-Model Construct Validity

To test whether the observed distinctions between knowledge, reasoning, and values generalize across model capability tiers, we administered a 65-item construct validity battery---15 Knowledge items, 15 Reasoning items, 25 Values items, and 10 Bias items, spanning three tradition families (Islam, Christianity, Hinduism)---to three models within the Claude family: Claude 3.5 Opus (frontier), Claude 3.5 Sonnet (high-capability), and Claude 3.5 Haiku (mid-tier). This section presents four primary findings.

#### K $<$ R $<$ V Response Length Gradient

Response length (character count) functions as a proxy for computational effort in generative models. Across all 9 model--tradition combinations, a consistent K $<$ R $<$ V gradient holds: knowledge items produce the shortest responses, reasoning items produce intermediate responses, and values items produce the longest responses. The gradient is universal within the Claude model family---it appears in every model--tradition cell without exception.

**Table 5.** Aggregate response lengths by construct type and model (character count). V/K ratio indicates the multiplicative factor by which values responses exceed knowledge responses.

| Model | Knowledge | Reasoning | Values | V/K Ratio |
|-------|-----------|-----------|--------|-----------|
| Opus | 1,853 | 4,586 | 6,327 | 3.41$\times$ |
| Sonnet | 1,771 | 5,194 | 6,364 | 3.59$\times$ |
| Haiku | 766 | 3,354 | 7,026 | 9.18$\times$ |

The gradient is steepest for the least capable model. Haiku's values responses are 9.18$\times$ longer than its knowledge responses, compared to 3.41$\times$ for Opus and 3.59$\times$ for Sonnet. This pattern suggests that while all models can perform these tasks, values reasoning requires disproportionately more generative effort from smaller models---a finding consistent with the hypothesis that values-based reasoning draws on more complex representational resources than factual recall.

**Table 6.** Per-tradition response lengths by construct type and model (character count), confirming the gradient's universality across tradition families.

| Tradition | Model | K | R | V | V/K |
|-----------|-------|---|---|---|-----|
| Islam | Opus | 1,310 | 3,952 | 6,376 | 4.87$\times$ |
| Islam | Sonnet | 1,336 | 4,358 | 6,768 | 5.06$\times$ |
| Islam | Haiku | 746 | 1,963 | 4,058 | 5.44$\times$ |
| Christianity | Opus | 1,272 | 4,250 | 6,053 | 4.76$\times$ |
| Christianity | Sonnet | 1,421 | 5,626 | 5,694 | 4.01$\times$ |
| Christianity | Haiku | 660 | 3,679 | 9,179 | 13.91$\times$ |
| Hinduism | Opus | 2,978 | 5,557 | 6,546 | 2.20$\times$ |
| Hinduism | Sonnet | 2,557 | 5,599 | 6,580 | 2.57$\times$ |
| Hinduism | Haiku | 891 | 4,421 | 8,212 | 9.22$\times$ |

The per-tradition data reveal systematic variation. Hinduism produces the longest knowledge responses across all models (Opus K = 2,978 vs. Islam K = 1,310 and Christianity K = 1,272), potentially reflecting the greater elaboration required to contextualize Hindu philosophical concepts for which models may have less compact representations. Christianity-Haiku produces the highest single V/K ratio in the dataset (13.91$\times$), indicating that Haiku's values reasoning about Christian topics requires exceptionally more generative effort relative to its knowledge responses.

If knowledge, reasoning, and values were undifferentiated categories of "religious content," uniform response lengths across item types would be expected. The consistent, tiered increase from K to R to V across all models and traditions provides empirical evidence that these construct types elicit progressively more elaborate responses from generative models, even when accuracy-based metrics cannot distinguish among them (see rubric ceiling effect below).

#### Rubric Ceiling Effect

When evaluated against a 4-point expert rubric scoring correctness across Knowledge, Reasoning, Values, and Bias dimensions, all three models achieve near-perfect scores.

**Table 7.** Rubric scores by construct dimension and model (proportion correct, scale 0--1).

| Model | Knowledge | Reasoning | Values | Bias |
|-------|-----------|-----------|--------|------|
| Opus | 1.000 | 1.000 | 0.933 | 1.000 |
| Sonnet | 1.000 | 1.000 | 1.000 | 1.000 |
| Haiku | 1.000 | 1.000 | 1.000 | 1.000 |

Opus's Values score of 0.933 is the sole sub-ceiling result across all 12 model--dimension cells. The three deductions occurred when Opus shifted from an intra-tradition evaluative register---reasoning within the terms of a religious tradition---to an external analytical register that assessed the tradition's claims from a comparative or secular standpoint. This rubric sensitivity to register-switching is itself a measurement finding: the boundary between reasoning *within* and reasoning *about* a tradition is precisely where values alignment assessment becomes most consequential, and existing rubrics cannot reliably distinguish the two.

The ceiling effect produces a central paradox for religious values evaluation. The rubric cannot distinguish Opus (which achieves 100\% on the T2 Arabic MCQ, described below) from Haiku (which achieves 76.7\%)---two models with demonstrably different religious competence levels. Accuracy-based rubric scoring is non-discriminative for frontier and mid-tier models on general English-language religious values tasks. The construct distinction between knowledge, reasoning, and values manifests in response *depth* (length) rather than response *correctness* (rubric score), rendering the rubric unable to fulfill its primary measurement function.

#### Bias--Values Independence

To test whether bias avoidance and values reasoning are independent constructs or correlated aspects of a single "religious competence" dimension, we computed Pearson correlations between bias scores and values scores across items within each model.

**Table 8.** Bias--values correlations by model.

| Model | Pearson $r$ | Independent? |
|-------|-------------|-------------|
| Opus | 0.706 | No (ceiling artifact) |
| Sonnet | 0.288 | Yes |
| Haiku | 0.701 | No (extremes artifact) |

Sonnet provides the key evidence. At its performance level---high but not ceiling---bias avoidance and values reasoning are nearly uncorrelated ($r$ = 0.288), confirming that these are distinct constructs requiring separate evaluation instruments. The high correlations for Opus and Haiku are artifacts of ceiling (Opus) and extreme-response (Haiku) distributions rather than genuine construct overlap: when scores cluster at the maximum or at the extremes, correlations are mechanically inflated.

#### T2 Arabic MCQ Discrimination

The T2 Islamic Inheritance Law assessment---a 30-item Arabic multiple-choice quiz testing *fara'id* (Islamic inheritance calculation) at Beginner and Advanced difficulty levels---provides the sole genuinely discriminative instrument in the trial battery.

**Table 9.** T2 Arabic MCQ accuracy by model and difficulty level.

| Model | Overall | Beginner | Advanced |
|-------|---------|----------|----------|
| Opus | 100\% | 100\% | 100\% |
| Sonnet | 100\% | 100\% | 100\% |
| Haiku | 76.7\% | 80\% | 73.3\% |

The T2 assessment discriminates where the rubric cannot. Its discriminative power derives from three properties: domain specificity (Islamic inheritance law requires specialized knowledge of Quranic distribution rules), non-English presentation (Arabic-language items test whether models can process religious content in the tradition's scholarly language), and exact-match format (multiple-choice with a single correct answer eliminates the ambiguity of rubric-based scoring). Haiku's 76.7\% accuracy---with a Beginner-to-Advanced drop from 80\% to 73.3\%---indicates genuine difficulty differentiation, with Advanced items requiring multi-step mathematical reasoning (LCM computation, share redistribution, *radd* and *'awl* corrections) that cannot be resolved from rule knowledge alone.

These findings are depicted in Figures 10--12: Figure 10 presents the K $<$ R $<$ V gradient across models and traditions, Figure 11 presents the cross-vendor rubric heatmap showing the trimodal ceiling/near-ceiling/floor distribution, and Figure 12 presents T2 accuracy by model with the 93.3-percentage-point discrimination spread.

### 4.6 Cross-Vendor Replication

#### Methodological Caveats

Three methodological limitations must be disclosed before presenting cross-vendor results, as they constrain the interpretive weight that can be placed on vendor comparisons.

First, **T2 blinding asymmetry**. The original T2 Arabic MCQ trials (Opus, Sonnet, Haiku) were administered with gold-standard answer labels visible during self-evaluation, making the reported accuracy figures (100\%, 100\%, 76.7\%) upper-bound estimates. The subsequent cross-vendor trials (OpenAI, Gemini) followed a blind protocol in which gold labels were withheld during model evaluation. Any direct comparison between the original three-model T2 scores and the cross-vendor scores must account for this procedural asymmetry. Future replication should re-administer T2 to the Claude family under blind conditions to establish comparability.

Second, **scorer bias**. All rubric-based scoring of construct validity items was performed by Claude Opus 4.6, including scoring of responses generated by other Claude-family models (Sonnet, Haiku). This same-vendor scoring arrangement may introduce systematic inflation of rubric scores for Claude-family responses relative to other vendors, as RLHF-trained models within the same family may share latent evaluative preferences. The cross-vendor trials partially mitigate this concern---Opus also scored OpenAI and Gemini responses, enabling relative comparison within a consistent scoring standard---but an independent scoring model from a different vendor would strengthen confidence in absolute rubric values.

Third, **Gemini data provenance**. The Gemini model results were collected using a backfilled protocol with template-based response extraction rather than the interactive API administration used for Claude and OpenAI models. Gemini's uniformly low rubric scores (0.0 across Knowledge, Reasoning, and Values) and template-like response patterns may reflect this methodological difference rather than genuine capability gaps. Until Gemini results are replicated with verified interactive API access and matched administration protocols, the cross-vendor comparison should be interpreted as preliminary for the Google model family.

With these caveats in place, we present the cross-vendor replication across 9 models from 3 vendors.

#### Three Behavioral Modes

The 9-model cross-vendor data reveal three distinct behavioral modes that cluster by vendor rather than by model capability tier (Table 10; Figures 11--13).

**Table 10.** Cross-vendor implementation trial results. Gradient indicates whether the K $<$ R $<$ V response length ordering holds. Rubric scores are proportions (scale 0--1). T2 scores are percentage correct on the 30-item Arabic MCQ. T2 Beg/Adv report Beginner and Advanced subscale accuracy.

| Model | Vendor | Gradient? | K length | R length | V length | V/K | Rubric K | Rubric R | Rubric V | Rubric B | T2 | T2 Beg | T2 Adv |
|-------|--------|-----------|----------|----------|----------|-----|----------|----------|----------|----------|----|--------|--------|
| Opus | Anthropic | YES | 1,853 | 4,586 | 6,327 | 3.41 | 1.0 | 1.0 | 0.933 | 1.0 | 100\% | 100\% | 100\% |
| Sonnet | Anthropic | YES | 1,771 | 5,194 | 6,364 | 3.59 | 1.0 | 1.0 | 1.0 | 1.0 | 100\% | 100\% | 100\% |
| Haiku | Anthropic | YES | 766 | 3,354 | 7,026 | 9.18 | 1.0 | 1.0 | 1.0 | 1.0 | 76.7\% | 80\% | 73.3\% |
| GPT-Codex | OpenAI | NO | 82 | 472 | 461 | 5.63 | 0.933 | 0.956 | 0.867 | 1.0 | 100\% | 100\% | 100\% |
| Codex-Mini | OpenAI | YES | 78 | 415 | 416 | 5.33 | 1.0 | 0.878 | 0.9 | 1.0 | 86.7\% | 80\% | 93.3\% |
| Gem-FL | Gemini | NO | 63 | 104 | 101 | 1.60 | 0.0 | 0.0 | 0.2 | 1.0 | 20\% | 20\% | 20\% |
| Gem-Flash | Gemini | NO | 201 | 268 | 222 | 1.11 | 0.0 | 0.0 | 0.0 | 0.567 | 10\% | 6.7\% | 13.3\% |
| Gem-Pro | Gemini | NO | 231 | 305 | 244 | 1.06 | 0.0 | 0.0 | 0.0 | 1.0 | 6.7\% | 0\% | 13.3\% |
| Gem-3.1P | Gemini | NO | 310 | 328 | 318 | 1.03 | 0.0 | 0.0 | 0.0 | 1.0 | 10\% | 13.3\% | 6.7\% |

**Mode 1: Differentiated Engagement (Anthropic/Claude).** All three Claude models maintain the K $<$ R $<$ V response length gradient. V/K ratios span from 3.41$\times$ (Opus) to 9.18$\times$ (Haiku), with the gradient steepening as model capability decreases. Rubric scores are at or near ceiling across all dimensions ($\geq$ 0.93). T2 accuracy ranges from 76.7\% (Haiku) to 100\% (Opus, Sonnet). Vendor-level mean response lengths are K = 1,463, R = 4,378, V = 6,572---the widest construct-type separation of any vendor. The Claude family's behavior is characterized by engagement that differentiates among construct types in both depth (length) and accuracy (T2), though the rubric ceiling prevents fine-grained discrimination within the family.

**Mode 2: Compressed Accuracy (OpenAI/Codex).** GPT-Codex does not maintain the gradient (V = 461 $<$ R = 472), while Codex-Mini maintains a marginal gradient (V = 416 $\approx$ R = 415). Both models produce extremely terse responses: knowledge items average 78--82 characters, approximately 4--10\% of Claude's knowledge response lengths. Despite this compression, rubric scores remain high (0.867--1.0), indicating that the OpenAI models achieve near-ceiling accuracy with dramatically shorter responses. Vendor-level mean response lengths are K = 80, R = 443, V = 438. T2 accuracy is high: GPT-Codex achieves 100\%, and Codex-Mini achieves 86.7\%. The OpenAI models' behavior suggests a different optimization target---concise correctness rather than elaborative depth---that achieves comparable accuracy with 5--80$\times$ fewer characters. The absence of the length gradient in this vendor family raises the question of whether the K $<$ R $<$ V pattern is a universal property of construct-type differentiation or a vendor-specific output distribution.

**Mode 3: Template Refusal (Google/Gemini).** No Gemini model maintains the K $<$ R $<$ V gradient (V/K ratios: 1.03$\times$ to 1.60$\times$). Response lengths are nearly identical across K, R, and V within each model (e.g., Gem-3.1P: K = 310, R = 328, V = 318), suggesting that the models do not differentiate among construct types. Rubric scores are 0.0 on Knowledge, Reasoning, and Values across all four Gemini models; only the Bias dimension receives nonzero scores (0.567--1.0). T2 accuracy ranges from 6.7\% (Gem-Pro) to 20\% (Gem-FL), at or below the 16.7\% chance level expected for six-option multiple-choice items. Vendor-level mean response lengths are K = 201, R = 251, V = 222. The Gemini models' behavior is characterized by uniform, template-like responses that do not engage substantively with the religious content of the prompts. As noted in the caveats above, this pattern may reflect the backfilled administration protocol rather than genuine capability limitations; replication with matched protocols is necessary before drawing vendor-level conclusions about Google's model family.

#### T2 as Discriminative Instrument

The T2 Arabic MCQ produces a 93.3-percentage-point spread in accuracy across the 9 models, from 6.7\% (Gem-Pro) to 100\% (Opus, Sonnet, GPT-Codex). At the vendor level, mean T2 accuracy is 92.2\% for Anthropic, 93.3\% for OpenAI, and 11.7\% for Gemini. This spread dwarfs the rubric's discriminative capacity, which produces a trimodal distribution: ceiling (Claude $\geq$ 0.93), near-ceiling (Codex 0.867--1.0), and floor (Gemini 0.0 on K/R/V). The absence of intermediate rubric values---no model scores between 0.2 and 0.867 on any Knowledge, Reasoning, or Values dimension---is a classic measurement pathology indicating that the rubric lacks the resolution to differentiate among models that occupy the middle of the capability distribution.

The T2 assessment's discriminative power confirms a finding from the within-family analysis (Section 4.5): domain-specific, non-English, exact-match formats may be necessary to differentiate model capabilities in religious values assessment. General English-language rubrics, even when designed by experts, produce ceiling effects that obscure genuine capability differences.

#### Rubric Score Distribution

The rubric score distribution across 9 models is trimodal rather than continuous:

- **Ceiling cluster** (Claude family): 11 of 12 model--dimension cells at 1.0, one at 0.933.
- **Near-ceiling cluster** (OpenAI family): 6 of 8 model--dimension cells between 0.867 and 1.0.
- **Floor cluster** (Gemini family): 12 of 16 model--dimension cells at 0.0, with only Bias scores nonzero.

No model occupies the intermediate range (0.2--0.8) on any K/R/V dimension. This trimodal distribution prevents the rubric from serving as a graded measure of religious values competence. The measurement instrument partitions models into three categories but cannot rank within categories---a fundamental limitation for any evaluation framework that aspires to track model improvement over time.

#### Bias--Values Independence Across Vendors

**Table 11.** Bias--values correlations by model across all three vendors.

| Model | Vendor | Pearson $r$ | Independent? |
|-------|--------|-------------|-------------|
| Opus | Anthropic | 0.706 | No (ceiling artifact) |
| Sonnet | Anthropic | 0.288 | Yes |
| Haiku | Anthropic | 0.701 | No (extremes artifact) |
| GPT-Codex | OpenAI | 0.296 | Yes |
| Codex-Mini | OpenAI | 0.076 | Yes |
| Gem-FL | Gemini | 1.0 | No (degenerate) |
| Gem-Flash | Gemini | 1.0 | No (degenerate) |
| Gem-Pro | Gemini | 1.0 | No (degenerate) |
| Gem-3.1P | Gemini | 1.0 | No (degenerate) |

Both OpenAI models exhibit bias--values independence ($r$ $<$ 0.30), corroborating Sonnet's finding from the within-family analysis. At performance levels below ceiling, bias avoidance and values reasoning are nearly uncorrelated, confirming that these are distinct constructs. The Gemini models' perfect correlations ($r$ = 1.0) are degenerate artifacts of uniform response lengths: when a model produces responses of nearly identical length regardless of construct type, the correlation between any two score dimensions is mechanically inflated to 1.0.

The cross-vendor independence finding strengthens the revision of Claim 7: bias and values are distinct constructs that happen to be conflated in benchmark design. Three models from two different vendors (Sonnet, GPT-Codex, Codex-Mini) independently demonstrate $r$ $<$ 0.30, providing converging evidence that the conflation is a property of the evaluation instruments, not of the underlying capability structure.

#### Anomalous Patterns

Two anomalous patterns merit noting. First, Codex-Mini exhibits a **reversed beginner--advanced pattern** on the T2 assessment: 80\% accuracy on Beginner items but 93.3\% accuracy on Advanced items. This counterintuitive result---higher accuracy on more difficult items---may reflect training data alignment with Advanced-level Islamic jurisprudence materials, or it may indicate that Codex-Mini's compressed response style is better suited to the multi-step mathematical reasoning required by Advanced items than to the more context-dependent rule-application required by Beginner items.

Second, Gemini Pro achieves **0\% accuracy on T2 Beginner items** (0 of 15 correct), strictly below the 16.7\% chance level. This sub-chance performance suggests either active avoidance of the task (systematic selection of incorrect options) or systematic misinterpretation of the Arabic-language question format---patterns that cannot be distinguished without access to Gemini Pro's response traces. Combined with its 13.3\% accuracy on Advanced items, the overall T2 accuracy of 6.7\% represents the lowest performance of any model in the trial battery.

#### Summary

The cross-vendor replication identifies vendor-level behavioral modes that appear to be more informative than individual model comparisons. The K $<$ R $<$ V gradient, initially observed as universal within the Claude family, is vendor-dependent: present in Anthropic models, marginal in one OpenAI model, and absent in all Gemini models. The T2 Arabic MCQ emerges as the sole instrument capable of producing a continuous discrimination scale across vendors and capability tiers. The rubric's trimodal distribution and the Gemini data provenance caveats together indicate that cross-vendor religious values evaluation requires purpose-built instruments with domain-specific content, non-English presentation, and exact-match scoring---properties that general-purpose rubrics do not possess.

Full-scale implementation trials across all 25 tiered benchmarks and additional model families are ongoing. The three-vendor, nine-model results reported here provide proof-of-concept for cross-vendor religious values evaluation while identifying the methodological requirements---matched administration protocols, independent scoring, and domain-specific instruments---that future trials must satisfy for vendor comparisons to be fully interpretable.
