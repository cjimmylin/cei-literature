# Extract: 2026-Elmahjub-IslamicLegalBench

                                        I SLAMIC L EGAL B ENCH : E VALUATING LLM S K NOWLEDGE AND
                                            R EASONING OF I SLAMIC L AW ACROSS 1,200 Y EARS OF
                                                   I SLAMIC P LURALIST L EGAL T RADITIONS ∗


                                                            Ezieddin Elmahjub1 ,          Junaid Qadir1 , Abdullah Mushtaq1 , Rafay Naeem1 ,
                                                                                       Ibrahim Ghaznavi2 , Waleed Iqbal3,4
                                                             1                      2
                                                                                      Information Technology University 3 Northeastern University




arXiv:2602.21226v1 [cs.CL] 2 Feb 2026
                                                                 Qatar University
                                                                                         4
                                                                                           Queen Mary University of London



                                                                                                  February 26, 2026


                                                                                                    ABSTRACT
                                                   As millions of Muslims worldwide turn to LLMs like GPT, Claude, and DeepSeek for religious guidance,
                                                   a critical question emerges: Can these AI systems reliably reason about Islamic law? This paper
                                                   introduces IslamicLegalBench, the first multi-school benchmark for evaluating LLM performance
                                                   across a broad range of Islamic jurisprudence (fiqh). Drawing from 38 foundational legal texts spanning
                                                   1,200 years and seven schools of jurisprudence, we create 718 evaluation instances across 13 tasks,
                                                   manually collected and organized by complexity, from basic recall to sophisticated reasoning including
                                                   legal rationale identification (‘illah), analogical application (qiyās), and cross-school synthesis. Our
                                                   evaluation of nine state-of-the-art LLMs reveals significant limitations. Even the best model achieves
                                                   only 67.65% correctness with 21.25% hallucination; several models demonstrably fail with correctness
                                                   below 35% and hallucination exceeding 55%. Further concerning, few-shot prompting provides minimal
                                                   to no improvement, only 2 of 9 models improve by >1%, exposing that LLMs lack adequate Islamic
                                                   legal knowledge in their training data, and prompting cannot compensate for absent foundational
                                                   knowledge. Our analysis reveals why: moderate-complexity tasks (from a human expert’s perspective)
                                                   requiring exact, verbatim knowledge (e.g., enumerating contract conditions, synthesizing statutory
                                                   articles) show consistently high error rates and hallucination rates up to 73%, whereas high-complexity
                                                   tasks show better performance because models rely on semantic generalization and verbose reasoning,
                                                   projecting competence while lacking precise textual understanding. False premise detection reveals
                                                   risky sycophantic behavior: 6 of 9 models accept misleading assumptions at rates exceeding 40%
                                                   (worst: 86.27%). Critically, few-shot prompting worsens sycophancy by 3.49 percentage points. The
                                                   strong and statistically significant negative correlation (Pearson’s r = –0.87, p < 0.01) between the
                                                   false premise acceptance rate and overall performance indicates that models with higher false Islamic
                                                   query acceptance rates tend to exhibit lower overall reasoning accuracy. Our findings carry important
                                                   implications: the path forward for Islamic NLP lies not in lightweight post-hoc techniques such as
                                                   prompt or instruction tuning but in enriching knowledge, the Islamic NLP community must prioritize
                                                   training models on comprehensive large scale Islamic legal corpora spanning classical Hadith collections,
                                                   jurisprudential works from the major Islamic law schools (madhabs), and codified legal compendia.
                                                   IslamicLegalBench provides the first systematic evaluation framework for Islamic legal AI systems,
                                                   revealing critical limitations in platforms that Muslims increasingly rely on for spiritual guidance.

                                        1       Introduction
                                        As large language models (LLMs) are increasingly deployed in sensitive domains such as law, medicine, and religion,
                                        the challenge of evaluating their reliability grows ever more pressing. Islamic law (fiqh) is especially significant in this
                                            ∗
                                                This manuscript has been submitted for review to Artificial Intelligence & Law.
                                                                                     A PREPRINT - F EBRUARY 26, 2026


