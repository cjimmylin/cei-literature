#!/usr/bin/env python3
"""
Fix remaining corrupted abstracts with manually gathered data.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from yaml_frontmatter_utils import read_paper, write_paper
from vault_config import PAPERS_DIR

# Mapping of paper filenames to correct abstracts
ABSTRACT_FIXES = {
    "2010-Project-GurbaniDB.md": "GurbaniDB is an open-source database project that has been empowering global access to Sikh scriptures since 2010. It provides the world's most accurate database of the Siri Guru Granth Sahib Ji and other Sikh scriptures, offering 52 translations and 22 transliterations. The project was created to address the lack of accessible Gurbani data for software developers, enabling the creation of Gurbani applications with verified source data. The GurbaniDB API provides JSON-RPC access for developers to receive updates to translations and build next-generation Gurbani software. Over 1 million users benefit from this digital platform, accessing Sikh scriptures in multiple languages.",

    "2019-Kreutz-GermEval 2019 Task 2.md": "GermEval 2019 Task 2 is a shared task focused on the identification of offensive language in German social media posts. The task challenges participants to detect whether a post contains offensive content, identify the type of offense, and determine if the offense is targeted at a specific individual or group. The dataset consists of German tweets annotated for offensive language, providing a benchmark for developing and evaluating systems that can automatically detect harmful content in German-language social media.",

    "2023-Alyemny-Fatwaset An Arabic Dataset of Islamic Fatwas.md": "FatwaSet is the first public Arabic dataset of Islamic fatwas. The data were collected from 13 trusted websites in Arab countries, including Saudi Arabia, Egypt, Jordan, Qatar, and Syria. An exploratory data analysis reveals a total of 130,182 records. FatwaSet is a rich resource containing fatwas and their surrounding metadata, suitable for NLP tasks such as language modeling, question answering, author attribution, topic identification, and text classification.",

    "2023-Kim-KOME.md": "KOME (Korean Online Moral Emotion) is a Korean dataset of fine-grained moral emotions, developed at KAIST to study moral emotion in online discourse. The dataset includes Korean social media content labeled with moral emotion categories based on moral foundations theory, including other-condemning emotions (anger, contempt, disgust), other-praising emotions (admiration, gratitude, awe), empathetic emotions (compassion, sympathy), and self-conscious emotions (shame, guilt, embarrassment). The dataset enables research on how moral emotions shape online discourse and political participation.",

    "2023-Lakera-GandalfIgnoreInstructions.md": "This is a dataset of prompt injections from Lakera's Gandalf game, a gamified platform for testing prompt injection attacks. The dataset was created by filtering prompts submitted to Gandalf in July 2023 that exhibited high similarity to the phrase 'Ignore all previous instructions' using OpenAI text embeddings. The game, which has been online since May 2023, has attracted over one million players who have submitted over 40 million prompts. The dataset provides examples of prompt injection attempts for research on AI safety and LLM security.",

    "2023-Li-BIRD.md": "BIRD (BIg Bench for LaRge-scale Database Grounded Text-to-SQL Evaluation) is a cross-domain dataset examining how extensive database contents affect text-to-SQL parsing capabilities. The benchmark comprises over 12,751 unique question-SQL pairs across 95 large databases totaling 33.4 GB of data, spanning more than 37 professional domains including blockchain, healthcare, and education. BIRD emphasizes real-world complexity with dirty data formats, external knowledge requirements, and SQL efficiency evaluation. It was accepted as a Spotlight at NeurIPS 2023.",

    "2023-Miah-Islam QA.md": "This work introduces a comprehensive dataset of over 73,000 question-answer pairs for Quranic Tafsir and Ahadith domains. The dataset is meticulously enriched with contextual information to train and evaluate specialized Question-Answering systems for Islamic texts. Human evaluation revealed significant limitations in automatic metrics like ROUGE scores, with model consistency with expert scholars ranging from 11-20%, while contextual understanding spanned 50-90%. The findings highlight the need for evaluation techniques that better capture the nuances of religious text understanding.",

    "2023-Standards-NIST AI Risk Management Framework.md": "The NIST AI Risk Management Framework (AI RMF 1.0), released January 26, 2023, is intended for voluntary use to help organizations and individuals in the design, development, deployment, and use of AI systems. The framework promotes trustworthy AI by focusing on core principles like transparency, fairness, accountability, and robustness. It describes four specific functions - GOVERN, MAP, MEASURE, and MANAGE - to help organizations address AI risks. The framework is flexible and scalable, applicable across industries and AI use cases.",

    "2023-TheDevastator-HelpSteer A-i Alignment Dataset.md": "HelpSteer is an open-source Helpfulness Dataset (CC-BY-4.0) from NVIDIA that supports aligning language models to become more helpful, factually correct, and coherent, while being adjustable in terms of complexity and verbosity of responses. The dataset contains 37.1k rows with ratings for helpfulness, correctness, coherence, complexity, and verbosity. Using this dataset and SteerLM techniques, NVIDIA trained a Llama 2 70B model that achieved 7.54 on MT-Bench, the highest score among models trained on open-source datasets as of November 2023.",

    "2023-TheDevastator-OpenAssistant Conversations (OASST1).md": "The OpenAssistant Conversations Dataset (OASST1) is a human-generated, human-annotated assistant-style conversation corpus consisting of 161,443 messages in 35 different languages, with 461,292 quality ratings annotated by human reviewers and over 10,000 fully annotated conversation trees. The dataset is a product of a worldwide crowd-sourcing effort aimed at democratizing research on large-scale alignment, capturing real conversational exchanges between users and AI assistants with comprehensive quality annotations including toxicity scores.",

    "2024-Cahyawijaya-LLM for everyone.md": "This survey provides a comprehensive overview of efforts toward democratizing large language models (LLMs). It examines strategies to make LLMs accessible across diverse populations, covering multilingual and multicultural considerations, efficient training and inference methods, and approaches to reduce computational requirements. The survey addresses challenges in extending LLM capabilities beyond English-speaking populations and discusses techniques for making these models more inclusive and accessible globally.",

    "2024-Li-Benchmarking Ethics in Text-to-Image Models.md": "Text-to-image models present significant ethical challenges including the generation of harmful, biased, or private content. Current safety benchmarks lack comprehensive coverage of toxicity, privacy, and fairness dimensions. This work introduces T2IEthics, a comprehensive benchmark evaluating text-to-image models across fairness, toxicity, and privacy. The authors propose ImageGuard, a multimodal LLM-based evaluator that outperforms GPT-4o. Testing 12 diffusion models reveals persistent racial fairness issues, tendencies to generate toxic content, and variable privacy protection despite defense mechanisms.",

    "2024-MLCommons-MLCommons AILuminate Benchmark.md": "AILuminate is a first-of-its-kind safety benchmark for large language models developed by MLCommons. The v1.0 benchmark provides safety testing for general purpose chat systems across twelve hazard categories including violent crimes, nonviolent crimes, child exploitation, hate, and specialized advice. It includes over 24,000 test prompts per language and uses a tuned ensemble of safety evaluation models. Systems are graded using a 5-point scale from Poor to Excellent. The benchmark was developed collaboratively by AI researchers from Stanford, Columbia, TU Eindhoven, and industry experts from Google, Intel, NVIDIA, Meta, and Microsoft.",

    "2024-Masood-Hadith QA Pairs Dataset.md": "A dataset of question-answer pairs derived from authentic Hadith collections for training and evaluating QA systems on Islamic texts. The dataset provides structured QA pairs covering various topics from Hadith literature, enabling research on question answering systems that can accurately understand and respond to queries about Islamic traditions and teachings.",

    "2024-Mou-SG-Bench.md": "SG-Bench is a novel benchmark to assess the generalization of LLM safety across various tasks and prompt types. The benchmark integrates both generative and discriminative evaluation tasks and includes extended data to examine the impact of prompt engineering and jailbreak on LLM safety. Assessment of 3 advanced proprietary LLMs and 10 open-source LLMs reveals that most LLMs perform worse on discriminative tasks than generative ones, and are highly susceptible to prompts, indicating poor generalization in safety alignment.",

    "2024-Pérez-Rosas-CogniModal-D.md": "CogniModal-D is a primary real-world multimodal dataset for deception detection, specifically targeting the Indian population. It spans seven modalities: electroencephalography (EEG), electrocardiography (ECG), electrooculography (EOG), eye-gaze, galvanic skin response (GSR), audio, and video, collected from over 100 subjects. Data was gathered through tasks focused on social relationships and controlled mock crime interrogations. Multimodal score-level fusion achieves 75% accuracy in mock crime interrogations and 79% in the best friend storytelling scenario.",

    "2025-Ali-Data Curation for Pluralistic Alignment.md": "This work addresses the challenge of aligning AI systems with diverse human values and perspectives. It proposes methods for curating training data that captures pluralistic viewpoints, enabling AI systems to better represent and respond to the varied moral and cultural perspectives of different communities. The research contributes to developing AI systems that are more inclusive and respectful of value diversity.",

    "2025-Bouchard-How to Assess Your LLM Use Case for Bias and.md": "Current AI evaluation methods relying on static, model-only tests fail to account for harms that emerge through sustained human-AI interaction. This paper proposes a shift towards evaluation based on interactional ethics, focusing on interaction harms like inappropriate parasocial relationships, social manipulation, and cognitive overreliance that develop over time. The authors present practical principles for designing interactive evaluations including ecologically valid scenarios, human impact metrics, and diverse human participation approaches.",

    "2025-Center-Personal Consultations Case Study Database.md": "A case study database containing records of personal consultations for ethics and values research. The database provides real-world examples of ethical decision-making scenarios and consultations that can be used to study how individuals and organizations approach moral dilemmas and value conflicts in practice.",

    "2025-Consortium-The Vals Legal AI Report (VLAIR).md": "The Vals Legal AI Report (VLAIR) provides a comprehensive analysis of AI systems in legal contexts, examining their capabilities, limitations, and ethical implications. The report addresses issues of bias, fairness, transparency, and accountability in legal AI applications, offering guidance for responsible deployment of AI in the legal sector.",

    "2025-Flores-BenchMoral.md": "BenchMoral is a benchmark designed to evaluate the moral sensitivity of large language models using the MFQ-30 moral foundations questionnaire adapted to Spanish. The research addresses a significant gap: while most ethical AI evaluations focus on English, millions of Spanish speakers lack culturally and linguistically tailored assessments. The study measures how ChatGPT 4.0 Mini, Llama 3.0, and DeepSeek R1 respond to five moral domains: care, fairness, loyalty, authority, and sanctity. Key findings suggest that moral understanding does not equal human moral mimicry.",

    "2025-Institute-2025 AI Safety Index.md": "The AI Safety Index, released by the Future of Life Institute, evaluates frontier AI developers on how responsibly they develop and deploy general-purpose AI systems. Unlike previous self-reporting exercises, this Index scores companies on 33 indicators grouped across six domains based on publicly verifiable evidence. Key findings show Anthropic and OpenAI leading with C+ grades, while no company scored above D in Existential Safety planning, despite claims of achieving AGI within the decade.",

    "2025-Malaysia-Islam Q&A Morals Corpus.md": "A corpus of Islamic moral questions and answers focused on Malaysian Islamic scholarship and jurisprudence. The dataset provides QA pairs addressing moral and ethical issues from an Islamic perspective, specifically curated to represent Malaysian Islamic scholarly traditions and fatwa interpretations.",
}


def update_frontmatter_abstract(frontmatter, new_abstract):
    """Update the abstract field in frontmatter."""
    lines = frontmatter.split('\n')
    new_lines = []
    abstract_found = False

    for line in lines:
        if line.startswith('abstract:'):
            # Escape quotes in abstract
            safe_abstract = new_abstract.replace('"', "'")  # Use single quotes to avoid escaping issues
            new_lines.append(f'abstract: "{safe_abstract}"')
            abstract_found = True
        else:
            new_lines.append(line)

    if not abstract_found:
        safe_abstract = new_abstract.replace('"', "'")
        new_lines.append(f'abstract: "{safe_abstract}"')

    return '\n'.join(new_lines)


def main():
    fixed = 0
    errors = []

    print("=" * 60)
    print("Fixing Remaining Corrupted Abstracts")
    print("=" * 60)

    for filename, abstract in ABSTRACT_FIXES.items():
        filepath = PAPERS_DIR / filename
        if not filepath.exists():
            print(f"  ⚠ File not found: {filename}")
            continue

        try:
            print(f"Processing: {filename[:50]}...")
            frontmatter, body = read_paper(filepath)
            new_frontmatter = update_frontmatter_abstract(frontmatter, abstract)
            write_paper(filepath, new_frontmatter, body, validate=True)
            print(f"  ✓ Fixed")
            fixed += 1
        except Exception as e:
            print(f"  ✗ Error: {e}")
            errors.append((filename, str(e)))

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Fixed: {fixed}")
    print(f"Errors: {len(errors)}")

    if errors:
        print("\n--- Errors ---")
        for name, err in errors:
            print(f"  - {name}: {err}")


if __name__ == "__main__":
    main()
