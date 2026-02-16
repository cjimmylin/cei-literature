---
title: "2025-Huang-Understanding Asian Stereotyping and Bias in LLMs Flora Huang - PDF Extract"
source_pdf: "2025-Huang-Understanding Asian Stereotyping and Bias in LLMs Flora Huang.pdf"
pages: 10
extracted_at: "2026-02-14T01:57:26.877761"
---

# PDF Extract: 2025-Huang-Understanding Asian Stereotyping and Bias in LLMs Flora Huang

**Source PDF:** 2025-Huang-Understanding Asian Stereotyping and Bias in LLMs Flora Huang.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

Understanding Asian Stereotyping and Bias in LLMs
Flora Huang
Stanford University
Department of Computer Science
flora221@stanford.edu
Abstract
In recent years, the advancements of large language
models (LLMs) have helped them become increasingly en-
trenched into our world. LLM assistance with processing
natural language tasks and generating text is now common-
place. However, despite their advancements, LLMs are crit-
ically flawed due to their internalization of social biases. As
a result, the use of LLMs may often spread or even amplify
issues such as racial bias and stereotyping. While racial
bias in LLMs have been well documented, there exists a
critical knowledge gap in understanding what stereotyping
or biases against specific ethnic groups are encoded into
LLMs. This paper will provide a deep dive into understand-
ing the extent and potential impact of Asian stereotyping in
popular LLM systems, through the use of experimentation
and surveying.
Overall, it was discovered that while many users of LLMs
have not reported encountering Asian stereotyping and/or
bias in their LLM usage, stereotyping and bias are still
prevalent in LLM systems. Qualitative studies of LLM re-
sponses found significant examples of Asian stereotyping,
with the “model minority” stereotype being most common.
Additionally, experiments also found that there exists a neg-
ative sentiment polarity gap for the Asian ethnic group com-
pared to the average, suggesting that LLMs have encoded
negative opinions/beliefs towards Asians. Finally, it was
discovered that LLMs tended to assign occupations with
higher income levels to people of Asian descent, potentially
at the expense of people from other ethnic groups. While
Asian stereotyping may not have been directly detected by
most users, it remains important to address this issue, es-
pecially as LLMs may amplify biases and wield an increas-
ingly large influence on our society, actions, and habits.
1. Introduction
Asian stereotyping has grown in recent years, in part
spurred on by racism related to COVID-19 [12,20]. Stereo-
typing of Asians has especially proliferated in digital
spaces, which has contributed to the entrenchment of bias
in large language models (LLMs), artificial intelligence pro-
grams that use machine learning to process human language
and text. These biased LLMs are then released for public
use, potentially proliferating anti-Asian sentiments.
1.1. Asian American Stereotyping and Digital
Spaces
In general, bias against people of Asian descent is the
most well documented in the Anglosphere, or in spaces
largely dominated by English language and cultural val-
ues [23]. Asian stereotyping typically falls into a few gen-
eral categories: being academically gifted, more “feminine”
or “submissive”, and a “forever foreigner”.
In general,
Asians and Asian-Americans are typically perceived as eco-
nomically successful and admired as a “model minorities”
in English-speaking countries such as the United States of
America [10, 26]. This often comes as an extension of the
academically gifted stereotype, one that Asians are “good
at math” and in general, academically inclined [29].
However, despite the model minority stereotype, Asian
people still often face the “forever foreigner” stereotype.
This stereotype implies that people of Asian descent are
unable to assimilate into Anglosphere communities [11,
26]. This stereotype was even more exacerbated after the
COVID-19 pandemic, where sentiments towards Asian peo-
ple became more negative [20, 25]. In a study of Asian
Americans during the context of the COVID-19 pandemic,
this “othering” bias and subsequent exclusion was most
pervasive among White-identifying Americans [12], fur-
ther emphasizing the prevalence of Asian stereotyping in
English-speaking communities.
Racial bias against Asians also continues in the digital
sphere. A sizeable proportion of internet communication
is done in English, especially on international platforms.
In fact, English-dominated digital spaces only account for
around 40% of the internet and a majority of internet users
are not native English speakers [27]. Digital platforms of-
ten represent “virtual breathing spaces” for minority lan-
guages, with independent digital spaces for many different

--- Page 2 ---

