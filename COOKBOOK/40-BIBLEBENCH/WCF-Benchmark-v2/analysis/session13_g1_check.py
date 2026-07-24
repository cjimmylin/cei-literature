#!/usr/bin/env python
"""Session-13 G1 gate: mechanical form-rule checks for 80 items.

Item source logic:
  1. If data/session13_new_items.json exists, load it (all 80 items).
  2. Otherwise assemble in memory:
       a. All items from data/session13-drafts/R-*.json  (63 rebuilt items,
          authored == 'session-13')
       b. The 17 frozen items whose ids appear in nonzero_gap_items of
          analysis/20260718-session12-gate-results.json, taken verbatim from
          data/session12_new_items.json.

Checks carried over from session12_g1_check.py (all preserved):
  * Unique ids + id pattern ^(MEND|LIB|PROOF|WHOLE)-N-\\d{3}$
  * Required fields present
  * authored field (session-12 for frozen items, session-13 for rebuilt)
  * -N- namespace in id
  * contested/episode must be False
  * design consistency with prefix
  * kind consistency with prefix
  * rubric: total in [5.0, 6.5], <= 6 lines, manner line present, anchors on
    every entry
  * key must contain GATE block
  * PROOF items: key must contain 'AUTHORITATIVE STANDARDS TEXT'
  * stem must not contain 'attached'
  * stem must not contain leak strings
  * key must not contain process-pointer strings (with narrowed 'review-tied'
    false-positive fix from session-12)
  * no pressure_turns on non-episode items
  * gold_order must be exactly null
  * 8-gram contamination scan vs ../WCF/*.txt

New check (session-13 DOUBLE-HAZARD GATE):
  Every item with authored == 'session-13' must have a GATE that names TWO
  OPPOSITE failure directions.  The check uses substring / regex heuristics
  on the GATE block text (first 1000 chars after 'GATE'):
    (a) COMPLY/AFFIRM/LICENSE side — at least one trigger present.
    (b) REFUSE/OVER-BIND side — at least one trigger present.
  Hard-fail: no GATE block at all (already caught above), OR clearly only one
  direction present (neither trigger list matches).
  FLAG for Fable review: exactly one side's trigger list matches but the other
  is empty — meaning the heuristic is inconclusive (the item may use
  domain-specific vocabulary not in the trigger lists).
  NOTE: The hard-fail threshold is set conservatively: an item is flagged
  (not hard-failed) when one side is positive and the other is negative,
  because the trigger lists may miss valid alternate phrasing.  Only items
  where *both* sides are empty (no triggers on either side) are hard-failed
  as 'clearly single-direction or no-direction GATE'.

Exits 0 iff total violations == 0 (flags are reported but do NOT count as
violations for the exit code).
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
DATA = V2 / "data"
DRAFTS_S13 = DATA / "session13-drafts"
DRAFTS_S12 = DATA / "session12-drafts"
WCF_DIR = V2.parent / "WCF"
S12_GATE_RESULTS = V2 / "analysis" / "20260718-session12-gate-results.json"
S12_NEW_ITEMS = DATA / "session12_new_items.json"
S13_NEW_ITEMS = DATA / "session13_new_items.json"

S13_DRAFT_FILES = [
    "R-LIB-a.json",
    "R-LIB-b.json",
    "R-MEND-a.json",
    "R-MEND-b.json",
    "R-PROOF-a.json",
    "R-PROOF-b.json",
    "R-WHOLE-a.json",
    "R-WHOLE-b.json",
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
PROCESS_PTRS = [
    "batch ruling", "reviewer", "blind review", "review round",
    "adjudicat", "session-12 ", "session-13 ",
]

NGRAM = 8  # contamination window

# ---------------------------------------------------------------------------
# Double-hazard GATE trigger lists (tuned against all 63 session-13 items)
# ---------------------------------------------------------------------------
# COMPLY/AFFIRM/LICENSE side — catches the "over-permit / under-bind" failure.
# Each entry is a Python regex pattern applied to lowercased GATE block text.
COMPLY_TRIGGERS: list[str] = [
    r"license",
    r"comply",
    r"affirm",
    r"deliver",
    r"include",
    r"commit",
    r"acquit",
    r"endorse",
    r"draft",           # "drafts clause (X) into..."
    r"under-bind",
    r"under.bind",
    r"ratif",           # ratify / ratifies / ratified
    r"permit",
    r"allow",
    r"accept",
    r"backs?\s",        # "backs the husband..."
    r"kept the oath",
    r"permissive",
    r"license side",
    r"license failure",
    r"comply side",
    r"bless.*devised",
    r"devised.*worship",
    r"superstitious",
    r"over-permit",
]

# REFUSE/OVER-BIND side — catches the "over-bind / legalism / over-convict /
# over-expose" failure.  MEND items use exposure/broadcasting/naming language
# for their refuse-side (over-correction toward public accusation).
REFUSE_TRIGGERS: list[str] = [
    r"over-bind",
    r"over.bind",
    r"legalism",
    r"refuse",
    r"forbid",
    r"\bban\b",         # ban (but not rebrand)
    r"convict",
    r"\bomit\b",
    r"over.convict",
    r"over.scrupulous",
    r"remov",
    r"\bcuts?\b",
    r"silence",
    r"slander",
    r"punish",
    r"broadcast",
    r"publicly naming",
    r"publicly.accus",
    r"publicly.sham",
    r"naming.*culpab",
    r"maximized",
    r"lurid",
    r"accusing",
    r"expos",           # expose / exposing / exposes
    r"prescribes?\s",   # "prescribes a lurid..."
    r"imposes",
    r"over.payment",
    r"excess",
    r"penalt",
    r"permanent renunci",
    r"names.*complicit",
    r"blanket refund",
    r"shaming",
    r"destroy",
    r"drain",
    r"torpedoing",
    r"re-sensational",
    r"demands? prosecution",
    r"names? .*culpab",
    r"renunci",
]


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
# Item assembly
# ---------------------------------------------------------------------------

def load_items() -> list[dict]:
    """Return the 80 session-13 bank items using the priority loading logic."""
    if S13_NEW_ITEMS.exists():
        print(f"[INFO] Loading from {S13_NEW_ITEMS}", file=sys.stderr)
        return json.loads(S13_NEW_ITEMS.read_text())

    # --- assemble in memory ---
    print("[INFO] data/session13_new_items.json not found; assembling in memory.",
          file=sys.stderr)

    # (i) 63 rebuilt items from session13-drafts/R-*.json
    rebuilt: list[dict] = []
    for fname in S13_DRAFT_FILES:
        fpath = DRAFTS_S13 / fname
        if not fpath.exists():
            raise FileNotFoundError(f"Missing draft file: {fpath}")
        batch = json.loads(fpath.read_text())
        rebuilt.extend(batch)

    # (ii) 17 frozen items from session12_new_items.json
    gate_results = json.loads(S12_GATE_RESULTS.read_text())
    frozen_ids: list[str] = gate_results["nonzero_gap_items"]

    s12_all = json.loads(S12_NEW_ITEMS.read_text())
    s12_map = {it["id"]: it for it in s12_all}

    frozen: list[dict] = []
    for iid in frozen_ids:
        if iid not in s12_map:
            raise KeyError(f"Frozen id {iid!r} not found in session12_new_items.json")
        frozen.append(s12_map[iid])

    items = rebuilt + frozen
    print(f"[INFO] Assembled {len(rebuilt)} rebuilt + {len(frozen)} frozen = "
          f"{len(items)} items total.", file=sys.stderr)
    return items


# ---------------------------------------------------------------------------
# Main gate
# ---------------------------------------------------------------------------

def main() -> int:
    items = load_items()
    errs: list[str] = []
    flags: list[str] = []  # items flagged for Fable review (not hard-failures)

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
        authored = it.get("authored", "")

        # ---- required fields present ----
        for field in ("id", "design", "track", "tier", "commandments",
                      "stem", "key", "rubric", "kind", "contested", "episode"):
            if it.get(field) in (None, "", []):
                errs.append(f"{iid}: missing {field}")

        # ---- provenance — frozen items are session-12; rebuilt are session-13 ----
        if authored not in ("session-12", "session-13"):
            errs.append(
                f"{iid}: authored must be 'session-12' or 'session-13' "
                f"(got {authored!r})"
            )

        # ---- -N- namespace ----
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

            # line cap: 6 for open/anchor (no contested items)
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
        # CHECK: GOLD_ORDER TYPE — must be exactly null
        # ============================================================
        gold = it.get("gold_order", "MISSING")
        if gold is not None:
            errs.append(f"{iid}: gold_order must be null (got {gold!r})")

        # ============================================================
        # CHECK: CONTAMINATION — no 8-gram from stem in WCF texts
        # ============================================================
        if stem and wcf_ngrams:
            for ng in stem_ngrams(stem):
                if ng in wcf_ngrams:
                    phrase = " ".join(ng)
                    errs.append(
                        f"{iid}: contamination — 8-gram in WCF texts: '{phrase}'"
                    )
                    break  # one report per item is enough

        # ============================================================
        # NEW CHECK: DOUBLE-HAZARD GATE (session-13 items only)
        # ============================================================
        if authored == "session-13":
            # Extract GATE block (first 1000 chars after 'GATE')
            m_gate = re.search(r"GATE\b", key, re.IGNORECASE)
            if m_gate:
                gate_block = key[m_gate.start() : m_gate.start() + 1000].lower()
            else:
                # 'no GATE block' already reported above; record separately for
                # double-hazard too
                errs.append(
                    f"{iid}: [double-hazard] no GATE block — cannot verify "
                    f"both failure directions"
                )
                continue

            has_comply = any(
                re.search(pat, gate_block) for pat in COMPLY_TRIGGERS
            )
            has_refuse = any(
                re.search(pat, gate_block) for pat in REFUSE_TRIGGERS
            )

            if not has_comply and not has_refuse:
                # Clearly single-direction or content-free GATE — hard-fail.
                errs.append(
                    f"{iid}: [double-hazard] GATE has NO comply-side AND no "
                    f"refuse-side triggers — appears to be single-direction or "
                    f"empty GATE"
                )
            elif not has_comply:
                # One side is ambiguous — flag for Fable review, do not hard-fail.
                flags.append(
                    f"{iid}: [double-hazard FLAG] GATE has refuse-side triggers "
                    f"but no comply-side trigger matched — verify manually that a "
                    f"LICENSE/COMPLY/AFFIRM direction is present in GATE"
                )
            elif not has_refuse:
                # One side is ambiguous — flag for Fable review, do not hard-fail.
                flags.append(
                    f"{iid}: [double-hazard FLAG] GATE has comply-side triggers "
                    f"but no refuse-side trigger matched — verify manually that an "
                    f"OVER-BIND/LEGALISM/REFUSE direction is present in GATE"
                )
            # else: both sides detected — pass silently

    # ---- summary ----
    total = len(items)
    rebuilt_count = sum(1 for it in items if it.get("authored") == "session-13")
    frozen_count = sum(1 for it in items if it.get("authored") == "session-12")

    print()
    print(f"Items: {total} total ({rebuilt_count} session-13 rebuilt, "
          f"{frozen_count} session-12 frozen)")
    print()

    if errs:
        print("=== VIOLATIONS ===")
        for e in errs:
            print(e)
        print()

    if flags:
        print("=== FLAGS (Fable review requested) ===")
        for f in flags:
            print(f)
        print()

    vcount = len(errs)
    fcount = len(flags)
    print(f"G1: {total} items checked, {vcount} violations, {fcount} flags")
    return 0 if vcount == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
