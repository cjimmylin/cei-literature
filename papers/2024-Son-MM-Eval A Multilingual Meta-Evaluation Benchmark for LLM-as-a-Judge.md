---


































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0444
type: preprint
short_title: "MM-Eval: A Multilingual Meta-Evaluation Benchmark for LLM-as-a-Judge and Reward Models"
year: 2024
first_author: "[[Son, Guijin]]"
last_author: "[[Kim, Seungone]]"
authors: "Son, Guijin; Yoon, Dongkeun; Suk, Juyoung; Aula-Blasco, Javier; Aslan, Mano; Kim, Vu Trong; Islam, Shayekh Bin; Prats-Cristià, Jaume; Tormo-Bañuelos, Lucía; Kim, Seungone"
authors_incomplete: false
url: "https://arxiv.org/abs/2410.17578"
external_pdf: "https://arxiv.org/pdf/2410.17578.pdf"
publication: arXiv
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2024/2024-Son-MM-Eval A Multilingual Meta-Evaluation Benchmark for LLM-as-a-Judge.md"
local_pdf: "[[PDFs/2024/2024-Son-MM-Eval A Multilingual Meta-Evaluation Benchmark for LLM-as-a-Judge.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "Multicultural/Cross-cultural"
cultures_nationalities_list: "Multicultural/Cross-cultural"
languages_list: "Multilingual"
religious_values: "Islam"
rv_islam: 50
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
religious_values_list: "Islam"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: 
LLM_assessed: "GPT-3.5, GPT-4, GPT-4o, GPT-4o mini, Llama-3, Qwen-2"
DATA_URL: "https://github.com/guijinSON/MM-Eval"
tags: 
abstract: "As Large Language Models (LLMs) are now capable of producing fluent and coherent content in languages other than English, it is not imperative to precisely evaluate these non-English outputs. However, when assessing the outputs from mutlilingual LLMs, prior works often employed LLM based evaluators that excel at assessing English outputs, without a thorough examination of whether these evaluators could effectively assess non-English text as well."
CONFERENCE: "Preprint"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: Yes
data_description: "Multilingual benchmark for ai safety"
data_metrics: "18 languages"
---
# MM-Eval: A Multilingual Meta-Evaluation Benchmark for LLM-as-a-Judge and Reward Models

## Authors

[[Son, Guijin]], [[Yoon, Dongkeun]], [[Suk, Juyoung]], [[Aula-Blasco, Javier]], [[Aslan, Mano]], [[Kim, Vu Trong]], [[Shayekh Bin Islam|Islam, Shayekh Bin]], [[Prats-Cristià, Jaume]], [[Tormo-Bañuelos, Lucía]], [[Kim, Seungone]]

## Metadata

**Authors:** Son, Guijin; Yoon, Dongkeun; Suk, Juyoung; Aula-Blasco, Javier; Aslan, Mano; Kim, Vu Trong; Islam, Shayekh Bin; Prats-Cristià, Jaume; Tormo-Bañuelos, Lucía; Kim, Seungone

**Year:** 2024

**Type:** preprint

**Venue:** arXiv

**Languages:** 122 languages for consistency, 18 languages including French

**Benchmark:** MM-Eval

## Links

- **arXiv:** https://arxiv.org/abs/2410.17578
- **Code/Data:** https://github.com/guijinSON/MM-Eval

## Abstract

Multilingual meta-evaluation benchmark with five core subsets (Chat, Reasoning, Safety, Language Hallucination, Linguistics) spanning 18 languages. Models achieve only 68.9% average accuracy (50% = random). Safety subset performance in low-resource languages is 18.4% lower than English.

## Summary

This paper introduces MM-Eval, a multilingual meta-evaluation benchmark designed to assess whether LLM-based evaluators (LLM-as-a-Judge and reward models) can reliably evaluate non-English outputs from multilingual LLMs. Unlike existing English-centric meta-evaluation benchmarks, MM-Eval is constructed with multilingual-specific challenges in mind, comprising five core subsets (Chat, Reasoning, Safety, Language Hallucination, Linguistics) covering 18 languages plus a Language Consistency subset spanning 122 languages. The benchmark evaluates both ranking accuracy (pairwise comparisons) and consistency/fairness of absolute scores across languages using a novel Language Consistency Index (LCI) metric. Results from evaluating 12 evaluator LLMs show considerable room for improvement (68.9% average accuracy vs. 50% random baseline), with safety evaluation performance in low-resource languages degrading by 18.4% compared to English, revealing unfairness and inconsistency in cross-lingual evaluation.

