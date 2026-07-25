"""Session-15 Arm-A: build one self-contained STRICT-v2 judge packet per bench
cell, for BLIND grading by judge agents. NO API of any kind (no OpenRouter
calls; runs with OPENROUTER_API_KEY unset).

For each of the 17 cells in analysis/20260724-session15-truth-bench.json this
script:
  1. pulls the item's FULL key/stem/rubric from data/session13_new_items.json;
  2. pulls the FULL logged SUT response from logs/20260724-session13-gate-main/*.eval
     (qwen = openrouter/qwen/qwen3.7-plus; haiku = openrouter/anthropic/claude-
     haiku-4.5 — DISCOVERED from each .eval's model metadata, not the filename);
  3. renders the COMPLETE strict-v2 judge prompt for that (item, response) pair
     using the SAME machinery session14_calibration.py uses —
        answer    = neutralize_structural_delimiters(defang_wcf_markers(completion))
        question  = neutralize_structural_delimiters(sample.input_text)
        criterion = neutralize_structural_delimiters(render_standard(item))
        prompt    = GRADE_TEMPLATE_STRICT_V2.format(question=, answer=, criterion=,
                                                    instructions=GRADE_INSTRUCTIONS)
     — only the template object differs (v2 instead of s14 strict);
  4. writes it to analysis/20260724-session15-bench-packets/<ITEM>__<sut>.md.

CRITICAL ANTI-LEAKAGE RULE: each packet contains ONLY the rendered judge prompt
(item key + SUT response + grading instructions). It contains NO expected score,
band, audit verdict, class label, or any reference to the truth bench / the
audits. The packets are graded BLIND. The truth bench is read ONLY to enumerate
(item, sut) pairs — its `expected`/`band`/`class` fields are never written out.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

WCF_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WCF_ROOT / "src"))
sys.path.insert(0, str(WCF_ROOT / "analysis"))

from inspect_ai.log import read_eval_log  # noqa: E402
from inspect_ai.scorer._model import neutralize_structural_delimiters  # noqa: E402

# STRICT rendering machinery — reuse, do NOT fork. render_standard builds the
# {criterion}; GRADE_INSTRUCTIONS carries the terminal GRADE line. Only the
# template object is swapped for the hardened v2 file.
from wcf_tasks import render_standard, GRADE_INSTRUCTIONS  # noqa: E402
from wcf_grading import defang_wcf_markers  # noqa: E402

# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #
LOG_DIR = WCF_ROOT / "logs" / "20260724-session13-gate-main"
ITEMS_JSON = WCF_ROOT / "data" / "session13_new_items.json"
TRUTH_BENCH = WCF_ROOT / "analysis" / "20260724-session15-truth-bench.json"
TEMPLATE_V2 = WCF_ROOT / "src" / "templates" / "wcf_grade_template_strict_v2.txt"
OUT_DIR = WCF_ROOT / "analysis" / "20260724-session15-bench-packets"

# SUT model ids as recorded in the eval metadata (verified at runtime).
SUT_MODEL_ID = {
    "qwen": "openrouter/qwen/qwen3.7-plus",
    "haiku": "openrouter/anthropic/claude-haiku-4.5",
}

# Load the v2 template ONCE at import (so tests can reuse render_strict_v2_prompt).
GRADE_TEMPLATE_STRICT_V2 = TEMPLATE_V2.read_text()


# --------------------------------------------------------------------------- #
# Render the STRICT-v2 prompt exactly as the scorer path would (v2 template)
# --------------------------------------------------------------------------- #
def render_strict_v2_prompt(question: str, completion: str, criterion: str,
                            metadata: dict | None = None):
    """Return (prompt_text, defanged_answer_seen_by_judge).

    Mirrors session14_calibration.render_strict_prompt exactly, except the
    template is the hardened strict-v2 instrument:
      1. defang WCF markers in the SUT completion (bounded_grader step)
      2. inspect neutralize_structural_delimiters on answer/question/criterion
      3. template.format(question, answer, criterion, instructions, **metadata)
    """
    defanged = defang_wcf_markers(completion)
    answer = neutralize_structural_delimiters(defanged)
    q = neutralize_structural_delimiters(question)
    crit = neutralize_structural_delimiters(criterion)
    md = {k: v for k, v in (metadata or {}).items()
          if k not in ("question", "answer", "criterion", "instructions")}
    prompt = GRADE_TEMPLATE_STRICT_V2.format(
        question=q, answer=answer, criterion=crit,
        instructions=GRADE_INSTRUCTIONS, **md,
    )
    return prompt, answer


# --------------------------------------------------------------------------- #
# Discover which .eval file is which SUT (by model metadata, not filename)
# --------------------------------------------------------------------------- #
def discover_sut_logs() -> dict:
    """sut_key -> loaded {id -> {question, completion, criterion, metadata}}.

    Reads each *.eval in LOG_DIR, keys it by its recorded eval.model, and maps
    the two SUTs we need (qwen, haiku) from SUT_MODEL_ID. Any extra eval file
    (e.g. gpt-4o-mini) is ignored.
    """
    model_to_items = {}
    model_to_file = {}
    for f in sorted(LOG_DIR.glob("*.eval")):
        log = read_eval_log(str(f))
        model = getattr(log.eval, "model", None)
        model_to_file[model] = f.name
        items = {}
        for s in (log.samples or []):
            question = s.input if isinstance(s.input, str) else str(s.input)
            criterion = s.target if isinstance(s.target, str) else (
                "\n".join(s.target) if isinstance(s.target, list) else str(s.target))
            items[str(s.id)] = {
                "question": question,
                "completion": s.output.completion,
                "criterion_from_log": criterion,
                "metadata": dict(s.metadata or {}),
            }
        model_to_items[model] = items

    out = {}
    for sut_key, model_id in SUT_MODEL_ID.items():
        if model_id not in model_to_items:
            raise RuntimeError(
                f"SUT {sut_key} model {model_id!r} not found among eval models "
                f"{list(model_to_items)}")
        out[sut_key] = model_to_items[model_id]
        print(f"[discover] {sut_key} = {model_id}  (file {model_to_file[model_id]}, "
              f"{len(model_to_items[model_id])} samples)")
    return out


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    bench = json.loads(TRUTH_BENCH.read_text())
    cells = bench["cells"]  # enumerate (item, sut) ONLY — never expected/band/class
    items = {r["id"]: r for r in json.loads(ITEMS_JSON.read_text())}
    sut_logs = discover_sut_logs()

    written = []
    for cell in cells:
        iid = cell["item"]
        sut = cell["sut"]
        item = items.get(iid)
        if item is None:
            raise RuntimeError(f"item {iid} not in {ITEMS_JSON.name}")
        logmap = sut_logs.get(sut)
        if logmap is None:
            raise RuntimeError(f"no SUT log for {sut}")
        rec = logmap.get(iid)
        if rec is None:
            raise RuntimeError(f"{iid} missing from {sut} eval log")

        # criterion is built from the item KEY via render_standard (same as the
        # scorer/calibration path); the logged target corroborates but we render
        # fresh from the authoritative item file.
        criterion = render_standard(item)
        prompt, _answer_seen = render_strict_v2_prompt(
            rec["question"], rec["completion"], criterion, rec["metadata"])

        # Packet body is ONLY the rendered blind judge prompt — no bench fields.
        out_path = OUT_DIR / f"{iid}__{sut}.md"
        out_path.write_text(prompt)
        written.append((out_path, len(prompt.encode("utf-8"))))

    print(f"\nWrote {len(written)} packets to {OUT_DIR.relative_to(WCF_ROOT)}/")
    for p, nbytes in written:
        print(f"  {p.name}  {nbytes} bytes")


if __name__ == "__main__":
    main()
