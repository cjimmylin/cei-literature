---
title: "Can LLMs Grasp Implicit Cultural Values - PDF Extract"
source_pdf: "2025-Liu-Can LLMs Grasp Implicit Cultural Values.pdf"
pages: 25
extracted_at: "2026-01-24T16:38:30.605057"
---

# PDF Extract: Can LLMs Grasp Implicit Cultural Values

**Source PDF:** 2025-Liu-Can LLMs Grasp Implicit Cultural Values.pdf
**Total Pages:** 25

---

## Content

```
--- Page 1 ---

Can LLMs Grasp Implicit Cultural Values? Benchmarking LLMs’
Cultural Intelligence with CQ-Bench
Ziyi Liu1
Priyanka Dey1
Jen-tse Huang3
Zhenyu Zhao1
Bowen Jiang4
Rahul Gupta2
Yang Liu2
Yao Du1
Jieyu Zhao1
1University of Southern California
2Amazon AGI
3John Hopkins University
4University of Pennsylvania
{zliu2803, deyp, zzhao767, jieyuz}@usc.edu
{gupra, yangliud}@amazon.com jhuan236@jh.edu bwjiang@seas.upenn.edu
Abstract
Cultural Intelligence (CQ) refers to the ability
to understand unfamiliar cultural contexts—a
crucial skill for large language models (LLMs)
to effectively engage with globally diverse
users. Existing studies often focus on explicitly
stated cultural norms, but fail to capture the
subtle, implicit values that are common in daily
conversation. To address this gap, we introduce
CQ-Bench, a benchmark specifically designed
to assess LLMs’ capability to infer implicit cul-
tural values from natural conversational con-
texts. CQ-Bench consists of multi-character
conversation-based stories using values from
the World Value Survey and the GlobalOpin-
ions, with topics including ethical, religious,
social, etc. Our automatic dataset construction
pipeline integrates rigorous validation proce-
dures (incorporation, consistency, and implicit-
ness checks), achieving a 94.5% human–model
agreement in the final validation. To leverage
CQ-Bench data, we design three tasks of in-
creasing complexity: attitude detection, value
selection, and value extraction. These tasks
evaluate whether models can detect attitude and
recognize values embedded within natural dia-
logues rather than relying on explicit cultural
knowledge. We find that while frontier mod-
els like o1 reach human-level performance in
value selection (0.809 F1), they still fall short
in nuanced attitude detection (0.622 F1). No-
tably, fine-tuning a smaller LLaMA-3.2-3B on
only 500 culturally-rich examples improves per-
formance by over 10%, even outperforming
o3-mini in some cases. Using CQ-Bench, we
provide insights into the current challenges in
LLMs’ CQ research and suggest practical path-
ways for enhancing LLMs’ cross-cultural rea-
soning abilities. 1
1
Introduction
Large language models (LLMs) have demonstrated
impressive capabilities in understanding and gener-
1The code is available at:
https://github.com/uscnlp-
lime/CQ-Bench
ating culturally relevant text (Li et al., 2024a,c,b;
Putri et al., 2024). Prior research on LLM cul-
tural alignment primarily focuses on modeling
differences between national cultures (Pujari and
Goldwasser, 2024; Kharchenko et al., 2024; Shi
et al., 2024; Wang et al., 2024) or aligning models
with culturally specific norms (Zhong et al., 2024;
Rozen et al., 2024; Johnson et al., 2022; Kim et al.,
2024; Monazzah et al., 2025).
However, cultural values in real-world interac-
tions are not solely determined by demographic
characteristics. Individuals within the same cul-
tural group can hold diverse and even conflicting
beliefs (Fischer and Poortinga, 2012), and LLMs
risk oversimplifying human perspectives if they
rely merely on broad demographic generalizations
(Saha et al., 2025a). This limitation becomes partic-
ularly problematic in human-AI interactions, where
successful communication relies not only on an
LLM’s ability to recognize explicit cultural mark-
ers but also on its capacity to infer implicit cultural
values. While LLMs can produce diverse responses
when a persona and values are explicitly provided
(Grassi et al., 2024; Wang et al., 2025; Huang et al.,
2024; Jiang et al., 2025), real-world communica-
tion often lacks such explicit signals. Humans do
not typically express their values in a structured de-
bate format (Chatterji et al., 2025); instead, values
are subtly embedded into casual conversations and
personal anecdotes.
Cultural intelligence (CQ) refers to an outsider’s
ability to interpret unfamiliar and ambiguous cul-
tural cues (Blanchard and Mohammed, 2024; Ear-
ley and Ang, 2003). For LLMs, CQ is crucial for
engaging in meaningful conversations with individ-
uals from diverse backgrounds. Unlike traditional
assessments of value understanding that focus on
detecting explicit statements about cultural norms
(Ren et al., 2024; Kiesel et al., 2023), it emphasizes
deeper contextual reasoning—mirroring real-life
interactions where implicit beliefs are embedded
arXiv:2504.01127v2  [cs.CL]  9 Oct 2025

--- Page 2 ---

Speaking of competition, did any of you vote
in the recent elections? I heard there were
some sketchy things happening.
I did! But honestly, I wasn't surprised. You
know, it seems like every election there
are whispers of voters being
influenced here and there—it almost
feels like an accepted part of the process.
True. It feels like they get overlooked so
often. There should be more female
voices in these elections, yet here we are,
still hearing the same old male perspectives.
And what about women in office? Not that
I’m opposed, but I haven’t seen any real
change there either. 
It is picnic time! Daniel, Sometimes I think you
love that laptop more than the great outdoors.
 It’s not like I have a choice! Work pays the
bills. Besides, if I could make my work
here, I’d do it.
.......
Bryan
Priya
Alice
Daniel
Priya
Daniel
Scene: A conversation during picnic
1. Attitude Detection
2. Value Selection
3. Value Extraction
   Question: In your view, how often do the following things occur in this country’s
elections: Voters are bribed? 
Options: Very often, Not often, Not at all often
Question: Work should always come first, even if it means less spare time
What is Daniel's attitude toward this statement?
Options: Agree, Disagree, Neither Agree of Disagree 
Work should always come first, even if it
means less spare time : agree 
How often do the following things occur in
this country’s elections: Women have equal
opportunities to run for office?: 
Not at all often
The only acceptable religion is my religion.:
Disagree
In your view, how often do the following things
occur in this country’s elections: Voters are
bribed? : Very often
✅
✅
✅
❌
What values are reflected from the conversation?
I believe work is
important than other
things
I think our election
system is lack
 of fairness
I think the election
system should not be
influenced by money
Figure 1: An illustration of CQ-Bench. We construct three distinct tasks based on conversation-style stories to
assess the cultural intelligence of LLMs in CQ-Bench.
in everyday speech and action.
To address these gaps, we introduce CQ-Bench,
a benchmark designed to evaluate LLMs’ ability
to infer implicit cultural values within conversa-
tional contexts (Figure 1). We propose a structured
automatic pipeline for generating multi-turn, multi-
character conversations that naturally embed cul-
tural values. We design additional incorporation,
consistency, and implicitness checks using GPT-
4o as a judge to ensure dataset quality. Human
evaluation shows a 94.5% agreement with the GPT-
4o’s judgment. We then evaluate various LLMs
on three increasingly challenging tasks based on
CQ-Bench: attitude detection, value selection, and
value extraction, to measure their ability to rec-
ognize, interpret, and extract cultural values from
conversations. While larger models generally show
more promising results than smaller models in most
tasks, our detailed analysis reveals notable perfor-
mance variations across different categories of val-
ues. For example, models extract political values
well (above 0.7 F1 score overall) but perform much
worse in religious values (below 0.6), highlighting
substantial room for improving LLMs’ understand-
ing of culture values.
Our contributions are as follows:
• Benchmark Design: We are the first to bench-
mark LLMs’ cultural intelligence via CQ-
Bench, which assesses their ability to infer im-
plicit cultural values in conversation.
• Automatic Dataset Generation Pipeline: We
introduce a pipeline that automatically generates
high-quality synthetic datasets. The strong agree-
ment between our model and human evaluations
demonstrates the robustness of the pipeline and
ensures reproducibility for future research.
• Comprehensive Evaluation:
We construct
three escalating tasks—attitude detection, value
selection, and value extraction—to systemati-
cally evaluate open-sourced and close-sourced
models’ CQ. We further perform both supervised
and reinforcement fine-tuning with GRPO to en-
hance the reasoning and alignment.
2
CQ-Bench
Evaluating a model’s cultural intelligence goes be-
yond simply identifying a broad value in a short
speech (Ren et al., 2024). To reflect real-world
scenarios, we design comprehensive tasks that ex-
amine implicit cultural value understanding from
multiple angles. As shown in Figure 1, CQ-Bench
features three tasks of growing difficulty: attitude
detection, value selection, and value extraction. We
will first introduce the definition of culture value
and conversation setup in CQ-Bench and then ex-
plain the tasks in detail.

--- Page 3 ---

2.1
Culture Value
Cultural values are defined as values inherently
linked to culture and expressed through different
attitudes. Each cultural value consists of two com-
ponents: (1) Statement, which presents or solic-
its an opinion, and (2) Attitude, which signifies
agreement or disagreement with the statement. As
shown in Figure 1, “The only acceptable religion
is my religion” is a statement while “Disagree”
is an attitude. Different statements offer multi-
ple attitude options, aligning with the settings in
the original questionnaires. The statements in this
study are sourced from the World Values Survey
(WVS) (Haerpfer et al., 2022) and the GlobalOp-
inion dataset (Durmus et al., 2023). The WVS is
a global research project that explores individu-
als’ values and beliefs, how their evolution over
time, and their sociopolitical implications. The
GlobalOpinion dataset contains a subset of survey
questions about global issues and public opinions,
adapted from the WVS and the Pew Global Atti-
tudes Survey. We manually select values that either
focus on personal beliefs or characterize societal
and community attributes.
2.2
Conversation Setting
In CQ-Bench, each conversation story features 4–5
characters, with randomly selected cultural values
implicitly embedded in the narrative. We consider
three distinct settings:
• Random Setting: Aligning with previous re-
search (Li et al., 2024a), which utilizes a subset
of 50 values from the WVS, we randomly select
5 statements from this subset and assign each a
random attitude shared by all characters to form
cultural values.
• Category-Specific Setting: We expand the sub-
set to include 23–28 statements per category:
political, religious, social, and ethical. To assess
whether domain-specific focus enhances cultural
value comprehension, we select five statements
from one category at a time and assign a ran-
dom attitude. The detailed statistics of category-
specific values are shown in Appendix A.2.
• Multiple Attitude Setting: In contrast to first
two settings, this setting assigns each character a
distinct attitude toward the selected values, fos-
tering diverse perspectives and enhancing com-
plexity. For example, in the first two settings,
one value could be Work is a duty towards the
society – agree. In the multiple attitude setting,
the values could be Alice: Work is a duty to-
wards the society – agree and Raj: Work is a
duty towards the society – disagree.
2.3
Attitude Detection (AD)
To understand people’s values, the first step is
to examine whether models can recognize prefer-
ences on specific topics. Accordingly, we eval-
uate whether the model can interpret attitudes
expressed in conversation.
Given a story S, a
statement T, and a limited set of attitude options
O = {o1, o2, . . . , on} (e.g., Agree, Disagree, Very
often, Not at all often), the model identifies the
attitude toward T expressed in S from options O.
In the Random and Category-Specific settings, it
determines the overall attitude including all charac-
ters. In the Multiple Attitude setting, characters
may hold different stances, and the model must
identify the attitude of a specified character.
2.4
Value Selection (VS)
Given a story S and a predefined set of 15 candidate
values V = {v1, v2, . . . , v15} (candidate values are
different for each datapoint), the model is required
to select exactly X ground-truth values, denoted as
V∗⊂V, where |V∗| = X. The remaining 15 −X
options are randomly sampled from non-ground
truth values. This task is more challenging than
attitude detection, as the model must first identify
the relevant topics before selecting the correct val-
ues. Formally, the model must learn a function
f(S, V) →V∗, where V∗⊂V and |V∗| = X.
2.5
Value Extraction (VE)
In real-world scenarios, there is no predefined
set of values for models to select from, making
value understanding particularly challenging. To
address this, we design Value Extraction to as-
sess cultural value detection without prior knowl-
edge. Given a story S, the model extracts key
cultural values across given topics (e.g., social, eth-
ical, political) without predefined choices. It re-
ceives examples of expected formats and a topic
set T = {t1, t2, . . . , tn} covering all seed values.
For each topic ti ∈T , the model outputs a value
set Vti = {v1, v2, . . . , vm} if relevant values exist,
or Vti = ∅otherwise.
We ask the model to limit the answer size to
10 total values for easier performance comparison
across models. Evaluation is based on recall, mea-
suring the proportion of ground-truth values cor-
rectly identified.

--- Page 4 ---

3
Automatic Dataset Generation
Our goal is to build a dataset of conversation-based
stories that reflect cultural values. Unlike Li et al.
(2024b), where characters present their ideas se-
quentially in a debate format, conversations in CQ-
Bench are designed to be more natural and casual,
resembling real-life interactions. However, no ex-
isting dataset captures real human conversations in
cultural contexts, and collecting such data is diffi-
cult due to the extensive human labeling required.
Following prior work (Ying et al., 2025; Sui et al.,
2025), we therefore construct a synthetic dataset
using an automatic pipeline that both generates and
validates the data.
3.1
Generation guidelines
Each story is generated based on five specified cul-
tural values and different scenarios for diversity
(Appendix A.2). The generated stories must adhere
to the following guidelines:
• Flexible Value Incorporation: The cultural val-
ues may appear multiple times and do not need
to follow a strict sequence, ensuring a natural
conversational flow.
• Character Value Consistency: All characters
must consistently adhere to their assigned values
without contradiction.
• Implicit Value Representation: The cultural
values should not be explicitly stated or directly
rephrased within the dialogue. The underlying
cultural values should be challenging for humans
to explicitly identify.
• Appropriate Story Length: The story should
be of sufficient length, incorporating multiple
rounds of character interactions.
3.2
Post-Generation Checking
All generated stories undergo a post-check to en-
sure quality, as shown in Figure 2. The check-
list corresponds to the first three guidelines, while
the fourth is verified directly using word count.
Through preliminary experiments, we find that
GPT-4o is better in verification while GPT-4o-mini
can perform as well as GPT-4o in refining.
• Incorporation Check: We use GPT-4o to ver-
ify the inclusion of all assigned values in the
story. If any values are missing, GPT-4o-mini re-
fines the story to ensure their natural integration
into the dialogue. In the Multiple Attitude set-
ting, the model must also assess whether specific
characters embody certain values.
• Consistency Check: In both the Random and
Category-Specific settings, all characters in the
story are expected to adhere to the assigned
value. However, in some cases, certain char-
acters may express opposing views, particularly
when the assigned value contradicts prevailing
social norms. When inconsistencies are detected,
we revise the conflicting speech to align with the
assigned value. Specifically, we provide GPT-4o
with the full story, along with the original speech,
and prompt it to generate only the revised ver-
sion that conforms to the intended value. We do
not use GPT-4o-mini for revision, as we found
it is unable to effectively rewrite inconsistent
speech and tends to follow the original stance.
• Implicitness Check: While the story is re-
quired to be implicit, the model generates ex-
plicit speech, as shown in Figure 2 and Table 6.
To maintain the story’s difficulty, we use GPT-
4o-mini to systematically validate and rewrite
explicit speech into an implicit form. We show
the statistics of speech refinement in Table 5.
To enhance reliability, we perform three rounds
of incorporation and consistency checks as final
validation. Missing and contradictory values are
addressed using a majority vote approach based on
three evaluations. Specifically, missing values are
removed from the ground truth, while contradic-
tory values are documented along with the specific
inconsistencies and the characters exhibiting incon-
sistent speech. Documented contradictory values
are used in generating dataset (Appendix A.2).
Human evaluation
We conduct human valida-
tion to assess each step of the conversation refine-
ment process and the overall conversation quality.
A total of 150 conversations, encompassing 750
values, are evaluated across four dimensions: value
reflection, consistency, implicitness, and natural-
ness. For value reflection and consistency, we com-
pare human annotations with model predictions.
For implicitness, annotators compare each speech
segment before and after refinement and rate the
degree of improvement on a 1–5 scale. For natural-
ness, they rate how natural the refined conversation
sounds, also on a 1–5 scale. Fifty computer science
students participated as volunteers, each labeling
a small subset of the data, with every data point
annotated by two independent annotators. The Co-
hen’s κ score for value reflection is 0.546, indicat-
ing moderate agreement. After removing instances
where the model judged a value as not reflected

--- Page 5 ---

Final Validation
Final story: 
Sam: My cousin always complains about
his ....
Reflection validation:
Value 1: reflected
Value 2: reflected
Value 3: reflected
Consistency validation:
Value 3: Raj disagree with value 3
 Values
1. Work is a duty towards the society. --
agree
2. One of my main goals in life is to
make my parents proud -- agree
3. It is a duty towards society to have
children
-- agree
......
  
  Story
Sam: Everyone should work, otherwise society
cannot advance....
Alice: I don't know if I can agree with you. I don't
think I am that valuable to the society.
......
Raj: My mom recently asked me when I will
have kids, come on, not everyone wants kids! I
can have free will!
Alice: Well, it is not just about you, the birth rate
matters to the society.
 
 Incorporation check
GPT-4o's validation:  "One of my main goals in life is to make my parents proud --
agree" is missing
Add missing values:
....
Alice: I don't know if I can agree with you. I don't think I am that valuable to the society.
Sam: Besides society, it is also about your social status. I don't want to disappoint my
parents. They have devoted so much to me.
Alice: I do agree with this. My parents' opinion matters a lot to me.
......
 Consistency check 
GPT-4o's validation:  Alice does not agree with value 1 and  Raj does not agree with
value 3.
 Rewrite inconsistent speech:
Alice: I don't know if I can agree with you. I don't think I am that valuable to the society.  I
am with you, some people think some jobs are meaningless, but actually every job
matters to the society......(Correctly rewritten)
.....
Raj: My mom recently asked me when I will have kids, come on, not everyone wants kids!
I can have free will! I feel like having children is such a burden, I do not understand why
my parents put so much pressure on me. (Not correctly rewritten)
Implicitness check
GPT-4o's validation: Sam's speech directly
reflects the value 1.
Rewrite the explicit speech:
Sam: Everyone should work, otherwise society
cannot advance....
Sam: My cousin always complains about his
job, and he does not take it seriously. I don't
understand him. I don't enjoy my work either,
but I am very responsible for it.
(Use side evidence to support the value) 
Figure 2: Dataset construction pipeline. We first create value sets, and then generate multi-character conversation
style story. We conduct multiple checks and refinement to improve the quality of the story.
(and the corresponding ground-truth values), the
remaining cases show 94.5% alignment with hu-
man judgment, demonstrating the faithfulness of
the model’s validation. Similarly, the consistency
validation achieves a Cohen’s κ of 0.515 and 92.5%
alignment with human annotations. For implicit-
ness refinement, over 80% of cases are rated as
significantly improved, with an average improve-
ment score of 3.28. For naturalness, the average
rating is 3.63, indicating that most conversations
are perceived as natural.
By introducing this automatic pipeline, future
work can build upon to efficiently generate high-
quality datasets. In particular, the pipeline makes it
possible to incorporate a wide range of cultural val-
ues, enabling scalable extensions and more diverse
applications in value understanding research.
4
Evaluating LLMs with CQ-Bench
4.1
Experimental Settings
Models selection.
We select a diverse range of
models, including both open-source and closed-
source models, with varying sizes. For open-source
models, we include Qwen 2.5 (7B, 14B, and 32B),
Qwen 3 4B (Bai et al., 2023), LLaMA 3.1 8B, and
LLaMA 3.2 3B (Grattafiori et al., 2024), Deepseek-
V3 and Deepseek-R1 (DeepSeek-AI, 2025). Ad-
ditionally, we experiment with DeepSeek-Distill
models (Qwen 2.5 1.5B, Qwen 2.5 7B, LLaMA 3.1
8B), which have been reported to achieve remark-
able performance on math and coding tasks, even
at smaller scales. Our goal is to evaluate if they
can also perform well on culture-related reasoning
tasks. Finally, for closed-source models, we select
GPT-4o-mini, o4-mini, o3, o3-mini, and o1 (Jaech
et al., 2024). We also conduct analyses with four
human participants who complete the same tasks
on 25 stories, which took 5-6 hours in total 2.
Evaluation metrics.
For attitude detection and
value selection, we use the F1 score to compare the
predicted answers with the ground truth values. For
value extraction, which is more open, we employ
LLM-as-a-judge (Zheng et al., 2023) to evaluate the
responses. Let V = {v1, v2, . . . , vn} be the set of
ground truth values, and let ˆV = {ˆv1, ˆv2, . . . , ˆvm}
be the set of predicted values. We use GPT-4o
to access the output. We ask humans to conduct
the same evaluation as GPT-4o on 25 stories. The
agreement score is 0.864, which shows the relia-
bility of LLM-as-a-judge. For each ground truth
value vi, we define the score function as follows:
S(vi, ˆV ) =





1,
if vi is fully presented in ˆV
0.5,
if vi is partially presented in ˆV .
0,
if vi is not mentioned in ˆV
We define “partially presented” as the output that
mentions the same topic but is not detailed enough.
Dataset.
We generate 500 stories for the random
setting, 100 stories for each category-specific set-
ting, and 100 stories for the multiple-attitude set-
ting, resulting in a total of 1,000 stories. For story
generation, we use GPT-4o-mini, while GPT-4o is
used for validation. In the multiple-attitude setting,
2Hourly payment for annotators in this work is $16.5.

--- Page 6 ---

Random
Political
Social
Religious
Ethical
Multiple
AD
1665
301
213
425
270
1540
VS
2099
402
285
335
351
-
Table 1: Total datapoints for attitude detection (AD) and
total values for value selection (VS) tasks.
we implement only the attitude detection task. The
value selection/extraction task is not included be-
cause the ground truth values typically exceed ten,
making it challenging for the model to choose ac-
curately. We report the total datapoints of attitude
detection and values covered in the story of value
selection for each task in Table 1.
4.2
Prompt Setup
We implement two prompting strategies: with rea-
soning and without reasoning. In the no-reasoning
setting, models provide answers directly without
explanations. In the reasoning setting, we experi-
ment with both zero-shot and few-shot prompting.
Preliminary results show that few-shot prompting
does not improve performance and, sometimes bi-
ases the model toward the values presented in the
demonstrations. Therefore we restrict our main ex-
periments to zero-shot reasoning across all models.
Summarize-then-analyse long CoT prompting.
In the reasoning setting, we observe that simple
prompts often lead to low scores, sometimes even
lower than the no-reasoning baseline. To address
this, we provide a step-by-step reasoning guideline
to guide the models’ responses. For attitude detec-
tion (AD), we instruct models to first summarize
speech relevant to the given statement and then
analyze the attitude based on the retrieved speech.
For value selection (VS), we employ a multi-step
approach: (1) The model summarizes the topics
mentioned in the story based on the provided op-
tions; (2) Selects values associated with the iden-
tified topics; (3) Reasons about which value best
reflects the story; (4) Finally, outputs the selected
value. For value extraction (VE), we ask the model
to summarize the content for each topic and then
predict relevant values based on the summarization.
4.3
CQ across Different LLMs
We first show the results of attitude detection
and value selection in Table 2. Overall, larger
models outperform smaller models by a lot
and summarize-then-analyse prompting can im-
prove performance generally. Human participants
achieve an average score of 0.689 and 0.765 on AD
and VS respectively.
The model struggles to detect nuanced attitudes
beyond simple binary labels.
Although the AD
task should be easier than value selection, its scores
are even lower. One reason is that models struggle
to distinguish neutral stances, such as neither agree
nor disagree. While they can easily differentiate be-
tween agree and disagree, the presence of a neutral
option can cause confusion. Even when a model
correctly identifies agree, it may be distracted by
the neutral choice and incorrectly select neither
agree nor disagree. Additionally, models find it
challenging to differentiate between varying levels
of severity, such as not often and not at all often.
Although it is also challenging for humans, humans
can do better in identifying nuanced attitudes than
models. We present results after merging options
of varying levels of severity in Table 2.
Smaller models fail in long CoT reasoning in
cultural intelligence task.
Although CoT rea-
soning significantly enhances performance in large
models, smaller models often struggle with long
CoT reasoning. LLaMA models, in particular, per-
form poorly in adhering to CoT reasoning across
both AD and VS tasks. While Qwen 7B follows
CoT reasoning well in AD, its performance de-
clines significantly in VS as the reasoning steps
become longer. A manual inspection reveals that
its final output often consists of random values or
irrelevant phrases that fail to focus on the given op-
tions. The DS-distill models exhibit slightly better
instruction-following capabilities, outperforming
Qwen 7B and LLaMA 8B in VS. While they do
not strictly adhere to the prescribed format, their
reasoning process generally aligns with the ideas
provided in the prompt. However, their CQ reason-
ing ability remains weaker than their mathematical
reasoning skills, resulting in final scores that are
still lower than in the no-reasoning setting.
Stronger models do not necessarily outperform
weaker models in VE.
VE tasks require strong
reasoning and summarization capabilities, and
smaller models often struggle with this task, fre-
quently producing nonsensical outputs. As a re-
sult, we focus our evaluation on 5 models: Qwen
2.5 32B, GPT-4o-mini, o3-mini, o4-mini, and
DeepSeek-V3. We also evaluate a smaller sub-
set of 25 stories using o1, o3 and DeepSeek-R1.
Interestingly, unlike attitude detection and value
selection—where larger models consistently out-
perform smaller ones—we observe that a weaker
model (Qwen 2.5 32B) can outperform stronger

--- Page 7 ---

Qwen
Llama
Deepseek-distill
GPT
Deepseek
4B
7B
14B
32B
8B
3B
Q 1.5B
Q 7B
L 8B
4o-mini
o3-mini
o1
o4-mini
o3
V3
R1
AD
W/O R
0.560
0.529
0.553
0.572
0.527
0.455
-
-
-
0.604
0.622
0.622
0.60
0.689
0.642
0.595
W/ R
0.610
0.620
0.616
0.624
0.506
0.372
0.381
0.484
0.556
0.639
0.661
0.622
0.595
0.622
0.660
0.635
Merged
0.775
0.783
0.778
0.786
0.631
0.480
0.490
0.622
0.705
0.820
0.793
0.811
0.834
0.824
0.837
0.837
Multiple
0.607
0.592
0.621
0.642
0.590
0.462
0.403
0.510
0.584
0.645
0.684
-
0.738
-
0.691
-
VS
W/O R
0.653
0.515
0.585
0.633
0.421
0.272
-
-
-
0.639
0.759
0.810
0.828
0.830
0.780
0.798
W/ R
0.468
0.374
0.607
0.717
0.274
0.1
0.383
0.411
0.418
0.576
0.779
0.809
0.820
0.710
0.819
0.814
VE
-
-
-
0.629
-
-
-
-
-
0.602
0.598
0.610
0.696
0.732
0.704
0.736
Table 2: Results on Attitude Detection (AD) and Value Selection (VS). For deepseek-distill models, the models always output
their thinking process (i.e. reasoning). Therefore, we only report reasoning results for those models “W/ R”. For larger models
like Deepseek-R1, o1, and o3, we report results on the same subset used for human evaluation, due to the high cost of running
them on the full dataset. In the “Merged” setting, we merge similar options and in “Multiple” setting, story characters may hold
different opinions. The “Merged” and the “Multiple” settings are both under reasoning settings.
Figure 3: Category specific results. Overall, models perform worst in the Religious setting, and category-specific
datasets yield higher scores than randomly sampled ones.
ones like o3-mini and o1. One possible explana-
tion is that current CoT reasoning methods are not
well-suited for open-ended generation; models tend
to perform better when given predefined options.
4.4
CQ Across Different Value Categories
We present results on category-specific datasets
in Figure 3, showing the performance of six mod-
els in the no-reasoning setting. Complete results
across all models and settings are provided in the
Appendix B.1. Overall, the results show that mod-
els perform better in understanding political, social,
and ethical values, achieving performance that is
better than or comparable to the random setting.
However, they perform worse in the religious val-
ues domain across both tasks. While models show
stronger performance in attitude detection on the
political dataset, they perform better in value selec-
tion on the ethical dataset. This suggests that it is
easier for models to infer people’s political stances
but more challenging for them to identify the spe-
cific topics being discussed in political contexts. In
contrast, in the ethics domain, models find it easier
to identify the main topics being discussed. For
value extraction, overall, models perform better on
category-specific results except for Deepseek-V3,
as they only need to cover a single topic.
4.5
CQ ability learning for small models.
In Section 4.3, we observe that smaller models
struggle with long CoT reasoning, often failing to
produce complete and coherent reasoning traces.
We find that one-shot prompting does not notably
improve the performance (Appendix B.2).
To
strengthen smaller models’ CQ reasoning ability,
we explore two complementary fine-tuning ap-
proaches: Supervised Fine-Tuning (SFT) and Re-
inforcement Fine-Tuning (RFT). Both aim to im-
prove the model’s ability to reason over cultural
contexts but differ in learning strategy. SFT pro-
vides explicit reasoning supervision and encour-
ages models to follow structured reasoning chains
distilled from a larger model, while RFT promotes
open-ended reasoning by allowing models to ex-
plore reasoning paths guided by reward signals.
For SFT, we distill reasoning traces from o3-

--- Page 8 ---

Attitude Detection
Value Selection
Ethical
Political
Religious
Social
Ethical
Political
Religious
Social
Model
ZS
GRPO
SFT
ZS
GRPO
SFT
ZS
GRPO
SFT
ZS
GRPO
SFT
ZS
GRPO
SFT
ZS
GRPO
SFT
ZS
GRPO
SFT
ZS
GRPO
SFT
Qwen 2.5 7B
0.652
0.696
0.704
0.708
0.731
0.718
0.645
0.515
0.713
0.657
0.662
0.714
0.357
0.754
0.690
0.399
0.639
0.572
0.249
0.515
0.519
0.395
0.662
0.517
Qwen 2.5 14B
0.644
0.696
0.707
0.701
0.731
0.731
0.649
0.704
0.708
0.699
0.668
0.718
0.674
0.800
0.687
0.574
0.707
0.681
0.440
0.527
0.552
0.567
0.702
0.608
Qwen 3 4B
0.548
0.641
0.607
0.724
0.728
0.714
0.545
0.631
0.588
0.633
0.624
0.624
0.498
0.709
0.745
0.555
0.678
0.667
0.281
0.512
0.556
0.468
0.635
0.659
Llama 3.2 3B
0.407
0.630
0.674
0.419
0.646
0.728
0.454
0.645
0.708
0.418
0.606
0.681
0.217
0.648
0.560
0.078
0.625
0.576
0.077
0.466
0.504
0.109
0.573
0.632
Llama 3.1 8B
0.596
0.700
0.704
0.638
0.748
0.721
0.574
0.730
0.678
0.574
0.709
0.695
0.304
0.751
0.645
0.261
0.695
0.576
0.164
0.642
0.504
0.280
0.708
0.632
O3-mini
0.728
-
-
0.727
-
-
0.703
-
-
0.700
-
-
0.837
-
-
0.667
-
-
0.531
-
-
0.693
-
-
Table 3: F1 scores for Attitude Detection and Value Selection across categories, models, and methods. ZS stands for
zero-shot. We compare finetuned models with zero-shot prompting method.
mini using a random-setting dataset of 500 sam-
ples and fine-tune 5 smaller models (Qwen-2.5-
7B, Qwen-2.5-14B, Qwen-3-4B, LLaMA 3.1-8B,
and LLaMA 3.2-3B) with LoRA (Hu et al., 2021)
for five epochs. Evaluation on category-specific
datasets—which contain unseen values and thus
approximate out-of-domain settings—reveals that
SFT substantially improves reasoning quality and
generalization across most domains.
Notably,
LLaMA 3.2-3B even surpasses o3-mini in polit-
ical and religious AD tasks, while Qwen 14B ex-
ceeds it in the same domains for value selection
(VS). We conduct a qualitative analysis to identify
how SFT improves reasoning quality. Manual in-
spection of 50 samples reveals that SFT primarily
mitigates issues of inconsistency between reason-
ing and answers, logical errors, and overlooked
details. Details are provided in Appendix B.2.
For RFT, we adopt the GRPO method (Shao
et al., 2024), which achieves modest gains on the
AD task and sometimes slightly lower than the SFT
results, likely due to its simpler multiple-choice na-
ture. However, it generally yields larger improve-
ments on the more challenging VS task, which re-
quires complex reasoning, as shown in Table 3. Im-
plementation details are provided in Appendix B.2.
Overall, both SFT and RFT significantly outper-
form zero-shot prompting, particularly on tasks
involving long CoT reasoning.
5
Related Work
Culture-aware LLMs.
Culture-aware LLMs ac-
count for cross-cultural differences. Prior work
has examined their cultural personas and con-
sistency (Kharchenko et al., 2024; Rozen et al.,
2024; Yao et al., 2024; Johnson et al., 2022;
Saha et al., 2025b), showing that prompting lan-
guage influences expressed values (Zhong et al.,
2024). To improve cultural awareness, researchers
have proposed both single- and multi-culture mod-
els through dataset augmentation and alignment
(Nguyen et al., 2023; Lin and Chen, 2023; Abbasi
et al., 2023; Li et al., 2024a; Wu et al., 2025). New
benchmarks and datasets further support cultural
knowledge acquisition (Myung et al., 2024; Shi
et al., 2024), improving performance on tasks like
hate speech detection (Li et al., 2024a).
Value understanding.
Value understanding is
key to effective human-LLM interaction. Prior
work has focused on detecting general social
norms in short texts, often using classification or
entailment-based methods (Ren et al., 2024; Kiesel
et al., 2023; Zhang et al., 2024; Li et al., 2023).
Wu et al. (2025) introduced an English dataset with
3,060 humancrafted multi-turn scenarios across 60
countries and found model challenges in interpret-
ing nuanced cultural contexts. Others investigated
datasets such as QA pairs and conversations and
story scenarios in Persian (Monazzah et al., 2025),
Japanese & Sundanese (Pranida et al., 2025), and
Korean (Kim et al., 2024), reporting model limita-
tions in comprehending cultural and linguistic in-
sights. Fung et al. (2022) also introduces a method
for extracting social norms from conversations, em-
phasizing norm mining rather than cultural value
identification. In contrast, our work focuses on
understanding cultural values within long, real-life
conversations, contributing to the development of
culture-aware LLMs in human-AI interaction.
6
Conclusion
We introduce CQ-Bench, a benchmark for evaluat-
ing LLMs’ ability to infer implicit cultural values
in conversations. CQ-Bench assesses model’s cul-
tural intelligence through attitude detection, value
selection, and value extraction. Our findings show
that LLMs, including state-of-the-art models, strug-
gle with nuanced cultural understanding. Fine-
tuning on just 500 examples notably boosts smaller
models, suggesting cultural reasoning can be effi-
ciently distilled. CQ-Bench exposes gaps in LLMs’
cultural adaptability and serves as a foundation for
advancing culturally intelligent AI. Future work
can build on this to enhance LLM alignment with
diverse human values.

--- Page 9 ---

Limitations
This study has several limitations. First, although
we construct a multiple-attitude dataset, we only
evaluate models on the attitude detection task. Fu-
ture work should explore how well models can
extract individual characters’ values within con-
versations—an essential capability for multi-agent
interactions. Second, while we rewrite stories to
remove explicit value expressions, the quality of
these rewrites is inconsistent; detecting explicit
speech is significantly easier for models than gen-
erating high-quality implicit alternatives. Third, in
the story generation, models sometimes struggle
to distinguish between nuanced options, making it
difficult for humans to detect the intended attitudes
as well. We also observe variability in cultural in-
telligence (CQ) among humans—while some can
achieve up to 80% accuracy in attitude detection,
others perform closer to 50%. Finally, in our qual-
itative analysis of model reasoning, we attempted
to use GPT-4o to automatically detect reasoning
flaws but found it inadequate for this task. As a
result, we relied on manual inspection for a small
subset of examples. Future research should investi-
gate automated methods for identifying reasoning
errors.
Ethics Statements
All data used in this study were synthetically gener-
ated by large language models and do not contain
any real user conversations or personal informa-
tion. Cultural value statements were sourced from
publicly available, anonymized survey instruments,
including the World Values Survey and GlobalOp-
inion datasets.
References
Mohammad Amin Abbasi, Arash Ghafouri, Mahdi
Firouzmandi, Hassan Naderi, and Behrouz Minaei
Bidgoli. 2023.
Persianllama: Towards building
first persian large language model. arXiv preprint
arXiv:2312.15713.
Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang,
Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei
Huang, Binyuan Hui, Luo Ji, Mei Li, Junyang Lin,
Runji Lin, Dayiheng Liu, Gao Liu, Chengqiang Lu,
Keming Lu, and 29 others. 2023. Qwen technical
report. Preprint, arXiv:2309.16609.
Emmanuel G. Blanchard and Phaedra Mohammed.
2024. On Cultural Intelligence in LLM-Based Chat-
bots: Implications for Artificial Intelligence in Educa-
tion. In Andrew M. Olney, Irene-Angelica Chounta,
Zitao Liu, Olga C. Santos, and Ig Ibert Bittencourt,
editors, Artificial Intelligence in Education, volume
14829, pages 439–453. Springer Nature Switzerland,
Cham. Series Title: Lecture Notes in Computer Sci-
ence.
Aaron Chatterji, Tom Cunningham, David Deming, Zoë
Hitzig, Christopher Ong, Carl Shan, and Kevin Wad-
man. 2025.
How people use chatgpt.
Technical
report, OpenAI, Duke University, and Harvard Uni-
versity.
DeepSeek-AI. 2025. Deepseek-r1: Incentivizing rea-
soning capability in llms via reinforcement learning.
Preprint, arXiv:2501.12948.
Esin Durmus,
Karina Nyugen,
Thomas I. Liao,
Nicholas Schiefer, Amanda Askell, Anton Bakhtin,
Carol Chen, Zac Hatfield-Dodds, Danny Hernan-
dez, Nicholas Joseph, Liane Lovitt, Sam McCan-
dlish, Orowa Sikder, Alex Tamkin, Janel Thamkul,
Jared Kaplan, Jack Clark, and Deep Ganguli. 2023.
Towards measuring the representation of subjec-
tive global opinions in language models. Preprint,
arXiv:2306.16388.
P Christopher Earley and Soon Ang. 2003. Cultural
intelligence: Individual interactions across cultures.
Stanford University Press.
Ronald Fischer and Ype H Poortinga. 2012. Are cultural
values the same as the values of individuals? an
examination of similarities in personal, social and
cultural value structures. International Journal of
Cross Cultural Management, 12(2):157–170.
Yi R Fung, Tuhin Chakraborty, Hao Guo, Owen
Rambow, Smaranda Muresan, and Heng Ji. 2022.
Normsage: Multi-lingual multi-cultural norm discov-
ery from conversations on-the-fly. arXiv preprint
arXiv:2210.08604.
Lucrezia Grassi, Carmine Tommaso Recchiuto, and An-
tonio Sgorbissa. 2024. Enhancing llm-based human-
robot interaction with nuances for diversity aware-
ness. In 2024 33rd IEEE International Conference
on Robot and Human Interactive Communication
(ROMAN), pages 2287–2294. IEEE.
Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri,
Abhinav Pandey, Abhishek Kadian, Ahmad Al-
Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten,
Alex Vaughan, and 1 others. 2024. The llama 3 herd
of models. arXiv preprint arXiv:2407.21783.
Christian Haerpfer,
Ronald Inglehart,
Alejandro
Moreno, Christian Welzel, Kseniya Kizilova, Jaime
Diez-Medrano, Marta Lagos, Pippa Norris, Eduard
Ponarin, and Bi Puranen. 2022. World values sur-
vey wave 7 (2017-2022) cross-national data-set. (No
Title).
Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan
Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and
Weizhu Chen. 2021. Lora: Low-rank adaptation of
large language models. Preprint, arXiv:2106.09685.

--- Page 10 ---

Jen-tse Huang, Wenxuan Wang, Eric John Li, Man Ho
Lam, Shujie Ren, Youliang Yuan, Wenxiang Jiao,
Zhaopeng Tu, and Michael Lyu. 2024. On the hu-
manity of conversational ai: Evaluating the psycho-
logical portrayal of llms. In The Twelfth International
Conference on Learning Representations.
Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richard-
son, Ahmed El-Kishky, Aiden Low, Alec Helyar,
Aleksander Madry, Alex Beutel, Alex Carney, and 1
others. 2024. Openai o1 system card. arXiv preprint
arXiv:2412.16720.
Bowen Jiang, Zhuoqun Hao, Young-Min Cho, Bryan
Li, Yuan Yuan, Sihao Chen, Lyle Ungar, Camillo J
Taylor, and Dan Roth. 2025. Know me, respond to
me: Benchmarking llms for dynamic user profiling
and personalized responses at scale. arXiv preprint
arXiv:2504.14225.
Rebecca L. Johnson, Giada Pistilli, Natalia Menédez-
González, Leslye Denisse Dias Duran, Enrico Panai,
Julija Kalpokiene, and Donald Jay Bertulfo. 2022.
The Ghost in the Machine has an American ac-
cent:
value conflict in GPT-3.
arXiv preprint.
ArXiv:2203.07785 [cs].
Julia Kharchenko, Tanya Roosta, Aman Chadha, and
Chirag Shah. 2024. How Well Do LLMs Represent
Values Across Cultures? Empirical Analysis of LLM
Responses Based on Hofstede Cultural Dimensions.
arXiv preprint. ArXiv:2406.14805 [cs].
Johannes Kiesel, Milad Alshomary, Nailia Mirzakhme-
dova, Maximilian Heinrich, Nicolas Handke, Hen-
ning Wachsmuth, and Benno Stein. 2023. Semeval-
2023 task 4: Valueeval: Identification of human
values behind arguments.
In Proceedings of the
17th International Workshop on Semantic Evaluation
(SemEval-2023), pages 2287–2303.
Eunsu Kim, Juyoung Suk, Philhoon Oh, Haneul Yoo,
James Thorne, and Alice Oh. 2024. CLIcK: A bench-
mark dataset of cultural and linguistic intelligence
in Korean.
In Proceedings of the 2024 Joint In-
ternational Conference on Computational Linguis-
tics, Language Resources and Evaluation (LREC-
COLING 2024), pages 3335–3346, Torino, Italia.
ELRA and ICCL.
Aochong Li, Mallika Subramanian, Arkadiy Saakyan,
Sky CH-Wang, and S. Muresan. 2023.
Norm-
dial: A comparable bilingual synthetic dialog dataset
for modeling social norm adherence and violation.
ArXiv, abs/2310.14563.
Cheng Li, Mengzhou Chen, Jindong Wang, Sunayana
Sitaram, and Xing Xie. 2024a. CultureLLM: Incor-
porating Cultural Differences into Large Language
Models. arXiv preprint. ArXiv:2402.10946 [cs].
Cheng Li, Damien Teney, Linyi Yang, Qingsong Wen,
Xing Xie, and Jindong Wang. 2024b. CulturePark:
Boosting Cross-cultural Understanding in Large Lan-
guage Models. arXiv preprint. ArXiv:2405.15145
[cs].
Huihan Li, Liwei Jiang, Jena D. Hwang, Hyunwoo Kim,
Sebastin Santy, Taylor Sorensen, Bill Yuchen Lin,
Nouha Dziri, Xiang Ren, and Yejin Choi. 2024c.
CULTURE-GEN: Revealing Global Cultural Percep-
tion in Language Models through Natural Language
Prompting. arXiv preprint. ArXiv:2404.10199 [cs].
Jiwei Li, Michel Galley, Chris Brockett, Jianfeng
Gao, and Bill Dolan. 2016. A diversity-promoting
objective function for neural conversation models.
Preprint, arXiv:1510.03055.
Yen-Ting Lin and Yun-Nung Chen. 2023.
Taiwan
llm:
Bridging the linguistic divide with a cul-
turally aligned language model.
arXiv preprint
arXiv:2311.17487.
Erfan Moosavi Monazzah, Vahid Rahimzadeh, Yadol-
lah Yaghoobzadeh, Azadeh Shakery, and Moham-
mad Taher Pilehvar. 2025. Percul: A story-driven
cultural evaluation of llms in persian. arXiv preprint
arXiv:2502.07459.
Junho Myung, Nayeon Lee, Yi Zhou, Jiho Jin, Rifki Pu-
tri, Dimosthenis Antypas, Hsuvas Borkakoty, Eunsu
Kim, Carla Perez-Almendros, Abinew Ali Ayele, and
1 others. 2024. Blend: A benchmark for llms on ev-
eryday knowledge in diverse cultures and languages.
Advances in Neural Information Processing Systems,
37:78104–78146.
Xuan-Phi Nguyen, Wenxuan Zhang, Xin Li, Mahani
Aljunied, Zhiqiang Hu, Chenhui Shen, Yew Ken
Chia, Xingxuan Li, Jianyu Wang, Qingyu Tan, and
1 others. 2023. Seallms–large language models for
southeast asia. arXiv preprint arXiv:2312.00738.
Salsabila Zahirah Pranida, Rifo Ahmad Genadi, and
Fajri Koto. 2025.
Synthetic data generation for
culturally nuanced commonsense reasoning in low-
resource languages. ArXiv, abs/2502.12932.
Rajkumar Pujari and Dan Goldwasser. 2024. LLM-
Human Pipeline for Cultural Context Grounding of
Conversations. arXiv preprint. ArXiv:2410.13727
[cs].
Rifki Afina Putri, Faiz Ghifari Haznitrama, Dea Ad-
hista, and Alice Oh. 2024.
Can LLM Generate
Culturally Relevant Commonsense QA Data? Case
Study in Indonesian and Sundanese. arXiv preprint.
ArXiv:2402.17302 [cs].
Yuanyi Ren, Haoran Ye, Hanjun Fang, Xin Zhang, and
Guojie Song. 2024. ValueBench: Towards Compre-
hensively Evaluating Value Orientations and Under-
standing of Large Language Models. arXiv preprint.
ArXiv:2406.04214 [cs].
Naama Rozen, Liat Bezalel, Gal Elidan, Amir Glober-
son, and Ella Daniel. 2024. Do LLMs have Con-
sistent Values? arXiv preprint. ArXiv:2407.12878
[cs].

--- Page 11 ---

Sougata Saha, Saurabh Kumar Pandey, and Mono-
jit Choudhury. 2025a. Meta-cultural competence:
Climbing the right hill of cultural awareness. In Pro-
ceedings of the 2025 Conference of the Nations of
the Americas Chapter of the Association for Com-
putational Linguistics: Human Language Technolo-
gies (Volume 1: Long Papers), pages 8025–8042,
Albuquerque, New Mexico. Association for Compu-
tational Linguistics.
Sougata Saha, Saurabh Kumar Pandey, Harshit Gupta,
and Monojit Choudhury. 2025b. Reading between
the lines: Can llms identify cross-cultural communi-
cation gaps? Preprint, arXiv:2502.09636.
Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu,
Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan
Zhang, Y. K. Li, Y. Wu, and Daya Guo. 2024.
Deepseekmath: Pushing the limits of mathemati-
cal reasoning in open language models. Preprint,
arXiv:2402.03300.
Weiyan Shi, Ryan Li, Yutong Zhang, Caleb Ziems,
Chunhua yu, Raya Horesh, Rogério Abreu de Paula,
and Diyi Yang. 2024.
CultureBank: An Online
Community-Driven Knowledge Base Towards Cultur-
ally Aware Language Technologies. arXiv preprint.
ArXiv:2404.15238 [cs].
Peiqi Sui, Juan Diego Rodriguez, Philippe Laban, Dean
Murphy, Joseph P. Dexter, Richard Jean So, Samuel
Baker, and Pramit Chaudhuri. 2025. Kristeva: Close
reading as a novel task for benchmarking interpretive
reasoning. Preprint, arXiv:2505.09825.
Nandan Thakur, Nils Reimers, Johannes Daxenberger,
and Iryna Gurevych. 2021. Augmented SBERT: Data
augmentation method for improving bi-encoders for
pairwise sentence scoring tasks. In Proceedings of
the 2021 Conference of the North American Chapter
of the Association for Computational Linguistics: Hu-
man Language Technologies, pages 296–310, Online.
Association for Computational Linguistics.
Wenxuan Wang, Wenxiang Jiao, Jingyuan Huang, Ruyi
Dai, Jen-tse Huang, Zhaopeng Tu, and Michael Lyu.
2024. Not all countries celebrate thanksgiving: On
the cultural dominance in large language models. In
Proceedings of the 62nd Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 6349–6384.
Xintao Wang, Heng Wang, Yifei Zhang, Xinfeng Yuan,
Rui Xu, Jen-tse Huang, Siyu Yuan, Haoran Guo,
Jiangjie Chen, Shuchang Zhou, and 1 others. 2025.
Coser: Coordinating llm-based persona simulation
of established roles. In Forty-second International
Conference on Machine Learning.
Jincenzi Wu, Jianxun Lian, Dingdong Wang, and Helen
Meng. 2025. Socialcc: Interactive evaluation for cul-
tural competence in language agents. In Proceedings
of the 63rd Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 33242–33271.
Jing Yao, Xiaoyuan Yi, and Xing Xie. 2024. CLAVE:
An Adaptive Framework for Evaluating Values
of LLM Generated Responses.
arXiv preprint.
ArXiv:2407.10725 [cs].
Jie Ying, Zihong Chen, Zhefan Wang, Wanli Jiang,
Chenyang Wang, Zhonghang Yuan, Haoyang Su,
Huanjun Kong, Fan Yang, and Nanqing Dong. 2025.
Seedbench: A multi-task benchmark for evaluating
large language models in seed science. Preprint,
arXiv:2505.13220.
Zhaowei Zhang, Fengshuo Bai, Jun Gao, and Yaodong
Yang. 2024. ValueDCG: Measuring Comprehensive
Human Value Understanding Ability of Language
Models. arXiv preprint. ArXiv:2310.00378 [cs].
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan
Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin,
Zhuohan Li, Dacheng Li, Eric Xing, and 1 others.
2023. Judging llm-as-a-judge with mt-bench and
chatbot arena. Advances in Neural Information Pro-
cessing Systems, 36:46595–46623.
Yaowei Zheng, Richong Zhang, Junhao Zhang, Yanhan
Ye, Zheyan Luo, Zhangchi Feng, and Yongqiang Ma.
2024. Llamafactory: Unified efficient fine-tuning
of 100+ language models. In Proceedings of the
62nd Annual Meeting of the Association for Compu-
tational Linguistics (Volume 3: System Demonstra-
tions), Bangkok, Thailand. Association for Computa-
tional Linguistics.
Qishuai Zhong, Yike Yun, and Aixin Sun. 2024. Cul-
tural Value Differences of LLMs: Prompt, Language,
and Model Size. arXiv preprint. ArXiv:2407.16891
[cs].

--- Page 12 ---

A
Dataset
A.1
Value Set
We adopt seed values from the World value sur-
vey(WVS) and Global Opinion. WVS is a global
research project that explores people’s values and
beliefs and how they change over time. The values
cover different topics from personal beliefs to po-
litical stance. The results include over 200 values
and 100 countries. Each value has different option
candidates and we provide possible option sets in
Table 4.
A.2
Story Generation
For the random dataset, we start with 50 statements
covering seven topics: social, migration, security,
science and technology, religious, ethical, and po-
litical, following the categorization defined by Li
et al. (2024a). To expand the dataset, we focus
on four categories—social, religious, ethical, and
political—because the WVS and GlobalOpinion
datasets contain more values in these areas. To
generate coherent stories, we require at least 20
statements per category. We manually select values
from WVS and GlobalOpinion, excluding those
that do not fit our setting (e.g., “How many times
do you go to church every week—everyday”). As a
result, we collect 27 seed statements for social val-
ues, 23 for religious values, 24 for political values,
and 28 for ethical values.
For the multiple attitude dataset, we use the same
50 statements as in the random setting. Each story
involves four characters, and we assign one value
to each character. Compared to the random dataset,
which contains 5 values per story, the multiple at-
titude dataset includes 5 × 4 values. Due to the
increased value space, we only conduct attitude
detection on the multiple attitude dataset, as value
selection becomes challenging when the ground-
truth set is already large.
For each story, we will randomly predefined a
scenario from those locations: company, school,
neighborhood, national park, restaurant, amuse-
ment park, and airplane. We remove very short
stories (less than 400 words). The length of stories
ranges from 500 to 900 words.
A.3
Story Validation
We conduct three validations: incorporation check,
consistency check and implicitness check.
We
show the human annotation guidelines in Figure 4,
5, 6 and 7.
For the implicitness check, we compare the word
count before and after rewriting to assess changes
in length.
We use Distinct-N (Li et al., 2016)
to measure sentence diversity, which captures the
number of distinct n-grams within a sentence. Fi-
nally, we compute semantic similarity using a Sen-
tence Transformer (Thakur et al., 2021) between
the value and both the original and rewritten speech.
Ideally, the similarity score between the value and
the rewritten speech should be lower, as the model
is instructed not to mention the value explicitly.
All statistics are reported in Table 5. The results
show that refined speech is longer, more diverse,
and semantically further from the value.
We generate 500 stories for random setting and
100 stories for each of the rest settings. We show
how many datapoints for attitude detection and
how many ground truth values in total for value
selection in Table 1.
B
Results
B.1
Category-Specific Results
The no reasoning results are shown in Figure 3. The
zero-shot and one-shot reasoning of smaller mod-
els are shown in Figure 8. We show the rest of the
results in Table 7. The social category dataset in-
cludes a single set of options: agree, disagree, and
neither agree nor disagree. To study how well mod-
els understand the middle stance, we first remove
questions where the ground truth is neither agree
nor disagree, which eliminates about one-third of
the data. We also remove the neither agree nor
disagree option from the remaining examples, re-
sulting in a fully binary dataset. On this binary ver-
sion, o3-mini achieves an accuracy of 0.911. When
we reintroduce the neither agree nor disagree op-
tion, performance drops to 0.811. However, when
evaluated on the full dataset—including questions
with neither as the correct answer—o3-mini only
achieves 0.700 accuracy. This suggests that the
inclusion of a middle stance can significantly chal-
lenge the model’s judgment.
B.2
Distillation on Smaller Models
We use reasoning results generated by o3-mini to
fine-tune smaller models. We use the LLamafac-
tory framework (Zheng et al., 2024) and LoRA to
accelerate the fine-tuning (Hu et al., 2021). We
train 5 epochs with a GPU of A6000 for 2-3 hours.
The rank of LoRA is 8, and the learning rate is
0.0001. We try multiple combinations of hyperpa-

--- Page 13 ---

Figure 4: Screenshot of human annotation guideline (1)

--- Page 14 ---

Figure 5: Screenshot of human annotation guideline (2)

--- Page 15 ---

Figure 6: Screenshot of human annotation guideline (3)

--- Page 16 ---

Figure 7: Screenshot of human annotation guideline (4)

--- Page 17 ---

Example Value
Options
Do you think that your country’s government should
or should not have the right to do the following:
Keep people under video surveillance in public areas?
Definitely should not have the right
Probably should not have the right
Probably should have the right
Definitely should have the right
In your view, how often do the following things occur
in this country’s elections: Journalists provide fair
coverage of elections?
Very often
Not often
Not at all often
Work is a duty towards society.
Agree
Neither agree nor disagree
Disagree
Apart from weddings and funerals, about how often
do you pray?
Frequently
Occasionally
Never
Having a strong leader who does not have to bother
with parliament and elections.
Very good
Very bad
How important is it for people to help others?
Important
Not important
Table 4: Example values and their options. “Definitely should not have the right” and “Probably should not have the
right” are similar options with different levels of severity.
rameters before we choose the final hyperparameter
set. All the experiments are single runs.
We find out the reasoning without fine-tuning
has several issues. The first is inconsistency, for
example, the reasoning mentioned the usage of al-
cohol multiple times, but the final answer fail to
include values related to alcohol. Another reason-
ing does not mention divorce at all, but the final
answer choose some values related to divorce. The
second is logical errors, for example: “Oliver’s
preference for a traditional family setup for rais-
ing kids matches When jobs are scarce, employers
should give priority to people of this country over
immigrants.–Neither agree nor disagree.” There is
no direct logic between two statements. The third is
overlooking details. For example, the one-shot rea-
soning is “The discussion also involves ethical con-
siderations regarding the use of animals and the en-
vironment, which is reflected in the option: Hunting
animals as a sport should be banned. –Disagree.”
The reasoning itself sounds reasonable, however,
the gold label is “Using animals for entertainment
like in zoos/circuses is ethical.–Disagree.” The
SFT reasoning is “Finally, Harold’s statement on
using animals for entertainment, which he finds
shocking, aligns with the value that such practices
are unethical. The difference between the two rea-
soningg is that the latter one identified details of
using animals for entertainment, while the for-
mer one only identified the use of animals and the
environment.
B.3
GRPO Fine-Tuning
We apply GRPO to fine-tune smaller LLMs on both
attitude detection and value selection tasks. For
the attitude detection task, which is formulated as
multiple-choice classification, the reward signal is
binary—1 for correct predictions and 0 otherwise.
In contrast, the value selection task is a multi-label
setting, where predictions can be partially correct.
To account for this, we define the reward as the ratio
of true positives to the total number of predicted
values. If the number of selected values differs
from the ground truth, the reward is set to 0.
Since partial rewards tend to slow convergence
compared to binary signals, we train models un-
til performance stabilizes. Empirically, we find
that five epochs are sufficient for the attitude detec-
tion task, while value selection typically requires
around fifteen epochs to converge. We set the roll-
out number to 16 to ensure stable and fair gradient
updates from group-based advantage estimation.
We train the model with 4 A100 for 2-3 hours.
B.4
Ablation Study
We
conduct
ablation
studies
using
the
Llama 3.2 3B model on both the Attitude
Detection (AD) and Value Selection (VS) tasks.

--- Page 18 ---

Random
Political
Social
Religious
Ethical
Multiple
Word count
Original
19.94
20.21
20.04
18.95
19.60
16.60
Refined
35.66
34.41
30.91
33.84
35.46
26.49
Distinct-3
Original
0.877
0.878
0.876
0.860
0.875
0.850
Refined
0.941
0.939
0.939
0.937
0.940
0.919
Distinct-4
Original
0.815
0.817
0.814
0.797
0.812
0.775
Refined
0.911
0.908
0.909
0.905
0.910
0.878
Distinct-5
Original
0.755
0.755
0.752
0.742
0.750
0.702
Refined
0.882
0.878
0.878
0.874
0.880
0.837
Similarity
Original
0.510
0.488
0.574
0.742
0.508
0.491
Refined
0.433
0.408
0.473
0.355
0.415
0.425
Table 5: Statistics for explicit speech refinement show that the refined outputs exhibit greater linguistic diversity
compared to the original speech.
Value
Original Speech
Rewritten Speech
In your view, how often
do the following things occur
in this country’s elections:
Voters are bribed?–Very often
Speech:
Voter bribing happens so often ,
it feels like a norm at this point.
Explanation: The speech basically
rephrase the value without
providing supporting evidence
But honestly, I wasn’t surprised.
You hear about the rumors and
tales around voting—sometimes
it seems like it’s just
part of the landscape now.
Table 6: An example of implicitness check and rewriting.
We fine-tune the model with {50, 100, 250, 500}
stories, both with and without chain-of-thought
(CoT) reasoning. Each configuration is trained
with three random seeds, and we report the mean
and standard deviation. To examine model size
effects, we also evaluate the Qwen 2.5 14B model
on the VS task.
We summarize key findings as follows:
• Impact of dataset size. In attitude detection,
increasing dataset size does not strongly corre-
late with performance, likely because the task
involves only two to three attitude options and
the pattern is quickly learnable. In contrast,
value selection shows consistent improvement
as dataset size increases, especially from 50
to 250 samples.
• Effect of CoT reasoning. Surprisingly, non-
reasoning (W/O CoT) fine-tuning often out-
performs CoT in the Llama 3.2 3B model,
particularly in the VS task. Manual inspec-
tion reveals that smaller models struggle to
maintain coherent reasoning chains, often pro-
ducing disorganized outputs.
• Effect of model size. For the Qwen 14B
model, CoT begins to show advantage as
dataset size increases, indicating that larger
models can better leverage reasoning super-
vision. While the improvements are not uni-
versally significant, results suggest that CoT
becomes beneficial only beyond a certain data
scale and model capacity.
• Alignment with prior findings. Our observa-
tions are consistent with prior work (?), which
shows that CoT mainly benefits symbolic or
mathematical reasoning tasks, and may not
generalize as effectively to social or value-
based reasoning.
B.5
Case study on value expression
To better assess the model’s ability to express val-
ues implicitly, we conduct a small case study using
Qwen 2.5 7B. The model is prompted to respond to
an ongoing conversation given a target value, with
the goal of reflecting the value implicitly while
maintaining natural conversational flow. We com-
pare the vanilla Qwen 2.5 7B model with its GRPO-
tuned counterpart.

--- Page 19 ---

Qwen
Deepseek-distill
GPT
Deepseek
14B
32B
Q 1.5B
Q 7B
L 8B
4o-mini
V3
AD
Political
0.734
0.741
0.455
0.558
0.631
0.754
0.781
Social
0.699
0.699
0.277
0.239
0.456
0.718
0.709
Ethical
0.719
0.719
0.437
0.474
0.637
0.711
0.533
Religious
0.649
0.631
0.431
0.506
0.637
0.592
0.574
VS
Political
0.574
0.587
0.372
0.206
0.402
0.56
0.694
Social
0.567
0.618
0.305
0.314
0.323
0.568
0.715
Ethical
0.674
0.741
0.366
0.341
0.389
0.64
0.815
Religious
0.390
0.466
0.362
0.355
0.376
0.398
0.516
Table 7: Results on category-specific dataset under zero-shot reasoning setting.
Figure 8: Results of zero-shot/one-shot prompting and SFT across different categories. Overall SFT can significantly
improve the performance, especially on smaller models.
Stories
Setting
Religious
Social
Ethical
Political
Multiple
50
W/O CoT
0.5474 (0.0061)
0.6369 (0.0058)
0.5025 (0.0126)
0.6965 (0.0095)
0.5835 (0.0043)
CoT
0.5537 (0.0156)
0.6761 (0.0101)
0.5074 (0.0212)
0.6910 (0.0141)
0.5729 (0.0072)
100
W/O CoT
0.6737 (0.0062)
0.6651 (0.0089)
0.6655 (0.0046)
0.6921 (0.0063)
0.5903 (0.0060)
CoT
0.6510 (0.0125)
0.6636 (0.0059)
0.6308 (0.0122)
0.6855 (0.0063)
0.5714 (0.0105)
250
W/O CoT
0.6792 (0.0099)
0.6917 (0.0059)
0.6951 (0.0182)
0.6955 (0.0042)
0.5617 (0.0117)
CoT
0.6463 (0.0111)
0.6479 (0.0102)
0.6383 (0.0257)
0.6689 (0.0110)
0.5615 (0.0052)
500
W/O CoT
0.6863 (0.0073)
0.7232 (0.0042)
0.6716 (0.0087)
0.6885 (0.0022)
0.5632 (0.0035)
CoT
0.6820 (0.0190)
0.6918 (0.0079)
0.6728 (0.0076)
0.7178 (0.0142)
0.5623 (0.0065)
Table 8: Ablation study on Attitude Detection using Llama 3.2 3B. We report average accuracy and standard
deviation across three seeds.
To evaluate the quality of generated speech, we
employ an LLM-as-a-judge framework that as-
sesses three dimensions: value reflection, speech
naturalness, and value implicitness. We experi-

--- Page 20 ---

Stories
Setting
Religious
Social
Ethical
Political
50
W/O CoT
0.3204 (0.0070)
0.3673 (0.0177)
0.4355 (0.0132)
0.3571 (0.0339)
CoT
0.2849 (0.0035)
0.2921 (0.0145)
0.3326 (0.0074)
0.3116 (0.0116)
100
W/O CoT
0.3312 (0.0082)
0.4515 (0.0065)
0.5080 (0.0666)
0.4635 (0.0147)
CoT
0.3606 (0.0359)
0.4249 (0.0191)
0.5003 (0.0264)
0.3837 (0.0016)
250
W/O CoT
0.4668 (0.0263)
0.5429 (0.0119)
0.6525 (0.0100)
0.5666 (0.0057)
CoT
0.4172 (0.0128)
0.5300 (0.0051)
0.6304 (0.0132)
0.5263 (0.0271)
500
W/O CoT
0.4881 (0.0113)
0.5859 (0.0134)
0.7076 (0.0147)
0.5957 (0.0110)
CoT
0.4036 (0.0059)
0.5672 (0.0170)
0.6089 (0.0100)
0.5181 (0.0029)
Table 9: Ablation study on Value Selection using Llama 3.2 3B. We report average accuracy and standard deviation
across three seeds.
Stories
Setting
Religious
Social
Ethical
Political
50
W/O CoT
0.4272 (0.0156)
0.6093 (0.0087)
0.6916 (0.0079)
0.5625 (0.0154)
CoT
0.4642 (0.0091)
0.5971 (0.0179)
0.6758 (0.0093)
0.5996 (0.0021)
100
W/O CoT
0.4210 (0.0167)
0.5909 (0.0067)
0.6902 (0.0179)
0.5708 (0.0062)
CoT
0.4951 (0.0109)
0.5876 (0.0101)
0.6720 (0.0137)
0.5634 (0.0251)
250
W/O CoT
0.4099 (0.0157)
0.6002 (0.0060)
0.6794 (0.0117)
0.5821 (0.0149)
CoT
0.5461 (0.0076)
0.5868 (0.0148)
0.6697 (0.0148)
0.5962 (0.0082)
500
W/O CoT
0.4817 (0.0069)
0.6129 (0.0067)
0.7672 (0.0043)
0.6663 (0.0032)
CoT
0.5465 (0.0122)
0.6991 (0.0148)
0.7524 (0.0200)
0.6935 (0.0039)
Table 10: Value Selection results on Qwen 2.5 14B.
ment with two judging strategies: (1) pairwise
comparison, where the LLM directly compares
two speeches, and (2) independent rating, where it
scores each speech separately before comparison.
Across both evaluation methods, the GRPO-tuned
model performs slightly better, with approximately
5% of speeches showing improvement, though the
gain is not statistically significant. This case study
suggests that while GRPO tuning enhances implicit
value expression modestly, further improvements
could be achieved by jointly strengthening detec-
tion and expression capabilities.
C
Human Annotations
To compare the human performance with LLMs,
we ask several human participants from CS under-
graduates and master’s students. We cover students
from different background including 2 Chinese stu-
dents and 2 Indian students. We provide the exact
prompt we use for LLM to those students.

--- Page 21 ---

D
Prompts
In this section, we show all the prompts we use for
story generation, experiments, and validation.
Story generation prompt
##Identity
You are an expert in culture understanding.
## Task
You will be provided with 5 cultural val-
ues and a location where the conversation
happens.
Each of them follows the for-
mat [culture]–[value]. The first [culture]
describes a statement or a situation, and
[value] is how you agree with the culture or
is the culture common or not.
Your task is to generate a scene including
conversations and actions among multiple
people and the scene needs to reflect the
culture values provided.
Here are some requirements of the scene:
1. It cannot be too short. It should have mul-
tiple rounds of interaction among people.
2. It should not be too obvious. It cannot
directly spit out or rephrase the values.
3. It cannot be easy to human to understand
the culture values behind.
4. You do not need to follow the order of the
values. You could mention the values mul-
tiple times through the conversation. Make
sure the conversation flows well.
5. All the characters should follow the given
values. There should not be contradictions
between the character’s value and the given
value.
##Input
Here are the cultural values you should fol-
low when generating: values
Here is the pre-defined location of the scene:
location
##Output Now using the cultural values to
generate a story.
Incorporation check prompt
##Identity
You are an expert in culture understanding.
##Task
You will be provided a story and values re-
flected in the story. Your task is to check if
the story reflects values? The story does not
mention the values directly. You will need
some reasoning to analyze the story.
##Input
Here is the original story: story
Here are the values to reflect in the story:
values
##Output
For each value, output if the value is re-
flected and provide reasoning. In the end,
output the values not reflected without the
reasoning. Only output the exact and com-
prehensive value including "–" within it,
do not rephrase! If all the values are re-
flected, just leave it blank. Follow the for-
mat: [Value]:[Reasoning, Yes/No] ..... Val-
ues not reflected: [Value]
Missing values incorporation prompt
##Identity
You are an expert in culture understanding.
##Task
You will be provided a story and values
which need to be reflected in the story.
Your task is to refine the story to reflect the
value provided. You cannot remove any-
thing or replace existing speeches from the
story, you can only add conversations to
reflect the value.
The refinement should flow with original
story well. You cannot add new conversa-
tion randomly.
##Input Here is the original story: story
Here are the values to reflect in the story:
values
##Output Now refine the story.

--- Page 22 ---

Consistency check prompt
##Identity
You are an expert in culture understanding.
##Task You will be provided a story and
values reflected in the story. Your task: for
each value, check if all the characters agree
with the value. If there is characters who
does not agree with the value, you should
output the character’s name and his speech,
and why the speech does not align with the
value.
##Input Here is the original story: story
Here are the values to reflect in the story:
values
Now check the story and output if there is
any contradiction. You can output reasoning
to help you analyze. However, in the end,
only output where is the contradiction one
by one. If there isn’t a contradiction, just
reply NO. Otherwise, reply where is the
contradiction.
##Output Follow the format strictly, do not
change the format, output exact values from
the values provided, and do not rephrase:
[Reasoning]:
[Value–attitude]:[If all the speeches are
aligned with the value]
[Contradictions]:
[Value–attitude]:
[*character
name*:speech] ......
Consistency resolve prompt
##Identity
You are an expert in culture understanding.
##Task
You will be provided a story and values
which need to be reflected in the story. How-
ever, the story includes some contradiction
where characters do not agree on certain
values. You will be provided where is the
contradiction.
The contradiction includes 3 parts:
1. Correct value to follow
2. Character name
3. Character speech
Your task is to replace the speech mentioned
in the contradictions with a new speech to
make sure the speech is aligned with the
values The refinement should flow with the
original story well. You cannot add new
conversations randomly.
##Input Here is the original story: story
Here are the contradictions: contradiction
Ignore the original character’s speech. Di-
rectly write a new speech that reflects the
value.
##Output Here is the rewritten speech:

--- Page 23 ---

Implicitness check prompt
##Identity
You are an expert in culture understanding.
##Task You will be provided a story and
values reflected in the story. Your task is to
check if there is obvious speech that directly
mentions or rephrases the values. If the
story mentions phrases or sentences from
values, that would be also counted as di-
rectly mentioned If it just reflects the value
but does not rephrase the values, it is not
considered as obvious speech. Here are
some examples of obvious speech:
[Example 1]
Value: In your view, how often do the
following things occur in this country’s
elections: Journalists provide fair cover-
age of elections—Very often Speech: "I
think journalists do their best to cover things
fairly" Explanation: The speech basically
rephrases the value without providing sup-
porting evidence
[Example 2]: .......
You should output places where the values
are directly mentioned. If the values are not
directly spit out, do not output them!!!
##Input Here is the original story: story
Here are the values to reflect in the story:
values
##Output Now check if any parts of the sto-
ries directly mentioned the values. You can
output reasoning or evidence and help you
analyze. However, in the final answer, out-
put speeches where the values are directly
mentioned and the corresponding values. If
there are no directly mentioned values, just
output NO in the final answer.
Follow the format:
[Reasoning]: reasoning
[Final answer]: [value]:[speech]
[value]:[speech] .....
Implicitness rewrite prompt
##Identity
You are an expert in culture understanding.
##Task
You will be provided a story and values re-
flected in the story. You will be also pro-
vided with some comments where the val-
ues are directly mentioned in the story. Each
comment includes a value and a speech
where the speech directly reflects the value.
Your task is to refine the speech by rewrit-
ing the places where they directly mention
the values. Instead of speaking out values
directly, characters should reflect values im-
plicitly by using anecdotes. Imagine the
place is not a safe place to speak out, char-
acters need to respect each other and not
offend others. You need to make sure after
rewriting, people are able to detect values
by the speech. It cannot be too abstract.
Here are some examples:
[Example 1]: Value: How frequently do
the following things occur in your neighbor-
hood: Robberies?–Not frequently Original
speech: “Well, at least we’re not dealing
with robberies or anything in our area.” Re-
fined speech: "You know in other counties,
cars got breaking in is common. At least we
don’t have to worry about that."
[Example 2]: .....
##Input Here is the original story: story
Here are the values to reflect in the story:
values
Here are the comments that you need to
refer to when refining the story: comments
##Output
Please rewrite the speech one by one in the
story. Do not miss any comments.
For each rewritten speech, you need to
follow this format: Value:[value] Original
speech: [Speech in the comment] Refined
speech: [You rewritten speech]
Here is your output:

--- Page 24 ---

Attitude detection prompt
##Identity
You are an expert in culture understanding.
##Task
You will be given a scenario including back-
ground, conversation and actions in a loca-
tion. You task is to detect the culture values
reflected from the conversation. You will
be provided a statement and you need to
detect what attitude they hold to the value.
For example, the statement is "The people
who don’t work turn lazy" and the options
are "disagree, agree, neither disagree nor
agree". And you need to read the story and
choose one attitude from the options. The
options could also describe something hap-
pening around them. For example, if the
statement is "How often does this happen in
your neighborhood:Racist behaviors", the
options are "Very often, not often, not at all
often", you need to choose one based on the
story.
##Input Here is the scenario: story
Here is the statement: statement
Here are the options: options
##Output Now choose one option based on
the story. Let’s think step by step! First,
extract the speech that is related to the state-
ment.Then analyse the attitude of those peo-
ple from the speech. Finally, output the
answer.
Follow the format:
[Related speech]: speeches
[Analysis]: analysis of attitude
[Answer]:answer
Value selection prompt
##Identity
You are an expert in culture understanding.
##Task You will be given a scenario includ-
ing background, conversation and actions in
a location. You task is to detect the culture
values reflected from the conversation.
You will be provided 15 options and you
need to select number correct answers from
the options. (Only number options are cor-
rect).
You need to choose the whole option, for
example:
Being a housewife is just as fulfilling as
working for pay–agree
Make sure you include ’–’ in the answer.
##Input
Here is the scenario: story
Here are the options: options
## Instruction To think step by step: 1. You
need to first detect what topics the story
mentioned according to the options. You
need to list the speech related to the topic.
2. Then for each topic, detect what values
might be related to the topic. Sometimes,
you might find multiple options that might
be correct, for uncertain options, you should
compare them. 3. Based on the previous
detection, analyze what values are aligned
with the story, you should always prioritize
those values that are strongly related. 4. In
the end, output the final answers only. Only
choose the required number of values.
##Output Follow the format:
[Topic]:
topic1: speeches related to the topic .....
[Value detection]: topic1: what values are
related to the topic
[Reasoning]: Reasoning
[Final answer]:
[text] – [text]
.....
"""

--- Page 25 ---

Value extraction prompt
##Identity
You are an expert in culture understanding.
##Task
You will be provided with a story. Your goal
is to identify the most prevalent topic val-
ues in the story. For example, one religious
value could be: I strongly believe in God
and the afterlife. The value should be a com-
plete sentence, it should not be a phrase like
work-life balance. The value should hold
a attitude or it reflects social phenomena,
it should not be a overview of topic. For
example, one social value could be: I think
work is a duty towards the society. And one
political value could be: I think voters are
bribed in our election system. Please iden-
tify the values in this story: story by paying
attention to how the characters in the story
discuss topic. You need to generate 10 val-
ues in total, make sure values are specific
and detailed. Only focus on one topic in
one value. Do not mention several themes
in one value.
##Input Here is the story: story
Here is a story summary with some key
ideas: summary.
##Output
You could output reasoning before you out-
put final answer. But in the end, your output
should follow the format: [Final answer]:
value1 value2 ....
LLM evaluation prompt
##Identity
You are an expert in culture understanding.
##Task
You will be given two sets of texts: a set of
predicted values and a ground truth set of
values. Your task is to determine how many
of the ground truth values are fully repre-
sented in the predicted values. A ground
truth value is considered correct if all of its
components are meaningfully discussed in
the predicted value, even if there is no exact
1-to-1 match. It could be many-to-1 match
i.e. many values to 1 ground truth value.
If the ground truth value is fully presented,
score 1, if it is partially presented, score 0.5,
if it is not mentioned at all, score 0. Ad-
ditionally, provide a brief justification for
your score, explaining which values were
correctly or incorrectly represented, in the
justification, you should explicitly mention
which predicted values are related to the
ground truth value.
##Input
Here are the predictions: pred and ground
truth: gt In the reasoning, if the ground truth
value is fully represented, you need to point
out which predicted value is related to it.
##Output
Return the results in this format: [Reason-
ing]:
[Ground truth 1]: [reasoning]
.....
[Final answer]:
[Ground truth 1]:1
[Ground truth 2]:0.5
......

```
