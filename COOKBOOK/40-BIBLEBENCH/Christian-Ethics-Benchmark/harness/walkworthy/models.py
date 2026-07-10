"""Normalized item model shared across all 10 WALKWORTHY designs.

The 10 designs serialize to 10 different Markdown dialects on disk; this module
is the clean internal core they all normalize into, so executors / judges / gates
can operate uniformly regardless of a design's authoring format.

Concepts:
- Item          : one `### WW-..` block (may correspond to a paired item = >=2 administrations).
- Administration: one conversation to run in its own request (a "seat"/"twin"/"variant"/"main").
- Turn          : one user turn; may carry `branches` (scripted multi-turn) + `markers`.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class Turn:
    index: int                                   # T1, T2, ... (1-based)
    text: Optional[str] = None                   # unconditional user text (single-turn, or T1)
    branches: Optional[Dict[str, str]] = None    # state -> user text (02: C/R; 07: validated/challenged/deflected)
    markers: List[str] = field(default_factory=list)  # repentance_window|openness_window|loyalty_test|terminal


@dataclass
class Administration:
    """One conversation the harness will run in a single request/session."""
    label: str                                   # main|expressed|revealed|seat_A|seat_B|arbiter|N|U|alpha|beta
    kind: str                                    # single_turn | scripted_multi_turn
    system: Optional[str] = None
    turns: List[Turn] = field(default_factory=list)
    terminal_ask: Optional[str] = None           # 07: the forced final artifact ask
    cold_open: Optional[str] = None              # 02: standalone control administration text
    meta: Dict[str, Any] = field(default_factory=dict)  # cue text, seat descriptor, variant, etc.


@dataclass
class Item:
    id: str
    design: str                                  # "01-goodsamaritan"
    title: str
    area: str                                    # primary area tag, A..N
    secondary: List[str] = field(default_factory=list)
    stratum: str = "a"                           # a | b | c
    dispute: Optional[str] = None                # DSP-1.. (iff stratum c, usually)
    tier: str = "core"                           # core | contested
    anchors: List[str] = field(default_factory=list)
    difficulty: str = "hard"                     # easy | hard
    pair_id: Optional[str] = None
    canary: str = ""
    variables: Dict[str, Any] = field(default_factory=dict)

    # normalized administration plan
    admin_mode: str = "single"                   # single | multi_turn | paired
    isolation_required: bool = False             # paired designs: each admin in a separate request
    order_permuted: bool = False                 # paired designs: permute admin order per manifest seed
    administrations: List[Administration] = field(default_factory=list)

    # rubric / key, kept as normalized text fields; scoring layers read these + spec §4
    key: Dict[str, Any] = field(default_factory=dict)

    # design-specific extras: facts_diff, allocation spec, extraction_schema, comprehension_control, etc.
    extras: Dict[str, Any] = field(default_factory=dict)

    is_exemplar: bool = False
    source_file: str = ""

    def is_runnable(self) -> bool:
        """True iff at least one administration has materializable model input.

        The 02/07/09 spec exemplars are abbreviated prose sketches (no scripted
        turns) — those parse to empty administrations and are NOT executable; the
        fully-authored seed banks are the run surface.
        """
        for a in self.administrations:
            if a.terminal_ask:
                return True
            for t in a.turns:
                if (t.text and t.text.strip()) or t.branches:
                    return True
        return False

    def n_model_calls_single_pass(self) -> int:
        """Lower-bound generation calls for one pass (before judges), for budgeting."""
        n = 0
        for a in self.administrations:
            if a.kind == "single_turn":
                n += 1
            else:  # scripted_multi_turn: one call per user turn + terminal
                n += len(a.turns) + (1 if a.terminal_ask else 0)
        return n
