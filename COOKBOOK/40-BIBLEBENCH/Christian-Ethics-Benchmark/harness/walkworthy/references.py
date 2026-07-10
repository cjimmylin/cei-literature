"""Reference-answer provider (W4 wiring) for the reference-anchored designs 06 + 09.

`assemble_rubric_prompt` embeds these anchors so a real judge — and, later, the human
labeler (protocol §3: judges and humans must score against identical anchors or κ is
confounded) — score against the corpus-keyed reference, not vibes. The panel builds its
`CLIJudge`s with this provider (they were previously built with none, so 06/09 were
scored unanchored).

- 06: the bank's matched-quality opposite-conclusion reference answers (G5 neutrality
  anchors). Some DSP items still lack a pole (M-3 authoring, tracked) — those return the
  refs that exist; 06 stays PROVISIONAL until G5.
- 09: the keyed determinations (symmetric who-owes-what core) + typed extraction schema
  — the symmetry anchors both seats must converge on.
"""
from __future__ import annotations

from typing import List


def _fmt_extraction(schema) -> str:
    if not isinstance(schema, list):
        return ""
    lines = []
    for e in schema:
        if isinstance(e, dict):
            lines.append("- " + ", ".join(f"{k}: {v}" for k, v in e.items()))
    return "\n".join(lines)


def bank_reference_provider(item) -> List[dict]:
    """Return [{label, text}] anchors for a reference-anchored item; [] otherwise."""
    design = getattr(item, "design", "")
    extras = getattr(item, "extras", {}) or {}
    key = getattr(item, "key", {}) or {}

    if design.startswith("06"):
        refs = extras.get("reference_answers") or []
        return [{"label": r.get("label", "reference"), "text": r.get("text", "")}
                for r in refs if r.get("text")]

    if design.startswith("09"):
        anchors: List[dict] = []
        if key.get("keyed_determinations"):
            anchors.append({"label": "Keyed determinations (symmetric core — must come "
                            "out the same from both seats)",
                            "text": key["keyed_determinations"]})
        if key.get("floor_violations"):
            anchors.append({"label": "Floor violations (anti-evil-consistency guard)",
                            "text": key["floor_violations"]})
        ext = _fmt_extraction(extras.get("extraction_schema"))
        if ext:
            anchors.append({"label": "Expected extractions (typed determinations)",
                            "text": ext})
        return anchors

    return []
