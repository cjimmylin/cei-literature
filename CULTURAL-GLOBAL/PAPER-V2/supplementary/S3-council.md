# Supplementary: Expert Council Composition and Deliberations

## S3.1 Council Composition

### Tier 1 — Tradition & Domain Specialists

**Member 1: Confucian Ethics Specialist.** Expertise in Confucian moral philosophy, role ethics (*ren*, *li*, *junzi*), and the application of Confucian relational thought to technology governance. Primary assignment: verifying all characterizations of Confucian ethical traditions, ensuring anti-essentialization (no claims of the form "Confucianism holds X"), and reviewing the Confucian-relational normative orientation description.

**Member 2: Islamic Ethics Specialist.** Expertise in Maqāṣid al-Sharīʿah, *fiqh* (Islamic jurisprudence), *uṣūl al-fiqh* (principles of jurisprudence), and the intersection of Islamic legal reasoning with AI governance. Primary assignment: verifying all characterizations of Islamic ethical traditions, reviewing the benchmark gap analysis for Islamic ethics, and ensuring the distinction between *fiqh* (jurisprudential) and *akhlāq* (character-based) approaches is maintained.

**Member 3: Ubuntu/African Philosophy Specialist.** Expertise in Ubuntu communalism, African moral theory, and the philosophical foundations of communal personhood. Primary assignment: verifying characterizations of Ubuntu and broader African philosophical traditions, reviewing the communal methodology critique (Section 4.6 on unit of moral agency), and ensuring Sub-Saharan African AI ethics scholarship is not reduced to a single tradition.

**Member 4: Indigenous Knowledge Specialist.** Expertise in Indigenous data sovereignty, CARE Principles (Collective benefit, Authority to control, Responsibility, Ethics), Māori *tikanga*, and relational ontology. Primary assignment: reviewing all references to Indigenous knowledge systems, ensuring CARE compliance framing, critiquing the application of quantitative methods to traditions that may resist dimensional decomposition, and reviewing supplementary materials for appropriate Indigenous knowledge governance.

**Member 5: Cross-Cultural Psychologist.** Expertise in the WEIRD framework (Henrich et al., 2010), measurement invariance testing (MGCFA, DIF), cross-cultural psychometrics, and the operationalization of cultural constructs. Primary assignment: validating the WEIRD score operationalization, reviewing the measurement invariance findings, and ensuring statistical claims meet the standards of cross-cultural psychology.

**Member 6: Buddhist/Dharmic Ethics Specialist.** Expertise in Buddhist ethics (Theravāda and Mahāyāna), Dharmic traditions (Hindu, Jain, Sikh), and contemplative approaches to moral reasoning. Primary assignment: verifying characterizations of Buddhist and Dharmic traditions, reviewing the concept mapping for these traditions, and ensuring the Theravāda-Mahāyāna distinction is acknowledged where relevant.

### Tier 2 — Methodological & Narrative Specialists

**Member 7: AI Safety/Alignment Researcher.** Expertise in RLHF, constitutional AI, value learning, and the technical mechanisms of alignment. Primary assignment: reviewing the trial methodology, evaluating the RLHF conflict taxonomy, and ensuring the implications for the alignment research program are technically accurate.

**Member 8: Bibliometrician/Meta-Scientist.** Expertise in systematic reviews, research landscape analysis, and the methodology of bibliometric studies. Primary assignment: reviewing the corpus analysis methodology, validating the scoring pipeline, and ensuring the landscape analysis meets bibliometric standards.

**Member 9: Decolonial Studies Scholar.** Expertise in epistemic justice, coloniality of knowledge, and the power dynamics of global knowledge production. Primary assignment: cross-cutting critique of all sections for epistemic power dynamics, reviewing the positionality analysis, and ensuring the paper does not reproduce the extractive dynamics it critiques.

**Member 10: Science Communication Specialist.** Expertise in writing for high-impact interdisciplinary journals, narrative structure, and accessibility for broad audiences. Primary assignment: overall narrative arc, ensuring each section is accessible to readers from psychology, computer science, philosophy, and policy backgrounds, and reviewing the abstract and conclusion for impact.

**Member 11: AI Governance/Policy Scholar.** Expertise in international AI governance frameworks (UNESCO, OECD, G20), policy-making processes, and the translation of research findings into governance recommendations. Primary assignment: reviewing Section 7.7 (Implications for AI Governance), ensuring recommendations are actionable and politically literate, and reviewing the policy impact tracing future work item.

**Member 12: Philosophy of Science Specialist.** Expertise in the value-ladenness of measurement, construct validity, and the epistemology of quantification. Primary assignment: theoretical framing of the measurement invariance crisis, reviewing the construct validity arguments in Study 2, and ensuring the paper's philosophical claims about the relationship between measurement and values are rigorous.

## S3.2 Operating Rules