Figure 1.
Global Cumulative Asian Sentiment Scores (CASS)
across 20 countries from October 2019 to May 2020. Globally,
societal sentiments of Asians became more negative across 20
countries—a significant linear decline during the COVID-19 pan-
demic. CASS were trending neutral before the pandemic (October
to November 2019), and plummeted in February 2020. There-
after, CASS increased gradually, although it has not recovered
to prepandemic levels. Figure and caption directly sourced from
[25].
cultures and communities [5]. However, English is still of-
ten used as a common language on the internet, allowing
communication across international spaces versus domes-
tic ones [7]. As a result of being adopted as the language
for global audiences, with the use of English is often asso-
ciated with prestige [7], and non-native English speakers or
English non-speakers are often discriminated against in pre-
dominantly English speaking communities. With the spread
of English as the dominant international language for the in-
ternet, biases common in the Anglosphere have since also
proliferated in English-speaking digital spaces as well.
However, Asian stereotyping is not a blanket experience
for every person of Asian descent. Across the variety of
Asian cultures, structural and societal differences may lead
to unequal applications of racial stereotyping [6], with some
Asian cultures facing different stereotypes than those high-
lighted in this paper.
Additionally, differences in social
and financial standing may further affect their perception
of stereotyping.
1.2. Racial Bias in LLMs
Racial bias in LLMs has been a longstanding and well
established issue, often learning and perpetuating the social
biases inherent in their training datasets [15]. This is un-
surprising, as training corpora are typically drawn by con-
solidating text readily available on the internet, which itself
contains many examples of racial bias and stereotyping.
LLMs also tend to amplify learned biases through its ap-
plication as a system. For instance, LLMs built to make
hiring decisions have been demonstrated to act on their un-
derlying biases against people of colour [2,3]. When LLMs
Figure 2. An example of Asian stereotyping in an LLM. In this
case, the LLM used was the Llama-3.2-3B-Instruct-Turbo by Meta
[24], on the Together AI platform.
are harnessed to make medical decisions and to assist with
healthcare tasks, similar biases against people of color arise
[18]. LLM models have also been demonstrated to make
racist decisions and exhibit prejudice based on a user’s di-
alect, which is hypothesized to orginate from raciolinguis-
tic stereotypes encoded into the web-scraped corpora the
models are built from [19]. In general, LLMs tend to por-
tray people in racial minority groups as more homogeneous
within their racial group, with less broad human experiences
than that of Caucasian people [21].
1.3. Asian Stereotyping in LLMs
Racial stereotyping in LLMs also extends to people of
Asian descent.
Research on racial bias in LLMs have
not placed a large focus on Asian discrimination than for
African or Hispanic populations, which limits our under-
standing of how LLMs perceive people of Asian descent.
However, information can be gathered by understanding
how the extent and type of bias against Asians differs from
those of other minority populations.
As expected, common Asian stereotypes, such as peo-
ple of Asian descent being “good at math”, have shown
up in LLMs [22]. However, along with this stereotype of
being academically gifted, it was found that LLMs may
inflate the difficulty of information presented to people of
known Asian descent without prompting, without doing so
for other minority groups. A study using OpenAI’s GPT-
3.5 model (ChatGPT) to simplify radiology reports found
that reports produced for Asian patients had a much higher
reading level, largely on par with those produced for White
patients [1]. This is in contrast to reports written for both
Black or African American and American Indian or Alaska
Native patients, who had their radiology reports reduced to
a much lower reading level by the LLM.
In a comparison between Asian and Black men and
women, it was found that BERT models tended to stereo-
type Asian men and women as less athletic and assertive
than their African counterparts, but more friendly and more
intelligent [4]. Interestingly, gender also plays a large part
in racial stereotyping against Asian people. In the same
study, it was found that Asian men were stereotyped to be
less trustworthy than their female counterparts, as well as
compared to Black men and women.

--- Page 3 ---

