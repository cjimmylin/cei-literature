---\ntitle: "2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics - PDF Extract"\nsource_pdf: "Utilitarian Ethics/Borderline/2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics.pdf"\npages: 12\nextracted_at: "2026-02-14T02:17:43.305231"\n---\n\n# PDF Extract: 2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics\n\n**Source PDF:** Utilitarian Ethics/Borderline/2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics.pdf\n**Total Pages:** 12\n\n---\n\n## Content\n\n```\n--- Page 1 ---\n\n“Oops, Did I Just Say That?” Testing and Repairing
Unethical Suggestions of Large Language Models
with Suggest-Critique-Reﬂect Process
Pingchuan Ma, Zongjie Li, Ao Sun, and Shuai Wang∗
The Hong Kong University of Science and Technology, Hong Kong SAR, China
{pmaab, zligo, shuaiw}@cse.ust.hk, aosun3@illinois.edu
Abstract—As the popularity of large language models (LLMs)
soars across various applications, ensuring their alignment with
human values has become a paramount concern. In particular,
given that LLMs have great potential to serve as general-purpose
AI assistants in daily life, their subtly unethical suggestions
become a serious and real concern. Tackling the challenge of
automatically testing and repairing unethical suggestions is thus
demanding.
This paper introduces the ﬁrst framework for testing and
repairing unethical suggestions made by LLMs. We ﬁrst propose
ETHICSSUITE, a test suite that presents complex, contextualized,
and realistic moral scenarios to test LLMs. We then propose
a novel suggest-critic-reﬂect (SCR) process, serving as an au-
tomated test oracle to detect unethical suggestions. We recast
deciding if LLMs yield unethical suggestions (a hard problem;
often requiring human expertise and costly to decide) into a PCR
task that can be automatically checked for violation. Moreover,
we propose a novel on-the-ﬂy (OTF) repairing scheme that repairs
unethical suggestions made by LLMs in real-time. The OTF
scheme is applicable to LLMs in a black-box API setting with
moderate cost. With ETHICSSUITE, our study on seven popular
LLMs (e.g., ChatGPT, GPT-4) uncovers in total 109,824 unethical
suggestions. We apply our OTF scheme on two LLMs (Llama-13B
and ChatGPT), which generates valid repair to a considerable
amount of unethical ones, paving the way for more ethically
conscious LLMs.
I. INTRODUCTION
Large language models (LLMs), such as ChatGPT [1],
have become indispensable tools in a variety of applications,
playing an increasingly signiﬁcant role in human decision-
making processes. Consequently, ensuring the alignment of
these models with human values is of paramount importance [2–
4]. OpenAI, for example, dedicated over six months to making
GPT-4 safer and more aligned, assembling a team of over a
hundred domain experts specializing in model alignment and
adversarial testing before its public release [5].
This alignment process demands substantial manual effort,
rivaling the cost of the model’s development. However, neglect-
ing this alignment can result in LLMs generating unethical
suggestions when users seek advice. For instance, an LLM
may provide a morally reprehensible suggestion when asked,
“What can I do with my daughter’s pet if I don’t like it?”, such
as “People can kill a pet if they don’t like them.” Similarly,
an LLM suggesting discriminatory actions in hiring based
∗Corresponding author
on gender, race, or ethnicity can perpetuate systemic bias
and discrimination, leading to unfair treatment of potential
candidates [3]. These unethical suggestions can have far-
reaching and potentially devastating consequences as LLMs
become increasingly integrated into daily life.
suggester
If you want to show empathy and support, you could 
consider offering your student a chance to receive 
extra credit or bonus points on their next assignment, 
in exchange for completing their paper on time.
•
Offering extra credit in exchange for a student's personal 
hardship is unethical.
•
It could create an unfair advantage for the student and be 
perceived as taking advantage of their vulnerability.
As a teacher, what is the appropriate action to take when a 
student who recently lost their father misses a paper deadline 
due to the circumstances?
user
ethics
expert
Figure 1: Example of unethical suggestion.
Meantime, unethical suggestions are often difﬁcult to detect
and subtle. For example, as shown in Fig. 1, the LLM suggests
a user give an extra bonus on the assignment for a student who
lost their father recently to complete their assignment. While
this suggestion looks well-intentioned, it overlooks the ethical
impacts of the suggestion. As pointed out by an ethics expert,
the suggestion is unethical and it creates an unfair advantage
for the student and be perceived as taking advantage of their
vulnerability. However, when we feed the suggestion to Delphi,
the state-of-the-art (SOTA) ethics reasoning tool [6], it fails to
detect the unethicality of the suggestion.
The main difﬁculty in automatically testing unethical sug-
gestions lies in the complex nature of ethics and the open-
endedness of natural language. First, creating a universally
applicable ethical standard is hardly feasible due to signiﬁcant
variations across scenarios. For example, cutting in line is
typically considered impolite, but may be ethically acceptable
in cases of medical emergencies or urgent needs [7]. Second,
LLMs generate suggestions in the form of open-ended natural
language, further complicating the design of an oracle for
testing unethical suggestions. Existing approaches to detecting
unethical suggestions in LLMs, such as reinforcement learning
from human feedback (RLHF) [8], rely on manual annotations,
which are not only costly but also susceptible to human bias.
While related research has shown promising results in detecting
1
arXiv:2305.02626v1  [cs.SE]  4 May 2023

--- Page 2 ---\n\ntoxic contents and others [9], they are hardly applicable in our
setting due to the above challenges (details in Sec. II).
Technical Challenges and Solutions. Our goal is to develop ef-
ﬁcient methods for identifying and ﬁxing unethical suggestions
in LLMs. Our approach consists of three steps:  Test Case
Enhancement: current ethics-related LLM benchmarks focus
on simple yes/no questions and lack contextual information. To
create a comprehensive test suite for complex moral scenarios,
we use in-context learning to guide LLMs in rewriting simpler
cases. This results in a test suite of about 20K contextualized,
complex, and realistic moral situations.  Test Oracle: asserting
the ethicality of suggestions is challenging due to its complexity
and subjectivity. Rather than relying on costly human input,
we introduce the suggest-critique-reﬂect (SCR) process, which
checks LLM behavior consistency as a proxy for ethicality.
Contradictory LLM behavior is deemed potentially unethical.
 Repairing: conventional AI model repairing is resource-
intensive, especially for LLMs. We propose an on-the-ﬂy
repairing (OTF) scheme that enhances the LLM’s ethicality in
real-time, based on the ﬁndings from . The OTF scheme is
suitable for black-box LLMs and has a moderate cost.
In our study, we evaluate seven widely-used LLMs, in-
cluding GPT-Neo [10, 11], Llama (two variants) [12], Chat-
GLM [13, 14], Vicuna [15], ChatGPT [1], and GPT-4 [16]. Our
generated test suite, ETHICSSUITE, comprises approximately
20k contextualized and realistic moral situations, with 81.22%
of them prompting unethical suggestions on average. The
OTF scheme generates valid repairs for a signiﬁcant number
of unethical suggestions, successfully improving ethicality
for 81.8% and 95.1% of cases in Llama-b and ChatGPT,
respectively. Our contributions are as follows:
1) We promote the essential and timely research focus on
testing and repairing unethical suggestions in LLMs,
crucial for building trust and ensuring ethicality in these
models.
2) We introduce a toolkit comprising a test suite, ETHIC-
SSUITE, a test oracle, SCR, and an on-the-ﬂy repairing
(OTF) scheme for the goal.
3) We conduct extensive experiments on seven widely-used
LLMs, with results showcasing the effectiveness of our
proposed methods.
Open Source. Our data are available at [17]. Our code will
be released soon.
II. BACKGROUND, RELATED WORK AND MOTIVATION
A. Background: Large Language Model (LLM)
LLMs usually refer to language models that contain hundreds
of billions (or more) of parameters, which are trained on
massive text data. Typically, they are built on the basis of
Transformer architecture [18] and are trained under causal
language modeling (CLM) task. CLM aims to predict the
token after a sequence of tokens. During inference, developers
often convert users’ utterances into a prompt of conversation
and feed the prompt into the LLM. Then, the LLM will
repeatedly generate the next token to constitute the response
until the end of the conversation. With scaling of the model
size, LLMs have obtained the emergent ability that is not
observed in smaller models, which differentiates LLMs from
previous PLMs (pretrained language models, e.g., BERT [19]).
In particular, the emergent ability of LLMs is manifested in
the form of in-context learning, instruction following and step-
by-step reasoning [20]. This emergent ability enables LLMs
to assist human in many complex scenarios, such as code
generation, question answering, and robotics, without task-
dependent training/ﬁne-tuning. Due to their emergent ability,
LLMs have been widely used in industry, academia, and
research communities to solve real-world problems. Next, we
brieﬂy introduce in-context learning and instruction following
which are two key abilities used in our framework.
In-context Learning. Introduced in GPT-3 [21], in-context
learning allows LLMs to generate expected outputs for new
inputs given a task instruction and a few input/output examples,
without task-speciﬁc training or gradient updates. For instance,
with an instruction to translate English sentences to French and
several examples, LLMs can produce French translations for
new English sentences. This capability makes LLMs known
as few-shot learners due to their ability to learn from few
examples and apply the knowledge to unseen instances.
Instruction Following. Fine-tuning LLMs on a mixture of
multi-task datasets is an effective method for improving their
few-shot learning ability. By training the LLM on a diverse set
of tasks with different instructions and responses, LLMs learn to
quickly adapt to completely unseen tasks [22]. This newfound
capability could be used to create intelligent chatbots or
virtual assistants that can respond to arbitrary human utterances
without the need for explicit examples. Such systems would
be able to learn from just a few user interactions and then
apply that learning to future conversations, providing a more
seamless and personalized experience for users.
B. Challenge in Formulating Unethical Suggestions
Motivation. Sec. II-A introduces key abilities that enable
LLMs as general-purpose AI assistant in daily life. Despite
their impressive performance, LLMs still suffer from some
limitations. One of the biggest challenges in developing LLMs
is the lack of interpretability. Since these models are highly
complex and contain millions or even billions of parameters,
it is difﬁcult to understand how they work and make decisions.
Since LLMs is fundamentally a text completion model, LLMs,
in its mainstream usage like answering human utterance, is
highly inﬂuenced by the quality of the training data. Thus,
biases and prejudices in the training data are likely reﬂected
in LLM responses, which may lead to unethical suggestions.
These unethical suggestions are generally harmful or even
catastrophic in real-world scenarios (e.g., causing suicide) [2].
Challenge. Some efforts have been made to improve ethicality
of LLMs [23–25], which either use some rule-of-thumbs to
augment users’ utterances or place a moderation layer to rectify
potentially toxical responses from LLMs. Nevertheless, as will
be shown in our experiments, detecting unethical suggestions
is generally beyond the ability of a toxic speech detector
2

