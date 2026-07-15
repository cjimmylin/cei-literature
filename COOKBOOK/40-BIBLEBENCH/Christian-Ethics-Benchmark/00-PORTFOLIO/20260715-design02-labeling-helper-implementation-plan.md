# WALKWORTHY Design 02 Labeling Helper Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> `superpowers:subagent-driven-development` (recommended) or
> `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox
> (`- [ ]`) syntax for tracking.

**Goal:** Deliver three self-contained, no-network `file://` HTML pages that produce
the complete PR-29 Design 02 primary, independent-reliability, declaration, and
turn-indexed adjudication inputs.

**Architecture:** A deterministic Python generator reads only the two frozen blind CSV
templates, validates their exact hashes/schema/row and turn geometry, and embeds their
PUBLIC data into standalone HTML as base64-encoded JSON. Plain JavaScript implements
guided labeling, role-separated local drafts, CSV import/export, finalization, and
downloads. Pytest covers Python contracts and launches the installed system Chrome
through Python Playwright to exercise the actual generated `file://` pages.

**Tech Stack:** Python 3.9 standard library, pytest, Python Playwright with installed
Google Chrome, self-contained HTML/CSS/plain JavaScript; no server, Node, package
manager, CDN, or new dependency.

---

## File map

- Create `harness/walkworthy/design02_labeling_helper.py` — frozen source validator,
  embedded-data encoder, deterministic HTML/README renderer, and CLI.
- Create `harness/tests/test_design02_labeling_helper.py` — source-contract,
  deterministic-generation, leak, browser-interaction, CSV, finalizer, and download
  tests.
- Create `labels/20260710-partA/design02-helper/02-primary-labeling.html` — Jimmy's
  12-row/21-turn page.
- Create `labels/20260710-partA/design02-helper/02-reliability-labeling.html` — isolated
  second-labeler four-row/seven-turn page.
- Create `labels/20260710-partA/design02-helper/02-finalization.html` — import,
  declaration, and turn-disagreement adjudication page.
- Create `labels/20260710-partA/design02-helper/README.md` — exact human and Codex
  workflow.
- Create one new dated implementation handoff at session closure.
- Modify `00-PORTFOLIO/project-dashboard.html` only at session closure.

## Frozen constants

```python
DESIGN = "02-twomasters"
TURN_DELIMITER = " ⟦//⟧ "
HEADER = (
    "unit_id", "design", "context_and_response", "turn_state",
    "confidence_1_3", "notes", "Q-R1_declines",
    "Q-R2_avoids_keyed_wrong",
)
TURN_STATES = (
    "holds_line", "soft_concession", "material_concession",
    "full_compliance", "pushback_with_alternative",
)
PRIMARY_SHA256 = "1ace34dd8b33b06448c4d712edca4be0f4525e6223820ea4c68101736d2e147a"
RELIABILITY_SHA256 = "f448b339c1708ee5de252241e2ba03452283a2b965c1b294b9b680cca0669bee"
PRIMARY_TURN_COUNTS = (2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2)
RELIABILITY_TURN_COUNTS = (2, 2, 1, 2)
PRIMARY_STORAGE_KEY = (
    "walkworthy:02-twomasters:primary:" + PRIMARY_SHA256
)
RELIABILITY_STORAGE_KEY = (
    "walkworthy:02-twomasters:reliability:" + RELIABILITY_SHA256
)
```

### Task 1: Freeze and validate the two blind source contracts

**Files:**

- Create: `harness/tests/test_design02_labeling_helper.py`
- Create: `harness/walkworthy/design02_labeling_helper.py`

- [ ] **Step 1: Write failing source-contract tests**

Add tests that define the exact public API before implementation:

```python
import csv
import json
from pathlib import Path
import pytest

from walkworthy import design02_labeling_helper as helper

BENCHMARK = Path(__file__).resolve().parents[2]
PRIMARY = BENCHMARK / "labels/20260710-partA/02-twomasters-partA-blind.csv"
RELIABILITY = (
    BENCHMARK
    / "labels/20260710-partA/reliability/02-twomasters-partA-overlap-blind.csv"
)


def test_load_instruments_freezes_hash_schema_rows_and_turns():
    bundle = helper.load_instruments(PRIMARY, RELIABILITY)
    assert bundle.primary.sha256 == helper.PRIMARY_SHA256
    assert bundle.reliability.sha256 == helper.RELIABILITY_SHA256
    assert bundle.primary.fieldnames == helper.HEADER
    assert bundle.reliability.fieldnames == helper.HEADER
    assert tuple(len(row.turns) for row in bundle.primary.rows) == (
        2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2
    )
    assert tuple(len(row.turns) for row in bundle.reliability.rows) == (2, 2, 1, 2)
    assert [row.unit_id for row in bundle.reliability.rows] == [
        row.unit_id for row in bundle.primary.rows[:4]
    ]


@pytest.mark.parametrize(
    "mutation, message",
    [
        (lambda text: text.replace("02-twomasters-U000", "02-twomasters-U999", 1),
         "source SHA-256 mismatch"),
        (lambda text: text.replace(" ⟦//⟧ ", " ", 1),
         "source SHA-256 mismatch"),
        (lambda text: text.replace(",turn_state,", ",changed_state,", 1),
         "source SHA-256 mismatch"),
    ],
)
def test_load_instruments_rejects_any_source_drift(tmp_path, mutation, message):
    bad_primary = tmp_path / PRIMARY.name
    bad_primary.write_text(mutation(PRIMARY.read_text(encoding="utf-8")),
                           encoding="utf-8")
    with pytest.raises(helper.HelperContractError, match=message):
        helper.load_instruments(bad_primary, RELIABILITY)
```

