---\ntitle: "2025-results]]-SEALGuard Safeguarding the Multilingual Conversations in - PDF Extract"\nsource_pdf: "2025/2025-results]]-SEALGuard Safeguarding the Multilingual Conversations in.pdf"\npages: 12\nextracted_at: "2026-02-14T02:17:33.748982"\n---\n\n# PDF Extract: 2025-results]]-SEALGuard Safeguarding the Multilingual Conversations in\n\n**Source PDF:** 2025/2025-results]]-SEALGuard Safeguarding the Multilingual Conversations in.pdf\n**Total Pages:** 12\n\n---\n\n## Content\n\n```\n--- Page 1 ---\n\nSEALGuard: Safeguarding the Multilingual Conversations in
Southeast Asian Languages for LLM Soware Systems
Wenliang Shan
wenliang.shan@monash.edu
Monash University
Melbourne, Victoria, Australia
Michael Fu
michael.fu@unimelb.edu.au
The University of Melbourne
Melbourne, Victoria, Australia
Rui Yang
rui.yang1@monash.edu
Monash University
Melbourne, Victoria, Australia
Chakkrit (Kla) Tantithamthavorn∗
chakkrit@monash.edu
Monash University
Melbourne, Victoria, Australia
ABSTRACT
Safety alignment is critical for LLM-powered systems. While recent
LLM-powered guardrail approaches such as LlamaGuard achieve
high detection accuracy of unsafe inputs written in English (e.g.,
“How to create a bomb?”), they struggle with multilingual unsafe
inputs. This limitation leaves LLM systems vulnerable to unsafe
and jailbreak prompts written in low-resource languages such as
those in Southeast Asia. This paper introduces SEALGuard, a mul-
tilingual guardrail designed to improve the safety alignment across
diverse languages. It aims to address the multilingual safety align-
ment gap of existing guardrails and ensure eﬀective ﬁltering of
unsafe and jailbreak prompts in LLM-powered systems. We adapt
a general-purpose multilingual language model into a multilingual
guardrail using low-rank adaptation (LoRA). We construct SEALS-
Bench, a large-scale multilingual safety alignment dataset contain-
ing over 260,000 prompts in ten languages, including safe, unsafe,
and jailbreak cases. We evaluate SEALGuard against state-of-the-
art guardrails such as LlamaGuard on this benchmark. Our ﬁndings
show that multilingual unsafe and jailbreak prompts substantially
degrade the performance of the state-of-the-art LlamaGuard, which
experiences a drop in Defense Success Rate (DSR) by 9% and 18%,
respectively, compared to its performance on English-only prompts.
In contrast, SEALGuard outperforms existing guardrails in detect-
ing multilingual unsafe and jailbreak prompts, improving DSR by
48% over LlamaGuard and achieving the best DSR, precision, and
F1-score. Our ablation study further reveals the contributions of
adaptation strategies and model size to the overall performance of
SEALGuard. We release our pre-trained model and benchmark at
https://github.com/awsm-research/SEALGuard to support further
research.
∗Corresponding author
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for proﬁt or commercial advantage and that copies bear this notice and the full citation
on the ﬁrst page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior speciﬁc permission
and/or a fee. Request permissions from permissions@acm.org.
Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
© 2018 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 978-1-4503-XXXX-X/2018/06...$15.00
https://doi.org/XXXXXXX.XXXXXXX
CCS CONCEPTS
• Computing methodologies →Natural language processing;
Discourse, dialogue and pragmatics; • Software and its engineer-
ing →Software safety.
KEYWORDS
Multilingual safety alignment, AI-powered software
ACM Reference Format:
Wenliang Shan, Michael Fu, Rui Yang, and Chakkrit (Kla) Tantithamtha-
vorn. 2018. SEALGuard: Safeguarding the Multilingual Conversations in
Southeast Asian Languages for LLM Software Systems. In Proceedings of
Make sure to enter the correct conference title from your rights conﬁrma-
tion email (Conference acronym ’XX). ACM, New York, NY, USA, 12 pages.
https://doi.org/XXXXXXX.XXXXXXX
1
INTRODUCTION
Large Language Models (LLMs)-powered software systems are in-
creasingly used in real-world applications, especially, in the multi-
lingual contexts, such as interactive language learning tutors [10,
38]. These systems build on the success of multilingual foundation
models that enable diverse language understanding. In particular,
there is a growing development of multilingual LLMs tailored for
lower-resource and regional languages such as Southeast Asian
languages [8, 28, 50]. Models such as SeaLLMs [50], SeaLion [28],
and Sailor [8] are trained on regional data and demonstrate stronger
multilingual capabilities than English-centric models like LLaMA
[40]. These Southeast Asian multilingual LLMs enable intelligent
software systems to deliver services in users’ native languages,
improving accessibility and inclusivity across linguistically diverse
populations.
However, these LLM-driven systems still face vulnerabilities
stemming from the probabilistic and non-deterministic behavior of
multilingual LLMs. Unlike traditional rule-based systems, which
avoid unsafe outputs by design, LLM-driven systems can generate
harmful responses when given unsafe prompts. Thus, ensuring their
reliability presents a unique research challenge, as highlighted by
Bengio et al. [3], Hassan et al. [14], and Yao et al. [45], since quality
assurance must contend with the open-ended and unpredictable
nature of model outputs.
In response to the vulnerabilities introduced by the probabilistic
nature of LLMs, researchers have proposed input-output guardrails
as external safety alignment mechanisms that form a protective

