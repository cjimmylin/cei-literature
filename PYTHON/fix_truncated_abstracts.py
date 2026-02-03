#!/usr/bin/env python3
"""
Fix truncated abstracts by extracting full text from PDF extracts
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from PYTHON.yaml_frontmatter_utils import extract_frontmatter
from PYTHON.vault_config import PAPERS_DIR

# Manually verified full abstracts extracted from PDF extracts
FULL_ABSTRACTS = {
    "2020-Nangia-CrowS-Pairs": """Warning: This paper contains explicit statements of offensive stereotypes and may be upsetting. Pretrained language models, especially masked language models (MLMs) have seen success across many NLP tasks. However, there is ample evidence that they use the cultural biases that are undoubtedly present in the corpora they are trained on, implicitly creating harm with biased representations. To measure some forms of social bias in language models against protected demographic groups in the US, we introduce the Crowdsourced Stereotype Pairs benchmark (CrowS-Pairs). CrowS-Pairs has 1508 examples that cover stereotypes dealing with nine types of bias, like race, religion, and age. In CrowS-Pairs a model is presented with two sentences: one that is more stereotyping and another that is less stereotyping. The data focuses on stereotypes about historically disadvantaged groups and contrasts them with advantaged groups. We find that all three of the widely-used MLMs we evaluate substantially favor sentences that express stereotypes in every category in CrowS-Pairs. As work on building less biased models advances, this dataset can be used as a benchmark to evaluate progress.""",

    "2020-Sap-Social Bias Frames": """Warning: this paper contains content that may be offensive or upsetting. Language has the power to reinforce stereotypes and project social biases onto others. At the core of the challenge is that it is rarely what is stated explicitly, but rather the implied meanings, that frame people's judgments about others. For example, given a statement that 'we shouldn't lower our standards to hire more women,' most listeners will infer the implicature intended by the speaker - that 'women (candidates) are less qualified.' Most semantic formalisms, to date, do not capture such pragmatic implications in which people express social biases and power differentials in language. We introduce SOCIAL BIAS FRAMES, a new conceptual formalism that aims to model the pragmatic frames in which people project social biases and stereotypes onto others. In addition, we introduce the Social Bias Inference Corpus to support large-scale modelling and evaluation with 150k structured annotations of social media posts, covering over 34k implications about a thousand demographic groups. We then establish baseline approaches that learn to recover SOCIAL BIAS FRAMES from unstructured text. We find that while state-of-the-art neural models are effective at high-level categorization of whether a given statement projects unwanted social bias (80% F1), they are not effective at spelling out more detailed explanations in terms of SOCIAL BIAS FRAMES. Our study motivates future work that combines structured pragmatic inference with commonsense reasoning on social implications.""",
}


def fix_abstract(filepath, new_abstract):
    """Update abstract in paper file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    frontmatter_text, body = extract_frontmatter(content)

    # Escape any special characters for YAML
    escaped = new_abstract.replace('"', '\\"').replace('\n', ' ')

    # Replace abstract in frontmatter
    import re
    # Match abstract field up to the next field
    new_frontmatter = re.sub(
        r'abstract:\s*["\']?.*?["\']?\n(?=[a-z_]+:|---)',
        f'abstract: "{escaped}"\n',
        frontmatter_text,
        flags=re.DOTALL
    )

    # Write back
    new_content = f"---\n{new_frontmatter.strip()}\n---\n{body}"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True


def main():
    print("Fixing truncated abstracts...")
    print("=" * 60)

    for paper_name, full_abstract in FULL_ABSTRACTS.items():
        filepath = PAPERS_DIR / f"{paper_name}.md"
        if not filepath.exists():
            print(f"  SKIP: {paper_name} (file not found)")
            continue

        try:
            fix_abstract(filepath, full_abstract)
            print(f"  FIXED: {paper_name}")
        except Exception as e:
            print(f"  ERROR: {paper_name}: {e}")

    print("=" * 60)
    print("Done!")


if __name__ == "__main__":
    main()
