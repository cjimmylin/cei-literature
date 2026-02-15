---
title: "2025-Rachamalla-Pragyaan Designing and Curating High-Quality Cultural Post-Training - PDF Extract"
source_pdf: "2025-Rachamalla-Pragyaan Designing and Curating High-Quality Cultural Post-Training.pdf"
pages: 37
extracted_at: "2026-02-15T17:54:28.276357"
---

# PDF Extract: 2025-Rachamalla-Pragyaan Designing and Curating High-Quality Cultural Post-Training

**Source PDF:** 2025-Rachamalla-Pragyaan Designing and Curating High-Quality Cultural Post-Training.pdf
**Total Pages:** 37

---

## Content

```
--- Page 1 ---

Pragyaan: Designing and Curating High-Quality Cultural Post-Training
Datasets for Indian Languages
Neel Prabhanjan Rachamalla, Aravind Konakalla, Gautam Rajeev,
Ashish Kulkarni, Chandra Khatri, and Shubham Agarwal
Krutrim AI, Bangalore, India
Contact: {neel.rachamalla1, ashish.kulkarni, shubham.agarwal1}@olakrutrim.com
Abstract
The effectiveness of Large Language Mod-
els (LLMs) depends heavily on the availabil-
ity of high-quality post-training data, particu-
larly instruction-tuning and preference-based
examples. Existing open-source datasets, how-
ever, often lack multilingual coverage, cul-
tural grounding, and suffer from task diver-
sity gaps that are especially pronounced for
Indian languages. We introduce a human-in-
the-loop pipeline that combines translations
with synthetic expansion to produce reliable
and diverse Indic post-training data. Using this
pipeline, we curate two datasets: Pragyaan-
IT (22.5K) and Pragyaan-Align (100K) across
10 Indian languages covering 13 broad and 56
sub-categories, leveraging 57 diverse datasets.
Our dataset protocol incorporates several often-
overlooked dimensions and emphasize task di-
versity, multi-turn dialogue, instruction fidelity,
safety alignment, and preservation of cultural
nuance, providing a foundation for more inclu-
sive and effective multilingual LLMs.
1
Introduction
Recent developments around Large Language Mod-
els (LLMs) (Touvron et al., 2023; Grattafiori et al.,
2024; Abdin et al., 2025; Guo et al., 2025) have
demonstrated that post-training data, comprising
both instruction-tuning and preference data, plays
a critical role in enhancing model alignment, task
generalization, and usability (Ouyang et al., 2022;
Bai et al., 2022b; Chung et al., 2022). Particularly
in a multilingual and multicultural landscape, like
India, the availability of high-quality, culturally
grounded post-training data is crucial to address
performance gaps in low-resource languages that
often arise from the scarcity of relevant and repre-
sentative training data (Joshi et al., 2020).
While several open-source datasets for post-
training (Longpre et al., 2023; Wang et al., 2022b;
Bercovich et al., 2025a) exist, they are predomi-
nantly English-centric and often suffer from limita-
tions such as inconsistent quality, restricted cover-
age, insufficient task complexity, and limited multi-
lingual coverage. These challenges extend to Indic
post-training data as well, focus of our work.
Direct translations of existing English post-
training datasets are prone to translation biases,
errors (Hartung et al., 2023; Savoldi et al., 2021;
Muennighoff et al., 2022) and loss of cultural
grounding (Wang et al., 2022a; Pudjiati et al.,
2022). For instance, a prompt like “Tell me about
a small herb to plant in backyard" might yield
Western herbs such as thyme or rosemary, whereas
Indian users would expect culturally familiar op-
tions like tulsi (holy basil), pudina (mint), or curry
leaves. Similarly, when asked “What is a good
comfort meal for a rainy day?", English-centric
answers such as tomato soup or grilled cheese over-
look Indian preferences like masala chai with pako-
ras or khichdi with ghee. Even in wellness contexts,
“Recommend a workout routine for beginners" may
default to squats and push-ups, neglecting prac-
tices like Surya Namaskar or yoga exercises. Such
mismatches highlight the need for post-training
data that reflects not just language, but also local
traditions and cultural context.
The recent popularity of LLM-based synthetic
data generation (Wang et al., 2022c) for creating
post-training datasets, while promising, still suffers
in quality due to linguistic inaccuracies, grammati-
cal inconsistencies, and reduced fluency, especially
in multilingual settings, that could degrade the per-
formance of models trained on them. Moreover,
the lack of fine-grained control over output com-
plexity and the potential for hallucination can lead
to the generation of low-quality, unreliable data.
With the aim of addressing these gaps, we
present an approach to curate high-quality post-
training datasets, especially in multilingual settings.
Our curation approach combines the above tech-
niques with post-hoc manual editing, leading to
a scalable human-in-the-loop pipeline, with spe-
arXiv:2510.07000v1  [cs.CL]  8 Oct 2025

--- Page 2 ---

cific focus on several aspects of quality, like task
coverage, multilingual representation, task com-
plexity, culture, multi-turns, reasoning, and others.
We leverage our approach to curate high-quality In-
dic post-training datasets: Pragyaan-IT comprising
22.5K instruction tuning examples and Pragyaan-
Align, a dataset of 100K preference examples in 10
Indian languages covering 56 task categories. Our
contributions could thus be summarized as follows:
• We present a scalable pipeline for curating
high-quality post-training data. Our approach
emphasizes a human-in-the-loop (HITL) that
is more efficient, reliable and ensures higher
quality than direct synthetic generation or
translation of existing English datasets.
• We introduce high-quality, manually cu-
rated, and culturally-inclusive post-training
Pragyaan dataset series, consisting of 1)
22.5K Pragyaan-IT and 2) 100K Pragyaan-
Align, designed for aligning LLMs to the di-
verse Indian cultural context.
• Our dataset includes a broad spectrum of
instruction-following tasks with varying lev-
els of complexity, ensuring the resulting mod-
els can handle a wide range of real-world
scenarios.
We provide a detailed analysis
of the dataset’s characteristics, including its
language distribution and domain representa-
tion, also showcasing its suitability for robust
instruction-following capabilities through a
small-scale pilot experiment.
2
Related Work
Post-training is a key step in aligning large lan-
guage models (LLMs) with human intent, com-
monly achieved through instruction tuning (Wei
et al., 2022a) and preference tuning (Bai et al.,
2022a) datasets, constructed in several ways. Task
template based resources such as Flan 2021 (Wei
et al., 2022a), Flan 2022 (Longpre et al., 2023),
and P3 (Sanh et al., 2022) adapt NLP datasets
into instruction–response format. Human-authored
datasets like Open Assistant (Köpf et al., 2023),
Dolly (Conover et al., 2023), and LIMA (Zhou
et al., 2023) demonstrate the value of curated in-
structions but face scalability challenges. To over-
come this, synthetic generation approaches lever-
age LLMs to expand from small human-annotated
seeds, with efforts such as Self-Instruct (Wang
et al., 2022c), Alpaca (Taori et al., 2023), and
Guanaco (Joseph Cheung, 2023), often distilling
knowledge (Hinton et al., 2015) from stronger
teacher LLM models. Advanced pipelines like
Evol-Instruct (Xu et al., 2023) iteratively increase
instruction complexity, while later works extend
these methods to reasoning and code generation
(Luo et al., 2023; Gunasekar et al., 2023). Com-
plementing these, user-contributed datasets such as
InstructionWild (Ni et al., 2023) and ShareGPT1
provide naturally occurring conversational data,
and Unnatural Instructions (Honovich et al., 2022)
show how seed tasks can be scaled into diverse
synthetic corpora. Subsequent work expanded into
specialized domains, including dialogue systems
(Köpf et al., 2023), structured knowledge ground-
ing (Xie et al., 2022), and chain-of-thought reason-
ing (Wei et al., 2022b; Kim et al., 2023). More
recently, the Magpie dataset (Xu et al., 2024) in-
troduced a fine-grained taxonomy spanning cre-
ative writing, math, role-playing, planning, and
data analysis, emphasizing the importance of broad
coverage in post-training resources. Preference
datasets such as UltraFeedback (Cui et al., 2023)
and Tulu3 (Lambert et al., 2025) comprises human
and synthetic preference pairs for LLM alignment.
Building on these advances, we construct our ap-
proach and dataset tailored to Indian languages and
cultural contexts leveraging manual annotations in
complement with synthetic generation.
While large-scale post-training datasets have be-
come increasingly available, they remain predom-
inantly English-centric, with limited coverage for
other languages. A few exceptions incorporate
some proportions of multilingual data (Köpf et al.,
2023; Longpre et al., 2023; Muennighoff et al.,
2023; Zhuo et al., 2024; Nguyen et al., 2023), but
they remain limited in cultural and linguistic diver-
sity compared to English resources. Prior efforts
to extend post-training resources beyond English
have typically followed three strategies: (1) trans-
lating English datasets into additional languages
(Li et al., 2023a; Khan et al., 2024), (2) gener-
ating template-based datasets (Yu et al., 2023b;
Gupta et al., 2023), and (3) manually curating in-
struction datasets in non-English languages (Li
et al., 2023b; Wang et al., 2022d). Amongst these,
template-based efforts such as xP3 (Muennighoff
et al., 2022) extend the P3 taxonomy with 28 mul-
tilingual datasets. However, xP3 relies on uniform
templates across languages, leading to limited task
diversity and frequent repetition. Translation-based
1https://sharegpt.com/

--- Page 3 ---

Figure 1: Workflow for building Indian language post-training data: English prompts are either translated or
expanded via modified self-instruct pipeline to generate synthetic prompts. In both cases, responses are then
produced with an LLM, translated into one of the 10 Indian languages, and manually refined (Section 3).
approaches face similar limitations, such as Bac-
trian (Li et al., 2023a), which translated Alpaca
(Taori et al., 2023) and Dolly (Conover et al., 2023)
into 52 languages. In contrast, our work intro-
duces human-edited datasets across 10 Indian lan-
guages, addressing issues of redundancy and cul-
tural grounding while providing a more diverse and
representative resource for multilingual alignment.
3
Methodology
We present our multi-stage post-training dataset
creation process that encompasses a variety of task
categories at both broad and fine-grained levels,
critical settings (complexity, interaction depth, con-
straints, safety, indian context, thinking trails) and
leverages human annotators alongside curated data
sources to ensure quality and coverage. While our
approach itself is generic, we discuss how we used
it to create high-quality Indic post-training datasets
that we collectively refer to as Pragyaan-IT and
Pragyaan-Align.
3.1
Data Construction Approaches
We employ two complementary approaches (Fig-
ure 1) that both combine translation and synthetic
generation with post-hoc manual editing to ensure
linguistic accuracy, fluency, and cultural appropri-
ateness in our datasets.
3.1.1
Approach 1: Translation with Human
Refinement
Here, we directly source English prompt-response
pairs from existing English datasets (more details
later in Section 3.5).
Prompts: We begin with English prompts which
are first translated into Indic languages using an
LLM, then refined by human annotators. During
verification, annotators correct linguistic errors,
improve readability, and adapt expressions where
needed to reflect Indian cultural norms. This results
in two categories, i.e. 1) Indic Generic Prompts:
direct translations of the English originals. 2) Indic
Context Prompts: culturally adapted and edited ver-
sions incorporating Indian references and contexts
by human annotators.
Responses: Corresponding English responses
undergo a similar pipeline independently, with
LLM-based translation into Indic languages, fol-
lowed by human editing for grammar, relevance,
length, and cultural appropriateness. Thus, we have
1) Indic Generic Responses: literal translations of
the English outputs. 2) Indic Context Responses:
refined versions adapted to Indian discourse norms.
3.1.2
Approach 2: Synthetic Expansion with
Human Refinement
This approach introduces an additional intermedi-
ate stage of synthetic prompt expansion in English.
Prompts: Starting with a seed set of English
prompts (sourced or created), we use the Self-
Instruct pipeline (Wang et al., 2022b) to iteratively
expand this set into a larger synthetic pool. While
in the original pipeline they generate new prompts
for classification and non-classification types via
different strategies, in our adaptation, we use the
same prompt template for both the cases. The re-
sulting synthetic English prompts are then trans-
lated into Indic languages with LLMs and refined
by human annotators to ensure correctness, clarity,
and cultural grounding. This yields 1) Synthetic
Indic Generic Prompts: literal translations of syn-
thetic English prompts. 2) Synthetic Indic Context
Prompts: culturally enriched translations.
Responses: For each synthetic English prompt,
we generate English responses using an LLM in-
dependently. These are then translated into Indic

--- Page 4 ---

languages and refined through human editing. An-
notators correct factual or linguistic errors, polish
style, and, when appropriate, enrich with cultural
nuances. This process produces 1) Synthetic In-
dic Generic Responses: faithful translations of the
English responses. 2) Synthetic Indic Context Re-
sponses: culturally adapted versions aligned with
the Indian local context.
While our first approach ensures fidelity through
the translation of existing English datasets, it re-
mains constrained in both scope and diversity. The
second approach complements this by introducing
synthetic expansion prior to translation, enabling
broader task coverage, richer cultural representa-
tion, and greater scalability with reduced depen-
dency on large English resources. Together, the
two approaches strike a balance between reliability
and diversity, yielding multilingual datasets that
are both high-quality and contextually rich.
3.2
Task Categories
Building on the design principles of several exist-
ing datasets, we curate a broad set of task categories
that combine core language tasks such as reasoning
(limited to CoT and self-thinking), inference, natu-
ral language understanding (NLU) and generation,
question answering (QA), dialogue and interaction,
information extraction, mathematics, coding, func-
tion calling, and instruction following, while also
extending into culturally grounded domains like
Indian states, religions, geo-political questions, etc.
To promote robustness and responsible deployment,
we additionally include safety and non-compliance,
Indian contentious content, and self-identity tasks.
Collectively, these categories establish a structured
yet comprehensive framework that spans diverse
sub-categories, enabling richer and more inclusive
post-training curation. A detailed breakdown of
sub-categories is provided in Table 1.
3.3
Task Settings
For each task category, we additionally define
several task settings that encourage diversity of
prompt complexity, interaction depth, instruction-
following, safety considerations, cultural ground-
ing, and explicit reasoning trails. We provide sys-
tematic descriptions of these settings next.
3.3.1
Complexity
We categorize tasks by complexity to ensure mod-
els are trained for both simple and challenging sce-
narios, with two primary levels: 1) Easy prompts
are direct and clearly defined, usually requiring
minimal reasoning (e.g.
a single factual or de-
scriptive query). 2) Hard prompts feature greater
structural complexity, often embedding multiple
sub-questions within a single query, requiring nu-
anced reasoning and fine-grained understanding.
Importantly, complexity is defined within each task
category, enabling fair assessment across heteroge-
neous task types (see Figures 6–11 in Appendix).
3.3.2
Multi-Turn Interactions
Multi-turn settings capture tasks where contextual
continuity is critical, such as dialogue, planning,
or role-play. These scenarios require models to
maintain memory of prior turns while generating
coherent and adaptive responses. We consider three
levels of interaction depths: 1) Single-turn (1 turn):
A response to an isolated prompt; 2) Short multi-
turn (3 turns): Three back-and-forth exchanges,
ensuring local continuity; 3) Extended multi-turn (5
turns): Five exchanges, for long-range memory and
coherence in extended conversations (e.g. planning
a festival with evolving constraints).
3.3.3
Instruction Following
We categorize instruction-following into three lev-
els, defined by the number and type of constraints
imposed on the response such as “answer in 100
words”, “respond in json format”, etc. (Figure 12
in Appendix). This ensures coverage of tasks that
range from loosely guided prompts to highly struc-
tured outputs. Different combinations of these con-
straints are applied depending on the nature of the
prompt: 1) Simple instruction following: prompts
include minimal or no explicit constraints on the
format or content of the response; 2) Medium in-
struction following: prompts introduce two to three
explicit constraints, requiring the model to accom-
modate multiple conditions at once; 3) Complex
instruction following: prompts impose several si-
multaneous constraints, demanding precise control
and structured outputs.
3.3.4
Safety
We define safety settings to ensure that models
behave responsibly when faced with sensitive, con-
troversial, or potentially harmful content in a real-
world setting. This dimension helps guide appropri-
ate responses while maintaining ethical standards.
We include 1) Safe: prompts are neutral and non-
controversial, allowing the model to provide direct
answers without ethical or policy concerns; 2) Non-

--- Page 5 ---

Broad Category
Sub Categories
Broad Category
Sub Categories
Reasoning & Inference
Non-Math Reasoning
Math Reasoning
Code Reasoning
Indian Relationships
Inference
Data Analysis
Natural Language Understanding & Genera-
tion
Named Entity Recognition
Text Classification
Grammar Correction
Translation
Creative Writing
Paraphrase Identification
Paraphrase Generation
Text Summarization
Headline Generation
Question Generation
Sentiment Analysis
Question Answering
General Question Answering
Fact Check
Interaction & Dialogue
Multi Turn Conversation
Role Playing
Advice Seeking
Planning
Brainstorming
Information Extraction
Information Seeking
Indian Cultural Context
Comprehension
Sanskrit Cultural & Creative Usage
Sanskrit Festival Greetings
Sanskrit Auspicious Day / Other Occasions
Sanskrit Subhashitas (Quotes)
Sanskrit Captions and Mottos
Sanskrit Person’s Name
Sanskrit Building / Institution / Company Name
Sanskrit Product Name
Mathematics
Math QA
Math Instruction Tuning
Math Proofs
Coding
Code Generation
Code Debugging
Code Editing
Code Explanation
Code Translation
Unit Test Generation
Code Theory
Code Review
Repository level Code Generation
Function Calling
Function Calling
Instruction Following
Instruction Following
Safety & Non-Compliance
Safety & Non-Compliance
Indian Contentious Questions
Indian Geo Political
Indian Politicians
Indian States
Indian Languages
Indian Religions
Self-Identity
Model-name
Person-based
Table 1: Taxonomy of NLP task categories and sub-categories for creating post-training datasets in Section 3.2.
safe: prompts involve sensitive or harmful material,
where the model is expected to either refuse po-
litely (e.g., “Sorry, I cannot assist with that ...”) or
generate a safe response.
3.3.5
Thinking Trails
We define ‘thinking trail’ settings to capture the
role of explicit reasoning in model responses, en-
suring that outputs range from direct answers to
more reflective reasoning styles. 1) Normal: di-
rect response generation without intermediate rea-
soning traces; 2) Chain-of-Thought (CoT): step-
by-step reasoning (Wei et al., 2022b) articulated
explicitly before the final answer; 3) Self-Thinking:
inspired by recent “deep thinking” paradigms (Guo
et al., 2025; Bercovich et al., 2025b; Abdin et al.,
2025), where models produce more elaborate, self-
reflective reasoning trails prior to the final response.
3.3.6
Indian Cultural Context
Given the centrality of Indic languages and cul-
tural alignment in our framework, we explicitly
model contextual grounding through three progres-
sively richer levels. 1) IC-1 represents generic
prompts leading to generic responses, with no ex-
plicit India related anchoring (e.g., Prompt: “Sug-
gest some breakfast items.”, Response: “Pancakes,
cereal, toast, scrambled eggs.”). Such responses
are accurate but remain culturally neutral, with no
particular alignment to cultural settings. 2) IC-2
represents generic prompts that nonetheless yield
Indic-grounded responses. For instance, the same
prompt above, in this setting, would elicit responses
such as “Idli, dosa, paratha, poha”, which are the
most popular breakfast items in India. 3) IC-3 in-
volves prompts that are themselves explicitly Indic,
thereby eliciting fully Indic-based responses. For
example, the prompt itself mentions “Suggest some
Indian breakfast items” with a similar response as
in the IC-2 setting. This setting encourages ground-
ing and diversity of responses with respect to Indian
cultural context that is required for training Indic
focused LLMs.
3.4
Human-In-The-Loop (HITL) Refinement
While synthetic generation and automated trans-
lation provides the backbone of our dataset cre-
ation pipeline, human annotators play an equally
central role in shaping its final form.
Each
prompt–response pair, once generated and as-
signed a configuration of settings (e.g., easy, 1-
Turn, Simple-IF, Safe, IC-3, Normal (No Think-
ing Trails)), enters a stage of manual intervention
where annotators act not merely as reviewers, but
as curators of the data. If a pair does not fully align

--- Page 6 ---

Figure 2: Distribution of Pragyaan-IT (Instruction-Tuning) data across languages (left) and categories (right).
with its designated configuration, annotators may
either (i) adapt the configuration to better reflect
the pair, or (ii) create a new prompt–response pair
that correctly conforms to the specified configura-
tion. This decision balances efficiency with fidelity
to the framework. In cases where manually gener-
ating a new response is especially time-intensive,
the annotators flag the prompt for regeneration and
they undergo another iteration through the pipeline.
Crucially, manual intervention goes beyond me-
chanical verification. Annotators conduct linguis-
tic quality checks ensuring fluency, grammatical
accuracy, syntactic correctness, and appropriate
response length, but are also encouraged to exer-
cise creative judgment. This includes refining awk-
ward phrasings, restructuring unclear outputs, or
enriching responses with culturally relevant details.
Even when a pair formally satisfies all defined con-
straints, annotators may modify it to adjust tone,
improve readability, contextual appropriateness or
pedagogical value as well as elevate the overall
communicative value of the response. These in-
terventions ensure that the dataset is not only con-
sistent with the defined settings, but also meaning-
ful and robust for deployment in real-world post-
training scenarios.
3.5
Dataset Curation
Our curation process draws from a broad pool of
existing resources while systematically adapting
them for Indic languages and tasks. In total, we
considered 57 diverse language datasets, together
with their relevant splits, spanning different cat-
egories and task families. These resources serve
either as direct candidates for translation into Indic
languages or as seed data for synthetic expansion
through a modified Self-Instruct pipeline (Wang
et al., 2022b) described earlier. By combining trans-
lation and generation in a complementary manner,
we ensure that the curated data covers not only core
Natural Language Processing (NLP) tasks but also
culturally grounded and contextually relevant di-
mensions. Table 3 in the Appendix provides an
overview of the corresponding candidate datasets
associated with each task sub-category.
Setting
Configuration
%
Complexity
Easy
62.32
Hard
37.68
Multi Turn
1-Turn
91.66
3-Turn
6.76
5-Turn
1.58
Instruction Following
Simple IF
96.95
Medium IF
2.49
Complex IF
0.56
Safety
Safe
92.51
Non-Safe
7.49
Indian Context
IC-1
32.04
IC-2
10.16
IC-3
57.80
Thinking Trails
Normal
99.98
CoT
0.01
Self Thinking
0.01
Table 2: Distribution of instances in Pragyaan-IT across
different task settings and configurations in Section 3.3.
4
Pragyaan: Indic Post-training Datasets
As part of this work, we construct high-quality
post-training datasets that explicitly target 10 In-
dian languages (Bengali, Gujarati, Hindi, Kannada,
Malayalam, Marathi, Oriya, Punjabi, Tamil, and
Telugu), yielding two complementary resources:
i) Pragyaan-IT (22.5K): an instruction-tuning
dataset designed to enhance a model’s ability to
follow diverse prompts across multiple domains,
ensuring that models can generalize well to every-
day user interactions.
ii) Pragyaan-Align (100K): a preference dataset
curated for Reinforcement Learning (RL)-based

--- Page 7 ---

Figure 3: Average word counts of Pragyaan-Align alignment data across languages (left) and categories (right).
alignment methods, emphasizing preference learn-
ing, safety, and cultural grounding, allowing mod-
els to align more closely with the user intent.
5
Analysis
We begin with an assessment of raw synthetic gen-
erations refined through human annotation, fol-
lowed by a broader dataset-level analysis.
5.1
Human Annotation Refinement
We evaluate the underlying LLM’s performance
for both generation and translation tasks across 5
dimensions, each on a scale of 1-5, for a small sub-
set (see Section A.5 in the Appendix for details
on evaluation). Particularly, for English genera-
tions, grammatical accuracy remains slightly lower
in comprehension (3.20) and creative writing (3.93)
tasks, while receiving high scores for other tasks.
For translation, the model shows the strongest per-
formance for Hindi (Figure 14). Telugu and Gu-
jarati exhibit moderate Lexical Diversity (3.43 and
3.30), while grammatical accuracy remains modest
in Telugu (3.62), Hindi (3.60), and Punjabi (3.55).
Thus, human refinements were critical for convert-
ing raw synthetic output into culturally grounded,
linguistically accurate, and task-aligned data, di-
rectly underpinning the reliability of our data cura-
tion framework.
5.2
Dataset analysis
Figure 2 shows the distribution of Pragyaan-IT
across 10 languages and 15 categories, while Ta-
ble 3 lists the candidate datasets used in its con-
struction. As seen in Figure 2, Indian Cultural Con-
text (26.2%) and Multi-Turn Conversation (23.7%)
dominate, while reasoning and paraphrasing re-
main limited (1–3%), forming targets for future
expansion.
Language coverage is led by Gu-
jarati (17.7%), Kannada (11.4%), Marathi (11.1%),
and Odia (10.8%).
In the current setting (Ta-
ble 2), we have 62.3% ‘Easy’ tasks, single-turn
interactions (91.7%), simple instruction-following
(96.9%), safe content (92.5%) with Indian context
well covered (IC-3: 57.8%). While this analysis
reflects the status of the Pragyaan-IT dataset at the
time of writing, the dataset is under active curation
and will be more comprehensive across task cate-
gories and settings as described in earlier sections.
Word count analysis highlights linguistic and
task-level variation (Figure 4). Gujarati and Odia
are most verbose in both prompts (∼110 words)
and responses (∼320 words), whereas Hindi mostly
remain concise. At the task level, Multi-turn con-
versation, Advice Seeking, and Creative Writing
yield the longest responses (550–620 words). Con-
versely, QA, Indian cultural context, and Compre-
hension tasks are consistently brief. Verbosity thus
correlates with conversational and creative tasks,
while simpler or context-specific settings produce
shorter outputs.
Pragyaan-Align, the preference dataset, has an
equal representation across all languages and 10
categories that helps promote fairness and miti-
gate bias. All instances in Pragyaan-Align follow
a standardized configuration: single-turn interac-
tions with instruction following and safe responses.
Our analysis shows variation in text lengths across
categories and languages. Average word counts
for prompts range from 36–63 words, preferred re-
sponses 137–539, while rejected responses range
from 154–466 words reflecting differences in task
complexity and elaboration. Detailed language-
wise as well as category-wise trends are also pre-
sented in Figure 3.
Overall, our Pragyaan datasets for post-training
provide a broad task and Indian language cover-
age. The various task settings and our curation

--- Page 8 ---

Figure 4: Average word counts of Pragyaan-IT data across languages (left) and categories (right).
Figure 5: Win rates of the Krutrim-2-12B (left) and Llama-3-8B (right) models after DPO, compared against their
respective pre-DPO versions.
process leveraging LLMs along with human-in-the-
loop help ensure high quality. Our future itera-
tions will expand complex reasoning capabilities
and enhance representation for under-covered low-
resource languages.
5.3
Downstream performance
To evaluate the quality of our curated dataset, we
conduct a pilot study with Direct Preference Op-
timization (DPO) (Rafailov et al., 2023) based
alignment on the Pragyaan-Align dataset using
two open-weight models which supports the lan-
guages under consideration: Krutrim-2-12B In-
struct (Kallappa et al., 2025) and Llama-3-8B In-
struct (Grattafiori et al., 2024).
For evaluation, we use the recently released Up-
desh dataset2, which covers similar categories and
languages. We sample around 100 examples from
nine relevant categories, balanced across ten lan-
guages. Responses from the models are scored
against the ground truth on a scale of 1–5 using
an LLM-as-a-judge. We provide more information
about the hyperparameter configuration and other
experimental details in Section A.6 and the corre-
sponding prompts used for evaluation in Section B
of the Appendix.
As shown in Figure 5, Krutrim-2-12B after DPO
either wins or draws in 60.4% of cases, loses in
29.9%, and both pre- and post-DPO responses
2https://huggingface.co/datasets/microsoft/
Updesh_beta
score poorly (<2) in 9.7%. A similar trend holds
for Llama-3-8B (61.1% wins or draws), confirming
the promising potential of our curated dataset for
alignment across different categories and multiple
Indian languages.
6
Conclusion
This work addresses the scarcity of high-quality
post-training data for multilingual LLMs by devel-
oping a human-in-the-loop pipeline to ensure diver-
sity, quality and cultural grounding. Through this
approach, we construct two datasets: Pragyaan-IT
and Pragyaan-Align covering 10 Indian languages
and multiple task categories. The datasets high-
light inclusion of local cultural context, task di-
versity, multi-turn dialogue, and safety alignment,
overcoming the limitations of naive translations
and low-quality synthetic resources. Although de-
signed for Indian languages, the pipeline is read-
ily adaptable to other multilingual contexts. We
present a comprehensive analysis of the dataset’s
characteristics, covering language distribution and
domain coverage, and further demonstrate its effec-
tiveness for alignment through a small-scale pilot
study. Future efforts will expand language cover-
age and further annotation quality refinement. We
aim for this work to support broader efforts in build-
ing culturally inclusive resources that strengthen
LLM applicability in multilingual contexts.

--- Page 9 ---

Limitations
Our dataset is part of an ongoing effort, with
plans to continually expand post-training instances.
While our human-in-the-loop framework mitigates
many issues, challenges such as minor linguistic
inaccuracies, fluency variation across languages,
and potential annotation subjectivity may still per-
sist. Moreover, our research prioritized Indian lan-
guages, and the generalization of findings to other
multilingual settings remain currently unexplored.
Extending the pipeline to new cultural and linguis-
tic contexts will require additional validation. We
view these limitations as avenues for future work
towards broader applicability and refinement of our
proposed framework.
Ethics Statement
This study focuses on curating large-scale post-
training datasets for Indian languages, encom-
passing diverse tasks and cultural contexts. The
pipeline combines synthetic generation with
human-in-the-loop refinement to ensure quality,
safety, and cultural fidelity. We provide proper at-
tribution to all source datasets and tools through ci-
tations. Human involvement was limited to annota-
tion and quality control; no personally identifiable
or sensitive information was collected. We engage
a team of 50 in-house annotators for dataset cre-
ation. All contributors were clearly informed that
their work supports LLM training and were com-
pensated fairly at locally prevailing market rates.
This study did not require formal IRB approval.
Throughout the process, we prioritized preserving
cultural nuances while avoiding harmful, biased, or
unsafe content. The resulting dataset is designed
to advance the development of multilingual and
culturally inclusive LLMs.
Acknowledgements
We thank the leadership at Krutrim for their sup-
port in carrying out this research. We also thank the
Data Annotation Team for their meticulous efforts
especially Sanmathi P N, Dr. Salman Alam, Rup-
katha Mukherjee, Vinod Kumar, Shivaram Prasad
Putta, Divyashree K, Arati V Thakur, Vaibhav
M Sutariya, Mitali Pradhan, Payal Yadav, Sneha
Aniyan, Hemant P Rajopadhye, Joel Johnson and
Srinidhi S. Additionally, we also thank Guduru
Manoj and Souvik Rana for the helpful discussions.
References
Marah Abdin, Sahaj Agarwal, Ahmed Awadallah, Vid-
hisha Balachandran, Harkirat Behl, Lingjiao Chen,
Gustavo de Rosa, Suriya Gunasekar, Mojan Java-
heripi, Neel Joshi, et al. 2025. Phi-4-reasoning tech-
nical report. arXiv preprint arXiv:2504.21318.
Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda
Askell, Anna Chen, Nova DasSarma, Dawn Drain,
Stanislav Fort, Deep Ganguli, Tom Henighan,
Nicholas Joseph, Saurav Kadavath, Jackson Kernion,
Tom Conerly, Sheer El-Showk, Nelson Elhage, Zac
Hatfield-Dodds, Danny Hernandez, Tristan Hume,
Scott Johnston, Shauna Kravec, Liane Lovitt, Neel
Nanda, Catherine Olsson, Dario Amodei, Tom
Brown, Jack Clark, Sam McCandlish, Chris Olah,
Ben Mann, and Jared Kaplan. 2022a. Training a
helpful and harmless assistant with reinforcement
learning from human feedback.
Yuntao Bai,
Saurav Kadavath,
Sandhini Kundu,
Amanda Askell, et al. 2022b.
Constitutional ai:
Harmlessness from ai feedback.
arXiv preprint
arXiv:2212.08073.
Samuel Barham, , Weller, Michelle Yuan, Kenton
Murray, Mahsa Yarmohammadi, Zhengping Jiang,
Siddharth Vashishtha, Alexander Martin, Anqi Liu,
Aaron Steven White, Jordan Boyd-Graber, and Ben-
jamin Van Durme. 2023. Megawika: Millions of
reports and their sources across 50 diverse languages.
Akhiad Bercovich, Itay Levy, Izik Golan, Mohammad
Dabbah, Ran El-Yaniv, Omri Puny, Ido Galil, Zach
Moshe, Tomer Ronen, Najeeb Nabwani, et al. 2025a.
Llama-nemotron: Efficient reasoning models. arXiv
preprint arXiv:2505.00949.
Akhiad Bercovich, Itay Levy, Izik Golan, Mohammad
Dabbah, Ran El-Yaniv, Omri Puny, Ido Galil, Zach
Moshe, Tomer Ronen, Najeeb Nabwani, et al. 2025b.
Llama-nemotron: Efficient reasoning models. arXiv
preprint arXiv:2505.00949.
Ning Bian, Hongyu Lin, Yaojie Lu, Xianpei Han,
Le Sun, and Ben He. 2023. Chatalpaca: A multi-
turn dialogue corpus based on alpaca instructions.
https://github.com/cascip/ChatAlpaca.
Daniel Borkan, Lucas Dixon, Jeffrey Sorensen, Nithum
Thain, and Lucy Vasserman. 2019. Nuanced metrics
for measuring unintended bias with real data for text
classification. In Companion Proceedings of The
2019 World Wide Web Conference.
Hyung Won Chung, Le Hou, Shayne Longpre, Barret
Zoph, et al. 2022. Scaling instruction-finetuned lan-
guage models. arXiv preprint arXiv:2210.11416.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro
Nakano, Christopher Hesse, and John Schulman.
2021. Training verifiers to solve math word prob-
lems. arXiv preprint arXiv:2110.14168.

--- Page 10 ---

Arman Cohan, Franck Dernoncourt, Doo Soon Kim,
Trung Bui, Seokhwan Kim, Walter Chang, and Nazli
Goharian. 2018. A discourse-aware attention model
for abstractive summarization of long documents. In
Proceedings of the 2018 Conference of the North
American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies,
Volume 2 (Short Papers).
Alexis Conneau, Ruty Rinott, Guillaume Lample, Ad-
ina Williams, Samuel R. Bowman, Holger Schwenk,
and Veselin Stoyanov. 2018. Xnli: Evaluating cross-
lingual sentence representations. In Proceedings of
the 2018 Conference on Empirical Methods in Natu-
ral Language Processing. Association for Computa-
tional Linguistics.
Mike Conover, Matt Hayes, Ankit Mathur, Jianwei Xie,
Jun Wan, Sam Shah, Ali Ghodsi, Patrick Wendell,
Matei Zaharia, and Reynold Xin. 2023. Free Dolly:
Introducing the World’s First Truly Open Instruction-
Tuned LLM.
Ganqu Cui, Lifan Yuan, Ning Ding, Guanming Yao,
Bingxiang He, Wei Zhu, Yuan Ni, Guotong Xie,
Ruobing Xie, Yankai Lin, et al. 2023. Ultrafeedback:
Boosting language models with scaled ai feedback.
arXiv preprint arXiv:2310.01377.
Sumanth Doddapaneni, Rahul Aralikatte, Gowtham
Ramesh, Shreya Goyal, Mitesh M. Khapra, Anoop
Kunchukuttan, and Pratyush Kumar. 2023. Towards
leaving no Indic language behind: Building monolin-
gual corpora, benchmark and models for Indic lan-
guages. In Proceedings of the 61st Annual Meeting
of the Association for Computational Linguistics (Vol-
ume 1: Long Papers), pages 12402–12426, Toronto,
Canada. Association for Computational Linguistics.
Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri,
Abhinav Pandey, Abhishek Kadian, Ahmad Al-
Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten,
Alex Vaughan, et al. 2024. The llama 3 herd of mod-
els. arXiv preprint arXiv:2407.21783.
Suriya Gunasekar, Yi Zhang, Jyoti Aneja, Caio
César Teodoro Mendes, Allie Del Giorno, Sivakanth
Gopi, Mojan Javaheripi, Piero Kauffmann, Gustavo
de Rosa, Olli Saarikivi, Adil Salim, Shital Shah,
Harkirat Singh Behl, Xin Wang, Sébastien Bubeck,
Ronen Eldan, Adam Tauman Kalai, Yin Tat Lee, and
Yuanzhi Li. 2023. Textbooks are all you need.
Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song,
Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma,
Peiyi Wang, Xiao Bi, et al. 2025. Deepseek-r1: In-
centivizing reasoning capability in llms via reinforce-
ment learning. arXiv preprint arXiv:2501.12948.
Himanshu Gupta,
Kevin Scaria,
Ujjwala Anan-
theswaran,
Shreyas
Verma,
Mihir
Parmar,
Saurabh Arjun Sawant, Chitta Baral, and Swa-
roop Mishra. 2023. Targen: Targeted data generation
with large language models.
Kai Hartung, Aaricia Herygers, Shubham Kurlekar,
Khabbab Zakaria, Taylan Volkan, Sören Gröttrup,
and Munir Georges. 2023. Measuring sentiment bias
in machine translation.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2020. Measuring massive multitask language under-
standing. arXiv preprint arXiv:2009.03300.
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul
Arora, Steven Basart, Eric Tang, Dawn Song, and
Jacob Steinhardt. 2021. Measuring mathematical
problem solving with the math dataset. NeurIPS.
Geoffrey Hinton, Oriol Vinyals, and Jeff Dean. 2015.
Distilling the knowledge in a neural network. arXiv
preprint arXiv:1503.02531.
Or Honovich, Thomas Scialom, Omer Levy, and Timo
Schick. 2022. Unnatural instructions: Tuning lan-
guage models with (almost) no human labor. arXiv
preprint arXiv:2212.09689.
Joseph Cheung. 2023.
GuanacoDataset (Revision
8cf0d29) .
Mandar Joshi, Eunsol Choi, Daniel S Weld, and Luke
Zettlemoyer. 2017. Triviaqa: A large scale distantly
supervised challenge dataset for reading comprehen-
sion. arXiv preprint arXiv:1705.03551.
Pratik Joshi, Sebastin Santy, Amar Budhiraja, Kalika
Bali, and Monojit Choudhury. 2020. The state and
fate of linguistic diversity and inclusion in the nlp
world. arXiv preprint arXiv:2004.09095.
Aditya Kallappa, Palash Kamble, Abhinav Ravi, Ak-
shat Patidar, Vinayak Dhruv, Deepak Kumar, Raghav
Awasthi, Arveti Manjunath, Shubham Agarwal, Ku-
mar Ashish, Gautam Bhargava, and Chandra Khatri.
2025. Krutrim llm: Multilingual foundational model
for over a billion people.
Mohammed Safi Ur Rahman Khan, Priyam Mehta,
Ananth Sankar, Umashankar Kumaravelan, Sumanth
Doddapaneni, Sparsh Jain, Anoop Kunchukuttan,
Pratyush Kumar, Raj Dabre, Mitesh M Khapra, et al.
2024. Indicllmsuite: A blueprint for creating pre-
training and fine-tuning datasets for indian languages.
arXiv preprint arXiv:2403.06350.
Seungone Kim, Se June Joo, Doyoung Kim, Joel Jang,
Seonghyeon Ye, Jamin Shin, and Minjoon Seo. 2023.
The cot collection: Improving zero-shot and few-shot
learning of language models via chain-of-thought
fine-tuning. arXiv preprint arXiv:2305.14045.
Andreas Köpf, Yannic Kilcher, Dimitri von Rütte,
Sotiris Anagnostidis, Zhi-Rui Tam, Keith Stevens,
Abdullah Barhoum, Nguyen Minh Duc, Oliver Stan-
ley, Richárd Nagyfi, et al. 2023.
Openassistant
conversations–democratizing large language model
alignment. arXiv preprint arXiv:2304.07327.

--- Page 11 ---

Aman Kumar, Himani Shrotriya, Prachi Sahu, Amogh
Mishra, Raj Dabre, Ratish Puduppully, Anoop
Kunchukuttan, Mitesh M. Khapra, and Pratyush Ku-
mar. 2022.
IndicNLG benchmark: Multilingual
datasets for diverse NLG tasks in Indic languages.
In Proceedings of the 2022 Conference on Empiri-
cal Methods in Natural Language Processing, pages
5363–5394, Abu Dhabi, United Arab Emirates. As-
sociation for Computational Linguistics.
Tom Kwiatkowski, Jennimaria Palomaki, Olivia Red-
field, Michael Collins, Ankur Parikh, Chris Alberti,
Danielle Epstein, Illia Polosukhin, Matthew Kelcey,
Jacob Devlin, Kenton Lee Toutanova, Llion Jones,
Ming-Wei Chang, Andrew Dai, Jakob Uszkoreit,
Quoc Le, and Slav Petrov. 2019. Natural questions:
a benchmark for question answering research. TACL.
Nathan Lambert, Jacob Morrison, Valentina Pyatkin,
Shengyi Huang, Hamish Ivison, Faeze Brahman,
Lester James V. Miranda, Alisa Liu, Nouha Dziri,
Shane Lyu, Yuling Gu, Saumya Malik, Victoria
Graf, Jena D. Hwang, Jiangjiang Yang, Ronan Le
Bras, Oyvind Tafjord, Chris Wilhelm, Luca Soldaini,
Noah A. Smith, Yizhong Wang, Pradeep Dasigi, and
Hannaneh Hajishirzi. 2025. Tulu 3: Pushing frontiers
in open language model post-training.
Haonan Li, Fajri Koto, Minghao Wu, Alham Fikri Aji,
and Timothy Baldwin. 2023a. Bactrian-x: A multilin-
gual replicable instruction-following model with low-
rank adaptation. arXiv preprint arXiv:2305.15011.
Lei Li, Yuwei Yin, Shicheng Li, Liang Chen, Peiyi
Wang, Shuhuai Ren, Mukai Li, Yazheng Yang,
Jingjing Xu, Xu Sun, Lingpeng Kong, and Qi Liu.
2023b. M3it: A large-scale dataset towards multi-
modal multilingual instruction tuning.
Yang Liu, Xiaotian Zhang, Haoze Sun, Yuzhen Huang,
Wei Wu, Yiliang Li, Hao Yu, Jun Liu, Yueqi Li,
Zhicheng Guo, Xiaoguang Li, Yongfeng Huang,
Guilin Li, Yujun Zhou, Yufeng Chen, Chenyan Jia,
and Xing-Jian Jiang. 2024. Mmlu-pro: a more ad-
vanced and challenging multi-task evaluation for llms.
arXiv preprint arXiv:2406.01574.
Shayne Longpre, Le Hou, Tu Vu, Albert Webson, et al.
2023. The flan collection: Designing data and meth-
ods for effective instruction tuning. arXiv preprint
arXiv:2301.13688.
Ziyang Luo, Can Xu, Pu Zhao, Qingfeng Sun, Xi-
ubo Geng, Wenxiang Hu, Chongyang Tao, Jing Ma,
Qingwei Lin, and Daxin Jiang. 2023. Wizardcoder:
Empowering code large language models with evol-
instruct.
Arnav Mhaske, Harshit Kedia, Sumanth Doddapaneni,
Mitesh M. Khapra, Pratyush Kumar, Rudra Murthy,
and Anoop Kunchukuttan. 2022. Naamapadam: A
large-scale named entity annotated data for indic lan-
guages.
Todor Mihaylov, Peter Clark, Tushar Khot, and Ashish
Sabharwal. 2018. A new dataset for open book ques-
tion answering. In Proceedings of the 2018 Con-
ference on Empirical Methods in Natural Language
Processing.
Niklas Muennighoff, Qian Liu, Armel Zebaze, Qinkai
Zheng, Binyuan Hui, Terry Yue Zhuo, Swayam
Singh, Xiangru Tang, Leandro von Werra, and
Shayne Longpre. 2023. Octopack: Instruction tun-
ing code large language models.
arXiv preprint
arXiv:2308.07124.
Niklas Muennighoff, Thomas Wang, Lintang Sutawika,
Adam Roberts, Stella Biderman, Teven Le Scao,
M Saiful Bari, Sheng Shen, Zheng-Xin Yong, Hailey
Schoelkopf, et al. 2022. Crosslingual generaliza-
tion through multitask finetuning. arXiv preprint
arXiv:2211.01786.
Niklas Muennighoff, Zitong Yang, Weijia Shi, Xi-
ang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke
Zettlemoyer, Percy Liang, and Emmanuel. 2025. s1:
Simple test-time scaling.
Huu Nguyen, Sameer Suri, Ken Tsui, and Christoph
Schuhmann. 2023.
The open instruction gen-
eralist (oig) dataset.
https://laion.ai/blog/
oig-dataset/.
Jinjie Ni, Fuzhao Xue, Kabir Jain, Mahir Hitesh Shah,
Zangwei Zheng, and Yang You. 2023. Instruction in
the wild: A user-based instruction dataset. https:
//github.com/XueFuzhao/InstructionWild.
NVIDIA. 2025. Llama-nemotron-post-training dataset:
A comprehensive collection of instruction tuning and
alignment data. arXiv preprint arXiv:2505.00949.
Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida,
et al. 2022.
Training language models to follow
instructions with human feedback. arXiv preprint
arXiv:2203.02155.
Guilherme Penedo, Anton Lozhkov, Hynek Kydlíˇcek,
Loubna Ben Allal, Edward Beeching, Agustín Pi-
queres Lajarín, Quentin Gallouédec, Nathan Habib,
Lewis Tunstall, and Leandro von Werra. 2025. Code-
forces cots. https://huggingface.co/datasets/
open-r1/codeforces-cots.
Danti Pudjiati, Ninuk Lustyantie, Ifan Iskandar, and
Tira Nur Fitria. 2022. Post-editing of machine trans-
lation: Creating a better translation of cultural spe-
cific terms. Language Circle: Journal of Language
and Literature, 17(1):61–73.
Ratish
Puduppully,
Himani
Shrotriya,
Anoop
Kunchukuttan,
and Mitesh M. Khapra. 2024.
Mathinstruct:
A high-quality math instruction
dataset.
Rafael Rafailov, Archit Sharma, Eric Mitchell, Christo-
pher D Manning, Stefano Ermon, and Chelsea Finn.
2023. Direct preference optimization: Your language
model is secretly a reward model. Advances in neural
information processing systems, 36:53728–53741.

--- Page 12 ---

Nazneen Rajani, Lewis Tunstall, Edward Beeching,
Nathan Lambert, Alexander M. Rush, and Thomas
Wolf. 2023. No robots. https://huggingface.co/
datasets/HuggingFaceH4/no_robots.
Samyam Rajbhandari, Jeff Rasley, Olatunji Ruwase,
and Yuxiong He. 2020. Zero: Memory optimizations
toward training trillion parameter models. In Pro-
ceedings of the International Conference for High
Performance Computing, Networking, Storage and
Analysis (SC).
Pranav Rajpurkar, Robin Jia, and Percy Liang. 2018.
Know what you don’t know: Unanswerable questions
for squad. arXiv preprint arXiv:1806.03822.
David Rein, Betty Li Hou, Asa Cooper Stickland, Jack-
son Petty, Richard Yuanzhe Pang, Julien Dirani, Ju-
lian Michael, and Samuel R. Bowman. 2024. GPQA:
A graduate-level google-proof q&a benchmark. In
First Conference on Language Modeling.
ServiceNow AI Research. 2024.
R1-distill-sft: A
dataset for instruction tuning with a focus on dis-
tillation from large language models. arXiv preprint
arXiv:2403.06350.
Pritika Rohera, Chaitrali Ginimav, Akanksha Salunke,
Gayatri Sawant, and Raviraj Joshi. 2024. L3cube-
indicquest: A benchmark question answering dataset
for evaluating knowledge of llms in indic context.
arXiv preprint arXiv:2405.18789.
Christian Rothermund, David Vögele, Lucas Roth,
Philipp Schmutz, Tobias Wiegand, and Sebastian
Aschenbrenner. 2025. Finemedlm-o1: Enhancing
medical knowledge reasoning ability of llm from
supervised fine-tuning to test-time training. arXiv
preprint arXiv:2501.09213.
Victor Sanh, Albert Webson, Colin Raffel, Stephen
Bach, Lintang Sutawika, Zaid Alyafeai, Antoine
Chaffin, Arnaud Stiegler, Arun Raja, Manan Dey,
M Saiful Bari, Canwen Xu, Urmish Thakker,
Shanya Sharma Sharma, Eliza Szczechla, Taewoon
Kim, Gunjan Chhablani, Nihal Nayak, Debajyoti
Datta, Jonathan Chang, Mike Tian-Jian Jiang, Han
Wang, Matteo Manica, Sheng Shen, Zheng Xin Yong,
Harshit Pandey, Rachel Bawden, Thomas Wang, Tr-
ishala Neeraj, Jos Rozen, Abheesht Sharma, An-
drea Santilli, Thibault Fevry, Jason Alan Fries, Ryan
Teehan, Teven Le Scao, Stella Biderman, Leo Gao,
Thomas Wolf, and Alexander M Rush. 2022. Multi-
task prompted training enables zero-shot task gener-
alization. In International Conference on Learning
Representations.
Beatrice Savoldi, Marco Gaido, Luisa Bentivogli, Mat-
teo Negri, and Marco Turchi. 2021. Gender bias in
machine translation.
Harman Singh, Nitish Gupta, Shikhar Bharadwaj, Di-
nesh Tewari, and Partha Talukdar. 2024a. Indicgen-
bench: A multilingual benchmark to evaluate genera-
tion capabilities of llms on indic languages.
Shivalika Singh, Freddie Vargus, Daniel Dsouza,
Börje F. Karlsson, Abinaya Mahendiran, Wei-Yin
Ko, Herumb Shandilya, Jay Patel, Deividas Mat-
aciunas, Laura OMahony, Mike Zhang, Ramith
Hettiarachchi, Joseph Wilson, Marina Machado,
Luisa Souza Moura, Dominik Krzemi´nski, Hakimeh
Fadaei, Irem Ergün, Ifeoma Okoh, Aisha Alaagib,
Oshan Mudannayake, Zaid Alyafeai, Vu Minh Chien,
Sebastian Ruder, Surya Guthikonda, Emad A. Al-
ghamdi, Sebastian Gehrmann, Niklas Muennighoff,
Max Bartolo, Julia Kreutzer, Ahmet Üstün, Marzieh
Fadaee, and Sara Hooker. 2024b. Aya dataset: An
open-access collection for multilingual instruction
tuning.
Zafir Stojanovski, Oliver Stanley, Joe Sharratt, Richard
Jones, Abdulhakeem Adefioye, Jean Kaddour, and
Andreas Köpf. 2025. Reasoning gym: Reasoning en-
vironments for reinforcement learning with verifiable
rewards.
Alon Talmor, Jonathan Herzig, Nicholas Lourie, and
Jonathan Berant. 2019. CommonsenseQA: A ques-
tion answering challenge targeting commonsense
knowledge. In Proceedings of the 2019 Conference
of the North American Chapter of the Association
for Computational Linguistics: Human Language
Technologies, Volume 1 (Long and Short Papers).
Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann
Dubois, Xuechen Li, Carlos Guestrin, Percy Liang,
and Tatsunori B Hashimoto. 2023. Stanford alpaca:
An instruction-following llama model.
Shubham Toshniwal, Ivan Moshkov, Sean Narenthi-
ran, Daria Gitman, Fei Jia, and Igor Gitman. 2024.
Openmathinstruct-1: A 1.8 million math instruc-
tion tuning dataset.
arXiv preprint arXiv: Arxiv-
2402.10176.
Foutse Touileb, Xavier Longpre, Adrien L’Heureux,
Tom Houlsby, Duy-Kien Le, Vincent Aribaud, Hugo
Le Scao, Tommaso Pasquini, Marco Miaschi, and
Patrick Muennighoff. 2024.
Magpie: A broad-
coverage, fine-grained multitask instruction dataset.
arXiv preprint arXiv:2403.00010.
Hugo Touvron, Louis Martin, Kevin Stone, Peter Al-
bert, Amjad Almahairi, Yasmine Babaei, Nikolay
Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti
Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton
Ferrer, Moya Chen, Guillem Cucurull, David Esiobu,
Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller,
Cynthia Gao, Vedanuj Goswami, Naman Goyal, An-
thony Hartshorn, Saghar Hosseini, Rui Hou, Hakan
Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa,
Isabel Kloumann, Artem Korenev, Punit Singh Koura,
Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Di-
ana Liskovich, Yinghai Lu, Yuning Mao, Xavier Mar-
tinet, Todor Mihaylov, Pushkar Mishra, Igor Moly-
bog, Yixin Nie, Andrew Poulton, Jeremy Reizen-
stein, Rashi Rungta, Kalyan Saladi, Alan Schelten,
Ruan Silva, Eric Michael Smith, Ranjan Subrama-
nian, Xiaoqing Ellen Tan, Binh Tang, Ross Tay-
lor, Adina Williams, Jian Xiang Kuan, Puxin Xu,

--- Page 13 ---

Zheng Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan,
Melanie Kambadur, Sharan Narang, Aurelien Ro-
driguez, Robert Stojnic, Sergey Edunov, and Thomas
Scialom. 2023. Llama 2: Open foundation and fine-
tuned chat models.
Jun Wang, Benjamin Rubinstein, and Trevor Cohn.
2022a. Measuring and mitigating name biases in
neural machine translation. In ACL.
Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa
Liu, Noah A. Smith, Daniel Khashabi, and Hannaneh
Hajishirzi. 2022b. Self-instruct: Aligning language
model with self generated instructions.
Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Al-
isa Liu, Noah A Smith, Daniel Khashabi, and Han-
naneh Hajishirzi. 2022c. Self-instruct: Aligning lan-
guage model with self generated instructions. ArXiv
preprint, abs/2212.10560.
Yizhong Wang, Yeganeh Li, Niklas Michael, Hila Go-
nen, Jesse He, Yi Zhao, Ziyi Lin, Yejin Shafi, Karan
Singh, Foutse Touileb, and et al. 2022d.
Super-
naturalinstructions: A generalization beyond english
language. arXiv preprint arXiv:2204.05367.
Jason Wei, Maarten Bosma, Vincent Zhao, Kelvin Guu,
Adams Wei Yu, Brian Lester, Nan Du, Andrew M.
Dai, and Quoc V Le. 2022a. Finetuned language
models are zero-shot learners. In International Con-
ference on Learning Representations.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou,
et al. 2022b. Chain-of-thought prompting elicits rea-
soning in large language models. Advances in neural
information processing systems, 35:24824–24837.
Sean Welleck, Ronan Le Bras, Hannaneh Hajishirzi,
and Yejin Choi. 2021. Naturalproofs: Mathematical
theorem proving in natural language. arXiv preprint
arXiv:2104.01112.
Tianbao Xie, Chen Henry Wu, Peng Shi, Ruiqi Zhong,
Torsten Scholak, Michihiro Yasunaga, Chien-Sheng
Wu, Ming Zhong, Pengcheng Yin, Sida I Wang,
et al. 2022. Unifiedskg: Unifying and multi-tasking
structured knowledge grounding with text-to-text lan-
guage models. arXiv preprint arXiv:2201.05966.
Can Xu, Qingfeng Sun, Kai Zheng, Xiubo Geng,
Pu Zhao, Jiazhan Feng, Chongyang Tao, and Daxin
Jiang. 2023. Wizardlm: Empowering large language
models to follow complex instructions.
Zhangchen Xu, Fengqing Jiang, Luyao Niu, Yun-
tian Deng, Radha Poovendran, Yejin Choi, and
Bill Yuchen Lin. 2024. Magpie: Alignment data
synthesis from scratch by prompting aligned llms
with nothing.
Zhangchen Xu, Yang Liu, Yueqin Yin, Mingyuan Zhou,
and Radha Poovendran. 2025. KodCode: A diverse,
challenging, and verifiable synthetic dataset for cod-
ing. In Findings of the Association for Computa-
tional Linguistics: ACL 2025, pages 6980–7008.
Yi Yang, Wen-tau Yih, and Christopher Meek. 2015.
Wikiqa: A challenge dataset for open-domain ques-
tion answering. In Proceedings of the 2015 Con-
ference on Empirical Methods in Natural Language
Processing.
Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio,
William Cohen, Ruslan Salakhutdinov, and Christo-
pher D. Manning. 2018. HotpotQA: A dataset for
diverse, explainable multi-hop question answering.
In Proceedings of the 2018 Conference on Empiri-
cal Methods in Natural Language Processing, pages
2369–2380, Brussels, Belgium. Association for Com-
putational Linguistics.
Yixin Ye, Zhen Huang, Yang Xiao, Ethan Chern, Shijie
Xia, and Pengfei Liu. 2025. Limo: Less is more for
reasoning.
Xiang Yu, Haidong Liu, Ning Yang, Qiaoli Wang,
Jianye Wang, Jia Li, Li Zhang, and Jian Zhang. 2023a.
Metamath: Bootstrap your own mathematical reason-
ing dataset. arXiv preprint arXiv:2309.12284.
Yue Yu, Yuchen Zhuang, Jieyu Zhang, Yu Meng,
Alexander Ratner, Ranjay Krishna, Jiaming Shen,
and Chao Zhang. 2023b. Large language model as
attributed training data generator: A tale of diversity
and bias.
Tianyu Zhang, Yang Liu, Yuxuan Xu, Yujia Wang,
Haoyu Chen, Hongwei Li, Chen Li, Jiawei Xie, and
Chen Zhang. 2024. Open-thoughts: A large-scale
dataset for learning and evaluating llm thinking pro-
cesses. arXiv preprint arXiv:2406.04178.
Chunting Zhou, Pengfei Liu, Puxin Xu, Srini Iyer, Jiao
Sun, Yuning Mao, Xuezhe Ma, Avia Efrat, Ping Yu,
Lili Yu, et al. 2023. Lima: Less is more for alignment.
arXiv preprint arXiv:2305.11206.
Terry Yue Zhuo, Armel Zebaze, Nitchakarn Suppat-
tarachai, Leandro von Werra, Harm de Vries, Qian
Liu, and Niklas Muennighoff. 2024.
Astraios:
Parameter-efficient instruction tuning code large lan-
guage models. arXiv preprint arXiv:2401.00788.
A
Appendix
A.1
Dataset Curation
For each sub-category, we curated multiple pub-
licly available candidate datasets and evaluated
their applicability to our data collection objectives,
assessing how they align with the chosen curation
approaches. Table 3 summarizes representative
categories along with corresponding datasets incor-
porated into our pipeline. It is worth noting that
data collection for certain sub-categories remains
an ongoing effort.
A.2
Data Construction Approaches
We further provide more details about the prompt
and responses for both the approaches in Table 4.

--- Page 14 ---

Sub Category
Candidate Datasets
Sub Category
Candidate Datasets
Non-Math Reasoning
MMLU (Hendrycks et al., 2020)
MMLU-Pro (Liu et al., 2024)
GPQA (Rein et al., 2024)
medical-o1-reasoning-SFT (Rothermund et al., 2025)
OpenThoughts (Zhang et al., 2024)
Sentiment Analysis
IndicSentiment (Doddapaneni et al., 2023)
pietrolesci/imdb
Math Reasoning
OpenThoughts (Zhang et al., 2024)
Llama-Nemotron-Posttraining-Dataset (NVIDIA, 2025)
ServiceNow-AI/R1-Distil-SFT (Research, 2024)
LIMO (Ye et al., 2025)
s1K (Muennighoff et al., 2025)
General Question Answering
OpenBookQA (Mihaylov et al., 2018)
TriviaQA (Joshi et al., 2017)
CommonSenseQA (Talmor et al., 2019)
WikiQA (Yang et al., 2015)
HotPotQA (Yang et al., 2018)
MegaWika (Barham et al., 2023)
Code Reasoning
OpenThoughts (Zhang et al., 2024)
Llama-Nemotron-Posttraining-Dataset (NVIDIA, 2025)
KodCode (Xu et al., 2025)
open-r1/codeforces-cots (Penedo et al., 2025)
Fact Check
NaturalQuestions (Kwiatkowski et al., 2019)
TriviaQA (Joshi et al., 2017)
Indic Quest (Rohera et al., 2024)
Indian Relationships
Reasoning Gym (Stojanovski et al., 2025)
Multi Turn Conversation
ChatAlpaca (Bian et al., 2023)
NoRobots (Rajani et al., 2023)
Opus Samantha
Inference
XNLI (Conneau et al., 2018)
Role Playing
Public Domain Alpaca
LimaRP
Magpie (Touileb et al., 2024)
Data Analysis
Magpie (Touileb et al., 2024)
Advice Seeking
Magpie (Touileb et al., 2024)
Named Entity Recognition
Naamapadam (Mhaske et al., 2022)
Bharath Bench
Planning
Magpie (Touileb et al., 2024)
Text Classification
pietrolesci/civilcomments-wilds (Borkan et al., 2019)
pietrolesci/wikitoxic
pietrolesci/hyperpartisan_news_detection
Bharath Bench
Aya Collection (Singh et al., 2024b)
Brainstorming
Magpie (Touileb et al., 2024)
Grammar Correction
Bharath Bench
Information Seeking
Magpie (Touileb et al., 2024)
Translation
Flores-IN (Singh et al., 2024a)
IN-22
Indian Cultural Context
Bharath Bench
Creative Writing
Magpie (Touileb et al., 2024)
Poetry
Comprehension
TriviaQA (Joshi et al., 2017)
SQUAD (Rajpurkar et al., 2018)
SQUAD 2.0 (Rajpurkar et al., 2018)
IndicQA
Paraphrase Identification
IndicXParaphrase (Doddapaneni et al., 2023)
Math QA
OpenMathInstruct 2 (Toshniwal et al., 2024)
GSM8K (Cobbe et al., 2021)
MATH (Hendrycks et al., 2021)
Tulu3 Persona Math (Lambert et al., 2025)
Tulu3 Persona GSM8K (Lambert et al., 2025)
Text Summarization
CrossSumIN (Singh et al., 2024a)
Indic Sentence Summarization (Kumar et al., 2022)
arxiv-summarization (Cohan et al., 2018)
news-summarization
Math Instruction Tuning
MetaMathQA (Yu et al., 2023a)
Math Instruct (Puduppully et al., 2024)
Headline Generation
Indic Headline Generation (Kumar et al., 2022)
NewSHead
Math Proofs
Natural Proofs (Welleck et al., 2021)
Question Generation
Indic Question Generation (Kumar et al., 2022)
Table 3: Representative datasets curated for different sub-categories that are used as candidate datasets in our data
curation approaches.
Approaches
Prompts
Responses
Approach 1: Transla-
tion + Human Refine-
ment
English prompts →LLM translation →human
verification/adaptation.
Outputs: Indic Generic Prompts, Indic Context
Prompts.
English responses →LLM translation →
human verification/adaptation.
Outputs: Indic Generic Responses, Indic
Context Responses.
Approach 2: Synthetic
Expansion + Human
Refinement
Seed English prompts →LLM expansion (Self-
Instruct) →LLM translation →human verifica-
tion/adaptation.
Outputs: Synthetic Indic Generic Prompts, Syn-
thetic Indic Context Prompts.
Synthetic English responses →LLM
translation →human verification/adapta-
tion.
Outputs:
Synthetic Indic Generic Re-
sponses, Synthetic Indic Context Re-
sponses.
Table 4: Comparison of data construction approaches, showing pipelines for prompts and responses with resulting
categories.

--- Page 15 ---

A.3
Complexity Definitions
Notably, complexity is evaluated relative to each
task category, ensuring that difficulty levels are
interpreted within the specific context of that cat-
egory. Figures 6–11 illustrate how complexity is
defined across different task categories.
A.4
Instruction Following
Various configurations of Instruction Following
incorporate different combinations of constraints
within the prompt. Figure 12 outlines the types of
constraints considered, accompanied by illustrative
examples for clarity while human annotation.
A.5
Human Annotation Refinement
Data annotators initially assessed the performance
of the underlying LLM on both generation and
translation tasks across multiple dimensions.
For generation, raw LLM responses were as-
sessed along dimensions such as Response Rel-
evance, Grammatical Accuracy, Cohesion and
Coherence, Rationality, and Completeness (see
Table 5 for the guidelines).
As shown in Fig-
ure 13, English generations perform consistently
well: tasks such as Indian Cultural Context, Ad-
vice Seeking, Information Seeking, Named En-
tity Recognition, Inference, Paraphrase Identifica-
tion, Paraphrase Generation, and Headline Gen-
eration achieve near-perfect scores in Response
Relevance (5.00) and Completeness (4.93–5.00).
Multi-Turn Conversation also scores high in Cohe-
sion and Coherence (5.00) and Response Relevance
(4.70). Grammatical Accuracy remains strong over-
all (4.00–4.40), though slightly lower in Compre-
hension (3.20) and Creative Writing (3.93).
For translation, annotators evaluated Lexical Di-
versity, Coherence and Cohesion, Completeness,
Grammatical Accuracy, and Named Entity Han-
dling (see Table 6 for the guidelines). Hindi shows
the strongest performance, achieving the highest
Completeness (4.92) and Named Entity Handling
(4.85). Telugu and Gujarati exhibit strong Lexical
Diversity (3.43 and 3.30), while Grammatical Ac-
curacy is highest in Telugu (3.62), Hindi (3.60), and
Punjabi (3.55). Further detailed evaluation scores
are illustrated in Figure 14.
A.6
Implementation
For training, we adopt a distributed DeepSpeed-
based setup with ZeRO-3 optimization (Rajbhan-
dari et al., 2020) across 2 H100 nodes (8 GPUs
per node) to efficiently handle large-scale model
fine-tuning. The Llama-3-8B and Krutrim-2-12B
instruct models are optimized using the Direct
Preference Optimization (DPO) objective with a
Beta parameter of 0.3, controlling the strength of
preference alignment. Training is performed on
sequences up to 4096 tokens, with a maximum
prompt length of 2048 tokens to accommodate
complex multi-turn instructions. We employ the
AdamW optimizer with a learning rate of 5×10−7,
weight decay of 0.01, and a cosine learning rate
scheduler with a warming ratio of 10% warmup
ratio for stable convergence and run for 1 epoch.
The batch configuration consists of 4 samples per
device with gradient accumulation over 2 steps,
yielding an effective batch size suitable for large-
scale distributed training setup.
Post-trained Krutrim-2-12B and Llama-3-8B
models are evaluated on the Updesh dataset across
10 languages and nine categories using LLM-as-
a-Judge scoring on a scale of 1-5.
Post-DPO,
Krutrim achieves 31.7% wins, 29.9% losses, 28.6%
draws, and 9.8% both-bad cases, while Llama
records 35.0% wins, 26.1% losses, 27.9% draws,
and 11.0% both-bad cases.
B
Prompts Used
Different prompts were crafted for each category
and complexity level during prompt generation us-
ing the self-instruct pipeline. For instance, Figures
15 and 16 illustrate example prompts for the Indian
Cultural Context category under easy and hard set-
tings, respectively. Similar design considerations
were applied across other categories to address their
specific requirements.
Figure 17 presents the prompt template em-
ployed for translating English prompt-response
pairs via LLMs. The Krutrim-2-12B and Llama-
3-8B Instruct models, after being fine-tuned using
DPO on 100K examples from the Pragyaan-Align
dataset, were evaluated on the Updesh dataset. The
evaluation utilized an LLM-as-a-Judge framework
for scoring, with the corresponding prompt design
shown in Figure 18.
C
Guidelines For Manual Annotation
The data annotation team follows a set of standard-
ized guidelines designed to maintain consistency
and uniformity throughout the annotation process.
These guidelines include precise definitions for
each category and setting, which are elaborated

--- Page 16 ---

Figure 6: Complexity Definitions for each sub-category.
Dimension
Explanation
Response Relevance
Measures how well the model output addresses the user query or task
instruction.
Why it matters for Indic/Multilingual Data: Responses must stay
on-topic and satisfy user intent; irrelevant outputs reduce usability and
may confuse readers.
Errors in this area: Off-topic responses, inclusion of unrelated infor-
mation, misinterpretation of the prompt.
Grammatical Accuracy
Correct use of grammar rules including syntax, tense, agreement, punc-
tuation, and morphology.
Why it matters for Indic/Multilingual Data: Proper grammar ensures
readability and clarity; morphologically rich languages are prone to
agreement and inflection errors.
Errors in this area: Wrong tense, subject-verb disagreement, missing
auxiliaries, incorrect case markings, improperly inflected words.
Cohesion and Coherence
Cohesion = linguistic devices (connectors, pronouns, conjunctions) link-
ing sentences; Coherence = logical flow of ideas.
Why it matters for Indic/Multilingual Data: Maintains well-structured
and easily understandable responses; lack of cohesion or coherence leads
to fragmented outputs.
Errors in this area: Abrupt topic shifts, disconnected sentences, miss-
ing references, inappropriate pronoun usage.
Rationality
Logical correctness and factual consistency of the response, including
reasoning and alignment with real-world knowledge.
Why it matters for Indic/Multilingual Data: Ensures trustworthiness
and usefulness of outputs, particularly for reasoning or factual tasks.
Errors in this area: Contradictory statements, illogical conclusions,
factually incorrect assertions, hallucinations.
Completeness
The extent to which the response fully addresses the user prompt or
includes all necessary information.
Why it matters for Indic/Multilingual Data: Partial answers reduce
usefulness, especially for multi-step reasoning or detailed explanations.
Errors in this area: Missing steps in reasoning, skipped entities, trun-
cated explanations, insufficient coverage of subtopics.
Table 5: Key dimensions for assessing LLM outputs in Indic languages, highlighting relevance and frequent pitfalls.

--- Page 17 ---

Figure 7: Complexity Definitions for each sub-category.
Figure 8: Complexity Definitions for each sub-category.

--- Page 18 ---

Figure 9: Complexity Definitions for each sub-category.
Figure 10: Complexity Definitions for each sub-category.

--- Page 19 ---

Figure 11: Complexity Definitions for each sub-category.
Figure 12: Instruction following: constraint types and examples

--- Page 20 ---

Dimension
Explanation
Lexical Diversity
The variety and richness of words used in the text. Higher lexical
diversity means using a wide range of vocabulary instead of repetitive or
generic terms.
Why It Matters for Indic Data: Indic languages have rich vocabulary
and multiple synonyms; poor diversity makes translations monotonous
and unnatural.
Errors in this area: Overuse of common words, failure to use synonyms,
repetitive phrasing.
Coherence and Cohesion
Coherence: Logical flow and overall sense of the text.
Cohesion: Use of linguistic devices (connectors, pronouns, conjunc-
tions) to link sentences smoothly.
Why It Matters for Indic Data: Many Indic languages use connectives
and honorific markers that impact cohesion; direct translation from
English often breaks these links.
Errors in this area: Disconnected sentences, abrupt topic shifts, missing
conjunctions or pronouns.
Completeness
Whether the output contains all necessary information from the source
without omissions or additions.
Why It Matters for Indic Data: When translating long or complex
Indic sentences, models often skip certain parts (e.g., verb phrases or
subordinate clauses).
Errors in this area: Missing phrases, dropped entities, truncated sen-
tences, or extra hallucinated details.
Grammatical Accuracy
Correct use of grammar rules (syntax, tense, agreement, case, morphol-
ogy). It affects fluency and correctness of the output.
Why It Matters for Indic Data: Indic languages have complex inflec-
tional morphology and word order; errors often occur in case endings,
gender/number agreement, and verb conjugations.
Errors in this area: Wrong tense, missing auxiliary verbs, subject-verb
disagreement, wrong case marking.
Named Entity Handling
Correct recognition and rendering of named entities (persons, places,
organizations, dates, currencies, etc.) across languages.
Table 6: Key dimensions for assessing LLM translations in Indic languages, highlighting their significance and
common errors.
Figure 13: LLM generation quality evaluation scores across various categories.

--- Page 21 ---

Figure 14: LLM translation quality evaluation scores across 11 Indian languages.
in Section 3.3. In addition to these specifications,
dedicated frameworks for quality assurance are pro-
vided, encompassing both language quality verifica-
tion and content quality verification, as illustrated
in Figures 19 and 20, respectively.
D
Examples
We provide examples of both instruction and pref-
erence tuning datasets in Figures 21-30.

--- Page 22 ---

Figure 15: Prompt used for generation of easy Indian cultural context English prompt in Self-Instruct pipeline.

--- Page 23 ---

Figure 16: Prompt used for generation of hard Indian cultural context English prompt in Self-Instruct pipeline.

--- Page 24 ---

Figure 17: Prompt used for translation via LLM.

--- Page 25 ---

Figure 18: Prompt used for evaluating post-trained model on Pragyaan-Align data via LLM-as-a-Judge.

--- Page 26 ---

Figure 19: Comprehensive language luality guidelines outlining key linguistic dimensions such as grammar, fluency,
clarity, and naturalness for ensuring high-quality annotated data.

--- Page 27 ---

Figure 20: Content quality guidelines detailing principles for maintaining factual accuracy, contextual relevance,
safety, and adherence to task-specific requirements during data annotation.

--- Page 28 ---

Figure 21: Pragyaan-Align alignment data examples in Advice Seeking and Brainstorming categories with Easy,
1-Turn, Simple-IF, Safe, IC-3, Normal (No Thinking Trails) settings configuration.

--- Page 29 ---

Figure 22: Pragyaan-Align alignment data example in Creative Writing category with Easy, 1-Turn, Simple-IF, Safe,
IC-3, Normal (No Thinking Trails) settings configuration.

--- Page 30 ---

Figure 23: Pragyaan-Align alignment data examples in Data Analysis and Editing categories with Easy, 1-Turn,
Simple-IF, Safe, IC-3, Normal (No Thinking Trails) settings configuration.

--- Page 31 ---

Figure 24: Pragyaan-Align alignment data examples in Information Seeking, Math and Reasoning categories with
Easy, 1-Turn, Simple-IF, Safe, IC-3, Normal (No Thinking Trails) settings configuration.

--- Page 32 ---

Figure 25: Pragyaan-Align alignment data examples in Planning and Role Playing categories with Easy, 1-Turn,
Simple-IF, Safe, IC-3, Normal (No Thinking Trails) settings configuration.

--- Page 33 ---

Figure 26: Pragyaan-IT data examples in categories Indian Cultural Context - (Easy, 1-Turn, Simple-IF, Safe, IC-3,
Normal (No Thinking Trails)), Creative Writing - (Hard, 1-Turn, Simple-IF, Safe, IC-3, Normal (No Thinking Trails))
and Advice Seeking - (Easy, 3-Turn, Simple-IF, Safe, IC-3, Normal (No Thinking Trails)) settings configuration.

--- Page 34 ---

Figure 27: Pragyaan-IT data examples in categories Planning - (Hard, 1-Turn, Simple-IF, Safe, IC-3, Normal (No
Thinking Trails)) and General Question Answering - (Easy, 1-Turn, Simple-IF, Safe, IC-1, Normal (No Thinking
Trails)) settings configuration.

--- Page 35 ---

Figure 28: Pragyaan-IT data examples in categories Brainstorming - (Easy, 1-Turn, Simple-IF, Non-Safe, IC-1,
Normal (No Thinking Trails)) and Grammar Correction - (Easy, 1-Turn, Simple-IF, Safe, IC-1, Normal (No Thinking
Trails)) settings configuration.

--- Page 36 ---

Figure 29: Pragyaan-IT data examples in category Information Seeking - (Hard, 1-Turn, Medium-IF, Safe, IC-3,
Normal (No Thinking Trails)) settings configuration.

--- Page 37 ---

Figure 30: Pragyaan-IT data examples in categories Named Entity Recognition - (Hard, 1-Turn, Complex-IF, Safe,
IC-3, Normal (No Thinking Trails)), Comprehension - (Easy, 1-Turn, Simple-IF, Safe, IC-1, Normal (No Thinking
Trails)) and Inference - (Hard, 1-Turn, Simple-IF, Safe, IC-1, Normal (No Thinking Trails)) settings configuration.

```
