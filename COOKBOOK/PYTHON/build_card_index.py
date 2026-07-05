#!/usr/bin/env python3
"""
COOKBOOK Phase 2 prep — card index + theme routing.

Harvests the YAML frontmatter of every evidence card (paper + lab) into
20260705-card-index.json and inverts theme_tags into a theme -> [stems]
routing map used to assign cards to theme-dossier aggregators.
"""

import json
from datetime import datetime
from pathlib import Path

from validate_cards import CARDS_DIR, LAB_CARDS_DIR, EVIDENCE_DIR, VOCAB, parse_card

OUT = EVIDENCE_DIR / "20260705-card-index.json"


def harvest(directory: Path, kind: str):
    entries = {}
    for path in sorted(directory.glob("*.card.md")):
        front, body, issues = parse_card(path)
        stem = path.name[: -len(".card.md")]
        tags = front.get("theme_tags") or []
        if isinstance(tags, str):
            tags = [tags]
        entries[stem] = {
            "kind": kind,
            "path": str(path.relative_to(EVIDENCE_DIR.parent.parent)),
            "theme_tags": [t for t in tags if t in VOCAB],
            "is_benchmark": bool(front.get("is_benchmark", False)),
            "confidence": front.get("confidence"),
            "task_format": front.get("task_format"),
            "scoring_type": front.get("scoring_type"),
            "company": front.get("company"),
            "words": len(body.split()),
            "parse_issues": issues,
        }
    return entries

def main():
    cards = harvest(CARDS_DIR, "paper")
    cards.update(harvest(LAB_CARDS_DIR, "lab"))

    themes = {t: [] for t in sorted(VOCAB)}
    untagged = []
    for stem, e in cards.items():
        if e["theme_tags"]:
            for t in e["theme_tags"]:
                themes[t].append(stem)
        else:
            untagged.append(stem)

    out = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "counts": {
            "cards": len(cards),
            "untagged": len(untagged),
            **{f"theme:{t}": len(s) for t, s in themes.items()},
        },
        "themes": themes,
        "untagged": untagged,
        "cards": cards,
    }
    OUT.write_text(json.dumps(out, indent=1), encoding="utf-8")
    print(f"Wrote {OUT}")
    for k, v in out["counts"].items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