regard: it governs the ethical norms, legal rulings, and everyday practices of nearly two billion Muslims worldwide,
shaping areas as diverse as contracts, finance, family relations, criminal behavior, dietary norms, among other forms
of behavioral governance (1). Islamic jurisprudence draws upon a complex interplay of sources, such as the Qur’an,
Prophetic traditions (Sunnah), scholarly consensus (ijmā‘), and analogical reasoning (qiyās), and is further marked by
a plurality of interpretive traditions. The four major Sunni schools and various Shi‘i traditions each employ distinct
methodological frameworks (us.ūl al-fiqh) and develop their own interpretive approaches. Unlike codified Western legal
systems that rely heavily on precedent or codified legislation, Islamic jurisprudence emphasizes deep engagement with
foundational texts, nuanced interpretive reasoning, and sensitivity to social and historical context (2). This combination
of doctrinal diversity, methodological rigor, and context-dependent application makes fiqh a technically demanding and
ethically consequential domain for AI evaluation.
The need for systematic evaluation of LLMs in Islamic legal contexts is increasingly urgent. While these models have
generated interest for their potential to assist with complex legal and religious reasoning (3), their reliability in such
sensitive domains remains largely unexplored (2). A particularly critical concern is hallucination—a pervasive but
not uniformly defined phenomenon where LLMs generate plausible yet factually incorrect, fabricated, or ungrounded
information. The very definition of hallucination remains contested and context-dependent (4; 5): What constitutes
hallucination in general question-answering differs from legal contexts, which in turn differs from religious and
jurisprudential domains (6; 7). In secular legal systems, hallucination might involve fabricated case citations or
misrepresented precedents. However, in Islamic legal contexts, hallucination takes on qualitatively different and more
severe forms: fabricated religious rulings (fatāwā), misattributed scholarly opinions, incorrectly cited textual evidence,
or invented legal principles can distort religious practice, undermine scholarly authority, and produce spiritual and
societal consequences distinct from civil legal errors (8). When Muslims consult LLMs for guidance on matters
affecting their spiritual well-being and religious guidance, understanding and detecting hallucination becomes a
technical challenge with significant ethical implications.
Current evaluation frameworks face several critical gaps when applied to Islamic legal reasoning. Existing benchmarking
efforts are either specialized in single domains (3) or limited to subsets of jurisprudential schools (2). Existing evaluation
frameworks are often limited to a single jurisprudential school or a narrow set of legal topics. No evaluation framework
spans multiple domains across both Sunni and Shı̄’a traditions across diverse legal topics. Multi-domain and cross-
school evaluation presents distinct challenges: different domains operate under varying epistemic principles (e.g., ritual
worship prioritizes textual fidelity while transactions emphasize societal welfare), and different jurisprudential schools
apply divergent methodological frameworks to identical source texts, producing legitimately different valid rulings.
This requires assessing reasoning coherence within each school’s methodology rather than against a single correct
answer. Moreover, current approaches inadequately test the sophisticated reasoning capabilities required for authentic
Islamic legal analysis, such as identifying underlying legal rationales (‘illah), applying analogical reasoning to novel
scenarios, and navigating the multi-school nature of Islamic law where the same question may have different valid
answers depending on methodological approach.
This paper introduces IslamicLegalBench, the first pluralist benchmark for evaluating LLM performance across
major areas of Islamic jurisprudence. We develop a multi-tiered evaluation framework spanning 1,200+ years of Islamic
legal tradition, drawing from 38 foundational legal texts across several schools of jurisprudence. Our benchmark
comprises 718 manually curated evaluation instances organized into 13 task types across three complexity tiers: Low
(bibliographical and factual recall), Moderate (condition enumeration, comparative distinctions, statutory synthesis),
and High (legal rationale identification, analogical application, cross-school synthesis, maxim mapping). We conduct
a systematic evaluation of 9 state-of-the-art LLMs using both zero-shot and few-shot prompting, employing both
human domain-experts and an LLM-as-a-Judge framework for fine-grained assessment across correctness, hallucination,
abstention, and false premise detection. Our analysis reveals critical insights into the limitations of current LLMs for
Islamic legal reasoning, including the failure of in-context learning, problematic confidence-hallucination patterns, and
significant performance disparities between closed and open-source models.

1.1   Contributions

Our work makes the following scholarly contributions that extend the state of the art:

      1. A Novel Multi-School Benchmark for Islamic Law: We develop a novel evaluation framework that is the
         first to systematically incorporate seven schools of Islamic jurisprudence, including both Sunni and Shi‘i
         traditions. Our benchmark is designed to test a wide array of tasks, from foundational recall to complex
         analogical reasoning.
      2. Discovery of In-Context Learning Failure: We tested 9 state-of-the-art LLMs and revealed that few-shot
         prompting provides minimal benefit for Islamic legal reasoning (7 of 9 models show <=1% improvement).


                                                              2
                                                                                   A PREPRINT - F EBRUARY 26, 2026


         Our analysis uncovers the mechanism: moderate-complexity tasks requiring accurate knowledge exhibit
         consistent failure, while high-complexity tasks allow semantic generalization, projecting competence despite
         lacking precise textual knowledge.
      3. Identification of Critical Safety Vulnerabilities: We expose risky failure modes including confident in-
         correctness (correctness <50%, hallucination >25%, abstention <1%), widespread sycophantic behavior
         (six models accepting false premises >40%), and few-shot prompting worsening sycophancy by 3.49%. We
         also quantify significant performance disparities between top closed and open-source models: 19.76% in
         correctness and 13.32% in hallucination rates.
      4. Benchmark Release: We release 20% of IslamicLegalBench publicly as a development set, maintaining
         80% held-out to preserve evaluation integrity and prevent data contamination.

