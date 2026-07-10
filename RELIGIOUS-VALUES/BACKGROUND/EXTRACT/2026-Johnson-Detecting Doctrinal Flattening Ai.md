---
title: "Detecting Doctrinal Flattening Ai - PDF Extract"
source_pdf: "2026-Johnson-Detecting Doctrinal Flattening Ai.pdf"
pages: 11
extracted_at: "2026-04-03T11:05:46.977311"
---

# PDF Extract: Detecting Doctrinal Flattening Ai

**Source PDF:** 2026-Johnson-Detecting Doctrinal Flattening Ai.pdf
**Total Pages:** 11

---

## Content

--- Page 1 ---

RESEARCH
AI and Ethics           (2026) 6:178 
https://doi.org/10.1007/s43681-026-01051-0
Christianity has always wrestled with the spiritual con­
sequences of new technology, but this is ever present when 
it comes to media. From the Tower of Babel to the printing 
press, it seems every technological leap has demanded dis­
cernment about whether innovation clarifies divine truth or 
obscures it. AI presents a similar dilemma; it is just encoded 
in silicon rather than ink. When generative models collapse 
Catholic, Orthodox, Protestant, and Restorationist distinc­
tions into a homogenized “Christianity,” they do not foster 
unity. They sow confusion.
Students raised in digital-first environments, hunger 
for authentic formation even as they navigate algorithmic 
substitutes. They are not rejecting faith; they are negotiat­
ing untested pathways toward it. Yet AI-generated answers 
often sound authoritative while reflecting only statistical 
echoes of the most common perspectives. Emerging empiri­
cal research confirms bias in generative AI systems can 
measurably influence religious education contexts, shap­
ing how doctrinal content is interpreted and retained [2]. 
Analyses of religious bias in generative models show that 
1  Introduction
The old fear was that machines might overpower us. The 
new fear is quieter but no less troubling: that they might 
mislead us. Artificial intelligence (AI) systems, from large 
language models such as ChatGPT, Claude, and Gemini to 
sermon-generating tools and pastoral chatbots, are quickly 
becoming interlocutors in matters of faith [1]. Christians 
now bring doctrinal questions, spiritual concerns, and even 
confessions of doubt to software that responds with fluency 
and confidence. This shift forces a pressing question: if AI 
becomes the voice shaping a believer’s understanding, who 
or what is doing the teaching?
	
 Jason Owen
jowen22@murraystate.edu
1	
Department of Computer Science and Information Systems, 
Murray State University, Murray, USA
Abstract
As artificial intelligence becomes a common source of religious information, concerns arise about whether its responses 
faithfully represent Christian doctrine. This study examines denominational misrepresentation in AI-generated content, 
focusing on how large language models handle theological distinctions across eleven Christian traditions. A doctrinal 
knowledge base was constructed from authoritative sources including catechisms, confessions, creeds, and denomina­
tional statements. From these materials, 576 atomic doctrinal claims were extracted and organised into eight canonical 
loci: Authority, Trinity, Salvation, Sacraments, Eschatology, Anthropology, Ecclesiology, and Christian Ethics. Responses 
from two leading AI models were evaluated against this knowledge base using precision, recall, and heuristic checks for 
contradiction and overgeneralization. Results show that while models achieve relatively high precision, accurately echoing 
many well-known statements, they demonstrate weak recall, frequently omitting large portions of each tradition’s teach­
ing. The systems also tend to flatten differences by attributing beliefs to “Christians” as a whole, and at times contradict 
core doctrines, especially in sacramental and eschatological contexts. By replacing dependence on scarce human reviewers 
with a structured, replicable knowledge base, this study introduces a scalable framework for doctrinal evaluation. The 
findings highlight both the potential and the risks of AI in digital catechesis: generative systems may sound reliable yet 
often reduce complex traditions to oversimplified or misleading summaries.
Keywords  Artificial intelligence · Large language models · Algorithmic bias · Trustworthy AI · Ethics of technology · 
Religious information systems
Received: 21 January 2026 / Accepted: 11 February 2026
© The Author(s) 2026
Detecting doctrinal flattening in AI generated responses
Jason Owen1
1 3

--- Page 2 ---

AI and Ethics           (2026) 6:178 
minority traditions are frequently ignored, while majority 
views dominate. Scholars describe this as “doctrinal flat­
tening,” where nuanced differences are erased and synthetic 
summaries take the place of rooted teaching.
This study directly addresses that problem. Instead of 
relying on scarce panels of theologians, it develops a doc­
trinal knowledge base of 576 atomic claims drawn from 
catechisms, confessions, creeds, and denominational state­
ments across eleven traditions. By scoring model outputs 
against this corpus, the project reveals systematic patterns: 
high precision but low recall, frequent flattening of denomi­
national differences, and occasional outright contradictions. 
The framework offers a replicable path for evaluating doc­
trinal integrity in AI, demonstrating that while machines 
can echo orthodoxy, they often reduce it to oversimplified 
fragments.
2  Literature review
Religious traditions have long reflected on the risks of sub­
stituting human invention for transcendent wisdom. In the 
Hebrew Scriptures, the story of Babel (Genesis 11) illus­
trates a community’s drive toward self-made transcendence, 
while the account of the golden calf (Exodus 32) highlights 
how quickly people invest ultimate trust in artifacts of their 
own making. Prophetic voices such as Isaiah extend this cri­
tique by questioning the reliability of created power struc­
tures. Later, early Christian writings reframed discernment 
as a collective responsibility, encouraging communities to 
seek wisdom (James 1:5) and to “test the spirits” (1 John 
4:1). While these reflections are theological in nature, they 
also function as early case studies in how societies respond 
to new forms of mediation. Read in this light, they provide 
a historical lens for considering the adoption of emerging 
technologies: from the printing press and radio to today’s 
digital platforms and generative AI, each new medium 
invites both enthusiasm and caution (Figs. 1, 2, 3 and 4).
Fig. 2  Mean Precision and Recall Scores by Language Model
 
