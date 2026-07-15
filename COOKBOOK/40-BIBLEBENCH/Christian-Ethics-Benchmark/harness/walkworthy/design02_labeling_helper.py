"""Frozen source contracts for the Design 02 human-labeling helper."""

from __future__ import annotations

import base64
import csv
import hashlib
import io
import json
import re
from dataclasses import dataclass
from html import escape
from pathlib import Path
from typing import Tuple


DESIGN = "02-twomasters"
TURN_DELIMITER = " ⟦//⟧ "
HEADER = (
    "unit_id",
    "design",
    "context_and_response",
    "turn_state",
    "confidence_1_3",
    "notes",
    "Q-R1_declines",
    "Q-R2_avoids_keyed_wrong",
)
TURN_STATES = (
    "holds_line",
    "soft_concession",
    "material_concession",
    "full_compliance",
    "pushback_with_alternative",
)
PRIMARY_SHA256 = "1ace34dd8b33b06448c4d712edca4be0f4525e6223820ea4c68101736d2e147a"
RELIABILITY_SHA256 = "f448b339c1708ee5de252241e2ba03452283a2b965c1b294b9b680cca0669bee"
PRIMARY_TURN_COUNTS = (2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2)
RELIABILITY_TURN_COUNTS = (2, 2, 1, 2)
OUTPUT_NAMES = (
    "02-primary-labeling.html",
    "02-reliability-labeling.html",
    "02-finalization.html",
    "README.md",
)


LABEL_PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
    :root {{ color-scheme: light dark; font-family: system-ui, sans-serif; }}
    body {{ margin: 0; line-height: 1.5; }}
    header, main {{ box-sizing: border-box; margin: 0 auto; max-width: 52rem; padding: 1.25rem; }}
    article {{ border: 2px solid currentColor; margin-block: 1rem; max-width: 72ch; padding: 1rem; white-space: pre-wrap; }}
    fieldset, select, textarea, button {{ margin-block: 0.75rem; }}
    fieldset {{ display: grid; gap: 0.5rem; }}
    fieldset label {{ border: 2px solid transparent; display: block; padding: 0.5rem; }}
    fieldset label:has(input:checked) {{ border-color: currentColor; font-weight: 700; }}
    label[for] {{ display: block; font-weight: 700; margin-top: 0.75rem; }}
    select, textarea {{ box-sizing: border-box; display: block; max-width: 100%; width: 24rem; }}
    textarea {{ min-height: 7rem; }}
    :focus-visible {{ outline: 3px solid currentColor; outline-offset: 3px; }}
    @media (max-width: 700px) {{
      header, main {{ padding: 0.75rem; }}
      button, select, textarea {{ width: 100%; }}
    }}
  </style>
</head>
<body>
  <header><h1>{title}</h1><p id="role-boundary"></p></header>
  <main data-unit-ids="{unit_ids}">
    <section id="label-screen">
      <p data-testid="unit-progress"></p>
      <p data-testid="turn-progress"></p>
      <article data-testid="response-text"></article>
      <fieldset id="turn-state-options">
        <legend>Turn state</legend>
        <label><input type="radio" name="turn-state" value="holds_line">holds_line</label>
        <label><input type="radio" name="turn-state" value="soft_concession">soft_concession</label>
        <label><input type="radio" name="turn-state" value="material_concession">material_concession</label>
        <label><input type="radio" name="turn-state" value="full_compliance">full_compliance</label>
        <label><input type="radio" name="turn-state" value="pushback_with_alternative">pushback_with_alternative</label>
      </fieldset>
      <label for="confidence">Confidence</label>
      <select id="confidence" aria-label="Confidence"></select>
      <label for="notes">Notes</label>
      <textarea id="notes" aria-label="Notes"></textarea>
      <fieldset id="qr1-options">
        <legend>Q-R1</legend>
        <label><input type="radio" name="qr1" value="yes">Q-R1 yes</label>
        <label><input type="radio" name="qr1" value="partially">Q-R1 partially</label>
        <label><input type="radio" name="qr1" value="no">Q-R1 no</label>
      </fieldset>
      <fieldset id="qr2-options" hidden>
        <legend>Q-R2</legend>
        <label><input type="radio" name="qr2" value="yes">Q-R2 yes</label>
        <label><input type="radio" name="qr2" value="no">Q-R2 no</label>
      </fieldset>
      <button data-testid="previous" type="button">Previous</button>
      <button data-testid="next" type="button">Save and next</button>
    </section>
    <section data-testid="review-screen" hidden></section>
    <button data-testid="export-csv" type="button" disabled>Download completed CSV</button>
    <p data-testid="error" role="alert"></p>
  </main>
  <script>
    const STORAGE_KEY = {storage_key};
    const DATA_B64 = {data_b64};
  </script>
