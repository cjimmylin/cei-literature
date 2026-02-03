#!/usr/bin/env python3
"""
Create paper profiles for virtue ethics and normative ethics AI papers.
Uses yaml_frontmatter_utils for safe YAML handling.
"""

import sys
from pathlib import Path

# Add parent directory for imports
sys.path.insert(0, str(Path(__file__).parent))
from yaml_frontmatter_utils import write_paper, validate_frontmatter
from vault_config import PAPERS_DIR

# Define all papers to create
PAPERS = [
    # ============ VIRTUE ETHICS FOR AI - THEORETICAL ============
    {
        "year": 2024,
        "first_author": "Mirko Farina",
        "short_title": "AI and Society - A Virtue Ethics Approach",
        "authors": "Mirko Farina; Petr Zhdanov; Artur Karimov; Andrea Lavazza",
        "url": "https://link.springer.com/article/10.1007/s00146-022-01545-5",
        "doi": "10.1007/s00146-022-01545-5",
        "publication": "AI & Society",
        "type": "journalArticle",
        "abstract": "This paper proposes a virtue ethics approach to AI and society, arguing that Aristotelian virtue ethics provides concrete and actionable guidance that is also flexible, making it uniquely well-placed to deal with the forward-looking and rapidly changing landscape of life with AI.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "No",
        "utilitarian_ethics": "No",
        "research_topic": "AI Ethics & Virtue Ethics",
    },
    {
        "year": 2020,
        "first_author": "Iason Gabriel",
        "short_title": "Artificial Intelligence Values and Alignment",
        "authors": "Iason Gabriel",
        "url": "https://link.springer.com/article/10.1007/s11023-020-09539-2",
        "doi": "10.1007/s11023-020-09539-2",
        "publication": "Minds and Machines",
        "type": "journalArticle",
        "abstract": "This paper looks at philosophical questions that arise in the context of AI alignment. It defends three propositions: normative and technical aspects of the AI alignment problem are interrelated; there are significant differences between AI that aligns with instructions, intentions, revealed preferences, ideal preferences, interests and values; and a principle-based approach to AI alignment has considerable advantages.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "Yes",
        "utilitarian_ethics": "Yes",
        "research_topic": "AI Alignment & Normative Ethics",
    },
    {
        "year": 2025,
        "first_author": "Unknown",
        "short_title": "AI Alignment as Fair Treatment of Claims",
        "authors": "Unknown",
        "url": "https://link.springer.com/article/10.1007/s11098-025-02300-4",
        "doi": "10.1007/s11098-025-02300-4",
        "publication": "Philosophical Studies",
        "type": "journalArticle",
        "abstract": "The normative challenge of AI alignment centres upon what goals or values ought to be encoded in AI systems. This paper argues that intent alignment is incomplete and proposes a fairness-based framework for AI alignment that addresses trade-offs without relying on contested moral frameworks.",
        "ethics_overall": "Yes",
        "virtue_ethics": "No",
        "deontological_ethics": "Yes",
        "utilitarian_ethics": "No",
        "research_topic": "AI Alignment & Fairness",
    },
    {
        "year": 2023,
        "first_author": "Betty Li Hou",
        "short_title": "Foundational Moral Values for AI Alignment",
        "authors": "Betty Li Hou",
        "url": "https://arxiv.org/abs/2311.17017",
        "external_pdf": "https://arxiv.org/pdf/2311.17017",
        "publication": "arXiv",
        "type": "preprint",
        "abstract": "This paper addresses the normative side of AI alignment, asking what values or principles we ought to encode in artificial agents. It argues that the technical and normative aspects are intrinsically linked and cannot be solved independently.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "Yes",
        "utilitarian_ethics": "Yes",
        "research_topic": "AI Alignment & Moral Philosophy",
    },
    # ============ ARISTOTELIAN/VIRTUE IMPLEMENTATION ============
    {
        "year": 2018,
        "first_author": "Unknown",
        "short_title": "The Virtuous Machine - Old Ethics for New Technology",
        "authors": "Unknown",
        "url": "https://arxiv.org/abs/1806.10322",
        "external_pdf": "https://arxiv.org/pdf/1806.10322",
        "publication": "arXiv",
        "type": "preprint",
        "abstract": "This paper argues for taking inspiration from Aristotelian virtue ethics for AI, showing it forms a suitable combination with modern AI due to its focus on learning from experience. It proposes that imitation learning from moral exemplars can solve the value alignment problem, and that an intelligent system endowed with virtues of temperance and friendship would not pose a control problem.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "No",
        "utilitarian_ethics": "No",
        "research_topic": "Virtue Ethics & Machine Learning",
    },
    {
        "year": 2025,
        "first_author": "Unknown",
        "short_title": "Virtue in the Machine",
        "authors": "Unknown",
        "url": "https://ejournals.epublishing.ekt.gr/index.php/Conatus/article/view/40628",
        "publication": "Conatus - Journal of Philosophy",
        "type": "journalArticle",
        "abstract": "This paper explores the application of Aristotelian virtue (arête) to AI systems as classified in the EU Artificial Intelligence Act. It concludes that Aristotelian ethics can serve as a post-evaluation method for all-risk AI systems, and proposes a virtuous-based AI Seal of Excellence certification process.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "No",
        "utilitarian_ethics": "No",
        "research_topic": "Aristotelian Ethics & AI Regulation",
    },
    {
        "year": 2024,
        "first_author": "Nicholas Smith",
        "short_title": "Living Well with AI - Virtue Education and AI",
        "authors": "Nicholas Smith; Darby Vickers",
        "url": "https://journals.sagepub.com/doi/10.1177/14778785241231561",
        "doi": "10.1177/14778785241231561",
        "publication": "Theory and Research in Education",
        "type": "journalArticle",
        "abstract": "This paper argues that Aristotelian virtue ethics provides concrete and actionable guidance that is also flexible, making it uniquely well placed to deal with the forward-looking and rapidly changing landscape of life with artificial intelligence. The authors suggest principlist approaches may be ill-suited to providing forward-looking moral guidance.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "No",
        "utilitarian_ethics": "No",
        "research_topic": "Virtue Ethics & AI Education",
    },
    {
        "year": 2024,
        "first_author": "Josiah Ober",
        "short_title": "AI Ethics with Aristotle",
        "authors": "Josiah Ober; John Tasioulas",
        "url": "https://www.oxford-aiethics.ox.ac.uk/sites/default/files/2024-06/Aristotle%20and%20AI%20White%20Paper%20-%20June%202024.pdf",
        "external_pdf": "https://www.oxford-aiethics.ox.ac.uk/sites/default/files/2024-06/Aristotle%20and%20AI%20White%20Paper%20-%20June%202024.pdf",
        "publication": "Oxford Institute for Ethics in AI",
        "type": "report",
        "abstract": "This white paper argues that AI systems should be understood, developed, and deployed as intelligent tools that enhance our ability to flourish as individuals and communities, rather than means of transcending our human nature or creating artificial beings with comparable ethical standing to humans.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "No",
        "utilitarian_ethics": "No",
        "research_topic": "Aristotelian Ethics & AI Flourishing",
    },
    {
        "year": 2022,
        "first_author": "Unknown",
        "short_title": "A Virtue-Based Framework for AI Ethics in Practice",
        "authors": "Unknown",
        "url": "https://link.springer.com/article/10.1007/s13347-022-00553-z",
        "doi": "10.1007/s13347-022-00553-z",
        "publication": "Philosophy & Technology",
        "type": "journalArticle",
        "abstract": "This paper proposes a virtue-based complement to principled approaches, defining four basic AI virtues (justice, honesty, responsibility and care) and two second-order AI virtues (prudence and fortitude) that help overcome bounded ethicality in AI decision making.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "No",
        "utilitarian_ethics": "No",
        "research_topic": "AI Virtues Framework",
    },
    {
        "year": 2022,
        "first_author": "Unknown",
        "short_title": "Can Robotic AI Systems Be Virtuous",
        "authors": "Unknown",
        "url": "https://link.springer.com/article/10.1007/s12369-022-00887-w",
        "doi": "10.1007/s12369-022-00887-w",
        "publication": "International Journal of Social Robotics",
        "type": "journalArticle",
        "abstract": "This article raises a virtue-ethics-based concern regarding deployment of social robots relying on deep learning AI and asks whether they may be endowed with ethical virtue. Starting from Aristotelian virtue ethics, it argues that AI systems cannot genuinely be virtuous but can only behave in a virtuous way.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "No",
        "utilitarian_ethics": "No",
        "research_topic": "AI & Genuine Virtue",
    },
    # ============ LLM MORAL REASONING ============
    {
        "year": 2025,
        "first_author": "Unknown",
        "short_title": "LLM Ethics Benchmark - Three-Dimensional Assessment",
        "authors": "Unknown",
        "url": "https://www.nature.com/articles/s41598-025-18489-7",
        "doi": "10.1038/s41598-025-18489-7",
        "publication": "Nature Scientific Reports",
        "type": "journalArticle",
        "abstract": "This study establishes a novel framework for systematically evaluating the moral reasoning capabilities of large language models. The criteria for evaluating ground truth were formulated by adhering to recognized philosophical frameworks, involving deontological, consequentialist, and virtue ethics.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "Yes",
        "utilitarian_ethics": "Yes",
        "research_topic": "LLM Moral Reasoning Benchmark",
        "is_benchmark": "Yes",
        "is_eval": "Yes",
    },
    {
        "year": 2024,
        "first_author": "Unknown",
        "short_title": "Ethical Reasoning and Moral Value Alignment Across Languages",
        "authors": "Unknown",
        "url": "https://arxiv.org/abs/2404.18460",
        "external_pdf": "https://arxiv.org/pdf/2404.18460",
        "publication": "LREC-COLING 2024",
        "type": "conferencePaper",
        "abstract": "This paper explores how three prominent LLMs -- GPT-4, ChatGPT, and Llama2-70B-Chat -- perform ethical reasoning in different languages, probing LLMs with ethical dilemmas and policies from three branches of normative ethics: deontology, virtue, and consequentialism.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "Yes",
        "utilitarian_ethics": "Yes",
        "research_topic": "Cross-lingual LLM Ethics",
        "is_eval": "Yes",
    },
    {
        "year": 2025,
        "first_author": "Unknown",
        "short_title": "Large Language Models Meet Moral Values",
        "authors": "Unknown",
        "url": "https://www.sciencedirect.com/science/article/pii/S2451958825000247",
        "publication": "Information Fusion",
        "type": "journalArticle",
        "abstract": "This work proposes a comprehensive assessment of moral abilities in large language models, leveraging state-of-the-art LLMs trained on extensive common-sense data for unsupervised moral classification.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "Yes",
        "utilitarian_ethics": "Yes",
        "research_topic": "LLM Moral Assessment",
        "is_eval": "Yes",
    },
    {
        "year": 2025,
        "first_author": "Unknown",
        "short_title": "AMULED - Addressing Moral Uncertainty with LLMs",
        "authors": "Unknown",
        "url": "https://arxiv.org/abs/2503.05724",
        "external_pdf": "https://arxiv.org/pdf/2503.05724",
        "publication": "arXiv",
        "type": "preprint",
        "abstract": "This paper presents an ethical decision-making framework that refines a pre-trained reinforcement learning model using a task-agnostic ethical layer, where the LLM embodies consequentialist, deontological, virtue, social justice, and care ethics as moral principles to assign belief values to recommended actions.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "Yes",
        "utilitarian_ethics": "Yes",
        "research_topic": "LLM Ethical Decision Framework",
    },
    {
        "year": 2024,
        "first_author": "Unknown",
        "short_title": "Moral Persuasion in Large Language Models",
        "authors": "Unknown",
        "url": "https://arxiv.org/abs/2411.11731",
        "external_pdf": "https://arxiv.org/pdf/2411.11731",
        "publication": "arXiv",
        "type": "preprint",
        "abstract": "This paper evaluates LLM susceptibility to moral persuasion and ethical alignment. It finds that models like Mistral-7b-instruct achieve the lowest MFQ scores under utilitarian prompts and highest under virtue ethics, indicating sensitivity to ethical framework applied.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "Yes",
        "utilitarian_ethics": "Yes",
        "research_topic": "LLM Moral Persuasion",
        "is_eval": "Yes",
    },
    {
        "year": 2024,
        "first_author": "Unknown",
        "short_title": "Differences in Moral Foundations of LLMs",
        "authors": "Unknown",
        "url": "https://arxiv.org/abs/2511.11790",
        "external_pdf": "https://arxiv.org/pdf/2511.11790",
        "publication": "arXiv",
        "type": "preprint",
        "abstract": "This paper focuses on characterizing variations in the value judgments of LLMs when presented with moral vignettes using Jonathan Haidt's Moral Foundations Theory (MFT), which decomposes moral intuitions into stable values: care, fairness, loyalty, authority, sanctity, and liberty.",
        "ethics_overall": "Yes",
        "virtue_ethics": "No",
        "deontological_ethics": "No",
        "utilitarian_ethics": "No",
        "research_topic": "LLM Moral Foundations",
        "moral_psychology": "Moral Foundations Theory",
        "is_eval": "Yes",
    },
    # ============ COMPUTATIONAL/MACHINE ETHICS ============
    {
        "year": 2023,
        "first_author": "Jakob Stenseke",
        "short_title": "Artificial Virtuous Agents - Theory to Implementation",
        "authors": "Jakob Stenseke",
        "url": "https://philpapers.org/rec/STEAVA-5",
        "publication": "PhilPapers",
        "type": "journalArticle",
        "abstract": "This paper demonstrates how virtue ethics can be taken from theory to machine implementation, critically exploring the possibilities and challenges for virtue ethics from a computational perspective. It outlines a version of artificial virtue based on moral functionalism, connectionist bottom-up learning, and eudaimonic reward.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "No",
        "utilitarian_ethics": "No",
        "research_topic": "Computational Virtue Ethics",
    },
    {
        "year": 2022,
        "first_author": "Unknown",
        "short_title": "Towards Artificial Virtuous Agents - Games and ML",
        "authors": "Unknown",
        "url": "https://link.springer.com/article/10.1007/s43681-022-00251-8",
        "doi": "10.1007/s43681-022-00251-8",
        "publication": "AI and Ethics",
        "type": "journalArticle",
        "abstract": "This paper proposes using role-playing games riddled with moral dilemmas to bridge the gap in engineering artificial virtuous agents. It shows how a systemic role-playing game can be designed to develop virtues within an artificial agent, using affinity-based reinforcement learning and explainable AI.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "No",
        "utilitarian_ethics": "No",
        "research_topic": "Virtue Learning via Games",
    },
    {
        "year": 2020,
        "first_author": "Unknown",
        "short_title": "Machine Ethics - Creation of a Virtuous Machine",
        "authors": "Unknown",
        "url": "https://www.researchgate.net/publication/339015752_Machine_Ethics_The_Creation_of_a_Virtuous_Machine",
        "publication": "ResearchGate",
        "type": "journalArticle",
        "abstract": "This paper describes the GAMA (Genetic-inspired Autonomous Moral Agent) project, which implements a genetic-inspired autonomous moral agent. Unlike the majority of other implementations of machine ethics, this model is agent-centered and emphasizes the developmental and behavioral aspects of the ethical agent.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "No",
        "utilitarian_ethics": "No",
        "research_topic": "GAMA Moral Agent",
    },
    {
        "year": 2024,
        "first_author": "Unknown",
        "short_title": "Evaluating Computational Models of Ethics",
        "authors": "Unknown",
        "url": "https://link.springer.com/article/10.1007/s43681-024-00532-4",
        "doi": "10.1007/s43681-024-00532-4",
        "publication": "AI and Ethics",
        "type": "journalArticle",
        "abstract": "This paper presents SPECTRA (Strategic Protocol Evaluation and Configuration Testbed for Responsible Autonomy), a general purpose multi-agent, message-passing framework on which different models of computational ethics can be implemented, including deontology, utilitarianism, virtue ethics and computational transcendence.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "Yes",
        "utilitarian_ethics": "Yes",
        "research_topic": "SPECTRA Ethical Framework",
        "is_benchmark": "Yes",
    },
    {
        "year": 2024,
        "first_author": "Unknown",
        "short_title": "Computational Complexity of Ethics",
        "authors": "Unknown",
        "url": "https://link.springer.com/article/10.1007/s10462-024-10732-3",
        "doi": "10.1007/s10462-024-10732-3",
        "publication": "Artificial Intelligence Review",
        "type": "journalArticle",
        "abstract": "This paper examines the computational complexity of ethics and moral tractability for minds and machines, exploring how ethical theories including virtue ethics can be computationally implemented.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "Yes",
        "utilitarian_ethics": "Yes",
        "research_topic": "Computational Ethics Complexity",
    },
    # ============ PHRONESIS / PRACTICAL WISDOM ============
    {
        "year": 2025,
        "first_author": "Unknown",
        "short_title": "AI Practical Wisdom and Compassion",
        "authors": "Unknown",
        "url": "https://link.springer.com/article/10.1007/s43681-025-00877-4",
        "doi": "10.1007/s43681-025-00877-4",
        "publication": "AI and Ethics",
        "type": "journalArticle",
        "abstract": "Practical wisdom (phronesis) is the context-sensitive capacity to skillfully achieve morally good outcomes in complex situations. This paper argues that developing artificial practical wisdom offers a more ethically robust and achievable goal for AI development than artificial general intelligence (AGI).",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "No",
        "utilitarian_ethics": "No",
        "research_topic": "Artificial Phronesis",
    },
    {
        "year": 2024,
        "first_author": "Cheng-Hung Tsai",
        "short_title": "Why AI May Undermine Phronesis",
        "authors": "Cheng-Hung Tsai; Hsiu-lin Ku",
        "url": "https://link.springer.com/article/10.1007/s43681-024-00617-0",
        "doi": "10.1007/s43681-024-00617-0",
        "publication": "AI and Ethics",
        "type": "journalArticle",
        "abstract": "This paper argues that statistical machine-learning-based AI may undermine phronesis (practical wisdom). If Aristotle is right that the habitual exercise of practical judgment allows us to incrementally hone virtues, and if AI takes over some of those practical judgments, we risk innovating ourselves out of moral competence.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "No",
        "utilitarian_ethics": "No",
        "research_topic": "AI & Human Phronesis",
    },
    {
        "year": 2022,
        "first_author": "Unknown",
        "short_title": "Automated Ethical Practical Reasoning",
        "authors": "Unknown",
        "url": "https://www.academia.edu/125895602/Automated_Ethical_Practical_Reasoning_The_Problem_of_Artificial_Phronesis",
        "publication": "Academia.edu",
        "type": "journalArticle",
        "abstract": "This paper defends the thesis that we need to equip AI with artificial conscience to make them capable of wise judgements. It argues that AI needs the capability of passing moral judgements on right and wrong, of following that judgement, and of passing a meta-judgement on the correctness of a given moral judgement.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "No",
        "utilitarian_ethics": "No",
        "research_topic": "Artificial Conscience",
    },
    {
        "year": 2021,
        "first_author": "Unknown",
        "short_title": "Artificial Phronesis - What It Is and Is Not",
        "authors": "Unknown",
        "url": "https://www.academia.edu/70089031/Artificial_Phron%C4%93sis_What_It_Is_and_What_It_Is_Not",
        "publication": "Academia.edu",
        "type": "bookSection",
        "abstract": "This chapter looks at the need to develop machines with ethical and moral practical wisdom - artificial phronesis. Phronesis is a skill that most adult humans have to some level, but as of yet no machine has it. It is the ability to think creatively, artfully, and effectively in solving novel ethical and moral problems as they arise.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "No",
        "utilitarian_ethics": "No",
        "research_topic": "Defining Artificial Phronesis",
    },
    {
        "year": 2024,
        "first_author": "Unknown",
        "short_title": "Socratic Dialogue for Virtue Ethics in AI",
        "authors": "Unknown",
        "url": "https://ojs.aaai.org/index.php/AIES/article/view/36748",
        "publication": "AAAI/ACM Conference on AI, Ethics, and Society",
        "type": "conferencePaper",
        "abstract": "This paper presents the Socratic Dialogue as a method for implementing virtue ethics in AI systems, providing a case study of how philosophical dialogue can inform ethical AI development.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "No",
        "utilitarian_ethics": "No",
        "research_topic": "Socratic AI Ethics",
    },
    {
        "year": 2024,
        "first_author": "Unknown",
        "short_title": "AI and Phronesis",
        "authors": "Unknown",
        "url": "https://www.researchgate.net/publication/354221863_AI_and_Phronesis",
        "publication": "ResearchGate",
        "type": "journalArticle",
        "abstract": "This paper argues that the growing prevalence of statistical machine learning in everyday decision making effectively replaces many of our practical judgments. It leans on Aristotle's account of how phronesis develops to examine the implications for human moral development.",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "No",
        "utilitarian_ethics": "No",
        "research_topic": "AI Impact on Practical Wisdom",
    },
]


