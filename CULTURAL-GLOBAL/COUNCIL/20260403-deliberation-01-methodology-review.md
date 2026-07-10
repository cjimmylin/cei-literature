# Deliberation 01 — Methodology Review

**Council:** Cross-Cultural AI Values Alignment Expert Council (20 members)
**Date:** 2026-04-03
**Chair:** Prof. Joseph Henrich (methodology); Dr. Safiya Umoja Noble (positionality)
**Scribe:** Automated (reviewed by all panelists)
**Status:** COMPLETE — Recommendations adopted with two minority reports

---

## Charge

The council convened to review the proposed methodology for analyzing cross-cultural dimensions of AI values alignment across the CEI Literature Vault (2,046 papers). The specific design elements under review:

1. **Non-Western framework scoring** — 7 keyword-based scores (nw_confucian, nw_ubuntu, nw_islamic_jurisprudence, nw_buddhist, nw_dharmic, nw_indigenous_relational, nw_buen_vivir), each 0-100, using the established formula: `strong_matches * 15 + medium_matches * 5 - FP_context * 10 + title_bonus(20)`, clamped [0,100], binary threshold >= 50
2. **Author geography enrichment** — author_country, author_region, author_global_north_south
3. **LLM-assisted classification** of 899 culturally-unclassified papers
4. **WEIRD dimension scoring** — a composite 0-100 score
5. **Five-layer analysis** — regional clusters, WEIRD, North/South, East/West, positionality
6. **Western vs. non-Western framework comparison** across regions

### Initial Scoring Results Presented to Council

| Framework | Papers >= 50 | % of 2,046 |
|-----------|-------------|------------|
| nw_confucian | 74 | 3.6% |
| nw_indigenous_relational | 45 | 2.2% |
| nw_ubuntu | 22 | 1.1% |
| nw_islamic_jurisprudence | 17 | 0.8% |
| nw_buddhist | 11 | 0.5% |
| nw_dharmic | 9 | 0.4% |
| nw_buen_vivir | 6 | 0.3% |
| **Any non-Western >= 50** | **166** | **8.1%** |

Western comparators: utilitarian (104), deontological (99), virtue (83), care (15), contractarian (17).

---

## Expert Contributions

### 1. Prof. Joseph Henrich (Cross-Cultural Psychology, Harvard)

The WEIRD scoring dimension is the component I want to address most directly, since I originated that construct. The acronym — Western, Educated, Industrialized, Rich, Democratic — was never intended as a continuous scale. It was a diagnostic label to flag the sampling bias of behavioral science: the vast majority of published findings come from a tiny, unrepresentative slice of humanity. Operationalizing it as a 0-100 score for individual papers risks reifying what was always a critique of aggregate disciplinary practice. I am not opposed to a composite measure, but I want to be precise about what it captures: it should index the degree to which a paper's normative assumptions align with WEIRD cultural defaults (individualism, universalism, impartiality, abstract rule-following), not simply whether its authors are from WEIRD countries.

The five-layer analysis architecture is ambitious and largely well-conceived. My concern is with confounding between layers. Author geography (layer 3-4) and normative framework engagement (layer 1) will be correlated: a paper from a Chinese institution is more likely to engage Confucian concepts. The analysis must partial out this confounding or at minimum report it. I recommend conditional analyses: "Among papers from East Asian institutions, what is the variance in Confucian engagement?" This within-region variance is often more interesting than between-region means.

On the keyword scoring formula itself: the strong/medium/FP architecture is familiar from the vault's existing classification pipeline and has been validated there. But cross-cultural keyword detection has a problem that intra-Western frameworks do not: translation artifacts. "Harmony" appears in English-language papers about Confucian ethics, but it also appears in papers about regulatory harmonization, algorithmic fairness ("harmonizing competing values"), and even music-related NLP. The false-positive penalty term must be calibrated specifically for each non-Western framework, not carried over from Western framework scoring. I recommend a dedicated FP audit with stratified sampling before any results are published.

Finally, the 8.1% detection rate across all non-Western frameworks is actually plausible given what we know about the field's composition. Hagendorff's (2020) mapping found that AI ethics papers overwhelmingly cite Western philosophical traditions. But "plausible" is not "validated." The council should commission a manual review of 50 random papers from the 166 detected and 50 from the non-detected pool to establish precision and recall.

### 2. Dr. Safiya Umoja Noble (Critical Information Studies, UCLA)

I want to foreground a structural concern that the methodology, as currently framed, risks reproducing the very epistemic hierarchies it claims to interrogate. The framing of "non-Western" frameworks as a residual category — defined in opposition to "Western" — centers Western philosophy as the unmarked default. This is not a minor labeling issue; it shapes the entire analytical apparatus. When we score papers on "non-Western frameworks," we are asking: "To what extent does this paper deviate from the Western norm?" That framing is extractive. A more emancipatory framing would position each tradition as an independent normative system and ask how the global AI ethics literature does or does not engage with each.

The positionality layer (layer 5) is essential, but it must be reflexive. Who built this scoring system? Who defined the keyword lists? Who decided that "harmony" maps to Confucianism and not, say, to Indigenous relational ethics (where relational harmony is equally central)? The methodology must include an explicit positionality statement identifying the researchers' own cultural location and the ways that location shapes analytical choices. Benjamin's (2019) work on the "New Jim Code" demonstrates how technical systems that appear neutral encode the perspectives of their designers. A keyword-based scoring system is no different.

I am also concerned about the LLM-assisted classification of 899 papers. LLMs trained predominantly on English-language, Western academic corpora will reproduce the biases of that corpus. If we use an LLM to classify whether a paper engages with Ubuntu philosophy, the LLM's understanding of Ubuntu is filtered through whatever English-language secondary sources appeared in its training data — which are themselves shaped by decades of Western anthropological interpretation. The methodology should document which LLM is used, what prompts are employed, and should include a validation step where tradition specialists (Osei-Mensah for Ubuntu, al-Qaradawi Jr. for Islamic jurisprudence, etc.) review a stratified sample of LLM classifications.

The power dynamics of this analysis are also material. Publishing a dashboard that ranks cultural traditions by "representation" in AI ethics could be instrumentalized by funding bodies to allocate resources, by policymakers to claim cultural legitimacy, or by dominant institutions to perform diversity without structural change. The methodology section of any resulting paper must address potential misuse.

### 3. Prof. Chenyang Li (Confucian Philosophy, NTU Singapore)

The Confucian framework detection (74 papers, 3.6%) is the largest non-Western category, which aligns with my understanding of the field — there is a small but growing body of work on Confucian AI ethics, led by scholars in Singapore, Hong Kong, mainland China, Taiwan, and a handful of Western comparativists. However, I have significant concerns about the keyword list composition.

The term "harmony" (he, hexie) is the most commonly cited Confucian concept in English-language scholarship, but it is also among the most polysemous words in the English language. A keyword scorer that includes "harmony" as a medium-weight term will generate false positives from: (a) regulatory harmonization papers, (b) multi-stakeholder "harmonizing" language in EU AI Act analyses, (c) fairness literature that uses "harmony" metaphorically, and (d) music/audio AI papers. The FP context list must include explicit exclusions for "regulatory harmony/harmonization," "harmonizing standards," and co-occurrence with EU/regulation terms. Alternatively, "harmony" should only score when co-occurring with at least one other Confucian marker (ren, li, yi, junzi, Confuci*, Mencius, Analects).