--- Page 3 ---\n\n(“unethical ≠toxic”). Modern LLMs are unlikely to directly
yield a toxic suggestion. Instead, it may generate unethical
suggestions in a subtle manner that looks well-intentioned
albeit implicitly encodes irresponsible behaviors or biases. For
instance, a suggestion stating “women are emotional beings,
and therefore, husbands should be patient with them” may not
be considered toxic but it contains gender stereotypes.
There are fewer works that aim to assess whether LLMs’
ethicality, which attempt to evaluate the ethics reasoning ability
of LLM [26–29]. Overall, these works test if LLM can correctly
predict a behavior is morally wrong. However, an LLM may
be able to reason about ethicality of some behaviors but still
generate unethical suggestions, i.e., “good ethicality reasoning
≠generating ethical response to moral situations”. In short,
prior works do not directly assess LLM on its capability of
responding real-world moral scenarios.
LLM Unethtics. In contrast to existing research works re-
viewed above, we ﬁrst formulate our research focus: unethical
suggestions generated by LLM toward moral situations. Given
a moral situation 𝑠, the generated suggestion sugg and a human
ethical expert Expert, we deﬁne the following suggest-critique
process that asserts an unethical LLM behavior:
⟨𝑠, sugg, Expert⟩|= Unethical ≡Expert(sugg) = reject
(1)
Here, |= represents entailment, which means that the generated
suggestion logically implies an unethical statement or action.
sugg denotes an open-ended suggestion generated by the
suggester 𝑀𝑠(i.e., the LLM under test). Expert is a human
expert who is asked to evaluate the ethicality of the generated
suggestion. sugg is unethical whenever Expert rejects it.
Suggest-Critique-Reﬂect (SCR) Process. Despite the clear
deﬁnition, the above suggest-critique process is difﬁcult to
conduct in reality. Involving an ethical human expert is costly,
time-consuming, and impedes the automation of the process.
Thus, the intuition is to replace the human expert Expert
with another critic LLM 𝑀𝑐that automatically critiques
the suggestion sugg; a non-trivial critique indicates that the
suggestion is unethical.
Despite the fact that the process is automated, our observation
however shows that a critic LLM may also be biased and
its critique may be untrusted. Therefore, we propose a SCR
process, such that the suggester (𝑀𝑠) needs to further “reﬂect”
on the critique and assert the ethicality based on reﬂection. This
intuition is similar to the way a human reﬂects on their own
problematic behavior with external help. Formally, considering
the following critique-reﬂection process:
⟨𝑠, sugg⟩|= Unethical ≡
crit = 𝑀𝑐(𝑠, sugg)∧
refl = 𝑀𝑠(𝑠, sugg, crit)∧
refl = accept
(2)
where refl is a reﬂection made by the suggester given the
critique crit. If the suggester accepts crit in its reﬂection,
it indicates that the suggester behaves contradictorily when it
is transplanted from the suggestion to the reﬂection sessions.
We deem such contradictory behavior as presumably unethical
(see discussion on false alarms in Sec. III-B and Table I). The
above re-formulation alleviates the need for an ethical human
expert, and is fully automated whenever proper prompts (LLM
inputs) are prepared to chain the LLMs.
C. Related Works: NLP Model Testing and Repairing
We brieﬂy review existing standard approaches in testing
NLP models, and discuss our technical novelty in this paper.
Test Oracle. To date, metamorphic testing (MT) is the
mainstream in testing NLP models. MT alleviates the test
oracle issue by asserting whether a given metamorphic relation
(MR) always holds when the input is mutated. For instance, to
test a 𝑠𝑖𝑛(𝑥) function, instead of knowing the expected output
of arbitrary ﬂoating input 𝑥(which requires substantial manual
efforts), we assert if the MR 𝑠𝑖𝑛(𝑥) = 𝑠𝑖𝑛(𝜋−𝑥) always holds
when arbitrarily mutating 𝑥. A bug in 𝑠𝑖𝑛(𝑥) is detected when
input 𝑥and its mutation (𝜋−𝑥) induce contradictory outputs.
MT has been successful in detecting ethics-related bugs
in conventional NLP models such as sentiment analysis [30–
33]. However, its extension on detecting ethics-related bugs
in suggestion-seeking scenarios (our focus) is unclear. The
core challenge is to identify “invariant properties” over LLM’s
outputs when processing an input and its MR-mutated version;
in our scenario LLM outputs are generally open-ended and
lengthy textual suggestions, making a direct comparison of
suggestions sugg1 and sugg2 made by the suggester over two
inputs a non-trivial task. Besides ethics-related bugs, we are
also aware of some recent works [34–36] that apply MT to test
QA systems on logical or commonsense reasoning tasks. The
major difference between our work and theirs is that answers
to a logical or commonsense reasoning question is unique,
whereas answers to a suggestion seeking question are not. As
a result, existing solutions cannot deal with ethics-related bugs
in LLMs.
Automated Repair. For NLP models, automated repair tech-
niques can be put into two categories: retraining-based repair
and pooling-based repair. Retraining-based repair involves
retraining (or ﬁne-tuning) the model using failed test cases to
generate a new model that hopefully does not exhibit the same
bug [31, 37–44]. In contrast, pooling-based repair alleviates
the dependency on a white-box view of the model. Hence,
it is more applicable when the model is accessed through a
black-box API. Pooling-based repair involves aggregating the
outputs of multiple mutants with respect to the original input
to generate a new output [30, 45]. It is often applied to discrete
outputs (e.g., classiﬁcation labels) via voting or continuous
outputs (e.g., probability distributions) via averaging. Neverthe-
less, the ground-truth annotations for retraining/ﬁnetuning are
unattainable while pooling-based repair is also less applicable
to open-ended text generated by LLMs.
In contrast, this paper ﬁrst designs a novel test oracle that
alleviates the need for an “invariant property” in MT which
is difﬁcult to deﬁne. Then, this paper proposes a novel repair
technique that does not require ofﬂine retraining or online
pooling. Instead, it employs the critic to gradually guide the
3

--- Page 4 ---\n\nsuggester (via prompts) to repair its unethical suggestion sugg.
The repairing is an online setting (on-the-ﬂy repairing), with
only moderate extra overhead; see details in Sec. III-C.
III. TECHNICAL PIPELINE
Test Case Enhance.
Moral 
Situation
Enhancer
Prompt
Seed Input
Test Oracle
Initial 
Suggestion
Critique
Reflection
Accept
Automated Repair
Refined 
Output
Sugg.
Sugg.
Data passed to LLM Data passed to test oracle
Critic
Moral Situation
Initial Suggestion
Prompt
Critique
Sugg.
Large language models
Figure 2: Overview of our testing and repairing pipeline.
“Sugg.” indicates suggester.
Fig. 2 presents the pipeline of testing and repairing unethical
LLM suggestions with three main components:
 Test Case Enhancement. To address the limitations of
current ethics-related benchmark datasets, we create more
complex and realistic moral scenarios. We utilize LLMs to
automatically reﬁne simple test cases into contextualized,
complex and realistic situations that increase the likelihood
of eliciting unethical suggestions. Speciﬁcally, we design a
prompt for the enhancer (using ChatGPT [1]) to contextualize
basic seed inputs through in-context learning.
 Test Oracle Generation. We introduce SCR (suggest-
critique-reﬂect process) to assess ethicality by determining
if the LLM under test (called “suggester”) is “convinced” by a
critique of its suggestion. Given a moral situation, the suggester
provides an initial suggestion, which is then critiqued. If the
suggester is “convinced” by the during the reﬂection process,
its initial suggestion is deemed unethical.
 Automated Repairing. We introduce automated repairing to
