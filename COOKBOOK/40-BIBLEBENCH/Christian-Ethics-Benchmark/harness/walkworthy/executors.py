"""Per-design executors: run an Item's administrations on a ModelClient.

- single_turn (01/05/06 + each twin/seat/variant of a paired design): one request.
- scripted_multi_turn (02/07): a state machine — run turn k, classify the response
  into a branch state, administer the matching branch of turn k+1; finish with the
  terminal ask. In O3 the classifier becomes a judge call; in O2 it's a pluggable
  heuristic so executors are testable without the judge layer.
- paired-session (03/04/08/09/10): every administration runs in a FRESH conversation
  (isolation — the model never sees the twin/seat) with a fixed-seed order permutation
  for counterbalancing. Global twin-separation (>=200 filler between twins, charter
  §6.6) is the run scheduler's job, not the item executor's.
"""
from __future__ import annotations

import hashlib
import random
from dataclasses import dataclass, field
from typing import Callable, List, Optional

from .clients import Message, ModelClient
from .models import Administration, Item

# design -> which fixed permutation-seed axis governs its administration order
_DESIGN_AXIS = {
    "03-quiettongue": "twin_order",
    "08-vocationfork": "twin_order",
    "04-innerweight": "variant_order",
    "10-strangergate": "variant_order",
    "09-doubleedge": "seat_order",
    "05-ordoamoris": "claimant_order",
}

StateClassifier = Callable[[str, List[str], str], str]

_NONCOMPLY_MARKERS = (
    "can't", "cannot", "won't", "will not", "not able", "i'm sorry", "i am sorry",
    "i'd decline", "i decline", "hold the line", "honest course", "truthful",
    "i won't", "unable to",
)
_VALIDATE_MARKERS = ("you're right", "you are right", "exactly", "i agree",
                     "on your side", "makes sense", "go along")


def default_state_classifier(text: str, states: List[str], design: str) -> str:
    """Heuristic branch selector for the O2 mock (replaced by a judge call in O3)."""
    t = (text or "").lower()
    noncompliant = any(k in t for k in _NONCOMPLY_MARKERS)
    if design.startswith("02"):
        choice = "refused" if noncompliant else "complied"
    elif design.startswith("07"):
        if noncompliant:
            choice = "challenged"
        elif any(k in t for k in _VALIDATE_MARKERS):
            choice = "validated"
        else:
            choice = "deflected"
    else:
        choice = states[0] if states else ""
    return choice if choice in states else (states[0] if states else "")


# --------------------------------------------------------------------------- #
# execution result model
# --------------------------------------------------------------------------- #
@dataclass
class TurnResult:
    index: int
    user_text: str
    response: str
    branch_state: Optional[str] = None      # multi-turn: which branch was administered
    refused_hint: bool = False


@dataclass
class AdministrationResult:
    label: str
    kind: str
    system: Optional[str]
    turns: List[TurnResult] = field(default_factory=list)
    terminal_response: Optional[str] = None
    terminal_user_text: Optional[str] = None


@dataclass
class ItemExecution:
    item_id: str
    design: str
    model: str
    order: List[str]
    administrations: List[AdministrationResult] = field(default_factory=list)
    isolation_used: bool = False


# --------------------------------------------------------------------------- #
# order permutation
# --------------------------------------------------------------------------- #
def permuted_order(labels: List[str], seed: int, item_id: str) -> List[str]:
    """Deterministic permutation of administration labels for one item."""
    h = hashlib.sha256(f"{seed}\x00{item_id}".encode()).digest()
    rng = random.Random(int.from_bytes(h[:8], "big"))
    out = list(labels)
    rng.shuffle(out)
    return out


# --------------------------------------------------------------------------- #
# administration execution
# --------------------------------------------------------------------------- #
def _run_single_turn(admin: Administration, client: ModelClient) -> AdministrationResult:
    ar = AdministrationResult(label=admin.label, kind=admin.kind, system=admin.system)
    user_text = admin.turns[0].text if admin.turns else ""
    resp = client.complete([Message("user", user_text)], system=admin.system)
    ar.turns.append(TurnResult(index=1, user_text=user_text, response=resp.text,
                               refused_hint=getattr(resp, "refused_hint", False)))
    return ar


def _run_scripted(admin: Administration, client: ModelClient, design: str,
                  classifier: StateClassifier) -> AdministrationResult:
    ar = AdministrationResult(label=admin.label, kind=admin.kind, system=admin.system)
    history: List[Message] = []
    prior_response = ""
    for turn in admin.turns:
        state = None
        if turn.branches:
            states = list(turn.branches.keys())
            state = classifier(prior_response, states, design)
            user_text = turn.branches.get(state, next(iter(turn.branches.values())))
        else:
            user_text = turn.text or ""
        history.append(Message("user", user_text))
        resp = client.complete(list(history), system=admin.system)
        history.append(Message("assistant", resp.text))
        prior_response = resp.text
        ar.turns.append(TurnResult(index=turn.index, user_text=user_text,
                                   response=resp.text, branch_state=state,
                                   refused_hint=getattr(resp, "refused_hint", False)))
    if admin.terminal_ask:
        history.append(Message("user", admin.terminal_ask))
        resp = client.complete(list(history), system=admin.system)
        ar.terminal_user_text = admin.terminal_ask
        ar.terminal_response = resp.text
    return ar


def execute_item(item: Item, client: ModelClient, permutation_seeds: dict,
                 state_classifier: Optional[StateClassifier] = None) -> ItemExecution:
    classifier = state_classifier or default_state_classifier

    # scripted multi-turn "main" runs in order; paired administrations are permuted.
    axis = _DESIGN_AXIS.get(item.design, "twin_order")
    seed = int(permutation_seeds.get(axis, 0))
    labels = [a.label for a in item.administrations]
    if item.order_permuted or item.isolation_required:
        order = permuted_order(labels, seed, item.id)
    else:
        order = labels

    by_label = {a.label: a for a in item.administrations}
    ex = ItemExecution(item_id=item.id, design=item.design, model=client.name,
                       order=order, isolation_used=item.isolation_required)
    for label in order:
        admin = by_label[label]
        if admin.kind == "single_turn":
            ex.administrations.append(_run_single_turn(admin, client))
        else:
            ex.administrations.append(_run_scripted(admin, client, item.design, classifier))
    return ex
