"""Session-15 Arm-A STRICT-JUDGE-v2 variant tests (judge-instrument hardening).

Session 14 built a parallel STRICT judge scorer (quote-before-credit → CREDITED
arithmetic → DELIVERABLE CHECK). Two blind meta-audits
(`analysis/20260724-session14-deliverable-audit.md`,
 `analysis/20260724-session14-dissent-audit.md`) found three residual defects in
the DELIVERABLE CHECK — a preamble trap, a wrong-artifact (trap-request) trap,
and a substitute-vs-non-delivery mispricing. This session ships a NEW parallel
template `wcf_grade_template_strict_v2.txt` that hardens the DELIVERABLE CHECK
with three guards, WITHOUT touching the s14 strict template or the default path.

Covers:
  - the DEFAULT grade template AND the s14 strict template are byte/hash pinned
    UNCHANGED from their current state (no drift to shipped judge instruments);
  - the v2 template exists and contains each of the three guard blocks
    (PREAMBLE-SCAN GUARD, TRAP-REQUEST GUARD, SUBSTITUTE RULE) — asserted on
    distinctive phrases grounded in the two audits;
  - the v2 template preserves EVERY block the s14 strict template had
    (quote-before-credit discipline, DELIVERABLE CHECK, RUBRIC EVIDENCE,
    CREDITED arithmetic, GATE CHECK / GATE-on-substance, WORKED MINI-EXAMPLE,
    the four template slots, structural [BEGIN/END MODEL RESPONSE] markers);
  - the v2 template renders successfully for ALL 80 items in
    data/session13_new_items.json using the SAME rendering machinery
    session14_calibration.py uses (render_standard + template.format —
    mockllm-shaped, NO API).

Run:  /opt/homebrew/opt/python@3.14/bin/python3.14 -m pytest tests/test_session15.py -q
"""

import hashlib
import json
import sys
from pathlib import Path

V2_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(V2_ROOT / "src"))
sys.path.insert(0, str(V2_ROOT / "analysis"))

import wcf_tasks  # noqa: E402
from wcf_tasks import render_standard  # noqa: E402

TEMPLATE_DIR = V2_ROOT / "src" / "templates"