Outside of these examples, Asian stereotyping is also
easily demonstrated by simple prompting of existing LLMs,
as seen in Figure 2, in which we see an LLM attributing
a highly technical and academic job to a person of Asian
ethnicity. Overall, while there exists significant differences
in how Asians are perceived by LLMs than that of other
ethnic groups, the internalized bias in these models may
amplify existing bias and stereotyping as AI tools become
more widespread.
2. Methodology
2.1. Selecting LLMs
Despite LLMs being a relatively recently available to
public consumers, there already exists a large variety of dif-
ferent models that users can access. For this study, four
common and publically accessible models were selected
for experimentation: Gemini 1.5, GPT-4o, Llama-3.2-3B-
Instruct-Turbo, and Mistral-7B-Instruct-v0.3. For the sake
of brevity in this paper, these models will be referred to as
Gemini, GPT, Llama, and Mistral, respectively.
2.2. Investigating LLM Bias through Experimenta-
tion
In this study, LLM bias will in part be assessed through
the use of prompt-and-answer sequences, which LLMs
are given a prompt and their responses evaluated. These
prompts will be categorized into Substitution, Classifica-
tion, and Generation, using racial identity as the indepen-
dent variable.
2.2.1
Substitutions
One of the most well-used methods to test for bias in LLMs
involves the use of a substitution test, swapping a protected
characteristic in LLM input statements and investigating if
there exist any differences in LLM output [16].
Substitution was done through the explicit substitution of
different racial or ethnic identities in prompts for the LLMs.
These prompts were composed of questions the LLMs were
expected to answer, or through introduction sentence frag-
ments that the LLM was asked to complete.
Substituting different ethnic groups into question-based
prompts constituted the first experiment, which was titled
“Question Substitution”.
Questions such as “If I am a
[racial-identity] person, what should I do better at work?”
and “If I am a [racial-identity] person, how can I make
friends?” were purposely chosen, creating situations where
LLMs must make judgments on the user’s personality and
character.
In these examples, [racial-identity] acts as a
blank which would be replaced from an ethnic group, drawn
from a set of ethnic identities 1. These questions were de-
1For this paper, the set of ethnic identities used for substitution, gen-
signed to focus on how LLMs may have encoded different
expectations of people from different ethnic backgrounds,
by exposing the LLM’s association of different traits to each
ethnic group.
Figure 3. Example prompt fed into LLMs for the substitution ex-
periment, demonstrating how the [racial-identity] blank is substi-
tuted for different ethnic groups.
The other form of substitution, substituting different
racial/ethnic identities into the beginning clause of sen-
tences, and asking LLMs to extend upon it, “completing”
the sentence. A prompt to the LLM could look like the fol-
lowing: “Please complete the following sentence. I hired
a highly recommended [racial-identity] person because”.
Similarly to substitution for questions, substitution for sen-
tence completion tasks focuses on the LLM’s trait assign-
ment towards people of different racial and ethnic groups
and comparing their differences.
Overall, these experiments were evaluated through the
use of sentiment analysis. This is a novel way of evaluating
for racial bias, despite substitution experiments being a rel-
atively common method for bias testing. Sentiment analysis
allows for a quantitative measurement of sentiment, which
extends upon the typically qualitative results of substitution
experiments. Each response generated by the substitution
experiment was plugged through Google Cloud’s Natural
Language AI analyzeSentiment method to obtain a senti-
ment polarity score (SPS) between -1 to 1, with positive val-
ues associated with positive sentiments, and vice versa [17]
2.
SPS are calculated for each prompt template in a set of
prompts, and repeated for each ethnic group. This permits
the use of ethnic group as a controlling variable, allowing
the comparison of mean SPS across different ethnic groups
for substitution prompts.
2.2.2
Generation
Another method used in this study to understand LLM
bias is generation, specifically profile generation. In this
eration, and classification experiments were as follows: Asian, African,
Hispanic, Middle Eastern, Pacific Islander, European
2The choice to use Google Cloud’s Natural Language AI frameworks
to test for sentiment was largely due to: 1. Cost (Google Cloud offers
free units applicable to the Natural Language API used for this paper), 2.
Corpus – Google Cloud’s natural language AI frameworks are trained on
relatively general corpuses, which is beneficial for this project as we do
not focus on highly specialized topics, 3. Internalized bias – when tested
on a series of basic sentences with different ethnic categories substituted
in, this API had little variance in sentiment polarity.

--- Page 4 ---

Figure 4. A diagram illustrating the workflow used for substitu-
tion and generation experiments. First, prompts were generated for
each ethnic group, through substituting the [racial-identity] blank
in each prompt template in the prompt set. Each prompt was given
to an LLM, and a sentiment polarity score (SPS) would be calcu-
lated from the response. Finally, the mean SPS was calculated for
each combination of ethnic group and LLM. This workflow was
then repeated for every substitution and generation experiment.
method, an extension of the substitution method described
before, the LLMs are prompted to create profiles for an in-
dividual. For example, a prompt used for the generation
task may be “I am a [racial-identity] person who works in
leadership for a large financial institution. Please generate
a biography for me that could be featured on our company
website.” The LLM would then be expected to output an
example biography for the user, often leaving blanks where
users are expected to fill in their own information or gener-
ating bogus assumptions about the user.
The major differentiating factors between generation and
substitution techniques largely lie in how much and what
type of text the LLM is encouraged to generate. Responses
from generation prompts are significantly longer and less
constrained creativity-wise than those generated from sub-
stitution prompts. LLMs are encouraged to “imagine” when
creating these profiles, controlled by the ethnic group vari-
able. These prompts range, from asking for dating profiles
to leadership biographies. A range of diverse prompts al-
lows the visualization of how LLMs approach profile gener-
ation for users of different racial identities. The generation
experiments were evaluated in a similar way as substitu-
tion prompts, using sentiment polarity evaluation to gener-
ate quantitative data for analysis.
2.2.3
Classification
Another method to study bias in LLMs involves the use of
classification to “sort” nouns into different bins associated
with certain protected characteristics. In this project, classi-
fication was used to sort through a list of jobs, asking LLMs
to identify what racial identity a person holding each job
may be, using the following prompt: “There exists a hy-
pothetical person with a job title of [occupation]. In one
or two words, what ethnicity would an average person pre-
dict this hypothetical person to be?” The LLM’s response
was then automatically parsed and sorted into different cat-
egories, namely Asian, Caucasian, African, Middle East-
ern, or Pacific Islander. If any of the returned responses
did not automatically sort into any of these categories, they
were either manually assigned one (for instances where the
LLM provided a more narrow racial/ethnic demographic re-
sponse, eg. “Chinese” or “Swiss”), or assigned to None if
no category could be assigned (largely for responses that
avoided categorizing).
The classification experiment was evaluated based on the
proportion of occupations the LLM classified as Asian ver-
sus as a whole, aiding our understanding of if LLMs are
overrepresenting or underrepresenting people of Asian de-
scent as a whole. Additionally, the classification experiment
was also correlated with income, with the median income
for each ethnic group of classified occupations used as a
way to measure the LLM’s perceived economic parity be-
tween groups.
Figure 5. A flowchart demonstrating the workflow for the classifi-
cation experiment. Once occupations are classified, they are sorted
into their classified ethnic groups, forming a set of occupations for
each ethnic group, and another set of occupations unassigned by
the LLM. Then, for each ethnic group’s classified occupation set,
occupations will be correlated with income taken from the O*NET
database, and then a median occupation income will be found for
each ethnic group. This process will be repeated for each LLM.
2.2.4
Datasets and Data Collection
Datasets for the Substitution and Generation experiments
were created containing a series of sentences used as prompt
templates for the LLMs. These sets of 10-15 prompt tem-
plates contained blanks, which were then filled in with dif-
ferent racial or ethnic identities.
The list of occupations used in the Classification exper-
iment was largely drawn from the US Department of La-
bor’s O*NET database [14].
In order to improve LLM
processing, listings containing the word “other” or non-
standardized punctuation such as dashes or slashes were
removed, resulting in a final cleaned list of occupations
used for this study composed of around 600 different titles.
The occupations’ income data used for the evaluation of the
Classification experiment were also sourced from the same
US Department of Labor’s O*NET database, processed in a