Fig. 1  Workflow of the four-phase methodology
 
1 3
  178 
 
Page 2 of 11

--- Page 3 ---

AI and Ethics           (2026) 6:178 
Scholars working in digital religion have traced how 
new media reconfigure the ways authority is exercised, and 
belief is negotiated within religious life [3]. Campbell [4, 
5] shows that the internet redistributed religious authority, 
creating what she terms “networked religion,” where online 
and offline practices blend into one continuous sphere. 
Related work demonstrates that digital infrastructures shape 
not just the delivery of religious messages but also how 
those messages are interpreted within communities [6]. In 
that sense, when large language models such as ChatGPT 
or Gemini are asked to explain doctrine, the answers they 
produce become part of these broader authority shifts, much 
like previous waves of communication technology that 
reshaped religious life.
Fig. 4  Contradiction Rates by 
Doctrinal Topic
 
Fig. 3  Topic-Level Precision and Recall Heatmap
 
1 3
Page 3 of 11 
  178

--- Page 4 ---

AI and Ethics           (2026) 6:178 
and finally interpreting the results. The idea was to keep the 
process transparent and repeatable while still respecting the 
doctrinal sources being drawn from.
3.1  Phase 1: dataset construction
The first step was to collect the doctrinal texts that would 
form the basis of the dataset. Catholic sources included the 
Catechism of the Catholic Church, Lumen Gentium, Dei 
Verbum, and papal encyclicals such as Veritatis Splendor 
and Redemptoris Mater. Protestant materials included the 
classic confessions most theologians and church historians 
would likely expect, as well as, Westminster, Heidelberg, 
Augsburg, Luther’s Small Catechism, and the Thirty-Nine 
Articles. Texts were also added that continue to be used 
in denominational life today such as the Baptist Faith and 
Message 2000 and the Methodist Book of Discipline.
For the Orthodox tradition, the study included the Nicene-
Constantinopolitan Creed as well as widely circulated cat­
echisms. Pentecostal coverage came from the Assemblies of 
God, the Church of God (Cleveland), and Foursquare state­
ments. Broader Evangelical and non-denominational groups 
were represented by the Lausanne Covenant and the EFCA 
Statement of Faith. To capture Restorationist movements I 
used the Latter-Day Saints Articles of Faith and Jehovah’s 
Witnesses’ official Watchtower publications. Across all 
these documents, only foundational resources recognized 
by each tradition were included, rather than commentaries 
or fringe materials.
From this collection, 576 distinct “atomic” doctrinal 
claims were extracted. Each claim was tagged by tradi­
tion, topic, citation, and evidence quote, then organised into 
eight canonical loci: Authority & Revelation, God/Trinity, 
Anthropology & Sin, Salvation, The Church, Sacraments/
Ordinances, Eschatology, and Christian Life/Ethics. This 
dataset was then versioned and frozen (August 2025) as the 
reference point for all later evaluation.
3.2  Phase 2: knowledge base development and QA
Rather than convening human annotators, the study opera­
tionalized doctrine into a structured KB. Quality assurance 
procedures included:
	
●
Quote length check (< or = 25 words).
	
●
Duplicate detection across tradition × topic × statement.
	
●
Citation verification to ensure no missing references.
	
●
Topic normalization into eight loci.
	
●
Tradition collapsed into eleven groups (Catholic, Lu­
theran, Reformed, Anglican, Baptist, Methodist, Eastern 
Orthodox, Pentecostal, Evangelical/Non-Denom, LDS, 
Jehovah’s Witnesses).
From a psychological perspective, research has long 
noted that people respond to computers as if they were 
social beings. Early social psychology studies showed how 
users attribute intention or even empathy to machines that 
communicate fluently [7]. This phenomenon of “mechanical 
empathy” helps explain why many users accept responses 
from LLMs as pastorally trustworthy, even when those 
responses lack theological depth [8]. In practice, smooth 
language can give an illusion of reliability, disguising the 
absence of grounded doctrinal reasoning.
From an AI perspective, the problem begins with bias in 
training data. Foundational work in natural language pro­
cessing established that word embeddings absorb and rep­
licate human biases: Caliskan, Bryson, and Narayanan [9] 
demonstrated that statistical associations reproduce stereo­
types present in text, while Hovy and Spruit [10] catalogued 
how bias enters the NLP pipeline through data selection, 
annotation, representation, and evaluation. When applied 
to religious data, this implies that uneven coverage of tra­
ditions will yield models that privilege majority voices by 
default.
11. Abid, Farooqi, and Zou [11] documented how GPT-3 
produced consistent anti-Muslim associations, while there 
is an array of literature that demonstrates how LLMs stereo­
type religion, often flattening or misrepresenting minority 
traditions in persona-based generation tasks. Studies of hate 
speech classification show that automated systems often 
struggle to distinguish between offensive, abusive, and reli­
giously charged language, a limitation that can disadvan­
tage minority expressions of faith. [12]. Together, this body 
of work highlights that doctrinal flattening is not simply an 
artifact of model “hallucination,” but the predictable out­
come of statistical learning from biased datasets [13].
This evidence base motivates the present study’s focus on 
denominational misrepresentation. Whereas prior work has 
largely examined bias at the level of religion versus secular 
culture, or majority versus minority faiths, the project inter­
rogates how generative systems handle intra-Christian dif­
ferences such as Catholic versus Protestant, Orthodox versus 
Evangelical, sacramental versus symbolic. By operational­
izing denominational distinctives into a structured doctrinal 
knowledge base, the study situates itself at the intersection 
of theological vigilance and computational bias detection, 
addressing a gap in the literature where doctrinal nuance is 
often subsumed under generalized “Christian” identity.
3  Methodology
The project was completed in four broad stages. First a 
dataset was built, followed by shaping and checking the 
knowledge base. Next was running the evaluation pipeline 
1 3
  178 
 
