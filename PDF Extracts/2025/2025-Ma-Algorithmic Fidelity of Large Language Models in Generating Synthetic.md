---
title: "2025-Ma-Algorithmic Fidelity of Large Language Models in Generating Synthetic - PDF Extract"
source_pdf: "2025-Ma-Algorithmic Fidelity of Large Language Models in Generating Synthetic.pdf"
pages: 25
extracted_at: "2026-02-15T17:54:26.994992"
---

# PDF Extract: 2025-Ma-Algorithmic Fidelity of Large Language Models in Generating Synthetic

**Source PDF:** 2025-Ma-Algorithmic Fidelity of Large Language Models in Generating Synthetic.pdf
**Total Pages:** 25

---

## Content

```
--- Page 1 ---

arXiv:2412.13169v2  [cs.CL]  2 Jun 2025
Algorithmic Fidelity of Large Language Models in Generating Synthetic
German Public Opinions: A Case Study
Bolei Ma∗1,2
Berk Yoztyurk∗1
Anna-Carolina Haensch1,2,3
Xinpeng Wang1,2
Markus Herklotz1
Frauke Kreuter1,2,3
Barbara Plank1,2
Matthias Assenmacher1,2
1LMU Munich, 2Munich Center for Machine Learning,
3University of Maryland, College Park
∗Equal contribution.
Correspondence: bolei.ma@lmu.de
Abstract
In recent research, large language models
(LLMs) have been increasingly used to inves-
tigate public opinions. This study investigates
the algorithmic fidelity of LLMs, i.e., the abil-
ity to replicate the socio-cultural context and
nuanced opinions of human participants. Using
open-ended survey data from the German Lon-
gitudinal Election Studies (GLES), we prompt
different LLMs to generate synthetic public
opinions reflective of German subpopulations
by incorporating demographic features into the
persona prompts. Our results show that Llama
performs better than other LLMs at represent-
ing subpopulations, particularly when there is
lower opinion diversity within those groups.
Our findings further reveal that the LLM per-
forms better for supporters of left-leaning par-
ties like The Greens and The Left compared
to other parties, and matches the least with
the right-party AfD. Additionally, the inclu-
sion or exclusion of specific variables in the
prompts can significantly impact the models’
predictions. These findings underscore the im-
portance of aligning LLMs to more effectively
model diverse public opinions while minimiz-
ing political biases and enhancing robustness
in representativeness.1
1
Introduction
Recent advances in LLMs have generated signifi-
cant interest in their potential for synthetic data
generation across various domains. A key and
widely debated question is whether LLMs can pro-
duce synthetic data that accurately represent human
opinions (Argyle et al., 2023; Santurkar et al., 2023;
Veselovsky et al., 2023; von der Heyde et al., 2025;
Long et al., 2024, inter alia).
In social science research, it is usually surveys
that provide insights into the attitudes and opinions
1The code for experiments and evaluation is available at
https://github.com/soda-lmu/llm-opinion-german.
05-11-2019
21-04-2020
03-11-2020
25-02-2021
06-05-2021
07-07-2021
11-08-2021
15-09-2021
29-09-2021
09-12-2021
0
0.1
0.2
0.3
0.4
0.5
0.6
Social Policy
Migration and  Integration
Environmental  Policy
Economic  Policy
Health Policy
GLES Survey Dates
Frequency
Health Policy
Social Policy
Environmental  Policy
Migration and  Integration
Economic  Policy
Figure 1: The distribution of the top 5 answer categories
between November 2019 and November 2021 in the
German GLES survey. There is a significant surge in
the Health Policy category from November 2019 to
April 2020, with it becoming the dominant focus during
this period and afterwards, likely due to the outbreak of
COVID-19 in early 2020.
of a population. Recent studies have explored us-
ing information from survey responses for LLM
prompts, i.e., creating so-called personas and then
using the LLM “responses” to additional questions
(Argyle et al., 2023; Dominguez-Olmedo et al.,
2024; Durmus et al., 2024, inter alia). Assessing
the fidelity of LLMs in capturing and reproduc-
ing human opinions deepens our understanding of
model behavior while at the same time helping re-
searchers design more reliable models aligned with
human values and improving their usability (Ma
et al., 2024). Among these studies, Argyle et al.
(2023) introduced the algorithmic fidelity, a con-
cept for assessing how effectively LLMs replicate
the socio-cultural context and nuanced opinions of
diverse human subpopulations. Their work used
1

--- Page 2 ---

LLMs to generate synthetic responses (“silicon
samples”) informed by demographic and ideologi-
cal profiles from political science datasets. Their
findings suggest that LLMs can closely approx-
imate real-world opinion distributions in certain
contexts, such as U.S. elections, although chal-
lenges persist in fully aligning the generated data
with actual demographic groups.
Recent research on LLM responses to opin-
ion polling have predominantly focused on US-
based and English-centric survey data. For ex-
ample, von der Heyde et al. (2025) evaluated the
algorithmic fidelity of GPT-3.5 in predicting Ger-
man voting behavior. Their findings revealed that
while GPT-3.5 accurately represented the voting
patterns of center and left-leaning political groups,
it struggled to capture those of right-leaning parties.
However, like many similar studies, their analysis
was limited to closed-ended survey questions with
single-choice responses. This highlights a key chal-
lenge: while LLMs may perform well in English-
speaking contexts, less is known about their ability
to generate representative opinions in non-English-
speaking countries and for open-ended questions.
This is particularly true for open-ended setups,
where scaling and accurately interpreting responses
pose significant challenges (Resnik et al., 2024).
To address these challenges, this study explores
the algorithmic fidelity of LLMs in generating syn-
thetic public opinions in an open-ended survey
question based on German survey data. We use the
survey question about the most important problems
facing Germany today from the German Longitu-
dinal Election Study (GLES). The survey is a lon-
gitudinal panel survey, and the answer distribution
can be found in Figure 1. We select variables from
the original survey data to represent survey partic-
ipants with their characteristics as personas. We
include three LLMs (Gemma, Llama2, Mixtral) in
our study and prompt them to simulate survey par-
ticipants to answer the open-ended question about
the most important political problem in Germany.
Finally, we compare the outputs regarding the dis-
tributional alignment with original survey answers,
predictive performance, and answer diversity. Our
most important findings are:
(1) Llama2 is better at modeling group opinions
(§4.1).
(2) Llama2’s representativeness fluctuates across
survey waves, with the model’s representative-
ness of the population decreasing as survey
diversity increases; the model represents sub-
population opinions unevenly, with favorable
alignment for left-leaning parties (such as the
Left, the Greens) over right-parties (such as
AfD) (§4.2).
(3) Including more variables in prompts improves
performance, with party affiliation being the
most influential factor (§4.3).
2
Related Work
LLMs for Survey Response Generation.
Re-
cent studies have increasingly repurposed survey
questionnaires, originally designed for public opin-
ion polling, to assess the opinions generated by
LLMs (Ma et al., 2024). For instance, Santurkar
et al. (2023) identified significant differences be-
tween LLM opinion distributions and US-based
survey participants. Similarly, Dominguez-Olmedo
et al. (2024) highlighted disparities between LLM
and human opinions, emphasizing the sensitivity
of model outputs to biases in prompting. Tjuatja
et al. (2024) found that LLMs are highly sensitive
to prompt perturbations and fail to replicate human-
like behavior. Collectively, these studies suggest
that LLMs align more closely with populations
holding left-leaning, Western-oriented values.
Opinion Generation in the German Contexts.
While most studies on opinions in LLM output
are English- and U.S.-centric, some research has
explored other contexts, such as the German case.
In a recent study, von der Heyde et al. (2025) em-
ployed the data of 2017 post-election cross-section
of the GLES. Respondents to this study reported
their vote choice in the survey. von der Heyde et al.
(2025) prompted GPT-3.5 (Brown et al., 2020) with
personas to simulate the survey participants. Based
on the close-ended choice setup, they found that
it does not predict citizens’ vote choice accurately,
exhibiting a bias towards the Green and Left parties,
similar to previous work in English contexts.
Evaluation of LLM Outputs.
Previous stud-
iesprimarily focused on closed-ended multiple-
choice questions, often relying on the model’s
first token prediction (e.g., Santurkar et al., 2023;
Dominguez-Olmedo et al., 2024; Tjuatja et al.,
2024) or semi-automated extraction of text an-
swers (von der Heyde et al., 2025). Alternatively,
Wang et al. (2024a,b) proposed training a classifier
directly on LLM responses manually labeled by
2

--- Page 3 ---

annotators, finding this method more robust. Af-
ter the output extraction, a few evaluation metrics
have been applied to measure the alignment of hu-
man and LLM responses (Ma et al., 2024), such
as Cohen’s Kappa (Argyle et al., 2023; Hwang
et al., 2023), 1-Wasserstein distance (Santurkar
et al., 2023; Hwang et al., 2023), KL divergence
(Dominguez-Olmedo et al., 2024; Sun et al., 2024),
Euclidean distance (Wang et al., 2023), Jensen-
Shannon distance (Durmus et al., 2024), etc. and
correlation and statistical analyses (Sun et al., 2024;
Jiang et al., 2024b). For our case study, we adapt
these metrics to examine the fidelity of LLM-
generated synthetic German public opinions.
3
Experimental Setups
3.1
Data
German Longitudinal Election Study (GLES
Panel).
We use the GLES Panel dataset from
GESIS (2023). The survey consists of 21 waves2
and contains socio-demographic information, vote
intentions, choices, and political attitudes of par-
ticipants. The target population is German citi-
zens eligible to vote during the respective elections
in Germany. Along with the respondents’ socio-
demographic data for our prompts, we use respon-
dents’ answers to the question “In your opinion,
what is the most important problem facing Ger-
many today?” for comparing human answers and
LLM outputs. The answers of participants were
collected as free-form texts.
Selected Information.
We included six variables
from the original survey: age, gender, leaning
party, region, education degree, and vocational de-
gree. Details on the sub-groups of the variables are
shown in §A.
Coding Scheme.
For coding the LLM text re-
sponses into categories, we follow the coding
scheme proposed in an additional sub-study of the
GLES (GESIS, 2024). Like Mellon et al. (2024),
who collapsed ∼50 classes into a simpler classi-
fication, we also set “coarse” classes (n=16). We
merged rarely represented classes into an upper
class (e.g., “Price Level”, “Housing Policy”, and
“Economic Policy” classes into one “Economic Pol-
icy” class). The distribution of GLES survey an-
swers based on the coarse classes is shown in Fig-
2A survey wave refers to a single round of data collec-
tion in a panel survey, gathering information from the same
participants at multiple points in time (Andreß et al., 2013).
ure 1. The full list of fine and coarse classes can be
found in §B in the Appendix.
3.2
Text Generation
Models.
We chose three instruction-tuned open-
weight LLMs:
Llama-2-13b-chat-hf (Tou-
vron et al., 2023), Gemma-7b-it (Team, 2024),
and Mixtral-8x7B-Instruct-v0.1 (Jiang et al.,
2024a).
Prompt Design.
After initial trial runs and in-
specting the LLM outputs, we used the prompt in
Figure 2 in our experiments with LLMs. We chose
German as the prompting language, as it is the lan-
guage in which the GLES survey was conducted,
and the generated texts can be compared to the
original text. During the experimentation phase,
the placeholders are replaced with the respondent’s
information, i.e., the variables from the survey data.
Identify the most important problem Germany in {month}
{year} is facing. Provide the answer in one concise sen-
tence, focusing on a single issue without elaborating or
listing additional problems. Do not repeat the informa-
tion you have been given and give your answer directly
and without introductory phrases. Answer in German and
only in German, do not use English. Answer from the
perspective of a respondent with German citizenship and
the characteristics specified below.
{article} (The) respondent is {age} years old and {gender}.
{pronoun} {educational_qualification_clause } and {voca-
tional_qualification_clause} {pronoun2} lives in {region}
and mainly supports {party}.
Figure 2: Translated prompt in English. The original
prompt in German is presented in Figure 9 in Appendix.
3.3
LLM Output Classification
To evaluate and compare the LLM outputs with
human responses, we needed to categorize the re-
sponses into specific classes and trained a classifier
to code the responses from the LLMs.
Manual Annotation.
Drawing from Wang et al.
(2024a,b), we manually annotated 1,500 LLM out-
puts, selecting 500 outputs randomly from each
LLM. We then trained a classifier based on the man-
ually developed annotation scheme for the LLM
outputs. Details on the scheme can be found in §C.
Classifier Training and Inference.
We fine-
tuned the German version of the base BERT
(Devlin et al., 2019) classifier on the annotated
LLM outputs. The fine-tuned classifier achieves a
weighted F1 score of 0.93 on the test set. The clas-
sifier is then used to classify all LLM responses.
3

--- Page 4 ---

3.4
Evaluation Metrics for Experiments
In the context of generative models, representative-
ness is the model’s ability to recover population-
level properties of the original data (Eigenschink
et al., 2023), i.e., a dimension of algorithmic fi-
delity. To compare the representativeness of the
LLM answers with the original survey data and to
measure the association between the variables, we
used the following evaluation metrics.
Jensen-Shannon (JS) Divergence.
JS diver-
gence is a symmetric and normalized measure of
divergence derived from KL divergence (Kullback
and Leibler, 1951). It is calculated as:
JSD(P ∥Q) = 1
2DKL(P ∥M) + 1
2DKL(Q ∥M)
(1)
where M = 1
2(P + Q) is the mixture distribu-
tion of P and Q (Lin, 2006). The JS divergence is
bounded between 0 and 1 (when using log2), mak-
ing it easier to interpret than KL divergence. We
use JS Distance, the square root of JS Divergence,
as in Durmus et al. (2024), because its bounded
range facilitates comparison across different data
waves. The JS distance is applied to measure the
representativeness of the coded LLM answers com-
pared to the real survey data.
Entropy.
Entropy measures the variability or un-
certainty in a set of outcomes (Jurafsky and Martin,
2024):
H(X) = −
X
x∈X
p(x) log p(x)
(2)
We use entropy to assess the diversity of text cate-
gories in synthetic and survey data. Lower entropy
indicates less variability, meaning fewer bits are
needed to represent the information in the data.
Conditional Entropy.
Conditional entropy mea-
sures the remaining uncertainty in variable X when
another variable Y is known. It calculates the en-
tropy of X given the distribution of Y :
H(X | Y ) =
X
y∈AY
P(y)

X
x∈AX
P(x | y) log
1
P(x | y)


=
X
x∈AX
X
y∈AY
P(x, y) log
1
P(x | y)
(3)
We use conditional entropy to evaluate how much
uncertainty remains about responses in the survey
when the subpopulation is known. This helps as-
sess whether the synthetic data captures patterns in
specific groups within the population.
Information Gain.
Also called mutual informa-
tion. It measures how much information one ran-
dom variable provides about another. It is calcu-
lated as the difference between the entropy of the
variable and its conditional entropy given another
variable:
I(X; Y ) = H(Y ) −H(Y | X)
(4)
It indicates how much knowing one variable (e.g.,
X) reduces uncertainty about another variable (e.g.,
Y ). A higher information gain indicates that know-
ing one variable reduces uncertainty about another
variable. In our experiments, we calculate the pop-
ulation entropy H(Y ) and conditional subpopula-
tion entropy H(Y | X), where X represents de-
mographic features. We will compute H(Y ) and
H(Y | X) for subpopulations and compare the
information gained in survey and LLM data.
Cramér’s V.
This is a measure of association
between nominal variables (Cramér, 1999). It is
based on Pearson’s χ2 test. However, Cramér’s V
discounts the value of the χ2 statistic for both the
sample size (N) and the size of the table of counts
(minimum of row count or column count minus 1 )
(Holbrook, 2022). It is computed as:
V =
s
χ2
N · min(r −1, c −1)
(5)
We use Cramérs’ V to check “pattern correspon-
dence” in LLM outputs. We map each input vari-
able (Xi) to the output variable (Y), and check
whether the pairwise correlations in survey data are
also present in the LLM-generated data.
4
Experiments and Results
Three main experiments were conducted on the
GLES data. The first evaluated all three LLMs
using a single wave, focusing on dataset statistics
and representativeness (§4.1). The second extended
this analysis across multiple waves with Llama2
to track performance over time (§4.2). The third
involved ablation studies to assess how different
variables affect representativeness and response
diversity (§4.3).
4.1
Experiment 1: Model Pre-Experiment in
One Wave
After dropping the observations with missing fea-
tures, we used the survey data from wave 12 (col-
lected between 05-11-2019 and 19-11-2019, i.e.,
before COVID-19) for the first experiment. All
4

--- Page 5 ---

Pop.
Subpop.
0.8
1
1.2
1.4
1.6
1.8
2
2.2
2.4
2.6
2.8
3
Pop.
Subpop.
Pop.
Subpop.
Pop.
Subpop.
0.8
1
1.2
1.4
1.6
1.8
2
2.2
2.4
2.6
2.8
3
Pop.
Subpop.
0.8
1
1.2
1.4
1.6
1.8
2
2.2
2.4
2.6
2.8
3
Pop.
Subpop.
Pop.
Subpop.
Pop.
Subpop.
0.8
1
1.2
1.4
1.6
1.8
2
2.2
2.4
2.6
2.8
3
Source
survey
Llama2
Mixtral
Die Linke
die AfD
die CDU/CSU
die FDP
die Grünen
die SPD
A minor party
No party
Figure 3: Information Gain for leaning party variable (Xi). Left: population entropy (H(Y )), right: subpopula-
tion entropy (H(Y | Xi)). A large gap between left and right (H(Y ) −H(Y | Xi)) means big information gain
when focusing on the samples of the subpopulation group, indicating responses with this group are less diverse.
three LLMs have been prompted to generate syn-
thetic answers. The generated answers are classi-
fied as stated in §3.3. We compared dataset statis-
tics and the textual style of the answers and com-
puted JS Distance and entropy.
In Table 1, we give an overview of statistics
about labels, textual characteristics, and representa-
tiveness (on the population level). 42 % of the
Gemma model answers were about COVID-19
(identified using Regex), even though the survey
answers were collected before COVID-19, which
indicates a very large proportion of hallucinations.
Therefore, we did not include the Gemma model
in the further subpopulation-level analysis. The
detailed JS Distances in each social group category
can be found in Table 14 in the Appendix.
Metric
Gemma
Llama2
Mixtral
Survey
Avg. Labels per Sample
1.03
1.20
1.33
1.03
Avg. Samples per Label
593
692
769
597
Avg. Word Count
36.37
25.65
43.75
2.29
Non-German Answer Rate
0.02
0.06
0.03
-
Non-response Rate
0
0
0.05
0.04
LLM Refusal Rate
1e-4
0
1e-4
-
COVID Regex Match Rate
0.42
0.03
2e-3
0
JS Distance to Survey
0.62
0.28
0.29
-
Answer Entropy
2.26
2.90
2.56
2.93
Table 1: Survey and LLM data statistics in experiment 1
A case study on information gain of the party
variables: Llama2 aligns more closely with sur-
vey data and maintains subgroup stability. Fig-
ure 3 compares population-level answer entropies
(left) with conditional entropies (right) for each
leaning party value. Information gain, calcu-
lated as the difference between these entropies,
reflects how much additional insight is provided
by knowing the leaning
party value.
The
population-level entropies (H(Y )) are close, with
the survey (2.93) closely matching Llama2 (2.90),
while Mixtral was a bit lower (2.56) (see left of
each subplot). After incorporating the leaning
party information and only looking at the samples
containing the specific party affiliations (H(Y |
Xi)), Mixtral shows still lower conditional entropy
(see right of each subplot), indicating less vari-
ation in responses. Especially for “Die Grünen
(The Greens)” and “AfD”, there are drastic drops
of H(Y | Xi). This suggests that Mixtral may risk
reflecting dominant group opinions, reducing diver-
sity, and showcasing stereotypical representations
of these subgroups. In contrast, Llama2 exhibits
less information gain, i.e., it is more aligned with
the survey data.
4.2
Experiment 2: Wave Experiment with
Llama2
We focused on Llama2 in the second in-depth ex-
periment and repeated the generation process for
the most 10 recent panel waves in GESIS (2023)
(waves 12-21). Over these two years, we observe
large shifts in survey label distributions (see Figure
1). This allows us to evaluate the representativeness
of the model under varying label distributions and
seek answers to the following questions:
• Do the LLM capabilities at both the population
and subpopulation levels vary over time?
5

--- Page 6 ---

12
13
14
15
16
17
18
19
20
21
12
13
14
15
16
17
18
19
20
21
12
13
14
15
16
17
18
19
20
21
12
13
14
15
16
17
18
19
20
21
12
13
14
15
16
17
18
19
20
21
12
13
14
15
16
17
18
19
20
21
age groups
education degree
gender
leaning party
region
vocational degree
0.15
0.2
0.25
0.3
0.35
0.4
0.45
0.5
0.55
0.6
age groups
18-29
30-44
45-59
60+
education degree
High school diploma
Higher education entrance qualification
Secondary school diploma
Intermediate school diploma
No school diploma
Is still student
gender
male
female
leaning party
Die Linke
die AfD
die CDU/CSU
die FDP
die Grünen
die SPD
A minor party
No party
region
East Germany
West Germany
vocational degree
in vocational training
Completed internship/volunteer work
Completed apprenticeship
Commercial or agricultural apprenticeship
Commercial apprenticeship
Vocational school diploma
University of applied sciences degree
Specialist school diploma
Master craftsman or technician qualification
University degree
No vocational training completed
Survey Waves
JS Distance
Figure 4: JS Distance of six subpopulation groups in Experiment 2. An in-depth presentation of the JS Distance for
each group is shown in Figure 13 in the Appendix.
• In which subpopulations are opinions repre-
sented more accurately?
Llama2 captures shifts in survey trends, but
higher answer diversity correlates with reduced
representativeness. For panel waves 12-21, we
repeated the text generation process and classified
the answers. Table 2 shows the population-level
entropy values and the JS distances. We calculated
Pearson’s correlation coefficient between survey
entropy and the JS distance and got r = −0.35, in-
dicating that the model’s representativeness of the
population decreases as the diversity in answers in-
creases. For wave 13, with data collection between
April 2020 and May 2020, the diversity of answers
reached its minimum (with an entropy of 0.58). In
Table 13, we see that 92.4 % of answers were about
“Health Policy” (and about the COVID-19). This
shows that LLMs’ responses reflect the change in
the survey date.
12
13
14
15
16
17
18
19
20
21
avg.
LLM entropy
2.90 0.58 1.67 1.31 2.12 2.20 2.27 2.46 2.46 2.49 2.04
survey entropy 2.93 2.02 2.24 2.31 2.53 2.82 2.75 2.85 2.92 2.19 2.55
JS distance
0.29 0.29 0.24 0.22 0.20 0.23 0.23 0.22 0.24 0.30 0.24
Table 2: Population level entropy values and the JS
distance in the Wave Experiment from wave 12-21.
Subpopulation-level findings: JS distances re-
veal representational variation influenced by
group information and complexity. Figure 4
shows the JS distances at the subpopulation level
for each variable. We observed the most variation
for education and leaning party variables. Al-
though the difference is smaller than the three vari-
ables above, gender and region have a consistent
JS difference regardless of panel waves. And no
age variable value consistently has a lower JS score.
It shows the model can represent the opinions of
different social groups at various levels but offers
no clear explanation for the variation in represen-
tation. This could come from better recognition of
certain groups’ views, the training data, or model
architecture. Another possibility is that some social
groups are more “informative” about this question.
Llama2 closely reflects sociodemographic pat-
terns, with minor deviations from survey influ-
ences. Cramér’s V values in Figure 14 in Appendix
show pairwise patterns between prompting vari-
ables and text answers. However, in comparison
with the survey’s values, we see that the model un-
derestimates the influence of age and education
degree on the text answers, the model consistently
overestimates the effect of region, and the gender
and party variables are both overestimated and
underestimated. However, except region, the dif-
ferences are usually less than 0.05, indicating that
the Llama2 closely reflects patterns between so-
ciodemographics and the survey.
A case study on party variables: Llama2 bet-
ter models groups with left-leaning parties. To
check how much of the JS distance can be associ-
ated with the modeling difficulty of the variables,
we plot the subpopulation entropy and JS distances
for leaning party in Figure 5. Since the popula-
tion entropy is the same for all subpopulations, we
can safely assume that lower conditional entropy
means higher information gain for that variable.
This allows us to examine how representativeness,
6

--- Page 7 ---

linked to the available information in a variable,
impacts alignment success. When mutual informa-
tion is high, LLMs can better model subpopulation
behavior. However, certain groups do not fall into
this trend line; “die Linke (the Left)” and “die Grü-
nen (the Greens)” are modeled better, and “AfD” is
worse (compared to the information their groups
carry). This finding aligns with previous work (e.g.,
Santurkar et al., 2023; von der Heyde et al., 2025),
which shows that LLMs tend to have a more left-
leaning feature. We show additional results on
other variables and observe similar results showing
that LLMs are biased towards left, Western, and
educated people in §G (4th paragraph).
die Grünen
die CDU/CSU
die SPD
die AfD
die FDP
No party
die Linke
A minor party
2.2
2.3
2.4
2.5
2.6
2.7
2.8
0.2
0.22
0.24
0.26
0.28
0.3
0.32
0.34
Subpopulation's Survey Entropy
JS Distance
Figure 5: Subpopulation entropy and JS distance for
leaning party (mean values for waves 12-21).
4.3
Experiment 3: Ablation Experiment
To further show how individual demographic in-
formation affects the LLM output diversity, we
conducted a series of ablation experiments with the
following variations:
• Including only one social group variable.
• Excluding one social group variable.
• Using no social group variables.
These were compared against the experiment
with all variables included.
In the base prompt, the model was only informed
that the response was from a German citizen, with
the relevant survey time frame. Detailed prompt
variations can be found in Table 8 in Appendix.
We used Llama2 and wave 12 data to analyze how
adding or removing social group single variables
impacts representativeness and answer diversity.
The use of wave 12 is because it took place before
COVID (see the dates of the waves in §A), and
might have more diverse answer categories (com-
pared to the dominance of health policy responses
illustrated in Figure 1).
Variable inclusion and exclusion have an im-
pact on model performance. Figure 6 shows the
JS distances in ablation experiments. Including all
variables reduces the JS distance by 0.15 compared
to the base prompt. Adding a single variable im-
proves predictions. Removing a variable worsens
performance, though it is still better than using only
one variable, except for the “all except party” case.
no demographics
only age
only vocational edu
only region
only gender
only party
only school edu
all except age
all except vocational edu
all except region
all except gender
all except party
all school edu
all variables
0
0.05
0.1
0.15
0.2
0.25
0.3
0.35
0.4
0.45
JS Distance
Experiment Type
no demographics
one variable
all except one variable
all variables
Figure 6: JS distances for the ablation experiment.
LLM outputs show stronger correlation with
variables when prompted with only one variable.
Table 3 compares Cramér’s V values between the
survey, including only one variable, and all vari-
ables included experiments. When only one vari-
able is provided, the generated texts show stronger
correlations with the input variable. Although JS
distances decrease when more variables are added,
this observation suggests that synthetic data pat-
terns are dynamic and can be influenced by the
number of prompt variables.
Prompt Variable
Survey
LLM-one
LLM-all
Age
0.09
0.09
0.07
Education Degree
0.06
0.25
0.05
Gender
0.08
0.20
0.16
Leaning Party
0.16
0.35
0.17
Region
0.06
0.42
0.15
Vocational Degree
0.08
0.12
0.07
Table 3: Cramér’s V values for the Ablation Experiment
The inclusion of the party variable has the
most significant impact on model performance,
with its presence leading to substantial improve-
ments in information gain. As shown in Figure 6,
adding either only the party or education variable
alone results in the greatest reduction in JS distance
compared to the model without demographics; ex-
cluding only the party variable leads to a smaller
improvement in JS distance, both highlighting the
party variable’s greater impact. Similar to Figure 3,
we plot information gain for party, comparing sur-
vey entropy to Llama2 with all variables, with only
7

--- Page 8 ---

Pop.
Subpop.
1.8
2
2.2
2.4
2.6
2.8
3
Pop.
Subpop.
Pop.
Subpop.
Pop.
Subpop.
1.8
2
2.2
2.4
2.6
2.8
3
Pop.
Subpop.
1.8
2
2.2
2.4
2.6
2.8
3
Pop.
Subpop.
Pop.
Subpop.
Pop.
Subpop.
1.8
2
2.2
2.4
2.6
2.8
3
Source
survey
1VAR_party
Llama2_all
Llama2_base
Die Linke
die AfD
die CDU/CSU
die FDP
die Grünen
die SPD
A minor party
No party
Figure 7: Information Gain for leaning party variable, comparing survey entropy to Llama2-all (with all
variables), 1VAR-party (with only party variable), and Llama2-base (with no variables). Left: population entropy
(H(Y )), right: subpopulation entropy (H(Y | Xi)).
one party variable, and with no variables in Figure
7. As expected, Llama2-base, which includes no
subpopulation variables, produces entropies close
to the population entropy, with random variations
of ±0.03. However, in the 1VAR-party experi-
ment, information gain ranges from 0.2 to 1.3, sig-
nificantly above random variation. This, along with
Cramér’s V values, suggests that the model gen-
erates typical responses, reducing the variation in
subpopulation opinions. Further detailed experi-
mental results are provided in §G of the Appendix.
5
Discussion
We next distill key findings from our experiments,
compare them to prior research, and offer insights
into the role of LLMs in modeling demographic
behaviors and their practical insights in survey-
based applications based on our German case study.
Algorithmic Fidelity in Modeling the German
population. von der Heyde et al. (2025) found that
GPT-3.5 vote predictions for the 2017 German elec-
tion are inaccurate and biased towards the Green
and Left parties. We also found that the model is
better at modeling the opinions of the Green and
the Left parties than the right parties. The subpop-
ulation entropy and in-group diversity can partially
explain this finding. Other factors could be the
models’ training data and the RLHF methods used.
Reduction in in-group diversity. Bisbee et al.
(2024) found that while GPT-3.5 could replicate
survey averages, its synthetic answers lacked vari-
ation compared to real survey data.
Similarly,
von der Heyde et al. (2025) noted GPT-3.5’s dif-
ficulty in capturing nuanced subpopulation behav-
iors. In our analysis, we also observe a reduction
in in-group diversity under certain conditions, par-
ticularly when only one variable is provided to
the model or when using the Mixtral model. This
suggests that the ability to represent within-group
diversity is limited by the model’s input structure
and specific architecture.
The role of LLM prompts. Binz and Schulz
(2023) highlighted how cognitive biases, such as
the framing effect, influenced GPT-3’s outputs. In
our third study, we also noticed that providing only
one variable in a prompt caused Llama2 to focus
disproportionately on that variable, possibly inter-
preting it as more critical than when multiple vari-
ables were included. Interestingly, this effect var-
ied by model: Mixtral over-relied on variables even
with full prompts, while Llama2 showed stronger
biases with fewer variables. This suggests that
model-specific differences influence how demo-
graphic factors are integrated and highlights the
need for careful prompt design. Argyle et al. (2023)
motivated the silicon sampling approach on this
conditional probability formula:
P(V, BLLM) = P(V |BLLM)P(BLLM)
(6)
here B is demographic backstories, and V is voting
patterns. If the model learned the P(V |B), one
could correct for the P(B) and obtain:
P(V, Bsurvey) = P(V |Bsurvey)P(Bsurvey)
(7)
8

--- Page 9 ---

However, in the ablation experiment, we ob-
served that prompting with the social groups is
not straightforward, and it does not align LLMs’ in-
ner parameters to “solely” consider P(Bsocial_group).
LLMs might not always be conditioned to sample
from the joint distribution of backstories. We pro-
pose that demographic variables’ order, number,
and predictive power have a complex interplay and
that this is a further research direction (see, e.g.,
Shu et al., 2024). Also, insights of vignette exper-
iments from survey methodology (Steiner et al.,
2017) could be useful in prompt design.
Wave 12
05-11-2019
Wave 13
21-04-2020
Wave 14
03-11-2020
Wave 15
25-02-2021
Wave 16
06-05-2021
Wave 17
07-07-2021
Wave 18
11-08-2021
Wave 19
15-09-2021
Wave 20
29-09-2021
Wave 21
09-12-2021
0
0.05
0.1
0.15
0.2
0.25
0.3
0.35
0.4
0.45
0.5
17
18
19
20
21
JS
Figure 8: JS distances of answers for the last five waves
(17-21) from GLES, comparing each survey’s answers
to those of the preceding surveys. In most cases, differ-
ences between survey responses increase over time. The
peak of wave 21 compared to wave 20 corresponds to
the drop of the health policy category on 29.09.2021 in
Figure 1, possibly due to some effect of COVID related
topics in that time.
Practical evaluation of LLMs. Figure 8 illus-
trates the JS distances of responses in the last five
survey waves compared to earlier waves. As shown,
responses from older surveys tend to differ more
significantly from those in recent surveys.
Consider a hypothetical scenario where LLMs
are continuously updated with up-to-date training
data while surveys are conducted less frequently
due to cost constraints. In such a scenario, Figure
8 suggests that LLMs may also help researchers
estimate the answers due to the timeliness of their
training data. However, even if the model is as-
sumed to be representative enough, the variety in
subgroup answers should also be considered for
practical uses. In contrast, recent work by Park
et al. (2024) demonstrates how LLMs, when ap-
plied to large-scale human participant interviews,
can simulate subpopulations’ attitudes and behav-
iors, with surveys as a valuable evaluation tool.
This highlights the potential of LLMs not only to
provide estimates but also to more accurately re-
flect diverse human perspectives, emphasizing the
importance of incorporating subgroup variation.
6
Conclusion and Recommendations
This paper evaluates the algorithmic fidelity of
LLMs to represent the opinions of German subpop-
ulations. While von der Heyde et al. (2025) found
that GPT-3.5 struggles with the nuances of German
subpopulations and the country’s multi-party sys-
tem in closed-ended voting questions, we explore
instead free-form open-ended text responses, fo-
cusing on how these responses align with survey
data. By using free-form text responses rather than
multiple-choice questions, we can identify detailed
issues in contextual information and the variety of
different subpopulations, underscoring the value
of this evaluation approach. Our findings show
that LLMs, particularly the Llama2 model, are
capable of associating text responses with social-
demographic variables, indicating a degree of rep-
resentativeness. However, the number of variables
included in the prompt plays a crucial role in model
performance. Despite this, the models still tend to
generate stereotypical representations, with a no-
ticeable favor towards left-leaning parties, consis-
tent with previous findings on the limited diversity
of opinions reflected in LLMs.
Based on these findings, we recommend that
both LLM and social science researchers consider
the following steps for future evaluation of LLM-
generated responses in survey-based research:
Improved representation of opinion diversity:
LLMs should be further developed to reflect the full
spectrum of opinions within subpopulations while
harmful contents are cautiously manipulated. This
includes addressing biases and avoiding the over-
simplification of diverse views into stereotypical
categories with certain safety mechanisms.
Cross-national comparison: Due to the current
discussion of English-centric biases of LLMs, a
more inclusive evaluation with opinion diversity
from non-English data or cross-national sources
such as GlobalOpinionQA (Durmus et al., 2024)
should be conducted and improved.
Timeliness and survey simulation: LLMs can
be valuable in situations where real survey data is
limited or outdated (Namikoshi et al., 2024; Ma
et al., 2024). With continuously updated training
data, LLMs could be further evaluated in the case
of estimating shifts in public opinion.
9

--- Page 10 ---

Limitations
As in our setup, we need to manually annotate the
LLM responses into 16 classes. This limitation con-
strains our ability to conduct a more comprehensive
exploration within this setup, as manual annotation
is both costly and inefficient. Future research could
address this limitation by exploring the potential of
combining human and LLM annotation, as recently
proposed by Choksi et al. (2024).
Another limitation concerns the inherent chal-
lenge of scaling and coding open-ended survey
responses. While we propose reducing the number
of classes to 16 in this paper which has also been
proposed by recent social science research (Mellon
et al., 2024), there might be instances where this
simplification may not fully capture the nuanced
nature of the responses. To address this, future
studies could incorporate qualitative analyses by
subject matter experts as part of the final validation
process.
Additionally, our study focused on three open-
weight LLMs and the German language, which
could limit the scope of our findings and might have
restricted the generalizability of our findings to
other LLMs or languages. Future research should
include a broader variety of models and prompting
languages to explore their performance and gener-
alizability. Moreover, as our approach primarily
relies on zero-shot prompting, a promising next
step would be to evaluate how alternative methods,
such as fine-tuning (e.g., Cao et al., 2025; Holtdirk
et al., 2025), could influence model performance
in the German context.
Ethical Considerations
Throughout the experimentation, we use the pub-
licly available survey dataset from GESIS (2023).
The original data contains social-demographics
of the human participants of the survey, with the
personally identifiable data removed. We solely
present the survey results and the responses gener-
ated by the LLMs, in an objective manner. We do
not intend to express our personal opinions on the
questions.
As LLMs are deployed in systems that interact
with humans, aligning them with humans’ ethi-
cal values gains more importance. Although, as
of today, LLMs can not reliably support opinion
polling surveys, they still carry important informa-
tion about human opinions, values, and attitudes
(Ma et al., 2024). Even if synthetic survey data is
not yet used to support surveys, LLMs as LLMs can
be important tools for consulting political and so-
cial information about countries, populations, sub-
populations, and politics in general (Hämäläinen
et al., 2023).
When interpreting the opinions reflected in LLM
outputs, we advise caution against anthropomor-
phism. Following recent discussions (Santurkar
et al., 2023; Röttger et al., 2024; Durmus et al.,
2024; Ma et al., 2024), we use the phrase “opinions
reflected in the LLM outputs” rather than suggest-
ing that LLMs “have” opinions, to avoid anthropo-
morphizing these models.
Acknowledgments
We thank the members of SODA Lab and MaiNLP
labs from LMU Munich, and the members of the
Social Data Science Group from University of
Mannheim for their constructive feedback. Xin-
peng Wang and Barbara Plank are supported by
ERC Consolidator Grant DIALECT (101043235).
Markus Herklotz and Matthias Assenmacher are
supported by the Deutsche Forschungsgemein-
schaft (DFG, German Research Foundation) under
the National Research Data Infrastructure – NFDI
27/1 - 460037581.
References
Utkarsh Agarwal, Kumar Tanmay, Aditi Khandelwal,
and Monojit Choudhury. 2024. Ethical reasoning
and moral value alignment of LLMs depend on the
language we prompt them in. In Proceedings of the
2024 Joint International Conference on Computa-
tional Linguistics, Language Resources and Eval-
uation (LREC-COLING 2024), pages 6330–6340,
Torino, Italia. ELRA and ICCL.
Hans-Jürgen Andreß, Katrin Golsch, and Alexander W.
Schmidt. 2013. Applied Panel Data Analysis for
Economic and Social Surveys. Springer.
Lisa P. Argyle, Ethan C. Busby, Nancy Fulda, Joshua R.
Gubler, Christopher Rytting, and David Wingate.
2023.
Out of one, many: Using language mod-
els to simulate human samples. Political Analysis,
31(3):337–351.
Arnav Arora, Lucie-aimée Kaffee, and Isabelle Augen-
stein. 2023. Probing pre-trained language models for
cross-cultural differences in values. In Proceedings
of the First Workshop on Cross-Cultural Considera-
tions in NLP (C3NLP), pages 114–130, Dubrovnik,
Croatia. Association for Computational Linguistics.
Marcel Binz and Eric Schulz. 2023. Using cognitive
psychology to understand gpt-3. Proceedings of the
National Academy of Sciences, 120(6):e2218523120.
10

--- Page 11 ---

James Bisbee, Joshua D. Clinton, Cassy Dorff, Brenton
Kenkel, and Jennifer M. Larson. 2024. Synthetic re-
placements for human survey data? the perils of large
language models. Political Analysis, 32(4):401–416.
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, Sandhini Agarwal, Ariel Herbert-Voss,
Gretchen Krueger, Tom Henighan, Rewon Child,
Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu,
Clemens Winter, Christopher Hesse, Mark Chen,
Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin
Chess, Jack Clark, Christopher Berner, Sam Mc-
Candlish, Alec Radford, Ilya Sutskever, and Dario
Amodei. 2020. Language models are few-shot learn-
ers. Preprint, arXiv:2005.14165.
Yong Cao, Haijiang Liu, Arnav Arora, Isabelle Augen-
stein, Paul Röttger, and Daniel Hershcovich. 2025.
Specializing large language models to simulate sur-
vey response distributions for global populations. In
Proceedings of the 2025 Conference of the Nations
of the Americas Chapter of the Association for Com-
putational Linguistics: Human Language Technolo-
gies (Volume 1: Long Papers), pages 3141–3154,
Albuquerque, New Mexico. Association for Compu-
tational Linguistics.
Yong Cao, Li Zhou, Seolhwa Lee, Laura Cabello, Min
Chen, and Daniel Hershcovich. 2023.
Assessing
cross-cultural alignment between ChatGPT and hu-
man societies: An empirical study. In Proceedings of
the First Workshop on Cross-Cultural Considerations
in NLP (C3NLP), pages 53–67, Dubrovnik, Croatia.
Association for Computational Linguistics.
Madiha Zahrah Choksi, Marianne Aubin Le Quéré,
Travis Lloyd, Ruojia Tao, James Grimmelmann, and
Mor Naaman. 2024. Under the (neighbor)hood: Hy-
perlocal surveillance on nextdoor. In Proceedings of
the CHI Conference on Human Factors in Computing
Systems, CHI ’24, New York, NY, USA. Association
for Computing Machinery.
Jacob Cohen. 1960. A coefficient of agreement for
nominal scales. Educational and Psychological Mea-
surement, 20(1):37–46.
Harald Cramér. 1999. Mathematical Methods of Statis-
tics (PMS-9). Princeton University Press.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. BERT: Pre-training of
deep bidirectional transformers for language under-
standing. In Proceedings of the 2019 Conference of
the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies, Volume 1 (Long and Short Papers), pages
4171–4186, Minneapolis, Minnesota. Association for
Computational Linguistics.
Ricardo Dominguez-Olmedo, Moritz Hardt, and Celes-
tine Mendler-Dünner. 2024. Questioning the survey
responses of large language models. In Advances in
Neural Information Processing Systems, volume 37,
pages 45850–45878. Curran Associates, Inc.
Esin Durmus, Karina Nguyen, Thomas Liao, Nicholas
Schiefer, Amanda Askell, Anton Bakhtin, Carol
Chen,
Zac Hatfield-Dodds,
Danny Hernandez,
Nicholas Joseph, Liane Lovitt, Sam McCandlish,
Orowa Sikder, Alex Tamkin, Janel Thamkul, Jared
Kaplan, Jack Clark, and Deep Ganguli. 2024. To-
wards measuring the representation of subjective
global opinions in language models. In First Confer-
ence on Language Modeling.
Peter Eigenschink, Thomas Reutterer, Stefan Vamosi,
Ralf Vamosi, Chang Sun, and Klaudius Kalcher.
2023. Deep Generative Models for Synthetic Data:
A Survey. IEEE Access, 11:47304–47320.
GESIS. 2023.
Gles panel 2016-2021, wellen 1-
21. GESIS, Köln. ZA6838 Datenfile Version 6.0.0,
https://doi.org/10.4232/1.14114.
GESIS. 2024.
Gles codierung des wichtigsten
politischen
problems
(2018-2022).
GESIS,
Köln.
ZA7957
Datenfile
Version
2.0.0,
https://doi.org/10.4232/1.14241.
Perttu Hämäläinen, Mikke Tavast, and Anton Kunnari.
2023. Evaluating large language models in gener-
ating synthetic hci research data: a case study. In
Proceedings of the 2023 CHI Conference on Human
Factors in Computing Systems, CHI ’23, New York,
NY, USA. Association for Computing Machinery.
Thomas M. Holbrook. 2022. An Introduction to Polit-
ical and Social Data Analysis Using R. Thomas M.
Holbrook.
Tobias Holtdirk, Dennis Assenmacher, Arnim Bleier,
and Claudia Wagner. 2025. Addressing Systematic
Non-response Bias with Supervised Fine-Tuning of
Large Language Models: A Case Study on German
Voting Behaviour.
EunJeong Hwang, Bodhisattwa Majumder, and Niket
Tandon. 2023. Aligning language models to user
opinions. In Findings of the Association for Com-
putational Linguistics: EMNLP 2023, pages 5906–
5919, Singapore. Association for Computational Lin-
guistics.
Albert Q. Jiang, Alexandre Sablayrolles, Antoine
Roux, Arthur Mensch, Blanche Savary, Chris
Bamford, Devendra Singh Chaplot, Diego de las
Casas, Emma Bou Hanna, Florian Bressand, Gi-
anna Lengyel, Guillaume Bour, Guillaume Lam-
ple, Lélio Renard Lavaud, Lucile Saulnier, Marie-
Anne Lachaux, Pierre Stock, Sandeep Subramanian,
Sophia Yang, Szymon Antoniak, Teven Le Scao,
Théophile Gervet, Thibaut Lavril, Thomas Wang,
Timothée Lacroix, and William El Sayed. 2024a.
Mixtral of experts. Preprint, arXiv:2401.04088.
Hang Jiang, Xiajie Zhang, Xubo Cao, Cynthia Breazeal,
Deb Roy, and Jad Kabbara. 2024b. PersonaLLM:
Investigating the ability of large language models to
11

--- Page 12 ---

express personality traits. In Findings of the Associ-
ation for Computational Linguistics: NAACL 2024,
pages 3605–3627, Mexico City, Mexico. Association
for Computational Linguistics.
Dan Jurafsky and James H. Martin. 2024.
Speech
and language processing: an introduction to natu-
ral language processing, computational linguistics,
and speech recognition.
S. Kullback and R. A. Leibler. 1951. On Information
and Sufficiency. The Annals of Mathematical Statis-
tics, 22(1):79 – 86.
Jianhua Lin. 2006.
Divergence measures based on
the shannon entropy.
IEEE Trans. Inf. Theor.,
37(1):145–151.
Lin Long, Rui Wang, Ruixuan Xiao, Junbo Zhao, Xiao
Ding, Gang Chen, and Haobo Wang. 2024.
On
LLMs-driven synthetic data generation, curation, and
evaluation: A survey. In Findings of the Associa-
tion for Computational Linguistics ACL 2024, pages
11065–11082, Bangkok, Thailand and virtual meet-
ing. Association for Computational Linguistics.
Bolei Ma, Xinpeng Wang, Tiancheng Hu, Anna-
Carolina Haensch, Michael A. Hedderich, Barbara
Plank, and Frauke Kreuter. 2024. The potential and
challenges of evaluating attitudes, opinions, and val-
ues in large language models. In Findings of the
Association for Computational Linguistics: EMNLP
2024, pages 8783–8805, Miami, Florida, USA. Asso-
ciation for Computational Linguistics.
Jonathan Mellon, Jack Bailey, Ralph Scott, James
Breckwoldt, Marta Miori, and Phillip Schmedeman.
2024. Do ais know what the most important issue
is? using language models to code open-text so-
cial survey responses at scale. Research & Politics,
11(1):20531680241231468.
Keiichi Namikoshi, Alex Filipowicz, David A. Shamma,
Rumen Iliev, Candice L. Hogan, and Nikos Arechiga.
2024.
Using llms to model the beliefs and
preferences of targeted populations.
Preprint,
arXiv:2403.20252.
Joon Sung Park, Carolyn Q. Zou, Aaron Shaw, Ben-
jamin Mako Hill, Carrie Cai, Meredith Ringel Morris,
Robb Willer, Percy Liang, and Michael S. Bernstein.
2024. Generative agent simulations of 1,000 people.
Preprint, arXiv:2411.10109.
Philip Resnik, Bolei Ma, Alexander Hoyle, Pranav Goel,
Rupak Sarkar, Maeve Gearing, Anna-Carolina Haen-
sch, and Frauke Kreuter. 2024. Topic-oriented proto-
col for content analysis of text – a preliminary study.
Unpublished manuscript.
Paul Röttger, Valentin Hofmann, Valentina Pyatkin,
Musashi Hinck, Hannah Kirk, Hinrich Schuetze, and
Dirk Hovy. 2024. Political compass or spinning ar-
row? towards more meaningful evaluations for values
and opinions in large language models. In Proceed-
ings of the 62nd Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Pa-
pers), pages 15295–15311, Bangkok, Thailand. As-
sociation for Computational Linguistics.
Guilherme Sanches de Oliveira and Edward Baggs.
2023. Psychology’s WEIRD Problems. Elements
in Psychology and Culture. Cambridge University
Press.
Shibani Santurkar, Esin Durmus, Faisal Ladhak, Cinoo
Lee, Percy Liang, and Tatsunori Hashimoto. 2023.
Whose opinions do language models reflect?
In
Proceedings of the 40th International Conference on
Machine Learning, ICML’23. JMLR.org.
Bangzhao Shu, Lechen Zhang, Minje Choi, Lavinia
Dunagan, Lajanugen Logeswaran, Moontae Lee, Dal-
las Card, and David Jurgens. 2024. You don’t need
a personality test to know these models are unre-
liable: Assessing the reliability of large language
models on psychometric instruments. In Proceed-
ings of the 2024 Conference of the North American
Chapter of the Association for Computational Lin-
guistics: Human Language Technologies (Volume
1: Long Papers), pages 5263–5281, Mexico City,
Mexico. Association for Computational Linguistics.
Peter M. Steiner, Christiane Atzmüller, and Dan Su.
2017. Designing valid and reliable vignette experi-
ments for survey research: A case study on the fair
gender income gap. Journal of Methods and Mea-
surement in the Social Sciences, 7:52–94.
Seungjong Sun, Eungu Lee, Dongyan Nan, Xiangy-
ing Zhao, Wonbyung Lee, Bernard J. Jansen, and
Jang Hyun Kim. 2024. Random silicon sampling:
Simulating human sub-population opinion using a
large language model based on group-level demo-
graphic information. Preprint, arXiv:2402.18144.
Gemma Team. 2024. Gemma: Open models based
on gemini research and technology.
Preprint,
arXiv:2403.08295.
Lindia Tjuatja, Valerie Chen, Tongshuang Wu, Ameet
Talwalkwar, and Graham Neubig. 2024. Do LLMs
exhibit human-like response biases? a case study in
survey design. Transactions of the Association for
Computational Linguistics, 12:1011–1026.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timothée Lacroix,
Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal
Azhar, Aurelien Rodriguez, Armand Joulin, Edouard
Grave, and Guillaume Lample. 2023. Llama: Open
and efficient foundation language models. Preprint,
arXiv:2302.13971.
Veniamin Veselovsky, Manoel Horta Ribeiro, Akhil
Arora, Martin Josifoski, Ashton Anderson, and
Robert West. 2023. Generating faithful synthetic data
with large language models: A case study in compu-
tational social science. Preprint, arXiv:2305.15041.
12

--- Page 13 ---

Leah von der Heyde, Anna-Carolina Haensch, and
Alexander Wenz. 2025. Vox populi, vox ai? us-
ing large language models to estimate german
vote choice.
Social Science Computer Review,
0(0):08944393251337014.
Xinpeng Wang, Chengzhi Hu, Bolei Ma, Paul Rottger,
and Barbara Plank. 2024a.
Look at the text:
Instruction-tuned language models are more robust
multiple choice selectors than you think. In First
Conference on Language Modeling.
Xinpeng Wang, Bolei Ma, Chengzhi Hu, Leon Weber-
Genzel, Paul Röttger, Frauke Kreuter, Dirk Hovy, and
Barbara Plank. 2024b. “my answer is C”: First-token
probabilities do not match text answers in instruction-
tuned language models. In Findings of the Associa-
tion for Computational Linguistics ACL 2024, pages
7407–7416, Bangkok, Thailand and virtual meeting.
Association for Computational Linguistics.
Xuena Wang, Xueting Li, Zi Yin, Yue Wu, and Jia
Liu. 2023. Emotional intelligence of large language
models. Journal of Pacific Rim Psychology, 17:1–12.
A
Data and Prompt Template
Table 4 shows the dates for the waves involved
in the original GLES survey (GESIS, 2023). The
six main social demographic variables and their
subgroups in the original survey are presented in
Table 5.
Wave
Start Date
End Date
10
06-11-2018
21-11-2018
11
28-05-2019
12-06-2019
12
05-11-2019
19-11-2019
13
21-04-2020
05-05-2020
14
03-11-2020
17-11-2020
15
25-02-2021
12-03-2021
16
06-05-2021
19-07-2021
17
07-07-2021
20-07-2021
18
11-08-2021
24-08-2021
19
15-09-2021
25-09-2021
20
29-09-2021
12-10-2021
21
09-12-2021
21-12-2021
Table 4: Data collection dates of GLES waves
In Figure 9, we show the original prompt in Ger-
man we used for the LLM response generation. We
use the template in German and expect the LLMs
to respond in German, in order to mirror the real
survey case. The placeholders in the prompt are re-
placed with the respondents’ information and then
fed to the LLMs that were experimented with. The
prompt templates used in the ablation study in §4.3
are presented in Table 8.
Social Groups
Sub-Groups
Age
18-29
30-44
45-59
60+
Gender
Male
Female
Leaning Party
AfD
CDU/CSU
FDP
Grünen
A minor party
Linke
SPD
No party
Region
East Germany
West Germany
Education Degree
High school diploma
Higher education entrance qualification
Secondary school diploma
Intermediate school diploma
Is still student
No school diploma
Vocational Degree
Completed vocational internship/volunteer work
Vocational school diploma
University of applied sciences degree
Specialist school diploma
Completed apprenticeship
Master craftsman or technician qualification
University degree
In vocational training
Commercial or agricultural apprenticeship
Commercial apprenticeship
No vocational training completed
Table 5: Social-Demographic Groups and Sub-Groups.
Identifizieren Sie das wichtigste Problem, mit dem
Deutschland im {month} {year} konfrontiert ist. Geben
Sie die Antwort in einem prägnanten Satz an, konzentri-
eren Sie sich nur auf ein einziges Thema ohne weitere Aus-
führungen oder Auflistung zusätzlicher Probleme. Wieder-
holen Sie nicht die Informationen die Ihnen gegeben wur-
den, und geben Sie Ihre Antwort direkt und ohne ein-
leitende Phrasen. Antworten Sie auf Deutsch und auss-
chließlich auf Deutsch, verwenden Sie keine Englische
Sprache. Antworten Sie aus der Sicht eines Befragten mit
deutscher Staatsbürgerschaft und den im nachfolgenden
spezifizierten Eigenschaften.
{artikel}
Befragte
ist
{age}
Jahre
alt
und
{gen-
der}. {pronoun} {schulabschluss_clause } und {berufab-
schluss_clause} {pronoun2} lebt in {region} und unter-
stützt hauptsächlich {party}.
Figure 9: Original prompt template in German.
13

--- Page 14 ---

B
Classes of the Coding Scheme
In Table 9, we show the original classes of the
coding scheme based on GESIS (2024) as well as
the merged and reduced 16 classes.
C
Annotation Scheme
The annotators followed the coding guidelines pro-
vided by (GESIS, 2024) for consistency. We used
the coarse classes for annotation to achieve better
agreement among annotators. One of the leading
authors and another project collaborator were asked
to conduct the same annotations of the 1,500 sam-
ples as volunteers. There exists disagreement on
minor cases that were resolved after discussion.
Both annotators are consent about the annotated
data use. Figure 10 and 11 show the annotation
screen and the annotation instruction given to the
annotators respectively.
 1
 2
 3
 4
 5
!python /content/drive/MyDrive/labeling/annotation.py \
--data_path /content/drive/MyDrive/labeling/base/chunk_0.json\
--TABLE_MAX_WIDTH 50 \
--TEXT_MAX_WIDTH 100
more_horiz
+-----------+----------------------------------------------------+---------------------------------------------------+
|   classid | ClassName                                          | subclasses                                        |
+===========+====================================================+===================================================+
|         0 | Politisches System und Prozesse (Political System  | Election Campaign and Government Formation,       |
|           | and Processes)                                     | Political Structures and Processes, Democracy,    |
|           |                                                    | Bureaucracy, Lobbyism, Corruption, Values,        |
|           |                                                    | political culture                                 |
+-----------+----------------------------------------------------+---------------------------------------------------+
|         1 | Sozialpolitik (Social Policy)                      | Social Policy, Social Justice, Poverty,           |
|           |                                                    | Unemployment and Basic(Social) Security, Pensions |
|           |                                                    | and Demographic Change                            |
+-----------+----------------------------------------------------+---------------------------------------------------+
|         2 | Gesundheitspolitik (Health Policy)                 | Health Policy, Nursing, Corona Pandemic           |
+-----------+----------------------------------------------------+---------------------------------------------------+
|         3 | Familien- und Gleichstellungspolitik (Family and   | Family Policy, Gender Equality                    |
|           | Gender Equality Policy)                            |                                                   |
+-----------+----------------------------------------------------+---------------------------------------------------+
|         4 | Bildungspolitik (Education Policy)                 | Education Policy, School Policy                   |
+-----------+----------------------------------------------------+---------------------------------------------------+
|         5 | Umweltpolitik (Environmental Policy)               | Energy Policy, Environmental Policy, Climate      |
|           |                                                    | Policy, Natural Disasters                         |
+-----------+----------------------------------------------------+---------------------------------------------------+
|         6 | Wirtschaftspolitik (Economic Policy)               | Economic Policy, Price Level, Infrastructure,     |
|           |                                                    | Digital Infrastructure, Transport Policy, Housing |
|           |                                                    | Policy                                            |
+-----------+----------------------------------------------------+---------------------------------------------------+
|         7 | Sicherheits (Security)                             | Terrorism, Internal Security, Crime and Violence, |
|           |                                                    | Radicalization and Extremism, Law and Justice,    |
|           |                                                    | Defense                                           |
+-----------+----------------------------------------------------+---------------------------------------------------+
|         8 | Außenpolitik (Foreign Policy)                      | Foreign Policy, Europe and European Union,        |
|           |                                                    | (Germany's Relations with) Russia, (Germany's     |
|           |                                                    | Relations with) Turkey, International Conflicts   |
|           |                                                    | and Peace, War in Ukraine                         |
+-----------+----------------------------------------------------+---------------------------------------------------+
|         9 | Medien und Kommunikation (Media and Communication) | Media                                             |
+-----------+----------------------------------------------------+---------------------------------------------------+
|        10 | Sonstiges (Others)                                 | Others                                            |
+-----------+----------------------------------------------------+---------------------------------------------------+
|        11 | Migration and Integration                          | Migration and Integration                         |
+-----------+----------------------------------------------------+---------------------------------------------------+
|        12 | Ostdeutschland                                     | Ostdeutschland                                    |
+-----------+----------------------------------------------------+---------------------------------------------------+
|        13 | keine Angabe (not specified)                       | keine Angabe                                      |
+-----------+----------------------------------------------------+---------------------------------------------------+
|        14 | weiß nicht                                         |                                                   |
+-----------+----------------------------------------------------+---------------------------------------------------+
|        15 | LLM refusal                                        | As an AI model, ..., It is not possible to answer |
+-----------+----------------------------------------------------+---------------------------------------------------+
|        16 | Values, political culture and general social       | Nationalism, Rise of left, Social cohesion,social |
|           | criticism                                          | division                                          |
+-----------+----------------------------------------------------+---------------------------------------------------+
number:14
output: Das wichtigste Problem, mit dem Deutschland im November 2019 konfrontiert ist, ist die unzureichende
Ausstattung der öffentlichen Pflanzen mit ausreichend Wasser.
translation: The most important problem facing Germany in November 2019 is the inadequate supply of public plants
with sufficient water.
label: 
Figure 10: Annotation Screen.
D
Technical Setup
We used Python 3.12.1 and the transformers 3
library (version 4.42.4) by HuggingFace (with Py-
torch Framework as the backend) to create two
custom classes: the BertClassifier (for the mul-
tilabel classification task) and TextGenerator (for
generating synthetic answers ).
3https://huggingface.co/docs/transformers/
Samples can be labeled with multiple classes, (up to 3) if needed.
example annotations:
1,10
14
12,2,1
If you really can't decide on a sample, you can label it with -1, and continue labeling, we can decide on these cases later on.
The following guide is from the original study and it can help you while giving your decision:
1. When coding the answers,no contextual knowledge should be used if possible. In addition, no interpretation should be
necessary to assign an answer to a category.
2. If several topics are mentioned (although the question explicitly asks for one topic), several codes are assigned in the order
in which they are mentioned. A maximum of 3 codes (in order of mention) are assigned.
3. if general topics are supported with additional examples (enumerations, reasons), only the general topic, and not the
example, is coded. Examples:
'Citizens are becoming more and more criminal because of the euro crisis, the refugees, the new president of the USA and
Brexit, but our politicians only listen to the citizens with half an ear!' -[17 crime and violence, criticism of politicians], not
Euro crisis or Refugees.
'Health policy and care'
[codes: 37 health policy, 38 care]
'Healthcare (e.g. care)' [code: 37 health policy]
The original coding scheme, detailed examples and explanations can be found here if needed:
Labeling Rules
keyboard_arrow_down
Figure 11: The instructions at the annotating tool.
Text Generation.
To fit models into a single
GPU, we have used the 8-bit quantized version
of the models. The inference configurations can
be found in the study repository. We did the infer-
ence with batch_size of 16 to benefit the parallel
computing power and reduce runtime. On aver-
age, TextGenerator generated 1.16 answers per
second. We performed 25 generation experiments,
using ca. 75 GPU hours for the generation task.
Text Classification.
As the contexts are all in
German, we used the German version of the
BERT model4.
The BertClassifier training
takes around 20 minutes for the setup 5. We trained
the with a batch_size of 32, a learning_rate of 2e-
5, and a fixed_precision at 16 bits to fasten the
convergence. The early stop condition stopped the
training after 3rd epoch when no further loss reduc-
tion was observed. Table 6 shows the other relevant
model parameters and hyperparameters.
Parameter
Value
epochs
15
learning_rate
2e-5
batch_size
32
weight_decay
0.01
fp16
True
max_length
512
Table 6: Hyperparameters for the BERT model
E
Qualitative Analysis
Table 10 shows a few sample responses from LLM
experiments. Before discussing models’ represen-
tativeness, we point to three qualitative issues ob-
served in the text generations:
4https://huggingface.co/google-bert/
bert-base-german-cased
14

--- Page 15 ---

Introductory Phrases.
We noted that all mod-
els use some “introductory phrases" even though
models were prompted not to use any. The Gemma
model starts the sentence 96 % of the time by list-
ing the social group variables given to it. Llama2
model uses the “The most important problem fac-
ing Germany" phrase in 96 % of its generations.
The Mixtral model uses the “One of the most im-
portant issues” phrase in 75 % of the answers. Even
if the text lengths had been comparable, these style
characteristics would allow humans to discriminate
synthetic responses from actual ones. At this point,
we did not put further effort into trying different
prompts and making the synthetic responses stylis-
tically similar to survey responses.
Mention of Future Events.
Despite specifying
the survey month and year (November 2019), re-
sponses occasionally referenced events that oc-
curred after the survey date, such as the COVID-19
pandemic (2020) and the Energy Crisis in Germany
(2021). For example, the Gemma model contained
COVID-19-related words (COVID, corona, coro-
navirus, COVID-19, sars-cov, etc.) in 42 % of its
responses. This problem was observed relatively
less in Llama2 and Mixtral models (3 % and 0.2 %
of answers, respectively).
Mixed-Language Answers.
Although models
were instructed to respond in German, a small per-
centage (up to 3%) of answers had some parts in
German, whereas some terms or clauses were in
English.
F
Additional Metrics
In this section, we present metrics in addition to
those in §3.4. These include the base metrics for
the main experimentation, as well as additional
metrics used for the additional results in §G.
Proportion Agreement.
It is the proportion of
two variables exactly matching. Like accuracy, this
measure does not consider the probability of match-
ing by chance and should be used as a descriptive
quantity (Argyle et al., 2023).
Cohen’s Kappa (κ).
It is a measure of agree-
ment between two categorical variables and is often
used as a measure of inter-rater agreement (Cohen,
1960). Unlike proportional agreement, it corrects
for the agreement by chance, and It is defined as
κ = p0−pe
1−pe where
• po is the observed agreement ratio
• pe is the expected agreement when annotators
assign labels randomly.
Kullback-Leibler Divergence.
It also known as
relative entropy, is a method used in measuring
the statistical distance between two probability dis-
tributions (Kullback and Leibler, 1951). For dis-
tributions P and Q of a discrete random variable
X = [X1, ..., Xn], the Kullback-Leibler (KL) di-
vergence can be defined as:
DKL(P ∥Q) =
X
x∈X
P(x) log
P(x)
Q(x)

(8)
KL Divergence is not a distance measure since it
does not satisfy the symmetry requirement of a
metric. i.e KL(P,Q) != KL(Q,P) , unless P and Q
are equal. If not, KL divergence is always greater
than 0 and not bounded.
Absolute Percentage Error (APE).
JS distance
enables us to compare model performance at the
question level. We employ the APE to evaluate the
accuracy of predictions in each category. APE is
calculated by determining the absolute differences
between predicted and actual frequencies and then
normalizing these differences by the reference sur-
vey frequencies. For each label, we compute:
APEL =

yt −ˆyt
yt

(9)
where yt is survey frequency and ˆyt LLM output
frequency for the label l.
G
Additional Results
In this section, we show additional results and fig-
ures for the main experimentation in §4.
Label Distribution on LLM Outputs.
Figure
12 shows the label distribution on the three LLM
outputs based on the coarse labels.
Detailed JS Distances of Subpopulation in Ex-
periment 1: Llama2 achieves better perfor-
mance in most categories.
We show the detailed
JS Distances in each social group category in Ex-
periment 1 in Table 14 for all three experimented
LLMs. Among the three LLMs, we notice Llama2
has the least JS Distances across the most subcate-
gories compared to the other two LLMs, showing
more alignment with the real survey data.
15

--- Page 16 ---

Additional JS Distances of Subpopulation Vari-
ables in Experiment 2: Further indication of
WEIRD bias of LLMs.
We show additional re-
sults of the survey’s subpopulation entropy and the
JS Distance between the Llama output and survey
results across 10 waves in experiment 2 in Figure
15, i.e., results for four other variables in addition
to the variable leaning_party in Figure 5 from
§4.2. For the vocational degree variable, groups
with a completed vocational internship are the least
well-represented on average. For the education
degree variable, groups with no degree or only
a secondary school diploma are less represented
compared to those with higher educational qual-
ifications. Among age groups, older cohorts are
less well-represented than younger ones. For the
regional variable, which includes only two groups,
there is a greater discrepancy in representing East
Germany compared to West Germany. Overall,
these findings align with prior evidence that LLMs
exhibit biases favoring Western, younger, and more
educated subpopulations, commonly referred to as
WEIRD bias5, as highlighted in studies such as
Santurkar et al. (2023), Cao et al. (2023), Arora
et al. (2023), and Agarwal et al. (2024).
Label-Level Percentage Errors in Experiment
3.
Table 7 shows label-level percentage errors.
We compared the best-performing models in the
1-var-* and w/o.-* experiments. In 7 out of 14
labels, using all variables produced the lowest per-
centage errors. Both JS distances and percentage
errors decreased with the inclusion of more vari-
ables, reinforcing the representational accuracy of
the Llama2 model for the German population.
Proportional Agreement (PA) and κ Scores
across Waves: LLMs face in achieving consis-
tent agreement with survey data over time, par-
ticularly in representing complex social phenom-
ena.
The scores in Table 11 compare Llama2-
generated responses with resampled survey data
across different waves. The PA for Llama2 fluctu-
ates significantly, reaching as high as 0.56 in wave
13 but dropping in later waves, especially after
wave 17, indicating inconsistencies in the model’s
ability to align with the original survey data. By
contrast, the survey resample maintains relatively
5The term "WEIRD bias" originates in psychology, where
values from Western, Educated, Industrialized, Rich, and
Democratic (W.E.I.R.D.) societies are assumed to represent
universal “human” values (Sanches de Oliveira and Baggs,
2023).
Labels
LLM-base min(1var. *) min(w/o. *) LLM-all
Political System, Processes
7.92
-3.62
0.92
9.71
Social Policy
-23.76
-21.94
-15.16
-7.45
Health Policy
22.02
3.32
2.84
2.08
Family and Gender Equality
-0.27
-0.25
-0.14
-0.10
Education Policy
-2.20
-2.15
-1.88
-1.83
Environmental Policy
4.43
0.42
0.15
2.52
Economic Policy
8.15
7.92
11.49
9.21
Security
-6.26
-7.37
-7.06
-6.88
Foreign Policy
6.58
1.93
1.59
0.54
Media and Communication
0.09
-0.01
0.00
0.03
Others
-3.11
-3.12
-3.12
-3.00
Migration and Integration
-17.16
-21.40
-19.80
-14.61
East Germany
0.01
-0.18
-0.17
0.14
Values, Polit. Culture, Social
3.56
1.31
9.90
9.65
Table 7: Percentage errors in the ablation experiment.
LLM-base denotes no demographics; min(1var. *) de-
notes best-performing experiment with one variable;
min(w/o. *) denotes best-performing experiment with
all except one variable; LLM-all denotes all variables.
stable PA scores, ranging between 0.34 and 0.55,
indicating better agreement with the original survey.
The κ scores, however, are low for both Llama2
and the survey resample, with Llama2 performing
particularly poorly (0.01–0.04). This suggests that
while the model can capture some high-level agree-
ment (as seen in PA scores), it struggles to replicate
the nuanced variability and structure of human re-
sponses across waves, especially as the diversity
of responses increases. These findings underscore
the challenges LLMs face in representing complex
social phenomena in survey data, especially over
time.
Label-level Breakdown with APE: LLM pre-
dictions show over- and underrepresentation of
certain political topics compared to survey data.
Table 12 and 13 show the comparison of predicted
label percentages between survey and LLM an-
swers in experiment 1 and 2 respectively. In Table
12, we observe that “Security”, “Migration and
Integration” and “Social Policy” topics are less rep-
resented than the survey in all LLM-texts and “Val-
ues, political culture and general social criticism”
represented much more, with a mean APE=218.1.
the Mixtral model emphasized “Environment Pol-
itics”, whereas Llama2 focused on “Political Sys-
tems and Processes” more than others. Table 13
shows “Health Policy”, “Values, political culture
and general social criticism" and “Economic Pol-
icy” are consistently more represented as the text
16

--- Page 17 ---

answer categories, whereas “Migration and Inte-
gration" and “Security” are less represented. We
also calculated the mean APE per label to compare
errors on average on which categories the Llama2
represented the political topics more accurately.
Factual Knowledge of Llama2 without Demo-
graphic Prompts.
We also check actual knowl-
edge of Llama2 model without giving any survey
contexts in Table 15. It shows Llama2’s general
accuracy in providing vote percentages for major
elections, though minor errors and formatting is-
sues occur, especially in the 2020 U.S. election.
For Germany’s most important problem in 2019,
Llama2 identifies key issues like climate change
and economic security but gives rough percentage
estimates rather than precise data. These results
suggest that while the model captures broad trends,
it struggles with exact figures when not given spe-
cific demographic or contextual prompts.
17

--- Page 18 ---

Experiment Name
Prompt Information
1_var_region
Der/Die Befragte lebt in {eastwest}. [/INST]
1_var_party
Der/Die Befragte unterstützt hauptsächlich {party}. [/INST]
1_var_education_degree
Der/Die Befragte {schulabschluss_clause} [/INST]
1_var_age
Der/Die Befragte ist {age} Jahre alt. [/INST]
1_var_gender
{artikel} Befragte ist {gender} [/INST]
1_var_vocational_degree
Der/Die Befragte {berufabschluss_clause} [/INST]
without_age
{artikel} Befragte ist {gender}. {pronoun} {schulabschluss_clause} und
{berufabschluss_clause} {pronoun2} lebt in {eastwest} und unterstützt hauptsächlich
{party}. [/INST]
without_region
{artikel} Befragte ist {age} Jahre alt und {gender}. {pronoun} {schulabschluss_clause}
und {berufabschluss_clause} {pronoun2} unterstützt hauptsächlich {party}. [/INST]
without_vocational_degree
{artikel} Befragte ist {age} Jahre alt und {gender}. {pronoun} {schulabschluss_clause}
{pronoun2} lebt in {eastwest} und unterstützt hauptsächlich {party}. [/INST]
without_education_degree
{artikel} Befragte ist {age} Jahre alt und {gender}. {pronoun} und
{berufabschluss_clause} {pronoun2} lebt in {eastwest} und unterstützt hauptsächlich
{party}. [/INST]
without_party
{artikel} Befragte ist {age} Jahre alt und {gender}. {pronoun} {schulabschluss_clause}
und {berufabschluss_clause} {pronoun2} lebt in {eastwest}. [/INST]
without_gender
Der/Die Befragte ist {age} Jahre alt. Er/Sie {schulabschluss_clause} und
{berufabschluss_clause} Er/Sie lebt in {eastwest} und unterstützt hauptsächlich {party}.
[/INST]
Table 8: Ablation experiments and the modified prompt contents. 1_var_* denotes the experimentation of prompting
with only one variation*. without_* denotes the experimentation of prompting with all variables except *.
Fine Labels
Coarse Labels
Election Campaign and Government Formation, Political Struc-
tures and Processes, Democracy, Bureaucracy, Lobbyism, Cor-
ruption
Political System and Processes
Values, political culture and general social criticism
Values, political culture and general social criticism
Social Policy, Social Justice, Poverty, Unemployment and Basic
Security, Pensions and Demographic Change
Social Policy
Health Policy, Nursing, Corona Pandemic
Health Policy
Family Policy, Gender Equality
Family and Gender Equality Policy
Education Policy, School Policy
Education Policy
Energy Policy, Environmental Policy, Climate Policy, Natural
Disasters
Environmental Policy
Economic Policy, Price Level, Infrastructure, Digital Infrastruc-
ture, Transport Policy, Housing Policy
Economic Policy
Terrorism, Internal Security, Crime and Violence, Radicalization
and Extremism, Law and Justice, Defense
Security
Foreign Policy, Europe and European Union, (Germany’s Rela-
tions with) Russia, (Germany’s Relations with) Turkey, Interna-
tional Conflicts and Peace, War in Ukraine
Foreign Policy
Media
Media and Communication
Others
Others
Migration and Integration
Migration and Integration
East Germany
East Germany
Not specified
Not specified
Don’t know
Don’t know
Table 9: Description of the Classes, originally in German, translated to English
18

--- Page 19 ---

Model
Original Answer
Translation
Gemma
Als 61-jährige Frau mit deutscher Staatsbürgerschaft, die
in Westdeutschland lebt und hauptsächlich keine Partei
unterstützt, ist das wichtigste Problem, mit dem
Deutschland im November 2019 konfrontiert ist, die
weiterhin bestehende Situation der COVID-19-Pandemie.
As a 61-year-old woman with German
citizenship, living in West Germany and
mainly not supporting any political party, the
most important issue facing Germany in
November 2019 is the ongoing situation of
the COVID-19 pandemic.
Llama2
Das wichtigste Problem, das Deutschland im November
2019 konfrontiert, ist die sich erhöhte Unsicherheit und
Angst in der Gesellschaft, insbesondere bei den
Menschen, die sich nicht in der Mitte der
Gesellschaftskontaktiven Gruppenzugehörigkeit finden.
The most important problem facing Germany
in November 2019 is the growing insecurity
and fear in society, especially among people
who do not belong to the centre of society.
Mixtral
Eines der wichtigsten Probleme, mit denen Deutschland
im November 2019 konfrontiert ist, ist der Umgang mit
den Folgen des Klimawandels und die Reduzierung von
Treibhausgasemissionen, was auch entscheidend für die
zukünftige Wirtschaft ist.
One of the most important issues facing
Germany in November 2019 is dealing with
the consequences of climate change and
reducing greenhouse gas emissions, which is
also crucial for the future economy.
Table 10: Sample Answers from the Model Experiment
1.3
1
42.6
0
0
1.2
4.4
1.9
29.2
0
0.5
7
0.4
10.4
17.3
17.5
3.1
0.2
0.5
17.2
17.9
1
1.8
0.1
0.1
9.6
0.3
13.4
2.8
10.9
0.4
0.1
0
42.5
7.4
2.8
0.1
0
8
17.3
1.7
6.1
7.6
24.9
1
0.3
2.3
14.6
8.7
7.9
1.3
0
3.1
24.2
0.2
3.7
Political 
System and Processes
Social 
Policy
Health 
Policy
Family and 
Gender Equality
Education
 Policy
Environment-
 al  Policy
Economic 
 Policy
Security
Foreign 
 Policy
Media and  
Communication
Other
Migration 
and Integration
East  
Germany
Values, political 
culture, 
 social criticism
0
5
10
15
20
25
30
35
40
gemma llama-2 Mixtral wave 12
Percentage
Figure 12: Label distributions of three experimented LLMs
wave
12
13
14
15
16
17
18
19
20
21
PA survey resample
0.38
0.55
0.52
0.46
0.42
0.37
0.38
0.36
0.34
0.52
κ survey resample
0.27
0.27
0.29
0.21
0.22
0.23
0.24
0.24
0.23
0.25
PA Llama2
0.14
0.56
0.41
0.46
0.31
0.24
0.23
0.21
0.19
0.25
κ Llama2
0.02
0.01
0.03
0.03
0.03
0.02
0.02
0.04
0.03
0.02
Table 11: Proportional Agreement (PA) and (κ) Scores. The original survey is the first annotator, and the second
annotator is the survey resample (comparison to stratified sampling from the original survey) or Llama2 model
19

--- Page 20 ---

Category
Source
Gemma
Llama2
Mixtral
Mean APE
East Germany
LLM
0.5
0.7
1.8
368.07
Survey
0.2
0.2
0.2
Economic Policy
LLM
4.9
20.2
14.8
78.02
Survey
9.0
9.0
9.0
Education Policy
LLM
0.1
0.5
0.0
91.38
Survey
2.4
2.4
2.4
Environmental Policy
LLM
1.2
14.8
35.3
78.09
Survey
14.6
14.6
14.6
Family and Gender Equality Policy
LLM
0.1
0.4
0.1
56.62
Survey
0.3
0.3
0.3
Foreign Policy
LLM
28.8
2.0
0.3
753.35
Survey
1.3
1.3
1.3
Health Policy
LLM
41.6
3.3
0.4
1344.72
Survey
1.1
1.1
1.1
Media and Communication
LLM
0.1
0.1
0.0
83.89
Survey
0.0
0.0
0.0
Migration and Integration
LLM
7.2
8.6
14.9
57.41
Survey
24.1
24.1
24.1
Others
LLM
0.0
0.2
6.1
97.60
Survey
3.0
3.0
3.0
Political System and Processes
LLM
1.4
15.7
2.6
84.93
Survey
7.5
7.5
7.5
Security
LLM
2.0
1.8
3.3
70.10
Survey
7.9
7.9
7.9
Social Policy
LLM
1.2
16.0
12.2
60.48
Survey
24.8
24.8
24.8
Values, Political Culture, and Social Criticism
LLM
10.8
15.6
8.3
207.01
Survey
3.8
3.8
3.8
APE
150.0
70.0
73.0
Table 12: Comparison of Predicted Label Percentages in Experiment 1. Colors indicate differences between LLM
and survey: green (LLM > Survey + 1%), red (LLM < Survey −1%), black (|LLM −Survey| < 1%).
20

--- Page 21 ---

Category
src
12
13
14
15
16
17
18
19
20
21
mean APE
Foreign Policy
llm
1.8
0.1
0.5
0.3
1.0
0.8
1.0
1.2
1.4
1.2
112.94
survey
1.2
0.3
0.3
0.3
0.3
0.4
0.6
0.7
0.4
0.4
Education Policy
llm
0.5
0.2
0.2
0.4
0.6
0.4
0.4
0.4
0.4
0.6
75.13
survey
2.2
1.0
1.1
1.4
2.0
2.4
1.7
2.0
2.2
1.1
Family and Gender Equality Policy
llm
0.2
0.0
0.1
0.0
0.1
0.0
0.0
0.1
0.1
0.1
61.72
survey
0.3
0.1
0.1
0.3
0.2
0.3
0.2
0.2
0.2
0.2
Health Policy
llm
3.1
92.4
68.9
78.5
55.6
50.6
48.3
33.9
34.0
32.0
60.4
survey
1.0
59.5
54.2
54.2
47.4
33.7
33.5
26.0
20.2
57.9
LLM Refusal
llm
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
nan
survey
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
Media and Communication
llm
0.1
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
98.33
survey
0.0
0.0
0.1
0.1
0.1
0.0
0.0
0.0
0.0
0.1
Migration and Integration
llm
9.6
0.5
1.6
1.4
2.1
2.3
2.4
2.2
2.1
1.8
77.65
survey
23.0
9.5
11.1
6.4
6.5
10.9
10.3
11.7
10.3
7.1
East Germany
llm
0.3
0.1
0.4
0.1
0.2
0.4
0.3
0.3
0.3
0.4
949.73
survey
0.2
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.1
0.1
Political System and Processes
llm
17.3
0.3
1.5
1.1
1.5
1.1
1.4
1.5
1.5
1.9
75.8
survey
7.2
2.7
3.0
5.2
5.4
4.6
4.6
4.5
6.7
3.2
Security
llm
1.0
0.2
0.2
0.3
0.6
0.7
0.5
0.4
0.4
0.4
83.5
survey
7.5
1.8
4.0
2.4
2.7
3.0
2.2
2.2
2.1
2.3
Others
llm
0.1
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
99.37
survey
3.0
2.1
2.1
3.2
3.1
2.6
2.5
2.2
2.3
1.8
Social Policy
llm
17.5
1.2
9.5
5.2
14.0
16.3
15.1
17.0
17.4
26.3
56.05
survey
23.7
7.5
9.1
8.6
8.8
12.2
10.7
13.4
14.8
8.0
Environmental Policy
llm
17.2
0.5
2.3
3.2
8.1
10.5
12.7
23.4
22.6
14.8
30.98
survey
13.9
2.0
3.2
4.2
7.4
11.5
18.1
20.5
21.1
7.8
Values, Political Culture and General Social Criticism
llm
13.4
1.3
5.8
2.6
4.5
3.7
4.7
4.7
4.5
5.8
191.96
survey
3.6
0.8
1.4
1.4
2.0
1.5
1.4
1.4
1.4
2.1
Economic Policy
llm
17.9
3.1
9.0
6.9
11.8
13.2
13.2
14.9
15.3
14.8
59.31
survey
8.3
8.9
6.2
8.4
9.4
11.8
9.2
10.2
12.5
4.9
Not Specified
llm
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
100.0
survey
3.7
3.0
3.5
3.1
3.8
4.0
4.0
4.1
4.9
2.4
Do Not Know
llm
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
100.0
survey
1.1
0.7
0.8
0.8
0.9
1.1
0.9
1.0
0.8
0.7
APE
71.0
66.0
46.0
50.0
38.0
50.0
53.0
47.0
51.0
80.0
Table 13: Comparison of Predicted Label Percentages between survey and LLM-answers in Experiment 2. Colors
indicate differences between LLM and survey: green (LLM > Survey + 1%), red (LLM < Survey −1%), black
(|LLM −Survey| < 1%).
21

--- Page 22 ---

East Germany
West Germany
0.22
0.24
0.26
0.28
0.3
Commercial or agricultural
apprenticeship
Commercial
apprenticeship
Completed vocational internship/
volunteer work
Completed
apprenticeship
No vocational edu
Specialist
school
diploma
University of
applied sciences
degree
University
degree
Vocational school diploma
craftsman or technician qualification
vocational
training
0.2
0.25
0.3
0.35
0.4
0.45
female
male
0.2
0.22
0.24
0.26
0.28
High school diploma
Higher education
entrance
qualification
Intermediate
school
diploma
No
school
diploma
Secondary
school
diploma
student
0.2
0.4
0.6
0.8
18-29
30-44
45-59
60+
0.2
0.22
0.24
0.26
0.28
A
minor
party
Die Linke
No
party
die AfD
die CDU/CSU
die FDP
die Grünen
die SPD
0.15
0.2
0.25
0.3
0.35
JS Distance
JS Distance
JS Distance
JS Distance
JS Distance
JS Distance
region
vocational degree
gender
education degree
age groups
leaning party
Figure 13: The mean and ±1 standard deviation of JS Distances for social groups in Experiment 2.
12
12
12
12
12
12
13
13
13
13
13
13
14
14
14
14
14
14
15
15
15
15
15
15
16
16
16
16
16
16
17
17
17
17
17
17
18
18
18
18
18
18
19
19
19
19
19
19
20
20
20
20
20
20
21
21
21
21
21
21
12
12
12
12
12
12
13
13
13
13
13
13
14
14
14
14
14
14
15
15
15
15
15
15
16
16
16
16
16
16
17
17
17
17
17
17
18
18
18
18
18
18
19
19
19
19
19
19
20
20
20
20
20
20
21
21
21
21
21
21
region
leaning party
gender
education degree
vocational degree
age groups
0
0.01
0.02
0.03
0.04
0.05
0.06
0.07
0.08
0.09
0.1
0.11
0.12
0.13
0.14
0.15
0.16
0.17
0.18
0.19 Source
survey
llm
Cramer's V
Figure 14: Cramér’s Values for pairwise patterns between the six prompting variables and text answers from the
survey and LLMs in Experiment 2
22

--- Page 23 ---

Social Group Category
Social Group
Gemma
Llama2
Mixtral
Population
Population
0.617
0.287
0.295
Age Groups
18-29
0.638
0.233
0.246
30-44
0.613
0.310
0.310
45-59
0.627
0.307
0.309
60+
0.610
0.286
0.299
Vocational Degree
Completed vocational internship/volunteer work
0.640
0.491
0.278
Vocational school diploma
0.600
0.314
0.264
University of applied sciences degree
0.626
0.272
0.339
Specialist school diploma
0.603
0.269
0.355
Completed apprenticeship
0.618
0.304
0.305
Master craftsman or technician qualification
0.626
0.297
0.374
University degree
0.618
0.287
0.334
In vocational training
0.648
0.238
0.306
Commercial or agricultural apprenticeship
0.629
0.335
0.287
Commercial apprenticeship
0.630
0.302
0.320
No vocational training completed
0.619
0.289
0.242
Gender
Male
0.617
0.300
0.325
Female
0.619
0.279
0.279
Leaning Party
AfD
0.618
0.329
0.351
CDU/CSU
0.612
0.325
0.301
FDP
0.648
0.374
0.423
Grünen
0.639
0.232
0.556
A minor party
0.606
0.307
0.323
Linke
0.594
0.256
0.267
SPD
0.619
0.275
0.318
No party
0.651
0.340
0.352
Region
East Germany
0.599
0.300
0.294
West Germany
0.623
0.285
0.299
Education Degree
High school diploma
0.617
0.279
0.326
Higher education entrance qualification
0.622
0.293
0.343
Secondary school diploma
0.625
0.320
0.241
Intermediate school diploma
0.619
0.295
0.302
Student
0.833
0.680
0.379
No school diploma
0.667
0.385
0.348
Table 14: Detailed JS Distances in each social group category in Experiment 1
23

--- Page 24 ---

vocational
training
Commercial
apprenticeship
Completed vocational internship/
volunteer work
Completed
apprenticeship
Commercial or agricultural
apprenticeship
No vocational edu
Vocational school diploma
Specialist
school
diploma
University of
applied sciences
degree
University
degree
craftsman or technician qualification
2.4
2.45
2.5
2.55
2.6
2.65
0.24
0.26
0.28
0.3
0.32
0.34
0.36
0.38
0.4
Secondary
school
diploma
Intermediate
school
diploma
High school diploma
Higher education
entrance
qualification
No
school
diploma
2.5
2.55
2.6
2.65
2.7
0.22
0.24
0.26
0.28
0.3
0.32
0.34
0.36
0.38
0.4
45-59
18-29
30-44
60+
2.51
2.52
2.53
2.54
2.55
2.56
2.57
0.242
0.244
0.246
0.248
0.25
0.252
0.254
0.256
0.258
0.26
West Germany
East Germany
2.52
2.54
2.56
2.58
2.6
2.62
2.64
2.66
2.68
0.24
0.245
0.25
0.255
0.26
0.265
0.27
Subpopulation's Survey Entropy
Subpopulation's Survey Entropy
Subpopulation's Survey Entropy
Subpopulation's Survey Entropy
JS Distance
JS Distance
JS Distance
JS Distance
vocational degree
education degree
age groups
region
Figure 15: Survey’s Subpopulation Entropy and the JS Distance in Experiment 2 (mean values for waves 12-21).
24

--- Page 25 ---

Prompt
Llama2 Answer
What were the vote percentages for
the major candidates in the 2016 US
presidential election?
In the 2016 US presidential election, the vote percentages for the major candidates
were:
Donald Trump (Republican): 46.1%
Hillary Clinton (Democratic): 48.2%
Gary Johnson (Libertarian): 3.3%
Jill Stein (Green): 1.1%
Note: These figures represent the national popular vote, excluding Maine and
Nebraska, which allocate electoral votes proportionally.
What were the vote percentages for
the major candidates in the 2020 US
presidential election?
In the 2020 United States presidential election, the vote percentages for the major
candidates were as follows:
* Joe Biden (Democratic Party): 51.1% (665,8533,295 votes)*
Donald Trump (Republican Party): 47.5% (62,2045,637 votes)*
Other candidates: 1.4% (19,362,8822 votes)
Note: These figures are based on the official results from the Federal Election
Commission and may not reflect final totals or percentages.
What were the vote percentages in the
2017 German federal election?
The vote percentages in the 2017 German federal election were as follows:
Chancellor Angela Merkel’s Christian Democratic Union (CDU): 32.9%
Social Democratic Party (SPD): 20.5%
Alternative for Germany (AfD): 12.6%
Free Democratic Party (FDP): 10.7%
Green Party: 9.2%
Note: These figures represent national vote share. Actual seat distribution may
differ due to proportional representation.
What is the most important problem in
Germany in November 2019? List the
answers and their percentages for the
German population. Do your best
guess.
It is difficult to determine the most important problem in Germany in November
2019, as opinions and priorities can vary greatly among individuals and groups.
However, based on current events and societal trends, here are some of the issues
that might be considered important by the German population:
1. Climate change and environmental protection (25-30%) - Concerns about climate
change and the environment have been growing in Germany, with increased
activism and calls for stronger government action to reduce carbon emissions and
protect natural resources.
2. Economy and job security (20-25%) - The German economy has been facing
challenges, including a slowdown in growth and job insecurity, particularly in the
automotive and manufacturing sectors.
3. Immigration and integration (15-15%) - Germany has been a destination for
many refugees and migrants, and the integration of these individuals into society
has been a persistent challenge, with debates around issues such as employment,
education, and social cohesion.
4. Healthcare and social welfare (5-10%) - Germany’s healthcare system has been
under strain, with debates over funding and access to certain medical services,
particularly for low-income families.
5. European and international politics ( < 5%) - Germany has played a key role in
European Union
Table 15: Checking the factual knowledge of Llama2 model without giving any survey contexts
25

```