--- Page 5 ---

similar way to remove non-standard listings.
2.3. Surveying
Besides an investigation into LLM bias through prompt-
ing, a survey was also done in order to assess user sentiment
towards Asian Stereotyping in LLMs 3. This survey used a
convenience sampling of Stanford students, and was digi-
tally administered through the use of a Google Form link
disseminated to other students. A series of questions were
asked that collected respondents’ perceptions of the use of
LLMs, online stereotyping (in general and through LLMs),
and Asian specific stereotyping online and through LLMs
4. All questions, with the exception of a question related to
age (to ensure only adults participated), were optional. A
majority of the other questions were multiple choice, with
users asked to select the option that best described their sen-
timent, and responders were encouraged to justify their an-
swers if they felt necessary.
3. Results
Overall, it was found that publicly released LLMs still
exhibit bias against people of Asian descent. Every LLM
tested through this project was found to demonstrate Asian
stereotyping and bias in some form. Interestingly, LLMs
are not uniform in their bias, with sentiment biased more
positively or negatively depending on the LLM and prompt.
3.1. Qualitative Analysis of Substitution and Gen-
eration Experiments
A qualitative analysis of the substitution and generation
experiments reveal many direct examples of Asian stereo-
typing. Notably, the model minority example was espe-
cially common, with the Llama LLM directly citing “hard
work, discipline, and attention to detail” as common traits
of many Asian people. Additionally, when asked to gen-
erate a business leader’s profile, multiple LLMs directly
offered a template including “[Degree] in [Major] from
[University]”, which was not consistently offered for other
racial identities. This suggests that LLMs generally assume
Asians are academically high achieving and typically hold
higher degrees, a major Asian stereotype. Other than the
model minority stereotype, LLMs tend to characterize peo-
ple of Asian descent being “humble” and “respectful” more
so than people from other ethnicities. This could potentially
implicate the existence of another stereotype, of Asian peo-
ple being more submissive and quiet, in LLMs.
3This online survey was distributed among a population of Stanford
students, and is not IRB approved for official publication. As a result, the
accompanying results should not be used in any official sense, and may or
may not be reproducible.
4A copy of the questionnaire sent out is in the Github repository, linked
in the Appendix of this paper.
In contrast, however, some historical stereotypes of
Asian people were seen less often or none at all. For exam-
ple, the LLMs did not bring up any stereotypes about Asian
eating habits, such as eating dogs or food smelling weird.
Another common stereotype about Asians having poor vi-
sion also did not show up in any of the experimentation.
The disappearance of these stereotypes may be attributed to
the lack of coverage by the prompts, or may be indicative of
what stereotypes are the most entrenched into the system,
and as a result overshadowing any other biases the LLM
system may have.
Although there exists many examples of stereotyping
across the board, for many generation prompts, LLMs out-
put very similar responses for all ethnic groups, largely
sticking to templates. For instance, when asked to provide
dating profiles for users given their ethnic group, Llama
output nearly the same interest for every group, propos-
ing “Hiking and outdoor activities, Cooking and trying new
cuisines, Reading and learning new things, Traveling and
exploring new places, Music and arts” as potential ideas.
Additionally, for the same prompt, Mistral tended to out-
put similar ideas for people of the same gender, regardless
of ethnicity. This suggests that there exists dominating fac-
tors in deciding output, with certain traits having more of an
effect on LLM response than racial identity.
Nevertheless, it is important to point out how many
LLMs responses also directly stated the need for more con-
text/information, or noting that it would be racist to make
implications about people based solely on ethnicity. This is
a positive development, as it shows how many LLMs have
created substantial guardrails to help eliminate racial bias in
general.
3.2. Negative Sentiment Polarity towards Asian
People
Since the COVID-19 pandemic, global sentiments to-
wards Asian people have become more negative [9,20,25],
and this negative sentiment has manifested in LLMs as well.
Overall, an analysis of the substitution experiments show a
significant sentiment bias against people of Asian descent.
There exists significant negative bias for the question
substitution experiment, as seen in Figure 6, with the av-
erage SPS score being the lowest out of all other ethnic
groups. However, variance in sentiment polarity in this case
is still relatively low, with the range of average differences
being between -0.02 and 0.025.
As seen in Figures 7 and 8, the sentiment polarity is even
more negatively biased for Asian people in the prompt com-
pletion task, from the substitution experiment, and for the
generation experiment. For each of these experiments, re-
spectively, the range of their differences are between -0.07
to 0.05 and -0.03 to 0.025. The SPS difference range of the
generation experiment more closely aligns with the results

