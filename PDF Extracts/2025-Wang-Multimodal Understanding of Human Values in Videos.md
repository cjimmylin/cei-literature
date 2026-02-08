---
title: "2025-Wang-Multimodal Understanding of Human Values in Videos - PDF Extract"
source_pdf: "2025-Wang-Multimodal Understanding of Human Values in Videos.pdf"
pages: 15
extracted_at: "2026-02-08T06:02:21.349885"
---

# PDF Extract: 2025-Wang-Multimodal Understanding of Human Values in Videos

**Source PDF:** 2025-Wang-Multimodal Understanding of Human Values in Videos.pdf
**Total Pages:** 15

---

## Content

```
--- Page 1 ---

The Value of Nothing*:
Multimodal Extraction of Human Values Expressed by TikTok Influencers
Alina Starovolsky-Shitrit†1, Alon Neduva†2, Naama Appel Doron1, Ella Daniel1, Oren Tsur2
1Tel-Aviv University
2Ben-Gurion University of the Negev
alinashitrit@mail.tau.ac.il, neduva@post.bgu.ac.il, {naamaapp, della}@tauex.tau.ac.il, orentsur@bgu.ac.il
Abstract
Societal and personal values are transmitted to younger gen-
erations through interaction and exposure. Traditionally, chil-
dren and adolescents learned values from parents, educators,
or peers. Nowadays, social platforms serve as a significant
channel through which youth (and adults) consume informa-
tion, as the main medium of entertainment, and possibly the
medium through which they learn different values. In this pa-
per we extract implicit values from TikTok movies uploaded
by online influencers targeting children and adolescents. We
curated a dataset of hundreds of TikTok movies and anno-
tated them according to the Schwartz Theory of Personal
Values. We then experimented with an array of Masked and
Large language model, exploring how values can be detected.
Specifically, we considered two pipelines – direct extraction
of values from video and a 2-step approach in which videos
are first converted to elaborated scripts and then values are
extracted.
Achieving state-of-the-art results, we find that the 2-step ap-
proach performs significantly better than the direct approach
and that using a trainable Masked Language Model as a sec-
ond step significantly outperforms a few-shot application of a
number of Large Language Models. We further discuss the
impact of fine-tuning and compare the performance of the
different models on identification of values present or con-
tradicted in the TikTok. Finally, we share the first values-
annotated dataset of TikTok videos. Our results pave the way
to further research on influence and value transmission in
video-based social platforms.
1
Introduction
The transmission of values between generations is a key pro-
cess for the preservation of society (Sch¨onpflug 2001). Clas-
sic research assumed that transmission of values is carried
out mainly by parents (Grusec 2011) or schools (Berson and
Oreg 2016). However, youth spend hours every day on so-
cial media (Smahel et al. 2020), where they encounter new
role models (Tolbert and Drogos 2019). The social media
environment has been shown to strongly influence children’s
behavior, in the context of consumer behavior (Coates et al.
*“Nowadays people know the price of everything and the value
of nothing,” The Picture of Dorian Gray (Wilde 1890)
†Authors contributed equally.
Copyright © 2025, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
2019). However, influencers in social media promote more
than products: they form communities, by establishing con-
nections, encouraging engagement, and promoting shared
values (Himelboim and Golan 2023).
The Schwartz Theory of Personal Values (Schwartz 1992)
offers a well-studied framework for the investigation of hu-
man motivation. It defines values as abstract goals, describ-
ing the end states aspired by people to achieve in their lives,
such as success, independence, and care. These goals cover
a wide range of motivations, with different individuals and
societies, varying in the prioritization they place on different
values (Schwartz 1992; Sagiv and Schwartz 2022). The the-
ory identifies 19 core values, characterized by the goals they
promote (Schwartz 2012). The values and their definitions,
as used in the shared taskes at SemEval-2023 (Kiesel et al.
2022) and CLEF-2024 (Kiesel et al. 2024b) are provided in
Table 1. Those 19 values are expressed through a wide va-
riety of judgments, evaluations, and behaviors (Sagiv and
Roccas 2021). Personal values, as defined by Schwartz, were
consistently identified in different contexts, such as national
cultures throughout the world (Sagiv and Schwartz 2022),
organizational cultures (Daniel, Arieli, and Akerman 2024),
traditional media (Kiesel et al. 2024a), and online disagree-
ments (van der Meer et al. 2023).
In this work we suggest that social media influencers tar-
geting youth can be characterized not only by genre, topic,
and style, but also by the values they pursue and promote.
For example, influencers hosting competitions between fol-
lowers promote values of achievement, those presenting a
unique craft project promote creativity, and others who pull
pranks on strangers promote disregard for social norms. A
specific example, presented in Table 2, depicts a gaming
influencer failing to return tennis balls served by a profes-
sional tennis player. The values manifested in the video are
Achievement (trying to properly return fast serves) and
conflicted Face (the influencer show himself failing again
and again to no avail).
How can we identify the values transmitted to youth
through social media? This question has only recently be-
gan to be addressed. Some studies identified values prevalent
in written social media using methods ranging from LIWC
word matching to masked language models (e.g., BERT)
(Kumar et al. 2018; Silva, Lo, and Lim 2020). However, re-
cent trends lean heavily toward visual based social media,
arXiv:2501.11770v1  [cs.CL]  20 Jan 2025

--- Page 2 ---

such as TikTok (Smahel et al. 2020; Rejeb et al. 2024). The
shift toward visual mediums introduces further challenge,
since it requires analyzing a clip, combining text, audio, and
video. Further, the clips are typically very short, providing
content through little stimuli. To the best of our knowledge,
this is the first attempt to extract values from TikTok specif-
ically, and visual social media in general.
In this work we experiment with an array of algorithms
to extract values from TikTok videos targeting adolescents.
To that end, we have curated a unique annotated corpus of
890 TikToks, posted by influencers targeting children and
adolescents, covering a variety of genres prevalent in Tik-
Tok (see Section 3 for details). The corpus is useful for the
investigation of values prevalent in this platform, and will be
open for analysis.
We further experiment with and compare methods of
value extraction, including fine-tuned Masked Language
Models and Large Language Models. We go on to evalu-
ate each method against the manual annotations, to identify
the most effective one. Specifically, we consider two main
pipelines: a direct extraction from LLMs, leveraging their
multimodal capabilities, and a 2-step extraction approach in
which a video is first converted to a detailed textual script
(master scene heading, action, dialogue) and the values are
extracted from the text, rather than directly from the video.
We achieve a higher F-score than previously reported state-
of-the-art results (Schroter, Dementieva, and Groh 2023;
Legkas et al. 2024), in spite the more challenging setting (a
direct comparison is unattainable, see Section 2). We find
that that the 2-step approach perform better than the di-
rect approach and that using a trainable Masked Language
Model in the second step significantly outperforms a few-
shot application of a Large Language Model. We further dis-
cuss the impact of fine-tuning and compare the performance
of the different models on the present manifestation of val-
ues and the conflicted manifestations. Finally, we share the
first values-annotated dataset of TikTok videos.
2
Related Work
TikTok and Influencers Research
Youth spend hours on
various social media sites (Smahel et al. 2020; Tome and
Cardita 2021), with TikTok gaining increased popularity
(Anderson, Faverio, and Gottfried 2023; Woodward 2024).
TikTok is characterized by engaging short videos that can
include pervasive use of filters, and background music (Re-
jeb et al. 2024). The use of a costume “for you” page and
“like” button increases immersion in the application (Mon-
tag, Yang, and Elhai 2021).
Social media in general, and TikTok specifically, are char-
acterized by a large number of Social Media Influencers
(SMIs). Social media influencers are social media users who
gained large following (Ki et al. 2020) by creating and cu-
rating content that portrays an appealing online personal-
ity (Tafesse and Wood 2021). Influencers form parasocial
relationships with their followers: members of the audi-
ence feels close, as if they know the influencers intimately
(Reinikainen et al. 2020). Although parasocial relationships
are known within traditional mass media, they may increase
in the context of social media, because of its interactive na-
ture (Conde and Casais 2023; Lou and Yuan 2019), and the
disclosure of the influencers’ personal lives (Conde and Ca-
sais 2023). Followers often identify with their favorite influ-
encers (Lou and Yuan 2019), making them likely role mod-
els for young viewers.
Ample research supports the understanding that children
and adolescents can learn from mass traditional media (Prot
et al. 2015), as well as social media (Ragelien˙e and Grønhøj
2021; Craig, Brooks, and Bichard 2021). From the media,
youth can acquire information (Dorey and McCool 2009),
but also form their worldviews (Duffett 2017). A recent
study established that the following of social media in-
fluencers is associated with higher importance ascribed to
materialistic values among Finish youth (Tuominen et al.
2023). We suggest that in order to further investigate the role
of influencers in youth value transmission, we must identify
the values they embrace.
Personal Values
Values are abstract goals describing end-
states individuals aspire to achieve in their lives (Sagiv and
Schwartz 2022; Schwartz 1992). Values direct a wide vari-
ety of behaviors, ranging between life-altering choices, such
as career preferences (Lipshits-Braziler, Arieli, and Daniel
2024), and daily behaviors, such as the choice of touristic
destinations (Saji, Vij, and Kabiraj 2015).
The Schwartz Theory of Personal Values is the leading
theory of values in social psychology, well-validated in hun-
dreds of samples across the world (Sagiv and Roccas 2017).
Importantly, the theory extends beyond moral values, such
as justice and care, to define a variety of motivations that can
motivate individuals (Twito-Weingarten and Knafo-Noam
2022), including, for example, safety, excitement, and in-
fluence. Moreover, the values are organized in a dynamic
system of inter-relations, as the pursuit of one value may
contrast the pursuit of conflicting values, yet enhance the
pursuit of compatible ones (Schwartz 1992). These inher-
ent trade-offs require individuals to prioritize among values.
The inter-relations can be summarized into two main axes.
One describes the opposition between self-transcendence
(care for others, close and distant) and self-enhancement (fo-
cus on advancement of self-interest). The second describes
the opposition between conservation (preservation of the
status-quo) and openness to change (embracing new expe-
riences).
Research established that children and adolescents hold
meaningful values, following the content and structure de-
fined by the Schwartz Theory of Personal Values (Daniel,
Misgav, and Chomsky 2024; Daniel and Benish-Weisman
2019; Knafo-Noam, Daniel, and Benish-Weisman 2023). It
is often agreed that children’s values are mainly learned
from the social environment, in a process of value trans-
mission (Twito and Knafo-Noam 2020). However, the so-
cial environment is varied and includes many socialization
agents. Such agents are parents (Grusec 2011; Knafo-Noam,
Barni, and Schwartz 2020), schools (Berson and Oreg 2016;
Auer et al. 2023), the peer group (Benish-Weisman, Oreg,
and Berson 2022; Benish-Weisman 2024), and the national
culture (Daniel et al. 2012). As social media becomes an im-

--- Page 3 ---

Value
Definition
SELF-DIRECTION–THOUGHT
Freedom to cultivate one’s own ideas and abilities
SELF-DIRECTION–ACTION
Freedom to determine one’s own actions
STIMULATION
Excitement, novelty, and change
HEDONISM
Pleasure and sensuous gratification
ACHIEVEMENT
Success according to social standards
POWER–DOMINANCE
Power through exercising control over people
POWER–RESOURCES
Power through control of material and social resources
FACE
Security and power through maintaining one’s public image and avoiding humiliation
SECURITY–PERSONAL
Safety in one’s immediate environment
SECURITY–SOCIETAL
Safety and stability in the wider society
TRADITION
Maintaining and preserving cultural, family, or religious traditions
CONFORMITY–RULES
Compliance with rules, laws, and formal obligations
CONFORMITY–INTERPERSONAL
Avoidance of upsetting or harming other people
HUMILITY
Recognizing one’s insignificance in the larger scheme of things
BENEVOLENCE–DEPENDABILITY
Being a reliable and trustworthy member of the in-group
BENEVOLENCE–CARING
Devotion to the welfare of in-group members
UNIVERSALISM–CONCERN
Commitment to equality, justice, and protection for all people
UNIVERSALISM–NATURE
Preservation of the natural environment
UNIVERSALISM–TOLERANCE
Acceptance and understanding of those who are different from oneself
Table 1: Value definitions, Schwartz Theory of Personal Values (Schwartz 1992, 2012)
portant factor in the lives of adolescents, it is crucial to learn
whether individuals within this sphere, such as influencers,
become socialization agents teaching youth personal values.
Values in the Media
Schwartz values were identified in
content displayed across social media platforms, such as
Instagram (Trill`o et al. 2021), Reddit (Chen et al. 2014),
Facebook and Twitter (Kumar et al. 2018). Values in so-
cial media content were presented in varied ways, such as
memes (Shifman 2019), and new-years’ resolutions (Halli-
nan et al. 2023). However, little is known about the preva-
lence of Schwartz values in youth-directed media. Some re-
search exists on the prevalence of values in child-directed
mass traditional media. An analysis of television shows ad-
dressing 9-11 year olds, showed high representation of val-
ues of fame (Uhls and Greenfield 2011). Similarly, television
shows addressing young children, displayed work as an ex-
pression of a large variety of values, including benevolence,
security, conformity, achievement, universalism, stimulation
and hedonism (Aharoni, Te’eni-Harari, and Eyal 2024). Our
work aims at opening the door to expand this work by de-
veloping an AI-based value classification in TikTok.
AI-Based Value Classification
The field of automated
value detection has evolved significantly. Focusing on meth-
ods for classifying values according to Schwartz’s The-
ory of Personal Values (Schwartz 2012), early approaches
leveraged the Linguistic Inquiry and Word Count (LIWC)
(Pennebaker et al. 2015), or a targeted dictionaries (Poni-
zovskiy et al. 2020) detecting values through lexical math-
cing. Values were detected in texts produced across various
platforms, including Twitter (Kadi´c-Maglajli´c, Lages, and
Pantano 2024), narrative texts (Fischer et al. 2022), song
lyrics (Demetriou et al. 2024), and social media platforms
such as Reddit (Oulahbib, Benhaddi, and El Hadaj 2024)
and Facebook (Kumar et al. 2018). Notable advances in-
clude the development of stack models combining LIWC
features trained on Facebook data with cross-platform val-
idation on Twitter (Silva, Lo, and Lim 2020). VALUENET
(Qiu et al. 2022), introduced a large-scale text dataset and
implemented a Transformer-based value regression model
for human value modeling in dialogue systems.
Recent developments in predicting values were intro-
duced with the application of masked langauge models. The
SemEval-2023 (Kiesel et al. 2022) and CLEF-2024 (Kiesel
et al. 2024b) competitions focused on value detection in ar-
gumentative texts and multi-lingual traditional media con-
texts respectively. These competitions demonstrated the ef-
fectiveness of BERT-based architectures (Schroter, Demen-

--- Page 4 ---

Figure 1: Values per movie in the annotated data.
tieva, and Groh 2023; Legkas et al. 2024) in capturing nu-
anced value expressions across two different text genres and
languages. It also demonstrated that the algorithm developed
in one context was not successful in identification of values
in a second context (Kiesel et al. 2024b), asserting the im-
portance of contextual models in value detection.
Generative AI methods were hardly utilized for value de-
tection, with the exception of the FULCRA project (Yao
et al. 2024), leveraging LLM-generated text pairs for safety-
oriented value detection. Our work extends these method-
ological advances by pioneering value detection in Tik-
Tok’s unique multimodal environment. Unlike previous ap-
proaches that focused on single modalities, TikTok content
presents a complex interplay of written text, audio, and vi-
sual elements. To address this challenge, we conduct a com-
parative analysis of two leading approaches: BERT-based
architectures and LLM-based methods. By evaluating these
distinct methodologies on the same TikTok dataset, we pro-
vide the first systematic comparison of their effectiveness in
detecting values within short-form video content. This novel
application to multimodal social media content, combined
with our comparative analysis, can contribute valuable in-
sights to both social media analysis and automated value de-
tection research, particularly for platforms where meaning is
conveyed through multiple channels simultaneously.
3
Data and Annotation
3.1
Data Curation
We identified potential TikTok influencers using surveys
of children and adolescents (anonymous survey, approved
by a the local IRB), and lists provided by three large lan-
guage models (ChatGPT, Gemini, Bing). Two research as-
sistants reviewed the potential influencers, to confirm they
are targeting children or adolescents and to classify them by
genre. This process resulted in a list of 89 influencers, pro-
ducing content in the major genres prevalent in child- and
adolescent-targeted TikTok: beauty and skincare, lifestyle,
entertainment and pranks, crafts and DYI, vlogging, gaming
and dancing, singing and lip-syncing. We sampled 10 Tik-
Toks from the page of each influencer. We first identified
the pinned TikToks, and supplemented the sample with the
last TikToks available on March 19, 2024, until a total of 10
TikToks was reached from each influencer, to the total N =
890.
We only selected TikToks that include verbal sound, such
as talking, narration or song. The crawling and curation were
done with slight modifications to the API shared by (Teather
2024).
3.2
Annotation Protocol
We constructed a codebook on the basis of the Schwartz the-
ory of personal values (Schwartz 1992, 2012). The codebook
included a definition to each of the 19 values derived from
the theory of personal values (Schwartz 2012). In addition,
the theory included examples of expression of these values
that are common on TikTok. The codebook included instruc-
tions for identifying values as present (1, marked as +), when
it is expressed or pursued in the TikTok; as absent (0), when
the TikTok does not refer to the value; or as conflicted (-
1, marked as -), when the TikTok contradicts or hinders the
pursuit of the value. Each TikTok could be annotated as re-
ferring to as many or as few values as relevant. A team of an-
notators was trained in value annotation. Each TikTok was
independently annotated by two annotators. A third anno-
tator consolidated the annotations by resolving discrepan-
cies. To assess inter-rater agreement on our nominally scaled
data, we considered various metrics beyond traditional π and
κ statistics, which are known to be sensitive to imbalanced
datasets (Gwet 2008). Given that our dataset exhibits signif-
icant imbalance, with the majority category (not present) ac-
counting for 0.76 of annotations and rare categories (conflict
and dominant) comprising only 0.06 and 0.03, we calculated
Gwet’s AC1 coefficient, which has been demonstrated to be
more robust against prevalence effects and marginal proba-
bility issues than Cohen’s Kappa (Wongpakaran et al. 2013).
Our analysis yielded an AC1 score of 0.77, indicating sub-
stantial inter-rater agreement despite the challenging data
distribution. The codebook is available at Appendix A.1.
In total, the annotated dataset of 890 TikTok TikToks,
were annotated with a total of 2968 labels (of values and
conflicting values). The distribution of values per movie is
presented in Figure 1 and the frequency of each value in
our dataset is presented in Figure 2. We make the annotated
dataset available at [URL to added in camera ready version].
4
Computational Approach
Our computational approach could be placed on three axes:
(i) Masked vs. Auto-regressive Language Models, (ii) Direct
vs. indirect, 2-step extraction from TikTok videos (marked d
versus s, repestecively), and (iii) Using pretrained LLMs vs.
fine-tuned models (marked FT). In the remainder of this sec-
tion we describe each axis and the way we integrate them.
Figure 3 provides a high-level illustration of the architec-
tures.
Masked vs. Auto-regressive Language Models
The clas-
sic machine learning framework depends on the availabil-
ity of a labeled dataset, facilitating training in a supervised
manner. A Masked Language Model (MLM) is pre-trained
to predict words that are masked at random. The MLM

