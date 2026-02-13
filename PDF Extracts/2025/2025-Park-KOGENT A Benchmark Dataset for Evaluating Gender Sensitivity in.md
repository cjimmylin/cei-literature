---
title: "2025-Park-KOGENT A Benchmark Dataset for Evaluating Gender Sensitivity in - PDF Extract"
source_pdf: "2025-Park-KOGENT A Benchmark Dataset for Evaluating Gender Sensitivity in.pdf"
pages: 16
extracted_at: "2026-02-13T10:43:53.980539"
---

# PDF Extract: 2025-Park-KOGENT A Benchmark Dataset for Evaluating Gender Sensitivity in

**Source PDF:** 2025-Park-KOGENT A Benchmark Dataset for Evaluating Gender Sensitivity in.pdf
**Total Pages:** 16

---

## Content

```
--- Page 1 ---

https://doi.org/10.1038/s41597-025-06344-3
Received: 30 May 2025
Accepted: 18 November 2025
Cite this article as: Park, S., Cho, E.,
Jung, C.Y. et al. A benchmark dataset
for evaluating gender sensitivity in
Korean political discourse with large
language models. Sci Data (2025).
https://doi.org/10.1038/
s41597-025-06344-3
Sunkyoung Park, Eunbi Cho, Chan Young Jung, Woo Chang Kang, Taegyoon Kim, Eunah
Park & Sanghoun Song
We are providing an unedited version of this manuscript to give early access to its
findings. Before final publication, the manuscript will undergo further editing. Please
note there may be errors present which affect the content, and all legal disclaimers
apply.
If this paper is publishing under a Transparent Peer Review model then Peer
Review reports will publish with the final article.
© The Author(s) 2025. Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International
License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit
to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not
have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the
article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain
permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.
Scientific Data
Article in Press
A benchmark dataset for evaluating gender
sensitivity in Korean political discourse with large
language models
ARTICLE IN PRESS

--- Page 2 ---

 
 
A benchmark dataset for evaluating gender sensitivity in Korean political 
discourse with large language models 
Sunkyoung Park, Eunbi Cho, Chan Young Jung, Woo Chang Kang,  
Taegyoon Kim, Eunah Park, Sanghoun Song 
 
Sunkyoung Park: Associate Professor, Division of Global Korean Studies, Korea University,   
https://orcid.org/0000-0001-5444-9768 
Eunbi Cho: Department of Linguistics, Korea University,  https://orcid.org/0009-0005-1704-
4063  
Chan Young Jung: Department of Linguistics, Korea University,  https://orcid.org/0009-0009-
0272-2908 
Woo Chang Kang: Associate Professor, Department of Political Science and International 
Relations, Korea University, https://orcid.org/0000-0002-8033-2288  
Taegyoon Kim: Assistant Professor, School of Digital Humanities and Computational Social 
Sciences, KAIST,  https://orcid.org/0000-0003-1230-774X 
Eunah Park: Department of Linguistics, Korea University,  https://orcid.org/0009-0008-6556-
7186 
Sanghoun Song: Associate Professor, Department of Linguistics, Korea University, 
https://orcid.org/0000-0002-4234-232X 
Corresponding author: Sanghoun Song (sanghoun@korea.ac.kr) 
 
Large language models are increasingly applied to political discourse, but their ability to 
detect culturally grounded gender sensitivity remains underexplored. We introduce KOGENT, a 
benchmark dataset of 1,222 transcripts from the Korean National Assembly, annotated for gender 
sensitivity across 6,024 utterances. Each utterance is labeled as high or low in gender sensitivity, 
based on contextual indicators of bias, discrimination, or inclusion, and tagged for the target group. 
KOGENT spans Korean legislative sessions from 1948 to 2024. Annotation reliability was ensured 
through dual coding and adjudication, yielding high intercoder agreement. When tasked with 
labeling utterances by gender sensitivity, GPT-4.1 achieved F1-scores of 87.5% (zero-shot) and 
91.2% (18-shot), while GPT-4o reached 90.4% and 91.1%, respectively. While incorporating in-
domain examples enhanced model performance, limitations in distinguishing between criticisms 
and reinforcements of inequality, culturally specific terminology, and extended contexts were 
observed for both models. Our results demonstrate KOGENT’s utility as a robust benchmark for 
analyzing gender sensitivity in Korean political speech and evaluating multilingual LLMs’ 
sociocultural alignment. 
 
Background & Summary 
 
Natural language processing (NLP) has been widely applied to the detection of gender bias 
in both online and political discourse[1-11]. While these studies have yielded valuable insights, 
they predominantly focus on overtly toxic or discriminatory language. In addition, most rely on 
data from online platforms such as Twitter or anonymous comment sections,      sources that may 
not fully reflect the linguistic dynamics of formal public discourse or political decision-making 
processes. As LLMs increasingly depend on high-quality benchmarks for performance evaluation 
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 3 ---

 
 
and enhancement, datasets with a focused emphasis on nuanced, context-dependent gender bias 
are essential to ensure the responsible deployment of models across sociocultural contexts. 
To address this limitation, we introduce  KOGENT (KOrean GENder-sensitivity Tagged 
dataset), a human-annotated dataset of 6,036 segments extracted from 1,222 meeting transcripts 
from the Korean National Assembly. Spanning all legislative sessions from the First National 
Assembly convened in 1948 to the conclusion of the 21st Assembly in 2024, KOGENT enables 
systematic and context-sensitive analysis of gender-sensitive and gender-insensitive language in 
political discourse.  
Gender sensitivity is defined as the capacity to recognize gender-based differences, 
inequalities, and biases, and to reflect this awareness through language, policies, and actions[12]. 
As a key component of gender equality and a central pillar of the Sustainable Development Goals, 
gender-sensitive communication merits greater empirical attention.  Partisan elites, in particular, 
play a pivotal role in shaping public attitudes through norm signaling and partisan-motivated 
reasoning[13-15]. Analyzing political speech hence offers unique insights into how gender norms 
are expressed, negotiated, and reinforced in the public sphere. Despite the growing body of work 
on harmful and toxic language in NLP[1-11], few studies have evaluated positive or inclusive 
language use—such as language that affirms diversity, acknowledges structural inequalities, or 
challenges systemic gender-based discrimination. KOGENT fills this gap by encompassing both 
inclusive and discriminatory utterances, thereby enabling a more comprehensive computational 
analysis of gender-related language practices in formal political discourse. 
Our contributions are fourfold. First, while much of the existing NLP literature focuses on 
detecting hate speech and overtly offensive language, inclusive or equality-promoting language 
remains understudied. In response to pervasive gender bias across NLP pipelines, prior research 
has proposed debiasing methods such as data augmentation[16], fine-tuning[17], and 
modifications to word embeddings[18-21]. However, few studies provide datasets that address 
explicitly gender-sensitive language. KOGENT fills the gap by incorporating positive expressions, 
such as acknowledgments of or solutions to gender-based discrimination and bias. 
Second, the dataset captures subtle, context-dependent forms of gender insensitive speech 
that escape detection in traditional hate speech frameworks. Superficial analysis of such 
expressions render a false neutrality, but underlying biases are revealed in context. Unlike previous 
studies centered in language marked by explicit hate or abuse, KOGENT foregrounds nuanced and 
indirect ways that gender bias may be embedded in contextual cues. Detecting such subtleties 
requires human annotation and careful contextual interpretation, underscoring the value of human-
annotated corpora that account for linguistic context and social subtext.  
Third, KOGENT focuses on the language of political elites, providing a distinct source of 
formal, policy-relevant discourse that is underrepresented in NLP research. Prior studies have 
focused largely on informal, anonymous, and emotionally charged discourse from social media 
platforms, which do not reflect the linguistic norms of institutional speech. In contrast,  legislative 
records are characterized by formality, self-monitoring, and indirectness, especially in discussions 
of sensitive topics like gender. Since legislators are fully aware that their statements are publicly 
archived, overtly discriminatory language is rare. They also understand that explicit gender-
discriminatory remarks are socially and politically unacceptable, thus they are likely to use refined 
and cautious language. This makes legislative discourse a “challenging flavor” for bias detection 
- precisely the kind that robust NLP systems should be able to handle. Furthermore, because the 
topics discussed in standing committees span a wide range of societal issues—including education, 
labor, health, and social welfare—KOGENT offers broad topical coverage, rendering it applicable 
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 4 ---

 
 
to multiple domains of public policy and discourse analysis. 
Fourth, KOGENT promotes linguistic and cultural diversity in NLP research. The vast 
majority of hate speech and bias detection datasets are in English [4, 22-25], with limited resources 
available in non-English languages[2-10]. This underrepresentation extends to the training data of 
large language models (LLMs), where Korean and other non-English languages are severely 
marginalized[26]. As a result, LLMs often fail to reflect the values, norms, and moral reasoning 
embedded in non-Anglophone contexts[27]. KOGENT contributes a comprehensive Korean-
language dataset grounded in a distinct socio-political environment. It includes expressions that 
are deeply rooted in Korean-specific gender discourse, some of which defy easy translation to 
other languages. These linguistic features challenge English-centric models and highlight the need 
to build NLP systems that are attuned to not only other languages but the sociocultural logic they 
encode. South Korea, in particular, presents a complex case: despite democratic consolidation, it 
ranks 122nd out of 193 countries in the proportion of female legislators (20.3% as of 2025, IPU) 
and has recorded the highest gender wage gap among OECD countries since 1992. In recent years, 
backlash against feminism has intensified[28-29], making the Korean legislature a revealing site 
for both progressive and regressive dynamics in gender discourse. In this context, KOGENT serves 
as a valuable resource that can enhance the cultural and contextual adaptability of LLMs beyond 
the English-speaking world. 
 
Methods 
 
Data Preparation  
     A five-step framework was used to construct KOGENT (see Fig. 1).  
 
Fig.1: Overview of KOGENT curation process 
 
We began by collecting a corpus of parliamentary speech from the Open Assembly Data 
Portal (https://open.assembly.go.kr/portal/openapi/main.do), encompassing transcripts of all 
sessions—including plenary sessions, standing and special committees, subcommittees, and 
hearings—from 1948 to 2024. In total, the dataset comprises 29,309 meeting records, with 
approximately 13.75 million speech turns. Speech turn refers to a unit of discourse in the transcript 
corresponding to a single speaker’s uninterrupted speech, from the moment they begin speaking 
until they yield the floor. The number of meetings by type and period is provided in Table S1 of 
the Supplementary Information. 
To construct the annotated dataset, we selected 1,222 transcripts, containing 1,888,382 speech 
turns, using a keyword-based sampling strategy. Following best practices from hate speech corpus 
construction[30], we filtered for transcripts containing at least 20 occurrences of predefined 
gender-related keywords (e.g., “emeni (mother)”, “pwuin (wife)”, “yuka (childcare)”, “kapwucang 
(patriarchy)”, “ceynte (gender)”, “cechwusan (low fertility)”, “tongsengay (homosexuality)”). 
This filtering step was necessary because most parliamentary records do not contain speech 
relevant to gender sensitivity; a fully random sample would hence yield a low density of analyzable 
expressions, reducing annotation efficiency and balance. 
 
Human Annotation Process 
The selected transcripts were randomly assigned to 15 trained annotators, all of whom were 
graduate or undergraduate students majoring in political science or Korean studies. Annotators 
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 5 ---

 
 
segmented each speech turn into utterances and annotated them for high or low gender sensitivity. 
Utterances annotated as high in gender sensitivity included those that      recognized gender 
discrimination, affirmed gender diversity, or reflected empathetic framing from the perspective of 
another gender. Examples included calls for equal pay, critiques of unequal childcare burdens, or 
acknowledgement of systemic bias. Utterances annotated as low in gender sensitivity included 
those that denied gender inequality, rejected diversity, or used gender-stereotyped expressions 
(e.g., unnecessarily adding gender markers in occupational titles such as “yecikwen (female 
employee)” or “yekyosa (female teacher).” Examples of annotated utterances are shown in Table 
S2.  
To accurately capture the nuance of each utterance, annotators were instructed to consider 
both the preceding and following discourse context. While these surrounding utterances were not 
used in the empirical analysis, annotators documented them in a separate column when such 
context informed their judgment. 
Quoted statements were annotated separately from the speaker’s original commentary. For 
instance, if a legislator quoted a gender-insensitive remark but showed clear criticism of or 
disagreement with it, the quotation and the critique were labeled independently to preserve 
contextual nuance.  
KOGENT also includes statements related to LGBTQ+ issues. Utterances that acknowledge 
and support sexual minorities or call for inclusive policies are labeled as reflecting high gender 
sensitivity, while homophobic or exclusionary remarks are labeled as reflecting low gender 
sensitivity.  
Annotators further recorded the target group being referred to in gender-sensitive or gender 
insensitive utterances, such as female only, male only, sexual minorities, or all populations when 
unspecified. 
 
Temporal and Institutional Considerations. 
Because KOGENT spans more than seven decades (1948–2024), the language, tone, and 
social norms concerning gender roles  have evolved considerably. Annotators were trained to 
recognize such diachronic variation by referencing period-specific linguistic conventions and 
socio-political contexts. For example, expressions that were commonly used in earlier decades 
with little consideration for  gender-related  implications are now often replaced with gender-
neutral terms as feminist discourse has become more influential in recent years. A notable case is 
the gradual replacement of yumocha (literally “mother’s cart”) with yuacha (“child’s cart”), as the 
former was criticized for implying that childcare is solely a mother’s responsibility. Annotators 
were instructed not to judge earlier expressions by present standards of gender sensitivity but rather 
to evaluate them within their respective historical contexts. To ensure consistency, calibration 
sessions using sample utterances from different decades were conducted so that annotators could 
align their judgments to the prevailing norms of each era. 
Furthermore, the structure of the National Assembly itself evolved during this period—with 
increasing diversity in meeting types such as standing committees and public hearings. These 
institutional variations introduce valuable diversity but may also influence discourse formality and 
topical focus, which users should consider when interpreting temporal trends. For example, since 
the establishment of the Gender Equality and Family Committee as a standing committee in 2002, 
the frequency of gender-sensitive utterances has increased noticeably in its proceedings. This 
institutional change reflects the growing institutionalization of gender issues in legislative 
discourse and should be taken into account when analyzing temporal or committee-level patterns 
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 6 ---

 
 
in the dataset. 
 
Intercoder Reliability  
Each transcript was independently reviewed by two annotators, introducing potential label 
disagreement. Thus, to quantify intercoder agreement, we calculated the cosine similarity between 
utterances labeled “high” or “low” gender sensitivity by the two annotators. We then examined 
label agreement at varying sentence similarity thresholds (e.g., 0.9, 0.8), with the expectation that 
pairs of sentences with higher cosine similarity scores (semantically similar sentences) would 
exhibit higher levels of agreement.  
Table 1 displays an intercoder reliability matrix for various cosine similarity thresholds. The 
calculation methods for the mean, Cohen’s Kappa, and Krippendorff’s Alpha are in the 
Supplementary Information.  
 
Threshold 
Total Matches 
Total Disagreements 
Mean 
Cohen’s Kappa 
Krippendorff’s Alpha 
0.9 
590 
5 
0.992 
0.983 
0.983 
0.7 
819 
16 
0.980 
0.961 
0.961 
0.5 
1027 
24 
0.977 
0.952 
0.952 
0.3 
1159 
32 
0.972 
0.943 
0.944 
Table 1. Inter-coder reliability by cosine similarity 
All 77 disagreed-upon utterances were resolved by a third-party adjudicator (the first 
author) to ensure annotation consistency. 
 
Data Records  
The KOGENT dataset is publicly available at Figshare [31]. It includes three main 
components: utterances.csv, containing 6,024 utterances extracted from 1,222 transcripts of the 
Korean National Assembly proceedings, english_translated_600_utterances.csv, an English-
translated subset of the data, and codebook.xlsx, an annotation codebook detailing labeling 
guidelines with examples. 
Each record in utterances.csv includes the utterance (in Korean), its gender sensitivity rating 
(H or L), the gender targeted (women, men, sexual minorities, all genders), keywords, preceding 
context, following context, transcript metadata (term, session, plenary session, committee name), 
speaker name, and annotator (anonymized). Among the 6,024 utterances, 3,868 were labeled as 
high in gender sensitivity (H) and 2,156 as low (L). 
To enhance the dataset’s usability for non-Korean researchers, we added an English-
translated subset of our dataset in english_translated_600_utterances.csv. Specifically, 
approximately 10% of the 6,024 utterances were randomly selected while maintaining label 
balance. The selected data were professionally translated by certified human translators to avoid 
potential stylistic bias or model contamination that could arise from machine translation tools or 
GPT-based systems. While the subtle nuances of gender sensitivity expressed in Korean are 
difficult to fully convey in English, a selectively translated portion of the dataset was provided to 
improve accessibility for non-Korean researchers without compromising the integrity of the 
original 
data. 
 
Data Overview 
Fig. 2 depicts the distribution of gender sensitivity labels (both H- and L-annotated 
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 7 ---

 
 
utterances) across legislative terms, showing a temporal increase in gender-related discourse, 
particularly during the 15th National Assembly (1996–2000). The trend became especially 
pronounced during the 20th National Assembly (2016–2020), which coincided with heightened 
public debate on gender equality in Korea. During this period, social controversies surrounding 
gender-based violence—such as the 2016 Gangnam Station femicide—and the rapid rise of online 
feminist movements such as #MeToo, brought issues of gender discrimination and digital sexual 
crimes to the center of public attention. These developments spurred extensive legislative 
deliberation on sexual violence, workplace discrimination, and gender-equality policy. In parallel, 
the expanded activities of the Gender Equality and Family Committee and other related standing 
committees further increased the number of gender-salient discussions in parliamentary 
proceedings. This pattern illustrates how KOGENT reflects real-world sociopolitical shifts in the 
salience and framing of gender discourse, underscoring its potential for analyzing temporal and 
contextual dynamics in political speech. 
Table 2 summarizes the distribution of annotations by targeted group and gender sensitivity 
label. Utterances referencing women comprised the majority, followed by those referencing all 
genders, men, and sexual minorities, in that order. Specifically, 3,139 utterances with high gender 
sensitivity (H) and 1,705 with low gender sensitivity (L) referred to women, making them the most 
frequently addressed group. Speech about men had a relatively balanced distribution, with 224 
high- and 192 low-sensitivity utterances. Utterances referring to all genders tended to consist of 
general statements on gender equality or institutional norms that did not specify a particular 
gender. Utterances targeting sexual minorities showed a different pattern from the others, with 185 
utterances showing low gender sensitivity and only 84 showing high sensitivity—indicating that 
discourse surrounding LGBTQ+ individuals is more likely to be discriminatory or insensitive. In 
addition to the H and L labels included in KOGENT, subsequent technical validation experiments 
incorporated “irrelevant” (I) utterances unrelated to gender to support extended classification tasks 
that account for cultural context. 
      
Fig. 2 Number of H/L annotated utterances by legislative term  
Target Subject 
H 
L 
Total 
Women 
3139 
1705 
4844 
Men 
224 
192 
416 
Sexual Minorities 
84 
185 
269 
All genders 
421 
74 
495 
Total  
3868 
2156 
6024 
Table 2. Number of H/L annotated utterances by targeted subject 
Technical Validation  
We assess the ability of two GPT models to associate each utterance in our corpus with its 
ground truth gender sensitivity label. To facilitate future work in cultural-contextual NLP, we 
incorporated both gender-sensitive utterances (labeled either H or L) and irrelevant utterances 
(labeled I). Given that the gender-sensitive utterances were sourced from the minutes of the 
National Assembly, we extracted I-labeled utterances from the National Institute of Korean 
Language Korean Parliamentary Corpus 2021 (v.1.1)[32]. This corpus comprises 4,895,642 
sentence-segmented records from subcommittee proceedings of the Korean National Assembly, 
covering the years 2003 to 2020. 
     Our dataset includes 3,868 H-labeled utterances and 2,156 L-labeled utterances, so we 
aimed to prepare approximately 3,000 I-labeled utterances to maintain a balanced design. Sentence 
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 8 ---

 
 
segmentation, performed using the Python library Kiwi (kiwipiepy)[33], revealed that about 89% 
of the H- and L-labeled utterances consisted of one to four sentences. To mirror this distribution, 
we sourced I-labeled utterances of similar length. Specifically, the Korean National Assembly 
minutes corpus was divided into chunks of four consecutive sentences, yielding a total of 
1,223,911 chunks. From these, we randomly selected 3,050 chunks that did not overlap with any 
sentences from the H- or L-labeled utterances. For each selected chunk, we randomly sampled 
between one and four sentences to form a candidate utterance. We then automatically filtered out 
utterances that were exact duplicates or contained fewer than ten characters in the Roman alphabet, 
numerical digits, or Hangul, resulting in 2,905 unique utterances.  
Subsequently, the authors, including experts in linguistics, politics, and gender studies, 
manually reviewed every utterance and excluded any that were related to gender sensitivity. 
Through this process, we finalized a set of 2,889 I-labeled utterances for use in the classification 
experiment.  
All utterances (H, L, and I labels) were first shuffled to ensure that the order of the inputs 
would not bias the models. We then conducted four classification experiments: zero-shot GPT-4o, 
18-shot GPT-4o, zero-shot GPT-4.1, and 18-shot GPT-4.1. To perform the classification, we used 
the OpenAI API, specifying model snapshots “gpt-4o-2024-11-20” for GPT-4o and “gpt-4.1-
2025-04-14” for GPT-4.1 to ensure experimental reproducibility. Each input to the user prompt 
consisted of a statement from the dataset, and the models were tasked with classifying it into one 
of three categories (H, L, or I). 
For the system prompt, we provided a detailed definition of gender sensitivity in Korean, 
consistent with the linguistic and cultural context of the data. Korean prompts were used to 
minimize potential loss of nuance that might occur during translation and to ensure that the models 
processed the original lexical, syntactic, and pragmatic characteristics of the utterances. 
In the zero-shot setting, the system prompt included only the definition of gender 
sensitivity and task instructions, while in the 18-shot setting, we appended 18 representative 
examples drawn from the dataset (6 per label, across 3 categories: family, gender, and minority 
rights) to guide the models' behavior. In both settings, the user prompt for each input followed the 
format: "문장 (Sentence): [input sentence]\n판단 (Label):", requiring the model to output a single 
label (H, L, or I) without additional text. 
We set the maximum output length (max_tokens) to 2 tokens to tightly constrain the 
response format and prevent unnecessary elaboration. The temperature parameter was set to 0.0 to 
promote deterministic behavior and maximize output consistency across similar inputs. Each 
utterance was classified independently without system memory of prior responses. The entire 
classification procedure was implemented using the OpenAI Python client. 
 
Label 
Precision 
Recall 
F1-scoe 
zero-shot 
18-shot 
zero-shot 
18-shot 
zero-shot 
18-shot 
H 
96.07 
97.02 
85.34 
85.86 
90.39 
91.10 
I 
77.15 
77.60 
99.65 
99.86 
86.97 
87.34 
L 
87.18 
89.93 
70.56 
73.91 
77.99 
81.13 
Table 3. Results of GPT-4o zero-shot and 18-shot classification 
 
Label 
Precision 
Recall 
F1-scoe 
zero-shot 
18-shot 
zero-shot 
18-shot 
zero-shot 
18-shot 
H 
97.37 
97.78 
79.47 
85.37 
87.51 
91.15 
I 
72.99 
74.78 
99.65 
99.76 
84.26 
85.48 
L 
84.12 
87.00 
70.70 
67.86 
76.83 
76.25 
Table 4. Results of GPT-4.1 zero-shot and 18-shot classification 
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 9 ---

 
 
 
Experimental results with GPT-4o and GPT-4.1 show that 18-shot prompting, using 
contextually appropriate examples related to family, gender equality, and minority rights, 
consistently improved classification performance across all labels (Table 4). GPT-4o achieved an 
F1-score improvement of 0.79% for H and 4.02% for L, while GPT-4.1 showed a 4.16% 
improvement for H (Table 3). These findings underscore the effectiveness of incorporating 
contextually relevant few-shot prompting and suggest that the constructed dataset covers diverse 
expressions of gender sensitivity, enabling models to generalize effectively to political discourse. 
Despite overall improvement, analysis of model errors revealed some limitations. The 
models occasionally struggled to interpret the intended meaning correctly, especially when it came 
to complex or culturally specific statements. For example, instances labeled ‘H’ (high in gender 
sensitivity) were sometimes incorrectly classified as ‘L’ (low in gender sensitivity). These errors 
occurred when the model failed to differentiate between statements criticizing real gender 
inequalities and those reinforcing stereotypes. A representative example is the statement, “Women 
inevitably take parental leave due to childcare responsibilities, but even taking a single day can be 
burdensome…” This reflects the reality of disproportionate childcare burdens in Korean society. 
However, the model may have misinterpreted it as a stereotypical assertion that women should be 
solely responsible for childcare. 
Another source of misclassification was unfamiliarity with recent or less common gender-
equality terminology. For instance, the term cechwulsan (“low fertility”) has long been used in 
Korean but implies that women bear responsibility for population decline. As an alternative, 
cechwulsayng (“low birth”) was proposed in 2018 by the Seoul Foundation of Women & Family 
to avoid such gender bias and is now recommended as a more neutral and inclusive term[34]. 
However, due to its relatively recent coinage and low usage frequency, the model sometimes failed 
to recognize its significance, resulting in misclassification as ‘I.’       
Furthermore, the model frequently failed to detect discriminatory language when it was 
embedded in broader contexts. A key example is the term cipsalam (“housewife”), which 
historically confined women’s social roles to the domestic sphere. While the model correctly 
classified utterances that contained this term as ‘L’ when they consisted of isolated sentences, it 
often failed to do so when the utterances were longer. This suggests that the model, while adept at 
contextual comprehension, sometimes prioritizes overall semantic flow over the detection of subtle 
gender bias[35]. The same pattern was observed with occupational terms unnecessarily marked by 
gender, such as “male nurse,”  “female employee,” or “female teacher,” which were not 
consistently flagged in extended contexts. 
Overall, the findings suggest that while LLMs show some ability to assess gender 
sensitivity in explicit cases, they are less successful at classifying more nuanced or context-specific 
expressions of gender bias. Notably, performance improved when examples from the constructed 
dataset were incorporated into few-shot prompts, highlighting the dataset’s value not only as a test 
set but also as a training resource to enhance sensitivity to more subtle forms of gender bias, 
particularly in official discourse. Given that the data consists of statements by Korean politicians, 
it reflects the sociocultural context of Korean society. Accurate interpretation of expressions such 
as cechwulsayng (“low birth”) and cipsalam (“housewife”) requires understanding underlying 
societal assumptions and gender norms in Korea. 
 
Usage Notes  
Social and Policy Implications: Although the original source material consists of 
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 10 ---

 
 
parliamentary records, this dataset can be utilized to measure gender sensitivity in text, audio, and 
visual data produced in various social contexts. It provides a foundation for descriptive analyses 
of expressions in everyday communication. Recognizing instances of low gender sensitivity in 
speech and other forms of expression can serve as an important first step toward fostering more 
gender-equitable attitudes and improving broader social norms. 
Comparative Politics Implications: The dataset enables the measurement of gender 
sensitivity across multiple units of analysis—such as individual legislators, specific meeting 
records, or entire parliamentary sessions. This, in turn, lays the groundwork for analytical research 
examining the impact of gender sensitivity on legislative behavior, including bill sponsorship, 
voting patterns, and speech-making practices. Additionally, it allows for the investigation of how 
contextual factors, such as constituency characteristics or shifts in democratic quality, influence 
policy changes related to gender equality. 
Comparative Linguistic Implications: Gender sensitivity reflects underlying socio-cultural 
characteristics. Because the KOGENT dataset captures linguistic and sociocultural nuances 
specific to Korea, it provides a unique opportunity to explore how gender sensitivity manifests 
within a particular cultural and linguistic context. Through cross-linguistic and cross-cultural 
comparisons, researchers can examine the extent to which measures of gender sensitivity 
developed in the Korean context can be generalized to other languages and societies. This offers a 
valuable starting point for expanding gender sensitivity research into the field of comparative 
linguistics. 
AI and NLP Applications: The dataset can contribute to the development of AI systems that 
detect and mitigate gender bias in text. It provides training data that can be used to improve content 
moderation, job description review, and writing assistance applications that suggest gender-
sensitive alternatives. Additionally, researchers can use this dataset to measure gender sensitivity 
in AI-generated language and fine-tune models to produce more inclusive text across various 
domains. This application bridges theoretical gender sensitivity research with practical 
technological development, potentially broadening the impact beyond academic contexts to 
everyday digital communications. 
Temporal and Contextual Limitations. We trained and calibrated annotators to account for 
diachronic and institutional variation, yet residual limitations may remain. Gender‐related 
language and parliamentary practices have changed over seven decades, so expressions that 
seemed neutral in earlier periods may be interpreted differently today; conversely, contemporary 
norms and recent shifts toward gender-neutral terminology may inadvertently color judgments of 
historical usage. Meeting-type composition also evolved (e.g., the 2002 establishment of the 
Gender Equality and Family Committee and the broader expansion of standing committees and 
hearings), potentially increasing opportunities for gender-salient speech in later years. In addition, 
keyword-based sampling may differentially capture eras, topics, and registers. These factors can 
affect longitudinal patterns even after careful training. We therefore encourage users to treat 
temporal and institutional shifts as potential confounders, apply appropriate design choices (e.g., 
term and committee fixed effects, decade- or meeting-type–specific sensitivity analyses), and 
avoid over-interpreting fine-grained trends without robustness checks. 
 
Data Availability 
The 
KOGENT 
dataset 
[31] 
is 
readily 
available 
at 
Figshare: 
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 11 ---

 
 
https://doi.org/10.6084/m9.figshare.30413125.v4. 
Code Availability 
Technical validation experiments with the KOGENT dataset [31] were conducted using 
Python to access the OpenAI API. The code, dataset, and supplementary visualization scripts are 
available at https://github.com/KORPUS-DB/KOGENT. 
 
References 
1. Albadi, N., Kurdi, M. & Mishra, S. Are they our brothers? Analysis and detection of religious 
hate speech in the Arabic Twitter-sphere. In 2018 IEEE/ACM International Conference on 
Advances in Social Networks Analysis and Mining (ASONAM) 69–76 (IEEE, 2018). 
2. Chiril, P. et al.. An annotated corpus for sexism detection in French tweets. In Proceedings of 
the 12th Language Resources and Evaluation Conference 1397–1403 (European Language 
Resources Association, Marseille, France, 2020). 
3. Fortuna, P., da Silva, J. R., Soler-Company, J., Wanner, L. & Nunes, S. A hierarchically-labeled 
Portuguese hate speech dataset. In Proceedings of the Third Workshop on Abusive Language 
Online 94–104 (Association for Computational Linguistics, Florence, Italy, 2019). 
4. Gao, L. & Huang, R. Detecting online hate speech using context aware models. In Proceedings 
of the International Conference Recent Advances in Natural Language Processing, RANLP 2017 
260–266 (INCOMA Ltd., Varna, Bulgaria, 2017). 
5. Jeong, Y. et al. KOLD: Korean offensive language dataset. In Proceedings of the 2022 Conference 
on Empirical Methods in Natural Language Processing (EMNLP 2022), 10818–10833 
(Association for Computational Linguistics, Abu Dhabi, United Arab Emirates, 2022). 
6. Lee, N., Jung, C. & Oh, A. Hate speech classifiers are culturally insensitive. In Proceedings of the 
First Workshop on Cross-Cultural Considerations in NLP (C3NLP) 35–46 (Association for 
Computational Linguistics, Dubrovnik, Croatia, 2023). 
7. Moon, J., Cho, W. I. & Lee, J. BEEP! Korean corpus of online news comments for toxic speech 
detection. In Proceedings of the Eighth International Workshop on Natural Language 
Processing for Social Media 25–31 (Association for Computational Linguistics, Online, 2020). 
8. Mubarak, H., Darwish, K. & Magdy, W. Abusive language detection on Arabic social media. In 
Proceedings of the First Workshop on Abusive Language Online 52–56 (Association for 
Computational Linguistics, Vancouver, BC, Canada, 2017). 
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 12 ---

 
 
9. Ousidhoum, N., Lin, Z., Zhang, H., Song, Y. & Yeung, D.-y. Multilingual and multi-aspect hate 
speech analysis. In Proceedings of the 2019 Conference on Empirical Methods in Natural 
Language Processing and the 9th International Joint Conference on Natural Language 
Processing (EMNLP-IJCNLP) 4675–4684 (Association for Computational Linguistics, Hong 
Kong, China, 2019). 
10. Pair, E. et al. Quantification of gender bias and sentiment toward political leaders over 20 
years of Kenyan news using natural language processing. Front. Psychol. 12, 712646 (2021). 
11. Rizwan, H., Shakeel, M. H. & Karim, A. Hate-speech and offensive language detection in Roman 
Urdu. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language 
Processing (EMNLP) 2512–2522 (Association for Computational Linguistics, Online, 2020). 
12. Azarbaijani-Moghaddam, S.. Gender awareness and development manual. Resource Material 
for Gender Trainers, A MoWA and UNDP Publication, Gender Equality, UNDP Afghanistan, Kabul 
(2007). 
13. Zaller, J. The Nature and Origins of Public Opinion. (Cambridge University Press, 1992). 
14. Lupia, A. The effect of information on voting behavior and electoral outcomes: An 
experimental study of direct legislation. Public Choice 78, 65–86 (1994).  
15. Hogg, M. A., & Reid, S. A. Social identity, self-categorization, and the communication of group 
norms. Communication Theory, 16, 7–30 (2006). 
16. Zhao, J., Wang, T., Yatskar, M., Ordonez, V. & Chang, K.-w. Gender bias in coreference 
resolution: Evaluation and debiasing methods. In Proceedings of the 2018 Conference of the 
North American Chapter of the Association for Computational Linguistics: Human Language 
Technologies, Volume 2 (Short Papers) 15–20 (Association for Computational Linguistics, New 
Orleans, Louisiana, 2018) 
17. Park, J. H., Shin, J. & Fung, P. Reducing gender bias in abusive language detection. In 
Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing 
2799–2804 (Association for Computational Linguistics, Brussels, Belgium, 2018). 
18. Bolukbasi, T., Chang, K.-w., Zou, J., Saligrama, V. & Kalai, A. Man is to computer programmer 
as woman is to homemaker? Debiasing word embeddings. In Advances in Neural Information 
Processing Systems 29 (NIPS 2016) (2016). 
19. Zhao, J., Wang, T., Yatskar, M., Ordonez, V. & Chang, K.-w. Men also like shopping: Reducing 
gender bias amplification using corpus-level constraints. In Proceedings of the 2017 
Conference on Empirical Methods in Natural Language Processing 2979–2989 (Association for 
Computational Linguistics, Copenhagen, Denmark, 2017). 
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 13 ---

 
 
20. Zhao, J., Zhou, Y., Li, Z., Wang, W. & Chang, K.-w. Learning gender-neutral word embeddings. 
In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing 
4847–4853 (Association for Computational Linguistics, Brussels, Belgium, 2018). 
21. Zhang, B. H., Lemoine, B. & Mitchell, M. Mitigating unwanted biases with adversarial learning. 
In Proceedings of the 2018 AAAI/ACM Conference on AI, Ethics, and Society 335–340 
(Association for Computing Machinery, New Orleans, LA, USA, 2018). 
22. de Gibert, O., Perez, N., García-Pablos, A. & Cuadros, M. Hate speech dataset from a white 
supremacy forum. In Proceedings of the 2nd Workshop on Abusive Language Online (ALW2) 
11–20 (Association for Computational Linguistics, Brussels, Belgium, 2018). 
23. Vidgen, B., Nguyen, D., Margetts, H., Rossini, P. & Tromble, R. Introducing CAD: The contextual 
abuse dataset. In Proceedings of the 2021 Conference of the North American Chapter of the 
Association for Computational Linguistics: Human Language Technologies 2289–2303 
(Association for Computational Linguistics, Online, 2021). 
24. Waseem, Z., Davidson, T., Warmsley, D. & Weber, I. Understanding abuse: A typology of 
abusive language detection subtasks. In Proceedings of the First Workshop on Abusive 
Language Online 78–84 (Association for Computational Linguistics, Vancouver, BC, Canada, 
2017). 
25. Zampieri, M. et al. Predicting the type and target of offensive posts in social media. In 
Proceedings of the 2019 Conference of the North American Chapter of the Association for 
Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers) 
1415–1420 (Association for Computational Linguistics, Minneapolis, Minnesota, 2019). 
26. Xu, Y. et al. A survey on multilingual large language models: Corpora, alignment, and bias. 
Front. Comput. Sci. 19, 1911362 (2025). 
27. Zewail, A., Figueroa, A., Graham, J. & Atari, M. Moral stereotyping in large language models. 
Preprint at  https://doi.org/10.31234/osf.io/t9x8r (2024). 
28. Jenkins, M. D. & Kim, H. J. The role of misogyny in the 2022 Korean presidential election: 
Understanding the backlash against feminism in industrialized democracies. Journal of East 
Asian Studies 24, 169–196, (2024). 
29. Jung, G. & Moon, M. “I am a feminist, but . . .” Practicing quiet feminism in the era of everyday 
backlash in South Korea. Gender & Society 38, 216–243 (2024). 
30. Waseem, Z., & Hovy, D. Hateful Symbols or Hateful People? Predictive Features for Hate 
Speech Detection on Twitter. In Proceedings of the NAACL Student Research Workshop 88–93 
(Association for Computational Linguistics, San Diego, California, 2016). 
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 14 ---

 
 
31. Song, S. et al. A benchmark dataset for evaluating gender sensitivity in Korean political 
discourse with large language models. figshare 
https://doi.org/10.6084/m9.figshare.30413125.v4 (2025). 
32. National Institute of Korean Language. NIKL Korean Parliamentary Corpus 2021 (v.1.1). 
https://corpus.korean.go.kr (2022).  
33. Lee, M. Kiwi: Developing a Korean morphological analyzer based on statistical language 
models and skip-bigram. Korean Journal of Digital Humanities 1, 109–136 (2024). 
34. Kim, S. A study on the characteristics of alternative expression in Korean sexist language: For 
“Gender Equality Words” in the Seoul Gender Equality Language Dictionary (2018–2020). 
Korean Studies Research 64, 287–311 (2022). 
35. Kotek, H., Dockum, R. & Sun, D. Q. Gender bias and stereotypes in large language models. In 
Proceedings of The ACM Collective Intelligence Conference 12–24 (Association for Computing 
Machinery, Delft, Netherlands, 2023).  
Author information 
Contributions 
Sunkyoung Park: conceptualization, methodology, supervision, writing-original draft, writing-
review and editing, project administration, funding acquisition. Eunbi Cho: coding, experiment, 
writing-original draft. Chan Young Jung: coding, experiment, writing-original draft. Woochang 
Kang: conceptualization, methodology, writing-review and editing, supervision. Taegyoon Kim: 
conceptualization, methodology, writing-review and editing, supervision. Eunah Park: coding, 
experiment, visualization. Sanghoun Song: conceptualization, methodology, writing-review and 
editing, supervision. 
 
Ethics declarations 
Competing interests 
The authors declare no competing interests. 
 
Additional information 
Correspondence and requests for materials should be addressed to S.S. 
 
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 15 ---

ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 16 ---

ARTICLE IN PRESS
ARTICLE IN PRESS

```
