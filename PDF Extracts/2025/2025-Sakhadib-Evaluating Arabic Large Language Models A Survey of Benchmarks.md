---
title: "2025-Sakhadib-Evaluating Arabic Large Language Models A Survey of Benchmarks - PDF Extract"
source_pdf: "2025-Sakhadib-Evaluating Arabic Large Language Models A Survey of Benchmarks.pdf"
pages: 16
extracted_at: "2026-02-13T13:57:13.821671"
---

# PDF Extract: 2025-Sakhadib-Evaluating Arabic Large Language Models A Survey of Benchmarks

**Source PDF:** 2025-Sakhadib-Evaluating Arabic Large Language Models A Survey of Benchmarks.pdf
**Total Pages:** 16

---

## Content

```
--- Page 1 ---

Evaluating Arabic Large Language Models: A Survey of Benchmarks,
Methods, and Gaps
Ahmed Alzubaidi, Shaikha Alsuwaidi, Basma El Amel Boussaha, Leen AlQadi
Omar Alkaabi, Mohammed Alyafeai, Hamza Alobeidli, Hakim Hacid
Technology Innovation Institute, Abu Dhabi, UAE
ahmed.alzubaidi@tii.ae
Abstract
This survey provides the first systematic re-
view of Arabic LLM benchmarks, analyzing
40+ evaluation benchmarks across NLP tasks,
knowledge domains, cultural understanding,
and specialized capabilities. We propose a tax-
onomy organizing benchmarks into four cate-
gories: Knowledge, NLP Tasks, Culture and
Dialects, and Target-Specific evaluations. Our
analysis reveals significant progress in bench-
mark diversity while identifying critical gaps:
limited temporal evaluation, insufficient multi-
turn dialogue assessment, and cultural misalign-
ment in translated datasets. We examine three
primary approaches: native collection, transla-
tion, and synthetic generation discussing their
trade-offs regarding authenticity, scale, and
cost. This work serves as a comprehensive
reference for Arabic NLP researchers, provid-
ing insights into benchmark methodologies, re-
producibility standards, and evaluation metrics
while offering recommendations for future de-
velopment.
1
Introduction
In recent years, Large Language Models (LLMs)
have demonstrated remarkable advances in natural
language understanding and logical reasoning ca-
pabilities, bringing us closer to the vision of AGI
(Naveed et al., 2025). From the beginning of the
transformer era, LLMs have shown potential be-
yond English, with numerous successes across mul-
tiple languages (Huang et al., 2025). The Arabic
language, spoken by almost 500 million people
globally1, exemplifies the critical need for mul-
tilingual LLM capabilities. Consequently, both
bilingual and Arabic-specific LLMs have been
released as closed and open-source models (Al-
Khalifa et al., 2025). A critical component of LLM
1World Bank (2024).
Population,
Total – Arab
World.
https://data.worldbank.org/indicator/SP.
POP.TOTL?locations=1A
development is the availability of robust bench-
marks that enable systematic evaluation of perfor-
mance across tasks and domains. In parallel with
progress in Arabic LLMs, a corresponding effort
has emerged focused on creating comprehensive
benchmarks for Arabic evaluation.
Developing Arabic benchmarks presents several
unique challenges. Data scarcity and limited diver-
sity in Arabic web content (Al-Khalifa et al., 2025)
increase the cost and effort required for benchmark
creation. To address these constraints, researchers
have pursued three primary approaches: translating
mainstream English benchmarks to Arabic, gen-
erating synthetic data using powerful LLMs, and
collecting native Arabic content. However, each ap-
proach presents trade-offs. Translation can produce
culturally misaligned benchmarks that undermine
evaluation robustness. Synthetic generation risks
introducing biases from the generating model and
may produce questions that facilitate circular eval-
uation. Both approaches are susceptible to cultural
misalignment problems (Nacar et al., 2025), often
requiring extensive human validation and iterative
refinement.
Additionally, Arabic’s linguistic diversity span-
ning Modern Standard Arabic (MSA) and numer-
ous regional dialects (Keleg et al., 2025), adds
complexity to comprehensive evaluation. Arabic
requires dedicated benchmarking analysis due to
its unique morphological complexity, 20+ dialectal
varieties functioning almost as distinct languages,
critical cultural sensitivity requirements that un-
dermine translation-based approaches, severe data
scarcity despite 500 million speakers, and a frag-
mented evaluation landscape challenges absent in
languages with standardized benchmarking bench-
marks like English.
Several recent surveys have examined Arabic
LLMs from various perspectives (Mashaabi et al.,
2024; Al-Khalifa et al., 2025; Rhel and Roussinov,
2025). However, none has provided an extensive,
arXiv:2510.13430v2  [cs.CL]  16 Oct 2025

--- Page 2 ---

comprehensive analysis of Arabic benchmarks and
evaluation approaches. This survey addresses that
gap by systematically reviewing the current land-
scape of evaluation techniques and benchmarking
datasets for Arabic LLMs. We aim to serve as the
primary reference for researchers and practitioners
in Arabic NLP when evaluating their models. Our
contributions are threefold: (1) we propose a tax-
onomy organizing existing benchmarks into four
major categories; (2) we provide a detailed analysis
of 40+ Arabic benchmarks, offering a comprehen-
sive resource for the Arabic NLP community; and
(3) we discuss common approaches, established
evaluation tools, current trends, and critical gaps
in Arabic benchmark coverage. Moreover, we pro-
vide a repository2 that consolidates all the bench-
marks, dataset links, code repositories, and inte-
grated frameworks to facilitate easy access for the
community.
The remainder of this paper is structured as fol-
lows: Section 2 presents background on Arabic
LLMs and related surveys. Section 3 introduces
our taxonomy, with Sections 4 through 7 examining
each category in detail. Section 8 analyzes the cur-
rent state and identifies gaps in Arabic benchmarks.
Section 9 concludes the paper.
2
Background
This section provides the necessary context for un-
derstanding the Arabic LLM benchmarking land-
scape. We first categorize existing Arabic LLMs
by their training approaches, then review related
survey work to position our contribution within the
broader literature.
2.1
Arabic LLMs
State-of-the-art Arabic LLMs can be categorized
into three types.
Native models are trained
from scratch exclusively on Arabic data, enabling
Arabic-only interaction. Examples include Jais
(Sengupta et al., 2023), ArabianGPT (Koubaa
et al., 2024), and AraGPT (Antoun et al., 2021).
Multilingual models support multiple languages
including Arabic, such as Qwen3 (Yang et al.,
2025), Gemma3 (Team et al., 2025b), and Llama
(Grattafiori et al., 2024), as well as closed-source
models like ChatGPT (OpenAI, 2023) and Claude
(Anthropic, 2024). Adapted Arabic models apply
continued pretraining or supervised fine-tuning to
2https://github.com/tiiuae/
Arabic-LLM-Benchmarks
existing multilingual models to enhance Arabic per-
formance, exemplified by AceGPT (Huang et al.,
2024), SILMA (Team, 2024), Fanar (Team et al.,
2025a), and Falcon-Arabic (TII, 2025).
2.2
Related Work
Several surveys have examined Arabic LLMs from
different perspectives. Mashaabi et al. (2024) pro-
vided an in-depth discussion of pretraining and
fine-tuning data for Arabic LLMs, including di-
alectal coverage, and listed available models with
details on accessibility and reproducibility. Rhel
and Roussinov (2025) surveyed pretrained Arabic
LLMs with focus on classical NLP applications
and benchmarks. Most recently, Al-Khalifa et al.
(2025) presented the historical evolution of Arabic
NLP, common pretraining and fine-tuning strate-
gies, and current research trends and challenges.
While Al-Khalifa et al. (2025) briefly discussed a
subset of existing benchmarks, no comprehensive
survey of Arabic LLM benchmarks exists. This
work fills that gap by systematically reviewing eval-
uation techniques and benchmarking datasets for
Arabic LLMs.
3
Benchmarks Taxonomy
We reviewed 40+ existing Arabic LLM bench-
marks and constructed a taxonomy that captures
various themes and categories, as depicted in Fig-
ure 1. Our taxonomy organizes benchmarks into
four categories:
Knowledge includes benchmarks evaluating gen-
eral knowledge and STEM capabilities, along with
domain-specific benchmarks in fields such as law
and medicine.
Natural Language Processing (NLP) encom-
passes early task-specific benchmarks and com-
prehensive multi-task benchmarks, reflecting the
evolution from narrow task evaluation to unified
assessment across diverse dialects and domains.
Culture and Dialects groups benchmarks assess-
ing cultural knowledge and dialect understanding,
addressing the essential property of cultural aware-
ness in Arabic LLMs.
Target-Specific covers benchmarks designed to
assess particular LLM properties such as safety,
hallucination detection, instruction-following, and
vision capabilities.
This taxonomy emerged from analyzing com-
mon patterns across benchmarks and reflects the
evolution from task-specific evaluation to compre-

--- Page 3 ---

hensive assessment. In the following sections, we
describe each category and we provide a compre-
hensive table (Tables 2) listing all discussed bench-
marks with their characteristics.
4
Knowledge
This section examines benchmarks evaluating
LLMs’ acquired knowledge and reasoning capa-
bilities, covering both general and STEM topics
and specialized domains like law, medicine, and
poetry.
4.1
General and STEM
Multilingual
efforts
produced
early
general
knowledge benchmarks with Arabic components.
MMLU_ar (Hendrycks et al., 2020) comprises
14,079 human-translated MCQs spanning 57 sub-
jects across difficulty levels, while EXAMS_ar
(Hardalov et al., 2020) contains 562 high-school
exam questions covering physics, chemistry, and
biology. However, these suffer from translation
concerns or limited scale.
ArabicMMLU (Koto et al., 2024) addressed
these limitations with 14,575 native Arabic MCQs
curated from educational exams across Arab
countries, covering all school levels plus univer-
sity, spanning STEM, social sciences, humanities,
and Arabic language understanding. AraSTEM
(Mustapha et al., 2024) further specialized in
STEM with 11,637 native MCQs which is 7,000
more STEM samples than ArabicMMLU though it
remains unpublished despite evaluation results on
open-weight models.
The 3LM suite (Boussaha et al., 2025) com-
bines three benchmarks totaling 3,151 questions:
3LM_nat from Arabic STEM exams, 3LM_syn
synthetically generated via Yourbench’s pipeline
(Shashidhar et al., 2025) using Qwen3-235B-A22B,
and 3LM_code comprising Arabic translations of
HumanEval (Chen et al., 2021) and MBPP (Austin
et al., 2021) instructions and comments.
Several benchmarks leverage Saudi Arabia’s
General Aptitude Test (GAT), which assesses
verbal abilities (reading comprehension, contex-
tual errors, sentence completion) and quantitative
skills (arithmetic, algebra, geometry, data analysis).
Early efforts (Alkaoud, 2024; Al-Khalifa and Al-
Khalifa, 2024) used 456 and 2,407 GAT samples
respectively but lacked reproducibility and scale,
evaluating only GPT-3.5 and GPT-4 with limited
shots. GATmath and GATLc (AlBallaa et al., 2025)
addressed these issues with 7k and 9k samples re-
spectively (16k total), publicly released with 5-shot
evaluation on diverse Arabic and bilingual LLMs.
Arabic-GSM8K (Omartificial-Intelligence-Space,
2025) provides human-validated translations of
the established GSM8K benchmark (Cobbe et al.,
2021), assessing middle-school mathematical rea-
soning through 5-shot settings.
4.2
Domain Knowledge
Legal Domain.
ArabLegalEval (Hijazi et al.,
2024) pioneered Arabic legal LLM evaluation us-
ing documents scraped from Saudi Arabia’s Min-
istry of Justice and Board of Experts websites. The
benchmark employs three approaches: synthetic
MCQ generation using GPT-4 and Claude-3-opus
with in-context examples from ArabicMMLU’s law
section, QA pairs from governmental FAQ sec-
tions, and machine-translated datasets from Legal-
bench (Guha et al., 2023) verified by legal experts.
MIZANQA (Bahaj and Ghogho, 2025) extends le-
gal evaluation to Moroccan law using MCQs from
various law exams.
Poetry and Linguistics. Fann or Flop (Alghal-
labi et al., 2025) assesses poetry understanding
through 6,984 poem-explanation pairs, evaluating
metaphorical and figurative comprehension. Evalu-
ation uses BLEU, chrF(++), BERTScore, and mDe-
BERTaV3 for character-level overlap and semantic
alignment, with GPT-4o as judge for faithfulness,
grammatical correctness, and interpretive depth.
Medical Domain. Al-Majmar et al. (2024) intro-
duced 808k medical QA samples from the AlTibbi
patient-doctor forum3. AraMed (Alasmari et al.,
2024) refined this to 270k high-quality samples
based on vote counts. MedArabiQ (Daoud et al.,
2025) further curated 100 AraMed samples, en-
hanced them through grammatical correction and
LLM modification, and added medical exam ques-
tions (MCQs and fill-in-the-blank), yielding 700
samples evaluating Arabic medical knowledge.
Religious Domain. Hajj-FAQ (Aleid and Azmi,
2025) addresses religious knowledge through
question-answering on Hajj fatwas (Islamic legal
rulings), providing a benchmark for LLMs’ under-
standing of Islamic jurisprudence and pilgrimage-
related guidance. This specialized dataset evaluates
models’ ability to handle religiously and culturally
sensitive content requiring both linguistic compe-
tence and domain-specific religious knowledge.
3https://altibbi.com/

--- Page 4 ---

Instruct Following
Safety
Hallucination
CamelEval
AraTrust,
Asas
AraHalluEval,
HalluVerse25,
 Halwasa
ARB, 
CAMEL-Bench,
Peacock
ALRAGE,
 AraTable
Multimodal
Arabic Benchmarks
Knowledge
Culture & Dialects
Target Specific
General & STEM
 Domain Knowledge
MMLU_ar, ArabicMMLU, 
AraSTEM, GAT, GATmath,
GATLc,  QIYAS,  
3LM, EXAMS_ar,
ArabLegalEval, 
Fann or Flop, Hajj-FAQ,
MedArabiQ, AraMed
MizanQA, Arabic-GSM8K
Culture
Dialects
Jawaher
Palm,
palmX
AL-QASIDA,
ARADICE,
ABSHER
LAraBench,
BALSAM,
AlGhafa
Multi-Task
NLP Tasks
context-based
ARCD,
TyDiQA(ar),
ORCA,
Dolphin
Task Specific
Figure 1: Taxonomy of Arabic Benchmarks.
5
NLP Tasks
Arabic LLM evaluation on fundamental NLP tasks
has evolved from narrow, task-specific datasets
to comprehensive, multi-dimensional benchmarks.
Early efforts like ARCD (Mozannar et al., 2019)
for reading comprehension and TyDiQA (Clark
et al., 2020) for question answering established
foundational paradigms for the pre-LLM era. The
landscape has shifted toward unified benchmarks
assessing generalist capabilities across understand-
ing, generation, and reasoning tasks, addressing
morphological complexity, dialectal variation, and
domain diversity (Table 2).
5.1
Comprehensive Multi-Task Benchmarks
LAraBench (Abdelali et al., 2024) pioneered sys-
tematic LLM benchmarking for Arabic NLP and
speech processing, comparing task-specific mod-
els against general-purpose LLMs across 33 tasks
spanning 61 datasets. It integrates earlier resources
like ARCD and dialect identification corpora, bridg-
ing pre-LLM and LLM evaluation eras. Evaluation
of GPT-3.5-turbo, GPT-4 (OpenAI et al., 2024),
BLOOMZ (Muennighoff et al., 2023a), Jais-13b-
chat (Sengupta et al., 2023) and Whisper (Radford
et al., 2023) under zero-shot and few-shot settings
reveals that specialized models outperform LLMs
in zero-shot scenarios, though larger LLMs with
few-shot adaptation substantially narrow this gap.
BALSAM (Al-Matham et al., 2025) provides
community-driven comprehensive evaluation em-
phasizing instruction-following across 78 tasks
and 14 categories, totaling 52K examples cover-
ing summarization, question answering, informa-
tion extraction, translation, classification, creative
writing, and reasoning. It addresses data contam-
ination through blind test sets and provides an
integrated leaderboard. Notably, LLM-as-judge
correlates more strongly with human judgments
(0.824 - 0.977) than traditional metrics (BLEU,
ROUGE, BERTScore). Datasets combine natu-
rally authored, translated, prompted, and synthetic
sources from xP3 (Muennighoff et al., 2023b),
PromptSource (Bach et al., 2022), SuperNaturalIn-
structions (Wang et al., 2022), TruthfulQA (Lin
et al., 2022), and 16 newly developed datasets
(1,755 prompts). Results show large closed-source
models (GPT-4o, Gemini 2.0, DeepSeek V3) out-
perform smaller Arabic-centric models, with per-
formance depending on tokenization quality, train-
ing data volume, and Arabic-specific fine-tuning.
Limitations include potential cultural misalignment
in translated datasets and insufficient assessment
of multi-turn dialogue and hallucination.
5.2
Task-Specific Benchmarks
Understanding and generation capabilities re-
quire specialized evaluation beyond comprehensive
suites.
ORCA (Elmadany et al., 2023) focuses on nat-
ural language understanding across Arabic’s lin-
guistic diversity, consolidating 60 datasets into 7
task clusters: sentence classification, structured
prediction (NER, POS), semantic textual similar-
ity, paraphrase identification, natural language in-
ference, word sense disambiguation, and question
answering. Evaluation employs task-appropriate
metrics (accuracy, F1-score, Pearson correlation,
exact match) across MSA and dialects, compar-
ing 18 multilingual and Arabic-specific pre-trained
models. Its public leaderboard with rich metadata
promotes transparency and reproducibility, provid-
ing a critical reference for understanding evolution
toward modern LLM evaluation.
Dolphin (Nagoudi et al., 2023) addresses natu-
ral language generation through nine tasks: head-
line and title generation, question generation,
paraphrasing, transliteration, abstractive and ex-

--- Page 5 ---

tractive summarization, and grammatical error
correction across MSA and dialects.
Consoli-
dating 15 datasets, it evaluates encoder-decoder
(mT5, AraT5) and decoder-only models (GPT-3.5,
BLOOMZ, Jais) using BLEU, ROUGE, METEOR,
BERTScore, and task-specific metrics like charac-
ter error rate. Results reveal substantial variabil-
ity and gaps between general-purpose multilingual
models and Arabic-finetuned baselines. However,
Dolphin predates instruction-tuned LLMs and re-
lies on zero-shot prompting, potentially underesti-
mating achievable performance.
Modern benchmarks like LAraBench, BAL-
SAM, ORCA, and Dolphin provide unified evalu-
ation benchmarks capturing understanding, gener-
ation, reasoning, and instruction-following while
incorporating dialectal and domain diversity, offer-
ing a roadmap for future Arabic LLM evaluation.
6
Culture and Dialects
Evaluation of cultural and dialectal understanding
in Arabic LLMs has developed progressively, with
each benchmark addressing gaps left by its prede-
cessors. Jawaher (Magdy et al., 2025) provided
one of the earliest culturally grounded resources by
compiling 10,037 Arabic proverbs drawn from on-
line resources. Each proverb was annotated with its
dialectal origin and idiomatic explanation, and cast
into a QA format, enabling evaluation of figurative
and cultural reasoning in dialectal Arabic a dimen-
sion overlooked in prior benchmarks. However,
Jawaher was limited to proverbial knowledge.
PALM (Alwajih et al., 2025a) addressed this gap
by curating a broader culturally inclusive dataset
through a year-long community-driven effort span-
ning all 22 Arab countries. Covering prose, dia-
logue, and cultural expressions across 20 topics, it
expanded evaluation beyond proverbs and tested
inclusivity using perplexity and generation quality.
Following the release of Palm, PalmX (Alwajih
et al., 2025b) released a benchmark focused on
assessing the deep understanding of Arabic and Is-
lamic culture. It contained two subtasks of MCQs
in MSA covering traditions, food, history, religious
practices, and expressions. Despite these advances,
benchmarks had yet to capture Arab-specific com-
monsense reasoning. Commonsense Reasoning in
Arab Culture (Sadallah et al., 2025) filled this gap
by introducing questions requiring culturally aware
inference, complementing the focus on linguistic
diversity in earlier work.
We next discuss existing benchmarks that eval-
uate LLMs on Arabic dialects. AraDiCE (Mousi
et al., 2025) provided a benchmark dataset that as-
sesses the identification and generation of dialects,
cognitive abilities when conversing in dialects, fo-
cusing on Egyptian, Levantine, and Gulf regions.
This work involved employing machine translation
techniques to translate mainstream benchmarks (i.e
ArabicMMLU, TruthfilQA) to LEV/EGY dialects,
to assess the desired cognitive skills. A subse-
quent effort by Alqasida et al. (Robinson et al.,
2025) proposed a comprehensive framework for
evaluating LLMs’ proficiency in Arabic dialects,
encompassing dimensions such as identification,
comprehension, generation quality, and translation
between dialects and MSA. Furthermore, NADI
2024 (Abdul-Mageed et al., 2024) was employed
to evaluate dialect identification tasks, alongside
several translation-based evaluations to examine
dialect chat capabilities. Absher (Al-Monef et al.,
2025) specialized in the Saudi dialect interpreta-
tion, focusing on vocabilary, phrases, and proverbs,
sourced from the Moajam website4.
From the reviewed benchmarks, it is evident
that only a limited number of serious efforts have
been made to establish evaluation suites targeting
cultural alignment and dialectal diversity in Ara-
bic LLMs. While these initiatives mark important
progress toward building linguistically and cultur-
ally grounded models, further work is needed to
broaden their scope and depth. Future benchmarks
should enable the community to more comprehen-
sively assess models’ capabilities in cultural un-
derstanding and effective communication across
Arabic dialects.
7
Target-Specific Tasks
Beyond general NLP capabilities, Arabic LLMs
require evaluation on specialized tasks reflecting
real-world deployment scenarios and LLM-specific
challenges.
Instruction-Following. CamelEval (Qian et al.,
2024)
evaluates
conversational
abilities
and
instruction-following through 1,610 generative
questions: 805 human-validated translations from
AlpacaEval (Dubois et al., 2023) and 805 syn-
thetically generated using GPT-4 from culturally
grounded textbooks.
Evaluation uses LLM-as-
judge computing win rates for open-ended gen-
eration.
4https://ar.mo3jam.com/

--- Page 6 ---

103
104
105
106
Number of Samples (log scale)
Dolphin
ORCA
LAraBench
AraMed
BALSAM
AraDiCE
Alghafa
CAMEL-Bench
ArabLegalEval
ALRAGE
Absher
PALM
MMLU_ar
ArabicMMLU
TyDiQA (Ar)
AraSTEM
Halwasa
Jawaher
GATmath, GATLc
Arabic-GSM8K
Fann or Flop
PalmX
Arabic Safeguard Dataset
Commonsense Reasoning
3LM
Qiyas
MizanQA
CamelEval
AraHalluEval
ARCD
ARB (Arabic Multimodal Reasoning)
HajjFAQ
Henna
HalluVerse25
ASAS (Arabic Safety Index)
MedArabiQ
AraTable
GAT
AraTrust
EXAMS_ar
AL-QASIDA
Arabic NLP Datasets Sizes Across Categories
Category
Target-Specific Tasks
Knowledge & STEM Tasks
Arabic NLP Tasks
Culture and Dialects Tasks
Figure 2: Arabic Datasets Sizes Across Categories. Size is log-scaled.
Context-Based Reasoning.
ALRAGE (El Fi-
lali et al., 2025) targets RAG evaluation through
2.12K question-answer-context trios from 40 Ara-
bic books, synthetically generated via Meta-Llama-
3.1-70B and validated by native speakers. AraTable
(Alshaikh et al., 2025) addresses structured tabular
data through 41 tables (15 QA pairs each) evaluat-
ing direct answering, fact verification, and complex
reasoning. Tables sourced from Wikipedia, govern-
ment portals, and GPT-4o were verified by human
experts, with evaluation combining accuracy and
the Assisted Self-Deliberation (ASD) framework
employing judge LLMs and human evaluation.
Hallucination Detection. HalluVerse25 (Abdal-
jalil et al., 2025) provides fine-grained multilingual
evaluation across entity, relation, and sentence hal-
lucination types, offering 828 Arabic samples from
Wikidata autobiographies where GPT-4 injected
false hallucinations validated by human judges.
AraHalluEval (Alansari and Luqman, 2025) fo-
cuses on Arabic through QA (300 samples from
TyDiQA-GoldP-AR and translated TruthfulQA)
and summarization (100 XLSum instances), distin-
guishing factuality and faithfulness hallucinations
through manual annotation. Halwasa (Mubarak
et al., 2024) provides larger-scale evaluation with
10K samples where ChatGPT and GPT-4 generated
factual sentences from 1,000 SAMER Arabic Lexi-
con words, with hallucination indicators annotated
by 200 annotators enabling sentence-level analysis.
Safety and Trustworthiness. Ashraf et al. (2025)
introduced 5,799 questions spanning direct attacks,
indirect attacks, and harmless requests with sen-
sitive words, employing dual-perspective evalu-
ation from governmental and oppositional view-
points. ASAS (aiastrolabe, 2025) provides the first
human-rated Arabic safety index for red-teaming
frontier models, exposing persistent weaknesses
in top-performing systems. AraTrust (Alghamdi
et al., 2024) assesses trustworthiness across nine
dimensions through 522 human-written MCQs.
Multimodal Capabilities.
Peacock (Alwajih
et al., 2024) pioneered Arabic multimodal eval-
uation with Henna benchmark combining standard
VQA/OCR prompts with focus on culture under-
standing. CAMEL-Bench (Ghaboura et al., 2024)
provides large-scale evaluation across eight do-
mains and 38 subdomains, revealing promising per-
formance but substantial weaknesses in specialized
domains requiring precise vision-text alignment.
ARB (Ghaboura et al., 2025) advances step-by-
step multimodal reasoning, emphasizing logical
integration of visual and textual inputs over simple
captioning.

--- Page 7 ---

Category
Coverage
Key Gaps
Q&A / Reading Comprehension
Moderate (5 datasets)
Evaluation methods vary; unified standards and human checks are needed
Translation & Multitask Generation
Moderate (4 datasets)
Inconsistent task design and limited reproducibility across models
Reasoning & Multi-step Thinking
Limited (3 datasets)
Datasets remain small and synthetic; real-world reasoning is underexplored
STEM / Academic Evaluation
Strong (8 datasets)
Dominated by exam-style data; lacks applied and interdisciplinary tasks
Law / Legal Reasoning
Limited (2 datasets)
Coverage restricted to few legal systems; broader legal diversity required
Poetry / Literature / Arts
Limited (3 datasets)
Creative language benchmarks remain narrow and genre-specific
Cultural Alignment & Dialect Evaluation
Strong (7 datasets)
Uneven dialectal representation and limited cultural depth
Commonsense & Cultural Reasoning
Limited (3 datasets)
Few tasks capture Arab-specific commonsense or pragmatic context
Hallucination / Truthfulness
Limited (3 datasets)
No standardized benchmark for measuring factual consistency
Retrieval-Augmented / Contextual Tasks
Limited (3 datasets)
Early research stage; grounding and factual retrieval need expansion
Table 1: Summary of Arabic NLP dataset coverage and key gaps. Coverage indicates the number of datasets per
task category, while Key Gaps outline remaining needs such as standardization, scale, and cultural balance.
8
Discussion
This section discusses key observations regarding
reproducibility practices, community initiatives,
methodological inconsistencies, and critical gaps
requiring future attention.
8.1
Reproducibility and Evaluation
Benchmarks
Reproducibility
is
fundamental
to
scientific
progress, yet our survey reveals significant het-
erogeneity in benchmark accessibility and trans-
parency. We classify benchmarks into three cate-
gories based on their openness:
Private Benchmarks release neither datasets nor
evaluation pipelines, severely limiting community
impact and making verification impossible. Ex-
amples include AraSTEM (11,637 samples) and
Halwasa (10K samples), which remain unavailable
despite published results.
Partially-Public Benchmarks release datasets but
withhold evaluation code, hindering exact reproduc-
tion due to ambiguities in preprocessing, prompt-
ing, and metric computation.
Public Benchmarks release both datasets and com-
plete pipelines, either through dedicated reposito-
ries (LAraBench, 3LM) or integration with main-
stream frameworks like lighteval (Habib et al.,
2023) and lm-eval-harness (Gao et al., 2024).
Our analysis reveals that approximately 25% of
surveyed benchmarks remain private or partially
public, limiting their impact towards Arabic NLP
community. We strongly advocate for complete
transparency as the community standard, recogniz-
ing that data contamination concerns can be ad-
dressed through alternative mechanisms such as
blind test sets (as employed by BALSAM), peri-
odic dataset refreshment, or held-out evaluation
techniques rather than complete privatization.
8.2
Methodological Inconsistencies and
Quality Issues
Through detailed examination of released bench-
marks, we identified several concerning inconsis-
tencies and quality issues that affect evaluation va-
lidity and cross-benchmark comparability.
Multiple-Choice Formatting. Benchmarks em-
ploy inconsistent option labeling: some use Latin
letters while others use Arabic letters. This incon-
sistency affects model performance as LLMs may
be more familiar with Latin alphabetic indices from
English pretraining. Standardization is needed for
fair cross-benchmark comparison.
Prompting Variations.
Few-shot evaluation
ranges from 0-shot to 5-shot with limited system-
atic investigation of optimal settings per task type.
Prompt phrasing varies from formal MSA to con-
versational styles, potentially affecting responses.
Quality Control Issues. Manual inspection re-
vealed typos, grammatical errors, and formatting
inconsistencies in several released datasets. Some
benchmarks contain culturally inappropriate con-
tent despite claims of cultural alignment. These
quality issues undermine benchmark validity and
highlight the need for rigorous review processes.
LLM-as-Judge Validation. While BALSAM re-
ports 0.824-0.977 correlation with human judg-
ments, most benchmarks adopting LLM-as-judge
lack validation specifically in Arabic contexts.
Judge model selection, prompt sensitivity, and po-
tential circular evaluation when judges resemble
evaluated models require systematic investigation.
8.3
Arabic LLM Leaderboards
Centralized leaderboards serve critical functions:
establishing performance baselines, enabling fair
model comparisons, tracking field progress over
time, and guiding model selection for practition-
ers. Several initiatives have emerged to fulfill these

--- Page 8 ---

roles for Arabic LLMs, each with distinct philoso-
phies and design choices.
The Open Arabic LLM Leaderboard (OALL)
(El Filali et al., 2024a) pioneered open-source
rankings, initially using Alghafa, EXAMS_ar, and
MMLU_ar. OALL v2 (El Filali et al., 2025) transi-
tioned to native benchmarks (ArabicMMLU, AL-
RAGE, AraTrust, MadinahQA), reflecting commu-
nity consensus against translated content. BAL-
SAM (Al-Matham et al., 2025) offers compre-
hensive evaluation across 78 tasks (52K samples)
with private test sets preventing contamination, in-
cluding both closed and open-source models. IL-
MAAM (Nacar et al., 2025) specializes in cultur-
ally aligned evaluation using refined ArabicMMLU
by ensuring religious sensitivity and social norms.
The AraGen benchmark (El Filali et al., 2024b)
and its associated leaderboard adopt a 3C3H evalu-
ation metric (Correctness, Completeness, Concise-
ness, Helpfulness, Honesty, Harmlessness), using
LLM-as-judge, and combine it with a dynamic,
blind-testing approaches to push for robust and fair
benchmarking of Arabic LLMs.
8.4
Critical Gaps
Despite substantial progress, several critical areas
remain underexplored or entirely absent from cur-
rent Arabic benchmarking efforts. Table 1 summa-
rizes the coverage of datasets per category as well
as key gaps.
Underexplored Areas.
Current benchmarks
lack temporal evaluation, multi-turn dialogue
assessment, code-switching evaluation (Arabic-
English/French mixing), low-resource dialect cov-
erage (Sudanese, Mauritanian), pragmatic under-
standing (sarcasm, indirect speech), and special-
ized domains beyond law/medicine (education,
journalism, technical documentation).
Methodological Challenges.
Data contamina-
tion threatens validity as training corpora expand.
Static benchmarks fail to capture temporal degrada-
tion. Cultural alignment lacks standardized metrics.
Heavy reliance on LLM-as-judge requires more
rigorous Arabic-specific validation.
Dataset Size Matters. As Figure 2 shows, bench-
mark sizes range from under 500 samples (Qiyas,
EXAMS_ar) to over 2 million (Dolphin). This
dramatic variability is consequential: small bench-
marks provide weaker statistical signals and are
more susceptible to overfitting, while aggregate
scores averaging across diverse benchmark sizes
can be misleading if not properly weighted. Evalu-
ation interpretation must account for dataset scale.
8.5
Recommendations
Through this study, we would like to recommend
researchers to (1) Prioritize native content with
mandatory cultural review. (2) Ensure complete re-
producibility through code release and framework
integration. (3) Address contamination via blind
test sets and adversarial filtering. (4) Standard-
ize prompting practices and multiple-choice for-
matting. (5) Validate evaluation methods against
diverse human judgments. (6) Expand dialectal
coverage systematically. (7) Implement rigorous
quality control processes. (8) Develop temporal
and dynamic evaluation mechanisms.
The Arabic NLP community must coordinate
on standardizing best practices, sharing evaluation
infrastructure, and prioritizing underexplored areas
to develop benchmarks that authentically capture
Arabic’s linguistic richness and cultural diversity.
9
Conclusion
This survey comprehensively reviews 40+ Arabic
LLM benchmarks, providing the first systematic
taxonomy across NLP tasks, knowledge domains,
cultural understanding, and specialized capabilities.
The field has evolved from task-specific datasets
(ARCD, TyDiQA) to comprehensive benchmarks
(BALSAM, LAraBench, ArabicMMLU) address-
ing understanding, generation, and reasoning.
Progress includes increased dialectal coverage,
cultural grounding, and domain diversity. However,
persistent challenges remain: data contamination,
cultural misalignment in translations, insufficient
coverage of temporal reasoning and multi-turn di-
alogue, and inconsistent reproducibility. Our rec-
ommendations emphasize reproducibility, cultural
authenticity, dialectal inclusivity, and methodolog-
ical rigor. As Arabic LLMs advance, evaluation
must authentically capture Arabic’s linguistic com-
plexity and cultural richness. This survey serves as
a comprehensive reference, guiding development
of more robust, culturally aligned Arabic LLM
evaluation.
Limitations
Despite our efforts to conduct a comprehensive re-
view, this survey has some limitations. The rapidly
evolving nature of Arabic LLM benchmarking
means recent or concurrent work may be excluded,
particularly proprietary benchmarks lacking public

--- Page 9 ---

documentation. Our review reflects benchmarks
through early 2025, and given the field’s acceler-
ating pace, information may quickly become out-
dated. Several benchmarks mentioned in publica-
tions (AraSTEM, Halwasa, Qiyas) remain unavail-
able, limiting our analysis to published descriptions
without independent verification.
We focus on evaluation benchmarks rather than
training datasets, emphasizing text-based and mul-
timodal evaluations while excluding speech-only
benchmarks. Our assessments of benchmark qual-
ity and cultural alignment necessarily reflect our
own perspectives; native speakers from different
regions may evaluate appropriateness differently.
Finally, our recommendations represent informed
opinions rather than community consensus, and our
classification of benchmarks as public or private
reflects information available at the time of writing,
which may have changed subsequently.
References
Samir Abdaljalil, Hasan Kurban, and Erchin Serpedin.
2025.
Halluverse25:
Fine-grained multilingual
benchmark dataset for llm hallucinations. Preprint,
arXiv:2503.07833.
Ahmed Abdelali, Hamdy Mubarak, Shammur Chowd-
hury, Maram Hasanain, Basel Mousi, Sabri Boughor-
bel, Samir Abdaljalil, Yassine El Kheir, Daniel Izham,
Fahim Dalvi, Majd Hawasly, Nizi Nazar, Youssef
Elshahawy, Ahmed Ali, Nadir Durrani, Natasa Milic-
Frayling, and Firoj Alam. 2024. LAraBench: Bench-
marking Arabic AI with large language models. In
Proceedings of the 18th Conference of the European
Chapter of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 487–520,
St. Julian’s, Malta. Association for Computational
Linguistics.
Muhammad Abdul-Mageed, Amr Keleg, AbdelRahim
Elmadany, Chiyu Zhang, Injy Hamed, Walid Magdy,
Houda Bouamor, and Nizar Habash. 2024. Nadi
2024: The fifth nuanced arabic dialect identification
shared task. arXiv preprint arXiv:2407.04910.
aiastrolabe. 2025. Redteaming frontier llms with ai
astrolabe arabic safety index (asas). Accessed: Oct.
3, 2025.
Shahad Al-Khalifa and Hend Al-Khalifa. 2024. The
qiyas benchmark: Measuring chatgpt mathematical
and language understanding in arabic. arXiv preprint
arXiv:2407.00146.
Shahad Al-Khalifa, Nadir Durrani, Hend Al-Khalifa,
and Firoj Alam. 2025. The landscape of arabic large
language models. Communications of the ACM.
Nashwan Ahmed Al-Majmar, Hezam Gawbah, and
Akram Alsubari. 2024.
Ahd: Arabic healthcare
dataset. Data in Brief, 56:110855.
Rawan Al-Matham, Kareem Darwish, Raghad Al-
Rasheed, Waad Alshammari, Muneera Alhoshan,
Amal Almazrua, Asma Al Wazrah, Mais Alheraki,
Firoj Alam, Preslav Nakov, Norah Alzahrani, Eman
alBilali, Nizar Habash, Abdelrahman El-Sheikh,
Muhammad Elmallah, Haonan Li, Hamdy Mubarak,
Mohamed Anwar, Zaid Alyafeai, and 24 others. 2025.
Balsam: A platform for benchmarking arabic large
language models. Preprint, arXiv:2507.22603.
Renad Al-Monef, Hassan Alhuzali, Nora Alturayeif,
and Ashwag Alasmari. 2025. Absher: A benchmark
for evaluating large language models’ understanding
of saudi dialects. Preprint, arXiv:2507.10216.
Aisha Alansari and Hamzah Luqman. 2025. Arahallue-
val: A fine-grained hallucination evaluation frame-
work for arabic llms. Preprint, arXiv:2509.04656.
Ashwag Alasmari, Sarah Alhumoud, and Waad Alsham-
mari. 2024. Aramed: Arabic medical question an-
swering using pretrained transformer language mod-
els. In Proceedings of the 6th Workshop on Open-
Source Arabic Corpora and Processing Tools (OS-
ACT) with Shared Tasks on Arabic LLMs Halluci-
nation and Dialect to MSA Machine Translation@
LREC-COLING 2024, pages 50–56.
Safa AlBallaa, Nora AlTwairesh, Abdulmalik AlSalman,
and Sultan Alfarhood. 2025.
Gatmath and gatlc:
Comprehensive benchmarks for evaluating arabic
large language models. PLoS One, 20(9):e0329129.
Hayfa A Aleid and Aqil M Azmi. 2025. Hajj-fqa: A
benchmark arabic dataset for developing question-
answering systems on hajj fatwas: H. aleid and a.
azmi. Journal of King Saud University Computer
and Information Sciences, 37(6):135.
Wafa Alghallabi, Ritesh Thawkar, Sara Ghaboura, Ke-
tan More, Omkar Thawakar, Hisham Cholakkal,
Salman Khan, and Rao Muhammad Anwer. 2025.
Fann or flop: A multigenre, multiera benchmark for
arabic poetry understanding in llms. arXiv preprint
arXiv:2505.18152.
Emad A. Alghamdi, Reem I. Masoud, Deema Alnuhait,
Afnan Y. Alomairi, Ahmed Ashraf, and Mohamed Za-
ytoon. 2024. Aratrust: An evaluation of trustworthi-
ness for llms in arabic. Preprint, arXiv:2403.09017.
Mohamed Alkaoud. 2024. A bilingual benchmark for
evaluating large language models. PeerJ Computer
Science, 10:e1893.
Ebtesam Almazrouei, Ruxandra Cojocaru, Michele
Baldo, Quentin Malartic, Hamza Alobeidli, Daniele
Mazzotta, Guilherme Penedo, Giulia Campesan, Mu-
gariya Farooq, Maitha Alhammadi, Julien Launay,
and Badreddine Noune. 2023. AlGhafa evaluation
benchmark for Arabic language models. In Proceed-
ings of ArabicNLP 2023, pages 244–275, Singapore
(Hybrid). Association for Computational Linguistics.

--- Page 10 ---

Rana Alshaikh, Israa Alghanmi, and Shelan Jeawak.
2025.
Aratable: Benchmarking llms’ reasoning
and understanding of arabic tabular data. Preprint,
arXiv:2507.18442.
Fakhraddin Alwajih, Abdellah El Mekki, Samar Mo-
hamed Magdy, AbdelRahim A. Elmadany, Omer
Nacar, El Moatez Billah Nagoudi, Reem Abdel-
Salam, Hanin Atwany, Youssef Nafea, Abdulfat-
tah Mohammed Yahya, Rahaf Alhamouri, Hamzah A.
Alsayadi,
Hiba Zayed,
Sara Shatnawi,
Serry
Sibaee, Yasir Ech-chammakhy, Walid Al-Dhabyani,
Marwa Mohamed Ali, Imen Jarraya, and 25 others.
2025a. Palm: A culturally inclusive and linguistically
diverse dataset for Arabic LLMs. In Proceedings
of the 63rd Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 32871–32894, Vienna, Austria. Association
for Computational Linguistics.
Fakhraddin Alwajih, Abdellah El Mekki, Hamdy
Mubarak, Majd Hawasly, Abubakr Mohamed, and
Muhammad Abdul-Mageed. 2025b. Palmx 2025:
The first shared task on benchmarking llms on arabic
and islamic culture. Preprint, arXiv:2509.02550.
Fakhraddin Alwajih, El Moatez Billah Nagoudi, Gagan
Bhatia, Abdelrahman Mohamed, and Muhammad
Abdul-Mageed. 2024. Peacock: A family of arabic
multimodal large language models and benchmarks.
Preprint, arXiv:2403.01031.
Anthropic. 2024. Introducing the next generation of
claude.
Wissam Antoun, Fady Baly, and Hazem Hajj. 2021.
AraGPT2: Pre-trained transformer for Arabic lan-
guage generation. In Proceedings of the Sixth Ara-
bic Natural Language Processing Workshop, pages
196–207, Kyiv, Ukraine (Virtual). Association for
Computational Linguistics.
Yasser Ashraf, Yuxia Wang, Bin Gu, Preslav Nakov,
and Timothy Baldwin. 2025. Arabic dataset for llm
safeguard evaluation. Preprint, arXiv:2410.17040.
Jacob Austin, Augustus Odena, Maxwell Nye, Maarten
Bosma, Henryk Michalewski, David Dohan, Ellen
Jiang, Carrie Cai, Michael Terry, Quoc Le, and
Charles Sutton. 2021. Program synthesis with large
language models. Preprint, arXiv:2108.07732.
Stephen H. Bach, Victor Sanh, Zheng-Xin Yong, Albert
Webson, Colin Raffel, Nihal V. Nayak, Abheesht
Sharma, Taewoon Kim, M Saiful Bari, Thibault
Fevry, Zaid Alyafeai, Manan Dey, Andrea Santilli,
Zhiqing Sun, Srulik Ben-David, Canwen Xu, Gun-
jan Chhablani, Han Wang, Jason Alan Fries, and 8
others. 2022. Promptsource: An integrated develop-
ment environment and repository for natural language
prompts. Preprint, arXiv:2202.01279.
Adil Bahaj and Mounir Ghogho. 2025.
Mizanqa:
Benchmarking large language models on moroc-
can legal question answering.
arXiv preprint
arXiv:2508.16357.
Basma El Amel Boussaha, Leen AlQadi, Mugariya Fa-
rooq, Shaikha Alsuwaidi, Giulia Campesan, Ahmed
Alzubaidi, Mohammed Alyafeai, and Hakim Hacid.
2025. 3lm: Bridging arabic, stem, and code through
benchmarking. arXiv preprint arXiv:2507.15850.
Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan,
Henrique Ponde de Oliveira Pinto, Jared Kaplan,
Harri Edwards, Yuri Burda, Nicholas Joseph, Greg
Brockman, Alex Ray, Raul Puri, Gretchen Krueger,
Michael Petrov, Heidy Khlaaf, Girish Sastry, Pamela
Mishkin, Brooke Chan, Scott Gray, and 39 others.
2021. Evaluating large language models trained on
code. Preprint, arXiv:2107.03374.
Jonathan H. Clark, Eunsol Choi, Michael Collins,
Dan Garrette, Tom Kwiatkowski, Vitaly Nikolaev,
and Jennimaria Palomaki. 2020.
Tydi qa:
A
benchmark for information-seeking question answer-
ing in typologically diverse languages.
Preprint,
arXiv:2003.05002.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro
Nakano, Christopher Hesse, and John Schulman.
2021. Training verifiers to solve math word prob-
lems. arXiv preprint arXiv:2110.14168.
Mouath Abu Daoud,
Chaimae Abouzahir,
Leen
Kharouf, Walid Al-Eisawi, Nizar Habash, and
Farah E Shamout. 2025. Medarabiq: Benchmark-
ing large language models on arabic medical tasks.
arXiv preprint arXiv:2505.03427.
Yann Dubois, Xuechen Li, Rohan Taori, Tianyi Zhang,
Ishaan Gulrajani, Jimmy Ba, Carlos Guestrin, Percy
Liang, and Tatsunori B. Hashimoto. 2023. Alpaca-
farm: A simulation framework for methods that learn
from human feedback. Preprint, arXiv:2305.14387.
Ali El Filali, Hamza Alobeidli, Clémentine Fourrier,
Basma El Amel Boussaha, Ruxandra Cojocaru,
Nathan Habib, and Hakim Hacid. 2024a. Open ara-
bic llm leaderboard.
https://huggingface.co/
spaces/OALL/Open-Arabic-LLM-Leaderboard.
Ali El Filali, Manel ALOUI, Tarique Husaain, Ahmed
Alzubaidi, Basma El Amel Boussaha, Ruxandra
Cojocaru, Clémentine Fourrier, Nathan Habib, and
Hakim Hacid. 2025. The open arabic llm leader-
board 2. https://huggingface.co/spaces/OALL/Open-
Arabic-LLM-Leaderboard.
Ali El Filali, Neha Sengupta, Abouelseoud, Preslav
Nakov, and Clémentine Fourrier. 2024b. Rethinking
llm evaluation with 3c3h: Aragen benchmark and
leaderboard. https://https://huggingface.co/
blog/leaderboard-3c3h-aragen.
AbdelRahim Elmadany, El Moatez Billah Nagoudi, and
Muhammad Abdul-Mageed. 2023. Orca: A challeng-
ing benchmark for arabic language understanding.
Preprint, arXiv:2212.10758.

--- Page 11 ---

Leo Gao, Jonathan Tow, Baber Abbasi, Stella Bider-
man, Sid Black, Anthony DiPofi, Charles Foster,
Laurence Golding, Jeffrey Hsu, Alain Le Noac’h,
Haonan Li, Kyle McDonell, Niklas Muennighoff,
Chris Ociepa, Jason Phang, Laria Reynolds, Hailey
Schoelkopf, Aviya Skowron, Lintang Sutawika, and
5 others. 2024. The language model evaluation har-
ness.
Sara Ghaboura, Ahmed Heakl, Omkar Thawakar, Ali Al-
harthi, Ines Riahi, Abduljalil Saif, Jorma Laaksonen,
Fahad S. Khan, Salman Khan, and Rao M. Anwer.
2024. Camel-bench: A comprehensive arabic lmm
benchmark. Preprint, arXiv:2410.18976.
Sara Ghaboura, Ketan More, Wafa Alghallabi, Omkar
Thawakar, Jorma Laaksonen, Hisham Cholakkal,
Salman Khan, and Rao Muhammad Anwer. 2025.
Arb: A comprehensive arabic multimodal reasoning
benchmark. Preprint, arXiv:2505.17021.
Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri,
Abhinav Pandey, Abhishek Kadian, Ahmad Al-
Dahle, Aiesha Letman, Akhil Mathur, Alan Schel-
ten, Alex Vaughan, Amy Yang, Angela Fan, Anirudh
Goyal, Anthony Hartshorn, Aobo Yang, Archi Mi-
tra, Archie Sravankumar, Artem Korenev, Arthur
Hinsvark, and 542 others. 2024. The llama 3 herd of
models. Preprint, arXiv:2407.21783.
Neel Guha, Julian Nyarko, Daniel E. Ho, Christo-
pher Ré, Adam Chilton, Aditya Narayana, Alex
Chohlas-Wood, Austin Peters, Brandon Waldon,
Daniel N. Rockmore, Diego Zambrano, Dmitry Tal-
isman, Enam Hoque, Faiz Surani, Frank Fagan, Galit
Sarfaty, Gregory M. Dickinson, Haggai Porat, Ja-
son Hegland, and 21 others. 2023. Legalbench: A
collaboratively built benchmark for measuring le-
gal reasoning in large language models. Preprint,
arXiv:2308.11462.
Nathan Habib, Clémentine Fourrier, Hynek Kydlíˇcek,
Thomas Wolf, and Lewis Tunstall. 2023. Lighteval:
A lightweight framework for llm evaluation.
Momchil
Hardalov,
Todor
Mihaylov,
Dimitrina
Zlatkova, Yoan Dinkov, Ivan Koychev, and Preslav
Nakov. 2020.
Exams:
A multi-subject high
school examinations dataset for cross-lingual and
multilingual question answering.
arXiv preprint
arXiv:2011.03080.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2020. Measuring massive multitask language under-
standing. arXiv preprint arXiv:2009.03300.
Faris Hijazi, Somayah AlHarbi, Abdulaziz AlHussein,
Harethah Abu Shairah, Reem AlZahrani, Hebah Al-
Shamlan, Omar Knio, and George Turkiyyah. 2024.
Arablegaleval: A multitask benchmark for assess-
ing arabic legal knowledge in large language models.
arXiv preprint arXiv:2408.07983.
Huang Huang, Fei Yu, Jianqing Zhu, Xuening Sun, Hao
Cheng, Dingjie Song, Zhihong Chen, Abdulmohsen
Alharthi, Bang An, Juncai He, Ziche Liu, Zhiyi
Zhang, Junying Chen, Jianquan Li, Benyou Wang,
Lian Zhang, Ruoyu Sun, Xiang Wan, Haizhou Li, and
Jinchao Xu. 2024. Acegpt, localizing large language
models in arabic. Preprint, arXiv:2309.12053.
Kaiyu Huang, Fengran Mo, Xinyu Zhang, Hongliang
Li, You Li, Yuanchi Zhang, Weijian Yi, Yulong Mao,
Jinchen Liu, Yuzhuang Xu, Jinan Xu, Jian-Yun Nie,
and Yang Liu. 2025. A survey on large language
models with multilingualism: Recent advances and
new frontiers. Preprint, arXiv:2405.10936.
Amr Keleg, Sharon Goldwater, and Walid Magdy. 2025.
Revisiting common assumptions about arabic dialects
in nlp. arXiv preprint arXiv:2505.21816.
Fajri Koto, Haonan Li, Sara Shatnawi, Jad Doughman,
Abdelrahman Sadallah, Aisha Alraeesi, Khalid Al-
mubarak, Zaid Alyafeai, Neha Sengupta, Shady She-
hata, Nizar Habash, Preslav Nakov, and Timothy
Baldwin. 2024. ArabicMMLU: Assessing massive
multitask language understanding in Arabic. In Find-
ings of the Association for Computational Linguistics:
ACL 2024, pages 5622–5640, Bangkok, Thailand. As-
sociation for Computational Linguistics.
Anis Koubaa, Adel Ammar, Lahouari Ghouti, Omar
Najar, and Serry Sibaee. 2024. Arabiangpt: Native
arabic gpt-based large language model. Preprint,
arXiv:2402.15313.
Stephanie Lin, Jacob Hilton, and Owain Evans. 2022.
Truthfulqa: Measuring how models mimic human
falsehoods. Preprint, arXiv:2109.07958.
Samar Mohamed Magdy, Sang Yun Kwon, Fakhraddin
Alwajih, Safaa Taher Abdelfadil, Shady Shehata, and
Muhammad Abdul-Mageed. 2025. JAWAHER: A
multidialectal dataset of Arabic proverbs for LLM
benchmarking. In Proceedings of the 2025 Confer-
ence of the Nations of the Americas Chapter of the
Association for Computational Linguistics: Human
Language Technologies (Volume 1: Long Papers),
pages 12320–12341, Albuquerque, New Mexico. As-
sociation for Computational Linguistics.
Malak Mashaabi, Shahad Al-Khalifa, and Hend Al-
Khalifa. 2024. A survey of large language models
for arabic language and its dialects. arXiv preprint
arXiv:2410.20238.
Basel Mousi, Nadir Durrani, Fatema Ahmad, Md. Arid
Hasan, Maram Hasanain, Tameem Kabbani, Fahim
Dalvi, Shammur Absar Chowdhury, and Firoj Alam.
2025. AraDiCE: Benchmarks for dialectal and cul-
tural capabilities in LLMs. In Proceedings of the
31st International Conference on Computational Lin-
guistics, pages 4186–4218, Abu Dhabi, UAE. Asso-
ciation for Computational Linguistics.
Hussein Mozannar, Karl El Hajal, Elie Maamary, and
Hazem M. Hajj. 2019. Neural arabic question an-
swering. CoRR, abs/1906.05394.

--- Page 12 ---

Hamdy Mubarak, Hend Al-Khalifa, and Khaloud Suli-
man Alkhalefah. 2024. Halwasa: Quantify and ana-
lyze hallucinations in large language models: Arabic
as a case study. In Proceedings of the 2024 Joint
International Conference on Computational Linguis-
tics, Language Resources and Evaluation (LREC-
COLING 2024), pages 8008–8015, Torino, Italia.
ELRA and ICCL.
Niklas Muennighoff, Thomas Wang, Lintang Sutawika,
Adam Roberts, Stella Biderman, Teven Le Scao,
M Saiful Bari, Sheng Shen, Zheng Xin Yong, Hai-
ley Schoelkopf, Xiangru Tang, Dragomir Radev, Al-
ham Fikri Aji, Khalid Almubarak, Samuel Albanie,
Zaid Alyafeai, Albert Webson, Edward Raff, and
Colin Raffel. 2023a.
Crosslingual generalization
through multitask finetuning. In Proceedings of the
61st Annual Meeting of the Association for Com-
putational Linguistics (Volume 1: Long Papers),
pages 15991–16111, Toronto, Canada. Association
for Computational Linguistics.
Niklas Muennighoff, Thomas Wang, Lintang Sutawika,
Adam Roberts, Stella Biderman, Teven Le Scao,
M Saiful Bari, Sheng Shen, Zheng-Xin Yong, Hai-
ley Schoelkopf, Xiangru Tang, Dragomir Radev,
Alham Fikri Aji, Khalid Almubarak, Samuel Al-
banie, Zaid Alyafeai, Albert Webson, Edward Raff,
and Colin Raffel. 2023b.
Crosslingual general-
ization through multitask finetuning.
Preprint,
arXiv:2211.01786.
Ahmad Mustapha, Hadi Al-Khansa, Hadi Al-Mubasher,
Aya Mourad, Ranam Hamoud, Hasan El-Husseini,
Marwah Al-Sakkaf, and Mariette Awad. 2024.
Arastem: A native arabic multiple choice question
benchmark for evaluating llms knowledge in stem
subjects. arXiv preprint arXiv:2501.00559.
Omer Nacar, Serry Taiseer Sibaee, Samar Ahmed, Safa
Ben Atitallah, Adel Ammar, Yasser Alhabashi, Ab-
dulrahman S. Al-Batati, Arwa Alsehibani, Nour Qan-
dos, Omar Elshehy, Mohamed Abdelkader, and Anis
Koubaa. 2025. Towards inclusive Arabic LLMs: A
culturally aligned benchmark in Arabic large lan-
guage model evaluation. In Proceedings of the First
Workshop on Language Models for Low-Resource
Languages, pages 387–401, Abu Dhabi, United Arab
Emirates. Association for Computational Linguistics.
El Moatez Billah Nagoudi, AbdelRahim Elmadany,
Ahmed Oumar El-Shangiti, and Muhammad Abdul-
Mageed. 2023. Dolphin: A challenging and diverse
benchmark for Arabic NLG. In Findings of the As-
sociation for Computational Linguistics: EMNLP
2023, pages 1404–1422, Singapore. Association for
Computational Linguistics.
Humza Naveed, Asad Ullah Khan, Shi Qiu, Muhammad
Saqib, Saeed Anwar, Muhammad Usman, Naveed
Akhtar, Nick Barnes, and Ajmal Mian. 2025. A com-
prehensive overview of large language models. ACM
Transactions on Intelligent Systems and Technology,
16(5):1–72.
Omartificial-Intelligence-Space.
2025.
Ara-
bic
gsm8k:
Arabic
grade
school
math
dataset.
https://huggingface.co/datasets/
Omartificial-Intelligence-Space/
Arabic-gsm8k-v2.
OpenAI. 2023. Chatgpt. https://chat.openai.com/
chat. Accessed: 2 October 2025.
OpenAI, Josh Achiam, Steven Adler, Sandhini Agarwal,
Lama Ahmad, Ilge Akkaya, Florencia Leoni Ale-
man, Diogo Almeida, Janko Altenschmidt, Sam Alt-
man, Shyamal Anadkat, Red Avila, Igor Babuschkin,
Suchir Balaji, Valerie Balcom, Paul Baltescu, Haim-
ing Bao, Mohammad Bavarian, Jeff Belgum, and
262 others. 2024. Gpt-4 technical report. Preprint,
arXiv:2303.08774.
Zhaozhi Qian, Faroq Altam, Muhammad Alqurishi, and
Riad Souissi. 2024. Cameleval: Advancing cultur-
ally aligned arabic language models and benchmarks.
Preprint, arXiv:2409.12623.
Alec Radford, Jong Wook Kim, Tao Xu, Greg Brock-
man, Christine McLeavey, and Ilya Sutskever. 2023.
Robust speech recognition via large-scale weak super-
vision. In Proceedings of the 40th International Con-
ference on Machine Learning, ICML’23. JMLR.org.
Haneh Rhel and Dmitri Roussinov. 2025. Large lan-
guage models and arabic content: a review. arXiv
preprint arXiv:2505.08004.
Nathaniel R. Robinson, Shahd Abdelmoneim, Kelly
Marchisio, and Sebastian Ruder. 2025. Al-qasida:
Analyzing llm quality and accuracy systematically in
dialectal arabic. In Findings of the Association for
Computational Linguistics: ACL 2025.
Abdelrahman Sadallah, Junior Cedric Tonga, Khalid
Almubarak, Saeed Almheiri, Farah Atif, Chatrine
Qwaider, Karima Kadaoui, Sara Shatnawi, Yaser
Alesh, and Fajri Koto. 2025.
Commonsense rea-
soning in Arab culture. In Proceedings of the 63rd
Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 7695–
7710, Vienna, Austria. Association for Computa-
tional Linguistics.
Neha Sengupta, Sunil Kumar Sahu, Bokang Jia,
Satheesh Katipomu, Haonan Li, Fajri Koto, William
Marshall, Gurpreet Gosal, Cynthia Liu, Zhim-
ing Chen, Osama Mohammed Afzal, Samta Kam-
boj, Onkar Pandit, Rahul Pal, Lalit Pradhan,
Zain Muhammad Mujahid, Massa Baali, Xudong
Han, Sondos Mahmoud Bsharat, and 13 others. 2023.
Jais and jais-chat: Arabic-centric foundation and
instruction-tuned open generative large language
models. Preprint, arXiv:2308.16149.
Sumuk Shashidhar, Clémentine Fourrier, Alina Lo-
zovskia, Thomas Wolf, Gokhan Tur, and Dilek
Hakkani-Tür. 2025. Yourbench: Easy custom evalua-
tion sets for everyone. Preprint, arXiv:2504.01833.

--- Page 13 ---

Fanar Team, Ummar Abbas, Mohammad Shahmeer Ah-
mad, Firoj Alam, Enes Altinisik, Ehsannedin Asgari,
Yazan Boshmaf, Sabri Boughorbel, Sanjay Chawla,
Shammur Chowdhury, Fahim Dalvi, Kareem Dar-
wish, Nadir Durrani, Mohamed Elfeky, Ahmed El-
magarmid, Mohamed Eltabakh, Masoomali Fatehkia,
Anastasios Fragkopoulos, Maram Hasanain, and 23
others. 2025a. Fanar: An arabic-centric multimodal
generative ai platform. Preprint, arXiv:2501.13944.
Gemma Team, Aishwarya Kamath, Johan Ferret, Shreya
Pathak, Nino Vieillard, Ramona Merhej, Sarah Perrin,
Tatiana Matejovicova, Alexandre Ramé, Morgane
Rivière, Louis Rouillard, Thomas Mesnard, Geoffrey
Cideron, Jean bastien Grill, Sabela Ramos, Edouard
Yvinec, Michelle Casbon, Etienne Pot, Ivo Penchev,
and 197 others. 2025b. Gemma 3 technical report.
Preprint, arXiv:2503.19786.
Silma Team. 2024. Silma.
TII. 2025. Falcon-arabic: A breakthrough in arabic
language models.
Yizhong Wang, Swaroop Mishra, Pegah Alipoor-
molabashi,
Yeganeh Kordi,
Amirreza Mirzaei,
Anjana Arunkumar, Arjun Ashok, Arut Selvan
Dhanasekaran, Atharva Naik, David Stap, Eshaan
Pathak, Giannis Karamanolakis, Haizhi Gary Lai, Is-
han Purohit, Ishani Mondal, Jacob Anderson, Kirby
Kuznia, Krima Doshi, Maitreya Patel, and 21 others.
2022. Super-naturalinstructions: Generalization via
declarative instructions on 1600+ nlp tasks. Preprint,
arXiv:2204.07705.
An Yang, Anfeng Li, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao,
Chengen Huang, Chenxu Lv, Chujie Zheng, Day-
iheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao
Ge, Haoran Wei, Huan Lin, Jialong Tang, and 41
others. 2025.
Qwen3 technical report.
Preprint,
arXiv:2505.09388.
A
Summary Table
Table 2 provides a comprehensive overview of all
the Arabic LLM benchmarks reviewed in this sur-
vey. This appendix clarifies abbreviations and high-
lights key insights for interpreting the data.
A.1
Column Definitions
Sample Composition Columns:
• NAT: Natively authored Arabic samples (orig-
inally created in Arabic by native speakers)
• SYN: Synthetically generated samples (cre-
ated using LLMs like GPT-4, Claude, or
Llama)
• TRAN: Translated samples (translated from
English or other languages to Arabic)
• Total: Total benchmark size
Evaluation Details:
• Metrics: Evaluation metrics employed (e.g.,
Accuracy, F1, BLEU, ROUGE, LLM-as-
Judge)
• Type:
Question
format
-
MCQ
(Multiple-choice), GEN (Generative/open-
ended),BENCH
(Multi-task
suite),
CL
(Classification), RS (Reasoning Steps)
Accessibility:
• PD (Public Dataset): Yes (publicly avail-
able), No (private/request-only), Partial (sub-
set public)
• PR (Public Repository): Yes (complete eval-
uation code available), No (no public reposi-
tory)
Notation: "–" (not available/applicable), "k"
(thousands), "m" (millions), "DS" (datasets)
A.2
Key Insights from the Table
Dataset Composition Trends:
• Native vs.
Translated:
Early bench-
marks (2020) relied heavily on translation
(MMLU_ar: 100% translated), while recent
benchmarks (2024-2025) prioritize native con-
tent (ArabicMMLU, GATmath: 100% native),
reflecting community consensus on cultural
authenticity.

--- Page 14 ---

• Synthetic Generation: Recent benchmarks
increasingly employ synthetic generation
(ALRAGE: 21.2k synthetic, ArabLegalEval:
10.58k synthetic), balancing scale with cost.
However, purely native benchmarks like Jawa-
her (10k native) and Absher (18k native)
demonstrate that large-scale native collection
remains feasible.
• Hybrid Approaches: BALSAM exemplifies
effective hybrid strategy (26k native, 1.7k syn-
thetic, 24k translated), combining strengths of
multiple approaches.
Scale Distribution:
• Large-Scale:
Dolphin (2m samples) and
LAraBench (296k) represent comprehensive
multi-task benchmarks.
• Medium-Scale:
Most benchmarks range
from 1k-20k samples, balancing quality and
coverage.
• Specialized: Domain-specific benchmarks
(legal, medical) tend toward smaller, higher-
quality datasets (1-7k samples).
Reproducibility Concerns:
• Fully Accessible: Only 21 of 41 benchmarks
provide both public datasets and repositories.
• Dataset-Only: 8 benchmarks release datasets
without evaluation code, hindering exact re-
production.
• Private: 9 benchmarks remain completely
private such as AraST EM, Halwasa, CamelE-
val and Qiyas, including some with substan-
tial contributions (AraST EM: 11.6k samples),
severely limiting community impact.
• Critical Gap: The high proportion of inacces-
sible benchmarks impedes scientific progress
and independent validation.
Evaluation Methodology Evolution:
• Traditional Metrics:
Early benchmarks
use standard metrics (Accuracy, F1, BLEU,
ROUGE).
• LLM-as-Judge: Recent benchmarks increas-
ingly adopt LLM-as-judge (BALSAM, AL-
RAGE, ArabLegalEval), particularly for gen-
erative tasks, though validation against human
judgments remains limited.
• Human Evaluation: Hallucination bench-
marks (AraHalluEval, Halwasa) maintain
human-as-judge given the critical nature of
the task, despite higher costs.
Task Coverage Patterns:
• NLP Tasks:
Well-covered with multiple
comprehensive benchmarks (ORCA, Dolphin,
LAraBench, BALSAM).
• STEM: Substantial progress with native
benchmarks (ArabicMMLU, AraST EM,
GATmath) addressing earlier translation limi-
tations.
• Culture & Dialects: Growing emphasis (7
benchmarks in 2025 alone), reflecting recog-
nition of cultural alignment importance.
• Target-Specific: Emerging area with recent
focus on hallucination detection and context-
based reasoning.
Temporal Distribution: Most benchmarks were
released in 2024-2025, indicating rapid field ac-
celeration. However, this concentration also sug-
gests potential redundancy in some areas (multiple
GAT-based benchmarks) while other areas remain
unexplored (temporal evaluation, code-switching,
multi-turn dialogue).
Geographic and Cultural Bias: Several bench-
marks focus on specific regional variants (Absher:
Saudi dialect, MizanQA: Moroccan law, GAT-
math: Saudi standardized tests), highlighting both
progress in regional representation and gaps in
coverage of other Arabic-speaking regions (North
Africa, Levant, Iraq).
B
Arabic NLP Benchmarks Timeline
Figure 3 presents a timeline of Arabic benchmark
releases from 2019 to 2025, categorized by our
four-category taxonomy. The visualization reveals
dramatic acceleration in benchmark development,
with 82% of all benchmarks (34 of 41) released in
2024-2025 alone. This recent surge reflects grow-
ing recognition of Arabic LLM evaluation needs
and demonstrates rapid field maturation across all
categories, particularly in cultural/dialectal assess-
ment where all 7 benchmarks emerged in 2025.

--- Page 15 ---

Year
Paper
Topic
NAT
SYN
TRAN
Total
Metrics
Type
PD
PR
Knowledge
2020
MMLU_ar (Hendrycks et al., 2020)
Humanities • Social Science • STEM
-
-
15k
15k
Accuracy • Log-prob
MCQ
Yes
Yes
2020
EXAMS_ar (Hardalov et al., 2020)
Science • Social Science • Religion
0.5k
-
-
0.5k
Accuracy • Log-prob
MCQ
Yes
Yes
2024
ArabicMMLU (Koto et al., 2024)
Humanities • Social Science • STEM • Arabic Language
14.57k
-
-
14.57k
Accuracy • Log-prob
MCQ
Yes
Yes
2024
AraSTEM (Mustapha et al., 2024)
STEM
11.63k
-
-
11.63k
Accuracy • Log-prob
MCQ
No
No
2024
GAT (Alkaoud, 2024)
Linguistic Abilities
0.45k
-
-
0.56k
Accuracy
MCQ
No
No
2024
Qiyas (Al-Khalifa and Al-Khalifa, 2024)
Linguistic Abilities • Mathematics
2.4k
-
-
2.4k
Accuracy
MCQ
No
No
2024
ArabLegalEval (Hijazi et al., 2024)
Law
79
10.58k
15.8
26.4k
Accuracy • LLM-as-Judge
MCQ, GEN
Yes
Yes
2024
AraMed (Alasmari et al., 2024)
Medical Domain • Healthcare
270k
-
-
270k
Accuracy • QA Metrics
GEN
Yes
Yes
2025
MizanQA (Bahaj and Ghogho, 2025)
Law
1.7k
-
-
1.7k
Accuracy • F1 • ECE
MCQ
Yes
No
2025
Fann or Flop (Alghallabi et al., 2025)
Poetry
6.9k
-
-
6.9k
BLEU • chrf(++) • BERTScore
GEN
Yes
Yes
2025
GATmath, GATLc (AlBallaa et al., 2025)
Linguistic Abilities • Mathematics
9k
-
-
9k
Accuracy
MCQ
Yes
No
2025
3LM (Boussaha et al., 2025)
STEM • Coding
0.8k
1.74k
0.54k
3.1k
Accuracy • Log-prob
MCQ, GEN
Yes
Yes
2025
Arabic-GSM8K (Omartificial-Intelligence-Space, 2025)
Mathematics • Reasoning
-
-
8.9k
8.9k
Exact-Match
GEN
Yes
No
2025
MedArabiQ (Daoud et al., 2025)
Medical
-
0.7k
-
0.7k
Accuracy • BERTScore
MCQ
Yes
Yes
2025
Hajj-FAQ (Aleid and Azmi, 2025)
Religious Domain • Islamic Jurisprudence
1.2k
-
-
1.2k
Accuracy • F1
QA
No
No
Arabic NLP Tasks
2019
ARCD (Mozannar et al., 2019)
Reading Comprehension
1.4k
-
-
1.4k
EM • F1
MCQ
Yes
Yes
2020
TyDiQA (Ar) (Clark et al., 2020)
Reading Comprehension
14k
-
-
14k
EM • F1
GEN
Yes
Yes
2023
ORCA (Elmadany et al., 2023)
Sentiment • Text Classification • NER • QA • Paraphrase • NLI •
Dialect ID • MT
-
-
-
588k
Accuracy • F1 • Pearson • EM
BENCH
Yes
No
2023
Dolphin (Nagoudi et al., 2023)
QA • Reading Comprehension • Reasoning • Math • Commonsense
• Dialogue • Summarization • Paraphrasing • Writing
-
-
-
2m
BLEU • ROUGE • METEOR • BERTScore
BENCH
No
No
2023
Alghafa (Almazrouei et al., 2023)
Reading Comprehension • Sentiment Analysis • QA
33.2k
-
-
33.2k
Accuracy • Log-prob
MCQ
Yes
Yes
2024
LAraBench (Abdelali et al., 2024)
Sentiment • Topic Classification • NER • QA • Paraphrase • NLI •
Dialect ID • MT • Reasoning • Summarization
296k
-
-
296k
F1 • BLEU • Task-specific
BENCH
Yes
Yes
2025
BALSAM (Al-Matham et al., 2025)
MT • Transliteration • DialectMT • Simplification • QRewrite •
Paraphrase • Intent • GrammarCorr • GenderRewrite • TextClass •
Sentiment • Sarcasm • DialectID • Command • Summarization •
SubjectGen • AnswerExt • SeqTag
26k
1.7k
24k
52k
LLM-as-Judge • BLEU • ROUGE
BENCH
Partial
Yes
Culture and dialects Tasks
2025
Jawaher (Magdy et al., 2025)
Proverbs • Figurative QA
10k
-
-
10k
BLEURT • BERTScore • LLM-as-Judge • Human-as-Judge
GEN
Yes
No
2025
PALM (Alwajih et al., 2025a)
Prose • Dialogue • Cultural Expressions
17.4k
-
-
17.4k
LLM-as-Judge
GEN
Yes
Yes
2025
PalmX (Alwajih et al., 2025b)
Shared Task • Arabic Culture MCQs • Islamic Culture MCQs
-
6.4k
-
6.4k
Accuracy, Log-prob
MCQ
Yes
No
2025
Commonsense Reasoning in Arab Culture (Sadallah et al., 2025)
Cultural Commonsense QA
3.5k
-
-
3.5k
Accuracy • Log-prob
MCQ
Yes
Yes
2025
AraDiCE (Mousi et al., 2025)
Dialect Identification/Generation/Translation • Cognitive Abilities
on Dialect * Culture
41.8k
-
45k
81,8k
Accuracy
BENCH
Yes
Yes
2025
AL-QASIDA (Robinson et al., 2025)
Dialectal Analysis
-
-
-
-
Accuracy • Dialectal Error Rate
BENCH
No
No
2025
Absher (Al-Monef et al., 2025)
Saudi Dialect • Saudi Culture
18k
-
-
18k
Accuracy • F1
MCQ
No
No
Target-Specific Tasks
2024
CamelEval (Qian et al., 2024)
Instruct-following
-
0.8k
0.8k
1.6k
Win-rate, LLM-as-Judge
GEN
No
No
2024
Halwasa (Mubarak et al., 2024)
Hallucination
-
10k
-
10k
Human-as-Judge
GEN
No
No
2024
Henna (Alwajih et al., 2024)
Multimodal
–
1.1k
–
1.1k
LLM-as-Judge
VQA, OCR, GEN
Yes
Yes
2024
CAMEL-Bench (Ghaboura et al., 2024)
Multimodal
29.0k
-
-
29.0k
Accuracy, PATS • LLM-as-Judge
VQA, OCR, RS, GEN
Yes
Yes
2024
AraTrust (Alghamdi et al., 2024)
Safety
0.52k
-
-
0.52k
Accuracy
MCQ
Yes
Yes
2024
Arabic Safeguard Dataset (Ashraf et al., 2025)
Safety
1.0k
-
4.8k
5.8k
LLM-as-Judge
GEN
Yes
Yes
2025
ALRAGE (El Filali et al., 2025)
Context-based (RAG)
-
21.2K
-
21.2K
LLM-as-Judge
GEN
Yes
Yes
2025
AraTable (Alshaikh et al., 2025)
Context-based (Tabular)
-
0.6k
-
0.6k
Accuray • Human-as-Juge
GEN
Yes
Yes
2025
AraHalluEval (Alansari and Luqman, 2025)
Hallucination
0.4k
-
0.8k
1.5k
Human-as-Juge
GEN
Yes
Yes
2025
HalluVerse25 (Abdaljalil et al., 2025)
Hallucination
-
0.8k
-
0.8k
Accuracy
CL
No
No
2025
ARB (Arabic Multimodal Reasoning) (Ghaboura et al., 2025)
Multimodal
1.36k
-
-
1.36k
BLEU • ROUGE • BERTScore • LaBSE • LLM-as-Judge
VQA, RS
Yes
Yes
2025
ASAS (Arab-ic Safety Index) (aiastrolabe, 2025)
Safety
0.8k
-
-
0.8k
LLM-as-Judge
GEN
No
No
Table 2: Summary of Arabic Benchmarks. NAT: # of native samples, TRAN: # of translated samples, SYN: # of synthetic samples, PD: dataset is public, and PR: repo is public.

--- Page 16 ---

2019
2020
2021
2022
2023
2024
2025
Year
ARCD
EXAMS_ar
MMLU_ar
TyDiQA (Ar)
Alghafa
Dolphin
ORCA
AraMed
AraSTEM
AraTrust
ArabLegalEval
Arabic Safeguard Dataset
ArabicMMLU
CAMEL-Bench
CamelEval
GAT
Halwasa
Henna
LAraBench
Qiyas
3LM
AL-QASIDA
ALRAGE
ARB (Arabic Multimodal Reasoning)
ASAS (Arabic Safety Index)
Absher
AraDiCE
AraHalluEval
AraTable
Arabic-GSM8K
BALSAM
Commonsense Arab Culture
Fann or Flop
GATmath, GATLc
HajjFAQ
HalluVerse25
Jawaher
MedArabiQ
MizanQA
PALM
PalmX
Timeline of Arabic Benchmark Releases by Year
Categories
Arabic NLP
Knowledge & STEM
Target-Specific
Culture & Dialects
Figure 3: Timeline of Arabic benchmark releases (2019-2025) showing dramatic acceleration, with 82% of the
benchmarks released in 2024-2025.

```
