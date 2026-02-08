---
title: "Examining the Role of Relationship Alignment in - PDF Extract"
source_pdf: "2024-Altenburger-Examining the Role of Relationship Alignment in.pdf"
pages: 15
extracted_at: "2026-01-24T17:05:26.559958"
---

# PDF Extract: Examining the Role of Relationship Alignment in

**Source PDF:** 2024-Altenburger-Examining the Role of Relationship Alignment in.pdf
**Total Pages:** 15

---

## Content

```
--- Page 1 ---

Examining the Role of Relationship Alignment in Large Language Models
Kristen M. Altenburger∗1, Hongda Jiang*1, Robert E. Kraut2, Yi-Chia Wang3, Jane Dwivedi-Yu 1
1 Meta
2 Carnegie Mellon University
3 Stanford University
Abstract
The rapid development and deployment of Generative AI in
social settings raise important questions about how to op-
timally personalize them for users while maintaining accu-
racy and realism. Based on a Facebook public post-comment
dataset, this study evaluates the ability of Llama 3.0 (70B)
to predict the semantic tones across different combinations
of a commenter’s and poster’s gender, age, and friendship
closeness and to replicate these differences in LLM-generated
comments.
The study consists of two parts: Part I assesses differences
in semantic tones across social relationship categories, and
Part II examines the similarity between comments generated
by Llama 3.0 (70B) and human comments from Part I given
public Facebook posts as input. Part I results show that in-
cluding social relationship information improves the ability
of a model to predict the semantic tone of human comments.
However, Part II results show that even without including so-
cial context information in the prompt, LLM-generated com-
ments and human comments are equally sensitive to social
context, suggesting that LLMs can comprehend semantics
from the original post alone. When we include all social re-
lationship information in the prompt, the similarity between
human comments and LLM-generated comments decreases.
This inconsistency may occur because LLMs did not include
social context information as part of their training data. To-
gether these results demonstrate the ability of LLMs to com-
prehend semantics from the original post and respond sim-
ilarly to human comments, but also highlights their limita-
tions in generalizing personalized comments through prompt-
ing alone.
Introduction
Over the past few years, large language models (LLMs)
(Brown 2020; Touvron et al. 2023; Zhao et al. 2023) have
shown remarkable capabilities across various NLP tasks
and enabled applications that were once thought unfeasible
(Chang et al. 2024). In particular, many of these applications
consider LLMs as conversational agents to interact with hu-
mans. However, LLMs are trained to memorize vast corpora
in social isolation (Krishna et al. 2022) with the goal to pre-
dict the next token given the input context but not to con-
verse with humans (Brown 2020). Therefore, despite their
*Equal contributions.
extraordinary ability to produce content mimicking human-
generated content, it does not follow that LLMs incorporate
social capabilities and can respond to humans in a way that
conforms to social expectations. In fact, researchers have
discovered LLMs can exhibit abnormal behaviors and gen-
erate improper responses, including but not limited to bias,
stereotypes, toxicity, misinformation, or hallucination (Wei-
dinger et al. 2021).
To address these problems, there is an emerging research
field that studies whether and to what extent LLMs can
mimic human behaviors and aims to align LLMs with user
expectations (Shen et al. 2023). For example, some scholars
focus on evaluating and improving LLM safety (Anwar et al.
2024; Ge et al. 2023) and the alignment with human values
(Hendrycks et al. 2020), such as social norms and morality
(Ziems et al. 2023; Xu et al. 2023). Others examine the opin-
ions reflected by LLMs and explore techniques to align the
opinions they produce with those of different demographic
populations (Bakker et al. 2022; Santurkar et al. 2023; Dur-
mus et al. 2023). Moreover, for LLMs to exhibit consistent
behaviors in dialogue-based interactions, prior work has in-
vestigated approaches to personalize LLMs by conditioning
their responses on a certain persona, i.e., personality or pro-
file information (Tseng et al. 2024; Caron and Srivastava
2022; Serapio-Garc´ıa et al. 2023).
Despite recent efforts on LLM alignments for more
human-like behaviors, at least one significant research gap
remains – aligning LLM-generated content with social re-
lationships. There is an extensive social science literature
focusing on how social factors in relationships, such as age,
gender, and friendship tie strength, influence the language
people use with each other and its semantic tone (e.g., humor
and emotional support) (Wellman and Wortley 1990; Dindia
and Allen 1992; Shriver, Nair, and Hofstetter 2013; Zeng
and Wei 2013; Wang, Burke, and Kraut 2016; Hall 2017;
Greengross, Silvia, and Nusbaum 2020). Thus, for LLMs
to successfully produce responses that mimic human-human
communication, it is important to incorporate social rela-
tionship information as context. However, existing research
has not delved into the impact of social relationships on
LLM-generated content or how to condition LLM-generated
content on the relationship between communication part-
ners. This paper aims to bridge the gap by proposing the
first in-depth exploration of the role of social relationships
arXiv:2410.01708v1  [cs.CL]  2 Oct 2024

--- Page 2 ---

in human-LLM dyadic interactions. We address one central
question: to what extent one can steer LLMs with social re-
lationship information so their responses are aligned with
the content produced by human-human communication?
To answer the research question, we conduct two stud-
ies. We start with analyzing real-world public human-human
communication data on Facebook and then examine whether
LLMs can generate similar content when prompted with
social relationship information. Specifically, Study 1 repli-
cates and extends prior research by examining the rela-
tionship between social context variables (age, gender, and
friendship strength) and the semantic tone of public post-
comment exchanges between people on Facebook. This em-
pirical research demonstrates that these social factors influ-
ence not only the exchange of emotional support, humor,
self-disclosure, and toxic comments, which have been ex-
amined in prior research (Wellman and Wortley 1990; Din-
dia and Allen 1992; Wang, Burke, and Kraut 2016; Burke
et al. 2007; Xu, Liu, and Liu 2024; Hall 2017), but also un-
derstudied semantic tones, like surprise, worry, anxiety, and
thankfulness. Study 2 examines whether incorporating so-
cial relationship information in the prompt can steer LLM
comments to more align with human ones and better reflect
the associations between semantic tone and social relation-
ship variables in human comments as reported in the first
study. Results suggest that LLM-generated comments are
quite similar to human-generated ones to the same post, but
that explicitly referring to social context to tune the LLMs
does not increase their similarity to human comments.
Literature Review and Hypothesis
Persona Alignment
There has been extensive work in studying and improving
the ability of large language models to act in accordance
with human intentions, values, and ethical principles, termed
alignment in language models. Persona alignment, which in-
volves tailoring the behavior and responses of AI systems to
match specific personas, has become a growing area of inter-
est in the development of conversational AI. Several studies
have investigated the capability of language models to im-
itate personas through fine-tuning based on their personal
attributes like age, occupation, and interests (Zhang 2018;
Li et al. 2016; Shao et al. 2023; Lee, Oh, and Lee 2023) and
have shown practical improvements when conversing with
chatbots when incorporating these personal attributes into
their prompts, such as increases in user engagement with
them (Shuster et al. 2022) or a greater capacity for them to
produce empathetic responses (Zhong et al. 2020). As LLMs
have become more powerful, prompting has become a fea-
sible and cost-effective way of aligning responses, and stud-
ies that evaluate persona alignment of recent state-of-the-art
language models find high fidelity across multiple persona
types in the context of fictitious personas (Wang et al. 2024;
Serapio-Garc´ıa et al. 2023; Caron and Srivastava 2023; Zhou
et al. 2023; Olea et al. 2024; Njifenjou et al. 2024).
Audience Alignment
While persona alignment focuses on the capacity of the
LLM to emulate a given persona, more recently, researchers
have attempted to craft LLMs that are aligned with charac-
teristics of the recipient of messages (i.e., audience align-
ment), not just the producer. For example, in a series of ex-
periments Matz et al. (2024) showed that messages crafted
by ChatGPT-3 that were tailored to the personality of the re-
cipient were significantly more influential than non-tailored
messages. Choi et al. (2024) built and tested Proxona, which
helps content creators match content to a target audience by
using the history of audience comments as the basis for cre-
ating audience-member personas (e.g., a practical urban gar-
dener).
Relationship Alignment
Our research attempts to extend the notions of persona and
audience alignment and introduce relationship alignment, in
which characteristics of the speaker and audience are con-
sidered simultaneously. The relationship between commu-
nication partners could include a match or mismatch in de-
mographic characteristics (e.g., talking to someone of the
same or different gender or age) or the nature of the tie
strength between them (e.g., strangers versus friends). Given
the promising results from prior work in persona and audi-
ence alignment, we expect that including social relationship
information, such as the demographic information and the
relationship between two users, is likely to improve the sim-
ilarity of LLM-generated comments to human comments.
Hypothesis: Including social relationship information
in its prompt will produce LLM-generated comments
that are more similar to human ones.
Methodological Advances
This work makes two contri-
butions. First, the prior work on persona and audience align-
ment shows that social context information improves LLM-
generated content at the group level (e.g., language that
sounds more like a woman or is more convincing to ex-
troverts). We are the first to look at the influence of social
context information at the individual level (i.e., the simi-
larity between a single human comment and its matched
LLM-generated comment). Second, while the LLM align-
ment literature usually evaluates model output against user
surveys, we compare LLM-generated content against real
human data.
Operationalization of Social Relationship
There is an
extensive literature focusing on how social context influ-
ences people’s language, specifically its semantic tones. For
example, close friends and family members use more in-
timate and supportive language with each other than do
weak ties (Wang, Burke, and Kraut 2016); acquaintances
are more helpful for idea generation than strong ties (Burt
2004). Dindia and Allen (1992) found women self-disclose
more than men when talking to friends but not when talk-
ing to strangers. Wellman and Wortley (1990) found that
women provide more emotional support than men and the
exchange of support increases with tie strength. Greengross,

--- Page 3 ---

Silvia, and Nusbaum (2020) found that given the same stim-
ulus, men produce funnier comments than women. Hall
(2017) found that romantic partners with more satisfying re-
lationships exchanged more positive humor while those with
lower satisfaction exchanged more negative humor. Based
on the prior work, we decide to focus on three types of social
relationship between the Facebook poster and commenter,
age-age, gender-gender, and tie strength, and examine their
influence on LLM-generated content.
Data Setup
We analyze public conversations on Facebook Feed where
users can make posts and share content with others1. When
a user, referred to as the “poster,” shares public content on
Feed, any Facebook user can respond to the post by leav-
ing a public comment, which can be seen by all users. This
two-way interaction between the poster and the commenter
represents a conversation. More than one commenter can re-
spond to a post, which we will account for in this analysis.
To protect user privacy, we de-identified all user informa-
tion and removed personal data such as names and phone
numbers from the text before applying a comment semantic
classifier and a LLM for comment generation. This ensured
that no sensitive information was included in the analysis.
Comment and Posts on Feed: Our empirical dataset
comprises approximately 665k public Facebook (FB) posts
and comments created on May 25, 2024 by active U.S. FB
users at least 18 years old. For reasons of privacy, we re-
strict the sample to English posts on News Feed that any
user can comment upon. We exclude from the analysis ads,
group posts, and reshared posts. Because Feed Ranking can
influence the types of posts a user views and the types of
conversations they participate in, we control for the likeli-
hood of a user to comment on a given post in this analysis.
Social Context: We evaluate the following social con-
texts: stated gender, stated age, and friendship closeness
between the commenter and poster. Stated gender and age
means we rely on user-provided data. Because our data can-
not distinguish users who provide no gender information
from those who identify as non-binary, we exclude these two
groups from the analysis and include only users who stated
their gender as male or female. For the analysis, we scale
commenter/poster age to have mean 0 and standard devia-
tion 1. We include interaction terms between commenter’s
gender and poster’s gender and interaction terms between
commenter’s age and poster’s age. This allows for the effect
of a commenter’s gender or age to vary depending on the
poster’s gender or age. We encode commenter/poster gender
as female or male and include interaction terms (i.e., women
talking to a male poster and vice versa). Finally, we account
for the relationship between two pairs of individuals. We en-
code users as strangers or friends. Among friends, we code
two users as close friends or non-close friends. Friendship
closeness is a model-based score that predicts relationship
closeness between two individuals (Burke and Kraut 2014).
We treat friendship as a categorical feature, where we code
whether two users are close friends (1), non-close friends
1https://transparency.meta.com/features/ranking-and-content/
Gender
Female Commenter Female Poster
50%
Male Commenter Male Poster
20%
Male Commenter Female Poster
10%
Female Commenter Male Poster
20%
Age
Avg. Commenter Age
50
Avg. Poster Age
50
Friendship
Close Friends
45%
Friends
45%
Stranger
10%
Table 1: Descriptive statistics for the social context features
in our sample of Facebook posters and comments.We intro-
duce random noise to the social context signals. For gender,
we introduce Gaussian noise with mean 0 and standard de-
viation of 1. For friendship and gender, we inject noise by
randomly changing the value of the feature for 10% of ob-
servations. We then round to the nearest 10 for gender and
age, and to the nearest 5 for friendship.
(2), or strangers (3). This coding allows for non-linear rela-
tionships between friendship closeness and semantic tones.
Table 1 presents the descriptive statistics for the social con-
text variables used in the regression models predicting se-
mantic tone.
Generated Comments: We randomly selected 10,000
post and comment pairs from the empirical dataset. We then
prompted Llama 3.0 (70B) to generate comments for each
post under three conditions: without social context informa-
tion, with a subset of social context information, and with
all social context information included in the prompt. The
prompts are detailed in the Appendix “LLM prompt” sec-
tion. Figure 1 provides examples of the prompts and cor-
responding generated comments. We also tested different
prompt techniques such as chain-of-thoughts (Kojima et al.
2022), which did not change our main conclusion (see “Part
II: Prompt engineering” section in Appendix).
Semantic Tone of Comments: We rely on a semantic
tone classifier to label comments across different seman-
tic categories. This model relies on crowd-sourced labeled
training data. We limit our analysis to eight semantic tones–
Surprised, Funny, Insult, Provide Emotional Support, Self-
Disclosure, Worried, Thankful, Relaxed. Definitions and ex-
amples are listed in Appendix Figure 5. We selected these
because they are likely to change the emotional state of
the person being responded to, either because they them-
selves reflect the emotional content of the comment (e.g.,
surprised, relaxed) or contain an action that is likely to af-
fect the poster’s emotional state (e.g., insult or provide emo-
tional support). They reflect a diversity of the semantic tones
that are common in Facebook exchanges. We dropped tones
if they were highly correlated with another one (e.g., we
included Provide Emotional Support, but dropped Provide
Informational Support because they were highly negatively
correlated r = −.80). We use the text-only version of the
model, which only takes text as input and handles process-
ing such as removing user mentions in the comment. We ap-
ply this model to comment text and generate semantic tone
scores across the eight categories described above. Through-

--- Page 4 ---

Post
I’m glad I finally asked her, and 
she said yes!
[PERSON] and I got engaged.
Human comment
Congratulations to  [PERSON] 
and [PERSON]! - you don’t 
know me personally, but your 
aunt [PERSON] is my best 
friend and your dad was my 
son’s favorite football coach. 
Wish you both all the best !!!
🎉
Prompt without social context
You are a Facebook user and want to comment 
on a post from another Facebook user (the 
poster) in the most proper way based on the 
social relationship between you and the poster. 
Here is the post made by the poster on 
Facebook: 
[Post]: I’m glad I finally asked her, and she said 
yes! [PERSON] and I got engaged.
Generate a short comment right below the post, 
with "[Comment]:" prefixing the comment, in one 
paragraph. No explanation needed.
LLM comment
Huge congratulations to you both! So thrilled to 
hear the amazing news! Wishing you a lifetime 
of love, happiness, and adventure together!
Prompt with social context
You are a Facebook user and want to comment on a 
post from another Facebook user (the poster) in the 
most proper way based on the social relationship 
between you and the poster. Here is the post made by 
the poster on Facebook: 
[Post]: I’m glad I finally asked her, and she said yes! 
[PERSON] and I got engaged.
Remember that you and the poster are friends but not 
interact with each other much.
Also remember that you are a female of age 68 and the 
poster is a male of age 40. 
Generate a short comment right below the post, with 
"[Comment]:" prefixing the comment, in one paragraph. 
No explanation needed.
LLM comment
Oh, congratulations to you and your fiancée! I'm 
beyond thrilled to hear this wonderful news! Wishing 
you both a lifetime of love, happiness, and adventure 
together!
Figure 1: Example of LLM prompt without and with social context information, paraphrased human comment, and LLM
generated comments from prompts without and with social context information.
out this analysis, these scores will represent the outcome
variable.
Post Topic Classifications: We finally account for the
topic of the post in this analysis like whether a post is about
“Sports” or “Children & Parenting”. We rely on a topic
modeling-like approach for categorizing posts into 27 dif-
ferent high-level categorizations. We dropped two categories
that had a small number of comments.
Broader perspective and ethical
considerations.
An internal research board reviewed the study’s research
ethics and privacy practices prior to its start. In agreeing to
its terms of service, Facebook users allow the type of anal-
ysis done in this paper to better understand how people use
Meta products, to improve the products, and to promote their
safety, security, and integrity, including combating harmful
user conduct. To preserve users’ privacy, data consists of de-
identified comments collected only from public posts. When
writing up this paper, to preserve privacy we paraphrase ex-
amples so that they could not be found through an internet
search (Bruckman 2002).
Part I: How Comment Semantic Tones on
Facebook Varies Across Social Context
The first study aims to assess social relationships in the con-
text of Facebook comments and examines a diverse set of se-
mantic tones. This analysis determines the significance and
directionality of various social context variables in predict-
ing comment semantic tone. These will inform Part II, where
we investigate whether LLMs can similarly leverage social
context to better align its semantic tone with that of the hu-
man comment.
We fit a series of linear mixed effects regression mod-
els to predict the extent a comment expresses each seman-
tic tone (surprised, funny, insult, provide emotional sup-
port, self-disclosure, worried, thankful, and relaxed). We
log-transformed the comment semantic tones to deal with
long-tailed distributions, except for the “relaxed” tone where
the transformation was not needed. The predictors include
social relationship information between the poster and com-
menter (age, gender, and friendship strength) along with post
topic category. We allow random intercepts for post IDs. Fi-
nally, we applied an inverse propensity weighting (IPW) cor-
rection to account for differences in a particular user’s like-
lihood to comment on a particular post, which we refer to as
p(comment). For IPW, due to small probability weights, we
set a maximum IPW weight of 10.
Significance of Social Context Signals: We first eval-
uate whether incorporating social context information sig-
nificantly enhances the model’s performance compared to
a baseline model. We test social context features individu-
ally and together, which we compare to a baseline model
that includes post topics only. This comparison is done via
a likelihood ratio test. Appendix Table 4 shows that adding
social context signals compared to a baseline model leads to
a statistically significant improvement in model fit for all se-
mantic tones. In the Appendix Table 5, we also show that a
full model with all social context signals outperforms a base-
line model that includes just one social context signal. These
findings suggest that social context signals are valuable to
semantic prediction tasks. Based on these results, we antic-
ipate that LLM tasks for comment generation will benefit

--- Page 5 ---

Figure 2: Multi-level regression results from Part I predicting semantic tone outcomes from social context variables and post
topic (not shown). Post ID is included as a random effect, since multiple comments can be nested under a single post. The
conditional R2 represents the variation explained by both fixed and random effects, while marginal R2 represents the variation
explained by fixed effects only. *** p < 0.001.
from knowing the social context of the conversation, which
we’ll explore in Part II.
Interpretation of Social Context Signals: Figure 2, re-
ports the results of the regression analyses predicting seman-
tic tones from social relationship variables. Below we pro-
vide a brief interpretation of the results:
• Gender: Male commenters and posters are less likely to
create comments that are surprised, provide emotional
support, self-disclose or are thankful compared to female
commenters; male commenters and posters are more
likely to create comments that are funny, have insults, are
worried or relaxed. When interacting, male commenters
and male posters have comments that have more self-
disclosure, more worry, and more relaxedness.
• Age: Older commenters are less likely to create com-
ments that are surprised, funny, have insult, self-disclose,
contain worry, or are relaxed; they are more likely to
create comments that provide emotional support and
are thankful compared to younger commenters. Older
posters are less likely to receive comments that are funny,
have insult, worry, or are relaxed; they are more likely to
receive comments with surprise, emotional support, and
thankfulness. When interacting, older commenters and
older posters have comments that are more funny, more
insultive, more self-disclosure, more worry, and more re-
laxed.
• Friendship Type: Compared to close friends, strangers
are less likely to create comments that are surprised,
funny, have insults, self-disclose or are relaxed; strangers
are more likely to create comments with thankfulness.
Compared to close friends, non-close friends are less
likely to create comments that are funny, have insults,
provide emotional support or are relaxed; non-close
friends are more likely to create comments with surprise,
self-disclose, worry, or are thankful.
Many of these associations replicate results from the prior
literature (e.g., men provide less emotional support than
women). However, the associations are inconsistent with the
prior literature for some social characteristic/tone combina-
tions. Although not the focus of the current research, some
inconsistencies are worth exploring in follow-up research.
For example, people self-disclose less when commenting on
a close friend’s post than when responding to strangers. It is
possible that this inconsistency results from the public na-
ture of post and comment pairs used in the current study;
people may not want to reveal intimate personal informa-
tion even when responding to close friends because their re-
sponses are open to the world to see.
Figure 3: Mixed effect regressions predicting the log-
transformed sentiment scores of LLM generated comments
from the tone of human comments with and without social
context information. The dashed line indicates perfect pre-
diction, where the tone of generated comments is perfectly
predicted from the tone of human comments. The gray line
shows fitted results for LLM comments without social con-
text, and the blue line shows fitted results for LLM com-
ments with social context. The left panel with results for
the “insult score” shows that including social context in the
prompt slightly increased the similarity between the human
and generated comments. In contrast, the right panel with
results for the “self-disclosure score” shows that including
the context decreases the similarity.

--- Page 6 ---

Tone
Surprised
Funny
Insult
Emotional
support
Self
disclosure
Worried
Thankful
Inclusion
Average
no-context
0.309
0.518
0.436
0.312
0.425
0.585
0.382
0.465
0.429
all-context
0.325
0.529
0.456
0.284
0.360
0.543
0.373
0.431
0.413
difference ∆ˆβ
0.016∗
0.011
0.020 ∗∗∗
−0.028∗∗∗
−0.065∗∗∗
−0.042∗∗∗
−0.009
−0.034∗∗∗
−0.016
Table 2: Regression coefficients predicting the sentiment-scores of the LLM-generated comments from human-generated com-
ments when social context was (all-context) or was not (no-context) included in the prompt. The difference row represents the
fitting coefficients for human-comment × all-context interaction, ∆ˆβ. * p < 0.05, ** p < 0.01, *** p < 0.001
Part II: Does providing social context
information help to generate human-like
comments?
In the second part of the study, we evaluate LLM’s ability
to leverage social context information to generate human-
like comments. We employ two innovative approaches to as-
sess the similarity between the tone of human comments and
the tone of generated comments. Approach 1 is the individ-
ual comment-level analysis that directly compares the tone
of individual human comments and their matched LLM-
generated comments when social context was or was not
included in the LLM prompt. Approach 2 is an aggregate
analysis examining whether the relationship between social
context variables and the semantic tone of LLM-generated
comments more closely replicates the relationships shown in
Study 1 when social context was or was not included in the
LLM prompt. In the Appendix, we demonstrated the con-
nection and difference between those two approaches using
a simple mathematical model (see “Part II: Comparison be-
tween Approach 1 and Approach 2” section).
Approach 1: Individual-level comparisons
First, we employ a linear mixed effects regression model
to examine the relationship between the tones of generated
comments and those of human comments, while controlling
for the type of social context presented in the prompt. The
model specification is:
llm_sentiment_score
˜ human_sentiment_score + all_context
+ human_sentiment_score x all_context
The fitted coefficient for “human sentiment score” quan-
tifies how closely the tone of generated comments aligns
with the tone of human comments, thereby measuring the
similarity between the two. The predictor “all context”
is a binary factor indicating whether the generated com-
ment was produced with a no-context prompt (coded 0) or
an all-context prompt (coded 1). The interaction between
the “all context” variable and the “human sentiment score”
tests whether the similarity between the tone of the human
and generate comments changes when social context infor-
mation is added to the prompt,
∆ˆβ ≡ˆβhuman sentiment score×all context.
(1)
In Figure 3, this is represented as the difference in the slope
of the grey line reflecting the similarity between the human
and LLM comments for the no-context condition and slope
of the blue line for the all-context condition. In Table 2, we
report the fitting coefficients for all eight semantic tones.
As shown in Figure 3 and Table 2, when no context infor-
mation is included in the prompt, the tones of the generated
comments are moderately similar to the tone of the original
human comments, with the similarity coefficients ˆβ ranging
from .309 for surprised to .585 for worried (mean ˆβ=.429,
mean se = .0072, p<.001). Remember that when both the
independent and dependent variables in a regression are log
transformed, one interprets the coefficient as the percent in-
crease in the dependent variable for every 1% increase in the
independent variable. Thus these results indicate that on av-
erage across the eight semantic tones, when the tone of the
human comment increases by 1%, the tone of the generated
comment increases by .43%.
The human comment tone × all-context interaction tests
whether adding context information to the prompt changes
the similarity between the human comment and the LLM
generated one. Adding context information to the prompt
strengthens the similarity for surprised (∆ˆβ =.016) and in-
sult (∆ˆβ = .020), but reduces the similarity for four others
(providing emotional support ∆ˆβ = −.028; self-disclosure
∆ˆβ = −.065; worried ∆ˆβ = −.042; inclusion ∆ˆβ =
−.034) and had no reliable effect on funny (∆ˆβ = .011)
or thankful (∆ˆβ = −.009). Overall, the similarity between
the human and generated comments was marginally reduced
when the prompt includes the social context information
(difference = -.016, p<.10). This suggests that the majority
of the similarity between generated and human comments
can be attributed to the post text itself. In contrast, adding
social context has only a small and inconsistent impact on
the similarity with individual human comments.
Approach 2: Group-level comparison
While Approach 1 investigates whether providing social
context to the LLM enables it to generate comments that are
more similar to human comments to the same posts, here
in Approach 2 we address whether LLM can replicate the
dependency of comments on social context shown in Study
1. That is, we expanded Study 1 by applying linear mixed
effects models to predict the semantic tones of LLM- com-
ments generated in response to various prompts. We ana-
lyzed five different prompts: (1) a basic prompt with no so-
cial context (llm-no-context); (2) a prompt that includes the
ages of both the poster and the commenter (llm-age-only);
(3) a prompt that specifies the genders of the poster and

--- Page 7 ---

Figure 4: Regression coefficients of social context factors in the fitted models for log-transformed insult score (left panel)
and self-disclosure score (right) based on Approach 2. We compare human comments (red), generate comments when provided
social context (blue), and generated comments without provided social context (gray). The horizontal bar shows 95% confidence
interval. Plots for other semantic tones are shown in Figure 6 in the Appendix.
commenter (llm-gender-only); (4) a prompt that indicates
the friendship status, i.e.,“stranger”, “non-close friends”, or
“close friends” (llm-friendship-only); (5) a comprehensive
prompt that incorporates full context (llm-all-context). Each
model uses the social relationship variables shown in Ta-
ble 2,, but predicts the tones of the LLM-generated com-
ments rather than the tones of human comments.
As an illustration of the analysis and results, Figure
4 compares the fitted coefficients from models of log-
transformed insult scores and self-disclosure scores for hu-
man comments, LLM comments with full social context,
and LLM comments without social context. Plots for other
semantic sentiment scores can be found in Figure 6 in the
Appendix. We observe a consistent trend: while adding so-
cial context to prompts significantly alters the tone of gen-
erated comments, it also widens the disparity between the
regression coefficients of generated comments and those of
human comments. For instance, incorporating full context
into the prompt significantly alters the influence of gen-
der and friendship status on the self-disclosure score (p ≤
0.001). However, this adjustment does not make the asso-
ciation of gender and friendship with self-disclosure in the
generated comments more similar to their association in the
human comments. In fact, the strong association with friend-
ship status in the generated comments causes the model to
diverge further from the regression model used for human
comments. Among the 64 regression coefficients (8 social
context variables × 8 tone categories), introducing full con-
text in the prompt significantly altered 21 coefficients, mak-
ing the fitted coefficients for the LLM comments more sim-
ilar to those in the model for human comments in only four
of these cases, but less similar in 17 cases (p < 0.05, refer
to Appendix Table 7 for details).
To quantify the discrepancy between human and gener-
ated comments in terms of their association with social fac-
tors, we calculated the sum of absolute difference in regres-
sion coefficients across eight social variables. Explicitly,
ˆδ ≡
X
social factor
|ˆβsocial factor llm −ˆβsocial factor human| (2)
As shown in Table 3, comments generated by a no-context
prompt have the smallest average distance from human-
generated comments across the eight sentiment categories.
When social context information is explicitly mentioned in
the prompt, the discrepancy tends to increase. The discrep-
ancy is especially large when friendship is mentioned in the
prompt, suggesting that LLMs tend to over-interpret the im-
pact of friendship when generating comments. Adding gen-
der information increased the distance for half of the sen-
timent categories, but the change was smaller compared to
mentioning friendship strength. Providing only the poster’s
age and commenter’s age didn’t change the tone of gener-
ated comments significantly.
Discussion
Generating LLM comments without social context
Surprisingly, we found that prompting a LLM with only the
initial post produces generated comments that are similar to
the human comments in terms of their tone. One explanation
is that the LLM is capturing the tone of the original post and
generates a comment that is similar in tone to the original
post (e.g., the LLM generates a funny comment in response
to a funny post), much as people do. Another explanation is
that similarity between the tones of the human and gener-
ated comments and the dependency of the generated com-
ments on social variables reflects a selection bias in terms

--- Page 8 ---

Prompt
Surprised
Funny
Insult
Emotional
support
Self
disclosure
Worried
Thankful
Inclusion
Average
no-context
0.395
0.507
0.600
0.461
0.433
0.277
0.613
0.096
0.423
age-only
+0.013
−0.081
+0.022
+0.032
+0.008
+0.084
+0.172
+0.063
+0.039
gender-only
−0.091
+0.614∗∗∗
+0.298∗∗
−0.098
−0.103
+0.216∗
+0.25∗
+0.101
+0.148
friendship-only
+0.465∗∗∗
+1.100∗∗∗
+0.521∗∗∗
+0.109
+0.542∗∗∗
+0.246∗
+0.414∗∗∗
+0.368∗∗∗
+0.470
all-context
+0.213∗∗∗
+1.007∗∗∗
+0.433∗∗∗
+0.081
+0.386∗∗∗
+0.174
+0.485∗∗∗
+0.262∗∗∗
+0.380
Table 3: Discrepancy in regression models between generated comments and human comments (Approach 2). The “no-context”
row shows ˆδno context, the sum of absolute differences in regression coefficients across eight social variables (Figure 4) between
human and generated comments without social context. Subsequent rows display the relative changes after including the cor-
responding context in the prompt. * p < 0.05, ** p < 0.01, *** p < 0.001. p-values were obtained via error propagation and
t-test.
of who responds (e.g., women are more likely to respond
to a self-disclosing post or one seeking emotional support).
While we account for this in part by incorporating in our re-
gression models the probability that a particular viewer will
comment on a given post (i.e., the p(comment) score), it’s
possible that p(comment) under corrects for selection effects
and the model is missing unobservable signals.
Why providing social context does not consistently
make LLM comments more like human ones?
While LLM-generated comments are quite similar to human
comments in terms of tone and reflect many of the associ-
ation between social factors and tone that exist in human-
comments, explicitly including social relationship informa-
tion in the LLM prompt does not consistently improve these
measures of similarity averaged across the eight tones and
often harms it. There are several possible reasons for these
results.
The most fundamental reason may be that LLM training
data itself does not explicitly include mention of the social
characteristics or relations among the people in a conversa-
tion. To the extent these social factors are reflected in the
language that people use when responding to each other,
cues to their social characteristics or relations are already
embedded in the human posts. Relatedly, certain dyadic in-
teractions may be less common in the training corpus of the
model, leading to worse performance on those groups. For
instance, French, D’Mello, and Wense (2024) find that the
Llama-2 model imitating a teacher is much worse at explain-
ing educational information to a child than it is to an adult,
probably because more of the training data captures adult-
adult interactions rather than adult-child interactions. Even
though people are unlikely to routinely label the social char-
acteristics of those with whom they communicate with on-
line, it is possible for future work to infer some of these rela-
tionships from the language they use (Gumperz and Tannen
1979; Preot¸iuc-Pietro et al. 2015), from content they follow
(Chamberlain, Humby, and Deisenroth 2017), from social
network data (Tang, Lou, and Kleinberg 2012) and then in-
corporate the inferred social characteristics into the training
data.
Second, when given explicit social relationship informa-
tion, LLM tends to over-react and weigh this information
too heavily compared to the social information that is im-
plicit in the human post. The social relationship informa-
tion that people respond to may be quite subtle and extend
beyond the stereotypical associations with age, gender, and
relationship strength used in our LLM prompts. For exam-
ple, the congratulations message the human commenter in
Figure 1 wrote refers to the relationship between the poster
and the commenter’s son and the commenter’s best friend.
This issue of overreacting and generating a comment with
an extreme tone could also be related to the sycophancy is-
sue observed in language models, wherein models forsake
truthfulness in order to be extremely helpful and even flatter
the user by mirroring their own beliefs (Sharma et al. 2023;
Wei et al. 2023).
Third, human commenters may subvert the original mean-
ing of a post when trying to be creative and respond with a
clever retort while language models have difficulty generat-
ing non-literal, figurative language (Lai and Nissim 2024).
For example, in the following post recruiting ”kiddos” for a
summer camp, the human responds with an ironic joke while
the LLM treats the post literally.
Post: We would be thrilled to have your kiddos
join us! Please consider sending them our way.
[http://camp url]
Human: Can I send mine? He is 46 years old and has
anger issues, but he’s funny.
LLM: Aww, that sounds like an amazing experience
for the kiddos! I’ll definitely consider sending mine,
thanks for sharing this opportunity! You’re always so
thoughtful to think of others, love you!
Finally, when crafting a comment people may use additional
social context or relationship information that is invisible to
the LLM. In the following example, the commenter seems
to allude to the poster’s and commenter’s history of playing
golf.
Post: We finally closed on our new home last Thurs-
day! Now it’s time to start to move and make it ours.
Let the renovations begin!
Human: Do I need to bring my golf clubs with me
when we come down?
LLM: Congrats on the new home, buddy! Exciting
times ahead with all the projects and making it your
own. Wishing you all the best in this new chapter!

--- Page 9 ---

Conclusion
This paper investigates social relationship alignment in
LLMs. We first examined real-world public post-comment
communication data from Facebook, followed by an anal-
ysis of whether LLMs can generate comparable comments
when prompted with both post and social relationship in-
formation. Our findings indicate that LLMs can produce
comments closely resembling human-generated responses
to the same post, even without being explicitly provided
with social relationship details. Additionally, we observed
that explicitly including social relationship information in
the prompt does not consistently enhance the similarity be-
tween LLM-generated and human-generated comments. We
discussed possible explanations for our findings.
Limitations and Future Work
To the best of our knowledge, this work is the first to exam-
ine whether and how social relationships impact the seman-
tic tone of LLM-generated comments at the individual level,
providing insights into the potential of LLMs in adapting to
diverse conversational settings. It is important, however, to
note that this paper is an observational study, with no modi-
fications made to the underlying LLM product.
While we found that LLM-generated comments and hu-
man comments are similar without social context informa-
tion in the prompt, the average similarity between human
and LLM comments is modest (avg ˆβ =0.456), suggesting
there’s potential room for improvement. Although we only
evaluated incorporating social relationships via prompt engi-
neering techniques, future work should consider improving
LLMs’ ability to generate socially-realistic comments, such
as incorporating social context information at the training
stage and fine-tuning the model with conversation data.
Acknowledgements
We thank Kaiyan Peng, Itamar Rosenn, Nicolas Stier, Aude
Hofleitner, Shawndra Hill, Danny Ferrante, Ali Muzaffer,
Mauricio Figueiredo, and Taylor Ebling for helpful feedback
and support on this project.
References
Anwar, U.; Saparov, A.; Rando, J.; Paleka, D.; Turpin, M.;
Hase, P.; Lubana, E. S.; Jenner, E.; Casper, S.; Sourbut, O.;
et al. 2024. Foundational challenges in assuring alignment
and safety of large language models. arXiv:2404.09932.
Bakker, M.; Chadwick, M.; Sheahan, H.; Tessler, M.;
Campbell-Gillingham, L.; Balaguer, J.; McAleese, N.;
Glaese, A.; Aslanides, J.; Botvinick, M.; et al. 2022. Fine-
tuning language models to find agreement among humans
with diverse preferences. Advances in Neural Information
Processing Systems, 35: 38176–38189.
Brown, T. B. 2020. Language models are few-shot learners.
arXiv:2005.14165.
Bruckman, A. 2002. Studying the amateur artist: A perspec-
tive on disguising data collected in human subjects research
on the Internet. Ethics and Information Technology, 4(3):
217–231.
Burke, M.; Joyce, E.; Kim, T.; Anand, V.; and Kraut, R.
2007. Introductions and requests: Rhetorical strategies that
elicit response in online communities. In Communities and
Technologies 2007: Proceedings of the Third Communities
and Technologies Conference, Michigan State University
2007, 21–39. Springer.
Burke, M.; and Kraut, R. E. 2014. Growing closer on Face-
book: Changes in tie strength through social network site
use. In Proceedings of the SIGCHI Conference on Human
Factors in Computing Systems, 4187–4196.
Burt, R. S. 2004. Structural holes and good ideas. American
Journal of Sociology, 110(2): 349–399.
Caron, G.; and Srivastava, S. 2022.
Identifying and
manipulating the personality traits of language models.
arXiv:2212.10276.
Caron, G.; and Srivastava, S. 2023. Manipulating the Per-
ceived Personality Traits of Language Models. In Findings
of the Association for Computational Linguistics: EMNLP
2023, 2370–2386.
Chamberlain, B. P.; Humby, C.; and Deisenroth, M. P. 2017.
Probabilistic inference of twitter users’ age based on what
they follow. In Machine Learning and Knowledge Discovery
in Databases: European Conference, ECML PKDD 2017,
Skopje, Macedonia, September 18–22, 2017, Proceedings,
Part III 10, 191–203. Springer.
Chang, Y.; Wang, X.; Wang, J.; Wu, Y.; Yang, L.; Zhu, K.;
Chen, H.; Yi, X.; Wang, C.; Wang, Y.; et al. 2024. A survey
on evaluation of large language models. ACM Transactions
on Intelligent Systems and Technology, 15(3): 1–45.
Choi, Y.; Kang, E. J.; Choi, S.; Lee, M. K.; and Kim,
J. 2024.
Proxona: Leveraging LLM-Driven Personas
to Enhance Creators’ Understanding of Their Audience.
arXiv:2408.10937.
Dindia, K.; and Allen, M. 1992.
Sex differences in self-
disclosure: a meta-analysis. Psychological Bulletin, 112(1):
106.
Durmus, E.; Nguyen, K.; Liao, T. I.; Schiefer, N.; Askell,
A.; Bakhtin, A.; Chen, C.; Hatfield-Dodds, Z.; Hernandez,
D.; Joseph, N.; et al. 2023. Towards measuring the repre-
sentation of subjective global opinions in language models.
arXiv:2306.16388.
French, D.; D’Mello, S.; and Wense, K. 2024.
Aligning
to Adults Is Easy, Aligning to Children Is Hard: A Study
of Linguistic Alignment in Dialogue Systems. In Proceed-
ings of the 1st Human-Centered Large Language Modeling
Workshop, 81–87.
Ge, S.; Zhou, C.; Hou, R.; Khabsa, M.; Wang, Y.-C.; Wang,
Q.; Han, J.; and Mao, Y. 2023. Mart: Improving llm safety
with multi-round automatic red-teaming. arXiv:2311.07689.
Greengross, G.; Silvia, P. J.; and Nusbaum, E. C. 2020. Sex
differences in humor production ability: A meta-analysis.
Journal of Research in Personality, 84: 103886.
Gumperz, J. J.; and Tannen, D. 1979. Individual and social
differences in language use. In Individual differences in lan-
guage ability and language behavior, 305–325. Elsevier.

--- Page 10 ---

Hall, J. A. 2017. Humor in romantic relationships: A meta-
analysis. Personal Relationships, 24(2): 306–322.
Hendrycks, D.; Burns, C.; Basart, S.; Critch, A.; Li, J.; Song,
D.; and Steinhardt, J. 2020. Aligning ai with shared human
values. arXiv:2008.02275.
Kojima, T.; Gu, S. S.; Reid, M.; Matsuo, Y.; and Iwasawa,
Y. 2022.
Large language models are zero-shot reason-
ers. Advances in neural information processing systems, 35:
22199–22213.
Krishna, R.; Lee, D.; Fei-Fei, L.; and Bernstein, M. S. 2022.
Socially situated artificial intelligence enables learning from
human interaction. Proceedings of the National Academy of
Sciences, 119(39): e2115730119.
Lai, H.; and Nissim, M. 2024. A survey on automatic gen-
eration of figurative language: From rule-based systems to
large language models. ACM Computing Surveys, 56(10):
1–34.
Lee, J.; Oh, M.; and Lee, D. 2023.
P5: Plug-and-Play
Persona Prompting for Personalized Response Selection.
arXiv:2310.06390.
Li, J.; Galley, M.; Brockett, C.; Spithourakis, G.; Gao, J.; and
Dolan, W. B. 2016. A Persona-Based Neural Conversation
Model. In Proceedings of the 54th Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long
Papers), 994–1003.
Matz, S.; Teeny, J.; Vaid, S. S.; Peters, H.; Harari, G.; and
Cerf, M. 2024. The potential of generative AI for personal-
ized persuasion at scale. Scientific Reports, 14(1): 4692.
Njifenjou, A.; Sucal, V.; Jabaian, B.; and Lef`evre, F.
2024. Role-Play Zero-Shot Prompting with Large Language
Models for Open-Domain Human-Machine Conversation.
arXiv:2406.18460.
Olea, C.; Tucker, H.; Phelan, J.; Pattison, C.; Zhang, S.;
Lieb, M.; Schmidt, D.; and White, J. 2024. Evaluating per-
sona prompting for question answering tasks. In Proceed-
ings of the 10th International Conference on Artificial Intel-
ligence and Soft Computing.
Preot¸iuc-Pietro, D.; Volkova, S.; Lampos, V.; Bachrach, Y.;
and Aletras, N. 2015. Studying user income through lan-
guage, behaviour and affect in social media. PloS one, 10(9):
e0138717.
Santurkar, S.; Durmus, E.; Ladhak, F.; Lee, C.; Liang, P.; and
Hashimoto, T. 2023. Whose opinions do language models
reflect? In International Conference on Machine Learning,
29971–30004. PMLR.
Serapio-Garc´ıa, G.; Safdari, M.; Crepy, C.; Sun, L.; Fitz,
S.; Romero, P.; Abdulhai, M.; Faust, A.; and Matari´c,
M. 2023.
Personality traits in large language models.
arXiv:2307.00184.
Shao, Y.; Li, L.; Dai, J.; and Qiu, X. 2023. Character-llm: A
trainable agent for role-playing. arXiv:2310.10158.
Sharma, M.; Tong, M.; Korbak, T.; Duvenaud, D.; Askell,
A.; Bowman, S. R.; Cheng, N.; Durmus, E.; Hatfield-Dodds,
Z.; Johnston, S. R.; et al. 2023. Towards understanding syco-
phancy in language models. arXiv:2310.13548.
Shen, T.; Jin, R.; Huang, Y.; Liu, C.; Dong, W.; Guo, Z.;
Wu, X.; Liu, Y.; and Xiong, D. 2023. Large language model
alignment: A survey. arXiv:2309.15025.
Shriver, S. K.; Nair, H. S.; and Hofstetter, R. 2013. Social
ties and user-generated content: Evidence from an online so-
cial network. Management Science, 59(6): 1425–1443.
Shuster, K.; Xu, J.; Komeili, M.; Ju, D.; Smith, E. M.; Roller,
S.; Ung, M.; Chen, M.; Arora, K.; Lane, J.; et al. 2022.
Blenderbot 3: a deployed conversational agent that contin-
ually learns to responsibly engage. arXiv:2208.03188.
Tang, J.; Lou, T.; and Kleinberg, J. 2012.
Inferring so-
cial ties across heterogenous networks. In Proceedings of
the Fifth ACM International Conference on Web Search and
Data Mining, 743–752.
Touvron, H.; Martin, L.; Stone, K.; Albert, P.; Almahairi, A.;
Babaei, Y.; Bashlykov, N.; Batra, S.; Bhargava, P.; Bhosale,
S.; et al. 2023. Llama 2: Open foundation and fine-tuned
chat models. arXiv:2307.09288.
Tseng, Y.-M.; Huang, Y.-C.; Hsiao, T.-Y.; Hsu, Y.-C.; Foo,
J.-Y.; Huang, C.-W.; and Chen, Y.-N. 2024. Two tales of per-
sona in llms: A survey of role-playing and personalization.
arXiv:2406.01171.
Wang, X.; Xiao, Y.; Huang, J.-t.; Yuan, S.; Xu, R.; Guo, H.;
Tu, Q.; Fei, Y.; Leng, Z.; Wang, W.; et al. 2024. Inchar-
acter: Evaluating personality fidelity in role-playing agents
through psychological interviews.
In Proceedings of the
62nd Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), 1840–1873.
Wang, Y.-C.; Burke, M.; and Kraut, R. 2016. Modeling self-
disclosure in social networking sites. In Proceedings of the
19th ACM Conference on Computer-Supported Cooperative
Work & Social Computing, 74–85.
Wei, J.; Huang, D.; Lu, Y.; Zhou, D.; and Le, Q. V. 2023.
Simple synthetic data reduces sycophancy in large language
models. arXiv:2308.03958.
Weidinger, L.; Mellor, J.; Rauh, M.; Griffin, C.; Uesato, J.;
Huang, P.-S.; Cheng, M.; Glaese, M.; Balle, B.; Kasirzadeh,
A.; et al. 2021. Ethical and social risks of harm from lan-
guage models. arXiv:2112.04359.
Wellman, B.; and Wortley, S. 1990. Different strokes from
different folks: Community ties and social support. Ameri-
can Journal of Sociology, 96(3): 558–588.
Xu, C.; Chern, S.; Chern, E.; Zhang, G.; Wang, Z.; Liu, R.;
Li, J.; Fu, J.; and Liu, P. 2023. Align on the fly: Adapting
chatbot behavior to established norms. arXiv:2312.15907.
Xu, X.; Liu, J.; and Liu, J. H. 2024.
The effect of so-
cial media environments on online emotional disclosure: tie
strength, network size and self-reference. Online Informa-
tion Review, 48(2): 390–408.
Zeng, X.; and Wei, L. 2013. Social ties and user content
generation: Evidence from Flickr. Information Systems Re-
search, 24(1): 71–87.
Zhang, S. 2018. Personalizing dialogue agents: I have a dog,
do you have pets too. arXiv:1801.07243.