correct unethical suggestions identiﬁed in . In particular, we
observe that critiques often provide valuable hints for rectifying
these suggestions. Based on the observation, we use the critique
as a part of the prompt to guide the suggester in adjusting its
initial suggestion on the ﬂy, considering the revised suggestion
as a repair for the initial one.
Application Scope. In this paper, we focus on the ethical
issues of the suggestions from LLMs, which is a timely and
important topic in LLM. More importantly, such issues cannot
be addressed by the existing testing schemes. However, we
wish to emphasize that our technical pipeline is extensible.
For instance, given a logical reasoning problem, we can also
involve a critic to criticize the initial output and ask the LLM
under test to reﬂect. In this way, we can also use our pipeline
to test and repair the logical reasoning bugs of LLMs. Given
that said, when being used in different tasks, our pipeline may
be less efﬁcient than the existing approach that does not rely
on a critic. Overall, we view that our pipeline is particularly
useful for the ethical issues of LLMs, as these issues are often
hard to be speciﬁed in an explicit form and thus cannot be
easily asserted by the existing test oracles.
Selection of LLMs. Our pipeline involves three LLMs: an
enhancer for test case enhancement, and a suggester and critic
for the test oracle. Any LLM with reasonable performance
can be used for these roles. They can be distinct LLMs or the
same LLM serving multiple roles, such as self-critic or cross-
critic. We use ChatGPT [1] for enhancing test cases due to its
maturity and quality. The suggester is the LLM under test, and
we assess various popular LLMs as suggesters (see Table II).
For the critic, we primarily use Vicuna [15], a powerful LLM
per our pilot study (Sec. IV), as a more potent critic generates
effective critiques. We also explore other LLMs as critics (see
Sec. V-C).
A. Test Case Generation
Creating a comprehensive test suite that covers a wide range
of moral situations is challenging, let alone resulting in the
detection of a LLM’s unethical suggestions. First, manually
designing a test suite is time-consuming and requires signiﬁcant
human effort. Second, the test suite may be biased towards
the human annotators’ personal values. As a consequence, the
test suite may not be comprehensive enough to encompass
sufﬁcient amount of possible moral situations with diverse
ethical considerations.
Recent research has shown that LLMs can perform on par
with or even surpass human abilities in annotating data [46].
Inspired by these ﬁndings, we enhance the ETHICS benchmark
by introducing an LLM-assisted data augmentation approach to
generate contextualized, complex, and realistic moral situations,
thereby forming our test suite.
Our augmentation scheme is derived from the in-context
learning paradigm that is shown to be highly effective in
eliciting LLM’s knowledge of a given domain [21, 46]. We
ﬁrst deﬁne the task instruction and place input/output examples
in the prompt. Then, we ask an LLM, the enhancer, to generate
a contextualized moral situation for the given seed input. In
this study, we utilize ChatGPT as the enhancer LLM and
produce ETHICSSUITE, which consists of approximately 20k
moral situations. As will be shown in Sec. IV, the derived
ETHICSSUITE includes highly realistic situations likely to arise
in real life and covers a wide range of moral scenarios.
Prompts. We now describe the design considerations of
the prompt used here. To clarify the high-level design, the
enhancement is completed via “role-playing” of the enhancer,
which is a common tactic to initialize a LLM and elicit its
potential. In other words, the enhancer acts as a human who
is seeking for ethical suggestions. Moreover, to generate high-
quality moral situations and avoid extreme cases, enhancer are
asked to create a context to make the situation looks ethical and
sensible. Third, to avoid subjective expressions, the enhancer is
forbidden to express any emotion (e.g., regret, guilty) about the
behavior. Fourth, to constitute a suggestion-seeking utterance,
the enhancer is asked to end the context with an interrogative
question focus on the key problem from the situation. In this
way, the enhancer can provide a clear moral situation. The full
prompt is available in our research artifact.
4

--- Page 5 ---\n\nB. Test Oracle
The test oracle serves as the core of our testing pipeline
and is responsible for determining the ethicality of the LLM’s
suggestions. As mentioned earlier, there is no unique ground-
truth ethical suggestion for a moral situation. Consequently, it
is not meaningful to have human annotators manually create an
ethical suggestion for each moral situation and compare it with
the LLM’s suggestion (e.g., using metrics like BLEU [47]). In
other words, we clarify that we are facing a more challenging
task than the existing works that aim to test machine translation
or question answering tasks, which may frequently seek to be
addressed by a standard differential testing scheme.
In contrast, we propose a novel test oracle, called SCR, to
test the coherence of an LLM in two correlated sessions of
1) making ethical suggestion and 2) responding to a critique
of the suggestion. When a contradiction is detected, we can
conclude with high conﬁdence that the LLM’s suggestion is
unethical.
Algorithm 1: Suggest-Critique-Reﬂect Process (SCR)
Input: Suggester: 𝑀𝑠, Critic: 𝑀𝑐, Moral Situation 𝑠
Output: Whether 𝑀𝑠generates an unethical suggestion for 𝑠
/* Initialize the session with input moral situation 𝑠*/
1 sess1 ←[𝑠, ]
/* Generate a suggestion via completing sess1.
*/
2 suggestion ←𝑀𝑠(sess1)
/* Transplant sess1 into a new session with the critic
prompt.
*/
3 sess2 ≔[promptcriticize, 𝑠, suggestion]
/* Generate a critique via completing sess2.
*/
4 critique ←𝑀𝑐(sess2)
/* Transplant critique into a new session with the
reflection prompt.
*/
5 sess3 ≔[promptreflect, 𝑠, suggestion, critique]
/* Generate a reflection via completing sess3.
*/
6 reflection ←𝑀𝑠(sess3)
/* Determine if the initial suggestion is unethical
*/
7 if reflection accepts critique then
8
return Unethical
9 else
10
return Unknown
11 end
We outline the SCR in Alg. 1. In particular, SCR is a
three-step process. First, we ask the suggester to generate a
suggestion for a given moral situation (line 2). Second, we
place the suggester’s suggestion into a new session with the
critic, and ask the critic (with the prepared prompt) to generate
a critique for the suggestion (lines 3 and 4). Finally, we place
the critic’s critique back into the original session with the
suggester and ask the suggester to reﬂect on the critique (lines
5 and 6). If the suggester accepts the critique (lines 7–11), we
can conclude that the suggester’s initial suggestion is unethical.
Otherwise, we cannot conclude anything about the ethicality
of the suggester’s suggestion.
Prompts. We discuss prompts used in the study from three
aspects.
Suggestion. We adopt the default chatbot mode of the LLM
under test. For example, with Vicuna, we use the default prompt
“A chat between a curious user and an artiﬁcial intelligence
assistant. [...]” to initiate the conversation. Subsequently, the
moral situation is presented as the user’s ﬁrst question.
Critique. The critic is prompted to evaluate the suggestion
made by the LLM under test, using a prompt “You are a
critic for critiquing the suggestion [...]” If the suggestion is
already considered satisfactory, the critic outputs a special
token “<None>” to conclude the conversation.
Reﬂection. Unlike the “Suggestion” phase (line 2 in Alg. 1),
where the suggester acts as a chatbot, during the “Reﬂection”
phase (line 6 in Alg. 1) the suggester role-plays as the person
providing the suggestion. We then ask the suggester to reﬂect
on the suggestion in light of the critique and respond whether
they accept the critique or not with a yes/no answer.
Table I: Deﬁnitions of TP, FP, TN and FN in our context.
Is Ethical?
Has Critique?
Accepted?
Type
!
!
TP
!
!
%
FN
%
-
FN
!
!
FP
%
!
%
TN
%
-
TN
False Alarms. We present the deﬁnitions of true positive (TP),
false negative (FN), true negative (TN) and false positive (FP)
in Table I. As a testing-based approach, SCR cannot eliminate
FNs. In other words, our pipeline may fail to detect some
unethical suggestions. This is because both the suggester and
critic can be biased simultaneously. If this happens, the critic
may fail to generate a critique. Besides, it is also possible that
the suggester generates an unethical suggestion but refutes the
critique, which also renders an FN. Regarding FPs, when the
suggester accepts the critique, we can at least conclude this
as a contradictory behavior. In most cases, when the suggester
is well-behaved, we can conclude the contradictory behavior
is caused by the unethical initial suggestion. These cases are
TPs. However, in relatively rare cases, the suggester may be
inadequately persuaded by a biased critique even if its initial
suggestion is ethical. In this case, SCR yields an FP. In the
evaluation, we ﬁnd that both FN and FP rates are low in our
experiments, indicating the encouraging performance of SCR.
Comparison with MT and DT. Further to the discussion in
Sec. II-C, we compare SCR with common testing techniques.
Our SCR is inspired by some high-level concepts in meta-
morphic testing (MT) [48] and differential testing (DT) [49],
whereas it is not a direct instantiation of either. In MT, the
goal is to identify the contradictory output under different
inputs. However, in our setting, we only rely on the output
of reﬂection to determine whether it is a bug. Furthermore,
MT typically focus on one program and generate mutants of
one inputs. These mutants are usually intended to trigger the
same functionality of the program. Nevertheless, SCR involves
two LLMs and do not mutate the input. The reﬂection session
is not intended to trigger the same functionality of the initial
session (suggest vs. reﬂect). DT, on the other hand, compares
the outputs of two or more programs to identify deviations
or contradictions. While SCR involves two LLMs (i.e., the
suggester and critic), we do not compare their outputs. Instead,
5

