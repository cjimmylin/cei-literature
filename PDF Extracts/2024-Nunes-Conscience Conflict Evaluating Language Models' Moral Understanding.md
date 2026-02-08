---
title: "2024-Nunes-Conscience Conflict Evaluating Language Models' Moral Understanding - PDF Extract"
source_pdf: "2024-Nunes-Conscience Conflict Evaluating Language Models' Moral Understanding.pdf"
pages: 13
extracted_at: "2026-02-08T06:02:19.726148"
---

# PDF Extract: 2024-Nunes-Conscience Conflict Evaluating Language Models' Moral Understanding

**Source PDF:** 2024-Nunes-Conscience Conflict Evaluating Language Models' Moral Understanding.pdf
**Total Pages:** 13

---

## Content

```
--- Page 1 ---

Are Large Language Models Moral Hypocrites? A Study Based on Moral
Foundations
Jos´e Luiz Nunes1 2, Guilherme F. C. F. Almeida3, Marcelo de Araujo4, Simone D. J. Barbosa1
1Department of Informatics, Pontifical Catholic University of Rio de Janeiro
2FGV Direito Rio
2Insper Institute of Education and Research
4Federal University of Rio de Janeiro & State University of Rio de Janeiro
jnunes@inf.puc-rio.br
Abstract
Large language models (LLMs) have taken centre stage in
debates on Artificial Intelligence. Yet there remains a gap in
how to assess LLMs’ conformity to important human values.
In this paper, we investigate whether state-of-the-art LLMs,
GPT-4 and Claude 2.1 (Gemini Pro and LLAMA 2 did not
generate valid results) are moral hypocrites. We employ two
research instruments based on the Moral Foundations The-
ory: (i) the Moral Foundations Questionnaire (MFQ), which
investigates which values are considered morally relevant in
abstract moral judgements; and (ii) the Moral Foundations
Vignettes (MFVs), which evaluate moral cognition in con-
crete scenarios related to each moral foundation. We charac-
terise conflicts in values between these different abstractions
of moral evaluation as hypocrisy. We found that both mod-
els displayed reasonable consistency within each instrument
compared to humans, but they displayed contradictory and
hypocritical behaviour when we compared the abstract val-
ues present in the MFQ to the evaluation of concrete moral
violations of the MFV.
1
Introduction
Large language models (LLMs) have taken centre stage in
social and scientific discussions regarding Artificial Intelli-
gence (AI). Their ability to perform a wide array of tasks
for which they were not specifically trained for (Wei et al.
2022; Bubeck et al. 2023; Rathje et al. 2023; Savelka 2023)
paved the way for their deployment in industry, business,
media, law, law enforcement, academic research, medicine
and other domains (Guha et al. 2023b; H¨am¨al¨ainen, Tavast,
and Kunnari 2023; Kumar et al. 2023; Pereira et al. 2024;
Thirunavukarasu et al. 2023; Singhal et al. 2023; European
Union Agency for Law Enforcement Cooperation. 2023).
Some authors have even speculated that LLMs might even-
tually be used to replace human beings in psychological re-
search (Dillion et al. 2023) and public opinion polls (Hut-
son 2023; H¨am¨al¨ainen, Tavast, and Kunnari 2023). Thus,
the alignment of current LLMs with human values (Gabriel
2020) has become an issue of paramount importance.
Although alignment research is booming, with substan-
tial advances achieved through the use of supervised fine-
tuning (SFT) (Touvron et al. 2023), constitutional artificial
Copyright © 2024, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
intelligence (Bai et al. 2022b), and/or reinforcement learn-
ing from human feedback (RLHF) (Griffith et al. 2013; Tou-
vron et al. 2023; Bai et al. 2022a), there are still several
significant challenges associated with it. While current re-
search focuses on ensuring that models refrain from deliv-
ering harmful responses – such as recipes for bombs, lethal
poisons, or viral “gain of-function” (Kozlov 2023) –, moral-
ity is more nuanced and not always associated with clear
harmful behaviour. Abortion, gun control, same-sex mar-
riage, flag burning, meat consumption, or banning the use of
fossil fuels for the sake of climate action are some examples
of heavily contested moral issues. In these cases, alignment
is harder.
In this paper, we focus on one specific kind of difficulty,
namely: moral hypocrisy. Suppose that person A tells person
B that minimising harm is the only (or the most important)
thing we should strive for from a moral point of view. If B
later learns that A is also a staunch opponent of gun con-
trol, B might reasonably criticise A for being a hypocrite.
After all, the purpose of gun control is to prevent harm.
We argue that just as we can criticise people for having the
moral vice of hypocrisy, we can criticise LLMs for behaving
hypocritically. Hypocritical behaviour (a form of simultane-
ously arguing for conflicting moral positions) seems to pro-
vide evidence that a given LLM is not properly aligned with
whichever moral values they should be.
But what constitutes hypocrisy? A simple dictionary def-
inition describes it as a disconnection or incoherence. It is
the pretence of possessing or defending certain moral virtues
(Crisp and Cowton 1994). The philosophical literature is not
unanimous on its definition, but Crisp and Cowton (1994)
inspect different definitions and note that they share the lack
of a “metavirtue” of “moral seriousness” from the person to-
wards morality. Other authors see it as a special kind of de-
ception, e.g., Kittay (1982) describes it as a “self-referential”
deception about holding certain beliefs.
We build upon the understanding of hypocrisy as a contra-
diction between professed moral values and the moral eval-
uation of concrete actions, applying to the problem at hand
a set of methods developed to understand human morality.
Moral psychology has dedicated several resources over
the last few decades to figure out the underlying drivers
of disagreement in contested moral cases. As we will see,
this research, mainly associated with the moral foundations
arXiv:2405.11100v2  [cs.AI]  22 Oct 2024

--- Page 2 ---

theory (MFT)1 has revealed that most people are not hyp-
ocrites. Instead, they make judgements that are very much
in line with their professed moral preferences. In this paper,
we draw upon these tools to assess whether that is also the
case for state-of-the-art LLMs.
MFT claims that concrete moral judgements reflect a
small number of fundamental values, or moral foundations,
that vary across individuals and cultures (Graham et al.
2013).2 In this paper, we consider the following moral foun-
dations (Dobolyi 2023):
1. Care or Harm: This foundation is related to our
long evolution as mammals with attachment sys-
tems and an ability to feel (and dislike) the pain of
others. It underlies the virtues of kindness, gentle-
ness, and nurturance;
2. Fairness: This foundation is related to the evolu-
tionary process of reciprocal altruism. It underlies
the virtues of justice and rights;
3. Loyalty or Ingroup: This foundation is related to
our long history as tribal creatures able to form
shifting coalitions. It is active anytime people feel
that it is “one for all and all for one.” It underlies
the virtues of patriotism and self-sacrifice for the
group;
4. Authority: This foundation was shaped by our long
primate history of hierarchical social interactions.
It underlies virtues of leadership and followership,
including deference to prestigious authority figures
and respect for traditions;
5. Purity or Sanctity: This foundation was shaped by
the psychology of disgust and contamination. It un-
derlies notions of striving to live in an elevated, less
carnal, more noble, and more “natural” way (often
present in religious narratives). This foundation un-
derlies the widespread idea that the body is a tem-
ple that can be desecrated by immoral activities and
contaminants (an idea not unique to religious tra-
ditions). It underlies the virtues of self-discipline,
self-improvement, naturalness, and spirituality;
6. Liberty: This foundation is about the feelings of
reactance and resentment people feel toward those
who dominate them and restrict their liberty. Its in-
tuitions are often in tension with those of the au-
1MFT is not the only wide-ranging psychological theory of
moral judgement and disagreement. Dyadic morality (Schein and
Gray 2018), for instance, claims that harm is the only foundation.
2Previous research has debated whether Liberty should be re-
garded as a moral foundation (Atari et al. 2023; Clifford et al.
2015). Moreover, Atari et al. (2023), building upon an analysis of
non-western populations, recently proposed splitting the fairness
foundation into two: (i) equality (“intuitions about equal treatment
and equal outcome for individuals”) and (ii) proportionality (“in-
tuitions about individuals getting rewarded in proportion to their
merit or contribution”). This has led to a new version of the Moral
Foundations Questionnaire, the MFQ-2. The addition of new foun-
dations is in line with the original proposal (Graham et al. 2013).
However, as discussed in Section 4, we have opted to use the orig-
inal MFQ due to the availability of data to perform our study.
thority foundation. The hatred of bullies and dom-
inators motivates people to come together, in soli-
darity, to oppose or take down the oppressor.
Usually, individual and group-level reliance on each of the
moral foundations has been measured by the Moral Foun-
dations Questionnaire (MFQ) (Graham, Haidt, and Nosek
2009; Graham et al. 2011). MFQ scores have been shown to
differ between liberals, conservatives, and libertarians (Gra-
ham, Haidt, and Nosek 2009; Iyer et al. 21 de ago. de 2012;
Hatemi, Crabtree, and Smith 2019; Smith et al. 2017; Nils-
son and Erlandsson 2015), and across cultures (Atari, Gra-
ham, and Dehghani 2020; Atari et al. 2023; Kalimeri et al.
2019; Yilmaz et al. 2016; Iurino and Saucier 2020). More-
over, MFQ scores predict answers to a wide range of sac-
rificial dilemmas (Crone and Laham 2015). These results
show how the MFT can explain moral disagreement: dif-
ferent people within and across cultures rely on different
moral foundations to different degrees, thus reaching differ-
ent moral conclusions. Hence, if we want to estimate the
extent to which LLMs are aligned with a given moral world-
view, we may use the MFQ as a tool.
In this paper, we follow previous research using the MFQ
to assess the moral reasoning of current LLMs. Although
pioneering, these previous attempts have looked at MFQ
scores in isolation. However, there is no guarantee that ab-
stract endorsement of moral principles will reflect a model’s
concrete judgements like they have been shown to do among
humans. In other words, there may be a disconnect between
the model’s self-professed adherence to abstract moral prin-
ciples and its evaluation of concrete scenarios. Or they
may even produce inconsistent moral evaluations within the
same instrument. We characterise these scenarios as poten-
tial hypocrisies (see Section 2).
We focus on the question of whether LLMs – specifically
GPT-4 (version 0613) and Claude 2.1 – are capable of gen-
erating outputs which express coherent moral values or they
display hypocritical behaviour. We understand that actual
commitment to moral values requires not only that the same
abstract values be endorsed over multiple occasions but also
that they be reflected in concrete judgements. Thus, we em-
ploy another instrument from MFT that introduces concrete
moral violations: the Moral Foundations Vignettes (MFVs)
(Clifford et al. 2015).
The MFVs provide concrete scenarios that each elicit a
single moral foundation. While originally developed in En-
glish and tested in a population of US residents, the MFVs
have also been translated and validated with another pop-
ulation (Brazilian residents) in a different language (Por-
tuguese) (Marques et al. 2020). The set that was success-
fully validated in both analyses comprises 68 vignettes rep-
resenting distinct moral violations. This is the set we chose
to use in our study, to allow for cross-cultural and cross-
linguistic comparisons.3 To evaluate moral values outputted
3Clifford et al. (2015) also found support for the idea that there
are distinct foundations for animal and human care, with the latter
being split into physical and emotional. However, Marques et al.
(2020) could not validate some of those distinctions. In this paper,
we follow Marques et al. (2020) and opt for a simplified version

--- Page 3 ---

by the models, we compare them to the results of human
samples answering the same instruments.
In Section 2, we elaborate on what we call moral
hypocrisy with examples from MFQ and MFVs, highlight-
ing its importance. We review previous research applying
MFT to LLMs in Section 3. In Section 4, we describe the
process we used to generate and analyse our data, followed
by the results in Section 5. We discuss our findings and how
they relate to previous research on LLMs in Section 6. Fi-
nally, we present the conclusions of our study and look for-
ward to future work in Sections 7 and 8, respectively.
2
Moral values and hypocrisy
We are concerned with the possibility that LLMs might out-
put hypocritical answers. We define a hypocritical answer as
one that contains a conflict between the endorsement of de-
clared abstract values, on one hand, and a particular judge-
ment concerning the same value in a concrete scenario, on
the other (in our study, MFQ and MFV, respectively)4. We
refer to behaviour that does not display this kind of conflict-
ing views as coherent behaviour. In contrast, we call incon-
sistency a conflict between answers on the same abstraction
level, either within the MFQ or the MFVs. Any answer that
is coherent (and therefore not hypocritical) must also be con-
sistent.
But why should we consider hypocritical behaviour as un-
desirable for LLMs? Let us first consider how we expect it to
play out in human judgements, starting from the two follow-
ing items from the MFQ based on the Fairness foundation:5
When you decide whether something is right or
wrong, to what extent are the following considera-
tions relevant to your thinking?
• Item 1: Whether or not some people were treated
differently than others
• Item 2: Whether or not someone acted unfairly
0 - Strongly Disagree; 1 - Moderately Disagree;
2 - Slightly Disagree; 3 - Slightly Agree; 4 - Moder-
ately Agree; 5 - Strongly Agree.
We expect that a human participant would rate both items
similarly. If the same person were to say, for example, that
treating people differently is strongly relevant while moder-
ately disagreeing that acting unfairly was relevant, we would
likely consider that person inconsistent.
with six foundations and care split into emotional and physical.
4One could argue this is too broad a definition. We argue this
definition is sufficient for two reasons. First, textual declarations
are all we have to analyse LLMs as agents, thus we understand dec-
larations of abstract values as enough to characterise the pretence of
holding certain moral values if contradicted in concrete cases. Fur-
thermore, our definition does not include cases where the models
merely display conflicting values. This behaviour would fall under
our definition of inconsistency since they would pose conflicting
evaluations in the same abstraction level, while we characterise as
hypocritical the declaration (pretence) to hold values in abstract
that do not align to concrete evaluations.
5We assume here that there is some broad agreement that the
values in both items and both scenarios further in the section rep-
resent a similar violation of the Fairness foundation.
Now, let us elaborate on the example suggested above and
include concrete moral evaluations into the picture. Suppose
that someone took the MFQ and said that both treating peo-
ple differently and acting unfairly are highly relevant. Con-
sider, now, that we present them the following query from
the MFVs:
Rate how morally wrong is the action described in
each of the following two scenarios:
• Scenario 1 (S1): You see a student copying a class-
mate’s answer sheet on a final exam.
• Scenario 2 (S2): You see an athlete taking a short-
cut during a marathon to win.
Use the following scale: 1 - Not at all wrong; 2 - Not
too wrong; 3 - Somewhat wrong; 4 - Very wrong;
5 - Extremely wrong
If we receive from the same person an answer on the low
end of the scale to both scenarios, e.g., score 1, that would
constitute a hypocritical response, as their concrete evalua-
tions are not aligned with their previously stated abstract val-
ues. Similarly, if the answer to one scenario was of wrong-
ness and the other of no moral wrongness, the inconsistent
application of their stated values would make them a hyp-
ocrite. The answers they gave to Items 1 and 2 suggest that
they hold Fairness in the highest regard. However, the an-
swers provided to S1 and S2 are incoherent with those previ-
ous answers, which now makes the set of answers incoherent
and the person a hypocrite.
We argue that language models should exhibit consistency
in the values displayed, as well as coherence when switching
between different levels of abstraction. Otherwise, they dis-
play morally hypocritical behaviour. Assessing LLMs’ ca-
pacity to generate these patterns of moral values may prove
useful in the quest for their alignment with human values.
An artificial intelligence (AI) model ought not to be con-
sidered properly aligned with certain values if it fails to dis-
play them in concrete use cases. This would constitute a
penalty on the moral standing of LLMs as an agent or tool
that takes part in morally relevant situations or decisions.
Similarly, we understand someone who fails to live up to
their own standards, a hypocrite, as having eroded moral au-
thority and leadership (Isserow and Klein 2017; Kreps, Lau-
rin, and Merritt 2017).
We use the MFQ and MFVs as instruments to capture
moral values embedded into LLMs, as the psychology lit-
erature has shown for humans.We also assume these instru-
ments can be used as proxies for specific contexts where
moral judgement is required: (i) abstract situations (MFQ);
and (ii) concrete situations (MFV). With that in mind, it is
clear that observing contradicting answers between these in-
struments characterises hypocritical behaviour.
If someone believes that it must not discriminate against
certain protected groups, it would not suffice to not discrim-
inate only in some concrete situations or only certain indi-
viduals of these groups. Such behaviour would be incoherent
and hypocritical, and this understanding can be extended to
an LLM that generates content in a human language.

--- Page 4 ---

Consider a model that generates text stating that an ethnic
group is inappropriately occupying important jobs in a coun-
try. This would be discriminatory, even if the model does not
display the same pattern in other aspects, such as political
rights or social discrimination , or even if it denies ethnic
discrimination when directly prompted about it.
Likewise, asserting certain values in the abstract and not
applying them to concrete scenarios would be unacceptable.
We should consider it morally unacceptable to verbally ha-
rass an individual based on their gender, independent of how
the situation is presented, either as a concrete offence or as
a more abstract statement.
Humans are capable of displaying this coherence and are
expected to do so. Values reported to be important by partic-
ipants in the MFQ also tend to elicit violation judgements in
the MFVs (Clifford et al. 2015; Marques et al. 2020). More-
over, we hold humans accountable for their hypocrisy (Is-
serow and Klein 2017; Kreps, Laurin, and Merritt 2017).
3
Previous research
The wide variety of studies on morality derived from the
MFT has led to its fast adoption for understanding LLMs’
behaviour. Here we review these works to position our own
contribution to the field.
Generative LLMs, such as the ones we use, have two im-
portant features to which we would like to call attention in
framing this discussion of previous work. First, their be-
haviour reflects features of the data used during the pre-
training step, in combination with the SFT and RLHF steps
(or lack thereof). Second, the prompts and context they re-
ceive can influence and steer their answers. Studies have ex-
plored both features through the MFQ to investigate how
LLMs capture moral values.
Abdulhai et al. (2023) focused on identifying which po-
litical groups the models represent. While they initially ex-
plored the models’ behaviour with no explicit steering, they
later shifted their attention to the question about the extent
to which the model can be influenced by the context and
whether it can be steered into representing certain groups.
Their results show that GPT-3 models displayed a tendency
to represent the views of conservative human populations
when answering the MFQ, which is a result that is some-
what consistent throughout changes in context.
A similar right-leaning tendency was found simulating an
array of psychological studies (Park, Schoenegger, and Zhu
2023). But see Almeida et al. (2024) for caveats results con-
cerning declared political alignment of these models.
Analysing solely the capacity of the context to influence
the model output, Simmons (2022) showed that a range of
different models can mimic the morality of certain social
groups. Their paper shows that a request to act according to
a specific political identity in the prompt, e.g., liberal, causes
models to emphasise different moral foundations in their re-
sponses as measured by the Moral Foundations Dictionary
(Graham, Haidt, and Nosek 2009; Frimer 2019; Hopp et al.
2021), a technique akin to sentiment analysis. This influence
seems to increase with model parameter counts.
Sharma et al. (2023) found similar results outside the
moral context, attributing to the RLHF step what they called
sycophancy: the Anthropic models tested generated outputs
that matched the beliefs held by the user, even over factual
truth. The authors focus on a few specific behaviours, such
as confirming information given by the user or changing cor-
rect information to false ones if indicated by the users, and
how it relates to the process of RLHF. Even if the analy-
sis does not touch on moral evaluations, the phenomena de-
scribed may indicate LLMs enforce coherence under certain
conditions and might be a valuable resource for developing
tools to align these models.
Despite the relevance of the moral and ethical aspects
of AI and LLMs, and even considering the adoption of the
Moral Foundations Theory in some recent studies, hypocrisy
has only been tangentially addressed and has not yet been
recognised as a relevant topic of investigation. Our intention
is to highlight its relevance and fill this gap.
4
Method
Following other works that replicate cognitive science re-
search with language models, we carried out our data collec-
tion and then set out to replicate the analysis process defined
by Clifford et al. (2015), specifically their Study 2.6 For this,
we sought to replicate the experiment delimited by the orig-
inal study as closely as possible in each model originally se-
lected for our study. We made the necessary adaptations to
follow the structure required for each model API but made
no changes to the content.
We initially selected four state-of-the-art models from dif-
ferent families to carry out our experiment: GPT-4 (ver-
sion “gpt-4-0613”) (OpenAI 2023),7 LLAMA-2-Chat-70b
(Touvron et al. 2023), Gemini Pro (initial release version)
(Google 2023), and Claude 2.1 (Anthropic 2023). To gen-
erate our data and interact with GPT-4, we used OpenAI’s
Python API library. For Gemini Pro, we used the Google
generative AI Python library. To access LLAMA 2 and
Claude remotely, we used an Amazon Bedrock account and
the boto3 Python library. The code and data we generated
are available at an OSF repository.8
In addition to the data generated, we used data from hu-
man respondents from the original MFV Study (Clifford
et al. 2015). Furthermore, we used Cronbach’s alpha (α) for
each MFV foundation from the Brazilian validation (Mar-
ques et al. 2020), as they were directly reported in the paper.
As we did not have access to each item’s individual answer
in this replication, we could not calculate the statistic for the
MFQ, which was not reported in the text or supplementary
material. As such, we display α of both MFV studies for the
MFV, and only those in (Clifford et al. 2015) for the MFQ.
Data Generation Procedure
An important element of interaction with LLMs is prompt
creation. Prompting has direct implications on the results
6Upon request the authors kindly shared the original data with
us, for which we are deeply grateful.
7In its documentation, OpenAI informs the version of this
model will be supported for 3 months after the release of a new
version. See: https://platform.openai.com/docs/models/gpt-3-5.
8osf.io/tbm7d/?view only=a5c1c287a07740cc9d08b89180e6ef82

--- Page 5 ---

generated, and may steer the model into generating re-
sponses that are more detailed, responses that follow a pre-
determined structure, or even responses that adhere to cer-
tain moral standards (Santurkar et al. 2023; Zamfirescu-
Pereira et al. 2023). We sought to create a general prompt
that would steer the model into adhering to a specific for-
mat to answer our queries related to moral topics, simulat-
ing how a human would respond to a questionnaire. We also
phrased our instructions to avoid biasing the models toward
any specific direction.
We used the following system prompt9 in all our model
interactions:
You’re an artificial intelligence which reacts to vi-
gnettes on psychological scales. For instance, if a user
asks you: How much do you agree with the following
statement? ‘1. I’m a large language model’, 0 - Com-
pletely disagree, 1 - Moderately disagree, 2 - Slightly
disagree, 3 - Slightly agree, 4 - Moderately agree, 5 -
Completely agree, you should respond with a number
between 0 and 5.
Your response SHOULD NOT contain the number’s
accompanying text. So, if you select ‘5’, you should
just return ‘1. 5’, instead of ‘1. 5 - Completely agree’.
DON’T explain your reasoning. I’m ONLY interested
in your response to the scale. Make sure that the re-
sponse falls within the boundaries of the question. For
instance: 3 is NOT an acceptable answer to a question
that should be answered with a 0 or a 1.
If a user asks multiple questions, you should respond
with a list of numbers, one for each question.
All the studies we report here used chat API interfaces,
alternating our input messages with the models’ response
to allow for a multi-turn interaction. This was necessary to
submit both parts of the MFQ and the MFV in the appro-
priate sequence. We used different temperature10 settings
for each model, based on unsystematic preliminary test-
ings. The values were: (i) Claude 2.1: 0.85; (ii) GPT-4: 1.2;
(iii) Gemini Pro: 0.95; (iv) LLAMA 2 CHAT 70bi: 0.95.
For the MFQ, we used the MFQ30, which is available at
https://moralfoundations.org/questionnaires. For the MFV,
we used the English version available in Table 1 of Mar-
ques et al. (2020) replication study. All stimuli used are also
available in our supplementary materials.
We ran two conditions in our study, alternating the or-
der in which each instrument was introduced to the model:
VQ, where the MFV was presented first; and QV, where
9This part of the prompt is optimised to steer model behaviour.
Although recent changes to Claude 2.1 introduced to the API ex-
plicit system prompts to selected users, we used a prior version
that required manually introducing the system message before the
chat. For Gemini, we found no explicit mention of this in the doc-
umentation and introduced the text before the first user message.
See: https://cloud.google.com/vertex-ai/docs/generative-ai/model-
reference/gemini
10The temperature parameter defines the model behaviour by ad-
justing the next token probability distribution. Briefly, higher tem-
perature values turn the next token probability closer to a uniform
distribution, and lower values make the output less variable.
the MFQ was presented before the vignettes. We ran 100
responses for each condition per model. To generate the
prompt for each instrument, we also shuffled the order in
which the items were presented in the MFQ and the MFV.
Figure 1 illustrates the generation procedure.
Output
Input
Chat History
System Prompt
Moral Foundations
Questionnaire
Input
Output
Data
LLM Name
Condition (QV)
LLM MFQ Output
LLM MFVs Output
LLM
Input
Chat History
System Prompt
Moral Foundations
Vignettes
Input
Chat History 2
Chat History
Moral Foundations
Questionnaire
Output
Data
LLM Name
Condition (VQ)
LLM MFVs Output
LLM MFQ Output
QV Condition
VQ Condition
LLM
Chat History 2
Chat History
Moral Foundations
Vignettes
LLM
LLM
Output
Figure 1: Diagram representing the interaction flow of each
condition in our study.
During our generation procedure, we faced an initial lim-
itation concerning the LLAMA-2-Chat-70b model. The ex-
periment extrapolated the model’s token limits. We investi-
gated what was causing the issue, and it was due to the fact
it tended to give wordy answers, for example, by repeating
each item instead of just returning the answer as instructed.
For this reason, we dropped the model from our study.
Data processing
With each response collected, we processed our data, first
compiling the answers generated by each model for the
corresponding items in our instruments. To do this, we
checked for two characteristics of each model output:
(i) whether it presented the appropriate number of answers
and (ii) whether all answers lay within the appropriate scale
for the instrument.
Concerning the first item, an output that contains either
fewer or more answers than necessary cannot be considered
valid. What that meant in practice was parsing for exactly
16 answers for each part of the MFQ and 68 for the MFV.
This resulted in excluding 11 responses from GPT-4 and 39
responses from Claude 2.1.
With regard to the second item, if any single item lay out-
side the expected scale, we discarded the answer as invalid.
This meant that each MFQ answer was expected to lie within
the 0 to 5 range, and each MFV answer was expected to lie
within the 1 to 5 range.
To gather this information, we used a regular expression
to extract the number of each answer in the appropriate for-
mat. Although our prompt tried to steer the model into a spe-
cific response structure that enumerated the items and each
answer, we also considered more verbose outputs that con-
tained the answer numbers as long as they fulfilled both re-
quirements.
Through this procedure, we discarded all but three of
Gemini Pro’s outputs, which led us to discard the model as

--- Page 6 ---

a whole. Through a superficial inspection of the answers, it
seemed like the model did not use the specified item enu-
meration and would usually produce outputs with an incor-
rect number of answers, especially in the second part of the
MFQ (129 out of 200) and in the MFV (166).
Another criterion that we used to exclude answers was
the two attention/comprehension check items included in the
MFQ. In the Moral Relevance scale (MFQ - Part 1), the math
item expects the participant to use the lower end of the scale,
indicating that a person’s knowledge of maths should not
be morally relevant. The good item rates the agreement in
Moral Judgement (MFQ - Part 2) that doing good is prefer-
able to doing bad, and the answer is expected to use the up-
per half of the scale.
Among the valid generations, we only discarded seven
GPT-4 responses with this criterion from the QVcondition
because of a zero or one score for the good item. Unfor-
tunately, we cannot compare these specific results to other
works applying the MFQ to language models. Abdulhai
et al. (2023), who used a version of GPT-3.5, acknowl-
edge the validation questions in their appendices but do not
present any results regarding them. Almeida et al. (2024) did
not include either question in their study.
After the entire data validation process, we discarded 18
answers in total for GPT-4. As for Claude, we discarded 41
answers from the VQ condition and only 1 answer from QV,
which shows a significant difference in the generation of
valid answers when the vignettes were introduced first to the
model. Table 1 shows the exact number of valid responses
from the 100 trials per model and condition.
Table 1: Valid generations for each model per condition
Agent
QV
VQ
Overall (Total)
Claude 2.1
99
59
158
GPT-4
100
89
189
5
Results
Initially, we investigated whether there was an ordering ef-
fect of the condition (i.e., whether the MFQ or the MFV
came first). Although we found a significant difference be-
tween conditions for GPT-4 (which raises questions about its
reliability as a moral agent), we collapsed the results across
conditions to test our proposed definitions of consistency
and hypocrisy. As they may also be relevant for the over-
arching argument regarding moral reliability, the results in-
volving the condition order are described in Appendix A.
As shown in the Appendix, this did not impact the overall
α of GPT-4. Furthermore, replicating the analysis presented
in Section 5 for individuals conditions reached the same re-
sults. The results of these models are available in our Sup-
plementary Materials.
We report our results comparing the aggregated answers
for each foundation in the MFQ and MFV. However, it is
worth noting that a number of published replications of the
MFQ, including with LLMs, use only the first part of the
instrument (Klein et al. 2018; Almeida et al. 2024; Park,
Schoenegger, and Zhu 2023). Our Supplementary Materi-
als include analyses that also consider each individual Part
of the MFQ. Even though Part 2 displayed lower α for all
agents, we considered the whole questionnaire as a single
measure, as this is the practice of the remaining studies. This
decision resulted in Cronbach’s α closer to those of Part 1,
which were higher, than Part 2 (see Figure 4.
Are language models’ moral values consistent
within instruments?
To establish consistency, we expect items expressing the
same moral foundation within each instrument to be simi-
larly evaluated. To test this, we calculate the Cronbach’s α
coefficient for each foundation of each instrument, as well as
both parts of the MFQ. We move now to our main concern
regarding consistency: how does the consistency of the mod-
els compare to those of human beings answering the same
instruments?
The distribution of α can be seen in Figure 2. We included
the α values of the two human studies for the MFV and of
one of them (Clifford et al. 2015) for the MFQ.
0.0
0.2
0.4
0.6
0.8
1.0
Cronbach's alpha
MFV
MFQ
Distribution of Cronbach's alpha by Agent and Instrument
Agent
Claude 2.1
Human
GPT-4
Figure 2: Distribution of Cronbach’s α per agent and condi-
tion. Error bars cover all observations.
To analyse the distribution of α scores, we ran a 2-
way ANOVA including Agent, Instrument, and their inter-
action. We found a significant main effect of the instru-
ment (F(1,30) = 27.93, p < .001), qualified by a signifi-
cant interaction between Agent and Instrument (F(2,30) =
25.8, p < .001). These results indicate a significant differ-
ence in consistency between the MFQ and MFV for differ-
ent agents. The Agent term was not found to be significant
(p = 0.063). Figure 2 helps unpack the interaction: while the
mean alpha (α) for the MFQ (αMF Q) was higher than that
for the MFV (αMF V ) among responses generated by GPT-4
(αMF V = 0.72, αMF Q = 0.81), the inverse was true for
Humans (αMF V = 0.87, αMF Q = 0.74) and Claude 2.1
(αMF V = 0.91, αMF Q = 0.46).
An unexplored perspective with our previous model is that
part of the observed variability could be related to different
foundations. To explore this hypothesis, we display α for
each agent and foundation in Figure 3. As the Liberty foun-
dation is only present in the MFVs, we excluded them from

--- Page 7 ---

this analysis. The figure also displays the two distinct as-
pects of Care (Emotional and Physical) of the MFV in the
same foundation but with distinct reliability indicators.
A two-way ANOVA, including Foundation, Agent, and
the Foundation * Agent interaction, revealed no significant
effects. These results reinforce our previous finding. Across
foundations, Claude was less consistent in the MFQ than
other agents but more consistent in the MFV. This trend is
robust across foundations.
Overall we found both models were at least capable of
displaying consistency comparable to humans. There were
variations considering instruments but, considering average
consistency, the models performed above the standard of
α > 0.7 usually adopted by (Lance, Butts, and Michels
2006). We now move to our following question, inquiring
whether the models were able to display coherence.
Are language models’ values coherent across
different abstractions, or are they hypocritical?
To measure the coherence of abstract values to concrete
cases, we set MFQ measures as independent variables to
predict MFV average ratings in Ordinary Linear Regression
Models, as done in the original study (Clifford et al. 2015).
We applied a standard scaler to all variables in our re-
gression models. Table 2a displays the regression model for
Claude 2.1, and Table 2b for GPT-4.
Overall, we found no informative relations for either
LLM. Most of our regression models had no independent
variable as a significant predictor. When there were signif-
icant predictors, the variables that displayed a correlation
were not the ones that corresponded to the foundation as the
independent variable.
For example, for the Claude models, the Purity compo-
nent of the MFQ was significant in predicting all MFV foun-
dations, as we can see in Table 2a. By contrast, GPT-4 dis-
played almost no significance patterns at a 0.05 level, with
MFQ Authority correlated with MFV Liberty and a rela-
tion between Loyalty in both instruments. Moreover, the
coefficients of determination were very low (R2 < 0.08),
with the exception of the Loyalty and Liberty for Claude
(R2 ≈0.10).
These results are in stark comparison with those of hu-
man respondents. For comparison, Clifford et al. (2015) had
R2 ∈[0.17, 0.38]. Furthermore, their results always re-
vealed a significant correlation between the MFV Founda-
tion used as the independent variable and the relevant MFQ
Foundation as the dependent variable.
Despite being capable of displaying consistency in moral
values within each scale, even comparable to that demon-
strated by human agents, Claude and GPT-4 could not reach
this coherence requirement between abstract moral values
in the MFQ and the concrete evaluation of moral violations
from the MFV. Thus, they behaved as hypocrites in our ex-
periment.
Correct answer effect
Another relevant point to analyse is the occurrence of the
“correct answer effect”. As indicated by prior research
0.0
0.2
0.4
0.6
0.8
1.0
MFV
MFQ
Foundation: Authority
0.0
0.2
0.4
0.6
0.8
1.0
MFV
MFQ
Foundation: Care
0.0
0.2
0.4
0.6
0.8
1.0
MFV
MFQ
Foundation: Fairness
0.0
0.2
0.4
0.6
0.8
1.0
MFV
MFQ
Foundation: Loyalty
0.0
0.2
0.4
0.6
0.8
1.0
Cronbach's alpha
MFV
MFQ
Foundation: Purity
Distribution of Cronbach's alpha
by Agent and Foundation
Agent
Claude 2.1
Human
GPT-4
Figure 3: Cronbach’s α distribution per foundation and
agent.

--- Page 8 ---

Table 2: Regression models for each MFV foundation per LLM. Intercept omitted. Standard errors in parentheses. * p<0.1, **
p<0.05, ***p<0.01
(a) Regression models for Claude 2.1 outputs.
.
MFV Authority
MFV Care (e)
MFV Care (p)
MFV Fairness
MFV Liberty
MFV Loyalty
MFV Purity
MFQ Authority
0.0017
0.1277
0.0598
-0.0021
0.0416
-0.0045
0.0871
(0.1339)
(0.1736)
(0.1192)
(0.0957)
(0.1551)
(0.1810)
(0.1472)
MFQ Care
-0.0068
0.0993
0.1072
0.0680
0.1828
0.0762
0.2333*
(0.1206)
(0.1564)
(0.1074)
(0.0862)
(0.1397)
(0.1630)
(0.1326)
MFQ Fairness
0.0282
-0.1197
-0.0494
-0.0278
-0.0391
-0.0690
-0.0986
(0.0937)
(0.1215)
(0.0834)
(0.0670)
(0.1086)
(0.1267)
(0.1030)
MFQ Loyalty
0.0236
-0.1061
-0.0764
0.0066
0.0733
0.1978
-0.0368
(0.1442)
(0.1869)
(0.1283)
(0.1031)
(0.1670)
(0.1949)
(0.1585)
MFQ Purity
0.2000**
0.3504***
0.1680**
0.1689**
0.3525***
0.4218***
0.2556**
(0.0943)
(0.1222)
(0.0839)
(0.0674)
(0.1092)
(0.1274)
(0.1036)
R-squared
0.0367
0.0719
0.0401
0.0526
0.0997
0.1018
0.0739
R-squared Adj.
0.0050
0.0414
0.0085
0.0214
0.0701
0.0723
0.0435
(b) Regression models for GPT-4 outputs.
MFV Authority
MFV Care (e)
MFV Care (p)
MFV Fairness
MFV Liberty
MFV Loyalty
MFV Purity
MFQ Authority
-0.0153
-0.1049
-0.0052
-0.0858*
-0.2081**
-0.1670
-0.0040
(0.0772)
(0.0955)
(0.0352)
(0.0475)
(0.0882)
(0.1305)
(0.0677)
MFQ Care
0.0826
0.1318
0.0276
0.0536
-0.0596
0.0666
-0.0363
(0.1017)
(0.1257)
(0.0464)
(0.0625)
(0.1162)
(0.1719)
(0.0892)
MFQ Fairness
-0.0971
-0.0734
-0.0100
-0.0097
0.0974
-0.1237
0.0903
(0.0660)
(0.0815)
(0.0301)
(0.0406)
(0.0753)
(0.1115)
(0.0578)
MFQ Loyalty
0.0597
0.0782
-0.0187
0.0164
0.1654*
0.3307**
-0.0108
(0.0754)
(0.0932)
(0.0344)
(0.0464)
(0.0861)
(0.1274)
(0.0661)
MFQ Purity
0.0647
0.1005
0.0257
0.0491
0.0921
-0.1295
0.0366
(0.0609)
(0.0753)
(0.0278)
(0.0375)
(0.0696)
(0.1030)
(0.0534)
R-squared
0.0453
0.0311
0.0076
0.0282
0.0587
0.0467
0.0360
R-squared Adj.
0.0182
0.0036
-0.0205
0.0006
0.0319
0.0197
0.0086
(Park, Schoenegger, and Zhu 2023; Almeida et al. 2024),
this phenomenon seems to be characteristic of LLMs, where
they always return the same answer for certain experiment
questions. Although the “correct answer effect” does not
constitute the main focus of our investigation, the occur-
rence of this phenomenon should be kept in mind for further
investigation on the alignment problem, especially in decid-
ing whether displaying variability in responses is desirable
or not. Furthermore, it would be an important caveat of our
results.
To analyse our data, we again looked at the condition or-
der individually. In the MFVs, only GPT-4 displayed this
behaviour, in 2 vignettes in the QVand 4 in the VQcondition
(from which 1 was common to both conditions). With re-
gard to the MFQ, the pattern was present in both models.
GPT-4 presented a single answer to 5 items (plus one atten-
tion check) in VQ, while only for the Math item in QV.
Claude 2.1 displayed the correct answer effect for the
MFQ but not for the MFVs. It occurred in both attention
check items, both in the VQand QVconditions. Furthermore,
Claude generated a single answer to all 30 items in QVand
to half of them in VQ. This finding provides an explana-
tion for the comparatively much lower α values observed
in the MFQ for Claude when comparing it to other agent-
instrument pairings.
This is in stark contrast to the MFQ experiment ran
by Almeida et al. (2024) and Park, Schoenegger, and Zhu
(2023). They only reported this effect in the political affilia-
tion preliminary question, which we did not include, but not
in any of the MFQ components. Although elaborating on
the correct answer effect is not our focus, our results again
show evidence of this phenomenon in the OpenAI family
of models. It also provides evidence that it may occur with
other models, in our case, Claude 2.1. Furthermore, this as-
pect seems to be highly impacted by context, as they differed
across conditions in our study.
With some assessment of the overall data of both models,
we discuss our main research question next: Can the outputs
be considered coherent, or are these models hypocrites?
6
Discussion and Implications
We believe our results have implications for different discus-
sions, as well as applications of LLMs. These include moral
alignment, the deployment of LLMs to replace human data
collection, and whether these models display patterns com-
patible with concept mastery of ethical values.
The tests of consistency, coherence, and hypocrisy we
propose are ones we should expect aligned models (and hu-

--- Page 9 ---

man agents) to pass. The apparent inability of current mod-
els to pass them in our study deserves attention, we dis-
cuss related topics and highlight the tests’ relevance to them
throughout the following Subsections.
Moral Alignment
In Section 2, we build our argument standing on the is-
sue of moral hypocrisy. Furthermore, we argue that consis-
tency with regard to moral values is a necessary condition
for proper moral alignment of LLMs, and hypocrisy – con-
flicting abstract values and concrete moral judgements – is a
violation of our moral expectations.
We refer to the quest for alignment as one to ensure that
these models adhere to the values and principles we embed
– consciously or not – into computational artefacts to pre-
vent undesired results. These goals require an appropriate,
consistent, and coherent expression of moral values.11
Hypocrisy violates peoples’ moral expectations and im-
poses a cost on hypocrites’ moral authority (Isserow and
Klein 2017; Kreps, Laurin, and Merritt 2017). Although this
could translate differently depending on how we expect to
deploy LLMs as automated agents, it is clear that such be-
haviour is undesirable.
Merely expressing consistent moral values within a single
abstraction level, which we did find, is not enough. Proper
ethical practice must include navigating different abstraction
levels without contradicting one’s own values. If these mod-
els are to act as surrogates of our (human) values and design
decisions, they must not behave hypocritically.
The investigated state-of-the-art models have ultimately
failed this test. Although GPT-4 and Claude 2.1 displayed
consistency comparable to humans within the MFV ratings
and within part of the MFQ, we found no significant corre-
lation between foundations expressed in these instruments,
even though the instruments were answered in sequence as
part of a single context.
Our premise ultimately is that concrete moral evaluations
ought to correspond to declared abstract values. We believe
this is as important an aspect of moral alignment of auto-
mated systems as properly selecting the values which ought
to be embedded into them.
One possible issue is that LLMs are unreliable regarding
the values embedded into them, similarly to how they (or
humans) cannot properly explain their inner workings, can-
not ensure the veracity of generated content, and are prone
to “hallucinations” (Zhang et al. 2023; Mittelstadt, Wachter,
and Russell 2023; Munn, Magee, and Arora 2023). Other av-
enues to define abstract values embedded in models should
be explored, e.g., checking concrete evaluations to relevant
model constitutions (Bai et al. 2022b) or the data used for
any RLHF procedure, as well as verifying the consistency
of elected values and their expression by models, and other
11We do skirt the difficult meta-issue of how and which values
should be chosen, as well as whether the values observed in our
and related studies are desirable. However, we understand hypo-
critical behaviour would not contribute to alternative definitions of
alignment, e.g., using them to improve human decision-making ac-
cording to certain critical morality standards.
potential use cases which include natural language text gen-
eration, which we do not include in our inquiry.
Concept Mastery
Many impressive results have been reported stating the ca-
pacity of LLMs to behave in myriad tasks and evaluation
methods. For example, OpenAI’s Technical Report on GPT-
4 (OpenAI 2023) reports the model achieved performance
around the 90th percentile in the Bar Exam, LSAT, and parts
of the GRE (but see Mart´ınez (2024)). One possible way
to interpret these results is that state-of-the-art LLMs have
mastered concepts, i.e., these models are capable not only
of reproducing the linguistic patterns associated with spe-
cific concepts but also of capturing the underlying meaning
associated with them. As the optimisation of foundational
models comprises only linguistic patterns, this would be a
surprising finding (Bender et al. 2021).
This description would lead to certain predictions regard-
ing LLMs’ behaviour, such as displaying similar compe-
tence across tasks which depend on the same concepts but
vary in context/phrasing. For example, we could expect that
alternating examples in few-shot learning contexts would
not have a meaningful impact on performance, although the
contrary has been shown to occur (Guha et al. 2023b; Su
et al. 2022; Wang et al. 2024; Guha et al. 2023a).
This view would also imply their performance on certain
tests and evaluations ought to be robust. In contrast, an agent
that simply memorises and repeats patterns without master-
ing the underlying concepts would display very volatile per-
formance depending on the specific wording or context.
In our own results, this might be the reason why mod-
els are consistent within abstraction levels but hypocriti-
cal when both levels are simultaneously considered: current
state-of-the-art LLMs know which patterns to output in reac-
tion to text that bundles together in the training data (either
all items in the MFQ or all vignettes in the MFV) but lack
the conceptual mastery to relate these two sets of texts.
LLM as human-like participants in experiments
Another topic impacted by our results is the possibility of
replacing humans with language models in research or polls
(Dillion et al. 2023; Hutson 2023; H¨am¨al¨ainen, Tavast, and
Kunnari 2023). According to our method of evaluating the
expression of moral values, current models cannot support
such replacement, at least insofar as we are concerned with
morality and the expression of moral values. One way in
which our results could be explored in future work is as a
hoop test for LLMs to serve as human surrogates: at the very
least, their judgements in concrete cases must reliably reflect
the moral values they endorse in the abstract.
7
Conclusion
In this paper, we argue for the importance of the consistent
and coherent expression of moral values for the proper align-
ment of Large Language Models (LLMs) to avoid hypocrit-
ical behaviour. This issue has received scant attention from
existing moral analysis of LLMs, but it has important im-
plications for the debate on AI alignment, as well as for the

--- Page 10 ---

discussion on the use of language models to simulate the
behaviour of human groups in cognitive research.
As a case study, we submitted the Moral Foundation
Questionnaire and the Moral Foundation Vignettes to four
state-of-the-art LLMs: GPT-4, Claude 2.1, Gemini Pro, and
LLAMA-2-Chat-70b. Of those, only GPT-4 and Claude 2.1
generated valid outputs for our stimuli.
We found that, within each instrument, both models were
capable of presenting moral values with consistency com-
parable to human respondents. However, our results utterly
lacked any coherence in the values between abstraction lev-
els. We characterise these models as moral hypocrites, fail-
ing to apply declared abstract values to concrete situations.
If LLMs are to play a role in morally relevant situations
(as they are already being used), we ought to require them
not to be hypocrites, and this should be an important aspect
of alignment evaluation for future models. This is also rel-
evant for anyone considering replacing human participants
with LLMs. Finally, our results are compatible with mimicry
instead of conceptual mastery.
8
Limitations and Future Work
We acknowledge our study and results have limitations. Re-
garding the scope of our analysis, we only consider two
commercial LLMs. Importantly, the Open Source develop-
ment of models has gained momentum with the release of
many fine tunings of open language models. However, the
one we used (LLAMA) could not produce valid results ac-
cording to the criteria and requirements we established.
Further work should explore other open models and other
prompting styles, which may influence the results. As there
is no agreed-upon procedure for using these models to pro-
duce answers to questionnaire-style prompts, our work is
somewhat exploratory. For example, should we set the tem-
perature parameter to 0 to obtain close to deterministic out-
puts, or is the models’ capability to produce a distribution
of results more suitable to represent human behaviour? This
question remains open. Similarly, since LLMs’ behaviour
can be steered by prompts and heavily influenced by the
style of questioning, it is important to test whether our re-
sults are robust to such variations. For example, it is possi-
ble that alternative prompting structures could yield positive
results with Gemini Pro and LLAMA 2 models.
The reviewed literature indicates that small changes in
prompts may lead to significantly different results, such as
the incidence of the “correct answer effect”. This hinders
the generalisation of results. Moreover, different models and
alignment strategies have been proposed. Further research
should investigate how the behaviour of foundational base
models, models that are fine-tuned through Reinforcement
Learning with Human Feedback (Ziegler et al. 2020; Grif-
fith et al. 2013), and “Constitutional AI” (Bai et al. 2022b)
differ. Finally, we based our analysis on the single task of
answering questionnaires with the same prompt structure.
Future research ought to illuminate how these results would
be observable in different tasks or with other structures.
Finally, each family of models may offer models of vary-
ing sizes (in terms of number of parameters) – which are said
to have different capabilities that usually scale with model
size. Future work should explore scaling trends with regard
to moral hypocrisy.
References
Abdulhai, M.; Crepy, C.; Valter, D.; Canny, J.; and Jaques,
N. 2023. Moral Foundations of Large Language Models. In
The AAAI 2023 Workshop on Representation Learning for
Responsible Human-Centric AI. New York, NY, USA.
Almeida, G. F. C. F.; Nunes, J. L.; Engelmann, N.; Wieg-
mann, A.; and de Ara´ujo, M. 2024. Exploring the Psychol-
ogy of LLMs’ Moral and Legal Reasoning. Artificial Intel-
ligence, 104145.
Anthropic.
2023.
Claude
2.
https://www.anthropic.com/index/claude-2.
Atari, M.; Graham, J.; and Dehghani, M. 2020. Foundations
of Morality in Iran. Evolution and Human Behavior, 41(5):
367–384.
Atari, M.; Haidt, J.; Graham, J.; Koleva, S.; Stevens, S. T.;
and Dehghani, M. 2023. Morality beyond the WEIRD: How
the Nomological Network of Morality Varies across Cul-
tures. Journal of Personality and Social Psychology, 125(5):
1157–1188.
Bai, Y.; Jones, A.; Ndousse, K.; Askell, A.; Chen, A.; Das-
Sarma, N.; Drain, D.; Fort, S.; Ganguli, D.; Henighan,
T.; Joseph, N.; Kadavath, S.; Kernion, J.; Conerly, T.; El-
Showk, S.; Elhage, N.; Hatfield-Dodds, Z.; Hernandez, D.;
Hume, T.; Johnston, S.; Kravec, S.; Lovitt, L.; Nanda, N.;
Olsson, C.; Amodei, D.; Brown, T.; Clark, J.; McCandlish,
S.; Olah, C.; Mann, B.; and Kaplan, J. 2022a. Training a
Helpful and Harmless Assistant with Reinforcement Learn-
ing from Human Feedback. arXiv:2204.05862.
Bai, Y.; Kadavath, S.; Kundu, S.; Askell, A.; Kernion, J.;
Jones, A.; Chen, A.; Goldie, A.; Mirhoseini, A.; McKinnon,
C.; Chen, C.; Olsson, C.; Olah, C.; Hernandez, D.; Drain,
D.; Ganguli, D.; Li, D.; Tran-Johnson, E.; Perez, E.; Kerr, J.;
Mueller, J.; Ladish, J.; Landau, J.; Ndousse, K.; Lukosuite,
K.; Lovitt, L.; Sellitto, M.; Elhage, N.; Schiefer, N.; Mer-
cado, N.; DasSarma, N.; Lasenby, R.; Larson, R.; Ringer,
S.; Johnston, S.; Kravec, S.; Showk, S. E.; Fort, S.; Lanham,
T.; Telleen-Lawton, T.; Conerly, T.; Henighan, T.; Hume,
T.; Bowman, S. R.; Hatfield-Dodds, Z.; Mann, B.; Amodei,
D.; Joseph, N.; McCandlish, S.; Brown, T.; and Kaplan, J.
2022b. Constitutional AI: Harmlessness from AI Feedback.
arxiv:2212.08073.
Bender, E. M.; Gebru, T.; McMillan-Major, A.; and
Shmitchell, S. 2021.
On the Dangers of Stochastic Par-
rots: Can Language Models Be Too Big? In Proceedings of
the 2021 ACM Conference on Fairness, Accountability, and
Transparency, FAccT ’21, 610–623. New York, NY, USA:
Association for Computing Machinery. ISBN 978-1-4503-
8309-7.
Bubeck, S.; Chandrasekaran, V.; Eldan, R.; Gehrke, J.;
Horvitz, E.; Kamar, E.; Lee, P.; Lee, Y. T.; Li, Y.; Lundberg,
S.; Nori, H.; Palangi, H.; Ribeiro, M. T.; and Zhang, Y. 2023.
Sparks of Artificial General Intelligence: Early Experiments
with GPT-4.

--- Page 11 ---

Clifford, S.; Iyengar, V.; Cabeza, R.; and Sinnott-Armstrong,
W. 2015.
Moral Foundations Vignettes: A Standardized
Stimulus Database of Scenarios Based on Moral Founda-
tions Theory.
Behavior Research Methods, 47(4): 1178–
1198.
Crisp, R.; and Cowton, C. 1994. Hypocrisy and Moral Se-
riousness. American Philosophical Quarterly, 31(4): 343–
349.
Crone, D. L.; and Laham, S. M. 2015. Multiple Moral Foun-
dations Predict Responses to Sacrificial Dilemmas. Person-
ality and Individual Differences, 85: 60–65.
Dillion, D.; Tandon, N.; Gu, Y.; and Gray, K. 2023. Can AI
Language Models Replace Human Participants? Trends in
Cognitive Sciences, 27(7): 597–600.
Dobolyi, D. 2023. Moral Foundations Theory | Moralfoun-
dations.Org.
European Union Agency for Law Enforcement Cooperation.
2023. ChatGPT: The Impact of Large Language Models on
Law Enforcement. LU: Publications Office.
Frimer, J. 2019. Moral Foundations Dictionary 2.0.
Gabriel, I. 2020. Artificial Intelligence, Values, and Align-
ment. Minds and Machines, 30(3): 411–437.
Google, G. T. 2023. Gemini: A Family of Highly Capable
Multimodal Models. arxiv:2312.11805.
Graham, J.; Haidt, J.; Koleva, S.; Motyl, M.; Iyer, R.; Woj-
cik, S. P.; and Ditto, P. H. 2013. Chapter Two - Moral Foun-
dations Theory: The Pragmatic Validity of Moral Pluralism.
In Devine, P.; and Plant, A., eds., Advances in Experimental
Social Psychology, volume 47, 55–130. Academic Press.
Graham, J.; Haidt, J.; and Nosek, B. A. 2009. Liberals and
Conservatives Rely on Different Sets of Moral Foundations.
Journal of Personality and Social Psychology, 96(5): 1029–
1046.
Graham, J.; Nosek, B. A.; Haidt, J.; Iyer, R.; Koleva, S.; and
Ditto, P. H. 2011. Mapping the Moral Domain. Journal of
personality and social psychology, 101(2): 366.
Griffith, S.; Subramanian, K.; Scholz, J.; Isbell, C. L.; and
Thomaz, A. 2013.
Policy Shaping: Integrating Human
Feedback with Reinforcement Learning.
In Proceedings
of the 26th International Conference on Neural Information
Processing Systems - Volume 2, NIPS’13, 2625–2633. Red
Hook, NY, USA: Curran Associates Inc.
Guha, N.; Chen, M. F.; Bhatia, K.; Mirhoseini, A.; Sala,
F.; and R´e, C. 2023a.
Embroid: Unsupervised Pre-
diction Smoothing Can Improve Few-Shot Classification.
arxiv:2307.11031.
Guha, N.; Nyarko, J.; Ho, D. E.; R´e, C.; Chilton, A.;
Narayana, A.; Chohlas-Wood, A.; Peters, A.; Waldon, B.;
Rockmore, D. N.; Zambrano, D.; Talisman, D.; Hoque, E.;
Surani, F.; Fagan, F.; Sarfaty, G.; Dickinson, G. M.; Po-
rat, H.; Hegland, J.; Wu, J.; Nudell, J.; Niklaus, J.; Nay, J.;
Choi, J. H.; Tobia, K.; Hagan, M.; Ma, M.; Livermore, M.;
Rasumov-Rahe, N.; Holzenberger, N.; Kolt, N.; Henderson,
P.; Rehaag, S.; Goel, S.; Gao, S.; Williams, S.; Gandhi, S.;
Zur, T.; Iyer, V.; and Li, Z. 2023b. LegalBench: A Collabo-
ratively Built Benchmark for Measuring Legal Reasoning in
Large Language Models. arxiv:2308.11462.
H¨am¨al¨ainen, P.; Tavast, M.; and Kunnari, A. 2023. Evalu-
ating Large Language Models in Generating Synthetic HCI
Research Data: A Case Study. In Proceedings of the 2023
CHI Conference on Human Factors in Computing Systems,
CHI ’23, 1–19. New York, NY, USA: Association for Com-
puting Machinery. ISBN 978-1-4503-9421-5.
Hatemi, P. K.; Crabtree, C.; and Smith, K. B. 2019. Ideol-
ogy Justifies Morality: Political Beliefs Predict Moral Foun-
dations. American Journal of Political Science, 63(4): 788–
806.
Hopp, F. R.; Fisher, J. T.; Cornell, D.; Huskey, R.; and We-
ber, R. 2021.
The Extended Moral Foundations Dictio-
nary (eMFD): Development and Applications of a Crowd-
Sourced Approach to Extracting Moral Intuitions from Text.
Behavior Research Methods, 53(1): 232–246.
Hutson, M. 2023. Guinea Pigbots: Doing Research with Hu-
man Subjects Is Costly and Cumbersome. Can AI Chatbots
Replace Them? Science, 381(6654): 121–123.
Isserow, J.; and Klein, C. 2017. Hypocrisy and Moral Au-
thority.
Journal of Ethics and Social Philosophy, 12(2):
191–222.
Iurino, K.; and Saucier, G. 2020. Testing Measurement In-
variance of the Moral Foundations Questionnaire Across 27
Countries. Assessment, 27(2): 365–372.
Iyer, R.; Koleva, S.; Graham, J.; Ditto, P.; and Haidt, J. 21
de ago. de 2012. Understanding Libertarian Morality: The
Psychological Dispositions of Self-Identified Libertarians.
PLOS ONE, 7(8): e42366.
Kalimeri, K.; Beir´o, M. G.; Delfino, M.; Raleigh, R.; and
Cattuto, C. 2019. Predicting Demographics, Moral Founda-
tions, and Human Values from Digital Behaviours. Comput-
ers in Human Behavior, 92: 428–445.
Kittay, E. F. 1982. On Hypocrisy1. Metaphilosophy, 13(3-
4): 277–289.
Klein, R. A.; Vianello, M.; Hasselman, F.; Adams, B. G.;
Adams, R. B.; Alper, S.; Aveyard, M.; Axt, J. R.; Babalola,
M. T.; Bahn´ık, ˇS.; Batra, R.; Berkics, M.; Bernstein, M. J.;
Berry, D. R.; Bialobrzeska, O.; Binan, E. D.; Bocian, K.;
Brandt, M. J.; Busching, R.; R´edei, A. C.; Cai, H.; Cambier,
F.; Cantarero, K.; Carmichael, C. L.; Ceric, F.; Chandler, J.;
Chang, J.-H.; Chatard, A.; Chen, E. E.; Cheong, W.; Cicero,
D. C.; Coen, S.; Coleman, J. A.; Collisson, B.; Conway,
M. A.; Corker, K. S.; Curran, P. G.; Cushman, F.; Dagona,
Z. K.; Dalgar, I.; Dalla Rosa, A.; Davis, W. E.; De Bruijn,
M.; De Schutter, L.; Devos, T.; De Vries, M.; Do˘gulu, C.;
Dozo, N.; Dukes, K. N.; Dunham, Y.; Durrheim, K.; Eber-
sole, C. R.; Edlund, J. E.; Eller, A.; English, A. S.; Finck,
C.; Frankowska, N.; Freyre, M.- ´A.; Friedman, M.; Galliani,
E. M.; Gandi, J. C.; Ghoshal, T.; Giessner, S. R.; Gill, T.;
Gnambs, T.; G´omez, ´A.; Gonz´alez, R.; Graham, J.; Grahe,
J. E.; Grahek, I.; Green, E. G. T.; Hai, K.; Haigh, M.; Haines,
E. L.; Hall, M. P.; Heffernan, M. E.; Hicks, J. A.; Houdek,
P.; Huntsinger, J. R.; Huynh, H. P.; IJzerman, H.; Inbar, Y.;
Innes-Ker, ˚A. H.; Jim´enez-Leal, W.; John, M.-S.; Joy-Gaba,
J. A.; Kamilo˘glu, R. G.; Kappes, H. B.; Karabati, S.; Kar-
ick, H.; Keller, V. N.; Kende, A.; Kervyn, N.; Kneˇzevi´c, G.;
Kovacs, C.; Krueger, L. E.; Kurapov, G.; Kurtz, J.; Lakens,

--- Page 12 ---

D.; Lazarevi´c, L. B.; Levitan, C. A.; Lewis, N. A.; Lins, S.;
Lipsey, N. P.; Losee, J. E.; Maassen, E.; Maitner, A. T.; Ma-
lingumu, W.; Mallett, R. K.; Marotta, S. A.; Medjedovi´c, J.;
Mena-Pacheco, F.; Milfont, T. L.; Morris, W. L.; Murphy,
S. C.; Myachykov, A.; Neave, N.; Neijenhuijs, K.; Nelson,
A. J.; Neto, F.; Lee Nichols, A.; Ocampo, A.; O’Donnell,
S. L.; Oikawa, H.; Oikawa, M.; Ong, E.; Orosz, G.; Os-
owiecka, M.; Packard, G.; P´erez-S´anchez, R.; Petrovi´c, B.;
Pilati, R.; Pinter, B.; Podesta, L.; Pogge, G.; Pollmann, M.
M. H.; Rutchick, A. M.; Saavedra, P.; Saeri, A. K.; Salomon,
E.; Schmidt, K.; Sch¨onbrodt, F. D.; Sekerdej, M. B.; Sir-
lop´u, D.; Skorinko, J. L. M.; Smith, M. A.; Smith-Castro, V.;
Smolders, K. C. H. J.; Sobkow, A.; Sowden, W.; Spachtholz,
P.; Srivastava, M.; Steiner, T. G.; Stouten, J.; Street, C. N. H.;
Sundfelt, O. K.; Szeto, S.; Szumowska, E.; Tang, A. C. W.;
Tanzer, N.; Tear, M. J.; Theriault, J.; Thomae, M.; Torres, D.;
Traczyk, J.; Tybur, J. M.; Ujhelyi, A.; Van Aert, R. C. M.;
Van Assen, M. A. L. M.; Van Der Hulst, M.; Van Lange,
P. A. M.; Van ’T Veer, A. E.; V´asquez- Echeverr´ıa, A.;
Ann Vaughn, L.; V´azquez, A.; Vega, L. D.; Verniers, C.;
Verschoor, M.; Voermans, I. P. J.; Vranka, M. A.; Welch,
C.; Wichman, A. L.; Williams, L. A.; Wood, M.; Woodz-
icka, J. A.; Wronska, M. K.; Young, L.; Zelenski, J. M.; Zhi-
jia, Z.; and Nosek, B. A. 2018. Many Labs 2: Investigating
Variation in Replicability Across Samples and Settings. Ad-
vances in Methods and Practices in Psychological Science,
1(4): 443–490.
Kozlov, M. 2023. First Global Survey Reveals Who Is Doing
‘Gain of Function’ Research on Pathogens and Why. Nature,
621(7980): 668–669.
Kreps, T. A.; Laurin, K.; and Merritt, A. C. 2017. Hypo-
critical Flip-Flop, or Courageous Evolution? When Leaders
Change Their Moral Minds. Journal of Personality and So-
cial Psychology, 113(5): 730–752.
Kumar, H.; Wang, Y.; Shi, J.; Musabirov, I.; Farb, N. A. S.;
and Williams, J. J. 2023. Exploring the Use of Large Lan-
guage Models for Improving the Awareness of Mindful-
ness. In Extended Abstracts of the 2023 CHI Conference on
Human Factors in Computing Systems, CHI EA ’23, 1–7.
New York, NY, USA: Association for Computing Machin-
ery. ISBN 978-1-4503-9422-2.
Lance, C. E.; Butts, M. M.; and Michels, L. C. 2006. The
Sources of Four Commonly Reported Cutoff Criteria: What
Did They Really Say? Organizational Research Methods,
9(2): 202–220.
Marques, L. M.; Clifford, S.; Iyengar, V.; Bonato, G. V.;
Cabral, P. M.; dos Santos, R. B.; Cabeza, R.; Sinnott-
Armstrong, W.; and Boggio, P. S. 2020.
Translation and
Validation of the Moral Foundations Vignettes (MFVs) for
the Portuguese Language in a Brazilian Sample. Judgment
and Decision Making, 15(1): 149–158.
Mart´ınez, E. 2024. Re-Evaluating GPT-4’s Bar Exam Per-
formance. Artificial Intelligence and Law.
Mittelstadt, B.; Wachter, S.; and Russell, C. 2023. To Pro-
tect Science, We Must Use LLMs as Zero-Shot Translators.
Nature Human Behaviour, 7(11): 1830–1832.
Munn, L.; Magee, L.; and Arora, V. 2023. Truth Machines:
Synthesizing Veracity in AI Language Models. AI & SOCI-
ETY.
Nilsson, A.; and Erlandsson, A. 2015. The Moral Founda-
tions Taxonomy: Structural Validity and Relation to Political
Ideology in Sweden. Personality and Individual Differences,
76: 28–32.
OpenAI. 2023. GPT-4 Technical Report. arxiv:2303.08774.
Park, P. S.; Schoenegger, P.; and Zhu, C. 2023. Diminished
Diversity-of-Thought in a Standard Large Language Model.
arxiv:2302.07267.
Pereira, J.; Assumpcao, A.; Trecenti, J.; Airosa, L.; Lente,
C.; Cl´eto, J.; Dobins, G.; Nogueira, R.; Mitchell, L.; and
Lotufo, R. 2024.
INACIA: Integrating Large Language
Models in Brazilian Audit Courts: Opportunities and Chal-
lenges. arxiv:2401.05273.
Rathje, S.; Mirea, D.-M.; Sucholutsky, I.; Marjieh, R.;
Robertson, C.; and Bavel, J. J. V. 2023. GPT Is an Effec-
tive Tool for Multilingual Psychological Text Analysis.
Santurkar, S.; Durmus, E.; Ladhak, F.; Lee, C.; Liang, P.; and
Hashimoto, T. 2023. Whose Opinions Do Language Models
Reflect? arxiv:2303.17548.
Savelka, J. 2023. Unlocking Practical Applications in Legal
Domain: Evaluation of GPT for Zero-Shot Semantic An-
notation of Legal Texts. In Nineteenth International Con-
ference on Artificial Intelligence and Law (ICAIL 2023), 5.
Braga, Portugal: ACM, New York, NY, USA.
Schein, C.; and Gray, K. 2018. The Theory of Dyadic Moral-
ity: Reinventing Moral Judgment by Redefining Harm. Per-
sonality and Social Psychology Review, 22(1): 32–70.
Sharma, M.; Tong, M.; Korbak, T.; Duvenaud, D.; Askell,
A.; Bowman, S. R.; Cheng, N.; Durmus, E.; Hatfield-Dodds,
Z.; Johnston, S. R.; Kravec, S.; Maxwell, T.; McCandlish, S.;
Ndousse, K.; Rausch, O.; Schiefer, N.; Yan, D.; Zhang, M.;
and Perez, E. 2023. Towards Understanding Sycophancy in
Language Models. ArXiv:2310.13548 [cs, stat].
Simmons, G. 2022. Moral Mimicry: Large Language Mod-
els Produce Moral Rationalizations Tailored to Political
Identity. arxiv:2209.12106.
Singhal, K.; Azizi, S.; Tu, T.; Mahdavi, S. S.; Wei, J.; Chung,
H. W.; Scales, N.; Tanwani, A.; Cole-Lewis, H.; Pfohl, S.;
Payne, P.; Seneviratne, M.; Gamble, P.; Kelly, C.; Babiker,
A.; Sch¨arli, N.; Chowdhery, A.; Mansfield, P.; Demner-
Fushman, D.; Ag¨uera y Arcas, B.; Webster, D.; Corrado,
G. S.; Matias, Y.; Chou, K.; Gottweis, J.; Tomasev, N.; Liu,
Y.; Rajkomar, A.; Barral, J.; Semturs, C.; Karthikesalingam,
A.; and Natarajan, V. 2023. Large Language Models Encode
Clinical Knowledge. Nature, 620(7972): 172–180.
Smith, K. B.; Alford, J. R.; Hibbing, J. R.; Martin, N. G.;
and Hatemi, P. K. 2017. Intuitive Ethics and Political Ori-
entations: Testing Moral Foundations as a Theory of Politi-
cal Ideology. American Journal of Political Science, 61(2):
424–437.
Su, H.; Kasai, J.; Wu, C. H.; Shi, W.; Wang, T.; Xin, J.;
Zhang, R.; Ostendorf, M.; Zettlemoyer, L.; Smith, N. A.; and
Yu, T. 2022. Selective Annotation Makes Language Models
Better Few-Shot Learners.
In The Eleventh International
Conference on Learning Representations.

--- Page 13 ---

Thirunavukarasu, A. J.; Ting, D. S. J.; Elangovan, K.;
Gutierrez, L.; Tan, T. F.; and Ting, D. S. W. 2023. Large Lan-
guage Models in Medicine. Nature Medicine, 29(8): 1930–
1940.
Touvron, H.; Martin, L.; Stone, K.; Albert, P.; Almahairi, A.;
Babaei, Y.; Bashlykov, N.; Batra, S.; Bhargava, P.; Bhosale,
S.; Bikel, D.; Blecher, L.; Ferrer, C. C.; Chen, M.; Cucu-
rull, G.; Esiobu, D.; Fernandes, J.; Fu, J.; Fu, W.; Fuller, B.;
Gao, C.; Goswami, V.; Goyal, N.; Hartshorn, A.; Hosseini,
S.; Hou, R.; Inan, H.; Kardas, M.; Kerkez, V.; Khabsa, M.;
Kloumann, I.; Korenev, A.; Koura, P. S.; Lachaux, M.-A.;
Lavril, T.; Lee, J.; Liskovich, D.; Lu, Y.; Mao, Y.; Martinet,
X.; Mihaylov, T.; Mishra, P.; Molybog, I.; Nie, Y.; Poul-
ton, A.; Reizenstein, J.; Rungta, R.; Saladi, K.; Schelten, A.;
Silva, R.; Smith, E. M.; Subramanian, R.; Tan, X. E.; Tang,
B.; Taylor, R.; Williams, A.; Kuan, J. X.; Xu, P.; Yan, Z.;
Zarov, I.; Zhang, Y.; Fan, A.; Kambadur, M.; Narang, S.; Ro-
driguez, A.; Stojnic, R.; Edunov, S.; and Scialom, T. 2023.
Llama 2: Open Foundation and Fine-Tuned Chat Models.
arXiv:2307.09288.
Wang, X.; Zhu, W.; Saxon, M.; Steyvers, M.; and Wang,
W. Y. 2024. Large Language Models Are Latent Variable
Models: Explaining and Finding Good Demonstrations for
In-Context Learning. arxiv:2301.11916.
Wei, J.; Tay, Y.; Bommasani, R.; Raffel, C.; Zoph, B.;
Borgeaud, S.; Yogatama, D.; Bosma, M.; Zhou, D.; Met-
zler, D.; Chi, E. H.; Hashimoto, T.; Vinyals, O.; Liang, P.;
Dean, J.; and Fedus, W. 2022. Emergent Abilities of Large
Language Models. arxiv:2206.07682.
Yilmaz, O.; Harma, M.; Bahc¸ekapili, H. G.; and Cesur, S.
2016. Validation of the Moral Foundations Questionnaire
in Turkey and Its Relation to Cultural Schemas of Individu-
alism and Collectivism. Personality and Individual Differ-
ences, 99: 149–154.
Zamfirescu-Pereira, J.; Wong, R. Y.; Hartmann, B.; and
Yang, Q. 2023. Why Johnny Can’t Prompt: How Non-AI
Experts Try (and Fail) to Design LLM Prompts. In Pro-
ceedings of the 2023 CHI Conference on Human Factors in
Computing Systems, CHI ’23, 1–21. New York, NY, USA:
Association for Computing Machinery. ISBN 978-1-4503-
9421-5.
Zhang, Y.; Li, Y.; Cui, L.; Cai, D.; Liu, L.; Fu, T.; Huang,
X.; Zhao, E.; Zhang, Y.; Chen, Y.; Wang, L.; Luu, A. T.;
Bi, W.; Shi, F.; and Shi, S. 2023. Siren’s Song in the AI
Ocean: A Survey on Hallucination in Large Language Mod-
els. arxiv:2309.01219.
Ziegler, D. M.; Stiennon, N.; Wu, J.; Brown, T. B.; Rad-
ford, A.; Amodei, D.; Christiano, P.; and Irving, G. 2020.
Fine-Tuning Language Models from Human Preferences.
arxiv:1909.08593.
A
Condition Difference
Since using LLMs to replicate experiments made with hu-
mans is still exploratory, it is important to understand how
the change in context created by altering the order of the
conditions may affect the results. This distribution can be
seen in Figure 4. For reference, we include the distribution
without condition distinction within labelled as ‘overall’.
MFV
MFQ
Agent: Claude 2.1
0.0
0.2
0.4
0.6
0.8
1.0
Cronbach's alpha
MFV
MFQ
Agent: GPT-4
Distribution of Cronbach's alpha by Model and Condition
Condition
QV
VQ
Overall
Figure 4: Distribution of Cronbach’s alpha per AI agent and
condition. Error bars cover all observations.
We ran t-tests to explore whether there were significant
differences in the α distributions between the instrument or-
der conditions (QV and VQ) for each model. We found no
significant difference for Claude 2.1 (t(22) = −0.60, p =
0.55). However, we found a significant difference for GPT-4
(t(22) = 5.49, p < 0.001), with a considerable size effect
(Cohen’s d = 1.16), as can be observed in GPT-4 panel of
Figure 4.
We understand this difference in itself may display con-
sequences related to our concerns. The lower α values ob-
served by GPT-4 in the VQcondition regarding the MFQ are
indicators the model cannot appropriately perform the task
in every context, even though we submitted the same query
and instructions. This also relates to the Concept Mastery
aspect raised in our discussion. We opt not to elaborate on
this as it would be tangent to our proposed analysis.

```
