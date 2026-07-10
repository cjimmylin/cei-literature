"""Shared low-level parsing machinery for WALKWORTHY seed files.

Every seed file is Markdown: a sequence of `### WW-..` item blocks, each with a
```yaml fenced frontmatter block and a set of `**Label:**` bold-label fields whose
values run until the next field / yaml fence / item header. Per-design *builders*
(loader.py) consume RawItem; this module is format-agnostic.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

import yaml

# ID then free-form remainder (titles vary: " — X", " / -R — X", " (pair) — X", " *(cue: T)*").
HEADER_RE = re.compile(r"^###\s+(WW-[0-9A-Za-z]+(?:-[0-9A-Za-z]+)*)\b\s*(.*)$")
_TITLE_SEP_RE = re.compile(r"^\s*(?:\(pair\)|/\s*-?\w+|—|--)\s*")
# A field-start line: begins with **...:** (bold text ending in a colon, closing bold).
FIELD_RE = re.compile(r"^\*\*(?P<label>[^*].*?):\*\*\s?(?P<rest>.*)$")
# Bare (unbolded) structural keyword lines we also treat as field starts (e.g. `facts_diff:`).
BARE_FIELD_RE = re.compile(r"^(?P<label>facts_diff|reskin_[a-z]|Checklist):\s*(?P<rest>.*)$")


@dataclass
class RawItem:
    id: str
    title: str
    yaml: dict
    fields: "OrderedFields"          # ordered label -> text
    body: str                        # raw block text (minus header line)
    source_file: str
    start_line: int


class OrderedFields:
    """Insertion-ordered, case-sensitive multi-field container.

    Some designs repeat a label surface (e.g. 09's four 'Keyed determinations (...)'
    variants) — we key on the *first token* family via helpers, but preserve raw labels.
    """

    def __init__(self) -> None:
        self._items: List[Tuple[str, str]] = []

    def add(self, label: str, value: str) -> None:
        self._items.append((label, value.strip()))

    def __contains__(self, label: str) -> bool:
        return any(l == label for l, _ in self._items)

    def get(self, label: str, default: Optional[str] = None) -> Optional[str]:
        for l, v in self._items:
            if l == label:
                return v
        return default

    def get_prefix(self, prefix: str) -> Optional[str]:
        """First field whose label starts with `prefix` (for variant-suffixed labels)."""
        for l, v in self._items:
            if l.startswith(prefix):
                return v
        return None

    def all_prefix(self, prefix: str) -> List[Tuple[str, str]]:
        return [(l, v) for l, v in self._items if l.startswith(prefix)]

    def labels(self) -> List[str]:
        return [l for l, _ in self._items]

    def items(self) -> List[Tuple[str, str]]:
        return list(self._items)


def split_items(text: str, source_file: str) -> List[Tuple[str, str, str, int]]:
    """Split a seed file into (id, title, block_body, start_line) tuples.

    Only `### WW-..` headers start items; file-level `**...**` notes before the
    first header are ignored.
    """
    lines = text.splitlines()
    blocks: List[Tuple[str, str, str, int]] = []
    cur_id: Optional[str] = None
    cur_title = ""
    cur_start = 0
    buf: List[str] = []

    def flush() -> None:
        if cur_id is not None:
            blocks.append((cur_id, cur_title, "\n".join(buf), cur_start))

    for i, line in enumerate(lines):
        m = HEADER_RE.match(line)
        if m:
            flush()
            cur_id = m.group(1)
            title = (m.group(2) or "").strip()
            title = _TITLE_SEP_RE.sub("", title).strip()
            cur_title = title
            cur_start = i + 1
            buf = []
        elif cur_id is not None:
            buf.append(line)
    flush()
    return blocks


def _extract_yaml(block: str) -> Tuple[dict, str]:
    """Pull the first ```yaml fenced block; return (parsed_dict, block_without_yaml)."""
    lines = block.splitlines()
    out_lines: List[str] = []
    yaml_lines: List[str] = []
    in_yaml = False
    captured = False
    for line in lines:
        stripped = line.strip()
        if not captured and not in_yaml and stripped.startswith("```") and "yaml" in stripped:
            in_yaml = True
            continue
        if in_yaml:
            if stripped.startswith("```"):
                in_yaml = False
                captured = True
                continue
            yaml_lines.append(line)
        else:
            out_lines.append(line)
    parsed = {}
    if yaml_lines:
        parsed = yaml.safe_load("\n".join(yaml_lines)) or {}
    return parsed, "\n".join(out_lines)


def _extract_fields(body_no_yaml: str) -> OrderedFields:
    """Extract `**Label:**` (and select bare) fields with multi-line values.

    A value runs from its start line to the next field-start line or an embedded
    ```yaml fence (which belongs to the *current* field's value, e.g. 09 extraction
    schema — so fenced blocks are captured verbatim into the current value, not split).
    """
    fields = OrderedFields()
    lines = body_no_yaml.splitlines()
    cur_label: Optional[str] = None
    cur_val: List[str] = []
    in_fence = False

    def flush() -> None:
        if cur_label is not None:
            fields.add(cur_label, "\n".join(cur_val))

    for line in lines:
        stripped = line.strip()
        # Track fenced code blocks so a `**...:**`-looking line inside a fence
        # is not mistaken for a field boundary.
        if stripped.startswith("```"):
            in_fence = not in_fence
            if cur_label is not None:
                cur_val.append(line)
            continue
        if not in_fence:
            m = FIELD_RE.match(line) or BARE_FIELD_RE.match(line)
            if m:
                flush()
                cur_label = m.group("label").strip()
                rest = m.group("rest")
                cur_val = [rest] if rest else []
                continue
        if cur_label is not None:
            cur_val.append(line)
    flush()
    return fields


def parse_raw_items(text: str, source_file: str) -> List[RawItem]:
    items: List[RawItem] = []
    for item_id, title, block, start_line in split_items(text, source_file):
        parsed_yaml, body_no_yaml = _extract_yaml(block)
        fields = _extract_fields(body_no_yaml)
        items.append(
            RawItem(
                id=item_id,
                title=title,
                yaml=parsed_yaml or {},
                fields=fields,
                body=block,
                source_file=source_file,
                start_line=start_line,
            )
        )
    return items