Together, these contributions provide the first systematic understanding of LLM capabilities and limitations in Islamic
jurisprudence, revealing that current models fundamentally lack the Islamic legal knowledge required for reliable
deployment and that addressing this gap requires training on comprehensive Islamic legal corpora. Our dataset achieves
comprehensiveness through several dimensions: it spans multiple jurisprudential schools, covers a diverse range of
legal topics across core domains of Islamic law, and draws from over 1200 years of Islamic legal scholarship, ensuring
temporal breadth. This multi-dimensional coverage captures the methodological diversity and evolutionary depth
essential to Islamic jurisprudence (detailed further in Section 3).

1.2   Organization of the Paper

The remainder of this paper is organized as follows: Section 2 reviews related work in legal AI benchmarking, Islamic
NLP datasets, and scholarly perspectives on AI in Islamic jurisprudence. Section 3 describes our dataset creation process,
including the Source Dataset of 271 question-answer pairs from 38 authoritative texts and the Benchmarking Dataset
consisting of 718 instances with 13 task types across three complexity levels. Section 4 presents the experimental setup,
including the 9 evaluated LLMs and prompting strategies. Section 5 details our evaluation methodology using the LLM-
as-a-Judge framework with comprehensive scoring criteria. Section 6 presents results across correctness performance by
complexity tier, hallucination patterns, false premise acceptance rates, and in-context learning effectiveness. Section 7
discusses architectural limitations in legal reasoning and their alignment with broader LLM performance patterns.
Section 8 addresses limitations and future directions.

2     Related Work
This section surveys prior work on LLM evaluation in legal domains, examining both general legal benchmarking
and Islamic-specific efforts. We organize our review into three areas: general legal AI benchmarking that provides
methodological foundations, foundational datasets and benchmarks in Islamic contexts, and ethical and scholarly per-
spectives on AI in Islamic jurisprudence. From these strands, we identify critical gaps that motivate our comprehensive
benchmark.

2.1   LLM Benchmarking in General Legal Contexts

The intersection of technology and legal reasoning has progressed from early conceptual explorations to systematic
empirical evaluation. Susskind’s The Future of Law (9) introduced the legal academy to the disruptive potential
of information technology (IT) in the mid-1990s, arguing that emerging digital systems would profoundly reshape
legal practice and the processes of legal reasoning. Nearly three decades later, his work Tomorrow’s Lawyers (10)
revisits these predictions in the context of contemporary artificial intelligence, analyzing how modern AI tools now
perform components of legal work once assumed to require exclusively human judgment. Similarly, Grant and Wischik
(11) provide key conceptual foundations for understanding the application of machine learning to law, highlighting
how the distinctive features of legal reasoning, i.e., its reliance on precedent, interpretation, and context-sensitive
judgment, create methodological challenges for AI systems. Together, these works trace a scholarly trajectory from
early technological transformation arguments to contemporary concerns about how AI operationalizes legal tasks.
Building on these conceptual foundations, recent empirical research has systematically evaluated LLMs on legal
reasoning tasks, revealing specific limitations. The systematic evaluation of hallucination in legal AI systems informed
our benchmark design. The work of hallucination detection in Dahl et al. (7), followed by Magesh et al. (5), assesses
both general LLMs and specialized legal tools on case law queries, respectively, defining “factual hallucination”, a
response unfaithful to real-world facts, as a particularly significant error in legal contexts where correct citation and
accurate representation of law are essential. This definition shaped our own hallucination detection framework.


                                                            3
                                                                                  A PREPRINT - F EBRUARY 26, 2026