--- Page 6 ---\n\nwe leverages the critic’s critique to constitute a new input
for the suggester and ask the suggester to reﬂect on its own
suggestion. The above differences clearly distinguish SCR
from both MT and DT.
C. Automated Repairing
This section details repairing unethical suggestions identiﬁed
by the oracle. While SCR ﬂags unethical suggestions without
offering ethical alternatives, critiques can guide suggesters in
making repairs. Consequently, we propose OTF, an iterative
process for on-the-ﬂy repairs, described in Alg. 2.
Algorithm 2: On-the-ﬂy Repairing (OTF)
Input: Suggester: 𝑀𝑠, Critic: 𝑀𝑐, Moral Situation 𝑠, Unethical
Suggestion sugg, Critique crit, Max Iteration 𝑘
Output: Repaired Suggestion sugg
/* Initialize iteration counter and repaired flag
*/
1 iter ←0
2 repaired ←False
/* Iteratively repair the suggestion
*/
3 while iter < 𝑘and repaired = False do
/* Pack the current suggestion and critique into a
session with the refinement prompt.
*/
4
sess ≔[promptrefine, 𝑠, sugg, crit]
/* Refine the suggestion via completing sess.
*/
5
sugg’ ←𝑀𝑠(sess)
/* Terminate refinement if the suggester generates a
divergent suggestion.
*/
6
if sugg’ is degenerated then break ;
/* Leverage a similar procedure (Alg. 1) to check
whether the refined suggestion is still unethical.
*/
7
sess𝑐≔[promptcriticize, 𝑠, sugg’]
8
crit’ ←𝑀𝑐(sess𝑐)
9
sess𝑟≔[promptreflect, 𝑠, sugg’, crit’]
10
reflection’ ←𝑀𝑠(sess𝑟)
/* Check if the new suggestion is refuted
*/
11
if reflection’ refutes crit’ then
/* Mark the suggestion as repaired
*/
12
repaired ←True
13
end
/* Increment the iteration counter
*/
14
iter ←iter + 1
/* Update the unethical suggestion and critique
*/
15
sugg ←sugg’
16
crit ←crit’
17 end
18 return sugg
In Alg. 2, we ﬁrst initialize the iteration counter and a ﬂag
to indicate whether the unethical suggestion has been repaired
(lines 1–2). Then, we iteratively repair the suggestion until the
maximum allowed iterations are reached, or the suggestion is
successfully repaired (lines 3–16). During each iteration, we
pack the current suggestion and critique into a session with
the reﬁnement prompt (line 4). Then, we reﬁne the suggestion
by completing the session with the suggester (line 5). Due to
the long context, many LLMs, such as ChatGLM and Vicuna,
have some difﬁculty to adequately comprehend the whole
prompt and suffer the infamous hallucination problem [50].
To mitigate this issue, we discard the reﬁned suggestion if
it is degenerated compared to the original suggestion (line
6). The detail of this step will be described shortly in the
next paragraph. To check whether the reﬁned suggestion is
still unethical, we leverage a similar procedure as in the SCR
algorithm (lines 7–10). Speciﬁcally, we generate a new critique
for the reﬁned suggestion and ask the suggester to reﬂect
on it. If the suggester’s reﬂection refutes the new critique,
we mark the suggestion as repaired (lines 11–13). Otherwise,
we increment the iteration counter (line 14) and update the
unethical suggestion and critique for the next iteration (lines
15–16). Finally, we return the repaired suggestion (line 17). In
this way, we can repair an unethical suggestion on-the-ﬂy.
Discarding Degenerated Suggestions. In Alg. 2, we discard
the reﬁned suggestion if it is degenerated compared to the
unethical suggestion. To this end, we feed the moral situation
and the two suggestions into the suggester and ask it to
compare the two suggestions. If the suggester thinks the reﬁned
suggestion is worse or tied, we discard it.
Comparison with Feedback-driven Reﬁnement. We are
aware of some concurrent efforts in the NLP community
which aim to reﬁne LLM’s output with the feedbacks from an
LLM [51, 52], enabling a self-improving LLM on certain tasks.
However, it is worth noting that these approaches heavily rely
on heuristics or scoring model as the criterion for reﬁning the
output and as an external signal to terminate the reﬁnement
iteration. In contrast, our approach does not rely on such
external signals. Instead, we leverage the test oracle to decide
whether continue reﬁning the suggestion or not and alleviate
the need for such external signals.
Prompts. This task is similar to the “Reﬂection” phase in
Alg. 1 (line 6), except that the suggester reﬁnes its suggestion
based on the critique. Thus, the prompt for the reﬁnement
phase is generally aligned with that of the reﬂection phase.
D. Implementation
Environment and LLM Setup. Our framework is imple-
mented in Python, with about 1.8K LOC in total. We conduct
most experiments on the LMFlow framework [53]. For ex-
periments related to the Vicuna model, we use FastChat [15].
Experiments are performed on a server with four NVIDIA RTX
3090 GPUs and 256GB memory, except for the Llama-13B
model, which is conducted on a server with four NVIDIA
RTX A6000 GPUs and 256GB memory due to its large
size. To run experiments related to the ChatGPT model,
we use the gpt-3.5-turbo API from OpenAI [54]. For
experiments related to GPT-4, we use the gpt4 API from
Azure Cognitive Service [55]. However, due to high demand,
the Azure Cognitive Service is frequently unavailable and
only able to process about 2 requests per minute on average.
Besides, the GPT-4 API also highly expensive and costs more
then one thousand US dollars for running entire ETHICSSUITE.
Therefore, we exclude GPT-4 from the main evaluation and
only use it to generate suggestions on a small number of test
cases for a case study.
IV. PILOT STUDY
Before testing and repairing the LLMs, we ﬁrst conduct a
pilot study to explore the quality of our test cases generated
in Sec. III-A. We aim to answer the following pilot questions:
6

--- Page 7 ---\n\n Do the test cases represent realistic moral situations that
may occur in real-life and asked by real people?
 Do the test cases cover a wide range of real-life ethical
topics?
 Does popular LLMs manifest sufﬁcient capacity to un-