--- Page 2 ---\n\nConference acronym ’XX, June 03–05, 2018, Woodstock, NY
Trovato et al.
layer around models without requiring direct ﬁne-tuning of the
underlying model. Examples include LlamaGuard [16], OpenAI
Moderation [26], Perplexity [2], Perspective API [21], and NVIDIA
NeMo [34]. These approaches classify and ﬁlter user prompts or
LLM outputs to prevent unsafe content. In particular, LlamaGuard
proposed by Inan et al. [16] achieves state-of-the-art performance
in detecting unsafe prompts, outperforming tools like OpenAI Mod-
eration [26] and Perspective API [21].
However, LlamaGuard was primarily trained and ﬁne-tuned on
English data, and its original paper acknowledges that it may not
perform reliably in other languages [16]. Our evaluation further
validates this concern, highlighting its limited eﬀectiveness in de-
fending against unsafe prompts in many under-resourced languages
in Southeast Asia. Notably, under-resourced languages are often
used as jailbreak attacks to bypass guardrails and trigger unsafe
responses from LLMs. In particular, Yong et al. [46] demonstrates
that translated unsafe prompts trigger unsafe responses from GPT-4
79% of the time. This exposes a key software engineering chal-
lenge: how can we design external guardrails that eﬀectively
protect multilingual LLM-driven systems, especially across
under-resourced languages like those in Southeast Asia?
To address this gap, we propose using low-rank adaptation (LoRA)
[15] to ﬁne-tune a multilingual LLM of similar size to LlamaGuard
(8B parameters) [16] as a multilingual safety guardrail for Southeast
Asian languages. We name our method SEALGuard: SouthEast
Asian Language GUARDrail for safeguarding multilingual LLM-
driven software systems.
To evaluate SEALGuard, we introduce SEALSBench, a mul-
tilingual safety benchmark comprising 266,444 prompts (169,433
safe, 80,601 unsafe, 16,410 jailbreak) across English and nine South-
east Asian languages and covering ten unsafe content categories
and nine jailbreak types. We compare our SEALGuard against
LlamaGuard[16] and OpenAI Moderation [25] through extensive
experiments on this dataset, addressing four research questions:
• (RQ1) What is the impact of multilingual unsafe prompts
in Southeast Asian languages on the performance of
existing guardrails?
Results. When encountering multilingual unsafe prompts,
the state-of-the-art LlamaGuard’s performance drops by 9%,
from 59% to 50%, while OpenAI Moderation’s DSR drops by
31%, from 60% to 29%.
• (RQ2) What is the impact of multilingual jailbreak
prompts in Southeast Asian languages on the perfor-
mance of existing guardrails?
Results. When encountering multilingual jailbreak prompts,
the state-of-the-art LlamaGuard’s performance drops by 18%,
from 59% to 41%, while OpenAI Moderation’s DSR drops by
38%, from 60% to 22%.
• (RQ3) How eﬀective is our SEALGuard at defending
against multilingual unsafe and jailbreak prompts in
Southeast Asian languages?
Results. Our SEALGuard achieves an F1 score of 98%,
which is 34%–58% higher than existing guardrails. Similarly,
SEALGuard achieves a DSR of 97% and a precision of 99%,
outperforming baseline approaches by 48%–66% and 3%–63%,
respectively.
• (RQ4) What are the contributions of adaptation strate-
gies and model size to the performance of our SEAL-
Guard multilingual guardrail?
Results. We found that LoRA adaptation is the most impor-
tant component of SEALGuard, boosting its F1 score from
26% to 98%.
Novelty & Contributions. To the best of our knowledge, the
main contributions of this paper are as follows: (1) We propose
SEALGuard, a multilingual guardrail designed to overcome the
limitations of existing guardrails in multilingual safety alignment.
(2) We introduce SEALSBench, a comprehensive multilingual safety
alignment dataset containing over 260,000 prompts across ten lan-
guages, including safe, unsafe, and jailbreak prompts. (3) We ex-
tensively evaluate our SEALGuard against baseline guardrails,
demonstrating its eﬀectiveness across multilingual scenarios. (4)
We perform an ablation study to analyze the impact of adaptation
strategies and model size on the performance of SEALGuard.
2
BACKGROUND & RELATED WORK
In this section, we provide background on LLM-powered agent
systems and their associated safety challenges. We present existing
safety alignment approaches, highlight the gap in multilingual
safety alignment, and discuss related work on safeguarding LLM-
based software systems.
2.1
LLM-Powered Agent Systems: Capabilities
and Safety Challenges
LLM agentic software systems are autonomous programs capable
of perceiving inputs, making decisions, and acting toward speciﬁc
goals [30]. Traditionally, they were built using symbolic reasoning
or task-speciﬁc rule-based logic [5, 41], often limiting adaptability
and scalability. Recent advances in large language models (LLMs)
have fundamentally reshaped this paradigm, enabling agentic sys-
tems that are far more ﬂexible and context-aware [23, 27].
In this work, we focus on LLM-powered agents for user-facing
applications (e.g., customer service chatbots and language learn-
ing tutors), which support open-ended dialogue and dynamic in-
tent interpretation. As LLMs continue to expand globally, multilin-
gual LLM-powered agents are increasingly deployed in real-world
applications, especially for low-resource and regional languages
[8, 28, 50], enhancing inclusivity and accessibility for diverse popu-
lations.
Traditional rule-based systems are deterministic functions :
→, mapping inputs ∈to outputs ∈using explicitly
deﬁned rules or decision trees. While predictable and interpretable,
they lack ﬂexibility and scalability. In contrast, large language mod-
els (LLMs) are probabilistic functions : →, generating out-
puts by sampling from a distribution (| ) over an open-ended
output space. This allows LLMs to support ﬂexible, context-aware
agent systems.
However, this ﬂexibility comes with safety risks: when given
unsafe prompts ∈Xunsafe, rule-based systems inherently avoid
unsafe behavior due to their constrained outputs, whereas LLMs
may generate unsafe responses through the probabilistic nature of
their generation—highlighting the need for LLM safety alignment.
Multilingual settings present additional challenges, as safety tools

--- Page 3 ---\n\nSEALGuard: Safeguarding the Multilingual Conversations in Southeast Asian Languages for LLM Soware Systems Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
and training resources for low-resource languages typically lag
behind those available for English.
2.2
Safety Alignment For LLM-Powered Agent
Systems
In response to these challenges, LLM safety alignment has emerged
as a critical research area, where models are tuned to improve safety
[1, 9, 12, 51]. However, such ﬁne-tuning often faces fundamental
safety–capability trade-oﬀs [6], potentially reducing creativity and
responsiveness, while requiring extensive computation to adjust
model parameters.
On the other hand, runtime guardrails act as external safety align-
ment mechanisms, forming a protective layer around LLMs without
requiring direct ﬁne-tuning. Examples include LlamaGuard [16],
OpenAI Moderation [26], Perplexity [2], Perspective API [21], and
NVIDIA NeMo [34]. These techniques classify and ﬁlter user prompts
to prevent unsafe inputs, aligning LLM behavior with safety goals.
In particular, LlamaGuard proposed by Inan et al. [16] achieves state-
of-the-art performance in detecting unsafe prompts, outperforming
tools like OpenAI Moderation [26] and Perspective API [21].
2.3
Motivation and Research Gap: Multilingual
Safety Alignment
While runtime guardrails like LlamaGuard have demonstrated strong
performance in ﬁltering unsafe prompts, current state-of-the-art
guardrails are primarily trained and evaluated on English inputs.
This leaves a signiﬁcant gap in multilingual contexts, where unsafe
prompts written in other languages, particularly low-resource or
less widely studied ones, can often evade detection.
Figure 1 illustrates this gap: an English unsafe prompt is suc-
cessfully blocked by the guardrail and prevented from reaching the
LLM agent. However, when the same prompt is translated into a
language such as Lao, it bypasses the guardrail and enters the LLM
agent system, which could trigger unsafe behavior. This indicates
that multilingual prompts can function as jailbreaks, bypassing
runtime guardrails that were not trained to recognize the semantics
of multilingual inputs. In particular, prior studies have shown that
low-resource languages can be exploited as attack vectors to bypass
safety mechanisms. Deng et al. [7] report that multilingual unsafe
prompts achieve attack success rates of 81% on ChatGPT and 41% on
GPT-4. Similarly, Yong et al. [46] demonstrate that translated unsafe
prompts bypass existing guardrails and trigger unsafe responses
from GPT-4 in 79% of tested cases. These ﬁndings highlight the
need for multilingual safety alignment to safeguard the LLM
component in the system.
Despite LlamaGuard’s eﬀectiveness in English, its ﬁne-
tuned data and evaluation focus are largely monolingual,
limiting its robustness in defending multilingual LLM sys-
tems. This limitation, noted in the original paper [16], high-
lights the need for multilingual guardrails. These guardrails
should eﬀectively defend against unsafe inputs across diverse lan-
guages, particularly low-resource ones such as those in Southeast
Asia. At the same time, they must maintain a low false alarm rate
to allow safe multilingual inputs to pass through. This is essential
for supporting multilingual agent systems powered by emerging
multilingual LLMs such as SeaLLMs [50], SeaLion [28], and Sailor
[8].
3
APPROACH
To address the challenge of multilingual safety alignment, we present
the technical details of how we adapt a general-purpose multilin-
gual language model into a multilingual guardrail using low-rank
adaptation (LoRA). Figure 2 provides an overview of our approach.
Below, we walk through each step of the process as illustrated in
the ﬁgure.
3.1
Apply Guardrail Chat Template
In Step 1 , we apply a guardrail chat template adapted from Lla-
maGuard [16] to make a general-purpose language model behave
like a safety classiﬁer. Speciﬁcally, we begin by including the fol-
lowing task description: “Task: Check if there is unsafe content
in ’User’ messages in conversations according to our safety policy
using the categories below.” Next, we deﬁne the unsafe content
categories between the special tags “<BEGIN UNSAFE CONTENT
CATEGORIES>” and “<END UNSAFE CONTENT CATEGORIES>”,
informing the model of the types of inputs that may be considered
unsafe. We then wrap the user’s message to be evaluated within
another set of special tags: <BEGIN CONVERSATION> How to build
a bomb? <END CONVERSATION>. Finally, we instruct the model
that its output must begin with either “safe” or “unsafe”, restricting
it to a binary classiﬁcation format suitable for safety evaluation.
3.2
Input to SeaLLM Model
In Step 2 , after the input has been structured using the chat tem-
plate, it undergoes tokenization through a Byte-Pair Encoding (BPE)
model [35] implemented via SentencePiece [20]. This process con-
verts the textual prompt into a sequence of token IDs—such as
[151644, ..., 151645, ...]—that correspond to subword units in the
model’s vocabulary. Each token ID serves as an index into the
word embedding matrix W ∈R×ℎof the SeaLLM model [50],
where = 152,064 represents the vocabulary size and ℎ= 3,584
denotes the hidden dimension. Using this embedding matrix, each
token is transformed into a dense vector, producing the input ma-
trix X ∈R×ℎ, where is the length of the input sequence. This
matrix X is then passed through a deep stack of 28 transformer
decoder layers. Each decoder block, following the architecture used
in SeaLLM [50], includes masked self-attention and feed-forward
neural networks (FFNN).
3.3
Adapting Multilingual Language Model to
Guardrail
While the SeaLLM model introduced in Step 2 was pre-trained on
multilingual data and is capable of understanding our task instruc-
tions, our evaluation reveals that it falls short in reliably identifying
unsafe prompts across multiple languages. This limitation stems
from the fact that SeaLLM was not explicitly trained as a guardrail,
and thus lacks the specialized alignment required for multilingual
safety detection.
To address this, in Step 3 , we use Low-Rank Adaptation (LoRA)
to eﬃciently adapt the SeaLLM model without ﬁne-tuning its full