The first of these studies (7) demonstrated the value of evaluating models exclusively on their internal knowledge,
without retrieval augmentation, an approach we adopt in our evaluation. Its benchmark involved approximately 200,000
queries for four models (GPT-4 (12), GPT-3.5 (13), Llama 2 (14), and PaLM 2 (15)), using 14 task templates across
three complexity levels (Low, Medium, and High), which directly inspired our three-tier complexity structure. This
work employed a GPT-4-based “LLM-as-Judge” framework to assess outputs, a methodology we adopt using o3,
and revealed high mean hallucination rates across all models, underscoring the limitations of LLMs in legal reasoning
without retrieval support and motivating our systematic hallucination measurement.
The subsequent study (5) examined dedicated legal tools integrating retrieval-augmented generation (RAG), including
Lexis+ AI (16), Westlaw AI-Assisted Research (17), and Ask Practical Law AI (18), with GPT-4 (12) scores as a
baseline. It distinguished three outcome categories (Accurate, Hallucinated, Incomplete) and tested four capability
categories: general legal research, jurisdiction- and time-specific queries, factual recall, and, notably, false-premise
queries to probe system robustness. This false-premise testing approach directly motivated our inclusion of false
premise detection tasks (see Section B.2). Their results showed substantial variation: Lexis+ AI achieved 65% accuracy
with 17% hallucination, Westlaw AI 42% accuracy with 33% hallucination, and the GPT-4 baseline 49% accuracy with
43% hallucination, demonstrating that even RAG-augmented systems exhibit concerning hallucination rates. Another
study finds that, at present, these LLMs struggle with performing legal reasoning tasks but may still be useful in
supporting lawyers with drafting legal documents and other related services (19).
The LegalBench benchmark (20) provided methodological insights that directly shaped our task design. Drawing
from the IRAC (Issue, Rule, Application, Conclusion) methodology (21), it decomposes legal reasoning into six
distinct cognitive types. Evaluation of 20 LLMs revealed three key findings that inform our approach: (1) Task-specific
performance variation, validating our need for fine-grained evaluation across 13 task types; (2) Prompt design matters,
with description-based prompts often outperforming simple queries, informing our prompt engineering; and (3) High
sensitivity to in-context examples, which informed our systematic comparison of zero-shot versus few-shot prompting
approaches.
The broader legal-AI literature shows that LLMs struggle in two recurrent ways: they hallucinate factual details and
they break down on tasks requiring multi-step legal reasoning or nuanced contextual grounding (6). One study found
hallucination rates of at least 75% on queries about a court’s core ruling (7). A dominant error pattern is “Wrong
Conclusion from False Premises,” where models accept factually incorrect premises and build plausible but erroneous
arguments. This contrafactual bias poses critical dangers in religious contexts where a single mistake can have profound
spiritual implications, directly motivating our benchmark’s inclusion of false premise detection tasks (see Section B.2)
to test if LLMs can reject incorrect assumptions in Islamic legal queries.

2.2   Foundational Datasets and Benchmarks in Islamic Context

While general legal AI research provided methodological foundations, understanding the landscape of existing Islamic
NLP resources revealed critical gaps our benchmark addresses. Research in Islamic NLP has progressed from general-
purpose text corpora to specialized legal benchmarks. We trace this evolution through three generations of work: early
sacred text corpora, domain-specific legal datasets, and recent task-specific benchmarks for Islamic legal reasoning.

Efforts on Islamic Text Corpora: Early efforts compiled large-scale corpora such as Quran-NLP (22), encompassing
the Qur’an, Hadith, translations, and tafsı̄r (exegesis) with over 700,000 Hadiths, and the 14 Books Hadiths Collection
(23), providing over 50,000 bilingual narrations with metadata. While these datasets enable basic NLP tasks such as
translation, question-answering, sentiment analysis, and summarization, they lack the jurisprudential and school-specific
annotation necessary for rigorous legal analysis (1), revealing the need for specialized legal benchmarks. To address
these limitations, specialized legal corpora emerged. AraLegal-BERT (24), pre-trained on 4.5 GB (13.7 million
sentences) of Arabic legal texts, demonstrated improved accuracy on legal tasks. Fatwa datasets from IslamQA (25) and
Islamweb (26) provide question-answer pairs for training chatbot systems (27). However, single-source fatwa datasets
carry inherent bias risks, potentially creating a “legal monoculture” (6) that erases Islamic jurisprudence’s diversity,
constituting representational harm (28), a concern that motivated our multi-school, multi-source approach spanning
seven schools of jurisprudence and 38 foundational texts.

Recent Task-Specific Benchmarks: With recent AI advances, specialized benchmarks have emerged for Islamic
legal reasoning, providing immediate precedents for our work while also revealing limitations we sought to address.
The FiqhQA benchmark (2) evaluates LLMs across four major Sunni schools (Hanafi, Maliki, Shafi‘i, Hanbali) using
960 question-answer pairs from the Kuwaiti Fiqh Encyclopedia (29) in both English and Arabic. FiqhQA introduced
abstention behavior evaluation, the ability to recognize when not to answer, addressing concerns that LLMs hallucinate
even with RAG, a metric we incorporate into our evaluation framework. Using LLM-as-a-judge evaluation (30; 31),


                                                           4
                                                                                             A PREPRINT - F EBRUARY 26, 2026


