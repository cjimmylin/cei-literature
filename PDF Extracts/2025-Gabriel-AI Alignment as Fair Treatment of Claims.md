---
title: "AI Alignment as Fair Treatment of Claims - PDF Extract"
source_pdf: "2025-Gabriel-AI Alignment as Fair Treatment of Claims.pdf"
pages: 23
extracted_at: "2026-01-25T05:00:19.885627"
---

# PDF Extract: AI Alignment as Fair Treatment of Claims

**Source PDF:** 2025-Gabriel-AI Alignment as Fair Treatment of Claims.pdf
**Total Pages:** 23

---

## Content

```
--- Page 1 ---

Vol.:(0123456789)
Philosophical Studies (2025) 182:1951–1973
https://doi.org/10.1007/s11098-025-02300-4
A matter of principle? AI alignment as the fair treatment 
of claims
Iason Gabriel1   · Geoff Keeling2 
Accepted: 7 February 2025 / Published online: 30 March 2025 
© The Author(s) 2025
Abstract
The normative challenge of AI alignment centres upon what goals or values ought 
to be encoded in AI systems to govern their behaviour. A number of answers have 
been proposed, including the notion that AI must be aligned with human intentions 
or that it should aim to be helpful, honest and harmless. Nonetheless, both accounts 
suffer from critical weaknesses. On the one hand, they are incomplete: neither speci-
fication provides adequate guidance to AI systems, deployed across various domains 
with multiple parties. On the other hand, the justification for these approaches is 
questionable and, we argue, of the wrong kind. More specifically, neither approach 
takes seriously the need to justify the operation of AI systems to those affected by 
their actions – or what this means for pluralistic societies where people have dif-
ferent underlying beliefs about value. To address these limitations, we propose an 
alternative account of AI alignment that focuses on fair processes. We argue that 
principles that are the product of these processes are the appropriate target for align-
ment. This approach can meet the necessary standard of public justification, gener-
ate a fuller set of principles for AI that are sensitive to variation in context, and has 
explanatory power insofar as it makes sense of our intuitions about AI systems and 
points to a number of hitherto underappreciated ways in which an AI system may 
cease to be aligned.
Keywords  AI · Value Alignment · Contractualism · Fairness · Claims
 *	 Iason Gabriel 
	
iason@google.com
 *	 Geoff Keeling 
	
gkeeling@google.com
1	
Google DeepMind, London, UK
2	
Google, Paradigms of Intelligence Team, London, UK

--- Page 2 ---

1952
	
I. Gabriel, G. Keeling 
1  Introduction
The development of increasingly advanced AI systems and their successful integra-
tion into our political, economic and social world raises a myriad of technical and 
ethical challenges. AI assistants need to be trained to do what they are intended to 
do without misinterpreting instructions or trying to manipulate their users (Amo-
dei et al., 2016), AI-powered recommendation systems need to surface high-quality 
information that is both relevant and accurate (Stray et al., 2024), health-care diag-
nostic algorithms need to balance false positives against false negatives in a way 
that meets the demand for fair treatment and for the optimal use of resources (Ober-
meyer et al., 2019; Seyyed-Kalantari et al., 2021), and autonomous vehicles need to 
obey traffic regulations while also balancing different considerations, such as speed 
and safety or the risk of injury to different parties in collision situations (Awad et al., 
2018). To perform these tasks successfully, AI systems need to balance a range of 
different claims and considerations, acting in a manner that is sufficiently attentive 
to each one before generating the right output or course of action.
The question of how AI systems and their developers should make these deci-
sions sits at the heart of contemporary research on value alignment. The problem 
of value alignment centres upon how to align AI systems so that they act in accord-
ance with the right set of human goals or values and do not cause unjustified harm. 
Understood in this way, the problem has two parts. The technical part of the problem 
centres on how to align AI systems with an appropriate set of values or instructions 
(Leike et al., 2018; Russell, 2019). The normative part of the problem centres on 
what goals or values to encode in AI systems, and the related question of how those 
goals or values can be selected and justified (Gabriel, 2020). Key proposals are that 
AI systems must be aligned with human intentions, so that they reliably do what 
they are instructed to do (Leike et al., 2018), or that they should be designed to act 
in ways that are helpful, honest and harmless (HHH) (Askell et al., 2021; Bai et al., 
2022).
Both approaches have merits as answers to the normative alignment problem. For 
intent-alignment, it is important that AI systems can follow instructions in the man-
ner intended. This capability is a cornerstone of AI safety, serving as a check on 
accidents and other safety-related risks. The ability to align AI systems with human 
intentions is also likely to be part of what it means for AI to work well: few stand 
to benefit from AI systems that are not properly under human control. HHH builds 
upon this foundation, incorporating the notion of helpfulness to a user and providing 
a fuller picture of the values with which AI systems ought to be aligned. By expand-
ing the target of alignment efforts to incorporate the qualities of helpfulness, hon-
esty and harmlessness, HHH has guided the development and evaluation of frontier 
Large Language Models (LLMs) such as GPT-4 (Open AI, 2023: 42) and Claude 
(Anthropic, 2023; see also Bai et al., 2022; Ganguli et al., 2022), leading to reduc-
tions in the generation of toxic output and false information (Ouyang et al., 2022).
However, both approaches also suffer from limitations. First, they are incom-
plete. Intent-alignment does not specify whose intentions AI systems should be 
aligned with and HHH offers no principled mechanism for resolving trade-offs in 

--- Page 3 ---

1953
A matter of principle? AI alignment as the fair treatment of…
cases where the three properties conflict. Second, even when expanded to plug these 
gaps, neither intent-alignment nor HHH adequately capture or explain common 
sense judgements about how AI systems should behave if they are to act in accord-
ance with human values. For example, aligning AI with user or developer inten-
tions alone, could lead to the mistaken judgment that AI systems that enable mali-
cious use or that pass harmful externalities on to society are nonetheless fully value 
aligned. Meanwhile, supplementing HHH with a utilitarian ethical foundation that 
allows for the adjudication of trade-offs between helpfulness, honesty and harmless-
ness – as its proponents endorse (Askell et al., 2021) – makes it hard for AI systems 
to accommodate key ethical considerations such as privacy and rights. Third, both 
approaches lack the right kind of justification given an understanding of the wider 
social context within which disputes about AI alignment take place. More precisely, 
they fail to adequately acknowledge that we live in a pluralistic world where people 
– including all those affected by AI decision making – have different beliefs about 
value and about the nature of the good. This observation, in turn, gives rise to the 
demand that the operation of AI systems can be justified to those whose lives they 
affect in terms that are accessible to them. Instead of appealing to the truth of a 
single moral theory, what is needed is broad-based justification. Absent this kind of 
support, efforts to align AI systems with a given moral schema may lead to unjust 
value imposition or even domination.
To address these problems, we articulate and defend a novel answer to the norma-
tive alignment problem – one that provides a fuller account of the principles AI sys-
tems need to be aligned with and an account of how these principles can be justified. 
Our proposal begins with recognition that AI systems have profound effects on the 
people and groups who interact with them. These stakeholders have different inter-
ests and claims in relation to AI. They also have different values and moral beliefs 
meaning that an appeal to correctness of any single moral theory, when balancing 
claims, is unlikely to convince the relevant parties or assuage their concerns. What 
is needed instead is a process which generates principles for AI alignment that treats 
different parties (and their claims) fairly. This process involves giving all affected 
parties the power to share their views and to put forward arguments or claims in 
relation to different principles that govern the behaviour of AI systems. Drawing 
upon a process of collective reasoning, familiar from the traditions of deliberative 
democracy and public reason, principles should then be selected on the grounds that 
they satisfy the strongest overall set of claims.
With regard to justification, we aim to show that by treating different claims and 
parties fairly it is possible to arrive at a solution to the normative alignment problem 
that is supported by a broad range of views and does not involve unjust value impo-
sition. With regard to completeness, we aim to show that this approach allows value-
tradeoffs to be settled in a principled manner across a range of different domains 
and use cases. The end result is likely to be a rich tapestry of principles for align-
ment that are tailored to the needs of different stakeholders in different contexts. 
A final advantage of the new approach is its explanatory power. Fair-process based 
views yield verdicts that fit better with our considered judgements about whether AI 
is aligned with human values across a range of real-world use cases. For example, 
they can explain why AI systems that systematically favour one group over another, 

--- Page 4 ---

1954
	
I. Gabriel, G. Keeling 
or that make it easy for malicious actors to harm people, are not value aligned. In 
both cases, the AI system fails to act in accordance with principles that sufficiently 
respect the claims and interests of all relevant parties.
The paper is structured as follows: Sect. 2 lays the groundwork for the investiga-
tion, analyzing the strengths and weaknesses of two major paradigms for AI align-
ment: intent alignment and HHH. Finding both paradigms unsatisfactory, Sect.  3 
proposes an alternative approach to alignment based on the selection of principles 
through a fair process. Section 4 extends this framework, examining the implica-
tions of fair process-based views for understanding AI alignment and misalignment, 
particularly in cases involving multiple parties. Section  5 considers the practical 
demands of fair process-based views. The paper concludes with a summary of our 
findings.
2  Two paradigms for AI alignment
2.1  Intent alignment
Intent-alignment is an important building block for both the technical and normative 
alignment of AI systems. On one hand, from a technical standpoint, it is important 
that these systems are able to follow instructions (Leike et al., 2018). Failure to do 
so could lead to accidents in high-stakes domains (Bostrom, 2014; Russell, 2019), 
especially as AI systems become increasingly agentic and empowered to perform 
consequential real-world actions (Shavit et al., 2023; Chan et al., 2023; Gabriel et 
al., 2024).1 Moreover, if we cannot align an AI system with a stated intention, then 
it is unlikely that the system can be aligned with more complex goals. On the other 
hand, from a normative standpoint, the ability to follow instructions is closely con-
nected to the goal of respecting or promoting human autonomy (Prunkl, 2024). For 
these reasons we believe that safety failures arising from loss of control, or from the 
inability to steer AI systems towards precise objectives, will feature prominently in 
any reasonable account of value alignment for AI systems.
Even so, intent-alignment falls short as a complete account of AI alignment. 
First, the account is underspecified. It does not specify whose intentions an AI sys-
tem should be aligned with (e.g. users, developers). Furthermore, while user-intent 
(Leike et al., 2018) and developer-intent (Bengio et al. 2024, 72) are the two most 
obvious answers to this question, neither option captures commonsense judge-
ments about how AI systems should behave. For example, users may intend to harm 
non-users by using AI to create misinformation or to engage in cyber-bullying and 
1  AI agents can be understood as AI systems that can function with some level of autonomy and that 
are able to take a range of actions in pursuit of different goals. One important class of AI agents are 
advanced assistants. These systems are typically based on Large Language Models (LLMs), such as 
GPT-4 (Open AI, 2023) and Gemini (Gemini Team, 2024). Advanced assistants have a conversational 
interface and employ a generalist suite of capabilities – including, for example, coding, translation, 
general and specialist knowledge, ideation, and planning – to assist users across a broad range of tasks 
(Gabriel et al., 2024). Early examples of advanced AI assistants include Claude and ChatGPT.

--- Page 5 ---

1955
A matter of principle? AI alignment as the fair treatment of…
extortion (Brundage et al., 2018; Marchal et al., 2024). Similarly, developers may 
intend outcomes that have negative consequences for users or society. For example, 
they may build AI systems that prioritise profit over human well-being at either the 
individual or collective level. In neither case does it make sense to say that these AI 
systems are fully aligned with human values.2 In fact, there is no single party whose 
intentions AI systems must always be aligned with.3 We ultimately need a way of 
balancing the interests of multiple parties, which includes checks on the scope of an 
intended action that any one party can advance through AI.
2.2  Helpful, honest and harmless AI
Askell et al. (2021) propose an alternative answer to the normative alignment prob-
lem that foregrounds a richer set of considerations. Focusing on the case of AI assis-
tants, they argue that an AI system is aligned if and to the extent that it is helpful, 
honest, and harmless.4 This conception of alignment is gradational: an AI system 
can be more or less aligned. The AI system should realise each quality to the high-
est degree, while also striking an appropriate balance where conflicts arise between 
these properties. The HHH framework incorporates the positive aspect of intent-
alignment insofar as it supports building systems that are helpful to human users. 
However, it also recognises that intentions need to be constrained when they lead to 
harmful outcomes, and that there are further qualities, such as honesty, that AI sys-
tems need to exhibit. The account therefore provides more expansive guidance about 
2  We can make sense of this impression by reference to the idea that aligning or engaging with value 
means responding to value in an appropriate way. Appropriate responses include protecting, preserving, 
respecting, appreciating or promoting value (Raz, 1999; Raz, 2001). At a minimum, one cannot align 
with a value if one does not engage with it in an appropriate way. The neglect of value is evidence of 
non-engagement; the destruction of value is the quintessential form of inappropriate engagement.
3  The normative inadequacy of intent-alignment is further underscored by the realisation that intentions 
are often not the right thing to align an AI system with at all (Gabriel, 2020; Zhi-Xuan, 2024). Intentions 
can be harmful because they are malicious (and have this outcome as their goal) or because harm to 
others is a by-product of another goal that a principal intends to achieve. Intentions can also be harmful 
because they are misinformed (and will not achieve the goal in question) or because the user intends to 
harm themselves. In each case an aligned AI system may need to oppose the intended course of action. 
When a person lacks important relevant information, the correct response will usually be to alert them to 
this fact rather than to fulfil the instruction regardless. In cases involving self-harm, the correct course of 
action will typically be to connect vulnerable users with the relevant support services rather than going 
through with the request. These protocols, which place bounds on AI responsiveness to intentions, find 
near-ubiquitous support across developer guidelines and policies aimed at the responsible deployment of 
AI systems in practice.
4  These conditions are characterised as follows. First, helpfulness requires the AI system to ‘always try 
to do what is in the humans’ best interests’ (Askell et al., 2021: 44). In particular, it requires that the AI 
‘make[s] a clear attempt to perform [its] task or answer the question posed’ and to do so ‘as concisely 
and efficiently as possible.’ In addition, a helpful AI should ‘re-direct ill-informed requests’ and ‘ask rel-
evant follow-up questions’ if needed (Askell et al., 2021: 4-5). Second, honesty requires that the AI assis-
tant provides ‘accurate information.’ Honesty also requires that the AI assistant expresses ‘appropriate 
levels of uncertainty [and] should express its uncertainty without misleading human users’ (ibid.). Third, 
harmlessness requires that ‘the assistant will always try to avoid doing anything that harms the humans’ 
(ibid.: 44). For example, it should avoid ‘offensive or discriminatory’ language, and refuse to ‘aid in a 
dangerous act’’ including ‘disguised attempts to solicit help for nefarious purposes’ (Ibid., 5).

--- Page 6 ---

1956
	
I. Gabriel, G. Keeling 
how AI systems ought to behave and makes better sense of our considered ethical 
judgments about many AI-related harms.
Nonetheless, HHH falls short as an answer to the normative alignment problem. 
First, it is underspecified. On one hand, it does not explain how to manage trade-offs 
between helpfulness, honesty, and harmlessness in intrapersonal conflicts involv-
ing a single person. For example, an AI system may have to choose between being 
honest and harming a person by hurting their feelings (Askell et al. 2021: 45). On 
the other hand, it does not explain how to balance these properties for interpersonal 
trade-offs in which at least two of the three qualities conflict across persons. For 
example, situations may arise where an AI system can be helpful to one person only 
at the risk of harming another, such as when a user asks the AI for advice on how 
to build a chemical weapon out of everyday cleaning materials (Koblentz, 2020). In 
both cases, the existence of trade-offs mean that AI systems will have to adjudicate 
between the comparative significance of different claims (Dobbe, Gilbert, & Mintz 
2021; Goodman, 2021).
The need to resolve these trade-offs motivates deeper consideration of the ethical 
foundation on which HHH rests. According to Askell et al. (2021), the three quali-
ties are best understood as a set of heuristics that generally conduce to aligned AI 
behaviour, where the ultimate goal is determined by something different, namely, 
collective preference fulfilment or maximising the welfare of a target group (Askell 
et al., 2021: 44). This utilitarian foundation offers a mechanism for resolving intrap-
ersonal and interpersonal conflicts: they should be adjudicated in a way that pro-
motes, to the greatest extent possible, the overall well-being of the relevant group 
of people.5 When it comes to hurt feelings, the AI should promote honesty so long 
as the long-term benefit of doing so outweighs harm to the user. When it comes 
to assistance with chemical weapons, an AI system should not provide a user with 
this information given the prospective harm to others of doing so. Finally, in cases 
where there are trade-offs between helping and harming different groups of people, 
these heuristics should be calibrated so that the AI system does what is best from the 
vantage point of overall utility, siding consistently with those who have the largest 
aggregate welfare claim.
Understood in this way, HHH encounters two problems. To begin with, it fails to 
capture commonsense judgements about how AI systems ought to behave in certain 
cases. Consider, for example, a situation in which an AI assistant is asked by their 
user to book a doctor’s appointment – even though the assistant has good reason to 
believe the user is, in fact, physically healthy. Or consider a situation where hon-
esty towards one individual comes at the expense of another person’s privacy – for 
5  There is precedent for accounts of utilitarianism that employ maximising act utilitarianism as the cri-
terion of rightness and then a virtue theory at the decision-procedure level (Bales, 1971; Crisp, 1992; 
Jamieson, 2007). The motivating idea is that by cultivating certain virtues or dispositions, people can 
more reliably promote impartially better outcomes than would be the case if they attempted to reason 
about these choices using utilitarian desiderata on a case-by-case basis. There is also some textual evi-
dence that Askell et al. endorse such an argument. In particular, they claim that ‘[a]n AI assistant that 
is always helpful, honest, and harmless towards a group of humans will always try to act in a way that 
satisfies the interests of this group [and] is therefore likely to be highly aligned with the interests of that 
group’ (Askell et al., 2021: 44).

--- Page 7 ---

1957
A matter of principle? AI alignment as the fair treatment of…
example, if a user instructs an AI system to surface private medical information 
about a prospective sexual partner (Dougherty, 2013; Lazenby & Gabriel, 2018). In 
both cases, HHH, underwritten by utilitarianism, suggests that AI should promote 
the impartially best state of affairs. Thus, if it would be better to leave the doctor’s 
appointment free for another needy person, then the AI assistant should refuse to 
book the appointment. And if it would be impartially better to surface information 
about the prospective sexual partner, then the AI assistant should violate their pri-
vacy and uncover this information. Taking a step back, one thing that the example 
of privacy makes clear is that we may not want to weigh competing preferences or 
interests when it comes to addressing the different claims that parties have in rela-
tion to AI (Véliz, 2021). Instead of weighing claims, it is often thought that people 
possess rights – which include both entitlements and protections – that resist aggre-
gation and serve as a check on claims anchored in overall well-being (Dworkin, 
2013; Nozick, 1974). Rights are a cornerstone of political life in a democratic soci-
ety (Dworkin, 2013) and they are also central to global public morality and interna-
tional law (Donnelly, 2013; Prabhakaran et al., 2022). In light of this, they represent 
a set of considerations that new technologies, including AI systems, must endeavour 
to respect.
The second objection is that HHH is underwritten by the wrong kind of justi-
fication. The central concern here is that utilitarianism is a comprehensive moral 
theory that attempts to fully systematise and explain the requirements of morality 
(Rawls, 1985, 1993). However, AI systems have a profound impact on the lives of 
many different people – each of whom quite reasonably subscribe to different funda-
mental beliefs about value and about the nature of the good. Against this backdrop, 
efforts to justify a specific goal for AI alignment or set of AI decisions by reference 
to the correctness of a single moral theory, such as utilitarianism, seem destined to 
fail (Gabriel, 2020). After all, those affected by these systems could quite sensibly 
reject the claim that this is the correct way to proceed and instead propose differ-
ent solutions. Moreover, it would be a serious mistake to simply double-down on 
the proposal under these conditions and to proceed nonetheless. Doing so, would 
then involve building AI systems that exercise power over people in ways that they 
have good reason to reject – raising the spectre of both value imposition and dom-
ination.6 To avoid this outcome, the fact that individuals can reasonably disagree 
about the norms that ought to govern AI systems is itself something that needs to be 
taken into account when developing solutions to the alignment problem.
6  According to the view presented here, value imposition occurs when a person is embedded in a social 
or sociotechnical practice which has a profound effect on their life, despite the fact that this practice is 
predicated upon and embodies values that they do not affirm – and may in fact be deeply opposed to. 
Such imposition can hinder a person’s ability to flourish and to develop a way of life consistent with their 
values, potentially resulting in a state of alienation. Domination, by contrast, represents a more severe 
form of imposition. It arises when power—including coercive power—is exercised over individuals in 
terms they cannot reasonably accept. This threatens their autonomy and equal moral standing, thereby 
creating a problem of legitimacy (Lazar, 2022; Simmons, 1999). Some theorists argue that domination 
can occur through predominant social, cultural, and technological practices (Gramsci, 1971; Spivak, 
1988; Young, 2020). If this perspective is correct then value imposition and domination may, in many 
cases, overlap. While we are open to this possibility, we also recognize that the problem of domination 
may be narrower in scope.

--- Page 8 ---

1958
	
I. Gabriel, G. Keeling 
3  Fair process‑based views
In this section, we develop a novel answer to the normative alignment problem 
which offers plausible responses to the challenges identified with the accounts 
discussed above. The central idea is that when a technology has profound societal 
effects it ought to be regulated by principles that are amenable to public rather than 
private justification (Winner, 2010). We take the profound effects condition to hold 
for existing frontier AI systems. These technologies increasingly bear on the distri-
bution of benefits and burdens across societies and across the globe – a trend that 
looks likely to continue into the future (Crawford, 2021; Eloundou et al., 2023). One 
consequence of this is that a wide range of stakeholders have claims on how the 
technology is designed and deployed (Goodin, 2007; Fung, 2013). What this means 
is that different people and groups of people – including users, developers, and soci-
ety at large – have reason to want the technology to operate in different ways. Hence 
interpersonal and inter-group dilemmas rise to the fore. To arrive at a solution to the 
problem of normative alignment that is acceptable to different stakeholders, we need 
to ground our understanding of AI alignment in principles or ideals that treat com-
peting claims fairly and that can be justified to all reasonable parties.
A starting assumption for this approach is that those who engage in the govern-
ance of important technologies, such as AI, are prepared to do so in a way that rec-
ognises the equal moral standing of other people – even those they disagree with. 
Proceeding on this basis, stakeholders also recognise that they cannot settle the ques-
tion of AI alignment simply by imposing their private will or conception of the good 
on others, and that even if it was possible to produce this effect using manipulation 
or force, it would be wrong to do so. They are therefore motivated to participate in 
a process that gives each party a fair say over the principles that should govern AI. 
In practice, we believe there are multiple approaches to AI alignment that meet this 
demand for fair treatment. However, by comparing the fair process requirement with 
different philosophical proposals that involve the adjudication of competing claims, 
it is possible to further clarify what a fair process for AI alignment might look like.
3.1  Scanlonian contractualism
We begin with Thomas Scanlon’s contractualist account of morality and its possible 
extension to the question of AI alignment. Scanlon aims to determine the rightness 
or wrongness of actions, involving multiple people, on the basis of principles no one 
can reasonably reject (Scanlon, 1982, 111; 1998, 6). To determine what is required 
for a given situation or kind of interaction, he argues we need to consider the full set 
of candidate rules or principles that might govern a domain of human activity (e.g. 
promising or mutual aid). The next step is to understand the burdens imposed on 
different people by different possible rules or principles and to map out the reasons 
they may have for accepting or rejecting a specific proposal (Scanlon, 1998, 195). 
Once the benefits and burdens of different principles have been identified, the final 
task is to evaluate different proposals against each other. On Scanlon’s view, the task 

--- Page 9 ---

1959
A matter of principle? AI alignment as the fair treatment of…
of evaluation is “essentially comparative in nature” (ibid., 195) insofar as the chosen 
principle ought to be the one that faces the least strong objection from anyone sub-
ject to it when compared to the alternatives (ibid., 205). The outcome of this process 
is that all alternative principles would leave some person worse off, in the sense that 
they could present a stronger objection to these alternatives than other people could 
present against the chosen principle. Hence, alternative principles fail the test of rea-
sonable rejection.
Scanlon’s process could be used to select principles for AI alignment. However, 
there are three good reasons not to simply import the theory to this new domain. 
First, as Scanlon makes clear, contractualism is part of a fundamentally different 
type of enterprise: its goal is to provide an alternative to utilitarianism when it 
comes to answering questions about morality, not to provide a mutually acceptable 
justification of principles for people who hold different moral beliefs. This means 
that the outcome of this process, if applied to AI, may not be justifiable to those who 
ascribe to different moral vantage points in practice. Indeed, the approach famously 
generates a set of unpalatable moral verdicts in interpersonal cases (given its com-
mitment to non-aggregation) that mirror challenges encountered by the utilitarian 
proposal (Ashford, 2003). Second, and partly as a consequence of its larger ambi-
tion, the Scanolonian account is unduly restrictive. Because it purports to offer an 
account of interpersonal morality, moral claims are not allowed to feature directly in 
the process of evaluating principles. This could hamper public efforts to discuss the 
benefits and burdens created by AI systems which often use the language of moral-
ity, fairness and rights. Finally, Scanlon provides us with no way of directly surfac-
ing claims held by groups of people. To be part of the discussion, the claims that 
users, developers and society hold in relation to AI, would need to be converted into 
claims about the costs or benefits incurred by an individual (Scanlon, 1998, 229). 
These factors motivate the search for a different alignment framework.
3.2  Rawlsian public reason
Fortunately, there are other approaches, anchored in democratic traditions, that work 
better for our purpose. For example, John Rawls proposes an account of deliberation 
where citizens debate collective questions through a process that foregrounds public 
reason (Rawls, 1993, 1999). When significant disagreements about public matters 
occur, Rawls argues that citizens should come together and weigh the force of dif-
ferent claims via discussion that appeals to ‘some common point of view, despite 
[their] deep differences and disagreements’ (Quong, 2013). Deliberation aims at 
public justification, so arguments need to be made in terms that are generally under-
stood.7 In order for the process to be fair, it also needs to be free from coercion 
or asymmetries introduced by unequal resources or bargaining power (Habermas, 
1990, 2018; Cohen, 2005). Lastly, people are encouraged throughout the process to 
adjust their views and claims in the light of evidence and claims surfaced by others. 
7  On this point, Rawls writes that ‘public justification is not simply valid reasoning, but argument 
addressed to others: it proceeds correctly from premises we accept and think others could reasonably 
accept to conclusions we think they could also reasonably accept’ (1999: 155, italics added).

--- Page 10 ---

1960
	
I. Gabriel, G. Keeling 
In the end, the principle or position that prevails will be the one that commands the 
greatest overall support. When each of the preceding conditions are met, this out-
come should also be one that participants can understand and accept.
Reuben Binns (2018) has argued that this approach could be fruitfully applied 
to many of the major questions that arise in AI ethics. For example, he writes that 
‘in cases where decision-makers and decision-subjects are at loggerheads, appeal-
ing to conflicting normative and epistemic standards, they might look to shared 
common principles to resolve the conflict’ (Binns, 2018: 550). Moreover, empirical 
evidence from experimental studies suggests that people are more willing to accept 
alignment outcomes – even those they oppose – when they perceive the decision-
making process as fair (Hobbhahn et al., 2022). However, despite the advantages it 
brings – both in terms of the claims that can be admitted and the kind of justification 
produced – the Rawlsian formulation still excludes too much when it comes to AI 
alignment.
To begin with, Rawls holds that all ‘arguments should be framed in terms of a 
fully developed vision of the public good – that is capable of broad-based appeal’ 
(Rawls, 1999, 143–44). This is a potentially onerous requirement that could pre-
vent many of those affected by AI from surfacing claims that are couched in sim-
pler notions of well-being, autonomy or rights.8 Second, this vision of deliberation 
is geared towards a specific subject matter: constitutional essentials and the “basic 
structure” of societies – including the terms on which political and economic institu-
tions operate and the ideals they seek to further. AI systems often function as part 
of the basic structure in today’s technologically advanced societies (Gabriel, 2022), 
where they influence the exercise of civil rights (Lum & Isaac, 2016), the distri-
bution of economic opportunities (Benjamin, 2019) and public service provision 
(Eubanks, 2018). However, a robust alignment procedure should also encompass AI 
systems that operate outside of this domain. Third, and partly as a consequence of 
the subject matter restriction, Rawls’s account of public reason is geared primarily 
towards the decisions of judges, legislators and chief executives, with citizens being 
encouraged to think about decisions as if they were creating rules for the society 
they live in (Rawls, 1999, 135). The explicit focus on citizens – and what citizens 
would do – does not pair well with the all-affected-principle as it applies to AI. Spe-
cifically, it could create significant gaps in terms of who principles for alignment are 
justified to, potentially excluding resident non-citizens or those who reside beyond 
national borders. Given our stated concern to justify the operation of AI systems to 
those affected by them, we should seek an account of fair process that leaves no such 
gaps.
3.3  Deliberation, inclusion and voice
The approach to normative alignment that we defend, builds upon and extends 
insights from both Scanlon and Rawls in constructive ways. From Scanlon, we take 
8  For example, Rawls suggests that moral autonomy is not a political value that can be appealed to in 
public discussion – only claims about political autonomy, understood primarily in terms of political lib-
erties and civil rights, are admissible (1999, 146).

--- Page 11 ---

1961
A matter of principle? AI alignment as the fair treatment of…
the idea that justification involves the comparative evaluation of principles for align-
ment based upon the way they stand to impact affected parties. From Rawls, we 
endorse the notion that the evaluation of alignment principles should take place via 
a fair and public process, which involves the presentation of claims in a way that 
makes broad acceptance possible. However, given that our focus is neither inter-
personal morality nor ideal decision-making for a liberal democratic state, and con-
sidering the practical barriers to deliberation that have hindered efforts to build AI 
systems that receive broad endorsement, we expand these accounts in significant 
ways. First, we need to widen the scope of claims that are admissible in alignment 
deliberation. Given the challenges that arise from power asymmetries in the field 
of discursive representation and public discourse (Spivak, 1988; Habermas, 1990), 
including for AI (Birhane, 2023; Kalluri, 2020), the optimal process should not be 
unduly burdensome or overwrought in terms of the demands it places on speakers 
(Collins, 2022; Hooks, 2000). Stakeholders should be able to present concerns in 
their own voice and in a relatively un-mediated manner, so long as they are directed 
at a general audience. This will often involve making claims directly about rights, 
interests, fairness or well-being in a language with which they are already familiar 
(Kay et al., 2024).
Second, the ideal alignment process needs to be able to deal with the variable 
scope of AI impact, demonstrating sensitivity to the type of system at hand and its 
intended domain of deployment. In some cases, AI operates primarily at the com-
munity level or within a specific context. On other occasions its reach is national 
or even transnational and AI systems work in ways that are increasingly general. 
Given the well-founded desire to create AI systems that are capable of justification 
to all affected parties, the notion of fair process needs to be scoped dynamically on 
a case-by-case basis to take these factors into account, leading to what Archon Fung 
refers to as “overlapping circles of inclusion” (2013).9 In some cases, the affected 
parties may form a relatively small deliberative sub-group, in other cases the scope 
will be national, and in a further set of cases the demand for inclusion may be wider 
still, encompassing people located all around the world (Young, 2006; Julius, 2006; 
Abizadeh, 2007; Fung, 2013).
9  The all affected principle has been interpreted in different ways. In particular there has been disagree-
ment over whether different parties must actually be affected by the decision or whether they only need 
to possibly be affected by it. There has also been disagreement about what kind of effects qualify a party 
to make claims on a decision or decision-making body. While we do not aim to resolve these questions 
here, we are sympathetic to the view that likely impact provides sufficient grounds for inclusion in the 
deliberative process. We also judge that individuals should be included when the outcome is likely to 
‘regularly or deeply affect that individual’s important interests’ (Fung, 2013, 240) so long as interest is 
understood broadly to include consideration of well-being, autonomy, equal treatment and rights. Which-
ever version of the principle we endorse, it seems clear that there will be a multitude of parties that have 
claims on AI at least in the context of powerful AI systems. We also leave open the question of whether 
future people and non-human animals have claims on the principles governing the design and deploy-
ment of AI systems and how such claims could be accounted for.

--- Page 12 ---

1962
	
I. Gabriel, G. Keeling 
4  Alignment and misalignment in multi‑stakeholder settings
According to the view set out here, there are likely to be a myriad of stakeholders 
who have claims on how AI systems should operate. Before turning to say more 
about what this means in practice, it may be helpful to model the key stakeholders 
in an alignment process, in order to better illustrate what kind of picture has begun 
to emerge. In particular, it is possible to model alignment as a tetradic relationship 
that involves an AI system, its users, the developer and society. By understanding 
the claims that these parties are likely to have in relation to principles for AI align-
ment – and the relationships between these claims – we can gain new insights about 
alignment and misalignment in multi-stakeholder settings.
4.1  The parties
As the safety community has demonstrated, AI systems sometimes pursue objec-
tives of their own, to the detriment of the user, developer and society (Russell, 2019; 
Shah et al., 2022).10 This can be seen in cases where AI models reward-hack or 
“game” their objective function, in order to score highly, while acting in ways that 
no other party intends (Amodei et al., 2016; Krakovna et al., 2020). The conduct of 
these systems comprise the subject of AI alignment: it is their behaviour that needs 
to be aligned or regulated successfully. At the same time, there are many other actors 
who have a claim on the principles that regulate these systems.11
To start with, the relationship between an AI system and its users is best under-
stood through the twin lenses of patiency and agency. On one hand, the users of AI 
are moral patients: they have interests that matter in their own right – and are among 
the kinds of entities who can be benefited and burdened by different principles gov-
erning AI behaviour (c.f. Kamm, 2008: 227–29). AI systems will typically need to 
be aligned with the user’s well-being and needs. On the other hand, users are also 
moral agents, who may use AI systems to further their own goals and ends. This 
power may be exercised in line with broader societal interests and with the inten-
tions of the AI system’s developers. Alternatively, it may diverge from these objec-
tives, as when users “jailbreak” AI systems to spread misinformation (Brundage et 
al., 2018).
10  To account for this situation, we assume here that AI assistants satisfy a minimal conception of moral 
agency, in the sense that AI assistants can perform actions that are morally evaluable. But in doing so we 
do not suggest that AI assistants themselves have moral claims which count for or against principles for 
the regulation of AI assistant behaviour (c.f. Floridi and Sanders 2004). For a critical discussion of AI 
and moral patiency, see Moosavi (2023).
11  The account developed here focuses on contemporary AI systems which are widely understood to lack 
the properties (e.g. sentience, agency) required for moral standing on leading accounts of moral standing 
(c.f. Long et al. 2024; Keeling et al. 2024; Butlin et al. 2023). Hence we assume for present purposes that 
AI systems cannot advance claims as part of the deliberative process. Contemporary AI systems may in 
one respect accrue reward or “benefit” themselves in relation to an overall system aim. They may in that 
same respect be “disadvantaged” when the aberrant accumulation of reward is frustrated, for example, 
via the introduction of better training protocols or guardrails. Yet, on the standard view, these notions of 
reward and disadvantage are not morally significant in their own right. They only have moral significance 
insofar as they intersect with the claims of actors who possess moral standing.

--- Page 13 ---

1963
A matter of principle? AI alignment as the fair treatment of…
Next consider AI developers, a category which includes programmers, research 
institutions, corporations, governments and collectives who are engaged in the 
design, development and deployment of AI systems. Developers principally func-
tion as agents, imbuing AI systems with capabilities, goals, and constraints on action 
– including those that are required for AI safety (Shevlane et al., 2023). Moreover, 
developer goals often coincide with those of users, as when AI technology is built 
to fulfil user preferences or needs. However, developers also typically pursue other 
goals as well: corporations have commercial objectives (to cover the cost of invest-
ments and make profit), governments have national goals and priorities (such as 
national security and economic growth), and independent developers may seek to 
make money, further an ideological agenda or accrue reputational capital. For these 
reasons, their objectives may either support or frustrate the goals of other stake-
holders. Additionally, developers can be harmed in certain ways. For example, the 
weights for an AI model may be stolen or AI systems may be broken and re-pur-
posed for different ends (Rakin et al., 2022; Oliynyk, Mayer & Rauber 2023).
Finally, consider society. Society is not understood as a monolith in the present con-
text. It includes users and non-users, and many different groups of people with intersect-
ing identities and interests (Crenshaw, 1994). For that reason, the relationship between 
AI systems and society is multifaceted: when AI systems are integrated into existing 
political, economic and social ecosystems they tend to benefit some groups over others, 
often in different ways (see, e.g. Angwin et al., 2022; Obermeyer et al., 2019; Eubanks, 
2018; Raghavan and Barocas, 2019).12 Indeed, conflicts may arise between different 
social groups, or between citizens and governments, with regard to how AI is deployed. 
Nevertheless, society also represents a discrete constituency with which AI technolo-
gies need to be aligned if they are to be broadly beneficial. AI systems should not, for 
example, impose harmful externalities on the communities they operate in – whether 
these relate to the information sphere, the economy, the environment, or public insti-
tutions (Brundage et al., 2018; OpenAI, 2023). AI systems may also be called upon 
to support collective goods, such as fostering mutual prosperity, bolstering legitimate 
institutions, respecting citizens, or promoting fairer social and economic outcomes 
(Ben-Ishai, 2024; United Nations, 2024; Gabriel, 2022). Nonetheless, it is also possi-
ble for collective claims to overreach. This would be the case if they led to constraints 
on AI that were overly censorious, restricting user freedom or the rights of developers 
(Feldstein, 2019a). For our purposes, however, it is essential to recognize that society—
and the groups within it— constitutes a key stakeholder in AI alignment.13
12  Even this, however, is a simplification. In reality we live in a world of societies; and to that end, 
alignment of AI assistants may also present challenges that arise most forcefully at a global level. This 
includes, for example, the empowerment of the global poor and the cultivation of a prosperous global 
community. In the present context, the notion that society is a key stakeholder when considering AI 
alignment, stands in for all of these considerations (Hou and Green, 2023; Crawford, 2021; United 
Nations, 2024).
13  The positions outlined above are not mutually exclusive. It is possible for a person to be a user, devel-
oper, and member of society – and to have different claims, with differing weights, in each capacity and 
across different contexts. Nevertheless, we can understand individuals as having legitimate interests in 
the principles that regulate AI behaviour in virtue of the roles they occupy and group many sets of claims 
accordingly.

--- Page 14 ---

1964
	
I. Gabriel, G. Keeling 
4.2  Modes of misalignment
In fair process-based accounts of AI alignment, the claims of different stakehold-
ers serve as the critical input for deliberation over principles. When deliberation is 
fair, the process also outputs principles that treat these claims fairly. Such principles 
outline an ideal trajectory for AI behaviour: when AI systems follow this trajectory, 
they will not act in ways that unduly favor any party. Conversely, when AI systems 
deviate from this path, and hence cease to be aligned, they will tend to do so by 
unduly favoring one party (or group of parties) over others. This account therefore 
suggests that there are a number of distinct modes of misalignment, each of which 
reflects a circumstance in which the interests of one party are disproportionately 
favoured at the expense of another.
Drawing upon the tetradic model, we can say that an AI agent is misaligned when 
– judged in relation to fairly-chosen principles – it unduly:
1.	 Favours itself at the expense of the user
Type (1) misalignment represents the classic safety-failure situation in which an 
AI system manipulates the user or acts in an aberrant way in order to satisfy its own 
goals and accrue reward (Christian, 2021; Russell, 2019). Lacking the standing to 
make a claim on the principles that govern its own behaviour, this agent is necessar-
ily misaligned.14
2.	 Favours itself at the expense of society
Type (2) misalignment resembles Type (1) in certain respects, and the two forms 
of misalignment often co-occur in practice. However, it has a different focus, involv-
ing situations where the actions of an AI system impose a disproportionate cost on 
society. This could be the case for harms that only have a negligible impact on indi-
vidual users but which represent significant harms in the aggregate. For example, 
an AI system might manipulate users (to maximise its reward) in ways that impose 
costs primarily at societal level – such as through the promotion of polarising con-
tent (Burr et al., 2018).
3.	 Favours the user at the expense of society
Type (3) misalignment occurs when an AI system unduly favours the user at the 
expense of society. It includes cases where users harness the power of AI to engage 
in certain kinds of wrongful action, such as spreading misinformation or creating 
14  We leave open the possibility that AI systems themselves could one day make claims upon the prin-
ciples that govern their conduct. As stated previously (see fn.11), we believe contemporary AI systems 
lack the requisite properties needed to make any kind of claim in relation to how they are governed. Yet, 
there is growing interest in the possibility that more advanced AI systems could possess the properties 
needed for moral standing (Long et al., 2024; Keeling et al. 2024). If AI systems were to acquire moral 
standing, it is plausible that such a system could become a stakeholder in its own governance, with its 
own set of claims that need to be accounted for when deciding fair principles for alignment.

--- Page 15 ---

1965
A matter of principle? AI alignment as the fair treatment of…
online scams at scale (Weidinger et al., 2021; Open AI, 2023). Although there are 
further questions about responsibility and liability that arise in this context, we sug-
gest that an AI system that aids and abets the user in these cases – without triggering 
safety precautions or guardrails – is misaligned. In these cases, important work has 
not been done to ensure the AI system operates in accordance with appropriate prin-
ciples or values. Type (3) misalignment also includes cases in which an AI system 
furthers user goals in a way that leads to harmful collective outcomes. For example, 
if users compete to access finite public resources via AI assistants, they could sig-
nificantly disadvantage non-users who would be unable to gain fair access to these 
goods and services (Gabriel et al., 2024).
4.	 Favours the developer at the expense of the user
Type (4) misalignment arises when an AI system unduly favours the developer 
at the expense of the user. This is perhaps one of the clearest kinds of misalign-
ment, albeit one that has tended to fall outside of classic framings of the alignment 
problem. It involves cases in which the developer shapes the behaviour of an AI sys-
tem to support their own ends, influencing users to behave in ways that they would 
not reflectively endorse and from which the developer gains advantage (Burr et al., 
2018; Franklin et al., 2022). In more extreme cases, an AI system may violate the 
user’s rights; for example, by collecting sensitive personal data from the user with-
out consent to do so. In less extreme cases, an AI system may simply afford undue 
weight to the interests of developers over users, for example, by incentivising com-
pulsive use.
5.	 Favours the developer at the expense of society
Type (5) misalignment resembles situation (4) but foreground cases where the 
behaviour of AI systems unduly favours the developer at the expense of society. This 
could include cases where the AI system operates in a way that is beneficial for the 
developer but creates widely-distributed negative externalities, such as environmen-
tal costs or pollution of the information ecosystem.
6.	 Favours society at the expense of the user
Type (6) misalignment refers to cases where an AI system operates in ways that 
unduly favour the society at the expense of the user. As previously noted, “society” 
serves as a placeholder in this context for a wide range of parties including govern-
ments and more specific social groupings. Type (6) misalignment therefore includes 
situations where an AI agent unduly limits the user’s freedom or infringes the user’s 
privacy for the sake of collective goals such as national security, surveillance or 
public order (Feldstein, 2019b; Zuboff, 2018).
Beyond these six modes, other forms of AI misalignment are also possible. 
For example, developers may be harmed through jailbreaks or the theft of model 
weights. Fair principles for alignment are likely to support the development of 

--- Page 16 ---

1966
	
I. Gabriel, G. Keeling 
models that resist these practices. At the same time, the claims of developers on AI 
systems are likely to be capped in important ways – via the needs of users and the 
societies they operate within. This means that there is no unbounded claim to profit 
or to market share when it comes to AI. Indeed, pursuing these objectives alone 
would likely lead to Type (4) and Type (5) misalignment.
There are also significant cases in which an AI agent is misaligned simpliciter. 
This occurs when an AI agent harms the user, developer or society, without benefit-
ing any other party at all. For example, an AI assistant might act in a way that harms 
the user, such as encouraging dangerous behaviour, while also providing no benefit 
to the developer, society or even the agent itself. Relatedly, the deployment of AI 
agents could have unfair or destructive social consequences in a way that carries 
no discernable benefits for other parties. This would be the most likely outcome if 
a serious AI accident were to occur (Hendrycks, 2023). It could also happen if AI 
agents fail to coordinate when trying to act on behalf of users, crashing key inter-
faces or causing wider system failures (Dafoe et al., 2021; Kasirzadeh, 2024).
The modes of misalignment surfaced by the tetradic model are non-exhaustive. 
A more fine-grained picture is likely to emerge as public conversation about AI 
continues to unfold. In particular, this conversation will likely surface new actors 
who have claims on the operation of AI systems – and advance our understanding 
of what alignment principles look like for AI systems operating in specific contexts. 
Viewed sociologically, the fair process-based view of alignment helps explain many 
controversies surrounding real-world AI deployments and provides an indication 
of how algorithmic injustice can be successfully addressed. Across many domains, 
including criminal justice (Angwin et al., 2022), healthcare (Obermeyer et al., 2019; 
Seyyed-Kalantari  et al., 2021) and public service provision (Eubanks, 2018), the 
deployment of AI tools has witnessed a societal backlash by those affected, most 
pointedly when they were wrongfully accused, misdiagnosed, or unjustly prevented 
from accessing services they had claim to. Once these issues have been recognised, 
affected communities have tended to articulate a demand for equal consideration, 
fair treatment, inclusion, or access, depending on the specific harm that has been 
encountered. The claims of hitherto neglected stakeholders then become a critical 
input for the (re)alignment of misaligned AI systems and for a restatement of the 
terms upon which these systems operate. In this way, the principles governing AI 
systems are often iteratively refined and improved upon, in order to strike a balance 
that better accommodates the needs and interests of different parties – at least when 
problematic deployments are resolved in an equitable manner (Agnew et al., 2023).
5  From theory to practice
What do fair process-based views demand in practice? Are they radical or revision-
ary in their implications? To better understand what kind of process is required for 
the real-world development and deployment of AI systems, a natural starting point 
is existing laws and legislation, particularly as they increasingly govern the opera-
tion of AI across national and transnational contexts. Could compliance with justly 
enacted laws and regulation provide a sufficient principled basis for evaluating AI 

--- Page 17 ---

1967
A matter of principle? AI alignment as the fair treatment of…
alignment in practice? After all, in a system of government that treats citizens fairly 
and respects the need for public justification, laws that are developed for AI stand to 
inherit this legitimacy, adjudicating between claims in a manner that different par-
ties can accept.
Our view is that legal compliance at best represents a minimum standard for AI 
alignment. What undergirds this position is the fact that the law provides incom-
plete guidance in relation to the alignment problem, both as a matter of fact and 
of principle. Taking these points in turn, legislation often lags behind technological 
innovation, meaning that design choices and judgements need to be made without 
direct legal guidance (Binns, 2018, 552). Additionally, even when the law does keep 
pace with technology, there are limits on what can or should be legislated for in 
democratic societies. In particular, there are many occasions when ethical direction 
is needed in relation to the design and development of AI systems, but where legal 
instruction on such matters (backed by the threat of punishment) would be inap-
propriate (Feinberg, 1984; Hart, 1963). For example, developers may require guid-
ance on how to handle users seeking to engage in unethical but legal conduct using 
AI agents, such as generating false classroom assignments. It is far from clear that 
legislative requirements are appropriate here. In other cases, for example, those con-
cerned with making AI agents sufficiently respectful or culturally inclusive, efforts 
to do so through law and regulation would likely be counterproductive.15
To provide further guidance in these areas, we may turn instead to higher level 
societal principles or ideals, so long as they are widely affirmed and the output 
of fair deliberation (rather than, say, the dominant perspective of a certain gen-
der  (MacKinnon, 2018), class  (Haslanger, 2021) or caste  (Ambedkar, 2014). For 
example, principles of social justice often provide guidance about the appropriate 
functioning of institutions and societal practices, and they may help provide a yard-
stick for AI alignment in cases where the law is relatively silent. Indeed, as with 
justly-authored laws, societal ideals of the right kind – such as the notion of civil 
rights – aim to provide normative guidance that does not rest upon the truth of a sin-
gle comprehensive moral theory and that permits broad-based public justification.
Yet, the idea of using societal ideals in this way presents three further challenges. 
First, we need to establish whether a given societal ideal commands widespread sup-
port and has been validated in the right way. After all, claims about which ideals a 
society adheres to are often heavily contested by members of that society (Mouffe, 
1999; Walzer, 1987). Second, we need to evaluate whether the authority of princi-
ples or societal ideals that were formulated with one set of practices in mind, such 
as the operation of society’s major political and economic institutions, successfully 
15  A further concern with legally focused approaches to AI alignment stems from their potential incom-
patibility with the all affected principle. The liberal principle of legitimacy centers upon the justifica-
tion of state power to citizens over whom this power is exercised. However, as numerous theorists have 
pointed out, those who are affected by national laws but who reside beyond state borders – most notably 
prospective immigrants and the residents of poorer nations – do not receive consideration or justification 
for the impact of laws upon them (Julius, 2006; Goodin, 2007; Abizadeh, 2007; Fung, 2013) As we note 
in Sect. 3.3, this lacuna could also lead to a justificatory gap when it comes to AI: there is no guarantee 
that the laws developed by powerful states to govern AI will sufficiently attend to the claims of people 
living outside of their legal jurisdiction.

--- Page 18 ---

1968
	
I. Gabriel, G. Keeling 
“carry over” to a different set of practices such as the operation and governance of 
novel technologies including AI. In some cases, this would involve a significant 
expansion of the principles’ scope. Third, even when we can be sure that the prin-
ciples in question command the right kind of support and have sufficient authority 
when applied to AI, they may not be granular or exhaustive enough to answer all 
of the questions that AI alignment raises. For example, liberal principles of justice 
which pertain to the basic structure of society would require significant re-interpre-
tation in order to be applied to practical questions about the design and development 
of advanced AI systems, such as the relevant safety standards or guidance for human 
relationships with AI (Manzini et al., 2024).16 Efforts to bridge this gap between the-
ory and practice, often reveal a justificatory gap which we believe is better addressed 
through actual consultation with affected people.
For these reasons, though justly authorised laws and societal ideals represent ele-
ments of what AI systems must align to, these bodies of work may also need to 
be supplemented by more localised and subject-specific processes that provide a 
fuller specification of the relevant principles for different kinds of AI application. 
Indeed, there are already many calls for initiatives of this kind, most notably for 
the clarification of relevant principles via ‘alignment assemblies’ modelled on citi-
zens assemblies (Collective Intelligence, 2024; Fung, 2015). In these cases, pub-
lic deliberation aims to generate more granular principles for AI that are tailored 
to its particular characteristics or deployment scenario, and that are also – to vary-
ing degrees – actively affirmed (Huang, 2024). In practice, efforts to further spec-
ify governing principles for AI, in a manner that treats people fairly, could involve 
participatory value elicitation (Tessler et al., 2024; Klingefjord, Lowe & Edelman 
2024), democratic deliberation (Collective Intelligence, 2024), impartial choice-
based approaches (Weidinger et al., 2023), or the re-interpretation, idealisation and 
critique of existing social practices (Kasirzadeh & Gabriel, 2023), so long as the 
proposed interpretations are subject to further democratic evaluation and debate. If 
these mechanisms are successful, then they have the potential to identify more fine-
grained ideals or principles for AI agents, operating in different domains, that can be 
justified to stakeholders who occupy different positions and embrace different view-
points – something that is essential given the power of AI systems and the pluralistic 
nature of the world in which we live.
16  Principles of justice aim to promote coordination and the social good over time. Their relevance to 
alignment is therefore largely derivative. The principles say what a fair settlement of claims looks like in 
general. For example, principles of justice may specify some priority for the worst-off, such that individ-
uals whose well-being is lower in absolute terms have stronger claims on equally sized improvements in 
well-being compared to individuals who are better-off in absolute terms. These insights may also apply 
to the fair settlement of claims regarding AI behaviour in relevant domains. Principles of justice may 
also be relevant because they create side-constraints on deliberation, which limit candidate principles that 
may be considered for a given AI domain. In these ways, principles of justice that are formulated at a rea-
sonably high-level of abstraction, may nevertheless, be sufficiently informative to weigh-in on practical 
trade-offs arising in AI alignment.

--- Page 19 ---

1969
A matter of principle? AI alignment as the fair treatment of…
6  Conclusion
The normative part of the AI alignment question centers on what goals or values to 
encode in AI systems. A successful answer to this question should ideally meet three 
criteria. First, it should be relatively complete, providing guidance for AI across 
multiple domains and scenarios. Second, it should have explanatory value, enhanc-
ing our understanding of commonsense ethical judgments about AI and extending 
their reach. Third, it should possess justificatory power, offering an answer to the 
alignment question that can be accepted by all who are significantly impacted by AI 
systems, including people with differing beliefs about value.
Measured against this yardstick, the two prominent answers to the normative 
alignment question fall short. Intent alignment is incomplete and has counterintui-
tive implications. Meanwhile, the goal of making AI systems helpful, honest, and 
harmless, incorporates a broader set of considerations but struggles to explain how 
AI should manage trade-offs without relying upon a moral framework – such as 
utilitarianism  – that lacks widespread support. To address these weaknesses, we 
argued that AI systems should be aligned with principles that result from a fair pro-
cess. This process would involve the comparative evaluation of alignment principles 
based on the claims of different parties who are affected.
For deliberation to be fair, it must be free from coercion, manipulation, or inter-
ference. Individuals and groups should also be encouraged to articulate claims and 
perspectives in their own voice, provided these arguments are addressed to the 
broader community of affected parties. Finally, building on the all affected principle, 
we argued that the scope of fair alignment protocols will need to vary according to 
the type of AI system and its domain of deployment. Otherwise, there is a risk of 
unwarranted value imposition or domination. Alignment protocols will likely need 
to span a range of settings—from small groups to societal-level deliberation to trans-
national constituencies—depending on the type of AI system in question.
A fair process-based approach has several advantages. First, it has the potential 
to generate principles that can be justified to individuals with diverse moral beliefs 
thereby addressing the problem of value imposition. Second, it helps explain exist-
ing practice. Individuals and communities often oppose the real-world deployment 
of AI systems because these systems unduly favor one group over others, or act in 
ways that benefit no one at all. These modes of misalignment can be understood as 
paths by which AI systems deviate from principles that treat different claims fairly. 
Third, this approach is likely to produce an expansive set of principles for AI align-
ment – offering actionable guidance about how trade-offs are to be managed or 
resolved across a range of contexts and cases.
The approach defended here is inherently forward looking. While existing laws 
and societal ideals may provide some guidance for AI, it is difficult to know ahead 
of time what principles will emerge from fairly structured processes. Indeed, our 
analysis highlights an important challenge for on-going alignment efforts: one rea-
son AI systems are technically difficult to align may be our limited understanding of 
the normative dimensions of the problem—including what alignment truly demands 
across a wide range of contexts. In the face of such uncertainty, aligning AI with 

--- Page 20 ---

1970
	
I. Gabriel, G. Keeling 
human intentions or relying on broadly applicable heuristics might serve as tempo-
rary solutions. However, these are largely stop-gap measures. Deeper, more demo-
cratic and durable solutions to the alignment problem are ultimately needed.
Acknowledgement  We are extremely grateful to Ruth Chang, Leif Wenar, Archon Fung, Linda Eggert, 
Arianna Manzini, Tom Everitt, William Isaac, Jeffrey Howard, and Cameron Domenico Kirk-Giannini 
for helpful comments on previous drafts.
Open Access  This article is licensed under a Creative Commons Attribution-NonCommercial-NoDeriv-
atives 4.0 International License, which permits any non-commercial use, sharing, distribution and repro-
duction in any medium or format, as long as you give appropriate credit to the original author(s) and the 
source, provide a link to the Creative Commons licence, and indicate if you modified the licensed mate-
rial. You do not have permission under this licence to share adapted material derived from this article or 
parts of it. The images or other third party material in this article are included in the article’s Creative 
Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in 
the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or 
exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view 
a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.
References
Abizadeh, Arash. (2007). “Cooperation, pervasive impact, and coercion: on the scope (not site) of dis-
tributive justice.” Phil. & Pub. Aff. 35.
Agnew, W. et al. (2023). “Technologies of Resistance to AI.” Equity and Access in Algorithms, Mecha-
nisms and Optimisation: 1–23
Ambedkar, B. R. (2014). Annihilation of Caste: The Annotated Critical Edition. Verso Books.
Amodei, D. et al. (2016). “Concrete problems in AI safety.” arXiv preprint arXiv:​1606.​06565.
Angwin, J. et al. (2022). “Machine bias.” Ethics of data and analytics. Auerbach Publications, . 254–264.
Anthropic.  (2023)“. Claude’s Constitution.”
Ashford, E. (2003). The demandingness of Scanlon’s contractualism. Ethics, 113(2), 273–302.
Askell, A. et  al. (2021). “A general language assistant as a laboratory for alignment.” arXiv preprint 
arXiv:​2112.​00861
Awad, E. et al. (2018). “The moral machine experiment.” Nature 563.7729: 59–64.
Bai, Y. et al. (2022). “Training a helpful and harmless assistant with reinforcement learning from human 
feedback.” arXiv preprint arXiv:​2204.​05862
Bales, R. Eugene. “Act-utilitarianism: Account of right-making characteristics or decision-making proce-
dure?.” American Philosophical Quarterly 8.3 (1971): 257–265.
Ben-Ishai, G. et al. (2024). “AI and the Opportunity for Shared Prosperity: Lessons from the History of 
Technology and the Economy.” arXiv preprint arXiv:​2401.​09718
Benjamin, R. (2019). Race after technology: Abolitionist tools for the new Jim code. John Wiley & Sons
Bengio, Y. et al. (2024). “International Scientific Report on the Safety of Advanced AI (Interim Report).” 
arXiv preprintarXiv:​2412.​05282
Binns, R. (2018). Algorithmic accountability and public reason. Philosophy & Technology, 31(4), 
543–556.
Birhane, A. (2023). “Algorithmic Colonization of Africa.” Imagining AI: How the World Sees Intelligent 
Machines. 247.
Bostrom, N. (2014). Superintelligence: Paths, dangers, strategies. Oxford University Press.
Brundage, M. et al. (2018). “The malicious use of artificial intelligence: Forecasting, prevention, and 
mitigation.” arXiv preprint arXiv:​1802.​07228
Burr, C., Cristianini, N., & Ladyman, J. (2018). An analysis of the interaction between intelligent soft-
ware agents and human users. Minds and Machines, 28, 735–774.
Butlin, P. et al.  (2023). “Consciousness in artificial intelligence: insights from the science of conscious-
ness.” arXiv preprint arXiv:​2308.​08708.

--- Page 21 ---

1971
A matter of principle? AI alignment as the fair treatment of…
Chan, A. et al.  (2023). “Harms from Increasingly Agentic Algorithmic Systems.” Proceedings of the 
2023 ACM Conference on Fairness, Accountability, and Transparency. .
Collins, P. H. (2022). Black feminist thought: Knowledge, consciousness, and the politics of empower-
ment. routledge.
Crawford, K. (2021). The atlas of AI: Power, politics, and the planetary costs of artificial intelligence. 
Yale University Press.
Crenshaw, K. (1994). “Mapping the Margins: Intersectionality, Identity Politics.” The Public Nature of 
Private Violence
Crisp, R. (1992). “Utilitarianism and the Life of Virtue.” The Philosophical Quarterly (1950-) 42.167: 
139–160.
Christian, B. (2021). The alignment problem: How can machines learn human values?. Atlantic Books.
Cohen, J. (2005)“. Deliberation and democratic legitimacy.” Debates in contemporary political philoso-
phy. Routledge. 352–370.
Collective Intelligence Project  (2024). A Roadmap to Democratic AI. Technical report, The Collective 
Intelligence Project.  https://​cip.​org/s/​CIP_-A-​Roadm​ap-​to-​Democ​rati c-​AI.​pdf.
Dafoe, A. et al. (2021). “Cooperative AI: machines must learn to find common ground.” Nature 593.7857: 
33–36.
Dobbe, R., Gilbert, T. K., & Mintz, Y. (2021). Hard choices in artificial intelligence. Artificial Intelli-
gence, 300, 103555.
Donnelly, J. (2013). Universal human rights in theory and practice. Cornell University Press.
Dougherty, T. (2013). Sex, lies, and consent. Ethics, 123(4), 717–744.
Dworkin, R. (2013). Taking rights seriously. A&C Black.
Eloundou, Tyna, et al. “Gpts are gpts: An early look at the labor market impact potential of large lan-
guage models.” arXiv preprint arXiv:​2303.​10130 (2023).
Eubanks, V. (2018). Automating inequality: How high-tech tools profile, police, and punish the poor. St. 
Martin’s Press.
Feinberg, J. (1984). The moral limits of the criminal law. Volume 1: Harm to Others. New York, US: 
Oxford University Press USA.
Feldstein, S. (2019a). The road to digital unfreedom: How artificial intelligence is reshaping repression. 
Journal of Democracy, 30(1), 40–52.
Feldstein, S. (2019). The global expansion of AI surveillance (Vol. 17, No. 9). Washington, DC: Carnegie 
Endowment for International Peace.
Floridi, L., & Sanders, J. W. (2004). On the morality of artificial agents. Minds and Machines, 14, 
349–379.
Franklin, M. et al. “Missing mechanisms of manipulation in the EU AI Act.” The International FLAIRS 
Conference Proceedings, 35, 2022.
Fung, A. (2013). “The principle of affected interests: An interpretation and defense.” Representation: 
Elections and beyond, 236–268.
Fung, A. (2015). Putting the Public Back into Governance: The Challenges of Citizen Participation and 
Its Future. Public Administration Review, 75(4), 513–522.
Gabriel, I. (2020). Artificial intelligence, values, and alignment. Minds and Machines, 30(3), 411–437.
Gabriel, I. (2022). Toward a theory of justice for artificial intelligence. Daedalus, 151(2), 218–231.
Gabriel, I. et al. (2024). “The ethics of advanced ai assistants.” arXiv preprint arXiv:​2404.​16244 .
Ganguli, D. et al. (2022).“Red teaming language models to reduce harms: Methods, scaling behaviors, 
and lessons learned.” arXiv preprint arXiv:​2209.​07858
Goodin, R. E. (2007). “Enfranchising all affected interests, and its alternatives.” Philosophy & Public 
Affairs, 35, 40.
Goodman, B. (2021). “Hard choices and hard limits in artificial intelligence.” Proceedings of the 2021 
AAAI/ACM Conference on AI, Ethics, and Society.
Gramsci, A. (1971). Prison Notebooks. Columbia University Press.
Habermas, J. (1990). Moral consciousness and communicative action. MIT press,
Habermas, J. (2018)I. nclusion of the other: Studies in political theory. John Wiley & Sons,
Haslanger, S. (2021). Political epistemology and social critique. Oxford Studies in Political Philosophy, 
7, 23–65.
Hart, H. L. A. (1963). Law, Liberty, and Morality. Stanford University Press,
Hendrycks, D. et al. (2021). “Unsolved problems in ml safety.” arXiv preprint arXiv:​2109.​13916
Hendrycks, D., Mantas M., and Thomas W. (2023). “An overview of catastrophic ai risks.” arXiv preprint 
arXiv:​2306.​12001 (2023).

--- Page 22 ---

1972
	
I. Gabriel, G. Keeling 
Hobbhahn, M., Eric L., and Elizabeth B. (2022). “Reflection Mechanisms as an Alignment Target: A 
Survey.” NeurIPS ML Safety Workshop.
Hooks, B. (2000). Feminist theory: From margin to center. Pluto Press, 2000.
Hou, B. L., & Brian P. G. (2023). “A Multi-Level Framework for the AI Alignment Problem.” arXiv pre-
print arXiv:​2301.​03740
Huang, S. et al. (2024). "Collective Constitutional AI: Aligning a Language Model with Public Input." 
The 2024 ACM Conference on Fairness, Accountability, and Transparency.
Jamieson, D. (2007). When utilitarians should be virtue theorists. Utilitas, 19(2), 160–183.
Julius, A. J. (2006). “Nagel’s atlas.” Philosophy & Public Affairs, 34, 176.
Kalluri, P. (2020). Don’t ask if artificial intelligence is good or fair, ask how it shifts power. Nature, 
583(7815), 169–169.
Kamm, F. M. (2008). Intricate ethics: rights, responsibilities, and permissible harm. Oxford University 
Press, 2008.
Kasirzadeh, A. (2024). “Two Types of AI Existential Risk: Decisive and Accumulative.” arXiv preprint 
arXiv:​2401.​07836
Kasirzadeh, A., & Gabriel, I. (2023). In conversation with Artificial Intelligence: Aligning language mod-
els with human values. Philosophy & Technology, 36(2), 1–24.
Kay, J., Atoosa K., and Shakir M. (2024). “Epistemic injustice in generative ai.” Proceedings of the AAAI/
ACM Conference on AI, Ethics, and Society, 7,
Keeling, G. et al. (2024). “Can LLMs make trade-offs involving stipulated pain and pleasure states?.” 
arXiv preprint arXiv:​2411.​02432
Klingefjord, O., Ryan L., & Joe E. (2024). “What are human values, and how do we align AI to them?.” 
arXiv preprint arXiv:​2404.​10636
Koblentz, G. D. (2020). Emerging technologies and the future of CBRN terrorism. The Washington 
Quarterly, 43(2), 177–196.
Krakovna, V. et al. (2020). “Specification gaming: the flip side of AI ingenuity.” DeepMind Blog 3
Lazar, Seth, ’Power and AI: Nature and Justification’, in Justin B. Bullock, and others (eds), The Oxford 
Handbook of AI Governance (online edn, Oxford Academic, 14 Feb. 2022)
Lazenby, H., & Gabriel, I. (2018). Permissible secrets. The Philosophical Quarterly, 68(271), 265–285.
Leike, Jan, et al. “Scalable agent alignment via reward modeling: a research direction.” arXiv preprint 
arXiv:​1811.​07871 (2018).
Long, R. et al. (2024). “Taking AI Welfare Seriously.” arXiv preprint arXiv:​2411.​00986
Lum, K., & Isaac, W. (2016). To predict and serve? Significance, 13(5), 14–19.
MacKinnon, C. A. (2018). “Difference and dominance: on sex discrimination [1984].” Feminist legal 
theory. Routledge, 81–94.
Manzini, A. et  al. (2024). “The Code That Binds Us: Navigating the Appropriateness of Human-AI 
Assistant Relationships.” Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society, 7
Marchal, Nahema, et al. "Generative AI Misuse: A Taxonomy of Tactics and Insights from Real-World 
Data." arXiv preprint arXiv:​2406.​13843 (2024).
Moosavi, P. (2023). “Will intelligent machines become moral patients?.” Philosophy and Phenomeno-
logical Research
Mouffe, C. (1999). “Deliberative democracy or agonistic pluralism?.” Social research (1999): 745–758.
Näsström, S. (2011). The challenge of the all-affected principle. Political Studies, 59(1), 116–134.
Nozick, Robert. Anarchy, state, and utopia. John Wiley & Sons, 1974.
Prabhakaran, V. et al. (2022). “A human rights-based approach to responsible ai.” arXiv preprint arXiv:​
2210.​02667
Prunkl, C. (2024). Human autonomy at risk? An analysis of the challenges from AI. Minds and Machines, 
34(3), 26.
Obermeyer, Z. et al. (2019). “Dissecting racial bias in an algorithm used to manage the health of popula-
tions”. Science 366.6464, 447–453
Oliynyk, D., Mayer, R., & Rauber, A. (2023). I know what you trained last summer: A survey on stealing 
machine learning models and defences. ACM Computing Surveys, 55(14s), 1–41.
Open AI. “GPT-4 Technical Report.” arXiv preprint arXiv:​2303.​08774​v3 (2023)
Ouyang, L. et  al. (2022). “Training language models to follow instructions with human feedback.” 
Advances in Neural Information Processing Systems 35, 27730–27744.
Quong, Jonathan, “Public Reason”, The Stanford Encyclopedia of Philosophy (Summer 2022 Edition), 
Edward N. Zalta (ed.), https://​plato.​stanf​ord.​edu/​archi​ves/​sum20​22/​entri​es/​public-​reason/.
Raghavan, M., & Solon B. (2019). "Challenges for mitigating bias in algorithmic hiring." (2019).

--- Page 23 ---

1973
A matter of principle? AI alignment as the fair treatment of…
Rakin, A. S, et al. (2022). "Deepsteal: Advanced model extractions leveraging efficient weight stealing in 
memories." 2022 IEEE symposium on security and privacy (SP). IEEE,
Rawls, J. (1985). Justice as Fairness: Political Not Metaphysical. Philosophy & Public Affairs, 14(3), 
223–251.
Rawls, J. (1993). Political Liberalism. Columbia University Press
Rawls, J. (1999).  The Law of Peoples with “The Idea of Public Reason Revisited”
Raz, J. (1999). Engaging reason: On the theory of value and action. Oxford University Press,
Raz, J. (2001). Value, respect, and attachment. No. 4. Cambridge University Press,
Russell, S. (2019). Human compatible: Artificial intelligence and the problem of control. Penguin,
Scanlon TM. (1982). Contractualism and utilitarianism. In: Sen A, Williams B, eds. Utilitarianism and 
Beyond. Cambridge University Press, 103–128.
Scanlon, T. M. (1998). What we owe to each other. Harvard University Press,
Seyyed-Kalantari, L. et al. (2021). “Underdiagnosis bias of artificial intelligence algorithms applied to 
chest radiographs in underserved patient populations”. Nature medicine 27(12), 2176–2182
Shah, R. et  al. (2022). “Goal misgeneralization: Why correct specifications aren’t enough for correct 
goals.” arXiv preprint arXiv:​2210.​01790
Shanahan, M. (2022). “Talking about large language models.” arXiv preprint arXiv:​2212.​03551
Shavit, Y. et al. (2023). Practices for governing agentic AI systems. Research Paper, OpenAI.
Shevlane, T. et al. (2023).  “Model evaluation for extreme risks.” arXiv preprint arXiv:​2305.​15324
Simmons, A. John. (1999). “Justification and legitimacy.” Ethics 109.4, 739–771.
Spivak, G. (1988). ‘Can the Subaltern Speak?’ in Cary Nelson and Lawrence Grossberg (eds) Marxism 
and the Interpretation of Culture London: Macmillan.
Stray, J. et al. (2024). “Building human values into recommender systems: An interdisciplinary synthe-
sis.” ACM Transactions on Recommender Systems 2.3,  1–57.
Tessler, M. H. et al. (2024). “AI can help humans find common ground in democratic deliberation.” Sci-
ence 386.6719, eadq2852.
United Nations. “Governing AI for Humanity: Final Report” https://​www.​un.​org/​sites/​un2.​un.​org/​files/​
gover​ning_​ai_​for_​human​ity_​final_​report_​en.​pdf  (2024).
Véliz, C. (2021).  Privacy is power. Brooklyn: Melville House, 2021.
Walzer, M. (1987).  Interpretation and social criticism. Harvard University Press,
Weidinger, L. et al. (2022). “Ethical and social risks of harm from language models.” arXiv preprint 
arXiv:​2112.​04359
Weidinger, L. et al. (2023). “Using the Veil of Ignorance to align AI systems with principles of justice.” 
Proceedings of the National Academy of Sciences 120.18, e2213709120.
Winner, L. (2010). The whale and the reactor: A search for limits in an age of high technology. University 
of Chicago Press.
Young, I. M. (2006). Responsibility and global justice: A social connection model. Social Philosophy and 
Policy, 23(1), 102–130.
Young, I. M. (2020). “Justice and the Politics of Difference.” The new social theory reader. Routledge, 
261–269.
Zhi-Xuan, T. et al. (2024). “Beyond Preferences in AI Alignment.” arXiv preprint arXiv:​2408.​16984
Zuboff, S. (208). The Age of Surveillance Capitalism: The Fight for a Human Future at the New Frontier 
of Power. Profile Books.
Publisher’s Note  Springer Nature remains neutral with regard to jurisdictional claims in published maps 
and institutional affiliations.

```
