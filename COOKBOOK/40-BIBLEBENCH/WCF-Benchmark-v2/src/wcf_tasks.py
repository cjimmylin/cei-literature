"""WCF-Benchmark-v2 — Inspect AI tasks (EXPLORATORY).

Two tasks over the ported v1 item bank:

    wcf_main      — 204 single-completion items across 9 designs
    wcf_episodes  — 22 NARROWGATE episodes via the scripted_dialogue solver

Scoring (simplest viable, user-locked): every item is graded by a fixed
separate grader model via model_graded_qa against the item's gold key +
weighted rubric, on a 0-100 scale (grader sums earned rubric points and
normalizes). Reported metrics are therefore MEANS ON A 0-100 SCALE, not
accuracies. The grader must be cross-family from the model under test —
enforced by convention at run time, not by code.

Run (from the v2 root, .venv-v2 active or via its bin/python):

    inspect eval src/wcf_tasks.py@wcf_main --model mockllm/model \
        -T grader_model=mockllm/model --limit 5
    inspect eval src/wcf_tasks.py@wcf_main --model openrouter/<vendor>/<sut> \
        -T grader_model=openrouter/<other-vendor>/<grader> --limit 15
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

from inspect_ai import Task, task
from inspect_ai.dataset import Sample, json_dataset
from inspect_ai.model import GenerateConfig, get_model
from inspect_ai.scorer import grouped, mean, model_graded_qa, multi_scorer, stderr
from inspect_ai.solver import generate, system_message

WCF_V2_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WCF_V2_ROOT / "src"))

from episode_solver import scripted_dialogue  # noqa: E402
from prompt_frames import (  # noqa: E402
    ANCHOR_ASK,
    EXAMINEE_SYSTEM,
    RANKING_ASK,
    TRACK_A_FRAME,
    TRACK_B_FRAME,
)
from wcf_grading import (  # noqa: E402
    GRADE_PATTERN,
    bounded_grader,
    panel_median,
)

logger = logging.getLogger(__name__)

DATA_DIR = WCF_V2_ROOT / "data"
TEMPLATE_DIR = WCF_V2_ROOT / "src" / "templates"
# Main (single-completion) template labels the response "[BEGIN MODEL RESPONSE]";
# the episode template (include_history=True) labels the history "[BEGIN TRANSCRIPT]"
# and flags the final-turn duplication so graders don't double-weight it (GP-10).
GRADE_TEMPLATE = (TEMPLATE_DIR / "wcf_grade_template.txt").read_text()
GRADE_TEMPLATE_EPISODE = (TEMPLATE_DIR / "wcf_grade_template_episode.txt").read_text()
GRADE_INSTRUCTIONS = (TEMPLATE_DIR / "wcf_grade_instructions.txt").read_text()
# GRADE_PATTERN is imported from wcf_grading (last-match, word-bounded, no digit
# truncation). Kept as a module attribute for backward compatibility.

# A rendered grading standard longer than this is probably an authoring or
# rendering bug; warn (never truncate — a truncated rubric corrupts scoring).
TARGET_WARN_CHARS = 6000

# v2.1 default: 3-grader median panel (session-3 Stream B: single-grader MAD vs
# alternates exceeded the pre-set 10-point instability threshold; ranking was
# stable but absolute levels carry a grader-of-choice offset). Reproduce the
# session-2 single-grader config with -T grader_model=openrouter/google/gemini-2.5-flash.
DEFAULT_GRADER = (
    "openrouter/google/gemini-2.5-flash"
    ",openrouter/deepseek/deepseek-chat"
    ",openrouter/mistralai/mistral-small-2603"
)


def render_standard(record: dict) -> str:
    """Build the grading standard ({criterion}) from key + gold_order + rubric.

    Deliberately excludes the standalone ``anchors`` list, ``difficulty_reservoir``
    and ``failure_notes`` — they roughly double prompt size and are not needed to
    grade (rubric entries carry their own anchor text where it matters).
    """
    parts = ["GOLD KEY:", record["key"].rstrip()]
    if record.get("gold_order"):
        parts.append(
            "GOLD ORDER (least to most heinous): " + " < ".join(record["gold_order"])
        )
    rubric_lines = ["SCORING RUBRIC (criteria with point weights):"]
    for entry in record["rubric"]:
        line = f"- ({entry.get('points')} pts) {str(entry.get('criterion', '')).strip()}"
        if entry.get("anchor"):
            line += f" [anchor: {str(entry['anchor']).strip()}]"
        if entry.get("axis"):
            line += f" [axis: {entry['axis']}]"
        rubric_lines.append(line)
    parts.append("\n".join(rubric_lines))
    standard = "\n\n".join(parts)
    if len(standard) > TARGET_WARN_CHARS:
        logger.warning(
            "grading standard for %s is %d chars (> %d)",
            record["id"], len(standard), TARGET_WARN_CHARS,
        )
    return standard


def record_to_sample(record: dict) -> Sample:
    frame = TRACK_A_FRAME if record["track"] == "A" else TRACK_B_FRAME
    body = f"{frame}\n\n{record['stem'].rstrip()}"
    # Format asks mirror v1 promptbuilder: CONTESTED gets the SAME ranking ask
    # as ORDINAL so the prompt never betrays which item is the contested one.
    if record["kind"] in ("ordinal", "contested"):
        body += RANKING_ASK
    elif record["kind"] == "anchor":
        body += ANCHOR_ASK
    return Sample(
        id=record["id"],
        input=body,
        target=render_standard(record),
        metadata={
            "design": record["design"],
            "track": record["track"],
            "tier": record["tier"],
            "commandments": record["commandments"],
            "contested": record["contested"],
            "episode": record["episode"],
            "kind": record["kind"],
            # v2.1: per-item pressure turn (episodes only; absent on main items).
            # Consumed OPT-IN by scripted_dialogue when pressure_variant="item".
            "pressure_turn": record.get("pressure_turn"),
        },
    )


def wcf_scorer(grader_model: str, grader_temperature: float, include_history: bool):
    """``grader_model`` accepts comma-separated slugs; 2+ graders reduce by MEDIAN
    via the explicit ``panel_median`` reducer (NOT inspect's default mode/majority
    — grades are continuous 0-100 strings, so mode is degenerate; and NOT the
    ``model=[...]`` list form, which silently reduces by mode).

    Each grader is wrapped in ``bounded_grader`` which (a) defangs the WCF
    template's own structural markers in the SUT answer before grading so a SUT
    cannot forge a rubric block / close the response block early (GP-02), and
    (b) routes out-of-range or non-numeric grades to ``unscored`` rather than
    letting >100 inflate a mean or a non-numeric string coerce to 0.0 (GP-04/06).
    The ``panel_median`` reducer records ``metadata['panel']`` (effective panel
    size + each grader's parsed value) so degradation is visible and per-grader
    provenance survives without a re-run (GP-06/07)."""
    template = GRADE_TEMPLATE_EPISODE if include_history else GRADE_TEMPLATE
    # Inspect's -T parser splits a comma-separated CLI value into a list; a
    # Python caller / the DEFAULT_GRADER passes a single comma-joined string.
    # Accept both.
    if isinstance(grader_model, str):
        grader_model = grader_model.split(",")
    graders = [str(g).strip() for g in grader_model if str(g).strip()]
    scorers = [
        bounded_grader(
            model_graded_qa(
                template=template,
                instructions=GRADE_INSTRUCTIONS,
                grade_pattern=GRADE_PATTERN,
                include_history=include_history,
                model=get_model(
                    g, config=GenerateConfig(temperature=grader_temperature)
                ),
            )
        )
        for g in graders
    ]
    if len(scorers) == 1:
        return scorers[0]
    return multi_scorer(scorers, panel_median())


@task
def wcf_main(
    grader_model: str = DEFAULT_GRADER, grader_temperature: float = 0.0
) -> Task:
    return Task(
        dataset=json_dataset(str(DATA_DIR / "wcf_main.jsonl"), record_to_sample),
        solver=[system_message(EXAMINEE_SYSTEM), generate()],
        scorer=wcf_scorer(grader_model, grader_temperature, include_history=False),
        metrics=[
            mean(),
            stderr(),
            grouped(mean(), "design"),
            grouped(mean(), "tier"),
        ],
    )


@task
def wcf_episodes(
    grader_model: str = DEFAULT_GRADER,
    grader_temperature: float = 0.0,
    pressure_variant: str = "generic",
) -> Task:
    """NARROWGATE episodes.

    ``pressure_variant`` selects the second-turn pressure injection:
      - ``"generic"`` (default) reproduces the session-2 frozen config exactly;
      - ``"item"`` uses per-item pressure turns (v2.1).
    """
    return Task(
        dataset=json_dataset(str(DATA_DIR / "wcf_episodes.jsonl"), record_to_sample),
        solver=[
            system_message(EXAMINEE_SYSTEM),
            scripted_dialogue(pressure_variant=pressure_variant),
        ],
        scorer=wcf_scorer(grader_model, grader_temperature, include_history=True),
        # EP-04: episodes are all tier=T4/track=A, so grouped(mean(),"tier") is a
        # single vacuous cell — dropped. Keep overall mean/stderr only.
        metrics=[mean(), stderr()],
    )
