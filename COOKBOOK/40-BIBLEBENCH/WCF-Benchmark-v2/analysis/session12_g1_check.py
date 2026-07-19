#!/usr/bin/env python
"""Session-12 G1 gate: mechanical form-rule checks for 80 draft items.

Reads 8 D-*.json files from data/session12-drafts/, runs every applicable
form-rule from the s6/s7 gate scripts, and adds two new session-12 checks:
  1. CONTAMINATION: no stem may contain an 8-gram that appears verbatim in
     any of the Westminster reference texts under WCF/*.txt.
  2. GOLD_ORDER TYPE: every item must have gold_order exactly null.

Prints one line per violation ("ITEM-ID: description") and a final summary
"G1: N items checked, M violations". Exits 0 iff M == 0.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
V2 = Path(__file__).resolve().parent.parent
DRAFTS = V2 / "data" / "session12-drafts"
WCF_DIR = V2.parent / "WCF"

DRAFT_FILES = [
    "D-LIB-a.json",
    "D-LIB-b.json",
    "D-MEND-a.json",
    "D-MEND-b.json",
    "D-PROOF-a.json",
    "D-PROOF-b.json",
    "D-WHOLE-a.json",
    "D-WHOLE-b.json",
]

# expected (design, kind) per id prefix
DESIGN_KIND = {
    "MEND":  ("mending",    "open"),
    "LIB":   ("liberty",    "open"),
    "PROOF": ("prooftext",  "anchor"),
    "WHOLE": ("wholeheart", "open"),
}

ID_RE = re.compile(r"^(MEND|LIB|PROOF|WHOLE)-N-\d{3}$")

LEAK_STRINGS = ["rubric", "this is a test", "you are being tested", "grader"]
# "review-" alone false-positives on legitimate key content ("TERM-LIMITED,
# review-tied, named-endpoint structure" in MEND-N-017); flag process wording only.
PROCESS_PTRS = ["batch ruling", "reviewer", "blind review", "review round", "adjudicat", "session-12 "]

NGRAM = 8  # contamination window


# ---------------------------------------------------------------------------
# Build 8-gram set from Westminster reference texts
# ---------------------------------------------------------------------------

def _normalize(text: str) -> list[str]:
    """Lowercase + strip punctuation → token list."""
    return re.sub(r"[^a-z0-9 ]", " ", text.lower()).split()


def build_wcf_ngrams(wcf_dir: Path) -> set[tuple[str, ...]]:
    ngrams: set[tuple[str, ...]] = set()
    for txt in wcf_dir.glob("*.txt"):
        tokens = _normalize(txt.read_text(encoding="utf-8", errors="replace"))
        for i in range(len(tokens) - NGRAM + 1):
            ngrams.add(tuple(tokens[i : i + NGRAM]))
    return ngrams


def stem_ngrams(stem: str) -> list[tuple[str, ...]]:
    tokens = _normalize(stem)
    return [tuple(tokens[i : i + NGRAM]) for i in range(len(tokens) - NGRAM + 1)]


# ---------------------------------------------------------------------------
# Main gate
# ---------------------------------------------------------------------------

def main() -> int:
    # --- load items ---
    items: list[dict] = []
    for f in DRAFT_FILES:
        items.extend(json.load(open(DRAFTS / f)))

    errs: list[str] = []

    # --- build contamination index ---
    wcf_ngrams = build_wcf_ngrams(WCF_DIR)

    # --- unique ids + pattern ---
    ids = [it["id"] for it in items]
    if len(set(ids)) != len(ids):
        seen: set[str] = set()
        for iid in ids:
            if iid in seen:
                errs.append(f"{iid}: duplicate id")
            seen.add(iid)

    for iid in ids:
        if not ID_RE.match(iid):
            errs.append(f"{iid}: id does not match ^(MEND|LIB|PROOF|WHOLE)-N-\\d{{3}}$")

    # --- per-item checks ---
    for it in items:
        iid = it["id"]
        prefix = iid.split("-")[0]
        exp_design, exp_kind = DESIGN_KIND.get(prefix, ("?", "?"))

        # ---- required fields present ----
        for field in ("id", "design", "track", "tier", "commandments",
                      "stem", "key", "rubric", "kind", "contested", "episode"):
            if it.get(field) in (None, "", []):
                errs.append(f"{iid}: missing {field}")

        # ---- provenance ----
        if it.get("authored") != "session-12":
            errs.append(f"{iid}: authored != 'session-12' (got {it.get('authored')!r})")
        if "-N-" not in iid:
            errs.append(f"{iid}: id missing -N- namespace")

        # ---- fixed field values ----
        if it.get("contested") is not False:
            errs.append(f"{iid}: contested must be False (got {it.get('contested')!r})")
        if it.get("episode") is not False:
            errs.append(f"{iid}: episode must be False (got {it.get('episode')!r})")

        # ---- design consistency with prefix ----
        if it.get("design") != exp_design:
            errs.append(f"{iid}: design={it.get('design')!r}, expected {exp_design!r}")

        # ---- kind consistency with prefix ----
        if it.get("kind") != exp_kind:
            errs.append(f"{iid}: kind={it.get('kind')!r}, expected {exp_kind!r}")

        # ---- rubric form ----
        rubric = it.get("rubric") or []
        if rubric:
            tot = sum(c.get("points", 0) for c in rubric)
            if not (5.0 <= tot <= 6.5):
                errs.append(f"{iid}: rubric total {tot:.2f} outside [5.0, 6.5]")

            # line cap: 6 for open/anchor (no contested items in s12)
            if len(rubric) > 6:
                errs.append(f"{iid}: {len(rubric)} rubric lines > 6")

            # manner line present
            if not any(c.get("axis") == "manner" for c in rubric):
                errs.append(f"{iid}: no manner line (axis=='manner')")

            # anchors on every rubric entry
            for idx, c in enumerate(rubric):
                if not c.get("anchor"):
                    errs.append(f"{iid}: rubric[{idx}] missing anchor")

        # ---- key checks ----
        key = it.get("key") or ""
        if "GATE" not in key:
            errs.append(f"{iid}: no GATE block in key")

        # PROOF-specific: must contain authoritative standards text marker
        if prefix == "PROOF":
            if "AUTHORITATIVE STANDARDS TEXT" not in key:
                errs.append(f"{iid}: key missing 'AUTHORITATIVE STANDARDS TEXT'")

        # ---- stem checks ----
        stem = it.get("stem") or ""
        low_stem = stem.lower()

        if "attached" in low_stem:
            errs.append(f"{iid}: stem says 'attached'")

        for s in LEAK_STRINGS:
            if s in low_stem:
                errs.append(f"{iid}: leak string {s!r} in stem")

        # ---- process-pointer leak in key ----
        low_key = key.lower()
        for p in PROCESS_PTRS:
            if p in low_key:
                errs.append(f"{iid}: process pointer {p!r} in key")

        # ---- no pressure_turns on non-episode items ----
        if it.get("pressure_turns"):
            errs.append(f"{iid}: non-episode carries pressure_turns")

        # ============================================================
        # NEW CHECK 1: GOLD_ORDER TYPE — must be exactly null
        # ============================================================
        gold = it.get("gold_order", "MISSING")
        if gold is not None:
            errs.append(f"{iid}: gold_order must be null (got {gold!r})")

        # ============================================================
        # NEW CHECK 2: CONTAMINATION — no 8-gram from stem in WCF texts
        # ============================================================
        if stem and wcf_ngrams:
            for ng in stem_ngrams(stem):
                if ng in wcf_ngrams:
                    phrase = " ".join(ng)
                    errs.append(f"{iid}: contamination — 8-gram in WCF texts: '{phrase}'")
                    break  # one report per item is enough

    # ---- summary ----
    total = len(items)
    vcount = len(errs)
    for e in errs:
        print(e)
    print(f"G1: {total} items checked, {vcount} violations")
    return 0 if vcount == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
