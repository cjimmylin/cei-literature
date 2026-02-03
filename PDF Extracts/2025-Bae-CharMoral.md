---
title: "CharMoral - PDF Extract"
source_pdf: "2025-Bae-CharMoral.pdf"
pages: 10
extracted_at: "2026-01-24T16:38:23.526679"
---

# PDF Extract: CharMoral

**Source PDF:** 2025-Bae-CharMoral.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

Proceedings of the 31st International Conference on Computational Linguistics, pages 8809–8818
January 19–24, 2025. ©2025 Association for Computational Linguistics
8809
CharMoral: A Character Morality Dataset for Morally Dynamic
Character Analysis in Long-Form Narratives
Suyoung Bae1, Gunhee Cho1, Boyang Li2, Yun-Gyung Cheong*1
1 Sungkyunkwan University, South Korea
2 Nanyang Technological University, Singapore
1 {sybae01, skate4333, aimecca}@skku.edu, 2 boyang.li@ntu.edu.sg
Abstract
This paper introduces CharMoral, a dataset
designed to analyze the moral evolution of
characters in long-form narratives. CharMoral,
built from 1,337 movie synopses, includes an-
notations for character actions, context, and
morality labels. To automatically construct
CharMoral, we propose a four-stage frame-
work, utilizing Large Language Models, to au-
tomatically classify actions as moral or im-
moral based on context. Human evaluations
and various experiments confirm the frame-
work’s effectiveness in moral reasoning tasks
in multiple genres. Our code and the Char-
Moral dataset are publicly available at https:
//github.com/BaeSuyoung/CharMoral.
1
Introduction
Value alignment, the task of ensuring that lan-
guage models and agents operate in accordance
with human values, is a critical challenge in the de-
velopment of ethical AI (Russell, 2019; Wolf et al.,
2023). As psychological research highlights that
narratives function as social simulations, allowing
individuals to develop and refine social skills (Oat-
ley, 2008), analyzing the ethical behavior of char-
acters in stories offers valuable insights for deploy-
ing ethical language models. By examining both
the moral actions of characters and the reactions of
others within the narrative, agents can more effec-
tively learn to align with human ethical standards,
enhancing their capacity for contextually appropri-
ate language understanding and generation.
Previous research on character analysis has
mainly focused on three key areas: character iden-
tification (Chen and Choi, 2016; Brahman et al.,
2021; Yu et al., 2022), social network analy-
sis (Lee and Jung, 2019; Fischer, 2021; TARASE-
VICH et al., 2023), and the exploration of char-
acters’ personas or personalities (Bamman et al.,
*Corresponding author.
movie name: Harry Potter and the Deathly Hallows
mid: tt1201607  rating: 8.1   story len: 1240
genre: ['Adventure', 'Drama', 'Fantasy’]
After burying [Dobby] at the garden of the Shell 
cottage, [Harry Potter] convinces [Griphook] to help 
them get to Lestrange's vault in [Gringotts], to 
retrieve one of [Voldemort]'s Horcruxes in exchange 
for Godric Gryffindor's Sword. Meanwhile, 
Ollivander , the [Wandmaker] warns [Harry] that he 
won't stand a chance with [Voldemort] who has the 
Elder Wand. They arrived in [Gringotts], Hermione 
disguised as Bellatrix , using a Polyjuice Potion, [Ron] 
disguised as a random wizard while [Harry] and 
[Griphook] go under the Invisibility Cloak. 
sid: 0   seg len: 80
…
Char: Gringotts
Situation: 
The 
setting 
involves 
[mask], 
where 
security is on high alert after 
the intruders' cover is blown. 
Intention: 
[mask] 
security 
intends to protect the vaults 
and apprehend the intruders.
Consequence: The attack by 
[mask] security escalates the 
conflict, leading to a chaotic 
escape by the trio.
label: immoral
Char: Harry Potter
Situation: 
After 
burying 
Dobby at the garden of the 
Shell cottage, [mask] Potter 
convinces Griphook to help 
them get to Lestrange's vault 
in Gringotts.  
Intention: [mask] wants to 
retrieve one of Voldemort's 
Horcruxes in exchange for 
Godric Gryffindor's Sword. 
Consequence: not exist 
label: moral
Char: Harry
Situation:  [mask] and his 
companions are in Gringotts, 
where 
they 
have 
just 
accessed Lestrange's vault to 
find the Horcrux.
Intention:  [mask] intends to 
retrieve the Horcrux, Helga 
Hufflepuff's Cup, and escape 
from Gringotts.
Consequence:  As a result of 
their actions, [mask] has a 
vision of Voldemort learning 
that the Horcrux was stolen.
label: immoral
sid: 1  seg len:93
With the help of Imperius curse, they manage to get 
to the carts that take them down to the vaults, but 
when their cover is blown, [Gringotts] attacks them. 
They manage to get to Lestrange's vault and find 
the Horcrux, Helga Hufflepuff’s Cup, at which 
[Griphook] betrays them and flees with the sword 
yelling "Thieves! Thieves!" [Harry] grabs the Horcrux 
and the trio escape using a captive dragon. As they 
swim ashore of a lake, after jumping off the dragon, 
[Harry] has a vision about [Voldemort] receiving the 
news that the Horcrux was stolen. 
Figure 1: An example of CharMoral dataset with an-
notated actions’ morality considering contexts. In each
segment, we extract character “actions”, and related
“contexts” . Then, we annotate the morality of the ac-
tions, considering each context.
2013; Kim et al., 2019; Sang et al., 2022; Yu
et al., 2023). However, the analysis of characters’
moral stances remains an under-explored area of
research, primarily due to several significant chal-
lenges. First, moral reasoning of actions is highly
dependent on context (Pyatkin et al., 2022). For
example, the action of ‘throwing a bomb at the
door’ might generally be considered unethical, but
in the context of rescuing trapped individuals from
aliens, it could be perceived as morally justified.
Second, a character’s morality is not static and
may evolve throughout the narrative, influenced
by unexpected events and interactions with other

--- Page 2 ---

8810
Dataset
#Stories
#Words per story
#Characters
Genres
Morality Labels
#Annotations
Storium (Akoury et al., 2020)
5,743
19,278
25,955
✗
✗
-
TVSTORYGEN (Chen and Gimpel, 2021)
29,000
1,868
34,300
✓
✗
-
Story2Personality (Sang et al., 2022)
507
1,381
3,543
✗
✗
-
Moral stories (Emelin et al., 2021)
12,000
90
12,000
✗
✓
12,000
CharMoral
1,337
1,665
9,389
✓
✓
103,836
Table 1: Comparison of the CharMoral dataset with previous story datasets used for character analysis. #Annota-
tions refers to the number of morally annotated actions in the entire #Stories.
characters who maintain their moral principles.
Despite the importance of this dynamic, existing
datasets do not facilitate the analysis of moral evo-
lution in long-form narratives. Current datasets,
such as Moral Stories (Emelin et al., 2021), focus
on short narratives with isolated moral situations.
Constructing a dataset that captures moral devel-
opment over time is particularly challenging, as
it requires human annotators, which can be both
time-consuming and costly.
To overcome these limitations, we introduce
a novel dataset called CharMoral, Character
Morality dataset designed to analyze characters
with dynamic moral stances in long-form nar-
ratives. This dataset enables the study of how
morally dynamic characters influence readers’ un-
derstanding and affect story engagement. Char-
Moral consists of a curated collection of 1,337 sto-
ries extracted from movie synopsis datasets. As
outlined in Figure 1, each story is annotated with
detailed information, including story segments,
character names, actions within segments, contex-
tual information surrounding these actions, and
corresponding morality labels.
Our framework operates in four stages. First,
we segment the story based on key events involv-
ing the main characters. Second, we utilize an
LLM to extract characters’ actions from each seg-
ment. Third, the LLM is employed again to ex-
tract contextual information–the situation, inten-
tion, and consequence–related to each action. Fi-
nally, we classify the morality of the character’s
actions within their contexts using a fine-tuned ex-
pert model, which is optimized to accurately pre-
dict moral judgments by factoring in contextual
information. This approach ensures a comprehen-
sive and scalable annotation process, facilitating
the analysis of moral dynamics across a large cor-
pus of long-form narratives.
We evaluate our dataset and annotation frame-
work through a human evaluation to measure how
closely it aligns with human moral judgments. Fur-
thermore, we assess the quality and effectiveness
of the dataset in training morality classifiers by per-
forming a range of tasks, including zero-shot, few-
shot, fine-tuning, and cross-domain evaluations.
The contributions of our work are as follows:
• We present a novel dataset for analyzing char-
acter morality in long-form narratives.
• We develop a framework leveraging LLMs
to extract character actions and contextual in-
formation (situation, intention, consequence),
enabling large-scale moral analysis.
• We developed a classification model, MAD,
which outperforms GPT-3.5 and GPT-4 in
moral reasoning tasks.
• We propose a new metric to track the moral
dynamics of characters and explore its corre-
lation with story engagement.
This paper is structured as follows. Section 2 re-
views related work, Section 3 presents the dataset
and framework, Section 4 details the experimen-
tal setup and morality classification, Section 5 an-
alyzes morally dynamic characters, and Section 6
discusses key findings and future directions.
2
Related Work
2.1
Character-Centric Narrative Understanding
Character analysis is essential for narrative under-
standing, as characters are pivotal in driving the
story forward (Bower and Morrow, 1990). The pre-
vious study of characters has largely concentrated
on three main areas. First, character identifica-
tion, which aims to identify and associate various
mentions of characters throughout a text (Chen
and Choi, 2016; Brahman et al., 2021; Yu et al.,
2022). For example, Chen and Choi (2016) trained
a model to identify characters mentioned in TV
show series datasets and determine which charac-
ter a pronoun refers to.

--- Page 3 ---

8811
B’s action
(3) Context 
Extraction
(2) Action 
Extraction
(4) Moral 
Action Detection
A’s action
A’s contexts
B’s contexts
seg n-1
seg 2
seg n
Input 
Story
...
seg 1
B’s action
Immoral 
(0.0021)
Context 
Extraction
Action 
Extraction
Moral Action 
Detection
A’s action
A’s contexts
B’s contexts
Moral 
(0.9887)
Event-Centric Story 
Segmentation
CharMoral
1
n
…
…
…
contexts
= Situation +Intention + Consequence
Figure 2: Overview of the CharMoral Dataset Construction Framework for annotating the moral stances of char-
acters’ actions in long-form narratives.
Castor
Archer
Castor
Archer
Pollux
Castor
Wanda
Archer
Castor
Wanda
Archer
Castor
Wanda
Archer
Seg 1
Seg 2
Seg 3
Sent 1-3       Sent 4-6      Sent 7-9     Sent 10-12    Sent 13-15    Sent 16-18
Initial Segmentation
Basic Units: 3
Identifying Segment
Characters
Merging Segments
Figure 3: The illustrations of the Event-Centric Story Segmentation Process.
Second, social network analysis uses the occur-
rence and co-occurrence of characters within the
story to construct social networks for analyzing
the narrative (Lee and Jung, 2019; Fischer, 2021;
TARASEVICH et al., 2023). Through social net-
works, it’s possible to analyze the relationships
and intimacy levels among characters, extracting
information about key characters, close allies of
the protagonist, and antagonists. Recent research
has been actively exploring the use of character
personas and personality analysis (Bamman et al.,
2013; Kim et al., 2019; Sang et al., 2022; Yu et al.,
2023). However, analyzing the morality of charac-
ters is under-explored.
2.2
Character Morality Datasets
Gert and Gert (2020) defines ‘Morality’ as “cer-
tain codes of conduct put forward by a society
or a group (such as religion and nationality), or
accepted by an individual for her own behav-
ior.” Prior research has focused on creating anno-
tated datasets for machine ethics, such as Social
Chemistry (Forbes et al., 2020), Scruples (Lourie
et al., 2020), Moral Stories (Emelin et al., 2021),
ETHICS (Hendrycks et al., 2021), and COM-
MONSENSE NORM BANK (Jiang et al., 2022).
However, most datasets focus on morality classi-
fications in a short text, typically one sentence
long, and fail to capture the complexity of con-
text needed for moral reasoning. In contrast, Char-
Moral offers longer, context-rich stories for deeper
moral analysis.
Several datasets are available for character anal-
ysis in narrative (Akoury et al., 2020; Chen and
Gimpel, 2021; Sang et al., 2022) as shown in Ta-
ble 1. However, these datasets lack annotations
related to the moral personalities of characters.
Whereas Emelin et al. (2021) have attempted to
annotate moral aspects of character actions in a
story, their dataset consists of short stories with
only single situations, making it difficult to ob-
serve changes in a character’s morality throughout
the narrative.
3
Building the CharMoral Dataset
The CharMoral dataset is reconstructed by execut-
ing the four steps illustrated in Figure 2: Event-
Centric Story Segmentation, Action Extraction,
Context Extraction, and Moral Action Detection.
CharMoral is built based on the IMDB Spoiler
Dataset 1, which consists of 1,572 movie synopses
and meta-information from IMDB, providing de-
tailed descriptions of characters’ actions and their
outcomes. For this study, we use 1,337 narratives,
eliminating fewer than 10 words.
3.1
Event-Centric Story Segmentation
The first step segments each story based on key
events involving the main characters. This method
draws upon earlier work, as described in Kim et al.
(2022), highlighting the significance of the main
characters in these pivotal narrative moments.
As shown in Figure 3, the first step divides
the story into segments of s sentences. 2 The
1https://www.kaggle.com/datasets/rmisra/
imdb-spoiler-dataset
2In this paper, we manually set s to 3 through a pilot ex-
periment.

--- Page 4 ---

8812
main characters are then identified as the five
most frequently mentioned names in the story.
To extract these characters, we utilize Stanford
CoreNLP (Manning et al., 2014) for co-reference
resolution and Named Entity Recognition (NER)
to identify character names. Consecutive segments
that feature the same set of main characters are
merged into a single segment. For example, if
‘Ryan’ and ‘Clark’ appear in two consecutive seg-
ments but are absent in the next, those segments
are combined.
3.2
Action Extraction
Since the story lacks meta-information regarding
the characters and their corresponding actions,
we extract this by using GPT-4o (OpenAI, 2023).
Each segment and the names of the characters
mentioned are fed into the LLM using a prompt
manually engineered for extracting characters’ ac-
tions. If there is no action associated with the char-
acter, the output is ‘no action’ and excluded from
our dataset. The prompt is detailed in Table 19.
3.3
Context Extraction
The moral reasoning behind a character’s actions
is highly context-dependent (Pyatkin et al., 2022),
and moral assessments can vary based on situa-
tions and intentions (Emelin et al., 2021). To as-
sess morality accurately, we extract the action’s
situation, intention, and consequence, prompting
LLM which was the same model used for charac-
ter action extraction. If the corresponding context
is missing, the output is ‘not exist’. The context
extraction prompt is shown in Table 20.
3.4
Action Morality Detection
To accurately annotate whether the actions of the
characters are morally justified based on their con-
textual information, we employ an expert model,
the Moral Action Detector (MAD). To provide re-
liable moral evaluations and ensure accurate pre-
dictions that account for relevant context, we fine-
tuned the BERT-large model (Devlin et al., 2019)
using the Moral Stories dataset (Emelin et al.,
2021), following the same fine-tuning settings as
described in Emelin et al. (2021)
Using the MAD, we predict whether the charac-
ter involved in the action has performed a moral
or immoral act by inputting the four extracted sen-
tences (situation, intention, consequence, and ac-
tion). In addition to the moral classification, we
store the softmax logit scores for further analysis.
After Segmentation
#Story
1,337
#Segment
30,616
Story Mean length
1,665
Segment Mean length
85
After Context Extraction
#Character
9,389
#Annotations
103,836
#Action exists
103,836 (100%)
#Situation exists
103,813 (99.98%)
#Intention exists
92,627 (89.2%)
#Consequence exists
82,076 (79.04%)
#All exists
75,724 (79.93%)
Label Distribution
#Moral
50,717
#Immoral
53,119
Table 2: The statistics of CharMoral
3.5
The Statistics of CharMoral
The statistics of CharMoral are presented in Ta-
ble 2. #Character refers to the total number of
characters appearing in our dataset, #Annotations
refers to the number of morally annotated actions
in the entire #Stories, and #Action, #Situation,
#Intention, and #Consequence exist indicate the
number of datasets where the respective compo-
nent is present and it’s proportion. Finally, #All ex-
ists refers to the number of datasets where the char-
acter’s action and context have all been extracted.
The CharMoral labels consist of moral and im-
moral. Details about the dataset are described in
the Appendix A.
4
Evaluation
4.1
Human Evaluation
We evaluate the effectiveness of our framework by
comparing its predictions with human assessments
and recruiting nine proficient English-speaking
graduate students for the task. Every annotator
evaluates the moral dimensions of 50 randomly
sampled sentences (character actions with con-
text). We then use majority voting based on the
annotation results of 9 annotators in each sen-
tence. The Inter-Annotator Agreement, measured
using Fleiss’ kappa (Cohen, 1960), is 0.55, show-
ing moderate agreement among evaluators (Ap-
pendix C for details).
Table 3 presents the human evaluation results,
showing that our framework achieves approxi-
mately 64% agreement with human assessments
when using only the action itself (A) to predict

--- Page 5 ---

8813
Model
MAD
GPT 3.5
GPT 4
Setting
A
SA
IA
CA
SIA
SCA
ICA
SICA
(Segment) + A
Acc
0.64
0.6
0.7
0.76
0.6
0.76
0.72
0.92
0.78
0.86
Table 3: The results of human assessments compare the moral action classification performance of MAD and LLMs.
For MAD, we evaluate using different context settings as outlined in Table 4. For GPT 3.5 and GPT 4, morality is
assessed by providing the entire text segment along with the character’s action.
morality. This agreement significantly increases to
92% when full context (SICA) is considered.
We also compare the performance of two LLMs
(GPT-3.5 and GPT-4) with human assessments
to show that using the extracted context factors
directly related to actions yields more accurate
morality predictions than relying solely on the
LLMs’ internal knowledge. We provide LLMs
with the text segment and action to evaluate the
morality of the actions. MAD significantly im-
proves moral action predictions, outperforming
GPT-3.5 and GPT-4, which achieve 78% and 86%
agreement, respectively. This highlights the supe-
rior performance of our model in making the pre-
dictions more closely aligned with human judg-
ment.
4.2
Action Morality Classification
4.2.1
Experimental Setups
We conduct experiments to evaluate the effec-
tiveness of our automatically building CharMoral
dataset across various moral reasoning tasks. Ad-
ditionally, we analyze the impact of varying con-
textual information on classification performance.
We define eight settings with varying levels of
contextual information, as outlined in Table 4, in-
cluding one setting with no context provided (A).
In each case, the model classifies actions as moral
or immoral based on the available context.
We use the BERT-large model (Devlin et al.,
2019) trained using CharMoral to assess the
morality classification performance. To verify the
model’s transferability, we also test cross-domain
classification
on
two
out-of-domain
datasets,
Moral Stories (Emelin et al., 2021) and Social
Chemistry (Forbes et al., 2020). Additionally, we
evaluate classification performance in zero-shot
and few-shot settings to determine whether Char-
Moral provides high-quality demonstrations for
accurate moral reasoning. We compare the per-
formance of two LLMs, GPT-3.5 and GPT-4o 3,
3https://openai.com/.
Setting
Context
A
-
SA
Situation
IA
Intention
CA
Consequence
SIA
Situation + Intention
SCA
Situation + Consequence
ICA
Intention + Consequence
SICA
Situation + Intention + Consequence
Table 4: Eight input settings in varying amounts of con-
text information for moral action classification tasks.
For all classification tasks, the model input is format-
ted as <CLS>context<SEP>action<SEP>.
using the SICA input setting. In the few-shot set-
ting, examples are sampled from CharMoral to
create demonstrations, showing that our dataset
effectively supports few-shot tasks by providing
high-quality examples. Additional details can be
found in Appendix D.
4.2.2
Results
As shown in Table 5, the classification model
trained on an in-domain setting demonstrates ex-
ceptional performance, achieving an accuracy of
94.7% when all contextual information is consid-
ered (SICA). The model also maintains strong per-
formance in cross-domain settings, with an accu-
racy of 96.9% when tested on the Moral Stories
dataset and 70.7% on Social Chemistry.
Table 6 presents the results of zero-shot and few-
shot evaluations. The results demonstrate that the
performance in both zero-shot and few-shot set-
tings is reasonable, with GPT-3.5 achieving an ac-
curacy of 61.7% in zero-shot, and GPT-4o achiev-
ing 66.7%. In the few-shot setting, the accuracy in
the 3-shot setting improved to 62.7% for GPT-3.5
and 68.4% for GPT-4o. We also observe that as the
number of demonstration examples increases, per-
formance generally improves. This demonstrates
that the CharMoral dataset is effective in creating
high-quality demonstrations, leading to strong per-
formance in few-shot tasks.

--- Page 6 ---

8814
In-domain
Cross-domain
Train →Test
Ours →Ours
Ours →MS
Ours →SC
Metric
Acc
F1
Acc
F1
Acc
F1
A
0.692
0.712
0.689
0.716
0.823
0.778
SA
0.708
0.722
0.697
0.719
0.810
0.739
IA
0.709
0.718
0.684
0.701
0.858
0.823
CA
0.929
0.928
0.967
0.967
0.850
0.829
SIA
0.725
0.733
0.693
0.706
0.795
0.710
SCA
0.933
0.930
0.966
0.966
0.783
0.758
ICA
0.939
0.938
0.968
0.968
0.819
0.801
SICA
0.947
0.947
0.969
0.969
0.707
0.655
Table 5: The results of fine-tuning moral action classi-
fication tasks: The first row shows the accuracy and F1
score when trained and tested on the CharMoral. The
second and third rows show the cross-domain classifi-
cation results, where the model is trained on the Char-
Moral and tested on the Moral Stories (MS) and Social
Chemistry (SC), respectively. The bold is the best score
in each input setting.
Model
GPT-3.5
GPT-4o
Metric
Acc
F1
Acc
F1
zero-shot
0.617
0.685
0.667
0.680
1-shot
0.619
0.688
0.667
0.690
3-shot
0.627
0.703
0.684
0.693
5-shot
0.622
0.708
0.683
0.692
Table 6: The results of zero-shot and few-shot context-
aware moral action classification task: The bold is the
best score in each setting.
5
Morally Dynamic Character Analysis
5.1
Moral Dynamic Score
Through the CharMoral, we can observe how char-
acters’ morality changes throughout long-form
narratives. By analyzing the moral dynamics of
characters, we can enhance people’s understand-
ing of the story and provide information to auto-
matically identify stories that are both instructive
and engaging.
We define a morally dynamic character as
a character whose morality shifts dynamically as
events unfold in a long story and a morally static
character as one who acts consistently according
to a stable set of moral values. To observe the
moral dynamics of characters within a story, we
introduce a new score, which we refer to as the
moral dynamic score of a character (c). The moral
dynamic score is defined as follows:
Rate
0∼4
4∼5
5∼6
6∼7
7∼8
8∼9
9∼10
# Story
4
14
112
375
531
289
7
# Character
11
90
409
1,547
2,397
1,279
55
# Dynamic Character
5
20
226
812
1,253
668
25
Figure 4: The above line plot represents the average
number of dynamic characters per story by rate and the
bottom table represents related statistics by rate.
Moral dynamic score:
scorec =
(#passc)
(#segmentc) −1
Morally dynamic character:
dynamicsc =
(
dynamic
if scorec ≥0.5,
static
otherwise
CharMoral records morality prediction values
for each character’s actions as softmax logit scores
between 0 to 1. To track changes in a character’s
morality over time, we calculate how often a char-
acter’s logit score crosses the 0.5 midpoint (The
number of times MAD’s prediction switches from
immoral to moral or from moral to immoral during
segment progression.), referred to as the number
of passes (#passc). We then divide the number
of passes by the total number of segments where
the character c appears, minus one to calculate
the rate of the character’s morality change. The
scorec can range from 0 to 1. If the scorec is 0.5
or higher, we classify the character c as a morally
dynamic character, and otherwise, as a morally
static character.
5.2
Analysis
Using the moral dynamic score defined in sec-
tion 5.1, we draw three conclusions (A1, A2, and
A3) from the analysis of story characters’ moral
dynamics and its correlation with story interest.
A1: A greater number of morally dynamic char-
acters positively contributes to the story’s over-
all interest. We investigate the relationship be-
tween the number of morally dynamic characters

--- Page 7 ---

8815
Rate
0∼4
4∼5
5∼6
6∼7
7∼8
8∼9
9∼10
# Story
4
14
112
375
531
289
7
# Dynamic main character
0
3
42
171
221
128
4
Figure 5: The above box plot represents the percent of
the story where there is a dynamic main character by
rate and the bottom table represents the statistics by
rate.
and a story’s level of interest by comparing the
average number of dynamic characters across dif-
ferent rating groups. The average number of dy-
namic characters per story for each rating group is
depicted as a line graph in Figure 4. The graph
shows that when the rating is between 0 and 4,
the average number of dynamic characters is 1.25,
while as the rating increases, this number gradu-
ally rises, reaching an average of 3.57 in stories
with ratings between 9 and 10. These results sug-
gest that a higher number of morally dynamic char-
acters is linked to greater story engagement.
A2: The moral evolution of the main character
plays a key role in increasing the story’s over-
all interest. We examine whether the moral evo-
lution of the main character (the most frequent
character), rather than just the total number of
morally dynamic characters, affects story engage-
ment. Specifically, we look at the proportion of sto-
ries in each rating group where the main character
is morally dynamic. Figure 5 presents this propor-
tion as a bar graph, showing the ratio of stories
with a morally dynamic main character to the to-
tal number of stories for each rating group. In sto-
ries with a rating between 0 and 4, none of the
main characters are dynamic, whereas in stories
with a rating between 9 and 10, 57% of the main
characters are dynamic. These results suggest that
stories with higher ratings tend to have morally
dynamic main characters, highlighting the impor-
tance of the main character’s moral evolution in
making a story more engaging.
A3: Morally dynamic main characters have a
significant impact on genre-specific story en-
gagement and ratings. We examine the impact
Genre
% Dynamic main character
Avg. Rate
Musical
60.00
7.28
Western
60.00
7.96
War
56.52
8.15
Thriller
50.95
7.22
Action
50.90
6.87
Film-Noir
50.00
8.23
Fantasy
49.38
6.96
Adventure
47.67
7.03
Sci-Fi
43.89
6.99
Mystery
42.65
7.47
Crime
42.63
7.38
History
41.82
7.63
Drama
41.42
7.47
Family
40.71
6.79
Horror
40.20
6.74
Biography
40.00
7.71
Romance
39.06
7.10
Comedy
37.68
6.85
Animation
35.62
7.45
Sport
28.00
7.11
Music
21.74
7.04
Table 7: Proportion of morally dynamic main charac-
ters and average rating across story genres.
of morally dynamic main characters on genre-
specific engagement and ratings. Table 7 shows
the proportion of stories in each genre with
morally dynamic main characters, alongside their
average ratings.
The Western genre has the highest proportion
of morally dynamic main characters (60%) and a
strong average rating of 7.96. Genres like Musical,
War, and Thriller also show high proportions of dy-
namic main characters, with Musical (60%) and
War (56.52%) achieving average ratings of 7.28
and 8.15, respectively. This suggests that the moral
evolution of the main character plays a key role
in enhancing story interest and ratings. Similarly,
Film-Noir, History, and Biography feature high
proportions of morally dynamic characters, with
average ratings between 7.63 and 8.23. These gen-
res often explore complex moral dilemmas, where
the protagonist’s internal conflicts are central to
the narrative. In contrast, genres like Sport (28%)
and Music (21.74%) have lower proportions of dy-
namic main characters and correspondingly lower
ratings, between 7.04 and 7.11.
In summary, genres with a higher proportion of
morally dynamic main characters tend to receive
higher ratings, suggesting that audiences are more
engaged with stories that feature significant char-
acter growth or moral conflict. In genres where
moral dynamics are less important, like Sport and

--- Page 8 ---

8816
Action
Situation
Intention
Consequence
A
SICA
Human
[Scar] manages to
knock Simba down
and leaps at him
[Scar]
manages
to
knock
Simba down and leaps at him,
creating a tense confrontation
at Pride Rock.
[Scar]
intends
to
defeat
Simba and assert his domi-
nance.
As a result of [Scar]’s action,
he finds himself surrounded
by the hyenas, who are now
turning against him.
I
IM
IM
[Lupin] has Harry
test himself out on a
Boggart.
After Professor Snape discov-
ers Harry out of bed, the map
is
confiscated
by
[Lupin]
who meets them in a set-
ting filled with tension and se-
crecy.
[Lupin] wants Harry to learn
how to generate a Patronus by
testing himself against a Bog-
gart.
By having Harry confront
the Boggart, [Lupin] aims to
help him improve his magical
skills and ultimately succeed
in conjuring a Patronus.
IM
M
M
[Maurice]
tells
Malcolm Ellie and
Alex to run.
[Maurice] tells Malcolm, El-
lie, and Alex to run as the
other apes become frightened
and wild.
[Maurice] wants to ensure
the safety of Malcolm, Ellie,
and Alex by urging them to
escape.
The action may lead to the
group avoiding danger and
potentially
surviving
the
chaotic situation.
IM
M
M
Table 8: Comparison of context-aware moral action classification results: This table shows three examples of
narrative segments, presenting the action and context (situation, intention, consequence) extracted through our
framework, along with the predicted action morality and human evaluation results for two settings (A and SICA). If
the prediction in each setting is moral, it is marked as M, and if it is immoral, it is marked as IM.
Music, the ratings tend to be lower.
5.3
A Case Study
Section 4.1 demonstrates the effectiveness of our
dataset and framework in predicting a character’s
morality, confirming that context enhances judg-
ment accuracy. Table 8 showcases three randomly
selected examples of human evaluations, compar-
ing our framework’s annotation results for two set-
tings: A (action only) and SICA (situation, inten-
tion, consequence, and action).
These examples show that annotations based
solely on actions (A) are often inaccurate and mis-
aligned with human judgments. In contrast, in-
cluding full context (SICA) consistently improves
prediction accuracy, demonstrating the significant
role of context in moral assessment.
6
Conclusion
In this paper, we introduced CharMoral, a novel
dataset designed to analyze the moral dynam-
ics of characters in long-form narratives. Using
a four-stage framework that leverages large lan-
guage models, we annotated character actions and
their morality, considering contextual information
such as situation, intention, and consequence. Our
experiments show that including context signifi-
cantly improves the accuracy of moral predictions,
aligning more closely with human judgments.
We further demonstrate that morally dynamic
characters, particularly main characters, play a key
role in increasing story engagement and ratings,
particularly in genres where moral dilemmas are
central, such as Western, War, and Film-Noir.
7
Limitation
Although our ultimate goal is to develop a method
that objectively assesses the morality of character
actions based on story context, moral concepts are
often shaped by cultural, social, and personal be-
liefs. As a result, biases inherent in the LLMs used
by our framework can affect assessments.
In future work, we aim to refine the framework
by accounting for cultural and individual differ-
ences in moral perspectives and to expand the
dataset to include a broader range of narrative
forms. These efforts will further enhance our un-
derstanding of character morality and its impact
on narrative engagement.
8
Ethic Consideration
We believe our research contributes ethically to
the fields of NLP and storytelling without causing
harm. To maintain ethical standards during the hu-
man evaluation phase, our study was reviewed and
approved by our institution’s Institutional Review
Board (IRB). We collected participant responses
without gathering any personally identifiable in-
formation. Before participation, individuals were
fully informed about the study’s objectives and
procedures, and we obtained their informed con-
sent.
Acknowledgments
This work was supported by Institute of Infor-
mation & communications Technology Planning
& Evaluation(IITP) grant funded by the Ko-
rea
government(MSIT)
(RS-2019-II190421,
Artificial
Intelligence
Graduate
School
Pro-

--- Page 9 ---

8817
gram(Sungkyunkwan
University))
and
the
National Research Foundation of Korea(NRF)
grant funded by the Korea government(MSIT)
(No. RS-2024-00357849).
References
Nader Akoury, Shufan Wang, Josh Whiting, Stephen
Hood, Nanyun Peng, and Mohit Iyyer. 2020. STO-
RIUM: A Dataset and Evaluation Platform for
Machine-in-the-Loop Story Generation. In Proceed-
ings of the 2020 Conference on Empirical Methods
in Natural Language Processing (EMNLP), pages
6470–6484, Online. Association for Computational
Linguistics.
David Bamman, Brendan O’Connor, and Noah A
Smith. 2013. Learning latent personas of film char-
acters. In Proceedings of the 51st Annual Meeting of
the Association for Computational Linguistics (Vol-
ume 1: Long Papers), pages 352–361.
Gordon H. Bower and Daniel G. Morrow. 1990. Men-
tal models in narrative comprehension.
Science,
247(4938):44–48.
Faeze Brahman, Meng Huang, Oyvind Tafjord, Chao
Zhao, Mrinmaya Sachan, and Snigdha Chaturvedi.
2021. "let your characters tell their story": A dataset
for character-centric narrative understanding.
In
Conference on Empirical Methods in Natural Lan-
guage Processing.
Mingda Chen and Kevin Gimpel. 2021. Tvstorygen: A
dataset for generating stories with character descrip-
tions. arXiv preprint arXiv:2109.08833.
Yu-Hsin Chen and Jinho D. Choi. 2016.
Character
identification on multiparty conversation: Identify-
ing mentions of characters in TV shows. In Proceed-
ings of the 17th Annual Meeting of the Special In-
terest Group on Discourse and Dialogue, pages 90–
100, Los Angeles. Association for Computational
Linguistics.
Jacob Cohen. 1960.
A coefficient of agreement for
nominal scales.
Educational and Psychological
Measurement, 20(1):37–46.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019.
BERT: Pre-training of
deep bidirectional transformers for language under-
standing.
In Proceedings of the 2019 Conference
of the North American Chapter of the Association
for Computational Linguistics: Human Language
Technologies, Volume 1 (Long and Short Papers),
pages 4171–4186, Minneapolis, Minnesota. Associ-
ation for Computational Linguistics.
Denis Emelin, Ronan Le Bras, Jena D. Hwang,
Maxwell Forbes, and Yejin Choi. 2021. Moral sto-
ries: Situated reasoning about norms, intents, ac-
tions, and their consequences.
In Proceedings of
the 2021 Conference on Empirical Methods in Nat-
ural Language Processing, pages 698–718, Online
and Punta Cana, Dominican Republic. Association
for Computational Linguistics.
Daniil Fischer, Frankand Skorinkin. 2021. Social Net-
work Analysis in Russian Literary Studies, pages
517–536. Springer International Publishing, Cham.
Maxwell Forbes, Jena D. Hwang, Vered Shwartz,
Maarten Sap, and Yejin Choi. 2020. Social chem-
istry 101: Learning to reason about social and moral
norms. In Proceedings of the 2020 Conference on
Empirical Methods in Natural Language Processing
(EMNLP), pages 653–670, Online. Association for
Computational Linguistics.
Bernard Gert and Joshua Gert. 2020. The definition
of morality. In Edward N. Zalta, editor, The Stan-
ford Encyclopedia of Philosophy, fall 2020 edition.
Metaphysics Research Lab, Stanford University.
Dan Hendrycks, Collin Burns, Steven Basart, Andrew
Critch, Jerry Li, Dawn Song, and Jacob Steinhardt.
2021. Aligning {ai} with shared human values. In
International Conference on Learning Representa-
tions.
Liwei Jiang, Jena D. Hwang, Chandra Bhagavatula, Ro-
nan Le Bras, Jenny Liang, Jesse Dodge, Keisuke
Sakaguchi, Maxwell Forbes, Jon Borchardt, Saadia
Gabriel, Yulia Tsvetkov, Oren Etzioni, Maarten Sap,
Regina Rini, and Yejin Choi. 2022. Can machines
learn morality? the delphi experiment.
Preprint,
arXiv:2110.07574.
Eunchong Kim, Taewoo Yoo, Gunhee Cho, Suyoung
Bae, and Yun-Gyung Cheong. 2022.
The Cre-
ativeSumm 2022 shared task: A two-stage summa-
rization model using scene attributes. In Proceed-
ings of The Workshop on Automatic Summarization
for Creative Writing, pages 51–56, Gyeongju, Re-
public of Korea. Association for Computational Lin-
guistics.
Hannah Kim, Denys Katerenchuk, Daniel Billet, Jun
Huan, Haesun Park, and Boyang Li. 2019. Under-
standing actors and evaluating personae with gaus-
sian embeddings. In Proceedings of the AAAI Con-
ference on Artificial Intelligence, volume 33, pages
6570–6577.
O-Joun Lee and Jason J. Jung. 2019. Modeling affec-
tive character network for story analytics.
Future
Generation Computer Systems, 92:458–478.
Nicholas Lourie, Ronan Le Bras, and Yejin Choi. 2020.
Scruples: A corpus of community ethical judgments
on 32,000 real-life anecdotes. arXiv e-prints.
Christopher Manning, Mihai Surdeanu, John Bauer,
Jenny Finkel, Steven Bethard, and David McClosky.
2014. The Stanford CoreNLP natural language pro-
cessing toolkit.
In Proceedings of 52nd Annual

--- Page 10 ---

8818
Meeting of the Association for Computational Lin-
guistics: System Demonstrations, pages 55–60, Bal-
timore, Maryland. Association for Computational
Linguistics.
Keith Oatley. 2008. The mind’s flight simulator. The
Psychologist, 21:1030–1032.
OpenAI. 2023.
Gpt-4.
https://openai.com/
research/gpt-4.
Valentina Pyatkin, Jena D Hwang, Vivek Srikumar,
Ximing Lu, Liwei Jiang, Yejin Choi, and Chan-
dra Bhagavatula. 2022.
Clarifydelphi: Reinforced
clarification questions with defeasibility rewards
for social and moral situations.
arXiv preprint
arXiv:2212.10409.
Stuart J. (Stuart Jonathan) Russell. 2019. Human com-
patible : artificial intelligence and the problem of
control. Viking, New York.
Yisi Sang, Xiangyang Mou, Mo Yu, Dakuo Wang, Jing
Li, and Jeffrey Stanton. 2022. MBTI personality pre-
diction for fictional characters using movie scripts.
In Findings of the Association for Computational
Linguistics: EMNLP 2022, pages 6715–6724, Abu
Dhabi, United Arab Emirates. Association for Com-
putational Linguistics.
YURI Y. TARASEVICH, ANNA V. DANILOVA, and
OLGA E. ROMANOVSKAYA. 2023.
Network
analysis of verbal communications in the novel the
master and margarita by m. a. bulgakov. Advances
in Complex Systems, 26(01).
Yotam Wolf, Noam Wies, Yoav Levine, and Amnon
Shashua. 2023.
Fundamental limitations of align-
ment in large language models.
arXiv preprint
arXiv:2304.11082.
Mo Yu, JiangNan Li, Shunyu Yao, Wenjie Pang, Xi-
aochen Zhou, Zhou Xiao, Fandong Meng, and Jie
Zhou. 2023.
Personality understanding of fic-
tional characters during book reading.
ArXiv,
abs/2305.10156.
Mo Yu, Yisi Sang, Kangsheng Pu, Zekai Wei, Han
Wang, Jing Li, Yue Yu, and Jie Zhou. 2022. Few-
shot character understanding in movies as an assess-
ment to meta-learning of theory-of-mind.
ArXiv,
abs/2211.04684.

```