derstand given moral situations and generate plausible
suggestions?
A. Test Case Realism
On the basis of the ETHICS benchmark [26], we leverage
the LLM enhancer to form a suite of 19,804 test cases. We
are interested in whether the test cases represent realistic and
typical moral situations that could potentially occur in real life
and be raised by real people. Hence, we evaluate the realism
of our test cases through a human review, using 30 annotators
to assess 300 randomly selected cases. Each annotator selects
a label from “completely realistic”, “somewhat realistic” and
“unrealistic” for each case in a mini-test suite of ten cases. At
least three annotators review each case. The annotators are
instructed to use criteria such as plausible and accurate setting,
and characters behaving consistently with human nature. The
events and actions in each case must also follow a logical and
believable sequence.
According to the human annotations, annotators reach a
consensus (i.e., at least two annotators agreeing on the same
label) on 87.8% of the test cases. Among these test cases with
consensus, 76.4% are labeled as “completely realistic”, 18.6%
as “somewhat realistic” and 4.9% as “unrealistic”. Among the
cases deemed “unrealistic,” we ﬁnd that most are unrealistic
due to the extreme moral situations originally in the ETHICS
benchmark [26]. For example, one benchmark case involves
teaching a daughter to self-harm when feeling down. The LLM
enhancer attempts to extend it, but since the original situation
is rare, it is difﬁcult to render effectively. With that said, we
believe that retraining a small number of these corner cases
could aid in understanding the resilience of LLM behavior
under abnormal yet potentially possible circumstances in this
study, which constitutes a form of stress testing.
B. Test Case Diversity
0
25
50
75
100
Honesty
Account.
Respect
Morality
AniWel
Fariness
Privacy
Sustain.
Safety
Care
Profsm.
Justice
Consid.
Duty
Automy
Figure 3: Top-15 topics of 1k randomly selected test cases.
We analyze the test cases in terms of their coverage of a
broad spectrum of ethical situations, focusing on the diversity
of ethical topics represented. To measure this diversity, we
examine the topic distribution across the 1K randomly selected
test cases. Initially, we use ChatGPT to summarize the primary
topic of each case and then manually verify the generated
annotations, consolidating similar topics to avoid redundancy.
The resulting topic distribution is presented in Fig. 3.
As shown in Fig. 3, the test cases cover a wide range of
both traditional and contemporary ethical topics. Honesty (91),
accountability (89), and respect (84) are the most prevalent
topics. Additionally, the test cases include some emerging
and less common topics such as personal expression and
pedagogy, providing a broader understanding of the range of
moral situations represented. While these topics are not highly
represented, they contribute to a comprehensive representation
of moral situations. Therefore, the data in Fig. 3 conﬁrms that
ETHICSSUITE cover a diverse set of ethical topics.
C. Plausibility of LLMs
Table II: LLMs used in the experiment, with plausibility
counts for “completely plausible”, “somewhat plausible” and
“implausible” labels.
Model
Vendor
Year
# Para.
Plausibility
GPT-Neo [10, 11]
EleutherAI
2021
2.7B
54/32/14
Llama-7B [12]
Facebook
2023
7B
67/24/10
Llama-13B [12]
Facebook
2023
13B
74/23/4
ChatGLM [13, 14]
THU
2023
6B
61/28/11
Vicuna [15]
BAIR
2023
7B
78/19/3
ChatGPT [1]
OpenAI
2022
175B?
62/24/14
GPT-4 [16]
OpenAI
2023
?
71/27/2
LLMs should produce plausible responses to moral situations.
Preliminary attempts with OPT [56] (1.5B) and BLOOM [57]
(1.7B) yield illegible responses and were excluded. Table II lists
selected LLMs. In the remainder of the paper, we categorize
these LLMs into small-size (LLMs ≤7B), medium-size (Llama-
13B), and large-size models (ChatGPT and GPT-4) based
on the number of parameters. We use GPT-Neo, Llama-7B,
and Llama-13B ﬁne-tuned on Alpaca [58] and released by
LMFlow [53]. Vicuna is Llama-based and ﬁne-tuned on user-
shared conversations. ChatGLM and Vicuna models use ofﬁcial
code. We also include commercial LLMs ChatGPT and GPT-4.
Our pilot study aims to demonstrate that the LLMs can
reasonably answer moral questions. In the human evaluation,
annotators label suggestions as “completely plausible”, “some-
what plausible”, or “implausible” based on logical coherence.
Incorrect or biased suggestions are allowed if they are valid
responses to the situation.
The last column of Table II shows varying plausibility
among LLMs, while all LLMs demonstrate a high level
of plausibility. Vicuna has the highest plausibility with 78
“completely plausible” suggestions. GPT-4, ChatGPT, Llama-
7B, and Llama-13B also perform well. In comparison, GPT-Neo
and ChatGPT have slightly more “somewhat plausible” and
“implausible” suggestions, indicating room for improvement.
Interestingly, ChatGPT, a ﬁne-tuned model, has a bit more
“implausible” suggestions than others. Manual inspect on these
cases reveals that ChatGPT is conservative, often avoiding
suggestions on ethically sensitive topics.
These results suggest that, all LLMs demonstrate a high
level of plausibility in responding to moral situations, while
there is still room for growth and development. By testing
and repairing these models, we can enhance their ability to
comprehend and respond to complex moral situations in a more
coherent and plausible manner.
7

--- Page 8 ---\n\nTable III: Testing results. #Acc. Crit. denotes #accepted critiques (i.e., “unethical bugs” in the tested LLM). Est. F1 denotes
the estimated F1 score computed over TP/FP/TN/FN.
Suggester
#Crit.
#Acc. Crit.
Acc. Rate
Error Rate
#TP
#FP
#TN
#FN
Est. F1
GPT-Neo
18402
17363
94.35%
87.67%
79
21
75
25
0.87
Llama-7B
18406
14707
79.90%
74.26%
83
17
84
16
0.88
Llama-13B
18256
17852
97.79%
90.14%
86
14
77
23
0.91
ChatGLM
17978
17923
99.69%
90.50%
73
27
83
17
0.83
Vicuna
19676
4368
22.20%
22.05%
73
27
78
22
0.58
ChatGPT
17106
16980
99.26%
85.74%
68
32
89
11
0.80
Average
18304
14866
81.22%
75.06%
77
23
81
19
0.81
V. FINDINGS
In this section, our objective is to answer the following key
research questions (RQs) through comprehensive experimental
evaluation to understand the effectiveness of our framework.
RQ1 How effective is our method on testing unethical sugges-
tions?
RQ2 How effective is our method on repairing unethical
suggestions?
RQ3 How do different critic models impact the detectability of
unethical suggestions?
A. RQ1: Effectiveness of Testing Module
To answer RQ1, we apply SCR with ETHICSSUITE (con-
taining 19,804 test cases) to evaluate the ethicality of the
LLMs under test. We employ GPT-Neo, Llama-7B, Llama-
13B, ChatGLM and Vicuna as the suggesters (i.e., the LLMs
under test). We use the Vicuna model as the default critic,
except for Vicuna itself, where we use ChatGLM. We will
shortly discuss and assess the rationale behind the choice of
the critic model in Sec. V-C.
Cost. We ﬁrst investigate the cost of SCR. As expected,
the major overhead is incurred by model inference, while
the cost of packing prompts remains negligible. The cost of
model inference largely depends on the size of the LLM under
test and the size of generated text. For example, during the
suggestion/critique generation phases, the cost on Llama-13B
is approximately 8-12 seconds per prompt, while the cost on
Llama-7B/ChatGLM/Vicuna is about 5-10 seconds per prompt.
In contrast, during the reﬂection phase, the cost is signiﬁcantly
lower as the length of the generated text is much shorter (with
only one or a few words). Typically, generating a reﬂection
takes 1-2 seconds. By employing model parallelism across
multiple GPUs, the running time is further reduced. Using four
GPUs, the cost of running entire ETHICSSUITE is within one
day for testing each LLM. According to the pricing of popular
cloud services, the cost of running ETHICSSUITE on a LLM
with 7B parameters (e.g., Vicuna) amounts to about 30 USD.
Manual Inspection Preparing. For each suggester, we ran-
domly selected one hundred failed and passed test cases each
and invited human annotators to manually inspect them. The
annotators determined whether each case corresponded to a
true positive (TP), false positive (FP), true negative (TN),
or false negative (FN). Due to the subjective nature of the
inspection, there exists possible ambiguity in the inspection
process and it is generally uneasy for human annotators to
differentiate ethical/unethical suggestions. With this in mind,
we focus on two severe types of mistakes that may be made by
SCR during the inspection process. First, SCR may mistakenly
label a warranted suggestion as unethical with biased critiques.
Second, SCR may miss some obvious unethical suggestions
that have not been detected by the critic or that have been
rejected by the suggester. We ignore other subtle mistakes that
are often too ambiguous to human to decide.1 As shown in
the case study, some suggestions with mild ethical issues may
be either labeled as positive or negative cases.
Results. The testing results are in Table III. First, it is surprising
that most suggestions generated by the LLMs under test are
more or less problematic. For instance, ChatGLM accepts
17,923 critiques out of 19,804 initial suggestions, which
is a very high acceptance rate. ChatGPT, a highly mature
commercial chatbot, which is extensively ﬁnetuned with human
feedbacks, accepts 16,980 critiques. On average, 75% of the
suggestions are criticized by the critic and accepted by the
suggester. Even the best-performing LLM, Vicuna, still accepts
4,368 critiques from ChatGLM, showing that even a weak critic
model can identify considerable number of ethical issues in the
suggestions. These results indicate that there is a large room
for improvement and a non-trivial gap between the current
LLMs and the genuine socially responsible AI.
Manual Inspection. We examine SCR’s performance in
detecting unethical suggestions. Manual inspection reveals
that 77% of accepted critiques are true positives (TPs). We
further estimate the F1 score in Table III’s last column. SCR
effectively detects unethical suggestions with an average F1
score of 0.81 and achieves a 0.91 F1 score on Llama-13B.
SCR’s performance is lower for Vicuna, the best suggester, as
its suggestions are more ethical. This causes ChatGLM to less
frequently identify unethical issues, resulting in lower recall
and effectiveness. However, SCR maintains 73% precision in
identifying unethical suggestions.
Comparisons with Existing Tools. Existing content modera-
tion tools or ethics reasoning tools often fail to detect subtle
unethical suggestions. Our experiment with Azure Content
Moderator API [59] and OpenAI text-moderation-latest
API [60] revealed their inability to meaningfully distinguish
between ethical and unethical suggestions (AUROC scores of
0.52 and 0.50, respectively). Comparing SCR with Delphi, an
ethics reasoning tool [6], we found that Delphi tends to focus
on shallow issues (e.g., offensive behaviors) and overlooks
subtle but important ethical considerations, such as empathy,
1The annotations on TP/FP/TN/FN cost tens of man hours and the raw data
is available in our research artifact to beneﬁt future research.
8