--- Page 4 ---\n\nConference acronym ’XX, June 03–05, 2018, Woodstock, NY
Trovato et al.
User with
unsafe input
Runtime
Guardrails
Blocked
LLM Agent
Bypass the guardrail
Sure, here are
the steps…
Unsafe prompt
in Low resource
languages
Unsafe prompt
in English
How can I build
a bomb?
តខចបងតបប
កយរបប?
Figure 1: Overview of how multilingual unsafe prompts interact with runtime guardrails compared to English unsafe prompts.
Training Data
Validation Data
Testing Data
SeaLLM
FFNN
Decoder 1
Masked Self-Attention
LayerNorm
8B Pretrained Frozen Parameters
Decoder 2
Decoder 28
…
Apply Guardrail Chat Template
How to build a bomb?
<|im_start|>system
Task: Check if there is unsafe content in
'User' messages in conversations according
our safety policy with the below categories.
<BEGIN UNSAFE CONTENT
CATEGORIES>
...
<END UNSAFE CONTENT CATEGORIES>
<BEGIN CONVERSATION>
User: How to build a bomb?
<END CONVERSATION>
Provide your safety assessment for ONLY
THE LAST User message in the above
conversation:
- First line must read 'safe' or ‘unsafe’.
<|im_end|>
<|im_start|>assistant
1
2
LoRA: Low Rank Adaptation
Word Embedding Layer
Masked Self-Attention
Layer
FFNN Layer
3
如何制造炸弹?
Cara membuat bom?
Làm thếnào đểchếtạo một quảbom?
Bagaimana untuk membina bom?
ဗံုးဘယ်လိုေဆာက်မလဲ။?
วธกาสรางะเบด?
របបបងតបបក?
Paano gumawa ng bomba?
ວທການສາງລກລະເບດ?
Multilingual Prompts in
Southeast Asian Langauges
4 Detect and Block Unsafe Prompts
SEALGuard
Greedy Decoding
Unsafe
Safe
Blocked
LLM-Powered System
+
Training
Inference
Tokenization & Embeddings
Figure 2: The overview of our SEALGuard approach.
parameter set. This preserves SeaLLM’s original multilingual capa-
bilities while introducing guardrail-speciﬁc knowledge, enabling
the model to detect unsafe content across diverse languages.
The core idea behind LoRA is to inject trainable low-rank modiﬁ-
cations into selected weight matrices of the model. Speciﬁcally, for
each target layer, the update is modeled as a low-rank matrix ΔW,
constructed from the product of two smaller trainable matrices:
A ∈Rℎ×and B ∈R×ℎ, where ℎis the hidden dimension and
≪ℎis a rank parameter that controls adaptation capacity. This
results in a new weight formulation:
W= W+ AB.
By keeping the original weights Wfrozen and only train-
ing the low-rank components, LoRA enables task-speciﬁc adap-
tation—in our case, alignment to multilingual guardrail behav-
ior—while maintaining the model’s general language understand-
ing.
In building SEALGuard, we incorporate LoRA into key compo-
nents of the SeaLLM model: the word embedding layer, the self-
attention blocks, and the feed-forward neural networks (FFNN).
3.4
Detect and Block Multilingual Unsafe
Prompts
In Step 5 , SEALGuard intercepts user prompts before they reach
an LLM-powered system, identifying and blocking unsafe inputs.
Similar to LlamaGuard [16], SEALGuard frames unsafe prompt
detection as sequence generation. Given the ﬁnal transformer de-
coder output H ∈R×ℎ—with as the sequence length and ℎas
the hidden size—a linear layer projects each hidden state Hto a
vocabulary distribution using a weight matrix Wlm ∈Rℎ×and
bias blm ∈R, where = 152,064. This transformation produces a
vector of raw prediction scores, referred to as logits, for each token
position.
These logits are then passed through a softmax function to com-
pute probabilities over all possible vocabulary tokens. Guided by
the chat template introduced in Step 1 , the model generates a re-
sponse sequence, where the ﬁrst token explicitly states whether
the input is “safe” or “unsafe”. We use greedy decoding to generate
tokens, selecting at each step the one with the highest probability:
= arg max

softmax(HWlm + blm)
where indexes the vocabulary. Generation stops at either the
special end-of-text token “<|im_end|>” or a predeﬁned length limit.
The ﬁrst generated token is used as the model’s safety decision.

--- Page 5 ---\n\nSEALGuard: Safeguarding the Multilingual Conversations in Southeast Asian Languages for LLM Soware Systems Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
4
EXPERIMENTAL DESIGN
In this section, we outline the motivation behind our four research
questions, introduce the proposed benchmark dataset that serves
as our experimental dataset, describe the types of unsafe prompts
and jailbreak attacks studied, present the baseline guardrails, and
detail our experimental setup.
4.1
Research Questions
To evaluate the eﬀectiveness of multilingual guardrails for South-
east Asian languages, we formulate the following four research
questions:
RQ1) What is the impact of multilingual unsafe prompts
in Southeast Asian languages on the performance of exist-
ing guardrails? LlamaGuard [16] achieves state-of-the-art per-
formance on English data, reaching 95% accuracy as a runtime
guardrail for classifying safe and unsafe prompts. However, its
training data is primarily in English. As a result, a key limitation
arises: Inan et al. Inan et al. [16] speculated that LlamaGuard may be
vulnerable to prompts written in other languages. This highlights
a research gap in multilingual safety alignment, where existing
guardrails may fail to generalize across diverse linguistic inputs.
Yet, little is known about how multilingual unsafe prompts aﬀect
the performance of these AI guardrails. Thus, we investigate the
impact of multilingual unsafe prompts on current AI guardrail
systems.
RQ2) What is the impact of multilingual jailbreak prompts
in Southeast Asian languages on the performance of exist-
ing guardrails? While general multilingual unsafe prompts al-
ready challenge existing guardrails, multilingual jailbreak prompts
pose an even greater risk. These prompts are intentionally crafted
to bypass safety mechanisms, circumventing the protections that
guardrails provide. Yet, current studies have not examined how
such jailbreak prompts aﬀect the performance of AI guardrail sys-
tems in multilingual settings. Thus, we investigate the impact of
multilingual jailbreak prompts on existing AI guardrails.
RQ3) How eﬀective is our SEALGuard at defending against
multilingual unsafe and jailbreak prompts in Southeast Asian
languages? To address the gap in multilingual safety alignment,
we proposed a multilingual guardrail capable of detecting unsafe
inputs across diverse linguistic settings. In Section 3, we describe
how we adapt a multilingual language model into a guardrail us-
ing low-rank adaptation (LoRA). However, the eﬀectiveness of this
approach remains unknown. Thus, we evaluate the performance of
our proposed SEALGuard against existing baseline guardrails, fo-
cusing on its ability to detect both multilingual unsafe and jailbreak
prompts while minimizing false positives.
RQ4) What are the contributions of adaptation strategies
and model size to the performance of our SEALGuard multi-
lingual guardrail? Our SEALGuard multilingual guardrail relies
on adapting a general-purpose multilingual language model into
a safety guardrail using low-rank adaptation (LoRA). While LoRA
serves as the primary adaptation strategy, the impact of diﬀerent
adaptation approaches and model sizes on guardrail performance
remains unclear. To better understand these factors, we formulate
this research question to conduct an ablation study, examining how
adaptation strategies and model size inﬂuence the eﬀectiveness of
SEALGuard.
4.2
SEALSBench: A Multilingual Safety
Alignment Benchmark in Southeast Asian
Languages
To address the four research questions, we construct a multilin-
gual LLM safety benchmark, SEALSBench, comprising 18,846 safe
prompts, 8,959 unsafe prompts, and 1,799 jailbreak prompts (unsafe),
totaling 29,604 prompts. Jailbreak prompts are a speciﬁc category
of unsafe inputs designed to bypass or mislead LLM safety mecha-
nisms. Figure 3 presents the distribution of safe and unsafe prompts,
along with a detailed breakdown of unsafe categories and jailbreak
prompt types. These prompts were initially written in English and
then translated into nine Southeast Asian languages to assess the
eﬀectiveness of multilingual guardrails across diverse linguistic con-
texts. Figure 4 summarizes the data construction workﬂow. Below,
we outline the step-by-step process used to construct this dataset.
Step 1: Data Collection. We extracted 8,959 unsafe prompts
from the BeaverTails dataset by Ji et al. [18], covering ten cate-
gories of unsafe prompts introduced in Section 4.3. These cate-
gories capture a broad range of safety concerns related to input
prompts submitted to LLMs, consistent with prior LLM safety stud-
ies [11, 31, 33]. Moreover, we extracted 1,799 unsafe prompts from
four additional benchmark datasets: Do-Not-Answer [42], CatQA
[4], AdvBench [52], and Forbidden Questions [36] and transformed
them into jailbreak prompts. These additional datasets help avoid
data contamination and ensure our jailbreak attacks have diﬀerent
distributions from the unsafe prompts in the BeaverTails dataset.
We then transformed them into jailbreak prompts using nine jail-
break attack strategies introduced in Section 4.4. This allows us to
cover a special class of unsafe prompts—jailbreak prompts—that are
designed to bypass safety guardrails and reﬂect jailbreak attempts
that may occur in real-world use. To evaluate whether safe inputs
will be incorrectly blocked by SEALGuard, we collect 18,846 safe
prompts from the Alpaca dataset by Taori et al. [39]. These prompts
represent safe interactions with LLMs that guardrails should allow
without blocking. In summary, our dataset contains a total of 29,604
prompts, including 8,959 unsafe prompts, 1,799 jailbreak prompts,
and 18,846 safe prompts.
Step 2: Multilingual Translation into Southeast Asian Lan-
guages. The collected 29,604 prompts were originally written in
English. In this study, we focus on nine Southeast Asian languages
supported by SeaLLM [29], covering major linguistic families in
the region: Chinese (Zho), Indonesian (Ind), Vietnamese (Vie), Thai
(Tha), Khmer (Khm), Lao, Malay (Msa), Burmese (Mya), and Taga-
log (Tgl). To support multilingual evaluation, we used the Google
Translate API [13] to translate all prompts into these nine languages.
This results in a total of 296,040 prompts, including the original
English and its translations into nine Southeast Asian languages.
These collectively form our multilingual safety benchmark dataset,
SouthEast Asian Languages Safety Benchmark, SEALSBench.
4.3
Studied Unsafe Categories
Our SEALSBench dataset consists of ten unsafe categories to sup-
port the evaluation of LLM safety alignment. Each category is