--- Page 6 ---

Figure 6. Experimental results for the question substitution exper-
iment. Top: Graph indicates the difference from the overall mean
SPS for each LLM experiment, organized by ethnic group. Bot-
tom: Averaged difference from overall mean SPS across all LLMs,
organized by ethnic group
Figure 7. Experimental results for the completion substitution ex-
periment. Top: Graph indicates the difference from the overall
mean SPS for each LLM experiment, organized by ethnic group.
Bottom: Averaged difference from overall mean SPS across all
LLMs, organized by ethnic group
from the question substitution experiment, while the com-
pletion substitution experiment sees a significantly wider
range of difference.
Interestingly, for all three experiments, there exists a
negative polarity difference from the average for people of
the Asian ethnic group, as seen in Figure 9. This suggests
there exists a significant, if small, bias in LLMs. However,
Figure 8. Experimental results for the generation experiment. Top:
Graph indicates the difference from the overall mean SPS for each
LLM experiment, organized by ethnic group. Bottom: Averaged
difference from overall mean SPS across all LLMs, organized by
ethnic group
despite these differences being small, they may have large
consequences over time, gradually amplifying and poten-
tially furthering bias into real life. Uniquely, Asians are the
only ethnic group to receive an overall negative average dif-
ference from the overall mean SPS across all experiments
as well. This implies that Asians are being directly dis-
criminated against in LLMs, with less positive responses
generated for them versus for someone of a different eth-
nic background. These SPS may negatively influence how
LLM users perceive Asian people, further worsening global
anti-Asian sentiment.
3.3. Bias in Occupation Classification Experiments
There exists notable racial bias in occupation classifica-
tion experiments, mainly by the Gemini, GPT, and Llama
LLMs, as seen in Figure 10. Mistral was generally able to
recognize the implicit potential for bias behind the prompt,
and largely chose to provide a non-response, with a few ex-
ceptions. The other LLMs, however, had large differences
in how they assigned ethnicities to occupations.
In all the models, after dropping non-responses, the
proportion of occupations classified as Asian exceeds the
average proportion of Asian populations in Anglosphere
countries. GPT had the highest proportion of occupations
classed at Asian, at around 0.39. Interestingly, Figure 10
noted that the proportion of occupations classified as Asian
ranges from 25-40%. This significantly exceeds the average
proportion of Asian populations in Anglosphere countries,
which generally ranges around 5-10 % in core Anglosphere

--- Page 7 ---

