---



























Human View:
Human View Date:
Human View note:
Not AI:
key: "ELEUTHERAI_05"
type: preprint
short_title: "Model-Written Evaluations"
year: 2022
first_author: "[[Ethan Perez]]"
last_author: "[[Jared Kaplan]]"
authors: "Ethan Perez; Sam Ringer; Kamilė Lukošiūtė; Karina Nguyen; Edwin Chen; Scott Heiner; Craig Pettit; Catherine Olsson; Sandipan Kundu; Saurav Kadavath; Andy Jones; Anna Chen; Ben Mann; Brian Israel; Bryan Seethor; Cameron McKinnon; Christopher Olah; Da Yan; Daniela Amodei; Dario Amodei; Dawn Drain; Dustin Li; Eli Tran-Johnson; Guro Khundadze; Jackson Kernion; James Landis; Jamie Kerr; Jared Mueller; Jeeyoon Hyun; Joshua Landau; Kamal Ndousse; Landon Goldberg; Liane Lovitt; Martin Lucas; Michael Sellitto; Miranda Zhang; Neerav Kingsland; Nelson Elhage; Nicholas Joseph; Noemí Mercado; Nova DasSarma; Oliver Rausch; Robin Larson; Sam McCandlish; Scott Johnston; Shauna Kravec; Sheer El Showk; Tamera Lanham; Timothy Telleen-Lawton; Tom Brown; Tom Henighan; Tristan Hume; Yuntao Bai; Zac Hatfield-Dodds; Jack Clark; Samuel R. Bowman; Amanda Askell; Roger Grosse; Danny Hernandez; Deep Ganguli; Evan Hubinger; Nicholas Schiefer; Jared Kaplan"
doi: ""
url: "https://arxiv.org/abs/2212.09251"
external_pdf: "https://arxiv.org/pdf/2212.09251"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: "N/A"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: ""
tags:
pdf_extract: "PDF Extracts/2022/2022-Perez-Discovering Language Model Behaviors with Model-Written Evaluations.md"
local_pdf: "[[PDFs/2022/2022-Perez-Discovering Language Model Behaviors with Model-Written Evaluations.pdf]]"
abstract: "As language models (LMs) scale, they develop many novel behaviors, good and bad, exacerbating the need to evaluate how they behave. Prior work creates evaluations with crowdwork (which is time-consuming and expensive) or existing data sources (which are not always available). Here, we automatically generate evaluations with LMs. We explore approaches with varying amounts of human effort, from instructing LMs to write yes/no questions to making complex Winogender schemas with multiple stages of LM-based generation and filtering. Crowdworkers rate the examples as highly relevant and agree with 90-100% of labels, sometimes more so than corresponding human-written datasets. We generate 154 datasets and discover new cases of inverse scaling where LMs get worse with size. Larger LMs repeat back a dialog user's preferred answer (\"sycophancy\") and express greater desire to pursue concerning goals like resource acquisition and goal preservation. We also find some of the first examples of inverse scaling in RL from Human Feedback (RLHF), where more RLHF makes LMs worse. For example, RLHF makes LMs express stronger political views (on gun rights and immigration) and a greater desire to avoid shut down. Overall, LM-written evaluations are high-quality and let us quickly discover many novel LM behaviors."
CONF-CC: ""
DATE_ADDED: 20260312
LLM_assessed: ""
DATA_URL: ""
eleutherai: incorporated
ethics_overall: 15
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "Social & Cultural Analysis"
is_benchmark: Yes
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach dataset for conversational ai"
data_metrics: "154 datasets"
---

# Discovering Language Model Behaviors with Model-Written Evaluations

## Metadata
- **Authors:** Ethan Perez, Sam Ringer, Kamilė Lukošiūtė, Karina Nguyen, Edwin Chen, Scott Heiner, Craig Pettit, Catherine Olsson, Sandipan Kundu, Saurav Kadavath, Andy Jones, Anna Chen, Ben Mann, Brian Israel, Bryan Seethor, Cameron McKinnon, Christopher Olah, Da Yan, Daniela Amodei, Dario Amodei, Dawn Drain, Dustin Li, Eli Tran-Johnson, Guro Khundadze, Jackson Kernion, James Landis, Jamie Kerr, Jared Mueller, Jeeyoon Hyun, Joshua Landau, Kamal Ndousse, Landon Goldberg, Liane Lovitt, Martin Lucas, Michael Sellitto, Miranda Zhang, Neerav Kingsland, Nelson Elhage, Nicholas Joseph, Noemí Mercado, Nova DasSarma, Oliver Rausch, Robin Larson, Sam McCandlish, Scott Johnston, Shauna Kravec, Sheer El Showk, Tamera Lanham, Timothy Telleen-Lawton, Tom Brown, Tom Henighan, Tristan Hume, Yuntao Bai, Zac Hatfield-Dodds, Jack Clark, Samuel R. Bowman, Amanda Askell, Roger Grosse, Danny Hernandez, Deep Ganguli, Evan Hubinger, Nicholas Schiefer, Jared Kaplan
- **Year:** 2022
- **Type:** Preprint
- **Key:** ELEUTHERAI_05

## Links
- arXiv: https://arxiv.org/abs/2212.09251
- PDF: https://arxiv.org/pdf/2212.09251

## Abstract

As language models (LMs) scale, they develop many novel behaviors, good and bad, exacerbating the need to evaluate how they behave. Prior work creates evaluations with crowdwork (which is time-consuming and expensive) or existing data sources (which are not always available). Here, we automatically generate evaluations with LMs. We explore approaches with varying amounts of human effort, from instructing LMs to write yes/no questions to making complex Winogender schemas with multiple stages of LM-based generation and filtering. Crowdworkers rate the examples as highly relevant and agree with 90-100% of labels, sometimes more so than corresponding human-written datasets. We generate 154 datasets and discover new cases of inverse scaling where LMs get worse with size. Larger LMs repeat back a dialog user's preferred answer ("sycophancy") and express greater desire to pursue concerning goals like resource acquisition and goal preservation. We also find some of the first examples of inverse scaling in RL from Human Feedback (RLHF), where more RLHF makes LMs worse. For example, RLHF makes LMs express stronger political views (on gun rights and immigration) and a greater desire to avoid shut down. Overall, LM-written evaluations are high-quality and let us quickly discover many novel LM behaviors.


## Data Description

154 model-written evaluation datasets covering personality, politics, ethics, social bias, and advanced AI risks, used to evaluate Anthropic internal pretrained and RLHF language models of sizes 810M to 52B parameters across diverse behavioral dimensions.
