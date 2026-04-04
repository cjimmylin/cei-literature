# Extract: 2026-Abdelaal-IslamicMMLU

                                                                       IslamicMMLU:
                                                    A Benchmark for Evaluating LLMs on Islamic Knowledge

                                               Ali Abdelaal, Mohammed Nader Al Haffar, Mahmoud Fawzi, Walid Magdy
                                                                    The University of Edinburgh
                                             {s2431177, s2419871, m.fawzi}@ed.ac.uk, wmagdy@inf.ed.ac.uk
                                                              Abstract
                                             Large language models are increasingly con-
                                             sulted for Islamic knowledge, yet no com-          The MMLU paradigm (Hendrycks et al., 2021)
                                             prehensive benchmark evaluates their perfor-
                                                                                                has been extended to legal (Hijazi et al., 2024),
                                             mance across core Islamic disciplines. We




arXiv:2603.23750v1 [cs.CL] 24 Mar 2026
                                             introduce IslamicMMLU, a benchmark of              cultural (Huang et al., 2024), and general Ara-
                                             10,013 multiple-choice questions spanning          bic (Koto et al., 2024) domains, but to our knowl-
                                             three tracks: Quran (2,013 questions), Hadith      edge no systematic Islamic knowledge evaluation
                                             (4,000 questions), and Fiqh (jurisprudence,        benchmark exists.
                                             4,000 questions). Each track is formed of             Islamic knowledge evaluation faces unique chal-
                                             multiple types of questions to examine LLMs
                                                                                                lenges across all three disciplines. Quranic evalu-
                                             capabilities handling different aspects of Is-
                                             lamic knowledge. The benchmark is used to
                                                                                                ation requires precise textual recall across 6,236
                                             create the IslamicMMLU public leaderboard          verses (Ayahs). Hadith evaluation demands source
                                             for evaluating LLMs, and we initially evalu-       authentication across authentic canonical collec-
                                             ate 26 LLMs, where their averaged accuracy         tions, textual completion, and reliability grad-
                                             across the three tracks varied between 39.8%       ing of authenticity. Fiqh evaluation confronts
                                             to 93.8% (by Gemini 3 Flash). The Quran            the inherent pluralism of Islamic jurisprudence,
                                             track shows the widest span (99.3% to 32.4%),      where the same act may receive different rul-
                                             while the Fiqh track includes a novel madhab
                                                                                                ings across multiple valid schools of thought
                                             (Islamic school of jurisprudence) bias detec-
                                             tion task revealing variable school-of-thought     (madhahib).“Correct/Incorrect” evaluation is fun-
                                             preferences across models. Arabic-speciﬁc          damentally insufﬁcient for ﬁqh, as a model pe-
                                             models show mixed results, but they all un-        nalised for answering according to one school
                                             derperform compared to frontier models. The        when the benchmark expected another is not ex-
                                             evaluation code and leaderboard are made pub-      hibiting error but reﬂecting the genuine plurality
                                             licly available.                                   of the tradition.
                                         1   Introduction                                          We introduce IslamicMMLU with the following
                                                                                                contributions:
                                         Large language models (LLMs) are increasingly
                                                                                                  1. IslamicMMLU benchmark:                 10,013
                                         consulted for information about Islamic topics
                                                                                                     multiple-choice questions spanning three
                                         by millions of users worldwide (Mubarak et al.,
                                                                                                     tracks with 12 task types that evaluate
                                         2025). Islamic knowledge spans multiple inter-
                                                                                                     different facets of Islamic knowledge.
                                         connected disciplines (e.g., Quranic studies, Ha-
                                                                                                  2. Fiqh track with madhab bias detection:
                                         dith sciences, and Islamic jurisprudence), each re-
                                                                                                     A novel evaluation task measuring implicit
                                         quiring distinct scholarly expertise and evaluation
                                                                                                     school-of-thought bias in LLMs.
                                         methodologies. Yet no comprehensive benchmark
                                                                                                  3. Evaluation of 26 LLMs: Comprehensive
                                         evaluates LLM performance across these core do-
                                                                                                     evaluation across all three tracks with boot-
                                         mains. This gap can lead to religious misinforma-
                                                                                                     strap conﬁdence intervals and statistical sig-
                                         tion affecting daily practice for Muslims who may
                                                                                                     niﬁcance testing.
                                         lack easy access to qualiﬁed scholars (Naous et al.,
                                                                                                  4. IslamicMMLU leaderboard1 : Evaluation
                                         2024; Fawzi et al., 2026).
                                                                                                     code and results released publicly via Hug-
                                            Several recent efforts address aspects of Islamic
                                                                                                     gingFace, with a live leaderboard supporting
                                         NLP (e.g., hallucination detection, cultural com-
                                         petence, and jurisprudential QA), but none pro-           1
                                                                                                   https://huggingface.co/spaces/
                                         vides comprehensive cross-discipline evaluation.       islamicmmlu/leaderboard
      community evaluation of new models.               extended this to harder questions with ten op-
                                                        tions. Domain-speciﬁc adaptations have emerged