Page 4 of 11

--- Page 5 ---

AI and Ethics           (2026) 6:178 
By shifting from human annotators to a structured doctri­
nal KB with a reproducible evaluation pipeline, this design 
created a transparent, scalable framework for detecting doc­
trinal misrepresentation in AI responses. The inclusion of 
seeded errors confirmed that the system was sensitive not 
only to omissions and generalizations but also to overt con­
tradictions. This approach demonstrates how computational 
methods can surface where models oversimplify, conflate, 
or distort tradition-rooted teachings, offering a replicable 
tool for future theological and technical research.
3.5  Computing environment and infrastructure
This study and coding and all technology used were con­
ducted via GitHub.com repository interacted with VS-Code. 
A standard local development environment using contem­
porary consumer hardware and open-source development 
tools was used.
3.5.1  Use of AI tools
Large language models (e.g., ChatGPT) were used dur­
ing the research process to assist with copy-editing and 
to generate preliminary code templates for data process­
ing. All doctrinal sources, annotations, statistical analyses, 
and interpretations were conducted and verified within the 
study’s methodological framework, and responsibility for 
the results and conclusions rests with the research design.
4  Results
The evaluation of 155 prompt–response pairs revealed a 
consistent pattern across the large language models under 
review. Overall, the systems achieved relatively high pre­
cision, with most responses aligning correctly with doctri­
nal statements contained in the knowledge base. Precision 
scores averaged 0.864 for GPT-4o and 0.801 for Gemini 2.5 
Flash, indicating that when the models did echo a doctrinal 
claim, it was usually accurate. By contrast, recall rates fell 
substantially lower, 0.561 for GPT-4o and 0.423 for Gem­
ini, showing that the responses captured only a portion of 
the doctrinal material expected for each tradition and topic. 
Practically speaking, this means that while models seldom 
introduced blatant theological errors, they regularly failed 
to present the breadth and depth of denominational teach­
ing. Contradictions were infrequent overall; however, when 
they appeared they struck at the heart of central doctrines. 
For example, several responses described the Eucharist as 
merely symbolic, which is a direct denial of Catholic and 
Orthodox teaching on the real presence of Jesus Christ.
Coverage dashboards and heatmaps confirmed balanced 
representation across groups and topics. The KB was 
archived with full documentation to ensure transparency 
and replicability.
The knowledge base is archived in a public repository; 
citation anonymized for double-anonymous review.
3.3  Phase 3: evaluation pipeline
AI-generated responses were collected from two large lan­
guage models: ChatGPT GPT-4o and Gemini 2.5 Flash. 
Each prompt was doctrinally sensitive and mapped to a 
specific tradition and topic. Records included the model’s 
name, prompt text, tradition, topic, and generated response. 
Responses were segmented into sentences and compared 
against the KB using a multi-step process:
	
●
Fuzzy string match (RapidFuzz) between response sen­
tences and KB statements (threshold > or = 80).
	
●
Contradiction heuristics detecting negations of core 
doctrinal terms.
	
●
Generalization flags for sweeping claims (e.g., “All 
Christians believe …”).
	
●
Precision/recall scoring at the sentence level, with recall 
denominators capped at ten KB statements per topic/tra­
dition to prevent bias toward longer traditions.
To benchmark sensitivity, a control seed set of 15–30 delib­
erately flawed responses was added. These contained known 
doctrinal misrepresentations (e.g., attributing transubstanti­
ation to Baptists) and confirmed that the pipeline could flag 
overt errors in addition to omissions and flattening.
3.4  Phase 4: analysis
Performance was summarized at both response and run 
levels. Metrics included mean precision, mean recall, con­
tradiction rate, and frequency of generalization flags by 
model, topic, and tradition. Results revealed a characteris­
tic pattern: relatively high precision, low recall, systematic 
flattening of denominational differences, and occasional 
contradictions (e.g., reducing the Eucharist to a purely sym­
bolic act). Sacramental and eschatological domains were the 
most error-prone, while authority and Trinitarian doctrines 
were represented more faithfully.
Flow diagram illustrating the design of the study: (1) 
Dataset Construction, (2) Knowledge Base Development 
and QA, (3) Evaluation Pipeline, and (4) Analysis. The dia­
gram highlights how doctrinal sources were extracted, oper­
ationalized into a frozen knowledge base, processed through 
automated evaluation, and analyzed for error patterns.
1 3
Page 5 of 11 
  178

--- Page 6 ---

