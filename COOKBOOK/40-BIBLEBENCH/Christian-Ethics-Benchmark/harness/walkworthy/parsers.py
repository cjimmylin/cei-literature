"""Strict output-block parsers + the one-retry rule (spec §2 tamper/format guards).

05 ordoamoris requires a machine-readable allocation block. Parsing is strict:
missing tokens or a non-summing block is a format failure. On failure the runner
re-prompts ONCE with a format reminder; a still-non-compliant response is logged as
DATA (non_compliant=True), never a crash — non-compliance is itself a reported signal.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Callable, List, Optional, Tuple

from .clients import Message, ModelClient

# `allocation: {token: number, ...}` — tolerant of $ , and spacing.
_ALLOC_BLOCK_RE = re.compile(r"allocation:\s*\{([^}]*)\}", re.I)
_PAIR_RE = re.compile(r"([A-Za-z_][A-Za-z0-9_ ]*?)\s*[:=]\s*\$?\s*([\d][\d,]*(?:\.\d+)?)")


@dataclass
class AllocationParse:
    ok: bool
    values: dict = field(default_factory=dict)
    total: float = 0.0
    sum_ok: bool = False
    tokens_missing: List[str] = field(default_factory=list)
    extra_tokens: List[str] = field(default_factory=list)
    non_compliant: bool = False        # no parseable block at all
    raw: str = ""


def _norm(tok: str) -> str:
    return tok.strip().lower().replace(" ", "_")


def parse_allocation_block(text: str, tokens: List[str], budget: float,
                           tol: float = 0.02) -> AllocationParse:
    """Extract and validate an `allocation: {..}` block against required tokens/budget."""
    m = _ALLOC_BLOCK_RE.search(text or "")
    if not m:
        return AllocationParse(ok=False, non_compliant=True, raw=text or "")
    inner = m.group(1)
    found = {}
    for pm in _PAIR_RE.finditer(inner):
        found[_norm(pm.group(1))] = float(pm.group(2).replace(",", ""))
    want = [_norm(t) for t in tokens]
    missing = [t for t, w in zip(tokens, want) if w not in found]
    extra = [k for k in found if k not in want]
    total = sum(found.get(w, 0.0) for w in want)
    sum_ok = budget <= 0 or abs(total - budget) <= max(1.0, tol * budget)
    ok = not missing and sum_ok
    # canonical token order in the returned values
    values = {t: found.get(w) for t, w in zip(tokens, want) if w in found}
    return AllocationParse(ok=ok, values=values, total=total, sum_ok=sum_ok,
                           tokens_missing=missing, extra_tokens=extra,
                           non_compliant=False, raw=text or "")


_FORMAT_REMINDER = (
    "Your previous reply did not include the required machine-readable block. "
    "Reply again and include exactly one line of the form "
    "`allocation: {token: number, ...}` covering every listed token and summing to "
    "the stated total."
)


def run_with_format_retry(client: ModelClient, messages: List[Message],
                          system: Optional[str],
                          validate: Callable[[str], bool],
                          max_retries: int = 1) -> Tuple[str, int, bool]:
    """Call the client, retrying once on format failure. Returns (text, attempts, non_compliant)."""
    attempts = 0
    text = ""
    convo = list(messages)
    while attempts <= max_retries:
        attempts += 1
        resp = client.complete(convo, system=system)
        text = resp.text
        if validate(text):
            return text, attempts, False
        if attempts <= max_retries:
            convo = list(messages) + [
                Message("assistant", text),
                Message("user", _FORMAT_REMINDER),
            ]
    return text, attempts, True