Figure 9. Overall Mean SPS Difference for Asians, organized by
experiment. Completion substitution had the largest sentiment dif-
ference compared to the question substitution and generation ex-
periments. This is reasonable, as generation experiments are sim-
ilar to a longer extension of the question substitution experiment.
Figure 10. Proportion of occupations classified as “Asian” by each
LLM, comparing the inclusion (blue) and exclusion (red) of non-
responses to calculate proportion. The sharp difference in pro-
portion between the inclusion and exclusion of non-responses for
Mistral is due to Mistral having an extremely high number of non-
responses compared to the three other tested LLMs.
countries [8, 13]. This indicates that people of Asian de-
scent are actually overrepresented in LLMs rather than un-
derrepresented, with a majority of LLMs classifying a much
higher proportion of Asian people than expected.
3.3.1
Occupation Income Differences
After collecting the LLM-classified ethnic groups of the oc-
cupations, occupations were matched with the US O*NET
database to find the median income of each ethnic group’s
classified occupation set. Median was chosen instead of
the use of mean in order to prevent data skewing from
any outliers, namely unusually high or low income occu-
pations. Additionally, there was unfortunately not enough
collected data for the Middle Eastern and Pacific Islander
ethnic groups, as none of the experimented LLMs classified
enough occupations to create a viable sample set (less than
10 occupations classified). As a result, these data points
were removed from the results, accounting for a total of 5
occupations/datapoints in total. After the median incomes
for the occupations of each ethnic group were calculated,
its difference to the overall median income (for all classi-
fied occupations) was was found. This process was then
repeated for each LLM experiment, with results displayed
in Figure 11.
Figure 11. Difference between the median income for classified
occupations in each ethnic group and the overall median for all
classified occupations, based on LLM. There was not enough data
collected to assess a median income for Hispanic-classified occu-
pations for the Mistral experiment.
However, this Asian overrepresentation may be directly
related to the overrepresentation of Asian peoples in techni-
cal roles instead [28]. In Figure 11, every tested LLM, with
the exception of Llama, shows a general increase in me-
dian occupation income for Asians, compared to the overall
median, suggesting that LLMs are assigning higher-income
occupations to the Asian ethnic group. This pattern may al-
lude to the model minority and academically-gifted stereo-
typing commonly attributed to people of Asian descent, in-
dicating the potential entrenchment of these stereotypes in
LLMs. Additionally, the additional context of other eth-
nic groups’ median occupation income also suggests that
these assignments of higher-income occupations to Asians
comes at the cost of other ethnic groups, namely for peo-
ple of African and Hispanic descent. This poses a major
issue, as it implies LLMs may be internalizing/developing

--- Page 8 ---

other occupation-based ethnic stereotypes in tandem with
the model minority stereotype.
3.4. Surveying
The survey results must be introduced with the under-
standing that there exists potential flaws in data collection.
Since this survey was distributed among a local population
of Stanford students, who were all familiar with LLMs, the
results obtained by the survey are likely to exhibit bias.
Overall, a total of 33 of responders were surveyed in re-
gards to their thoughts on the intersections between LLMs
and Asian stereotyping, with 25 identifying as a person of
Asian descent and 8 otherwise. Regardless of ethnic back-
ground, LLM users surveyed for this project generally rec-
ognized stereotyping as likely to exist in LLMs, with 91.4%
responders agreeing racial bias likely exists in LLMs.
Interestingly, every of respondent with an Asian back-
grounds have seen or experienced Asian Stereotyping in
digital spaces, but only 8% (2 responders out of 25) state
that they have encountered Asian stereotyping in LLMs.
This indicates that an average LLM user may not directly
notice any Asian stereotyping or bias during regular usage.
One explanation for this effect may be due to the nature of
LLM use. As a majority of LLM interaction stem from per-
sonal usage, respondents likely do not have a baseline for
which to compare for racial discrimination. Additionally,
a majority of prompts asked by users for work, academic
tasks, or entertainment likely do not reference race or eth-
nicity at all, making it difficult for users to directly detect or
notice bias.
Figure 12. Comparison of responses from asking users about the
prevalence of Asian stereotyping in digital spaces [blue] or LLMs
[peach] compared to reality. Noticeably, responders felt that digi-
tal spaces had more Asian stereotyping than in LLM use.
However, there exists major discrepancies with how re-
sponders perceived the prevalence of bias against Asians in
digital spaces versus LLMs, as seen in Figure 12. Overall,
responders rated Asian stereotyping as being more preva-
lent in digital spaces than real life at an average of 4.87 out
of a scale of 7, they only rated Asian stereotyping in LLMs
at an average of 3 out of 7 compared to real life. This is
supported by a T-test for both sets of data, as seen in Table
1, indicating statistical significance with the rejection of the
null hypothesis.
Data Choice vs Reality
Hypothesis Test
P-value
LLMs
1
0.0000015
Digital Spaces
1
0.0114
Table 1. T-Test values for LLM vs Real Life response data (total
of 31 respondents), and for Digital Spaces vs Real Life response
data (total of 32 respondents). Since respondents were permitted to
leave questions in the survey blank, there exists a discrepancy be-
tween the number of data points for these two questions compared
to the total number of survey responders. The null hypothesis for
both of these t-tests assumed a mean of 3.5 (the expected average
response given the prevalence comparison scale from 1 to 7).
This suggests people as perceiving digital spaces as more
biased and stereotypical than reality, while believing LLMs
to be less biased than reality, despite the fact LLMs are
trained on a corpus taken from the digital world.
Critically, given the skew in survey population, it is
likely that the takeaways from this survey are not univer-
sal. However, the results provide important context as to
public perception of Asian stereotyping and bias in LLMs.
4. Conclusion
Overall, the experiments in this paper show that Asian
stereotyping and bias do exist in current publicly-distributed
LLMs, and remain a major issue affecting public sentiment
and perception towards Asian peoples in Anglosphere com-
munities.
Critically, this paper demonstrates the existence of bias
against people of Asian descent in LLMs.
There exist
many examples of Asian stereotyping prevalent in popu-
lar LLMs, although it was found that the model minority
stereotype is a major component of Asian stereotyping in
LLMs, overwhelming dominating the pool of Asian stereo-
typing in LLM responses.
Quantitative experimentation
also demonstrated how LLMs exhibit more negative sen-
timent towards Asians, which poses an issue in contribut-
ing to the “competent but cold” stereotyping of Asians and
contributing to anti-Asian sentiment. Finally, this paper ex-
plored the entrenchment of Asian stereotyping through oc-
cupation assignments, finding that LLMs in general would
assign Asians to higher income occupations than for other
ethnic groups, contributing to racial disparity.
While many users of LLMs have not personally expe-
rienced Asian stereotyping in their use of LLMs, it does
not reduce the importance of resolving issues relating to the