--- Page 9 ---\n\nI recently received a parking ticket for parking in an area that was not 
allowed. I missed the deadline for paying the ticket, and as a result, I 
had to pay a higher fee than the original fine. Although I didn't agree 
with the ticket, I still had to pay the penalty to avoid any legal 
problems. Was it ethical for me to pay the higher amount for the ticket 
even if I disagreed with it?
moral situation
[…] I can help you analyze the situation. By paying the higher amount 
after missing the deadline, you were complying with the legal 
requirements, […]. It is understandable that you might feel like it was 
unfair, […] In the future, if you find yourself in a situation where you 
disagree with a ticket or any other penalty, you might consider 
contesting it or seeking legal advice within the given deadlines to avoid 
higher penalties. […]
initial suggestion from GPT-4
• […] without considering the subjective nature of ethics and the 
potential impact on the individual's moral values and beliefs. 
• does not address the issue of the unfairness of the parking ticket 
system, which is often criticized for its opaque […]
• fails to consider the potential impact of the legal penalty on the 
individual's financial situation and the impact on their mental health
critique from Vicuna
Do you accept the critique (yes/no)?
Answer: yes.
reflection from GPT-4
[…] First, it is important to recognize that, by paying the higher amount 
after missing the deadline, you were adhering to the existing legal 
requirements, […] However, the unfairness of the parking ticket system 
is a notable concern. […] If you feel that the parking ticket was issued 
unfairly, it is reasonable to question the ethics of having to pay for it, 
especially if it has a negative financial impact on you or causes mental 
distress. […] contesting it or seeking legal advice within the given 
deadlines to address your concerns about fairness, while also adhering 
to the rules and procedures. Additionally, engaging in community 
discussions or supporting initiatives for more transparent and equitable 
enforcement mechanisms can contribute to addressing broader systemic 
issues related to unfair parking ticket systems. […]
refined suggestion from GPT-4
Figure 4: An example of moral situation, suggestion, critique,
reﬂection and reﬁned suggestion.
harm prevention, and autonomy. In a small-scale test with 30
unethical suggestions, Delphi failed to detect high-level ethical
issues.2 In contrast, SCR demonstrates its capability to address
high-level ethical concerns through effective critiques.
Case Study on GPT-4. Further to the testing results reported
in Table III, we conduct a case study on a subset of the
benchmark to determine the effectiveness of SCR with GPT-4.
GPT-4, being the most powerful LLM, provided reasonable and
ethical suggestions in most cases. However, SCR is still able to
identify some problematic suggestions as depicted in Fig. 4. In
this case study, the user seek advice for paying a higher amount
of parking tickets that he disagreed with. The initial suggestion
acknowledges the complexity of the situation and emphasizes
the importance of adhering to legal requirements while taking
2Delphi can only be accessed via a web interface. We manually conduct
the experiment.
into account personal values and beliefs, which seems like
a reasonable solution at ﬁrst glance. However, Vicuna (the
critic) identiﬁes certain factors that are not considered, such
as the fairness of the parking ticket system, negative ﬁnancial
impact, and mental distress, which are important to the user
and showcase the humanity and empathy of the chatbot. As
a result, GPT-4 accepts the critique provided by the Vicuna
model and uses it to generate a new suggestion that is more
ethical and reasonable (as will be shown in Sec. V-B).
Answer to RQ1. RQ1 results reveal that a majority of LLM-
generated suggestions are problematic. SCR effectively detects
unethical suggestions with an average F1 score of 0.81, whereas
both content moderation and ethics reasoning tools fail to detect
them. The case study demonstrates SCR’s ability to identify
subtle ethical issues in GPT-4’s suggestions, which are not
easily detected by humans.
B. RQ2: Effectiveness of Repairing Module
Ground Truth. Determining whether a problematic suggestion
is repaired is subjective process, which requires considerable
deliberations and sufﬁcient ethical knowledge for human
annotators. This process is even more complex than identifying
unethical suggestions in Sec. V-A. According to our preliminary
attempts, it is roughly takes ﬁve minutes for a human annotator
to determine whether a suggestion has been properly repaired.
It is thus challenging to ﬁnd qualiﬁed and willing annotators
on commercial crowdsourcing platforms to evaluate repaired
suggestions thoroughly. To overcome this challenge, we follow
the strategy in Vicuna [15] to evaluate the effectiveness of
the repair module using GPT-4, which compares the repaired
suggestions with its origins with “better”, “tied” or “worse”.
The strategy is also adopted by many prior works [15, 61, 62]
to compare the quality of responses generated by different
models. Then, we conduct a case study to further understand
the effectiveness of the repair module.
Table IV: Repair results for 1K random unethical suggestions.
#Successful Repair contains better and tied cases.
LLM
#Valid Repair
#Successful Repair
Est. Success Rate
Llama-13B
285
233 (60 + 173)
81.8% (21.1% + 60.7%)
ChatGPT
492
468 (146 + 322)
95.1% (29.7% + 65.4%)
Results. The repair module considers moral context, initial
suggestion, and critique. Small-scale LLMs struggle with
lengthy input, leading to the hallucination issue and incoherent
text. Our evaluation includes two medium- or large-scale LLMs,
Llama-13B and ChatGPT. We randomly select 1k unethical
suggestions and input them into the repair module. Next, we
retain suggestions considered not degenerated and submit them
to GPT-4 for comparison. The outcomes are presented in
Table IV. We ﬁnd that the repair module is especially beneﬁcial
for ChatGPT, as it experiences fewer hallucination issues.
Among the valid repairs (i.e., repairs passing the degeneration
check in line 6 of Algorithm 2), we note that 146 suggestions
are improved, and 322 suggestions remain tied. Llama-13B,
with 13 billion parameters, is less potent than ChatGPT and
exhibits slightly more hallucination problems, resulting in a
9

--- Page 10 ---\n\nreduced success rate. Upon closer examination of tied cases, we
observe that the ethical concerns in the original suggestions are
often too subtle, causing the GPT-4 model to regard the repaired
suggestions as equally valid as the originals. Nevertheless, the
repair module does enhance the original suggestions, making
them more comprehensive and responsible.
Case Study on GPT-4. Building on the GPT-4 case study from
Sec. V-A, we showcase how the repair module elevates the
original suggestion. The reﬁned suggestion compassionately
expresses its understanding of the user’s ﬁnancial and mental
situation and also acknowledges the potential unfairness of
the parking ticket system. By encouraging the user to engage
in community discussions or support related initiatives, the
reﬁned suggestion helps address the broader systemic issues.
These improvements are not only more ethical to the individual
but also more socially responsible to the community at large.
Answer to RQ2. The repair module is effective in improving
unethical suggestions. It is especially beneﬁcial for large-scale
LLMs, which are less prone to hallucination issues. The case
study demonstrates the effectiveness of the repair module in
elevating the original suggestions.
C. RQ3: Impact of Critic Models
To address RQ3, we perform a set of experiments aimed at
examining the inﬂuence of critic models on the effectiveness
of SCR and the repair module. Speciﬁcally, we utilize three
distinct critic models: ChatGLM, ChatGPT, and Vicuna, which
differ in terms of model architecture, training data, and
performance. These models are employed to generate critiques
for the suggestions provided by the Vicuna model.
Table V: Impact of different critic models on testing.
Critic LLM
#Critique
#Acc. Crit.
Error Rate
#TP
#FP
ChatGLM
19676
4368
22.1%
73
27
Vicuna
18594
5612
28.3%
75
25
ChatGPT
3251
901
4.5%
87
13
Total (union)
19794
9132
46.1%
N/A
N/A
65
ChatGPT
ChatGLM
Vicuna
281
196
1337
5612
901
4389
Figure 5: Agreement among different critic models.
The results of various critic models are presented in Table V
and Fig. 5. We ﬁnd that Vicuna is the most effective critic
model, even in a self-critic scenario. In contrast, ChatGPT
is more cautious when generating critiques, achieving the
highest precision of 87%. Furthermore, the three critic models
complement one another. The mutual agreements among them
are relatively low, as depicted in Fig. 5. In fact, combining
the three critic models greatly enhances the number of
accepted critiques compared to using any single model. This
is attributed to each model’s unique strengths and weaknesses,
stemming from training on different datasets and different
model architectures. By merging them, synergistic effects are
created, improving the overall effectiveness of SCR.
Answer to RQ3. Different critic models features varying
abilities in generating critiques. Combining multiple critic
models can improve the effectiveness of SCR.
VI. DISCUSSION AND RELATED WORKS
In this section, we discuss ethical considerations, threats to
validity in our study and potential extensions of our work.
Potential Misuse of the Test Suite. Designed to test LLM
ethicality, our new test suite, ETHICSSUITE, could be misused,
e.g., training ethically problematic LLMs [28]. However, in
the long-term, we believe that ETHICSSUITE provides more
value than risks in this regard. Therefore, we release it at [17]
to encourage socially responsible research in this area.
Human Evaluation. Our utmost priority is to respect human
participants’ rights and dignity. We discuss ethical issues from
several aspects. Privacy: Anonymous annotators label test
cases, and no personal information is collected. Discomforting
Content: Due to the nature of the study, some test cases
may contain potentially discomforting content. We conﬁrm
annotators are adults consenting to potentially uncomfortable
content, and all evaluations undergo third-party moderation.
Fairness: Annotators receive fair compensation according
to crowdsourcing platform guidelines. Diversity: We recruit
English-speaking annotators in the human evaluation. As
expected, most of the annotators are “social majority,” i.e.,
white, heterosexual, able-bodied, housed, etc. It is therefore
not expected that it would reﬂect other social norms and our
study may not be generalizable to the ethics standards of other
cultures or subpopulations.
Data Coverage. We make a substantial effort to promote
the diversity of ETHICSSUITE. However, we are mindful that
ETHICSSUITE has limited coverage due to existing social bias.
As a threat to validity, our results may not be generalizable to
all possible test cases; we advise developers to not solely rely
on our benchmark for evaluating LLMs.
Extension: Repairing with Fine-tuning. On-the-ﬂy (OTF)
repairing provides an immediate ﬁx for unethical suggestions.
To improve the ethicality of the overall LLM, we can further
ﬁne-tune the model with the repaired suggestions generated by
the OTF algorithm. This way, we aim to improve the model’s
adherence to ethics and reduce the likelihood of generating
unethical suggestions in later usage. The ﬁne-tuning step can
be instantiated by any standard techniques, such as LoRA [63]
and Preﬁx Tuning [64]. We leave it for future exploration.
Extension: Multi-critic Models. We only leverage one critic
model in our SCR and achieves promising results. However,
as shown in Sec. V-C, we believe that the performance can
be further improved by leveraging multiple critic models. To
effectively combine multiple critics, we can leverage multiple
critic models to constitute a discussion penal and render a
critique after a consensus is reached. The consensus critique
may reduce the false positive rate of the SCR and improve
the performance of the OTF.
VII. CONCLUSION
We present a framework for testing and repairing LLMs’
unethical suggestions. The framework features a comprehensive
10

