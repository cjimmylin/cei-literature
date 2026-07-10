---
title: "2024-Liang-Whats Documented in AI 32K Model Cards - Background Extract"
source_pdf: "2024-Liang-Whats Documented in AI 32K Model Cards.pdf"
source_folder: "02-external-papers"
pages: 18
extracted_at: "2026-04-03T10:25:00"
---

# Background Extract: 2024-Liang-Whats Documented in AI 32K Model Cards

**Source PDF:** 2024-Liang-Whats Documented in AI 32K Model Cards.pdf
**Source:** 02-external-papers
**Total Pages:** 18

---

## Content

```
--- Page 1 ---

What’s documented in AI? Systematic Analysis of
32K AI Model Cards
Weixin Liang1*, Nazneen Rajani2*, Xinyu Yang3*, Ezinwanne Ozoani2, Eric Wu4, Yiqun
Chen5, Daniel Scott Smith6, and James Zou1,4,5+
1Department of Computer Science, Stanford University, Stanford, CA, USA
2Hugging Face, Inc.
3Department of Information Science, Cornell University, Ithaca, NY, USA
4Department of Electrical Engineering, Stanford University, Stanford, CA, USA
5Department of Biomedical Data Science, Stanford University, Stanford, CA, USA
6Graduate School of Education, Stanford University, Stanford, CA, USA
+Correspondence should be addressed to: jamesz@stanford.edu
*these authors contributed equally to this work
ABSTRACT
The rapid proliferation of AI models has underscored the importance of thorough documentation, as it enables users to
understand, trust, and effectively utilize these models in various applications. Although developers are encouraged to produce
model cards, it’s not clear how much information or what information these cards contain. In this study, we conduct a
comprehensive analysis of 32,111 AI model documentations on Hugging Face, a leading platform for distributing and deploying
AI models. Our investigation sheds light on the prevailing model card documentation practices. Most of the AI models with
substantial downloads provide model cards, though the cards have uneven informativeness. We find that sections addressing
environmental impact, limitations, and evaluation exhibit the lowest filled-out rates, while the training section is the most
consistently filled-out. We analyze the content of each section to characterize practitioners’ priorities. Interestingly, there are
substantial discussions of data, sometimes with equal or even greater emphasis than the model itself. To evaluate the impact of
model cards, we conducted an intervention study by adding detailed model cards to 42 popular models which had no or sparse
model cards previously. We find that adding model cards is moderately correlated with an increase weekly download rates. Our
study opens up a new perspective for analyzing community norms and practices for model documentation through large-scale
data science and linguistics analysis.
Introduction
The rising prevalence of AI models in various sectors has underscored the necessity of comprehensive model documentation1–3.
As these models grow in complexity, their inner workings can seem increasingly obscure to those without specialized
knowledge4–6. This creates a critical need for accurate and comprehensive documentation7,8. Effective model documentation
serves as a vital communication bridge between developers and users, offering explicit guidance on the model’s functionality,
from its inputs and outputs to its range of applications6,9. Importantly, it reveals potential biases, errors, and limitations inherent
in the model10. This focus on transparency cultivates trust among users, a crucial component in fields where model output has
far-reaching consequences, such as in healthcare, finance, and law enforcement11. Ultimately, model documentation serves as a
pivotal tool for improving model utility and credibility across a range of stakeholders12–16.
Model cards have emerged as the standard approach to document AI models7,17, inspired by the concept of food nutrition
labels18 and datasheets19 in the electronics industry. They are documents that provide essential information about a model
in a standardized, easy-to-understand format. At the core of these cards are sections detailing model training and validation
procedures, intended uses and potential limitations such as bias and fairness analysis, and usage guidance. Compared to
other documentation formats such as academic papers or technical reports, model cards are increasingly becoming a preferred
reference for practitioners in the AI community for a number of reasons. First, they offer more concise, relevant, and easily
understandable information about AI models, rendering them more accessible. Another important aspect of model cards is their
up-to-date nature, as they can be frequently updated to reflect any changes, improvements, or new findings about the AI model.
In contrast, academic papers, once published, may not be updated as regularly, which could result in outdated information.
Additionally, many popular model repositories, especially those originating from industry or open-source enthusiasts, don’t
have accompanying academic papers or technical reports20,21. This further accentuates the indispensable role of model cards as
arXiv:2402.05160v1  [cs.SE]  7 Feb 2024

--- Page 2 ---

a comprehensive, streamlined, and informative communication mechanism within the AI ecosystem.
While many model cards are being created by researchers and developers5–7,9,22–24, there hasn’t been a systematic analysis
of the quality and informativeness of the model cards. In particular, we do not know what has and has not been documented.
This is an important gap in our knowledge because adherence to community norms and documentation completeness directly
impact the accessibility, transparency and user trust of AI models. As AI becomes increasingly ubiquitous in society, there
is a need for regulation to keep up with the pace of technical progress25. Toward this end, industry-wide AI documentation
standards can help to spur innovation and protect against harms26, similar to how the electronics and automotive industries
have converged toward universal technical specifications27. Without comprehensive information on a model’s functionality,
limitations, and potential biases, users may not make informed decisions, leading to misuse or unintended consequences.
Furthermore, without systematic analysis of current model cards, we risk propagating insufficient documentation practices,
which can hinder efforts toward ensuring fairness, accountability, and equitable use of AI technologies.
To address this gap in knowledge, we present a comprehensive large-scale analysis on 32,111 AI model cards created from
6,392 distinct user accounts. These model cards are uploaded by developers to Hugging Face, which is one of the most popular
model repositories for hosting cutting-edge AI models across a multitude of research domains and applications28,29. Distinct
from GitHub, which hosts general software repositories, Hugging Face offers a user-friendly, AI-specific platform that provides
an integrated machine learning pipeline. Importantly, it has established community guidelines for model cards, fostering a
standardization that GitHub’s user-dependent README documents lack, making it an ideal choice for our study. Through this
analysis, we seek to characterize the extent to which the AI community has adopted and adapted model cards, the strengths and
weaknesses of current documentation efforts, as well as to evaluate their impact on model development and usage. Our study
reveals that, although the adoption of model cards has been largely successful, significant gaps persist in the completeness
and quality of the provided documentation, with more than half of the models lacking a model card. The training section is
most consistently completed, while sections addressing environmental impact, limitations, and evaluation exhibit the lowest
completion rates, indicating a need for greater emphasis on these aspects of model documentation. Furthermore, our section
content analysis of four key model card sections—Limitations, Uses, Evaluation, and Training—reveals an increased dialogue
on data, often drawing comparable, if not surpassing, attention than the AI models themselves. To assess the impact of model
cards on model utilization, we conducted an intervention study by adding detailed model cards to 42 popular models which
have no or sparse model cards previously. This resulted in a moderate increase in weekly downloads, indicating the influence of
well-documented model cards on model utilization. Our study provides a unique outlook on community norms and practices
around model documentation through large-scale data science and linguistic analysis.
Results
Data Overview of AI Models Hosted on Hugging Face
Our analysis encompasses 74,970 AI model repositories on Hugging Face uploaded by 20,455 distinct user accounts as of
October 1st, 2022. The number of models exhibits exponential growth, with a weekly growth rate of 3.16% and a doubling
time of 22 weeks (Fig. 1a). As a sanity check, the number of model repositories reached 145,306 by March 4th, 2023, thereby
confirming the exponential trend. The top 5 trending AI model1 repositories on Hugging Face over time reveal shifts in
community attention (Fig. 1b). Initially, GPT and BERT models dominated, reflecting a focus on language understanding and
text generation. However, in Q3 2022, interest shifted toward image generative models, particularly Stable Diffusion and its
variants, highlighting diverse interests beyond natural language processing. Despite the widespread adoption of Hugging Face
model cards, only 32,111 (44.2%, contributed by 6,392 distinct user accounts) out of the 74,970 model repositories currently
include model cards as Markdown README.md files within their model repo (Fig. 1c). However, these models account for
90.5% of total download traffic, highlighting the significance of model cards in fostering model adoption and usage. Here
the download traffic is measured by the number of model repositories downloads. In light of these findings, our subsequent
analyses will concentrate on the 32,111 models equipped with model cards.
Completeness of Model Cards Across Various Sections
Model cards provides a standardized structure for conveying key information about AI models. Grounded in academic literature7
and official guidelines from Hugging Face17, model cards conventionally comprise sections such as Training, Evaluation, Uses,
Limitations, Environmental Impact, Citation, and How to Start. As illustrated in Fig. 1d, these sections represent the essential
constituents of a comprehensive model card. We parsed and evaluated the structure of model cards using a keyword-based
detection pipeline for each section (e.g., detecting mentions of CO2 and its variants to identify the Environmental Impact
section).
1The trending models were defined as those receiving the most likes within a specific time period, following Hugging Face’s official definition30.
2/18

--- Page 3 ---

Our evaluation indicates a significant disparity in community attention to different model card sections, a trend that seems
to be expanding over time. Across all the model cards, Environmental Impact (2.0%, or 639 out of 32,111 model cards),
Citation (14.4%), Evaluation (15.4%), and Limitations (17.4%) sections exhibit the lowest filled-out rates, while the Training
section (74.3%) is most frequently filled out (Fig. 2a). Similar trends also hold for top 100 model cards and top 1000 model
cards. Sections with lower fill-out rates also tends to have shorter average section word count among filled-out, indicating low
community attention (Fig. 2c). For example, the Environmental Impact section demonstrates both a low completion rate (3.7%)
among the top 1,000 model cards and a low average word count (68 words) among the filled-out ones. In contrast, the Training
section exhibits the highest filled-out rate (71.0%) and the second highest average word counts (168 words). Interestingly,
despite its lower completion rate (22.1%), the Limitations section tends to be the longest (151 words on average), hinting at the
complex nature of discussing model limitations. Results are consistent across the top 100 model cards and the all the model
cards (Supp. Fig. S1).
The disparities in community attention across different sections are progressively widening over time. A notable trend is
the rapid increase in the filled-out rate for the Training section, which is increasing at 0.2% per week (p = 3.31E-244), even
after accounting for model categories such as tabular and natural language processing. The Environmental Impact section also
exhibits an increase in its fill rate (p = 4.64E-24). An interesting discovery is that a large majority, about 84.8% (542 out of
639), of the Environmental Impact sections appear to be automatically created by AI model-building tools31,32, which not only
make the AI model but also part of the model card. In particular, about 58.5% (374 out of 639) of these sections mention
"Model Trained Using AutoNLP," while around 26.3% (168 out of 639) state "Model Trained Using AutoTrain." Moreover,
their section text aligns perfectly with the template provided by AutoNLP/AutoTrain. The adoption of these automated tools to
track CO2 emissions is a welcome change, as they increase awareness about the environmental impact of AI models. Through
these tools, developers can better grasp the carbon footprint of their models, leading to more informed decisions during their
creation and training process. Meanwhile, the filled-out rates for other sections are experiencing a decline (p < 0.001, Supp.
Table S1).
Top model cards associated with the most downloaded models are distinctive from an average model card in a number of
ways. One distinctive feature is that they are considerably longer (Fig. 2b, Supp. Table S2). The top 100 model cards are, on
average, 1.35 times longer than the top 1,000 model cards (521 words vs. 384 words) and 2.73 times longer than an average
model card at the population level (191 words). The section filled-out rate also differ significantly. Take top 100 model cards as
an example. Although their Training section completion rate is similar to the population level (81% vs. 74.3%), they have
significantly higher filled-out rates for Environmental Impact (9.0% vs. 2.0%), Limitations (39.0% vs. 17.4%), and Evaluation
(47.0% vs. 15.4%) sections. The top 100 also have significantly higher filled-out rates in the Citation section (67.0% vs. 14.4%).
These findings underscore the fact that top model cards are generally more detailed and structured, with a greater emphasis on
sustainability and more thorough discussions of model performance and limitations. Furthermore, top models often have a
strong connection to the academic research community, as shown by the high frequency of filled-out citation sections. Users
may find these models more appealing because they come from scientific research, which is typically thoroughly checked for
quality and accuracy by other experts in the same field.
A Deep Dive into Model Card Content
To gain a comprehensive understanding of current practices and challenges in model documentation and identify areas for
improvement, we conducted a content analysis of four critical model card sections on Hugging Face: Limitations, Uses,
Evaluation, and Training. This analysis was motivated by Hugging Face’s internal user study33, which identified the Limitations
and Uses sections as the most challenging to write, and the fact that Evaluation and Training are two indispensable aspects
of AI models. We employed a sentence-level topic modeling approach to accurately identify patterns and themes within the
text, enabling a fine-grained analysis of model card sections compared to document-level topic modeling (see Methods). We
quantified the prevalence of specific themes by calculating the frequency of sections containing sentences that mention those
themes, both across all model cards and within the top 100 model cards.
Limitations Sections
In the Limitations sections, our topic analysis uncovered a diverse array of subject matter, reflecting the
myriad challenges and limitations faced by AI models. We identified three primary themes: disclaimers, data limitations, and
model limitations. Disclaimers emerged in 11.6% of the filled-out Limitations sections, often emphasizing the model is "not
intended for production" or "should not be considered a clinical diagnostic tool," particularly for medical AI models. Explicit
disclaimer sentences regarding third-party usage were also noted. In the top 100 model cards, a large majority, about 89.2%, of
the filled-out Limitations sections included such disclaimers. This stands in contrast to the typical practice in academic research
papers, where disclaimers are less frequently seen34,35. This distinction is probably a reflection of the low barrier of access and
deployment of AI models on Hugging Face, thereby requiring explicit cautionary notes to mitigate risks tied to potential misuse
of AI models. Data and model limitations received nearly equal attention, appearing in 30.1% and 27.2% of the filled-out
Limitations sections, respectively. Their prevalence on the top 100 model cards are similar too. In data limitations, developers
3/18

--- Page 4 ---

discussed the biases in training data, and the limited training data coverage. Discussions on model limitations revolved around
both technical and societal aspects. From a technical standpoint, constraints, such as the maximum input length (e.g., 1024
tokens) for transformer-based models, were noted. On the societal front, concerns were raised about the biases in the AI model,
as well as the potential risks that the AI model would inherit biases from its pre-trained backbone models (e.g., "since the model
is further pretrained on the BERT model, it may have the same biases embedded within the original BERT model.").
Uses Sections
In the Uses sections, our topic analysis uncovered three primary themes: designated model functionality,
operational guidelines, and misapplications. The most prominent theme in the Uses sections was the designated model
functionality, featured in 58.2% of the filled-out Uses sections. Here, developers clearly laid out the specific tasks the model
was built for, such as "a fine-tuned model for generating tweets related to Indian politics." Closely linked was the theme of
operational guidelines, covered in 25.2% of the filled-out sections. This included practical information like installation steps,
usage examples, checkpoint details, and fine-tuning instructions. Another important theme was misapplications, outlining the
improper or out-of-scope use of the models. This theme, seen in 8.1% of the filled-out sections, covered topics like malicious
usage or the model’s deployment in high-stakes situations. Although some overlap exists between the themes in the Limitations
and Uses sections, each emphasizes distinct aspects. For example, broad statements on commercial usage might appear under a
Disclaimer theme in Limitations, whereas specific warnings about misuse feature in the misapplication theme in Uses.
Evaluation Sections
Our topic analysis of the Evaluation sections in model cards highlighted two key themes: evaluation
data and evaluation results. Featured in 37.8% of the filled-out sections, the first theme, evaluation data, described various
datasets used for model testing. The second theme, evaluation results, appeared in 26.9% of the filled-out sections, presenting
performance metrics such as F1 scores and BLEU scores that depict a model’s competence. Interestingly, these performance
evaluations tend to present aggregate metrics across complete test datasets. Yet, such a broad approach can often obscure
systematic errors within specific subgroups36. For this reason, there’s a growing call in the research community for more
granular, subgroup-based evaluations that take into account factors such as age, gender, and location2,37. This fine-grained
evaluation method aligns with practices in medicine. For instance, the U.S. Food and Drug Administration has mandated
disaggregated clinical trial results38, requiring the analysis and reporting of outcomes by demographic subgroups, including
sex, race, and age. This practice is designed to ensure the safety and efficacy of treatments across a diverse population and to
uncover any disparities in response among different demographic groups. By adopting such an approach, emphasizing granular
insights, the AI community can move towards a paradigm that promotes better understanding and communication of model
strengths and limitations, driving towards a more inclusive and fair AI ecosystem, benefiting all users equally.
Training Sections
In the Training sections, our analysis surfaced three main themes: hyperparameter configurations, training
data, and training protocol. The theme of hyperparameter configurations, featured in 39.5% of the completed sections, provides
important information such as the number of epochs, batch size, and the selected optimizer. Equally important is the theme of
training data, appearing in 32.7% of the filled-out sections. This theme provides a comprehensive description not only of the
volume and characteristics of the training dataset, but also of specific data pre-processing steps such as "convert all characters
to lowercase." Recent studies have highlighted the time-intensive nature of data work in AI development39,40. The third theme,
training protocol, appearing in 25.1% of the filled-out sections, presents the technical steps required to replicate the training
process. Taken together, these themes underscore a broader commitment within the AI community towards transparency and
reproducibility by enabling researchers, practitioners, and industry stakeholders to efficiently build upon others’ work41,42.
Model Card Intervention Study
It is not well-understood how the quality of the model card affects model usage. To quantitatively study this relationship, we
drew inspirations from well-established experimental design principles43 and designed a Model Card Intervention Study. We
conducted an intervention study by adding detailed model cards to 42 popular models which has no or sparse model cards
previously to evaluate the impact of model cards (Fig. 4a). A Hugging Face employee with AI research background (one of the
paper authors) wrote these model cards. The 42 models are sampled from model repositories that are (1) ranked top 5,000 based
on cumulative downloads; (2) created in 2021 or 2022; and (3) had no model card or sparse model cards (≤100 words). It took
on average 40 mins to create each detailed model card, which contains an average of 596.5 words. To ensure that the results
are consistent across time, we upload the model card in two batches. The first batch (N = 26) are uploaded within the week
of 2022-11-07, and the second batch (N = 16) are uploaded within the week of 2022-11-14. We then compared the average
weekly downloads three weeks before and three weeks after the intervention.
To control for shared temporal variation in downloads across models, we constructed a control group for both batches by
randomly sampling N = 92 models from the model repositories using the same filtering conditions (i.e. these control models
also have no or similarly sparse model cards and have similar creation times and downloads as the models in the experimental
group). To account for the unequal distribution of downloads across models, we normalize the weekly downloads for each
model by dividing the corresponding average downloads before treatment. We then applied a difference-in-difference analysis44
4/18

--- Page 5 ---

to summarize the effect of the intervention:
Yi,t = β0 +β1 ·1{i = Treatment}+β2 ·1{t = Post-intervention}+β3 ·{i = Treatment}1{t = Post-intervention}.
(1)
Here, Yi,t is the normalized downloads of a model in group i (treatment or control) and time t (pre- or post-intervention). In (1),
β2 and β2 +β3 quantify the relative changes in downloads for the control and treatment groups, respectively. Therefore, β3
(and the corresponding p-value for testing H0 : β3 = 0) quantifies the impact of adding model cards on the weekly downloads.
Fig. 4b shows the intervention results from the difference-in-difference analysis applied to Batches 1 and 2. For Batch 2,
the model downloads in the treatment group significantly increased compared to the control group (p-value: 0.01). The average
weekly downloads for the models in the treatment group increased by 29.0% (95% CI [10.6%, 47.5%]), while the control group
did not see a significant change in downloads (p-value: 0.30). The results for Batch 1 were less clear: the average changes in
downloads are 2.4% (95% CI [0.5%, 4.4%]) and 2.2% (95% CI [-1.5%, 5.9%]) for the control group and the treatment group,
respectively. The observed effects might be limited due to external factors; for instance, the post-intervention period for Batch 1
fell with the 2022 Thanksgiving holiday season, which could have biased the estimated effect size towards the null, as users
were less likely to download and use a model regardless of the model card quality. Additionally, the sample size used in the
study is relatively small and could contribute to the differences in the results between the two batches. Further research with
larger sample sizes and controlling for external factors may provide more conclusive insights into the relationship between
model card quality and model usage.
Discussion
In this paper, we present a comprehensive large-scale analysis on 32,111 AI model documentations on Hugging Face to
understand the extent to which the AI community has adopted and adapted model cards, the strengths and weaknesses of
current documentation efforts, as well as to evaluate their impact on model development and usage. Overall, our results indicate
a widespread uptake of model cards within the AI community: 44.2% of the models have a corresponding model card, and
these models account for a significant 90.5% of total download traffic. This substantial adoption underscores the community’s
recognition of the importance of model cards in facilitating model comprehension and application.
However, we discovered a significant dichotomy within the community’s documentation practice. While model cards
have been adopted on a broad scale, there’s a striking disparity in the attention given to different sections of these cards. A
majority of model cards incorporate a Training section, signifying a focus on model development. Conversely, sections detailing
Environmental Impact and Evaluation are notably sparse, found in only 2.0% and 15.4% of model cards respectively. This gap
extends to the Limitations section, which is only present in 17.4% of the model cards. The growing divergence in the attention
given to various sections, coupled with an increasing reluctance to address the limitations of models—both trends evidenced by
our data— not only obstructs users from making informed decisions about model selection and usage but also undermines
trust in these AI models. Our findings echo a recognized trend in the broader scientific community: the tendency to downplay
study limitations, emphasizing successes while often overshadowing potential weaknesses and negative outcomes34,35. Unlike
traditional scientific papers which undergo peer review, model cards have no such mechanism for ensuring balanced and
comprehensive documentation. This creates a unique challenge, indicating the need for novel solutions. Future work should
focus on shaping strategies and standards to foster transparency and completeness in model card documentation. This is
fundamental to building trust, advancing responsible AI use, and providing users with the critical information needed for
informed model selection and application45.
Furthermore, our topic modeling analysis of four key model card sections—Limitations, Uses, Evaluation, and Train-
ing—reveals an emerging consensus regarding the vital role of data within the AI pipeline. In Limitation sections, data
limitations and model limitations received nearly equal attention. In both Training and Evaluation sections, data emerges as a
central theme. This emphasis on data in model documentation echoes existing literature that underscores the importance of data
in AI model development. In practice, machine learning developers spend twice as much time on data as they do on the models
themselves39,40,46. Poor-quality data can significantly impact the performance, fairness, robustness, safety, and scalability of
AI systems10,47. Unfortunately, despite the criticality of data, it is widely acknowledged in the literature that data-related work
is often undervalued in AI research. Data work is frequently perceived as “operational”48 compared to the more celebrated task
of building novel models and algorithms. As a result, a data-centric focus is often lacking in current AI research. Recent calls
have been made by researchers to prioritize data-centric AI research2. Our results align with this trend and underscore the need
for a more data-centric approach. By embracing and emphasizing the importance of data, the AI community can enhance the
quality and reliability of models and foster advancements in responsible AI research.
In the model card intervention study, we experimentally examined the impact of detailed model cards on model usage.
While the observed effect, a moderate increase in model downloads, suggests a positive influence of enhanced model cards, the
findings should be interpreted with certain considerations. The timing of our post-intervention period for one batch coincided
5/18

--- Page 6 ---

with the 2022 Thanksgiving holiday season, which might have led to an underestimation of the actual effect size due to generally
reduced model activity. Furthermore, the sample size of 42 intervened models might have limited our statistical power to detect
smaller effects. Despite these potential limitations, this study presents an important first step in quantitatively understanding
the impact of model cards on model usage. In the broader context of open-source software documentation, previous studies
have demonstrated that the organization of repository homepages and README files can significantly influence a project’s
perception, sustainability, and popularity, and even impact audience members’ actions, such as joining the project49–52. Given
our preliminary results, we believe that it is worth pursuing more extensive, larger-scale randomized studies of model cards in
the future. This can shed light on the nuanced ways in which model cards influence not just model downloads, but also broader
aspects of model usage and their downstream impacts. The insights from such future work would be instrumental in guiding
best practices for model card design and implementation, to fully realize their potential in promoting transparency, usability,
and responsible AI practices.
Topics on how to create high-quality and responsible documentation should be incorporated into the AI curriculum5,53–56.
Table 1 presents a compilation of selected resources, including tools for generating model cards with graphical user interfaces,
educational materials, and example model cards. These resources can serve as valuable teaching aids for students and
practitioners alike. For example, green AI tools have been developed to automatically track model training CO2 emissions and
document the environmental impact31,32. Furthermore, the Hugging Face Model Cards Writing Tool simplifies the process of
creating model cards by providing a user-friendly graphical interface, allowing individuals and teams with diverse skill sets and
roles to collaborate effortlessly, even without coding or markdown knowledge. Documentation will be integral to the next stage
of AI development, especially as we translate models from research sandbox to real-world deployment. By providing these
resources, we aim to reduce barriers to entry and encourage the responsible deployment of AI models through transparent and
accurate documentation.
Correspondence
Correspondence should be addressed to J.Z. (email: jamesz@stanford.edu).
Competing interests
The authors declare no conflict of interest.
Acknowledgements
We thank D. McFarland and H. Fang for discussions. J.Z. is supported by the National Science Foundation (CCF 1763191 and
CAREER 1942926), the US National Institutes of Health (P30AG059307 and U01MH098953) and grants from the Silicon
Valley Foundation and the Chan-Zuckerberg Initiative.
References
1. Swanson, K., Wu, E., Zhang, A., Alizadeh, A. A. & Zou, J. From patterns to patients: Advances in clinical machine learning
for cancer diagnosis, prognosis, and treatment. Cell 186, 1772–1791, DOI: https://doi.org/10.1016/j.cell.2023.01.035
(2023).
2. Liang, W. et al. Advances, challenges and opportunities in creating data for trustworthy ai. Nat. Mach. Intell. 4, 669 – 677
(2022).
3. Arrieta, A. B. et al. Explainable artificial intelligence (xai): Concepts, taxonomies, opportunities and challenges toward
responsible ai. Inf. fusion 58, 82–115 (2020).
4. Molnar, C. Interpretable Machine Learning: A Guide for Making Black Box Models Explainable (Lulu. com, 2020).
5. Shen, H. et al. Value cards: An educational toolkit for teaching social impacts of machine learning through deliberation. In
Proceedings of the 2021 ACM conference on fairness, accountability, and transparency, 850–861 (2021).
6. Seifert, C., Scherzinger, S. & Wiese, L. Towards generating consumer labels for machine learning models. In 2019 IEEE
First International Conference on Cognitive Machine Intelligence (CogMI), 173–179 (IEEE, 2019).
7. Mitchell, M. et al. Model cards for model reporting. In Proceedings of the conference on fairness, accountability, and
transparency, 220–229 (2019).
8. Bender, E. M., Gebru, T., McMillan-Major, A. & Shmitchell, S. On the dangers of stochastic parrots: Can language models
be too big? In Proceedings of the 2021 ACM conference on fairness, accountability, and transparency, 610–623 (2021).
6/18

--- Page 7 ---

9. Arnold, M. et al. Factsheets: Increasing trust in ai services through supplier’s declarations of conformity. IBM J. Res. Dev.
63, 6–1 (2019).
10. Mehrabi, N., Morstatter, F., Saxena, N., Lerman, K. & Galstyan, A. A survey on bias and fairness in machine learning.
ACM Comput. Surv. (CSUR) 54, 1–35 (2021).
11. He, B. et al. Blinded, randomized trial of sonographer versus ai cardiac function assessment. Nature 1–5 (2023).
12. Ribeiro, M. T., Singh, S. & Guestrin, C. "why should i trust you?" explaining the predictions of any classifier. In
Proceedings of the 22nd ACM SIGKDD international conference on knowledge discovery and data mining, 1135–1144
(2016).
13. Raji, I. D. & Yang, J. About ml: Annotation and benchmarking on understanding and transparency of machine learning
lifecycles. arXiv preprint arXiv:1912.06166 (2019).
14. Diakopoulos, N. Accountability in algorithmic decision making. Commun. ACM 59, 56–62 (2016).
15. Selbst, A. & Powles, J. “meaningful information” and the right to explanation. In conference on fairness, accountability
and transparency, 48–48 (PMLR, 2018).
16. Kulesza, T., Burnett, M., Wong, W.-K. & Stumpf, S. Principles of explanatory debugging to personalize interactive machine
learning. In Proceedings of the 20th international conference on intelligent user interfaces, 126–137 (2015).
17. HuggingFace. Huggingface model card guidebook (2021). Accessed: 2023-05-07.
18. Holland, S., Hosny, A., Newman, S., Joseph, J. & Chmielinski, K. The dataset nutrition label: A framework to drive higher
data quality standards. arXiv preprint arXiv:1805.03677 (2018).
19. Gebru, T. et al. Datasheets for datasets. Commun. ACM 64, 86–92 (2021).
20. Conover, M. et al. Hello dolly: Democratizing the magic of chatgpt with open models. https://huggingface.co/databricks/
dolly-v1-6b (2023).
21. Chiang, W.-L. et al. Vicuna: An Open-Source Chatbot Impressing GPT-4 with 90% ChatGPT Quality (2023).
22. Bender, E. M. & Friedman, B. Data statements for natural language processing: Toward mitigating system bias and
enabling better science. Transactions Assoc. for Comput. Linguist. 6, 587–604 (2018).
23. Bender, E. M., Friedman, B. & McMillan-Major, A. A guide for writing data statements for natural language processing
(2021).
24. Pushkarna, M., Zaldivar, A. & Kjartansson, O. Data cards: Purposeful and transparent dataset documentation for responsible
ai. In 2022 ACM Conference on Fairness, Accountability, and Transparency, 1776–1826 (2022).
25. Brundage, M. et al. Toward trustworthy ai development: mechanisms for supporting verifiable claims. arXiv preprint
arXiv:2004.07213 (2020).
26. Jobin, A., Ienca, M. & Vayena, E. The global landscape of ai ethics guidelines. Nat. Mach. Intell. 1, 389–399 (2019).
27. Mackiewicz, R. E. Overview of iec 61850 and benefits. In 2006 IEEE Power Engineering Society General Meeting, 8–pp
(IEEE, 2006).
28. Taori, R. et al. Stanford alpaca: An instruction-following llama model. https://huggingface.co/models/tatsu-lab/alpaca
(2023).
29. Köpf, A. et al.
Openassistant conversations–democratizing large language model alignment.
arXiv preprint
arXiv:2304.07327 (2023).
30. HuggingFace. Trending models. https://huggingface.co/?trending=model (accessed 2023-04-12).
31. HuggingFace. Displaying carbon emissions for your model. https://huggingface.co/docs/hub/model-cards-co2 (accessed
2023-04-12).
32. HuggingFace. Autotrain. https://huggingface.co/autotrain (accessed 2023-04-12).
33. HuggingFace. Model card user studies. https://huggingface.co/docs/hub/model-cards-user-studies (accessed 2023-04-12).
34. Smith, J. J., Amershi, S., Barocas, S., Wallach, H. M. & Vaughan, J. W. Real ml: Recognizing, exploring, and articulating
limitations of machine learning research. 2022 ACM Conf. on Fairness, Accountability, Transpar. (2022).
35. Ioannidis, J. P. A. Limitations are not properly acknowledged in the scientific literature. J. clinical epidemiology 60 4,
324–9 (2007).
7/18

--- Page 8 ---

36. Daneshjou, R. et al. Disparities in dermatology ai performance on a diverse, curated clinical image set. Sci. advances 8,
eabq6147 (2022).
37. Liang, W. & Zou, J. Metashift: A dataset of datasets for evaluating contextual distribution shifts and training conflicts. In
International Conference on Learning Representations (2022).
38. Food and Drug Administration. Guidance for the study of drugs likely to be used in the elderly (1989).
39. Sambasivan, N. et al. “everyone wants to do the model work, not the data work”: Data cascades in high-stakes ai. In
proceedings of the 2021 CHI Conference on Human Factors in Computing Systems, 1–15 (2021).
40. Anaconda, Inc. State of Data Science 2020. https://www.anaconda.com/state-of-data-science-2020 (2020). [Online;
accessed May 22, 2023].
41. Wolf, T. et al. Transformers: State-of-the-art natural language processing. In Proceedings of the 2020 conference on
empirical methods in natural language processing: system demonstrations, 38–45 (2020).
42. McMillan-Major, A. et al. Reusable templates and guides for documenting datasets and models for natural language
processing and generation: A case study of the huggingface and gem data and model cards. arXiv preprint arXiv:2108.07374
(2021).
43. Campbell, D. T. Experimental and quasi-experimental designs for research in teaching. Handb. research on teaching
(1963).
44. Angrist, J. D. & Pischke, J.-S. Mostly harmless econometrics: An empiricist’s companion (Princeton university press,
2009).
45. Bernstein, M. S. et al. Ethics and society review: Ethics reflection as a precondition to research funding. Proc. Natl. Acad.
Sci. United States Am. 118 (2021).
46. Kaggle. 2019 kaggle ml & ds survey. https://www.kaggle.com/c/kagglesurvey-2019 (2019). (Accessed on 08/27/2020).
47. Halevy, A., Norvig, P. & Pereira, F. The unreasonable effectiveness of data. IEEE intelligent systems 24, 8–12 (2009).
48. Sculley, D. et al. Hidden technical debt in machine learning systems. Adv. neural information processing systems 28
(2015).
49. Qiu, H. S., Li, Y. L., Padala, S., Sarma, A. & Vasilescu, B. The signals that potential contributors look for when choosing
open-source projects. Proc. ACM on Human-Computer Interact. 3, 1–29 (2019).
50. Vasilescu, B. et al. Gender and tenure diversity in github teams. In Proceedings of the 33rd annual ACM conference on
human factors in computing systems, 3789–3798 (2015).
51. Begel, A., Bosch, J. & Storey, M.-A. Social networking meets software development: Perspectives from github, msdn,
stack exchange, and topcoder. IEEE software 30, 52–66 (2013).
52. Fan, Y., Xia, X., Lo, D., Hassan, A. E. & Li, S. What makes a popular academic ai repository? Empir. Softw. Eng. 26,
1–35 (2021).
53. Fiesler, C., Garrett, N. & Beard, N. What do we teach when we teach tech ethics? a syllabi analysis. In Proceedings of the
51st ACM technical symposium on computer science education, 289–295 (2020).
54. Reich, R., Sahami, M., Weinstein, J. M. & Cohen, H. Teaching computer ethics: A deeply multidisciplinary approach. In
Proceedings of the 51st ACM Technical Symposium on Computer Science Education, 296–302 (2020).
55. Bates, J. et al. Integrating fate/critical data studies into data science curricula: where are we going and how do we get
there? In Proceedings of the 2020 conference on fairness, accountability, and transparency, 425–435 (2020).
56. Leidig, P. M. & Cassel, L. Acm taskforce efforts on computing competencies for undergraduate data science curricula. In
Proceedings of the 2020 ACM Conference on Innovation and Technology in Computer Science Education, 519–520 (2020).
57. Chmielinski, K. S. et al. The dataset nutrition label (2nd gen): Leveraging context to mitigate harms in artificial intelligence.
arXiv preprint arXiv:2201.03954 (2022).
58. Hutchinson, B. et al. Towards accountability for machine learning datasets: Practices from software engineering and
infrastructure. In Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency, 560–575
(2021).
59. Zou, J. & Schiebinger, L. Design ai so that it’s fair. Nature 559, 324–326 (2018).
60. Regulation, P. Regulation (eu) 2016/679 of the european parliament and of the council. Regul. (eu) 679, 2016 (2016).
8/18

--- Page 9 ---

61. Goodman, B. & Flaxman, S. European union regulations on algorithmic decision-making and a “right to explanation”. AI
magazine 38, 50–57 (2017).
62. Grootendorst, M. Bertopic: Neural topic modeling with a class-based tf-idf procedure. arXiv preprint arXiv:2203.05794
(2022).
63. Devlin, J., Chang, M.-W., Lee, K. & Toutanova, K. Bert: Pre-training of deep bidirectional transformers for language
understanding. arXiv preprint arXiv:1810.04805 (2018).
64. Reimers, N. & Gurevych, I. Making monolingual sentence embeddings multilingual using knowledge distillation. In
Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (Association for Computational
Linguistics, 2020).
65. McInnes, L., Healy, J. & Melville, J. UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction.
ArXiv e-prints (2018). 1802.03426.
66. McInnes, L. & Healy, J. Accelerated hierarchical density based clustering. In Data Mining Workshops (ICDMW), 2017
IEEE International Conference on, 33–42 (IEEE, 2017).
9/18

--- Page 10 ---

Figure 1. Overview of 74,970 AI Models Hosted on Hugging Face. (a) Exponential Growth of Hugging Face Model
Repositories: Our analysis indicates a substantial increase in the number of models hosted on Hugging Face, exhibiting a
weekly growth rate of 3.16% and a doubling time of 22 weeks. As of October 1st, 2022, there are 74,970 AI model repositories
available on the platform. (b) Temporal Trends in Model Popularity: Examination of the top-5 trending AI model repositories
on Hugging Face reveals dynamic shifts in community focus towards various model types. Language understanding and text
generation models initially dominate, while image generative models gain prominence in later stages. (c) Model Card Adoption
and Download Traffic: Despite only 42.8% of model repositories (32,111 out of 74,970) featuring model cards, these models
account for an overwhelming 90.5% of total download traffic on the platform. Our analysis focuses on these 32,111 models for
further examination. (d) Model Card Illustration: An exemplary model card is displayed, showcasing the essential components
and information typically provided by a model card.
10/18

--- Page 11 ---

Figure 2. Section Analysis of Hugging Face Model Cards. (a) Low Filled-out Rates for Model Card Sections: This panel
presents the filled-out percentages for each section in 32,111 model cards, as well as the top 100 and top 1,000 model cards
ranked by downloads. Environmental Impact, Limitations, and Evaluation sections exhibit the lowest filled-out rates, while the
training section is most frequently filled out. (b) Highly Downloaded Models Have Longer Model Cards. Model cards in the
top tier, ranked by downloads, are notably longer, suggesting a positive correlation between model card length and their usage.
The total word count across all the sections is shown on the y-axis. (c) Disparate Community Attention Patterns Across Model
Card Sections: The Environmental Impact section demonstrates both a low filled-out rate among the top 1,000 model cards and
a low average word count, indicating low community attention. Conversely, the Training section exhibits high filled-out rates
and average word counts, signifying more community attention.
11/18

--- Page 12 ---

Figure 3. Uncovering Key Themes in Model Card Sections through Topic Modeling Analysis. This figure displays the
outcomes of our topic modeling assessment on the contents of the (a) Limitations Section, (b) Uses Section, (c) Evaluation
Section, and (d) Training Section of model cards. Each panel illustrates the human-assigned theme label, prevalence,
associated keywords, and representative sentences for each section. Prevalence reflects the frequency of sections containing
sentences mentioning a specific theme, and top 100 prevalence is the prevalance measured on only the top 100 model cards.
The keywords and representative sentences were algorithmically determined. Theme labels were manually assigned based on
the grouping of topic modeling sentence clusters. Our section content analysis identifies practitioners’ priorities within each
section, highlighting the community’s focus on discussing data, sometimes with equal or even greater emphasis than the model
itself.
12/18

--- Page 13 ---

Treatment Group 
(Intervention by 
Adding Model Cards)
Batch 1 
(Submitted: 2022-11-07)
Batch 2 
(Submitted: 2022-11-14)
(N=26)
(N=92)
(N=16)
 Control Group 
(Not Adding 
Model Cards)
(a)
(b)
Figure 4. Model Card Intervention Study. (a) Experimental design: A schematic representation of the Model Card
Intervention Study, delineating the selection of models, division into treatment (two batches) and control groups, and model
card intervention process. (b) Outcome: Box plots displaying the percentage change in average weekly downloads for the
treatment and control groups in Batches 1 and 2. For each color-filled box, three horizontal lines correspond to the 25th, 50th,
and 75th percentiles; the upper (lower) whiskers extend from the 75th (25th) percentiles to the largest (smallest) value no
further than 1.5 × interquartile range. Statistical significance (p-values) is indicated for each batch. Overall, our analysis
revealed a moderate effect of model cards on model downloads.
13/18

--- Page 14 ---

Resource type Name
URL/Reference
Description
Model Card 
Generation 
Tools
HuggingFace Model Cards 
Writing Tool
https://huggingface.co/spaces/huggingface/Model
_Cards_Writing_Tool
Web application for creating model cards 
on HuggingFace from scratch
US Census Bureau Model 
Card Generator
https://bias.xd.gov/resources/model-card-generat
or/
Python-based tool for increasing 
transparency in government machine 
learning workﬂows
VerifyML Model Card 
Generation Web Tool
https://www.verifyml.com/
Web application for editing and comparing 
model cards online
TensorFlow Model Card 
Toolkit
https://pypi.org/project/model-card-toolkit/
Python library for automating model card 
generation.
Parl.AI Auto Generation Tool
https://parl.ai/docs/tutorial_model_cards.html
Open-source tool for documenting 
conversational AI research
ChatGPT
https://chat.openai.com/
AI text generation for brainstorming 
limitations
Salesforce Model Card 
Creation Toolkit
https://help.salesforce.com/s/articleView?id=releas
e-notes.rn_bi_edd_model_card.htm&release=232&
type=5
Tool for generating model cards on 
SalesForce platform
HuggingFace 
Community 
Resources
HuggingFace Model Card 
Guidebook
https://huggingface.co/docs/hub/model-cards
Community guidelines on the structure of 
model cards
The landscape of ML 
documentation tools
https://huggingface.co/docs/hub/model-card-land
scape-analysis
Links to recent research on ML 
documentation
Displaying carbon emissions 
for your model
https://huggingface.co/docs/hub/model-cards-co2 Guide on tracking and reporting CO2 
emissions
Education 
Resources
ABOUT ML Resources 
Library
https://partnershiponai.org/about-ml-resources-libr
ary/
Multistakeholder initiative to operationalize 
ML transparency through documentation
Code.org ML Lesson 8: 
Model Cards
https://studio.code.org/s/aiml-2022/lessons/8/
Teaching materials on model cards
Intro to AI Ethics Lession 5: 
Model Cards
https://www.kaggle.com/learn/intro-to-ai-ethics
Lesson on writing model cards
The HuggingFace Course
https://huggingface.co/course/
Course on creating model cards to 
HuggingFace
Example Model 
Cards
Model Card for RoBERTa 
Large OpenAI Detector
https://huggingface.co/roberta-large-openai-detect
or
Example model card for a ﬁne-tuned 
RoBERTa model on HuggingFace
Model Card for Pespective 
API
https://developers.perspectiveapi.com/s/about-the
-api-model-cards
Example model card for a conversation 
moderation AI model
Model Cards with Google
https://modelcards.withgoogle.com/model-reports Curated list of example Google model 
cards
Table 1. Selected resources for promoting responsible and informative model card creation.
14/18

--- Page 15 ---

Materials and Methods
Model Cards as AI Documentation Framework
A plethora of documentation tools have been proposed to address different aspects of AI systems, with early efforts focused
on data and later expanding to capture the AI development lifecycle more comprehensively. Data-focused documentation
tools22–24, including datasheets for datasets19 and data nutrition labels18,57, serve as a vehicle for communication between
dataset creators and consumers, addressing the lack of industry standards for documenting AI datasets. These tools document
the contexts and contents of datasets, including their motivation, composition, collection process, and recommended uses,
facilitating greater transparency, accountability, and reproducibility of AI results while mitigating unwanted biases in AI models.
They also enable dataset creators to be intentional throughout the dataset creation process. Datasheets and other forms of data
documentation are increasingly released along with datasets, helping researchers and practitioners to choose the right dataset
for their needs. These tools emphasize the data lifecycle58, encompassing aspects like assembly, collection, and annotation.
Later, efforts expanded to capture the AI development lifecycle more comprehensively, emphasizing the importance of an
iterative design process to ensure accessibility to users with diverse backgrounds and goals when interacting with model cards –
including developers, students, policymakers, ethicists, those impacted by AI models, and other stakeholders. Model cards7 and
FactSheets9 serve as reporting tools for trained AI models, documenting evaluation, usage, and other relevant aspects. Model
cards foster transparency, accountability, comparability, and user confidence, which are essential for responsible development
and deployment of AI models12–16,59. Furthermore, model cards also have the potential to assist in regulatory compliance by
offering a structured framework for documenting and communicating key information about a model’s performance, training,
and evaluation process6,9,60,61. Value cards5 educate students and practitioners about values related to AI models, while
consumer labels for AI models6 help non-experts understand key concerns. Researcher are also exploring the design of
system cards for complex systems such as AI-based content ranking which often involves a pipeline of many AI models, and
discussing complicated issues including use policies, access controls, and monitoring for abuse. In the broader context of
open-source software documentation, previous studies have demonstrated that the organization of repository homepages and
README files can significantly influence a project’s perception and even impact audience members’ actions, such as joining
the project49,50. Well-structured READMEs have been linked to enhanced sustainability and popularity of projects51,52. These
insights underscore the necessity for comprehensive and user-friendly documentation to promote user trust, engagement, and
adoption of AI models and tools.
Accessing and Parsing Model Cards
We employed the Hugging Face’s library, huggingface_hub, for accessing the model cards on the Hugging Face Hub. The
hugging face_hub.list_models() API grants access to all models hosted on the Hub, which numbered 74,970 as of October 1st,
2022. Additionally, the library’s ModelCard module allows for the loading of existing cards from the hub. By examining the
CardData metadata of models, we can verify the presence of a model card, and employ huggingface_hub.ModelCards.load()
function to obtain the card associated with a given model.
Model cards are written in Markdown format and serve as the README file for the model repository. To extract plain
descriptive text for further analysis, we utilized the Python package mistune (https://mistune.readthedocs.io/
en/latest/) to parse the README file and remove features such as tables, codes, links, and images. The structure of
model cards plays a crucial role in conveying key information. Drawing from academic literature7 and Hugging Face’s official
guidelines, model cards typically include sections such as Training, Evaluation, Uses, Limitations, Environmental Impact,
Citation, and How to Start. An example model card, shown in Fig. 1d, demonstrates the essential components and information
provided by model cards.
However, due to the subjective and dynamic nature of section naming, sections that discuss the same topic may not have the
same title. For example, both the "Training Procedure" and "Training Results" sections may address aspects of the training.
To categorize sections with the same topic, we use a keyword-based detection method to identify similar topics. We define
categories based on Hugging Face Model Card template. We then applied keyword detection on both the section titles and
contents to categorize the sections. It is important to note that section detection could not be solely based on the section titles.
While some section titles, such as "Training Data," may contain keywords that allow direct categorization, other information
may be hidden within the section contents. For instance, in the "Model Trained Using AutoTrain" section, the topic being
discussed cannot be inferred from the section title alone, but the section contains information about the amount of CO2
generated by AutoTrain, which can be categorized as Environmental Impact. By utilizing keyword detection, we achieved a
coverage of categorized sections of 89.51%, which validates the reliability of our categorizing method.
Topic Modeling
We leverage a sentence-level topic modeling approach to identify the patterns and themes within the section. For each section,
we first employ NLP methods to split it into sentences and label the sentences with their original section, which constructs
15/18

--- Page 16 ---

a sentence-section map. Then we deploy BERTopic62(https://maartengr.github.io/BERTopic/) approach to
automatically cluster the themes. BERTopic is a topic modeling technique that utilizes BERT63 embeddings and class-based
TF-IDF (c-TF-IDF) to develop compact and coherent clusters, thereby enabling the generation of easily understandable topics
while preserving salient terms within the topic descriptions. It starts by converting the documents to numerical representations.
The sentences will be embedded using the default embedding model Sentence Transformer64 all-MiniLM-L6-v2. Then Uniform
Manifold Approximation and Projection65 (UMAP) is used to reduce the dimensionality of document embedding into something
easier for clustering. After reducing the embeddings, it starts clustering the data. For that, a density-based clustering technique,
Hierarchical Density-Based Spatial Clustering of Applications with Noise66 (HDBSCAN) is used to cluster the data. It can
find clusters of different shapes and has the nice feature of identifying outliers where possible. When using HDBSCAN to do
clustering, the bag-of-words representation is used on the cluster level for the purpose of topic representation, in which the
frequency of each cluster can be found. That is, all documents in a cluster can be combined into a single document, and we can
count how often each word appears in each cluster. From the generated bag-of-words representations, c-TF-IDF is used to
extract the most important words per cluster.
Wx,c = ∥tfx,c∥×log

1+ A
fx

,
where Wx,c is the c-TF-IDF score of word x in class c, tfx,c is the frequency of word x in class c, fx is the frequency of word
x accross all classes, and A is the average number of words per class. Then the words are sorted based on their c-TF-IDF score,
and the keywords are the top words. The representative sentences are selected randomly in each cluster.
By employing this, we have got the automatically clustered topics generated from BERTopic with their keywords
and representative sentences. However, the clustered topics are too fine-grid, and we identify some topics that are ac-
ceptable to be merged. For example, in the training section, topic 2_used_dataset_containing_commoncrawl and topic
4_bookcorpus_books_11038_tables are both about the training data. Although we can fine-tune the parameters of BERTopic
to get better results, the fine-tuning process could be time-consuming and might miss some important patterns. Therefore, we
manually identify similar clustered topics based on the keywords and representative sentences, and use BERTopic to merge
them and get the new keywords and representative sentences.
Finally, we use the sentence-section map constructed previously and map the sentences to sections, and calculate the size of
sections within each topic. This allows us to identify the most prominent themes in each section and the size of each theme
relative to the section.
Code and Data Availability
The analysis code and the set of 42 model cards created in this study are publicly available on GitHub https://github.
com/Weixin-Liang/AI-model-card-analysis-HuggingFace. The Hugging Face model cards data can be
accessed through the Hugging Face Hub API at https://huggingface.co/docs/huggingface_hub/package_
reference/hf_api.
16/18

--- Page 17 ---

Figure S1. In-depth Analysis of Section Word Counts in Model Cards. (a) Comparative Assessment of Average Section
Lengths in Model Cards Based on Word Count. This figure displays the average section length, measured in word count, among
completed sections for all model cards, the top 1000 model cards, and the top 100 model cards. Sections such as How to Start,
Training, and Limitations are substantially longer, while Citation, Evaluation, Environmental Impact, and Intended Uses are
relatively shorter. Interestingly, despite its lower completion rate, the Limitations section exhibits one of the highest average
word counts (161 words in the top 1000 model cards). (b-c) Disparate Community Attention Patterns Across Model Card
Sections, Analyzed for both the top 100 model cards (b) and all model cards (c). The Environmental Impact section
demonstrates both a low completion rate and a low average word count, indicating limited community attention. In contrast, the
Training section displays high completion rates and average word counts, signifying greater community engagement.
17/18

--- Page 18 ---

Table S1. Temporal trends in the completion rates of different model card sections. The table displays the results of a
linear regression analysis conducted to assess the changes in the fill rates of different sections of model cards over time, while
controlling for model categories (e.g., tabular and natural language processing). A significant trend is the swift increase in the
completion rate for the Training section, rising at 0.2% per week (p = 3.31E-244). In contrast, most other sections are
experiencing a decline in their completion rates (p < 0.001). An interesting exception to this pattern is the Environmental
Impact section, which demonstrates a rise in its completion rate (p = 4.64E-24).
Table S2. Highly Downloaded Models Have Longer Model Cards. Model cards in the top tier, ranked by downloads, are
notably longer, suggesting a positive correlation between model card length and their usage. The total word count across all the
sections is shown on the y-axis.
18/18
```