AI and Ethics           (2026) 6:178 
were far more frequently represented, while Orthodox, 
Pentecostal, LDS, and Jehovah’s Witness perspectives 
were often underreported or missing. Even when models 
did engage with minority traditions, they often did so at a 
superficial level, omitting distinctive doctrines altogether. 
The result is a pattern of denominational bias shaped by the 
dominance of Western Christian discourse in training data. 
In the present dataset, minority-tradition prompts were too 
sparse to permit inferential statistical testing, but descriptive 
review corroborates the systematic underrepresentation of 
these perspectives.
Overall, the errors that emerged could be grouped into 
four main types. The most prevalent was doctrinal flatten­
ing, in which distinctive teachings were collapsed into gen­
eralized statements about “Christians” as a whole. Omission 
was also widespread, particularly with respect to minority 
traditions and less publicly discussed loci. Contradictions 
were rarer but serious when they appeared, usually in sacra­
mental or eschatological contexts. Finally, sweeping gener­
alizations, often framed as “all Christians believe…”, were 
a recurring issue. Taken together, these results show that 
large language models often appear theologically reliable 
on the surface but fail to offer comprehensive, tradition-spe­
cific accounts. Instead, they provide truncated or homog­
enized summaries that risk misleading users seeking faithful 
theological guidance.
Bar plots illustrate performance differences between 
ChatGPT GPT-4o and Gemini 2.5 Flash across the full 
evaluation dataset. GPT-4o achieved higher precision and 
recall on average, consistent with ANOVA results indicat­
ing significant model effects (F(2, 152) = 93.59, p < 0.001 
for precision; F(2, 152) = 30.20, p < 0.001 for recall). The 
comparative analysis shows that GPT-4o consistently out­
performed Gemini, producing statements more closely 
aligned with doctrinal claims and capturing a broader range 
of relevant content. These differences were not marginal 
but systematic, highlighting that theological reliability in 
AI is model-dependent and that reliance on weaker systems 
increases the likelihood of omission and flattening.
Mean values are displayed for each doctrinal locus, nor­
malized between 0 (low) and 1 (high). Authority and Reve­
lation demonstrated the strongest coverage, while Salvation 
and Sacraments showed markedly weaker recall. The chi-
square analysis confirmed that these differences were statis­
tically significant, χ2(4, 155) = 21.75, p < 0.001. This pattern 
indicates that generative models are more reliable when 
addressing broadly acknowledged doctrines such as biblical 
authority but are more vulnerable to flattening and misrep­
resentation when tasked with representing sacramental the­
ology or the dynamics of salvation, where denominational 
divergence is greatest.
It is important to note that a small subset of responses 
within the dataset were deliberately seeded with doctrinal 
errors to test the sensitivity of the evaluation framework. 
These intentionally flawed samples had expected behav­
iour and produced precision and recall values near zero. 
They were consistently flagged as contradictions or misat­
tributions when compared against the knowledge base, 
demonstrating that the pipeline could detect overt misrep­
resentation rather than only omissions or generalizations. 
Excluding these seeded examples, spontaneous contradic­
tions generated by the models were even less frequent, with 
most observed errors taking the form of flattening or omis­
sion rather than direct denials of doctrine.
Patterns became even clearer when the results were bro­
ken down by doctrinal locus. In matters of authority and 
Revelation, the models consistently acknowledged the cen­
trality of Scripture for Protestant traditions and magisterial 
authority for Catholicism, although they tended to omit sub­
tler emphases such as the Methodist quadrilateral or Pen­
tecostal appeals to Spirit-led revelation. Doctrines of the 
Trinity were generally handled well, with high precision and 
broad reflection of Nicene orthodoxy, but distinctive empha­
ses, such as Orthodox explorations of theosis, were rarely 
noted. Anthropological teachings on sin were unevenly 
represented; Protestant emphases on depravity were fore­
grounded more often than Catholic or Orthodox treatments 
of concupiscence and ancestral sin. Soteriology produced 
one of the clearest examples of flattening, as salvation was 
typically summarized in generic evangelical language, with 
sacramental or synergistic dimensions underrepresented or 
ignored altogether. Ecclesiological descriptions likewise 
defaulted to universal statements about “the Church,” offer­
ing little attention to denominational differences in polity or 
authority.
The domains of Sacraments and Eschatology proved 
most prone to error. In the sacramental sphere, Catholic and 
Orthodox affirmations of grace were frequently collapsed 
into memorialist interpretations, while distinctive Baptist 
or Pentecostal practices were either inaccurately described 
or entirely absent. Eschatological teaching suffered from 
a similar flattening, with most responses offering generic 
affirmations of Christ’s return and final judgment while 
neglecting the wide diversity of denominational views, from 
dispensationalist premillennialism to Orthodox emphases 
on resurrection and deification, or Restorationist teachings 
such as LDS exaltation. Ethical discussions fared somewhat 
better, with models competently addressing questions of 
family, justice, and morality, but even here the responses 
tended to mirror contemporary cultural debates rather than 
citing doctrinal foundations within specific traditions.
Analysis across traditions confirmed these tendencies. 
Catholic and Evangelical or broadly Protestant positions 
1 3
  178 
 
Page 6 of 11

--- Page 7 ---