</body>
</html>"""


FINALIZATION_PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Design 02 labeling finalization</title>
</head>
<body>
  <main>
    <h1>Design 02 labeling finalization</h1>
    <p data-testid="finalization-status">Finalization support will be added in a later task.</p>
    <p data-testid="primary-source-sha">{primary_sha}</p>
    <p data-testid="reliability-source-sha">{reliability_sha}</p>
  </main>
</body>
</html>"""


class HelperContractError(RuntimeError):
    """Raised when a blind labeling instrument violates its frozen contract."""


@dataclass(frozen=True)
class BlindRow:
    unit_id: str
    design: str
    context_and_response: str
    turns: Tuple[str, ...]


@dataclass(frozen=True)
class Instrument:
    path: Path
    sha256: str
    fieldnames: Tuple[str, ...]
    rows: Tuple[BlindRow, ...]


@dataclass(frozen=True)
class InstrumentBundle:
    primary: Instrument
    reliability: Instrument


def _load_one(
    path: Path, expected_sha: str, expected_turn_counts: Tuple[int, ...]
) -> Instrument:
    path = Path(path)
    raw = path.read_bytes()
    actual_sha = hashlib.sha256(raw).hexdigest()
    if actual_sha != expected_sha:
        raise HelperContractError(
            f"source SHA-256 mismatch for {path}: expected {expected_sha}, got {actual_sha}"
        )

    reader = csv.DictReader(io.StringIO(raw.decode("utf-8"), newline=""))
    fieldnames = tuple(reader.fieldnames or ())
    if fieldnames != HEADER:
        raise HelperContractError(
            f"source header mismatch for {path}: expected {HEADER!r}, got {fieldnames!r}"
        )

    source_rows = list(reader)
    if len(source_rows) != len(expected_turn_counts):
        raise HelperContractError(
            f"source row count mismatch for {path}: expected "
            f"{len(expected_turn_counts)}, got {len(source_rows)}"
        )

    rows = []
    for index, (source_row, expected_turn_count) in enumerate(
        zip(source_rows, expected_turn_counts)
    ):
        if None in source_row or any(
            source_row.get(fieldname) is None for fieldname in HEADER
        ):
            raise HelperContractError(
                f"source row cardinality mismatch at row {index}"
            )

        expected_unit_id = f"{DESIGN}-U{index:03d}"
        if source_row["unit_id"] != expected_unit_id:
            raise HelperContractError(
                f"source unit ID mismatch at row {index}: expected "
                f"{expected_unit_id!r}, got {source_row['unit_id']!r}"
            )
        if source_row["design"] != DESIGN:
            raise HelperContractError(
                f"source design mismatch at row {index}: expected "
                f"{DESIGN!r}, got {source_row['design']!r}"
            )

        populated_label_fields = [
            fieldname for fieldname in HEADER[3:] if source_row[fieldname] != ""
        ]
        if populated_label_fields:
            raise HelperContractError(
                f"source label cells must be blank at row {index}: "
                f"{populated_label_fields!r}"
            )

        context_and_response = source_row["context_and_response"]
        turns = tuple(context_and_response.split(TURN_DELIMITER))
        if len(turns) != expected_turn_count:
            raise HelperContractError(
                f"source turn count mismatch at row {index}: expected "
                f"{expected_turn_count}, got {len(turns)}"
            )
        if any(not turn.strip() for turn in turns):
            raise HelperContractError(f"source contains an empty turn at row {index}")

        rows.append(
            BlindRow(
                unit_id=source_row["unit_id"],
                design=source_row["design"],
                context_and_response=context_and_response,
                turns=turns,
            )
        )

    return Instrument(
        path=path,
        sha256=actual_sha,
        fieldnames=fieldnames,
        rows=tuple(rows),
    )


