---
title: "The Chai Platform's AI Safety Framework - PDF Extract"
source_pdf: "2023-Lu-The Chai Platform's AI Safety Framework.pdf"
pages: 6
extracted_at: "2026-01-24T17:05:16.461363"
---

# PDF Extract: The Chai Platform's AI Safety Framework

**Source PDF:** 2023-Lu-The Chai Platform's AI Safety Framework.pdf
**Total Pages:** 6

---

## Content

```
--- Page 1 ---

The Chai Platform’s AI Safety Framework
Xiaoding Lu
Aleksey Korshuk
Zongyi Liu
William Beauchamp
Chai Research
Abstract
Chai empowers users to create and interact
with customized chatbots, offering unique and
engaging experiences.
Despite the exciting
prospects, the work recognizes the inherent
challenges of a commitment to modern safety
standards. Therefore, this paper presents the
integrated AI safety principles into Chai to pri-
oritize user safety, data protection, and ethical
technology use. The paper specifically explores
the multidimensional domain of AI safety re-
search, demonstrating its application in Chai’s
conversational chatbot platform. It presents
Chai’s AI safety principles, informed by well-
established AI research centres and adapted
for chat AI. This work proposes the following
safety framework: Content Safeguarding; Sta-
bility and Robustness; and Operational Trans-
parency and Traceability. The subsequent im-
plementation of these principles is outlined, fol-
lowed by an experimental analysis of Chai’s AI
safety framework’s real-world impact. We em-
phasise the significance of conscientious appli-
cation of AI safety principles and robust safety
measures. The successful implementation of
the safe AI framework in Chai indicates the
practicality of mitigating potential risks for re-
sponsible and ethical use of AI technologies.
The ultimate vision is a transformative AI tool
fostering progress and innovation while priori-
tizing user safety and ethical standards.
1
Introduction
With the rapid improvement in the quality and flu-
ency of virtual conversational AI agents, there has
been growing integration of chat-based based AI
systems (Chat AIs) into a range of real-world ap-
plications (Caldarini et al., 2022; Almansor and
Hussain, 2020). This has led to the development of
new technologies and opportunities, as seen in plat-
forms such as the Chai research platform. The Chai
research platform is an innovative online platform
that empowers users to design and interact with
chatbots that emulate friends, mentors, or fictional
characters (Irvine et al., 2023).
However, with this flexibility comes potential
challenges. If unregulated, there’s a risk that users,
intentionally or unintentionally, might design chat-
bots that do not align to desired ethical and safe AI
standards. This potential issue highlights the impor-
tance of robust safety measures to prevent harmful
outcomes, such as promoting inappropriate content
or negatively impacting user well-being (Lu et al.,
2023). This paper addresses safety considerations
for Chat AI and introduces the AI safety princi-
ples integrated into the Chai platform to ensure that
deployed chat ai technologies best align with mod-
ern safe AI practices (Schuett et al., 2023). Safe
AI is about developing and managing AI systems
that work in a manner that is beneficial to human-
ity and encourages generation of safe content. It
involves prioritising user safety, protecting data,
and ensuring that the technology behaves ethically
and responsibly (Mohseni et al., 2022). In this pa-
per, we detail our three main chat ai safety pillars;
content safeguarding (Awad et al., 2018), system
stability and robustness (Drenkow et al., 2021), and
operational transparency and traceability (Wanner
et al., 2022). The second part of this paper then
discusses how these considerations are practically
integrated into chat ai platforms, where we detail
the strategies taken that reinforces Chai’s commit-
ment to creating a safe AI conversational platform.
2
Background
AI safety, as a field of study, is dedicated to un-
derstanding and mitigating the potential risks as-
sociated with the development and deployment of
artificial intelligence technologies (Bostrom, 2014;
Schuett et al., 2023).
The primary concern re-
volves around ensuring alignment (Christian, 2020;
Gabriel and Ghazavi, 2021) of these technologies
with human values, ethics, and societal norms (Yud-
kowsky, 2011). This involves designing AI systems
arXiv:2306.02979v1  [cs.AI]  5 Jun 2023

--- Page 2 ---

that can understand, learn from, and act in accor-
dance with the principles, values, and goals that
humans hold (Gabriel, 2020; Sotala and Yampol-
skiy, 2014). The objective is to create artificial
intelligence that not only improves efficiency and
productivity but also respects human autonomy,
privacy, and other core ethical principles (Dignum,
2019).
In
order
to
achieve
this,
AI
safety
re-
search (Mohseni et al., 2022) is multidimensional,
involving elements of computer science, cognitive
science, ethics, and social science (Fishbein and
Ajzen, 2005; Sarma and Hay, 2017). Researchers
investigate technical aspects like robustness, inter-
pretability, and transparency of AI systems, while
also exploring philosophical questions about moral
and ethical considerations regarding how we define
human values (Turchin, manuscript; Muehlhauser
and Helm, 2012; Friedman and Hendry, 2019). A
range of approaches explore how to effectively in-
corporate defined human values within reward func-
tions used to train AI systems (Hendrycks et al.,
2020; Soares et al., 2015; Ng and Russell, 2000;
Riedl and Harrison, 2016; Armstrong; Etzioni and
Etzioni, 2016). The ultimate aim is to ensure that
the vast transformative power of AI is harnessed in
a manner that is safe, responsible, and beneficial
for all of humanity (Taylor et al., 2020).
In this work, we outline the approach used to
incoporate modern AI safety standards within gen-
erative AI technology for Chai’s conversational
chatbot platform (Irvine et al., 2023).
3
AI Safety Principles
In this section we analyse the different important
considerations that various well-established AI re-
search centres have proposed, and then use this to
propose three main pillars that define Chai’s AI
safety principles for a conversational chatbot plat-
form.
Deepmind outline three core AI safety principles
(Leike et al., 2017); specification, robustness and
assurance. Meta’s pillars of responsible AI (Pesenti,
2021) are privacy, security, fairness, transparency
and accountability. While OpenAI’s tenants (Will-
ner) include the reduction of harm, fostering trust,
and continuous improvement. We analyse the dif-
ferent proposed pillars and aggregate them into the
following main categories, with a consideration of
how to align these definitions best for chat AI:
1. Content Safeguarding Content safeguarding
aims to encourage chat AI systems to gener-
ate responses (content) that are aligned with
human values such that they do not cause any
risk to users. This includes ensuring that the
system generates any appropriate, ethical con-
tent and that the system remains respectful to
users, as well as adhering to modern standards
of morality and ethics (Awad et al., 2018).
2. Stability and Robustness Stable and Ro-
bust systems can handle diverse situations
without failing- whether that be possible do-
main/distributional shifts (Liusie et al., 2022;
Malinin et al., 2021; Liang et al., 2023) or
user perturbations, such as adversarial attacks
(Raina and Gales, 2023; Chakraborty et al.,
2018), that it might encounter when deployed.
Robust systems act in a predictable manner
and do not exhibit any unexpected behaviour,
even in environments that are different from
the standard training domain (Shafique et al.,
2021).
3. Operational Transparency and Traceabil-
ity This refers to creators having the ability to
interpret, observe, audit and track all system
activity (Mora-Cantallops et al., 2021; Räuker
et al., 2023; Wanner et al., 2022). For exam-
ple, this can be achieved by having logs of
all past system activity which can be analysed
for quality control, allowing developers to de-
termine the cause of any possible undesirable
behaviour at an early stage. Early detection of
unsafe AI behaviour allows for intervention,
e.g. via human action or activation/tripping
of safety mechanisms before the undesired AI
behaviour progresses further (Schwalbe and
Schels, 2020).
4
Chai Safety Framework
In this section, we outline the methods used to
achieve the three safety pillars presented for Chai’s
AI platform in the previous section.
4.1
The Chai platform
The Chai platform is an online framework where
thousands of chat AIs with distinct personas are
hosted, which other users can freely interact with.
The lifecycle begins with users having the ability to
create new chat ai personas by selecting keywords
that describe the characteristics of a particular chat
ai. Keywords such as bubbly or intelligent are then

--- Page 3 ---

Figure 1: AI Safety System Content Safeguarding Pipeline.
used to condition the responses of a particular chat
AI persona. Users can then upload an image that
represents the chat AI, which for example can be
the cover picture of a fictional character that the
keywords attempt to describe, and select a name
that describes the persona. The chat persona is then
uploaded to the platform, where other users are
able to explore all existing chat AIs and converse
with any selected persona.
4.1.1
Content Safeguarding
To ensure that the content generated by any chat
AI aligns with human values while performing the
task, we apply multiple stages of safety alignment
to all created chat AI personas as well as uploaded
images.
One concern is that a particular set of selected
keywords may lead to personas that could display
antisocial behaviour. We therefore develop a mod-
eration system that is applied to all chatbots before
deployment, where the moderation system filters
out any chatbots that may exhibit negative prop-
erties. This is achieved by running thousands of
logged conversational histories into each new per-
sona, and then sampling the responses of chat AI
personas under the different conversational histo-
ries. We then apply an automatic safety classifier
to all outputs of the chat persona, and if the anal-
ysis flags that the chat AI may not be sufficiently
safe, then the persona is discarded and not included
within the set of accessible personas on the chai AI
platform. Further beyond moderation of deployed
personas, our base model is trained to generate safe
responses, as detailed in Lu et al. (2023).
Similarly, users may upload images that do not
adhere to safety standards. We therefore use an
image moderation classification system to block
any images which are not deemed safe. Our en-
tire Content Safeguarding pipeline is presented in
Figure 1.
4.1.2
Stability and Robustness
To ensure that the deployed Chai system is robust
and can handle diverse outputs, the base chat AI
language model is frequently retrained with recent
user conversations from diverse geographical lo-
cations. Continuously retraining our system on
current user conversations ensures that the model
can rapidly adapt to any implicit distributional shift
of user queries. Additionally, the platform provides
users with the opportunity to rate the chatbot’s re-
sponses or provide suggestions on possible better
responses. This information can then be frequently
used to update our reward function (Irvine et al.,
2023), to better align our systems with users’ prefer-
ences and be better equipped for any new emerging
domain that the system may encounter.
4.1.3
Operational Transparency and
Traceability
The Chai Platform logs all user conversational ex-
changes which we store in a private and secure
server. If users flag any responses from particu-
lar personas, we have the full trace of exchanges
with the persona which can be used to analyse the
system. Further, by periodically reviewing the ex-
changes for quality and safety, we can better un-
derstand how the AI chatbot interacts with users,
identify potential risks, and monitor the chat AI’s
compliance with our content guidelines and poli-
cies. This helps enable early detection of any un-
safe practices which can be remedied.

--- Page 4 ---

5
Experiments
The aim of this experimental section is to deter-
mine the impact of Chai’s AI safety framework on
the real-world safety attributes of deployed AI chat-
bots on the Chai platform. As detailed in Lu et al.
(2023), the base large language model used in all
deployed chatbots is a GPT-J 6B (Wang and Ko-
matsuzaki, 2021) model fine-tuned on novels and
literature 1. Since the inception of the deployed
platform on 5th May 2022, the base model has un-
dergone various iterations of development to align
with the AI safety framework, under the categories
of content safeguarding, stability & robustness and
Operational Transparency & Traceability. Section
4 indicates the specific details of the approaches
used to achieve these desired AI safety goals.
Although qualitative analysis of randomly sam-
pled user conversations has revealed that the latest
iterations of the deployed chat AIs adhere well to
modern safety standards, as desired, it is critical
to measure this progress quantiatively. However,
it can be challenging to define a single metric to
measure the safety of a chatbot model. Inspired by
OpenAI’s moderation tool 2, in this work, we de-
fine a single-value safety score, ¯s to act as a proxy
measure for platform safety. Specifically we re-
port the Note Safe for Work (NSFW) words ratio
by day, which gives the fraction of all words, w
appearing in real user conversations (totaling N
words) 3, classed as NSFW in a single day for de-
ployed models. We define a dictionary, V, for all
the NSFW words in the English language, aligning
to OpenAI’s moderation categories: hate speech,
self-harm, sexual content and violence.
¯s = 1
N
N
X
n
1(wn ∈V)
(1)
With this definition of model safety we observe
how new iterations of the chat AIs impact the frac-
tion of NSFW words. Figure 2 demonstrates that
key major updates in the base models and plat-
form safety design in June 2022, October 2022
and March 2023 result in significant improvements
in model safety as per our proxy metric. This en-
courages us to believe that with an active effort to
align the Chai research platform with our proposed
1https://huggingface.co/hakurei/lit-6B
2https://platform.openai.com/docs/guides/
moderation
3There are typically 2 million user-chatbot conversations
per day with an average length of 500 words in a conversation.
AI safety principles, we are able to have signifi-
cant measurable and quantifiable improvements in
model safety. This leads us to the understanding
that our model is safe to be deployed in real-world
settings.
Figure 2: AI Safety Progression
6
Conclusions
In conclusion, the emergence and rapid evolution
of conversational AI platforms like Chai heralds an
exciting era of personalized and democratized AI
interactions. However, this powerful tool also ne-
cessitates careful stewardship to ensure that its use
aligns with ethical standards and does not inadver-
tently lead to harmful consequences. As this paper
outlines, through the conscientious application of
AI safety principles and robust safety measures,
platforms like Chai can provide not just power-
ful and unique AI interactions, but also a safe and
nurturing environment for users to explore the land-
scape of conversational AI.
With a multifaceted approach that includes
safety-oriented training, rigorous moderation, and
consistent audits within Chai’s AI safety fram-
work (content safeguarding, stability & robustness
and operational transparency & traceability), we
demonstrate that the implementation of AI safety
is both an attainable and practical endeavor. This
study highlights the successful application of the
safe AI framework, indicating how potential risks
can be mitigated to ensure the responsible and eth-
ical use of AI technologies. It is clear that, when
approached with due diligence and responsibil-
ity, AI can be a transformative tool that fosters
progress and innovation, while always prioritizing
user safety and ethical standards.

--- Page 5 ---

References
Ebtesam Almansor and Farookh Hussain. 2020. Survey
on Intelligent Chatbots: State-of-the-Art and Future
Research Directions, pages 534–543.
Stuart Armstrong. Research agenda v0.9: Synthesising
a human’s preferences into a utility function.
Edmond Awad, Sohan Dsouza, Richard Kim, Jonathan
Schulz, Joseph Henrich, Azim Shariff, Jean-François
Bonnefon, and Iyad Rahwan. 2018. The moral ma-
chine experiment. Nature, 563(7729):59–64.
Nick Bostrom. 2014. Superintelligence. Dunod.
Guendalina Caldarini, Sardar F. Jaf, and Kenneth Mc-
Garry. 2022. A literature survey of recent advances
in chatbots. CoRR, abs/2201.06657.
Anirban Chakraborty, Manaar Alam, Vishal Dey, Anu-
pam Chattopadhyay, and Debdeep Mukhopadhyay.
2018. Adversarial attacks and defences: A survey.
CoRR, abs/1810.00069.
Brian Christian. 2020. The alignment problem: Ma-
chine Learning and human values. Norton &amp;
Company.
Virginia Dignum. 2019.
Ensuring responsible ai in
practice. Responsible Artificial Intelligence, page
93–105.
Nathan Drenkow, Numair Sani, Ilya Shpitser, and
Mathias Unberath. 2021. Robustness in deep learn-
ing for computer vision: Mind the gap?
CoRR,
abs/2112.00639.
Amitai Etzioni and Oren Etzioni. 2016. Designing ai
systems that obey our laws and values. Commun.
ACM, 59(9):29–31.
Martin Fishbein and Icek Ajzen. 2005. Theory-based
behavior change interventions: Comments on hob-
bis and sutton.
Journal of Health Psychology,
10(1):27–31.
Batya Friedman and David G. Hendry. 2019. Value sen-
sitive design: Shaping technology with moral imagi-
nation. MIT Press.
Iason Gabriel. 2020. Artificial intelligence, values and
alignment. CoRR, abs/2001.09768.
Iason Gabriel and Vafa Ghazavi. 2021. The challenge of
value alignment: from fairer algorithms to AI safety.
CoRR, abs/2101.06060.
Dan Hendrycks, Collin Burns, Steven Basart, Andrew
Critch, Jerry Li, Dawn Song, and Jacob Steinhardt.
2020. Aligning AI with shared human values. CoRR,
abs/2008.02275.
Robert Irvine, Douglas Boubert, Vyas Raina, Adian
Liusie, Ziyi Zhu, Vineet Mudupalli, Aliaksei Kor-
shuk, Zongyi Liu, Fritz Cremer, Valentin Assassi,
Christie-Carol Beauchamp, Xiaoding Lu, Thomas
Rialan, and William Beauchamp. 2023. Rewarding
chatbots for real-world engagement with millions of
users.
Jan Leike, Miljan Martic, Victoria Krakovna, Pedro A.
Ortega, Tom Everitt, Andrew Lefrancq, Laurent
Orseau, and Shane Legg. 2017. Ai safety gridworlds.
Jian Liang, Ran He, and Tieniu Tan. 2023. A compre-
hensive survey on test-time adaptation under distri-
bution shifts.
Adian Liusie, Vatsal Raina, Vyas Raina, and Mark
Gales. 2022. Analyzing biases to spurious corre-
lations in text classification tasks. In Proceedings of
the 2nd Conference of the Asia-Pacific Chapter of the
Association for Computational Linguistics and the
12th International Joint Conference on Natural Lan-
guage Processing (Volume 2: Short Papers), pages
78–84, Online only. Association for Computational
Linguistics.
Xiaoding Lu, Aleksey Korshuk, Zongyi Liu, William
Beauchamp, and Chai Research. 2023. Safer conver-
sational ai as a source of user delight.
Andrey Malinin, Neil Band, Alexander Ganshin, Ger-
man Chesnokov, Yarin Gal, Mark J. F. Gales,
Alexey Noskov, Andrey Ploskonosov, Liudmila
Prokhorenkova, Ivan Provilkov, Vatsal Raina, Vyas
Raina, Mariya Shmatova, Panos Tigas, and Boris
Yangel. 2021.
Shifts: A dataset of real distribu-
tional shift across multiple large-scale tasks. CoRR,
abs/2107.07455.
Sina Mohseni, Haotao Wang, Chaowei Xiao, Zhiding
Yu, Zhangyang Wang, and Jay Yadawa. 2022. Tax-
onomy of machine learning safety: A survey and
primer. ACM Comput. Surv., 55(8).
Marçal Mora-Cantallops, Salvador Sánchez-Alonso,
Elena García-Barriocanal, and Miguel-Angel Sicilia.
2021. Traceability for trustworthy ai: A review of
models and tools. Big Data and Cognitive Comput-
ing, 5(2).
Luke Muehlhauser and Louie Helm. 2012. The singu-
larity and machine ethics. The Frontiers Collection,
page 101–126.
Andrew Y. Ng and Stuart J. Russell. 2000. Algorithms
for inverse reinforcement learning. In Proceedings
of the Seventeenth International Conference on Ma-
chine Learning, ICML ’00, page 663–670, San Fran-
cisco, CA, USA. Morgan Kaufmann Publishers Inc.
Jerome Pesenti. 2021. Facebook’s five pillars of re-
sponsible ai, de, jun. 2021. URL https://ai. facebook.
com/blog/facebooks-five-pillars-of-responsible-ai.
Vyas Raina and Mark Gales. 2023. Identifying adver-
sarially attackable and robust samples.
Mark O. Riedl and Brent Harrison. 2016. Using stories
to teach human values to artificial agents. In AAAI
Workshop: AI, Ethics, and Society.

--- Page 6 ---

Tilman Räuker, Anson Ho, Stephen Casper, and Dylan
Hadfield-Menell. 2023. Toward transparent ai: A
survey on interpreting the inner structures of deep
neural networks.
Gopal P. Sarma and Nick J. Hay. 2017. Mammalian
value systems.
Jonas Schuett, Noemi Dreksler, Markus Anderljung,
David McCaffary, Lennart Heim, Emma Bluemke,
and Ben Garfinkel. 2023. Towards best practices
in agi safety and governance: A survey of expert
opinion.
Gesina Schwalbe and Martin Schels. 2020. A survey on
methods for the safety assurance of machine learning
based systems.
Muhammad Shafique, Mahum Naseer, Theocharis
Theocharides, Christos Kyrkou, Onur Mutlu, Lois
Orosa,
and Jungwook Choi. 2021.
Robust
machine learning systems:
Challenges, current
trends, perspectives, and the road ahead.
CoRR,
abs/2101.02559.
Nate Soares, Benja Fallenstein, Stuart Armstrong, and
Eliezer Yudkowsky. 2015. Corrigibility. In Artificial
Intelligence and Ethics, Papers from the 2015 AAAI
Workshop, Austin, Texas, USA, January 25, 2015,
volume WS-15-02 of AAAI Technical Report. AAAI
Press.
Kaj Sotala and Roman V Yampolskiy. 2014. Responses
to catastrophic agi risk: a survey. Physica Scripta,
90(1):018001.
Jessica Taylor, Eliezer Yudkowsky, Patrick LaVictoire,
and Andrew Critch. 2020. Alignment for advanced
machine learning systems. Ethics of Artificial Intelli-
gence, page 342–382.
Alexey Turchin. manuscript. Ai alignment problem:
?human values? don?t actually exist.
Ben Wang and Aran Komatsuzaki. 2021.
GPT-J-
6B: A 6 Billion Parameter Autoregressive Lan-
guage Model. https://github.com/kingoflolz/
mesh-transformer-jax.
Jonas Wanner, Lukas-Valentin Herm, Kai Heinrich,
and Christian Janiesch. 2022. The effect of trans-
parency and trust on intelligent system acceptance:
Evidence from a user-based study. Electronic Mar-
kets, 32(4):2079–2102.
Dave Willner. [link].
Eliezer Yudkowsky. 2011. Complex value systems are
required to realize valuable futures.

```
