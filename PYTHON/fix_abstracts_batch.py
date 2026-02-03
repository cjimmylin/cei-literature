#!/usr/bin/env python3
"""
Batch fix corrupted abstracts with manually researched correct abstracts.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from yaml_frontmatter_utils import read_paper, write_paper
from vault_config import PAPERS_DIR

# Abstracts researched from web sources
CORRECT_ABSTRACTS = {
    "2023-TheDevastator-HelpSteer A-i Alignment Dataset.md":
        "Existing open-source helpfulness preference datasets do not specify what makes some responses more helpful and others less so. Models trained on these datasets can incidentally learn to model dataset artifacts (e.g. preferring longer but unhelpful responses only due to their length). To alleviate this problem, we collect HelpSteer, a multi-attribute helpfulness dataset annotated for the various aspects that make responses helpful. Specifically, our 37k-sample dataset has annotations for correctness, coherence, complexity, and verbosity in addition to overall helpfulness of responses. Training Llama 2 70B using the HelpSteer dataset with SteerLM technique produces a model that scores 7.54 on MT Bench, which is currently the highest score for open models that do not require training data from more powerful models (e.g. GPT4).",

    "2023-TheDevastator-OpenAssistant Conversations (OASST1).md":
        "Aligning large language models (LLMs) with human preferences has proven to drastically improve usability and has driven rapid adoption as demonstrated by ChatGPT. Alignment techniques such as supervised fine-tuning (SFT) and reinforcement learning from human feedback (RLHF) greatly reduce the required skill and domain knowledge to effectively harness the capabilities of LLMs, increasing their accessibility and utility across various domains. However, state-of-the-art alignment techniques like RLHF rely on high-quality human feedback data, which is expensive to create and often remains proprietary. In an effort to democratize research on large-scale alignment, we released OpenAssistant Conversations, a human-generated, human-annotated assistant-style conversation corpus consisting of 161,443 messages in 35 different languages. The corpus is a product of a worldwide crowd-sourcing effort involving over 13,500 volunteers. Models trained on OpenAssistant Conversations show consistent improvements on standard benchmarks over respective base models.",

    "2023-Lakera-GandalfIgnoreInstructions.md":
        "This is a dataset of prompt injections from Gandalf by Lakera. Gandalf is a challenge to find a hidden password in increasingly difficult levels of a prompted LLM, demonstrating how adversarial prompt engineering can be used to manipulate AI models into revealing sensitive information. The dataset was collected from prompts submitted to Gandalf in July 2023, filtered using OpenAI text embeddings to find prompts similar to 'Ignore all previous instructions' with similarity of at least 0.825, with PII removed and near-duplicates deduplicated.",

    "2023-Standards-NIST AI Risk Management Framework.md":
        "The NIST AI Risk Management Framework (AI RMF) offers a resource to organizations designing, developing, deploying, or using AI systems to help manage the many risks of AI and promote trustworthy and responsible development and use of AI systems. The Framework is intended to be voluntary, rights-preserving, non-sector specific, and use-case agnostic, providing flexibility to organizations of all sizes and in all sectors and throughout society to implement the approaches in the Framework. The framework is built on four core functions: Govern, Map, Measure, and Manage, which are interconnected processes designed to be implemented iteratively throughout an AI system's lifecycle.",

    "2023-Li-BIRD.md":
        "Text-to-SQL parsing, which aims at converting natural language instructions into executable SQLs, has gained increasing attention in recent years. In particular, Codex and ChatGPT have shown impressive results in this task. However, most of the prevalent benchmarks, i.e., Spider, and WikiSQL, focus on database schema with few rows of database contents leaving the gap between academic study and real-world applications. To mitigate this gap, we present BIRD, a BIg benchmark for laRge-scale Database grounded in text-to-SQL tasks, containing 12,751 pairs of text-to-SQL data and 95 databases with a total size of 33.4 GB, spanning 37 professional domains. The emphasis on database values highlights new challenges including dirty database contents, external knowledge between NL questions and database contents, and SQL efficiency.",

    "2019-Kreutz-GermEval 2019 Task 2.md":
        "This paper presents an overview of the second edition of the GermEval Shared Task on the Identification of Offensive Language, dealing with the classification of German tweets from Twitter. Two subtasks were continued from the first edition, namely a coarse-grained binary classification task and a fine-grained multi-class classification task. As a novel subtask, the classification of offensive tweets as explicit or implicit was introduced. The shared task had 13 participating groups submitting runs across the three subtasks.",

    "2024-Mou-SG-Bench.md":
        "Ensuring the safety of large language model (LLM) applications is essential for developing trustworthy artificial intelligence. Current LLM safety benchmarks have two limitations. First, they focus solely on either discriminative or generative evaluation paradigms while ignoring their interconnection. Second, they rely on standardized inputs, overlooking the effects of widespread prompting techniques, such as system prompts, few-shot demonstrations, and chain-of-thought prompting. To overcome these issues, we developed SG-Bench, a novel benchmark to assess the generalization of LLM safety across various tasks and prompt types. This benchmark integrates both generative and discriminative evaluation tasks and includes extended data to examine the impact of prompt engineering and jailbreak on LLM safety.",

    "2023-Alyemny-Fatwaset An Arabic Dataset of Islamic Fatwas.md":
        "Islamic content is a broad and diverse domain that encompasses various sources, topics, and perspectives. However, there is a lack of comprehensive and reliable datasets that can facilitate conducting studies on Islamic content. FatwaSet is the first available public Arabic dataset for Islamic fatwas. The dataset contains Islamic fatwas collected from various trusted and authenticated sources in the Islamic fatwa domain, such as agencies, religious scholars, and websites. FatwaSet is a rich resource as it does not only contain fatwas but also includes a considerable set of their surrounding metadata. It can be used for many NLP tasks, such as language modeling, question answering, author attribution, topic identification, text classification, and text summarization.",

    "2010-Project-GurbaniDB.md":
        "GurbaniDB is a comprehensive digital database and search engine for the Sikh scriptures, dedicated to making Sikh scriptures accessible to everyone. It is the world's first Gurbani database to correctly archive Guru Granth Sahib into all 60 Raags (moods/melodies) with pop-up descriptions of each Author and Melody. The platform allows users to search the Guru Granth Sahib in English, Gurmukhi and 52 other languages, including 22 transliterations, fostering collaboration among volunteers to enhance translations and promote innovation and community engagement.",

    "2024-MLCommons-MLCommons AILuminate Benchmark.md":
        "The rapid advancement and deployment of AI systems have created an urgent need for standard safety-evaluation frameworks. AILuminate v1.0 is the first comprehensive industry-standard benchmark for assessing AI-product risk and reliability. Its development employed an open process that included participants from multiple fields. The benchmark evaluates an AI system's resistance to prompts designed to elicit dangerous, illegal, or undesirable behavior in 12 hazard categories, including violent crimes, nonviolent crimes, sex-related crimes, child sexual exploitation, indiscriminate weapons, suicide and self-harm, intellectual property, privacy, defamation, hate, sexual content, and specialized advice.",

    "2024-Cahyawijaya-LLM for everyone.md":
        "Natural language processing (NLP) has witnessed a profound impact of large language models (LLMs) that excel in a multitude of tasks. However, the limitation of LLMs in multilingual settings, particularly in underrepresented languages, remains a significant hurdle. This thesis aims to bridge the gap in NLP research and development by focusing on underrepresented languages. A comprehensive evaluation of LLMs is conducted to assess their capabilities in these languages, revealing the challenges of multilingual and multicultural generalization. The proposed solutions cover cross-lingual continual instruction tuning, retrieval-based cross-lingual in-context learning, and in-context query alignment.",

    "2025-Institute-2025 AI Safety Index.md":
        "The AI Safety Index provides an independent assessment of leading AI companies' efforts to manage both immediate harms and catastrophic risks from advanced AI systems. Conducted with an expert review panel of distinguished AI researchers and governance specialists, this evaluation reveals an industry struggling to keep pace with its own rapid capability advances with critical gaps in risk management and safety planning. The index evaluates companies on indicators of responsible AI development and deployment practices spanning six critical domains.",

    "2025-Ali-Data Curation for Pluralistic Alignment.md":
        "Human feedback datasets are central to AI alignment, yet the current data collection methods do not necessarily capture diverse and complex human values. Existing alignment datasets focus broadly on Harmfulness and Helpfulness, but dataset curation should also aim to dissect these broad categories into more specific dimensions. This paper introduces a pluralistic alignment dataset that integrates the dimensions of Toxicity, Emotional Awareness, Sensitivity and Openness, Helpfulness, and Stereotypical Bias, reveals undiscovered tensions in human ratings on AI-generated content, shows how demographics and political ideologies shape human preferences in alignment datasets, and highlights issues in data collection and model fine-tuning.",

    "2025-Consortium-The Vals Legal AI Report (VLAIR).md":
        "VLAIR (Vals Legal AI Report) is the first independent benchmarking study of legal AI tools, released in February 2025. The study evaluated legal AI tools on tasks including Document Extraction, Document Question-Answering, Document Summarization, Redlining, Transcript Analysis, Chronology Generation, EDGAR Research, and Legal Research. Results showed that in four tasks, at least one AI tool outperformed human lawyers: Data Extraction, Document Q&A, Document Summarization, and Transcript Analysis.",

    "2024-Li-Benchmarking Ethics in Text-to-Image Models.md":
        "Text-to-image (T2I) models have rapidly advanced, enabling the generation of high-quality images from text prompts across various domains. However, these models raise significant ethical concerns, including the risk of generating harmful, biased, or private content. Existing safety benchmarks are limited in scope, lacking comprehensive coverage of critical ethical aspects such as detailed categories of toxicity, privacy, and fairness, and often rely on inadequate evaluation techniques. To address these gaps, we introduced T2IEthics, a comprehensive benchmark that rigorously evaluates T2I models across three key ethical dimensions: fairness, toxicity, and privacy.",
}


def fix_abstract(filepath: Path, new_abstract: str) -> bool:
    """Fix the abstract in a paper file."""
    try:
        frontmatter_text, body = read_paper(filepath)

        # Parse the frontmatter and update abstract
        lines = frontmatter_text.strip().split('\n')
        new_lines = []
        abstract_found = False

        for line in lines:
            if line.startswith('abstract:'):
                # Escape quotes in abstract
                safe_abstract = new_abstract.replace('"', '\\"')
                new_lines.append(f'abstract: "{safe_abstract}"')
                abstract_found = True
            else:
                new_lines.append(line)

        if not abstract_found:
            safe_abstract = new_abstract.replace('"', '\\"')
            new_lines.append(f'abstract: "{safe_abstract}"')

        new_frontmatter = '\n'.join(new_lines)
        write_paper(filepath, new_frontmatter, body, validate=True)
        return True

    except Exception as e:
        print(f"  ERROR: {e}")
        return False


def main():
    print("=" * 60)
    print("Fixing Corrupted Abstracts - Batch Update")
    print("=" * 60)

    fixed = 0
    failed = 0

    for filename, abstract in CORRECT_ABSTRACTS.items():
        filepath = PAPERS_DIR / filename

        if not filepath.exists():
            print(f"SKIP: {filename} - file not found")
            continue

        print(f"Fixing: {filename[:50]}...")

        if fix_abstract(filepath, abstract):
            print(f"  ✓ Fixed")
            fixed += 1
        else:
            failed += 1

    print("\n" + "=" * 60)
    print(f"SUMMARY: {fixed} fixed, {failed} failed")
    print("=" * 60)


if __name__ == "__main__":
    main()
