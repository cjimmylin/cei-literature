#!/usr/bin/env python3
"""
Fix the tags YAML in all 17 newly created P1 papers.
The issue: '  - G-20' is parsed as orphaned list item.
Fix: quote the gap tag so it's '  - "G-20"'.
"""
import re
from pathlib import Path

PAPERS_DIR = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers")

# All 17 new P1 paper filenames (final names after rename)
P1_PAPERS = [
    "2025-Betley-Emergent Misalignment.md",
    "2025-Chen-Persona Vectors.md",
    "2025-Wang-Persona Features Control EM.md",
    "2025-MacDiarmid-Natural EM from Reward Hacking.md",
    "2025-Ahmed-SpecEval.md",
    "2025-Zhang-Stress-Testing Model Specifications.md",
    "2026-Qiu-Peer-Prediction Scalable Oversight.md",
    "2025-Recchia-Confirmation Bias in LLM Oversight.md",
    "2025-Carro-AI Debaters Own Beliefs Bias.md",
    "2026-Halpern-Social Choice for AI Alignment Survey.md",
    "2026-Christian-RMs Inherit Value Biases.md",
    "2025-Korbak-CoT Monitorability.md",
    "2026-Deckenbach-Eval-Design Awareness Safer Scores.md",
    "2026-Nair-Value-Conflict Diagnostics for Faking.md",
    "2026-Zhou-Utility-Behavior Gap.md",
    "2025-Cloud-Subliminal Learning.md",
    "2026-Lam-SSGM Memory-Drift Governance.md",
]

def fix_tags_block(content):
    """
    Replace:
        tags:
          - AIAlignment
          - G-20
    with:
        tags:
          - AIAlignment
          - "G-20"

    More precisely: quote any list item under 'tags:' that contains a hyphen in the value.
    Use safe regex on the tags block only.
    """
    # Pattern: a list item line under tags that has a gap ID like G-20 or G-06/20
    # Match lines like "  - G-20" or "  - G-06/20" or "  - G-06-20"
    # These are inside the YAML frontmatter block (between --- delimiters)

    # Safe approach: use subn to replace only unquoted gap tags
    # Pattern: "^  - (G-\d+[/-]\d+)$" in multiline
    pattern = r'^  - (G-\d+(?:[/-]\d+)*)$'
    fixed, count = re.subn(pattern, r'  - "\1"', content, flags=re.MULTILINE)
    return fixed, count


fixed_count = 0
for fname in P1_PAPERS:
    path = PAPERS_DIR / fname
    if not path.exists():
        print(f"NOT FOUND: {fname}")
        continue

    content = path.read_text(encoding='utf-8')
    fixed, n = fix_tags_block(content)

    if n > 0:
        path.write_text(fixed, encoding='utf-8')
        print(f"Fixed {n} tag(s): {fname}")
        fixed_count += 1
    else:
        print(f"No change needed: {fname}")

print(f"\nFixed {fixed_count} files.")
