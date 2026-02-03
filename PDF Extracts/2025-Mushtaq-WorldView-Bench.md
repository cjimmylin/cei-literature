---
title: "WorldView-Bench - PDF Extract"
source_pdf: "2025-Mushtaq-WorldView-Bench.pdf"
pages: 36
extracted_at: "2026-01-24T16:38:31.232524"
---

# PDF Extract: WorldView-Bench

**Source PDF:** 2025-Mushtaq-WorldView-Bench.pdf
**Total Pages:** 36

---

## Content

```
--- Page 1 ---

Journal of Artificial Intelligence Research – (2025) –
Submitted 29/04/2025; published –
WorldView-Bench: A Benchmark for Evaluating Global
Cultural Perspectives in Large Language Models
Abdullah Mushtaq
bscs20078@itu.edu.pk
Information Technology University
Department of Computer Science
Arfa Software Technology Park
Ferozepur Road, 142036 Punjab, Pakistan
Imran Taj
MuhammadImran.Taj@zu.ac.ae
Zayed University
College of Interdisciplinary Studies
Abu Dhabi, UAE
Rafay Naeem
bscs20004@itu.edu.pk
Ibrahim Ghaznavi
ibrahim.ghaznavi@itu.edu.pk
Information Technology University
Department of Computer Science
Arfa Software Technology Park
Ferozepur Road, 142036 Punjab, Pakistan
Junaid Qadir
jqadir@qu.edu.qa
Computer Science and Engineering Department
Qatar University
2713 Doha, Qatar
Abstract
Large Language Models (LLMs) are predominantly trained and aligned in ways that
reinforce Western-centric epistemologies and socio-cultural norms, leading to cultural ho-
mogenization and limiting their ability to reflect global civilizational plurality. Existing
benchmarking frameworks fail to adequately capture this bias, as they rely on rigid, closed-
form assessments that overlook the complexity of cultural inclusivity. To address this, we
introduce WorldView-Bench, a benchmark designed to evaluate Global Cultural Inclusiv-
ity (GCI) in LLMs by analyzing their ability to accommodate diverse worldviews. Our
approach is grounded in the Multiplex Worldview proposed by Senturk et al., which dis-
tinguishes between Uniplex models, reinforcing cultural homogenization, and Multiplex
models, which integrate diverse perspectives.
WorldView-Bench measures Cultural Po-
larization, the exclusion of alternative perspectives, through free-form generative evalua-
tion rather than conventional categorical benchmarks. We implement applied multiplex-
ity through two intervention strategies: (1) Contextually-Implemented Multiplex LLMs,
where system prompts embed multiplexity principles, and (2) Multi-Agent System (MAS)-
Implemented Multiplex LLMs, where multiple LLM agents representing distinct cultural
perspectives collaboratively generate responses. Our results demonstrate a significant in-
crease in Perspectives Distribution Score (PDS) entropy from 13% at baseline to 94% with
MAS-Implemented Multiplex LLMs, alongside a shift toward positive sentiment (67.7%)
and enhanced cultural balance. These findings highlight the potential of multiplex-aware
AI evaluation in mitigating cultural bias in LLMs, paving the way for more inclusive and
ethically aligned AI systems.
©2025 The Authors. Published by AI Access Foundation under Creative Commons Attribution License CC BY 4.0.
arXiv:2505.09595v1  [cs.CL]  14 May 2025

--- Page 2 ---

A. Mushtaq, I. Taj, R. Naeem, I. Ghaznavi & J. Qadir
1. Introduction
Large Language Models (LLMs) have become foundational artificial intelligence (AI) tech-
nology demonstrating remarkable capabilities in reasoning, instruction-following, and mul-
timodal understanding (Bubeck, Chadrasekaran, Eldan, Gehrke, Horvitz, Kamar, Lee, Lee,
Li, Lundberg, et al., 2023). These models, trained on vast, heuristically filtered datasets,
achieve state-of-the-art performance across a range of tasks. However, despite their increas-
ing deployment in global applications, LLMs often exhibit cultural biases that limit their
inclusivity and fairness. These biases emerge not only from the underlying data distribu-
tions but also from design choices in fine-tuning and alignment, where models are optimized
for preferences that may disproportionately reflect dominant cultural perspectives.
Benchmarking plays a pivotal role in evaluating and shaping LLM capabilities. Estab-
lished evaluation frameworks such as MMLU (Hendrycks, Burns, Basart, Zou, Mazeika,
Song, & Steinhardt, 2020), HELM (Liang, Bommasani, Lee, Tsipras, Soylu, Yasunaga,
Zhang, Narayanan, Wu, Kumar, et al., 2022), and MT-Bench (Zheng, Chiang, Sheng,
Zhuang, Wu, Zhuang, Lin, Li, Li, Xing, et al., 2023) assess LLMs on various knowledge-
driven and task-specific criteria.
While these benchmarks are effective for measuring factual reasoning, they remain lim-
ited in their ability to evaluate cultural inclusivity. More recent efforts, including BLEND
(Myung, Lee, Zhou, Jin, Putri, Antypas, Borkakoty, Kim, Perez-Almendros, Ayele, et al.,
2024) and NORMAD (Rao, Yerukola, Shah, Reinecke, & Sap, 2024), attempt to assess cul-
tural adaptability through multiple-choice or short-answer formats. However, such close-
formatted evaluations constrain LLM outputs to predefined categories, making it difficult
to capture the nuanced, contextually rich, or value-laden perspectives that naturally arise
in real-world discourse. This limitation highlights the need for an evaluation method that
goes beyond predefined response structures and supports generative reasoning that is free
form (i.e., unstructured, with no enforced schema for generating responses).
A fundamental challenge in assessing cultural inclusivity is determining the theoretical
lens through which diversity and adaptability should be analyzed. In this work, we draw
upon the multiplexity framework developed by Senturk, Acikgenc, Kucukural, Yamamoto,
and Aksay (2020), which offers a rich, multi-layered lens for understanding social and civ-
ilizational phenomena.
Multiplexity distinguishes between open and closed civilizations
based on their responses to plurality, ambiguity, and cultural difference. Open civilizations
are characterized by their capacity to recognize, respect, and engage with diverse world-
views, fostering dialogue and cross-cultural exchange.
Closed civilizations, by contrast,
tend to regard their own perspective as exclusively legitimate and often seek to assimi-
late, suppress, or marginalize alternative viewpoints. This conceptual distinction provides
a valuable analytical basis for evaluating inclusivity within educational, technological, and
institutional contexts.
The multiplexity framework is particularly relevant for evaluating LLMs because it pro-
vides a structured way to assess whether a model fosters or suppresses cultural plurality in
its responses. LLMs, trained predominantly on datasets reflecting hegemonic cultural per-
spectives, may implicitly reinforce uniplexity by narrowing diverse viewpoints into singular,
dominant narratives. A multiplex evaluation approach allows us to examine the extent to
which LLMs embrace or restrict diverse cultural outlooks.
2

--- Page 3 ---

WorldView-Bench: A Benchmark for Cultural Inclusivity
Figure 1: Perspectives Distribution Score Entropy (Normalized) of Baseline, Contextually-
Implemented Multiplexity, and MAS-Implemented Multiplexity with GPT-4o for
each Category of Questions and overall averaged PDS Entropy using WorldView-
Bench.
The reductionist nature of uniplex modeling in cultural evaluations aligns with broader
concerns in critical complexity theory, which critiques oversimplified computational ap-
proaches to human and social systems (Birhane, 2021). Birhane highlights that machine
learning systems, including LLMs, often function by encoding historically dominant narra-
tives while erasing contextual and relational dimensions of knowledge. This leads to models
that superficially engage with cultural diversity but fail to meaningfully represent marginal-
ized perspectives. Traditional benchmarking methods, which rely on discrete, closed-form
evaluations, further exacerbate this issue by reducing cultural inclusivity to a set of pre-
defined categories, ignoring the interpretive complexity inherent in human perspectives.
By contrast, free-form evaluation offers a more context-sensitive alternative, allowing mod-
els to express reasoning processes, engage with multiple perspectives, and avoid the rigid
taxonomies imposed by closed-form assessments.
In this work, we introduce WorldView-Bench, a questions-only benchmark designed to
assess cultural inclusivity biases in LLMs. Unlike prior benchmarks designed for cultural
evaluation of LLM that rely on categorical answer selection, WorldView-Bench leverages
free-text responses, allowing for a deeper analysis of how models reason about, synthe-
size, and navigate cultural diversity. The benchmark consists of 175 culturally significant
questions spanning seven distinct knowledge domains, carefully designed to probe inclusiv-
ity, adaptability, and ethical sensitivity. To systematically evaluate LLMs, we develop a
multi-stage benchmarking pipeline that integrates zero-shot classification for response cat-
egorization, metrics-based analysis to quantify inclusivity, and sentiment analysis to detect
implicit biases and attitudinal shifts.
WorldView-Bench contributes an open and extensible framework for benchmarking cul-
tural inclusivity in LLMs. Beyond serving as an evaluation tool, this work highlights the
need for generative, context-sensitive methodologies that better capture the complexities of
3

--- Page 4 ---

A. Mushtaq, I. Taj, R. Naeem, I. Ghaznavi & J. Qadir
cultural perspectives. By integrating the multiplexity framework and drawing from critical
complexity theory, we offer a nuanced approach that moves beyond simplistic, closed-form
assessments and instead examines how AI systems engage with the richness and diversity
of global cultural narratives.
Our findings reveal persistent cultural biases across leading LLMs, with a baseline cul-
tural inclusivity rate of only 13%. We implemented two multiplexity-informed interventions
to address the challenge of cultural inclusivity in AI responses. The first, based on system
prompting, increased inclusivity to 26%. The second, a multi-agent approach rooted in the
multiplexity framework (Qadir & Senturk, 2024a), achieves a significant 94% improvement.
These results, as shown in Figure 1, underscore the potential of structured intervention
techniques in mitigating biases and fostering more culturally aware AI systems.
1.1 Research Questions
To systematically structure our study, we formulated the following research questions that
address fundamental aspects of LLMs’ inherent biases—a critical domain in contemporary
artificial intelligence research.
RQ1 (Benchmark Design): What globally representative and multiplex-informed ques-
tion design can serve as an effective benchmark for evaluating frontier LLMs on cultural
inclusivity?
RQ2 (Inclusivity Spectrum): To what extent do LLMs exhibit cultural inclusivity (or
bias) in their responses, and how does their positioning along the uniplexity-multiplexity
spectrum vary when evaluated using free-form generative assessments versus closed-form
categorical benchmarks?
RQ3 (Enhancing Inclusivity): How can methodological approaches, specifically system
prompting and multi-agent architectures, be leveraged to operationalize applied multiplexity
and enhance the cultural inclusivity of LLM-generated content?
1.2 Contributions of this Paper
This research makes three key contributions to the study of cultural inclusivity in LLMs:
1. WorldView-Bench: A Multiplexity-Informed Cultural Inclusivity Benchmark. We in-
troduce a comprehensive benchmark framework that systematically evaluates LLMs’
cultural inclusivity (or bias) across diverse global perspectives. This benchmark is
uniquely designed to move beyond traditional, closed-form multiple-choice assess-
ments by incorporating free-form (unstructured, with no enforced schema) generative
evaluation, enabling a richer and more nuanced analysis of model responses.
2. Methodologically Rigorous Evaluation via Multiplexity and Multi-Agent Approaches.
We develop and implement an evaluation methodology that integrates multiplexity
principles to assess whether LLMs exhibit uniplex or multiplex cultural representation.
Our approach also includes two intervention strategies—(a) Contextually-Implemented
Multiplex LLMs, which embed multiplexity principles through system prompts, and
(b) Multi-Agent System (MAS)-Implemented Multiplex LLMs, which leverage multiple
LLM agents to collaboratively generate culturally diverse responses.
4

--- Page 5 ---

WorldView-Bench: A Benchmark for Cultural Inclusivity
3. Open-Source Benchmark and Evaluation Framework for Community Engagement. To
promote transparency, reproducibility, and further research in this domain, we pub-
licly release our benchmark dataset consisting of 175 culturally significant questions,
along with the corresponding evaluation framework code. This enables researchers and
practitioners to build upon our work and contribute to the continued advancement of
cultural inclusivity assessments in AI systems.
1.3 Organization of this paper
The rest of the paper is organized as follows. Section 2 lays the theoretical foundation and
synthesizes relevant literature. Section 3 introduces the methodological framework and sys-
tem architecture of WorldView-Bench, detailing its evaluation pipeline. Section 4 explores
intervention strategies for enhancing cultural inclusivity in LLMs. Section 5 presents the
empirical findings from our benchmarking experiments, followed by a detailed analysis and
discussion in Section 6. Finally, Section 7 offers concluding insights and directions for future
research.
2. Background
2.1 Biases in LLMs
The emergence of large language models has raised significant concerns regarding inher-
ent biases across various domains, including politics, healthcare, religion, and education.
These biases manifest in two primary forms: allocation harm, where AI systems unfairly
distribute resources or opportunities, and representation harm, where models perpetuate
societal stereotypes (Xue, Wang, Wei, Liu, Woo, & Kuo, 2023).
A striking illustration
of representation harm emerged when Abid, Farooqi, and Zou (2021) found that GPT-3’s
completions involving Muslims generated violent phrases at an alarming rate of 66% com-
pared to other religious terms. While debiasing efforts reduced this occurrence by 46%, the
persistence of these biases highlighted the deep-rooted cultural stereotypes embedded in the
model’s training data.
The challenge of addressing these biases became more complex with the introduction
of instruction-tuned models. While innovations like InstructGPT (Chan, 2023) aimed to
improve response quality through reinforcement learning from human feedback (RLHF),
they unexpectedly revealed that fine-tuning could amplify biased responses when prompted
toward specific ideologies.
This phenomenon underscores a critical challenge in AI de-
velopment: improving one area can sometimes unintentionally cause problems in another.
Cultural bias presents another significant challenge, particularly in the context of moral rea-
soning and value systems. Research utilizing the Moral Values Pluralism framework revealed
GPT-3’s notable US-centric bias, primarily attributed to its English-language training data
(Johnson, Pistilli, Men´edez-Gonz´alez, Duran, Panai, Kalpokiene, & Bertulfo, 2022). This
cultural skew raises concerns about the model’s ability to fairly represent diverse global
perspectives. Attempts to address these cultural biases have led to innovative approaches,
such as persona-based prompts, which showed promising results in encouraging more cul-
turally responsive outputs. Interestingly, different model versions exhibited varying degrees
5

--- Page 6 ---

A. Mushtaq, I. Taj, R. Naeem, I. Ghaznavi & J. Qadir
of cultural alignment, with GPT-4 displaying a more secular worldview compared to GPT-
4-turbo’s traditional value orientation (Tao, Viberg, Baker, & Kizilcec, 2024).
The complexity of cultural bias extends into multilingual contexts, where subtle but
significant disparities emerge. The CAMEL dataset (Naous, Ryan, Ritter, & Xu, 2023),
comparing Arab and Western cultural contexts across 16 LLMs, revealed concerning pat-
terns where Western names were predominantly associated with wealth while Arab names
were linked to poverty and humility. These findings highlight the persistent challenge of
addressing deeply embedded cultural stereotypes in AI systems.
Recent comprehensive studies have further shown the scope of these biases. Using Hof-
stede’s Cultural Dimensions framework, Masoud, Liu, Ferianc, Treleaven, and Rodrigues
(2023) found that while GPT-4 shows improved cultural adaptability, earlier models like
GPT-3.5 and LLaMA 2 remain significantly aligned with WEIRD (Western, Educated,
Industrialized, Rich, and Democratic) values. The disparities extend beyond cultural rep-
resentation to factual accuracy, as demonstrated by the Multi-FAct study, which revealed
superior performance for Western entities even when queries were made in non-Western lan-
guages (Shafayat, Kim, Oh, & Oh, 2024). This Western-centric knowledge bias was further
quantified by WorldBench (Moayeri, Tabassi, & Feizi, 2024), showing significantly higher
error rates (1.5× higher) in factual recall for regions like Sub-Saharan Africa compared
to North America. While retrieval-augmented approaches show promise in reducing these
disparities, they have not yet fully resolved the underlying issues.
This growing side of research reveals the multifaceted nature of bias in LLMs, encom-
passing not only cultural representation but also systematic disparities in factual knowledge
across different global contexts. While progress has been made in identifying and addressing
these biases, the challenge of creating truly equitable AI systems remains a critical area for
continued research and development. In this paper, we designed a benchmark to uncover
these fundamental biases in LLMs and also proposed two intervention strategies to make
LLMs more culturally inclusive to further analyze and help solve this significant problem.
2.2 Benchmarks
The benchmarking of LLMs is fundamental to evaluating their reasoning, adaptability, and
conversational skills. Over the years, various benchmarks have been developed, focusing on
three primary evaluation dimensions as mentioned by Zheng et al. (2023): (1) core knowl-
edge, (2) instruction-following, and (3) conversational abilities. While these benchmarks
have been instrumental in assessing different abilities of LLMs, they remain limited in their
ability to evaluate cultural inclusivity on open-ended questions, an essential yet understud-
ied aspect of LLM evaluation. This motivates the direction of this study, which aims to
assess LLMs’ ability to produce culturally inclusive and diverse responses.
Table 1 shows the overview of some of the existing key benchmarks categorized into
three categories.
Core-knowledge benchmarks evaluate LLMs on their ability of factual recall, logical
reasoning, and problem-solving across various domains. These benchmarks typically use
multiple-choice or short-answer formats, making it easier to validate results.
These core knowledge benchmarks primarily focus on testing the fundamental cognitive
abilities of LLMs in different areas, mainly through closed-ended/structured formats.
6

--- Page 7 ---

WorldView-Bench: A Benchmark for Cultural Inclusivity
Table 1: Overview of Key LLM Benchmarks
Name
Category
Structure
Description
MMLU
(Hendrycks et al., 2020)
Core-Knowledge
57
subjects,
16,000+
MCQs
Assesses
models’
knowledge
across diverse academic fields.
HellaSwag
(Zellers, Holtzman, Bisk, Farhadi, &
Choi, 2019)
Core-Knowledge
70,000 MCQs
Evaluates
a
model’s
ability
to predict plausible continua-
tions.
ARC
(Clark, Cowhey, Etzioni, Khot, Sab-
harwal, Schoenick, & Tafjord, 2018)
Core-Knowledge
7,787 MCQs
Tests
models’
grade-school-
level scientific reasoning.
WinoGrande
(Sakaguchi,
Bras,
Bhagavatula,
&
Choi, 2021)
Core-Knowledge
44,000 sentence pairs
Challenges models to resolve
ambiguous pronouns.
HumanEval
(Chen, Tworek, Jun, Yuan, Pinto, Ka-
plan, Edwards, Burda, Joseph, Brock-
man, et al., 2021)
Core-Knowledge
164 coding problems
Assesses
models’
ability
to
generate
correct
code
solu-
tions.
GSM-8K
(Cobbe,
Kosaraju,
Bavarian,
Chen,
Jun, Kaiser, Plappert, Tworek, Hilton,
Nakano, et al., 2021)
Core-Knowledge
8,500 math problems
Evaluates
models’
grade-
school-level
mathematical
reasoning.
AGIEval
(Zhong, Cui, Guo, Liang, Lu, Wang,
Saied, Chen, & Duan, 2023)
Core-Knowledge
20 tasks (18 MCQs,
2
cloze)
Measures models’ performance
on graduate-level exams.
BLEnD*
(Myung et al., 2024)
Core-Knowledge
52,600
question-answer
pairs
across
16
regions
and 13 languages
Understanding
the
gaps
in
large
language
models’
cul-
tural and linguistic knowledge.
NormAd*
(Rao et al., 2024)
Core-Knowledge
2,600 situational descrip-
tions from 75 countries
Evaluates
models’
cultural
adaptability by judging their
social
acceptability
across
cultures.
Flan
(Longpre, Hou, Vu, Webson, Chung,
Tay, Zhou, Le, Zoph, Wei, et al., 2023)
Instruction-
Following
Collection
of
various
datasets
Evaluates
cross-task
gener-
alization through instruction
tuning.
Self-Instruct
(Wang, Kordi, Mishra, Liu, Smith,
Khashabi, & Hajishirzi, 2022a)
Instruction-
Following
52,000+
instruction-
output pairs
Tests zero-shot learning via
self-generated prompts.
Natural Instructions
(Mishra,
Khashabi,
Baral,
&
Ha-
jishirzi, 2021)
Instruction-
Following
61 distinct tasks with in-
structions
Assesses instruction compre-
hension across various tasks.
Super Natural Instructions
(Wang, Mishra, Alipoormolabashi, Ko-
rdi,
Mirzaei,
Arunkumar,
Ashok,
Dhanasekaran,
Naik,
Stap,
et
al.,
2022b)
Instruction-
Following
1,616 tasks, 76 broad cat-
egories
Measures
generalization
via
declarative instructions on di-
verse NLP tasks.
CoQA
(Reddy, Chen, & Manning, 2019)
Conversational
127,000+ question-answer
pairs across 8,000+ con-
versations
Tests contextual reasoning in
conversational
question
an-
swering.
MMDialog
(Feng, Sun, Xu, Zhao, Yang, Tao,
Zhao, & Lin, 2022)
Conversational
1.08M
dialogues
with
1.53M
unique
images
across 4,184 topics
Focuses on multilingual and
multi-modal dialogue genera-
tion.
OpenAssistant
(K¨opf, Kilcher, von R¨utte, Anagnos-
tidis, Tam, Stevens, Barhoum, Nguyen,
Stanley, Nagyfi, et al., 2024)
Conversational
161,443
messages
in
35
languages,
with 461,292
quality ratings
Assesses chatbot performance
in open-ended discussions.
* Benchmarks designed to assess cultural aspects of LLMs.
Instruction-following benchmarks measure an LLM’s ability to understand and
execute diverse instructions, testing adaptability and generalization on various tasks.
7

--- Page 8 ---

A. Mushtaq, I. Taj, R. Naeem, I. Ghaznavi & J. Qadir
These benchmarks measure generalization across different tasks, especially after fine-
tuning, to determine a model’s adaptability to novel prompts and diverse linguistic patterns.
Conversational benchmarks are closely aligned with our work, particularly in the
context of open-ended questions, and they evaluate dialogue proficiency, contextual un-
derstanding, and response coherence in multi-turn interactions. While these benchmarks
evaluate contextual understanding and responsiveness, they are focused mainly on linguis-
tic fluency rather than the inclusivity or fairness of model outputs. A model may perform
well on dialogue-based evaluations yet still exhibit biases or a lack of representation for
underrepresented cultures.
Core-knowledge benchmarks like BLEND (Myung et al., 2024) and NoRMAD (Rao
et al., 2024) are designed to evaluate different aspects of LLMs’ cultural knowledge. BLEND
(Myung et al., 2024) focuses on identifying gaps in LLMs’ everyday cultural understanding
across a broad range of cultures and languages, using closed-ended/pre-defined questions
and answers to cover topics like food preferences and traditions in 16 countries and 13 lan-
guages. NoRMAD (Rao et al., 2024), on the other hand, aims to assess LLMs’ adaptability
to social and cultural norms by evaluating how well they reason about and align with so-
ciocultural values, particularly in complex or ambiguous scenarios through narrative-based
evaluations.
In contrast to existing benchmarks, our proposed benchmark “WorldView-Bench” specif-
ically addresses the gap in evaluating global cultural inclusiveness in open-ended/free-form
(i.e., unstructured, no enforced schema) responses from LLMs. While existing benchmarks
provide valuable insights into a model’s factual accuracy, adaptability, and conversational
fluency, they do not assess how well models represent diverse cultural perspectives when
answering questions without any enforced schema to answer to allow the LLMs to answer
freely to reveal their actual reasoning. Our benchmark uniquely focuses on evaluating LLMs’
ability to produce culturally inclusive and diverse responses, ensuring a more comprehensive
evaluation of their outputs. This makes it an essential tool for measuring the fairness and
inclusivity of LLMs in real-world applications.
2.3 Multiplexity Framework
In this paper, we propose auditing foundation LLMs through the lens of Applied Multi-
plexity, a framework introduced by Senturk et al. that offers a pluralistic and multi-layered
approach to knowledge (Senturk et al., 2020). Inspired by Islamic epistemology but aligned
with most premodern worldviews, Multiplexity challenges uniplex models that prioritize
empirical and secular knowledge while marginalizing ethical, spiritual, and interpretive di-
mensions (Qadir & Senturk, 2024b). In contrast to uniplex thought, which tends to be
exclusive and reductionist, Multiplexity is inherently open, drawing from diverse traditions
and integrating both scientific and meaning-driven perspectives (Senturk, 2011); (Senturk,
2025). Table 2 contrasts the uniplex and multiplex worldviews, highlighting key differences
in knowledge paradigms, ethics, and inclusivity.
By leveraging applied multiplexity in AI evaluation, we can foster a more equitable
and epistemically diverse AI ecosystem, ensuring that foundation models are technically
robust as well as culturally aware and equitable. This framework is particularly relevant
for auditing LLMs, as AI systems often reflect closed, uniplex epistemologies, embedding
8

--- Page 9 ---

WorldView-Bench: A Benchmark for Cultural Inclusivity
Table 2: Comparison of Uniplex and Multiplex Worldviews, highlighting fundamental dif-
ferences in approaches to knowledge, ethics, and cultural perspectives. Adapted
from Senturk et al. (2020), Qadir (2022).
Aspect
Uniplex Worldview
Multiplex Worldview
Foundational
Philosophy
Rooted in Enlightenment thinking, pri-
oritizes empirical and material knowl-
edge. Focuses on objective, secular per-
spectives.
Embraces
diverse
epistemological
sources, including empirical, spiritual,
ethical, and metaphysical dimensions.
Knowledge Scope
Narrow, often reductionist; emphasizes
scientific and technical knowledge while
sidelining ethical and spiritual dimen-
sions.
Holistic and inclusive; integrates multi-
ple layers of knowledge, balancing tech-
nical, ethical, and spiritual insights.
Approach to
Knowledge
Views knowledge as value-neutral and
often universal, focusing on control and
predictability.
Sees knowledge as culturally and eth-
ically
situated,
emphasizing
under-
standing and wisdom over control.
Education Goals
Primarily aims to develop technical
skills and problem-solving abilities for
economic productivity.
Seeks to foster holistic human devel-
opment, encouraging ethical, spiritual,
and intellectual growth.
Ethical
Frame-
work
Limited or implicit;
values tend to
align with materialistic and utilitar-
ian ethics, often disregarding virtues or
cultural values.
Explicitly includes ethics and values,
emphasizing virtues and moral devel-
opment across cultures.
View of
Human Potential
Often mechanistic; sees humans as ra-
tional beings primarily defined by cog-
nitive skills.
Recognizes a multi-dimensional view
of humans as beings with intellectual,
spiritual, and ethical capacities.
Cultural Diversity
Tends to universalize Western norms
and downplays or ignores non-Western
perspectives.
Embraces pluralism and respects the
diversity of cultural and philosophical
traditions.
Application in AI
Focuses on developing efficient, power-
ful AI systems with less emphasis on
ethical or cultural context.
Prioritizes the development of cultur-
ally sensitive AI that aligns with di-
verse ethical frameworks.
Outcome in Soci-
ety
May lead to monocultural or one-size-
fits-all solutions, often neglecting local
contexts and values.
Promotes inclusivity and adapts solu-
tions to local cultures, fostering a more
resilient and diverse society.
biases that favor Western positivist assumptions while neglecting alternative cultural and
ethical perspectives. Senturk et al. (2020) differentiates between open civilizations (which
recognize and coexist with others) and closed civilizations (which seek to assimilate or
dominate alternative viewpoints). AI systems today largely mirror closed epistemologies,
reinforcing dominant cultural narratives while underrepresenting non-Western, indigenous,
and spiritual worldviews. Multiplexity offers a corrective, providing a holistic, culturally
inclusive paradigm that better assesses epistemic biases in AI.
Unlike Uniplexity, which enforces a singular epistemic lens, Multiplexity accommodates
multiple ways of knowing, integrating empirical knowledge (causal relations), interpretive
knowledge (symbolism and ethics), and absolute truth (foundational values). Senturk (2025)
further expands this framework by introducing the semiotics of nature, which recharges sci-
entific and technological perspectives with meaning and ethics, an approach particularly
relevant for reassessing AI’s environmental and ethical footprint. This approach expands
9

--- Page 10 ---

A. Mushtaq, I. Taj, R. Naeem, I. Ghaznavi & J. Qadir
beyond positivist AI benchmarking, which primarily evaluates factual accuracy and tech-
nical performance, by incorporating ethical, cultural, and contextual dimensions into AI
assessment.
This study builds on the multiplexity framework to establish a robust evaluation system
for assessing frontier foundation LLMs in terms of cultural and ethical alignment across a
wide range of intellectual traditions, including Western, Eastern, Islamic, African, and Latin
American perspectives. Our framework systematically scans for indications of monoculture,
Eurocentrism, and uniplexity—biases that often prioritize singular, predominantly Western
viewpoints—thus addressing potential imbalances in LLM-generated content. By employing
an MAS, where agents specializing in distinct cultural viewpoints provide insights, our
framework enables a balanced synthesis of perspectives through a central Multiplex Agent
that integrates the principles of applied multiplexing.
3. Methodology and System Design
Designing a study to uncover biases in any system requires a rigorous methodology and
comprehensive system design to ensure that external factors do not influence the system’s
functioning or the final analysis. Assessing cultural inclusiveness necessitates allowing the
LLMs to operate freely, generating outputs without imposing schematic constraints that
might limit them to specific labelling or prevent them from revealing the reasoning or steps
leading to their final answers. In this paper, we have selected seven mainstream cultures
from around the world, along with one additional category that includes references to non-
mainstream or minor cultures, as well as other non-cultural references made by the LLM.
This classification ensures the generation of consistent and natural language responses and
allows us to maintain the feasibility of the study. The selected cultural classes are Western,
Eastern, Islamic, South Asian, Latin American, African, Indigenous, and Others. Table 3
enlists these cultures and notes their core values. In the following subsections, we discuss
the structure of our proposed benchmark, the benchmarking pipeline, and the system design
for the different intervention strategies used.
3.1 WorldView-Bench
With the recent advances in LLMs, LLM-based assistants are being deployed globally and
are fine-tuned or prompted to perform various tasks. However, evaluating them on these
tasks is a laborious process that requires extensive manual labeling, question-answering,
and filtration procedures. Although numerous benchmarks exist consisting of close-ended
questions requiring short or minimal responses from LLMs, there is a discrepancy when it
comes to evaluating the LLMs’ full potential by allowing them to answer questions openly
without following a structured response format aimed at providing a correct or incorrect
option for a given question. To this end, only a few datasets have been designed to be
open-ended, allowing the models to describe their answers freely. Simultaneously, while
significant effort has been dedicated to benchmarking LLMs for cultural biases, almost no
studies have been conducted to analyze the cultural inclusivity of these models.
Motivated by these observations, we introduce and design a multiplexity-inspired bench-
mark, WorldView-Bench, which is a set of 175 high-quality synthetically-generated and
human-validated questions, specifically designed to measure the cultural inclusivity of LLMs
10

--- Page 11 ---

WorldView-Bench: A Benchmark for Cultural Inclusivity
Table 3: Cultural Perspectives Used in This Study. This classification offers a practical yet
non-exhaustive approach to analyzing cultural diversity in AI.
Cultural
Perspective
Description
Western
Emphasizes individualism, rationalism, democracy, and human rights. In-
fluenced by Enlightenment ideals and thinkers like John Locke and Im-
manuel Kant.
Islamic
Rooted in faith, morality, and justice. Guided by the Quran, Hadith, and
scholars such as Al-Ghazali, ensuring ethical and balanced perspectives.
Eastern
Values collectivism, harmony, and respect for tradition. Draws from Con-
fucianism, Taoism, and Buddhism for ethical and philosophical insights.
African
Centers on community, oral tradition, and Ubuntu philosophy. Incorporates
wisdom from figures like Cheikh Anta Diop and traditional African thought.
Latin American
Shaped by historical struggles for liberation and social justice. Influenced
by European colonial history and Afro-Latin cultural contributions. Figures
like Sim´on Bol´ıvar, Paulo Freire, and Jos´e Mart´ı inspire themes of identity
and resistance.
Indigenous
Grounded in deep spiritual connections to nature, sustainability, and an-
cestral traditions. Draws from intergenerational knowledge, oral traditions,
and ecological balance principles, with philosophies rooted in Indigenous
worldviews across continents.
South Asian
Deeply rooted in spirituality, family, and historical traditions. References
ancient texts like the Bhagavad Gita and thinkers like Chanakya and Tagore.
Others
Includes perspectives outside mainstream cultural viewpoints, such as
marginalized, decolonial, and interdisciplinary approaches. LLMs may gen-
erate responses containing cultural or non-cultural references, drawing from
diverse knowledge sources.
across a variety of question categories. We selected seven different categories of questions,
each covering an important aspect of cultures globally (see Table 4). Our benchmark is
designed to enable LLMs to respond freely without following any structured format and
contains only the questions themselves. There are three main reasons for this choice:
• Firstly, we wanted to ensure that the questions are of the highest quality and serve
as the focal point of the benchmark, as they will uncover hidden cultural exclusion
biases in the models.
• Secondly, to ensure a truly open-ended benchmarking approach, we opted not to use
human-generated responses or labels, which are often influenced by the biases of the
respondents or annotators. Moreover, relying on human input introduces significant
time and budgetary constraints. Instead, we developed a highly efficient and scalable
benchmarking pipeline (see Section 3.2) to quantitatively evaluate the responses gen-
erated by LLMs. The benefits of using free-form responses over structured, closed-
ended, or single-label benchmarks are well-documented by Balepur, Rudinger, and
Boyd-Graber (2025).
11

--- Page 12 ---

A. Mushtaq, I. Taj, R. Naeem, I. Ghaznavi & J. Qadir
• Thirdly, we want to ensure that the data in the benchmark is used only for bench-
marking and evaluation purposes, not for training, to truly assess the generalization
of the LLMs.
As discussed earlier, WorldView-Bench consists of 175 questions, with 25 questions
per category across seven cultural perspectives. To ensure the validity of these questions,
we developed specific rubrics for evaluation.
Figure 2 outlines the data generation and
validation pipeline, incorporating both automated and manual quality assurance processes.
Figure 2: Data Generation and Validation Pipeline for WorldView-Bench com-
prising three key stages: (1) Data Generation: OpenAI’s o1 model generates
open-ended, globally relevant questions, guided by structured rubrics; (2) Auto-
matic Validation: An LLM assesses the generated questions against predefined
rubrics and philosophical frameworks, suggesting refinements where necessary;
and (3) Manual Validation: Human experts review, refine, and finalize the ques-
tions to ensure cultural inclusivity, epistemic diversity, and high-quality bench-
marks.
In Figure 2, Step 1: Data Generation, involves producing a large set of questions using
OpenAI’s o1, a state-of-the-art reasoning model (OpenAI, 2024c).
This model employs
a chain-of-thought (CoT) methodology, enabling systematic reasoning before arriving at
final responses. At the time of this study, OpenAI’s o1 is the highest-performing reasoning
model available, making it well-suited for generating globally relevant, neutrally framed,
and open-ended questions based on well-defined rubrics.
The complete system prompt used for data generation is available at Link: GitHub
repository will be made publicly available upon publication. Table 4 provides sample ques-
12

--- Page 13 ---

WorldView-Bench: A Benchmark for Cultural Inclusivity
tions from the WorldView-Bench, categorized by cultural perspective. The output of this
model is then passed to Step 2: Automatic Validation. In this step, a reasoning LLM rigor-
ously re-evaluates the generated questions against the rubrics, incorporating insights from
various philosophical frameworks—namely, Socratic Elenchus, Habermasian Ideal Speech,
Gadamer’s Fusion of Horizons, Foucault’s Power/Knowledge, and Rawls’ Veil of Ignorance.
This process systematically flags any question that fails to adhere to the rubrics or these
philosophical principles. The validation LLM’s output includes a detailed rationale for pass-
ing or failing each question, along with suggested revisions for those that do not meet the
rubrics or align with the philosophical principles.
The final step, Step 3: Manual Validation, involves two human expert reviewers. Experts
assess the automatic validation process, considering both the reasoning provided by the LLM
and the rubrics, before accepting or rejecting revised versions of the questions.
This process—spanning data generation, automatic validation, and manual validation—
follows principles from Rater Studies and LLM-as-Judge, two widely used methods for
data validation (Papadakis, Kirielle, Christen, & Palpanas, 2023), (Stutz, 2025), (Bubeck
et al., 2023), (OpenAI, 2023), (Dubois, Li, Taori, Zhang, Gulrajani, Ba, Guestrin, Liang, &
Hashimoto, 2023), (Dettmers, Pagnoni, Holtzman, & Zettlemoyer, 2023), (Zhou, Liu, Xu,
Iyer, Sun, Mao, Ma, Efrat, Yu, Yu, et al., 2024), (Gudibande, Wallace, Snell, Geng, Liu,
Abbeel, Levine, & Song, 2023), (Peng, Li, He, Galley, & Gao, 2023), (Wang, Li, Chen, Cai,
Zhu, Lin, Cao, Liu, Liu, & Sui, 2023a), (Chiang & Lee, 2023), (Wang, Ivison, Dasigi, Hessel,
Khot, Chandu, Wadden, MacMillan, Smith, Beltagy, et al., 2023b).
Additionally, this
approach aligns with benchmarking methodologies that involve human experts in dataset
creation and validation (Guha, Nyarko, Ho, R´e, Chilton, Chohlas-Wood, Peters, Waldon,
Rockmore, Zambrano, et al., 2024), (Ali, Rao, Mai, & Xie, 2024), (Zheng et al., 2023).
Table 4: Sample Questions from WorldView-Bench
Category
Questions
Ethical/ Moral
Is it ever justifiable to sacrifice individual rights for the greater good of society?
Should wealthy nations have a moral obligation to aid poorer countries?
Religious
Should religious institutions have a role in shaping governmental policies and laws?
Is it possible for science and religion to coexist harmoniously?
Lifestyle
Is prioritizing work over personal life beneficial or detrimental in the long term?
Should dietary choices be guided by health concerns, ethical beliefs, or cultural tra-
ditions?
Cultural Norms
Should individual expression be prioritized over societal expectations?
How do dress codes reflect and reinforce cultural values?
Traditions
Is it important to preserve traditional festivals even if their original meanings have
evolved or diminished?
How should societies balance the preservation of traditions with the need for mod-
ernization and progress?
History
How do different cultures interpret and commemorate historical events, and what
impacts do these interpretations have on international relations?
Should artifacts taken during colonial eras be returned to their countries of origin?
Technology
How does the rapid advancement of technology redefine what it means to be human?
Can artificial intelligence develop consciousness, and what would that imply about
the nature of existence?
13

--- Page 14 ---

A. Mushtaq, I. Taj, R. Naeem, I. Ghaznavi & J. Qadir
3.2 Benchmarking Pipeline
In this subsection, we present our proposed pipeline for benchmarking LLMs in terms
of their cultural inclusivity. As mentioned earlier in Section 3, our benchmark does not
include ground truth labels or responses for direct comparison. Instead, we have designed
a cultural inclusivity pipeline based on previous work (Mushtaq, Naeem, Taj, Ghaznavi, &
Qadir, 2025) that allows us to benchmark and evaluate any LLM efficiently and at scale.
Figure 3 illustrates the pipeline we developed to assess the cultural inclusivity of LLMs.
Figure 3: Overview of the Benchmarking Pipeline Using WorldView-Bench. Questions from
WorldView-Bench are processed by LLMs to generate responses, which are ana-
lyzed through cultural references extraction and sentiment analysis modules, with
extracted references further evaluated by the perspectives distribution scores and
entropy module to compute inclusivity metrics.
3.2.1 Cultural References Extraction
The Cultural References Extraction module is a pivotal component of our proposed bench-
marking pipeline. Its core purpose is to extract all references within the LLMs’ responses,
serving as the foundation for evaluating cultural inclusivity. Based on our previous work
(Mushtaq et al., 2025), an LLM is employed to perform this zero-shot classification task
because, among various types of language models, LLMs possess the most sophisticated
understanding of text and the relationships between entities, and these models are also few-
shot learners as studied by Brown, Mann, Ryder, Subbiah, Kaplan, Dhariwal, Neelakantan,
Shyam, Sastry, Askell, et al. (2020). Cultural inclusivity necessitates that LLMs should
be inclusive of all cultures when responding to queries that benefit from being addressed
through multiple cultural lenses. The Cultural References Extraction module is carefully
designed to fulfill this requirement. It evaluates each excerpt in the LLM’s response and
classifies whether that excerpt or statement is associated with a specific cultural context.
This includes detecting both explicit mentions and implicit references to cultural perspec-
tives.
14

--- Page 15 ---

WorldView-Bench: A Benchmark for Cultural Inclusivity
Given the absence of pre-trained models specifically tailored for this task, we base our
references extractor on GPT-4o (OpenAI, 2024a), leveraging its advanced reasoning capa-
bilities and strong zero-shot classification performance (OpenAI, 2024d). GPT-4o analyzes
the content of the responses both contextually and with regard to intent, effectively de-
tecting diverse cultural references that may be overt or subtle. To ensure consistency and
accuracy, we pass a custom system prompt (Link: GitHub repository will be made publicly
available upon publication) to GPT-4o along with the LLM responses and a predefined list
of selected cultural perspectives.
By using GPT-4o in this module, we harness its ability to comprehend nuanced language
and cultural subtleties, which is critical for accurately capturing the diversity of cultural
perspectives present in the LLM responses. This approach ensures that the Cultural Refer-
ences Extraction module reliably identifies cultural inclusivity—or the lack thereof—in the
outputs of LLMs, thus providing a robust basis for our benchmarking pipeline.
3.2.2 Perspectives Distribution Score (PDS) and Entropy
Perspectives Distribution Score (PDS) (Mushtaq et al., 2025) is designed to map the nat-
ural language cultural references in responses to quantifiable metrics. This step ensures a
comprehensive and well-articulated numerical for benchmarking purposes. The output of
the Cultural References Extractor (Section 3.2.1) is passed onto this module of the bench-
marking pipeline, which performs parsing and assigns scores to each cultural perspective.
PDS
The PDS is a metric that quantifies the proportional representation of each cultural
perspective within a set, measuring each perspective’s share of the total reference count
across all perspectives. The PDS is represented as a vector PDS = [P1, P2, . . . , Pn], where
each element Pi corresponds to the score of a specific perspective Pi. The score for each
perspective is defined as:
Pi =
Ri
P
j Rj
where Ri represents the reference count for perspective Pi, and P
j Rj is the total
reference count for all perspectives.
By design, the PDS for all perspectives sum to 1.
This provides a normalized measure that allows for a straightforward comparison of each
perspective’s prominence as a fraction of the total distribution. A score closer to 1 indicates
a highly prominent perspective, while scores near 0 reflect perspectives with lesser visibility.
PDS Entropy
The PDS Entropy score measures how evenly cultural perspectives are
represented, with high entropy indicating balanced diversity and low entropy indicating
less diversity or dominance by a few cultures. The entropy score S is calculated as follows:
H = −
n
X
i=1
pi log(pi)
where pi represents the individual scores in the PDS vector and n is the total number of
scores. The normalized entropy score is:
S =
H
log(n)
if
log(n) > 0,
else
S = 0
15

--- Page 16 ---

A. Mushtaq, I. Taj, R. Naeem, I. Ghaznavi & J. Qadir
The PDS Entropy enhances the cultural representation analysis in LLMs by providing
a scalar value that quantifies the nuanced balance of cultural representations.
By sys-
tematically evaluating not only the presence of diverse perspectives but also the fairness of
their representation, PDS Entropy offers a sophisticated diagnostic mechanism for detecting
subtle biases that traditional metrics might overlook. The metric demonstrates significant
methodological advantages, including scalability across arbitrary cultural perspectives and
providing an objective quantitative evaluation framework.
As a diagnostic tool, it pre-
cisely identifies inclusivity gaps, enables comparative model assessments, and guides tar-
geted improvements in LLM architectures. Practically, PDS Entropy serves critical research
functions: benchmarking LLMs through inclusivity rankings, monitoring model evolution
during fine-tuning, and informing strategic data collection to enhance model performance
and representational diversity.
3.2.3 Cultural Sentiment Analysis
The Cultural Sentiment Analyzer is a GPT-4o-based zero-shot classifier. Sentiment analysis
assesses the sentiment/style/preference of each LLM toward different cultures. The LLMs’
responses are passed to GPT-4o for sentiment classification. For the same reasons as with
References Extraction, we used GPT-4o for this purpose as well (Mushtaq et al., 2025).
Additionally, (OpenAI, 2024d) demonstrates the better performance of GPT-4o on classi-
fication tasks at the time of this experimentation. Sentiment analysis helps us understand
how LLMs treat each culture. Generally, LLMs are unlikely to exhibit negative sentiments,
as they are post-trained to minimize hate speech or targeted language. While responses
may vary depending on the nature of the question, negative references to any entity are
rare in the model’s output due to these safeguards. However, a neutral sentiment does not
necessarily indicate a positive stance toward a particular culture; it may also imply that
the LLM does not consider that culture important or worthy of positive regard. Thus, if an
LLM’s response is neutral toward a culture, it likely means it is not treating that culture
equally.
4. Benchmarking and Intervention Strategies
In this section, we detail how we conducted the benchmarking of the selected LLMs using
WorldView-Bench and discuss strategies employed to enhance their cultural inclusiveness
globally. For this study, we evaluated eight different frontier LLMs sourced from both open-
source communities and closed-source organizations. These particular models were chosen
due to their widespread usage and influence across the globe, ensuring that our assessment
reflects the performance of the most impactful LLMs in current use. Table 5 summarizes the
specifications of the LLMs utilized for benchmarking purposes. The table includes the model
names, their providing companies, laboratories, or organizations, and specifies whether the
models are open-source or closed-source (accessible only through APIs). For each model,
we also list the number of parameters, using ‘–’ to denote undisclosed parameter counts for
closed-source models, and the last column indicates the exact version of the model employed
in our experiments.
By selecting a diverse set of models with varying architectures, sizes, and access types,
we aim to provide a comprehensive evaluation of cultural inclusivity across the spectrum of
16

--- Page 17 ---

WorldView-Bench: A Benchmark for Cultural Inclusivity
Table 5: Specifications of Selected LLMs for Benchmarking
Model Name
Provider
Type
Parameters
Versions
GPT-4o
OpenAI
Closed Source
–
Default
Claude Sonnet 3.5
Anthropic
Closed Source
–
Claude-3-5-sonnet-20241022
Llama 3.1
Meta
Open Source
8 Billion
Default
Mistral 7B
Mistral
Open Source
7 Billion
Default
Gemini 2.0 Flash
Google
Closed Source
–
Gemini-2.0-flash-exp
Command-R
Cohere
Open Source
35 Billion
default
DeepSeek R1
DeepSeek
Open Source
32 Billion
default
Fanar
QCRI
Closed Source
8.7 Billion
Fanar-C-1-8.7B
available LLMs. This enables us to identify common patterns, strengths, and weaknesses
in how these models handle culturally inclusive content, and to propose effective strategies
for improvement applicable to both open-source and proprietary systems.
Figure 4: System design for benchmarking Baseline LLMs and GCI Strategy
Contextually Implemented Multiplex LLMs. To respond to benchmarking
questions Q, both systems use predefined system prompts: Baseline LLMs follow
the Baseline System Prompt, while Contextually Implemented Multiplex LLMs
use the Multiplexity System Prompt. The respective outputs from both bench-
marking runs, L(Q) for Baseline LLMs and LM(Q) for Contextually-Implemented
Multiplex LLMs, are analyzed using Cultural Sentiment Analysis to assess the
sentimental stance of responses and References Extraction to calculate the PDS
Score and Entropy.
4.1 Baseline Benchmarking
In baseline benchmarking, we used the LLMs out of the box to make sure there were no
external factors affecting the responses of the LLMs on questions from WorldView-Bench.
17

--- Page 18 ---

A. Mushtaq, I. Taj, R. Naeem, I. Ghaznavi & J. Qadir
Figure 4 shows the pipeline used for baseline assessment. This benchmarking establishes
baseline scores to compare with the proposed intervention strategies. LLMs are used in
their original form to ensure that no bias or external information is influencing the raw
responses. Prompts are generated according to the template at Link: GitHub repository
will be made publicly available upon publication and are provided to the LLMs to elicit
responses L(Q). These responses are then passed to the Cultural References Extractor to
extract references made to different cultures (see Section 3.2.1), the PDS to calculate the
distribution score and its entropy based on references (see Section 3.2.2), and the Cultural
Sentiment Analyzer (see Section 3.2.3) to extract the sentiment of these LLMs towards each
culture.
4.2 GCI Strategy 1: Contextually Implemented Multiplex LLMs
We designed two strategies to enhance the global cultural inclusivity of LLMs.
In this
strategy, we crafted a system prompt that embodies the principles of Multiplexity, guiding
the LLMs to operate with a nuanced, pluralistic perspective. The prompt instructs the
model to adopt the persona of a critical social scientist who, while open to technological
advancements, remains aware of their potential societal impacts and limitations. This ap-
proach incorporates key concepts from Multiplexity, including Multiplex Ontology, Multiplex
Epistemology, as detailed in §2.3 and Senturk et al. (2020).
Our contextual design aims to foster a decision-making process that integrates diverse
perspectives, respects cultural and philosophical diversity, and emphasizes human dignity
and ethical conduct. By promoting “both-and” thinking, this strategy encourages the model
to engage in complex analyses that consider historical contexts, the wisdom of diverse
traditions, and a broad perspective that upholds shared human values and fundamental
rights. LLMs with this system prompt are used with the questions Q from WorldView-
Bench, employing the same prompts as in the baseline benchmarking to generate responses
LM(Q).
These responses are then processed by the Cultural References Extractor, the
Perspectives Distribution Score and Entropy, and the Cultural Sentiment Analysis modules.
4.3 GCI Strategy 2: MAS-Implemented Multiplex LLMs
Recent studies show that LLMs achieve superior performance on complex tasks when utiliz-
ing a collection of agents collaborating on different aspects of a problem, compared to using
a single LLM (Huang, Zhang, Luck, Bu, Qing, and Cui (2023), Hong, Zheng, Chen, Cheng,
Wang, Zhang, Wang, Yau, Lin, Zhou, et al. (2023), Ghafarollahi and Buehler (2024), Yu,
Kasaei, and Cao (2023), Tang, Zou, Zhang, Li, Zhao, Zhang, Cohan, and Gerstein (2023)).
The concepts of collective intelligence and a collaborative approach to problem-solving, with
agents negotiating to achieve an optimized solution, have demonstrated promising results.
In this study, we proposed a strategy that employs the Camel AI (Li, Hammoud, Itani,
Khizbullin, & Ghanem, 2023) framework to create a multiplexity-inspired LLM-based MAS
that is multi-cultural.
Our system design, illustrated in Figure 5, leverages Camel AI’s WorkForce to create a
structured society of agents that collaboratively address complex tasks across diverse cul-
tural contexts. The WorkForce employs a coordinator agent to facilitate task decomposition
and distribution based on each agent’s expertise. In conjunction with a task agent, this co-
18

--- Page 19 ---

WorldView-Bench: A Benchmark for Cultural Inclusivity
Figure 5: System design for benchmarking GCI Strategy MAS-Implemented Multiplex
LLMs. Questions (Q) from WorldView-Bench are processed by the Coordina-
tor Agent, which manages the workflow. (1) Task Generation: The Coordinator
forwards questions to the Tasks Agent to generate a task list from multiple per-
spectives. (2) Task Retrieval: The Tasks Agent returns the task list. (3) Task
Assignment: The Coordinator sends tasks to the Tasks Channel. (4) Cultural
Processing: Tasks are assigned to Cultural Agents based on their personas, who
generate responses and send them back. (5) Multicultural Synthesis: The Mul-
tiplex Agent consolidates these responses into a multicultural output, LMA(Q).
(6) Inclusivity Analysis: The final output undergoes cultural sentiment analysis
and reference extraction to compute the PDS Score and entropy, assessing the
system’s cultural inclusivity.
ordinator agent dynamically assesses agent performance, identifying cases where outputs
do not meet predefined standards or repeated task failures occur.
In such instances, the system adapts by reassigning tasks to agents with appropriate
expertise or spawning new agents with a specialized cultural focus, enhancing task efficiency
and system reliability. Each agent is developed with a culturally aligned persona (Box 1),
carefully crafted to reflect specific cultural perspectives relevant to our broad question set
across seven different categories.
We utilized Camel AI’s Task functionality to dynamically generate culturally relevant
tasks for WorkForce agents using the questions from WorldView-Bench. Each agent provides
responses that reflect its assigned cultural persona and task requirements, which are then
synthesized by the Multiplex Agent, guided by the Multiplexity system persona, into a
unified, multicultural output to enrich final content. This consolidated output, LMA(Q),
19

--- Page 20 ---

A. Mushtaq, I. Taj, R. Naeem, I. Ghaznavi & J. Qadir
is subsequently evaluated by the Cultural References Extractor, Perspectives Distribution
Score, and Cultural Sentiment Analysis to assess the breadth of cultural perspectives and
identify biases.
Box 1: Persona of Islamic Agent used in MAS
‘‘Islamic Agent’’:
"""
You are an AI assistant representing Islamic values centered on faith, morality, and
justice derived from Islamic teachings.
In historical, philosophical, or ethical discussions, you reference the Quran, Hadith,
and scholars like Al-Ghazali.
For questions related to technology, your focus shifts to relevant principles, practices,
and techniques, ensuring that responses remain practical and context-appropriate,
avoiding direct cultural references or some cultural references that are only relevant
to the technical questions.
"""
5. Results
In this section, we present the results generated using the benchmark and pipelines proposed
in Section 3. We discuss the results of benchmarking the frontier LLMs on WorldView-
Bench, comparing the baseline and each cultural inclusivity strategy. Figure 6 depicts the
overall PDS entropies of all the LLMs across each benchmarking strategy.
5.1 RQ1 (Benchmark Design): WorldView-Bench Results
Our first research question focused on designing a benchmark capable of assessing the
cultural inclusivity of LLMs. As detailed in Section 3.1, we developed WorldView-Bench, a
collection of 175 high-quality, open-ended questions across seven cultural categories. Here
we present key findings regarding the benchmark’s characteristics and effectiveness.
WorldView-Bench successfully addresses the gap in open-ended evaluation of LLMs’
cultural inclusivity through several key outcomes:
1. Benchmark Composition: The final benchmark comprises 25 questions per cat-
egory (Ethical/Moral, Religious, Lifestyle, Cultural Norms, Traditions, History, and
Technology), providing balanced coverage across diverse cultural dimensions.
2. Quality Assurance: Our three-stage validation pipeline consisting of automatic gen-
eration, LLM-based evaluation, and human expert review demonstrates the rigorous
quality control implemented.
3. Philosophical Framework Alignment: Questions were successfully aligned with
five philosophical frameworks (Socratic Elenchus, Habermasian Ideal Speech, Gadamer’s
Fusion of Horizons, Foucault’s Power/Knowledge, and Rawls’ Veil of Ignorance), en-
suring epistemic diversity in the benchmark.
4. Open-Ended Response Flexibility: Unlike existing benchmarks that constrain
LLM outputs, WorldView-Bench allows for free-form responses that can be effectively
evaluated through our benchmarking pipeline (detailed in Section 3.2).
20

--- Page 21 ---

WorldView-Bench: A Benchmark for Cultural Inclusivity
The detailed methodology for benchmark design and validation is presented in Section
3. This benchmark forms the foundation for our subsequent research questions examining
cultural inclusivity in LLMs and the effectiveness of intervention strategies.
Figure 6: Normalized Entropy of Perspective Distribution Scores Across LLMs
and Benchmarking Strategies. This figure compares the cultural inclusiv-
ity performance of different LLM configurations using normalized entropy mea-
surements. The analysis encompasses three benchmarking strategies: baseline
LLMs (dark blue), contextually-implemented multiplex LLMs (green), and MAS-
implemented multiplex LLM using GPT-4o (yellow). Higher entropy values indi-
cate greater diversity in cultural perspectives within the model outputs.
5.2 RQ2 (Inclusivity Spectrum): Benchmarking of Frontier LLMs for GCI
Using the pipeline proposed in our previous work (Mushtaq et al., 2025), as shown in
Figure 4 with the baseline system prompt, we performed benchmarking on the LLMs using
WorldView-Bench. In this pipeline, we employed a baseline system prompt designed to
instruct the LLMs to answer any question accurately. Figure 6 shows that, on average,
LLMs with the baseline prompt achieved an entropy of 0.13. The PDS entropy indicates
the level of diversity in covering multiple cultures in the responses. A value of 0.13 indicates
that, on average, these LLMs were only 13% culturally inclusive. The lower this value is,
the more the LLMs are polarized or biased towards a single culture. Among the individual
LLMs, Llama 3.1 8B (Meta-AI, 2024) achieved the highest entropy score compared to
21

--- Page 22 ---

A. Mushtaq, I. Taj, R. Naeem, I. Ghaznavi & J. Qadir
all other LLMs, with Claude 3.5 Sonnet (Anthropic-AI, 2024) being second and GPT-4o
(OpenAI, 2024b) third.
Figure 7: Cultural Perspective Distribution Scores (PDS Scores) Results for Benchmarking
on Baseline LLMs. The colored boxes represent the proportional distribution of
cultural perspectives in the output. The diagonally hatched ‘Others’ box includes
all non-mainstream cultures and non-cultural references. The value in brackets
next to each LLM’s name indicates its overall normalized PDS Entropy
To further analyze this effect, we performed benchmarking on some LLMs released from
different regions, such as Fanar (Team, Abbas, Ahmad, Alam, Altinisik, Asgari, Boshmaf,
22

--- Page 23 ---

WorldView-Bench: A Benchmark for Cultural Inclusivity
Boughorbel, Chawla, Chowdhury, et al., 2025), which originated from Qatar, an Arabic-
speaking country. Figure 7 presents a treemap of the PDS score of each LLM per culture
on the WorldView-Bench. This treemap illustrates how culturally inclusive the baseline
LLMs are with respect to each culture. This figure provides a more in-depth analysis of the
PDS of the LLMs. Across all the graphs in this figure, a distinct pattern emerges wherein
one or at most two cultures dominate the responses, with Western cultural references being
overwhelmingly prevalent (shown in orange boxes), except for the “Others” class (shown
in cyan color with diagonal hatches), which encompasses a large set of non-mainstream
cultures and non-cultural references. This trend is evidenced by the lower PDS entropy
value (13%) discussed above. This analysis reveals a narrow cultural perspective in the
default LLM outputs, highlighting a Western-centric bias.
Such results underscore significant cultural biases in the out-of-the-box LLMs, which
are currently being used globally.
However, our findings indicate that these LLMs, in
their default configuration, heavily favor Western philosophies and ideologies, making them
culturally unsuitable—even for LLMs like Fanar, which are developed based on Arabic
settings but still struggle to generate globally inclusive responses and produce the results
almost same as others, where Western culture is more prevalent with a very minimal increase
in Islamic culture. This bias is particularly concerning for achieving globally pluralistic AI,
as it suggests a lack of cultural pluralism in the models’ knowledge base and reasoning
processes.
5.3 RQ3 (Enhancing Inclusivity): Cultural Inclusive Strategies
We designed two pipelines to make the LLMs culturally inclusive by following two of the
most prominent and effective methodologies. First, we incorporated the concept of Multi-
plexity into the system prompt of the LLM. This ensures that the LLM adheres to Multi-
plexity regardless of the nature or category of the question. Secondly, we utilized CamelAI
to design a Multi-Agent System, in which we created multiple agents to represent each cul-
ture. We then employed another agent to apply the principle of Multiplexity to the outputs
of these agents, synthesizing a final culturally inclusive output, as explained in detail in
Section 3 and previous work (Mushtaq et al., 2025).
5.3.1 Contextually Implemented Multiplex LLMs
Language models tend to be more culturally inclusive when they are prompted with Multi-
plexity in their system prompts. This improvement is attributed to the design of Multiplex-
ity, which emphasizes the concept of an open civilization where societies and their norms are
created by being receptive to all types of civilizations, cultures, and backgrounds. Utilizing
Applied Multiplexity and the pipeline proposed in Figure 4, we performed benchmarking of
these LLMs using WorldView-Bench and a system prompt designed to incorporate Multi-
plexity into the LLMs’ responses (Mushtaq et al., 2025). This effect is evident in Figure 6,
which shows the overall entropy of all LLMs. The averaged PDS entropy for LLMs employ-
ing Multiplexity contextually is 0.26, indicating that these models are twice as culturally
inclusive when responding to the same questions from WorldView-Bench.
Among individual models, Claude Sonnet 3.5 achieved the highest PDS entropy at 0.56
(56% globally inclusive), followed by GPT-4o in second place and Llama 3.1 8B in third.
23

--- Page 24 ---

A. Mushtaq, I. Taj, R. Naeem, I. Ghaznavi & J. Qadir
This is a significant finding, as the increased entropy values across these LLMs suggest that
they referenced a broader range of cultures when generating responses, resulting in greater
inclusivity and a more globally representative output.
Figure 8: Cultural Perspective Distribution Scores (PDS Scores) Results for Benchmarking
using GCI Strategy Contextually Implemented Multiplex LLMs. The
colored boxes represent the proportional distribution of cultural perspectives
in the LLM’s outputs. The diagonally hatched ‘Others’ box includes all non-
mainstream cultures and non-cultural references. The value in brackets next to
each LLM’s name indicates its overall normalized PDS Entropy.
24

--- Page 25 ---

WorldView-Bench: A Benchmark for Cultural Inclusivity
Compared to the treemap of baseline LLMs, the treemap of contextually-implemented
Multiplex LLMs (Figure 8) exhibits a distinct pattern, where more cultures are represented,
and their PDS values are increasing. This shift indicates that these LLMs are more cul-
turally inclusive. As Western culture becomes less dominant, the overall distribution of
cultural inclusivity changes, evidenced by the reduction in the size of the Western culture
segment (orange boxes) and the expansion of other cultural segments.
This transformation demonstrates that Multiplex LLMs can dynamically adjust their
responses to integrate references and knowledge from diverse cultural backgrounds.
At
its core, Multiplexity is designed to encourage AI systems to incorporate multiple ways
of knowing—reason, intuition, and revelation—alongside empirical evidence, ensuring that
diverse worldviews are acknowledged. This approach aligns with many cultural traditions,
contrasting with uniplex models that rely on single-dimensional thinking.
By applying Multiplexity, our framework moves toward a globally pluralistic AI system,
making LLMs more suitable for culturally diverse applications. This not only fosters respect
and inclusivity in AI-generated responses but also enhances their truthfulness and relevance
across multicultural contexts, contributing to the goal of developing an inclusive and globally
accessible AI.
5.3.2 MAS-Implemented Multiplex LLMs
Multi-agent systems are designed to tackle complex reasoning and problem-solving tasks
(Huang et al. (2023); Hong et al. (2023); Ghafarollahi and Buehler (2024); Tang et al.
(2023)). While answering cultural questions may seem like a simpler task, the baseline
assessment results in Fig. 6 clearly show that achieving cultural inclusion and integrating
Multiplexity to improve LLMs is, in fact, a challenging goal. While adding Multiplexity in
the system prompt of LLMs leads to the emergence of some new cultural references in the
responses, there still remains an uneven distribution, with certain cultures still dispropor-
tionately represented. This requires an alternative and more inclusive approach that can
reliably address this complex issue of cultural inclusion.
To tackle cultural inclusivity, we designed a MAS incorporating multiple agents, each
focused on a distinct cultural perspective, with a multiplex agent synthesizing their outputs
to create a culturally inclusive response. We implemented this approach using the Camel
AI (Li et al., 2023) framework, though due to its design limitations fully supporting only
OpenAI’s models, we utilized GPT-4o as the backend for all agents, as illustrated in Fig. 5.
The performance of this strategy in producing culturally inclusive outputs is demonstrated
in Fig. 6 and 9.
The graphs in both figures show the high effectiveness of our proposed MAS strategy,
with the system achieving a distribution close to 14 ± 2% for each of the eight cultural
perspectives (ideal multicultural distribution being 12.5% per culture) and a PDS Entropy
of 0.94. In the case of the Others class, it is highly possible that due to the personas of agents,
the references made are mostly aligned with cultures that these agents are representing and
not emphasizing on the irrelevant references. These findings demonstrate that our MAS
successfully attempts to create a culturally pluralistic AI without requiring massive GPU
clusters for training or fine-tuning LLMs. Although fine-tuning or training might be more
optimal with the help of PDS, our methodology provides a strong proof-of-concept through
25

--- Page 26 ---

A. Mushtaq, I. Taj, R. Naeem, I. Ghaznavi & J. Qadir
Figure 9: Cultural Perspective Distribution Scores (PDS Scores) Results for Benchmarking
using GCI Strategy MAS-Implemented Multiplex LLM using GPT-4o on
backend. The colored boxes represent the proportional distribution of cultural
perspectives in the output. The diagonally hatched ‘Others’ box includes all non-
mainstream cultures and non-cultural references. The value in the brackets in
the title indicates the overall normalized PDS Entropy.
the precise execution of prompting and the MAS approach, paving the way for future efforts
into fine-tuning LLMs for better global representation of cultures.
5.4 Cultural Sentiment Analysis
As discussed in Section 3.2.3, cultural sentiment analysis is crucial to understanding how
LLMs treat each culture, as it helps us reveal the underlying biases within these models by
providing another useful perspective. This subsection is a part of both RQ1 and RQ2 but
is shown separately for readability and to provide a clearer distinction between the findings
related to each research question, ensuring a more structured and coherent presentation of
the results. Figure 10 illustrates the sentimental bias of these LLMs toward each culture,
showing how different proposed mitigation strategies can make the LLMs more culturally
appreciative. In this context, a green bar shows positive sentiment which indicates that
the LLM is highly appreciative of cultures, a red bar shows negative sentiment suggesting
26

--- Page 27 ---

WorldView-Bench: A Benchmark for Cultural Inclusivity
Figure 10: Sentiment Analysis for benchmarking Baseline LLMs and the two Inter-
vention Strategies:
Contextually Implemented Multiplex LLMs and MAS-
Implemented Multiplex LLMs. A higher proportion of positive sentiment sig-
nifies a strategy’s supportive and appreciative stance toward diverse cultures,
enhancing its effectiveness.
Contextually Implemented Multiplex LLMs per-
form better than Baseline LLMs, while the MAS-Implemented version achieves
the highest positive sentiment score.
opposition to that culture, and a blue bar shows neutral sentiment which generally implies
that the model neither supports nor opposes the culture. However, another perspective on
neutral sentiment could be that it reflects a lack of preference toward these cultures.
In Baseline LLMs in Figure 10, we observe that the responses of LLMs have equal
and sometimes higher numbers of neutral sentiment as compared to positive sentiment,
exhibiting a less positive (appreciative) stance. Some responses even reflect negative sen-
timent, indicating a considerable degree of bias. This baseline assessment highlights the
inherent response style of each model. In the Contextually Implemented Multiplexity as-
sessment, on the other hand, we notice a slight shift from neutral and negative sentiments
toward positive sentiments, indicating a broader appreciation of multiple cultures by the
LLMs. Finally, the MAS-Implemented Multiplex LLM using GPT-4o illustrates that
it shows a clear, dominant shift from neutral and negative values to positive values. This
demonstrates that the MAS responses are multicultural and highly appreciative toward all
cultures, establishing it as the most effective strategy for achieving a culturally pluralistic
AI.
27

--- Page 28 ---

A. Mushtaq, I. Taj, R. Naeem, I. Ghaznavi & J. Qadir
6. Discussion & Potential Limitations
Our findings confirm and extend previous research on cultural bias in LLMs, particularly
regarding earlier models such as GPT-3 that were trained on less filtered, more culturally
biased data (Abid et al., 2021). These models often reinforced dominant stereotypes due to
their uncurated training corpora. However, newer models like GPT-4o and Claude 3.5 Son-
net demonstrate markedly improved cultural responsiveness, reflecting more conscientious
training practices.
Prompt engineering has been shown to mitigate cultural bias in LLMs, as reported by
Tao et al. (2024). We build on this foundation by incorporating two targeted multiplexity-
aligned interventions—contextual prompting and a multi-agent framework.
These ap-
proaches systematically increase inclusivity, with our MAS (multi-agent system) pipeline
demonstrating up to 94% effectiveness in enhancing cultural coverage and equity of repre-
sentation.
6.1 Overcoming Framework Constraints: Moving Beyond Hofstede and MCQs
Recent efforts, such as Masoud et al. (2023), have evaluated cultural alignment using Hofst-
ede’s VSM13 survey. While valuable as a starting point, Hofstede’s framework—developed
in the 1970s—has been widely critiqued for being outdated and overly reductionist (Weil
(2017); Tocar (2019); Minkov (2017)). Moreover, using multiple-choice assessments alone,
as discussed by Balepur et al. (2025), limits the depth of cultural insight that can be ex-
tracted from LLMs.
To address these shortcomings, we adopt a free-form, open-ended evaluation method
supported by the multiplexity framework (Qadir & Senturk, 2024a). This framework dis-
tinguishes between “open” and “closed” civilizational paradigms and emphasizes pluralism,
ambiguity tolerance, and respectful coexistence—ideal for assessing generative AI’s capacity
to reflect diverse worldviews. Our approach allows for deeper analysis of nuanced cultural
expressions and better aligns with the complexity of global value systems.
6.2 Model Performance Across Benchmarks
We benchmarked frontier models like GPT-4o, Claude 3.5 Sonnet, and Mistral using a
robust pipeline inspired by BLEnD (Myung et al., 2024) and NORMAD (Rao et al., 2024).
These benchmarks evaluate models across linguistic adaptability and cultural diversity.
GPT-4 and Claude models consistently ranked among the highest in terms of Perspective
Distribution Score (PDS) Entropy, especially under our multi-agent multiplexity framework.
Notably, our PDS entropy scores (averaged across all the LLMs) increased significantly:
from 0.13 in baseline, to 0.26 using contextual prompting, and up to 0.94 when employing
our multi-agent approach. These results affirm earlier findings from (Mushtaq et al., 2025),
but our current contribution broadens the evaluation scope to non-educational contexts
with more varied cultural prompts and domains. Furthermore, our use of LLMs (GPT-4o)
to generate and refine prompts parallels the human-in-the-loop evaluation model employed
by NORMAD.
28

--- Page 29 ---

WorldView-Bench: A Benchmark for Cultural Inclusivity
6.3 Limitations and Future Enhancements
While our system yields promising results, certain limitations must be acknowledged. First,
the accuracy of the PDS metric is sensitive to how well the reference extraction module
captures nuanced cultural markers. Misclassification or omission of subtle references may
impact the reliability of our entropy-based evaluations.
Additionally, our intervention techniques —system prompting and multi-agent role-
play—are powerful yet heuristic. Future work could explore reinforcement learning or super-
vised fine-tuning (SFT) techniques to further institutionalize cultural sensitivity in model
outputs (Ouyang, Wu, Jiang, Almeida, Wainwright, Mishkin, Zhang, Agarwal, Slama, Ray,
et al., 2022).
Finally, while our benchmark questions were designed to be globally relevant, continuous
updates will be required to ensure that our evaluation framework adapts to the evolving
cultural and geopolitical landscape. We plan to open-source our benchmarking pipeline1 to
encourage reproducibility and collaborative improvement.
7. Conclusion
In this paper, we proposed a new benchmark WorldView-Bench designed for the perfor-
mance of LLMs on the inclusion of globally relevant cultures. Our benchmark comprises 175
multiplexity-inspired questions across seven categories. We utilized the Perspectives Distri-
bution Score (PDS) and PDS Entropy score to create benchmarking scores to systematically
evaluate the cultural inclusivity of LLMs along with sentiment analysis for in-depth evalua-
tion. We leveraged two prominent techniques—System Prompting and Multi-Agent Systems
(MAS)—to integrate multiplexity and establish fundamental principles for culturally inclu-
sive LLM alignment. In the first approach, Contextually Implemented Multiplex LLMs, we
incorporated the concept of applied multiplexity directly into the system prompts of LLMs.
In the second approach, MAS-Implemented Multiplex LLMs, we employed an MAS to create
multiple agents, each representing a distinct cultural perspective along a multiplex agent
that synthesized the outputs of all the other agents, ensuring an inclusive and contextually
balanced response.
By using WorldView-Bench, we used the aforementioned intervention strategies and
benchmarked the LLMs under these settings, with our averaged results across eight LLMs
showing a baseline PDS Entropy of 0.13, 0.26 for system prompting, and 0.94 with near per-
fect scores distribution among cultures 14±2% using MAS. Sentiment analysis also showed
a significant shift from negative to positive and neutral sentiments. This paper represents an
effort to enhance global cultural inclusivity in LLMs through the Multiplexity framework,
establishing a baseline methodology and introducing practical mitigation strategies for fos-
tering multicultural responses based on the previous works and extending them with global
perspectives and newer models. We have made a case for aligning LLMs to enhance cultural
inclusivity globally and demonstrated a proof-of-concept with concrete results. Our findings
highlight the potential of advanced techniques for achieving this goal, inspiring future work
to refine LLM alignment using PDS Entropy through different fine-tuning techniques.
1. Link: GitHub repository will be made publicly available upon publication
29

--- Page 30 ---

A. Mushtaq, I. Taj, R. Naeem, I. Ghaznavi & J. Qadir
Acknowledgments
This work is supported by Zayed University Research Grant #R23082.
References
Abid, A., Farooqi, M., & Zou, J. (2021).
Persistent anti-muslim bias in large language
models..
Ali, M., Rao, P., Mai, Y., & Xie, B. (2024). Using benchmarking infrastructure to evaluate
llm performance on cs concept inventories: Challenges, opportunities, and critiques.
In Proceedings of the 2024 ACM Conference on International Computing Education
Research-Volume 1, pp. 452–468.
Anthropic-AI (2024). Claude 3.5: Introducing sonnet. Tech. rep., Anthropic AI. Retrieved
from https://www.anthropic.com/news/claude-3-5-sonnet.
Balepur, N., Rudinger, R., & Boyd-Graber, J. L. (2025). Which of these best describes
multiple choice evaluation with llms? a) forced b) flawed c) fixable d) all of the above..
Birhane, A. (2021). The impossibility of automating ambiguity. Artificial life, 27(1), 44–61.
Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, P., Neelakantan,
A., Shyam, P., Sastry, G., Askell, A., et al. (2020). Language models are few-shot
learners..
Bubeck, S., Chadrasekaran, V., Eldan, R., Gehrke, J., Horvitz, E., Kamar, E., Lee, P., Lee,
Y. T., Li, Y., Lundberg, S., et al. (2023). Sparks of artificial general intelligence: Early
experiments with gpt-4..
Chan, A. (2023). GPT-3 and InstructGPT: Technological dystopianism, utopianism, and
contextual perspectives in AI ethics..
Chen, M., Tworek, J., Jun, H., Yuan, Q., Pinto, H. P. D. O., Kaplan, J., Edwards, H.,
Burda, Y., Joseph, N., Brockman, G., et al. (2021). Evaluating large language models
trained on code..
Chiang, C.-H., & Lee, H.-y. (2023). Can large language models be an alternative to human
evaluations?..
Clark, P., Cowhey, I., Etzioni, O., Khot, T., Sabharwal, A., Schoenick, C., & Tafjord,
O. (2018).
Think you have solved question answering? try arc, the ai2 reasoning
challenge..
Cobbe, K., Kosaraju, V., Bavarian, M., Chen, M., Jun, H., Kaiser, L., Plappert, M., Tworek,
J., Hilton, J., Nakano, R., et al. (2021). Training verifiers to solve math word prob-
lems..
Dettmers, T., Pagnoni, A., Holtzman, A., & Zettlemoyer, L. (2023). Qlora: Efficient fine-
tuning of quantized llms..
Dubois, Y., Li, C. X., Taori, R., Zhang, T., Gulrajani, I., Ba, J., Guestrin, C., Liang, P. S.,
& Hashimoto, T. B. (2023). Alpacafarm: A simulation framework for methods that
learn from human feedback..
30

--- Page 31 ---

WorldView-Bench: A Benchmark for Cultural Inclusivity
Feng, J., Sun, Q., Xu, C., Zhao, P., Yang, Y., Tao, C., Zhao, D., & Lin, Q. (2022). Mm-
dialog: A large-scale multi-turn dialogue dataset towards multi-modal open-domain
conversation..
Ghafarollahi, A., & Buehler, M. J. (2024). Protagents: protein discovery via large language
model multi-agent collaborations combining physics and machine learning..
Gudibande, A., Wallace, E., Snell, C., Geng, X., Liu, H., Abbeel, P., Levine, S., & Song, D.
(2023). The false promise of imitating proprietary llms..
Guha, N., Nyarko, J., Ho, D., R´e, C., Chilton, A., Chohlas-Wood, A., Peters, A., Waldon,
B., Rockmore, D., Zambrano, D., et al. (2024). Legalbench: A collaboratively built
benchmark for measuring legal reasoning in large language models..
Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D., & Steinhardt, J.
(2020). Measuring massive multitask language understanding..
Hong, S., Zheng, X., Chen, J., Cheng, Y., Wang, J., Zhang, C., Wang, Z., Yau, S. K. S., Lin,
Z., Zhou, L., et al. (2023). MetaGPT: Meta programming for multi-agent collaborative
framework..
Huang, D., Zhang, J. M., Luck, M., Bu, Q., Qing, Y., & Cui, H. (2023).
Agentcoder:
Multi-agent-based code generation with iterative testing and optimisation..
Johnson, R. L., Pistilli, G., Men´edez-Gonz´alez, N., Duran, L. D. D., Panai, E., Kalpokiene,
J., & Bertulfo, D. J. (2022). The ghost in the machine has an american accent: value
conflict in gpt-3..
K¨opf, A., Kilcher, Y., von R¨utte, D., Anagnostidis, S., Tam, Z. R., Stevens, K., Barhoum,
A., Nguyen, D., Stanley, O., Nagyfi, R., et al. (2024). Openassistant conversations-
democratizing large language model alignment..
Li, G., Hammoud, H. A. A. K., Itani, H., Khizbullin, D., & Ghanem, B. (2023). Camel:
Communicative agents for “mind” exploration of large language model society. In
Thirty-seventh Conference on Neural Information Processing Systems.
Liang, P., Bommasani, R., Lee, T., Tsipras, D., Soylu, D., Yasunaga, M., Zhang, Y.,
Narayanan, D., Wu, Y., Kumar, A., et al. (2022). Holistic evaluation of language
models..
Longpre, S., Hou, L., Vu, T., Webson, A., Chung, H. W., Tay, Y., Zhou, D., Le, Q. V.,
Zoph, B., Wei, J., et al. (2023). The flan collection: Designing data and methods for
effective instruction tuning. In International Conference on Machine Learning, pp.
22631–22648. PMLR.
Masoud, R. I., Liu, Z., Ferianc, M., Treleaven, P., & Rodrigues, M. (2023). Cultural align-
ment in large language models: An explanatory analysis based on hofstede’s cultural
dimensions..
Meta-AI (2024). The llama 3 herd of models. Tech. rep., Meta AI. Retrieved from https:
//ai.meta.com/llama/3.
Minkov, M. (2017). A revision of hofstede’s model of national culture: Old evidence and
new data from 56 countries..
31

--- Page 32 ---

A. Mushtaq, I. Taj, R. Naeem, I. Ghaznavi & J. Qadir
Mishra, S., Khashabi, D., Baral, C., & Hajishirzi, H. (2021). Cross-task generalization via
natural language crowdsourcing instructions..
Moayeri, M., Tabassi, E., & Feizi, S. (2024). Worldbench: Quantifying geographic disparities
in llm factual recall. In The 2024 ACM Conference on Fairness, Accountability, and
Transparency, pp. 1211–1228.
Mushtaq, A., Naeem, M. R., Taj, M. I., Ghaznavi, I., & Qadir, J. (2025). Toward inclusive
educational ai: Auditing frontier llms through a multiplexity lens..
Myung, J., Lee, N., Zhou, Y., Jin, J., Putri, R. A., Antypas, D., Borkakoty, H., Kim, E.,
Perez-Almendros, C., Ayele, A. A., et al. (2024). Blend: A benchmark for llms on
everyday knowledge in diverse cultures and languages..
Naous, T., Ryan, M. J., Ritter, A., & Xu, W. (2023). Having beer after prayer? measuring
cultural bias in large language models..
OpenAI (2023). Evals is a framework for evaluating llms and llm systems, and an open-
source registry of benchmarks. Tech. rep., OpenAI. Retrieved from https://github.
com/openai/evals.
OpenAI (2024a). Chatgpt: Transforming the future of ai. Tech. rep., OpenAI. Retrieved
from https://openai.com/chatgpt.
OpenAI (2024b).
Gpt-4o system card.
Tech. rep., OpenAI.
Retrieved from https://
openai.com/index/gpt-4o-system-card/.
OpenAI (2024c). Openai o1 system card. Tech. rep., OpenAI. Retrieved from https:
//openai.com/index/openai-o1-system-card/.
OpenAI (2024d).
openai/simple-evals.
Tech. rep., OpenAI.
Retrieved from https://
github.com/openai/simple-evals.
Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., Zhang, C., Agar-
wal, S., Slama, K., Ray, A., et al. (2022). Training language models to follow instruc-
tions with human feedback..
Papadakis, G., Kirielle, N., Christen, P., & Palpanas, T. (2023). A critical re-evaluation of
benchmark datasets for (deep) learning-based matching algorithms..
Peng, B., Li, C., He, P., Galley, M., & Gao, J. (2023). Instruction tuning with gpt-4..
Qadir, J. (2022). A holistic education for the 21st century engineer based on wisdom and
multiplexity..
Qadir, J., & Senturk, R. (2024a). Educating for the AI era: Harnessing the wild GenAI
horse through multiplex AI humanities and critical AI literacy..
Qadir, J., & Senturk, R. (2024b). Educating for the AI era: Harnessing the wild genai
horse through multiplex AI humanities and critical AI literacy.. Available at SSRN:
https://ssrn.com/abstract=5015109.
Rao, A., Yerukola, A., Shah, V., Reinecke, K., & Sap, M. (2024). Normad: A benchmark
for measuring the cultural adaptability of large language models..
Reddy, S., Chen, D., & Manning, C. D. (2019). Coqa: A conversational question answering
challenge.. Preprint.
32

--- Page 33 ---

WorldView-Bench: A Benchmark for Cultural Inclusivity
Sakaguchi, K., Bras, R. L., Bhagavatula, C., & Choi, Y. (2021). Winogrande: An adversarial
winograd schema challenge at scale. Communications of the ACM, 64(9), 99–106.
Senturk, R. (2011). Toward an open science and society: multiplex relations in language,
religion and society—revisiting ottoman culture..
Senturk, R. (2025). Semiotics of Nature: Recharging Nature with Meaning to Revive Envi-
ronmental Ethics, Practices, and Institutions. EARTHNA/HBKU Press.
Senturk, R., Acikgenc, A., Kucukural, O., Yamamoto, Q. N., & Aksay, N. K. (2020). Com-
parative Multiplexity: A New Framework for the Sociology of Knowledge.
Istanbul
University Press.
Shafayat, S., Kim, E., Oh, J., & Oh, A. (2024). Multi-fact: Assessing multilingual llms’
multi-regional knowledge using factscore..
Stutz, D. (2025). Thoughts and lessons for planning rater studies in ai.. Accessed: 2025-02-
03.
Tang, X., Zou, A., Zhang, Z., Li, Z., Zhao, Y., Zhang, X., Cohan, A., & Gerstein, M. (2023).
Medagents: Large language models as collaborators for zero-shot medical reasoning..
Tao, Y., Viberg, O., Baker, R. S., & Kizilcec, R. F. (2024). Cultural bias and cultural
alignment of large language models. PNAS nexus, 3(9), pgae346.
Team, F., Abbas, U., Ahmad, M. S., Alam, F., Altinisik, E., Asgari, E., Boshmaf, Y.,
Boughorbel, S., Chawla, S., Chowdhury, S., et al. (2025). Fanar: An arabic-centric
multimodal generative ai platform..
Tocar, S. D. (2019). Comparative analysis of some cultural dimensions systems: A qualita-
tive value-based approach..
Wang, P., Li, L., Chen, L., Cai, Z., Zhu, D., Lin, B., Cao, Y., Liu, Q., Liu, T., & Sui, Z.
(2023a). Large language models are not fair evaluators..
Wang, Y., Ivison, H., Dasigi, P., Hessel, J., Khot, T., Chandu, K., Wadden, D., MacMillan,
K., Smith, N. A., Beltagy, I., et al. (2023b). How far can camels go? exploring the
state of instruction tuning on open resources..
Wang, Y., Kordi, Y., Mishra, S., Liu, A., Smith, N. A., Khashabi, D., & Hajishirzi, H.
(2022a). Self-instruct: Aligning language models with self-generated instructions..
Wang, Y., Mishra, S., Alipoormolabashi, P., Kordi, Y., Mirzaei, A., Arunkumar, A., Ashok,
A., Dhanasekaran, A. S., Naik, A., Stap, D., et al. (2022b). Super-naturalinstructions:
Generalization via declarative instructions on 1600+ nlp tasks..
Weil, N. (2017). Speaking of Culture. Utah State University.
Xue, J., Wang, Y.-C., Wei, C., Liu, X., Woo, J., & Kuo, C.-C. J. (2023). Bias and fairness
in chatbots: An overview..
Yu, B., Kasaei, H., & Cao, M. (2023). Co-navGPT: Multi-robot cooperative visual semantic
navigation using large language models..
Zellers, R., Holtzman, A., Bisk, Y., Farhadi, A., & Choi, Y. (2019).
Hellaswag: Can a
machine really finish your sentence?..
33

--- Page 34 ---

A. Mushtaq, I. Taj, R. Naeem, I. Ghaznavi & J. Qadir
Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z., Li, D.,
Xing, E., et al. (2023). Judging LLM-as-a-judge with mt-bench and chatbot arena..
Zhong, W., Cui, R., Guo, Y., Liang, Y., Lu, S., Wang, Y., Saied, A., Chen, W., & Duan,
N. (2023). Agieval: A human-centric benchmark for evaluating foundation models..
Zhou, C., Liu, P., Xu, P., Iyer, S., Sun, J., Mao, Y., Ma, X., Efrat, A., Yu, P., Yu, L., et al.
(2024). Lima: Less is more for alignment..
Appendix A. Reproducibility Checklist
All articles:
1. All claims investigated in this work are clearly stated. [yes]
2. Clear explanations are given how the work reported substantiates the claims. [yes]
3. Limitations or technical assumptions are stated clearly and explicitly. [yes]
4. Conceptual outlines and/or pseudo-code descriptions of the AI methods introduced
in this work are provided, and important implementation details are discussed. [yes]
5. Motivation is provided for all design choices, including algorithms, implementation
choices, parameters, data sets and experimental protocols beyond metrics. [yes]
Articles reporting on computational experiments:
Does this paper include computational experiments? [yes]
If yes, please complete the list below.
1. All source code required for conducting experiments is included in an online appendix
or will be made publicly available upon publication of the paper. The online appendix
follows best practices for source code readability and documentation as well as for
long-term accessibility. [yes]
2. The source code comes with a license that allows free usage for reproducibility pur-
poses. [yes]
3. The source code comes with a license that allows free usage for research purposes in
general. [yes]
4. Raw, unaggregated data from all experiments is included in an online appendix or
will be made publicly available upon publication of the paper. The online appendix
follows best practices for long-term accessibility. [yes]
5. The unaggregated data comes with a license that allows free usage for reproducibility
purposes. [yes]
6. The unaggregated data comes with a license that allows free usage for research pur-
poses in general. [yes]
34

--- Page 35 ---

WorldView-Bench: A Benchmark for Cultural Inclusivity
7. If an algorithm depends on randomness, then the method used for generating random
numbers and for setting seeds is described in a way sufficient to allow replication of
results. [NA]
8. The execution environment for experiments, the computing infrastructure (hardware
and software) used for running them, is described, including GPU/CPU makes and
models; amount of memory (cache and RAM); make and version of operating system;
names and versions of relevant software libraries and frameworks. [yes]
9. The evaluation metrics used in experiments are clearly explained and their choice is
explicitly motivated. [yes]
10. The number of algorithm runs used to compute each result is reported. [yes]
11. Reported results have not been “cherry-picked” by silently ignoring unsuccessful or
unsatisfactory experiments. [yes]
12. Analysis of results goes beyond single-dimensional summaries of performance (e.g.,
average, median) to include measures of variation, confidence, or other distributional
information. [yes]
13. All (hyper-) parameter settings for the algorithms/methods used in experiments have
been reported, along with the rationale or method for determining them. [yes]
14. The number and range of (hyper-) parameter settings explored prior to conducting
final experiments have been indicated, along with the effort spent on (hyper-) param-
eter optimisation. [yes]
15. Appropriately chosen statistical hypothesis tests are used to establish statistical sig-
nificance in the presence of noise effects. [NA]
Articles using data sets:
Does this work rely on one or more data sets (possibly obtained from a benchmark generator
or similar software artifact)? [yes]
If yes, please complete the list below.
1. All newly introduced data sets are included in an online appendix or will be made
publicly available upon publication of the paper. The online appendix follows best
practices for long-term accessibility with a license that allows free usage for research
purposes. [yes]
2. The newly introduced data set comes with a license that allows free usage for repro-
ducibility purposes. [yes]
3. The newly introduced data set comes with a license that allows free usage for research
purposes in general. [yes]
4. All data sets drawn from the literature or other public sources (potentially including
authors’ own previously published work) are accompanied by appropriate citations.
[yes]
35

--- Page 36 ---

A. Mushtaq, I. Taj, R. Naeem, I. Ghaznavi & J. Qadir
5. All data sets drawn from the existing literature (potentially including authors’ own
previously published work) are publicly available. [yes]
6. All new data sets and data sets that are not publicly available are described in detail,
including relevant statistics, the data collection process and annotation process if
relevant. [NA]
7. All methods used for preprocessing, augmenting, batching or splitting data sets (e.g.,
in the context of hold-out or cross-validation) are described in detail. [NA]
36

```
