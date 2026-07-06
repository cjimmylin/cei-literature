"""DUPLEX P0 — pre-registered analysis (pure functions).

Gates G1/G2/G3 (design §7) and the X2 shortcut audit. No I/O, no live calls: every
function takes plain result dicts and returns plain dicts, so they are unit-testable
against synthetic fixtures that are engineered to pass AND to fail each gate.
"""

from .gates import (
    process_beats_content,
    pairwise_separation,
    greene_direction,
    run_p0_gates,
)
from .shortcut_audit import (
    lexical_length_baseline,
    FineTuneProbe,
    combined_shortcut_verdict,
)

__all__ = [
    "process_beats_content",
    "pairwise_separation",
    "greene_direction",
    "run_p0_gates",
    "lexical_length_baseline",
    "FineTuneProbe",
    "combined_shortcut_verdict",
]
