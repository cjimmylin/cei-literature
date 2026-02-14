---
title: "2024-Zangari-A survey on moral foundation theory and pre-trained language models - PDF Extract"
source_pdf: "2024-Zangari-A survey on moral foundation theory and pre-trained language models.pdf"
pages: 26
extracted_at: "2026-02-13T14:50:53.679142"
---

# PDF Extract: 2024-Zangari-A survey on moral foundation theory and pre-trained language models

**Source PDF:** 2024-Zangari-A survey on moral foundation theory and pre-trained language models.pdf
**Total Pages:** 26

---

## Content

```
--- Page 1 ---

Vol.:(0123456789)
AI & SOCIETY (2025) 40:4973–4998 
https://doi.org/10.1007/s00146-025-02225-w
REVIEW
A survey on moral foundation theory and pre‑trained language 
models: current advances and challenges
Lorenzo Zangari1 · Candida Maria Greco1 · Davide Picca2 · Andrea Tagarelli1
Received: 10 October 2024 / Accepted: 3 February 2025 / Published online: 24 March 2025 
© The Author(s) 2025
Abstract
Moral values have deep roots in early civilizations, codified within norms and laws that regulated societal order and the 
common good. They play a crucial role in understanding the psychological basis of human behavior and cultural orientation. 
The moral foundation theory (MFT) is a well-established framework that identifies the core moral foundations underlying 
the manner in which different cultures shape individual and social lives. Recent advancements in natural language process-
ing, particularly pre-trained language models (PLMs), have enabled the extraction and analysis of moral dimensions from 
textual data. This survey presents a comprehensive review of MFT-informed PLMs, providing an analysis of moral tenden-
cies in PLMs and their application in the context of MFT. We also review relevant datasets and lexicons and discuss trends, 
limitations, and future directions. By providing a structured overview of the intersection between PLMs and MFT, this 
work bridges moral psychology insights within the realm of PLMs, paving the way for further research and development in 
creating morally aware AI systems.
Keywords  Pre-trained language models · Moral foundation theory · Moral values survey · Natural language processing
1  Introduction
Moral values have roots in the earliest civilizations, which 
had already codified ethical principles within norms and 
laws that regulated daily life, attesting to a deep reflection 
on the order of society and the common good. They instill a 
sense of responsibility and encourage behaviors that would 
support the well-being of the community (Schwartz 1992) or 
increase the division between people within society (Brady 
et al. 2020). This makes morality a distinctive element of 
individual character, which influences decisions and human 
behavior that can lead to a sense of integrity and self-esteem 
(Rana and Solaiman 2022), and to implication of what is a 
morally good or bad life (Hofmann et al. 2014; Ellemers 
2018; Kádár et al. 2019).
In recent years, the integration of moral foundations into 
computational models has been an area of active research 
(Reinig et al. 2024). The advances in Natural Language Pro-
cessing (NLP) have revolutionized the way we extract infor-
mation and knowledge from textual data. Particularly, Pre-
trained Language Models (PLMs), powered by Transformer 
backbones (Vaswani et al. 2017), have become a ground-
breaking technology in addressing a wide range of tasks (Lin 
et al. 2022). Transformers’ self-attention mechanism allows 
for capturing global complex dependencies within input 
data, enabling exceptional performance in NLP and beyond.
Although the linguistic choices of individuals might 
reflect their moral values, the connection between lan-
guage and morality is not always clear and may be 
expressed differently across linguistic patterns (Kennedy 
et al. 2021). Despite this complexity, PLMs—by learn-
ing lexical, semantic, and factual information from a large 
corpus of training data—inevitably capture a wide range of 
cultural and moral biases embedded within the language 
(Abdulhai et al. 2024; Hämmerl et al. 2023; Schramowski 
et al. 2022). Therefore, they can serve as effective tools for 
 *	 Candida Maria Greco 
	
candida.greco@dimes.unical.it
	
Lorenzo Zangari 
	
lorenzo.zangari@dimes.unical.it
	
Davide Picca 
	
davide.picca@unil.ch
	
Andrea Tagarelli 
	
tagarelli@dimes.unical.it
1	
DIMES Dept., University of Calabria, Rende (CS), Italy
2	
University of Lausanne, Lausanne, Switzerland

--- Page 2 ---

4974
	
AI & SOCIETY (2025) 40:4973–4998
capturing and analyzing moral dimensions. In this respect, 
one emerging trend is to integrate PLMs with moral infor-
mation to infer moral foundations from input data and/
or analyze the multifaceted moral dimensions embedded 
in language models. In this respect, one of the emerging 
trends is to integrate PLMs with moral information for 
inferring moral foundations from the input data and ana-
lyzing the moral dimensions embedded in PLMs. These 
approaches are beneficial for applications in social sci-
ences, policy-making, and even in enhancing AI ethics. 
For example, PLMs can be employed to execute moral 
judgment tasks like moderating content on social plat-
forms (Franco et al. 2023); or to analyze political speeches 
and campaigns, as well as business strategies, identify-
ing potential manipulative tactics (Liu et al. 2022; Luc-
eri et al. 2024). Hence the need to study AI systems for 
morality becomes paramount. Furthermore, recent studies 
have shown that PLMs can be trained to recognize and 
reflect moral judgments, or can be inspected to reveal cer-
tain moral tendencies present in the pre-training datasets 
(Guo et al. 2023a; Preniqi et al. 2024; Zhang et al. 2023). 
Therefore, the study of methodologies integrating PLMs 
and moral foundations can provide a kind of transparency 
that becomes the basis for user’s confidence in AI systems. 
To this regard, Wang et al. (2024) introduce STREAM, a 
platform that collects human moral judgments to be used 
for the training of more ethical AI models.
In this work, we provide a systematic overview of the 
recent advances in the integration of moral foundations 
within PLMs, from the perspective of the Moral Founda-
tion Theory (MFT) (Haidt and Joseph 2004). MFT posits 
that human moral reasoning is based on innate, modular 
foundations, and identifies five core dyadic moral founda-
tions: Care/Harm, Fairness/Cheating, Loyalty/Betrayal, 
Authority/Subversion, and Sanctity/Degradation. Given 
its aim to identify moral foundations that embrace cul-
tural diversity while striving for universality, MFT has 
been the subject of extensive debate over the years (Prinz 
2009; Curry et al. 2019; Iurino and Saucier 2020). This 
has resulted in various revisions of the theory, including 
the addition of new foundations and the refinement of 
existing ones. By incorporating a theory like MFT that 
is both adaptive and widely recognized, PLMs can better 
align with the diverse and evolving moral perspectives of 
society across different cultures.
Objectives and scope of the survey.
We aim to analyze the current approaches to combin-
ing MFT and PLMs to systematize and provide valuable 
insights into how PLMs perceive and generate relevant 
content within a moral framework. We summarize our 
main contributions as follows:
•	 New taxonomy: we provide a comprehensive overview 
of the PLMs involved in the context of MFT. Addition-
ally, we formalize the essential strategies and tasks 
adopted within the domain of MFT-informed PLMs. 
Based on our theoretical framework, we organize the 
existing works in the literature into two main categories: 
(i) Moral-driven PLMs, which focus on training PLMs 
on MFT-based data; and (ii) Moral-targeted PLMs, 
which analyze the moral foundations embedded in PLM 
responses at the inference phase.
•	 Moral surveys, lexicons, and datasets: We review and 
categorize the most commonly used datasets, surveys and 
lexicons for training and assessing PLMs on MFT-related 
tasks.
•	 Findings, challenges, and future directions: We discuss 
key findings from the reviewed works, highlight ongo-
ing challenges in the field, and suggest future research 
directions. We emphasize the importance of constructing 
reliable and inclusive datasets, along with the pivotal role 
of PLMs in the context of MFT. This includes consid-
ering aspects such as the model size and the strategies 
employed for training or fine-tuning the PLMs.
To the best of our knowledge, this is the first effort to pro-
vide a comprehensive and systematic review dedicated to 
exploring the combination of MFT and PLMs. By bridging 
the gap between moral psychology and advanced computa-
tional linguistics, this work aims to lay the groundwork for 
future research and development in creating morally aware 
AI systems.
The remainder of this work is organized as follows. Sec-
tion 2 summarizes existing surveys on PLMs focusing on 
moral, ethics and cultural values aspects. Section 3 provides 
a theoretical background of the two pillars of this survey: 
MFT and PLMs. In Sect. 4 we formalize the tasks arising 
from the integration of MFT and PLMs. Section 5 gives an 
overview of widely adopted moral data sources. In Sect. 6 
we present our taxonomy and describe existing works. In 
Sect. 7 we discuss the main trends, challenges, and possible 
future directions.
2  Related works
Recent advancements in the field of moral values within 
PLMs include the design of algorithms capable of detecting 
morally relevant contents and the implementation of proce-
dures or evaluation metrics that reflect the moral perceptions 
of PLMs. However, the existing literature lacks comprehen-
sive reviews that explore the intersection of MFT and PLMs 
within a computer science perspective. Existing surveys 
mainly focus on social science, evaluating the integration 
of PLMs within human society from a broader outlook. For 

--- Page 3 ---

4975
AI & SOCIETY (2025) 40:4973–4998	
instance, Adilazuarda et al. (2024) investigate cultural val-
ues representation and inclusion in PLMs, highlighting the 
absence of a consistent definition of culture and employing 
different proxies to represent cultures. They categorized two 
broad approaches to studying cultural values inside PLMs: 
observing the response of the PLMs to various inputs and 
observing the internal state of PLMs. Wang et al. (2023) 
review the existing alignment tools for PLMs, with empha-
sis on training approaches and model assessment strategies, 
pointing out the limits of PLMs in humans, such as misread-
ing human commands and producing biased or erroneous 
material. Guo et al. (2023b) offer a review of the evaluation 
methods of PLMs, including aspects related to morality, 
such as the typically used datasets related to MFT. Similarly, 
Chang et al. (2024) provide an overview of the evaluation 
methods for PLMs in terms of robustness, ethics, biases, 
and trustworthiness. Gallegos et al. (2023) summarize bias 
evaluation and mitigation techniques for PLMs, expanding 
the notion of fairness and harm to improve the fairness capa-
bilities of PLMs. The work that most closely aligns with ours 
is Reinig et al. (2024), which provides a broad review on 
modeling morality in text analysis, covering various moral 
theories and methodologies such as transformer models, 
dictionary-/rule-based approaches, and machine learning 
techniques. The authors focus on the theoretical challenges 
in operationalizing moral values, highlighting issues such as 
low inter-annotator agreement and the scarcity of resources 
available for training and evaluation, particularly in non-
English languages. The presence of such work reflects an 
emerging interest in the intersection of moral values and AI, 
confirming that the recent research is gradually recognizing 
the need to address morality within computational models.
Differences with existing surveys. We systematically 
review works that are framed within the context of PLMs 
and MFT. Compared to other works based on the combi-
nation of PLMs and human psychological aspects, such as 
Adilazuarda et al. (2024), we do not focus solely on review-
ing methods that observe the responses or the status of the 
PLMs, but we also consider fine-tuned or further pre-trained 
PLMs for detecting moral values. Similarly to Wang et al. 
(2023), we aim to review the evaluation and training strate-
gies, but for the specific area of MFT and PLMs. Guo et al. 
(2023b), Chang et al. (2024) and Gallegos et al. (2023) 
investigate moral values only from an evaluation perspec-
tive and within the much broader scope of ethics, safety, 
and AI alignment.
In contrast to Reinig et al. (2024), our work focuses spe-
cifically on the integration of MFT and PLMs. While Reinig 
et al. (2024) offers a high-level overview of the research 
connecting morality and AI, our study provides a detailed 
examination of each individual contribution. Additionally, 
we place greater emphasis on cross-domain generalization 
and the moral biases inherent in PLMs, offering a detailed 
exploration of their role in MFT-related tasks.
Despite the increasing interest in facing moral values 
within PLMs, there is a lack of comprehensive surveys 
exploring the integration of MFT and PLMs. Existing works 
often addresses MFT and PLMs separately or marginally 
discuss their combination. Our work fills this gap by provid-
ing the first systematic review dedicated to exploring how 
MFT principles can be operationalized within PLMs. We 
introduce a novel taxonomy categorizing approaches into 
moral-driven and moral-targeted PLMs, delve into specific 
architectures and training strategies, and offer an in-depth 
analysis of relevant datasets and lexicons.
3  Theoretical background
In this section, we describe the two fundamental pillars of 
this survey: the moral foundation theory and pre-trained 
language models. In Sect. 3.1 we delve into the principles 
and applications of MFT, while in Sect. 3.2 we provide an 
overview of the PLMs involved in the works explored in this 
survey, as well as a brief description of the strategies they 
employed for tailoring PLMs to downstream applications.
3.1  Moral foundation theory
Moral foundations theory (MFT), introduced by Haidt and 
Joseph (2004), aims to investigate the underlying reasons 
behind common moral themes across different cultures. It 
posits that multiple psychological systems form the basis 
of our intuitive ethics, which are then shaped by cultural 
virtues, narratives, and institutions.
MFT’s foundational framework initially established five 
principled dichotomies, or moral foundation dimensions, 
within an evolutionary context. These dimensions represent 
critical aspects of social cooperation and conflict resolution 
that were essential for ancestral survival and flourishing:
•	 Care (vs. Harm): emphasizes the importance of caring 
for others and avoiding harm. It prompts individuals to be 
compassionate and protective toward those in vulnerable 
positions.
•	 Fairness (vs. Cheating): focuses on reciprocal altruism 
and social justice, highlighting virtues like honesty and 
integrity.
•	 Loyalty (vs. Betrayal): underscores the value of loyalty 
to groups or tribes, which historically conferred survival 
advantages by fostering strong relational bonds.

--- Page 4 ---

4976
	
AI & SOCIETY (2025) 40:4973–4998
•	 Authority (vs. Subversion): emphasizes respect for 
legitimate authority and traditions, reflecting principles 
of social organization and hierarchy.
•	 Sanctity (vs. Degradation): concerns purity and pollu-
tion, rooted in the behavioral immune system that guards 
against threats of infection or moral corruption.
Care, Fairness, Loyalty, Authority, and Sanctity1 are cat-
egorized as Virtues, while their counterparts are referred to 
as Vices. Figure 1 summarizes the key aspects behind each 
moral dimension of MFT. Each foundation is associated 
with five basic principles of human morality: (i) Adaptive 
challenge: the basic survival need or challenge addressed 
by the foundation. (ii) Original triggers: the stimuli that ini-
tially activated each foundation. (iii) Current triggers: mod-
ern stimuli that activate each foundation. (iv) Characteris-
tic emotions: the emotions typically associated with each 
foundation. (v) Relevant virtues: the positive character traits 
linked to each foundation.
In the years following its introduction, researchers 
focused on validating the original five dimensions of MFT 
through surveys, experiments, and cross-cultural compari-
sons, revealing that while all foundations were present in 
most populations studied, their relative importance varied 
across cultural and political contexts (Haidt and Graham 
2007; Graham et al. 2009; Graham and Haidt 2010).
Furthermore, while widely regarded as a robust and ver-
satile theory,2 MFT has received criticism and undergone 
significant refinement since its inception. For instance, Prinz 
(2009) challenged the notion of innate moral foundations, 
casting doubt on the nativist underpinnings of MFT and 
arguing that culture plays a more decisive role in shaping 
morality. Curry et al. (2019) noted that MFT lacks a system-
atic foundation in cooperation theory and omits key domains 
like Family, Reciprocity, Heroism, or Property. Additionally, 
its inclusion of Sanctity as a moral dimension is questioned 
for lacking clear ties to cooperative behavior.
Iurino and Saucier (2020) highlights challenges in repli-
cating its five foundations across diverse populations, hence 
questioning its universality. Furthermore, they suggest that 
MFT’s framework, developed in Western settings, struggles 
to adapt to global cultural diversity.
Over the years, these critiques have prompted further 
revisions and refinements of MFT. In particular, the initial 
set of five foundations described above has not remained 
static; rather, starting from 2011, researchers have revisited 
these dimensions in light of novel findings, cross-cultural 
examinations, and theoretical debates. Beyond the formal 
redefinition of some foundation (e.g., Fairness), the focus 
has shifted to additional candidate foundations that may 
capture morally salient intuitions not encompassed by the 
original set.
Fig. 1   The original five moral foundations (Graham et al. 2013). The Foundation column refers to the basic building blocks or core principles of 
human morality
1  Note that the value of Sanctity is also referred to as Purity.
2  https://​moral​found​ations.​org/​publi​catio​ns/.

--- Page 5 ---

4977
AI & SOCIETY (2025) 40:4973–4998	
One significant area of development involves the Fairness 
foundation. Originally conceived with a focus on equality 
as a core component, subsequent empirical evidence sug-
gested that moral judgments concerning fair treatment and 
just outcomes are more variegated than initially thought. 
Specifically, researchers recognized that notions of Fairness 
could also revolve around Proportionality, i.e., rewarding 
individuals in accordance with their contributions or merit. 
This insight prompted Atari et al. (2023) to propose splitting 
the Fairness foundation into two distinct dimensions: Equal-
ity and Proportionality. Equality centers on the importance 
of equal treatment and outcomes, appealing more strongly to 
politically left-leaning individuals, whereas Proportionality 
addresses whether resources and benefits are allocated in 
proportion to one’s efforts or achievements-principles that 
resonate more with politically right-leaning audiences. The 
recognition that Fairness encompasses multiple moral intui-
tions exemplifies how MFT accommodates greater complex-
ity as data and perspectives accumulate.
Considering other revisions that led to the inclusion of 
new moral dimensions, Iyer et al. (2012) introduced the Lib-
erty/Oppression dimension, which highlights the feelings 
of reactance and resentment people feel toward those who 
dominate them and restrict their liberty.
Atari et al. (2020) included the Honor foundation—
identified in Middle Eastern contexts—points to the moral 
weight placed on reputation, family integrity, and one’s 
social standing, elements that do not map neatly onto the 
original five foundations. This foundation has also been 
discussed by Karami et al. (2023) which examined the sali-
ence of honor-related themes in cultural narratives, showing 
the complexity of moral judgments across linguistic and 
sociocultural contexts. The expansion of the MFT with this 
dimension emphasizes the cultural specificity of certain 
moral dimensions, as well as the MFT’s openness to revis-
ing its framework to incorporate non-Western moral logics.
Likewise, the Ownership foundation, proposed as early 
as 2013 and further articulated by Atari and Haidt (2023), 
brings into focus moral intuitions about property rights 
and respect for what belongs to oneself and others. Such 
intuitions about rightful possession, theft, and territoriality 
appear to have evolutionary underpinnings and are ubiqui-
tous across cultures, yet they were not explicitly addressed 
in the initial formulation of MFT.
Incorporating new foundations and refining existing ones 
are not merely ad hoc responses to criticisms. Instead, these 
adjustments indicate an ongoing effort to improve the theo-
ry’s cultural reach, empirical rigor, and conceptual clarity. 
By focusing on dimensions that meet established criteria—
such as broad cultural presence, affective salience, and evo-
lutionary plausibility (Graham et al. 2013)—the theory has 
moved toward a more detailed account of moral cognition. 
Rather than remaining a fixed model, MFT has proceeded as 
a research program capable of responding to emerging evi-
dence and integrating a variety of scholarly perspectives. As 
a result, it continues to be a useful tool in social psychology 
and in examining cultural variations and political ideologies 
(Kobbe et al. 2020).
Fig. 2   Diagram of PLMs architectures with relative task adaptation strategies

--- Page 6 ---

4978
	
AI & SOCIETY (2025) 40:4973–4998
3.2  Pre‑trained language models
Pre-trained language models have profoundly transformed 
the field of NLP, pushing society into an era of sophisticated 
language comprehension and generation. Trained on exten-
sive corpora, these models discern patterns and structures 
within language, enabling them to excel in tasks such as 
translation, summarization, and question-answering.
In this section, we describe the specific PLMs employed 
in the works discussed in Sect. 6, and we provide a brief 
summary of the main strategies for adapting PLMs to down-
stream tasks. We emphasize that the discussed strategies are 
not exhaustive but are specifically those employed by the 
studies considered in this survey to address MFT-related 
tasks. Figure 2 shows a diagram of the potential PLMs archi-
tectures and strategies that can be employed within the field 
of MFT and PLMs.
3.2.1  Encoder‑only models: BERT and BERT‑based
BERT-based models are a family of PLMs that leverage the 
Bidirectional Encoder Representations from Transformers 
architecture (Devlin et al. 2019). These models are encoder-
based, i.e., they primarily focus on encoding the input text 
into dense vector representations. This approach allows the 
models to capture global and contextual relationships within 
the text, making them highly effective for understanding and 
processing language.
BERT (Devlin et al. 2019) has set a new standard in NLP 
by introducing the bidirectionality in the pre-training phase. 
Unlike previous models that read text sequentially, BERT 
reads the entire sequence of words at once by considering 
simultaneously the left and right context, allowing a deeply 
understand of the entire input. As a result, BERT has signifi-
cantly improved performance across a variety of NLP tasks, 
including named entity recognition, question answering and 
language inference. S-BERT (Reimers and Gurevych 2019) 
generates high-quality sentence embeddings efficiently, 
which are particularly useful for tasks like semantic search, 
sentence similarity, and clustering. S-BERT significantly 
reduces the computational effort required by BERT to find 
the most similar pair in a collection while maintaining the 
same level of accuracy. A variant of BERT is SqueezeBERT 
(Iandola et al. 2020), designed to be more efficient by reduc-
ing latency and computational requirements while maintain-
ing comparable performance levels, particularly for use on 
environments with limited computational resources.
3.2.2  Encoder–decoder models: T5
Unlike BERT, which is primarily an encoder model, T5 
(Raffel et al. 2020) employs an encoder–decoder architec-
ture that allows it to handle a wide variety of text-related 
tasks within a unified framework. The key innovation of T5 
is its text-to-text approach, where all tasks are framed as text 
generation problems. Thus, the inputs and outputs for every 
task are represented as text strings, simplifying the model’s 
application across different NLP tasks.
3.2.3  Decoder‑only models
Other models such as GPT-3, GPT-3.5 (Brown et al. 2020), 
ChatGPT (OpenAI 2023), and open alternatives like 
LLaMA-2 (Touvron et al. 2023) have further pushed the 
boundaries of what PLMs can achieve. Unlike BERT and 
T5, these models are decoder-only. Therefore, they can pre-
dict the next word in a sequence given the previous words, 
which makes them suitable for text generation tasks.
GPT-3 and GPT-3.5 (Brown et al. 2020) are among 
the most advanced in this category, capable of producing 
human-like text. It is trained to generate responses w.r.t. the 
format expected by users and human instructions and prefer-
ences. ChatGPT (OpenAI 2023) has GPT-3.5 (and GPT-4) 
as a core model, but is specifically optimized for interactive 
conversations and dialogs. OPT (Zhang et al. 2022) is an 
open generative model designed to provide an accessible 
alternative to proprietary models like GPT-3, replicating its 
performance and sizes. LLaMA-2 (Touvron et al. 2023) is 
another open-source model trained on high-quality sources 
across multiple domains, filtering low-quality content and 
repetitive or non-informative text. OpenAssistant 12B (Köpf 
et al. 2023) is fine-tuned on the OpenAssistant Conversa-
tions data, which is an assistant-style conversation corpus 
constructed with human assistance and annotations. Claude 
3 Opus (Anthropic 2024) is designed for enhanced conversa-
tional AI capabilities, reducing biases and avoiding generat-
ing harmful or unethical content. It is designed for reliability 
and reduced biases, ensuring safer and more responsible AI 
interactions.
Due to their extensive scale in terms of parameters (bil-
lions), training data, and computational resources, the mod-
els we discussed here are known as Large Language Models 
(LLMs). Note that strictly speaking, all LLMs can be viewed 
as PLMs (Chen et al. 2024).
3.2.4  Task‑adaptation strategies
In this section, we will analyze and explore the strategies uti-
lized by the approaches discussed in Sect. 6 to tailor PLMs 
to MFT-related tasks.
One of the most common approach is fine-tuning, which 
involves additional training on a smaller, task-specific data-
set, allowing the model to learn the requirements of that par-
ticular task while leveraging the broad knowledge it gained 
during pre-training. Fine-tuning typically adjusts some or 

--- Page 7 ---

4979
AI & SOCIETY (2025) 40:4973–4998	
all layers of the PLM and adds a task-specific layer, such as 
output layers for classification.
Another common strategy is the feature-based approach, 
where the PLM’s weights are frozen, and its outputs are 
used as context-sensitive word embeddings for a separate 
task-specific model (Min et al. 2024). Frozen contextual 
embeddings are employed in scenarios in which fine-tuning 
PLMs is impractical, e.g., when there is insufficient labeled 
data or for addressing computationally expensive NLP tasks.
A number of works in Sect. 6 opted for prompt engineer-
ing, which involves adding natural language text, typically in 
the form of short phrases, to provide guidance to pre-trained 
models in performing specific tasks (Min et al. 2024). The 
most common type of prompt-based learning is few-shot 
learning, in which task descriptions and examples (0 or k 
examples, respectively 0-shot or k-shot learning) are used to 
guide a PLM in performing the task. Prompt engineering has 
several advantages, such as reducing computational needs 
compared to fine-tuning and allowing unsupervised probing 
of PLMs to assess their knowledge on specific tasks.
Finally, some works employed adversarial learning and 
reinforcement learning in the fine-tuning phase. The former 
enhances model robustness by exposing them to adversarial 
attacks, which are intentionally manipulated inputs designed 
to induce inaccuracies in the model’s predictions (Goodfel-
low et al. 2015). The aim is to obtain models resilient to 
adversarial attacks and less sensitive to small perturbations 
in the input. The latter teaches models to make sequences 
of decisions by rewarding desired behaviors and penaliz-
ing undesired ones. It is particularly effective for aligning 
PLMs with human preferences. This approach has been suc-
cessfully employed to reduce harmful and biased responses, 
having outputs that are not only accurate but also align with 
societal norms (Stiennon et al. 2020).
4  MFT‑related tasks
In this section, we discuss and formalize the tasks related 
to the integration of PLMs and MFT. Our objective is to 
present a formal definitions of the primary tasks addressed 
by the investigated works, serving as a valuable foundation 
for future research endeavors. We categorize the identified 
tasks as illustrated in Fig. 3. We define TD as the MFT theory 
and D as the set of moral foundation values associated to TD. 
Without loss of generalizability, we assume that D does not 
strictly represent the original MFT foundations with virtues 
and vices, but rather moral values in which virtues and vices 
can be treated separately, i.e.,
Following this approach, D could be easily integrated with 
other moral values, i.e., {non-moral} ∪D (Hoover et al. 
2020), which can be useful for aligning with the continuous 
refinements in MFT (Iyer et al. 2012; Atari et al. 2020; Atari 
and Haidt 2023; Karami et al. 2023)
4.1  Moral values prediction
Moral values prediction involves learning a function MΘ 
that infer the moral values D from the input data. Formally, 
given the input space X,  the objective of the moral values 
prediction task is to learn MΘ ∶X ↦Y, where Y ⊆P(D), 
and P(D) indicates the powerset of D. Note that MΘ could 
be a PLM that is freezed, fine-tuned or further pre-trained 
(cf. Sect. 3.2.4) for performing the final downstream task.
To train the PLM for the moral values prediction task, we 
assume the availability of a labeled dataset L = (xi, di)n
i=1, 
where xi ∈X is an input instance, di ⊆D is the correspond-
ing label(s), and n is the size of the dataset. The goal is to 
D =
⎧
⎪
⎪
⎨
⎪
⎪⎩
Care,
Harm,
Fairness,
Cheating,
Loyalty,
Betrayal,
Authority,
Subversion,
Purity,
Degradation
⎫
⎪
⎪
⎬
⎪
⎪⎭
.
Fig. 3   Categorization of the main MFT-related tasks addressed by existing literature

--- Page 8 ---

4980
	
AI & SOCIETY (2025) 40:4973–4998
minimize the loss function L(MΘ(xi), di) over the labeled 
dataset, where the choice of the loss function depends on 
the particular setting of the problem (e.g., single-label or 
multi-label classification).
Cross-domain and within-domain moral values 
prediction.
Methods that address the moral values prediction task 
can be framed into cross-domain and within-domain sce-
narios. Note that in the current literature these scenarios 
can be referred to as out-of-domain and in-domain (Preniqi 
et al. 2024; Guo et al. 2023a; Liscio et al. 2022). Specifi-
cally, since all the works analyzed in this survey intend the 
same concept for cross- (within-) and out-of- (in-) domain, 
in this survey we use the term domain to refer to a set of 
data characterized by a distinct distribution of textual fea-
tures and labels, which can differ either due to variations 
in topical content (e.g., different social movements within 
the same dataset) or due to differences in data sources (e.g., 
social media posts vs. news articles). Under this definition, 
all cross-domain moral values prediction methods assume 
that training and test data are sampled from different domain 
distributions, both in terms of labels and textual features. 
Indeed, cross-corpus or cross-topic data are typically col-
lected in different time period, and this difference can poten-
tially impact the topics, the sentiments expressed about the 
topics, and the type of justification and reasoning used for 
the expressed sentiments (Trager et al. 2022).
Hereinafter, we will use the terms cross-domain and 
within-domain to create various setups that enrich the pre-
viously defined tasks, such as cross-domain moral values 
prediction and within-domain moral values prediction. 
Within-domain methods focus on optimizing performance 
within the same domain of the training data, that is, train and 
test data are drawn from the same distribution. Cross-domain 
approaches focus on transferring knowledge from the source 
domain(s) to the target domain. They involve adapting a 
model trained on one or multiple domains to perform well 
in a different, often less-resourced, domain. These methods 
operate under two key assumptions to improve generaliza-
tion capabilities across distinct contexts: the training and 
evaluation data are drawn from distinct distributions (i.e., 
differing in terms of labels and textual features), and the 
existence of latent data representations that are invariant 
across different environments. Figure 4 schematizes how a 
moral values prediction task is typically addressed.
4.2  Moral values alignment
In the moral value alignment problem the objective is to 
assess whether PLM response is aligned with specific moral 
Fig. 4   Within-domain and Cross-domain moral values prediction task. In the within-domain scenario, the model is trained and tested on data 
originating from the same distribution (source). In the Cross-domain scenario, the model is trained and tested on data originating from different 
distributions (source and target)
Fig. 5   Moral values alignment problem. Given data with moral con-
tents, a prompt expressing specific moral values D is generated and 
input to a PLM, which has a state S. The moral values D and the 
PLM’s response are then fed into the alignment function f to evaluate 
how well the PLM aligns with D. If the PLM is only used for infer-
ence, we are dealing with a Non-learning-based moral value align-
ment problem. If the PLM includes components that are trained or 
fine-tuned to align with f,  we are dealing with the Learning-based 
moral value alignment problem

--- Page 9 ---

4981
AI & SOCIETY (2025) 40:4973–4998	
values. In this context, alignment refers to the evaluation of 
whether the response of the PLM is in line with the moral 
values expressed in the input text X and denoted by D. Here-
inafter, we will assume that the alignment function f needs to 
be minimized, indicating that a lower value means a higher 
degree of moral alignment for the PLM. The operational 
framework for addressing this task is shown in Fig. 5. In 
our formulation, the problem can be approached as follows.
Learning-based Moral Value Alignment: We provide a 
similar setting to the one proposed by Dognin et al. (2024). 
Let us denote with S the current conversation history of the 
PLM, P the set of possible prompts given to the model, R the 
set of responses that can be generated, and f ∶R × D ↦ℝk 
an alignment function. The objective is to learn a function 
MΘ ∶S × P ↦R that provides responses ri ∈R for a given 
prompt in a given state such that f(ri, di) is minimized over 
the dataset L = (ri, di)n
i=1, with di ∈D.
For example, if a PLM is prompted with moral dilemmas, 
the aligned responses would be those that consider the moral 
dimensions relevant to the scenario. Suppose a scenario that 
involve choosing between honesty and loyalty, such as decid-
ing whether to tell the truth about a friend’s mistake or to 
keep the secret. The responses chosen by the PLM should 
reflect an understanding of the moral weight of fairness ver-
sus loyalty and make a decision that appropriately consider 
both values.
Non-learning-based Moral Value Alignment: This 
approach involves analyzing the responses of PLMs without 
the need for learning or adaptation. The predefined function 
MΘ is combined with a module that maps the responses of 
the PLMs to moral foundations based on the principles of 
MFT. This approach entails analyzing PLM responses with-
out the need for learning or adaptation. The predefined func-
tion MΘ is combined with a module that maps the responses 
of the PLMs to moral foundations based on the principles 
of MFT. For instance, PLMs can be treated as questionnaire 
respondents and their response can be compared with human 
responses, hence providing insight into the personality of 
PLMs.
5  Surveys, datasets, and lexicons with moral 
values
MFT is central to datasets on morality (Guo et al. 2023b). 
Current insights into morality largely come from analyzing 
moral vignettes, questionnaires, and social media datasets 
(Hofmann et al. 2014). We group data sources into three 
categories: (i) Moral surveys, which correspond to set of 
close-ended questions designed to gauge individuals’ moral 
beliefs, (ii) Moral lexicons, which refer to lists of word-
score pairs related to moral values, and (iii) MFT-annotated 
datasets, which refer to data manually or (semi-) automati-
cally labeled with the dimensions of MFT. Figure 6 shows 
examples of these three types of datasets. Table 1 provides a 
summary of the data sources described in this survey, along 
with their category (moral surveys, moral lexicons, mft-
annotated datasets) and their size in terms of rows.
5.1  Moral surveys
The Moral Foundations Questionnaire (MFQ) (Graham 
et al. 2011) is a psychometric tool designed to evaluate the 
extent to which individuals endorse the five moral foun-
dations of MFT. It is widely used in social psychology to 
understand individual differences in moral scenarios. The 
MFQ evaluates each foundation by utilizing 30 questions 
and six items, which are graded on a 6-point Likert scale 
(Likert 1932), anchored from 1 (“strongly disagree”) to 6 
(“strongly agree”). Table 2 shows moral foundations with 
Fig. 6   a Example of Moral Survey dataset (extracted from the MFQ); b example of Moral lexicon dataset (extracted from the MFDV2); c exam-
ple of MFT-annotated dataset (extracted from the MFTC

--- Page 10 ---

4982
	
AI & SOCIETY (2025) 40:4973–4998
corresponding example items statements used in the MFQ 
to assess an individual’s moral values related to each founda-
tion (Graham et al. 2008).
The Moral Foundations Questionnaire-2 (MFQ-2) (Atari 
et al. 2023) contains 36 questions built on top of the MFQ 
by refining Fairness/Cheating into two distinct dimensions: 
Equality/Inequality and Proportionality/Disproportional-
ity. Equality/Inequality is a concept that promotes social 
justice and equality, while Proportionality/Disproportional-
ity focuses on remuneration based on merit, contributing to 
virtues like productivity and deservingness, but also foster-
ing corruption and nepotism. Like the MFQ, the MFQ-2 
uses Likert scale assessments to gauge moral priorities, from 
1 (“slightly describes me”) to 5 (“describes me extremely 
well”). The studies conducted to develop MFQ-2 has shown 
Table 1   Summary of the data sources used in the revised works 
(Dataset), specifying whether they are Moral survey, Moral lexicon or 
MFT-annotated dataset (Category), along with their size in terms of 
number of rows (Size). Symbol “–” indicates information unavailable 
or not applicable
Dataset
Size
Labels
# annotators
Source
Moral survey
MFQ (Graham et al. 2011)
30
5 (Care/Harm, Fair./Cheat., Loyal./Betr., Auth./Subv., 
Sanct./Degrad.)
–
Link
MFQ-2 (Atari et al. 2023)
36
6 (Care/Harm, Equal./Ineq., Propor./Disprop., Loyal./
Betr., Auth./Subv., Sanct./Degrad.)
–
Link
Moral lexicon
MFDv1 (Graham et al. 2009)
324
10 (Care, Harm, Fair., Cheat., Loyal., Betr., Auth., 
Subv., Sanct., Degrad.)
–
Link
MFDv2 (Frimer 2019)
2014
10 (Care, Harm, Fair., Cheat., Loyal., Betr., Auth., 
Subv., Sanct., Degrad.)
–
Link
eMFD (Hopp et al. 2021)
3270
5 (Care/Harm, Fair./Cheat., Loyal./Betr., Auth./Subv., 
Sanct./Degrad.)
–
Link
MoralStrength (Araque et al 2020)
1000
5 (Care/Harm, Fair./Cheat., Loyal./Betr., Auth./Subv., 
Sanct./Degrad.)
At least 5 per item
Link
MFT-annotated dataset
MFTC (Hoover et al. 2020)
35,108
10 (Care, Harm, Fair., Cheat., Loyal., Betr., Auth., 
Subv., Sanct., Degrad.)
At least 3 per item
Link
MFRC (Trager et al. 2022)
16,123
8 (Care/Harm, Equal./Ineq., Propor./Disprop., Loyal./
Betr., Auth./Subv., Sanct./Degrad. Thin, Impl./
Expl.)
At least 3 per item
Link
MFNC (Weber et al. 2021)
35,985
10 (Care, Harm, Fair., Cheat., Loyal., Betr., Auth., 
Subv., Sanct., Degrad.)
557
Link
Covid (Rojecki et al. 2021)
2648
10 (Care, Harm, Fair., Cheat., Loyal., Betr., Auth., 
Subv., Sanct., Degrad.)
–
–
Congress (Johnson and Goldwasser 2018)
2050
10 (Care, Harm, Fair., Cheat., Loyal., Betr., Auth., 
Subv., Sanct., Degrad.)
2
–
Extended Congress (Roy and Goldwasser 2021) 161,295 10 (Care, Harm, Fair., Cheat., Loyal., Betr., Auth., 
Subv., Sanct., Degrad.)
–
–
Facebook (Beiró et al. 2023)
4498
12 (Care, Harm, Fair., Cheat., Loyal., Betr., Auth., 
Subv., Sanct., Degrad., Liber., Oppr.)
9
–
Covid-19 (Pacheco et al. 2022)
750
5 (Care/Harm, Fair./Cheat., Loyal./Betr., Auth./Subv., 
Sanct./Degrad.)
3
Link
Extended ArgQuality (Kobbe et al. 2020)
320
5 (Care/Harm, Fair./Cheat., Loyal./Betr., Auth./Subv., 
Sanct./Degrad.)
2
Link
MoralArg (Alshomary et al. 2022)
230,000 5 (Care/Harm, Fair./Cheat., Loyal./Betr., Auth./Subv., 
Sanct./Degrad.)
–
Link
MIC (Ziems et al. 2022)
38,000
5 (Care/Harm, Fair./Cheat., Loyal./Betr., Auth./Subv., 
Sanct./Degrad.)
186 total, 3 per item Link
MAAFS (McCurrie et al. 2018)
69
6 (Care/Harm, Fair./Cheat., Loyal./Betr., Auth./Subv., 
Sanct./Degrad., Liber./Oppr.)
575
Link
MFVs (Clifford et al. 2015)
132
6 (Care/Harm, Fair./Cheat., Loyal./Betr., Auth./Subv., 
Sanct./Degrad., Liber./Oppr.)
510
–

--- Page 11 ---

4983
AI & SOCIETY (2025) 40:4973–4998	
how the structure and influence of moral foundations vary 
across cultural contexts.
5.2  Moral lexicons
The Moral Foundations Dictionary (MFD) (Graham et al. 
2009) is the first vocabulary developed to assess moral val-
ues from textual data. The MFD provides a list of words and 
phrases associated with the five moral foundation dimen-
sions. The average number of words included in MFD for 
each moral category is 32, hence having a size of 324 words. 
MFDv2 (Frimer 2019) is an extension of MFD, which con-
sists of a lexicon of 2014 words, with each word associated 
to a single moral category. Another extension of the MFD is 
the extended Moral Foundation Dictionary (eMFD) (Hopp 
et al. 2021), a dictionary of text samples extracted from the 
Moral Foundations News Corpus (MNFC) (Weber et al. 
2021), containing English news articles on a variety of top-
ics. Lemmas and stems are annotated with a moral value and 
words in the eMFD are weighted according to a probabilistic 
scoring procedure.
MoralStrength (Araque et al 2020) is a semi-automated 
lexicon of approximately 1000 lemmas, obtained as an 
extension of the MFD, which quantifies the relevance and 
strength of words related to the five moral foundations of 
MFT. The lexicon is constructed by initially selecting seed 
words related to each moral foundation and then expanding 
this set through semantic similarity measures derived from 
word embeddings.
LibertyMFD (Araque et al. 2022) is in turn an extension 
of MoralStrength for detecting the Liberty moral dimension. 
Roy and Goldwasser (2021) extend the dataset proposed by 
Johnson and Goldwasser (2018) to build a topic indicator 
lexicon, for topics like Gun Control and Immigration.
5.3  MFT‑annotated datasets
The Moral Foundations Twitter Corpus (MFTC) by Hoover 
et al. (2020) comprises tweets, categorized into 10 moral 
values, reflecting the dyadic dimensions (i.e., care and 
harm are separate labels). Additionally, the dataset includes 
a non-moral label for tweets that do not exhibit any moral 
sentiment. It includes seven different domains related to 
morally relevant issues: (i) All lives matter, referring to 
American social movement that emerged as a reaction to the 
Black Lives Matter movement; (ii) The Baltimore Protests, 
concerning tweets related to the protest over the murder of 
Freddie Gray; (iii) Black Lives Matter, including all tweets 
with the hashtag #BlackLivesMatter; (iv) 2016 Presiden-
tial Election; (v) Davidson, a collection of hate speech and 
inflammatory language (Davidson et al. 2017); (vi) Hurri-
cane Sandy; (vii) METOO movement.
Further exploring the domain of social media, the Moral 
Foundations Reddit Corpus (MFRC) (Trager et al. 2022) 
introduces a dataset of English Reddit posts drawn from 
12 different subreddits, chosen according to the buckets of 
US politics, French politics and everyday moral life. Unlike 
Hoover et al. (2020), the MFRC does not deal with the Fair-
ness/Cheating dimension of MFT, but addresses the dimen-
sions of Equality/Inequality and Proportionality/Dispropor-
tionality, following the framework of Atari et al. (2023). It 
also includes Thin morality and Non-moral categories, i.e., 
judgments which do not clearly refer to the six moral dimen-
sion, and judgments without moral content, respectively.
The Moral Foundations News Corpus (MNFC) (Weber 
et al. 2021) comprises news articles collected from major 
outlets (e.g., The New York Times) between 2013 and 2015 
and analyzed with the MFD to detect words related to spe-
cific moral foundations. Several annotators used an online 
platform (Moral Narrative Analyzer), to highlight portions 
of the text that reflected moral content. They also identified 
the most prominent moral foundation. Additionally, they 
annotated specific entities mentioned in the text (e.g., people 
or organizations) with moral foundations.
Beiró et al. (2023) gathered English Facebook comments 
focused on the topic of COVID-19 vaccination. They manu-
ally annotated 4498 comments utilizing the same dimensions 
used by Hoover et al. (2020).
Johnson and Goldwasser (2018) collected tweets of US 
politicians related to 6 topics: (i) abortion, (ii) the Affordable 
Care Act, (iii) guns, (iv) immigration, (v) LGBTQ rights, 
and (vi) terrorism. They annotated 2050 tweets based on top-
ics, policy frames, and the five moral dimensions of MFT, 
plus a non-moral category, enabling to frame the problem as 
Table 2   Example of items 
(second column) for each 
moral foundation (first column) 
in the Moral Foundations 
Questionnaire (MFQ)
Foundation
Example item
Care
Compassion for those who are suffering is the most crucial virtue
Fairness
I think it’s morally wrong that rich children inherit a lot of money 
while poor children inherit nothing
Authority
Respect for authority is something all children need to learn
Loyalty
People should be loyal to their family members, even when they 
have done something wrong
Purity
I would call some acts wrong on the grounds that they are unnatural

--- Page 12 ---

4984
	
AI & SOCIETY (2025) 40:4973–4998
an 11-label classification task. Roy and Goldwasser (2021) 
further extended this dataset by collecting more tweets from 
US congress members, using a lexicon-based approach.
Pacheco et al. (2022) built a corpus of 750 tweets about 
the COVID-19 vaccine manually annotated by morality 
foundation, and vaccination stance (pro, anti, neutral, disa-
gree). Similarly, Rojecki et al. (2021) annotated 2648 tweets 
related to the COVID-19 pandemic.
Kobbe et al. (2020) augmented the ArgQuality Corpus 
(Wachsmuth et al. 2017), which includes debate arguments 
for two stances on 16 topics like evolution vs. creation and 
banning plastic bottles. The dataset contains 320 argu-
ments balanced by stance. Kobbe et al. (2020) annotated 
it with moral dimensions, enabling analysis of the rela-
tionship between moral values, argument quality, stance, 
and audience reactions. Similarly, Alshomary et al. (2022) 
used Hulpus et al. (2020)’s lexicon linking moral founda-
tions to Wikipedia concepts, creating a dataset of 230k 
argumentative texts balanced across five moral dimensions 
and annotated with moral values. To assess the quality of 
the proposed dataset, a sample of 100 example have been 
manually validated.
The Moral Integrity Corpus (MIC) (Ziems et al. 2022) 
was built up from Social Chemistry 101 (Forbes et al. 
2020), which is a corpus of norms describing binary judg-
ments of everyday situations. MIC extends Social Chem-
istry 101 by providing moral annotations related to MFT 
on 38,000 prompt-reply pairs.
The Moral and Affective Film Set (MAAFS) (McCur-
rie et al. 2018) comprises 69 crowd-sourced YouTube 
video clips representing MFT dimensions. Independent 
participants (575 total) rated these videos using standard-
ized questionnaires assessing MFT moral foundations, 
arousal (emotional intensity), wrongness (moral judg-
ment of actions), weirdness (perceived strangeness), and 
clarity (understanding of the moral content and context), 
among other factors. Two of the authors reviewed and 
selected videos based on alignment with moral vignettes 
or foundations.
The Moral Foundations Vignettes (MFVs) (Clifford 
et al. 2015) introduces a collection of moral vignettes, 
each violating one of the five moral foundations. It con-
tains 132 vignettes, crafted to encompass diverse content 
and validated through factor analysis and human partici-
pants. The dataset was annotated by 510 respondents and 
evaluated by approximately 30 individuals to ensure con-
sistency and reliability of the responses.
6  Methods
We organize existing studies into two main categories. The 
first one regards Moral-driven PLMs, which refer to works 
that adopt training strategies for learning model that predict 
or are aligned with moral values. The general approach here 
is to fine-tune or further pre-train PLMs for predicting the 
moral values of the underlying moral foundations hidden 
in the data. The second category, namely Moral-targeted 
PLMs, regards methods that seek to assess the moral values 
embedded into the PLMs without any moral task-specific 
adaptation, to probe their responsiveness to morally chal-
lenging issues and situations. The general approach is to 
Fig. 7   The interplay between the two categories of methods (Moral-
targeted PLMs and Moral-driven PLMs) and various aspects related 
to PLMs within the context of MFT, which encompass: the architec-
ture of the models (green rectangles), the types of MFT-related tasks 
addressed (red rectangles), the data employed (blue rectangles) and 
the strategies used for problem resolution (yellow rectangles). Dashed 
lines indicate dependency relationships, while solid lines indicate 
parent-child dependencies within the tree

--- Page 13 ---

4985
AI & SOCIETY (2025) 40:4973–4998	
analyze the PLM responses to determine their beliefs and the 
effects of training on a particular dataset. Figure 7 illustrates 
how these two categories intertwine with various aspects 
of PLMs in the context of MFT, including MFT-related 
Table 3   Summary of the selected works in this survey.  For each 
work, we indicate the reference of the source work (Ref.); the main 
component(s) used in the corresponding approach (Model); the 
addressed task (MFT-related task); the strategies for tailoring PLMs 
to the downstream application (Strategy); the data used for training 
and/or evaluation (Data); and the source code availability (Code)
Refs.
Model
MFT-related task
Data
Strategy
Code
Moral-driven PLMs
Roy and Goldwasser (2021)
DRaIL + BERT
Within-domain moral values 
prediction
Twitter (Extended Congress)
Fine-tuning
Pacheco et al. (2022)
DRaiL + BERT
Within-domain moral values 
prediction
Twitter (Covid-19)
Fine-tuning
✓
Bulla et al. (2022)
SqueezeBERT
Within-domain moral values 
prediction
Twitter (MFTC)
Fine-tuning
✓
Rao et al. (2023)
BERT
Within-domain moral values 
prediction
Twitter (MFTC, Congress, 
Covid)
Fine-tuning
Trager et al. (2022)
BERT
Within-domain moral values 
prediction
Reddit (MFRC), Twitter 
(MFTC)
Fine-tuning
Liscio et al. (2022)
BERT
Cross-domain moral values 
prediction
Twitter (MFTC)
Further pre-training + Fine-
Tuning
✓
Guo et al. (2023a)
BERT + neural architectures
Cross-domain moral values 
prediction
Twitter (MFTC, Covid, Con-
gress) and news (MFNC)
Fine-tuning + Adversarial 
learning
✓
Preniqi et al. (2024)
BERT
Within-domain and cross-
domain moral values 
prediction
Twitter (MFTC), Facebook, 
Reddit (MFRC)
Fine-tuning + Adversarial 
learning
✓
Nguyen et al. (2024)
RoBERTa
Within-domain and cross-
domain moral values 
prediction
Twitter (MFTC), Reddit 
(MFRC), MFNC, MIC, 
MFVs, Extended Congress, 
Social Chemistry
Fine-tuning
✓
Kobbe et al. (2020)
S-BERT, BERT
Within-domain and cross-
domain moral values 
prediction
MFD, Twitter (MFTC), 
Extended ArgQuality
Fine-tuning
Alshomary et al. (2022)
BERT + Project Debater
Within-domain moral value 
prediction and arguments 
generation
Extended ArgQuality
Fine-tuning
✓
Dognin et al. (2024)
Open-Assistant 12 B
Learning-based moral values 
alignment
MIC
Fine-tuning + Reinforcement 
Learning
Mokhberian et al. (2022)
RoBERTa
Within-domain moral values 
prediction
MFTC, MFRC, MFNC
Fine-tuning
Moral-targeted PLMs
Abdulhai et al. (2024)
GPT-3
Non-learning-based moral 
value alignment
MFQ
1-shot prompting
✓
Simmons (2023)
GPT-3, GPT3.5 and OPT
Non-learning-based moral 
value alignment
Social scenario data-
sets + MFDv1, MFDv2, 
and eMFD
0-shot prompting
He et al. (2024)
Various LLMs
Non-learning-based moral 
values alignment
Tweets
0-shot prompting
✓
Nunes et al. (2024)
GPT-4, Claude 2.1
Non-learning-based moral 
values alignment
MFQ, MFVs
0-shot prompting
✓
Jiang et al. (2024)
DAMF + Social-PLM
Moral values prediction
Tweets about Covid-19
Feature-based
Carrasco-Farre (2024)
Claude 3 Opus
Non-learning-based moral 
value alignment
Persuasion dataset + eMFD
0-shot prompting
Fraser et al. (2022)
T5
Non-learning-based moral 
values alignment
MFQ
0-shot prompting
Kennedy et al. (2021)
BERT
Non-learning-based moral 
values alignment
Facebook status 
updates + MFDv1, MFDv2
Feature-based,
✓
Xie et al. (2020)
S-BERT
Moral value prediction
MAAFS, MFVs
Feature-based
Hämmerl et al. (2023)
S-BERT
Non-learning-based moral 
values alignment
MFQ
Feature-based
✓

--- Page 14 ---

4986
	
AI & SOCIETY (2025) 40:4973–4998
tasks, data types, model architectures, and problem-solving 
strategies. Solid lines represent hierarchical (parent-child) 
dependencies, while dashed lines indicate relational depend-
encies. Examining these interconnections within each cat-
egory reveals correlations and patterns that help structure 
and describe the intersection of PLMs and MFT.
Table 3 shows the selected works for this survey. The 
table is partitioned into two subtables based on the afore-
mentioned categories. For each method, we describe the 
utilized model(s) (Model column); the addressed task (MFT-
related task column); the strategies for tailoring PLMs to the 
downstream application (Strategy column); the data used for 
training and/or evaluation (Data column); and the source 
code availability (Code column).
We also propose a meta-definition for the problem of 
integrating PLMs with MFT, aiming to establish a formal 
foundation framework for all the works examined.
Meta-Definition (Integration of PLMs and MFT). Let 
MΘ denote a PLM with parameters Θ, and TD denote the 
MFT theory equipped with a selected set of moral dimen-
sions D (e.g., the set of original moral dimensions pro-
posed by Haidt and Joseph (2004), or alternative set). An 
integration process between a PLM MΘ and a MFT TD can 
be described as any function belonging to a class of func-
tions F = {f ∣f ∶A →B × ℝs.t. A, B ⊆T ⧵{}}
, where 
T = {MΘ, ΨTD} and ΨTD is the set of possible non-empty out-
come sets dependent on TD, i.e., 2D ⧵{}.
The meta-definition forms the foundation for the two cat-
egories in this work: Moral-driven PLMs and Moral-targeted 
PLMs. The key difference lies in MFT’s role: in Moral-Driven 
PLMs, MFT guides training, allowing the model to predict 
moral values from input data without MFT during inference; 
Moral-Targeted PLMs rely on MFT at inference to prompt and 
interpret the model’s moral responses.
Moral-driven PLMs. PLMs are here adapted during the 
training stage to make inference based on MFT. The integra-
tion process involves a PLM MΘ in which knowledge about 
MFT is embedded into the parameters Θ. Moral-driven PLM 
can hence be expressed by a function f ∈F such that:
The process for learning the parameters Θ typically employs 
fine-tuning or pre-training techniques on data labeled with 
moral dimensions D. In the case of moral values prediction 
task, we have f ∶MΘ ↦2D × ℝ, in which the integration 
of ℝ takes into account the case in which we are dealing 
with both classification and regression tasks [e.g., ranking 
moral values (Araque et al 2020)]. As an example, consider 
a BERT model trained on social media posts labeled with the 
Care and Harm moral values. When applied to new social 
media posts, the model can predict whether a post reflects 
f ∶MΘ ↦ΨTD × ℝ.
Care or Harm, or to score how much a post contains these 
moral values.
Moral-targeted PLMs. MFT is here used to analyze and 
assess the moral values embedded within the responses gener-
ated by PLMs. The integration process involves evaluating the 
responses of MΘ to assess its behavior w.r.t. the MFT theory 
TD. Moral-targeted PLMs can hence be expressed by a function 
f ∈F such that:
In this case, the knowledge of MFT is not embedded into 
the parameters Θ, but it is injected through a transformation 
ΨTD. The function f takes the MFT theory TD as input and as 
a basis to analyze the output produced by MΘ, hence produc-
ing a response belonging to the subspace of ΨTD × ℝ. For 
instance, considering the Non-learning based moral value 
alignment task, an element of ΨTD in the domain corresponds 
to prompts with elements of TD (e.g., moral survey data-
sets). ΨTD in the co-domain can be the power set of D. For 
instance, consider prompting GPT-3 with moral dilemmas, 
such as “Is it acceptable to lie to protect someone’s feel-
ings?”. The model’s responses are then analyzed using MFT 
to determine which moral dimensions, such as Fairness or 
Loyalty, are reflected in the answers.
6.1  Moral‑driven PLMs
In this section, we describe moral-driven PLMs. Initially, we 
discuss methods that leverage BERT-based model for moral 
values prediction on social data in both within-domain and 
cross-domain scenarios. Then, we analyze studies that iden-
tify moral values to support argument analysis and moral 
values alignment.
PLMs for moral values prediction in social discourses. 
Bulla et al. (2022) extend the work of Hoover et al. (2020) 
by replacing the LSTM model with a PLM. Specifically, 
SqueezeBERT is fine-tuned on the labeled tweets of the 
MFTC dataset for the task of multi-label classification of 
moral values. Each of the moral dimensions has been defined 
as the union of the two moral values that compose it, e.g., 
for the Care moral value, positive tweets are the ones labeled 
either with Care or Harm. Experimental results show that 
the BERT-based model outperforms the LSTM in all seven 
domains of the MFTC, achieving an F1 score ranging from 
47.0 to 86.0 across the moral dimension. Similarly, Rao et al. 
(2023) fine-tune BERT on Covid, MFTC, Congress datasets 
to study partisan differences in moral language. They find 
conservatives use more negative moral language than liber-
als, indicating a more morally charged tone in conservative 
Covid-19 tweets. Political elites use moral rhetoric more 
than non-elites, suggesting leaders frame Covid-19 issues in 
moral terms, influencing public opinion. Issues like masking 
f ∶MΘ × ΨTD ↦ΨTD × ℝ.

--- Page 15 ---

4987
AI & SOCIETY (2025) 40:4973–4998	
and lockdowns are more morally charged in conservative 
discussions, while vaccines are more prominent in liberal 
discourse. Trager et al. (2022) fine-tune BERT on the moral 
dimensions of the MFRC, both in multi-label and binary 
classification settings. In the former case, all moral catego-
ries are predicted simultaneously. In the latter case, each 
label is predicted separately. Experiments have shown that 
multi-label BERT achieves lower performance than BERT 
as a binary classifier, with F1 scores ranging from 0.37 to 
0.51. On the MFTC, achieved F1 scores range from 0.54 to 
0.82. A cross-domain strategy is also considered, by down-
sampling the MFTC dataset to have the same number of 
samples for each label as MRFC for consistency purposes. 
Then, a BERT model is trained on the MFRC and tested 
on the down-sampled MFTC and vice versa. Interestingly, 
models trained on the MFRC and tested on the MFTC have 
better classification performance, with F1 scores ranging 
from 0.28 to 0.53 vs. 0.31–0.43 across the moral dimensions. 
This is mainly ascribed to the Fairness Foundation’s split 
into Proportionality and Equality, as described in Sect. 5.3, 
which makes cross-domain training more difficult.
The effect of cross-domain classification on the moral 
prediction task have been thoroughly investigated by Liscio 
et al. (2022). Each topic of the MFTC is treated as a differ-
ent domain, thus obtaining seven datasets each correspond-
ing to a topic (e.g., Black Lives Matter, Sandy, and so on), 
and train a BERT model on different settings to evaluate 
its generalizability and transferability capabilities for moral 
values prediction as well as its catastrophic forgetting prop-
erty. Each setting varies based on the source of training data, 
evaluation, or fine-tuned data. The MFTC dataset is divided 
into source and target data to test various multi-label clas-
sification scenarios. The source data consist of six out of the 
seven MFTC topics, treated as the available data, while the 
target data are derived from a novel topic of the MFTC. The 
settings are as follows: (i) in the source scenario, the source 
data correspond to the training set; (ii) in the target scenario, 
the training set corresponds to the target data; (iii) in the 
fine-tune scenario, the classifier is trained on the source data, 
and then fine-tuned on the target data; (iv) in the all sce-
nario, the training set includes both source and target data. In 
each scenario, the classifier is evaluated on both source and 
target data, resulting in eight total combinations. Best results 
are obtained considering the scenario in which the training 
set includes both source and target data, obtaining 0.75 of 
F1 score when the target dataset is related to the topic “ME 
TOO”. Moreover, similar to Trager et al. (2022), pre-training 
a BERT classifier on the MFTC yields better performance 
on unseen data, even when little training data are available. 
However, fine-tuning on a novel topic causes catastrophic 
forgetting of the topic it was pre-trained with, even when 
fine-tuning on a small portion of data from the novel topic. 
Specifically, this issue arises in the fine-tune scenario (iii), 
where the classifier is first trained on source topic data and 
then fine-tuned on target topic data. Catastrophic forgetting 
results particularly evident when evaluating the model on 
an unbalanced source derived from the Davidson topic (cf. 
Sect. 5.3), in which the shift in label distribution with other 
topics such as Black Lives Matter is pronounced.
Guo et al. (2023a) propose DAMF, a framework for moral 
value prediction on heterogeneous datasets, leveraging an 
adversarial training strategy. Rather than training the classi-
fier on the aggregation of data, features from different data-
sets are mapped into a shared common embedding space. 
Specifically, a BERT model is used to encode text, and a 
domain classifier is learned with the purpose of detecting 
the correct domain the data come from. The domain clas-
sifier works as an adversary, hence pushing BERT embed-
dings to be domain invariant. The moral foundations are the 
classified based on the learned domain-invariant embedding. 
DAMF is evaluated using different datasets in the cross-
domain setting: Covid-19, Congress, MFTC and the MFNC. 
Results show that model performance improves when fusing 
heterogeneous datasets. When using Covid-19, Congress and 
MFNC as training data, the achieved F1 score performance 
on the MFTC is equal to 0.43.
MoralBERT (Preniqi et al. 2024) is a framework in which 
both a base BERT and a BERT trained with the adversarial 
learning strategy used by Guo et al. (2023a) are fine-tuned 
for single-label and multi-label moral values prediction. 
Similarly to Trager et al. (2022) and Liscio et al. (2022), the 
single-label setting outperforms the multi-label one in terms 
of F1 score. MoralBERT with adversarial learning outper-
forms MoralStrength by a large margin and achieves F1 
score equal to 0.65 and 0.52, in the single-label and multi-
label cases, respectively. The performance degradation in 
the multi-label setting is likely due to the fact that BERT 
model is fine-tuned on a specific moral value (e.g., Care), 
and therefore they fail to capture the relationship arising 
between different moral values. In a cross-domain scenario 
(training on two social media datasets, and testing on the 
third left-out social media dataset), the overall performance 
tends to decrease since the distribution of moral values dif-
fers from dataset to dataset, even if they are from the same 
domain.
MFormer Nguyen et al. (2024) is a collection of five 
binary classifiers based on the RoBERTa-base architecture 
Liu et al. (2019), developed for predicting moral values in 
textual data. Each classifier is fine-tuned to predict one moral 
foundation (e.g., Care/Harm) and is fine-tuned on a diverse 
array of data. Specifically, the MFRC, MFTC, and MNFC 
datasets were combined into a single dataset for training 
the model. Notably, unlike other approaches such as Guo 
et al. (2023a), the authors chose not to consider the polarity 
(virtue or vice) of moral dimensions, as these are loosely 
defined concepts and assigning them can introduce noise 

--- Page 16 ---

4988
	
AI & SOCIETY (2025) 40:4973–4998
due to human annotator bias. MFormer outperformed sim-
ple baselines such as MFD (lexicon-based methods), GloVe 
(embedding similarity), and supervised classifiers (logistic 
regression) in within-domain moral foundation classifica-
tion tasks. In cross-domain evaluations, MFormer was tested 
on the MFVs, Extended Congress, Social Chemistry, and 
MIC datasets, achieving good performance across all moral 
dimensions.
Methods such as Roy and Goldwasser (2021) and Pacheco 
et al. (2022) integrate PLM encoders within declarative 
frameworks, by associating a BERT classifier to logical 
rules. Both works exploit DRaiL (Pacheco and Goldwas-
ser 2021), a framework that combines logical reasoning and 
deep learning for addressing NLP tasks. Roy and Goldwas-
ser (2021) use MFT for elucidating the political stances of 
American politicians and analyzing their positions. This is 
addressed by using logical rules within DRaIL to model 
tweets and other meta-data, from the Extended Congress 
dataset. Each rule corresponds to a classifier that maps fea-
tures on the left-hand side of the rule to the predicted output 
on the right-hand side. Three rules are defined to describe 
the foundation of a tweet, the ideology, and the topic. Each 
base rule is associated with a BERT model to encode tweets. 
Combining multiple rules encoded with BERT is shown to 
be useful in prediction, achieving the highest performance 
in terms of the F1 score (0.52). Concerning MFT, a strong 
correlation is found between the usage of MFT and politi-
cians’ nuanced stances on particular divisive issue, based 
on Twitter. For example, considering the topic of ‘immigra-
tion’, Democrats employ the term Care to refer to dreamers 
and young people, while Republicans use this term when 
discussing ‘border wall’ and ‘border patrol’. Pacheco et al. 
(2022) apply a similar architecture to identify the moral 
foundation in tweets about the Covid-19 vaccine. Each 
tweet is annotated with its moral foundation and vaccina-
tion stance. Relational properties of tweets are described 
using logical rules, indicating whether a tweet includes a 
moral judgment, its specific moral foundation, and vaccina-
tion stance. Like Roy and Goldwasser (2021), tweets are 
encoded using BERT. Jointly modeling moral judgment 
and vaccination stance improves performance on the moral 
prediction task. Mokhberian et al. (2022) aim to improve 
the performance of RoBERTa in moral value prediction by 
identifying and removing noisy annotations in the MFTC, 
MFRC and MFNC datasets. Noisy annotations reflect the 
subjectivity of human judgments on moral issues, which 
often lead to annotator disagreement based on personal 
beliefs, but also ambiguity of the texts and human errors. 
Specifically, the authors quantify such disagreement through 
entropy and identify outliers by evaluating how well a text 
labeled by an annotator aligns with other texts assigned the 
same label. Training the model on the refined datasets show 
significant improvements in classification performance, 
including higher F1 scores and accuracy.
PLMs to support argument analysis. The approaches 
by Kobbe et al. (2020) and Alshomary et al. (2022) aim 
to identify moral values for supporting argument analysis. 
Kobbe et al. (2020) propose different variants of S-BERT 
to generate text encoding. In one of these, the MFD is used 
as seed data, and S-BERT is fine-tuned to encode moral 
foundations in DBpedia3 data labeled utilizing the MFD 
through a weak-supervision strategy. In another approach, 
S-BERT is enhanced with sense-disambiguation features 
through a word sense-disambiguated version of the MFD 
based on WordNet synsets. For evaluating the methods, both 
the MFTC and the extended ArgQuality corpus are used. 
In one setting, MFTC is used for training different models 
in a within-domain scenario. When dealing with a cross-
domain scenario, models are trained on the MFTC and tested 
on the extended ArgQuality corpus. In both cases, multi-
label BERT is the best-performing method, with an average 
F1 score equal to 0.45 and 0.308, respectively. The lower 
performance for the moral class would be explained by the 
differences in class distribution between the two datasets. 
Interestingly, in the experiments related to the correlations 
of multi-label BERT between arguments and moral values, 
a weak positive correlation is observed between argument 
quality and moral sentiment for the two most frequent cat-
egories on the ArgQuality corpus.
Alshomary et al. (2022) propose Moral Debater to exam-
ine how morally framed arguments influence different audi-
ences. A model is learned to identify moral foundations in 
arguments by fine-tuning BERT on the MoralArg dataset. 
By testing it on the ArgQuality corpus, the model is found 
to outperform the multi-label BERT model of Kobbe et al. 
(2020), obtaining an average F1 score of 0.40 vs. 0.28. The 
learned model is used to study the effect of morally framed 
arguments on the audience by combining it with IBM’s 
Project Debater (Slonim 2022). Given as input a controver-
sial topic, a stance on the topic, and a set of morals to be 
targeted, it generates arguments with the given stance. The 
findings indicate that the generated arguments are aligned 
with the audience’s moral beliefs. In the case of conserva-
tive views, arguments that emphasize loyalty, authority, and 
purity are compelling, whereas for liberal views, arguments 
respond strongly to themes of care and fairness.
Adapting PLMs to support specific moral values. Con-
sidering the task of learning-based moral value alignment, 
Dognin et al. (2024) propose Contextual Moral Value Align-
ment Through Context-Based Aggregation (CMVA-GS), 
which leverages MFT to create a series of moral agents 
based on OpenAssistant 12B. Each moral agent is fine-
tuned using reinforcement learning, with reward functions 
3  https://​www.​dbped​ia.​org/.

--- Page 17 ---

4989
AI & SOCIETY (2025) 40:4973–4998	
tailored to its respective moral values. The reward function 
indicates the reward for a specific action at a given prompt 
based on the moral value being optimized. The moral agents’ 
responses are then aggregated contextually to generate the 
final output. The fine-tuning and evaluation dataset is the 
Moral Integrity Corpus (MIC), which is labeled on five 
moral dimensions. The CMVA-GS models tend to achieve 
the highest ROUGE scores, indicating better alignment with 
moral values compared to other PLMs such as Llama-7B 
and Llama-13B.
6.2  Moral‑targeted PLMs
We further explore the existing literature of works exam-
ining the moral alignment of PLMs. We firstly review the 
literature that leverages LLMs, which inherit moral inclina-
tions during their training phase or are influenced by prompt 
design to provide biased responses in relation to specific 
moral values. Then, we delve into studies which explore 
the inherent moral biases in the contextual embeddings of 
encoder–decoder and encoder-based PLMs.
Moral values discovery through prompt engineering. 
Abdulhai et al. (2024) analyze the moral foundations of 
GPT-3 models (curie, babbage and davinci) to understand 
the values encoded from their training data and their poten-
tial impact on unforeseen tasks. They examine whether these 
models exhibit specific moral stances, the consistency of 
these stances across contexts, and how prompts can influ-
ence their endorsement of certain moral foundations.
Questions from the MFQ are exploited to construct 
prompts containing a description of the task, a rating scale 
specifying the model response (from 0, meaning ‘not rel-
evant’, to 5, which is ‘extremely relevant’), and a static 
example to show the model how to structure its response. 
To evaluate potential cultural and political biases in GPT-
3, its default responses are analyzed and prompted with a 
political affiliation. By comparing the response of GPT-3 
models with human studies, it is observed that less expen-
sive GPT-3 models (curie, babbage) exhibit greater differ-
ences from human moral foundations, while more expensive 
models (davinci) align more closely, suggesting that larger 
models may better capture moral political values. As regards 
the consistency of PLMs’ moral foundations across different 
contexts, certain dimensions (e.g., Fairness and Purity) are 
weighted more strongly than others. Additionally, results 
reveal moral correlations in the model’s responses (prompts 
exalting Authority also lead to higher scores on the Purity 
traits, similarly for Fairness and Harm). Overall, the results 
suggest that while GPT-3 models may exhibit certain polit-
ical tendencies, these can be modified through deliberate 
prompting, which also affects behavior in downstream tasks.
Simmons (2023) examines the “moral mimicry” phenom-
ena, i.e., whether PLMs can replicate the US political party 
moral biases. The goals are (i) to assess whether PLMs uti-
lize moral terminology appropriately in different situations; 
(ii) if they can emulate human moral biases when given a 
political identity; and (iii) if and how the model size influ-
ences such capability. Prompts are intended to motivate 
language models to provide clear moral justifications. Each 
prompt contains a scenario, a political identity statement 
and a moral stance. The scenario is a description of circum-
stances or behaviors that need moral assessment. A politi-
cal identity statement is a text referencing political beliefs, 
such as “liberal” or “conservative”. A moral stance labels 
the scenario’s acceptance or disapproval such as “moral" or 
“immoral”. Five distinct prompt templates are utilized to 
assess sensitivity to specific phrasings. Three dictionaries 
(MFDv1, MFDv2, and eMFD) are used to evaluate the moral 
foundational content of the responses from GPT-3, GPT-3.5, 
and OPT models. To focus on foundational content, the posi-
tive or negative connotations of words are removed, merg-
ing Virtues and Vices into a single category (for example, 
Care/Harm). Experimental results for the first goal show that 
PLMs increase their use of specific moral foundations when 
those foundations are salient in a given scenario. However, 
PLMs diverge more from human consensus than individual 
humans, indicating they do not perfectly replicate human 
use of moral foundations. When conditioned with politi-
cal identity, PLMs apply more individualizing foundations 
(Care/Harm, Fairness/Cheating) when prompted with a 
liberal identity, and more binding foundations (Authority/
Subversion, Sanctity/Degradation, Loyalty/Betrayal) when 
prompted with a conservative identity. Larger models, espe-
cially within the OPT family, demonstrate stronger moral 
mimicry.
Jiang et al. (2024) combine DAMF with Social-PLM 
(Jiang and Ferrara 2024) to detect moral values on a 
COVID-19 dataset (Chen et al 2020) and analyze social 
media user groups. Users valuing fairness and authority 
participate more in discussions, while those emphasizing 
Care and Purity show distinct engagement patterns. Tweets 
combining multiple moral foundations are rare but attract 
more engagement.
Carrasco-Farre (2024) examines the ability of PLMs to 
adjust their arguments based on the prompt, employing per-
suasive strategies that require different levels of cognitive 
effort and utilizing different moral language. To this pur-
pose, the study utilizes the responses of the experiments 
performed by Anthropic,4 in which human participants were 
presented with various claims on divise topics (e.g., police 
body cameras and lab-grown meat) and corresponding per-
suasive arguments generated by Claude 3 Opus or human-
generated. Persuasiveness is measured by shifts in agree-
ment with claims before and after exposure to arguments. 
4  https://​www.​anthr​opic.​com/​news/​measu​ring-​model-​persu​asive​ness.

--- Page 18 ---

4990
	
AI & SOCIETY (2025) 40:4973–4998
The PLM is prompted to produce arguments using different 
persuasive techniques (for example, arguments aimed at 
persuading undecided or opposed individuals). The analysis 
focuses on both cognitive effort, through readability and per-
plexity, and the moral-emotional language, evaluated using 
sentiment analysis and the frequency of words expressing 
MFT moral traits. The PLM use more moral language than 
humans overall, with a higher frequency of both positive and 
negative moral foundations, contributing to its persuasive 
power. The study suggests that the strategic use of moral 
language by PLMs, including negative bias such as harm and 
cheating, plays a significant role in persuasion.
He et al. (2024) focus on evaluating the affective align-
ment of 36 LLMs (such as LLaMA-2, GPT-3, OPT and etc.). 
The goal is to measure how closely the models’ emotional 
and moral tone aligns with humans ones from liberal and 
conservative perspectives. It uses two prompting approaches: 
default prompting, where LLMs generate responses without 
ideological context, and steered prompting, where LLMs are 
guided to adopt a liberal or a conservative perspective. The 
responses generated by the models are compared to exist-
ing tweets on contentious topics like COVID-19 and abor-
tion. Using DAMF, the moral values from these tweets are 
extracted, while the political ideologies of the users are iden-
tified based on the political bias of the news sources shared 
in their tweets. The results reveal that LLMs tend to express 
higher levels of Care and Loyalty than human tweets, skew-
ing towards liberal perspectives, even when prompted with 
conservative viewpoints.
Nunes et al. (2024) explore whether GPT-4 and Claude 
2.1 exhibit moral hypocrisy by testing the consistency of 
the models’ abstract principles and whether such abstract 
principles align with their judgments in real-life scenarios. 
The models were assessed with MFQ for abstract values and 
the MFVs for concrete moral judgments. Specifically, they 
are prompted to respond to MFQ and MFVs with numeri-
cal answers (e.g., on a Likert scale) without providing any 
explanatory text or reasoning. While both models showed 
consistency in handling abstract values, y comparable to 
human respondents, they struggled to apply these values 
across different concrete contexts, revealing a form of moral 
hypocrisy.
Moral bias analysis in PLMs embeddings. Fraser et al. 
(2022) explore the Delphi framework (Jiang et al. 2021) 
for MFT. It is a PLM built on the UNICORN (Lourie et al. 
2021) model, which is a specialized version of T5 for com-
monsense question answering. Delphi is fine-tuned on the 
COMMONSENSE NORM BANK dataset (Jiang et al. 
2021), consisting of various moral judgments on everyday 
situations. Delphi responds to ethical queries in various for-
mats, predicting moral judgments that align with general 
societal views. The system’s final task is to provide moral 
judgments in response to user queries. According to Fraser 
et al. (2022), when using the MFQ as a basis for their Del-
phi queries, the two most crucial foundations are Care and 
Fairness.
Kennedy et al. (2021) aim to assess a direct connection 
between individual moral concerns and language, examin-
ing both moral and general language (i.e., not necessarily 
expressing moral concerns). In this study, data are gath-
ered from 2.6k participants, including their responses to 
the MFQ and 107k Facebook posts. Two approaches are 
employed to relate moral concerns to language. The first 
is MFD-based, testing the connection between moral lan-
guage (via MFD and MFDv2) and individual concerns. 
The second approach uses general language, applying 
bag-of-words with LDA and text embeddings via GloVE 
and BERT. A regression analysis is carried out to predict 
each MFQ score from the text representations. Experimen-
tal results reveal that MFD-based measures are generally 
less effective at predicting moral concerns compared to 
NLP-techniques. In particular, BERT is able to capture 
differences in language w.r.t. moral concerns that were not 
captured by individuals’ lexicons.
Xie et al. (2020) introduce a text-based method for pre-
dicting human moral judgments of moral scenarios. The 
aim is to ascertain whether human-judged moral categories 
can be deduced solely from text, leveraging contextualized 
language models. The study assesses different representa-
tions of moral scenarios and their efficacy in categorizing 
nuanced moral differences, even with limited training data. 
The scenarios are gathered from three independent data-
sets, including MAAFS and MFVs. The experimental set-
tings evaluate several classifiers with different representa-
tions of moral vignettes, including contextual embeddings 
with S-BERT. S-BERT embeddings achieve the highest 
accuracy across all datasets and classification methods.
Hämmerl et al. (2023) explore whether moral standards 
learned from dominant languages, such as English, are 
imposed on other languages during cross-lingual transfer 
learning. They employ the MORALDIRECTION frame-
work for multilingual PLMs to encode action verbs with 
positive and negative connotations. These verbs are used 
in template questions to generate sentence embeddings, 
and PCA is applied to derive a “moral direction” subspace. 
The scores are then normalized to estimate moral values. 
The framework is tested with multilingual models (e.g., 
mBERT, XLM-R), monolingual models, and S-BERT 
models for each language, showing high correlation 
between S-BERT and human moral judgments across lan-
guages, though slightly lower for Arabic and Czech with 
XLM-R.
Training with parallel data eliminates cultural differ-
ences, aligning models more closely with English. Anal-
ysis of parallel sentence pairs highlights discrepancies 

--- Page 19 ---

4991
AI & SOCIETY (2025) 40:4973–4998	
caused by literal translations and lexical confusion, espe-
cially in Czech-English pairs.
PLMs’ moral dimensions are evaluated using the MFQ 
by comparing model scores against human responses 
across cultures. While models can generally distinguish 
right from wrong, they struggle with complex sentences 
and negations. The models’ scores do not fully align with 
human responses and vary by language, with greater dis-
crepancies observed in models trained on smaller lan-
guage-specific datasets, underscoring the impact of train-
ing data on moral judgments.
7  Findings, challenges and future directions
Our discussion so far has provided insights into the poten-
tial of PLMs in modeling the framework of MFT. These 
insights might contribute to a deeper understanding of the 
complexities involved in integrating MFT and PLMs and 
the ongoing efforts to improve their performance.
Main trends in the existing literature. Observing 
Table 3, recurring patterns can be noticed regarding mod-
els selection, tasks addressed, data employed, and strate-
gies used (the interplay among the categories and these 
aspects are shown in Fig. 7). From the perspective of 
model choice, BERT and BERT-based models represent 
the most commonly used technology when creating moral-
driven PLMs, while LLMs are primarily employed as 
moral-targeted PLMs. Clearly, the choice of the model has 
a significant impact on the adaptation strategy as well as 
the number of layers to freeze during training. Therefore, 
a clear separation of strategies can be observed between 
moral-driven PLMs, which exclusively use fine-tuning 
strategies to adapt to MFT task, and moral-targeted PLMs, 
which adopt few-shot prompting and feature extraction. 
Particularly, given the relatively smaller number of param-
eters of BERT compared to larger models, the majority 
of works opt to train all its layers. Approaches involving 
LLMs, on the other hand, more selective in their training 
strategies due to the significantly larger number of param-
eters. Typically, fine-tuning techniques such as Low-Rank 
Adaptation (LoRA) are employed, allowing updates to be 
made to only a small subset of parameters, such as adapt-
ers or embedding layers, while the majority of the layers 
remains frozen Dognin et al. (2024).
Moral-driven PLMs are frequently employed for tasks 
involving moral values prediction, while moral-targeted 
PLMs are predominantly utilized for moral value align-
ment tasks. Specifically, MFT-annotated datasets are 
generally used in the context of within-domain and cross-
domain moral values prediction tasks. Conversely, lexi-
cons and moral surveys are primarily used for address-
ing moral value alignment challenges. As regards the 
employed data, we can notice that moral surveys and 
moral lexicons are mostly used to evaluate moral value 
alignment, while MFT-annotated datasets are primarily 
involved in tasks of moral values prediction.
Correlation between moral foundations and political 
stances. A prominent theme is the correlation between 
moral foundations and political stances. Roy and Gold-
wasser (2021) demonstrate a strong link between the use 
of moral foundation language in tweets and the nuanced 
political positions of U.S. politicians on issues such as 
gun control and immigration. This correlation is further 
explored by the work of Simmons (2023), who finds that 
changing the political identity in prompts affects the like-
lihood of expressing particular moral foundations, with 
PLMs using more individualizing foundations when 
prompted with a liberal identity, and more binding foun-
dations when prompted with a conservative identity. Addi-
tionally, Rao et al. (2023) highlights partisan differences in 
moral language, noting that conservatives tend to use more 
negative moral language compared to liberals, suggesting 
a more critical and morally charged tone in conservative 
tweets.
PLMs vs Lexicon-based methods. The superiority of 
PLMs over traditional and lexicon-based methods is evi-
dent in several studies. Bulla et al. (2022) notice enhanced 
performance with PLMs upon earlier works, while Xie et al. 
(2020) highlight the superior performance of contextual 
embeddings in predicting human moral judgments. Addi-
tionally, Kennedy et al. (2021) point out the limitations of 
lexicon-based measures, suggesting that predefined moral 
dictionaries may not fully capture the complexity and vari-
ability of moral language as expressed naturally by indi-
viduals. The moral nuances in natural language can be bet-
ter captured by PLMs. Furthermore, Roy and Goldwasser 
(2021) and Pacheco et al. (2022) investigated the integra-
tion of PLMs with logical reasoning frameworks. They 
show that combining PLMs such as BERT with declarative 
frameworks like DRaiL enhances the performance of NLP 
tasks by effectively modeling complex relational properties 
and dependencies in text data. This approach allows for the 
definition of logical rules that capture these dependencies, 
leading to improved performance.
Effect of training strategies. Training strategies, includ-
ing fine-tuning and adversarial learning, have shown several 
enhancements in moral value prediction tasks. The works 
proposed by Kobbe et al. (2020), Alshomary et al. (2022), 
Dognin et al. (2024), and Guo et al. (2023a) highlight the 
effectiveness of these approaches in aligning model outputs 
with desired moral values.
Fine-tuning emerges as the predominant strategy for 
adapting models to specific tasks and datasets, involv-
ing additional training on task-specific datasets to capture 
nuances and improve performance. Adversarial learning, as 

--- Page 20 ---

4992
	
AI & SOCIETY (2025) 40:4973–4998
employed by DAMF (Guo et al. 2023a) and MoralBERT 
(Preniqi et al. 2024), is used to create domain-invariant 
embeddings, improving cross-domain performance by 
reducing the impact of domain-specific biases. Prompt engi-
neering and reinforcement learning are notable strategies for 
aligning PLMs with specific moral values without extensive 
fine-tuning.
Effect of prompting. Several works have examined how 
the construction of prompts can elicit specific moral traits 
and influence PLM responses. This aspect is crucial for 
understanding how PLMs reflect and generate moral judg-
ments, providing insights into the moral tendencies embed-
ded in the models’ pre-training data. Abdulhai et al. (2024) 
and Simmons (2023) show that deliberate prompting can 
significantly influence the moral foundations exhibited by 
models, affecting their responses and behaviors in various 
tasks. This highlights the malleability of PLMs and their 
potential to be guided through carefully designed prompts to 
exhibit desired moral and ethical considerations. Addition-
ally, modifying the models’ moral stances through prompt-
ing affects their behavior in downstream tasks, such as dona-
tion decisions, demonstrating the practical implications of 
moral prompting.
Effect of cross-domain strategies. Cross-domain 
strategies and their impact on model performance have 
been extensively explored. Trager et al. (2022), Liscio 
et al. (2022), Preniqi et al. (2024), Guo et al. (2023a) and 
Alshomary et al. (2022) demonstrate that training models 
on heterogeneous datasets generally improves performance. 
However, challenges remain due to class distribution differ-
ences and the phenomenon of catastrophic forgetting when 
models are fine-tuned on new domains, as noted by Liscio 
et al. (2022). This issue highlights the difficulty of maintain-
ing model accuracy across varied datasets.
Cross-lingual approach and lack of diverse datasets. 
Cross-lingual transfer of moral standards is another criti-
cal area of investigation. Hämmerl et al. (2023) explores 
whether moral standards learned from dominant language 
sources (e.g., English) are imposed on other languages dur-
ing cross-lingual transfer learning, which could lead to nega-
tive consequences. Training with parallel data tends to elimi-
nate cultural differences, aligning models more closely with 
English, but models trained on smaller, language-specific 
datasets show more variability in moral judgments. How-
ever, the scarcity of labeled datasets in non-English lan-
guages limits our understanding of how PLMs perform in 
predicting moral values across diverse linguistic and cultural 
settings. An exception is Simonsen and Widmann (2023), 
which collected more than 20k sentences from political com-
munication across six languages (Danish, Dutch, English, 
German, Swedish, and Spanish) to study moral appeals in 
party manifestos from ten Western democracies. It is worth 
mentioning also the Moral Machine (Awad et al. 2018), an 
online platform which exposes moral dilemmas to face as 
car drivers and collected 40M decisions in 10 languages 
from millions of people in 233 countries. While these efforts 
represent important steps forward, they remain limited in 
scope and coverage.
Recent studies on cultural bias in NLP models reveal that 
PLMs often mirror the cultural norms of high-resource lan-
guages. For instance, Tao et al. (2024) shows that widely 
used PLMs tend to align more closely with the cultural val-
ues of English-speaking and Protestant European countries 
compared African-Islamic countries. Navigli et al. (2023) 
highlights that most NLP models are heavily influenced by 
high-resource languages, resulting in skewed representations 
of cultural norms and values. The dominance of these lan-
guages in training corpora amplifies their influence on down-
stream tasks, often neglecting the unique cultural dimensions 
of low-resource languages. Johnson et al. (2022) demon-
strate the challenges associated with low-resource languages, 
where limited data availability hinders the training and per-
formance of PLMs. Creating balanced and representative 
datasets from various cultural and linguistic backgrounds 
will ensure that PLMs can better generalize moral judgments 
across different contexts. Overall, the ability of PLMs to 
effectively represent and predict moral values in linguisti-
cally and culturally distinct low-resource languages remain 
uncertain. A comprehensive training on diverse datasets is 
crucial for improving the alignment of PLMs with moral 
values across different languages and cultures. Without such 
efforts, the there is a risk of perpetuating moral biases that 
favor high-resource languages and aligning poorly with the 
moral standards of underrepresented communities.
Moreover, the majority of existing datasets are sourced 
from social media platforms, as indicated in Sect. 5, which 
limits the diversity of language and context represented. The 
reliance on social media data, primarily in English, does not 
capture the full spectrum of moral values across different 
cultures and languages.
The role of model size. Model size also plays a crucial 
role in moral alignment. The works proposed by Abdulhai 
et al. (2024) and Simmons (2023) indicate that larger mod-
els, such as GPT-3, align more closely with human moral 
foundations compared to smaller models. This suggests that 
model complexity contributes to better capturing and repre-
senting moral values.
Bias on moral judgment and reliability of manually 
annotated data. The potential bias in moral judgments is 
discussed by Fraser et al. (2022), who hypothesize that Del-
phi’s moral principles are likely influenced by the moral 
views of its annotators, specifically young, English-speaking 
North Americans. This highlights a broader concern: the 
responses of systems trained on morally annotated data-
sets may not be universally applicable or unbiased. Sev-
eral works have highlighted the inherent subjectivity and 

--- Page 21 ---

4993
AI & SOCIETY (2025) 40:4973–4998	
potential biases in annotating moral judgments, emphasizing 
the influence of annotators’ worldviews, beliefs, and demo-
graphic characteristics. For instance, Ziems et al. (2022) 
point out that any collection of moral judgments will inher-
ently reflect the worldviews of its annotators. In their work, 
they employed Amazon Mechanical Turk workers, which 
tend to be more educated, less religious, and more likely to 
be unemployed w.r.t. the general population, according to 
Goodman et al. (2013). Similarly, Kobbe et al. (2020) and 
Mokhberian et al. (2022) emphasize that the personal beliefs 
of human annotators can influence the annotation process, 
raising questions about the validity of annotations employed 
in training and evaluating automated systems. This issue 
is further elaborated by Johnson and Goldwasser (2018), 
who observed the political bias of annotators when labeling 
tweets. To mitigate this, annotators were instructed to label 
from the perspective of the politician who wrote the tweet. 
Also Trager et al. (2022) noted that moral judgments are 
highly subjective and likely to be influenced by the annota-
tors’ sociopolitical and demographic contexts. They argue 
that while such biases may have minimal impact on tasks 
like sentiment analysis, they can profoundly affect domains 
involving moral values. They provided detailed psychologi-
cal and demographic metadata about their annotators and 
recognize that their dataset reflects biases specific to its Eng-
lish-speaking, affluent, and predominantly liberal annota-
tor pool, which limits its representativeness of global moral 
concerns. Similarly, Hoover et al. (2020) discuss disagree-
ments among annotators on moral foundations, highlighting 
the difficulty in achieving consensus due to the absence of 
objective criteria for moral coding. They warn that resolv-
ing such disagreements excessively can artificially inflate 
inter-annotator reliability, masking the inherent subjectiv-
ity of moral judgments. To this regard, Weber et al. (2021) 
provide further evidence on the subjectivity and variability 
inherent in human moral annotations. Their study shows that 
even highly trained annotators (i.e., individuals who have 
undergone extensive preparation specifically tailored to the 
annotation task) fail to achieve high inter-annotator reliabil-
ity, emphasizing that moral intuition extraction is strongly 
influenced by individuals’ demographic and ideological 
characteristics. They argue that traditional methods rely-
ing on small groups of expert annotators may inadvertently 
inflate inter-annotator reliability through implicit consensus-
building, potentially at the expense of validity. Instead, they 
propose leveraging crowd-sourcing platforms to aggregate 
annotations from a diverse population, acknowledging and 
embracing the inherent subjectivity of moral judgments as 
a more valid approach.
These considerations highlights the need for a careful 
selection of annotators, ensuring a sufficient demographic 
and moral diversity to promote balanced and fair moral 
judgments. A related issue is the reliability of manually 
annotated data. Before moral values can be reliably utilized 
for argument analysis, the quality of the annotations must be 
ensured. A low inter-annotator agreement doubt the validity 
of the findings, raising concerns about the consistency and 
accuracy of these annotations (Kobbe et al. 2020; Fraser 
et al. 2022). Therefore, there is an emergency for robust and 
standardized annotation processes.
Moral labeling discrepancy. Another limitation regards 
the data sources utilized in the field (Table 1). Among 
the various datasets, a notable discrepancy is observed 
in the choice of labels, with some datasets employing 10 
or more labels and others opting for 5. The underlying 
motivation for this decision is that both labeling schemes 
are closely related, and it is often ambiguous which end 
of the dimension is being addressed, particularly in the 
context of negated sentences; for instance, the sentence 
“I could never hurt you” could either be classified under 
Harm due to its use of vocabulary related to this dimension 
or be annotated as the opposite, Care, since it expresses an 
inability to harm someone, thereby aligning more strongly 
with the Virtue class (Kobbe et al. 2020). This duality 
underscores the complexity and subjectivity inherent in 
labeling and categorizing moral dataset, since also PLMs 
exhibit inconsistencies, especially with complex phrases 
and negation (Hämmerl et al. 2023).
Ontologies to guide PLMs. Given the flexibility of 
PLMs and their significant responsiveness to prompting, 
there is a clear need for models that can be guided by 
predefined ontologies to provide consistent and coherent 
responses aligned with a specific worldview. The core 
issue here is that morality is deeply influenced by cul-
tural factors, which vary widely across different societies. 
By integrating ontologies, which encapsulate structured 
knowledge and worldviews, models can be better directed 
to align their outputs with culturally relevant moral stand-
ards. This approach would involve embedding cultural 
and moral frameworks directly into the model’s training 
process, ensuring that the generated responses adhere to 
these predefined moral principles. Such a method would 
mitigate the influence of arbitrary prompts and steer the 
model towards more stable and culturally coherent moral 
judgments.
Explainability and interpretability. A critical area lack-
ing in current research is the explainability and interpret-
ability of PLM outputs concerning moral judgments. Most 
existing works do not explore the reasoning behind the 
model’s outputs, leaving a gap in understanding how deci-
sions are made. This lack of transparency can undermine 
trust in these models, especially in sensitive applications 
involving moral and ethical considerations. Incorporat-
ing methods similar to the Chain-of-Thought approach, as 
demonstrated in the work of Jin et al. (2022), can signifi-
cantly enhance the interpretability of PLMs. By explicitly 

--- Page 22 ---

4994
	
AI & SOCIETY (2025) 40:4973–4998
detailing the steps and reasoning paths taken to arrive at 
a given solution, users can gain insights into the underly-
ing processes of the model. This not only improves trust 
and reliability but also allows for the identification and 
correction of biases and errors in the model’s reasoning. 
Developing frameworks for explainability and interpret-
ability in moral prediction tasks is essential for advancing 
the field and ensuring the ethical deployment of PLMs.
8  Conclusions
This survey explores the field related to the intersection 
between MFT and PLMs, highlighting the efforts made 
in targeting and driving PLMs in the context of MFT. We 
formalized the MFT-related tasks addressed by current 
PLMs and provided a meta-definition that can encompass a 
broad spectrum of PLMs integrating MFT. This theoretical 
framework enables to categorize the current approaches in 
the field. Hence, we provided a comprehensive overview 
of the current state of research, highlighting significant 
advances and ongoing challenges. By addressing these 
challenges and exploring new research directions, such 
as enhancing dataset reliability, improving cross-domain 
generalization, and integrating ontologies for consistent 
moral alignment, the field can move towards developing 
morally aware AI systems capable of operating effectively 
in diverse and multicultural environments. These advance-
ments would pave the way for AI systems that are not only 
technically proficient but also ethically sound, contributing 
positively to the society.
Acknowledgements  A.T., resp. C.M.G, is supported by project "Future 
Artificial Intelligence Research (FAIR)'' spoke 9 (H23C22000860006), 
resp. project SERICS (PE00000014), both under the MUR National 
Recovery and Resilience Plan (NextGenerationEU).
Author Contributions  D.P. conceived the idea presented in this work. 
L.Z. and C.M.G. performed the literature search and critical analysis. 
A.T. supervised the writing, reviewing and editing. All authors partici-
pated in the writing process.
Funding  Open access funding provided by Università della Calabria 
within the CRUI-CARE Agreement.
Data availability  No datasets were generated or analyzed during the 
current study.
Declarations 
Conflict of interest  The authors declare no competing interests.
Open Access  This article is licensed under a Creative Commons Attri-
bution 4.0 International License, which permits use, sharing, adapta-
tion, distribution and reproduction in any medium or format, as long 
as you give appropriate credit to the original author(s) and the source, 
provide a link to the Creative Commons licence, and indicate if changes 
were made. The images or other third party material in this article are 
included in the article’s Creative Commons licence, unless indicated 
otherwise in a credit line to the material. If material is not included in 
the article’s Creative Commons licence and your intended use is not 
permitted by statutory regulation or exceeds the permitted use, you will 
need to obtain permission directly from the copyright holder. To view a 
copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
References
Abdulhai M, Serapio-García G, Crepy C et al (2024) Moral founda-
tions of large language models. In: Al-Onaizan Y, Bansal M, 
Chen Y (eds) Proceedings of the 2024 conference on empirical 
methods in natural language processing, EMNLP 2024, Miami, 
FL, USA, November 12–16, 2024. Association for Computa-
tional Linguistics, pp 17737–17752. https://​aclan​tholo​gy.​org/​
2024.​emnlp-​main.​982
Adilazuarda MF, Mukherjee S, Lavania P et al (2024) Towards measur-
ing and modeling “culture” in LLMs: a survey. In: Al-Onaizan Y, 
Bansal M, Chen YN (eds) Proceedings of the 2024 Conference 
on Empirical Methods in Natural Lan- guage Processing. Asso-
ciation for Computational Linguistics, Miami, Florida, USA, pp 
15763–15784. https://​doi.​org/​10.​18653/​v1/​2024.​emnlp-​main.​
882. https://​aclan​tholo​gy.​org/​2024.​emnlp-​main.​882/
Alshomary M, El Baff R, Gurcke T et al (2022) The moral debater: 
a study on the computational generation of morally framed 
arguments. In: Muresan S, Nakov P, Villavicencio A (eds) 
Proceedings of the 60th annual meeting of the association for 
computational linguistics (volume 1: long papers). Association 
for Computational Linguistics, Dublin, pp 8782–8797. https://​
aclan​tholo​gy.​org/​2022.​acl-​long.​601
Anthropic A (2024) The claude 3 model family: Opus, Sonnet, 
Haiku. Claude-3 Model Card
Araque O, Gatti L, Kalimeri K (2020) Moralstrength: exploiting a 
moral lexicon and embedding similarity for moral foundations 
prediction. Knowl Based Syst 191:105184. https://​doi.​org/​10.​
1016/j.​knosys.​2019.​105184
Araque O, Gatti L, Kalimeri K (2022) LibertyMFD: a lexicon to assess 
the moral foundation of liberty. In: Proceedings of the 2022 
ACM conference on information technology for social good, pp 
154–160. Association for Computing Machinery, New York, NY, 
USA, GoodIT ’22, p 154–160. https://​doi.​org/​10.​1145/​35244​58.​
35472​64
Atari M, Haidt J (2023) Ownership is (likely to be) a moral foundation. 
Behavioral and Brain Sciences 46:e326. https://​doi.​org/​10.​1017/​
S0140​525X2​30011​9X
Atari M, Graham J, Dehghani M (2020) Foundations of morality in 
Iran. Evol Hum Behav 41(5):367–384
Atari M, Haidt J, Graham J et al (2023) Morality beyond the weird: 
how the nomological network of morality varies across cultures. 
J Personal Soc Psychol 125(5):1157–1188. https://​doi.​org/​10.​
1037/​pspp0​000470
Awad E, Dsouza S, Kim R et al (2018) The moral machine experiment. 
Nature 563(7729):59–64
Beiró MG, D’Ignazi J, Bustos VP et al (2023) Moral narratives around 
the vaccination debate on facebook. In: Ding Y, Tang J, Sequeda 
JF et al (eds) Proceedings of the ACM web conference 2023, 
WWW 2023, Austin, TX, USA, 30 April 2023–4 May 2023. 
ACM, pp 4134–4141. https://​doi.​org/​10.​1145/​35435​07.​35838​65
Brady WJ, Crockett MJ, Van Bavel JJ (2020) The mad model of 
moral contagion: the role of motivation, attention, and design 
in the spread of moralized content online. Perspect Psychol Sci 
15(4):978–1010
Brown TB, Mann B, Ryder N et al (2020) Language models are 
few-shot learners. In: Proceedings of the 34th international 

--- Page 23 ---

4995
AI & SOCIETY (2025) 40:4973–4998	
conference on neural information processing systems. Curran 
Associates Inc., Red Hook, NY, USA, NIPS’20
Bulla L, Giorgis SD, Gangemi A et al (2022) Detection of morality in 
tweets based on the moral foundation theory. In: Nicosia G, Ojha 
V, Malfa EL et al (eds) Machine learning, optimization, and data 
science—8th international workshop, LOD 2022, Certosa di Pon-
tignano, Italy, September 19–22, 2022, revised selected papers, 
part I. Lecture notes in computer science, vol 13810. Springer, 
Berlin, pp 1–13. https://​doi.​org/​10.​1007/​978-3-​031-​25599-1_1
Carrasco-Farre C (2024) Large language models are as persuasive as 
humans, but how? about the cognitive effort and moral-emotional 
language of LLM arguments. CoRR. arXiv:​2404.​09329. https://​
doi.​org/​10.​48550/​ARXIV.​2404.​09329
Chang Y, Wang X, Wang J et al (2024) A survey on evaluation of large 
language models. ACM Trans Intell Syst Technol 15(3):39:1–
39:45. https://​doi.​org/​10.​1145/​36412​89
Chen E, Lerman K, Ferrara E et al (2020) Tracking social media dis-
course about the COVID-19 pandemic: development of a pub-
lic coronavirus Twitter data set. JMIR Public Health Surveill 
6(2):e19273
Chen Z, Mao H, Li H et al (2024) Exploring the potential of large 
language models (LLMs) in learning on graphs. ACM SIGKDD 
Explor Newsl 25(2):42–61
Clifford S, Iyengar V, Cabeza R et al (2015) Moral foundations 
vignettes: a standardized stimulus database of scenarios based on 
moral foundations theory. Behav Res Methods 47(4):1178–1198
Curry OS, Chesters MJ, Van Lissa CJ (2019) Mapping morality with 
a compass: testing the theory of ‘morality-as-cooperation’ with 
a new questionnaire. J Res Personal 78:106–124
Davidson T, Warmsley D, Macy MW et al (2017) Automated hate 
speech detection and the problem of offensive language. In: Pro-
ceedings of the eleventh international conference on web and 
social media, ICWSM 2017, Montréal, Québec, Canada, May 
15–18, 2017. AAAI Press, pp 512–515. https://​aaai.​org/​ocs/​
index.​php/​ICWSM/​ICWSM​17/​paper/​view/​15665
Devlin J, Chang M, Lee K et al (2019) BERT: pre-training of deep bidi-
rectional transformers for language understanding. In: Burstein 
J, Doran C, Solorio T (eds) Proceedings of the 2019 conference 
of the North American chapter of the Association for Computa-
tional Linguistics: human language technologies, NAACL-HLT 
2019, Minneapolis, MN, USA, June 2–7, 2019, volume 1 (long 
and short papers). Association for Computational Linguistics, 
Dublin, pp 4171–4186. https://​doi.​org/​10.​18653/​v1/​n19-​1423
Dognin PL, Rios J, Luss R et al (2024) Contextual moral value align-
ment through context-based aggregation. CoRR. arXiv:​2403.​
12805. https://​doi.​org/​10.​48550/​ARXIV.​2403.​12805
Ellemers N (2018) Morality and social identity. In: van Zomeren M, 
Dovidio JF (eds) The Oxford handbook of the human essence. 
Oxford University Press, Oxford. https://​doi.​org/​10.​1093/​oxfor​
dhb/​97801​90247​577.​013.5
Forbes M, Hwang JD, Shwartz V et al (2020) Social chemistry 101: 
learning to reason about social and moral norms. In: Webber B, 
Cohn T, He Y et al (eds) Proceedings of the 2020 conference on 
empirical methods in natural language processing, EMNLP 2020, 
Online, November 16–20, 2020. Association for Computational 
Linguistics, Dublin, pp 653–670. https://​doi.​org/​10.​18653/​v1/​
2020.​emnlp-​main.​48
Franco M, Gaggi O, Palazzi CE (2023) Analyzing the use of large 
language models for content moderation with chatGPT examples. 
In: Guidi B, Michienzi A, Ricci L (eds) Proceedings of the 3rd 
international workshop on open challenges in online social net-
works, OASIS 2023, Rome, Italy, September 4–8, 2023. ACM, 
pp 1–8. https://​doi.​org/​10.​1145/​35996​96.​36128​95
Fraser KC, Kiritchenko S, Balkir E (2022) Does moral code have a 
moral code? Probing Delphi’s moral philosophy. In: Verma A, 
Pruksachatkun Y, Chang KW et al (eds) Proceedings of the 2nd 
workshop on trustworthy natural language processing (TrustNLP 
2022). Association for Computational Linguistics, Seattle, pp 
26–42. https://​aclan​tholo​gy.​org/​2022.​trust​nlp-1.3
Frimer J (2019) Moral foundations dictionary 2.0. https://​doi.​org/​10.​
17605/​OSF.​IO/​EZN37
Gallegos IO, Rossi RA, Barrow J et al (2023) Bias and fairness in large 
language models: a survey. Comput Linguist 50(3):1097–1179. 
https://​doi.​org/​10.​1162/​colia​00524
Goodfellow IJ, Shlens J, Szegedy C (2015) Explaining and harnessing 
adversarial examples. In: Bengio Y, LeCun Y (eds) 3rd Interna-
tional conference on learning representations, ICLR 2015, San 
Diego, CA, USA, May 7–9, 2015, conference track proceedings. 
http://​arxiv.​org/​abs/​1412.​6572
Goodman JK, Cryder CE, Cheema A (2013) Data collection in a flat 
world: the strengths and weaknesses of mechanical Turk samples. 
J Behav Decis Mak 26(3):213–224
Graham J, Haidt J (2010) Beyond beliefs: religions bind individuals into 
moral communities. Personal Soc Psychol Rev 14(1):140–150
Graham J, Nosek BA, Haidt J et al (2008) Moral foundations ques-
tionnaire. J Personal Soc Psychol. https://​doi.​org/​10.​1037/​
t05651-​000
Graham J, Haidt J, Nosek BA (2009) Liberals and conservatives rely 
on different sets of moral foundations. J Personal Soc Psychol 
96(5):1029
Graham J, Nosek BA, Haidt J et al (2011) Mapping the moral domain. 
J Personal Soc Psychol 101(2):366
Graham J, Haidt J, Koleva S et al (2013) Moral foundations theory: 
the pragmatic validity of moral pluralism. In: Advances in 
experimental social psychology, vol 47. Elsevier, Amsterdam, 
pp 55–130. https://​doi.​org/​10.​1016/​B978-0-​12-​407236-​7.​00002-
4. https://​linki​nghub.​elsev​ier.​com/​retri​eve/​pii/​B9780​12407​23670​
00024
Guo S, Mokhberian N, Lerman K (2023a) A data fusion framework 
for multi-domain morality learning. In: Lin Y, Cha M, Quercia D 
(eds) Proceedings of the seventeenth international AAAI confer-
ence on web and social media, ICWSM 2023, Limassol, Cyprus, 
June 5–8, 2023. AAAI Press, pp 281–291. https://​doi.​org/​10.​
1609/​icwsm.​v17i1.​22145
Guo Z, Jin R, Liu C et al (2023b) Evaluating large language models: 
a comprehensive survey. CoRR. arXiv:​2310.​19736. https://​doi.​
org/​10.​48550/​arXiv.​2310.​19736
Haidt J, Graham J (2007) When morality opposes justice: conservatives 
have moral intuitions that liberals may not recognize. Soc Justice 
Res 20(1):98–116
Haidt J, Joseph C (2004) Intuitive ethics: how innately prepared intui-
tions generate culturally variable virtues. Daedalus 133(4):55–
66. https://​doi.​org/​10.​1162/​00115​26042​365555
Hämmerl K, Deiseroth B, Schramowski P et al (2023) Speaking multi-
ple languages affects the moral bias of language models. In: Rog-
ers A, Boyd-Graber JL, Okazaki N (eds) Findings of the Associa-
tion for Computational Linguistics: ACL 2023, Toronto, Canada, 
July 9–14, 2023. Association for Computational Linguistics, pp 
2137–2156. https://​doi.​org/​10.​18653/​v1/​2023.​findi​ngs-​acl.​134
He Z, Guo S, Rao A et al (2024) Whose emotions and moral sentiments 
do language models reflect? In: Ku LW, Martins A, Srikumar V 
(eds) Findings of the Association for Computational Linguistics 
ACL 2024. Association for Computational Linguistics, Bangkok, 
Thailand and virtual meeting, pp 6611–6631. https://​doi.​org/​10.​
18653/​v1/​2024.​findi​ngs-​acl.​395. https://​aclan​tholo​gy.​org/​2024.​
findi​ngs-​acl.​395
Hofmann W, Wisneski DC, Brandt MJ et al (2014) Morality in every-
day life. Science 345(6202):1340–1343
Hoover J, Portillo-Wightman G, Yeh L et al (2020) Moral foundations 
Twitter corpus: a collection of 35k tweets annotated for moral 
sentiment. Soc Psycholo Personal Sci 11(8):1057–1071. https://​
doi.​org/​10.​1177/​19485​50619​876629

--- Page 24 ---

4996
	
AI & SOCIETY (2025) 40:4973–4998
Hopp FR, Fisher JT, Cornell D et al (2021) The extended moral foun-
dations dictionary (eMFD): development and applications of a 
crowd-sourced approach to extracting moral intuitions from text. 
Behav Res Methods 53:232–246
Hulpus I, Kobbe J, Stuckenschmidt H et al (2020) Knowledge graphs 
meet moral values. In: Gurevych I, Apidianaki M, Faruqui M 
(eds) Proceedings of the ninth joint conference on lexical and 
computational semantics, *SEM@COLING 2020, Barcelona, 
Spain (Online), December 12–13, 2020. Association for Com-
putational Linguistics, pp 71–80. https://​aclan​tholo​gy.​org/​2020.​
stars​em-1.​8/
Iandola FN, Shaw AE, Krishna R et al (2020) Squeezebert: what can 
computer vision teach NLP about efficient neural networks? 
In: Moosavi NS, Fan A, Shwartz V et al (eds) Proceedings of 
SustaiNLP: workshop on simple and efficient natural language 
processing, SustaiNLP@EMNLP 2020, Online, November 20, 
2020. Association for Computational Linguistics, pp 124–135. 
https://​doi.​org/​10.​18653/​v1/​2020.​susta​inlp-1.​17
Iurino K, Saucier G (2020) Testing measurement invariance of the 
moral foundations questionnaire across 27 countries. Assessment 
27:365–372. https://​doi.​org/​10.​1177/​10731​91118​817916
Iyer R, Koleva S, Graham J et al (2012) Understanding libertarian 
morality: the psychological dispositions of self-identified liber-
tarians. PLoS ONE 7(8):e42366. https://​doi.​org/​10.​1371/​journ​
al.​pone.​00423​66
Jiang J, Ferrara E (2024) Social-LLM: modeling user behavior at 
scale using language models and social network data. CoRR 
abs/2401.00893. https://​doi.​org/​10.​48550/​ARXIV.​2401.​00893
Jiang L, Hwang JD, Bhagavatula C et al (2021) Can machines learn 
morality? The Delphi experiment. arXiv preprint. arXiv:​2110.​
07574. https://​doi.​org/​10.​48550/​arXiv.​2110.​07574
Jiang J, Luceri L, Ferrara E (2024) Moral values underpinning COVID-
19 online communication patterns. CoRR. abs/2401.08789. 
https://​doi.​org/​10.​48550/​ARXIV.​2401.​08789
Jin Z, Levine S, Gonzalez F et al (2022) When to make exceptions: 
exploring language models as accounts of human moral judg-
ment. In: Proceedings of the 36th international conference on 
neural information processing systems. Curran Associates Inc., 
Red Hook, NY, USA, NIPS’22
Johnson K, Goldwasser D (2018) Classification of moral foundations 
in microblog political discourse. In: Gurevych I, Miyao Y (eds) 
Proceedings of the 56th annual meeting of the Association for 
Computational Linguistics (volume 1: long papers). Association 
for Computational Linguistics, pp 720–730. https://​doi.​org/​10.​
18653/​v1/​P18-​1067. https://​aclan​tholo​gy.​org/​P18-​1067
Johnson RL, Pistilli G, Menédez-González N et al (2022) The ghost 
in the machine has an American accent: value conflict in GPT-
3. CoRR. arXiv:​2203.​07785. https://​doi.​org/​10.​48550/​ARXIV.​
2203.​07785
Kádár DZ, Parvaresh V, Ning P (2019) Morality, moral order, and lan-
guage conflict and aggression: a position paper. J Lang Aggress 
Confl 7(1):6–31. https://​doi.​org/​10.​1075/​jlac.​00017.​kad. https://​
www.​jbe-​platf​orm.​com/​conte​nt/​journ​als/​10.​1075/​jlac.​00017.​kad
Karami B, Bakouie F, Gharibzadeh S (2023) A transformer-based deep 
learning model for Persian moral sentiment analysis. J Inf Sci. 
https://​doi.​org/​10.​1177/​01655​51523​11883​44
Kennedy B, Atari M, Davani AM et al (2021) Moral concerns are dif-
ferentially observable in language. Cognition 212:104696
Kobbe J, Rehbein I, Hulpuş I et al (2020) Exploring morality in argu-
mentation. In: Cabrio E, Villata S (eds) Proceedings of the 7th 
workshop on argument mining. Association for Computational 
Linguistics, Online, pp 30–40. https://​aclan​tholo​gy.​org/​2020.​
argmi​ning-1.4
Köpf A, Kilcher Y, von Rütte D et al (2023) Openassistant conver-
sations - democratizing large language model alignment. In: 
Proceedings of the 37th international conference on neural 
information processing systems. Curran Associates Inc., Red 
Hook, NY, USA, NIPS’23
Likert R (1932) A technique for the measurement of attitudes. Arch 
Psychol 140:1–55
Lin T, Wang Y, Liu X et al (2022) A survey of transformers. AI Open 
3:111–132. https://​doi.​org/​10.​1016/j.​aiopen.​2022.​10.​001
Liscio E, Dondera A, Geadau A et al (2022) Cross-domain classifi-
cation of moral values. In: Carpuat M, de Marneffe M, Ruíz 
IVM (eds) Findings of the Association for Computational Lin-
guistics: NAACL 2022, Seattle, WA, United States, July 10–15, 
2022. Association for Computational Linguistics, pp 2727–2745. 
https://​doi.​org/​10.​18653/​v1/​2022.​findi​ngs-​naacl.​209
Liu Y, Ott M, Goyal N et al (2019) RoBERTa: a robustly optimized 
BERT pretraining approach. arXiv:​1907.​11692. https://​doi.​org/​
10.​48550/​arXiv.​1907.​11692
Liu Y, Zhang XF, Wegsman D et al (2022) POLITICS: pretraining with 
same-story article comparison for ideology prediction and stance 
detection. In: Carpuat M, de Marneffe M, Ruíz IVM (eds) Find-
ings of the Association for Computational Linguistics: NAACL 
2022, Seattle, WA, United States, July 10–15, 2022. Association 
for Computational Linguistics, pp 1354–1374. https://​doi.​org/​10.​
18653/​v1/​2022.​findi​ngs-​naacl.​101
Lourie N, Bras RL, Bhagavatula C et al (2021) UNICORN on RAIN-
BOW: a universal commonsense reasoning model on a new mul-
titask benchmark. In: Thirty-fifth AAAI conference on artificial 
intelligence, AAAI 2021, thirty-third conference on innovative 
applications of artificial intelligence, IAAI 2021, the eleventh 
symposium on educational advances in artificial intelligence, 
EAAI 2021, virtual event, February 2–9, 2021. AAAI Press, pp 
13480–13488. https://​doi.​org/​10.​1609/​aaai.​v35i15.​17590
Luceri L, Boniardi E, Ferrara E (2024) Leveraging large language mod-
els to detect influence campaigns on social media. In: Chua T, 
Ngo C, Lee RK et al (eds) Companion proceedings of the ACM 
on web conference 2024, WWW 2024, Singapore, Singapore, 
May 13–17, 2024. ACM, pp 1459–1467. https://​doi.​org/​10.​1145/​
35893​35.​36519​12
McCurrie CH, Crone DL, Bigelow F et al (2018) Moral and affective 
film set (MAAFS): a normed moral video database. PLoS One 
13(11):e0206604
Min B, Ross H, Sulem E et al (2024) Recent advances in natural lan-
guage processing via large pre-trained language models: a survey. 
ACM Comput Surv 56(2):30:1–30:40. https://​doi.​org/​10.​1145/​
36059​43
Mokhberian N, Hopp FR, Harandizadeh B et al (2022) Noise audits 
improve moral foundation classification. In: IEEE/ACM inter-
national conference on advances in social networks analysis and 
mining, ASONAM 2022, Istanbul, Turkey, November 10–13, 
2022. IEEE, pp 147–154. https://​doi.​org/​10.​1109/​ASONA​
M55673.​2022.​10068​681
Navigli R, Conia S, Ross B (2023) Biases in large language mod-
els: origins, inventory, and discussion. ACM J Data Inf Qual 
15(2):10:1–10:21. https://​doi.​org/​10.​1145/​35973​07
Nguyen TD, Chen Z, Carroll NG et al (2024) Measuring moral dimen-
sions in social media with mformer. Proc Int AAAI Conf Web 
Soc Media 18(1):1134–1147. https://​doi.​org/​10.​1609/​icwsm.​
v18i1.​31378
Nunes JL, Almeida GFCF, de Araújo M et al (2024) Are large lan-
guage models moral hypocrites? A study based on moral founda-
tions. In: Das S, Green BP, Varshney K et al (eds) Proceedings 
of the seventh AAAI/ACM conference on AI, ethics, and society 
(AIES-24) - Full Archival Papers, vol 1, October 21–23, 2024, 
San Jose, California, USA. AAAI Press, pp 1074–1087. https://​
doi.​org/​10.​1609/​AIES.​V7I1.​ 31704. arXiv:​abs/​2405.​11100
OpenAI (2023) ChatGPT. https://​openai.​com/​blog/​chatg​pt

--- Page 25 ---

4997
AI & SOCIETY (2025) 40:4973–4998	
Pacheco ML, Goldwasser D (2021) Modeling content and context with 
deep relational learning. Trans Assoc Comput Linguist 9:100–
119. https://​doi.​org/​10.​1162/​tacl_a_​00357
Pacheco ML, Islam T, Mahajan M et al (2022) A holistic framework 
for analyzing the COVID-19 vaccine debate. In: Carpuat M, 
de Marneffe MC, Meza Ruiz IV (eds) Proceedings of the 2022 
conference of the North American chapter of the Association for 
Computational Linguistics: human language technologies. Asso-
ciation for Computational Linguistics, Seattle, pp 5821–5839, 
https://​doi.​org/​10.​18653/​v1/​2022.​naacl-​main.​427. https://​aclan​
tholo​gy.​org/​2022.​naacl-​main.​427
Preniqi V, Ghinassi I, Ive J et al (2024) MoralBERT: a fine-tuned lan-
guage model for capturing moral values in social discussions. In: 
Proceedings of the 2024 international conference on information 
technology for social good. Association for Computing Machin-
ery, New York. https://​doi.​org/​10.​1145/​36775​25.​36786​94
Prinz JJ (2009) Against moral nativism. In: Stich: and his critics, pp 
167–189. https://​doi.​org/​10.​1002/​97814​44308​709.​ch10
Raffel C, Shazeer N, Roberts A et al (2020) Exploring the limits of 
transfer learning with a unified text-to-text transformer. J Mach 
Learn Res 21:140:1–140:67. http://​jmlr.​org/​papers/​v21/​20-​074.​
html
Rana SS, Solaiman M (2022) Moral identity, consumption values and 
green purchase behaviour. J Islam Mark 14(10):2550–2574. 
https://​doi.​org/​10.​1108/​JIMA-​01-​2021-​0030
Rao A, Guo S, Wang SN et al (2023) Pandemic culture wars: partisan 
differences in the moral language of COVID-19 discussions. In: 
He J, Palpanas T, Hu X et al (eds) IEEE international conference 
on big data, BigData 2023, Sorrento, Italy, December 15–18, 
2023. IEEE, pp 413–422. https://​doi.​org/​10.​1109/​BigDa​ta590​
44.​2023.​10386​084
Reimers N, Gurevych I (2019) Sentence-BERT: sentence embeddings 
using Siamese BERT-networks. In: Inui K, Jiang J, Ng V et al 
(eds) Proceedings of the 2019 conference on empirical methods 
in natural language processing and the 9th international joint 
conference on natural language processing, EMNLP-IJCNLP 
2019, Hong Kong, China, November 3–7, 2019. Association for 
Computational Linguistics, pp 3980–3990. https://​doi.​org/​10.​
18653/​v1/​D19-​1410
Reinig I, Becker M, Rehbein I, et al (2024) A survey on modelling 
morality for text analysis. In: Ku LW, Martins A, Srikumar V 
(eds) Findings of the Association for Computational Linguistics 
ACL 2024. Association for Computational Linguistics, Bangkok, 
Thailand and virtual meeting, pp 4136–4155. https://​doi.​org/​10.​
18653/​v1/​2024.​findi​ngs-​acl.​245. https://​aclan​tholo​gy.​org/​2024.​
findi​ngs-​acl.​245
Rojecki A, Zheleva E, Levine L (2021) The moral imperatives of self-
quarantining. In: Annual meeting of the American Political Sci-
ence Association
Roy S, Goldwasser D (2021) Analysis of nuanced stances and senti-
ment towards entities of US politicians through the lens of moral 
foundation theory. In: Ku LW, Li CT (eds) Proceedings of the 
ninth international workshop on natural language processing for 
social media. Association for Computational Linguistics, Online, 
pp 1–13. https://​doi.​org/​10.​18653/​v1/​2021.​socia​lnlp-1.1. https://​
aclan​tholo​gy.​org/​2021.​socia​lnlp-1.1
Schramowski P, Turan C, Andersen N et al (2022) Large pre-trained 
language models contain human-like biases of what is right and 
wrong to do. Nat Mach Intell 4(3):258–268
Schwartz SH (1992) Universals in the content and structure of val-
ues: theoretical advances and empirical tests in 20 countries. In: 
Advances in experimental social psychology, vol 25. Academic 
Press, pp 1–65. https://​doi.​org/​10.​1016/​S0065-​2601(08)​60281-6. 
https://​www.​scien​cedir​ect.​com/​scien​ce/​artic​le/​pii/​S0065​26010​
86028​16
Simmons G (2023) Moral mimicry: large language models produce 
moral rationalizations tailored to political identity. In: Padma-
kumar V, Vallejo G, Fu Y (eds) Proceedings of the 61st annual 
meeting of the Association for Computational Linguistics (vol-
ume 4: student research workshop). Association for Computa-
tional Linguistics, Toronto, Canada, pp 282–29.https://​doi.​org/​
10.​18653/​v1/​2023.​acl-​srw.​40. https://​aclan​tholo​gy.​org/​2023.​
acl-​srw.​40
Simonsen KB, Widmann T (2023) The politics of right and wrong: 
moral appeals in political communication over six decades in 
ten western democracies. https://​doi.​org/​10.​31219/​osf.​io/​m6qkg. 
http://​osf.​io/​m6qkg
Slonim N (2022) Project debater—an autonomous debating system. In: 
Proceedings of the international symposium on artificial intel-
ligence and mathematics 2022 (ISAIM 2022), Fort Lauderdale, 
Florida, USA, January 3–5, 2022. https://​isaim​2022.​cs.​ou.​edu/​
papers/​ISAIM​2022_​Tishby_​Slonim.​pdf
Stiennon N, Ouyang L, Wu J et al (2020) Learning to summarize with 
human feedback. In: Larochelle H, Ranzato M, Hadsell R et al 
(eds) Advances in neural information processing systems 33: 
annual conference on neural information processing systems 
2020, NeurIPS 2020, December 6–12, 2020, virtual. https://​
proce​edings.​neuri​ps.​cc/​paper/​2020/​hash/​1f898​85d55​6929e​98d3e​
f9b86​448f9​51-​Abstr​act.​html
Tao Y, Viberg O, Baker RS et al (2024) Cultural bias and cultural 
alignment of large language models. PNAS Nexus 3(9):pgae346. 
https://​doi.​org/​10.​1093/​pnasn​exus/​pgae3​46
Touvron H, Lavril T, Izacard G et al (2023) Llama: open and efficient 
foundation language models. CoRR. arXiv:​2302.​13971. https://​
doi.​org/​10.​48550/​ARXIV.​2302.​13971
Trager J, Ziabari AS, Davani AM et al (2022) The moral foundations 
reddit corpus. CoRR. arXiv:​2208.​05545. https://​doi.​org/​10.​
48550/​ARXIV.​2208.​05545
Vaswani A, Shazeer N, Parmar N et al (2017) Attention is all you need. 
In: Guyon I, von Luxburg U, Bengio S et al (eds) Advances in 
neural information processing systems 30: annual conference 
on neural information processing systems 2017, December 
4–9, 2017, Long Beach, CA, USA, pp 5998–6008. https://​proce​
edings.​neuri​ps.​cc/​paper/​2017/​hash/​3f5ee​24354​7dee9​1fbd0​53c1c​
4a845​aa-​Abstr​act.​html
Wachsmuth H, Naderi N, Hou Y et al (2017) Computational argu-
mentation quality assessment in natural language. In: Lapata M, 
Blunsom P, Koller A (eds) Proceedings of the 15th conference of 
the european chapter of the Association for Computational Lin-
guistics, EACL 2017, Valencia, Spain, April 3–7, 2017, volume 
1: long papers. Association for Computational Linguistics, pp 
176–187. https://​doi.​org/​10.​18653/​v1/​e17-​1017
Wang Y, Zhong W, Li L et al (2023) Aligning large language models 
with human: a survey. CoRR. arXiv:​2307.​12966. https://​doi.​org/​
10.​48550/​ARXIV.​2307.​12966
Wang Y, Lu E, Ruan Z et al (2024) Stream: social data and knowledge 
collective intelligence platform for training ethical ai models. AI 
Soc 40(1):145–153. https://​doi.​org/​10.​1007/​s00146-​023-​01851-6
Weber R, Mangus JM, Huskey R et al (2021) Extracting latent moral 
information from text narratives: relevance, challenges, and solu-
tions. In: Computational methods for communication science. 
Routledge, pp 39–59. https://​doi.​org/​10.​1080/​19312​458.​2018.​
14476​56
Xie JY, Hirst G, Xu Y (2020) Contextualized moral inference. CoRR. 
arXiv:​2008.​10762. https://​doi.​org/​10.​48550/​arXiv.​2008.​10762
Zhang S, Roller S, Goyal N et al (2022) OPT: open pre-trained trans-
former language models. CoRR. arXiv:​2205.​01068. https://​doi.​
org/​10.​48550/​ARXIV.​2205.​01068
Zhang Y, Wu J, Yu F et al (2023) Moral judgments of human vs. AI 
agents in moral dilemmas. Behav Sci 13(2):181. https://​doi.​org/​

--- Page 26 ---

4998
	
AI & SOCIETY (2025) 40:4973–4998
10.​3390/​bs130​20181. https://​www.​mdpi.​com/​2076-​328X/​13/2/​
181
Ziems C, Yu JA, Wang Y et al (2022) The moral integrity corpus: a 
benchmark for ethical dialogue systems. In: Muresan S, Nakov 
P, Villavicencio A (eds) Proceedings of the 60th annual meet-
ing of the Association for Computational Linguistics (volume 
1: long papers), ACL 2022, Dublin, Ireland, May 22–27, 2022. 
Association for Computational Linguistics, pp 3755–3773. 
https://​doi.​org/​10.​18653/​v1/​2022.​acl-​long.​261
Publisher's Note  Springer Nature remains neutral with regard to 
jurisdictional claims in published maps and institutional affiliations.

```