## Data Description

MM-EVAL: a multilingual meta-evaluation benchmark spanning 18 languages (plus 122-language consistency subset) with five core subsets (Chat, Reasoning, Safety, Language Hallucination, Linguistics) for evaluating LLM-as-a-Judge and reward model capabilities in non-English settings.


## Detailed Summary

This paper introduces MM-Eval, a multilingual meta-evaluation benchmark that assesses whether LLM-based evaluators can reliably judge non-English outputs from multilingual LLMs. The benchmark addresses a critical gap: existing meta-evaluation benchmarks are English-centric, yet evaluator LLMs are widely used to assess multilingual outputs without verification of their cross-lingual reliability. MM-Eval is distinguished by its multilingual-first design philosophy, constructing challenges unique to multilingual settings rather than merely translating English benchmarks. It comprises five core subsets (Chat, Reasoning, Safety, Language Hallucination, Linguistics) covering 18 languages, plus a Language Consistency subset spanning 122 languages. A novel metric, the Language Consistency Index (LCI), quantifies how uniformly evaluators score parallel inputs across languages, measuring fairness and consistency beyond simple ranking accuracy.

## Paper Outline

1. Introduction - Gap in multilingual meta-evaluation
2. Preliminary - Role of evaluator LLMs in alignment
3. MM-Eval Benchmark - Five core subsets and Language Consistency subset design
4. Experimental Setup - 12 evaluator LLMs (open reward models, open judges, proprietary)
5. Results - Performance across subsets and languages
6. Validation - Correlation with Best-of-N rankings
7. Conclusion

## Methods Summary

MM-Eval uses controlled translation rather than full machine translation to avoid translationese artifacts. The five core subsets evaluate different capabilities: Chat (general instruction following), Reasoning (logical and mathematical), Safety (harmful content detection), Language Hallucination (detecting when models respond in the wrong language), and Linguistics (language-specific grammatical and morphological challenges). The Language Consistency subset presents parallel inputs across 122 languages to test whether evaluators assign consistent scores regardless of language. Evaluation uses both pairwise accuracy (standard meta-evaluation) and the novel LCI metric. The benchmark is validated by measuring correlation with Best-of-N rankings, finding significantly stronger correlation compared to English-only and machine-translated benchmarks.

## Results Summary

Across 12 evaluator LLMs (including GPT-4o, Claude models, and open-weight judges), the overall average accuracy is only 68.9% on core subsets (where random guessing yields 50%). Performance on the Safety subset degrades by 18.4% for low-resource languages compared to English. On the Linguistics subset, performance differences between high-resource and low-resource languages are significant. The Language Consistency analysis reveals that evaluators are unfair and inconsistent for lower-resourced languages, systematically assigning lower scores to good responses and higher scores to bad ones. MM-Eval shows statistically significant positive correlation with Best-of-N performance rankings, while English-only meta-evaluation benchmarks fail to show such alignment for multilingual evaluation.

## Conclusions

Strong evaluation performance in English does not readily transfer to non-English languages. Developing robust multilingual evaluator LLMs requires addressing fairness and consistency across languages, beyond simply capturing human preferences in English. The authors warn against assuming that English evaluation capabilities naturally generalize and release MM-Eval to serve as a foundation for building better multilingual evaluators.

## Artifact Contributions

- **MM-Eval benchmark**: Six subsets covering 18+122 languages with multilingual-specific challenges
- **Language Consistency Index (LCI)**: Novel metric for measuring cross-lingual evaluation fairness
- **Code and benchmark**: https://github.com/guijinSON/MM-Eval
- **Empirical evaluation**: Results for 12 evaluator LLMs across all subsets

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Evaluates LLM-as-a-Judge reliability for safety assessment in French. Shows significant degradation in non-English safety evaluation accuracy.

## Tags

