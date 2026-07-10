#!/usr/bin/env python3
"""
Rename P1 paper files to proper vault naming convention:
YYYY-FirstAuthorSurname-Short Title
Updates paper records, PDF files, extract files, and internal wikilinks.
"""
import re
import shutil
from pathlib import Path

VAULT_ROOT = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS")
PDFS_DIR = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs")
PAPERS_DIR = VAULT_ROOT / "papers"
EXTRACTS_DIR = VAULT_ROOT / "PDF Extracts"

# (old_stem, new_stem) pairs — only for those needing rename
RENAMES = [
    # P1-02: Persona Vectors — actual first author is Runjin Chen
    (
        "2025-Anthropic-Persona Vectors",
        "2025-Chen-Persona Vectors",
    ),
    # P1-03: Persona Features — actual first author is Miles Wang
    (
        "2025-OpenAI-Persona Features Control EM",
        "2025-Wang-Persona Features Control EM",
    ),
    # P1-04: Natural EM — actual first author is Monte MacDiarmid
    (
        "2025-Anthropic-Natural EM from Reward Hacking",
        "2025-MacDiarmid-Natural EM from Reward Hacking",
    ),
    # P1-05: SpecEval — first author Ahmed Ahmed
    (
        "2025-SpecEval",
        "2025-Ahmed-SpecEval",
    ),
    # P1-06: Stress-Testing — first author Jifan Zhang
    (
        "2025-Stress-Testing Model Specifications",
        "2025-Zhang-Stress-Testing Model Specifications",
    ),
    # P1-07: Peer-Prediction — first author Tianyi Alex Qiu
    (
        "2026-Peer-Prediction Scalable Oversight",
        "2026-Qiu-Peer-Prediction Scalable Oversight",
    ),
    # P1-08: Confirmation Bias — first author Gabriel Recchia
    (
        "2025-Confirmation Bias in LLM Oversight",
        "2025-Recchia-Confirmation Bias in LLM Oversight",
    ),
    # P1-09: AI Debaters — first author María Carro
    (
        "2025-AI Debaters Own Beliefs Bias",
        "2025-Carro-AI Debaters Own Beliefs Bias",
    ),
    # P1-10: Social Choice survey — first author Daniel Halpern
    (
        "2026-Social Choice for AI Alignment Survey",
        "2026-Halpern-Social Choice for AI Alignment Survey",
    ),
    # P1-12: CoT Monitorability — first author Tomek Korbak
    (
        "2025-CoT Monitorability",
        "2025-Korbak-CoT Monitorability",
    ),
    # P1-13: Eval-Design — first author Katharina Deckenbach
    (
        "2026-Eval-Design Awareness Safer Scores",
        "2026-Deckenbach-Eval-Design Awareness Safer Scores",
    ),
    # P1-14: Value-Conflict — first author Inderjeet Nair
    (
        "2026-Value-Conflict Diagnostics for Faking",
        "2026-Nair-Value-Conflict Diagnostics for Faking",
    ),
    # P1-15: Utility-Behavior Gap — first author Yujun Zhou
    (
        "2026-Utility-Behavior Gap",
        "2026-Zhou-Utility-Behavior Gap",
    ),
    # P1-16: Subliminal Learning — first author Alex Cloud
    (
        "2025-Subliminal Learning",
        "2025-Cloud-Subliminal Learning",
    ),
    # P1-17: SSGM — first author Chingkwun Lam
    (
        "2026-SSGM Memory-Drift Governance",
        "2026-Lam-SSGM Memory-Drift Governance",
    ),
]


def get_year(stem):
    return int(stem.split("-")[0])


def rename_all():
    print("=" * 60)
    print("P1 File Rename — Vault Naming Convention Fix")
    print("=" * 60)

    for old_stem, new_stem in RENAMES:
        year = get_year(old_stem)
        print(f"\n{old_stem}")
        print(f"  → {new_stem}")

        # Paper .md
        old_paper = PAPERS_DIR / f"{old_stem}.md"
        new_paper = PAPERS_DIR / f"{new_stem}.md"

        # PDF
        old_pdf = PDFS_DIR / str(year) / f"{old_stem}.pdf"
        new_pdf = PDFS_DIR / str(year) / f"{new_stem}.pdf"

        # Extract
        old_extract = EXTRACTS_DIR / str(year) / f"{old_stem}.md"
        new_extract = EXTRACTS_DIR / str(year) / f"{new_stem}.md"

        # Rename PDF
        if old_pdf.exists():
            old_pdf.rename(new_pdf)
            print(f"  PDF renamed: {new_pdf.name}")
        elif new_pdf.exists():
            print(f"  PDF already at: {new_pdf.name}")
        else:
            print(f"  PDF NOT FOUND: {old_pdf}")

        # Rename extract
        if old_extract.exists():
            # Update the source_pdf wikilink inside extract
            content = old_extract.read_text(encoding='utf-8')
            old_wikilink = f"[[Lit-WS-PDFs/{year}/{old_stem}.pdf]]"
            new_wikilink = f"[[Lit-WS-PDFs/{year}/{new_stem}.pdf]]"
            content = content.replace(old_wikilink, new_wikilink)
            old_extract.write_text(content, encoding='utf-8')
            old_extract.rename(new_extract)
            print(f"  Extract renamed: {new_extract.name}")
        elif new_extract.exists():
            print(f"  Extract already at: {new_extract.name}")
        else:
            print(f"  Extract NOT FOUND: {old_extract}")

        # Rename paper record + update internal links
        if old_paper.exists():
            content = old_paper.read_text(encoding='utf-8')
            # Update local_pdf wikilink
            old_pdf_link = f"[[Lit-WS-PDFs/{year}/{old_stem}.pdf]]"
            new_pdf_link = f"[[Lit-WS-PDFs/{year}/{new_stem}.pdf]]"
            content = content.replace(old_pdf_link, new_pdf_link)
            # Update pdf_extract path
            old_extract_path = f"PDF Extracts/{year}/{old_stem}.md"
            new_extract_path = f"PDF Extracts/{year}/{new_stem}.md"
            content = content.replace(old_extract_path, new_extract_path)
            old_paper.write_text(content, encoding='utf-8')
            old_paper.rename(new_paper)
            print(f"  Paper renamed: {new_paper.name}")
        elif new_paper.exists():
            print(f"  Paper already at: {new_paper.name}")
        else:
            print(f"  Paper NOT FOUND: {old_paper}")

    print("\nDone.")


if __name__ == "__main__":
    rename_all()
