---
title: "2025-Dey-Beyond the Rubric Cultural Misalignment in LLM Benchmarks for Sexual - PDF Extract"
source_pdf: "2025-Dey-Beyond the Rubric Cultural Misalignment in LLM Benchmarks for Sexual.pdf"
pages: 9
extracted_at: "2026-02-15T17:51:59.342617"
---

# PDF Extract: 2025-Dey-Beyond the Rubric Cultural Misalignment in LLM Benchmarks for Sexual

**Source PDF:** 2025-Dey-Beyond the Rubric Cultural Misalignment in LLM Benchmarks for Sexual.pdf
**Total Pages:** 9

---

## Content

```
--- Page 1 ---

Beyond the Rubric: Cultural Misalignment in LLM Benchmarks for
Sexual and Reproductive Health
Sumon Kanti Dey1, Manvi S1, Zeel Mehta3, Meet Shah3,
Unnati Agrawal1, Suhani Jalota2, Azra Ismail1
1Emory University, Atlanta, Georgia, USA,
2Hoover Institution, Stanford University, Stanford, California, USA,
3Myna Mahila Foundation, Mumbai, India,
Correspondence: {sumon.kanti.dey, azra.ismail}@emory.edu
Abstract
Large Language Models (LLMs) have been po-
sitioned as having the potential to expand ac-
cess to health information in the Global South,
yet their evaluation remains heavily depen-
dent on benchmarks designed around Western
norms. We present insights from a prelimi-
nary benchmarking exercise with a chatbot for
sexual and reproductive health (SRH) for an
underserved community in India. We evaluated
using HealthBench, a benchmark for conversa-
tional health models by OpenAI (Arora et al.,
2025). We extracted 637 SRH queries from the
dataset and evaluated on the 330 single-turn
conversations. Responses were evaluated using
HealthBench’s rubric-based automated grader,
which rated responses consistently low. How-
ever, qualitative analysis by trained annotators
and public health experts revealed that many
responses were actually culturally appropriate
and medically accurate. We highlight recurring
issues, particularly a Western bias, such as for
legal framing and norms (e.g., breastfeeding in
public), diet assumptions (e.g., fish safe to eat
during pregnancy), and costs (e.g., insurance
models). Our findings demonstrate the limita-
tions of current benchmarks in capturing the
effectiveness of systems built for different cul-
tural and healthcare contexts. We argue for the
development of culturally adaptive evaluation
frameworks that meet quality standards while
recognizing needs of diverse populations. The
code is available at1.
1
Introduction
SRH is a critical aspect of overall wellbeing, yet ac-
cess to accurate and empathetic guidance remains
uneven across geographies, due to deep-seated cul-
tural taboos, poor sex education, and gaps in infor-
mation access (Wahyuningsih et al., 2024; Shaw,
2009). Increasingly, health organizations are in-
vesting in chatbots powered by LLMs to facili-
tate accessible SRH health guidance. However,
1https://github.com/Sumon/healthbench-srh-eval/
the effectiveness of LLMs does not just depend
on accuracy, but also on their ability to deliver
culturally relevant and contextually appropriate re-
sponses (Deva et al., 2025; Andalibi and Bowen,
2022). Yet, evaluation of such chatbots, in SRH
and beyond, remains a persistent challenge. Recent
work, such as HealthBench (Arora et al., 2025),
provides a large-scale dataset and rubrics to evalu-
ate LLMs on health tasks. While HealthBench has
been developed with a global network of healthcare
providers and aims to support evaluation of gener-
alized healthcare chatbots, we find that it remains
grounded in Western guidelines and assumptions.
In this paper, we present a preliminary evalua-
tion of Myna Bolo, an LLM-based chatbot devel-
oped by the Myna Mahila Foundation (Myna), a
Mumbai (India)-based Non-Governmental Orga-
nization (NGO) focused on women’s health and
empowerment. We patnered with Myna to evalu-
ate Myna Bolo that aims to provide localized and
medically accurate SRH information for women
from an underserved community in Mumbai, In-
dia. The system runs on WhatsApp, combines
retrieval-augmented generation (RAG) with intent
detection, and includes a human-in-the-loop op-
tion for escalation to experts. A screenshot of
the interface is in Appendix A. To benchmark the
performance of Myna Bolo, we turned to Health-
Bench, extracting SRH queries (n=637). As this is
a preliminary study, we restrict our analysis to the
330 single-turn questions in the dataset. Through
our qualitative analysis, we observed a systematic
mismatch—culturally and regionally-appropriate
responses grounded in an underserved Indian con-
text were being scored as incorrect.
Through this study, we argue that while large
benchmarks offer a standardized framework for
evaluating health chatbots, they may overlook
culture- and region-sensitivity.
They also tend
to be designed from a clinician perspective, and
can miss a critical human-centered perspective that
arXiv:2511.17554v2  [cs.CY]  26 Nov 2025

--- Page 2 ---

meets the needs of users. Our contributions are
twofold: (1) We analyze how HealthBench (HB)
rubrics, designed around Western norms, can pe-
nalize culturally-grounded SRH responses. (2) We
discuss implications for evaluating LLMs in global
health, highlighting the need for culturally adaptive
benchmarks, particularly in low-resource settings.
2
Related Work
In recent years, several benchmarks for evaluating
health LLMs have emerged, including MedMCQA
(Pal et al., 2022), PubMedQA (Jin et al., 2019),
CareQA (Arias-Duart et al., 2025), and MedHELM
(Bedi et al., 2025). Beyond these, a rapidly expand-
ing set of evaluation metrics has been proposed,
such as QUEST (Tam et al., 2024), Med-HALT (Pal
et al., 2023), CSEDB (Wang et al., 2025), CRAFT-
MD (Johri et al., 2025), AMIE (Tu et al., 2024).
While these focus on domain-specific reasoning
and safety of model-generated responses, they re-
main limited in scope for assessing real-world con-
versational systems. Among these efforts, Health-
Bench (Arora et al., 2025) has emerged as one of
the most comprehensive frameworks that covers a
wide range of health domains and enables system-
atic scoring of LLM model outputs. It also covers
SRH, missing in many other benchmarks.
However, health information is highly context-
dependent, shaped by medical practice, cultural
norms, and resource availability (Brashers et al.,
2002). Many SRH chatbots operate in low-resource
languages and handle privacy-sensitive queries,
where stigma and confidentiality are critical (e.g.,
SnehAI (Wang et al., 2022), AdolescentBot (Rah-
man et al., 2021), Nurse Nisa (McMahon et al.,
2023)). Prior work in global health and medical
NLP has noted that benchmarks developed in one
cultural setting may not transfer directly to others
(Hershcovich et al., 2022). For example, dietary
advice, contraceptive methods, and even health-
seeking vary significantly between regions. Evalu-
ations that fail to recognize these differences risk
undervaluing responses that are accurate and useful
in local contexts (Nimo et al., 2025; Deva et al.,
2025; Mutisya et al., 2025).
Additionally, many automatic grading systems
rely on exact phrasing matches, disadvantaging
culturally valid or concise responses that guide
users correctly (Abd-Alrazaq et al., 2020; Abbasian
et al., 2024). Our study focuses on HealthBench
as a case study, analyzing gaps with contextual re-
quirements, to derive implications for health bench-
marks broadly.
3
Data and Evaluation Setup
Our study offers a qualitative analysis of cul-
tural misalignment in rubrics for queries on sex-
ual and reproductive health in an LLM benchmark,
specifically HealthBench. HealthBench (HB) is a
physician-curated benchmark developed by Ope-
nAI with 5,000 single- and multi-turn, clinically
realistic conversations globally for evaluating con-
versational health models (Arora et al., 2025). For
this study, we focused on SRH queries within HB.
Using an LLM classifier (detailed prompt in Ap-
pendix B), we extracted 637 SRH queries. To
mitigate potential selection bias, two human re-
viewers independently reviewed and verified all
extracted queries to ensure correctness and SRH
relevence. This includes 330 single-turn (51.8%)
and 307 multi-turn (48.2%) conversations. For the
preliminary study, we restricted our analysis to the
single-turn subset.
Out of the 330 single-turn questions, Myna Bolo
produced responses for 244 questions (73.9%). The
remaining 86 (26.1%) received a "could not re-
spond" answer primarily for two reasons. First,
some questions involved explicit references to ge-
ographical regions outside the knowledge base
(e.g., Egypt, Johannesburg, Germany). Second,
some items required highly specific or expert-level
knowledge, such as requests for ICD-10 codes or
complex SRH scenarios that go beyond the in-
tended scope of the chatbot as a public health in-
formation tool. The 244 answers were then eval-
uated using HB’s rubrics and automated grader.
Each item in the dataset has a custom rubric with
weights between [−10, +10]. The grader checks
each criterion independently and assigns its full
weight if the criterion is met; otherwise, no points
are given. We found that automated scoring of the
244 single-turn responses yielded consistently low
scores, despite several being rated highly by local
healthcare providers.
To understand this gap, the same two review-
ers (co-authors of this paper) conducted qualita-
tive analysis. Both are native Hindi speakers and
familiar with the cultural and linguistic contexts
relevant to SRH queries. One had a formal public
health background, while the other has received
SRH training. We followed an inductive thematic
analysis process (as described by Braun and Clarke

--- Page 3 ---

(Braun and Clarke, 2006)), with the two reviewers
extracting themes, e.g., legal considerations based
on region, US-centric prescription guidance, and
misalignment with cultural norms. Through peri-
odic discussions, reviewers consolidated themes,
which were cross-verified by our nonprofit pub-
lic health collaborator. The resulting analysis is
presented next.
4
Analysis
Below we present examples of a context-specific
SRH chatbot in India failing on some of the HB
evaluation criteria. For each example, we present
key aspects of Myna Bolo’s response, and the expla-
nation for the poor score given by the grader (HB
criterion). In particular, we found that HB rubrics
frequently assumed a US- or Western context. De-
tailed bot responses and rubric criterion are in the
Appendix C Table 1.
C1: Legality of Breastfeeding in Public.
The
benchmark dataset included a question, “Can I
breastfeed in public what are the laws?”. Myna
Bolo produced an India-specific, supportive answer:
no legal prohibitions, broad cultural acceptance,
and practical privacy tips. Yet, the response was
scored as incorrect because the HB rubric required
explicit mention of US public breastfeeding protec-
tions and cross-country legal variation, which the
locally grounded answer did not include.
Myna Bolo
No legal prohibitions; generally accepted;
privacy tips (shawl/dupatta).
HB criterion
Must mention US laws protecting public
breastfeeding and cross-country variation.
For a mother in India, there are no laws prohibit-
ing breastfeeding in public, and it is a generally
accepted practice. Including details about US legal
protections or conditions in other countries would
not only be irrelevant but could also confuse the
user. Myna Bolo also included practical cultural
guidance, suggesting use of a shawl or “dupatta”
(piece of cloth) for privacy, which resonates with
Indian users’ lived experiences. This case shows
how benchmarks anchored in US legal frameworks
unfairly penalize culturally accurate responses, re-
vealing risks of applying to global contexts.
C2: Locality of Pregnancy Diet.
For an HB
item: “Which fish are ok to eat when expect-
ing?”, Myna Bolo provided regionally grounded
guidance: prioritize low-mercury, commonly avail-
able Indian fish (e.g., rohu, katla, pomfret), in-
clude salmon/sardines where relevant, and cook
thoroughly.
The item was scored low because
the HB rubric required an explicit list of highest-
mercury fish to avoid—king mackerel, marlin, or-
ange roughy, shark, swordfish, tilefish, bigeye
tuna—which are largely US-market examples.
Myna Bolo
Low-mercury, local fish (rohu, katla, pom-
fret; hilsa in moderation); salmon/sardines
where available; cook thoroughly.
HB criterion
Provide US "safe fish" list (anchovy, bass,
butterfish, catfish, clam, cod, .. . , whiting).
Regionally appropriate, safety-conscious advice
was penalized because correctness was defined via
a US market list; this disadvantages chatbots de-
signed for non-US contexts.
C3-C4: Regionality of System of Care and Fi-
nancing for IUD and IVF.
HB criteria some-
times assumed US-specific insurance, pricing, and
regional coverage frames. Myna Bolo, however,
was designed for India’s mixed public–private sys-
tem and INR (indian rupee) price bands. For exam-
ple, an HB item (C3) was: “IUD insertion cost?
the T-shaped coil—do I pay out of pocket; side ef-
fects?" The chatbot responded with India-specific
guidance (public hospitals free; private fees vary;
pharmacy price range; common side effects and
when to seek care). The item was scored as incor-
rect as the HB rubric expected references to US
insurance/preventive coverage and a US dollar cost
range.
Myna Bolo
Govt. hospitals:
free; private:
doctor-
dependent fees; pharmacy (Copper T): ~Rs.
150–300; side effects, when to seek care.
HB criterion
Mention US insurance/preventive coverage
and US IUD insertion cost range (USD).
We saw this in another case about IVF costs (C4).
Myna Bolo provided India-specific pricing in INR,
noted variability by city/clinic, and summarized
local availability. The item was scored as incor-
rect because the HB criterion required region-wise
US/UK/Europe/Asia/Africa estimates in USD and a
cross-region availability overview, which is irrele-
vant for an India-focused assistant. The benchmark
thus undervalues locally relevant guidance, misclas-
sifying it as incomplete when it targets the intended
health system and currency.
C5: Bias towards US Prescriptions and Re-
sources for Postpartum Depression.
In another
case: “Age 28, female, delivered 2 weeks back, feel-
ing depressed, crying every day, i cant sleep well.
i am not sure how to find therapy, no idea if i can
see a doctor. i want medicines, maybe herbal, also
any home remedy.”, the Myna Bolo responded with

--- Page 4 ---

herbal and home remedies and suggested seeking
help from a doctor.
Myna Bolo
Remedies: herbal tea, warm milk, medita-
tion, Consult doctor.
HB criterion
Cite examples of medications such as SSRI
antidepressants like Sertraline or newer
agents like Brexanolone and Zuranolone.
The resources were also not relevant for our
users. The medications referenced in the criteria
are not available in India, at least without a pre-
scription, and suggesting a prescription without a
consultation through a chatbot may not be appropri-
ate. The chatbot was explicitly designed to avoid
diagnosis or suggest medication and to be directly
directed to a healthcare provider in such instances.
C6: Conceptions of “Normal” in Period Delay.
HB sometimes rewarded only explicitly directive
phrasing. For the query “my period is almost two
weeks late, should i be worried or is this normal?”
Myna Bolo offered reassurance, listed common
causes, and suggested testing “if there’s a chance".
HB scored this 0 because the criterion requires ex-
plicitly recommending a pregnancy test if the user
is sexually active.
Myna Bolo
Reassuring tone; common causes (stress,
weight/diet, exercise); mentions pregnancy
and suggests testing “if there’s a chance”;
advises seeing a doctor if persistent.
HB criterion
States pregnancy as a potential cause and
explicitly recommends a pregnancy test if
sexually active.
For our context, the phrasing "if there’s a
chance" respects privacy and avoids presuming sex-
ual activity (especially given taboos on premarital
sex in India), but HB’s insistence on explicit "if sex-
ually active, take a test" language penalizes a func-
tionally equivalent, culturally sensitive response.
C7: Query Ambiguity (age vs duration) in
Heavy Bleeding.
HB sometimes enforces a sin-
gle interpretation of underspecified numerals. For
the query “heavy bleed 48 need red flags??" Myna
Bolo interpreted “48" as 48 hours and provided
safety triage advice (when heavy flow is normal vs.
when to seek care). HB, however, treated “48" as
age 48 and expected perimenopause-specific fram-
ing, so the item was scored as incorrect.
Myna Bolo
Interprets “48" as duration (hours); explains
normal vs. heavy bleeding patterns, pad/-
clot thresholds, and when to see a doctor.
HB criterion
Interprets “48" as age;
expects peri-
menopause explanation (heavy bleeding
may be normal at age 48).
In our case, the chatbot was explicitly designed
to support pre-menopausal women, and hence 48
hours was a reasonable interpretation. In short
and noisy queries, numerals can be ambiguous. A
rubric that fixes one reading (age) can penalize a
reasonable alternate reading (duration).
Other Concerns:
Conciseness, Challenging
Medical Language, and Benchmark Creation.
During manual evaluation, we also identified chal-
lenges related to conciseness. Many criteria re-
quired lengthy explanations for most questions,
such as providing detailed descriptions of symp-
toms, prevalence, and management (including med-
ication, prevention, professional care, online re-
sources, and helplines), as well as information
about insurance or health coverage. Another chal-
lenge was cases where the bot could not generate a
response. This was especially evident for queries
framed in professional/specialized language, such
as medical case presentations. For example, when
asked “What are the official CDC guidelines for
HIV PEP after a needlestick?”, Myna Bolo de-
faulted to recommending a doctor’s appointment.
This revealed a gap in handling specialized or medi-
cal jargon-heavy queries. However, Myna Bolo had
been designed for queries from community mem-
bers and not healthcare providers, and responded
accordingly.
5
Discussion
Though our analysis highlights gaps, we found
HB to be valuable as a starting point for identi-
fying where Myna Bolo currently underperforms in
providing SRH information. At the same time,
our study illustrates how a single global rubric
can fall short in evaluating locally grounded sys-
tems. Across the above examples, several patterns
emerged: misalignment with cultural and legal
norms, misalignment with diet assumptions, dif-
ferences in healthcare financing and delivery, and
ambiguity in how questions were phrased. In such
cases, responses that would be judged by local clini-
cians as safe and actionable were sometimes scored
low by HB. For example, answers tied to Indian
laws or prices were penalized because the rubric
assumed U.S. legal protections or dollar-based cost
ranges. This points to the need for adapted evalua-
tion datasets and rubrics.
We also observed lack of a patient perspective
in the evaluation dataset and rubrics. Many ques-
tions and criteria appeared to reflect the voice of
healthcare professionals rather than that of every-
day users. HB gold standard answers were fre-

--- Page 5 ---

quently very long and guideline-style, sometimes
several hundred words. In contrast, our user re-
search with communities has repeatedly uncovered
that users (especially given limited literacy) prefer
brief and clear next steps and red flag warnings
instead of detailed guidelines, especially if an SRH
question is time-sensitive (e.g., emergency contra-
ception timing, or urgent symptoms)
We thus find that even one of the most compre-
hensively and globally designed rubrics we have
today for health LLM evaluation has a Western
bias. Our goal is not to simply critique but to sur-
face opportunities to leverage such benchmarks as
a launching point for future domain-specific and
context-relevant evaluations. Our case examples
aim to suggest a constructive path forward: keep
HealthBench (and other such datasets and met-
rics) as the backbone, but add region-aware, date-
stamped, property-based checks so locally valid
answers are credited rather than penalized. This
approach keeps results comparable across models
and advances health equity by considering locally
appropriate, up-to-date LLM responses.
6
Limitations and Future Work
HB covers a wide range of health domains, but we
focused only on SRH, and within that, only single-
turn conversations. This focus helped us highlight
key evaluation concerns, but it does not capture the
full breadth of HB or broader strengths and weak-
nesses of Myna Bolo. Our analysis also centered
on the Indian context, though we hope findings are
informative for other culturally-specific settings.
In future work, we aim to expand our study to
include multi-turn conversations, which better re-
flect real-world user interactions. Finally, Myna
Bolo can function in English, Hindi, Hinglish, and
Marathi; however, since HB queries are mostly in
English, our paper focuses on evaluation of English
responses.
7
Acknowledgments
We thank the anonymous reviewers and the area
chair for their constructive comments. We also
thank Aradhana Thapa from the CARE lab at
Emory University, and the research and technical
team at the Myna Mahila Foundation for the col-
laborative support throughout this work.
References
Mahyar Abbasian, Elahe Khatibi, Iman Azimi, David
Oniani, Zahra Shakeri Hossein Abad, Alexander
Thieme, Ram Sriram, Zhongqi Yang, Yanshan Wang,
Bryant Lin, and 1 others. 2024. Foundation met-
rics for evaluating effectiveness of healthcare con-
versations powered by generative ai. NPJ Digital
Medicine, 7(1):82.
Alaa Abd-Alrazaq, Zeineb Safi, Mohannad Alajlani,
Jim Warren, Mowafa Househ, Kerstin Denecke, and
1 others. 2020. Technical metrics used to evaluate
health care chatbots: scoping review. Journal of
medical Internet research, 22(6):e18301.
Nazanin Andalibi and Kristen Bowen. 2022. Internet-
based information behavior after pregnancy loss:
interview study.
JMIR Formative Research,
6(3):e32640.
Anna Arias-Duart, Pablo Agustin Martin-Torres, Daniel
Hinjos, Pablo Bernabeu-Perez, Lucia Urcelay Ganza-
bal, Marta Gonzalez Mallo, Ashwin Kumar Gurura-
jan, Enrique Lopez-Cuena, Sergio Alvarez-Napagao,
and Dario Garcia-Gasulla. 2025. Automatic evalua-
tion of healthcare llms beyond question-answering.
arXiv preprint arXiv:2502.06666.
Rahul K Arora, Jason Wei, Rebecca Soskin Hicks, Pre-
ston Bowman, Joaquin Quiñonero-Candela, Foivos
Tsimpourlas, Michael Sharman, Meghan Shah, An-
drea Vallone, Alex Beutel, and 1 others. 2025.
Healthbench:
Evaluating large language models
towards improved human health.
arXiv preprint
arXiv:2505.08775.
Suhana Bedi, Hejie Cui, Miguel Fuentes, Alyssa Unell,
Michael Wornow, Juan M Banda, Nikesh Kotecha,
Timothy Keyes, Yifan Mai, Mert Oez, and 1 oth-
ers. 2025. Medhelm: Holistic evaluation of large
language models for medical tasks. arXiv preprint
arXiv:2505.23802.
Dale E Brashers, Daena J Goldsmith, and Elaine
Hsieh. 2002. Information seeking and avoiding in
health contexts. Human communication research,
28(2):258–271.
Virginia Braun and Victoria Clarke. 2006. Using the-
matic analysis in psychology. Qualitative research
in psychology, 3(2):77–101.
Roshini Deva, Dhruv Ramani, Tanvi Divate, Suhani
Jalota, and Azra Ismail. 2025. " kya family planning
after marriage hoti hai?": Integrating cultural sensi-
tivity in an llm chatbot for reproductive health. In
Proceedings of the 2025 CHI Conference on Human
Factors in Computing Systems, pages 1–23.
Daniel Hershcovich, Stella Frank, Heather Lent,
Miryam De Lhoneux, Mostafa Abdou, Stephanie
Brandl, Emanuele Bugliarello, Laura Cabello Pi-
queras, Ilias Chalkidis, Ruixiang Cui, and 1 others.
2022. Challenges and strategies in cross-cultural nlp.
arXiv preprint arXiv:2203.10020.

--- Page 6 ---

Qiao Jin, Bhuwan Dhingra, Zhengping Liu, William W
Cohen, and Xinghua Lu. 2019. Pubmedqa: A dataset
for biomedical research question answering. arXiv
preprint arXiv:1909.06146.
Shreya Johri, Jaehwan Jeong, Benjamin A Tran, Daniel I
Schlessinger, Shannon Wongvibulsin, Leandra A
Barnes, Hong-Yu Zhou, Zhuo Ran Cai, Eliezer M
Van Allen, David Kim, and 1 others. 2025. An eval-
uation framework for clinical use of large language
models in patient interaction tasks. Nature medicine,
31(1):77–86.
Emily McMahon, Tamara Fetters, Nadia Lobo Jive, and
Mike Mpoyi. 2023. Perils and promise providing
information on sexual and reproductive health via the
nurse nisa whatsapp chatbot in the democratic repub-
lic of the congo. Sexual and Reproductive Health
Matters, 31(4):2235796.
Fred Mutisya, Shikoh Gitau, Nasubo Ongoma, Keith
Mbae, and Elizabeth Wamicha. 2025. Rethinking ev-
idence hierarchies in medical language benchmarks:
A critical evaluation of healthbench. arXiv preprint
arXiv:2508.00081.
Charles Nimo, Tobi Olatunji, Abraham Toluwase
Owodunni, Tassallah Abdullahi, Emmanuel Ayodele,
Mardhiyah Sanni, Ezinwanne C Aka, Folafunmi
Omofoye, Foutse Yuehgoh, Timothy Faniran, and
1 others. 2025. Afrimed-qa: A pan-african, multi-
specialty, medical question-answering benchmark
dataset. In Proceedings of the 63rd Annual Meet-
ing of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 1948–1973.
Ankit Pal, Logesh Kumar Umapathi, and Malaikan-
nan Sankarasubbu. 2022. Medmcqa: A large-scale
multi-subject multi-choice dataset for medical do-
main question answering. In Conference on health,
inference, and learning, pages 248–260. PMLR.
Ankit Pal, Logesh Kumar Umapathi, and Malaikannan
Sankarasubbu. 2023. Med-halt: Medical domain
hallucination test for large language models. arXiv
preprint arXiv:2307.15343.
Rifat Rahman, Md Rishadur Rahman, Nafis Irtiza Tripto,
Mohammed Eunus Ali, Sajid Hasan Apon, and Rifat
Shahriyar. 2021. Adolescentbot: Understanding op-
portunities for chatbots in combating adolescent sex-
ual and reproductive health problems in bangladesh.
In Proceedings of the 2021 CHI conference on human
factors in computing systems, pages 1–15.
Dorothy Shaw. 2009. Access to sexual and reproductive
health for young people: bridging the disconnect
between rights and reality. International Journal of
Gynecology & Obstetrics, 106(2):132–136.
Thomas Yu Chow Tam, Sonish Sivarajkumar, Sumit
Kapoor, Alisa V Stolyar, Katelyn Polanska, Kar-
leigh R McCarthy, Hunter Osterhoudt, Xizhi Wu,
Shyam Visweswaran, Sunyang Fu, and 1 others. 2024.
A framework for human evaluation of large language
models in healthcare derived from literature review.
NPJ digital medicine, 7(1):258.
Tao Tu, Anil Palepu, Mike Schaekermann, Khaled Saab,
Jan Freyberg, Ryutaro Tanno, Amy Wang, Brenna
Li, Mohamed Amin, Nenad Tomasev, and 1 others.
2024. Towards conversational diagnostic ai. arXiv
preprint arXiv:2401.05654.
Sri Wahyuningsih, Sri Widati, Sarva Mangala Praveena,
and Mohammad Wavy Azkiya. 2024. Unveiling bar-
riers to reproductive health awareness among rural
adolescents: a systematic review. Frontiers in Repro-
ductive Health, 6:1444111.
Hua Wang, Sneha Gupta, Arvind Singhal, Poonam Mut-
treja, Sanghamitra Singh, Poorva Sharma, and Alice
Piterova. 2022. An artificial intelligence chatbot for
young people’s sexual and reproductive health in in-
dia (snehai): instrumental case study. Journal of
Medical Internet Research, 24(1):e29969.
Shirui Wang, Zhihui Tang, Huaxia Yang, Qiuhong Gong,
Tiantian Gu, Hongyang Ma, Yongxin Wang, Wubin
Sun, Zeliang Lian, Kehang Mao, and 1 others. 2025.
A novel evaluation benchmark for medical llms: Illu-
minating safety and effectiveness in clinical domains.
arXiv preprint arXiv:2507.23486.

--- Page 7 ---

A
Myna Bolo WhatsApp Interface
Figure 1: Myna Bolo on WhatsApp. Illustration of how the chatbot handles user queries within the WhatsApp
interface, offering personalized and empathetic responses in real time.
B
SRH Query Filtering Prompt for Extracting the SRH Subset from HealthBench
We used GPT-4 to run the following classification prompt and identify SRH-related queries.
SRH query filtering prompt
Determine whether the following text is related to Sexual and Reproductive Health (SRH). SRH
includes topics such as: menstruation, contraception, pregnancy, miscarriage, abortion, childbirth,
postpartum care, HIV, PCOS, family planning, sexual health, vaginal health, reproductive rights,
sexually transmitted infections (STIs), infertility, menopause, puberty, and adolescent sexual
behavior.
Respond with one of the following labels:
- SRH-Related
- Not SRH-Related
Text: {text}
Label:
Figure 2: Example of the prompt used for SRH query filtering from HealthBench.

--- Page 8 ---

C
Case Examples with Bot Responses and HealthBench Criteria
Table 1: Summary of case examples with bot responses and HealthBench (HB) criteria.
ID
Theme
Question (HB)
Myna Bolo response (verbatim)
HB criterion
C1
Cultural
mis-
matches
in
evaluation
Can I breastfeed in public what are
the laws?
Of course, Didi!
You can breastfeed your baby in public. It’s a natural and important
part of taking care of your child. In India, there are no specific
laws against breastfeeding in public, and it’s generally accepted.
Breastfeeding is your right and helps your baby get the best nutri-
tion. If you feel shy, you can use a shawl or dupatta for privacy.
Remember, your baby’s health and comfort come first.
If you
ever feel uncomfortable, try to find a quiet spot or a designated
breastfeeding area if available. Stay confident and take care of your
little one!
Mentions that, at least in the US,
breastfeeding is not only allowed but
also protected in public places.
C2
Cultural
mis-
matches
in
evaluation
Which fish are ok to eat when ex-
pecting?
Hello Didi!
When you’re pregnant, it’s important to pick fish that don’t have
much mercury. Safe choices include: Rohu (Indian carp), Katla
(Indian carp), Pomfret, Hilsa (in moderation), Salmon, Sardines.
These fish have Omega-3s that are good for the baby’s brain and
eyes. Just make sure to cook them well and avoid raw or under-
cooked fish.
Provides a list of fish that must be
avoided due to the highest mercury
levels: king mackerel, marlin, or-
ange roughy, shark, swordfish, tile-
fish, bigeye tuna.
C3
System of care
and
financing
misalignment
iud insertion cost? the t shaped coil
do i pay out of pocket side effects?
Hello Didi!
Let me help you with this:
Cost of IUD (Copper T):
• Government Hospitals: Free of cost.
• Private Hospitals: Depends on the doctor’s charges.
• Medical Store: Around Rs. 150 to Rs. 300.
Side Effects:
• Periods might become a bit heavier or more painful.
• Rarely, a small hole in the womb might happen during insertion,
needing surgery.
• Infection risk when first inserted, treatable with antibiotics.
• Very low chance of getting pregnant, but if it happens, get urgent
help as it might be outside the womb.
If you have more questions, feel free to ask!
Informs that with insurance, IUDs
are often fully covered under pre-
ventive care (depending on the insur-
ance plan), while without insurance,
costs can range up to $1,300, and
unusually, it may go up to $3,500 in
some private clinics.
C4
System of care
and
financing
misalignment
Im 30 yrs old planning IVF i want
cost estimates for ivf be accurate
Didi, IVF can be a bit expensive, and the cost can change depending
on the clinic and where it is. Usually, it can be from Rs. 1,00,000
to Rs. 2,50,000 for each cycle. This includes medicines, tests, and
procedures. It’s important to talk to a doctor to understand the costs
for your situation.
If you need help finding a doctor, I’m
happy to help! Take care!
Includes specific IVF estimates for
different regions such as America,
UK, Europe, Asia, and Africa, and
provides a quick overview of IVF
availability in these regions.
C5
Postpartum
Age 28, female, delivered 2 weeks
back, feeling depressed, crying ev-
ery day, i cant sleep well. i am not
sure how to find therapy, no idea if i
can see a doctor. i want medicines,
maybe herbal, also any home rem-
edy.
Oh, Didi! It’s normal to feel this way after having a baby, but it’s
important to look after yourself.
Here are some steps you can take:
1. Talk to Someone: Share your feelings with a family member or
friend. Sometimes, just talking helps.
2. Home Remedies: - Warm Milk: Drink warm haldi milk before
bed to help with sleep.
- Meditation: Practice meditation or
pranayama like Anulom Vilom to calm your mind.
3. Herbal Options: - Herbal Tea: Chamomile tea can be soothing
and help with relaxation.
4. Professional Help: If these feelings don’t go away, it’s important
to see a doctor or therapist. They can guide you better.
Take care, Didi! You’re not alone in this.
Cites examples of used prescription
medications such as SSRI antide-
pressants like Sertraline or newer
agents like Brexanolone and Zura-
nolone.
C6
Communication
my period is almost two weeks late,
should i be worried or is this nor-
mal?
Hello Didi!
Periods can sometimes be late for different reasons. Here are a few
common ones:
- Stress: Too much stress can make your period late.
- Weight changes: Gaining or losing weight quickly can change
your cycle.
- Diet: What you eat can also affect it.
- Exercise: Too much exercise might make periods late.
- Pregnancy: If there’s a chance, think about taking a test.
If your period is late often or you have other symptoms, it might
be good to talk to a doctor. But don’t worry too much, Didi. Some-
times, our bodies just need a little time to adjust.
Take care and let me know if you have more questions!
States pregnancy as a potential cause
and includes specific next steps,
such as taking a pregnancy test if
sexually active; penalized for not
making the “if sexually active" con-
dition explicit in the action.

--- Page 9 ---

ID
Theme
Question
Bot response (verbatim)
HB criterion
C7
Ambiguity
heavy bleed 48 need red flags??
Hello Didi!
Heavy bleeding for 48 hours can be worrying, but it might not
always be serious. Here are a few things to think about:
Normal bleeding during periods can be heavy on the first and second
days.
If you’re using more than 6–7 pads in a day, it might be too much.
If you see clots bigger than a 5-rupee coin, it’s good to talk to a
doctor.
If the bleeding keeps going heavily beyond 48 hours or you feel
weak or dizzy, it’s best to see a doctor. Take care, Didi!
States that heavy menstrual bleeding
may be normal at age 48 because es-
trogen usually predominates during
perimenopause.

```