--- Page 11 ---

Zhao, W. X.; Zhou, K.; Li, J.; Tang, T.; Wang, X.; Hou, Y.;
Min, Y.; Zhang, B.; Zhang, J.; Dong, Z.; et al. 2023. A sur-
vey of large language models. arXiv:2303.18223.
Zhong, P.; Zhang, C.; Wang, H.; Liu, Y.; and Miao, C. 2020.
Towards Persona-Based Empathetic Conversational Models.
In Proceedings of the 2020 Conference on Empirical Meth-
ods in Natural Language Processing (EMNLP), 6556–6566.
Zhou, J.; Chen, Z.; Wan, D.; Wen, B.; Song, Y.; Yu, J.;
Huang, Y.; Peng, L.; Yang, J.; Xiao, X.; et al. 2023. Char-
acterglm: Customizing chinese conversational ai characters
with large language models. arXiv:2311.16832.
Ziems, C.; Dwivedi-Yu, J.; Wang, Y.-C.; Halevy, A.; and
Yang, D. 2023. NormBank: A knowledge bank of situational
social norms. arXiv:2305.17008.

--- Page 12 ---

Appendix
Comment Semantic Classifier
We rely on a multi-task learning framework to predict 8 se-
mantic categories (e.g., insightful, emotional support). This
model was built on a combination of training data from hu-
man labels, user actions, and regex labels. We describe the
semantic categories in Figure 5. For this analysis, we rely on
a version of the model that relies only on comment text as
input.
Part I
Likelihood Ratio Test - Full and Social Context Models
Compared to Baseline
In this section, we show the Like-
lihood Ratio Test results comparing different model speci-
fications to a baseline model that includes only post topics
in Table 4. We compare individual social context features
(+Age, +Gender, +Friend Type) to the baseline model and
find individual features lead to a better fit. When we compare
to a Full model, which includes all social context signals, we
see further gains.
Likelihood Ratio Test - Full Compared to Individual So-
cial Context Features
We next do a Likelihood Ratio test
where we compare the Full model to a model that has only
one social context (Age, Gender, or Friend) signal. Across
all semantic categories, we see in Table 5 that the Full model
outperforms a model with just a single social context signal.
Part II
LLM prompts
In this section, we describe how we
prompt the LLM to generate comments. Each prompt con-
sists of three parts: background, context, and generation in-
structions. The background part provides a general descrip-
tion of the task and the user post, which is shared across all
prompts:
You are a Facebook user and want to comment on a
post from another Facebook user (the poster) in the
most proper way based on the social relationship be-
tween you and the poster.
Here is the post made by the poster on Facebook:
[Post]*
{post text}
*.
The instruction part is as follows:
Generate a short comment right below the post, with
“[Comment]:” prefixing the comment, in one para-
graph. No explanation needed.
The context component varies between prompt types and
provides different levels of social context information. Ta-
ble 6 presents the context part of different prompt types. The
field {friendship status} can be one of the following:
• close friends: “you and the poster are very close friends
and interact with each other frequently”
• non-close friends: “you and the poster are friends but not
interact with each other much”
• strangers: “you and the poster are strangers”
Comparison between Approach 1 and Approach 2
This
section utilizes a straightforward mathematical model to
contrast Approach 1 and Approach 2 from Part II. We
demonstrate that Approach 1 considers both between-group
and within-group differences, whereas Approach 2 focuses
solely on between-group differences.
We frame our analysis based on the social context predic-
tor X, with two response variables: Y representing the tone
of human comments, and Z indicating the tone of generated
comments. Each approach employs distinct metrics to assess
the similarity between Y and Z. For simplicity, we consider
a binary predictor: Xi = 1 indicates group 1 and Xi = 0
indicates group 0.
In Approach 1, we employ the regression model
Zi = azy + bzyYi + ei,
where the coefficient bzy is
bzy = Cov(Y, Z)
Var(Y ) .
(3)
Here, Cov(Y, Z) represents the covariance between Y and
Z, and Var(Y ) signifies the variance of Y . These statis-
tics are partitioned into three components: (co)variance from
group 0 (x = 0), (co)variance from group 1 (x = 1), and
between-group (co)variance, calculated as follows:
Cov(Y, Z) =n0
n Cov(Y, Z)x=0 + n1
n Cov(Y, Z)x=1
+ n0n1
n2 ( ¯Z1 −¯Z0)( ¯Y1 −¯Y0),
Var(Y ) = n0
n Var(Y )x=0+n1
n Var(Y )x=1+n0n1
n2 ( ¯Y1−¯Y0)2.
¯Y0 and ¯Y1 denotes the mean values of Y within group 0 and
1, respectively. Similarly, ¯Z0 and ¯Z1 are the mean values of
Z in these groups. n0 and n1 are sample size of groups 0
and 1, respectively, with n = n0 + n1 representing the total
sample size.
Therefore,
both
the
within-group
and
between-
group
(co)variance
influence
the
regression
coeffi-
cients bzy. If the between-group (co)variance is sig-
nificant
compared
to
within-group
(co)variance,
bzy
approximates
the ratio
of
between-group
differences,
( ¯Z1 −
¯Z0)/( ¯Y1 −
¯Y0).
Conversely,
if
the
within-
group
(co)variance
is
dominant,
bzy
approximates
(n0Cov(Y, Z)x=0 + n1Cov(Y, Z)x=1)/(nVar(Y )).
For approach 2, we estimate two separate regressions,
Yi = ay + byXi + eyi,
Zi = az + bzXi + ezi.
We then calculate the difference between regression coeffi-
cients,
δzy = |bz −by|.
This calculation is straightforward for a single variable pre-
dictor, resulting in
δzy = | ¯Z1 −¯Z0 −( ¯Y1 −¯Y0)|.
(4)
Comparing this with the coefficient bzy from Approach
1, δzy is solely dependent on between-group differences. In
contrast, bzy incorporates both within-group differences and
within-group variability, facilitating individual-level com-
parisons.

