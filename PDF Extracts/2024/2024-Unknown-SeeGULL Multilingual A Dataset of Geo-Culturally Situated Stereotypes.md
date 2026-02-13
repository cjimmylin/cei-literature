---
title: "2024-Unknown-SeeGULL Multilingual A Dataset of Geo-Culturally Situated Stereotypes - PDF Extract"
source_pdf: "2024-Unknown-SeeGULL Multilingual A Dataset of Geo-Culturally Situated Stereotypes.pdf"
pages: 12
extracted_at: "2026-02-13T09:50:29.885743"
---

# PDF Extract: 2024-Unknown-SeeGULL Multilingual A Dataset of Geo-Culturally Situated Stereotypes

**Source PDF:** 2024-Unknown-SeeGULL Multilingual A Dataset of Geo-Culturally Situated Stereotypes.pdf
**Total Pages:** 12

---

## Content

```
--- Page 1 ---

SeeGULL Multilingual: a Dataset of Geo-Culturally Situated Stereotypes
Mukul Bhutani
Google Research
mukulbhutani@google.com
Kevin Robinson
Google Research
kevinrobinson@google.com
Vinodkumar Prabhakaran
Google Research
vinodkpg@google.com
Shachi Dave
Google Research
shachi@google.com
Sunipa Dev
Google Research
sunipadev@google.com
Abstract
While generative multilingual models are
rapidly being deployed, their safety and fair-
ness evaluations are largely limited to resources
collected in English. This is especially prob-
lematic for evaluations targeting inherently
socio-cultural phenomena such as stereotyping,
where it is important to build multi-lingual re-
sources that reflect the stereotypes prevalent
in respective language communities.
How-
ever, gathering these resources, at scale, in var-
ied languages and regions pose a significant
challenge as it requires broad socio-cultural
knowledge and can also be prohibitively ex-
pensive. To overcome this critical gap, we em-
ploy a recently introduced approach that cou-
ples LLM generations for scale with culturally
situated validations for reliability, and build
SeeGULL Multilingual, a global-scale multilin-
gual dataset of social stereotypes, containing
over 25K stereotypes, spanning 20 languages,1
with human annotations across 23 regions, and
demonstrate its utility in identifying gaps in
model evaluations. Content warning: Stereo-
types shared in this paper can be offensive.
1
Introduction
Generative multilingual models (Brown et al.,
2020; Chowdhery et al., 2022; Anil et al., 2023)
have gained popular usage in the recent years due
to their gradually increased functionalities across
languages, and applications. However, there has
been a severe lack in cross cultural considerations
in these models, specifically when it comes to eval-
uations of their safety and fairness (Sambasivan
et al., 2021). These evaluations have been known
to be largely restricted to Western viewpoints (Prab-
hakaran et al., 2022), and typically only the English
language (Gallegos et al., 2023). This is inherently
problematic as it promotes a unilateral narrative
about fair and safe models that is decoupled from
1Languages (in ISO codes): ar, bn, de, es, fr, hi, id, it, ja,
ko, mr, ms, nl, pt, sw, ta, te, th, tr, vi; Details in Table 2.
Figure 1: Examples from SeeGULL Multilingual. Lang.
(Language): es: Spanish, fr: French, it: Italian, sw:
Swahili, fr: French; S: # of annotators (out of 3) who
reported it as a stereotype; O: mean offensiveness rating
of the stereotype.
cross cultural perspectives (Arora et al., 2023; Zhou
et al., 2023). It also creates harmful, unchecked
effects including model safeguards breaking down
when encountered by simple multilingual adversar-
ial attacks (Yong et al., 2024).
As language and culture are inherently inter-
twined, it is imperative that model safety evalua-
tions are both multilingual and multicultural (Hovy
and Yang, 2021). In particular, preventing the prop-
agation of stereotypes – that can lead to potential
downstream harms (Shelby et al., 2023) – is cru-
cially tied to geo-cultural factors (Hinton, 2017).
Yet, most sizeable stereotype evaluation resources
are limited to the English language (Nadeem et al.,
2021; Nangia et al., 2020). While some efforts
have created resources in languages other than En-
glish (Névéol et al., 2022), they are limited to spe-
cific contexts. On the other hand, some approaches
such as by Jha et al. (2023) have global coverage
of stereotype resources but are restricted to the En-
glish language alone. Consequently, they fail to
capture uniquely salient stereotypes prevalent in
different languages of the world, as simply translat-
ing them to other languages will lose out on cultural
relevance (Malik et al., 2022).
arXiv:2403.05696v1  [cs.CL]  8 Mar 2024

--- Page 2 ---

In this work, we address this critical gap by em-
ploying the SeeGULL (Stereotypes Generated Us-
ing LLMs in the Loop) approach (Jha et al., 2023)
to build a broad-coverage multilingual stereotype
resource: SeeGULL Multilingual. It covers 20 lan-
guages across 23 regions they are commonly used
in. It contains a total of 25,861 stereotypes about
1,190 identity groups, and captures nuances of dif-
fering offensiveness in different global regions. We
make this dataset publicly available 2 to foster re-
search in this domain. We also demonstrate the
utility of this dataset in testing model safeguards.
2
Dataset Creation Methodology
Stereotypes are generalizations made about the
identity (id) of a person, such as their race, gender,
or nationality, typically through an association with
some attribute (attr) that indicates competence, be-
haviour, profession, etc. (Quinn et al., 2007; Koch
et al., 2016). In this work we create a multilin-
gual and multicultural dataset of stereotypes asso-
ciated with nationality and region based identities
of people. We use the methodology established by
Jha et al. (2023), which is constituted primarily of
three steps: (i) identifying relevant identity terms,
(ii) prompting a generative model in a few-shot
setting to produce similar candidate associations
for identity terms from (i), and finally (iii) procur-
ing socially situated human validations for those
candidate associations.
We chose 20 languages that diversify coverage
across global regions as well as prevalence in doc-
umented LLM training datasets (A.1). Some lan-
guages are used as a primary language in multiple
countries with distinct geo-cultures and social nu-
ances (e.g., Spanish in Spain and Mexico). We
consider each language-country pair individually
and conduct the following steps separately for each.
2.1
Identifying Salient Identity Terms
Salient identities and stereotypes can vary greatly
across languages and countries of the world, and a
multilingual stereotype dataset needs to reflect this
diversity. To reliably create the dataset at scale, we
scope and collect stereotypes only about national,
and local regional identities.
2https://github.com/
google-research-datasets/
SeeGULL-Multilingual
Nationality based demonyms:
We use a list of
179 nationality based demonyms in English,3 and
translate them to target languages.4 In languages
such as Spanish, Italian, and Portuguese, where de-
monyms are gendered (e.g., Bolivian in English can
be Boliviano (masculine) or Boliviana (feminine)
in Italian), we use all gendered versions.
Regional demonyms
We source regional de-
monyms (such as Californians, Parisians, etc.)
within each country from established online
sources in respective languages (see A.8 for de-
tails). A lot of these demonyms are present only in
the respective target language without any English
translation, such as the Dutch demonym Drenten,
and the Turkish demonym Hakkârili.
2.2
Generating Associations
To generate associations in different languages,
we use PaLM-2 (Anil et al., 2023), which is a
generative language model trained on large mul-
tilingual text across hundreds of languages. Us-
ing few shot examples of stereotypes from ex-
isting datasets (Nadeem et al., 2021; Klineberg,
1951), we instruct the model to produce candi-
date tuples in the format (id, attr) (Jha et al.,
2023). The template Complete the pairs:
(id1, attr1)(id2, attr2)(id3,
trans-
lated in different languages is used to prompt the
model. The generated text gives us a large volume
of salient candidate associations.
2.3
Culturally Situated Human Annotations
Associations generated in steps so far need to be
grounded in social context of whether they are in-
deed stereotypical. Annotators were diverse in gen-
der, and compensated above prevalent market rates
(more details and annotation instructions in A.3).
Stereotype Annotations.
Three annotations are
collected for each candidate tuple in their respec-
tive language. The tuples are also annotated in
country specific manner, i.e., French tuples are an-
notated by French users in France specifically. We
adopt this approach since region of annotator resi-
dence impacts socially subjective tasks like stereo-
type annotations (Davani et al., 2022). In addition,
for languages that are common in multiple coun-
tries, we get separate annotations in each country
(e.g., Spanish in Spain and Spanish in Mexico).
3https://w.wiki/9ApA
4https://translate.google.com/

--- Page 3 ---

Offensiveness Annotations.
For each stereotype
in our dataset, we estimate how offensive it is. We
do so by obtaining three in-language, globally sit-
uated annotations for each attribute term in the
dataset on its degree of offensiveness on a Likert
scale of ‘Not offensive’ to ‘Extremely Offensive’.
3
Dataset: SeeGULL Multilingual
We introduce the dataset SeeGULL Multilingual
(SGM), a large scale dataset of stereotypes with
broad global coverage. The stereotypes are in the
form of (identity term, attribute), and include infor-
mation such as how frequently they were identified
as stereotypes, and their mean offensiveness rating.
A snapshot of the data is in Figure 1, and the data,
and data card are detailed in Appendix A.1.
Coverage:
SGM covers stereotypes in a total of
20 languages, as collected from 23 countries of the
world. The dataset has a total of 25,861 stereo-
types about 1,190 unique identities - including
gendered demonyms where applicable - and spread
across 7,159 unique attributes.
Overlap with English SeeGULL:
The English
SeeGULL (SGE) resource from (Jha et al., 2023)
has about 7,000 stereotypes about nationalities.
SGM has 9,251 unique nationality based stereo-
types, of which, only 949 stereotypes are in com-
mon with SGE. The maximum overlap is seen in
the Spanish dataset collected in Spain (13.2%), and
Portuguese in Portugal (13%), while the least over-
lap was for Tamil (4.8%), and Hindi (5.37%).5 Ad-
ditionally, 10,292 regional demonym based stereo-
types are all newly introduced in SGM, making the
overall dataset overlap with SGE about 5%.
Country-level Differences:
Languages contain
socio-cultural information which can differ at
places of use. We observe this difference in SGM
with some examples in Figure 2, for languages Ben-
gali, Spanish, and Portuguese that were annotated
across 2 regions each. At an aggregate level, of
the 1138 common tuples annotated in Portuguese
in Portugal and Brazil, 45.4% of the tuples were
marked as stereotypical by at least 2 annotators
in Portugal compared to 74.6% tuples marked as
such in Brazil. This trend is consistently noted for
each of the 3 languages (A.6). It highlights the
geo-cultural subjectivity of stereotypes, and how
perspectives differ despite sharing the same lan-
guage.
5Based on exact match of translated stereotypes.
Figure 2: Example differences in known stereotypes in
the same language across two different countries. S(Ci)
is the # annotators marking the tuple as stereotype in
country Ci. Countries are denoted by their ISO codes.
Stereotypes about Gendered Demonyms.
Gen-
dered demonyms result in gendered, and sometimes
intersectional stereotypes about people in different
countries. SGM records these for Spanish, Por-
tuguese, Italian, and Dutch. For e.g., in Portugal,
the identities Bragantinos (male) and Bragantinas
(female) associated with the region of Braganca
are associated with attributes party-goers and con-
servative respectively. We see most notable dif-
ferences between attributes associated with gen-
dered demonyms in Portuguese and Spanish, with
attributes about beauty such as pretty, or brunette
being associated with feminine identities, while
warrior, or brave with masculine ones.
4
SGM for Analysis and Evaluations
4.1
Offensive Stereotypes in SGM
While all stereotypes can have negative down-
stream impacts, some associations that imply de-
generacy and criminality are especially offensive.
Aggregating over stereotypes about nationalities
across all languages in SGM, we note how Alba-
nia and Rwanda have some of the most offensive
stereotypes associated with them, while Singapore
and Canada have the least offensive stereotypes
associated (A.4). Figure 3 shows the aggregated
offensiveness associated with different countries of
the world.
Figure 4 showcases some examples of highly
offensive stereotypes associated with different na-
tional and regional identities (also A.4).
The perception of an attribute or stereotype as
offensive or not can vary by language, and geo-
culture (Zhou et al., 2023). So we also aggregate

--- Page 4 ---

Figure 3: Offensive Annotations for nationalities of the
world. We take all the stereotypes along the nationality
axis, and find the average mean offensive score, cor-
responding to each country. The countries having the
darker shades of red, have on an average, more offensive
stereotypes associated with them.
Figure 4: Example of highly offensive stereotypes. The
column country denotes the country of annotation.
over the individual languages, and observe that Ital-
ian and Swahili have the most number of offensive
stereotypes with about 22% of all stereotypes for
these languages being marked as “Somewhat Offen-
sive" or more. On the other extreme, Hindi (1.83%)
and Korean (2.66 %) are the languages having the
least fraction of offensive stereotypes (full list in
A.4 Table 4) .
4.2
Foundation Model Evaluations with SGM
Evaluating stereotyping by multilingual language
models is challenging due to paucity of resources
in languages apart from English. SGM enables us
to create an evaluation set measuring whether a
system endorses stereotypical associations across
a socially situated, globally localized, and more
comprehensive set of stereotypes, and whether the
extent of endorsing stereotypes differs by language.
We adapt evaluation methods for measuring bias
in inference capabilities (Dev et al., 2020; Parrish
আিম এমন একজনেক িচিন 
িযিন "সুশ্রঙ্খল।" ব্যিক্তি཯ট হল:
(A) বাহরাইন
(B) জাপািন
(C) ິমাজাি࿂ম্বিকান
(D) ິসামাཀྵল
পরবতীর্তী লাইেন আপনার উত্তর 
ཀྵলখুন, অথবা আপিন যিদ 
অিনཨশ্চিত হন তেব (?) ཀྵলখুন।
I know a person who is 
"orderly." The person is:
(A) Bahrain
(B) Japanese
(C) Mozambican
(D) Somali
Write your answer on 
the next line, or write (?) 
if you are unsure.
Figure 5: Example of evaluation prompt in Bengali and
English translation. The stereotypical identity associ-
ated with the blue attribute is highlighted in orange.
↓Endorsed,
Endorsed,
Model
Multilingual
English
Delta
PaLM 2
61.3%
58.9%
+2.4
GPT-4 Turbo
43.0%
33.6%
+9.4
Gemini Pro
39.7%
41.8%
-2.1
Mixtral 8X7B
21.0%
15.3%
+5.7
Table 1: All systems evaluated endorsed stereotypical
associations; note the difference (Delta) when evaluat-
ing in-language queries vs English translated queries.
et al., 2022) to create the evaluation of foundation
models depicted in Figure 5. Each question in the
task contains only one stereotypical answer, with
other identity terms randomly sampled. We create
an evaluation set from stereotypes in SGM to create
4,600 questions, drawing 100 samples across each
language, region, and demonym type.
We evaluate four different models: PaLM 2,
GPT-4 Turbo, Gemini Pro, and Mixtral 8X7B.
We observe that all models endorse stereotypes
present in SGM, and at different rates when the
same queries are asked in English (Table 1). We
note that PaLM 2 has the highest rate of endorse-
ment, while Mixtral demonstrate the lowest. Our
results also show that English-translated queries
would have missed a significant fraction of stereo-
type endorsements in three out of four models. Fig-
ure 6 also notes that models tend to endorse stereo-
types present in different languages at different
rates. These findings further underlines the need
for the forms of multilingual evaluation enabled by
SGM.
5
Conclusion
For holistic safety evaluations of multilingual mod-
els, English-only resources or their translations
are not sufficient. This work introduces a large
scale, multilingual, and multicultural stereotype re-
source covering a wide range of global identities. It
also exposes how these stereotypes may percolate

--- Page 5 ---

Figure 6: Endorsement of stereotypes varies by lan-
guage and place. Endorsements per language and coun-
try are aggregated across all models.
unchecked into system output, due to the preva-
lent lack of coverage. In considerations of model
safety, cross cultural perspectives on stereotypes,
their offensiveness, and potential harms must be in-
cluded. We encourage future work to explore other
methods to utilize SGM to measure expressions
of representational harms and stereotypes within
application-specific contexts for global users.
Limitations
The dataset created in this work is constrained by
the resources needed to create large scale, qual-
ity data. The dataset covers 20 languages and not
the full range of many thousands of languages and
dialects used across the world. Unfortunately, gen-
eration quality of most models is limited to few
languages currently which guide our methodology.
Further, we obtain annotations from 23 countries,
whereas it could be from a much larger set given
the spread of the 20 languages. This is constrained
both by the availability of annotators and the cost of
data annotations. Next, we limit the identity terms
of recorded stereotypes to be demonyms associated
with nationalities and regions within each nation.
We also limit the granularity with which regions are
considered, and also don’t include regions within
all countries at a global scale. These are design
choices for reliably collecting stereotypes at scale,
guided by how stereotypes are socio-culturally situ-
ated (Jha et al., 2023; Hovy and Yang, 2021). While
this helps create a dataset that is grounded in local
knowledge, there are other stereotypes at other lev-
els of granularities, and about other identities that
are not covered by this work. We hope that this
work acts as a foundation, based on which larger,
multilingual safety datasets can be built.
Ethical Considerations
We emphasize that this dataset does not capture all
possible stereotypes about any identity, or stereo-
types about all geocultural identities. Thus, this
dataset should not be used alone to categorize any
model or its output as completely devoid of stereo-
types. Instead careful considerations should be
made by dataset users depending on the intended
application. Further, we explicitly call out the in-
tended usage of this dataset for evaluation purposes
in the attached Data Card (A.1). This dataset con-
tains a large number of stereotypes which can help
build model safeguards. We caution users against
unintentional, or malicious misuse.
References
Rohan Anil, Andrew M. Dai, Orhan Firat, Melvin
Johnson, Dmitry Lepikhin, Alexandre Passos, Sia-
mak Shakeri, Emanuel Taropa, Paige Bailey, Zhifeng
Chen, Eric Chu, Jonathan H. Clark, et al. 2023. Palm
2 technical report.
Arnav Arora, Lucie-aimée Kaffee, and Isabelle Augen-
stein. 2023. Probing pre-trained language models for
cross-cultural differences in values. In Proceedings
of the First Workshop on Cross-Cultural Considera-
tions in NLP (C3NLP), pages 114–130, Dubrovnik,
Croatia. Association for Computational Linguistics.
Yanhong Bai, Jiabao Zhao, Jinxin Shi, Tingjiang Wei,
Xingjiao Wu, and Liang He. 2023. Fairmonitor: A
four-stage automatic framework for detecting stereo-
types and biases in large language models.
Shaily Bhatt, Sunipa Dev, Partha Talukdar, Shachi
Dave, and Vinodkumar Prabhakaran. 2022.
Re-
contextualizing fairness in nlp: The case of india. In
Proceedings of the 2nd Conference of the Asia-Pacific
Chapter of the Association for Computational Lin-
guistics and the 12th International Joint Conference
on Natural Language Processing, pages 727–740.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, et al. 2020. Language models are few-shot
learners. Advances in neural information processing
systems, 33:1877–1901.
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin,
Maarten Bosma, Gaurav Mishra, Adam Roberts,
Paul Barham, Hyung Won Chung, Charles Sutton,

--- Page 6 ---

Sebastian Gehrmann, et al. 2022. Palm: Scaling
language modeling with pathways. arXiv preprint
arXiv:2204.02311.
Aida Mostafazadeh Davani, Mark Díaz, and Vinodku-
mar Prabhakaran. 2022. Dealing with disagreements:
Looking beyond the majority vote in subjective an-
notations. Transactions of the Association for Com-
putational Linguistics, 10:92–110.
Sunipa Dev, Akshita Jha, Jaya Goyal, Dinesh Tewari,
Shachi Dave, and Vinodkumar Prabhakaran. 2023.
Building stereotype repositories with complementary
approaches for scale and depth. In Proceedings of
the First Workshop on Cross-Cultural Considerations
in NLP (C3NLP), pages 84–90, Dubrovnik, Croatia.
Association for Computational Linguistics.
Sunipa Dev, Tao Li, Jeff M. Phillips, and Vivek Sriku-
mar. 2020. On measuring and mitigating biased infer-
ences of word embeddings. Proceedings of the AAAI
Conference on Artificial Intelligence, 34(05):7659–
7666.
Isabel O. Gallegos, Ryan A. Rossi, Joe Barrow,
Md Mehrab Tanjim, Sungchul Kim, Franck Dernon-
court, Tong Yu, Ruiyi Zhang, and Nesreen K. Ahmed.
2023. Bias and fairness in large language models: A
survey.
Gemini Team Google. 2023.
Gemini: A family of
highly capable multimodal models. arXiv preprint
arXiv:2312.11805.
Google. 2024a. Configure safety attributes | vertex ai |
google cloud.
Google. 2024b. Configure safety settings for the palm
api | vertex ai | google cloud.
Perry Hinton. 2017. Implicit stereotypes and the predic-
tive brain: cognition and culture in “biased” person
perception. Palgrave Communications, 3(1):1–9.
Dirk Hovy and Diyi Yang. 2021. The importance of
modeling social factors of language: Theory and
practice. In Proceedings of the 2021 Conference
of the North American Chapter of the Association
for Computational Linguistics: Human Language
Technologies, pages 588–602, Online. Association
for Computational Linguistics.
Akshita Jha, Aida Mostafazadeh Davani, Chandan K
Reddy, Shachi Dave, Vinodkumar Prabhakaran, and
Sunipa Dev. 2023. SeeGULL: A stereotype bench-
mark with broad geo-cultural coverage leveraging
generative models. In Proceedings of the 61st Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 9851–9870,
Toronto, Canada. Association for Computational Lin-
guistics.
Akshita Jha, Vinodkumar Prabhakaran, Remi Denton,
Sarah Laszlo, Shachi Dave, Rida Qadri, Chandan K.
Reddy, and Sunipa Dev. 2024. Beyond the surface:
A global-scale analysis of visual stereotypes in text-
to-image generation.
Otto Klineberg. 1951. The scientific study of national
stereotypes. International social science bulletin,
3(3):505–514.
Alex Koch, Roland Imhoff, Ron Dotsch, Christian
Unkelbach, and Hans Alves. 2016.
The abc of
stereotypes about groups: Agency/socioeconomic
success, conservative–progressive beliefs, and com-
munion. Journal of personality and social psychol-
ogy, 110(5):675.
Vijit Malik, Sunipa Dev, Akihiro Nishi, Nanyun Peng,
and Kai-Wei Chang. 2022. Socially aware bias mea-
surements for Hindi language representations. In
Proceedings of the 2022 Conference of the North
American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies,
pages 1041–1052, Seattle, United States. Association
for Computational Linguistics.
Mistral AI. 2024. Endpoints | mistral ai large language
models.
Mistral AI. 2024. Guardrailing | mistral ai large lan-
guage models.
Moin Nadeem, Anna Bethke, and Siva Reddy. 2021.
Stereoset: Measuring stereotypical bias in pretrained
language models. In Proceedings of the 59th Annual
Meeting of the Association for Computational Lin-
guistics and the 11th International Joint Conference
on Natural Language Processing (Volume 1: Long
Papers), pages 5356–5371.
Manish Nagireddy, Lamogha Chiazor, Moninder Singh,
and Ioana Baldini. 2023. Socialstigmaqa: A bench-
mark to uncover stigma amplification in generative
language models.
Nikita Nangia, Clara Vania, Rasika Bhalerao, and
Samuel Bowman. 2020. Crows-pairs: A challenge
dataset for measuring social biases in masked lan-
guage models. In Proceedings of the 2020 Confer-
ence on Empirical Methods in Natural Language
Processing (EMNLP), pages 1953–1967.
Aurélie Névéol, Yoann Dupont, Julien Bezançon, and
Karën Fort. 2022.
French CrowS-pairs: Exten-
sion à une langue autre que l’anglais d’un corpus
de mesure des biais sociétaux dans les modèles de
langue masqués (French CrowS-pairs : Extending a
challenge dataset for measuring social bias in masked
language models to a language other than English).
In Actes de la 29e Conférence sur le Traitement Au-
tomatique des Langues Naturelles. Volume 1 : con-
férence principale, pages 355–364, Avignon, France.
ATALA.
OpenAI, :, Josh Achiam, Steven Adler, Sandhini Agar-
wal, Lama Ahmad, Ilge Akkaya, Florencia Leoni
Aleman, Diogo Almeida, Janko Altenschmidt, and
Sam Altman et. al. 2023. Gpt-4 technical report.
Alicia
Parrish,
Angelica
Chen,
Nikita
Nangia,
Vishakh Padmakumar, Jason Phang, Jana Thompson,
Phu Mon Htut, and Samuel Bowman. 2022. Bbq: A

--- Page 7 ---

hand-built bias benchmark for question answering.
In Findings of the Association for Computational
Linguistics: ACL 2022, pages 2086–2105.
Vinodkumar Prabhakaran, Rida Qadri, and Ben Hutchin-
son. 2022. Cultural incongruencies in artificial intel-
ligence.
Kimberly A Quinn, C Neil Macrae, and Galen V Bo-
denhausen. 2007. Stereotyping and impression for-
mation: How categorical thinking shapes person per-
ception. 2007) The Sage Handbook of Social Psy-
chology: Concise Student Edition. London: Sage
Publications Ltd, pages 68–92.
Nithya Sambasivan, Erin Arnesen, Ben Hutchinson,
Tulsee Doshi, and Vinodkumar Prabhakaran. 2021.
Re-imagining algorithmic fairness in india and be-
yond.
In Proceedings of the 2021 ACM Confer-
ence on Fairness, Accountability, and Transparency,
FAccT ’21, page 315–328, New York, NY, USA. As-
sociation for Computing Machinery.
Renee Shelby, Shalaleh Rismani, Kathryn Henne,
AJung Moon, Negar Rostamzadeh, Paul Nicholas,
N’Mah Yilla-Akbari, Jess Gallegos, Andrew Smart,
Emilio Garcia, et al. 2023. Sociotechnical harms of
algorithmic systems: Scoping a taxonomy for harm
reduction. In Proceedings of the 2023 AAAI/ACM
Conference on AI, Ethics, and Society, pages 723–
741.
Agnes Sólmundsdóttir,
Dagbjört Guðmundsdóttir,
Lilja Björk Stefánsdóttir, and Anton Ingason. 2022.
Mean machine translations: On gender bias in Ice-
landic machine translations. In Proceedings of the
Thirteenth Language Resources and Evaluation Con-
ference, pages 3113–3121, Marseille, France. Euro-
pean Language Resources Association.
Aniket Vashishtha, Kabir Ahuja, and Sunayana Sitaram.
2023. On evaluating and mitigating gender biases in
multilingual settings. In Findings of the Association
for Computational Linguistics: ACL 2023, pages 307–
318, Toronto, Canada. Association for Computational
Linguistics.
Zheng-Xin Yong, Cristina Menghini, and Stephen H.
Bach. 2024. Low-resource languages jailbreak gpt-4.
Li Zhou, Laura Cabello, Yong Cao, and Daniel Her-
shcovich. 2023. Cross-cultural transfer learning for
Chinese offensive language detection. In Proceed-
ings of the First Workshop on Cross-Cultural Consid-
erations in NLP (C3NLP), pages 8–15, Dubrovnik,
Croatia. Association for Computational Linguistics.

--- Page 8 ---

A
Appendix
A.1
Dataset
The dataset contains 25,861 annotated stereotypes
across 23 language + countries of annotation com-
bination (Table 2), and is available online 6. The
first two columns of Table 7 describes the lan-
guages, countries (of annotations), and the total
annotations that are being released as part of this
dataset. Since data disagreements are features of
subjective data (Davani et al., 2022), we consider
any associations with at least 1 annotation (of 3
annotators) as stereotype to be sufficient for the
tuple to be included in the published dataset. The
filtering of the data for usage is left to the user. The
data card detailing intended usage, data collection
and annotation, costs, etc. is also made available
online 7.
Lang.
Lang.
ISO code
Country
Country.
ISO code
French
fr
France
FR
German
de
Germany
DE
Japanese
ja
Japan
JA
Korean
ko
South Korea
KR
Turkish
tr
Turkey
TR
Portuguese
pt
Portugal
PT
Portuguese
pt
Brazil
BR
Spanish
es
Spain
ES
Spanish
es
Mexico
MX
Indonesian
id
Indonesia
ID
Vietnamese
vi
Vietnam
VN
Arabic
ar
UAE
AE
Malay
ms
Malaysia
MY
Thai
th
Thailand
TH
Italian
it
Italy
IT
Swahili
sw
Kenya
KE
Dutch
nl
Netherlands
NL
Bengali
bn
Bangladesh
BD
Bengali
bn
India
IN
Hindi
hi
India
IN
Marathi
mr
India
IN
Tamil
ta
India
IN
Telugu
te
India
IN
Table 2: Languages (with ISO codes) and the countries
(with ISO codes) where we get them annotated.
Table 3 shows the distribution of tuples across
the nationality and regional axis. Of the 25,861
annotated tuples, 19,543 stereotypes have unique
English translations (via Google Translate API).
The differences arises due to the fact that we, by
6https://github.com/
google-research-datasets/
SeeGULL-Multilingual
7https://github.com/
google-research-datasets/
SeeGULL-Multilingual/blob/main/SeeGULL_
Multilingual_Data_Card.pdf
design, get a few tuples annotated in two different
countries speaking the same language (section 3
and A.6). Finally, stereotypes having different gen-
der based identity terms but with same attributes
(e.g (mauritana, árabe) and (mauritanos, árabe)) are
back-translated to English in exact same way and
are thus counted as such.
Axis
# All
Stereotypes
# Unique
Stereotypes
# identities
Nationality
14,960
9,251
492
Regional
10,901
10,292
698
Total
25,861
19,543
1,190
Table 3: Distribution of number of unique stereotypes
and identities across nationality and regional axis. For
the nationality axis, the 492 identities/demonyms map
to 179 unique international countries.
A.2
Related Stereotype Resources
Stereotype resources are essential for generative
model evaluations, and a large body of work
pushes to increase the overall coverage of these re-
sources (Nadeem et al., 2021; Nangia et al., 2020;
Jha et al., 2023). These resources help significantly
bolster model safeguards (Nagireddy et al., 2023;
Bai et al., 2023; Jha et al., 2024). Thus, it is imper-
ative that the resources cover global identities, to
enable models across modalities and languages to
be safe and beneficial for all. There have been
attempts to increase these resources across lan-
guages (Névéol et al., 2022; Sólmundsdóttir et al.,
2022; Vashishtha et al., 2023), and cultures (Bhatt
et al., 2022; Dev et al., 2023). However, due to the
cost of curating, these resources are often limited
in both size, and global coverage. In this work, we
address these challenges by leveraging social in-
formation captured and generated by multilingual
models and globally situated annotations.
A.3
Annotation Details
We get annotations from humans for two different
task. The first task, called Stereotype Annotation is
used to determine if an (identity, attribute) tuple is
considered as stereotypical or not. The second task,
Offensive Annotation is for determining the offen-
siveness of a given attribute in a particular region.
All annotations were procured through a partner
vendor who handled the recruitment, obtained in-
formed consent, and provided clean, anonymous
ratings within each task.
Annotators were recruited such that they used
the target language and resided in the country of

--- Page 9 ---

popular usage. They were also selected such that
every data point was annotated by at least one non-
male identifying person. Annotators were paid
above prevalent market rates and respecting local
minimum wage laws in respective countries.
A.3.1
Task: Stereotype Annotation
Annotators: Since we documenting stereotypes in
a multilingual setting, our annotation tasks are in
different target languages depending on the region
the task is being conducted in. Annotators are
proficient in English reading and writing, as well as
in the target language that the data is in. Moreover,
since we have regional identities corresponding to
each region, we ensure that annotators are people
living in that region. Finally, as described in section
3, for the languages of Spanish, Portuguese, and
Bengali, we perform human annotations separately
in two different regions each.
Labels: The annotators had the options to select
between three labels.
• Non-Stereotype (NS)
• Stereotype (S)
• Unsure (U) (with justification)
The label Unsure captures the case where either the
annotator does not have full confidence, or if the
tuple is factual in nature.
A.3.2
Task: Offensiveness Annotation
Annotators: The annotation task is in different tar-
get languages per dataset. Annotators are proficient
in English reading and writing, as well as in the tar-
get language that the data is in. The region that the
raters are from is also different per data segment
(for example, Spanish users in Mexico, Spanish
users in Spain, Bengali users in Bangladesh, etc.).
Each data point (attribute term) is rated by 3 anno-
tators of diverse gender identities.
Labels: The annotators need to label each attribute
as one of the following on a Likert scale.
• Not Offensive (NO) (-1): if the attribute is not
perceived as offensive at all, or is positive or
neutral such as ’good’, ’okay’, etc in English.
Consider similar terms in the language the
data is in for this task.
• Slightly Offensive (O1) (+1)
• Somewhat Offensive (O2) (+2)
• Moderately Offensive (O3) (+3)
• Extremely Offensive (O4) (+4): if the at-
tribute is perceived as extremely offensive
when associated with the identity (like female,
Russian, Asian, Jew, etc.) of a person such
as attributes implying criminal behavior and
activities, such as ’criminal’, ’terrorist’, etc
in English. Consider similar terms in the lan-
guage the data is in for this task.
• Unsure (with justification) (U) (0): if the
annotator is not sure about if the attribute is
offensive.
The answers can vary from Extremely offensive
to Not offensive. The integers from (-1) to (+4) are
used for calculating the mean offensiveness of an
attribute and are not visible to the annotators.
A.4
Offensiveness
For all the stereotypes in SeeGULL Multilingual,
we also get the offensive annotations of the cor-
responding attributes on Likert scale. For all the
attributes, we average out the offensiveness annota-
tions by the three annotators and call it the "mean
offensiveness" score.
Table 4 shows the percentage of stereotypes that
are annotated as "Somewhat offensive (O2)" or
higher, per region.
Lang. (Country)
# Stereotypes
w/ MO >= 2
% Stereotypes
w/ MO >= 2
it (Italy)
223
22.62%
sw (Kenya)
213
22.07%
es (Spain)
179
13.32%
th (Thailand)
116
12.03%
ar (UAE)
86
10.78%
pt (Brazil)
180
8.65%
es (Mexico)
142
8.14%
ja (Japan)
71
8.05%
id (Indonesia)
91
7.98%
de (Germany)
72
6.94%
ms (Malaysia)
88
6.83%
bn (India)
57
6.14%
vi (Vietnam)
47
6.01%
pt (Portuguese)
91
5.99%
fr (France)
60
4.85%
tr (Turkey)
40
3.92%
te (India)
10
3.68%
nl (Netherlands)
45
3.65%
mr (India)
38
3.17%
ta (India)
43
3.1%
bn (Bangladesh)
36
2.82%
ko (South Korea)
23
2.66%
hi (India)
14
1.83%
Table 4: Percentage of stereotypes with mean offensive
(MO) score >=2, i.e with a rating of "somewhat offen-
sive" or more.
Finally, stereotypes in SeeGULL Multilingual
can be thought of either belonging having a na-
tionality based demonym or a regional (within a
country) based demonym. For all the nationality
based demonyms in SGE, we group them based on
their corresponding countries and get an average of

--- Page 10 ---

offensiveness scores associated with them. Table
5 shows the top 20 countries which have the most
offensive stereotypes associated with them. Simi-
larly, the table 6 lists out the countries having the
least offensive stereotypes associated with them.
Country
Mean MO
# Stereotypes
Albania
2.09
33
Rwanda
1.99
46
Iraq
1.54
70
Colombia
1.50
140
Somalia
1.18
76
Afghanistan
1.07
121
Nigeria
1.05
59
Serbia
0.95
142
South Sudan
0.84
66
North Korea
0.78
370
Northern Ireland
0.73
123
Ireland
0.66
141
Syria
0.65
116
Romania
0.53
55
Crimea
0.43
61
Pakistan
0.41
74
South Africa
0.40
54
Palestine
0.39
181
Algeria
0.33
55
Israel
0.32
76
Table 5: Top 20 countries (or geographical regions)
having the highest mean offensive scores associated
with them. The higher the number, the more offensive
stereotypes are associated. Please note: we have filter
out any countries having fewer than 30 stereotypes from
this analysis.
Country
Mean MO
# Stereotypes
Singapore
-0.94
138
Canada
-0.91
63
Maldives
-0.91
134
Seychelles
-0.90
75
South Korea
-0.87
72
Slovakia
-0.87
40
New Zealand
-0.86
57
Japan
-0.86
274
Nepal
-0.85
321
Kenya
-0.85
139
Switzerland
-0.85
281
Uruguay
-0.84
135
Bhutan
-0.83
102
Bermuda
-0.83
52
Slovenia
-0.83
62
Gibraltar
-0.82
67
Denmark
-0.81
144
Greece
-0.80
296
Armenia
-0.80
43
Lebanon
-0.79
36
Table 6: Top 20 countries having the lowest mean of-
fensive scores associated with them. The higher the
number, the more offensive stereotypes are associated.
Please note: we have filter out any countries having
fewer than 30 stereotypes from this analysis.
A.5
Overlap with English SeeGULL
SeeGULL Multilingual dataset contain a total of
25,861 stereotypes out of which a total of 2370
stereotypes (949 unique stereotypes) were overlap-
ping with SGE. Thus, about 5% of unique stereo-
types in SeeGULL Multilingual overlap with SGE.
The Table 7 shows the overlap of SGE with SeeG-
ULL Multilingual corresponding to each of the 23
language + country combinations.
Lang.
(Country)
Total
Annotations
# SGE
matched
% SGE
matched
es (Spain)
1344
178
13.24%
pt (Portugal)
1520
199
13.09%
te (India)
272
35
12.86%
it (Italy)
986
121
12.27%
es (Mexico)
1745
203
11.63%
ja (Japan)
882
98
11.11%
pt (Brazil)
2082
209
10.03%
ko (South Korea)
864
86
9.95%
fr (France)
1238
115
9.28%
de (Germany)
1037
95
9.16%
ar (UAE)
943
84
8.90%
vi (Vietnam)
782
67
8.56%
tr (Turkey)
1021
84
8.22%
ms (Malaysia)
1288
103
7.99%
id (Indonesia)
1141
91
7.97%
bn (India)
929
74
7.96%
sw (Kenya)
965
76
7.87%
nl (Netherlands)
1233
97
7.86%
bn (Bangladesh)
1276
95
7.44%
th (Thailand)
964
68
7.05%
mr (India)
1197
84
7.01%
hi (Hindi)
763
41
5.37%
ta (Tamil)
1389
67
4.82%
Table 7: Per language overlap between SGE(SeeGULL
English (Jha et al., 2023)) and SeeGULL Multilingual.
A.6
Stereotypes in a Language across
Countries
A few languages are spoken across different coun-
tries in the world. These countries, that may share
the same language, due to different socio-cultural
backgrounds, can have a different notions of what
is considered a stereotype. Table 8 quantitatively
demonstrates how much annotations vary across
countries
A.7
Foundation Model Evaluations
A.7.1
Creating the Evaluation set
To create the evaluation set, we create a balanced
sample across country, language, and regional or
international demonyms. Within each bucket, we
take all attributes (e.g., orderly) where we could
also create three distracting demonyms that do not
also share an association with that same attribute.

--- Page 11 ---

Spain
Mexico
Portugal
Brazil
India
Bangladesh
Language
Spanish
Portuguese
Bengali
# candidate associations annotated
1229
1138
650
% Stereotype >= 1
65.8%
89.6%
79.7%
98.0%
67.5%
97.5%
% Stereotype >= 2
31.0%
35.2%
45.4%
74.5%
35.6%
87.5%
% Stereotype >= 3
11.6%
9.6%
21.9%
27.7%
10.3%
44.3%
Table 8: Annotation differences for the same language across two different regions.
From there, we first sample attributes, then sam-
ple from potential distracting demonyms for that
attribute. We randomize the demonyms to form a
question item. To encode each question item into
a prompt, we first substitute the attribute (in the
target language) into the English instruction prefix.
Then, we separately translate the prefix into the tar-
get language, as well as a suffix instruction. Finally,
we take those translations and merge them with the
SeeGULL Multilingual demonyms (which are al-
ready in the target language) into the prompt for the
evaluation set. We create parallel English-language
prompts using the same sample of question items.
To encode questions into English prompts, we use
the same instructions and process but without trans-
lation, using the English demonyms and attributes
from the SeeGULL Multilingual dataset.
A.7.2
Multilingual capabilities of Models
Foundation models have varying multilingual ca-
pabilities across languages. For example, the un-
derlying PaLM 2 language model was trained on
hundreds of languages (Anil et al., 2023) and Gem-
ini was trained to support a range of multilingual
capabilities (Gemini Team Google, 2023). Mix-
tral supports English, French, German, Italian, and
Spanish (Mistral AI, 2024), while GPT systems are
primarily built using English data only (OpenAI
et al., 2023). We evaluate all foundation models on
all languages included in SeeGULL Multilingual.
A.7.3
Evaluation protocol
In order to demonstrate that SeeGULL Multilingual
can be used for improving foundation models, we
run inference without additional safety guardrails
or mitigation layers that are typically used by down-
stream application developers. Mistral (Mistral AI,
2024) and Gemini (Google, 2024a) provide con-
figurable safety guardrails which we disable, and
PaLM 2 includes metadata about safety with re-
sponses (Google, 2024b) which we do not consider.
GPT models do not support configurable safety
through the API.
We run inference for evaluations through pub-
lic APIs for four families of foundation mod-
els. We draw one sample from each model with
temperature=0.
All system versions were
fixed, and inference was run during January and
February 2024. Each system was queried with tem-
perature=0.0. Model version are show in Table
9.
Model response styles varied by foundation
model, even with unambiguous and consistent in-
structions. To score responses, we use a heuristic
to parse decoded text, and considered the model to
endorse the stereotype if it produced text a) used
the format as instructed and produced the letter
of the stereotypical association, b) instead gener-
ated the exact word of the stereotypical association,
c) produced text containing only the letter of the
stereotypical association formatted as instructed,
but with other additional text, and d) all formatted
letter choices, repeating one letter choice twice.
Table 9: Inference details for each foundation model
Model
Version
API parameters
PaLM 2
text-bison-001
no filtering
GPT-4 Turbo
gpt-4-1106-preview
no sys. instructions
Gemini Pro
gemini-pro
no filtering
Mixtral 8X7B
mistral-small
no prompting
A.8
Regional Demonyms
There is no single place containing regional
demonyms for all the countries of the world. We
source the regional demonyms online from the
following sources followed by manual validation.
France:
• https://en.wikipedia.org/wiki/
Regions_of_France
• https://en.wiktionary.org/wiki/
Category:fr:Demonyms
• https://en.wiktionary.org/wiki/
Appendix:French_demonyms
Germany:
• https://en.wikipedia.org/wiki/List_
of_adjectival_and_demonymic_forms_
of_place_names#Federated_states_and_
other_territories_of_Germany
Japan:

--- Page 12 ---

• https://en.wikipedia.org/wiki/List_
of_regions_of_Japan
• Since no particular demonym are found, we default to
"People from [name of the region]".
South Korea:
• https://en.wikipedia.org/wiki/
Provinces_of_South_Korea
• Since no particular demonym are found, we default to
"People from [name of the region]".
Bangladesh:
• https://en.wikipedia.org/wiki/List_
of_adjectival_and_demonymic_forms_
of_place_names#Bangladeshi_divisions
Turkey:
• https://en.wikipedia.org/wiki/
Provinces_of_Turkey
• https://en.wiktionary.org/wiki/
Category:tr:Demonyms
Portugal:
• https://pt.wikipedia.org/wiki/Lista_
de_gent%C3%ADlicos_de_Portugal
• http://www.portaldalinguaportuguesa.
org/index.php?action=gentilicos
Brazil:
• https://en.wikipedia.org/wiki/List_
of_adjectival_and_demonymic_forms_
of_place_names#Brazilian_states
Spain:
• https://en.wikipedia.org/wiki/
Autonomous_communities_of_Spain
• https://en.wiktionary.org/wiki/
Category:es:Demonyms
Mexico:
• https://en.wikipedia.org/wiki/List_
of_adjectival_and_demonymic_forms_
of_place_names#States_of_Mexico
Indonesia:
• https://en.wikipedia.org/wiki/
Javanese_people
• https://www.dictionary.com/browse/
sumatran
• https://en.wikipedia.org/wiki/
Sundanese_people#
• https://en.wikipedia.org/wiki/
Western_New_Guinea
• https://en.wikipedia.org/wiki/
Moluccans#
• https://en.wiktionary.org/wiki/
Sulawesian
Vietnam:
• https://en.wikipedia.org/wiki/List_
of_regions_of_Vietnam
• Since no particular demonym are found, we default to
"People from [name of the region]".
United Arab Emirates (UAE):
• https://en.wikipedia.org/wiki/
Emirate_of_Abu_Dhabi
• https://en.wikipedia.org/wiki/
Emirate_of_Ajman
• https://en.wikipedia.org/wiki/
Emirate_of_Dubai
• https://en.wikipedia.org/wiki/
Emirate_of_Sharjah
Malaysia:
• https://en.wikipedia.org/wiki/List_
of_adjectival_and_demonymic_forms_
of_place_names#Malaysian_states_and_
territories
Thailand:
• No particular demonym, defaulted to "People from
[name of the region]".
Italy:
• https://en.wikipedia.org/wiki/
Regions_of_Italy
India:
• https://en.wikipedia.org/wiki/List_
of_adjectival_and_demonymic_forms_
of_place_names#Indian_states_and_
territories
Kenya:
• No particular demonym, defaulted to "People from
[name of the region]".
Netherlands:
• https://nl.wiktionary.org/w/index.
php?title=Categorie:Demoniem_in_het_
Nederlands&from=F
A.9
Licenses of models and data used
The data (SGE) was released with CC-BY-4.0 li-
cence 8 which permits its usage for research pur-
poses. The intended usage guidelines of the differ-
ent models were adhered to 9 10 11. We abide by
the terms of use of any models used in this paper.
8https://github.com/google-research-
datasets/seegull/tree/main?tab=CC-BY-4.0-1-ov-file#readme
9https://mistral.ai/terms-of-service/
10https://ai.google.dev/terms
11https://openai.com/policies/business-terms

```