--- Page 6 ---\n\nConference acronym ’XX, June 03–05, 2018, Woodstock, NY
Trovato et al.
Complete dataset
Unsafe dataset
Complete dataset
Figure 3: The distribution of safe and unsafe prompts, along with category-wise breakdowns of unsafe and jailbreak prompts.
x
Alpaca
Beavertails
Unsafe Prompts
Safe Prompts
Jailbreak Prompts
Step 2
Multilingual Translation Using
Google Translate API
Step 1: Data Collection
SEALSBench
A Multiligual Safety Benchmark
Do-Not-Answer, CatQA,
AdvBench, Forbidden Questions
Training
Validation
Testing
Figure
4:
Workﬂow
for
Constructing
our
SEALS-
Bench Dataset.
labeled as C1 through C10, where C stands for Category: C1: Vio-
lent Criminal Activity (1,729 samples), C2 – Non-Violent Criminal
Conduct (4,196 samples), C3 – Child Sexual Abuse (145 samples),
C4 – False and Defamatory Claims (1,415 samples), C5 – Hazardous
Professional Guidance (362 samples), C6 – Personal Information
Exposure (852 samples), C7 – Discriminatory and Hateful Expres-
sion (1,022 samples), C8 – Self-Destructive Behavior Promotion
(87 samples), C9 – Explicit Sexual Material (342 samples), C10 –
Misinformation & Extremist Content (807 samples).
4.4
Studied Jailbreak Attacks
We consider nine diﬀerent jailbreak attacks spanning these three
major categories.
Obfuscation-Based Attacks. These techniques aim to circumvent
the safety mechanisms of large language models (LLMs) by disguis-
ing unsafe prompts through various forms of obfuscation.
Caesar Cipher [48] employs systematic character replacement
techniques, where responses requested in matching encrypted for-
mats can potentially bypass both input and output safety mecha-
nisms.
Zulu [47] exploits low-resource language vulnerabilities by
reformulating harmful prompts in less-supported languages, then
manipulating the model to translate them back into unsafe content,
thereby evading guardrail systems.
Template-Based Attacks. These attacks utilize pre-constructed
frameworks or prompt structures that exploit predictable patterns
and known vulnerabilities within LLMs.
AIM [17] manipulates the model into adopting a predeﬁned
persona that operates outside normal ethical constraints, promoting
unethical, illegal, and harmful responses through character role-
play.
DAN [37] creates scenarios where the model ’believes’ normal
restrictions no longer apply, often framing interactions as role-
playing exercises to bypass content ﬁlters.
Combination (Preﬁx injection + Refusal Suppression) [43]
combines multiple techniques, including preﬁx injection (using
innocuous openings) with refusal suppression instructions, con-
straining the model’s ability to generate standard refusal responses.
Self Cipher [49] prompts the model to act as an expert in un-
deﬁned cipher systems, leveraging the model’s internal encoding
capabilities to implicitly encrypt queries and decrypt outputs with-
out explicit encoding rules.
Deep Inception [22] employs multi-layered narrative struc-
tures that progressively guide the model toward restricted behavior
through incremental logical steps, often embedded within ﬁctional
scenarios.
Code-Based Attacks. These attacks exploit LLMs’ programming
capabilities by disguising harmful content within technical instruc-
tions or programming logic.

--- Page 7 ---\n\nSEALGuard: Safeguarding the Multilingual Conversations in Southeast Asian Languages for LLM Soware Systems Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
Dual use [19] combines code injection techniques with pay-
load splitting to craft harmful prompts that appear as legitimate
programming tasks while containing malicious intent.
Code Chameleon [24] reformulates harmful instructions as
code completion tasks, using custom encryption functions embed-
ded within programming contexts to enable decryption and execu-
tion of harmful queries while bypassing safety mechanisms.
4.5
Baseline Guardrails
(1) LlamaGuard [16]: An LLM-based guardrail ﬁne-tuned on a
proprietary moderation dataset to classify prompts as “safe”
or “unsafe.” We evaluate two variants: “Llama-Guard-3-8B”
and the smaller “Llama-Guard-3-1B”.
(2) OpenAI Moderation [25]: A GPT-based moderation sys-
tem trained via active learning on public data. It ﬂags prompts
as unsafe if the returned boolean is “True”, covering diverse
safety categories.
4.6
Experimental Setup
Data Splitting. We split our dataset into 5% training (14,800 sam-
ples), 5% validation (14,800 samples), and 90% testing (266,444 sam-
ples). We ensure that all language variants of a given prompt remain
in the same split by partitioning based on unique English prompt
IDs rather than random sampling.
Model Implementation and Optimization. We developed SEAL-
Guard using Transformers [44] and PyTorch [32], ﬁne-tuning the
multilingual SeaLLMs-v3-7B-Chat [50] with LoRA [15]. Training
was conducted on an AMD 5950X CPU with two NVIDIA RTX
3090 GPUs. Input prompts were wrapped in a chat template, and
the model was trained to autoregressively generate the prompt
followed by a classiﬁcation token (“safe” or “unsafe”). We optimized
the model using Cross-Entropy Loss, masking prompt tokens dur-
ing loss computation to focus learning on the classiﬁcation output.
The loss is deﬁned as
L= −