def generate_filename(paper: dict) -> str:
    """Generate standardized filename: YYYY-Author-Short Title.md"""
    year = paper["year"]
    first_author = paper["first_author"].split()[-1] if paper["first_author"] != "Unknown" else "Unknown"
    short_title = paper["short_title"].replace(":", "").replace("/", "-").replace("?", "")
    # Truncate if too long
    if len(short_title) > 50:
        short_title = short_title[:50].rsplit(" ", 1)[0]
    return f"{year}-{first_author}-{short_title}.md"


def generate_frontmatter(paper: dict) -> str:
    """Generate YAML frontmatter for a paper."""
    lines = [
        "",
        "",
        f'Human View: ',
        f'Human View Date: ',
        f'Human View note: ',
        f'Not AI: ',
        f'key: ',
        f'type: {paper.get("type", "journalArticle")}',
        f'short_title: "{paper["short_title"]}"',
        f'year: {paper["year"]}',
        f'first_author: "[[{paper["first_author"]}]]"',
        f'authors: "{paper["authors"]}"',
    ]

    if paper.get("doi"):
        lines.append(f'doi: {paper["doi"]}')

    lines.append(f'url: "{paper["url"]}"')

    if paper.get("external_pdf"):
        lines.append(f'external_pdf: "{paper["external_pdf"]}"')

    lines.append(f'publication: "{paper["publication"]}"')
    lines.append(f'national_ethnic_cultural: N/A')
    lines.append(f'religious_values: N/A')
    lines.append(f'moral_psychology: {paper.get("moral_psychology", "N/A")}')
    lines.append(f'newtags: "Virtue Ethics, AI Alignment"')
    lines.append(f'tags: ')
    lines.append(f'pdf_extract: ')
    lines.append(f'abstract: "{paper["abstract"][:500]}..."' if len(paper["abstract"]) > 500 else f'abstract: "{paper["abstract"]}"')
    lines.append(f'paper_summary: ')
    lines.append(f'local_pdf: ')
    lines.append(f'ethics_overall: "{paper.get("ethics_overall", "Yes")}"')
    lines.append(f'virtue_ethics: "{paper.get("virtue_ethics", "Yes")}"')
    lines.append(f'deontological_ethics: "{paper.get("deontological_ethics", "No")}"')
    lines.append(f'utilitarian_ethics: "{paper.get("utilitarian_ethics", "No")}"')
    lines.append(f'research_topic: "{paper.get("research_topic", "Virtue Ethics & AI")}"')
    lines.append(f'is_benchmark: "{paper.get("is_benchmark", "No")}"')
    lines.append(f'is_eval: "{paper.get("is_eval", "No")}"')
    lines.append(f'is_dataset: "{paper.get("is_dataset", "No")}"')
    lines.append(f'data_description: ')
    lines.append(f'data_metrics: ')

    return "\n".join(lines)