2     Background and Related Work                       for law, medicine, and cultural knowledge, es-
                                                        tablishing MCQ evaluation as the reproducible,
2.1    Islamic Knowledge Domains
                                                        scalable framework for cross-model comparison.
Islam, the world’s second-largest religion, centres     HELM (Liang et al., 2023) provides a holistic eval-
on three interconnected scholarly traditions that       uation framework spanning multiple scenarios and
underpin religious practice and daily life. The         metrics.
Quran is the central scripture of Islam, com-
prising 114 chapters (surahs) and 6,236 verses          2.3 Arabic NLP Benchmarks
(ayahs). Muslims believe it to be the verba-            ArabicMMLU (Koto et al., 2024) is the most di-
tim word of God as revealed to Muhammad, the            rect comparator: 14,575 native Arabic questions
prophet of Islam. The Quran is recited in the ﬁve       across 40 subjects sourced from school exams in
daily prayers that structure Muslim worship, and is     eight Arab countries, with quality validation on
among the most widely memorised religious texts         100 samples achieving 96% accuracy. It includes
in the world (Abokhodair et al., 2020).                 Islamic studies as a single category with basic
   The Hadith literature records the sayings, ac-       questions without the domain depth needed to ex-
tions, and tacit approvals of the Prophet Muham-        amine knowledge in different nuances of Islam.
mad (Fawzi et al., 2025). It consists of two parts:     ACVA, introduced with AceGPT (Huang et al.,
1) isnad which is the chain of narrators who nar-       2024), offers 8,000+ true/false questions on Ara-
rated the quote of the prophet till the time it has     bic cultural values but explicitly excludes religious
been written, and 2) matn, which is the main            jurisprudence. AlGhafa (Almazrouei et al., 2023)
content of the quote itself. Islam has two main         provides a general Arabic evaluation benchmark
branches. The Sunni branch which is followed            but does not cover Islamic knowledge domains in
by the majority of Muslims and the Shia branch.         depth. ILMAAM (Nacar et al., 2025) provides a
Six canonical collections of Hadith are widely          culturally aligned Arabic MMLU variant. ArabLe-
accepted by Sunni Muslims as the most reliable          galEval (Hijazi et al., 2024) evaluates LLMs on
source of Hadith, which are Bukhari, Muslim, Abu        Saudi secular law with 10,000+ MCQs for domain-
Dawud, Tirmidhi, Nasa’i, and Ibn Majah. Hadith          speciﬁc evaluation. A recent survey catalogues
sciences classify narrations by authenticity accord-    over 40 Arabic benchmarks and identiﬁes gaps
ing to how evident it has been said by the prophet.     in religious domain coverage (Al-Zubaidi et al.,
There are four main authenticity levels: sahih (au-     2025).
thentic), hasan (good), da‘if (weak), and mawdu‘
(fabricated). Shia Muslims use other books.             2.4 Cultural Bias in LLMs
   Both Quran and Hadith are the main sources           Naous et al. (2024) demonstrate that LLMs default
of Islamic jurisprudence (in Arabic Fiqh). There        to Western cultural norms even when prompted
are four major Sunni schools (madhab), namely           in Arabic. Plaza-del Arco et al. (2024) ﬁnd dif-
Hanaﬁ, Maliki, Shaﬁ’i, and Hanbali, developed           ferential treatment across faiths, with Islam fac-
over centuries and are recognised as equally valid.     ing elevated stereotyping and disproportionate re-
They often agree but may reach different rul-           fusal rates. Abid et al. (2021) provide foundational
ings on the same question, creating a legitimate        evidence of persistent anti-Muslim bias in GPT-3.
pluralism that standard single-answer evaluation        DLAMA (Keleg and Magdy, 2023) reveals West-
paradigms cannot capture. The Shia disagreement         ern bias in multilingual knowledge probing.
about Hadith may lead to to some variation in Fiqh.
Nevertheless, it still agrees with Sunni in many rul-   2.5 Islamic and Religious NLP
ings regarding life and worship.                        IslamicEval 2025 (Mubarak et al., 2025) is the ﬁrst
                                                        shared task targeting LLM hallucinations in Is-