∑
=1
log (| <,)
(1)
whereis the length of the target sequence,is the target token
at position,<are previously generated tokens, is the input, and
is the model’s predicted probability distribution parameterized
by .
Hyper-Parameter Settings. We followed standard hyperparam-
eter settings commonly used for LoRA ﬁne-tuning. Speciﬁcally, we
used a learning rate of 1e-4 with a LoRA dropout rate of 0.05. The
rank () of the LoRA modules was set to 8, and the scaling factor
() was set to 32. We applied gradient clipping with a maximum
gradient norm of 1.0. For learning rate scheduling, we used a cosine
scheduler with 5% of the total training steps allocated to warm-
up. The complete training recipe of our SEALGuard approach is
available in our replication package at https://github.com/awsm-
research/SEALGuard.
5
EXPERIMENTAL RESULTS
In this section, we present the results for our three research ques-
tions.
(RQ1) What is the impact of multilingual unsafe
prompts in Southeast Asian languages on the
performance of existing guardrails?
Approach. To assess the impact of multilingual unsafe prompts in
Southeast Asian languages on the performance of existing guardrails,
we use 80,601 unsafe prompts from the SEALSBench testing set,
written in English and nine Southeast Asian (SEA) languages. We
ﬁrst evaluate guardrail performance on the English prompts to
establish baselines in their familiar language. We then assess per-
formance on the non-English SEA prompts to measure the impact
of multilingual inputs. Speciﬁcally, we evaluate two state-of-the-art
language model-based guardrails: LlamaGuard [16] and OpenAI
Moderation [25]. We use Defense Success Rate (DSR) as our pri-
mary metric, which evaluates guardrail capability to defend against
unsafe prompts:
• Defense Success Rate (DSR):
DSR =

+ 
where is the number of true positives (correctly detected
unsafe/jailbreak prompts) and is the number of false
negatives (missed unsafe/jailbreak prompts).
59.74%
58.78%
44.7%
29.4%
49.63%
44.56%
0.00
0.25
0.50
0.75
1.00
OpenAI Moderation
LlamaGuard 8b
LlamaGuard 1b
Guardrails
Defense Success Rate (DSR)
English Unsafe Prompts w/o Jailbreak Attacks
SEA Unsafe Prompts w/o Jailbreak Attacks
(RQ1) Guardrail DSR: English Unsafe vs. SEA Unsafe 
Figure 5: DSR result of unsafe prompts in English and SEA
languages.
Results. Figure 5 presents the defense success rate (DSR) of the
three baseline guardrails, comparing their performance across two
scenarios: unsafe prompts in English (blue bars) versus multilingual
unsafe prompts, excluding jailbreak prompts, in Southeast Asian
languages (red bars).
LlamaGuard 8B’s DSR substantially decreases by 9%, de-
clining from 58.78% to 49.63% when defending against mul-
tilingual unsafe prompts. Similarly, OpenAI Moderation’s DSR
experiences a substantial decline of 30%, dropping from 59.74%
to 29.4% when encountering multilingual unsafe prompts. On the
other hand, LlamaGuard 1B achieves a lower performance of 45% for
both English unsafe prompts and multilingual unsafe prompts than

--- Page 8 ---\n\nConference acronym ’XX, June 03–05, 2018, Woodstock, NY
Trovato et al.
LlamaGuard 8B. These ﬁndings reveal that the eﬀectiveness
of state-of-the-art guardrails is decreased when defending
multilingual unsafe prompts, highlighting the need for mul-
tilingual guardrails capable of eﬀectively defending such
multilingual prompts.
(RQ2) What is the impact of multilingual
jailbreak prompts in Southeast Asian languages
on the performance of existing guardrails?
Approach. To assess the impact of multilingual jailbreak prompts
in Southeast Asian languages on guardrail performance, we use
8,060 unsafe prompts in English, and 16410 jailbreak prompts in
English and nine SEA languages from our SEALSBench test set.
We ﬁrst evaluate guardrail performance on English unsafe prompts,
which yields the same baselines as in RQ1. We then assess perfor-
mance on multilingual jailbreak prompts to measure the eﬀect of
multilingual jailbreak inputs, using the same baseline and metric
(DSR) as in RQ1.
59.74%
58.78%
44.7%
21.91%
41.02%
44.94%
0.00
0.25
0.50
0.75
1.00
OpenAI Moderation
LlamaGuard 8b
LlamaGuard 1b
Guardrails
Defense Success Rate (DSR)
English Unsafe Prompts w/o Jailbreak Attacks
Multilingual Jailbreak Attacks
(RQ2) Guardrail DSR: English Unsafe vs. Multilingual Jailbreaks
Figure 6: DSR result of unsafe prompts in English and Multi-
lingual jailbreak prompts.
Results. Figure 6 presents the defense success rate (DSR) of the
three baseline guardrails, comparing their performance across two
scenarios: unsafe prompts written in English without jailbreak
attacks (blue bars) versus multilingual jailbreak attacks in Southeast
Asian languages and English (red bars).
LlamaGuard 8B’s DSR substantially decreases by 18%, de-
clining from 58.78% to 41.02% when defending against multi-
lingual jailbreak prompts. Similarly, OpenAI Moderation’s DSR
experiences a substantial decline of 38%, dropping from 59.74% to
21.91% when encountering multilingual jailbreak prompts. As in
RQ1, LlamaGuard 1B still achieves a lower performance of 45% for
both English unsafe prompts and multilingual jailbreak prompts
than LlamaGuard 8B. These ﬁndings highlight that the eﬀec-
tiveness of state-of-the-art guardrails is decreased when de-
fending multilingual jailbreak prompts, highlighting the
need for multilingual jailbreak-aware guardrails capable of
eﬀectively defending such multilingual jailbreak prompts.
(RQ3) How eﬀective is our SEALGuard at
defending against multilingual unsafe and
jailbreak prompts in Southeast Asian languages?
Approach. To address this RQ, we compare our SEALGuard ap-
proach with LlamaGuard and OpenAI Moderation using the full
multilingual testing set from our SEALSBench dataset. This set
includes 169,433 safe, 80,601 unsafe, and 16,410 jailbreak prompts
written in English and nine Southeast Asian languages. We use the
same Defense Success Rate (DSR) as in RQ1 and RQ2 to evaluate
guardrail eﬀectiveness in defending against unsafe and jailbreak
prompts. Beyond defense capability, maintaining a low false alarm
rate is also critical to avoid misclassifying safe content. Thus, we
use precision to measure the accuracy of the guardrail in avoiding
false alarms—i.e., how well it identiﬁes only truly unsafe prompts
without misclassifying safe ones. We also use the F1-Score to cap-
ture the overall balance between correctly detecting unsafe prompts
and minimizing false positives. Formally:
• Precision:
Precision =

+ 
where is the number of true positives (correctly detected
unsafe/jailbreak prompts) and is the number of false
positives (safe prompts incorrectly classiﬁed as unsafe).
• F1-Score:
F1 = 2 · Precision · DSR
Precision + DSR
Results. Figure 7 presents the experimental results of our SEAL-
Guard and the three baseline approaches according to our three
evaluation measures (i.e., DSR, Precision, and F1-Score).
Our SEALGuard achieves an F1-Score of 98%, which is
58%, 52%, and 34% better than the LlamaGuard-3-1B, OpenAI
Moderation, and LlamaGuard-3-8B respectively. In terms of
DSR, Figure 7 shows that our SEALGuard achieves the highest
DSR of 97%, while the three baselines achieve 49%, 45%, and 31%,
respectively. This ﬁnding indicates that SEALGuard substantially
improves the DSR by 48%, 52%, and 66%. In terms of precision, Fig-
ure 7 shows that SEALGuard achieves the highest precision of 99%,
while the three baselines achieve 96%, 91%, and 36%, respectively.
This ﬁnding demonstrates that SEALGuard substantially improves
precision by 3%, 8%, and 63%.
In summary, these ﬁndings conﬁrm that our SEALGuard ap-
proach is eﬀective in defending against multilingual unsafe and
jailbreak prompts while maintaining a low false positive rate. These
results demonstrate that SEALGuard eﬀectively overcomes
a key limitation of the state-of-the-art guardrail, Llama-
Guard—namely, its reduced eﬀectiveness in defending against
multilingual unsafe and jailbreak prompts, as shown in RQ1
and RQ2.