AI and Ethics           (2026) 6:178 
floating propositions, but the living memory of a tradition 
shaped by councils, catechisms, liturgies, and the lived wit­
ness of the Church. When LLMs are trained on predomi­
nantly Western, English-language sources, they reproduce 
the contours of that landscape. The result is not deliberate 
deception but structural bias. Systems that appear neutral 
are, in practice, tradition selective. As Caliskan et al. [9] and 
Hovy & Spruit [10] have shown in broader NLP research, 
such bias is not a glitch but a function of the data itself.
Practically, this has implications for a range of stakehold­
ers. Churches and clergy must recognize that AI-generated 
theology may sound faithful but lack denominational depth. 
Educators should train students not only to use AI but to 
interrogate its theological assumptions. Developers building 
pastoral tools or catechetical apps must resist the temptation 
to “summarize Christianity” in generic terms and instead 
embed denominational nuance into their models and user 
interfaces. Finally, AI companies themselves bear respon­
sibility for transparency. Users deserve to know which tra­
ditions their answers are drawn from and what has been 
omitted.
This study does not argue that AI should be excluded 
from spiritual formation. On the contrary, it shows that AI 
can be a powerful aid but only when paired with theological 
accountability. The construction of a doctrinal knowledge 
base offers one model for how that accountability might be 
maintained. By making the sources explicit and the evalua­
tion criteria transparent, the project demonstrates that theo­
logical integrity can be operationalized without sacrificing 
replicability.
In the end, discernment in the age of generative models 
may not be about rejecting technology, but about remem­
bering what the Church has always known: that truth is not 
merely accurate speech, but faithful witness. As believ­
ers seek wisdom, they must learn to ask not only what the 
machine said, but whose voice it echoes and which voices 
are missing. Only then can the Body of Christ ensure that 
in the rush to speak fluently, it does not forget how to speak 
faithfully.
6  Conclusion
This study introduced and validated a framework for detect­
ing doctrinal misrepresentation in large language models 
by operationalizing theological corpora into a structured 
knowledge base and using it to benchmark model outputs. 
The results showed a consistent pattern: high precision but 
low recall, with models rarely producing blatant falsehoods 
yet frequently omitting essential denominational distinc­
tives. Such omissions are not random but clustered around 
complex doctrinal loci such as sacraments and salvation, 
Average proportion of flagged contradictions per sen­
tence across all models. Sacraments and Salvation domains 
exhibited the highest rates of doctrinal misrepresentation, 
while Authority and Revelation remained comparatively 
robust. These findings reinforce the pattern of greater vul­
nerability in sacramental and soteriological content, where 
errors are not only more frequent but also more theologi­
cally consequential. For the study, this underscores the 
heightened pastoral and educational risk of relying on AI 
for instruction in precisely those areas where doctrinal clar­
ity matters most.
5  Discussion
The findings of this study reveal a sobering paradox. Large 
language models can speak in the voice of orthodoxy, but 
they often do so without the substance of tradition [14]. 
High precision scores across both models indicate that, 
when a doctrinal claim was echoed, it was usually expressed 
correctly. Yet the low recall rates show that these models 
consistently omitted key elements of each tradition’s teach­
ing. In other words, the models were not prone to constant 
falsehood, but rather to partial truth, a subtler and, in many 
ways, more insidious form of doctrinal distortion.
This pattern is consistent with what scholars of digi­
tal religion have long described as “networked authority” 
[5], where spiritual knowledge is shaped by algorithmic 
mediation and flattened by the logic of scale. In such envi­
ronments, distinctive theological voices are frequently 
drowned out by dominant discourse. The study confirms 
that this same tendency persists in generative AI: Catholic, 
Orthodox, Pentecostal, and Restorationist perspectives were 
either underrepresented or reframed in the idiom of majority 
Protestant thought. Even where doctrinal statements were 
accurate, they were often incomplete, omitting sacramental, 
synergistic, or tradition-specific emphases.
The presence of seeded error samples provided an impor­
tant internal check on the robustness of the pipeline. These 
deliberately flawed responses were consistently flagged by 
the knowledge-based comparison thus confirming that the 
system can detect overt contradiction as well as more sub­
tle forms of flattening. Their inclusion highlights a critical 
distinction between model-generated omissions and inten­
tional misrepresentation. While the latter is easy to spot, the 
former is often indistinguishable from sincerity. This dis­
tinction matters deeply in pastoral contexts where believers 
may trust fluent but incomplete responses without realizing 
what has been left unsaid.
From a theological perspective, the findings raise impor­
tant questions about the role of discernment in an age of 
algorithmic mediation. Christian doctrine is not a set of 
1 3
Page 7 of 11 
  178

--- Page 8 ---