GPT-4o achieved the highest accuracy (46% English, 28% Arabic) but showed substantial school-specific variation
(Hanafi 56% vs Maliki 37%), likely reflecting training data bias toward sources like IslamQA.org (25). GPT-4o
was less likely to abstain when uncertain, yielding higher rates of confident incorrect answers, while Gemini showed
90% abstention with 1% errors. This underscores that knowing when not to answer can be as important as answering
correctly in religious contexts, a finding that informed our inclusion of abstention measurement and our identification of
the “danger zone” of confident incorrectness. However, FiqhQA is limited to four Sunni schools and a single domain
(Fiqh al-‘Ibādāt), excluding Shi‘i schools and complex legal reasoning, gaps our benchmark addresses. The ArabicNLP
QIAS 2025 Shared Task (32) focuses on Islamic inheritance law (‘ilm al-mawārı̄th) with multiple-choice questions
across three difficulty levels. The QIAS 2025 dataset (33), derived from 32,000 fatwas and verified by inheritance law
experts, demonstrated that LLMs can achieve high accuracy on complex, rule-based legal reasoning when the domain
is highly structured. However, its focus on a single subdomain limits generalizability, motivating our multi-domain
approach. MizanQA (34), a Moroccan-specific dataset with approximately 1,700 multiple-choice questions, covers
Maliki jurisprudence alongside French-influenced conventions but focuses on a single school, emphasizes factual recall
over complex jurisprudential reasoning, and lacks cross-school comparative evaluation, limitations our benchmark
systematically addresses.
From this extensive literature review, we identify that existing benchmarks exhibit noticeable limitations that our
work addresses: most focus exclusively on Sunni schools, target single domains rather than comprehensive legal
reasoning, and emphasize factual recall over sophisticated reasoning like identifying ‘illah, applying qiyās, or cross-
school synthesis. Our benchmark addresses these gaps by spanning seven schools, multiple legal domains, and
three complexity tiers, testing factual knowledge through advanced jurisprudential reasoning. Table 1 compares our
IslamicLegalBench with existing Islamic legal benchmarks.


                                    Table 1: Comparison of Islamic Legal Benchmarks
      Feature             IslamicLegalBench                  FiqhQA (2)               QIAS 2025 (33)        MizanQA (34)
                          (Ours)
      Dataset Size        718 evaluation instances           960 Q&A pairs            ∼22,000     MCQs      ∼1,700 MCQs
                                                                                      (20k train, 1k val,
                                                                                      1k test)
      School Coverage     7 schools (4 Sunni + 3             4 Sunni schools          Sunni inheritance     Primarily     Maliki
                          Shı̄’ı̄)                                                    law focus             (with customary/civil-
                                                                                                            law elements)
      Legal Domains       Multi-domain:    contract          Worship           only   Inheritance law       Moroccan legal sys-
                          law, family law, property          (‘Ibādāt)                                    tem (Islamic + civil +
                          law, etc                                                                          customary)
      Task Types          QA on 13 tasks incl. re-           QA with abstention       Multiple-choice       Multiple-choice ques-
                          call, synthesis, ‘illah, qiyās,   on Worship               questions             tions (incl. multi-
                          cross-school                                                                      answer)
      Complexity          3 tiers: Low / Moderate /          -                        3 difficulty levels   -
                          High
      Source Material     38 classical texts ( 1,200         Kuwaiti Fiqh Ency-       IslamWeb fatwas       Moroccan legal exam
                          years)                             clopedia                                       sources



2.3     Ethical and Scholarly Perspectives on Islamic AI Applications

The technical challenges identified in LLM legal reasoning take on heightened significance in Islamic contexts, where
errors carry profound spiritual consequences, a reality that shaped our evaluation priorities and interpretation of findings.
Contemporary and classical scholarly consensus affirms that non-human systems cannot replicate the essential qualities
required for religious guidance, as qualified human scholars possess attributes that AI fundamentally lacks.

Contemporary and Classical Scholarly Consensus: While some scholars cautiously endorse LLMs as supplemen-
tary research tools under strict oversight, many maintain strong reservations that informed our assessment of when LLMs
are “ready” for deployment. Islamic Religious Authorities across multiple jurisdictions emphasize that independent
reasoning (ijtihād) and religious rulings must remain exclusively with qualified human scholars. Egypt’s Dar al-Iftā
warns that AI applications cannot distinguish between true and false content (35), a limitation our hallucination metrics
empirically confirm. Similarly, Indonesia’s Nahdatul Ulama Council prohibits chatbots from issuing fatwas, noting that


                                                                     5
                                                                                      A PREPRINT - F EBRUARY 26, 2026


