"""Design 02 — Two Masters (break_turn). Scripted multi-turn ladder."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from inspect_ai import Task, task
from inspect_ai.model import GenerateConfig

from walkworthy_inspect.datasets import load_design
from walkworthy_inspect.metrics import break_turn
from walkworthy_inspect.scorers import DEFAULT_JUDGE, design02_scorer
from walkworthy_inspect.solvers import DEFAULT_MAX_TOKENS, multiturn_ladder_solver

DESIGN = "02-twomasters"


@task
def design02_twomasters(judge_model: str = DEFAULT_JUDGE,
                        dataset_dir: str | None = None) -> Task:
    return Task(
        dataset=load_design(DESIGN, dataset_dir=dataset_dir),
        # the classifier that picks ladder branches is the judge model; it degrades to
        # the v1 lexical heuristic under mockllm so mock validation completes.
        solver=multiturn_ladder_solver(classifier_model=judge_model,
                                       max_tokens=DEFAULT_MAX_TOKENS),
        scorer=design02_scorer(judge_model=judge_model),
        metrics=[break_turn()],
        config=GenerateConfig(max_tokens=DEFAULT_MAX_TOKENS),
        name="walkworthy_design02_twomasters",
    )
