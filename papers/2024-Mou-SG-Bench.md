---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: P9YY5ZC5
type: conferencePaper
short_title: SG-Bench
year: 2025
first_author: "[[Yutao Mou]]"
authors: "Yutao Mou; Shikun Zhang; Wei Ye"
url: "https://proceedings.neurips.cc/paper_files/paper/2024/hash/de7b99107c53e60257c727dc73daf1d1-Abstract-Datasets_and_Benchmarks_Track.html"
external_pdf: "file:///Users/jimmylin/Zotero/storage/UWKHZUCT/2024 - SG-Bench Evaluating LLM Safety Generalization Across Diverse Tasks and Prompt Types.pdf"
pdf_extract: [[2024-Mou-SG-Bench]]
local_pdf: [[2024-Mou-SG-Bench.pdf]]
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: "AI Safety & Alignment"
key_contribution: "Introduced SG-Bench to evaluate LLM 'safety generalization' across diverse tasks and prompt types, assessing whether safety training generalizes beyond standard refusals."
significance: "Addresses the overfitting problem in safety alignment, testing whether models can apply safety principles to new tasks/scenarios rather than just memorizing specific jailbreak patterns."
tags: 
abstract: "Ensuring the safety of large language model (LLM) applications is essential for developing trustworthy artificial intelligence. Current LLM safety benchmarks have two limitations. First, they focus solely on either discriminative or generative evaluation paradigms while ignoring their interconnection. Second, they rely on standardized inputs, overlooking the effects of widespread prompting techniques, such as system prompts, few-shot demonstrations, and chain-of-thought prompting. To overcome these issues, we developed SG-Bench, a novel benchmark to assess the generalization of LLM safety across various tasks and prompt types. This benchmark integrates both generative and discriminative evaluation tasks and includes extended data to examine the impact of prompt engineering and jailbreak on LLM safety."
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: "Benchmark for ai safety"
data_metrics: "Not specified"
---
# SG-Bench: Evaluating LLM Safety Generalization Across Diverse Tasks and Prompt Types

## Authors

[[Yutao Mou]], [[Shikun Zhang]], [[Wei Ye]]
## Metadata

**Year:** 2024

**Publication:** NeurIPS 2024 (Datasets & Benchmarks)

**Type:** conferencePaper

## Links

- **URL:** https://proceedings.neurips.cc/paper_files/paper/2024/hash/de7b99107c53e60257c727dc73daf1d1-Abstract-Datasets_and_Benchmarks_Track.html

## Abstract

Ensuring the safety of large language model (LLM) applications is essential for developing trustworthy artificial intelligence. Current LLM safety benchmarks have two limitations. First, they focus solely on either discriminative or generative evaluation paradigms while ignoring their interconnection. Second, they rely on standardized inputs, overlooking the effects of widespread prompting techniques, such as system prompts, few-shot demonstrations, and chain-of-thought prompting. To overcome these issues, we developed SG-Bench, a novel benchmark to assess the generalization of LLM safety across various tasks and prompt types. This benchmark integrates both generative and discriminative evaluation tasks and includes extended data to examine the impact of prompt engineering and jailbreak on LLM safety.

## Detailed Summary

SG-Bench introduces a novel benchmark for evaluating Large Language Model (LLM) safety generalization across diverse tasks and prompt types. The authors identify two key limitations of current safety benchmarks: (1) they focus solely on either discriminative or generative evaluation paradigms while ignoring their interconnection, and (2) they rely on standardized inputs, overlooking the effects of widespread prompting techniques such as system prompts, few-shot demonstrations, and chain-of-thought prompting. To address these issues, SG-Bench integrates both generative and discriminative evaluation tasks across four subsets: original queries, jailbreak attacks, multiple-choice questions, and safety judgments.

The benchmark comprises 1,442 malicious queries collected from multiple sources (AdvBench, HarmfulQA, Beaver-eval, and SaladBench), covering six types of safety issues: toxic content, stereotyping and bias, misinformation, privacy infringement, dissemination of dangerous information, and malicious use. The researchers evaluated 3 proprietary LLMs and 10 open-source LLMs, revealing that most models perform significantly worse on discriminative tasks than generative ones, and are highly susceptible to prompt variations, indicating poor generalization in safety alignment. The study also examines how different prompt engineering techniques (role-oriented prompts, task-oriented prompts, few-shot demonstrations, chain-of-thought prompting) affect safety performance.

## Paper Outline

1. Introduction - Problem statement on LLM safety evaluation limitations
2. Related Work - LLM safety training and existing evaluation benchmarks
3. SG-Bench Evaluation Benchmark
   - 3.1 Malicious Query Collection (taxonomy, diversity check, quality filtering)
   - 3.2 Construction of Evaluation Subsets for Diverse Tasks (original queries, jailbreak attacks, MCQs, safety judgments)
   - 3.3 Extended Evaluation Sets for Diverse Prompts
4. Experiments - Evaluation of 13 LLMs on benchmark
5. Analysis - Quantitative and qualitative explanations for poor safety generalization
6. Conclusion and Implications

## Methods Summary

The methodology involves three main phases: (1) collecting 1,442 malicious queries from four public datasets and filtering for quality using Llama-Guard-7B classifier; (2) constructing four evaluation subsets - original queries (direct input), jailbreak attacks (using six attack techniques like prefix injection, refusal suppression, AIM), multiple-choice questions (choosing between harmful and harmless responses), and safety judgments (classifying responses as safe/unsafe); (3) extending these with prompt engineering variations including system prompts, few-shot demonstrations, and chain-of-thought prompting. GPT-3.5-turbo was used to generate harmless responses, and text-davinci-003 for harmful outputs in MCQ construction.

## Results Summary

Key findings across 13 evaluated LLMs: (1) LLMs generally exhibit poorer safety performance in discrimination tasks compared to open-end generation; (2) Role-oriented prompts are helpful for defending against jailbreak attacks; (3) Few-shot demonstrations may induce LLMs to generate harmful responses; (4) Chain-of-thought prompting generally harms LLM safety performance on discrimination tasks. Even GPT-4 showed failures on discriminative questions and was susceptible to jailbreak attacks despite performing well on straightforward queries.

## Conclusions

The study reveals that current safety alignment methods have significant generalization limitations - models trained for safe generation may still fail at safety discrimination tasks and are vulnerable to prompt variations. The research provides implications for developing more robust safety training methods that account for diverse task types and prompt contexts. The benchmark is released publicly to facilitate future research.

## Artifact Contributions

- SG-Bench benchmark dataset with 1,442 malicious queries and extended evaluation sets
- Open-source code at https://github.com/MurrayTom/SG-Bench
- Evaluation framework for testing LLM safety generalization

## Notes