--- Page 5 ---

Figure 2: Occurrences of each value in the annotated dataset. Blue bars indicate the appearance of a value (e.g., achievement)
and red bars indicate the conflicted value (e.g., apathy and lack of ambition, conflicting with achievement).
Figure 3: Direct and indirect extraction of values from Tik-
Tok movies. Fine tuning the textual models on scripts is op-
tional. LLMs are used in a zero/few-shot manner. The MLM
must be trained on a subsample in a supervised manner.
is then used to create a contextual embedding of an input
text, pushing it forward into a classification head. In this
work we experiment with both roBERTa-large (Liu 2019)
and DeBERTaV2-xlarge (He, Gao, and Chen 2023) with an
additional classification header performing transfer learning
(Devlin 2018). We use this supervised approach on textual
data only – the scripts and director notes extracted from the
videos by another model.
Generative (auto-regressive) Large Language Models
(LLMs) have been demonstrated to perform well on a range
of language processing and multimodal tasks. LLMs do not
require specific training (transfer learning) as classification
is done by prompting the model with the task description
(Radford et al. 2019; Brown et al. 2020; Kojima et al. 2022).
State-of-the-Art models such as ChatGPT.4o (OpenAI 2024)
and Gemini 1.5 Pro (Google 2024) are multimodal - allow-
ing the user to process different modalities such as text,
sound and video. In this work we use Gemini 1.5 Pro with a
prompt tailored for the specific tasks of script extraction and
for direct and 2-step classification (see below). In the 2-step
setting we also use Mistral 7B (Jiang et al. 2023).
Specifically, the prompt contains a short formal descrip-
tion of Schwartz’s theory of basic values, a definition for
each value, along with some examples and a request to iden-
tify the values in a given TikTok (an .mp4 file is uploaded).
The exact prompts are available in Appendix A.
Direct vs. 2-step Extraction
We use an LLM as a clas-
sifier in two settings – direct and indirect (2-steps). In the
direct setting we prompt the model to identify and extract
the values directly from the TikTok video. In the indirect ap-
proach we first prompt an LLM to extract the full script and
director’s notes from a TikTok and then extract the values
from the script, either in a supervised manner using one of
the MLMs or in a few-shot manner, using the exact same
prompt we used in the direct approach, albeit, replacing the
word ‘movie’ by the word ‘script’.
An example of a generated script is presented in Table 2.
We experiment with the different approaches for three
main reasons: First, previous work reported results over
text in a supervised setting. Secondly, the inner-workings of
(multimodal) LLMs are opaque and different prompts and
tasks may result in unstable results. Finally, while LLMs
are flashy and do not require supervision, it was argued that
they underperform on nuanced tasks such as the detection of
emotions, figurative language, implicit hate etc. (Ziems et al.
2024).
Transfer learning and Fine-tuning
Pretrained Language
Models, either masked or auto-regressive, serve as founda-
tional models and can be used as-is, either by prompting
(LLMs) or by performing transfer learning on a small an-
notated sample (MLMs). However, both types of language
models could be further fine-tuned on in-domain data, be-
fore the classification phase. Typically1, fine-tuning is done
1Fine-tuning can also be done as part of the classifier training.

