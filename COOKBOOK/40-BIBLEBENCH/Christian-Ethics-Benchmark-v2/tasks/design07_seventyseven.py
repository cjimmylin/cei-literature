"""Design 07 — SeventySeven (arc_shape). Scripted multi-turn ladder."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from inspect_ai import Task, task
from inspect_ai.model import GenerateConfig

from walkworthy_inspect.datasets import load_design
from walkworthy_inspect.metrics import arc_shape
from walkworthy_inspect.scorers import DEFAULT_JUDGE, design07_scorer
from walkworthy_inspect.solvers import DEFAULT_MAX_TOKENS, multiturn_ladder_solver

DESIGN = "07-seventyseven"


@task
def design07_seventyseven(judge_model: str = DEFAULT_JUDGE,
                          dataset_dir: str | None = None,
                         item_ids: str | None = None) -> Task:
    return Task(
        dataset=load_design(DESIGN, dataset_dir=dataset_dir, item_ids=item_ids),
        solver=multiturn_ladder_solver(classifier_model=judge_model,
                                       max_tokens=DEFAULT_MAX_TOKENS),
        scorer=design07_scorer(judge_model=judge_model),
        metrics=[arc_shape()],
        config=GenerateConfig(max_tokens=DEFAULT_MAX_TOKENS),
        name="walkworthy_design07_seventyseven",
    )
