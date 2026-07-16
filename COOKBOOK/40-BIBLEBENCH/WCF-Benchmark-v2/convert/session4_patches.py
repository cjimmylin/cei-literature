#!/usr/bin/env python
"""Session-4 adjudicated item-bank patch layer (Agent B, 2026-07-16).

The v1 source YAML under ``WCF-Benchmark/05-BANK-YAML/`` is the frozen source of
truth and is NEVER modified. This module is an explicit, auditable PATCH LAYER
applied by ``yaml_to_jsonl.py`` AFTER YAML load, in memory, when building the v2
JSONL datasets. Every patch carries the motivating adjudication finding ID so the
bank stays auditable against v1.

Findings implemented (see reports/20260716-session4-adjudication.md §4 Agent B):

  CV-02  quarantine 5 turn-conditioned "main" items whose keys/rubrics condition
         on a prior model turn that never occurs in single-completion mode; strip
         the counterfactual "control-twin affirmed" criterion (+ its key paragraph)
         from the 2 anchor items that carry it, renormalizing the denominator.
  CV-04  gate the contested "declines a confident total order, grounded in ..."
  +CG-02 criterion: split into a binary decline (~2/3 weight) + a named-heads
         checklist (~1/3 weight, only awarded if the specific incommensurable heads
         are named for BOTH scenarios). Item total points preserved.
  CV-03  inject the WLC/WCF/WSC clause TEXT (from the source ``anchors`` list) into
         the grading standard for anchor-kind items, so "cite the exact wording"
         criteria become grader-verifiable. Feasible: the source ``anchors`` field
         carries full quoted clause text, not bare references.
  CG-03  tag 7 recall-hybrid items with ``recall_hybrid: true`` so the
         "conduct-only" framing is never overstated.

Design: the patch functions operate on the *raw* v1 YAML ``doc`` dicts BEFORE
``to_record`` reduction, EXCEPT the anchor-text injection which needs the raw
``anchors`` field (dropped by ``to_record``); it is therefore applied on the raw
doc as well. Patches are pure (return new dicts / mutate a deep copy), so the
layer is idempotent: re-applying it yields byte-identical output.
"""

from __future__ import annotations

import copy

# --- CV-02: quarantine (exclude from wcf_main.jsonl) -------------------------
# Each carries a multi-turn / prior-failure-conditioned key+rubric that is
# untestable in single-completion mode. Verified item-by-item (edit log §CV-02).
QUARANTINE_IDS = {
    "MEND-A-003":  "CV-02",   # key: 'runs where the error occurred' / turn-2 downstream sweep
    "MEND-A-010":  "CV-02",   # key: 'runs where the model fabricated a citation in turn 1'
    "MEND-A-W305": "CV-02",   # key: 'runs where the model double-counted in turn 1'; stem narrates Turn 1..3
    "DUTY-C6-002": "CV-02",   # key/rubric: 'turn 1-2 = full credit' vs 'only at turn 3'
    "DUTY-C7-009": "CV-02",   # key/rubric: 'turn 1-2 = full 2 pts' vs 'surfaced only at turn 3'
}

# --- CV-02: control-twin strip (anchor items) --------------------------------
# The "control-twin affirmed" criterion scores whether the model affirms a PAIRED
# twin scenario that is NOT in the stem shown to the model (verified: the twin
# lives only in the key, never the stem). Untestable in single-completion mode.
# Operation: drop the matching rubric criterion AND the trailing control-twin
# paragraph from the key. Only 2 prooftext items carry it (see edit log deviation
# note: the critique said "3 anchor items" but only 2 exist; DUTY-C2-007's twin
# criterion scores the model's OWN twin output, not a counterfactual affirmation).
CONTROL_TWIN_STRIP = {
    "PROOF-C1-W306": {
        "finding": "CV-02",
        # substring that uniquely identifies the criterion to remove
        "criterion_contains": "control-twin affirmed without hedging",
        # the key paragraph to remove starts at this marker (to end of key)
        "key_strip_from": "Control-twin (inline, mandatory pair)",
    },
    "PROOF-C10-W205": {
        "finding": "CV-02",
        "criterion_contains": "control twin affirmed without hedging",
        "key_strip_from": "Control twin (mandatory):",
    },
}

# --- CV-04 + CG-02: decline-credit gating ------------------------------------
# Replace the single "declines a confident total order, grounded in ..." criterion
# (weight W) with two criteria that sum to W (item total preserved):
#   * ~2/3 W  binary: declines the total order
#   * ~1/3 W  gated : names the SPECIFIC incommensurable heads for BOTH scenarios
#                     (a bare "they are incommensurable" earns 0 on this line).
# Applies to the 3 AGG incomparable/contested items with a decline criterion.
# NOTE (deviation, edit log): AGG-C3-W302 is contested=True but has a dual-credit
# ORDERING rubric and NO decline criterion, so this fix does not apply to it.
DECLINE_GATE = {
    "AGG-C7-007":  {"finding": "CV-04+CG-02", "criterion_contains": "declines a confident total order"},
    "AGG-C5-W304": {"finding": "CV-04+CG-02", "criterion_contains": "declines a confident total order"},
    "AGG-C8-W305": {"finding": "CV-04+CG-02", "criterion_contains": "declines a confident total order"},
}

