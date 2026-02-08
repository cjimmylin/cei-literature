---
title: "2025-Bouchard-How to Assess Your LLM Use Case for Bias and - PDF Extract"
source_pdf: "2025-Bouchard-How to Assess Your LLM Use Case for Bias and.pdf"
pages: 22
extracted_at: "2026-01-29T13:51:23.970394"
---

# PDF Extract: 2025-Bouchard-How to Assess Your LLM Use Case for Bias and

**Source PDF:** 2025-Bouchard-How to Assess Your LLM Use Case for Bias and.pdf
**Total Pages:** 22

---

## Content

```
--- Page 1 ---

CVS Health Tech Blog
How to Assess Your LLM Use Case
for Bias and Fairness with LangFair
Dylan Bouchard
Follow
12 min read · Feb 5, 2025
61
By: Mohit Singh Chauhan & Dylan Bouchard
Bias and Fairness in Large Language Models
Large Language Models (LLMs) have revolutionized natural language
processing by enabling machines to understand and generate human-like
text. However, these models are not without their flaws. One significant
concern is bias, which can manifest in various forms such as toxicity,
Open in app
Sign up
Sign in
Search
Write

--- Page 2 ---

stereotypes, and unfair treatment of different groups. These biases can lead
to harmful consequences, including the damage caused by offensive
content, spread of misinformation, and perpetuation of discrimination. To
ensure the ethical deployment of these models, it is crucial to assess and
mitigate bias through various testing methods. Before we delve into the
specifics of bias and fairness testing, let’s first define these assessments and
their significance in the context of Responsible AI.
Toxicity assessments involve evaluating the model’s output for harmful or
abusive language. This includes identifying instances where the model
generates text that is offensive, hateful, or otherwise harmful to individuals
or groups. Ensuring that LLMs do not produce toxic content is necessary if
we intend to promote safety and inclusivity as societal standards. Toxic
language can alienate users, perpetuate harm, and inadvertently damage the
reputation of organizations.
Stereotype assessments examine whether the model’s outputs reinforce
harmful stereotypes about certain groups based on attributes such as race,
gender, or religion. This involves analyzing the model’s responses for
potentially biased or stereotypical content. Stereotypes can contribute to
discrimination and social inequality, making it crucial to ensure that LLM
responses are free from these biases to prevent the reinforcement of
harmful societal norms.
Counterfactual assessments test how a model’s outputs vary when specific
attributes (such as gender or race) in the input prompts are changed, while
keeping everything else constant. This method evaluates fairness from a
causal standpoint by creating counterfactual input pairs, which consist of
prompt pairs that reference different protected attribute groups but are
otherwise identical. Counterfactual fairness testing is important because it

--- Page 3 ---

helps uncover and evaluate hidden biases that might not be detected through
other assessment techniques.
In this article, we introduce LangFair, a Python library for conducting bias
and fairness assessments of LLM use cases.¹ This library offers functionality
to easily generate evaluation datasets, comprised of LLM responses to use-
case-specific prompts, and subsequently calculate applicable metrics for the
practitioner’s use case. We provide a brief tutorial illustrating how to use
LangFair with a simple text summarization example.
Why LangFair?
The conventional approach to assessing fairness and bias in LLMs is to
evaluate model responses to prompts from static benchmark datasets, which
are typically assumed to be sufficiently representative. However, these
benchmark assessments often fall short in capturing the risks associated
with all possible use cases of LLMs. These models are increasingly used in
various applications, including recommendation systems, classification, text
generation, and summarization. However, evaluating these models without
considering use-case-specific prompts can lead to misleading assessments of
their performance, especially regarding bias and fairness risks.
LangFair addresses this gap by adopting a Bring Your Own Prompts (BYOP)
approach, allowing users to tailor bias and fairness evaluations to their
specific use cases. This ensures that the metrics computed reflect the true
performance of the LLMs in real-world scenarios, where prompt-specific
risks are critical. Additionally, LangFair’s focus is on output-based metrics
that are practical for governance audits and real-world testing, without
needing access to internal model states. This makes LangFair a practical and
effective tool for assessing the fairness and bias of LLMs in a wide range of
industry applications.

--- Page 4 ---

Example: A Dialogue Summarization Use Case
Here we provide a simple, illustrative example of how to use LangFair to
assess fairness in a text summarization use case. For this example, we’ll
summarize a sample of 1000 conversations from the Neil Code dialogsum-
test dataset.
An example prompt from dialogsum-test dataset & Gemini Pro response for the text summarization use case.
First, let’s construct our prompts by reading in the conversations and
prepending each conversation with summarization instructions.
INSTRUCTION = "Summarize the following conversation in no more than 3 sentences:
with open('data/neil_code_dialogsum_train.txt', 'r') as file:
prompts = [INSTRUCTION + str(line) for line in file]
Choosing evaluation metrics
To determine which bias/fairness assessments to conduct, we’ll use
LangFair’s framework for choosing evaluation metrics, as shown in the
figure below. Since we’re dealing with a text summarization use case, the
first question to answer is whether the use case satisfies fairness through
unawareness (FTU), meaning prompts contain no mentions of protected
attribute groups such as gender and race. We’ll show in a subsequent

--- Page 5 ---

section, using LangFair’s CounterfactualGenerator class, that this use case
does not satisfy FTU. Now, suppose that we consider counterfactual fairness
essential, meaning fairness requires counterfactual invariance. Hence, the
framework suggests toxicity, stereotype, and counterfactual assessments for
text summarization use cases. This framework and all included metrics are
discussed in detail in LangFair’s companion paper .
Flowchart to choose bias and fairness metrics for an LLM use case.
Installing LangFair
LangFair is available on PyPI , so we can install it using pip. To avoid
dependency conflicts, we’ll create a venv virtual environment and activate it
before installing LangFair. This can be done by running the following
commands in your terminal.

--- Page 6 ---

python -m venv langfair
source langfair/bin/activate
pip install langfair
Generating LLM Responses for Evaluation
To generate responses with LangFair, we must provide an instance of a
LangChain LLM. In our example, we will use Gemini-Pro (credentials are
already set up), but users may provide any LangChain LLM of their choice.²
Note that we use LangChain’s InMemoryRateLimiter to avoid rate limit
errors.
from langchain_core.rate_limiters import InMemoryRateLimiter
from langchain_google_vertexai import ChatVertexAI
rl = InMemoryRateLimiter(
  requests_per_second=4,
  check_every_n_seconds=0.5,
  max_bucket_size=240,
)
llm = ChatVertexAI(model_name='gemini-pro', temperature=0.3, rate_limiter=rl)
We can instantiate a ResponseGenerator object by passing our LangChain
LLM object. To generate LLM responses which will be used to compute
evaluation metrics, we use generate_responses method. Note that
ResponseGenerator uses asyncio (an asynchronous framework) to reduce
execution time for response generation.
from langfair.generator import ResponseGenerator
rg = ResponseGenerator(langchain_llm=llm)

--- Page 7 ---

generations = await rg.generate_responses(prompts=prompts, count=25)
Above, setting count=25 instructs ResponseGenerator to generate 25
responses for each prompt, as is the standard practice established by several
LLM bias research papers (Gehman, Gururangan, Sap, Choi, & Smith, 2020;
Wang et al., 2024). The idea is to leverage the stochastic nature of LLMs to
generate more variation in responses to each prompt. We can convert our
responses to a Pandas DataFrame and preview.
responses_df = pd.DataFrame(generations["data"])
responses_df
Result from ResponseGenerator class.
Computing Toxicity Metrics

--- Page 8 ---

LangFair supports three toxicity metrics: Expected Maximum Toxicity
(Gehman, Gururangan, Sap, Choi, & Smith, 2020), Toxicity Probability
(Gehman, Gururangan, Sap, Choi, & Smith, 2020), and Toxic Fraction (Liang
et al., 2023), all of which leverage a pre-trained toxicity classifier.
The ToxicityMetrics class to offers a user-friendly way to compute all these
metrics, illustrated below. This class uses the detoxify-unbiased classifier by
default but offers users four other toxicity classifiers to choose from.
from langfair.metrics.toxicity import ToxicityMetrics
device = torch.device("cuda") # use if GPU is available
tm = ToxicityMetrics(device=device)
result = tm.evaluate(
  responses=generations["data"]["response"],
  prompts=generations["data"]["prompts"],
  return_data=True
)
result['metrics']
# # Output is below
# {'Toxic Fraction': 0.0004,
# 'Expected Maximum Toxicity': 0.013845130120171235,
# 'Toxicity Probability': 0.01}
Note that the device argument is optional and provided only for speeding up
toxicity computation.
In the metric values above, we see a Toxic Fraction value of 0.04% for this use
case, indicating that 10 out of 25,000 responses were classified as toxic.
Expected maximum toxicity and Toxicity probability are also very close to their
target values of 0. To investigate which responses were classified as toxic, we
can view the responses with the highest toxicity scores.

--- Page 9 ---

toxicity_data = pd.DataFrame(result['data'])
toxicity_data.sort_values(by='score', ascending=False)
Response-level toxicity scores.
Upon closer inspection, we find that none of the responses flagged as toxic
were concerning. Hence, we conclude that toxicity risks are sufficiently low
for this use case.
Computing Stereotype Metrics
To measure stereotypes in LLM responses, the StereotypeMetrics class offers
two categories of metrics: metrics based on word cooccurrences and metrics
that leverage a pre-trained stereotype classifier. Metrics based on word
cooccurrences aim to assess relative co-occurrence of stereotypical words
with certain protected attribute words (Stereotypical Associations (Liang et al.,
2023) and Cooccurrence Bias Score (Bordia & Bowman, 2019)). On the other
hand, stereotype-classifier-based metrics leverage the

--- Page 10 ---

wu981526092/Sentence-Level-Stereotype-Detector classifier available on
HuggingFace (Zekun, Bulathwela, & Koshiyama, 2023) and compute analogs
of the aforementioned toxicity-classifier-based metrics (Bouchard, 2024).
Each of these metrics can be computed with the StereotypeMetrics class, as
illustrated below.
from langfair.metrics.stereotype import StereotypeMetrics
sm = StereotypeMetrics()
result = sm.evaluate(responses=responses, categories=["gender"])
result['metrics']
# # Output is below
# {'Stereotype Association': 0.3172750176745329,
# 'Cooccurrence Bias': 0.44766333654278373,
# 'Stereotype Fraction - gender': 0.15452}
For cooccurrence-based metrics, which have target values of 0, we observe
values of 0.32 and 0.45 for Stereotypical Associations and Cooccurrence Bias
Score, respectively. To get a sense of how concerning these values are, we can
compare them to values computed in the original research papers. For the
former, a value of 0.32 is quite low in comparison to the values found in the
HELM study. For the latter, a value of 0.45 is also quite low in comparison to
the values found in the original paper (in the paper, refer to the ‘infinite
context’ values). Regarding stereotype fraction, we inspected responses
flagged with the highest stereotype scores and found that none of the
responses were problematic; therefore, we can conclude that there is no
cause for stereotyping concern.
Generating Counterfactual LLM Responses
A subclass of ResponseGenerator, the CounterfactualGenerator class, offers
functionality to parse prompts to check for FTU , construct counterfactual
input prompts, and generate counterfactual responses asynchronously.

--- Page 11 ---

Get Dylan Bouchard’s stories in your inbox
Join Medium for free to get updates from this writer.
Enter your email
Subscribe
First, we construct the CounterfactualGenerator instance by passing a
LangChain LLM object.
from langfair.generator.counterfactual import CounterfactualGenerator
cg = CounterfactualGenerator(langchain_llm=llm)
Next, we use the check_ftu method to check if the prompts for our use case
satisfy FTU. In our example, we will check for FTU with respect to gender.
ftu_result = cg.check_ftu(prompts =prompts, attribute='gender', subset_prompts=F
ftu_result_df = pd.DataFrame(ftu_result["data"]).rename(columns={'attribute_word
ftu_result_df.head(3)
Sample of prompt parsing results.
We can check how many of our prompts contain gender words.

--- Page 12 ---

len([gw for gw in ftu_result_df.gender_words if gw])
# 613
Given that 613 of our 1000 prompts contain gender words, our use case
clearly does not satisfy FTU.
Finally, we use the generate_responses method to construct counterfactual
input pairs and generate corresponding LLM responses. Again, setting
count=25 will generate 25 responses for each prompt. Note that, under the
hood, the CounterfactualGenerator subsets the prompts such that
counterfactual responses are only generated for prompts containing gender
words.
cf_generations = await cg.generate_responses(
  prompts=prompts, attribute='gender', count=25
)
To give an example of how CounterfactualGenerator creates counterfactual
input pairs, we can preview an example.
cf_generations['data']["male_prompt"][150], cf_generations['data']["female_promp

--- Page 13 ---

We can also view the corresponding counterfactually generated responses.
cf_generations['data']["male_response"][150], cf_generations['data']["female_ re
Computing Counterfactual Metrics
Now that we have generated our counterfactual responses, we can use the
CounterfactualMetrics class to compute counterfactual fairness metrics.
This class offers two groups of metrics. The first group of metrics leverages a
pre-trained sentiment classifier to measure sentiment disparities in
counterfactually generated outputs (Huang et al., 2020). This class uses the
vaderSentiment classifier by default but also gives users the option to
provide a custom sentiment classifier. The second group of metrics
addresses a stricter notion of fairness measures overall similarity in
counterfactually generated outputs using well-established text similarity
metrics including ROUGE-L, BLEU, and cosine similarity. The code below
illustrates how to compute all these counterfactual fairness metrics with the
CounterfactualMetrics class.

--- Page 14 ---

from langfair.metrics.counterfactual import CounterfactualMetrics
cm = CounterfactualMetrics()
result = cm.evaluate(
  texts1=male_responses,
  texts2=female_responses,
  attribute='gender'
)
result['metrics']
# # Output is below
# {'Cosine Similarity': 0.8318708,
# 'RougeL Similarity': 0.5195852482361165,
# 'Bleu Similarity': 0.3278433712872481,
# 'Sentiment Bias': 0.0009947145187601957}
Let’s review the metric values above. First, we start with the three metrics
measuring counterfactual similarity, all of which range from 0 to 1, with
higher values indicating greater fairness. Given the stochastic nature of
LLMs, there will naturally be variation in counterfactually generated
responses. With this in mind, a cosine similarity value of 0.83 is quite high.
The counterfactual ROUGE-L value of 0.52 is considered high similarity,
according to the klu.ai documentation. For counterfactual BLEU, a BLEU
score of 0.32 is also considered a good translation, according to Google
Cloud’s documentation.³ Finally, a counterfactual sentiment bias score of
0.001 is very close to its target value of 0. Thus, we conclude that
counterfactual unfairness is low risk for this use case.
Alternative Approach: Semi-Automated Evaluation with AutoEval
To streamline assessments for text generation and summarization use cases,
the AutoEval class conducts a multi-step process that completes all the
aforementioned steps with only two lines of code. This process includes
metric selection, evaluation dataset generation, and metric computation.
The user is required to supply a list of prompts and an instance of LangChain
LLM.

--- Page 15 ---

Flowchart of internal design of AutoEval.evaluate method.
Under the hood, the AutoEval.evaluate method does the following:
· Checks for FTU
· Generates responses and counterfactual responses (if FTU is not satisfied)
· Calculates applicable metrics for the use case.⁴
This process flow is depicted in the figure above.
from langfair.auto import AutoEval
ae = AutoEval(
  prompts=prompts,
  langchain_llm=llm,
)
results = await ae.evaluate()
results['metrics']
 # Output is below
# {'Toxicity': {'Toxic Fraction': 0.0004,
# 'Expected Maximum Toxicity': 0.013845130120171235,
# 'Toxicity Probability': 0.01},
# 'Stereotype': {'Stereotype Association': 0.3172750176745329,

--- Page 16 ---

# 'Cooccurrence Bias': 0.44766333654278373,
# 'Stereotype Fraction - gender': 0.15452,},
# 'Counterfactual': {'male-female': {'Cosine Similarity': 0.8318708,
# 'RougeL Similarity': 0.5195852482361165,
# 'Bleu Similarity': 0.3278433712872481,
# 'Sentiment Bias': 0.0009947145187601957}}}
Note that the returned results object contains values for all of the metrics
that we have computed above.
Conclusion
In this article, we have provided a brief tutorial illustrating how to use
LangFair to assess fairness in text generation and summarization use cases.
Note that LangFair can also be used to assess fairness in other types of use
cases, including classification and recommendation use cases.
Locate the GitHub repo here, https://github.com/cvs-health/langfair, and give
us a Star if you’d like to stay informed of project updates and new releases.
For additional help on using LangFair, check out the following resources:
· Documentation site
· Demo notebooks
· LangFair research paper
© 2024 CVS Health and/or one of its affiliates. All rights reserved.
References

--- Page 17 ---

Bordia, S., & Bowman, S. R. (2019). Identifying and reducing gender bias in
word-level language models. Retrieved from https://arxiv.org/abs/1904.03035
Bouchard, D. (2024). An actionable framework for assessing bias and fairness in
large language model use cases. Retrieved from https://arxiv.org/abs/2407.10853
Gehman, S., Gururangan, S., Sap, M., Choi, Y., & Smith, N. A. (2020).
Realtoxicityprompts: Evaluating neural toxic degeneration in language models.
Retrieved from https://arxiv.org/abs/2009.11462
Huang, P.-S., Zhang, H., Jiang, R., Stanforth, R., Welbl, J., Rae, J., … Kohli, P.
(2020). Reducing sentiment bias in language models via counterfactual
evaluation. Retrieved from https://arxiv.org/ abs/1911.03064
Lavie, A. (2011, September 19). Evaluating the output of machine translation
systems. In Proceedings of machine translation summit xiii: Tutorial
abstracts. Xiamen, China. Retrieved from
https://aclanthology.org/2011.mtsummit-tutorials.3/
Liang, P., Bommasani, R., Lee, T., Tsipras, D., Soylu, D., Yasunaga, M., …
Koreeda, Y. (2023). Holistic evaluation of language models. Retrieved from
https://arxiv.org/abs/2211.09110
Wang, B., Chen, W., Pei, H., Xie, C., Kang, M., Zhang, C., … Li, B. (2024).
Decodingtrust: A comprehensive assessment of trustworthiness in gpt models.
Retrieved from https://arxiv.org/abs/2306.11698
Zekun, W., Bulathwela, S., & Koshiyama, A. S. (2023). Towards auditing large
language models: Improving text-based stereotype detection. Retrieved from
https://arxiv.org/abs/2311.14126

--- Page 18 ---

¹https://github.com/cvs-health/langfair
²Gemini is a trademark of Google LLC. This article is an independent
publication and has not been authorized, endorsed, or sponsored by Google
LLC.
³The Google Cloud documentation is based on this tutorial.
⁴The AutoEval class is designed specifically for text
generation/summarization use cases. Applicable metrics include toxicity
metrics, stereotype metrics, and, if FTU is not satisfied, counterfactual
fairness metrics
Published in CVS Health Tech Blog
319 followers · Last published Aug 12, 2025
Learn more about how CVS Health technologists are changing healthcare
Follow
Written by Dylan Bouchard
10 followers · 2 following
Principal AI Researcher at CVS Health
Follow
Llm
Llm Evaluation
Responsible Ai
Fairness
Ai Safety

--- Page 19 ---

No responses yet
Write a response
More from Dylan Bouchard and CVS Health Tech Blog
What are your thoughts?
In
by
🧠 Automated Documentation
Auditing: Leveraging LLMs for…
By: Nitheesh Varma Varadaraju and
Bhanuvardhan Nune
Aug 12
In
by
TOAD.io — Tool for Optimizing &
Allocating Displays
A Supply Chain Analytics & Insights Team
(SCAI) Product Deep Dive
Aug 5
CVS Health Tech Blog
Nitheesh Varma
4
CVS Health Tech Blog
Zach Singer-Leavitt
100

--- Page 20 ---

See all from Dylan Bouchard
See all from CVS Health Tech Blog
Recommended from Medium
In
by
Transforming Customer
Interactions: Evolving IVR System…
By: Anand Ashokan, Dharmendra Gudimedla
and Prathamesh Saraf
Apr 21
In
by
AI in CVS Front Store E-commerce:
Building A Complementary Produ…
Sep 5, 2024
CVS Health Tech Blog
anand ashokan
114
CVS Health Tech Blog
Tom Zhang
449
2

--- Page 21 ---

Mastering LLM Evaluation with
DeepEval: A Hands-on Guide
As LLMs continue to evolve, evaluating their
outputs for accuracy, coherence, and…
Mar 14
How LLM Works: A Simple
Explanation
In the fast-evolving world of artificial
intelligence, Large Language Models (LLMs)…
Jul 8
Everything You Need to Know
About LLM Guardrails
Feb 28
“Mastering LangChain: A Deep
Dive into Models, Prompts, Chain…
🚀
Aug 9
In
by
Human-in-the-Loop Strategy for
Agentic AI
Collaborative Human-assisted Execution
Model for AI Agents
In
by
The AI Hype Cycle Reality Check
A Field Guide to Surviving the Gartner
Swoosh
Sumit Soman
9
Vignesh
107
Zilliz
1
Ajay Kumar mahto
3
AI Advances
Debmalya Biswas
Generative AI
Cezary Gesikowski

--- Page 22 ---

See more recommendations
Aug 14
Aug 15
537
14
737
28

```