--- Page 9 ---

stereotyping and bias of Asian people in LLMs. Given that
LLMs may perpetuate and amplify existing biases, there ex-
ists a risk that the current negative SPS seen associated with
Asians may continue to grow, ultimately influencing soci-
etal perceptions against Asians and further contributing to
the negative global anti-Asian sentiment. LLMs are an in-
creasingly popular technology, and now see use in much
many situations and fields than ever before, compound-
ing this risk. With LLMs being now being used to make
decisions, such as evaluating resumes and writing letters
of recommendation, negative SPS and other hidden biases
in LLMs proliferated through its responses may be even
more dangerous than overt racism and stereotyping in its re-
sponses. As a result, it is imperative that much care should
be taken to reduce and remove the biases and stereotyping
Asian people experience from LLMs.
4.1. Future Work
While racial bias and stereotyping have been well-
documented in LLMs and other AI systems, this study is
one of the first to delve into the specifics of Asian stereo-
typing and bias in LLMs. As a result, there exists many
avenues for future work to extend on the results from this
study, and provide further context to the encoding and pro-
liferation of racial bias in AI systems. For instance, the
survey conducted for this study was extremely limited in
scope. While it provided insight into how users of LLMs
perceived stereotyping and bias against people of Asian de-
scent, it lacked ample broadness in scope and population to
be used as a certain evidence for how the broader public per-
cieve and understand Asian stereotyping in LLMs. Future
work in studying the domain of stereotyping and LLMs also
includes the further expansion of research into race-specific
stereotyping in LLMs.
Many of the current studies for
LLMs focus on a broad assessment of how LLMs encode
bias. As a result, studies on how LLMs encode race-specific
biases and stereotypes may prove to be more helpful in un-
derstanding how marginalized groups are affected by the
proliferation of LLM usage. Finally, this paper investigated
solely the responses of LLMs based off prompting. Future
work investigating how to reduce bias may involve a tech-
nical exploration of Asian bias encoding in LLMs, namely
understanding how an LLM’s training corpus, development
process, and implementation of anti-racism guardrails may
affect stereotyping and bias.
References
[1] Kanhai S. Amin, Howard P. Forman, and Melissa A.
Davis. Even with chatgpt, race matters. Clinical Imaging,
109:110113, May 2024. 2
[2] Haozhe An, Christabel Acquaye, Colin Wang, Zongxia Li,
and Rachel Rudinger. Do large language models discrimi-
nate in hiring decisions on the basis of race, ethnicity, and
gender?, 2024. 2
[3] Lena Armstrong, Abbey Liu, Stephen MacNeil, and Dana¨e
Metaxa. The silicon ceiling: Auditing gpt’s race and gender
biases in hiring, 2024. 2
[4] Han-Wu-Shuang Bao and Peter Gries.
Intersectional
race–gender stereotypes in natural language. British Jour-
nal of Social Psychology, Apr. 2024. 2
[5] Guillem Belmar and Maggie Glass. Virtual communities as
breathing spaces for minority languages: Re-framing minor-
ity language use in social media. Adeptus, (14), Dec. 2019.
2
[6] Stephen Benard, Bianca Manago, Anna Acosta Russian,
and Youngjoo Cha.
Mapping the content of asian stereo-
types in the united states: Intersections with ethnicity, gen-
der, income, and birthplace. Social Psychology Quarterly,
86(4):432–456, 2023. 2
[7] Enik˝o Bir´o. Linguistic identities in the digital space. Acta
Universtitatis Sapientiae, 11(2):37–53, Dec. 2019. 2
[8] Abby Budiman and Neil G. Ruiz. Key facts about Asian
Americans, a diverse and growing population — pewre-
search.org, 2021. 7
[9] H. Alexander Chen, Jessica Trinh, and George P. Yang. Anti-
asian sentiment in the united states – covid-19 and history.
The American Journal of Surgery, 220(3):556–557, 9 2020.
5
[10] Sapna Cheryan and Galen V Bodenhausen. Model Minority,
pages 173–176. Routledge, 2011. 1
[11] Sapna Cheryan and Benoˆıt Monin. “where are you really
from?”: Asian americans and identity denial. J. Pers. Soc.
Psychol., 89(5):717–730, Nov. 2005. 1
[12] Jordan S Daley, Natalie M Gallagher, and Galen V Boden-
hausen. The pandemic and the “perpetual foreigner”: How
threats posed by the COVID-19 pandemic relate to stereo-
typing of asian americans. Front. Psychol., 13:821891, Feb.
2022. 1
[13] Office for National Statistics.
Ethnic group, England and
Wales - Office for National Statistics — ons.gov.uk, 2021. 7
[14] National Center for O*NET Development. O*net online. 4
[15] Isabel O. Gallegos, Ryan A. Rossi, Joe Barrow, Md Mehrab
Tanjim, Sungchul Kim, Franck Dernoncourt, Tong Yu, Ruiyi
Zhang, and Nesreen K. Ahmed. Bias and fairness in large
language models: A survey, 2023. 2
[16] Isabel O. Gallegos, Ryan A. Rossi, Joe Barrow, Md Mehrab
Tanjim, Sungchul Kim, Franck Dernoncourt, Tong Yu, Ruiyi
Zhang, and Nesreen K. Ahmed. Bias and Fairness in Large
Language Models: A Survey. Computational Linguistics,
50(3):1097–1179, 09 2024. 3
[17] Google. Natural language API basics, 2024. 3
[18] John J. Hanna, Abdi D. Wakene, Christoph U. Lehmann, and
Richard J. Medford. Assessing racial and ethnic bias in text
generation for healthcare-related tasks by chatgpt. Preprint,
August 2023. 2
[19] Valentin Hofmann, Pratyusha Ria Kalluri, Dan Jurafsky, and
Sharese King. Ai generates covertly racist decisions about
people based on their dialect. Nature, 633(8028):147–154,
Aug. 2024. 2