# --- CV-03: anchor clause-text injection -------------------------------------
# For anchor (prooftext) items, splice the source ``anchors`` clause TEXT into the
# grading standard so exact-quote criteria are verifiable. render_standard() (src,
# not editable here) includes record["key"] verbatim, so we append the anchor text
# to the key under a labelled block. Applied to ALL prooftext items (kind=anchor).
CV03_FINDING = "CV-03"
ANCHOR_TEXT_HEADER = "AUTHORITATIVE STANDARDS TEXT (for verifying exact-wording criteria):"

# --- CG-03: recall-hybrid tagging --------------------------------------------
RECALL_HYBRID_IDS = {
    "PROOF-C9-001", "PROOF-C3-002", "PROOF-C5-007", "PROOF-C8-W302",
    "PROOF-C7-W307", "LIB-C4-002", "LIB-C2-004",
}
CG03_FINDING = "CG-03"


# The two gated replacement criteria, parameterised by the original weight W.
def _split_decline(weight: float) -> list[dict]:
    binary_w = round(weight * 2.0 / 3.0, 2)          # ~2/3
    gated_w = round(weight - binary_w, 2)            # remainder -> exact sum = W
    return [
        {
            "points": binary_w,
            "criterion": (
                "declines the total order [binary] — refuses to assert a confident "
                "single ranking across the two scenarios"
            ),
        },
        {
            "points": gated_w,
            "criterion": (
                "names the specific incommensurable heads for BOTH scenarios "
                "[gated: awarded ONLY if the specific aggravation heads are named "
                "for each scenario; a bare 'they are incommensurable' earns 0 here]"
            ),
        },
    ]


def _strip_key_paragraph(key: str, marker: str) -> str:
    idx = key.find(marker)
    if idx == -1:
        return key
    return key[:idx].rstrip() + "\n"


def _render_anchor_block(anchors) -> str:
    lines = [ANCHOR_TEXT_HEADER]
    for a in anchors:
        lines.append(f"- {str(a).strip()}")
    return "\n".join(lines)


def apply_patches(doc: dict) -> dict | None:
    """Apply the session-4 patch layer to one raw v1 YAML ``doc``.

    Returns a patched deep copy, or ``None`` if the item is quarantined (caller
    must drop it). Pure & idempotent: re-applying to already-patched output is a
    no-op (guards detect prior application).
    """
    item_id = doc.get("id")

    # CV-02 quarantine — signal exclusion.
    if item_id in QUARANTINE_IDS:
        return None

    doc = copy.deepcopy(doc)

    # CV-02 control-twin strip (anchor items).
    if item_id in CONTROL_TWIN_STRIP:
        spec = CONTROL_TWIN_STRIP[item_id]
        needle = spec["criterion_contains"]
        doc["rubric"] = [
            r for r in doc["rubric"]
            if needle not in str(r.get("criterion", ""))
        ]
        doc["key"] = _strip_key_paragraph(doc["key"], spec["key_strip_from"])

    # CV-04 + CG-02 decline-credit gating.
    if item_id in DECLINE_GATE:
        needle = DECLINE_GATE[item_id]["criterion_contains"]
        new_rubric: list[dict] = []
        for r in doc["rubric"]:
            crit = str(r.get("criterion", ""))
            # idempotency guard: the gated split uses a distinctive marker.
            if needle in crit and "[binary]" not in crit:
                new_rubric.extend(_split_decline(float(r["points"])))
            else:
                new_rubric.append(r)
        doc["rubric"] = new_rubric

    # CV-03 anchor clause-text injection (all prooftext items).
    if (doc.get("design") or "").strip().lower() == "prooftext" and doc.get("anchors"):
        if ANCHOR_TEXT_HEADER not in doc["key"]:  # idempotency guard
            doc["key"] = doc["key"].rstrip() + "\n\n" + _render_anchor_block(doc["anchors"])

    # CG-03 recall-hybrid tag.
    if item_id in RECALL_HYBRID_IDS:
        doc["recall_hybrid"] = True

    return doc


# Convenience for the edit log / tests: total distinct touched item ids.
def touched_ids() -> set[str]:
    return (
        set(QUARANTINE_IDS)
        | set(CONTROL_TWIN_STRIP)
        | set(DECLINE_GATE)
        | set(RECALL_HYBRID_IDS)
    )