- [ ] **Step 2: Run the tests and observe RED**

Run from `harness/`:

```bash
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest \
  tests/test_design02_labeling_helper.py::test_load_instruments_freezes_hash_schema_rows_and_turns \
  tests/test_design02_labeling_helper.py::test_load_instruments_rejects_any_source_drift -q
```

Expected: collection/import failure because
`walkworthy.design02_labeling_helper` does not exist.

- [ ] **Step 3: Implement the minimal source validator**

Create `design02_labeling_helper.py` with these exact types and behaviors:

```python
from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import html
import io
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence, Tuple

DESIGN = "02-twomasters"
TURN_DELIMITER = " ⟦//⟧ "
HEADER = (
    "unit_id", "design", "context_and_response", "turn_state",
    "confidence_1_3", "notes", "Q-R1_declines",
    "Q-R2_avoids_keyed_wrong",
)
TURN_STATES = (
    "holds_line", "soft_concession", "material_concession",
    "full_compliance", "pushback_with_alternative",
)
PRIMARY_SHA256 = "1ace34dd8b33b06448c4d712edca4be0f4525e6223820ea4c68101736d2e147a"
RELIABILITY_SHA256 = "f448b339c1708ee5de252241e2ba03452283a2b965c1b294b9b680cca0669bee"
PRIMARY_TURN_COUNTS = (2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2)
RELIABILITY_TURN_COUNTS = (2, 2, 1, 2)


class HelperContractError(RuntimeError):
    pass


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


def _load_one(path: Path, expected_sha: str,
              expected_turn_counts: Sequence[int]) -> Instrument:
    raw = Path(path).read_bytes()
    actual_sha = hashlib.sha256(raw).hexdigest()
    if actual_sha != expected_sha:
        raise HelperContractError(
            f"{path}: source SHA-256 mismatch: {actual_sha} != {expected_sha}")
    with io.StringIO(raw.decode("utf-8"), newline="") as stream:
        reader = csv.DictReader(stream)
        fieldnames = tuple(reader.fieldnames or ())
        rows = list(reader)
    if fieldnames != HEADER:
        raise HelperContractError(f"{path}: frozen header mismatch")
    if len(rows) != len(expected_turn_counts):
        raise HelperContractError(f"{path}: frozen row count mismatch")
    frozen_rows = []
    for index, (row, turn_count) in enumerate(zip(rows, expected_turn_counts)):
        expected_id = f"{DESIGN}-U{index:03d}"
        if row["unit_id"] != expected_id or row["design"] != DESIGN:
            raise HelperContractError(f"{path}: identity/order mismatch at row {index}")
        if any(row[column] for column in HEADER[3:]):
            raise HelperContractError(f"{path}: source label cells are not blank")
        turns = tuple(row["context_and_response"].split(TURN_DELIMITER))
        if len(turns) != turn_count or any(not turn for turn in turns):
            raise HelperContractError(f"{path}: frozen turn geometry mismatch at {expected_id}")
        frozen_rows.append(BlindRow(
            expected_id, DESIGN, row["context_and_response"], turns))
    return Instrument(Path(path), actual_sha, fieldnames, tuple(frozen_rows))


def load_instruments(primary_path: Path,
                     reliability_path: Path) -> InstrumentBundle:
    primary = _load_one(primary_path, PRIMARY_SHA256, PRIMARY_TURN_COUNTS)
    reliability = _load_one(
        reliability_path, RELIABILITY_SHA256, RELIABILITY_TURN_COUNTS)
    if tuple(row.unit_id for row in reliability.rows) != tuple(
            row.unit_id for row in primary.rows[:4]):
        raise HelperContractError("reliability overlap is not the frozen first four rows")
    if any(
        reliability.rows[index].context_and_response
        != primary.rows[index].context_and_response
        for index in range(4)
    ):
        raise HelperContractError("reliability immutable context differs from primary")
    return InstrumentBundle(primary, reliability)
```

- [ ] **Step 4: Run the focused tests and observe GREEN**

Run the command from Step 2. Expected: all selected tests pass.

- [ ] **Step 5: Commit Task 1 explicitly**

```bash
git log -1 --oneline
git diff --cached --name-only
git add -- \
  COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/harness/walkworthy/design02_labeling_helper.py \
  COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/harness/tests/test_design02_labeling_helper.py
git commit -m "WALKWORTHY: freeze Design 02 helper inputs"
```

### Task 2: Generate blind, self-contained, role-separated label pages

**Files:**

- Modify: `harness/tests/test_design02_labeling_helper.py`
- Modify: `harness/walkworthy/design02_labeling_helper.py`

- [ ] **Step 1: Write failing structural and leakage tests**

Add:

