#!/usr/bin/env python3
"""
Create paper profiles for consequentialist/utilitarian ethics papers.
"""

import os
from pathlib import Path
from datetime import datetime

# Paper data
papers = [
    {
        "filename": "2025-Hui-Decoding Moral Responses in AI.md",
        "short_title": "Decoding Moral Responses in AI",
        "year": 2025,
        "first_author": "Bryant P.H. Hui",
        "authors": "Bryant P.H. Hui; Chiu Lun Lau; Rui Sun",
        "doi": "10.1016/j.chbr.2025.100854",
        "url": "https://www.sciencedirect.com/science/article/pii/S2451958825002696",
        "external_pdf": "https://www.sciencedirect.com/science/article/pii/S2451958825002696/pdfft?md5=c8e7d7c8c8c8c8c8c8c8c8c8c8c8c8c8&pid=1-s2.0-S2451958825002696-main.pdf",
        "publication": "Computers in Human Behavior Reports",
        "type": "journalArticle",
        "abstract": "Despite the proliferation of powerful large language models (LLMs), there remains a need for systematic, quantitative comparisons of their responses to moral dilemmas. This study builds on advances in AI ethics by systematically comparing the moral response patterns of seven LLMs, including GPT-3, GPT-3.5, GPT-4, GPT-4.1, Claude 3.7 Sonnet, Grok 3, and Gemini 2.5 Pro. Each LLM was presented with a series of moral dilemmas, both personal and impersonal, under three conditions: no rule, a deontological preamble, and a utilitarian preamble. LLMs differentiate moral personal and impersonal dilemmas like humans: more utilitarian choices in non-emotional decisions. The findings highlight the learning prowess of LLMs and potential ways AI models diverge from human response patterns in morally charged scenarios.",
        "key_contribution": "Systematic quantitative comparison of seven LLMs on moral dilemmas showing utilitarian tendencies in impersonal contexts",
        "significance": "Demonstrates that LLMs exhibit human-like patterns in moral reasoning but diverge in emotional/personal contexts",
        "newtags": "Utilitarianism, Moral Dilemmas, LLM Evaluation",
    },
    {
        "filename": "2025-Dillion-AI Language Model Rivals Expert Ethicist.md",
        "short_title": "AI Language Model Rivals Expert Ethicist",
        "year": 2025,
        "first_author": "Danica Dillion",
        "authors": "Danica Dillion; Debanjan Mondal; Niket Tandon; Kurt Gray",
        "doi": "10.1038/s41598-025-86510-0",
        "url": "https://www.nature.com/articles/s41598-025-86510-0",
        "external_pdf": "https://www.nature.com/articles/s41598-025-86510-0.pdf",
        "publication": "Scientific Reports",
        "type": "journalArticle",
        "abstract": "This study advances work on the Moral Turing Test and finds that Americans rate ethical advice from GPT-4o as slightly more moral, trustworthy, thoughtful, and correct than that of the popular New York Times advice column, The Ethicist. Participants perceived GPT models as surpassing both a representative sample of Americans and a renowned ethicist in delivering moral justifications and advice.",
        "key_contribution": "Empirical evidence that GPT-4o's ethical advice is rated more favorably than expert human ethicists",
        "significance": "Advances the Moral Turing Test research showing AI can match or exceed human moral expertise perception",
        "newtags": "Utilitarianism, Moral Turing Test, AI Ethics",
    },
    {
        "filename": "2024-Stenseke-Computational Complexity of Ethics.md",
        "short_title": "Computational Complexity of Ethics",
        "year": 2024,
        "first_author": "Jakob Stenseke",
        "authors": "Jakob Stenseke",
        "doi": "10.1007/s10462-024-10732-3",
        "url": "https://link.springer.com/article/10.1007/s10462-024-10732-3",
        "external_pdf": "https://arxiv.org/pdf/2302.04218.pdf",
        "publication": "Artificial Intelligence Review",
        "type": "journalArticle",
        "abstract": "Debates on whether artificial intelligence can or should be used to solve problems in ethical domains have mainly been driven by what AI can or cannot do in terms of human capacities. This paper addresses these issues by exploring what kind of moral machines are possible based on the ethical problems computational systems can or cannot solve effectively, analyzing normative ethics through the lens of computational complexity theory. The results indicate that most problems the normative frameworks pose lead to tractability issues in every category analyzed.",
        "key_contribution": "Analyzes consequentialism, deontology, and virtue ethics through computational complexity theory",
        "significance": "Shows tractability issues for all major normative frameworks when implemented computationally",
        "newtags": "Utilitarianism, Deontology, Virtue Ethics, Computational Complexity",
    },
    {
        "filename": "2024-Zhi-Xuan-Beyond Preferences in AI Alignment.md",
        "short_title": "Beyond Preferences in AI Alignment",
        "year": 2024,
        "first_author": "Tan Zhi-Xuan",
        "authors": "Tan Zhi-Xuan; Micah Carroll; Matija Franklin; Hal Ashton",
        "doi": "10.1007/s11098-024-02249-w",
        "url": "https://link.springer.com/article/10.1007/s11098-024-02249-w",
        "external_pdf": "https://arxiv.org/pdf/2408.16984.pdf",
        "publication": "Philosophical Studies",
        "type": "journalArticle",
        "abstract": "The dominant practice of AI alignment assumes that preferences are an adequate representation of human values, that human rationality can be understood in terms of maximizing the satisfaction of preferences, and that AI systems should be aligned with preferences of one or more humans. These commitments constitute what we term a preferentist approach to AI alignment. In this paper, we characterize and challenge the preferentist approach, describing conceptual and technical alternatives. We argue that expected utility theory is both unnecessary and insufficient for rational agency.",
        "key_contribution": "Critiques expected utility maximization as the foundation for AI alignment",
        "significance": "Proposes alternatives to preferentist approaches showing utility theory limitations",
        "newtags": "Utilitarianism, Value Alignment, Expected Utility Theory",
    },
    {
        "filename": "2025-Barman-RLHF Whose Culture Whose Values.md",
        "short_title": "RLHF Whose Culture Whose Values",
        "year": 2025,
        "first_author": "Kristian Gonzalez Barman",
        "authors": "Kristian Gonzalez Barman; Simon Lohse; Henk W. De Regt",
        "doi": "10.1007/s13347-025-00861-0",
        "url": "https://link.springer.com/article/10.1007/s13347-025-00861-0",
        "external_pdf": "https://arxiv.org/pdf/2407.17482.pdf",
        "publication": "Philosophy & Technology",
        "type": "journalArticle",
        "abstract": "This paper argues for the epistemic and ethical advantages of pluralism in Reinforcement Learning from Human Feedback (RLHF) in the context of Large Language Models (LLMs). Drawing on social epistemology and pluralist philosophy of science, we suggest ways in which RLHF can be made more responsive to human needs and how to address challenges along the way.",
        "key_contribution": "Argues for epistemic and ethical pluralism in RLHF to address value diversity",
        "significance": "Addresses whose values are encoded in RLHF and proposes pluralist solutions",
        "newtags": "RLHF, Value Pluralism, Social Epistemology",
    },
    {
        "filename": "2025-Chaudhari-RLHF Deciphered.md",
        "short_title": "RLHF Deciphered",
        "year": 2025,
        "first_author": "Shreyas Chaudhari",
        "authors": "Shreyas Chaudhari; Pranjal Aggarwal; Vishvak Murahari; Tanmay Rajpurohit; Ashwin Kalyan; Karthik Narasimhan; Ameet Deshpande; Bruno Castro da Silva",
        "doi": "10.1145/3743127",
        "url": "https://dl.acm.org/doi/10.1145/3743127",
        "external_pdf": "https://dl.acm.org/doi/pdf/10.1145/3743127",
        "publication": "ACM Computing Surveys",
        "type": "journalArticle",
        "abstract": "This paper addresses the challenge of aligning large language models with human preferences, with reinforcement learning from human feedback (RLHF) as a promising solution. The article analyzes RLHF through reinforcement learning principles, focusing on the reward model, examining modeling choices and function approximation caveats, and revealing limitations like incorrect generalization, model misspecification, and sparse feedback.",
        "key_contribution": "Comprehensive critical analysis of RLHF revealing limitations and reward model issues",
        "significance": "Systematic review exposing RLHF challenges including reward hacking and misspecification",
        "newtags": "RLHF, Reward Modeling, Value Alignment",
    },
    {
        "filename": "2023-Dai-Safe RLHF.md",
        "short_title": "Safe RLHF",
        "year": 2023,
        "first_author": "Josef Dai",
        "authors": "Josef Dai; Xuehai Pan; Ruiyang Sun; Jiaming Ji; Xinbo Xu; Mickel Liu; Yizhou Wang; Yaodong Yang",
        "doi": "10.48550/arXiv.2310.12773",
        "url": "https://arxiv.org/abs/2310.12773",
        "external_pdf": "https://arxiv.org/pdf/2310.12773.pdf",
        "publication": "arXiv",
        "type": "preprint",
        "abstract": "This research addresses the challenge of balancing AI system performance with safety in large language models. The authors propose Safe RLHF, an algorithm that explicitly decouples human preferences regarding helpfulness and harmlessness by training separate reward and cost models. The approach formalizes safety as a constrained optimization problem and employs the Lagrangian method to dynamically balance these competing objectives during model fine-tuning.",
        "key_contribution": "Proposes Safe RLHF that decouples helpfulness and harmlessness with separate models",
        "significance": "Addresses the tension between helpfulness and safety in RLHF alignment",
        "newtags": "RLHF, AI Safety, Constrained Optimization",
    },
    {
        "filename": "2025-Tennant-Moral Intrinsic Rewards for Alignment.md",
        "short_title": "Moral Intrinsic Rewards for Alignment",
        "year": 2025,
        "first_author": "Elizaveta Tennant",
        "authors": "Elizaveta Tennant; Stephen Hailes; Mirco Musolesi",
        "doi": "N/A",
        "url": "https://openreview.net/forum?id=ZFk4eh0WcL",
        "external_pdf": "https://openreview.net/pdf?id=ZFk4eh0WcL",
        "publication": "ICLR Workshop",
        "type": "conferencePaper",
        "abstract": "The paper introduces intrinsic reward functions that explicitly encode core human values for automated Reinforcement Learning-based fine-tuning of foundation agent models. As an initial implementation, the paper evaluates training using the traditional philosophical frameworks of Deontological Ethics and Utilitarianism, quantifying moral rewards for agents in terms of actions and consequences on the Iterated Prisoner's Dilemma environment.",
        "key_contribution": "Introduces intrinsic reward functions encoding deontological and utilitarian ethics for RL",
        "significance": "Proposes transparent alternative to RLHF using explicit ethical frameworks",
        "newtags": "Utilitarianism, Deontology, Intrinsic Rewards, RL",
    },
    {
        "filename": "2025-Baum-Aggregation Problems Machine Ethics.md",
        "short_title": "Aggregation Problems Machine Ethics",
        "year": 2025,
        "first_author": "Kevin Baum",
        "authors": "Kevin Baum; Marija Slavkovik",
        "doi": "10.1609/aies.v8i1.36554",
        "url": "https://ojs.aaai.org/index.php/AIES/article/view/36554",
        "external_pdf": "https://ojs.aaai.org/index.php/AIES/article/download/36554/38692/40629",
        "publication": "AAAI/ACM Conference on AI, Ethics, and Society",
        "type": "conferencePaper",
        "abstract": "The paper discusses theoretical challenges of combining conflicting human moral judgments into coherent AI behavior. The core idea examined is the use of aggregation procedures to synthesize diverse moral preferences or judgments into actionable system behavior, with these approaches aiming to accommodate normative diversity without presupposing agreement on one comprehensive moral theory.",
        "key_contribution": "Analyzes aggregation approaches for synthesizing diverse moral judgments in AI",
        "significance": "Addresses how to combine conflicting utilitarian and non-utilitarian preferences",
        "newtags": "Utilitarianism, Moral Aggregation, Value Pluralism",
    },
    {
        "filename": "2025-Kneer-Hard Problem AI Alignment Value Forks.md",
        "short_title": "Hard Problem AI Alignment Value Forks",
        "year": 2025,
        "first_author": "Markus Kneer",
        "authors": "Markus Kneer; Juri Viehoff",
        "doi": "10.1145/3715275.3732174",
        "url": "https://dl.acm.org/doi/10.1145/3715275.3732174",
        "external_pdf": "https://philarchive.org/archive/KNETHP",
        "publication": "ACM FAccT",
        "type": "conferencePaper",
        "abstract": "In this article, we report findings from a series of experiments (N=1029) intended to establish whether agent-type (Human vs. AI) matters for what should be done in moral trade-offs. We find that, relative to a human decision-maker, participants more often judge that AI agents should opt for fairness at the expense of maximizing utility. Aligning AI with human values may require that an AI act differently from what a human agent should do, even when facing the exact same dilemma.",
        "key_contribution": "Empirically demonstrates value forks between human and AI agents in moral trade-offs",
        "significance": "Shows AI may need different ethical standards than humans, complicating alignment",
        "newtags": "Utilitarianism, Value Alignment, Fairness",
    },
    {
        "filename": "2025-Sun-Axiology AI Ethics MCDA.md",
        "short_title": "Axiology AI Ethics MCDA",
        "year": 2025,
        "first_author": "Fei Sun",
        "authors": "Fei Sun; Damir Isovic; Gordana Dodig-Crnkovic",
        "doi": "10.3390/proceedings2025126017",
        "url": "https://www.mdpi.com/2504-3900/126/1/17",
        "external_pdf": "https://www.mdpi.com/2504-3900/126/1/17/pdf",
        "publication": "Proceedings (MDPI)",
        "type": "conferencePaper",
        "abstract": "The fast advancement of artificial intelligence presents ethical challenges that exceed the scope of traditional moral theories. This paper proposes a value-centered framework for AI ethics grounded in axiology, which distinguishes intrinsic values like dignity and fairness from instrumental ones such as accuracy and efficiency. Using Multi-Criteria Decision Analysis (MCDA), the framework translates values into structured evaluations, enabling transparent trade-offs.",
        "key_contribution": "Proposes axiological framework using MCDA to integrate multiple ethical theories",
        "significance": "Enables structured trade-offs between utilitarian and non-utilitarian values",
        "newtags": "Utilitarianism, Axiology, MCDA, Value Framework",
    },
    {
        "filename": "2019-Aliman-Requisite Variety Ethical Utility Functions.md",
        "short_title": "Requisite Variety Ethical Utility Functions",
        "year": 2019,
        "first_author": "Nadisha-Marie Aliman",
        "authors": "Nadisha-Marie Aliman; Leon Kester",
        "doi": "10.48550/arXiv.1907.00430",
        "url": "https://arxiv.org/abs/1907.00430",
        "external_pdf": "https://arxiv.org/pdf/1907.00430.pdf",
        "publication": "arXiv",
        "type": "preprint",
        "abstract": "This work addresses value alignment in AI safety by examining how ethical utility functions should reflect the complexity of human moral intuitions. The authors conduct a transdisciplinary analysis drawing on neuroscience and psychology to assess moral variety, then propose that for the utility function of an AI not to violate human ethical intuitions, it trivially has to be a model of these intuitions. They integrate augmented utilitarianism as an ethical framework.",
        "key_contribution": "Proposes augmented utilitarianism for AI utility functions based on moral intuitions",
        "significance": "Addresses variety requirements for ethical utility functions in value alignment",
        "newtags": "Utilitarianism, Utility Functions, Value Alignment",
    },
    {
        "filename": "2023-Boddington-Normative Ethical Theory AI Ethics.md",
        "short_title": "Normative Ethical Theory AI Ethics",
        "year": 2023,
        "first_author": "Paula Boddington",
        "authors": "Paula Boddington",
        "doi": "10.1007/978-981-19-9382-4_6",
        "url": "https://link.springer.com/chapter/10.1007/978-981-19-9382-4_6",
        "external_pdf": "N/A",
        "publication": "AI Ethics (Springer)",
        "type": "bookChapter",
        "abstract": "Normative ethical theories propose frameworks for determining value and for guiding judgment and action. The chapter examines three dominant varieties: consequentialism, focusing on outcomes of actions; deontology, focusing on the nature of actions themselves; and virtue ethics, focusing on the moral character of the agent. The application of ethical theories to situations of rapidly changing technology presents many challenges.",
        "key_contribution": "Comprehensive overview of consequentialism, deontology, and virtue ethics for AI",
        "significance": "Foundational chapter on applying normative ethics to AI systems",
        "newtags": "Utilitarianism, Deontology, Virtue Ethics, Normative Ethics",
    },
    {
        "filename": "2025-Vishwanath-Machine Ethics or AI Alignment.md",
        "short_title": "Machine Ethics or AI Alignment",
        "year": 2025,
        "first_author": "Ajay Vishwanath",
        "authors": "Ajay Vishwanath; Marija Slavkovik",
        "doi": "N/A",
        "url": "https://ceur-ws.org/Vol-3975/paper9.pdf",
        "external_pdf": "https://ceur-ws.org/Vol-3975/paper9.pdf",
        "publication": "CEUR Workshop Proceedings",
        "type": "conferencePaper",
        "abstract": "AI, in its current form, can be argued to be utilitarian (a form of consequentialism), by design. In supervised learning, an objective function is optimized to maximize accuracy or minimize error in predictions, while in reinforcement learning, a reward function is maximized. This paper examines the relationship between Machine Ethics and AI Alignment fields and their approaches to ethical AI.",
        "key_contribution": "Argues AI is inherently utilitarian by design due to optimization objectives",
        "significance": "Clarifies relationship between machine ethics and alignment approaches",
        "newtags": "Utilitarianism, Machine Ethics, AI Alignment",
    },
    {
        "filename": "2023-Stenseke-Use and Abuse Normative Ethics Moral Machines.md",
        "short_title": "Use and Abuse Normative Ethics Moral Machines",
        "year": 2023,
        "first_author": "Jakob Stenseke",
        "authors": "Jakob Stenseke",
        "doi": "10.3233/FAIA220614",
        "url": "https://ebooks.iospress.nl/doi/10.3233/FAIA220614",
        "external_pdf": "N/A",
        "publication": "Social Robots in Social Institutions (IOS Press)",
        "type": "bookChapter",
        "abstract": "The paper asks how we develop AI systems that adhere to human norms and values, and whether it's promising to develop systems based on normative frameworks such as consequentialism, deontology, or virtue ethics. While many machine ethics researchers answer yes, the author challenges this methodological strategy by exploring the difference between normative ethics in human practices versus machines.",
        "key_contribution": "Critiques applying normative frameworks directly to machines",
        "significance": "Argues machines lack resources to justify normative theory use",
        "newtags": "Utilitarianism, Deontology, Machine Ethics, Normative Ethics",
    },
    {
        "filename": "2020-Della Foresta-Consequentialism Machine Ethics.md",
        "short_title": "Consequentialism Machine Ethics",
        "year": 2020,
        "first_author": "Josiah Della Foresta",
        "authors": "Josiah Della Foresta",
        "doi": "N/A",
        "url": "https://montrealethics.ai/consequentialism-and-machine-ethics-towards-a-foundational-machine-ethic-to-ensure-the-ethical-conduct-of-artificial-moral-agents/",
        "external_pdf": "N/A",
        "publication": "Montreal AI Ethics Institute",
        "type": "report",
        "abstract": "This paper argues that Consequentialism represents a kind of ethical theory that is the most plausible to serve as a basis for a machine ethic. The paper outlines the concept of an artificial moral agent and the essential properties of Consequentialism, presents a scenario involving autonomous vehicles, evaluates a Deontological approach, and discusses the problem of moral conflict. The monism of Consequentialism ensures that moral conflicts cannot arise.",
        "key_contribution": "Argues consequentialism is most suitable foundation for machine ethics",
        "significance": "Demonstrates algorithmic nature of consequentialism for AMAs",
        "newtags": "Utilitarianism, Consequentialism, Artificial Moral Agents",
    },
    {
        "filename": "2025-Benavoli-AI Safety Uncertainty Incomplete Preferences.md",
        "short_title": "AI Safety Uncertainty Incomplete Preferences",
        "year": 2025,
        "first_author": "Alessio Benavoli",
        "authors": "Alessio Benavoli; Alessandro Facchini; Marco Zaffalon",
        "doi": "10.48550/arXiv.2512.23508",
        "url": "https://arxiv.org/abs/2512.23508",
        "external_pdf": "https://arxiv.org/pdf/2512.23508.pdf",
        "publication": "arXiv",
        "type": "preprint",
        "abstract": "The paper addresses AI safety through two problem frameworks: the AI assistance game and the AI shutdown game. It examines how to design AI agents that learn human utility functions and how to create systems that respect shutdown commands without interference. The authors argue that addressing these challenges requires AI agents that can reason under uncertainty and handle both incomplete and non-Archimedean preferences.",
        "key_contribution": "Argues AI safety requires uncertainty handling and non-standard preference representations",
        "significance": "Proposes alternatives to standard expected utility for safe AI assistance",
        "newtags": "Utilitarianism, AI Safety, Utility Theory, Preferences",
    },
]