2.2    MMLU and LLM Evaluation                          lamic content, attracting 13 teams. The shared task
The MMLU benchmark (Hendrycks et al., 2021)             offers solution to LLMs hallucination with Quran
established MCQ-based knowledge evaluation as           and Hadith. Their released dataset highlights the
a standard paradigm, with 15,908 questions across       presence of hallucination in Islamic content by dif-
57 subjects. MMLU-Pro (Wang et al., 2024)               ferent LLMs, which further motivates the need for
    Benchmark         Lang #Q Tracks Bias Pub. Val.                      Quran        Hadith         Fiqh
    ArabicMMLU         ar 14.6k   †
                                  1    7   3 2 ann.       Questions       2,013       4,000          4,000
    ACVA               ar 8k+     1    7   3   —          Task types        3            4             5
    IslamicEval ’25    ar  —      2    7   3 task         Sources       114 surahs 6 collections 1 encyclopedia
    PalmX              ar  —      1    7   3   —          Bias analysis     —           —           Madhab
    FiqhQA             ar 960     1    7   3 synth
    Isl.LegalBench     ar 718     1    7   3 expert      Table 2: IslamicMMLU benchmark overview. 10,013
    AlGhafa            ar 10k+    0    7   3   —
                                                         questions from 3 tracks across 12 task types.
    IslamicMMLU ar         10k    3    3 API expert

Table 1: Comparison with related benchmarks. #Q          tion type design, and domain-speciﬁc challenges.
= question count; Tracks = Islamic discipline count      Table 2 summarises the three tracks.
(† ArabicMMLU has Islamic Studies as one of 40 sub-
jects); Bias = madhab bias detection; Pub. = public      3.1 Quran Track
access (3 = open, API = leaderboard-only); Val. = val-
idation method.                                          The Quran track comprises 2,013 four-way
                                                         multiple-choice questions covering all 114 surahs
                                                         (S). Sourced from standard Arabic Quranic text,
a benchmark that measures LLMs knowledge of              the dataset underwent normalization (e.g., removal
Islamic content.                                         of diacritics and kashida; uniﬁcation of Alef and
   PalmX (Al-Wajih et al., 2025) addresses cul-          Ya forms) following (Darwish and Magdy, 2014).
tural competence including an Islamic culture sub-       To ensure validity, all questions pass a program-
task. QIAS (Bouchekif et al., 2025) covers Is-           matic uniqueness constraint to prevent duplicate
lamic inheritance reasoning. FiqhQA (Atif et al.,        candidates or distractors matching the ground
2025) introduces 960 question-answer pairs cate-         truth.
gorised by school but relies on synthetically gen-          Verse (Ayah) Count (114 questions, 6%): This
erated answers from a single LLM, raising con-           task evaluates factual recall of surah lengths. Dis-
cerns about circular evaluation. IslamicLegal-           tractors are selected via a structured strategy: (1)
Bench (Elmahjub et al., 2026) provides 718 man-          ground truth; (2) subsequent S count; (3) preced-
ually curated instances across seven schools of          ing S count; and (4) a random S count. If pre-
jurisprudence, measuring legal reasoning depth.          ceding or subsequent counts match the target, we
QuranQA (Malhas and Elsayed, 2022) establishes           apply an incremental offset (±2) to maintain four
reading comprehension benchmarks for Quranic             unique candidates.
text. IslamTrust (Lahmar et al., 2025) evaluates            Surah Identiﬁcation (833 questions, 41%):
alignment with consensus Islamic ethics, achiev-         Models must identify the source S of a given verse.
ing only 66.5% alignment with GPT-4.                     To prioritize contextual reasoning over keyword
   Despite these initiatives, a signiﬁcant gap re-       matching, we only include verses with a Jaccard
mains for a comprehensive benchmark and leader-          similarity index J > 0.4 relative to at least one
board that systematically evaluates LLM perfor-          verse in a different S. We employ hard-negative
mance across diverse Islamic domains and mea-            mining to select: (1) the ground truth S; (2) the
sures potential bias toward various schools of Fiqh.     nearest-neighbor S containing the most lexically
IslamicMMLU is designed to address this gap (see         similar verse; and (3-4) two randomly sampled
Table 1).                                                surahs.
                                                            Verse Retrieval (1,066 questions, 53%): This
3    Data Preparation Methodology
                                                         task requires mapping a verse index V to its tex-
IslamicMMLU follows the MMLU paradigm: 4-                tual content within Surah S. To increase linguis-
option MCQ, standardised Arabic prompts, and             tic complexity, V is stochastically represented as
zero-shot evaluation. All questions are gener-           either a numeric digit or its Arabic textual equiva-
ated from native Arabic content sourced from             lent. We ﬁlter for verses with J > 0.4 across the
authoritative Islamic texts (not translated from         corpus and construct adversarial choices: (1) the
English), programmatic question generation with          ground truth (max 10 words); (2) the most lexi-
quality veriﬁcation, and domain-expert review            cally similar verse in the corpus; (3) a positional
when needed. IslamicMMLU consists of three               distractor at an offset of ±2 from V within S;
main tracks, each differ in source material, ques-       and (4) a "null response" indicating "No verse at
this position." The latter acts as the correct answer   of questions between the four levels of authentic-
for trap questions where V exceeds the total verse      ity, where fabricated ones were taken from a set of
count of S, speciﬁcally testing for model halluci-      Arabic poems as distractors.
nation and boundary awareness.
                                                        3.3 Fiqh Track