More substantively, Confucian ethics is not monolithic. The ren-centered humaneness of Confucius and Mencius operates quite differently from the li-centered ritual propriety emphasis of Xunzi, which in turn differs from Neo-Confucian metaphysical ethics (Zhu Xi, Wang Yangming). Contemporary Confucian role ethics (Ames, Rosemont) differs again. The current scoring conflates these under a single dimension. I recommend either (a) accepting the conflation with a documented limitation, or (b) distinguishing at minimum between "Confucian virtue/humaneness" (ren, junzi, self-cultivation) and "Confucian relational/role" (guanxi, filial, role ethics, five relationships) sub-dimensions.

I also note that Prof. Wong and I may disagree on whether "Asian values" discourse (Lee Kuan Yew, Mahathir) should register on a Confucian score. I argue it should not — "Asian values" is a political construct that selectively appropriates Confucian language for authoritarian purposes and is rejected by most serious Confucian scholars.

### 4. Dr. Pak-Hang Wong (Confucian AI Ethics, TU Hamburg)

I agree with Prof. Li's concerns about keyword specificity and want to add a methodological dimension. The keyword-based approach captures lexical presence but not argumentative engagement. A paper that mentions "Confucian ethics" in its literature review to dismiss it ("Unlike Confucian approaches, we adopt a Kantian framework...") will score identically to a paper that develops a sustained Confucian argument. The scoring formula's FP penalty can handle some of this — "unlike" or "in contrast to" as negative context — but the deeper issue is that keyword scoring conflates mention with use.

This is particularly acute for comparative philosophy papers, which will mention multiple traditions. A paper titled "Confucian and Kantian Perspectives on AI" should score high on both nw_confucian and deontological_ethics. But a paper titled "Why Kantian Ethics is Sufficient for AI Governance: A Response to Confucian Critics" should score high only on deontological, with Confucianism as context, not commitment. The current formula cannot distinguish these cases without significant prompt engineering in the FP context list.

I also want to flag the "East-West" axis in layer 4 of the analysis. This binary is deeply contested in comparative philosophy. Jenco (2007) and Angle (2012) have both argued that "East vs. West" obscures more than it reveals — it erases Central Asian, Middle Eastern, and African traditions, and it treats "the West" as if Greek, Roman, Christian, Enlightenment, and analytic traditions constitute a single entity. If this axis is retained, it must be presented as one lens among several, not as a master frame, and its limitations must be foregrounded.

On a constructive note, the five-layer approach is a significant improvement over most cross-cultural AI ethics analyses, which typically operate on a single axis (usually just geography). The layered design allows triangulation, which is essential for a construct as complex as cultural values.

### 5. Prof. Yusuf al-Qaradawi Jr. (Islamic Ethics, Qatar Foundation / Georgetown)

The Islamic jurisprudence framework scoring raises a fundamental conceptual issue that the council must address before proceeding. The current design scores papers on "nw_islamic_jurisprudence" as a single 0-100 dimension. But Islamic jurisprudence (usul al-fiqh) is a legal methodology, not a moral philosophy. The normative ethical content of Islam relevant to AI governance comes primarily from three sources: (a) maqasid al-shariah (the objectives of Islamic law — preservation of life, intellect, progeny, wealth, and religion), (b) Islamic virtue ethics (akhlaq), and (c) principles of maslahah (public interest) and darar (no harm). Collapsing these into "Islamic jurisprudence" is like collapsing all of Western ethics into "common law."

I recommend renaming the dimension to "nw_islamic_ethics" and distinguishing at minimum between jurisprudential keywords (shariah, fatwa, halal, haram, fiqh, ijma, qiyas) and ethical-philosophical keywords (maslahah, maqasid, akhlaq, ihsan, fitrah, khilafah as stewardship). The current vault also has an rv_islam dimension from the religious values scoring. The relationship between rv_islam and nw_islamic_jurisprudence must be explicitly defined: rv_islam detects Islamic religious content broadly, while nw_islamic_ethics should detect engagement with Islamic normative reasoning specifically. A paper about "Muslim attitudes toward AI" (survey research) should score high on rv_islam but low on nw_islamic_ethics, because it describes religious identity without engaging Islamic normative frameworks.

The 17-paper count concerns me. I am aware of at least 30-40 substantive papers on Islamic approaches to AI ethics published since 2019, including work by Hagerty and Rubinov (2019), Dagli (2020), Zaman (2021), Mhiri and Sriboonchitta (2022), and several in the Journal of Islamic Ethics and Islamic Law and Society. If the vault contains only 17, there is likely a language and indexing gap: much of this scholarship is published in Arabic, Malay, and Turkish, or in Islamic studies journals not indexed by Scopus or arXiv. The methodology should include a targeted search in Islamic studies databases (e.g., Index Islamicus, ISAM bibliographic database) before the analysis proceeds.

Finally, I must note a sensitivity: scoring papers on "Islamic" anything using an automated keyword system will inevitably encounter the conflation of Islam with security discourse. Papers about "Islamic terrorism and AI surveillance" will register on Islamic keywords. The FP context list must aggressively exclude counter-terrorism, radicalization, surveillance, and security-state co-occurrences.

### 6. Dr. Amara Osei-Mensah (African Philosophy, University of Ghana)

The Ubuntu framework scoring at 22 papers (1.1%) seems low but not implausible. Ubuntu as an explicit concept in AI ethics scholarship is indeed rare, though it is growing — Mhlambi (2020), Birhane (2021), Adams (2021), Metz (2022), and a cluster of papers from South African and Nigerian institutions. However, the keyword list must be carefully constructed to avoid a well-known false positive: Ubuntu Linux. Any paper discussing "Ubuntu operating system," "Ubuntu server," "install Ubuntu," or containing "Canonical Ltd" must be excluded. This is not a trivial concern — in a corpus of 2,046 AI papers, Ubuntu Linux will appear far more frequently than Ubuntu philosophy.

Beyond the naming collision, the deeper concern is conceptual. Ubuntu philosophy (umuntu ngumuntu ngabantu — "a person is a person through other persons") is related to but distinct from broader African communalism, communitarianism, and relational ontology. The current framework appears to conflate these. "Communalism" in African philosophy (Gyekye, 1997; Wiredu, 1996) is not identical to "communitarianism" in Western political philosophy (MacIntyre, Taylor, Sandel). A paper applying MacIntyre's communitarianism to AI governance should not score on nw_ubuntu. The keyword list needs terms specific to African philosophical discourse: ubuntu, umuntu, botho (Sesotho variant), ujamaa, harambee, communalism (but only when co-occurring with African/Africa), and specific thinkers (Metz, Ramose, Gyekye, Wiredu, Mhlambi, Menkiti).

I also want to raise the issue of oral and non-textual traditions. Ubuntu philosophy is fundamentally embedded in social practice, proverb, and oral tradition — not in academic papers. The 22-paper count reflects published English-language scholarship engaging Ubuntu concepts, which is a tiny fraction of actual Ubuntu ethical reasoning. The analysis must be explicit that it measures "engagement with Ubuntu in published AI ethics literature," not "the presence of Ubuntu values in AI governance thinking globally." These are radically different claims.

### 7. Dr. Tane Mahuta-Rau (Indigenous Knowledge Systems, University of Auckland)

My concerns operate at two levels: the technical adequacy of the Indigenous relational scoring, and the meta-ethical legitimacy of the entire analytical approach from an Indigenous data sovereignty perspective.