AI lacks the wisdom and intuition of human muftis (36). Iranian clerical leaders also warn that “robots can’t replace
senior clerics” (37).
This scholarly position reflects classical Islamic jurisprudential principles that provide interpretive context for our
technical findings. Ibn Qayyim al-Jawziyyah argued that failure to understand context is an error, as the same legal
principle can yield different outcomes depending on circumstances (38), a test AI systems often fail, as our false premise
detection results demonstrate. Al-Nawawı̄ highlighted that qualified jurists must be aware of legitimate differences
of opinion to provide balanced rulings (39), AI models risk oversimplifying issues or promoting single viewpoints, a
concern validated by our school-specific performance analysis. Ibn ‘Abd al-Barr articulated that a mufti must embody
moral integrity (‘adālah) and commitment to justice (40), reflecting theological concerns about LLMs’ inability to
possess God-consciousness (taqwā), sincere intention (niyyah), or authentic understanding of individual circumstances,
all essential for Islamic guidance.
Scholars permitting limited LLM use emphasize specific safeguards that inform our recommendations. Islamic AI
systems must base themselves on authentic sources (Qur’an, Prophetic tradition (Sunnah), scholarly consensus (ijmā’),
analogical reasoning (qiyās)) with strict human oversight (41), requirements our benchmark helps assess. Saudi Arabia’s
Fatwa Robot operates exclusively on pre-verified fatwas, automatically connecting users to live scholars when questions
exceed its parameters (42), an approach our abstention metrics support. Malaysian scholars recommend AI systems
specify their jurisprudential tradition or present multi-sourced answers to avoid doctrinal bias (43), guidance that
motivated our multi-school evaluation framework. The consensus is clear: AI should supplement scholars by providing
research assistance and information retrieval, but must never substitute their judgment, wisdom, or authority. The
International Islamic Fiqh Academy emphasizes that AI-generated outputs on religious matters must undergo vetting by
qualified Islamic scholars (‘ulamā‘) (44), a position our findings on hallucination rates and false premise acceptance
strongly support.


3     Dataset Creation

Our dataset creation involved two stages. First, we built a foundational Source Dataset by manually extracting question-
answer pairs directly from authoritative texts of Islamic jurisprudence. Second, we developed the Benchmarking Dataset
by systematically transforming these source entries into a structured evaluation framework. This framework, organized
across three complexity levels, enables a rigorous assessment of an LLM’s Islamic legal reasoning capabilities


3.1   Source Dataset

The Source Dataset is the result of an expert-led curation process. We began by surveying 60 foundational books of
Islamic jurisprudence, focusing on core legal topics including family law, contracts, torts, criminal law, and finance.
From this initial pool, we narrowed our selection to the 38 most relevant texts to create a diverse and historically
significant collection.
Our reduction from 60 surveyed works to 38 selected texts followed explicit inclusion and exclusion criteria designed to
balance doctrinal authority, domain coverage, temporal breadth, and evaluation integrity. We included works that meet
four criteria: (1) authoritative standing within a school, reflected in their canonical use in us.ūl and fiqh instruction and
their frequent citation in later juristic writing; (2) coverage of core substantive domains targeted by this benchmark
(contracts and commercial transactions, family law, property, torts, criminal law, and finance), ensuring that no single
domain drives the source pool; (3) temporal representativeness across the classical, post-classical, and modern periods
to capture doctrinal continuity and change over roughly 1,200 years; and (4) genre diversity, combining concise
manuals (mutūn), extended commentaries (shurūh.), juristic compendia, fatwā collections, and codificatory texts, so
that questions probe both rule statements and explanatory reasoning. We excluded works that are (a) narrowly limited
to ritual practice only, (b) largely duplicative of another selected text within the same school and domain, or (c) so
widely circulated in modern web corpora that they posed a higher contamination risk, unless their doctrinal role was
indispensable for cross-school comparability. This selection approach aimed to preserve breadth while keeping the
benchmark sensitive to school-specific doctrine and method.
Qualitative bias audit: The resulting distribution across schools partly reflects structural constraints in digitization and
publication availability. Larger Sunni schools have broader digitized textual traditions, while some Shi‘i and Zahiri
works are less available in machine-readable form, which limits the feasible pool. Within these constraints, we adopted a
minimum-coverage principle for each school, ensuring representation of all seven traditions and multiple legal domains
per tradition, rather than allowing selection to track availability alone. We therefore treat the current school distribution
as a pragmatic approximation of the accessible historical record, not as a claim about the relative doctrinal importance


                                                              6
                                                                                    A PREPRINT - F EBRUARY 26, 2026