3.2   Hadith Track                                      The Fiqh track utilised the encyclopedia book
The Hadith track comprises 4,000 questions span-        "Jurisprudence According to the Four Schools"
ning the six canonical Sunni collections (Kutub al-     by ‘Abd al-Rahman al-Jaziri, commissioned by
Sittah) The dataset employs a deterministic gen-        Al-Azhar University. The complete text spans
eration pipeline with ﬁxed random seeds for full        2,221 pages across 1,043 sections covering eight
reproducibility.                                        ﬁqh categories. We extract a structured corpus
                                                        of 2,163 rulings across 797 topics using a multi-
Preprocessing. Raw hadith texts undergo the             agent pipeline with adversarial veriﬁcation (Fig-
same standard Arabic text normalisation applied         ure 1a): a content classiﬁcation stage (GPT-4.1)
to Quran text; Critically, the isnad (chain of narra-   ﬁrst ﬁlters the 1,043 sections, ﬁnding that approxi-
tors) is trimmed from each hadith before question       mately 60% contain extractable ﬁqh rulings while
generation to prevent models from trivially iden-       the remaining 40% are meta-commentary, philo-
tifying the source collection from narrator names       sophical discussion, or cross-references. Three
rather than demonstrating genuine content knowl-        models (GPT-4.1 in structured output mode, GPT-
edge, forcing models to identify collections from       4o, and GPT-5.1) then extract in parallel, produc-
the matn, the main content alone. Cross-collection      ing typed records with per-madhab rulings, legal
ﬁltering removes near-identical narrations appear-      classiﬁcations, structural components (pillars, con-
ing in multiple collections with different attribu-     ditions, obligations), and evidence chains. En-
tions.                                                  semble voting via fuzzy-matching alignment re-
                                                        solves disagreements by majority agreement. A
Question Types. The track tests four facets of
                                                        separate reasoning model (o1) performs adver-
Hadith knowledge:
                                                        sarial veriﬁcation against the source text, check-
   Source Identiﬁcation (1,000 questions): Given a
                                                        ing madhab attribution, ruling content, numeri-
hadith text with the isnad removed, identify which
                                                        cal counts, and uniqueness claims: 85% of ex-
canonical collection it belongs to. This is applied
                                                        tractions pass directly, 12% enter iterative reﬁne-
to Hadith that appeared in only one of the six
                                                        ment via o3, and 3% are rejected outright. The
books. Distractors are other collections.
                                                        corpus maintains near-uniform madhab represen-
   Cloze Completion (1,000 questions): Fill in a        tation (approximately 25% per school).
missing keyword from a hadith text. Target words           From this corpus, we generate 4,000 questions
are selected via IDF weighting to ensure the blank      across ﬁve types (Section 4; Figure 1b). Distrac-
tests substantive vocabulary rather than common         tor selection varies by type: for ruling identiﬁca-
particles. Distractors are synonyms to the hidden       tion, distractors are rulings from other schools or
word generated by an LLM (GPT4o).                       plausible variations; for bias detection, all options
   Chapter Classiﬁcation (1,000 questions): Given       are correct (one per school); for multi-hop reason-
a hadith from a given collection, identify which        ing, distractors are partial-reasoning answers. An-
chapter (topic) within the collection it belongs to     swer option order is randomised across all ques-
(e.g., Prayer, Fasting). This is the most challeng-     tion types.
ing type, as it requires mapping narrative content
to taxonomic labels rather than keyword matching.       Quality Veriﬁcation. Each question undergoes
   Authenticity Grading (∼1,000 questions): As-         automatic veriﬁcation against ﬁve criteria: source
