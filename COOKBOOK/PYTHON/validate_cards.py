#!/usr/bin/env python3
"""
COOKBOOK Phase 1 gate — evidence-card validator.

Checks every expected card (manifest papers -> 20260705-cards/, AI-Labs
shortlist -> 20260705-ailabs-cards/) for:
  - existence (straggler detection)
  - parseable YAML frontmatter with required keys
  - theme_tags drawn from the controlled vocabulary (non-empty)
  - body word floor (300 paper / 250 lab; degraded papers exempt)
  - at least one page ref "(p." in the body (non-degraded only)

Writes the mutable run ledger 20260705-run-state.json (state file, not a
report) and prints a console summary with straggler + invalid lists.
"""

import json
import re
from datetime import datetime
from pathlib import Path

EVIDENCE_DIR = Path(__file__).resolve().parents[1] / "30-EVIDENCE"
CARDS_DIR = EVIDENCE_DIR / "20260705-cards"
LAB_CARDS_DIR = EVIDENCE_DIR / "20260705-ailabs-cards"

VOCAB = {
    "best-practices", "design-space", "validity-psychometrics",
    "saturation-discrimination", "contamination-robustness",
    "agentic-multiturn", "llm-judges-scoring", "normative-ethics",
    "moral-psychology", "religious-values", "cultural-linguistic",
    "pluralism-aggregation", "ai-lab-practices",
}

REQUIRED_PAPER = ["stem", "reader_model", "confidence", "is_benchmark", "theme_tags"]
REQUIRED_LAB = ["stem", "company", "reader_model", "confidence", "theme_tags"]


def parse_card(path: Path):
    """Return (front_dict, body, issues). Tolerant YAML-ish parsing."""
    issues = []
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.S)
    if not m:
        return {}, text, ["no frontmatter block"]
    fm_text, body = m.group(1), m.group(2)
    front = {}
    try:
        import yaml
        front = yaml.safe_load(fm_text) or {}
        if not isinstance(front, dict):
            front, issues = {}, ["frontmatter not a mapping"]
    except Exception as e:  # fall back to regex per-line
        issues.append(f"yaml parse failed ({type(e).__name__}); regex fallback")
        for line in fm_text.splitlines():
            km = re.match(r'^(\w+):\s*(.*)$', line)
            if km:
                key, val = km.group(1), km.group(2).strip()
                if val.startswith("[") and val.endswith("]"):
                    front[key] = [v.strip().strip('"\'') for v in val[1:-1].split(",") if v.strip()]
                else:
                    front[key] = val.strip('"\'')
    return front, body, issues


def check_card(path: Path, required, word_floor, degraded=False):
    front, body, issues = parse_card(path)
    for key in required:
        if key not in front or front[key] in (None, "", []):
            issues.append(f"missing key: {key}")
    tags = front.get("theme_tags") or []
    if isinstance(tags, str):
        tags = [tags]
    bad = [t for t in tags if t not in VOCAB]
    if bad:
        issues.append(f"invalid theme_tags: {bad}")
    words = len(body.split())
    if not degraded and words < word_floor:
        issues.append(f"body too short: {words} words")
    if not degraded and "(p." not in body:
        issues.append("no page refs in body")
    return issues, words


def main():
    manifest = json.loads((EVIDENCE_DIR / "20260705-corpus-manifest.json").read_text())
    shortlist = json.loads((EVIDENCE_DIR / "20260705-ailabs-shortlist.json").read_text())

    degraded_stems = {p["stem"] for p in manifest["papers"] if p["extract_quality"] != "ok"}

    stragglers, invalid, valid = [], {}, []
    for p in manifest["papers"]:
        path = CARDS_DIR / f"{p['stem']}.card.md"
        if not path.exists():
            stragglers.append(p["stem"])
            continue
        issues, _ = check_card(path, REQUIRED_PAPER, 300, p["stem"] in degraded_stems)
        if issues:
            invalid[p["stem"]] = issues
        else:
            valid.append(p["stem"])

    lab_stragglers, lab_invalid, lab_valid = [], {}, []
    for r in shortlist["reports"]:
        path = LAB_CARDS_DIR / f"{r['stem']}.card.md"
        if not path.exists():
            lab_stragglers.append(r["stem"])
            continue
        issues, _ = check_card(path, REQUIRED_LAB, 250)
        if issues:
            lab_invalid[r["stem"]] = issues
        else:
            lab_valid.append(r["stem"])

    state = {
        "checked_at": datetime.now().isoformat(timespec="seconds"),
        "papers": {
            "expected": len(manifest["papers"]),
            "valid": len(valid),
            "invalid": len(invalid),
            "stragglers": len(stragglers),
            "straggler_stems": stragglers,
            "invalid_details": invalid,
        },
        "labs": {
            "expected": len(shortlist["reports"]),
            "valid": len(lab_valid),
            "invalid": len(lab_invalid),
            "stragglers": len(lab_stragglers),
            "straggler_stems": lab_stragglers,
            "invalid_details": lab_invalid,
        },
    }
    (EVIDENCE_DIR / "20260705-run-state.json").write_text(
        json.dumps(state, indent=1), encoding="utf-8"
    )

    print(f"PAPER CARDS: {len(valid)} valid / {len(invalid)} invalid / "
          f"{len(stragglers)} missing (of {len(manifest['papers'])})")
    print(f"LAB CARDS:   {len(lab_valid)} valid / {len(lab_invalid)} invalid / "
          f"{len(lab_stragglers)} missing (of {len(shortlist['reports'])})")
    if invalid:
        print("Invalid paper cards:")
        for stem, iss in list(invalid.items())[:30]:
            print(f"  {stem}: {iss}")
    if lab_invalid:
        print("Invalid lab cards:")
        for stem, iss in list(lab_invalid.items())[:30]:
            print(f"  {stem}: {iss}")


if __name__ == "__main__":
    main()
