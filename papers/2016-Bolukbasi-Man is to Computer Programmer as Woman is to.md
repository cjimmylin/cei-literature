---































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: UGFNILD5
type: conferencePaper
short_title: "Man is to Computer Programmer as Woman is to"
year: 2016
first_author: "[[Tolga Bolukbasi]]"
last_author: "[[Adam Kalai]]"
authors: "Tolga Bolukbasi; Kai-Wei Chang; James Zou; Venkatesh Saligrama; Adam Kalai"
doi: 10.48550/arXiv.1607.06520
url: "http://arxiv.org/abs/1607.06520"
external_pdf: "http://arxiv.org/pdf/1607.06520.pdf"
publication: "Proceedings of the 30th Conference on Neural Information Processing Systems (NIPS 2016)"
CONF-CC: "NeurIPS 2016"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "American, Bias & Fairness"
key_contribution: "The seminal paper identifying gender bias in word embeddings (e.g., 'Man is to Computer Programmer as Woman is to Homemaker') and proposing debiasing algorithms."
significance: "Founded the field of fairness in NLP embeddings, demonstrating that AI models inherit and amplify societal stereotypes from training data and offering the first mathematical fixes."
tags: 
pdf_extract: "PDF Extracts/2016/2016-Bolukbasi-Man is to Computer Programmer as Woman is to.md"
local_pdf: "[[PDFs/2016/2016-Bolukbasi-Man is to Computer Programmer as Woman is to.pdf]]"
abstract: "The blind application of machine learning runs the risk of amplifying biases present in data. Such a danger is facing us with word embedding, a popular framework to represent text data as vectors which has been used in many machine learning and natural language processing tasks. We show that even word embeddings trained on Google News articles exhibit female/male gender stereotypes to a disturbing extent."
paper_summary: "Abstract: The blind application of machine learning runs the risk of amplifying biases present in data. Such a danger is facing us with word embedding, a popular framework to represent text data as vectors whic | Overview: Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings Tolga Bolukbasi1, Kai-Wei Chang2, James Zou2, Venkatesh Saligrama1,2, Adam Kalai2 1Boston University, 8 Saint Mary's S | Conclusions: Word embeddings help us further our understanding of bias in language. We ﬁnd a single direction that largely captures gender, that helps us capture a"
DATE_ADDED: 20260208
LLM_assessed: NA
DATA_URL: "NA"
CONFERENCE: "NeurIPS 2016"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: No
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for bias and fairness"
data_metrics: "Not specified"
---
# Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings

## Metadata

**Authors:** Bolukbasi, Tolga; Chang, Kai-Wei; Zou, James; Saligrama, Venkatesh; Kalai, Adam

**Year:** 2016

**Type:** preprint

**DOI:** [10.48550/arXiv.1607.06520](https://doi.org/10.48550/arXiv.1607.06520)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2016/2016-Bolukbasi-Man is to Computer Programmer as Woman is to.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/1607.06520
- **DOI:** https://doi.org/10.48550/arXiv.1607.06520

## Abstract

The blind application of machine learning runs the risk of amplifying biases present in data. Such a danger is facing us with word embedding, a popular framework to represent text data as vectors which has been used in many machine learning and natural language processing tasks. We show that even word embeddings trained on Google News articles exhibit female/male gender stereotypes to a disturbing extent. This raises concerns because their widespread use, as we describe, often tends to amplify these biases. Geometrically, gender bias is ﬁrst shown to be captured by a direction in the word embedding. Second, gender neutral words are shown to be linearly separable from gender deﬁnition words in the word embedding. Using these properties, we provide a methodology for modifying an embedding to remove gender stereotypes, such as the association between between the words receptionist and female, while maintaining desired associations such as between the words queen and female. We deﬁne metrics to quantify both direct and indirect gender biases in embeddings, and develop algorithms to “debias” the embedding. Using crowd-worker evaluation as well as standard benchmarks, we empirically demonstrate that our algorithms signiﬁcantly reduce gender bias in embeddings while preserving the its useful properties such as the ability to cluster related concepts and to solve analogy tasks. The resulting embeddings can be used in applications without amplifying gender bias.

## Authors

[[Tolga Bolukbasi]], [[Kai-Wei Chang]], [[James Zou]], [[Venkatesh Saligrama]], [[Adam Kalai]]

## Data Description

This paper evaluates gender bias in word embeddings, primarily the Word2Vec embedding trained on Google News (w2vNEWS, 3 million words, 300 dimensions) and the GloVe web-crawl embedding. The authors quantify direct and indirect gender bias using geometric metrics, generate and evaluate analogies via Amazon Mechanical Turk crowd-workers (150 analogies rated by 10 workers each), and propose hard and soft debiasing algorithms. The evaluation uses standard embedding benchmarks (RG, WS, MSR-analogy) to confirm debiasing preserves embedding utility while reducing stereotypical associations.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language #Statistics---Machine-Learning

## Citation Info

3229 citations (Semantic Scholar/arXiv) [2025-08-27] 3219 citations (Semantic Scholar/arXiv) [2025-08-23]