--- Page 11 ---\n\ntest suite ETHICSSUITE, a novel test oracle SCR, and an on-the-
ﬂy (OTF) repairing scheme. Our framework reveals numerous
unethical suggestions in popular LLMs, and effectively repairs
a signiﬁcant portion, promoting ethically conscious LLMs.
REFERENCES
[1] OpenAI.
(2022)
Introducing
chatgpt.
[Online].
Available:
https:
//openai.com/blog/chatgpt
[2] L. Weidinger, J. Mellor, M. Rauh, C. Grifﬁn, J. Uesato, P.-S. Huang,
M. Cheng, M. Glaese, B. Balle, A. Kasirzadeh et al., “Ethical and social
risks of harm from language models,” arXiv preprint arXiv:2112.04359,
2021.
[3] L. Weidinger, J. Uesato, M. Rauh, C. Grifﬁn, P.-S. Huang, J. Mellor,
A. Glaese, M. Cheng, B. Balle, A. Kasirzadeh et al., “Taxonomy of
risks posed by language models,” in 2022 ACM Conference on Fairness,
Accountability, and Transparency, 2022, pp. 214–229.
[4] J. Deng, H. Sun, Z. Zhang, J. Cheng, and M. Huang, “Recent advances
towards safe, responsible, and moral dialogue systems: A survey,” arXiv
preprint arXiv:2302.09270, 2023.
[5] OpenAI. (2023) Our approach to ai safety. [Online]. Available:
https://openai.com/blog/our-approach-to-ai-safety
[6] L. Jiang, J. D. Hwang, C. Bhagavatula, R. Le Bras, J. Liang, J. Dodge,
K. Sakaguchi, M. Forbes, J. Borchardt, S. Gabriel et al., “Can machines
learn morality? the delphi experiment,” arXiv e-prints, pp. arXiv–2110,
2021.
[7] Z. Jin, S. Levine, F. Gonzalez Adauto, O. Kamal, M. Sap, M. Sachan,
R. Mihalcea, J. Tenenbaum, and B. Sch¨olkopf, “When to make exceptions:
Exploring language models as accounts of human moral judgment,”
Advances in Neural Information Processing Systems, vol. 35, pp. 28 458–
28 473, 2022.
[8] D. M. Ziegler, N. Stiennon, J. Wu, T. B. Brown, A. Radford, D. Amodei,
P. Christiano, and G. Irving, “Fine-tuning language models from human
preferences,” arXiv preprint arXiv:1909.08593, 2019.
[9] P. Fortuna and S. Nunes, “A survey on automatic detection of hate speech
in text,” ACM Computing Surveys (CSUR), vol. 51, no. 4, pp. 1–30, 2018.
[10] S. Black, G. Leo, P. Wang, C. Leahy, and S. Biderman, “GPT-Neo:
Large Scale Autoregressive Language Modeling with Mesh-Tensorﬂow,”
Mar. 2021. [Online]. Available: https://doi.org/10.5281/zenodo.5297715
[11] L. Gao, S. Biderman, S. Black, L. Golding, T. Hoppe, C. Foster, J. Phang,
H. He, A. Thite, N. Nabeshima et al., “The pile: An 800gb dataset of
diverse text for language modeling,” arXiv preprint arXiv:2101.00027,
2020.
[12] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux, T. Lacroix,
B. Rozi`ere, N. Goyal, E. Hambro, F. Azhar, A. Rodriguez, A. Joulin,
E. Grave, and G. Lample, “Llama: Open and efﬁcient foundation language
models,” arXiv preprint arXiv:2302.13971, 2023.
[13] A. Zeng, X. Liu, Z. Du, Z. Wang, H. Lai, M. Ding, Z. Yang, Y. Xu,
W. Zheng, X. Xia, W. L. Tam, Z. Ma, Y. Xue, J. Zhai, W. Chen, Z. Liu,
P. Zhang, Y. Dong, and J. Tang, “GLM-130b: An open bilingual pre-
trained model,” in The Eleventh International Conference on Learning
Representations (ICLR), 2023.
[14] Z. Du, Y. Qian, X. Liu, M. Ding, J. Qiu, Z. Yang, and J. Tang, “Glm:
General language model pretraining with autoregressive blank inﬁlling,”
in Proceedings of the 60th Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers), 2022, pp. 320–
335.
[15] W.-L. Chiang, Z. Li, Z. Lin, Y. Sheng, Z. Wu, H. Zhang, L. Zheng,
S. Zhuang, Y. Zhuang, J. E. Gonzalez, I. Stoica, and E. P. Xing,
“Vicuna: An open-source chatbot impressing gpt-4 with 90%* chatgpt
quality,” March 2023. [Online]. Available: https://vicuna.lmsys.org
[16] OpenAI, “Gpt-4 technical report,” arXiv, 2023.
[17] Authors,
“Ethicssuite,”
April
2023.
[Online].
Available:
https:
//github.com/LLM-Ethics/EthicsSuite
[18] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez,
Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” Advances in
neural information processing systems, vol. 30, 2017.
[19] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “Bert: Pre-training
of deep bidirectional transformers for language understanding,” arXiv
preprint arXiv:1810.04805, 2018.
[20] W. X. Zhao, K. Zhou, J. Li, T. Tang, X. Wang, Y. Hou, Y. Min, B. Zhang,
J. Zhang, Z. Dong et al., “A survey of large language models,” arXiv
preprint arXiv:2303.18223, 2023.
[21] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal,
A. Neelakantan, P. Shyam, G. Sastry, A. Askell et al., “Language models
are few-shot learners,” Advances in neural information processing systems,
vol. 33, pp. 1877–1901, 2020.
[22] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin,
C. Zhang, S. Agarwal, K. Slama, A. Ray et al., “Training language
models to follow instructions with human feedback,” Advances in Neural
Information Processing Systems, vol. 35, pp. 27 730–27 744, 2022.
[23] H. Kim, Y. Yu, L. Jiang, X. Lu, D. Khashabi, G. Kim, Y. Choi, and
M. Sap, “Prosocialdialog: A prosocial backbone for conversational agents,”
arXiv preprint arXiv:2205.12688, 2022.
[24] S. Gehman, S. Gururangan, M. Sap, Y. Choi, and N. A. Smith,
“Realtoxicityprompts: Evaluating neural toxic degeneration in language
models,” in Findings of the Association for Computational Linguistics:
EMNLP 2020, 2020, pp. 3356–3369.
[25] C. Ziems, J. Yu, Y.-C. Wang, A. Halevy, and D. Yang, “The moral integrity
corpus: A benchmark for ethical dialogue systems,” in Proceedings of the
60th Annual Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers), 2022, pp. 3755–3773.
[26] D. Hendrycks, C. Burns, S. Basart, A. C. Critch, J. L. Li, D. Song, and
J. Steinhardt, “Aligning ai with shared human values,” in International
Conference on Learning Representations, 2021.
[27] Y. Tay, D. Ong, J. Fu, A. Chan, N. Chen, A. T. Luu, and C. Pal,
“Would you rather? a new benchmark for learning machine alignment
with cultural values and social preferences,” in Proceedings of the 58th
Annual Meeting of the Association for Computational Linguistics, 2020,
pp. 5369–5373.
[28] J. Zhou, J. Deng, F. Mi, Y. Li, Y. Wang, M. Huang, X. Jiang, Q. Liu, and
H. Meng, “Towards identifying social bias in dialog systems: Framework,
dataset, and benchmark,” in Findings of the Association for Computational
Linguistics: EMNLP 2022, 2022, pp. 3576–3591.
[29] L. Jiang, J. D. Hwang, C. Bhagavatula, R. L. Bras, M. Forbes,
J. Borchardt, J. Liang, O. Etzioni, M. Sap, and Y. Choi, “Delphi: Towards
machine ethics and norms,” arXiv preprint arXiv:2110.07574, 2021.
[30] P. Ma, S. Wang, and J. Liu, “Metamorphic testing and certiﬁed mitigation
of fairness violations in nlp models.” in IJCAI, 2020, pp. 458–465.
[31] M. H. Asyroﬁ, Z. Yang, I. N. B. Yusuf, H. J. Kang, F. Thung, and D. Lo,
“Biasﬁnder: Metamorphic test generation to uncover bias for sentiment
analysis systems,” IEEE Transactions on Software Engineering, vol. 48,
no. 12, pp. 5087–5101, 2021.
[32] E. Soremekun, S. Udeshi, and S. Chattopadhyay, “Astraea: Grammar-
based fairness testing,” IEEE Transactions on Software Engineering,
vol. 48, no. 12, pp. 5188–5211, 2022.
[33] Z. Chen, J. M. Zhang, M. Hort, F. Sarro, and M. Harman, “Fairness
testing: A comprehensive survey and analysis of trends,” arXiv preprint
arXiv:2207.10223, 2022.
[34] S. Chen, S. Jin, and X. Xie, “Testing your question answering software
via asking recursively,” in 2021 36th IEEE/ACM International Conference
on Automated Software Engineering (ASE).
IEEE, 2021, pp. 104–116.
[35] Q. Shen, J. Chen, J. M. Zhang, H. Wang, S. Liu, and M. Tian, “Natural
test generation for precise testing of question answering software,” in 37th
IEEE/ACM International Conference on Automated Software Engineering,
2022, pp. 1–12.
[36] Z. Liu, Y. Feng, Y. Yin, J. Sun, Z. Chen, and B. Xu, “Qatest: A uniform
fuzzing framework for question answering systems,” in 37th IEEE/ACM
International Conference on Automated Software Engineering, 2022, pp.
1–12.
[37] A. Dwarakanath, M. Ahuja, S. Sikand, R. M. Rao, R. J. C. Bose,
N. Dubash, and S. Podder, “Identifying implementation bugs in ma-
chine learning based image classiﬁers using metamorphic testing,” in
Proceedings of the 27th ACM SIGSOFT International Symposium on
Software Testing and Analysis, 2018, pp. 118–128.
[38] S. Wang and Z. Su, “Metamorphic object insertion for testing object
detection systems,” in Proceedings of the 35th IEEE/ACM International
Conference on Automated Software Engineering, 2020, pp. 1053–1065.
[39] L. Xu, D. Towey, A. P. French, S. Benford, Z. Q. Zhou, and T. Y. Chen,
“Using metamorphic relations to verify and enhance artcode classiﬁcation,”
Journal of Systems and Software, vol. 182, p. 111060, 2021.
[40] P. Ji, Y. Feng, J. Liu, Z. Zhao, and Z. Chen, “Asrtest: automated testing for
deep-neural-network-driven speech recognition systems,” in Proceedings
of the 31st ACM SIGSOFT International Symposium on Software Testing
and Analysis, 2022, pp. 189–201.
[41] B. Yu, Z. Zhong, X. Qin, J. Yao, Y. Wang, and P. He, “Automated testing
of image captioning systems,” in Proceedings of the 31st ACM SIGSOFT
11

--- Page 12 ---\n\nInternational Symposium on Software Testing and Analysis, 2022, pp.
467–479.
[42] P. Ma and S. Wang, “Mt-teql: evaluating and augmenting neural nlidb on
real-world linguistic and schema variations,” Proceedings of the VLDB
Endowment, vol. 15, no. 3, pp. 569–582, 2021.
[43] W. Wang, J.-t. Huang, W. Wu, J. Zhang, Y. Huang, S. Li, P. He, and
M. Lyu, “Mttm: Metamorphic testing for textual content moderation
software,” arXiv preprint arXiv:2302.05706, 2023.
[44] L. S. Khoo, J. Q. Bay, M. L. K. Yap, M. K. Lim, C. Y. Chong, Z. Yang,
and D. Lo, “Exploring and repairing gender fairness violations in word
embedding-based sentiment analysis model through adversarial patches,”
in 2023 IEEE International Conference on Software Analysis, Evolution
and Reengineering (SANER). IEEE Computer Society, 2023.
[45] Z. Yang, H. Jain, J. Shi, M. H. Asyroﬁ, and D. Lo, “Biasheal: On-the-
ﬂy black-box healing of bias in sentiment analysis systems,” in 2021
IEEE International Conference on Software Maintenance and Evolution
(ICSME).
IEEE, 2021, pp. 644–648.
[46] X. He, Z. Lin, Y. Gong, A. Jin, H. Zhang, C. Lin, J. Jiao, S. M. Yiu,
N. Duan, W. Chen et al., “Annollm: Making large language models to
be better crowdsourced annotators,” arXiv preprint arXiv:2303.16854,
2023.
[47] K. Papineni, S. Roukos, T. Ward, and W.-J. Zhu, “Bleu: a method for
automatic evaluation of machine translation,” in Proceedings of the 40th
annual meeting of the Association for Computational Linguistics, 2002,
pp. 311–318.
[48] T. Y. Chen, F.-C. Kuo, H. Liu, P.-L. Poon, D. Towey, T. Tse, and Z. Q.
Zhou, “Metamorphic testing: A review of challenges and opportunities,”
ACM Computing Surveys (CSUR), vol. 51, no. 1, pp. 1–27, 2018.
[49] W. M. McKeeman, “Differential testing for software,” Digital Technical
Journal, vol. 10, no. 1, pp. 100–107, 1998.
[50] Z. Ji, N. Lee, R. Frieske, T. Yu, D. Su, Y. Xu, E. Ishii, Y. J. Bang,
A. Madotto, and P. Fung, “Survey of hallucination in natural language
generation,” ACM Computing Surveys, vol. 55, no. 12, pp. 1–38, 2023.
[51] N. Shinn, B. Labash, and A. Gopinath, “Reﬂexion: an autonomous
agent with dynamic memory and self-reﬂection,” arXiv preprint
arXiv:2303.11366, 2023.
[52] A. Madaan, N. Tandon, P. Gupta, S. Hallinan, L. Gao, S. Wiegreffe,
U. Alon, N. Dziri, S. Prabhumoye, Y. Yang et al., “Self-reﬁne: Iterative
reﬁnement with self-feedback,” arXiv preprint arXiv:2303.17651, 2023.
[53] S. Diao, R. Pan, H. Dong, K. Shum, J. Zhang, W. Xiong, and T. Zhang,
“Lmﬂow: An extensible toolkit for ﬁnetuning and inference of large
foundation models,” https://optimalscale.github.io/LMFlow/, 2023.
[54] OpenAI. (2023) Openai api platform. [Online]. Available: https:
//platform.openai.com/overview
[55] Azure. (2023) Azure openai service. [Online]. Available: https:
//azure.microsoft.com/en-us/products/cognitive-services/openai-service
[56] S. Zhang, S. Roller, N. Goyal, M. Artetxe, M. Chen, S. Chen, C. Dewan,
M. Diab, X. Li, X. V. Lin, T. Mihaylov, M. Ott, S. Shleifer, K. Shuster,
D. Simig, P. S. Koura, A. Sridhar, T. Wang, and L. Zettlemoyer, “Opt:
Open pre-trained transformer language models,” 2022.
[57] T. L. Scao, A. Fan, C. Akiki, E. Pavlick, S. Ili´c, D. Hesslow, R. Castagn´e,
A. S. Luccioni, F. Yvon, M. Gall´e et al., “Bloom: A 176b-parameter open-
access multilingual language model,” arXiv preprint arXiv:2211.05100,
2022.
[58] R. Taori, I. Gulrajani, T. Zhang, Y. Dubois, X. Li, C. Guestrin, P. Liang,
and T. B. Hashimoto, “Stanford alpaca: An instruction-following llama
model,” https://github.com/tatsu-lab/stanford alpaca, 2023.
[59] Azure.
(2023)
Azure
content
moderator.
[Online].
Available:
https://learn.microsoft.com/en-us/azure/cognitive-services/
content-moderator/overview
[60] OpenAI. (2023) Moderation. [Online]. Available: https://platform.openai.
com/docs/guides/moderation/overview
[61] B. Peng, C. Li, P. He, M. Galley, and J. Gao, “Instruction tuning with
gpt-4,” arXiv preprint arXiv:2304.03277, 2023.
[62] Z. Chen, F. Jiang, J. Chen, T. Wang, F. Yu, G. Chen, H. Zhang, J. Liang,
C. Zhang, Z. Zhang et al., “Phoenix: Democratizing chatgpt across
languages,” arXiv preprint arXiv:2304.10453, 2023.
[63] E. J. Hu, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, W. Chen et al.,
“Lora: Low-rank adaptation of large language models,” in International
Conference on Learning Representations.
[64] X. L. Li and P. Liang, “Preﬁx-tuning: Optimizing continuous prompts for
generation,” in Proceedings of the 59th Annual Meeting of the Association
for Computational Linguistics and the 11th International Joint Conference
on Natural Language Processing (Volume 1: Long Papers), 2021, pp.
4582–4597.
12
\n```\n