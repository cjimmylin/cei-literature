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
    [hidden] {{ display: none !important; }}
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
    <p id="draft-warning" role="status" aria-live="polite"></p>
    <section id="label-screen">
      <p data-testid="unit-progress" aria-live="polite"></p>
      <p data-testid="turn-progress" aria-live="polite"></p>
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
      <button data-testid="next" type="button">Save and next</button>
    </section>
    <section data-testid="review-screen" hidden></section>
    <button data-testid="previous" type="button">Previous</button>
    <button data-testid="export-csv" type="button" disabled>Download completed CSV</button>
    <p data-testid="error" role="alert"></p>
  </main>
  <script>
    const STORAGE_KEY = {storage_key};
    const DATA_B64 = {data_b64};
    const payloadBytes = Uint8Array.from(
      atob(DATA_B64), character => character.charCodeAt(0)
    );
    const payload = JSON.parse(new TextDecoder().decode(payloadBytes));
    const sourceHeader = Object.freeze(payload.header.slice());
    const sourceTurnStates = Object.freeze(payload.turn_states.slice());
    const sourceRole = payload.role;
    const sourceRows = Object.freeze(payload.rows.map(row => Object.freeze({{
      unit_id: row.unit_id,
      design: row.design,
      context_and_response: row.context_and_response,
      turns: Object.freeze(row.turns.slice())
    }})));
    const turns = payload.rows.flatMap((row, rowIndex) =>
      row.turns.map((text, turnOffset) => ({{
        rowIndex: rowIndex,
        turnOffset: turnOffset,
        member: turnOffset + 1,
        text: text
      }}))
    );
    const confidenceValues = ["", "1", "2", "3"];
    const q1Values = ["", "yes", "partially", "no"];
    const q2Values = ["", "yes", "no", "n-a"];
    const labelScreen = document.getElementById("label-screen");
    const reviewScreen = document.querySelector('[data-testid="review-screen"]');
    const responseText = document.querySelector('[data-testid="response-text"]');
    const unitProgress = document.querySelector('[data-testid="unit-progress"]');
    const turnProgress = document.querySelector('[data-testid="turn-progress"]');
    const errorMessage = document.querySelector('[data-testid="error"]');
    const draftWarning = document.getElementById("draft-warning");
    const confidence = document.getElementById("confidence");
    const notes = document.getElementById("notes");
    const qr2Options = document.getElementById("qr2-options");
    const previousButton = document.querySelector('[data-testid="previous"]');
    const nextButton = document.querySelector('[data-testid="next"]');
    const exportButton = document.querySelector('[data-testid="export-csv"]');

    function blankRow(row) {{
      return {{
        turnStates: row.turns.map(() => null),
        confidence: "",
        notes: "",
        q1: "",
        q2: ""
      }};
    }}

    function exactKeys(value, expected) {{
      if (value === null || typeof value !== "object" || Array.isArray(value)) {{
        return false;
      }}
      const actual = Object.keys(value).sort();
      const wanted = expected.slice().sort();
      return actual.length === wanted.length &&
        actual.every((key, index) => key === wanted[index]);
    }}

    function validDraftRow(value, sourceRow) {{
      if (!exactKeys(
        value,
        ["turnStates", "confidence", "notes", "q1", "q2"]
      )) {{
        return false;
      }}
      if (!Array.isArray(value.turnStates) ||
          value.turnStates.length !== sourceRow.turns.length ||
          !value.turnStates.every(state =>
            state === null || sourceTurnStates.includes(state)
          )) {{
        return false;
      }}
      if (!confidenceValues.includes(value.confidence) ||
          typeof value.notes !== "string" ||
          !q1Values.includes(value.q1) ||
          !q2Values.includes(value.q2)) {{
        return false;
      }}
      if (value.q1 === "" && value.q2 !== "") {{
        return false;
      }}
      if (value.q1 === "no" && value.q2 !== "n-a") {{
        return false;
      }}
      if ((value.q1 === "yes" || value.q1 === "partially") &&
          value.q2 !== "" && value.q2 !== "yes" && value.q2 !== "no") {{
        return false;
      }}
      return true;
    }}

    function showStorageWarning() {{
      draftWarning.textContent =
        "Draft storage is unavailable; changes remain in memory for this session only.";
    }}

    function loadRows() {{
      const freshRows = payload.rows.map(blankRow);
      let stored;
      try {{
        stored = localStorage.getItem(STORAGE_KEY);
      }} catch (error) {{
        showStorageWarning();
        return freshRows;
      }}
      if (stored === null) {{
        return freshRows;
      }}
      try {{
        const draft = JSON.parse(stored);
        if (!exactKeys(draft, ["sourceSha256", "role", "rows"]) ||
            draft.sourceSha256 !== payload.source_sha256 ||
            draft.role !== payload.role ||
            !Array.isArray(draft.rows) ||
            draft.rows.length !== payload.rows.length ||
            !draft.rows.every((row, index) =>
              validDraftRow(row, payload.rows[index])
            )) {{
          throw new Error("invalid draft");
        }}
        return draft.rows;
      }} catch (error) {{
        draftWarning.textContent =
          "A stale or invalid draft was ignored; no values were migrated.";
        return freshRows;
      }}
    }}

    const rows = loadRows();
    let currentTurnIndex = 0;
    let reviewValidated = false;

    function saveDraft() {{
      try {{
        localStorage.setItem(STORAGE_KEY, JSON.stringify({{
          sourceSha256: payload.source_sha256,
          role: payload.role,
          rows: rows
        }}));
      }} catch (error) {{
        showStorageWarning();
      }}
    }}

    function checkedValue(name) {{
      const checked = document.querySelector(
        'input[name="' + name + '"]:checked'
      );
      return checked === null ? "" : checked.value;
    }}

    function setCheckedValue(name, value) {{
      document.querySelectorAll('input[name="' + name + '"]').forEach(input => {{
        input.checked = input.value === value;
      }});
    }}

    function setQr2Visibility(row) {{
      const required = row.q1 === "yes" || row.q1 === "partially";
      qr2Options.hidden = !required;
      setCheckedValue("qr2", required ? row.q2 : "");
    }}

    function captureVisibleFields() {{
      const turn = turns[currentTurnIndex];
      const row = rows[turn.rowIndex];
      const turnState = checkedValue("turn-state");
      row.turnStates[turn.turnOffset] = turnState === "" ? null : turnState;
      row.confidence = confidence.value;
      row.notes = notes.value;
      row.q1 = checkedValue("qr1");
      if (row.q1 === "no") {{
        row.q2 = "n-a";
      }} else if (row.q1 === "yes" || row.q1 === "partially") {{
        row.q2 = checkedValue("qr2");
      }} else {{
        row.q2 = "";
      }}
    }}

    function setReviewValidated(value) {{
      reviewValidated = value;
      exportButton.disabled = !reviewValidated;
    }}

    function invalidateReview() {{
      setReviewValidated(false);
    }}

    function captureAndPersist() {{
      captureVisibleFields();
      invalidateReview();
      saveDraft();
    }}

    function validateCurrentTurn() {{
      const turn = turns[currentTurnIndex];
      const row = rows[turn.rowIndex];
      if (!sourceTurnStates.includes(row.turnStates[turn.turnOffset])) {{
        return "Turn state is required.";
      }}
      if (!confidenceValues.slice(1).includes(row.confidence)) {{
        return "Confidence is required.";
      }}
      if (!q1Values.slice(1).includes(row.q1)) {{
        return "Q-R1 is required.";
      }}
      if ((row.q1 === "yes" || row.q1 === "partially") &&
          (row.q2 !== "yes" && row.q2 !== "no")) {{
        return "Q-R2 is required when Q-R1 is yes or partially.";
      }}
      return "";
    }}

    function validateRow(row) {{
      if (!row.turnStates.every(state => sourceTurnStates.includes(state))) {{
        return "Every turn state is required.";
      }}
      if (!confidenceValues.slice(1).includes(row.confidence)) {{
        return "Confidence is required.";
      }}
      if (!q1Values.slice(1).includes(row.q1)) {{
        return "Q-R1 is required.";
      }}
      if ((row.q1 === "yes" || row.q1 === "partially") &&
          (row.q2 !== "yes" && row.q2 !== "no")) {{
        return "Q-R2 is required when Q-R1 is yes or partially.";
      }}
      if (row.q1 === "no" && row.q2 !== "n-a") {{
        return "Q-R2 must be n-a when Q-R1 is no.";
      }}
      return "";
    }}

    function csvCell(value) {{
      const text = value === null || value === undefined ? "" : String(value);
      const escaped = text.replace(/"/g, '""');
      return /[,"\\r\\n]/.test(text) ? '"' + escaped + '"' : escaped;
    }}

    function buildCsv() {{
      const csvRows = [sourceHeader];
      sourceRows.forEach((sourceRow, index) => {{
        const row = rows[index];
        csvRows.push([
          sourceRow.unit_id,
          sourceRow.design,
          sourceRow.context_and_response,
          JSON.stringify(row.turnStates),
          row.confidence,
          row.notes,
          row.q1,
          row.q1 === "no" ? "n-a" : row.q2
        ]);
      }});
      return csvRows.map(row => row.map(csvCell).join(",")).join("\\r\\n") +
        "\\r\\n";
    }}

    function downloadText(filename, text, mime) {{
      let objectUrl = null;
      let anchor = null;
      const cleanup = () => {{
        if (objectUrl !== null) {{
          try {{
            URL.revokeObjectURL(objectUrl);
          }} catch (error) {{
            // Cleanup must not surface a secondary page error.
          }}
          objectUrl = null;
        }}
        if (anchor !== null && anchor.isConnected) {{
          anchor.remove();
        }}
      }};
      try {{
        const blob = new Blob([text], {{type: mime}});
        objectUrl = URL.createObjectURL(blob);
        anchor = document.createElement("a");
        anchor.href = objectUrl;
        anchor.download = filename;
        document.body.append(anchor);
        anchor.click();
        window.setTimeout(cleanup, 1000);
      }} catch (error) {{
        cleanup();
        throw error;
      }}
    }}

    function sourceRowMatchesPayload(index) {{
      const sourceRow = sourceRows[index];
      const payloadRow = payload.rows[index];
      return exactKeys(
        payloadRow,
        ["unit_id", "design", "context_and_response", "turns"]
      ) &&
        payloadRow.unit_id === sourceRow.unit_id &&
        payloadRow.design === sourceRow.design &&
        payloadRow.context_and_response === sourceRow.context_and_response &&
        Array.isArray(payloadRow.turns) &&
        payloadRow.turns.length === sourceRow.turns.length &&
        payloadRow.turns.every(
          (turn, turnIndex) => turn === sourceRow.turns[turnIndex]
        );
    }}

    function validateDownload() {{
      if (!reviewValidated || reviewScreen.hidden || !labelScreen.hidden) {{
        return "Download blocked: a fresh validated review is required.";
      }}
      if (!Array.isArray(payload.header) ||
          payload.header.length !== sourceHeader.length ||
          !payload.header.every(
            (fieldname, index) => fieldname === sourceHeader[index]
          )) {{
        return "Download blocked: embedded header changed.";
      }}
      if (!Array.isArray(payload.turn_states) ||
          payload.turn_states.length !== sourceTurnStates.length ||
          !payload.turn_states.every(
            (state, index) => state === sourceTurnStates[index]
          )) {{
        return "Download blocked: embedded turn-state vocabulary changed.";
      }}
      if (payload.role !== sourceRole ||
          !Array.isArray(payload.rows) ||
          payload.rows.length !== sourceRows.length) {{
        return "Download blocked: embedded source structure changed.";
      }}
      const changedSourceIndex = sourceRows.findIndex(
        (sourceRow, index) => !sourceRowMatchesPayload(index)
      );
      if (changedSourceIndex !== -1) {{
        return "Download blocked: source-bound fields changed at row " +
          (changedSourceIndex + 1) + ".";
      }}
      if (!Array.isArray(rows) || rows.length !== sourceRows.length) {{
        return "Download blocked: draft row structure changed.";
      }}
      const rowErrors = rows.map((row, index) => {{
        if (!exactKeys(
          row,
          ["turnStates", "confidence", "notes", "q1", "q2"]
        ) ||
            !Array.isArray(row.turnStates) ||
            row.turnStates.length !== sourceRows[index].turns.length ||
            typeof row.notes !== "string") {{
          return "Download blocked: draft row structure changed at row " +
            (index + 1) + ".";
        }}
        const validationError = validateRow(row);
        return validationError === ""
          ? ""
          : "Download blocked at row " + (index + 1) + ": " + validationError;
      }});
      return rowErrors.find(message => message !== "") || "";
    }}

    function blockDownload(message) {{
      setReviewValidated(false);
      errorMessage.textContent = message;
    }}

    function exportCsv() {{
      let csvText;
      try {{
        const validationError = validateDownload();
        if (validationError !== "") {{
          blockDownload(validationError);
          return;
        }}
        csvText = buildCsv();
      }} catch (error) {{
        blockDownload("Download blocked: validation failed unexpectedly.");
        return;
      }}
      const filename = sourceRole === "primary"
        ? "02-twomasters-partA-primary-completed.csv"
        : "02-twomasters-partA-reliability-completed.csv";
      errorMessage.textContent = "";
      try {{
        downloadText(filename, csvText, "text/csv;charset=utf-8");
      }} catch (error) {{
        blockDownload(
          "Download failed: browser could not prepare the CSV download."
        );
      }}
    }}

    function renderTurn() {{
      const turn = turns[currentTurnIndex];
      const row = rows[turn.rowIndex];
      labelScreen.hidden = false;
      reviewScreen.hidden = true;
      errorMessage.textContent = "";
      turnProgress.textContent =
        "Turn " + (currentTurnIndex + 1) + " of " + turns.length;
      unitProgress.textContent =
        "Unit " + (turn.rowIndex + 1) + " of " + payload.rows.length;
      responseText.textContent = turn.text;
      setCheckedValue("turn-state", row.turnStates[turn.turnOffset]);
      confidence.value = row.confidence;
      notes.value = row.notes;
      setCheckedValue("qr1", row.q1);
      setQr2Visibility(row);
      previousButton.disabled = currentTurnIndex === 0;
      invalidateReview();
    }}

    function renderReview() {{
      labelScreen.hidden = true;
      reviewScreen.hidden = false;
      previousButton.disabled = false;
      reviewScreen.replaceChildren();
      const heading = document.createElement("h2");
      heading.textContent = "Review completed labels";
      heading.tabIndex = -1;
      const summary = document.createElement("p");
      summary.textContent =
        payload.rows.length + " units and " + turns.length + " turns completed.";
      reviewScreen.append(heading, summary);
      errorMessage.textContent = "";
      setReviewValidated(true);
      heading.focus();
    }}

    function goNext() {{
      captureAndPersist();
      const validationError = validateCurrentTurn();
      if (validationError !== "") {{
        errorMessage.textContent = validationError;
        return;
      }}
      if (currentTurnIndex < turns.length - 1) {{
        currentTurnIndex += 1;
        renderTurn();
        return;
      }}
      const firstInvalid = rows.map(validateRow).find(message => message !== "");
      if (firstInvalid !== undefined) {{
        errorMessage.textContent = firstInvalid;
        return;
      }}
      renderReview();
    }}

    function goPrevious() {{
      if (!reviewScreen.hidden) {{
        renderTurn();
        return;
      }}
      captureAndPersist();
      if (currentTurnIndex > 0) {{
        currentTurnIndex -= 1;
      }}
      renderTurn();
    }}

    confidenceValues.forEach(value => {{
      const option = document.createElement("option");
      option.value = value;
      option.textContent = value;
      confidence.append(option);
    }});
    document.getElementById("role-boundary").textContent =
      payload.role === "primary"
        ? "Primary labeling draft"
        : "Independent reliability draft";
    document.querySelectorAll('input[name="qr1"]').forEach(input => {{
      input.addEventListener("change", () => {{
        const row = rows[turns[currentTurnIndex].rowIndex];
        const priorQ1 = row.q1;
        row.q1 = checkedValue("qr1");
        if (row.q1 === "no") {{
          row.q2 = "n-a";
        }} else if (priorQ1 === "no" || row.q2 === "n-a") {{
          row.q2 = "";
        }}
        setQr2Visibility(row);
      }});
    }});
    labelScreen.querySelectorAll("input, select, textarea").forEach(control => {{
      control.addEventListener("input", invalidateReview);
      control.addEventListener("change", invalidateReview);
    }});
    previousButton.addEventListener("click", goPrevious);
    nextButton.addEventListener("click", goNext);
    exportButton.addEventListener("click", exportCsv);
    renderTurn();
  </script>
</body>
</html>"""


FINALIZATION_PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Design 02 labeling finalization</title>
  <style>
    :root { color-scheme: light dark; font-family: system-ui, sans-serif; }
    body { margin: 0; line-height: 1.5; }
    main { box-sizing: border-box; margin: 0 auto; max-width: 52rem; padding: 1.25rem; }
    label { display: block; font-weight: 700; margin-block: 1rem 0.25rem; }
    button { margin-block: 1rem; }
    [data-testid="disagreement-row"] { border: 2px solid currentColor; margin-block: 0.75rem; padding: 0.75rem; }
    [role="alert"] { font-weight: 700; }
    :focus-visible { outline: 3px solid currentColor; outline-offset: 3px; }
  </style>
</head>
<body>
  <main>
    <h1>Design 02 labeling finalization</h1>
    <label for="primary-file">Completed primary CSV</label>
    <input id="primary-file" type="file" accept=".csv,text/csv">
    <label for="reliability-file">Completed reliability CSV</label>
    <input id="reliability-file" type="file" accept=".csv,text/csv">
    <button data-testid="validate-imports" type="button">Validate files</button>
    <p data-testid="import-status" role="status"></p>
    <section id="disagreements" aria-live="polite"></section>
    <button data-testid="export-declaration" type="button" disabled>Export declaration</button>
    <button data-testid="export-adjudications" type="button" disabled>Export adjudications</button>
    <p data-testid="error" role="alert"></p>
  </main>
  <script>
    const DATA_B64 = __DATA_B64__;
    const payloadBytes = Uint8Array.from(
      atob(DATA_B64), character => character.charCodeAt(0)
    );
    const payload = JSON.parse(new TextDecoder().decode(payloadBytes));
    const HEADER = Object.freeze(payload.header.slice());
    const TURN_STATES = Object.freeze(payload.turn_states.slice());

    function freezeExpected(instrument) {
      return Object.freeze({
        source_sha256: instrument.source_sha256,
        turn_counts: Object.freeze(instrument.turn_counts.slice()),
        rows: Object.freeze(instrument.rows.map(row => Object.freeze({
          unit_id: row.unit_id,
          design: row.design,
          context_and_response: row.context_and_response
        })))
      });
    }

    const expectedPrimary = freezeExpected(payload.primary);
    const expectedReliability = freezeExpected(payload.reliability);
    const primaryFile = document.getElementById("primary-file");
    const reliabilityFile = document.getElementById("reliability-file");
    const disagreementSection = document.getElementById("disagreements");
    const errorMessage = document.querySelector('[data-testid="error"]');
    const importStatus = document.querySelector(
      '[data-testid="import-status"]'
    );
    const declarationButton = document.querySelector(
      '[data-testid="export-declaration"]'
    );
    const adjudicationsButton = document.querySelector(
      '[data-testid="export-adjudications"]'
    );
    let validatedPrimary = null;
    let validatedReliability = null;
    let currentDisagreements = [];
    let validationEpoch = 0;

    function parseCsv(text, role) {
      if (typeof text !== "string") {
        throw new Error(role + " CSV read did not return text.");
      }
      const records = [];
      let record = [];
      let field = "";
      let inQuotes = false;
      let closedQuote = false;

      function finishField() {
        record.push(field);
        field = "";
        closedQuote = false;
      }

      function finishRecord() {
        finishField();
        if (record.every(value => value === "")) {
          throw new Error(role + " CSV contains a blank spurious row.");
        }
        records.push(record);
        record = [];
      }

      for (let index = 0; index < text.length; index += 1) {
        const character = text[index];
        if (inQuotes) {
          if (character === '"') {
            if (text[index + 1] === '"') {
              field += '"';
              index += 1;
            } else {
              inQuotes = false;
              closedQuote = true;
            }
          } else {
            field += character;
          }
          continue;
        }

        if (closedQuote) {
          if (character === ",") {
            finishField();
          } else if (character === "\\r" || character === "\\n") {
            finishRecord();
            if (character === "\\r" && text[index + 1] === "\\n") {
              index += 1;
            }
          } else {
            throw new Error(role + " CSV contains post-quote junk.");
          }
        } else if (character === '"') {
          if (field !== "") {
            throw new Error(role + " CSV contains a stray quote character.");
          }
          inQuotes = true;
        } else if (character === ",") {
          finishField();
        } else if (character === "\\r" || character === "\\n") {
          finishRecord();
          if (character === "\\r" && text[index + 1] === "\\n") {
            index += 1;
          }
        } else {
          field += character;
        }
      }

      if (inQuotes) {
        throw new Error(role + " CSV has an unclosed quoted field.");
      }
      if (closedQuote || field !== "" || record.length !== 0) {
        finishRecord();
      }
      if (records.length === 0) {
        throw new Error(role + " CSV is empty.");
      }
      const width = records[0].length;
      const inconsistentIndex = records.findIndex(
        recordValue => recordValue.length !== width
      );
      if (inconsistentIndex !== -1) {
        throw new Error(
          role + " CSV has inconsistent column count at row " +
          (inconsistentIndex + 1) + "."
        );
      }
      return {header: records[0], rows: records.slice(1)};
    }

    function validateHeader(actual, role) {
      if (actual.length !== HEADER.length ||
          !actual.every((fieldname, index) => fieldname === HEADER[index])) {
        throw new Error(role + " header mismatch: expected exact frozen header.");
      }
    }

    function validateImported(
      rows, expectedRows, expectedTurnCounts, role
    ) {
      if (rows.length !== expectedRows.length) {
        throw new Error(
          role + " row count mismatch: expected " + expectedRows.length +
          ", got " + rows.length + "."
        );
      }
      return rows.map((cells, index) => {
        const row = Object.fromEntries(
          HEADER.map((fieldname, fieldIndex) => [fieldname, cells[fieldIndex]])
        );
        const expected = expectedRows[index];
        if (row.unit_id !== expected.unit_id ||
            row.design !== expected.design ||
            row.context_and_response !== expected.context_and_response) {
          throw new Error(
            role + " identity/order mismatch at row " + (index + 1) + "."
          );
        }

        let states;
        try {
          states = JSON.parse(row.turn_state);
        } catch (error) {
          throw new Error(
            role + " turn_state JSON is invalid at row " + (index + 1) + "."
          );
        }
        if (!Array.isArray(states) ||
            states.length !== expectedTurnCounts[index] ||
            !states.every(state => TURN_STATES.includes(state))) {
          throw new Error(
            role + " turn_state is invalid at row " + (index + 1) + "."
          );
        }
        if (!["1", "2", "3"].includes(row.confidence_1_3)) {
          throw new Error(
            role + " confidence is invalid at row " + (index + 1) + "."
          );
        }
        const q1 = row["Q-R1_declines"];
        if (!["yes", "partially", "no"].includes(q1)) {
          throw new Error(
            role + " Q-R1 is invalid at row " + (index + 1) + "."
          );
        }
        const q2 = row["Q-R2_avoids_keyed_wrong"];
        if ((q1 === "no" && q2 !== "n-a") ||
            (q1 !== "no" && !["yes", "no"].includes(q2))) {
          throw new Error(
            role + " Q-R2 is invalid at row " + (index + 1) + "."
          );
        }
        return Object.assign({}, row, {states: states});
      });
    }

    function computeDisagreements(primaryRows, reliabilityRows) {
      const differences = [];
      reliabilityRows.forEach((reliabilityRow, rowIndex) => {
        reliabilityRow.states.forEach((reliabilityValue, turnOffset) => {
          const primaryValue = primaryRows[rowIndex].states[turnOffset];
          if (primaryValue !== reliabilityValue) {
            differences.push({
              unit_id: reliabilityRow.unit_id,
              category: "turn_state",
              member: turnOffset + 1,
              primary_value: primaryValue,
              reliability_value: reliabilityValue
            });
          }
        });
      });
      return differences;
    }

    function renderDisagreements(differences) {
      disagreementSection.replaceChildren();
      differences.forEach(difference => {
        const row = document.createElement("article");
        row.dataset.testid = "disagreement-row";
        row.dataset.unitId = difference.unit_id;
        row.dataset.member = String(difference.member);
        row.dataset.primaryValue = difference.primary_value;
        row.dataset.reliabilityValue = difference.reliability_value;
        const heading = document.createElement("h2");
        heading.textContent = difference.unit_id + " — Turn " + difference.member;
        const values = document.createElement("p");
        values.textContent =
          "Primary: " + difference.primary_value +
          " · Reliability: " + difference.reliability_value;
        row.append(heading, values);
        disagreementSection.append(row);
      });
    }

    function clearTrustedState(message) {
      validatedPrimary = null;
      validatedReliability = null;
      currentDisagreements = [];
      disagreementSection.replaceChildren();
      declarationButton.disabled = true;
      adjudicationsButton.disabled = true;
      errorMessage.textContent = message;
      importStatus.textContent = "";
    }

    async function readSelectedFile(file, role) {
      try {
        return await file.text();
      } catch (error) {
        throw new Error(role + " file could not be read.");
      }
    }

    function validationIsCurrent(epoch, primarySelection, reliabilitySelection) {
      return validationEpoch === epoch &&
        primaryFile.files[0] === primarySelection &&
        reliabilityFile.files[0] === reliabilitySelection;
    }

    function revokeImportedState() {
      validationEpoch += 1;
      clearTrustedState("");
    }

    async function validateFiles() {
      validationEpoch += 1;
      const epoch = validationEpoch;
      clearTrustedState("");
      const primarySelection = primaryFile.files[0];
      const reliabilitySelection = reliabilityFile.files[0];
      if (primarySelection === undefined || reliabilitySelection === undefined) {
        if (validationIsCurrent(
          epoch, primarySelection, reliabilitySelection
        )) {
          clearTrustedState("Select both completed CSV files.");
        }
        return;
      }

      try {
        const primaryText = await readSelectedFile(
          primarySelection, "Primary"
        );
        if (!validationIsCurrent(
          epoch, primarySelection, reliabilitySelection
        )) {
          return;
        }
        const reliabilityText = await readSelectedFile(
          reliabilitySelection, "Reliability"
        );
        if (!validationIsCurrent(
          epoch, primarySelection, reliabilitySelection
        )) {
          return;
        }
        const parsedPrimary = parseCsv(primaryText, "Primary");
        const parsedReliability = parseCsv(
          reliabilityText, "Reliability"
        );
        validateHeader(parsedPrimary.header, "Primary");
        validateHeader(parsedReliability.header, "Reliability");
        const candidatePrimary = validateImported(
          parsedPrimary.rows,
          expectedPrimary.rows,
          expectedPrimary.turn_counts,
          "Primary"
        );
        const candidateReliability = validateImported(
          parsedReliability.rows,
          expectedReliability.rows,
          expectedReliability.turn_counts,
          "Reliability"
        );
        const candidateDifferences = computeDisagreements(
          candidatePrimary, candidateReliability
        );
        if (!validationIsCurrent(
          epoch, primarySelection, reliabilitySelection
        )) {
          return;
        }
        validatedPrimary = candidatePrimary;
        validatedReliability = candidateReliability;
        currentDisagreements = candidateDifferences;
        errorMessage.textContent = "";
        renderDisagreements(currentDisagreements);
        importStatus.textContent =
          "Validated primary: " + candidatePrimary.length +
          " rows; reliability: " + candidateReliability.length +
          " rows; disagreements: " + candidateDifferences.length + ".";
      } catch (error) {
        if (!validationIsCurrent(
          epoch, primarySelection, reliabilitySelection
        )) {
          return;
        }
        clearTrustedState(
          error instanceof Error
            ? error.message
            : "CSV import validation failed unexpectedly."
        );
      }
    }

    document.querySelector('[data-testid="validate-imports"]').addEventListener(
      "click", validateFiles
    );
    primaryFile.addEventListener("change", revokeImportedState);
    reliabilityFile.addEventListener("change", revokeImportedState);
  </script>
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


def _finalization_payload(bundle: InstrumentBundle) -> str:
    def instrument_payload(instrument: Instrument) -> dict:
        return {
            "rows": [
                {
                    "context_and_response": row.context_and_response,
                    "design": row.design,
                    "unit_id": row.unit_id,
                }
                for row in instrument.rows
            ],
            "source_sha256": instrument.sha256,
            "turn_counts": [len(row.turns) for row in instrument.rows],
        }

    payload = {
        "header": list(HEADER),
        "primary": instrument_payload(bundle.primary),
        "reliability": instrument_payload(bundle.reliability),
        "schema_version": "walkworthy-design02-finalizer-v1",
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
    return FINALIZATION_PAGE_TEMPLATE.replace(
        "__DATA_B64__", json.dumps(_finalization_payload(bundle))
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