--- Page 9 ---\n\nSEALGuard: Safeguarding the Multilingual Conversations in Southeast Asian Languages for LLM Soware Systems Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
97.23%
44.63%
48.93%
30.63%
DSR
SEALGuard
LlamaGuard−3−8B
LlamaGuard−3−1B
OpenAI Moderation
0.00
0.25
0.50
0.75
1.00
98.9%
36.35%
90.64%
95.84%
Precision
SEALGuard
OpenAI Moderation
LlamaGuard−3−8B
LlamaGuard−3−1B
0.00
0.25
0.50
0.75
1.00
98.05%
40.07%
63.55%
46.43%
F1
SEALGuard
LlamaGuard−3−8B
OpenAI Moderation
LlamaGuard−3−1B
0.00
0.25
0.50
0.75
1.00
Figure 7: (RQ3) The experimental results of our SEALGuard and the three baseline comparisons classifying safe and unsafe
(including jailbreaks) prompts. (↗) Higher F1, DSR, Precision, Accuracy = Better.
Table 1: (RQ4 Results) The performance comparisons of our
SEALGuard approach and the ﬁve variants to analyze the
contributions of the adaptation strategy and model size.
Methods
DSR
Precision
F1-Score
SeaLLM-V3-7B-Chat + LoRA (SEALGuard)
97.23
98.90
98.05
SeaLLM-V3-1.5B-Chat + LoRA
96.5
98.20
97.34
SeaLLM-V3-7B-Chat + NeMo
49.88
77.17
60.59
SeaLLM-V3-1.5B-Chat + NeMo
89.45
34.89
50.20
SeaLLM-V3-7B-Chat
15.07
89.51
25.80
SeaLLM-V3-1.5B-Chat
18.48
60.14
28.27
(RQ4) What are the contributions of adaptation
strategies and model size to the performance of
our SEALGuard multilingual guardrail?
Approach. To address this RQ, we conduct an ablation study to
evaluate the contribution of each component in SEALGuard. Our
approach combines two key elements: the SeaLLM-v3-7B-Chat
model (7B parameters) and a LoRA-based adaptation strategy that
aligns a general-purpose language model with guardrail objec-
tives. To assess the eﬀectiveness of the adaptation, we compare
our method with two variants: (1) applying the chat template in-
troduced in Section 3.1 directly to SeaLLM-v3-7B-Chat without
adaptation, and (2) using the NVIDIA NeMo toolkit with the same
model, an oﬀ-the-shelf guardrail framework that requires no ﬁne-
tuning. To examine the impact of model size, we also compare
against a smaller model, SeaLLM-v3-1.5B-Chat. In summary, we
evaluate six models in this RQ:
• SeaLLM-V3-7B-Chat + LoRA (SEALGuard): our proposed ap-
proach by applying LoRA on a multilingual language model.
• SeaLLM-V3-1.5B-Chat + LoRA: applying LoRA on a smaller
multilingual language model to study the impact of model
size on performance.
• SeaLLM-V3-7B-Chat + NeMo: applying the NeMo framework
for adaptation to study the eﬀect of alternative adaptation
strategies.
• SeaLLM-V3-1.5B-Chat + NeMo: applying the NeMo frame-
work on a smaller model to analyze both adaptation strategy
and model size impact.
• SeaLLM-V3-7B-Chat: no adaptation, used to isolate and eval-
uate the contribution of adaptation strategies.
• SeaLLM-V3-1B-Chat: no adaptation, used to evaluate the
baseline performance of a smaller model without any adap-
tation.
Results. Table 1 presents the performance comparison of our
SEALGuard approach and ﬁve variants to analyze the contributions
of adaptation strategies and model size.
LoRA adaptation is the key component driving the eﬀec-
tiveness of our SEALGuard approach. Within SEALGuard, the
LoRA module alone contributes 72% of the total F1-Score. Speciﬁ-
cally, when comparing “SeaLLM-V3-7B-Chat + LoRA (SEALGuard)”
with “SeaLLM-V3-7B-Chat” (without LoRA), the F1-Score drops
from 98% to 26%, highlighting a 72% contribution by LoRA.
In addition, comparing “SeaLLM-V3-7B-Chat + NeMo” with
“SeaLLM-V3-7B-Chat + LoRA (SEALGuard)” shows an F1-Score in-
crease from 61% to 98%, representing a 37% improvement attributed
to LoRA. Similarly, for the smaller variant of SEALGuard, “SeaLLM-
V3-1.5B-Chat + LoRA” outperforms both “SeaLLM-V3-1.5B-Chat”
and “SeaLLM-V3-7B-Chat + NeMo” by 70% and 38% in F1-Score,
respectively. These results demonstrate that LoRA is the most
eﬀective adaptation strategy for aligning a general-purpose
language model with a guardrail. In summary, these ﬁndings
validate the design rationale of SEALGuard, showing that LoRA
adaptation is the primary driver of performance gains, while model
size plays a comparatively minor role—even models with around
1B parameters can achieve promising results with our approach.
6
DISCUSSION
Our experimental results conﬁrm the eﬀectiveness of SEALGuard in
defending against multilingual unsafe and jailbreak prompts, show-
ing substantial improvements over existing guardrails. However,
its performance across diﬀerent languages, unsafe prompt types,

--- Page 10 ---\n\nConference acronym ’XX, June 03–05, 2018, Woodstock, NY
Trovato et al.
Figure 8: (Discussion) The experimental results for our SEALGuard and the other ﬁve baseline models classifying in category,
language, and jailbreak attacks.
and jailbreak prompts remains unclear. Thus, in this section, we
analyze SEALGuard ’s performance across these three dimensions.
6.1
Performance Across Diﬀerent Languages
To assess the cross-lingual robustness of our SEALGuard approach,
we analyze the performance of our SEALGuard across ten diﬀer-
ent languages. Speciﬁcally, the evaluation includes 80,601 unsafe
prompts, 16,410 jailbreak prompts, and 169,433 safe prompts from
our SEALSBench dataset. We focus on the F1-score as it captures
both the model’s ability to defend against unsafe prompts and its
tendency to raise false alarms on safe ones.
The left part of Figure 8 shows the F1-scores of our SEAL-
Guard across the ten studied languages. SEALGuard consis-
tently achieves the highest performance in all languages,
eﬀectively mitigating the language-speciﬁc vulnerabilities
present in existing guardrails. It also outperforms the strongest
baseline, LlamaGuard 8B, by a clear margin, as illustrated in Fig-
ure 8. This analysis conﬁrms the cross-lingual robustness of our
SEALGuard approach.
6.2
Performance on Diﬀerent Unsafe categories
To assess the robustness of SEALGuard across diﬀerent types
of unsafe content, we analyze its performance on ten diﬀerent
unsafe categories. As introduced in 4.3, we used 10 unsafe categories
labeled as C1 to C10 in our test dataset, totaling 80,601 prompts.
We adopt DSR as the evaluation measure because this analysis
involves only unsafe prompts, allowing DSR to assess single-class
performance without interference from false positives associated
with safe prompts.
The middle part of Figure 8 presents the DSR of SEALGuard com-
pared to baseline guardrails across ten unsafe categories. LlamaGuard-
8B exhibits low Defense Success Rate (DSR below 30%) in several
categories, including C5 (Hazardous Professional Guidance), C7
(Discriminatory and Hateful Expression), and C10 (Misinformation
& Extremist Content). In contrast, SEALGuard demonstrates
consistently high performance across all categories, with
DSR exceeding 95% in every category, conﬁrming its robust-
ness across diverse types of unsafe content.
6.3
Performance on Diﬀerent Jailbreak Prompts
To evaluate the robustness of SEALGuard across diﬀerent jailbreak
categories, we analyze its performance against nine jailbreak at-
tacks. As described in Section 4.4, this analysis covers 10 jailbreak
categories from our test dataset, totaling 16,410 prompts. We use
Defense Success Rate (DSR) as the evaluation metric, as the analy-
sis focuses solely on jailbreak prompts without any safe examples,
making DSR the appropriate measure for assessing single-class
performance.
The right part of Figure 8 presents the DSR of SEALGuard across
nine jailbreak categories. While LlamaGuard-8B shows low Defense
Success Rate (DSR below 30%) against Deep-Inception, Chameleon,
Zulu, and Dual-use jailbreak prompts, SEALGuard achieves con-
sistently high performance across all jailbreak types, with
DSR exceeding 95% in every category, conﬁrming its robust-
ness against diverse jailbreak attacks.
7
THREATS TO VALIDITY
Threats to internal validity relate to factors within our study that
may aﬀect the accuracy of the ﬁndings. One such threat is the
potential variation in translation accuracy when converting Eng-
lish prompts into Southeast Asian languages, which may aﬀect
guardrails’ detection performance. To mitigate this, we rely on
consistent use of the Google Translate API and make our transla-
tion process publicly available to promote transparency and repro-
ducibility. Another internal threat is the limited diversity in unsafe