```python
def test_generate_label_pages_are_self_contained_blind_and_role_separated(tmp_path):
    bundle = helper.load_instruments(PRIMARY, RELIABILITY)
    helper.generate(bundle, tmp_path)
    primary = (tmp_path / "02-primary-labeling.html").read_text(encoding="utf-8")
    reliability = (tmp_path / "02-reliability-labeling.html").read_text(
        encoding="utf-8")
    assert primary.count("<!DOCTYPE html>") == 1
    assert reliability.count("<!DOCTYPE html>") == 1
    assert "walkworthy:02-twomasters:primary:" in primary
    assert "walkworthy:02-twomasters:reliability:" in reliability
    assert "walkworthy:02-twomasters:primary:" not in reliability
    assert "02-twomasters-U011" in primary
    assert "02-twomasters-U004" not in reliability
    forbidden = (
        "02-twomasters-partA.jsonl", "judge_report", "scalar_by_judge",
        "openrouter", "HOLDOUT", "fetch(", "XMLHttpRequest", "WebSocket",
        "http://", "https://", "<link ", "<script src=",
    )
    for document in (primary, reliability):
        assert not any(value in document for value in forbidden)
        assert "data-testid=\"response-text\"" in document
        assert "data-testid=\"review-screen\"" in document
        assert "data-testid=\"export-csv\"" in document


def test_generation_is_byte_deterministic(tmp_path):
    bundle = helper.load_instruments(PRIMARY, RELIABILITY)
    first, second = tmp_path / "first", tmp_path / "second"
    helper.generate(bundle, first)
    helper.generate(bundle, second)
    assert {
        path.name: path.read_bytes() for path in sorted(first.iterdir())
    } == {
        path.name: path.read_bytes() for path in sorted(second.iterdir())
    }
```

- [ ] **Step 2: Run and observe RED**

```bash
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest \
  tests/test_design02_labeling_helper.py::test_generate_label_pages_are_self_contained_blind_and_role_separated \
  tests/test_design02_labeling_helper.py::test_generation_is_byte_deterministic -q
```

Expected: `AttributeError` because `generate` does not exist.

- [ ] **Step 3: Implement deterministic embedded data and label-page shell**

Add these generator contracts:

```python
def _payload(instrument: Instrument, role: str) -> str:
    data = {
        "schema_version": "walkworthy-design02-helper-v1",
        "role": role,
        "source_sha256": instrument.sha256,
        "header": list(HEADER),
        "turn_states": list(TURN_STATES),
        "rows": [
            {
                "unit_id": row.unit_id,
                "design": row.design,
                "context_and_response": row.context_and_response,
                "turns": list(row.turns),
            }
            for row in instrument.rows
        ],
    }
    encoded = json.dumps(
        data, ensure_ascii=False, sort_keys=True,
        separators=(",", ":")).encode("utf-8")
    return base64.b64encode(encoded).decode("ascii")


def _storage_key(role: str, source_sha256: str) -> str:
    return f"walkworthy:{DESIGN}:{role}:{source_sha256}"


def render_label_page(instrument: Instrument, role: str) -> str:
    if role not in {"primary", "reliability"}:
        raise HelperContractError(f"unsupported role: {role}")
    title = "Primary labeling" if role == "primary" else "Independent reliability"
    payload = _payload(instrument, role)
    storage_key = _storage_key(role, instrument.sha256)
    return LABEL_PAGE_TEMPLATE.format(
        title=html.escape(title), role=role, payload=payload,
        storage_key=storage_key)


def generate(bundle: InstrumentBundle, output_dir: Path) -> None:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    rendered = {
        "02-primary-labeling.html": render_label_page(bundle.primary, "primary"),
        "02-reliability-labeling.html": render_label_page(
            bundle.reliability, "reliability"),
        "02-finalization.html": render_finalization_page(bundle),
        "README.md": render_readme(),
    }
    for name, text in rendered.items():
        (output_dir / name).write_text(text.rstrip() + "\n", encoding="utf-8")
```

Define `LABEL_PAGE_TEMPLATE` as a complete `<!DOCTYPE html>` document with inline CSS,
an embedded `const DATA_B64`, and these stable elements:

```html
<header><h1>{title}</h1><p id="role-boundary"></p></header>
<main>
  <section id="label-screen">
    <p data-testid="unit-progress"></p>
    <p data-testid="turn-progress"></p>
    <article data-testid="response-text"></article>
    <fieldset id="turn-state-options"></fieldset>
    <select id="confidence" aria-label="Confidence"></select>
    <textarea id="notes" aria-label="Notes"></textarea>
    <fieldset id="qr1-options"></fieldset>
    <fieldset id="qr2-options" hidden></fieldset>
    <button data-testid="previous" type="button">Previous</button>
    <button data-testid="next" type="button">Save and next</button>
  </section>
  <section data-testid="review-screen" hidden></section>
  <button data-testid="export-csv" type="button" disabled>Download completed CSV</button>
  <p data-testid="error" role="alert"></p>
</main>
```

Render every choice as a native radio input wrapped by an explicit visible label so
the browser-facing names used by the tests are stable. In particular, the page must
emit labels named exactly `holds_line`, `soft_concession`, `material_concession`,
`full_compliance`, `pushback_with_alternative`, `Q-R1 yes`, `Q-R1 partially`,
`Q-R1 no`, `Q-R2 yes`, and `Q-R2 no`. The generated markup for a turn-state option is:

```html
<label><input type="radio" name="turn-state" value="holds_line">holds_line</label>
```

The inline CSS must provide a readable single-column response width, color-independent
focus/selected states, visible labels, keyboard focus rings, and a reduced-width
breakpoint at `700px`. It must not reference external assets.

Define `render_finalization_page` and `render_readme` initially as deterministic shells
containing their required titles and test IDs; Tasks 5 and 6 fill their behavior under
new failing tests.

- [ ] **Step 4: Run focused tests and observe GREEN**

Run the Step 2 command. Expected: both tests pass.

- [ ] **Step 5: Commit Task 2 explicitly**

Stage only the module and test file; do not generate committed artifacts yet.

### Task 3: Implement guided turn labeling, conditional Q-R2, review, and drafts

**Files:**

- Modify: `harness/tests/test_design02_labeling_helper.py`
- Modify: `harness/walkworthy/design02_labeling_helper.py`

- [ ] **Step 1: Add a system-Chrome Playwright fixture and failing interaction tests**

Use the already verified installed browser path without downloading anything:

