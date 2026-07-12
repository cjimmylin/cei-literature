"""Deterministic monotone policies over rendered CROSSROADS affordances."""
from __future__ import annotations

import hashlib
import json
import re


_WARM = re.compile(r"\b(warm|kind|support|compassion|gentle|comfort)\w*", re.I)
_STALL = re.compile(r"\b(wait|later|schedule|meeting|delay|review)\w*", re.I)
_PIOUS = re.compile(r"\b(moral|loving|virtu|righteous|grace|charit)\w*", re.I)


def _descriptions(episode: dict) -> list[str]:
    rows = episode.get("affordances")
    if not isinstance(rows, list) or len(rows) not in {3, 4}:
        raise ValueError("bots require three or four rendered affordances")
    descriptions = [row.get("description") for row in rows]
    if any(not isinstance(text, str) for text in descriptions):
        raise ValueError("affordances need public descriptions")
    return descriptions


def _maximum(episode: dict, score) -> int:
    rows = _descriptions(episode)
    values = [score(text) for text in rows]
    return min(i for i, value in enumerate(values) if value == max(values))


def warm_path(episode: dict) -> int:
    return _maximum(episode, lambda text: len(_WARM.findall(text)))


def stall(episode: dict) -> int:
    return _maximum(episode, lambda text: len(_STALL.findall(text)))


def template_memorizer(episode: dict) -> int:
    rendered = json.dumps(
        episode.get("multiturn_script"), sort_keys=True, ensure_ascii=False
    ).encode()
    return int.from_bytes(hashlib.sha256(rendered).digest()[:4], "big") % len(
        _descriptions(episode)
    )


def length_tell(episode: dict) -> int:
    return _maximum(episode, len)


def tool_position(episode: dict) -> int:
    _descriptions(episode)
    return 0


def pious_language(episode: dict) -> int:
    return _maximum(episode, lambda text: len(_PIOUS.findall(text)))


BOTS = {
    "warm_path": warm_path,
    "stall": stall,
    "template_memorizer": template_memorizer,
    "length_tell": length_tell,
    "tool_position": tool_position,
    "pious_language": pious_language,
}