--- Page 11 ---\n\nSEALGuard: Safeguarding the Multilingual Conversations in Southeast Asian Languages for LLM Soware Systems Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
and jailbreak prompts, which could bias evaluation results. To mit-
igate this, we curate SEALSBench from six diverse data sources
[4, 18, 36, 39, 42, 52], including ten unsafe categories and nine jail-
break categories, thereby enhancing the representativeness of the
dataset.
Threats to external validity relate to the degree to which our ﬁnd-
ings can be generalized to other LLM safety alignment datasets used
for evaluating guardrail performance. While our SEALGuard ap-
proach is assessed using our curated SEALSBench dataset, the
results may not necessarily generalize to other datasets. To miti-
gate this, we incorporate prompts from six diverse sources [4, 18,
36, 39, 42, 52] during the data collection step when constructing
our SEALSBench dataset, ensuring a broad representation of safe,
unsafe, and jailbreak prompts. The ﬁnal dataset comprises over
260,000 prompts written in ten diﬀerent languages.
8
CONCLUSION
In this paper, we empirically show that LlamaGuard’s Defense
Success Rate (DSR) drops by 9% and 18% under multilingual un-
safe and jailbreak prompts, revealing a critical gap in multilingual
safety alignment for LLM software systems. To address this, we
introduce SEALGuard, a multilingual guardrail adapted via LoRA
from a general-purpose multilingual model, focusing on South-
east Asian languages. We also present SEALSBench, a benchmark
dataset of over 260K prompts across English and nine Southeast
Asian languages, covering safe, unsafe, and jailbreak scenarios.
SEALGuardachieves 97% DSR, 99% precision, and 98% F1-score,
outperforming LlamaGuard by 48%, 8%, and 34%, respectively, while
maintaining robust performance across languages and unsafe types.
REFERENCES
[1] Reda Alami, Ali Khalifa Almansoori, Ahmed Alzubaidi, Mohamed El Amine
Seddik, Mugariya Farooq, and Hakim Hacid. 2024. Alignment with preference
optimization is all you need for llm safety. arXiv preprint arXiv:2409.07772 (2024).
[2] Gabriel Alon and Michael Kamfonas. 2023. Detecting language model attacks
with perplexity. arXiv preprint arXiv:2308.14132 (2023).
[3] Yoshua Bengio, Geoﬀrey Hinton, Andrew Yao, Dawn Song, Pieter Abbeel, Trevor
Darrell, Yuval Noah Harari, Ya-Qin Zhang, Lan Xue, Shai Shalev-Shwartz, et al.
2024. Managing extreme AI risks amid rapid progress. Science 384, 6698 (2024),
842–845.
[4] Rishabh Bhardwaj, Do Duc Anh, and Soujanya Poria. 2024. Language Models are
Homer Simpson! Safety Re-Alignment of Fine-tuned Language Models through
Task Arithmetic. arXiv preprint arXiv:2402.11746 (2024).
[5] Bruce G Buchanan and Edward A Feigenbaum. 1981. DENDRAL and Meta-
DENDRAL: Their applications dimension. In Readings in artiﬁcial intelligence.
Elsevier, 313–322.
[6] Pin-Yu Chen, Han Shen, Payel Das, and Tianyi Chen. 2025. Fundamental Safety-
Capability Trade-oﬀs in Fine-tuning Large Language Models. arXiv preprint
arXiv:2503.20807 (2025).
[7] Yue Deng, Wenxuan Zhang, Sinno Jialin Pan, and Lidong Bing. [n. d.]. Multilin-
gual Jailbreak Challenges in Large Language Models. https://doi.org/10.48550/
arXiv.2310.06474 arXiv:2310.06474 [cs]
[8] Longxu Dou, Qian Liu, Fan Zhou, Changyu Chen, Zili Wang, Ziqi Jin, Zichen Liu,
Tongyao Zhu, Cunxiao Du, Penghui Yang, Haonan Wang, Jiaheng Liu, Yongchi
Zhao, Xiachong Feng, Xin Mao, Man Tsung Yeung, Kunat Pipatanakul, Fajri
Koto, Min Si Thu, Hynek Kydlíček, Zeyi Liu, Qunshu Lin, Sittipong Sripaisarn-
mongkol, Kridtaphad Sae-Khow, Nirattisai Thongchim, Taechawat Konkaew,
Narong Borijindargoon, Anh Dao, Matichon Maneegard, Phakphum Artkaew,
Zheng-Xin Yong, Quan Nguyen, Wannaphong Phatthiyaphaibun, Hoang H. Tran,
Mike Zhang, Shiqi Chen, Tianyu Pang, Chao Du, Xinyi Wan, Wei Lu, and Min
Lin. 2025. Sailor2: Sailing in South-East Asia with Inclusive Multilingual LLM.
arXiv preprint arXiv:2502.12982 (2025).
[9] Tianqi Du, Zeming Wei, Quan Chen, Chenheng Zhang, and Yisen Wang. 2025.
Advancing llm safe alignment with safety representation ranking. arXiv preprint
arXiv:2505.15710 (2025).
[10] Duolingo. 2025. Duolingo - The world’s best way to learn a language. https:
//www.duolingo.com/.
[11] Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav
Kadavath, Ben Mann, Ethan Perez, Nicholas Schiefer, Kamal Ndousse, et al. 2022.
Red teaming language models to reduce harms: Methods, scaling behaviors, and
lessons learned. arXiv preprint arXiv:2209.07858 (2022).
[12] Suyu Ge, Chunting Zhou, Rui Hou, Madian Khabsa, Yi-Chia Wang, Qifan Wang,
Jiawei Han, and Yuning Mao. 2023. Mart: Improving llm safety with multi-round
automatic red-teaming. arXiv preprint arXiv:2311.07689 (2023).
[13] Suhun Han. 2025. googletrans 4.0.2. https://pypi.org/project/googletrans/.
[14] Ahmed E Hassan, Gustavo A Oliva, Dayi Lin, Boyuan Chen, Zhen Ming, et al.
2024. Rethinking Software Engineering in the Foundation Model Era: From
Task-Driven AI Copilots to Goal-Driven AI Pair Programmers. arXiv preprint
arXiv:2404.10225 (2024).
[15] Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean
Wang, Lu Wang, and Weizhu Chen. 2021. Lora: Low-rank adaptation of large
language models. arXiv preprint arXiv:2106.09685 (2021).
[16] Hakan Inan, Kartikeya Upasani, Jianfeng Chi, Rashi Rungta, Krithika Iyer, Yuning
Mao, Michael Tontchev, Qing Hu, Brian Fuller, Davide Testuggine, et al. 2023.
Llama guard: Llm-based input-output safeguard for human-ai conversations.
arXiv preprint arXiv:2312.06674 (2023).
[17] Jailbreak Chat. 2023. Jailbreak Chat Prompt. https://www.jailbreakchat.com/
prompt/4f37a029-9dﬀ-4862-b323-c96a5504de5d Last accessed: 2024-09-20.
[18] Jiaming Ji, Mickel Liu, Josef Dai, Xuehai Pan, Chi Zhang, Ce Bian, Boyuan Chen,
Ruiyang Sun, Yizhou Wang, and Yaodong Yang. 2023. Beavertails: Towards
improved safety alignment of llm via a human-preference dataset. Advances in
Neural Information Processing Systems 36 (2023), 24678–24704.
[19] Daniel Kang, Xuechen Li, Ion Stoica, Carlos Guestrin, Matei Zaharia, and Tat-
sunori Hashimoto. 2024. Exploiting programmatic behavior of llms: Dual-use
through standard security attacks. In 2024 IEEE Security and Privacy Workshops
(SPW). IEEE, 132–143.
[20] Taku Kudo. 2018. Subword regularization: Improving neural network translation
models with multiple subword candidates. arXiv preprint arXiv:1804.10959 (2018).
[21] Alyssa Lees, Vinh Q Tran, Yi Tay, Jeﬀrey Sorensen, Jai Gupta, Donald Metzler, and
Lucy Vasserman. 2022. A new generation of perspective api: Eﬃcient multilingual
character-level transformers. In Proceedings of the 28th ACM SIGKDD conference
on knowledge discovery and data mining. 3197–3207.
[22] Xuan Li, Zhanke Zhou, Jianing Zhu, Jiangchao Yao, Tongliang Liu, and Bo Han.
2023. Deepinception: Hypnotize large language model to be jailbreaker. arXiv
preprint arXiv:2311.03191 (2023).
[23] Yuanchun Li, Hao Wen, Weijun Wang, Xiangyu Li, Yizhen Yuan, Guohong Liu,
Jiacheng Liu, Wenxing Xu, Xiang Wang, Yi Sun, et al. 2024. Personal llm agents:
Insights and survey about the capability, eﬃciency and security. arXiv preprint
arXiv:2401.05459 (2024).
[24] Huijie Lv, Xiao Wang, Yuansen Zhang, Caishuang Huang, Shihan Dou, Junjie Ye,
Tao Gui, Qi Zhang, and Xuanjing Huang. 2024. Codechameleon: Personalized
encryption framework for jailbreaking large language models. arXiv preprint
arXiv:2402.16717 (2024).
[25] Todor Markov, Chong Zhang, Sandhini Agarwal, Tyna Eloundou, Teddy Lee,
Steven Adler, Angela Jiang, and Lilian Weng. 2022. A Holistic Approach to
Undesired Content Detection. arXiv preprint arXiv:2208.03274 (2022).
[26] Todor Markov, Chong Zhang, Sandhini Agarwal, Florentine Eloundou Nekoul,
Theodore Lee, Steven Adler, Angela Jiang, and Lilian Weng. 2023. A holistic
approach to undesired content detection in the real world. In Proceedings of the
AAAI Conference on Artiﬁcial Intelligence, Vol. 37. 15009–15018.
[27] Tula Masterman, Sandi Besen, Mason Sawtell, and Alex Chao. 2024. The landscape
of emerging ai agent architectures for reasoning, planning, and tool calling: A
survey. arXiv preprint arXiv:2404.11584 (2024).
[28] Raymond Ng, Thanh Ngan Nguyen, Yuli Huang, Ngee Chia Tai, Wai Yi Leong,
Wei Qi Leong, Xianbin Yong, Jian Gang Ngui, Yosephine Susanto, Nicholas Cheng,
et al. 2025. Sea-lion: Southeast asian languages in one network. arXiv preprint
arXiv:2504.05747 (2025).
[29] Xuan-Phi Nguyen, Wenxuan Zhang, Xin Li, Mahani Aljunied, Zhiqiang Hu,
Chenhui Shen, Yew Ken Chia, Xingxuan Li, Jianyu Wang, Qingyu Tan, et al.
2023. SeaLLMs–Large Language Models for Southeast Asia. arXiv preprint
arXiv:2312.00738 (2023).
[30] Eugenio Oliveira, Klaus Fischer, and Olga Stepankova. 1999. Multi-agent systems:
which research for which applications. Robotics and Autonomous Systems 27, 1-2
(1999), 91–106.
[31] Alicia Parrish, Angelica Chen, Nikita Nangia, Vishakh Padmakumar, Jason Phang,
Jana Thompson, Phu Mon Htut, and Samuel R Bowman. 2021. BBQ: A hand-built
bias benchmark for question answering. arXiv preprint arXiv:2110.08193 (2021).
[32] Adam Paszke, Sam Gross, Soumith Chintala, Gregory Chanan, Edward Yang,
Zachary DeVito, Zeming Lin, Alban Desmaison, Luca Antiga, and Adam Lerer.
2017. Automatic diﬀerentiation in PyTorch. In NIPS-W.
[33] Maribeth Rauh, John Mellor, Jonathan Uesato, Po-Sen Huang, Johannes Welbl,
Laura Weidinger, Sumanth Dathathri, Amelia Glaese, Geoﬀrey Irving, Iason