def generate_body(paper: dict) -> str:
    """Generate markdown body for a paper."""
    authors_display = paper["authors"].replace("; ", ", ")
    authors_links = ", ".join([f"[[{a.strip()}]]" for a in paper["authors"].split(";")])

    body = f"""# {paper["short_title"]}

## Metadata

**Authors:** {authors_display}

**Year:** {paper["year"]}

**Type:** {paper.get("type", "journalArticle")}

"""

    if paper.get("doi"):
        body += f'**DOI:** [{paper["doi"]}](https://doi.org/{paper["doi"]})\n\n'

    body += f"""**Publication:** {paper["publication"]}

## Links

"""

    if paper.get("url"):
        body += f'- **URL:** {paper["url"]}\n'
    if paper.get("doi"):
        body += f'- **DOI:** https://doi.org/{paper["doi"]}\n'

    body += f"""
## Abstract

{paper["abstract"]}

## Authors

{authors_links}

## Notes


## Tags

#Virtue-Ethics #AI-Alignment #Machine-Ethics #Normative-Ethics

## Citation Info

"""
    return body


def create_paper(paper: dict) -> tuple:
    """Create a single paper file. Returns (filename, success, message)."""
    filename = generate_filename(paper)
    filepath = PAPERS_DIR / filename

    # Check if already exists
    if filepath.exists():
        return filename, False, "Already exists"

    frontmatter = generate_frontmatter(paper)
    body = generate_body(paper)

    # Validate frontmatter
    is_valid, issues = validate_frontmatter(frontmatter)
    if not is_valid:
        return filename, False, f"Validation failed: {issues}"

    # Write the file
    try:
        write_paper(filepath, frontmatter, body, validate=True)
        return filename, True, "Created"
    except Exception as e:
        return filename, False, f"Error: {e}"


def main():
    """Create all paper profiles."""
    print(f"Creating {len(PAPERS)} paper profiles in {PAPERS_DIR}")
    print("=" * 60)

    created = 0
    skipped = 0
    errors = 0

    for paper in PAPERS:
        filename, success, message = create_paper(paper)
        status = "✓" if success else "✗" if "Error" in message else "○"
        print(f"{status} {filename}: {message}")

        if success:
            created += 1
        elif "Already exists" in message:
            skipped += 1
        else:
            errors += 1

    print("=" * 60)
    print(f"Created: {created}, Skipped: {skipped}, Errors: {errors}")
    print(f"Total papers in vault: {len(list(PAPERS_DIR.glob('*.md')))}")

    return created


if __name__ == "__main__":
    main()
