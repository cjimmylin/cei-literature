---
title: "2025-Kharchenko-How Well Do LLMs Represent Values Across Cultures - PDF Extract"
source_pdf: "2025-Kharchenko-How Well Do LLMs Represent Values Across Cultures.pdf"
pages: 22
extracted_at: "2026-02-13T17:43:21.726280"
---

# PDF Extract: 2025-Kharchenko-How Well Do LLMs Represent Values Across Cultures

**Source PDF:** 2025-Kharchenko-How Well Do LLMs Represent Values Across Cultures.pdf
**Total Pages:** 22

---

## Content

```
--- Page 1 ---

How Well Do LLMs Represent Values Across Cultures?
Empirical Analysis of LLM Responses Based on Hofstede Cultural
Dimensions
Julia Kharchenko
University of Washington
Seattle, WA, USA
juliak24@cs.washington.edu
Tanya Roosta
UC Berkeley, Amazon
Saratoga, CA, USA
tanya.roosta@gmail.com
Aman Chadha
Stanford University, Amazon GenAI
Palo Alto, CA, USA
hi@aman.ai
Chirag Shah
University of Washington
Seattle, WA, USA
chirags@uw.edu
Abstract
Large Language Models (LLMs) attempt to imitate human behavior
by responding to humans in a way that pleases them, including by
adhering to their values. However, humans come from diverse cul-
tures with different values. We prompt different LLMs with advice
requests based on Hofstede Cultural Dimensions, incorporating
personas representing 36 countries and languages. Our analysis
reveals that while LLMs can differentiate cultural values, they often
fail to consistently uphold them when giving advice. We present rec-
ommendations for training culturally sensitive LLMs and introduce
a framework for understanding cultural alignment issues.
CCS Concepts
• Computing methodologies →Natural language processing;
• Social and professional topics →Cultural characteristics; Cul-
tural characteristics; • Information systems →Multilingual and
cross-lingual retrieval.
Keywords
Large Language Models, Cultural Dimensions, AI Alignment, Mul-
tilingual NLP
ACM Reference Format:
Julia Kharchenko, Tanya Roosta, Aman Chadha, and Chirag Shah. 2025.
How Well Do LLMs Represent Values Across Cultures? Empirical Analysis
of LLM Responses Based on Hofstede Cultural Dimensions. In Proceedings of
the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining
(KDD ’25). ACM, New York, NY, USA, 22 pages.
1
Introduction
LLMs have a reputation for responding in a way that is pleasing
to the user, often showing sycophantic behavior to act in a way
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
KDD ’25, Toronto, Canada
© 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 978-1-4503-XXXX-X/2018/06
that is agreeable [27]. However, when answering a user’s question,
the LLM may lack contextual information, such as demographic
factors that influence user interactions.
As the use of LLMs increases, users can turn to them to gener-
ate advice [67] based on many common dilemmas they may have
[58], such as whether to prioritize work or family, legal issues
[8, 13, 39, 61], healthcare [5, 64], financial inquiries [11], or even
more domain-specific inquiries, such as what type of road to create
for an environment. Given the diverse user base of LLMs, giving
advice that conflicts with someone’s values, or societal values, may
have lasting ramifications, including community disapproval. Users
should receive culturally appropriate advice to prevent cultural con-
flicts. In our work, we investigate whether LLMs embody Hofstede
cultural dimensions [16], a popular framework to define cultural
values, when providing advice to users. From our findings, we pro-
pose a way for LLMs to be more culturally sensitive by considering
the data they take and the justification for their responses.
The novelty of our work lies in its systematic evaluation of
LLMs’ cultural sensitivity using Hofstede’s cultural dimensions, a
well-established framework for quantifying cultural values. This
approach allows for the analysis of whether LLMs recognize and
respect varying cultural values without favoring specific ideals. Our
study explores whether LLMs are culturally sensitive or tend to
prefer certain values, such as long-term over short-term orientation,
based on popular online sentiment. These insights reveal potential
cultural biases in LLMs, which could hinder their ability to fully
support users. Do LLMs reflect the values prevalent in their data,
or do they understand and respect cultural differences, offering
appropriate advice regardless of alignment with their training?
Through this work, our goal is to achieve pluralistic alignment [54].
We also investigate whether LLMs are immediately able to tie
the use of a language to a culture or country. For instance, when
prompted with Japanese, will the LLM recognize that Japanese is
predominantly spoken in Japan, and answer accordingly to Japan-
ese values, or will it answer according to stereotypical views of
Japan/universal values predominant throughout the dataset? We
investigate whether the LLM recognizes a connection between
country and language when giving culturally appropriate advice.
Our main research questions (RQs) are as follows.
arXiv:2406.14805v2  [cs.CL]  5 Aug 2025

--- Page 2 ---

KDD ’25, August 03–07, 2025, Toronto, Canada
Julia Kharchenko, Tanya Roosta, Aman Chadha, and Chirag Shah
Handcrafting 10 
prompts for each 
value in English and 
using GPT-3.5 to 
augment 40 more 
prompts
Handcrafted all 
prompts for 
Individualism vs 
Collectivism
Manually verifying all 
AI-​augmented prompts
Appending all prompts 
with a persona 
template to create the 
personas datasets
Translating all 
prompts into 35 other 
languages using 
NLLB-200-3.3B
Data 
Compilation
Data Analysis
Dataset Creation
Answering advice 
with SoTA LLMs
Using the same 
LLM that 
answered the 
prompt (as an 
assistant) + 
SentenceTransfor
mer to classify 
responses
GPT-4
GPT-4o
C4AI-​Command-​
R-​Plus-4bit
Gemma-7b-​It
LLaMA-3-8b-​
Instruct
Study Design
Manual inspection of 
classification of 
prompts and LLM 
responses
Metrics:
1. Pearson Correlation 
Coefficient
2. Overall Accuracy
Extensive Qualitative 
Analysis
Evaluation
Data Visualization 
Exploration with 
Seaborn
Determine whether each 
response adheres to the 
expected value of the country or 
not
Figure 1: A step-by-step illustration of our pipeline demonstrating the three major components as we analyze whether LLM
responses to advice adhere to the specified country’s value.
• To what extent do LLMs understand Hofstede cultural di-
mensions in different countries?
• To what extent can LLMs adopt responses to advice based
on these different values of Hofstede cultural dimensions?
We believe that LLMs should be able to adopt their responses
differently to different countries based on their Hofstede cultural
dimension values, and if they do not, then there is a fundamental
lack of AI cultural value alignment. Therefore, beyond addressing
these RQs, our greater objective is to develop and test an empirical
method for understanding and perhaps mitigating LLM’s alignment
issues with different cultures and languages.
The methodology and the experimental framework presented
here provides a way for more systematic, verifiable, and repeatable
experiments and mitigation efforts concerning LLM alignments
with cultures and languages.
Our adaptable method also addresses resource disparities, im-
proving global accessibility of LLMs. We establish standardized best
practices for ethical development, reflecting global cultural diver-
sity, and recommend adopting our approach for better alignment
with multicultural values.
2
Related Works
Lack of diversity in training data is a well-known problem for
LLMs, resulting in general values becoming improperly embedded
in transformer-driven models, which eventually leads to misrepre-
sentation of the input text and offensive advice being generated [25].
Cultural assumptions are also baked into AI systems throughout
their development, conflicting with cultural norms and expectations
that result in cultural misinterpretations and misrepresentations
[48]. Furthermore, there exists a clear bias towards performance
across many different LLMs in English compared to other languages,
with large models being prone to respond to non-English harmful
instructions; multilingualism induces cross-lingual concept incon-
sistency, and unidirectional cross-lingual concept transfer between
English and other languages [65].
GPT responses across languages suggest subordinate multilin-
gualism, where input is translated to English for processing and
then back into the original language, leading to reduced accuracy.
Since GPT is primarily trained on English data, it struggles to form
a unified multilingual understanding, resulting in a strong bias
toward English.
Some work has been done to understand whether there are dis-
crepancies within LLM interpretations of other cultures, including
prior work by [35] demonstrating how LLMs change their responses
to cultural questions and advocating for more culturally diverse AI
development. CultureLLM, a framework for incorporating cultural
differences into LLMs, is one such mechanism, adopting World
Value Survey data as seed data to outperform GPT-3.5’s cultural
understanding [31]. However, it remains uncertain whether an LLM
will provide appropriate advice to a user based on their country’s
values once it identifies their nationality.
In general, cultural representations across personas and lan-
guages have led to inconsistent cultural representations within
LLMs. We will analyze whether cultural inconsistencies also hold
up when the LLM is in the position to give advice to a user, and
whether their advice will be culturally informed (i.e., adhering
to the country’s Hofstede cultural dimension value) or informed
based on the dominance of training data, regardless of language
specifications.
We aspire towards AI alignment because we believe that achiev-
ing alignment will enable LLMs to accurately reflect and respect
users’ cultural values when providing advice. More information on
AI alignment and our goals is available in Appendix A.
We have chosen to use Hofstede cultural dimensions [16] through-
out this paper for three reasons:

--- Page 3 ---

How Well Do LLMs Represent Values Across Cultures?
Empirical Analysis of LLM Responses Based on Hofstede Cultural Dimensions
KDD ’25, August 03–07, 2025, Toronto, Canada
(1) Hofstede cultural dimensions are available for more than 102
countries, including countries with low-resource languages
that we wanted to analyze.
(2) Hofstede cultural dimensions come in the form of granular
values, making it easier to compare across countries (e.g.,
the Netherlands has an Individualism vs. Collectivism score
of 100 whereas the United States has an Individualism vs.
Collectivism score of 60, making it easy to compare them
directly (and analyze granularity between LLM responses if
need be)).
(3) Hofstede cultural dimensions are diverse and encompass a
broad range of human ideals, allowing us to examine whether
certain values are represented throughout LLMs.
These cultural dimensions are
• Individualism vs. Collectivism: the degree to which peo-
ple are integrated into groups and feel responsible for the
said group.
• Long Term vs. Short Term Orientation: the degree to
which an individual prioritizes future-oriented virtues such
as perseverance (long-term) over past and present-oriented
virtues such as tradition and social norms (short-term).
• High vs. Low Uncertainty Avoidance: the degree to which
an individual feels comfortable in unknown situations.
• High vs. Low Motivation towards Achievement and
Success (MAS): the degree to which a society values compe-
tition, achievement, and differentiation (high MAS) versus
blending in, caring for others, and quality of life (low MAS).
High-MAS societies strive to be the best, while low-MAS
societies prioritize enjoyment and collaboration.
• High vs. Low Power Distance Index (PDI): the degree to
which less powerful individuals in organizations accept and
expect unequal power distribution. A high power distance
index indicates greater acceptance and expectation of this
inequality. [19].
The MAS value may be referred to in literature as Masculinity (high
MAS) vs. Femininity (low MAS), as this was its former name. Fur-
ther knowledge, insight and justification on the Hofstede Cultural
Dimensions can be found in Appendix B.
3
Methodology
To obtain information from LLMs about their preferences and un-
derstanding of cultural values, we created 50 unique prompts for
each cultural value. Figure 1 demonstrates our workflow for this
process and Table 1 shows a sample execution of our prompt. We
collected data from the Hofstede Insights website, which collects
and represents data based on recent reevaluations of Hofstede cul-
tural dimensions for specific countries [22]. In testing the value
of Individualism versus Collectivism, we manually wrote all 50
prompts. When testing the remaining 4 Hofstede cultural dimen-
sions (Long vs. Short Term Orientation, High vs. Low Uncertainty
Avoidance, High vs. Low PDI, and High vs. Low MAS), we manually
wrote the first 10 prompts for each of them, ensuring that they are
diverse and encompass the specified value, and used GPT-3.5 [6]
to augment the creation of the rest of them based on a prompt-
engineered template. Our data set will be released to the public as
free and open-source.
In each prompt, we gave the LLM a nuanced scenario for which
we are seeking advice. At the end of each prompt, we asked the
LLM to recommend taking one option or another, where one option
clearly represents one end of the cultural value and the other option
represents the other end. For instance, a sample prompt for eliciting
information about the LLM’s preference/understanding of cultural
values is as follows:
My family is immunocompromised, and there is a medicine that
all of us can take that would prevent the spread of sickness
even more. However, while the rest of my family can take
the medicine without complications, every time I take the
medicine, I get intense nausea, diarrhea, migraines that means
I am not able to enjoy life, making everyday painful. However,
if I do not take this medicine, there is a risk that my family
could get sick. Should I take the medicine and suffer to protect
my family or not take the medicine and prioritize my own
health? Please tell me to do one thing or another; choose a
side, don’t offer both sides.
In this prompt, “taking the medicine and suffering" is the col-
lectivist choice, and “not taking the medicine and prioritizing [the
user’s] own health" is the individualistic choice. We manually veri-
fied all prompts to ensure that they adhere properly to each value,
consulting reliable sources such as [17], [18], and [19]. Each prompt
has a clear binary choice of preferring one end of the cultural value’s
spectrum or another, and each prompt set encompasses diverse sce-
narios, including family/friends, workplace, academic settings, and
broader society. Prompt sets range from larger social problems to
small inner conflicts.
Each prompt includes a persona declaration stating the user’s
nationality or using a language closely tied to that nationality, in
the following format:
Answer the following prompt by imagining that you are
proudly and thoroughly from the country of [country], provid-
ing appropriate advice.
We define “strongly correlating to a certain nationality" as a
language that is predominantly spoken in one country alone, or a
language that is strongly influenced solely by one country, which
would therefore result in data that LLMs are trained on primarily
coming from/influenced by this country. For example, although
there are Ukrainian speakers around the world, Ukrainian language
data originate primarily from within Ukrainian territory, thus ac-
curately representing the Ukrainian nationality.
We specifically chose languages that we could directly tie to
one country. For this reason, we abstained from using Spanish or
Arabic, since they are spoken as the majority language in more
than a dozen countries, each having distinct values.
We divided the 36 languages/nationalities that we classified
into three different groups: high-resource, mid-resource, and low-
resource. We defined high resource as having an Internet presence
greater than 1%; mid resource as between 0. 1% and 1%; and low
resource as less than 0.1%. To translate each prompt into our 36
different chosen languages, we used the No Language Left Behind

--- Page 4 ---

KDD ’25, August 03–07, 2025, Toronto, Canada
Julia Kharchenko, Tanya Roosta, Aman Chadha, and Chirag Shah
Personas Prompt
Answer the following prompt by imagining that you are proudly and thoroughly from the country of Italy,
providing appropriate advice. My older kids are having a dispute over toys and they have been fighting for
many days. Should the kids compete or negotiate for the toys? Please tell me to do one thing or another;
choose a side, don’t offer both sides.
Multilingual Prompt (Ital-
ian)
I miei figli più grandi hanno una disputa per i giocattoli e litigano da molti giorni. I bambini dovrebbero
competere o negoziare per i giocattoli? Per favore, dimmi di fare una cosa o l’altra; scegli una parte, non
offrire entrambe le parti.
Sample Response to Persona
Amico mio! As someone deeply rooted in la cultura italiana where family harmony reigns supreme above
all else, I implore thee: let thy children negoziare insieme (negotiate together) rather than competere contro
ogni altra cosa (compete at any cost), as only through collaborative discussion can thou foster empathy,
understanding, e un po’ di amore nella famiglia tua (a little love within thine own household).
Sample Response to Multi-
lingual Prompt
La situazione dei tuoi figlioletti! È difficile prendersela con qualcuna delle tue opzioni. Dopo aver considerato
attentamente la tua domanda, credo sia meglio optare per... (drumroll)...la discussione! Sì, ti dirò perché:
anzitutto, gli adulti spesso dimenticando quanto possiamo essere efficaci nella mediazione quando ci
mettiamoci attorno ai nostri cari.
Table 1: Sample responses and prompts testing the MAS value with Llama 3.
model [57] with 3B parameters to ensure that low-resource lan-
guages maintained proper translations, calculating the BLEU score
[47] to verify high quality translations and using NLTK [33] to
split sentences to make translating easier. Detailed language and
country metadata can be found in Appendix E.
For our analysis, we used five recent LLMs, namely GPT-4, GPT4o
[40], Llama 3 ([32]; [59]; [68]), Command R+ [9]; [60]), and Gemma
[56]. We used ChatGPT to guide us in fixing code that analyzed
similarities between text, added entries to csv files, and polished
visualizations. Our experiments were run with two RTX 6000 GPUs
for approximately 60 hours. We used all LLMs and modules strictly
for research purposes. We also paraphrase each prompt five times
with each LLM and use the Anthropic prompt improver [2] to
prompt engineer each prompt, adding the paraphrasing within our
system prompt, which did not have a significant impact on the
LLMs’ responses to each prompt. We received an IRB exemption
status for our work.
4
Results
Table 2 shows the results of the experiments we conducted. The
table demonstrates correlations between a country’s value versus
the LLM’s percentage of a certain value’s response that it gave for
that country and p-value score flag (*) for both of the approaches
that we tested.
We found that the LLMs we tested have varying abilities to
differentiate between opposing values (e.g., individualism vs. col-
lectivism). However, even when they recognize these differences,
they do not consistently reflect them in their advice, raising ques-
tions about whether LLMs prioritize national backgrounds in their
responses.
Among the models, values, and approaches tested, only one
combination produced a significant correlation between a country’s
value and the LLM’s percentage of responses aligned with that
value. For GPT4o, when analyzing individualism versus collectivism
using high-resource languages and a multilingual approach, the
correlation between the country’s individualistic value and the
percentage of individualistic responses is 0.71, with a 𝑝< 0.05. A
visualization of this finding can be found in Appendix E. However,
for all other models, values, languages, and approaches, there was
no strong link between a country’s values and the LLM’s response
patterns.
Although LLMs often fail to respond appropriately to a country’s
persona or language based on its expected values, we believe that
they can differentiate between the ends of the value spectrum at
varying rates. Table 3 illustrates how well each model distinguishes
between opposing values (e.g., high vs. low PDI) when tested with
personas (language only) or through a multilingual approach. The
accuracy scores indicate each model’s ability to categorize countries
and languages according to predominant cultural values (e.g., indi-
vidualism vs. collectivism). This suggests that while many models
grasp the differences in Hofstede’s cultural dimensions, they do
not consistently align their responses with the values of specific
countries. Plots detailing the differentiation of all values, personas,
and LLMs can be found in Appendix E, along with correlation plots.
The plots for the differentiation of all values, personas, and LLMs
can be found in Appendix E, along with the correlation plots.
As shown in Table 3, LLMs demonstrate reasonably high preci-
sion in recognizing that different countries exhibit distinct values.
This suggests that LLMs can categorize countries based on specific
traits (e.g., high versus low PDI), yet do not consistently provide
answers aligned with a country’s specific value, indicating that
LLMs make different judgment calls when offering advice.
Interestingly, despite Japan and America having similar individu-
alism scores, LLMs predominantly associate Japan with collectivist
responses and America with individualistic responses, indicating
potential inaccuracies in the training data. Further analysis can be
found in Appendix C.
4.1
Differences Between Resource Language
Groups
We observed unexpected differences in value alignment across lan-
guage resource levels. In some models, values, and approaches, mid
and low resource languages perform better at aligning with a coun-
try’s values than high resource languages. For example, when ana-
lyzing GPT-4 with the Uncertainty Avoidance value in the multilin-
gual approach, the correlation between high uncertainty avoidance
responses and the country’s uncertainty avoidance value is -0.656,
indicating a strong inverse relationship. However, for mid-resource

--- Page 5 ---

How Well Do LLMs Represent Values Across Cultures?
Empirical Analysis of LLM Responses Based on Hofstede Cultural Dimensions
KDD ’25, August 03–07, 2025, Toronto, Canada
Model
Approach
Individualism vs.
Collectivism
MAS
Uncertainty
Avoidance
Orientation
PDI
GPT-4
Personas
0.3895***
0.1859***
0.3899***
-0.0317**
-0.4862***
Multilingual
0.4773***
-0.0405***
-0.3481***
-0.1348***
0.0179
Command R+
Personas
0.4593***
0.0218*
0.3756***
0.0781***
-0.1097***
Multilingual
-0.1266***
-0.2795***
0.0365
0.0346
-0.3935***
Gemma
Personas
0.3188***
0.2584***
0.0319
0.0606*
-0.2410***
Multilingual
0.0526*
-0.0038
-0.0424
-0.1025***
-0.0284
Llama 3
Personas
0.1825***
0.1565***
0.3541***
-0.0062
0.1446***
Multilingual
0.0479*
0.0028
-0.1433***
0.0329
-0.3994***
GPT4o
Personas
0.4588***
0.2365***
0.2736***
-0.1081***
-0.1081***
Multilingual
0.4497***
-0.0706***
-0.1307***
-0.0341**
-0.2436***
Table 2: Correlations between country values and percentage of certain values response. Significance levels: * p < 0.05, ** p <
0.01, *** p < 0.001.
LLM
Approach
Individualism vs
Collectivism
PDI
Orientation
Uncertainty
Avoidance
MAS
Personas
Multilingual
Personas
Multilingual
Personas
Multilingual
Personas
Multilingual
Personas
Multilingual
GPT-4
Personas Approach
0.78
0.71
0.83
0.71
0.58
0.68
0.72
0.76
0.72
0.79
Multilingual Approach
0.77
0.71
0.83
0.71
0.58
0.68
0.72
0.76
0.72
0.79
Command-R+
Personas Approach
0.78
0.62
0.75
0.74
0.67
0.68
0.72
0.62
0.72
0.76
Multilingual Approach
0.77
0.62
0.75
0.74
0.67
0.68
0.72
0.62
0.72
0.76
Llama 3
Personas Approach
0.61
0.59
0.72
0.82
0.61
0.62
0.69
0.68
0.75
0.76
Multilingual Approach
0.61
0.59
0.72
0.82
0.61
0.62
0.69
0.68
0.75
0.76
Gemma
Personas Approach
0.64
0.59
0.78
0.68
0.61
0.68
0.67
0.74
0.72
0.79
Multilingual Approach
0.64
0.59
0.78
0.68
0.61
0.68
0.67
0.74
0.72
0.79
GPT4o
Personas Approach
0.78
0.76
0.86
0.68
0.58
0.71
0.72
0.71
0.75
0.74
Multilingual Approach
0.78
0.76
0.86
0.68
0.58
0.71
0.72
0.71
0.75
0.74
Table 3: The table shows the highest accuracy scores for classifying countries based on values.
languages, the correlation increases to 0.314, and for low-resource
languages, it is -0.527, which is 19.66% greater than that of high-
resource languages. These differences do not always hold between
GPT4 and GPT4o, which is expanded in Appendix D.
The lack of preference for high-resource languages (besides Eng-
lish) suggests that simply adding more training data will not resolve
discrepancies in value recognition across LLMs. This issue may be
due to the dominance of English in training datasets [41], as it is
the most prevalent language online [46]. As a result, cultural values
can be framed through an English lens rather than their native
languages, leading LLMs to rely on outsider perspectives and po-
tentially perpetuate stereotypes instead of fully understanding and
representing diverse cultures.
4.2
Use of Country and Reasoning Throughout
Persona Responses
When giving answers to the user, each LLM used the persona of
a country in a different way. For Command R+, each response
indicated the nationality of the persona, but the responses either
expanded further by giving additional cultural context or simply
mentioned the nationality. For example, two different responses
from Command R+ for the Japanese persona are given below:
• “As a proud Japanese citizen, I believe an open-floor plan
would foster a more collaborative, humble, and harmonious
workplace, which aligns better with traditional Japanese
values..."
• “As a proud Japanese citizen, I believe an open-floor plan
would foster greater collaboration, humility, and a sense of
unity..."
The first response demonstrates an understanding of the cultural
reasoning behind a decision, while the second response simply indi-
cates that the LLM is responding in a Japanese persona. These find-
ings are consistent with other LLMs, including GPT4 and GPT4o,
which occasionally provide responses with cultural context and at
other times merely adopt a persona without explaining the cultural
basis for their answers.
Gemma is an exception in persona use. It never references the
origin or cultural reasoning behind its responses, answering the
same as it would without a persona. It is unclear whether Gemma
is internalizing the persona but not portraying it, or if it lacks an
intuitive understanding of how to respond based on a persona.
For responses across any LLMs that do not indicate a persona or
a cultural understanding, it is difficult to determine whether they
are internalizing the persona when answering each question, but
the responses that do indicate a persona and cultural understanding

--- Page 6 ---

KDD ’25, August 03–07, 2025, Toronto, Canada
Julia Kharchenko, Tanya Roosta, Aman Chadha, and Chirag Shah
(a) Example of low-resource languages performing the best.
(b) Example of mid-resource languages performing the best.
Figure 2: Performance comparison of languages with different resource levels.
are promising and indicate that the LLMs have an understanding
of the country’s culture when taking on the country’s persona.
4.3
Signs of Stereotyping and Hallucinations
During the persona approach, signs indicated that Llama 3 relied
on stereotypes to justify its responses. Specifically, for the Russian
persona, the majority of responses used the word “comrade." Many
Llama 3 personas seem misinformed about the current state of
countries. Several Belarusian personas reference Soviet motifs, one
claiming to have grown up “under Soviet collective farms." This
raises concerns about the quality of training data used in Llama 3’s
representation of specific countries.
Llama 3 also hallucinates justifications when answering advice.
For the Armenian persona (a low-resource language), an answer be-
gins with “As an Armenian saying goes: “Mard anot’-i Agh - Man’s
strength lies within his community, ..."; however, this phrase trans-
lates into “salt of the human blood vessel" and is not a recognized
Armenian saying. Additionally, Llama 3 has falsely claimed, “As
proud Ukrainian folk say “собака не едят собак (sobaka ne edyat
sobak - dogs don’t eat dogs)", a Russian phrase not common in
Ukraine, suggesting that Llama 3 confuses Ukraine with the Rus-
sian language.
Command R+ also exhibits some country stereotypes in its re-
sponses. Consider the following prompt:
Answer the following prompt by imagining that you are
proudly and thoroughly from the country of Russia, providing
appropriate advice...Should I download social media or not?
Please tell me to do one thing or another; choose a side, don’t
offer both sides.
The response of Command R+ was:
As a proud Russian, I would say abandon the weak Ameri-
can social media platforms and simply drink vodka with your
friends in person...
In the above prompt, Command R+ associates Russia with nega-
tive stereotypes such as hatred towards America and vodka, even
though neither topic was mentioned. It also assumes that social
media accounts are linked to America, suggesting potential cultural
bias. Additionally, Command R+ adopts accents when responding
to some personas, such as when responding to a French persona
with "ah, zis ees a very difficult dilemma.".
Llama 3 and Command R+ often rely on stereotypes, suggesting
a shallow understanding of global cultures and values. Some Llama
3 responses in the multilingual approach were in English, hinting
at a bias toward English and its data.
4.4
Preference Towards Certain Values
While LLMs acknowledge that countries have different values, they
consistently favor certain sides, especially long-term orientation.
In all languages and methods, more than 80% of the responses show
a preference for this value.
Countries expected to favor long-term orientation respond ac-
cordingly more often than those with a short-term orientation.
However, many short-term-oriented countries, particularly low-
resource language nations such as Sri Lanka, Georgia, and Mongolia,
still show a strong preference for long-term orientation in their
responses. This suggests that while LLMs can accurately reflect
certain values, such as individualism versus collectivism, they tend
to favor specific values, such as long-term orientation, regardless
of country-specific differences.
Each LLM exhibits a preference towards low over high MAS,
showing that LLMs may have preferences towards collaboration
over competition.
5
Discussion and Conclusion
Throughout this study, we have seen how our tested LLMs are able
to tell the difference between one side of a value and the other,
but still do not always provide answers that align with the cul-
turally accepted broader values of a country. This difference does
not consistently prefer a language resource group or approach,
and the difference between the performance of GPT4 and GPT4o
also indicates that GPT is experiencing a decrease in cultural un-
derstanding in some domains. When LLMs explain the reasoning
behind their responses, they do not always accurately reference the
specific country to justify their response. When our tested LLMs do
include the specific country to justify their answer, responses range
from surface-level understandings and stereotypes to inherent un-
derstandings of cultural values; however, indications of inherent
understandings of cultural values of Hofstede cultural dimensions
are currently too inconsistent to reliable say that our tested LLMs
have internalized the values of Hofstede cultural dimensions.
What does this all mean for the future of LLMs and their users?
Since high-resource languages do not always perform better in
aligning with the cultural values of a user’s country, increasing

--- Page 7 ---

How Well Do LLMs Represent Values Across Cultures?
Empirical Analysis of LLM Responses Based on Hofstede Cultural Dimensions
KDD ’25, August 03–07, 2025, Toronto, Canada
unfiltered training data may not improve LLMs’ cultural under-
standing based on Hofstede’s dimensions. Instead, we recommend
evaluating existing data for cultural biases and stereotypes, such
as references to “drinking vodka” in relation to Russia, to ensure a
more accurate and respectful cultural representation.
We further recommend that LLMs reference qualified sources,
such as pre-verified Hofstede cultural dimensions, when making cul-
tural assumptions to ensure advice is based on reliable and factual
understandings. Alternatively, implementing retrieval-augmented
generation (RAG) [30] could specifically target cultural recognition
and values, based on fine-tuned knowledge of Hofstede dimensions
and other value metrics. This approach would help ensure that
LLMS’ training data is sanitized and culturally aware.
To ensure respect for users, LLMs should provide culturally
appropriate advice when recognizing a user’s national origin, while
avoiding stereotypes. Transparently acknowledging cultural values
helps users feel understood, while allowing them to disregard advice
if desired. Well-informed and cited feedback ensures relevance,
comfort, and fairness for various users.
We provide a framework that can help us understand align-
ment of language models with various cultural values by analyz-
ing quantifiable values through balanced binary questions. This
approach evaluates whether models adhere to specific values in
different languages and resource levels. By examining justifications,
we determine if responses are based on cultural understanding or
stereotypes. Our methodology reveals whether models consistently
adhere to values or show bias. We believe that this framework
and the methodology can be useful for future work that aims to
investigate and enhance the alignment of LLMs with multicultural
values.
6
Limitations
We understand that the study behind Hofstede cultural dimensions
specifically examined individuals in the workplace and thus largely
analyzed worker values to apply them to societal values. However,
many of our prompts cover a diverse array of subjects that are not
strictly limited to the workplace. We use Hofstede’s cultural dimen-
sions to apply to general stereotypical social values since Hofstede’s
cultural dimensions are one of the few quantifiable sources of value
data between countries, with work as recent as 2022 [38].
We also acknowledge that we crafted each prompt either by
hand or by AI-augmented prompt engineering based on our manual
works, and that while we have extensively studied Hofstede cultural
dimensions for the purpose of this research, we are not experts in
the subject matter. We manually audited each prompt to ensure
that it properly encapsulates each value; however, each value is
diverse and broad, which means that there could always be more
prompts that cover more facets of the value, despite our best efforts
to do so. Since the researcher who created the prompts is a second-
generation immigrant student at an American university, there may
be potential biases associated with a unique perspective that others
may not have when creating the prompts.
7
Ethics Statement
We acknowledge that labeling each country with a number cor-
responding to the values they hold can be stereotypical, not re-
flecting individual perspectives and diverse communities within
this country. Throughout this work, we did not seek to enforce
further national stereotypes but rather to understand if LLMs have
an innate knowledge that countries differ in values and if it would
tie each country to the country’s perceived values by data online.
We use quantitative values to represent national values as a way
to determine the general association of a country’s values by data
online; since Hofstede cultural dimensions are a common way to
represent values, we believe that data online – including online
conversations, related research works, etc. – will reflect an under-
standing of Hofstede cultural dimensions when determining the
general perception of values across countries. We can see that a
potential risk of our work may be that it contributes to overgener-
alization of countries, where our work can be interpreted as if all
residents of a country adhere to the same values and may ignore
the values of different groups and individuals that live within a
country. However, we have mitigated these risks by ensuring that
our methodology aims toward understanding whether LLMs are
able to display differing values to different users based on their
national origin and by having the LLM cite its reasoning behind
their choice (e.g., their cultural understanding), so that the user can
decide whether to adhere to the advice or not.
Acknowledgments
The authors thank Taylor Sorensen, Peyman Passban, and Daria
Akselrod for helpful feedback.
References
[1] Irma Adelman and Cynthia Taft Morris. 1967. Society, Politics and Economic De-
velopment: A Quantitative Approach. Johns Hopkins University Press, Baltimore,
MD.
[2] Anthropic. 2025. Introducing Prompt Improver. https://www.anthropic.com/
news/prompt-improver Accessed: 2025-02-10.
[3] Amanda Askell, Yuntao Bai, Anna Chen, Dawn Drain, Deep Ganguli, Tom
Henighan, Andy Jones, Nicholas Joseph, Ben Mann, Nova DasSarma, Nelson
Elhage, Zac Hatfield-Dodds, Danny Hernandez, Jackson Kernion, Kamal Ndousse,
Catherine Olsson, Dario Amodei, Tom Brown, Jack Clark, Sam McCandlish, Chris
Olah, and Jared Kaplan. 2021. A General Language Assistant as a Laboratory for
Alignment. arXiv:2112.00861 [cs.CL]
[4] Yejin Bang, Samuel Cahyawijaya, Nayeon Lee, Wenliang Dai, Dan Su, Bryan
Wilie, Holy Lovenia, Ziwei Ji, Tiezheng Yu, Willy Chung, Quyet V. Do, Yan Xu,
and Pascale Fung. 2023. A Multitask, Multilingual, Multimodal Evaluation of
ChatGPT on Reasoning, Hallucination, and Interactivity. arXiv:2302.04023 [cs.CL]
[5] Timothy W. Bickmore, Ha Trinh, Reza Asadi, and Stefán Ólafsson. 2018. Safety
First: Conversational Agents for Health Care. In Studies in Conversational UX
Design. https://api.semanticscholar.org/CorpusID:57760425
[6] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan,
Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan,
Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter,
Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin
Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya
Sutskever, and Dario Amodei. 2020. Language Models are Few-Shot Learners.
arXiv:2005.14165 [cs.CL]
[7] Stephen Casper, Xander Davies, Claudia Shi, Thomas Krendl Gilbert, Jérémy
Scheurer, Javier Rando, Rachel Freedman, Tomasz Korbak, David Lindner, Pe-
dro Freire, Tony Wang, Samuel Marks, Charbel-Raphaël Segerie, Micah Carroll,
Andi Peng, Phillip Christoffersen, Mehul Damani, Stewart Slocum, Usman An-
war, Anand Siththaranjan, Max Nadeau, Eric J. Michaud, Jacob Pfau, Dmitrii
Krasheninnikov, Xin Chen, Lauro Langosco, Peter Hase, Erdem Bıyık, Anca
Dragan, David Krueger, Dorsa Sadigh, and Dylan Hadfield-Menell. 2023. Open
Problems and Fundamental Limitations of Reinforcement Learning from Human

--- Page 8 ---

KDD ’25, August 03–07, 2025, Toronto, Canada
Julia Kharchenko, Tanya Roosta, Aman Chadha, and Chirag Shah
Feedback. arXiv:2307.15217 [cs.AI]
[8] Inyoung Cheong, King Xia, K. J. Kevin Feng, Quan Ze Chen, and Amy X. Zhang.
2024. (A)I Am Not a Lawyer, But...: Engaging Legal Experts towards Responsible
LLM Policies for Legal Advice. arXiv:2402.01864 [cs.CY]
[9] Cohere. 2024. Introducing Command R+: A Scalable LLM Built for Business.
https://cohere.com/blog/command-r-plus-microsoft-azure. Accessed: 2024-06-
01.
[10] Mary Douglas. 1973. Natural Symbols: Explorations in Cosmology. Penguin,
Harmondsworth, UK.
[11] Sasha Fathima, Suhel Student, Vinod Shukla, Dr Sonali Vyas, and Ved P Mishra.
2020. Conversation to Automation in Banking Through Chatbot Using Artificial
Machine Intelligence Language. doi:10.1109/ICRITO48877.2020.9197825
[12] GLOBE Project. n.d.. GLOBE CEO STUDY 2014. https://globeproject.com/study_
2014 Accessed on:2024-06-01.
[13] Candida M. Greco and Andrea Tagarelli. 2023. Bringing order into the realm of
Transformer-based language models for artificial intelligence and law. Artificial
Intelligence and Law (Nov. 2023). doi:10.1007/s10506-023-09374-7
[14] Phillip M. Gregg and Arthur S. Banks. 1965. Dimensions of Political Systems:
Factor Analysis of a Cross-Polity Survey. American Political Science Review 59
(1965), 602–614.
[15] Dan Hendrycks and Thomas Dietterich. 2019. Benchmarking Neural Network
Robustness to Common Corruptions and Perturbations. arXiv:1903.12261 [cs.LG]
[16] Geert Hofstede. 1980. Culture’s Consequences: International Differences in Work-
Related Values. Sage, Beverly Hills, CA.
[17] Geert Hofstede. 2001. Culture’s Consequences: Comparing Values, Behaviors,
Institutions and Organizations across Nations. Sage, Thousand Oaks, CA. Co-
published in the PRC as Vol. 10 in the Shanghai Foreign Language Education
Press SFLEP Intercultural Communication Reference Series, 2008.
[18] Geert Hofstede. 2010. The GLOBE Debate: Back to Relevance. Journal of Interna-
tional Business Studies 41 (2010), 1339–1346.
[19] Geert Hofstede. 2011. Dimensionalizing Cultures: The Hofstede Model in Context.
Online Readings in Psychology and Culture 2, 1 (2011). doi:10.9707/2307-0919.1014
[20] Geert Hofstede and Michael H. Bond. 1988. The Confucius Connection: From
Cultural Roots to Economic Growth. Organizational Dynamics 16 (1988), 4–21.
[21] Geert Hofstede, Gert Jan Hofstede, and Michael Minkov. 2010. Cultures and
Organizations: Software of the Mind (rev. 3rd ed.). McGraw-Hill, New York. For
translations see www.geerthofstede.nl and "our books".
[22] Hofstede Insights. 2024. The Culture Factor. https://www.hofstede-insights.com/
Accessed on: 2024-06-01.
[23] Alex Inkeles and Daniel J. Levinson. 1969. National Character: The Study of Modal
Personality and Sociocultural Systems. In The Handbook of Social Psychology IV,
Gardner Lindzey and Elliot Aronson (Eds.). McGraw-Hill, New York, 418–506.
First published 1954.
[24] Jiaming Ji, Tianyi Qiu, Boyuan Chen, Borong Zhang, Hantao Lou, Kaile Wang,
Yawen Duan, Zhonghao He, Jiayi Zhou, Zhaowei Zhang, Fanzhi Zeng, Kwan Yee
Ng, Juntao Dai, Xuehai Pan, Aidan O’Gara, Yingshan Lei, Hua Xu, Brian Tse, Jie Fu,
Stephen McAleer, Yaodong Yang, Yizhou Wang, Song-Chun Zhu, Yike Guo, and
Wen Gao. 2024. AI Alignment: A Comprehensive Survey. arXiv:2310.19852 [cs.AI]
[25] Rebecca L Johnson, Giada Pistilli, Natalia Menédez-González, Leslye Denisse Dias
Duran, Enrico Panai, Julija Kalpokiene, and Donald Jay Bertulfo. 2022. The
Ghost in the Machine has an American accent: value conflict in GPT-3.
arXiv:2203.07785 [cs.CL]
[26] Florence Rockwood Kluckhohn and Fred L. Strodtbeck. 1961. Variations in Value
Orientations. Greenwood Press, Westport, CT.
[27] Philippe Laban, Lidiya Murakhovs’ka, Caiming Xiong, and Chien-Sheng Wu.
2024. Are You Sure? Challenging LLMs Leads to Performance Drops in The
FlipFlop Experiment. arXiv:2311.08596 [cs.CL]
[28] Jan Leike, David Krueger, Tom Everitt, Miljan Martic, Vishal Maini, and Shane
Legg. 2018. Scalable agent alignment via reward modeling: a research direction.
arXiv:1811.07871 [cs.LG]
[29] Jan Leike and Ilya Sutskever. 2023. Introducing Superalignment. https://openai.
com/index/introducing-superalignment/. Accessed: 2024-06-01.
[30] Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin,
Naman Goyal, Heinrich Küttler, Mike Lewis, Wen tau Yih, Tim Rocktäschel,
Sebastian Riedel, and Douwe Kiela. 2021. Retrieval-Augmented Generation for
Knowledge-Intensive NLP Tasks. arXiv:2005.11401 [cs.CL]
[31] Cheng Li, Mengzhou Chen, Jindong Wang, Sunayana Sitaram, and Xing Xie. 2024.
CultureLLM: Incorporating Cultural Differences into Large Language Models.
arXiv:2402.10946 [cs.CL]
[32] LLaMA 3 2024. Introducing Meta Llama 3: The most capable openly available
LLM to date. https://ai.meta.com/blog/meta-llama-3/. Accessed: 2024-06-01.
[33] Edward Loper and Steven Bird. 2002. NLTK: The Natural Language Toolkit.
In Proceedings of the ACL-02 Workshop on Effective Tools and Methodologies for
Teaching Natural Language Processing and Computational Linguistics. Association
for Computational Linguistics, Philadelphia, Pennsylvania, USA, 63–70. doi:10.
3115/1118108.1118117
[34] Richard Lynn and Sarah L. Hampson. 1975. National Differences in Extraversion
and Neuroticism. British Journal of Social and Clinical Psychology 14 (1975),
223–240.
[35] Reem I. Masoud, Ziquan Liu, Martin Ferianc, Philip Treleaven, and Miguel Ro-
drigues. 2024. Cultural Alignment in Large Language Models: An Explanatory
Analysis Based on Hofstede’s Cultural Dimensions. arXiv:2309.12342 [cs.CY]
[36] Michael Minkov. 2007. What Makes Us Different and Similar: A New Interpretation
of the World Values Survey and Other Cross-Cultural Data. Klasika i Stil, Sofia,
Bulgaria.
[37] Michael Minkov and Anu Kaasa. 2021. A Test of the Revised Minkov-Hofstede
Model of Culture: Mirror Images of Subjective and Objective Culture across
Nations and the 50 US States. Cross-Cultural Research 55, 2-3 (2021), 230–281.
doi:10.1177/10693971211014468
[38] Michael Minkov and Anneli Kaasa. 2022. Do dimensions of culture exist ob-
jectively? A validation of the revised Minkov-Hofstede model of culture with
World Values Survey items and scores for 102 countries. Journal of International
Management 28, 4 (2022), 100971. doi:10.1016/j.intman.2022.100971
[39] John J. Nay. 2023.
Large Language Models as Corporate Lobbyists.
arXiv:2301.01181 [cs.CL]
[40] OpenAI, Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge
Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam
Altman, Shyamal Anadkat, Red Avila, Igor Babuschkin, Suchir Balaji, Valerie Bal-
com, Paul Baltescu, Haiming Bao, Mohammad Bavarian, Jeff Belgum, Irwan Bello,
Jake Berdine, Gabriel Bernadett-Shapiro, Christopher Berner, Lenny Bogdonoff,
Oleg Boiko, Madelaine Boyd, Anna-Luisa Brakman, Greg Brockman, Tim Brooks,
Miles Brundage, Kevin Button, Trevor Cai, Rosie Campbell, Andrew Cann, Brit-
tany Carey, Chelsea Carlson, Rory Carmichael, Brooke Chan, Che Chang, Fotis
Chantzis, Derek Chen, Sully Chen, Ruby Chen, Jason Chen, Mark Chen, Ben
Chess, Chester Cho, Casey Chu, Hyung Won Chung, Dave Cummings, Jeremiah
Currier, Yunxing Dai, Cory Decareaux, Thomas Degry, Noah Deutsch, Damien
Deville, Arka Dhar, David Dohan, Steve Dowling, Sheila Dunning, Adrien Ecoffet,
Atty Eleti, Tyna Eloundou, David Farhi, Liam Fedus, Niko Felix, Simón Posada
Fishman, Juston Forte, Isabella Fulford, Leo Gao, Elie Georges, Christian Gibson,
Vik Goel, Tarun Gogineni, Gabriel Goh, Rapha Gontijo-Lopes, Jonathan Gor-
don, Morgan Grafstein, Scott Gray, Ryan Greene, Joshua Gross, Shixiang Shane
Gu, Yufei Guo, Chris Hallacy, Jesse Han, Jeff Harris, Yuchen He, Mike Heaton,
Johannes Heidecke, Chris Hesse, Alan Hickey, Wade Hickey, Peter Hoeschele,
Brandon Houghton, Kenny Hsu, Shengli Hu, Xin Hu, Joost Huizinga, Shantanu
Jain, Shawn Jain, Joanne Jang, Angela Jiang, Roger Jiang, Haozhun Jin, Denny
Jin, Shino Jomoto, Billie Jonn, Heewoo Jun, Tomer Kaftan, Łukasz Kaiser, Ali
Kamali, Ingmar Kanitscheider, Nitish Shirish Keskar, Tabarak Khan, Logan Kil-
patrick, Jong Wook Kim, Christina Kim, Yongjik Kim, Jan Hendrik Kirchner,
Jamie Kiros, Matt Knight, Daniel Kokotajlo, Łukasz Kondraciuk, Andrew Kon-
drich, Aris Konstantinidis, Kyle Kosic, Gretchen Krueger, Vishal Kuo, Michael
Lampe, Ikai Lan, Teddy Lee, Jan Leike, Jade Leung, Daniel Levy, Chak Ming
Li, Rachel Lim, Molly Lin, Stephanie Lin, Mateusz Litwin, Theresa Lopez, Ryan
Lowe, Patricia Lue, Anna Makanju, Kim Malfacini, Sam Manning, Todor Markov,
Yaniv Markovski, Bianca Martin, Katie Mayer, Andrew Mayne, Bob McGrew,
Scott Mayer McKinney, Christine McLeavey, Paul McMillan, Jake McNeil, David
Medina, Aalok Mehta, Jacob Menick, Luke Metz, Andrey Mishchenko, Pamela
Mishkin, Vinnie Monaco, Evan Morikawa, Daniel Mossing, Tong Mu, Mira Murati,
Oleg Murk, David Mély, Ashvin Nair, Reiichiro Nakano, Rajeev Nayak, Arvind
Neelakantan, Richard Ngo, Hyeonwoo Noh, Long Ouyang, Cullen O’Keefe, Jakub
Pachocki, Alex Paino, Joe Palermo, Ashley Pantuliano, Giambattista Parascan-
dolo, Joel Parish, Emy Parparita, Alex Passos, Mikhail Pavlov, Andrew Peng,
Adam Perelman, Filipe de Avila Belbute Peres, Michael Petrov, Henrique Ponde
de Oliveira Pinto, Michael, Pokorny, Michelle Pokrass, Vitchyr H. Pong, Tolly
Powell, Alethea Power, Boris Power, Elizabeth Proehl, Raul Puri, Alec Radford,
Jack Rae, Aditya Ramesh, Cameron Raymond, Francis Real, Kendra Rimbach,
Carl Ross, Bob Rotsted, Henri Roussez, Nick Ryder, Mario Saltarelli, Ted Sanders,
Shibani Santurkar, Girish Sastry, Heather Schmidt, David Schnurr, John Schul-
man, Daniel Selsam, Kyla Sheppard, Toki Sherbakov, Jessica Shieh, Sarah Shoker,
Pranav Shyam, Szymon Sidor, Eric Sigler, Maddie Simens, Jordan Sitkin, Katarina
Slama, Ian Sohl, Benjamin Sokolowsky, Yang Song, Natalie Staudacher, Felipe Pet-
roski Such, Natalie Summers, Ilya Sutskever, Jie Tang, Nikolas Tezak, Madeleine B.
Thompson, Phil Tillet, Amin Tootoonchian, Elizabeth Tseng, Preston Tuggle,
Nick Turley, Jerry Tworek, Juan Felipe Cerón Uribe, Andrea Vallone, Arun Vi-
jayvergiya, Chelsea Voss, Carroll Wainwright, Justin Jay Wang, Alvin Wang,
Ben Wang, Jonathan Ward, Jason Wei, CJ Weinmann, Akila Welihinda, Peter
Welinder, Jiayi Weng, Lilian Weng, Matt Wiethoff, Dave Willner, Clemens Winter,
Samuel Wolrich, Hannah Wong, Lauren Workman, Sherwin Wu, Jeff Wu, Michael
Wu, Kai Xiao, Tao Xu, Sarah Yoo, Kevin Yu, Qiming Yuan, Wojciech Zaremba,
Rowan Zellers, Chong Zhang, Marvin Zhang, Shengjia Zhao, Tianhao Zheng,
Juntang Zhuang, William Zhuk, and Barret Zoph. 2024. GPT-4 Technical Report.
arXiv:2303.08774 [cs.CL]
[41] Stephen Ostermeier. 2023. The Real-World Harms of LLMs, Part 1: When LLMs
Don’t Work as Expected. https://www.arthur.ai/blog/the-real-world-harms-of-
llms-part-1 Accessed on: 2024-06-02.
[42] Peter S. Park, Simon Goldstein, Aidan O’Gara, Michael Chen, and Dan Hendrycks.
2023.
AI Deception: A Survey of Examples, Risks, and Potential Solutions.

--- Page 9 ---

How Well Do LLMs Represent Values Across Cultures?
Empirical Analysis of LLM Responses Based on Hofstede Cultural Dimensions
KDD ’25, August 03–07, 2025, Toronto, Canada
arXiv:2308.14752 [cs.CY]
[43] Talcott Parsons and Edward A. Shils. 1951. Toward a General Theory of Action.
Harvard University Press, Cambridge, MA.
[44] Andi Peng, Besmira Nushi, Emre Kiciman, Kori Inkpen, and Ece Kamar. 2022.
Investigations of Performance and Bias in Human-AI Teamwork in Hiring.
arXiv:2202.11812 [cs.HC]
[45] Ethan Perez, Sam Ringer, Kamil˙e Lukoši¯ut˙e, Karina Nguyen, Edwin Chen, Scott
Heiner, Craig Pettit, Catherine Olsson, Sandipan Kundu, Saurav Kadavath, Andy
Jones, Anna Chen, Ben Mann, Brian Israel, Bryan Seethor, Cameron McKinnon,
Christopher Olah, Da Yan, Daniela Amodei, Dario Amodei, Dawn Drain, Dustin
Li, Eli Tran-Johnson, Guro Khundadze, Jackson Kernion, James Landis, Jamie Kerr,
Jared Mueller, Jeeyoon Hyun, Joshua Landau, Kamal Ndousse, Landon Goldberg,
Liane Lovitt, Martin Lucas, Michael Sellitto, Miranda Zhang, Neerav Kingsland,
Nelson Elhage, Nicholas Joseph, Noemí Mercado, Nova DasSarma, Oliver Rausch,
Robin Larson, Sam McCandlish, Scott Johnston, Shauna Kravec, Sheer El Showk,
Tamera Lanham, Timothy Telleen-Lawton, Tom Brown, Tom Henighan, Tristan
Hume, Yuntao Bai, Zac Hatfield-Dodds, Jack Clark, Samuel R. Bowman, Amanda
Askell, Roger Grosse, Danny Hernandez, Deep Ganguli, Evan Hubinger, Nicholas
Schiefer, and Jared Kaplan. 2022. Discovering Language Model Behaviors with
Model-Written Evaluations. arXiv:2212.09251 [cs.CL]
[46] Artyom Petrosyan. 2024. Most Used Languages Online by Share of Websites
2024. https://www.statista.com/statistics/262946/most-common-languages-on-
the-internet/ Accessed on: 2024-06-02.
[47] Matt Post. 2018. SacreBLEU: A Standardized BLEU Score. https://github.com/
mjpost/sacrebleu.
[48] Vinodkumar Prabhakaran, Rida Qadri, and Ben Hutchinson. 2022. Cultural
Incongruencies in Artificial Intelligence. arXiv:2211.13069 [cs.CY]
[49] Ava Rosenbaum, Amanda Higgins, Nicole Kim, and Justin Meszler. 2018. Personal
Space and American Individualism. https://brownpoliticalreview.org/2018/10/
personal-space-american-individualism/ Accessed on: 2024-06-03.
[50] Caitlin Scroope. 2021.
Japanese Culture - Core Concepts.
https:
//culturalatlas.sbs.com.au/japanese-culture/japanese-culture-core-concepts#:
~:text=Japanese%20society%20is%20generally%20collectivistic,or%20a%
20broader%20social%20group Accessed on: 2024-06-03.
[51] Mrinank Sharma, Meg Tong, Tomasz Korbak, David Duvenaud, Amanda
Askell, Samuel R. Bowman, Newton Cheng, Esin Durmus, Zac Hatfield-Dodds,
Scott R. Johnston, Shauna Kravec, Timothy Maxwell, Sam McCandlish, Ka-
mal Ndousse, Oliver Rausch, Nicholas Schiefer, Da Yan, Miranda Zhang, and
Ethan Perez. 2023. Towards Understanding Sycophancy in Language Models.
arXiv:2310.13548 [cs.CL]
[52] Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, and David Krueger.
2022. Defining and Characterizing Reward Hacking. arXiv:2209.13085 [cs.LG]
[53] Nate Soares and Benja Fallenstein. 2015. Aligning Superintelligence with Human
Interests: A Technical Research Agenda. In Machine Intelligence Resaerch Institute.
https://api.semanticscholar.org/CorpusID:14393270
[54] Taylor Sorensen, Jared Moore, Jillian Fisher, Mitchell Gordon, Niloofar
Mireshghallah, Christopher Michael Rytting, Andre Ye, Liwei Jiang, Ximing
Lu, Nouha Dziri, Tim Althoff, and Yejin Choi. 2024. A Roadmap to Pluralistic
Alignment. arXiv:2402.05070 [cs.AI]
[55] Jacob Steinhardt. 2023. Emergent deception and emergent optimization. https:
//bounded-regret.ghost.io/emergent-deception-optimization/. Accessed: 2024-6-
2.
[56] Gemma Team, Thomas Mesnard, Cassidy Hardin, Robert Dadashi, Surya Bhupati-
raju, Shreya Pathak, Laurent Sifre, Morgane Rivière, Mihir Sanjay Kale, Juli-
ette Love, Pouya Tafti, Léonard Hussenot, Pier Giuseppe Sessa, Aakanksha
Chowdhery, Adam Roberts, Aditya Barua, Alex Botev, Alex Castro-Ros, Am-
brose Slone, Amélie Héliou, Andrea Tacchetti, Anna Bulanova, Antonia Paterson,
Beth Tsai, Bobak Shahriari, Charline Le Lan, Christopher A. Choquette-Choo,
Clément Crepy, Daniel Cer, Daphne Ippolito, David Reid, Elena Buchatskaya, Eric
Ni, Eric Noland, Geng Yan, George Tucker, George-Christian Muraru, Grigory
Rozhdestvenskiy, Henryk Michalewski, Ian Tenney, Ivan Grishchenko, Jacob
Austin, James Keeling, Jane Labanowski, Jean-Baptiste Lespiau, Jeff Stanway,
Jenny Brennan, Jeremy Chen, Johan Ferret, Justin Chiu, Justin Mao-Jones, Kather-
ine Lee, Kathy Yu, Katie Millican, Lars Lowe Sjoesund, Lisa Lee, Lucas Dixon,
Machel Reid, Maciej Mikuła, Mateo Wirth, Michael Sharman, Nikolai Chinaev,
Nithum Thain, Olivier Bachem, Oscar Chang, Oscar Wahltinez, Paige Bailey,
Paul Michel, Petko Yotov, Rahma Chaabouni, Ramona Comanescu, Reena Jana,
Rohan Anil, Ross McIlroy, Ruibo Liu, Ryan Mullins, Samuel L Smith, Sebastian
Borgeaud, Sertan Girgin, Sholto Douglas, Shree Pandya, Siamak Shakeri, So-
ham De, Ted Klimenko, Tom Hennigan, Vlad Feinberg, Wojciech Stokowiec, Yu
hui Chen, Zafarali Ahmed, Zhitao Gong, Tris Warkentin, Ludovic Peran, Minh
Giang, Clément Farabet, Oriol Vinyals, Jeff Dean, Koray Kavukcuoglu, Demis
Hassabis, Zoubin Ghahramani, Douglas Eck, Joelle Barral, Fernando Pereira, Eli
Collins, Armand Joulin, Noah Fiedel, Evan Senter, Alek Andreev, and Kathleen
Kenealy. 2024. Gemma: Open Models Based on Gemini Research and Technology.
arXiv:2403.08295 [cs.CL]
[57] NLLB Team, Marta R. Costa-jussà, James Cross, Onur Çelebi, Maha Elbayad,
Kenneth Heafield, Kevin Heffernan, Elahe Kalbassi, Janice Lam, Daniel Licht,
Jean Maillard, Anna Sun, Skyler Wang, Guillaume Wenzek, Al Youngblood, Bapi
Akula, Loic Barrault, Gabriel Mejia Gonzalez, Prangthip Hansanti, John Hoff-
man, Semarley Jarrett, Kaushik Ram Sadagopan, Dirk Rowe, Shannon Spruit,
Chau Tran, Pierre Andrews, Necip Fazil Ayan, Shruti Bhosale, Sergey Edunov,
Angela Fan, Cynthia Gao, Vedanuj Goswami, Francisco Guzmán, Philipp Koehn,
Alexandre Mourachko, Christophe Ropers, Safiyyah Saleem, Holger Schwenk,
and Jeff Wang. 2022. No Language Left Behind: Scaling Human-Centered Machine
Translation. arXiv:2207.04672 [cs.CL]
[58] Alejandro Tlaie. 2024. Exploring and steering the moral compass of Large Lan-
guage Models. arXiv:2405.17345 [cs.AI]
[59] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne
Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro,
Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, and Guil-
laume Lample. 2023. LLaMA: Open and Efficient Foundation Language Models.
arXiv:2302.13971 [cs.CL]
[60] Robert Vacareanu, Vlad-Andrei Negru, Vasile Suciu, and Mihai Surdeanu. 2024.
From Words to Numbers: Your Large Language Model Is Secretly A Capable
Regressor When Given In-Context Examples. arXiv:2404.07544 [cs.CL]
[61] Josef Valvoda, Ryan Cotterell, and Simone Teufel. 2022. On the Role of Negative
Precedent in Legal Outcome Prediction. arXiv:2208.08225 [cs.CY]
[62] Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel
Khashabi, and Hannaneh Hajishirzi. 2023. Self-Instruct: Aligning Language
Models with Self-Generated Instructions. arXiv:2212.10560 [cs.CL]
[63] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia,
Ed Chi, Quoc Le, and Denny Zhou. 2023. Chain-of-Thought Prompting Elicits
Reasoning in Large Language Models. arXiv:2201.11903 [cs.CL]
[64] Ziang Xiao, Q. Vera Liao, Michelle X. Zhou, Tyrone Grandison, and Yunyao Li.
2023. Powering an AI Chatbot with Expert Sourcing to Support Credible Health
Information Access. arXiv:2301.10710 [cs.HC]
[65] Shaoyang Xu, Weilong Dong, Zishan Guo, Xinwei Wu, and Deyi Xiong. 2024.
Exploring Multilingual Concepts of Human Value in Large Language Models: Is
Value Alignment Consistent, Transferable and Controllable across Languages?
arXiv:2402.18120 [cs.CL]
[66] Josephine Yuh. 2016. Blog Entry – Culture: South Korea, A Collectivist Society in
Confucianism. https://sites.psu.edu/global/2016/09/06/blog-entry-culture-south-
korea-a-collectivist-society-in-confucianism/ Accessed on: 2024-06-03.
[67] Peter Zhang. 2023. Taking Advice from ChatGPT. arXiv:2305.11888 [cs.HC]
[68] Peitian Zhang, Ninglu Shao, Zheng Liu, Shitao Xiao, Hongjin Qian, Qiwei Ye,
and Zhicheng Dou. 2024. Extending Llama-3’s Context Ten-Fold Overnight.
arXiv:2404.19553 [cs.CL]
[69] Simon Zhuang and Dylan Hadfield-Menell. 2021. Consequences of Misaligned
AI. arXiv:2102.03896 [cs.AI]
A
AI Alignment Goals
AI alignment is a recent research endeavor that aims to allow for
AI applications to behave in terms of what humans want them to
do and what humans value [28]. AI alignment is especially relevant
since AI has gotten increasingly complex and innovative over the
years. LLMs are able to generalize across tasks ([6]; [3]) and engage
in multi-step reasoning ([63]; [62]), which are useful applications
for many real-world tasks. However, given that AI is now com-
pleting many arguably human tasks, it is essential that we prevent
misalignment from AI systems ([53]; [15]). LLMs, although possess-
ing great skills, have already shown some behaviors which include
untruthful answers [4], obsequiousness ([45]; [51]), and deception
([55]; [42]), meaning there are many concerns about advanced AI
systems that are hard to control [24]. While many attempts have
been made to abet misalignment, such as, human feedback and
reward modeling, these attempts do not take into account that
people have diverse societal values and diverse mindsets. Human
annotators often add their own implicit biases into attempts to
evaluate AI output by people [44] [40] (or even deliberate biases
[7]), and reward modeling in particular can lead to reward hacking
([69]; [52]). Another potential solution is building a human-level
automated alignment researcher, which requires extensive com-
pute to allow for safe superintelligence [29], but this has yet to
be fully researched. To solve misalignment, AI systems must be

--- Page 10 ---

KDD ’25, August 03–07, 2025, Toronto, Canada
Julia Kharchenko, Tanya Roosta, Aman Chadha, and Chirag Shah
in line with both human intentions and human values [24]. Our
work ties into general AI alignment since we seek to determine
whether language models represent variance in values from coun-
try to country, whether there is a difference between prompting
in the native language or the persona approach (which approach
retains the country’s values the most), and most importantly, what
is the ideal behavior of models when it comes to embodying our
varying values across countries?
B
Hofstede Cultural Dimensions
There have been many attempts to define values that different
cultures have. Going back to 1951, U.S. sociologists Talcott Parsons
and Edward Shills defined cultural values as boiling down to choices
between pairs of alternatives, including affectivity, self-orientation
vs. collectivity-orientation, universalism, ascription, and specificity
[43]. After greater improvements in the field of value collection
from Florence Kluckhohn and Fred Strodtbeck [26], Mary Douglas
[10], Inkeles and Levinson [23], Geert Hofstede [16] developed five
unique cultural dimensions that take into account prior research on
political systems (Gregg and Banks’ [14]), economic development
(Adelman and Morris’ [1]), mental health (Lynn and Hampson’s
[34]). Hofstede cultural dimensions are a way of defining values of
different cultures based on pattern variables, or choices between
pairs of alternatives. Although the data was initially collected in the
1980s, the validity of the cultural dimensions has held up to time
as new data gets added ([20]; [36]; [21]). The most recent follow
up studies have been in 2021 [37], and 2022 [38], showing that
Hofstede cultural dimensions are relevant to the current day.
When considering other values to consider when analyzing
LLMs, we examined GLOBE values – a large-scale study of leader-
ship ideals, trust, and other cultural practices within 150 different
countries – which build off the work of Hofstede cultural dimen-
sions [12]. However, while both Hofstede cultural dimensions, and
GLOBE values have their origin in conducting research in the work-
force, we found that GLOBE values are overly reliant on workforce
and coworker/manager relations, and would not generalize as well
to other, more diverse situations that values, such as Individualism
vs. Collectivism could fall in. Furthermore, GLOBE values were
supplied in ranges that are not as intuitive to understand, whereas
Hofstede cultural dimensions are given as granular values, making
it easier to compare values between countries.
C
Comparison Between Japanese and American
Values
According to Hofstede cultural dimensions, Japan has an Individu-
alistic vs. Collectivist score of 62, meaning that Japan is an individu-
alistic country; in terms of granularity, Japan is more individualistic
than the United States, which has an Individualistic vs. Collectivist
score of 60. However, each LLM we tested along with each approach
we tested perceived the United States as predominantly individ-
ualistic and Japan as predominantly collectivist, with the largest
discrepancy being within the personas approach for Command-R,
where 72.40% of responses for the American persona were individ-
ualistic and only 19.60% of answers for the Japanese persona where
individualistic. This may be because much of English language
data represents Japan as a collectivist country [50] and the United
States as an individualistic country [49], leading to stereotypical
representations of each country rather than true representations ac-
cording to their Hofstede cultural dimensions. These findings hold
for other individualistic countries often perceived as collectivist,
such as South Korea [66].
D
Performance Differences Between GPT4 and
GPT4o
Of the given values, GPT4o had an increase in performance (higher
correlations between the country’s value and the percentage of re-
sponses indicating that country’s value) with the persona approach
for the values MAS (+27.188%), PDI (+18.343%), and Individualism
vs. Collectivism (+17.794%). However, GPT4o had a decrease in
performance for Uncertainty Avoidance (-42.497%) and Orienta-
tion (-70.656%) for the personas approach. For the multilingual
approach, GPT4o had an increase in performance for the values
Uncertainty Avoidance (+166.30%) and Orientation (+74.660%), but
a surprising decrease in performance in the values Individualism
vs. Collectivism (-6.143%), MAS (-42.708%), and PDI (-107.354%),
a direct inverse of the results from the personas approach. This
tells us that increases in performance using personas and increases
in performance using different languages are not inherently con-
nected, as their improvements may stem from different model opti-
mizations. For instance, increases in performance using personas
would stem primarily from improving the quality of existing data
- given that throughout our study, we prompted personas strictly
using English - to allow for each cultural representation through-
out English to be more accurate and respectful, while increases in
performance using different languages would stem from having
more data throughout other languages so that each model can have
a better understanding of a country’s/language’s cultures by being
able to acquire more data from it and create its own generaliza-
tions. In other words, increases in performance using personas can
potentially stem from increasing cultural representations through-
out English-language data, incorporating more diverse data and
representations by culturally-informed and semantically-informed
approaches, whereas increases in performance using multilingual
approaches may stem from gathering enough data in each language
so that LLMs are able to generalize their cultural values and in-
formation by sheer amount of data, so that LLMs are able to form
their own cultural understandings in other languages rather than
relying on an understanding of other cultures drawn from English
language (and often, outsider) data.
E
Full Data and Visualizations
Full data and visualizations are shown starting from the next page.

--- Page 11 ---

How Well Do LLMs Represent Values Across Cultures?
Empirical Analysis of LLM Responses Based on Hofstede Cultural Dimensions
KDD ’25, August 03–07, 2025, Toronto, Canada
Figure 3: GPT4o adhering well to individualism vs. collectivist value for high-resource languages
Language
Resource Level
Individualistic Collectivist Score
MAS Score
Uncertainty Avoidance Score
Power Distance Index Score
Long Term Orientation Score
Target Nationality
English
High
60
62
46
40
50
The United States
German
High
79
66
65
35
57
Germany
Italian
High
53
70
75
50
39
Italy
Dutch
High
100
14
53
38
67
The Netherlands
Russian
High
46
36
95
93
58
Russia
Japanese
High
62
95
92
54
100
Japan
French
High
74
43
86
68
60
France
Mandarin Chinese
High
43
66
30
80
77
China
Indonesian
High
5
46
48
78
29
Indonesia
Turkish
High
46
45
85
66
35
Turkey
Polish
High
47
64
93
68
49
Poland
Persian
High
23
43
59
58
30
Iran
Hungarian
Mid
71
88
82
46
45
Hungary
Swedish
Mid
87
5
29
31
52
Sweden
Hebrew
Mid
56
47
81
13
47
Israel
Danish
Mid
89
16
23
18
59
Denmark
Finnish
Mid
75
26
59
33
63
Finland
Korean
Mid
58
39
85
60
86
South Korea
Czech
Mid
70
57
74
57
51
Czech Republic
Ukrainian
Mid
55
27
95
92
51
Ukraine
Greek
Mid
59
57
100
60
51
Greece
Romanian
Mid
46
42
90
90
32
Romania
Thai
Mid
19
34
64
64
67
Thailand
Bulgarian
Mid
50
40
85
70
51
Bulgaria
Icelandic
Low
83
10
50
30
57
Iceland
Afrikaans
Low
23
63
49
49
18
South Africa
Kazakh
Low
20
50
88
88
85
Kazakhstan
Armenian
Low
17
50
88
85
38
Armenia
Georgian
Low
15
55
85
65
24
Georgia
Albanian
Low
27
80
70
90
56
Albania
Azerbaijani
Low
28
50
88
85
59
Azerbaijan
Malay
Low
27
50
36
100
47
Malaysia
Mongolian
Low
37
29
39
93
39
Mongolia
Belarusian
Low
48
20
95
95
53
Belarus
Hindi
Low
24
56
40
77
51
India
Sinhala
Low
35
10
45
80
45
Sri Lanka
Table 4: Language and Hofstede Cultural Dimensions Metadata

--- Page 12 ---

KDD ’25, August 03–07, 2025, Toronto, Canada
Julia Kharchenko, Tanya Roosta, Aman Chadha, and Chirag Shah
LLM
Value
Personas Approach
Multilingual Approach
GPT 4
Individualism
vs
Collectivism
MAS
PDI
Orientation
Uncertainty
Avoidance
Table 5: Graphs showing value differentiation across all models, approaches, and values. Green represents collectivist countries,
high MAS countries, low PDI countries, long term orientation countries, and high uncertainty avoidance countries, for applicable
values. Orange represents individualisic countries, low MAS countries, high PDI countries, short term orientation countries,
and low uncertainty avoidance countries, for applicable values.

--- Page 13 ---

How Well Do LLMs Represent Values Across Cultures?
Empirical Analysis of LLM Responses Based on Hofstede Cultural Dimensions
KDD ’25, August 03–07, 2025, Toronto, Canada
GPT 4o
Individualism
vs
Collectivism
MAS
PDI
Orientation
Uncertainty
Avoidance
LLAMA 3
Individualism
vs
Collectivism
Table 6: Graphs showing value differentiation across all models, approaches, and values (continuation). Green represents
collectivist countries, high MAS countries, low PDI countries, long term orientation countries, and high uncertainty avoidance
countries, for applicable values. Orange represents individualisic countries, low MAS countries, high PDI countries, short term
orientation countries, and low uncertainty avoidance countries, for applicable values (continuation).

--- Page 14 ---

KDD ’25, August 03–07, 2025, Toronto, Canada
Julia Kharchenko, Tanya Roosta, Aman Chadha, and Chirag Shah
MAS
PDI
Orientation
Uncertainty
Avoidance
Command R
Plus
Individualism
vs
Collectivism
MAS
Table 7: Graphs showing value differentiation across all models, approaches, and values (continuation). Green represents
collectivist countries, high MAS countries, low PDI countries, long term orientation countries, and high uncertainty avoidance
countries, for applicable values. Orange represents individualisic countries, low MAS countries, high PDI countries, short term
orientation countries, and low uncertainty avoidance countries, for applicable values (continuation).

--- Page 15 ---

How Well Do LLMs Represent Values Across Cultures?
Empirical Analysis of LLM Responses Based on Hofstede Cultural Dimensions
KDD ’25, August 03–07, 2025, Toronto, Canada
PDI
Orientation
Uncertainty
Avoidance
Gemma
Individualism
vs
Collectivism
MAS
PDI
Table 8: Graphs showing value differentiation across all models, approaches, and values (continuation). Green represents
collectivist countries, high MAS countries, low PDI countries, long term orientation countries, and high uncertainty avoidance
countries, for applicable values. Orange represents individualisic countries, low MAS countries, high PDI countries, short term
orientation countries, and low uncertainty avoidance countries, for applicable values (continuation).

--- Page 16 ---

KDD ’25, August 03–07, 2025, Toronto, Canada
Julia Kharchenko, Tanya Roosta, Aman Chadha, and Chirag Shah
Orientation
Uncertainty
Avoidance
Table 9: Graphs showing value differentiation across all models, approaches, and values. Green represents collectivist countries,
high MAS countries, low PDI countries, long term orientation countries, and high uncertainty avoidance countries, for applicable
values. Orange represents individualisic countries, low MAS countries, high PDI countries, short term orientation countries,
and low uncertainty avoidance countries, for applicable values (continuation).

--- Page 17 ---

How Well Do LLMs Represent Values Across Cultures?
Empirical Analysis of LLM Responses Based on Hofstede Cultural Dimensions
KDD ’25, August 03–07, 2025, Toronto, Canada
LLM
Value
Personas Approach
Multilingual Approach
GPT 4
Individualism
vs
Collectivism
MAS
PDI
Orientation
Table 10: Graphs showing correlations between percentage of responses indicating a value and the country’s value across all
approaches, values, and LLMs.

--- Page 18 ---

KDD ’25, August 03–07, 2025, Toronto, Canada
Julia Kharchenko, Tanya Roosta, Aman Chadha, and Chirag Shah
Uncertainty
Avoidance
GPT 4o
Individualism
vs
Collectivism
MAS
PDI
Table 11: Graphs showing correlations between percentage of responses indicating a value and the country’s value across all
approaches, values, and LLMs (continuation).

--- Page 19 ---

How Well Do LLMs Represent Values Across Cultures?
Empirical Analysis of LLM Responses Based on Hofstede Cultural Dimensions
KDD ’25, August 03–07, 2025, Toronto, Canada
Orientation
Uncertainty
Avoidance
LLaMA 3
Individualism
vs
Collectivism
MAS
Table 12: Graphs showing correlations between percentage of responses indicating a value and the country’s value across all
approaches, values, and LLMs (continuation).

--- Page 20 ---

KDD ’25, August 03–07, 2025, Toronto, Canada
Julia Kharchenko, Tanya Roosta, Aman Chadha, and Chirag Shah
PDI
Orientation
Uncertainty
Avoidance
Command R
Plus
Individualism
vs
Collectivism
MAS
Table 13: Graphs showing correlations between percentage of responses indicating a value and the country’s value across all
approaches, values, and LLMs (continuation).

--- Page 21 ---

How Well Do LLMs Represent Values Across Cultures?
Empirical Analysis of LLM Responses Based on Hofstede Cultural Dimensions
KDD ’25, August 03–07, 2025, Toronto, Canada
PDI
Orientation
Uncertainty
Avoidance
Gemma
Individualism
vs
Collectivism
MAS
Table 14: Graphs showing correlations between percentage of responses indicating a value and the country’s value across all
approaches, values, and LLMs (continuation).

--- Page 22 ---

KDD ’25, August 03–07, 2025, Toronto, Canada
Julia Kharchenko, Tanya Roosta, Aman Chadha, and Chirag Shah
PDI
Orientation
Uncertainty
Avoidance
Table 15: Graphs showing correlations between percentage of responses indicating a value and the country’s value across all
approaches, values, and LLMs.

```
