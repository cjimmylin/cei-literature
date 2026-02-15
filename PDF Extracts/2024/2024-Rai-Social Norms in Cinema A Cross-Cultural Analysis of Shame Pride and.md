---
title: "2024-Rai-Social Norms in Cinema A Cross-Cultural Analysis of Shame Pride and - PDF Extract"
source_pdf: "2024-Rai-Social Norms in Cinema A Cross-Cultural Analysis of Shame Pride and.pdf"
pages: 20
extracted_at: "2026-02-15T17:51:57.472126"
---

# PDF Extract: 2024-Rai-Social Norms in Cinema A Cross-Cultural Analysis of Shame Pride and

**Source PDF:** 2024-Rai-Social Norms in Cinema A Cross-Cultural Analysis of Shame Pride and.pdf
**Total Pages:** 20

---

## Content

```
--- Page 1 ---

Social Norms in Cinema: A Cross-Cultural Analysis of Shame, Pride and
Prejudice
Sunny Rai†, Khushang Jilesh Zaveri⋄, Shreya Havaldar†, Soumna Nema♠,
Lyle H. Ungar† & Sharath Chandra Guntuku†
†University of Pennsylvania, ⋄Johns Hopkins University, ♠Mahindra University
{sunnyrai, sharathg}@seas.upenn.edu
Abstract
Shame and pride are social emotions expressed
across cultures to motivate and regulate peo-
ple’s thoughts, feelings, and behaviors.
In
this paper, we introduce the first cross-cultural
dataset of over 10k shame/pride-related ex-
pressions, with underlying social expectations
from 5.4K Bollywood and Hollywood movies.
We examine how and why shame and pride
are expressed across cultures using a blend of
psychology-informed language analysis com-
bined with large language models. We find
significant cross-cultural differences in shame
and pride expression aligning with known cul-
tural tendencies of the USA and India – e.g., in
Hollywood, shame-expressions predominantly
discuss self whereas shame is expressed toward
others in Bollywood. Women are more sanc-
tioned across cultures and for violating similar
social expectations.
1
Introduction
Shame and pride are social emotions expressed
across cultures to motivate and regulate people’s
thoughts, feelings, behaviors, achievements, and so-
cial adaptations (Fischer and Tangney, 1995; Goetz
and Keltner, 2007; Fessler, 2007; Schaumberg and
Skowronek, 2022). The expressions and appraisals
of shame and pride vary across cultures and is a re-
search question of great significance to understand
society and self-regulation (Wong and Tsai, 2007;
Lewis et al., 2010; Wegge et al., 2022). The overar-
ching question we ask in this paper is, how and why
shame and pride are expressed across cultures.
Knowing cross-cultural differences in shame/pride-
related expressions will help us measure psycholog-
ical constructs such as shame proneness (Tangney
et al., 1992; Cohen et al., 2011) and self-esteem
(Pyszczynski et al., 2004) reliably from language
– enabling effective human-computer interactions
in domains such as AI-driven psychotherapy (Re-
sendiz and Klinger, 2023; Demszky et al., 2020).
Examining behaviors evoking shame and pride will
And should we bow before others begging....them
to marry our daughters?
This shall not happen.
Neither
will
the
girls
be
alive
here
nor
shall....we be ashamed of ourselves. You cannot
kill the life which God has given. I won’t let
you commit the sin.
⇒Not able to marry off their daughters evokes
shame.
Sister-in-law!
Congrats,
sister-in-law!
Big
brother has started working!
Really?
Now you will have a place of pride in this family!
Yes, please!
⇒Employed husband evokes pride
Table 1: Excerpts of dialogues expressing explicit social
emotions shame and pride indicating actions and social
approval.
reveal culture-specific societal expectations and
attitudes (See Table 1) – paramount to building
culturally competent AI models for diverse users
(Talat et al., 2021; Atari et al., 2023).
For our study, we select two top movie indus-
tries, i.e., Hollywood and Bollywood1. Hollywood
primarily depicts social situations from the USA,
an individualist society that values competency
and autonomy (Triandis, 1989, 1988). Bollywood
depicts India, a collectivist society where one’s
sense of self is interwoven with community be-
liefs. The cultural dichotomy between India and
the USA (i.e., collectivism vs. individualism) thus
presents a rich ground for understanding variations
in their beliefs and values. Our approach blends
psychology-informed language analysis with state-
of-the-art Large Language Model (LLM) to delin-
eate interpretable psychosocial constructs such as
self-focus and morality in shame/pride-related ex-
pressions and extract implicit social expectations
behind them.
1https://en.wikipedia.org/wiki/Film_industry
arXiv:2402.11333v5  [cs.CY]  9 Feb 2025

--- Page 2 ---

This paper makes the following research contri-
butions: (a) We develop a cross-cultural dataset of
over 10k shame/pride-related dialogues with un-
derlying social expectations2, (b) We demonstrate
cross-cultural variations in how and why shame and
pride are expressed in movies, and (c) We illustrate
that women are more subjected to social sanctions
than men across cultures and for violating similar
social expectations.
To the best of our knowledge, this is the first em-
pirical study analyzing the psychosocial constructs
underlying shame/pride-related expressions across
cultures and the social expectations behind them.
2
Movies Subtitles Corpora
Movies provide culture-specific life-like depic-
tions of social situations (Adkins and Castle, 2014;
Kubrak, 2020).
The natural conversation style
between characters in movies can reveal the so-
cial power dynamics (e.g., boss-employee, father-
daughter) and gender roles. Another potential al-
ternative is social media posts however, they are
(a) skewed to social situations specific to young de-
mographic groups from Western countries, and (b)
are second-hand reports that do not reveal fully the
social dynamics of how shame/pride are expressed
in natural conversations, for instance, between a
boss and an employee.
We collected English subtitles for 5,435 Holly-
wood and Bollywood movies that were released
post-1990 by auto-crawling websites that host or
link movie subtitles (See Table 2 for data distribu-
tion). The subtitles are professionally done trans-
lations to preserve the emotions and intended mes-
sage. Bollywood movie subtitles were collected
from www.Bollynook.com and Hollywood movie
subtitles were from the publicly available Kaggle
movie subtitles dataset3. The year mapping was
performed to ensure a similar period for collected
movies. The year of release for movies was veri-
fied by either parsing subtitle file names having a
release year or probing Wikipedia entries.
2.1
Extracting Shame and Pride related
Expressions
The expressions of shame and pride could be ex-
plicit (See Table 1) or implicit (e.g. characters’
lowered shoulders, avoiding eye contact, etc.). We
2https://github.com/Khushangz/
Cross-Cultural-Social-Norms-Dataset/
3https://www.kaggle.com/datasets/adiamaan/
movie-subtitle-dataset
Hollywood
Bollywood
#Movies
2697
2738
#Tokens
20.78M
22.62M
#Shame
1221
5409
#Pride
2805
2999
#Control
4385
8303
Table 2: Data Distribution. #shame indicates the num-
ber of dialogues with the word "shame" or its derivative
form (e.g., ashamed, shameless - See Table A1). Simi-
larly, #pride indicates the number of dialogues with the
word pride or its derivative form (e.g., proud). Control
comprises dialogues without words shame, pride, or
their derivatives.
extracted explicit mentions of shame and pride
to learn about occurrences of shame and pride as
determined by the characters. We adopted a key-
word search-based approach (See Appendix A1)
to identify dialogues along with the previous and
the next two lines for situational context (See Table
1). For short dialogues such as monosyllabic re-
sponses in spoken conversations, we appended an
extra previous and next line to context. One author
manually checked the entire dataset of shame and
pride-related dialogues to filter out dialogues with
conventional phrases such as "what a shame", "it’s
a shame", "proudly presents".
Detecting implicit shame/pride-related expres-
sions in textual discourse is a complex task. Com-
putational systems for detecting social emotions
such as shame and guilt underperform significantly
compared to basic emotions such as joy due to
internal self-evaluation associated with social emo-
tions (Demszky et al., 2020; Resendiz and Klinger,
2023). We used GPT-4 language model (Achiam
et al., 2023) to detect implicit expressions of shame
in given movie dialogues. We recruited two human
annotators to determine the agreement with GPT-4
generated labels (See Appendix A.2 for details).
On a randomly sampled 100 situations each from
H/Bollywood, the model labeled 20 samples to be
expressing shame in Bollywood and 5 samples in
Hollywood. However, the agreement between hu-
man annotators was low (4 out of 20 samples in
Bollywood and 1 out of 5 samples in Hollywood
where both annotators agreed with GPT-4). Hu-
man annotators across cultures tend to cross-label
shame and guilt (Troiano et al., 2019) and follow-
up discussions with annotators revealed similar ten-
dencies. One such example from Hollywood is

--- Page 3 ---

Figure 1: An overview of our approach comprising two
key steps (a) Vocabulary approach and (b) Prompting a
pre-trained LLM.
provided below:
“about feeding the poor, I’ve never done any of
that. God tells us to love everybody. I’ve hated
people... my family, my family, ”
Here, the speaker is probably expressing guilt,
shame, or both. Given subjective beliefs and poor
agreement with generated outputs, we adopted a
high precision-low recall strategy and limited our
further analysis to explicit mentions of shame and
pride.
We created four sets of dialogues: (a) shame-
related dialogues in Bollywood, (b) shame-related
dialogues in Hollywood, (c) pride-related dialogues
in Bollywood and (d) pride-related dialogues in
Hollywood. Cross-cultural differences also exist in
speaking styles across cultures and we thus formed
a control set of dialogues unrelated to shame and
pride for both movie industries to remove the varia-
tions in language markers owing to culture-specific
speaking styles (See Table 2 for dialogue distribu-
tion).
3
Approach
Fig. 1 illustrates our study design comprising two
key approaches (a) using a psychosocial vocabulary
approach to measure how expressions of shame and
pride differ and (b) prompting LLM approach to
extract reasons behind them and how they differ
between India and the U.S.A.
3.1
Vocabulary Approach
Linguistic Inquiry of Word Count (LIWC) (Boyd
et al., 2022) is a corpus analysis tool to identify
psychological constructs such as "self-focus" and
"morality", and therefore, is widely used for exam-
ining social behaviors such as self-regulation and
conformity.
To understand cross-cultural linguistic variations
in the manifestation of shame and pride, we com-
puted the normalized distribution of psychosocial
categories in LIWC from the dialogues and exam-
ined their correlation with shame and pride com-
pared to the control set. The search keywords used
for building social emotions corpus (See Table A1)
were removed from the LIWC dictionary to prevent
overestimation of shame- (e.g., negative emotion)
and pride-related categories (e.g., achievement).
3.2
Prompting Approach
Identifying why shame/pride is expressed in dis-
course requires multicultural world knowledge.
LLMs such as GPT-4 exhibit a superlative prag-
matic understanding of the world around us and are
increasingly used for extracting implicit meanings
and beliefs (Pan et al., 2023; Törnberg, 2023). We
used GPT-4 chat in a two-shot setting ( See Tables
A2 and A3 for prompts) to identify:
• who is <being shamed/feeling proud> in the
given movie discourse, and what is their gen-
der? and,
• What is the reason behind <the feeling of
shame/pride>?
Since there are at least two characters in a dis-
course, the first question orients the LLM to fo-
cus on the person experiencing the social sanction
or approval and then identify their gender. The
output for the second question serves as the im-
plicit social expectation that led to the expression
of shame/pride in the culture. Asking for "rea-
son" leading to the expression of social emotion
encourages LLMs to retrieve expectations from the
provided context, mitigating potential Anglocentric
tendencies (Havaldar et al., 2023b).
Thematic
Analysis
of
Reasons
Behind
Shame/Pride-related
Expressions
To
cap-
ture overarching themes in social expectations
that led to shame/pride-related expressions in
Indian and American societies, we performed
agglomerative clustering after embedding unique

--- Page 4 ---

Figure 2: Pearson r for LIWC categories significantly
correlated (p < 0.05) with shame for Hollywood and
Bollywood after Benjamini-Hochberg p-value correc-
tion (See Appendix for confidence intervals and p val-
ues). Note, 1st person sing pronouns are strongly cor-
related with Hollywood-shame whereas the correlation
with 2nd person pronoun and social references are up to
3 times stronger in Bollywood compared to Hollywood.
See Table A7 and A9 for the complete set of correla-
tions.
shame and pride-related reasons using SBERT
embeddings (Reimers and Gurevych, 2019).
Unlike movie dialogues, reasons extracted from
GPT-4 chat are short phrases (See Table 4) and are
devoid of culture-specific language style markers
(i.e., Indian English vs American English) thus, no
control for culture-specific language is needed.
4
Results
4.1
How is shame/pride expressed across
cultures?
Shame is associated with negative emotions, power,
and morality in both movie industries (See Ta-
bles A7 and A9) however, significant cultural nu-
ances exist in its manifestation (See Fig. 2). In
Bollywood, shame-related expressions are other-
oriented as indicated by 2nd person pronouns and
social references. Female and sexual categories are
correlated with shame exclusively in Bollywood po-
tentially indicating the honor system in collectivist
societies (Caffaro et al., 2014). Other psychoso-
cial categories such as swearing and conflict with
present focus reveal the role of shame in enforcing
conformity. In Hollywood, shame expressions are
self-focused with remorse (e.g., sadness, anxiety)
and have past-focused language. Illness is uniquely
correlated with shame in Hollywood indicating so-
cial sanctions around incapability.
A similar dichotomy is observed for pride (See
Figure 3: Pearson r for LIWC categories significantly
correlated (p < 0.05) with pride for Hollywood and
Bollywood after Benjamini-Hochberg p-value correc-
tion (See Appendix for confidence intervals and p val-
ues). Note the contrast, Achievement-related & We-
centered pride in Bollywood vs Social & Self-centered
pride in Hollywood. See Table A8 and A10 for the com-
plete set of correlations.
Fig. 3). In Bollywood, pride is achievement/power
focused and "We"-centered. Pride is associated
exclusively with men in Bollywood. Other psy-
chosocial categories such as moral and politics are
more strongly associated with pride. In Hollywood,
pride is more self-centered and expressed for family
more. Male references are more strongly associ-
ated with pride than females in Hollywood whereas
the female category has an insignificant (p > 0.05)
correlation with pride in Bollywood. Pride has a
positive undertone in Hollywood whereas in Bol-
lywood, we speculate that it relates to honor (e.g.,
protecting family’s pride, bringing pride to family)
and does not have a positive undertone.
4.2
How do social expectations behind
shame/pride vary across cultures?
Cross-Cultural Shame/Pride Dataset
For the
Bollywood set, GPT-4 predicted reasons (also im-
plicit social expectations) for 5321 (98.4%) shame-
related dialogues out of 5409, and 2237 (74.6%)
pride-related dialogues out of 2999. For the Holly-
wood set, GPT-4 chat predicted a reason for 1156
(94.6%) shame-related dialogues out of 1221 and
1731 (61.7%) pride-related dialogues out of 2805.
Upon manual analysis, we found that pride is also
used to express affection, specifically toward close
family members such as children. As a result, a
lower number of reasons is associated with pride
compared to shame. GPT-4 chat predicted a to-
tal of 10,445 social expectations (See Table 3 for
distribution). Prompting "reasons" behind shame

--- Page 5 ---

Bollywood
Hollywood
shame
pride
shame
pride
male
2690
1259
591
776
female
1215
326
246
236
Not clear
1416
652
319
719
total
5321
2237
1156
1731
Table 3: Reason and Gender distribution (with dupli-
cates) for dialogues for which GPT-4 predicted male
or female. The duplicate reasons are not removed as
their frequency reflects their prevalence and is useful
for estimating gender association.
and pride allowed us to capture high specificity in
cultural norms (See Tables 4 for shame-related ex-
pectations and A6 for pride-related expectations).
4.2.1
Manual Evaluation
Two volunteers manually verified the predicted gen-
der for "the person experiencing shame/pride" and
the predicted "reason" for a randomly sampled set
of 100 dialogues each from Hollywood and Bolly-
wood. An Indian annotator aware of social roles
and expectations in Indian society labeled the Bol-
lywood set. Likewise, an American annotator la-
beled the Hollywood set.
For Bollywood, 8% of predicted gender and 11%
of predicted reasons were incorrect where it was
5% and 2% respectively for Hollywood (See Ta-
ble A5 for more details). There were 20 cases
where gender (15) and/or reason (9) were ambigu-
ous whereas, for Hollywood, there were 11 (gen-
der=10, reason=1) such samples.
4.2.2
Thematic Analysis
Twenty-four clusters for shame-related reasons and
fifteen for pride-related reasons were formed using
agglomerative clustering ( See Tables A13 and A14
for clustering parameters). The clusters were man-
ually assigned a theme (as depicted on the Y-axis
of Fig. 4 and 5) after analyzing the ten closest sam-
ples based on cosine distance from the centroid of
the cluster (See Table A11 and A12 for examples in
each cluster). We computed the relative association
for each cluster with Bollywood and Hollywood
using eq. 1 and performed the Barnard-Exact Test
(Barnard, 1947) with the Yates Correction (Yates,
1934) to test if the possibility of observing norms
related to pre-assigned themes is statistically differ-
ent across movie industries.
Bollywood
eavesdropping on private conversation
expressing love for a man
Incestuous relationship
giving birth to a girl child
Hollywood
not living up to expectations
hiding/avoiding confrontation
not returning calls after intimacy
mistreatment of a woman
Table 4: A subset of reasons extracted from movie
dialogues expressing shame. A total of 4604 unique
reasons (Bollywood-3660, Hollywood-944) were ex-
tracted.
⃗∆= ∀ti∈themes
Dbollyti
Dbolly
−
Dhollyti
Dholly
(1)
Here,
Dindustryti
represents
dialogues
to
industry ∈{holly, bolly} and ti ∈themes (as
depicted on Y-axis in Fig 4 and 5).
Shame-related social norms
Themes such as
lack of accountability and poverty are more com-
mon in Hollywood whereas inappropriate sexual
behavior and gender roles are more prevalent in
Bollywood (See Fig. 4). Unsurprisingly, collec-
tivist factors such as non-conformity in gender
roles, disrespect, and deviation from family norms
are strongly associated with shame in Bollywood
whereas individualistic attributes such as poverty,
causing harm and incompetence evoke shame in
Hollywood.
Pride-related social norms
Duty, doing the
"right" thing, and, self-identity are associated with
pride in Hollywood whereas Ethnolinguistic iden-
tity, and son’s achievements are associated with
pride in Bollywood (See Fig. 5).
4.2.3
How is shame/pride attributed across
genders?
For the Bollywood set, GPT-4 predicted 1541 tar-
gets as female and 3949 as male. For the Holly-
wood set, GPT-4 predicted 482 targets as female
and 1367 as male. Across all combinations (shame
vs pride x Bollywood vs. Hollywood in Table 3),
there are more male targets than females in line

--- Page 6 ---

Figure 4: Relative association (∆) of Bollywood and
Hollywood to themes obtained from agglomerative clus-
tering performed on shame-related norms. ∗indicates
significant difference i.e., p < 0.05. See Table A15 for
statistics and p-value.
with the findings of Geena Davis Inclusion Quo-
tient4.
We computed the gender-wise attribution to
"shame" and "pride" in movie dialogues using eq.
2. A positive score indicates a higher association
of gender groups with pride, whereas a negative
score reflects a higher association with shame. A
null score indicates no preference.
⃗∆g = ∀g∈{male,female}
Dprideg −Dshameg
Dg
(2)
Here, Dprideg represents movie dialogues hav-
ing pride-related words where the target of pride is
g ∈{male, female}, Dshameg represents movie
dialogues having shame-related word where the tar-
get of shame is g ∈{male, female} and Dg rep-
resents the number of movie dialogues spoken by g.
As depicted in Fig. 6, Hollywood movies are pride-
oriented, whereas Bollywood movies are shame-
oriented. Females are attributed more shame, and
the difference (male-female) in the expression of
pride and shame is 0.16 for Hollywood and 0.21
for Bollywood.
4https://about.google/intl/ALL_us/main/
gender-equality-films/
Figure 5: Relative association (∆) of Bollywood and
Hollywood to themes obtained from agglomerative clus-
tering performed on pride-related norms. ∗indicates
significant difference i.e., p < 0.05. See Table A16 for
statistics and p-value.
Figure 6: Relative association (∆) of social emotions
attributed to male and female. A higher positive score
indicates a stronger association of gender with pride.
Social expectations evoking shame are similar
across movie industries (See Fig. 7 and 8). Sexual-
ity (e.g., promiscuity, immodesty) is the dominant
theme for sanctioning women in both movie indus-
tries whereas males are shamed for incompetency.
Women across movie industries express more pride
in family roles. Men-pride in Bollywood is cen-
tered on justice, winning and bravery whereas it is
duty, self-identity and winning in Hollywood (See
Fig. A1 for gender differences in pride).
5
Discussion
We release a cross-cultural dataset of shame- and
pride-related expressions with implicit reasons be-
hind them. To the best of our knowledge, the only
related corpus is the GoEmotions dataset (Demszky
et al., 2020) comprising 817 samples for embar-
rassment and 452 samples for pride. Our dataset

--- Page 7 ---

Figure 7: Gender differences in shame-related themes
in Bollywood movies. ∗indicates significant difference
i.e., p < 0.05.
can help develop computational models for detect-
ing shame/pride expressions and recognizing how
appraisals of such emotions vary – enabling cultur-
ally cognisant human-computer conversations for
diverse users (Kim et al., 2011) and cross-cultural
intent translation5.
Shame is a highly undesirable emotion em-
phasizing incompetency and failures in the U.S.
and used sparingly (Cohen, 2003; Boiger et al.,
2013) whereas Eastern cultures use shame more
frequently and it is known to have a desirable affect
(Lim, 2016). Notably, we also observe that shame
is 4.5 times more common in Bollywood compared
to Hollywood. We also observe that shame is self-
focused (reflecting internal shame) in Hollywood
(See Table 2 and Fig. 2 for frequency distribution
and psychosocial constructs). In contrast, shame is
interdependent in collectivist communities (Wong
and Tsai, 2007). The empirical analyses reveal
other-focused (also, the public nature of shame)
in Bollywood movies (See Fig. 3). Moreover,
the contrasting tenses coupled with varying emo-
tions, i.e., past-focus + sadness in Hollywood vs.
present-focus + conflict in Bollywood, reflect their
varying goals, i.e., remorse for past failures/losses
5DARPA
Computational
Cultural
Under-
standing:
https://www.darpa.mil/program/
computational-cultural-understanding
Figure 8: Gender differences in shame-related themes
in Hollywood movies. ∗indicates significant difference
i.e., p < 0.05.
vs enforcing conformity (Wong and Tsai, 2007).
Pride-related discourse in Hollywood is duty and
achievement-focused, in line with prior findings
that the significance of "success" grows as a soci-
ety becomes more individualistic (Cohen, 2003).
In Bollywood, pride is collective and male-focused
(we, achievement, male-focused) (Khadilkar et al.,
2022). It is also interesting to note linguistic mark-
ers such as determiner (used with objects/nouns) in
Bollywood indicate more materialistic pride, com-
pared to personal pronouns and social references
in Hollywood which reflect more personal pride.
Eliciting reasons leading to shame and pride ex-
pressions revealed social expectations across cul-
tures. We observed high specificity in extracted
reasons revealing cultural subtleties (e.g., desire
for a son in Bollywood vs. returning calls after
date night in Hollywood). To tease apart cultural
differences, we first considered mapping social ex-
pectations/generated reasons to Schwartz’s Theory
of Values (Schwartz, 2012). However, social ex-
pectations were found to have contrasting values
depending on the culture. Consider "refusing to
marry", an instance of non-conformity in Indian
society, whereas it is an instance of self-direction in
a Western context. We thus performed hierarchical
clustering and empirically picked the distance after
manually analyzing the quality and granularity of
clusters. The situations connected to shame and

--- Page 8 ---

pride in the U.S. society (i.e., lacking accountabil-
ity, poverty, harm) vs Indian society (e.g., inappro-
priate sexual behavior, gender roles, betrayal - see
Fig 4 and 5) align with known cultural tendencies
(i.e., individualist vs collectivist) of both nations
(Triandis, 1988).
The vision of safe and accountable AI is cen-
tered on LLMs’ moral and value alignment. The
dominant approach for norm discovery involves
prompting LLMs, sometimes coupled with a verifi-
cation step such as an entailment test or identifying
underlying emotion (negative emotion →norm vi-
olation) (Jiang et al., 2021; Fung et al., 2022; CH-
Wang et al., 2023). However, a majority of social
situations and the human annotators employed to
label those situations reflect English beliefs and
ethics. Our approach for extracting culture-specific
social expectations and attitudes using social emo-
tions overcomes this limitation. While the cluster-
ing was performed on the reasons extracted from
movie conversations, the cluster themes are similar
to patterns seen during LIWC analysis, validating
our approach for overcoming Anglocentric bias in
LLMs for norm discovery.
Lastly, we examined how social expectations as-
sociated with shame/pride are attributed to men
and women across cultures influencing their so-
cial behaviors. For example, women are less as-
sertive across cultures to avoid negative attribu-
tion (Amanatullah and Morris, 2010; Ferguson
and Eyre, 2000) and ask for less during negoti-
ation than men (Arnold and McAuliffe, 2021). We
demonstrated that shame, a negative self-conscious
emotion expressing devaluation, is targeted toward
women more than men, and pride, a social emotion
endorsing social value, is more used for men than
women. The similarity in social expectations (e.g.
regulating sexual behaviors of women vs shaming
incompetency in men) across cultures is surprising.
We thus feel that it is important to characterize so-
cial biases in the training data before their use for
aligning LLMs.
6
Conclusion
We
introduced
a
multi-cultural
dataset
of
shame/pride-related expressions and the underly-
ing social expectations. This study demonstrates
(a) cross-cultural linguistic differences in shame
and pride-related expression, offering insights
into their functions across cultures, (b) cultural
dichotomy in social expectations, and (c) more
"social sanctions" and fewer "endorsements"
to women in movies.
Future work can utilize
our dataset for culturally aligned LLMs and
build social emotion perception and appraisal in
human-computer interactions. Additionally, our
analysis of shame/pride is the first of its kind;
we hope future NLP researchers will build upon
this work to investigate social expectations in
LLMs from a multicultural, social emotion-based
perspective.
Social Impact and Ethics Statement
Social norms discovery is a crucial component of
social and behavioral change programs6 promot-
ing equity, social justice, and well-being (Mauduy
et al., 2022; Bonan et al., 2020). Further work
explores style as a product of norm differences
(Havaldar et al., 2023a). Social psychology in-
vestigates social norms (descriptive vs injunctive)
to design experiments for understanding behav-
iors such as self-regulation, persuasion (Cialdini
et al., 1990) and decision-making (Gavrilets, 2020;
Bhanot, 2021) to promote collective-level change
in societies.
Relatedly, Kimbrough and Vostroknutov (2023)
showed people’s tendency to choose self-serving
social norms using a dictator-recipient setup, em-
phasizing the need for dedicated research efforts to
understand morality and belief distortion in differ-
ent contexts. The norms and cultural preferences
learned from movies that often showcase stereo-
typical behaviors of society may induce pluralistic
ignorance and, more importantly, lead to discrimi-
nation and biases in LLMs when used for training.
We hope that this paper will encourage scrutiny of
source corpora and derived norms before their use
for fine-tuning LLMs.
Limitations
Social norms mutate as society evolves. We ac-
knowledge that our dataset of movies (released
post-1990) may reflect social norms that are less
characteristic of contemporary society. Moreover,
countries like India and America contain a mix of
cultures. The captured norms may not reflect the
cultural variations, for example, between regions
(e.g., East Coast vs West Coast in the U.S.A or
North vs South in India). Movies also exaggerat-
edly depict the world around us (e.g., weddings,
6ALIGN-https://www.alignplatform.org/
learning-collaborative

--- Page 9 ---

criminal activities, sexual abuse, etc.), and we cau-
tion against stereotyping cultures based on movie-
based norms.
The dominant language in Bollywood movies is
Hindi and our analysis is based on their English
translations which may not always be accurate, es-
pecially when the discourse is about concepts na-
tive to a culture. LIWC dictionary may also lack
complete coverage for such concepts. We did not
compare the movie genre and acknowledge that
situational/unrealistic norms (e.g., science fiction,
comedy, etc.) could exist. Regardless, social norms
associated with shame and pride are still relatable
and reflect the target audience’s beliefs. This study
is conducted over a thirty-year long period and the
aggregated norms may not truly reflect the current
trends.
We acknowledge that the excerpts expressing
shame and pride from movie subtitles may have
led to the over-representation of certain social situ-
ations (e.g., son’s achievement and daughter’s wed-
ding in India vs duty and competence in America).
The prompts used to elicit norms may have induced
unwanted bias (Cheng et al., 2023; Lucy and Bam-
man, 2021) and it is worth investigating the vari-
ations if any, in extracted norms due to different
prompt designs.
Data use and availability
Bollywood subtitles were scraped from a website
called www.bollynook.com and Hollywood subti-
tles are taken from publicly available Kaggle movie
subtitles datasets. We will only release dialogue ex-
cerpts related to shame and pride. We have around
7.5k such instances in Bollywood and almost 2.8k
in Hollywood. Under the interpretation of fair use
in research, this makes up a very small portion
of dialogues taken from Bollywood (i.e. almost
3 samples (5 lines long) per movie on average)
and Hollywood (about 1 sample (5 lines long) per
movie on average).
Acknowledgements
This work was supported in part by the Penn Global
Engagement Research Fund. We acknowledge the
use of ChatGPT, an AI language model developed
by OpenAI, for its assistance with writing.
References
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama
Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
Diogo Almeida, Janko Altenschmidt, Sam Altman,
Shyamal Anadkat, et al. 2023. Gpt-4 technical report.
arXiv preprint arXiv:2303.08774.
Todd Adkins and Jeremiah J Castle. 2014. Moving
pictures? experimental evidence of cinematic influ-
ence on political attitudes. Social Science Quarterly,
95(5):1230–1244.
Emily T Amanatullah and Michael W Morris. 2010.
Negotiating gender roles: Gender differences in as-
sertive negotiating are mediated by women’s fear of
backlash and attenuated when negotiating on behalf
of others. Journal of personality and social psychol-
ogy, 98(2):256.
Sophie H Arnold and Katherine McAuliffe. 2021. Chil-
dren show a gender gap in negotiation. Psychological
Science, 32(2):153–158.
Mohammad Atari, Mona J Xue, Peter S Park, Damián
Blasi, and Joseph Henrich. 2023. Which humans?
Working paper.
GA Barnard. 1947. Significance tests for 2× 2 tables.
Biometrika, 34(1/2):123–138.
Syon P Bhanot. 2021. Isolating the effect of injunctive
norms on conservation behavior: New evidence from
a field experiment in california. Organizational Be-
havior and Human Decision Processes, 163:30–42.
Michael Boiger, Simon De Deyne, and Batja Mesquita.
2013. Emotions in “the world”: cultural practices,
products, and meanings of anger and shame in two in-
dividualist cultures. Frontiers in psychology, 4:867.
Jacopo Bonan, Cristina Cattaneo, Giovanna d’Adda,
and Massimo Tavoni. 2020. The interaction of de-
scriptive and injunctive social norms in promoting
energy conservation. Nature Energy, 5(11):900–909.
Ryan L Boyd, Ashwini Ashokkumar, Sarah Seraj, and
James W Pennebaker. 2022. The development and
psychometric properties of liwc-22. Austin, TX: Uni-
versity of Texas at Austin, pages 1–47.
Federica Caffaro, Federico Ferraris, and Susanna
Schmidt. 2014. Gender differences in the perception
of honour killing in individualist versus collectivistic
cultures: Comparison between italy and turkey. Sex
roles, 71(9):296–318.
Sky CH-Wang, Arkadiy Saakyan, Oliver Li, Zhou Yu,
and Smaranda Muresan. 2023. Sociocultural norm
similarities and differences via situational alignment
and explainable textual entailment. arXiv preprint
arXiv:2305.14492.
Myra Cheng, Tiziano Piccardi, and Diyi Yang. 2023.
Compost: Characterizing and evaluating caricature
in llm simulations. arXiv preprint arXiv:2310.11501.

--- Page 10 ---

Robert B Cialdini, Raymond R Reno, and Carl A Kall-
gren. 1990. A focus theory of normative conduct:
Recycling the concept of norms to reduce littering
in public places. Journal of personality and social
psychology, 58(6):1015.
Dov Cohen. 2003. The american national conversation
about (everything but) shame. Social Research: An
International Quarterly, 70(4):1075–1108.
Taya R Cohen, Scott T Wolf, Abigail T Panter, and
Chester A Insko. 2011. Introducing the gasp scale: a
new measure of guilt and shame proneness. Journal
of personality and social psychology, 100(5):947.
Dorottya Demszky, Dana Movshovitz-Attias, Jeongwoo
Ko, Alan Cowen, Gaurav Nemade, and Sujith Ravi.
2020. Goemotions: A dataset of fine-grained emo-
tions. arXiv preprint arXiv:2005.00547.
Tamara J Ferguson and Heidi L Eyre. 2000. Engender-
ing gender differences in shame and guilt: Stereo-
types, socialization, and situational pressures. Gen-
der and emotion, page 254.
D Fessler. 2007. From appeasement to conformity. Self-
conscious emotions: Theory and research, pages 174–
193.
Kurt W Fischer and June Price Tangney. 1995. Self-
conscious emotions and the affect revolution: Frame-
work and overview. Self-conscious emotions: The
psychology of shame, guilt, embarrassment, and
pride, pages 3–22.
Yi R Fung, Tuhin Chakraborty, Hao Guo, Owen
Rambow, Smaranda Muresan, and Heng Ji. 2022.
Normsage: Multi-lingual multi-cultural norm discov-
ery from conversations on-the-fly. arXiv preprint
arXiv:2210.08604.
Sergey Gavrilets. 2020. The dynamics of injunctive
social norms. Evolutionary Human Sciences, 2:e60.
Jennifer L Goetz and Dacher Keltner. 2007. Shifting
meanings of self-conscious emotions across cultures.
The self-conscious emotions: Theory and research,
pages 153–173.
Shreya Havaldar, Matthew Pressimone, Eric Wong, and
Lyle Ungar. 2023a. Comparing styles across lan-
guages. In Proceedings of the 2023 Conference on
Empirical Methods in Natural Language Processing,
pages 6775–6791, Singapore. Association for Com-
putational Linguistics.
Shreya Havaldar,
Sunny Rai,
Bhumika Singhal,
Langchen Liu, Sharath Chandra Guntuku, and Lyle
Ungar. 2023b. Multilingual language models are
not multicultural: A case study in emotion.
In
WASSA’2023, ACL.
Liwei Jiang, Jena D Hwang, Chandra Bhagavatula, Ro-
nan Le Bras, Maxwell Forbes, Jon Borchardt, Jenny
Liang, Oren Etzioni, Maarten Sap, and Yejin Choi.
2021. Delphi: Towards machine ethics and norms.
arXiv preprint arXiv:2110.07574.
Kunal Khadilkar, Ashiqur R KhudaBukhsh, and Tom M
Mitchell. 2022. Gender bias, social bias, and rep-
resentation in bollywood and hollywood. Patterns,
3(2).
Sangmoon Kim, Ryan Thibodeau, and Randall S Jor-
gensen. 2011. Shame, guilt, and depressive symp-
toms: a meta-analytic review. Psychological bulletin,
137(1):68.
Erik O Kimbrough and Alexander Vostroknutov. 2023.
A theory of injunctive norms. Available at SSRN
3566589.
Tina Kubrak. 2020. Impact of films: Changes in young
people’s attitudes after watching a movie. Behavioral
sciences, 10(5):86.
Michael Lewis, Kiyoko Takai-Kawakami, Kiyobumi
Kawakami, and Margaret Wolan Sullivan. 2010. Cul-
tural differences in emotional responses to success
and failure. International journal of behavioral de-
velopment, 34(1):53–61.
Nangyeon Lim. 2016. Cultural differences in emotion:
differences in emotional arousal level between the
east and the west. Integrative medicine research,
5(2):105–109.
Li Lucy and David Bamman. 2021. Gender and repre-
sentation bias in gpt-3 generated stories. In Proceed-
ings of the Third Workshop on Narrative Understand-
ing, pages 48–55.
Maxime Mauduy, Daniel Priolo, Nicolas Margas, and
Cécile Sénémeaud. 2022. When combining injunc-
tive and descriptive norms strengthens the hypocrisy
effect: A test in the field of discrimination. Frontiers
in Psychology, 13:989599.
Alexander Pan, Jun Shern Chan, Andy Zou, Nathaniel
Li, Steven Basart, Thomas Woodside, Hanlin Zhang,
Scott Emmons, and Dan Hendrycks. 2023. Do the
rewards justify the means? measuring trade-offs be-
tween rewards and ethical behavior in the machiavelli
benchmark. In International Conference on Machine
Learning, pages 26837–26867. PMLR.
Tom Pyszczynski, Jeff Greenberg, Sheldon Solomon,
Jamie Arndt, and Jeff Schimel. 2004. Why do people
need self-esteem? a theoretical and empirical review.
Psychological bulletin, 130(3):435.
Nils Reimers and Iryna Gurevych. 2019. Sentence-bert:
Sentence embeddings using siamese bert-networks.
In Proceedings of the 2019 Conference on Empirical
Methods in Natural Language Processing and the 9th
International Joint Conference on Natural Language
Processing (EMNLP-IJCNLP), pages 3982–3992.
Yarik Menchaca Resendiz and Roman Klinger. 2023.
Affective natural language generation of event de-
scriptions through fine-grained appraisal conditions.
INLG 2023, page 375.

--- Page 11 ---

Rebecca L Schaumberg and Samuel E Skowronek. 2022.
Shame broadcasts social norms: The positive social
effects of shame on norm acquisition and normative
behavior. Psychological Science, 33(8):1257–1277.
Shalom H Schwartz. 2012. An overview of the schwartz
theory of basic values. Online readings in Psychol-
ogy and Culture, 2(1):11.
Zeerak Talat, Hagen Blix, Josef Valvoda, Maya Indira
Ganesh, Ryan Cotterell, and Adina Williams. 2021.
A word on machine ethics: A response to jiang et
al.(2021). arXiv preprint arXiv:2111.04158.
June P Tangney, Patricia Wagner, and Richard Gramzow.
1992. Proneness to shame, proneness to guilt, and
psychopathology. Journal of abnormal psychology,
101(3):469.
Petter Törnberg. 2023. Chatgpt-4 outperforms experts
and crowd workers in annotating political twitter
messages with zero-shot learning. arXiv preprint
arXiv:2304.06588.
Harry Triandis. 1988. Collectivism v. individualism:
A reconceptualisation of a basic concept in cross-
cultural social psychology. In Cross-cultural studies
of personality, attitudes and cognition, pages 60–95.
Springer.
Harry C Triandis. 1989. The self and social behavior
in differing cultural contexts. Psychological review,
96(3):506.
Enrica Troiano, Sebastian Padó, and Roman Klinger.
2019. Crowdsourcing and validating event-focused
emotion corpora for german and english. In Proceed-
ings of the 57th Annual Meeting of the Association
for Computational Linguistics, pages 4005–4011.
Maximilian Wegge, Enrica Troiano, Laura Ana Maria
Oberlaender, and Roman Klinger. 2022. Experiencer-
specific emotion and appraisal prediction. In Pro-
ceedings of the Fifth Workshop on Natural Language
Processing and Computational Social Science (NLP+
CSS), pages 25–32.
Ying Wong and Jeanne Tsai. 2007. Cultural models
of shame and guilt. The self-conscious emotions:
Theory and research, 209:223.
Frank Yates. 1934. Contingency tables involving small
numbers and the χ 2 test. Supplement to the Journal
of the Royal Statistical Society, 1(2):217–235.

--- Page 12 ---

A
Appendix
A.1
Search Keywords
Search keywords defined in Table A1 were used to extract shame- and pride-related dialogues from
Bollywood and Hollywood movie subtitles.
Lemma
Word forms
shame
shame, shamed, shameful, ashamed
pride
proud, prouder, proudly, pride
Table A1: List of search keywords for extracting dialogues.
A.2
Examining Implicit shame
We prompted GPT-4 chat to identify (a) if a given discourse expresses shame, and (b) identify the
behavior or action behind shame, for a randomly sampled set of 100 samples without explicit mentions
of shame/pride each from Hollywood and Bollywood. We asked two human annotators to evaluate the
correctness of GPT-4 chat-generated outputs. See Table A4 for annotation guidelines.
A.3
Prompts
The prompts designed to extract the subject experiencing shame and pride, their gender, and the reason
behind the emotions are provided in Tables A2 and A3.
Prompts for norm discovery in Bollywood movie dialogues
"You are an experienced social scientist and you study Indian society. Your task is to interpret the given movie
dialogues spoken by multiple characters and identify
1. Who is feeling proud? Provide the gender. If agent or gender is not explicit, use the pronouns, name, and
salutations to guess agent and gender.
2. Identify the reason behind feeling proud. If not explicit, return NA.
The answer should be short and in below CSV format. <who_proud, gender, reason>
Input: Your mother had already given up on me because I was useless hopeless But you were the apple of her
eye My child will make me proud look after me He’ll support in my old-age But this kid left her all alone.
Output: mother, male, provide care for old parents
Input: I’ve heard there’s a promising young student in your school What’s his name? He’s made us proud in long
jump, we are here to felicitate him Call him Show yourself, Raju Tempre
Output: authority, NA, Sports achievement"
"You are an experienced social scientist and you study Indian society. Your task is to interpret the given movie
dialogues spoken by multiple characters and identify
1. Who is being shamed? Predict the gender. If gender is not explicit, use the pronouns, name, and salutations
to guess gender.
2. Identify the primary reason for shaming. If not explicit, return NA.
The answer should be short and in CSV format. < who_shame, gender, reason>
Input: And should we bow before others begging....them to marry our daughters? This shall not happen. Neither
will the girls be alive here nor shall....we be ashamed of ourselves. You cannot kill the life which God has given.
I won’t let you commit the sin.
Output: girl’s parent, NA, not able to marry off their daughters
Input: Black marketers are now in the open. And the thieves too Politics is in a great mess Shame on this system.
There’s no democracy Get rid of these politicians The gong has struck..”Our hearts are swaying to it’s beats”
Output: System, NA, poor law and regulations"
Table A2: Bollywood: Prompts for norm discovery using GPT-4 Chat. The temperature was set to 0 to minimize
randomness.
A.3.1
Annotation
The annotation guidelines to verify the gender predicted by GPT-4 and the correctness of the reason are
provided in Table A4. The annotators for Bollywood set and Hollywood set were Indian and American
respectively. Both annotators were female, proficient in English language, and well-versed with social
norms. During annotation, if the gender or the reason is unclear, the annotators were asked to label "not

--- Page 13 ---

Prompts for norm discovery in Hollywood movie dialogues
"You are an experienced social scientist and you study American society. Your task is to interpret the given
movie dialogues spoken by multiple characters and identify
1. Who is feeling proud? Provide the gender. If agent or gender is not explicit, use the pronouns, name, and
salutations to guess agent and gender.
2. Identify the reason behind feeling proud? If not explicit, return NA.
The answer should be short and in below CSV format. <who_proud, gender, reason>
Input: I want to go to Worlds and win gold. I want to go to the 88 Olympics in Seoul and win gold. Good! I’m
proud of you. Are you getting the support that you need? What do you mean sir?
Output: Sir, male, winning olympic gold
Input: Yes. Yes, I did. I promise, this time I really got the promotion. - I’m proud of you, son. - Thank you, sir.
Excuse me. Hi, sweetheart.
Output: father, male, for getting the promotion"
"You are an experienced social scientist and you study American society. Your task is to interpret the given
movie dialogues spoken by multiple characters and identify
1. Who is being shamed? Predict the gender. If gender is not explicit, use the pronouns, name, and salutations
to guess gender.
2. Identify the primary reason for shaming. If not explicit, return NA.
The answer should be short and in CSV format. < who_shame, gender, reason>
Input: You still owe me 100. Remember? You stiffed Donny for 100 bucks? Cheapskate. Shame on you. Pay
this man his C-note. Now I know why they call you the Snake.
Output: NA, male, not returning borrowed money
Input: You prey on your own people. You steal from your own people. Have you no shame!? - Huh? - Well,
we’re still here. Man: Mr. Markopolos, it’s all yours.
Output: Snake, male, stealing and preying on people"
Table A3: Hollywood: Prompts for norm discovery using GPT-4 Chat. The temperature was set to 0 to minimize
randomness.
Guidelines for Manual Evaluation
Step-1. Read the conversation and identify the person feeling ashamed (or being shamed) or
proud.
Step-2. Identify the gender. Check gender markers such as Mr/Mrs., s/he, him/her, etc. If
the name is provided in the conversation, check if the name is likely to be a male name or
female. If not clear, mark "not explicit".
Step-3. Read the reason behind shame/pride. Compare with conversation and determine if
the provided reason is the cause for shame/pride.
Table A4: Guidelines for Annotation
explicit". We only considered the cases where the gender was predicted to be either male or female. The
task is objective and inter-annotator agreement was not computed. The annotators volunteered for the task
and were not provided monetary compensation.
A.4
LIWC Correlation Results
Tables A7, A8, A9 and A10 contain positively correlated (p < 0.05) LIWC categories, the most frequent
five words for each category, Pearson r and confidence interval.
A.5
Clustering Results
Tables A13 and A14 contain the manually annotated Cluster Themes, the total number of samples in each
cluster, and Bollywood vs Hollywood distribution. The distance was set to 5 and the duplicates were
removed. The theme and top three examples demonstrating its meaning are provided in Tables A11 and
A12.

--- Page 14 ---

Gender Evaluation
Incorrect
Ambiguous
Bollywood
8
15 (3 Female)
Hollywood
5
10 (3 Female)
Social Norms/Reason Evaluation
Incorrect
Ambiguous
Bollywood
11
9
Hollywood
2
1
Table A5: Manual Evaluation of predicted gender and reasons for randomly sampled 100 samples each from
Bollywood and Hollywood.
Bollywood
mastering a trick
fulfilling father’s dreams
provide care for old parents
fiancee’s physical appearance
his wealth
Hollywood
for being a hard worker regardless of the task
being a brilliant student
winning Olympic gold
achievements and growth
coming out as queer
Table A6: A subset of reasons extracted from movie dialogues expressing pride. A total of 3163 unique reasons
(Bollywood-1589, Hollywood-1574) were extracted.
LIWC Categories
Top-5 words
r
p-value
95% CI
Negative emotions (EMO_NEG)
(bad, mad, scared, worry, fear)
0.330
0.000
[0.315, 0.344]
Negative tone (TONE_NEG)
(lost, kill, wrong, bad, hit)
0.249
0.000
[0.233, 0.265]
POWER
(sir, respect, own, kill, poor)
0.198
0.000
[0.182, 0.214]
EMOTION
(love, good, bad, happy, crazy)
0.168
0.000
[0.152, 0.185]
2nd person pronouns (YOU)
(you, your, you’re, yourself, you’ve)
0.161
0.000
[0.145, 0.178]
Social references (SOCREFS)
(you, your, he, her, him)
0.148
0.000
[0.132, 0.165]
FEELING
(feel, touch, feeling, felt, hard)
0.133
0.000
[0.117, 0.150]
DRIVES
(we, our, us, sir, married)
0.115
0.000
[0.098, 0.132]
SOCIAL
(you, your, he, her, him)
0.110
0.000
[0.094, 0.127]
MORAL
(wrong, innocent, duty, decent, excuse)
0.102
0.000
[0.085, 0.118]
AFFECT
(love, good, keep, respect, well)
0.078
0.000
[0.062, 0.095]
NEGATE
(not, don’t, no, aren’t, won’t)
0.065
0.000
[0.049, 0.082]
FEMALE
(her, she, girl, she’s, mom)
0.060
0.000
[0.043, 0.077]
Personal Pronouns (PPRON)
(you, i, me, your, my)
0.058
0.000
[0.041, 0.075]
FAMILY
(son, married, uncle, dad, mom)
0.055
0.000
[0.039, 0.072]
Preposition (PREP)
(to, of, in, for, on)
0.053
0.000
[0.037, 0.070]
SEXUAL
(chaste, lust, sex, sexy, pimp)
0.051
0.000
[0.034, 0.067]
PRONOUN
(you, i, me, your, my)
0.040
0.000
[0.023, 0.057]
Auxiliary verbs (AUXVERB)
(is, are, have, be, don’t)
0.029
0.001
[0.013, 0.046]
CONFLICT
(kill, killed, accusing, killing, cruel)
0.024
0.007
[0.007, 0.041]
SWEAR
(hell, bloody, idiot, damn, ass)
0.024
0.007
[0.007, 0.041]
Anger (EMO_ANGER)
(mad, angry, hate, cruel, argue)
0.022
0.015
[0.005, 0.039]
FOCUSPRESENT
(is, are, don’t, i’m, aren’t)
0.021
0.018
[0.005, 0.038]
Table A7: Psychosocial categories positively correlated (p < 0.05) with shame in Bollywood. p-values were
corrected using Benjamini-Hochberg correction. The categories are arranged in decreasing order of correlation.

--- Page 15 ---

LIWC Categories
Top-5 words
r
p-value
95% CI
DRIVES
(we, our, us, sir, work)
0.122
0.000
[0.104,0.140]
Determiner (DET)
(the, a, my, your, that)
0.101
0.000
[0.082,0.119]
ACHIEVE
(work, better, win, best, try)
0.098
0.000
[0.080,0.116]
POWER
(sir, own, respect, kill, power)
0.091
0.000
[0.072,0.109]
Social References (SOCREFS)
(you, your, he, we, our)
0.085
0.000
[0.067,0.103]
Preposition (PREP)
(of, to, in, for, with)
0.084
0.000
[0.066,0.103]
MORAL
(wrong, duty, brave, arrogant, useless)
0.075
0.000
[0.057,0.093]
Conjunction (CONJ)
(and, but, so, if, as)
0.075
0.000
[0.056,0.093]
REWARD
(win, won, glory, success, successful)
0.071
0.000
[0.052,0.089]
Positive tone (TONE_POS)
(love, good, thank, well, great)
0.064
0.000
[0.046,0.082]
POLITIC
(nation, army, sultan, president, dynasty)
0.064
0.000
[0.045,0.082]
WE
(we, our, us, we’ll, let’s)
0.060
0.000
[0.042,0.079]
SOCIAL
(you, your, he, we, our)
0.060
0.000
[0.041,0.078]
FAMILY
(son, papa, married, dad, uncle)
0.059
0.000
[0.041,0.078]
AFFILIATION
(we, our, us, dear, we’ll)
0.059
0.000
[0.041,0.077]
FEELING
(feel, feeling, hard, felt, sense)
0.055
0.000
[0.036,0.073]
ETHNICITY
(indian, indians, british, hindi, caste)
0.054
0.000
[0.036,0.072]
MALE
(he, his, him, son, sir)
0.054
0.000
[0.036,0.072]
CULTURE
(indian, nation, army, car, indians)
0.044
0.000
[0.026,0.062]
AFFECT
(love, good, thank, well, great)
0.040
0.000
[0.021,0.058]
ARTICLE
(the, a, an, that)
0.039
0.000
[0.021,0.058]
Personal Pronouns (PPRON)
(you, i, my, your, me)
0.036
0.000
[0.017,0.054]
PROSOCIAL
(thank, please, sorry, respect, gift)
0.032
0.001
[0.014,0.051]
FUNCTION
(you, the, i, of, to)
0.032
0.001
[0.013,0.050]
2nd person pronouns (YOU)
(you, your, you’re, you’ve, you’ll)
0.030
0.003
[0.011,0.048]
THEY
(they, their, them, they’re, they’ll)
0.029
0.003
[0.011,0.048]
CERTITUDE
(really, real, surely, proved, actually)
0.021
0.041
[0.002,0.039]
Positive Emotion (EMO_POS)
(love, good, happy, happiness, smile)
0.020
0.049
[0.001,0.038]
Table A8: Psychosocial categories positively correlated (p < 0.05) with pride in Bollywood. p-values were
corrected using Benjamini-Hochberg correction. The categories are arranged in decreasing order of correlation.
LIWC Categories
Top-5 words
r
p
95% CI
Negative emotions (EMO_NEG)
(sick, pain, fear, bad, afraid)
0.425
0.000
[0.403, 0.446]
Negative tone (TONE_NEG)
(lost, wrong, sick, pain, poor)
0.355
0.000
[0.331, 0.377]
EMOTION
(good, love, sick, pain, bad)
0.290
0.000
[0.266, 0.314]
POWER
(own, sir, poor, killed, war)
0.263
0.000
[0.238, 0.287]
AFFECT
(well, good, love, help, damn)
0.168
0.000
[0.142, 0.193]
DRIVES
(we, us, our, work, we’re)
0.152
0.000
[0.127, 0.178]
FUNCTION
(you, i, the, to, of)
0.131
0.000
[0.105, 0.157]
Personal Pronouns (PPRON)
(you, i, me, i’m, my)
0.111
0.000
[0.085, 0.137]
MORAL
(wrong, excuse, decent, honest, duty)
0.110
0.000
[0.084, 0.136]
1st person sing. pronouns (I)
(i, me, i’m, my, i’ll)
0.102
0.000
[0.076, 0.128]
Sadness (EMO_SAD)
(crying, cry, sob, lonely, sad)
0.096
0.000
[0.070, 0.122]
NEGATE
(no, not, don’t, nothing, never)
0.090
0.000
[0.063, 0.116]
Preposition (PREP)
(to, of, in, for, on)
0.089
0.000
[0.062, 0.115]
PRONOUN
(you, i, that, it, me)
0.088
0.000
[0.062, 0.114]
YOU
(you, your, you’re, yourself, you’ve)
0.080
0.000
[0.054, 0.106]
Auxiliary verb (AUXVERB)
(be, i’m, is, was, have)
0.077
0.000
[0.051, 0.103]
FOCUSPAST
(was, did, were, been, didn’t)
0.069
0.000
[0.043, 0.096]
SOCIAL
(you, your, we, he, you’re)
0.060
0.000
[0.033, 0.086]
Conjunction (CONJ)
(and, so, but, if, when)
0.056
0.000
[0.030, 0.082]
LINGUISTIC
(you, i, the, to, of)
0.056
0.000
[0.030, 0.082]
ALLNONE
(no, all, nothing, never, yes)
0.055
0.000
[0.029, 0.081]
FAMILY
(son, dad, baby, mom, mama)
0.054
0.000
[0.028, 0.081]
Social references (SOCREFS)
(you, your, we, he, you’re)
0.050
0.000
[0.024, 0.077]
Anxiety (EMO_ANX)
(fear, afraid, worry, terrified, scared)
0.042
0.004
[0.015, 0.068]
ILLNESS
(sick, pain, pains, flu, sickly)
0.038
0.010
[0.012, 0.064]
FEELING
(feel, felt, pain, feeling, hard)
0.035
0.020
[0.008, 0.061]
Anger (EMO_ANGER)
(hate, hated, mad, angry, hates)
0.033
0.026
[0.007, 0.059]
DIFFER
(not, but, if, didn’t, or)
0.033
0.027
[0.007, 0.059]
Discrepancy (DISCREP)
(should, can, would, can’t, want)
0.032
0.029
[0.006, 0.059]
COGNITION
(no, not, all, know, but)
0.032
0.033
[0.005, 0.058]
Table A9: Psychosocial categories positively correlated (p<0.05) with shame in Hollywood. p-values were corrected
using Benjamini-Hochberg correction. The categories are arranged in decreasing order of correlation.

--- Page 16 ---

LIWC Categories
Top-5 words
r
p-value
95% CI
Personal Pronouns (PPRON)
(you, i, i’m, me, my)
0.135
0.000
[0.113,0.158]
Social References (SOCREFS)
(you, your, we, he, you’re)
0.131
0.000
[0.108,0.154]
FAMILY
(son, dad, baby, mom, mama)
0.121
0.000
[0.099,0.144]
Conjunction (CONJ)
(and, so, but, as, if)
0.114
0.000
[0.091,0.137]
SOCIAL
(you, your, we, he, you’re)
0.102
0.000
[0.079,0.125]
FUNCTION
(you, i, the, of, to)
0.100
0.000
[0.077,0.123]
1st person sing. pronouns (I)
(i, i’m, me, my, i’ll)
0.095
0.000
[0.072,0.118]
YOU
(you, your, you’re, you’ve, yourself)
0.091
0.000
[0.068,0.114]
MALE
(he, his, him, man, son)
0.084
0.000
[0.061,0.107]
DRIVES
(we, our, us, we’re, dad)
0.076
0.000
[0.053,0.099]
Positive tone (TONE_POS)
(good, well, thank, great, love)
0.072
0.000
[0.049,0.095]
PRONOUN
(you, i, i’m, that, it)
0.072
0.000
[0.048,0.095]
Auxiliary Verb (AUXVERB)
(i’m, be, is, was, have)
0.071
0.000
[0.048,0.094]
Positive Emotion (EMO_POS)
(good, love, happy, hope, wonderful)
0.070
0.000
[0.047,0.093]
Preposition (PREP)
(of, to, in, for, on)
0.070
0.000
[0.047,0.093]
AFFILIATION
(we, our, us, we’re, dad)
0.054
0.000
[0.031,0.078]
EMOTION
(good, love, happy, hope, bad)
0.052
0.000
[0.029,0.075]
ETHNICITY
(american, irish, chinese, german, christian)
0.052
0.000
[0.029,0.075]
REWARD
(win, won, winner, successful, earned)
0.048
0.000
[0.025,0.071]
ACHIEVE
(work, better, best, trying, try)
0.045
0.000
[0.022,0.068]
POWER
(sir, own, war, strong, mighty)
0.044
0.001
[0.021,0.067]
AFFECT
(good, well, thank, great, love)
0.041
0.001
[0.018,0.064]
MORAL
(wrong, excuse, hero, brave, dignity)
0.040
0.002
[0.017,0.064]
FEMALE
(her, she, she’s, girl, ladies)
0.034
0.009
[0.011,0.057]
CULTURE
(american, car, president, nation, mayor)
0.033
0.012
[0.009,0.056]
FOCUSPAST
(was, did, been, were, had)
0.032
0.013
[0.009,0.055]
SHEHE
(he, his, him, her, she)
0.031
0.016
[0.008,0.054]
WORK
(work, job, school, deal, company)
0.028
0.033
[0.005,0.051]
Table A10: Psychosocial categories positively correlated (p<0.05) with pride in Hollywood. p-values were corrected
using Benjamini-Hochberg correction. The categories are arranged in decreasing order of correlation.
(a) Pride-related norms in Bollywood
(b) Pride-related norms in Hollywood
Figure A1: Gender-wise differences in themes associated with normative expectations from pride-related discourse
in Bollywood and Hollywood. ∆(Female −Male) is the difference between normalized dialogues attributed
to females under a theme and to males under the same theme (as in eq. 1 but for dimension gender). ∗indicates
significant difference i.e., p < 0.05

--- Page 17 ---

Theme
Examples from cluster
Stealing
shamelessness and taking money, lying and misusing money, Stealing and bribery
Poverty
not having money, being poor, living in poor conditions
Incompetence
not fulfilling responsibilities, not meeting expectations or making a mistake, Failure
or perceived incompetence
Promiscuity
being promiscuous, Having a love affair, shameless behavior and expressing love
Inappropriate social behavior
not living up to someone’s expectations, being disloyal, Being rude and ungrateful
Disobedience
not upholding cultural values, disobedience or lack of respect, being disloyal
Parent-related
not standing up for his mother, not taking care of his father, not taking responsibility
for his son
Marriage-related
refusing to marry, being forced into marriage, not accepting the proposed marriage
Immodesty
Wearing inappropriate clothes, inappropriate behavior nudity in public, behaving
indecently in public
Gender Roles
not behaving as per her husband’s expectations, behaving inappropriately in front of
her daughter, going against her husband
Sexual Harassment
assaulting a girl, physical assault on women, sexual assault
Cowardice
lack of courage, cowardice and inability to stand up for oneself, lack of pride and
integrity
Alcoholism
excessive drinking, inappropriate behavior due to alcohol, drinking and irresponsible
behavior
Non-conformity
not conforming to gender norms, breaking gender norms, behaving inappropriately
according to societal norms
Illegal activities
engaging in criminal activities, Being a criminal, committing illegal acts
Betrayal
Betrayal or dishonesty, betrayal and infidelity, Deception/Betrayal
Lack of accountability
not taking responsibility and blaming others, wrongdoing without remorse, not
acknowledging wrongdoing
Disrespect
disrespecting others, disrespecting an authority figure, Disrespectful and inappropri-
ate behavior
Harm
causing harm to others, committing harmful deeds, causing trouble and endangering
others
Lying/Deception
lying and hiding information, Lying or deceit, Deception/Not being truthful
Inappropriate sexual behavior
inappropriate advances and comments, inappropriate behavior towards a young girl,
inappropriate language and behavior
Social Etiquette
Being humiliated in public, being disrespected and belittled, being mocked and
treated shamefully
Privacy-related
invading personal space, invading someone’s privacy, intrusion of personal space,
trespassing/invading personal space
Accusation
accused of wrongdoing, being accused of something, being accused of infidelity
Family norms
Disrespecting family, causing harm and shame to family, causing difficulty and
shame to family
Lack of shame
perceived shamelessness, being perceived as shameless, feeling embarrassed and
ashamed
Table A11: Themes (n = 26) and top-3 examples for clusters obtained after agglomerative clustering of shame-
related dialogues from Bollywood and Hollywood. The cluster Lack of shame was removed since the reason behind
shame was not evident. Clusters Lack of accountability and Inappropriate social behavior were merged together
(and named “Lack of accountability”) due to overlapping normative expectations.

--- Page 18 ---

Theme
Examples from cluster
Achievement
being a brilliant student, working hard and achieving a spectacular result, professional
achievement
Family Roles
raising their child, having an unselfish mother, having a simple and good daughter
Self-identity
being a man, being a woman, being gay
Duty
fulfilling duty, Accomplishing something great, saving the world
Bravery
bravery and sacrifice, bravery and service to nation, bravery and selflessness
Nation
saving the country’s pride, making country proud, Making country proud
Doing the "right" thing
for doing the right thing, for being heroes, for having courage
Son’s achievements
son’s success and progress, son’s hard work and achievement, son’s determination
Family Honor
maintaining dignity and pride, taking care of family pride, saving family’s pride
Justice
standing up for justice, fighting for justice, bringing justice
Wedding
marrying with pride and respect, sister’s marriage, daughter’s marriage into a reputed
family
Physical Appearance & Assets
his manhood, his wealth and beautiful wife, his knowledge and power
Resilience
resilience and determination, overcoming struggles, enduring hardships without
complaint
Winning
Sports achievement, working hard and achieving a spectacular result, winning some-
thing
Ethnolinguistic Identity
being Indian, defending the pride of Rajputs, being a Maharashtrian
Table A12: Themes (n = 15) and top-3 examples for clusters obtained after agglomerative clustering of pride-related
dialogues from Bollywood and Hollywood.
Theme (Shame-related norms)
Total Samples
Hollywood
Bollywood
Lack of Accountability
802
185
617
Accusation
70
0
70
Alcoholism
98
18
80
Betrayal
262
26
236
Cowardice
209
51
158
Disobedience
216
49
167
Disrespect
246
26
220
Family norms
203
24
179
Gender roles
221
17
204
Harm
225
64
161
Illegal activities
253
27
226
Immodesty
311
58
253
Incompetence
342
83
259
Lying/Deception
222
53
169
Marriage-related
179
25
154
Non-conformity
208
28
180
Parent-related
263
34
229
Poverty
414
108
306
Privacy-related
102
14
88
Promiscuity
595
89
506
Inappropriate Sexual behavior
407
33
374
Sexual Harassment
232
24
208
Social Etiquette
417
97
320
Stealing
351
49
302
Total
6848
1182
5666
Table A13: Distribution of reasons (shame) across manually labeled clusters. A total of twenty-six clusters were
generated with distance=5. Duplicates were removed for clustering. One cluster with generic reasons ( such as
phrases "lack of shame") was removed and two clusters with similar reasons (related to accountability) were merged.
Finally, 24 clusters were considered. The total is slightly more than numbers in Table 3 since a reason could be
mapped to multiple clusters.

--- Page 19 ---

Theme (Pride-related norms)
Total Samples
Hollywood
Bollywood
Achievement
332
174
158
Bravery
248
69
179
Doing the "right" thing
82
82
0
Duty
792
449
343
Ethnolinguistic Identity
148
7
141
Family Honor
263
77
186
Family Roles
356
156
200
Justice
255
109
146
Nation
216
57
159
Physical Appearance
106
49
57
Resilience
180
68
112
Self-identity
273
157
116
Son’s Achievements
315
87
228
Wedding
120
23
97
Winning
411
205
206
Total
4097
1769
2328
Table A14: Distribution of reasons (pride) across manually labeled clusters. A total of fifteen clusters were generated
with distance=5. The total is slightly more than the numbers in Table 3 since a reason could be mapped to multiple
clusters
Theme
Statistic
p-value
Inappropriate Sexual behavior
5.0380
0.00001
Gender roles
3.8262
0.0006
Betrayal
3.2044
0.001
Illegal activities
2.8258
0.005
Disrespect
2.8284
0.005
Sexual Harassment
2.8358
0.005
Promiscuity
1.5553
0.1
Accusation
3.8411
0.0006
Stealing
1.6798
0.09
Parent-related
1.8961
0.06
Family norms
2.0813
0.04
Non-conformity
1.4724
0.1
Marriage-related
1.1817
0.2
Privacy-related
0.9518
0.3
Alcoholism
-0.2920
0.8
Immodesty
-0.6634
0.5
Disobedience
-2.1438
0.03
Lying/Deception
-2.6508
0.008
Cowardice
-2.7746
0.006
Incompetence
-3.5187
0.002
Social Etiquette
-3.3461
0.002
Harm
-4.5140
0.00009
Poverty
-4.9028
0.00002
Lack of accountability
-4.6312
0.00007
Table A15: Barnard Exact test with Yates correction for testing statistically significant occurrence of shame-related
themes in Bollywood and Hollywood.

--- Page 20 ---

Theme
Statistic
p-value
Ethnolinguistic Identity
9.6185
0.0000
Son’s Achievements
5.8025
0.0000
Bravery
5.0368
0.0000
Family Honor
4.7046
0.0000
Nation
5.1183
0.0000
Wedding
5.3898
0.0000
Resilience
1.4959
0.1370
Justice
0.1441
0.8963
Family Roles
-0.2560
0.8024
Physical Appearance
-0.6420
0.5223
Winning
-2.8913
0.0038
Achievement
-3.5425
0.0004
Self-identity
-4.9482
0.0000
Doing the "right" thing
-10.4936
0.0000
Duty
-8.5488
0.0000
Table A16: Barnard Exact test with Yates correction for testing statistically significant occurrence of pride-related
themes in Bollywood and Hollywood.

```
