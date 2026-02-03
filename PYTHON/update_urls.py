#!/usr/bin/env python3
"""Update markdown files with found URLs for papers missing them."""

from pathlib import Path

from vault_config import PAPERS_DIR

# URLs found for papers that were missing them
FOUND_URLS = {
    "RNDCEFC4": {  # McBE
        "arxiv": "https://arxiv.org/abs/2507.02088",
        "acl": "https://aclanthology.org/2025.findings-acl.313/"
    },
    "BY3E46VS": {  # SHADES
        "acl": "https://aclanthology.org/2025.naacl-long.600/",
        "openreview": "https://openreview.net/forum?id=zSwnz6BsDa"
    },
    "MAHWYKT8": {  # Multi-Dimensional View of Aggression
        "acl": "https://aclanthology.org/2020.trac-1.3/",
        "semantic_scholar": "https://www.semanticscholar.org/paper/A-Multi-Dimensional-View-of-Aggression-when-voicing-Srivastava-Vajpayee/22428dc028d3d953e4722f16af4512e2592cdf58"
    },
    "2IXQNVL4": {  # Trolley Problem for AI
        "aaai": "https://ojs.aaai.org/index.php/AAAI-SS/article/view/35590",
        "researchgate": "https://www.researchgate.net/publication/392180946"
    },
    "JALT756H": {  # Automated Classification of Moral Reasoning
        "ssrn": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3205286",
        "semantic_scholar": "https://www.semanticscholar.org/paper/Automated-Classification-of-Modes-of-Moral-in-Ash-Chen/d4eaffcc771de90d51d9052cbe6a17c9121a9a4d"
    },
    "MTV37PE2": {  # Iranian Social Norms
        "arxiv": "https://arxiv.org/abs/2406.09123",
        "acl": "https://aclanthology.org/2025.findings-naacl.337/"
    },
    "QURKVCVW": {  # MedEthicEval
        "arxiv": "https://arxiv.org/abs/2503.02374",
        "acl": "https://aclanthology.org/2025.naacl-industry.34/"
    },
    "G6BN8ZME": {  # Ethicsophical Landscape - not found
    },
    "RSLK7KS9": {  # Towards Theory-based Moral AI
        "arxiv": "https://arxiv.org/abs/2306.11432",
        "ceur": "https://ceur-ws.org/Vol-3547/paper3.pdf"
    },
    "SRKAQM3X": {  # GermEval 2019
        "semantic_scholar": "https://www.semanticscholar.org/paper/Overview-of-GermEval-Task-2,-2019-Shared-Task-on-of-Stru%C3%9F-Siegel/f8e9851f175d9f8b87201118906b39f5491041b1",
        "researchgate": "https://www.researchgate.net/publication/337441720"
    },
    "JCYY44E4": {  # Survey of LLMs in Medicine
        "arxiv": "https://arxiv.org/abs/2311.05112",
        "semantic_scholar": "https://www.semanticscholar.org/paper/A-Survey-of-Large-Language-Models-in-Medicine:-and-Zhou-Gu/bca0bbd01ea917b7a9fe369288ea3ba03d3b1ff3"
    },
    "4YDBJ27I": {  # Ten Hard Problems in AI
        "arxiv": "https://arxiv.org/abs/2402.04464",
        "semantic_scholar": "https://www.semanticscholar.org/paper/Ten-Hard-Problems-in-Artificial-Intelligence-We-Get-Leech-Garfinkel/dcd2f0156d89619c622431cffa0b9c2e01c631a0"
    },
    "RL573MSX": {  # Frontier AI Ethics
        "arxiv": "https://arxiv.org/abs/2404.06750"
    },
    "3RNRAN7W": {  # Ethics Whitepaper
        "arxiv": "https://arxiv.org/abs/2410.19812",
        "github": "https://github.com/MxEddie/Ethics-Whitepaper"
    },
    "HRXS9ILQ": {  # Technical Risks of LAWS
        "arxiv": "https://arxiv.org/abs/2502.10174",
        "researchgate": "https://www.researchgate.net/publication/389056163"
    },
    "ZCHG4W4T": {  # Contemplative AI
        "arxiv": "https://arxiv.org/abs/2504.15125",
        "semantic_scholar": "https://www.semanticscholar.org/paper/Contemplative-Artificial-Intelligence-Laukkonen-Inglis/823a6f37db9d18ec4fdfaf02e01400c5ec6c0ab9"
    },
    "XWUV45S3": {  # Speciesism in AI
        "arxiv": "https://arxiv.org/abs/2508.11534"
    },
    "8HB8V7WZ": {  # Approval Regulation of Frontier AI
        "arxiv": "https://arxiv.org/abs/2408.06210",
        "semantic_scholar": "https://www.semanticscholar.org/paper/Certified-Safe:-A-Schematic-for-Approval-Regulation-Salvador/73225354b43308acff62d0aa6358234cd97a4042"
    },
    "VVVLTVIR": {  # VisAlign
        "arxiv": "https://arxiv.org/abs/2308.01525",
        "neurips": "https://neurips.cc/virtual/2023/poster/73563",
        "github": "https://github.com/jiyounglee-0523/VisAlign"
    },
    "JRW7RCQN": {  # FairMT-Bench
        "arxiv": "https://arxiv.org/abs/2410.19317",
        "openreview": "https://openreview.net/forum?id=RSGoXnS9GH",
        "github": "https://github.com/FanZT6/FairMT-bench"
    },
    "7FLQPGMT": {  # T2ISafety
        "arxiv": "https://arxiv.org/abs/2501.12612",
        "cvpr": "https://openaccess.thecvf.com/content/CVPR2025/html/Li_T2ISafety_Benchmark_for_Assessing_Fairness_Toxicity_and_Privacy_in_Image_CVPR_2025_paper.html",
        "github": "https://github.com/adwardlee/t2i_safety"
    },
    "GHNYTYDF": {  # HELM Safety
        "stanford": "https://crfm.stanford.edu/2024/11/08/helm-safety.html",
        "leaderboard": "https://crfm.stanford.edu/helm/safety/latest/",
        "github": "https://github.com/stanford-crfm/helm"
    },
    "9WY3JY6S": {  # Africa Knows Conference / Ubuntu AI Ethics
        "conference": "https://nomadit.co.uk/conference/africaknows/paper/57969",
        "journal": "https://www.emerald.com/insight/content/doi/10.1108/JICES-04-2022-0037/full/html"
    },
    "ESZUEQJQ": {  # FACTS Grounding
        "arxiv": "https://arxiv.org/abs/2501.03200",
        "deepmind": "https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/"
    },
    "ABZUCNSW": {  # Mapping Moral Reasoning Circuits
        "springer": "https://link.springer.com/chapter/10.1007/978-3-031-93415-5_6",
        "github": "https://github.com/coairesearch/mapping_moral_reasoning"
    },
    "NCKQ4LJ6": {  # Ethical Decision-Making Five Domains
        "journal": "https://jisem-journal.com/index.php/journal/article/view/12555"
    },
    "FDB79D6M": {  # Characterizing AI Agents
        "arxiv": "https://arxiv.org/abs/2504.21848",
        "researchgate": "https://www.researchgate.net/publication/391328794"
    },
    "U6X9LC4B": {  # Religious Affiliation and Moral Domain
        "guilford": "https://guilfordjournals.com/doi/10.1521/soco.2021.39.1.139",
        "harvard": "https://scholar.harvard.edu/files/slevine/files/levine_et_al_2021_religion_and_morality.pdf"
    }
}