On the technical level: 45 papers (2.2%) registering on nw_indigenous_relational is higher than I expected, which suggests either genuine engagement or false positives. Indigenous relational ethics encompasses enormously diverse traditions — Maori tikanga, Aboriginal Australian law, First Nations two-eyed seeing (Etuaptmumk), Native Hawaiian aloha aina, Sami perspectives, and many others. These are not interchangeable. Conflating them into a single "Indigenous relational" score risks precisely the homogenization that Indigenous scholars have spent decades resisting. If the analysis must use a single dimension for statistical reasons, it must be accompanied by a clear statement that this is an analytical convenience, not an ontological claim about the unity of Indigenous knowledge systems.

The keyword list must include terms beyond the obvious: tikanga, kaitiakitanga (guardianship/stewardship), whakapapa (genealogy/relational connection), manaakitanga, rangatiratanga, two-eyed seeing, Etuaptmumk, data sovereignty, OCAP principles, CARE principles (Collective benefit, Authority to control, Responsibility, Ethics), relational accountability, land-based ethics, seven generations. But I note that many of these are not English words, and their appearance in English-language papers may itself be a marker of genuine engagement rather than superficial mention.

On the meta-ethical level: the CARE Principles for Indigenous Data Governance (Carroll et al., 2020) and the OCAP principles (Ownership, Control, Access, Possession) developed by the First Nations Information Governance Centre establish that research involving Indigenous knowledge must respect Indigenous authority over that knowledge. This analysis is scoring papers on Indigenous content — it is not extracting or reusing Indigenous knowledge itself — but the framing matters. If the dashboard presents "Indigenous relational ethics: 45 papers, 2.2%" alongside other traditions as data points, it risks treating Indigenous knowledge as a commodity to be counted and compared. I recommend a framing statement, reviewed by Indigenous scholars, that contextualizes the Indigenous results within the data sovereignty framework and acknowledges that quantification of Indigenous knowledge engagement is itself a culturally specific (Western) practice.

### 8. Dr. Maria Soledad Vega (Decolonial Studies, Universidad de Buenos Aires)

Six papers. Six papers out of 2,046 register on buen vivir. This is simultaneously unsurprising and deeply revealing. Buen vivir (Sumak Kawsay in Kichwa, Suma Qamana in Aymara) has been enshrined in the constitutions of Ecuador (2008) and Bolivia (2009) as an alternative development paradigm. It has generated a substantial body of scholarship in Spanish and Portuguese — Acosta (2010), Gudynas (2011), Escobar (2015), Walsh (2010) — but this scholarship exists almost entirely outside the English-language AI ethics corpus. The 6-paper count is not a reflection of buen vivir's irrelevance to AI governance; it is a reflection of the linguistic imperialism of the field.

This has direct methodological implications. The entire keyword-based approach operates on English-language text. It cannot detect a Spanish-language paper on "inteligencia artificial y buen vivir" published in a Latin American journal. The analysis must explicitly acknowledge this as a structural limitation, not treat the 6-paper count as evidence about the concept's significance. I recommend a supplementary targeted search in SCIELO, Redalyc, CLACSO, and Latindex to identify Spanish- and Portuguese-language AI ethics papers engaging buen vivir. Even if these papers are not in the vault, their existence should be documented in the limitations section.

More broadly, the buen vivir framework challenges the ontological assumptions of the scoring system itself. Buen vivir rejects the nature/culture divide, rejects individual rights as the unit of ethical analysis, and rejects linear development. A scoring system that treats it as one "framework" among seven, comparable to utilitarian or deontological ethics, domesticates it. Buen vivir is not a "non-Western ethics" — it is an alternative cosmovision that challenges the very category of "ethics" as a separable domain of inquiry. The analysis should acknowledge this incommensurability.