sess the reliability grade of a hadith {authentic,      traceability, madhab accuracy, linguistic correct-
good, weak, fabricated}. This carries the high-         ness, distractor validity, and coverage balance. Ad-
est practical stakes, as incorrect grading can af-      ditionally, 213 stratiﬁed question samples with
fect which narrations are used for deriving Is-         their answers were manually reviewed by a pro-
lamic rulings. Items where narrations appear near-      fessor in comparative jurisprudence at Al-Azhar
identically across collections with different grades    University. The reviewer approved 207 of 213
are ﬁltered to reduce ambiguity. We split this set      questions (97.2%), with three requiring minor re-
visions and three rejected for factual errors (two     Comparative Fiqh (780 questions). Questions
madhab misattributions, one insufﬁcient source         requiring identiﬁcation of points of agreement or
grounding). While the use of a single reviewer lim-    divergence across schools. Representative exam-
its generalisability, the high approval rate across    ples for all question types appear in Appendix E
all ﬁve question types provides reasonable conﬁ-
dence in question quality.                             4.1 Madhab Bias Detection Methodology
   Figure 1 presents the two core pipeline archi-      The bias detection task exploits the inherent plu-
tectures for the Fiqh track: (a) the multi-agent       ralism of Sunni jurisprudence. Because all four
extraction pipeline that converts al-Jaziri’s source   schools are equally valid within the tradition,
text into a structured corpus, and (b) the question    no answer is “wrong” in the conventional sense.
generation pipeline that produces the 4,000 bench-     When a model selects an option, it implicitly en-
mark questions from that corpus.                       dorses that school’s position. By aggregating re-
                                                       sponses across 800 questions, we measure whether
4   Fiqh Question Design and Bias                      models exhibit systematic preferences. A model
    Methodology                                        with no madhab bias would show approximately
The 3,200 knowledge questions and 800 bias de-         25% selection rate for each school; signiﬁcant de-
tection questions span eight ﬁqh categories propor-    viation, measured via chi-squared test against the
tional to the source corpus: prayer (34%), family      uniform distribution, indicates implicit preference.
law (20%), ethics (16%), tahara (12%), hajj (6%),      Answer order is randomised across questions to
criminal law (5%), fasting (5%), and zakat (3%).       prevent positional bias.
Five question types test distinct facets of Islamic       This extends bias measurement from the inter-
legal reasoning:                                       cultural axis studied by Naous et al. (2024)
                                                       (Western vs. Islamic norms) to the intra-tradition
Madhab Ruling Identiﬁcation (820 questions).           axis (preferences among equally legitimate Sunni
Given a ﬁqh topic and a speciﬁed madhab, se-           schools). The distinction matters practically: a
lect the correct ruling from four options. Distrac-    user following the Maliki school who receives
tors are populated with rulings from other schools     Hanbali-biased responses may adopt rulings their
or plausible variations. Example: “What is the         own tradition does not endorse.
Shaﬁ’i position on congregational prayer for the
ﬁve obligatory prayers?” Correct: Communal             5 Ranking LLMs according to
obligation (fard kifaya). Distractors: Maliki (rec-      IslamicMMLU
ommended), Hanbali (individual obligation).
                                                       5.1 Evaluation Protocol
Multi-Hop Reasoning (810 questions). Ques-             We evaluate 26 models across four tiers: fron-
tions requiring synthesis of multiple corpus facts     tier (10 models including Gemini 3, GPT-5 series,
to reach the correct answer. For example, deter-       Claude 4.5), mid-tier (8 models including GPT-
mining whether an act invalidates prayer may re-       4o, Llama 4, DeepSeek v3), Arabic-specialised
quire knowing both the ruling’s classiﬁcation and      (5 models: Fanar-Sadiq, Fanar, Fanar-C-2-27B,
its structural role (pillar vs. condition).            Jais-2-70B, ALLaM-7B), and baselines (3 models
Madhab Bias Detection (800 questions). All             including GPT-4 and GPT-3.5-turbo); full model
four answer options are valid, each representing       speciﬁcations appear in Appendix A. All mod-
the correct ruling from a different madhab. The        els receive identical Arabic prompts (Appendix B)
question avoids any school speciﬁcation, asking        with zero-shot instructions, temperature set to 0
simply “What is the ruling on [topic]?” A model’s      for deterministic output, and single-letter response
selection reveals which school it defaults to when     format (A, B, C, or D). Invalid responses are
unconstrained.                                         marked incorrect.
                                                          The overall score is the equally weighted aver-
Component Parsing (790 questions). Ques-               age of a model’s accuracy across the three tracks.
tions asking models to classify sub-actions as pil-    Equal weighting reﬂects the design principle that
lars (arkan), conditions of validity (shurut sihha),   each track represents a distinct Islamic knowledge
conditions of obligation (shurut wujub), or recom-     domain of equal scholarly importance, regardless
mended acts (sunan).                                   of question count. We note that alternative weight-
                                  extraction                                                                                            veriﬁcation

  source                                                      yes (60%)                                    ensemble             o1 veriﬁcation                    pass (85%) database
                     content                                                    multi-model
                                                 usable?                                                                                                 pass?
  section         classiﬁcation                                                  extraction                 voting                  judge                                    storage
                    (GPT-4.1)                         no (40%)            GPT-4.1 | GPT-4o | GPT-5.1                                                         fail (12%)


                                               skip section                                                                                           o3 reﬁnement


