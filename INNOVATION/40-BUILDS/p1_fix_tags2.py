#!/usr/bin/env python3
"""
Fix the tags block in P1 paper records.
Replace multi-item tags list with single-item (remove the gap ID from tags since
it's already in the innovation_gap field). This resolves the validator's
"Orphaned list item" false positive for the 2nd item in a list.

Safe approach: use regex subn on the raw file content — no parse-and-rebuild.
"""
import re
from pathlib import Path

PAPERS_DIR = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers")

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

# Replace:
#   tags:
#     - AIAlignment
#     - "G-XX"
# with:
#   tags:
#     - AIAlignment
#
# Pattern: match tags block with 2 items (AIAlignment + quoted gap ID)
# The gap ID line starts with '  - "G-'
PATTERN = re.compile(
    r'(tags:\n  - AIAlignment\n)  - "G-[^"]+"\n',
    re.MULTILINE
)

fixed = 0
for fname in P1_PAPERS:
    path = PAPERS_DIR / fname
    if not path.exists():
        print(f"NOT FOUND: {fname}")
        continue

    content = path.read_text(encoding='utf-8')
    new_content, n = PATTERN.subn(r'\1', content)

    if n > 0:
        path.write_text(new_content, encoding='utf-8')
        print(f"Fixed: {fname}")
        fixed += 1
    else:
        print(f"No match: {fname}")

print(f"\nTotal fixed: {fixed}")