def find_markdown_file(papers_dir: Path, key: str):
    """Find the markdown file for a given Zotero key."""
    for md_file in papers_dir.glob("*.md"):
        content = md_file.read_text(encoding='utf-8')
        if f"key: {key}" in content:
            return md_file
    return None

def update_markdown_with_urls(filepath: Path, urls: dict) -> bool:
    """Update a markdown file with new URLs."""
    content = filepath.read_text(encoding='utf-8')

    # Check if there's already a Links section
    if "## Links" in content:
        return False  # Already has links

    # Build the links section
    links_section = "\n## Links\n\n"
    for source, url in urls.items():
        source_name = source.replace("_", " ").title()
        links_section += f"- **{source_name}:** {url}\n"

    # Insert before ## Notes section
    if "## Notes" in content:
        content = content.replace("## Notes", links_section + "\n## Notes")
    else:
        content += links_section

    filepath.write_text(content, encoding='utf-8')
    return True

def main():
    papers_dir = PAPERS_DIR

    updated = 0
    not_found = 0

    for key, urls in FOUND_URLS.items():
        if not urls:
            print(f"Skipping {key} - no URLs found")
            continue

        md_file = find_markdown_file(papers_dir, key)
        if md_file:
            if update_markdown_with_urls(md_file, urls):
                print(f"Updated: {md_file.name}")
                updated += 1
            else:
                print(f"Already has links: {md_file.name}")
        else:
            print(f"File not found for key: {key}")
            not_found += 1

    print(f"\nUpdated {updated} files")
    if not_found:
        print(f"Could not find {not_found} files")

if __name__ == "__main__":
    main()