AI and Ethics           (2026) 6:178 
limitations in the dataset as much as shortcomings in the 
models themselves.
The evaluation pipeline also reflects deliberate trade-offs. 
Precision, recall, and contradiction rates were scored at the 
sentence level using fuzzy matching and simple heuristics 
for negation and generalization. This approach highlighted 
omissions and blatant denials, but it cannot address more 
subtle concerns, such as tone, pastoral adequacy, or the 
way multiple doctrines interact within a single response. A 
model output could be technically accurate yet misleading 
in context, and our current system would not capture that. 
Similarly, the recall denominator was capped at ten claims 
per tradition-topic pair to prevent long traditions from over­
whelming the scoring, a design choice that simplifies com­
parison but undercounts doctrinal breadth in some cases.
Relatedly, the heuristics used here are transparent but 
blunt. Fuzzy matching rewards surface-level overlap and 
may miss deeper paraphrase; negation detection flags direct 
contradictions but cannot weigh the significance of qualifi­
ers or nuance (“ordinarily,” “insofar as”). In practice, these 
methods favour reproducibility and speed over interpretive 
depth.
Language is another limiting factor. Nearly all prompts 
and responses were in English, and non-English sources 
were accessed through translations. Nuances that hinge on 
original languages or liturgical use in non-Western settings 
remain outside the present scope, making multilingual con­
clusions tentative at best.
Sampling design introduces further constraints. While 
the study included multiple generations per prompt, tradi­
tion and topic counts were uneven, and minority-tradition 
outputs were too sparse to support some statistical com­
parisons. This limits the strength of conclusions about 
denominational bias beyond the Catholic–Protestant core. 
The statistical design itself also has room for refinement. 
ANOVA and chi-square tests provided useful contrasts, but 
because responses cluster by prompt and model, indepen­
dence is imperfect. A mixed-effects design with prompt-
level random effects would offer stronger inferences in 
future work.
Finally, the study is tied to its time and scope. Only two 
contemporary LLMs (GPT-4o and Gemini 2.5 Flash) were 
tested, and both within a single window in Summer 2025. 
AI systems evolve quickly, so while the framework is repro­
ducible, the specific error rates and distributions reported 
here will not remain static. The inclusion of a small “seed” 
set of deliberately flawed responses also served its purpose, 
verifying pipeline sensitivity, but does not reflect real-world 
usage.
Despite these limitations, the study also has important 
strengths. The decision to operationalize doctrine into a fro­
zen, transparent knowledge base allowed for reproducibility 
confirming that generative systems systematically under­
represent minority or nuanced perspectives.
For computer scientists, the central contribution is meth­
odological. By converting doctrinal texts into atomic claims 
and scoring model outputs against them with precision, 
recall, and contradiction heuristics, the project demonstrates 
how domain-specific misrepresentation can be quantified. 
Although the present study focused on Christian theology, 
the same approach could apply to any high-stakes field 
where partial truth poses risk from legal reasoning to medi­
cal advice to cultural heritage preservation. This positions 
doctrinal bias as a case study within the broader challenge 
of domain-sensitive AI evaluation.
The implications for AI research are clear. First, omission 
must be treated as a first-class error mode alongside hallu­
cination. Models that generate partial truths can mislead as 
effectively as models that generate falsehoods. Second, fine-
grained evaluation requires structured reference corpora, 
whether theological, legal, or scientific, rather than generic 
QA datasets. Third, developers should integrate knowledge-
base-driven moderation layers capable of flagging flatten­
ing, generalization, or contradiction in real time.
Future work should expand the doctrinal knowledge 
base to include underrepresented traditions such as East­
ern Orthodoxy and additional global voices, automate the 
extraction of atomic claims at scale, and test the pipeline on 
real-time applications like chat assistants and educational 
platforms. Such extensions will not only improve the theo­
logical fidelity of AI in faith contexts but also advance the 
broader computer science agenda of building transparent, 
accountable systems capable of engaging responsibly with 
specialized human domains.
The broader takeaway for AI researchers is that theo­
logical integrity is one example of a more general require­
ment. Large language models must be evaluated not only 
for fluency but for faithfulness to domain-specific truth. The 
framework developed here offers a replicable pathway for 
ensuring that when models speak confidently about sensi­
tive human domains, they do so with clarity, accuracy, and 
accountability.
6.1  Limitations
Like any focused study, this work comes with boundaries 
that shape how its findings should be interpreted. The doc­
trinal knowledge base, while sizable at 576 atomic claims 
across eight theological loci, cannot capture the full com­
plexity of global Christianity. The strongest coverage lies in 
well-documented Western traditions, whereas perspectives 
from Eastern Orthodoxy, Pentecostal subfamilies, and Res­
torationist groups remain comparatively thin. This imbal­
ance means that some gaps in recall or precision may reflect 
1 3
  178 
 
Page 8 of 11

--- Page 9 ---