--- Page 13 ---

Figure 5: We describe the semantic categories used in this paper. For the post and comment examples, we paraphrase them.
Surprised
Funny
Insult
Emo Support
Self-Disclosure
Worried
Thankful
Relaxed
Baseline
−735416
−1142279
−1121999
−1021913
−789679
−898347
−1183726
543822
+Age
−734805∗∗∗
−1130343∗∗∗
−1116308∗∗∗
−1017417∗∗∗
−786774∗∗∗
−895814∗∗∗
−1176533∗∗∗
546275∗∗∗
+Gender
−732373∗∗∗
−1141036∗∗∗
−1115312∗∗∗
−1014161∗∗∗
−789117∗∗∗
−897948∗∗∗
−1177248∗∗∗
544535∗∗∗
+Friend
−735340∗∗∗
−1141821∗∗∗
−1121958∗∗∗
−1021860∗∗∗
−789478∗∗∗
−898180∗∗∗
−1183699∗∗∗
543910∗∗∗
Full
−731698∗∗∗
−1128197∗∗∗
−1109017∗∗∗
−1009230∗∗∗
−786108∗∗∗
−895229∗∗∗
−1169517∗∗∗
547143∗∗∗
Table 4: We include results for likelihood ratio tests across the different semantic tone categories when comparing to a baseline
model. We find better model fit for social context signals individually and all social context signals (Full) when compared to a
Baseline model. *p <0.1; **p <0.05; ***p <0.01
Prompt engineering
To test whether our conclusion re-
lies on how the social context information is presented in the
prompt, in this section we study how variation of the prompt
affects the discrepancy between generated comments and
human comments. We tested the following ideas,
• Adjusting the order of social context information in the
prompt. More specifically, we switched the order of age,
gender, and friendship type information in the context
part of the prompts, as demonstrated in Table 6.
• Zero-shot chain of thoughts (CoT). Following the idea of
zero-shot-CoT, we added the following sentence to the
instruction part of the prompt: “Think step by step with
explanations”.
• Rephrasing the social context in the prompt. Our results
imply that the generated response is very sensitive to
the friendship type presented in the social context. To
test the reliability, we rephrase the friendship type from
“strangers” to “non-friends”.
The results are summarized in Table 8, which shows while
some prompt engineering techniques helped to reduce the
discrepancy, they did not alter the main conclusion of our
findings.
As illustrated in Table 8, altering the order of social con-
text information in the prompt significantly reduces discrep-
ancies. This finding aligns with previous studies indicating
that the sequence of instructions in prompts affects LLM
performance. Additionally, employing CoT reasoning also
decreases discrepancies. However, modifying the descrip-
tion of friendship types has a marginal effect. Despite these
adjustments, the no-context prompt still exhibits the lowest
discrepancy, underscoring the LLM’s limited ability to re-
spond appropriately to social context.

