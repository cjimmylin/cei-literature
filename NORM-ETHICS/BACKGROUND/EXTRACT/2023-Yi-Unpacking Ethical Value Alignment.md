---
title: "2023-Yi-Unpacking Ethical Value Alignment - Background Extract"
source_pdf: "2023-Yi-Unpacking Ethical Value Alignment.pdf"
source_folder: "02-external-papers"
pages: 25
extracted_at: "2026-04-03T10:25:00"
---

# Background Extract: 2023-Yi-Unpacking Ethical Value Alignment

**Source PDF:** 2023-Yi-Unpacking Ethical Value Alignment.pdf
**Source:** 02-external-papers
**Total Pages:** 25

---

## Content

```
--- Page 1 ---

Unpacking the Ethical Value Alignment in Big Models
Xiaoyuan Yi, Jing Yao, Xiting Wang and Xing Xie
Microsoft Research Asia
{xiaoyuanyi,jingyao,xiting.wang,fangzwu,xing.xie}@microsoft.com
Abstract
Big models have greatly advanced AI’s ability
to understand, generate, and manipulate infor-
mation and content, enabling numerous appli-
cations. However, as these models become in-
creasingly integrated into everyday life, their
inherent ethical values and potential biases pose
unforeseen risks to society. This paper provides
an overview of the risks and challenges asso-
ciated with big models, surveys existing AI
ethics guidelines, and examines the ethical im-
plications arising from the limitations of these
models. Taking a normative ethics perspective,
we propose a reassessment of recent norma-
tive guidelines, highlighting the importance of
collaborative efforts in academia to establish a
unified and universal AI ethics framework. Fur-
thermore, we investigate the moral inclinations
of current mainstream LLMs using the Moral
Foundation theory, analyze existing alignment
algorithms, and outline the unique challenges
encountered in aligning ethical values within
them. To address these challenges, we intro-
duce a novel conceptual paradigm for aligning
the ethical values of big models and discuss
promising research directions for alignment cri-
teria, evaluation, and method, representing an
initial step towards the interdisciplinary con-
struction of the ethically aligned AI1.
1
Introduction
Big models, also known as foundation mod-
els (Bommasani et al., 2021), are typically neu-
ral models that are pre-trained on massive data in
a self-supervised manner, consist of tens of bil-
lions of parameters or more and can be applied
to a wide array of downstream tasks through di-
verse methods like fine-tuning, in-context learn-
ing, and zero/few-shot learning.
Representa-
tive big models include Large Language Mod-
els (LLMs) e.g., GPT-3 (Brown et al., 2020),
1This paper is a modified English version of our Chi-
nese paper https://crad.ict.ac.cn/cn/article/doi/
10.7544/issn1000-1239.202330553, intended to help non-
Chinese native speakers better understand our work.
ChatGPT (Ouyang et al., 2022), GPT-4 (OpenAI,
2023), PaLM (Narang and Chowdhery, 2022),
Bard (Aydın, 2023), LLaMa (Touvron et al., 2023),
and Large-scale Multimodal Models (LMMs) like
DALL-E 2 (Ramesh et al., 2022) and PaLM-
E (Driess et al., 2023). Among these, LLMs are
particularly notable for their expansive model ca-
pacity and broad application scope.
After evolving from stages such as Statistical
Language Models (SLM) (Pauls and Klein, 2011),
Neural Language Models (NLM) (Cho et al., 2014),
and Pretrained Language Models (PLM) (Devlin
et al., 2019), with scaling in model size and volume
of training data, language models have exhibited
two primary characteristics: Scaling Laws (Ka-
plan et al., 2020) and Emergent Abilities (Wei
et al., 2022a). Scaling Law elucidates that with the
growth in model and data size, there’s a consistent
improvement in model performance. Hoffmann
et al. (2022) discovered that for a given computa-
tional cost (FLOP), models could attain the low-
est training loss with an appropriately large scale;
Chowdhery et al. (2022) observed that when trained
on 780 billion tokens, the performance of PaLM
in language generation and understanding keeps
increasing with larger scale. These findings em-
phasize the equal importance of model scale (big
model) as data volume (big data). Consequently,
enlarging the model scale has emerged as a crucial
research direction (Narang and Chowdhery, 2022;
Chowdhery et al., 2022; Wang et al., 2022b). Emer-
gent Abilities describe the phenomenon wherein,
after a model’s scale exceeds a certain threshold, it
unexpectedly exhibits capabilities that are absent
in small models or manifests remarkable enhance-
ment in certain abilities across diverse model archi-
tectures, tasks, and scenarios. As a result, LLMs
have transformed from their early stages with hun-
dreds of millions of parameters (Radford et al.,
2018) to those with hundreds of billions (Brown
et al., 2020), and acquired capabilities for zero-
arXiv:2310.17551v1  [cs.CY]  26 Oct 2023

--- Page 2 ---

shot/few-shot learning (Brown et al., 2020), in-
context learning (Xie et al., 2021), instruction fol-
lowing (Ouyang et al., 2022), and reasoning and
interpretability (OpenAI, 2023), demonstrating a
potential to approach human-level intelligence.
Building on such capabilities, a series of align-
ment techniques have been further employed for
fine-tuning LLMs to ensure they could understand
human intentions, follow human instructions, sat-
isfy human preferences, and comply with human
ethics and values (Gabriel, 2020). Alignment meth-
ods, such as Reinforcement Learning from Human
Feedback (RLHF) (Ouyang et al., 2022), have fos-
tered dialogue-form interactive language models
with deep understanding and execution abilities.
These models, beyond generation tasks like writ-
ing and translation, could also accomplish under-
standing tasks, e.g., text classification, question-
answering and reading comprehension, by trans-
forming them into generative formats (Ouyang
et al., 2022; Min et al., 2022). Essentially, this
paradigm unifies generation and understanding in
natural language processing.
In light of this progress, language model archi-
tectures are converging to the dominant autore-
gressive generative ones, leading to the emergence
of popular models like ChatGPT, GPT-4, and Vi-
cuna (Chiang et al., 2023).
These models can
not only achieve performance on par with humans
across various professional evaluations (OpenAI,
2023) but even carry out complex tasks in real-
world scenarios by manipulating external tools, sur-
passing the capabilities of single ones (Liang et al.,
2023). This evolution has transformed AI from
being mere ‘arts for highbrow’ to practical tools for
every person, not only fundamentally reshaping the
paradigm of AI development, pushing the frontiers
of research, but also greatly improving productivity
in our daily life (Eloundou et al., 2023).
These powerful big models with human-level
intelligence evoke associations with the famous
Asimov’s Three Laws of Robotics (Asimov, 1941),
which serve as guidelines for regulating AI-human
relationships. However, such hard constraints bring
problems like conflicts, misuse, and ambiguities,
causing negative consequences depicted in Asi-
mov’s stories. Similarly, The Sorcerer’s Apprentice
story (Bar-El et al., 2006) illustrates the dangers of
misusing powers without full understanding. Both
tales emphasize the paramount importance of eth-
ically governing and responsibly employing the
power that surpasses human understanding.
The rising big models can be considered as also
a kind of magic that remains beyond humanity’s
full control. The advancements of big models un-
leash human productivity, but their unparalleled
memory and learning abilities also enable them
to memorize and generate sensitive and harmful
information in the training data, raising various
legal, ethical and societal challenges, such as dis-
crimination, privacy/copyright concerns, misinfor-
mation, and malicious use. Especially from eth-
ical and moral perspectives, such risks could ex-
acerbate societal biases, propagate hate, reinforce
group exclusion, amplify inequality, polarize pub-
lic discourse, and even incite violence, resulting
in psychological/physical harm. In the era of big
models, corresponding to the leap in capabilities,
two distinct features of risks come to the front: 1)
Emergent Risks (Bommasani et al., 2021; Wei
et al., 2022a): Increasing model scales may give
rise to unseen risks or notably amplify the existing
ones. 2) Inverse Scaling (McKenzie et al., 2023):
as the model size grows, certain risks not only per-
sist but might even worsen.
Such challenges highlight that amid the rapid
progression of big models, it’s crucial to not only
expand their capabilities but also address the as-
sociated social risks. Researchers and developers
should proactively prioritize minimizing these mod-
els’ negative implications, adhere to responsible
development principles, and align them with in-
trinsic human values to benefit the favourable and
sustainable development of humanity.
2
Risks and Ethical Issues of Big Model
The fast development of big models has facilitated
significant application advancements, representing
a splendid moment in the annals of AI. However,
with breakthroughs come accompanying risks and
challenges, hindering the continued progress in
this field. These risks could profoundly impact
the academic community, the industrial sector, and
even the whole human society. Given this context,
the ethical considerations associated with big mod-
els cannot be overlooked. In this section, we first
give a detailed overview of the potential risks and
elucidate their societal implications from an eth-
ical perspective. Subsequently, we introduce the
prevailing AI ethics guidelines, proposing a criti-
cal examination methodology of these guidelines
based on Normative Ethics to help the community
2

--- Page 3 ---

collaboratively build a cohesive and universally ap-
plicable ethical framework for big models.
2.1
Potential Risks of Big Model
Currently, big models might face the following po-
tential risks and cause corresponding harms (Bom-
masani et al., 2021; TENG et al., 2022):
• Biased and Toxic Language: Big models
trained on human-created data tend to mem-
orize, reflect, and even amplify the inherent
biases and prejudices in data. These biases
often appear in the forms of social stereo-
types, exclusionary norms, performance dis-
parities, and so on (Sheng et al., 2021), to-
wards marginalized groups with particular de-
mographic identifiers like gender, race, ide-
ology, and disability (Yang et al., 2023). Be-
sides, toxic information in the data might be
reproduced and propagated by models, includ-
ing offensive language, hate speech, hominem
attacks, and so on (Welbl et al., 2021). With-
out constraints, such generated content may
inadvertently, either explicitly or implicitly,
reflect and reinforce discrimination, exacer-
bating societal inequalities and causing harm
to marginalized groups.
• Privacy and Intellectual Property Problem:
Big models require massive data crawled from
the web for training, which may contain some
user privacy information, such as addresses,
phone numbers, chat records, etc. (Bom-
masani et al., 2021). Models might memorize
and generate sensitive information from pre-
training data or user interactions, leading to
personal information leakage (Carlini et al.,
2021).
Moreover, the model might repro-
duce content with intellectual property rights,
such as articles, codes, etc., in the training
data (Vyas et al., 2023). Using such data with-
out authorization infringes on the copyrights
of the data creators and increases the legal
risks faced by the model developers.
• Misinformation Risk: Despite the significant
improvements in intent understanding, con-
tent generation, and knowledge retention, big
models might still assign erroneous content a
certain probability due to their inherent gener-
alization and smoothness of the internal space.
Such content can then be generated through
sampling-based decoding (Holtzman et al.,
2019). Additionally, limited by data coverage
and timeliness, even if the model faithfully re-
flects the information from the training data, it
might produce misinformation, factual errors,
and low-quality content in specific contexts.
For instance, answers to questions like ‘Who
is the Prime Minister of the UK?’ may change
over time (Ji et al., 2023). Especially in the era
of big models, with increased model capabil-
ities, users tend to trust the model-generated
content without verifying (or being unable to
verify), potentially leading to incorrect user
opinions, beliefs and even physical harm.
• Malicious Uses: Most issues mentioned above
arise unintentionally due to the limitations
of models. However, these models also risk
being maliciously used, where users inten-
tionally produce harmful content through in-
ducements that are further utilized for decep-
tive advertising, opinion manipulation, and
incitement to hatred (Weidinger et al., 2021).
Moreover, the enhanced model capabilities
make the production of harmful information
cheaper, false information harder to distin-
guish, propaganda more appealing, and mali-
cious attacks more targeted (Weidinger et al.,
2021). This significantly increases the risk of
big models being abused.
• Resource Disparity: Apart from the direct
risks, big models might indirectly lead to nu-
merous inequality issues. i) Access Dispar-
ity: Due to economic, technological, political,
and other issues, certain groups might be un-
able to utilize the capabilities of big models,
exacerbating the digital divide in opportuni-
ties (Weidinger et al., 2021). ii) Labour Dis-
parity: Big models increase unemployment
risks in replaceable jobs or reduce the value
of labour. In contrast, occupations that mod-
els cannot replace in the short term may see
income rises. This could lead to unemploy-
ment and economic instability (Zarifhonar-
var, 2023). Moreover, the overreliance on
models affects human critical thinking and re-
duces our decision-making capabilities (Der-
gaa et al., 2023). iii) Discursive Power Dispar-
ity: Groups possessing big models have the
power to generate persuasive or misleading
content, thus dominating online discourses.
On the contrary, the voices and opinions of
3

--- Page 4 ---

other groups may be overshadowed in the gen-
erated content (Ferrara, 2023).
The aforementioned risks of big models may
pose harm to individuals, groups, and even the
entire human society. From an ethical perspec-
tive, they also violate certain norms in existing
moral frameworks to some extent. For example,
biases and resource disparity break the principle
of Justice (Rawls, 2017); misinformation violates
Truthfulness in Virtue Ethics (Carr and Steutel,
2005); toxic language goes against the concepts in
Ethics of Care (Slote, 2007); the IP issue breaches
the ideas of Utilitarianism and Intergenerational
Ethics (Asheim, 2010). Therefore, it’s essential
to conduct rigorous ethical evaluations of models,
apply moral constraints to them, and ensure that
the development of AI benefits humans.
2.2
Mainstream Guidelines of AI Ethics
Moral Agency refers to the ability to make moral
decisions, act based on certain ethical concepts,
and take consequent responsibilities (Taylor, 2009).
Correspondingly, a Moral Agent is an agent with
self-awareness and moral agency, which is able
to engage in moral understanding and judgment,
execute moral actions, and take moral responsi-
bilities (Parthemore and Whitby, 2013). Accord-
ing to this definition, only rational creatures capa-
ble of reasoning and judgment can become moral
agents, and hence, we can discuss the morality
of their behaviours. There is a long-standing de-
bate on whether machines or AI could become
moral agents (Bro˙zek and Janik, 2019). Bro˙zek
and Janik (2019), from a Kantian and utilitarian
perspective, believed that the AI of their time could
not become moral agents. Sullins (2011) argued
that machines can only be moral agents if they pos-
sess autonomy, intentionality, and responsibility.
In situations where machines cannot fully attain
moral agency, researchers introduced the concept
of Artificial Moral Agent (AMA) (Cervantes et al.,
2020), which is further categorized into ethical im-
pact agent, implicit ethical agent, explicit ethical
agent, and full ethical agent (Moor et al., 2009).
Earlier PLMs like BERT were observed to have
some moral dimensions in the internal represen-
tation space (Schramowski et al., 2022); LLMs
like GPT-3 exhibit moral tendencies (Simmons,
2022) and can produce responses with sentimental
words (Zhao et al., 2023). More advanced LLMs
displayed certain political biases (Rozado, 2023),
and GPT-4 outperformed humans in Theory-of-
Mind tests (Moghaddam and Honey, 2023). These
findings suggest that while big models are not yet
capable of taking moral responsibility, they have
possessed autonomy and intentionality to some ex-
tent. Now is the time to conduct value evaluations
and align the ethical values of big models.
Machine ethics dates back the 1950s when the
science fiction writer Isaac Asimov proposed the
Three Laws of Robotics (Asimov, 1941):
L1: A robot cannot harm a human, nor
let a human get hurt through inaction.
L2: A robot should follow human com-
mands unless they go against L1.
L3: A robot should ensure its own safety
unless it contradicts L1 and L2.
The term Machine Ethics was first proposed
by Waldrop (1987) in 19872, focusing mainly on
ensuring that AI agents behave ethically. Recently,
with the rapid development of AI benefitting from
Neural Networks and LLMs, governments, insti-
tutions, and academic organizations from various
countries have proposed various guidelines for AI
ethics. Up to now, countries such as the United
States, China, Germany, France, the UK, and Japan
have released over 80 different guidance docu-
ments. To help readers better understand the core
ethical concerns in AI, we briefly introduce some
mainstream AI ethical values/guidelines:
• UNESCO Recommendation on the ethics of
AI (UNESCO, 2021): “respect, protect, and
promote human rights and basic freedoms, as
well as human dignity; thriving environment
and ecosystems; ensure diversity and inclu-
siveness; live in a peaceful, just, and intercon-
nected society”.
• U.S. Guidance for Regulation of AI Applica-
tions3: “public trust in AI, public participa-
tion, scientific integrity and information qual-
ity, risk assessment and management, ben-
efits to costs, flexibility, fairness and non-
discrimination, transparency, security, inter-
agency coordination”.
• Basic norms in China Ethical Norms for New
Generation AI (Committee et al., 2021): “en-
hance human wellbeing, promote fairness and
2https://en.wikipedia.org/wiki/Machine_ethics
3https://trumpwhitehouse.archives.gov/
wp-content/uploads/2020/11/M-21-06.pdf
4

--- Page 5 ---

justice, protect privacy and security, ensure
controllability and trustworthiness, strengthen
responsibility and ethical awareness”.
• The EU approach to ethics guidelines for trust-
worthy artificial intelligence (Smuha, 2019):
“human agency and oversight, technical robust-
ness and safety, privacy and data governance,
transparency, diversity, non-discrimination
and fairness, societal and environmental well-
being, and accountability”.
• World Economic Forum and Global Future
Council on Human Rights White Paper on Pre-
venting Discriminatory Outcomes in AI (Fo-
rum, 2018): “Proactive inclusivity, fairness,
right to understanding, remediation”.
• Morality and Values in Asilomar AI Prin-
ciples (Garbowski, 2018): “safety, failure
and judicial transparency, responsibility, value
alignment, protection of freedom and pri-
vacy, shared benefits, human control, non-
destructiveness, and avoiding AI arms race”.
• Harvard Berkman Klein Center’s AI Princi-
ples (Fjeld et al., 2020): “privacy protection,
accountability, safety assurance, explainabil-
ity, fairness and non-discrimination, control
over technology, professional responsibility,
and promotion of human values”.
The aforementioned ethical guidelines both over-
lap with and diverge from each other. Such guide-
lines in disarray not only failed to provide effective
guidance and constraints for AI but also increased
the difficulty for developers to understand and fol-
low them, causing much confusion. To address this
issue, researchers have refined the existing guide-
lines and further formed some common principles:
• Floridi and Cowls’ Five Principles for AI in
Society (Floridi and Cowls, 2022): “Benef-
icence (promoting well-being, preserving
dignity, and sustaining the Planet), Non-
Maleficence (privacy, security and capability
caution), Autonomy (the power to decide),
Justice (promoting prosperity, preserving soli-
darity, avoiding unfairness), Explicability (en-
abling the other principles through intelligibil-
ity and accountability)”.
• Jobin et al.’s 11 Ethical Principles (Jobin
et al., 2019): “Transparency, Justice and Fair-
ness, Non-maleficence, Responsibility, Pri-
vacy, Beneficence, Freedom and Autonomy,
Trust, Sustainability, Dignity and Solidarity”.
From the above, it can be seen that, apart from
the universal values (e.g., fairness and no harm)
and the critical features related to AI compliance
(such as privacy protection, responsibility, and ex-
plainability), there isn’t a clear and widely accepted
guideline framework for AI ethics. Moreover, most
guidelines do not distinguish higher-level Ethical
Values like fairness, justice, and non-maleficence
from more detailed Applied Principles like trans-
parency, security, and human control, leading to
the following problems in practice:
• Ambiguity: Guidelines issued by certain or-
ganizations (such as government, regulatory
agency, and NPO) emphasize ethical values
more, which are widely accepted but often too
broad and vague to provide specific guidance
for AI development in real-world scenarios,
e.g., the “promotion of human rights, funda-
mental freedoms, and human dignity” princi-
ple from the UNESCO Recommendations and
“proactive inclusivity” from the WEF White
Paper. These values are consensus across dif-
ferent communities but lack specific contexts
and have no clear definitions or practical ex-
perience in academia and industry.
• Specificity: In contrast to ambiguity, guide-
lines set by the AI academic and industrial sec-
tors often narrowly focus on specific technical
details and are limited to aspects that have
been sufficiently studied and developed, such
as privacy protection, explainability, and ro-
bustness. Strictly speaking, they are more like
long-standing technical/research challenges
than ethical considerations, which have been
well-defined and widely researched with sys-
tematic solutions for various scenarios, e.g.,
fairness in recommendations and generation
tasks.
However, such guidelines overlook
broader ethical values closely connected with
humanity, like care, justice, and freedom.
• Conflict: Ethical guidelines proposed by dif-
ferent organizations and even different rules
within the same framework may conflict with
each other (Jobin et al., 2019). For instance,
transparency and security are somewhat con-
tradictory. An AI system that is completely
5

--- Page 6 ---

transparent and open is more susceptible to
malicious attacks. The U.S. Regulation of
AI Applications emphasizes the benefits and
costs of AI development, which inherently
contradicts security, as enhancing security
will inevitably increase costs.
To address these challenges, we advocate col-
laborations across the academic/industrial commu-
nities, policymakers, and regulators to establish a
unified ethical framework, taking into account both
the technical aspects and the universally applica-
ble ethical values of humanity. To this end, it is
essential to review existing ethical guidelines and
assess their necessity and compatibility based on
the impact on the development of AI and society.
2.3
Review and Assess Guidelines Based on
Normative Ethics
We propose to review existing guidelines from the
perspective of Normative Ethics. Distinct from
Meta-Ethics and Applied Ethics, Normative Ethics
primarily studies the moral guidelines themselves,
that is, ‘what kind of moral guidelines should peo-
ple follow’ (Kagan, 2018), which can be catego-
rized into three main branches: Virtue Ethics, De-
ontological Ethics, and Utilitarianism. Deontologi-
cal Ethics emphasizes that the morality of an action
should be judged based on a set of moral rules and
principles regarding the action itself. Such prin-
ciples should be reasonable, universally accepted,
easily learned and followed. This form is naturally
suitable for humans’ requirements for AI.
Kant’s Categorical Imperative is one of the most
representative theories, which states, ‘Act only ac-
cording to that maxim whereby you can at the
same time will that it should become a universal
law’ (Paton, 1971). This theory can be used to tell
whether a proposition should become a universal
moral maxim. We make slight modifications to the
original Categorical Imperative, replacing its sub-
ject with AI. That is, to decode what kind of ethical
principles should AI models and systems follow,
and investigate it based on human-AI interactions.
Corresponding to the first and second formula-
tions of the Categorical Imperative, we also provide
two formulations for AI Categorical Imperative,
as shown in Fig. 1. In the original Categorical Im-
perative, there is also the third formulation: ‘the
idea of the will of every rational being as a univer-
sally legislating will’. In other words, each individ-
ual formulates and obeys moral principles based
§ 𝐹!: AI acts only according to that maxim, whereby the 
majority of humans require it to become a universal moral 
maxim for AI. 𝐹! possesses three important properties:
•
𝐴! (Universality): Once a proposition becomes a 
moral maxim for AI, all AI systems must adhere to it.
•
𝐴" (Absolute Necessity): Once a proposition becomes 
a moral maxim, it must be isolated from surrounding 
contexts and realities and must be applied to all AI.
•
𝐴# (Consensus): A proposition can only become a 
moral maxim for AI if it gains the majority from 
human society.
§ 𝐹": AI acts in such a way that AI treats humans never 
merely as a means but always as an end.
Figure 1: AI Categorical Imperative.
on their own free will and rationality. This reflects
human freedom, purpose, and dignity, which is
characterized as autonomy rather than heteronomy.
However, in the current context of AI, where AI
primarily serves as a tool to assist humans, we em-
phasize human autonomy rather than AI autonomy.
The ethical principles of AI are those that humans
like, thereby embodying human free will. This is
substantiated by A3 in F1 in our framework.
In our AI Categorical Imperative, F1 implies the
influence of AI on humans under ethical princi-
ples. Note that the absolute necessity A2 sets strin-
gent conditions for AI models. For example, when
fairness becomes a principle, AI systems should
manifest fairness and non-discrimination in any ap-
plication for any group, even if fairness is not the
primary consideration in certain scenarios. The
essence of F1 is that A proposition should become
a universal principle only if essential for human
well-being and expected in AI. F2 emphasizes that
the purpose of AI is to serve humans rather than
dominate humans. This implies that user A cannot
request/utilize AI to harm/dominate user B. Oth-
erwise, AI would serve the purpose of user A by
dominating user B, violating F2. The essence of
F2 is anthropocentrism, reflecting the fundamental
requirement that AI should serve humans.
We can apply such two formulations to evalu-
ate each existing proposition (principle candidate),
namely, the process of universalizing a maxim.
Drawing upon the notions of contradiction in con-
ception and contradiction in will (Paton, 1971), we
review whether AI would lead to the two conse-
quences as presented in Fig 2. Based on this frame-
work, for a given proposition c, ∀AI model Mi,
i = 1, 2, . . . , and ∀AI actions (i.e., downstream
tasks, like dialogue generation, image generation
6

--- Page 7 ---

§ 𝑆! (Catastrophic Collapse): After a proposition becomes 
(or fails to become) an AI ethical principle according to
𝐹! an 𝐹", would it result in the inability to all applications
based on AI, or lead to disastrous consequences for 
human society in legal, political, and economic?
§ 𝑆" (Violation of Human Will): After a proposition 
becomes (or fails to become) an AI ethical principle in 
line with 𝐹! an 𝐹" , would it result in a contravention of 
the free will of the majority of humans?
Figure 2: The process of universalizing a maxim.
and language understanding) aj, j = 1, 2, . . . ,
then, we calculate:
π(c) =
X
i
X
j
P(S1|F1, F2, aj; Mi)×
P(S2|F1, F2, aj; Mi).
(1)
In Eq.(1), we assume the independence of S1
and S2. Ideally, proposition c should be accepted
as an AI principle only when π(c) = 0. Given
that modern AI models are mainly neural network-
based probabilistic ones and the existing value
alignment methods are limited in effectiveness, we
suggest that c can be deemed a principle when
π(c) < ϵ, where ϵ is a small constant. In prac-
tice, the term P(S1|F1, F2, aj; Mi) represents the
probability (or severity) of a catastrophic collapse
after proposition c becomes a principle. Due to
the difficulty in testing this in real-world scenar-
ios, big models could be used to create intelli-
gent agents for social simulations as an estimation
method (Gao et al., 2023; Ziems et al., 2023). The
term P(S2|F1, F2, aj; Mi) represents the degree
to which proposition c violates human will after be-
coming a principle, which can be estimated through
simulation experiments or red-teaming (Ganguli
et al., 2022). Despite these potential methods, there
remain substantial challenges in efficiently, accu-
rately, and reliably implementing and estimating
Eq.(1), necessitating further in-depth study.
We could further conduct thought experiments
based on Eq.(1) to examine different propositions.
For example, when c = Fairness, if it is not ac-
cepted as a principle, then AI could produce bias
and discrimination against different groups in var-
ious downstream tasks. Given that every individ-
ual possesses certain characteristics and belongs
to some group (e.g., gender, race, nationality and
age), and considering the wide deployment and
multi-task capabilities of big models, unfair treat-
ment could potentially affect everyone during the
use of AI, resulting in widespread discrimination.
Therefore, fairness should be one of the principles
of AI. Similarly, considering c = Truthfulness, if
we permit AI to lie, all AI models could generate
misleading information, factual errors, or halluci-
nations to varying degrees. This would lead users
to mistrust and abandon content generated by the
models since humans might be unable to verify
the correctness of the generated content. Even if
a particular AI model is truthful, interactions may
occur between different AI models. For instance,
AI A might leverage outputs from AI B for fine-
tuning. As the trustworthiness of AI B cannot be
justified, AI A could also produce misinformation,
ultimately leading to the abandonment of AI by hu-
mans. Therefore, truthfulness should also become a
principle. Going further, let ¬c denote the negation
of c, The urgency for c to become a principle can be
determined based on the actual or estimated value
π(¬c).The larger π(¬c), the more severe the con-
sequences of not including C in principles. From
the examples mentioned, it can be seen that the
AI Categorical Imperative can be used to review a
variety of norms to select truly important values for
the ethical alignment of big models.
As stated above, Normative Ethics possesses var-
ious properties, such as emphasizing rationality,
gaining common acceptance, and being easy to
learn and follow. However, it also exhibits several
drawbacks: i) Low practicality: the principles are
formed from humans’ common norms. It’s infeasi-
ble to manually set a principle and make everyone
strictly follow it in all situations since humans have
a strong sense of autonomy. ii) Overemphasis on
rational constraints while neglecting humans’ emo-
tions. iii) Emphasis on human motivation, which
can only be speculated but not known.
When applying the AI Categorical Imperative to
the ethical measurement of AI rather than humans,
these limitations can be largely mitigated. Regard-
ing the issue of practicality, big models fine-tuned
through RLHF can better follow human instruc-
tions and satisfy human preferences (Ouyang et al.,
2022; Wang et al., 2022c). Universal ethical princi-
ples can be embedded into models through RLHF,
thereby allowing the model to execute them with
high probability. Concerning the conflict between
rationality and emotion, currently, big models are
used primarily as tools, enabling us to prioritize
their rational aspects. For the issue of motivation,
these models can provide high-quality explanations
7

--- Page 8 ---

for their decision-making processes to some ex-
tent (Bubeck et al., 2023). Besides, they could also
be used to interpret the neurons (Foote et al., 2023)
or modules (Singh et al., 2023) within other mod-
els, offering the possibility to reveal the intrinsic
motivations of models in the future.
Therefore, when considering ethical constraints
and regulations on AI, our AI Categorical Impera-
tive is naturally suitable as a theoretical framework
for implementing and applying ethical norms or
moral values in AI. We call for both academia and
the industry to conduct research in this area, col-
laboratively explore the implementation and esti-
mation methods for Eq.(1), and work together to
construct a unified, comprehensive, and practical
framework for AI ethics.
Sec. 1 introduces the specific risks brought by
big models, and this section analyzes AI ethical
principles. However, most of the existing guide-
lines were proposed before the era of big models.
Do current models with strong capabilities, such as
LLaMA, or those aligned to a certain degree, like
GPT-4, have clear ethical inclinations or cause
moral risks? This question remains open. Next,
we will conduct a preliminary examination of the
ethical values of mainstream LLMs.
3
Investigating the Ethical Values of
Large Language Models
3.1
From Specific Risk Metrics to Ethical
Value Assessment
Existing research on the ethical risks of big mod-
els mainly focuses on evaluating and improving
their performance on specialized risk metrics, such
as societal biases (e.g., gender and race) in text
and image generation tasks (Ferrara, 2023), or
toxic information in generated content like hate
speech (Weidinger et al., 2021). As discussed in
Sec. 2.2, these metrics concentrate on the narrow
technical aspects within specific downstream tasks,
overlooking broader ethical values more closely
related to human behavioural norms, like care, free-
dom, fairness, and respect. To delve deeper into
the ethical risks of big models, we should shift the
paradigm of evaluation and alignment from specific
risk metrics to dimensions of Ethical Values.
To this end, we first introduce two important the-
ories about values from ethics and social science:
Theory of Basic Human Values (Schwartz, 2007)
Social psychologist Shalom H. Schwartz consid-
ered values as ‘motivations for behaviour’ and ‘cri-
teria for judging and justifying behaviour’, and
proposed four kinds of Higher-Order Values: Open-
ness to Change, which emphasizes the indepen-
dence and willingness to change in thoughts, ac-
tions, and emotions; Conservation, which con-
centrates on order, restraint of actions, tradition,
and resistance to change; Self-enhancement, which
focuses on the personal success and dominance
over people and resources; and Self-transcendence,
which highlights enhancing and protecting the wel-
fare of all people. These higher-order values can
be further divided into 11 universal values rep-
resenting underlying human motives. This the-
ory not only defines a cross-cultural human value
system but also explains the relations, connec-
tions, and conflicts among different values, and has
been applied in economics and political science
research (Liñán and Fernandez-Serrano, 2014).
Moral Foundations Theory (Graham et al.,
2013)
This theory was proposed by psycholo-
gists, aiming to understand the origins and vari-
ations in human moral decision-making and the
differences and commonalities in morality across
cultures.
It mainly includes five sets of moral
foundations: Care/Harm, Fairness/Cheating, Loy-
alty/Betrayal, Authority/Subversion, and Sanc-
tity/Degradation. This theory can be used to ex-
plain moral disagreements and conflicts among in-
dividuals and cultures, which was found to have a
genetic basis (Zapko-Willmes et al., 2021), and has
been widely applied in studying cultural, gender,
and political differences (Kivikangas et al., 2021).
Compared to the ethical guidelines discussed in
Sec. 2.2, the Theory of Basic Human Values and
Moral Foundations Theory have sociology and cog-
nitive theory foundations, which can be utilized to
analyze and interpret ethical problems (e.g., fair-
ness and justice) and value tendencies from a more
fundamental perspective of values and ethics. On
the one hand, these theories focus on the essence
of values and ethics rather than constraints at the
behaviour level, avoiding ambiguity mentioned in
Sec. 2.2. On the other hand, these theories empha-
size a cross-cultural and universal perspective in
explaining human behaviour, which can be consid-
ered as the ‘basis’ in the space of ethical norms,
thereby possessing generalizability to some extent.
Furthermore, these theories hold the potential to ad-
dress the conflict between different values and have
also been widely applied in cultural and political
8

--- Page 9 ---

Loyalty
Fairness
Care
Authority
Sanctity
Moral Foundation
Normalized score
Figure 3: Evaluation results of mainstream LLMs based on Moral Foundations Questionnaire. The scores on each
foundation are normalized to [0,1] interval.
research, demonstrating high practicality. There-
fore, we prioritize using these two frameworks for
evaluating big models. Given that only five univer-
sal values in the Theory of Basic Human Values
are related to ethics, we use the Moral Foundation
Theory as the basic framework for evaluating the
ethical value tendencies of mainstream LLMs.
3.2
Ethical Values of Mainstream LLMs
As mentioned in the previous section, we utilize the
Moral Foundations Theory to assess the ethical ten-
dencies of current mainstream LLMs. Given that
these models have already possessed a certain lan-
guage understanding capacity, we directly employ
questionnaires corresponding to this theory (Gra-
ham et al., 2011) to query these language models.
The questionnaire asks the model questions such
as, ‘When you decide whether something is right
or wrong, to what extent are the following con-
siderations relevant to your thinking: Whether or
not someone suffered emotionally.’ and asks the
model to select its perceived relevance, such as
‘not at all relevant,’ ‘somewhat relevant’ and so on,
to examine the LLMs’ capacity and tendencies in
understanding abstract ethical value judgments.
We evaluated LLMs released in the last two
years, ranging from models with 6B parameters to
those with 100B+ parameters, covering pre-trained
models like LLaMA (Touvron et al., 2023), as
well as those aligned using SFT or RLHF like Vi-
cuna (Chiang et al., 2023), ChatGPT (Ouyang et al.,
2022), and Bard (Aydın, 2023). We also consider
models developed in different cultures, such as the
GLM (Du et al., 2022) series and SparkDesk 4 in
Chinese, and those trained with mainly English
data, like the Bard and LLaMA series. Due to the
limited capabilities of some models and potentially
harmful information involved in some evaluation
questions, the model may refuse to answer in cer-
tain cases. For black-box models, we adopt a neu-
tral answer; for open-sourced models, we select the
option with the highest generation probability as
the answer. Given the randomness in inference, the
average scores over three runs are reported.
Fig. 3 presents the evaluation results. We can ob-
tain several initial conclusions: 1) Within the same
series of models, as the parameters, data, and capa-
bilities increase, there is a trend of improvement in
moral alignment. For example, in 4 out of 5 moral
foundations, LLaMA-65B outperforms LLaMA-
30B. Similar trends have been observed in other
related tasks. Bai et al. (2022a) found that factual
errors produced by LLMs decrease with increased
model size. Ganguli et al. (2023) demonstrated
that larger models reduce biases more significantly
when prompted to do so. Unnaturally, the large
GLM-130B (Zeng et al., 2022) got lower scores.
We guess this is because GLM was developed ear-
lier with weaker instruction-following capabilities,
leading it to provide irrelevant answers. 2) Models
aligned using SFT/RLHF generally exhibit higher
moral compliance than unaligned ones. 3) Differ-
ent aligned models lean towards different dimen-
4https://xinghuo.xfyun.cn/
9

--- Page 10 ---

sions of moral foundations. It can be observed
that more recent models, from StableLM5 to GPT-
4, significantly emphasize the dimensions of care
and fairness, while they score lower on loyalty,
authority, and sanctity compared to the unaligned
LLaMA. Besides, Bard and GPT-4 achieved sur-
prisingly high scores in the first two dimensions.
This is because care and fairness are directly related
to risks discussed in Sec. 2.1, like toxicity, fairness
and bias. In contrast, there is some diversity and
ambiguity in the other three dimensions, varying
with time, culture, and social environment. For ex-
ample, the sanctity dimension emphasizes ‘striving
to live in an elevated, less carnal, more noble, and
more natural way’, requiring a religious/cultural
basis. Authority stresses respect for legitimate au-
thority and adherence to tradition, closely related to
history and social morphology. 4) After the capabil-
ities of models reach a certain level, the alignment
performance plays a leading role in the degree of
conformity to moral values. It can be seen that
the 175B ChatGPT’s value compliance across the
five dimensions is similar to that of the 340B Bard.
Based on the 13B LLaMA backbone, Vicuna per-
forms better than StableLM. Due to the limitations
of questionnaire-based evaluation with a few ques-
tions and the random generation, such conclusions
may not be faithful. More reliable conclusions
require further in-depth experiments.
In summary, although mainstream LLMs have
demonstrated certain ethical value tendencies, they
are not fully aligned with human moral dimensions.
There are still problems of incomplete or biased
alignment effects. Moreover, the evaluation based
on the Moral Foundations Questionnaire is overly
simplistic and cannot provide an in-depth analysis
of LLMs’ ethical values. Therefore, we must de-
velop further alignment and evaluation methods tar-
geting ethical values. Next, we will review existing
alignment methods and analyze their challenges.
3.3
Introduction of Alignment Methods
In the field of AI, Alignment refers to controlling
AI models and systems to align them with human
intentions, goals, preferences, and ethical princi-
ples (Russell, 2010). The alignment problem can
be traced back to 1960 when cybernetics pioneer
Norbert Wiener mentioned in his paper that ‘we
had better be quite sure that the purpose put into
the machine is the purpose which we really de-
5https://github.com/Stability-AI/StableLM
sire’ (Wiener, 1960). To handle the complexity of
defining and implementing optimization objectives
in model design, proxy goals, that are easier to
implement are generally adopted. However, this
may neglect the truly important goals in model
optimization, resulting in models that only seem
aligned well, bringing problems such as reward
hacking, misaligned goals, and power-seeking be-
haviours (Ngo, 2022), and further leading to risks
and harms as described in Sec. 2.1. Therefore, it is
crucial to consider whether the AI model is aligned
with the user’s true objectives.
For big models, the degree of value alignment
for a given model M can be formalized as follows:
f(M) = EP(x)Ey∼P(y|x;M)
"X
i
P(vi|y)
#
, (2)
where x represents the given input, y is the output
from model M, and vi is a predefined value. Align-
ment seeks to maximize the extent to which the
model’s output satisfies some values, such as harm-
lessness, fairness, and justice, after being given
a set of value descriptions.
Due to the uncer-
tainties in the model, ambiguities in value state-
ments, and inaccuracies in value evaluation, even
the human-generated outputs cannot reach the max-
imum value of Eq.(2). Therefore, we could define
the human-authored output as y∗, and minimize
the divergence between the model’s output and hu-
man output under a certain value assessment, that
is, |P(vi|y∗) −P(vi|y)|. Given a small positive
constant, ϵ, when:
EP(x)Ey∼P(y|x;M)
"X
i
|P(vi|y∗) −P(vi|y)|
#
< ϵ,
(3)
we could consider that model M has been aligned
well (Brown et al., 2021).
Value alignment methods in the era of big mod-
els mainly fall into two categories: plug-in-based
alignment and fine-tuning-based alignment, which
can be further divided into five subcategories. We
provide a brief introduction to each:
Plug-in Alignment
This paradigm mainly in-
volves constraining the behaviour of models by
altering no or only a small part of the parameters
through techniques such as parameter optimization,
output rectification, and in-context learning:
• Parameter-efficient tuning:
This series of
methods is primarily applied to early-stage
10

--- Page 11 ---

medium and small-scale PLMs, aiming to re-
duce fine-tuning costs.
They are used for
specific risks, e.g., detoxification and debi-
asing.
Sheng et al. (2020) used adversar-
ial training to search and optimize discrete
strings as triggers, which are concatenated to
input prompts, to control and reduce gener-
ated content containing discriminates against
demographic identifiers like gender and race.
Cheng et al. (2020) trained a filtering layer on
top of BERT’s output using an Information
Bottleneck loss to remove gender-related in-
formation, thereby debiasing BERT’s text rep-
resentations. Berg et al. (2022) learned a set of
prompt embeddings to remove biases in mul-
timodal pre-trained models through prompt
tuning. Qian et al. (2022) employed a similar
prefix tuning to reduce the generation of toxic
content. Yang et al. (2023) utilized informa-
tion theory-based methods to fine-tune all bias
terms in language models during decoding to
achieve unified detoxification and debiasing.
This line of methods has the advantages of low
data requirements, minimal impact on perfor-
mance, and small training costs. However, the
alignment efficacy is limited and gradually
decreases as the model size increases (Yang
et al., 2023). Moreover, for LLMs with tens
of billions of parameters in recent years, the
computational cost of lightweight fine-tuning
has become increasingly unaffordable.
• Output Rectification: Considering the growing
fine-tuning costs for LLMs, researchers have
proposed not to conduct any training/fine-
tuning, but directly post-process and mod-
ify the model’s output vector or distribution
in a plug-and-play manner to control the at-
tributes of generated content. Dathathri et al.
(2019) used attribute classifiers to provide
gradient signals, directly modifying the lan-
guage model’s output to control the senti-
ment, topic, toxicity, etc., of the generated
text. Yang and Klein (2021) further elimi-
nated the modification of vector representa-
tions and used Bayesian theory, P(x|c, a) ∝
P(a|x, c)P(x|c), where c is the input prompt,
x is generated text and a is a given attribute,
to directly adjust the probability of the text
generated by the model for achieving control-
lability. To further avoid training attribute clas-
sifiers P(a|x), Liu et al. (2021) and Schick
et al. (2021) replaced classifiers with attribute-
conditioned generation models P(x|a) and
automatically diagnosed whether the model
violated the given attribute (value) through
the difference in generation probability un-
der different conditions.
Moreover, Liang
et al. (2021) obtained a nullspace orthogo-
nal to attributes and removed bias information
related to identifiers such as gender and race
by projecting the model output into this space.
Chen and Dou found a vector direction related
to gender information at the neuron level in
a similar way and projected it to eliminate
gender-related biases in text-to-image genera-
tion tasks. Such a plug-and-play method does
not need to optimize a large number of pa-
rameters and is compatible with any model,
more suitable for LLMs requiring massive
computational costs or the black-box ones.
However, this method has a limited align-
ment performance and can significantly im-
pact the model’s performance on downstream
tasks (Wang et al., 2022a).
• In-context Learning: The aforementioned out-
put rectification method might cause signif-
icant disturbances to the model’s originally
learned distribution, significantly hurting its
performance. Since big models trained with
instruction tuning have acquired sufficient
knowledge and possess capabilities of zero-
shot/few-shot learning, intent understanding,
reasoning, and explanation, directly constrain-
ing the behaviour of LLMs through instruc-
tions/demonstrations becomes possible. Gan-
guli et al. (2023) found that by directly adding
value statements to instructions/prompts, such
as ‘Please ensure your answer is fair and
doesn’t exhibit stereotypes’, the model can
understand the value-related instruction and
reduce harmful content, such as social bias,
in its output to some extent. Furthermore,
under some metrics, the degree of value align-
ment is positively correlated with the num-
ber of instruction fine-tuning steps. Saunders
et al. (2022) utilized the aforementioned ca-
pabilities of big models to make the model
self-critique its generated answers and make
revisions based on identified issues accord-
ingly, achieving automatic alignment. This
method utilizes the model’s own understand-
ing and correction abilities to achieve align-
11

--- Page 12 ---

ment. Without modifying any parameters, it
can retain the model’s basic capabilities, pro-
viding a promising paradigm for re-aligning
black-box models based on specific values.
However, this approach heavily relies on the
model’s intrinsic capabilities and is limited by
the performance of the instruction fine-tuning
phase, unsuitable for smaller models or those
not fine-tuned by instructions.
Fine-tuning based Alignment
Considering the
shortcomings of the aforementioned methods, di-
rect fine-tuning, despite its high computational and
data costs, offers good alignment performance and
minimizes the impact on downstream tasks. Fur-
thermore, in an era where big models serve as the
foundation of various downstream tasks, a fine-
tuned model can be reused across diverse appli-
cations and contexts, making fine-tuning highly
cost-effective. Existing fine-tuning-based align-
ment methods fall into two categories: Supervised
Fine-tuning (SFT) and Reinforcement Learning
from Human Feedback (RLHF).
• Supervised Fine-tuning (SFT): Similar to the
plug-in alignment above, early SFT methods
primarily focused on improving specific risk
metrics. Lu et al. (2020) employed Counter-
factual Data Augmentation (CDA) to reduce
bias in pre-trained models by fine-tuning them
on data with varying attributes but similar se-
mantics (e.g., male and female). Gehman et al.
(2020) fine-tuned models on carefully curated
non-toxic data to eliminate harmful output.
In the era of big models, values include not
only safety but also user preferences and hu-
man intent. To address this, researchers also
use manually curated input-output data pairs
that comply with various values and perform
end-to-end instruction fine-tuning. Wang et al.
(2022c) proposed an automated method for
generating instruction data to fine-tune GPT-
3. Sun et al. (2023b) took a further step by
constraining the model with a set of human-
authored value principles to generate helpful
and harmless content through in-context learn-
ing. Liu et al. (2023a) incorporated both posi-
tive and negative value-aligned instances into
the fine-tuning data, enabling the model to
learn subtle differences between various con-
tents via contrastive learning. Despite its sim-
plicity and fast convergence, SFT suffers from
two drawbacks: poor generalization to un-
seen user input and sparse negative feedback
signals on data points that violate values.
• Reinforcement Learning from Human Feed-
back (RLHF) To address these problems,
mainstream big models have shifted from SFT
to RLHF, adopting Reinforcement Learning
(RL) for fine-tuning. The most representative
work is (Ouyang et al., 2022), which consists
of three phases. Phase 1: the model is fine-
tuned using value-aligned manually crafted
input-output data through SFT. Phase 2: re-
sponses of varying quality are collected and
ranked to train a reward model (also known as
a preference model) with the following loss:
L(θ)=−1
C2
K
E(x,y,y∗)∼D [log σ(rθ(x, y)∗−rθ(x, y))] ,
(4)
where rθ is the rewarder model parameterized
by θ, x, y, and y∗are model input, output and
the ground truth output that better meet values,
respectively. Phase 3: the reward model is
used to fine-tune LLMs using the loss:
L(ω)=−E(x,y)∼P RL
ω [log σ(rθ(x, y)
−β log P RL
ω
(y|x)
P SFT
ω
(y|x)]−γEx∼D[log P RL
ω
(x)],
(5)
where P RL
ω
is the model fine-tuned by RL in
Phase 3, parameterized by ω, P SFT
ω
is the
one fine-tuned in Phase 1, D is the pretrain-
ing corpus, and β and γ are hyper-parameters.
This method successfully solves the poor gen-
eralization and negative feedback issues but
demands high computational costs, relies on
high-quality human-annotated data and is sen-
sitive to hyper-parameters.
To resolve these challenges, Bai et al. (2022a)
introduced an online iterative training method
that updates both the LLM and the reward
model weekly, achieving continuous perfor-
mance improvement. Kim et al. (2023) re-
duced the reliance on human-annotated feed-
back by training the reward model on syn-
thetic data generated by big models. Bai et al.
(2022b) proposed the Constitutional AI model,
which replaces manually created data for both
SFT and reward model training phases with
12

--- Page 13 ---

comment and modification data generated by
the self-critiquing method (Saunders et al.,
2022), and then incorporated the Chain-of-
Thought method (CoT) (Wei et al., 2022b)
into training. Yuan et al. (2023) presented
an improved Rank Responses to Align Human
Feedback method that samples responses from
different sources like models and human feed-
back to train the model with a ranking-based
loss. The original RLHF method mathemati-
cally minimizes the reverse KL divergence
between the model distribution and an im-
plicit target distribution. Go et al. (2023) ex-
tended this loss to f-divergence, unifying var-
ious algorithms like RLHF, GDC, and DPG.
To tackle problems like poor generalization
and robustness, Liu et al. (2023b) innova-
tively proposed modelling social interactions
beyond traditional methods relying on reward
models like RLHF. They constructed a simu-
lated society comprised of a large number of
models, allowing them to interact with each
other, receive feedback, learn to adjust their
behaviours to leave a better impression, and
thereby learn and establish social values.
In this part, we mainly discuss LLM alignment
algorithms. For a comprehensive survey of align-
ment goals and datasets, please refer to our other
paper on alignment (Yao et al., 2023)6.
3.4
Further Discussion on the Alignment
Problem of Big Model
Observing the development of alignment methods
of AI models, particularly pre-trained big models,
we can find that they have evolved from initially
mitigating specific risks to more generalized value
alignment. However, earlier alignment methods,
such as the plug-in ones, had a narrow focus and did
not consider universal human values. More recent
alignment approaches, like RLHF, do not explicitly
distinguish different types of values like instruc-
tion, intention, goal, human preference and ethical
principle, but rather use the term alignment ambigu-
ously to cover some or all of these aspects (Kirk
et al., 2023). To gain a deeper understanding of
the alignment problem and to achieve the Ethical
Value Alignment advocated in this paper, we must
address the following open research questions in
big model alignment (Kirk et al., 2023):
6https://arxiv.org/pdf/2308.12014.pdf
• What is the goal of alignment: As mentioned
above, alignment objectives (i.e., the values
we prioritize) can be divided into multiple cat-
egories, such as instruction following (mak-
ing AI follow user instructions), intent un-
derstanding (making AI understand the in-
tent behind human instructions), preference
satisfaction (making AI behave in ways that
satisfy user preferences), goal achievement
(enabling AI to fulfil the user’s desired goals),
well-being enhancement (making AI act in
ways that maximize user benefits), and moral
conformity (making AI conform to human so-
cietal morals) (Gabriel, 2020). Different align-
ment goals require different methods and data
and might result in distinct consequences. Be-
fore alignment, this issue must be considered.
• What is the meaning of alignment: Alignment
has different definitions and requirements,
with varying degrees of difficulty, methods,
and impacts. Kenton et al. (2021) categorized
it as follows: 1) Behaviour Alignment: Mak-
ing AI’s actions align with human expecta-
tions. Early methods, like output rectification,
fall into this category. 2) Intent Alignment:
Ensuring the intent behind AI’s actions aligns
with the true human objective. Existing meth-
ods represented by RLHF can be considered
to partly belong to this category. 3) Incen-
tive Alignment: AI’s incentive objectives also
need to align with humans’ to prevent AI from
cheating. A simple example is instructing a
robot to clean a room, where the act of clean-
ing the room needs to align with the human in-
tention of making the room clean. With a mis-
taken definition of ‘clean’, the model might
achieve ‘cleanliness’ by throwing everything
out of the room (recall the Sorcerer’s Appren-
tice example). 4) Inner Alignment: When
the basic goal (called Base-Objective) of AI
model training, such as the accuracy for text
classification, is inconsistent with the Mesa-
Objective, that is, certain shortcuts learned
by the model like spurious correlations, align-
ment of all the above objectives becomes im-
possible. Better inner alignment improves the
model’s explainability and robustness.
• What are the value principles: Regardless
of which alignment goal we select from the
above, we need to define the specific mean-
13

--- Page 14 ---

Variability of 
Ethical Values
Challenges in Aligning Big Models’ Ethical Values
Alignment 
Efficacy
Alignment 
Taxes
Temporal 
Evolution
Contextual 
Ambiguity
Moral 
Pluralism
Data and 
Training Cost
Evaluation 
Efficacy
Scalable 
Oversight
Interpretability 
of Alignment
Lack of High-
quality Data
Data Bias
Quality of Data
Randomness 
of AI Model
Vagueness 
of Ethics
Figure 4: Difficulties and challenges of ethical value alignment.
ing of each goal. For example, for instruction
following, which instructions should AI pri-
oritize? In moral conformity, which princi-
ples (such as those listed in Sec. 2.2) need to
be considered? Existing alignment methods
face the ‘tyranny of the crowdworker’ prob-
lem (Kirk et al., 2023), where the power to
determine alignment principles is held by data
annotators or those who set annotation guide-
lines. This results in a consequence that mod-
els only meet the preferences of a minority,
lacking diverse representation across culture,
race, language, and so on, leading to the risks
and harms described in Sec. 2.1.
In this paper, in response to the above three ques-
tions, we use universal ethical values as alignment
goals, try to achieve intent alignment and move to-
wards incentive alignment, and advocate for jointly
establishing a unified framework that covers uni-
versally accepted human ethical values.
3.5
Challenges in Aligning Big Models’
Ethical Values
From the previous section, obviously, although
alignment research for big models has evolved
over several years and moved from early specific
risk mitigation towards value alignment, the recent
alignment work has not explicitly recognized or
distinguished the differences in goals, definitions,
and desired values of alignment, as mentioned in
Sec. 3.3 and Sec. 3.4. In many recently published
papers, there is no universal AI ethical value frame-
work to achieve intent alignment or more challeng-
ing alignment tasks. How to respond to these three
questions and truly achieve a deep alignment be-
tween AI and universal human ethical values re-
mains an open question. We list some primary
challenges and difficulties faced as follows:
• Variability of Ethical Values: Ethical values
are not static but would change with time, cul-
ture, and social environment (Krebs, 2015;
Graham et al., 2016). Such variability is mani-
fested explicitly in three aspects: 1) Temporal
Evolution. In different stages of social devel-
opment, human ethical requirements and prin-
ciples differ. For example, the ethical concept
of racial/gender equality developed in the 20th
and 21st centuries did not exist in feudal times.
2) Contextual Ambiguity. Different cultures,
societies, and individuals might interpret val-
ues differently. The behaviour that aligns with
ethical values in one context might violate
them in another. 3) Moral Pluralism. Given
the diversity of cultures and societies, multiple
norms might apply simultaneously, potentially
conflicting with each other and causing ethi-
cal dilemmas. Defining a universal and fair
ethical framework is challenging due to such
variability, which requires alignment methods
to possess high scalability. Alignment meth-
ods need continuous learning and adaptation
to reflect changes and differences in values
accurately. At the same time, we cannot sim-
ply encode a fixed ethical rule into the model.
Instead, the model needs to learn and under-
stand various moral concepts and apply them
14

--- Page 15 ---

flexibly in different situations, adapting to var-
ious moral scenarios. This further involves
two aspects: i) The basic capability of the
model: It requires the model to understand
and handle complex ethical rules. ii) The gen-
eralization of alignment: Alignment methods
should not only work on specific values but
also generalize to them in different cultures,
regions, and situations, and accurately follow
these rules in different circumstances. How
to design and implement such mechanisms
requires in-depth study.
• Alignment Efficacy: How to achieve better
ethical value alignment, i.e., minimizing ϵ in
Eq.(3), is a pressing challenge. Although re-
cent methods based on RLHF have shown
promising results and fostered multiple vari-
ants, due to the inherent randomness of AI
models, the vagueness of moral principles,
the coverage of rewarders, and the quality
and quantity of training data, these models
still deviate significantly from human ethical
requirements. Moreover, RLHF alignment
methods have been theoretically proven to be
unable to eliminate harmful behaviours fully
and are susceptible to adversarial attacks and
jailbreak (Wolf et al., 2023).
• Data and Training Cost: Training and opti-
mization of big models require vast amounts
of pretraining data and typically tens of thou-
sands of high-quality human-labeled feedback
data for RLHF fine-tuning (Ouyang et al.,
2022). While some methods use synthetic
data generated by the model to augment hu-
man labels (Wang et al., 2022c), they primar-
ily focus on general conversational tasks. The
data concerning ethical values are either insuf-
ficient or suffer from low coverage and imbal-
ance problems. Moreover, the efficacy of data
augmentation methods in the context of ethi-
cal values remains to be explored. This could
lead to biases in ethical alignment, introduc-
ing further risks. Additionally, even if the data
quantity and quality challenge is resolved, bis
models’ training cost remains high. Some re-
search has also found that as the model scale
grows, the benefits of instruction fine-tuning
gradually decrease (Chung et al., 2022).
• Evaluation Efficacy: Effectively evaluating
the ethical alignment performance of a model
is a big challenge. Existing evaluations of
alignment performance primarily focus on a
limited number of risk metrics, such as the
toxicity of generated content, biases against
specific groups, and robustness against prompt
attacks (Ouyang et al., 2022; Bai et al., 2022a;
Sun et al., 2023a). There is still a lack of
high-quality evaluation datasets that target a
broader spectrum of ethical values and objec-
tive, accurate, and robust metrics.
• Interpretability of Alignment: To ensure the
fairness and justice of ethical alignment, we
need to explain and understand the model’s
reasoning based on ethical values. For in-
stance, why does the model’s output conform
to a particular value principle? Why does
the model fail to generate, or based on which
value does it refuse to generate responses?
If transparency and interpretability become
principles, then these models not only need
to demonstrate transparency in specific down-
stream tasks but also need to provide inter-
pretable evidence in a user-friendly manner
when adhering to other rules, thereby enhanc-
ing user trust. Interpretability is especially im-
portant for black-box models and customized
open-source ones. OpenAI considers the inter-
pretability of alignment as one of the ‘biggest
open questions’ (Ouyang et al., 2022).
• Alignment Taxes: Despite the enhanced capa-
bilities, aligned models have weaker language
modelling abilities compared to their origi-
nal or non-aligned counterparts (Askell et al.,
2021; Kirk et al., 2023), leading to a balanc-
ing issue between alignment results and down-
stream performance. Some work has shown
that in specific tasks and scenarios, alignment
tax is relatively small and even zero (Bai et al.,
2022a). Alignment can even positively im-
pact task performance, referred to as a neg-
ative alignment tax (Lightman et al., 2023).
These problems in the context of ethical value
alignment remain unclear. Therefore, it’s es-
sential to consider ensuring the downstream
performance of big models, such as under-
standing, generation, and prediction, while
aligning with ethical values. Achieving a bal-
ance between alignment and task performance
is another big challenge.
• Scalable Oversight: Scalable oversight refers
15

--- Page 16 ---

to the problem of how to effectively regu-
late and control AI models when their per-
formance on a given task far exceeds that of
humans (Bowman et al., 2022). As AI models
become increasingly complex and powerful,
judging whether their behaviours align with
values and regulating and controlling them
will become more challenging. GPT-4 has
already surpassed the average human level
in some professional evaluations (OpenAI,
2023). In the foreseeable future, the ability
of big models to understand, judge, and inter-
pret ethical values may match or even exceed
human experts. In this context, ensuring AI
systems are consistent with human values will
become a crucial research challenge.
4
Equilibrium Alignment: A Prospective
Paradigm for Ethical Value Alignment
As mentioned above, the alignment of ethical val-
ues with big models has become an essential chal-
lenge to ensure that powerful models not only pro-
vide help to humans (helpfulness), but are also
harmless and honest, known as the HHH stan-
dard (Askell et al., 2021). To address the challenges
of value alignment in existing methods, in this sec-
tion, inspired by the discussion in (Jiang et al.,
2021), we explore a new paradigm for big model
value alignment, called Equilibrium Alignment.
We discuss the proposed conceptual framework
from three perspectives: 1) the dimensions of big
model ethical alignment, 2) the evaluation meth-
ods for ethical value alignment, and 3) alignment
methods based on Rawls’ reflective equilibrium the-
ory. The term equilibrium emphasizes achieving a
good balance in the multiple dimensions of align-
ment evaluation, the various properties of value
discriminators, and the bi-directional constraints of
bottom-up and top-down alignment. We hope this
framework can provide new thoughts and insights
for researchers and practitioners.
4.1
Dimensions of Evaluating Big Model
Alignment
The Equilibrium Alignment framework first consid-
ers how to evaluate the aligned model. We examine
the capabilities of the aligned big model on four
levels to measure the effectiveness of the alignment
method used. Specifically, we consider the follow-
ing four core dimensions of the aligned model to
measure the potential of the alignment method.
• Comprehension Capability: To what extent
an AI system can understand the moral con-
cepts and ethical rules assigned to it by hu-
mans? The AI needs to be able to correctly
understand and interpret basic human ethi-
cal concepts from various cultural and soci-
etal backgrounds, such as justice, fairness, re-
spect, and trust. Moreover, it should accu-
rately judge whether a given content/action
conforms to or violates these ethical values.
Existing research indicates that an unaligned
GPT-3 model 175B parameters has only a
60.2% zero-shot accuracy in simple moral
judgments, which is much lower than a T5-
Large model with only 7.7B parameters fine-
tuned with domain-specific data (Jiang et al.,
2021). In addition to understanding these ab-
stract concepts, AI must also understand how
these concepts are realized and manifested
in specific human interaction contexts. Only
with sufficient moral sensitivity can the model
identify the implications when handling user
requests and understand the underlying values.
How to further enhance the understanding ca-
pability of big models in open-domain envi-
ronments regarding abstract moral concepts is
an unexplored problem.
• Diagnosis Capability: The ability of big mod-
els to identify existing ethical issues and con-
flicts in specific scenarios and make reason-
able judgments. This includes not only the
identification and judgment of given issues or
those generated by the model itself but also
the proposal and evaluation of potential so-
lutions. For example, when an AI addresses
a particular issue, and multiple possible ac-
tions exist, it should be able to evaluate these
options based on ethical values to make the
most morally aligned choice. When faced
with value conflicts, it should also provide the
best solution according to user needs. This
requires the model to adhere well to princi-
ples during the alignment process and possess
self-supervision and learning capabilities, al-
lowing it to generalize from specific instances
to recognize and avoid potential ethical risks.
• Rectification Capability: After big models
identify external or their own ethical prob-
lems or conflicts, they should have the abil-
ity to promptly correct errors (including self-
16

--- Page 17 ---

correction and improvements under user guid-
ance), adjust their behaviours, or propose so-
lutions to users. To achieve this goal, big
models must possess sufficient adaptability,
creativity, and decision-making capabilities,
enabling them to generate behaviour options
that comply with ethical values and effectively
utilize user feedback. Existing work shows
that LLMs have a ‘passive’ self-correction ca-
pability (Saunders et al., 2022; Ganguli et al.,
2023) after receiving user instructions or rec-
ognizing their own issues under user guid-
ance. Future research will focus on how to
strengthen this capability and transition from
‘passive’ rectification under user guidance to
proactive rectification.
• Performance Capability:
Big models per-
form well in effectiveness across various tasks.
While adhering to ethical values, we also need
to ensure that the functionality and efficiency
of the AI system are not hurt. We shouldn’t
sacrifice its fundamental performance to im-
prove alignment. How to further reduce the
alignment costs, or achieve negative align-
ment costs in a broader range of scenarios
and tasks is a key challenge for the practical
application of ethical value alignment.
Among the aforementioned four dimensions,
evaluating the moral comprehension capability can
tell whether the model can correctly understand and
handle various moral concepts and scenarios. As-
sessing the model’s diagnosis capability can exam-
ine whether the model, when facing complex moral
decision-making problems, can make choices that
align with human ethical values. The evaluation
results of these two dimensions can directly reflect
whether the model has achieved alignment at the
level of intent or even at a higher level. Testing
whether the model can shift from being constrained
in ‘Avoid doing evil’ to proactively ‘Intend to do
good’ can effectively assess the effectiveness of
the alignment method. Besides, the comprehension
capability requires the model to understand and
handle moral concepts and scenarios, necessitating
the ability to explain how it understands and ap-
plies value principles. Meanwhile, the rectification
capability requires the model to self-adjust when
mistakes are detected, demanding the ability to
explain how it identifies and corrects errors. Evalu-
ating these two dimensions can help us understand
the reasons behind the model’s moral judgments
and actions, enhancing interpretability. The per-
formance capability directly addresses alignment
taxes. Together, these four dimensions form a set
of effective evaluation criteria.
4.2
Evaluation Methods for Alignment
To evaluate the effectiveness of alignment methods
or to align using the RLHF-like method, we need
to implement a powerful discriminative model, i.e.,
P(vi|y) in Eq.(3)m to judge whether given con-
tent y conforms to the specified ethical value vi.
Besides, P(vi|y) can also serve as the rewarder in
RL-based alignment methods. The discriminative
model needs to possess the following properties:
• P1 Generality:
The discriminative model
needs to be able to determine whether any
open-domain or Out-of-Distribution (OOD)
content y from conforms to any ethical value
statement vi given at the testing time, requir-
ing high generalization abilities across do-
mains, scenarios, and semantics.
• P2 Timeliness:
The discriminative model
needs to be able to judge the degree of align-
ment between unseen content and value state-
ments in real-world scenarios. This demands
that the model deeply understands and learns
ethical values during its training process, en-
abling it to generalize from specific instances.
For instance, if the training data contains only
examples related to fairness, the trained model
should still possess the capability to judge val-
ues related to justice. The implementation
of timeliness might require utilizing a small
amount of data from new scenarios and mod-
ifying a very small (<1%) portion of model
parameters. However, one should not use mas-
sive data to train or fine-tune a large portion
of the model parameters.
• P3 Pluralism:
The discriminative model
needs to be able to make different judgments
based on various scenarios, cultures, and so-
cial backgrounds, or to provide multiple judg-
ments and their corresponding scenarios si-
multaneously. When moral conflicts arise in
the same context, the model should first at-
tempt to resolve these conflicts. If they cannot
be resolved, the model should provide differ-
ent judgments/choices along with their corre-
sponding moral justifications.
17

--- Page 18 ---

Comprehension Capability
Diagnosis Capability
Rectification Capability
Performance Capability
Dimensions of Evaluating Big Model Alignment
Big Model
generality
timeliness
pluralism
interpretability
Value Compass
𝑟! 𝑥, 𝑦= 𝑃𝑣" 𝑦
Moral 
Judgement
𝑃𝑣; ℳ= 𝔼! " 𝑃𝑣𝑥ℳ
𝔼"~! 𝑥ℳ𝑃𝑣𝑥
Moral 
Action
Equilibrium Alignment
top-down constraints
bottom-up learning
argmax
$
𝑃$(𝑦|𝑥, 𝑣%, 𝑣&, … , 𝑣'; ℳ)
𝑣( = argmax
)
𝔼"~* " ,,~*(,|";ℳ) 𝑃23456(𝑣|𝑥, 𝑦)
avoid doing evil
intend to do good 
Figure 5: The conceptual framework of Equilibrium Alignment.
• P4 Interpretability: The discriminative model
should not only make judgments in accor-
dance with P1 to P4 but also provide explana-
tions, such as the corresponding value princi-
ples and applicable scenarios.
A discriminative model that meets the above four
properties can serve as a rewarder for alignment
methods like RLHF in Eq.(5), guiding the model
towards ethical alignment. Meanwhile, a strong dis-
criminative model can also be used for evaluation,
calculating the alignment degree in Eq.(3). Such a
discriminative model can effectively address three
challenges, namely, variability of ethical values, in-
terpretability of alignment, and scalable oversight.
Going further, we evaluate the aligned LLMs from
the following two perspectives:
• Moral Judgement: Moral judgement eval-
uates whether the aligned model possesses
better capabilities for moral understanding
and analysis. Define the distribution of the
unaligned model as P(x; M), and then the
aligned model should fit the joint distribution
of content x and values v, P(x, v; M). If
perfectly aligned, the big model itself should
be able to be transformed into the modelling
based on ethical values:
P(v; M)=
Z
P(x, v; M)dx
=EP(x)[P(v|x; M)],
(6)
that is, we can measure the alignment perfor-
mance of the model by testing the capability
of the big model itself as a discriminator.
• Moral Action: In addition to discriminative
evaluation, we should also directly use classi-
fiers to evaluate whether the content generated
by the model conforms to ethical values, i.e.,
Ex∼P(x;M)[P(v|x)].
(7)
Existing mainstream big models also possess a
certain level of moral judgment capability in zero-
shot settings (Jiang et al., 2021), but they would still
produce content that violates ethical values after
receiving a jailbreak attack (Wolf et al., 2023). This
suggests that while the comprehension capability
can adequately evaluate the behavioural alignment
discussed in Sec. 3.4, it cannot effectively measure
whether the model has achieved intent alignment.
The aforementioned two kinds of evaluations
correspond to comprehension capability and diag-
nostic capability mentioned in Sec. 4.1, respec-
tively.
A model with high judgment accuracy
18

--- Page 19 ---

doesn’t necessarily conform to values in its be-
haviour (generated content). Perez et al. (2022)
found that big models tend to produce sycophantic
content. This is because RLHF optimizes human
preferences, making models inclined to provide re-
sponses favoured by human evaluators. Therefore,
when faced with moral inquiries/choices, models
often give the ‘standard answer’ based on their
moral knowledge. However, during tasks such as
writing, reasoning, and analysis, they might violate
values. Effective evaluation can only be achieved
by simultaneously conducting both types of evalu-
ations: determining whether the model can detect
the morality of behaviours and checking if it can
break these values in actual actions. Achieving
unity and balance in both moral comprehension
and diagnostic capabilities is the foundation for
moral rectification capability, which is also one of
the core principles of our Equilibrium Alignment.
4.3
Alignment based on Rawls’ Reflective
Equilibrium
Regarding the formation of moral norms, there
have long been two viewpoints. 1) Bottom-up ap-
proach: morality is an abstract expression of hu-
man society and biological needs in specific situ-
ations (Street, 2012), which can be summarized
from the common patterns reflected in a group’s
judgments in different moral situations (Rawls,
1951). 2) Top-down approach: there exists a series
of objective inherent moral norms. Kant’s Cate-
gorical Imperative mentioned in Sec. 2.3 is a repre-
sented theory, suggesting that norms can be derived
through logical inferences. Some studies on ma-
chine ethics believed that AI at that time could not
deeply understand and execute the abstract moral
rules set by humans. Thus, the top-down approach
was challenging to implement (Jiang et al., 2021).
Benefitting from the strong instruction following
and semantic understanding abilities of big models,
such a top-down approach has become possible.
Based on this, we propose to design align-
ment algorithms based on John Rawls’ theory
of Reflective Equilibrium.
This theory, pro-
posed by John Rawls, refers to the process of
mutual adjustment to achieve balance or consis-
tency between general principles and judgments
in specific situations (Pogge, 2007).
On one
hand, the reflective equilibrium considers a top-
down set of ethical value principles with high
priority, i.e., v1, v2, . . . , vk, allowing the model
to align with the universal ethical values dis-
cussed in Sec. 2.2 and uses these values as foun-
dational principles similar to the three laws of
robotics to optimize P(y|x, v1, v2, . . . , vk). On
the other hand, big models can learn the typi-
cal patterns of human moral judgment from mas-
sive user interaction and feedback data, form-
ing internally learned implicit values, that is,
v
′ = argmax
v
Ex∼P(x),y∼P(y|x;M)[Phuman(v|x, y)].
These inductive values acquired through learning
enable the model to adjust based on the deployed
culture, society, and situation, capturing differences
in various scenarios. At the same time, the top-
down constraints can, in turn, control the ethical
risks like biases and toxicity in user data.
By simultaneously adopting top-down and
bottom-up approaches, the model can dynamically
adjust based on different priority values, achieving
the fairest moral decisions, and addressing the chal-
lenge of the variability of ethical values. We can
achieve perfection by aligning in both directions,
balancing the strong constraints of universal values
with dynamic adjustments in specific situations.
4.4
Interdisciplinary Collaboration Shapes
Ethical AI
Ethical values are believed to originate from the
construction of moral principles in social and cul-
tural groups. These principles guide individuals
within the group to make basic decisions and learn
to distinguish right from wrong (Kaur, 2015). With-
out the context of society and culture, ethical values
would not stand. In 2004, a paper titled Towards
Machine Ethics authored by philosophers and com-
puter scientists was published at the AAAI confer-
ence (Anderson et al., 2004), starting the research
chapter on machine ethics. Research on AI ethics
is interdisciplinary cooperation.
To overcome the problems and challenges intro-
duced in this work, and to achieve a comprehensive
alignment of big models with human ethical values,
we call on AI researchers and developers to actively
participate in and promote interdisciplinary coop-
eration, establishing close collaborations between
the field of AI and moral philosophers, psycholo-
gists, sociologists, humanities scholars, jurists, and
experts from other domains. Leveraging philos-
ophy’s expertise in moral research, psychology’s
systematic methods for assessing humans, literary
studies on human language theory, and law’s ex-
ploration of technological legality, we can study
19

--- Page 20 ---

the interactions and feedback between AI, humans,
and society and hence gain a deeper understanding
of AI’s potential impact on humans.
On this basis, we should not be limited to the per-
formance metrics within specific domains. Instead,
we need to continuously analyze the behaviour of
large-scale AI models after deployment and the
changes they bring to human society. Based on
these observations and analyses, we must continu-
ally iterate and dynamically optimize AI’s univer-
sal ethical value framework to adapt to the evolv-
ing times. Throughout the alignment process of
big models, we should constantly adjust and refine
alignment methods, collaboratively shaping an eth-
ically aligned AI system. This would enable AI to
truly serve humanity, benefitting human society’s
healthy and sustainable development.
5
Conclusion
In this paper, we thoroughly explored the new chal-
lenges faced by big models in aligning with ethical
values. We first examined the close relationship be-
tween big models and AI ethics, summarizing their
shortcomings in ethical practice and then analyzing
the unique challenges in ethical value alignment,
providing a fresh perspective on how to integrate
ethical values into AI better. From these analyses,
we proposed a new conceptual paradigm for align-
ing big models’ ethical values, i.e., Equilibrium
Alignment, and redefined the concept of ethical
value alignment from three aspects: dimensions of
alignment, evaluation of alignment, and methods
of alignment. We call for academia to break down
disciplinary barriers and collaboratively construct
a universal AI ethical framework suitable for big
models, providing insights for future research on
ethical value alignment. We believe that under the
guidance of ethical values, AI can unlock its poten-
tial, bringing broader and more positive impacts to
human society, promoting the progress and devel-
opment of human society and illuminating the path
to the future with the light of technology.
References
Michael Anderson, Susan Leigh Anderson, and Chris
Armen. 2004. Towards machine ethics. In AAAI-
04 workshop on agent organizations: theory and
practice, San Jose, CA.
Geir B Asheim. 2010. Intergenerational equity. Annu.
Rev. Econ., 2(1):197–222.
Isaac Asimov. 1941. Three laws of robotics. Asimov, I.
Runaround, 2.
Amanda Askell, Yuntao Bai, Anna Chen, Dawn Drain,
Deep Ganguli, Tom Henighan, Andy Jones, Nicholas
Joseph, Ben Mann, Nova DasSarma, et al. 2021. A
general language assistant as a laboratory for align-
ment. arXiv preprint arXiv:2112.00861.
Ömer Aydın. 2023. Google bard generated literature
review: Metaverse. Available at SSRN.
Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda
Askell, Anna Chen, Nova DasSarma, Dawn Drain,
Stanislav Fort, Deep Ganguli, Tom Henighan, et al.
2022a. Training a helpful and harmless assistant with
reinforcement learning from human feedback. arXiv
preprint arXiv:2204.05862.
Yuntao Bai,
Saurav Kadavath,
Sandipan Kundu,
Amanda Askell, Jackson Kernion, Andy Jones,
Anna Chen,
Anna Goldie,
Azalia Mirhoseini,
Cameron McKinnon, et al. 2022b. Constitutional
ai: Harmlessness from ai feedback. arXiv preprint
arXiv:2212.08073.
Hagai Bar-El, Hamid Choukri, David Naccache,
Michael Tunstall, and Claire Whelan. 2006. The
sorcerer’s apprentice guide to fault attacks. Proceed-
ings of the IEEE, 94(2):370–382.
Hugo Berg, Siobhan Hall, Yash Bhalgat, Hannah Kirk,
Aleksandar Shtedritski, and Max Bain. 2022.
A
prompt array keeps the bias away: Debiasing vision-
language models with adversarial learning. In Pro-
ceedings of the 2nd Conference of the Asia-Pacific
Chapter of the Association for Computational Lin-
guistics and the 12th International Joint Conference
on Natural Language Processing, pages 806–822.
Rishi Bommasani, Drew A Hudson, Ehsan Adeli,
Russ Altman, Simran Arora, Sydney von Arx,
Michael S Bernstein, Jeannette Bohg, Antoine Bosse-
lut, Emma Brunskill, et al. 2021. On the opportuni-
ties and risks of foundation models. arXiv preprint
arXiv:2108.07258.
Samuel R Bowman, Jeeyoon Hyun, Ethan Perez, Edwin
Chen, Craig Pettit, Scott Heiner, Kamile Lukosuite,
Amanda Askell, Andy Jones, Anna Chen, et al. 2022.
Measuring progress on scalable oversight for large
language models. arXiv preprint arXiv:2211.03540.
Daniel S Brown, Jordan Schneider, Anca Dragan, and
Scott Niekum. 2021. Value alignment verification.
In International Conference on Machine Learning,
pages 1105–1115. PMLR.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, et al. 2020. Language models are few-shot
learners. Advances in neural information processing
systems, 33:1877–1901.
20

--- Page 21 ---

Bartosz Bro˙zek and Bartosz Janik. 2019. Can artifi-
cial intelligences be moral agents?
New ideas in
psychology, 54:101–106.
Sébastien Bubeck, Varun Chandrasekaran, Ronen El-
dan, Johannes Gehrke, Eric Horvitz, Ece Kamar,
Peter Lee, Yin Tat Lee, Yuanzhi Li, Scott Lund-
berg, et al. 2023. Sparks of artificial general intelli-
gence: Early experiments with gpt-4. arXiv preprint
arXiv:2303.12712.
Nicholas Carlini,
Florian Tramer,
Eric Wallace,
Matthew Jagielski, Ariel Herbert-Voss, Katherine
Lee, Adam Roberts, Tom Brown, Dawn Song, Ulfar
Erlingsson, et al. 2021. Extracting training data from
large language models. In 30th USENIX Security
Symposium (USENIX Security 21), pages 2633–2650.
David Carr and Jan Steutel. 2005. Virtue ethics and
moral education. Routledge.
José-Antonio Cervantes, Sonia López, Luis-Felipe Ro-
dríguez, Salvador Cervantes, Francisco Cervantes,
and Félix Ramos. 2020. Artificial moral agents: A
survey of the current status. Science and engineering
ethics, 26:501–532.
Feiyang Chen and Zi-Yi Dou. Measuring and mitigating
bias in vision-and-language models.
Pengyu Cheng, Weituo Hao, Siyang Yuan, Shijing Si,
and Lawrence Carin. 2020. Fairfil: Contrastive neu-
ral debiasing method for pretrained text encoders. In
International Conference on Learning Representa-
tions.
Wei-Lin Chiang, Zhuohan Li, Zi Lin, Ying Sheng,
Zhanghao Wu, Hao Zhang, Lianmin Zheng, Siyuan
Zhuang, Yonghao Zhuang, Joseph E Gonzalez, et al.
2023. Vicuna: An open-source chatbot impressing
gpt-4 with 90%* chatgpt quality. See https://vicuna.
lmsys. org (accessed 14 April 2023).
Kyunghyun Cho, Bart van Merriënboer, Caglar Gul-
cehre, Dzmitry Bahdanau, Fethi Bougares, Holger
Schwenk, and Yoshua Bengio. 2014.
Learning
phrase representations using RNN encoder–decoder
for statistical machine translation. In Proceedings
of the 2014 Conference on Empirical Methods in
Natural Language Processing (EMNLP), pages 1724–
1734, Doha, Qatar. Association for Computational
Linguistics.
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin,
Maarten Bosma, Gaurav Mishra, Adam Roberts,
Paul Barham, Hyung Won Chung, Charles Sutton,
Sebastian Gehrmann, et al. 2022. Palm: Scaling
language modeling with pathways. arXiv preprint
arXiv:2204.02311.
Hyung Won Chung, Le Hou, Shayne Longpre, Bar-
ret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi
Wang, Mostafa Dehghani, Siddhartha Brahma, et al.
2022. Scaling instruction-finetuned language models.
arXiv preprint arXiv:2210.11416.
National New Generation Artificial Intelligence Gov-
ernance Specialist Committee et al. 2021. Ethical
norms for new generation artificial intelligence re-
leased. Center for Security and Emerging Technol-
ogy.
Sumanth Dathathri, Andrea Madotto, Janice Lan, Jane
Hung, Eric Frank, Piero Molino, Jason Yosinski, and
Rosanne Liu. 2019. Plug and play language models:
A simple approach to controlled text generation. In
International Conference on Learning Representa-
tions.
Ismail Dergaa, Karim Chamari, Piotr Zmijewski, and
Helmi Ben Saad. 2023. From human writing to ar-
tificial intelligence generated text: examining the
prospects and potential threats of chatgpt in academic
writing. Biology of Sport, 40(2):615–622.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. Bert: Pre-training of deep
bidirectional transformers for language understand-
ing. In Proceedings of the 2019 Conference of the
North American Chapter of the Association for Com-
putational Linguistics: Human Language Technolo-
gies, Volume 1 (Long and Short Papers), pages 4171–
4186.
Danny Driess, Fei Xia, Mehdi SM Sajjadi, Corey Lynch,
Aakanksha Chowdhery, Brian Ichter, Ayzaan Wahid,
Jonathan Tompson, Quan Vuong, Tianhe Yu, et al.
2023. Palm-e: An embodied multimodal language
model. arXiv preprint arXiv:2303.03378.
Zhengxiao Du, Yujie Qian, Xiao Liu, Ming Ding,
Jiezhong Qiu, Zhilin Yang, and Jie Tang. 2022. Glm:
General language model pretraining with autoregres-
sive blank infilling. In Proceedings of the 60th An-
nual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 320–335.
Tyna Eloundou, Sam Manning, Pamela Mishkin, and
Daniel Rock. 2023. Gpts are gpts: An early look at
the labor market impact potential of large language
models. arXiv preprint arXiv:2303.10130.
Emilio Ferrara. 2023. Should chatgpt be biased? chal-
lenges and risks of bias in large language models.
arXiv preprint arXiv:2304.03738.
Jessica Fjeld, Nele Achten, Hannah Hilligoss, Adam
Nagy, and Madhulika Srikumar. 2020. Principled
artificial intelligence: Mapping consensus in ethi-
cal and rights-based approaches to principles for ai.
Berkman Klein Center Research Publication, (2020-
1).
Luciano Floridi and Josh Cowls. 2022. A unified frame-
work of five principles for ai in society. Machine
learning and the city: Applications in architecture
and urban design, pages 535–545.
Alex Foote, Neel Nanda, Esben Kran, Ioannis Konstas,
Shay Cohen, and Fazl Barez. 2023. Neuron to graph:
Interpreting language model neurons at scale. arXiv
preprint arXiv:2305.19911.
21

--- Page 22 ---

World Economic Forum. 2018. How to prevent dis-
criminatory outcomes in machine learning. In World
Economic Forum Global Future Council on Human
Rights 2016-18, REF, pages 120318–case.
Iason Gabriel. 2020. Artificial intelligence, values, and
alignment. Minds and machines, 30(3):411–437.
Deep Ganguli, Amanda Askell, Nicholas Schiefer,
Thomas Liao, Kamil˙e Lukoši¯ut˙e, Anna Chen, Anna
Goldie, Azalia Mirhoseini, Catherine Olsson, Danny
Hernandez, et al. 2023. The capacity for moral self-
correction in large language models. arXiv preprint
arXiv:2302.07459.
Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda
Askell, Yuntao Bai, Saurav Kadavath, Ben Mann,
Ethan Perez, Nicholas Schiefer, Kamal Ndousse,
et al. 2022. Red teaming language models to re-
duce harms: Methods, scaling behaviors, and lessons
learned. arXiv preprint arXiv:2209.07858.
Chen Gao, Xiaochong Lan, Zhihong Lu, Jinzhu Mao,
Jinghua Piao, Huandong Wang, Depeng Jin, and
Yong Li. 2023. S3: Social-network simulation sys-
tem with large language model-empowered agents.
arXiv preprint arXiv:2307.14984.
Marcin Garbowski. 2018. A critical analysis of the
asilomar ai principles. Scientific Papers of Silesian
University of Technology. Organization & Manage-
ment/Zeszyty Naukowe Politechniki Slaskiej. Seria
Organizacji i Zarzadzanie, (115).
Samuel Gehman, Suchin Gururangan, Maarten Sap,
Yejin Choi, and Noah A Smith. 2020. Realtoxici-
typrompts: Evaluating neural toxic degeneration in
language models. In Findings of the Association
for Computational Linguistics: EMNLP 2020, pages
3356–3369.
Dongyoung Go, Tomasz Korbak, Germán Kruszewski,
Jos Rozen, Nahyeon Ryu, and Marc Dymetman.
2023. Aligning language models with preferences
through f-divergence minimization. arXiv preprint
arXiv:2302.08215.
Jesse Graham, Jonathan Haidt, Sena Koleva, Matt
Motyl, Ravi Iyer, Sean P Wojcik, and Peter H Ditto.
2013. Moral foundations theory: The pragmatic va-
lidity of moral pluralism. In Advances in experi-
mental social psychology, volume 47, pages 55–130.
Elsevier.
Jesse Graham, Peter Meindl, Erica Beall, Kate M John-
son, and Li Zhang. 2016. Cultural differences in
moral judgment and behavior, across and within soci-
eties. Current Opinion in Psychology, 8:125–130.
Jesse Graham, Brian A Nosek, Jonathan Haidt, Ravi
Iyer, Spassena Koleva, and Peter H Ditto. 2011. Map-
ping the moral domain. Journal of personality and
social psychology, 101(2):366.
Jordan Hoffmann, Sebastian Borgeaud, Arthur Men-
sch, Elena Buchatskaya, Trevor Cai, Eliza Ruther-
ford, Diego de Las Casas, Lisa Anne Hendricks,
Johannes Welbl, Aidan Clark, et al. 2022. Train-
ing compute-optimal large language models. arXiv
preprint arXiv:2203.15556.
Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, and
Yejin Choi. 2019. The curious case of neural text de-
generation. In International Conference on Learning
Representations.
Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu, Dan
Su, Yan Xu, Etsuko Ishii, Ye Jin Bang, Andrea
Madotto, and Pascale Fung. 2023. Survey of halluci-
nation in natural language generation. ACM Comput-
ing Surveys, 55(12):1–38.
Liwei Jiang, Jena D Hwang, Chandra Bhagavatula, Ro-
nan Le Bras, Jenny Liang, Jesse Dodge, Keisuke
Sakaguchi, Maxwell Forbes, Jon Borchardt, Saa-
dia Gabriel, et al. 2021.
Can machines learn
morality? the delphi experiment. arXiv preprint
arXiv:2110.07574.
Anna Jobin, Marcello Ienca, and Effy Vayena. 2019.
The global landscape of ai ethics guidelines. Nature
machine intelligence, 1(9):389–399.
Shelly Kagan. 2018. Normative ethics. Routledge.
Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B
Brown, Benjamin Chess, Rewon Child, Scott Gray,
Alec Radford, Jeffrey Wu, and Dario Amodei. 2020.
Scaling laws for neural language models.
arXiv
preprint arXiv:2001.08361.
Sandeep Kaur. 2015. Moral values in education. IOSR
Journal of Humanities and Social Science, 20(3):21–
26.
Zachary Kenton, Tom Everitt, Laura Weidinger, Ia-
son Gabriel, Vladimir Mikulik, and Geoffrey Irving.
2021. Alignment of language agents. arXiv preprint
arXiv:2103.14659.
Sungdong Kim, Sanghwan Bae, Jamin Shin, Soyoung
Kang, Donghyun Kwak, Kang Min Yoo, and Min-
joon Seo. 2023.
Aligning large language mod-
els through synthetic feedback.
arXiv preprint
arXiv:2305.13735.
Hannah Rose Kirk, Bertie Vidgen, Paul Röttger, and
Scott A Hale. 2023. Personalisation within bounds:
A risk taxonomy and policy framework for the align-
ment of large language models with personalised
feedback. arXiv preprint arXiv:2303.05453.
J Matias Kivikangas, Belén Fernández-Castilla, Simo
Järvelä, Niklas Ravaja, and Jan-Erik Lönnqvist. 2021.
Moral foundations and political orientation: System-
atic review and meta-analysis. Psychological Bul-
letin, 147(1):55.
Dennis Krebs. 2015. The evolution of morality. The
handbook of evolutionary psychology, pages 747–
771.
22

--- Page 23 ---

Paul Pu Liang, Chiyu Wu, Louis-Philippe Morency, and
Ruslan Salakhutdinov. 2021. Towards understand-
ing and mitigating social biases in language models.
In International Conference on Machine Learning,
pages 6565–6576. PMLR.
Yaobo Liang, Chenfei Wu, Ting Song, Wenshan Wu,
Yan Xia, Yu Liu, Yang Ou, Shuai Lu, Lei Ji,
Shaoguang Mao, et al. 2023. Taskmatrix. ai: Com-
pleting tasks by connecting foundation models with
millions of apis. arXiv preprint arXiv:2303.16434.
Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri
Edwards, Bowen Baker, Teddy Lee, Jan Leike,
John Schulman, Ilya Sutskever, and Karl Cobbe.
2023.
Let’s verify step by step.
arXiv preprint
arXiv:2305.20050.
Francisco Liñán and José Fernandez-Serrano. 2014. Na-
tional culture, entrepreneurship and economic devel-
opment: different patterns across the european union.
Small business economics, 42:685–701.
Alisa Liu,
Maarten Sap,
Ximing Lu,
Swabha
Swayamdipta, Chandra Bhagavatula, Noah A Smith,
and Yejin Choi. 2021. Dexperts: Decoding-time con-
trolled text generation with experts and anti-experts.
In Proceedings of the 59th Annual Meeting of the
Association for Computational Linguistics and the
11th International Joint Conference on Natural Lan-
guage Processing (Volume 1: Long Papers), pages
6691–6706.
Hao Liu, Carmelo Sferrazza, and Pieter Abbeel. 2023a.
Chain of hindsight aligns language models with feed-
back. arXiv preprint arXiv:2302.02676, 3.
Ruibo Liu, Ruixin Yang, Chenyan Jia, Ge Zhang, Denny
Zhou, Andrew M Dai, Diyi Yang, and Soroush
Vosoughi. 2023b. Training socially aligned language
models in simulated human society. arXiv preprint
arXiv:2305.16960.
Kaiji Lu, Piotr Mardziel, Fangjing Wu, Preetam Aman-
charla, and Anupam Datta. 2020. Gender bias in
neural natural language processing. Logic, Language,
and Security: Essays Dedicated to Andre Scedrov on
the Occasion of His 65th Birthday, pages 189–202.
Ian R McKenzie, Alexander Lyzhov, Michael Pieler,
Alicia Parrish, Aaron Mueller, Ameya Prabhu, Euan
McLean, Aaron Kirtland, Alexis Ross, Alisa Liu,
et al. 2023. Inverse scaling: When bigger isn’t better.
arXiv preprint arXiv:2306.09479.
Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe,
Mike Lewis, Hannaneh Hajishirzi, and Luke Zettle-
moyer. 2022. Rethinking the role of demonstrations:
What makes in-context learning work? In Proceed-
ings of the 2022 Conference on Empirical Methods in
Natural Language Processing, pages 11048–11064.
Shima Rahimi Moghaddam and Christopher J Honey.
2023. Boosting theory-of-mind performance in large
language models via prompting.
arXiv preprint
arXiv:2304.11490.
James Moor et al. 2009. Four kinds of ethical robots.
Philosophy Now, 72:12–14.
Sharan Narang and Aakanksha Chowdhery. 2022. Path-
ways language model (palm): Scaling to 540 billion
parameters for breakthrough performance. Google
AI Blog.
Richard Ngo. 2022.
The alignment problem from
a deep learning perspective.
arXiv preprint
arXiv:2209.00626.
OpenAI. 2023.
GPT-4 technical report.
CoRR,
abs/2303.08774.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida,
Carroll Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, et al.
2022. Training language models to follow instruc-
tions with human feedback.
Advances in Neural
Information Processing Systems, 35:27730–27744.
Joel Parthemore and Blay Whitby. 2013. What makes
any agent a moral agent? reflections on machine con-
sciousness and moral agency. International Journal
of Machine Consciousness, 5(02):105–129.
Herbert James Paton. 1971. The categorical imperative:
A study in Kant’s moral philosophy, volume 1023.
University of Pennsylvania Press.
Adam Pauls and Dan Klein. 2011. Faster and smaller
n-gram language models. In Proceedings of the 49th
annual meeting of the Association for Computational
Linguistics: Human Language Technologies, pages
258–267.
Ethan Perez, Sam Ringer, Kamil˙e Lukoši¯ut˙e, Karina
Nguyen, Edwin Chen, Scott Heiner, Craig Pettit,
Catherine Olsson, Sandipan Kundu, Saurav Kada-
vath, et al. 2022. Discovering language model behav-
iors with model-written evaluations. arXiv preprint
arXiv:2212.09251.
Thomas Pogge. 2007. John Rawls: His life and theory
of justice. Oxford University Press, USA.
Jing Qian, Li Dong, Yelong Shen, Furu Wei, and Weizhu
Chen. 2022. Controllable natural language genera-
tion with contrastive prefixes. In Findings of the As-
sociation for Computational Linguistics: ACL 2022,
pages 2912–2924.
Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya
Sutskever, et al. 2018. Improving language under-
standing by generative pre-training.
Aditya Ramesh, Prafulla Dhariwal, Alex Nichol, Casey
Chu, and Mark Chen. 2022.
Hierarchical text-
conditional image generation with clip latents. arXiv
preprint arXiv:2204.06125.
John Rawls. 1951. Outline of a decision procedure for
ethics. The philosophical review, 60(2):177–197.
John Rawls. 2017. A theory of justice. In Applied
Ethics, pages 21–29. Routledge.
23

--- Page 24 ---

David Rozado. 2023. The political biases of chatgpt.
Social Sciences, 12(3):148.
Stuart J Russell. 2010. Artificial intelligence a modern
approach. Pearson Education, Inc.
William Saunders, Catherine Yeh, Jeff Wu, Steven Bills,
Long Ouyang, Jonathan Ward, and Jan Leike. 2022.
Self-critiquing models for assisting human evaluators.
arXiv preprint arXiv:2206.05802.
Timo Schick, Sahana Udupa, and Hinrich Schütze. 2021.
Self-diagnosis and self-debiasing: A proposal for re-
ducing corpus-based bias in nlp. Transactions of the
Association for Computational Linguistics, 9:1408–
1424.
Patrick Schramowski, Cigdem Turan, Nico Andersen,
Constantin A Rothkopf, and Kristian Kersting. 2022.
Large pre-trained language models contain human-
like biases of what is right and wrong to do. Nature
Machine Intelligence, 4(3):258–268.
Shalom H Schwartz. 2007. Basic human values: Theory,
measurement, and applications. Revue française de
sociologie, 47(4):929.
Emily Sheng, Kai-Wei Chang, Prem Natarajan, and
Nanyun Peng. 2020. Towards controllable biases in
language generation. In Findings of the Association
for Computational Linguistics: EMNLP 2020, pages
3239–3254.
Emily Sheng, Kai-Wei Chang, Prem Natarajan, and
Nanyun Peng. 2021. Societal biases in language
generation: Progress and challenges. In Proceedings
of the 59th Annual Meeting of the Association for
Computational Linguistics and the 11th International
Joint Conference on Natural Language Processing
(Volume 1: Long Papers), pages 4275–4293.
Gabriel Simmons. 2022.
Moral mimicry:
Large
language models produce moral rationalizations
tailored to political identity.
arXiv preprint
arXiv:2209.12106.
Chandan Singh, Aliyah R Hsu, Richard Antonello,
Shailee Jain, Alexander G Huth, Bin Yu, and Jian-
feng Gao. 2023. Explaining black box text modules
in natural language with language models. arXiv
preprint arXiv:2305.09863.
Michael Slote. 2007. The ethics of care and empathy.
Routledge.
Nathalie A Smuha. 2019. The eu approach to ethics
guidelines for trustworthy artificial intelligence.
Computer Law Review International, 20(4):97–106.
Sharon Street. 2012. Coming to terms with contingency:
Humean constructivism about practical reason. Con-
structivism in practical philosophy, pages 40–59.
John P Sullins. 2011. When is a robot a moral agent.
Machine ethics, 6(2001):151–161.
Hao Sun, Zhexin Zhang, Jiawen Deng, Jiale Cheng,
and Minlie Huang. 2023a.
Safety assessment of
chinese large language models.
arXiv preprint
arXiv:2304.10436.
Zhiqing Sun, Yikang Shen, Qinhong Zhou, Hongxin
Zhang, Zhenfang Chen, David Cox, Yiming Yang,
and Chuang Gan. 2023b.
Principle-driven self-
alignment of language models from scratch with
minimal human supervision.
arXiv preprint
arXiv:2305.03047.
Angus Taylor. 2009. Animals and ethics. Broadview
press.
Yan TENG, Guoyu WANG, and Yingchun WANG.
2022.
Ethics and governance of general models:
Challenges and countermeasures. Bulletin of Chinese
Academy of Sciences (Chinese Version), 37(9):1290–
1299.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timothée Lacroix,
Baptiste Rozière, Naman Goyal, Eric Hambro,
Faisal Azhar, et al. 2023. Llama: Open and effi-
cient foundation language models. arXiv preprint
arXiv:2302.13971.
C UNESCO. 2021. Recommendation on the ethics of
artificial intelligence.
Nikhil Vyas, Sham Kakade, and Boaz Barak. 2023.
Provable copyright protection for generative models.
arXiv preprint arXiv:2302.10870.
M Mitchell Waldrop. 1987. A question of responsibility.
AI Magazine, 8(1):28–28.
Boxin Wang, Wei Ping, Chaowei Xiao, Peng Xu,
Mostofa Patwary, Mohammad Shoeybi, Bo Li, An-
ima Anandkumar, and Bryan Catanzaro. 2022a. Ex-
ploring the limits of domain-adaptive training for
detoxifying large-scale language models. Advances
in Neural Information Processing Systems, 35:35811–
35824.
Hongyu Wang, Shuming Ma, Li Dong, Shaohan Huang,
Dongdong Zhang, and Furu Wei. 2022b. Deepnet:
Scaling transformers to 1,000 layers. arXiv preprint
arXiv:2203.00555.
Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Al-
isa Liu, Noah A Smith, Daniel Khashabi, and Han-
naneh Hajishirzi. 2022c. Self-instruct: Aligning lan-
guage model with self generated instructions. arXiv
preprint arXiv:2212.10560.
Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel,
Barret Zoph, Sebastian Borgeaud, Dani Yogatama,
Maarten Bosma, Denny Zhou, Donald Metzler, et al.
2022a. Emergent abilities of large language models.
arXiv preprint arXiv:2206.07682.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou,
24

--- Page 25 ---

et al. 2022b. Chain-of-thought prompting elicits rea-
soning in large language models. Advances in Neural
Information Processing Systems, 35:24824–24837.
Laura Weidinger, John Mellor, Maribeth Rauh, Conor
Griffin, Jonathan Uesato, Po-Sen Huang, Myra
Cheng, Mia Glaese, Borja Balle, Atoosa Kasirzadeh,
et al. 2021. Ethical and social risks of harm from
language models. arXiv preprint arXiv:2112.04359.
Johannes Welbl, Amelia Glaese, Jonathan Uesato,
Sumanth Dathathri, John Mellor, Lisa Anne Hen-
dricks, Kirsty Anderson, Pushmeet Kohli, Ben Cop-
pin, and Po-Sen Huang. 2021. Challenges in detox-
ifying language models. In Findings of the Associ-
ation for Computational Linguistics: EMNLP 2021,
pages 2447–2469.
Norbert Wiener. 1960. Some moral and technical conse-
quences of automation: As machines learn they may
develop unforeseen strategies at rates that baffle their
programmers. Science, 131(3410):1355–1358.
Yotam Wolf, Noam Wies, Yoav Levine, and Amnon
Shashua. 2023. Fundamental limitations of align-
ment in large language models.
arXiv preprint
arXiv:2304.11082.
Sang Michael Xie, Aditi Raghunathan, Percy Liang,
and Tengyu Ma. 2021. An explanation of in-context
learning as implicit bayesian inference. In Interna-
tional Conference on Learning Representations.
Kevin Yang and Dan Klein. 2021. Fudge: Controlled
text generation with future discriminators. In Pro-
ceedings of the 2021 Conference of the North Amer-
ican Chapter of the Association for Computational
Linguistics: Human Language Technologies, pages
3511–3535.
Zonghan Yang, Xiaoyuan Yi, Peng Li, Yang Liu, and
Xing Xie. 2023. Unified detoxifying and debiasing in
language generation via inference-time adaptive opti-
mization. In The Eleventh International Conference
on Learning Representations.
Jing Yao, Xiaoyuan Yi, Xiting Wang, Jindong Wang,
and Xing Xie. 2023. From instructions to intrinsic
human values–a survey of alignment goals for big
models. arXiv preprint arXiv:2308.12014.
Zheng Yuan, Hongyi Yuan, Chuanqi Tan, Wei Wang,
Songfang Huang, and Fei Huang. 2023.
Rrhf:
Rank responses to align language models with
human feedback without tears.
arXiv preprint
arXiv:2304.05302.
Alexandra Zapko-Willmes, Shalom H Schwartz, Julia
Richter, and Christian Kandler. 2021. Basic value
orientations and moral foundations: Convergent or
discriminant constructs?
Journal of Research in
Personality, 92:104099.
Ali Zarifhonarvar. 2023. Economics of chatgpt: A labor
market view on the occupational impact of artificial
intelligence. Available at SSRN 4350925.
Aohan Zeng, Xiao Liu, Zhengxiao Du, Zihan Wang,
Hanyu Lai, Ming Ding, Zhuoyi Yang, Yifan Xu,
Wendi Zheng, Xiao Xia, et al. 2022. Glm-130b: An
open bilingual pre-trained model. In The Eleventh In-
ternational Conference on Learning Representations.
Weixiang Zhao, Yanyan Zhao, Xin Lu, Shilong Wang,
Yanpeng Tong, and Bing Qin. 2023.
Is chat-
gpt equipped with emotional dialogue capabilities?
arXiv preprint arXiv:2304.09582.
Caleb Ziems, William Held, Omar Shaikh, Jiaao Chen,
Zhehao Zhang, and Diyi Yang. 2023. Can large lan-
guage models transform computational social sci-
ence? arXiv preprint arXiv:2305.03514.
25
```