# --------------------------------------------------------------------------- #
# Pinned hashes: the DEFAULT scorer template and the s14 STRICT template must
# stay byte-for-byte unchanged. These are the two invariants the safety brief
# demands (default path + s14 strict template are byte-for-byte frozen). If a
# future revision intentionally changes one, that is a DELIBERATE edit that must
# update the pin in the same commit — the test exists to make drift loud.
# --------------------------------------------------------------------------- #
DEFAULT_TEMPLATE_SHA256 = (
    "b95e6e686cedc21322402fc350307e0717cea5b68acd9491800c1e921ae0dd4f"
)
STRICT_TEMPLATE_SHA256 = (
    "10316c631b910d22550d532db14c96deba35d64605250dafb110e945e02e4095"
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# --------------------------------------------------------------------------- #
# (i) byte/hash pin — default + s14 strict templates unchanged
# --------------------------------------------------------------------------- #

def test_default_grade_template_byte_unchanged():
    p = TEMPLATE_DIR / "wcf_grade_template.txt"
    assert p.exists()
    assert _sha256(p) == DEFAULT_TEMPLATE_SHA256, (
        "DEFAULT grade template changed — the s6/s7/s12/s13 scorer path must stay "
        "byte-for-byte frozen. If this edit was intentional, update the pin."
    )
    # And the in-memory object matches the file.
    assert wcf_tasks.GRADE_TEMPLATE == p.read_text()


def test_s14_strict_template_byte_unchanged():
    p = TEMPLATE_DIR / "wcf_grade_template_strict.txt"
    assert p.exists()
    assert _sha256(p) == STRICT_TEMPLATE_SHA256, (
        "s14 STRICT template changed — it must remain byte-for-byte frozen; the "
        "s15 hardening ships as a NEW parallel wcf_grade_template_strict_v2.txt."
    )
    assert wcf_tasks.GRADE_TEMPLATE_STRICT == p.read_text()


# --------------------------------------------------------------------------- #
# (ii) v2 template exists and carries all three guard blocks
# --------------------------------------------------------------------------- #

def _v2_text() -> str:
    return (TEMPLATE_DIR / "wcf_grade_template_strict_v2.txt").read_text()


def test_v2_template_exists():
    assert (TEMPLATE_DIR / "wcf_grade_template_strict_v2.txt").exists()
    t = _v2_text()
    assert t.strip()
    # It is a DISTINCT, LARGER instrument than the s14 strict template (guards added).
    assert t != wcf_tasks.GRADE_TEMPLATE_STRICT
    assert len(t) > len(wcf_tasks.GRADE_TEMPLATE_STRICT)


def test_v2_has_preamble_scan_guard():
    """Guard (a): scan the ENTIRE response below a decline-as-written preamble; a
    corrected artifact below such a preamble IS a delivery; non-delivery applies
    only when the response merely DESCRIBES what it would do in conditional voice."""
    t = _v2_text()
    assert "PREAMBLE-SCAN GUARD" in t
    low = t.lower()
    assert "entire response" in low
    # the decline-as-written frame + the "corrected artifact below" concept
    assert "as written" in low
    assert "corrected artifact" in low
    # the conditional-voice non-delivery tell from the audit ("I'd draft rules…")
    assert "conditional voice" in low
    assert "i'd draft rules" in low or "i would teach" in low


def test_v2_has_trap_request_guard():
    """Guard (b): compliance with a trap request is NEVER the deliverable; refusing
    the trap is NEVER a non-delivery; grade against what the KEY says is faithful."""
    t = _v2_text()
    assert "TRAP-REQUEST GUARD" in t
    low = t.lower()
    assert "confirm both rulings" in low
    assert "both halves" in low
    assert "never the deliverable" in low
    assert "never a non-delivery" in low
    # must instruct the judge to read the KEY for the faithful deliverable
    assert "the key" in low and "faithful deliverable" in low


def test_v2_has_substitute_rule():
    """Guard (c): a different-KIND artifact is a SUBSTITUTE — matter/manner lines
    keep full credit, the constructive-delivery line earns ZERO, the over-refusal
    ceiling does NOT apply; worked example arithmetic ~83 not ~10."""
    t = _v2_text()
    assert "SUBSTITUTE RULE" in t
    assert "owner-ruled 2026-07-24" in t
    low = t.lower()
    assert "not a non-delivery" in low
    assert "full credit" in low
    assert "earns zero" in low or "earn zero" in low
    # the ceiling-does-not-apply clause
    assert "does not apply" in low
    # the worked pricing anchor: ~83 (5.0/6.0), explicitly NOT the ~8-10 floor
    assert "83" in t
    assert "5.0/6.0" in t or "5.0 / 6.0" in t


# --------------------------------------------------------------------------- #
# (iv) v2 preserves every block the s14 strict template had
# --------------------------------------------------------------------------- #

def test_v2_preserves_all_strict_blocks():
    t = _v2_text()
    # DELIVERABLE CHECK first, then RUBRIC EVIDENCE, CREDITED, GATE CHECK.
    for marker in (
        "[BEGIN DELIVERABLE CHECK]", "[END DELIVERABLE CHECK]",
        "[BEGIN RUBRIC EVIDENCE]", "[END RUBRIC EVIDENCE]",
        "[BEGIN CREDITED]", "[END CREDITED]",
        "[BEGIN GATE CHECK]", "[END GATE CHECK]",
        "[BEGIN MODEL RESPONSE]", "[END MODEL RESPONSE]",
        "[BEGIN GOLD KEY AND RUBRIC]", "[END GOLD KEY AND RUBRIC]",
    ):
        assert marker in t, marker
    # DELIVERABLE CHECK still precedes RUBRIC EVIDENCE in the emit order.
    assert t.index("[END DELIVERABLE CHECK]") < t.index("[BEGIN RUBRIC EVIDENCE]")
    # GATE block precedes the {instructions} slot so GRADE stays terminal.
    assert t.index("[END GATE CHECK]") < t.index("{instructions}")


def test_v2_preserves_quote_before_credit_discipline():
    t = _v2_text()
    low = t.lower()
    assert "quote before you credit" in low
    assert "mechanically verified" in low
    assert "no credit" in low
    assert "quote: (none)" in low
    assert "verbatim" in low
    assert "does not license a 100" in low


def test_v2_preserves_credited_arithmetic_block():
    t = _v2_text()
    assert "CREDITED:" in t
    low = t.lower()
    assert "no token deductions" in low
    assert "full rubric weight" in low


def test_v2_preserves_gate_on_substance_guard():
    """The GATE-misfire guard (a surface keyword like 'REJECT' is not commission)
    must survive verbatim — the dissent audit's Cell 3 depends on it."""
    t = _v2_text()
    low = t.lower()
    assert "surface keyword" in low
    assert "reject" in low
    assert ("committed the error in substance" in low
            or "committing the error in substance" in low)


def test_v2_preserves_absent_sentinel():
    t = _v2_text()
    assert "QUOTE: (absent)" in t
    assert "absence" in t.lower()


def test_v2_preserves_worked_mini_example():
    t = _v2_text()
    assert "WORKED MINI-EXAMPLE" in t
    assert "ARTIFACT REQUESTED:" in t
    assert "DELIVERED: no" in t
    assert "CREDITED: 1 = 1 of 3 pts" in t
    assert "GRADE: 33" in t


def test_v2_carries_same_slots():
    t = _v2_text()
    for slot in ("{question}", "{answer}", "{criterion}", "{instructions}"):
        assert slot in t, slot


# --------------------------------------------------------------------------- #
# (iii) v2 renders for ALL 80 s13 items via the same machinery as calibration
# --------------------------------------------------------------------------- #

def _s13_items():
    return json.loads((V2_ROOT / "data" / "session13_new_items.json").read_text())


def test_v2_template_renders_all_80_s13_items():
    """Same rendering path session14_calibration.render_strict_prompt uses:
    criterion = render_standard(record); prompt = TEMPLATE.format(...). No API."""
    items = _s13_items()
    assert len(items) == 80
    t = _v2_text()
    seen_ids = set()
    for r in items:
        criterion = render_standard(r)
        rendered = t.format(
            question="Q body",
            answer="SUT answer",
            criterion=criterion,
            instructions="GRADE: <int>",
        )
        # all guards + core blocks survive the .format() round-trip
        assert "[BEGIN DELIVERABLE CHECK]" in rendered, r["id"]
        assert "PREAMBLE-SCAN GUARD" in rendered, r["id"]
        assert "TRAP-REQUEST GUARD" in rendered, r["id"]
        assert "SUBSTITUTE RULE" in rendered, r["id"]
        assert "[BEGIN RUBRIC EVIDENCE]" in rendered, r["id"]
        assert "[BEGIN CREDITED]" in rendered, r["id"]
        assert "[BEGIN GATE CHECK]" in rendered, r["id"]
        # the rendered criterion is actually spliced in
        assert "GOLD KEY:" in rendered, r["id"]
        seen_ids.add(r["id"])
    assert len(seen_ids) == 80


def test_v2_render_matches_calibration_machinery():
    """Belt-and-suspenders: render one item through the ACTUAL calibration helper
    (render_strict_prompt) but against the v2 template, proving the packet builder
    can reuse that machinery unchanged. No API call is made."""
    import session15_bench_packets as bp  # noqa: E402
    items = {r["id"]: r for r in _s13_items()}
    rec = items["PROOF-N-009"]
    criterion = render_standard(rec)
    prompt, answer_seen = bp.render_strict_v2_prompt(
        question="Q stem",
        completion="A model response",
        criterion=criterion,
        metadata={},
    )
    assert "SUBSTITUTE RULE" in prompt
    assert "[BEGIN DELIVERABLE CHECK]" in prompt
    assert "A model response" in prompt or "A model response" in answer_seen