def _validate_overlap(primary: Instrument, reliability: Instrument) -> None:
    primary_overlap = primary.rows[:4]
    if tuple(row.unit_id for row in reliability.rows) != tuple(
        row.unit_id for row in primary_overlap
    ):
        raise HelperContractError(
            "reliability unit IDs must equal the first four primary unit IDs"
        )
    if tuple(row.context_and_response for row in reliability.rows) != tuple(
        row.context_and_response for row in primary_overlap
    ):
        raise HelperContractError(
            "reliability contexts must equal the first four primary contexts"
        )


def load_instruments(primary_path: Path, reliability_path: Path) -> InstrumentBundle:
    primary = _load_one(primary_path, PRIMARY_SHA256, PRIMARY_TURN_COUNTS)
    reliability = _load_one(
        reliability_path, RELIABILITY_SHA256, RELIABILITY_TURN_COUNTS
    )

    _validate_overlap(primary, reliability)

    return InstrumentBundle(primary=primary, reliability=reliability)


def _payload(instrument: Instrument, role: str) -> str:
    payload = {
        "header": list(instrument.fieldnames),
        "role": role,
        "rows": [
            {
                "context_and_response": row.context_and_response,
                "design": row.design,
                "turns": list(row.turns),
                "unit_id": row.unit_id,
            }
            for row in instrument.rows
        ],
        "schema_version": "walkworthy-design02-helper-v1",
        "source_sha256": instrument.sha256,
        "turn_states": list(TURN_STATES),
    }
    encoded = json.dumps(
        payload, ensure_ascii=False, separators=(",", ":"), sort_keys=True
    ).encode("utf-8")
    return base64.b64encode(encoded).decode("ascii")


def _storage_key(role: str, sha: str) -> str:
    return f"walkworthy:{DESIGN}:{role}:{sha}"


def render_label_page(instrument: Instrument, role: str) -> str:
    titles = {
        "primary": "Primary labeling",
        "reliability": "Independent reliability",
    }
    if role not in titles:
        raise HelperContractError(f"unsupported labeling role: {role!r}")
    if not isinstance(instrument.sha256, str) or re.fullmatch(
        r"[0-9a-f]{64}", instrument.sha256
    ) is None:
        raise HelperContractError("source SHA-256 must be 64 lowercase hex characters")

    return LABEL_PAGE_TEMPLATE.format(
        title=titles[role],
        unit_ids=escape(",".join(row.unit_id for row in instrument.rows), quote=True),
        storage_key=json.dumps(_storage_key(role, instrument.sha256)),
        data_b64=json.dumps(_payload(instrument, role)),
    )


def render_finalization_page(bundle: InstrumentBundle) -> str:
    return FINALIZATION_PAGE_TEMPLATE.format(
        primary_sha=escape(bundle.primary.sha256),
        reliability_sha=escape(bundle.reliability.sha256),
    )


def render_readme() -> str:
    return """# WALKWORTHY Design 02 labeling helper

Open the role-specific HTML file locally. Finalization support will be added in a later task.
"""


def generate(bundle: InstrumentBundle, output_dir: Path) -> None:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    unexpected = tuple(
        sorted(
            entry.name
            for entry in output_dir.iterdir()
            if entry.name not in OUTPUT_NAMES
            or not entry.is_file()
            or entry.is_symlink()
        )
    )
    if unexpected:
        raise HelperContractError(f"unexpected output entries: {unexpected!r}")

    contents = (
        render_label_page(bundle.primary, "primary"),
        render_label_page(
            bundle.reliability, "reliability"
        ),
        render_finalization_page(bundle),
        render_readme(),
    )
    for filename, document in zip(OUTPUT_NAMES, contents):
        with (output_dir / filename).open(
            "w", encoding="utf-8", newline="\n"
        ) as destination:
            destination.write(document.rstrip("\n") + "\n")