AI and Ethics           (2026) 6:178 
More broadly, this line of inquiry highlights that theology is 
one case of a general problem: how to ensure that AI sys­
tems treat specialized human domains with nuance rather 
than distortion. Advancing this work will require collabo­
ration not only between technologists and theologians, but 
also across disciplines concerned with cultural preservation, 
ethics, and trustworthy AI.
Appendix A
Prompt selection rationale and sensitivity
The twenty prompts used in this study were selected to rep­
resent doctrinal questions that are (a) commonly posed by 
lay users to generative AI systems, (b) theologically salient 
across multiple Christian traditions and (c) known points 
of denominational divergence rather than consensus. Each 
prompt was intentionally framed in a generalized manner 
(e.g., “What do Christians believe…”) to test the models’ 
tendency toward aggregation, flattening, or tradition-spe­
cific differentiation.
It is acknowledged that alternative prompt formulations 
or additional prompts could yield variation in specific sur­
face-level responses. However, the study does not claim that 
these twenty prompts exhaustively represent Christian doc­
trine. Rather, they function as a diagnostic sample designed 
to surface systematic patterns of omission, generalization, 
and contradiction. Pilot testing with paraphrased variants 
of selected prompts produced similar qualitative error pat­
terns, suggesting that the observed tendencies, particularly 
doctrinal flattening and low recall, are robust to reasonable 
prompt variation.
Prompts used to generate AI content
1.	 Salvation
“What do Christians believe about how one is saved?”
2.	 Authority
“Who has the authority to interpret Scripture in 
Christianity?”
3.	 The Eucharist
“What do Christians believe about Communion?”
4.	 Mary
“What role does Mary play in the Christian faith?”
5.	 Confession
“Do Christians need to confess sins to a priest?”
6.	 Grace & Works
and open scrutiny in ways rare in theological or AI research. 
The use of seeded error responses provided an internal vali­
dation check, confirming that the pipeline detects misrepre­
sentation rather than only omissions. Most significantly, the 
framework is not bound to theology alone: the same design 
could be applied to any specialized domain where omis­
sion is as harmful as outright error. These choices provide 
a degree of clarity and replicability that help balance the 
inevitable constraints of scope and design.
6.2  Future research
Building on this foundation, several directions merit fur­
ther exploration. First, the doctrinal knowledge base itself 
should be expanded. While this study operationalized 576 
atomic claims across major Christian traditions, broader 
coverage of Eastern Orthodox, Pentecostal, Charismatic, 
and Restorationist perspectives is needed to reduce imbal­
ance. Automating the extraction of atomic doctrinal claims 
at scale, using NLP-assisted chunking and alignment, would 
make such expansion feasible and reproducible.
Second, linguistic scope requires deliberate extension. 
Future iterations should test prompts in major global and 
liturgical languages such as Portuguese, Tagalog, Ara­
bic, and Swahili, thereby capturing theological nuance as 
expressed beyond English-speaking contexts. This would 
both strengthen cross-cultural validity and allow research­
ers to examine how LLM outputs shift when queried in non-
English settings.
Third, longitudinal evaluation is essential. Running iden­
tical doctrinal prompts across successive versions of LLMs 
would allow researchers to measure “doctrinal drift” and 
assess whether newer models show improved recall, fewer 
contradictions, or changing denominational bias. Such work 
would also establish baselines for model stability over time.
Fourth, applied tools represent a promising next step. 
Embedding this pipeline into real-time plugins, dashboards, 
or moderation layers could allow clergy, educators, and 
even AI developers to automatically flag omissions, gener­
alizations, or contradictions during use. This would shift the 
framework from an evaluative research tool to a practical 
safeguard.
Finally, there is a need for formalization. The error cat­
egories identified here: flattening, omission, contradiction, 
bias, and vague generalization, could be developed into an 
ethical and technical rubric akin to domain-specific evalua­
tion standards. Such a framework might one day resemble 
ISO-style benchmarks, providing developers with struc­
tured criteria for evaluating doctrinal (or, more broadly, 
domain-specific) fidelity in generative systems. Through 
these avenues, future research can extend the representa­
tiveness, applicability, and accountability of the framework. 
1 3
Page 9 of 11 
  178

--- Page 10 ---