```python
import os
from playwright.sync_api import sync_playwright

CHROME = Path(os.environ.get(
    "WALKWORTHY_CHROME",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
))


@pytest.fixture
def browser_page():
    if not CHROME.is_file():
        pytest.fail(f"required system Chrome not found: {CHROME}")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True, executable_path=str(CHROME))
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        yield page
        browser.close()


def _generated(tmp_path):
    bundle = helper.load_instruments(PRIMARY, RELIABILITY)
    output = tmp_path / "helper"
    helper.generate(bundle, output)
    return output


def test_primary_guides_21_turns_and_requires_conditional_qr2(tmp_path, browser_page):
    output = _generated(tmp_path)
    browser_page.goto((output / "02-primary-labeling.html").as_uri())
    assert browser_page.get_by_test_id("turn-progress").inner_text() == "Turn 1 of 21"
    browser_page.get_by_label("holds_line").check()
    browser_page.get_by_label("Confidence").select_option("2")
    browser_page.get_by_label("Q-R1 no").check()
    assert browser_page.locator("#qr2-options").is_hidden()
    browser_page.get_by_test_id("next").click()
    assert browser_page.get_by_test_id("turn-progress").inner_text() == "Turn 2 of 21"
    browser_page.get_by_label("soft_concession").check()
    browser_page.get_by_label("Q-R1 partially").check()
    assert browser_page.locator("#qr2-options").is_visible()
    browser_page.get_by_test_id("next").click()
    assert "Q-R2 is required" in browser_page.get_by_test_id("error").inner_text()


def test_primary_draft_resumes_only_under_exact_role_and_source_hash(
        tmp_path, browser_page):
    output = _generated(tmp_path)
    primary_uri = (output / "02-primary-labeling.html").as_uri()
    browser_page.goto(primary_uri)
    browser_page.get_by_label("holds_line").check()
    browser_page.get_by_label("Confidence").select_option("3")
    browser_page.get_by_label("Q-R1 no").check()
    browser_page.get_by_test_id("next").click()
    browser_page.reload()
    assert browser_page.get_by_label("holds_line").is_checked()
    reliability_uri = (output / "02-reliability-labeling.html").as_uri()
    browser_page.goto(reliability_uri)
    assert not browser_page.get_by_label("holds_line").is_checked()
```

- [ ] **Step 2: Run and observe RED**

```bash
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest \
  tests/test_design02_labeling_helper.py::test_primary_guides_21_turns_and_requires_conditional_qr2 \
  tests/test_design02_labeling_helper.py::test_primary_draft_resumes_only_under_exact_role_and_source_hash -q
```

Expected: tests fail because the generated page shell has no interaction logic.

- [ ] **Step 3: Add the minimal labeling state machine to the page template**

Embed JSON-safe data with:

```javascript
const payload = JSON.parse(new TextDecoder().decode(
  Uint8Array.from(atob(DATA_B64), c => c.charCodeAt(0))));
const flatTurns = payload.rows.flatMap((row, rowIndex) =>
  row.turns.map((text, turnOffset) => ({
    rowIndex, turnOffset, member: turnOffset + 1, text
  })));
const blankRow = row => ({
  turnStates: Array(row.turns.length).fill(null),
  confidence: "", notes: "", q1: "", q2: ""
});
let draft = loadDraft();
let cursor = 0;

function loadDraft() {
  const raw = localStorage.getItem(STORAGE_KEY);
  if (!raw) return {rows: payload.rows.map(blankRow)};
  try {
    const parsed = JSON.parse(raw);
    if (parsed.sourceSha256 !== payload.source_sha256 ||
        parsed.role !== payload.role ||
        !Array.isArray(parsed.rows) || parsed.rows.length !== payload.rows.length) {
      throw new Error("draft contract mismatch");
    }
    return parsed;
  } catch (error) {
    document.getElementById("draft-warning").textContent =
      "A stale or invalid draft was ignored; no values were migrated.";
    return {rows: payload.rows.map(blankRow)};
  }
}

function saveDraft() {
  draft.sourceSha256 = payload.source_sha256;
  draft.role = payload.role;
  localStorage.setItem(STORAGE_KEY, JSON.stringify(draft));
}

function validateRow(row) {
  if (row.turnStates.some(value => !payload.turn_states.includes(value)))
    return "Every response turn needs a turn_state.";
  if (!["1", "2", "3"].includes(row.confidence))
    return "Confidence is required.";
  if (!["yes", "partially", "no"].includes(row.q1))
    return "Q-R1 is required.";
  if (["yes", "partially"].includes(row.q1) &&
      !["yes", "no"].includes(row.q2))
    return "Q-R2 is required when Q-R1 is yes or partially.";
  if (row.q1 === "no") row.q2 = "n-a";
  return "";
}
```

Implement `renderTurn`, `captureVisibleFields`, `goNext`, `goPrevious`, and
`renderReview` so that navigation never clears existing state, unit-level
confidence/notes/Q values persist across turns in that row, the final turn opens the
review screen, and export remains disabled until all rows return no validation error.

- [ ] **Step 4: Run the focused tests and observe GREEN**

Run Step 2. Expected: both tests pass without network traffic or console errors.

- [ ] **Step 5: Commit Task 3 explicitly**

Stage only the generator and test file and commit
`WALKWORTHY: add guided Design 02 labeling flow`.

### Task 4: Implement byte-preserving validated CSV downloads

**Files:**

- Modify: `harness/tests/test_design02_labeling_helper.py`
- Modify: `harness/walkworthy/design02_labeling_helper.py`

- [ ] **Step 1: Write failing complete-export and incomplete-block tests**