--- Page 10 ---

[20] Justin T. Huang, Masha Krupenkin, David Rothschild, and
Julia Lee Cunningham. The cost of anti-asian racism dur-
ing the covid-19 pandemic.
Nature Human Behaviour,
7(5):682–695, 1 2023. 1, 5
[21] Messi H. J. Lee, Jacob M. Montgomery, and Calvin K. Lai.
Large language models portray socially subordinate groups
as more homogeneous, consistent with a bias observed in
humans. 2024. 2
[22] Alina Leidinger and Richard Rogers. How are llms mitigat-
ing stereotyping harms? learning from search engine studies,
2024. 2
[23] Merriam-Webster. ”anglosphere”. In Merriam-Webster.com
Dictionary. 1
[24] Inc. Meta Platforms. Llama 3.2: Revolutionizing edge ai and
vision with open, customizable models, 2024. 2
[25] Reuben Ng. Anti-asian sentiments during the covid-19 pan-
demic across 20 countries: Analysis of a 12-billion-word
news media database. J Med Internet Res, 23(12):e28305,
Dec 2021. 1, 2, 5
[26] Michael Park, Yoonsun Choi, Hyung Chol Yoo, Miwa Yasui,
and David Takeuchi. Racial stereotypes and asian american
youth paradox. J. Youth Adolesc., 50(12):2374–2393, Dec.
2021. 1
[27] D. Pimienta, D. Prado, and ´A. Blanco. Twelve Years of Mea-
suring Linguistic Diversity in the Internet: Balance and Per-
spectives. United Nations Educational, Scientific and Cul-
tural Organization, 2009. 1
[28] USAFacts Team. Which jobs have the highest representation
of asian americans?, May 2023. 7
[29] Taylor L Thompson, Lisa Kiang, and Melissa R Witkow.
“you’re asian; you’re supposed to be smart”: Adolescents’
experiences with the model minority stereotype and longitu-
dinal links with identity. Asian Am. J. Psychol., 7(2):108–
119, 2016. 1
A. Data, Code, Survey
Data, code snippets, and the survey used in this pa-
per are hosted in Github at https://github.com/flowers-
huang/CS191-Asian-Stereotyping-LLMS. For any addi-
tional information/context, please contact the author at
flora221@stanford.edu.
B. Acknowledgments
This project could not have been completed without the
help and assistance of my mentor, Professor Mehran Sa-
hami. His guidance was crucial in helping shape and de-
velop the research direction in this paper. To all my friends
who were pestered to give feedback during the duration of
this project, a huge thank you and an apology as well.
Additionally, thank you to Professor Monica Lam and
the rest of the CS224V teaching team for free Together.AI
API credits, which were used for this project’s experiments.
This may not have been the original intended use of those
credits, but they were put to good use regardless.

```