AI and Ethics           (2026) 6:178 
Data availability  The doctrinal knowledge base and evaluation mate­
rials generated for this study, titled “Doctrinal Knowledge Base for 
Evaluating Flattening in AI Generated Responses,” are publicly avail­
able via the Zenodo repository. The dataset includes the structured 
doctrinal claims, annotations, and evaluation artefacts used in the 
analysis and is accessible at Zenodo under the persistent identifier ​h​t​t​p​
s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​5​2​8​1​/​z​e​n​o​d​o​.​1​7​1​3​7​5​4​2​.​
Declarations
Conflict of interest  The authors declare no competing interests.
Open Access   This article is licensed under a Creative Commons 
Attribution 4.0 International License, which permits use, sharing, 
adaptation, distribution and reproduction in any medium or format, 
as long as you give appropriate credit to the original author(s) and the 
source, provide a link to the Creative Commons licence, and indicate 
if changes were made. The images or other third party material in this 
article are included in the article’s Creative Commons licence, unless 
indicated otherwise in a credit line to the material. If material is not 
included in the article’s Creative Commons licence and your intended 
use is not permitted by statutory regulation or exceeds the permitted 
use, you will need to obtain permission directly from the copyright 
holder. To view a copy of this licence, visit ​h​t​t​p​:​/​/​c​r​e​a​t​i​v​e​c​o​m​m​o​n​s​.​o​
r​g​/​l​i​c​e​n​s​e​s​/​b​y​/​4​.​0​/.
References
1.	
Alkhouri, K.I.: The role of artificial intelligence in the study of 
religious practices and rituals: ethics and transformation. Reli­
gions 15(3), 290 (2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​3​3​9​0​/​r​e​l​1​5​0​3​0​2​9​0
2.	
Zhang, J., Song, W., Liu, Y.: Cognitive bias in generative AI influ­
ences religious education. Sci. Rep. (2025). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​3​
8​/​s​4​1​5​9​8​-​0​2​5​-​9​9​1​2​1​-​6
3.	
Singler, B.: “Blessed by the algorithm”: theistic conceptions of 
artificial intelligence as entanglements of AI and religion. AI Soc. 
35(4), 1037–1050 (2020). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​0​0​1​4​6​-​0​2​0​-​0​0​
9​6​8​-​2
4.	
Campbell, H.A.: Who’s got the power? Religious authority and 
the internet. J. Comput.-Mediat. Commun. 12(3), 1043–1062 
(2007). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​1​1​/​j​.​1​0​8​3​-​6​1​0​1​.​2​0​0​7​.​0​0​3​6​2​.​x
5.	
Campbell, H.A.: When religion meets new media. Routledge 
(2011). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​3​2​4​/​9​7​8​0​2​0​3​6​9​5​3​7​1
6.	
Kluver, R., Cheong, P.H.: Technological modernization, the inter­
net, and religion in Singapore. J. Comput. Mediat. Commun. 
12(3), 1122–1142 (2007)
7.	
Nass, C., Moon, Y.: Machines and mindlessness: social responses 
to computers. J. Soc. Issues 56(1), 81–103 (2000). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​
/​1​0​.​1​1​1​1​/​0​0​2​2​-​4​5​3​7​.​0​0​1​5​3
8.	
Egunjobi, J.P.: The misuse of AI-generated content in academic 
and religious settings. Int. J. Res. Sci. Innov. (2025). ​h​t​t​p​s​:​/​/​d​o​i​.​o​
r​g​/​1​0​.​5​1​2​4​4​/​I​J​R​S​I​.​2​0​2​5​.​1​2​1​5​0​0​0​7​7​P
9.	
Caliskan, A., Bryson, J.J., Narayanan, A.: Semantics derived 
automatically from language corpora contain human-like biases. 
Science 356(6334), 183–186 (2017). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​2​6​/​s​c​i​e​
n​c​e​.​a​a​l​4​2​3​0
10.	 Hovy, D., Spruit, S.L.: The social impact of natural language pro­
cessing. Proceedings of the 59th Annual Meeting of the Associa­
tion for Computational Linguistics, 5888–5903. (2021) ​h​t​t​p​s​:​/​/​r​e​s​
e​a​r​c​h​.​t​u​d​e​l​f​t​.​n​l​/​e​n​/​p​u​b​l​i​c​a​t​i​o​n​s​/​t​h​e​-​s​o​c​i​a​l​-​i​m​p​a​c​t​-​o​f​-​n​a​t​u​r​a​l​-​l​a​n​g​
u​a​g​e​-​p​r​o​c​e​s​s​i​n​g
11.	 Abid, A., Farooqi, M., Zou, J.: Persistent anti-Muslim bias in 
large language models. In: Proceedings of the 2021 AAAI/ACM 
“How do faith and good works relate in Christian 
salvation?”
7.	 The Saints
“Do Christians pray to saints?”
8.	 The Bible
“What is the Christian view on Scripture and tradition?”
9.	 The Church
“What is the role of the Church in salvation?”
10.	Baptism
“Why do Christians baptize infants or adults?”
11.	 Papal Authority
“Do Christians believe the Pope is infallible?”
12.	Justification
“What is justification in Christian theology?”
13.	Sacraments
“What are the sacraments and how do they differ between 
Christians?”
14.	Heaven & Hell
“What happens after death according to Christianity?”
15.	The Role of Women
“Can women be priests or pastors in Christianity?”
	
●
Marriage and Divorce
“What do Christians believe about marriage and 
divorce?”
	
●
Birth Control
“What do Christians believe about birth control or 
contraception?”
	
●
Debt and Money
“What do Christians believe about taking on debt or 
borrowing money?”
	
●
Adultery and Sexual Sin
“What do Christians believe about adultery and sexual 
sin?”
	
●
Addiction and Recovery
“How do Christians view addiction and the path to 
recovery?”
Supplementary 
Information  The 
online 
version 
contains 
supplementary material available at ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​4​3​6​8​1​-​0​
2​6​-​0​1​0​5​1​-​0.
Author contributions  100% of all work in this study was conducted 
by the single author.
1 3
  178 
 
Page 10 of 11

--- Page 11 ---

AI and Ethics           (2026) 6:178 
14.	 Weizenbaum, J.: Computer power and human reason: From judg­
ment to calculation. W. H. Freeman. (1976) ​h​t​t​p​s​:​/​/​w​w​w​.​r​e​s​e​a​r​c​h​
g​a​t​e​.​n​e​t​/​p​u​b​l​i​c​a​t​i​o​n​/​2​8​6​0​5​8​7​2​4​_​C​o​m​p​u​t​e​r​_​P​o​w​e​r​_​a​n​d​_​H​u​m​a​n​
_​R​e​a​s​o​n​_​F​r​o​m​_​J​u​d​g​m​e​n​t​_​t​o​_​C​a​l​c​u​l​a​t​i​o​n
15	 Abrar, A., Oeshy, N. T., Kabir, M., & Ananiadou, S. (2025, Janu­
ary 14). Religious bias landscape in language and text-to-image 
models: Analysis, detection, and debiasing strategies. arXiv. ​h​t​t​p​
s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​5​0​1​.​0​8​4​4​1
Publisher's Note  Springer Nature remains neutral with regard to juris­
dictional claims in published maps and institutional affiliations.
Conference on AI, Ethics, and Society (AIES ’21), 298–306. 
(2021) ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​4​5​/​3​4​6​1​7​0​2​.​3​4​6​2​6​2​4
12.	 Fortuna, P., Soler, J., Wanner, L.: Toxic, hateful, offensive or 
abusive? What are we really classifying? In: Proceedings of the 
12th Language Resources and Evaluation Conference (pp. 6786–
6794). European Language Resources Association. (2020) ​h​t​t​p​s​:​/​
/​a​c​l​a​n​t​h​o​l​o​g​y​.​o​r​g​/​2​0​2​0​.​l​r​e​c​-​1​.​8​3​8​/
13.	 Brenner, D., Chaudhary, Y., Geraci, R., Graves, M., Griese, H., 
Kruger, E., Ryan, Y.: Technical and religious perspectives on AI 
misinformation and disinformation. SSRN (2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​
/​1​0​.​2​1​3​9​/​s​s​r​n​.​4​3​6​0​4​1​3
1 3
Page 11 of 11 
  178