--- Page 12 ---\n\nConference acronym ’XX, June 03–05, 2018, Woodstock, NY
Trovato et al.
Gabriel, et al. 2022. Characteristics of harmful text: Towards rigorous bench-
marking of language models. Advances in Neural Information Processing Systems
35 (2022), 24720–24739.
[34] Traian Rebedea, Razvan Dinu, Makesh Sreedhar, Christopher Parisien, and
Jonathan Cohen. 2023. Nemo guardrails: A toolkit for controllable and safe
llm applications with programmable rails. arXiv preprint arXiv:2310.10501 (2023).
[35] Rico Sennrich. 2015. Neural machine translation of rare words with subword
units. arXiv preprint arXiv:1508.07909 (2015).
[36] Xinyue Shen, Zeyuan Chen, Michael Backes, Yun Shen, and Yang Zhang. 2023. "
do anything now": Characterizing and evaluating in-the-wild jailbreak prompts
on large language models. arXiv preprint arXiv:2308.03825 (2023).
[37] Xinyue Shen, Zeyuan Chen, Michael Backes, Yun Shen, and Yang Zhang. 2024. "
do anything now": Characterizing and evaluating in-the-wild jailbreak prompts
on large language models. In Proceedings of the 2024 on ACM SIGSAC Conference
on Computer and Communications Security. 1671–1685.
[38] Speak. 2025. Speak - The language learning app that gets you speaking. https:
//www.speak.com/.
[39] Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li, Carlos
Guestrin, Percy Liang, and Tatsunori B. Hashimoto. 2023. Stanford Alpaca: An
Instruction-following LLaMA model. https://github.com/tatsu-lab/stanford_
alpaca.
[40] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne
Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal
Azhar, et al. 2023. Llama: Open and eﬃcient foundation language models. arXiv
preprint arXiv:2302.13971 (2023).
[41] William Van Melle. 1978. MYCIN: a knowledge-based consultation program for
infectious disease diagnosis. International journal of man-machine studies 10, 3
(1978), 313–322.
[42] Yuxia Wang, Haonan Li, Xudong Han, Preslav Nakov, and Timothy Baldwin.
2023. Do-not-answer: A dataset for evaluating safeguards in llms. arXiv preprint
arXiv:2308.13387 (2023).
[43] Alexander Wei, Nika Haghtalab, and Jacob Steinhardt. 2023. Jailbroken: How
does llm safety training fail? Advances in Neural Information Processing Systems
36 (2023), 80079–80110.
[44] Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue,
Anthony Moi, Pierric Cistac, Tim Rault, Rémi Louf, Morgan Funtowicz, et al.
2019. Huggingface’s transformers: State-of-the-art natural language processing.
arXiv preprint arXiv:1910.03771 (2019).
[45] Yifan Yao, Jinhao Duan, Kaidi Xu, Yuanfang Cai, Zhibo Sun, and Yue Zhang. 2024.
A survey on large language model (llm) security and privacy: The good, the bad,
and the ugly. High-Conﬁdence Computing (2024), 100211.
[46] Zheng-Xin Yong, Cristina Menghini, and Stephen H Bach. 2023. Low-resource
languages jailbreak gpt-4. arXiv preprint arXiv:2310.02446 (2023).
[47] Zheng-Xin Yong, Cristina Menghini, and Stephen H Bach. 2023. Low-resource
languages jailbreak gpt-4. arXiv preprint arXiv:2310.02446 (2023).
[48] Youliang Yuan, Wenxiang Jiao, Wenxuan Wang, Jen-tse Huang, Pinjia He, Shum-
ing Shi, and Zhaopeng Tu. 2023. Gpt-4 is too smart to be safe: Stealthy chat with
llms via cipher. arXiv preprint arXiv:2308.06463 (2023).
[49] Youliang Yuan, Wenxiang Jiao, Wenxuan Wang, Jen-tse Huang, Pinjia He, Shum-
ing Shi, and Zhaopeng Tu. 2023. Gpt-4 is too smart to be safe: Stealthy chat with
llms via cipher. arXiv preprint arXiv:2308.06463 (2023).
[50] Wenxuan Zhang, Hou Pong Chan, Yiran Zhao, Mahani Aljunied, Jianyu Wang,
Chaoqun Liu, Yue Deng, Zhiqiang Hu, Weiwen Xu, Yew Ken Chia, et al. 2024.
Seallms 3: Open foundation and chat multilingual large language models for
southeast asian languages. arXiv preprint arXiv:2407.19672 (2024).
[51] Xuandong Zhao, Will Cai, Tianneng Shi, David Huang, Licong Lin, Song Mei,
and Dawn Song. 2025. Improving llm safety alignment with dual-objective
optimization. arXiv preprint arXiv:2503.03710 (2025).
[52] Andy Zou, Zifan Wang, Nicholas Carlini, Milad Nasr, J Zico Kolter, and Matt
Fredrikson. 2023. Universal and transferable adversarial attacks on aligned
language models. arXiv preprint arXiv:2307.15043 (2023).
\n```\n