(a) Multi-agent extraction pipeline. Three models extract in parallel with ensemble voting, followed by o1 veriﬁcation and o3
reﬁnement for failed extractions.

                  generation


                                                                      ruling ID
                                                                                                                           validation
   corpus         ruling                 type-speciﬁc                multi-hop
  database       selection                 generator                                          LLM                              yes                                   yes checkpoint
                                                                                                                 rule                   LLM quality     accept?
                                                                     bias detect            generation                                                                     + export
  ﬁqh corpus   topic + madhab                                                                                   valid?                    check
                                                                    component                 GPT-5.1                                                        no
                                                                                                                      no

                                                                    comparative                                                                          revise
                                                                                                                discard


(b) Question generation pipeline. Rulings are routed to type-speciﬁc generators, producing candidates via GPT-5.1. Each
question undergoes rule-based validation followed by LLM quality check before inclusion.

Figure 1: Fiqh track pipeline architectures. (a) Extraction of structured rulings from al-Jaziri’s source text. (b) Gen-
eration and validation of benchmark questions from the structured corpus.
ing schemes (e.g., proportional to question count)                                                      tween the top model and the GPT-3.5-turbo base-
would produce slightly different rankings; per-                                                         line (39.75%) conﬁrms that the benchmark distin-
track scores are reported for researchers prefer-                                                       guishes model capabilities effectively above the
ring different aggregation methods. For the Fiqh                                                        25% random baseline ﬂoor.
track, models are evaluated on the 3,200 knowl-
edge questions; the 800 bias detection questions                                                        5.3 Per-Track Analysis
are scored separately as they have no single correct                                                    Performance varies substantially across tracks
answer. The random baseline for 4-choice MCQ is                                                         (per-task breakdowns in Table 4). The Quran track
25%.                                                                                                    has the widest spread: 99.25% (Gemini 3 Flash) to
Statistical Methodology. Because all models                                                             32.44% (GPT-3.5-turbo), a 66.8-point gap. Four
are evaluated with temperature 0 (deterministic),                                                       models exceed 95%, yet weaker models score well
run-to-run variance is zero and repeated trials are                                                     below 50%, making it the most discriminative do-
unnecessary. However, accuracy on a ﬁnite test set                                                      main. The Hadith track spans 93.00% to 41.64%
has inherent sampling uncertainty. We compute                                                           (51.4 points), and the Fiqh track spans 89.06% to
bootstrap conﬁdence intervals (1,000 resamples of                                                       45.16% (43.9 points).
question-level correct/incorrect vectors) for all re-                                                      Cross-track discrepancies reveal model-speciﬁc
ported accuracies. McNemar’s test on question-                                                          strengths. Claude Opus 4.5 achieves strong Quran
level agreement can be applied to the question-                                                         (94.6%) and Hadith (90.8%) scores but notably
level data for pairwise comparisons; as an ex-                                                          weaker Fiqh (72.7%), suggesting difﬁculty with
ample, the difference between Gemini 3 Flash                                                            comparative reasoning. Fanar-Sadiq scores 94.4%
(93.8%) and Gemini 3 Pro (92.3%) is statistically                                                       on Quran (competitive with frontier models) but
signiﬁcant (McNemar’s χ2 =12.4, p<0.001), con-                                                          only 72.9% on Hadith, indicating uneven domain
ﬁrming that the 1.5-point gap is not attributable to                                                    coverage. These patterns demonstrate the value of
sampling variation.                                                                                     multi-track evaluation: a single aggregate score
                                                                                                        obscures important domain-speciﬁc capabilities
5.2     Overall Results                                                                                 and weaknesses.
Table 3 presents accuracy for all 26 evaluated
models across all three tracks. Gemini 3 Flash                                                          5.4 Arabic-Speciﬁc Models
achieves the highest overall accuracy (93.77%),                                                         Arabic-specialised models show mixed results.
followed by Gemini 3 Pro (92.32%) and Gemini                                                            Fanar-Sadiq (Fanar Team et al., 2025) (81.56%)
2.5 Pro (90.34%). Google models dominate the                                                            performs competitively, likely beneﬁting from
top three positions. GPT-5 (89.92%) is the top                                                          its specialised Islamic retrieval-augmented gener-
non-Google model; Claude Sonnet 4.5 (86.15%)                                                            ation system. Jais-2-70B (63.4%) and ALLaM-
is the top Anthropic model. The 54-point gap be-                                                        7B (59.5%) rank in the lower-mid tier despite their
                                                                                                                   0           Han.   Mal.   Sha.   Hba.
                                                                                     Gem. 3 Flash
 Gem. 3 Flash (93.8)                                                                  Gem. 3 Pro
                                       Quran
   Gem. 3 Pro (92.3)                                                                     GPT-5.2
                                       Hadith
 Gem. 2.5 Pro (90.3)                                                                 Gem. 2.5 Pro
                                       Fiqh
        GPT-5 (89.9)
                                                                                                                                                     frontier
                                                                                      Cl. Son. 4.5
      GPT-5.2 (89.5)                                                                       GPT-5
      GPT-5.1 (88.4)
                                                                                   Gem. 2.5 Flash
   Cl. Son. 4.5 (86.2)
                                                                                         GPT-5.1
  Cl. Opus 4.5 (86.0)
                                                                                      Cl. 3.7 Son.