def generate_paper_content(paper):
    """Generate the full markdown content for a paper."""

    # Build frontmatter
    frontmatter = f'''---


Human View:
Human View Date:
Human View note:
Not AI:
key:
type: {paper["type"]}
short_title: "{paper["short_title"]}"
year: {paper["year"]}
first_author: "[[{paper["first_author"]}]]"
authors: "{paper["authors"]}"
doi: {paper["doi"]}
url: "{paper["url"]}"
external_pdf: "{paper["external_pdf"]}"
publication: {paper["publication"]}
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: {paper["newtags"]}
key_contribution: "{paper["key_contribution"]}"
significance: "{paper["significance"]}"
tags:
pdf_extract: "PDF Extracts/{paper["filename"].replace(".md", "")}.md"
abstract: "{paper["abstract"][:500]}..."
paper_summary:
local_pdf: "[[PDFs/{paper["filename"].replace(".md", ".pdf")}]]"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "Yes"
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
data_description: "N/A"
data_metrics: "Not specified"
---
'''

    # Parse authors for wikilinks
    author_list = paper["authors"].split("; ")
    author_wikilinks = ", ".join([f"[[{a.strip()}]]" for a in author_list])

    # Build body
    body = f'''# {paper["short_title"]}

## Metadata

**Authors:** {paper["authors"]}

**Year:** {paper["year"]}

**Type:** {paper["type"]}

**DOI:** [{paper["doi"]}](https://doi.org/{paper["doi"]})

**Publisher:** {paper["publication"]}

## Links

- **Local PDF:** [[PDFs/{paper["filename"].replace(".md", ".pdf")}|Open PDF]]

- **URL:** {paper["url"]}
- **DOI:** https://doi.org/{paper["doi"]}

## Abstract

{paper["abstract"]}

## Authors

{author_wikilinks}

## Key Contribution

{paper["key_contribution"]}

## Significance

{paper["significance"]}

## Notes



## Tags

#{paper["newtags"].replace(", ", " #").replace(" ", "-")}

## Citation Info

'''

    return frontmatter + body


def main():
    papers_dir = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers")

    created = []
    skipped = []

    for paper in papers:
        filepath = papers_dir / paper["filename"]

        if filepath.exists():
            skipped.append(paper["filename"])
            continue

        content = generate_paper_content(paper)
        filepath.write_text(content, encoding="utf-8")
        created.append(paper["filename"])
        print(f"Created: {paper['filename']}")

    print(f"\n=== Summary ===")
    print(f"Created: {len(created)} papers")
    print(f"Skipped (already exist): {len(skipped)}")

    if skipped:
        print(f"\nSkipped files:")
        for f in skipped:
            print(f"  - {f}")

    return created


if __name__ == "__main__":
    main()