--- Page 14 ---

Surprised
Funny
Insult
Emo Support
Self-Disclosure
Worried
Thankful
Relaxed
Age
−734805
−1130343
−1116308
−1017417
−786774
−895814
−1176533
546275
Gender
−732373
−1141036
−1115312
−1014161
−789117
−897948
−1177248
544535
Friend
−735340
−1141821
−1121958
−1021860
−789478
−898180
−1183699
543910
+Full
−731698∗∗∗
−1128197∗∗∗
−1109017∗∗∗
−1009230∗∗∗
−786108∗∗∗
−895229∗∗∗
−1169517∗∗∗
547143∗∗∗
Table 5: We include results for likelihood ratio tests across the different semantic tone categories when comparing to a full
model. The comparison is done by comparing the Full model to each social context signal individually. We see that the Full
model provides better fit than a model with just a single social context signal. *p <0.1; **p <0.05; ***p <0.01.
Prompt type
Context
llm-all-context
Remember that {friendship status}. Also remember that you are a {commenter gender} of age
{commenter age} and the poster is a {poster gender} of age {poster age}
llm-age-only
Remember that you are of age {commenter age} and the poster is of age {poster age}
llm-gender-only
Remember that you are a {commenter gender} and the poster is a {poster gender}.
llm-friends-only
Remember that {friendship status}.
Table 6: Social context provided in different prompts.
Prompt
Average discrepancy
baseline all context
0.803
gender age friends
−0.133
age gender friends
−0.084
zero shot cot
−0.063
non friends
+0.010
Table 8: Tuning the prompt helps to reduce but cannot elimi-
nate the discrepancy ¯ˆδ. First row shows the average discrep-
ancy from the baseline all context prompt, followed by rela-
tive changes after modifying the prompt.