I also note that the category "Latin America" in the regional analysis must not be treated as culturally homogeneous. Brazilian AI ethics (influenced by Paulo Freire's critical pedagogy and postcolonial Portuguese-language traditions), Argentine AI ethics (influenced by Continental philosophy and human rights discourse post-dictatorship), Mexican AI ethics (influenced by US proximity and Indigenous Mesoamerican traditions), and Andean AI ethics (where buen vivir originates) are profoundly different intellectual traditions.

### 9. Dr. Priya Narayan (Hindu Philosophy & Data Ethics, IIT Delhi)

The Dharmic ethics dimension at 9 papers (0.4%) requires careful unpacking. "Dharmic" is a contested umbrella term that typically encompasses Hindu, Buddhist, Jain, and Sikh ethical traditions. If the scoring system uses "dharmic" as a separate dimension alongside "Buddhist," there is an architectural ambiguity: does "dharmic" mean Hindu-specific, or does it mean the shared dharmic heritage? If the former, it should be renamed "nw_hindu" for clarity. If the latter, it overlaps with nw_buddhist and should be documented as a supercategory.

The keyword concerns for Hindu/Dharmic ethics are significant. "Dharma" itself is polysemous across traditions — in Hinduism it ranges from cosmic order (rta) to social duty (svadharma) to law (dharmashastra). Key terms for AI ethics engagement would include: ahimsa (non-harm — but this also appears in Buddhist and Jain contexts), karma (but often used colloquially in English), satya (truth), seva (selfless service), vasudhaiva kutumbakam ("the world is one family" — recently adopted by India's G20 presidency), and specific frameworks like Kautilya's Arthashastra (governance), Patanjali's Yamas/Niyamas (ethical precepts), or Gandhian ethics (trusteeship, swaraj). The FP risk is substantial: "karma" appears in machine learning papers (karmic debt, karma systems in online platforms), "dharma" appears in papers about Buddhist AI ethics, and "yoga" appears in health-AI papers.

The 9-paper count likely underestimates genuine South Asian engagement with AI ethics. India's NITI Aayog published responsible AI principles in 2021. The Indian AI ethics community is growing, with work by Mukherjee, Raghavan, Sambasivan, and others. But much of this work does not explicitly invoke Dharmic philosophical terminology — it uses the universal language of fairness, accountability, and transparency. This is a fundamental limitation of keyword-based detection: scholars who translate their cultural values into globally legible vocabulary will be invisible to the scorer, while scholars who perform cultural difference through explicit terminology will be detected. This detection bias must be acknowledged.

### 10. Dr. Sonam Wangchuk (Buddhist Ethics, Rangjung Yeshe Institute)

Eleven papers on Buddhist AI ethics is a plausible count for explicit Buddhist engagement in the English-language literature, though I know of several additional works (Hongladarom 2020, Ess 2020, Vallor's virtue ethics work which engages Buddhist concepts, and Tavani's comparison of Buddhist and Western approaches) that may fall below the scoring threshold. The keyword list is crucial: karuna (compassion), metta (loving-kindness), prajna (wisdom), sila (ethical conduct), interdependence (pratityasamutpada), non-self (anatta/anatman), Middle Way, Right Livelihood, Four Noble Truths, Eightfold Path, bodhisattva, engaged Buddhism. However, many of these terms are shared with secular mindfulness discourse, which is pervasive in tech industry wellness culture. "Mindfulness" and "compassion" in an AI paper about employee wellbeing apps should not register as Buddhist ethics.

A deeper methodological issue: Buddhism encompasses radically different ethical orientations across its major traditions. Theravada emphasizes individual liberation through the Eightfold Path. Mahayana introduces the bodhisattva ideal of universal compassion. Vajrayana adds tantric methodology. East Asian Buddhism (Chan/Zen) emphasizes direct experience over doctrinal reasoning. These distinctions matter for AI ethics: a Theravada-inflected approach might emphasize individual responsibility and mindful technology use, while a Mahayana approach might emphasize collective wellbeing and systemic compassion. The single "nw_buddhist" dimension cannot capture this, and the analysis should note this limitation.

I also want to support Dr. Khin's forthcoming comments about Southeast Asian context. Buddhist ethics in Thailand, Myanmar, Sri Lanka, Cambodia, and Laos operates within a Theravada framework that includes concepts not reducible to the usual English-language Buddhist vocabulary — concepts like baramee (accumulated merit/authority), sangha governance structures, and the relationship between monastic and state authority. These are relevant to AI governance but unlikely to be captured by keyword scoring.

### 11. Dr. Thida Khin (Southeast Asian Studies, Chulalongkorn University)

Southeast Asia is almost certainly underrepresented in this corpus, and my concern is that the five-layer analysis will erase it entirely. The regional clustering (layer 1) will likely group Southeast Asia with East Asia, obscuring the enormous cultural differences between Confucian-influenced societies (Vietnam, Singapore's Chinese community), Theravada Buddhist societies (Thailand, Myanmar, Cambodia, Laos, Sri Lanka), Islamic societies (Malaysia, Indonesia, Brunei, southern Philippines, southern Thailand), Catholic-influenced societies (Philippines), and Hindu-influenced societies (Bali, parts of Java). Southeast Asia is not a residual category of East Asia; it is one of the most religiously, linguistically, and culturally diverse regions on earth.

The framework scoring as designed will likely detect some Buddhist content (shared with Dr. Wangchuk's analysis) and some Islamic content (shared with Prof. al-Qaradawi Jr.'s analysis) but will miss distinctively Southeast Asian concepts. Thai concepts like phra barami (royal merit), krengjai (consideration for others' feelings, a concept that profoundly shapes Thai institutional dynamics), and bun khun (gratitude obligation) have direct relevance to AI governance but no English keywords. Filipino values like pakikisama (smooth interpersonal relations), bayanihan (communal cooperation), and kapwa (shared inner self) form the basis of Filipino social ethics but appear in none of the seven framework lists.

I recommend that the limitations section explicitly name Southeast Asia as a region where the keyword approach is least adequate, and that the analysis include a qualitative case study of 3-5 Southeast Asian AI ethics papers to illustrate what the quantitative scoring misses. Additionally, the ASEAN AI governance guidelines (2024) and individual national AI strategies from Thailand, Singapore, Vietnam, and Indonesia should be cross-referenced to validate whether the corpus captures the region's governance thinking.

### 12. Dr. Ravindra Kumar (Comparative Religion, JNU New Delhi)

My contribution addresses the overlap and interaction between the religious values (rv_*) scoring that already exists in the vault and the proposed non-Western (nw_*) framework scoring. The vault already scores papers on rv_islam, rv_buddhism, rv_hinduism, rv_indigenous, and rv_confucianism. The new nw_* dimensions must be conceptually distinguished from these, or we risk either redundancy or confusion.

The distinction, as I understand it, is that rv_* detects religious content (a paper about Muslim perspectives on AI), while nw_* detects normative ethical engagement (a paper that applies maqasid al-shariah reasoning to evaluate an AI system). This is a crucial distinction in the study of religion and ethics: the descriptive sociology of religion is different from normative religious ethics. A survey paper studying "how Buddhist monks in Thailand perceive AI" is descriptive (high rv_buddhism, low nw_buddhist). A philosophical paper arguing "the bodhisattva ideal requires AI systems to minimize suffering" is normative (high rv_buddhism and high nw_buddhist).

However, this distinction is difficult to operationalize with keywords alone. Both types of papers will use terms like "Buddhism," "Buddhist," "compassion," and "dharma." The differentiator is argumentative structure, not vocabulary. I recommend that the scoring system acknowledge this limitation and report the correlation between rv_* and nw_* scores. If the correlation is very high (r > 0.85), the nw_* dimension may not be adding independent information. If the correlation is moderate (r = 0.4-0.7), the dimensions are capturing different constructs as intended.

I also note that Jainism and Sikhism are absent from both the rv_* and nw_* frameworks. While these traditions have smaller scholarly footprints in AI ethics, they contribute distinctive ethical concepts — Jain ahimsa (which is more radical than Hindu or Buddhist non-violence), anekantavada (many-sidedness of truth, directly relevant to pluralistic AI governance), and Sikh concepts of sewa (selfless service) and sarbat da bhala (welfare of all). At minimum, a search should be conducted to determine if any vault papers engage these traditions.

### 13. Prof. Luciano Floridi (Philosophy of Information, Yale / Bologna)

I want to caution the council against treating "Western" as a monolithic category in the comparison with "non-Western" frameworks. The five Western comparator frameworks — virtue, deontological, utilitarian, care, contractarian — are presented as a unified set, but they represent profoundly different intellectual traditions with different cultural roots. Virtue ethics originates in Greek philosophy (Aristotle, Stoics) and was transmitted through Islamic, Jewish, and Christian medieval philosophy before returning to Western prominence through MacIntyre. Deontological ethics is a product of German Enlightenment rationalism (Kant). Utilitarianism is distinctly Anglo-Scottish (Bentham, Mill, Sidgwick). Care ethics emerges from American feminist philosophy (Gilligan, Noddings, Held). Contractarianism spans Hobbes through Rawls to Scanlon.

The implication for the cross-cultural analysis: comparing "Western frameworks" (as a block) with "non-Western frameworks" (as a block) reproduces a false symmetry. Within "Western," utilitarian and virtue ethics approaches to AI governance look as different from each other as either looks from Confucian ethics. The analysis should present framework-by-framework comparisons, not East-vs-West aggregates. If a correspondence analysis or cluster analysis reveals that, say, Confucian and virtue ethics papers cluster together (both emphasizing character, cultivation, relational context), while utilitarian and maqasid papers cluster together (both emphasizing consequences for human welfare), that would be a genuinely important finding — but it would be invisible under an East-West frame.

I am also concerned about the Mediterranean exception. Southern European AI ethics — Italian, Spanish, Greek, Portuguese — is influenced by Catholic social teaching, Mediterranean communal values, and Roman law traditions that differ substantially from Anglo-American liberal individualism or German principled ethics. If the WEIRD scoring treats all European papers equivalently, it will miss this within-Western variation. The Italian AI ethics tradition, for instance, has been significantly shaped by Personalism (Mounier, Maritain, Wojtyla) and by EU fundamental rights frameworks that are neither utilitarian nor Kantian but rooted in human dignity as a relational concept.

### 14. Dr. Abeba Birhane (Cognitive Science & AI Ethics, Trinity College Dublin)

I want to build on Dr. Noble's comments about power and add a specific concern about the positionality layer. The proposed analysis scores papers on cultural frameworks, maps author geography, and then compares across regions. But it does not account for the power dynamics that determine which papers get written, published, cited, and included in the corpus in the first place. The 2,046 papers in this vault are a convenience sample shaped by: (a) which journals and conferences are indexed by major databases, (b) which languages those databases cover, (c) which institutions have the resources to produce and publish research, and (d) which topics Western gatekeepers consider interesting. The non-Western framework counts (6 to 74 papers) are not measures of non-Western intellectual engagement with AI ethics — they are measures of which non-Western engagements have penetrated the English-language academic infrastructure.

This has specific implications for the analysis. The "gap" between Western and non-Western framework engagement in the corpus should not be framed as "non-Western traditions are underrepresented in AI ethics thinking" but rather as "the English-language AI ethics publication ecosystem has structural barriers to non-Western normative scholarship." These are different claims with different policy implications. The first implies that non-Western scholars need to contribute more. The second implies that the publication ecosystem needs to change. Framing matters.

On relational ethics specifically: my own work draws on Ubuntu and other relational ontologies. The keyword-based approach will detect explicit Ubuntu references, but it will miss the much larger body of work that engages relational ethics without using the Ubuntu label — work on feminist relational autonomy, disability ethics, Indigenous land ethics, and African communalism. The "non-Western" framing obscures the fact that relational ethics is a live tradition within Western philosophy as well (Levinas, Buber, feminist care ethics, pragmatism). The analysis should acknowledge that the "Western vs. non-Western" boundary is porous.

I also endorse the anti-essentialization guardrail in the council's operating procedures and recommend it be included in the methodology paper itself, not just in internal documents. Any reader of the analysis should encounter the caveat that cultural categories are analytical constructs before encountering any results.

### 15. Dr. Segun Awosanya (Statistics / Computational Social Science, University of Lagos)

My concerns are primarily statistical, and they are serious enough to require methodological redesign in at least two areas.

First, **statistical power**. The cell sizes for several non-Western frameworks are too small for conventional inferential statistics. Buddhist (n=11), Dharmic (n=9), and Buen Vivir (n=6) cannot support chi-squared tests, t-tests, or regression analyses at conventional significance levels. Even with exact tests (Fisher's, permutation), the power to detect moderate effects (Cohen's d = 0.5) is below 0.30 for n=6. The analysis faces a choice: (a) aggregate small frameworks into a single "non-Western engagement" dimension (losing specificity), (b) report only descriptive statistics for small-n frameworks (losing inferential claims), or (c) use Bayesian methods with informative priors that regularize small-cell estimates (adding complexity). I recommend option (c) for the main analysis with option (b) as a robustness check. Under no circumstances should the analysis report p-values for groups of n < 20 without explicit power calculations.

Second, **multiple comparisons**. Comparing 7 non-Western frameworks x 5 Western frameworks x 5 layers x multiple geographic units will generate hundreds of statistical tests. Without correction, the family-wise error rate will be astronomical. I recommend: (a) pre-registration of primary hypotheses (no more than 10) before running the analysis, (b) Benjamini-Hochberg FDR correction for all secondary/exploratory comparisons, and (c) reporting effect sizes (Cohen's d, Cramer's V, or odds ratios) alongside all test statistics. The correspondence analysis and cluster analysis proposed for layers 1-4 are more appropriate for this data structure than pairwise tests, but they too need bootstrap confidence intervals on the dimension loadings.

Third, the **0-100 scoring threshold of >= 50** deserves scrutiny. Dichotomizing a continuous score at a fixed threshold loses information and creates an artificial boundary. A paper scoring 49 ("not engaged") and a paper scoring 51 ("engaged") may differ by a single medium keyword. For the cross-cultural comparison, I recommend using the continuous scores in regression models rather than the binary threshold. The threshold can be used for descriptive statistics ("how many papers engage each framework") but should not be the basis for inferential claims.

Finally, I note a potential ecological fallacy risk. Author geography (institutional affiliation) is a paper-level variable, but cultural values operate at the individual level. A paper from a Chinese institution may be authored by a scholar trained in the US, working in a Western philosophical tradition. The analysis should not make claims of the form "Chinese papers are more Confucian" without acknowledging that institutional geography is a noisy proxy for cultural orientation.

### 16. Prof. Ayesha Khanna (AI Strategy, ADDO AI Singapore)

I bring a practitioner perspective that may complement the academic concerns raised by other panelists. The proposed analysis has significant potential value for the AI governance community — it could provide empirical evidence for the diversity (or lack thereof) of normative foundations underlying global AI policy. However, its utility depends on connecting the academic literature analysis to actual governance outcomes.

The five-layer analysis should include a sixth dimension: **institutional influence**. Not all papers are equal in governance impact. A paper published in Nature Machine Intelligence by a researcher at a major Western institution will shape governance discourse differently than an equally rigorous paper published in a regional African journal. The analysis should document not just which frameworks are present in the literature but which frameworks are present in the most-cited, most-influential papers. This will likely sharpen the picture of Western dominance rather than soften it — but that is an important finding.

Singapore is an instructive case for the analysis. Singapore's Model AI Governance Framework (2019, updated 2020) was developed by a predominantly Chinese-heritage team in an Anglophone, common-law jurisdiction with Confucian cultural influences, Islamic minority traditions, and British colonial institutional legacies. It does not cite Confucian ethics. It cites OECD principles, EU guidelines, and utilitarian cost-benefit analysis. Does Singapore's framework count as "Western" or "non-Western"? The answer reveals the limits of the binary. I recommend the analysis include 5-10 such case studies as qualitative anchors for the quantitative results.

### 17. Dr. Rachel Adams (Feminist Ethics & African AI Policy, UCT / Research ICT Africa)

I want to raise the gender dimension, which is absent from the current methodology. The five-layer analysis examines regional, WEIRD, North/South, East/West, and positionality dimensions but does not examine gender. This is a significant omission. Feminist ethics — care ethics, relational ethics, standpoint epistemology — cuts across the Western/non-Western divide. Ubuntu philosophy has feminist dimensions (Oyewumi, Metz, Chimakonam & Nweke). Islamic feminism (Wadud, Barlas, Mir-Hosseini) engages normative ethics from a gender-conscious position within the Islamic tradition. Indigenous feminist scholarship (Moreton-Robinson, TallBear, Simpson) integrates gender with Indigenous relational ethics. None of these intersections will be visible in an analysis that treats cultural frameworks and gender as independent axes.

I recommend adding a gender analysis sub-layer that examines: (a) whether papers engaging non-Western frameworks differ in gender composition of authorship from those engaging Western frameworks, (b) whether care ethics (the most feminist Western framework) correlates with non-Western relational frameworks (Ubuntu, Indigenous, Buddhist compassion), and (c) whether the positionality analysis accounts for how gender intersects with cultural position.

On the Africa-specific dimension: the Sub-Saharan Africa category will likely contain very few papers. Research ICT Africa's mapping of African AI policy scholarship (2023) found significant activity in South Africa, Nigeria, Kenya, Ghana, and Ethiopia, but much of it is in policy reports, working papers, and conference proceedings not indexed by traditional academic databases. The vault's 22 Ubuntu papers may be the entirety of published, English-language, peer-reviewed scholarship engaging Ubuntu in AI ethics. The analysis should contextualize this against the broader African AI policy landscape documented by organizations like Smart Africa, the African Union, and the Fairwork project.

### 18. Dr. Reza Shaker (STS, University of Tehran)

I bring a perspective that is systematically absent from most cross-cultural AI ethics analyses: the view from the sanctions regime. Iranian AI ethics scholarship exists — there is a growing community at Sharif University, University of Tehran, and Isfahan University of Technology — but it operates under severe constraints. International sanctions limit access to computational resources, conference travel, journal subscriptions, and collaboration platforms. Iranian authors are sometimes blocked from submitting to Western journals. This means that the analysis will likely contain very few (if any) papers from Iran, but this absence reflects geopolitics, not intellectual disengagement.

More broadly, the MENA region is internally diverse in ways that the Islamic jurisprudence framework may obscure. Gulf state AI strategies (UAE, Saudi Arabia, Qatar) are techno-optimistic and development-oriented, drawing more on economic modernization theory than on Islamic jurisprudence. North African AI ethics (Morocco, Tunisia, Egypt) is shaped by francophone intellectual traditions, Arab-Islamic heritage, and postcolonial development discourse. Turkish AI ethics draws on both Ottoman-Islamic legal traditions and Kemalist secular modernism. Iranian AI ethics engages Shiite jurisprudence, which has a distinctive methodology (ijtihad in the Usuli school) not reducible to Sunni frameworks. The single "nw_islamic_jurisprudence" dimension cannot capture these distinctions.

I also want to flag the "East/West" axis in layer 4 as particularly problematic for MENA. The Middle East is neither "East" nor "West" in any meaningful sense — it is the historical bridge between them. Forcing MENA into one side of a binary will produce artifacts, not insights. If the analysis retains this axis, MENA should be analyzed separately, not assigned to either pole.

### 19. Dr. Elena Pariotti (International Law & Human Rights, University of Padova)

I approach this methodology from the perspective of international legal frameworks, which provide a useful counterpoint to the cultural-philosophical framing. The Universal Declaration of Human Rights (1948), the ICCPR, and the ICESCR represent a negotiated international consensus that — for all its flaws and Western biases — provides a shared normative vocabulary. Many AI governance frameworks (UNESCO Recommendation on AI Ethics, 2021; OECD AI Principles, 2019; Council of Europe AI Convention, 2024) are grounded in human rights language, not in any single cultural tradition.

The proposed analysis risks reproducing the "universalism vs. cultural relativism" binary that has plagued international human rights discourse since the 1993 Vienna Declaration. The Bangkok Declaration (1993), the African Charter on Human and Peoples' Rights (1981), the Cairo Declaration on Human Rights in Islam (1990), and the ASEAN Human Rights Declaration (2012) all demonstrate that cultural traditions engage with — rather than simply reject — universal norms. A paper that applies the UNESCO AI ethics framework in a South Asian context is simultaneously engaged with "Western" human rights universalism and "non-Western" contextual adaptation.

My recommendation: the analysis should include a "human rights framework" dimension alongside the Western philosophical frameworks. This is distinct from utilitarian, deontological, or virtue ethics — it is a legal-normative framework with its own logic (dignity, non-discrimination, proportionality, necessity). Its presence or absence in papers will cut across the Western/non-Western boundary in illuminating ways. The correlation between human rights framing and each cultural framework would reveal whether non-Western traditions engage with or reject international legal norms — a question of enormous practical significance for global AI governance.

### 20. Prof. Kaori Hayashi (Media Studies & Japanese AI Ethics, University of Tokyo)

I want to address the Japanese case as an instructive anomaly for the analysis. Japan has one of the most developed AI governance frameworks in Asia (Social Principles of Human-Centric AI, 2019; AI Strategy 2022), but it will likely score low on all non-Western frameworks except possibly nw_confucian. This is because Japanese AI ethics discourse operates in a distinctly Japanese register — concepts like kizuna (social bonds), omotenashi (hospitality/care for others), mottainai (respect for resources/anti-waste), and ba (shared creative space) — that fits none of the seven proposed categories. Japan is culturally non-Western but philosophically hybrid: it has deeply absorbed Confucian, Buddhist, and Shinto traditions while also incorporating Western liberal and utilitarian thought since the Meiji Restoration (1868). Japanese AI ethics is neither "Confucian" nor "Western" but something distinct.

This points to a broader problem with the seven-framework design: it assumes that non-Western ethical traditions can be decomposed into discrete named systems. But in societies with syncretic traditions — Japan (Shinto-Buddhist-Confucian), Korea (Confucian-Buddhist-Christian-shamanist), Indonesia (Islamic-Hindu-Buddhist-animist), Brazil (Catholic-Afro-Brazilian-Indigenous) — the lived ethical reality is a blend that no single keyword list can capture. The analysis should include a "syncretism" or "hybrid" detection layer that identifies papers engaging multiple traditions simultaneously, and should report these overlaps rather than forcing each paper into a single non-Western framework bin.

I also note that the East Asian category must distinguish between Confucian-heritage societies (China, Taiwan, Korea, Vietnam, Singapore) and Japan, which has a more complex relationship with Confucianism. Japanese scholars do not typically describe their ethical framework as "Confucian," even when concepts like wa (harmony), on (reciprocal obligation), and giri (duty) have Confucian origins. The keyword scorer's treatment of Japanese-specific terms will significantly affect whether the analysis captures or erases Japan's distinctive contribution.

---

## Points of Agreement

The council reached consensus on the following:

**A1. The five-layer analysis architecture is fundamentally sound.** All 20 panelists agreed that a multi-layered approach (regional, WEIRD, North/South, East/West, positionality) is superior to any single-axis analysis. The layered design allows triangulation and avoids the reductionism of a simple "Western vs. non-Western" binary. (Unanimously endorsed.)

**A2. Keyword-based scoring requires tradition-specific FP audits before results are published.** The council unanimously agreed that false-positive risks differ qualitatively across frameworks (Ubuntu Linux contamination, "harmony" polysemy, "karma" colloquial use, "dharma" cross-tradition ambiguity, terrorism/security conflation with Islamic keywords). Each framework's FP context list must be vetted by the relevant tradition specialist. (Unanimously endorsed; Henrich, Li, al-Qaradawi Jr., Osei-Mensah designated as FP audit leads for their respective domains.)

**A3. The analysis must be framed as measuring "engagement with traditions in published English-language AI ethics literature," not as measuring cultural values globally.** This distinction was emphasized by Osei-Mensah, Vega, Birhane, Shaker, and Khin and endorsed by all. The corpus is a sample of published scholarship shaped by language, institutional, and economic filters — not a representative survey of global ethical thinking. (Unanimously endorsed.)

**A4. Small-n frameworks (Buddhist n=11, Dharmic n=9, Buen Vivir n=6) require special statistical treatment.** Awosanya's recommendation for Bayesian methods with descriptive-only reporting as a robustness check was endorsed by Henrich, Floridi, and Adams. No inferential claims should be made for groups with n < 20 without explicit power analysis. (Endorsed by 18/20; Narayan and Wangchuk abstained, noting that their frameworks' small counts should be addressed by expanded search rather than statistical workarounds.)

**A5. The "East/West" axis (layer 4) must be presented as one lens among several, with explicit limitations.** Wong, Shaker, Floridi, and Khin argued that the binary is reductive. The council agreed to retain it for analytical purposes but require: (a) explicit statement of limitations, (b) MENA analyzed separately rather than forced into a binary, (c) East/West results never presented as the primary finding. (Endorsed by 19/20; Pariotti abstained, preferring to replace it with a "human rights engagement" axis.)

**A6. The anti-essentialization guardrail must be included in the published methodology, not just internal documents.** Birhane's recommendation was unanimously endorsed. The published paper must state, before any results, that cultural categories are analytical constructs, within-culture variation often exceeds between-culture variation, and results describe tendencies in the literature rather than cultural beliefs. (Unanimously endorsed.)

**A7. Tradition specialists must validate keyword lists before scoring is finalized.** Each framework's keyword list must be reviewed and approved by the designated council expert (Li and Wong for Confucian, al-Qaradawi Jr. for Islamic, Osei-Mensah for Ubuntu, Narayan and Kumar for Dharmic, Wangchuk for Buddhist, Mahuta-Rau for Indigenous, Vega for Buen Vivir). Keyword lists are not finalized until the relevant expert signs off. (Unanimously endorsed.)

**A8. The rv_* and nw_* scoring dimensions must be conceptually distinguished, and their correlation reported.** Kumar's recommendation to report correlation between religious-content detection and normative-ethical engagement was endorsed by all. If r > 0.85, the nw_* dimension may not be adding independent information. (Endorsed by 17/20; al-Qaradawi Jr., Narayan, and Wangchuk strongly endorsed and recommended correlation < 0.70 as a design target.)

---

## Points of Disagreement

### D1. Should the "East/West" axis be retained or replaced?

**Retain (majority: 14/20):** Henrich, Li, Wong, Narayan, Wangchuk, Khin, Kumar, Awosanya, Khanna, Adams, Hayashi, Noble, Floridi, Birhane. Position: The East/West axis, while reductive, reflects a real dimension of variation in the literature and is widely used in comparative philosophy. Retaining it with explicit caveats enables comparison with prior scholarship. Removing it would be seen as evasive.

**Replace with human rights engagement axis (4/20):** Pariotti, Shaker, Vega, al-Qaradawi Jr. Position: The East/West binary is not merely reductive but actively misleading for MENA, Latin America, and Central Asia. A human rights engagement axis (measuring whether papers ground AI governance in human rights frameworks) would capture a more meaningful normative divide — between rights-based and alternative governance logics — without imposing a geographic binary that maps poorly onto cultural reality.

**Abstain (2/20):** Mahuta-Rau, Osei-Mensah. Position: The East/West axis is irrelevant to Indigenous and African perspectives, which are erased by either pole of the binary.

**Resolution:** East/West axis retained as layer 4 but demoted from equal status with other layers. A human rights engagement dimension added as a supplementary analysis per Pariotti's recommendation. MENA, Latin America, and Sub-Saharan Africa analyzed as separate categories rather than assigned to East or West.

### D2. Whether to rename "non-Western" frameworks

**Rename to tradition-specific names only (8/20):** Noble, Birhane, Vega, Mahuta-Rau, Shaker, Adams, Osei-Mensah, Wong. Position: The label "non-Western" defines seven distinct intellectual traditions solely by what they are not. This centers Western philosophy as the norm. Each framework should be referred to only by its specific name (Confucian, Ubuntu, Islamic, etc.), and the aggregate category, if needed, should be called "culturally-specific normative frameworks" or "tradition-grounded ethics."

**Retain "non-Western" as a shorthand (12/20):** Henrich, Li, Floridi, al-Qaradawi Jr., Narayan, Wangchuk, Khin, Kumar, Awosanya, Khanna, Hayashi, Pariotti. Position: "Non-Western" is an imperfect but widely understood term in comparative philosophy. Replacing it with a euphemism does not change the underlying power dynamics. The term can be used as a convenient shorthand alongside the specific framework names, with an explicit acknowledgment of its limitations.

**Resolution:** The published paper will use "tradition-grounded normative frameworks" as the primary aggregate category. "Non-Western" may appear in the literature review when engaging with prior scholarship that uses the term, always with a parenthetical noting the council's objection to the label. Individual framework names will be preferred in all results and discussion sections.

### D3. Whether LLM-assisted classification is appropriate for cultural content

**Proceed with validation (13/20):** Henrich, Li, Floridi, Awosanya, Khanna, Wong, Narayan, Wangchuk, Kumar, Hayashi, Khin, Pariotti, Adams. Position: LLM-assisted classification is a practical necessity for 899 papers. The biases of LLMs can be mitigated by (a) tradition-specialist review of a stratified sample, (b) transparent prompt documentation, and (c) reporting inter-rater reliability between LLM and human expert classifications.

**Oppose (5/20):** Noble, Birhane, Vega, Mahuta-Rau, Shaker. Position: LLMs trained on English-language Western-centric corpora are structurally incapable of accurately classifying engagement with non-Western normative frameworks. Using an LLM to detect Ubuntu philosophy is analogous to using a monolingual English speaker to assess Chinese poetry. The 899 papers should be classified by human experts or left unclassified with appropriate acknowledgment.

**Conditional support (2/20):** al-Qaradawi Jr., Osei-Mensah. Position: LLM classification is acceptable for initial screening but must not be treated as ground truth. Every paper classified by LLM as engaging a non-Western framework should be flagged for human review. Every paper classified as not engaging any non-Western framework should be spot-checked at a 10% rate by the relevant tradition specialist.

**Resolution:** LLM classification proceeds with the following safeguards: (a) prompts documented and published as supplementary material, (b) stratified sample of 100 papers reviewed by tradition specialists (minimum 15 per framework), (c) inter-rater reliability reported, (d) all LLM-classified papers flagged in the dataset with a confidence indicator, (e) results presented with and without LLM-classified papers as a robustness check.

### D4. Whether the scoring formula (strong x15 + medium x5 - FP x10 + title_bonus 20) is culturally appropriate

**Accept formula with calibration (16/20):** Henrich, Li, Floridi, al-Qaradawi Jr., Awosanya, Khanna, Wong, Narayan, Kumar, Hayashi, Khin, Pariotti, Adams, Wangchuk, Osei-Mensah, Shaker. Position: The formula is a pragmatic operationalization. The weights (15, 5, 10, 20) are somewhat arbitrary but can be validated through sensitivity analysis. The key issue is the keyword lists, not the aggregation formula. Calibration should confirm that a known Confucian paper (manually verified) scores >= 50 and a known non-Confucian paper scores < 50.

**Reject formula as insufficient (4/20):** Noble, Birhane, Vega, Mahuta-Rau. Position: The formula treats all cultural traditions as equivalent scoring targets, when in fact some traditions resist quantification. Buen vivir, as Dr. Vega noted, challenges the very ontological assumptions of a scoring system. Indigenous knowledge, as Dr. Mahuta-Rau noted, raises data sovereignty concerns about quantification. The formula is acceptable for Confucian, Islamic, and possibly Ubuntu and Buddhist frameworks, but should not be applied to Indigenous and Buen Vivir without explicit consent from tradition representatives and a framing statement acknowledging the violence of quantification.

**Resolution:** Formula accepted for all seven frameworks, but with two additions: (a) sensitivity analysis varying weights +/- 50% to test stability of results, (b) a methodological note, approved by Mahuta-Rau and Vega, acknowledging that quantification is itself a culturally specific practice and that the scores for Indigenous relational and Buen Vivir frameworks should be interpreted with particular caution.

---

## Recommendations

The council issues the following actionable recommendations:

**R1. Commission tradition-specific FP audits.** Before finalizing scores, each tradition specialist reviews the keyword list and FP context for their framework. Deliver keyword list review within 2 weeks. (Assigned: Li/Wong for Confucian, al-Qaradawi Jr. for Islamic, Osei-Mensah for Ubuntu, Narayan/Kumar for Dharmic, Wangchuk for Buddhist, Mahuta-Rau for Indigenous, Vega for Buen Vivir.)

**R2. Conduct precision-recall validation.** Manually review 50 detected papers (stratified across all 7 frameworks) and 50 non-detected papers to establish precision and recall estimates. Report as supplementary Table 1. (Assigned: Henrich to design sampling scheme; Awosanya to compute estimates; tradition specialists to adjudicate.)

**R3. Rename "non-Western" to "tradition-grounded normative frameworks."** Use specific framework names in all results. "Non-Western" appears only in literature review context with a caveat. Update all variable prefixes from `nw_` to `tg_` in internal documentation (code-level prefix change optional if too disruptive).

**R4. Rename "nw_islamic_jurisprudence" to "nw_islamic_ethics" (or tg_islamic_ethics).** Distinguish jurisprudential keywords from ethical-philosophical keywords per al-Qaradawi Jr.'s recommendation. Document the relationship between rv_islam and nw_islamic_ethics explicitly.

**R5. Clarify "Dharmic" scope.** Define whether nw_dharmic is Hindu-specific or an umbrella category. If Hindu-specific, rename to nw_hindu. If an umbrella, document overlap with nw_buddhist and handle double-counting. (Assigned: Narayan and Kumar to recommend; Wangchuk to review.)

**R6. Implement Bayesian statistical framework for small-n traditions.** Use weakly informative priors for Buddhist, Dharmic, and Buen Vivir analyses. Report posterior distributions rather than point estimates. No p-values for n < 20 without power analysis. (Assigned: Awosanya to specify model; Henrich to review.)

**R7. Add targeted search for underrepresented traditions.** Before analysis, search SCIELO/Redalyc (Spanish/Portuguese, for Buen Vivir), Index Islamicus/ISAM (Arabic/Turkish/Malay, for Islamic ethics), J-STAGE (Japanese, for Japanese AI ethics), and CNKI/Wanfang (Chinese, for Confucian AI ethics). Document found papers even if not added to vault. (Assigned: Vega for Latin American, al-Qaradawi Jr. for Islamic, Hayashi for Japanese, Li for Chinese.)

**R8. Add human rights engagement dimension.** Score all papers on a "human rights framework" dimension (keywords: human rights, dignity, non-discrimination, UDHR, ICCPR, proportionality, necessity, UNESCO AI ethics). Report correlation with all cultural frameworks. (Assigned: Pariotti to define keyword list.)

**R9. Include gender sub-layer.** Add gender analysis examining: (a) author gender composition by framework, (b) correlation between care ethics and non-Western relational frameworks, (c) gender-culture intersections in the positionality layer. (Assigned: Adams to specify; Noble to review.)

**R10. Report within-region variance.** For every between-region comparison, report within-region variance (standard deviation or interquartile range). If within > between, flag the comparison as potentially uninformative. (Assigned: Awosanya to implement.)

**R11. Include 5-10 qualitative case studies.** Select papers that illustrate what keyword scoring captures and misses. Include at minimum: (a) one Japanese paper to illustrate syncretic traditions, (b) one Southeast Asian paper to illustrate missing keywords, (c) one paper from a sanctions-affected country to illustrate structural exclusion, (d) one Latin American paper in Spanish to illustrate language exclusion, (e) one paper where rv_* and nw_* diverge to illustrate the descriptive/normative distinction. (Assigned: Khanna to select with input from Hayashi, Khin, Shaker, Vega, Kumar.)

**R12. Publish scoring code, keyword lists, and prompts as open supplementary material.** Full reproducibility requires transparency about the scoring machinery. All keyword lists, FP context lists, scoring code, and LLM prompts should be published alongside the paper. (Unanimously endorsed.)

---

## Minority Reports

### Minority Report A: On the Legitimacy of Quantifying Indigenous and Buen Vivir Traditions

**Signatories:** Dr. Tane Mahuta-Rau, Dr. Maria Soledad Vega
**Endorsed by:** Dr. Safiya Umoja Noble, Dr. Abeba Birhane

We wish to register our view that the application of keyword-based scoring to Indigenous relational ethics and Buen Vivir is not merely methodologically imperfect but epistemically violent. Both traditions explicitly challenge the Western analytical practice of decomposing holistic lifeways into measurable variables. The CARE Principles for Indigenous Data Governance establish that research involving Indigenous knowledge must be conducted under Indigenous authority. This analysis, while not extracting Indigenous knowledge per se, operationalizes Indigenous concepts as scoring targets in a system designed by non-Indigenous researchers, using a Western quantitative methodology, without formal consultation with Indigenous communities.

We acknowledge that the council has adopted safeguards (R1 keyword review, sensitivity analysis, framing statement). We do not believe these are sufficient. The framing statement acknowledges the "violence of quantification" but then proceeds to quantify. Acknowledgment without structural change is performative.

Our recommended alternative: for Indigenous relational and Buen Vivir frameworks, replace keyword scoring with a qualitative analysis conducted in partnership with scholars from those traditions. The quantitative cross-cultural comparison would then cover five frameworks (Confucian, Ubuntu, Islamic, Buddhist, Dharmic) where the relevant tradition specialists on this council have endorsed quantification. Indigenous and Buen Vivir engagement would be reported in a dedicated qualitative section with appropriate methodological framing. This approach sacrifices symmetry (7 frameworks compared on equal terms) but gains legitimacy and respect for the traditions in question.

The majority rejected this proposal on practical grounds (asymmetric methodology complicates the analysis) and on the argument that all seven frameworks' scores are presented with the same caveats. We respectfully disagree and record this minority position for the published paper's methodology section.

### Minority Report B: On the Structural Limitations of a Corpus-Based Approach

**Signatory:** Dr. Reza Shaker
**Endorsed by:** Dr. Maria Soledad Vega, Dr. Thida Khin

The entire analytical design rests on the assumption that a corpus of 2,046 English-language AI ethics papers is a meaningful sample from which to draw conclusions about global cultural engagement with AI values. I argue that this assumption is untenable for at least three categories of absence:

1. **Sanctions-excluded scholarship.** Iranian, North Korean, Syrian, Cuban, and Russian AI ethics scholars face structural barriers to publication in indexed English-language journals. Their absence from the corpus is not random — it is a direct consequence of geopolitical power. Any analysis that reports "MENA engagement with AI ethics" without accounting for the systematic exclusion of Iranian scholarship is reporting on Arab Gulf and North African perspectives only, not on the region.

2. **Language-excluded scholarship.** As Dr. Vega documented, substantial bodies of AI ethics scholarship exist in Spanish, Portuguese, Chinese, Japanese, Arabic, Korean, Bahasa, Thai, and other languages. A corpus-based analysis of English-language papers cannot detect this scholarship and should not make claims about "global" engagement.

3. **Format-excluded scholarship.** Much Global South AI ethics thinking occurs in policy documents, NGO reports, blog posts, community consultations, and oral traditions that do not appear in academic databases. The corpus captures the academic surface, not the governance reality.

I do not oppose the analysis — it will produce valuable findings about the English-language AI ethics literature. But I urge the council to insist that the title, abstract, and framing of any published paper explicitly bound the claims to "the English-language AI ethics publication ecosystem" and not use language that implies global coverage. The difference between "Buen Vivir is underrepresented in AI ethics" and "Buen Vivir is underrepresented in the English-language AI ethics literature indexed by major databases" is the difference between a finding and a colonial assertion.

The majority agreed with this framing concern (see A3) but considered it adequately addressed by the anti-essentialization guardrail and the recommended framing language. I believe it requires stronger structural integration — specifically, a "Structural Absences" section in the published paper that documents each category of exclusion with specific examples (Iranian sanctions, Latin American language barriers, Southeast Asian format barriers) rather than a generic limitations paragraph.

---

## Procedural Notes

- **Next deliberation:** 20260403-deliberation-02 — Framework keyword list review (scheduled after R1 delivery)
- **Validation sample:** Henrich to circulate sampling scheme within 1 week; tradition specialists to begin manual review upon receipt
- **Targeted search:** R7 searches to begin immediately; results reported at next deliberation
- **Document status:** This deliberation record was circulated to all 20 council members for review. No factual corrections were requested. Dr. Mahuta-Rau requested that the minority report use "epistemically violent" rather than the original "epistemically problematic"; this change was accepted.

---

*Filed: 2026-04-03 | Council Deliberation 01 of 5 | CULTURAL-GLOBAL/COUNCIL/*