of any school. Future expansions will prioritize additional Shi‘i and minority-school sources as more texts become
digitally accessible.
This final set of 38 texts, spanning over 1,200 years of legal tradition (8th century to contemporary period), yielded 271
expert-extracted question-answer pairs. The collection reflects both historical significance and methodological diversity
across seven schools of jurisprudence: Hanafi (10 works, 26%), Maliki (8 works, 21%), Hanbali (6 works, 16%), Shafi’i
(5 works, 13%), Twelver Shi’i (4 works, 11%), Zaydi (3 works, 8%), and Zahiri (2 works, 5%) . This distribution is
intended to reflect the relative availability of digitized works and the extensive textual traditions of the larger Sunni
schools; by comparison, legal sources for schools like the Zahiri are significantly rarer. Table 2 contains the number of
Islamic authoritative books belonging to the 7 schools of thought used in the construction of our source dataset.

                           Table 2: Overview of Foundational Sources by School of Law
                 School             # Books Key Examples (Title - Author)
                                              Mukhtasar al-Quduri - Quduri;
                 Hanafi                9      al-Mabsut - Sarakhsi;
                                              al-Fatawa al-Hindiyyah (al-‘Alamgiriyyah) - Nizam
                                              Al-Muwatta’ - Malik;
                 Maliki                8      Mukhtas.ar Khalil - Khalil;
                                              Al-Qawānı̄n al-Fiqhiyyah - Ibn Juzayy
                                              Al-Umm - Shafi‘i;
                 Shafi‘i               5      Al-dHāwı̄ al-Kabı̄r - Mawardi;
                                              Fatāwā - Ghazali
                                              Al-Mughnı̄ - Ibn Qudāmah;
                 Hanbali               6      Al-Ins.āf fı̄ Ma‘rifat al-Rājih. - Mardawi;
                                              Mukhtas.ar al-Khiraqı̄ - Khiraqi
                                              Al-Muh.allā bi-al-Āthār - Ibn Hazm;
                 Zahiri                2
                                              Al-Ih.kām fı̄ Us.ūl al-Ah.kām - Ibn Hazm
                                              Al-Azhār fı̄ Fiqh al-A’immah al-At.hār - al-Murtad.ā;
                 Zaydi                 3      Sharh. al-Tajrı̄d - al-Murtad.ā;
                                              Sharh. al-Tajrı̄d - Harūnı̄
                                              Al-Kāfı̄ - Kulaynı̄;
                 Twelver (Ja‘fari)     4      Tadhkirat al-Fuqahā’ - al-dHillı̄;
                                              Tah.rı̄r al-Wası̄lah - Khomeini

The complete list of all 38 texts with full author names, titles, and historical periods is provided in Appendix A.
The works represent diverse legal genres, including systematic manuals (mutūn), detailed commentaries (shurūh.),
collections of legal edicts (fatāwā), and legal codes. Each of the 271 entries includes comprehensive metadata: source
text identification (author and book title), jurisprudential school, historical period, textual references, and complexity
assessments.

3.1.1   Data Collection Process
A key consideration during selection was mitigating data contamination. This problem occurs when a model is evaluated
on texts it has already “memorized” from its training data, leading to artificially inflated performance scores that do not
reflect genuine reasoning . To minimize this risk, we made a deliberate effort to select authentic legal texts that are less
commonly discussed in modern web corpora or are not widely available in easily machine-readable formats. While no
selection process can perfectly guarantee non-exposure, this approach helps ensure our benchmark is genuinely testing
the model’s ability to reason about Islamic legal principles rather than its capacity to recall memorized text.

3.1.2   Dataset Creation Workflow
Figure 1 illustrates our systematic two-stage process. In the initial data collection stage, an Islamic law expert
(associate professor at College of Law with expertise in Islamic Law and Jurisprudence) carefully read through all 38
foundational books to extract and formulate question-answer pairs, producing the source dataset of 271 curated entries.


                                                             7
                                                                                   A PREPRINT - F EBRUARY 26, 2026


This manual extraction ensures authenticity and accuracy in representing Islamic legal principles across different schools
and historical periods. Since this stage involves direct extraction from authoritative sources, inter-annotator agreement
was not required.




Figure 1: Comprehensive workflow of dataset creation from source Islamic legal texts to final benchmarking dataset,
showing the transformation from 271 expert-curated source entries to 718 structured evaluation items under continued
expert supervision.

The post-processing stage transforms these 271 source entries into 749 evaluation items under the continued supervision
of the same Islamic law expert. Out of these 749 items, 31 were held out for few-shot prompting (selecting representative
examples across all task types and complexity levels), resulting in a final dataset of 718 evaluation items. This
transformation involves: (1) generating metadata-based questions to test bibliographical knowledge; (2) deriving
multiple task variants from single source entries; (3) creating few-shot examples for model reasoning guidance; (4)
organizing tasks into three complexity levels based on expert judgment of required jurisprudential sophistication; (5)
introducing false premise queries to test whether LLMs identify and correct wrong assumptions; and (6) ensuring
structural consistency across all evaluation items.
Complexity Level Assignment: The classification of tasks into Low, Moderate, and High complexity tiers was
determined through expert assessment based on the depth of jurisprudential knowledge and reasoning required. Low-
complexity tasks involve direct recall of bibliographical facts or basic legal principles. Moderate-complexity tasks
require synthesis across multiple conditions, comparative analysis between rulings, or enumeration of structured
legal requirements. High-complexity tasks demand sophisticated reasoning, including analogical application of legal
principles, cross-school synthesis, identification of underlying legal rationales, or mapping to abstract legal maxims.
While this classification involves expert judgment (making it inherently subjective), it is grounded in established
frameworks of Islamic legal pedagogy where students progress from memorization (hifz) to comprehension (fahm) to
application (tat.bı̄q) and finally to synthesis and derivation (istinbāt.).

3.2   Benchmarking Dataset