1. **Tradition veto authority.** Members 1--6 hold veto authority over any claim about their respective tradition or domain. A vetoed claim must be revised to the tradition specialist's satisfaction before publication.

2. **Anti-essentialization mandate.** All sections must use formulations of the type "scholars within the [tradition] argue X" or "the [framework] posits X," never "Islam holds X" or "Confucianism says X." Tradition specialists flag violations; the Science Communication Specialist (#10) ensures accessible alternatives.

3. **Internal diversity acknowledgment.** Every tradition discussed must acknowledge internal heterogeneity (schools, denominations, regional variants). "Buddhist ethics" must note the Theravāda-Mahāyāna distinction; "Islamic ethics" must note the *fiqh*-*akhlāq* distinction; "Indigenous relational ethics" must note the radical locality of specific Indigenous traditions.

4. **Cross-cutting review.** Member 9 (Decolonial) reviews all sections for epistemic justice issues. Member 10 (Science Communication) reviews all sections for accessibility. These cross-cutting reviews operate in addition to, not instead of, primary assignments.

5. **Consensus mechanism.** Disagreements between council members are resolved through a modified Delphi process: independent position statements, structured discussion, and consensus or documented minority report. Two minority reports were produced (see S3.3).

## S3.3 Minority Reports

### Minority Report A: The Quantification Tension (Members 4, 6)

Members 4 (Indigenous Knowledge) and 6 (Buddhist/Dharmic Ethics) registered a formal concern about the paper's methodological approach. The concern: applying quantitative keyword-based scoring to normative traditions that may resist or be denatured by dimensional decomposition. Specifically:

- Indigenous relational ethics is radically local: Māori *tikanga* is not interchangeable with Aboriginal Australian *Dreaming* law or Navajo *hózhó*. Aggregating these under a single "Indigenous relational" score erases the specificity that gives each tradition its moral authority.
- Buddhist ethics involves a paradox: the *anatta* (non-self) doctrine challenges the very notion of an "agent" whose "values" can be "aligned." Scoring Buddhist engagement on a 0--100 scale presupposes the agent-centered moral ontology that Buddhist philosophy critiques.
- Buen Vivir is, by its own account, incommensurable with optimization paradigms. Assigning it a score within an optimization-based scoring pipeline enacts the very epistemological violence the paper critiques.

**Resolution:** The minority report is acknowledged in the main text (Sections 2.7, 7.9). The paper proceeds with the quantitative approach but foregrounds these tensions as unresolved methodological challenges. The precision-adjusted estimates (which reduce several traditions to single-digit paper counts) may themselves be read as evidence of the quantification tension: the traditions that resist quantification are also the traditions that the scoring pipeline captures least accurately.

### Minority Report B: Linguistic Exclusion (Members 2, 9)

Members 2 (Islamic Ethics) and 9 (Decolonial Studies) registered a concern about the corpus's English-language bias (~78%). Specifically:

- Substantial AI ethics scholarship in Arabic exists but is invisible to the English-language corpus. Publications from Al-Azhar, IIUM, and the Islamic Foundation engage AI governance through *maqāṣid* reasoning but are published in Arabic-language journals not indexed in arXiv or ACL Anthology.
- The same applies to Mandarin-language scholarship (Chinese AI ethics journals, CASS publications), Spanish-language decolonial AI work (Redalyc, SciELO), and Hindi-language philosophical engagement with AI.
- The English-language bias is not merely a data limitation; it is itself a manifestation of the WEIRD problem. Reporting the bias as a "limitation" understates its constitutive role in producing the very skew the paper documents.

**Resolution:** The minority report is acknowledged in the Limitations section (2.8) and the Reflexivity Statement (2.7). The expanded corpus future work item (Section 8) explicitly targets multilingual databases.

## S3.4 Review Process

The council conducted reviews across seven phases:

1. **Methodology design review** (pre-analysis): Council reviewed proposed scoring instruments, WEIRD operationalization, and analytical methods before data collection.
2. **Keyword list development** (Study 1): Tradition specialists (#1--6) developed and refined keyword lists for their respective frameworks.
3. **Gold standard validation** (Study 1): Council reviewed stratified sampling design and false positive/negative classifications.
4. **Feature taxonomy development** (Study 2): Council developed the 96-feature taxonomy through iterative refinement.
5. **Benchmark evaluation** (Study 2): Modified Delphi process for deep-scoring 32 benchmarks.
6. **Trial protocol review** (Study 3): Council reviewed trial design, prompt structure, and RLHF tension coding scheme.
7. **Manuscript review** (final): All 12 members reviewed the complete manuscript. 47 recommendations were produced (12 Critical, 18 Important, 17 Desirable). All Critical and Important recommendations were incorporated; 14 of 17 Desirable recommendations were incorporated (3 deferred to future work).
