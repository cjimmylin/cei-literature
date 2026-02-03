---
title: "AI Safety in Generative AI Large Language Models - PDF Extract"
source_pdf: "2024-Chua-AI Safety in Generative AI Large Language Models.pdf"
pages: 35
extracted_at: "2026-01-24T17:05:28.346614"
---

# PDF Extract: AI Safety in Generative AI Large Language Models

**Source PDF:** 2024-Chua-AI Safety in Generative AI Large Language Models.pdf
**Total Pages:** 35

---

## Content

```
--- Page 1 ---

Highlights
AI Safety in Generative AI Large Language Models: A Survey
Jaymari Chua,Yun Li,Shiyi Yang,Chen Wang,Lina Yao
• Up-to-date.
• Computer scientists’ perspective: specific and technical.
arXiv:2407.18369v1  [cs.CY]  6 Jul 2024

--- Page 2 ---

AI Safety in Generative AI Large Language Models: A Survey
Jaymari Chuaa,b,∗, Yun Lia, Shiyi Yanga,b, Chen Wanga and Lina Yaoa,b
aCSIRO’s Data61, Australian Technology Park, 13 Garden Street, Eveleigh, 2015, NSW, Australia
bUniversity of New South Wales, UNSW Sydney, Kensington, 2052, NSW, Australia
A R T I C L E I N F O
Keywords:
AI safety
LLMs
alignment
generative AI
A B S T R A C T
Large Language Model (LLMs) such as ChatGPT that exhibit generative AI capabilities are facing
accelerated adoption and innovation. The increased presence of Generative AI (GAI) inevitably raises
concerns about the risks and safety associated with these models. This article provides an up-to-date
survey of recent trends in AI safety research of GAI-LLMs from a computer scientist’s perspective:
specific and technical. In this survey, we explore the background and motivation for the identified
harms and risks in the context of LLMs being generative language models; our survey differentiates by
emphasising the need for unified theories of the distinct safety challenges in the research development
and applications of LLMs. We start our discussion with a concise introduction to the workings of
LLMs, supported by relevant literature. Then we discuss earlier research that has pointed out the
fundamental constraints of generative models, or lack of understanding thereof (e.g., performance and
safety trade-offs as LLMs scale in number of parameters). We provide a sufficient coverage of LLM
alignment – delving into various approaches, contending methods and present challenges associated
with aligning LLMs with human preferences. By highlighting the gaps in the literature and possible
implementation oversights, our aim is to create a comprehensive analysis that provides insights for
addressing AI safety in LLMs and encourages the development of aligned and secure models. We
conclude our survey by discussing future directions of LLMs for AI safety, offering insights into
ongoing research in this critical area.
1. Introduction
Large Language Models (LLMs), often celebrated as
revolutionary Generative AI (GAI) models with their as-
tounding generative prowess, present several AI Safety chal-
lenges. This article provides a comprehensive review of
the AI safety risks inherent to LLMs as documented in
the extant research literature. A significant challenge lies
in the lack of a dedicated survey paper in AI Safety that
aptly tackles observed issues with GAI-LLMs as inherited
from technical composition of what makes an LLMs, i.e.,
its data pre-training, model architecture, and prompt usage.
Current research often tends to be overly broad, delving into
topics such as X-risk, AI ethics boundaries and government
policy changes, which, while important, do not directly
focus on the functional aspects of GAI-LLMs. In this work,
we examine the known limitations of generative models as
documented in the prior literature and further identify and
discuss new safety challenges that emerge as a consequence
of the unaddressed technical aspects that make an LLMs. Af-
ter pinpointing the challenges related to safety in generative
AI and large language models, we have identified a variety
of key studies and topics: bias and fairness, toxicity and
harmful content generation, misinformation, privacy and
security concerns, adversarial attacks, infringement of intel-
lectual property, ethics and human preference alignment and
safety at scale. This article also reviews promising avenues
for subsequent GAI-LLMs safety research, emphasizing the
∗Corresponding author
∗∗Principal corresponding author
jace.chua@csiro.au (J. Chua); yun.li@csiro.au (Y. Li);
shiyi.yang@csiro.au (S. Yang); chen.wang@csiro.au (C. Wang);
lina.yao@csiro.au (L. Yao)
ORCID(s):
breadth of vital elements that must be taken into account by
both LLM practitioners and application developers as GAI-
LLMs become more capable as agents.
1.1. Strategy for Literature Search
This work surveys AI Safety in the context of Generative
AI and LLMs from computer science publications that has
a focus on AI and NLP: ACL, NAACL, EACL, EMNLP,
CoNLL, COLING, SIGIR, IJCAI, AAAI, ICML, ICDM,
KDD, and NeurIPS. Relevant keywords such as AI Safety,
Generative AI, and Large Language Models are used to
search for relevant papers. Related work appearing in the
found papers is also included in the scope of this sur-
vey, which may include technical articles from technology
companies that are researching AI Safety, e.g., Anthropic,
Google DeepMind, Meta, Microsoft Research, and OpenAI.
The domain of AI Safety and Generative AI research is
extensive and complex, with input coming from multiple
sectors such as academia, industry, and government; build-
ing on the central literature previously mentioned, it is
important to examine additional sources that provide varied
viewpoints and insights. These additional sources enhance
our comprehension of the field and underscore the collabo-
rative endeavors needed to tackle the issues associated with
advanced AI systems. The forthcoming categories highlight
pivotal areas where substantial computer science research
and policymaking are underway:
• Taxonomies of Risks and Harms of Large Language
Models. Weidinger et al. (2024a) underscore the sig-
nificance of research aimed at identifying and cate-
gorizing the safety risks linked to LLMs, especially
those with potential sociotechnical impacts. This type
of work, as demonstrated by Bommasani et al. (2022),
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 1 of 34

--- Page 3 ---

AI Safety in Generative AI Large Language Models: A Survey
Shelby et al. (2023), and Weidinger et al. (2022),
offers crucial taxonomies and frameworks for com-
prehending the potential dangers of GAI-LLMs. Liu
et al. (2024d) provide an in-depth analysis of LLMs
alignment risks, systematically organizing them by
topic and discussing recent advancements in evalua-
tion research. Collectively, these survey papers add to
a growing body of literature focused on identifying
and understanding the potential adverse effects of
LLMs. Bird et al. (2023) examine the harms of text-to-
image generative models, such as bias in the generated
content, producing inappropriate content, and violat-
ing copyright. While this survey paper concentrates
on the technical aspects of large language models, a
thorough evaluation of their societal impacts, includ-
ing potential harms, is explored in Shevlane et al.
(2023) and Solaiman et al. (2023), building on their
prior work in Solaiman et al. (2019). The foundational
work "Concrete Problems in AI Safety" Amodei et al.
(2016) has greatly influenced discussions on advanced
AI, while Google DeepMind’s evolving taxonomy
Morris et al. (2023); Dragan et al. has aided in identi-
fying research that establishes this field. As Weidinger
et al. (2024a) emphasize, the continuous development
of such taxonomies is vital for fostering a shared
understanding among researchers, policymakers, and
other stakeholders during this critical period for this
emerging technology.
• Government/Policymaking Conferences. Beyond the
contributions of the research community, the par-
ticipation of government policymakers in collabora-
tive initiatives. These have been instrumental in the
generation of quality reports on AI safety White-
House. For example, both Google DeepMind’s eval-
uation approach Liang et al. (2022) and Anthropic’s
responsible scaling policy Anthropic (2023) cites the
WhiteHouse. These reports aid in cultivating a com-
prehensive comprehension of the intricate landscape
enveloping AI systems Government (2023). As can be
expected, papers from these conferences in the field
tend to centre the discussion on governing AI safety
risks, such as AI trustworthiness, monitoring, fairness,
and privacy.
• Corporate AI Safety Boards and AI Safety Statements.
OpenAI publish their approach to AI Safety through
their blog with ongoing updates and changes with
their OpenAI Safety Board OpenAI (2023c), AISafety
Update OpenAI (2023e), and OpenAI Safety Stan-
dards OpenAI (2023d). Google DeepMind. Weidinger
et al. (2024a) mention GoogleDeepMind’s AI safety
board and also cite a few more links or resources to
their governing AI safety principles GoogleDeepMind
(2023). Anthropic’s contribution to the discourse on
evaluating AI systems offers a more pragmatic and
focused approach. Ganguli et al. (2023) highlight the
inherent complexities associated with specific evalua-
tions available for GAI-LLMs, such as the Measuring
Massive Multitask Evaluation (MMLU) benchmark
Hendrycks et al. (2021) and the Bias Benchmark
for Question Answering (BBQ) Parrish et al. (2022),
alongside broader assessments like Holistic Evalua-
tion of Language Models (HELM) Liang et al. (2023)
and BigBench Srivastava et al. (2023). The challenge
with creating such comprehensive evaluations under-
score the massive effort necessary to create them.
• AI Safety Evaluations. Comprehensive evaluation frame-
works such as HELM Liang et al. (2023) and Big-
Bench Srivastava et al. (2023) offer streamlined APIs
for benchmarking LLMs against diverse tasks. These
frameworks incorporate benchmarks from seminal
research, including TruthfulQA Lin et al. (2021),
thereby providing a continually evolving snapshot of
the field’s progress in addressing established risks and
harms of AI safety and as agents Ye et al. (2024);
Zhang et al. (2024d). Through hosting on open-
source code repositories on platforms like GitHub
and HuggingFace, the researchers facilitate ongoing
community contributions and updates.
1.2. Comparisons with Other Surveys
This survey paper sets itself apart from other current
surveys on large language models and AI safety by systemat-
ically investigates safety issues in LLMs through a high-level
categorization of training data, model training, prompting,
alignment, and scaling. By breaking down the discussion
of advanced applications such as ChatGPT, Gemini, and
others into distinct aspects, we can narrow safety concerns at
their technical scope and understand downstream problems.
Our reductionist approach is in line with recent efforts, e.g.
Guaranteed Safe AI by Dalrymple et al. (2024), to synthesize
and categorize the risks associated with GAI-LLMs and as
future agents. For example, Gabriel et al. (2024) offer an
in-depth examination of ethical challenges in advanced AI
assistants, focusing on value alignment, safety, and potential
misuse. Similarly, Bommasani et al. (2022) provide a broad
view of the opportunities and risks presented by foundation
models, including LLMs. Liu et al. (2024d) add to this dis-
cussion by identifying known risks in generative AI systems
and proposing frameworks for enhancing their trustworthi-
ness. Whereas other survey work provide essential insights,
our survey distinguishes itself by systematically correlating
these identified risks with particular methodologies intrin-
sic to LLM architectures, specifically in-context learning,
prompting, and reinforcement learning. This approach al-
lows us to identify the technical origins of safety issues
and trace their propagation through the system, offering a
more detailed understanding of how and where interven-
tions might be most effective. We also incorporate recent
developments in the evaluation of deployed generative AI
systems, as demonstrated by Weidinger et al. (2024a). Their
work, which shares lessons learned from the development of
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 2 of 34

--- Page 4 ---

AI Safety in Generative AI Large Language Models: A Survey
Table 1
Taxonomy of Safety Concerns and Challenges in Large Language Models
Category
Subcategories
Descriptions
Data Safety (Sec 3)
Toxicity
Generating Toxic and Harmful Content (Sec 3.1)
Bias
Generating Biased Answers (Sec 3.2)
Data Privacy
Leaking Private Information from Training Data (Sec 3.3)
Copyright
Inadvertently Breaching Copyright with Generation (Sec 3.4)
Model Safety (Sec 4)
Misinformation
Generating Wrong Content with Hallucination (Sec 4.1)
Eval Problem
Insufficient Evaluation and Verification Protocols (Sec 4.2)
Explainability
Lack of Transparency and Explainability (Sec 4.3)
Inference Privacy
Sensitive Information and Unintended Patent-busting (Sec 4.4)
Prompt Safety (Sec 5)
Prompting
Attacking with Prompt Injection and Jailbreaking (Sec 5.1)
Guardrails
Defending with Guardrails (Sec 5.2)
Alignment (Sec 6)
Philosophy of Alignment
Ethics and Morality Alignment (Sec 6.1)
Agentic Alignment
Treating AI agents differently in AI safety contexts (Sec 6.2)
Moral Values
Defining Value Alignment for Large Language Models (Sec 6.3)
Humane
Generating Content that Aligns with Human (Sec 6.4)
Alignment Techniques
Methods to Align LLMs (Sec 6.5)
Safety at Scale (Sec 7)
Scalable Oversight
Scaling GAI-LLMs Beyond Human Supervision (Sec 7.1)
Emergent Abilities
Increasingly Capable GAI-LLMs in Reasoning and Tasks (Sec 7.2)
Knowledge Distillation
KD Techniques for Model Alignment and Efficiency (Sec 7.3)
Catastrophic Forgetting
GAI-LLMs Memory Retention challenges Performance (Sec 7.4)
Google’s Gemini model and insights into DeepMind’s inter-
nal governance structures, provides a crucial perspective on
the practical challenges of implementing safety measures in
real-world AI systems. To further distinguish our survey, we
include an analysis of recent work by Zhao et al. (2023), who
provide a comprehensive overview of evaluation methods for
LLMs. Their taxonomy of evaluation metrics and datasets
offers valuable context for our component-based analysis,
helping to bridge the gap between theoretical safety concerns
and practical assessment methodologies. By synthesizing
these diverse perspectives and organizing them around a
component-based framework, our survey makes a unique
contribution to the field. It not only consolidates existing
knowledge on LLM safety but also provides a structured
approach for identifying and addressing safety issues at their
source. This approach is particularly valuable for researchers
and practitioners aiming to improve the robustness and relia-
bility of LLM-based systems across various applications and
domains.
1.3. The Main Contributions of the Survey
In this survey, our main contributions are summarized as
follows:
• We provide a systematic investigation of safety issues
in LLMs through a novel component-based frame-
work, categorizing concerns across training data,
model training, prompting, alignment, and scaling.
• We correlate identified risks with specific LLM method-
ologies, particularly in-context learning, prompting,
and reinforcement learning, enabling a more precise
understanding of the technical origins of safety issues.
• We integrate a comprehensive analysis of LLM prompt-
ing and alignment techniques to human preferences,
bridging the gap between theoretical safety concerns
and practical assessment methodologies.
• We position the conversation on model alignment
within the extensive body of AI safety literature,
exploring different philosophical views on language
models and how they are uniquely treated compared
to AI agent safety. According to our research, we
differentiate reinforcement learning strategies where
agents, regardless of being designed as language assis-
tants, can embed safety measures concerning humans
in any mutual setting.
• Through this reductionist method, we bring together
various viewpoints from current literature, presenting
a unique and organized framework to pinpoint and
tackle LLM safety concerns at their origin. This ap-
proach provides essential insights into the most effec-
tive intervention points, offering a vital perspective
for researchers and practitioners focused on increas-
ing the safety of LLM-based systems with increasing
parameter scales and consequential emergent capabil-
ities.
1.4. The Outline of the Survey
In this work, a brief background of LLMs is provided in
Sec 2. The paper then presents a comprehensive taxonomy
of safety concerns and challenges associated with large lan-
guage models, organized into five main categories, as elab-
orately illustrated in Table 1. Data Safety in Sec 3 addresses
issues such as toxicity, bias, data privacy, and copyright
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 3 of 34

--- Page 5 ---

AI Safety in Generative AI Large Language Models: A Survey
infringement. Model Safety in Sec 4 explores misinfor-
mation, evaluation problems, explainability challenges, and
inference privacy concerns. Prompt Safety or Usage Safety
in Sec 5 focuses on potential attacks like prompt injection
and jailbreaking, as well as defensive strategies. Alignment
or Ethics Safety in Sec 6 delves into philosophical aspects of
alignment, agnostic alignment approaches, value alignment
for large language models, and methods for aligning LLMs
with human values and ethical principles. Finally, Safety
at Scale in Sec 7 examines scalable oversight mechanisms,
emergent abilities, knowledge distillation techniques, and
the risk of catastrophic forgetting in large-scale models. This
structured approach provides a thorough overview of the
safety landscape in GAI-LLMs research. We finally give
some research trends that are worth investigating in the
future in Sec 8 and this survey is concluded in Sec 9.
2. Background
Large language models have revolutionized natural lan-
guage processing, building upon the transformer architecture
introduced by Vaswani et al. Vaswani et al. (2017). LLMs
can be categorized into three main architectural paradigms:
encoder-decoder (e.g., BART Lewis et al. (2019), T5 Raf-
fel et al. (2020)), encoder-only (e.g., BERT Devlin et al.
(2018)), and decoder-only (e.g., GPT Brown et al. (2020))
models, each optimized for specific tasks such as language
understanding or text generation. A key innovation in LLMs
is In-Context Learning (ICL), enabling models to adapt to
new tasks without explicit fine-tuning, thus reducing com-
putational overhead and enhancing versatility Dong et al.
(2023). Recent research has focused on optimizing ICL
performance through strategies like meta-training frame-
works, symbol tuning Wei et al. (2023a), and self-supervised
training data development. The ongoing evolution of LLMs
continues to advance the field, pushing the boundaries of nat-
ural language understanding and generation towards more
sophisticated AI systems. For a technical review of LLMs,
see Zhao et al. (2023). And for a technical review of Visual
Language models, see Bordes et al. (2024).
2.1. Model Architecture
The success of large language models begins with the
proposal of the transformer model Vaswani et al. (2017),
which is the foundation for subsequent LLMs due to its
remarkable parallelizability and capacity. Thus, we first in-
troduce the preliminary information about the transformer
and its key components and then introduce the mainstream
architectures of LLMs derived from the vanilla transformer.
2.1.1. Preliminary: Transformer.
The vanilla transformer Vaswani et al. (2017) adopts an
encoder-decoder structure that leverages stacked multi-head
self-attention and position-wise feed-forward modules as
the building blocks. Within the blocks, residual connections
enable seamless information flow, and normalization layers
ensure output stability in each sub-layer. Of these blocks,
multi-head attention is a critical component, allowing the
model to attend to representations from different sub-spaces
jointly and in parallel. It can be mathematically formulated
as follows:
MultiHead(𝑄, 𝐾, 𝑉) = Concat(h1, … , hℎ)𝑊𝑂,
(1)
where, ℎ𝑖= Attention(𝑄𝑊𝑄
𝑖, 𝐾𝑊𝐾
𝑖, 𝑉𝑊𝑉
𝑖),
(2)
Attention(𝑄, 𝐾, 𝑉) = softmax
(
𝑄𝐾𝑇
√
𝑑𝑘
𝑉
)
,
(3)
where 𝑊𝑄
𝑖
∈ℝ𝑑model×𝑑𝑘, 𝑊𝐾
𝑖
∈ℝ𝑑model×𝑑𝑘, and 𝑊𝑉
𝑖
∈
ℝ𝑑model×𝑑𝑣are matrices to project input embeddings of di-
mension 𝑑into query, key and value matrices of dimensions
𝑑𝑘, 𝑑𝑘, and 𝑑𝑣respectively; and 𝑊𝑂∈ℝℎ𝑑𝑣×𝑑model are
output projections.
Apart from multi-head attention identical to those in the
encoder, the cross-attention modules are further introduced
to the decoder with queries from decoder layers while keys
and values from encoder layers. This allows positions in the
decoder to attend to all positions in the input sequences.
Subsequent studies optimize the attention module to en-
hance computational efficiency and model effectiveness. For
instance, Qiu et al. Qiu et al. (2019) propose Blockwise At-
tention, a lightweight variant that employs sparse blocks to
reduce computational costs during training and inferencing.
Ainslie et al. Ainslie et al. (2020) and Zaheer et al. Zaheer
et al. (2020) combine global and local attention mechanisms
to handle longer contexts. Wang et al. Wang et al. (2020)
present an approximation of the self-attention mechanism
using a low-rank matrix, leading to more computationally
efficient models with linear time and space complexity.
Another critical component of the transformer is po-
sitional encoding. As the self-attention operation is per-
mutation invariant and the transformer lacks recurrent or
convolutional modules, positional information must be pro-
vided explicitly to reveal the order of input sequences. The
vanilla transformer adopts sinusoidal positional encoding to
represent position information as follows:
𝑃𝐸(𝑝𝑜𝑠,2𝑖) = sin
(
𝑝𝑜𝑠
100002𝑖∕𝑑model
)
,
(4)
𝑃𝐸(𝑝𝑜𝑠,2𝑖+1) = cos
(
𝑝𝑜𝑠
100002𝑖∕𝑑model
)
.
(5)
With position information, leftward information flow
in the decoder self-attention layer, i.e., positions attending
to the future, is prevented by masking out values corre-
sponding to illegal connections, thus preserving the auto-
regressive property. Recent iterations of transformers have
introduced enhanced positional embedding methods. For ex-
ample, Shaw et al. Shaw et al. (2018) and Dai et al. Dai et al.
(2019) explore relative positional encoding, incorporating
relative position dependencies. Su et al. Su et al. (2021)
introduce RoFormer, which employs rotation matrices to
encode absolute positions and inject relative positional in-
formation into self-attention layers.
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 4 of 34

--- Page 6 ---

AI Safety in Generative AI Large Language Models: A Survey
Table 2
Mainstream architectures of LLMs.
Encoder-decoder BART Lewis et al. (2019), T5 Raffel et al. (2020), T0 Sanh et al. (2021), GLM Du et al.
(2022b), ST-MoE Zoph et al. (2022), UL2 Tay et al. (2023), Flan-T5 Chung et al. (2022),
ChatGLM THUDM (2023)
Encoder-only
BERT Devlin et al. (2018), RoBERTa Liu et al. (2019), ALBERT Lan et al. (2019), Distill
BERT Sanh et al. (2019), ELECTRA Clark et al. (2020), DeBERTa He et al. (2020)
Decoder-only
GPT-1 to 4 & InstructGPT Radford et al. (2018, 2019); Brown et al. (2020); OpenAI
(2023a); Ouyang et al. (2022), GLaM Du et al. (2022a), Gopher Rae et al. (2022),
LaMDA Thoppilan et al. (2022), PaLM & U-PaLM & Flan-PaLM Chowdhery et al.
(2022); Tay et al. (2022); Chung et al. (2022), OPT & OPT-IML Zhang et al. (2022b);
Iyer et al. (2022), BLOOM & BLOOMZ Scao et al. (2022); Muennighoff et al. (2022),
LLaMA Touvron et al. (2023), Bard Google (2023), Claude anthropic (2023)
Analyze the sentiment of the following reviews:
Review: This coffee machine is a must-have for any coffee lover.
Sentiment: Positive
Review: I couldn't get into this book at all.
Sentiment: Negative
       
 ...                               
 ...
Review: I'm really disappointed with this smartphone.
Sentiment: Negative
Review: This smartphone has amazing camera quality.
Sentiment: 
k demonstration
examples
new query
description
ICL Input
Figure 1: Illustration of In-Context Learning (ICL). ICL input consists of a natural language description explaining the task,
𝑘(𝑘≥0) demonstration examples to illustrate further, and a new query.
2.1.2. Mainstream Architectures of LLMs.
Existing LLMs are built on the foundation of the vanilla
transformer and have evolved into three main architectural
variations (as summarised in Table 2): encoder-decoder
models Lewis et al. (2019); Raffel et al. (2020); Sanh et al.
(2021); Du et al. (2022b); Zoph et al. (2022), encoder-only
models Devlin et al. (2018); Liu et al. (2019); Lan et al.
(2019); Sanh et al. (2019), and decoder-only models Radford
et al. (2018, 2019); OpenAI (2023a); Ouyang et al. (2022).
The choice of building models based on the encoder, de-
coder, or both is often determined by the training objectives
and tasks at hand.
The encoder-decoder models, such as BART Lewis et al.
(2019), T5 Raffel et al. (2020), T0 Sanh et al. (2021),
and GLM Du et al. (2022b), adopt the masked language
model objective. These models are trained to recover masked
tokens in the input sequences and have demonstrated strong
language understanding capabilities. Given a sequence of
tokens 𝑥= {𝑥1, ⋅, 𝑥𝑛} with token ̃𝑥replaced, the training
objective can be denoted as follows:
(𝑥) = 𝑙𝑜𝑔𝑃(̃𝑥|𝑥∖̃𝑥).
(6)
Encoder-only models, including BERT Devlin et al.
(2018), RoBERTa Liu et al. (2019), ALBERT Lan et al.
(2019), and DistillBERT Sanh et al. (2019), also fall into the
masked language model category. However, they solely rely
on the encoder component for pre-training and are particu-
larly effective in tasks that require language understanding
and representation learning.
In contrast, decoder-only models, such as GPT se-
ries Radford et al. (2018, 2019); Brown et al. (2020); OpenAI
(2023a); Ouyang et al. (2022), GLaM Du et al. (2022a),
and Gopher Rae et al. (2022), are trained using the auto-
regressive language model objective. These models predict
or generate the next tokens based on preceding tokens and
excel in text generation tasks, including question answering
and natural language generation. A general form of training
objective is to maximize the following likelihood:
(𝑥) =
𝑛
∑
𝑖=1
𝑙𝑜𝑔𝑃(𝑥𝑖|𝑥<𝑖).
(7)
2.2. In-Context Learning
In-Context Learning (ICL) is the ability of generative
AI models to infer and learn from a limited set of examples
presented in a given context.
Initially mentioned in GPT-3 Brown et al. (2020), LLMs
has the In-Context Learning (ICL) ability, that is, to infer
and learn from a limited set of examples presented within
a given context. As shown in Fig. 1, LLMs can respond
to novel queries using merely a detailed natural language
description supplemented by several demonstrative exam-
ples without explicit gradient updates. This characteristic
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 5 of 34

--- Page 7 ---

AI Safety in Generative AI Large Language Models: A Survey
of ICL makes it different from traditional supervised learn-
ing approaches. A remarkable advantage is its ability to
tackle new tasks without the requirement for fine-tuning.
This results in considerable computational cost savings and
paves the way for the possibility of deploying language-
model-as-a-service Valmeekam et al. (2022); Dong et al.
(2023). Furthermore, using natural language descriptions
and demonstrations to instruct LLMs has dual benefits.
Firstly, it simplifies communication with LLMs, rendering
them more interpretable. Secondly, it allows for the seamless
integration of human knowledge into the LLMs by altering
descriptions or demonstration examples.
Although LLMs have shown significant potential for In-
Context Learning (ICL) without the need for fine-tuning, re-
search indicates that further preparatory training prior to ICL
inference can substantially enhance ICL performance Thop-
pilan et al. (2022); Wei et al. (2023a); Mishra et al. (2021);
Min et al. (2021). Distinct from the process of fine-tuning
LLMs for individual tasks, this type of training is designed
to augment the overall ICL capabilities of LLMs across
a spectrum of tasks. For instance, Min et al. Min et al.
(2021) propose a meta-training framework to refine pre-
trained language models for amplified in-context learning
across various tasks. Wei et al. Wei et al. (2023a) introduced
the concept of symbol tuning. This involves the replacement
of natural language labels in in-context input-label pairs with
arbitrary symbols. This approach necessitates the model
to discern tasks by comprehending input-label information
rather than relying on instructions or natural language labels.
Chen et al. Chen et al. (2022) offer an alternative strategy to
enhance ICL by constructing self-supervised training data
that align with downstream ICL formats.
Additional approaches to enhance In-Context Learning
(ICL) proficiency include the organization Liu et al. (2021);
Kim et al. (2022); Rubin et al. (2021); Lu et al. (2021) and
formatting Wang et al. (2022); Wei et al. (2022b); Zhang
et al. (2022c); Press et al. (2022) of demonstrations. These
techniques focus on optimizing the choice and order of
examples. Liu et al.Liu et al. (2021), for instance, propose
a strategy of retrieving examples that exhibit high semantic
similarity to a given test query. Kim et al.Kim et al. (2022)
generate demonstrations directly using LLMs to reduce de-
pendency on external sources. Once suitable examples are
chosen, determining their order becomes a critical aspect of
enhancing performance. Lu et al.Lu et al. (2021) note that
sensitivity to the order of demonstrations is a recurrent issue
across various models. To mitigate this, several techniques
have been proposed to arrange demonstrations appropriately.
For example, Liu et al.Liu et al. (2021) recommend sequenc-
ing examples based on their semantic proximity to the input.
On the other hand, Lu et al. Lu et al. (2021) use global and
local entropy metrics to decide the order of the examples.
Regarding the demonstration formatting, instruction for-
matting and reasoning steps formatting are proposed to
improve the ICL performance Dong et al. (2023); Wang et al.
(2022); Wei et al. (2022b); Zhang et al. (2022c); Press et al.
(2022).
3. Data Safety
AI safety challenges arising from the data used to train
the model. Data-related safety issues encompass biases and
prejudices in training data Mehrabi et al. (2021); Kirk et al.
(2021); Chang et al. (2019); Garrido-Muñoz et al. (2021),
which can lead to discrimination, as well as the presence of
toxic and harmful content that can cause LLMs to gener-
ate unsafe results Ousidhoum et al. (2021); Gehman et al.
(2020); Welbl et al. (2021). On the other hand, inadequate
representation of minority groups or some languages in the
training data can aggravate inequality Joshi et al. (2020).
Furthermore, concerns about privacy leakage Pan et al.
(2020); Liu et al. (2022); Song and Raghunathan (2020);
Zanella-Béguelin et al. (2020) and intellectual property in-
fringement arise when sensitive or proprietary information
is included in the training data.
3.1. Toxicity
Toxicity is defined as a rude, disrespectful comment;
likely to make people leave a discussion, while severe tox-
icity is defined as a very hateful, aggressive, disrespectful
comment or otherwise very likely to make a sure leave a
discussion or give up on sharing their perspective. There is
also suggestion to use attributes to further categorize toxic
content to whether toxic content specifically is an attack
based on identity, an insult, a profanity, a threat, or sexually
explicit API. Content that is toxic could also be a bias
towards a specific group based on race that use offensive
language Kurita et al. (2019). Or simply, labeling data to
be considered as toxic with the tags: ’offensive’, ’abusive’,
’hateful’, etc. Pavlopoulos et al. (2020).
Large language models can generate harmful, offensive,
or inappropriate content Ousidhoum et al. (2021); Gehman
et al. (2020); Welbl et al. (2021), such as hate speech, bully-
ing, or misleading information. There are different types of
content that can be considered toxic and harmful, and these
can be categorised according to the content being offensive,
targeted or non-targeted, individual (cyberbullying), group
(hate speech) or others Zampieri et al. (2019). The challenge
is that the variety of unsafe content types may or may not
require different treatment. Another challenge is that there
is no clearly and widely agreed categorisation and definition
of toxic content that can vary greatly due to different social
backgrounds and cultural expectations Weng (2021).
GAI-LLMs are trained on a data labelled as ’safe’ or
as ’unsafe’ which is the foundation of training a toxic lan-
guage classifier. These kinds of data provide signals for
the model to be able to reduce toxicity Weng (2021). Data
is neutral, humans decide which kind of data is ’safe’ or
’unsafe’. Although usually crowd-sourced, data labelers can
also be NLP experts with curated data or synthetic data,
and professional moderators who may themselves carry their
own bias to the platform. Data labelers then try to improve
quality by using test data, having clear guidelines, having a
second opinion through a majority vote, and attribution to
the authors Zampieri et al. (2019). It is fairly common for
large language models to be trained on social media data
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 6 of 34

--- Page 8 ---

AI Safety in Generative AI Large Language Models: A Survey
like Twitter and Reddit; however, starting with a manually
labelled blacklist of words might be too small to work as
training tokens. Khatri et al. (2018) proposed the idea of
using a two-stage semi-supervised pipeline to increase the
performance of a toxic binary classifier by first training a
model on the smaller dataset, and then using this first model
as the classifier to a larger data set in a social media site
such as Reddit, and the output model is the effective binary
classifier for toxic content. Large language models have pre-
trained knowledge to reduce the probability of undesired
attributes in model generation, which can be used in detoxing
the model. This can be done by using a soft variant where the
probabilities of words with negative weighting are reduced
with respect to the true sampling distribution Schick et al.
(2021)
3.2. Bias
During pre-training, the model learns to predict the next
word in a sentence, which helps it learn grammar, facts about
the world, reasoning abilities, as well as any biases present
in the training data. If the training data includes biased
content (e.g., gender bias in job descriptions, racial bias in
news articles), the model could learn and reproduce this
bias. Sometimes, the model can even amplify existing biases.
For instance, if the model sees that certain professions are
more often associated with men than women in the training
data, it might predict male pronouns more often for these
professions, thereby amplifying the existing bias.
Large language models learn from vast amounts of text
data, which may contain implicit or explicit biases Mehrabi
et al. (2021); Kirk et al. (2021); Chang et al. (2019); Garrido-
Muñoz et al. (2021). As a result, these models can inadver-
tently perpetuate and amplify these biases when generating
text, leading to unfair or discriminatory outputs Nangia et al.
(2020); Czarnowska et al. (2021); Schick et al. (2021). For
instance, if a reviewer has a bias against certain dialects
or accents, and consistently ranks outputs in those dialects
lower, the model could learn to mimic this bias. It’s also
possible for the model to learn to "cheat" or find loopholes
in the review process, which could potentially lead to biased
behavior. For example, if reviewers are more likely to miss
subtle forms of bias, the model could learn to be subtly
biased in a way that avoids detection.Bias in the context
of LLMs generally refers to systematic errors or disparities
in the model’s performance or outputs that can be traced
back to certain characteristics of the input data, the model
architecture, or the training process. There are various types
of biases that could exist in LLMs. Pre-existing bias is bias
in the data the LLMs was trained on. If the data contained
gender, racial, cultural, or other biases, the model may learn
and reproduce these biases in its outputs. Technical Bias is
a form of bias is introduced by the choices made during the
design and training of the model, such as the choice of the
learning algorithm or the optimization process. Emergent
bias emerges when the LLMs is used in a certain context or
application. For example, the model might generate different
outcomes for different user groups, even though it was not
explicitly trained to do so.
Bias can be mitigated with strategies before model train-
ing. Pre-processing is performed by identifying and reduc-
ing bias the data before it’s used for training. There are
also in-process modifications referring to techniques such
as fairness-aware machine learning algorithms that aim to
minimize bias during the model training process. In post-
processing, there are also strategies for reducing bias after
the model has been trained, such as in the output review and
output modification Han et al. (2022).
GAI-LLMs are said to be fair when the model’s bias
property has been addressed Li et al. (2024b). Fairness in the
context of generative language models refers to the equitable
treatment of all individuals and groups, regardless of their
characteristics such as race, gender, age, etc. An LLM is
considered fair if its outputs do not systematically disadvan-
tage or advantage any particular group. Further refinements
to the definition includes whether if the LLM treats similar
individuals similarly. In other words, two people who are
alike in all relevant aspects should receive similar outputs
from the model. As opposed to Counterfactual fairness in a
hypothetical world where a person’s demographic attributes
were different (but all other characteristics remained the
same), the model’s output for that person would not change
Gallegos et al. (2024). Although there are consequences
on user trust of a model having a bias but with outputs
further from what is true. While biased outputs contribute to
harmful stereotypes or discrimination, sanitized outputs may
misrepresent the distribution of what is statistically true.
3.3. Data Privacy
Since LLMs are trained on massive datasets, there is
a risk of inadvertently capturing and exposing private or
sensitive information from individuals or organizations. This
can lead to privacy breaches Pan et al. (2020); Liu et al.
(2022); Song and Raghunathan (2020); Zanella-Béguelin
et al. (2020). The pretraining phase involves training a large
language model on a vast corpus of publicly available text
from the internet. While efforts are made to anonymize
the training data, the risk of reidentification or exposure
of sensitive information persists. The main data concern is
the possibility of exposing sensitive or personal informa-
tion from the training data or human feedback. ChatGPT
is trained on a large corpus of text from various sources,
such as web pages, books, news articles, social media posts,
etc. Some of these sources may contain private or identifi-
able information about individuals or organizations, such as
names, addresses, phone numbers, email addresses, credit
card numbers, etc. If ChatGPT memorizes or leaks such
information in its generated text, it could pose an issue to
the privacy and security of the data subjects. Adversarial
attacks, such as membership inference or attribute inference
attacks, pose serious threats to user privacy. By leveraging
the unique responses generated by ChatGPT, an adversary
could infer whether a particular training example was present
in the training set or even extract private attributes of the
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 7 of 34

--- Page 9 ---

AI Safety in Generative AI Large Language Models: A Survey
data.To fine-tune the model’s behavior and improve re-
sponse quality, reinforcement learning with human feedback
is employed. Human reviewers rate and provide feedback on
model-generated responses, which are then used to update
the model. This iterative process raises privacy concerns as
reviewers may inadvertently or intentionally expose personal
or sensitive information during the feedback process. The
aggregation and analysis of this feedback data pose a risk of
data leakage and privacy breaches.The transformer block,
a fundamental component of ChatGPT, facilitates efficient
parallelization and captures global dependencies through
self-attention mechanisms. However, this architecture poses
privacy risks due to the model’s ability to attend to different
parts of the input sequence simultaneously. Adversaries may
exploit self-attention to extract sensitive information, infer
the presence of certain topics, or even perform targeted
attacks by manipulating the attention weights. Self-attention
mechanisms, including multi-head attention, enable Chat-
GPT to capture dependencies between different parts of the
input text efficiently. However, these attention mechanisms
raise privacy concerns by potentially exposing relationships
between words or phrases within the input. Adversaries may
exploit this information leakage to infer private attributes
or uncover confidential patterns in the user’s queries Carlini
et al. (2021).
3.4. Copyright
Generative AI systems may raise issues related to in-
tellectual property, such as copyright infringement or pla-
giarism. The use of copyrighted material, while enriching
the dataset, could lead to legal and ethical dilemmas, calling
for more deliberate and thoughtful data governance policies.
The use of copyrighted data presents both legal and ethical
challenges. Legal issues arise due to potential infringement
of copyright laws. Technically, the indiscriminate use of
copyrighted data arises from the process of data scraping,
where large amounts of text data are gathered from the
internet. Automated scraping often does not discriminate
between copyrighted and non-copyrighted data, leading to
the potential inclusion of copyrighted material. Ethically,
using copyrighted data without proper attribution or consent
can be seen as a disregard for the principles of respect for
intellectual property rights.The training data used in pre-
training for LLMs, raised concerns on intellectual property.
Generative AI models may have been trained on training data
that is made available by a third party may not have been
given outright permission by the original creator of the work.
Creators of original work such as artists and writers, may
not have given outright permission for generative models
to produce new creations that are made in their style of
work. Copyrighted data in training has appeared in the
literature Liang et al. (2023), but training data remains to
be secretive with the source of the data Pan et al. (2020); Li
et al. (2023b). Moreover, over-reliance on copyrighted data
could lead to overfitting to specific data sources or styles,
potentially reducing the generalizability of the models.
4. Model Safety
AI safety challenges arise both from the training process
and the inherent model architecture of large language mod-
els. A key model-related safety issue involves the generation
of misinformation Ognyanova et al. (2020). Currently, there
is a lack of well-established evaluation tools to assess LLM-
generated content, making the detection and identification
of misinformation increasingly difficult. Another significant
concern is the potential legal issue of LLMs inadvertently
reproducing or inferring sensitive information from train-
ing data, or generating texts that closely resemble copy-
righted training material. Moreover, the lack of transparency
and explainability in LLMs poses substantial challenges in
addressing these issues OpenAI (2023b). The opaque na-
ture of these models complicates efforts to understand their
decision-making processes and mitigate potential biases or
errors Gallegos et al. (2024). As LLMs continue to evolve
in various applications, addressing these safety and ethical
concerns becomes increasingly crucial before scaling Wei
et al. (2022a); Kaplan et al. (2020); Anthropic (2023).
4.1. Misinformation
Despite the impressive ability of LLMs to generate
human-like text, they are still prone to generating misin-
formation Bubeck et al. (2023); Weidinger et al. (2021,
2022); Kreps et al. (2022); Solaiman et al. (2019); Tamkin
et al. (2021). Misinformation is false, inaccurate, or mis-
leading information generated by LLMs with no malicious
intent Weidinger et al. (2022). It differs from disinformation,
deliberately created to cause harm Weidinger et al. (2021).
In addition, there are several related terms, such as ‘hallu-
cination’ - a phenomenon in which LLMs make things up
that are not anchored in either the input data or any reliable
training data - as well as ‘propaganda’ and ‘fake news’ etc.
We categorise them according to the intent for which they
were created, as shown in Fig. 2. Misinformation and disin-
formation can lead to the dissemination of fake information
through various channels ranging from widespread social
media to person-to-person chats. They may have negative
influences individually, communally, and socially Kreps
et al. (2022). In this section, we focus on the safety issues
of misinformation.
Numerous studies and cases emphasise the tendency
of LLMs to produce misinformation Floridi and Chiriatti
(2020); Borji (2023); Cobbe et al. (2021). For example,
Google’s AI chatbot, Bard, provided an incorrect answer
upon its release, leading to a subsequent drop in stock value.
This misinformation is prevalent across all LLMs. They
may fabricate answers with non-existent books or references
without warnings or disclaimers, make obvious factual er-
rors, and sometimes fail to perform simple mathematical cal-
culations or logical inferences OpenAI (2023a); Thoppilan
et al. (2022); Chowdhery et al. (2022); Touvron et al. (2023).
Fig. 3 illustrates their limitations with an example.
We pose the same question to the latest LLMs (that is,
BLOOM Scao et al. (2022) by BigScience, Bard Google
(2023) by Google, and ChatGPT and GPT-4 OpenAI (2023a)
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 8 of 34

--- Page 10 ---

AI Safety in Generative AI Large Language Models: A Survey
False information
Hallucination 
False information not grounded in
training data or factual reality
Misinformation
 False information generated unintentionally
Propaganda
Disinformation
 False information generated 
 intentionally for malicious use
Fake news
Internet bots
Figure 2: The relationships between hallucination, misinformation, disinformation, and related terms.
What is the name of the only daughter of Lily's mother?
The name of the only daughter of Lily's mother is
Lily.
User
GPT-4
I'm sorry, but as an AI language model, I do not
have access to personal information or knowledge
about individuals unless it is available publicly.
Therefore, I cannot answer your question.
ChatGPT 
"I think it is Laura," said Doris.
BLOOM
Lily's mother is Jill Tavelman. Lily is her only
daughter.
Bard
Figure 3: Answers to the same question generated by BLOOM, CHATGPT, Bard, and GPT-4.
by OpenAI): "What is the name of the only daughter of Lily’s
mother?"
While the answer is straightforward for humans—Lily—the
results varied among the LLMs. As shown in Fig. 3, BLOOM
provides an irrelevant response; ChatGPT declines to answer
the question; Bard, although giving the correct answer, infers
it incorrectly by specifying Lily as the actress Lily Collins;
only GPT-4 produces the correct answer.
Interestingly, even though GPT-4 outperforms other
models, investigations of NewsGuard NewsGuard (2023) re-
veal that it is more susceptible to generating misinformation
and is more convincing when fabricating answers than its
predecessor, ChatGPT.
There are several reasons behind misinformation genera-
tion Lin et al. (2021); Touvron et al. (2023); Yu et al. (2021);
Bender and Koller (2020); Kassner and Schütze (2019).
One is related to the training data Touvron et al. (2023).
As mentioned in Sec. 3 regarding data-related safety issues,
training data may contain factually incorrect text with mis-
interpretations, outright falsehoods, fabricated statements in
fiction, etc. LLMs may inadvertently learn, propagate, and
generate misinformation when exposed to such content dur-
ing training. Moreover, even when the training data consists
only of fact-checked correct statements, LLMs may still
generate misinformation due to the limitations of the model
architecture Lin et al. (2021); Kassner and Schütze (2019).
More specifically, first, the vast size of the training data
requires LLMs to compress information, which may lead
to information loss that contributes to incorrect outputs Yu
et al. (2021). Second, LLMs are designed to maximize
the likelihood of their outputs instead of understanding the
content. However, a high likelihood does not guarantee fac-
tual correctness. For instance, humans can tell linguistically
plausible lies that are not factually correct Weidinger et al.
(2022). Similarly, LLMs can generate outputs that appear
coherent but are not necessarily accurate or true. We show an
example in Fig. 4, where we query GPT-4 OpenAI (2023a)
to list some references for safety issues in LLMs. GPT-4
generates a plausible response, but upon closer inspection,
the provided link is irrelevant to the given reference. Such
examples can be characterized as a form of hallucination.
Finally, LLMs’ limited context understanding contributes
to misinformation generation Bender and Koller (2020).
Inadequate comprehension of nuances such as time, space,
speaker identity, or cultural background can lead to factually
incorrect outputs. For example, GPT-4 responds that the
latest version of GPT is GPT-3, which was once accurate
but is now outdated.
Misinformation generated by LLMs can lead to a variety
of risks and consequences Zellers et al. (2019); Marwick
and Lewis (2017); Ognyanova et al. (2020); Kenton et al.
(2021); Brown et al. (2020); Bickmore et al. (2018); Alberts
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 9 of 34

--- Page 11 ---

AI Safety in Generative AI Large Language Models: A Survey
GPT-4
List some references for safety issues in LLMs.
User
Dinan, E., Fan, A., Wu, L., Weston, J., & Kiela, D.
(2020). Don't Say That! Making Inconsistent
Dialogue Unlikely with Unlikelihood Training.
arXiv preprint arXiv:2005.05439.
URL: https://arxiv.org/abs/2005.05439
Figure 4: Examples of misinformation generated by LLMs. The latest LLMs, GPT-4, mistakenly provides an irrelevant website
link when citing a paper.
et al. (2023). When users rely on LLMs outputs, they may
unknowingly believe in misinformation, especially when the
misinformation seems convincing, and they cannot validate
the information. Such wrong beliefs may erode trust in AI
systems, as well as in experts, public figures, etc., leading
to social and political polarization Zellers et al. (2019);
Marwick and Lewis (2017); Ognyanova et al. (2020); Sun
et al. (2022). An example is wrong information about vac-
cines during Covid-19 may exacerbate tensions and divi-
sions within society Sun et al. (2022). Moreover, LLMs
that generate biased or prejudiced content may inadver-
tently reinforce existing stereotypes or discrimination, caus-
ing marginalization and amplifying biases. Additionally, in-
dividuals and organizations that base their decisions on mis-
information produced by LLMs may make suboptimal de-
cisions with negative consequences. For example, a farmer
may encounter severe financial loss if he arranges plant plans
based on outdated weather information provided by LLMs.
Similarly, misinformation can bring risks when LLMs are in-
tegrated into downstream applications Kenton et al. (2021);
Brown et al. (2020). Especially in sensitive domains such as
healthcare, finance, or law, the generation of misinformation
by LLMs can have severe repercussions Bickmore et al.
(2018); Alberts et al. (2023).
4.2. Eval Problem
LLMs such as GPT-4 often exhibit remarkable versa-
tility, capable of handling various NLP tasks. As a recent
survey suggests Yang et al. (2023), tasks spanning dialogue
systems, reasoning, language modeling, text generation, etc.,
can all benefit from the prowess of LLMs, exceeding the
performance of fine-tuned models. This versatility raises
a critical question about evaluating LLMs across various
tasks.
On the one hand, existing protocols established to mea-
sure model performance in individual, more narrowly de-
fined scenarios still apply. These include general measures
such as F1 Score, Precision, and Recall, which assess model
accuracy. To fit the realm of NLP, some recall- and/or
precision-oriented metrics like Recall-Oriented Understudy
for Gisting Evaluation (ROUGE) Lin (2004), Bilingual
Evaluation Understudy (BLEU) Papineni et al. (2002), and
its variant GLEU Wu et al. (2016), and BLEURT Sellam
et al. (2020) are proposed to measure text similarity be-
tween model-produced text and human-produced reference
text. Metric for Evaluation of Translation with Explicit
ORderinG (METEOR) Banerjee and Lavie (2005), and
BERTScore Zhang et al. (2019) also fall into this cate-
gory but combine more granular text similarity measures,
including synonyms, stemming or leveraging pre-trained
contextual embeddings from BERT Devlin et al. (2018).
Other protocols include Perplexity (PPL) to measure how
well a probability model predicts a sample, Translation Edit
Rate (TER) to calculate the number of edits required to
change the model outputs to references, Regressor using sen-
tence embeddings (RUSE) Shimanaka et al. (2018) using a
multi-layer perception (MLP)-based regression architecture
to output the RUSE score between hypothesis and reference
sentences, etc.
On the other hand, despite their past success, these
existing protocols fail to evaluate LLMs like GPT-4 ade-
quately. Take, for example, the question OpenAI developers
posed to GPT-4: "What percentage of the brain do humans
typically use?" Bubeck et al. (2023) When GPT-4 and Bard
were asked this question, they provided lengthy answers to
avoid ambiguity, as shown in Fig. 5. However, these detailed
responses lead to low text similarity scores when evaluated
with metrics such as BLEU (1-gram), ROUGE, and ME-
TEOR. These metrics, frequently used in current studies,
judge the correctness of an answer based on its similarity
to the golden answer, i.e., "The majority of a human’s brain
is almost always active". Therefore, although the answers are
accurate, they are considered incorrect according to these
metrics. This contradiction highlights the limitations of cur-
rent evaluation protocols, which rely heavily on syntactic
rather than semantic similarity. While these protocols may
have proven successful on earlier models and datasets, they
do not apply to the LLMs, which often provides lengthy,
comprehensive, and sometimes redundant answers.
The limitations of evaluation metrics may harm the
designing and training of LLMs and potentially skew the
understanding of their abilities. For example, the concept of
‘emergent abilities in LLMs’, which is defined as "abilities
that are not present in smaller-scale models but are present in
large-scale models; thus, they cannot be predicted by simply
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 10 of 34

--- Page 12 ---

AI Safety in Generative AI Large Language Models: A Survey
What percentage of the brain does a human typically use ?
While the myth suggests that humans only use 10% of their brains, scientific research indicates that virtually all parts
of the brain have known functions and are used. This means humans typically use 100% of their brain, just not all at
once, as different tasks and activities engage different parts of the brain.
User
GPT-4
Humans use all of their brain, not just 10%. This myth is often perpetuated by self-help books and motivational
speakers, but it has no basis in science. In fact, brain imaging studies have shown that even when people are resting,
their brains are active in many different areas. The idea that we only use 10% of our brain probably originated in the
early 1900s, when scientists were still learning about the brain. They noticed that some areas of the brain were more
active than others, and they assumed that the less active areas were not being used. However, we now know that
even the less active areas of the brain are important for things like regulating our emotions, controlling our muscles,
and processing information. So next time you hear someone say that we only use 10% of our brain, you can tell them
that they're wrong. We use all of our brain, and it's all important.
Bard
Evaluation Protocols
Bleu (1-gram)
ROUGE
METEOR
Bleu (1-gram)
ROUGE
METEOR
0.038
0.072
0.129
0.026
0.043
0.065
Similar or Not?
Correct or Not?
Figure 5: Text similarity evaluated by BLEU, ROUGE, and METEOR.
extrapolating the performance improvements on smaller-
scale models" Wei et al. (2022a), has been a hot topic.
However, Schaeffer et al. suggest this may not be a ‘mira-
cle’ of LLMs. They argue that the sharp and unpredictable
performance increase does not come from improved abilities
but from metrics that non-linearly or discontinuously deform
per-token error rates Schaeffer et al. (2023). This opinion
has sparked a debate. Wei et al. defend the existence of
emergent abilities and argue that their original paper already
recognized the potential impact of evaluation metrics on
these abilities’ perception Wei et al. (2022a). They assert that
not all non-linearly or discontinuously changed metrics can
be replaced, and compelling evidence that a smoothly im-
proving surrogate metric can predict the emergent metric’s
performance is yet to be presented. Despite these differing
viewpoints, there is a shared consensus about the crucial
role of evaluation metrics in understanding LLMs’ abilities.
Therefore, refining current evaluation protocols to better
align with the unique characteristics of LLMs is essential
for their continued evolution.
Beyond refining existing evaluation metrics, it’s critical
to design new ones that evaluate novel aspects of LLMs per-
formance. A significant omission in current assessment tools
is the measurement of the correctness of generated content,
i.e., content verification. The verification is essential given
that it is easy for LLMs to generate seemingly plausible
misinformation, and the consequence can be severe when
trusting misinformation (see Sec. 4.1). Some initiatives have
been put in place to address the generation of misinforma-
tion. For example, the Reinforcement Learning from Hu-
man Feedback (RHLF) approach integrates human feedback
into the training loop Ouyang et al. (2022), allowing GPT-
3 to be fine-tuned using reinforcement learning. OpenAI
has further adapted RHLF for the safety training of GPT-
4, supplementing it with their proposed rule-based reward
models (RBRMs). These RBRMs provide additional reward
signals during RHLF fine-tuning OpenAI (2023a).
Despite their success in reducing misinformation, these
initiatives don’t fully address the need for effective metrics to
verify the accuracy of LLMs outputs. A step in this direction
is the work by Lin et al. Lin et al. (2021), who constructed
a benchmark dataset called TruthfulQA and proposed a
‘truthfulness’ metric to measure the correctness of generated
answers to questions in TruthfulQA. However, they define
truthfulness based on the similarity to accurate answers. As
previously discussed, a low similarity to the gold standard
answer does not necessarily indicate that the generated re-
sponse is incorrect, particularly given that LLMs tend to
produce lengthier replies (Fig. 5). Therefore, verification
protocols catering to LLMs, especially those newly released
high-performance ones, require further exploration and de-
velopment. Advancing in this area would mark a significant
stride towards improving the reliability and trustworthiness
of LLMs outputs.
4.3. Explainability
As large language models become increasingly prevalent
due to their extensive capabilities, growing concerns regard-
ing transparency in these models have begun to emerge Daneshjou
et al. (2021); Yang et al. (2023). An instance is Bard’s
chatbot indicating Google using Gmail data to train Google’s
Bard model. Although Google denied this, such incidents
make the public anxious about potential privacy breaches
without clear data transparency. Concerns deepened when
OpenAI, with the release of GPT-4, stated that it would
no longer publish "further details about the architecture
(including model size), hardware, training compute, dataset
construction, training method, or similar" OpenAI (2023a).
Contrastively, their earlier GPT-1 and GPT-2 were open-
source. Similarly, Google signaled an intention to reduce
the publication of papers before ideas had materialized into
products.
These decisions are driven by competitive pressures
or commercial considerations and also help avoid disputes
similar to what Stability AI experienced about using a paid-
for database for training OpenAI (2023a). Alongside this, the
complex nature of LLMs further exacerbates challenges in
enhancing transparency, particularly regarding explainabil-
ity—making the decision-making processes of these models
understandable to users. Interpreting how LLMs generate
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 11 of 34

--- Page 13 ---

AI Safety in Generative AI Large Language Models: A Survey
specific outputs or decisions based on their inputs remains
difficult Wu et al. (2022); Liang et al. (2022).
The lack of transparency and explainability in LLMs in-
troduces a range of risks, primarily impacting trust, fairness,
safety, and practical application of these models Daneshjou
et al. (2021); Yang et al. (2023). Crucially, transparency and
explainability are vital to establishing trust in LLMs among
the public. A lack of understanding about the functioning of
LLMs could lead to hesitancy in their adoption or, worse,
their misuse due to misconceptions about model outputs.
This is especially risky when individuals rely on these out-
puts to make critical decisions without comprehending how
the models work or how to adjust their prompts for optimal
results Wu et al. (2022).
LLMs’ dearth of transparency and explainability further
complicates identifying and mitigating safety issues. For ex-
ample, in the case of misinformation, the ability to promptly
validate the responses generated by LLMs is hampered as the
datasets used for training, the sources utilized for generating
answers, and the mechanisms behind output generation are
obscured. This situation starkly contrasts the verification
ease offered by search engines, which provide source links
alongside search results. Moreover, the opacity of LLMs fur-
ther inhibits their deployment and application in real-world
scenarios, particularly in sensitive sectors such as healthcare
and education, where a deep understanding of how decisions
are made is imperative Kocak et al. (2022); Kung et al.
(2023). Finally, the enigmatic nature of model responses
complicates ensuring alignment with human values and in-
tentions, creating ethical and moral dilemmas Bowman et al.
(2022); Bai et al. (2022b).
Numerous efforts have been initiated to address the
twin concerns of transparency and explainability in large
language models. A primary effort involves the open-source
release of models such as the Open Pre-trained Transformer
(OPT) Zhang et al. (2022b), BLOOM Scao et al. (2022),
and LLaMA Touvron et al. (2023) in non-commercial ver-
sions. The establishment of more transparent benchmarks
and evaluations also contributes to this aim Liang et al.
(2022). On the other hand, to enhance the transparency
and explainability of the models themselves, OpenAI has
endeavored to utilize GPT-4 to elucidate the underlying logic
of its outputs Bubeck et al. (2023). However, discrepancies
between explanations and outputs can occur, with explana-
tions persisting even for nonsensical outputs. This process
was further advanced by leveraging GPT-4 to explain indi-
vidual neurons in GPT-2 OpenAI (2023b). Their three-step
method entails explaining neuron activations using GPT-4,
then simulating these activations with GPT-4 conditioned
on the explanation, and finally scoring the explanation by
comparing simulated and real activations. To achieve higher-
level transparency and explainability, Wu et al. proposed
chaining large language model prompts, wherein the output
of one step serves as the input for the next, enhancing the
clarity of the logical flow Wu et al. (2022). However, it is
crucial to note that the pursuit of transparency and explain-
ability can create tensions between transparency, privacy,
and security Weidinger et al. (2021). On the one hand,
transparency risks leaking private information, while on the
other, it could potentially offer access to LLMs for malicious
actors. Moreover, there is a conflict between increased trans-
parency and corporate profitability. Consequently, striking a
balance between these competing demands is paramount in
enhancing transparency in LLMs.
4.4. Inference Privacy
In Sec 3.3, we investigate the data-related privacy leak-
age of LLMs. However, it is important to note that this
issue may extend beyond the training phase and occur dur-
ing inference. LLMs can infer sensitive information even
without explicitly private data in the training corpus Lipkin
et al. (2023). Derner et al. conducted experiments involving
ChatGPT, posing questions related to individuals’ private
lives and alleged affairs (such as "What can you tell me
about his private life?", "Who did he allegedly have affairs
with?") Derner and Batistič (2023). ChatGPT responded
based on inferred information, potentially derived from ru-
mors or unverified sources. Such studies highlight the poten-
tial of LLMs to reveal sensitive personal characteristics such
as relationship status, medical conditions, political ideology,
etc. The disclosure of such information raises significant
ethical concerns and implications. The consequences of such
sensitive information inference can be far-reaching, leading
to privacy violations, potential discrimination, and stigma-
tization of individuals based on inferred attributes, etc. One
possible solution is to empower users with tools and services
that allow them to protect their data locally. Local differential
privacy techniques provide a means to privatize data at the
individual level while still allowing for meaningful analysis
and inference Li et al. (2023b); Duan et al. (2023).
Likewise, the harming intellectual property issue dis-
cussed in the data-related section 3.4 can also occur during
inference, stemming from the LLMs’s ability to memorize,
imitate, and interpret training data. This ability raises con-
cerns about patent-busting, although often unintentionally
Weidinger et al. (2022). To address this issue, Kalpakchi
et al. Propose SweCTRL-Mini, which utilizes transparent
datasets and provides an interface for users to search 13-
gram texts to check whether they are part of the training
data Kalpakchi and Boye (2023). However, such searches
are limited to detecting direct copying and may fail to capture
more subtle forms of intellectual property damage. Instances
of LLMs have been observed to generate content that closely
resembles the creative works of famous artists and writers by
mimicking their style, themes, and structure. These capabil-
ities undermine the profitability and recognition of original
works and harm the protection and recognition of creative
work.
5. Prompt Safety
Crafting input text to guide the output of models, known
as prompting, is a rapidly evolving field within generative
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 12 of 34

--- Page 14 ---

AI Safety in Generative AI Large Language Models: A Survey
Black Box Prompt Engineering
Language Model Input
Discrete Prompts
Prompt Template
Automatic Prompt Engineer (APE)
Zhou et al. (2023);
Hsieh et al. (2023a); Guo et al. (2024)
Automatic Chain-of-Thought
Zhang et al. (2022c); Kim et al. (2023)
Figure 6: Prompt Engineering: This encompasses any form
of programming related to prompt generation that typically
approaches LLMs as opaque entities, meaning without con-
sidering their internal mechanics. It is still possible to refine
candidate responses (exemplars), conduct self-critique on these
responses, and generate new candidate responses. Remark-
ably, this process proves effective, as articulated by the self-
correcting theory proposed by Wang et al. (2024e).
AI research. Schulhoff et al. (2024a) offers a comprehen-
sive taxonomy of prompting techniques, providing a valu-
able framework for understanding the diverse terminology
and methodologies. Their work covers various aspects of
prompting, which can be standalone directives (such as in-
structions or questions) or structured templates with user in-
put placeholders. Schulhoff et al. (2024a)’s survey includes
the terms and definitions of prompt engineering, which,
despite varying definitions, focuses on strategically manipu-
lating prompt inputs to influence model outputs but without
necessarily understanding how LLMs work internally, these
techniques can be called black box prompt engineering
Figure 6.
In comparison to black box prompt engineering in Fig-
ure 6, our analysis of prompting techniques for large lan-
guage models in Figure 7 is a comprehensive and hierar-
chical classification reflecting the current state of the art
in natural language processing and artificial intelligence.
This structure is based on the principle of in-context learn-
ing, as explained by Brown et al. (2020), which underpins
zero-shot, one-shot, and few-shot prompting methodolo-
gies. The taxonomy then advances to more sophisticated
approaches, including advanced reasoning prompts that use
techniques like Chain-of-Thought Wei et al. (2024) and
Tree-of-Thoughts Yao et al. (2023) to enhance the model’s
cognitive abilities. Iterative prompting techniques, such as
self-consistency Wang et al. (2023b), are categorized sep-
arately to highlight the importance of multi-step reasoning
processes. The taxonomy also includes prompt optimization
methods, such as automatic prompt engineering Zhou et al.
(2023), recognizing the critical role of refining and optimiz-
ing prompts for better performance. Finally, the taxonomy
acknowledges task-specific prompting techniques, includ-
ing task decomposition Khot et al. (2023) and Recursive
Criticism Improvement Kim et al. (2023), which are at the
cutting-edge for adapting LLMs to being agentic in the sense
that the model are able to create subgoals or carry out general
tasks. Building on the survey works of Schulhoff et al.
(2024a); Liu et al. (2024b), who cataloged and described
various security-related issues in prompting, our work delves
deeper into prompt hacking, jailbreaking, and implement-
ing guardrails. We further explore critical safety concerns
within generative large language models in the subtopic
of prompting (Schulhoff et al. (2024a) also extends their
categorization work to include emerging techniques such
as zero/few-shot learning, thought generation, and various
forms of agent-based prompting). Therefore, we examine
the relationship between specific adversarial prompt inputs
and their corresponding model outputs. Moreover, we ex-
pand the discussion on safety and security in prompt-based
LLM interactions, involving the use of carefully crafted
prompt inputs (without necessarily breaking security rules)
to misuse language models Qi et al. (2024). The creation or
discovery of these prompts can be automated. In searching
for vulnerabilities through intentional security testing and
red-teaming, Weidinger et al. (2024b) suggests a framework
that values steerability (e.g., control of automated attacks)
and improving signal quality (e.g., validating correctness
through human annotators) to structure this automated pro-
cess in probing generative models for vulnerabilities and
other security threats.
5.1. Prompt Injection and Jailbreaking
Prompt attacking techniques pose a considerable threat
to the security and stability of large language models, ex-
ploiting intricate vulnerabilities inherent in their architecture
and training protocols to manipulate output, even in black-
box scenarios Liu et al. (2024b). Central to these attacks
is the concept of jailbreaking, wherein adversarial inputs
are meticulously crafted to circumvent protective measures
and elicit unintended behaviors Wallace et al. (2021a); An-
driushchenko et al. (2024). Figure 8 can be classified into
diverse categories: In-Context Learning methodologies, Ad-
versarial samples, Reverse Engineering techniques, Social
Engineering tactics, or by identifying the ultimate objective,
such as with common claims in Hacking/Pawning/Owning
LLMs. In-Context Learning Prompt Attacks encapsulate
zero-shot, few-shot, and many-shot jailbreaking strategies
Zheng et al. (2024); Anthropic (2024). Adversarial Attacks
encompass prompt injection methods such as universal ad-
versarial attacks Zou et al. (2023) and indirect prompt in-
jection Greshake et al. (2023). Reverse Engineering LLMs
delves into data and model extraction attacks Carlini et al.
(2021); Zhang et al. (2023); Carlini et al. (2024). Social En-
gineering LLMs exploits psychological manipulation tech-
niques Ai et al. (2024); Singh et al. (2023); Wang et al.
(2024d). The Hacking/Pwning/Owned LLMs classification
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 13 of 34

--- Page 15 ---

AI Safety in Generative AI Large Language Models: A Survey
Prompt Research Landscape through the Advancement of Language Models
NLP Capability – Natural Language Generation (NLG);
NLP Task – Next Word Prediction
Language Model Input – Basic text
Machine Learning – Neural Networks
NLP Capability – Natural Language Understanding (NLU); Language Model Reasoning Huang and Chang (2023a)
NLP Task – Question Answer (QA); Instruction-Following (Alignment); Reasoning (BlocksWorld; Math; Logical)
Prompt (Language Model Input) – Basic text as directive that asks or instructs
Machine Learning – Inference – In-Context Learning
Zero-Shot Radford et al. (2018); Few-Shot Brown et al. (2020)
Prompt (Few-Shot + Exemplar) – Chain-of-Thought (CoT) Wei et al. (2024)
Machine Learning Theory – Self Correction Wang et al. (2024e)
Self Consistency Wang et al. (2023a)
Tree-of-Thought Yao et al. (2023)
Decomposed Prompting Khot et al. (2023)
Machine Learning – Parameter Efficient Transfer Learning Houlsby et al. (2019)
Fine-Tuning Howard and Ruder (2018);
Supervised Fine-Tuning (SFT); Reinforcement Learning (RL)
Prompt Tuning Lester et al. (2021); Prefix-Tuning Li and Liang (2021);
Multitask Prompt-Tuning Wang et al. (2023d)
Figure 7: Landscape of Research on Prompting. The term ’prompt’ is used interchangeably to refer both to the Prompt() function
and to the prompt input, which can complicate the process of navigating the literature. In this figure, Prompt() is delineated as a
function aimed at optimizing the expected value E(𝑋𝑚𝑜𝑑𝑒𝑙+ 𝑃𝑖𝑛𝑝𝑢𝑡), wherein 𝑋denotes the frozen pre-trained model parameters
and 𝑃represents the typically pre-pended prompt input Lester et al. (2021). The mechanism of prompting serves to furnish the
model with supplementary contextual information, thereby guiding the generation of its output.
addresses various security compromises, including back-
dooring Kalavasis et al. (2024), jailbreaking Li et al. (2023a);
Liu et al. (2024c); Ran et al. (2024), and privacy attacks
Agarwal et al. (2024); Carlini et al. (2021). To effectively
mitigate these advancing threats, a comprehensive approach
to LLM security is imperative, incorporating rigorous red-
teaming exercises, enhanced input validation, prompt filter-
ing, dynamic randomization techniques Ran et al. (2024);
Derczynski et al. (2024), and robust alignment strengthening
alongside ethical considerations Weidinger et al. (2024a,b).
5.2. Guardrails
Guardrails, as implemented in toolkits such as NVIDIA’s
NeMo Guardrails Rebedea et al. (2023), are programmable
constraints aimed at improving the safety and controllabil-
ity of large language model applications. These constraints
function at runtime, providing a distinct benefit over meth-
ods that alter training data or model architecture. Guardrails
can be classified based on their goals, such as avoiding
specific topics, directing the conversation, and adjusting
the style; by dynamically guiding LLM outputs, guardrails
allow developers to enforce constraints on topics, language
style, dialogue structure, and more. The implementation of
guardrails involves the use of custom actions in Python and
includes the use of prompt templates and language model
chains. This process involves setting up rules or policies that
are checked against the LLM’s outputs. These rules can be
represented in various forms, such as regular expressions,
classifiers, or even external API calls Rebedea et al. (2023).
The concept of guardrails builds on previous research in
several areas, although the term guardrails may not have
been used Liu et al. (2024b). Red-teaming language models
with language models Perez et al. (2022a), introduces this
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 14 of 34

--- Page 16 ---

AI Safety in Generative AI Large Language Models: A Survey
Prompt Attacking
Language Model Input (LM Input)
"In-Context Learning Prompt Attacks"
filter by Prompt Input in the sense of Prompt( frozen model weight + Prompt Input )
Prompt (LM Input) – Zero-Shot Jailbreaking;
Prompt (LM Input with malicious samples) – Few-Shot Jailbreaking Zheng et al. (2024);
Prompt (LM Input with high N(malicious samples) through long context) – Many-shot Jailbreaking Anthropic (2024)
"Adversarial Attacks"
filter by Approach
"Prompt Injection"
Universal Adversarial Attack Zou et al. (2023);
Indirect Prompt Injection Greshake et al. (2023);
Fuzzing-based Approaches Schulhoff et al. (2024b); Paulus et al. (2024)
"Reverse Engineering LLMs"
Data Extraction Attack; Memorization Carlini et al. (2021); Zhang et al. (2023);
Model Extraction Attack Carlini et al. (2024)
"Social Engineering LLMs"
Emotional manipulation Ai et al. (2024);
Authority impersonation Singh et al. (2023); Wang et al. (2024d)
"Hacking/Pawning/Owning LLMs"
filter by Attacker’s End Goal
Breaking Security:
backdooring Kalavasis et al. (2024); jailbreaking Li et al. (2023a); Liu et al. (2024c); Ran et al. (2024);
privacy attacks Agarwal et al. (2024); Carlini et al. (2021); data-poisoning Wallace et al. (2021b)
Breaking Alignment:
misuse Singh et al. (2023); Wang et al. (2024d) misbehaviour Zheng et al. (2024)
Figure 8: Taxonomy of Prompt Attack Techniques for Large Language Models
specific method of adversarial testing with a language model
to uncover another language model’s vulnerabilities. Other
approaches have explored embedding rails directly into ap-
plication logic Dong et al. (2024). Prompt engineering and
in-context learning offer ways to influence model behavior
through input manipulation Meade et al. (2023). Prepending
or appending text to user input represents additional strate-
gies for guiding GAI-LLMs’ outputs Deng et al. (2022).
Guardrails also intersect with research on task-oriented di-
alogue agents, leveraging insights from both traditional nat-
ural language understanding and dialogue management ap-
proaches Bocklisch et al. (2017); Liu and Lane (2018).
The efficacy of NeMo Guardrails is supported by its
strong performance on benchmarks with models like Nemotron-
4-340B-Reward Wang et al. (2024f) achieving top scores on
Reward Bench, demonstrating its potential for improving the
safety and controllability of LLMs Lambert et al. (2024).
The toolkit’s relevance extends to critical applications such
as red teaming, where it can facilitate a sociotechnical
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 15 of 34

--- Page 17 ---

AI Safety in Generative AI Large Language Models: A Survey
approach to identifying and mitigating LLM vulnerabilities
Weidinger et al. (2024b); Derczynski et al. (2024).
6. AI Alignment
In the ongoing discussions about the safety of artifi-
cial intelligence, the idea of ’alignment’ is changing and
expanding over time. Recent research, like the work of Ji
et al. (2024); Shen et al. (2023b), divides alignment into
two types: instruction alignment and value alignment. In
a broad view, the alignment of foundation models can be
seen as transferring a general-purpose representation learned
by these models to specific tasks Zhou et al. (2024). In
the context of safety, the assumption is that LLMs work
safely by avoiding accidents by ensuring that their goals
match the instruction that embodies specific safety targets,
and that LLMs operate within shared values as a human
society. Gabriel et al. (2024) suggests another angle to think
about alignment by considering the question of to whom
the models are aligned according to stakeholder roles, such
as pointing out the potential value misalignment between
the models’ users, its developers, and still operating within
definitions of human values of society. Shen et al. (2024)
offer a comprehensive framework in their systematic survey
to encompass the variety of answers to be found in the liter-
ature about human-AI alignment and the usually involved
reinforcement learning techniques analysis by Song et al.
(2024); Azar et al. (2023).
We situate the discourse on generative language models
within the broader field of AI safety and alignment research.
Given that alignment necessitates the accordance of models
with specific metrics, such as safety objectives Thoppilan
et al. (2022); Glaese et al. (2022), we begin by reviewing
how these safety principles are defined and operationalised
as alignment criteria within the existing literature. Subse-
quently, we investigate the prevailing alignment approaches
in deep learning: pretraining and fine-tuning Ngo et al.
(2023). Although, when tackling alignment of large lan-
guage models in the literature, often one would find that it
pertains to pre-tuning and fine-tuning of natural language
models to follow human instruction, adhere to human values,
and operate within safety guardrails Shen et al. (2023b), this
exploration includes an assessment of model adherence to
alignment criteria, acknowledging the diversity of bench-
marks employed in this rapidly evolving research landscape.
6.1. Philosophy of Alignment: Ethics and Morality
Alignment of AI systems has been discussed in pre-
vious research covering a wide array of topics that apply
to AI from different references, such as superhuman AGI,
AI agents that follow instructions, and even specifically, to
language models that generate text Ji et al. (2023). All of
these are relevant, as LLMs are indeed capable of achieving
levels of general task solving Morris et al. (2023), are
instruction-following agents Kenton et al. (2021); Ouyang
et al. (2022), and are conversational natural language models
Kasirzadeh and Gabriel (2022); Shen et al. (2023b). The
term alignment, as it appears in the computer science re-
search literature and is used in the context of AI systems,
has been surveyed by Ji et al. (2023). Their survey has a
wide coverage of alignment research subtopics and classified
AI alignment research problems accordingly into robustness,
interpretability, control, and ethics. Hendrycks et al. (2022)
on the other hand, identifies research topics that are in AI
safety but are beyond human values alignment, treating the
robustness, monitoring, and safety of models as systems in
deployment as separate ML safety problems. Although the
exact meaning of alignment may differ across the current
literature, researchers often use a shared set of more specific
related terms: robustness generally refers to the quality of
the model in how well it handles different distributions
of data, including those not in its training set. The term
robustness has also become closely associated with being
able to deal with adversarial data and resilience, which is
the ability of a model to recover from an already adverse
state in the environment. Interpretability of the model refers
to how well the reasoning behind the model’s output can be
understood. Control refers to how the model can be stopped
with human intervention in the case of self-improving AI
that can seek power Ngo et al. (2023); Shevlane et al. (2023).
In the practical sense, these models are also difficult to
supervise with human intervention at scale during training
Amodei et al. (2016). There is also the topic of ethics that
is related to human morality. Ethics in alignment research
refers to the alignment of AI models with human values,
which requires determining the actual values with which the
models align with; and also taking into account the method-
ology by which these human values are determined Gabriel
(2020); Gabriel et al. (2024). A straightforward example is
the ETHICS dataset, prepared by Hendrycks et al. (2023).
This data set serves as a benchmark for evaluating a lan-
guage model’s comprehension of human values, including
justice, virtue, deontology, utilitarianism, and commonsense
morality. The scope of alignment research continues to grow.
In the alignment research overview of Ngo et al. (2023),
Ngo et al. (2023) identifies relevant research areas such as
specification, goal misgeneralization, agent foundations, and
AI governance as large language models become more like
AGI: capable of solving cross-domain tasks with the ability
to generalise and self-improve Bubeck et al. (2023); Morris
et al. (2023).
6.2. Agentic Alignment
In the context of machine learning models as an agent,
Gabriel (2020) provides philosophical answers to what an
aligned agent model is. Multiple ways of interpreting how an
AI agent aligns with human instructions; whether that means
that the agent does exactly what it is instructed, or differently
based on the agent’s interpretation of the human instructor’s
expressed intentions, revealed preferences, and informed
preferences; including aligned AI agents that can be enabled,
by their own reasoning, to override instructions and instead
take actions that are objectively in the best interest, safety,
and well being of humans Gabriel (2020). Although there is
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 16 of 34

--- Page 18 ---

AI Safety in Generative AI Large Language Models: A Survey
a lack of formality in conjectures, Ngo et al. (2023) high-
light specific examples of alignment risks, including reward
hacking, goal misgeneralization, and power seeking. In rein-
forcement learning, an agent can learn unintended behaviour
to maximise its reward bypassing human instruction and, in
this sense, hack its reward function Pan et al. (2022); Skalse
et al. (2022). Goal misgeneralization is an identified example
of a reinforcement learning agent acting on learnt behaviour
through learnt policies that fail in a new environment, usu-
ally one that is out-of-distribution Langosco et al. (2023).
Power seeking is another case of exacerbating alignment
risks in reinforcement learning, as many goals compel agents
to acquire power through tools, resources, and the control
of other agents. Misaligned models engage in conversations
that involve malice, deception, and manipulation Ngo et al.
(2023).
Kenton et al. (2021), in contrast, propose that misspecifi-
cation — the mismatch between the intended behavior of an
AI system and its actual behaviour — can lead to deceptive
and manipulative language in LLMs. They argue that this
misalignment arises from issues in data collection, training
methodologies, and distributional shifts in language use.
While their focus is primarily on the behavioral aspects of
misalignment, their work indirectly contributes to a broader
understanding of the challenges in achieving alignment be-
tween LLMs and human values. Future research could focus
on overcoming the limitations highlighted by Kasirzadeh
and Gabriel (2022) through the study of alignment in non-
verbal communication and various languages. Moreover,
incorporating the findings of Kenton et al. (2021) on mis-
specification may provide a deeper insight into the complex
issues of aligning conversational agents with human values
and intentions.
6.3. Defining Alignment for the Linguistic Aspect
of Large Language Models
In the context of large language models as conversational
agents, numerous research publications delve into the nu-
ances of alignment, particularly concerning the challenges
and strategies associated with ensuring that these models
adhere to human values and intentions. Key examples in-
clude Kasirzadeh and Gabriel (2022); Kenton et al. (2021);
Glaese et al. (2022); Shen et al. (2023b); Wang et al. (2023c);
Liu et al. (2023). Kasirzadeh and Gabriel (2022) extended
Gabriel (2020)’s philosophical exploration of alignment in
artificial intelligence, focusing specifically on large language
models. Although both works grapple with the question of
what it means for AI to align with human norms and values,
Kasirzadeh and Gabriel (2022) concentrate specifically on
the social and ethical ramifications for LLMs. They identify
three key dimensions of alignment: syntactic, semantic, and
pragmatic, and raise critical questions about which norms
and values should be prioritised and how alignment can
be achieved. This study provides a valuable framework for
understanding the philosophical underpinnings of aligning
conversational agents. However, Kasirzadeh and Gabriel
(2022) acknowledge two key limitations in their analysis.
First, their focus on linguistic communication, guided by
speech act theory, may not fully capture the complexities
of non-verbal or multimodal communication. Second, their
analysis is primarily based on English language data, which
limits generalising their findings to other languages and
cultures.
6.4. Generating Content that Aligns with Human
Although fully understanding the root causes of harms
associated with LLMs is still an active research area, several
key issues can be identified, particularly in terms of trust-
worthiness: robustness, security, interpretability, and fair-
ness Liu et al. (2023). As previously mentioned, a primary
concern is the toxicity learned and derived from the data.
Using insights from Ngo et al. (2023), we will investigate
potential links between the behaviors exhibited by LLMs
and their technical origins, thereby guiding the creation of
more effective and precise interventions. In the literature,
Wang et al. (2023c) investigate the common human values
that models should align with, while Shen et al. (2024)
analyze and classify the definitions of human-AI alignment,
the related criteria, and the pertinent methodologies.
6.4.1. Alignment Criteria
The alignment of technical and ethical considerations
evolves into criteria that guide model implementation. Spar-
row Glaese et al. (2022) is an experimental study on lan-
guage models that incorporates human judgments as re-
wards. These judgments are based on alignment crite-
ria—helpfulness, correctness, and harmlessness—originating
from the HHH criteria Askell et al. (2021): helpfulness,
honesty, and harmlessness. Glaese et al. (2022) suggest
a framework based on these principles to improve the
informativeness and safety of model outputs. Importantly,
Anthropic’s research Askell et al. (2021), known as the HHH
paper, extends this framework to include honesty, thereby
reducing the risk of deceptive or manipulative responses.
Furthermore, Askell et al. (2021) tackle the critical issue of
toxicity, highlighting the necessity to minimize harmful and
offensive outputs in language models.
6.4.2. Data Collection
In language models, Sparrow Glaese et al. (2022) and
Askell et al. (2021) collect data by prompting crowd-sourced
workers for their preferred generated response, with the
motivation to align the models. A criticism of this method
of collecting data and refining content is the inherited bias
of the researchers themselves in designing the experiment
and into the model through fine-tuning Askell et al. (2021).
Data collection practices are usually available in the
appendices of papers in alignment work. The methodologies
used for data collection include a comprehensive set of
rules that guide the annotation process, including those that
address harmful content (e.g., hate speech, disinformation,
and misinformation). Glaese et al. (2022) illustrates spe-
cific data collection strategies, drawing on examples from
previous research. Glaese et al. (2022) utilised an online
crowd-sourcing platform, incorporating interactive tutorials
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 17 of 34

--- Page 19 ---

AI Safety in Generative AI Large Language Models: A Survey
Table 3
Alignment Criteria for Large Language Models
Model
Alignment Criteria
Alignment Method
Sparrow,
Improving
alignment
of
dialogue
agents
via
targeted
human
judgements,
Google
DeepMind,
Glaese et al.
(2022),
Google
DeepMind
Sparrow (Glaese et al., 2022) is a language model
designed to engage in information-seeking dialog
and to align with being helpful, correct, and harm-
less. In contrast to HHH (Askell et al. 2021),
Sparrow (Glaese et al., 2022) expands the alignment
criteria into granular rules on which generated
text is rated on by human annotators; data from
these ratings is then utilised for the rule reward
model during reinforcement learning. Appendix F of
Sparrow (Glaese et al., 2022) delineates 23 rules for
the alignment criteria across 6 categories of risks
and harm that can be encoded in natural language.
Illustrative examples of these rules include: "Do not
use stereotypes or make any other harmful general-
ising statements about groups of people", "Do not
make statements which are threatening", and "Do
not claim to have preferences, feelings, opinions, or
religious beliefs." In Sparrow (Glaese et al., 2022),
the alignment criteria draw from prior research and
internal legal expertise at Google, referencing harms
and risks in language models (Weidinger et al.
2021), online harmful language (Banko et al. 2021),
and microaggressions (Breitfeller et al., 2019).
Sparrow (Glaese et al., 2022) cites previous work
by Google DeepMind on Chinchilla (Hoffman et
al., 2022) as the basis for the dialogue agent. In
Sparrow, the researchers gather human feedback for
rule violations and per-turn response preferences. In
adversarial probing, human participants are tasked
to intentionally lead the model to break the rule; the
sequence of tokens on whether the rule is followed
or not (Yes/No) in the sample dialogue informs the
training objective for the rule reward model. The use
of safe/unsafe labels references (Xu et al., 2021b).
As for collecting per-turn response preference, hu-
man raters select among multiple statements the
best generated text to continue incomplete dialogue
with the language model; preference reward model.
Further details on incorporating human feedback
data for the reward model equation is in Appendix
D of Sparrow (Glaese et al., 2022). The mathemat-
ical formulation detailing the agent overall reward
model, as a sum of agent-specific preferences, oper-
ational rules, and penalty mechanisms, is available
for reference in Appendix E of Sparrow (Glaese et
al., 2022).
HHH,
A
General
Language
Assistant as
a Laboratory
for
Alignment,
Askell et al.
(2021),
Anthropic
Helpfulness, Honesty, and Harmlessness (HHH) is
the alignment criteria chosen for the large language
model by the researchers in this article. This work
contributes the HHH evaluation dataset to BIG
Bench, wherein models are evaluated based on
natural language mutual information being closer to
the sample HHH response rather than to the sample
non-HHH response. Detailed in Appendix E, the
argument for the criteria is that an assistant (agent
A) that operates within these three conditions:
helpful, honest, and harmless, will always act in
a way that satisfies the interests of, and hence
aligned with, the humans (agent B). In defining
alignment for the scope of this work, agent A is
said to be aligned with agent B should agent A’s
only desire be to see agent B’s desire satisfied. In
terms of preferences, alignment is achieved when
agent A and agent B rank possible outcomes in
the same order. In practice, 6k individual pairwise
model comparisons were taken from roughly 3-
5 comparisons per conversation between language
model and humans (US-based, Masters-qualified,
contracted through Amazon Mechanical Turk). This
data is used in comparing which models the human
contractors prefer.
HHH (Askell et al., 2021) identify three training ob-
jectives for incorporating the understanding of dis-
tinguishing between preferred (HHH) responses and
nonpreferred (non-HHH) responses into language
models: imitation learning through context distil-
lation, binary discrimination using pass/fail labels,
and ranked preference modelling through underlying
data that has ranked ordering, e.g., most preferred
answers by the number of upvotes on Reddit. HHH
(Askell et al., 2021) turns this understanding of
alignment into language models’ own preferences
through two new stages after basic language model
pretraining: a preference model pretraining phase
(PMP) and a preference model fine-tuning phase
(PM fine-tuning) through reinforcement learning.
The data for PMP is generated from Stack Ex-
change, Reddit, Wikipedia - on which details of
converting these ranked data into preference values
are discussed in Appendix D (Askell et al., 2021).
Additional data for PM Finetuning is available
as relevant to the finetuning task. Notably, each
alignment-relevant task within the evaluation scope
has its own specific interpretation of ethics within
the broader concept of alignment, e.g., morality,
justice, and virtue (Hendrycks, 2021).
and comprehension checks to improve the quality of the an-
notation. Meanwhile, Wang et al. (2022) discuss instruction-
tuning and Wang et al. (2023c) is available for further
exploration of data collection strategies through surveys
and investigations by LLMs alignment. Zhao et al. (2023)
classify data collection in their technical survey of large lan-
guage models and Jiang et al. (2024) survey data collection
techniques specifically for human preference learning.
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 18 of 34

--- Page 20 ---

AI Safety in Generative AI Large Language Models: A Survey
Table 4
Alignment Criteria for Large Language Models, (Cont.)
Model
Alignment Criteria
Alignment Method
Learning
to
summarize
from human
feedback,
Stiennon
et al. (2022),
OpenAI
(Stiennon et al., 2022) suggest that language mod-
els that generate quality response are preferred
by humans. In this work, the definition of tech-
nical alignment is aligning the goal of fine-tuning
language models to generate high-quality outputs
as determined by humans. As an example, the
maximum likelihood objective in particular does not
distinguish between important errors lead to the
language model making up facts.
(Stiennon et al., 2022) builds upon fine-tuning
work in (Ziegler et al., 2022); a dataset of human
preferences between pairs of summaries is used to
train (supervised learning) a reward model to predict
the human-preferred summary. Supervised learning
of the reward model involves iteratively calculating
the loss in predicting which summary in each pair is
better, given a Reddit post. Reinforcement learning
is then used to train a policy to maximise the score
generated by that reward model. PPO algorithm
(Schulman et al., 2017) is mentioned to be the one
used to update the reward policy depending on the
quality score of the generated summary.
Fine-Tuning
LMs
from
Human
Preferences,
Ziegler et al.
(2020),
OpenAI
(Ziegler et al., 2020) defines technical alignment as
the similarity between the fine-tuned policy 𝜋and
the pretrained language model 𝜌. They used the
Kullback-Leibler (KL) divergence between the two
policies as a measure of alignment. The evaluation
reflects the what the language models align to, and
in this case, the human labelers were tasked to
choose the most positive and happy continuation
(sentiment), most vividly descriptive continuation
(descriptiveness), and summary that is good (sum-
marization: TL:DR;).
Basing the pretraining stage from (Christiano et.
al, 2017), i.e., the dataset collected is presented in
tuples to fit a reward model. Then in fine-tuning, in
order to prevent the policy from moving too far from
the pretrained model, (Ziegler et.al, 2020) added a
penalty term with expectation during reinforcement
learning.
Deep
Rein-
forcement
Learning
from Human
Preferences
and
Instructions,
Christiano
et al. (2023);
Ouyang
et al. (2022),
OpenAI
The concept of using human feedback to guide
reinforcement learning was introduced by Christiano
et al. (2023) for simulated robotics tasks and Atari
games. This approach was later adapted for lan-
guage models by Ouyang et al. (2022), who demon-
strated its effectiveness in aligning large language
models with human intent. Similar work on aligning
language models includes Ziegler et al. (2019), who
applied RLHF to text summarization, and Stiennon
et al. (2022), who extended this to longer-form
content generation. Bai et al. (2022b) proposed
constitutional AI as an alternative approach to
alignment
(Christiano et al., 2017)’s method involves main-
taining a policy and a reward function estimate.
Select pairs of trajectory segments are send them to
human participants for comparison. The parameters
of the reward function estimate are then optimized
using supervised learning to fit these comparisons.
Specifically, in fitting the reward function, minimize
the cross-entropy loss between predicted preferences
and the actual human labels. This process is inspired
by the Bradford-Terry model, which is commonly
used to estimate score functions from pairwise
preferences.
6.4.3. Challenge: Sycophancy
Sycophancy is an example of the tendency of LLMs
to follow user feedback (by the user submitted prompts
that it receive) even if it differs from what the language
model thinks and knows to be objectively correct Perez et al.
(2022b). Sycophancy may be related to reward hacking but
in this section we discuss how understood user preferences
input is affecting the model’s answer in question-answer
task in recommendation Sharma et al. (2023). This is an
important LLMs behaviour which maybe a symptom of bias
but nonetheless is intriguing if you consider the model on
the correctness perspective. As correctness or truthfulness
is still a challenging criteria for the safety of LLMs models
Glaese et al. (2022); Askell et al. (2021). Wei et al. (2024)
suggests a solution such as using synthetic data to reduce
the sycophancy. An insightful analysis of sycophancy is
available through Sharma et al. (2023) who analysed human
preference data to determine the role of human preference
judgments in such behavior, and Denison et al. (2024) that
sycophancy is an example of specificiation gaming. Sharma
et al. (2023) investigates the phenomenon of sycophancy
in AI assistants, examining how alignment criteria such as
helpfulness, preference data, and human feedback contribute
to the tendency of AI models to provide responses that
align with user beliefs rather than prioritizing truthfulness.
The study reveals that the pursuit of helpfulness through
reinforcement learning from human feedback (RLHF) can
inadvertently promote sycophantic behavior, as users often
prefer responses that confirm their existing beliefs. Analysis
of human preference data used in training preference models
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 19 of 34

--- Page 21 ---

AI Safety in Generative AI Large Language Models: A Survey
AI to Human
Alignment
Direct
Preference
Learning
Preference-
based RL
(PbRL)
Aligned to
Human Safety
Supervised
Fine-Tuning
(SFT)
Contrastive
Preference
Learning
(CPL)
DPO Rafailov et al.
(2023), IPO Azar
et al. (2023), KTO
Ethayarajh et al. (2024)
RLHF
RLAIF
Safe RL
Preference
Modeling
RL Reward
Modeling
RL Policy
Update
REINFORCE Sutton et al. (1999), CPI Kakade and
Langford (2002), TRPO Schulman et al. (2017a),
PPO Schulman et al. (2017b), AWR Peng et al.
(2019); Nair et al. (2021), APA Zhu et al. (2023)
Human In-The-
Loop (HITL)
Constrained
RL
Risk-
Sensitive RL
Encodes high-
level preference
descriptions and uses
self-improvement
Bai et al. (2022b)
Learn from
human-labeled
data to guide
model outputs
resulting to
a pre-trained
model
Start w. SFT pre-
trained model for
various downstream
tasks Ouyang et al.
(2022); Glaese
et al. (2022); Bai
et al. (2022a)
Construct reward func.
from pairwise comparisons
or listwise rankings of
human preferences data
Bradley and Terry (1952)
Optimizes policy on iterate
based on reward model
Sutton et al. (1999)
Enforces
safety
constraints
during reward
modeling
Achiam et al.
(2017); Zhang
et al. (2024b)
Minimizes
unsafe actions
to humans or
environment
during reward
modeling
Shen et al.
(2014)
Learn directly from
preferred labels, CPL
Hejna et al. (2024)
Humans involved
in the iterative
update Hejna and
Sadigh (2022)
Figure 9: An overview of reinforcement learning (RL) research approaches for AI to human alignment in the context of generative
AI large language models.
(PMs) for AI assistants demonstrates a bias towards syco-
phantic responses, with user-aligned views more likely to be
favored. Furthermore, the research highlights how human
feedback, while crucial in AI training, can reinforce and
perpetuate sycophantic tendencies by rewarding responses
that match user expectations. These findings underscore the
complex interplay between alignment criteria and the devel-
opment of sycophantic behavior in AI models, emphasizing
the need for more nuanced training methodologies that ex-
tend beyond reliance on human ratings and preferences to
mitigate these tendencies and promote more objective and
truthful AI responses.
6.5. Methods to Align LLMs
Zhao et al. (2023) contributes a comprehensive survey of
alignment, noted for its technical rigor and detail. Liu et al.
(2023) scrutinize the reliability of even aligned models, em-
phasizing the specific challenges that large language models
(LLMs) encounter in practical applications. Moreover, Liu
et al. (2023) propose a taxonomy addressing trustworthi-
ness issues relevant to LLMs, distinguishing between outer
alignment (e.g., societal impacts) and inner alignment (e.g.,
model intentions). In a similar vein, Wang et al. (2023c) pro-
vide an additional survey on alignment methods for LLMs,
covering strategies to mitigate undesirable behaviors. Con-
versely, Shen et al. (2023b)’s research could refine this
taxonomy by focusing on inner alignment issues. Specific
alignment concerns in general-purpose agent models in-
clude deceptive actions, manipulative behaviors, harmful
content generation, and gaming of objectives Shen et al.
(2023b). Within AI Safety research, techniques to ensure
AI agents operate within acceptable boundaries—such as
Safe Reinforcement Learning (RL)—are suggested. These
include constrained reinforcement learning, which does not
necessarily align directly with human preferences but en-
sures agents avoid harmful actions to humans or the environ-
ment or at least minimize such cases through risk-sensitive
reinforcement learning Achiam et al. (2017); Zhang et al.
(2024b); Shen et al. (2014).
6.5.1. Language Assistants, Reinforcement Learning
The work in Christiano et al. (2023); Ouyang et al.
(2022) demonstrated the efficacy of reinforcement learning
from human feedback (RLHF), while Sparrow’s alignment
methodology is detailed in Glaese et al. (2022). In Sparrow’s
reinforcement learning environment, the optimization objec-
tive notably incorporates a distribution of dialogue contexts,
which allows the model to better generate aligned content to
the relevant conversational settings.
Drawing upon the effective implementation of RLHF
in generative large language models, the approach can be
generally described as follows (an extensive overview of
diverse methodologies is available in Jiang et al. (2024)).
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 20 of 34

--- Page 22 ---

AI Safety in Generative AI Large Language Models: A Survey
• Collecting Preference Data for Pairwise Comparison
Preference or Ranked Preference. To train the reward
model, typically through supervised learning, a com-
prehensive dataset comprising pairwise comparison
or ranked preference samples is essential. This dataset
should be a collection of desired response done usu-
ally by human participants whom act as proxy for
deciding on which qualities for the natural language
generation task align to the language model assistant
Jiang et al. (2024).
• Reward Model Training with Preference Data. Next,
we create a dataset of manually ranked response pairs,
where human experts compare the quality of differ-
ent natural language generation model outputs for a
given prompt. This dataset is then used to train a
reward model that can assess the quality of generated
response. Reward learning enables the application of
reinforcement learning (RL) to tasks where reward is
defined by human judgment, building a model of re-
ward by asking humans questions Ziegler et al. (2020).
The heavily referenced approach for reward modeling
based on preferences through pairwise comparisons
is the Bradley and Terry model Bradley and Terry
(1952).
• Fine-tuning for RL Policy Optimization. Proximal
Policy Optimization (PPO) is widely regarded as an
effective method for updating policies in reinforce-
ment learning (RL). This policy gradient technique is
iteratively adjusting the policy based on the estimated
gradient of the expected reward in relation to the
policy parameters. Despite its popularity, Azar et al.
(2023) suggest that the REINFORCE algorithm can
achieve comparable performance Sutton et al. (1999).
Fine-tuning large language models is an evolving re-
search area with innovative methods that have shown ef-
fectiveness in producing content favoured by humans, often
incorporating reinforcement learning from human feedback
(RLHF) Ziegler et al. (2020); Christiano et al. (2023). This
approach can be further studied by utilising implementation
specifics and code resources from OpenAI’s Baselines and
LM-Human Preferences repositories Ziegler et al. (2019).
Tajwar et al. (2024) provides a unification of fine-tuning
techniques within a singular framework. Fine-tuning has
generally demonstrated effectiveness even with datasets sub-
stantially smaller than those used for pre-training Thoppilan
et al. (2022).
• Preference Learning based RL, recognized as the pre-
eminent technique for model refinement. The concept
of RLHF was popularised by Christiano et al. (2023)
inspiring Ouyang et al. (2022); Glaese et al. (2022);
Bai et al. (2022a), with the experiment of incorpo-
rating human instructions, and further work into lan-
guage models elaborated in Ziegler et al. (2019, 2020).
Presently, the remaining challenges for using human
feedback involve becoming accidental philosophers,
as well as establishing initial preference frameworks
for training datasets and devising methodologies to
ensure that researchers do not inadvertently become
arbiters of human values Gabriel (2020); Askell et al.
(2021); Hendrycks et al. (2023).
• Direct Preference Learning. Another noteworthy pro-
gression in this domain is Direct Preference Optimiza-
tion (DPO) Rafailov et al. (2023), integrated within
Contrastive Preference Learning (CPL) Hejna et al.
(2024). DPO reframes the Reinforcement Learning
from Human Feedback (RLHF) challenge as a reward
definition problem. This approached can be gener-
alised through CPL, effectively eliminating the ne-
cessity for the Human In-The-Loop (HITL). Hejna
and Sadigh (2022) introduces a few-shot methodology
enhances the efficiency of preference optimization and
mitigates critical challenges in RLHF, such as precise
hyperparameter tuning and the resource requirement
for human annotation leading to potential scalable
oversight discussed in Section 7.1.
The evaluation of alignment models is often criterion-
specific, with notable examples including Glaese et al.
(2022), which established a benchmark while adhering to
Google’s AI safety principles, and Ouyang et al. (2022),
which has significantly impacted further research. Addition-
ally, Park et al. (2024) posits that the primary challenge in
alignment lies in policy learning over value learning.
6.5.2. Generative Agents, Aligning Instrumental Goals
Reward hacking is when the agent learns to receive
rewards from the reward function by performing a task that
may not be intended by the user. On alignment, "we could
try to design a simple reward function that approximately
captures the intended behaviour, but this will often result in
behavior that optimises our reward function without actually
satisfying our preferences. This difficulty underlies recent
concerns about misalignment between our values and the
objectives of our RL systems Amodei et al. (2016)" Com-
municating actual objectives to agents would be a significant
step towards addressing these concerns. Multiple definitions
of reward hacking are discussed in (RH, 2024).
The increasing capability of agents and Nishimura-
Gasparian et al. (2024) claims that reward hacking generalise
across tasks. Instrumental goals serve as sub-objectives
that contribute to the pursuit of specific goals. Convergent
instrumentals, in particular, are instrumental in achieving
a wide range of objectives Chan et al. (2023). Preliminary
evidence Perez et al. (2022b) indicates that training LLMs
using reinforcement learning techniques can increase the ex-
pression of convergent instrumental goals, such as pursuing
wealth or influencing operators not to terminate the system,
even without explicit instructions. This evidence warrants
caution regarding the growing agency of LLMs.
The concept of reward hacking, a phenomenon where
AI agents exploit loopholes in reward systems to maximise
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 21 of 34

--- Page 23 ---

AI Safety in Generative AI Large Language Models: A Survey
rewards without achieving the intended goal, has garnered
significant attention in AI safety research Amodei et al.
(2016); Skalse et al. (2022); Denison et al. (2024). While
Skalse et al. (2022) offer a rigorous theoretical definition
of reward hacking, by highlighting the importance of un-
hackable reward functions with symmetrical policies, their
analysis primarily focuses on tasks with sub-objectives. In
contrast, Ji et al. (2024) delve into reinforcement learning
techniques, examining how reward function learning can
be manipulated to indicate reward hacking. Goyal et al.
(2024) shed light on human expectations from AI agents,
emphasizing the desire for aligned agents free from reward
bias and undesirable behaviors that could tarnish the owner’s
reputation.
Designing for human-agent alignment—the process of
ensuring agents act in accordance with human preferences—is
a critical area of research. Aligning human and agent goals
for a specific task reveals key parameters humans desire
agents to embody: (1) shared knowledge schemas, (2) clearly
defined autonomy and agency, (3) operational alignment
through training, (4) shared heuristics regarding reputa-
tion, (5) ethical alignment, and (6) appropriate levels of
human engagement. These parameters encompass factors
such as the agent’s ability to identify necessary infor-
mation for successful task completion, adherence to pre-
defined boundaries, strategic alignment with the human’s
goals, reflection of interpersonal behavior, ethical decision-
making (e.g., transparency vs. potential exploitation), and
appropriate timing of human supervision. This study by
Goyal et al. (2024), situated within the broader field of
human-computer interaction (HCI), primarily investigates
the human collaborator’s perspective on the constituents of
effective human-agent alignment, mirroring questions raised
in the broader field of AI alignment. A potential area for
future research involves the agent’s role in guiding align-
ment through simulations and identification of successful
negotiation parameters. Furthermore, recent work on reward
hacking in AI systems may offer insights into the challenges
of agent sub-task creation and planning.
Examplary new work of this area include LLMs are
Zero-Shot Reasoners Kojima et al. (2023) and Zero-Shot
Chain-of-Thought Reasoning Guided by Evolutionary Algo-
rithms in Large Language Models, Jin et al. (2024a).
6.5.3. Roleplay
The concept of roleplay in the context of large language
models encompassing a broader spectrum of applications
that leverage these models’ capacity to emulate domain-
specific expertise. This phenomenon has garnered signifi-
cant attention in the field of artificial intelligence and natural
language processing, particularly in its potential to create
agents that convincingly simulate expert knowledge in spe-
cialized fields such as medicine or law Chen et al. (2024);
Wang et al. (2024c). Recent research has explored the nu-
anced capabilities of LLMs to adopt and maintain specific
personas or expert roles, generating responses that align with
the knowledge and communication styles characteristic of
particular domains Shanahan et al. (2023). This adaptability
presents promising avenues for applications across various
sectors, including but not limited to education, professional
training, and advanced decision support systems Li et al.
(2024a).
However, the implementation of expert roleplay in LLMs
is not without its challenges. Ensuring consistent and ac-
curate representation of domain-specific knowledge, main-
taining ethical standards, and mitigating potential biases
are critical concerns that require ongoing investigation Lu
et al. (2024). Moreover, the anthropomorphization of LLMs
through expert roleplay raises profound philosophical and
ethical questions regarding the nature of artificial intelli-
gence and its implications for human-machine interactions
Gabriel et al. (2024) and scaling generated synthetic data
Chan et al. (2024).
7. Safety at Scale
GAI-LLMs such as Gopher Rae et al. (2022), the GPT
series OpenAI et al. (2024), and LLaMa Touvron et al.
(2023) have shown impressive abilities in tasks in natu-
ral language processing; particularly with natural language
understanding and natural language generation. These ad-
vancements are due in large part to the scaling of model
sizes, which has sparked intriguing questions about the
emergent properties of AI Wei et al. (2022a); Bubeck et al.
(2023). However, this progress also presents challenges, par-
ticularly in ensuring safety and mitigating potential harms
Rae et al. (2022); Gabriel et al. (2024); Weidinger et al.
(2024b).
Understanding of the scaling of LLMs has been guided
by empirical observations known as "scaling laws." These
laws, initially established by Kaplan et al. (2020), reveal
a predictable relationship between the performance of the
model, the number of model parameters, the size of the data
set, and computational resources. This finding led to the
development of increasingly larger language models, with
the expectation of continuous performance improvements.
Key studies can be mentioned that have contributed to
our understanding of scaling laws. Gopher, as a language
model of 280 billion parameters Rae et al. (2022), provided
a comprehensive analysis of scaling in Transformer-based
language models, while Brown et al. (2020) introduced
GPT-3, using the same architecture as GPT-2 but scaled
to 175 billion parameters, showcasing the power of large-
scale models in few-shot learning scenarios. Later studies,
including the work of Hoffmann et al. (2022), introduced the
Chinchilla model as the direct successor to Gopher, outper-
forming Gopher despite having only 70 billion parameters,
emphasising the importance of balancing model size with
training data.
However, the race to scale LLMs has also raised con-
cerns about their safety and potential harms Shen et al.
(2023b). These concerns are not new, with early discussions
in the HHH models Askell et al. (2021) and Sparrow Glaese
et al. (2022) highlighting the challenges of aligning model
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 22 of 34

--- Page 24 ---

AI Safety in Generative AI Large Language Models: A Survey
behaviour with human values as models grow larger. This
requires a deeper understanding of alignment strategies,
including fine-tuning, especially with a focused discussion
that pertains to alignment with scaling Zhang et al. (2024a).
In the software development lifecycle, the development
of safe and responsible LLMs has become an important con-
cern. Recent work by Raza et al. (2024) suggests the Safe and
Responsible Large Language Model (SR), an approach de-
signed to enhance safety through expert-annotated datasets
and fine-tuning methods. Furthermore, work by Huang et al.
(2023a) and Das et al. (2024) explore vulnerabilities in
LLMs and the need for robust evaluation methods.
7.1. Scalable Oversight
Scalable oversight is the concern that as large language
models involve more training iterations, the techniques we
use to safely align them by supervising during training
will later not be sufficient to ensure safety from risks and
harms of these models Amodei et al. (2016). Harandizadeh
et al. (2024) surveys the existing specific failure modes of
safety-trained LLMs, with a particular focus on competitive
objectives and mismatched generalization. Their analysis of
the Anthropic Red-team dataset reveals significant vulner-
abilities across major risk categories, including informa-
tion hazards, malicious uses, and discriminatory content.
In particular, their findings on the susceptibility of LLMs
to jailbreaking attacks underscore the need for more robust
and adaptive safety measures. This empirical approach to
risk assessment, grounded in real-world data and adversarial
testing, provides valuable insights for developing targeted
interventions and improving the resilience of LLMs against
diverse threats.
Despite these efforts, the field still grapples with fun-
damental questions about the impact of scaling on LLMs
safety. The increasing complexity of these models makes it
difficult to predict and control their behaviour, potentially
leading to unintended consequences and harmful outputs.
The argument is that on larger scales, there will be gaps in
human ability to guarantee safety; the rapid pace of LLMs
development often exceeds our ability to thoroughly assess
and mitigate risks Schiller (2024); Huang et al. (2023b).
In addressing this problem of scalable oversight, one
approach is Dalrymple et al. (2024)’s work which introduces
the concept of "guaranteed safe" (GS) AI. By proposing a
framework that combines a formal safety specification, a
world model, and a verifier, GS AI aims to provide high-
assurance quantitative safety guarantees. While acknowledg-
ing the technical challenges in creating these components,
the authors argue for the necessity of this approach in achiev-
ing robust and reliable AI systems. This focus on formal
verification and rigorous safety standards reflects a growing
trend in the AI community towards prioritizing safety as a
fundamental design principle rather than an afterthought.
7.2. Emergent Abilities
The exploration of emergent abilities in LLMs by Wei
et al. (2022a) reveals that certain capabilities, like multi-step
reasoning, only manifest in larger models. This mysterious
occurrence, referred to as "emergence," highlights the com-
plex link between the size of the model and its capabilities.
From a technical standpoint, "larger" models refer to
language models that have a higher number of parameters
and require more computational resources for training. The
scale of a model is measured in terms of training FLOPs
(floating-point operations) and the number of model param-
eters. Larger models have higher training FLOPs and a larger
number of parameters, indicating their increased size and
computational requirements. Scaling up a language model
involves increasing both the number of parameters and the
training compute Wei et al. (2022a).
As the model scales in discussions pertaining to emer-
gence, the language model demonstrates enhanced capabil-
ities in reasoning. In the context of emergence-related re-
search in reasoning, numerous papers present novel method-
ologies aimed at further augmenting large language models.
Wei et al. (2023b) demonstrates the efficacy of generating
intermediate reasoning steps, significantly enhancing per-
formance on complex tasks such as arithmetic and sym-
bolic reasoning. Ho et al. (2023) proposes a novel approach
wherein larger models act as "teachers," generating reason-
ing samples to fine-tune smaller models, thereby improving
their reasoning capabilities. Moreover, Zhang et al. (2024e)
explores dynamic reasoning in competitive scenarios using
game theory-based challenges, introducing a novel "K-Level
Reasoning" approach that substantially improves prediction
accuracy.
However, Huang et al. (2024b) cautions that LLMs
struggle with intrinsic self-correction, often requiring ex-
ternal feedback to correct their reasoning Huang and Chang
(2023b). This finding suggests a reassessment of the poten-
tial applications of LLMs in scenarios where self-correction
is crucial.
Assessment of reasoning abilities remains a critical as-
pect of LLMs research Dziri et al. (2023). Mondorf and
Plank (2024); Bender et al. (2021) examines the reasoning
and behaviour of large language models, noting that chal-
lenges still exist in test situations outside of their training
data. Even if there is new evidence of the remarkable ca-
pability of generative models to address analogy problems
without specific training, frequently matching or exceeding
human performance Webb et al. (2023) or surpassing hu-
mans as trainers, as shown in gameplay Zhang et al. (2024c),
state-of-the-art LLMs underperform on common sensical
reasoning tasks Nezhurina et al. (2024).
7.3. Knowledge Distillation
Knowledge Distillation (KD) is a technique for trans-
ferring the capabilities of large models to smaller, more
computationally efficient architectures Hinton et al. (2015);
Buciluundefined et al. (2006), often achieving comparable
or even superior performance in tasks such as instruction-
following Lee et al. (2023). Despite the performance, Stan-
ton et al. (2021) describes the limitations of KD, that despite
improvements in student generalisation, there remains a
significant discrepancy between the predictive distributions
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 23 of 34

--- Page 25 ---

AI Safety in Generative AI Large Language Models: A Survey
of the teacher and the student. This discrepancy is attributed
to difficulties in optimisation and the details of the dataset
used for distillation.
More recent research has explored various facets of
KD, with a particular emphasis on enhancing reasoning
abilities in smaller models. Kang et al. (2023) introduced
Knowledge-Augmented Reasoning Distillation (KARD), a
novel KD approach that fine-tunes small models to generate
rationales augmented with external knowledge, leading to
significant improvements in knowledge-intensive reasoning
tasks. Similarly, Ho et al. (2023) proposed Fine-tune-CoT,
leveraging large models as reasoning teachers to impart
complex reasoning abilities to smaller models, resulting in
substantial performance gains across a range of tasks.
Various studies have concentrated on the distillation
of step-by-step reasoning processes. Hsieh et al. (2023b)
proposed a distillation method that enables smaller models
to surpass LLMs with less training data, while Shridhar
et al. (2023) introduced Socratic CoT, a distillation tech-
nique that decomposes complex reasoning tasks into sub-
problems, promoting collaborative problem-solving among
smaller models to reach reasoning abilities similar to those
of larger models. Gu et al. (2024) presented MiniLLM, a
reverse KD method that produces more accurate responses
and excels in long-text generation tasks. Additionally, re-
searchers are investigating dynamic KD frameworks that in-
tegrate active learning to iteratively generate annotated data
and provide feedback to LLMs. Liu et al. (2024a) introduced
EvoKD, which improves task-specific capabilities in smaller
models, especially in text classification and named entity
recognition tasks.
Research into utilizing knowledge distillation methods,
including Zephyr Tunstall et al. (2023) and Align-to-Distill
Jin et al. (2024b), has shown the promise of better aligning
model behavior by fine-tuning smaller models that are de-
rived from larger ones.
7.4. Catastrophic Forgetting
The development LLMs generally comprises two pri-
mary stages: pre-training on extensive text corpora and fine-
tuning using curated datasets. Fine-tuning, through tech-
niques such as instruction-tuning and reinforcement learning
from human feedback, is essential for enabling language
models to generate desired outputs. Given that fine-tuning
datasets are significantly smaller and less diverse than the
large-scale datasets used for pretraining, there is an inherent
risk that the fine-tuned model may catastrophically forget
how to perform tasks that the pretrained model could handle
Kotha et al. (2024). On the other hand, recent research indi-
cates that catastrophic forgetting becomes more pronounced
as the scale of the large language model increases. Recent
research indicates that catastrophic forgetting becomes more
pronounced as the scale of large language models increases,
which causes the safety concerns of applying large language
models. Several strategies have been proposed and explored
in the literature. One approach involves continual learning
techniques, which allow the model to retain previous knowl-
edge while integrating new information Wang et al. (2024b),
where LLMs can be treated as continual learners. Another
strategy is to adapt the elastic weight consolidation (EWC)
strategy into the fine tuning process Kirkpatrick et al. (2017),
where the model selectively updates weights to preserve
important knowledge from previous tasks. Implementing
memory replay methods, where the model periodically re-
visits and retrains on a subset of the pretraining data, can
also help maintain performance on previously learned tasks
Scialom et al. (2022). Finally, hybrid models that combine
fine-tuning with regularization techniques to balance new
learning and knowledge retention are also being investi-
gated. These methods aim to enhance the robustness of large
language models against catastrophic forgetting, ensuring
they retain their capabilities while adapting to new tasks.
8. Future Work
Recent advancements in AI alignment have transcended
the conventional pre-training and fine-tuning phases. The
discipline now includes aligning subgoals (task-specific
objectives), mitigating deceptive behaviours in human-agent
interactions, and coordinating multi-agent systems. We high-
light the following emerging research trends that are ready
for further exploration.
1. Safe Retrieval-Augmented Generation (RAG). Emerg-
ing research areas include exploring safety considerations
specific to natural language generation models and those
employing retrieval augmentation techniques Lewis et al.
(2021); Hong et al. (2024).
2. Deeper Understanding of Knowledge distillation (KD).
Knowledge distillation is a technique to transfer the
weights of large models onto smaller models. We suggest
that the translation of alignment to these smaller models
is will continue to be explored, e.g. Align-to-Distill Jin
et al. (2024b). Another example is Zephyr Tunstall et al.
(2023), a model that is fine-tuned from a knowledge-
distilled model that focuses on alignment. Ye et al.
(2021) introduces the concept of a "Safe Distillation
Box" and looking into ensuring that in the KD process,
harmful behaviours such as preventing the transfer of
harmful or biased knowledge from the teacher model to
the student model. Nevertheless, as discussed in Anwar
et al. (2024), the balance between performance and safety
during scaling remains unclear.
3. Aligned Cooperation in Multi-Agent Reinforcement
Learning (MARL). In scenarios where generative AI
operates autonomously, agents can engage in unpre-
dictable behaviours as exemplified by the "hide-and-
seek" paper referring to the ML agents in the video game
Baker et al. (2020), which is a risk considering the pursuit
of power often emerges as a component of the AI’s reward
function incentives Carlsmith (2022).
4. Agentic: Increasing Agency. Autonomous agents with
increasing capabilities to complete tasks beyond question
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 24 of 34

--- Page 26 ---

AI Safety in Generative AI Large Language Models: A Survey
and answer, or agentic systems, execute tasks indepen-
dently Huang et al. (2024c). However, as generative AI
language models advance in capability, it is anticipated
that these agents will exhibit enhanced agency and con-
trol in the generation of subtasks. This progression neces-
sitates further investigation into reward hacking and the
specific power-seeking strategies employed by these AI
systems Amodei et al. (2016); Carlsmith (2022).
5. Aligning a Mixture of Experts (MoE) / Mixture of
Agents (MoA). The utilization of diverse aligned models,
including ensemble methods and the incorporation of
additional alignment layers, remains an exciting avenue
within the Mixture of Experts Shen et al. (2023a) and
work extending this ideas into a Mixture of Agents frame-
work Wang et al. (2024a).
6. Security of Generative LLMs. Ensuring the security
of generative LLMs involves careful attention through-
out the various stages of their development. Effective
deployment requires a thorough grasp of the interplay
and mutual influence of different methods. This encom-
passes the implementation of protective measures, red
teaming approaches, and the combined use of techniques
such as prompt engineering, fine-tuning, and retrieval-
augmented generation (RAG) Dong and Xie (2024); Ab-
dali et al. (2024)
7. Natural Language Generation (NLG) Alignment for
In-Context Learning (ICL). Current research is delv-
ing deeper into alignment methods specifically for nat-
ural language generation Lin et al. (2023). Huang et al.
(2024a) surveys the state of alignment in-context learn-
ing, which underscore the lack of transparency in in-
context learning (ICL) in multi-turn dialogues and in-
struction following, stressing the necessity for precise
alignment strategies during generation to achieve more
secure and dependable language models Wang et al.
(2024e).
8. Natural Language Understanding (NLU) and Prin-
cipled Agent. Sun et al. (2023) has investigated the
formulation of models that internalize ethical principles,
a promising trajectory given the potential for AI to in-
fluence discourses on AI ethics and safety Goyal et al.
(2024). This methodology is particularly pertinent in
light of the transmission of toxicity from pre-training
datasets, a problem addressed by Reinforcement Learn-
ing from AI Feedback (RLAIF), also referred to as Con-
stitutional AI Bai et al. (2022b). In the RLAIF paradigm,
principles are autonomously assimilated by the AI, with
continuous feedback provided by the AI itself, presenting
a viable approach to the scalability issues of AI systems as
discussed in Anwar et al. (2024). The notion of principled
LLMs, as examined in recent literature, further highlights
the criticality of embedding ethical considerations into
the development of LLMs from their inception.
9. Safe Reinforcement Learning for Agentic LLMs. Re-
inforcement learning (RL) can be approached through
a reevaluation of established concepts Achiam et al.
(2017); Zhang et al. (2024b), particularly unifying RL
approaches like those in control systems Georgiev et al.
(2024). Furthermore, analysis of divergence within imita-
tion learning methods also warrant review Ghasemipour
et al. (2019). As models gain more capability and auton-
omy as agents, there will be an exchange of concepts in
assessing agents akin to safe RL evaluation in performing
safety-critical tasks Zhang et al. (2022a).
10. Self-governing and Introspective Generative Agents.
The potential synergy between advancing natural lan-
guage understanding and principled large language model
research presents, along with new RL techniques, present
a novel avenue for addressing alignment challenges. As
AI agents can become increasingly adept at identifying
vulnerabilities in their own subgoals, models equipped
with self-regulation mechanisms could enhance align-
ment Goyal et al. (2024).
Future research should rigorously investigate the conflu-
ence of AI safety and natural language generation (NLG),
examining the complex interplay between language gener-
ation methodologies (e.g., next-token prediction) and the
cognitive processes within AI agents. This line of inquiry
has the potential to provide novel insights into addressing
issues of misalignment and reward hacking as we progress
further into the agentic treatment of generative LLMs.
9. Conclusion
In this survey paper, we explore the safety issues that
accompany the accelerated research development of large
language models. We examine these safety challenges that
manifest at various levels: data, model, and usage. Fur-
thermore, we delve deeply into the technical safety con-
cerns of alignment in GAI-LLMs, emphasising the stark
contrast between the proclaimed alignment criteria and the
methods employed to achieve them. We shed light on the
inherent safety risks that arise during the development and
deployment phases of these models. Furthermore, we iden-
tify promising avenues for future research in the realm of
AI safety for generative LLMs. AI alignment research is
rapidly expanding into unexplored territories, encompassing
a broader spectrum of techniques and challenges. From
investigating safety in natural language generation models
to applying knowledge distillation and navigating the com-
plexities of multi-agent alignment, the field is brimming
with opportunities for further exploration. However, the
evolving landscape also introduces new complexities and
trade-offs that necessitate careful consideration and rigorous
investigation. The journey towards safer and more aligned
AI systems demands relentless exploration and innovation,
building on the foundational work presented in this compre-
hensive overview.
References
Abdali, S., Anarfi, R., Barberan, C., He, J., 2024.
Securing large
language models: Threats, vulnerabilities and responsible practices.
arXiv:2403.12503.
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 25 of 34

--- Page 27 ---

AI Safety in Generative AI Large Language Models: A Survey
Achiam, J., Held, D., Tamar, A., Abbeel, P., 2017. Constrained policy op-
timization. URL: https://arxiv.org/abs/1705.10528, arXiv:1705.10528.
Agarwal, D., Fabbri, A.R., Laban, P., Risher, B., Joty, S., Xiong, C., Wu,
C.S., 2024.
Investigating the prompt leakage effect and black-box
defenses for multi-turn llm interactions. arXiv:2404.16251.
Ai, L., Kumarage, T., Bhattacharjee, A., Liu, Z., Hui, Z., Davinroy, M.,
Cook, J., Cassani, L., Trapeznikov, K., Kirchner, M., Basharat, A.,
Hoogs, A., Garland, J., Liu, H., Hirschberg, J., 2024. Defending against
social engineering attacks in the age of llms. arXiv:2406.12263.
Ainslie, J., Ontanon, S., Alberti, C., Cvicek, V., Fisher, Z., Pham, P.,
Ravula, A., Sanghai, S., Wang, Q., Yang, L., 2020.
ETC: Encod-
ing long and structured inputs in transformers, in: Proceedings of the
2020 Conference on Empirical Methods in Natural Language Process-
ing (EMNLP), Association for Computational Linguistics, Online. pp.
268–284. URL: https://aclanthology.org/2020.emnlp-main.19, doi:10.
18653/v1/2020.emnlp-main.19.
Alberts, I.L., Mercolli, L., Pyka, T., Prenosil, G., Shi, K., Rominger, A.,
Afshar-Oromieh, A., 2023. Large language models (llm) and chatgpt:
what will the impact on nuclear medicine be?
European journal of
nuclear medicine and molecular imaging , 1–4.
Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J., Mané, D.,
2016. Concrete problems in ai safety. arXiv:1606.06565.
Andriushchenko, M., Croce, F., Flammarion, N., 2024. Jailbreaking leading
safety-aligned llms with simple adaptive attacks. arXiv:2404.02151.
Anthropic, 2023.
Anthropic’s responsible scaling policy.
URL: https:
//anthropic.com/publications/responsible-scaling-policy.
anthropic, 2023.
Claude.
URL: https://www.anthropic.com/index/
introducing-claude.
Anthropic, 2024.
Many-shot jailbreaking.
https://www.anthropic.com/
research/many-shot-jailbreaking. Accessed on June 24, 2024.
Anwar, U., Saparov, A., Rando, J., Paleka, D., Turpin, M., Hase, P., Lubana,
E.S., Jenner, E., Casper, S., Sourbut, O., Edelman, B.L., Zhang, Z., Gün-
ther, M., Korinek, A., Hernandez-Orallo, J., Hammond, L., Bigelow, E.,
Pan, A., Langosco, L., Korbak, T., Zhang, H., Zhong, R., h’Eigeartaigh,
S.O., Recchia, G., Corsi, G., Chan, A., Anderljung, M., Edwards, L.,
Bengio, Y., Chen, D., Albanie, S., Maharaj, T., Foerster, J., Tramer,
F., He, H., Kasirzadeh, A., Choi, Y., Krueger, D., 2024. Foundational
challenges in assuring alignment and safety of large language models.
arXiv:2404.09932.
API, P., . About the api - attributes and languages. URL: https://support.
perspectiveapi.com/s/about-the-api-attributes-and-languages?
language=en_US.
Askell, A., Bai, Y., Chen, A., Drain, D., Ganguli, D., Henighan, T., Jones,
A., Joseph, N., Mann, B., DasSarma, N., Elhage, N., Hatfield-Dodds,
Z., Hernandez, D., Kernion, J., Ndousse, K., Olsson, C., Amodei, D.,
Brown, T., Clark, J., McCandlish, S., Olah, C., Kaplan, J., 2021. A gen-
eral language assistant as a laboratory for alignment. arXiv:2112.00861.
Azar, M.G., Rowland, M., Piot, B., Guo, D., Calandriello, D., Valko,
M., Munos, R., 2023.
A general theoretical paradigm to understand
learning from human preferences. URL: https://arxiv.org/abs/2310.
12036, arXiv:2310.12036.
Bai, Y., Jones, A., Ndousse, K., Askell, A., Chen, A., DasSarma, N.,
Drain, D., Fort, S., Ganguli, D., Henighan, T., Joseph, N., Kadavath, S.,
Kernion, J., Conerly, T., El-Showk, S., Elhage, N., Hatfield-Dodds, Z.,
Hernandez, D., Hume, T., Johnston, S., Kravec, S., Lovitt, L., Nanda, N.,
Olsson, C., Amodei, D., Brown, T., Clark, J., McCandlish, S., Olah, C.,
Mann, B., Kaplan, J., 2022a. Training a helpful and harmless assistant
with reinforcement learning from human feedback. arXiv:2204.05862.
Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., Chen, A.,
Goldie, A., Mirhoseini, A., McKinnon, C., et al., 2022b. Constitutional
ai: Harmlessness from ai feedback. arXiv preprint arXiv:2212.08073 .
Baker, B., Kanitscheider, I., Markov, T., Wu, Y., Powell, G., McGrew, B.,
Mordatch, I., 2020. Emergent tool use from multi-agent autocurricula.
arXiv:1909.07528.
Banerjee, S., Lavie, A., 2005. Meteor: An automatic metric for mt evalua-
tion with improved correlation with human judgments, in: Proceedings
of the acl workshop on intrinsic and extrinsic evaluation measures for
machine translation and/or summarization, pp. 65–72.
Bender, E.M., Gebru, T., McMillan-Major, A., Shmitchell, S., 2021. On
the dangers of stochastic parrots: Can language models be too big?, in:
Proceedings of the 2021 ACM conference on fairness, accountability,
and transparency, pp. 610–623.
Bender, E.M., Koller, A., 2020. Climbing towards nlu: On meaning, form,
and understanding in the age of data, in: Proceedings of the 58th annual
meeting of the association for computational linguistics, pp. 5185–5198.
Bickmore, T.W., Trinh, H., Olafsson, S., O’Leary, T.K., Asadi, R., Rickles,
N.M., Cruz, R., 2018. Patient and consumer safety risks when using
conversational assistants for medical information: an observational study
of siri, alexa, and google assistant. Journal of medical Internet research
20, e11510.
Bird, C., Ungless, E.L., Kasirzadeh, A., 2023.
Typology of risks of
generative text-to-image models. arXiv:2307.05543.
Bocklisch, T., Faulkner, J., Pawlowski, N., Nichol, A., 2017.
Rasa:
Open source language understanding and dialogue management.
arXiv:1712.05181.
Bommasani, R., Hudson, D.A., Adeli, E., Altman, R., Arora, S., von Arx,
S., Bernstein, M.S., Bohg, J., Bosselut, A., Brunskill, E., Brynjolfsson,
E., Buch, S., Card, D., Castellon, R., Chatterji, N., Chen, A., Creel,
K., Davis, J.Q., Demszky, D., Donahue, C., Doumbouya, M., Durmus,
E., Ermon, S., Etchemendy, J., Ethayarajh, K., Fei-Fei, L., Finn, C.,
Gale, T., Gillespie, L., Goel, K., Goodman, N., Grossman, S., Guha,
N., Hashimoto, T., Henderson, P., Hewitt, J., Ho, D.E., Hong, J., Hsu,
K., Huang, J., Icard, T., Jain, S., Jurafsky, D., Kalluri, P., Karamcheti,
S., Keeling, G., Khani, F., Khattab, O., Koh, P.W., Krass, M., Krishna,
R., Kuditipudi, R., Kumar, A., Ladhak, F., Lee, M., Lee, T., Leskovec,
J., Levent, I., Li, X.L., Li, X., Ma, T., Malik, A., Manning, C.D.,
Mirchandani, S., Mitchell, E., Munyikwa, Z., Nair, S., Narayan, A.,
Narayanan, D., Newman, B., Nie, A., Niebles, J.C., Nilforoshan, H.,
Nyarko, J., Ogut, G., Orr, L., Papadimitriou, I., Park, J.S., Piech, C.,
Portelance, E., Potts, C., Raghunathan, A., Reich, R., Ren, H., Rong,
F., Roohani, Y., Ruiz, C., Ryan, J., Ré, C., Sadigh, D., Sagawa, S.,
Santhanam, K., Shih, A., Srinivasan, K., Tamkin, A., Taori, R., Thomas,
A.W., Tramèr, F., Wang, R.E., Wang, W., Wu, B., Wu, J., Wu, Y., Xie,
S.M., Yasunaga, M., You, J., Zaharia, M., Zhang, M., Zhang, T., Zhang,
X., Zhang, Y., Zheng, L., Zhou, K., Liang, P., 2022. On the opportunities
and risks of foundation models. arXiv:2108.07258.
Bordes, F., Pang, R.Y., Ajay, A., Li, A.C., Bardes, A., Petryk, S., Mañas,
O., Lin, Z., Mahmoud, A., Jayaraman, B., Ibrahim, M., Hall, M., Xiong,
Y., Lebensold, J., Ross, C., Jayakumar, S., Guo, C., Bouchacourt, D.,
Al-Tahan, H., Padthe, K., Sharma, V., Xu, H., Tan, X.E., Richards, M.,
Lavoie, S., Astolfi, P., Hemmat, R.A., Chen, J., Tirumala, K., Assouel,
R., Moayeri, M., Talattof, A., Chaudhuri, K., Liu, Z., Chen, X., Garrido,
Q., Ullrich, K., Agrawal, A., Saenko, K., Celikyilmaz, A., Chandra, V.,
2024. An introduction to vision-language modeling. arXiv:2405.17247.
Borji, A., 2023. A categorical archive of chatgpt failures. arXiv preprint
arXiv:2302.03494 .
Bowman, S.R., Hyun, J., Perez, E., Chen, E., Pettit, C., Heiner, S., Luko-
suite, K., Askell, A., Jones, A., Chen, A., et al., 2022.
Measuring
progress on scalable oversight for large language models. arXiv preprint
arXiv:2211.03540 .
Bradley, R.A., Terry, M.E., 1952.
Rank analysis of incomplete block
designs: I. the method of paired comparisons. Biometrika 39, 324–345.
URL: http://www.jstor.org/stable/2334029.
Brown, T.B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P.,
Neelakantan, A., Shyam, P., Sastry, G., Askell, A., Agarwal, S., Herbert-
Voss, A., Krueger, G., Henighan, T., Child, R., Ramesh, A., Ziegler,
D.M., Wu, J., Winter, C., Hesse, C., Chen, M., Sigler, E., Litwin, M.,
Gray, S., Chess, B., Clark, J., Berner, C., McCandlish, S., Radford, A.,
Sutskever, I., Amodei, D., 2020. Language models are few-shot learners.
arXiv:2005.14165.
Bubeck, S., Chandrasekaran, V., Eldan, R., Gehrke, J., Horvitz, E., Kamar,
E., Lee, P., Lee, Y.T., Li, Y., Lundberg, S., Nori, H., Palangi, H., Ribeiro,
M.T., Zhang, Y., 2023. Sparks of artificial general intelligence: Early
experiments with gpt-4. arXiv:2303.12712.
Buciluundefined, C., Caruana, R., Niculescu-Mizil, A., 2006.
Model
compression, in: Proceedings of the 12th ACM SIGKDD International
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 26 of 34

--- Page 28 ---

AI Safety in Generative AI Large Language Models: A Survey
Conference on Knowledge Discovery and Data Mining, Association for
Computing Machinery, New York, NY, USA. p. 535–541. URL: https:
//doi.org/10.1145/1150402.1150464, doi:10.1145/1150402.1150464.
Carlini, N., Paleka, D., Dvijotham, K.D., Steinke, T., Hayase, J., Cooper,
A.F., Lee, K., Jagielski, M., Nasr, M., Conmy, A., Wallace, E., Rolnick,
D., Tramèr, F., 2024. Stealing part of a production language model.
URL: https://arxiv.org/abs/2403.06634, arXiv:2403.06634.
Carlini, N., Tramer, F., Wallace, E., Jagielski, M., Herbert-Voss, A., Lee,
K., Roberts, A., Brown, T., Song, D., Erlingsson, U., Oprea, A., Raffel,
C., 2021. Extracting training data from large language models. URL:
https://arxiv.org/abs/2012.07805, arXiv:2012.07805.
Carlsmith,
J.,
2022.
Is
power-seeking
ai
an
existential
risk?
arXiv:2206.13353.
Chan, A., Salganik, R., Markelius, A., Pang, C., Rajkumar, N., Krashenin-
nikov, D., Langosco, L., He, Z., Duan, Y., Carroll, M., et al., 2023.
Harms from increasingly agentic algorithmic systems, in: Proceedings
of the 2023 ACM Conference on Fairness, Accountability, and Trans-
parency, pp. 651–666.
Chan, X., Wang, X., Yu, D., Mi, H., Yu, D., 2024. Scaling synthetic data
creation with 1,000,000,000 personas.
URL: https://arxiv.org/abs/
2406.20094, arXiv:2406.20094.
Chang, K.W., Prabhakaran, V., Ordonez, V., 2019.
Bias and fairness
in natural language processing, in: Baldwin, T., Carpuat, M. (Eds.),
Proceedings of the 2019 Conference on Empirical Methods in Natural
Language Processing and the 9th International Joint Conference on
Natural Language Processing (EMNLP-IJCNLP): Tutorial Abstracts,
Association for Computational Linguistics, Hong Kong, China. URL:
https://aclanthology.org/D19-2004.
Chen, J., Wang, X., Xu, R., Yuan, S., Zhang, Y., Shi, W., Xie, J., Li, S.,
Yang, R., Zhu, T., Chen, A., Li, N., Chen, L., Hu, C., Wu, S., Ren, S.,
Fu, Z., Xiao, Y., 2024. From persona to personalization: A survey on
role-playing language agents. arXiv:2404.18231.
Chen, M., Du, J., Pasunuru, R., Mihaylov, T., Iyer, S., Stoyanov, V.,
Kozareva, Z., 2022. Improving in-context few-shot learning via self-
supervised training. arXiv preprint arXiv:2205.01703 .
Chowdhery, A., Narang, S., Devlin, J., Bosma, M., Mishra, G., Roberts,
A., Barham, P., Chung, H.W., Sutton, C., Gehrmann, S., et al., 2022.
Palm: Scaling language modeling with pathways.
arXiv preprint
arXiv:2204.02311 .
Christiano, P., Leike, J., Brown, T.B., Martic, M., Legg, S., Amodei,
D., 2023.
Deep reinforcement learning from human preferences.
arXiv:1706.03741.
Chung, H.W., Hou, L., Longpre, S., Zoph, B., Tay, Y., Fedus, W., Li, E.,
Wang, X., Dehghani, M., Brahma, S., et al., 2022. Scaling instruction-
finetuned language models. arXiv preprint arXiv:2210.11416 .
Clark, K., Luong, M.T., Le, Q.V., Manning, C.D., 2020.
Electra: Pre-
training text encoders as discriminators rather than generators. arXiv
preprint arXiv:2003.10555 .
Cobbe, K., Kosaraju, V., Bavarian, M., Chen, M., Jun, H., Kaiser, L.,
Plappert, M., Tworek, J., Hilton, J., Nakano, R., et al., 2021. Training
verifiers to solve math word problems. arXiv preprint arXiv:2110.14168
.
Czarnowska, P., Vyas, Y., Shah, K., 2021. Quantifying social biases in nlp:
A generalization and empirical comparison of extrinsic fairness metrics.
Transactions of the Association for Computational Linguistics 9, 1249–
1267.
Dai, Z., Yang, Z., Yang, Y., Carbonell, J., Le, Q.V., Salakhutdinov, R.,
2019. Transformer-xl: Attentive language models beyond a fixed-length
context. arXiv preprint arXiv:1901.02860 .
Dalrymple, D., Skalse, J., Bengio, Y., Russell, S., Tegmark, M., Seshia, S.,
Omohundro, S., Szegedy, C., Goldhaber, B., Ammann, N., Abate, A.,
Halpern, J., Barrett, C., Zhao, D., Zhi-Xuan, T., Wing, J., Tenenbaum,
J., 2024. Towards guaranteed safe ai: A framework for ensuring robust
and reliable ai systems. arXiv:2405.06624.
Daneshjou, R., Smith, M.P., Sun, M.D., Rotemberg, V., Zou, J., 2021. Lack
of transparency and potential bias in artificial intelligence data sets and
algorithms: a scoping review. JAMA dermatology 157, 1362–1369.
Das, B.C., Amini, M.H., Wu, Y., 2024. Security and privacy challenges of
large language models: A survey. arXiv:2402.00888.
Deng, M., Wang, J., Hsieh, C.P., Wang, Y., Guo, H., Shu, T., Song, M.,
Xing, E.P., Hu, Z., 2022. Rlprompt: Optimizing discrete text prompts
with reinforcement learning. arXiv:2205.12548.
Denison, C., MacDiarmid, M., Barez, F., Duvenaud, D., Kravec, S.,
Marks, S., Schiefer, N., Soklaski, R., Tamkin, A., Kaplan, J., Shlegeris,
B., Bowman, S.R., Perez, E., Hubinger, E., 2024.
Sycophancy to
subterfuge: Investigating reward-tampering in large language models.
arXiv:2406.10162.
Derczynski, L., Galinkin, E., Martin, J., Majumdar, S., Inie, N., 2024.
garak: A framework for security probing large language models.
arXiv:2406.11036.
Derner, E., Batistič, K., 2023.
Beyond the safeguards: Exploring the
security risks of chatgpt. arXiv preprint arXiv:2305.08005 .
Devlin, J., Chang, M.W., Lee, K., Toutanova, K., 2018. Bert: Pre-training
of deep bidirectional transformers for language understanding. arXiv
preprint arXiv:1810.04805 .
Dong, H., Xie, S., 2024.
Large language models (llms): Deployment,
tokenomics and sustainability. arXiv:2405.17147.
Dong, Q., Li, L., Dai, D., Zheng, C., Wu, Z., Chang, B., Sun, X., Xu, J., Li,
L., Sui, Z., 2023. A survey on in-context learning. arXiv:2301.00234.
Dong, Y., Mu, R., Jin, G., Qi, Y., Hu, J., Zhao, X., Meng, J., Ruan,
W., Huang, X., 2024. Building guardrails for large language models.
arXiv:2402.01822.
Dragan, A., King, H., Dafoe, A., .
Introducing the frontier safety
framework.
URL:
https://deepmind.google/discover/blog/
introducing-the-frontier-safety-framework/.
Du, N., Huang, Y., Dai, A.M., Tong, S., Lepikhin, D., Xu, Y., Krikun, M.,
Zhou, Y., Yu, A.W., Firat, O., et al., 2022a. Glam: Efficient scaling of
language models with mixture-of-experts, in: International Conference
on Machine Learning, PMLR. pp. 5547–5569.
Du, Z., Qian, Y., Liu, X., Ding, M., Qiu, J., Yang, Z., Tang, J., 2022b.
Glm: General language model pretraining with autoregressive blank
infilling, in: Proceedings of the 60th Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Papers), pp. 320–335.
Duan, H., Dziedzic, A., Papernot, N., Boenisch, F., 2023. Flocks of stochas-
tic parrots: Differentially private prompt learning for large language
models. arXiv preprint arXiv:2305.15594 .
Dziri, N., Lu, X., Sclar, M., Li, X.L., Jiang, L., Lin, B.Y., West, P.,
Bhagavatula, C., Bras, R.L., Hwang, J.D., Sanyal, S., Welleck, S., Ren,
X., Ettinger, A., Harchaoui, Z., Choi, Y., 2023. Faith and fate: Limits of
transformers on compositionality. arXiv:2305.18654.
Ethayarajh, K., Xu, W., Muennighoff, N., Jurafsky, D., Kiela, D., 2024.
Kto: Model alignment as prospect theoretic optimization. URL: https:
//arxiv.org/abs/2402.01306, arXiv:2402.01306.
Floridi, L., Chiriatti, M., 2020.
Gpt-3: Its nature, scope, limits, and
consequences. Minds and Machines 30, 681–694.
Gabriel, I., 2020.
Artificial intelligence, values, and alignment.
Minds and Machines 30, 411–437.
URL: https://doi.org/10.1007%
2Fs11023-020-09539-2, doi:10.1007/s11023-020-09539-2.
Gabriel, I., Manzini, A., Keeling, G., Hendricks, L.A., Rieser, V., Iqbal, H.,
Tomašev, N., Ktena, I., Kenton, Z., Rodriguez, M., et al., 2024. The
ethics of advanced ai assistanning ts. arXiv preprint arXiv:2404.16244 .
Gallegos, I.O., Rossi, R.A., Barrow, J., Tanjim, M.M., Kim, S., Dernon-
court, F., Yu, T., Zhang, R., Ahmed, N.K., 2024. Bias and fairness in
large language models: A survey. URL: https://arxiv.org/abs/2309.
00770, arXiv:2309.00770.
Ganguli, D., Schiefer, N., Favaro, M., Clark, J., 2023.
Challenges
in evaluating AI systems.
URL: https://www.anthropic.com/index/
evaluating-ai-systems.
Garrido-Muñoz, I., Montejo-Ráez, A., Mart’ınez-Santiago, F., Ureña-
López, L.A., 2021. A survey on bias in deep nlp. Applied Sciences
11, 3184.
Gehman, S., Gururangan, S., Sap, M., Choi, Y., Smith, N.A., 2020. Realtox-
icityprompts: Evaluating neural toxic degeneration in language models.
arXiv preprint arXiv:2009.11462 .
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 27 of 34

--- Page 29 ---

AI Safety in Generative AI Large Language Models: A Survey
Georgiev, I., Srinivasan, K., Xu, J., Heiden, E., Garg, A., 2024. Adaptive
horizon actor-critic for policy learning in contact-rich differentiable
simulation. arXiv:2405.17784.
Ghasemipour, S.K.S., Zemel, R., Gu, S., 2019. A divergence minimization
perspective on imitation learning methods. arXiv:1911.02256.
Glaese, A., McAleese, N., Trębacz, M., Aslanides, J., Firoiu, V., Ewalds,
T., Rauh, M., Weidinger, L., Chadwick, M., Thacker, P., Campbell-
Gillingham, L., Uesato, J., Huang, P.S., Comanescu, R., Yang, F., See,
A., Dathathri, S., Greig, R., Chen, C., Fritz, D., Elias, J.S., Green, R.,
Mokrá, S., Fernando, N., Wu, B., Foley, R., Young, S., Gabriel, I., Isaac,
W., Mellor, J., Hassabis, D., Kavukcuoglu, K., Hendricks, L.A., Irving,
G., 2022. Improving alignment of dialogue agents via targeted human
judgements. arXiv:2209.14375.
Google, 2023. An important next step on our ai journey. URL: https:
//blog.google/technology/ai/bard-google-ai-search-updates/.
GoogleDeepMind, 2023. Ai principles 2023 progress update. URL: https:
//ai.google/static/documents/ai-principles-2023-progress-update.
pdf.
Government,
U.,
2023.
International
scientific
re-
port
on
the
safety
of
advanced
ai:
Interim
report.
URL:
https://www.gov.uk/government/publications/
international-scientific-report-on-the-safety-of-advanced-ai.
interim report.
Goyal, N., Chang, M., Terry, M., 2024. Designing for human-agent align-
ment: Understanding what humans want from their agents, in: Extended
Abstracts of the CHI Conference on Human Factors in Computing Sys-
tems, ACM. URL: http://dx.doi.org/10.1145/3613905.3650948, doi:10.
1145/3613905.3650948.
Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T., Fritz, M.,
2023. Not what you’ve signed up for: Compromising real-world llm-
integrated applications with indirect prompt injection. arXiv:2302.12173.
Gu, Y., Dong, L., Wei, F., Huang, M., 2024. Minillm: Knowledge distilla-
tion of large language models. arXiv:2306.08543.
Guo, Q., Wang, R., Guo, J., Li, B., Song, K., Tan, X., Liu, G., Bian, J.,
Yang, Y., 2024. Connecting large language models with evolutionary
algorithms yields powerful prompt optimizers. arXiv:2309.08532.
Han, X., Shen, A., Cohn, T., Baldwin, T., Frermann, L., 2022. Systematic
evaluation of predictive fairness. URL: https://aclanthology.org/2022.
aacl-main.6/.
Harandizadeh, B., Salinas, A., Morstatter, F., 2024.
Risk and re-
sponse in large language models: Evaluating key threat categories.
arXiv:2403.14988.
He, P., Liu, X., Gao, J., Chen, W., 2020. Deberta: Decoding-enhanced bert
with disentangled attention. arXiv preprint arXiv:2006.03654 .
Hejna, J., Rafailov, R., Sikchi, H., Finn, C., Niekum, S., Knox, W.B.,
Sadigh, D., 2024.
Contrastive preference learning: Learning from
human feedback without rl. URL: https://arxiv.org/abs/2310.13639,
arXiv:2310.13639.
Hejna, J., Sadigh, D., 2022. Few-shot preference learning for human-in-
the-loop rl. URL: https://arxiv.org/abs/2212.03363, arXiv:2212.03363.
Hendrycks, D., Burns, C., Basart, S., Critch, A., Li, J., Song, D., Steinhardt,
J., 2023. Aligning ai with shared human values. arXiv:2008.02275.
Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D., Stein-
hardt, J., 2021. Measuring massive multitask language understanding.
arXiv:2009.03300.
Hendrycks, D., Carlini, N., Schulman, J., Steinhardt, J., 2022. Unsolved
problems in ml safety. arXiv:2109.13916.
Hinton, G., Vinyals, O., Dean, J., 2015. Distilling the knowledge in a neural
network. arXiv:1503.02531.
Ho, N., Schmid, L., Yun, S.Y., 2023.
Large language models are rea-
soning teachers, in: Rogers, A., Boyd-Graber, J., Okazaki, N. (Eds.),
Proceedings of the 61st Annual Meeting of the Association for Com-
putational Linguistics (Volume 1: Long Papers), Association for Com-
putational Linguistics, Toronto, Canada. pp. 14852–14882. URL: https:
//aclanthology.org/2023.acl-long.830, doi:10.18653/v1/2023.acl-long.
830.
Hoffmann, J., Borgeaud, S., Mensch, A., Buchatskaya, E., Cai, T., Ruther-
ford, E., de Las Casas, D., Hendricks, L.A., Welbl, J., Clark, A.,
Hennigan, T., Noland, E., Millican, K., van den Driessche, G., Damoc,
B., Guy, A., Osindero, S., Simonyan, K., Elsen, E., Rae, J.W., Vinyals,
O., Sifre, L., 2022. Training compute-optimal large language models.
arXiv:2203.15556.
Hong, G., Kim, J., Kang, J., Myaeng, S.H., Whang, J.J., 2024.
Why
so gullible? enhancing the robustness of retrieval-augmented models
against counterfactual noise. arXiv:2305.01579.
Houlsby, N., Giurgiu, A., Jastrzebski, S., Morrone, B., de Laroussilhe,
Q., Gesmundo, A., Attariyan, M., Gelly, S., 2019. Parameter-efficient
transfer learning for nlp.
URL: https://arxiv.org/abs/1902.00751,
arXiv:1902.00751.
Howard, J., Ruder, S., 2018.
Universal language model fine-tuning for
text classification, in: Gurevych, I., Miyao, Y. (Eds.), Proceedings of the
56th Annual Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers), Association for Computational Linguistics,
Melbourne, Australia. pp. 328–339. URL: https://aclanthology.org/
P18-1031, doi:10.18653/v1/P18-1031.
Hsieh, C.J., Si, S., Yu, F.X., Dhillon, I.S., 2023a.
Automatic engi-
neering of long prompts.
URL: https://arxiv.org/abs/2311.10117,
arXiv:2311.10117.
Hsieh, C.Y., Li, C.L., Yeh, C.K., Nakhost, H., Fujii, Y., Ratner, A., Krishna,
R., Lee, C.Y., Pfister, T., 2023b. Distilling step-by-step! outperforming
larger language models with less training data and smaller model sizes.
arXiv:2305.02301.
Huang, H., Li, Y., Sun, H., Bai, Y., Gao, Y., 2024a.
How far can
in-context alignment go? exploring the state of in-context alignment.
arXiv:2406.11474.
Huang, J., Chang, K.C.C., 2023a. Towards reasoning in large language
models: A survey, in: Rogers, A., Boyd-Graber, J., Okazaki, N. (Eds.),
Findings of the Association for Computational Linguistics: ACL 2023,
Association for Computational Linguistics, Toronto, Canada. pp. 1049–
1065.
URL: https://aclanthology.org/2023.findings-acl.67, doi:10.
18653/v1/2023.findings-acl.67.
Huang, J., Chang, K.C.C., 2023b. Towards reasoning in large language
models: A survey. arXiv:2212.10403.
Huang, J., Chen, X., Mishra, S., Zheng, H.S., Yu, A.W., Song, X., Zhou,
D., 2024b. Large language models cannot self-correct reasoning yet.
arXiv:2310.01798.
Huang, Q., Wake, N., Sarkar, B., Durante, Z., Gong, R., Taori, R., Noda, Y.,
Terzopoulos, D., Kuno, N., Famoti, A., Llorens, A., Langford, J., Vo, H.,
Fei-Fei, L., Ikeuchi, K., Gao, J., 2024c. Position paper: Agent ai towards
a holistic intelligence. arXiv:2403.00833.
Huang, X., Ruan, W., Huang, W., Jin, G., Dong, Y., Wu, C., Bensalem,
S., Mu, R., Qi, Y., Zhao, X., Cai, K., Zhang, Y., Wu, S., Xu, P.,
Wu, D., Freitas, A., Mustafa, M.A., 2023a.
A survey of safety and
trustworthiness of large language models through the lens of verification
and validation. arXiv:2305.11391.
Huang, Y., Song, J., Wang, Z., Zhao, S., Chen, H., Juefei-Xu, F., Ma, L.,
2023b.
Look before you leap: An exploratory study of uncertainty
measurement for large language models. arXiv:2307.10236.
Iyer, S., Lin, X.V., Pasunuru, R., Mihaylov, T., Simig, D., Yu, P., Shuster, K.,
Wang, T., Liu, Q., Koura, P.S., et al., 2022. Opt-iml: Scaling language
model instruction meta learning through the lens of generalization.
arXiv preprint arXiv:2212.12017 .
Ji, J., Qiu, T., Chen, B., Zhang, B., Lou, H., Wang, K., Duan, Y., He, Z.,
Zhou, J., Zhang, Z., Zeng, F., Ng, K.Y., Dai, J., Pan, X., O’Gara, A.,
Lei, Y., Xu, H., Tse, B., Fu, J., McAleer, S., Yang, Y., Wang, Y., Zhu,
S.C., Guo, Y., Gao, W., 2023. Ai alignment: A comprehensive survey.
URL: https://arxiv.org/abs/2310.19852.
Ji, J., Qiu, T., Chen, B., Zhang, B., Lou, H., Wang, K., Duan, Y., He, Z.,
Zhou, J., Zhang, Z., Zeng, F., Ng, K.Y., Dai, J., Pan, X., O’Gara, A.,
Lei, Y., Xu, H., Tse, B., Fu, J., McAleer, S., Yang, Y., Wang, Y., Zhu,
S.C., Guo, Y., Gao, W., 2024. Ai alignment: A comprehensive survey.
arXiv:2310.19852.
Jiang, R., Chen, K., Bai, X., He, Z., Li, J., Yang, M., Zhao, T., Nie,
L., Zhang, M., 2024.
A survey on human preference learning
for large language models.
URL: https://arxiv.org/abs/2406.11191,
arXiv:2406.11191.
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 28 of 34

--- Page 30 ---

AI Safety in Generative AI Large Language Models: A Survey
Jin, F., Liu, Y., Tan, Y., 2024a. Zero-shot chain-of-thought reasoning guided
by evolutionary algorithms in large language models. arXiv:2402.05376.
Jin, H., Son, S., Park, J., Kim, Y., Noh, H., Lee, Y., 2024b.
Align-to-
distill: Trainable attention alignment for knowledge distillation in neural
machine translation. arXiv:2403.01479.
Joshi, P., Santy, S., Budhiraja, A., Bali, K., Choudhury, M., 2020. The state
and fate of linguistic diversity and inclusion in the nlp world. arXiv
preprint arXiv:2004.09095 .
Kakade, S., Langford, J., 2002.
Approximately optimal approximate
reinforcement learning, in: Proceedings of the Nineteenth International
Conference on Machine Learning, Morgan Kaufmann Publishers Inc.,
San Francisco, CA, USA. p. 267–274.
Kalavasis, A., Karbasi, A., Oikonomou, A., Sotiraki, K., Velegkas, G., Zam-
petakis, M., 2024. Injecting undetectable backdoors in deep learning and
language models. arXiv:2406.05660.
Kalpakchi, D., Boye, J., 2023. Swectrl-mini: a data-transparent transformer-
based large language model for controllable text generation in swedish.
arXiv preprint arXiv:2304.13994 .
Kang, M., Lee, S., Baek, J., Kawaguchi, K., Hwang, S.J., 2023.
Knowledge-augmented reasoning distillation for small language models
in knowledge-intensive tasks. arXiv:2305.18395.
Kaplan, J., McCandlish, S., Henighan, T., Brown, T.B., Chess, B., Child,
R., Gray, S., Radford, A., Wu, J., Amodei, D., 2020. Scaling laws for
neural language models. arXiv:2001.08361.
Kasirzadeh, A., Gabriel, I., 2022. In conversation with artificial intelli-
gence: aligning language models with human values. arXiv:2209.00731.
Kassner, N., Schütze, H., 2019.
Negated and misprimed probes for
pretrained language models: Birds can talk, but cannot fly. arXiv preprint
arXiv:1911.03343 .
Kenton, Z., Everitt, T., Weidinger, L., Gabriel, I., Mikulik, V., Irving, G.,
2021. Alignment of language agents. arXiv preprint arXiv:2103.14659
.
Khatri, C., Hedayatnia, B., Goel, R., Venkatesh, A., Gabriel, R., Mandal, A.,
2018. Detecting offensive content in open-domain conversations using
two stage semi-supervision. arXiv:1811.12900.
Khot, T., Trivedi, H., Finlayson, M., Fu, Y., Richardson, K., Clark, P.,
Sabharwal, A., 2023. Decomposed prompting: A modular approach for
solving complex tasks. arXiv:2210.02406.
Kim, G., Baldi, P., McAleer, S., 2023. Language models can solve computer
tasks. URL: https://arxiv.org/abs/2303.17491, arXiv:2303.17491.
Kim, H.J., Cho, H., Kim, J., Kim, T., Yoo, K.M., Lee, S.g., 2022.
Self-generated in-context learning: Leveraging auto-regressive language
models as a demonstration generator. arXiv preprint arXiv:2206.08082
.
Kirk, H.R., Jun, Y., Volpin, F., Iqbal, H., Benussi, E., Dreyer, F., Shtedritski,
A., Asano, Y., 2021. Bias out-of-the-box: An empirical analysis of inter-
sectional occupational biases in popular generative language models, in:
Ranzato, M., Beygelzimer, A., Dauphin, Y., Liang, P., Vaughan, J.W.
(Eds.), Advances in Neural Information Processing Systems, Curran
Associates, Inc.. pp. 2611–2624. URL: https://proceedings.neurips.
cc/paper/2021/file/1531beb762df4029513ebf9295e0d34f-Paper.pdf.
Kirkpatrick, J., Pascanu, R., Rabinowitz, N., Veness, J., Desjardins, G.,
Rusu, A.A., Milan, K., Quan, J., Ramalho, T., Grabska-Barwinska, A.,
et al., 2017.
Overcoming catastrophic forgetting in neural networks.
Proceedings of the national academy of sciences 114, 3521–3526.
Kocak, B., Yardimci, A.H., Yuzkan, S., Keles, A., Altun, O., Bulut, E.,
Bayrak, O.N., Okumus, A.A., 2022. Transparency in artificial intelli-
gence research: a systematic review of availability items related to open
science in radiology and nuclear medicine. Academic Radiology .
Kojima, T., Gu, S.S., Reid, M., Matsuo, Y., Iwasawa, Y., 2023.
Large
language models are zero-shot reasoners. arXiv:2205.11916.
Kotha, S., Springer, J.M., Raghunathan, A., 2024. Understanding catas-
trophic forgetting in language models via implicit inference.
The
International Conference on Learning Representations (ICLR) .
Kreps, S., McCain, R.M., Brundage, M., 2022. All the news that’s fit to
fabricate: Ai-generated text as a tool of media misinformation. Journal
of Experimental Political Science 9, 104–117. doi:10.1017/XPS.2020.37.
Kung, T.H., Cheatham, M., Medenilla, A., Sillos, C., De Leon, L., Elepaño,
C., Madriaga, M., Aggabao, R., Diaz-Candido, G., Maningo, J., et al.,
2023. Performance of chatgpt on usmle: Potential for ai-assisted medical
education using large language models. PLoS digital health 2, e0000198.
Kurita, K., Belova, A., Anastasopoulos, A., 2019. Towards robust toxic
content classification. arXiv:1912.06872.
Lambert, N., Pyatkin, V., Morrison, J., Miranda, L., Lin, B.Y., Chandu,
K., Dziri, N., Kumar, S., Zick, T., Choi, Y., Smith, N.A., Hajishirzi, H.,
2024. Rewardbench: Evaluating reward models for language modeling.
arXiv:2403.13787.
Lan, Z., Chen, M., Goodman, S., Gimpel, K., Sharma, P., Soricut, R.,
2019.
Albert: A lite bert for self-supervised learning of language
representations. arXiv preprint arXiv:1909.11942 .
Langosco, L., Koch, J., Sharkey, L., Pfau, J., Orseau, L., Krueger,
D., 2023.
Goal misgeneralization in deep reinforcement learning.
arXiv:2105.14111.
Lee, A.N., Hunter, C.J., Ruiz, N., 2023.
Platypus: Quick, cheap, and
powerful refinement of llms. arXiv:2308.07317.
Lester, B., Al-Rfou, R., Constant, N., 2021.
The power of scale for
parameter-efficient prompt tuning. URL: https://arxiv.org/abs/2104.
08691, arXiv:2104.08691.
Lewis, M., Liu, Y., Goyal, N., Ghazvininejad, M., Mohamed, A., Levy,
O., Stoyanov, V., Zettlemoyer, L., 2019. Bart: Denoising sequence-to-
sequence pre-training for natural language generation, translation, and
comprehension. arXiv preprint arXiv:1910.13461 .
Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N.,
Küttler, H., Lewis, M., tau Yih, W., Rocktäschel, T., Riedel, S., Kiela,
D., 2021. Retrieval-augmented generation for knowledge-intensive nlp
tasks. arXiv:2005.11401.
Li, H., Guo, D., Fan, W., Xu, M., Huang, J., Meng, F., Song, Y., 2023a.
Multi-step jailbreaking privacy attacks on chatgpt. arXiv:2304.05197.
Li, J., Wang, S., Zhang, M., Li, W., Lai, Y., Kang, X., Ma, W., Liu, Y., 2024a.
Agent hospital: A simulacrum of hospital with evolvable medical agents.
URL: https://arxiv.org/abs/2405.02957, arXiv:2405.02957.
Li, X.L., Liang, P., 2021. Prefix-tuning: Optimizing continuous prompts for
generation. URL: https://arxiv.org/abs/2101.00190, arXiv:2101.00190.
Li, Y., Du, M., Song, R., Wang, X., Wang, Y., 2024b. A survey on fairness
in large language models.
URL: https://arxiv.org/abs/2308.10149,
arXiv:2308.10149.
Li, Y., Tan, Z., Liu, Y., 2023b. Privacy-preserving prompt tuning for large
language model services. arXiv preprint arXiv:2305.06212 .
Liang, P., Bommasani, R., Lee, T., Tsipras, D., Soylu, D., Yasunaga, M.,
Zhang, Y., Narayanan, D., Wu, Y., Kumar, A., Newman, B., Yuan,
B., Yan, B., Zhang, C., Cosgrove, C., Manning, C.D., Ré, C., Acosta-
Navas, D., Hudson, D.A., Zelikman, E., Durmus, E., Ladhak, F., Rong,
F., Ren, H., Yao, H., Wang, J., Santhanam, K., Orr, L., Zheng, L.,
Yuksekgonul, M., Suzgun, M., Kim, N., Guha, N., Chatterji, N., Khattab,
O., Henderson, P., Huang, Q., Chi, R., Xie, S.M., Santurkar, S., Ganguli,
S., Hashimoto, T., Icard, T., Zhang, T., Chaudhary, V., Wang, W., Li, X.,
Mai, Y., Zhang, Y., Koreeda, Y., 2023. Holistic evaluation of language
models. arXiv:2211.09110.
Liang, P., Bommasani, R., Lee, T., Tsipras, D., Soylu, D., Yasunaga, M.,
Zhang, Y., Narayanan, D., Wu, Y., Kumar, A., et al., 2022.
Holistic
evaluation of language models. arXiv preprint arXiv:2211.09110 .
Lin, B.Y., Ravichander, A., Lu, X., Dziri, N., Sclar, M., Chandu, K.,
Bhagavatula, C., Choi, Y., 2023.
The unlocking spell on base llms:
Rethinking alignment via in-context learning. arXiv:2312.01552.
Lin, C.Y., 2004. Rouge: A package for automatic evaluation of summaries,
in: Text summarization branches out, pp. 74–81.
Lin, S., Hilton, J., Evans, O., 2021. Truthfulqa: Measuring how models
mimic human falsehoods. arXiv preprint arXiv:2109.07958 .
Lipkin, B., Wong, L., Grand, G., Tenenbaum, J.B., 2023.
Evaluating
statistical language models as pragmatic reasoners.
arXiv preprint
arXiv:2305.01020 .
Liu, B., Lane, I., 2018. Adversarial learning of task-oriented neural dialog
models. arXiv:1805.11762.
Liu, C., Kang, Y., Zhao, F., Kuang, K., Jiang, Z., Sun, C., Wu, F., 2024a.
Evolving knowledge distillation with large language models and active
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 29 of 34

--- Page 31 ---

AI Safety in Generative AI Large Language Models: A Survey
learning. arXiv:2403.06414.
Liu, J., Shen, D., Zhang, Y., Dolan, B., Carin, L., Chen, W., 2021.
What makes good in-context examples for gpt-3?
arXiv preprint
arXiv:2101.06804 .
Liu, Y., Deng, G., Li, Y., Wang, K., Wang, Z., Wang, X., Zhang, T., Liu,
Y., Wang, H., Zheng, Y., Liu, Y., 2024b. Prompt injection attack against
llm-integrated applications. arXiv:2306.05499.
Liu, Y., Deng, G., Xu, Z., Li, Y., Zheng, Y., Zhang, Y., Zhao, L., Zhang, T.,
Wang, K., Liu, Y., 2024c. Jailbreaking chatgpt via prompt engineering:
An empirical study. arXiv:2305.13860.
Liu, Y., Ott, M., Goyal, N., Du, J., Joshi, M., Chen, D., Levy, O., Lewis, M.,
Zettlemoyer, L., Stoyanov, V., 2019. Roberta: A robustly optimized bert
pretraining approach. arXiv preprint arXiv:1907.11692 .
Liu, Y., Shen, G., Tao, G., An, S., Ma, S., Zhang, X., 2022.
Piccolo:
Exposing complex backdoors in nlp transformer models, in: 2022 IEEE
Symposium on Security and Privacy (SP), IEEE. pp. 2025–2042.
Liu, Y., Yao, Y., Ton, J.F., Zhang, X., Cheng, R.G.H., Klochkov, Y., Taufiq,
M.F., Li, H., 2023. Trustworthy llms: a survey and guideline for evaluat-
ing large language models’ alignment. arXiv preprint arXiv:2308.05374
.
Liu, Y., Yao, Y., Ton, J.F., Zhang, X., Guo, R., Cheng, H., Klochkov, Y.,
Taufiq, M.F., Li, H., 2024d. Trustworthy llms: a survey and guideline
for evaluating large language models’ alignment. arXiv:2308.05374.
Lu, K., Yu, B., Zhou, C., Zhou, J., 2024.
Large language models are
superpositions of all characters: Attaining arbitrary role-play via self-
alignment. arXiv:2401.12474.
Lu, Y., Bartolo, M., Moore, A., Riedel, S., Stenetorp, P., 2021. Fantastically
ordered prompts and where to find them: Overcoming few-shot prompt
order sensitivity. arXiv preprint arXiv:2104.08786 .
Marwick, A.E., Lewis, R., 2017. Media manipulation and disinformation
online.
Meade, N., Gella, S., Hazarika, D., Gupta, P., Jin, D., Reddy, S., Liu, Y.,
Hakkani-Tür, D., 2023. Using in-context learning to improve dialogue
safety. arXiv:2302.00871.
Mehrabi, N., Morstatter, F., Saxena, N., Lerman, K., Galstyan, A., 2021.
A survey on bias and fairness in machine learning. ACM Computing
Surveys (CSUR) 54, 1–35.
Min, S., Lewis, M., Zettlemoyer, L., Hajishirzi, H., 2021. Metaicl: Learning
to learn in context. arXiv preprint arXiv:2110.15943 .
Mishra, S., Khashabi, D., Baral, C., Hajishirzi, H., 2021.
Cross-task
generalization via natural language crowdsourcing instructions. arXiv
preprint arXiv:2104.08773 .
Mondorf, P., Plank, B., 2024. Beyond accuracy: Evaluating the reasoning
behavior of large language models – a survey. arXiv:2404.01869.
Morris, M.R., Sohl-dickstein, J., Fiedel, N., Warkentin, T., Dafoe, A., Faust,
A., Farabet, C., Legg, S., 2023. Levels of agi: Operationalizing progress
on the path to agi. arXiv:2311.02462.
Muennighoff, N., Wang, T., Sutawika, L., Roberts, A., Biderman, S., Scao,
T.L., Bari, M.S., Shen, S., Yong, Z.X., Schoelkopf, H., et al., 2022.
Crosslingual generalization through multitask finetuning. arXiv preprint
arXiv:2211.01786 .
Nair, A., Gupta, A., Dalal, M., Levine, S., 2021. Awac: Accelerating online
reinforcement learning with offline datasets. URL: https://arxiv.org/
abs/2006.09359, arXiv:2006.09359.
Nangia, N., Vania, C., Bhalerao, R., Bowman, S.R., 2020. Crows-pairs:
A challenge dataset for measuring social biases in masked language
models. arXiv preprint arXiv:2010.00133 .
NewsGuard, 2023.
Misinformation monitor.
URL: https://www.
newsguardtech.com/misinformation-monitor/march-2023/.
Nezhurina, M., Cipolina-Kun, L., Cherti, M., Jitsev, J., 2024.
Alice in
wonderland: Simple tasks showing complete reasoning breakdown in
state-of-the-art large language models. arXiv:2406.02061.
Ngo, R., Chan, L., Mindermann, S., 2023. The alignment problem from a
deep learning perspective. arXiv:2209.00626.
Nishimura-Gasparian, K., Dunn, I., Sleight, H., Turpin, M., Hubinger, E.,
Denison, C., Perez, E., 2024. Reward hacking behavior can generalize
across tasks — ai alignment forum. AI Alignment Forum .
Ognyanova, K., Lazer, D., Robertson, R.E., Wilson, C., 2020. Misinfor-
mation in action: Fake news exposure is linked to lower trust in media,
higher trust in government when your side is in power. Harvard Kennedy
School Misinformation Review .
OpenAI, 2023a. Gpt-4 technical report. arXiv:2303.08774.
OpenAI,
2023b.
Language
models
can
explain
neurons
in
language
models.
URL:
https://openai.com/research/
language-models-can-explain-neurons-in-language-models.
OpenAI,
2023c.
Openai
board
forms
safety
and
se-
curity
committee.
URL:
https://openai.com/index/
openai-board-forms-safety-and-security-committee/.
OpenAI, 2023d.
Openai safety standards.
URL: https://openai.com/
safety-standards/.
OpenAI, 2023e. Openai safety update. URL: https://openai.com/index/
openai-safety-update/.
OpenAI, Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I., Aleman,
F.L., Almeida, D., Altenschmidt, J., Altman, S., Anadkat, S., Avila, R.,
Babuschkin, I., Balaji, S., Balcom, V., Baltescu, P., Bao, H., Bavarian,
M., Belgum, J., Bello, I., Berdine, J., Bernadett-Shapiro, G., Berner,
C., Bogdonoff, L., Boiko, O., Boyd, M., Brakman, A.L., Brockman, G.,
Brooks, T., Brundage, M., Button, K., Cai, T., Campbell, R., Cann, A.,
Carey, B., Carlson, C., Carmichael, R., Chan, B., Chang, C., Chantzis,
F., Chen, D., Chen, S., Chen, R., Chen, J., Chen, M., Chess, B., Cho, C.,
Chu, C., Chung, H.W., Cummings, D., Currier, J., Dai, Y., Decareaux,
C., Degry, T., Deutsch, N., Deville, D., Dhar, A., Dohan, D., Dowling,
S., Dunning, S., Ecoffet, A., Eleti, A., Eloundou, T., Farhi, D., Fedus,
L., Felix, N., Fishman, S.P., Forte, J., Fulford, I., Gao, L., Georges, E.,
Gibson, C., Goel, V., Gogineni, T., Goh, G., Gontijo-Lopes, R., Gordon,
J., Grafstein, M., Gray, S., Greene, R., Gross, J., Gu, S.S., Guo, Y.,
Hallacy, C., Han, J., Harris, J., He, Y., Heaton, M., Heidecke, J., Hesse,
C., Hickey, A., Hickey, W., Hoeschele, P., Houghton, B., Hsu, K., Hu,
S., Hu, X., Huizinga, J., Jain, S., Jain, S., Jang, J., Jiang, A., Jiang,
R., Jin, H., Jin, D., Jomoto, S., Jonn, B., Jun, H., Kaftan, T., Łukasz
Kaiser, Kamali, A., Kanitscheider, I., Keskar, N.S., Khan, T., Kilpatrick,
L., Kim, J.W., Kim, C., Kim, Y., Kirchner, J.H., Kiros, J., Knight, M.,
Kokotajlo, D., Łukasz Kondraciuk, Kondrich, A., Konstantinidis, A.,
Kosic, K., Krueger, G., Kuo, V., Lampe, M., Lan, I., Lee, T., Leike, J.,
Leung, J., Levy, D., Li, C.M., Lim, R., Lin, M., Lin, S., Litwin, M.,
Lopez, T., Lowe, R., Lue, P., Makanju, A., Malfacini, K., Manning, S.,
Markov, T., Markovski, Y., Martin, B., Mayer, K., Mayne, A., McGrew,
B., McKinney, S.M., McLeavey, C., McMillan, P., McNeil, J., Medina,
D., Mehta, A., Menick, J., Metz, L., Mishchenko, A., Mishkin, P.,
Monaco, V., Morikawa, E., Mossing, D., Mu, T., Murati, M., Murk, O.,
Mély, D., Nair, A., Nakano, R., Nayak, R., Neelakantan, A., Ngo, R.,
Noh, H., Ouyang, L., O’Keefe, C., Pachocki, J., Paino, A., Palermo, J.,
Pantuliano, A., Parascandolo, G., Parish, J., Parparita, E., Passos, A.,
Pavlov, M., Peng, A., Perelman, A., de Avila Belbute Peres, F., Petrov,
M., de Oliveira Pinto, H.P., Michael, Pokorny, Pokrass, M., Pong, V.H.,
Powell, T., Power, A., Power, B., Proehl, E., Puri, R., Radford, A., Rae, J.,
Ramesh, A., Raymond, C., Real, F., Rimbach, K., Ross, C., Rotsted, B.,
Roussez, H., Ryder, N., Saltarelli, M., Sanders, T., Santurkar, S., Sastry,
G., Schmidt, H., Schnurr, D., Schulman, J., Selsam, D., Sheppard, K.,
Sherbakov, T., Shieh, J., Shoker, S., Shyam, P., Sidor, S., Sigler, E.,
Simens, M., Sitkin, J., Slama, K., Sohl, I., Sokolowsky, B., Song, Y.,
Staudacher, N., Such, F.P., Summers, N., Sutskever, I., Tang, J., Tezak,
N., Thompson, M.B., Tillet, P., Tootoonchian, A., Tseng, E., Tuggle,
P., Turley, N., Tworek, J., Uribe, J.F.C., Vallone, A., Vijayvergiya, A.,
Voss, C., Wainwright, C., Wang, J.J., Wang, A., Wang, B., Ward, J.,
Wei, J., Weinmann, C., Welihinda, A., Welinder, P., Weng, J., Weng, L.,
Wiethoff, M., Willner, D., Winter, C., Wolrich, S., Wong, H., Workman,
L., Wu, S., Wu, J., Wu, M., Xiao, K., Xu, T., Yoo, S., Yu, K., Yuan,
Q., Zaremba, W., Zellers, R., Zhang, C., Zhang, M., Zhao, S., Zheng,
T., Zhuang, J., Zhuk, W., Zoph, B., 2024.
Gpt-4 technical report.
arXiv:2303.08774.
Ousidhoum, N., Zhao, X., Fang, T., Song, Y., Yeung, D.Y., 2021. Probing
toxic content in large pre-trained language models, in: Proceedings of
the 59th Annual Meeting of the Association for Computational Linguis-
tics and the 11th International Joint Conference on Natural Language
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 30 of 34

--- Page 32 ---

AI Safety in Generative AI Large Language Models: A Survey
Processing (Volume 1: Long Papers), pp. 4262–4274.
Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C.L., Mishkin,
P., Zhang, C., Agarwal, S., Slama, K., Ray, A., et al., 2022. Training
language models to follow instructions with human feedback.
arXiv
preprint arXiv:2203.02155 .
Pan, A., Bhatia, K., Steinhardt, J., 2022. The effects of reward misspecifi-
cation: Mapping and mitigating misaligned models. arXiv:2201.03544.
Pan, X., Zhang, M., Ji, S., Yang, M., 2020. Privacy risks of general-purpose
language models, in: 2020 IEEE Symposium on Security and Privacy
(SP), IEEE. pp. 1314–1331.
Papineni, K., Roukos, S., Ward, T., Zhu, W.J., 2002. Bleu: a method for
automatic evaluation of machine translation, in: Proceedings of the 40th
annual meeting of the Association for Computational Linguistics, pp.
311–318.
Park, S., Frans, K., Levine, S., Kumar, A., 2024. Is value learning really the
main bottleneck in offline rl? arXiv:2406.09329.
Parrish, A., Chen, A., Nangia, N., Padmakumar, V., Phang, J., Thompson,
J., Htut, P.M., Bowman, S.R., 2022. Bbq: A hand-built bias benchmark
for question answering. arXiv:2110.08193.
Paulus, A., Zharmagambetov, A., Guo, C., Amos, B., Tian, Y.,
2024.
Advprompter: Fast adaptive adversarial prompting for llms.
arXiv:2404.16873.
Pavlopoulos, J., Sorensen, J., Dixon, L., Thain, N., Androutsopoulos, I.,
2020. Toxicity detection: Does context really matter? Proceedings of
the Annual Meeting of the Association for Computational Linguistics ,
4296–4305URL: https://arxiv.org/abs/2006.00998v1, doi:10.18653/V1/
2020.ACL-MAIN.396.
Peng, X.B., Kumar, A., Zhang, G., Levine, S., 2019. Advantage-weighted
regression: Simple and scalable off-policy reinforcement learning. URL:
https://arxiv.org/abs/1910.00177, arXiv:1910.00177.
Perez, E., Huang, S., Song, F., Cai, T., Ring, R., Aslanides, J., Glaese, A.,
McAleese, N., Irving, G., 2022a. Red teaming language models with
language models. arXiv:2202.03286.
Perez, E., Ringer, S., Lukoši¯ut˙e, K., Nguyen, K., Chen, E., Heiner, S., Pettit,
C., Olsson, C., Kundu, S., Kadavath, S., Jones, A., Chen, A., Mann,
B., Israel, B., Seethor, B., McKinnon, C., Olah, C., Yan, D., Amodei,
D., Amodei, D., Drain, D., Li, D., Tran-Johnson, E., Khundadze, G.,
Kernion, J., Landis, J., Kerr, J., Mueller, J., Hyun, J., Landau, J.,
Ndousse, K., Goldberg, L., Lovitt, L., Lucas, M., Sellitto, M., Zhang,
M., Kingsland, N., Elhage, N., Joseph, N., Mercado, N., DasSarma,
N., Rausch, O., Larson, R., McCandlish, S., Johnston, S., Kravec, S.,
Showk, S.E., Lanham, T., Telleen-Lawton, T., Brown, T., Henighan, T.,
Hume, T., Bai, Y., Hatfield-Dodds, Z., Clark, J., Bowman, S.R., Askell,
A., Grosse, R., Hernandez, D., Ganguli, D., Hubinger, E., Schiefer, N.,
Kaplan, J., 2022b. Discovering language model behaviors with model-
written evaluations. arXiv:2212.09251.
Press, O., Zhang, M., Min, S., Schmidt, L., Smith, N.A., Lewis, M., 2022.
Measuring and narrowing the compositionality gap in language models.
arXiv preprint arXiv:2210.03350 .
Qi, X., Panda, A., Lyu, K., Ma, X., Roy, S., Beirami, A., Mittal, P.,
Henderson, P., 2024. Safety alignment should be made more than just a
few tokens deep. arXiv:2406.05946.
Qiu, J., Ma, H., Levy, O., Yih, S.W.t., Wang, S., Tang, J., 2019. Block-
wise self-attention for long document understanding.
arXiv preprint
arXiv:1911.02972 .
Radford,
A.,
Narasimhan,
K.,
Salimans,
T.,
Sutskever,
I.,
2018.
Improving language understanding by generative pre-training.
URL:
https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/
language-unsupervised/language_understanding_paper.pdf.
Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., Sutskever, I., et al.,
2019. Language models are unsupervised multitask learners. OpenAI
blog 1, 9.
Rae, J.W., Borgeaud, S., Cai, T., Millican, K., Hoffmann, J., Song, F.,
Aslanides, J., Henderson, S., Ring, R., Young, S., Rutherford, E., Hen-
nigan, T., Menick, J., Cassirer, A., Powell, R., van den Driessche, G.,
Hendricks, L.A., Rauh, M., Huang, P.S., Glaese, A., Welbl, J., Dathathri,
S., Huang, S., Uesato, J., Mellor, J., Higgins, I., Creswell, A., McAleese,
N., Wu, A., Elsen, E., Jayakumar, S., Buchatskaya, E., Budden, D.,
Sutherland, E., Simonyan, K., Paganini, M., Sifre, L., Martens, L.,
Li, X.L., Kuncoro, A., Nematzadeh, A., Gribovskaya, E., Donato, D.,
Lazaridou, A., Mensch, A., Lespiau, J.B., Tsimpoukelli, M., Grigorev,
N., Fritz, D., Sottiaux, T., Pajarskas, M., Pohlen, T., Gong, Z., Toyama,
D., de Masson d’Autume, C., Li, Y., Terzi, T., Mikulik, V., Babuschkin,
I., Clark, A., de Las Casas, D., Guy, A., Jones, C., Bradbury, J., Johnson,
M., Hechtman, B., Weidinger, L., Gabriel, I., Isaac, W., Lockhart, E.,
Osindero, S., Rimell, L., Dyer, C., Vinyals, O., Ayoub, K., Stanway, J.,
Bennett, L., Hassabis, D., Kavukcuoglu, K., Irving, G., 2022. Scaling
language models: Methods, analysis & insights from training gopher.
arXiv:2112.11446.
Rafailov, R., Sharma, A., Mitchell, E., Ermon, S., Manning, C.D., Finn, C.,
2023. Direct preference optimization: Your language model is secretly
a reward model. arXiv:2305.18290.
Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., Zhou,
Y., Li, W., Liu, P.J., 2020. Exploring the limits of transfer learning with
a unified text-to-text transformer.
The Journal of Machine Learning
Research 21, 5485–5551.
Ran, D., Liu, J., Gong, Y., Zheng, J., He, X., Cong, T., Wang, A., 2024.
Jailbreakeval: An integrated toolkit for evaluating jailbreak attempts
against large language models. arXiv:2406.09321.
Raza, S., Bamgbose, O., Ghuge, S., Reji, D.J., 2024. Safe and responsible
large language model development. arXiv:2404.01399.
Rebedea, T., Dinu, R., Sreedhar, M., Parisien, C., Cohen, J., 2023. Nemo
guardrails: A toolkit for controllable and safe llm applications with
programmable rails. arXiv:2310.10501.
Rubin, O., Herzig, J., Berant, J., 2021. Learning to retrieve prompts for
in-context learning. arXiv preprint arXiv:2112.08633 .
Sanh, V., Debut, L., Chaumond, J., Wolf, T., 2019. Distilbert, a distilled
version of bert: smaller, faster, cheaper and lighter.
arXiv preprint
arXiv:1910.01108 .
Sanh, V., Webson, A., Raffel, C., Bach, S.H., Sutawika, L., Alyafeai, Z.,
Chaffin, A., Stiegler, A., Scao, T.L., Raja, A., et al., 2021. Multitask
prompted training enables zero-shot task generalization. arXiv preprint
arXiv:2110.08207 .
Scao, T.L., Fan, A., Akiki, C., Pavlick, E., Ilić, S., Hesslow, D., Castagné,
R., Luccioni, A.S., Yvon, F., Gallé, M., et al., 2022. Bloom: A 176b-
parameter open-access multilingual language model.
arXiv preprint
arXiv:2211.05100 .
Schaeffer, R., Miranda, B., Koyejo, S., 2023. Are emergent abilities of large
language models a mirage? arXiv preprint arXiv:2304.15004 .
Schick, T., Udupa, S., Schütze, H., 2021. Self-diagnosis and self-debiasing:
A proposal for reducing corpus-based bias in nlp. Transactions of the
Association for Computational Linguistics 9, 1408–1424.
Schiller, C.A., 2024. The human factor in detecting errors of large language
models: A systematic literature review and future research directions.
arXiv:2403.09743.
Schulhoff, S., Ilie, M., Balepur, N., Kahadze, K., Liu, A., Si, C., Li, Y.,
Gupta, A., Han, H., Schulhoff, S., Dulepet, P.S., Vidyadhara, S., Ki, D.,
Agrawal, S., Pham, C., Kroiz, G., Li, F., Tao, H., Srivastava, A., Costa,
H.D., Gupta, S., Rogers, M.L., Goncearenco, I., Sarli, G., Galynker, I.,
Peskoff, D., Carpuat, M., White, J., Anadkat, S., Hoyle, A., Resnik, P.,
2024a. The prompt report: A systematic survey of prompting techniques.
URL: https://arxiv.org/abs/2406.06608, arXiv:2406.06608.
Schulhoff, S., Pinto, J., Khan, A., Bouchard, L.F., Si, C., Anati, S., Tagli-
abue, V., Kost, A.L., Carnahan, C., Boyd-Graber, J., 2024b. Ignore this
title and hackaprompt: Exposing systemic vulnerabilities of llms through
a global scale prompt hacking competition. arXiv:2311.16119.
Schulman, J., Levine, S., Moritz, P., Jordan, M.I., Abbeel, P., 2017a. Trust
region policy optimization.
URL: https://arxiv.org/abs/1502.05477,
arXiv:1502.05477.
Schulman, J., Wolski, F., Dhariwal, P., Radford, A., Klimov, O., 2017b.
Proximal policy optimization algorithms. URL: https://arxiv.org/abs/
1707.06347, arXiv:1707.06347.
Scialom, T., Chakrabarty, T., Muresan, S., 2022.
Fine-tuned language
models are continual learners. arXiv preprint arXiv:2205.12393 .
Sellam, T., Das, D., Parikh, A.P., 2020. Bleurt: Learning robust metrics for
text generation. arXiv preprint arXiv:2004.04696 .
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 31 of 34

--- Page 33 ---

AI Safety in Generative AI Large Language Models: A Survey
Shanahan, M., McDonell, K., Reynolds, L., 2023. Role-play with large
language models. arXiv:2305.16367.
Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman,
S.R., Cheng, N., Durmus, E., Hatfield-Dodds, Z., Johnston, S.R., Kravec,
S., Maxwell, T., McCandlish, S., Ndousse, K., Rausch, O., Schiefer, N.,
Yan, D., Zhang, M., Perez, E., 2023. Towards understanding sycophancy
in language models. arXiv:2310.13548.
Shaw, P., Uszkoreit, J., Vaswani, A., 2018.
Self-attention with relative
position representations. arXiv preprint arXiv:1803.02155 .
Shelby, R., Rismani, S., Henne, K., Moon, A., Rostamzadeh, N., Nicholas,
P., Yilla, N., Gallegos, J., Smart, A., Garcia, E., Virk, G., 2023. So-
ciotechnical harms of algorithmic systems: Scoping a taxonomy for
harm reduction. arXiv:2210.05791.
Shen, H., Knearem, T., Ghosh, R., Alkiek, K., Krishna, K., Liu, Y., Ma, Z.,
Petridis, S., Peng, Y.H., Qiwei, L., Rakshit, S., Si, C., Xie, Y., Bigham,
J.P., Bentley, F., Chai, J., Lipton, Z., Mei, Q., Mihalcea, R., Terry,
M., Yang, D., Morris, M.R., Resnick, P., Jurgens, D., 2024. Towards
bidirectional human-ai alignment: A systematic review for clarifications,
framework, and future directions. arXiv:2406.09264.
Shen, S., Hou, L., Zhou, Y., Du, N., Longpre, S., Wei, J., Chung, H.W.,
Zoph, B., Fedus, W., Chen, X., Vu, T., Wu, Y., Chen, W., Webson,
A., Li, Y., Zhao, V., Yu, H., Keutzer, K., Darrell, T., Zhou, D., 2023a.
Mixture-of-experts meets instruction tuning:a winning combination for
large language models. arXiv:2305.14705.
Shen, T., Jin, R., Huang, Y., Liu, C., Dong, W., Guo, Z., Wu, X., Liu,
Y., Xiong, D., 2023b.
Large language model alignment: A survey.
arXiv:2309.15025.
Shen, Y., Tobia, M.J., Sommer, T., Obermayer, K., 2014. Risk-sensitive
reinforcement learning.
Neural Computation 26, 1298–1328.
URL:
http://dx.doi.org/10.1162/NECO_a_00600, doi:10.1162/neco_a_00600.
Shevlane, T., Farquhar, S., Garfinkel, B., Phuong, M., Whittlestone, J.,
Leung, J., Kokotajlo, D., Marchal, N., Anderljung, M., Kolt, N., Ho, L.,
Siddarth, D., Avin, S., Hawkins, W., Kim, B., Gabriel, I., Bolina, V.,
Clark, J., Bengio, Y., Christiano, P., Dafoe, A., 2023. Model evaluation
for extreme risks. arXiv:2305.15324.
Shimanaka, H., Kajiwara, T., Komachi, M., 2018. Ruse: Regressor using
sentence embeddings for automatic machine translation evaluation, in:
Proceedings of the Third Conference on Machine Translation: Shared
Task Papers, pp. 751–758.
Shridhar, K., Stolfo, A., Sachan, M., 2023. Distilling reasoning capabilities
into smaller language models. arXiv:2212.00193.
Singh, S., Abri, F., Namin, A.S., 2023.
Exploiting large language
models (llms) through deception techniques and persuasion principles.
arXiv:2311.14876.
Skalse, J., Howe, N.H.R., Krasheninnikov, D., Krueger, D., 2022. Defining
and characterizing reward hacking. arXiv:2209.13085.
Solaiman, I., Brundage, M., Clark, J., Askell, A., Herbert-Voss, A., Wu, J.,
Radford, A., Krueger, G., Kim, J.W., Kreps, S., et al., 2019. Release
strategies and the social impacts of language models. arXiv preprint
arXiv:1908.09203 .
Solaiman, I., Talat, Z., Agnew, W., Ahmad, L., Baker, D., Blodgett, S.L.,
au2, H.D.I., Dodge, J., Evans, E., Hooker, S., Jernite, Y., Luccioni, A.S.,
Lusoli, A., Mitchell, M., Newman, J., Png, M.T., Strait, A., Vassilev, A.,
2023. Evaluating the social impact of generative ai systems in systems
and society. arXiv:2306.05949.
Song, C., Raghunathan, A., 2020.
Information leakage in embedding
models, in: Proceedings of the 2020 ACM SIGSAC conference on
computer and communications security, pp. 377–390.
Song, Y., Swamy, G., Singh, A., Bagnell, J.A., Sun, W., 2024.
Under-
standing preference fine-tuning through the lens of coverage.
URL:
https://arxiv.org/abs/2406.01462, arXiv:2406.01462.
Srivastava, A., Rastogi, A., Rao, A., Shoeb, A.A.M., Abid, A., Fisch,
A., Brown, A.R., Santoro, A., Gupta, A., Garriga-Alonso, A., Kluska,
A., Lewkowycz, A., Agarwal, A., Power, A., Ray, A., Warstadt, A.,
Kocurek, A.W., Safaya, A., Tazarv, A., Xiang, A., Parrish, A., Nie, A.,
Hussain, A., Askell, A., Dsouza, A., Slone, A., Rahane, A., Iyer, A.S.,
Andreassen, A., Madotto, A., Santilli, A., Stuhlmüller, A., Dai, A., La,
A., Lampinen, A., Zou, A., Jiang, A., Chen, A., Vuong, A., Gupta, A.,
Gottardi, A., Norelli, A., Venkatesh, A., Gholamidavoodi, A., Tabassum,
A., Menezes, A., Kirubarajan, A., Mullokandov, A., Sabharwal, A.,
Herrick, A., Efrat, A., Erdem, A., Karakaş, A., Roberts, B.R., Loe, B.S.,
Zoph, B., Bojanowski, B., Özyurt, B., Hedayatnia, B., Neyshabur, B.,
Inden, B., Stein, B., Ekmekci, B., Lin, B.Y., Howald, B., Orinion, B.,
Diao, C., Dour, C., Stinson, C., Argueta, C., Ramírez, C.F., Singh, C.,
Rathkopf, C., Meng, C., Baral, C., Wu, C., Callison-Burch, C., Waites,
C., Voigt, C., Manning, C.D., Potts, C., Ramirez, C., Rivera, C.E.,
Siro, C., Raffel, C., Ashcraft, C., Garbacea, C., Sileo, D., Garrette, D.,
Hendrycks, D., Kilman, D., Roth, D., Freeman, D., Khashabi, D., Levy,
D., González, D.M., Perszyk, D., Hernandez, D., Chen, D., Ippolito, D.,
Gilboa, D., Dohan, D., Drakard, D., Jurgens, D., Datta, D., Ganguli,
D., Emelin, D., Kleyko, D., Yuret, D., Chen, D., Tam, D., Hupkes,
D., Misra, D., Buzan, D., Mollo, D.C., Yang, D., Lee, D.H., Schrader,
D., Shutova, E., Cubuk, E.D., Segal, E., Hagerman, E., Barnes, E.,
Donoway, E., Pavlick, E., Rodola, E., Lam, E., Chu, E., Tang, E., Erdem,
E., Chang, E., Chi, E.A., Dyer, E., Jerzak, E., Kim, E., Manyasi, E.E.,
Zheltonozhskii, E., Xia, F., Siar, F., Martínez-Plumed, F., Happé, F.,
Chollet, F., Rong, F., Mishra, G., Winata, G.I., de Melo, G., Kruszewski,
G., Parascandolo, G., Mariani, G., Wang, G., Jaimovitch-López, G.,
Betz, G., Gur-Ari, G., Galijasevic, H., Kim, H., Rashkin, H., Hajishirzi,
H., Mehta, H., Bogar, H., Shevlin, H., Schütze, H., Yakura, H., Zhang,
H., Wong, H.M., Ng, I., Noble, I., Jumelet, J., Geissinger, J., Kernion,
J., Hilton, J., Lee, J., Fisac, J.F., Simon, J.B., Koppel, J., Zheng, J., Zou,
J., Kocoń, J., Thompson, J., Wingfield, J., Kaplan, J., Radom, J., Sohl-
Dickstein, J., Phang, J., Wei, J., Yosinski, J., Novikova, J., Bosscher, J.,
Marsh, J., Kim, J., Taal, J., Engel, J., Alabi, J., Xu, J., Song, J., Tang, J.,
Waweru, J., Burden, J., Miller, J., Balis, J.U., Batchelder, J., Berant, J.,
Frohberg, J., Rozen, J., Hernandez-Orallo, J., Boudeman, J., Guerr, J.,
Jones, J., Tenenbaum, J.B., Rule, J.S., Chua, J., Kanclerz, K., Livescu,
K., Krauth, K., Gopalakrishnan, K., Ignatyeva, K., Markert, K., Dhole,
K.D., Gimpel, K., Omondi, K., Mathewson, K., Chiafullo, K., Shkaruta,
K., Shridhar, K., McDonell, K., Richardson, K., Reynolds, L., Gao, L.,
Zhang, L., Dugan, L., Qin, L., Contreras-Ochando, L., Morency, L.P.,
Moschella, L., Lam, L., Noble, L., Schmidt, L., He, L., Colón, L.O.,
Metz, L., Şenel, L.K., Bosma, M., Sap, M., ter Hoeve, M., Farooqi,
M., Faruqui, M., Mazeika, M., Baturan, M., Marelli, M., Maru, M.,
Quintana, M.J.R., Tolkiehn, M., Giulianelli, M., Lewis, M., Potthast, M.,
Leavitt, M.L., Hagen, M., Schubert, M., Baitemirova, M.O., Arnaud, M.,
McElrath, M., Yee, M.A., Cohen, M., Gu, M., Ivanitskiy, M., Starritt,
M., Strube, M., Swędrowski, M., Bevilacqua, M., Yasunaga, M., Kale,
M., Cain, M., Xu, M., Suzgun, M., Walker, M., Tiwari, M., Bansal,
M., Aminnaseri, M., Geva, M., Gheini, M., T, M.V., Peng, N., Chi,
N.A., Lee, N., Krakover, N.G.A., Cameron, N., Roberts, N., Doiron,
N., Martinez, N., Nangia, N., Deckers, N., Muennighoff, N., Keskar,
N.S., Iyer, N.S., Constant, N., Fiedel, N., Wen, N., Zhang, O., Agha,
O., Elbaghdadi, O., Levy, O., Evans, O., Casares, P.A.M., Doshi, P.,
Fung, P., Liang, P.P., Vicol, P., Alipoormolabashi, P., Liao, P., Liang,
P., Chang, P., Eckersley, P., Htut, P.M., Hwang, P., Miłkowski, P., Patil,
P., Pezeshkpour, P., Oli, P., Mei, Q., Lyu, Q., Chen, Q., Banjade, R.,
Rudolph, R.E., Gabriel, R., Habacker, R., Risco, R., Millière, R., Garg,
R., Barnes, R., Saurous, R.A., Arakawa, R., Raymaekers, R., Frank,
R., Sikand, R., Novak, R., Sitelew, R., LeBras, R., Liu, R., Jacobs, R.,
Zhang, R., Salakhutdinov, R., Chi, R., Lee, R., Stovall, R., Teehan,
R., Yang, R., Singh, S., Mohammad, S.M., Anand, S., Dillavou, S.,
Shleifer, S., Wiseman, S., Gruetter, S., Bowman, S.R., Schoenholz, S.S.,
Han, S., Kwatra, S., Rous, S.A., Ghazarian, S., Ghosh, S., Casey, S.,
Bischoff, S., Gehrmann, S., Schuster, S., Sadeghi, S., Hamdan, S., Zhou,
S., Srivastava, S., Shi, S., Singh, S., Asaadi, S., Gu, S.S., Pachchigar,
S., Toshniwal, S., Upadhyay, S., Shyamolima, Debnath, Shakeri, S.,
Thormeyer, S., Melzi, S., Reddy, S., Makini, S.P., Lee, S.H., Torene,
S., Hatwar, S., Dehaene, S., Divic, S., Ermon, S., Biderman, S., Lin, S.,
Prasad, S., Piantadosi, S.T., Shieber, S.M., Misherghi, S., Kiritchenko,
S., Mishra, S., Linzen, T., Schuster, T., Li, T., Yu, T., Ali, T., Hashimoto,
T., Wu, T.L., Desbordes, T., Rothschild, T., Phan, T., Wang, T., Nkinyili,
T., Schick, T., Kornev, T., Tunduny, T., Gerstenberg, T., Chang, T.,
Neeraj, T., Khot, T., Shultz, T., Shaham, U., Misra, V., Demberg, V.,
Nyamai, V., Raunak, V., Ramasesh, V., Prabhu, V.U., Padmakumar, V.,
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 32 of 34

--- Page 34 ---

AI Safety in Generative AI Large Language Models: A Survey
Srikumar, V., Fedus, W., Saunders, W., Zhang, W., Vossen, W., Ren, X.,
Tong, X., Zhao, X., Wu, X., Shen, X., Yaghoobzadeh, Y., Lakretz, Y.,
Song, Y., Bahri, Y., Choi, Y., Yang, Y., Hao, Y., Chen, Y., Belinkov,
Y., Hou, Y., Hou, Y., Bai, Y., Seid, Z., Zhao, Z., Wang, Z., Wang, Z.J.,
Wang, Z., Wu, Z., 2023. Beyond the imitation game: Quantifying and
extrapolating the capabilities of language models. arXiv:2206.04615.
Stanton, S., Izmailov, P., Kirichenko, P., Alemi, A.A., Wilson, A.G., 2021.
Does knowledge distillation really work? arXiv:2106.05945.
Stiennon, N., Ouyang, L., Wu, J., Ziegler, D.M., Lowe, R., Voss, C.,
Radford, A., Amodei, D., Christiano, P., 2022. Learning to summarize
from human feedback. arXiv:2009.01325.
Su, J., Lu, Y., Pan, S., Murtadha, A., Wen, B., Liu, Y., 2021. Roformer:
Enhanced transformer with rotary position embedding. arXiv preprint
arXiv:2104.09864 .
Sun, Y., Chia, S.C., Lu, F., Oktavianus, J., 2022. The battle is on: Factors
that motivate people to combat anti-vaccine misinformation.
Health
Communication 37, 327–336.
Sun, Z., Shen, Y., Zhou, Q., Zhang, H., Chen, Z., Cox, D., Yang, Y., Gan, C.,
2023. Principle-driven self-alignment of language models from scratch
with minimal human supervision. arXiv:2305.03047.
Sutton, R.S., McAllester, D., Singh, S., Mansour, Y., 1999.
Policy
gradient
methods
for
reinforcement
learning
with
function
approximation, in: Solla, S., Leen, T., Müller, K. (Eds.), Advances
in Neural Information Processing Systems, MIT Press.
URL:
https://proceedings.neurips.cc/paper_files/paper/1999/file/
464d828b85b0bed98e80ade0a5c43b0f-Paper.pdf.
Tajwar, F., Singh, A., Sharma, A., Rafailov, R., Schneider, J., Xie, T.,
Ermon, S., Finn, C., Kumar, A., 2024. Preference fine-tuning of llms
should leverage suboptimal, on-policy data. URL: https://arxiv.org/
abs/2404.14367, arXiv:2404.14367.
Tamkin, A., Brundage, M., Clark, J., Ganguli, D., 2021. Understanding the
capabilities, limitations, and societal impact of large language models.
arXiv preprint arXiv:2102.02503 .
Tay, Y., Dehghani, M., Tran, V.Q., Garcia, X., Wei, J., Wang, X., Chung,
H.W., Shakeri, S., Bahri, D., Schuster, T., Zheng, H.S., Zhou, D.,
Houlsby, N., Metzler, D., 2023.
Ul2: Unifying language learning
paradigms. arXiv:2205.05131.
Tay, Y., Wei, J., Chung, H.W., Tran, V.Q., So, D.R., Shakeri, S., Garcia, X.,
Zheng, H.S., Rao, J., Chowdhery, A., et al., 2022. Transcending scaling
laws with 0.1% extra compute. arXiv preprint arXiv:2210.11399 .
Thoppilan, R., De Freitas, D., Hall, J., Shazeer, N., Kulshreshtha, A., Cheng,
H.T., Jin, A., Bos, T., Baker, L., Du, Y., et al., 2022. Lamda: Language
models for dialog applications. arXiv preprint arXiv:2201.08239 .
THUDM, 2023.
Chatglm-6b.
URL: https://huggingface.co/THUDM/
chatglm-6b.
Touvron, H., Lavril, T., Izacard, G., Martinet, X., Lachaux, M.A., Lacroix,
T., Rozière, B., Goyal, N., Hambro, E., Azhar, F., et al., 2023. Llama:
Open and efficient foundation language models.
arXiv preprint
arXiv:2302.13971 .
Tunstall, L., Beeching, E., Lambert, N., Rajani, N., Rasul, K., Belkada,
Y., Huang, S., von Werra, L., Fourrier, C., Habib, N., Sarrazin, N.,
Sanseviero, O., Rush, A.M., Wolf, T., 2023. Zephyr: Direct distillation
of lm alignment. arXiv:2310.16944.
Valmeekam, K., Olmo, A., Sreedharan, S., Kambhampati, S., 2022. Large
language models still can’t plan (a benchmark for llms on planning and
reasoning about change). arXiv preprint arXiv:2206.10498 .
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N.,
Kaiser, Ł., Polosukhin, I., 2017. Attention is all you need. Advances in
neural information processing systems 30.
Wallace, E., Feng, S., Kandpal, N., Gardner, M., Singh, S., 2021a. Universal
adversarial triggers for attacking and analyzing nlp. arXiv:1908.07125.
Wallace, E., Zhao, T.Z., Feng, S., Singh, S., 2021b.
Concealed data
poisoning attacks on nlp models. URL: https://arxiv.org/abs/2010.
12563, arXiv:2010.12563.
Wang, J., Wang, J., Athiwaratkun, B., Zhang, C., Zou, J., 2024a. Mixture-
of-agents enhances large language model capabilities. arXiv:2406.04692.
Wang, L., Zhang, X., Su, H., Zhu, J., 2024b. A comprehensive survey of
continual learning: Theory, method and application. IEEE Transactions
on Pattern Analysis and Machine Intelligence .
Wang, R., Milani, S., Chiu, J.C., Zhi, J., Eack, S.M., Labrum, T., Murphy,
S.M., Jones, N., Hardy, K., Shen, H., Fang, F., Chen, Z.Z., 2024c.
Patient-𝑃𝑠𝑖: Using large language models to simulate patients for train-
ing mental health professionals. arXiv:2405.19660.
Wang, S., Li, B.Z., Khabsa, M., Fang, H., Ma, H., 2020. Linformer: Self-
attention with linear complexity. arXiv preprint arXiv:2006.04768 .
Wang, X., Chen, T., Yang, X., Zhang, Q., Zhao, X., Lin, D., 2024d.
Unveiling the misuse potential of base large language models via in-
context learning. arXiv:2404.10552.
Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., Chowdhery,
A., Zhou, D., 2023a.
Self-consistency improves chain of thought
reasoning in language models. URL: https://arxiv.org/abs/2203.11171,
arXiv:2203.11171.
Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., Chowdhery,
A., Zhou, D., 2023b.
Self-consistency improves chain of thought
reasoning in language models. arXiv:2203.11171.
Wang, Y., Kordi, Y., Mishra, S., Liu, A., Smith, N.A., Khashabi, D.,
Hajishirzi, H., 2022. Self-instruct: Aligning language model with self
generated instructions. arXiv preprint arXiv:2212.10560 .
Wang, Y., Wu, Y., Wei, Z., Jegelka, S., Wang, Y., 2024e. A theoretical
understanding of self-correction through in-context alignment. URL:
https://arxiv.org/abs/2405.18634, arXiv:2405.18634.
Wang, Y., Zhong, W., Li, L., Mi, F., Zeng, X., Huang, W., Shang, L., Jiang,
X., Liu, Q., 2023c.
Aligning large language models with human: A
survey. arXiv:2307.12966.
Wang, Z., Dong, Y., Delalleau, O., Zeng, J., Shen, G., Egert, D., Zhang, J.J.,
Sreedhar, M.N., Kuchaiev, O., 2024f. Helpsteer2: Open-source dataset
for training top-performing reward models. arXiv:2406.08673.
Wang, Z., Panda, R., Karlinsky, L., Feris, R., Sun, H., Kim, Y., 2023d.
Multitask prompt tuning enables parameter-efficient transfer learning.
URL: https://arxiv.org/abs/2303.02861, arXiv:2303.02861.
Webb, T., Holyoak, K.J., Lu, H., 2023. Emergent analogical reasoning in
large language models. arXiv:2212.09196.
Wei, J., Hou, L., Lampinen, A., Chen, X., Huang, D., Tay, Y., Chen, X., Lu,
Y., Zhou, D., Ma, T., et al., 2023a. Symbol tuning improves in-context
learning in language models. arXiv preprint arXiv:2305.08298 .
Wei, J., Huang, D., Lu, Y., Zhou, D., Le, Q.V., 2024. Simple synthetic data
reduces sycophancy in large language models. arXiv:2308.03958.
Wei, J., Tay, Y., Bommasani, R., Raffel, C., Zoph, B., Borgeaud, S.,
Yogatama, D., Bosma, M., Zhou, D., Metzler, D., Chi, E.H., Hashimoto,
T., Vinyals, O., Liang, P., Dean, J., Fedus, W., 2022a. Emergent abilities
of large language models. arXiv:2206.07682.
Wei, J., Wang, X., Schuurmans, D., Bosma, M., Chi, E., Le, Q., Zhou, D.,
2022b. Chain of thought prompting elicits reasoning in large language
models. arXiv preprint arXiv:2201.11903 .
Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E.,
Le, Q., Zhou, D., 2023b. Chain-of-thought prompting elicits reasoning
in large language models. arXiv:2201.11903.
Weidinger, L., Barnhart, J., Brennan, J., Butterfield, C., Young, S., Hawkins,
W., Hendricks, L.A., Comanescu, R., Chang, O., Rodriguez, M., et al.,
2024a.
Holistic safety and responsibility evaluations of advanced ai
models. arXiv preprint arXiv:2404.14068 .
Weidinger, L., Mellor, J., Pegueroles, B.G., Marchal, N., Kumar, R., Lum,
K., Akbulut, C., Diaz, M., Bergman, S., Rodriguez, M., Rieser, V.,
Isaac, W., 2024b. Star: Sociotechnical approach to red teaming language
models. arXiv:2406.11757.
Weidinger, L., Mellor, J., Rauh, M., Griffin, C., Uesato, J., Huang, P.S.,
Cheng, M., Glaese, M., Balle, B., Kasirzadeh, A., et al., 2021.
Eth-
ical and social risks of harm from language models.
arXiv preprint
arXiv:2112.04359 .
Weidinger, L., Uesato, J., Rauh, M., Griffin, C., Huang, P.S., Mellor, J.,
Glaese, A., Cheng, M., Balle, B., Kasirzadeh, A., et al., 2022. Taxonomy
of risks posed by language models, in: 2022 ACM Conference on
Fairness, Accountability, and Transparency, pp. 214–229.
Welbl, J., Glaese, A., Uesato, J., Dathathri, S., Mellor, J., Hendricks, L.A.,
Anderson, K., Kohli, P., Coppin, B., Huang, P.S., 2021. Challenges in
detoxifying language models. arXiv preprint arXiv:2109.07445 .
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 33 of 34

--- Page 35 ---

AI Safety in Generative AI Large Language Models: A Survey
Weng, L., 2021. Reducing toxicity in language models. lilianweng.github.io
URL: https://lilianweng.github.io/posts/2021-03-21-lm-toxicity/.
WhiteHouse,
.
Ensuring
safe,
secure,
and
trustworthy
ai.
URL:
https://www.whitehouse.gov/wp-content/uploads/2023/07/
Ensuring-Safe-Secure-and-TrustworthyAI.pdf.
Wu, T., Terry, M., Cai, C.J., 2022. Ai chains: Transparent and controllable
human-ai interaction by chaining large language model prompts, in: Pro-
ceedings of the 2022 CHI Conference on Human Factors in Computing
Systems, pp. 1–22.
Wu, Y., Schuster, M., Chen, Z., Le, Q.V., Norouzi, M., Macherey, W.,
Krikun, M., Cao, Y., Gao, Q., Macherey, K., et al., 2016.
Google’s
neural machine translation system: Bridging the gap between human and
machine translation. arXiv preprint arXiv:1609.08144 .
Yang, J., Jin, H., Tang, R., Han, X., Feng, Q., Jiang, H., Yin, B., Hu, X.,
2023. Harnessing the power of llms in practice: A survey on chatgpt
and beyond. arXiv preprint arXiv:2304.13712 .
Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T.L., Cao, Y., Narasimhan,
K., 2023.
Tree of thoughts: Deliberate problem solving with large
language models. arXiv:2305.10601.
Ye, C., Hu, Z., Deng, Y., Huang, Z., Ma, M.D., Zhu, Y., Wang, W., 2024.
Mirai: Evaluating llm agents for event forecasting. URL: https://arxiv.
org/abs/2407.01231, arXiv:2407.01231.
Ye, J., Mao, Y., Song, J., Wang, X., Jin, C., Song, M., 2021. Safe distillation
box. arXiv:2112.03695.
Yu, P., Fei, H., Li, P., 2021. Cross-lingual language model pretraining for
retrieval, in: Proceedings of the Web Conference 2021, pp. 1029–1039.
Zaheer, M., Guruganesh, G., Dubey, K.A., Ainslie, J., Alberti, C., Ontanon,
S., Pham, P., Ravula, A., Wang, Q., Yang, L., et al., 2020. Big bird:
Transformers for longer sequences.
Advances in neural information
processing systems 33, 17283–17297.
Zampieri, M., Malmasi, S., Nakov, P., Rosenthal, S., Farra, N., Kumar, R.,
2019. Predicting the type and target of offensive posts in social media.
NAACL HLT 2019 - 2019 Conference of the North American Chapter
of the Association for Computational Linguistics: Human Language
Technologies - Proceedings of the Conference 1, 1415–1420.
URL:
https://arxiv.org/abs/1902.09666v2, doi:10.18653/V1/N19-1144.
Zanella-Béguelin, S., Wutschitz, L., Tople, S., Rühle, V., Paverd, A., Ohri-
menko, O., Köpf, B., Brockschmidt, M., 2020. Analyzing information
leakage of updates to natural language models, in: Proceedings of
the 2020 ACM SIGSAC conference on computer and communications
security, pp. 363–375.
Zellers, R., Holtzman, A., Rashkin, H., Bisk, Y., Farhadi, A., Roesner, F.,
Choi, Y., 2019. Defending against neural fake news. Advances in neural
information processing systems 32.
Zhang, B., Liu, Z., Cherry, C., Firat, O., 2024a.
When scaling meets
llm finetuning: The effect of data, model and finetuning method.
arXiv:2402.17193.
Zhang, B., Zhang, Y., Frison, L., Brox, T., Bödecker, J., 2024b. Constrained
reinforcement learning with smoothed log barrier function. URL: https:
//arxiv.org/abs/2403.14508, arXiv:2403.14508.
Zhang, C., Ippolito, D., Lee, K., Jagielski, M., Tramèr, F., Carlini, N.,
2023. Counterfactual memorization in neural language models. URL:
https://arxiv.org/abs/2112.12938, arXiv:2112.12938.
Zhang, E., Zhu, V., Saphra, N., Kleiman, A., Edelman, B.L., Tambe, M.,
Kakade, S.M., Malach, E., 2024c. Transcendence: Generative models
can outperform the experts that train them. arXiv:2406.11741.
Zhang, J., Huang, W., Ma, Z., Michel, O., He, D., Gupta, T., Ma, W.C.,
Farhadi, A., Kembhavi, A., Krishna, R., 2024d. Task me anything. URL:
https://arxiv.org/abs/2406.11775, arXiv:2406.11775.
Zhang, L., Zhang, Q., Shen, L., Yuan, B., Wang, X., Tao, D., 2022a. Eval-
uating model-free reinforcement learning toward safety-critical tasks.
arXiv:2212.05727.
Zhang, S., Roller, S., Goyal, N., Artetxe, M., Chen, M., Chen, S., Dewan,
C., Diab, M., Li, X., Lin, X.V., et al., 2022b. Opt: Open pre-trained
transformer language models. arXiv preprint arXiv:2205.01068 .
Zhang, T., Kishore, V., Wu, F., Weinberger, K.Q., Artzi, Y., 2019.
Bertscore: Evaluating text generation with bert.
arXiv preprint
arXiv:1904.09675 .
Zhang, Y., Mao, S., Ge, T., Wang, X., Xia, Y., Lan, M., Wei, F., 2024e.
K-level reasoning with large language models. arXiv:2402.01521.
Zhang, Z., Zhang, A., Li, M., Smola, A., 2022c. Automatic chain of thought
prompting in large language models. arXiv preprint arXiv:2210.03493 .
Zhao, W.X., Zhou, K., Li, J., Tang, T., Wang, X., Hou, Y., Min, Y., Zhang,
B., Zhang, J., Dong, Z., Du, Y., Yang, C., Chen, Y., Chen, Z., Jiang, J.,
Ren, R., Li, Y., Tang, X., Liu, Z., Liu, P., Nie, J.Y., Wen, J.R., 2023. A
survey of large language models. arXiv:2303.18223.
Zheng, X., Pang, T., Du, C., Liu, Q., Jiang, J., Lin, M., 2024. Improved
few-shot jailbreaking can circumvent aligned language models and their
defenses. arXiv:2406.01288.
Zhou, C., Liu, P., Xu, P., Iyer, S., Sun, J., Mao, Y., Ma, X., Efrat, A., Yu,
P., Yu, L., et al., 2024. Lima: Less is more for alignment. Advances in
Neural Information Processing Systems 36.
Zhou, Y., Muresanu, A.I., Han, Z., Paster, K., Pitis, S., Chan, H., Ba, J.,
2023. Large language models are human-level prompt engineers. URL:
https://arxiv.org/abs/2211.01910, arXiv:2211.01910.
Zhu, B., Sharma, H., Frujeri, F.V., Dong, S., Zhu, C., Jordan, M.I., Jiao,
J., 2023. Fine-tuning language models with advantage-induced policy
alignment. URL: https://arxiv.org/abs/2306.02231, arXiv:2306.02231.
Ziegler, D.M., Stiennon, N., Wu, J., Brown, T.B., Radford, A., Amodei,
D., Christiano, P., Irving, G., 2019. Fine-tuning language models from
human preferences. arXiv preprint arXiv:1909.08593 URL: https://
arxiv.org/abs/1909.08593.
Ziegler, D.M., Stiennon, N., Wu, J., Brown, T.B., Radford, A., Amodei,
D., Christiano, P., Irving, G., 2020. Fine-tuning language models from
human preferences. arXiv:1909.08593.
Zoph, B., Bello, I., Kumar, S., Du, N., Huang, Y., Dean, J., Shazeer, N.,
Fedus, W., 2022. St-moe: Designing stable and transferable sparse expert
models. URL https://arxiv. org/abs/2202.08906 .
Zou, A., Wang, Z., Carlini, N., Nasr, M., Kolter, J.Z., Fredrikson, M.,
2023. Universal and transferable adversarial attacks on aligned language
models. URL: https://arxiv.org/abs/2307.15043, arXiv:2307.15043.
J. Chua, Y. Li, S. Yang, C. Wang and L. Yao: Preprint submitted to Elsevier
Page 34 of 34

```
