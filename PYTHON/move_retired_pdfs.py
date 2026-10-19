#!/usr/bin/env python3
"""Move the PDFs of notes retired or unlinked on 2026-10-18/19 into the PDF folder's RECYCLE-BIN.

The PDF folder lives outside the repo (see .vault-config.json / VAULT_PDF_PATH), so the
2026-10-18/19 cleanup could not move these files itself:

- 2 duplicates retired by the duplicate merge (logs/20261018-duplicate-merge.md)
- 3 PDFs that were a different paper than their note (logs/20261018-junk-abstracts.md)
- 1 more wrong paper and 2 ScienceDirect error pages (logs/20261019-small-data-fixes.md)
- 1 wrong paper under a retired duplicate note (logs/20261019b-followup-fixes.md)

Each file is looked up by name anywhere under the PDF folder (stray copies in subfolders
included) and moved, never deleted, to <PDF folder>/RECYCLE-BIN/20261018-retired-pdfs/,
keeping its path relative to the PDF folder.

Usage (from the vault root):
    python3 PYTHON/move_retired_pdfs.py            # dry run: list what would move
    python3 PYTHON/move_retired_pdfs.py --apply    # move
"""
import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / ".agent"))

RETIRED = {
    "2025-Sun-Decoding Moral Responses in AI A Quantitative Analysis of Large.pdf":
        "duplicate merge: the SocialSense paper filed under another title (note retired)",
    "2025-Snoswell-Beyond Verdicts Evaluating Language Model Moral Competence Aaron J..pdf":
        "duplicate merge: duplicate of the kept Snoswell note",
    "2024-Kajiwara-Hate Speech Dataset Catalogue hatespeechdata.pdf":
        "wrong paper: AbuseEval v1.0 (Caselli et al., LREC 2020), not the catalogue website",
    "2025-Unknown-Is ChatGPT A Good Translator A Preliminary Study.pdf":
        "wrong paper: 'Is ChatGPT a Good NLG Evaluator?' (Wang et al. 2023)",
    "2024-Kajiwara-A curated dataset for hate speech detection on social media text - PMC.pdf":
        "wrong paper: gender bias in chemical NER (Zhao et al., arXiv 2212.12799)",
    "2024-Conitzer-Social Choice for AI Alignment.pdf":
        "wrong paper: arXiv 2404.10000, DC Stark resonances for the ammonia molecule (Pirkola & Horbatsch)",
    "2025-Hui-Decoding Moral Responses in AI.pdf":
        "not a paper: ScienceDirect error page",
    "2022-Zhang-Artificial Intelligence and Moral Dilemmas.pdf":
        "not a paper: ScienceDirect error page",
    "2022-Mhlambi-The role of the African value of Ubuntu in global AI inclusion.pdf":
        "wrong paper (Saloojee & Saloojee 2011, social inclusion); its note was retired as a duplicate of Gwagwa et al.",
    "2025-Xiong-BuddhismEval Bilingual Evaluation Benchmark for Buddhist.pdf":
        "wrong paper: an education encyclopedia index; its note was retired as a duplicate of the kept BuddhismEval note",
    "2025-Ogunremi-1 Decolonizing NLP for “Low-resource Languages”.pdf":
        "duplicate merge: same GRACE article as the kept 2023-Ògúnrẹ̀mí note",
}
DEST = Path("RECYCLE-BIN") / "20261018-retired-pdfs"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--apply", action="store_true", help="move the files (default: dry run)")
    args = ap.parse_args()

    from lib import config  # needs .vault-config.json or VAULT_PDF_PATH, like other vault tools
    base = Path(config.PDFS_DIR)
    if not base.is_dir():
        sys.exit(f"PDF folder not found: {base}")
    print(f"PDF folder: {base}")

    found = 0
    for name, why in RETIRED.items():
        hits = [p for p in base.rglob(name) if DEST.parts[0] not in p.relative_to(base).parts]
        if not hits:
            print(f"  not found: {name}")
            continue
        for src in hits:
            rel = src.relative_to(base)
            dst = base / DEST / rel
            found += 1
            print(f"  {'move' if args.apply else 'would move'}: {rel}\n      -> {DEST / rel}   ({why})")
            if args.apply:
                if dst.exists():
                    sys.exit(f"refusing to overwrite {dst}")
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(src), str(dst))
    print(f"{'Moved' if args.apply else 'Dry run:'} {found} file(s).")
    if not args.apply and found:
        print("Run again with --apply to move them.")


if __name__ == "__main__":
    main()