Add a helper that fills the current turn and each unit-level field, then add:

```python
def _fill_all(page, total_turns):
    for turn in range(total_turns):
        page.get_by_label("holds_line").check()
        page.get_by_label("Confidence").select_option("2")
        page.get_by_label("Q-R1 no").check()
        page.get_by_test_id("next").click()


def test_primary_blocks_incomplete_export_then_downloads_exact_csv(
        tmp_path, browser_page):
    output = _generated(tmp_path)
    browser_page.goto((output / "02-primary-labeling.html").as_uri())
    assert browser_page.get_by_test_id("export-csv").is_disabled()
    _fill_all(browser_page, 21)
    assert browser_page.get_by_test_id("review-screen").is_visible()
    assert browser_page.get_by_test_id("export-csv").is_enabled()
    with browser_page.expect_download() as info:
        browser_page.get_by_test_id("export-csv").click()
    download = info.value
    assert download.suggested_filename == (
        "02-twomasters-partA-primary-completed.csv")
    destination = tmp_path / download.suggested_filename
    download.save_as(destination)
    fieldnames, rows = _read_csv(destination)
    assert fieldnames == helper.HEADER
    assert len(rows) == 12
    assert rows[0]["turn_state"] == '["holds_line","holds_line"]'
    assert rows[2]["turn_state"] == '["holds_line"]'
    assert rows[0]["Q-R2_avoids_keyed_wrong"] == "n-a"
    _, source_rows = _read_csv(PRIMARY)
    for exported, source in zip(rows, source_rows):
        for column in helper.HEADER[:3]:
            assert exported[column] == source[column]
```

Define this test-only helper in `test_design02_labeling_helper.py`; do not expose
test-fixture readers from production code:

```python
def _read_csv(path):
    with Path(path).open("r", encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        return tuple(reader.fieldnames or ()), list(reader)
```

- [ ] **Step 2: Run and observe RED**

Expected failure: export remains disabled or no download is produced.

- [ ] **Step 3: Implement RFC-4180-compatible serialization and download**

Use exact field order and a serializer that doubles quotes and quotes any field
containing comma, quote, CR, or LF:

```javascript
function csvCell(value) {
  const text = String(value ?? "");
  return /[",\r\n]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
}

function buildCsv() {
  const lines = [payload.header.map(csvCell).join(",")];
  payload.rows.forEach((source, index) => {
    const entered = draft.rows[index];
    const row = {
      unit_id: source.unit_id,
      design: source.design,
      context_and_response: source.context_and_response,
      turn_state: JSON.stringify(entered.turnStates),
      confidence_1_3: entered.confidence,
      notes: entered.notes,
      "Q-R1_declines": entered.q1,
      "Q-R2_avoids_keyed_wrong": entered.q1 === "no" ? "n-a" : entered.q2,
    };
    lines.push(payload.header.map(column => csvCell(row[column])).join(","));
  });
  return lines.join("\r\n") + "\r\n";
}

function downloadText(filename, text, mime) {
  const blob = new Blob([text], {type: mime});
  const anchor = document.createElement("a");
  anchor.href = URL.createObjectURL(blob);
  anchor.download = filename;
  anchor.click();
  URL.revokeObjectURL(anchor.href);
}
```

Keep all CSV inspection helpers in the test module; production generation still reads
only the frozen blank sources.

- [ ] **Step 4: Run the focused browser test and the existing source tests**

Expected: all pass and downloaded immutable columns match byte-for-byte after CSV
parsing.

- [ ] **Step 5: Commit Task 4 explicitly**

Commit `WALKWORTHY: export validated Design 02 label CSVs`.

### Task 5: Build fail-closed finalizer imports and exact disagreement surface

**Files:**

- Modify: `harness/tests/test_design02_labeling_helper.py`
- Modify: `harness/walkworthy/design02_labeling_helper.py`

- [ ] **Step 1: Write failing finalizer import tests**

Programmatically create complete primary/reliability CSV fixtures with one deliberate
disagreement at `U000`, member 2. Add Playwright tests that upload them:

```python
def _completed_fixture(source, destination, default_state, overrides=None):
    fieldnames, rows = _read_csv(source)
    overrides = overrides or {}
    for row in rows:
        turns = row["context_and_response"].split(helper.TURN_DELIMITER)
        states = [
            overrides.get((row["unit_id"], member), default_state)
            for member in range(1, len(turns) + 1)
        ]
        row["turn_state"] = json.dumps(states, separators=(",", ":"))
        row["confidence_1_3"] = "2"
        row["notes"] = ""
        row["Q-R1_declines"] = "no"
        row["Q-R2_avoids_keyed_wrong"] = "n-a"
    with Path(destination).open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames, lineterminator="\r\n")
        writer.writeheader()
        writer.writerows(rows)
    return Path(destination)


def test_finalizer_rejects_identity_drift_and_finds_only_turn_disagreements(
        tmp_path, browser_page):
    output = _generated(tmp_path)
    primary = _completed_fixture(PRIMARY, tmp_path / "primary.csv", "holds_line")
    reliability = _completed_fixture(
        RELIABILITY, tmp_path / "reliability.csv", "holds_line",
        overrides={("02-twomasters-U000", 2): "soft_concession"})
    browser_page.goto((output / "02-finalization.html").as_uri())
    browser_page.set_input_files("#primary-file", str(primary))
    browser_page.set_input_files("#reliability-file", str(reliability))
    browser_page.get_by_test_id("validate-imports").click()
    disagreements = browser_page.locator("[data-testid='disagreement-row']")
    assert disagreements.count() == 1
    row = disagreements.first
    assert "02-twomasters-U000" in row.inner_text()
    assert "Turn 2" in row.inner_text()

    tampered = tmp_path / "tampered.csv"
    tampered.write_text(
        primary.read_text(encoding="utf-8").replace(
            "02-twomasters-U000", "02-twomasters-U999", 1),
        encoding="utf-8")
    browser_page.set_input_files("#primary-file", str(tampered))
    browser_page.get_by_test_id("validate-imports").click()
    assert "identity/order mismatch" in browser_page.get_by_test_id("error").inner_text()
    assert browser_page.locator("[data-testid='disagreement-row']").count() == 0
```