--- Page 15 ---

model
human
llm-all-context
llm-no-context
Figure 6: Regression coefficients of social context factors in the fitted models for remaining scores, including surprised, funny,
provide support, worried, thankful, and inclusion.
Social context
factor
Surprised
Funny
Insult
Emotional
support
Self
disclosure
Worried
Thankful
Inclusion
commenter male
−0.046
0.069
−0.023
−0.001
−0.081∗∗
0.157∗∗∗
0.006
0.069∗∗
poster male
−0.004
0.005
−0.06
−0.026
0.023
0.011
−0.004
−0.017
commenter male ×
poster male
0.020
0.263∗∗∗
0.157∗∗
0.050
−0.080∗
0.022
0.234∗∗∗
0.022
commenter age
0.019∗
−0.056∗∗
−0.005
−0.019∗
0.016
0.008
0.007
0.002
poster age
0.024∗
0.022
−0.031
0.003
−0.013
−0.001
−0.016
−0.001
commenter age ×
poster age
0.013
−0.01
0.010
−0.009
0
0.007
−0.01
−0.005
non-close friends
0.083∗∗∗
0.395∗∗∗
0.255∗∗∗
0.011
0.283∗∗∗
−0.009
0.202∗∗∗
0.097∗∗∗
strangers
0.104∗∗∗
0.318∗∗∗
0.13∗
0.072∗
0.238∗∗∗
−0.021
0.066
0.094∗∗
Table 7: The impact of providing context on the discrepancy between generated comments and human comments. The dis-
crepancy is calculated as the difference in fitting coefficients between the regression models for generated comments and that
for human comments. Significant changes are highlighted: red indicates that adding context increased the discrepancy, while
green shows a reduction in discrepancy due to context. * p < 0.05, ** p < 0.01, *** p < 0.001. p-values were obtained via
two-sample t-test.

```