--- Page 6 ---

Genre: Sports/Challenge
Sound: Yes
NARRATOR: "This pro tennis player Taylor Fritz with
one of the fastest serves on tour. His fastest serve
ever was 240 KM/H, but can I, a person who’s never
played tennis, return one?"
[pro]
TAYLOR FRITZ is shown on a tennis court serving, then
staring into the camera.
[#9 IN THE WORLD]
[with one]
[fastest]
[serves]
[240KM/H]
[I]
[never]
[return]
The NARRATOR is shown holding a tennis racket, about
to return a serve.
[SERVE 1]
TAYLOR FRITZ serves the ball. The NARRATOR misses.
NARRATOR: "Oof"
[SERVE 4]
TAYLOR FRITZ serves. The NARRATOR misses again.
NARRATOR: "Oh, yo, that was..."
[SERVE 10]
TAYLOR FRITZ serves. The NARRATOR misses.
NARRATOR: "F*ck"
[SERVE 18]
TAYLOR FRITZ serves. The NARRATOR misses.
NARRATOR: "F*ck. [giggles] Yo!"
[SERVE 24]
TAYLOR FRITZ serves. The NARRATOR misses.
NARRATOR: "F*ck, I thought I could do this."
[SERVE 32]
TAYLOR FRITZ serves. The NARRATOR misses.
NARRATOR: "F*ck no, I cannot!"
[SERVE 38]
TAYLOR FRITZ serves. The NARRATOR misses.
[SERVE 47]
TAYLOR FRITZ serves. The NARRATOR hits the ball back.
NARRATOR: "Oh! Where’d it go?"
[50TH SERVE]
TAYLOR FRITZ serves for the last time.
NARRATOR: "Oh, come on."
Table 2: The script generated by the video-to-script prompt
(Appendix A.2) for video ID 7341895431883967746
in a similar way to the pretraining, that is – given a dedicated
corpora, masked language models are fine-tuned by predict-
ing randomly masked words (Zaken, Goldberg, and Ravfo-
gel 2022), and autoregressive models are fine-tuned on next-
word prediction task (Hu et al. 2021). In this work we use
the roberta-large framework to fine-tune the roBERTa-large,
the DeBERTaV2-xlarge, and the Mistral LLM. We report
results obtained both by the basic pretrained models and the
fine-tuned models.
Compute Resources
All experiments and training were
executed on Google Colab Enterprise runtime environment
with an NVIDIA Tesla A100 GPU (a2-highgpu-1g configu-
ration).
5
Results, Analysis, and Discussion
The F-scores achieved by each of the models on each
of the nineteen values are presented in Figure 4 and the
weighted and macro F-scores are presented in Table 3. The
best overall results for values and their conflicted counter-
parts were achieved with the non-fine-tuned RoBERTa-large
(roBERTas) with weighted F-scores of 0.49/0.42/0.47 (pre-
sent/contradicted/all [+/−/all], respectively). These levels
of classification reflect the opacity of the signal, that cor-
responds to a multidimensional and complex human phe-
nomenon. In fact, even human annotators required extensive
training and still found the task non-trivial. At the same time,
these results are competitive with previously reported state-
of-the-art results (Schroter, Dementieva, and Groh 2023;
Legkas et al. 2024) achieved in less challenging settings in
which (i) text, rather than video, was the original medium
of the input, and (ii) the number of examples available for
training was an order of magnitude larger.2
Looking at specific values (Figure 4a), best classification
was achieved for Achievement (0.71), Benevolence
Dependability (0.61), and Security Personal
(0.58), all by the RoBERTas model. Achievement,
present in more than one third of the videos, is the most fre-
quent value in the annotated dataset, thus more occurrences
are found in training and in the test set. However, the two
other values occur far less than most values, hence perfor-
mance cannot be attributed to prior frequency alone.
A fine-grained analysis of the results by method and value
reveals interesting patterns, suggesting a number of insights.
We address some of these patterns in the remainder of this
section.
MLMs vs. LLMs
The best LLM results were obtained by
Geminid. However, it was outperformed by both RoBERTas
and DeBERTas in all metrics and over the three parti-
tions ({weighted, macro} × {+, −, all}, Table 3). Look-
ing at single values, we observe that Gemini outper-
forms the MLMs in cases in which the number of occur-
rences of the value is minimal, hence supervised training
is hampered, see results per value in Figure 4 and com-
pare to the value distribution Figure 2. An example is
Universalism Concern in the present manifestations,
and Power Resources in the contradiction manifesta-
tion.
These results are consistent with the literature, reporting
that strong supervised models tend to outperform current
LLMs on tasks requiring nuance, typical to the Computa-
tional Social Science (CSS) research (Ziems et al. 2024).
Pretraining vs. Fine-tuning
All the fine-tuned models
fell short, comparing to their pretrained counterparts. While
somewhat surprising, previous studies report similar trends
in various tasks and settings, e.g., (Zaken, Goldberg, and
Ravfogel 2022; Kumar et al. 2022), as well as in the best
performer in she value detection shared task (Schroter, De-
mentieva, and Groh 2023). Given the task and data at hand,
2A direct comparison is unattainable due to the very different
nature of the data in terms of source, medium and style.

--- Page 7 ---

0.00
0.18
0.35
0.53
0.71
 
 
  
 
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
  
 
 
  
 
  
 
 
 
 
 
 
 
 
 
 
  
 
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
  
 
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
  
 
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
  
 
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
  
 
 
 
 
  
 
 
 
 
 
 
 
 
th
ou
gh
t
ac
tio
n
do
mi
na
nc
e
re
so
ur
ce
s
pe
rs
on
al
so
ci
et
al
ru
le
s
in
te
rp
er
so
na
l
ca
rin
g
de
pe
nd
ab
ili
ty
co
nc
er
n
na
tu
re
to
le
ra
nc
e
Se
lf-
dir
ec
tio
n
St
im
ul
at
io
n
He
do
ni
sm
Ac
hi
ev
em
en
t
Po
we
r
Fa
ce
Se
cu
rit
y
Tr
ad
iti
on
Co
nf
or
mi
ty
Hu
mi
l i t
y
Be
ne
vo
le
nc
e
Un
iv
er
sa
l i
sm
roberta-large
roberta-large-FT
deberta-v2-xlarge
deberta-v2-xlarge-FT
Gemini-transcript
Gemini-video
Mistral
(a) Present manifestations (Max. F-Score: 0.71)
0.00
0.14
0.27
0.40
0.54
 
 
  
 
 
 
 
 
  
 
 
 
 
   
 
 
 
  
 
 
 
 
 
  
 
 
 
 
   
 
 
 
  
 
 
 
 
 
  
 
 
 
 
   
 
 
 
  
 
 
 
 
 
  
 
 
 
 
   
 
 
 
  
 
 
 
 
 
  
 
 
 
 
   
 
 
 
  
 
 
 
 
 
  
 
 
 
 
   
 
 
 
  
 
 
 
 
 
  
 
 
 
 
   
 
th
ou
gh
t
ac
tio
n
do
mi
na
nc
e
re
so
ur
ce
s
pe
rs
on
al
so
ci
et
al
ru
le
s
in
te
rp
er
so
na
l
ca
rin
g
de
pe
nd
ab
ili
ty
co
nc
er
n
na
tu
re
to
le
ra
nc
e
Se
lf-
dir
ec
tio
n
St
im
ul
at
io
n
He
do
ni
sm
Ac
hi
ev
em
en
t
Po
we
r
Fa
ce
Se
cu
rit
y
Tr
ad
iti
on
Co
nf
or
mi
ty
Hu
mi
l i t
y
Be
ne
vo
le
nc
e
Un
iv
er
sa
l i
sm
roberta-large
roberta-large-FT
deberta-v2-xlarge
deberta-v2-xlarge-FT
Gemini-transcript
Gemini-video
Mistral
(b) Contradicting manifestations (Max. F-Score: 0.54)
Figure 4: F-Scores per each model and value. Values appearing less than 30 times were not included in the BERT based MLM
models, thus excluded from the analysis (appearing with score 0 in the figure).
Masked Language Models
Large Language Models
roBERTas
DeBERTas
roBERTas
F T
DeBERTas
F T
Mistrals
Geminis
Geminid
Weighted+
0.49
0.44
0.30
0.33
0.29
0.33
0.40
Macro+
0.44
0.38
0.26
0.29
0.33
0.28
0.33
Weighted−
0.42
0.41
0.33
0.30
0.17
0.21
0.22
Macro−
0.35
0.35
0.27
0.25
0.22
0.18
0.22
Weightedall
0.47
0.43
0.31
0.33
0.26
0.30
0.35
Macroall
0.39
0.36
0.25
0.26
0.29
0.24
0.29
Table 3: Weighted and Macro F-Score results for the values (+), the conflicted values (−) and all (all). FT: fined-tuned model;
s indicates extraction from scripts (2-step extraction); d indicates direct extraction from video.
we attribute this result to the combination of two main fac-
tors: (i) The relatively small dataset used for finetuning, (ii)
The large number of imbalanced classes, as presented in Fig-
ure 2. Future work will explore the impact of each of these
factors.
Direct vs. 2-step Extraction
The textual models (MLMs)
applied in a 2-step pipeline and trained in a supervised man-
ner, achieved better results than Geminid applied directly on
the videos. However, comparing apples to apples, consid-
ering only the LLMs, we found that the direct application
of Geminid on the videos significantly outperformed the ap-
plication of both Geminis and Mistrals on the scripts in the
2-step pipeline. These results highlight the importance of the
visual and sound elements to the TikTok platform, and thus
the potential of the direct multimodal approach.
Present vs. Conflicting Manifestations
Most present val-
ues are more frequent (Figure 2) and better detected than val-
ues in conflict (Figure 4 and Table 3). It is interesting to note
that while Geminid, our top performing LLM, showed de-
cent performance on the present values (Weighted+ F-score
of 0.4, compared to 0.49 by the top performing model and
0.33 by the second best LLM), it perform poorly on the con-
flicting values, achieving an F-score of only 0.22, compared
to the 0.42 by the top performing model and only slightly
better than the other LLMs. This result is surprising: while
MLM results are expected to drop due to the smaller number
of labeled instances available for training, we would have
expected LLMs, used in a few-shot manner, to perform com-
parably on present and conflicting values. We have no plau-
sible explanation for this significant drop in performance
and intend to further explore it in the future.

--- Page 8 ---

Video to Script Conversion
Finally, the use of the mul-
timodal Gemini 1.5Pro to convert videos to detailed textual
script (master scene heading, action, dialogue) proved ben-
eficial for the task. We find the conversion to be reason-
ably accurate and the level of details provide useful mark-
ers. This conversion was vital for the application of the suc-
cessful MLM. Two points are worth highlighting: First, be-
fore converging on the final prompt (see Appendix A.2) we
have experimented with different prompts, producing differ-
ent outputs in various formats and detail. The evaluation of
the quality of the script was done in a qualitative manner by
two of the authors. Second, even the state-of-the-art mod-
els often fail to capture important details. For example, in
a humerus nonsensical TikTok showing the influencer air-
driving a car as a part of a guessing charade game, practi-
cally air driving, floating around in the room and bumping
into objects, the generated script failed to reflect the fact that
the influencer was actually moving in the air – the main point
of the video.
Limitations
This study is not without limitations. First,
we sampled influencers in seven specific genres. In our
dataset, we found much variability between the genres in
content as well as style. We identified genres most impor-
tant for children and adolescents, yet know that TikTok is
extremely varied, and other genres exist. Thus, it is yet to
verify that our results generalize across TikTok. Second, we
applied the Schwartz personal values theory to define and
identify values. This theory was tested across cultures and in
hundreds of samples across the world (Sagiv and Schwartz
2022), and is considered the leading theoretical framework
of values in social science. At the same time, the theory was
not constructed specifically within the context of social me-
dia, and does not focus on unique aspects of this context.
Specialized theories can add information for future investi-
gation (Shifman et al. 2025). Last, in our analysis, we uti-
lized two MLMs, and two LLMs. the use of other models
may offer different results, and future studies can extend this
investigation further.
6
Conclusions and Implications
We present pipeline for the extraction of personal values
from TikTok, and demonstrate their utility. We show that
(supervised) BERT based models outperform LLMs in value
extraction, and offer a method for conversion of multimodal
TikToks into text appropriate for BERT training and analy-
sis. We also show variability in detection between different
values, and between values supported and those contradicted
in the TikToks.
The methods presented have important implications for
research and society. TikTok emerged as a leading plat-
form among youth (Anderson, Faverio, and Gottfried 2023;
Woodward 2024), yet at the same time produces worry
among parents, educators, and decision makers (Conte et al.
2024). By applying value detection, research can move on
to investigate value transmission in TikTok at scale. Such
research can provide society with much needed information
regarding the social environment of young people. It is im-
portant to note that advertisers and influencers can make
similar use of the method, in order to target youth more
effectively. We follow (De Veirman, Hudders, and Nelson
2019) in call for policy makers and educators to mitigate
misuse of online platforms by enabling youth to better iden-
tify patterns of influence in social media.
References
Aharoni, M.; Te’eni-Harari, T.; and Eyal, K. 2024. Integrat-
ing values into the social learning process: The occupational
world in children’s television shows in Israel. Journal of
Children and Media, 1–19.
Anderson, M.; Faverio, M.; and Gottfried, J. 2023. Teens,
social media and technology 2023. Pew Res Cent.
Auer, P.; Makarova, E.; D¨oring, A. K.; and Demo, H. 2023.
Value transmission in primary schools: are teachers’ accul-
turation orientations a moderator? Frontiers in Education,
8: 1136303.
Benish-Weisman, M.; Oreg, S.; and Berson, Y. 2022. The
contribution of peer values to children’s values and behavior.
Personality and Social Psychology Bulletin, 48: 844–864.
Benish-Weisman, M. 2024. “Tell me who your friends are,
and I will tell you who you are:” The contribution of peers
to adolescents’ values. Child Development Perspectives.
Berson, Y.; and Oreg, S. 2016. The role of school princi-
pals in shaping children’s values.
Psychological Science,
27: 1539–1549.
Brown, T.; Mann, B.; Ryder, N.; Subbiah, M.; Kaplan, J. D.;
Dhariwal, P.; Neelakantan, A.; Shyam, P.; Sastry, G.; Askell,
A.; et al. 2020. Language models are few-shot learners. Ad-
vances in neural information processing systems, 33: 1877–
1901.
Chen, J.; Hsieh, G.; Mahmud, J. U.; and Nichols, J. 2014.
Understanding individuals’ personal values from social me-
dia word use. In Proceedings of the 17th ACM conference on
Computer supported cooperative work & social computing,
405–414.
Coates, A. E.; Hardman, C. A.; Halford, J. C.; Christiansen,
P.; and Boyland, E. J. 2019. Social media influencer mar-
keting and children’s food intake: A randomized trial. Pedi-
atrics, 143: e20182554.
Conde, R.; and Casais, B. 2023. Micro, macro and mega-
influencers on instagram: The power of persuasion via the
parasocial relationship. Journal of business research, 158:
113708.
Conte, G.; Iorio, G. D.; Esposito, D.; Romano, S.; Panvino,
F.; Maggi, S.; Altomonte, B.; Casini, M. P.; Ferrara, M.; and
Terrinoni, A. 2024. Scrolling through adolescence: A sys-
tematic review of the impact of TikTok on adolescent mental
health. European Child & Adolescent Psychiatry, 1–17.
Craig, C. M.; Brooks, M. E.; and Bichard, S. 2021. Proso-
cial consumer socialization: how socialization agents impact
prosocial attitudes and behavior. Atlantic Journal of Com-
munication, 29(3): 136–150.
Daniel, E.; Arieli, S.; and Akerman, L. 2024. The values of
schools: an analysis of vision statements. European Journal
of Psychology of Education, 39: 3661–3683.

--- Page 9 ---

Daniel, E.; and Benish-Weisman, M. 2019. Value develop-
ment during adolescence: Dimensions of change and stabil-
ity. Journal of Personality, 87: 620–632.
Daniel, E.; Misgav, K.; and Chomsky, A. 2024.
Middle
childhood development in personal values. Journal of Per-
sonality, 92: 1283–1298.
Daniel, E.; Schiefer, D.; M¨ollering, A.; Benish-Weisman,
M.; Boehnke, K.; and Knafo, A. 2012. Value differentia-
tion in adolescence: The role of age and cultural complexity.
Child Development, 83: 322–336.
De Veirman, M.; Hudders, L.; and Nelson, M. R. 2019. What
is influencer marketing and how does it target children? A
review and direction for future research. Frontiers in psy-
chology, 10: 498106.
Demetriou, A. M.; Kim, J.; Manolios, S.; and Liem, C. 2024.
Towards Estimating Personal Values in Song Lyrics. arXiv
preprint arXiv:2408.12694.
Devlin, J. 2018.
Bert: Pre-training of deep bidirectional
transformers for language understanding.
arXiv preprint
arXiv:1810.04805.
Dorey, E.; and McCool, J. 2009. The role of the media in
influencing children’s nutritional perceptions.
Qualitative
Health Research, 19(5): 645–654.
Duffett, R. G. 2017.
Influence of social media market-
ing communications on young consumers’ attitudes. Young
Consumers, 18(1): 19–39.
Fischer, R.; Karl, J.; Fetvadjiev, V.; Grener, A.; and Luczak-
Roesch, M. 2022. Opportunities and challenges of extracting
values in autobiographical narratives. Frontiers in Psychol-
ogy, 13: 886455.
Google. 2024.
Gemini 1.5: Unlocking multimodal
understanding
across
millions
of
tokens
of
context.
arXiv:2403.05530.
Grusec, J. E. 2011. Socialization processes in the family:
Social and emotional development. Annual Review of Psy-
chology, 62: 243–269.
Gwet, K. L. 2008. Computing inter-rater reliability and its
variance in the presence of high agreement. British Journal
of Mathematical and Statistical Psychology, 61(1): 29–48.
Hallinan, B.; Kim, B.; Mizoroki, S.; Scharlach, R.; Trill`o, T.;
Thelwall, M.; Segev, E.; and Shifman, L. 2023. The value
(s) of social media rituals: A cross-cultural analysis of New
Year’s resolutions. Information, Communication & Society,
26(4): 764–785.
He, P.; Gao, J.; and Chen, W. 2023. DeBERTaV3: Improv-
ing DeBERTa using ELECTRA-Style Pre-Training with
Gradient-Disentangled Embedding Sharing. In The Eleventh
International Conference on Learning Representations.
Himelboim, I.; and Golan, G. J. 2023.
A social network
approach to social media influencers on Instagram: The
strength of being a nano-influencer in cause communities.
Journal of Interactive Advertising, 23(1): 1–13.
Hu, E. J.; Shen, Y.; Wallis, P.; Allen-Zhu, Z.; Li, Y.; Wang,
S.; Wang, L.; and Chen, W. 2021. Lora: Low-rank adaptation
of large language models. arXiv preprint arXiv:2106.09685.
Jiang, A. Q.; Sablayrolles, A.; Mensch, A.; Bamford, C.;
Chaplot, D. S.; Casas, D. d. l.; Bressand, F.; Lengyel, G.;
Lample, G.; Saulnier, L.; et al. 2023. Mistral 7B. arXiv
preprint arXiv:2310.06825.
Kadi´c-Maglajli´c, S.; Lages, C. R.; and Pantano, E. 2024. No
time to lie: Examining the identity of pro-vaccination and
anti-vaccination supporters through user-generated content.
Social Science & Medicine, 347: 116721.
Ki, C.-W. C.; Cuevas, L. M.; Chong, S. M.; and Lim, H.
2020. Influencer marketing: Social media influencers as hu-
man brands attaching to followers and yielding positive mar-
keting results by fulfilling needs. Journal of Retailing and
Consumer Services, 55: 102133.
Kiesel, J.; Alshomary, M.; Handke, N.; Cai, X.; Wachsmuth,
H.; and Stein, B. 2022. Identifying the human values behind
arguments. In Proceedings of the 60th Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long
Papers), 4459–4471.
Kiesel, J.; C¸ ¨oltekin, C¸ .; Heinrich, M.; Fr¨obe, M.; Al-
shomary, M.; De Longueville, B.; Erjavec, T.; Handke, N.;
Kopp, M.; Ljubeˇsi´c, N.; Meden, K.; Mirzhakhmedova, N.;
Morkeviˇcius, V.; Reitis-M¨unstermann, T.; Scharfbillig, M.;
Stefanovitch, N.; Wachsmuth, H.; Potthast, M.; and Stein, B.
2024a. Overview of Touch´e 2024: Argumentation Systems.
308–332.
Kiesel, J.; C¸ ¨oltekin, C¸ .; Heinrich, M.; Fr¨obe, M.; Alshomary,
M.; De Longueville, B.; Erjavec, T.; Handke, N.; Kopp, M.;
Ljubeˇsi´c, N.; et al. 2024b. Overview of Touch´e 2024: Argu-
mentation Systems.
Knafo-Noam, A.; Barni, D.; and Schwartz, S. H. 2020. Par-
ent–child value similarity: Broadening from intergenera-
tional transmission to reciprocal influences, genetics, and
environmental antecedents, 163–185.
Oxford University
Press. ISBN 9780190676049.
Knafo-Noam, A.; Daniel, E.; and Benish-Weisman, M.
2023. The development of values in middle childhood: Five
maturation criteria. Current Directions in Psychological Sci-
ence.
Kojima, T.; Gu, S. S.; Reid, M.; Matsuo, Y.; and Iwasawa,
Y. 2022.
Large language models are zero-shot reason-
ers. Advances in neural information processing systems, 35:
22199–22213.
Kumar, A.; Raghunathan, A.; Jones, R. M.; Ma, T.; and
Liang, P. 2022.
Fine-Tuning can Distort Pretrained Fea-
tures and Underperform Out-of-Distribution.
In Interna-
tional Conference on Learning Representations.
Kumar, U.; Reganti, A. N.; Maheshwari, T.; Chakroborty, T.;
Gamb¨ack, B.; and Das, A. 2018. Inducing Personalities and
Values from Language Use in Social Network Communities.
Information Systems Frontiers, 20(6): 1219–1240.
Legkas, S.; Christodoulou, C.; Zidianakis, M.; Koutrintzes,
D.; Petasis, G.; and Dagioglou, M. 2024.
Hierocles of
alexandria at touch´e: multi-task & multi-head custom archi-
tecture with transformer-based models for human value de-
tection. In Working Notes of the Conference and Labs of the
Evaluation Forum (CLEF 2024). CEUR Workshop Proceed-
ings, CEUR-WS. org.

--- Page 10 ---

Lipshits-Braziler, Y.; Arieli, S.; and Daniel, E. 2024. Per-
sonal values and career-related preferences among young
adults. Journal of Personality.
Liu, Y. 2019. Roberta: A robustly optimized bert pretraining
approach. arXiv preprint arXiv:1907.11692, 364.
Lou, C.; and Yuan, S. 2019. Influencer marketing: How mes-
sage value and credibility affect consumer trust of branded
content on social media. Journal of interactive advertising,
19(1): 58–73.
Montag, C.; Yang, H.; and Elhai, J. D. 2021. On the psychol-
ogy of TikTok use: A first glimpse from empirical findings.
Frontiers in public health, 9: 641673.
OpenAI. 2024. GPT-4 Technical Report. arXiv:2303.08774.
Oulahbib, I.; Benhaddi, M.; and El Hadaj, S. 2024. Mea-
suring Personal Values Of African Reddit Users Using a
Lexicon-Based Approach. In International Conference On
Big Data and Internet of Things, 308–322. Springer.
Pennebaker, J. W.; Boyd, R. L.; Jordan, K.; and Blackburn,
K. 2015. The development and psychometric properties of
LIWC2015.
Ponizovskiy, V.; Ardag, M.; Grigoryan, L.; Boyd, R.; Dobe-
wall, H.; and Holtz, P. 2020. Development and validation
of the personal values dictionary: A theory–driven tool for
investigating references to basic human values in text. Eu-
ropean Journal of Personality, 34(5): 885–902.
Prot, S.; Anderson, C. A.; Gentile, D. A.; Warburton, W.;
Saleem, M.; Groves, C. L.; and Brown, S. C. 2015. Media as
agents of socialization. Handbook of socialization: Theory
and research, 276–300.
Qiu, L.; Zhao, Y.; Li, J.; Lu, P.; Peng, B.; Gao, J.; and Zhu,
S.-C. 2022. Valuenet: A new dataset for human value driven
dialogue system. In Proceedings of the AAAI Conference on
Artificial Intelligence, volume 36, 11183–11191.
Radford, A.; Wu, J.; Child, R.; Luan, D.; Amodei, D.;
Sutskever, I.; et al. 2019. Language models are unsupervised
multitask learners. OpenAI Blog.
Ragelien˙e, T.; and Grønhøj, A. 2021. The role of peers, sib-
lings and social media for children’s healthy eating social-
ization: a mixed methods study. Food Quality and Prefer-
ence, 93: 104255.
Reinikainen, H.; Munnukka, J.; Maity, D.; and Luoma-Aho,
V. 2020. ‘You really are a great big sister’–parasocial rela-
tionships, credibility, and the moderating role of audience
comments in influencer marketing.
Journal of marketing
management, 36(3-4): 279–298.
Rejeb, A.; Rejeb, K.; Appolloni, A.; Treiblmaier, H.; and
Iranmanesh, M. 2024. Mapping the scholarly landscape of
TikTok (Douyin): a bibliometric exploration of research top-
ics and trends. Digital Business, 100075.
Sagiv, L.; and Roccas, S. 2017. What personal values are
and what they are not: Taking a cross-cultural perspective.
ISBN 9783319563527.
Sagiv, L.; and Roccas, S. 2021. How do values affect behav-
ior? Let me count the ways. Personality and Social Psychol-
ogy Review, 25: 295–316.
Sagiv, L.; and Schwartz, S. H. 2022. Personal values across
cultures. Annual Review of Psychology, 73: 517–546.
Saji, B. S.; Vij, M.; and Kabiraj, S. 2015.
Selection of
tourism destination as a representation of human values.
Business Perspectives and Research, 3: 95–108.
Sch¨onpflug, U. 2001. Intergenerational transmission of val-
ues: The role of transmission belts. Journal of cross-cultural
psychology, 32(2): 174–185.
Schroter, D.; Dementieva, D.; and Groh, G. 2023. Adam-
smith at SemEval-2023 task 4: Discovering human values
in arguments with ensembles of transformer-based models.
arXiv preprint arXiv:2305.08625.
Schwartz, S. H. 1992. Universals in the content and struc-
ture of values: Theoretical advances and empirical tests in
20 countries. Advances in Experimental Social Psychology,
25: 1–65.
Schwartz, S. H. 2012. An overview of the Schwartz theory
of basic values. Online readings in Psychology and Culture,
2(1): 11.
Shifman, L. 2019. Internet memes and the twofold artic-
ulation of values. Society and the internet: How networks
of information and communication are changing our lives,
43–57.
Shifman, L.; Trill`o, T.; Hallinan, B.; Mizoroki, S.; Green, A.;
Scharlach, R.; and Frosh, P. 2025. The expression of values
on social media: An analytical framework. New Media &
Society, 14614448241307035.
Silva, A.; Lo, P.-C.; and Lim, E.-P. 2020.
On Predicting
Personal Values of Social Media Users using Community-
Specific Language Features and Personal Value Correlation.
Smahel, D.; Machacrova, H.; Mascheroni, G.; Dedkova, L.;
Staksrud, E.; Olafsson, K.; Livingstone, S.; and Hasebrink,
U. 2020. EU Kids Online: Survery results from 19 coutries.
Tafesse, W.; and Wood, B. P. 2021. Followers’ engagement
with instagram influencers: The role of influencers’ content
and engagement strategy. Journal of retailing and consumer
services, 58: 102303.
Teather, D. 2024. TikTokAPI.
Tolbert, A. N.; and Drogos, K. L. 2019. Tweens’ wishful
identification and parasocial relationships with youtubers.
Frontiers in Psychology, 10: 2781.
Tome, J.; and Cardita, S. 2021.
In 2021, the Internet
went for TikTok, space and beyond. https://blog.cloudflare.
com/popular-domains-year-in-review-2021/, Last accessed
on 2025-1-13.
Trill`o, T.; Scharlach, R.; Hallinan, B.; Kim, B.; Mizoroki,
S.; Frosh, P.; and Shifman, L. 2021. What does# freedom
look like? Instagram and the visual imagination of values.
Journal of Communication, 71(6): 875–897.
Tuominen, J.; Rantala, E.; Reinikainen, H.; and Wilska, T.-
A. 2023. Modern-day socialization agents: The connection
between social media influencers, materialism, and purchase
intentions of Finnish young people. The Journal of Social
Media in Society, 12(1).

--- Page 11 ---

Twito, L.; and Knafo-Noam, A. 2020. Beyond culture and
the family: Evidence from twin studies on the genetic and
environmental contribution to values.
Twito-Weingarten, L.; and Knafo-Noam, A. 2022. The de-
velopment of values and their relation to morality. Rout-
ledge, 3rd edition.
Uhls, Y. T.; and Greenfield, P. M. 2011. The rise of fame:
An historical content analysis. Cyberpsychology: Journal of
Psychosocial Research on Cyberspace, 5(1): 1.
van der Meer, M.; Vossen, P.; Jonker, C.; and Murukanna-
iah, P. 2023. Do Differences in Values Influence Disagree-
ments in Online Discussions? In Bouamor, H.; Pino, J.; and
Bali, K., eds., Proceedings of the 2023 Conference on Em-
pirical Methods in Natural Language Processing, 15986–
16008. Singapore: Association for Computational Linguis-
tics.
Wilde, O. 1890. The picture of dorian gray. Oxford Univer-
sity Press.
Wongpakaran, N.; Wongpakaran, T.; Wedding, D.; and
Gwet, K. L. 2013. A comparison of Cohen’s Kappa and
Gwet’s AC1 when calculating inter-rater reliability coeffi-
cients: a study conducted with personality disorder samples.
BMC medical research methodology, 13: 1–7.
Woodward,
M.
2024.
TIKTOK
USER
STATIS-
TICS 2025:EVERYTHING YOU NEED TO KNOW.
https://www.searchlogistics.com/learn/statistics/tiktok-
user-statistics/, Last accessed on 2025-1-13.
Yao, J.; Yi, X.; Gong, Y.; Wang, X.; and Xie, X. 2024. Value
FULCRA: Mapping Large Language Models to the Multi-
dimensional Spectrum of Basic Human Value. In Duh, K.;
Gomez, H.; and Bethard, S., eds., Proceedings of the 2024
Conference of the North American Chapter of the Associa-
tion for Computational Linguistics: Human Language Tech-
nologies (Volume 1: Long Papers), 8762–8785. Mexico City,
Mexico: Association for Computational Linguistics.
Zaken, E. B.; Goldberg, Y.; and Ravfogel, S. 2022.
Bit-
Fit: Simple Parameter-efficient Fine-tuning for Transformer-
based Masked Language-models. In Proceedings of the 60th
Annual Meeting of the Association for Computational Lin-
guistics (Volume 2: Short Papers), 1–9.
Ziems, C.; Held, W.; Shaikh, O.; Chen, J.; Zhang, Z.; and
Yang, D. 2024.
Can Large Language Models Transform
Computational Social Science? Computational Linguistics,
50(1): 237–291.
Paper Checklist to be included in your paper
1. For most authors...
(a) Would answering this research question advance sci-
ence without violating social contracts, such as violat-
ing privacy norms, perpetuating unfair profiling, exac-
erbating the socio-economic divide, or implying disre-
spect to societies or cultures? Yes
(b) Do your main claims in the abstract and introduction
accurately reflect the paper’s contributions and scope?
Yes
(c) Do you clarify how the proposed methodological ap-
proach is appropriate for the claims made? Yes
(d) Do you clarify what are possible artifacts in the data
used, given population-specific distributions? Yes
(e) Did you describe the limitations of your work? Yes
(f) Did you discuss any potential negative societal im-
pacts of your work? Yes
(g) Did you discuss any potential misuse of your work?
Yes
(h) Did you describe steps taken to prevent or mitigate po-
tential negative outcomes of the research, such as data
and model documentation, data anonymization, re-
sponsible release, access control, and the reproducibil-
ity of findings? Yes
(i) Have you read the ethics review guidelines and en-
sured that your paper conforms to them? Yes
2. Additionally, if your study involves hypotheses testing...
(a) Did you clearly state the assumptions underlying all
theoretical results? NA
(b) Have you provided justifications for all theoretical re-
sults? NA
(c) Did you discuss competing hypotheses or theories that
might challenge or complement your theoretical re-
sults? NA
(d) Have you considered alternative mechanisms or expla-
nations that might account for the same outcomes ob-
served in your study? NA
(e) Did you address potential biases or limitations in your
theoretical framework? Yes
(f) Have you related your theoretical results to the existing
literature in social science? Yes
(g) Did you discuss the implications of your theoretical
results for policy, practice, or further research in the
social science domain? Yes
3. Additionally, if you are including theoretical proofs...
(a) Did you state the full set of assumptions of all theoret-
ical results? NA
(b) Did you include complete proofs of all theoretical re-
sults? NA
4. Additionally, if you ran machine learning experiments...
(a) Did you include the code, data, and instructions
needed to reproduce the main experimental results (ei-
ther in the supplemental material or as a URL)? Yes
(b) Did you specify all the training details (e.g., data splits,
hyperparameters, how they were chosen)? Yes
(c) Did you report error bars (e.g., with respect to the ran-
dom seed after running experiments multiple times)?
No
(d) Did you include the total amount of compute and the
type of resources used (e.g., type of GPUs, internal
cluster, or cloud provider)? No
(e) Do you justify how the proposed evaluation is suffi-
cient and appropriate to the claims made? Yes

--- Page 12 ---

(f) Do you discuss what is “the cost“ of misclassification
and fault (in)tolerance? No
5. Additionally, if you are using existing assets (e.g., code,
data, models) or curating/releasing new assets, without
compromising anonymity...
(a) If your work uses existing assets, did you cite the cre-
ators? Yes
(b) Did you mention the license of the assets? NA
(c) Did you include any new assets in the supplemental
material or as a URL? No
(d) Did you discuss whether and how consent was ob-
tained from people whose data you’re using/curating?
Yes
(e) Did you discuss whether the data you are using/cu-
rating contains personally identifiable information or
offensive content? Yes
(f) If you are curating or releasing new datasets, did you
discuss how you intend to make your datasets FAIR
(see ?)? Yes
(g) If you are curating or releasing new datasets, did you
create a Datasheet for the Dataset (see ?)? Yes
6. Additionally, if you used crowdsourcing or conducted
research with human subjects, without compromising
anonymity...
(a) Did you include the full text of instructions given to
participants and screenshots? Yes
(b) Did you describe any potential participant risks, with
mentions of Institutional Review Board (IRB) ap-
provals? Yes
(c) Did you include the estimated hourly wage paid to
participants and the total amount spent on participant
compensation? NA
(d) Did you discuss how data is stored, shared, and dei-
dentified? NA
A
Prompts and Responses
In this appendix we provide the prompts used for value ex-
traction (direct and 2-step extraction) and the prompt used in
converting a movie to textual script, along with an example
of a generated script and a the values extracted from it.
A.1
Prompt for Value Extraction
The prompt used for direct extraction is provided at Figures
5 and 6. This very same “prompt” served as the annotation
guidelines (code book) offered to annotators. Note that the
figure contains an examples (“few shot”) for only one value
(SELF-DIRECTION-THOUGHT) while the actual prompt
(and the annotation guidelines) provided examples for each
of the values. The same prompt was used for few-shot ex-
traction from scripts in the 2-step extraction, the sole dif-
ference is that the opening line is “You are given a movie
script of a TikTok video”, rather than “You are given a Tik-
Tok video”. The full code book (prompt) is available at [add
URL].
A.2
Prompt for Srtipt Extraction
The prompt used to convert TikTok movies to textual scripts
is available in Figure 7; the script generated by applying this
prompt on TikTok ID 7341895431883967746 is presented
in Table 2. The manual annotations for this specific movie
are: Achievement- present (1), Face - conflict (-1).

--- Page 13 ---

Figure 5: Annotation guidelines and prompt for direct extraction.

--- Page 14 ---

Figure 6: Additional guidelines, appended after all the examples (code book).

--- Page 15 ---

Figure 7: The prompt used to convert TikTok movies to textual scripts.

```