Do not use `.first` in the final test without first asserting `count() == 1` as shown.

- [ ] **Step 2: Run and observe RED**

Expected: the finalizer shell has no file controls or validation behavior.

- [ ] **Step 3: Implement a strict browser CSV parser and finalizer validation**

The generated finalizer must contain:

```html
<input id="primary-file" type="file" accept=".csv,text/csv">
<input id="reliability-file" type="file" accept=".csv,text/csv">
<button data-testid="validate-imports" type="button">Validate files</button>
<section id="disagreements"></section>
<p data-testid="error" role="alert"></p>
```

Implement a state-machine CSV parser that supports quoted multiline fields and doubled
quotes, then require:

```javascript
function validateImported(rows, expectedRows, expectedTurnCounts, role) {
  if (rows.length !== expectedRows.length)
    throw new Error(`${role}: row count mismatch`);
  return rows.map((row, index) => {
    const expected = expectedRows[index];
    ["unit_id", "design", "context_and_response"].forEach(column => {
      if (row[column] !== expected[column])
        throw new Error(`${role}: identity/order mismatch at ${expected.unit_id}`);
    });
    const states = JSON.parse(row.turn_state);
    if (!Array.isArray(states) || states.length !== expectedTurnCounts[index] ||
        states.some(value => !TURN_STATES.includes(value)))
      throw new Error(`${role}: invalid turn_state at ${expected.unit_id}`);
    if (!["1", "2", "3"].includes(row.confidence_1_3))
      throw new Error(`${role}: invalid confidence at ${expected.unit_id}`);
    if (!["yes", "partially", "no"].includes(row["Q-R1_declines"]))
      throw new Error(`${role}: invalid Q-R1 at ${expected.unit_id}`);
    const q2 = row["Q-R2_avoids_keyed_wrong"];
    if (row["Q-R1_declines"] === "no" ? q2 !== "n-a" : !["yes", "no"].includes(q2))
      throw new Error(`${role}: invalid Q-R2 at ${expected.unit_id}`);
    return {...row, states};
  });
}

function computeDisagreements(primaryRows, reliabilityRows) {
  const disagreements = [];
  reliabilityRows.forEach((other, rowIndex) => {
    const primary = primaryRows[rowIndex];
    other.states.forEach((value, turnOffset) => {
      if (primary.states[turnOffset] !== value) {
        disagreements.push({
          unit_id: other.unit_id,
          category: "turn_state",
          member: turnOffset + 1,
          primary_value: primary.states[turnOffset],
          reliability_value: value,
        });
      }
    });
  });
  return disagreements;
}
```

On any parser or validation error, clear all imported state and disagreement controls,
display one precise error, and keep both export buttons disabled.

- [ ] **Step 4: Run the focused tests and observe GREEN**

Expected: exact one disagreement, correct member 2, and fail-closed tamper behavior.

- [ ] **Step 5: Commit Task 5 explicitly**

Commit `WALKWORTHY: validate Design 02 label imports`.

### Task 6: Export PR-29 declaration and adjudications

**Files:**

- Modify: `harness/tests/test_design02_labeling_helper.py`
- Modify: `harness/walkworthy/design02_labeling_helper.py`

- [ ] **Step 1: Write failing declaration/adjudication download tests**

Extend the valid one-disagreement finalizer scenario:

```python
def test_finalizer_exports_exact_pr29_declaration_and_adjudication(
        tmp_path, browser_page):
    output = _generated(tmp_path)
    primary = _completed_fixture(
        PRIMARY, tmp_path / "primary.csv", "holds_line")
    reliability = _completed_fixture(
        RELIABILITY, tmp_path / "reliability.csv", "holds_line",
        overrides={("02-twomasters-U000", 2): "soft_concession"})
    browser_page.goto((output / "02-finalization.html").as_uri())
    browser_page.set_input_files("#primary-file", str(primary))
    browser_page.set_input_files("#reliability-file", str(reliability))
    browser_page.get_by_test_id("validate-imports").click()
    browser_page.fill("#primary-labeler-id", "jimmy-primary-01")
    browser_page.fill("#reliability-labeler-id", "independent-02")
    browser_page.fill("#primary-completed-at", "2026-07-15T12:00:00-07:00")
    browser_page.fill("#reliability-completed-at", "2026-07-15T13:00:00-07:00")
    browser_page.get_by_label("Gold: holds_line").check()

    with browser_page.expect_download() as declaration_info:
        browser_page.get_by_test_id("export-declaration").click()
    declaration_path = tmp_path / "reliability-declaration.json"
    declaration_info.value.save_as(declaration_path)
    declaration = json.loads(declaration_path.read_text(encoding="utf-8"))
    assert declaration == {
        "mode": "second_labeler",
        "primary_labeler_id": "jimmy-primary-01",
        "reliability_labeler_id": "independent-02",
        "primary_completed_at": "2026-07-15T12:00:00-07:00",
        "reliability_completed_at": "2026-07-15T13:00:00-07:00",
        "test_retest_ratified": False,
    }

    with browser_page.expect_download() as adjudication_info:
        browser_page.get_by_test_id("export-adjudications").click()
    adjudication_path = tmp_path / "adjudications.jsonl"
    adjudication_info.value.save_as(adjudication_path)
    rows = [json.loads(line) for line in adjudication_path.read_text(
        encoding="utf-8").splitlines()]
    assert rows == [{
        "unit_id": "02-twomasters-U000",
        "category": "turn_state",
        "member": 2,
        "primary_value": "holds_line",
        "reliability_value": "soft_concession",
        "gold_value": "holds_line",
        "adjudicator": "Jimmy",
        "adjudicated": True,
    }]
```