Gem. 2.5 Flash (83.1)
                                                                                     Cl. Opus 4.5
   Cl. 3.7 Son. (82.3)
                                                                                          GPT-4o
 Fanar-Sadiq (81.6)
                                                                                         GPT-4.1
       GPT-4o (77.3)
                                                                                   DeepSeek v3.2
      GPT-4.1 (75.6)

                                                                                                                                                     mid-tier
      Grok 4.1 (72.9)                                                                    Grok 4.1
DeepSeek v3.2 (68.5)                                                                   Ll. 4 Scout
    Ll. 4 Mav. (66.7)                                                                  Ll. 4 Mav.
        Fanar (66.0)                                                               DeepSeek v3.1
 Cl. Haiku 4.5 (65.4)                                                               Cl. Haiku 4.5
DeepSeek v3.1 (65.4)                                                                  Fanar-Sadiq
   Jais-2-70B (63.4)
                                                                                                                                                     arabic
                                                                                       Jais-2-70B
    Ll. 4 Scout (59.6)                                                                ALLaM-7B
        GPT-4 (59.6)                                                                        Fanar


                          25% random
  ALLaM-7B (59.5)
                                                                                           GPT-4
 Cl. 3.5 Haiku (57.5)
                                                                                                                                                     baseline
                                                                                    Cl. 3.5 Haiku
      Fanar-C (54.0)
                                                                                         Fanar-C