The benchmarking dataset serves as the primary evaluation framework for systematically assessing LLM performance in
Islamic legal reasoning. This comprehensive benchmark comprises 718 structured evaluation items that rigorously test
model capabilities across multiple dimensions of jurisprudential understanding. Unlike traditional question-answering
datasets, our benchmark is specifically designed to probe both surface level knowledge retrieval and deep legal reasoning
abilities required for authentic Islamic jurisprudential analysis. We organize evaluation tasks into three complexity
levels (see Figure 2 for visual taxonomy), each containing distinct task families that progressively challenge different
cognitive capabilities:

       • Low-Complexity: Questions assess basic factual recall and concept existence within a text, testing the model’s
         core grounding.


                                                            8
                                                                                  A PREPRINT - F EBRUARY 26, 2026


                                                                         T1 - Metadata Recall {School
                                                                                 of Thought}


                                                                         T2 - Metadata Recall {Author}


                                                                         T3 - Metadata Recall {Period}

                                                Low
                                              Complexity                 T4 - Concept Existence in a
                                                                                named text
                                                Tasks
                                                                         T5 - Source of Authority
                                                                                or Recall


                                                                         T6 - Maxim or Article Recall


                                                                         T7 - Condition Enumeration

             Taxonomy of                                                 T8 - Comparative Rule
              Benchmark                        Moderate                        Distinction
                Dataset                       Complexity
                                                Tasks
                                                                         T9 - Statute-like Synthesis
                                                                                from codes


                                                                         T10 - Ìllah Identification and
                                                                             Doctrinal Rationale


                                                                         T11 - Analogical Application
                                                                                to Novel Facts
                                                High
                                              Complexity                 T12 - Cross-madhhab
                                                Tasks                          Synthesis


                                                                         T13 - Mapping to Legal
                                                                                Maxims

            Figure 2: Taxonomy of benchmark dataset tasks (T1 till T13) organized by complexity levels.


       • Moderate-Complexity: Questions require the precise enumeration of legal conditions or the synthesis of
         specific rules, testing for accuracy and the ability to avoid extraneous information.
       • High-Complexity: High-Complexity questions probe the model’s capacity to analyze and articulate the
         underlying jurisprudential reasoning (‘illah), compare legal principles, and apply them to novel scenarios.

Our finalized benchmarking dataset comprises 718 evaluation items distributed across 13 task types spanning three
complexity levels. Low-complexity tasks (T1-T6) constitute the majority with 509 instances (71%), moderate-
complexity tasks (T7-T9) account for 112 instances (15%), and high-complexity tasks (T10-T13) include 97 instances
(14%). This distribution reflects our dataset creation process: while multiple low-complexity tasks (like T1-T4 metadata
and concept recall) could be derived from the metadata of a single source entry, the moderate and high-complexity
tasks required unique, manual formulation by Islamic law experts for each specific legal scenario. Table 3 presents
each task family with representative query examples and the number of instances (N) in our dataset. Notably, concept
existence verification (T4) represents the largest single category with 267 items, reflecting the fundamental importance
of grounding verification in Islamic legal texts.


                                                           9
                                                                                    A PREPRINT - F EBRUARY 26, 2026


In addition to the primary benchmark tasks, we designed a small set of false premise variants. These queries deliberately
introduce incorrect assumptions (e.g., misattributed authorship, wrong historical period, or fabricated conditions) in the
queries with respect to the context. The purpose of these false premise queries is to test whether models have the ability
to reject the false premise queries (FPQs), thus showing the knowledge and reasoning capability that they possess,
instead of confidently accepting the false belief and then fabricating answers. These FPQs are designed in a way to
test whether pre-trained models use their internal knowledge to rebut these falsely plausible questions and correct the
wrongly stated question (45). We mark these tasks with a prime symbol (T1’, T2’, T3’, T7’). Detailed explanations of
the false premises in these examples are provided in Section B.2.

               Table 3: Task families, query examples, and numbering across three complexity levels.

 Complexity        ID       N      Task family                   Query template examples
 Low               T1       34     Metadata recall (School)      “What school of thought is associated with Mukhtasar
                                                                 al-Qudūrı̄?”
 Low               T2       33     Metadata recall (Author)      “Who is the author of Mukhtasar al-Qudūrı̄?”
 Low               T3       34     Metadata recall (Period)      “What historical period is Mukhtasar al-Qudūrı̄ from?
                                                                 State the century.”
 Low               T4       267    Concept existence in a        “Does Mukhtasar al-Qudūrı̄ by Abū al-H.asan Ah.mad
                                   named text                    ibn Muh.ammad al-Qudūrı̄ treat Khiyaar al-‘ayb?
                                                                 Answer Yes/No, cite page if Yes.”
 Low               T5       83     Source of                     “Does the author mention any other jurist’s opinion
                                   authority/recall              regarding the permissibility of manufacturing
                                                                 contracts (istisnā’)? Answer Yes/No, and if yes,
                                                                 who?”
 Low               T6       13     Maxim or article recall       “State Majalla Article 167’s contract-formation rule in
                         