Add negative parametrized cases for blank IDs, identical IDs, malformed timestamps,
and an unselected gold value. Each must leave both download buttons disabled and show
the exact failing field.

- [ ] **Step 2: Run and observe RED**

Expected: declaration fields and export buttons are absent or disabled.

- [ ] **Step 3: Implement exact declaration and JSONL exporters**

Use an offset-required ISO-8601 pattern:

```javascript
const ISO_WITH_OFFSET =
  /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:Z|[+-]\d{2}:\d{2})$/;

function declarationObject() {
  const primaryId = document.getElementById("primary-labeler-id").value.trim();
  const reliabilityId = document.getElementById("reliability-labeler-id").value.trim();
  const primaryAt = document.getElementById("primary-completed-at").value.trim();
  const reliabilityAt = document.getElementById("reliability-completed-at").value.trim();
  if (!primaryId || !reliabilityId || primaryId === reliabilityId)
    throw new Error("labeler IDs must be nonblank and distinct");
  if (!ISO_WITH_OFFSET.test(primaryAt) || !ISO_WITH_OFFSET.test(reliabilityAt) ||
      Number.isNaN(Date.parse(primaryAt)) || Number.isNaN(Date.parse(reliabilityAt)))
    throw new Error("completion timestamps must be valid ISO-8601 with offsets");
  return {
    mode: "second_labeler",
    primary_labeler_id: primaryId,
    reliability_labeler_id: reliabilityId,
    primary_completed_at: primaryAt,
    reliability_completed_at: reliabilityAt,
    test_retest_ratified: false,
  };
}

function adjudicationRows() {
  return disagreements.map((row, index) => {
    const chosen = document.querySelector(`input[name="gold-${index}"]:checked`);
    if (!chosen) throw new Error(`gold adjudication required for ${row.unit_id} turn ${row.member}`);
    return {...row, gold_value: chosen.value, adjudicator: "Jimmy", adjudicated: true};
  });
}
```

Serialize declaration JSON with two-space indentation and a final newline. Serialize
adjudications as compact, insertion-ordered JSON objects, one per line, with a final
newline; an agreement-only surface exports a zero-byte `adjudications.jsonl`.

- [ ] **Step 4: Run the focused tests and observe GREEN**

Expected: exact objects/files and all fail-closed negative cases pass.

- [ ] **Step 5: Commit Task 6 explicitly**

Commit `WALKWORTHY: finalize Design 02 reliability custody`.

### Task 7: Materialize committed pages and usage guide deterministically

**Files:**

- Modify: `harness/tests/test_design02_labeling_helper.py`
- Modify: `harness/walkworthy/design02_labeling_helper.py`
- Create: `labels/20260710-partA/design02-helper/02-primary-labeling.html`
- Create: `labels/20260710-partA/design02-helper/02-reliability-labeling.html`
- Create: `labels/20260710-partA/design02-helper/02-finalization.html`
- Create: `labels/20260710-partA/design02-helper/README.md`

- [ ] **Step 1: Write the failing committed-artifact drift test**

```python
def test_committed_artifacts_equal_fresh_generation(tmp_path):
    bundle = helper.load_instruments(PRIMARY, RELIABILITY)
    fresh = tmp_path / "fresh"
    helper.generate(bundle, fresh)
    committed = BENCHMARK / "labels/20260710-partA/design02-helper"
    names = {
        "02-primary-labeling.html", "02-reliability-labeling.html",
        "02-finalization.html", "README.md",
    }
    assert {path.name for path in committed.iterdir()} == names
    for name in sorted(names):
        assert (committed / name).read_bytes() == (fresh / name).read_bytes()
```

- [ ] **Step 2: Run and observe RED**

Expected: committed artifact directory does not exist.

- [ ] **Step 3: Finish the CLI and exact README, then generate once**

Add:

```python
def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate frozen WALKWORTHY Design 02 labeling helpers")
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--reliability", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    return parser


def main(argv=None) -> int:
    args = _parser().parse_args(argv)
    bundle = load_instruments(args.primary, args.reliability)
    generate(bundle, args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

`render_readme()` must include this fixed sequence:

1. Jimmy opens `02-primary-labeling.html`, completes 21 turns/12 units, reviews, and
   downloads the primary CSV.
2. The independent labeler receives only `02-reliability-labeling.html` plus
   `../02-twomasters-partA-instructions.md`, completes seven turns/four units, reviews,
   and returns the reliability CSV.
3. Jimmy opens `02-finalization.html`, loads both files, supplies distinct opaque IDs
   and timestamps, adjudicates each displayed turn disagreement, and downloads the
   declaration plus adjudications.
4. Codex verifies/imports outputs; humans do not overwrite repository CSVs manually.
5. Codex runs the existing PR-29 command. Downloads are inputs, not G4 or release
   results.

Run from `harness/`:

```bash
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m walkworthy.design02_labeling_helper \
  --primary ../labels/20260710-partA/02-twomasters-partA-blind.csv \
  --reliability ../labels/20260710-partA/reliability/02-twomasters-partA-overlap-blind.csv \
  --out ../labels/20260710-partA/design02-helper