GPT-3.5-turbo (39.8)
                                                                                    GPT-3.5-turbo
                         20                     40       60         80   100
                                                                                                     -10    -5       0      5   10    15      20
                                                     Accuracy (%)                                          deviation from 25% (∆%)

            (a) Per-track accuracy for all 26 models sorted by overall         (b) Madhab selection deviation from uniform 25% on 800
            score. Arabic-speciﬁc models in bold.                              bias detection questions.

        Figure 2: Model evaluation results. (a) Per-track accuracy with cross-track spread. (b) Madhab bias: dots near the
        centre line indicate balanced school selection.
        large-scale Arabic pretraining, with both showing                      Bias–Accuracy Relationship. A moderate neg-
        notably strong Hadith performance (77.8% and                           ative correlation exists between accuracy and bias
        70.9%) but weak Quran scores (48.1% and 43.2%).                        magnitude (Pearson r=−0.38, p=0.049; Spear-
        Fanar (66.0%) and Fanar-C-2-27B (54.0%) score                          man ρ=−0.53, p=0.005), suggesting higher-
        lower still, clustering with or below general-                         performing models tend toward more balanced
        purpose mid-tier models despite their Arabic-                          school selection. However, notable exceptions
        speciﬁc training. Arabic pretraining alone ap-                         exist (some high-accuracy models show elevated
        pears insufﬁcient for Islamic knowledge; domain-                       bias), indicating that capability improvements
        speciﬁc training data and retrieval augmentation                       alone do not guarantee fairness within traditions.
        matter more than language coverage.
                                                                               5.6 Error Analysis
        5.5        Madhab Bias Analysis
                                                                               Fiqh. Qualitative examination of Fiqh errors re-
        For the 800 Fiqh bias detection questions, we mea-
                                                                               veals three recurring patterns. Madhab confusion:
        sure each model’s selection distribution across the
                                                                               models return rulings from an incorrect school
        four schools. Figure 2b visualises the deviation
                                                                               when a speciﬁc madhab is speciﬁed, indicating
        from uniform 25% selection for all 26 models.
                                                                               difﬁculty with school-speciﬁc retrieval. Multi-
        Variable Bias. Unlike cultural bias studies                            hop reasoning failure: questions requiring syn-
        showing consistent Western skew (Naous et al.,                         thesis of multiple facts (e.g., determining conse-
        2024), madhab preferences are model-speciﬁc.                           quences of omitting a pillar vs. violating a con-
        Gemini 3 Flash shows near-uniform distribution                         dition) show the largest frontier-to-baseline gap
        (χ2 =0.32, p>0.9), while GPT-5.1 signiﬁcantly                          (87.2% vs. 41.1%). Comparative difﬁculty: Com-
        favours Hanbali (35.6%). Arabic-speciﬁc models                         parative Fiqh questions achieve the lowest top-
        show moderate Hanaﬁ preference (32–33%), pos-                          model accuracy (76.7%), as cross-school synthe-
        sibly reﬂecting Gulf training data where Hanaﬁ                         sis demands tracking divergent positions. We note
        jurisprudence predominates. With 26 indepen-                           that per-type accuracy differences should be inter-
        dent tests, we apply Bonferroni correction (αadj =                     preted with caution for Comparative Fiqh (n=780)
        0.05/26 = 0.0019); only Claude Opus 4.5                                and Component Parsing (n=790), where smaller
        (χ2 =16.06) retains signiﬁcance after correction.                      question pools yield wider conﬁdence intervals
    Model            Overall Quran Hadith Fiqh           leaderboard on HuggingFace.2 The platform en-
    Gemini 3 Flash    93.8   99.3    93.0   89.1         ables evaluation of models by providing an API
    Gemini 3 Pro      92.3   97.3    91.7   87.9         key and model identiﬁer; the platform runs the full
    Gemini 2.5 Pro    90.3   95.8    89.7   85.5
    GPT-5             89.9   98.0    88.2   83.5
                                                         pipeline automatically and publishes results to a
    GPT-5.2           89.5   94.8    87.8   85.9         public dataset.
    GPT-5.1           88.4   95.3    88.3   81.5            All 10,013 questions follow a standardised four-
    Cl. Sonnet 4.5    86.2   88.2    85.4   84.9
    Cl. Opus 4.5      86.0   94.6    90.8   72.7         option MCQ format with consistent metadata
    Gem. 2.5 Flash    83.1   82.4    83.8   83.1         (track, category, question type, difﬁculty level).
    Cl. 3.7 Sonnet    82.3   81.0    84.9   81.1         This standardised structure is designed for exten-
    Fanar-Sadiq       81.6   94.4    72.9   77.4         sibility: additional Islamic knowledge domains –
    GPT-4o            77.3   71.3    82.0   78.5         such as aqidah (creed), sirah (prophetic biogra-
    GPT-4.1           75.6   68.0    81.3   77.5
    Grok 4.1 Fast     72.9   79.1    65.6   74.0         phy), or tafsir (Quranic exegesis) – can be added
    DeepSeek v3.2     68.5   60.1    71.1   74.3         as new tracks without modifying the evaluation
    Ll. 4 Maverick    66.7   56.3    73.5   70.3
    Fanar             66.0   56.9    66.5   74.5
                                                         infrastructure. The leaderboard provides rank-
    Cl. Haiku 4.5     65.4   53.8    73.1   69.4         ings, analytics including madhab bias visualisa-
    DeepSeek v3.1     65.4   55.3    71.0   69.8         tions, and side-by-side model comparison across
    Jais-2-70B        63.4   48.1    77.8   64.4
    Ll. 4 Scout       59.6   43.3    64.9   70.6         all tracks and question types.
    GPT-4             59.6   42.9    68.4   67.4
    ALLaM-7B          59.5   43.2    70.9   64.5         7 Conclusion and Future Work
    Cl. 3.5 Haiku     57.5   47.3    62.8   62.4
    Fanar-C-2-27B     54.0   41.9    60.7   59.5         We introduced IslamicMMLU, a comprehensive
    GPT-3.5-turbo     39.8   32.4    41.6   45.2         benchmark of 10,013 questions across 12 tasks
                                                         covering the Quran, Hadith, and Fiqh. Our eval-
Table 3: IslamicMMLU accuracy (%) for all 26 mod-        uation of 26 LLMs demonstrates the benchmarks
els. Arabic-speciﬁc models in bold. Fiqh accuracy is     strong discriminative power, revealing a 54-point
on the 3,200 knowledge questions (800 bias detection     performance gap between frontier and legacy mod-
questions scored separately). Per-question-type break-
                                                         els. Notably, we ﬁnd a signiﬁcant correlation be-
downs are in Table 4.
                                                         tween model capability and reduced madhab bias,
                                                         suggesting that advanced reasoning may naturally
than the larger Ruling Identiﬁcation (n=820) and         mitigate intra-tradition skew.
Multi-Hop (n=810) sets.                                     Future work will expand this framework by in-
                                                         corporating Shia jurisprudence to ensure broader
Quran. The wide performance spread on this               representation. Furthermore, we aim to extend
track suggests Quranic textual knowledge is highly       the MMLU paradigm to additional domains. By
discriminative: models either have extensive expo-       releasing our evaluation suite an