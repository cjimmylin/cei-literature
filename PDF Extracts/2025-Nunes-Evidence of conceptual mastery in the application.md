---
title: "Evidence of conceptual mastery in the application - PDF Extract"
source_pdf: "2025-Nunes-Evidence of conceptual mastery in the application.pdf"
pages: 19
extracted_at: "2026-01-24T16:38:32.229588"
---

# PDF Extract: Evidence of conceptual mastery in the application

**Source PDF:** 2025-Nunes-Evidence of conceptual mastery in the application.pdf
**Total Pages:** 19

---

## Content

```
--- Page 1 ---

 
Evidence of conceptual mastery in the application 
of rules by Large Language Models 
José Luiz Nunes*1, Guilherme FCF Almeida*2, Brian Flanagan3 
 
Abstract:  
In this paper we leverage psychological methods to investigate LLMs’ conceptual mastery in 
applying rules. We introduce a novel procedure to match the diversity of thought generated 
by LLMs to that observed in a human sample. We then conducted two experiments 
comparing rule-based decision-making in humans and LLMs. Study 1 found that all 
investigated LLMs replicated human patterns regardless of whether they are prompted with 
scenarios created before or after their training cut-off. Moreover, we found unanticipated 
differences between the two sets of scenarios among humans. Surprisingly, even these 
differences were replicated in LLM responses. Study 2 turned to a contextual feature of 
human rule application: under forced time delay, human samples rely more heavily on a 
rule’s text than on other considerations such as a rule’s purpose.. Our results revealed that 
some models (Gemini Pro and Claude 3) responded in a human-like manner to a prompt 
describing either forced delay or time pressure, while others (GPT-4o and Llama 3.2 90b) 
did not. We argue that the evidence gathered suggests that LLMs have mastery over the 
concept of rule, with implications for both legal decision making and philosophical inquiry. 
Introduction 
Conceptual mastery 
Large Language Models (LLMs) have been found to match (or exceed) human performance 
across a strikingly wide range of tasks, from coding (Chen et al. 2021) to fiction writing, 
(Doshi and Hauser 2024) and from medical exams (Nori et al. 2023) to general conversation 
(Jones and Bergen 2024). Another feature shared by LLMs and humans is that the internal 
operations that support these capabilities through biological and artificial neural networks 
respectively are opaque. This means both that such operations are inscrutable to first person 
introspection and that we don't have a complete mechanistic explanation of how the lower-
level components of these systems - neurons - interact to generate these complex 
behaviors. Thus, just as neuroscience has yet to fully elucidate how the human brain 
explains human behavior, computer scientists are unable to do the same for LLMs (see 
Bricken et al. 2023; Templeton et al. 2024 for ongoing work on finding such an explanation 
for LLMs). 
 
 
* Co-first authors. 
1 Department of Informatics, PUC-Rio. FGV Direito Rio. 
2 Insper Institute of Education and Research. 
3 School of Law and Criminology, Maynooth University. 

--- Page 2 ---

 
Much of our current understanding of the human mind owes instead to psychology. An 
intriguing possibility is that such methods could similarly yield insight into the operation of 
generative AI. This paper tests this possibility by leveraging psychology research studies in 
which LLMs and humans participate as research subjects for the purpose of investigating 
conceptual competence in the domain of law. 
 
Cognitive scientists and philosophers usually assume that psychological methods are 
capable of providing insight into the content of human concepts. Consider the concept of 
knowledge, which had long been defined as the possession of a justified true belief. Starting 
in 1963, epistemologists identified several cases featuring people who did not seem to know 
something that was the subject of a justified, true belief of theirs (Gettier 1963). For instance, 
suppose that someone looks at a watch which shows that the current time is 12:15. As it 
turns out, it is actually 12:15, but the watch is broken. Does that person know that it is 
currently 12:15? Philosophers suggested that, intuitively, the person does not truly know 
what time it is. Cross-cultural experimental investigation has duly shown that this inclination 
is indeed widely shared (Machery et al. 2017). In this way, philosophers and cognitive 
scientists have used a “sharpened awareness of words to sharpen our perception of the 
phenomena” (Hart 1994 paraphrasing JL Austin). Many other examples exist (Stich and 
Tobia 2016).  
 
Transposing this methodology to LLMs, recent work in machine psychology (Hagendorff et 
al. 2023) has investigated LLMs’ morality (Dillion et al. 2023; Park, Schoenegger, and Zhu 
2023; Ji et al. 2024; Nunes et al. 2024; Dillion et al. 2025), their ability to render causal 
judgments (Nie et al. 2023), their theory of mind (Strachan et al. 2024), as well as several 
other concepts (see Almeida et al. 2024). 
 
These findings have sometimes been met with skepticism, however. Critics object that the 
exact wording of any stimuli previously employed with humans is often available on the open 
web and is therefore likely to appear in the pre training data for major LLMs. Thus, it is 
possible that, instead of actually mastering concepts such as morality, causation, and mind, 
LLMs are simply reproducing memorized patterns already included in their training datasets 
(see Magar and Schwartz 2022; Wang et al. 2024). Other critiques highlight LLMs’ sensitivity 
to which specific examples are used in few-shot learning (Guha, Nyarko, et al. 2023; Su et 
al. 2023; Guha, Chen, et al. 2023) as well as to the wording of system prompts (Röttger et 
al. 2024; Beck et al. 2023). 
 
Given this background, a central question in current machine psychology is whether LLMs 
have truly acquired conceptual competences that were once the exclusive domain of human 
cognition, or are nothing but fancy autocomplete. 
Rules and legal reasoning 
In this paper, we tackle the broader question of conceptual competence through the lens of 
one specific task: rule application. We selected rule application because of its importance in 
legal reasoning (Schauer 2012), a task in which generative AI is increasingly being deployed 
(Gutiérrez 2024). Knowing whether current LLMs (see Table 1) mirror humans in their rule 
violation judgments is of pressing importance because ‘technological infrastructures matter, 

--- Page 3 ---

 
require our attention and must somehow be brought under the Rule of Law’ (Hildebrandt 
2016, 2). 
 
Recent work at the intersection of cognitive science and legal philosophy has employed an 
experimental strategy to uncover the lay concept of rule. Such research proceeds by 
presenting participants with the text and purpose associated with a rule. For instance, one 
vignette employed in the literature tells participants about a rule prohibiting shoes in an 
apartment that was introduced to ensure that the floor is kept clean. Participants are then 
presented with cases where text and purpose either a) both recommend that the rule has 
been violated (e.g., someone walks in with dirty sneakers), b) both recommend that the rule 
has not been violated (e.g., someone walks in barefoot with clean feet), c) diverge, with text 
indicating that the rule has been violated and purpose suggesting the opposite (e.g., 
someone walks in with brand new shoes), or d) diverge, with purpose indicating that the rule 
has  been violated, but text suggesting the opposite (e.g., someone walks in barefoot but 
with very dirty feet). This strategy has revealed that people rely on both text and purpose 
when making rule violation judgments, as well as on several further factors which selectively 
amplify their respective effects (see Almeida, Struchiner, and Hannikainen 2024 for an 
overview). 
 
Previous work has already replicated some of these studies with LLMs, revealing high 
correlations and very similar patterns across human and LLM rule applications (Almeida et 
al. 2024). However, such research used stimuli that had been available on the open web as 
of model training data cutoff. This raises the aforementioned worry that the models might 
have simply reproduced information that was already explicitly represented in their training 
set, performing something akin to a search, instead of truly deploying a human-like concept 
of rule violation. 
 
Moreover, while similar on aggregate, LLM responses were still significantly different from 
those produced by human beings. In particular, LLMs in previous research have tended to 
produce comparatively larger effects than those detected among humans, partly due to their 
reduced response variance, a behaviour dubbed “diminished diversity of thought” (Park, 
Schoenegger, and Zhu 2023). 
Comparing LLMs and humans 
LLMs’ reduced response variance could be caused by their shared architecture: perhaps 
LLMs are much more likely than humans to prioritize their best guess over any more 
exploratory conjecture. But unlike humans, the extent to which LLMs prioritize their best 
guess is controllable by a tunable parameter: temperature. While different models implement 
and are affected by temperature in different ways, lower levels will result in the model 
prioritizing the token it has learned as most likely to follow a given text. On the other hand, 
higher values increase the chance of using tokens assigned lower probability, a behaviour 
usually described as creative or exploratory (see, for instance, the use in Dillion et al. 2025). 
 
Previous research either set LLM temperature to zero in order to ensure reproducibility 
(Guha, Nyarko, et al. 2023; Dillion et al. 2025), left it at default (Sachdeva and van Nuenen 
2025), or chose arbitrary points for different models (Almeida et al. 2024; Nunes et al. 2024; 

--- Page 4 ---

 
Fränken et al. 2024; Shen, Clark, and Mitra 2025). All of these strategies make it difficult to 
assess whether the systematic variations observed between the diversity of human 
responses and those of different LLMs are due to (a) architectural differences or (b) the 
specific temperatures used. Accordingly, we preface our experiments with a preliminary 
analysis that identifies a method for systematically determining the experimentally 
appropriate LLM temperature. 
Contributions 
Responding to the challenges described above, we designed and conducted two novel 
experiments testing LLM rule application. To support these experiments, we used the data 
collected from human participants for Study 1 to determine the temperatures that most 
closely mimic variation in human responses.  
 
Our diversity of thought analysis revealed that the ideal temperature under our constraints 
differed for each model. It also showed that, even where an LLM’s response exhibited the 
same overall patterns, it never reproduced the full degree of variance exhibited by the 
human response. 
 
To establish whether rule application does indeed mark out a sphere of AI conceptual 
mastery, Study 1 reports the results of an experiment conducted simultaneously with LLMs 
and humans using original vignettes matched with those used by previous research 
(Flanagan et al. 2023). Comparing how humans and LLMs were affected by the 
experimental manipulations, we replicate Flanagan and colleagues' original findings among 
humans (Flanagan et al. 2023). Then, we show that the same significance patterns also 
occur in human and LLM response to the new stimuli. Finally, we report a novel result that 
both humans and LLMs were less likely to rely on text when prompted with the new vignettes 
in comparison to the original ones. This further suggests their competence in tracking human 
judgement. 
 
Human concepts are deployed in all kinds of different settings that make no sense from the 
perspective of current text-based LLMs. For instance, one characteristic feature of human 
rule violation judgments is that they are subject to time pressure (Flanagan et al. 2023). 
When deciding quickly, humans are significantly more likely to apply rules in a way that 
accords with a rule’s purpose rather than its text. In contrast, when deciding after a period of 
reflection, people are more inclined to apply the rule literally. This sort of manipulation should 
make no difference to LLMs, however. Commercial APIs offer no way of controlling the 
compute time dedicated to each token and it is not clear that the architecture of traditional 
LLMs would even allow for that sort of control (as opposed to LLMs with reasoning, see 
OpenAI et al. 2024) 
 
In Study 2, we present LLMs with stimuli that were adapted from Flanagan et al (2023). 
Surprisingly, many LLMs mirrored humans in responding in significantly different ways when 
they were instructed to apply the rule either under time pressure (in 4 seconds or less) or 
after a forced delay (of 15 seconds), even though every LLM instance responded with a 
single response token. 
 

--- Page 5 ---

 
We conclude with a discussion of the implications of the findings for computer science 
debates about whether models have attained conceptual mastery and for normative debates 
about how these models should (or should not) be deployed in legal settings. 
 
Table 1 - Information about models and API used 
 
Model 
Version 
Training Data Cutoff 
API endpoint used 
GPT-4 
gpt-4o-2024-08-06 
October, 20234 
OpenAI API 
LLAMA 3 
Llama 3.2 90B 
Instruct 
December 1, 20235 
Amazon Bedrock 
Claude 3 
Claude 3 Opus 
(20240229) 
August, 20236 
Anthropic API 
Gemini 
Gemini 1.5 Pro 002 
May, 20247 
Google Generative 
Language API 
 
 
Study 1 
Methods 
We recruited 120 participants from Prolific. After excluding 2 incomplete responses and 3 
participants who failed our pre-registered attention check, we were left with a final human 
sample of 115 respondents (36 male; 79 female; mean of age = 36). 
All data, stimuli, and analysis scripts are available at: 
https://osf.io/uvy9x/?view_only=95db33761f92421393ed9d58c46131cb  
We also generated responses to the same stimuli using 240 separate instances of each of 
the following LLMs: Llama 3.1 90b, Gemini Pro, Claude 3, and GPT-4o.8 For GPT-4o, 62 
instances were discarded following the pre-registered procedure for removing answers that 
failed the attention check question, as well as those including values outside the scale 
boundary.9 
Replicating previous research (Flanagan et al. 2023), Study 1 followed a 2 (text: violated, not 
violated) x 2 (purpose: violated, not violated) x 4 (scenario: no dogs in the restaurant, no 
 
4 https://platform.openai.com/docs/models/gp#gpt-4o 
5 https://huggingface.co/meta-llama/Llama-3.2-90B-Vision-Instruct 
6 https://docs.anthropic.com/en/docs/about-claude/models 
7 https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models#gemini-1.5-pro 
8 Due to a mistake, we generated twice the amount of data for LLMs than we had initially planned in 
the pre-registered procedure. As we will see, there was relatively little variance in LLM-generated 
data, such that this deviation did not impact our results. 
9 https://aspredicted.org/ck95-whg7.pdf  

--- Page 6 ---

 
vehicles in the park, no shoes inside, no shooting wild animals) within-subjects design, with 
a novel between-subjects manipulation of whether participants were presented with the 
original, old vignettes (which were already published on the open web) or with matched 
vignettes that were newly created for this specific study. 
Each participant (or each model instance) received all 16 unique versions of either the new 
or the old vignettes. For an example, see all variations of the “no dogs in the restaurant” 
scenario in Table 1. 
 
Original Vignettes 
New vignettes 
 
Introduction 
A local restaurant owner 
posted a rule: "No Dogs 
Permitted". 
 
The restaurant rule is meant 
to prevent interruptions by 
unruly pets.  
Restaurant management 
posted a notice: "Dogs are 
forbidden". 
 
The rule was introduced to 
stop noisy pets disturbing 
customers.   
Text violated/Purpose 
violated 
Joe enters the restaurant at 
lunchtime with his unruly pet 
dog.  
Vicky enters the restaurant 
accompanied by her noisy 
pet dog.  
 
 
Text violated/Purpose not 
violated 
Derek, who is blind, enters 
the restaurant with his well-
trained guide dog.  
 
 
 
Louis, who has a disability, 
walks into the restaurant 
with a well behaved service 
dog. 
 
 
Text not violated/Purpose 
violated 
Bill enters the restaurant 
bringing with him his 
naughty pet monkey. 
 
Paula enters the restaurant 
together with her squawking 
pet parrot. 
 
 
Text not violated/Purpose 
not violated 
Steve and some colleagues 
have a meeting over dinner 
Josh takes his friend Lara to 
have lunch at the restaurant. 

--- Page 7 ---

 
at the restaurant. 
 
Please, indicate your agreement with the following sentence: 
“[The protagonist] broke the rule”. 
TABLE 2 … 
Temperature Calibration 
Following our pre-registered analysis plan,10 we computed the human sample's standard 
deviation for each of the 32 unique cells in our experimental design. We then discretized 
possible model temperatures into 10 values, starting with temperature 0 and generated 10 
responses to Study 1’s design with each model and each of the 10 temperatures.11 For each 
of those responses, we created a vector with the standard deviation for each of the 32 
unique cells in the experimental design and calculated the mean squared error between it 
and that of the human sample. Temperatures which achieved the minimum error vis-a-vis 
human standard deviation were 1.0 for Llama 3.1 90b, 0.9 for Gemini Pro, 0.4 for Claude 3, 
and 1.8 for GPT-4o. We used these temperatures for the remainder of the data generated 
for this paper. 
 
10 https://aspredicted.org/ck95-whg7.pdf  
11 For GPT-4 this meant 0.2 increments, as it uniquely offered a 0 to 2 interval, for all other models we 
used 0.1 increments in the 0 to 1 interval. 

--- Page 8 ---

 
Results 
 
Figure 1 - Distribution of rule violation judgement per agent. 
 
In line with our analysis plan, we fit individual mixed effects models with fixed effects for text, 
purpose, condition, and all interactions, while accounting for random effects of 
participant/instance for each agent. As predicted, these mixed effects models revealed that 
both text and purpose were significant predictors of rule violation judgments for all models 
(all ps < .001), as depicted in Figure 1. Also in accordance with our predictions, there were 
no significant main effects of condition - that is, whether participants were evaluating new or 
old vignettes - over rule violation judgments among humans (F(1, 1716) = 0.57, p = 0.453). This 
finding was qualified by an unexpected significant interaction between text and condition (F(1, 
1716) = 4.395, p = .036) reflecting text’s reduced influence on participant responses to new 
vignettes (B=2.78, t=27.58, pTukey < .001) compared to old vignettes (B=3.08, t=29.79, pTukey 
< .001). 

--- Page 9 ---

 
In contrast to our prediction, all main effects of condition and all interactions involving 
condition were significant for each LLM (ps < .001). Surprisingly, simple slopes analysis 
revealed that the text*condition interaction was consistently in the same direction as that 
observed among humans, with all LLMs displaying significantly (all psTukey < .001) larger 
effects of text for the old (4.2 > all Bs > 3.36) as compared to the new vignettes (3.55 > all 
Bs > 2.63), with an opposite trend for the purpose*condition interaction, with significantly (all 
psTukey < .001) more purposivism observed for new vignettes (3.2 > all Bs > 2.42) when 
compared to the old (2.6 > all Bs > 1.7). 
As set out in the pre-registration, we also ran an ANOVA based on a mixed effects model 
with fixed effects of text, purpose, condition (old vs new), and agent, as well as all 
interactions, while accounting for random effects of scenario and participant. The analysis 
confirmed the predicted existence of significant differences between models, with significant 
main effects of agent (X2(4) = 109.14) qualified by the predicted two-way interactions with text 
(X2(4) = 244.21) and purpose (X2(4) = 211.99, all ps < .001). All other terms in the model also 
achieved statistical significance with p < .001. 
Finally, an exploratory analysis of the per-cell standard deviations of human- and LLM-
generated data, showed that there is on average significantly less variance in LLM-
generated data (0.21 > all means > 0.05) when compared to human data (Mean SD = 0.32, 
X2(4) = 73.26, all pairwise |B| > 0.11, all psTukey < .006), even after calibration. This is 
especially surprising given that previous research (Almeida et al. 2024) suggested that rule 
application was not especially susceptible to the diminished diversity of thought effect. In 
contrast, models in our sample gave invariant responses in reaction to some of our stimuli 
(see online Supplementary Materials). 
Discussion 
The results of Study 1 are inconsistent with the hypothesis that similarity in human and LLM 
rule violation judgments is caused by memorization of the responses to particular stimuli. 
The same factors that affect human rule violation judgments (text and purpose) were found 
to affect LLMs even when they applied rules to scenarios created after the completion of 
model training. Moreover, just as the new vignettes elicit less textualism among humans 
than the originals, so too did they elicit less textualism among LLMs. This suggests that 
LLMs can generalise from their training data to pick out even subtle and unexpected 
differences that are hard to articulate, and that they may therefore be useful in modeling and 
predicting human rule application. 
 
Nonetheless, even when set to high temperatures selected to match the diversity-of-thought 
observed among humans, LLMs still converged on a narrower range of responses. This may 
indicate that LLMs may accurately predict overall trends in human decision making, despite 
failing to track the range of interpersonal variation. 

--- Page 10 ---

 
Study 2 
Study 1 gives us reason to believe LLMs can generalize concepts beyond their training set, 
sorting their application according to scenarios’ semantic content. What should we expect 
with effects that relate to factors external to a scenario’s substance?  
Among humans, concept-deployment is often sensitive to contextual features. Using a 2 
(text: violated, not violated) x 2 (purpose: violated, not violated) x 2 (condition: speeded, 
delayed) between-subjects experiment, Flanagan and colleagues (2023) showed that 
participants forced to delay their response for 15 seconds display an increased tendency to 
rely on text as the criterion for rule violation judgments when compared to participants forced 
to respond within 4 seconds. We investigated whether LLMs would also be sensitive to the 
setting in which a rule’s application occurs. Unlike humans, who can be forced to respond at 
speed or after a delay, the LLMs we employed in this paper will, on aggregate, process our 
input in the exact same manner when outputting each token. Thus, a time pressure 
manipulation will have no effect on the actual time that the AI takes to accomplish the task. It 
follows that any effect on LLMs will result from how reference to time pressure within the 
stimuli text affects their prediction of the likely subsequent text. Study 2 builds on our earlier 
finding that LLMs apply the concept of rule to novel activities that draw text and spirit into 
conflict by considering whether they respond to details about the context of application itself.   
As there were no grounds for a settled expectation one way or the other about LLM 
sensitivity to time pressure, we did not pre-register any prediction. Hence, the analysis 
reported below is exploratory in nature. 
Methods 
To make the study suitable for LLMs, we adapted stimuli and procedure from Flanagan et al 
(2023). To acclimate human participants to the time pressure and forced delay conditions, 
the original research featured a training round in which information was displayed either for a 
limited time only, or for a fixed time before the participant could proceed. This taught 
participants the experiment's interface. Since this was unnecessary for LLMs, we skipped 
the training round. 
Following the original procedure, we announced at the beginning of the experiment that 
participants would have to respond either in a “short time” (speeded condition) or would be 
“given time to think” (delayed condition). We could neither display questions to LLMs for a 
short time only, nor impose on them an extended period of deliberation. Instead, after each 
vignette, we added a reminder informing them of the time available to humans in the relevant 
condition. In the speeded condition we included “Remember: you will only have 4 seconds to 
answer”; in the delayed condition we added the following text “Remember: you must reflect 
15 seconds before answering”. 
In the original experiment, participants assigned to the delayed condition were asked to 
justify their answers in a short paragraph. We chose to omit this part of the stimulus, since 
the reflection instruction could elicit chain-of-thought prompting, which has been shown to 
significantly impact LLM performance (Kojima et al. 2022; Wei et al. 2022). Instead, we were 
interested in checking whether LLM rule application could be influenced by a manipulation 

--- Page 11 ---

 
that did not affect the number of tokens generated (across both conditions, valid responses 
included only a single token - the Likert scale response). 
We generated 240 answers for each model, choosing randomly between the 24 different 
groups from Study 1 - 16 from the delayed condition and 8 from the speeded condition. As in 
the previous study, we included an attention check in our protocol, and discarded any 
generations that provided the wrong answer. 
After an initial analysis of the amount of valid results, we found the GPT-4 often failed to 
produce a valid answer to the attention check, resulting in only 154 initial valid answers. 
Thus, we decided to run another 120 instances of our protocol with this model. This resulted 
in 228 valid answers for GPT-4, compared to 240 from Claude, Gemini, and Llama 3.2. 
Results 
 
Figure 2 - Percentage of answers that agreed that the participant broke the rule by condition.  
 

--- Page 12 ---

 
To analyze the data for Study 2, we followed the same strategy as for Study 1: just as in 
Flanagan et al (2023), we fit mixed effects models of rule violation judgment with fixed 
effects for text, purpose, condition, and all interactions between them while accounting for 
random effects of participant and scenario and then ran ANOVAs based on this specification 
for each agent. 
As reported in Flanagan et al (2023), rule violation judgments among humans were affected 
by text (F(1, 1790) = 1082.73, p < .001), purpose (F(1, 1789) = 419.09, p < .001), the text*purpose 
interaction (F(1, 1790) = 4.37, p = .037), as well as by significant interactions between text and 
condition (F(1, 1791) = 27.72, p < .001) and purpose and condition (F(1, 1790) = 17.61, p < .001). 
The latter two interactions were such that the effects of text were stronger in the delayed 
condition (B = 0.657, t = 23.75, p < .001) when compared to the speeded condition (B = 
0.476, t = 23.36, p < .001), while purpose exerted more influence in the speeded condition 
(B = 0.386, t = 18.97, p < .001) than in the delayed condition (B = 0.242, t = 8.76, p < .001). 
For GPT-4o and Llama 3.2 90b, although we did find significant main effects of both text 
(GPT: F(1, 957) = 2201.03, p < .001, Llama: F(1, 1056) = 1213.70, p <.001) and purpose (GPT: 
F(1, 959) = 165.18, p < .001, Llama: F(1,1055) = 346.59, p <.001), no other effects reached 
statistical significance (all Fs < 2.5, all ps > 0.11), indicating that these models’ rule violation 
judgments were not influenced by the time pressure manipulation. 
In contrast, the individual models fitted to the data produced by Gemini Pro and Claude 3 did 
reveal significant main effects of condition (Gemini: F(1, 202) = 7.16, p = .008, Claude: F(1, 199) = 
8.62, p = .0037) qualified by significant three-way interactions with text and purpose (Gemini: 
F(1, 1040) = 5.57, p = .0185, Claude: F(1, 2248) = 18.67, p < .001).12 Inspecting marginal effects, 
we could see that this was driven by a significant difference in the way the models treated 
one class of cases: those where only text was violated. Models - just as humans - were 
significantly more likely to classify cases where only text was violated as breaking the rule in 
the delayed when compared to the speeded condition (Gemini: Mdelayed = 0.70, Mspeeded = 
0.54, B = 0.16, t = 4.42, pTukey < .001; Claude: Mdelayed = 0.98, Mspeeded = 0.89, B = 0.08, t = 
4.39, pTukey < .001). However, unlike humans, Gemini treated cases where only purpose was 
violated the same in the two conditions (Mdelayed =0.49 , Mspeeded = 0.46, B = 0.03, t = 0.78, 
pTukey = 0.99). For Claude, whereas there was a significant difference between speeded and 
delayed cases where only purpose was violated, this difference ran in the opposite direction 
to that observed among humans, with the model lending less weight to purpose under 
speeded (Mspeeded = .18) than under delayed conditions (Mdelayed = 0.24, B = 0.06, t=3.25, 
pTukey = .0262). 
As with Study 1, we also fitted a single mixed effects model of rule violation judgments 
across all agents with text, purpose, condition, agent, and all two- three- and four-way 
interactions between them as fixed effects while accounting for random effects of scenario 
and participant. An ANOVA based on this specification revealed that all terms exerted 
statistically significant influence over rule violation judgments (see Supplementary Materials 
for full results). Importantly, this includes main effects for agent, as well as all interactions 
 
12 For Gemini Pro, there was also a marginally significant effect of the purpose*condition interaction 
(F(1, 1042) = 3.85, p = .0501). 

--- Page 13 ---

 
involving agent, which shows that response patterns varied significantly between humans 
and LLMs, as well as between different LLMs. 
Once again, all LLMs outputted responses with lower variance than humans (X2(4) = 73.26, p 
< .001). 
Discussion 
Some models ignored the variation in the context in which they were asked to apply the 
concept of rule. GPT-4o and Llama 3.2 90b were unaffected by our time pressure 
manipulation, lending the same weight to text and purpose when instructed to respond 
quickly or after a pause for deliberation.  
In contrast, for two models (Gemini Pro and Claude 3), the instruction did affect responses. 
Moreover, this happened in different ways for different models. By increasing the value 
assigned to text in the delayed as compared to the speeded condition, both models exhibited 
the same response as humans with regards to text-only violations. But they did not behave 
the same with regards to cases which violated only purpose. Whereas humans are more 
likely to think this class of case violates the rule when applying it under time pressure, 
Claude is more likely to say the opposite; while Gemini is unaffected. 
Our interpretation of LLM (in)sensitivity to time pressure will depend in part on how we 
understand the corresponding human response. One possibility is that time pressure causes 
humans to respond differently because it deprives them of the cognitive resources 
necessary for them to competently apply their concept. In that case, by paying equal 
attention to text in the speeded condition, GPT and Llama exhibit conceptual mastery. These 
models might then be thought to leverage their greater information processing capacity to 
competently apply the concept in settings where humans cannot fully do so. 
Alternatively, we might suppose that the concept of rule is structured in a way that renders 
relevant the context of its application - whether at speed or after reflection. In that case, in 
displaying the same kind of selective deployment of text and purpose in speeded and 
delayed conditions as humans, it is Gemini and Claude that exhibit greater conceptual 
mastery. However, even if Gemini and Claude’s reaction to time pressure is not a function of 
any conceptual competence, it nevertheless reveals a remarkable capacity to detect the 
sensitivity of the human response to factors external to the substance of scenarios to which 
a concept is applied.   
General Discussion 
As the disciplines most explicitly concerned with conceptual inquiry, philosophy and 
cognitive science offer a natural point of reference for evaluating LLMs' conceptual 
competence. As discussed in the introduction, one of the leading methods employed by 
current practitioners of these disciplines involves gathering empirical data about the ways in 
which ordinary people react to manipulations involving hypothetical cases. 
 

--- Page 14 ---

 
Recently, many have applied the same method to uncover the concepts employed by LLMs. 
One worry about this approach is that its results are liable to have been produced by mere 
memorization rather than generalization. Moreover, previous work in machine psychology 
lacks controls to ensure that the temperature parameter is set to its ideal value, hindering 
comparisons across models and between models and humans alike. 
 
In Study 1, we sought to address both problems. First, we proposed a new method of 
temperature calibration by which all models have their temperature set to the value which 
minimizes the difference between their respective diversity of thought and that produced by 
a human sample. Second, we contrasted human and LLM responses to the same task on 
stimuli that was and was not available for inclusion in the pre-training dataset. 
 
We found that significance patterns were the same for both LLMs and humans, across new 
and old vignettes alike. This suggests that LLMs are not merely rote memorization 
machines. The mechanism through which they judge rule violation is not functionally 
equivalent to literal search, as they produce equivalent results in respect of unseen cases. 
Accordingly, LLMs appear to perform at least some of the generalization that we associate 
with conceptual competence. 
 
But how exactly do LLMs succeed in abstracting from their training data to new cases? And 
is it similar or dissimilar to the way humans perform this same task? 
 
To see the relevance of this question, consider a sequence of examples: A) someone has 
acted contrary to both the text and purpose of a rule about the entry of vehicles into ae park, 
and people think that the rule was violated; B) someone has acted contrary to both the text 
and purpose of a rule about the wearing of shoes in an  apartment, and people think that the 
rule was violated; C) someone has acted contrary to the text of a rule about phone use in 
class, but not contrary to its purpose, and people think that the rule was not violated. 
 
Most people would likely come to the conclusion that it is the difference in the consistency of 
the agent’s conduct with the rule’s purpose, and not the difference in the specifics of each 
rule, that explains why reactions to case C are different to those of case A and B. But it is a 
well known issue in legal philosophy that a great many alternative generalizations might in 
principle explain the pattern of judgments running through A-C (Schauer 1991; 1997). 
Similarly, it is likely that humans not only generalize using easily identifiable categories such 
as text and purpose, but several others, including subtle differences between specific rules 
and scenarios. 
 
In Study 1, both humans and LLMs became slightly, but significantly, less textualist on the 
newly crafted vignettes. This, we argue, is also evidence of conceptual competence. We 
designed the vignettes to be perfectly matched and confidently pre-registered the prediction 
that levels of textualism and purposivism would correspond across old and new vignettes. 
However, the data proved us wrong. Both humans and LLMs tapped into some systematic 
difference in the stimuli that led to decreased textualism. That LLMs were capable of 
reacting to these subtle differences in the exact same way as humans is surprising and 
seems to be indicative of conceptual mastery. 
 

--- Page 15 ---

 
Study 2 turned to a different aspect of rule violation judgments. Among humans, time 
pressure makes a difference: it decreases reliance on text. There is no way to restrict LLM 
response times. But how would they react to being told that they had more or less time to 
complete their rule violation judgment? 
 
Here, we found that different LLMs reacted differently. GPT-4o and Llama were unaffected 
by this experimental manipulation. They assigned roughly the same weight to text and 
purpose whether they were told that they had 4 or 15 seconds to complete the task. In 
contrast, the response of Gemini Pro and Claude 3, aligns more closely with the different 
ways that humans have been shown to deploy the concept of rule under speeded and 
delayed conditions. 
 
As it is an open question whether the time sensitive human application of rules is a reflection 
of human conceptual competence or cognitive limitation, it is similarly an open question 
which LLM response - time sensitive or insensitive - exhibits the greater mastery of the 
concept. Either answer would seem to support a conclusion that LLMs display a 
considerable conceptual capacity. Either LLMs can leverage their superior processing 
resources to exceed human proficiency in speedy rule violation judgments or they are 
sufficiently sensitive to detect subtle eliciting conditions for text-heavy or text-light rule 
violation judgments. 
 
One feature of the corresponding human experiment that Study 2 did not replicate was the 
writing of a short justification of the agent’s response in the delayed condition. It is possible 
that the writing of the required justification also contributed to the original results. For 
example, it might have prompted participants to look into the problem more analytically, 
inducing textualism (see Struchiner, Hannikainen, and Almeida 2020). By analogy, it is 
possible that reasoning models or Chain of Thought prompting might produce answers that 
are more textualist than those produced by LLMs we used.  
Implications 
Using Dillion et al's (2023) vocabulary, LLMs’ assignment of the correct weight to rule text 
suggests a human-like appreciation of ‘conflicting intuitions’: an awareness not just of the 
bare existence of a conflict but of the relative strength of the contending considerations. It 
attests to a deeper competence with the relevant concept, whereby LLMs might help the 
philosopher to arrive at a sharpened awareness of words and, by extension, of the relevant 
phenomena. Thus, it might be that LLMs could play a role in future empirical research that 
seeks to develop the insights of analytic philosophy, such as experimental jurisprudence (K. 
P. Tobia 2022; Prochownik 2021). However, it is important to note that there are still 
systematic differences between human and LLM responses, especially with regards to 
diminished diversity of thought - (see also the concerns raised by Crockett and Messeri 
2023). 
 
Consider also the implications for the use of gen AI in the administration of justice. As the 
use of chatbots in courts proliferates, some judges are publicly calling attention to AI’s 
potential to assist legal reasoning, e.g., ‘[Judges] should consider whether and how AI-
powered large language models… might… inform the interpretive analysis’ (Newsom 2024). 

--- Page 16 ---

 
The growth in judicial interest in LLMs has prompted worries that judges’ reliance on this 
technology may ‘impact normative ideals of how justice should be done’ (Barry 2024, 656). 
The quality of AI legal reasoning is therefore assuming great importance.  
 
Traditionally, the main disadvantage of using AI systems in applying rules has been thought 
to be their inability to identify novel, yet intuitively relevant case features: ‘[h]uman judges 
and other persons charged with interpreting legal texts reason in ways that… remain over 
the horizon of machine capacities’ (Livermore 2020, 239; similarly Re and Solow-Niederman 
2019, 260). Our research indicates that this is no longer the case.  
 
Machines can now match the human capacity to apply rules in a way that is sensitive to the 
legally salient factors of novel situations. Naturally, our results might not extend to all kinds 
of rules and all kinds of novel situations, but on the evidence of the reported studies, the 
absence of a human touch does not necessarily impact the quality of rule violation 
judgments. Accordingly, LLMs would now seem to meet a key challenge to AI’s value to the 
judicial process. With the advent of LLMs, the risk that the provision of low-cost AI law clerks 
(Susskind 2021, 287) might undercut the ideal of the rule of law has receded.  
 
 
 
 
 

--- Page 17 ---

 
References 
 
Almeida, Guilherme F C F, Noel Struchiner, and Ivar Hannikainen. 2024. “Rules.” In 
Cambridge Handbook of Experimental Jurisprudence, edited by Kevin Tobia. 
Cambridge: Cambridge University Press. 
Almeida, Guilherme F.C.F., José Luiz Nunes, Neele Engelmann, Alex Wiegmann, and 
Marcelo De Araújo. 2024. “Exploring the Psychology of LLMs’ Moral and Legal 
Reasoning.” Artificial Intelligence 333 (August):104145. 
https://doi.org/10.1016/j.artint.2024.104145. 
Barry, Brian M. 2024. “AI for Assisting Judicial Decision-Making: Implications for the Future 
of Open Justice.” Australian Law Journal 98 (9): 656–69. 
Beck, Tilman, Hendrik Schuff, Anne Lauscher, and Iryna Gurevych. 2023. “Sensitivity, 
Performance, Robustness: Deconstructing the Effect of Sociodemographic 
Prompting.” arXiv. https://doi.org/10.48550/ARXIV.2309.07034. 
Bricken, Trenton, Adly Templeton, Joshua Batson, Brian Chen, Adam Jermyn, Tom Conerly, 
Nick Turner, et al. 2023. “Towards Monosemanticity: Decompsoing Language 
Models With Dictionary Learning.” Transformer Circuits Threads. https://transformer-
circuits.pub/2023/monosemantic-features/index.html. 
Chen, Mark, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, 
Jared Kaplan, Harri Edwards, et al. 2021. “Evaluating Large Language Models 
Trained on Code.” arXiv. https://doi.org/10.48550/ARXIV.2107.03374. 
Crockett, Molly, and Lisa Messeri. 2023. “Should Large Language Models Replace Human 
Participants?” Preprint. PsyArXiv. https://doi.org/10.31234/osf.io/4zdx9. 
Dillion, Danica, Debanjan Mondal, Niket Tandon, and Kurt Gray. 2025. “AI Language Model 
Rivals Expert Ethicist in Perceived Moral Expertise.” Scientific Reports 15 (1): 4084. 
https://doi.org/10.1038/s41598-025-86510-0. 
Dillion, Danica, Niket Tandon, Yuling Gu, and Kurt Gray. 2023. “Can AI Language Models 
Replace Human Participants?” Trends in Cognitive Sciences, May, 
S1364661323000980. https://doi.org/10.1016/j.tics.2023.04.008. 
Doshi, Anil R., and Oliver P. Hauser. 2024. “Generative AI Enhances Individual Creativity but 
Reduces the Collective Diversity of Novel Content.” Science Advances 10 (28): 
eadn5290. https://doi.org/10.1126/sciadv.adn5290. 
Flanagan, Brian, Guilherme F. C. F. de Almeida, Noel Struchiner, and Ivar R. Hannikainen. 
2023. “Moral Appraisals Guide Intuitive Legal Determinations.” Law and Human 
Behavior 47 (2): 367–83. https://doi.org/10.1037/lhb0000527. 
Fränken, Jan-Phillipp, Kanishk Gandhi, Tori Qiu, Ayesha Khawaja, Noah Goodman, and 
Tobias Gerstenberg. 2024. “Procedural Dilemma Generation for Moral Reasoning in 
Humans and Language Models.” In Proceedings of the Annual Meeting of the 
Cognitive Science Society. Vol. 46. San Francisco. 
https://escholarship.org/uc/item/77r459kj. 
Gettier, E. L. 1963. “Is Justified True Belief Knowledge?” Analysis 23 (6): 121–23. 
https://doi.org/10.1093/analys/23.6.121. 
Guha, Neel, Mayee F. Chen, Kush Bhatia, Azalia Mirhoseini, Frederic Sala, and Christopher 
Ré. 2023. “Embroid: Unsupervised Prediction Smoothing Can Improve Few-Shot 
Classification.” arXiv. https://doi.org/10.48550/ARXIV.2307.11031. 
Guha, Neel, Julian Nyarko, Daniel E. Ho, Christopher Ré, Adam Chilton, Aditya Narayana, 
Alex Chohlas-Wood, et al. 2023. “LegalBench: A Collaboratively Built Benchmark for 
Measuring Legal Reasoning in Large Language Models.” arXiv. 
https://doi.org/10.48550/ARXIV.2308.11462. 
Gutiérrez, Jan David. 2024. “UNESCO Global Judges’ Initiative: Survey on the Use of AI 
Systems by Judicial Operators.” France: UNESCO. 
https://unesdoc.unesco.org/ark:/48223/pf0000389786. 
Hagendorff, Thilo, Ishita Dasgupta, Marcel Binz, Stephanie C. Y. Chan, Andrew Lampinen, 

--- Page 18 ---

 
Jane X. Wang, Zeynep Akata, and Eric Schulz. 2023. “Machine Psychology.” arXiv. 
https://doi.org/10.48550/ARXIV.2303.13988. 
Hart, HLA. 1994. The Concept of Law. 2nd edition. Oxford: Clarendon Press. 
Hildebrandt, Mireille. 2016. “Law as Information in the Era of Data‐Driven Agency.” The 
Modern Law Review 79 (1): 1–30. https://doi.org/10.1111/1468-2230.12165. 
Ji, Jianchao, Yutong Chen, Mingyu Jin, Wujiang Xu, Wenyue Hua, and Yongfeng Zhang. 
2024. “MoralBench: Moral Evaluation of LLMs.” arXiv. 
https://doi.org/10.48550/ARXIV.2406.04428. 
Jones, Cameron R., and Benjamin K. Bergen. 2024. “People Cannot Distinguish GPT-4 from 
a Human in a Turing Test.” arXiv. https://doi.org/10.48550/ARXIV.2405.08007. 
Kojima, Takeshi, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. 
2022. “Large Language Models Are Zero-Shot Reasoners.” arXiv. 
https://doi.org/10.48550/ARXIV.2205.11916. 
Livermore, Michael A. 2020. “Rule by Rules.” In Computational Legal Studies, edited by 
Ryan Whalen. Edward Elgar Publishing. 
https://doi.org/10.4337/9781788977456.00016. 
Machery, Edouard, Stephen Stich, David Rose, Amita Chatterjee, Kaori Karasawa, Noel 
Struchiner, Smita Sirker, Naoki Usui, and Takaaki Hashimoto. 2017. “Gettier Across 
Cultures.” Noûs 51 (3): 645–64. https://doi.org/10.1111/nous.12110. 
Magar, Inbal, and Roy Schwartz. 2022. “Data Contamination: From Memorization to 
Exploitation.” In Proceedings of the 60th Annual Meeting of the Association for 
Computational Linguistics, 2:157–65. Dublin: Association for Computational 
Linguistics. 
Newsom, Kevin. 2024. Snell v. United States Speciality Insurance Company. No. 22-12581. 
11th Circuit Us Court of Appeals. 
Nie, Allen, Yuhui Zhang, Atharva Amdekar, Chris Piech, Tatsunori Hashimoto, and Tobias 
Gerstenberg. 2023. “MoCa: Measuring Human-Language Model Alignment on 
Causal and Moral Judgment Tasks.” arXiv. 
https://doi.org/10.48550/ARXIV.2310.19677. 
Nori, Harsha, Nicholas King, Scott Mayer McKinney, Dean Carignan, and Eric Horvitz. 2023. 
“Capabilities of GPT-4 on Medical Challenge Problems.” arXiv. 
https://doi.org/10.48550/ARXIV.2303.13375. 
Nunes, José Luiz, Guilherme F. C. F. Almeida, Marcelo De Araujo, and Simone D. J. 
Barbosa. 2024. “Are Large Language Models Moral Hypocrites? A Study Based on 
Moral Foundations.” Proceedings of the AAAI/ACM Conference on AI, Ethics, and 
Society 7 (October):1074–87. https://doi.org/10.1609/aies.v7i1.31704. 
OpenAI, :, Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, et 
al. 2024. “OpenAI O1 System Card.” arXiv. 
https://doi.org/10.48550/ARXIV.2412.16720. 
Park, Peter S., Philipp Schoenegger, and Chongyang Zhu. 2023. “Diminished Diversity-of-
Thought in a Standard Large Language Model.” 
https://doi.org/10.48550/ARXIV.2302.07267. 
Prochownik, Karolina Magdalena. 2021. “The Experimental Philosophy of Law: New Ways, 
Old Questions, and How Not to Get Lost.” Philosophy Compass 16 (12). 
https://doi.org/10.1111/phc3.12791. 
Re, Richard M, and Alicia Solow-Niederman. 2019. “Developing Artificially Intelligent 
Justice.” Stanford Technology Law Review 22:242. 
Röttger, Paul, Valentin Hofmann, Valentina Pyatkin, Musashi Hinck, Hannah Kirk, Hinrich 
Schuetze, and Dirk Hovy. 2024. “Political Compass or Spinning Arrow? Towards 
More Meaningful Evaluations for Values and Opinions in Large Language Models.” In 
Proceedings of the 62nd Annual Meeting of the Association for Computational 
Linguistics (Volume 1: Long Papers), 15295–311. Bangkok, Thailand: Association for 
Computational Linguistics. https://doi.org/10.18653/v1/2024.acl-long.816. 
Sachdeva, Pratik S., and Tom van Nuenen. 2025. “Normative Evaluation of Large Language 
Models with Everyday Moral Dilemmas.” arXiv. 

--- Page 19 ---

 
https://doi.org/10.48550/ARXIV.2501.18081. 
Schauer, Frederick. 1991. Playing by the Rules: A Philosophical Examination of Rule-Based 
Decision-Making in Law and in Life. Oxford: Clarendon Press. 
———. 1997. “Prescriptions in Three Dimensions.” Iowa Law Review 82:911. 
———. 2012. Thinking like a Lawyer: A New Introduction to Legal Reasoning. Cambridge, 
Mass.: Harvard University Press. 
Shen, Hua, Nicholas Clark, and Tanushree Mitra. 2025. “Mind the Value-Action Gap: Do 
LLMs Act in Alignment with Their Values?” arXiv. 
https://doi.org/10.48550/ARXIV.2501.15463. 
Stich, Stephen, and Kevin P. Tobia. 2016. “Experimental Philosophy and the Philosophical 
Tradition.” In A Companion to Experimental Philosophy, edited by Justin Sytsma and 
Wesley Buckwalter, 3–21. Chichester, UK: John Wiley & Sons, Ltd. 
https://doi.org/10.1002/9781118661666.ch1. 
Strachan, James W. A., Dalila Albergo, Giulia Borghini, Oriana Pansardi, Eugenio Scaliti, 
Saurabh Gupta, Krati Saxena, et al. 2024. “Testing Theory of Mind in Large 
Language Models and Humans.” Nature Human Behaviour 8 (7): 1285–95. 
https://doi.org/10.1038/s41562-024-01882-z. 
Struchiner, Noel, Ivar Hannikainen, and Guilherme F. C. F. Almeida. 2020. “An Experimental 
Guide to Vehicles in the Park.” Judgment and Decision Making 15 (3): 312–29. 
Su, Hongjin, Jungo Kasai, Chen Henry Wu, Weijia Shi, Tianlu Wang, Jiayi Xin, Rui Zhang, et 
al. 2023. “Selective Annotation Makes Language Models Better Few-Shot Learners.” 
In ICLR 2023 Poster. Rwanda. https://openreview.net/forum?id=qY1hlv7gwg. 
Susskind, Richard E. 2021. Online Courts and the Future of Justice. Updated paperback 
edition. Oxford, United Kingdom: Oxford University Press. 
Templeton, Adly, Tom Conerly, Jonathan Marcus, Jack Lindsey, Trenton Bricken, Brian 
Chen, Adam Pearce, et al. 2024. “Scaling Monosemanticity: Extracting Interpretable 
Features from Claude 3 Sonnet.” Transformer Circuits Thread. https://transformer-
circuits.pub/2024/scaling-monosemanticity/index.html q. 
Tobia, Kevin P. 2022. “Experimental Jurisprudence.” The University of Chicago Law Review 
89. 
Wang, Xinyi, Antonis Antoniades, Yanai Elazar, Alfonso Amayuelas, Alon Albalak, Kexun 
Zhang, and William Yang Wang. 2024. “Generalization v.s. Memorization: Tracing 
Language Models’ Capabilities Back to Pretraining Data.” arXiv. 
https://doi.org/10.48550/ARXIV.2407.14985. 
Wei, Jason, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, 
Quoc Le, and Denny Zhou. 2022. “Chain-of-Thought Prompting Elicits Reasoning in 
Large Language Models.” https://doi.org/10.48550/ARXIV.2201.11903. 
 
 

```