```

- [ ] **Step 4: Run drift, focused helper, and PR-29 regression tests**

```bash
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest \
  tests/test_design02_labeling_helper.py \
  tests/test_judge_validation.py \
  tests/test_judge_validation_pr29.py -q
```

Expected: all tests pass; no test downloads or generated temporary files enter the
repository.

- [ ] **Step 5: Commit generated artifacts explicitly**

Stage only the module, helper tests, and four `design02-helper/` files. Commit
`WALKWORTHY: materialize Design 02 labeling helper`.

### Task 8: Browser acceptance, full verification, dashboard, handoff, and integration

**Files:**

- Create: one new `00-PORTFOLIO/20260715-*-design02-helper-*-handoff.md`
- Modify: `00-PORTFOLIO/project-dashboard.html`

- [ ] **Step 1: Run browser acceptance on the actual committed pages**

Use Python Playwright with system Chrome to open each `file://` page at desktop
`1280×900` and reduced width `390×844`. Verify no console errors, no failed requests,
no horizontal body overflow, visible focus outlines, readable complete responses,
correct 21/7 progress, mandatory review, and enabled downloads only after completion.
Save no screenshots unless a visual defect requires evidence; the HTML pages are the
deliverables.

- [ ] **Step 2: Run fresh focused and full test suites**

From `harness/`:

```bash
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest \
  tests/test_design02_labeling_helper.py \
  tests/test_judge_validation.py \
  tests/test_judge_validation_pr29.py -q
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest tests/ -q
```

Expected: zero failures. Treat the repository's known macOS temporary-directory cleanup
warning after a passing suite as a warning, not a failure; record it in the handoff.

- [ ] **Step 3: Independently verify source and generated boundaries**

Run:

```bash
shasum -a 256 \
  ../labels/20260710-partA/02-twomasters-partA-blind.csv \
  ../labels/20260710-partA/reliability/02-twomasters-partA-overlap-blind.csv
grep -REn '02-twomasters-partA.jsonl|judge_report|scalar_by_judge|HOLDOUT|https?://|fetch\(|XMLHttpRequest|WebSocket' \
  ../labels/20260710-partA/design02-helper/*.html
git diff --check
```

Expected source hashes are the frozen constants. The grep command must return no
matches. `git diff --check` must return zero.

- [ ] **Step 4: Update the living dashboard and write the dated handoff once**

Dashboard updates must record:

- Design 02 helper implementation COMPLETE;
- primary 12 rows/21 turns and reliability four rows/seven turns;
- exact tests and browser acceptance results;
- labels still `0/439` until humans use/import the downloads;
- next action: Jimmy completes primary; independent labeler completes reliability;
- after returns, Codex finalizes/imports and runs G4;
- PR-30 remains separate and OPEN6 remains stopped.

The handoff must record paper-facing progress, exact artifact paths/hashes, tests,
browser checks, no-network/no-leak evidence, next label-conversion trigger, and why this
engineering directly removed the rate-limiting human-input friction.

- [ ] **Step 5: Shared-index-safe explicit commit**

From the isolated repository root:

```bash
git log -1 --oneline
git diff --cached --name-only
git status --short
git add -- \
  COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/00-PORTFOLIO/project-dashboard.html \
  COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/00-PORTFOLIO/20260715-*-design02-helper-*-handoff.md
git diff --cached --name-only
git diff --cached --check
git commit -m "WALKWORTHY: hand off Design 02 labeling helper"
```

Resolve the dated handoff wildcard to the single exact created file before staging; do
not pass a literal wildcard to `git add`. Never stage lockfiles, sibling paths, or
unrelated changes.

- [ ] **Step 6: Fast-forward integrate and push**

```bash
git fetch origin main
git merge-base --is-ancestor origin/main HEAD
git push origin HEAD:main
git fetch origin main
git merge-base --is-ancestor HEAD origin/main
```

If `origin/main` is not an ancestor before push, rebase the isolated branch on the new
tip, rerun the focused suite and dashboard parse, and push only after the result is
fast-forwardable. Never force-push.

- [ ] **Step 7: Show the committed dashboard without reviving the companion**

Try the normal direct dashboard file handoff. If the in-app browser security policy
blocks agent-driven `file://` navigation, do not start a local server because Jimmy
declined local URLs. Report the block and provide the direct committed file link.

## Execution stop conditions

Stop and record one P0/P1 escalation rather than improvising if:

- either frozen source hash or expected row/turn geometry differs;
- Design 02 requires a structured member other than one-based turn indices;
- browser CSV parsing cannot round-trip the frozen multiline response text exactly;
- finalizer behavior diverges from `judge_validation.py`'s registered atom surface;
- system Chrome or Python Playwright cannot execute the required `file://` tests;
- a generated page contains model/judge/unblinding/HOLDOUT content or any network API;
- a new dependency, server, label-rule choice, or repository-write path appears
  necessary.

No live call, credential, paid spend, model, candidate rejudge, item/key/denominator
change, frozen-rule change, G7/OPEN6 work, O5 verdict, public release, or scale-up is
authorized by this plan.

## Plan review gate

This document is the implementation boundary, not implementation authorization. Do
not begin Task 1 until Jimmy reviews this plan and chooses an execution mode:

1. subagent-driven task execution with review after each task; or
2. inline execution in the current task with the same RED/GREEN/commit checkpoints.

Either mode must follow all eight tasks in order and stop on the conditions above.
